#!/usr/bin/env python3
"""Construye el documento de estado del TPI de molinetes al 11/11 (para el docente) como DOCX sin dependencias externas.

Mismo formato y mismos datos de producción que build-tpi-subte-avance-nov-docx.py; cambia el cuerpo: es una foto
del trabajo completo, no un diff contra el avance del 12/10."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from datetime import datetime, timezone
from html import escape


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "materias/SIM/entregables/TPI/subte/TPI_Subte_Estado_2026-11-11.docx"

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def run(text, *, bold=False, italic=False, color="000000", size=21):
    props = []
    if bold:
        props.append("<w:b/>")
    if italic:
        props.append("<w:i/>")
    props.extend([
        f'<w:color w:val="{color}"/>',
        f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>',
        '<w:rFonts w:ascii="Aptos" w:hAnsi="Aptos" w:cs="Aptos"/>',
    ])
    preserve = ' xml:space="preserve"' if text[:1].isspace() or text[-1:].isspace() else ""
    return f"<w:r><w:rPr>{''.join(props)}</w:rPr><w:t{preserve}>{escape(text)}</w:t></w:r>"


def paragraph(parts="", *, style=None, before=0, after=120, line=276, keep=False,
              align=None, page_break=False, left=0, hanging=0):
    if isinstance(parts, str):
        parts = [parts] if parts.startswith("<w:r>") else [run(parts)]
    ppr = []
    if style:
        ppr.append(f'<w:pStyle w:val="{style}"/>')
    ppr.append(f'<w:spacing w:before="{before}" w:after="{after}" w:line="{line}" w:lineRule="auto"/>')
    if keep:
        ppr.append("<w:keepNext/>")
    if align:
        ppr.append(f'<w:jc w:val="{align}"/>')
    if page_break:
        ppr.append("<w:pageBreakBefore/>")
    if left or hanging:
        ppr.append(f'<w:ind w:left="{left}" w:hanging="{hanging}"/>')
    return f"<w:p><w:pPr>{''.join(ppr)}</w:pPr>{''.join(parts)}</w:p>"


def rich(*items, size=21):
    """items: texto o tupla (texto, negrita, cursiva, color)."""
    out = []
    for item in items:
        if isinstance(item, str):
            out.append(run(item, size=size))
        else:
            text = item[0]
            bold = item[1] if len(item) > 1 else False
            italic = item[2] if len(item) > 2 else False
            color = item[3] if len(item) > 3 else "000000"
            out.append(run(text, bold=bold, italic=italic, color=color, size=size))
    return out


def cell(text, width, *, header=False, center=False, shade=None):
    fill = shade or ("17365D" if header else "FFFFFF")
    color = "FFFFFF" if header else "000000"
    p = paragraph(run(str(text), bold=header, color=color, size=18 if header else 19),
                  after=0, line=240, align="center" if center else "left")
    return (
        f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>'
        f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>'
        '<w:vAlign w:val="center"/><w:tcMar>'
        '<w:top w:w="95" w:type="dxa"/><w:left w:w="110" w:type="dxa"/>'
        '<w:bottom w:w="95" w:type="dxa"/><w:right w:w="110" w:type="dxa"/>'
        '</w:tcMar></w:tcPr>' + p + '</w:tc>'
    )


def table(headers, rows, widths, centers=()):
    borders = ''.join(
        f'<w:{edge} w:val="single" w:sz="4" w:space="0" w:color="D9D9D9"/>'
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV")
    )
    grid = ''.join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    header_row = '<w:tr><w:trPr><w:tblHeader/></w:trPr>' + ''.join(
        cell(value, widths[i], header=True, center=i in centers) for i, value in enumerate(headers)
    ) + '</w:tr>'
    body = []
    for row_no, values in enumerate(rows):
        shade = "F2F6FA" if row_no % 2 else "FFFFFF"
        body.append('<w:tr>' + ''.join(
            cell(value, widths[i], center=i in centers, shade=shade) for i, value in enumerate(values)
        ) + '</w:tr>')
    return (
        '<w:tbl><w:tblPr><w:tblW w:w="0" w:type="auto"/>'
        '<w:tblLayout w:type="fixed"/><w:tblCellMar>'
        '<w:top w:w="95" w:type="dxa"/><w:left w:w="110" w:type="dxa"/>'
        '<w:bottom w:w="95" w:type="dxa"/><w:right w:w="110" w:type="dxa"/>'
        f'</w:tblCellMar><w:tblBorders>{borders}</w:tblBorders></w:tblPr>'
        f'<w:tblGrid>{grid}</w:tblGrid>{header_row}{"".join(body)}</w:tbl>'
        + paragraph("", after=70)
    )


def bullet(text, *, bold_lead=None):
    parts = []
    if bold_lead and text.startswith(bold_lead):
        parts = rich((bold_lead, True), text[len(bold_lead):], size=20)
    else:
        parts = rich(text, size=20)
    p = paragraph(parts, after=55, line=250, left=520, hanging=300)
    return p.replace("<w:pPr>", '<w:pPr><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>', 1)



# ---------------------------------------------------------------------------
# Datos de la producción (corridas_peatonales.csv, 6 días × 4 escenarios, 11/11/2026)
# ---------------------------------------------------------------------------

def h1(texto):
    return paragraph(run(texto, bold=True, size=27), style="Heading1", before=120, after=90, keep=True)


def coma(x, d=1):
    return f"{x:.{d}f}".replace(".", ",").replace("-", "−")


DIAS = [  # día SBASE, generados, (P90 s, % > 30 s) para E0, E1, E3, E13
    ("vie 06/03", 16760, [(16.2, 3.6), (10.8, 0.4), (10.2, 1.7), (7.8, 0.2)]),
    ("mié 11/03", 17620, [(14.7, 2.3), (9.9, 0.4), (9.9, 1.0), (7.5, 0.0)]),
    ("mié 25/03", 19706, [(29.7, 9.9), (15.0, 3.4), (17.1, 5.6), (11.1, 1.7)]),
    ("mié 13/05", 20530, [(24.3, 8.0), (12.9, 2.2), (14.1, 3.4), (9.0, 0.5)]),
    ("vie 15/05", 17841, [(18.3, 6.0), (12.0, 1.8), (12.6, 2.6), (8.1, 0.2)]),
    ("vie 05/06", 17457, [(15.3, 2.9), (10.2, 0.4), (10.5, 1.0), (7.5, 0.1)]),
]

# (medida, E0, alternativa, D, IC inferior, IC superior, cambio %)
DIFERENCIAS = {
    "E1 (22 molinetes)": [
        ("P90 de espera (s)", 19.75, 11.80, -7.95, -15.77, -0.13, -40.3),
        ("Proporción > 30 s (%)", 5.4, 1.4, -4.0, -7.5, -0.5, -73.5),
        ("P90 cohorte pico (s)", 24.55, 13.30, -11.25, -21.09, -1.41, -45.8),
    ],
    "E3 (validación rápida)": [
        ("P90 de espera (s)", 19.75, 12.40, -7.35, -13.55, -1.15, -37.2),
        ("Proporción > 30 s (%)", 5.4, 2.5, -2.9, -5.5, -0.3, -53.2),
        ("P90 cohorte pico (s)", 24.55, 14.85, -9.70, -17.11, -2.29, -39.5),
    ],
    "E13 (las dos)": [
        ("P90 de espera (s)", 19.75, 8.50, -11.25, -20.08, -2.42, -57.0),
        ("Proporción > 30 s (%)", 5.4, 0.5, -5.0, -9.8, -0.2, -91.7),
        ("P90 cohorte pico (s)", 24.55, 9.35, -15.20, -27.71, -2.69, -61.9),
    ],
}

VENTANAS = [  # ventana, observado medio, simulado medio, sesgo %
    ("07:00", 1374, 902, -34.4), ("07:15", 1807, 1347, -25.4), ("07:30", 1784, 1635, -8.4),
    ("07:45", 2032, 1865, -8.2), ("08:00", 1691, 1849, 9.3), ("08:15", 2248, 2126, -5.4),
    ("08:30", 1938, 1680, -13.3), ("08:45", 1594, 1514, -5.0), ("09:00", 2113, 2188, 3.6),
    ("09:15", 1742, 1971, 13.2),
]

body = []
body.append(paragraph(run("TPI Simulación: molinetes de Constitución (Línea C)", bold=True, size=34),
                      style="Title", after=70, line=360, keep=True))
body.append(paragraph(run("Estado del trabajo al 11 de noviembre de 2026", size=23, color="404040"),
                      style="Subtitle", after=210, line=280, keep=True))
body.append(table(
    ["Dato", "Detalle"],
    [
        ["Integrantes", "Juan Cruz Bonadeo (53533) y Matías Estevez (53528)"],
        ["Comisión", "401"],
        ["Docente", "Guillermo Leale"],
        ["Herramienta", "AnyLogic 8.9.10 PLE, Pedestrian Library y Rail Library"],
        ["Archivos", "SubteConstitucion.alp, corridas_peatonales.csv (24 corridas) e informe en LaTeX"],
    ],
    [2450, 6600],
))
body.append(paragraph(rich(
    ("En una línea. ", True),
    "El modelo está terminado y en producción: simula la estación en dos niveles, desde la puerta del tren del "
    "Roca hasta el molinete de la Línea C, con un día hábil real por réplica. Hay 6 días corridos con los cuatro "
    "escenarios (24 corridas). Las tres alternativas reducen la espera respecto de la situación actual en los "
    "9 intervalos de Bonferroni. Falta cerrar el informe, la planilla y el video.",
), after=180))

# 1. Problema
body.append(h1("1. Problema y pregunta"))
body.append(paragraph(
    "Constitución es la estación más cargada del subte: tiene las 14 ventanas de 15 minutos con más ingresos de "
    "toda la red. El estudio cubre el vestíbulo Principal de la Línea C, que da al hall del Roca y concentra el "
    "84,7 % de los ingresos de la estación, en días hábiles de 07:00 a 09:30.",
    after=90,
))
body.append(paragraph(rich(
    ("Por qué hace falta simular. ", True),
    "Con promedios el problema no existe: en la ventana de las 08:15 entran 2.214 pasajeros en 15 minutos y cada "
    "molinete está ocupado un 32 % del tiempo, así que un M/M/c con 20 servidores no predice cola. Pero la cola "
    "existe, porque la gente llega en oleadas: en la franja arriban 47 trenes del Roca, uno cada 3 minutos en "
    "mediana. Es congestión transitoria por arribos en lote, que los modelos estacionarios promedian.",
), after=90))
body.append(paragraph(rich(
    ("Pregunta de decisión. ", True),
    "¿Cuánto baja la espera si se habilitan los 22 molinetes del vestíbulo en lugar de los 20 que se usan, si se "
    "valida más rápido, o si se hacen las dos cosas?",
), after=150))

# 2. Datos
body.append(h1("2. Datos"))
body.append(bullet("SBASE (Buenos Aires Data): validaciones por molinete cada 15 minutos, enero a junio de 2026. Se usan 75 días hábiles de marzo a junio con servicio normal del Roca.", bold_lead="SBASE (Buenos Aires Data):"))
body.append(bullet("Trenes Argentinos: respondió el pedido por TAD el 26/10. Envió el plano de la estación y las llegadas reales de cada tren de marzo a junio, que alimentan el modelo.", bold_lead="Trenes Argentinos:"))
body.append(bullet("OpenStreetMap: georreferencia del plano y del pasillo hasta el vestíbulo.", bold_lead="OpenStreetMap:"))
body.append(bullet("Literatura: tiempos de validación y velocidades de marcha (TCQSM, estudios de metro con AnyLogic).", bold_lead="Literatura:"))
body.append(bullet("Sin respuesta de SBASE: no hay plano del subsuelo, así que la plaza de transbordo y el interior del vestíbulo son supuestos, marcados [SUP] en el modelo.", bold_lead="Sin respuesta de SBASE:"))
body.append(paragraph("", after=60))

# 3. Modelo
body.append(h1("3. Modelo en AnyLogic"))
body.append(paragraph(run("PedSource (puertas del tren / calle)  ->  hall  ->  PedChangeLevel (escaleras mecánicas)  ->  "
                          "elección de cola  ->  PedService (molinete)  ->  PedSink",
                          bold=True, color="17365D", size=19), align="center", before=30, after=130, line=260))
body.append(bullet("Día real: cada réplica sortea un día hábil; de ese día salen las validaciones de SBASE por ventana y las llegadas reales de los trenes. El pasaje de cada tren es Poisson con la demanda de su ramal; el resto entra desde la calle.", bold_lead="Día real:"))
body.append(bullet("Descenso: cada tren descarga por sus 21 puertas en el andén que le toca; la dispersión de la oleada sale de caminar el andén (hasta ~155 m a 1,1-1,5 m/s).", bold_lead="Descenso:"))
body.append(bullet("Acceso: el pasajero cruza el hall entre los obstáculos del plano y baja por la escalera mecánica de su lado del bloque central; la plaza de transbordo y un pasillo de 84 m lo llevan al vestíbulo de 50 × 34 m.", bold_lead="Acceso:"))
body.append(bullet("Elección de cola: cada pasajero elige el molinete con menor espera estimada, contando a los que ya van en camino.", bold_lead="Elección de cola:"))
body.append(bullet("Sistema terminal: arranca vacío a las 07:00, los arribos se cortan a las 09:30 y la corrida sigue hasta que sale el último pasajero. No hay período de calentamiento.", bold_lead="Sistema terminal:"))
body.append(bullet("Presentación: la vista está en los cuatro bloques que pidió la cátedra (variables, medidas de rendimiento, lógica y modelo espacial), con panel en vivo, vista 3D con los trenes del Roca y mapa de calor de densidad.", bold_lead="Presentación:"))
body.append(paragraph("", after=60))

# 4. Escenarios y medidas
body.append(h1("4. Escenarios y medidas"))
body.append(table(
    ["Escenario", "Molinetes", "Validación", "Estado"],
    [
        ["E0 Base", "20", "Triangular (1,8; 2,4; 3,5) s", "Corrido, 6 días"],
        ["E1 Capacidad", "22", "Igual que E0", "Corrido, 6 días"],
        ["E3 Validación rápida", "20", "Triangular (1,5; 1,8; 2,5) s [SUP, TCQSM]", "Corrido, 6 días"],
        ["E13 Combinado", "22", "Igual que E3", "Corrido, 6 días"],
    ],
    [2300, 1300, 3350, 2100], centers=(1,),
))
body.append(bullet("Primarias: P90 de la espera en la franja, proporción de pasajeros que esperan más de 30 s y P90 de quienes llegan en el pico (08:15-08:45).", bold_lead="Primarias:"))
body.append(bullet("Secundarias: espera media, largo de cola, cola máxima, utilización, tránsito del Roca hasta la cola y dispersión entre molinetes.", bold_lead="Secundarias:"))
body.append(paragraph("", after=60))

# 5. Diseño experimental
body.append(h1("5. Diseño experimental"))
body.append(bullet("Números aleatorios comunes: un generador por fuente de azar (calle, servicio, velocidad, trenes, día). En cada réplica, los cuatro escenarios reciben el mismo día, los mismos trenes y los mismos pasajeros; sólo cambian los molinetes o la validación.", bold_lead="Números aleatorios comunes:"))
body.append(bullet("Comparación: cada alternativa contra E0 con intervalo t apareado. Bonferroni sobre 3 primarias × 3 comparaciones (k = 9, α = 0,05/9) para una confianza conjunta de al menos 95 %.", bold_lead="Comparación:"))
body.append(bullet("Réplicas: el diseño fija un piloto de n0 = 10 días y el cálculo de n*. Por el costo de cómputo (~100 min por tanda de 10 corridas en paralelo) hoy hay 6 días.", bold_lead="Réplicas:"))
body.append(bullet("Regla de decisión, fijada antes de correr: una alternativa mejora una medida si su intervalo queda entero por debajo de cero.", bold_lead="Regla de decisión,"))
body.append(paragraph("", after=60))

# 6. Verificación
body.append(h1("6. Verificación"))
body.append(bullet("Verificador automático: compila las funciones del modelo contra la API de AnyLogic, ejecuta casos de prueba (conservación, cierre a las 09:30, drenaje, filas de salida) y controla la estructura del .alp. Se corre antes de cada cambio.", bold_lead="Verificador automático:"))
body.append(bullet("Conservación: en las 24 corridas, generados = procesados + atascados. Los atascados van de 19 a 66 por corrida (0,1-0,4 % de ~18.000); por encima de máx(20; 0,5 %) la corrida se descarta.", bold_lead="Conservación:"))
body.append(bullet("Números comunes comprobados: con la misma semilla, los cuatro escenarios generan exactamente los mismos ingresos.", bold_lead="Números comunes comprobados:"))
body.append(bullet("Rendimiento: el ruteo peatonal va sin peso de densidad (camino más corto), lo que aceleró la corrida 3-4 veces. Se declara como simplificación.", bold_lead="Rendimiento:"))
body.append(paragraph("", after=60))

# 7. Validación
body.append(h1("7. Validación contra el día real"))
body.append(paragraph(
    "Como cada réplica reproduce un día concreto, el caudal simulado por ventana se compara con las validaciones "
    "observadas ese mismo día (E0, promedio de los 6 días).",
    after=80,
))
body.append(table(
    ["Ventana", "Observado", "Simulado", "Sesgo"],
    [[v, f"{o:,}".replace(",", "."), f"{s:,}".replace(",", "."), ("+" if b > 0 else "") + coma(b) + " %"]
     for v, o, s, b in VENTANAS],
    [2000, 2300, 2300, 2450], centers=(1, 2, 3),
))
body.append(bullet("De 07:30 a 09:15 el caudal queda dentro de ±13 % del observado y sigue la forma del pico."))
body.append(bullet("En 07:00-07:30 el modelo queda 25-34 % abajo: arranca vacío y el primer pasaje tarda en caminar hasta los molinetes. Es el transitorio inicial y cae fuera del pico."))
body.append(bullet("Reparto entre molinetes: CV del modelo 0,30 contra 0,56 de SBASE. El modelo reparte más parejo que la gente real, así que podría sobreestimar el efecto de E1."))
body.append(paragraph("", after=60))

# 8. Resultados
body.append(h1("8. Resultados (6 días)"))
body.append(paragraph("P90 de la espera en cola y proporción de pasajeros que esperan más de 30 s, por día y escenario:", after=80))
rows = []
for dia, gen, vals in DIAS:
    rows.append([dia, f"{gen:,}".replace(",", ".")] + [f"{coma(p)} s · {coma(q)} %" for p, q in vals])
body.append(table(["Día SBASE", "Pasajeros", "E0", "E1", "E3", "E13"], rows,
                  [1350, 1150, 1650, 1650, 1650, 1600], centers=(1, 2, 3, 4, 5)))
body.append(paragraph(
    "El orden se repite los 6 días: E13 < E1 ≈ E3 < E0. El día con más pasajeros (13/05) no es el de mayor espera, "
    "que es el 25/03: la espera depende de cómo llegan los trenes y no sólo del total.",
    after=120,
))
body.append(paragraph(
    "Diferencias apareadas D = alternativa − E0 con t de Student (5 g.l.) y Bonferroni para las 9 primarias "
    "(α = 0,05/9, confianza individual 99,44 %, conjunta ≥ 95 %):",
    after=80,
))
rows = []
for esc, medidas in DIFERENCIAS.items():
    for i, (m, e0, alt, d, lo, hi, pct) in enumerate(medidas):
        d_dec = 1 if "%" in m else 2
        rows.append([esc if i == 0 else "", m, coma(e0, d_dec), coma(alt, d_dec), coma(d, d_dec),
                     f"[{coma(lo, d_dec)}; {coma(hi, d_dec)}]", coma(pct) + " %"])
body.append(table(["Alternativa", "Medida", "E0", "Alt.", "D", "IC 99,44 %", "Cambio"], rows,
                  [1850, 2100, 800, 800, 900, 1650, 950], centers=(2, 3, 4, 5, 6)))
body.append(paragraph(rich(
    ("Lectura. ", True),
    "Ninguno de los 9 intervalos contiene el cero: con 6 días, cada alternativa reduce las tres medidas primarias "
    "respecto de la situación actual, con confianza conjunta del 95 %. Habilitar los 2 molinetes que faltan (E1) "
    "y validar más rápido (E3) dan efectos parecidos, de alrededor del 40 % en el P90. La combinación (E13) baja el "
    "P90 de 19,8 s a 8,5 s y deja casi en cero a los que esperan más de 30 s.",
), after=90))
body.append(paragraph(rich(
    ("Efecto de los números aleatorios comunes. ", True),
    "Para el P90 de E0 contra E1, Var(D) = 16,9 frente a Var(E0) + Var(E1) = 39,7: el apareamiento reduce la "
    "varianza de la diferencia a menos de la mitad.",
), after=150))

# 9. Limitaciones
body.append(h1("9. Supuestos y limitaciones"))
body.append(bullet("Réplicas: hay 6 días de los 10 planificados. Con un semiancho de 1 s, el procedimiento secuencial pide entre 87 y 338 días, inalcanzable con esta variabilidad entre días; la conclusión se apoya en el signo de las diferencias, que ya es significativo.", bold_lead="Réplicas:"))
body.append(bullet("Acceso congestionado: el P90 del tránsito del Roca, de la puerta del tren a la cola, es de ~765 s en los cuatro escenarios. Es igual en todos, así que no cambia la comparación, pero puede atenuar la oleada que llega a los molinetes.", bold_lead="Acceso congestionado:"))
body.append(bullet("Proporción del Roca: se supone que el 80 % de los usuarios del vestíbulo viene del tren; los datos no permiten estimarla.", bold_lead="Proporción del Roca:"))
body.append(bullet("Validación rápida de E3: rango de la literatura (TCQSM), sin medición propia.", bold_lead="Validación rápida de E3:"))
body.append(bullet("Espera real: no hay datos de cola en Constitución, sólo de validaciones. La conclusión es comparativa: los cuatro escenarios comparten los supuestos.", bold_lead="Espera real:"))
body.append(paragraph("", after=60))

# 10. Entregables
body.append(h1("10. Estado de los entregables"))
body.append(table(
    ["Entregable", "Estado"],
    [
        ["Modelo (.alp)", "Terminado; verificado y en producción"],
        ["Corridas", "24 corridas (6 días × 4 escenarios) en corridas_peatonales.csv"],
        ["Informe en LaTeX (10 pasos)", "Redactado con el modelo final; faltan volcar los resultados de producción y los enlaces"],
        ["Planilla de corridas", "Armada con las 3 comparaciones y Bonferroni; falta cargar las corridas"],
        ["Video (≤ 3 min)", "Presentación y guion listos; falta grabar"],
        ["AnyLogic Cloud", "Datos embebidos en el modelo para que corra en Cloud; falta publicar el enlace"],
    ],
    [3000, 6050],
))

sect = (
    '<w:sectPr>'
    '<w:headerReference w:type="default" r:id="rId2"/>'
    '<w:footerReference w:type="default" r:id="rId3"/>'
    '<w:pgSz w:w="11906" w:h="16838"/>'
    '<w:pgMar w:top="900" w:right="950" w:bottom="900" w:left="950" w:header="420" w:footer="420" w:gutter="0"/>'
    '<w:cols w:space="720"/><w:docGrid w:linePitch="360"/>'
    '</w:sectPr>'
)

document_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W}" xmlns:r="{R}"><w:body>{''.join(body)}{sect}</w:body></w:document>'''

styles_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W}">
  <w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Aptos" w:hAnsi="Aptos"/><w:sz w:val="21"/><w:color w:val="000000"/></w:rPr></w:rPrDefault>
  <w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
  <w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/>
    <w:pPr><w:keepNext/><w:spacing w:after="70"/></w:pPr><w:rPr><w:b/><w:color w:val="000000"/><w:sz w:val="34"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/>
    <w:pPr><w:keepNext/><w:spacing w:after="210"/></w:pPr><w:rPr><w:color w:val="404040"/><w:sz w:val="23"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/>
    <w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="240" w:after="90"/><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:b/><w:color w:val="000000"/><w:sz w:val="27"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/>
    <w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="150" w:after="60"/><w:outlineLvl w:val="1"/></w:pPr><w:rPr><w:b/><w:color w:val="000000"/><w:sz w:val="22"/></w:rPr></w:style>
</w:styles>'''

numbering_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="{W}"><w:abstractNum w:abstractNumId="0"><w:multiLevelType w:val="singleLevel"/>
<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="•"/><w:lvlJc w:val="left"/>
<w:pPr><w:tabs><w:tab w:val="num" w:pos="520"/></w:tabs><w:ind w:left="520" w:hanging="300"/></w:pPr>
<w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/></w:rPr></w:lvl></w:abstractNum>
<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num></w:numbering>'''

header_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:hdr xmlns:w="{W}">{paragraph(run("SIM  |  TPI  |  MOLINETES DE CONSTITUCIÓN", bold=True, color="606060", size=16), after=0)}</w:hdr>'''
footer_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="{W}">{paragraph(run("Comisión 401  |  Bonadeo y Estevez  |  estado al 11 de noviembre de 2026", color="707070", size=16), after=0, align="center")}</w:ftr>'''

content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
<Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>
<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>'''

package_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''

document_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>
<Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
</Relationships>'''

now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
core_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>TPI Simulación de molinetes de subte</dc:title>
<dc:creator>Juan Cruz Bonadeo y Matias Estevez</dc:creator><dc:subject>Estado del trabajo al 11/11/2026</dc:subject>
<dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified></cp:coreProperties>'''
app_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Application>Microsoft Office Word</Application><AppVersion>16.0000</AppVersion></Properties>'''

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as z:
    for name, data in {
        "[Content_Types].xml": content_types,
        "_rels/.rels": package_rels,
        "word/document.xml": document_xml,
        "word/_rels/document.xml.rels": document_rels,
        "word/styles.xml": styles_xml,
        "word/numbering.xml": numbering_xml,
        "word/header1.xml": header_xml,
        "word/footer1.xml": footer_xml,
        "docProps/core.xml": core_xml,
        "docProps/app.xml": app_xml,
    }.items():
        z.writestr(name, data)

print(OUTPUT)

