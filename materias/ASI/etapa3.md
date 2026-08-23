# Etapa 3 — Planificación de un Proyecto de TI

> **Fuente de verdad de este entregable.** El `.docx` y el `.pdf` se generan desde acá con
> `npm run docx -- materias/ASI/etapa3.md materias/ASI/etapa3.docx` y después
> `scripts/preview-docx.sh`. No editar los generados a mano.
>
> **Para qué es.** Es el documento completo de la Etapa 3, que se va subiendo a Drive a
> medida que se completa, porque el docente lo revisa antes de la entrega final. Los
> apartados marcados *En elaboración* todavía no se escribieron; se dejan enunciados para
> que se vea el plan.
>
> **Estado al 2026-08-23.** Puntos 1 a 4.2 escritos, con el punto 3 validado por el
> docente. El Acta (4.4) va como Anexo I, en archivo aparte. Faltan la EDT y los puntos
> 5 a 12.
>
> Contenido tomado de la wiki: Unidad 5 y sección TP Integrador → Etapa 3.

---

## ETAPA 3 — PLANIFICACIÓN DE UN PROYECTO DE TI

**Proyecto de TI para Personal (Telecom Argentina) — Proceso de instalación de internet con fibra óptica**

<!-- cols: 24,76 -->

| | |
|---|---|
| Cátedra | Administración de Sistemas de Información — 4º Año Ingeniería en Sistemas de Información |
| Comisión | 403 |
| Grupo | 310 |
| Integrantes | 53535 Bonadeo, Juan Cruz · 52674 Casermeiro, Gonzalo · 53543 De la Rosa, Valentín Yael · 53215 Lezcano, Diego · 52688 Lurati, Ignacio |

<!-- cols: 12,20,25,43 -->

| Mod | Fecha | Autor | Descripción |
|---|---|---|---|
| 1 | 19/08/2026 | Grupo N310 | Envío de los puntos 1 a 3 para validación |
| 2 | 23/08/2026 | CC | Validación del punto 3 y redefinición de las alternativas |
| 3 | 23/08/2026 | Grupo N310 | Reformulación del punto 3 según lo indicado |

---

## 1. PROYECTO PROPUESTO

### Problema o necesidad detectada

El proceso de instalación de internet con fibra óptica, relevado y modelado en la Etapa 1, presenta tres debilidades documentadas en las etapas anteriores y que hoy no tienen tratamiento:

1. **Falta de trazabilidad de la orden de trabajo.** El estado real de la instalación no está disponible en tiempo real para las áreas que lo necesitan, lo que genera reclamos duplicados y consultas manuales entre Operaciones, NOC y Comercial.
2. **Ausencia de criterio de priorización en la cola de órdenes de trabajo.** Identificado en la Etapa 2 como riesgo **R07**, severidad 12, **sin plan de tratamiento**.
3. **Falta de control de competencias técnicas al asignar una orden.** Identificado en la Etapa 2 como riesgo **R04** —técnico sin capacitación en el nuevo modelo de ONT—, severidad 12, **también sin plan de tratamiento**.

### Proyecto

Implementar una **plataforma de gestión de órdenes de trabajo con aplicación móvil de campo** para resolver trazabilidad, priorización y control de competencias técnicas en instalaciones de fibra óptica.

El proyecto es el tratamiento de R04 y R07, y aporta además a la mitigación de R06 —elimina aguas arriba la causa de los reclamos duplicados— y de R05, dado que la aplicación de campo es el control ya comprometido en la Etapa 2 para que los técnicos contratistas operen sin acceso a los sistemas de backend.

### Trazabilidad con las etapas anteriores

<!-- cols: 22,48,30 -->

| Origen | Texto ya comprometido | Cómo lo ataca |
|---|---|---|
| Objetivo de TI (Etapa 1) | Implementar una aplicación de gestión para técnicos de campo y aumentar la productividad operativa en un 5% | Es el alcance del proyecto |
| Meta de TI (Etapa 1) | Asignación optimizada de técnicos | Motor de asignación por competencia, zona, carga y ventana horaria |
| Objetivo de negocio (Etapa 1) | Aumentar el rendimiento de los técnicos en un 5% (instalaciones sobre horas de trabajo) | Objetivo O1, con el mismo indicador |
| Meta de negocio (Etapa 1) | Mejorar el tiempo de instalación | Objetivo O2 |

### Proceso afectado y usuarios

Afecta las **actividades 3 a 9** del proceso modelado en la Etapa 1. Las actividades 1 y 2 —recepción de la solicitud y verificación de cobertura— quedan fuera y siguen gestionándose en el CRM.

Usuarios: técnico instalador de campo (propio y contratista), supervisor de instalaciones, NOC, área comercial (consulta), logística y almacén, y Gerencia de Operaciones. El cliente final no es usuario: recibe notificaciones y firma la conformidad.

### Alcance — qué incluye

Módulo de despacho y priorización con cola única · motor de asignación por competencia certificada, zona, carga y ventana horaria · aplicación móvil *offline-first* con checklist por modelo de ONT, mediciones ópticas, evidencia fotográfica, geolocalización y conformidad digital del cliente · integraciones con SGOT, CRM, base de datos y NMS · seguridad con inicio de sesión único, doble factor y baja automática de credenciales · tablero de indicadores.

### Alcance — qué NO incluye

- El rediseño del flujo de escalamiento del CRM (R06), que ya tiene plan de tratamiento propio.
- El reemplazo o la migración del CRM, del SGOT o de la base de datos.
- Obra civil, tendido troncal, ampliación de nodos (R11) y mantenimiento preventivo del cable (R08).
- El reemplazo del firewall (R03), la redundancia del balanceador (R09) y la correlación de eventos del NMS (R10).
- Venta, facturación y recupero de clientes.
- Otros procesos de campo: reparaciones, mudanzas y desinstalaciones.
- La adquisición de vehículos y fusionadoras.

---

## 2. OBJETIVOS

<!-- cols: 5,22,27,16,13,17 -->

| # | Objetivo | Indicador | Línea base | Meta | Plazo |
|---|---|---|---|---|---|
| O1 | Aumentar la productividad del técnico de campo | Instalaciones finalizadas conformes ÷ horas-técnico disponibles | 0,50 inst./hora-técnico *(supuesto)* | 0,525 (+5%) | 6 meses desde la puesta en producción |
| O2 | Reducir la latencia de registro del cierre de la orden | % de órdenes cerradas dentro de los 15 minutos de terminada la visita, y tiempo medio entre asignación y cierre | 20% · 26 h *(supuesto)* | ≥90% · ≤8 h | Mes 4, sostenido 3 meses |
| O3 | Reducir las visitas fallidas por causa evitable | Órdenes reprogramadas por "técnico sin competencia" o "kit incompleto" ÷ órdenes despachadas | 12% *(supuesto)* | ≤6% | 6 meses desde la puesta en producción |
| O4 | Asegurar el cumplimiento de la priorización de la cola | % de órdenes despachadas según el orden del motor, y % de cumplimiento del SLA de primera respuesta | No medible en la situación actual — esa imposibilidad **es** la definición de R07 | ≥95% · ≥90% | Mes 3 desde la puesta en producción |

> **Sobre las líneas base.** Los valores marcados como *supuesto* son estimaciones: las Etapas 1 y 2 no relevaron indicadores de operación. Se los declara explícitamente como supuestos y **su medición formal es un entregable propio de la fase de Relevamiento y análisis**, sobre cuyo resultado se recalibran las metas.

---

## 3. ALTERNATIVAS Y SELECCIÓN

Se identifican tres proyectos de TI alternativos. Cada uno ataca un problema distinto de la organización, detectado en el análisis de riesgos de la Etapa 2. Se desarrolla el primero; los otros dos se mencionan como opciones evaluadas y no seleccionadas para esta etapa.

<!-- cols: 6,30,42,22 -->

| | Alternativa | Problema que ataca | Estado |
|---|---|---|---|
| 1 | Plataforma de gestión de órdenes de trabajo con aplicación móvil de campo | Falta de trazabilidad de la orden, ausencia de criterio de priorización en la cola (R07, severidad 12, sin tratamiento) y falta de control de competencias al asignar (R04, severidad 12, sin tratamiento) | **Seleccionada** |
| 2 | Plataforma de seguridad perimetral y gestión de identidades | Perímetro sobre equipamiento obsoleto sin soporte del fabricante (R03, severidad 15) y credenciales de contratistas que sobreviven al fin del contrato (R05, severidad 15) | Mencionada |
| 3 | Gestión de capacidad y mantenimiento preventivo de planta externa | Nodos de distribución que se saturan sin aviso y bloquean nuevas altas comerciales (R11) y tendido de fibra que se degrada sin plan de inspección hasta producir el corte (R08) | Mencionada |

### Justificación de la selección

Se selecciona la alternativa 1 por cuatro razones, en orden de peso:

1. **Trata riesgos que quedaron sin tratamiento.** R04 y R07 fueron identificados y valorados en severidad 12 en la Etapa 2 y no recibieron planilla de tratamiento. Este proyecto es el tratamiento de ambos: cierra un hueco de la entrega anterior en lugar de repetirla.
2. **Ejecuta un objetivo ya comprometido.** El objetivo de TI de la Etapa 1 —implementar una aplicación de gestión para técnicos de campo y aumentar la productividad operativa en un 5%— es el alcance de este proyecto, con el mismo indicador que el objetivo de negocio asociado.
3. **Impacta directamente sobre el proceso crítico.** Interviene las actividades 3 a 9 del proceso modelado en la Etapa 1. Las alternativas 2 y 3 sostienen la infraestructura y la planta externa, pero no modifican ninguna actividad del proceso.
4. **Habilita el resto de la planificación.** Al involucrar oficina, depósito y trabajo de campo, es la única de las tres que permite un análisis completo de higiene y seguridad laboral sobre los sectores del proceso crítico.

### Modo de construcción

La solución se implementa sobre una **plataforma de Field Service Management (FSM) configurable, contratada como servicio (SaaS)**. La organización no construye el producto: configura los flujos, los roles, la matriz de competencias, las reglas de priorización, los acuerdos de nivel de servicio y la aplicación de campo, y construye las **integraciones** con los sistemas existentes y la **capa de seguridad**.

**Contrapartida asumida.** El modelo implica un costo recurrente por usuario que crece con la dotación, dependencia del proveedor, y —lo más sensible en este caso— la salida de datos personales de clientes del perímetro de la organización. Este último punto agrava directamente el riesgo R05, valorado en severidad 15 en la Etapa 2, y se compensa por vía contractual: región de alojamiento habilitada, cifrado en tránsito y en reposo, inicio de sesión único con doble factor, mínimo privilegio por rol, notificación de bajas de credenciales en menos de 24 horas y derecho de auditoría. El tratamiento completo se desarrolla en el análisis de factibilidad legal del punto 12.

---

## 4. CICLO DE VIDA, FASES Y ESTRUCTURA DE DESGLOSE DE TRABAJO

### 4.1 Ciclo de vida

Se adopta un **ciclo de vida híbrido**.

**Predictivo** para la selección del proveedor, la contratación, la arquitectura de integración, la seguridad y el cumplimiento normativo: los requerimientos son estables y cerrables por anticipado, existe un proceso formal de compras con RFI y RFP, hay evaluación legal por tratamiento de datos personales, y las integraciones con sistemas heredados se especifican antes de construirse. Son entregables definidos, con aprobaciones secuenciales, que no admiten iteración.

**Incremental e iterativo** para la configuración funcional, la experiencia de uso de la aplicación de campo, las reglas de priorización y de asignación, y el despliegue territorial. La usabilidad de la aplicación con guantes, bajo sol directo y con conectividad intermitente no se puede especificar por adelantado, y los pesos del motor de asignación se calibran con datos de operación real. Se resuelve con un piloto en zona acotada, ajuste, y despliegue por olas geográficas.

**Por qué no cascada pura.** Si la aplicación se especifica de punta a punta y se entrega recién al final, el riesgo es entregar una herramienta que los técnicos no adoptan y cuyo uso falsean —cierres cargados en bloque al fin de la jornada—, lo que destruye la medición de los objetivos O1 y O2 y deja el proyecto sin evidencia de resultado.

**Por qué no ágil puro.** Existen compromisos contractuales con un proveedor externo, adquisiciones con plazos de entrega, un marco regulatorio de datos personales y un presupuesto que la Gerencia de Operaciones necesita aprobado y estimado por anticipado. Un alcance abierto no es compatible con esas condiciones.

### 4.2 Fases del proyecto

<!-- cols: 8,32,60 -->

| # | Fase | Entregable principal |
|---|---|---|
| 1 | Inicio | Acta de Proyecto aprobada |
| 2 | Relevamiento y análisis | Documento de requerimientos y **medición de las líneas base de O1 a O4** |
| 3 | Selección de proveedor | RFI, lista corta, RFP, evaluación y contrato firmado |
| 4 | Diseño y configuración | Plataforma configurada: flujos, roles, matriz de competencias, reglas de priorización, SLA y tableros |
| 5 | Integración y seguridad | Integraciones con SGOT, CRM, base de datos, NMS y stock operativas; inicio de sesión único, doble factor y baja automática de credenciales |
| 6 | Migración de datos | Órdenes abiertas, padrón de técnicos y matriz de competencias inicial |
| 7 | Pruebas | Informe de pruebas funcionales, de integración, de carga y de seguridad |
| 8 | Piloto en zona acotada | Informe de piloto con ajustes de experiencia de uso y de reglas de priorización |
| 9 | Capacitación | Técnicos, supervisores, NOC y almacén capacitados y evaluados |
| 10 | Despliegue por olas | Sistema en producción en todo el alcance geográfico |
| 11 | Estabilización y cierre | Acta de cierre, lecciones aprendidas, traspaso a operación y actualización de la CMDB |

> La fase 11 cierra el circuito con la Etapa 2: el sistema es un nuevo elemento de configuración en la CMDB y su puesta en producción constituye un cambio normal, que pasa por el Comité Asesor de Cambios según el proceso definido en el punto 11.2 de aquella etapa.

### 4.3 Estructura de Desglose de Trabajo (EDT)

*En elaboración.* Se descompone cada una de las once fases hasta el nivel de paquete de trabajo, con identificador, actividad, predecesora, duración estimada, perfil responsable y entregable verificable, en el formato que fija la cátedra. El diseño contempla desde el inicio el solapamiento de actividades que compiten por un mismo perfil, requisito para el aplanamiento de recursos del punto 10.

### 4.4 Acta de Proyecto

Se adjunta como **Anexo I**, confeccionada según la plantilla de la cátedra.

---

## 5. RECURSOS HUMANOS — PERFILES Y COMPETENCIAS

*En elaboración.* Los perfiles se derivan de las actividades de la EDT. El equipo previsto incluye jefe de proyecto, analista funcional, especialista de integraciones, especialista de seguridad, consultor de la plataforma contratada, diseñador de experiencia de uso, responsable de pruebas, capacitador y un referente de operaciones. Para cada uno se detallan responsabilidades, competencias, cantidad y dedicación a lo largo del proyecto.

---

## 6. HIGIENE Y SEGURIDAD LABORAL

*En elaboración.* Se presentan dos planos: la **base operativa** —depósito y pañol, playa de carga y estacionamiento de vehículos técnicos, mesa de despacho, oficina del NOC y sala técnica— y un **croquis tipo de trabajo en campo** con la escena de tendido aéreo. Sobre ellos se desarrollan las medidas preventivas por sector, encadenando sector, personas expuestas, riesgo, medida y su representación en el plano. Los riesgos relevantes identificados son trabajo en altura, riesgo eléctrico por proximidad a línea energizada, espacio confinado en cámaras subterráneas, circulación de vehículos, manipulación manual de cargas en depósito, y fatiga visual y riesgos psicosociales por turnos rotativos en el NOC.

---

## 7. ACTIVOS A ADQUIRIR

*En elaboración.* Licencias de la plataforma FSM por usuario, servicio de implantación y configuración, horas de consultoría para las cuatro integraciones, dispositivos móviles rugerizados para los técnicos, administración de dispositivos móviles, servicio de mapas y geolocalización, ambiente de pruebas no productivo, capacitación y soporte durante la estabilización. Para cada uno se detallan cantidad y características mínimas exigibles.

---

## 8. FORMA DE ADQUISICIÓN

*En elaboración.* Se asigna a cada activo su modalidad —suscripción anual, contrato de servicios por hora, compra directa o pago por uso— con la justificación correspondiente.

---

## 9. RFI Y RFP

*En elaboración.* Se define la diferencia entre ambos instrumentos y se indica en qué adquisición concreta del proyecto se utilizaría cada uno: el RFI para relevar el mercado de plataformas FSM antes de fijar especificaciones, y el RFP para la contratación conjunta de licenciamiento, implantación e integración una vez definidos los requisitos.

---

## 10. TIEMPOS DEL PROYECTO

*En elaboración.* Asignación de recursos a la EDT, estimación de duraciones, diagrama de Red con determinación del camino crítico y de las holguras, diagrama de Gantt con la cantidad de personas por perfil, aplanamiento de recursos y estimación de la duración total del proyecto.

---

## 11. VARIABLES DE COSTO

*En elaboración.* Horas por perfil y valor hora, licenciamiento recurrente, servicios de implantación e integración, hardware, capacitación, costos indirectos y reserva de contingencia, con el costo total de propiedad proyectado a tres años.

---

## 12. ANÁLISIS DE FACTIBILIDAD

*En elaboración.* Factibilidad técnica, económica y legal. La factibilidad legal es la de mayor peso en este proyecto: el tratamiento de datos personales de clientes en una plataforma contratada como servicio activa la Ley 25.326 en materia de transferencia internacional de datos, figura del encargado de tratamiento, medidas de seguridad exigibles y obligación de notificación ante brecha, en concurrencia con la Ley 27.078 y las normativas de calidad de servicio del ENACOM.
