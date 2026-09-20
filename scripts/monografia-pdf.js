#!/usr/bin/env node
/**
 * monografia-pdf.js — Markdown -> PDF con carátula e índice, en el formato que
 * piden las cátedras para TPs, monografías e informes.
 *
 * Cumple: A4, Arial 10, interlineado 1.5, texto justificado, títulos en negrita,
 * numeración de páginas, índice automático a partir de los "## ".
 *
 * Uso (desde la raíz del repo):
 *   node scripts/monografia-pdf.js materias/XXX/entregables/trabajo.md
 *   node scripts/monografia-pdf.js <entrada.md> [salida.pdf] [opciones]
 *
 * Opciones:
 *   --html-only   deja el .html y no abre Chrome (para depurar estilos)
 *   --no-toc      sin índice
 *   --no-cover    sin carátula (para entregas que no la piden)
 *
 * Los datos fijos de carátula (institución, facultad, carrera, alumno, legajo)
 * salen de scripts/datos-alumno.json. En el .md solo va lo que cambia por
 * trabajo. Plantilla para copiar: scripts/templates/tp.md
 *
 * Frontmatter reconocido:
 *   materia, codigo, tipo, titulo, subtitulo, comision, grupo, etapa, fecha
 *   profesores:  (lista)
 *   alumnos:     (lista, formato "Apellido, Nombre | correo | legajo")
 * Cualquiera de ellos pisa el default de datos-alumno.json.
 */
const fs = require('fs');
const path = require('path');
const { marked } = require('marked');

const ROOT = path.resolve(__dirname, '..');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

const argv = process.argv.slice(2);
const flags = argv.filter((a) => a.startsWith('--'));
const pos = argv.filter((a) => !a.startsWith('--'));
if (!pos.length) {
  console.error('Uso: node scripts/monografia-pdf.js <entrada.md> [salida.pdf] [--html-only] [--no-toc] [--no-cover]');
  process.exit(1);
}

const inPath = path.resolve(pos[0]);
const outPdf = pos[1] ? path.resolve(pos[1]) : inPath.replace(/\.md$/i, '.pdf');
const outHtml = outPdf.replace(/\.pdf$/i, '.html');
const htmlOnly = flags.includes('--html-only');
const withToc = !flags.includes('--no-toc');
const withCover = !flags.includes('--no-cover');

/* ─────────────────────────────── frontmatter ─────────────────────────────
   Parser mínimo: "clave: valor" y listas con "  - item" bajo una clave vacía. */
function parseFrontmatter(text) {
  const meta = {};
  const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/);
  if (!m) return { meta, body: text };
  let key = null;
  for (const raw of m[1].split('\n')) {
    const line = raw.replace(/\s+$/, '');
    if (!line.trim() || line.trim().startsWith('#')) continue;
    const item = line.match(/^\s+-\s+(.*)$/);
    if (item && key) {
      const v = unquote(stripComment(item[1]));
      if (v === '') continue;
      if (!Array.isArray(meta[key])) meta[key] = [];
      meta[key].push(v);
      continue;
    }
    const kv = line.match(/^([a-zA-Z_][\w]*):\s*(.*)$/);
    if (kv) {
      key = kv[1];
      const val = unquote(stripComment(kv[2]));
      meta[key] = val === '' ? [] : val;   // vacío = puede venir una lista abajo
    }
  }
  // las claves que quedaron como [] vacío y nadie llenó, se descartan
  for (const k of Object.keys(meta)) {
    if (Array.isArray(meta[k]) && meta[k].length === 0) delete meta[k];
  }
  return { meta, body: text.slice(m[0].length) };
}
const unquote = (s) => s.trim().replace(/^["'](.*)["']$/, '$1');
/* comentario YAML al final de la línea: " # ...". No se toca si el valor viene
   entrecomillado, para no romper un título que lleve almohadilla. */
const stripComment = (s) => {
  const t = s.trim();
  if (t.startsWith('"') || t.startsWith("'")) return t;
  if (t.startsWith('#')) return '';
  return t.replace(/\s+#.*$/, '').trim();
};
const esc = (s) => String(s ?? '').replace(/[<>&]/g, (c) => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;' }[c]));

/* ─────────────────────────────── datos ─────────────────────────────── */
let defaults = {};
try {
  defaults = JSON.parse(fs.readFileSync(path.join(ROOT, 'scripts/datos-alumno.json'), 'utf8'));
} catch { /* sin archivo de datos: se usa solo el frontmatter */ }

const src = fs.readFileSync(inPath, 'utf8');
const { meta: fmeta, body: mdBody } = parseFrontmatter(src);

const meta = {
  institucion: defaults.institucion,
  facultad: defaults.facultad,
  carrera: defaults.carrera,
  alumnos: defaults.alumnos,
  ...fmeta,
};
// comisión por materia, si no vino explícita
if (!meta.comision && meta.codigo && defaults.comisiones) {
  meta.comision = defaults.comisiones[meta.codigo];
}
const asList = (v) => (Array.isArray(v) ? v : v ? [v] : []);

/* logo: se incrusta como data URI si el archivo existe */
let logoTag = '';
if (defaults.logo) {
  const lp = path.isAbsolute(defaults.logo) ? defaults.logo : path.join(ROOT, defaults.logo);
  if (fs.existsSync(lp)) {
    const ext = path.extname(lp).slice(1).toLowerCase();
    const mime = ext === 'svg' ? 'image/svg+xml' : `image/${ext === 'jpg' ? 'jpeg' : ext}`;
    logoTag = `<img class="logo" src="data:${mime};base64,${fs.readFileSync(lp).toString('base64')}" alt="">`;
  }
}

/* ─────────────────────────────── carátula ─────────────────────────────── */
const alumnos = asList(meta.alumnos).map((a) => a.split('|').map((x) => x.trim()));
const conDatos = alumnos.some((a) => a.length > 1);

const alumnosHtml = !alumnos.length ? '' : conDatos
  ? `<table class="alu"><thead><tr><th>Nombre y Apellido</th><th>Correo electrónico</th><th>Legajo</th></tr></thead><tbody>${
      alumnos.map((a) => `<tr><td>${esc(a[0])}</td><td>${esc(a[1] || '')}</td><td>${esc(a[2] || '')}</td></tr>`).join('')
    }</tbody></table>`
  : `<div class="lista">${alumnos.map((a) => `<div>${esc(a[0])}</div>`).join('')}</div>`;

const profes = asList(meta.profesores);
const profesHtml = profes.length
  ? `<div class="bloque"><div class="rot">${profes.length > 1 ? 'Profesores' : 'Profesor/a'}</div>
     <div class="lista">${profes.map((p) => `<div>${esc(p)}</div>`).join('')}</div></div>` : '';

const cursada = [
  meta.comision ? ['Comisión', meta.comision] : null,
  meta.grupo ? ['Grupo', meta.grupo] : null,
  meta.etapa ? ['Etapa', meta.etapa] : null,
].filter(Boolean);
const cursadaHtml = cursada.length
  ? `<div class="cursada">${cursada.map(([k, v]) => `<span><b>${k}</b> ${esc(v)}</span>`).join('')}</div>` : '';

const cover = !withCover ? '' : `
<div class="cover">
  ${logoTag}
  <div class="inst">${esc(meta.institucion)}</div>
  ${meta.facultad ? `<div class="fac">${esc(meta.facultad)}</div>` : ''}
  ${meta.carrera ? `<div class="car">${esc(meta.carrera)}</div>` : ''}
  <div class="rule"></div>
  ${meta.materia ? `<div class="mat">${esc(meta.materia)}</div>` : ''}
  ${meta.tipo ? `<div class="tipo">${esc(meta.tipo)}</div>` : ''}
  <div class="tit">${esc(meta.titulo)}</div>
  ${meta.subtitulo ? `<div class="sub">${esc(meta.subtitulo)}</div>` : ''}
  ${cursadaHtml}
  <div class="spacer"></div>
  ${profesHtml}
  ${alumnosHtml ? `<div class="bloque"><div class="rot">${alumnos.length > 1 ? 'Alumnos' : 'Alumno'}</div>${alumnosHtml}</div>` : ''}
  ${meta.fecha ? `<div class="fecha"><b>Fecha de entrega:</b> ${esc(meta.fecha)}</div>` : ''}
</div>`;

/* ─────────────────────────────── índice y cuerpo ─────────────────────────────── */
const toc = [];
mdBody.replace(/^##\s+(.+)$/gm, (full, t) => { toc.push(t.trim()); return full; });
const tocHtml = !withToc || !toc.length ? '' : `
<div class="toc-page">
  <h1 class="toc-h">Índice</h1>
  <ul class="toc">${toc.map((t) => `<li>${esc(t)}</li>`).join('')}</ul>
</div>`;

const body = marked.parse(mdBody);

/* ─────────────────────────────── html ─────────────────────────────── */
const html = `<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>${esc(meta.titulo)}</title>
<style>
@page { size: A4; margin: 25mm 25mm 22mm 30mm; }
@page :first { margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
  font-size: 10pt; line-height: 1.5; color: #000;
  text-align: justify; hyphens: auto;
}

/* ---------- carátula ---------- */
.cover {
  page-break-after: always;
  height: 297mm; width: 210mm;
  padding: 26mm 26mm 32mm 26mm;
  display: flex; flex-direction: column; align-items: center; text-align: center;
}
.cover .logo { width: 26mm; margin-bottom: 7mm; }
.cover .inst { font-size: 13pt; font-weight: bold; line-height: 1.35; }
.cover .fac  { font-size: 12pt; font-weight: bold; margin-top: 1.5mm; }
.cover .car  { font-size: 10.5pt; margin-top: 1.5mm; }
.cover .rule { width: 55mm; border-top: 1.2pt solid #000; margin: 9mm 0 8mm; }
.cover .mat  { font-size: 12pt; font-weight: bold; letter-spacing: .05em; text-transform: uppercase; }
.cover .tipo { font-size: 10.5pt; margin-top: 2mm; }
.cover .tit  { font-size: 19pt; font-weight: bold; line-height: 1.25; margin: 11mm 0 0; }
.cover .sub  { font-size: 10.5pt; line-height: 1.45; margin: 5mm 6mm 0; color: #333; text-align: center; }
.cover .cursada { margin-top: 8mm; font-size: 10pt; display: flex; gap: 9mm; }
.cover .spacer { flex: 1; min-height: 8mm; }
.cover .bloque { width: 100%; margin-bottom: 6mm; }
.cover .rot { font-size: 10pt; font-weight: bold; margin-bottom: 2mm; }
.cover .lista { font-size: 10pt; line-height: 1.6; }
.cover table.alu {
  width: 100%; border-collapse: collapse; font-size: 9pt; text-align: left;
}
.cover table.alu th, .cover table.alu td { border: .6pt solid #555; padding: 1.4mm 2mm; }
.cover table.alu th { background: #ececec; font-weight: bold; }
.cover .fecha { font-size: 10pt; margin-top: 3mm; }

/* ---------- índice ---------- */
.toc-page { page-break-after: always; }
h1.toc-h {
  font-size: 13pt; font-weight: bold; text-align: left;
  margin: 0 0 6mm; padding-bottom: 2mm; border-bottom: 1pt solid #000;
}
ul.toc { list-style: none; margin: 0; padding: 0; }
ul.toc li { margin: 0 0 2.6mm; font-size: 10pt; text-align: left; }

/* ---------- cuerpo ---------- */
h2 { font-size: 12pt; font-weight: bold; text-align: left; margin: 9mm 0 3mm; page-break-after: avoid; }
h3 { font-size: 10.5pt; font-weight: bold; text-align: left; margin: 6mm 0 2mm; page-break-after: avoid; }
h4 { font-size: 10pt; font-weight: bold; text-align: left; margin: 4mm 0 1.5mm; page-break-after: avoid; }
p { margin: 0 0 2.8mm; orphans: 2; widows: 2; }
ul, ol { margin: 0 0 3mm; padding-left: 7mm; }
li { margin-bottom: 1.4mm; }
blockquote {
  margin: 3.5mm 0 3.5mm 6mm; padding-left: 4mm;
  border-left: 2pt solid #666; font-style: italic;
}
blockquote p { margin-bottom: 1mm; }
hr { border: 0; border-top: .6pt solid #999; margin: 5mm 0; }
code { font-family: "Courier New", monospace; font-size: 9pt; }
a { color: #000; text-decoration: none; word-break: break-all; }
img { max-width: 100%; }
table {
  width: 100%; border-collapse: collapse; margin: 2mm 0 3mm;
  font-size: 8.6pt; line-height: 1.3; page-break-inside: avoid;
}
th, td { border: .6pt solid #444; padding: 1.6mm 2mm; text-align: left; vertical-align: top; }
th { background: #e8e8e8; font-weight: bold; }
table + p em { font-size: 8.4pt; color: #333; }
</style></head><body>
${cover}
${tocHtml}
${body}
</body></html>`;

fs.writeFileSync(outHtml, html, 'utf8');
console.log(`HTML  → ${path.relative(process.cwd(), outHtml)}`);
if (htmlOnly) process.exit(0);

/* ─────────────────────────────── pdf ─────────────────────────────── */
(async () => {
  if (!fs.existsSync(CHROME)) {
    console.error(`No encontré Chrome en ${CHROME}. Usá --html-only.`);
    process.exit(1);
  }
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
        color:#333;padding:0 25mm 0 30mm;text-align:right;"><span class="pageNumber"></span></div>`;
    await page.pdf({
      path: outPdf, format: 'A4', printBackground: true,
      displayHeaderFooter: true, headerTemplate: '<div></div>', footerTemplate: foot,
      margin: { top: '25mm', bottom: '22mm', left: '30mm', right: '25mm' },
    });
    fs.unlinkSync(outHtml);
    console.log(`PDF   → ${path.relative(process.cwd(), outPdf)}  (${(fs.statSync(outPdf).size / 1024).toFixed(0)} KB)`);
  } finally { await browser.close(); }
})();
