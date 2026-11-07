#!/usr/bin/env node
/**
 * html-to-pdf.js — imprime a PDF un HTML escrito a mano (guías visuales, carillas) con Chrome headless.
 * Respeta el @page del HTML (tamaño y márgenes) e imprime los fondos de color.
 *
 * Uso: node scripts/html-to-pdf.js <entrada.html> [salida.pdf]
 */
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');
const puppeteer = require('puppeteer-core');

const CHROME = process.env.CHROME_PATH || [
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
].find((p) => fs.existsSync(p));

const [entrada, salida] = process.argv.slice(2);
if (!entrada) {
  console.error('Uso: node scripts/html-to-pdf.js <entrada.html> [salida.pdf]');
  process.exit(1);
}
const html = path.resolve(entrada);
const pdf = path.resolve(salida || html.replace(/\.html?$/i, '.pdf'));

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME });
  const page = await browser.newPage();
  await page.goto(pathToFileURL(html).href, { waitUntil: 'networkidle0' });
  await page.pdf({ path: pdf, printBackground: true, preferCSSPageSize: true });
  await browser.close();
  console.log(pdf);
})();
