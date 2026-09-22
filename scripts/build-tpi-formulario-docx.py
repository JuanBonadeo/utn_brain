#!/usr/bin/env python3
"""Construye el formulario de propuesta de tema del TPI (v2, subte) como DOCX sin dependencias externas."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from datetime import datetime, timezone
from html import escape


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "materias/SIM/entregables/TPI/TPI_Simulacion_Propuesta_de_Tema.docx"

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
    if bold_lead and text.startswith(bold_lead):
        parts = rich((bold_lead, True), text[len(bold_lead):], size=20)
    else:
        parts = rich(text, size=20)
    p = paragraph(parts, after=55, line=250, left=520, hanging=300)
    return p.replace("<w:pPr>", '<w:pPr><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>', 1)


body = []
body.append(paragraph(run("TPI Simulación — Propuesta de tema", bold=True, size=34),
                      style="Title", after=70, line=360, keep=True))
body.append(paragraph(run("Versión 2 — molinetes de Constitución, Línea C", size=23, color="404040"),
                      style="Subtitle", after=210, line=280, keep=True))

body.append(table(
    ["Dato", "Definición"],
    [
        ["Integrantes", "Juan Cruz Bonadeo (53533) y Matias Estevez (53528)"],
        ["Comisión", "401 — Facultad Regional Rosario"],
        ["Docente", "Guillermo Leale"],
        ["Estado", "Tema confirmado por mail el 20 de septiembre de 2026"],
    ],
    [2450, 6600],
))
body.append(paragraph(rich(
    ("Nota. ", True),
    "Esta versión reemplaza la propuesta del 31 de julio. El docente confirmó el tema del subte por mail "
    "el 2026-09-20 (“Vamos con lo del subte… Completen el formulario con este tema. Editen su último "
    "envío.”) y pidió llegar al miércoles 23/09 con el caso definido.",
), after=180))

body.append(paragraph(run("Tema", bold=True, size=27), style="Heading1", before=140, after=90, keep=True))
body.append(paragraph(
    "Simulación de la línea de molinetes del vestíbulo Principal de la estación Constitución de la Línea C "
    "del subte de Buenos Aires durante el pico de la mañana de los días hábiles, para evaluar el efecto de la "
    "cantidad de molinetes habilitados y de la velocidad de validación sobre el tiempo de espera de los "
    "pasajeros que llegan en tandas desde la terminal ferroviaria Roca.",
    after=150,
))

body.append(paragraph(run("Observaciones", bold=True, size=27), style="Heading1", before=120, after=90, keep=True))
body.append(paragraph(
    "Elegimos este caso porque es el punto del sistema donde el fenómeno de cola es más nítido y porque los "
    "datos de entrada son públicos y de granularidad fina. El Gobierno de la Ciudad publica, para cada "
    "molinete individual y cada ventana de 15 minutos, la cantidad de pasajeros que lo atravesaron; sobre la "
    "serie de enero a junio de 2026 verificamos que las catorce ventanas de quince minutos más cargadas de "
    "todo el subte corresponden a Constitución, que en el pico de 08:15 a 08:45 el vestíbulo principal recibe "
    "unos 2.066 pasajeros cada cuarto de hora con alrededor de veinte molinetes activos sobre veintiocho "
    "instalados, y que la franja de 07:00 a 09:30 concentra 17.482 pasajeros por día hábil. Lo que hace que "
    "el caso justifique simulación, y no una fórmula de colas, es que a esa intensidad cada molinete recibe "
    "un pasajero cada ocho segundos y medio contra un tiempo de validación del orden de dos a tres segundos: "
    "en promedio el sistema está lejos de saturarse y un modelo analítico concluiría que no hay cola, cuando "
    "en la práctica sí la hay. La cola se forma porque Constitución es la terminal del Ferrocarril Roca y los "
    "pasajeros no llegan de a uno sino en tandas, cada vez que arriba una formación. Es un caso de congestión "
    "transitoria por arribos en lote sobre un sistema subutilizado en promedio, que es exactamente donde la "
    "simulación de eventos discretos aporta lo que el cálculo no da. La hipótesis de mejora es concreta y de "
    "costo bajo: habilitar los molinetes instalados que hoy permanecen cerrados en la franja pico, redistribuir "
    "el flujo hacia el segundo vestíbulo de la estación, que absorbe solo el quince por ciento del total, o "
    "acelerar la validación con pago contactless, que la estación ya tiene instalado en un molinete y por lo "
    "tanto es medible y no un supuesto.",
    after=150,
))

body.append(paragraph(run("Anexo — respaldo técnico", bold=True, size=30), style="Heading1",
                      before=180, after=90, keep=True, page_break=True))

body.append(paragraph(run("Definición del caso, según lo pedido el 2026-09-20", bold=True, size=24),
                      style="Heading2", after=70, keep=True))
body.append(table(
    ["Qué pidió el docente", "Respuesta"],
    [
        ["Qué línea en específico", "Línea C, estación Constitución, vestíbulo Principal (84,7 % del flujo de la estación)"],
        ["Qué horarios o franjas", "07:00 a 09:30, con pico en 08:15 a 08:45"],
        ["Qué días", "Días hábiles, excluyendo 11 feriados que el propio dato identifica"],
        ["Medidas de rendimiento", "Espera en cola (media y percentil 90), proporción con espera > 30 s, tiempo de disipación de la tanda; como secundarias Lq, utilización por molinete y throughput"],
    ],
    [2450, 6600],
))

body.append(paragraph(run("Verificación de los criterios de selección del enunciado (§5)", bold=True, size=24),
                      style="Heading2", before=100, after=70, keep=True))
body.append(table(
    ["Criterio", "Cómo lo cumple"],
    [
        ["1. Aleatoriedad relevante", "Arribos en tandas de tamaño e intervalo aleatorios y tiempo de validación variable. El CV del flujo entre días en la ventana pico es 0,24"],
        ["2. Datos disponibles", "Verificado: serie 2013-2026 por molinete individual cada 15 min. Perfilados 117 días hábiles de 2026"],
        ["3. Hipótesis de mejora", "Molinetes habilitados (E1), redistribución entre vestíbulos (E2), validación contactless (E3)"],
        ["4. Alcance acotable", "Una estación, un vestíbulo, una franja de dos horas y media"],
    ],
    [2450, 6600],
))

body.append(paragraph(run("Escenarios", bold=True, size=24), style="Heading2", before=100, after=70, keep=True))
body.append(bullet("E0 — base: ~19,5 molinetes activos de 28, con la distribución de carga observada."))
body.append(bullet("E1 — abrir los 28 molinetes instalados durante la franja pico."))
body.append(bullet("E2 — redistribuir flujo hacia el vestíbulo Plaza, hoy con el 15 % del total."))
body.append(bullet("E3 — validación contactless EMV/QR: cambia el tiempo de servicio, no la cantidad de servidores."))
body.append(paragraph("", after=60))

body.append(paragraph(run("Estado de los datos", bold=True, size=24), style="Heading2", before=80, after=70, keep=True))
body.append(table(
    ["Dataset", "Origen", "Estado"],
    [
        ["Subte — Viajes Molinetes 2026 (ene-jun), por molinete y 15 min", "BA Data", "Descargado y perfilado (45 MB zip → 548 MB CSV)"],
        ["Series 2013-2025", "mismo dataset", "Disponibles para ampliar el horizonte"],
        ["Tiempo de servicio del molinete", "no existe en ningún dataset", "Medición en campo pendiente"],
        ["Estructura de las tandas", "el agregado de 15 min la borra", "Medición en campo pendiente"],
    ],
    [3300, 2900, 2850],
))
body.append(paragraph(rich(
    ("Reproducible con ", False), ("scripts/sbase-perfil.py", False, True), (". Los CSV no se commitean.", False),
    size=19,
), after=140))

body.append(paragraph(run("Limitaciones a declarar en el informe", bold=True, size=24),
                      style="Heading2", before=80, after=70, keep=True))
body.append(bullet(
    "Los molinetes registran a quien pasó, no a quien esperó: la cola es salida del modelo y no puede "
    "validarse contra el dataset. Se resuelve midiendo el largo de cola en campo."
))
body.append(bullet(
    "Posible censura por capacidad en el pico: si los molinetes saturan, el conteo mide el caudal máximo "
    "del molinete y no la demanda real."
))
body.append(bullet(
    "El campo de hora cambia de formato según el mes (marzo y abril de 2026 usan HH:MM, el resto "
    "HH:MM:SS). Agregar sin normalizar parte cada hora en dos, en silencio."
))
body.append(bullet(
    "Molinetes con registro casi nulo en seis meses (Turn07, 3 pasajeros) — fuera de servicio o mal "
    "identificados. Se excluyen."
))
body.append(paragraph("", after=60))

body.append(paragraph(run("Historial de la propuesta", bold=True, size=24), style="Heading2", before=80, after=70, keep=True))
body.append(paragraph(
    "La versión del 31/07 presentaba dos temas: Ecobici (rebalanceo en el corredor Constitución/Retiro-"
    "Catalinas) y despacho de emergencias de San Francisco. Ecobici quedó descartado porque otro grupo lo "
    "tomó primero. El tema de molinetes de subte figuraba en esa versión como candidato de reserva y es el "
    "que el docente aprobó el 2026-09-20.",
    after=100,
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
<w:hdr xmlns:w="{W}">{paragraph(run("SIM  |  TPI  |  PROPUESTA DE TEMA  —  MOLINETES DE CONSTITUCIÓN", bold=True, color="606060", size=16), after=0)}</w:hdr>'''
footer_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="{W}">{paragraph(run("Comisión 401  |  Bonadeo y Estevez  |  versión 2 — 20 de septiembre de 2026", color="707070", size=16), after=0, align="center")}</w:ftr>'''

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
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>TPI Simulación — Propuesta de tema</dc:title>
<dc:creator>Juan Cruz Bonadeo y Matias Estevez</dc:creator><dc:subject>Versión 2 — molinetes de Constitución</dc:subject>
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
