/*
 * md -> docx para los entregables de ASI.
 * El .md del repo es la fuente de verdad; este script solo lo renderiza.
 *
 * Uso (desde la raíz del repo):
 *   NODE_PATH=<scratchpad>/docxbuild/node_modules \
 *     node scripts/build-docx.js materias/ASI/entregable.md materias/ASI/entregable.docx
 *
 * Soporta:
 *   #  título del documento (centrado)
 *   ## sección          ### campo/apartado          #### subapartado
 *   párrafos justificados, listas «- » y «1. », > citas, ---, tablas
 *   **negrita**, *itálica*, `código`
 *   lo que contiene ⚠ sale en rojo (marcador interno, sacar antes de entregar)
 *
 * Ancho de columnas de una tabla: poner antes de la tabla, en el .md,
 *   <!-- cols: 5,25,25,15,15,15 -->   (porcentajes, suman 100)
 * Si no se indica, reparte en partes iguales.
 *
 * Ignora todo lo anterior al primer "## " (bloque de notas internas del .md).
 */
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType,
  TableLayoutType, VerticalAlign, Footer, PageNumber,
} = require('docx');

const [, , inPath, outPath] = process.argv;
if (!inPath || !outPath) { console.error('Uso: build-docx.js <in.md> <out.docx>'); process.exit(1); }

/* ---------- constantes de página y estilo ---------- */
const FONT = 'Arial';
const A4 = { width: 11906, height: 16838 };
const MARGIN = 1134;                              // 2 cm
const CONTENT_W = A4.width - MARGIN * 2;          // 9638 twips
const BODY = 22;                                  // 11 pt
const TBL = 18;                                   // 9 pt
const INK = '1A1A1A';
const RED = 'B00020';
const GRID_H = 'C7CBCF';   // horizontales de tabla
const GRID_V = 'E2E5E8';   // verticales de tabla, más tenues
const HEAD_FILL = 'F4F5F6';

const line = (color, size) => ({ style: BorderStyle.SINGLE, size, color });

/* ---------- inline ---------- */
function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)/g;
  let last = 0, m;
  const push = (t, extra) => {
    if (!t) return;
    out.push(new TextRun({ text: t, font: FONT, size: BODY, color: INK, ...base, ...extra }));
  };
  while ((m = re.exec(text)) !== null) {
    push(text.slice(last, m.index));
    const tok = m[0];
    if (tok.startsWith('**')) push(tok.slice(2, -2), { bold: true });
    else if (tok.startsWith('`')) push(tok.slice(1, -1), { font: 'Consolas', size: (base.size || BODY) - 2 });
    else push(tok.slice(1, -1), { italics: true });
    last = m.index + tok.length;
  }
  push(text.slice(last));
  return out.length ? out : [new TextRun({ text: '', font: FONT, size: base.size || BODY })];
}

const warn = (s) => (s.includes('⚠') ? { color: RED, italics: true } : {});

const para = (text, opts = {}) => new Paragraph({
  children: runs(text, { ...warn(text), ...(opts.runProps || {}) }),
  alignment: opts.alignment ?? AlignmentType.JUSTIFIED,
  spacing: { after: 140, line: 288, ...(opts.spacing || {}) },
  ...(opts.bullet ? { bullet: opts.bullet } : {}),
  ...(opts.numbering ? { numbering: opts.numbering } : {}),
  ...(opts.indent ? { indent: opts.indent } : {}),
});

/* ---------- tablas ---------- */
function buildTable(rows, colPct) {
  const nCols = rows[0].length;
  const pct = (colPct && colPct.length === nCols)
    ? colPct
    : new Array(nCols).fill(100 / nCols);
  const widths = pct.map((p) => Math.round((CONTENT_W * p) / 100));
  // corrige el redondeo en la última columna
  widths[nCols - 1] += CONTENT_W - widths.reduce((a, b) => a + b, 0);

  const body = rows.slice(2); // saltea la fila de guiones

  // en columnas angostas justificar deja ríos horribles: solo se justifica
  // el texto de las columnas anchas
  const JUSTIFY_MIN = 22;
  const mkRow = (cells, head) => new TableRow({
    tableHeader: head,
    cantSplit: true,
    children: cells.map((c, idx) => new TableCell({
      width: { size: widths[idx], type: WidthType.DXA },
      verticalAlign: head ? VerticalAlign.CENTER : VerticalAlign.TOP,
      shading: head ? { type: ShadingType.CLEAR, color: 'auto', fill: HEAD_FILL } : undefined,
      margins: { top: 90, bottom: 90, left: 120, right: 120 },
      children: [new Paragraph({
        children: runs(c, { size: TBL, ...(head ? { bold: true } : {}), ...warn(c) }),
        alignment: (!head && pct[idx] >= JUSTIFY_MIN)
          ? AlignmentType.JUSTIFIED : AlignmentType.LEFT,
        spacing: { before: 0, after: 0, line: 252 },
      })],
    })),
  });

  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    layout: TableLayoutType.FIXED,
    borders: {
      top: line(GRID_H, 4), bottom: line(GRID_H, 4),
      left: line(GRID_V, 2), right: line(GRID_V, 2),
      insideHorizontal: line(GRID_H, 2), insideVertical: line(GRID_V, 2),
    },
    rows: [mkRow(rows[0], true), ...body.map((r) => mkRow(r, false))],
  });
}

/* ---------- encabezados ---------- */
function heading(level, text) {
  const clean = text.replace(/\*\*/g, '');
  // Nada de filetes: la jerarquía se marca con cuerpo, mayúsculas,
  // espaciado entre letras y aire alrededor.
  if (level === 1 || level === 2) {
    const isTitle = level === 1;
    return new Paragraph({
      heading: isTitle ? HeadingLevel.TITLE : HeadingLevel.HEADING_1,
      alignment: AlignmentType.CENTER,
      keepNext: true,
      spacing: { before: isTitle ? 0 : 560, after: 260 },
      children: [new TextRun({
        text: clean.toUpperCase(), font: FONT, bold: true,
        size: isTitle ? 30 : 25, color: INK, characterSpacing: 30,
      })],
    });
  }
  if (level === 3) {
    return new Paragraph({
      heading: HeadingLevel.HEADING_2,
      keepNext: true,
      spacing: { before: 400, after: 140 },
      children: [new TextRun({
        text: clean.toUpperCase(), font: FONT, bold: true,
        size: 21, color: INK, characterSpacing: 18,
      })],
    });
  }
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    keepNext: true,
    spacing: { before: 280, after: 110 },
    children: [new TextRun({ text: clean, font: FONT, bold: true, size: 22, color: INK })],
  });
}

/* ---------- parser ---------- */
const src = fs.readFileSync(inPath, 'utf8');
const start = src.indexOf('\n## ');
const lines = (start >= 0 ? src.slice(start + 1) : src).split('\n');

const children = [];
let pendingCols = null;
let i = 0;

while (i < lines.length) {
  const line0 = lines[i].trimEnd();
  const trimmed = line0.trim();

  if (!trimmed) { i++; continue; }

  // directiva de anchos de columna
  const cols = trimmed.match(/^<!--\s*cols:\s*([\d.,\s]+)\s*-->$/);
  if (cols) { pendingCols = cols[1].split(',').map((n) => parseFloat(n.trim())); i++; continue; }
  if (trimmed.startsWith('<!--')) { i++; continue; }

  if (trimmed === '---') {
    children.push(new Paragraph({ text: '', spacing: { before: 0, after: 260 } }));
    i++; continue;
  }

  if (trimmed.startsWith('|')) {
    const rows = [];
    while (i < lines.length && lines[i].trim().startsWith('|')) {
      rows.push(lines[i].trim().replace(/^\||\|$/g, '').split('|').map((c) => c.trim()));
      i++;
    }
    children.push(buildTable(rows, pendingCols));
    pendingCols = null;
    children.push(new Paragraph({ text: '', spacing: { after: 200 } }));
    continue;
  }

  const h = line0.match(/^(#{1,4})\s+(.*)$/);
  if (h) { children.push(heading(h[1].length, h[2])); i++; continue; }

  if (trimmed.startsWith('>')) {
    const buf = [];
    while (i < lines.length && lines[i].trim().startsWith('>')) {
      buf.push(lines[i].trim().replace(/^>\s?/, '')); i++;
    }
    const txt = buf.join(' ').trim();
    children.push(new Paragraph({
      children: runs(txt, { size: 20, ...warn(txt) }),
      alignment: AlignmentType.JUSTIFIED,
      indent: { left: 454, right: 454 },
      spacing: { before: 180, after: 260, line: 264 },
    }));
    continue;
  }

  const ul = trimmed.match(/^[-*]\s+(.*)$/);
  if (ul) {
    const buf = [ul[1]]; i++;
    while (i < lines.length && /^\s{2,}\S/.test(lines[i]) && lines[i].trim()) { buf.push(lines[i].trim()); i++; }
    children.push(para(buf.join(' '), { bullet: { level: 0 }, spacing: { after: 100, line: 276 } }));
    continue;
  }

  const ol = trimmed.match(/^(\d+)\.\s+(.*)$/);
  if (ol) {
    const buf = [ol[2]]; i++;
    while (i < lines.length && /^\s{2,}\S/.test(lines[i]) && lines[i].trim()) { buf.push(lines[i].trim()); i++; }
    children.push(para(buf.join(' '), { numbering: { reference: 'ol', level: 0 }, spacing: { after: 100, line: 276 } }));
    continue;
  }

  const buf = [trimmed]; i++;
  while (i < lines.length && lines[i].trim()
         && !/^([-*]\s|>|#{1,4}\s|\||\d+\.\s|---$|<!--)/.test(lines[i].trim())) {
    buf.push(lines[i].trim()); i++;
  }
  children.push(para(buf.join(' ')));
}

/* ---------- documento ---------- */
const doc = new Document({
  hyphenation: { autoHyphenation: true },
  numbering: {
    config: [{
      reference: 'ol',
      levels: [{
        level: 0, format: 'decimal', text: '%1.', alignment: AlignmentType.START,
        style: { paragraph: { indent: { left: 640, hanging: 340 } } },
      }],
    }],
  },
  styles: { default: { document: { run: { font: FONT, size: BODY, color: INK } } } },
  sections: [{
    properties: {
      page: {
        size: { width: A4.width, height: A4.height },
        margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN },
      },
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 120 },
          children: [new TextRun({
            children: ['Página ', PageNumber.CURRENT, ' de ', PageNumber.TOTAL_PAGES],
            font: FONT, size: 16, color: '6B7075',
          })],
        })],
      }),
    },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outPath, buf);
  console.log(`Escrito: ${outPath} (${buf.length} bytes)`);
});
