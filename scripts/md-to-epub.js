#!/usr/bin/env node
/**
 * md-to-epub.js — Markdown -> EPUB 3 (con toc.ncx para Kindle)
 *
 * Pensado para leer los resúmenes de estudio en un Kindle (Send to Kindle acepta
 * .epub). No necesita pandoc: usa `marked` y `jszip`, que ya están en node_modules.
 *
 * Uso (desde la raíz del repo):
 *   node scripts/md-to-epub.js <entrada.md> [salida.epub]
 *
 * Estructura esperada del .md (la misma de los resúmenes de estudio/):
 *   # Título                → título del libro
 *   texto / blockquote      → portada (todo lo que hay antes del primer "## ")
 *   ## Capítulo             → un archivo por capítulo; entra al índice
 *   ### Subsección          → entra al índice, anidada bajo su capítulo
 *
 * Las imágenes locales (![](../figs/x.png)) se copian dentro del EPUB. El emoji ⚠️
 * se reemplaza por "Atención:", porque las fuentes del Kindle no lo tienen.
 * No renderiza LaTeX: para apuntes con fórmulas, usar md-to-pdf.js.
 */
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { marked } = require('marked');
const JSZip = require('jszip');

const args = process.argv.slice(2);
if (!args[0]) {
  console.error('Uso: node scripts/md-to-epub.js <entrada.md> [salida.epub]');
  process.exit(1);
}
const input = path.resolve(args[0]);
const output = path.resolve(args[1] || input.replace(/\.md$/i, '.epub'));
const baseDir = path.dirname(input);

const MATERIAS = {
  IO: 'Investigación Operativa', TPA: 'Tecnologías para la Automatización', LEG: 'Legislación',
  SIM: 'Simulación', IYS: 'Ingeniería y Sociedad', RD: 'Redes de Datos',
  SGD: 'Soporte a la Gestión de Datos', ASI: 'Administración de Sistemas de Información',
  IPP: 'Intro a la Práctica Profesional', ISW: 'Ingeniería y Calidad de Software',
};
const cod = (input.split(path.sep).join('/').match(/\/materias\/([A-Z]+)\//) || [])[1];
let autor = 'UTN · Ingeniería en Sistemas';
try {
  const d = JSON.parse(fs.readFileSync(path.join(__dirname, 'datos-alumno.json'), 'utf8'));
  const a = (d.alumnos || [])[0];
  if (a) autor = a.split('|')[0].trim();
} catch (_) { /* sin datos de alumno: queda el genérico */ }

// ─────────────────────────────────────────── partir el markdown

const md = fs.readFileSync(input, 'utf8').replace(/\r\n/g, '\n');
const titulo = (md.match(/^# (.+)$/m) || [, path.basename(input, '.md')])[1].trim();
const partes = md.split(/^(?=## )/m);
const portadaMd = partes[0].replace(/^# .+$/m, '').trim();
const capsMd = partes.slice(1);

// ─────────────────────────────────────────── markdown -> XHTML

const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const sinTags = (s) => s.replace(/<[^>]+>/g, '').replace(/&amp;/g, '&').replace(/&lt;/g, '<')
  .replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'");

const imagenes = new Map(); // ruta local -> nombre dentro del epub

function aXhtml(src) {
  let html = marked.parse(src.replace(/⚠️\s*/g, '**Atención:** '), { gfm: true });
  // imágenes locales: copiarlas al epub
  html = html.replace(/<img([^>]*?)src="([^"]+)"([^>]*)>/g, (m, a, s, b) => {
    if (/^https?:/.test(s)) return `<img${a}src="${s}"${b}/>`;
    const abs = path.resolve(baseDir, decodeURI(s));
    if (!fs.existsSync(abs)) { console.warn('  imagen no encontrada:', s); return ''; }
    if (!imagenes.has(abs)) imagenes.set(abs, `img${imagenes.size + 1}${path.extname(abs).toLowerCase()}`);
    return `<img${a}src="images/${imagenes.get(abs)}"${b.replace(/\/\s*$/, '')}/>`;
  });
  // XHTML bien formado: elementos vacíos cerrados, entidades de HTML a numéricas
  html = html.replace(/<(br|hr)\s*>/g, '<$1/>')
    .replace(/<input([^>]*?)\s*\/?>/g, '<input$1/>')
    .replace(/&nbsp;/g, '&#160;');
  return html;
}

const capitulos = capsMd.map((cmd, i) => {
  const id = `cap${String(i + 1).padStart(2, '0')}`;
  let html = aXhtml(cmd);
  const subs = [];
  let k = 0;
  html = html.replace(/<h2>([\s\S]*?)<\/h2>/, (m, t) => `<h2 id="${id}">${t}</h2>`);
  html = html.replace(/<h3>([\s\S]*?)<\/h3>/g, (m, t) => {
    const sid = `${id}-s${++k}`;
    subs.push({ sid, texto: sinTags(t) });
    return `<h3 id="${sid}">${t}</h3>`;
  });
  const texto = sinTags((html.match(/<h2[^>]*>([\s\S]*?)<\/h2>/) || [, `Capítulo ${i + 1}`])[1]);
  return { id, archivo: `${id}.xhtml`, texto, subs, html };
});

const pagina = (t, cuerpo) => `<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="es" lang="es">
<head><meta charset="utf-8"/><title>${esc(t)}</title><link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
${cuerpo}
</body>
</html>
`;

const css = `body { font-family: serif; line-height: 1.45; margin: 0 0.4em; }
h1 { font-size: 1.6em; text-align: center; margin: 2em 0 0.4em; }
h2 { font-size: 1.35em; margin-top: 0; page-break-before: always; }
h3 { font-size: 1.1em; margin-top: 1.3em; }
p { margin: 0.5em 0; text-align: justify; }
.materia { text-align: center; font-variant: small-caps; margin-top: 3em; }
.autor { text-align: center; font-style: italic; }
blockquote { margin: 0.8em 0; padding: 0.3em 0.7em; border-left: 3px solid #555; background: #f2f2f2; }
blockquote p { text-align: left; }
table { border-collapse: collapse; width: 100%; margin: 0.8em 0; font-size: 0.85em; }
th, td { border: 1px solid #777; padding: 0.25em 0.4em; vertical-align: top; text-align: left; }
th { background: #e6e6e6; }
pre { white-space: pre-wrap; font-size: 0.8em; background: #f2f2f2; padding: 0.5em; border: 1px solid #ccc; }
code { font-family: monospace; font-size: 0.9em; }
img { max-width: 100%; }
ol, ul { margin: 0.4em 0 0.4em 1.2em; padding: 0; }
li { margin: 0.2em 0; }
`;

// ─────────────────────────────────────────── índices

const navOl = capitulos.map((c) => {
  const sub = c.subs.length
    ? `\n<ol>${c.subs.map((s) => `<li><a href="${c.archivo}#${s.sid}">${esc(s.texto)}</a></li>`).join('')}</ol>`
    : '';
  return `<li><a href="${c.archivo}">${esc(c.texto)}</a>${sub}</li>`;
}).join('\n');
const nav = pagina('Índice', `<nav epub:type="toc" id="toc"><h1>Índice</h1>\n<ol>\n${navOl}\n</ol></nav>`);

let orden = 0;
const ncxPoints = capitulos.map((c) => {
  const cn = ++orden;
  const subs = c.subs.map((s) => `<navPoint id="np${++orden}" playOrder="${orden}"><navLabel><text>${esc(s.texto)}</text></navLabel><content src="${c.archivo}#${s.sid}"/></navPoint>`).join('');
  return `<navPoint id="np${cn}" playOrder="${cn}"><navLabel><text>${esc(c.texto)}</text></navLabel><content src="${c.archivo}"/>${subs}</navPoint>`;
}).join('\n');

const uid = 'urn:uuid:' + crypto.createHash('md5').update(input).digest('hex')
  .replace(/^(.{8})(.{4})(.{4})(.{4})(.{12})$/, '$1-$2-$3-$4-$5');
const ncx = `<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="${uid}"/></head>
<docTitle><text>${esc(titulo)}</text></docTitle>
<navMap>
${ncxPoints}
</navMap>
</ncx>
`;

const portada = pagina(titulo, `<h1>${esc(titulo)}</h1>
${cod && MATERIAS[cod] ? `<p class="materia">UTN · Ingeniería en Sistemas · ${esc(MATERIAS[cod])}</p>` : ''}
<p class="autor">${esc(autor)}</p>
${portadaMd ? aXhtml(portadaMd) : ''}`);

const mime = (f) => ({ '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.svg': 'image/svg+xml' })[path.extname(f)];
const fecha = new Date().toISOString().replace(/\.\d+Z$/, 'Z');
const opf = `<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="es">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">${uid}</dc:identifier>
<dc:title>${esc(titulo)}</dc:title>
<dc:creator>${esc(autor)}</dc:creator>
<dc:language>es</dc:language>
<meta property="dcterms:modified">${fecha}</meta>
</metadata>
<manifest>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
<item id="css" href="style.css" media-type="text/css"/>
<item id="portada" href="portada.xhtml" media-type="application/xhtml+xml"/>
${capitulos.map((c) => `<item id="${c.id}" href="${c.archivo}" media-type="application/xhtml+xml"/>`).join('\n')}
${[...imagenes.values()].map((n, i) => `<item id="im${i + 1}" href="images/${n}" media-type="${mime(n)}"/>`).join('\n')}
</manifest>
<spine toc="ncx">
<itemref idref="portada"/>
<itemref idref="nav"/>
${capitulos.map((c) => `<itemref idref="${c.id}"/>`).join('\n')}
</spine>
</package>
`;

// ─────────────────────────────────────────── empaquetar

(async () => {
  const zip = new JSZip();
  zip.file('mimetype', 'application/epub+zip', { compression: 'STORE' });
  zip.file('META-INF/container.xml', `<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
`);
  zip.file('OEBPS/content.opf', opf);
  zip.file('OEBPS/nav.xhtml', nav);
  zip.file('OEBPS/toc.ncx', ncx);
  zip.file('OEBPS/style.css', css);
  zip.file('OEBPS/portada.xhtml', portada);
  for (const c of capitulos) zip.file(`OEBPS/${c.archivo}`, pagina(c.texto, c.html));
  for (const [abs, n] of imagenes) zip.file(`OEBPS/images/${n}`, fs.readFileSync(abs));
  const buf = await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE', mimeType: 'application/epub+zip' });
  fs.writeFileSync(output, buf);
  console.log(`EPUB  → ${path.relative(process.cwd(), output)}  (${capitulos.length} capítulos, ${imagenes.size} imágenes, ${Math.round(buf.length / 1024)} KB)`);
})();
