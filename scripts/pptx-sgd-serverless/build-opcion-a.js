// Presentación de SGD: Serverless — variante A · Minimal (keynote editorial).
// Una idea por lámina, tipografía grande, negro tinta + un único acento rojo.
// Uso (desde la raíz del repo):  node scripts/pptx-sgd-serverless/build-opcion-a.js
const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");

const RAIZ = path.resolve(__dirname, "..", "..");
const DIR = path.join(RAIZ, "materias", "SGD", "entregables", "serverless", "opciones");
fs.mkdirSync(DIR, { recursive: true });
const OUT = process.argv[2] || path.join(DIR, "presentacion-A-minimal.pptx");

// ---------- paleta ----------
const INK = "111111";   // dominante: texto y formas
const RED = "D62828";   // único acento
const GREY = "6B6B6B";  // texto secundario
const LINE = "CFCFCF";  // líneas finas / contornos
const SOFT = "F2F2F2";  // relleno suave
const WHITE = "FFFFFF";
const HEAD = "Arial", BODY = "Calibri";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
pres.author = "Bonadeo, Juan Cruz y grupo";
pres.title = "Serverless — SGD (opción A)";
pres.theme = { headFontFace: HEAD, bodyFontFace: BODY };
const W = 13.333, ML = 0.8, CW = W - 2 * ML;

pres.defineSlideMaster({
  title: "BLANCO",
  background: { color: WHITE },
  objects: [],
  slideNumber: { x: W - ML - 0.6, y: 6.9, w: 0.6, h: 0.3, fontSize: 11, color: GREY, align: "right", fontFace: BODY },
});
pres.defineSlideMaster({ title: "TINTA", background: { color: INK }, objects: [] });

// ---------- helpers ----------
function T(s, text, o) {
  s.addText(text, Object.assign({ isTextBox: true, margin: 0, color: INK, fontFace: BODY, fontSize: 18, valign: "top" }, o));
}
function titulo(s, t) { T(s, t, { x: ML, y: 0.6, w: CW, h: 0.9, fontSize: 40, bold: true, fontFace: HEAD, valign: "middle" }); }
function seccion(s, t) { T(s, t, { x: ML, y: 6.9, w: 6, h: 0.3, fontSize: 11, color: GREY }); }
function fuente(s, t, y = 6.45) { T(s, t, { x: ML, y, w: CW, h: 0.3, fontSize: 11, color: GREY, italic: true }); }
function punto(s, x, y, d, color = RED) {
  s.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color }, line: { type: "none" }, objectName: "punto" });
}
function seg(s, x1, y1, x2, y2, color = INK, arrow = false, width = 2) {
  const line = { color, width };
  if (arrow) line.endArrowType = "triangle";
  s.addShape(pres.shapes.LINE, { x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1) || 0.001,
    h: Math.abs(y2 - y1) || 0.001, flipH: x2 < x1, flipV: y2 < y1, line });
}
function caja(s, x, y, w, h, o = {}) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: o.r || 0.08,
    fill: { color: o.fill || WHITE }, line: o.noLine ? { type: "none" } : { color: o.line || INK, width: o.lw || 1.5, dashType: o.dash || "solid" },
    objectName: o.name || "caja" });
}
let n = 0;
function lamina(master, sec, notas) {
  const s = pres.addSlide({ masterName: master, sectionTitle: sec });
  n += 1;
  s.addNotes(notas);
  return s;
}

const S1 = "Expositor 1 — Qué es", S2 = "Expositor 2 — Cómo funciona",
  S3 = "Expositor 3 — Economía y datos", S4 = "Expositor 4 — Límites y futuro";
const K1 = "01  Qué es", K2 = "02  Cómo funciona", K3 = "03  Economía y datos", K4 = "04  Límites y futuro";

// ================= EXPOSITOR 1 =================
pres.addSection({ title: S1 });

// 1. Portada
{
  const s = lamina("BLANCO", S1, "[Expositor 1] Buenas, somos el grupo que presenta serverless. Vamos a contar qué es, cómo funciona por dentro, cuánto cuesta de verdad y cuándo no conviene. Somos cuatro y nos pasamos la palabra por bloques.");
  punto(s, ML, 1.35, 0.42);
  T(s, "SGD · SOPORTE A LA GESTIÓN DE DATOS CON P. VISUAL", { x: ML + 0.65, y: 1.35, w: 10, h: 0.42, fontSize: 13, bold: true, color: GREY, charSpacing: 2, valign: "middle" });
  T(s, "Serverless", { x: ML - 0.05, y: 1.95, w: CW, h: 1.9, fontSize: 115, bold: true, fontFace: HEAD, valign: "middle" });
  T(s, "Qué es, cómo funciona y cuándo no conviene", { x: ML, y: 3.95, w: CW, h: 0.6, fontSize: 28, color: GREY });
  T(s, [{ text: "Integrantes  ", options: { bold: true } }, { text: "Bonadeo, Juan Cruz · [Integrante 2] · [Integrante 3] · [Integrante 4]", options: { color: GREY } }],
    { x: ML, y: 5.75, w: CW, h: 0.4, fontSize: 16 });
  T(s, "UTN — Facultad Regional Rosario · Ingeniería en Sistemas de Información · 2026", { x: ML, y: 6.2, w: CW, h: 0.35, fontSize: 14, color: GREY });
}

// 2. Statement: no significa sin servidores
{
  const s = lamina("BLANCO", S1, "[Expositor 1] Lo primero que confunde es el nombre. Serverless no significa que no haya servidores: existen, están en un datacenter y alguien los mantiene. La diferencia es que ese alguien es el proveedor, no vos. Como wireless: los cables siguen estando, pero no los tirás vos.");
  T(s, "Serverless no significa", { x: ML, y: 1.5, w: CW, h: 1.0, fontSize: 56, bold: true, fontFace: HEAD, valign: "middle" });
  T(s, "«sin servidores».", { x: ML, y: 2.5, w: CW, h: 1.0, fontSize: 56, bold: true, fontFace: HEAD, valign: "middle" });
  T(s, "Significa que no son tu problema.", { x: ML, y: 3.75, w: CW, h: 0.9, fontSize: 44, bold: true, fontFace: HEAD, color: RED, valign: "middle" });
  T(s, "Como wireless: los cables existen, pero no los tirás vos.", { x: ML, y: 5.2, w: CW, h: 0.5, fontSize: 22, color: GREY });
  seccion(s, K1);
}

// 3. Cifra: 15 billones
{
  const s = lamina("BLANCO", S1, "[Expositor 1] Y no es algo de nicho. Lambda, el servicio serverless de Amazon, ejecuta más de quince billones de invocaciones por mes, billones de los nuestros: diez a la doce. Según Datadog, el 65 % de los clientes de AWS usa Lambda y el 70 % de los de Google Cloud usa Cloud Run.");
  titulo(s, "Ya no es nicho");
  T(s, "15 billones", { x: ML - 0.05, y: 1.75, w: CW, h: 1.9, fontSize: 120, bold: true, fontFace: HEAD, color: RED, valign: "middle" });
  T(s, "de invocaciones por mes en AWS Lambda (10¹²)", { x: ML, y: 3.7, w: CW, h: 0.5, fontSize: 26, color: INK });
  [["65 %", "de los clientes de AWS usan Lambda"], ["70 %", "de los de Google Cloud usan Cloud Run"]].forEach(([a, b], i) => {
    const x = ML + i * 5.2;
    T(s, a, { x, y: 4.7, w: 2.2, h: 0.9, fontSize: 48, bold: true, fontFace: HEAD, valign: "middle" });
    T(s, b, { x: x + 2.25, y: 4.7, w: 2.7, h: 0.9, fontSize: 17, color: GREY, valign: "middle" });
  });
  fuente(s, "Fuentes: AWS (2026); Datadog, State of Serverless (2025).");
  seccion(s, K1);
}

// 4. Tres propiedades
{
  const s = lamina("BLANCO", S1, "[Expositor 1] Tomamos la definición de la CNCF, que deja tres propiedades. No administrás infraestructura; escala hasta cero cuando no hay tráfico; y pagás por ejecución, no por tener algo encendido. Si falta una, no es serverless: un Kubernetes administrado cuesta aunque nadie lo llame.");
  titulo(s, "Si falta una, no es serverless");
  const cols = [
    ["No administrás", "Ni el tamaño de la máquina, ni los parches, ni la capacidad."],
    ["Escala a cero", "De 0 a N instancias según la demanda, y de vuelta a 0."],
    ["Pagás por uso", "Por ejecución, no por tener un servidor encendido."],
  ];
  const cw = (CW - 2 * 0.6) / 3;
  cols.forEach(([h, d], i) => {
    const x = ML + i * (cw + 0.6);
    T(s, String(i + 1), { x, y: 1.75, w: cw, h: 1.8, fontSize: 120, bold: true, fontFace: HEAD, color: RED, valign: "middle" });
    T(s, h, { x, y: 3.7, w: cw, h: 0.6, fontSize: 28, bold: true, fontFace: HEAD });
    T(s, d, { x, y: 4.4, w: cw, h: 1.0, fontSize: 18, color: GREY });
  });
  fuente(s, "Definición: CNCF, Serverless Whitepaper.");
  seccion(s, K1);
}

// 5. Escalera como línea de tiempo
{
  const s = lamina("BLANCO", S1, "[Expositor 1] Serverless es el último escalón de una escalera: en cada paso te desentendés de una capa más. Pasamos de comprar el servidor a alquilar una VM, a subir una app, a un contenedor y finalmente a una función. Lo clave es la unidad de cobro: del año a la hora y de la hora al milisegundo. Pase al expositor 2: veamos qué pasa por dentro.");
  titulo(s, "La unidad de cobro: del año al milisegundo");
  const pasos = [["Bare metal", "un servidor", "año"], ["IaaS", "una VM", "hora"], ["PaaS", "una app", "hora"], ["Contenedores", "un contenedor", "hora"], ["FaaS", "una función", "ms"]];
  const x0 = 1.6, x1 = W - 1.6, yL = 4.0, step = (x1 - x0) / 4;
  seg(s, x0, yL, x1, yL, LINE, false, 2);
  pasos.forEach(([nom, dep, u], i) => {
    const cx = x0 + i * step, ult = i === 4, d = ult ? 0.55 : 0.3;
    punto(s, cx - d / 2, yL - d / 2, d, ult ? RED : INK);
    T(s, [{ text: nom, options: { bold: true, fontSize: 20, breakLine: true, fontFace: HEAD } }, { text: "desplegás " + dep, options: { fontSize: 15, color: GREY } }],
      { x: cx - 1.2, y: 2.55, w: 2.4, h: 1.0, align: "center", valign: "bottom" });
    T(s, u, { x: cx - 1.2, y: 4.45, w: 2.4, h: 0.9, align: "center", fontSize: ult ? 48 : 32, bold: true, fontFace: HEAD, color: ult ? RED : INK, valign: "middle" });
  });
  T(s, "Por primera vez, si nadie usa el sistema, el costo de cómputo es cero.", { x: ML, y: 5.75, w: CW, h: 0.5, fontSize: 22, color: GREY });
  seccion(s, K1);
}

// ================= EXPOSITOR 2 =================
pres.addSection({ title: S2 });

// 6. Ciclo de vida
{
  const s = lamina("BLANCO", S2, "[Expositor 2] Una función no está corriendo: se invoca cuando pasa algo, un pedido HTTP, un archivo, un mensaje, un horario. La primera vez hay que preparar el entorno, la fase INIT; después se ejecuta y el entorno queda congelado. Si llega otro pedido se reutiliza y se saltea INIT; si pasan 5 a 15 minutos sin pedidos, se apaga.");
  titulo(s, "Una función no corre: es invocada");
  const fases = [["EVENTO", "HTTP, archivo, cola o cron"], ["INIT", "microVM, código, runtime, tus imports"], ["INVOKE", "ejecuta el handler"], ["FREEZE", "congela; sin eventos en 5–15 min, se apaga"]];
  const d = 1.75, gap = (CW - 4 * d - 2 * 0.35) / 3, y = 2.6;
  const cx = i => ML + 0.35 + i * (d + gap) + d / 2;
  fases.forEach(([f, desc], i) => {
    const x = cx(i) - d / 2, init = i === 1;
    s.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: init ? RED : WHITE }, line: init ? { type: "none" } : { color: INK, width: 2 }, objectName: "fase" });
    T(s, f, { x, y, w: d, h: d, fontSize: 18, bold: true, fontFace: HEAD, color: init ? WHITE : INK, align: "center", valign: "middle" });
    T(s, desc, { x: cx(i) - 1.3, y: y + d + 0.2, w: 2.6, h: 0.8, fontSize: 15, color: GREY, align: "center" });
    if (i < 3) seg(s, x + d + 0.1, y + d / 2, x + d + gap - 0.1, y + d / 2, INK, true);
  });
  // vuelta warm por arriba: FREEZE -> INVOKE
  const ya = 2.2;
  seg(s, cx(3), y - 0.02, cx(3), ya, GREY); seg(s, cx(3), ya, cx(2), ya, GREY); seg(s, cx(2), ya, cx(2), y - 0.05, GREY, true);
  T(s, "warm: reusa el entorno, sin INIT", { x: cx(2), y: 1.8, w: cx(3) - cx(2), h: 0.3, fontSize: 14, italic: true, color: GREY, align: "center" });
  T(s, "sólo en cold start", { x: cx(1) - 1.3, y: 2.2, w: 2.6, h: 0.3, fontSize: 14, italic: true, color: RED, align: "center" });
  seccion(s, K2);
}

// 7. Cifra: < 125 ms
{
  const s = lamina("BLANCO", S2, "[Expositor 2] El proveedor tiene que correr código de miles de clientes en la misma máquina, aislados y en milisegundos. Amazon lo resolvió con Firecracker, un monitor de máquinas virtuales escrito en Rust: levanta una microVM en menos de 125 milisegundos con unos 5 megas de memoria extra. Es menos de lo que dura un parpadeo.");
  titulo(s, "Una VM en menos de un parpadeo");
  T(s, "< 125 ms", { x: ML - 0.05, y: 1.75, w: CW, h: 1.9, fontSize: 130, bold: true, fontFace: HEAD, color: RED, valign: "middle" });
  T(s, "tarda Firecracker en arrancar una microVM con Linux: la base de AWS Lambda", { x: ML, y: 3.7, w: CW, h: 0.5, fontSize: 24 });
  [["~5 MiB", "de memoria extra por microVM"], ["KVM", "aislamiento por hardware, no por confianza"], ["100–150 ms", "dura un parpadeo"]].forEach(([a, b], i) => {
    const x = ML + i * 3.95;
    T(s, a, { x, y: 4.75, w: 3.7, h: 0.75, fontSize: 36, bold: true, fontFace: HEAD, valign: "middle" });
    T(s, b, { x, y: 5.5, w: 3.6, h: 0.6, fontSize: 16, color: GREY });
  });
  seccion(s, K2);
}

// 8. Cold start (barras de rango)
{
  const s = lamina("BLANCO", S2, "[Expositor 2] Esa primera invocación, la que pasa por INIT, es más lenta: es el cold start, el precio de poder escalar a cero. Depende del lenguaje: Go o Rust menos de 100 ms, Python entre 200 y 400, Java sin optimizar puede tardar segundos. Se mitiga con entornos precalentados, que se pagan por hora, o con SnapStart, que restaura una foto de un entorno ya inicializado.");
  titulo(s, "Cold start: el precio de escalar a cero");
  const x0 = ML + 3.0, aw = 6.5, maxMs = 500, sc = aw / maxMs, y0 = 1.8, rh = 0.66;
  const filas = [["Go / Rust", 10, 100, "< 100 ms"], ["Java + SnapStart", 90, 140, "90–140 ms"], ["Python", 200, 400, "200–400 ms"], ["Java sin SnapStart", 300, 500, "segundos", true], ["Extra en VPC", 200, 500, "+200–500 ms"]];
  for (let t = 0; t <= maxMs; t += 100) {
    s.addShape(pres.shapes.LINE, { x: x0 + t * sc, y: y0 - 0.05, w: 0.001, h: filas.length * rh, line: { color: LINE, width: 0.75 } });
    T(s, String(t), { x: x0 + t * sc - 0.3, y: y0 + filas.length * rh + 0.02, w: 0.6, h: 0.3, fontSize: 12, color: GREY, align: "center" });
  }
  T(s, "milisegundos", { x: x0, y: y0 + filas.length * rh + 0.32, w: aw, h: 0.3, fontSize: 12, color: GREY, align: "center" });
  filas.forEach(([lbl, a, b, val, sale], i) => {
    const y = y0 + i * rh, extra = i === 4;
    T(s, lbl, { x: ML, y, w: 2.8, h: 0.48, fontSize: 18, align: "right", valign: "middle", color: extra ? GREY : INK, italic: extra });
    s.addShape(pres.shapes.RECTANGLE, { x: x0 + a * sc, y: y + 0.1, w: (b - a) * sc, h: 0.3, fill: { color: extra ? LINE : (i === 2 ? RED : INK) }, line: { type: "none" }, objectName: "rango" });
    if (sale) seg(s, x0 + b * sc, y + 0.25, x0 + aw + 0.3, y + 0.25, INK, true);
    T(s, val, { x: sale ? x0 + aw + 0.4 : x0 + b * sc + 0.12, y, w: 1.6, h: 0.48, fontSize: 16, bold: true, valign: "middle", color: extra ? GREY : INK });
  });
  T(s, [{ text: "Se mitiga ", options: { bold: true } }, { text: "con entornos precalentados (se pagan por hora) o con SnapStart (restaura un entorno ya inicializado).", options: { color: GREY } }],
    { x: ML, y: 5.95, w: CW, h: 0.45, fontSize: 18 });
  fuente(s, "Órdenes de magnitud reportados en 2026 (fuentes secundarias), no mediciones propias.");
  seccion(s, K2);
}

// 9. Concurrencia
{
  const s = lamina("BLANCO", S2, "[Expositor 2] En Lambda cada entorno atiende un pedido a la vez. La cuenta es pedidos por segundo por duración: cien pedidos por segundo que tardan dos décimas son 20 entornos simultáneos; si tardan dos segundos, son 200. El límite por defecto es mil por cuenta y región, y es la causa número uno de throttling.");
  titulo(s, "Un pedido por entorno a la vez");
  const q = 0.16, g = 0.06, gx = 7.4;
  // fila 1
  T(s, [{ text: "100 pedidos/s × 0,2 s", options: { breakLine: true } }, { text: "= 20 entornos", options: { bold: true, color: INK } }],
    { x: ML, y: 1.85, w: 6.2, h: 1.0, fontSize: 28, color: GREY, fontFace: HEAD });
  for (let i = 0; i < 20; i++) s.addShape(pres.shapes.RECTANGLE, { x: gx + i * (q + g), y: 2.25, w: q, h: q, fill: { color: INK }, line: { type: "none" }, objectName: "entorno" });
  // fila 2
  T(s, [{ text: "100 pedidos/s × 2 s", options: { breakLine: true } }, { text: "= 200 entornos", options: { bold: true, color: RED } }],
    { x: ML, y: 3.55, w: 6.2, h: 1.0, fontSize: 28, color: GREY, fontFace: HEAD });
  for (let r = 0; r < 10; r++) for (let c = 0; c < 20; c++)
    s.addShape(pres.shapes.RECTANGLE, { x: gx + c * (q + g), y: 3.35 + r * (q + g), w: q, h: q, fill: { color: RED }, line: { type: "none" }, objectName: "entorno" });
  T(s, "concurrencia = pedidos por segundo × duración · límite por defecto: 1000 por cuenta y región", { x: ML, y: 5.85, w: CW, h: 0.45, fontSize: 18, color: GREY });
  seccion(s, K2);
}

// 10. Stateless
{
  const s = lamina("BLANCO", S2, "[Expositor 2] Consecuencia directa: dos pedidos no tienen garantía de caer en el mismo entorno. Por eso el estado de negocio nunca se guarda en la memoria de la función: va a la base. Serverless es stateless por contrato, no por casualidad. Pase al expositor 3: todo esto tiene un costo.");
  titulo(s, "Stateless por contrato");
  const yA = 2.6, yB = 4.0;
  [[yA, "pedido 1", "entorno A"], [yB, "pedido 2", "entorno B"]].forEach(([y, p, e]) => {
    caja(s, ML, y, 1.9, 0.75, { fill: SOFT, noLine: true, r: 0.37 });
    T(s, p, { x: ML, y, w: 1.9, h: 0.75, fontSize: 18, align: "center", valign: "middle" });
    seg(s, ML + 2.0, y + 0.375, ML + 3.0, y + 0.375, INK, true);
    caja(s, ML + 3.1, y, 2.3, 0.75);
    T(s, e, { x: ML + 3.1, y, w: 2.3, h: 0.75, fontSize: 18, bold: true, align: "center", valign: "middle" });
    seg(s, ML + 5.5, y + 0.375, ML + 6.6, 3.7, RED, true);
  });
  s.addShape(pres.shapes.CAN, { x: ML + 6.7, y: 2.95, w: 1.4, h: 1.5, fill: { color: RED }, line: { type: "none" }, objectName: "base" });
  T(s, "base de datos", { x: ML + 6.3, y: 4.55, w: 2.2, h: 0.4, fontSize: 16, bold: true, align: "center", color: RED });
  T(s, "No hay garantía de caer en el mismo entorno.", { x: ML + 8.9, y: 2.6, w: 3.0, h: 1.4, fontSize: 24, bold: true, fontFace: HEAD });
  T(s, "El estado va a la base, nunca a la memoria de la función.", { x: ML + 8.9, y: 4.0, w: 3.0, h: 1.0, fontSize: 18, color: GREY });
  seccion(s, K2);
}

// ================= EXPOSITOR 3 =================
pres.addSection({ title: S3 });

// 11. Costo de un caso concreto (gráfico nativo)
{
  const s = lamina("BLANCO", S3, "[Expositor 3] Se cobra por pedido, veinte centavos de dólar por millón, y por gigabyte-segundo: memoria por tiempo de ejecución, al milisegundo. Una API con cinco millones de pedidos al mes, de 200 ms y medio giga cada uno, cuesta unos 2,47 dólares descontando la capa gratuita. Una VM chica encendida todo el mes cuesta unos 15: seis veces más.");
  titulo(s, "5 millones de pedidos al mes: USD 2,47");
  s.addChart(pres.charts.BAR, [{ name: "USD por mes", labels: ["VM t3.small 24×7", "Lambda"], values: [15, 2.47] }], {
    x: ML, y: 1.8, w: 7.2, h: 3.6, barDir: "bar", varyColors: true, chartColors: [INK, RED],
    showValue: true, dataLabelPosition: "outEnd", dataLabelFormatCode: '"USD "0.00', dataLabelFontSize: 16, dataLabelFontBold: true, dataLabelColor: INK, dataLabelFontFace: BODY,
    catAxisLabelColor: INK, catAxisLabelFontSize: 16, catAxisLabelFontFace: BODY, catAxisLineShow: false,
    valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" }, valAxisMinVal: 0, valAxisMaxVal: 18,
    showLegend: false, barGapWidthPct: 50,
  });
  T(s, "6×", { x: ML + 7.7, y: 1.8, w: 4.0, h: 1.9, fontSize: 130, bold: true, fontFace: HEAD, color: RED, valign: "middle" });
  T(s, "más barato que una máquina virtual chica encendida todo el mes", { x: ML + 7.75, y: 3.8, w: 3.9, h: 1.0, fontSize: 20, color: GREY });
  fuente(s, "API de 200 ms y 512 MB por pedido. Precios oficiales de AWS Lambda (US East, x86); cálculo propio.", 5.75);
  seccion(s, K3);
}

// 12. Punto de cruce (gráfico nativo)
{
  const s = lamina("BLANCO", S3, "[Expositor 3] Pero esa API está ociosa casi todo el tiempo. Normalizado por procesador, el vCPU-hora de Lambda cuesta unas tres veces el de una instancia equivalente. El servidor es una línea plana; Lambda arranca en cero y sube con el uso. Se cruzan cerca del 34 %, un tercio: debajo gana serverless, arriba conviene el servidor.");
  titulo(s, "El punto de cruce: un tercio de uso");
  const us = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
  s.addChart(pres.charts.LINE, [
    { name: "Lambda", labels: us.map(u => u + " %"), values: us.map(u => +(0.106 * u / 100).toFixed(4)) },
    { name: "Servidor encendido 24/7", labels: us.map(u => u + " %"), values: us.map(() => 0.036) },
  ], {
    x: ML, y: 1.7, w: 7.8, h: 4.6, chartColors: [RED, INK], lineSize: 4, lineDataSymbol: "none",
    showLegend: true, legendPos: "t", legendFontSize: 14, legendFontFace: BODY, legendColor: INK,
    showCatAxisTitle: true, catAxisTitle: "utilización", catAxisTitleFontSize: 13, catAxisTitleColor: GREY, catAxisTitleFontFace: BODY,
    showValAxisTitle: true, valAxisTitle: "USD por vCPU-hora", valAxisTitleFontSize: 13, valAxisTitleColor: GREY, valAxisTitleFontFace: BODY,
    catAxisLabelColor: GREY, valAxisLabelColor: GREY, catAxisLabelFontSize: 13, valAxisLabelFontSize: 13, catAxisLabelFontFace: BODY, valAxisLabelFontFace: BODY,
    valAxisLabelFormatCode: "0.00", valAxisMinVal: 0, valAxisMaxVal: 0.12, valAxisMajorUnit: 0.02,
    valGridLine: { color: "EEEEEE", size: 1 }, catGridLine: { style: "none" },
  });
  T(s, "≈ 34 %", { x: ML + 8.2, y: 1.9, w: 3.6, h: 1.4, fontSize: 80, bold: true, fontFace: HEAD, color: RED, valign: "middle" });
  T(s, "punto de cruce", { x: ML + 8.25, y: 3.3, w: 3.5, h: 0.45, fontSize: 20, bold: true });
  T(s, "El vCPU-hora de Lambda cuesta ~3× el de una instancia: gana en cargas espigadas, pierde en las constantes.", { x: ML + 8.25, y: 3.9, w: 3.5, h: 1.6, fontSize: 17, color: GREY });
  fuente(s, "Cálculo propio: Lambda ≈ USD 0,106 / vCPU-h; EC2 c7g.large ≈ USD 0,036 / vCPU-h.");
  seccion(s, K3);
}

// 13. Bases de datos: separar cómputo de almacenamiento
{
  const s = lamina("BLANCO", S3, "[Expositor 3] Esto es lo más cercano a la materia. Para que una base sea serverless tiene que poder apagar el cómputo sin perder los datos: los datos viven en un almacenamiento persistente y los nodos que procesan consultas se prenden y apagan según la demanda. Así funcionan Neon, Aurora Serverless v2 y DynamoDB on-demand.");
  titulo(s, "Datos: apagar el cómputo sin perder la base");
  const bw = 1.9, g = 0.35, x0 = ML;
  for (let i = 0; i < 3; i++) {
    const on = i === 1, x = x0 + i * (bw + g);
    caja(s, x, 2.5, bw, 1.0, on ? { fill: RED, noLine: true } : { line: LINE, dash: "dash", lw: 1.5 });
    T(s, on ? "cómputo activo" : "apagado", { x, y: 2.5, w: bw, h: 1.0, fontSize: 17, bold: on, color: on ? WHITE : GREY, align: "center", valign: "middle" });
  }
  seg(s, x0 + bw + g + bw / 2, 3.6, x0 + bw + g + bw / 2, 4.2, INK, true);
  caja(s, x0, 4.3, 3 * bw + 2 * g, 1.1, { fill: INK, noLine: true });
  T(s, "almacenamiento persistente", { x: x0, y: 4.3, w: 3 * bw + 2 * g, h: 1.1, fontSize: 22, bold: true, color: WHITE, align: "center", valign: "middle" });
  const xr = ML + 7.3, wr = W - ML - xr;
  T(s, "Separar cómputo de almacenamiento", { x: xr, y: 2.5, w: wr, h: 1.4, fontSize: 30, bold: true, fontFace: HEAD });
  T(s, [{ text: "Neon", options: { bold: true, breakLine: true } }, { text: "Aurora Serverless v2", options: { bold: true, breakLine: true } }, { text: "DynamoDB on-demand", options: { bold: true } }],
    { x: xr, y: 4.1, w: wr, h: 1.4, fontSize: 20, paraSpaceAfter: 6 });
  seccion(s, K3);
}

// 14. El choque de las conexiones
{
  const s = lamina("BLANCO", S3, "[Expositor 3] Pero hay un choque clásico: Postgres soporta cientos de conexiones, no miles. Si quinientas funciones corren a la vez y cada una abre su conexión, la base se cae. Se resuelve con un pooler en el medio, como RDS Proxy o PgBouncer, o con bases que se consultan por HTTP. Pase al expositor 4: cuándo conviene y cuándo no.");
  titulo(s, "El choque: las conexiones");
  T(s, "500", { x: ML - 0.05, y: 1.75, w: 4.6, h: 1.9, fontSize: 130, bold: true, fontFace: HEAD, color: RED, valign: "middle" });
  T(s, "funciones a la vez, una conexión cada una. Postgres soporta cientos.", { x: ML, y: 3.7, w: 4.6, h: 1.1, fontSize: 22 });
  // diagrama: λ -> pooler -> base
  const fx = ML + 5.4, fy = 1.95, px = ML + 7.6, dbx = W - ML - 1.4;
  for (let i = 0; i < 6; i++) {
    const y = fy + i * 0.5;
    caja(s, fx, y, 1.0, 0.36, { fill: INK, noLine: true, r: 0.05 });
    T(s, "λ", { x: fx, y, w: 1.0, h: 0.36, fontSize: 16, bold: true, color: WHITE, align: "center", valign: "middle" });
    seg(s, fx + 1.05, y + 0.18, px - 0.05, fy + 1.43, GREY, true, 1.25);
  }
  caja(s, px, fy + 1.0, 1.7, 0.86, { fill: RED, noLine: true });
  T(s, "pooler", { x: px, y: fy + 1.0, w: 1.7, h: 0.86, fontSize: 20, bold: true, color: WHITE, align: "center", valign: "middle" });
  seg(s, px + 1.75, fy + 1.43, dbx - 0.08, fy + 1.43, INK, true);
  s.addShape(pres.shapes.CAN, { x: dbx, y: fy + 0.75, w: 1.4, h: 1.4, fill: { color: INK }, line: { type: "none" }, objectName: "base" });
  T(s, "Postgres", { x: dbx - 0.2, y: fy + 2.25, w: 1.8, h: 0.35, fontSize: 15, align: "center", color: GREY });
  T(s, [{ text: "Solución: ", options: { bold: true } }, { text: "un pooler (RDS Proxy, PgBouncer) que reutiliza pocas conexiones, o bases con API HTTP (DynamoDB, driver serverless de Neon).", options: { color: GREY } }],
    { x: ML, y: 5.35, w: CW, h: 0.8, fontSize: 18 });
  seccion(s, K3);
}

// ================= EXPOSITOR 4 =================
pres.addSection({ title: S4 });

// 15. Cuándo sí / cuándo no
{
  const s = lamina("BLANCO", S4, "[Expositor 4] Juntando todo: serverless encaja cuando la carga es espigada, disparada por eventos y sin estado, como generar una miniatura al subir una foto o procesar sensores. iRobot procesa así más de veinte millones de eventos por día. No encaja cuando la carga es constante, la latencia es crítica, hay estado o conexiones persistentes, o el sistema es una cadena larga de funciones acopladas.");
  titulo(s, "Cuándo sí, cuándo no");
  const cw = (CW - 1.0) / 2;
  [["ENCAJA", "Espigada", RED, ["por eventos y asíncrona", "sin estado, paralelizable", "miniaturas, IoT, tareas programadas"]],
   ["NO ENCAJA", "Constante", INK, ["latencia crítica: el cold start no se tolera", "con estado o conexiones persistentes", "cadenas largas de funciones acopladas"]]].forEach(([k, big, col, items], i) => {
    const x = ML + i * (cw + 1.0);
    T(s, k, { x, y: 1.85, w: cw, h: 0.4, fontSize: 14, bold: true, color: GREY, charSpacing: 2 });
    T(s, big, { x, y: 2.25, w: cw, h: 1.3, fontSize: 64, bold: true, fontFace: HEAD, color: col, valign: "middle" });
    T(s, items.map((t, j) => ({ text: t, options: { breakLine: j < items.length - 1 } })), { x, y: 3.75, w: cw, h: 1.6, fontSize: 20, paraSpaceAfter: 8 });
  });
  T(s, "iRobot: más de 20 M de eventos IoT por día con Lambda, −30 % de costo cloud (reportado por el proveedor).", { x: ML, y: 5.75, w: CW, h: 0.45, fontSize: 16, color: GREY, italic: true });
  seccion(s, K4);
}

// 16. Prime Video −90 %
{
  const s = lamina("BLANCO", S4, "[Expositor 4] El caso más famoso lo contó el propio Amazon. En 2023, Prime Video sacó de serverless su sistema de monitoreo de calidad de streams: eran funciones encadenadas con varias transiciones por cada segundo de video y los datos viajaban por la red. Lo pasaron a un solo proceso en contenedores y el costo bajó un 90 %.");
  titulo(s, "El contraejemplo de Amazon");
  T(s, "−90 %", { x: ML - 0.05, y: 1.65, w: CW, h: 2.3, fontSize: 160, bold: true, fontFace: HEAD, color: RED, valign: "middle" });
  T(s, "de costo en el monitoreo de streams de Prime Video (2023)", { x: ML, y: 4.0, w: CW, h: 0.5, fontSize: 26 });
  // antes -> después
  const y = 4.95;
  T(s, [{ text: "Antes  ", options: { bold: true, color: INK } }, { text: "funciones encadenadas, datos por la red", options: { color: GREY } }], { x: ML, y, w: 5.3, h: 0.5, fontSize: 18, valign: "middle" });
  seg(s, ML + 5.45, y + 0.25, ML + 6.25, y + 0.25, RED, true);
  T(s, [{ text: "Después  ", options: { bold: true, color: INK } }, { text: "un solo proceso en contenedores", options: { color: GREY } }], { x: ML + 6.45, y, w: 5.3, h: 0.5, fontSize: 18, valign: "middle" });
  seccion(s, K4);
}

// 17. Statement: la lección
{
  const s = lamina("BLANCO", S4, "[Expositor 4] La lección no es que serverless sea malo. Lo que más costaba no era procesar: era mover datos entre etapas. Cuando comunicar cuesta más que computar, hay que juntar los componentes, no separarlos.");
  T(s, "Cuando comunicar cuesta", { x: ML, y: 1.7, w: CW, h: 1.0, fontSize: 54, bold: true, fontFace: HEAD, valign: "middle" });
  T(s, "más que computar,", { x: ML, y: 2.7, w: CW, h: 1.0, fontSize: 54, bold: true, fontFace: HEAD, valign: "middle" });
  T(s, "hay que juntar, no separar.", { x: ML, y: 3.8, w: CW, h: 1.0, fontSize: 54, bold: true, fontFace: HEAD, color: RED, valign: "middle" });
  T(s, "La lección de Prime Video no es «serverless es malo».", { x: ML, y: 5.3, w: CW, h: 0.5, fontSize: 22, color: GREY });
  seccion(s, K4);
}

// 18. 2026
{
  const s = lamina("BLANCO", S4, "[Expositor 4] Y la industria tomó nota. En 2026 AWS lanzó Lambda Managed Instances, funciones sobre servidores dedicados para cargas estables: el propio proveedor admite el punto de cruce. También anunció microVMs con sesiones de hasta ocho horas que conservan estado. Y dos de cada tres que usan funciones también usan contenedores: el futuro es híbrido.");
  titulo(s, "2026: el propio AWS se flexibiliza");
  const cw = (CW - 2 * 0.6) / 3;
  [["8 h", "sesiones de Lambda MicroVMs que conservan estado (anuncio de julio de 2026)", RED],
   ["66 %", "de quienes usan funciones también usan contenedores", INK],
   ["19 %", "de las funciones Lambda ya corren en ARM; eran 9 % dos años antes", INK]].forEach(([a, b, col], i) => {
    const x = ML + i * (cw + 0.6);
    T(s, a, { x, y: 1.8, w: cw, h: 1.7, fontSize: 96, bold: true, fontFace: HEAD, color: col, valign: "middle" });
    T(s, b, { x, y: 3.6, w: cw, h: 1.2, fontSize: 18, color: GREY });
  });
  T(s, [{ text: "Lambda Managed Instances: ", options: { bold: true } }, { text: "funciones sobre EC2 para cargas estables. Es AWS reconociendo el punto de cruce.", options: { color: GREY } }],
    { x: ML, y: 5.2, w: CW, h: 0.8, fontSize: 18 });
  fuente(s, "Fuentes: AWS (2026); Datadog, State of Serverless (2025).");
  seccion(s, K4);
}

// 19. Cierre
{
  const s = lamina("TINTA", S4, "[Expositor 4] Para cerrar, tres ideas. Serverless no es sin servidores: es no administrarlos. Se paga por uso, así que gana en cargas espigadas y pierde arriba de un tercio de utilización. Y es un trade-off: se elige por encaje con el problema, no por moda. Gracias, ¿preguntas?");
  T(s, "TRES IDEAS PARA LLEVARSE", { x: ML, y: 0.8, w: 8, h: 0.4, fontSize: 14, bold: true, color: GREY, charSpacing: 2 });
  const ideas = [["No es «sin servidores»", "es no administrarlos."], ["Se paga por uso", "pierde arriba de un tercio de uso."], ["Es un trade-off", "se elige por encaje, no por moda."]];
  ideas.forEach(([a, b], i) => {
    const y = 1.55 + i * 1.35;
    T(s, String(i + 1), { x: ML, y, w: 0.8, h: 1.0, fontSize: 54, bold: true, fontFace: HEAD, color: RED, valign: "middle" });
    T(s, [{ text: a, options: { bold: true, color: WHITE, breakLine: true } }, { text: b, options: { color: "BDBDBD" } }],
      { x: ML + 0.95, y, w: 5.9, h: 1.0, fontSize: 22, valign: "middle" });
  });
  T(s, "¿Preguntas?", { x: 7.9, y: 2.4, w: 4.7, h: 1.3, fontSize: 48, bold: true, fontFace: HEAD, color: RED, valign: "middle" });
  T(s, "Gracias", { x: 7.9, y: 3.7, w: 4.0, h: 0.6, fontSize: 24, color: "BDBDBD" });
  T(s, "Fuentes: CNCF Serverless Whitepaper · AWS Lambda (documentación y precios) · Firecracker (NSDI 2020) · Cloudflare Workers · Datadog State of Serverless 2025 · Prime Video Tech Blog (2023).",
    { x: ML, y: 6.2, w: CW, h: 0.6, fontSize: 11, color: "9E9E9E" });
}

pres.writeFile({ fileName: OUT }).then(() => console.log("ok:", OUT, "—", n, "láminas"));
