#!/usr/bin/env node
/**
 * build.js — Informe final del TPI UTNHub (SGD) en PDF.
 *
 * Toma materias/SGD/entregables/utnhub/informe-utnhub.md, lo pasa a HTML con
 * el estilo del informe de referencia (Aptos, títulos numerados en azul
 * #0F4761, carátula con el logo de la UTN) y lo imprime con Chrome.
 *
 * Dos pasadas: la primera imprime con outline (marcadores) para saber en qué
 * página cae cada título; la segunda vuelve a imprimir con esos números en el
 * índice.
 *
 * Uso (desde la raíz del repo):  node scripts/sgd/utnhub-informe/build.js
 */
const fs = require('fs');
const path = require('path');
const os = require('os');
const { execFileSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..', '..', '..');
const { marked } = require(path.join(ROOT, 'node_modules', 'marked'));
const puppeteer = require(path.join(ROOT, 'node_modules', 'puppeteer-core'));

const SRC = path.join(ROOT, 'materias/SGD/entregables/utnhub/informe-utnhub.md');
const OUT = path.join(ROOT, 'materias/SGD/entregables/utnhub/informe-utnhub.pdf');
const HTML = path.join(os.tmpdir(), 'informe-utnhub.html');

const CHROME = [
  process.env.CHROME_PATH,
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
].find((p) => p && fs.existsSync(p));

/* Aptos: viene con Office como "cloud font". Si no está, cae a Segoe/Helvetica. */
const fontDir = path.join(process.env.LOCALAPPDATA || '', 'Microsoft/FontCache/4/CloudFonts');
function fontFace() {
  if (!fs.existsSync(fontDir)) return '';
  let python = path.join(ROOT, '.venv/Scripts/python.exe');
  if (!fs.existsSync(python)) python = path.join(ROOT, '.venv/bin/python');
  let map;
  try {
    map = JSON.parse(execFileSync(python, ['-c', `
import glob, json
from PIL import ImageFont
out = {}
for f in glob.glob(r'${fontDir}/Aptos*/*.ttf'):
    fam, sty = ImageFont.truetype(f, 10).getname()
    out.setdefault(sty, f)
print(json.dumps(out))`]).toString());
  } catch { return ''; }
  const want = [
    ['Aptos', 'Regular', 400, 'normal'], ['Aptos', 'Italic', 400, 'italic'],
    ['Aptos', 'SemiBold', 600, 'normal'], ['Aptos', 'Bold', 700, 'normal'],
    ['Aptos', 'Bold Italic', 700, 'italic'],
    ['Aptos Display', 'Display', 400, 'normal'], ['Aptos Display', 'Display Bold', 700, 'normal'],
  ];
  return want.filter(([, s]) => map[s]).map(([fam, s, w, st]) =>
    `@font-face{font-family:"${fam}";src:url("file:///${map[s].replace(/\\/g, '/')}");font-weight:${w};font-style:${st};}`
  ).join('\n');
}

/* ───────────── markdown → html ───────────── */
const raw = fs.readFileSync(SRC, 'utf8');
const fm = {};
const body = raw.replace(/^---\n([\s\S]*?)\n---\n/, (_, y) => {
  let key = null;
  for (const line of y.split('\n')) {
    const m = line.match(/^(\w+):\s*(.*)$/);
    if (m) { key = m[1]; fm[key] = m[2] ? m[2].replace(/^"|"$/g, '') : []; }
    else if (/^\s+-\s+/.test(line) && key) fm[key].push(line.replace(/^\s+-\s+/, '').replace(/^"|"$/g, ''));
  }
  return '';
});

// numeración de títulos: "## X" → "1 X", "### Y" → "1.1 Y"
const toc = [];
let h2 = 0, h3 = 0;
const slug = (s) => s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '')
  .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const renderer = new marked.Renderer();
renderer.heading = function ({ tokens, depth, text }) {
  const inner = this.parser.parseInline(tokens);
  if (depth === 2 && !/^anexo/i.test(text)) {
    h2++; h3 = 0;
    const id = `s${h2}-${slug(text)}`;
    toc.push({ lvl: 2, num: `${h2}`, text, id });
    return `<h2 id="${id}"><span class="num">${h2}</span>${inner}</h2>`;
  }
  if (depth === 2) {
    const id = slug(text);
    toc.push({ lvl: 2, num: '', text, id });
    return `<h2 id="${id}" class="sin-num">${inner}</h2>`;
  }
  if (depth === 3 && h2) {
    h3++;
    const id = `s${h2}-${h3}-${slug(text)}`;
    toc.push({ lvl: 3, num: `${h2}.${h3}`, text, id });
    return `<h3 id="${id}"><span class="num">${h2}.${h3}</span>${inner}</h3>`;
  }
  return `<h${depth}>${inner}</h${depth}>`;
};
// imágenes: ![pie](ruta) → figura; el número se pone al final, en orden
renderer.image = function ({ href, text }) {
  const src = 'file:///' + path.resolve(path.dirname(SRC), href).replace(/\\/g, '/');
  return `<figure><img src="${src}" alt=""><figcaption><b>Figura #.</b> ${text}</figcaption></figure>`;
};
marked.use({ renderer, gfm: true });
const diagramas = require('./diagramas');
const bodyD = body.replace(/^\{\{diagrama:([\w-]+)\|(.+?)\}\}$/gm, (_, n, pie) => {
  if (!diagramas[n]) throw new Error('Diagrama desconocido: ' + n);
  return `<div class="diagrama">${diagramas[n]()}<div class="pie"><b>Figura #.</b> ${marked.parseInline(pie)}</div></div>`;
});
// un párrafo que es solo una imagen no debe quedar envuelto en <p>; y las
// figuras (capturas y diagramas) se numeran en el orden en que aparecen
let nfig = 0;
const content = marked.parse(bodyD)
  .replace(/<p>\s*(<figure>[\s\S]*?<\/figure>)\s*<\/p>/g, '$1')
  .replace(/<b>Figura #\.<\/b>/g, () => `<b>Figura ${++nfig}.</b>`);

/* ───────────── carátula, índice, estilos ───────────── */
const logo = 'file:///' + path.join(__dirname, 'logo-utn.png').replace(/\\/g, '/');
const integrantes = (fm.integrantes || []).map((l) => {
  const [nombre, legajo] = l.split('|').map((s) => s.trim());
  return `<tr><td>${nombre}</td><td>Legajo ${legajo}</td></tr>`;
}).join('');
const cover = `
<section class="cover">
  <img class="logo" src="${logo}">
  <div class="inst">Universidad Tecnológica Nacional<br>Facultad Regional Rosario</div>
  <div class="catedra">Ingeniería en Sistemas de Información · Cátedra: ${fm.materia}</div>
  <div class="titulo">${fm.titulo}</div>
  <div class="subtitulo">${fm.subtitulo}</div>
  <div class="bloque">
    <div class="rotulo">${fm.grupo}</div>
    <table class="integrantes">${integrantes}</table>
  </div>
  <div class="bloque">
    <div class="rotulo">Profesores</div>
    ${(fm.profesores || []).map((p) => `<div>${p}</div>`).join('')}
  </div>
  <div class="bloque pie">
    <div>Repositorio: <b>${fm.repo}</b></div>
    <div>Aplicación: <b>${fm.app}</b></div>
    <div class="anio">${fm.fecha}</div>
  </div>
</section>`;

function buildToc(pages) {
  const rows = toc.map((t) => `
    <a class="toc-row l${t.lvl}" href="#${t.id}">
      <span class="tnum">${t.num}</span><span class="ttxt">${t.text}</span>
      <span class="dots"></span><span class="tpag">${pages[t.id] || ''}</span>
    </a>`).join('');
  return `<section class="toc"><h1 class="toc-title">Índice</h1>${rows}</section>`;
}

const css = `
${fontFace()}
:root{ --azul:#0F4761; --azul2:#156082; --tinta:#1b1f24; --gris:#5b6470; --linea:#d5dde4; --fondo:#f2f6f9; }
@page{ size:A4; }
*{ box-sizing:border-box; }
html{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }
body{ margin:0; font-family:"Aptos","Segoe UI","Helvetica Neue",Arial,sans-serif; font-size:11pt;
  line-height:1.5; color:var(--tinta); text-align:left; hyphens:auto; }
p{ margin:0 0 8pt; orphans:3; widows:3; }
strong{ font-weight:700; color:#0c2533; }
a{ color:var(--azul2); text-decoration:none; }
h2,h3,h4{ font-family:"Aptos Display","Aptos","Segoe UI",sans-serif; font-weight:400; color:var(--azul);
  break-after:avoid; page-break-after:avoid; }
h2{ font-size:20pt; margin:26pt 0 10pt; padding-bottom:5pt; border-bottom:1.2pt solid var(--azul); }
h2 .num, h3 .num{ display:inline-block; min-width:1.9em; color:var(--azul2); font-weight:700; }
h2 .num{ min-width:1.4em; }
h3{ font-size:14pt; margin:18pt 0 6pt; }
h4{ font-size:11.5pt; font-weight:700; margin:12pt 0 4pt; color:var(--azul2); }
h2 + h3{ margin-top:8pt; }
ul,ol{ margin:0 0 8pt; padding-left:20pt; }
li{ margin:2pt 0; }
li::marker{ color:var(--azul2); }
code{ font-family:Consolas,"Cascadia Mono",monospace; font-size:9pt; background:var(--fondo);
  padding:0.5pt 3pt; border-radius:2pt; color:#0c3a52; }
pre{ background:var(--fondo); border-left:3pt solid var(--azul2); padding:7pt 10pt; font-size:8.6pt;
  line-height:1.35; white-space:pre-wrap; break-inside:avoid; margin:0 0 10pt; }
pre code{ background:none; padding:0; }
table{ width:100%; border-collapse:collapse; margin:4pt 0 12pt; font-size:9.6pt; line-height:1.35; break-inside:auto; }
thead{ display:table-header-group; }
tr{ break-inside:avoid; }
th{ background:var(--azul); color:#fff; font-weight:600; text-align:left; padding:5pt 7pt; }
td{ padding:4.5pt 7pt; border-bottom:0.6pt solid var(--linea); vertical-align:top; }
tbody tr:nth-child(even) td{ background:#f7fafc; }
blockquote{ margin:6pt 0 12pt; padding:8pt 12pt; background:var(--fondo); border-left:3pt solid var(--azul2);
  border-radius:0 3pt 3pt 0; break-inside:avoid; }
blockquote p:last-child{ margin-bottom:0; }
figure{ margin:8pt 0 14pt; break-inside:avoid; text-align:center; }
figure img{ max-width:100%; max-height:118mm; border:0.6pt solid var(--linea); border-radius:3pt; }
figure svg{ max-width:100%; }
figcaption{ font-size:9pt; color:var(--gris); margin-top:4pt; }
figcaption b{ color:var(--azul); }
.diagrama{ margin:6pt 0 14pt; break-inside:avoid; text-align:center; }
.diagrama .pie{ font-size:9pt; color:var(--gris); margin-top:4pt; }
.diagrama .pie b{ color:var(--azul); }
.kpis{ display:grid; grid-template-columns:repeat(4,1fr); gap:6pt; margin:6pt 0 14pt; break-inside:avoid; }
.kpi{ border:0.6pt solid var(--linea); border-top:2.5pt solid var(--azul2); border-radius:3pt; padding:6pt 8pt; }
.kpi .v{ font-family:"Aptos Display","Aptos",sans-serif; font-size:17pt; color:var(--azul); line-height:1.1; }
.kpi .l{ font-size:8.4pt; color:var(--gris); line-height:1.25; margin-top:2pt; }
.dos{ display:grid; grid-template-columns:1fr 1fr; gap:10pt; }
.dos figure{ margin-bottom:6pt; }

/* carátula */
.cover{ height:247mm; display:flex; flex-direction:column; align-items:center; text-align:center; padding-top:4mm; break-after:page; }
.cover .logo{ width:26mm; margin-bottom:5mm; }
.cover .inst{ font-size:13pt; letter-spacing:.5pt; line-height:1.35; color:#111; }
.cover .catedra{ font-size:9.5pt; color:var(--gris); margin-top:3mm; }
.cover .titulo{ font-family:"Aptos Display","Aptos",sans-serif; font-size:40pt; color:var(--azul); margin-top:26mm; line-height:1.05; letter-spacing:-.5pt; }
.cover .subtitulo{ font-size:13pt; color:#333; margin-top:4mm; max-width:140mm; line-height:1.35; }
.cover .bloque{ margin-top:12mm; font-size:10.5pt; line-height:1.45; }
.cover .rotulo{ font-weight:700; color:var(--azul); font-size:10.5pt; margin-bottom:2mm; text-transform:none; }
.cover table.integrantes{ width:auto; margin:0 auto; font-size:10pt; }
.cover table.integrantes td{ border:none; padding:1pt 7pt; background:none !important; text-align:left; }
.cover table.integrantes td:nth-child(2){ color:var(--gris); }
.cover table.integrantes td:nth-child(3){ color:var(--gris); }
.cover .pie{ margin-top:auto; font-size:9.5pt; color:var(--gris); }
.cover .pie b{ color:var(--azul2); font-weight:600; }
.cover .anio{ margin-top:3mm; font-size:11pt; color:#111; }

/* índice */
.toc{ break-after:page; }
.toc-title{ font-family:"Aptos Display","Aptos",sans-serif; font-weight:400; color:var(--azul); font-size:22pt;
  margin:0 0 12pt; padding-bottom:5pt; border-bottom:1.2pt solid var(--azul); }
.toc-row{ display:flex; align-items:baseline; color:var(--tinta); }
.toc-row.l2{ font-weight:700; margin-top:7pt; font-size:11pt; }
.toc-row.l3{ padding-left:18pt; font-size:10pt; margin-top:1.5pt; color:#333; }
.tnum{ min-width:24pt; color:var(--azul2); }
.toc-row.l3 .tnum{ min-width:28pt; }
.dots{ flex:1; border-bottom:0.8pt dotted #9aa7b2; margin:0 5pt; transform:translateY(-3pt); }
.tpag{ min-width:14pt; text-align:right; }
`;

function html(pages) {
  return `<!doctype html><html lang="es"><head><meta charset="utf-8"><title>${fm.titulo}</title>
<style>${css}</style></head><body>${cover}${buildToc(pages)}<main>${content}</main></body></html>`;
}

/* ───────────── impresión en dos pasadas ───────────── */
(async () => {
  if (!CHROME) { console.error('No encontré Chrome. Definí CHROME_PATH.'); process.exit(1); }
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: true,
    args: ['--allow-file-access-from-files', '--font-render-hinting=none'] });
  const foot = `<div style="width:100%;font-family:Aptos,'Segoe UI',Arial,sans-serif;font-size:8pt;color:#6b7680;
    padding:0 20mm;display:flex;justify-content:space-between;">
    <span>UTNHub · Informe final del TPI · Grupo 7</span><span class="pageNumber"></span></div>`;
  const opts = { format: 'A4', printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<div></div>', footerTemplate: foot,
    margin: { top: '22mm', bottom: '20mm', left: '22mm', right: '22mm' } };

  async function print(pages, outline) {
    fs.writeFileSync(HTML, html(pages), 'utf8');
    const page = await browser.newPage();
    await page.goto('file:///' + HTML.replace(/\\/g, '/'), { waitUntil: 'networkidle0' });
    await page.evaluate(() => document.fonts.ready);
    const buf = await page.pdf({ ...opts, outline, tagged: true });
    await page.close();
    return buf;
  }

  // pasada 1: ubicar títulos buscando su texto en el PDF
  const tmpPdf = path.join(os.tmpdir(), 'informe-utnhub-p1.pdf');
  fs.writeFileSync(tmpPdf, await print({}, false));
  let python = path.join(ROOT, '.venv/Scripts/python.exe');
  if (!fs.existsSync(python)) python = path.join(ROOT, '.venv/bin/python');
  const needles = toc.map((t) => ({ id: t.id, s: (t.num ? t.num + ' ' : '') + t.text }));
  const pages = JSON.parse(execFileSync(python, ['-c', `
import json, sys, re, pymupdf
needles = json.loads(sys.argv[2]); doc = pymupdf.open(sys.argv[1])
norm = lambda s: re.sub(r'\\s+', ' ', s).strip()
texts = [norm(p.get_text()) for p in doc]
out = {}; start = 2
for n in needles:
    for i in range(start, len(texts)):
        if norm(n['s']) in texts[i]:
            out[n['id']] = i + 1; start = i; break
print(json.dumps(out))`, tmpPdf, JSON.stringify(needles)]).toString());
  const faltan = toc.filter((t) => !pages[t.id]).map((t) => t.text);
  if (faltan.length) console.warn('Sin página en el índice:', faltan.join(' | '));

  // pasada 2: definitiva
  fs.writeFileSync(OUT, await print(pages, true));
  await browser.close();
  console.log(`PDF → ${path.relative(ROOT, OUT)} (${(fs.statSync(OUT).size / 1024).toFixed(0)} KB)`);
})();
