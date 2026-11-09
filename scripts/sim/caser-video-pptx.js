// Presentación de apoyo para el video del TPI Caser (Simulación 2026). Se importa a Google Slides.
// Uso, desde la raíz del repo:  node scripts/sim/caser-video-pptx.js
// Sale en materias/SIM/entregables/TPI/caser/video/TPI_Caser_Video.pptx, con el guion de cada integrante en las notas.
const path = require("path");
const pptxgen = require("pptxgenjs");
const { applyTheme } = require(path.join(process.env.USERPROFILE || "", ".claude/skills/synced/a66da44a-ad40-488b-8227-7a38fa69d614_7b945559-ddfe-4c63-a4d3-f2712b1105c5/pptx/scripts/apply_theme.js"));

const RAIZ = path.resolve(__dirname, "..", "..");
const SIM = path.join(RAIZ, "materias", "SIM");
const SALIDA = path.join(SIM, "entregables", "TPI", "caser", "video", "TPI_Caser_Video.pptx");

const THEME = {
  name: "Caser horno",
  headFontFace: "Calibri",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1F2733", lt1: "FFFFFF", dk2: "1D2B45", lt2: "F3F4F6",
    accent1: "EB5A32", accent2: "F59678", accent3: "15803D", accent4: "2A78D6", accent5: "FFA53C", accent6: "6B7480",
    hlink: "2A78D6", folHlink: "6B7480",
  },
};
const HEX = THEME.colors;
// Estados del horno, los mismos colores de la animación
const ESTADOS = [["Apagado", "C8CCD2"], ["Acumulando", "F0DC82"], ["Calentando", "FFA53C"], ["Procesando", "EB5A32"],
  ["Caliente sin carga", "F59678"], ["Enfriando", "96B4E6"]];

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9"; // 10 x 5.625 in
pres.title = "TPI Caser · ¿Cuándo encender el horno?";
pres.author = "Brizio, Casermeiro, Constantini, Messina, Navos";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
const C = pres.SchemeColor;

pres.defineSlideMaster({
  title: "OSCURA",
  background: { color: HEX.dk2 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 1.25, w: 8.8, h: 1.0, fontSize: 40, bold: true, color: C.background1, align: "left", valign: "bottom", margin: 0 }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "CONTENIDO",
  background: { color: HEX.lt1 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.3, w: 9.0, h: 0.7, fontSize: 30, bold: true, color: C.text2, align: "left", valign: "middle", margin: 0 }, text: "" } },
  ],
  slideNumber: { x: 9.2, y: 5.2, w: 0.4, h: 0.25, fontSize: 10, color: HEX.accent6, align: "right" },
});

function cinta(slide, x, y, w, h, conLeyenda, sobreOscuro) {
  // Mini "cinta de tiempo": una campaña típica, con los colores de los estados.
  const tramos = [[1, 6], [1, 18], [2, 6], [3, 30], [4, 10], [3, 6], [4, 8], [5, 10], [0, 6]];
  const total = tramos.reduce((a, t) => a + t[1], 0);
  let cx = x;
  tramos.forEach(([e, d], i) => {
    const tw = (w * d) / total;
    slide.addShape(pres.shapes.RECTANGLE, { x: cx, y, w: tw, h, fill: { color: ESTADOS[e][1] }, line: { color: ESTADOS[e][1], width: 0 }, objectName: `cinta${i}` });
    cx += tw;
  });
  if (!conLeyenda) return;
  let lx = x;
  ESTADOS.forEach(([n, col], i) => {
    slide.addShape(pres.shapes.RECTANGLE, { x: lx, y: y + h + 0.12, w: 0.14, h: 0.14, fill: { color: col }, line: { color: col, width: 0 }, objectName: `ley${i}` });
    slide.addText(n, { x: lx + 0.18, y: y + h + 0.06, w: 1.4, h: 0.26, fontSize: 10, color: sobreOscuro ? "C9D3E3" : HEX.accent6, margin: 0, isTextBox: true, objectName: `leyTxt${i}` });
    lx += 0.18 + 0.075 * n.length + 0.25;
  });
}

function circulo(slide, x, y, texto, color, nombre) {
  slide.addShape(pres.shapes.OVAL, { x, y, w: 0.46, h: 0.46, fill: { color }, line: { color, width: 0 }, objectName: nombre });
  slide.addText(texto, { x, y, w: 0.46, h: 0.46, fontSize: 15, bold: true, color: C.background1, align: "center", valign: "middle", margin: 0, isTextBox: true, objectName: nombre + "Txt" });
}

// ---------------------------------------------------------------- 1. Portada
pres.addSection({ title: "Presentación" });
let s = pres.addSlide({ masterName: "OSCURA", sectionTitle: "Presentación" });
s.addText("¿Cuándo encender el horno?", { placeholder: "title" });
s.addText("Simulación del régimen de campañas de un horno de cementación, con datos reales de una fábrica de tornillos",
  { x: 0.6, y: 2.35, w: 8.4, h: 0.7, fontSize: 18, color: "C9D3E3", margin: 0, isTextBox: true, objectName: "subtitulo" });
cinta(s, 0.6, 3.3, 8.8, 0.32, true, true);
s.addText("Augusto Brizio · Gonzalo Casermeiro · Jeremias Constantini · Tiziano Messina · Juan Ignacio Navos",
  { x: 0.6, y: 4.45, w: 8.8, h: 0.3, fontSize: 13, color: C.background1, margin: 0, isTextBox: true, objectName: "autores" });
s.addText("Grupo 10 · UTN · Facultad Regional Rosario · Simulación 2026", { x: 0.6, y: 4.8, w: 8.8, h: 0.3, fontSize: 11, color: "9AA8BF", margin: 0, isTextBox: true, objectName: "facultad" });
s.addNotes("JEREMIAS (0:00–0:30, diapositivas 1 y 2). Hola, somos el grupo 10 y vamos a presentar el caso de una fábrica de tornillos de Santa Fe: su horno de cementación y temple. Las piezas entran al horno en cajones de tornillos de unos 140 kilos, que en la planta llaman ULI.");

// ---------------------------------------------------------------- 2. El problema
s = pres.addSlide({ masterName: "CONTENIDO", sectionTitle: "Presentación" });
s.addText("Un horno que cuesta prender", { placeholder: "title" });
const stats = [["36 h", "calentando, sin poder cargar nada"], ["48 h", "enfriando después de la última carga"], ["≈ 100 kW", "caliente, aunque esté vacío"]];
stats.forEach(([v, t], i) => {
  const y = 1.25 + i * 1.2;
  s.addText(v, { x: 0.5, y, w: 2.3, h: 0.7, fontSize: 40, bold: true, color: C.accent1, margin: 0, valign: "middle", isTextBox: true, objectName: `stat${i}` });
  s.addText(t, { x: 2.85, y, w: 2.4, h: 0.7, fontSize: 15, color: C.text1, margin: 0, valign: "middle", isTextBox: true, objectName: `statTxt${i}` });
});
s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 5.6, y: 1.25, w: 3.9, h: 3.3, rectRadius: 0.15, fill: { color: HEX.dk2 }, line: { color: HEX.dk2, width: 0 }, objectName: "pregunta" });
s.addText([
  { text: "Hoy se prende con unas 79 ULI acumuladas y, si se vacía la cola, queda caliente hasta 48 h.", options: { fontSize: 14, color: "C9D3E3", breakLine: true } },
  { text: " ", options: { fontSize: 10, breakLine: true } },
  { text: "¿Cuántas ULI conviene esperar antes de encenderlo?", options: { fontSize: 22, bold: true, color: "FFFFFF" } },
], { x: 5.9, y: 1.5, w: 3.3, h: 2.8, valign: "top", margin: 0, isTextBox: true, objectName: "preguntaTxt" });
s.addNotes("JEREMIAS (sigue). El horno tarda 36 horas en calentarse y 48 en enfriarse, y caliente gasta luz y gas aunque esté vacío. Por eso se prende por campañas, cuando se juntan unas 80 ULI. La empresa nos preguntó: ¿cuántas conviene esperar antes de encenderlo?");

// ---------------------------------------------------------------- 3. Datos y modelo
pres.addSection({ title: "Modelo" });
s = pres.addSlide({ masterName: "CONTENIDO", sectionTitle: "Modelo" });
s.addText("Datos reales, modelo validado", { placeholder: "title" });
const cards = [
  ["1", "52 semanas reales", "Cada semana simulada sortea una semana real de lavado: se conservan los días vacíos y los picos.", HEX.accent4],
  ["2", "Facturas del horno", "Luz y gas por día caliente y por encendido, con regresiones sobre las facturas (R² 0,90 y 0,92).", HEX.accent1],
  ["3", "4 de 6", "medidas históricas dentro de la tolerancia: toneladas, duración de campaña, espera y kWh.", HEX.accent3],
];
cards.forEach(([n, h, t, col], i) => {
  const x = 0.5 + i * 3.05;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.2, w: 2.85, h: 2.05, rectRadius: 0.12, fill: { color: HEX.lt2 }, line: { color: "E3E6EA", width: 1 }, objectName: `card${i}` });
  circulo(s, x + 0.2, 1.38, n, col, `cardNum${i}`);
  s.addText(h, { x: x + 0.78, y: 1.38, w: 1.95, h: 0.46, fontSize: 17, bold: true, color: C.text2, margin: 0, valign: "middle", isTextBox: true, objectName: `cardH${i}` });
  s.addText(t, { x: x + 0.2, y: 1.98, w: 2.5, h: 1.15, fontSize: 13, color: C.text1, margin: 0, valign: "top", isTextBox: true, objectName: `cardT${i}` });
});
const bloques = [["Source", "lavado"], ["Wait", "cola"], ["Delay", "horno"], ["Sink", "salida"]];
s.addText("En AnyLogic (Process Modeling Library):", { x: 0.5, y: 3.55, w: 4.5, h: 0.3, fontSize: 12, bold: true, color: HEX.accent6, margin: 0, isTextBox: true, objectName: "pmlTitulo" });
bloques.forEach(([b, d], i) => {
  const x = 0.5 + i * 2.3;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 3.95, w: 1.75, h: 0.75, rectRadius: 0.1, fill: { color: "EEF3FD" }, line: { color: "C9D8F6", width: 1 }, objectName: `pml${i}` });
  s.addText([{ text: b, options: { bold: true, fontSize: 15, color: HEX.accent4, breakLine: true } }, { text: d, options: { fontSize: 12, color: HEX.accent6 } }],
    { x, y: 3.95, w: 1.75, h: 0.75, align: "center", valign: "middle", margin: 0, isTextBox: true, objectName: `pmlTxt${i}` });
  if (i < 3) s.addShape(pres.shapes.RIGHT_ARROW, { x: x + 1.85, y: 4.2, w: 0.35, h: 0.25, fill: { color: "AAB2BD" }, line: { color: "AAB2BD", width: 0 }, objectName: `flecha${i}` });
});
s.addNotes("AUGUSTO (0:30–1:05). Usamos datos reales de la empresa: un año de registros de cada ULI, con su fecha de lavado y su peso, y las facturas de luz y de gas del propio horno. Las llegadas no las inventamos: cada semana simulada sortea una de las 52 semanas reales. Con eso armamos un modelo de eventos discretos en AnyLogic y lo validamos contra el registro histórico: reproduce las toneladas por mes, la duración de las campañas, la espera y el consumo de energía.");

// ---------------------------------------------------------------- 4. AnyLogic
s = pres.addSlide({ masterName: "CONTENIDO", sectionTitle: "Modelo" });
s.addText("El modelo corriendo", { placeholder: "title" });
s.addImage({ path: path.join(SIM, "figs", "tpi-caser-visual.png"), x: 0.5, y: 1.1, w: 6.6, h: 3.71, altText: "Animación del modelo en AnyLogic", objectName: "captura" });
const items = [["Cola", "cada ULI, coloreada según cuánto espera; violeta = urgente"], ["Horno", "seis estados, del apagado al enfriado"],
  ["Plata", "costo en vivo y horas de horno caliente sin carga"]];
items.forEach(([h, t], i) => {
  const y = 1.15 + i * 1.2;
  s.addText([{ text: h, options: { bold: true, fontSize: 15, color: C.text2, breakLine: true } }, { text: t, options: { fontSize: 13, color: C.text1 } }],
    { x: 7.35, y, w: 2.2, h: 1.05, valign: "top", margin: 0, isTextBox: true, objectName: `item${i}` });
});
s.addNotes("GONZALO (1:05–1:45). Acá se pasa a AnyLogic en vivo; esta diapositiva queda de respaldo si algo falla. Este es el modelo en AnyLogic: por dentro es Source, Wait, Delay y Sink, y el horno tiene seis estados. Cada cuadradito es una ULI esperando; cambian de color según cuánto esperan, y el violeta es un pedido urgente, que obliga a prender el horno antes. Acá el horno calienta, y ahora carga una ULI cada 85 minutos. Cuando se vacía la cola, la regla actual lo deja caliente hasta 48 horas por si llega algo: es lo salmón de la cinta de tiempo. Si aplico el escenario E3, el horno se apaga en el momento.");

// ---------------------------------------------------------------- 5. Escenarios
pres.addSection({ title: "Resultados" });
s = pres.addSlide({ masterName: "CONTENIDO", sectionTitle: "Resultados" });
s.addText("Cuatro reglas, los mismos 30 años", { placeholder: "title" });
const esc = [["E0", "Regla actual", "enciende con 79 ULI; caliente sin carga hasta 48 h", HEX.accent6],
  ["E1", "Umbral bajo", "enciende con 45 ULI", HEX.accent4],
  ["E2", "Espera máxima", "79 ULI o 15 días la más vieja", HEX.accent5],
  ["E3", "Apagar enseguida", "se apaga apenas se vacía la cola", HEX.accent3]];
esc.forEach(([c, n, d, col], i) => {
  const x = 0.5 + i * 2.3;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.2, w: 2.1, h: 2.1, rectRadius: 0.12, fill: { color: HEX.lt2 }, line: { color: "E3E6EA", width: 1 }, objectName: `esc${i}` });
  circulo(s, x + 0.2, 1.38, c, col, `escNum${i}`);
  s.addText(n, { x: x + 0.2, y: 1.95, w: 1.75, h: 0.4, fontSize: 16, bold: true, color: C.text2, margin: 0, isTextBox: true, objectName: `escN${i}` });
  s.addText(d, { x: x + 0.2, y: 2.35, w: 1.75, h: 0.85, fontSize: 13, color: C.text1, margin: 0, valign: "top", isTextBox: true, objectName: `escD${i}` });
});
const met = [["30", "réplicas de un año por escenario"], ["mismos", "30 años para las cuatro reglas"], ["t apareado", "con Bonferroni (α = 0,05/3)"]];
met.forEach(([v, t], i) => {
  const x = 0.5 + i * 3.05;
  s.addText(v, { x, y: 3.6, w: 2.85, h: 0.6, fontSize: 28, bold: true, color: C.accent1, margin: 0, isTextBox: true, objectName: `met${i}` });
  s.addText(t, { x, y: 4.2, w: 2.85, h: 0.45, fontSize: 13, color: C.text1, margin: 0, isTextBox: true, objectName: `metTxt${i}` });
});
s.addNotes("TIZIANO (1:45–2:15). Comparamos cuatro reglas: la actual, bajar el umbral a 45 ULI, poner una espera máxima de 15 días y apagar el horno apenas se vacía la cola. Corrimos cada una 30 veces, un año simulado por corrida, y a las cuatro les tocaron los mismos 30 años, con las mismas llegadas. Así la única diferencia es la regla, y podemos comparar año contra año con un test t apareado, con corrección de Bonferroni.");

// ---------------------------------------------------------------- 6. Resultados
s = pres.addSlide({ masterName: "CONTENIDO", sectionTitle: "Resultados" });
s.addText("Apagar enseguida ahorra 18 M$ por año", { placeholder: "title" });
s.addChart(pres.charts.BAR, [{ name: "Costo relevante del año (M$)", labels: ["E0 actual", "E1 umbral 45", "E2 espera 15 d", "E3 apagar ya"], values: [83.7, 88.5, 86.5, 65.7] }], {
  x: 0.4, y: 1.1, w: 5.4, h: 3.9, barDir: "col",
  chartColors: ["9AA3AE", "C8CCD2", "C8CCD2", HEX.accent3],
  showTitle: true, title: "Costo relevante del año (M$, media de 30 réplicas)", titleFontSize: 12, titleColor: HEX.dk1, titleFontFace: "+mn-lt",
  showValue: true, dataLabelPosition: "outEnd", dataLabelFormatCode: "0.0", dataLabelFontSize: 12, dataLabelFontFace: "+mn-lt", dataLabelColor: HEX.dk1,
  catAxisLabelColor: HEX.accent6, valAxisLabelColor: HEX.accent6, catAxisLabelFontSize: 11, valAxisLabelFontSize: 10,
  catAxisLabelFontFace: "+mn-lt", valAxisLabelFontFace: "+mn-lt", valAxisMinVal: 0, valAxisMaxVal: 100,
  valGridLine: { color: "E3E6EA", size: 0.5 }, catGridLine: { style: "none" }, showLegend: false, barGapWidthPct: 60,
  objectName: "graficoCostos",
});
s.addTable([
  [{ text: "Contra E0", options: { bold: true, color: HEX.accent6 } }, { text: "Costo (M$/año)", options: { bold: true, color: HEX.accent6, align: "right" } }, { text: "Espera (días)", options: { bold: true, color: HEX.accent6, align: "right" } }],
  ["E1 umbral 45", { text: "+4,8 ± 1,7", options: { color: "B91C1C", align: "right" } }, { text: "−2,6 ± 0,4", options: { color: HEX.accent3, align: "right" } }],
  ["E2 espera 15 d", { text: "+2,9 ± 0,8", options: { color: "B91C1C", align: "right" } }, { text: "−1,0 ± 0,4", options: { color: HEX.accent3, align: "right" } }],
  [{ text: "E3 apagar ya", options: { bold: true } }, { text: "−18,0 ± 1,8", options: { bold: true, color: HEX.accent3, align: "right" } }, { text: "+1,1 ± 0,3", options: { color: "B91C1C", align: "right" } }],
], { x: 6.05, y: 1.3, w: 3.5, colW: [1.3, 1.15, 1.05], fontSize: 12, color: HEX.dk1, border: { type: "solid", pt: 0.5, color: "E3E6EA" }, rowH: 0.42, objectName: "tablaIC" });
s.addText("Intervalos al 98,3 % (Bonferroni). Ninguno contiene al cero: todas las diferencias son significativas. El ahorro de E3 se mantiene en todo el análisis de sensibilidad de precios.",
  { x: 6.05, y: 3.25, w: 3.5, h: 1.3, fontSize: 12, color: HEX.accent6, margin: 0, valign: "top", isTextBox: true, objectName: "notaIC" });
s.addNotes("JUAN IGNACIO (2:15–2:50, diapositivas 6 y 7). Bajar el umbral o poner una espera máxima reduce la espera, pero cuesta entre 3 y 5 millones de pesos más por año. Apagar el horno apenas se vacía la cola ahorra 18 millones por año, un 21 por ciento del costo, a cambio de un día más de espera promedio, y el resultado se mantiene aunque cambien los precios.");

// ---------------------------------------------------------------- 7. Conclusión
s = pres.addSlide({ masterName: "OSCURA", sectionTitle: "Resultados" });
s.addText("Recomendación", { placeholder: "title" });
s.addText("Mantener el umbral y apagar el horno apenas se vacía la cola", { x: 0.6, y: 2.35, w: 5.2, h: 1.0, fontSize: 22, bold: true, color: C.background1, margin: 0, valign: "top", isTextBox: true, objectName: "recomendacion" });
s.addText("Lo que cuesta no es esperar más o menos ULI: es el horno caliente sin nada adentro.", { x: 0.6, y: 3.45, w: 5.2, h: 0.8, fontSize: 14, color: "C9D3E3", margin: 0, valign: "top", isTextBox: true, objectName: "porque" });
s.addText("−21,5 %", { x: 6.1, y: 1.9, w: 3.4, h: 1.0, fontSize: 60, bold: true, color: "7DD3A0", align: "left", margin: 0, isTextBox: true, objectName: "ahorroPct" });
s.addText("del costo de operar el horno (≈ 18 M$ por año), con 1,1 días más de espera media", { x: 6.1, y: 2.95, w: 3.4, h: 0.9, fontSize: 13, color: "C9D3E3", margin: 0, valign: "top", isTextBox: true, objectName: "ahorroTxt" });
s.addText("Trabajo futuro: sumar la demanda y el nivel de servicio para ponerle precio a la espera.", { x: 0.6, y: 4.75, w: 8.8, h: 0.35, fontSize: 12, color: "9AA8BF", margin: 0, isTextBox: true, objectName: "futuro" });
s.addNotes("JUAN IGNACIO (sigue). Nuestra recomendación: mantener el umbral y no dejar el horno caliente esperando. Gracias.");

(async () => {
  await pres.writeFile({ fileName: SALIDA });
  await applyTheme(SALIDA, THEME);
  console.log(SALIDA);
})();
