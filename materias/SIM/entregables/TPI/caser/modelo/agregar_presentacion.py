#!/usr/bin/env python3
"""Agrega la presentación para el video a CaserHorno.alp (una sola vez; IDE cerrado).

Uso, desde la raíz del repo:
    .venv/Scripts/python.exe -I materias/SIM/entregables/TPI/caser/modelo/agregar_presentacion.py

Qué agrega en Main:
- Planta en 2D: lavado → cola (grilla de cuadraditos, uno por ULI, con marca roja en el umbral) → horno
  (color según estado, cinta con la ULI que se está tratando, 27 resistencias que se encienden) → salida.
- Statechart de 6 estados que REFLEJA la variable `estado` con transiciones por condición (no decide nada).
- Dos gráficos en vivo: ULI en cola contra el umbral, y energía acumulada.
- Tres variables solo de presentación (uliEnHorno, nCreadas, nSalidasTotal) y tres funciones
  (colorHorno, textoHorno, progresoCiclo). No cambian ningún resultado: el CSV de corridas debe seguir igual.
Los bloques del diagrama de flujo pasan a la esquina superior derecha.
Formatos tomados de ejemplos oficiales de AnyLogic 8.9 (Calculator, Digital Watch, Epidemic and Clinic) y
del TimePlot del modelo del subte que compiló en 8.9.9.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

ALP = Path(__file__).resolve().parent / "CaserHorno.alp"
s = ALP.read_text(encoding="utf-8")
if "<Name>cintaHorno</Name>" in s:
    sys.exit("La presentación ya está aplicada.")

_id = [1810000000000]


def nid():
    _id[0] += 1
    return str(_id[0])


def x(t):
    return escape(str(t))


def argb(r, g, b):
    return str((0xFF << 24 | r << 16 | g << 8 | b) - 2 ** 32)


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a))
    s = s.replace(a, b)


LABEL = "<Label><X>10</X><Y>0</Y></Label>"
PFLAGS = "<PublicFlag>true</PublicFlag><PresentationFlag>true</PresentationFlag><ShowLabel>false</ShowLabel>"
COLORES = {0: (200, 200, 200), 1: (240, 220, 130), 2: (255, 165, 60), 3: (235, 90, 50), 5: (245, 150, 120), 4: (150, 180, 230)}
NARANJA, GRIS_OSCURO = (240, 150, 40), (85, 85, 85)


def rect(name, X, Y, w, h, fill, line=(120, 120, 120), xcode=None, ycode=None, visible=None, replication=None,
         fillcode=None, lw=1, dashed=False):
    dyn = ""
    if xcode:
        dyn += f"<XCode>{x(xcode)}</XCode>"
    if ycode:
        dyn += f"<YCode>{x(ycode)}</YCode>"
    if visible:
        dyn += f"<VisibleCode>{x(visible)}</VisibleCode>"
    if replication:
        dyn += f'<ReplicationCode Class="CodeValue"><Code>{x(replication)}</Code></ReplicationCode>'
    fc = f"<FillColorCode>{x(fillcode)}</FillColorCode>" if fillcode else ""
    fillxml = f"<FillColor>{argb(*fill)}</FillColor>" if fill else "<FillColor/>"
    return (f"<Rectangle><Id>{nid()}</Id><Name>{name}</Name><X>{X}</X><Y>{Y}</Y><Label><X>10</X><Y>10</Y></Label>{PFLAGS}"
            f"<DrawMode>SHAPE_DRAW_2D3D</DrawMode>{dyn}<EmbeddedIcon>false</EmbeddedIcon><Z>0</Z><ZHeight>10</ZHeight>"
            f"<LineWidth>{lw}</LineWidth><LineColor>{argb(*line)}</LineColor><LineMaterial>null</LineMaterial>"
            f"<LineStyle>{'DASHED' if dashed else 'SOLID'}</LineStyle><Width>{w}</Width><Height>{h}</Height><Rotation>0.0</Rotation>"
            f"{fillxml}{fc}<FillMaterial>null</FillMaterial></Rectangle>")


def text(name, X, Y, t, code=None, size=12, bold=False, color=(50, 70, 100), visible=None):
    vis = f"<VisibleCode>{x(visible)}</VisibleCode>" if visible else ""
    tc = f"<TextCode>{x(code)}</TextCode>" if code else ""
    return (f"<Text><Id>{nid()}</Id><Name>{name}</Name><X>{X}</X><Y>{Y}</Y>{LABEL}{PFLAGS}<DrawMode>SHAPE_DRAW_2D3D</DrawMode>{vis}"
            f"<EmbeddedIcon>false</EmbeddedIcon><Z>0</Z><Rotation>0.0</Rotation><Color>{argb(*color)}</Color>"
            f"<Text>{x(t)}</Text>{tc}<Font><Name>SansSerif</Name><Size>{size}</Size><Style>{1 if bold else 0}</Style></Font>"
            f"<Alignment>LEFT</Alignment></Text>")


def plot(name, X, Y, w, h, series, ventana, desde_cero=True):
    ds = "".join(f"<DatasetExpression><Title>{x(t)}</Title><Expression>null</Expression><Color>{argb(*c)}</Color>"
                 f"<Expression2>{x(e)}</Expression2><Expression2Flag>true</Expression2Flag><PointStyle>NONE</PointStyle>"
                 f"<LineWidth>2.0</LineWidth></DatasetExpression>" for t, e, c in series)
    return (f"<TimePlot><Id>{nid()}</Id><Name>{name}</Name><X>{X}</X><Y>{Y}</Y><Label><X>0</X><Y>-10</Y></Label>{PFLAGS}"
            f"<AutoUpdate>true</AutoUpdate><OccurrenceAtTime>true</OccurrenceAtTime><OccurrenceDate>1783584000000</OccurrenceDate>"
            f'<OccurrenceTime Class="CodeUnitValue"><Code>0</Code><Unit Class="TimeUnits">HOUR</Unit></OccurrenceTime>'
            f'<RecurrenceCode Class="CodeUnitValue"><Code>2</Code><Unit Class="TimeUnits">HOUR</Unit></RecurrenceCode>'
            f"<EmbeddedIcon>false</EmbeddedIcon><Width>{w}</Width><Height>{h}</Height><BackgroundColor>-1</BackgroundColor>"
            f"<BorderColor>-12490271</BorderColor><ChartArea><XOffset>55</XOffset><YOffset>15</YOffset><Width>{w - 80}</Width>"
            f"<Height>{h - 70}</Height><BackgroundColor>-1</BackgroundColor><BorderColor>-12490271</BorderColor><GridColor>-4144960</GridColor></ChartArea>"
            f"<Legend><Place>SOUTH</Place><TextColor>-16777216</TextColor><Size>30</Size></Legend><Labels><HorLabelsPosition>DEFAULT</HorLabelsPosition>"
            f"<VerLabelsPosition>DEFAULT</VerLabelsPosition><TextColor>-12490271</TextColor></Labels><Persistent>true</Persistent>"
            f"<ShowLegend>true</ShowLegend><TimeWindowsMovementType>MOVEMENT_WITH_TIME</TimeWindowsMovementType><TimeWindowUnits>MODEL_TIME_UNIT</TimeWindowUnits>"
            f"<VerScaleFromExpression>0</VerScaleFromExpression><VerScaleToExpression>100</VerScaleToExpression><VerScaleType>AUTO</VerScaleType>"
            f"<DrawLine>true</DrawLine><Interpolation>STEP</Interpolation>{ds}<SamplesToKeep>2000</SamplesToKeep>"
            f"<TimeWindowExpression>{ventana}</TimeWindowExpression><LabelFormat>MODEL_TIME_UNITS</LabelFormat></TimePlot>")


# ------------------------------------------------------------------ planta 2D
COLS, PASO, FILAS = 24, 14, 12
X0, Y0 = 192, 132
cap = COLS * FILAS
pres = "".join([
    text("titulo", 20, 22, "Caser - horno de cementacion y temple", size=20, bold=True),
    text("txtEscenario", 20, 50, "Escenario",
         '"Escenario " + escenario + "  |  umbral " + umbralULI + " ULI  |  " + (Double.isInfinite(esperaMaxDias) ? "sin espera maxima" : "espera max. " + esperaMaxDias + " dias") + "  |  caliente sin carga " + horasEnVacio + " h"', size=13),
    text("txtKpi", 20, 74, "KPI",
         '"Dia " + (int) Math.floor(time() / 24) + "   |   campanas " + nEncendidos + " (por prioridad " + nEncendidosPrioridad + ")   |   ULI tratadas " + nTratadas + "   |   espera media " + (esperas.isEmpty() ? "-" : String.format("%.1f", media(esperas) / 24)) + " dias   |   " + (kgTratados > 0 ? String.format("%.2f", kWhTotal() / kgTratados) : "-") + " kWh/kg" + (midiendo ? "" : "   (calentamiento del modelo)")', size=13, bold=True),
    # lavado
    rect("zonaLavado", 20, 130, 130, 140, (215, 232, 246)),
    text("txtLavado", 32, 150, "LAVADO", size=14, bold=True),
    text("txtLavado2", 32, 172, "llegan ULI de lunes", size=11),
    text("txtLavado3", 32, 187, "a viernes", size=11),
    text("txtLavado4", 32, 215, "lavadas", 'nCreadas + " ULI lavadas"', size=12, bold=True),
    rect("flecha1", 152, 198, 26, 4, (120, 120, 120)),
    # cola
    rect("zonaCola", 180, 110, 362, 200, (238, 238, 238)),
    text("txtColaTitulo", 186, 126, "COLA DEL HORNO (ULI lavadas esperando)", size=11, bold=True),
    rect("uliEnCola", X0, Y0 + 4, 12, 12, NARANJA, line=(160, 90, 20),
         xcode=f"{X0} + (index % {COLS}) * {PASO}", ycode=f"{Y0 + 4} + (index / {COLS}) * {PASO}",
         replication=f"Math.min(nEnCola, {cap})"),
    rect("marcaUmbral", X0, Y0, 3, 16, (220, 0, 0), line=(220, 0, 0),
         xcode=f"{X0} + (umbralULI % {COLS}) * {PASO} - 2", ycode=f"{Y0 + 4} + (umbralULI / {COLS}) * {PASO} - 2",
         visible=f"umbralULI < {cap}"),
    text("txtCola", 186, 305, "Cola", '"En cola: " + nEnCola + " ULI (" + Math.round(kgEnCola) + " kg)   |   marca roja = umbral " + umbralULI', size=12, bold=True),
    text("txtColaMas", 470, 126, "+", '"+" + (nEnCola - ' + str(cap) + ')', size=11, bold=True, color=(200, 0, 0), visible=f"nEnCola > {cap}"),
    rect("flecha2", 544, 198, 26, 4, (120, 120, 120)),
    # horno
    rect("cuerpoHorno", 572, 110, 330, 200, COLORES[0], line=(60, 60, 60), fillcode="colorHorno()", lw=2),
    text("txtHornoTitulo", 584, 130, "HORNO DE CEMENTACION Y TEMPLE", size=12, bold=True, color=(40, 40, 40)),
    text("txtHornoEstado", 584, 160, "Estado", "textoHorno()", size=16, bold=True, color=(30, 30, 30)),
    rect("cintaHorno", 590, 210, 294, 24, GRIS_OSCURO, line=(40, 40, 40)),
    rect("uliEnCinta", 592, 213, 18, 18, NARANJA, line=(160, 90, 20), xcode="592 + 272 * progresoCiclo()", visible="ocupado"),
    rect("resistencia", 596, 252, 22, 7, GRIS_OSCURO, line=(40, 40, 40), xcode="596 + index * 32", replication="9",
         fillcode="estado == 2 || estado == 3 ? new java.awt.Color(230, 50, 20) : new java.awt.Color(85, 85, 85)"),
    text("txtResist", 590, 278, "27 resistencias", size=10, color=(40, 40, 40)),
    text("txtCampana", 590, 298, "Campana",
         '"Campana actual: " + (estado >= 2 && estado <= 3 ? ulisCampana + " ULI" : "-") + "   |   energia total " + Math.round(kWhTotal() / 1000) + " MWh"', size=11, color=(40, 40, 40)),
    rect("flecha3", 904, 198, 26, 4, (120, 120, 120)),
    # salida
    rect("zonaSalida", 932, 130, 150, 140, (214, 238, 214)),
    text("txtSalida", 944, 150, "SALIDA", size=14, bold=True),
    text("txtSalida2", 944, 172, "revenido (algunos),", size=11),
    text("txtSalida3", 944, 187, "zincado y envasado", size=11),
    text("txtSalida4", 944, 215, "tratadas", 'nSalidasTotal + " ULI tratadas"', size=12, bold=True),
    # statechart
    text("txtStatechart", 20, 352, "Estado del horno (statechart)", size=12, bold=True),
    rect("marcoProcesando", 30, 548, 345, 52, None, line=(150, 150, 150), dashed=True),
    text("txtProcesando", 290, 614, "Procesando", size=10, color=(120, 120, 120)),
    # gráficos
    plot("graficoCola", 400, 345, 780, 200, [("ULI en cola", "nEnCola", (240, 150, 40)), ("Umbral de encendido", "umbralULI", (220, 0, 0))], 1440),
    plot("graficoEnergia", 400, 555, 780, 175, [("Energia acumulada (MWh)", "kWhTotal() / 1000", (70, 110, 200))], 1440),
    text("txtLogica", 820, 18, "Logica (Process Modeling Library):", size=10, color=(120, 120, 120)),
    text("aviso", 20, 745, "Entradas reales agregadas (12 meses). Resultados no validados: ver 08-validacion-etapa1.md", size=10, color=(120, 120, 120)),
])
inicio = "<LevelVisibility>DIM_NON_CURRENT</LevelVisibility><Presentation>"
i = s.index(inicio) + len(inicio)  # el primer Level es el de Main
j = s.index("</Presentation></Level></Presentation>", i)
s = s[:i] + pres + s[j:]

# ------------------------------------------------------------------ statechart (refleja `estado`)
ESTADOS = [("Apagado", 40, 380, 0), ("Acumulando", 40, 440, 1), ("Calentando", 40, 500, 2),
           ("Cargando", 40, 560, 3), ("CalienteEnVacio", 230, 560, 5), ("Enfriando", 230, 440, 4)]
sid = {n: nid() for n, *_ in ESTADOS}
sc = []
for n, X, Y, k in ESTADOS:
    etiqueta = "Caliente en vacio" if n == "CalienteEnVacio" else n
    sc.append(f'<StatechartElement Class="State" ParentState="ROOT_NODE"><Id>{sid[n]}</Id><Name>{n}</Name><X>{X}</X><Y>{Y}</Y>'
              f'<Label><X>10</X><Y>10</Y></Label><PublicFlag>false</PublicFlag><PresentationFlag>true</PresentationFlag><ShowLabel>true</ShowLabel>'
              f'<Properties Width="130" Height="30"><FillColor>{argb(*COLORES[k])}</FillColor></Properties></StatechartElement>')
sc.append(f'<StatechartElement Class="EntryPoint" ParentState="ROOT_NODE"><Id>{nid()}</Id><Name>graficoHorno</Name><X>105</X><Y>362</Y>'
          f'{LABEL}<PublicFlag>false</PublicFlag><PresentationFlag>true</PresentationFlag><ShowLabel>false</ShowLabel>'
          f'<Points><Point><X>0</X><Y>0</Y></Point><Point><X>0</X><Y>18</Y></Point></Points><Properties Target="{sid["Apagado"]}"></Properties></StatechartElement>')
# (origen, destino, condición, X, Y, puntos relativos)
TRANS = [
    ("Apagado", "Acumulando", "estado != 0", 105, 410, [(0, 0), (0, 30)]),
    ("Acumulando", "Calentando", "estado != 1", 105, 470, [(0, 0), (0, 30)]),
    ("Calentando", "Cargando", "estado != 2 && !enVacio", 105, 530, [(0, 0), (0, 30)]),
    ("Calentando", "CalienteEnVacio", "estado != 2 && enVacio", 170, 515, [(0, 0), (125, 0), (125, 45)]),
    ("Cargando", "CalienteEnVacio", "estado == 3 && enVacio", 170, 568, [(0, 0), (60, 0)]),
    ("CalienteEnVacio", "Cargando", "estado == 3 && !enVacio", 230, 582, [(0, 0), (-60, 0)]),
    ("CalienteEnVacio", "Enfriando", "estado != 3", 330, 560, [(0, 0), (0, -90)]),
    ("Cargando", "Enfriando", "estado != 3", 60, 590, [(0, 0), (0, 25), (310, 25), (310, -135), (300, -135)]),
    ("Enfriando", "Apagado", "estado != 4", 295, 440, [(0, 0), (0, -45), (-125, -45)]),
]
for k, (a, b, cond, X, Y, pts) in enumerate(TRANS):
    p = "".join(f"<Point><X>{px}</X><Y>{py}</Y></Point>" for px, py in pts)
    sc.append(f'<StatechartElement Class="Transition" ParentState="ROOT_NODE"><Id>{nid()}</Id><Name>t{a}{b}</Name><X>{X}</X><Y>{Y}</Y>'
              f'{LABEL}<PublicFlag>false</PublicFlag><PresentationFlag>true</PresentationFlag><ShowLabel>false</ShowLabel>'
              f'<Points>{p}</Points><IconOffset>10.0</IconOffset>'
              f'<Properties Source="{sid[a]}" Target="{sid[b]}" Trigger="condition">'
              f'<Timeout Class="CodeUnitValue"><Code>1</Code><Unit Class="TimeUnits">HOUR</Unit></Timeout>'
              f'<Condition>{x(cond)}</Condition>'
              f'<Rate Class="CodeUnitValue"><Code>1</Code><Unit Class="RateUnits">PER_HOUR</Unit></Rate>'
              f'<MessageType>Object</MessageType><DefaultTransition>true</DefaultTransition><FilterType>unconditionally</FilterType>'
              f'<EqualsExpression>"text"</EqualsExpression><SatisfiesExpression>true</SatisfiesExpression></Properties></StatechartElement>')
i = s.index("</Variables>")  # el primero es el de Main
s = s[:i + len("</Variables>")] + "<StatechartElements>" + "".join(sc) + "</StatechartElements>" + s[i + len("</Variables>"):]

# ------------------------------------------------------------------ variables y funciones de presentación
FLAGS_OFF = "<PublicFlag>false</PublicFlag><PresentationFlag>false</PresentationFlag><ShowLabel>true</ShowLabel>"
nuevas = ""
for k, (n, t, v) in enumerate([("uliEnHorno", "ULI", "null"), ("nCreadas", "int", "0"), ("nSalidasTotal", "int", "0")]):
    nuevas += (f'<Variable Class="PlainVariable"><Id>{nid()}</Id><Name>{n}</Name><X>1400</X><Y>{1000 + 22 * k}</Y>{LABEL}{FLAGS_OFF}'
               f'<Properties SaveInSnapshot="true" Constant="false" AccessType="public" StaticVariable="false"><Type>{x(t)}</Type>'
               f'<UnitType>NONE</UnitType><SdArray>false</SdArray><InitialValue Class="CodeValue"><Code>{x(v)}</Code></InitialValue></Properties></Variable>')
i = s.index("</Variables>")
s = s[:i] + nuevas + s[i:]

c = ", ".join
FUNCS = [
    ("colorHorno", "java.awt.Color", "\n".join(
        [f"if (estado == 3 &amp;&amp; enVacio) return new java.awt.Color({c(map(str, COLORES[5]))});"]
        + [f"if (estado == {k}) return new java.awt.Color({c(map(str, COLORES[k]))});" for k in (0, 1, 2, 3)]
        + [f"return new java.awt.Color({c(map(str, COLORES[4]))});"])),
    ("textoHorno", "String", x("""switch (estado) {
    case 0: return "Apagado";
    case 1: return "Acumulando: " + nEnCola + " de " + umbralULI + " ULI";
    case 2: return (campanaPrioridad ? "Calentando por prioridad" : "Calentando") + " - faltan " + Math.round(eCalentamiento.getRest()) + " h";
    case 3: return enVacio ? "Caliente sin carga - apaga en " + Math.round(eVacio.getRest()) + " h"
                           : (campanaPrioridad ? "Cargando ULI urgentes" : "Cargando ULI");
    case 4: return "Enfriando - faltan " + Math.round(eEnfriamiento.getRest()) + " h";
    default: return "?";
}""")),
    ("progresoCiclo", "double", x("""if (!ocupado || uliEnHorno == null) return 0;
return Math.max(0, Math.min(1, (time() - uliEnHorno.tInicio) / (minPorULI / 60)));""")),
]
fx = ""
for k, (n, ret, body) in enumerate(FUNCS):
    fx += (f'<Function AccessType="public" StaticFunction="false"><ReturnModificator>RETURNS_VALUE</ReturnModificator><ReturnType>{x(ret)}</ReturnType>'
           f'<Id>{nid()}</Id><Name>{n}</Name><X>1700</X><Y>{1000 + 22 * k}</Y><PublicFlag>true</PublicFlag><PresentationFlag>false</PresentationFlag>'
           f'<ShowLabel>true</ShowLabel>{LABEL}<Body>{body}</Body></Function>')
rep("</Functions>", fx + "</Functions>")

# Ganchos mínimos en la lógica (solo alimentan la animación)
rep("nEnCola++;\nkgEnCola += u.kg;", "nEnCola++;\nnCreadas++;\nkgEnCola += u.kg;")
rep("sig.tInicio = time();", "sig.tInicio = time();\nuliEnHorno = sig;")
rep("acumular();\nocupado = false;", "acumular();\nocupado = false;\nuliEnHorno = null;\nnSalidasTotal++;")

# ------------------------------------------------------------------ bloques a la esquina superior derecha
POS = {"source": 840, "colaHorno": 920, "horno": 1000, "sink": 1080}
for n, X in POS.items():
    rep(f"<Name>{n}</Name><X>", f"<Name>{n}</Name><X>")
    s = re.sub(rf"(<EmbeddedObject><Id>\d+</Id><Name>{n}</Name>)<X>\d+</X><Y>\d+</Y>", rf"\g<1><X>{X}</X><Y>40</Y>", s)
for cn, a, b in (("c1", "source", "colaHorno"), ("c2", "colaHorno", "horno"), ("c3", "horno", "sink")):
    s = re.sub(rf"(<Connector><Id>\d+</Id><Name>{cn}</Name>)<X>\d+</X><Y>\d+</Y>", rf"\g<1><X>{POS[a] + 10}</X><Y>40</Y>", s)
    s = re.sub(rf"(<Name>{cn}</Name>.*?<Points><Point><X>0</X><Y>0</Y></Point><Point><X>)\d+(</X>)",
               rf"\g<1>{POS[b] - POS[a] - 20}\g<2>", s, count=1, flags=re.S)

# ULI: sin dibujo propio (la cola se dibuja con la grilla); si no, se apilarían en (0,0)
rep("<Name>cuerpoULI</Name><X>-5</X><Y>-5</Y><Label><X>0</X><Y>-10</Y></Label><PublicFlag>true</PublicFlag><PresentationFlag>true</PresentationFlag><ShowLabel>false</ShowLabel><DrawMode>SHAPE_DRAW_2D3D</DrawMode>",
    "<Name>cuerpoULI</Name><X>-5</X><Y>-5</Y><Label><X>0</X><Y>-10</Y></Label><PublicFlag>true</PublicFlag><PresentationFlag>true</PresentationFlag><ShowLabel>false</ShowLabel><DrawMode>SHAPE_DRAW_2D3D</DrawMode><VisibleCode>false</VisibleCode>")
# Visual más lento: 12 h simuladas por segundo
rep("<RealTimeScale>48.0</RealTimeScale></PresentationProperties>", "<RealTimeScale>12.0</RealTimeScale></PresentationProperties>")

ET.fromstring(s.encode("utf-8"))
ALP.write_text(s, encoding="utf-8", newline="\n")
print("Presentación agregada a", ALP.name)
