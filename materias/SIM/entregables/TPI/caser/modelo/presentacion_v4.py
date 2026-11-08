#!/usr/bin/env python3
"""Presentación v4 para la defensa (2026-11-08, IDE cerrado). Una sola vez sobre CaserHorno.alp.

Uso, desde la raíz del repo:
    .venv/Scripts/python.exe -I materias/SIM/entregables/TPI/caser/modelo/presentacion_v4.py

Rehace la presentación de Main (conserva el statechart, su marco y los bloques de la PML):
- Encabezado con fecha real (el modelo arranca el lunes 18/08/2025, primera semana de los datos) y escenario.
- Seis indicadores en tarjetas, calculados desde t = 0 aunque el modelo esté en su período de calentamiento.
- Planta: lavado (con la semana real sorteada) → cola (cada ULI pintada según cuánto lleva esperando y casilleros
  vacíos hasta el umbral) → horno (estado, barra de la fase, cinta, resistencias y termómetro ilustrativo) →
  salida; bloques de la PML en su propio panel, sin textos superpuestos.
- Cinta de tiempo del horno: los últimos 60 días, una franja por estado.
- Gráfico de la cola contra el umbral con fechas en el eje.
- Panel "¿Dónde se va la plata?": reparto del tiempo del horno por estado, costo acumulado (luz, gas y capital)
  y el costo de las horas caliente sin carga.
- Escenario E0-E3 elegible en vivo y botones de velocidad (1 día/s, 1 semana/s, rápido) y de reinicio.

Lógica: solo se AGREGAN acumuladores de presentación (vis*, hist*) y una llamada a acumularVis() al principio de
acumular() y de despachar(), más dos contadores en encender() y despachar(). No usan números aleatorios ni cambian
ninguna variable que lea la lógica: el CSV de CorridasE0E3 tiene que quedar idéntico (lo controla el verificador).
Experimento Visual: sin calentamiento, horizonte de 2 años, arranca a 1 día por segundo.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

ALP = Path(__file__).resolve().parent / "CaserHorno.alp"
s = ALP.read_text(encoding="utf-8")
if "<Name>acumularVis</Name>" in s:
    sys.exit("La presentación v4 ya está aplicada.")

_id = [1840000000000]


def nid():
    _id[0] += 1
    return str(_id[0])


def x(t):
    return escape(str(t))


def argb(h):
    v = int(h.lstrip("#"), 16) | 0xFF000000
    return str(v - (1 << 32))


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:120], s.count(a))
    s = s.replace(a, b)


# ---------------------------------------------------------------- paleta
INK, MUTED, LINE, PANEL, WHITE = "#1f2733", "#6b7480", "#d9dde3", "#f6f7f9", "#ffffff"
HEAD, HEAD2 = "#1d2b45", "#c9d3e3"
# Estados de presentación: 0 apagado, 1 acumulando, 2 calentando, 3 procesando, 4 caliente sin carga, 5 enfriando
EST_RGB = [(200, 204, 210), (240, 220, 130), (255, 165, 60), (235, 90, 50), (245, 150, 120), (150, 180, 230)]
EST_NOM = ["Apagado", "Acumulando", "Calentando", "Procesando", "Caliente sin carga", "Enfriando"]

COMMON = ("<Label><X>10</X><Y>0</Y></Label><PublicFlag>true</PublicFlag><PresentationFlag>true</PresentationFlag>"
          "<ShowLabel>false</ShowLabel><DrawMode>SHAPE_DRAW_2D3D</DrawMode>")


def dyn(**kw):
    """Propiedades dinámicas en el orden que usa el .alp."""
    out = ""
    for tag in ("XCode", "YCode", "VisibleCode"):
        if kw.get(tag):
            out += f"<{tag}>{x(kw[tag])}</{tag}>"
    if kw.get("rep"):
        out += f'<ReplicationCode Class="CodeValue"><Code>{x(kw["rep"])}</Code></ReplicationCode>'
    return out


def rect(name, X, Y, w, h, fill=None, line=LINE, lw=1, style="SOLID", fillcode=None, linecode=None,
         wcode=None, hcode=None, radius=None, **kw):
    tag = "RoundedRectangle" if radius else "Rectangle"
    f = f"<FillColor>{argb(fill)}</FillColor>" if fill else "<FillColor />"
    lc = f"<LineColor>{argb(line)}</LineColor>" if line else "<LineColor />"
    return (f"<{tag}><Id>{nid()}</Id><Name>{name}</Name><X>{int(X)}</X><Y>{int(Y)}</Y>{COMMON}{dyn(**kw)}"
            f"<EmbeddedIcon>false</EmbeddedIcon><Z>0</Z><ZHeight>10</ZHeight><LineWidth>{lw}</LineWidth>{lc}"
            + (f"<LineColorCode>{x(linecode)}</LineColorCode>" if linecode else "")
            + f"<LineMaterial>null</LineMaterial><LineStyle>{style}</LineStyle><Width>{int(w)}</Width>"
            + (f"<WidthCode>{x(wcode)}</WidthCode>" if wcode else "")
            + f"<Height>{h}</Height>"
            + (f"<HeightCode>{x(hcode)}</HeightCode>" if hcode else "")
            + f"<Rotation>0.0</Rotation>{f}"
            + (f"<FillColorCode>{x(fillcode)}</FillColorCode>" if fillcode else "")
            + "<FillMaterial>null</FillMaterial>"
            + (f"<ArcRadius>{radius}</ArcRadius>" if radius else "")
            + f"</{tag}>")


def text(name, X, Y, txt, color=INK, size=12, bold=False, align="LEFT", code=None, colorcode=None, **kw):
    return (f"<Text><Id>{nid()}</Id><Name>{name}</Name><X>{int(X)}</X><Y>{int(Y)}</Y>{COMMON}{dyn(**kw)}"
            f"<EmbeddedIcon>false</EmbeddedIcon><Z>0</Z><Rotation>0.0</Rotation><Color>{argb(color)}</Color>"
            + (f"<ColorCode>{x(colorcode)}</ColorCode>" if colorcode else "")
            + f"<Text>{x(txt)}</Text>"
            + (f"<TextCode>{x(code)}</TextCode>" if code else "")
            + f"<Font><Name>SansSerif</Name><Size>{size}</Size><Style>{1 if bold else 0}</Style></Font>"
            f"<Alignment>{align}</Alignment></Text>")


def line(name, X, Y, dx, dy, color=MUTED, lw=2, arrow=False):
    return (f"<Line><Id>{nid()}</Id><Name>{name}</Name><X>{int(X)}</X><Y>{int(Y)}</Y>{COMMON}"
            f"<EmbeddedIcon>false</EmbeddedIcon><Z>0</Z><ZHeight>10</ZHeight><LineWidth>{lw}</LineWidth>"
            f"<LineColor>{argb(color)}</LineColor><LineMaterial>null</LineMaterial><LineStyle>SOLID</LineStyle>"
            f"<BeginArrowSize>1</BeginArrowSize><BeginArrowStyle>0</BeginArrowStyle>"
            f"<EndArrowSize>{2 if arrow else 1}</EndArrowSize><EndArrowStyle>{1 if arrow else 0}</EndArrowStyle>"
            f"<Dx>{dx}</Dx><Dy>{dy}</Dy><Dz>0</Dz></Line>")


def button(name, X, Y, w, h, label, action, labelcode=None, size=11):
    return (f'<Control Type="Button"><EmbeddedIcon>false</EmbeddedIcon><Id>{nid()}</Id><Name>{name}</Name>'
            f"<X>{X}</X><Y>{Y}</Y><Label><X>0</X><Y>-10</Y></Label><PublicFlag>true</PublicFlag>"
            f"<PresentationFlag>true</PresentationFlag><ShowLabel>false</ShowLabel><DrawMode>SHAPE_DRAW_2D3D</DrawMode>"
            f'<BasicProperties Width="{w}" Height="{h}"><EmbeddedIcon>false</EmbeddedIcon><TextColor/>'
            f"<Enabled>true</Enabled><ActionCode>{x(action)}</ActionCode></BasicProperties>"
            f'<ExtendedProperties><Font Name="Dialog" Size="{size}" Style="1"/><LabelText>{x(label)}</LabelText>'
            + (f"<LabelCode>{x(labelcode)}</LabelCode>" if labelcode else "")
            + "</ExtendedProperties></Control>")


def radio(name, X, Y, w, h, opciones, action, default):
    bts = "".join(f"<Button>{x(o)}</Button>" for o in opciones)
    return (f'<Control Type="RadioButtons"><EmbeddedIcon>false</EmbeddedIcon><Id>{nid()}</Id><Name>{name}</Name>'
            f"<X>{X}</X><Y>{Y}</Y><Label><X>0</X><Y>-10</Y></Label><PublicFlag>true</PublicFlag>"
            f"<PresentationFlag>true</PresentationFlag><ShowLabel>false</ShowLabel><DrawMode>SHAPE_DRAW_2D3D</DrawMode>"
            f'<BasicProperties Width="{w}" Height="{h}"><EmbeddedIcon>false</EmbeddedIcon>'
            f"<TextColor>{argb(INK)}</TextColor><Enabled>true</Enabled><ActionCode>{x(action)}</ActionCode>"
            f'</BasicProperties><ExtendedProperties><Font Name="Dialog" Size="12" Style="0"/>'
            f"<DefaultValueCode>{x(default)}</DefaultValueCode><Orientation>HORIZONTAL</Orientation>{bts}"
            f"<LinkTo>false</LinkTo></ExtendedProperties></Control>")


# ---------------------------------------------------------------- 1. variables, funciones y ganchos en la lógica
VARS = [("visHoras", "double[]", "new double[6]"), ("visAreaKg", "double", "0"), ("visEncendidos", "int", "0"),
        ("visSumaEspera", "double", "0"), ("visNEspera", "int", "0"), ("tUltimoVis", "double", "0"),
        ("histEstado", "int[]", "new int[360]"), ("histIdx", "int", "0"), ("histTick", "int", "0"),
        ("visTratadas", "int", "0"), ("visKg", "double", "0"), ("kgSalidaTotal", "double", "0")]
xml_vars = ""
for k, (n, t, v) in enumerate(VARS):
    xml_vars += (f'<Variable Class="PlainVariable"><Id>{nid()}</Id><Name>{n}</Name><X>1400</X><Y>{1200 + 22 * k}</Y>'
                 f"<Label><X>10</X><Y>0</Y></Label><PublicFlag>false</PublicFlag><PresentationFlag>false</PresentationFlag>"
                 f'<ShowLabel>true</ShowLabel><Properties SaveInSnapshot="true" Constant="false" AccessType="public" '
                 f'StaticVariable="false"><Type>{x(t)}</Type><UnitType>NONE</UnitType><SdArray>false</SdArray>'
                 f'<InitialValue Class="CodeValue"><Code>{x(v)}</Code></InitialValue></Properties></Variable>')
i = s.index("</Variables>", s.index("<Name>Main</Name>"))
s = s[:i] + xml_vars + s[i:]

C_EST = ", ".join(f"new java.awt.Color({r}, {g}, {b})" for r, g, b in EST_RGB)
FUNCS = [
    ("estadoVis", "int", [],
     "if (estado == 0) return 0;\nif (estado == 1) return 1;\nif (estado == 2) return 2;\n"
     "if (estado == 3) return ocupado || !enVacio ? 3 : 4;\nreturn 5;"),
    ("acumularVis", "void", [],
     "// Solo presentación: tiempo por estado y área de kg en cola desde t = 0 (no depende del calentamiento).\n"
     "double t = time();\ndouble dt = t - tUltimoVis;\nvisHoras[estadoVis()] += dt;\nvisAreaKg += kgEnCola * dt;\ntUltimoVis = t;"),
    ("visHorasEstado", "double", [("k", "int")],
     "return visHoras[k] + (estadoVis() == k ? time() - tUltimoVis : 0);"),
    ("visHorasTotal", "double", [],
     "double h = 0;\nfor (int k = 0; k < 6; k++) h += visHorasEstado(k);\nreturn h;"),
    ("ordenEstado", "int", [("pos", "int")],
     "// Orden de la barra: lo que cuesta primero.\nint[] o = {3, 4, 2, 5, 1, 0};\nreturn o[pos];"),
    ("fracEstado", "double", [("k", "int")],
     "double h = visHorasTotal();\nreturn h <= 0 ? 0 : visHorasEstado(k) / h;"),
    ("fracAcumulada", "double", [("pos", "int")],
     "double f = 0;\nfor (int i = 0; i < pos; i++) f += fracEstado(ordenEstado(i));\nreturn f;"),
    ("colorEstado", "java.awt.Color", [("k", "int")],
     f"java.awt.Color[] c = {{{C_EST}}};\nreturn k < 0 ? new java.awt.Color(236, 238, 241) : c[k];"),
    ("colorHist", "java.awt.Color", [("i", "int")],
     "int v = histEstado[(histIdx + i) % histEstado.length];\nreturn colorEstado(v - 1);"),
    ("visHorasCaliente", "double", [], "return visHorasEstado(3) + visHorasEstado(4);"),
    ("visLuz", "double", [],
     "return (kWhPorEncendido * visEncendidos + kWhPorDiaCaliente / 24 * visHorasCaliente()) * tarifaKWh;"),
    ("visGas", "double", [], "return kgGLPPorDiaCaliente / 24 * visHorasCaliente() * precioGLPkg;"),
    ("visCapital", "double", [],
     "double area = visAreaKg + kgEnCola * (time() - tUltimoVis);\n"
     "return tasaCapitalMensual * area / (24 * 30.4375) * costoProductoKg;"),
    ("visTotal", "double", [], "return visLuz() + visGas() + visCapital();"),
    ("visDesperdicio", "double", [],
     "// Lo que cuesta tener el horno caliente sin carga: luz y gas de esas horas.\n"
     "return visHorasEstado(4) * (kWhPorDiaCaliente / 24 * tarifaKWh + kgGLPPorDiaCaliente / 24 * precioGLPkg);"),
    ("visEsperaMediaDias", "double", [], "return visNEspera == 0 ? 0 : visSumaEspera / visNEspera / 24;"),
    ("esperaMasViejaDias", "double", [], "return nEnCola == 0 ? 0 : (time() - llegadaMasVieja()) / 24;"),
    ("colorEdad", "java.awt.Color", [("tLleg", "double")],
     "double d = (time() - tLleg) / 24;\n"
     "if (d < 3) return new java.awt.Color(111, 191, 128);\n"
     "if (d < 7) return new java.awt.Color(242, 201, 76);\n"
     "if (d < 14) return new java.awt.Color(242, 153, 74);\n"
     "return new java.awt.Color(214, 69, 69);"),
    ("temperaturaHorno", "double", [],
     "// Ilustrativa: rampa lineal de 25 a 900 °C al calentar y de vuelta al enfriar.\n"
     "if (estado == 2) return 25 + 875 * Math.max(0, Math.min(1, 1 - eCalentamiento.getRest() / hCalentamiento));\n"
     "if (estado == 3) return 900;\n"
     "if (estado == 4) return 25 + 875 * Math.max(0, Math.min(1, eEnfriamiento.getRest() / hEnfriamiento));\n"
     "return 25;"),
    ("colorTemperatura", "java.awt.Color", [],
     "double f = (temperaturaHorno() - 25) / 875;\n"
     "return new java.awt.Color((int) (90 + 160 * f), (int) (90 - 40 * f), (int) (95 - 70 * f));"),
    ("progresoFase", "double", [],
     "if (estado == 2) return 1 - eCalentamiento.getRest() / Math.max(1e-9, hCalentamiento);\n"
     "if (estado == 4) return 1 - eEnfriamiento.getRest() / Math.max(1e-9, hEnfriamiento);\n"
     "if (estado == 3 && enVacio && horasEnVacio > 0) return 1 - eVacio.getRest() / horasEnVacio;\n"
     "if (estado == 1) return Math.min(1, nEnCola / (double) umbralULI);\nreturn 0;"),
    ("fechaTexto", "String", [],
     "// t = 0 es el lunes 18/08/2025, primera semana de los datos de lavado.\n"
     "java.time.LocalDate d = java.time.LocalDate.of(2025, 8, 18).plusDays((long) Math.floor(time() / 24));\n"
     "String f = d.format(java.time.format.DateTimeFormatter.ofPattern(\"EEEE d 'de' MMMM 'de' yyyy\", new java.util.Locale(\"es\", \"AR\")));\n"
     "return f.substring(0, 1).toUpperCase() + f.substring(1) + String.format(\"  ·  %02d:00 h\", (int) Math.floor(time() % 24));"),
    ("plata", "String", [("pesos", "double")],
     "return String.format(new java.util.Locale(\"es\", \"AR\"), \"$ %.1f M\", pesos / 1e6);"),
    ("descEscenario", "String", [],
     "String e = escenario.equals(\"E1\") ? \"umbral bajo\" : escenario.equals(\"E2\") ? \"umbral con espera máxima\""
     " : escenario.equals(\"E3\") ? \"apagar apenas se vacía la cola\" : \"regla actual\";\n"
     "return \"Escenario \" + escenario + \" · \" + e + \":  enciende con \" + umbralULI + \" ULI  ·  \""
     " + (Double.isInfinite(esperaMaxDias) ? \"sin espera máxima\" : \"o si la más vieja lleva \" + (int) esperaMaxDias + \" días\")"
     " + \"  ·  \" + (horasEnVacio > 0 ? \"caliente sin carga hasta \" + (int) horasEnVacio + \" h\" : \"se apaga apenas se vacía la cola\");"),
    ("escenarioIndice", "int", [],
     "return escenario.equals(\"E1\") ? 1 : escenario.equals(\"E2\") ? 2 : escenario.equals(\"E3\") ? 3 : 0;"),
    ("resetVis", "void", [],
     "acumularVis();\nfor (int k = 0; k < 6; k++) visHoras[k] = 0;\n"
     "visAreaKg = 0; visEncendidos = 0; visSumaEspera = 0; visNEspera = 0; visTratadas = 0; visKg = 0;"),
    ("cambiarEscenario", "void", [("v", "int")],
     "// Solo para la animación: cambia la regla en vivo y reinicia los contadores de presentación.\n"
     "acumularVis();\n"
     "escenario = v == 1 ? \"E1\" : v == 2 ? \"E2\" : v == 3 ? \"E3\" : \"E0\";\n"
     "umbralULI = v == 1 ? 45 : 79;\n"
     "esperaMaxDias = v == 2 ? 15 : Double.POSITIVE_INFINITY;\n"
     "horasEnVacio = v == 3 ? 0 : 48;\n"
     "if (estado == 1) {\n"
     "    if (Double.isInfinite(esperaMaxDias)) eEsperaMax.reset();\n"
     "    else eEsperaMax.restart(Math.max(0, esperaMaxDias * 24 - (time() - llegadaMasVieja())));\n"
     "}\n"
     "if (estado == 3 && enVacio) eVacio.restart(Math.max(0, Math.min(eVacio.getRest(), horasEnVacio)));\n"
     "resetVis();\n"
     "evaluarEncendido();"),
]
xml_f = ""
for k, (n, rt, params, body) in enumerate(FUNCS):
    mod = "VOID" if rt == "void" else "RETURNS_VALUE"
    ps = "".join(f"<Parameter><Name>{pn}</Name><Type>{x(pt)}</Type></Parameter>" for pn, pt in params)
    xml_f += (f'<Function AccessType="public" StaticFunction="false"><ReturnModificator>{mod}</ReturnModificator>'
              f"<ReturnType>{x(rt)}</ReturnType><Id>{nid()}</Id><Name>{n}</Name><X>1900</X><Y>{900 + 22 * k}</Y>"
              f"<PublicFlag>true</PublicFlag><PresentationFlag>false</PresentationFlag><ShowLabel>true</ShowLabel>"
              f"<Label><X>10</X><Y>0</Y></Label>{ps}<Body>{x(body)}</Body></Function>")
rep("</Functions>", xml_f + "</Functions>")

# Ganchos (solo presentación)
rep("<Body>double t = time();\nif (midiendo) {", "<Body>acumularVis();\ndouble t = time();\nif (midiendo) {")
rep("<Body>if (estado != 3 || ocupado) return;\nULI sig = elegirSiguiente();",
    "<Body>if (estado != 3 || ocupado) return;\nacumularVis();\nULI sig = elegirSiguiente();")
rep("if (midiendo) esperas.add(time() - sig.tLlegada);",
    "if (midiendo) esperas.add(time() - sig.tLlegada);\nvisSumaEspera += time() - sig.tLlegada;\nvisNEspera++;")
rep("tEncendido = time();\ncampanaMedida = midiendo;", "tEncendido = time();\nvisEncendidos++;\ncampanaMedida = midiendo;")
rep("kgCampana += u.kg;", "kgCampana += u.kg;\nvisTratadas++;\nvisKg += u.kg;\nkgSalidaTotal += u.kg;")
# Muestreo: una franja de la cinta de tiempo cada 4 h (dos muestreos de 2 h).
rep("dsEnergia.add(time(), kWhTotal() / 1000);",
    "dsEnergia.add(time(), kWhTotal() / 1000);\n"
    "if (histTick++ % 2 == 0) { histEstado[histIdx] = estadoVis() + 1; histIdx = (histIdx + 1) % histEstado.length; }")

# ---------------------------------------------------------------- 2. presentación nueva
root = ET.fromstring(s.encode("utf-8"))
main_name = "Main"
i0 = s.index("<Name>Main</Name>")
ip = s.index("<Presentation>", i0)
lvl_open = s.index("<Presentation>", s.index("<Level>", ip))
lvl_close = s.index("</Presentation>", lvl_open)
bloque = s[lvl_open + len("<Presentation>"):lvl_close]
CONSERVAR = ("marcoProcesando", "graficoCola")
piezas = re.findall(r"<(Text|Rectangle|TimePlot)>.*?</\1>", bloque, flags=re.S)
elems = re.findall(r"(<(Text|Rectangle|TimePlot)>.*?</\2>)", bloque, flags=re.S)
guardados = {}
for xml_el, _ in elems:
    nm = re.search(r"<Name>([^<]+)</Name>", xml_el).group(1)
    if nm in CONSERVAR:
        guardados[nm] = xml_el
assert set(guardados) == set(CONSERVAR), guardados.keys()

# Gráfico de la cola: mismo elemento, nueva geometría, 60 días de ventana y fechas en el eje.
g = guardados["graficoCola"]
g = re.sub(r"<X>400</X><Y>345</Y>", "<X>420</X><Y>482</Y>", g, count=1)
g = g.replace("<Width>780</Width><Height>200</Height><BackgroundColor>-1</BackgroundColor><BorderColor>-12490271</BorderColor>",
              f"<Width>470</Width><Height>230</Height><BackgroundColor>-1</BackgroundColor><BorderColor>{argb(LINE)}</BorderColor>")
g = g.replace("<ChartArea><XOffset>55</XOffset><YOffset>15</YOffset><Width>700</Width><Height>130</Height>",
              "<ChartArea><XOffset>44</XOffset><YOffset>34</YOffset><Width>410</Width><Height>140</Height>")
g = g.replace("<BorderColor>-12490271</BorderColor><GridColor>", f"<BorderColor>{argb(LINE)}</BorderColor><GridColor>")
g = g.replace("<TextColor>-12490271</TextColor>", f"<TextColor>{argb(MUTED)}</TextColor>")
g = g.replace("<TimeWindowExpression>1440</TimeWindowExpression><LabelFormat>MODEL_TIME_UNITS</LabelFormat>",
              "<TimeWindowExpression>1440</TimeWindowExpression><LabelFormat>MODEL_DATE_DATE_ONLY</LabelFormat>")
assert "MODEL_DATE_DATE_ONLY" in g and "<XOffset>44</XOffset>" in g and "<X>420</X>" in g
g = g.replace("<Title>ULI en cola</Title>", "<Title>ULI esperando el horno</Title>")
g = g.replace("<Title>Umbral de encendido</Title>", "<Title>Umbral de encendido</Title>")

P = []
add = P.append
W = 1400

# Encabezado
add(rect("fondoEncabezado", 0, 0, W, 66, fill=HEAD, line=None))
add(text("titulo", 24, 12, "Caser · Horno de cementación y temple", color=WHITE, size=21, bold=True))
add(text("txtEscenario", 24, 42, "escenario", color=HEAD2, size=12, code="descEscenario()"))
add(text("txtFecha", W - 24, 12, "fecha", color=WHITE, size=16, bold=True, align="RIGHT", code="fechaTexto()"))
add(text("txtDia", W - 24, 42, "día", color=HEAD2, size=12, align="RIGHT",
         code='"día " + (int) Math.floor(time() / 24 + 1) + " de simulación  ·  velocidad: " + '
              '(getEngine().getRealTimeScale() >= 1000 ? "máxima" : getEngine().getRealTimeScale() >= 100 ? '
              '"1 semana por segundo" : getEngine().getRealTimeScale() >= 20 ? "1 día por segundo" : '
              'String.format("%.0f h por segundo", getEngine().getRealTimeScale()))'))

# Indicadores
KPIS = [
    ("Campañas del horno", 'String.valueOf(visEncendidos)', None, INK),
    ("ULI tratadas", 'String.valueOf(visTratadas)', None, INK),
    ("Espera media antes del horno", 'visNEspera == 0 ? "–" : String.format("%.1f días", visEsperaMediaDias())', None, INK),
    ("La ULI más vieja lleva", 'nEnCola == 0 ? "cola vacía" : String.format("%.1f días", esperaMasViejaDias())',
     "colorEdad(nEnCola == 0 ? time() : llegadaMasVieja())", INK),
    ("Energía por kg tratado",
     'String.format("%.2f kWh/kg", (kWhPorEncendido * visEncendidos + kWhPorDiaCaliente / 24 * visHorasCaliente()) '
     '/ Math.max(1, visKg))', None, INK),
    ("Costo acumulado del horno", "plata(visTotal())", None, "#c2410c"),
]
kw_, gap = 217, 10
for k, (lab, code, ccode, col) in enumerate(KPIS):
    X = 24 + k * (kw_ + gap)
    add(rect(f"kpiFondo{k}", X, 76, kw_, 58, fill=WHITE, line=LINE, radius=8))
    if ccode:
        add(rect(f"kpiMarca{k}", X, 76, 6, 58, fill="#6fbf80", line=None, fillcode=ccode))
    add(text(f"kpiValor{k}", X + 14, 82, "0", color=col, size=19, bold=True, code=code))
    add(text(f"kpiTexto{k}", X + 14, 112, lab, color=MUTED, size=11))

# Planta
PY, PH = 144, 196
add(line("flecha1", 174, PY + PH / 2, 20, 0, arrow=True))
add(line("flecha2", 594, PY + PH / 2, 20, 0, arrow=True))
add(line("flecha3", 944, PY + PH / 2, 20, 0, arrow=True))
# Lavado
add(rect("zonaLavado", 24, PY, 150, PH, fill="#e3edf9", line="#b6cbe8", radius=10))
add(text("txtLavado", 36, PY + 12, "LAVADO", color="#1a3d8f", size=13, bold=True))
add(text("txtLavado4", 36, PY + 44, "0", color=INK, size=24, bold=True, code="String.valueOf(nCreadas)"))
add(text("txtLavado5", 36, PY + 76, "ULI lavadas", color=MUTED, size=11))
add(text("txtLavado6", 36, PY + 138, "semana real sorteada", color=MUTED, size=10))
add(text("txtLavado8", 36, PY + 154, "n.º", color="#1a3d8f", size=12, bold=True,
         code='"n.º " + (semanaActual + 1) + " de " + (llegadasSemanas.length / 5)'))
# Cola
CX, CW = 194, 400
add(rect("zonaCola", CX, PY, CW, PH, fill=PANEL, line=LINE, radius=10))
add(text("txtColaTitulo", CX + 12, PY + 10, "COLA DEL HORNO", color=INK, size=12, bold=True,
         code='"COLA DEL HORNO  ·  " + nEnCola + " ULI  ·  " + String.format(new java.util.Locale("es", "AR"), "%,.0f", kgEnCola) + " kg"'))
GX, GY, ST, SQ, COLS, MAXC = CX + 14, PY + 32, 15, 13, 24, 192
add(rect("casilleroVacio", GX, GY, SQ, SQ, fill=WHITE, line="#c3c8cf", style="DASHED",
         XCode=f"{GX} + (index % {COLS}) * {ST}", YCode=f"{GY} + (index / {COLS}) * {ST}",
         rep=f"Math.min(umbralULI, {MAXC})"))
add(rect("uliEnCola", GX, GY, SQ, SQ, fill="#6fbf80", line="#5b6470",
         XCode=f"{GX} + (index % {COLS}) * {ST}", YCode=f"{GY} + (index / {COLS}) * {ST}",
         rep=f"Math.min(colaHorno.size(), {MAXC})",
         fillcode="((ULI) colaHorno.get(index)).urgente ? new java.awt.Color(124, 58, 237) : colorEdad(((ULI) colaHorno.get(index)).tLlegada)",
         linecode="((ULI) colaHorno.get(index)).urgente ? new java.awt.Color(110, 40, 170) : new java.awt.Color(91, 100, 112)"))
add(rect("marcaUmbral", GX, GY, SQ + 4, SQ + 4, fill=None, line="#d23c3c", lw=2,
         XCode=f"{GX} + ((umbralULI - 1) % {COLS}) * {ST} - 2", YCode=f"{GY} + ((umbralULI - 1) / {COLS}) * {ST} - 2",
         VisibleCode=f"umbralULI <= {MAXC}"))
add(text("txtColaMas", CX + CW - 12, PY + 10, "+", color="#d23c3c", size=11, bold=True, align="RIGHT",
         code=f'"+" + (colaHorno.size() - {MAXC}) + " más"', VisibleCode=f"colaHorno.size() > {MAXC}"))
LY = PY + PH - 22
leyenda = [("<3 d", "#6fbf80"), ("3–7", "#f2c94c"), ("7–14", "#f2994a"), (">14 d", "#d64545")]
lx = CX + 14
for k, (lab, col) in enumerate(leyenda):
    add(rect(f"leyEdad{k}", lx, LY + 2, 11, 11, fill=col, line=None))
    add(text(f"txtLeyEdad{k}", lx + 15, LY + 1, lab, color=MUTED, size=10))
    lx += 15 + 6 * len(lab) + 10
add(rect("leyVacio", lx, LY + 2, 11, 11, fill=WHITE, line="#c3c8cf", style="DASHED"))
add(text("txtLeyVacio", lx + 15, LY + 1, "falta", color=MUTED, size=10))
add(rect("leyUmbral", lx + 54, LY + 1, 13, 13, fill=None, line="#d23c3c", lw=2))
add(text("txtLeyUmbral", lx + 72, LY + 1, "umbral", color=MUTED, size=10, code='"umbral " + umbralULI'))
add(rect("leyUrgente", lx + 136, LY + 2, 11, 11, fill="#7c3aed", line=None))
add(text("txtLeyUrgente", lx + 151, LY + 1, "urgente", color=MUTED, size=10))
# Horno
HX, HW = 614, 330
add(rect("cuerpoHorno", HX, PY, HW, PH, fill="#c8ccd2", line="#3b4048", lw=2, fillcode="colorHorno()", radius=10))
add(text("txtHornoTitulo", HX + 12, PY + 10, "HORNO DE CEMENTACIÓN Y TEMPLE", color="#222831", size=12, bold=True))
add(text("txtHornoEstado", HX + 12, PY + 30, "Estado", color="#14181d", size=16, bold=True, code="textoHorno()"))
add(rect("faseFondo", HX + 12, PY + 58, 250, 8, fill="#ffffff", line=None,
         VisibleCode="estado == 1 || estado == 2 || estado == 4 || (estado == 3 && enVacio)"))
add(rect("faseAvance", HX + 12, PY + 58, 250, 8, fill="#3b4048", line=None, wcode="250 * progresoFase()",
         VisibleCode="estado == 1 || estado == 2 || estado == 4 || (estado == 3 && enVacio)"))
add(rect("cintaHorno", HX + 12, PY + 78, 262, 30, fill="#4a4f57", line="#2b2f35"))
for k in range(9):
    add(rect(f"rodillo{k}", HX + 18 + k * 30, PY + 110, 14, 4, fill="#2b2f35", line=None))
add(rect("uliEnCinta", HX + 16, PY + 83, 20, 20, fill="#f2994a", line="#5b6470",
         XCode=f"{HX + 16} + 234 * progresoCiclo()", VisibleCode="ocupado",
         fillcode="uliEnHorno == null ? new java.awt.Color(242, 153, 74) : uliEnHorno.urgente ? new java.awt.Color(124, 58, 237) : colorEdad(uliEnHorno.tLlegada)"))
add(rect("resistencia", HX + 14, PY + 124, 22, 7, fill="#555555", line="#2b2f35",
         XCode=f"{HX + 14} + index * 29", rep="9", fillcode="colorTemperatura()"))
add(text("txtCampana", HX + 12, PY + 160, "campaña", color="#14181d", size=11, bold=True,
         code='estado == 3 ? "Campaña: " + ulisCampana + " ULI  ·  " + String.format("%.1f t", kgCampana / 1000)'
              ' + "  ·  hace " + Math.round((time() - tEncendido) / 24) + " días" : '
              'estado == 2 ? "El horno todavía no puede cargar" : estado == 4 ? "Disponible otra vez al terminar de enfriar" : '
              '"Sin campaña en curso"'))
add(text("termoNota", HX + 304, PY + 172, "ilustrativa", color="#30353c", size=9, align="CENTER"))
# Termómetro (ilustrativo)
TX, TY, TH = HX + 296, PY + 66, 84
add(rect("termoTubo", TX, TY, 16, TH, fill=WHITE, line="#3b4048", radius=8))
add(rect("termoNivel", TX + 3, TY + TH - 3, 10, 0, fill="#d23c3c", line=None, radius=5,
         YCode=f"{TY + TH - 3} - {TH - 6} * (temperaturaHorno() - 25) / 875",
         hcode=f"{TH - 6} * (temperaturaHorno() - 25) / 875", fillcode="colorTemperatura()"))
add(text("termoValor", TX + 8, TY + TH + 6, "25 °C", color="#14181d", size=11, bold=True, align="CENTER",
         code='Math.round(temperaturaHorno()) + " °C"'))
# Salida
SX = 964
add(rect("zonaSalida", SX, PY, 150, PH, fill="#e3f4e6", line="#b7dcc0", radius=10))
add(text("txtSalida", SX + 12, PY + 12, "SALIDA", color="#0b6b3a", size=13, bold=True))
add(text("txtSalida4", SX + 12, PY + 44, "0", color=INK, size=24, bold=True, code="String.valueOf(nSalidasTotal)"))
add(text("txtSalida5", SX + 12, PY + 76, "ULI tratadas", color=MUTED, size=11))
add(text("txtSalida6", SX + 12, PY + 150, "0 t", color="#0b6b3a", size=12, bold=True,
         code='String.format("%.1f toneladas", kgSalidaTotal / 1000)'))
# Panel de la lógica (los bloques se mueven adentro)
LX = 1134
add(rect("zonaLogica", LX, PY, 242, PH, fill=None, line=LINE, radius=10))
add(text("txtLogica", LX + 12, PY + 10, "Lógica en AnyLogic", color=INK, size=12, bold=True))
add(text("txtLogica2", LX + 12, PY + 27, "Process Modeling Library", color=MUTED, size=10))
add(text("txtLogica3", LX + 12, PY + 132, "Source → Wait → Delay → Sink", color=INK, size=10, bold=True))

# Statechart (se conserva en su lugar; solo marco y título)
add(rect("zonaStatechart", 24, 350, 380, 322, fill=None, line=LINE, radius=10))
add(text("txtStatechart", 122, 356, "Estado del horno (statechart)", color=INK, size=12, bold=True))
add(guardados["marcoProcesando"])
add(text("txtProcesando", 290, 614, "Procesando", color="#6b7480", size=10))

# Cinta de tiempo
GX0, GY0, GWD = 420, 350, 956
add(rect("zonaCinta", GX0, GY0, GWD, 120, fill=WHITE, line=LINE, radius=10))
add(text("txtCinta", GX0 + 12, GY0 + 10, "Cinta de tiempo del horno · últimos 60 días", color=INK, size=12, bold=True))
lx = GX0 + 360
for k in (0, 1, 2, 3, 4, 5):
    r_, g_, b_ = EST_RGB[k]
    add(rect(f"leyEst{k}", lx, GY0 + 12, 11, 11, fill=f"#{r_:02x}{g_:02x}{b_:02x}", line=None))
    add(text(f"txtLeyEst{k}", lx + 15, GY0 + 11, EST_NOM[k], color=MUTED, size=10))
    lx += 15 + int(6.4 * len(EST_NOM[k])) + 16
SX0, SW, SH = GX0 + 12, GWD - 24, 40
add(rect("cintaFondo", SX0, GY0 + 36, SW, SH, fill="#eceef1", line=None))
ANCHO = SW / 360
add(rect("franja", SX0, GY0 + 36, 3, SH, fill="#eceef1", line=None,
         XCode=f"{SX0} + index * {ANCHO:.4f}", rep="360", fillcode="colorHist(index)"))
add(rect("cintaBorde", SX0, GY0 + 36, SW, SH, fill=None, line="#c3c8cf"))
for k, lab in enumerate(["hace 60 días", "hace 45 días", "hace 30 días", "hace 15 días"]):
    X = SX0 + k * SW / 4
    add(line(f"tick{k}", X, GY0 + 78, 0, 5, color="#9aa3ae", lw=1))
    add(text(f"txtTick{k}", X, GY0 + 85, lab, color=MUTED, size=10, align="LEFT" if k == 0 else "CENTER"))
add(text("txtTickHoy", SX0 + SW, GY0 + 85, "ahora", color=INK, size=10, bold=True, align="RIGHT"))

# Gráfico de la cola
add(g)
add(text("txtGrafico", 432, 490, "ULI en cola contra el umbral", color=INK, size=12, bold=True))

# ¿Dónde se va la plata?
PX0, PY0, PW, PHh = 904, 482, 472, 230
add(rect("zonaPlata", PX0, PY0, PW, PHh, fill=WHITE, line=LINE, radius=10))
add(text("txtPlata", PX0 + 12, PY0 + 8, "¿Dónde se va la plata?", color=INK, size=13, bold=True))
BX, BY, BW, BH = PX0 + 12, PY0 + 38, PW - 24, 24
add(rect("barraFondo", BX, BY, BW, BH, fill="#eceef1", line=None))
for pos in range(6):
    add(rect(f"barra{pos}", BX, BY, 0, BH, fill="#c8ccd2", line=WHITE, lw=1,
             XCode=f"{BX} + {BW} * fracAcumulada({pos})", wcode=f"{BW} * fracEstado(ordenEstado({pos}))",
             fillcode=f"colorEstado(ordenEstado({pos}))"))
    add(text(f"txtBarra{pos}", BX, BY + 6, "", color="#14181d", size=10, bold=True, align="CENTER",
             XCode=f"{BX} + {BW} * (fracAcumulada({pos}) + fracEstado(ordenEstado({pos})) / 2)",
             code=f'Math.round(100 * fracEstado(ordenEstado({pos}))) + " %"',
             VisibleCode=f"fracEstado(ordenEstado({pos})) > 0.06"))
COST = [("Luz (marginal)", "visLuz()", "#2a78d6"), ("Gas (GLP)", "visGas()", "#eb6834"),
        ("Capital inmovilizado", "visCapital()", "#1baf7a")]
CY0 = BY + 52
for k, (lab, fn, col) in enumerate(COST):
    Y = CY0 + k * 20
    add(text(f"txtCosto{k}", BX, Y, lab, color=INK, size=11))
    add(rect(f"barraCosto{k}", BX + 140, Y + 2, 0, 12, fill=col, line=None,
             wcode=f"200 * {fn} / Math.max(1, Math.max(visLuz(), Math.max(visGas(), visCapital())))"))
    add(text(f"valCosto{k}", BX + BW, Y, "$", color=INK, size=11, bold=True, align="RIGHT", code=f"plata({fn})"))
add(line("lineaTotal", BX, CY0 + 61, BW, 0, color=LINE, lw=1))
add(text("txtTotal", BX, CY0 + 65, "Total acumulado", color=INK, size=12, bold=True))
add(text("valTotal", BX + BW, CY0 + 65, "$", color="#c2410c", size=12, bold=True, align="RIGHT", code="plata(visTotal())"))
add(rect("cajaDesperdicio", BX, CY0 + 88, BW, 38, fill="#fdece6", line="#f59678", radius=8))
add(text("txtDesperdicio", BX + 10, CY0 + 92, "", color="#9a3412", size=12, bold=True,
         code='"Horno caliente sin carga: " + String.format("%.0f h", visHorasEstado(4)) + "  →  " + plata(visDesperdicio())'))
add(text("txtDesperdicio2", BX + 10, CY0 + 109, "es el gasto que evita E3 (apagar apenas se vacía la cola)", color="#9a3412", size=10))

# Barra inferior: escenario y velocidad
FY = 724
add(rect("zonaControles", 24, FY, 1352, 84, fill=PANEL, line=LINE, radius=10))
add(text("txtCtrlEsc", 38, FY + 9, "Escenario", color=INK, size=12, bold=True))
add(radio("radioEscenario", 38, FY + 30, 600, 24,
          ["E0 regla actual", "E1 umbral 45", "E2 espera máx. 15 d", "E3 apagar enseguida"],
          "cambiarEscenario(value);", "escenarioIndice()"))
add(text("txtCtrlEsc2", 38, FY + 60, "", color=MUTED, size=10,
         code='"Ahora: " + descEscenario().replace("Escenario ", "")'))
add(text("txtCtrlVel", 680, FY + 9, "Velocidad", color=INK, size=12, bold=True))
VEL = [("btnCampana", "Ver una campaña", 24), ("btnMes", "Ver meses", 168), ("btnRapido", "Avanzar rápido", 2000)]
for k, (nm, lab, esc) in enumerate(VEL):
    add(button(nm, 680 + k * 150, FY + 30, 140, 28, lab,
               f"getEngine().setRealTimeMode(true);\ngetEngine().setRealTimeScale({esc});"))
add(button("btnReiniciar", 1140, FY + 30, 220, 28, "Reiniciar contadores", "resetVis();"))

for pieza in P:
    try:
        ET.fromstring(pieza)
    except ET.ParseError as e:
        sys.exit(f"pieza inválida ({e}): {pieza[:300]}")
nuevo = "".join(P)
s = s[:lvl_open + len("<Presentation>")] + nuevo + s[lvl_close:]

# Bloques de la PML dentro del panel de la lógica
for nm, (X, Y) in {"source": (LX + 28, PY + 82), "colaHorno": (LX + 88, PY + 82), "horno": (LX + 148, PY + 82),
                   "sink": (LX + 208, PY + 82)}.items():
    s, n = re.subn(rf"(<EmbeddedObject><Id>\d+</Id><Name>{nm}</Name>)<X>-?\d+</X><Y>-?\d+</Y>",
                   rf"\g<1><X>{X}</X><Y>{Y}</Y>", s, count=1)
    assert n == 1, nm

# ---------------------------------------------------------------- 3. experimento Visual y ventana
vi = s.index("<Name>Visual</Name>")
vf = s.index("</SimulationExperiment>", vi)
v = s[vi:vf]
v2 = v.replace("<Parameter><ParameterName>calentamientoModeloDias</ParameterName></Parameter>",
               '<Parameter><ParameterName>calentamientoModeloDias</ParameterName><ParameterValue Class="CodeValue"><Code>0</Code></ParameterValue></Parameter>')
v2 = v2.replace("<Parameter><ParameterName>horizonteDias</ParameterName></Parameter>",
                '<Parameter><ParameterName>horizonteDias</ParameterName><ParameterValue Class="CodeValue"><Code>730</Code></ParameterValue></Parameter>')
v2 = v2.replace("<RealTimeScale>12.0</RealTimeScale>", "<RealTimeScale>24.0</RealTimeScale>")
v2 = v2.replace("<Title>Caser horno - E0, semilla 1 (animacion)</Title>", "<Title>Caser · horno de cementación y temple (animación)</Title>")
v2 = v2.replace("<InitialDate>1783584000000</InitialDate>", "<InitialDate>1755486000000</InitialDate>")
v2 = v2.replace("<FinalDate>1783584000000</FinalDate><FinalTime>10921</FinalTime>",
                "<FinalDate>1755486000000</FinalDate><FinalTime>17545</FinalTime>")
assert v2.count("<Code>0</Code></ParameterValue>") >= 1 and "<Code>730</Code>" in v2 and "24.0" in v2 and "17545" in v2
s = s[:vi] + v2 + s[vf:]
# Configuración de ejecución (la que usa AnyLogic Cloud): misma fecha y escala.
rep("<InitialDate>1783584000000</InitialDate><InitialTime>0.0</InitialTime><FinalDate>1783584000000</FinalDate><FinalTime>10921</FinalTime></ModelTimeProperties>\n<AnimationProperties>",
    "<InitialDate>1755486000000</InitialDate><InitialTime>0.0</InitialTime><FinalDate>1755486000000</FinalDate><FinalTime>10921</FinalTime></ModelTimeProperties>\n<AnimationProperties>")
rep("<RealTimeScale>48.0</RealTimeScale><EnableZoomAndPanning>", "<RealTimeScale>24.0</RealTimeScale><EnableZoomAndPanning>")
rep("<Frame><Id>1800000000183</Id><Width>1200</Width><Height>760</Height></Frame>",
    "<Frame><Id>1800000000183</Id><Width>1400</Width><Height>820</Height></Frame>")

try:
    ET.fromstring(s.encode("utf-8"))
except ET.ParseError as e:
    fila, col = e.position
    print("XML inválido:", e, "\n", s.split("\n")[fila - 1][max(0, col - 400):col + 100])
    sys.exit(1)
ALP.write_text(s, encoding="utf-8", newline="\n")
print("Presentación v4 aplicada a", ALP.name)
