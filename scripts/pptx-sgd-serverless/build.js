// Presentación de SGD: Serverless (14 láminas, 4 expositores, 15 min).
// Uso (desde la raíz del repo):  node scripts/pptx-sgd-serverless/build.js
// Las notas del orador salen de materias/SGD/entregables/serverless/guion-presentacion.md
// (un bloque "## Lámina N" por diapositiva).
const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");

const RAIZ = path.resolve(__dirname, "..", "..");
const DIR = path.join(RAIZ, "materias", "SGD", "entregables", "serverless");
const OUT = process.argv[2] || path.join(DIR, "presentacion-serverless.pptx");
const GUION = path.join(DIR, "guion-presentacion.md");

// ---------- tema ----------
const THEME = {
  name: "SGD Serverless",
  headFontFace: "Arial",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "0B1220", lt1: "FFFFFF", dk2: "334155", lt2: "F1F5F9",
    accent1: "F59E0B", // ámbar: lo que se dispara / lo que se paga
    accent2: "0F766E", // teal oscuro: texto de acento sobre claro
    accent3: "64748B", // gris pizarra: texto secundario
    accent4: "B91C1C", // rojo: "no encaja"
    accent5: "15803D", // verde: "encaja"
    accent6: "CBD5E1",
    hlink: "0F766E", folHlink: "64748B",
  },
};
const HEX = THEME.colors;
const INK = HEX.dk1, PAPER_DARK = "0B1220";

// ---------- notas desde el guion ----------
function leerNotas() {
  const md = fs.readFileSync(GUION, "utf8");
  const notas = {};
  for (const b of md.split(/^## /m).slice(1)) {
    const m = b.match(/^Lámina (\d+)[^\n]*\n([\s\S]*)$/);
    if (!m) continue;
    const texto = m[2]
      .replace(/^\*(.+)\*$/gm, "[$1]")
      .replace(/\*\*/g, "")
      .replace(/([^\n])\n(?!\n)/g, "$1 ")
      .replace(/\n{3,}/g, "\n\n")
      .trim();
    notas[+m[1]] = texto;
  }
  return notas;
}
const NOTAS = leerNotas();

// ---------- presentación ----------
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
pres.author = "Bonadeo, Juan Cruz y grupo";
pres.title = "Serverless — SGD";
pres.subject = "Soporte a la Gestión de Datos con P. Visual";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
// Colores en hex (no scheme) para que el script corra en cualquier máquina sin dependencias extra.
const C = { text1: HEX.dk1, text2: HEX.dk2, background1: HEX.lt1, background2: HEX.lt2,
  accent1: HEX.accent1, accent2: HEX.accent2, accent3: HEX.accent3, accent4: HEX.accent4, accent5: HEX.accent5, accent6: HEX.accent6 };
const W = 13.333, ML = 0.6, CW = W - 2 * ML;

pres.defineSlideMaster({
  title: "PORTADA",
  background: { color: PAPER_DARK },
  objects: [],
});
pres.defineSlideMaster({
  title: "CONTENIDO",
  background: { color: "FFFFFF" },
  margin: [0.5, 0.6, 0.6, 0.6],
  objects: [
    { placeholder: { options: { name: "kicker", type: "body", x: ML, y: 0.35, w: 8, h: 0.35,
        fontSize: 12, bold: true, color: C.accent2, charSpacing: 2, margin: 0, valign: "middle" },
      text: "" } },
    { placeholder: { options: { name: "title", type: "title", x: ML, y: 0.7, w: CW, h: 0.8,
        fontSize: 30, bold: true, color: C.text1, fontFace: THEME.headFontFace, margin: 0, valign: "middle", align: "left" },
      text: "" } },
    { text: { text: "SGD · Serverless", options: { x: ML, y: 7.0, w: 4, h: 0.3, fontSize: 10,
        color: C.accent3, margin: 0 } } },
  ],
  slideNumber: { x: W - ML - 0.6, y: 7.0, w: 0.6, h: 0.3, fontSize: 10, color: C.accent3, align: "right" },
});

// ---------- helpers ----------
let n = 0;
function nueva(master, seccion) {
  const s = pres.addSlide({ masterName: master, sectionTitle: seccion });
  n += 1;
  if (NOTAS[n]) s.addNotes(NOTAS[n]);
  return s;
}
function encabezado(s, kicker, titulo) {
  s.addText(kicker, { placeholder: "kicker" });
  s.addText(titulo, { placeholder: "title" });
}
function tarjeta(s, x, y, w, h, opts = {}) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h, rectRadius: 0.1,
    fill: { color: opts.fill || C.background2, transparency: opts.transparency || 0 },
    line: opts.line ? { color: opts.line, width: 1 } : { type: "none" },
    objectName: opts.name || "tarjeta",
  });
}
function insignia(s, x, y, texto, d = 0.5, fill = C.accent1, color = C.text1) {
  s.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: fill }, line: { type: "none" }, objectName: "insignia" });
  s.addText(texto, { x, y, w: d, h: d, align: "center", valign: "middle", fontSize: d > 0.45 ? 16 : 12,
    bold: true, color, margin: 0, isTextBox: true, fontFace: THEME.headFontFace });
}
function texto(s, t, o) { s.addText(t, Object.assign({ isTextBox: true, margin: 0, color: C.text1, fontSize: 15, valign: "top" }, o)); }
function flecha(s, x1, y1, x2, y2, color = C.accent3) {
  const flipH = x2 < x1, flipV = y2 < y1;
  s.addShape(pres.shapes.LINE, { x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1) || 0.001,
    h: Math.abs(y2 - y1) || 0.001, flipH, flipV, line: { color, width: 2, endArrowType: "triangle" } });
}
function linea(s, x1, y1, x2, y2, color = C.accent3) {
  s.addShape(pres.shapes.LINE, { x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1) || 0.001,
    h: Math.abs(y2 - y1) || 0.001, line: { color, width: 2 } });
}
function fuente(s, t) { texto(s, t, { x: ML, y: 6.62, w: CW, h: 0.3, fontSize: 10, color: C.accent3, italic: true }); }

const S1 = "Expositor 1 — Qué es";
const S2 = "Expositor 2 — Cómo funciona";
const S3 = "Expositor 3 — Economía y datos";
const S4 = "Expositor 4 — Límites y futuro";

// ===== 1. Portada =====
pres.addSection({ title: S1 });
{
  const s = nueva("PORTADA", S1);
  texto(s, "SOPORTE A LA GESTIÓN DE DATOS CON P. VISUAL", { x: ML, y: 1.2, w: 7.5, h: 0.4, fontSize: 13, bold: true, color: C.accent1, charSpacing: 2 });
  texto(s, "Serverless", { x: ML, y: 1.75, w: 7.8, h: 1.4, fontSize: 66, bold: true, color: C.background1, fontFace: THEME.headFontFace, valign: "middle" });
  texto(s, "Qué es, cómo funciona por dentro y cuándo no conviene", { x: ML, y: 3.2, w: 7.4, h: 1.0, fontSize: 24, color: C.accent6 });
  texto(s, [
    { text: "Integrantes: ", options: { bold: true, color: C.background1 } },
    { text: "Bonadeo, Juan Cruz · [Integrante 2] · [Integrante 3] · [Integrante 4]", options: { color: C.accent6 } },
  ], { x: ML, y: 5.55, w: 8.5, h: 0.4, fontSize: 14 });
  texto(s, "UTN — Facultad Regional Rosario · Ingeniería en Sistemas de Información · 2026",
    { x: ML, y: 6.0, w: 8.5, h: 0.4, fontSize: 13, color: C.accent3 });
  // motivo: grilla de entornos; sólo algunos encendidos (escala según demanda)
  const on = new Set([2, 7, 8, 13, 14, 15, 19]);
  for (let r = 0; r < 5; r++) for (let c = 0; c < 4; c++) {
    const i = r * 4 + c;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 9.0 + c * 0.9, y: 1.2 + r * 0.9, w: 0.7, h: 0.7, rectRadius: 0.08,
      fill: { color: on.has(i) ? C.accent1 : C.text2, transparency: on.has(i) ? 0 : 55 }, line: { type: "none" }, objectName: "entorno" });
  }
  texto(s, "Entornos que existen sólo mientras hay demanda", { x: 9.0, y: 5.75, w: 3.6, h: 0.5, fontSize: 11, color: C.accent3, italic: true });
}

// ===== 2. Gancho =====
{
  const s = nueva("CONTENIDO", S1);
  encabezado(s, "01 · QUÉ ES", "Serverless no significa «sin servidores»");
  tarjeta(s, ML, 1.75, CW, 1.35);
  insignia(s, ML + 0.35, 2.17, "!", 0.5);
  texto(s, [
    { text: "Los servidores existen: no son tu problema.", options: { bold: true, fontSize: 22, breakLine: true } },
    { text: "Como wireless: los cables siguen estando, pero no los tirás vos.", options: { fontSize: 16, color: C.text2 } },
  ], { x: ML + 1.15, y: 1.95, w: CW - 1.5, h: 1.0, valign: "middle" });
  const stats = [
    ["15", "billones (10¹²) de invocaciones por mes en AWS Lambda"],
    ["65 %", "de los clientes de AWS usan Lambda"],
    ["70 %", "de los clientes de Google Cloud usan Cloud Run"],
  ];
  const cw = (CW - 2 * 0.4) / 3;
  stats.forEach(([num, lbl], i) => {
    const x = ML + i * (cw + 0.4);
    tarjeta(s, x, 3.45, cw, 2.9, { fill: C.background1, line: HEX.accent6 });
    texto(s, num, { x: x + 0.35, y: 3.8, w: cw - 0.7, h: 1.2, fontSize: 48, bold: true, color: C.accent2, fontFace: THEME.headFontFace, valign: "middle" });
    texto(s, lbl, { x: x + 0.35, y: 5.1, w: cw - 0.7, h: 0.9, fontSize: 16, color: C.text2 });
  });
  fuente(s, "Fuentes: AWS (2026); Datadog, State of Serverless (2025).");
}

// ===== 3. Definición =====
{
  const s = nueva("CONTENIDO", S1);
  encabezado(s, "01 · QUÉ ES", "Tres propiedades: si falta una, no es serverless");
  texto(s, [
    { text: "«Construir y correr aplicaciones que no requieren gestión de servidores. Se ejecutan, escalan y facturan en respuesta a la demanda exacta del momento.»", options: { italic: true, breakLine: true } },
    { text: "— CNCF, Serverless Whitepaper", options: { fontSize: 12, color: C.accent3 } },
  ], { x: ML, y: 1.7, w: CW, h: 1.0, fontSize: 17, color: C.text2 });
  const props = [
    ["Sin gestión de infraestructura", "No provisionás, no parcheás el sistema operativo, no dimensionás capacidad."],
    ["Escala hasta cero", "De 0 a N instancias según la demanda, y de vuelta a 0 cuando no hay tráfico."],
    ["Pago por uso real", "Se cobra por ejecución, no por tener un servidor encendido."],
  ];
  const cw = (CW - 2 * 0.4) / 3;
  props.forEach(([t, d], i) => {
    const x = ML + i * (cw + 0.4);
    tarjeta(s, x, 3.0, cw, 2.75);
    insignia(s, x + 0.35, 3.3, String(i + 1), 0.6);
    texto(s, t, { x: x + 0.35, y: 4.05, w: cw - 0.7, h: 0.75, fontSize: 19, bold: true });
    texto(s, d, { x: x + 0.35, y: 4.85, w: cw - 0.7, h: 0.85, fontSize: 15, color: C.text2 });
  });
  texto(s, [
    { text: "Contraejemplo: ", options: { bold: true } },
    { text: "un Kubernetes administrado no cumple la 3: el pod cuesta aunque nadie lo llame.", options: {} },
  ], { x: ML, y: 6.0, w: CW, h: 0.45, fontSize: 15, color: C.text2 });
}

// ===== 4. Escalera =====
{
  const s = nueva("CONTENIDO", S1);
  encabezado(s, "01 · QUÉ ES", "Cada escalón te saca una capa de encima");
  const esc = [
    ["Bare metal", "un servidor", "compra (CAPEX)"],
    ["IaaS · EC2", "una máquina virtual", "hora"],
    ["PaaS · Heroku", "una aplicación", "hora"],
    ["Contenedores · K8s", "un contenedor", "hora"],
    ["FaaS · Lambda", "una función", "milisegundo"],
  ];
  const bw = 2.2, gap = (CW - 5 * bw) / 4, base = 5.3;
  esc.forEach(([t, dep, pago], i) => {
    const h = 1.5 + i * 0.38, x = ML + i * (bw + gap), y = base - h, ult = i === 4;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: bw, h, rectRadius: 0.08,
      fill: { color: ult ? C.accent1 : C.background2 }, line: { type: "none" }, objectName: "escalon" });
    texto(s, [
      { text: t, options: { bold: true, fontSize: 15, breakLine: true } },
      { text: "Desplegás " + dep, options: { fontSize: 12, color: C.text2, breakLine: true } },
      { text: "Pagás por " + pago, options: { fontSize: 12, bold: ult, color: ult ? C.text1 : C.text2 } },
    ], { x: x + 0.15, y: y + 0.15, w: bw - 0.3, h: 1.2, paraSpaceAfter: 3 });
  });
  const hw = (CW - 0.4) / 2;
  [["FaaS — tu código", "Funciones que se disparan por eventos: Lambda, Cloud Functions, Workers."],
   ["BaaS — servicios que consumís", "Base, autenticación, almacenamiento por API: Firebase, Auth0, S3."]].forEach(([t, d], i) => {
    const x = ML + i * (hw + 0.4);
    tarjeta(s, x, 5.55, hw, 0.95, { fill: C.background1, line: HEX.accent6 });
    texto(s, [{ text: t + "  ", options: { bold: true } }, { text: d, options: { color: C.text2 } }],
      { x: x + 0.25, y: 5.6, w: hw - 0.5, h: 0.85, fontSize: 14, valign: "middle" });
  });
}

// ===== 5. Ciclo de vida =====
pres.addSection({ title: S2 });
{
  const s = nueva("CONTENIDO", S2);
  encabezado(s, "02 · CÓMO FUNCIONA", "Una función no corre: es invocada");
  const fases = [
    ["EVENTO", "Pedido HTTP, archivo subido, mensaje en cola, horario (cron)", C.background2],
    ["INIT", "Crea la microVM, baja el código, arranca el runtime, corre tu init (imports, conexión a la base)", C.accent1],
    ["INVOKE", "Ejecuta el handler con los datos del evento", C.background2],
    ["FREEZE", "Congela el entorno. Sin eventos en 5–15 min: se apaga", C.background2],
  ];
  const bw = 2.6, gap = (CW - 4 * bw) / 3, y = 1.75, h = 1.95;
  fases.forEach(([t, d, f], i) => {
    const x = ML + i * (bw + gap);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: bw, h, rectRadius: 0.1, fill: { color: f }, line: { type: "none" }, objectName: "fase" });
    texto(s, [{ text: t, options: { bold: true, fontSize: 16, breakLine: true, fontFace: THEME.headFontFace } },
      { text: d, options: { fontSize: 13, color: C.text2 } }], { x: x + 0.18, y: y + 0.18, w: bw - 0.36, h: h - 0.3, paraSpaceAfter: 4 });
    if (i < 3) flecha(s, x + bw + 0.06, y + h / 2, x + bw + gap - 0.06, y + h / 2);
  });
  texto(s, "sólo en cold start", { x: ML + bw + gap, y: y + h + 0.05, w: bw, h: 0.3, fontSize: 11, italic: true, color: C.accent3, align: "center" });
  // vuelta warm: FREEZE -> INVOKE
  const xInv = ML + 2 * (bw + gap) + bw / 2, xFrz = ML + 3 * (bw + gap) + bw / 2, yb = y + h, yl = yb + 0.45;
  linea(s, xFrz, yb, xFrz, yl); linea(s, xFrz, yl, xInv, yl); flecha(s, xInv, yl, xInv, yb + 0.03);
  texto(s, "warm: reusa el entorno y se saltea INIT", { x: xInv + 0.1, y: yl + 0.05, w: xFrz - xInv - 0.2, h: 0.3, fontSize: 11, italic: true, color: C.accent3, align: "center" });

  const hw = (CW - 0.4) / 2, yc = 4.65, hc = 1.85;
  tarjeta(s, ML, yc, hw, hc);
  texto(s, [{ text: "Stateless por contrato", options: { bold: true, fontSize: 17, breakLine: true } },
    { text: "Dos pedidos no tienen garantía de caer en el mismo entorno: el estado de negocio va a la base, nunca a la memoria de la función.", options: { fontSize: 14, color: C.text2 } }],
    { x: ML + 0.3, y: yc + 0.22, w: hw - 0.6, h: hc - 0.4, paraSpaceAfter: 6 });
  tarjeta(s, ML + hw + 0.4, yc, hw, hc);
  texto(s, [{ text: "Lambda: un pedido por entorno a la vez", options: { bold: true, fontSize: 17, breakLine: true } },
    { text: "concurrencia = pedidos/s × duración", options: { fontFace: "Courier New", fontSize: 14, breakLine: true } },
    { text: "100/s × 0,2 s = 20 entornos", options: { fontFace: "Courier New", fontSize: 14, color: C.text2, breakLine: true } },
    { text: "100/s × 2 s  = 200 entornos", options: { fontFace: "Courier New", fontSize: 14, color: C.text2 } }],
    { x: ML + hw + 0.7, y: yc + 0.22, w: hw - 0.6, h: hc - 0.4, paraSpaceAfter: 4 });
}

// ===== 6. Cold start =====
{
  const s = nueva("CONTENIDO", S2);
  encabezado(s, "02 · CÓMO FUNCIONA", "Cold start: el precio de escalar a cero");
  const x0 = ML + 2.5, aw = 4.6, maxMs = 500, sc = aw / maxMs, y0 = 1.95, rh = 0.72;
  const filas = [
    ["Go / Rust", 10, 100, "< 100 ms"],
    ["Java + SnapStart", 90, 140, "90–140 ms"],
    ["Python", 200, 400, "200–400 ms"],
    ["Java sin SnapStart", 300, 500, "segundos", true],
    ["Extra si está en VPC", 200, 500, "+200–500 ms"],
  ];
  // grilla
  for (let t = 0; t <= maxMs; t += 100) {
    s.addShape(pres.shapes.LINE, { x: x0 + t * sc, y: y0 - 0.1, w: 0.001, h: filas.length * rh, line: { color: HEX.accent6, width: 0.75 } });
    texto(s, t + "", { x: x0 + t * sc - 0.3, y: y0 + filas.length * rh - 0.05, w: 0.6, h: 0.3, fontSize: 11, color: C.accent3, align: "center" });
  }
  texto(s, "milisegundos", { x: x0, y: y0 + filas.length * rh + 0.25, w: aw, h: 0.3, fontSize: 11, color: C.accent3, align: "center" });
  filas.forEach(([lbl, a, b, val, sale], i) => {
    const y = y0 + i * rh;
    texto(s, lbl, { x: ML, y, w: 2.35, h: 0.45, fontSize: 14, align: "right", valign: "middle", color: i === 4 ? C.accent3 : C.text1, italic: i === 4 });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x0 + a * sc, y: y + 0.07, w: (b - a) * sc, h: 0.32, rectRadius: 0.05,
      fill: { color: i === 4 ? C.accent3 : C.accent1, transparency: i === 4 ? 40 : 0 }, line: { type: "none" }, objectName: "rango" });
    if (sale) flecha(s, x0 + b * sc, y + 0.23, x0 + aw + 0.35, y + 0.23, C.accent1);
    texto(s, val, { x: sale ? x0 + aw + 0.42 : x0 + b * sc + 0.1, y, w: 1.3, h: 0.45, fontSize: 13, bold: true, valign: "middle", color: C.text2 });
  });
  fuente(s, "Órdenes de magnitud reportados en 2026 (fuentes secundarias), no mediciones propias.");
  // mitigaciones
  const xm = 8.85, wm = W - ML - xm;
  tarjeta(s, xm, 1.75, wm, 4.65);
  texto(s, "Cómo se mitiga", { x: xm + 0.3, y: 1.95, w: wm - 0.6, h: 0.4, fontSize: 17, bold: true });
  texto(s, [
    { text: "Provisioned Concurrency: ", options: { bold: true } }, { text: "entornos precalentados, pero se pagan por hora.", options: { color: C.text2, breakLine: true } },
    { text: "SnapStart: ", options: { bold: true } }, { text: "restaura una foto de un entorno ya inicializado.", options: { color: C.text2, breakLine: true } },
    { text: "Runtime compilado y paquete liviano: ", options: { bold: true } }, { text: "menos que bajar y arrancar.", options: { color: C.text2, breakLine: true } },
    { text: "Isolates (Cloudflare): ", options: { bold: true } }, { text: "evitan el problema de raíz.", options: { color: C.text2 } },
  ], { x: xm + 0.3, y: 2.5, w: wm - 0.6, h: 3.7, fontSize: 14, paraSpaceAfter: 12 });
}

// ===== 7. Aislamiento =====
{
  const s = nueva("CONTENIDO", S2);
  encabezado(s, "02 · CÓMO FUNCIONA", "Por dentro: aislar el código de miles de clientes");
  const hw = (CW - 0.5) / 2;
  // Firecracker
  {
    const x = ML;
    texto(s, [{ text: "AWS Lambda · ", options: { bold: true } }, { text: "Firecracker microVM", options: { color: C.accent2, bold: true } }],
      { x, y: 1.7, w: hw, h: 0.4, fontSize: 18 });
    for (let i = 0; i < 3; i++) {
      const bx = x + i * 1.95, by = 2.25;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: bx, y: by, w: 1.75, h: 1.55, rectRadius: 0.08, fill: { color: C.background2 }, line: { color: HEX.accent6, width: 1 }, objectName: "microvm" });
      texto(s, "microVM", { x: bx, y: by + 0.08, w: 1.75, h: 0.3, fontSize: 11, color: C.accent3, align: "center" });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: bx + 0.25, y: by + 0.45, w: 1.25, h: 0.5, rectRadius: 0.06, fill: { color: C.accent1 }, line: { type: "none" }, objectName: "funcion" });
      texto(s, "función", { x: bx + 0.25, y: by + 0.45, w: 1.25, h: 0.5, fontSize: 12, bold: true, align: "center", valign: "middle" });
      texto(s, "kernel invitado", { x: bx, y: by + 1.08, w: 1.75, h: 0.3, fontSize: 11, color: C.text2, align: "center" });
    }
    [["< 125 ms", "en arrancar una microVM"], ["~5 MiB", "de memoria extra por microVM"]].forEach(([a, b], i) => {
      texto(s, a, { x: x + i * 2.9, y: 4.05, w: 2.8, h: 0.6, fontSize: 32, bold: true, color: C.accent2, fontFace: THEME.headFontFace });
      texto(s, b, { x: x + i * 2.9, y: 4.65, w: 2.8, h: 0.35, fontSize: 13, color: C.text2 });
    });
    texto(s, "Aislamiento por hardware (KVM) · corre cualquier binario", { x, y: 5.25, w: hw, h: 0.4, fontSize: 14 });
  }
  // V8
  {
    const x = ML + hw + 0.5;
    texto(s, [{ text: "Cloudflare Workers · ", options: { bold: true } }, { text: "isolates de V8", options: { color: C.accent2, bold: true } }],
      { x, y: 1.7, w: hw, h: 0.4, fontSize: 18 });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 2.25, w: hw, h: 1.55, rectRadius: 0.08, fill: { color: C.background2 }, line: { color: HEX.accent6, width: 1 }, objectName: "procesoV8" });
    texto(s, "un solo proceso del motor V8", { x, y: 2.33, w: hw, h: 0.3, fontSize: 11, color: C.accent3, align: "center" });
    const k = 7, fw = 0.62, fg = (hw - 0.5 - k * fw) / (k - 1);
    for (let i = 0; i < k; i++) {
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 0.25 + i * (fw + fg), y: 2.75, w: fw, h: 0.5, rectRadius: 0.06, fill: { color: C.accent1 }, line: { type: "none" }, objectName: "isolate" });
      texto(s, "f" + (i + 1), { x: x + 0.25 + i * (fw + fg), y: 2.75, w: fw, h: 0.5, fontSize: 12, bold: true, align: "center", valign: "middle" });
    }
    texto(s, "miles de isolates por proceso", { x, y: 3.33, w: hw, h: 0.3, fontSize: 11, color: C.text2, align: "center" });
    [["~100×", "más rápido que un proceso Node"], ["~10×", "menos memoria al arrancar"]].forEach(([a, b], i) => {
      texto(s, a, { x: x + i * 2.9, y: 4.05, w: 2.8, h: 0.6, fontSize: 32, bold: true, color: C.accent2, fontFace: THEME.headFontFace });
      texto(s, b, { x: x + i * 2.9, y: 4.65, w: 2.8, h: 0.35, fontSize: 13, color: C.text2 });
    });
    texto(s, "Aislamiento por el motor (software) · sólo JS, TS o WASM", { x, y: 5.25, w: hw, h: 0.4, fontSize: 14 });
  }
  tarjeta(s, ML, 5.85, CW, 0.65);
  texto(s, "Firecracker: monitor de máquinas virtuales en Rust, open source. Es la base de Lambda y de Fargate.",
    { x: ML + 0.3, y: 5.85, w: CW - 0.6, h: 0.65, fontSize: 14, valign: "middle", color: C.text2 });
}

// ===== 8. Facturación =====
pres.addSection({ title: S3 });
{
  const s = nueva("CONTENIDO", S3);
  encabezado(s, "03 · ECONOMÍA Y DATOS", "Se paga por milisegundo de ejecución");
  const lw = 6.0;
  tarjeta(s, ML, 1.75, lw, 1.3, { fill: PAPER_DARK });
  texto(s, [
    { text: "costo = pedidos × USD 0,20 / millón", options: { breakLine: true } },
    { text: "      + GB-s × USD 0,0000167", options: {} },
  ], { x: ML + 0.3, y: 1.75, w: lw - 0.6, h: 1.3, fontFace: "Courier New", fontSize: 16, color: C.background1, valign: "middle", bold: true });
  texto(s, [
    { text: "GB-segundo = memoria configurada × tiempo de ejecución", options: { bullet: true, breakLine: true } },
    { text: "Capa gratuita: 1 M de pedidos + 400.000 GB-s por mes", options: { bullet: true, breakLine: true } },
    { text: "Memoria de 128 MB a 10 GB; la CPU crece en proporción", options: { bullet: true, breakLine: true } },
    { text: "Sin tráfico, el costo de cómputo es cero", options: { bullet: true, bold: true } },
  ], { x: ML, y: 3.3, w: lw, h: 2.6, fontSize: 15, paraSpaceAfter: 10, color: C.text2 });
  // ejemplo
  const xr = ML + lw + 0.5, wr = W - ML - xr;
  texto(s, "Ejemplo: API con 5 M de pedidos/mes, 200 ms y 512 MB", { x: xr, y: 1.75, w: wr, h: 0.4, fontSize: 16, bold: true });
  s.addChart(pres.charts.BAR, [{ name: "USD por mes", labels: ["EC2 t3.small 24×7", "Lambda"], values: [15, 2.47] }], {
    x: xr, y: 2.25, w: wr, h: 3.3, barDir: "bar", chartColors: [HEX.accent3, HEX.accent1],
    showValue: true, dataLabelPosition: "outEnd", dataLabelFormatCode: '"USD "0.00', dataLabelFontSize: 14, dataLabelFontBold: true,
    dataLabelColor: HEX.dk1, dataLabelFontFace: "+mn-lt",
    catAxisLabelColor: HEX.dk2, catAxisLabelFontSize: 14, catAxisLabelFontFace: "+mn-lt", catAxisLineShow: false,
    valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" }, valAxisMaxVal: 18, valAxisMinVal: 0,
    showLegend: false, barGapWidthPct: 60, varyColors: true,
  });
  texto(s, "≈ 6 veces más barato", { x: xr, y: 5.6, w: wr, h: 0.45, fontSize: 20, bold: true, color: C.accent2 });
  fuente(s, "Precios oficiales de AWS Lambda (US East, x86). Cálculo propio.");
}

// ===== 9. Punto de cruce =====
{
  const s = nueva("CONTENIDO", S3);
  encabezado(s, "03 · ECONOMÍA Y DATOS", "Arriba de un tercio de uso, conviene un servidor");
  const us = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
  const lam = us.map(u => +(0.106 * u / 100).toFixed(4));
  const ec2 = us.map(() => 0.036);
  const cw = 7.6;
  s.addChart(pres.charts.LINE, [
    { name: "Lambda", labels: us.map(u => u + " %"), values: lam },
    { name: "Servidor encendido 24/7 (EC2)", labels: us.map(u => u + " %"), values: ec2 },
  ], {
    x: ML, y: 1.65, w: cw, h: 4.85, chartColors: [HEX.accent1, HEX.accent2], lineSize: 3, lineDataSymbol: "none",
    showLegend: true, legendPos: "t", legendFontSize: 13, legendFontFace: "+mn-lt", legendColor: HEX.dk2,
    showTitle: false,
    catAxisTitle: "utilización", showCatAxisTitle: true, catAxisTitleFontSize: 12, catAxisTitleColor: HEX.accent3,
    valAxisTitle: "USD por vCPU-hora", showValAxisTitle: true, valAxisTitleFontSize: 12, valAxisTitleColor: HEX.accent3,
    catAxisLabelColor: HEX.accent3, valAxisLabelColor: HEX.accent3, catAxisLabelFontSize: 12, valAxisLabelFontSize: 12,
    catAxisLabelFontFace: "+mn-lt", valAxisLabelFontFace: "+mn-lt", catAxisTitleFontFace: "+mn-lt", valAxisTitleFontFace: "+mn-lt",
    valAxisLabelFormatCode: "0.00", valAxisMinVal: 0, valAxisMaxVal: 0.12, valAxisMajorUnit: 0.02,
    valGridLine: { color: HEX.lt2, size: 1 }, catGridLine: { style: "none" },
  });
  const xr = ML + cw + 0.45, wr = W - ML - xr;
  texto(s, "≈ 34 %", { x: xr, y: 1.75, w: wr, h: 0.9, fontSize: 48, bold: true, color: C.accent2, fontFace: THEME.headFontFace });
  texto(s, "punto donde las dos líneas se cruzan", { x: xr, y: 2.65, w: wr, h: 0.4, fontSize: 14, color: C.text2 });
  texto(s, [
    { text: "Lambda: cero en reposo, crece lineal con el uso", options: { bullet: true, breakLine: true } },
    { text: "Servidor: costo fijo aunque esté ocioso", options: { bullet: true, breakLine: true } },
    { text: "El vCPU-hora de Lambda cuesta ~3× el de una instancia", options: { bullet: true, breakLine: true } },
    { text: "Gana en cargas espigadas; pierde en cargas constantes", options: { bullet: true, bold: true } },
  ], { x: xr, y: 3.3, w: wr, h: 3.1, fontSize: 15, paraSpaceAfter: 10, color: C.text2 });
  fuente(s, "Cálculo propio con precios oficiales: Lambda ≈ USD 0,106 / vCPU-h; EC2 c7g.large ≈ USD 0,036 / vCPU-h.");
}

// ===== 10. Bases de datos =====
{
  const s = nueva("CONTENIDO", S3);
  encabezado(s, "03 · ECONOMÍA Y DATOS", "Datos: apagar el cómputo sin perder la base");
  const lw = 5.3;
  texto(s, "Separar cómputo de almacenamiento", { x: ML, y: 1.7, w: lw, h: 0.4, fontSize: 18, bold: true });
  // cómputo (efímero) sobre almacenamiento (persistente)
  for (let i = 0; i < 3; i++) {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: ML + 0.3 + i * 1.6, y: 2.3, w: 1.35, h: 0.75, rectRadius: 0.08,
      fill: { color: i === 1 ? C.accent1 : C.background2 }, line: { color: i === 1 ? HEX.accent1 : HEX.accent6, width: 1, dashType: i === 1 ? "solid" : "dash" }, objectName: "nodo" });
    texto(s, i === 1 ? "cómputo activo" : "apagado", { x: ML + 0.3 + i * 1.6, y: 2.3, w: 1.35, h: 0.75, fontSize: 12, bold: i === 1, align: "center", valign: "middle", color: i === 1 ? C.text1 : C.accent3 });
  }
  flecha(s, ML + 0.3 + 1.6 + 0.675, 3.1, ML + 0.3 + 1.6 + 0.675, 3.55);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: ML + 0.3, y: 3.6, w: 4.55, h: 0.8, rectRadius: 0.08, fill: { color: C.text2 }, line: { type: "none" }, objectName: "storage" });
  texto(s, "almacenamiento persistente", { x: ML + 0.3, y: 3.6, w: 4.55, h: 0.8, fontSize: 15, bold: true, color: C.background1, align: "center", valign: "middle" });
  texto(s, [
    { text: "Neon: ", options: { bold: true } }, { text: "Postgres que escala el cómputo a cero", options: { color: C.text2, breakLine: true } },
    { text: "Aurora Serverless v2: ", options: { bold: true } }, { text: "MySQL / Postgres elástico", options: { color: C.text2, breakLine: true } },
    { text: "DynamoDB on-demand: ", options: { bold: true } }, { text: "NoSQL sin capacidad fija", options: { color: C.text2 } },
  ], { x: ML, y: 4.65, w: lw, h: 1.6, fontSize: 14, paraSpaceAfter: 6 });

  // problema de conexiones
  const xr = ML + lw + 0.6, wr = W - ML - xr;
  tarjeta(s, xr, 1.7, wr, 4.75);
  texto(s, "El choque: conexiones", { x: xr + 0.3, y: 1.9, w: wr - 0.6, h: 0.4, fontSize: 18, bold: true });
  texto(s, "500 funciones a la vez × 1 conexión cada una. Postgres soporta cientos.", { x: xr + 0.3, y: 2.35, w: wr - 0.6, h: 0.7, fontSize: 14, color: C.text2 });
  const fx = xr + 0.4, fy = 3.15, px = xr + 2.6, dbx = xr + wr - 1.5;
  for (let i = 0; i < 5; i++) {
    const y = fy + i * 0.42;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: fx, y, w: 0.85, h: 0.32, rectRadius: 0.05, fill: { color: C.accent1 }, line: { type: "none" }, objectName: "funcion" });
    texto(s, "λ", { x: fx, y, w: 0.85, h: 0.32, fontSize: 13, bold: true, align: "center", valign: "middle" });
    flecha(s, fx + 0.9, y + 0.16, px - 0.05, fy + 0.98);
  }
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: px, y: fy + 0.63, w: 1.35, h: 0.7, rectRadius: 0.08, fill: { color: C.accent2 }, line: { type: "none" }, objectName: "pooler" });
  texto(s, "pooler", { x: px, y: fy + 0.63, w: 1.35, h: 0.7, fontSize: 14, bold: true, color: C.background1, align: "center", valign: "middle" });
  flecha(s, px + 1.4, fy + 0.98, dbx - 0.05, fy + 0.98);
  s.addShape(pres.shapes.CAN, { x: dbx, y: fy + 0.45, w: 1.1, h: 1.05, fill: { color: C.text2 }, line: { type: "none" }, objectName: "base" });
  texto(s, "Postgres", { x: dbx - 0.1, y: fy + 1.55, w: 1.3, h: 0.3, fontSize: 12, align: "center", color: C.text2 });
  texto(s, [
    { text: "Pooler: ", options: { bold: true } }, { text: "RDS Proxy, PgBouncer reutilizan pocas conexiones", options: { color: C.text2, breakLine: true } },
    { text: "API HTTP: ", options: { bold: true } }, { text: "DynamoDB, driver serverless de Neon", options: { color: C.text2 } },
  ], { x: xr + 0.3, y: 5.35, w: wr - 0.6, h: 0.95, fontSize: 14, paraSpaceAfter: 4 });
}

// ===== 11. Cuándo sí / no =====
pres.addSection({ title: S4 });
{
  const s = nueva("CONTENIDO", S4);
  encabezado(s, "04 · LÍMITES Y FUTURO", "Cuándo sí y cuándo no");
  const hw = (CW - 0.4) / 2, y = 1.75, h = 3.75;
  [[C.accent5, "Encaja", "✓", ["Carga espigada o impredecible", "Disparada por eventos y asíncrona", "Sin estado y paralelizable", "Ej.: miniaturas al subir una foto, sensores IoT, tareas programadas"],
    "iRobot (Roomba): más de 20 M de eventos IoT por día, −30 % de costo cloud"],
   [C.accent4, "No encaja", "✕", ["Carga constante: arriba de ~1/3 de uso pierde", "Latencia crítica: el cold start no se tolera", "Estado o conexiones persistentes", "Cadenas largas de funciones acopladas"],
    "Prime Video: −90 % de costo saliendo de serverless (lámina siguiente)"]].forEach(([col, t, ico, items, caso], i) => {
    const x = ML + i * (hw + 0.4);
    tarjeta(s, x, y, hw, h, { fill: col, transparency: 90 });
    insignia(s, x + 0.3, y + 0.28, ico, 0.55, col, C.background1);
    texto(s, t, { x: x + 1.0, y: y + 0.28, w: hw - 1.3, h: 0.55, fontSize: 22, bold: true, valign: "middle" });
    texto(s, items.map((it, j) => ({ text: it, options: { bullet: true, breakLine: j < items.length - 1, italic: j === 3 && i === 0, color: j === 3 && i === 0 ? C.text2 : C.text1 } })),
      { x: x + 0.35, y: y + 1.05, w: hw - 0.7, h: 2.0, fontSize: 15, paraSpaceAfter: 7 });
    texto(s, caso, { x: x + 0.35, y: y + 3.05, w: hw - 0.7, h: 0.6, fontSize: 13, bold: true, color: C.text2 });
  });
  tarjeta(s, ML, 5.75, CW, 0.75, { fill: PAPER_DARK });
  texto(s, [{ text: "Espigada, por eventos y sin estado → serverless.   ", options: { color: C.accent1, bold: true } },
    { text: "Constante, de baja latencia o con estado → contenedores o VMs.", options: { color: C.background1, bold: true } }],
    { x: ML + 0.3, y: 5.75, w: CW - 0.6, h: 0.75, fontSize: 16, valign: "middle" });
}

// ===== 12. Prime Video =====
{
  const s = nueva("CONTENIDO", S4);
  encabezado(s, "04 · LÍMITES Y FUTURO", "Prime Video: el contraejemplo de Amazon");
  tarjeta(s, ML, 1.75, 3.6, 3.4, { fill: PAPER_DARK });
  texto(s, "−90 %", { x: ML + 0.3, y: 2.05, w: 3.0, h: 1.4, fontSize: 64, bold: true, color: C.accent1, fontFace: THEME.headFontFace, valign: "middle" });
  texto(s, "de costo en el sistema de monitoreo de calidad de streams (Amazon, 2023)", { x: ML + 0.3, y: 3.5, w: 3.0, h: 1.4, fontSize: 15, color: C.accent6 });
  const x1 = ML + 4.0, bw = 3.65, x2 = x1 + bw + 0.75;
  [[x1, "Antes", ["Funciones encadenadas (Step Functions + Lambda)", "Varias transiciones por cada segundo de video", "Los datos viajaban entre etapas por la red y S3"]],
   [x2, "Después", ["Un solo proceso en contenedores (ECS)", "Conversión y detección juntas, en memoria", "Sin mover datos entre etapas"]]].forEach(([x, t, items], i) => {
    tarjeta(s, x, 1.75, bw, 3.4, { fill: i ? C.accent2 : C.background2, transparency: i ? 88 : 0 });
    texto(s, t, { x: x + 0.3, y: 1.95, w: bw - 0.6, h: 0.45, fontSize: 19, bold: true });
    texto(s, items.map((it, j) => ({ text: it, options: { bullet: true, breakLine: j < items.length - 1 } })),
      { x: x + 0.3, y: 2.55, w: bw - 0.6, h: 2.45, fontSize: 15, paraSpaceAfter: 9, color: C.text2 });
  });
  flecha(s, x1 + bw + 0.1, 3.45, x2 - 0.1, 3.45, C.accent1);
  tarjeta(s, ML, 5.45, CW, 1.05);
  insignia(s, ML + 0.3, 5.72, "→", 0.5);
  texto(s, [{ text: "La lección no es «serverless es malo»: ", options: { bold: true } },
    { text: "cuando comunicar cuesta más que computar, hay que juntar los componentes, no separarlos.", options: { color: C.text2 } }],
    { x: ML + 1.05, y: 5.45, w: CW - 1.35, h: 1.05, fontSize: 16, valign: "middle" });
}

// ===== 13. 2026 =====
{
  const s = nueva("CONTENIDO", S4);
  encabezado(s, "04 · LÍMITES Y FUTURO", "2026: el serverless «puro» se flexibiliza");
  const items = [
    ["Lambda Managed Instances", "Funciones sobre servidores EC2 para cargas estables, con varios pedidos por entorno. AWS admite el punto de cruce."],
    ["Lambda MicroVMs", "Sesiones de hasta 8 h que conservan estado (anunciado en julio de 2026). Rompe «efímero» y «sin estado»."],
    ["IA en el edge", "Inferencia en 300+ datacenters cerca del usuario; WebAssembly con arranques por debajo del milisegundo."],
    ["Arquitecturas híbridas", "66 % de quienes usan funciones también usan contenedores. Cada carga va donde le conviene."],
  ];
  const cw = (CW - 0.4) / 2, ch = 2.15;
  items.forEach(([t, d], i) => {
    const x = ML + (i % 2) * (cw + 0.4), y = 1.75 + Math.floor(i / 2) * (ch + 0.35);
    tarjeta(s, x, y, cw, ch);
    insignia(s, x + 0.3, y + 0.3, String(i + 1), 0.5);
    texto(s, t, { x: x + 1.0, y: y + 0.3, w: cw - 1.3, h: 0.5, fontSize: 19, bold: true, valign: "middle" });
    texto(s, d, { x: x + 1.0, y: y + 0.9, w: cw - 1.3, h: 1.1, fontSize: 15, color: C.text2 });
  });
  fuente(s, "Fuentes: AWS (2026); Datadog, State of Serverless (2025); Cloudflare.");
}

// ===== 14. Cierre =====
{
  const s = nueva("PORTADA", S4);
  texto(s, "TRES IDEAS PARA LLEVARSE", { x: ML, y: 0.9, w: 8, h: 0.4, fontSize: 13, bold: true, color: C.accent1, charSpacing: 2 });
  const ideas = [
    ["No es «sin servidores»", "es no tener que administrarlos."],
    ["Se paga por uso", "gana en cargas espigadas y pierde arriba de un tercio de uso."],
    ["Es un trade-off", "se elige por encaje con el problema, no por moda."],
  ];
  ideas.forEach(([a, b], i) => {
    const y = 1.6 + i * 1.3;
    insignia(s, ML, y + 0.1, String(i + 1), 0.65);
    texto(s, [{ text: a + ": ", options: { bold: true, color: C.background1 } }, { text: b, options: { color: C.accent6 } }],
      { x: ML + 1.0, y, w: 6.9, h: 0.85, fontSize: 20, valign: "middle" });
  });
  texto(s, "¿Preguntas?", { x: 8.95, y: 2.3, w: 3.8, h: 1.4, fontSize: 40, bold: true, color: C.accent1, fontFace: THEME.headFontFace, valign: "middle" });
  texto(s, "Gracias", { x: 8.95, y: 3.6, w: 3.9, h: 0.6, fontSize: 22, color: C.accent6 });
  texto(s, "Fuentes principales: CNCF Serverless Whitepaper · AWS Lambda (documentación y precios) · Firecracker (NSDI 2020) · Cloudflare Workers · Datadog State of Serverless 2025 · Amazon Prime Video Tech Blog (2023).",
    { x: ML, y: 5.9, w: CW, h: 0.7, fontSize: 11, color: C.accent3 });
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  console.log("ok:", OUT, "—", n, "láminas,", Object.keys(NOTAS).length, "notas");
})();
