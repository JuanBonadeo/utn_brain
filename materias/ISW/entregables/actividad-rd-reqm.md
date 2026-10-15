# Actividad RD y REQM — Inscripción universitaria

> Fuente de verdad del entregable. Se genera con
> `node scripts/build-docx.js materias/ISW/entregables/actividad-rd-reqm.md materias/ISW/entregables/actividad-rd-reqm.docx`.
> Enunciado: `fuentes/clases-2026/ICSW-2026 Actividad RD y REQM A.md`. Límite: 3 páginas.

---

## Grupo 34.584

**Integrantes:** Bonadeo Juan · Casermeiro Gonzalo · Conti Stéfano · Dana Agustín · Parmigiani Luis · Redaelli Martín

**Necesidad central:** que el alumno pueda inscribirse a materias en línea, dentro de las fechas oficiales, y sepa en el momento si quedó inscripto o por qué no.

## Parte A – Desarrollo de requisitos (área RD)

### SG1 · Interesados, necesidades y requisitos del cliente

**Interesados:** Alumnos · Secretaría Académica · Docentes y responsables de cátedra · Área de Sistemas · Autoridades.

<!-- cols: 34,33,33 -->

| Lo que dijo el interesado | Necesidad real | Solución propuesta (no es requisito todavía) |
|---|---|---|
| "Quiero anotarme desde mi casa o el celular" | Inscribirse sin ir a la facultad | Portal web responsive |
| "Si la materia está llena, quiero quedar en lista de espera" | No perder un lugar que se libere | Lista de espera con notificaciones (no decidido para la 1ª versión) |
| "No duplicar datos sin definir cómo se sincronizan" | Que la información oficial siga en un solo lugar | Integración con el sistema académico existente |

**RC1.** El alumno debe poder solicitar su inscripción a una comisión desde cualquier dispositivo con internet, durante el período oficial, viendo antes los días, horarios y cupos disponibles. El sistema debe informarle en la misma operación si la inscripción fue aceptada o el motivo del rechazo (correlatividad, cupo o fuera de fecha).

**RC2.** Secretaría Académica debe poder configurar las fechas oficiales de inscripción y el cupo de cada comisión, y ninguna comisión debe superar el cupo configurado.

**Preguntas pendientes:**

- ¿"Correlativa aprobada" significa final aprobado o regularidad? ¿Cambia según el plan de estudios? (Secretaría)
- ¿Qué excepciones de inscripción existen y quién las autoriza? (Secretaría)
- ¿Lista de espera, cambio de comisión y notificaciones entran en la primera versión? (Autoridades y Secretaría)
- ¿El sistema académico puede exponer una API? ¿En qué formato guarda los datos? (Sistemas)
- Si el sistema académico no responde, ¿se rechaza la solicitud o queda pendiente? (Sistemas y Secretaría)
- ¿La cifra de 3.000 alumnos simultáneos en los primeros 30 minutos está medida? (Sistemas)

### SG2 · Requisitos del producto, funciones e interfaz

<!-- cols: 8,57,10,25 -->

| ID | Requisito del producto | Origen | Función / componente |
|---|---|---|---|
| RP1 | Autenticar al usuario y determinar su rol (alumno, Secretaría, docente) | RC1, RC2 | Seguridad |
| RP2 | Mostrar las comisiones (materia, días, horarios y cupo disponible) sólo de las materias que el alumno puede cursar | RC1 | Consulta de oferta |
| RP3 | Validar las correlatividades según el plan de estudios del alumno | RC1 | Validaciones |
| RP4 | Validar que la solicitud esté dentro del período oficial y que la comisión tenga cupo | RC1, RC2 | Validaciones |
| RP5 | Registrar la inscripción y descontar el cupo en una sola operación, sin sobrecupo aunque haya accesos simultáneos | RC1, RC2 | Inscripciones |
| RP6 | Informar el resultado: comprobante de inscripción o motivo del rechazo | RC1 | Inscripciones |
| RP7 | Alta, modificación y baja de períodos de inscripción y cupos por comisión (sólo Secretaría) | RC2 | Configuración académica |
| RP8 | Registrar cada solicitud: alumno, fecha y hora, validaciones realizadas y resultado | RC1 | Auditoría |
| RP9 | Atender 3.000 usuarios simultáneos con respuesta menor a 3 segundos (valor a validar) | RC1 | Infraestructura |

**RI1 – Interfaz con el sistema académico.** Origen: portal de inscripción. Destino: sistema académico. Datos: legajo, plan de estudios, materias aprobadas y regulares, comisión elegida y estado de la inscripción. Condiciones: el portal consulta la historia académica para validar (RP3) y envía cada inscripción aceptada. Si el sistema académico no responde, la solicitud queda "pendiente de confirmación" y se reintenta; nunca se confirma sin validar las correlatividades.

**Requisitos derivados de decisiones técnicas:**

- **RD1.** El portal es web y responsive, para usarse desde computadora y celular sin instalar nada.
- **RD2.** Para no bloquear el sistema académico en la apertura, el portal consulta una copia de la oferta y los cupos que se sincroniza periódicamente, y envía las inscripciones al sistema académico mediante una cola.

### SG3 · Escenarios

**Escenario normal – inscripción aceptada:** (1) el alumno ingresa y se autentica (RP1); (2) ve la oferta de comisiones (RP2); (3) elige una comisión; (4) el sistema valida período, cupo y correlatividades consultando el sistema académico (RP3, RP4, RI1); (5) registra la inscripción y descuenta el cupo (RP5); (6) muestra el comprobante (RP6) y registra la auditoría (RP8).

**Escenario alternativo / de error:**

- **4a. Falta una correlativa:** el sistema rechaza la solicitud indicando qué materia falta, no descuenta cupo y registra la auditoría.
- **4b. El sistema académico no responde:** la solicitud queda pendiente; se le informa al alumno que se confirmará más tarde y se reintenta.

**Secuencia de funciones:** Autenticación → Consulta de oferta → Validaciones → Registro de inscripción → Informe del resultado → Auditoría.

### SG3 · Ambigüedades, conflictos, factibilidad y validación

<!-- cols: 36,16,48 -->

| Problema detectado | Tipo | Propuesta |
|---|---|---|
| "Correlativa aprobada": final aprobado o regularidad | Ambigüedad | Definirlo con Secretaría por plan de estudios y dejarlo configurable |
| "No admitir inscripciones sin requisitos" vs. "podemos autorizar excepciones" | Conflicto | La validación automática siempre se aplica; la excepción es un trámite manual de Secretaría, fuera del flujo automático |
| Confirmación inmediata vs. demoras del sistema académico | Compromiso entre atributos | Se prioriza la consistencia sobre la velocidad: estado "pendiente de confirmación" |
| 3.000 usuarios simultáneos sin validar | Factibilidad técnica | Prueba de carga temprana sobre un prototipo |
| Plazo (próximo cuatrimestre) vs. alcance | Factibilidad de plazo | Primera versión sin lista de espera ni cambio de comisión |

**Validación con los interesados:** prototipo navegable de consulta e inscripción revisado con alumnos y Secretaría; revisión de las reglas de correlatividad con Secretaría usando casos reales de alumnos; piloto con una carrera antes de la apertura general.

## Parte B – Gestión de requisitos (área REQM)

### SP 1.1 · Entendimiento

<!-- cols: 12,48,40 -->

| RC | Quién aclara | Quién acepta |
|---|---|---|
| RC1 | Alumnos (por medio del centro de estudiantes) y Secretaría Académica (reglas de inscripción) | Secretaría Académica |
| RC2 | Secretaría Académica | Secretaría Académica y docentes (cupos de sus comisiones) |

- **Pregunta 1:** ¿"correlativa aprobada" es final aprobado o regularidad? **Respuesta a confirmar:** para cursar se exige regularidad y para rendir, final aprobado, según el plan. Confirma Secretaría.
- **Pregunta 2:** si el sistema académico no responde, ¿se confirma la inscripción? **Respuesta a confirmar:** no; queda pendiente y se confirma en menos de 1 hora. Confirman Secretaría y Sistemas.

### SP 1.2 · Compromiso

Deben acordar la implementación: **Secretaría Académica** (reglas y cupos), **Área de Sistemas** (integración e infraestructura), **líder del proyecto y equipo de desarrollo** (esfuerzo y plazo) y **Autoridades** (alcance y presupuesto). El acuerdo queda registrado en una minuta firmada.

**Impacto estimado:** RI1 es el de mayor **riesgo**, porque la API del sistema académico no está confirmada: Sistemas se compromete a exponer los servicios antes del inicio del desarrollo. RP5 y RP9 suman **esfuerzo** por la concurrencia y requieren pruebas de carga. En **plazo**, la primera versión llega al próximo cuatrimestre sólo si se deja afuera la lista de espera.

### SP 1.3 · Solicitud de cambio

<!-- cols: 22,78 -->

| Campo | Contenido |
|---|---|
| ID / solicitante | SC-01 · Centro de estudiantes |
| Descripción | Agregar lista de espera por comisión y notificar al alumno cuando se libere un cupo |
| Justificación | Disminuir consultas y reclamos en Secretaría, un objetivo planteado por las Autoridades |
| Análisis de impacto | Nuevos RP (gestionar la lista de espera, notificar al alumno); modifica RP5 (al liberarse un cupo se ofrece al primero de la lista); nueva interfaz con el servicio de correo; nuevos casos de prueba; alrededor de 2 semanas más de esfuerzo; riesgo para el plazo |
| Decisión | Aprobada para la segunda versión (decide el comité de cambios: Secretaría, Sistemas y líder del proyecto). Estado: diferida |

### SP 1.4 · Trazabilidad

<!-- cols: 10,10,25,55 -->

| RC | RP | Función / componente | Caso de prueba |
|---|---|---|---|
| RC1 | RP2 | Consulta de oferta | CP01: sólo se muestran las comisiones de materias que el alumno puede cursar |
| RC1 | RP3 | Validaciones | CP02: alumno sin la correlativa → rechazo indicando la materia que falta |
| RC1, RC2 | RP5 | Inscripciones | CP03: dos alumnos piden el último cupo a la vez → sólo uno queda inscripto |
| RC2 | RP7 | Configuración académica | CP04: solicitud fuera del período configurado → rechazo |

**Hacia adelante** (RC → RP → componente → caso de prueba) se comprueba que cada RC esté implementado y probado. **Hacia atrás**, si falla un caso de prueba se sigue la fila hasta el RC para saber qué requisito y qué interesado se ven afectados. Un RP sin RC de origen es funcionalidad que nadie pidió, y un RC sin caso de prueba queda sin verificar.

### SP 1.5 · Inconsistencias

**Inconsistencia inventada:** RC2 y RP7 establecen que Secretaría configura el cupo **por comisión**, pero en el diseño de la base de datos el cupo quedó guardado **por materia**, así que todas las comisiones de una materia comparten el mismo valor.

**Detección:** el caso de prueba CP05 (configurar un cupo de 25 en una comisión e inscribir al alumno 26) falla, y la revisión de la matriz de trazabilidad muestra que RP7 no tiene un componente que lo cumpla.

**Corrección:** se registra la inconsistencia, se corrige el diseño para guardar el cupo por comisión, se vuelven a ejecutar CP05 y las pruebas de regresión, y se actualiza la matriz de trazabilidad.
