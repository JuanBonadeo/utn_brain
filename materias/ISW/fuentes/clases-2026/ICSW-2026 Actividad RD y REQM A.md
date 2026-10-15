Caso de trabajo · Inscripción universitaria

Actividad grupal de ingeniería de requisitos  |  CMMI-DEV v1.2 · RD y REQM

Material de partida para los estudiantes. Las declaraciones siguientes son información inicial de relevamiento,
NO requisitos ya validados.

1. Contexto del proyecto
La Universidad del Saber Eterno utiliza un sistema académico para registrar alumnos, materias, correlatividades
y calificaciones. Actualmente, las inscripciones se realizan mediante formularios y correos electrónicos que
luego procesa Secretaría Académica. La universidad quiere incorporar un portal web de inscripción a materias,
integrado con el sistema existente, antes del próximo cuatrimestre.

El proyecto incluye consulta de oferta, solicitud de inscripción y respuesta al alumno. El equipo deberá
determinar reglas, excepciones, información requerida y límites del alcance. No se ha seleccionado todavía una
solución técnica definitiva.

2. Voces de los interesados (relevamiento inicial)

Alumnos




“Quiero anotarme desde mi casa o el celular, sin ir a la facultad.”
“Antes de confirmar, necesito ver materias, comisiones, días, horarios y cupos.”
“Si no me puedo anotar, quiero entender por qué. A veces el sistema me marca una materia como pendiente
aunque rendí hace poco.”
“Si la materia está llena, me gustaría quedar en lista de espera y enterarme si aparece un lugar.”

Secretaría Académica



“Nadie debería inscribirse si no cumple las correlatividades del plan de estudios vigente.”
“Las inscripciones dependen de las fechas oficiales y los cupos por comisión. Necesitamos poder configurar
ambos.”
“En situaciones justificadas podemos autorizar excepciones; no deberían resolverse automáticamente.”
“Necesitamos consultar quién se inscribió, cuándo y qué validaciones se realizaron.”

Docentes y responsables de cátedra




“No queremos recibir más alumnos que la capacidad permitida para la comisión.”
“La nómina de inscriptos debe estar disponible antes del inicio del cursado.”
“Si un alumno cambia de comisión, necesitamos que la nómina se actualice.”

Área de Sistemas / Infraestructura


“El sistema académico existente conserva la información oficial; no conviene duplicar datos sin definir cómo
se sincronizan.”
“En la apertura de inscripciones ingresan miles de alumnos a la vez. La solución no debe bloquear el sistema
académico.”
“Hay que definir autenticación, permisos, auditoría y qué sucede si falla la comunicación con el sistema
académico.”










Actividad de aula · RD / REQM · Caso ficticio para análisis y discusión

Autoridades universitarias


“El portal debe estar operativo para el próximo período de inscripción, con el presupuesto y equipo
disponibles.”
“La experiencia del alumno debe mejorar y deben disminuir las consultas y reclamos en Secretaría.”



3. Datos para analizar


La universidad estima 3.000 alumnos conectados durante los primeros 30 minutos de apertura; la cifra no
está validada técnicamente.

  Algunos actores entienden “correlativa aprobada” como examen final aprobado; otros mencionan

regularidad de cursado. Las reglas dependen del plan de estudios.

  Secretaría afirma que no deben admitirse inscripciones sin requisitos; también indica que puede autorizar





excepciones.
Los alumnos esperan confirmación inmediata, pero Sistemas advierte posibles demoras o caídas del
sistema académico.
Todavía no se decidió si lista de espera, cambios de comisión y notificaciones estarán incluidos en la
primera versión.

4. Consigna de trabajo en grupos
A partir del caso, seleccionen UNA necesidad central y desarrollen 1 o 2 requisitos del cliente (RC). A partir de
ellos, deriven los requisitos del producto (RP) necesarios para describir el comportamiento del sistema, sin
pretender especificar toda la solución. Cuando corresponda, incluyan requisitos de interfaces (RI) y derivados de
decisiones técnicas (RD). No confundan la sigla RD usada como identificador de un requisito derivado con el
área de proceso Requirements Development.

Parte A · Desarrollo de requisitos (área RD)

Práctica

SG1 · SP 1.1 / 1.2

SG2 · SP 2.1 / 2.2 / 2.3

SG3 · SP 3.1 / 3.2

SG3 · SP 3.3 / 3.4 / 3.5

Parte B · Gestión de requisitos (área REQM)

Práctica

SP 1.1 · Entendimiento

SP 1.2 · Compromiso

Qué debe hacer el grupo / evidencia mínima

Identificar interesados, distinguir necesidades de
soluciones propuestas, registrar preguntas
pendientes y redactar 1–2 RC claros y verificables.

Derivar RP de los RC, proponer funciones y
componentes responsables e identificar al menos
una interfaz relevante y sus datos/condiciones.

Describir un escenario normal y uno alternativo/de
error; identificar funciones y secuencia de
operaciones.

Detectar ambigüedad o conflicto, analizar factibilidad
y compromiso entre atributos, y proponer cómo
validar los requisitos con stakeholders.

Qué debe hacer el grupo / evidencia mínima

Definir quién aclara y quién acepta cada RC; registrar
al menos dos preguntas y las respuestas que deben
confirmarse.

Explicar qué participantes deben acordar la
implementación y qué impacto estiman en plazo,

Actividad de aula · RD / REQM · Caso ficticio para análisis y discusión

SP 1.3 · Cambios

SP 1.4 · Trazabilidad

SP 1.5 · Inconsistencias

esfuerzo o riesgo.

Proponer un registro de solicitud de cambio, su
justificación, análisis de impacto y decisión.

Dibujar relaciones RC → RP → función/componente →
caso de prueba y mostrar cómo seguirlas en sentido
inverso.

Inventar una inconsistencia entre requisito vigente y
diseño, código o prueba; indicar cómo detectarla y
corregirla.

Actividad de aula · RD / REQM · Caso ficticio para análisis y discusión


