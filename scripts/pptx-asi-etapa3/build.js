const pptxgen = require("pptxgenjs");
const path = require("path");

const RAIZ = path.resolve(__dirname, "..", "..");
const FIGS = process.argv[3] || path.join(RAIZ, "materias", "ASI", "figs", "presentacion");
const OUT  = process.argv[2] || path.join(RAIZ, "materias", "ASI", "entregables", "etapa3-presentacion.pptx");

// ---- paleta, tomada del entregable y del anexo grafico ----
const NAVY  = "15406B";
const ICE   = "DCE9F7";
const RED   = "B23A2E";
const MID   = "5B7FA6";
const MUTED = "4C6480";
const GOLD  = "8A6413";
const WHITE = "FFFFFF";
const PAPER = "F4F8FC";

const F = "Calibri";
const W = 13.333, H = 7.5;
const ML = 0.62, MR = 0.62;
const CW = W - ML - MR;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "Grupo 310 - Comision 403";
pres.title  = "ASI - TP Integrador Etapa 3";

// ============ helpers ============

// motivo visual: insignia circular con el numero de punto
function badge(s, n, opts = {}) {
  const dark = opts.dark || false;
  const x = opts.x !== undefined ? opts.x : ML;
  const y = opts.y !== undefined ? opts.y : 0.42;
  const d = 0.62;
  s.addShape(pres.ShapeType.ellipse, {
    x, y, w: d, h: d,
    fill: { color: dark ? ICE : NAVY },
    line: { color: dark ? ICE : NAVY, width: 0 },
  });
  s.addText(n, {
    x, y, w: d, h: d, isTextBox: true, margin: 0,
    fontFace: F, fontSize: n.length > 2 ? 13 : 17, bold: true,
    color: dark ? NAVY : WHITE, align: "center", valign: "middle",
  });
  return x + d;
}

// cabecera estandar de lamina de contenido
function head(s, num, titulo, bajada) {
  const right = badge(s, num);
  s.addText(titulo, {
    x: right + 0.24, y: 0.38, w: CW - (right - ML) - 0.24, h: 0.62,
    isTextBox: true, margin: 0, fontFace: F, fontSize: 29, bold: true,
    color: NAVY, valign: "middle",
  });
  if (bajada) {
    s.addText(bajada, {
      x: right + 0.24, y: 1.02, w: CW - (right - ML) - 0.24, h: 0.52,
      isTextBox: true, margin: 0, fontFace: F, fontSize: 12.5,
      color: MUTED, valign: "top",
    });
    return 1.66;
  }
  return 1.32;
}

// tarjeta con fondo tenue
function card(s, o) {
  s.addShape(pres.ShapeType.roundRect, {
    x: o.x, y: o.y, w: o.w, h: o.h, rectRadius: 0.06,
    fill: { color: o.fill || PAPER },
    line: { color: o.line || ICE, width: 1 },
  });
}

// cifra grande con etiqueta
function stat(s, o) {
  card(s, { x: o.x, y: o.y, w: o.w, h: o.h, fill: o.fill || PAPER, line: o.line || ICE });
  s.addText(o.valor, {
    x: o.x, y: o.y + 0.13, w: o.w, h: 0.72, isTextBox: true, margin: 0,
    fontFace: F, fontSize: o.tam || 34, bold: true,
    color: o.color || NAVY, align: "center", valign: "middle",
  });
  s.addText(o.etiqueta, {
    x: o.x + 0.1, y: o.y + 0.85, w: o.w - 0.2, h: o.h - 0.95, isTextBox: true, margin: 0,
    fontFace: F, fontSize: 11, color: MUTED, align: "center", valign: "top",
  });
}

// lista con vinetas
function lista(s, items, o) {
  s.addText(items.map((t, i) => ({
    text: t, options: { bullet: true, breakLine: i < items.length - 1 },
  })), {
    x: o.x, y: o.y, w: o.w, h: o.h, isTextBox: true, margin: 0,
    fontFace: F, fontSize: o.fs || 13, color: o.color || "2A3B4D",
    paraSpaceAfter: o.gap !== undefined ? o.gap : 7, valign: "top",
  });
}

function rotulo(s, t, o) {
  s.addText(t, {
    x: o.x, y: o.y, w: o.w, h: 0.26, isTextBox: true, margin: 0,
    fontFace: F, fontSize: 11.5, bold: true, color: o.color || NAVY,
    charSpacing: 0.8, valign: "middle",
  });
}

function parrafo(s, t, o) {
  s.addText(t, {
    x: o.x, y: o.y, w: o.w, h: o.h, isTextBox: true, margin: 0,
    fontFace: F, fontSize: o.fs || 13, color: o.color || "2A3B4D",
    valign: "top", lineSpacingMultiple: 1.08,
  });
}

// lamina de figura a sangre: las figuras se generan en 16:9 nativo
// (scripts/pptx-asi-etapa3/figs16x9.py), asi que llenan la diapositiva entera.
function figura(s, archivo) {
  s.background = { color: WHITE };
  s.addImage({ path: path.join(FIGS, archivo), x: 0, y: 0, w: W, h: H });
}

const TB = { color: NAVY, fill: ICE, bold: true, fontFace: F, fontSize: 11.5, valign: "middle" };
function celda(t, o = {}) {
  return { text: t, options: Object.assign({ fontFace: F, fontSize: 11.5, color: "2A3B4D", valign: "middle" }, o) };
}

// ================= 1 · PORTADA =================
{
  const s = pres.addSlide();
  s.background = { color: NAVY };
  s.addShape(pres.ShapeType.ellipse, { x: 10.6, y: -1.5, w: 5.2, h: 5.2, fill: { color: "1C4E7E" }, line: { width: 0 } });
  s.addShape(pres.ShapeType.ellipse, { x: 11.9, y: 5.1, w: 3.2, h: 3.2, fill: { color: "1C4E7E" }, line: { width: 0 } });

  s.addText("UNIVERSIDAD TECNOLÓGICA NACIONAL  ·  ADMINISTRACIÓN DE SISTEMAS DE INFORMACIÓN", {
    x: ML, y: 0.72, w: 10.2, h: 0.3, isTextBox: true, margin: 0,
    fontFace: F, fontSize: 12, bold: true, color: "8FB6DA", charSpacing: 1.1,
  });
  s.addText("Planificación de un\nProyecto de TI", {
    x: ML, y: 1.35, w: 9.6, h: 2.0, isTextBox: true, margin: 0,
    fontFace: F, fontSize: 50, bold: true, color: WHITE, lineSpacingMultiple: 0.95,
  });
  s.addText("Trabajo Práctico Integrador 2026 — Etapa 3", {
    x: ML, y: 3.42, w: 9.6, h: 0.4, isTextBox: true, margin: 0,
    fontFace: F, fontSize: 19, color: ICE,
  });

  card(s, { x: ML, y: 4.12, w: 7.5, h: 0.92, fill: "1C4E7E", line: "2E6395" });
  s.addText("Personal (Telecom Argentina)  ·  Proceso de instalación de internet con fibra óptica", {
    x: ML + 0.26, y: 4.12, w: 7.0, h: 0.92, isTextBox: true, margin: 0,
    fontFace: F, fontSize: 13.5, color: WHITE, valign: "middle",
  });

  s.addText("COMISIÓN 403  ·  GRUPO 310", {
    x: ML, y: 5.42, w: 6.0, h: 0.28, isTextBox: true, margin: 0,
    fontFace: F, fontSize: 11.5, bold: true, color: "8FB6DA", charSpacing: 1.0,
  });
  s.addText(
    "53535 · Bonadeo, Juan Cruz          52674 · Casermeiro, Gonzalo\n" +
    "53215 · Lezcano, Diego              52688 · Lurati, Ignacio", {
    x: ML, y: 5.76, w: 8.4, h: 0.8, isTextBox: true, margin: 0,
    fontFace: F, fontSize: 13, color: ICE, lineSpacingMultiple: 1.25,
  });
  s.addNotes("Reparto sugerido de la exposición (15-20 min):\n" +
    "· Bonadeo — láminas 2 a 5 (puntos 1, 2 y 3) y cierre, láminas 20 a 22 (punto 12 y conclusión).\n" +
    "· Casermeiro — láminas 6 a 9 (puntos 4 y 5).\n" +
    "· Lezcano — láminas 10 a 14 (puntos 6, 7-8 y 9).\n" +
    "· Lurati — láminas 15 a 19 (puntos 10 y 11).\n" +
    "Es una sugerencia: se puede reordenar sin tocar el deck.");
}

// ================= 2 · PROBLEMA =================
{
  const s = pres.addSlide();
  const y0 = head(s, "1", "El problema detectado", "Tres debilidades del proceso de instalación relevadas en las Etapas 1 y 2, hoy sin tratamiento");

  const items = [
    ["Trazabilidad", "El estado real de la instalación no está disponible en tiempo real. Genera reclamos duplicados y consultas manuales entre Operaciones, NOC y Comercial.", "Origen de R06"],
    ["Priorización", "La cola de órdenes de trabajo no tiene criterio de priorización. No es posible siquiera medir el cumplimiento del orden de despacho.", "R07 · severidad 12"],
    ["Competencias", "No se controla la competencia técnica al asignar una orden: técnico sin capacitación en el nuevo modelo de ONT.", "R04 · severidad 12"],
  ];
  const cw = (CW - 0.5) / 3;
  items.forEach(([t, d, tag], i) => {
    const x = ML + i * (cw + 0.25);
    card(s, { x, y: y0, w: cw, h: 3.86 });
    s.addShape(pres.ShapeType.ellipse, { x: x + 0.28, y: y0 + 0.28, w: 0.44, h: 0.44, fill: { color: NAVY }, line: { width: 0 } });
    s.addText(String(i + 1), { x: x + 0.28, y: y0 + 0.28, w: 0.44, h: 0.44, isTextBox: true, margin: 0, fontFace: F, fontSize: 13, bold: true, color: WHITE, align: "center", valign: "middle" });
    s.addText(t, { x: x + 0.85, y: y0 + 0.28, w: cw - 1.1, h: 0.44, isTextBox: true, margin: 0, fontFace: F, fontSize: 18, bold: true, color: NAVY, valign: "middle" });
    parrafo(s, d, { x: x + 0.28, y: y0 + 0.95, w: cw - 0.56, h: 2.2, fs: 13 });
    s.addText(tag, { x: x + 0.28, y: y0 + 3.28, w: cw - 0.56, h: 0.32, isTextBox: true, margin: 0, fontFace: F, fontSize: 11.5, bold: true, color: RED, valign: "middle" });
  });

  card(s, { x: ML, y: y0 + 4.06, w: CW, h: 1.28, fill: NAVY, line: NAVY });
  s.addText([
    { text: "R04 y R07 fueron identificados y valorados en la Etapa 2 y quedaron sin planilla de tratamiento. ", options: { color: WHITE } },
    { text: "Este proyecto es el tratamiento de ambos.", options: { color: ICE, bold: true } },
  ], { x: ML + 0.32, y: y0 + 4.06, w: CW - 0.64, h: 1.28, isTextBox: true, margin: 0, fontFace: F, fontSize: 15, valign: "middle" });

  s.addNotes("Bonadeo. Punto 1 del entregable. El proyecto no repite la Etapa 2: cierra el hueco que dejó. R04 y R07 son severidad 12 y son los únicos dos riesgos de esa severidad que quedaron sin plan de tratamiento.");
}

// ================= 3 · EL PROYECTO =================
{
  const s = pres.addSlide();
  const y0 = head(s, "1", "El proyecto propuesto", null);

  card(s, { x: ML, y: y0 - 0.12, w: CW, h: 0.95, fill: NAVY, line: NAVY });
  s.addText("Plataforma de gestión de órdenes de trabajo con aplicación móvil de campo", {
    x: ML + 0.32, y: y0 - 0.12, w: CW - 0.64, h: 0.95, isTextBox: true, margin: 0,
    fontFace: F, fontSize: 21, bold: true, color: WHITE, valign: "middle",
  });

  const yb = y0 + 1.06;
  const cw = (CW - 0.3) / 2;

  card(s, { x: ML, y: yb, w: cw, h: 4.04 });
  rotulo(s, "QUÉ INCLUYE", { x: ML + 0.3, y: yb + 0.22, w: cw - 0.6 });
  lista(s, [
    "Despacho y priorización con cola única",
    "Motor de asignación por competencia certificada, zona, carga y ventana horaria",
    "Aplicación móvil offline-first: checklist por modelo de ONT, mediciones ópticas, evidencia fotográfica y conformidad del cliente",
    "Integraciones con SGOT, CRM, base de datos y NMS",
    "SSO, doble factor y baja automática de credenciales",
    "Tablero de indicadores",
  ], { x: ML + 0.3, y: yb + 0.62, w: cw - 0.6, h: 3.2, fs: 12.5, gap: 8 });

  card(s, { x: ML + cw + 0.3, y: yb, w: cw, h: 4.04 });
  rotulo(s, "QUÉ NO INCLUYE", { x: ML + cw + 0.6, y: yb + 0.22, w: cw - 0.6, color: MUTED });
  lista(s, [
    "Reemplazo o migración del CRM, del SGOT o de la base de datos",
    "Rediseño del escalamiento del CRM (R06), que ya tiene plan propio",
    "Obra civil, tendido troncal y ampliación de nodos (R11)",
    "Reemplazo del firewall (R03) y redundancia del balanceador (R09)",
    "Otros procesos de campo: reparaciones, mudanzas y desinstalaciones",
    "Vehículos y fusionadoras",
  ], { x: ML + cw + 0.6, y: yb + 0.62, w: cw - 0.6, h: 3.2, fs: 12.5, gap: 8, color: MUTED });

  parrafo(s, "Interviene las actividades 3 a 9 del proceso modelado en la Etapa 1. Las actividades 1 y 2 —recepción de la solicitud y verificación de cobertura— siguen en el CRM.", {
    x: ML, y: yb + 4.24, w: CW, h: 0.5, fs: 12.5, color: MUTED,
  });

  s.addNotes("Bonadeo. Punto 1. El alcance está delimitado por exclusión explícita: lo que queda afuera está afuera porque ya tiene tratamiento propio o porque pertenece a otro proyecto. El docente destacó esta delimitación.");
}

// ================= 4 · OBJETIVOS =================
{
  const s = pres.addSlide();
  const y0 = head(s, "2", "Objetivos", "Cada uno con indicador, línea base, meta y plazo. Las líneas base se declaran como supuestos: su medición es un entregable de la fase 2.");

  const filas = [
    [{ text: "", options: TB }, { text: "Objetivo", options: TB }, { text: "Indicador", options: TB },
     { text: "Línea base", options: TB }, { text: "Meta", options: TB }, { text: "Plazo", options: TB }],
    [celda("O1", { bold: true, color: NAVY, align: "center" }), celda("Aumentar la productividad del técnico de campo"),
     celda("Instalaciones conformes ÷ horas-técnico"), celda("0,50 inst./h  (supuesto)"), celda("0,525  (+5%)", { bold: true, color: NAVY }), celda("6 meses desde producción")],
    [celda("O2", { bold: true, color: NAVY, align: "center" }), celda("Reducir la latencia de registro del cierre de la orden"),
     celda("% cerradas dentro de los 15 min · tiempo asignación→cierre"), celda("20%  ·  26 h  (supuesto)"), celda("≥90%  ·  ≤8 h", { bold: true, color: NAVY }), celda("Mes 4, sostenido 3 meses")],
    [celda("O3", { bold: true, color: NAVY, align: "center" }), celda("Reducir las visitas fallidas por causa evitable"),
     celda("Reprogramadas por falta de competencia o kit ÷ despachadas"), celda("12%  (supuesto)"), celda("≤6%", { bold: true, color: NAVY }), celda("6 meses desde producción")],
    [celda("O4", { bold: true, color: NAVY, align: "center" }), celda("Asegurar el cumplimiento de la priorización de la cola"),
     celda("% despachadas según el motor · cumplimiento del SLA"), celda("No medible hoy — esa imposibilidad es R07", { color: RED }), celda("≥95%  ·  ≥90%", { bold: true, color: NAVY }), celda("Mes 3 desde producción")],
  ];
  s.addTable(filas, {
    x: ML, y: y0, w: CW, colW: [0.62, 2.85, 3.05, 2.5, 1.65, 1.42],
    border: { type: "solid", color: ICE, pt: 1 }, rowH: [0.58, 1.05, 1.05, 1.05, 1.05],
    fill: { color: WHITE }, autoPage: false,
  });
  parrafo(s, "O1 comparte indicador con el objetivo de negocio comprometido en la Etapa 1. O4 no tiene línea base porque la imposibilidad de medirlo es, precisamente, la definición del riesgo R07.", {
    x: ML, y: y0 + 5.06, w: CW, h: 0.5, fs: 12.5, color: MUTED,
  });
  s.addNotes("Bonadeo. Punto 2. Lo importante acá: O1 y el objetivo de negocio de la Etapa 1 comparten indicador, y O4 no tiene línea base porque la imposibilidad de medirlo ES la definición del riesgo R07.");
}

// ================= 5 · ALTERNATIVAS =================
{
  const s = pres.addSlide();
  const y0 = head(s, "3", "Alternativas y selección", "Tres proyectos de TI que atacan problemas distintos de la organización, todos detectados en el análisis de riesgos de la Etapa 2");

  const alts = [
    ["1", "Plataforma de gestión de órdenes con aplicación móvil de campo", "Trazabilidad, priorización (R07) y control de competencias (R04)", true],
    ["2", "Seguridad perimetral y gestión de identidades", "Perímetro obsoleto sin soporte (R03) y credenciales de contratistas que sobreviven al contrato (R05) — severidad 15", false],
    ["3", "Capacidad y mantenimiento preventivo de planta externa", "Nodos que se saturan sin aviso (R11) y fibra que se degrada sin plan de inspección (R08)", false],
  ];
  let y = y0;
  alts.forEach(([n, t, p, sel]) => {
    card(s, { x: ML, y, w: CW, h: 1.08, fill: sel ? ICE : PAPER, line: sel ? MID : ICE });
    s.addShape(pres.ShapeType.ellipse, { x: ML + 0.26, y: y + 0.3, w: 0.48, h: 0.48, fill: { color: sel ? NAVY : "AFC6DC" }, line: { width: 0 } });
    s.addText(n, { x: ML + 0.26, y: y + 0.3, w: 0.48, h: 0.48, isTextBox: true, margin: 0, fontFace: F, fontSize: 14, bold: true, color: WHITE, align: "center", valign: "middle" });
    s.addText(t, { x: ML + 0.9, y: y + 0.08, w: 4.7, h: 0.92, isTextBox: true, margin: 0, fontFace: F, fontSize: 13.5, bold: true, color: NAVY, valign: "middle" });
    s.addText(p, { x: ML + 5.7, y: y + 0.08, w: 5.15, h: 0.92, isTextBox: true, margin: 0, fontFace: F, fontSize: 12, color: sel ? NAVY : MUTED, valign: "middle" });
    s.addText(sel ? "SELECCIONADA" : "Mencionada", {
      x: ML + CW - 1.65, y: y + 0.08, w: 1.4, h: 0.92, isTextBox: true, margin: 0,
      fontFace: F, fontSize: sel ? 11.5 : 12, bold: sel, color: sel ? RED : MUTED, align: "right", valign: "middle",
    });
    y += 1.2;
  });

  const yb = y + 0.16;
  const cw = (CW - 0.3) / 2;
  card(s, { x: ML, y: yb, w: cw, h: 1.74, fill: NAVY, line: NAVY });
  rotulo(s, "MODO DE CONSTRUCCIÓN", { x: ML + 0.3, y: yb + 0.18, w: cw - 0.6, color: "8FB6DA" });
  parrafo(s, "SaaS: plataforma de Field Service Management configurable, contratada como servicio. La organización no construye el producto: lo configura, y construye las integraciones y la capa de seguridad.", {
    x: ML + 0.3, y: yb + 0.56, w: cw - 0.6, h: 1.05, fs: 12.5, color: WHITE,
  });

  card(s, { x: ML + cw + 0.3, y: yb, w: cw, h: 1.74 });
  rotulo(s, "CONTRAPARTIDA ASUMIDA", { x: ML + cw + 0.6, y: yb + 0.18, w: cw - 0.6, color: RED });
  parrafo(s, "Costo recurrente por usuario, dependencia del proveedor y salida de datos personales del perímetro. Esto último agrava R05 y se compensa por vía contractual (punto 8) y en la factibilidad legal.", {
    x: ML + cw + 0.6, y: yb + 0.56, w: cw - 0.6, h: 1.05, fs: 12.5,
  });

  s.addNotes("Bonadeo. Punto 3. Ojo con la formulación: las alternativas NO son modos de construir lo mismo (interno / SaaS / tercerizado), son proyectos distintos que atacan otros problemas. Así lo redefinió el docente el 23/08. El modo de construcción SaaS también lo indicó él.");
}

// ================= 6 · CICLO DE VIDA =================
{
  const s = pres.addSlide();
  const y0 = head(s, "4.1", "Ciclo de vida híbrido", "No es una elección de compromiso: cada mitad del proyecto tiene una naturaleza distinta y exige un enfoque distinto");

  const cw = (CW - 0.3) / 2;
  card(s, { x: ML, y: y0, w: cw, h: 2.72, fill: ICE, line: MID });
  rotulo(s, "PREDICTIVO", { x: ML + 0.3, y: y0 + 0.2, w: cw - 0.6 });
  parrafo(s, "Selección y contratación del proveedor, arquitectura de integración, seguridad y cumplimiento normativo.", { x: ML + 0.3, y: y0 + 0.58, w: cw - 0.6, h: 0.85, fs: 13 });
  parrafo(s, "Requerimientos estables y cerrables por anticipado, proceso formal de compras con RFI y RFP, evaluación legal por datos personales. Entregables definidos, con aprobaciones secuenciales, que no admiten iteración.", { x: ML + 0.3, y: y0 + 1.5, w: cw - 0.6, h: 1.1, fs: 12.5, color: MUTED });

  card(s, { x: ML + cw + 0.3, y: y0, w: cw, h: 2.72, fill: PAPER, line: ICE });
  rotulo(s, "INCREMENTAL E ITERATIVO", { x: ML + cw + 0.6, y: y0 + 0.2, w: cw - 0.6 });
  parrafo(s, "Configuración funcional, experiencia de uso de la aplicación de campo, reglas de priorización y asignación, despliegue territorial.", { x: ML + cw + 0.6, y: y0 + 0.58, w: cw - 0.6, h: 0.85, fs: 13 });
  parrafo(s, "La usabilidad con guantes, bajo sol directo y sin conectividad no se especifica por adelantado, y los pesos del motor se calibran con datos reales. Se resuelve con piloto, ajuste y despliegue por olas.", { x: ML + cw + 0.6, y: y0 + 1.5, w: cw - 0.6, h: 1.1, fs: 12.5, color: MUTED });

  const yb = y0 + 2.98;
  card(s, { x: ML, y: yb, w: cw, h: 2.38 });
  rotulo(s, "POR QUÉ NO CASCADA PURA", { x: ML + 0.3, y: yb + 0.18, w: cw - 0.6, color: RED });
  parrafo(s, "Si la aplicación se entrega recién al final, el riesgo es una herramienta que los técnicos no adoptan y cuyo uso falsean —cierres cargados en bloque al fin de la jornada—, lo que destruye la medición de O1 y O2.", { x: ML + 0.3, y: yb + 0.58, w: cw - 0.6, h: 1.65, fs: 13 });

  card(s, { x: ML + cw + 0.3, y: yb, w: cw, h: 2.38 });
  rotulo(s, "POR QUÉ NO ÁGIL PURO", { x: ML + cw + 0.6, y: yb + 0.18, w: cw - 0.6, color: RED });
  parrafo(s, "Hay compromisos contractuales con un proveedor externo, adquisiciones con plazo de entrega, marco regulatorio de datos personales y un presupuesto que la Gerencia necesita aprobado por anticipado.", { x: ML + cw + 0.6, y: yb + 0.58, w: cw - 0.6, h: 1.65, fs: 13 });

  s.addNotes("Casermeiro. Punto 4.1. El docente destacó especialmente la defensa del ciclo de vida híbrido. La clave es que no se justifica por moda sino por la naturaleza de cada grupo de entregables.");
}

// ================= 7 · FASES =================
{
  const s = pres.addSlide();
  const y0 = head(s, "4.2", "Las once fases del proyecto", "Cada fase cierra con un entregable verificable. El paquete de primer nivel de la EDT se corresponde con la fase.");

  const fases = [
    ["1", "Inicio", "Acta de Proyecto aprobada"],
    ["2", "Relevamiento y análisis", "Requerimientos y medición de las líneas base de O1 a O4"],
    ["3", "Selección de proveedor", "RFI, lista corta, RFP, evaluación y contrato firmado"],
    ["4", "Diseño y configuración", "Flujos, motor de asignación y aplicación de campo configurados"],
    ["5", "Integración y seguridad", "SGOT, CRM, base de datos y NMS operativos; SSO y doble factor"],
    ["6", "Migración de datos", "Órdenes abiertas, padrón de técnicos y matriz de competencias"],
    ["7", "Pruebas", "Funcionales, de integración, de carga y de seguridad"],
    ["8", "Piloto en zona acotada", "Informe de piloto con ajustes de uso y de priorización"],
    ["9", "Capacitación", "Técnicos, supervisores, NOC y almacén capacitados y evaluados"],
    ["10", "Despliegue por olas", "Sistema en producción en todo el alcance geográfico"],
    ["11", "Estabilización y cierre", "Acta de cierre, traspaso a operación y alta del CI en la CMDB"],
  ];
  const cw = (CW - 0.28) / 2;
  fases.forEach(([n, t, e], i) => {
    const col = i < 6 ? 0 : 1;
    const row = i < 6 ? i : i - 6;
    const x = ML + col * (cw + 0.28);
    const y = y0 + row * 0.885;
    s.addShape(pres.ShapeType.roundRect, { x, y, w: 0.46, h: 0.46, rectRadius: 0.12, fill: { color: NAVY }, line: { width: 0 } });
    s.addText(n, { x, y, w: 0.46, h: 0.46, isTextBox: true, margin: 0, fontFace: F, fontSize: 13, bold: true, color: WHITE, align: "center", valign: "middle" });
    s.addText(t, { x: x + 0.62, y: y - 0.05, w: cw - 0.62, h: 0.32, isTextBox: true, margin: 0, fontFace: F, fontSize: 13.5, bold: true, color: NAVY, valign: "middle" });
    s.addText(e, { x: x + 0.62, y: y + 0.27, w: cw - 0.62, h: 0.46, isTextBox: true, margin: 0, fontFace: F, fontSize: 12, color: MUTED, valign: "top" });
  });

  parrafo(s, "La fase 11 cierra el circuito con la Etapa 2: el sistema es un nuevo elemento de configuración en la CMDB y su puesta en producción constituye un cambio normal, que pasa por el CAB.", {
    x: ML + cw + 0.28, y: y0 + 4.42, w: cw, h: 1.0, fs: 12.5, color: MUTED,
  });

  s.addNotes("Casermeiro. Punto 4.2. Si preguntan por qué once fases y no menos: cada una corta donde hay una decisión de avance o un entregable que otra área tiene que aprobar.");
}

// ================= 8 · EDT =================
{
  const s = pres.addSlide();
  const y0 = head(s, "4.3", "Estructura de desglose de trabajo", "Once paquetes de primer nivel y cincuenta paquetes de trabajo, cada uno con predecesora, duración, perfil y entregable verificable");

  const sw = (CW - 0.9) / 4;
  [["11", "paquetes de\nprimer nivel"], ["50", "paquetes de\ntrabajo"], ["9", "perfiles\nasignados"], ["30", "actividades en el\ncamino crítico"]]
    .forEach(([v, e], i) => stat(s, { x: ML + i * (sw + 0.3), y: y0, w: sw, h: 1.88, valor: v, etiqueta: e, tam: 40 }));

  const yb = y0 + 2.16;
  const cw = (CW - 0.3) / 2;

  card(s, { x: ML, y: yb, w: cw, h: 3.2 });
  rotulo(s, "CRITERIO DE DESCOMPOSICIÓN", { x: ML + 0.3, y: yb + 0.2, w: cw - 0.6 });
  parrafo(s, "No se descompone por debajo del nivel en que un paquete tiene un único entregable verificable y un responsable identificable.", { x: ML + 0.3, y: yb + 0.6, w: cw - 0.6, h: 0.95, fs: 13.5 });
  parrafo(s, "Las fases 9 y 10 se abren por ola de despliegue, porque cada ola es una entrega con valor propio y admite decisión de avance o retroceso.", { x: ML + 0.3, y: yb + 1.72, w: cw - 0.6, h: 1.1, fs: 13, color: MUTED });

  card(s, { x: ML + cw + 0.3, y: yb, w: cw, h: 3.2, fill: ICE, line: MID });
  rotulo(s, "SOLAPAMIENTOS PREVISTOS DESDE EL DISEÑO", { x: ML + cw + 0.6, y: yb + 0.2, w: cw - 0.6 });
  lista(s, [
    "AF — 2.2, 2.3 y 2.4 arrancan a la vez; la medición de línea base es la actividad más larga de la fase",
    "EI — 5.1 a 5.4 encadenadas sobre un único especialista, con 5.6 y 6.1 en la misma ventana: el conflicto de mayor impacto",
    "ES — interviene en 3.3 y 3.4, y luego en 5.5 y 5.6",
    "CP — 4.6, 4.7 y 5.1 comparten ventana; después 8.3, 10.1 y 11.1",
  ], { x: ML + cw + 0.6, y: yb + 0.6, w: cw - 0.6, h: 2.5, fs: 12.5, gap: 9 });

  s.addNotes("Casermeiro. Punto 4.3. Los solapamientos no son un descuido: están diseñados en la estructura y son el insumo del análisis de sobreasignación del punto 10. Es el punto donde la EDT y el aplanamiento se conectan.");
}

// ================= 9 · RRHH =================
{
  const s = pres.addSlide();
  const y0 = head(s, "5", "Recursos humanos", "Ningún perfil figura acá sin ser responsable de al menos un paquete de la EDT. La carga sale de sumar las duraciones de esos paquetes.");

  const filas = [
    [{ text: "Perfil", options: TB }, { text: "Pers.", options: Object.assign({}, TB, { align: "center" }) },
     { text: "Horas", options: Object.assign({}, TB, { align: "center" }) },
     { text: "Ventana", options: Object.assign({}, TB, { align: "center" }) },
     { text: "Ded.", options: Object.assign({}, TB, { align: "center" }) },
     { text: "Origen del recurso", options: TB }],
    ...[
      ["Analista funcional (AF)", "1", "848", "d6 – d189", "58%", "Interno"],
      ["Consultor de la plataforma (CP)", "1", "784", "d58 – d184", "78%", "Provisto por el proveedor"],
      ["Referente de operaciones (RO)", "1", "704", "d6 – d184", "49%", "Interno — Gerencia de Operaciones"],
      ["Especialista de integraciones (EI)", "2", "560", "d14 – d172", "22%", "Uno interno y uno por bolsa de horas"],
      ["Jefe de proyecto (JP)", "1", "408", "d0 – d192", "27%", "Interno — Tecnología y Sistemas"],
      ["Especialista de seguridad (ES)", "1", "312", "d14 – d109", "41%", "Interno — Seguridad de la Información"],
      ["Responsable de pruebas (QA)", "2", "232", "d27 – d109", "18%", "Interno"],
      ["Capacitador (CA)", "1", "200", "d105 – d164", "42%", "Interno — RR.HH. con Supervisión"],
      ["Diseño de experiencia de uso (UX)", "1", "192", "d58 – d145", "28%", "Interno; si no existe el rol, por obra"],
    ].map(r => [celda(r[0]), celda(r[1], { align: "center" }), celda(r[2], { align: "center" }),
                celda(r[3], { align: "center" }), celda(r[4], { align: "center" }), celda(r[5], { color: MUTED })]),
    [celda("Total", { bold: true, color: NAVY }), celda("11", { bold: true, color: NAVY, align: "center" }),
     celda("4.240", { bold: true, color: NAVY, align: "center" }), celda("d0 – d192", { bold: true, color: NAVY, align: "center" }),
     celda("—", { align: "center" }), celda("530 días-persona sobre 9 perfiles", { bold: true, color: NAVY })],
  ];
  s.addTable(filas, {
    x: ML, y: y0, w: CW, colW: [3.15, 0.72, 0.85, 1.42, 0.78, 5.17],
    border: { type: "solid", color: ICE, pt: 1 },
    rowH: [0.5, 0.44, 0.44, 0.44, 0.44, 0.44, 0.44, 0.44, 0.44, 0.44, 0.5],
    fill: { color: WHITE }, autoPage: false,
  });

  parrafo(s, "Ningún perfil alcanza dedicación completa: todos se afectan parcialmente y conservan sus responsabilidades de línea. La duplicación en EI y QA no responde a volumen sino al aplanamiento de recursos —evita 23 días hábiles de atraso—.", {
    x: ML, y: y0 + 5.14, w: CW, h: 0.6, fs: 12.5, color: MUTED,
  });

  s.addNotes("Casermeiro. Punto 5. La pregunta esperable es por qué dos personas en EI y en QA: la respuesta está en el punto 10, con una sola persona por perfil el proyecto pasa de 192 a 215 días.");
}

// ================= 10 · H&S CRITERIO =================
{
  const s = pres.addSlide();
  const y0 = head(s, "6", "Higiene y seguridad laboral", "Se analizan los sectores del proceso crítico —incluido el trabajo de campo—, no los sectores donde se ejecuta el proyecto");

  rotulo(s, "PREVENCIÓN PRIMARIA · CUATRO ACCIONES JERARQUIZADAS DE MAYOR A MENOR EFICACIA", { x: ML, y: y0, w: CW });
  const niveles = [
    ["1", "En el diseño", "De instalaciones, equipos y puestos. El layout es el instrumento que la materializa.", NAVY],
    ["2", "En el origen", "Se elimina o sustituye la fuente del riesgo.", "1C4E7E"],
    ["3", "En el medio", "Barreras entre la fuente y la persona: vallado, vehículo como barrera física.", "3E7099"],
    ["4", "Sobre la persona", "EPP, capacitación, vigilancia de la salud. El escalón más débil.", "8FA9C2"],
  ];
  const cw = (CW - 0.6) / 4;
  niveles.forEach(([n, t, d, c], i) => {
    const x = ML + i * (cw + 0.2);
    card(s, { x, y: y0 + 0.4, w: cw, h: 2.32, fill: c, line: c });
    s.addText(n, { x: x + 0.24, y: y0 + 0.54, w: 0.5, h: 0.45, isTextBox: true, margin: 0, fontFace: F, fontSize: 26, bold: true, color: i < 3 ? "8FB6DA" : WHITE, valign: "middle" });
    s.addText(t, { x: x + 0.24, y: y0 + 1.04, w: cw - 0.48, h: 0.33, isTextBox: true, margin: 0, fontFace: F, fontSize: 14.5, bold: true, color: WHITE, valign: "middle" });
    s.addText(d, { x: x + 0.24, y: y0 + 1.42, w: cw - 0.48, h: 1.15, isTextBox: true, margin: 0, fontFace: F, fontSize: 12, color: i < 3 ? ICE : "1B3A57", valign: "top" });
  });

  const yb = y0 + 3.02;
  const c2 = (CW - 0.3) / 2;
  card(s, { x: ML, y: yb, w: c2, h: 2.32 });
  rotulo(s, "SECTORES ANALIZADOS", { x: ML + 0.3, y: yb + 0.18, w: c2 - 0.6 });
  parrafo(s, "Base operativa — depósito y pañol, playa de carga, oficina del NOC, mesa de despacho, sala técnica y aula.\n\nCampo — tendido aéreo en vía pública, cámara subterránea (espacio confinado) y domicilio del cliente.", {
    x: ML + 0.3, y: yb + 0.58, w: c2 - 0.6, h: 1.62, fs: 13,
  });

  card(s, { x: ML + c2 + 0.3, y: yb, w: c2, h: 2.32, fill: ICE, line: MID });
  rotulo(s, "DONDE EL SISTEMA ES LA MEDIDA PREVENTIVA", { x: ML + c2 + 0.6, y: yb + 0.18, w: c2 - 0.6 });
  parrafo(s, "La habilitación vigente para trabajo en altura y riesgo eléctrico pasa a ser condición de despacho: una orden que requiere altura no puede asignarse a un técnico con certificación vencida. El control deja de depender de la memoria del técnico y se vuelve prevención en el diseño del flujo. Es, a la vez, el tratamiento de R04.", {
    x: ML + c2 + 0.6, y: yb + 0.58, w: c2 - 0.6, h: 1.62, fs: 12.5,
  });

  s.addNotes("Lezcano. Punto 6. La idea fuerte: el EPP se consigna siempre como complemento y nunca como respuesta principal. Y el caso del checklist bloqueante en la app es donde el proyecto y la higiene y seguridad se cruzan.");
}

// ================= 11 y 12 · PLANOS =================
{
  const s = pres.addSlide();
  figura(s, "fig3-plano.png");
  s.addNotes("Lezcano. Punto 6, figura 3 del Anexo II. Escala 1:125, norte indicado. Señalar: circulaciones peatonal y vehicular separadas y sin cruces, matafuegos identificados por clase, recorridos de evacuación y punto de encuentro fuera del edificio. Las cotas son mínimos de diseño supuestos, a validar con el Servicio de Higiene y Seguridad.");
}
{
  const s = pres.addSlide();
  figura(s, "fig4-campo.png");
  s.addNotes("Lezcano. Punto 6, figura 4 del Anexo II. Cuatro escenas: planta y vista lateral del tendido aéreo, cámara subterránea y domicilio del cliente. El vehículo aguas arriba es barrera física —prevención en el medio—; el checklist bloqueante en la app es prevención en el diseño.");
}

// ================= 13 · ACTIVOS =================
{
  const s = pres.addSlide();
  const y0 = head(s, "7·8", "Activos a adquirir y forma de adquisición", "Dimensionado sobre el alcance del proyecto: operación de fibra óptica en el Gran Rosario, 60 técnicos. No es la operación nacional.");

  const filas = [
    [{ text: "Activo o servicio", options: TB }, { text: "Cantidad", options: Object.assign({}, TB, { align: "center" }) },
     { text: "Forma de adquisición", options: TB }, { text: "Por qué así", options: TB }],
    ...[
      ["Licencias de la plataforma FSM", "78", "Suscripción anual", "En SaaS no hay licencia perpetua. La anual fija el precio durante la implantación y los 6 meses de medición; el compromiso plurianual consolidaría la dependencia antes del piloto"],
      ["Servicio de implantación y configuración", "784 h", "Bolsa de horas con tope", "El precio cerrado exigiría congelar la configuración antes del piloto, cuando 8.3 prevé ajustar reglas con datos reales"],
      ["Consultoría de integración", "560 h", "Servicios por hora, con tope", "El esfuerzo depende del estado real de los sistemas heredados, que se conoce recién en 2.3"],
      ["Dispositivos móviles rugerizados", "63", "Compra directa", "Vida útil superior al horizonte del proyecto y uso permanente. Quedan como activo y se incorporan a la CMDB"],
      ["Unidades de evaluación de dispositivos", "6", "Comodato", "Se necesitan antes de decidir la compra y se devuelven: traslada el costo de la prueba al oferente"],
      ["Servicio de mapas y geolocalización", "por uso", "Pago por uso, con tope mensual", "El volumen es proporcional a las órdenes y no es estimable antes de la medición de líneas base"],
      ["Soporte premium de estabilización", "12 meses", "Suscripción de plazo acotado", "Se descarta el pago por incidente: incentiva a no reportar y distorsiona el indicador"],
    ].map(r => [celda(r[0], { bold: true, color: NAVY }), celda(r[1], { align: "center" }), celda(r[2]), celda(r[3], { color: MUTED, fontSize: 11 })]),
  ];
  s.addTable(filas, {
    x: ML, y: y0, w: CW, colW: [2.9, 0.95, 2.3, 5.94],
    border: { type: "solid", color: ICE, pt: 1 },
    rowH: [0.52, 0.68, 0.68, 0.68, 0.68, 0.68, 0.68, 0.68],
    fill: { color: WHITE }, autoPage: false,
  });

  s.addNotes("Lezcano. Puntos 7 y 8, fusionados en una sola tabla como muestra la guía de cátedra. La columna que importa es la última: cada modalidad se elige por una razón de riesgo o de incertidumbre, no por costumbre.");
}

// ================= 14 · RFI y RFP =================
{
  const s = pres.addSlide();
  const y0 = head(s, "9", "RFI y RFP", "Dos instrumentos distintos y sucesivos: el RFI reduce la incertidumbre sobre el mercado, el RFP reduce la incertidumbre sobre la oferta");

  const cw = (CW - 0.3) / 2;
  const bloques = [
    ["RFI · PEDIDO DE INFORMACIÓN", ICE, MID, NAVY, [
      "Momento — etapa temprana, antes de fijar especificaciones",
      "Se pide — capacidades, arquitectura, modelos de licenciamiento y rangos de precio",
      "Se obtiene — un mapa del mercado que depura los requerimientos",
      "No vinculante para ninguna de las partes",
      "Acá: paquete 3.1, 5 días, crítico. Relevar integración nativa, alojamiento de datos y alcance real del modo offline",
    ]],
    ["RFP · PEDIDO DE PROPUESTA", PAPER, ICE, NAVY, [
      "Momento — con la lista corta hecha y el pliego cerrado",
      "Se pide — propuesta técnica y económica, cronograma, equipo, SLA y condiciones contractuales",
      "Se obtiene — ofertas comparables y puntuables, base de la negociación",
      "Vinculante para el oferente por el plazo de validez",
      "Acá: paquete 3.3, 7 días, crítico. Solo a la lista corta y sobre los requerimientos aprobados en 2.6",
    ]],
  ];
  bloques.forEach(([t, fill, line, col, items], i) => {
    const x = ML + i * (cw + 0.3);
    card(s, { x, y: y0, w: cw, h: 3.5, fill, line });
    rotulo(s, t, { x: x + 0.3, y: y0 + 0.2, w: cw - 0.6, color: col });
    lista(s, items, { x: x + 0.3, y: y0 + 0.6, w: cw - 0.6, h: 2.75, fs: 12.5, gap: 10 });
  });

  const yb = y0 + 3.74;
  card(s, { x: ML, y: yb, w: CW, h: 1.62, fill: NAVY, line: NAVY });
  rotulo(s, "CRITERIOS PONDERADOS DE EVALUACIÓN, DEFINIDOS ANTES DE ABRIR LAS PROPUESTAS", { x: ML + 0.3, y: yb + 0.15, w: CW - 0.6, color: "8FB6DA" });
  const crit = [["25%", "Seguridad y\nprotección de datos"], ["20%", "Capacidad de\nintegración"], ["20%", "Motor de asignación\ny modo offline"], ["15%", "Costo total de\npropiedad a 3 años"], ["10%", "Plazo de\nimplantación"], ["10%", "Soporte local\ny SLA"]];
  const kw = (CW - 0.6) / 6;
  crit.forEach(([p, t], i) => {
    const x = ML + 0.3 + i * kw;
    s.addText(p, { x, y: yb + 0.56, w: kw - 0.15, h: 0.38, isTextBox: true, margin: 0, fontFace: F, fontSize: 19, bold: true, color: i < 3 ? ICE : "8FB6DA", valign: "middle" });
    s.addText(t, { x, y: yb + 0.96, w: kw - 0.15, h: 0.5, isTextBox: true, margin: 0, fontFace: F, fontSize: 10.5, color: "B7CFE6", valign: "top" });
  });

  s.addNotes("Lezcano. Punto 9. Dos remates: (1) los tres primeros criterios concentran el 65% y se corresponden con los riesgos de la Etapa 2 que el proyecto trata o agrava; (2) hay un umbral de admisibilidad —la propuesta sin alojamiento en la región queda fuera cualquiera sea su puntaje—. No se emite RFQ porque el objeto no es un bien de especificación cerrada.");
}

// ================= 15 · TIEMPOS =================
{
  const s = pres.addSlide();
  const y0 = head(s, "10", "Tiempos del proyecto", "Estimación determinística por camino crítico sobre los 50 paquetes. En días hábiles y meses relativos al día 0, la aprobación del Acta.");

  const sw = (CW - 0.9) / 4;
  [["187", "días hábiles a fechas\ntempranas (CPM)", NAVY],
   ["192", "días hábiles de duración\nadoptada  ≈ 9,1 meses", RED],
   ["30 / 50", "actividades en el\ncamino crítico", NAVY],
   ["6", "tramos de sobreasignación\ndetectados", NAVY]]
    .forEach(([v, e, c], i) => stat(s, { x: ML + i * (sw + 0.3), y: y0, w: sw, h: 1.88, valor: v, etiqueta: e, tam: v.length > 4 ? 32 : 40, color: c, fill: i === 1 ? ICE : PAPER, line: i === 1 ? MID : ICE }));

  const yb = y0 + 2.16;
  const cw = (CW - 0.3) / 2;

  card(s, { x: ML, y: yb, w: cw, h: 3.2 });
  rotulo(s, "POR DÓNDE PASA EL CAMINO CRÍTICO", { x: ML + 0.3, y: yb + 0.18, w: cw - 0.6 });
  lista(s, [
    "Arranque y relevamiento",
    "Selección del proveedor — 31 días hábiles consecutivos, el tramo más largo y menos comprimible: depende de plazos de mercado y de la firma del contrato",
    "Las cuatro integraciones encadenadas sobre un mismo especialista",
    "Pruebas, piloto, capacitación de gestión, tres olas de despliegue y estabilización",
    "Las otras 20 actividades tienen holgura, entre 1 y 84 días hábiles: corriendo 24 de ellas dentro de esa holgura se resuelven los conflictos que el refuerzo no elimina",
  ], { x: ML + 0.3, y: yb + 0.58, w: cw - 0.6, h: 2.55, fs: 12, gap: 8 });

  const xr = ML + cw + 0.3;
  card(s, { x: xr, y: yb, w: cw, h: 3.2, fill: ICE, line: MID });
  rotulo(s, "APLANAMIENTO DE RECURSOS", { x: xr + 0.3, y: yb + 0.18, w: cw - 0.6 });
  const estrategias = [
    ["CPM a fechas tempranas", "187 días", "recursos ilimitados · no ejecutable", false],
    ["(a) Nivelación pura, una persona por perfil", "215 días", "+28 días (+15%) · 9 personas", false],
    ["(b) Refuerzo de EI y QA con una persona parcial", "192 días", "+5 días (+2,7%) · 11 personas", true],
  ];
  let ye = yb + 0.56;
  estrategias.forEach(([t, d, obs, sel]) => {
    s.addText(t, { x: xr + 0.3, y: ye, w: cw - 2.05, h: 0.38, isTextBox: true, margin: 0, fontFace: F, fontSize: 12, bold: sel, color: NAVY, valign: "middle" });
    s.addText(d, { x: xr + cw - 1.72, y: ye, w: 1.42, h: 0.38, isTextBox: true, margin: 0, fontFace: F, fontSize: 16, bold: true, color: sel ? RED : MUTED, align: "right", valign: "middle" });
    s.addText(obs, { x: xr + 0.3, y: ye + 0.34, w: cw - 0.6, h: 0.28, isTextBox: true, margin: 0, fontFace: F, fontSize: 10.5, color: sel ? RED : MUTED, valign: "middle" });
    ye += 0.64;
  });
  parrafo(s, "Se adopta la segunda: dos personas parciales cuestan menos que 23 días hábiles adicionales de proyecto, que arrastran licenciamiento, estructura y el diferimiento de los beneficios.", { x: xr + 0.3, y: ye + 0.04, w: cw - 0.6, h: 0.62, fs: 11.5 });

  s.addNotes("Lurati. Punto 10. Insistir en que el cronograma va en meses relativos al día 0 y no en fechas de calendario: la fecha de inicio real no está definida. Fue una decisión del grupo (D2) ante una consulta que el docente no respondió.");
}

// ================= 16, 17 · RED y GANTT =================
{
  const s = pres.addSlide();
  figura(s, "fig1-red.png");
  s.addNotes("Lurati. Punto 10, figura 1 del Anexo II. Actividad en el nodo, en dos bandas. En rojo las 30 críticas con holgura total nula; en azul las 20 con holgura. Cada nodo lleva ES-D-EF arriba y LS-HT-LF abajo. Las etiquetas amarillas son las 8 precedencias que cruzan de una banda a la otra.");
}
{
  const s = pres.addSlide();
  figura(s, "fig2a-gantt.png");
  s.addNotes("Lurati. Punto 10, figura 2.a del Anexo II. Cronograma aplanado adoptado, 192 días. En rojo el camino crítico, en azul las no críticas, en línea de puntos la holgura remanente. Los cuatro hitos verticales: contrato firmado (d58), inicio del piloto (d122), ola 3 en producción (d169) y cierre (d192).");
}

// ================= 18 · HISTOGRAMA =================
{
  const s = pres.addSlide();
  figura(s, "fig2b-histo.png");
  s.addNotes("Lurati. Punto 10, figura 2.b del Anexo II. Mismo eje de tiempo y misma escala que el Gantt.\n" +
    "Las barras celestes claras son los picos de dos personas: son exactamente las seis ventanas de " +
    "sobreasignación que motivaron el refuerzo de EI y QA, y la comparación de estrategias está en la lámina 15. " +
    "La línea de puntos es la dotación asignada, y no se supera ningún día.\n" +
    "Si preguntan por qué no un tercer refuerzo: sumar un segundo referente de operaciones solo bajaría de 192 a " +
    "189 días, mejora que no justifica una tercera incorporación.");
}

// ================= 19 · COSTOS =================
{
  const s = pres.addSlide();
  const y0 = head(s, "11", "Variables de costo", "Todos los valores son supuestos declarados, a validar contra cotizaciones reales y contra las respuestas al RFI y al RFP. Expresados en dólares.");

  const cw = 6.0, CH = 5.36;
  card(s, { x: ML, y: y0, w: cw, h: CH });
  rotulo(s, "ESTRUCTURA DEL COSTO — AÑO 1  (USD)", { x: ML + 0.3, y: y0 + 0.22, w: cw - 0.6 });
  const comp = [
    ["Recursos humanos propios", "3.456 h al valor hora por perfil", "112.624", false],
    ["Adquisiciones (bienes)", "63 dispositivos rugerizados", "39.060", false],
    ["Servicios", "Licencias, implantación, MDM, mapas y soporte", "103.150", false],
    ["Subtotal costo directo", "", "254.834", true],
    ["Costos indirectos", "12% sobre el costo directo", "30.580", false],
    ["Reserva de contingencia", "15% — responde a R03, R04, R05 y R07", "42.812", false],
  ];
  let y = y0 + 0.72;
  comp.forEach(([t, d, v, tot]) => {
    s.addText(t, { x: ML + 0.3, y, w: 2.55, h: 0.5, isTextBox: true, margin: 0, fontFace: F, fontSize: 12.5, bold: tot, color: NAVY, valign: "middle" });
    s.addText(d, { x: ML + 2.9, y, w: 2.05, h: 0.5, isTextBox: true, margin: 0, fontFace: F, fontSize: 11, color: MUTED, valign: "middle" });
    s.addText(v, { x: ML + cw - 1.5, y, w: 1.2, h: 0.5, isTextBox: true, margin: 0, fontFace: F, fontSize: 13, bold: true, color: tot ? NAVY : "2A3B4D", align: "right", valign: "middle" });
    y += 0.54;
  });
  card(s, { x: ML + 0.3, y: y0 + 4.06, w: cw - 0.6, h: 0.98, fill: NAVY, line: NAVY });
  s.addText("Costo total del año 1", { x: ML + 0.55, y: y0 + 4.06, w: 3.0, h: 0.98, isTextBox: true, margin: 0, fontFace: F, fontSize: 14, bold: true, color: WHITE, valign: "middle" });
  s.addText("328.226", { x: ML + cw - 2.2, y: y0 + 4.06, w: 1.85, h: 0.98, isTextBox: true, margin: 0, fontFace: F, fontSize: 24, bold: true, color: ICE, align: "right", valign: "middle" });

  const xr = ML + cw + 0.32, rw = CW - cw - 0.32;
  card(s, { x: xr, y: y0, w: rw, h: CH, fill: ICE, line: MID });
  rotulo(s, "COSTO TOTAL DE PROPIEDAD A TRES AÑOS  (USD)", { x: xr + 0.3, y: y0 + 0.22, w: rw - 0.6 });
  const tco = [["Año 1", "328.226", "ejecución del proyecto"], ["Año 2", "100.379", "operación en régimen"], ["Año 3", "102.855", "con indexación contractual del 5%"]];
  let y2 = y0 + 0.8;
  tco.forEach(([a, v, o]) => {
    s.addText(a, { x: xr + 0.3, y: y2, w: 1.0, h: 0.46, isTextBox: true, margin: 0, fontFace: F, fontSize: 13, bold: true, color: NAVY, valign: "middle" });
    s.addText(v, { x: xr + 1.2, y: y2, w: 1.5, h: 0.46, isTextBox: true, margin: 0, fontFace: F, fontSize: 15, bold: true, color: NAVY, align: "right", valign: "middle" });
    s.addText(o, { x: xr + 2.9, y: y2, w: rw - 3.2, h: 0.46, isTextBox: true, margin: 0, fontFace: F, fontSize: 11.5, color: MUTED, valign: "middle" });
    y2 += 0.56;
  });
  s.addText([{ text: "531.460", options: { fontSize: 34, bold: true, color: NAVY } }, { text: "   total a 3 años", options: { fontSize: 13.5, color: MUTED } }],
    { x: xr + 0.3, y: y0 + 2.56, w: rw - 0.6, h: 0.72, isTextBox: true, margin: 0, fontFace: F, valign: "middle" });
  parrafo(s, "El año de ejecución concentra el 62% del total; el 38% restante es recurrente. Ese 38% es el rasgo económico distintivo del modelo contratado como servicio: el compromiso presupuestario no termina con la puesta en producción y crece con la dotación licenciada. Un desarrollo propio habría invertido la proporción.", {
    x: xr + 0.3, y: y0 + 3.42, w: rw - 0.6, h: 1.75, fs: 12.5,
  });

  s.addNotes("Lurati. Punto 11. Dos aclaraciones que conviene anticipar: el consultor de la plataforma (784 h) no se computa como RRHH propio porque lo provee el proveedor —va dentro del servicio de implantación—, y la contingencia del 15% no es un porcentaje de estilo: se justifica riesgo por riesgo con R03, R04, R05 y R07 de la Etapa 2.");
}

// ================= 20 · FACTIBILIDAD TÉCNICA =================
{
  const s = pres.addSlide();
  const y0 = head(s, "12", "Factibilidad técnica", "El proyecto no requiere tecnología por desarrollar: las plataformas FSM configuradas como servicio son un producto maduro. El problema está en otro lado.");

  card(s, { x: ML, y: y0, w: CW, h: 1.72, fill: NAVY, line: NAVY });
  rotulo(s, "EL SUPUESTO CRÍTICO, DECLARADO COMO RIESGO ABIERTO Y NO COMO HIPÓTESIS FAVORABLE", { x: ML + 0.32, y: y0 + 0.16, w: CW - 0.64, color: "8FB6DA" });
  s.addText([
    { text: "No está documentado si el SGOT, el CRM y el NMS exponen interfaces de programación aptas. ", options: { color: WHITE, bold: true } },
    { text: "De ese hecho depende la viabilidad de los paquetes 5.1 a 5.4, que están sobre el camino crítico y concentran 560 horas del especialista de integraciones. El punto de verificación es el paquete 2.3, que tiene apenas 4 días de holgura.", options: { color: ICE } },
  ], { x: ML + 0.32, y: y0 + 0.58, w: CW - 0.64, h: 1.05, isTextBox: true, margin: 0, fontFace: F, fontSize: 13.5, valign: "top", lineSpacingMultiple: 1.05 });

  const yb = y0 + 2.0;
  const cw = (CW - 0.6) / 3;
  const planes = [
    ["i", "Base de datos intermedia", "Esquema de intercambio y procesos programados contra vistas controladas del sistema de origen."],
    ["ii", "Intercambio por lotes", "En ventanas pactadas, con acuse y reproceso. Degrada la trazabilidad a cuasi tiempo real."],
    ["iii", "Automatización de interfaz", "Solo como recurso transitorio: frágil ante cambios de pantalla y caro de mantener."],
  ];
  rotulo(s, "PLAN ALTERNATIVO ANTE LA AUSENCIA DE API, EN ORDEN DECRECIENTE DE PREFERENCIA", { x: ML, y: yb, w: CW });
  planes.forEach(([n, t, d], i) => {
    const x = ML + i * (cw + 0.3);
    card(s, { x, y: yb + 0.4, w: cw, h: 1.85 });
    s.addText(n, { x: x + 0.28, y: yb + 0.5, w: 0.7, h: 0.35, isTextBox: true, margin: 0, fontFace: F, fontSize: 16, bold: true, color: MID, valign: "middle" });
    s.addText(t, { x: x + 0.28, y: yb + 0.86, w: cw - 0.56, h: 0.33, isTextBox: true, margin: 0, fontFace: F, fontSize: 13.5, bold: true, color: NAVY, valign: "middle" });
    s.addText(d, { x: x + 0.28, y: yb + 1.24, w: cw - 0.56, h: 0.95, isTextBox: true, margin: 0, fontFace: F, fontSize: 12, color: MUTED, valign: "top" });
  });

  const yc = yb + 2.5;
  card(s, { x: ML, y: yc, w: CW, h: 1.32 });
  rotulo(s, "OTROS RIESGOS TÉCNICOS RELEVANTES", { x: ML + 0.3, y: yc + 0.14, w: CW - 0.6 });
  s.addText([
    { text: "RT2 · sev 12 — ", options: { bold: true, color: NAVY } },
    { text: "la interfaz del SGOT no soporta el caudal de sincronización (240 órdenes diarias con pico al cierre de jornada). Se valida en 7.4.     ", options: { color: "2A3B4D" } },
    { text: "RT5 · sev 10 — ", options: { bold: true, color: NAVY } },
    { text: "indisponibilidad del canal por R03 (firewall sin soporte) y R09 (balanceador sin redundancia): dependencia externa declarada, fuera del alcance.", options: { color: "2A3B4D" } },
  ], { x: ML + 0.3, y: yc + 0.52, w: CW - 0.6, h: 0.72, isTextBox: true, margin: 0, fontFace: F, fontSize: 12.5, valign: "top", lineSpacingMultiple: 1.05 });

  s.addNotes("Bonadeo. Punto 12. Lo defendible acá es que el supuesto no se escondió: se declaró como riesgo con severidad 20, se le puso un punto de verificación temprano (2.3) y se le escribió un plan alternativo con las tres vías cotizadas en el RFP.");
}

// ================= 21 · FACTIBILIDAD ECONÓMICA =================
{
  const s = pres.addSlide();
  const y0 = head(s, "12", "Factibilidad económica", "Inversión descontada de USD 285.414 —costo directo más indirectos, sin la reserva— contra beneficios anuales de USD 222.400. Tasa de corte 15%, horizonte 5 años.");

  const sw = (CW - 0.9) / 4;
  [["+31.515", "VAN a 5 años al 15% (USD)\n11% de la inversión", NAVY],
   ["19,0%", "TIR, cuatro puntos sobre\nla tasa de corte", NAVY],
   ["3,14", "años de repago desde el Acta\n≈ 2,4 desde producción", NAVY],
   ["85%", "de realización de beneficios:\numbral de indiferencia", RED]]
    .forEach(([v, e, c], i) => stat(s, { x: ML + i * (sw + 0.3), y: y0, w: sw, h: 1.88, valor: v, etiqueta: e, tam: 34, color: c, fill: i === 3 ? ICE : PAPER, line: i === 3 ? MID : ICE }));

  const yb = y0 + 2.16, cw = (CW - 0.3) / 2, CH = 3.2;

  card(s, { x: ML, y: yb, w: cw, h: CH });
  rotulo(s, "DE DÓNDE SALEN LOS BENEFICIOS  (USD por año)", { x: ML + 0.3, y: yb + 0.22, w: cw - 0.6 });
  const ben = [["O3", "Visitas fallidas evitables reducidas del 12% al 6%", "103.000"],
               ["O2", "70% de las órdenes pasa a cerrarse en el momento", "57.700"],
               ["O1", "+5% de productividad = 3 técnicos de capacidad", "54.000"],
               ["—", "Reclamos y consultas duplicadas evitados", "7.700"]];
  let y = yb + 0.74;
  ben.forEach(([o, d, v]) => {
    s.addText(o, { x: ML + 0.3, y, w: 0.5, h: 0.44, isTextBox: true, margin: 0, fontFace: F, fontSize: 12.5, bold: true, color: NAVY, valign: "middle" });
    s.addText(d, { x: ML + 0.82, y, w: cw - 2.15, h: 0.44, isTextBox: true, margin: 0, fontFace: F, fontSize: 12, color: "2A3B4D", valign: "middle" });
    s.addText(v, { x: ML + cw - 1.35, y, w: 1.05, h: 0.44, isTextBox: true, margin: 0, fontFace: F, fontSize: 13, bold: true, color: NAVY, align: "right", valign: "middle" });
    y += 0.48;
  });
  card(s, { x: ML + 0.3, y: yb + 2.62, w: cw - 0.6, h: 0.44, fill: ICE, line: ICE });
  s.addText([{ text: "222.400", options: { fontSize: 17, bold: true, color: NAVY } }, { text: "   total anual en régimen", options: { fontSize: 12, color: MUTED } }],
    { x: ML + 0.48, y: yb + 2.62, w: cw - 0.96, h: 0.44, isTextBox: true, margin: 0, fontFace: F, valign: "middle" });

  card(s, { x: ML + cw + 0.3, y: yb, w: cw, h: CH, fill: ICE, line: MID });
  rotulo(s, "LECTURA HONESTA DEL RESULTADO", { x: ML + cw + 0.6, y: yb + 0.22, w: cw - 0.6, color: RED });
  parrafo(s, "El proyecto es viable, pero el margen es ajustado. A tres años todavía no se repaga: necesita el cuarto y el quinto año de operación para justificarse.", { x: ML + cw + 0.6, y: yb + 0.62, w: cw - 0.6, h: 0.82, fs: 13 });
  parrafo(s, "La sensibilidad no está en los costos, que son acotados, sino en los beneficios. En un escenario de realización sostenida del 60% —posible, porque las líneas base son supuestos y no mediciones— el VAN cae a −189.336. El origen más frágil es O1: la productividad solo se convierte en resultado si hay demanda insatisfecha que absorba la capacidad liberada.", {
    x: ML + cw + 0.6, y: yb + 1.5, w: cw - 0.6, h: 1.55, fs: 12.5, color: "2A3B4D",
  });

  s.addNotes("Bonadeo. Punto 12. No maquillar el resultado: está escrito así a propósito. La consecuencia práctica está en la conclusión: la decisión de despliegue masivo se toma en el paquete 8.4, después de medir las líneas base en 2.4, no con la aprobación del Acta.");
}

// ================= 22 · LEGAL Y CONCLUSIÓN =================
{
  const s = pres.addSlide();
  s.background = { color: NAVY };
  s.addShape(pres.ShapeType.ellipse, { x: 11.4, y: -1.9, w: 4.6, h: 4.6, fill: { color: "1C4E7E" }, line: { width: 0 } });

  badge(s, "12", { dark: true, x: ML, y: 0.42 });
  s.addText("Factibilidad legal y conclusión", {
    x: ML + 0.86, y: 0.38, w: CW - 0.86, h: 0.62, isTextBox: true, margin: 0,
    fontFace: F, fontSize: 29, bold: true, color: WHITE, valign: "middle",
  });
  s.addText("Alojar datos personales de clientes en una plataforma contratada como servicio los saca del perímetro de la organización. Eso tiene consecuencias jurídicas concretas.", {
    x: ML + 0.86, y: 1.02, w: CW - 1.6, h: 0.36, isTextBox: true, margin: 0,
    fontFace: F, fontSize: 12.5, color: "8FB6DA",
  });

  const cw = (CW - 0.6) / 3;
  const leyes = [
    ["Ley 25.326", "Datos personales", "El proveedor es encargado del tratamiento (art. 25); el alojamiento fuera del país es transferencia internacional (art. 12) y se vuelve requisito eliminatorio del RFP. Subsisten el deber de seguridad y confidencialidad."],
    ["Ley 25.506", "Firma digital", "La conformidad trazada en pantalla es firma electrónica, no digital: quien la invoca debe acreditar su validez. Se compensa con geolocalización, marca temporal, fotos, mediciones y auditoría inalterable."],
    ["Ley 20.744", "Contratistas y control", "El art. 30 impone responsabilidad solidaria por el contratista. La matriz de competencias que bloquea la asignación es el registro documentado de ese deber de control. La geolocalización se limita a la jornada y a hitos."],
  ];
  leyes.forEach(([l, t, d], i) => {
    const x = ML + i * (cw + 0.3);
    card(s, { x, y: 1.62, w: cw, h: 2.42, fill: "1C4E7E", line: "2E6395" });
    s.addText(l, { x: x + 0.28, y: 1.76, w: cw - 0.56, h: 0.34, isTextBox: true, margin: 0, fontFace: F, fontSize: 16, bold: true, color: WHITE, valign: "middle" });
    s.addText(t, { x: x + 0.28, y: 2.1, w: cw - 0.56, h: 0.28, isTextBox: true, margin: 0, fontFace: F, fontSize: 11.5, bold: true, color: "8FB6DA", valign: "middle" });
    s.addText(d, { x: x + 0.28, y: 2.46, w: cw - 0.56, h: 1.45, isTextBox: true, margin: 0, fontFace: F, fontSize: 11, color: ICE, valign: "top", lineSpacingMultiple: 1.05 });
  });

  s.addText("CONCLUSIÓN DEL ANÁLISIS DE FACTIBILIDAD", {
    x: ML, y: 4.36, w: CW, h: 0.3, isTextBox: true, margin: 0,
    fontFace: F, fontSize: 11.5, bold: true, color: "8FB6DA", charSpacing: 1.0,
  });
  const conc = [
    ["Técnicamente factible", "con un supuesto crítico declarado: que el SGOT, el CRM y el NMS expongan interfaces de programación. Se verifica en 2.3."],
    ["Económicamente viable, de margen estrecho", "VAN +31.515, TIR 19,0%, repago 3,14 años. A tres años el proyecto todavía no se repaga."],
    ["Legalmente factible bajo condición contractual", "sin las cláusulas del punto 8 el proyecto agravaría R05 en lugar de contenerlo."],
  ];
  let y = 4.72;
  conc.forEach(([t, d]) => {
    s.addShape(pres.ShapeType.ellipse, { x: ML + 0.04, y: y + 0.14, w: 0.16, h: 0.16, fill: { color: ICE }, line: { width: 0 } });
    s.addText([{ text: t + " ", options: { bold: true, color: WHITE } }, { text: d, options: { color: "B7CFE6" } }],
      { x: ML + 0.36, y, w: CW - 0.36, h: 0.44, isTextBox: true, margin: 0, fontFace: F, fontSize: 13, valign: "middle" });
    y += 0.5;
  });

  card(s, { x: ML, y: 6.32, w: CW, h: 0.78, fill: "1C4E7E", line: RED });
  s.addText([
    { text: "Por eso la decisión de despliegue masivo no se adopta con la aprobación del Acta, sino en el paquete 8.4: ", options: { color: WHITE, bold: true } },
    { text: "una vez medidas las líneas base (2.4), verificadas las interfaces (2.3) y cerrados los precios en el contrato (3.5).", options: { color: ICE } },
  ], { x: ML + 0.32, y: 6.32, w: CW - 0.64, h: 0.78, isTextBox: true, margin: 0, fontFace: F, fontSize: 13, valign: "middle" });

  s.addNotes("Bonadeo. Cierre. El remate del trabajo es este: hasta el paquete 8.4 el compromiso económico es acotado; a partir de ahí se compromete el grueso del licenciamiento y de los dispositivos. Es una planificación con un punto de decisión explícito, no un plan de una sola vía.");
}

pres.writeFile({ fileName: OUT }).then(() => console.log("OK " + OUT));
