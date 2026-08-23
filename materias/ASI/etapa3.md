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
> 5 a 12. **Fecha de entrega: 28/08/2026.**
>
> **Decisiones tomadas por el grupo ante consultas que el docente no respondió:**
> líneas base declaradas como supuestos con su medición como entregable de la fase 2
> (D3); cronograma en meses relativos desde la aprobación del Acta (D2); justificación
> de la selección cualitativa, sin matriz ponderada, en línea con su indicación de que
> las otras dos alternativas solo se mencionan. Las tres quedan sujetas a revisión si
> el docente se pronuncia.
>
> Contenido tomado de la wiki: Unidad 5 y sección TP Integrador → Etapa 3.

---

## UNIVERSIDAD TECNOLÓGICA NACIONAL

### CÁTEDRA

Administración de Sistemas de Información — 4º Año Ingeniería en Sistemas de Información

### TRABAJO PRÁCTICO INTEGRADOR 2026 — ETAPA 3

**Planificación de un Proyecto de TI**

*Proyecto de TI para Personal (Telecom Argentina) — Proceso de instalación de internet con fibra óptica*

**Comisión Nº:** 403

**Grupo Nº:** 310

### INTEGRANTES

*Legajo, Apellido y Nombres, Email*

- 53535, Bonadeo Juan Cruz, juancruzbonadeo04@gmail.com
- 52674, Casermeiro Gonzalo, gonzacasermeiro@gmail.com
- 53543, De la Rosa Valentín Yael, mferreyra079@gmail.com
- 53215, Lezcano Diego, diegolezcano209@gmail.com
- 52688, Lurati Ignacio, ignaciolurati2@gmail.com

### VERSIÓN DEL DOCUMENTO

<!-- cols: 10,18,22,50 -->

| Mod | Fecha | Autor | Descripción |
|---|---|---|---|
| 1 | 19/08/2026 | Grupo N310 | Envío de los puntos 1 a 3 para validación del docente |
| 2 | 23/08/2026 | CC | Validación del punto 3 y redefinición de las alternativas |
| 3 | 23/08/2026 | Grupo N310 | Reformulación del punto 3 y avance de los puntos 4.1 y 4.2 |

### ÍNDICE

1. Proyecto propuesto
2. Objetivos
3. Alternativas y selección
4. Ciclo de vida, fases y estructura de desglose de trabajo
5. Recursos humanos — perfiles y competencias
6. Higiene y seguridad laboral
7. Activos a adquirir
8. Forma de adquisición
9. RFI y RFP
10. Tiempos del proyecto
11. Variables de costo
12. Análisis de factibilidad

Anexo I — Acta de Proyecto

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

La estructura se descompone en once paquetes de primer nivel, correspondientes a las fases, y cuarenta y seis paquetes de trabajo. Cada paquete se define hasta el nivel que permite asignar un responsable, estimar una duración y verificar un entregable, según el criterio fijado por la cátedra.

**Perfiles asignados.** Se identifican con la sigla que se utiliza en la columna correspondiente:

<!-- cols: 10,32,58 -->

| Sigla | Perfil | Alcance de su intervención |
|---|---|---|
| JP | Jefe de Proyecto | Coordinación de alcance, tiempo, costo y comunicación; contratación y cierre |
| AF | Analista funcional | Relevamiento, requerimientos, validación con usuarios y acompañamiento de la configuración |
| EI | Especialista de integraciones | Interfaces con SGOT, CRM, base de datos, NMS y sistema de stock; migración de datos |
| ES | Especialista de seguridad | Requerimientos de seguridad, autenticación, privilegios y pruebas de seguridad |
| CP | Consultor de la plataforma | Configuración de la plataforma contratada; provisto por el proveedor |
| UX | Diseñador de experiencia de uso | Diseño y validación de la aplicación de campo con los técnicos |
| QA | Responsable de pruebas | Diseño y ejecución del plan de pruebas |
| CA | Capacitador | Material de capacitación y dictado |
| RO | Referente de operaciones | Conocimiento del proceso, datos maestros, piloto y despliegue |

**Estructura de desglose.** Las duraciones se expresan en días hábiles.

<!-- cols: 7,36,11,9,12,25 -->

| ID | Paquete de trabajo | Pred. | Dur. | Perfil | Entregable |
|---|---|---|---|---|---|
| **1** | **Inicio** | | | | |
| 1.1 | Elaborar el Acta de Proyecto | — | 3 | JP | Acta de Proyecto aprobada |
| 1.2 | Conformar el equipo y asignar dedicaciones | 1.1 | 2 | JP | Matriz de asignación de recursos |
| 1.3 | Realizar la reunión de arranque | 1.2 | 1 | JP | Minuta de inicio |
| **2** | **Relevamiento y análisis** | | | | |
| 2.1 | Relevar el proceso actual de despacho y ejecución de órdenes | 1.3 | 8 | AF, RO | Documento del proceso actual |
| 2.2 | Especificar los requerimientos funcionales | 2.1 | 10 | AF | Documento de requerimientos |
| 2.3 | Especificar los requerimientos de integración | 2.1 | 6 | EI | Especificación de interfaces |
| 2.4 | Medir las líneas base de los objetivos O1 a O4 | 2.1 | 15 | AF, RO | Informe de línea base |
| 2.5 | Especificar los requerimientos de seguridad y cumplimiento | 2.1 | 5 | ES | Requerimientos de seguridad |
| 2.6 | Validar los requerimientos con los usuarios clave | 2.2, 2.3, 2.5 | 3 | AF, RO | Requerimientos aprobados |
| **3** | **Selección de proveedor** | | | | |
| 3.1 | Elaborar y emitir el RFI | 2.6 | 5 | JP, AF | RFI emitido |
| 3.2 | Analizar las respuestas y conformar la lista corta | 3.1 | 5 | JP, AF | Lista corta de proveedores |
| 3.3 | Elaborar y emitir el RFP | 3.2 | 7 | JP, AF, ES | RFP emitido |
| 3.4 | Evaluar las propuestas técnicas y económicas | 3.3 | 8 | JP, AF, EI, ES | Cuadro comparativo de propuestas |
| 3.5 | Negociar y firmar el contrato | 3.4 | 6 | JP | Contrato firmado |
| **4** | **Diseño y configuración** | | | | |
| 4.1 | Configurar los flujos de orden de trabajo, estados y roles | 3.5 | 10 | CP, AF | Flujos configurados |
| 4.2 | Parametrizar la matriz impacto/urgencia y los acuerdos de nivel de servicio | 4.1 | 6 | CP, AF | Motor de priorización operativo |
| 4.3 | Configurar el motor de asignación por competencia, zona, carga y ventana horaria | 4.2 | 8 | CP, AF | Motor de asignación operativo |
| 4.4 | Relevar y cargar la matriz de competencias por técnico | 3.5 | 7 | RO | Matriz de competencias cargada |
| 4.5 | Diseñar y validar la experiencia de uso de la aplicación de campo | 3.5 | 8 | UX | Prototipo validado con técnicos |
| 4.6 | Configurar la aplicación de campo según el diseño validado | 4.3, 4.5 | 8 | CP, UX | Aplicación de campo configurada |
| 4.7 | Configurar los tableros de indicadores | 4.2 | 4 | CP | Tableros operativos |
| **5** | **Integración y seguridad** | | | | |
| 5.1 | Integrar con el sistema de gestión de órdenes de trabajo | 4.1 | 10 | EI | Integración operativa |
| 5.2 | Integrar con el CRM | 5.1 | 8 | EI | Integración operativa |
| 5.3 | Integrar con la base de datos de clientes y órdenes | 5.2 | 6 | EI | Integración operativa |
| 5.4 | Integrar con el sistema de monitoreo de red | 5.3 | 5 | EI | Integración operativa |
| 5.5 | Implementar el inicio de sesión único y el doble factor | 3.5 | 6 | ES | Autenticación operativa |
| 5.6 | Implementar el mínimo privilegio y la baja automática de credenciales | 5.5 | 8 | ES, EI | Control de accesos operativo |
| **6** | **Migración de datos** | | | | |
| 6.1 | Migrar las órdenes de trabajo abiertas | 5.3 | 4 | EI | Órdenes migradas |
| 6.2 | Cargar el padrón de técnicos y los datos maestros | 4.4 | 3 | RO | Datos maestros cargados |
| **7** | **Pruebas** | | | | |
| 7.1 | Diseñar el plan y los casos de prueba | 2.6 | 6 | QA | Plan de pruebas |
| 7.2 | Ejecutar las pruebas funcionales | 4.6, 4.7, 7.1 | 8 | QA, AF | Informe de pruebas funcionales |
| 7.3 | Ejecutar las pruebas de integración | 5.4, 6.1, 7.1 | 6 | QA, EI | Informe de pruebas de integración |
| 7.4 | Ejecutar las pruebas de carga | 7.3 | 4 | QA | Informe de pruebas de carga |
| 7.5 | Ejecutar las pruebas de seguridad | 5.6, 7.1 | 5 | ES, QA | Informe de pruebas de seguridad |
| 7.6 | Corregir las observaciones y volver a probar | 7.2, 7.4, 7.5 | 6 | CP, EI | Observaciones cerradas |
| **8** | **Piloto** | | | | |
| 8.1 | Preparar el piloto: zona, técnicos y dispositivos | 7.6 | 4 | JP, RO | Piloto preparado |
| 8.2 | Ejecutar el piloto en zona acotada | 8.1, 6.2 | 15 | RO, CP | Piloto en operación |
| 8.3 | Ajustar las reglas de asignación y la experiencia de uso | 8.2 | 8 | CP, UX | Ajustes aplicados |
| 8.4 | Elaborar el informe de piloto y decidir el avance | 8.3 | 2 | JP | Informe de piloto aprobado |
| **9** | **Capacitación** | | | | |
| 9.1 | Elaborar el material de capacitación | 7.2 | 8 | CA, AF | Material de capacitación |
| 9.2 | Capacitar a supervisores, despacho y NOC | 8.4, 9.1 | 4 | CA | Personal de gestión capacitado |
| 9.3 | Capacitar a los técnicos de campo por olas | 9.2 | 10 | CA | Técnicos capacitados |
| 9.4 | Evaluar la capacitación | 9.3 | 3 | CA | Evaluaciones registradas |
| **10** | **Despliegue por olas** | | | | |
| 10.1 | Desplegar la ola 1 | 9.2 | 6 | CP, RO | Ola 1 en producción |
| 10.2 | Desplegar la ola 2 | 10.1 | 6 | CP, RO | Ola 2 en producción |
| 10.3 | Desplegar la ola 3 | 10.2 | 6 | CP, RO | Ola 3 en producción |
| **11** | **Estabilización y cierre** | | | | |
| 11.1 | Acompañar la operación en período de estabilización | 10.3 | 15 | CP, RO | Operación estabilizada |
| 11.2 | Dar de alta el elemento de configuración en la CMDB y cerrar el cambio ante el CAB | 10.3 | 3 | EI | Elemento de configuración registrado |
| 11.3 | Transferir a operación y documentar | 11.1 | 5 | JP, AF | Documentación de traspaso |
| 11.4 | Elaborar el acta de cierre y las lecciones aprendidas | 11.2, 11.3 | 3 | JP | Acta de cierre |

**Solapamientos previstos.** La estructura contempla deliberadamente actividades concurrentes que comparten un mismo perfil. Son el insumo del análisis de sobreasignación y del aplanamiento de recursos del punto 10:

- **Analista funcional.** Los paquetes 2.2, 2.3 y 2.4 arrancan simultáneamente al terminar 2.1, y el analista participa de 2.2 y 2.4 a la vez. La medición de la línea base (2.4) es además la actividad más larga de la fase.
- **Especialista de integraciones.** Los paquetes 5.1 a 5.4 se planifican encadenados sobre un único especialista, mientras 5.6 y 6.1 lo requieren en la misma ventana. Es el conflicto de mayor impacto sobre la duración total.
- **Especialista de seguridad.** Interviene en 3.3 y 3.4 durante la selección del proveedor, y en 5.5 y 5.6 durante la implementación, con solapamiento sobre el cierre de la fase 3.
- **Consultor de la plataforma.** Los paquetes 4.6, 4.7 y 5.1 comparten ventana temporal, y más adelante 8.3, 10.1 y 11.1 vuelven a concentrarse sobre el mismo perfil.
- **Referente de operaciones.** Participa de 2.1 y 2.4 en el relevamiento y de 4.4 durante la configuración, además del piloto y las tres olas de despliegue.

**Criterio de descomposición.** No se descompone por debajo del nivel en que un paquete tiene un único entregable verificable y un responsable identificable. Los paquetes de las fases 9 y 10 se abren por ola de despliegue porque cada una constituye una entrega con valor propio y admite decisión de avance o retroceso.

### 4.4 Acta de Proyecto

Se incluye como **Anexo I** al final de este documento, confeccionada según la plantilla de la cátedra.

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

*En elaboración.* Asignación de recursos a la EDT, estimación de duraciones, diagrama de Red con determinación del camino crítico y de las holguras, diagrama de Gantt con la cantidad de personas por perfil, aplanamiento de recursos y estimación de la duración total del proyecto. El cronograma se expresa en **meses relativos** contados desde la aprobación del Acta de Proyecto, no en fechas de calendario, para no atar la planificación a una fecha de inicio todavía no definida.

---

## 11. VARIABLES DE COSTO

*En elaboración.* Horas por perfil y valor hora, licenciamiento recurrente, servicios de implantación e integración, hardware, capacitación, costos indirectos y reserva de contingencia, con el costo total de propiedad proyectado a tres años.

---

## 12. ANÁLISIS DE FACTIBILIDAD

*En elaboración.* Factibilidad técnica, económica y legal. La factibilidad legal es la de mayor peso en este proyecto: el tratamiento de datos personales de clientes en una plataforma contratada como servicio activa la Ley 25.326 en materia de transferencia internacional de datos, figura del encargado de tratamiento, medidas de seguridad exigibles y obligación de notificación ante brecha, en concurrencia con la Ley 27.078 y las normativas de calidad de servicio del ENACOM.

---

## ANEXO I — ACTA DE PROYECTO

### ACTA DEL PROYECTO

**Implementar una plataforma de gestión de órdenes de trabajo con aplicación móvil de campo para resolver trazabilidad, priorización y control de competencias técnicas en instalaciones de fibra óptica**

---

#### DE

**Gerencia de Operaciones** — Personal (Telecom Argentina)

*Patrocinador del proyecto. Es el área titular del proceso crítico afectado y de
los objetivos de negocio que el proyecto compromete.*

#### PARA

Integrantes de las áreas de la organización que deben tomar conocimiento del proyecto:

- Gerencia de Operaciones — Supervisión de Instalaciones
- Gerencia de Tecnología y Sistemas — Desarrollo, Infraestructura y Seguridad de la Información
- Centro de Operaciones de Red (NOC)
- Gerencia Comercial — Atención al Cliente
- Logística y Almacenes
- Compras y Abastecimiento
- Recursos Humanos
- Servicio de Higiene y Seguridad Laboral

Y el equipo del proyecto, inicialmente conformado por las personas indicadas en
el apartado DESIGNACIÓN.

#### DESIGNACIÓN

El patrocinador designa los siguientes roles para la ejecución del proyecto:

<!-- cols: 44,56 -->

| Rol designado | Área de procedencia |
|---|---|
| Director de Proyecto | Gerencia de Tecnología y Sistemas |
| Arquitecto de Software / Líder Técnico | Gerencia de Tecnología y Sistemas — Desarrollo |
| Analista Funcional | Gerencia de Tecnología y Sistemas — Desarrollo |
| Responsable de Seguridad de la Información | Gerencia de Tecnología y Sistemas — Seguridad de la Información |
| Referente de Operaciones | Gerencia de Operaciones — Supervisión de Instalaciones |

El resto del equipo —desarrollo, experiencia de usuario, datos, pruebas,
infraestructura y capacitación— es conformado por el Director de Proyecto según
los perfiles y competencias descriptos en el punto 5 de esta etapa.

#### DESCRIPCIÓN DE SU RESPONSABILIDAD

**Director de Proyecto.** Dirigir el proyecto y **conformar el equipo que lo
llevará adelante**: desarrollo, diseño de experiencia de usuario, datos, pruebas,
infraestructura y capacitación. Los perfiles y competencias de ese equipo se
detallan en el punto 5 de esta etapa. Es responsable de la planificación, del
cumplimiento del cronograma, del presupuesto aprobado, de la gestión de riesgos y
de las comunicaciones con el patrocinador y las áreas involucradas. Responde por
la entrega de los entregables comprometidos en este Acta.

**Arquitecto de Software / Líder Técnico.** Definir la arquitectura de la
plataforma y de las integraciones con SGOT, CRM, la base de datos de clientes y
órdenes de trabajo, y el sistema de gestión de red (NMS). Conducir técnicamente al
equipo de desarrollo que designe el Director de Proyecto y responder por la
calidad técnica de los entregables.

**Analista Funcional.** Relevar y validar los requerimientos con Supervisión de
Instalaciones, técnicos de campo, NOC y Logística. Responsable de la **medición
de las líneas base** de los indicadores comprometidos en los objetivos, y de la
definición de las reglas de priorización y del motor de asignación.

**Responsable de Seguridad de la Información.** Definir e implementar los
controles de acceso, autenticación y auditoría de la plataforma, incluida la
baja automática de credenciales integrada con Recursos Humanos. Verificar el
cumplimiento de la Ley 25.326 de Protección de Datos Personales sobre los datos
de clientes que la aplicación de campo trata.

**Referente de Operaciones.** Ser el nexo entre el equipo del proyecto y la
operación. Facilitar el acceso a la información del proceso, a los técnicos y a
las zonas de trabajo; coordinar el piloto y validar funcionalmente los
entregables antes de su aceptación.

#### DESCRIPCIÓN DE SU AUTORIDAD

**Director de Proyecto.** Tiene autoridad para asignar trabajo dentro del equipo
del proyecto, coordinar con las áreas involucradas y con proveedores, y validar
entregables intermedios. Puede aprobar cambios que **no afecten** el alcance, el
costo total ni la fecha de finalización comprometidos en este Acta; todo cambio
que afecte alguno de esos tres factores debe elevarse al patrocinador para su
aprobación. Tiene autoridad para acceder a las instalaciones de la organización
en horario de funcionamiento y, cuando el proyecto lo requiera, fuera de él,
coordinando previamente con el Referente de Operaciones.

**Arquitecto de Software / Líder Técnico.** Tiene autoridad para definir la
arquitectura técnica y aprobar o rechazar diseños de integración. Las decisiones
que impliquen modificar los sistemas existentes (SGOT, CRM, NMS) requieren
acuerdo previo del área propietaria de cada sistema.

**Analista Funcional.** Tiene autoridad para convocar a usuarios clave de
Operaciones, NOC y Logística a instancias de relevamiento y validación, dentro
de la disponibilidad acordada con cada área.

**Responsable de Seguridad de la Información.** Tiene autoridad para **bloquear
la puesta en producción** de cualquier componente que no cumpla las políticas de
seguridad de la organización o la normativa de protección de datos personales.
Esta decisión solo puede ser revertida por la Gerencia de Tecnología y Sistemas.

**Referente de Operaciones.** Tiene autoridad para autorizar el ingreso del
equipo del proyecto a las zonas operativas y para definir, junto con Supervisión
de Instalaciones, la zona y el momento del piloto.

⚠ *Autoridad de compra: el Director de Proyecto puede aprobar adquisiciones
hasta el monto fijado por la política de compras vigente de la organización;
para excederlo debe solicitar autorización a la Gerencia de Administración y
Finanzas.* **(Completar con el monto real si el grupo lo define. Este es el
campo donde el ejemplo de cátedra es más concreto — conviene no dejarlo genérico.)**

---

### ALCANCE DEL PROYECTO

#### Justificación

El proceso de instalación de internet con fibra óptica, relevado y modelado en
la Etapa 1 de este trabajo, presenta tres debilidades que fueron identificadas y
documentadas en las etapas anteriores y que hoy no tienen tratamiento:

1. **Falta de trazabilidad de la orden de trabajo.** El estado real de la
   instalación no está disponible en tiempo real para las áreas que lo
   necesitan, lo que genera reclamos duplicados y consultas manuales entre
   Operaciones, NOC y el área Comercial.

2. **Ausencia de criterio de priorización en la cola de órdenes de trabajo.**
   Identificado en la Etapa 2 como riesgo **R07**, valorado en severidad 12 y
   **sin plan de tratamiento**.

3. **Falta de control de competencias técnicas al asignar una orden.**
   Identificado en la Etapa 2 como riesgo **R04** — técnico sin capacitación en
   el nuevo modelo de ONT —, valorado en severidad 12 y **también sin plan de
   tratamiento**.

Este proyecto constituye el tratamiento de los riesgos R04 y R07, cubriendo un
hueco de la etapa anterior, y contribuye adicionalmente a la mitigación de R06
(ausencia de flujo de escalamiento en el CRM) al eliminar aguas arriba la causa
de los reclamos duplicados, y de R05 (credenciales de contratistas sin baja),
dado que la aplicación de campo es el control ya comprometido en la Etapa 2 para
que los técnicos contratistas operen sin acceso a los sistemas de backend.

Asimismo, el proyecto da cumplimiento al **objetivo de TI ya definido por la
organización en la Etapa 1** — *implementar una aplicación de gestión para
técnicos de campo que permita aumentar la productividad operativa en un 5%* — y
a la meta de TI *Asignación Optimizada de Técnicos*, ambos alineados con el
objetivo de negocio de *aumentar el rendimiento de los técnicos en un 5%,
medido como instalaciones sobre horas de trabajo*.

#### Producto

**Plataforma de gestión de órdenes de trabajo con aplicación móvil de campo**:
solución de mercado de *Field Service Management*, contratada como servicio,
configurada e integrada con los sistemas existentes y en producción, que gestiona
el ciclo completo de la orden de trabajo de instalación de fibra óptica, desde el
despacho hasta el cierre con conformidad del cliente.

Comprende seis componentes:

1. Módulo de despacho y priorización, con cola única alimentada por CRM, SGOT y
   excepciones del NMS, cronómetro de SLA y escalamiento.
2. Motor de asignación por competencia certificada, zona o nodo, carga del día,
   ventana horaria y stock del vehículo.
3. Aplicación móvil de campo *offline-first* del proveedor, configurada con
   agenda, ficha de orden de trabajo, checklist por modelo de ONT, registro de
   mediciones ópticas, evidencia fotográfica, geolocalización, consumo de
   materiales, tipificación obligatoria del motivo cuando la visita no se
   completa y conformidad del cliente con firma digital.
4. Integraciones con SGOT, CRM, base de datos de clientes y órdenes de trabajo,
   NMS y sistema de stock.
5. Capa de seguridad: inicio de sesión único con doble factor, mínimo
   privilegio, baja automática de credenciales integrada con Recursos Humanos y
   registro de auditoría.
6. Tablero de indicadores para Supervisión y Gerencia de Operaciones.

Los componentes 1, 2, 3 y 6 se obtienen configurando la plataforma contratada;
los componentes 4 y 5 —integraciones y capa de seguridad— se construyen sobre
la infraestructura de la organización.

#### Entregables

Primera aproximación de la Estructura de Desglose de Trabajo, con los
entregables principales por fase:

<!-- cols: 30,70 -->

| Fase | Entregable principal |
|---|---|
| 1. Inicio | Acta de Proyecto aprobada |
| 2. Relevamiento y análisis | Documento de requerimientos validado y **medición de las líneas base** de los indicadores |
| 3. Selección de proveedor | RFI, lista corta, RFP evaluado y contrato firmado |
| 4. Diseño y configuración | Plataforma configurada: flujos, roles, matriz de competencias, reglas de priorización, SLA y tableros |
| 5. Integración y seguridad | Integraciones operativas y controles de seguridad implementados |
| 6. Migración de datos | Matriz de competencias y datos maestros cargados |
| 7. Pruebas | Informe de pruebas funcionales, de integración y de seguridad |
| 8. Piloto | Informe de piloto en zona acotada, con ajustes aplicados |
| 9. Capacitación | Técnicos, supervisores y despachantes capacitados |
| 10. Despliegue por olas | Plataforma en producción en todas las zonas |
| 11. Estabilización y cierre | Documentación, transferencia operativa, alta del elemento de configuración en la CMDB y cierre formal |

#### Objetivos

<!-- cols: 5,22,27,16,13,17 -->

| # | Objetivo | Indicador | Línea base | Meta | Plazo |
|---|---|---|---|---|---|
| O1 | Aumentar la productividad del técnico de campo | Instalaciones finalizadas conformes ÷ horas-técnico disponibles | 0,50 inst./hora-técnico *(supuesto)* | 0,525 (+5%) | 6 meses desde la puesta en producción |
| O2 | Reducir la latencia de registro del cierre de la orden de trabajo | % de órdenes cerradas en el sistema dentro de los 15 minutos de terminada la visita, y tiempo medio entre asignación y cierre | 20% · 26 h *(supuesto)* | ≥90% · ≤8 h | Mes 4, sostenido 3 meses |
| O3 | Reducir las visitas fallidas por causa evitable | Órdenes reprogramadas por "técnico sin competencia" o "kit incompleto" ÷ órdenes despachadas | 12% *(supuesto)* | ≤6% | 6 meses desde la puesta en producción |
| O4 | Asegurar el cumplimiento de la priorización de la cola | % de órdenes despachadas según el orden del motor de priorización, y % de cumplimiento del SLA de primera respuesta | No medible en la situación actual — esa imposibilidad **es** la definición del riesgo R07 | ≥95% · ≥90% | Mes 3 desde la puesta en producción |

> **Sobre las líneas base.** Los valores indicados como *supuesto* son
> estimaciones: las Etapas 1 y 2 de este trabajo no relevaron indicadores de
> operación. Su medición formal constituye un entregable propio de la fase 2
> (Relevamiento y análisis), y las metas se recalibrarán sobre los valores
> reales medidos.

#### Límite

El proyecto **no incluye**:

- El rediseño del flujo de escalamiento del CRM (riesgo R06), que cuenta con
  plan de tratamiento propio en la Etapa 2.
- El reemplazo o la migración del CRM, del SGOT o de la base de datos de
  clientes y órdenes de trabajo.
- Obra civil, tendido troncal, ampliación de nodos (riesgo R11) y mantenimiento
  preventivo del cable (riesgo R08).
- El reemplazo del firewall (riesgo R03), la redundancia del balanceador de
  carga (riesgo R09) y la correlación de eventos del NMS (riesgo R10).
- Los procesos de venta, facturación y recupero de clientes.
- Otros procesos de campo distintos de la instalación: reparaciones, mudanzas y
  desinstalaciones.
- La adquisición de vehículos y fusionadoras de fibra óptica.
- Las actividades 1 y 2 del proceso modelado en la Etapa 1 —recepción de la
  solicitud y verificación de cobertura—, que continúan gestionándose en el CRM.

---

#### Firma Autorizante

Nombre: _______________________________________________

Título: _______________________________________________
