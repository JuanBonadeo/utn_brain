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
> **Estado al 2026-08-23.** Los doce puntos de la consigna están desarrollados. El Acta va
> como Anexo I dentro de este mismo documento. **Fecha de entrega: 28/08/2026.**
>
> Pendiente de definición del grupo: los nombres propios y el monto de autoridad de compra
> del Acta, y el dibujo de los dos planos del punto 6, cuya especificación está escrita.
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

<!-- cols: 6,13,13,68 -->

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

<!-- cols: 16,52,32 -->

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

<!-- cols: 5,17,25,23,14,16 -->

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

<!-- cols: 4,31,50,15 -->

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

<!-- cols: 5,35,60 -->

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

<!-- cols: 7,30,16,7,16,24 -->

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

Los perfiles que se presentan no constituyen un listado de puestos que podrían participar del proyecto: **cada uno se deriva de los paquetes de trabajo de la EDT del punto 4.3**, y ninguno figura en esta sección sin ser responsable de al menos un paquete con entregable verificable. La carga que se consigna surge de sumar las duraciones de los paquetes en los que el perfil interviene, y la dedicación media resulta de dividir esa carga por la ventana temporal en que el perfil está afectado al proyecto según la programación aplanada del punto 10. El esfuerzo total planificado asciende a **4.240 horas-persona** sobre una jornada de ocho horas.

Se destaca que *perfil requerido* no equivale a persona exclusiva. Ninguno de los nueve perfiles alcanza dedicación completa, de modo que todos se afectan parcialmente al proyecto y conservan sus responsabilidades de línea, con la disponibilidad comprometida formalmente en el paquete 1.2.

<!-- cols: 8,16,27,25,8,16 -->

| Sigla | Perfil | Responsabilidades | Competencias | Pers. | Dedicación |
|---|---|---|---|---|---|
| JP | Jefe de proyecto | Alcance, tiempo, costo, riesgos y comunicaciones; conducción del proceso de contratación y del cierre formal | Dirección de proyectos, negociación con proveedores, gestión de interesados | 1 | d0–d192 · 408 h · 27% |
| AF | Analista funcional | Relevamiento, requerimientos, medición de líneas base, validación con usuarios y acompañamiento de la configuración | Análisis y modelado de procesos, elicitación de requerimientos, definición de indicadores | 1 | d6–d189 · 848 h · 58% |
| EI | Especialista de integraciones | Interfaces con SGOT, CRM, base de datos, NMS y stock; migración de órdenes; alta del CI en la CMDB | Interfaces y servicios web, mapeo y migración de datos, sistemas heredados | 2 | d14–d172 · 560 h · 22% |
| ES | Especialista de seguridad | Requerimientos de seguridad y cumplimiento, autenticación, privilegios y pruebas de seguridad | Gestión de identidades, Ley 25.326, evaluación de riesgo tecnológico | 1 | d14–d109 · 312 h · 41% |
| CP | Consultor de la plataforma | Configuración de flujos, reglas, motor de asignación, aplicación de campo, tableros, piloto y olas | Dominio de la plataforma FSM contratada, parametrización, transferencia de conocimiento | 1 | d58–d184 · 784 h · 78% |
| UX | Diseñador de experiencia de uso | Diseño y validación de la aplicación de campo y ajuste posterior al piloto | Diseño centrado en el usuario, ensayos con usuarios en contexto real, accesibilidad | 1 | d58–d145 · 192 h · 28% |
| QA | Responsable de pruebas | Plan y casos de prueba; ejecución funcional, de integración, de carga y de seguridad | Diseño de casos, pruebas de carga, gestión de defectos, criterios de aceptación | 2 | d27–d109 · 232 h · 18% |
| CA | Capacitador | Material de capacitación, dictado a gestión y a técnicos por olas, y evaluación | Didáctica de adultos, formación en campo, evaluación de aprendizaje | 1 | d105–d164 · 200 h · 42% |
| RO | Referente de operaciones | Conocimiento del proceso, matriz de competencias, datos maestros, piloto y acompañamiento del despliegue | Dominio del proceso de instalación, autoridad operativa, vínculo con supervisión y técnicos | 1 | d6–d184 · 704 h · 49% |

### JP — Jefe de proyecto

Interviene en 1.1, 1.2, 1.3, 3.1 a 3.5, 8.1, 8.4, 11.3 y 11.4. Requiere dirección de proyectos, conducción de un proceso de compras con RFI y RFP, y negociación contractual con el proveedor de la plataforma. En lo blando, capacidad de decisión ante el patrocinador y manejo de interesados con intereses contrapuestos. Recurso **interno**, de la Gerencia de Tecnología y Sistemas, según la designación del Acta.

### AF — Analista funcional

Es el perfil de mayor carga individual: 106 días-persona en catorce paquetes, desde 2.1 hasta 11.3. Requiere modelado de procesos, elicitación y especificación de requerimientos, y definición operativa de indicadores para el paquete 2.4. En lo blando, escucha activa y capacidad de traducir la lógica de campo a reglas configurables. Recurso **interno**.

### EI — Especialista de integraciones

Interviene en 2.3, 3.4, 5.1 a 5.4, 5.6, 6.1, 7.3, 7.6 y 11.2. Requiere dominio de interfaces y servicios web, mapeo y migración de datos, y conocimiento de los sistemas heredados de la organización. Se prevé **una persona interna** de la Gerencia de Tecnología y Sistemas y **una segunda contratada** por bolsa de horas al integrador, dado que el pico es transitorio y no justifica una incorporación permanente.

### ES — Especialista de seguridad

Interviene en 2.5, 3.3, 3.4, 5.5, 5.6 y 7.5. Requiere gestión de identidades y accesos, dominio de la Ley 25.326 y criterio para evaluar la exposición que introduce el modelo SaaS sobre el riesgo R05. En lo blando, firmeza para ejercer la facultad de bloqueo de puesta en producción que el Acta le confiere. Recurso **interno** de Seguridad de la Información.

### CP — Consultor de la plataforma

Interviene en 4.1 a 4.3, 4.6, 4.7, 7.6, 8.2, 8.3, 10.1 a 10.3 y 11.1. Es el perfil de mayor dedicación media (78%) y el único **provisto por el proveedor** como parte del servicio de implantación contratado. Requiere dominio de la plataforma FSM adjudicada y competencia para transferir ese conocimiento al equipo interno antes del cierre.

### UX — Diseñador de experiencia de uso

Interviene en 4.5, 4.6 y 8.3. Requiere diseño centrado en el usuario y, sobre todo, capacidad de ensayo en contexto real: uso con guantes, bajo sol directo y con conectividad intermitente. Se prevé **interno**; si la organización no dispusiera del rol, se contrata por obra dado el volumen acotado de 24 días-persona (*supuesto, a validar*).

### QA — Responsable de pruebas

Interviene en 7.1 a 7.5. Requiere diseño de casos, pruebas de carga y gestión de defectos, e independencia respecto de quien configura e integra. Recurso **interno**, con dos personas afectadas parcialmente.

### CA — Capacitador

Interviene en 9.1 a 9.4. Requiere didáctica de adultos y formación en campo, con material diferenciado para supervisión, despacho, NOC y técnicos. Recurso **interno**, aportado por Recursos Humanos junto con Supervisión de Instalaciones.

### RO — Referente de operaciones

Interviene en 2.1, 2.4, 2.6, 4.4, 6.2, 8.1, 8.2, 10.1 a 10.3 y 11.1. Es el perfil que aporta el conocimiento del proceso y la autoridad operativa para habilitar el piloto. Recurso **interno** de la Gerencia de Operaciones, con dedicación del 49% que debe acordarse con su supervisión por tratarse de personal de línea.

### Justificación del refuerzo en EI y QA

La duplicación de personas en estos dos perfiles no responde a una estimación de volumen sino al **aplanamiento de recursos del punto 10**. El análisis de sobreasignación detecta picos de dos personas en EI entre d68–d72 (paquetes 5.1 y 5.6) y entre d92–d96 (5.4 y 6.1), y en QA entre d97–d98 (7.2 y 7.3). Como 5.1 a 5.4 y 7.3 pertenecen al camino crítico, y 6.1 dispone de un solo día de holgura, esos conflictos no pueden resolverse corriendo actividades sin extender el proyecto. Con una sola persona por perfil, la programación aplanada arroja **215 días hábiles**; con el refuerzo de un EI y un QA adicionales, **192 días hábiles**, frente a los 187 días de la duración teórica a fechas tempranas. El refuerzo evita, entonces, 23 días hábiles de atraso. Un tercer refuerzo en RO solo reduciría la duración a 189 días, por lo que no se incorpora.

### Acumulación de roles

Con dedicaciones medias de entre 18% y 78%, la acumulación es posible pero acotada. **UX y CA admiten fusión en una misma persona**: sus ventanas se solapan entre d105 y d145, pero sus paquetes no coinciden en ningún día —9.1 finaliza en d113 y 8.3 comienza en d137—, y la carga conjunta alcanza 49 días-persona. Exige, eso sí, una persona con ambas competencias, lo que se declara como *supuesto a validar*. **CA es también compatible con JP** en términos de calendario, pero se descarta: la dedicación del 27% del jefe de proyecto surge únicamente de los paquetes en que es responsable, mientras que su función de seguimiento es continua y no está reflejada en la EDT.

No admiten acumulación: **ES con QA**, porque el paquete 7.5 los requiere simultáneamente y porque comprometería la independencia de la prueba respecto de quien implementó los controles; **ES con EI**, por el mismo motivo en 5.6; **AF**, por ser el perfil de mayor carga y estar presente en nueve de las once fases; **CP**, por su dedicación del 78% y su condición de recurso externo; y **RO**, porque es personal de la operación, cuya afectación al 49% ya representa el límite negociable con su área.

---

## 6. HIGIENE Y SEGURIDAD LABORAL

### Criterio de prevención adoptado

El análisis se ordena según los **tres niveles de prevención**: la **prevención primaria**, que evita el riesgo o su materialización; la **secundaria**, que actúa cuando la alteración de la salud ya comenzó aunque no se manifieste —vigilancia de la salud, exámenes periódicos, diagnóstico precoz—; y la **terciaria**, que evita recaídas, complicaciones o secuelas. La prevención primaria es la más eficaz y la más eficiente, y se descompone a su vez en cuatro acciones jerarquizadas de mayor a menor: **en el diseño** de instalaciones, equipos y puestos de trabajo; **en el origen**; **en el medio de transmisión**, interponiendo barreras entre la fuente y la persona; y **sobre la persona**, mediante equipo de protección personal, capacitación, vigilancia de la salud y reducción del tiempo de exposición.

Este punto asume de manera explícita que **la prevención sobre la persona es el escalón más débil** de esa jerarquía, porque su eficacia depende de una conducta individual que debe sostenerse en cada jornada y en cada trabajador. Por esa razón, cada medida se declara acompañada del nivel al que pertenece, y el layout se utiliza como el instrumento que materializa la prevención en el diseño: separación de circulaciones de peatones y vehículos, distancias mínimas, zonas de acceso restringido, ubicación de salidas, de elementos de extinción y del punto de encuentro. El equipo de protección personal se consigna como complemento y nunca como respuesta principal a un riesgo.

**Alcance.** Se analizan los sectores del **proceso crítico** —la instalación de internet con fibra óptica—, y no los sectores donde se ejecuta el proyecto. Esa lectura incorpora el trabajo de campo, que es donde se concentran los riesgos de mayor severidad. Se presentan **dos planos**: el de la **base operativa** y un **croquis tipo de trabajo en campo**.

### Medidas preventivas por sector

<!-- cols: 16,17,17,20,14,16 -->

| Sector | Personas expuestas | Riesgo | Medida preventiva | Nivel | Representación en el plano |
|---|---|---|---|---|---|
| Depósito y pañol de materiales | Personal de almacén, técnicos que retiran el kit de instalación | Caída de objetos desde estantería, sobreesfuerzo por manipulación manual de bobinas, atrapamiento por autoelevador | Estanterías ancladas con carga máxima señalizada y material pesado en el nivel inferior; zona de armado de kits separada de la de circulación; carros y medios mecánicos de elevación; faja y calzado de seguridad | 1 · Diseño, con complemento de nivel 4 | Trazado de estanterías, sentido de la senda peatonal demarcada, mesa de armado de kits y ubicación del matafuego clase ABC |
| Playa de carga y estacionamiento de vehículos técnicos | Técnicos, personal de almacén, conductores | Atropellamiento, aplastamiento en maniobra de retroceso, caída durante la carga y descarga | Circulación vehicular unidireccional; senda peatonal física y separada; velocidad máxima señalizada; espejo en el punto ciego; prohibición de retroceso sin señalero; chaleco reflectivo | 1 · Diseño y 3 · Medio | Sentido único de circulación con flechas, senda peatonal, dársenas de carga, espejo y cartelería de velocidad |
| Oficina del NOC (sala 24 horas) | Personal de soporte remoto, supervisores de turno | Fatiga visual, postura sostenida, ruido de fondo, riesgos psicosociales por turnos rotativos y trabajo nocturno | Puestos orientados de forma perpendicular a las ventanas e iluminación sin reflejo sobre la pantalla; monitores y sillas regulables; cableado en canaleta; diagrama de rotación de turnos con descanso planificado y pausas programadas | 1 · Diseño, con complemento de nivel 4 | Orientación de los puestos respecto de las ventanas y luminarias, cotas de distancia ojo-pantalla y recorrido de canaletas |
| Mesa de despacho y supervisión | Despachantes, supervisores de instalaciones | Los mismos riesgos del puesto de videoterminal, con mayor carga mental por atención simultánea | Límite de pantallas por operador; auriculares con limitador de nivel sonoro; superficie de trabajo con distancias de alcance definidas; rotación de tareas dentro del turno | 1 · Diseño y 4 · Persona | Cantidad y disposición de puestos, superficie por puesto y separación respecto de la sala del NOC |
| Sala técnica o nodo de distribución | Personal de infraestructura, NOC, técnicos autorizados | Riesgo eléctrico y arco eléctrico, temperatura elevada, ruido de equipos, acceso no autorizado | Acceso restringido con control de identidad; distancia libre de trabajo frente a tableros; procedimiento de bloqueo y etiquetado de energía; matafuego apto para equipos energizados; herramientas y calzado dieléctricos | 1 · Diseño y 3 · Medio | Recinto delimitado con puerta controlada, cotas de distancia libre frente a tableros, señal de riesgo eléctrico y matafuego clase C |
| Aula de capacitación | Técnicos, supervisores y despachantes en formación | Aforo excedido, evacuación dificultada, fatiga en jornadas extensas | Aforo declarado y verificado; puertas con apertura hacia el sentido de evacuación; recorrido libre hacia la salida; pausas programadas; prácticas de altura solo con supervisión | 1 · Diseño | Aforo indicado, ancho y sentido de apertura de puertas, luces de emergencia y recorrido señalizado hasta la salida |

<!-- cols: 16,16,16,19,16,17 -->

| Sector | Personas expuestas | Riesgo | Medida preventiva | Nivel | Representación en el croquis |
|---|---|---|---|---|---|
| Campo con tendido aéreo en vía pública | Técnicos instaladores, propios y contratistas; peatones y terceros | **Trabajo en altura**, **riesgo eléctrico por proximidad a línea energizada**, circulación vehicular, caída de herramientas sobre terceros | Distancia mínima de aproximación a la línea energizada como condición de inicio; escalera dieléctrica; vehículo con balizas ubicado aguas arriba como barrera física; vallado y conos que cierran la zona de caída de objetos; suspensión de la tarea con viento o tormenta; arnés con doble cabo sobre anclaje certificado y casco con barbijo | 1 · Diseño y 3 · Medio, con complemento de nivel 4 | Posición del vehículo respecto del flujo vehicular, perímetro vallado, cota de aproximación a la línea y desvío peatonal señalizado |
| Campo con cámara subterránea | Técnicos instaladores, vigía de superficie | **Espacio confinado**: atmósfera deficiente o explosiva, anegamiento, caída a distinto nivel | Permiso de trabajo escrito previo; medición de atmósfera antes del ingreso y durante la tarea; ventilación forzada; trabajo de a dos con vigía permanente en el exterior; arnés con línea de vida sobre trípode de rescate; vallado de la boca en sus cuatro lados | 1 · Diseño y 2 · Origen | Boca vallada en todo su perímetro, posición del vigía, del ventilador y del trípode de rescate |
| Domicilio del cliente | Técnico instalador, ocupantes de la vivienda | Riesgo eléctrico en el tablero domiciliario, caída desde escalera, animales sueltos, conflicto con el cliente | Verificación y corte de energía antes de intervenir; escalera propia certificada, nunca provista por el cliente; **lista de verificación de seguridad obligatoria en la aplicación de campo, que bloquea el inicio de la orden si no se completa**; protocolo de trabajo solitario con aviso de llegada y de cierre | 1 · Diseño y 4 · Persona | Esquema tipo con posición de la escalera, del tablero y de la zona despejada de trabajo |

> La lista de verificación previa al inicio de la orden es el caso donde el sistema del proyecto actúa como medida de prevención en el diseño: el control deja de depender de la memoria del técnico y pasa a ser una condición del flujo de trabajo configurado en la plataforma.

### Especificación de los planos

Los planos se confeccionan en planta, con escala uniforme y norte indicado, y comparten una misma simbología. Las cotas se expresan como **mínimos de diseño supuestos, a validar con el Servicio de Higiene y Seguridad de la organización**, dado que este trabajo no relevó medidas reales de las instalaciones.

#### Plano 1 — Base operativa

Debe contener el perímetro del predio con el acceso vehicular controlado y el acceso peatonal diferenciado; la playa de carga con sus dársenas y el estacionamiento de vehículos técnicos; el depósito con el trazado de estanterías, la zona de bobinas, la mesa de armado de kits y el pañol de herramientas; la oficina del NOC; la mesa de despacho y supervisión; la sala técnica o nodo; el aula de capacitación; y los sanitarios y vestuarios.

Sobre esa planta deben representarse: **circulaciones**, con la senda peatonal en trazo continuo y la circulación vehicular en trazo distinto y sentido único indicado por flechas, sin cruces no señalizados entre ambas; **cotas relativas** de ancho de senda peatonal, ancho de pasillo de circulación de vehículos y equipos de elevación, distancia libre frente a tableros eléctricos y distancia entre puestos de videoterminal; **señalización** de velocidad máxima, riesgo eléctrico, acceso restringido, carga máxima de estantería y aforo del aula; **matafuegos identificados por clase**, con clase ABC en depósito, playa de carga y aula, y clase C o agente limpio en la sala técnica y en la sala del NOC; **luces de emergencia y salidas de emergencia** con su sentido de apertura y el recorrido de evacuación señalizado desde cada sector; y el **punto de encuentro**, ubicado fuera del edificio, sobre superficie despejada y sin interferir la circulación vehicular. Se agregan la ubicación del botiquín y el recorrido de acceso de una ambulancia hasta el ingreso principal.

#### Plano 2 — Croquis tipo de trabajo en campo

Representa la escena de tendido aéreo en vía pública, en vista de planta con una vista lateral auxiliar. Debe incluir: calzada, vereda y sentido del tránsito; el poste con la línea de energía en el nivel superior y el tendido de fibra en el nivel inferior, acotando la distancia mínima de aproximación; el vehículo técnico con balizas ubicado aguas arriba del punto de trabajo, actuando como barrera física; el perímetro de conos y vallas que encierra tanto la zona de trabajo como la proyección de caída de objetos; el desvío peatonal señalizado; la posición del operario en altura con arnés y la del segundo operario a nivel de piso en función de vigía. Como esquemas complementarios se incorporan la cámara subterránea —boca vallada en sus cuatro lados, ventilación forzada, trípode de rescate y vigía en el exterior— y el domicilio del cliente.

> **Nota.** Ambos planos se adjuntan aparte, en archivo independiente, por su formato gráfico.

### Marco legal aplicable

<!-- cols: 20,40,40 -->

| Norma | Qué exige | Cómo se satisface en el proyecto |
|---|---|---|
| **Ley 19.587** de Higiene y Seguridad en el Trabajo y su decreto reglamentario **351/79** | Condiciones de higiene y seguridad de los establecimientos: características constructivas, iluminación, ventilación, protección contra incendios, señalización, provisión de equipo de protección personal y capacitación del trabajador sobre los riesgos de su tarea | Los dos planos y la tabla de medidas por sector constituyen la respuesta directa: circulaciones, distancias, señalización, matafuegos por clase, salidas y punto de encuentro. La capacitación es la fase 9 de la EDT y su evaluación queda registrada |
| **Ley 24.557** de Riesgos del Trabajo | Afiliación a una aseguradora de riesgos del trabajo, denuncia de accidentes y enfermedades profesionales, exámenes médicos periódicos y plan de prevención auditable por la Superintendencia de Riesgos del Trabajo | Los exámenes de aptitud para trabajo en altura y para riesgo eléctrico se registran como competencia habilitante del técnico, con fecha de vencimiento, en la matriz de competencias de la plataforma |
| **Ley 20.744** de Contrato de Trabajo | Deber de seguridad del empleador, jornada, descansos y régimen de trabajo nocturno y por turnos | El diagrama de rotación del NOC y de la mesa de despacho se configura respetando descansos entre turnos; la plataforma no despacha órdenes a técnicos fuera de su ventana horaria habilitada |
| **Ley 27.555** de Teletrabajo | Régimen del contrato de teletrabajo: jornada, derecho a la desconexión, provisión de elementos de trabajo y condiciones de higiene y seguridad en el domicilio | Aplica a los puestos de despacho y supervisión que operen en modalidad remota. Se declara como **supuesto a validar con Recursos Humanos** si esa modalidad se adopta; en caso afirmativo, el tablero de indicadores no genera alertas fuera de la jornada declarada |

La responsabilidad alcanza también a los **técnicos contratistas**, que ejecutan parte de las instalaciones. El pliego de contratación debe exigir constancia de cobertura de riesgos del trabajo, habilitaciones vigentes y entrega de equipo de protección personal, en las mismas condiciones que se exigen al personal propio.

### Conexión con el riesgo R04

La **habilitación registrada por técnico para trabajo en altura y para riesgo eléctrico** cumple simultáneamente dos funciones. Como medida de higiene y seguridad, materializa la vigilancia de la salud y la aptitud para la tarea que exigen la Ley 19.587 y la Ley 24.557. Como control de gestión, es el tratamiento del riesgo **R04** —técnico sin capacitación en el nuevo modelo de ONT, severidad 12, sin plan de tratamiento en la Etapa 2—, que este proyecto asume.

Lo que cambia con la plataforma es el modo de exigirla. Hoy la verificación depende del criterio del despachante y no queda registrada. Con la matriz de competencias cargada —paquete 4.4 de la Estructura de Desglose de Trabajo— y el motor de asignación configurado —paquete 4.3—, la habilitación vigente pasa a ser una **condición de despacho**: una orden que requiere trabajo en altura no puede asignarse a un técnico cuya certificación esté ausente o vencida. La medida deja de ser prevención sobre la persona, que depende de que alguien recuerde controlarla, y se convierte en prevención en el diseño del propio flujo de trabajo. Ese mismo control es el que sostiene el objetivo **O3**, la reducción de las visitas fallidas por causa evitable del 12% al 6% o menos.

---

## 7. ACTIVOS A ADQUIRIR

El modo de construcción adoptado —plataforma de *Field Service Management* contratada como servicio y configurada por la organización— determina la naturaleza de los activos: predominan las suscripciones y los servicios profesionales por sobre los bienes de capital. El único activo físico relevante son los dispositivos de campo. Cada activo se referencia contra el paquete de la EDT que lo requiere y contra el momento del cronograma en que debe estar disponible. Los valores de cantidad que dependen de la dotación real se declaran como supuestos y se validan en el relevamiento (paquete 2.1) y en la carga del padrón de técnicos (paquete 6.2).

### 7.1 Activos y servicios requeridos

<!-- cols: 18,16,50,16 -->

| Activo o servicio | Cantidad | Características mínimas exigibles | Paquetes EDT |
|---|---|---|---|
| Licencias de la plataforma FSM, nominativas, en tres tipos (campo, gestión y consulta) | 229 *(supuesto)* | Modo desconectado real —alta, edición y cierre de orden sin cobertura— con sincronización diferida y resolución de conflictos; motor de asignación por competencia certificada, zona, carga y ventana horaria, parametrizable sin programación; matriz impacto/urgencia con cronómetro de SLA; API REST documentada, versionada y con límites de consumo publicados; inicio de sesión único SAML 2.0 u OIDC y doble factor; registro de auditoría inalterable y exportable; región de alojamiento de datos declarada por contrato; disponibilidad mensual mínima del 99,5% con penalidad | 4.1 a 4.7, 5.1 a 5.6, 8.2, 10.1 a 10.3 |
| Servicio de implantación y configuración, prestado por partner certificado | 784 horas del perfil CP | Certificación vigente del fabricante de la plataforma; referencias comprobables en operaciones de servicio en campo; equipo nominado, con reemplazo sujeto a aprobación; configuración entregada versionada y documentada, con transferencia de conocimiento al equipo interno | 4.1 a 4.7, 7.6, 8.2, 8.3, 10.1 a 10.3, 11.1 |
| Horas de consultoría de integración | 560 horas del perfil EI, de las cuales 232 corresponden a las cuatro interfaces | Experiencia comprobable en integración con sistemas heredados; entrega del contrato de interfaz documentado por sistema; manejo de reintentos, idempotencia, registro de errores y plan de reproceso; verificación previa en ambiente no productivo | 2.3, 5.1 a 5.4, 5.6, 6.1, 7.3 |
| Dispositivos móviles rugerizados | 190 *(supuesto: 180 en servicio y 10 de reposición)* | Grado de protección IP68; resistencia a caída de 1,5 m sobre hormigón; autonomía mínima de 12 horas con batería reemplazable por el usuario; pantalla de 600 nits o superior, legible bajo sol directo; operación con guantes y con pantalla mojada; receptor GPS, cámara con enfoque a corta distancia para lectura de números de serie, y lector de código de barras; cifrado del almacenamiento y administración remota | 8.1, 9.3, 10.1 a 10.3 |
| Unidades de evaluación de dispositivos para prueba en campo | 6 *(supuesto)* | Al menos dos modelos de fabricantes distintos, para validar legibilidad, operación con guantes y autonomía en jornada completa antes de comprometer la compra | 4.5, 8.1 |
| Solución de administración de dispositivos móviles (MDM) | 190 suscripciones | Inventario, bloqueo y borrado remoto; contenedor de aplicaciones corporativas; política de contraseña y cifrado forzadas; modo quiosco; distribución y actualización centralizada de la aplicación de campo; baja del dispositivo sincronizada con la baja de la credencial | 5.6, 8.1, 10.1 a 10.3 |
| Servicio de mapas y geolocalización | Por transacción; volumen a validar | Geocodificación de domicilios, cálculo de ruta y matriz de distancias; cobertura verificada en el área de servicio; límite de consultas y disponibilidad declarados; prohibición contractual de reutilización comercial de los domicilios consultados | 4.3, 4.6 |
| Ambiente de pruebas no productivo | 1 ambiente | Paridad de versión y de configuración con producción; datos enmascarados; independiente de la instancia productiva; disponible desde el inicio de la configuración y sostenido después del cierre del proyecto | 4.1, 7.1 a 7.6 |
| Ampliación del servicio corporativo de identidad (inicio de sesión único y doble factor) | 229 identidades *(supuesto)* | Federación SAML 2.0 u OIDC contra el directorio corporativo; segundo factor por aplicación o token físico; aprovisionamiento y desaprovisionamiento automático integrado con Recursos Humanos | 5.5, 5.6, 7.5 |
| Servicio de capacitación | 200 horas del perfil CA | Material construido sobre el proceso y la configuración propios, no material genérico de producto; dictado por olas; evaluación con registro nominal por participante; derecho de reproducción interna del material | 9.1 a 9.4 |
| Soporte premium de estabilización | 12 meses desde la ola 1 | Mesa de ayuda en español; primera respuesta en menos de 1 hora para incidente crítico; escalamiento con responsable nominado; informe mensual de incidentes y de disponibilidad | 11.1, 11.2 |

Los umbrales indicados son exigencias del pliego, no mediciones: se confirman contra la oferta efectiva del mercado durante el análisis del RFI (paquete 3.2). Las líneas de datos móviles de los dispositivos no constituyen una adquisición externa, dado que la organización es operador móvil y la provisión se resuelve por autoconsumo interno con cargo por transferencia entre áreas.

**Momento de disponibilidad.** Las licencias y el ambiente de pruebas deben estar operativos al inicio del paquete 4.1, es decir el día 58 del cronograma, inmediatamente después de la firma del contrato (3.5). Los dispositivos del piloto se requieren antes del día 115, inicio de 8.1, y el parque completo antes del día 151, inicio de 10.1. El soporte premium se activa con la ola 1.

### 7.2 Dimensionamiento del licenciamiento

<!-- cols: 23,13,16,48 -->

| Tipo de usuario | Cantidad *(supuesto)* | Tipo de licencia | Fundamento del dimensionamiento |
|---|---|---|---|
| Técnico instalador de campo, propio y contratista | 180 | Campo (móvil) | Una licencia nominativa por técnico habilitado; es el volumen que gobierna el costo recurrente y el que más varía con la dotación tercerizada |
| Supervisor de instalaciones | 12 | Gestión | Requiere despacho, reasignación y tablero de su zona |
| Mesa de despacho | 10 | Gestión | Opera la cola única y el escalamiento de SLA |
| Centro de Operaciones de Red (NOC) | 8 | Gestión | Genera órdenes por excepción del NMS y sigue su estado |
| Consulta comercial | 15 | Consulta | Solo lectura del estado de la orden, sin acceso a la configuración |
| Administración de la plataforma | 4 | Gestión | Configuración de reglas, roles y tableros tras el traspaso a operación |

La cantidad exacta depende de la dotación real, que no fue relevada en las etapas anteriores: los valores anteriores son supuestos y se validan en el relevamiento del proceso. Por esa razón se exige que el contrato admita una banda de variación de más o menos veinte por ciento sobre la cantidad contratada sin renegociar el precio unitario, y que las licencias sean nominativas pero reasignables, condición indispensable frente a la rotación del personal contratista, que es la causa raíz del riesgo R05.

### 7.3 Criterios de evaluación de proveedores

Los criterios se fijan antes de emitir el RFP y se aplican en la evaluación de propuestas (paquete 3.4), con participación del jefe de proyecto, el analista funcional, el especialista de integraciones y el especialista de seguridad:

- **Aptitud funcional.** Cobertura nativa del motor de asignación por competencias y del modo desconectado, verificada en demostración con un caso propio y no con un guion del oferente. Toda función que exija desarrollo a medida se computa como riesgo, no como cumplimiento.
- **Aptitud técnica de integración.** Calidad y estabilidad de la API, límites de consumo, mecanismos de eventos, y disponibilidad de un ambiente no productivo para las pruebas de 7.1 a 7.6.
- **Seguridad y cumplimiento.** Certificación de gestión de seguridad vigente, región de alojamiento, capacidad de federación de identidad y de baja automática de credenciales, y aceptación de las cláusulas del apartado 8.2 sin reservas.
- **Capacidad de implantación.** Existencia de partner certificado en el país, referencias en operaciones de campo de escala comparable y disponibilidad efectiva del equipo en la ventana del día 58 al 184.
- **Condiciones económicas.** Costo total de propiedad a tres años, no precio de la primera factura: licenciamiento, implantación, integración, soporte y costo de salida.
- **Continuidad y salida.** Solvencia del proveedor, hoja de ruta del producto y condiciones de portabilidad de datos y de configuración al terminar el contrato.

---

## 8. FORMA DE ADQUISICIÓN

### 8.1 Modalidad por activo

<!-- cols: 18,17,65 -->

| Activo o servicio | Modalidad | Justificación de la modalidad elegida |
|---|---|---|
| Licencias de la plataforma FSM | Suscripción anual | En el modelo de servicio no existe licencia perpetua. Frente a la suscripción mensual, la anual reduce el precio unitario y fija su valor durante la implantación y los seis meses de medición de O1 a O3. Se descarta el compromiso plurianual inicial porque consolidaría la dependencia del proveedor antes de conocer el resultado del piloto |
| Servicio de implantación y configuración | Contrato de servicios por hora, con bolsa de 784 horas y tope | El precio cerrado exigiría congelar el alcance de configuración antes del piloto, cuando 8.3 prevé ajustar reglas y experiencia de uso con datos reales. La bolsa con tope acota el riesgo económico y permite reasignar horas entre paquetes sin adenda |
| Horas de consultoría de integración | Contrato de servicios por hora, con tope | El esfuerzo depende del estado real de los sistemas heredados, que se conoce recién en 2.3. Un precio cerrado se cotizaría con sobreprecio por incertidumbre y trasladaría a la organización un costo que no se va a consumir |
| Dispositivos móviles rugerizados | Compra directa | Su vida útil supera el horizonte del proyecto y el uso es permanente, no estacional. El alquiler encarece el costo total en ese plazo. Quedan como activo de la organización, se amortizan y se incorporan a la CMDB junto con el elemento de configuración dado de alta en 11.2 |
| Unidades de evaluación de dispositivos | Comodato | Se necesitan antes de decidir la compra y se devuelven. Adquirir modelos que luego se descartan sería un gasto perdido; el comodato traslada el costo de la prueba al oferente, sin obligación de compra y con devolución documentada |
| Solución de administración de dispositivos móviles | Suscripción anual por dispositivo | El parque varía con la dotación y el producto requiere actualización continua frente a nuevas versiones del sistema operativo, condición que una licencia perpetua no garantiza. La renovación anual permite ajustar la cantidad |
| Servicio de mapas y geolocalización | Pago por uso | El volumen de consultas es proporcional a las órdenes despachadas y no es estimable antes de la medición de líneas base (2.4). Un abono fijo se pagaría igual en meses de baja demanda. Se contrata con tope de gasto mensual y alerta de consumo |
| Ambiente de pruebas no productivo | Suscripción anual, exigida como ítem del mismo contrato de licenciamiento | Contratado por separado y por plazo corto, se pierde al cerrar el proyecto; la operación lo necesita de forma permanente para probar cada cambio antes de presentarlo al Comité Asesor de Cambios |
| Ampliación del servicio de identidad | Suscripción anual, como ampliación del acuerdo corporativo vigente | Se amplía el contrato existente en lugar de incorporar un proveedor nuevo: duplicar directorios de identidad reabriría el riesgo R05 en vez de tratarlo |
| Servicio de capacitación | Contrato de servicios por hora, liquidado por comisión dictada | La cantidad de comisiones depende de la dotación real de técnicos, conocida recién en 6.2. Una suma fija obligaría a comprometer ese número por anticipado |
| Soporte premium de estabilización | Suscripción anual con plazo acotado a doce meses | Cubre la estabilización y el período de medición de los objetivos, y luego se revisa contra el nivel de incidentes observado. Se descarta el pago por incidente porque incentiva a no reportar y distorsiona el indicador |

### 8.2 Cláusulas contractuales exigibles por tratamiento de datos personales

La alternativa contratada como servicio traslada fuera del perímetro de la organización datos personales de clientes: domicilio, teléfono, geolocalización de la visita, fotografía de la instalación y firma de conformidad. Ese traslado agrava el riesgo R05, valorado en severidad 15 en la Etapa 2, y constituye el flanco principal de la modalidad elegida. Su compensación es contractual, no técnica. Las cláusulas siguientes se especifican en el paquete 2.5, se incorporan al pliego en 3.3 y se negocian en 3.5 como condiciones no negociables; su cumplimiento efectivo se verifica en las pruebas de seguridad del paquete 7.5.

- **Región de alojamiento.** Declaración expresa de la región donde residen los datos y las copias de resguardo, con prohibición de traslado a otra jurisdicción sin autorización previa por escrito de la organización, y ajuste al régimen de transferencia internacional de la Ley 25.326.
- **Cifrado.** Cifrado en tránsito con protocolo actualizado y sin versiones obsoletas habilitadas, y cifrado en reposo de datos y copias de resguardo, con custodia de claves declarada y separada del personal de soporte.
- **Encargado de tratamiento.** El proveedor actúa como encargado y la organización conserva la condición de responsable. El proveedor trata los datos únicamente bajo instrucción documentada, no los utiliza para fines propios ni para el entrenamiento de modelos, y responde por sus subcontratistas, cuya nómina debe estar declarada y toda modificación notificada con antelación.
- **Gestión de credenciales.** Baja efectiva de la credencial en menos de veinticuatro horas desde la notificación de la organización, con constancia verificable, propagación de la baja al dispositivo a través del MDM, prohibición de cuentas genéricas y acceso de soporte del proveedor otorgado solo por incidente, con registro y vencimiento automático.
- **Derecho de auditoría.** Facultad de auditar una vez por año y ante todo incidente, por la organización o por un tercero designado, entrega anual del informe de certificación vigente y acceso exportable a los registros de auditoría. Notificación de brecha de seguridad en menos de veinticuatro horas, con plan de respuesta conjunto.
- **Salida y portabilidad.** Devolución de la totalidad de los datos y de la configuración en formato abierto y documentado dentro de los treinta días de terminado el contrato, borrado certificado de las copias, y período de asistencia para la reversión de al menos noventa días. El costo de la exportación debe estar fijado en el contrato y no puede quedar librado a cotización posterior, condición que sostiene la capacidad real de cambiar de proveedor.

El tratamiento normativo completo de estas obligaciones se desarrolla en el análisis de factibilidad legal del punto 12.

---

## 9. RFI Y RFP

La selección del proveedor de la plataforma de Field Service Management se resuelve mediante un proceso formal de compras, previsto en la fase 3 del ciclo de vida y descompuesto en los paquetes 3.1 a 3.5 de la Estructura de Desglose de Trabajo. Ese proceso utiliza dos instrumentos distintos y sucesivos: el pedido de información (RFI, *Request for Information*) y el pedido de propuesta (RFP, *Request for Proposal*). No son equivalentes ni intercambiables: responden a preguntas diferentes, se emiten en momentos diferentes y producen resultados de naturaleza diferente.

### Diferencia entre ambos instrumentos

<!-- cols: 17,40,43 -->

| Dimensión | RFI | RFP |
|---|---|---|
| Propósito | Explorar el mercado y conocer qué soluciones existen, quiénes las proveen y bajo qué condiciones generales | Obtener propuestas formales, comparables y evaluables de un conjunto acotado de proveedores ya identificados |
| Momento del proceso | Etapa temprana, antes de fijar las especificaciones definitivas de compra | Etapa avanzada, una vez conformada la lista corta y cerrado el pliego de requisitos |
| Grado de definición de los requerimientos | Bajo o medio: se conocen la necesidad y el problema, pero no las especificaciones técnicas exigibles | Alto: los requerimientos funcionales, de integración y de seguridad están especificados y aprobados |
| Qué se pide al proveedor | Información descriptiva sobre capacidades, arquitectura, modelos de licenciamiento y rangos de precio orientativos | Propuesta técnica y económica completa, con alcance, cronograma, equipo, niveles de servicio y condiciones contractuales |
| Qué se obtiene | Un mapa del mercado que permite depurar los requerimientos y descartar proveedores no aptos | Ofertas comparables entre sí, puntuables con criterios ponderados y base de la negociación posterior |
| Carácter vinculante | No vinculante para ninguna de las partes; no genera obligación de contratar ni compromiso de precio | Vinculante para el oferente en los términos y por el plazo de validez que fija el pliego; su aceptación deriva en contrato |

En síntesis, el RFI reduce la incertidumbre sobre el mercado y el RFP reduce la incertidumbre sobre la oferta. Emitir un RFP sin haber hecho antes el RFI obliga a redactar especificaciones sobre supuestos, con el riesgo de exigir características que ninguna plataforma del mercado regional ofrece —lo que deja el pliego desierto— o de omitir capacidades disponibles que la organización habría aprovechado.

### El RFI en este proyecto

El RFI corresponde al paquete de trabajo 3.1, tiene una duración estimada de cinco días hábiles, es responsabilidad conjunta del jefe de proyecto y del analista funcional, y forma parte del camino crítico del proyecto: se emite inmediatamente después de la validación de los requerimientos con los usuarios clave (paquete 2.6) y condiciona el inicio de todos los paquetes posteriores de la fase 3.

Su necesidad es directa. El proyecto adopta la modalidad SaaS: la organización no construye el producto, lo contrata y lo configura. En consecuencia, las especificaciones de compra no pueden fijarse en el vacío, porque dependen de qué es efectivamente configurable en las plataformas disponibles. El equipo no está en condiciones de redactar un pliego exigible antes de conocer la oferta real del mercado regional.

El relevamiento comprende los siguientes puntos:

- **Oferta disponible.** Qué plataformas de Field Service Management operan en el mercado regional, con qué presencia en la Argentina y con qué casos de implantación en empresas de telecomunicaciones o de servicios de campo de escala comparable.
- **Capacidad de integración nativa.** Cuáles cuentan con conectores nativos o interfaces de programación documentadas para sistemas de gestión de órdenes de trabajo y para sistemas de monitoreo de red. Es el punto de mayor peso: las cuatro integraciones de la fase 5 —SGOT, CRM, base de datos de clientes y órdenes, y NMS— concentran cuarenta y cinco días hábiles de trabajo del especialista de integraciones, y tres de ellas están sobre el camino crítico. La existencia de conectores nativos modifica esa estimación de manera sustantiva.
- **Modelo de licenciamiento y rangos de precio.** Si el licenciamiento es por usuario nominado, por usuario concurrente o por volumen de órdenes procesadas; qué rango de precio por usuario y por mes maneja cada proveedor, y qué componentes quedan fuera del precio base. Este dato es insumo directo del punto 11 y del costo total de propiedad a tres años.
- **Localización del alojamiento de datos.** Si el proveedor aloja los datos en la Argentina o en la región, y bajo qué certificaciones. La contrapartida asumida en el punto 3 —salida de datos personales de clientes del perímetro de la organización, con agravamiento del riesgo R05— convierte este punto en condición excluyente, no en preferencia.
- **Capacidad de operación sin conexión.** Qué alcance real tiene el modo *offline* de la aplicación de campo: qué operaciones admite sin conectividad, cómo resuelve la sincronización posterior y cómo trata los conflictos. Los objetivos O2 y O3 dependen de que el técnico pueda registrar el cierre en el domicilio del cliente, donde la conectividad es intermitente.

El producto del paquete 3.2 —análisis de respuestas y conformación de la lista corta, cinco días hábiles, también crítico— es el filtro que aplica estos criterios sobre las respuestas recibidas y deja tres o cuatro proveedores habilitados a recibir el pliego.

### El RFP en este proyecto

El RFP corresponde al paquete 3.3, tiene una duración de siete días hábiles, interviene el jefe de proyecto, el analista funcional y el especialista de seguridad, y también integra el camino crítico. Se emite únicamente a los proveedores de la lista corta y sobre la base de los requerimientos aprobados en el paquete 2.6 y de la información recogida en el RFI.

El pliego solicita:

- **Propuesta técnica**, con el detalle de la configuración prevista para los flujos de orden de trabajo, la matriz impacto/urgencia y los acuerdos de nivel de servicio, el motor de asignación por competencia certificada, zona, carga y ventana horaria, la aplicación de campo y los tableros de indicadores; y el detalle de las cuatro integraciones, indicando para cada una el mecanismo propuesto, el esfuerzo estimado y qué parte queda a cargo del proveedor y qué parte de la organización.
- **Propuesta económica**, discriminando el licenciamiento recurrente por usuario del servicio de implantación y configuración, y explicitando la política de actualización de precios durante la vigencia del contrato.
- **Cronograma** de implantación compatible con la planificación del proyecto, con hitos verificables y compromiso de disponibilidad del consultor de plataforma, cuya carga en la EDT alcanza noventa y ocho días-persona.
- **Equipo asignado**, con perfiles, antecedentes y dedicación comprometida de cada integrante.
- **Niveles de servicio de soporte y de disponibilidad**, con tiempos de respuesta por severidad, ventana de atención, disponibilidad mensual comprometida y penalidades por incumplimiento.
- **Plan de migración** de las órdenes de trabajo abiertas, del padrón de técnicos y de los datos maestros, correspondientes a los paquetes 6.1 y 6.2.
- **Condiciones contractuales de protección de datos y de salida**: región de alojamiento, cifrado en tránsito y en reposo, figura del encargado de tratamiento, notificación ante brecha, derecho de auditoría y cláusula de reversibilidad que garantice la devolución de los datos en formato utilizable al término del contrato.

### Por qué no se emite un RFQ

No corresponde un pedido de cotización (RFQ, *Request for Quotation*) porque el objeto de la contratación no es un bien de especificación cerrada, comparable únicamente por precio. Lo que se contrata es una solución que incluye licenciamiento, configuración funcional, cuatro integraciones con sistemas heredados, migración de datos, capacitación y soporte durante la estabilización: componentes cuyo alcance y calidad varían entre proveedores y determinan buena parte del riesgo del proyecto. Un instrumento que solo compara precios sería incapaz de discriminar entre una oferta con conectores nativos y otra que exige desarrollo a medida, aunque ambas cotizaran lo mismo. El RFQ sería adecuado, en cambio, para la compra de los dispositivos móviles rugerizados del punto 7, donde la especificación técnica sí puede cerrarse por anticipado.

### Secuencia y criterios de evaluación

La cadena de la fase 3 es: **3.1** emisión del RFI (5 días) → **3.2** análisis de respuestas y lista corta (5 días) → **3.3** emisión del RFP (7 días) → **3.4** evaluación de propuestas (8 días) → **3.5** negociación y firma del contrato (6 días). Los cinco paquetes son críticos y suman treinta y un días hábiles consecutivos: cualquier demora en la respuesta de los proveedores se traslada íntegramente a la fecha de finalización del proyecto.

La evaluación del paquete 3.4 se realiza con criterios ponderados definidos antes de abrir las propuestas. Los pesos se declaran como **propuesta del grupo**, sujeta a validación del área de Compras y Abastecimiento:

<!-- cols: 33,7,60 -->

| Criterio | Peso | Fundamento |
|---|---|---|
| Seguridad y protección de datos | 25% | Región de alojamiento, cifrado, baja automática de credenciales y derecho de auditoría; responde a R05 (severidad 15) y es condición de la factibilidad legal del punto 12 |
| Capacidad de integración | 20% | Conectores para SGOT, CRM, base de datos y NMS; las integraciones son la ruta crítica de la fase 5 y la fuente principal de riesgo de plazo |
| Funcionalidad del motor de asignación y del modo sin conexión | 20% | Es el tratamiento de R04 y R07 y la condición de cumplimiento de O2 y O3 |
| Costo total de propiedad a tres años | 15% | Licenciamiento recurrente más implantación e integración, no solo precio de lista |
| Plazo de implantación | 10% | Compatibilidad con el cronograma comprometido y con la disponibilidad del consultor de plataforma |
| Soporte local y niveles de servicio | 10% | Atención en el país, en idioma español y en la ventana horaria de la operación de campo |

Los tres primeros criterios concentran el 65% de la ponderación y se corresponden con los riesgos de la Etapa 2 que el proyecto trata o agrava. Se establece además un umbral de admisibilidad: la propuesta que no satisfaga la condición excluyente de alojamiento de datos en la región queda fuera de la evaluación, cualquiera sea su puntaje en los restantes criterios.

---

## 10. TIEMPOS DEL PROYECTO

### Método y supuestos

La estimación de tiempos se construye sobre la Estructura de Desglose de Trabajo del punto 4.3 mediante el **método del camino crítico (CPM)** con estimación **determinística**: a cada paquete de trabajo se le asigna una duración de valor único, obtenida por juicio experto y analogía con implantaciones de plataformas de servicio contratadas de alcance comparable. No se aplica estimación por tres valores (PERT), porque el objetivo del análisis es determinar la secuencia condicionante y las holguras, y no la distribución de probabilidad de la fecha de fin.

Los supuestos que sostienen el cálculo se declaran de manera explícita:

- **Unidad de medida.** Todas las duraciones se expresan en **días hábiles**. La jornada de trabajo es de **8 horas**; el mes se computa en **21 días hábiles**, criterio que se aplica de manera uniforme para convertir días a meses.
- **Tipo de dependencia.** Todas las relaciones de precedencia son **fin a comienzo con demora nula**. No se emplean adelantos ni superposiciones parciales entre actividades, de modo que el cálculo de fechas tempranas y tardías sea directamente verificable a partir de la tabla de precedencias.
- **Disponibilidad de recursos.** En la primera pasada de CPM se supone disponibilidad ilimitada de recursos, condición necesaria para que el camino crítico quede determinado únicamente por la lógica de precedencias. La restricción real de dotación se introduce después, en el aplanamiento.
- **Disponibilidad del proveedor.** Se supone que el consultor de la plataforma se incorpora sin demora una vez firmado el contrato (paquete 3.5). *Valor supuesto, a validar contra el plazo de movilización que el proveedor comprometa en la respuesta al RFP.*
- **Ausencias y calendario.** No se descuentan licencias, feriados ni recesos, por trabajarse en días hábiles netos y en escala relativa.
- **Dos precedencias adicionales respecto de la EDT.** El análisis de red incorpora dos dependencias que la descomposición del punto 4.3 no explicitaba: el paquete 8.1 (preparación del piloto) requiere además el informe de línea base (2.4), porque el piloto es la primera instancia en que se contrasta la operación contra los valores de partida de O1 a O4; y el paquete 11.3 (transferencia a operación) requiere además la evaluación de la capacitación (9.4), porque no puede transferirse la operación a un plantel cuya competencia sobre la herramienta no está evaluada.

**Por qué el cronograma se expresa en meses relativos.** El día 0 de la planificación es la **aprobación del Acta de Proyecto** por parte de la Gerencia de Operaciones, y todas las fechas se cuentan desde ese origen. Se adopta este criterio por tres razones. Primero, la fecha de aprobación depende del ciclo presupuestario de la organización y no está definida al momento de esta planificación: fijar una fecha de calendario obligaría a inventar un dato que ninguna de las etapas anteriores respalda. Segundo, si esa fecha se corriera, un cronograma anclado a calendario quedaría íntegramente invalidado, mientras que uno relativo conserva su validez y solo requiere trasladar el origen. Tercero, la escala relativa aísla la duración del proyecto —que es la variable que el análisis debe determinar— de las particularidades del calendario laboral argentino, que corresponde incorporar recién en la programación operativa, una vez conocida la fecha real de arranque.

En consecuencia, el **período estimado de inicio** es el mes inmediatamente posterior a la aprobación del Acta y del presupuesto asociado. Toda fecha de calendario que se derive de este cronograma es una proyección condicionada a ese hito.

---

### Diagrama de Red

El diagrama de red se construye con la notación de **actividad en el nodo** (*Activity on Node*, o diagrama de precedencias). Cada actividad es un nodo rectangular dividido en seis casillas: la fila superior contiene, de izquierda a derecha, el **inicio temprano (ES)**, la **duración (D)** y el **fin temprano (EF)**; la fila inferior contiene el **inicio tardío (LS)**, la **holgura total (HT)** y el **fin tardío (LF)**. El identificador y el nombre del paquete se ubican en la franja central del nodo. Las flechas representan relaciones de precedencia fin a comienzo y no consumen tiempo.

El cálculo se resuelve en dos pasadas. La **pasada hacia adelante** propaga las fechas tempranas desde el nodo inicial, tomando en cada nodo `ES = máx(EF de las predecesoras)` y `EF = ES + D`. La **pasada hacia atrás** propaga las fechas tardías desde el nodo final, tomando `LF = mín(LS de las sucesoras)` y `LS = LF − D`. La **holgura total** resulta de `HT = LS − ES = LF − EF`, y las actividades con holgura total nula constituyen el camino crítico.

El diagrama en formato gráfico, con los nodos y las flechas de precedencia dibujados, **se adjunta aparte** por no admitir el presente documento la inclusión de imágenes. La tabla que sigue contiene la totalidad de la información del diagrama y permite reconstruirlo íntegramente: las columnas de precedencia definen las flechas, y las columnas de fechas definen el contenido de cada nodo. Los identificadores en **negrita** corresponden a actividades críticas. Las denominaciones completas de cada paquete se encuentran en la tabla de la EDT del punto 4.3.

Todos los valores están expresados en días hábiles contados desde el día 0.

<!-- cols: 8,22,8,25,26,11 -->

| ID | Predecesoras | Dur. | Temprano ES–EF | Tardío LS–LF | Holgura |
|---|---|---|---|---|---|
| **1.1** | — | 3 | 0 – 3 | 0 – 3 | 0 |
| **1.2** | 1.1 | 2 | 3 – 5 | 3 – 5 | 0 |
| **1.3** | 1.2 | 1 | 5 – 6 | 5 – 6 | 0 |
| **2.1** | 1.3 | 8 | 6 – 14 | 6 – 14 | 0 |
| **2.2** | 2.1 | 10 | 14 – 24 | 14 – 24 | 0 |
| 2.3 | 2.1 | 6 | 14 – 20 | 18 – 24 | 4 |
| 2.4 | 2.1 | 15 | 14 – 29 | 98 – 113 | 84 |
| 2.5 | 2.1 | 5 | 14 – 19 | 19 – 24 | 5 |
| **2.6** | 2.2, 2.3, 2.5 | 3 | 24 – 27 | 24 – 27 | 0 |
| **3.1** | 2.6 | 5 | 27 – 32 | 27 – 32 | 0 |
| **3.2** | 3.1 | 5 | 32 – 37 | 32 – 37 | 0 |
| **3.3** | 3.2 | 7 | 37 – 44 | 37 – 44 | 0 |
| **3.4** | 3.3 | 8 | 44 – 52 | 44 – 52 | 0 |
| **3.5** | 3.4 | 6 | 52 – 58 | 52 – 58 | 0 |
| **4.1** | 3.5 | 10 | 58 – 68 | 58 – 68 | 0 |
| 4.2 | 4.1 | 6 | 68 – 74 | 77 – 83 | 9 |
| 4.3 | 4.2 | 8 | 74 – 82 | 83 – 91 | 9 |
| 4.4 | 3.5 | 7 | 58 – 65 | 107 – 114 | 49 |
| 4.5 | 3.5 | 8 | 58 – 66 | 83 – 91 | 25 |
| 4.6 | 4.3, 4.5 | 8 | 82 – 90 | 91 – 99 | 9 |
| 4.7 | 4.2 | 4 | 74 – 78 | 95 – 99 | 21 |
| **5.1** | 4.1 | 10 | 68 – 78 | 68 – 78 | 0 |
| **5.2** | 5.1 | 8 | 78 – 86 | 78 – 86 | 0 |
| **5.3** | 5.2 | 6 | 86 – 92 | 86 – 92 | 0 |
| **5.4** | 5.3 | 5 | 92 – 97 | 92 – 97 | 0 |
| 5.5 | 3.5 | 6 | 58 – 64 | 88 – 94 | 30 |
| 5.6 | 5.5 | 8 | 64 – 72 | 94 – 102 | 30 |
| 6.1 | 5.3 | 4 | 92 – 96 | 93 – 97 | 1 |
| 6.2 | 4.4 | 3 | 65 – 68 | 114 – 117 | 49 |
| 7.1 | 2.6 | 6 | 27 – 33 | 91 – 97 | 64 |
| 7.2 | 4.6, 4.7, 7.1 | 8 | 90 – 98 | 99 – 107 | 9 |
| **7.3** | 5.4, 6.1, 7.1 | 6 | 97 – 103 | 97 – 103 | 0 |
| **7.4** | 7.3 | 4 | 103 – 107 | 103 – 107 | 0 |
| 7.5 | 5.6, 7.1 | 5 | 72 – 77 | 102 – 107 | 30 |
| **7.6** | 7.2, 7.4, 7.5 | 6 | 107 – 113 | 107 – 113 | 0 |
| **8.1** | 7.6, 2.4 | 4 | 113 – 117 | 113 – 117 | 0 |
| **8.2** | 8.1, 6.2 | 15 | 117 – 132 | 117 – 132 | 0 |
| **8.3** | 8.2 | 8 | 132 – 140 | 132 – 140 | 0 |
| **8.4** | 8.3 | 2 | 140 – 142 | 140 – 142 | 0 |
| 9.1 | 7.2 | 8 | 98 – 106 | 134 – 142 | 36 |
| **9.2** | 8.4, 9.1 | 4 | 142 – 146 | 142 – 146 | 0 |
| 9.3 | 9.2 | 10 | 146 – 156 | 166 – 176 | 20 |
| 9.4 | 9.3 | 3 | 156 – 159 | 176 – 179 | 20 |
| **10.1** | 9.2 | 6 | 146 – 152 | 146 – 152 | 0 |
| **10.2** | 10.1 | 6 | 152 – 158 | 152 – 158 | 0 |
| **10.3** | 10.2 | 6 | 158 – 164 | 158 – 164 | 0 |
| **11.1** | 10.3 | 15 | 164 – 179 | 164 – 179 | 0 |
| 11.2 | 10.3 | 3 | 164 – 167 | 181 – 184 | 17 |
| **11.3** | 11.1, 9.4 | 5 | 179 – 184 | 179 – 184 | 0 |
| **11.4** | 11.2, 11.3 | 3 | 184 – 187 | 184 – 187 | 0 |

La red resultante contiene **treinta actividades críticas** y **veinte actividades con holgura**. El fin temprano del nodo terminal (11.4) se produce en el **día 187**, que es la duración del proyecto a fechas tempranas y con disponibilidad ilimitada de recursos.

---

### Camino crítico

El camino crítico está constituido por las treinta actividades con holgura total nula, encadenadas en la siguiente secuencia:

> 1.1 → 1.2 → 1.3 → 2.1 → 2.2 → 2.6 → 3.1 → 3.2 → 3.3 → 3.4 → 3.5 → 4.1 → 5.1 → 5.2 → 5.3 → 5.4 → 7.3 → 7.4 → 7.6 → 8.1 → 8.2 → 8.3 → 8.4 → 9.2 → 10.1 → 10.2 → 10.3 → 11.1 → 11.3 → 11.4

La suma de sus duraciones asciende a **187 días hábiles**, equivalentes a aproximadamente **8,9 meses** de 21 días hábiles. Cualquier demora en cualquiera de estas treinta actividades traslada la fecha de finalización del proyecto en igual magnitud.

El recorrido atraviesa ocho tramos con características distintas.

**Arranque y relevamiento (días 0 a 27).** Las tres actividades de inicio son cortas pero estrictamente secuenciales y ninguna admite paralelización: no se conforma el equipo antes de tener el Acta aprobada, ni se ejecuta la reunión de arranque antes de tener el equipo. El tramo de relevamiento entra al camino crítico por la vía de la especificación funcional (2.2, diez días), que es la más extensa de las tres especificaciones que confluyen en la validación con usuarios clave (2.6). Las especificaciones de integración y de seguridad, más breves, quedan absorbidas por esa ventana y conservan holguras de 4 y 5 días respectivamente.

**Selección del proveedor (días 27 a 58): el tramo más largo y menos comprimible.** Los cinco paquetes de la fase 3 —RFI, análisis de respuestas, RFP, evaluación de propuestas y negociación del contrato— suman **31 días hábiles**, es decir, casi el 17% de la duración total del proyecto, sin que se produzca en ese lapso ningún avance sobre el producto. Es el tramo crítico más resistente a la compresión, y por una razón estructural: sus duraciones no dependen de la capacidad del equipo del proyecto sino de **plazos externos y de terceros** —el tiempo que los proveedores del mercado toman para responder un RFI y un RFP, y el tiempo que consumen las instancias internas de compras y legales para cerrar un contrato de servicio con tratamiento de datos personales—. Añadir personas a esta fase no la acorta. Es, además, un tramo con un condicionante duro adicional: la fase 4 completa y las integraciones no pueden comenzar antes de la firma, porque el objeto que se configura y se integra todavía no está determinado. Toda la crítica del proyecto está represada detrás del paquete 3.5.

**Configuración de base e integraciones encadenadas (días 58 a 97).** Tras la firma, el camino crítico pasa por la configuración de flujos, estados y roles (4.1), que es la actividad de la que dependen tanto el resto de la configuración funcional como la primera integración. A partir de ahí, la criticidad se traslada íntegramente a la **cadena de integraciones 5.1 → 5.2 → 5.3 → 5.4**, veintinueve días hábiles consecutivos de SGOT, CRM, base de datos de clientes y órdenes, y sistema de monitoreo de red. Esta cadena es crítica por dos motivos simultáneos: existe una dependencia técnica real —la integración con el CRM presupone resuelto el modelo de orden de trabajo que aporta la integración con el SGOT, y la integración con el NMS presupone la base de datos ya sincronizada—, y las cuatro recaen sobre un **único perfil especialista de integraciones**. Es el punto donde la lógica de precedencias y la restricción de recursos se refuerzan mutuamente, y por eso constituye el objetivo principal del aplanamiento que se desarrolla más adelante.

**Pruebas (días 97 a 113).** El camino crítico entra a la fase 7 no por las pruebas funcionales sino por las **pruebas de integración** (7.3), que es la única que espera el cierre de la cadena 5.1–5.4 y la migración de órdenes abiertas. De ahí pasa a las pruebas de carga (7.4), que dependen de un ambiente ya integrado y estable, y desemboca en la corrección de observaciones y la reprueba (7.6), que actúa como punto de convergencia de las tres campañas de prueba —funcional, de carga y de seguridad— y como compuerta de calidad antes del piloto. Las pruebas funcionales y las de seguridad no son críticas: disponen de 9 y 30 días de holgura.

**Piloto (días 113 a 142).** Los cuatro paquetes de la fase 8 son íntegramente críticos y suman veintinueve días hábiles, de los cuales quince corresponden a la ejecución del piloto en zona acotada (8.2). Esa duración no es comprimible por asignación de recursos: el piloto necesita **transcurrir** un volumen suficiente de instalaciones reales para que los pesos del motor de asignación y la usabilidad de la aplicación de campo puedan calibrarse sobre datos de operación y no sobre supuestos. Es tiempo de calendario, no esfuerzo. El tramo cierra con el ajuste de reglas y experiencia de uso (8.3) y con el informe de piloto y la decisión de avance (8.4), que es el hito de aprobación más relevante del proyecto.

**Capacitación del personal de gestión (días 142 a 146).** El camino crítico atraviesa la capacitación de supervisores, despacho y NOC (9.2) y no la de los técnicos de campo (9.3). La razón es que el despliegue de la primera ola requiere que la mesa de despacho y el NOC estén operando sobre la nueva plataforma —son quienes reciben, priorizan y escalan—, mientras que los técnicos se capacitan por olas, en paralelo con el propio despliegue, y por eso 9.3 conserva 20 días de holgura.

**Tres olas de despliegue (días 146 a 164).** Las tres olas son secuenciales por decisión de diseño del ciclo de vida, no por dependencia técnica: cada ola es una entrega con valor propio y con decisión de avance o retroceso, y se despliega la siguiente solo cuando la anterior está estabilizada. Suman dieciocho días hábiles críticos y son, junto con el piloto, el tramo donde una decisión de gestión —no una restricción física— sostiene la criticidad. Comprimirlas es posible, pero implicaría renunciar al control de riesgo que el despliegue escalonado aporta.

**Estabilización y cierre (días 164 a 187).** El acompañamiento de la operación en período de estabilización (11.1) aporta quince días críticos, otra vez tiempo de transcurso más que de esfuerzo, seguido de la transferencia a operación (11.3) y del acta de cierre y lecciones aprendidas (11.4). El alta del elemento de configuración en la CMDB y el cierre del cambio ante el Comité Asesor de Cambios (11.2) corre en paralelo con 17 días de holgura.

---

### Actividades con holgura

Las veinte actividades no críticas se presentan ordenadas por holgura total descendente. La holgura total indica cuántos días hábiles puede demorarse el inicio de la actividad sin afectar la fecha de finalización del proyecto, y es la reserva de maniobra sobre la que opera el aplanamiento de recursos del apartado siguiente.

<!-- cols: 7,67,7,10,9 -->

| ID | Actividad | Dur. | Holgura | Perfil |
|---|---|---|---|---|
| 2.4 | Medir las líneas base de los objetivos O1 a O4 | 15 | 84 | AF, RO |
| 7.1 | Diseñar el plan y los casos de prueba | 6 | 64 | QA |
| 4.4 | Relevar y cargar la matriz de competencias por técnico | 7 | 49 | RO |
| 6.2 | Cargar el padrón de técnicos y los datos maestros | 3 | 49 | RO |
| 9.1 | Elaborar el material de capacitación | 8 | 36 | CA, AF |
| 5.5 | Implementar el inicio de sesión único y el doble factor | 6 | 30 | ES |
| 5.6 | Implementar el mínimo privilegio y la baja automática de credenciales | 8 | 30 | ES, EI |
| 7.5 | Ejecutar las pruebas de seguridad | 5 | 30 | ES, QA |
| 4.5 | Diseñar y validar la experiencia de uso de la aplicación de campo | 8 | 25 | UX |
| 4.7 | Configurar los tableros de indicadores | 4 | 21 | CP |
| 9.3 | Capacitar a los técnicos de campo por olas | 10 | 20 | CA |
| 9.4 | Evaluar la capacitación | 3 | 20 | CA |
| 11.2 | Dar de alta el elemento de configuración en la CMDB y cerrar el cambio ante el CAB | 3 | 17 | EI |
| 4.2 | Parametrizar la matriz impacto/urgencia y los acuerdos de nivel de servicio | 6 | 9 | CP, AF |
| 4.3 | Configurar el motor de asignación | 8 | 9 | CP, AF |
| 4.6 | Configurar la aplicación de campo según el diseño validado | 8 | 9 | CP, UX |
| 7.2 | Ejecutar las pruebas funcionales | 8 | 9 | QA, AF |
| 2.5 | Especificar los requerimientos de seguridad y cumplimiento | 5 | 5 | ES |
| 2.3 | Especificar los requerimientos de integración | 6 | 4 | EI |
| 6.1 | Migrar las órdenes de trabajo abiertas | 4 | 1 | EI |

**Lectura de las holguras mayores.** Las cuatro holguras más grandes no son un margen de comodidad sino una consecuencia estructural de la red, y conviene interpretarlas.

La medición de las líneas base (2.4) concentra la mayor holgura del proyecto, **84 días hábiles**. Puede iniciarse en cuanto termina el relevamiento del proceso actual, pero su único sucesor es la preparación del piloto, en el día 113. Esa distancia le otorga una libertad de posicionamiento que ninguna otra actividad tiene y la convierte en la primera candidata a ser desplazada en el aplanamiento. Ahora bien, esa holgura es de posición, no de omisión: la medición es el entregable que convierte los valores declarados como supuestos en los objetivos O1 a O4 en cifras verificables, y debe estar cerrada antes del piloto porque el piloto es la primera instancia de contraste contra ella. Postergarla es admisible; suprimirla o dejarla correr sobre el piloto destruiría la evidencia de resultado del proyecto.

El diseño del plan y los casos de prueba (7.1) dispone de **64 días**, porque puede elaborarse desde la aprobación de los requerimientos y sus sucesores recién se activan cuando hay configuración e integraciones que probar. Es holgura genuina y explica que el responsable de pruebas registre la dedicación media más baja del equipo.

Las dos actividades del referente de operaciones vinculadas a datos maestros —matriz de competencias (4.4) y padrón de técnicos (6.2)— comparten **49 días** de holgura. Ambas pueden ejecutarse en cuanto se firma el contrato, pero solo son exigidas por el piloto. Esta holgura es la que permite liberar al referente de operaciones durante la fase de relevamiento, donde su participación sí es crítica.

La cadena de seguridad 5.5 → 5.6 → 7.5 comparte **30 días** de holgura por tratarse de un ramal paralelo completo: nace en la firma del contrato y desemboca en la corrección de observaciones. Es el ramal no crítico más largo de la red y, como se verá, el único cuyo desplazamiento en el aplanamiento excede la holgura disponible y produce impacto real sobre la duración total.

En el extremo opuesto, la migración de órdenes de trabajo abiertas (6.1) tiene **un solo día** de holgura: es una actividad prácticamente crítica, y cualquier dificultad en la calidad de los datos migrados la incorpora de inmediato al camino crítico. Las cuatro actividades con 9 días —la parametrización, el motor de asignación, la aplicación de campo y las pruebas funcionales— forman un ramal de holgura compartida: consumida por una, desaparece para las restantes.

---

### Histograma de recursos y conflictos detectados

Construido el cronograma a fechas tempranas, se elabora el histograma de carga por perfil, que representa para cada día hábil la cantidad de personas requeridas de cada perfil. La condición de dotación de partida es de **una persona por perfil**, dado que el tamaño del proyecto no justifica equipos por especialidad. El histograma revela **seis conflictos de sobreasignación**, todos ellos de pico 2, es decir, ventanas en las que un mismo perfil resulta requerido simultáneamente por dos actividades.

<!-- cols: 9,10,14,7,60 -->

| Perfil | Ventana | Actividades | Pico | Naturaleza del conflicto |
|---|---|---|---|---|
| AF | d14 – d29 | 2.2, 2.4, 2.6, 3.1 | 2 | El analista funcional debe especificar los requerimientos y medir simultáneamente las líneas base; la medición es la actividad más larga de la fase y solapa además con la validación con usuarios y la emisión del RFI |
| RO | d24 – d27 | 2.4, 2.6 | 2 | El referente de operaciones es requerido a la vez por la medición de la línea base y por la validación de requerimientos con usuarios clave |
| EI | d68 – d72 | 5.1, 5.6 | 2 | La primera integración arranca mientras el especialista todavía interviene en la implementación del mínimo privilegio y la baja automática de credenciales |
| EI | d92 – d96 | 5.4, 6.1 | 2 | La integración con el NMS y la migración de órdenes abiertas parten ambas del cierre de la integración con la base de datos y compiten por el mismo especialista |
| CP | d74 – d78 | 4.3, 4.7 | 2 | El consultor de la plataforma debe configurar el motor de asignación y los tableros de indicadores en la misma ventana, ambos derivados de la parametrización de SLA |
| QA | d97 – d98 | 7.2, 7.3 | 2 | Las pruebas funcionales y las de integración se superponen dos días sobre el único responsable de pruebas |

El histograma muestra además que los conflictos no están distribuidos de manera uniforme. Se concentran en dos zonas: la **fase de relevamiento**, donde el analista funcional y el referente de operaciones son requeridos por todas las actividades a la vez, y la **franja de integración y pruebas** entre los días 68 y 103, donde el especialista de integraciones registra dos conflictos separados y el responsable de pruebas uno. Esta segunda zona coincide exactamente con el tramo del camino crítico en el que la lógica de precedencias es más rígida, lo que anticipa que resolver esos conflictos únicamente por corrimiento tendrá costo en duración.

---

### Aplanamiento de recursos

El objetivo del aplanamiento es eliminar las sobreasignaciones y obtener un perfil de carga sostenible, sin exceder para ningún perfil el límite de una persona por día. Se evaluaron dos estrategias.

#### Estrategia (a): nivelación pura, una sola persona por perfil

Consiste en resolver los seis conflictos exclusivamente por **corrimiento de actividades dentro de su holgura**, sin incorporar personal. La estrategia es viable para los conflictos del analista funcional, del referente de operaciones y del consultor de la plataforma, cuyas actividades en conflicto disponen de holgura suficiente. No lo es para los dos perfiles restantes.

En el caso del **especialista de integraciones**, los dos conflictos no pueden resolverse por corrimiento porque las actividades implicadas pertenecen a la cadena crítica 5.1–5.4 o dependen de ella con holgura casi nula: correr la implementación del mínimo privilegio agota su holgura de 30 días y empuja las pruebas de seguridad, y correr la migración de órdenes abiertas —que tiene un solo día de holgura— traslada de inmediato las pruebas de integración, que son críticas. En el caso del **responsable de pruebas**, la superposición de las pruebas funcionales y de integración solo se resuelve serializándolas, y como las de integración son críticas, la serialización empuja las pruebas de carga, la corrección de observaciones y, con ellas, todo el piloto.

El resultado es una duración total de **215 días hábiles**, frente a los 187 del cálculo a fechas tempranas: un incremento de **28 días hábiles**, equivalente a un **15%** de la duración del proyecto. El proyecto pasaría de aproximadamente 8,9 a 10,2 meses.

#### Estrategia (b): refuerzo selectivo de los dos perfiles cuello de botella

Consiste en incorporar **una segunda persona en los dos perfiles que concentran los conflictos irresolubles por corrimiento** —especialista de integraciones y responsable de pruebas—, y resolver los cuatro conflictos restantes por corrimiento dentro de la holgura disponible. Ambas incorporaciones son de **dedicación parcial**: el histograma resultante muestra para el especialista de integraciones una dedicación media del 22% sobre dos personas, y para el responsable de pruebas del 18%, de modo que en ningún caso se trata de sumar dos recursos de tiempo completo, sino de disponer de un segundo par de manos en las ventanas de solapamiento.

El resultado es una duración total de **192 días hábiles**, apenas **5 días** por encima del óptimo teórico de 187.

<!-- cols: 29,11,16,16,28 -->

| Estrategia | Duración | Diferencia | Dotación | Valoración |
|---|---|---|---|---|
| Cálculo CPM a fechas tempranas (recursos ilimitados) | 187 días | — | Teórica, no ejecutable | Referencia de comparación |
| (a) Nivelación pura, una persona por perfil | 215 días | +28 días (+15%) | 9 personas | Ejecutable, pero traslada el cierre casi un mes y medio |
| (b) Refuerzo de EI y QA con una persona parcial cada uno | 192 días | +5 días (+2,7%) | 11 personas | **Adoptada** |

#### Justificación de la estrategia adoptada

Se adopta la estrategia (b). La diferencia entre ambas es de **23 días hábiles** de duración del proyecto, poco más de un mes calendario, y el criterio de decisión es la comparación entre el sobrecosto de las dos personas adicionales y el costo de esos 23 días.

El sobrecosto de la incorporación es acotado y controlable, porque las dos personas se suman con dedicación parcial y en ventanas delimitadas: el segundo especialista de integraciones interviene esencialmente en dos tramos —la implementación de la capa de seguridad y la migración de órdenes abiertas— y el segundo responsable de pruebas, en la superposición de las campañas funcional y de integración y en la superposición de las pruebas de carga y de seguridad. Se trata de esfuerzo incremental medido en días-persona, no de dos posiciones de tiempo completo a lo largo de nueve meses.

El costo de los 23 días hábiles adicionales, en cambio, es de naturaleza distinta y de mayor alcance. Extender el proyecto un mes implica sostener durante ese mes **la totalidad de la estructura del proyecto**, no solo los dos perfiles en conflicto: la jefatura de proyecto, el consultor de la plataforma provisto por el proveedor, el referente de operaciones y los costos indirectos de gestión permanecen activos. A ello se suman tres efectos que no se expresan en el presupuesto del proyecto pero sí en el resultado de la organización. Primero, el licenciamiento recurrente de la plataforma comienza a devengarse desde la firma del contrato, de modo que cada día de demora en llegar a producción es un día de costo sin beneficio operativo. Segundo, los objetivos O1 a O4 tienen plazos contados desde la puesta en producción, y su verificación se desplaza en la misma medida. Tercero, el proyecto es el tratamiento comprometido de los riesgos R04 —técnico sin capacitación en el nuevo modelo de ONT— y R07 —ausencia de criterio de priorización en la cola de órdenes—, ambos valorados en severidad 12 y sin plan de tratamiento vigente: cada mes adicional de proyecto es un mes adicional de exposición a esos riesgos.

La comparación es concluyente: **el sobrecosto de dos incorporaciones parciales es menor que el costo de 23 días hábiles adicionales de proyecto**, y adicionalmente reduce el riesgo de cronograma, porque un plan que consume íntegramente las holguras para nivelar recursos deja al proyecto sin reservas frente a cualquier desvío.

**Sobre un tercer refuerzo evaluado y descartado.** Se analizó incorporar además un **segundo referente de operaciones**, con el fin de eliminar el corrimiento de la carga del padrón de técnicos y los datos maestros, que es el que retrasa cinco días el arranque del piloto. La duración total bajaría de 192 a **189 días hábiles**, es decir, apenas dos días por encima del óptimo teórico. La mejora de **3 días hábiles** no justifica la incorporación de una persona más: la relación entre el costo marginal y el beneficio marginal se deteriora abruptamente respecto de los dos refuerzos adoptados, que aportaron 23 días. Se descarta, en aplicación del criterio de rendimiento decreciente sobre la compresión del cronograma.

#### Corrimientos aplicados

La tabla siguiente registra los desplazamientos efectuados sobre el cronograma a fechas tempranas para obtener el cronograma aplanado adoptado. Los días se expresan en días hábiles desde el día 0.

<!-- cols: 7,51,9,9,14,10 -->

| ID | Actividad | Inicio orig. | Inicio nivel. | Corrimiento | Holgura |
|---|---|---|---|---|---|
| 2.4 | Medir las líneas base de los objetivos O1 a O4 | d14 | d82 | 68 | 84 |
| 4.7 | Configurar los tableros de indicadores | d74 | d90 | 16 | 21 |
| 5.6 | Implementar el mínimo privilegio y la baja automática | d64 | d96 | 32 | 30 |
| 4.4 | Relevar y cargar la matriz de competencias | d58 | d97 | 39 | 49 |
| 7.2 | Ejecutar las pruebas funcionales | d90 | d97 | 7 | 9 |
| 7.5 | Ejecutar las pruebas de seguridad | d72 | d104 | 32 | 30 |
| 7.4 | Ejecutar las pruebas de carga | d103 | d105 | 2 | 0 |
| 9.1 | Elaborar el material de capacitación | d98 | d105 | 7 | 36 |
| 7.6 | Corregir las observaciones y volver a probar | d107 | d109 | 2 | 0 |
| 8.1 | Preparar el piloto | d113 | d115 | 2 | 0 |
| 6.2 | Cargar el padrón de técnicos y los datos maestros | d65 | d119 | 54 | 49 |
| 8.2 | Ejecutar el piloto en zona acotada | d117 | d122 | 5 | 0 |
| 8.3 | Ajustar las reglas y la experiencia de uso | d132 | d137 | 5 | 0 |
| 8.4 | Elaborar el informe de piloto y decidir el avance | d140 | d145 | 5 | 0 |
| 9.2 | Capacitar a supervisores, despacho y NOC | d142 | d147 | 5 | 0 |
| 9.3 | Capacitar a los técnicos de campo por olas | d146 | d151 | 5 | 20 |
| 10.1 | Desplegar la ola 1 | d146 | d151 | 5 | 0 |
| 10.2 | Desplegar la ola 2 | d152 | d157 | 5 | 0 |
| 9.4 | Evaluar la capacitación | d156 | d161 | 5 | 20 |
| 10.3 | Desplegar la ola 3 | d158 | d163 | 5 | 0 |
| 11.1 | Acompañar la operación en estabilización | d164 | d169 | 5 | 0 |
| 11.2 | Alta del elemento de configuración en la CMDB y cierre ante el CAB | d164 | d169 | 5 | 17 |
| 11.3 | Transferir a operación y documentar | d179 | d184 | 5 | 0 |
| 11.4 | Elaborar el acta de cierre y las lecciones aprendidas | d184 | d189 | 5 | 0 |

**Descomposición de los 5 días de desvío.** Los 5 días hábiles que separan el cronograma aplanado de los 187 teóricos tienen dos orígenes identificables, y ninguno es arbitrario.

Los **primeros 2 días** provienen del ramal de seguridad. Los paquetes 5.6 y 7.5 debieron desplazarse 32 días cada uno para liberar al especialista de integraciones y al responsable de pruebas en sus ventanas de conflicto, mientras que su holgura disponible era de 30. El exceso de 2 días se propaga a las pruebas de carga (7.4), a la corrección de observaciones (7.6) y a la preparación del piloto (8.1), las tres críticas.

Los **3 días restantes** provienen de la carga del padrón de técnicos y datos maestros (6.2), que debió desplazarse 54 días —contra una holgura de 49— para escalonar la carga del referente de operaciones, y que es predecesora directa de la ejecución del piloto. El piloto no puede arrancar antes del día 122 aunque su preparación esté lista en el 119. Este es exactamente el desvío que un segundo referente de operaciones eliminaría, y el motivo por el cual esa alternativa llevaría el proyecto a 189 días.

A partir de la ejecución del piloto, el desvío acumulado de 5 días se traslada sin amplificarse a todas las actividades críticas subsiguientes, hasta el acta de cierre.

---

### Diagrama de Gantt

El diagrama de Gantt en formato gráfico —barras horizontales por actividad sobre el eje de tiempo, con el camino crítico destacado, las holguras representadas en trazo discontinuo y el histograma de recursos por perfil al pie— **se adjunta aparte**, por no admitir el presente documento la inclusión de imágenes.

La tabla siguiente presenta el cronograma aplanado agregado por fase, con el inicio y el fin expresados en días hábiles relativos al día 0 y su conversión a meses de 21 días hábiles, junto con la dotación simultánea máxima por perfil activa en cada fase. Las fases se solapan entre sí: el proyecto no es una secuencia de bloques estancos, y varias fases conviven en la misma ventana temporal.

<!-- cols: 33,14,12,41 -->

| Fase | Días | Meses | Personas por perfil |
|---|---|---|---|
| 1. Inicio | d0 – d6 | 0,0 – 0,3 | JP 1 |
| 2. Relevamiento y análisis | d6 – d97 | 0,3 – 4,6 | AF 1 · RO 1 · EI 1 · ES 1 |
| 3. Selección de proveedor | d27 – d58 | 1,3 – 2,8 | JP 1 · AF 1 · ES 1 · EI 1 |
| 4. Diseño y configuración | d58 – d104 | 2,8 – 5,0 | CP 1 · AF 1 · UX 1 · RO 1 |
| 5. Integración y seguridad | d58 – d104 | 2,8 – 5,0 | EI 2 · ES 1 |
| 6. Migración de datos | d92 – d122 | 4,4 – 5,8 | EI 1 · RO 1 |
| 7. Pruebas | d27 – d115 | 1,3 – 5,5 | QA 2 · AF 1 · ES 1 · EI 1 · CP 1 |
| 8. Piloto | d115 – d147 | 5,5 – 7,0 | JP 1 · RO 1 · CP 1 · UX 1 |
| 9. Capacitación | d105 – d164 | 5,0 – 7,8 | CA 1 · AF 1 |
| 10. Despliegue por olas | d151 – d169 | 7,2 – 8,0 | CP 1 · RO 1 |
| 11. Estabilización y cierre | d169 – d192 | 8,0 – 9,1 | CP 1 · RO 1 · EI 1 · JP 1 · AF 1 |

**Dotación total y carga por perfil.** El proyecto se ejecuta con **once personas** distribuidas en nueve perfiles, ninguna de ellas con dedicación exclusiva. La tabla siguiente consolida la carga resultante del cronograma aplanado. La columna de días-persona expresa el esfuerzo total de cada perfil; la ventana indica el intervalo entre su primera y su última intervención; la dedicación media es el cociente entre el esfuerzo y la ventana, e informa qué proporción del tiempo la persona está efectivamente afectada al proyecto.

<!-- cols: 38,11,15,8,19,9 -->

| Perfil | Personas | Días-persona | Horas | Ventana | Ded. media |
|---|---|---|---|---|---|
| Analista funcional (AF) | 1 | 106 | 848 | d6 – d189 | 58% |
| Consultor de la plataforma (CP) | 1 | 98 | 784 | d58 – d184 | 78% |
| Referente de operaciones (RO) | 1 | 88 | 704 | d6 – d184 | 49% |
| Especialista de integraciones (EI) | 2 | 70 | 560 | d14 – d172 | 22% |
| Jefe de proyecto (JP) | 1 | 51 | 408 | d0 – d192 | 27% |
| Especialista de seguridad (ES) | 1 | 39 | 312 | d14 – d109 | 41% |
| Responsable de pruebas (QA) | 2 | 29 | 232 | d27 – d109 | 18% |
| Capacitador (CA) | 1 | 25 | 200 | d105 – d164 | 42% |
| Diseñador de experiencia de uso (UX) | 1 | 24 | 192 | d58 – d145 | 28% |
| **Total** | **11** | **530** | **4.240** | **d0 – d192** | — |

El esfuerzo total del proyecto asciende a **4.240 horas-persona**, cifra que constituye el insumo directo del cálculo de costos de recursos humanos del punto 11.

Del histograma consolidado se desprenden tres observaciones de gestión. El **consultor de la plataforma** es el perfil de mayor dedicación media, 78%, y prácticamente no admite ser compartido con otras iniciativas: su ventana cubre desde la configuración inicial hasta la estabilización. El **jefe de proyecto** presenta la ventana más extensa —los 192 días completos— pero la dedicación media más baja entre los perfiles de conducción, 27%, distribución característica de un rol de coordinación con picos en el inicio, la contratación, el informe de piloto y el cierre. Los dos perfiles **reforzados**, con dedicaciones medias del 22% y del 18% sobre dos personas, confirman cuantitativamente el argumento del apartado anterior: el refuerzo no consiste en duplicar equipos, sino en disponer de una segunda persona en las ventanas de solapamiento.

---

### Duración estimada del proyecto

La duración estimada del proyecto es de **192 días hábiles**, equivalentes a **aproximadamente 9,1 meses** de 21 días hábiles cada uno, contados desde la aprobación del Acta de Proyecto.

<!-- cols: 28,19,53 -->

| Concepto | Valor | Observación |
|---|---|---|
| Duración CPM a fechas tempranas | 187 días hábiles | Óptimo teórico, con recursos ilimitados |
| Duración con nivelación pura | 215 días hábiles | Alternativa evaluada y descartada |
| **Duración aplanada adoptada** | **192 días hábiles** | **≈ 9,1 meses · 11 personas · 4.240 horas** |
| Desvío sobre el óptimo teórico | 5 días hábiles (2,7%) | 2 días por el ramal de seguridad, 3 por los datos maestros |
| Longitud del camino crítico | 30 actividades | 187 días de encadenamiento crítico |

**Sobre la fecha de inicio y el período de ejecución.** El día 0 del cronograma es la **aprobación del Acta de Proyecto** por parte de la Gerencia de Operaciones, hito que no está fechado y que depende de la aprobación presupuestaria correspondiente. En consecuencia, la duración de 192 días hábiles es firme, pero su ubicación en el calendario es condicional.

A título ilustrativo, y declarado expresamente como **supuesto de encuadre presupuestario**: si el Acta se aprobara dentro del **primer mes del ejercicio siguiente**, la ejecución se extendería desde ese mes hasta **alrededor del décimo mes** del mismo ejercicio, con el acta de cierre y las lecciones aprendidas emitidas en ese período. Bajo ese supuesto, la puesta en producción de la última ola de despliegue se alcanzaría hacia el **octavo mes** —día 169— y el período de estabilización ocuparía el tramo final. Este dato es relevante porque los plazos comprometidos en los objetivos O1 a O4 se cuentan desde la puesta en producción y no desde el cierre del proyecto: la verificación de O4 —cumplimiento de la priorización de la cola y del acuerdo de nivel de servicio de primera respuesta— vencería tres meses después de esa fecha, y las de O1 y O3, seis meses después, es decir, ya dentro del ejercicio siguiente al de ejecución.

**Condicionantes de la estimación.** Tres factores concentran el riesgo de cronograma y deben ser objeto de seguimiento específico. El **tramo de selección del proveedor**, con 31 días hábiles críticos gobernados por plazos de terceros, es el que menos admite compresión y el que más probabilidad tiene de desviarse; toda demora en la respuesta al RFI o al RFP, o en el cierre contractual, se traslada íntegramente a la fecha de finalización. La **cadena de integraciones 5.1–5.4**, con 29 días hábiles críticos consecutivos, depende de la disponibilidad y la calidad de las interfaces de los sistemas existentes —SGOT, CRM, base de datos de clientes y órdenes, y NMS—, que son activos de terceras áreas de la organización. Y el **piloto**, cuyos 15 días son tiempo de transcurso y no de esfuerzo, no puede acortarse sin degradar la calidad de la calibración del motor de asignación, que es precisamente el componente que trata el riesgo R04.

Finalmente, corresponde señalar que el cronograma aplanado **consume casi por completo las holguras de los ramales de seguridad y de datos maestros**. Esa es la contrapartida asumida al optar por una duración de 192 días en lugar de 215: el plan es más corto pero menos elástico en esas dos zonas, y cualquier desvío en ellas se traduce de manera inmediata en desplazamiento de la fecha de cierre. La reserva de contingencia que se dimensiona en el punto 11 debe cubrir explícitamente ese riesgo.

---

## 11. VARIABLES DE COSTO

Este punto identifica las variables que intervienen en el cálculo del costo del proyecto y les asigna una estructura cuantificada. La cátedra advierte que la factibilidad económica no puede sostenerse sobre una afirmación cualitativa, de modo que cada variable se acompaña de un valor estimado que habilita el análisis del punto 12. Todos los valores monetarios son **supuestos declarados** y deben validarse contra cotizaciones reales antes de comprometer presupuesto.

> **Nota metodológica — moneda.** Los importes se expresan en **dólares estadounidenses (USD)**. La razón es doble: el licenciamiento de las plataformas de *Field Service Management* de mercado y los servicios de implantación asociados se cotizan en esa moneda, y expresar la estimación en pesos la dejaría desactualizada por la variación del tipo de cambio antes de la propia ejecución del proyecto. La conversión a moneda local se realiza al momento de la imputación presupuestaria, con el tipo de cambio vigente.

### Variables consideradas

<!-- cols: 19,24,57 -->

| Variable de costo | Unidad de medida | Fuente del dato |
|---|---|---|
| Horas por perfil | Horas-persona | Tabla de carga por perfil derivada de la EDT y del aplanamiento de recursos del punto 10 (4.240 horas-persona) |
| Valor hora por perfil | USD por hora | Supuesto sobre el mercado argentino de servicios profesionales de TI; a validar con Recursos Humanos y con Compras |
| Licenciamiento de la plataforma | USD por usuario por mes | Propuesta económica del proveedor seleccionado en el RFP (paquete 3.4); cantidad de usuarios del padrón de operaciones |
| Servicio de implantación e integración | USD por hora del consultor, o precio cerrado | Propuesta del proveedor; incluye las 784 horas del consultor de la plataforma |
| Hardware de campo | USD por dispositivo | Cotización de dispositivos rugerizados; cantidad = dotación de técnicos más reserva |
| Administración de dispositivos móviles (MDM) | USD por dispositivo por mes | Suscripción del proveedor de MDM |
| Servicio de mapas y geolocalización | USD por mes, según volumen de consultas | Pago por uso, estimado sobre el volumen mensual de órdenes de trabajo |
| Ambiente de pruebas no productivo | USD por mes | Suscripción adicional del proveedor de la plataforma |
| Capacitación | USD por material y USD por hora improductiva del técnico capacitado | Paquetes 9.1 a 9.4 de la EDT y valor hora del técnico de campo |
| Soporte durante la estabilización | USD por mes de soporte reforzado | Cláusula de soporte del contrato, paquete 11.1 |
| Costos indirectos | Porcentaje sobre el costo directo | Política interna de imputación de estructura, gestión y espacios |
| Reserva de contingencia | Porcentaje sobre el costo directo más indirectos | Severidad de los riesgos vigentes de la Etapa 2 aplicables al proyecto |

### Costo de recursos humanos

Las horas provienen de la tabla de carga por perfil del punto 10, sobre jornada de ocho horas. El valor hora es un supuesto, coherente entre perfiles: se escalona según especialización y escasez del perfil en el mercado local.

<!-- cols: 44,11,8,19,18 -->

| Perfil | Personas | Horas | Valor hora (USD) | Subtotal (USD) |
|---|---|---|---|---|
| Jefe de proyecto (JP) | 1 | 408 | 45 | 18.360 |
| Analista funcional (AF) | 1 | 848 | 32 | 27.136 |
| Especialista de integraciones (EI) | 2 | 560 | 38 | 21.280 |
| Especialista de seguridad (ES) | 1 | 312 | 42 | 13.104 |
| Diseñador de experiencia de uso (UX) | 1 | 192 | 30 | 5.760 |
| Responsable de pruebas (QA) | 2 | 232 | 28 | 6.496 |
| Capacitador (CA) | 1 | 200 | 25 | 5.000 |
| Referente de operaciones (RO) | 1 | 704 | 22 | 15.488 |
| **Total recursos humanos propios** | | **3.456** | **32,59 (medio ponderado)** | **112.624** |

**Sobre el consultor de la plataforma.** El perfil CP acumula 784 horas y es provisto por el proveedor, no por la organización. Por eso **no se computa como costo de recursos humanos propios**: se imputa íntegramente dentro del servicio de implantación e integración contratado, en la tabla siguiente. La suma de ambos conceptos reconstituye las 4.240 horas-persona del proyecto (3.456 propias más 784 del proveedor) sin duplicar ningún importe.

### Costo de adquisiciones y servicios

Corresponde al primer año, contado desde la aprobación del Acta. El licenciamiento se computa desde la firma del contrato (mes 3) con dotación reducida durante configuración, pruebas y piloto, y con dotación plena a partir de la tercera ola de despliegue.

<!-- cols: 46,23,19,12 -->

| Concepto | Cantidad | Costo unitario (USD) | Subtotal año 1 (USD) |
|---|---|---|---|
| Licenciamiento FSM — configuración y piloto | 15 usuarios × 4 meses | 45 por usuario/mes | 2.700 |
| Licenciamiento FSM — producción | 78 usuarios × 5 meses | 45 por usuario/mes | 17.550 |
| Servicio de implantación e integración | 784 horas de consultor | 65 por hora | 50.960 |
| Bolsa de horas adicionales del proveedor | 120 horas | 65 por hora | 7.800 |
| Dispositivos móviles rugerizados | 63 unidades | 620 por unidad | 39.060 |
| Administración de dispositivos móviles | 63 × 5 meses | 4 por dispositivo/mes | 1.260 |
| Servicio de mapas y geolocalización | 5 meses | 900 por mes | 4.500 |
| Ambiente de pruebas no productivo | 10 meses | 500 por mes | 5.000 |
| Capacitación — material y plataforma | 1 | 3.000 | 3.000 |
| Capacitación — horas improductivas de técnicos | 60 técnicos × 4 horas | 12 por hora | 2.880 |
| Soporte reforzado de estabilización | 3 meses | 2.500 por mes | 7.500 |
| **Total adquisiciones y servicios — año 1** | | | **142.210** |

### Estructura del costo total

Se aplica la expresión indicada por la cátedra: **Costo total = recursos humanos + adquisiciones + servicios + costos indirectos + reserva de contingencia.** Los dispositivos rugerizados constituyen la única adquisición de bienes; el resto de la tabla anterior es servicio.

<!-- cols: 35,54,11 -->

| Componente | Cálculo | Importe (USD) |
|---|---|---|
| Recursos humanos propios | 3.456 horas al valor hora por perfil | 112.624 |
| Adquisiciones (bienes) | 63 dispositivos rugerizados | 39.060 |
| Servicios | Licenciamiento, implantación, MDM, mapas, ambiente, capacitación y soporte | 103.150 |
| **Subtotal costo directo** | | **254.834** |
| Costos indirectos | 12% sobre el costo directo | 30.580 |
| **Subtotal con indirectos** | | **285.414** |
| Reserva de contingencia | 15% sobre el subtotal con indirectos | 42.812 |
| **Costo total del año 1** | | **328.226** |

**Justificación del porcentaje de indirectos.** El 12% cubre estructura de gestión, puestos de trabajo, conectividad y servicios generales imputables al equipo del proyecto durante los 192 días hábiles de duración. Es un supuesto sujeto a la política de imputación interna.

**Justificación de la reserva de contingencia.** El 15% no es un porcentaje de estilo: responde a riesgos vigentes de la Etapa 2 con incidencia directa sobre este proyecto. R05 —credenciales de contratista sin baja, severidad 15— es el riesgo que obliga a la capa de seguridad más exigente y a las cláusulas contractuales de auditoría, cuya negociación puede encarecer la propuesta. R03 —firewall obsoleto sin soporte, severidad 15— condiciona la salida de tráfico hacia la plataforma contratada y puede forzar trabajo adicional de perimetral no previsto. R07 y R04, severidad 12 cada uno y sin plan de tratamiento previo, implican que las reglas de priorización y la matriz de competencias se calibran con datos que hoy no existen, lo que expone a reprocesos de configuración tras el piloto. Finalmente, la medición de las líneas base (paquete 2.4) puede arrojar valores que obliguen a recalibrar el alcance funcional.

### Costo total de propiedad a tres años

La tabla separa la inversión inicial, que ocurre una sola vez, del costo recurrente propio del modelo de contratación como servicio. La contingencia se reduce al 5% en los años 2 y 3, porque los riesgos de ejecución del proyecto ya no aplican en régimen de operación. El licenciamiento del año 3 incorpora una indexación contractual supuesta del 5%.

<!-- cols: 60,10,10,10,10 -->

| Concepto | Año 1 | Año 2 | Año 3 | Total |
|---|---|---|---|---|
| Recursos humanos propios y servicios de implantación | 234.484 | — | — | 234.484 |
| Licenciamiento de la plataforma | 20.250 | 42.120 | 44.226 | 106.596 |
| Servicios recurrentes (MDM, mapas, ambiente) | 10.760 | 13.824 | 13.824 | 38.408 |
| Soporte, evolutivos y administración funcional | — | 21.600 | 21.600 | 43.200 |
| Reposición de dispositivos (20% anual) | — | 7.812 | 7.812 | 15.624 |
| Dispositivos rugerizados | 39.060 | — | — | 39.060 |
| **Subtotal directo** | **254.834** | **85.356** | **87.462** | **427.652** |
| Costos indirectos (12%) | 30.580 | 10.243 | 10.495 | 51.318 |
| Contingencia (15% / 5%) | 42.812 | 4.780 | 4.898 | 52.490 |
| **Costo total del año** | **328.226** | **100.379** | **102.855** | **531.460** |

El año de ejecución del proyecto concentra el 62% del costo total de propiedad a tres años, y el 38% restante es recurrente. Ese 38% es el rasgo económico distintivo del modelo contratado como servicio: el compromiso presupuestario no termina con la puesta en producción, sino que se sostiene mientras la plataforma esté en operación y crece con la dotación licenciada. Un desarrollo propio habría invertido la proporción, concentrando el esfuerzo al inicio. Este dato es el insumo central del análisis de factibilidad económica del punto 12.

### Sensibilidad

Dos variables concentran la incertidumbre del cálculo.

**Cantidad de usuarios licenciados.** Es la variable recurrente y arrastra además el hardware de campo. Una desviación del 20% sobre los 78 usuarios supuestos —es decir, 62 o 94 usuarios— mueve el licenciamiento de los tres años en USD 25.693, la dotación de dispositivos en USD 7.812 en el año 1 y su reposición en USD 3.125 adicionales. Incorporando indirectos y contingencia, el efecto sobre el costo total de propiedad se aproxima a **USD 44.000, un ±8,3%**.

**Valor hora.** Una desviación del 20% sobre los valores supuestos afecta USD 22.525 del costo de recursos humanos propios, USD 11.752 del servicio de implantación y USD 3.840 de la administración funcional posterior. Con indirectos y contingencia, el impacto sobre el costo total de propiedad es de aproximadamente **USD 46.000, un ±8,6%**.

La conclusión operativa es que, con una dotación de este tamaño, **ambas variables pesan prácticamente lo mismo**: el mayor volumen de horas compensa el carácter recurrente de la licencia. Esa paridad se rompe si la dotación crece, porque el licenciamiento escala con los usuarios mientras el esfuerzo de implantación se paga una sola vez: por encima de unos 150 usuarios, el precio por usuario pasa a dominar. En consecuencia, la negociación del RFP debe atender por igual el valor hora del servicio de implantación y el tramo de precio por usuario, y en este último exigir la definición contractual de qué constituye un usuario licenciado —en particular si el técnico contratista consume licencia plena o de tipo restringido— y un mecanismo de reducción de usuarios ante bajas de dotación.

### Supuestos

<!-- cols: 23,17,60 -->

| Supuesto | Valor asumido | Base y validación pendiente |
|---|---|---|
| Moneda de la estimación | Dólar estadounidense | Práctica del mercado de licenciamiento; validar la política cambiaria de imputación con Administración y Finanzas |
| Valor hora por perfil | 22 a 45 USD/hora | Mercado argentino de servicios profesionales de TI; validar con Recursos Humanos y con las propuestas del RFP |
| Usuarios licenciados | 78 | Padrón estimado: 60 técnicos instaladores, 8 de supervisión y despacho, 6 del NOC y 4 de consulta comercial; validar contra el padrón real del alcance geográfico |
| Precio de licencia | 45 USD por usuario/mes | Estimación de mercado de plataformas FSM; se determina con la propuesta económica del RFP (paquete 3.4) |
| Valor hora del consultor de la plataforma | 65 USD/hora | Servicio de implantación del proveedor; puede cotizarse como precio cerrado en lugar de por hora |
| Dispositivos rugerizados | 63 unidades a 620 USD | Un dispositivo por técnico más 3 de reserva; validar con la especificación mínima exigible del punto 7 |
| Costos indirectos | 12% del costo directo | Política interna de imputación de estructura; validar con Administración y Finanzas |
| Reserva de contingencia | 15% en el año 1, 5% en régimen | Severidad de R03, R04, R05 y R07 de la Etapa 2; revisar tras la medición de líneas base |
| Indexación del licenciamiento | 5% anual desde el año 3 | Cláusula de ajuste a negociar en el contrato |
| Reposición de dispositivos | 20% anual del parque | Tasa de rotura y extravío en operación de campo; validar con el histórico de Logística |
| Horas improductivas de capacitación | 4 horas por técnico a 12 USD/hora | Duración del dictado del paquete 9.3; validar con el costo laboral real del técnico de campo |

Ninguno de estos valores proviene de una cotización formal. Todos deben confirmarse durante la fase 2 (Relevamiento y análisis) y, en el caso del licenciamiento y de los servicios de implantación, con las respuestas al RFI y al RFP, antes de que la Gerencia de Operaciones comprometa el presupuesto ante la Gerencia de Administración y Finanzas.

---

## 12. ANÁLISIS DE FACTIBILIDAD

El análisis se realiza sobre las tres dimensiones exigidas —técnica, económica y legal— y se apoya en la EDT del punto 4, en los perfiles del punto 5, en los activos y su forma de adquisición de los puntos 7 y 8, en los tiempos del punto 10 y en la estructura de costos del punto 11. Se mantiene la escala de valoración de riesgos empleada en la Etapa 2 —probabilidad de 1 a 5, impacto de 1 a 5, severidad de 1 a 25— para que ambas etapas resulten comparables.

### Factibilidad técnica

**Disponibilidad de la tecnología.** El proyecto no requiere tecnología por desarrollar: las plataformas de *Field Service Management* configurables ofrecidas como servicio son un producto maduro, con varios oferentes en el mercado y funcionalidad estándar de cola de despacho, motor de asignación, aplicación móvil con operación sin conectividad, captura de evidencia y tableros de indicadores. La confirmación de esta disponibilidad no se asume: es exactamente el propósito del paquete 3.1 (elaboración y emisión del RFI) antes de fijar especificaciones en el RFP del paquete 3.3.

**Integración con los sistemas existentes: el supuesto crítico del proyecto.** No está documentado si el SGOT (A3), el CRM (A1) y el NMS (A10) exponen interfaces de programación de aplicaciones aptas para integración. De ese hecho depende la viabilidad de los paquetes 5.1 a 5.4, que están sobre el camino crítico y concentran 560 horas del especialista de integraciones. Se declara explícitamente como riesgo abierto y no como hipótesis favorable. El paquete 2.3 —especificar requerimientos de integración— es el punto de verificación, y dispone de apenas 4 días de holgura, por lo que cualquier demora en el relevamiento de interfaces se traslada casi de inmediato al camino crítico. Ante la ausencia de interfaz de programación se prevén, en orden decreciente de preferencia: (i) **integración por base de datos intermedia**, con un esquema de intercambio y procesos programados de lectura y escritura contra vistas controladas del sistema de origen; (ii) **intercambio de archivos por lotes** en ventanas pactadas, con acuse y reproceso de rechazos, que degrada la trazabilidad de tiempo real a cuasi tiempo real; y (iii) **automatización de interfaz de usuario**, admitida solo como recurso transitorio para el sistema que no ofrezca ninguna otra vía, por su fragilidad ante cambios de pantalla y su costo de mantenimiento. Cada alternativa se traduce en horas adicionales del especialista de integraciones y debe cotizarse en el RFP.

**Sincronización sin conectividad y resolución de conflictos.** La aplicación de campo opera *offline-first*, de modo que dos dispositivos pueden modificar la misma orden sin red. El diseño de la resolución de conflictos es explícito: la orden tiene un único técnico asignado, que actúa como titular lógico, con lo que el conflicto queda acotado a reasignaciones en curso y a trabajos de cuadrilla; la reconciliación se resuelve **por campo y no por registro**, con marca temporal del dispositivo sincronizada contra servidor horario; las evidencias —fotografías, mediciones ópticas y conformidad— se tratan como registros de solo agregado, nunca sobrescribibles; y toda divergencia sobre el estado terminal de la orden deriva a una cola de excepciones que resuelve el despacho. El comportamiento se verifica en el paquete 7.3 y se somete a condiciones reales durante los 15 días del piloto (8.2).

**Capacidad y volumen.** Sobre la dotación supuesta de 60 técnicos, el caudal estimado es de unas 240 órdenes diarias, con un pico de sincronización concentrado al cierre de la jornada. El riesgo no está en la plataforma contratada sino en la capacidad de la interfaz del SGOT heredado, que no fue dimensionada para ese patrón. Las medidas previstas son cola de mensajes con reintento y espera creciente, sincronización incremental por diferencias, escalonamiento de ventanas por zona y acuerdo de cupo con el área propietaria del SGOT. El paquete 7.4 —pruebas de carga, 4 días, sobre el camino crítico— es el que valida o refuta el dimensionamiento.

**Capacidad de la organización.** La organización cuenta con Centro de Operaciones de Red propio en régimen continuo (A4), áreas de Tecnología y de Seguridad de la Información, y un inventario de activos ya relevado y valorado en la Etapa 2, lo que permite conocer de antemano sobre qué componentes se apoya la solución. El equipo del proyecto aporta 4.240 horas-persona en 192 días hábiles, con el conocimiento del producto cubierto por el consultor de la plataforma provisto por el proveedor. Dos riesgos de infraestructura, ajenos al alcance, condicionan la operación: **R03** —firewall sin soporte del fabricante, severidad 15— y **R09** —balanceador sin redundancia, severidad 10— afectan el canal por el cual la aplicación de campo alcanza los sistemas internos. El proyecto no los trata, pero los declara como dependencia externa.

<!-- cols: 6,40,4,4,6,40 -->

| ID | Riesgo técnico | P | I | Sev | Respuesta |
|---|---|---|---|---|---|
| RT1 | El SGOT, el CRM o el NMS no exponen interfaz de programación apta | 4 | 5 | 20 | Verificar en 2.3 antes del RFP; plan alternativo por base intermedia, lotes o automatización de interfaz, con horas cotizadas en el RFP |
| RT2 | La interfaz del SGOT no soporta el caudal de sincronización | 3 | 4 | 12 | Cola con reintento, sincronización por diferencias, ventanas escalonadas, cupo acordado; validación en 7.4 |
| RT3 | Conflictos de sincronización sin conectividad | 3 | 3 | 9 | Titularidad única de la orden, reconciliación por campo, evidencias de solo agregado, cola de excepciones; prueba en 7.3 y en el piloto |
| RT4 | Cobertura celular insuficiente en zonas de instalación | 3 | 3 | 9 | Operación sin conectividad como requisito no negociable del RFP; sincronización diferida y validación en el piloto |
| RT5 | Indisponibilidad del canal por R03 y R09 | 2 | 5 | 10 | Dependencia externa declarada; escalamiento al plan de tratamiento propio de R03 y R09 |
| RT6 | Falsos positivos del NMS (R10) contaminan la generación de órdenes | 3 | 2 | 6 | Umbral de confirmación y validación humana en el NOC antes del despacho automático |
| RT7 | Datos maestros de competencias incompletos o desactualizados | 3 | 3 | 9 | Paquete 4.4 con validación del referente de operaciones; certificación vencida bloquea la asignación |
| RT8 | Interrupción o discontinuidad del servicio del proveedor | 2 | 4 | 8 | Nivel de servicio y penalidades en contrato, exportación periódica de datos en formato abierto, cláusula de reversibilidad |

### Factibilidad económica

**Base de cálculo.** Se adopta la estructura de conceptos del punto 11. Los importes se expresan en dólares estadounidenses constantes, para independizar el análisis de la variación del poder adquisitivo de la moneda local. Los valores unitarios y volumétricos que no surgen de las etapas anteriores se declaran como **supuestos a validar** contra las cotizaciones que se obtengan del RFP y contra la medición de líneas base del paquete 2.4.

<!-- cols: 24,16,60 -->

| Supuesto | Valor | Observación |
|---|---|---|
| Dotación de técnicos instaladores | 60 | Valor supuesto, a validar |
| Horas-técnico disponibles por año | 120.960 | 60 × 8 h × 21 días × 12 meses |
| Órdenes despachadas por año | 68.700 | Derivado de la línea base O1 (0,50 inst./hora-técnico) y de O3 (12% de visitas fallidas) |
| Costo de un desplazamiento fallido | 25 | Valor supuesto: combustible, peaje y desgaste. **No** incluye la franja de agenda perdida, ya computada en O1 |
| Costo anual cargado de un técnico | 18.000 | Valor supuesto, a validar |
| Costos del proyecto y de operación | Los del punto 11 | No se recalculan aquí: se toman de la estructura de costos y del costo total de propiedad del punto 11 |
| Tasa de descuento | 15% anual | Costo de capital supuesto, en moneda constante |
| Horizonte de evaluación | 5 años | Vida útil del parque de dispositivos y plazo razonable del contrato de licenciamiento |

**Costos.** Se toman del punto 11 sin recalcularlos. Corresponde una distinción metodológica: el **presupuesto** del proyecto asciende a USD 328.226 e incluye la reserva de contingencia, porque es el monto que debe autorizarse; la **inversión que se descuenta** en la evaluación es de USD 285.414, es decir el costo directo más los indirectos, sin la reserva, porque una reserva de contingencia es una previsión ante riesgo y no una erogación esperada. Si los riesgos se materializan, el resultado se deteriora en la proporción en que la reserva se consuma.

<!-- cols: 49,41,10 -->

| Concepto | Origen | Importe (USD) |
|---|---|---|
| Costo directo del proyecto | Punto 11, subtotal costo directo | 254.834 |
| Costos indirectos | Punto 11, 12% sobre el directo | 30.580 |
| **Inversión considerada en la evaluación** | | **285.414** |
| Reserva de contingencia (no descontada) | Punto 11, 15% | 42.812 |
| **Presupuesto total a autorizar** | | **328.226** |
| Costo operativo anual en régimen | Punto 11, costo total del año 2 | 100.379 |

<!-- cols: 16,74,10 -->

| Origen | Cuantificación | Importe anual |
|---|---|---|
| O1 | +5% de productividad equivale a 3 técnicos de capacidad adicional sin ampliar la dotación: 3 × 18.000 | 54.000 |
| O2 | 70% de las órdenes pasa a cerrarse en el momento (48.090 órdenes) con 6 minutos menos de carga administrativa diferida: 4.809 h × 12 | 57.700 |
| O3 | Visitas fallidas evitables reducidas de 8.244 a 4.122 por año: 4.122 × 25 | 103.000 |
| Costos evitados | Reclamos y consultas duplicadas por falta de visibilidad, reducidos en un 70%: 3.847 casos × 10 min × 12 | 7.700 |
| **Total** | | **222.400** |

**Flujo de fondos y evaluación.** El año 0 corresponde a los 9,1 meses de ejecución del proyecto. Se supone una realización del 60% de los beneficios durante el primer año de operación, por la rampa de despliegue en tres olas, el período de estabilización y el recálculo de metas sobre las líneas base medidas. El costo operativo se indexa un 2,5% anual.

<!-- cols: 8,20,18,18,18,18 -->

| Año | Beneficio | Costo oper. | Flujo neto | Factor 15% | Valor actual |
|---|---|---|---|---|---|
| 0 | — | — | −285.414 | 1,0000 | −285.414 |
| 1 | 133.440 | 100.379 | 33.061 | 0,8696 | 28.749 |
| 2 | 222.400 | 102.855 | 119.545 | 0,7561 | 90.393 |
| 3 | 222.400 | 105.427 | 116.973 | 0,6575 | 76.912 |
| 4 | 222.400 | 108.062 | 114.338 | 0,5718 | 65.373 |
| 5 | 222.400 | 110.764 | 111.636 | 0,4972 | 55.505 |

Aplicando las técnicas de evaluación de inversiones de la unidad:

- **Tiempo de repago (TPR):** **3,14 años** desde la aprobación del Acta, es decir aproximadamente 2,4 años desde la puesta en producción.
- **Tasa de retorno (TR):** flujo neto en régimen de 119.545 sobre una inversión de 285.414, equivalente al **42% anual**.
- **Valor actual neto (VAN) a cinco años, al 15%:** **+USD 31.515**. Es positivo, de modo que el proyecto supera el costo de capital supuesto, pero por un margen estrecho: representa un 11% de la inversión.
- **Tasa interna de retorno (TIR):** **19,0%**, cuatro puntos por encima de la tasa de corte. A tres años el VAN es negativo; el proyecto necesita el cuarto y el quinto año de operación para justificarse.

**Análisis honesto del resultado.** El proyecto es económicamente viable, pero el margen es ajustado y conviene decirlo sin adornos. El umbral de indiferencia se alcanza cuando se realiza el **85% de los beneficios estimados**: por debajo de eso el valor actual neto se vuelve negativo. En un escenario pesimista de realización sostenida del 60% —plenamente posible, porque las líneas base de O1, O2 y O3 son hoy supuestos y no mediciones— el valor actual neto cae a **−USD 189.336**. La sensibilidad del resultado no está en los costos, que son razonablemente acotados, sino en los beneficios.

De los cuatro orígenes de beneficio, el más frágil es **O1**: el aumento de productividad solo se convierte en resultado económico si existe demanda insatisfecha que absorba la capacidad liberada. El hecho de que la cola de órdenes carezca de criterio de priorización (R07) sugiere que la hay, pero es un supuesto y no un dato. El más sólido es **O3**, porque cada visita fallida evitada es una erogación que efectivamente no se realiza.

En consecuencia, la decisión de avance posterior al piloto (paquete 8.4) debe adoptarse **después** de la medición de líneas base del paquete 2.4, que es su predecesora en la red. Si esa medición contradice los supuestos, corresponde recalibrar las metas y reevaluar la conveniencia económica antes del despliegue masivo, que es donde se compromete el grueso del licenciamiento y de los dispositivos.

### Factibilidad legal

**Ley 25.326 de Protección de Datos Personales.** Las órdenes de trabajo contienen datos personales de clientes —nombre, domicilio, teléfono, datos del servicio— y, con la aplicación de campo, se agregan fotografías del domicilio y coordenadas de la instalación. Al alojarse en una plataforma contratada como servicio, esos datos salen del perímetro de la organización, con tres consecuencias jurídicas. Primera, el proveedor asume la condición de **encargado del tratamiento**: por el artículo 25, el tratamiento por cuenta de terceros debe instrumentarse por contrato, los datos no pueden aplicarse a una finalidad distinta ni cederse, y deben destruirse al concluir la relación. Segunda, si el alojamiento se ubica fuera del país se configura una **transferencia internacional de datos**, prohibida por el artículo 12 hacia países que no brinden nivel adecuado de protección, salvo consentimiento o cláusulas contractuales que aseguren garantías equivalentes, para lo cual la autoridad de aplicación tiene aprobados modelos de cláusulas contractuales tipo. Tercera, subsisten en cabeza de la organización el **deber de seguridad y de confidencialidad** de los artículos 9 y 10, y la inscripción de la base de datos ante la Agencia de Acceso a la Información Pública; las medidas de seguridad recomendadas por la autoridad prevén además la **notificación de incidentes**, que el proyecto convierte en obligación contractual con plazo cierto. La conexión con la Etapa 2 es directa: **R05 —credenciales de contratista no dadas de baja, severidad 15—** deja de ser un problema de acceso interno para convertirse en un incumplimiento del deber de seguridad sobre datos personales alojados fuera del perímetro. El paquete 5.6 (mínimo privilegio y baja automática de credenciales) es su control técnico, y las cláusulas del punto 8 —región de alojamiento habilitada, cifrado en tránsito y en reposo, notificación de bajas en menos de 24 horas, derecho de auditoría y reversibilidad— son su control contractual. Ninguna de las dos es prescindible.

**Ley 27.078 Argentina Digital y normativa del ENACOM.** El servicio involucrado es un servicio de TIC en competencia, sujeto al régimen de calidad dictado por el ENACOM, que fija parámetros de tiempo de respuesta, plazos de instalación y reparación, y régimen de información al regulador. Los acuerdos de nivel de servicio que el proyecto instrumenta en el objetivo O4 deben ser, como mínimo, tan exigentes como los parámetros regulatorios; el proyecto no los reemplaza, los operacionaliza. Como beneficio colateral, la traza completa de la orden de trabajo constituye el respaldo probatorio ante requerimientos del regulador, hoy inexistente por la propia falta de trazabilidad que motiva el proyecto.

**Ley 24.240 de Defensa del Consumidor.** El artículo 4 impone información cierta, clara y detallada sobre las condiciones de la prestación, y el artículo 8 bis el trato digno. Las notificaciones de estado de la instalación y la ventana horaria comprometida son cumplimiento de ese deber, no una prestación accesoria. Sobre la conformidad digital cabe una precisión: la información al consumidor debe brindarse gratuitamente y en soporte físico, salvo que el consumidor **opte expresamente** por otro medio; por lo tanto, la aplicación debe registrar esa opción y ofrecer siempre la entrega de una copia de la conformidad, cuya conservación queda a cargo de la organización.

**Ley 25.506 de Firma Digital.** La distinción es determinante. La **firma digital** requiere certificado emitido por un certificador licenciado y goza de presunción de autoría e integridad (artículos 7 y 8): quien la desconoce debe probar la falsedad. La **firma electrónica** es, por el artículo 5, todo otro método que carezca de alguno de esos requisitos, y su valor probatorio es inverso: quien la invoca debe acreditar su validez. La conformidad trazada por el cliente sobre la pantalla del dispositivo es firma electrónica, no digital. Se asume esa condición y se la compensa con evidencia complementaria —geolocalización de la instalación, marca temporal, fotografías, mediciones ópticas y registro de auditoría inalterable—, que es precisamente lo que hoy no existe en el proceso manual. Si la organización requiriera plena eficacia probatoria, deberá contratar un servicio de firma digital con certificador licenciado, con su costo asociado; se deja planteado y no se lo incorpora al alcance.

**Legislación laboral y responsabilidad por contratistas.** El trabajo de campo queda alcanzado por la Ley 19.587 de Higiene y Seguridad y su decreto reglamentario, y por la Ley 24.557 de Riesgos del Trabajo, con las medidas desarrolladas en el punto 6 —trabajo en altura, riesgo eléctrico, espacio confinado, circulación vehicular—. Respecto de los técnicos contratistas, el artículo 30 de la Ley 20.744 impone al principal el deber de exigir el cumplimiento de las obligaciones laborales y de seguridad social y establece responsabilidad solidaria por su omisión. La matriz de competencias del paquete 4.4, al bloquear la asignación de una orden a un técnico con certificación o habilitación vencida, opera simultáneamente como tratamiento de **R04** y como registro documentado del ejercicio de ese deber de control.

**Geolocalización de los técnicos.** La ubicación del trabajador es dato personal en los términos del artículo 2 de la Ley 25.326, y su tratamiento debe conciliar la facultad de organización y dirección del empleador (artículos 64 y 65 de la Ley 20.744) con la exigencia de que los sistemas de control se practiquen con discreción y salvaguarden la dignidad del trabajador (artículo 70). El régimen que se adopta es: finalidad declarada y limitada a la asignación y verificación de órdenes; captura restringida a la jornada laboral, con desactivación fuera de ella; consentimiento informado con notificación previa e individualizada; minimización —se registra la ubicación en los hitos de la orden, no un rastreo continuo—; plazo de conservación acotado; prohibición de uso disciplinario no declarado; y comunicación previa a la representación gremial. Este punto debe cerrarse antes del piloto, no después.

<!-- cols: 16,32,52 -->

| Norma | Exigencia concreta | Cómo la satisface el proyecto |
|---|---|---|
| Ley 25.326, arts. 9, 10 y 25 | Deber de seguridad y confidencialidad; contrato con el encargado del tratamiento; datos no aplicables a otra finalidad y destruidos al concluir | Cláusulas del punto 8 con cifrado, derecho de auditoría y reversibilidad; SSO, doble factor, mínimo privilegio y baja automática (paquetes 5.5 y 5.6, tratamiento de R05) |
| Ley 25.326, art. 12 | Restricción a la transferencia internacional de datos | Región de alojamiento habilitada como requisito eliminatorio del RFP y cláusulas contractuales tipo aprobadas por la autoridad |
| Medidas de seguridad de la autoridad de aplicación | Notificación de incidentes de seguridad | Obligación contractual de notificar la brecha con plazo cierto y procedimiento de escalamiento al NOC y a Seguridad |
| Ley 27.078 y régimen de calidad del ENACOM | Parámetros de tiempo de respuesta y disponibilidad; régimen de información | SLA parametrizados en el paquete 4.2 y medidos en O4; traza de la orden como respaldo probatorio |
| Ley 24.240, arts. 4 y 8 bis | Información cierta, clara y detallada; trato digno; opción expresa por el soporte electrónico | Notificaciones de estado y ventana horaria; registro de la opción del cliente y entrega de copia de la conformidad |
| Ley 25.506, arts. 5, 7 y 8 | Distinción entre firma digital y electrónica y su valor probatorio | Conformidad asumida como firma electrónica, reforzada con geolocalización, marca temporal, fotografías, mediciones y auditoría inalterable |
| Leyes 19.587 y 24.557 | Condiciones de higiene y seguridad y cobertura de riesgos del trabajo | Medidas por sector del punto 6; registro en la aplicación del uso de elementos de protección personal por tipo de tarea |
| Ley 20.744, art. 30 | Deber de control sobre contratistas y responsabilidad solidaria | Matriz de competencias y habilitaciones vigentes que bloquea la asignación (paquete 4.4, tratamiento de R04) |
| Ley 20.744, arts. 65 y 70, y Ley 25.326 | Proporcionalidad de los medios de control y protección del dato personal del trabajador | Geolocalización limitada a la jornada y a hitos de la orden, con consentimiento informado, plazo de conservación acotado y comunicación gremial previa |

### Conclusión del análisis de factibilidad

**Técnica.** El proyecto es técnicamente factible, con una condición que no admite postergación: la existencia y la capacidad de las interfaces del SGOT, del CRM y del NMS deben confirmarse en el paquete 2.3, antes de emitir el RFP. Es el riesgo de mayor severidad del análisis (RT1, severidad 20) y el único capaz de alterar el alcance, el costo y la duración a la vez. Declararlo abierto, con tres planes alternativos cotizables, es preferible a suponerlo resuelto. El resto de los riesgos técnicos tiene severidad igual o menor a 12 y respuesta definida dentro de la propia planificación.

**Económica.** El proyecto es económicamente viable en el escenario base —valor actual neto de +USD 31.515 a cinco años, tasa interna de retorno del 19,0% frente a una tasa de corte del 15% y repago a los 3,14 años—, pero el margen es estrecho y el resultado descansa sobre líneas base que hoy son supuestos y no mediciones. El umbral de indiferencia se ubica en el 85% de realización de los beneficios estimados, y un escenario de realización sostenida del 60% arroja valor actual neto marcadamente negativo. A tres años el proyecto todavía no se repaga: necesita el cuarto y el quinto año de operación. La conclusión honesta es de **factibilidad económica condicionada**: el proyecto se justifica, pero la decisión de despliegue masivo debe adoptarse recién en el paquete 8.4, con las líneas base ya medidas en el paquete 2.4 y los precios ya cerrados en el contrato del paquete 3.5.

**Legal.** Es la dimensión de mayor peso y también la más exigente. No hay impedimento legal para ejecutar el proyecto, pero sí un conjunto de obligaciones que deben quedar satisfechas por vía contractual y de configuración antes de que la plataforma reciba el primer dato real: región de alojamiento y cláusulas de transferencia internacional cerradas antes de la firma del contrato; baja automática de credenciales operativa antes del piloto, por su vínculo directo con R05; régimen de geolocalización notificado y consentido antes de que el primer técnico use la aplicación; y asunción expresa de que la conformidad del cliente es firma electrónica y no digital.

**Veredicto global.** El proyecto se declara **factible con condiciones**. Las tres condiciones habilitantes, en orden cronológico, son: confirmar las interfaces de integración en el paquete 2.3; cerrar las cláusulas de protección de datos y transferencia internacional en el paquete 3.5; y validar las líneas base medidas en el paquete 2.4 antes de la decisión de avance del paquete 8.4. Ninguna de las tres agrega actividades a la planificación: las tres ya están en la EDT, y este análisis fija el momento en que cada una deja de ser un supuesto para convertirse en un hecho verificado.

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

<!-- cols: 25,75 -->

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

<!-- cols: 5,18,24,23,14,16 -->

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
