// Presentacion de la defensa de la Etapa 4 de ASI (Cuadra).
//
//   node scripts/asi/pptx-etapa4/build.js [salida.pptx]
//
// El contenido de las laminas transcribe materias/ASI/entregables/etapa4/etapa4.md:
// si el documento cambia, este archivo se actualiza a mano. Las notas del orador, en
// cambio, se leen del guion (etapa4-guion.md), una por "### Lamina N".
const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");

const RAIZ = path.resolve(__dirname, "..", "..", "..");
const DIR = path.join(RAIZ, "materias", "ASI", "entregables", "etapa4");
const OUT = process.argv[2] || path.join(DIR, "etapa4-presentacion.pptx");
const GUION = path.join(DIR, "etapa4-guion.md");

// ---- paleta: el azul de los entregables del grupo + ambar de senal de obra ----
const NAVY = "15406B";
const DEEP = "0F2F50";
const BLOCK = "1C4E7E";
const ICE = "DCE9F7";
const PAPER = "F4F8FC";
const AMBER = "E8A33D";
const AMBER_SOFT = "FBEFD9";
const INK = "22313F";
const MUTED = "4C6480";
const LINE = "C9D9EA";
const WHITE = "FFFFFF";

const F = "Calibri";
const W = 13.333, H = 7.5;
const ML = 0.65;
const CW = W - 2 * ML;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.theme = { headFontFace: F, bodyFontFace: F };
pres.author = "Grupo 310 - Comision 403";
pres.title = "Cuadra - ASI TP Integrador Etapa 4";

// ============ notas del orador, desde el guion ============
function notasDelGuion() {
  const notas = {};
  if (!fs.existsSync(GUION)) return notas;
  const txt = fs.readFileSync(GUION, "utf8");
  let orador = "";
  for (const bloque of txt.split(/^## /m).slice(1)) {
    const cab = bloque.split("\n")[0];
    if (/^(Reloj|Preguntas)/.test(cab)) continue;
    orador = cab.split("·")[0].trim();
    for (const lam of bloque.split(/^### /m).slice(1)) {
      const m = lam.match(/^Lámina (\d+) — ([^\n]+)/);
      if (!m) continue;
      const cuerpo = lam.split("\n").slice(1).join("\n")
        .split(/^---$/m)[0]
        .replace(/\*\*/g, "").replace(/\*/g, "")
        .replace(/^> ?/gm, "")
        .replace(/\n{3,}/g, "\n\n")
        .replace(/([^\n])\n(?!\n)/g, "$1 ") // une los renglones cortados del .md
        .trim();
      notas[m[1]] = `${orador} — ${m[2]}\n\n${cuerpo}`;
    }
  }
  return notas;
}
const NOTAS = notasDelGuion();

// ============ helpers ============
function txt(s, t, o) {
  s.addText(t, Object.assign({
    isTextBox: true, margin: 0, fontFace: F, fontSize: 15, color: INK, valign: "top",
  }, o));
}

function card(s, o) {
  s.addShape(pres.ShapeType.roundRect, {
    x: o.x, y: o.y, w: o.w, h: o.h, rectRadius: o.r || 0.08,
    fill: { color: o.fill || PAPER }, line: { color: o.line || LINE, width: o.lw || 1 },
  });
}

// motivo visual: la "manzana" -- un cuadrado redondeado con numero o sigla
function manzana(s, label, o) {
  const d = o.d || 0.56;
  s.addShape(pres.ShapeType.roundRect, {
    x: o.x, y: o.y, w: d, h: d, rectRadius: 0.1,
    fill: { color: o.fill || NAVY }, line: { color: o.fill || NAVY, width: 0 },
  });
  txt(s, label, {
    x: o.x, y: o.y, w: d, h: d, fontSize: o.fs || (label.length > 2 ? 14 : 18),
    bold: true, color: o.color || WHITE, align: "center", valign: "middle",
  });
}

// cabecera de lamina de contenido: manzana con el punto del entregable + titulo
function head(s, n, punto, titulo, bajada) {
  s.background = { color: WHITE };
  manzana(s, punto, { x: ML, y: 0.45, d: 0.62 });
  txt(s, titulo, {
    x: ML + 0.86, y: 0.42, w: CW - 0.86, h: 0.68, fontSize: 32, bold: true,
    color: NAVY, valign: "middle",
  });
  if (bajada) {
    txt(s, bajada, {
      x: ML + 0.86, y: 1.12, w: CW - 0.86, h: 0.5, fontSize: 15, color: MUTED,
    });
  }
  pie(s, n);
  if (NOTAS[n]) s.addNotes(NOTAS[n]);
}

function pie(s, n, oscuro) {
  txt(s, "Cuadra  ·  ASI 2026  ·  Grupo 310", {
    x: ML, y: 7.05, w: 6, h: 0.25, fontSize: 10, color: oscuro ? "8FB6DA" : "8A9BB0",
  });
  txt(s, String(n), {
    x: W - ML - 1, y: 7.05, w: 1, h: 0.25, fontSize: 10, align: "right",
    color: oscuro ? "8FB6DA" : "8A9BB0",
  });
}

function bullets(s, items, o) {
  s.addText(items.map((t, i) => ({
    text: t, options: { bullet: { indent: 16 }, breakLine: i < items.length - 1 },
  })), Object.assign({
    isTextBox: true, margin: 0, fontFace: F, fontSize: 15, color: INK,
    paraSpaceAfter: 9, valign: "top",
  }, o));
}

// grilla de manzanas para portada y cierre
function grilla(s, x0, y0, cols, rows, lado, calle, color, destacada) {
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      s.addShape(pres.ShapeType.roundRect, {
        x: x0 + c * (lado + calle), y: y0 + r * (lado + calle), w: lado, h: lado,
        rectRadius: 0.08, fill: { color }, line: { color, width: 0 },
      });
    }
  }
  if (destacada) {
    // pin ambar en una esquina: el reclamo
    const [c, r] = destacada;
    const px = x0 + c * (lado + calle) - calle / 2 - 0.17;
    const py = y0 + r * (lado + calle) - calle / 2 - 0.17;
    s.addShape(pres.ShapeType.ellipse, {
      x: px - 0.16, y: py - 0.16, w: 0.66, h: 0.66,
      fill: { color: AMBER, transparency: 70 }, line: { width: 0, color: AMBER },
    });
    s.addShape(pres.ShapeType.ellipse, {
      x: px, y: py, w: 0.34, h: 0.34, fill: { color: AMBER }, line: { width: 0, color: AMBER },
    });
  }
}

// ================= 1 · PORTADA =================
{
  const s = pres.addSlide();
  s.background = { color: NAVY };
  grilla(s, 8.55, 0.85, 4, 5, 0.86, 0.26, BLOCK, [2, 2]);

  txt(s, "UTN FRRo  ·  ADMINISTRACIÓN DE SISTEMAS DE INFORMACIÓN  ·  TPI 2026 — ETAPA 4", {
    x: ML, y: 0.75, w: 7.6, h: 0.3, fontSize: 12, bold: true, color: "8FB6DA", charSpacing: 1,
  });
  txt(s, "Cuadra", {
    x: ML, y: 1.85, w: 7.5, h: 1.4, fontSize: 88, bold: true, color: WHITE, valign: "middle",
  });
  txt(s, "Del reclamo a la cuadrilla, a la vista de todos", {
    x: ML, y: 3.3, w: 7.6, h: 0.6, fontSize: 26, italic: true, color: AMBER,
  });
  txt(s, "Una startup para ciudades inteligentes: reclamos urbanos que llegan al responsable correcto, con tiempos públicos y datos abiertos.", {
    x: ML, y: 4.1, w: 7.2, h: 0.9, fontSize: 16, color: ICE, lineSpacingMultiple: 1.1,
  });
  txt(s, "Comisión 403  ·  Grupo 310", {
    x: ML, y: 5.65, w: 7, h: 0.32, fontSize: 14, bold: true, color: WHITE,
  });
  txt(s, "Bonadeo  ·  Casermeiro  ·  Lezcano  ·  Lurati", {
    x: ML, y: 6.0, w: 7, h: 0.32, fontSize: 14, color: ICE,
  });
  if (NOTAS["1"]) s.addNotes(NOTAS["1"]);
}

// ================= 2 · EL PROBLEMA =================
{
  const s = pres.addSlide();
  head(s, 2, "1", "Reclamar no alcanza",
    "Un bache, una luminaria apagada, un cable caído: el problema no es verlo, es que llegue a quien lo resuelve.");

  const y = 1.95, h = 3.65, w = (CW - 0.4) / 2;
  const cols = [
    ["El vecino", "¿De quién es el problema?", [
      "La calle es del municipio, el poste de la distribuidora, el cable de una telco.",
      "Si se equivoca de destinatario, el reclamo se pierde.",
      "Si acierta, no sabe cuándo se resuelve: vuelve a reclamar.",
    ]],
    ["Quien lo resuelve", "El mismo bache entra 20 veces", [
      "Teléfono, redes, mensajería, mostrador: nadie sabe cuáles son el mismo reclamo.",
      "La cuadrilla sale con una dirección escrita a mano y sin foto.",
      "El cierre no deja evidencia ni tiempos.",
    ]],
  ];
  cols.forEach(([quien, frase, items], i) => {
    const x = ML + i * (w + 0.4);
    card(s, { x, y, w, h });
    txt(s, quien.toUpperCase(), {
      x: x + 0.4, y: y + 0.32, w: w - 0.8, h: 0.3, fontSize: 12, bold: true, color: MUTED, charSpacing: 1.2,
    });
    txt(s, frase, {
      x: x + 0.4, y: y + 0.66, w: w - 0.8, h: 0.55, fontSize: 23, bold: true, color: NAVY,
    });
    bullets(s, items, { x: x + 0.4, y: y + 1.45, w: w - 0.8, h: 2.1, fontSize: 15.5 });
  });

  card(s, { x: ML, y: 5.88, w: CW, h: 0.85, fill: AMBER_SOFT, line: AMBER_SOFT });
  txt(s, [
    { text: "Resultado: ", options: { bold: true, color: "8A5A12" } },
    { text: "nadie puede decir cuánto se tarda en arreglar una luminaria.", options: { color: INK } },
  ], { x: ML + 0.4, y: 5.88, w: CW - 0.8, h: 0.85, fontSize: 19, valign: "middle" });
}

// ================= 3 · ROSARIO YA LO RESOLVIO =================
{
  const s = pres.addSlide();
  head(s, 3, "1", "Rosario ya lo resolvió… para Rosario",
    "En la Etapa 1 lo tomamos como base para evaluarla como ciudad en transición.");

  // izquierda: lo que tiene Rosario
  const xl = ML, wl = 5.55, y0 = 1.95;
  txt(s, "LO QUE YA EXISTE", { x: xl, y: y0, w: wl, h: 0.3, fontSize: 12, bold: true, color: MUTED, charSpacing: 1.2 });
  const chips = [["147", "Línea de atención"], ["Munibot", "Asistente por mensajería"], ["SUA", "Sistema Único de Atención"], ["CIOR", "Centro Integrado de Operaciones"]];
  chips.forEach(([sig, desc], i) => {
    const cy = y0 + 0.45 + i * 0.86;
    s.addShape(pres.ShapeType.roundRect, {
      x: xl, y: cy, w: 1.55, h: 0.66, rectRadius: 0.08, fill: { color: NAVY }, line: { color: NAVY, width: 0 },
    });
    txt(s, sig, { x: xl, y: cy, w: 1.55, h: 0.66, fontSize: 18, bold: true, color: WHITE, align: "center", valign: "middle" });
    txt(s, desc, { x: xl + 1.8, y: cy, w: wl - 1.8, h: 0.66, fontSize: 16, color: INK, valign: "middle" });
  });

  // derecha: lo que falta
  const xr = ML + 6.15, wr = CW - 6.15;
  card(s, { x: xr, y: y0, w: wr, h: 3.85 });
  txt(s, "LO QUE FALTA", { x: xr + 0.4, y: y0 + 0.3, w: wr - 0.8, h: 0.3, fontSize: 12, bold: true, color: MUTED, charSpacing: 1.2 });
  const faltas = [
    ["Los municipios medianos", "del Gran Rosario no pueden desarrollar ni operar un sistema así por su cuenta."],
    ["Las prestadoras", "con infraestructura en la calle no reciben el reclamo integrado, ni siquiera en Rosario."],
  ];
  faltas.forEach(([b, r], i) => {
    const fy = y0 + 0.8 + i * 1.45;
    manzana(s, String(i + 1), { x: xr + 0.4, y: fy + 0.04, d: 0.5, fill: AMBER, fs: 16 });
    txt(s, [{ text: b + " ", options: { bold: true, color: NAVY } }, { text: r }], {
      x: xr + 1.15, y: fy, w: wr - 1.55, h: 1.2, fontSize: 17, lineSpacingMultiple: 1.05,
    });
  });

  card(s, { x: ML, y: 6.05, w: CW, h: 0.72, fill: NAVY, line: NAVY });
  txt(s, [
    { text: "No competimos con el 147: nos integramos.  ", options: { bold: true, color: WHITE } },
    { text: "Mercado resegmentado: el modelo de una ciudad grande, como servicio, para quien no puede construirlo.", options: { color: ICE } },
  ], { x: ML + 0.4, y: 6.05, w: CW - 0.8, h: 0.72, fontSize: 15.5, valign: "middle" });
}

// ================= 4 · COMO FUNCIONA =================
{
  const s = pres.addSlide();
  head(s, 4, "1", "Cómo funciona Cuadra",
    "Una plataforma en la nube que lleva el reclamo desde el vecino hasta la cuadrilla que lo resuelve, sea del municipio o de una prestadora.");

  const pasos = [
    ["App del vecino", "Foto, ubicación por GPS y categoría. Sin instalar nada: también desde un QR en la calle. Número de seguimiento y aviso en cada cambio."],
    ["Motor de ruteo", "Decide a quién le corresponde —área municipal o prestadora— por tipo y zona. Agrupa los repetidos en una sola orden."],
    ["App de cuadrilla", "La orden en el celular, sin conexión, con prioridad. Cierre con foto del antes y del después, georreferenciado."],
    ["Tablero público", "Tiempos de resolución por barrio, categoría y responsable. Datos abiertos, agregados y anonimizados."],
  ];
  const y = 2.05, h = 3.3, gap = 0.42;
  const w = (CW - gap * 3) / 4;
  pasos.forEach(([t, d], i) => {
    const x = ML + i * (w + gap);
    card(s, { x, y, w, h, fill: i === 3 ? NAVY : PAPER, line: i === 3 ? NAVY : LINE });
    manzana(s, String(i + 1), { x: x + 0.3, y: y + 0.3, d: 0.52, fill: i === 3 ? AMBER : NAVY, fs: 17 });
    txt(s, t, { x: x + 0.3, y: y + 0.98, w: w - 0.6, h: 0.45, fontSize: 19, bold: true, color: i === 3 ? WHITE : NAVY });
    txt(s, d, { x: x + 0.3, y: y + 1.5, w: w - 0.55, h: 1.7, fontSize: 14, color: i === 3 ? ICE : INK, lineSpacingMultiple: 1.05 });
    if (i < 3) {
      s.addShape(pres.ShapeType.rightArrow, {
        x: x + w + 0.07, y: y + h / 2 - 0.15, w: gap - 0.14, h: 0.3,
        fill: { color: AMBER }, line: { color: AMBER, width: 0 },
      });
    }
  });

  card(s, { x: ML, y: 5.6, w: CW, h: 0.62, fill: ICE, line: ICE });
  txt(s, [
    { text: "Conector  ", options: { bold: true, color: NAVY } },
    { text: "Se integra con lo que ya existe —el SUA de una ciudad grande, el sistema comercial de una prestadora—: suma, no reemplaza." },
  ], { x: ML + 0.35, y: 5.6, w: CW - 0.7, h: 0.62, fontSize: 15, valign: "middle" });
  txt(s, "La app de cuadrilla es la misma solución que planificamos para Personal en la Etapa 3: trazabilidad, priorización y evidencia de cierre.", {
    x: ML, y: 6.38, w: CW, h: 0.4, fontSize: 13, italic: true, color: MUTED,
  });
}

// ================= 5 · NO ES UNA APP MAS =================
{
  const s = pres.addSlide();
  head(s, 5, "1", "Por qué no es una app más");

  // izquierda: la idea disruptiva
  const xl = ML, wl = 6.0;
  txt(s, "La disrupción no está en la tecnología: está en cambiar el comportamiento del mercado.", {
    x: xl, y: 1.5, w: wl, h: 1.05, fontSize: 15, italic: true, color: MUTED,
  });
  txt(s, "El reclamo deja de ser un trámite de cada organización y pasa a ser un servicio con tiempos públicos.", {
    x: xl, y: 2.25, w: wl, h: 1.6, fontSize: 25, bold: true, color: NAVY, lineSpacingMultiple: 1.02,
  });
  const dos = [["Para el vecino", "deja de importar de quién es el problema."], ["Para el municipio", "la demora deja de ser invisible."]];
  dos.forEach(([a, b], i) => {
    txt(s, [{ text: a + ", ", options: { bold: true, color: INK } }, { text: b }], {
      x: xl, y: 4.05 + i * 0.5, w: wl, h: 0.45, fontSize: 17,
    });
  });

  // derecha: ejes de la consigna
  const xr = ML + 6.6, wr = CW - 6.6;
  txt(s, "EJES DE LA CONSIGNA QUE CUBRE", { x: xr, y: 1.55, w: wr, h: 0.3, fontSize: 12, bold: true, color: MUTED, charSpacing: 1.2 });
  const ejes = ["Empleo de TICs", "Transparencia gobierno–ciudadanos", "Datos abiertos", "Planificación urbana", "Entorno social", "Ambiente y residuos"];
  const cw = (wr - 0.25) / 2;
  ejes.forEach((e, i) => {
    const cx = xr + (i % 2) * (cw + 0.25), cy = 1.98 + Math.floor(i / 2) * 0.72;
    s.addShape(pres.ShapeType.roundRect, {
      x: cx, y: cy, w: cw, h: 0.56, rectRadius: 0.08, fill: { color: ICE }, line: { color: ICE, width: 0 },
    });
    txt(s, e, { x: cx + 0.2, y: cy, w: cw - 0.3, h: 0.56, fontSize: 14.5, bold: true, color: NAVY, valign: "middle" });
  });

  // abajo: triple impacto
  const ti = [
    ["Económico", "Menor costo por reclamo atendido y menos salidas en falso de las cuadrillas."],
    ["Social", "El barrio periférico ve el mismo tablero que el centro: la desigualdad se vuelve visible."],
    ["Ambiental", "Menos kilómetros de cuadrilla; detección temprana de basurales y pérdidas de agua."],
  ];
  txt(s, "TRIPLE IMPACTO", { x: ML, y: 5.05, w: 4, h: 0.3, fontSize: 12, bold: true, color: MUTED, charSpacing: 1.2 });
  const tw = (CW - 0.6) / 3;
  ti.forEach(([t, d], i) => {
    const x = ML + i * (tw + 0.3);
    card(s, { x, y: 5.42, w: tw, h: 1.38 });
    txt(s, t, { x: x + 0.3, y: 5.55, w: tw - 0.6, h: 0.36, fontSize: 16, bold: true, color: NAVY });
    txt(s, d, { x: x + 0.3, y: 5.92, w: tw - 0.55, h: 0.82, fontSize: 13.5, color: INK });
  });
}

// ================= 6 · CLIENTES Y MERCADO =================
{
  const s = pres.addSlide();
  head(s, 6, "2", "Una plataforma de varios lados",
    "Solo funciona si están los que reclaman, los que resuelven y los que reciben su parte.");

  const segs = [
    ["Municipios", "PAGAN", "Medianos, del Gran Rosario: suscripción mensual. Cliente principal.", true],
    ["Prestadoras", "PAGAN", "Luz, agua, gas, telecomunicaciones: licencia por cuadrilla.", true],
    ["Vecinos", "GRATIS", "Reportan y siguen su reclamo. Actor crítico: si no responde, lo abandonan.", false],
    ["Planificadores", "PAGAN", "Consultoras, universidades, obras públicas: informes a medida.", true],
  ];
  const y = 1.95, h = 2.25, gap = 0.3, w = (CW - gap * 3) / 4;
  segs.forEach(([t, tag, d, paga], i) => {
    const x = ML + i * (w + gap);
    card(s, { x, y, w, h });
    s.addShape(pres.ShapeType.roundRect, {
      x: x + 0.3, y: y + 0.3, w: 0.95, h: 0.34, rectRadius: 0.06,
      fill: { color: paga ? NAVY : AMBER }, line: { width: 0, color: paga ? NAVY : AMBER },
    });
    txt(s, tag, { x: x + 0.3, y: y + 0.3, w: 0.95, h: 0.34, fontSize: 11, bold: true, color: WHITE, align: "center", valign: "middle", charSpacing: 1 });
    txt(s, t, { x: x + 0.3, y: y + 0.78, w: w - 0.6, h: 0.42, fontSize: 18, bold: true, color: NAVY });
    txt(s, d, { x: x + 0.3, y: y + 1.24, w: w - 0.55, h: 0.95, fontSize: 13.5, color: INK });
  });

  // abajo izquierda: arquetipo
  const yb = 4.5, hb = 2.3;
  const wl = 6.3;
  card(s, { x: ML, y: yb, w: wl, h: hb, fill: AMBER_SOFT, line: AMBER_SOFT });
  txt(s, "QUIÉN DECIDE", { x: ML + 0.4, y: yb + 0.3, w: 4, h: 0.3, fontSize: 12, bold: true, color: "8A5A12", charSpacing: 1.2 });
  txt(s, "Laura, 42 años, secretaria de gobierno de un municipio del Gran Rosario", {
    x: ML + 0.4, y: yb + 0.66, w: wl - 0.8, h: 0.75, fontSize: 18, bold: true, color: INK,
  });
  txt(s, "Recibe reclamos por teléfono, redes y mensajería, deriva a mano los de la distribuidora y no puede responder cuánto tarda su gestión en arreglar una luminaria.", {
    x: ML + 0.4, y: yb + 1.4, w: wl - 0.8, h: 0.85, fontSize: 13.5, color: INK,
  });

  // abajo derecha: meta
  const xr = ML + wl + 0.35, wr = CW - wl - 0.35;
  card(s, { x: xr, y: yb, w: wr, h: hb });
  txt(s, "MERCADO OBJETIVO: GRAN ROSARIO", { x: xr + 0.4, y: yb + 0.3, w: wr - 0.8, h: 0.3, fontSize: 12, bold: true, color: MUTED, charSpacing: 1.2 });
  const metas = [["3", "año 1"], ["8", "año 2"], ["14", "año 3"]];
  const mw = (wr - 0.8) / 3;
  metas.forEach(([n, a], i) => {
    const mx = xr + 0.4 + i * mw;
    txt(s, n, { x: mx, y: yb + 0.62, w: mw, h: 0.9, fontSize: 48, bold: true, color: NAVY, align: "center", valign: "middle" });
    txt(s, a, { x: mx, y: yb + 1.5, w: mw, h: 0.3, fontSize: 13, color: MUTED, align: "center" });
  });
  txt(s, "municipios al cierre de cada año · Funes, Roldán, Baigorria, VGG, Pérez, San Lorenzo…", {
    x: xr + 0.4, y: yb + 1.85, w: wr - 0.8, h: 0.35, fontSize: 12, color: MUTED, align: "center",
  });
}

// ================= 7 · MVP =================
{
  const s = pres.addSlide();
  head(s, 7, "1", "MVP: un piloto Mago de Oz de 90 días",
    "El vecino usa la aplicación real; el ruteo lo hace a mano el equipo. Validamos la demanda antes de construir el motor.");

  const hs = [
    ["H1", "Los vecinos usan un canal nuevo si les muestra el seguimiento", "≥ 15% de los reclamos entra por la app"],
    ["H2", "Buena parte de los reclamos son repetidos", "≥ 25% se agrupa con otro"],
    ["H3", "La trazabilidad acorta los tiempos", "−30% en el tiempo medio de resolución"],
    ["H4", "El municipio paga por el servicio", "Firma la suscripción al terminar el piloto"],
    ["H5", "Las prestadoras aceptan reclamos ruteados", "Una prueba la app de cuadrilla en la zona"],
  ];
  const x0 = ML, y0 = 1.95, rh = 0.6;
  const wHip = 6.5;
  txt(s, "HIPÓTESIS", { x: x0 + 0.85, y: y0, w: 4, h: 0.28, fontSize: 12, bold: true, color: MUTED, charSpacing: 1.2 });
  txt(s, "CRITERIO AL DÍA 90", { x: x0 + 0.85 + wHip + 0.3, y: y0, w: 4, h: 0.28, fontSize: 12, bold: true, color: MUTED, charSpacing: 1.2 });
  hs.forEach(([id, hip, crit], i) => {
    const y = y0 + 0.42 + i * (rh + 0.1);
    const clave = id === "H3" || id === "H4";
    card(s, { x: x0, y, w: CW, h: rh, fill: clave ? ICE : PAPER, line: clave ? ICE : LINE });
    manzana(s, id, { x: x0 + 0.1, y: y + 0.07, d: 0.46, fill: clave ? NAVY : MUTED, fs: 14 });
    txt(s, hip, { x: x0 + 0.85, y, w: wHip, h: rh, fontSize: 15.5, color: INK, valign: "middle", bold: clave });
    txt(s, crit, { x: x0 + 0.85 + wHip + 0.3, y, w: CW - wHip - 1.4, h: rh, fontSize: 15.5, color: NAVY, bold: true, valign: "middle" });
  });

  card(s, { x: ML, y: 6.05, w: CW, h: 0.72, fill: AMBER_SOFT, line: AMBER_SOFT });
  txt(s, [
    { text: "Pivot previsto: ", options: { bold: true, color: "8A5A12" } },
    { text: "si H4 falla y H5 se confirma, la prestadora pasa a ser el cliente principal y el municipio entra gratis como canal." },
  ], { x: ML + 0.4, y: 6.05, w: CW - 0.8, h: 0.72, fontSize: 15.5, valign: "middle" });
}

// ================= 8 · CANVAS =================
{
  const s = pres.addSlide();
  head(s, 8, "2", "Business Model Canvas");
  txt(s, "Lámina completa: Anexo I", { x: W - ML - 3.5, y: 0.58, w: 3.5, h: 0.4, fontSize: 13, italic: true, color: MUTED, align: "right" });

  const x0 = ML, y0 = 1.4, gw = CW, gap = 0.1;
  const colW = (gw - gap * 4) / 5;
  const topH = 3.75, botH = 1.5;
  const X = (c) => x0 + c * (colW + gap);
  const halfH = (topH - gap) / 2;

  function bloque(x, y, w, h, titulo, items, o = {}) {
    card(s, { x, y, w, h, r: 0.05, fill: o.fill || PAPER, line: o.fill || LINE });
    txt(s, titulo.toUpperCase(), { x: x + 0.16, y: y + 0.12, w: w - 0.3, h: 0.26, fontSize: 10.5, bold: true, color: o.head || MUTED, charSpacing: 0.8 });
    s.addText(items.map((t, i) => ({ text: t, options: { bullet: { indent: 10 }, breakLine: i < items.length - 1 } })), {
      isTextBox: true, margin: 0, x: x + 0.16, y: y + 0.44, w: w - 0.28, h: h - 0.52,
      fontFace: F, fontSize: o.fs || 12, color: o.color || INK, paraSpaceAfter: 3, valign: "top",
    });
  }

  bloque(X(0), y0, colW, topH, "Socios clave", ["Municipio piloto", "Personal (Telecom)", "Nube por uso", "Polo Tecnológico y BCR Innova", "UTN FRRo", "Vecinales", "Programas de emprendedores"]);
  bloque(X(1), y0, colW, halfH, "Actividades clave", ["Operar la plataforma", "Implementar y capacitar", "Vender y sumar prestadoras"]);
  bloque(X(1), y0 + halfH + gap, colW, halfH, "Recursos clave", ["Base georreferenciada de reclamos: barrera de entrada", "Plataforma y 4 cofundadores"]);
  bloque(X(2), y0, colW, topH, "Propuesta de valor", ["Municipio: saber y mostrar cuánto tarda", "Prestadora: solo sus reclamos, con foto y cierre con evidencia", "Vecino: reclamar una vez y seguirlo", "Planificadores: datos con historia"], { fill: NAVY, head: AMBER, color: WHITE, fs: 12.5 });
  bloque(X(3), y0, colW, halfH, "Relación", ["Piloto como puerta de entrada", "Referente de cuenta y mesa de usuarios", "Vecinos: autoservicio"]);
  bloque(X(3), y0 + halfH + gap, colW, halfH, "Canales", ["Venta directa", "QR en la vía pública", "El municipio invita a sus prestadoras"]);
  bloque(X(4), y0, colW, topH, "Segmentos", ["Municipios medianos (cliente principal)", "Prestadoras en la vía pública", "Vecinos (gratis)", "Planificadores"]);

  const yb = y0 + topH + gap, bw = (gw - gap) / 2;
  bloque(x0, yb, bw, botH, "Estructura de costos", ["Enfoque en costo · CF USD 5.500/mes con el retiro de los socios", "CV por municipio y cuadrilla + 5% de tributos · equilibrio ≈ 6 municipios"]);
  bloque(x0 + bw + gap, yb, bw, botH, "Fuentes de ingreso", ["Suscripción municipal · implementación", "Licencia por cuadrilla · datos e informes · sin publicidad"], { fill: AMBER_SOFT, head: "8A5A12" });
}

// ================= 9 · FUENTES DE INGRESO =================
{
  const s = pres.addSlide();
  head(s, 9, "2", "Fuentes de ingreso",
    "Cada segmento que paga tiene su fuente. El precio sale del valor percibido, no del costo más un margen.");

  const fuentes = [
    ["Suscripción municipal", "USD 600 – 2.200", "por mes, según tramo de habitantes"],
    ["Implementación", "USD 2.500", "pago único al alta"],
    ["Licencia por cuadrilla", "USD 35", "por cuadrilla y por mes (mínimo 10)"],
    ["Datos e informes", "USD 1.500", "por informe · USD 400/mes la interfaz"],
  ];
  const wl = 5.7, y0 = 1.95, rh = 0.93;
  fuentes.forEach(([f, p, d], i) => {
    const y = y0 + i * (rh + 0.12);
    card(s, { x: ML, y, w: wl, h: rh });
    txt(s, f, { x: ML + 0.3, y: y + 0.13, w: 2.6, h: 0.35, fontSize: 15.5, bold: true, color: INK });
    txt(s, d, { x: ML + 0.3, y: y + 0.5, w: 3.0, h: 0.35, fontSize: 12, color: MUTED });
    txt(s, p, { x: ML + 2.95, y, w: wl - 3.25, h: rh, fontSize: 21, bold: true, color: NAVY, align: "right", valign: "middle" });
  });
  txt(s, "Supuestos a validar con el MVP · en dólares, cobrados en pesos, sin IVA · sin publicidad: el tablero y los datos abiertos son gratis.", {
    x: ML, y: 6.25, w: wl, h: 0.55, fontSize: 12, italic: true, color: MUTED,
  });

  // derecha: grafico nativo del año 3
  const xr = ML + wl + 0.45, wr = CW - wl - 0.45;
  card(s, { x: xr, y: y0, w: wr, h: 4.85 });
  txt(s, "AÑO 3 · 14 MUNICIPIOS Y 280 CUADRILLAS", { x: xr + 0.35, y: y0 + 0.28, w: wr - 0.7, h: 0.28, fontSize: 12, bold: true, color: MUTED, charSpacing: 1.2 });
  txt(s, "USD 336.600 por año", { x: xr + 0.35, y: y0 + 0.6, w: wr - 0.7, h: 0.6, fontSize: 30, bold: true, color: NAVY });
  s.addChart(pres.ChartType.bar, [{
    name: "Participación", labels: ["Suscripción municipal", "Licencias por cuadrilla", "Datos e informes", "Implementación"],
    values: [54.2, 34.9, 6.4, 4.5],
  }], {
    x: xr + 0.2, y: y0 + 1.35, w: wr - 0.4, h: 3.35, barDir: "bar", barGapWidthPct: 45,
    chartColors: [NAVY], showValue: true, dataLabelFormatCode: '0.0"%"', dataLabelPosition: "outEnd",
    dataLabelColor: INK, dataLabelFontSize: 13, dataLabelFontBold: true, dataLabelFontFace: F,
    catAxisLabelColor: INK, catAxisLabelFontSize: 13, catAxisLabelFontFace: F, catAxisOrientation: "maxMin",
    catAxisLineShow: false, valAxisHidden: true, valAxisMaxVal: 68, valAxisMinVal: 0,
    valGridLine: { style: "none" }, catGridLine: { style: "none" }, showLegend: false,
  });
}

// ================= 10 · COSTOS Y EQUILIBRIO =================
{
  const s = pres.addSlide();
  head(s, 10, "2", "Costos y punto de equilibrio",
    "Enfoque en costo: el ruteo, los avisos y los datos son automáticos, y la nube se paga por uso.");

  const wl = 6.0, y0 = 1.95;
  card(s, { x: ML, y: y0, w: wl, h: 4.85 });
  txt(s, "CON UN MUNICIPIO DE HASTA 100.000 HABITANTES", { x: ML + 0.4, y: y0 + 0.3, w: wl - 0.8, h: 0.28, fontSize: 12, bold: true, color: MUTED, charSpacing: 1.2 });
  txt(s, "Q = CF / (P − CVu)", { x: ML + 0.4, y: y0 + 0.7, w: wl - 0.8, h: 0.5, fontSize: 22, bold: true, color: INK });
  txt(s, "= 5.500 / (1.200 − 180 − 60) = 5.500 / 960 ≈ 5,7", { x: ML + 0.4, y: y0 + 1.2, w: wl - 0.8, h: 0.42, fontSize: 17, color: INK });
  const filas = [
    ["CF  5.500", "costos fijos por mes, con el retiro de los cuatro socios"],
    ["P  1.200", "suscripción mensual del tramo"],
    ["CVu  240", "180 de operación + 60 de tributos (5%)"],
  ];
  filas.forEach(([a, b], i) => {
    const y = y0 + 1.85 + i * 0.5;
    txt(s, a, { x: ML + 0.4, y, w: 1.45, h: 0.4, fontSize: 14.5, bold: true, color: NAVY });
    txt(s, b, { x: ML + 1.9, y, w: wl - 2.3, h: 0.4, fontSize: 14, color: INK });
  });
  card(s, { x: ML + 0.4, y: y0 + 3.5, w: wl - 0.8, h: 1.05, fill: NAVY, line: NAVY });
  txt(s, "≈ 6 municipios", { x: ML + 0.7, y: y0 + 3.5, w: 3.2, h: 1.05, fontSize: 30, bold: true, color: WHITE, valign: "middle" });
  txt(s, "se alcanza durante el año 2", { x: ML + 3.55, y: y0 + 3.5, w: wl - 4.15, h: 1.05, fontSize: 14, color: ICE, valign: "middle" });

  // derecha: margen de contribucion vs costos fijos
  const xr = ML + wl + 0.45, wr = CW - wl - 0.45;
  card(s, { x: xr, y: y0, w: wr, h: 4.85 });
  txt(s, "MARGEN VS. COSTOS FIJOS · USD POR MES", { x: xr + 0.35, y: y0 + 0.3, w: wr - 0.7, h: 0.28, fontSize: 12, bold: true, color: MUTED, charSpacing: 1.2 });
  s.addChart(pres.ChartType.bar, [
    { name: "Margen de contribución", labels: ["Cierre del año 1", "Cierre del año 2"], values: [2620, 10240] },
    { name: "Costos fijos", labels: ["Cierre del año 1", "Cierre del año 2"], values: [5500, 8000] },
  ], {
    x: xr + 0.2, y: y0 + 0.7, w: wr - 0.4, h: 3.35, barDir: "col", barGrouping: "clustered", barGapWidthPct: 70,
    chartColors: [NAVY, AMBER], showValue: true, dataLabelFormatCode: "#,##0", dataLabelPosition: "outEnd",
    dataLabelColor: INK, dataLabelFontSize: 13, dataLabelFontBold: true, dataLabelFontFace: F,
    catAxisLabelColor: INK, catAxisLabelFontSize: 13, catAxisLabelFontFace: F,
    valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 12000,
    valGridLine: { style: "none" }, catGridLine: { style: "none" },
    showLegend: true, legendPos: "t", legendFontSize: 12.5, legendFontFace: F, legendColor: INK,
  });
  txt(s, "En el año 2 los fijos suben a unos USD 8.000 con un desarrollador y soporte. La brecha del primer año y medio la cubre la inversión.", {
    x: xr + 0.35, y: y0 + 4.1, w: wr - 0.7, h: 0.65, fontSize: 12.5, italic: true, color: MUTED,
  });
}

// ================= 11 · EQUIPO =================
{
  const s = pres.addSlide();
  head(s, 11, "2", "Un rol y una hipótesis por cofundador",
    "Cuatro estudiantes avanzados de Ingeniería en Sistemas que ya planificaron una plataforma de órdenes de trabajo con app de campo.");

  const roles = [
    ["Dirección y municipios", "Venta institucional, negociación del piloto, inversor y programas de emprendedores.", ["H4"]],
    ["Prestadoras y alianzas", "Licencias por cuadrilla, relación con Personal y el ecosistema. Sostiene el pivot.", ["H5"]],
    ["Tecnología", "Plataforma, app de cuadrilla, conectores, seguridad y datos personales.", ["H3"]],
    ["Producto y operaciones", "App del vecino, tablero y datos abiertos; ruteo manual del piloto y capacitación.", ["H1", "H2"]],
  ];
  const y0 = 1.95, gap = 0.3, w = (CW - gap) / 2, h = 1.82;
  roles.forEach(([r, d, hs], i) => {
    const x = ML + (i % 2) * (w + gap), y = y0 + Math.floor(i / 2) * (h + 0.25);
    card(s, { x, y, w, h });
    hs.forEach((hh, j) => manzana(s, hh, { x: x + 0.3 + j * 0.62, y: y + 0.3, d: 0.54, fill: NAVY, fs: 14 }));
    txt(s, r, { x: x + 0.3 + hs.length * 0.62 + 0.15, y: y + 0.3, w: w - 1.5, h: 0.54, fontSize: 19, bold: true, color: NAVY, valign: "middle" });
    txt(s, d, { x: x + 0.3, y: y + 1.0, w: w - 0.6, h: 0.72, fontSize: 14.5, color: INK });
  });

  card(s, { x: ML, y: 6.05, w: CW, h: 0.72, fill: AMBER_SOFT, line: AMBER_SOFT });
  txt(s, [
    { text: "Pacto de socios: ", options: { bold: true, color: "8A5A12" } },
    { text: "las acciones se consolidan en cuatro años, con un mínimo de uno. Quien se va antes del primer año no conserva acciones." },
  ], { x: ML + 0.4, y: 6.05, w: CW - 0.8, h: 0.72, fontSize: 15.5, valign: "middle" });
}

// ================= 12 · QUE PEDIMOS =================
{
  const s = pres.addSlide();
  head(s, 12, "3", "Qué le pedimos al inversor");

  // fila de cifras
  const stats = [["USD 70.000", "para 18 meses"], ["20%", "de la SAS"], ["USD 350.000", "valuación posterior"]];
  const sw = (CW - 0.6) / 3, sy = 1.45;
  stats.forEach(([v, e], i) => {
    const x = ML + i * (sw + 0.3);
    card(s, { x, y: sy, w: sw, h: 1.45, fill: i === 0 ? NAVY : PAPER, line: i === 0 ? NAVY : LINE });
    txt(s, v, { x, y: sy + 0.18, w: sw, h: 0.75, fontSize: 38, bold: true, color: i === 0 ? WHITE : NAVY, align: "center", valign: "middle" });
    txt(s, e, { x, y: sy + 0.92, w: sw, h: 0.35, fontSize: 14, color: i === 0 ? ICE : MUTED, align: "center" });
  });

  // tramos
  const ty = 3.3;
  txt(s, "ENTRA EN DOS TRAMOS", { x: ML, y: ty, w: 5, h: 0.28, fontSize: 12, bold: true, color: MUTED, charSpacing: 1.2 });
  const tw = 3.55, tx2 = ML + tw + 0.75;
  const tramos = [
    [ML, "Tramo 1 · mes 0", "USD 35.000 por el 10%", "Financia el piloto de 90 días.", PAPER, LINE, NAVY],
    [tx2, "Tramo 2 · mes 6", "USD 35.000 por el 10%", "Se libera cuando el municipio firma la suscripción (H4).", AMBER_SOFT, AMBER_SOFT, "8A5A12"],
  ];
  tramos.forEach(([x, a, b, c, fill, line, col]) => {
    card(s, { x, y: ty + 0.4, w: tw, h: 1.75, fill, line });
    txt(s, a.toUpperCase(), { x: x + 0.3, y: ty + 0.6, w: tw - 0.6, h: 0.28, fontSize: 11.5, bold: true, color: col, charSpacing: 1 });
    txt(s, b, { x: x + 0.3, y: ty + 0.92, w: tw - 0.6, h: 0.42, fontSize: 19, bold: true, color: INK });
    txt(s, c, { x: x + 0.3, y: ty + 1.36, w: tw - 0.6, h: 0.7, fontSize: 14, color: INK });
  });
  s.addShape(pres.ShapeType.rightArrow, {
    x: ML + tw + 0.18, y: ty + 0.4 + 1.75 / 2 - 0.16, w: 0.4, h: 0.32, fill: { color: AMBER }, line: { color: AMBER, width: 0 },
  });

  // uso de fondos
  const ux = tx2 + tw + 0.5, uw = W - ML - ux;
  txt(s, "EN QUÉ SE USA", { x: ux, y: ty, w: uw, h: 0.28, fontSize: 12, bold: true, color: MUTED, charSpacing: 1.2 });
  const uso = [["60%", "Producto y equipo", 0.60, NAVY], ["25%", "Piloto y venta", 0.25, MID()], ["15%", "Reserva", 0.15, AMBER]];
  function MID() { return "5B7FA6"; }
  uso.forEach(([p, t, f, col], i) => {
    const y = ty + 0.45 + i * 0.58;
    s.addShape(pres.ShapeType.roundRect, { x: ux, y: y + 0.08, w: Math.max(0.3, (uw - 2.2) * f / 0.6), h: 0.34, rectRadius: 0.05, fill: { color: col }, line: { width: 0, color: col } });
    txt(s, p, { x: ux + (uw - 2.2) + 0.15, y, w: 0.65, h: 0.5, fontSize: 16, bold: true, color: NAVY, valign: "middle" });
    txt(s, t, { x: ux + (uw - 2.2) + 0.8, y, w: 1.4, h: 0.5, fontSize: 13.5, color: INK, valign: "middle" });
  });

  card(s, { x: ML, y: 6.05, w: CW, h: 0.72, fill: NAVY, line: NAVY });
  txt(s, [
    { text: "Si el piloto falla, el inversor arriesgó la mitad.  ", options: { bold: true, color: WHITE } },
    { text: "Si funciona, el segundo tramo va a una empresa con un cliente pagando. Se suman aportes no reembolsables.", options: { color: ICE } },
  ], { x: ML + 0.4, y: 6.05, w: CW - 0.8, h: 0.72, fontSize: 15, valign: "middle" });
}

// ================= 13 · CIERRE =================
{
  const s = pres.addSlide();
  s.background = { color: NAVY };
  txt(s, "CUADRA CIERRA EL INTEGRADOR", { x: ML, y: 0.7, w: 8, h: 0.3, fontSize: 13, bold: true, color: "8FB6DA", charSpacing: 1.2 });

  const etapas = [
    ["1", "Diagnóstico", "Rosario, ciudad en transición: falta una estrategia unificada para escalar."],
    ["2", "ITIL", "Cada reclamo con prioridad, responsable y tiempo comprometido."],
    ["3", "Proyecto de TI", "La plataforma de OT con app de campo para Personal, primer socio prestador."],
    ["4", "Emprendimiento", "Cuadra lleva todo eso a cualquier cuadrilla que trabaje en la calle."],
  ];
  const y = 1.5, gap = 0.3, w = (CW - gap * 3) / 4, h = 3.0;
  etapas.forEach(([n, t, d], i) => {
    const x = ML + i * (w + gap), ult = i === 3;
    s.addShape(pres.ShapeType.roundRect, {
      x, y, w, h, rectRadius: 0.08, fill: { color: ult ? WHITE : BLOCK }, line: { width: 0, color: ult ? WHITE : BLOCK },
    });
    manzana(s, n, { x: x + 0.3, y: y + 0.3, d: 0.54, fill: ult ? AMBER : ICE, color: ult ? WHITE : NAVY, fs: 17 });
    txt(s, "ETAPA " + n, { x: x + 1.0, y: y + 0.3, w: w - 1.2, h: 0.54, fontSize: 12, bold: true, color: ult ? MUTED : "8FB6DA", valign: "middle", charSpacing: 1 });
    txt(s, t, { x: x + 0.3, y: y + 1.0, w: w - 0.6, h: 0.42, fontSize: 19, bold: true, color: ult ? NAVY : WHITE });
    txt(s, d, { x: x + 0.3, y: y + 1.5, w: w - 0.55, h: 1.4, fontSize: 15, color: ult ? INK : ICE });
  });

  txt(s, "Del reclamo a la cuadrilla, a la vista de todos", {
    x: ML, y: 5.05, w: 8.8, h: 0.75, fontSize: 32, italic: true, bold: true, color: AMBER,
  });
  txt(s, "Gracias. ¿Preguntas?", { x: ML, y: 5.9, w: 8, h: 0.6, fontSize: 24, color: WHITE });
  grilla(s, 10.05, 4.95, 3, 2, 0.62, 0.2, BLOCK, [1, 1]);
  pie(s, 13, true);
  if (NOTAS["13"]) s.addNotes(NOTAS["13"]);
}

// pptxgenjs deja entradas de carpeta en el zip, que rompen la apertura desde la nube
pres.writeFile({ fileName: OUT }).then((f) => {
  try { require("child_process").execFileSync("zip", ["-dq", f, "*/"]); } catch (e) { /* sin carpetas */ }
  console.log("escrito:", f);
});
