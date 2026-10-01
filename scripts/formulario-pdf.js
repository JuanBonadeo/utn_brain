#!/usr/bin/env node
/**
 * formulario-pdf.js — hoja de fórmulas en HTML (con LaTeX) -> PDF A4
 *
 * Para formularios de cajas tipo "hoja de fórmulas", donde el layout lo define
 * el propio HTML (grilla, cajas) y no conviene pasar por markdown.
 *
 * La matemática va con delimitadores \( ... \) (en línea) y \[ ... \] (bloque).
 * Se renderiza con KaTeX del lado del servidor y se imprime con el Chrome de la
 * Mac vía puppeteer-core, igual que md-to-pdf.js.
 *
 * Uso:
 *   node scripts/formulario-pdf.js <fuente.html> [salida.pdf] [--landscape]
 */

const fs = require('fs');
const path = require('path');
const katex = require('katex');

const argv = process.argv.slice(2);
const flags = argv.filter((a) => a.startsWith('--'));
const positional = argv.filter((a) => !a.startsWith('--'));
if (positional.length === 0) {
  console.error('Uso: node scripts/formulario-pdf.js <fuente.html> [salida.pdf] [--landscape]');
  process.exit(1);
}

const input = path.resolve(positional[0]);
const outputPdf = positional[1] ? path.resolve(positional[1]) : input.replace(/\.html$/i, '.pdf');
const ROOT = path.resolve(__dirname, '..');
const KATEX_CSS = path.join(ROOT, 'node_modules', 'katex', 'dist', 'katex.min.css');
const CHROME =
  process.env.CHROME_PATH ||
  (process.platform === 'win32'
    ? 'C:/Program Files/Google/Chrome/Application/chrome.exe'
    : '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome');
const { pathToFileURL } = require('url');

const render = (tex, displayMode) =>
  katex.renderToString(tex, { displayMode, throwOnError: true, strict: 'ignore' });

let html = fs.readFileSync(input, 'utf8');
html = html.replace(/\\\[([\s\S]+?)\\\]/g, (_, t) => render(t.trim(), true));
html = html.replace(/\\\(([\s\S]+?)\\\)/g, (_, t) => render(t.trim(), false));

const katexCss = fs
  .readFileSync(KATEX_CSS, 'utf8')
  .replace(/url\(fonts\//g, `url(${pathToFileURL(path.join(path.dirname(KATEX_CSS), 'fonts')).href}/`);
html = html.replace('</head>', `<style>${katexCss}</style></head>`);

const tmpHtml = path.join(require('os').tmpdir(), `formulario-${process.pid}.html`);
fs.writeFileSync(tmpHtml, html);

(async () => {
  const puppeteer = require('puppeteer-core');
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: true, args: ['--no-sandbox'] });
  try {
    const page = await browser.newPage();
    await page.goto(pathToFileURL(tmpHtml).href, { waitUntil: 'networkidle0' });
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({
      path: outputPdf,
      format: 'A4',
      landscape: flags.includes('--landscape'),
      printBackground: true,
      preferCSSPageSize: true,
    });
    console.log(`PDF → ${path.relative(process.cwd(), outputPdf)}`);
  } finally {
    await browser.close();
    fs.unlinkSync(tmpHtml);
  }
})();
