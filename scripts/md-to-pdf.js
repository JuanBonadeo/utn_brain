#!/usr/bin/env node
/**
 * md-to-pdf.js — Markdown (con LaTeX) -> HTML -> PDF
 *
 * Pensado para los apuntes y resúmenes de la wiki. Renderiza la matemática con
 * KaTeX del lado del servidor (no hace falta JS en el HTML final) e imprime con
 * el Chrome instalado en la Mac vía puppeteer-core.
 *
 * No hay pandoc ni LibreOffice en esta máquina: este es el camino.
 *
 * Uso:
 *   node scripts/md-to-pdf.js <entrada.md> [salida.pdf]
 *   node scripts/md-to-pdf.js <entrada.md> --html-only
 *
 * Opciones:
 *   --html-only   deja solo el .html (no abre Chrome)
 *   --no-toc      sin índice
 *   --subtitle=".."  subtítulo bajo el título
 */

const fs = require('fs');
const path = require('path');
const katex = require('katex');
const { marked } = require('marked');

// ─────────────────────────────────────────────────────────── args

const argv = process.argv.slice(2);
const flags = argv.filter((a) => a.startsWith('--'));
const positional = argv.filter((a) => !a.startsWith('--'));

if (positional.length === 0) {
  console.error('Uso: node scripts/md-to-pdf.js <entrada.md> [salida.pdf] [--html-only] [--no-toc]');
  process.exit(1);
}

const inputPath = path.resolve(positional[0]);
const outputPdf = positional[1]
  ? path.resolve(positional[1])
  : inputPath.replace(/\.md$/i, '.pdf');
const outputHtml = outputPdf.replace(/\.pdf$/i, '.html');

const htmlOnly = flags.includes('--html-only');
const withToc = !flags.includes('--no-toc');
const subtitleFlag = flags.find((f) => f.startsWith('--subtitle='));
const subtitleArg = subtitleFlag ? subtitleFlag.split('=').slice(1).join('=') : null;

const ROOT = path.resolve(__dirname, '..');
const KATEX_CSS = path.join(ROOT, 'node_modules', 'katex', 'dist', 'katex.min.css');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

// ─────────────────────────────────────────── 1. extraer matemática

// Se saca la matemática ANTES de parsear markdown para que `marked` no
// destroce backslashes, guiones bajos ni asteriscos dentro de las fórmulas.
// Los placeholders son alfanuméricos puros: markdown no los toca.

const mathStore = [];

function stashMath(src) {
  let out = src;

  // Display: $$...$$  (puede ocupar varias líneas)
  out = out.replace(/\$\$([\s\S]+?)\$\$/g, (_m, tex) => {
    const i = mathStore.push({ tex: tex.trim(), display: true }) - 1;
    return `\n\nxxMATHBLOCK${i}ENDxx\n\n`;
  });

  // Inline: $...$  — se ignora \$ (moneda) y $ pegado a dígito ($100)
  out = out.replace(/(^|[^\\$])\$(?!\s)([^$\n]*?[^\\\s])\$(?!\d)/g, (_m, pre, tex) => {
    const i = mathStore.push({ tex: tex.trim(), display: false }) - 1;
    return `${pre}xxMATHINLINE${i}ENDxx`;
  });

  return out;
}

function renderMath(html) {
  return html
    .replace(/xxMATHBLOCK(\d+)ENDxx/g, (_m, i) => renderOne(+i))
    .replace(/xxMATHINLINE(\d+)ENDxx/g, (_m, i) => renderOne(+i));
}

function renderOne(i) {
  const { tex, display } = mathStore[i];
  try {
    return katex.renderToString(tex, {
      displayMode: display,
      throwOnError: false,
      strict: false,
      trust: true,
    });
  } catch (err) {
    console.warn(`  ⚠ KaTeX no pudo con: ${tex.slice(0, 60)}`);
    return `<code class="math-error">${tex}</code>`;
  }
}

// ─────────────────────────────────────────────── 2. leer y parsear

let raw = fs.readFileSync(inputPath, 'utf8');

// El H1 y el blockquote inicial se usan para la portada, no para el cuerpo.
let docTitle = path.basename(inputPath, '.md');
const h1Match = raw.match(/^#\s+(.+)$/m);
if (h1Match) {
  docTitle = h1Match[1].trim();
  raw = raw.replace(h1Match[0], '');
}

// Blockquote que sigue inmediatamente al título -> subtítulo/epígrafe
let lead = '';
const leadMatch = raw.match(/^\s*((?:>.*\n)+)/);
if (leadMatch) {
  lead = leadMatch[1]
    .split('\n')
    .map((l) => l.replace(/^>\s?/, ''))
    .join('\n')
    .trim();
  raw = raw.replace(leadMatch[0], '');
}

const stashed = stashMath(raw);

marked.setOptions({ gfm: true, breaks: false });

// Renderer: recolecta los H2 para el índice y les pone id
const sections = [];
marked.use({
  renderer: {
    heading(token) {
      const text = this.parser.parseInline(token.tokens);
      const level = token.depth;
      if (level === 2) {
        const id = `sec-${sections.length}`;
        sections.push({ id, text: text.replace(/<[^>]+>/g, '').trim() });
        return `<h2 id="${id}">${text}</h2>\n`;
      }
      return `<h${level}>${text}</h${level}>\n`;
    },
    // marked v18 se come los "[ ]" sin dejar <input>: hay que mirar token.task
    listitem(token) {
      const body = this.parser.parse(token.tokens, !!token.loose);
      if (token.task) {
        return `<li class="task${token.checked ? ' done' : ''}">${body}</li>\n`;
      }
      return `<li>${body}</li>\n`;
    },
  },
});

let body = marked.parse(stashed);
body = renderMath(body);

// ────────────────────────────────────────── 3. callouts y detalles

// Convierte los marcadores ⚠️ / ➕ / 📌 al inicio de un bloque en callouts
// con etiqueta de texto (queda mucho mejor impreso que el emoji a color).
const CALLOUTS = [
  { emoji: '⚠️', cls: 'warn', label: 'Atención' },
  { emoji: '➕', cls: 'add', label: 'Agregado' },
  { emoji: '📌', cls: 'exam', label: 'Dato de examen' },
];

for (const { emoji, cls, label } of CALLOUTS) {
  // blockquote que arranca con el marcador
  const bq = new RegExp(`<blockquote>\\s*<p>\\s*(?:⚠️)?${emoji}\\s*`, 'g');
  body = body.replace(bq, `<blockquote class="callout ${cls}"><p><span class="clabel">${label}</span> `);
  // párrafo suelto que arranca con el marcador
  const p = new RegExp(`<p>\\s*(?:⚠️)?${emoji}\\s*`, 'g');
  body = body.replace(p, `<p class="callout inline-callout ${cls}"><span class="clabel">${label}</span> `);
}

// Envolver tablas. Las cortas se mantienen enteras en una página; las largas
// se dejan cortar (si no, empujan media página en blanco) repitiendo el thead.
body = body.replace(/<table>([\s\S]*?)<\/table>/g, (m, inner) => {
  const rows = (inner.match(/<tr>/g) || []).length;
  const cls = rows <= 7 ? 'tw keep' : 'tw';
  return `<div class="${cls}"><table>${inner}</table></div>`;
});

// Un bloque corto que introduce una tabla no debe quedar solo al pie de página
body = body.replace(
  /(<(?:p|blockquote)\b)([^>]*>[\s\S]{0,260}?<\/(?:p|blockquote)>)(\s*)(?=<div class="tw)/g,
  (_m, open, rest, ws) => `${open} data-stick${rest}${ws}`,
);

// ─────────────────────────────────────────────────── 4. índice

let toc = '';
if (withToc && sections.length > 2) {
  const items = sections
    .map((s) => {
      const m = s.text.match(/^(\d+)\.\s*(.*)$/);
      const num = m ? m[1] : '';
      const label = m ? m[2] : s.text;
      return `<li><a href="#${s.id}"><span class="tnum">${num}</span><span class="tlabel">${label}</span></a></li>`;
    })
    .join('\n');
  toc = `<nav class="toc"><h2 class="toc-h">Contenido</h2><ol>${items}</ol></nav>`;
}

// ────────────────────────────────────────────────── 5. plantilla

const katexCss = fs.readFileSync(KATEX_CSS, 'utf8')
  // las fuentes viven al lado del CSS; con file:// hay que apuntar absoluto
  .replace(/url\(fonts\//g, `url(${path.join(path.dirname(KATEX_CSS), 'fonts')}/`);

const subtitle = subtitleArg !== null ? subtitleArg : lead;

const html = `<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>${docTitle}</title>
<style>
${katexCss}
</style>
<style>
:root{
  --ink:#1a1d21;
  --ink-soft:#4a5158;
  --ink-faint:#767d85;
  --rule:#d8dce1;
  --rule-soft:#e9ecef;
  --accent:#1f4b6e;
  --accent-soft:#eef3f7;
  --warn:#9a5b00;
  --warn-bg:#fdf6e9;
  --warn-rule:#e0a340;
  --add:#1f6a45;
  --add-bg:#eef7f2;
  --add-rule:#4d9c75;
  --exam:#5a3d8a;
  --exam-bg:#f3f0f9;
  --exam-rule:#8e70c4;
}

@page{
  size: A4;
  margin: 19mm 17mm 20mm 17mm;
}

*{ box-sizing:border-box; }

html{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }

body{
  margin:0;
  font-family:"Charter","Bitstream Charter","Palatino Linotype",Palatino,Georgia,serif;
  font-size:10.2pt;
  line-height:1.52;
  color:var(--ink);
  text-rendering:optimizeLegibility;
  font-kerning:normal;
  font-variant-numeric:oldstyle-nums proportional-nums;
  hyphens:auto;
}

/* ─── portada / cabecera ─────────────────────────────── */
.masthead{
  border-bottom:2.5pt solid var(--accent);
  padding-bottom:9pt;
  margin-bottom:5pt;
}
.eyebrow{
  font-family:"Avenir Next","Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size:7.6pt;
  font-weight:600;
  letter-spacing:.16em;
  text-transform:uppercase;
  color:var(--accent);
  margin:0 0 5pt;
  font-variant-numeric:lining-nums;
}
h1.doc{
  font-family:"Avenir Next","Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size:25pt;
  font-weight:600;
  letter-spacing:-.018em;
  line-height:1.1;
  margin:0;
  color:var(--ink);
}
.lead{
  margin:9pt 0 0;
  font-size:9.1pt;
  line-height:1.5;
  color:var(--ink-soft);
  max-width:44em;
}
.lead strong{ color:var(--ink); font-weight:600; }
.lead code{ font-size:.92em; }

/* ─── índice ─────────────────────────────────────────── */
.toc{
  margin:16pt 0 4pt;
  padding:11pt 13pt 12pt;
  background:var(--accent-soft);
  border-radius:3pt;
  break-inside:avoid;
}
.toc-h{
  font-family:"Avenir Next","Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size:7.6pt !important;
  font-weight:600;
  letter-spacing:.15em;
  text-transform:uppercase;
  color:var(--accent);
  margin:0 0 7pt !important;
  padding:0 !important;
  border:none !important;
}
.toc ol{
  margin:0; padding:0; list-style:none;
  columns:2; column-gap:22pt;
}
.toc li{ margin:0 0 3.2pt; break-inside:avoid; }
.toc a{
  text-decoration:none; color:var(--ink);
  display:flex; gap:6pt; align-items:baseline;
  font-size:9pt;
}
.tnum{
  font-family:"Avenir Next","Helvetica Neue",Helvetica,Arial,sans-serif;
  font-variant-numeric:lining-nums;
  font-size:8pt; font-weight:600; color:var(--accent);
  min-width:1.15em; text-align:right; flex:none;
}
.tlabel{ flex:1; }

/* ─── títulos ────────────────────────────────────────── */
h1,h2,h3,h4,thead th,.tnum,.clabel,.eyebrow,.toc-h{
  /* los sans llevan numerales de caja alta: si no, el 0 de "0." parece una o */
  font-variant-numeric:lining-nums proportional-nums;
}
h2{
  font-family:"Avenir Next","Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size:14.2pt;
  font-weight:600;
  letter-spacing:-.012em;
  line-height:1.22;
  color:var(--accent);
  margin:23pt 0 8pt;
  padding-bottom:4pt;
  border-bottom:.9pt solid var(--rule);
  break-after:avoid;
  break-inside:avoid;
}
h2:first-of-type{ margin-top:17pt; }
h3{
  font-family:"Avenir Next","Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size:10.6pt;
  font-weight:600;
  letter-spacing:-.005em;
  color:var(--ink);
  margin:14pt 0 5pt;
  break-after:avoid;
  break-inside:avoid;
}
h4{
  font-family:"Avenir Next","Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size:9.4pt; font-weight:600; color:var(--ink-soft);
  margin:11pt 0 4pt; break-after:avoid;
}

p{ margin:0 0 7pt; orphans:2; widows:2; }

[data-stick]{ break-after:avoid; }

strong{ font-weight:600; }
em{ font-style:italic; }

a{ color:var(--accent); text-decoration:none; }

hr{
  border:none;
  border-top:.8pt solid var(--rule-soft);
  margin:16pt 0;
}

/* ─── listas ─────────────────────────────────────────── */
ul,ol{ margin:0 0 8pt; padding-left:16pt; }
li{ margin:0 0 3.4pt; }
li>ul, li>ol{ margin-top:3.4pt; }
ul{ list-style:none; padding-left:13pt; }
ul>li{ position:relative; }
ul>li::before{
  content:"·";
  position:absolute; left:-10pt; top:-.08em;
  color:var(--accent);
  font-weight:700; font-size:1.35em;
}
ul>li.task::before{ content:none; }
li.task{
  list-style:none;
  padding-left:16pt;
  text-indent:-16pt;      /* la casilla cuelga; las líneas siguientes alinean */
  margin-bottom:5.6pt;
}
li.task input[type="checkbox"]{
  appearance:none; -webkit-appearance:none;
  width:9pt; height:9pt;
  margin:0 7pt 0 0;
  padding:0;
  vertical-align:-.04em;
  border:1pt solid var(--ink-faint);
  border-radius:1.5pt;
  background:#fff;
  text-indent:0;
}

/* ─── tablas (booktabs) ──────────────────────────────── */
.tw{ margin:9pt 0 11pt; }
.tw.keep{ break-inside:avoid; }
table{
  width:100%;
  border-collapse:collapse;
  font-size:8.9pt;
  line-height:1.4;
}
thead{ display:table-header-group; }
tr{ break-inside:avoid; }
thead th{
  font-family:"Avenir Next","Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size:7.5pt;
  font-weight:600;
  letter-spacing:.075em;
  text-transform:uppercase;
  color:var(--accent);
  text-align:left;
  vertical-align:bottom;
  padding:0 8pt 4.5pt 0;
  border-bottom:.9pt solid var(--accent);
  hyphens:none;        /* si no parte "FÓRMULA" en "FÓRMU-LA" */
  text-wrap:balance;
}
thead th:last-child{ padding-right:0; }
tbody td{
  padding:5pt 8pt 5pt 0;
  vertical-align:top;
  border-bottom:.4pt solid var(--rule-soft);
}
tbody td:last-child{ padding-right:0; }
tbody tr:last-child td{ border-bottom:.9pt solid var(--rule); }
tbody td:first-child{ color:var(--ink); }
table strong{ font-weight:600; }
/* primera columna angosta cuando es un símbolo o un número */
tbody td .katex{ font-size:1em; }

/* ─── citas y callouts ───────────────────────────────── */
blockquote{
  margin:9pt 0 10pt;
  padding:7pt 11pt 7pt 12pt;
  border-left:2.2pt solid var(--rule);
  background:#fafbfc;
  color:var(--ink-soft);
  font-size:9.4pt;
  border-radius:0 2.5pt 2.5pt 0;
  break-inside:avoid;
}
blockquote p:last-child{ margin-bottom:0; }
blockquote strong{ color:var(--ink); }

.callout{
  border-left-width:2.6pt;
  border-radius:0 2.5pt 2.5pt 0;
  break-inside:avoid;
}
p.inline-callout{
  margin:9pt 0 10pt;
  padding:7pt 11pt 7pt 12pt;
  border-left:2.6pt solid var(--rule);
  background:#fafbfc;
  font-size:9.6pt;
}
.callout.warn{ border-left-color:var(--warn-rule); background:var(--warn-bg); color:#4a3a1c; }
.callout.add { border-left-color:var(--add-rule);  background:var(--add-bg);  color:#1d3c2d; }
.callout.exam{ border-left-color:var(--exam-rule); background:var(--exam-bg); color:#33264a; }

.clabel{
  font-family:"Avenir Next","Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size:6.9pt;
  font-weight:700;
  letter-spacing:.11em;
  text-transform:uppercase;
  padding:1.4pt 4.5pt;
  border-radius:2pt;
  margin-right:5pt;
  vertical-align:.1em;
  white-space:nowrap;
  color:#fff;
  background:var(--ink-faint);
}
.callout.warn .clabel{ background:var(--warn-rule); color:#3d2c08; }
.callout.add  .clabel{ background:var(--add-rule);  color:#0d2b1d; }
.callout.exam .clabel{ background:var(--exam-rule); color:#241a3d; }

/* ─── código ─────────────────────────────────────────── */
code{
  font-family:"SF Mono","Menlo",Consolas,monospace;
  font-size:.845em;
  background:#f2f4f6;
  padding:.08em .26em;
  border-radius:2pt;
  color:#33404d;
  font-variant-numeric:lining-nums;
  hyphens:none;              /* si no, parte rutas con guión y confunde */
  word-break:break-word;
}
pre{
  background:#f7f8fa;
  border:.4pt solid var(--rule-soft);
  border-radius:3pt;
  padding:8pt 10pt;
  overflow:hidden;
  font-size:8.4pt;
  line-height:1.42;
  margin:9pt 0 10pt;
  break-inside:avoid;
}
pre code{ background:none; padding:0; font-size:1em; }
.math-error{ background:#fdecec; color:#a12626; }

/* ─── matemática ─────────────────────────────────────── */
.katex{ font-size:1.045em; }
.katex-display{
  margin:10pt 0 11pt;
  break-inside:avoid;
}
.katex-display > .katex{ font-size:1.09em; }
blockquote .katex-display{ margin:7pt 0; }
td .katex-display{ margin:3pt 0; }
td .katex-display > .katex{ font-size:1em; }
</style>
</head>
<body>
<header class="masthead">
  <p class="eyebrow">UTN · Ingeniería en Sistemas · Simulación</p>
  <h1 class="doc">${docTitle}</h1>
</header>
${subtitle ? `<div class="lead">${renderMath(marked.parse(stashMath(subtitle))).replace(/^<p>|<\/p>\s*$/g, '')}</div>` : ''}
${toc}
${body}
</body>
</html>`;

fs.writeFileSync(outputHtml, html, 'utf8');
console.log(`HTML  → ${path.relative(process.cwd(), outputHtml)}`);

if (htmlOnly) process.exit(0);

// ────────────────────────────────────────────── 6. imprimir PDF

(async () => {
  if (!fs.existsSync(CHROME)) {
    console.error(`No encontré Chrome en ${CHROME}. Usá --html-only.`);
    process.exit(1);
  }

  const puppeteer = require('puppeteer-core');
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox', '--font-render-hinting=none'],
  });

  try {
    const page = await browser.newPage();
    await page.goto('file://' + outputHtml, { waitUntil: 'networkidle0' });
    await page.evaluate(() => document.fonts.ready);

    const foot = `
      <div style="width:100%;font-family:'Avenir Next',Helvetica,Arial,sans-serif;
                  font-size:7pt;color:#8b9199;padding:0 17mm;
                  display:flex;justify-content:space-between;align-items:center;">
        <span style="letter-spacing:.07em;">${docTitle.replace(/[<>&]/g, '')}</span>
        <span><span class="pageNumber"></span> / <span class="totalPages"></span></span>
      </div>`;

    await page.pdf({
      path: outputPdf,
      format: 'A4',
      printBackground: true,
      displayHeaderFooter: true,
      headerTemplate: '<div></div>',
      footerTemplate: foot,
      margin: { top: '19mm', bottom: '20mm', left: '17mm', right: '17mm' },
    });

    const kb = (fs.statSync(outputPdf).size / 1024).toFixed(0);
    console.log(`PDF   → ${path.relative(process.cwd(), outputPdf)}  (${kb} KB)`);
  } finally {
    await browser.close();
  }
})();
