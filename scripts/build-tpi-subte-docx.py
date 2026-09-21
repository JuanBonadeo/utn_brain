#!/usr/bin/env python3
"""Construye la ficha breve del TPI de molinetes como DOCX sin dependencias externas."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from datetime import datetime, timezone
from html import escape


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "materias/SIM/entregables/TPI/subte/TPI_Subte_Definicion_y_Modelo_Inicial.docx"

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
body.append(paragraph(run("TPI Simulación de molinetes de subte", bold=True, size=34),
                      style="Title", after=70, line=360, keep=True))
body.append(paragraph(run("Definición del caso y modelo inicial en AnyLogic", size=23, color="404040"),
                      style="Subtitle", after=210, line=280, keep=True))
body.append(table(
    ["Dato", "Definición"],
    [
        ["Integrantes", "Juan Cruz Bonadeo (53533) y Matias Estevez (53528)"],
        ["Comisión", "401"],
        ["Docente", "Guillermo Leale"],
        ["Fecha de reunión", "Miércoles 23 de septiembre de 2026"],
        ["Estado", "Tema aprobado el 20 de septiembre y modelo inicial preparado"],
    ],
    [2450, 6600],
))
body.append(paragraph(rich(
    ("Resultado actual. ", True),
    "El caso ya está definido y cuenta con evidencia de SBASE. También se preparó un modelo inicial en AnyLogic con los escenarios E0 a E3. Para calibrarlo faltan las mediciones de tiempo de servicio y estructura de las tandas, además de ejecutar el proyecto completo en el IDE.",
), after=180))

body.append(paragraph(run("Definición del caso", bold=True, size=27), style="Heading1", before=140, after=90, keep=True))
body.append(table(
    ["Dimensión", "Alcance"],
    [
        ["Sistema", "Línea de molinetes del vestíbulo Principal de Constitución"],
        ["Línea y estación", "Línea C, estación Constitución"],
        ["Días", "Días hábiles"],
        ["Franja", "07:00 a 09:30"],
        ["Pico", "08:15 a 08:45"],
        ["Unidad", "Un pasajero que ingresa al subte"],
    ],
    [2450, 6600],
))
body.append(paragraph(rich(
    ("Problema de decisión. ", True),
    "Se evaluará cuánto mejoran las esperas al habilitar más molinetes, redistribuir parte del flujo hacia el vestíbulo Plaza o modificar el tiempo de validación mediante EMV y QR.",
)))
body.append(paragraph(rich(
    ("Por qué requiere simulación. ", True),
    "En promedio, cada molinete recibe un pasajero cada 8,5 segundos, mientras una validación demora aproximadamente 2 a 3 segundos. Un modelo de colas basado solo en promedios anticiparía poca congestión. La cola aparece porque los pasajeros llegan en tandas desde la terminal del Ferrocarril Roca; la simulación representa esa congestión transitoria.",
), after=150))

body.append(paragraph(run("Evidencia disponible", bold=True, size=27), style="Heading1", before=120, after=90, keep=True))
body.append(table(
    ["Indicador", "Valor observado"],
    [
        ["Base analizada", "117 días hábiles depurados, enero a junio de 2026"],
        ["Demanda 07:00 a 09:30", "17.482 pasajeros por día hábil"],
        ["Máximo medio", "2.066 pasajeros cada 15 minutos a las 08:30"],
        ["Molinetes", "28 instalados, 21 con tráfico real y 19,5 activos en promedio"],
        ["Participación por vestíbulo", "Principal 84,7 % y Plaza 15,3 %"],
        ["Desbalance observado", "Turn14 procesa 1.485 pasajeros y Turn23 129 en la franja"],
    ],
    [3600, 5450],
))
body.append(paragraph(rich(
    ("Fuente. ", True),
    "BA Data, Viajes Molinetes 2026. Los conteos se encuentran desagregados por molinete y por intervalos de 15 minutos.",
), after=140))

body.append(paragraph(run("Modelo inicial en AnyLogic", bold=True, size=27), style="Heading1", before=120, after=90, keep=True))
body.append(paragraph(run("Source por tandas  ->  Queue  ->  Seize  ->  Delay  ->  Release  ->  Sink",
                          bold=True, color="17365D", size=21), align="center", before=30, after=130, line=260))
body.append(paragraph(
    "Cada agente representa un pasajero. Source inyecta varios pasajeros simultáneamente; Queue conserva el orden FIFO; Seize toma un molinete del ResourcePool; Delay representa la validación; Release libera el recurso y Sink registra la salida. Los arribos se detienen a las 09:30 y el modelo continúa hasta procesar a todos los pasajeros que llegaron dentro de la franja.",
    after=140,
))
body.append(table(
    ["Parámetro", "Estado"],
    [
        ["Cantidad base de molinetes", "20 como aproximación entera provisional de 19,5"],
        ["Cantidad en E1", "28, sujeto a confirmar su disponibilidad para ingreso"],
        ["Tiempo de servicio SUBE", "Pendiente de medición en campo"],
        ["Tiempo de servicio EMV y QR", "Pendiente de medición en campo"],
        ["Tamaño de tanda", "Pendiente de medición en campo"],
        ["Intervalo entre tandas", "Pendiente de medición en campo"],
    ],
    [3600, 5450],
))

body.append(paragraph(run("Escenarios", bold=True, size=27), style="Heading1", before=130, after=90, keep=True))
body.append(table(
    ["Escenario", "Cambio evaluado"],
    [
        ["E0 Base", "Configuración actual con aproximadamente 20 molinetes activos"],
        ["E1 Capacidad", "Habilitar los 28 molinetes instalados"],
        ["E2 Redistribución", "Desviar una fracción del flujo hacia el vestíbulo Plaza"],
        ["E3 Contactless", "Cambiar el tiempo de servicio por el medido para EMV y QR"],
    ],
    [2450, 6600],
))
body.append(paragraph(
    "E2 mide por ahora el alivio sobre el vestíbulo Principal y contabiliza a los pasajeros desviados. Para recomendar una mejora sobre toda la estación será necesario incorporar la capacidad, el flujo propio y la cola de Plaza.",
    after=150,
))

body.append(paragraph(run("Medidas de rendimiento", bold=True, size=27), style="Heading1", before=120, after=90, keep=True))
body.append(paragraph(run("Medidas principales", bold=True, size=22), style="Heading2", after=60, keep=True))
body.append(bullet("Tiempo de espera en cola por pasajero, expresado como media y percentil 90."))
body.append(bullet("Proporción de pasajeros con una espera superior a 30 segundos."))
body.append(bullet("Tiempo de disipación de cada tanda, desde su llegada hasta que la cola vuelve a cero."))
body.append(paragraph(run("Medidas secundarias", bold=True, size=22), style="Heading2", before=70, after=60, keep=True))
body.append(bullet("Largo promedio temporal de la cola y máximo por réplica."))
body.append(bullet("Utilización de los molinetes y dispersión entre unidades."))
body.append(bullet("Pasajeros procesados y balance de la cohorte al cierre de la franja."))
body.append(paragraph(
    "La comparación final utilizará corridas múltiples. Se recomendará una configuración por su percentil 90 de espera únicamente si el intervalo de confianza del 95 % de la diferencia apareada frente a E0 no contiene cero.",
    after=150,
))

body.append(paragraph(run("Estado para la reunión", bold=True, size=27), style="Heading1", before=120, after=90, keep=True))
body.append(table(
    ["Estado", "Elemento"],
    [
        ["Listo", "Línea, estación, vestíbulo, días, franja y pico definidos"],
        ["Listo", "Datos SBASE perfilados y fundamento del uso de simulación"],
        ["Listo", "Escenarios E0 a E3 y medidas de rendimiento"],
        ["Listo", "Modelo inicial y parámetros expuestos en AnyLogic"],
        ["Pendiente", "Medición de servicio, tandas, molinetes habilitados y cola observada"],
        ["Pendiente", "Compilación y ejecución completa del proyecto en el IDE"],
        ["Pendiente", "Edición del último envío del formulario con el tema del subte"],
    ],
    [2100, 6950],
    centers=(0,),
))
body.append(paragraph(rich(
    ("Próximo paso. ", True),
    "Realizar la medición en campo, cargar los parámetros en el modelo y validar sus colas y caudales contra una jornada independiente.",
), before=30, after=0))

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
<w:ftr xmlns:w="{W}">{paragraph(run("Comisión 401  |  Bonadeo y Estevez  |  20 de septiembre de 2026", color="707070", size=16), after=0, align="center")}</w:ftr>'''

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
<dc:creator>Juan Cruz Bonadeo y Matias Estevez</dc:creator><dc:subject>Definición del caso y modelo inicial en AnyLogic</dc:subject>
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
