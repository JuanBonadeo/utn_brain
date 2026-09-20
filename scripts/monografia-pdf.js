#!/usr/bin/env node
/**
 * monografia-pdf.js — Markdown -> PDF con el formato que piden las cátedras
 * para trabajos monográficos (carátula + índice + numeración de páginas).
 *
 * Cumple: A4, Arial 10, interlineado 1.5, texto justificado, títulos en
 * negrita, números de página, índice automático a partir de los "## ".
 *
 * El .md lleva un frontmatter YAML simple con los datos de carátula:
 *   institucion, facultad, carrera, materia, docente, titulo, subtitulo,
 *   alumnos, anio, comision, fecha
 *
 * Uso:
 *   node scripts/monografia-pdf.js <entrada.md> [salida.pdf] [--html-only]
 */
const fs = require('fs');
const path = require('path');
const { marked } = require('marked');

const argv = process.argv.slice(2);
const flags = argv.filter((a) => a.startsWith('--'));
const pos = argv.filter((a) => !a.startsWith('--'));
if (!pos.length) { console.error('Uso: node scripts/monografia-pdf.js <entrada.md> [salida.pdf]'); process.exit(1); }

const inPath = path.resolve(pos[0]);
const outPdf = pos[1] ? path.resolve(pos[1]) : inPath.replace(/\.md$/i, '.pdf');
const outHtml = outPdf.replace(/\.pdf$/i, '.html');
const htmlOnly = flags.includes('--html-only');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

/* ---------- frontmatter ---------- */
let src = fs.readFileSync(inPath, 'utf8');
const meta = {};
const fm = src.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/);
if (fm) {
  for (const line of fm[1].split('\n')) {
    const m = line.match(/^([a-zA-Z_]+):\s*(.*)$/);
    if (m) meta[m[1]] = m[2].trim().replace(/^["']|["']$/g, '');
  }
  src = src.slice(fm[0].length);
}
const esc = (s) => String(s || '').replace(/[<>&]/g, (c) => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;' }[c]));

/* ---------- índice ---------- */
const toc = [];
src.replace(/^##\s+(.+)$/gm, (_, t) => { toc.push(t.trim()); return _; });

/* ---------- cuerpo ---------- */
const body = marked.parse(src);

const tocHtml = toc.map((t, i) =>
  `<li><span class="t">${esc(t)}</span><span class="dots"></span></li>`).join('');

const html = `<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>${esc(meta.titulo)}</title>
<style>
@page { size: A4; margin: 25mm 25mm 22mm 30mm; }
@page :first { margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
  font-size: 10pt;
  line-height: 1.5;
  color: #000;
  text-align: justify;
  hyphens: auto;
}

/* ---- carátula ---- */
.cover {
  page-break-after: always;
  height: 297mm; width: 210mm;
  padding: 28mm 28mm 32mm 28mm;
  display: flex; flex-direction: column; align-items: center;
  text-align: center;
}
.cover .logo {
  width: 30mm; height: 30mm; border: 1px dashed #999; border-radius: 3px;
  display: flex; align-items: center; justify-content: center;
  font-size: 7.5pt; color: #999; margin-bottom: 8mm; letter-spacing: .04em;
}
.cover .inst { font-size: 13pt; font-weight: bold; line-height: 1.35; }
.cover .fac  { font-size: 11pt; margin-top: 2mm; }
.cover .car  { font-size: 10pt; margin-top: 1.5mm; color: #222; }
.cover .rule { width: 55mm; border-top: 1.2pt solid #000; margin: 10mm 0 9mm; }
.cover .mat  { font-size: 11pt; font-weight: bold; letter-spacing: .05em; text-transform: uppercase; }
.cover .tit  { font-size: 19pt; font-weight: bold; line-height: 1.25; margin: 12mm 0 0; }
.cover .sub  { font-size: 10.5pt; line-height: 1.45; margin: 5mm 6mm 0; color: #333; text-align: center; }
.cover .spacer { flex: 1; }
.cover .datos { width: 100%; font-size: 10pt; line-height: 1.75; text-align: center; }
.cover .datos .k { font-weight: bold; }
.cover .fecha { font-size: 10pt; margin-top: 8mm; }

/* ---- índice ---- */
.toc-page { page-break-after: always; }
h1.toc-h {
  font-size: 13pt; font-weight: bold; text-align: left;
  margin: 0 0 6mm; padding-bottom: 2mm; border-bottom: 1pt solid #000;
}
ol.toc { list-style: none; margin: 0; padding: 0; counter-reset: toc; }
ol.toc li {
  counter-increment: toc; margin: 0 0 2.6mm; font-size: 10pt;
  display: flex; align-items: baseline; text-align: left;
}
ol.toc li .t { }

/* ---- cuerpo ---- */
h2 {
  font-size: 12pt; font-weight: bold; text-align: left;
  margin: 9mm 0 3mm; page-break-after: avoid;
}
h3 {
  font-size: 10.5pt; font-weight: bold; text-align: left;
  margin: 6mm 0 2mm; page-break-after: avoid;
}
h4 { font-size: 10pt; font-weight: bold; text-align: left; margin: 4mm 0 1.5mm; page-break-after: avoid; }
p { margin: 0 0 2.8mm; orphans: 2; widows: 2; }
strong { font-weight: bold; }
em { font-style: italic; }
ul, ol { margin: 0 0 3mm; padding-left: 7mm; }
li { margin-bottom: 1.4mm; }
blockquote {
  margin: 3.5mm 0 3.5mm 6mm; padding-left: 4mm;
  border-left: 2pt solid #666; font-style: italic; color: #1a1a1a;
}
blockquote p { margin-bottom: 1mm; }
hr { border: 0; border-top: .6pt solid #999; margin: 5mm 0; }
code { font-family: "Courier New", monospace; font-size: 9pt; }
a { color: #000; text-decoration: none; word-break: break-all; }

table {
  width: 100%; border-collapse: collapse; margin: 2mm 0 3mm;
  font-size: 8.6pt; line-height: 1.3; page-break-inside: avoid;
}
th, td { border: .6pt solid #444; padding: 1.6mm 2mm; text-align: left; vertical-align: top; }
th { background: #e8e8e8; font-weight: bold; }

/* pie de tabla en cursiva y chico: el párrafo que sigue a una tabla */
table + p em { font-size: 8.4pt; color: #333; }
</style></head><body>

<div class="cover">
  <div class="logo">[LOGO UTN]</div>
  <div class="inst">${esc(meta.institucion)}</div>
  <div class="fac">${esc(meta.facultad)}</div>
  <div class="car">${esc(meta.carrera)}</div>
  <div class="rule"></div>
  <div class="mat">${esc(meta.materia)}</div>
  <div class="tit">${esc(meta.titulo)}</div>
  <div class="sub">${esc(meta.subtitulo)}</div>
  <div class="spacer"></div>
  <div class="datos">
    <div><span class="k">Docente:</span> ${esc(meta.docente)}</div>
    <div><span class="k">Alumno:</span> ${esc(meta.alumnos)}</div>
    <div><span class="k">Comisión:</span> ${esc(meta.comision)}</div>
    <div><span class="k">Año de cursado:</span> ${esc(meta.anio)}</div>
  </div>
  <div class="fecha"><span class="k" style="font-weight:bold;">Fecha de presentación:</span> ${esc(meta.fecha)}</div>
</div>

<div class="toc-page">
  <h1 class="toc-h">Índice</h1>
  <ol class="toc">${tocHtml}</ol>
</div>

${body}
</body></html>`;

fs.writeFileSync(outHtml, html, 'utf8');
console.log(`HTML  → ${path.relative(process.cwd(), outHtml)}`);
if (htmlOnly) process.exit(0);

(async () => {
  if (!fs.existsSync(CHROME)) { console.error(`No encontré Chrome en ${CHROME}. Usá --html-only.`); process.exit(1); }
  const puppeteer = require('puppeteer-core');
  const browser = await puppeteer.launch({
    executablePath: CHROME, headless: true,
    args: ['--no-sandbox', '--font-render-hinting=none'],
  });
  try {
    const page = await browser.newPage();
    await page.goto('file://' + outHtml, { waitUntil: 'networkidle0' });
    await page.evaluate(() => document.fonts.ready);
    const foot = `<div style="width:100%;font-family:Arial,Helvetica,sans-serif;font-size:8pt;
        color:#333;padding:0 25mm 0 30mm;text-align:right;">
        <span class="pageNumber"></span></div>`;
    await page.pdf({
      path: outPdf, format: 'A4', printBackground: true,
      displayHeaderFooter: true, headerTemplate: '<div></div>', footerTemplate: foot,
      margin: { top: '25mm', bottom: '22mm', left: '30mm', right: '25mm' },
    });
    console.log(`PDF   → ${path.relative(process.cwd(), outPdf)}  (${(fs.statSync(outPdf).size / 1024).toFixed(0)} KB)`);
  } finally { await browser.close(); }
})();
