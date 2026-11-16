/**
 * diagramas.js — SVG de los diagramas del informe UTNHub.
 * El markdown los pide con {{diagrama:nombre|pie}} y build.js los reemplaza.
 */
const AZUL = '#0F4761', AZUL2 = '#156082', CELESTE = '#1CA4DF', TINTA = '#1b1f24',
  GRIS = '#5b6470', LINEA = '#9fb3c2', FONDO = '#f2f6f9', BLANCO = '#ffffff';
const FONT = `font-family="Aptos, 'Segoe UI', Arial, sans-serif"`;
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

/* ───────── primitivas ───────── */
function defs() {
  return `<defs>
<marker id="fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="${AZUL2}"/></marker>
</defs>`;
}
function caja(x, y, w, h, { titulo, lineas = [], fill = BLANCO, borde = AZUL2, cab = AZUL, tc = BLANCO, size = 9.5 } = {}) {
  let s = `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="5" fill="${fill}" stroke="${borde}" stroke-width="1.1"/>`;
  if (titulo) {
    s += `<path d="M${x},${y + 5} a5,5 0 0 1 5,-5 h${w - 10} a5,5 0 0 1 5,5 v13 h-${w} z" fill="${cab}"/>`;
    s += `<text x="${x + w / 2}" y="${y + 13}" text-anchor="middle" font-size="10" font-weight="700" fill="${tc}" ${FONT}>${esc(titulo)}</text>`;
  }
  lineas.forEach((l, i) => {
    const bold = l.startsWith('*');
    s += `<text x="${x + 7}" y="${y + (titulo ? 31 : 15) + i * 12.5}" font-size="${size}" ${bold ? 'font-weight="700"' : ''} fill="${TINTA}" ${FONT}>${esc(bold ? l.slice(1) : l)}</text>`;
  });
  return s;
}
function texto(x, y, t, { size = 9, fill = GRIS, anchor = 'middle', bold = false, italic = false } = {}) {
  return `<text x="${x}" y="${y}" text-anchor="${anchor}" font-size="${size}" fill="${fill}" ${bold ? 'font-weight="700"' : ''} ${italic ? 'font-style="italic"' : ''} ${FONT}>${esc(t)}</text>`;
}
function flecha(pts, { dash = false, color = AZUL2, ambas = false } = {}) {
  const d = pts.map((p, i) => `${i ? 'L' : 'M'}${p[0]},${p[1]}`).join(' ');
  return `<path d="${d}" fill="none" stroke="${color}" stroke-width="1.2" ${dash ? 'stroke-dasharray="4 3"' : ''} marker-end="url(#fl)" ${ambas ? 'marker-start="url(#fl)"' : ''}/>`;
}
function linea(pts, { color = AZUL2 } = {}) {
  const d = pts.map((p, i) => `${i ? 'L' : 'M'}${p[0]},${p[1]}`).join(' ');
  return `<path d="${d}" fill="none" stroke="${color}" stroke-width="1.1"/>`;
}
const svg = (w, h, inner) =>
  `<svg viewBox="0 0 ${w} ${h}" width="100%" xmlns="http://www.w3.org/2000/svg">${defs()}${inner}</svg>`;

/* ───────── 1. arquitectura ───────── */
function arquitectura() {
  let s = '';
  // usuario
  s += caja(6, 52, 92, 56, { lineas: ['*Alumno', 'navegador', 'web o celular'], fill: FONDO });
  // frontend
  s += caja(122, 20, 150, 120, { titulo: 'Frontend · Next.js 15', lineas: ['React 18 + Tailwind', 'App Router (SSR)', 'Proxy /api/backend/*', 'Sesión: cookie httpOnly', 'Streaming SSE del chat', 'Railway'] });
  s += flecha([[98, 80], [122, 80]]);
  // backend con capas
  s += `<rect x="298" y="8" width="214" height="314" rx="6" fill="${FONDO}" stroke="${AZUL}" stroke-width="1.3"/>`;
  s += texto(405, 22, 'Backend · FastAPI (Python 3.12) · Railway', { size: 9.5, fill: AZUL, bold: true });
  s += caja(308, 30, 194, 62, { titulo: 'Presentación — api/', lineas: ['12 routers REST + SSE', 'deps: usuario, admin', 'Pydantic (schemas/)'], cab: AZUL2 });
  s += caja(308, 102, 194, 102, { titulo: 'Negocio', lineas: ['services/ — reglas del dominio', 'agent/ — LangGraph, 10 tools', 'rag/ — chunker, embeddings,', '        retriever', 'ai/ — clasificador de novedades', 'workers/ — scheduler'], cab: AZUL2 });
  s += caja(308, 214, 194, 98, { titulo: 'Datos', lineas: ['repositories/ — 9 repositorios', 'db/models — SQLAlchemy 2.0', 'alembic — 31 migraciones', 'scrapers/ — sitio, PDFs, Drive,', '        Instagram, UTNTAC'], cab: AZUL2 });
  s += flecha([[405, 92], [405, 102]]);
  s += flecha([[405, 204], [405, 214]]);
  s += flecha([[272, 60], [308, 60]], { ambas: true });
  // externos
  s += caja(540, 214, 134, 62, { titulo: 'Neon', lineas: ['PostgreSQL serverless', '+ pgvector (768 dim)', 'índice HNSW coseno'], cab: '#2b6a3f', borde: '#2b6a3f' });
  s += flecha([[502, 250], [540, 250]], { ambas: true });
  s += caja(540, 102, 134, 50, { titulo: 'Google Gemini', lineas: ['LLM del agente', 'gemini-embedding-001'], cab: '#5b3f8c', borde: '#5b3f8c' });
  s += flecha([[502, 128], [540, 128]]);
  s += caja(540, 160, 134, 44, { titulo: 'OpenAI', lineas: ['gpt-4o-mini (clasificador)'], cab: '#5b3f8c', borde: '#5b3f8c' });
  s += flecha([[502, 182], [540, 182]]);
  s += caja(540, 30, 134, 50, { titulo: 'Google OAuth 2.0', lineas: ['code flow + PKCE', 'id_token vs. JWKS'], cab: '#8a5a12', borde: '#8a5a12' });
  s += flecha([[502, 55], [540, 55]], { ambas: true });
  // AWS
  s += `<rect x="122" y="346" width="390" height="78" rx="6" fill="#fff8ef" stroke="#b9782a" stroke-width="1.2"/>`;
  s += texto(132, 360, 'AWS — ingesta de novedades', { size: 9.5, fill: '#8a5a12', bold: true, anchor: 'start' });
  s += caja(132, 368, 88, 46, { lineas: ['*EventBridge', 'web: cada 7 d', 'IG: cada 6 h'], borde: '#b9782a' });
  s += flecha([[220, 391], [240, 391]], { color: '#b9782a' });
  s += caja(240, 368, 140, 46, { lineas: ['*2 Lambdas (contenedor)', 'utnhub-ingesta-utn-web', 'utnhub-ingesta-instagram'], borde: '#b9782a' });
  s += flecha([[380, 391], [400, 391]], { color: '#b9782a' });
  s += caja(400, 368, 102, 46, { lineas: ['*S3', 'copia de imágenes', 'de las novedades'], borde: '#b9782a' });
  s += flecha([[310, 368], [310, 336], [526, 336], [526, 266], [540, 266]], { color: '#b9782a', dash: true });
  s += texto(420, 332, 'escribe novedades + log de auditoría', { size: 8, fill: '#8a5a12' });
  // fuentes
  s += caja(540, 290, 134, 78, { titulo: 'Fuentes públicas', lineas: ['frro.utn.edu.ar', 'Instagram (centros)', 'PDFs y Drive', 'planillas UTNTAC'], cab: GRIS, borde: GRIS });
  s += flecha([[540, 300], [512, 300]], { dash: true, color: GRIS });
  return svg(680, 430, s);
}

/* ───────── 2. dominio académico ───────── */
function dominioAcademico() {
  let s = '';
  const B = {};
  const box = (id, x, y, w, titulo, attrs) => {
    const h = 22 + attrs.length * 12.5 + 5;
    B[id] = { x, y, w, h };
    s += caja(x, y, w, h, { titulo, lineas: attrs, size: 8.8 });
  };
  // alturas reales: 1 atributo → 39.5, 2 → 52, 4 → 77
  box('usuario', 8, 8, 150, 'Usuario', ['id · email · nombre · apellido', 'legajo · rol', 'password (bcrypt) · google_sub', 'calendario_token · anio_ingresado']);
  box('um', 200, 8, 150, 'UsuarioMateria', ['condicion: aprobado | regular |', '   cursando | libre', 'nota · anio_cursada', 'cursada_id (opcional)']);
  box('materia', 392, 8, 140, 'Materia', ['codigo (PK) · nombre', 'anio_carrera · cuatrimestre', 'horas · creditos', 'tipo: troncal | electiva']);
  box('corr', 560, 8, 112, 'Correlatividad', ['materia_codigo', 'materia_requerida', 'tipo: regular |', '   aprobada']);
  box('mesa', 560, 122, 112, 'MesaMateria', ['dia_semana · hora', 'nota · origen']);
  box('comision', 200, 150, 150, 'Comision', ['nombre (1K01, 4EK02…)', 'anio']);
  box('cursada', 392, 150, 140, 'Cursada', ['cuatrimestre · docente', 'profesor_id (opcional)']);
  box('mp', 8, 262, 150, 'MateriaProfesor', ['materia_codigo · cargo · anio']);
  box('profesor', 200, 262, 150, 'Profesor', ['nombre · email', 'nombre_key (único)']);
  box('horario', 392, 262, 140, 'Horario', ['dia · hora_inicio · hora_fin', 'aula']);
  box('evento', 560, 250, 112, 'EventoCalendario', ['titulo · tipo', 'fecha_inicio · fecha_fin', 'content_hash (único)', 'usuario_id (opcional)']);
  box('hc', 8, 358, 150, 'HorarioConsulta', ['dia · hora · modalidad · aula']);
  box('review', 200, 358, 150, 'ReviewCatedra (UTNTAC)', ['votos en 5 niveles', 'cantidad_respuestas']);
  box('resena', 392, 358, 140, 'ResenaAlumno', ['nivel 1–5 · comentario']);
  box('dia', 560, 358, 112, 'EstadoDia', ['fecha · se_cursa', 'motivo']);

  const lab = (x, y, t, a = 'middle') => { s += texto(x, y, t, { size: 8.5, fill: AZUL, bold: true, anchor: a }); };
  const nota = (x, y, t) => { s += texto(x, y, t, { size: 7.5, italic: true }); };
  // Usuario 1—N UsuarioMateria N—1 Materia
  s += linea([[158, 46], [200, 46]]); lab(163, 42, '1', 'start'); lab(196, 42, 'N', 'end');
  s += linea([[350, 46], [392, 46]]); lab(355, 42, 'N', 'start'); lab(388, 42, '1', 'end');
  // Materia — Correlatividad: la que exige y la exigida
  s += linea([[532, 34], [560, 34]]); lab(536, 30, '1', 'start'); lab(557, 30, 'N', 'end');
  s += linea([[532, 64], [560, 64]]); lab(536, 60, '1', 'start'); lab(557, 60, 'N', 'end');
  nota(616, 96, 'requiere (autorrelación)');
  // Materia 1 — 0..1 MesaMateria
  s += linea([[505, 85], [505, 108], [616, 108], [616, 122]]); lab(510, 98, '1', 'start'); lab(621, 119, '0..1', 'start');
  // Materia 1—N Cursada
  s += linea([[450, 85], [450, 150]]); lab(455, 98, '1', 'start'); lab(455, 146, 'N', 'start');
  // Comision 1—N Cursada
  s += linea([[350, 176], [392, 176]]); lab(355, 172, '1', 'start'); lab(388, 172, 'N', 'end');
  // UsuarioMateria N — 0..1 Cursada (comisión elegida)
  s += linea([[300, 85], [300, 128], [420, 128], [420, 150]], { color: LINEA }); lab(305, 98, 'N', 'start'); lab(425, 146, '0..1', 'start');
  nota(360, 124, 'comisión elegida');
  // Cursada 1—N Horario
  s += linea([[495, 202], [495, 262]]); lab(500, 214, '1', 'start'); lab(500, 258, 'N', 'start');
  // Profesor 0..1 — N Cursada (docente)
  s += linea([[350, 280], [372, 280], [372, 192], [392, 192]], { color: LINEA }); lab(355, 276, '0..1', 'start'); lab(388, 188, 'N', 'end');
  // Profesor 1—N MateriaProfesor / HorarioConsulta / ReviewCatedra / ResenaAlumno
  s += linea([[200, 282], [158, 282]]); lab(196, 278, '1', 'end'); lab(162, 278, 'N', 'start');
  s += linea([[215, 314], [215, 336], [83, 336], [83, 358]]); lab(220, 326, '1', 'start'); lab(88, 354, 'N', 'start');
  s += linea([[275, 314], [275, 358]]); lab(280, 326, '1', 'start'); lab(280, 354, 'N', 'start');
  s += linea([[335, 314], [335, 336], [462, 336], [462, 358]]); lab(340, 326, '1', 'start'); lab(467, 354, 'N', 'start');
  // Usuario 1—N ResenaAlumno (por el margen izquierdo y abajo)
  s += linea([[30, 85], [30, 134], [3, 134], [3, 412], [462, 412], [462, 397.5]], { color: LINEA }); lab(35, 98, '1', 'start'); lab(467, 408, 'N', 'start');
  // Usuario 1—N EventoCalendario (eventos personales)
  s += linea([[120, 85], [120, 112], [180, 112], [180, 232], [616, 232], [616, 250]], { color: LINEA }); lab(125, 98, '1', 'start'); lab(621, 246, 'N', 'start');
  nota(300, 228, 'eventos personales (usuario_id); NULL = institucional');
  return svg(680, 420, s);
}

/* ───────── 3. dominio de contenido: chat, novedades, RAG ───────── */
function dominioContenido() {
  let s = '';
  s += caja(8, 8, 140, 52, { titulo: 'Usuario', lineas: ['(ver modelo académico)'], size: 8.8 });
  s += caja(190, 8, 150, 52, { titulo: 'Conversacion', lineas: ['titulo · created_at'], size: 8.8 });
  s += caja(382, 8, 150, 78, { titulo: 'Mensaje', lineas: ['role · contenido · tokens', 'fuentes_json (citas)', 'tools_json (tools usadas)'], size: 8.8 });
  s += caja(560, 8, 112, 52, { titulo: 'ChatFeedback', lineas: ['util · motivo'], size: 8.8 });
  const lab = (x, y, t, a = 'middle') => { s += texto(x, y, t, { size: 8.5, fill: AZUL, bold: true, anchor: a }); };
  s += linea([[148, 34], [190, 34]]); lab(154, 30, '1', 'start'); lab(185, 30, 'N', 'end');
  s += linea([[340, 34], [382, 34]]); lab(346, 30, '1', 'start'); lab(377, 30, 'N', 'end');
  s += linea([[532, 34], [560, 34]]); lab(537, 30, '1', 'start'); lab(556, 30, 'N', 'end');

  s += caja(8, 116, 170, 104, { titulo: 'Novedad', lineas: ['titulo · descripcion · contenido', 'categoria: evento | aviso |', '   noticia | general', 'estado: publicada | pendiente |', '   descartada · confianza', 'moderado_manual · orden_portada'], size: 8.8 });
  s += caja(222, 116, 150, 66, { titulo: 'NovedadFuente', lineas: ['external_id (único)', 'url · imagen · fecha'], size: 8.8 });
  s += caja(416, 116, 116, 66, { titulo: 'Centro', lineas: ['handle · nombre', 'tipo · url_perfil'], size: 8.8 });
  s += linea([[178, 140], [222, 140]]); lab(184, 136, '1', 'start'); lab(217, 136, 'N', 'end');
  s += linea([[372, 140], [416, 140]]); lab(378, 136, 'N', 'start'); lab(411, 136, '1', 'end');
  s += texto(290, 198, 'una novedad puede venir de varias cuentas', { size: 7.5, italic: true });

  s += caja(560, 116, 112, 104, { titulo: 'IngestaLog', lineas: ['fuente', 'iniciado / finalizado', 'items vistos / nuevos', 'descartados', 'tokens_usados', 'estado · errores'], size: 8.8 });
  s += caja(222, 236, 310, 52, { titulo: 'RagChunk', lineas: ['contenido · embedding vector(768) · fuente · url · titulo · chunk_index'], size: 8.8 });
  s += texto(377, 304, 'corpus del asistente: índice HNSW por distancia coseno', { size: 7.5, italic: true });
  return svg(680, 312, s);
}

/* ───────── 4. pipeline de novedades ───────── */
function pipelineNovedades() {
  let s = '';
  const pasos = [
    ['1. Scraping', 'sitio FRRO e', 'Instagram (sin', 'credenciales)'],
    ['2. Filtro previo', 'dedup exacta por', 'external_id · >90 d', 'afuera · máx. 40'],
    ['3. Clasificación', 'gpt-4o-mini con', 'salida JSON y', 'visión de la imagen'],
    ['4. Dedup semántica', 'compara contra las', '30 más recientes', '→ suma una fuente'],
    ['5. Publicación', 'confianza ≥ 0,75', '→ publicada; si no,', 'pendiente (admin)'],
  ];
  const w = 122, g = 14;
  pasos.forEach((p, i) => {
    const x = 6 + i * (w + g);
    s += caja(x, 10, w, 78, { titulo: p[0], lineas: p.slice(1), size: 8.8 });
    if (i) s += flecha([[x - g, 49], [x, 49]]);
  });
  s += `<rect x="6" y="104" width="671" height="30" rx="5" fill="${FONDO}" stroke="${LINEA}"/>`;
  s += texto(341, 123, 'Cada corrida deja una fila en IngestaLog (fuente, inicio y fin, ítems vistos/nuevos/descartados, tokens, errores) · imágenes copiadas a S3', { size: 8.6, fill: TINTA });
  return svg(684, 140, s);
}

/* ───────── 5. agente ───────── */
function agente() {
  let s = '';
  s += caja(6, 40, 110, 58, { lineas: ['*Pregunta', 'en lenguaje natural', '+ últimos 10 msj.'], fill: FONDO });
  s += flecha([[116, 69], [146, 69]]);
  s += caja(146, 30, 130, 78, { titulo: 'Nodo agente', lineas: ['Gemini, temperatura 0', 'prompt: no inventar,', 'citar fuentes, fecha', 'de hoy inyectada'] });
  s += caja(326, 6, 200, 128, { titulo: 'ToolNode — 10 tools', lineas: ['rag_search · ficha_materia', 'buscar_correlativas', 'buscar_horario_comision', 'buscar_profesor · mesas_de_examen', 'proximos_eventos · ultimas_novedades', 'mi_progreso_academico', 'plan_de_estudio'] });
  s += flecha([[276, 55], [326, 55]]);
  s += flecha([[326, 90], [276, 90]]);
  s += texto(301, 49, 'llama', { size: 7.5, italic: true });
  s += texto(301, 104, 'resultado', { size: 7.5, italic: true });
  s += caja(560, 30, 116, 78, { lineas: ['*Respuesta (SSE)', 'tokens en vivo', 'pasos del agente', 'fuentes citadas', 'fichas de materia'], fill: FONDO });
  s += flecha([[211, 108], [211, 166], [618, 166], [618, 108]]);
  s += texto(300, 162, 'sin más tools que llamar (máx. 8 iteraciones)', { size: 7.5, italic: true });
  s += texto(434, 151, 'consultan services/ y pgvector', { size: 8, fill: GRIS, anchor: 'start' });
  s += flecha([[426, 134], [426, 154]], { dash: true, color: GRIS });
  return svg(682, 178, s);
}

module.exports = {
  arquitectura, 'dominio-academico': dominioAcademico, 'dominio-contenido': dominioContenido,
  'pipeline-novedades': pipelineNovedades, agente,
};
