#!/usr/bin/env python3
"""Construye el informe de avance del TPI de molinetes (entrega del 12/10) como DOCX sin dependencias externas."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from datetime import datetime, timezone
from html import escape


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "materias/SIM/entregables/TPI/subte/TPI_Subte_Avance_2026-10-12.docx"

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


body = []
body.append(paragraph(run("TPI Simulación: molinetes de Constitución (Línea C)", bold=True, size=34),
                      style="Title", after=70, line=360, keep=True))
body.append(paragraph(run("Informe de avance: modelo base funcionando y escenarios definidos", size=23, color="404040"),
                      style="Subtitle", after=210, line=280, keep=True))
body.append(table(
    ["Dato", "Detalle"],
    [
        ["Integrantes", "Juan Cruz Bonadeo (53533) y Matías Estevez (53528)"],
        ["Comisión", "401"],
        ["Docente", "Guillermo Leale"],
        ["Herramienta", "AnyLogic 8.9.10 PLE, Pedestrian Library"],
        ["Fecha del avance", "12 de octubre de 2026"],
    ],
    [2450, 6600],
))
body.append(paragraph(rich(
    ("Estado en una línea. ", True),
    "El modelo base corre la franja 07:00-09:30 completa, conserva y drena a todos los pasajeros, y ya produjo "
    "30 pares de réplicas E0-E1 con números aleatorios comunes. Los escenarios alternativos están definidos; "
    "E1 está implementado y comparado, y E2 y E3 están definidos con su alcance propuesto para revisar en la consulta.",
), after=180))

# 1. Caso
body.append(paragraph(run("1. Caso y pregunta", bold=True, size=27), style="Heading1", before=140, after=90, keep=True))
body.append(table(
    ["Dimensión", "Definición"],
    [
        ["Sistema", "Línea de molinetes del vestíbulo Principal de Constitución, Línea C"],
        ["Días y franja", "Días hábiles, 07:00 a 09:30; pico 08:15 a 08:45"],
        ["Entidad", "Pasajero que ingresa al subte"],
        ["Recursos", "Molinetes del vestíbulo Principal (22 identificadores en el dataset)"],
        ["Pregunta", "¿Cuánto cambia la espera si se habilitan los 22 molinetes del vestíbulo en lugar de los 20 que operan en promedio?"],
    ],
    [2450, 6600],
))
body.append(paragraph(rich(
    ("Por qué requiere simulación. ", True),
    "En promedio cada molinete está ocupado cerca del 26 % del tiempo, y un modelo analítico M/M/c concluiría "
    "que casi no hay cola. La cola existe porque los pasajeros llegan en oleadas: cada tren del Ferrocarril Roca "
    "descarga cientos de personas que caminan juntas hasta los molinetes. Es congestión transitoria sobre un "
    "sistema subutilizado en promedio, que es el caso en que la fórmula falla y la simulación es la herramienta adecuada.",
), after=150))

# 2. Datos
body.append(paragraph(run("2. Datos de entrada", bold=True, size=27), style="Heading1", before=120, after=90, keep=True))
body.append(table(
    ["Entrada", "Fuente", "Valor usado"],
    [
        ["Demanda por cuarto de hora", "BA Data, Subte Viajes Molinetes 2026 (por molinete, cada 15 min)", "Perfil medio marzo-junio 2026, 80 días hábiles; 18.532 pasajeros en la franja"],
        ["Llegadas de trenes", "Horarios oficiales de la Línea Roca vigentes desde el 03/08/2026", "47 trenes en días hábiles entre 07:00 y 09:30"],
        ["Distancia andén-vestíbulo", "OpenStreetMap, medición propia sobre 14 vías", "85 m (rango 69-112 m)"],
        ["Tiempo de validación", "TCQSM 3.ª ed. (TRB), Station Planning Standards de London Underground y cota del dataset SBASE (≤ 3,66 s)", "Triangular (1,8; 2,4; 3,5) s"],
        ["Dispersión de la descarga del tren", "Caminata por el andén según velocidades del TCQSM", "145 s"],
        ["Demora andén-molinetes", "D/0,95 + h/0,30 con D = 85 m", "106 s"],
        ["Proporción que llega en tren", "Supuesto explícito (sin fuente pública)", "0,80"],
    ],
    [2300, 3700, 3050],
))
body.append(paragraph(
    "Los tres parámetros sin dato publicado (validación, descarga y proporción del Roca) se trabajan con rangos "
    "optimista, intermedio y pesimista tomados de fuentes técnicas citables. Los resultados de este avance usan "
    "el valor intermedio. Se pidieron planos y datos a SBASE (Ley 104, trámite 01084412/26) y a Trenes Argentinos "
    "(TAD, EX-2026-96962531), con vencimiento cerca del 27/10; si llegan, reemplazan al valor intermedio.",
    after=150,
))

# 3. Modelo
body.append(paragraph(run("3. Modelo base en AnyLogic", bold=True, size=27), style="Heading1", before=120, after=90, keep=True))
body.append(paragraph(run("PedSource (trenes y calle)  ->  elección de cola  ->  PedService (molinete)  ->  PedGoTo  ->  PedSink",
                          bold=True, color="17365D", size=20), align="center", before=30, after=130, line=260))
body.append(bullet("Capa peatonal (Pedestrian Library): vestíbulo de 70 × 34 m con paredes, molinetes lineales y una cola por molinete. El plano es hipotético y así se indica en pantalla, porque no hay plano oficial publicado."))
body.append(bullet("Llegadas: cada tren del Roca libera su pasaje escalonado durante la descarga, más un flujo Poisson desde la calle; el total por ventana se ajusta al perfil SBASE."))
body.append(bullet("Elección de cola: cada pasajero elige el molinete con menor espera estimada, contando también a los que ya van en camino (evita que todos vayan al mismo)."))
body.append(bullet("Cierre: los arribos se cortan a las 09:30 y la corrida continúa hasta que sale el último pasajero (drenaje), sin perder a nadie."))
body.append(bullet("Además existe una capa lógica de eventos discretos (Source → Queue → Seize → Delay → Release → Sink) con E0-E3, usada para verificar la lógica."))
body.append(paragraph("", after=60))
body.append(table(
    ["Experimento", "Para qué sirve"],
    [
        ["PeatonalFranjaVisualE0 / E1", "Franja completa con animación (escala 30x), escenario intermedio"],
        ["PeatonalE0 / PeatonalE1", "Prueba corta de 480 peatones para ver el circuito"],
        ["PeatonalCorridasApareadas", "30 pares E0-E1 de producción; escribe corridas_peatonales.csv"],
    ],
    [3300, 5750],
))

# 4. Verificación
body.append(paragraph(run("4. Verificación y estado de funcionamiento", bold=True, size=27), style="Heading1", before=120, after=90, keep=True))
body.append(bullet("Conservación: en las 60 corridas, pasajeros generados = procesados con drenaje; ninguna corrida quedó sin vaciar.", bold_lead="Conservación:"))
body.append(bullet("Caudal: alrededor de 18.400 pasajeros generados por corrida contra 18.532 del perfil SBASE.", bold_lead="Caudal:"))
body.append(bullet("Números aleatorios comunes: E0 y E1 de cada par generan exactamente la misma demanda; solo cambia la cantidad de molinetes.", bold_lead="Números aleatorios comunes:"))
body.append(bullet("Reproducibilidad: la producción se repitió en otra máquina (Windows) con la misma demanda en las 60 corridas y diferencias menores a 0,2 s en el P90 medio.", bold_lead="Reproducibilidad:"))
body.append(bullet("Errores corregidos durante los pilotos: colas orientadas al revés, elección de cola que mandaba a todos al mismo molinete, peatones que quedaban encerrados y trenes inexistentes en el horario.", bold_lead="Errores corregidos durante los pilotos:"))
body.append(paragraph("Cada corrida de la franja completa tarda unos 7 segundos sin animación.", after=150))

# 5. Escenarios
body.append(paragraph(run("5. Escenarios alternativos", bold=True, size=27), style="Heading1", before=120, after=90, keep=True))
body.append(table(
    ["Escenario", "Qué cambia", "Estado"],
    [
        ["E0 Base", "20 molinetes habilitados (19,5 activos en promedio según SBASE)", "Implementado y corrido"],
        ["E1 Capacidad", "Habilitar los 22 molinetes del vestíbulo Principal", "Implementado, corrido y comparado"],
        ["E1-B Ampliación", "28 molinetes (ampliación hipotética; el espacio físico no está verificado)", "Implementado, sin correr"],
        ["E2 Redistribución", "Desviar una fracción del flujo al vestíbulo Plaza mediante señalización", "Definido; en la capa lógica mide solo el alivio de Principal"],
        ["E3 Contactless", "Validación EMV/QR: cambia el tiempo de servicio, no la cantidad de molinetes", "Definido; sin tiempo de validación citable"],
    ],
    [2000, 4300, 2750],
))
body.append(paragraph(
    "En la propuesta inicial E1 era \"abrir los 28 molinetes\". Al procesar el dataset se vio que 28 es el total "
    "de la estación incluyendo los de Plaza: el vestíbulo Principal tiene 22. Por eso E1 pasa a ser 22 y 28 queda "
    "como ampliación hipotética.",
    after=150,
))

# 6. Resultados preliminares
body.append(paragraph(run("6. Resultados preliminares E0 contra E1", bold=True, size=27), style="Heading1", before=120, after=90, keep=True))
body.append(paragraph(
    "30 pares con semilla común, escenario intermedio. Diferencias apareadas D = E1 − E0 con intervalo t; "
    "las tres medidas primarias usan Bonferroni (k = 3, 98,33 % cada una).",
    after=80,
))
body.append(table(
    ["Medida", "E0", "E1", "D", "IC de D"],
    [
        ["P90 de espera (s)", "28,3", "18,5", "−9,8", "[−9,93; −9,63]"],
        ["Proporción con espera > 30 s", "8,5 %", "2,1 %", "−6,4 pp", "[−6,5; −6,2] pp"],
        ["P90 de espera en el pico 08:15-08:45 (s)", "36,7", "25,6", "−11,1", "[−11,36; −10,74]"],
        ["Espera media (s)", "10,9", "7,4", "−3,5", "[−3,51; −3,42]"],
        ["Cola máxima (personas)", "230", "170", "−60", "[−62,0; −58,8]"],
        ["Utilización media", "26,1 %", "23,7 %", "−2,4 pp", "—"],
    ],
    [3550, 1150, 1150, 1250, 1950],
    centers=(1, 2, 3, 4),
))
body.append(paragraph(rich(
    ("Lectura. ", True),
    "Con los supuestos del escenario intermedio, habilitar los 22 molinetes reduce el P90 de espera en un 35 % "
    "y la proporción de pasajeros que esperan más de 30 s de 8,5 % a 2,1 %. Ningún intervalo contiene el cero.",
), after=90))
body.append(paragraph(rich(
    ("Limitación. ", True),
    "Los intervalos son muy angostos porque todas las réplicas usan el mismo día medio de SBASE: miden la "
    "variabilidad del modelo, no la diferencia entre días reales. La espera real no puede validarse, porque el "
    "dataset registra validaciones y no colas; las conclusiones quedan condicionadas a los rangos de entrada.",
), after=150))

# 7. Próximos pasos
body.append(paragraph(run("7. Próximos pasos", bold=True, size=27), style="Heading1", before=120, after=90, keep=True))
body.append(bullet("Sensibilidad: correr los contextos optimista y pesimista de los rangos y, si el tiempo alcanza, variar el día hábil entre réplicas."))
body.append(bullet("Incorporar planos y datos de SBASE y Trenes Argentinos si responden antes del cierre."))
body.append(bullet("Redactar el informe final en LaTeX siguiendo los diez pasos y grabar el video de presentación."))

body.append(paragraph(run("8. Puntos a revisar en la consulta", bold=True, size=27), style="Heading1", before=120, after=90, keep=True))
body.append(bullet("¿Es correcto definir E1 como los 22 molinetes del vestíbulo Principal en lugar de los 28 de la estación?"))
body.append(bullet("¿Aceptan los rangos con fuente para los parámetros sin dato publicado, con el intermedio como comparación principal?"))
body.append(bullet("¿Alcanza con E1 como escenario alternativo corrido, dejando E2 (Plaza) y E3 (EMV/QR) definidos como extensiones, o prefieren correr alguno de ellos?"))

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
<w:ftr xmlns:w="{W}">{paragraph(run("Comisión 401  |  Bonadeo y Estevez  |  avance al 12 de octubre de 2026", color="707070", size=16), after=0, align="center")}</w:ftr>'''

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
<dc:creator>Juan Cruz Bonadeo y Matias Estevez</dc:creator><dc:subject>Avance: modelo base y escenarios</dc:subject>
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
