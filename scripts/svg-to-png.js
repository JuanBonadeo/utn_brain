#!/usr/bin/env node
/**
 * svg-to-png.js — Rasteriza un SVG standalone (viewBox propio) a PNG, a una
 * escala fija, usando Chrome headless (puppeteer-core). Pensado para las
 * figuras de figs/ que se embeben en los .docx (build-docx.js no soporta SVG).
 *
 * Uso: node scripts/svg-to-png.js <entrada.svg> [salida.png] [escala]
 */
const fs = require('fs');
const path = require('path');

const [, , inPath, outArg, scaleArg] = process.argv;
if (!inPath) {
  console.error('Uso: node scripts/svg-to-png.js <entrada.svg> [salida.png] [escala]');
  process.exit(1);
}
const outPath = outArg ? path.resolve(outArg) : inPath.replace(/\.svg$/i, '.png');
const scale = scaleArg ? parseFloat(scaleArg) : 2;

function detectChrome() {
  if (process.env.CHROME_PATH && fs.existsSync(process.env.CHROME_PATH)) return process.env.CHROME_PATH;
  const candidatos = {
    darwin: ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'],
    win32: [
      String.raw`C:\Program Files\Google\Chrome\Application\chrome.exe`,
      String.raw`C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`,
      path.join(process.env.LOCALAPPDATA || '', String.raw`Google\Chrome\Application\chrome.exe`),
      String.raw`C:\Program Files\Microsoft\Edge\Application\msedge.exe`,
    ],
    linux: ['/usr/bin/google-chrome', '/usr/bin/chromium-browser', '/usr/bin/chromium'],
  }[process.platform] || [];
  return candidatos.find((p) => p && fs.existsSync(p)) || null;
}

(async () => {
  const svg = fs.readFileSync(path.resolve(inPath), 'utf8');
  const m = svg.match(/viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"/);
  if (!m) { console.error('No encontré viewBox="0 0 W H" en el SVG.'); process.exit(1); }
  const w = Math.round(parseFloat(m[1]));
  const h = Math.round(parseFloat(m[2]));

  const CHROME = detectChrome();
  if (!CHROME) { console.error('No encontré Chrome/Edge.'); process.exit(1); }
  const puppeteer = require('puppeteer-core');
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: true, args: ['--no-sandbox'] });
  try {
    const page = await browser.newPage();
    await page.setViewport({ width: w, height: h, deviceScaleFactor: scale });
    await page.setContent(`<!doctype html><html><head><style>
      html,body{margin:0;padding:0;background:#fff;}
      svg{display:block;width:${w}px;height:${h}px;}
    </style></head><body>${svg}</body></html>`);
    await page.waitForSelector('svg');
    await page.screenshot({ path: outPath, omitBackground: false });
    console.log(`Escrito: ${outPath} (${w * scale}x${h * scale}px)`);
  } finally {
    await browser.close();
  }
})();
