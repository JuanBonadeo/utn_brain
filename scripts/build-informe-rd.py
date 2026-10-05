"""
md -> docx para los informes de RD (Medin), clonando el formato del Informe 2.

El .docx del Informe 2 hace de plantilla: se conserva la carátula, el
encabezado, el pie con numeración, los estilos de títulos y el diseño de las
tablas; se reemplaza todo el cuerpo por el contenido del .md.

Uso (desde la raíz del repo):
    .venv/Scripts/python scripts/build-informe-rd.py <in.md> <out.docx>

El .md arranca con un frontmatter mínimo:
    ---
    numero: 3
    titulo: Capa de Transporte
    encabezado: Capa de Transporte
    ---

Soporta: «# N. Título» (Heading1), «## N.M. Título» (Heading2),
«#### Enunciado» (Heading4), párrafos (una línea cada uno), viñetas «- »,
tablas pipe, bloques ``` (monoespaciado), **negrita**, *itálica*, `código`,
y el par «**Pregunta N: ...**» / «*Respuesta:* ...» del anexo.

El índice queda como campo TOC: hay que actualizarlo abriendo el .docx en Word
(F9) o con scripts/word-finalizar.ps1, que además exporta el PDF.
"""
import re
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

from lxml import etree

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / 'materias/RD/entregables/Informe2_Redes_WiFi7.docx'

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
W = '{%s}' % W_NS
NSDECL = 'xmlns:w="%s"' % W_NS

CONTENT_W = 11906 - 1700 - 1440   # ancho útil de la plantilla, en twips
ARIAL = '<w:rFonts w:ascii="Arial" w:cs="Arial" w:eastAsia="Arial" w:hAnsi="Arial"/>'
MONO = '<w:rFonts w:ascii="Consolas" w:cs="Consolas" w:eastAsia="Consolas" w:hAnsi="Consolas"/>'


def el(xml):
    """Parsea un fragmento w: suelto inyectándole el namespace."""
    xml = re.sub(r'^<(w:\w+)', r'<\1 ' + NSDECL, xml, count=1)
    return etree.fromstring(xml)


# ---------- runs con formato inline ----------
INLINE = re.compile(r'(\*\*.+?\*\*|`[^`]+`|(?<![\w*])\*[^*\s][^*]*?\*(?![\w*]))')


def runs(text, size=24, bold=False, italic=False):
    out = []
    for tok in INLINE.split(text):
        if not tok:
            continue
        b, i, mono = bold, italic, False
        if tok.startswith('**') and tok.endswith('**') and len(tok) > 4:
            tok, b = tok[2:-2], True
        elif tok.startswith('`') and tok.endswith('`'):
            tok, mono = tok[1:-1], True
        elif tok.startswith('*') and tok.endswith('*') and len(tok) > 2:
            tok, i = tok[1:-1], True
        # una negrita puede traer itálica adentro y viceversa: una sola pasada alcanza
        rpr = (MONO if mono else ARIAL)
        if b:
            rpr += '<w:b w:val="1"/><w:bCs w:val="1"/>'
        if i:
            rpr += '<w:i w:val="1"/><w:iCs w:val="1"/>'
        sz = size - 2 if mono else size
        rpr += f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'
        out.append(f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{escape(tok)}</w:t></w:r>')
    return ''.join(out)


def para(text, after=160, before=None, jc='both', **kw):
    bef = f' w:before="{before}"' if before is not None else ''
    return el(f'<w:p><w:pPr><w:spacing w:after="{after}"{bef} w:line="360" w:lineRule="auto"/>'
              f'<w:jc w:val="{jc}"/></w:pPr>{runs(text, **kw)}</w:p>')


def heading(level, text):
    return el(f'<w:p><w:pPr><w:pStyle w:val="Heading{level}"/></w:pPr>'
              f'<w:r><w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>')


def bullet(text):
    return el('<w:p><w:pPr><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
              '<w:spacing w:after="80" w:before="0" w:line="360" w:lineRule="auto"/>'
              '<w:ind w:left="720" w:right="0" w:hanging="360"/><w:jc w:val="both"/></w:pPr>'
              f'{runs(text)}</w:p>')


def code_line(text, first, last):
    bef = 120 if first else 0
    aft = 160 if last else 0
    return el(f'<w:p><w:pPr><w:keepNext w:val="{0 if last else 1}"/><w:keepLines/>'
              '<w:shd w:fill="f2f5f9" w:val="clear"/>'
              f'<w:spacing w:after="{aft}" w:before="{bef}" w:line="240" w:lineRule="auto"/>'
              '<w:ind w:left="284" w:right="284"/></w:pPr>'
              f'<w:r><w:rPr>{MONO}<w:sz w:val="19"/><w:szCs w:val="19"/></w:rPr>'
              f'<w:t xml:space="preserve">{escape(text) or " "}</w:t></w:r></w:p>')


def empty():
    return el('<w:p><w:pPr><w:spacing w:after="160" w:line="360" w:lineRule="auto"/>'
              '<w:jc w:val="both"/></w:pPr></w:p>')


def page_break():
    return el('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')


def toc():
    return el('<w:p><w:pPr><w:spacing w:after="0" w:line="360" w:lineRule="auto"/></w:pPr>'
              '<w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
              '<w:r><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r>'
              '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
              f'<w:r><w:rPr>{ARIAL}<w:sz w:val="24"/></w:rPr><w:t>Actualizar el índice (F9).</w:t></w:r>'
              '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>')


# ---------- tablas, con el diseño de las del Informe 2 ----------
CELL_BORDERS = ('<w:tcBorders>' + ''.join(
    f'<w:{s} w:color="aaaaaa" w:space="0" w:sz="4" w:val="single"/>'
    for s in ('top', 'left', 'bottom', 'right')) + '</w:tcBorders>')
CELL_MAR = ('<w:tcMar><w:top w:w="80" w:type="dxa"/><w:left w:w="120" w:type="dxa"/>'
            '<w:bottom w:w="80" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tcMar>')


def strip_md(s):
    return re.sub(r'\*\*|`|(?<!\w)\*|\*(?!\w)', '', s)


def table(rows):
    ncol = len(rows[0])
    rows = [r + [''] * (ncol - len(r)) for r in rows]
    # ancho por columna: proporcional al texto, con piso para que no se aplasten
    weight = []
    for c in range(ncol):
        lens = [len(strip_md(r[c])) for r in rows]
        # piso: la palabra más larga del encabezado tiene que entrar en una línea
        floor = max(6, max((len(w) for w in strip_md(rows[0][c]).split()), default=0) + 2)
        weight.append(max(floor, min(45, sum(lens) / len(lens) * 0.6 + max(lens) * 0.4)))
    tot = sum(weight)
    widths = [int(CONTENT_W * w / tot) for w in weight]
    widths[-1] += CONTENT_W - sum(widths)
    center = [sum(len(strip_md(r[c])) for r in rows[1:]) / max(1, len(rows) - 1) < 18
              for c in range(ncol)]

    borders = ''.join(f'<w:{s} w:color="000000" w:space="0" w:sz="4" w:val="single"/>'
                      for s in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'))
    xml = [f'<w:tbl><w:tblPr><w:tblW w:w="{CONTENT_W}" w:type="dxa"/><w:jc w:val="center"/>'
           f'<w:tblBorders>{borders}</w:tblBorders><w:tblLayout w:type="fixed"/>'
           '<w:tblLook w:val="0000"/></w:tblPr><w:tblGrid>']
    xml += [f'<w:gridCol w:w="{w}"/>' for w in widths]
    xml.append('</w:tblGrid>')
    for ri, r in enumerate(rows):
        head = ri == 0
        xml.append('<w:tr><w:trPr><w:cantSplit/>' + ('<w:tblHeader w:val="1"/>' if head else '') + '</w:trPr>')
        for ci, cell in enumerate(r):
            shd = '<w:shd w:fill="d6e4f0" w:val="clear"/>' if head else ''
            jc = 'center' if head or center[ci] else 'left'
            xml.append(f'<w:tc><w:tcPr><w:tcW w:w="{widths[ci]}" w:type="dxa"/>{CELL_BORDERS}{shd}{CELL_MAR}'
                       '<w:vAlign w:val="center"/></w:tcPr>'
                       f'<w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:jc w:val="{jc}"/></w:pPr>'
                       f'{runs(cell.strip(), size=22, bold=head)}</w:p></w:tc>')
        xml.append('</w:tr>')
    xml.append('</w:tbl>')
    return el(''.join(xml))


def split_row(line):
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    return [c.strip() for c in line.split('|')]


# ---------- md -> elementos ----------
def parse(md):
    meta = {}
    m = re.match(r'---\n(.*?)\n---\n', md, re.S)
    if m:
        for ln in m.group(1).splitlines():
            k, _, v = ln.partition(':')
            meta[k.strip()] = v.strip()
        md = md[m.end():]

    out = []
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1
            continue
        if ln.startswith('```'):
            i += 1
            block = []
            while i < len(lines) and not lines[i].startswith('```'):
                block.append(lines[i].rstrip())
                i += 1
            i += 1
            for k, b in enumerate(block):
                out.append(code_line(b, k == 0, k == len(block) - 1))
            continue
        if ln.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = split_row(lines[i])
                if not all(re.fullmatch(r':?-{2,}:?', c) for c in cells if c):
                    rows.append(cells)
                i += 1
            out.append(table(rows))
            out.append(empty())
            continue
        h = re.match(r'(#{1,4}) (.+)', ln)
        if h:
            level = len(h.group(1))
            out.append(heading(level, h.group(2).strip()))
            i += 1
            continue
        if re.match(r'\s*[-*] ', ln):
            out.append(bullet(re.sub(r'^\s*[-*] ', '', ln)))
            i += 1
            continue
        q = re.match(r'\*\*(Pregunta \d+:.*)\*\*$', ln)
        if q:
            out.append(para(q.group(1), after=60, before=160, bold=True))
            i += 1
            continue
        a = re.match(r'\*Respuesta:\*\s*(.*)', ln)
        if a:
            p = para(a.group(1))
            p.insert(1, el(f'<w:r><w:rPr>{ARIAL}<w:i w:val="1"/><w:iCs w:val="1"/>'
                           '<w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>'
                           '<w:t xml:space="preserve">Respuesta: </w:t></w:r>'))
            out.append(p)
            i += 1
            continue
        out.append(para(ln))
        i += 1
    return meta, out


def replace_text(node, old, new):
    for t in node.iter(W + 't'):
        if t.text and old in t.text:
            t.text = t.text.replace(old, new)


def main(inp, outp):
    meta, body_els = parse(Path(inp).read_text(encoding='utf-8'))
    zin = zipfile.ZipFile(TEMPLATE)
    doc = etree.fromstring(zin.read('word/document.xml'))
    body = doc.find(W + 'body')
    kids = list(body)

    # carátula: kids[0..25], «Índice»: 26, TOC: 27, salto: 28, cuerpo: 29..-2, sectPr: -1
    toc_idx = next(i for i, e in enumerate(kids) if e.tag == W + 'sdt')
    for e in kids[toc_idx:-1]:
        body.remove(e)
    replace_text(body, 'Trabajo Práctico N.º 2', f'Trabajo Práctico N.º {meta.get("numero", "3")}')
    replace_text(body, 'WiFi 7 (IEEE 802.11be)', meta.get('titulo', ''))
    sect = kids[-1]
    for e in [toc(), page_break()] + body_els:
        sect.addprevious(e)

    styles = zin.read('word/styles.xml').decode('utf-8')
    # nivel de esquema explícito para que el TOC \o los levante en cualquier idioma de Word
    for sid, lvl in (('Heading1', 0), ('Heading2', 1)):
        styles = re.sub(r'(<w:style [^>]*w:styleId="%s">.*?<w:pPr>)' % sid,
                        r'\1<w:outlineLvl w:val="%d"/>' % lvl, styles, count=1, flags=re.S)

    with zipfile.ZipFile(outp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == 'word/document.xml':
                data = etree.tostring(doc, xml_declaration=True, encoding='UTF-8', standalone=True)
            elif item.filename == 'word/styles.xml':
                data = styles.encode('utf-8')
            elif item.filename.startswith('word/header'):
                data = data.decode('utf-8').replace('WiFi 7', meta.get('encabezado', meta.get('titulo', ''))).encode('utf-8')
            zout.writestr(item, data)
    print(f'ok: {outp} ({len(body_els)} bloques)')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
