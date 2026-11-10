// Presentación de la defensa del TPI Subte Constitución (Simulación 2026): 7 diapositivas, máximo 3 minutos,
// con 50 s reservados para mostrar el modelo funcionando en AnyLogic (diapositiva 5).
// Uso, desde la raíz del repo:  node scripts/sim/subte-defensa-pptx.js
// Sale en materias/SIM/entregables/TPI/subte/TPI_Subte_Defensa.pptx. Las notas de cada diapositiva son el guion
// de 13-guion-defensa.md. Los números de resultados salen de informe/generado/valores.tex (resultados_informe.py);
// si todavía no existe, la diapositiva de resultados queda marcada como pendiente. Volver a correr después de la
// producción.
const fs = require("fs");
const path = require("path");
const pptxgen = require("pptxgenjs");

const RAIZ = path.resolve(__dirname, "..", "..");
const SIM = path.join(RAIZ, "materias", "SIM");
const TPI = path.join(SIM, "entregables", "TPI", "subte");
const FIGS = path.join(SIM, "figs");
const SALIDA = path.join(TPI, "TPI_Subte_Defensa.pptx");
const LOGO_UTN = path.join(SIM, "entregables", "TPI", "caser", "video", "img", "logo-utn.png"); // 1227 x 319 px
const fig = (n) => path.join(FIGS, n);
const existe = (p) => fs.existsSync(p);

// Recomendación final: se escribe a mano aplicando la regla del paso 7 a los resultados. null = pendiente.
const RECOMENDACION = null;

// Colores: los del diagrama de la estación (azul Línea C, naranja del recorrido, beige del hall).
const COL = { tinta: "1F2733", noche: "16223A", lineaC: "1F5FBF", flujo: "D9531E", hall: "E9E4D8", gris: "6B7480",
  claro: "F3F4F6", verde: "15803D", rojo: "B91C1C", blanco: "FFFFFF" };
const FUENTE = "Calibri";

// ---------- datos ----------
function leerValores() {
  const p = path.join(TPI, "informe", "generado", "valores.tex");
  if (!existe(p)) return null;
  const v = {};
  const re = /\\newcommand\{\\(\w+)\}\{(.*)\}\s*$/gm;
  const txt = fs.readFileSync(p, "utf8");
  let m;
  while ((m = re.exec(txt))) {
    if (m[2].includes("pendiente")) continue;
    v[m[1]] = m[2].replace(/\\num\{([^}]*)\}/g, "$1").replace(/~\\%/g, " %").replace(/\\%/g, "%")
      .replace(/(-?\d+)\.(\d+)/g, "$1,$2").replace(/-/g, "−");
  }
  return v;
}

function leerGuion() {
  // Secciones "## m:ss · Quién · Diapositiva N: ..." de 13-guion-defensa.md (con sus indicaciones ">").
  const txt = fs.readFileSync(path.join(TPI, "13-guion-defensa.md"), "utf8");
  const partes = txt.split(/^## /m).slice(1).filter((s) => /^\d:\d\d/.test(s));
  return partes.map((s) => {
    const [cab, ...resto] = s.split("\n");
    const cuerpo = resto.filter((l) => l.trim()).map((l) => l.replace(/^> ?/, "INDICACIÓN: ")).join("\n").trim();
    return { cab: cab.trim(), cuerpo };
  });
}

const V = leerValores();
const GUION = leerGuion();
const nota = (i) => GUION.filter((g) => i.some((k) => g.cab.includes(k))).map((g) => `[${g.cab}]\n${g.cuerpo}`).join("\n\n");
const val = (k, def = "[pendiente]") => (V && V[k] !== undefined ? V[k] : def);

// ---------- presentación ----------
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9"; // 10 x 5.625 in
pres.title = "Molinetes de Constitución, Línea C";
pres.author = "Bonadeo, Estevez";
pres.theme = { headFontFace: FUENTE, bodyFontFace: FUENTE };

pres.defineSlideMaster({
  title: "CONTENIDO",
  background: { color: COL.blanco },
  objects: [
    { rect: { x: 0, y: 0, w: 0.12, h: 5.625, fill: { color: COL.lineaC } } },
    { image: { x: 0.45, y: 5.12, w: 0.3 * 1227 / 319, h: 0.3, path: LOGO_UTN } },
    { text: { text: "TPI Simulación 2026 · Molinetes de Constitución", options: { x: 2.0, y: 5.12, w: 6.6, h: 0.3,
      fontFace: FUENTE, fontSize: 10, color: COL.gris, align: "right", valign: "middle" } } },
  ],
  slideNumber: { x: 9.1, y: 5.12, w: 0.5, h: 0.3, fontFace: FUENTE, fontSize: 10, color: COL.gris, align: "right" },
});

function titulo(s, texto, sub) {
  s.addText(texto, { x: 0.45, y: 0.25, w: 9.1, h: 0.6, fontFace: FUENTE, fontSize: 26, bold: true, color: COL.tinta,
    margin: 0, valign: "middle" });
  if (sub) s.addText(sub, { x: 0.45, y: 0.82, w: 9.1, h: 0.35, fontFace: FUENTE, fontSize: 14, color: COL.gris,
    margin: 0, valign: "top" });
}

function imagen(s, archivo, x, y, wMax, hMax, ancho, alto) {
  const r = Math.min(wMax / ancho, hMax / alto);
  const w = ancho * r, h = alto * r;
  if (!existe(archivo)) {
    s.addText(`Falta ${path.basename(archivo)}`, { x, y, w: wMax, h: hMax, fontFace: FUENTE, fontSize: 12,
      color: COL.rojo, align: "center", valign: "middle", fill: { color: COL.claro } });
    return;
  }
  s.addImage({ path: archivo, x: x + (wMax - w) / 2, y: y + (hMax - h) / 2, w, h });
}

function vinetas(s, items, x, y, w, h, tam = 16) {
  s.addText(items.map((t, i) => ({ text: t, options: { bullet: { indent: 14 }, breakLine: i < items.length - 1,
    paraSpaceAfter: 8 } })), { x, y, w, h, fontFace: FUENTE, fontSize: tam, color: COL.tinta, valign: "top", margin: 2 });
}

// 1. Portada + problema
{
  const s = pres.addSlide();
  s.background = { color: COL.noche };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.12, h: 5.625, fill: { color: COL.flujo } });
  s.addText("Molinetes de Constitución, Línea C", { x: 0.6, y: 0.9, w: 8.8, h: 0.9, fontFace: FUENTE, fontSize: 36,
    bold: true, color: COL.blanco, margin: 0 });
  s.addText("¿Conviene habilitar más molinetes, validar más rápido o las dos cosas?", { x: 0.6, y: 1.8, w: 8.8,
    h: 0.6, fontFace: FUENTE, fontSize: 20, color: "C9D6EE", margin: 0 });
  s.addText([
    { text: "Ingreso a la Línea C en Constitución, ", options: {} },
    { text: "07:00 a 09:30 de un día hábil", options: { bold: true } },
    { text: ": las 14 ventanas de 15 min con más pasajeros de toda la red del subte.", options: {} },
  ], { x: 0.6, y: 2.75, w: 8.4, h: 0.8, fontFace: FUENTE, fontSize: 16, color: COL.blanco, margin: 0 });
  s.addText("Juan Cruz Bonadeo · Matías Estevez — Simulación, UTN FRRo, 2026", { x: 0.6, y: 4.6, w: 8.8, h: 0.4,
    fontFace: FUENTE, fontSize: 13, color: "9FB0CC", margin: 0 });
  s.addNotes(nota(["Diapositiva 1"]));
}

// 2. Por qué simular
{
  const s = pres.addSlide({ masterName: "CONTENIDO" });
  titulo(s, "Por qué simular y no usar una fórmula", "Con promedios no hay cola; con oleadas, sí");
  imagen(s, fig("tpi-subte-perfil-demanda.png"), 0.35, 1.3, 5.4, 3.6, 1440, 680);
  vinetas(s, [
    "08:15: 2.214 validaciones en 15 min; cada molinete ocupado un tercio del tiempo",
    "M/M/c con esos promedios: casi sin espera",
    "Pero el Roca trae 47 trenes en la franja: la gente llega en oleadas",
    "La cola es transitoria → simulación de eventos discretos",
  ], 5.95, 1.35, 3.7, 3.6, 15);
  s.addNotes(nota(["Diapositiva 2"]));
}

// 3. El modelo
{
  const s = pres.addSlide({ masterName: "CONTENIDO" });
  titulo(s, "El modelo: del tren al molinete", "AnyLogic, Pedestrian Library · sistema terminal");
  vinetas(s, [
    "Cada réplica = un día hábil real (75 días, mar–jun 2026)",
    "Validaciones por ventana de SBASE y llegada real de cada tren (Trenes Argentinos)",
    "Bajan por 21 puertas, caminan andén y hall, escaleras mecánicas, plaza y pasillo",
    "Eligen cola por distancia y fila; validan; la réplica termina cuando sale el último que entró antes de las 09:30",
  ], 0.45, 1.35, 3.5, 3.6, 13);
  imagen(s, fig("tpi-subte-estacion-niveles.png"), 4.0, 0.95, 5.85, 4.15, 2210, 1955);
  s.addNotes(nota(["Diapositiva 3"]));
}

// 4. Escenarios y medidas
{
  const s = pres.addSlide({ masterName: "CONTENIDO" });
  titulo(s, "Escenarios y medidas", "Todos contra la situación actual (E0), con el mismo día y los mismos pasajeros");
  const cab = (t) => ({ text: t, options: { bold: true, color: COL.blanco, fill: { color: COL.lineaC } } });
  const filas = [
    [cab("Escenario"), cab("Molinetes"), cab("Validación (s)"), cab("Qué representa")],
    ["E0", "20", "Triangular (1,8; 2,4; 3,5)", "Situación actual"],
    ["E1", "22", "Triangular (1,8; 2,4; 3,5)", "Habilitar los 22 del vestíbulo"],
    ["E3", "20", "Triangular (1,5; 1,8; 2,5)", "Validación sin contacto (EMV/QR)"],
    ["E13", "22", "Triangular (1,5; 1,8; 2,5)", "Las dos medidas juntas"],
  ];
  s.addTable(filas, { x: 0.45, y: 1.35, w: 9.1, colW: [1.2, 1.2, 2.6, 4.1], fontFace: FUENTE, fontSize: 14,
    color: COL.tinta, border: { type: "solid", pt: 0.75, color: "D1D5DB" }, rowH: 0.38, valign: "middle" });
  s.addText("Medidas primarias", { x: 0.45, y: 3.45, w: 9.1, h: 0.35, fontFace: FUENTE, fontSize: 16, bold: true,
    color: COL.flujo, margin: 0 });
  vinetas(s, [
    "P90 de la espera en la franja (no la media: la media esconde la oleada)",
    "Proporción de pasajeros que esperan más de 30 s",
    "P90 de la espera de quienes llegan en el pico (08:15–08:45)",
  ], 0.45, 3.8, 9.1, 1.2, 14);
  s.addNotes(nota(["Diapositiva 4"]));
}

// 5. El modelo en funcionamiento (50 s en AnyLogic; la captura es el respaldo si algo falla)
{
  const s = pres.addSlide();
  s.background = { color: COL.noche };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.12, h: 5.625, fill: { color: COL.flujo } });
  s.addText("El modelo en funcionamiento", { x: 0.45, y: 0.25, w: 6, h: 0.6, fontFace: FUENTE, fontSize: 26,
    bold: true, color: COL.blanco, margin: 0 });
  s.addText("AnyLogic · PeatonalFranjaVisualE0 · ~50 s", { x: 0.45, y: 0.82, w: 6, h: 0.35, fontFace: FUENTE,
    fontSize: 14, color: "9FB0CC", margin: 0 });
  const pasos = ["Los 4 bloques: variables, medidas, lógica y simulación", "Llega un tren: bajan por las 21 puertas",
    "Cruzan el hall y bajan por las escaleras mecánicas", "Pasillo y oleada en los molinetes",
    "Panel en vivo: hora, cola, P90", "Mapa de calor: dónde se acumula la gente"];
  s.addText(pasos.map((t, i) => ({ text: `${i + 1}  ${t}`, options: { breakLine: i < pasos.length - 1, paraSpaceAfter: 9 } })),
    { x: 0.45, y: 1.45, w: 3.9, h: 3.6, fontFace: FUENTE, fontSize: 14, color: COL.blanco, valign: "top", margin: 0 });
  const captura = fig("tpi-subte-modelo-espacial.png");
  if (existe(captura)) { const { w, h } = tamPng(captura); imagen(s, captura, 4.6, 0.3, 5.1, 4.9, w, h); }
  else s.addText("Respaldo: poner acá una captura del modelo corriendo\n(materias/SIM/figs/tpi-subte-modelo-espacial.png)",
    { x: 4.6, y: 0.9, w: 5.0, h: 3.8, fontFace: FUENTE, fontSize: 13, color: "9FB0CC", align: "center", valign: "middle",
      line: { color: "9FB0CC", dashType: "dash", width: 1 } });
  s.addNotes(nota(["Diapositiva 5"]));
}

// 6. Resultados
{
  const s = pres.addSlide({ masterName: "CONTENIDO" });
  const n = val("nPares", "[N]");
  titulo(s, "Resultados", `${n} días por escenario · números aleatorios comunes · t apareado con Bonferroni (k = 9)`);
  const cab = (t) => ({ text: t, options: { bold: true, color: COL.blanco, fill: { color: COL.lineaC }, align: "center" } });
  const esc = [["E0", "EO"], ["E1", "EI"], ["E3", "ET"], ["E13", "EIT"]];
  const filas = [[cab("Escenario"), cab("P90 espera (s)"), cab("Espera > 30 s"), cab("Δ P90 vs E0 [IC 99,4 %]")]];
  for (const [nom, k] of esc) {
    const prop = val(`propTreinta${k}`);
    const propPct = /\d/.test(prop) ? `${(parseFloat(prop.replace("−", "-").replace(",", ".")) * 100).toFixed(1).replace(".", ",").replace("-", "−")} %` : prop;
    const dif = k === "EO" ? "—" : !V ? "[pendiente]" : `${val(`difPNoventa${k}`)} s [${val(`icInfPNoventa${k}`)}; ${val(`icSupPNoventa${k}`)}]`;
    const ver = k === "EO" ? "" : val(`veredictoPNoventa${k}`, "");
    const colVer = ver === "mejora" ? COL.verde : ver === "empeora" ? COL.rojo : COL.tinta;
    filas.push([{ text: nom, options: { bold: true } }, { text: val(`pNoventa${k}`), options: { align: "center" } },
      { text: propPct, options: { align: "center" } }, { text: dif, options: { align: "center", color: colVer, bold: !!ver } }]);
  }
  const forest = fig("tpi-subte-res-forest.png");
  const conFig = existe(forest);
  s.addTable(filas, { x: 0.45, y: 1.35, w: conFig ? 5.3 : 9.1, colW: conFig ? [0.9, 1.15, 1.15, 2.1] : [1.5, 2.0, 2.0, 3.6],
    fontFace: FUENTE, fontSize: conFig ? 12 : 15, color: COL.tinta, border: { type: "solid", pt: 0.75, color: "D1D5DB" },
    rowH: 0.42, valign: "middle" });
  if (conFig) {
    const { w, h } = tamPng(forest);
    imagen(s, forest, 5.9, 1.25, 3.7, 3.7, w, h);
  }
  if (!V) s.addText("PENDIENTE: correr resultados_informe.py con la producción y volver a generar esta presentación",
    { x: 0.45, y: 3.7, w: 9.1, h: 0.5, fontFace: FUENTE, fontSize: 13, color: COL.rojo, bold: true, margin: 0 });
  else s.addText("Verde: el intervalo queda entero por debajo de 0 (mejora con evidencia estadística).",
    { x: 0.45, y: 3.65, w: conFig ? 5.3 : 9.1, h: 0.6, fontFace: FUENTE, fontSize: 12, color: COL.gris, margin: 0 });
  s.addNotes(nota(["Diapositiva 6"]));
}

// 7. Conclusión y alcance
{
  const s = pres.addSlide({ masterName: "CONTENIDO" });
  titulo(s, "Conclusión y alcance");
  s.addShape(pres.shapes.RECTANGLE, { x: 0.45, y: 1.05, w: 9.1, h: 1.5, fill: { color: COL.hall }, line: { color: COL.hall } });
  s.addText(RECOMENDACION || "[PENDIENTE: recomendación según la regla de decisión, con los intervalos de la producción]",
    { x: 0.65, y: 1.1, w: 8.7, h: 1.4, fontFace: FUENTE, fontSize: 18, bold: true,
      color: RECOMENDACION ? COL.tinta : COL.rojo, valign: "middle", margin: 0 });
  s.addText("Vale dentro de estos supuestos", { x: 0.45, y: 2.75, w: 9.1, h: 0.35, fontFace: FUENTE, fontSize: 16,
    bold: true, color: COL.flujo, margin: 0 });
  vinetas(s, [
    "La espera real no está medida: la comparación entre escenarios es más sólida que los valores absolutos",
    "80 % de las validaciones viene del Roca (supuesto; no identificable con los datos)",
    "Validación sin contacto: extremo rápido del rango técnico, no medido",
    "Subsuelo sin plano oficial; el modelo reparte la carga entre molinetes más parejo que la realidad",
  ], 0.45, 3.1, 9.1, 1.9, 14);
  s.addNotes(nota(["Diapositiva 7"]));
}

function tamPng(p) {
  const b = fs.readFileSync(p);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
}

pres.writeFile({ fileName: SALIDA }).then(() => {
  console.log(`listo: ${SALIDA}`);
  console.log(V ? `resultados desde valores.tex (${V.nPares} pares)` : "SIN resultados: diapositivas 6 y 7 pendientes");
  console.log(`notas: ${GUION.length} secciones del guion`);
});
