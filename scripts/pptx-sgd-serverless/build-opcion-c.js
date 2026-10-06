// Presentación de SGD: Serverless — variante C · Historia.
// Hilo conductor: el SysAcad, el sistema de autogestión de la facu, el día de inscripción a materias.
// Los números del caso son supuestos ilustrativos, no mediciones del SysAcad real.
// Uso (desde la raíz del repo):  node scripts/pptx-sgd-serverless/build-opcion-c.js
const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");

const RAIZ = path.resolve(__dirname, "..", "..");
const DIR = path.join(RAIZ, "materias", "SGD", "entregables", "serverless", "opciones");
fs.mkdirSync(DIR, { recursive: true });
const OUT = process.argv[2] || path.join(DIR, "presentacion-C-historia.pptx");

// ---------- paleta: violeta profundo + coral ----------
const INK = "1E1433";      // texto principal
const VIOLET = "3B1F78";   // primario
const NIGHT = "1A0F3D";    // fondo de capítulos
const LAV = "F1EDFA";      // tarjetas
const LAV2 = "D9D0F0";     // bordes y elementos suaves
const CORAL = "F2545B";    // acento
const SLATE = "4A4560";    // texto secundario
const MUTED = "7A7391";    // captions
const WHITE = "FFFFFF";
const HEAD = "Cambria", BODY = "Calibri";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
pres.author = "Bonadeo, Juan Cruz y grupo";
pres.title = "Serverless — SGD (opción C: historia)";
pres.theme = { headFontFace: HEAD, bodyFontFace: BODY };
const W = 13.333, ML = 0.6, CW = W - 2 * ML;

pres.defineSlideMaster({ title: "OSCURA", background: { color: NIGHT }, objects: [] });
pres.defineSlideMaster({
  title: "CONTENIDO",
  background: { color: WHITE },
  objects: [
    { placeholder: { options: { name: "kicker", type: "body", x: ML, y: 0.35, w: 9, h: 0.35,
        fontSize: 12, bold: true, color: CORAL, charSpacing: 2, margin: 0, valign: "middle", fontFace: BODY }, text: "" } },
    { placeholder: { options: { name: "title", type: "title", x: ML, y: 0.7, w: CW, h: 0.8,
        fontSize: 30, bold: true, color: VIOLET, fontFace: HEAD, margin: 0, valign: "middle", align: "left" }, text: "" } },
    { text: { text: "SGD · Serverless", options: { x: ML, y: 7.0, w: 4, h: 0.3, fontSize: 10, color: MUTED, margin: 0, fontFace: BODY } } },
  ],
  slideNumber: { x: W - ML - 0.6, y: 7.0, w: 0.6, h: 0.3, fontSize: 10, color: MUTED, align: "right" },
});

// ---------- helpers ----------
function nueva(master, seccion, nota) {
  const s = pres.addSlide({ masterName: master, sectionTitle: seccion });
  s.addNotes(nota);
  return s;
}
function encabezado(s, kicker, titulo) {
  s.addText(kicker, { placeholder: "kicker" });
  s.addText(titulo, { placeholder: "title" });
}
function texto(s, t, o) {
  s.addText(t, Object.assign({ isTextBox: true, margin: 0, color: INK, fontSize: 15, valign: "top", fontFace: BODY }, o));
}
function caja(s, x, y, w, h, fill = LAV, line = null, name = "tarjeta") {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.1, fill: { color: fill },
    line: line ? { color: line, width: 1 } : { type: "none" }, objectName: name });
}
function circulo(s, x, y, t, d = 0.55, fill = CORAL, color = WHITE) {
  s.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: fill }, line: { type: "none" }, objectName: "circulo" });
  texto(s, t, { x, y, w: d, h: d, align: "center", valign: "middle", fontSize: 16, bold: true, color, fontFace: HEAD });
}
function flecha(s, x1, y1, x2, y2, color = MUTED) {
  s.addShape(pres.shapes.LINE, { x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1) || 0.001,
    h: Math.abs(y2 - y1) || 0.001, flipH: x2 < x1, flipV: y2 < y1, line: { color, width: 2, endArrowType: "triangle" } });
}
function linea(s, x1, y1, x2, y2, color = MUTED) {
  s.addShape(pres.shapes.LINE, { x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1) || 0.001,
    h: Math.abs(y2 - y1) || 0.001, line: { color, width: 2 } });
}
function supuesto(s, x, y, w) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h: 0.32, rectRadius: 0.16, fill: { color: WHITE }, line: { color: CORAL, width: 1 }, objectName: "rotulo-supuesto" });
  texto(s, "SUPUESTO DEL EJEMPLO", { x, y, w, h: 0.32, fontSize: 10, bold: true, color: CORAL, align: "center", valign: "middle", charSpacing: 1 });
}
function fuente(s, t) { texto(s, t, { x: ML, y: 6.62, w: CW, h: 0.3, fontSize: 10, color: MUTED, italic: true }); }
function capitulo(seccion, num, pregunta, bajada, nota) {
  const s = nueva("OSCURA", seccion, nota);
  texto(s, num, { x: ML, y: 1.3, w: 3, h: 1.4, fontSize: 88, bold: true, color: CORAL, fontFace: HEAD, valign: "middle" });
  texto(s, pregunta, { x: ML, y: 2.95, w: 10.5, h: 1.7, fontSize: 40, bold: true, color: WHITE, fontFace: HEAD, valign: "top" });
  texto(s, bajada, { x: ML, y: 4.85, w: 10, h: 0.9, fontSize: 18, color: LAV2 });
  // motivo: hilera de "alumnos" — sólo algunos activos
  for (let i = 0; i < 14; i++) {
    s.addShape(pres.shapes.OVAL, { x: ML + i * 0.42, y: 6.25, w: 0.24, h: 0.24,
      fill: { color: i % 4 === 1 ? CORAL : "3A2E66" }, line: { type: "none" }, objectName: "alumno" });
  }
  return s;
}

const S1 = "Expositor 1 — El caso y qué es";
const S2 = "Expositor 2 — Qué pasa por dentro";
const S3 = "Expositor 3 — Costos y base de datos";
const S4 = "Expositor 4 — Cuándo no y cierre";

// ===================== BLOQUE 1 =====================
pres.addSection({ title: S1 });

// 1. Portada
{
  const s = nueva("OSCURA", S1,
    "[Expositor 1] Buenas, somos el grupo de serverless. En vez de definirlo de entrada, vamos a contarlo con una historia que todos sufrimos: el SysAcad el día de inscripción a materias. Todo el año anda, y justo el día que lo necesitamos todos, se cae. Cada uno de nosotros va a responder una pregunta sobre ese caso.");
  texto(s, "SOPORTE A LA GESTIÓN DE DATOS CON P. VISUAL", { x: ML, y: 1.1, w: 8, h: 0.4, fontSize: 13, bold: true, color: CORAL, charSpacing: 2 });
  texto(s, "Serverless", { x: ML, y: 1.65, w: 8, h: 1.4, fontSize: 72, bold: true, color: WHITE, fontFace: HEAD, valign: "middle" });
  texto(s, "La historia del SysAcad, que se cae justo el día de la inscripción", { x: ML, y: 3.15, w: 7.4, h: 1.1, fontSize: 26, color: LAV2, fontFace: HEAD, italic: true });
  texto(s, [
    { text: "Integrantes: ", options: { bold: true, color: WHITE } },
    { text: "Bonadeo, Juan Cruz · [Integrante 2] · [Integrante 3] · [Integrante 4]", options: { color: LAV2 } },
  ], { x: ML, y: 5.55, w: 8.6, h: 0.4, fontSize: 14 });
  texto(s, "UTN — Facultad Regional Rosario · Ingeniería en Sistemas de Información · 2026", { x: ML, y: 6.0, w: 8.6, h: 0.4, fontSize: 13, color: MUTED });
  // motivo: grilla de alumnos, casi todos apagados salvo un bloque encendido (el pico)
  for (let r = 0; r < 6; r++) for (let c = 0; c < 6; c++) {
    const on = r >= 2 && c >= 2 && r <= 4;
    s.addShape(pres.shapes.OVAL, { x: 9.15 + c * 0.6, y: 1.25 + r * 0.6, w: 0.38, h: 0.38,
      fill: { color: on ? CORAL : "3A2E66" }, line: { type: "none" }, objectName: "alumno" });
  }
  texto(s, "El día de inscripción, todos a la vez", { x: 9.15, y: 4.95, w: 3.6, h: 0.4, fontSize: 12, italic: true, color: MUTED });
}

// 2. El caso: el 503 del día de inscripción + demanda contra capacidad (gráfico nativo)
{
  const s = nueva("CONTENIDO", S1,
    "[Expositor 1] Esto lo vimos todos: el día que abre la inscripción a cursado entramos al SysAcad y nos encontramos con esto. El gráfico explica por qué. La línea violeta es lo que aguanta un servidor dimensionado para el uso normal; la coral es la demanda de ese día. A las ocho la demanda la supera unas cinco veces, y todo lo que no entra se responde con un error. El resto del año, en cambio, ese servidor está casi ocioso. Los números son supuestos para el ejemplo: no sabemos cómo está montado el SysAcad por dentro.");
  encabezado(s, "EL CASO", "SysAcad: tranquilo todo el año, caído el día de inscripción");
  // ventana de navegador con el 503
  const bx = ML, by = 1.75, bw = 5.0, bh = 3.0;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: bx, y: by, w: bw, h: bh, rectRadius: 0.12, fill: { color: WHITE }, line: { color: LAV2, width: 1 },
    shadow: { type: "outer", color: "3B1F78", opacity: 0.18, blur: 10, offset: 3, angle: 90 }, objectName: "navegador" });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: bx, y: by, w: bw, h: 0.5, rectRadius: 0.12, fill: { color: LAV }, line: { type: "none" }, objectName: "barra" });
  s.addShape(pres.shapes.RECTANGLE, { x: bx, y: by + 0.3, w: bw, h: 0.2, fill: { color: LAV }, line: { type: "none" }, objectName: "barra-base" });
  ["F2545B", "F5B841", "5BC27A"].forEach((c, i) => s.addShape(pres.shapes.OVAL, { x: bx + 0.2 + i * 0.22, y: by + 0.18, w: 0.14, h: 0.14, fill: { color: c }, line: { type: "none" }, objectName: "punto" }));
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: bx + 0.95, y: by + 0.11, w: bw - 1.15, h: 0.28, rectRadius: 0.14, fill: { color: WHITE }, line: { color: LAV2, width: 0.75 }, objectName: "url" });
  texto(s, "sysacad · inscripción a cursado", { x: bx + 1.1, y: by + 0.11, w: bw - 1.4, h: 0.28, fontSize: 10, color: MUTED, valign: "middle" });
  texto(s, "503", { x: bx + 0.4, y: by + 0.75, w: 2.4, h: 1.05, fontSize: 64, bold: true, color: CORAL, fontFace: HEAD, valign: "middle" });
  texto(s, [{ text: "Servicio no disponible", options: { bold: true, color: INK, breakLine: true } },
    { text: "Demasiados usuarios conectados. Intente más tarde.", options: { color: SLATE, fontSize: 13 } }],
    { x: bx + 0.4, y: by + 1.95, w: bw - 0.8, h: 0.8, fontSize: 17 });
  for (let i = 0; i < 8; i++) {
    const ang = i * Math.PI / 4, r = 0.32, cx = bx + bw - 0.9, cy = by + 1.27;
    s.addShape(pres.shapes.OVAL, { x: cx + r * Math.cos(ang) - 0.065, y: cy + r * Math.sin(ang) - 0.065, w: 0.13, h: 0.13,
      fill: { color: VIOLET, transparency: 10 + i * 11 }, line: { type: "none" }, objectName: "spinner" });
  }
  texto(s, "Recreación ilustrativa, no una captura real", { x: bx, y: by + bh + 0.08, w: bw, h: 0.25, fontSize: 10, color: MUTED, italic: true });
  // cifras del caso
  supuesto(s, bx, 5.25, 2.6);
  [["5.000", "alumnos a la vez a las 08:00", CORAL], ["< 100", "el resto del año", VIOLET]].forEach(([a, b, col], i) => {
    const x = bx + i * 2.6;
    texto(s, a, { x, y: 5.65, w: 2.4, h: 0.6, fontSize: 34, bold: true, color: col, fontFace: HEAD, valign: "middle" });
    texto(s, b, { x, y: 6.22, w: 2.4, h: 0.35, fontSize: 13, color: SLATE });
  });
  // demanda contra capacidad, día de inscripción
  const xr = bx + bw + 0.55, wr = W - ML - xr;
  texto(s, "Pedidos por segundo el día de inscripción", { x: xr, y: 1.75, w: wr, h: 0.4, fontSize: 17, bold: true, color: VIOLET });
  const horas = ["06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00"];
  const dem = [5, 60, 2000, 1300, 450, 200, 90, 60, 40];
  s.addChart(pres.charts.LINE, [
    { name: "Demanda", labels: horas, values: dem },
    { name: "Capacidad de un servidor dimensionado para el uso normal", labels: horas, values: horas.map(() => 400) },
  ], {
    x: xr - 0.1, y: 2.2, w: wr + 0.1, h: 3.55, chartColors: [CORAL, VIOLET], lineSize: 3, lineDataSymbol: "none",
    showLegend: true, legendPos: "t", legendFontSize: 12, legendFontFace: BODY, legendColor: SLATE,
    catAxisLabelColor: MUTED, valAxisLabelColor: MUTED, catAxisLabelFontSize: 11, valAxisLabelFontSize: 11,
    catAxisLabelFontFace: BODY, valAxisLabelFontFace: BODY, valAxisMinVal: 0, valAxisMaxVal: 2200, valAxisMajorUnit: 500,
    valAxisLabelFormatCode: "0", valGridLine: { color: "ECE8F5", size: 1 }, catGridLine: { style: "none" },
  });
  caja(s, xr, 5.9, wr, 0.62, LAV);
  texto(s, [{ text: "A las 08:00 la demanda supera 5 veces la capacidad: ", options: { bold: true, color: INK } },
    { text: "todo lo que no entra es un 503.", options: { color: CORAL, bold: true } }],
    { x: xr + 0.25, y: 5.9, w: wr - 0.5, h: 0.62, fontSize: 15, valign: "middle" });
}

// 3. El dilema
{
  const s = nueva("CONTENIDO", S1,
    "[Expositor 1] Con un servidor tradicional hay dos opciones y las dos son malas. Si lo dimensionás para el pico, pagás once meses de una máquina ociosa. Si lo dimensionás para el promedio, el día que importa se cae. Serverless propone una tercera: que la capacidad siga a la demanda.");
  encabezado(s, "EL CASO", "El dilema: ¿para cuántos alumnos compramos el servidor?");
  const cw = (CW - 2 * 0.4) / 3, y = 1.75, h = 4.0;
  const ops = [
    ["Para el pico", "Aguanta la inscripción, pero el resto del año está ocioso y lo pagás igual.", "ocioso", 5, 1, LAV, VIOLET],
    ["Para el promedio", "Barato todo el año, pero el día que importa se satura y se cae.", "saturado", 2, 2, LAV, VIOLET],
    ["Que siga a la demanda", "Capacidad cero cuando no hay nadie, miles de instancias en el pico.", "serverless", 0, 0, VIOLET, WHITE],
  ];
  ops.forEach(([t, d, tag, cap, uso, fill, col], i) => {
    const x = ML + i * (cw + 0.4);
    caja(s, x, y, cw, h, fill);
    circulo(s, x + 0.35, y + 0.35, ["A", "B", "C"][i], 0.55, i === 2 ? CORAL : VIOLET);
    texto(s, t, { x: x + 1.1, y: y + 0.35, w: cw - 1.4, h: 0.55, fontSize: 20, bold: true, color: col, fontFace: HEAD, valign: "middle" });
    // mini-diagrama: capacidad (cajas) vs demanda
    const bx = x + 0.4, by = y + 1.25;
    if (i < 2) {
      for (let k = 0; k < 5; k++) {
        const existe = k < cap, usada = k < uso;
        s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: bx + k * 0.52, y: by, w: 0.42, h: 0.42, rectRadius: 0.05,
          fill: { color: existe ? (usada ? VIOLET : WHITE) : LAV }, line: { color: existe ? VIOLET : CORAL, width: 1, dashType: existe ? "solid" : "dash" }, objectName: "capacidad" });
      }
      texto(s, i === 0 ? "4 de 5 servidores ociosos" : "faltan 3 servidores el día pico", { x: bx, y: by + 0.5, w: cw - 0.8, h: 0.35, fontSize: 13, italic: true, color: i === 0 ? SLATE : CORAL });
    } else {
      for (let k = 0; k < 5; k++) {
        s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: bx + k * 0.52, y: by, w: 0.42, h: 0.42, rectRadius: 0.05,
          fill: { color: k < 3 ? CORAL : VIOLET }, line: { color: k < 3 ? CORAL : LAV2, width: 1, dashType: k < 3 ? "solid" : "dash" }, objectName: "capacidad" });
      }
      texto(s, "existen sólo las instancias que hacen falta", { x: bx, y: by + 0.5, w: cw - 0.8, h: 0.35, fontSize: 13, italic: true, color: LAV2 });
    }
    texto(s, d, { x: x + 0.4, y: y + 2.3, w: cw - 0.8, h: 1.4, fontSize: 16, color: i === 2 ? WHITE : SLATE });
  });
  texto(s, [{ text: "Ese es el problema que resuelve serverless: ", options: { bold: true, color: VIOLET } },
    { text: "pagar por lo que se usa, cuando se usa.", options: { color: SLATE } }], { x: ML, y: 6.0, w: CW, h: 0.45, fontSize: 17 });
}

// 4. Qué es
{
  const s = nueva("CONTENIDO", S1,
    "[Expositor 1] Serverless no significa que no haya servidores: existen, pero los administra el proveedor, como el wireless no elimina los cables. La CNCF lo define con tres propiedades: no gestionás infraestructura, escala hasta cero y pagás por uso real. Y tiene dos mitades: FaaS, que es nuestro código, y BaaS, los servicios que consumimos. Ahora, ¿qué pasa por dentro el día de la inscripción? Le paso a mi compañero.");
  encabezado(s, "QUÉ ES", "No es «sin servidores»: es que no son tu problema");
  const props = [["Sin gestión de infraestructura", "No elegís máquina ni parcheás el sistema operativo."],
    ["Escala hasta cero", "De 0 a N instancias según la demanda, y de vuelta a 0."],
    ["Pago por uso real", "Se cobra por ejecución, no por servidor encendido."]];
  const lw = 5.6;
  props.forEach(([t, d], i) => {
    const y = 1.75 + i * 1.12;
    circulo(s, ML, y + 0.12, String(i + 1), 0.6);
    texto(s, [{ text: t, options: { bold: true, fontSize: 18, color: VIOLET, breakLine: true } }, { text: d, options: { fontSize: 15, color: SLATE } }],
      { x: ML + 0.85, y, w: lw - 0.85, h: 1.0 });
  });
  texto(s, "Definición: CNCF, Serverless Whitepaper. Si falta una de las tres, no es serverless.", { x: ML, y: 5.2, w: lw, h: 0.7, fontSize: 13, italic: true, color: MUTED });
  // diagrama FaaS + BaaS aplicado al caso
  const xr = ML + lw + 0.5, wr = W - ML - xr;
  caja(s, xr, 1.7, wr, 4.75, LAV);
  texto(s, "El caso, armado en serverless", { x: xr + 0.3, y: 1.85, w: wr - 0.6, h: 0.4, fontSize: 16, bold: true, color: VIOLET });
  const ax = xr + 0.25, fx = xr + 1.85, bx = xr + wr - 2.1;
  caja(s, ax, 3.4, 1.3, 0.8, WHITE, LAV2, "alumno");
  texto(s, "Alumno", { x: ax, y: 3.4, w: 1.3, h: 0.8, fontSize: 15, bold: true, align: "center", valign: "middle" });
  caja(s, fx, 3.3, 1.6, 1.0, CORAL, null, "faas");
  texto(s, [{ text: "inscribir()", options: { bold: true, breakLine: true } }, { text: "FaaS · tu código", options: { fontSize: 12 } }],
    { x: fx, y: 3.3, w: 1.6, h: 1.0, fontSize: 15, color: WHITE, align: "center", valign: "middle" });
  flecha(s, ax + 1.32, 3.8, fx - 0.05, 3.8);
  const baas = [["Login", 2.5], ["Base de datos", 3.55], ["Cola de mails", 4.6]];
  baas.forEach(([t, y]) => {
    caja(s, bx, y, 1.85, 0.75, VIOLET, null, "baas");
    texto(s, t, { x: bx, y, w: 1.85, h: 0.75, fontSize: 14, bold: true, color: WHITE, align: "center", valign: "middle" });
    flecha(s, fx + 1.63, 3.8, bx - 0.05, y + 0.375);
  });
  texto(s, "BaaS · servicios que consumís", { x: bx - 0.3, y: 5.5, w: 2.45, h: 0.35, fontSize: 12, italic: true, color: SLATE, align: "center" });
  texto(s, "La mayor parte del sistema es BaaS; tu función es el pegamento.", { x: xr + 0.3, y: 5.9, w: wr - 0.6, h: 0.4, fontSize: 13, color: SLATE });
}

// ===================== BLOQUE 2 =====================
pres.addSection({ title: S2 });
capitulo(S2, "02", "08:00 del día de inscripción: 5.000 alumnos apretan F5",
  "¿Qué pasa por dentro de la plataforma en ese momento?",
  "[Expositor 2] Son las ocho de la mañana del día de inscripción y entran cinco mil alumnos al mismo tiempo. Veamos qué hace la plataforma por dentro con cada uno de esos pedidos.");

// 6. Ciclo de vida
{
  const s = nueva("CONTENIDO", S2,
    "[Expositor 2] Cada clic en «Inscribirme» es un evento que invoca la función. Si no hay un entorno listo, la plataforma hace el INIT: crea una microVM, baja el código, arranca el runtime y corre la inicialización. Después ejecuta la función y congela el entorno, que se reutiliza si llega otro pedido. Como dos pedidos pueden caer en entornos distintos, el estado de la inscripción tiene que ir a la base, nunca a memoria.");
  encabezado(s, "QUÉ PASA POR DENTRO", "Cada clic en «Inscribirme» es un evento");
  const fases = [
    ["CLIC", "POST /inscripcion llega al API Gateway", LAV, INK],
    ["INIT", "Crea la microVM, baja el código, arranca el runtime y conecta a la base", CORAL, WHITE],
    ["INVOKE", "Corre inscribir() con los datos del alumno", LAV, INK],
    ["FREEZE", "Congela el entorno; si no hay pedidos en 5–15 min, se apaga", LAV, INK],
  ];
  const bw = 2.6, gap = (CW - 4 * bw) / 3, y = 1.75, h = 2.0;
  fases.forEach(([t, d, f, col], i) => {
    const x = ML + i * (bw + gap);
    caja(s, x, y, bw, h, f, null, "fase");
    texto(s, [{ text: t, options: { bold: true, fontSize: 17, fontFace: HEAD, breakLine: true } }, { text: d, options: { fontSize: 14 } }],
      { x: x + 0.2, y: y + 0.2, w: bw - 0.4, h: h - 0.35, color: col, paraSpaceAfter: 5 });
    if (i < 3) flecha(s, x + bw + 0.06, y + h / 2, x + bw + gap - 0.06, y + h / 2);
  });
  texto(s, "sólo si no hay un entorno listo", { x: ML + bw + gap, y: y + h + 0.05, w: bw, h: 0.3, fontSize: 12, italic: true, color: CORAL, align: "center" });
  const xInv = ML + 2 * (bw + gap) + bw / 2, xFrz = ML + 3 * (bw + gap) + bw / 2, yb = y + h, yl = yb + 0.45;
  linea(s, xFrz, yb, xFrz, yl); linea(s, xFrz, yl, xInv, yl); flecha(s, xInv, yl, xInv, yb + 0.03);
  texto(s, "el próximo alumno reusa el entorno", { x: xInv + 0.1, y: yl + 0.05, w: xFrz - xInv - 0.2, h: 0.3, fontSize: 12, italic: true, color: MUTED, align: "center" });
  caja(s, ML, 4.75, CW, 1.6, VIOLET, null, "stateless");
  circulo(s, ML + 0.35, 5.27, "!", 0.55, CORAL);
  texto(s, [{ text: "Stateless por contrato. ", options: { bold: true, color: WHITE } },
    { text: "Dos pedidos del mismo alumno pueden caer en entornos distintos: la inscripción se guarda en la base, nunca en la memoria de la función.", options: { color: LAV2 } }],
    { x: ML + 1.15, y: 4.75, w: CW - 1.5, h: 1.6, fontSize: 17, valign: "middle" });
}

// 7. Concurrencia + cold start
{
  const s = nueva("CONTENIDO", S2,
    "[Expositor 2] En Lambda cada entorno atiende un pedido a la vez, así que la cantidad de entornos sale de multiplicar pedidos por segundo por la duración. Con nuestro supuesto de dos mil pedidos por segundo y trescientos milisegundos, son seiscientos entornos, debajo del límite por defecto de mil. Pero si la función tardara un segundo, serían dos mil y la plataforma empezaría a rechazar pedidos. Además, cada entorno nuevo paga un cold start, que va de menos de cien milisegundos en Go o Rust a segundos en Java sin optimizar.");
  encabezado(s, "QUÉ PASA POR DENTRO", "¿Cuántos entornos hacen falta a las 08:00?");
  const lw = 6.4;
  caja(s, ML, 1.75, lw, 1.15, NIGHT, null, "formula");
  texto(s, "entornos = pedidos/s × duración", { x: ML + 0.3, y: 1.75, w: lw - 0.6, h: 1.15, fontSize: 22, bold: true, color: WHITE, fontFace: "Courier New", valign: "middle" });
  const filas = [
    ["2.000/s × 0,3 s", "600", "entra en el límite por defecto (1.000)", VIOLET],
    ["2.000/s × 1,0 s", "2.000", "supera el límite: la plataforma rechaza pedidos", CORAL],
  ];
  filas.forEach(([f, r, c, col], i) => {
    const y = 3.15 + i * 1.25;
    caja(s, ML, y, lw, 1.05, LAV, null, "escenario");
    texto(s, f, { x: ML + 0.3, y, w: 2.6, h: 1.05, fontSize: 17, fontFace: "Courier New", valign: "middle" });
    texto(s, r, { x: ML + 2.8, y, w: 1.5, h: 1.05, fontSize: 34, bold: true, color: col, fontFace: HEAD, valign: "middle", align: "right" });
    texto(s, c, { x: ML + 4.5, y, w: lw - 4.7, h: 1.05, fontSize: 14, color: SLATE, valign: "middle" });
  });
  supuesto(s, ML, 5.75, 2.6);
  texto(s, "2.000 pedidos/s y 300 ms son del ejemplo. El límite de 1.000 por cuenta y región es de AWS.", { x: ML + 2.8, y: 5.7, w: lw - 2.8, h: 0.6, fontSize: 12, color: MUTED });
  // cold start
  const xr = ML + lw + 0.5, wr = W - ML - xr;
  texto(s, "Cada entorno nuevo paga un cold start", { x: xr, y: 1.75, w: wr, h: 0.4, fontSize: 17, bold: true, color: VIOLET });
  const x0 = xr + 1.9, aw = wr - 2.9, sc = aw / 500, y0 = 2.45, rh = 0.68;
  const rangos = [["Go / Rust", 10, 100, "< 100 ms"], ["Java + SnapStart", 90, 140, "90–140 ms"], ["Python", 200, 400, "200–400 ms"], ["Java sin optimizar", 300, 500, "segundos", true]];
  for (let t = 0; t <= 500; t += 250) {
    s.addShape(pres.shapes.LINE, { x: x0 + t * sc, y: y0 - 0.1, w: 0.001, h: rangos.length * rh, line: { color: LAV2, width: 0.75 } });
    texto(s, t + " ms", { x: x0 + t * sc - 0.4, y: y0 + rangos.length * rh - 0.05, w: 0.8, h: 0.3, fontSize: 11, color: MUTED, align: "center" });
  }
  rangos.forEach(([l, a, b, v, sale], i) => {
    const y = y0 + i * rh;
    texto(s, l, { x: xr, y, w: 1.8, h: 0.45, fontSize: 13, align: "right", valign: "middle" });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x0 + a * sc, y: y + 0.08, w: (b - a) * sc, h: 0.3, rectRadius: 0.05, fill: { color: sale ? CORAL : VIOLET }, line: { type: "none" }, objectName: "rango" });
    if (sale) flecha(s, x0 + b * sc, y + 0.23, x0 + aw + 0.25, y + 0.23, CORAL);
    texto(s, v, { x: sale ? x0 + aw + 0.3 : x0 + b * sc + 0.08, y, w: 1.0, h: 0.45, fontSize: 12, bold: true, color: SLATE, valign: "middle" });
  });
  texto(s, "Mitigación: SnapStart restaura una foto de un entorno ya inicializado; Provisioned Concurrency los deja precalentados, pero se paga por hora.",
    { x: xr, y: 5.45, w: wr, h: 0.9, fontSize: 14, color: SLATE });
  fuente(s, "Tiempos de cold start: órdenes de magnitud reportados en 2026 (fuentes secundarias).");
}

// 8. Firecracker
{
  const s = nueva("CONTENIDO", S2,
    "[Expositor 2] Esos seiscientos entornos conviven en máquinas físicas con código de miles de otros clientes. Amazon los aísla con Firecracker, un monitor de máquinas virtuales en Rust que levanta una microVM en menos de ciento veinticinco milisegundos con unos cinco megas de memoria extra. Cloudflare hace lo contrario: miles de isolates de V8 dentro de un solo proceso, casi sin cold start pero sólo para JavaScript o WebAssembly. Con esto, le paso a mi compañero para hablar de plata.");
  encabezado(s, "QUÉ PASA POR DENTRO", "600 microVMs al lado del código de otros clientes");
  // servidor físico con microVMs
  caja(s, ML, 1.75, 7.2, 3.9, LAV, LAV2, "servidor");
  texto(s, "un servidor físico de AWS", { x: ML + 0.3, y: 1.85, w: 5, h: 0.35, fontSize: 13, italic: true, color: MUTED });
  for (let r = 0; r < 3; r++) for (let c = 0; c < 6; c++) {
    const nuestra = (r * 6 + c) % 3 === 0;
    const x = ML + 0.35 + c * 1.12, y = 2.35 + r * 1.05;
    caja(s, x, y, 0.95, 0.85, nuestra ? CORAL : WHITE, nuestra ? null : LAV2, "microvm");
    texto(s, nuestra ? "inscribir()" : "otro cliente", { x, y, w: 0.95, h: 0.85, fontSize: 11, bold: nuestra, color: nuestra ? WHITE : MUTED, align: "center", valign: "middle" });
  }
  texto(s, "cada caja es una microVM con su propio kernel: aislamiento por hardware (KVM)", { x: ML, y: 5.8, w: 7.2, h: 0.4, fontSize: 14, color: SLATE });
  const xr = ML + 7.7, wr = W - ML - xr;
  [["< 125 ms", "en levantar una microVM"], ["~5 MiB", "de memoria extra por microVM"]].forEach(([a, b], i) => {
    texto(s, a, { x: xr, y: 1.7 + i * 1.35, w: wr, h: 0.8, fontSize: 40, bold: true, color: VIOLET, fontFace: HEAD, valign: "middle" });
    texto(s, b, { x: xr, y: 2.5 + i * 1.35, w: wr, h: 0.4, fontSize: 15, color: SLATE });
  });
  caja(s, xr, 4.5, wr, 1.75, NIGHT, null, "v8");
  texto(s, [{ text: "La alternativa: isolates de V8", options: { bold: true, color: WHITE, breakLine: true } },
    { text: "Cloudflare corre miles de funciones en un solo proceso. Casi sin cold start, pero sólo JS o WASM.", options: { color: LAV2, fontSize: 14 } }],
    { x: xr + 0.25, y: 4.6, w: wr - 0.5, h: 1.55, fontSize: 15, valign: "middle", paraSpaceAfter: 4 });
  fuente(s, "Firecracker: monitor de máquinas virtuales en Rust, open source; base de Lambda y Fargate.");
}

// ===================== BLOQUE 3 =====================
pres.addSection({ title: S3 });
capitulo(S3, "03", "¿Cuánto cuesta? ¿Y qué le pasa a la base de datos?",
  "La parte que decide si esto conviene, y la que más tiene que ver con la materia.",
  "[Expositor 3] Ya sabemos que el sistema aguanta el pico. Ahora vienen las dos preguntas que deciden si conviene: cuánto cuesta y qué le pasa a la base de datos cuando seiscientas funciones le pegan a la vez.");

// 10. Costos
{
  const s = nueva("CONTENIDO", S3,
    "[Expositor 3] Lambda cobra veinte centavos de dólar por millón de pedidos más el tiempo de ejecución, medido en gigabyte-segundo, al milisegundo. Hay una capa gratuita mensual de un millón de pedidos y cuatrocientos mil gigabyte-segundo. En nuestro supuesto, el día de inscripción son doscientos mil pedidos de trescientos milisegundos: treinta mil gigabyte-segundo, que entran enteros en la capa gratuita. Un servidor chico encendido todo el año cuesta unos ciento ochenta dólares.");
  encabezado(s, "COSTOS", "Se paga por milisegundo: el día pico entra en la capa gratuita");
  const lw = 6.0;
  caja(s, ML, 1.75, lw, 1.25, NIGHT, null, "formula");
  texto(s, [{ text: "costo = pedidos × USD 0,20 / millón", options: { breakLine: true } }, { text: "      + GB-s × USD 0,0000167", options: {} }],
    { x: ML + 0.3, y: 1.75, w: lw - 0.6, h: 1.25, fontFace: "Courier New", fontSize: 16, bold: true, color: WHITE, valign: "middle" });
  const items = [["GB-segundo", "memoria configurada × tiempo de ejecución"], ["Capa gratuita", "1 M de pedidos + 400.000 GB-s por mes"], ["Sin tráfico", "el costo de cómputo es cero"]];
  items.forEach(([a, b], i) => {
    const y = 3.25 + i * 0.85;
    circulo(s, ML, y + 0.05, String(i + 1), 0.5, VIOLET);
    texto(s, [{ text: a + ": ", options: { bold: true, color: VIOLET } }, { text: b, options: { color: SLATE } }], { x: ML + 0.75, y, w: lw - 0.75, h: 0.6, fontSize: 15, valign: "middle" });
  });
  fuente(s, "Precios oficiales de AWS Lambda (US East, x86) y EC2 t3.small ≈ USD 15/mes, según el informe. Cuenta del caso: cálculo propio.");
  // cuenta del caso
  const xr = ML + lw + 0.5, wr = W - ML - xr;
  caja(s, xr, 1.75, wr, 4.6, LAV, null, "cuenta");
  supuesto(s, xr + 0.3, 1.95, 2.6);
  texto(s, "El día de inscripción", { x: xr + 0.3, y: 2.4, w: wr - 0.6, h: 0.4, fontSize: 17, bold: true, color: VIOLET });
  texto(s, [
    { text: "200.000 pedidos × 0,3 s × 0,5 GB", options: { breakLine: true } },
    { text: "= 30.000 GB-s", options: { bold: true, breakLine: true } },
    { text: "< 400.000 GB-s gratis por mes", options: { color: SLATE } },
  ], { x: xr + 0.3, y: 2.9, w: wr - 0.6, h: 1.2, fontSize: 15, fontFace: "Courier New", paraSpaceAfter: 4 });
  const cw2 = (wr - 0.9) / 2;
  [["≈ USD 0", "cómputo en Lambda", CORAL], ["≈ USD 180", "t3.small todo el año", VIOLET]].forEach(([a, b, col], i) => {
    const x = xr + 0.3 + i * (cw2 + 0.3);
    caja(s, x, 4.35, cw2, 1.75, WHITE, LAV2, "resultado");
    texto(s, a, { x: x + 0.15, y: 4.5, w: cw2 - 0.3, h: 0.85, fontSize: 30, bold: true, color: col, fontFace: HEAD, valign: "middle", align: "center" });
    texto(s, b, { x: x + 0.15, y: 5.4, w: cw2 - 0.3, h: 0.5, fontSize: 14, color: SLATE, align: "center" });
  });
}

// 11. Punto de cruce (gráfico nativo)
{
  const s = nueva("CONTENIDO", S3,
    "[Expositor 3] Pero ojo: serverless no es siempre más barato. Normalizado por procesador, el vCPU-hora de Lambda cuesta unas tres veces lo que una instancia equivalente. Las líneas se cruzan cerca del treinta y cuatro por ciento de uso: debajo gana serverless, arriba conviene un servidor. El SysAcad está casi todo el año cerca del cero, así que está bien del lado izquierdo.");
  encabezado(s, "COSTOS", "Gana mientras el uso esté debajo de un tercio");
  const us = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
  s.addChart(pres.charts.LINE, [
    { name: "Lambda", labels: us.map(u => u + " %"), values: us.map(u => +(0.106 * u / 100).toFixed(4)) },
    { name: "Servidor encendido 24/7 (EC2)", labels: us.map(u => u + " %"), values: us.map(() => 0.036) },
  ], {
    x: ML, y: 1.65, w: 7.6, h: 4.85, chartColors: [CORAL, VIOLET], lineSize: 3, lineDataSymbol: "none",
    showLegend: true, legendPos: "t", legendFontSize: 13, legendFontFace: BODY, legendColor: SLATE,
    showCatAxisTitle: true, catAxisTitle: "utilización", catAxisTitleFontSize: 12, catAxisTitleColor: MUTED, catAxisTitleFontFace: BODY,
    showValAxisTitle: true, valAxisTitle: "USD por vCPU-hora", valAxisTitleFontSize: 12, valAxisTitleColor: MUTED, valAxisTitleFontFace: BODY,
    catAxisLabelColor: MUTED, valAxisLabelColor: MUTED, catAxisLabelFontSize: 12, valAxisLabelFontSize: 12, catAxisLabelFontFace: BODY, valAxisLabelFontFace: BODY,
    valAxisLabelFormatCode: "0.00", valAxisMinVal: 0, valAxisMaxVal: 0.12, valAxisMajorUnit: 0.02,
    valGridLine: { color: "ECE8F5", size: 1 }, catGridLine: { style: "none" },
  });
  const xr = ML + 8.05, wr = W - ML - xr;
  texto(s, "≈ 34 %", { x: xr, y: 1.75, w: wr, h: 0.9, fontSize: 48, bold: true, color: CORAL, fontFace: HEAD, valign: "middle" });
  texto(s, "de uso: ahí se cruzan las líneas", { x: xr, y: 2.65, w: wr, h: 0.4, fontSize: 15, color: SLATE });
  caja(s, xr, 3.35, wr, 2.95, LAV, null, "lectura");
  texto(s, [
    { text: "~3×", options: { bold: true, color: VIOLET, fontSize: 26, fontFace: HEAD, breakLine: true } },
    { text: "cuesta el vCPU-hora de Lambda frente a una instancia.", options: { color: SLATE, breakLine: true } },
    { text: " ", options: { fontSize: 8, breakLine: true } },
    { text: "SysAcad: ", options: { bold: true, color: VIOLET } },
    { text: "casi todo el año cerca de 0 % de uso. Del lado que gana serverless.", options: { color: SLATE } },
  ], { x: xr + 0.3, y: 3.5, w: wr - 0.6, h: 2.7, fontSize: 15 });
  fuente(s, "Cálculo propio con precios oficiales: Lambda ≈ USD 0,106 / vCPU-h; EC2 c7g.large ≈ USD 0,036 / vCPU-h.");
}

// 12. Base de datos
{
  const s = nueva("CONTENIDO", S3,
    "[Expositor 3] Y acá está el problema que más tiene que ver con la materia. Si cada uno de los seiscientos entornos abre su propia conexión a Postgres, la base se cae, porque soporta cientos de conexiones, no miles. La solución es un pooler, como RDS Proxy o PgBouncer, que reutiliza pocas conexiones para muchas funciones, o una base que se consulte por HTTP. Y las bases serverless, como Neon o Aurora Serverless, separan cómputo de almacenamiento para poder apagar el cómputo sin perder los datos. Le paso a mi compañero.");
  encabezado(s, "BASE DE DATOS", "El sistema aguantó el pico… y se cayó la base");
  const lw = 7.3;
  caja(s, ML, 1.75, lw, 4.6, LAV, null, "problema");
  // sin pooler (arriba) vs con pooler (abajo)
  const fx = ML + 0.35;
  texto(s, "Sin pooler: 600 conexiones", { x: fx, y: 1.9, w: 4, h: 0.35, fontSize: 14, bold: true, color: CORAL });
  texto(s, "Con pooler: pocas conexiones reutilizadas", { x: fx, y: 4.1, w: 5, h: 0.35, fontSize: 14, bold: true, color: VIOLET });
  const dbx = ML + lw - 1.55;
  [[2.35, false], [4.55, true]].forEach(([y0, pool]) => {
    for (let i = 0; i < 4; i++) {
      const y = y0 + i * 0.36;
      caja(s, fx, y, 0.85, 0.28, CORAL, null, "funcion");
      texto(s, "λ", { x: fx, y, w: 0.85, h: 0.28, fontSize: 12, bold: true, color: WHITE, align: "center", valign: "middle" });
      flecha(s, fx + 0.9, y + 0.14, pool ? fx + 2.55 : dbx - 0.05, pool ? y0 + 0.66 : y0 + 0.66, pool ? MUTED : CORAL);
    }
    if (pool) {
      caja(s, fx + 2.6, y0 + 0.3, 1.5, 0.72, VIOLET, null, "pooler");
      texto(s, "pooler", { x: fx + 2.6, y: y0 + 0.3, w: 1.5, h: 0.72, fontSize: 14, bold: true, color: WHITE, align: "center", valign: "middle" });
      flecha(s, fx + 4.15, y0 + 0.66, dbx - 0.05, y0 + 0.66, VIOLET);
    }
    s.addShape(pres.shapes.CAN, { x: dbx, y: y0 + 0.1, w: 1.1, h: 1.05, fill: { color: pool ? VIOLET : CORAL }, line: { type: "none" }, objectName: "base" });
    texto(s, pool ? "OK" : "cae", { x: dbx, y: y0 + 0.35, w: 1.1, h: 0.75, fontSize: 14, bold: true, color: WHITE, align: "center", valign: "middle" });
  });
  texto(s, "Postgres soporta cientos de conexiones, no miles.", { x: fx, y: 3.75, w: lw - 0.7, h: 0.3, fontSize: 13, italic: true, color: SLATE });
  texto(s, "Pooler: RDS Proxy o PgBouncer. Si no, bases con API HTTP.", { x: fx, y: 5.95, w: lw - 0.7, h: 0.35, fontSize: 13, color: SLATE });
  // separar cómputo y almacenamiento
  const xr = ML + lw + 0.5, wr = W - ML - xr;
  texto(s, "Bases serverless: separar cómputo de almacenamiento", { x: xr, y: 1.75, w: wr, h: 0.8, fontSize: 17, bold: true, color: VIOLET });
  for (let i = 0; i < 3; i++) {
    const on = i === 1, x = xr + i * (wr / 3);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 0.05, y: 2.75, w: wr / 3 - 0.2, h: 0.7, rectRadius: 0.08,
      fill: { color: on ? CORAL : WHITE }, line: { color: on ? CORAL : LAV2, width: 1, dashType: on ? "solid" : "dash" }, objectName: "nodo" });
    texto(s, on ? "activo" : "apagado", { x: x + 0.05, y: 2.75, w: wr / 3 - 0.2, h: 0.7, fontSize: 12, bold: on, color: on ? WHITE : MUTED, align: "center", valign: "middle" });
  }
  flecha(s, xr + wr / 2 - 0.05, 3.5, xr + wr / 2 - 0.05, 3.9);
  caja(s, xr, 3.95, wr - 0.1, 0.75, NIGHT, null, "storage");
  texto(s, "almacenamiento persistente", { x: xr, y: 3.95, w: wr - 0.1, h: 0.75, fontSize: 14, bold: true, color: WHITE, align: "center", valign: "middle" });
  texto(s, "Neon, Aurora Serverless v2, DynamoDB on-demand: el cómputo escala a cero y los datos quedan.", { x: xr, y: 4.95, w: wr - 0.1, h: 1.3, fontSize: 14, color: SLATE });
}

// ===================== BLOQUE 4 =====================
pres.addSection({ title: S4 });
capitulo(S4, "04", "¿Y si el sistema se usara todo el día?",
  "Cuándo serverless deja de ser la respuesta.",
  "[Expositor 4] Para nuestro caso, serverless encaja muy bien. Pero si el sistema se usara todo el día, todos los días, la historia sería otra. Veamos cuándo no conviene.");

// 14. Cuándo no + Prime Video
{
  const s = nueva("CONTENIDO", S4,
    "[Expositor 4] Serverless encaja con cargas espigadas, disparadas por eventos y sin estado, como el SysAcad en inscripción. No encaja con cargas constantes, latencia crítica o cadenas largas de funciones. El ejemplo más famoso lo dio Amazon: en 2023 el equipo de Prime Video sacó un sistema de monitoreo de serverless, lo pasó a un solo proceso en contenedores y bajó el costo un noventa por ciento, porque lo caro era mover datos entre funciones, no procesarlos.");
  encabezado(s, "CUÁNDO NO", "Prime Video: −90 % de costo saliendo de serverless");
  const hw = 3.85;
  [["Encaja", ["Carga espigada", "Disparada por eventos", "Sin estado"], VIOLET, "✓"],
   ["No encaja", ["Carga constante", "Latencia crítica", "Funciones encadenadas"], CORAL, "✕"]].forEach(([t, its, col, ico], i) => {
    const y = 1.75 + i * 2.35;
    caja(s, ML, y, hw, 2.15, LAV, null, "encaje");
    circulo(s, ML + 0.3, y + 0.28, ico, 0.5, col);
    texto(s, t, { x: ML + 0.95, y: y + 0.28, w: hw - 1.2, h: 0.5, fontSize: 19, bold: true, color: col, valign: "middle", fontFace: HEAD });
    texto(s, its.map((x, j) => ({ text: x, options: { bullet: true, breakLine: j < its.length - 1 } })), { x: ML + 0.35, y: y + 0.95, w: hw - 0.6, h: 1.1, fontSize: 15, color: SLATE, paraSpaceAfter: 3 });
  });
  const xr = ML + hw + 0.5, wr = W - ML - xr;
  caja(s, xr, 1.75, wr, 4.5, NIGHT, null, "primevideo");
  texto(s, "−90 %", { x: xr + 0.4, y: 1.95, w: 3.5, h: 1.2, fontSize: 60, bold: true, color: CORAL, fontFace: HEAD, valign: "middle" });
  texto(s, "Prime Video, monitoreo de calidad de streams (Amazon, 2023)", { x: xr + 0.4, y: 3.15, w: wr - 0.8, h: 0.4, fontSize: 14, color: LAV2 });
  const bw = (wr - 1.5) / 2, by = 3.75;
  [["Antes", "Funciones encadenadas; los datos viajaban entre etapas por la red y S3"], ["Después", "Un solo proceso en contenedores (ECS), todo en memoria"]].forEach(([t, d], i) => {
    const x = xr + 0.4 + i * (bw + 0.7);
    caja(s, x, by, bw, 1.55, i ? VIOLET : "2C2058", null, "antesdespues");
    texto(s, [{ text: t, options: { bold: true, color: WHITE, breakLine: true } }, { text: d, options: { color: LAV2, fontSize: 14 } }],
      { x: x + 0.2, y: by + 0.15, w: bw - 0.4, h: 1.3, fontSize: 16, paraSpaceAfter: 3 });
  });
  flecha(s, xr + 0.4 + bw + 0.1, by + 0.78, xr + 0.4 + bw + 0.6, by + 0.78, CORAL);
  texto(s, [{ text: "Lección: ", options: { bold: true, color: CORAL } }, { text: "cuando comunicar cuesta más que computar, hay que juntar los componentes.", options: { color: WHITE } }],
    { x: xr + 0.4, y: 5.5, w: wr - 0.8, h: 0.6, fontSize: 15, valign: "middle" });
}

// 15. 2026
{
  const s = nueva("CONTENIDO", S4,
    "[Expositor 4] La propia industria lo reconoce. En 2026 Amazon lanzó Lambda Managed Instances, funciones que corren sobre servidores dedicados para cargas estables, y anunció microVMs que conservan estado hasta ocho horas. Además la inferencia de IA se está llevando al edge, y dos de cada tres empresas que usan funciones también usan contenedores. El futuro es híbrido.");
  encabezado(s, "HACIA DÓNDE VA", "2026: el serverless «puro» se flexibiliza");
  const items = [
    ["Lambda Managed Instances", "Funciones sobre EC2 para cargas estables: AWS admite el punto de cruce."],
    ["Lambda MicroVMs", "Sesiones de hasta 8 h con estado (anunciado en julio de 2026)."],
    ["IA en el edge", "Inferencia cerca del usuario, en 300+ datacenters."],
    ["Híbrido", "66 % de quienes usan funciones también usan contenedores."],
  ];
  // línea de tiempo horizontal
  const bw = 2.75, y = 3.0, x0 = ML + bw / 2, x1 = W - ML - bw / 2, step = (x1 - x0) / (items.length - 1);
  linea(s, x0, y, x1, y, LAV2);
  items.forEach(([t, d], i) => {
    const cx = x0 + i * step;
    circulo(s, cx - 0.3, y - 0.3, String(i + 1), 0.6, i % 2 ? VIOLET : CORAL);
    const bx = cx - bw / 2;
    texto(s, t, { x: bx, y: y + 0.55, w: bw, h: 0.75, fontSize: 18, bold: true, color: VIOLET, align: "center", fontFace: HEAD, valign: "middle" });
    texto(s, d, { x: bx, y: y + 1.35, w: bw, h: 1.3, fontSize: 15, color: SLATE, align: "center" });
  });
  texto(s, "Cada carga va donde le conviene.", { x: ML, y: 1.75, w: CW, h: 0.6, fontSize: 20, italic: true, color: CORAL, fontFace: HEAD });
  fuente(s, "Fuentes: AWS (2026); Datadog, State of Serverless (2025); Cloudflare.");
}

// 16. Cierre: vuelta al caso
{
  const s = nueva("OSCURA", S4,
    "[Expositor 4] Volvamos al SysAcad. Si estuviera armado así, aguantaría el pico, costaría casi cero el resto del año y lo único que habría que cuidar es la base, con un pooler. Ese es el criterio general: serverless es un trade-off que se elige por encaje con el problema, no por moda. Gracias, ¿preguntas?");
  texto(s, "VOLVIENDO AL CASO", { x: ML, y: 0.9, w: 8, h: 0.4, fontSize: 13, bold: true, color: CORAL, charSpacing: 2 });
  texto(s, "El SysAcad, en serverless", { x: ML, y: 1.35, w: 8.2, h: 0.8, fontSize: 30, bold: true, color: WHITE, fontFace: HEAD, valign: "middle" });
  const ideas = [["Aguanta el pico", "escala de 0 a cientos de entornos sin comprar nada."],
    ["Cuesta casi cero", "el resto del año, porque el uso está muy debajo de un tercio."],
    ["Cuidá la base", "con un pooler o una base serverless."]];
  ideas.forEach(([a, b], i) => {
    const y = 2.55 + i * 1.05;
    circulo(s, ML, y + 0.1, String(i + 1), 0.6);
    texto(s, [{ text: a + ": ", options: { bold: true, color: WHITE } }, { text: b, options: { color: LAV2 } }], { x: ML + 0.95, y, w: 7.2, h: 0.8, fontSize: 19, valign: "middle" });
  });
  texto(s, "Es un trade-off: se elige por encaje con el problema, no por moda.", { x: ML, y: 5.8, w: 8.2, h: 0.5, fontSize: 17, italic: true, color: CORAL, fontFace: HEAD });
  texto(s, "¿Preguntas?", { x: 9.1, y: 2.6, w: 3.7, h: 1.2, fontSize: 40, bold: true, color: CORAL, fontFace: HEAD, valign: "middle" });
  texto(s, "Gracias", { x: 9.1, y: 3.8, w: 3.7, h: 0.6, fontSize: 22, color: LAV2, fontFace: HEAD });
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  console.log("ok:", OUT);
})();
