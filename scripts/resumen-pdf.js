#!/usr/bin/env node
/**
 * resumen-pdf.js — Markdown -> PDF con el estilo de los resúmenes de cursada
 * (tipo Google Docs): Arial, texto justificado, títulos en negrita, carátula
 * mínima con índice paginado (puntos guía + nº de página) y nº de página abajo
 * a la derecha. Sin colores ni recuadros.
 *
 * Uso (desde la raíz del repo):
 *   node scripts/resumen-pdf.js <entrada.md> [salida.pdf] [--html-only]
 *
 * Estructura esperada del .md:
 *   # TÍTULO                      → título de la carátula (negrita, subrayado)
 *   **línea** / párrafos          → líneas de la carátula (hasta el primer "## ")
 *   ## Sección                    → título de sección; va al índice
 *   ### Subsección                → va al índice, con sangría
 *
 * Sección de preguntas: si el título de un "## " contiene "Preguntas", los
 * párrafos que empiezan con **N) …** se toman como preguntas (negrita) y todo
 * lo que sigue hasta la próxima pregunta como respuesta (con sangría).
 *
 * Un "## Respuestas" arranca en página nueva (bancos de ejercicios con las
 * respuestas al final). Las imágenes se centran y se achican.
 *
 * Marcas "(Tanenbaum)" / "(conocimiento general)" en itálica salen en gris chico.
 *
 * Números de página del índice: dos pasadas. Se imprime, se lee con pdftotext
 * (poppler) en qué página cayó cada título y se vuelve a imprimir. Si no hay
 * pdftotext, el índice sale sin números.
 */
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { marked } = require('marked');

function detectChrome() {
  if (process.env.CHROME_PATH && fs.existsSync(process.env.CHROME_PATH)) return process.env.CHROME_PATH;
  const c = {
    darwin: ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'],
    win32: [
      'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
      'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
      path.join(process.env.LOCALAPPDATA || '', 'Google\\Chrome\\Application\\chrome.exe'),
      'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
    ],
    linux: ['/usr/bin/google-chrome', '/usr/bin/chromium-browser', '/usr/bin/chromium'],
  }[process.platform] || [];
  return c.find((p) => p && fs.existsSync(p)) || null;
}

const argv = process.argv.slice(2);
const flags = argv.filter((a) => a.startsWith('--'));
const pos = argv.filter((a) => !a.startsWith('--'));
if (!pos[0]) {
  console.error('Uso: node scripts/resumen-pdf.js <entrada.md> [salida.pdf] [--html-only]');
  process.exit(1);
}
const inMd = path.resolve(pos[0]);
const outPdf = path.resolve(pos[1] || inMd.replace(/\.md$/, '.pdf'));
const outHtml = outPdf.replace(/\.pdf$/, '.html');
const htmlOnly = flags.includes('--html-only');

/* ─────────────── md → partes ─────────────── */
const raw = fs.readFileSync(inMd, 'utf8').replace(/\r\n/g, '\n');
const cut = raw.search(/^## /m);
const head = cut >= 0 ? raw.slice(0, cut) : raw;
const body = cut >= 0 ? raw.slice(cut) : '';
const titleMatch = head.match(/^#\s+(.+)$/m);
const title = titleMatch ? titleMatch[1].trim() : path.basename(inMd, '.md');
const coverLines = head.replace(/^#\s+.+$/m, '').trim();

const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const strip = (s) => s.replace(/\*\*|__|\*|`/g, '').trim();

const heads = [];
let n = 0;
const renderer = new marked.Renderer();
renderer.heading = function ({ tokens, depth, text }) {
  const inner = this.parser.parseInline(tokens);
  if (depth === 2 || depth === 3) {
    const id = `h${++n}`;
    heads.push({ id, depth, text: strip(text) });
    const cls = depth === 2 && /^respuestas$/i.test(strip(text)) ? ' class="answers"' : '';
    return `<h${depth} id="${id}"${cls}>${inner}</h${depth}>\n`;
  }
  return `<h${depth}>${inner}</h${depth}>\n`;
};
marked.setOptions({ renderer, gfm: true });

let bodyHtml = marked.parse(body);
bodyHtml = bodyHtml.replace(/<em>\((Tanenbaum|conocimiento general)\)<\/em>/g, '<span class="src">($1)</span>');
const coverHtml = marked.parse(coverLines);

const tocHtml = heads.map((h) => `
  <div class="toc-row d${h.depth}"><a href="#${h.id}">${esc(h.text)}</a><span class="dots"></span><span class="pg" data-for="${h.id}"></span></div>`).join('');

const css = `
@page { size: A4; margin: 22mm 22mm 20mm 25mm; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #fff; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #000;
       text-align: justify; hyphens: auto; -webkit-hyphens: auto; }
a { color: inherit; text-decoration: none; }

.cover { page-break-after: always; }
.cover h1 { font-size: 16pt; font-weight: bold; text-decoration: underline; margin: 0 0 6pt; text-align: left; }
.cover p { margin: 0 0 2pt; font-size: 11pt; text-align: left; }
.toc-title { font-weight: bold; font-size: 11pt; margin: 14mm 0 4pt; }
.toc-row { display: flex; align-items: baseline; font-size: 10.5pt; margin: 0 0 3pt; text-align: left; }
.toc-row.d3 { padding-left: 8mm; font-size: 10pt; }
.toc-row .dots { flex: 1; border-bottom: 1px dotted #000; margin: 0 3pt 3pt; min-width: 10mm; }
.toc-row .pg { min-width: 6mm; text-align: right; }

h2 { font-size: 14pt; font-weight: bold; margin: 20pt 0 8pt; break-after: avoid; text-align: left; }
.cover + h2 { margin-top: 0; }
h3 { font-size: 11.5pt; font-weight: bold; margin: 14pt 0 5pt; break-after: avoid; text-align: left; }
h4 { font-size: 10.5pt; font-weight: bold; margin: 10pt 0 4pt; break-after: avoid; }
p { margin: 0 0 6pt; }
strong { font-weight: bold; }

ul, ol { margin: 0 0 7pt; padding-left: 7mm; }
li { margin: 0 0 3pt; }
ul { list-style: none; }
ul > li { position: relative; }
ul > li::before { content: "-"; position: absolute; left: -4.5mm; }
ol { list-style: decimal; }

table { width: 100%; border-collapse: collapse; margin: 4pt 0 9pt; font-size: 9.5pt; line-height: 1.3;
        break-inside: avoid; text-align: left; }
th, td { border: 0.6pt solid #000; padding: 3pt 5pt; vertical-align: top; }
th { font-weight: bold; background: #efefef; }
tr { break-inside: avoid; }

pre { font-family: Menlo, Consolas, "Courier New", monospace; font-size: 8.6pt; line-height: 1.35;
      border: 0.6pt solid #888; background: #f7f7f7; padding: 5pt 7pt; margin: 4pt 0 9pt;
      white-space: pre; overflow: hidden; break-inside: avoid; text-align: left; }
code { font-family: Menlo, Consolas, "Courier New", monospace; font-size: 9pt; }
pre code { font-size: inherit; }
blockquote { margin: 4pt 0 8pt; padding: 0 0 0 7pt; border-left: 1.5pt solid #000; }
hr { border: 0; border-top: 0.6pt solid #000; margin: 10pt 0; }

h2.answers { break-before: page; margin-top: 0; }
img { display: block; max-width: 55%; max-height: 62mm; margin: 4pt auto 8pt; }
.src { font-size: 8.5pt; color: #555; font-style: italic; font-weight: normal; }

/* preguntas y respuestas */
.q { font-weight: bold; margin: 11pt 0 4pt; break-after: avoid; text-align: left; }
.a { margin-left: 7mm; }
ul.a, ol.a { margin-left: 7mm; }
`;

const html = `<!doctype html><html lang="es"><head><meta charset="utf-8"><title>${esc(title)}</title>
<style>${css}</style></head><body>
<section class="cover">
  <h1>${esc(title)}</h1>
  ${coverHtml}
  <div class="toc-title">Índice</div>
  ${tocHtml}
</section>
${bodyHtml}
<script>
/* marcar preguntas/respuestas dentro de los "## ...Preguntas..." */
(function(){
  const h2s=[...document.querySelectorAll('h2')].filter(h=>/preguntas/i.test(h.textContent));
  h2s.forEach(h=>{
    let el=h.nextElementSibling, inQ=false;
    while(el && el.tagName!=='H2'){
      const isQ = el.tagName==='P' && el.firstElementChild && el.firstElementChild.tagName==='STRONG'
                  && /^\\d+\\)/.test(el.textContent.trim()) && el.firstElementChild.textContent.length>=el.textContent.trim().length-1;
      if(isQ){ el.classList.add('q'); inQ=true; }
      else if(el.tagName==='H3'){ inQ=false; }
      else if(inQ){ el.classList.add('a'); }
      el=el.nextElementSibling;
    }
  });
})();
</script>
</body></html>`;

fs.writeFileSync(outHtml, html);
if (htmlOnly) { console.log(`HTML  → ${path.relative(process.cwd(), outHtml)}`); process.exit(0); }

/* ─────────────── pdf en dos pasadas ─────────────── */
function hasPdftotext() {
  // Algunas builds (la de Git Bash en Windows) salen con código 99 en -v:
  // solo cuenta como ausente si no se encuentra el binario.
  try { execFileSync('pdftotext', ['-v'], { stdio: 'ignore' }); return true; }
  catch (e) { return e.code !== 'ENOENT'; }
}
const norm = (s) => s.normalize('NFC').replace(/\s+/g, ' ').trim();

(async () => {
  const CHROME = detectChrome();
  if (!CHROME) { console.error('No encontré Chrome/Edge. Definí CHROME_PATH o usá --html-only.'); process.exit(1); }
  const puppeteer = require('puppeteer-core');
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: true,
    args: ['--no-sandbox', '--font-render-hinting=none'] });
  try {
    const page = await browser.newPage();
    await page.goto('file://' + outHtml, { waitUntil: 'networkidle0' });
    await page.evaluate(() => document.fonts.ready);
    const foot = `<div style="width:100%;font-family:Arial,Helvetica,sans-serif;font-size:8.5pt;
      padding:0 22mm 0 25mm;text-align:right;color:#000;"><span class="pageNumber"></span></div>`;
    const print = () => page.pdf({ path: outPdf, format: 'A4', printBackground: true,
      displayHeaderFooter: true, headerTemplate: '<div></div>', footerTemplate: foot, preferCSSPageSize: true });

    await print();
    if (hasPdftotext()) {
      // -layout: sin él, el pdftotext de xpdf pega el título con el párrafo siguiente.
      const txt = execFileSync('pdftotext', ['-layout', '-enc', 'UTF-8', outPdf, '-'], { encoding: 'utf8' });
      // Un título ocupa su propia línea: se busca primero como línea exacta
      // (evita que "OSPF" matchee dentro de "OSPF y BGP") y, si no aparece
      // (título partido en dos líneas), como texto dentro de la página.
      const pagesLines = txt.split('\f').map((pg) => pg.split('\n').map(norm).filter(Boolean));
      const pagesFlat = pagesLines.map((ls) => ls.join(' '));
      const nums = {};
      let from = 1; // la página 0 es la carátula
      for (const h of heads) {
        const key = norm(h.text);
        let found = -1;
        for (let i = from; i < pagesLines.length; i++) if (pagesLines[i].includes(key)) { found = i; break; }
        if (found < 0) for (let i = from; i < pagesFlat.length; i++) if (pagesFlat[i].includes(key)) { found = i; break; }
        if (found >= 0) { nums[h.id] = found + 1; from = found; }
      }
      await page.evaluate((m) => {
        document.querySelectorAll('.pg').forEach((s) => { s.textContent = m[s.dataset.for] || ''; });
      }, nums);
      await print();
      const miss = heads.filter((h) => !nums[h.id]).map((h) => h.text);
      if (miss.length) console.warn('Sin nº de página en el índice:', miss.join(' | '));
    } else {
      console.warn('No hay pdftotext: el índice sale sin números de página.');
    }
    fs.unlinkSync(outHtml);
    console.log(`PDF   → ${path.relative(process.cwd(), outPdf)}  (${(fs.statSync(outPdf).size / 1024).toFixed(0)} KB)`);
  } finally { await browser.close(); }
})();
