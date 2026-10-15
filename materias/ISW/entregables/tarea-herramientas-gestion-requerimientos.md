# Tarea — Herramientas de gestión de requerimientos

> Fuente de verdad del entregable. Se genera con
> `node scripts/build-docx.js materias/ISW/entregables/tarea-herramientas-gestion-requerimientos.md materias/ISW/entregables/tarea-herramientas-gestion-requerimientos.docx`.
> Precios consultados en octubre de 2026 (G2, GetApp); son aproximados.

---

## Herramientas de gestión de requerimientos: comparación

**Herramientas elegidas:** **Tuleap Community Edition** (gratuita, de código abierto) e **IBM Engineering Requirements Management DOORS Next** (paga).

<!-- cols: 22,39,39 -->

| Capacidad | Tuleap Community Edition (gratuita) | IBM DOORS Next (paga) |
|---|---|---|
| Licencia y costo | Código abierto (GPL). Gratis; existe una edición Enterprise paga con soporte, desde ~€1.560/año | Comercial. Desde ~US$ 164 por usuario/mes en la nube; on-premise por cotización |
| Instalación | Se instala en un servidor propio (Linux); acceso web | Nube de IBM o servidor propio; acceso web |
| Tipo de herramienta | Plataforma ALM completa: requisitos, planificación ágil, incidencias, pruebas y repositorios Git | Herramienta especializada en requisitos, parte de la suite IBM ELM |
| Captura y especificación | Requisitos como ítems de "trackers" configurables (campos, tipos, estados) | Requisitos dentro de módulos con formato de documento; importa Word, Excel y ReqIF |
| Atributos y tipos de requisito | Campos y tipos totalmente configurables por proyecto | Tipos de artefacto, atributos y tipos de vínculo configurables |
| Trazabilidad | Vínculos entre requisitos, historias, tareas, pruebas, defectos y commits; búsquedas entre trackers y vista de cobertura de requisitos por las pruebas | Vínculos tipados (satisface, deriva de, valida), vistas y matrices de trazabilidad hacia diseño y pruebas |
| Análisis de impacto | Siguiendo los vínculos manualmente o con consultas | Automático: al cambiar un requisito, marca como sospechosos los vínculos afectados |
| Gestión de cambios | Flujos de trabajo (workflow) con estados, permisos y transiciones; historial de cada ítem | Conjuntos de cambios, flujos de aprobación e historial completo con auditoría |
| Versiones y líneas base | Historial por ítem; líneas base y generación de documentos sólo en la edición Enterprise | Líneas base, comparación entre versiones y configuraciones por variante de producto |
| Revisión y aprobación | Por estados del workflow y comentarios | Revisiones formales con participantes, aprobaciones y firma electrónica |
| Gestión de pruebas | Incluida (campañas, casos de prueba y su vínculo con requisitos) | Mediante IBM Engineering Test Management (otra licencia) |
| Gestión ágil | Incluida (Scrum, Kanban, backlog, sprints) | Mediante otra herramienta de la suite (IBM EWM) o integración con Jira |
| Reportes | Tableros, gráficos y consultas configurables | Vistas, reportes y documentos exportables; revisión de la redacción con IA (complemento) |

**Ventajas y desventajas:**

<!-- cols: 16,42,42 -->

| | Tuleap Community Edition | IBM DOORS Next |
|---|---|---|
| Ventajas | Sin costo de licencia · Todo el ciclo de vida en una sola herramienta (requisitos, pruebas, Git, agilidad) · Muy configurable · Trazabilidad de punta a punta | Estándar de la industria en sistemas críticos (aeroespacial, automotriz, defensa) · Análisis de impacto automático · Líneas base y configuraciones avanzadas · Revisiones formales con firma · Soporte oficial de IBM |
| Desventajas | Hay que instalarla y mantener el servidor · Sin soporte oficial (sólo la comunidad) · Líneas base y documentos sólo en la versión paga · Configurarla lleva tiempo | Costo alto por usuario · Curva de aprendizaje alta · Pruebas y gestión ágil requieren licencias aparte · Excesiva para proyectos chicos |
| Conviene para | Equipos chicos o medianos, proyectos académicos o empresas que quieren una ALM sin costo de licencia | Organizaciones grandes o reguladas, con muchos requisitos y obligación de auditoría |

**Relación con REQM (CMMI):** las dos cubren las prácticas del área: entender y aceptar requisitos (estados y aprobaciones, SP 1.1 y 1.2), gestionar cambios (workflow e historial, SP 1.3), mantener la trazabilidad bidireccional (vínculos y matrices, SP 1.4) e identificar inconsistencias (consultas o vínculos sospechosos, SP 1.5). La diferencia está en el grado de automatización: DOORS Next detecta el impacto de un cambio por sí sola, mientras que en Tuleap hay que buscarlo siguiendo los vínculos.
