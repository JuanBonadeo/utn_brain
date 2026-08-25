# Etapa 3 — Documento de validación del punto 3

> **Fuente de verdad de este entregable.** El `.docx` y el `.pdf` se generan
> desde acá con `npm run docx -- materias/ASI/etapa3-validacion-punto3.md materias/ASI/etapa3-validacion-punto3.docx`
> y después `scripts/preview-docx.sh`. No editar los generados a mano.
>
> **Para qué es.** La consigna, punto 3, dice *"Identificar alternativas para el
> desarrollo del Proyecto. Seleccionar una y justificar. (Validar con el
> docente)"*. Este documento es lo que se le manda al docente para esa
> validación: contiene los puntos 1, 2 y 3, y nada más. El Acta (punto 4.b) y la
> EDT quedan retenidas hasta que la alternativa esté validada.
>
> Contenido tomado de la wiki: Unidad 5 y sección TP Integrador → Etapa 3.

---

## ETAPA 3 — VALIDACIÓN DEL PUNTO 3

**Proyecto de TI para Personal (Telecom Argentina) — Proceso de instalación de internet con fibra óptica**

<!-- cols: 24,76 -->

| | |
|---|---|
| Cátedra | Administración de Sistemas de Información — 4º Año Ingeniería en Sistemas de Información |
| Comisión | 403 |
| Grupo | 310 |
| Integrantes | 53535 Bonadeo, Juan Cruz · 52674 Casermeiro, Gonzalo · 53543 De la Rosa, Valentín Yael · 53215 Lezcano, Diego · 52688 Lurati, Ignacio |

---

### 1. PROYECTO PROPUESTO

#### Problema o necesidad detectada

El proceso de instalación de internet con fibra óptica, relevado y modelado en la Etapa 1, presenta tres debilidades documentadas en las etapas anteriores y que hoy no tienen tratamiento:

1. **Falta de trazabilidad de la orden de trabajo.** El estado real de la instalación no está disponible en tiempo real para las áreas que lo necesitan, lo que genera reclamos duplicados y consultas manuales entre Operaciones, NOC y Comercial.
2. **Ausencia de criterio de priorización en la cola de órdenes de trabajo.** Identificado en la Etapa 2 como riesgo **R07**, severidad 12, **sin plan de tratamiento**.
3. **Falta de control de competencias técnicas al asignar una orden.** Identificado en la Etapa 2 como riesgo **R04** —técnico sin capacitación en el nuevo modelo de ONT—, severidad 12, **también sin plan de tratamiento**.

#### Proyecto

Implementar una **plataforma de gestión de órdenes de trabajo con aplicación móvil de campo (OT-Campo)** que resuelva la falta de trazabilidad, priorización y control de competencias técnicas en el proceso de instalación de fibra óptica.

El proyecto es el tratamiento de R04 y R07, y aporta además a la mitigación de R06 (elimina aguas arriba la causa de los reclamos duplicados) y de R05, dado que la aplicación de campo es el control ya comprometido en la Etapa 2 para que los técnicos contratistas operen sin acceso a los sistemas de backend.

#### Trazabilidad con las etapas anteriores

<!-- cols: 22,48,30 -->

| Origen | Texto ya comprometido | Cómo lo ataca |
|---|---|---|
| Objetivo de TI (Etapa 1) | Implementar una aplicación de gestión para técnicos de campo y aumentar la productividad operativa en un 5% | Es el alcance del proyecto |
| Meta de TI (Etapa 1) | Asignación optimizada de técnicos | Motor de asignación por competencia, zona, carga y ventana horaria |
| Objetivo de negocio (Etapa 1) | Aumentar el rendimiento de los técnicos en un 5% (instalaciones sobre horas de trabajo) | Objetivo O1, con el mismo indicador |
| Meta de negocio (Etapa 1) | Mejorar el tiempo de instalación | Objetivo O2 |

#### Proceso afectado y usuarios

Afecta las **actividades 3 a 9** del proceso modelado en la Etapa 1. Las actividades 1 y 2 —recepción de la solicitud y verificación de cobertura— quedan fuera y siguen gestionándose en el CRM.

Usuarios: técnico instalador de campo (propio y contratista), supervisor de instalaciones, NOC, área comercial (consulta), logística y almacén, y Gerencia de Operaciones. El cliente final no es usuario: recibe notificaciones y firma la conformidad.

#### Alcance — qué incluye

Módulo de despacho y priorización con cola única · motor de asignación por competencia certificada, zona, carga y ventana horaria · aplicación móvil *offline-first* con checklist por modelo de ONT, mediciones ópticas, evidencia fotográfica, geolocalización y conformidad digital del cliente · integraciones con SGOT, CRM, base de datos y NMS · seguridad con inicio de sesión único, doble factor y baja automática de credenciales · tablero de indicadores.

#### Alcance — qué NO incluye

- El rediseño del flujo de escalamiento del CRM (R06), que ya tiene plan de tratamiento propio.
- El reemplazo o la migración del CRM, del SGOT o de la base de datos.
- Obra civil, tendido troncal, ampliación de nodos (R11) y mantenimiento preventivo del cable (R08).
- El reemplazo del firewall (R03), la redundancia del balanceador (R09) y la correlación de eventos del NMS (R10).
- Venta, facturación y recupero de clientes.
- Otros procesos de campo: reparaciones, mudanzas y desinstalaciones.
- La adquisición de vehículos y fusionadoras.

---

### 2. OBJETIVOS

<!-- cols: 5,22,27,16,13,17 -->

| # | Objetivo | Indicador | Línea base | Meta | Plazo |
|---|---|---|---|---|---|
| O1 | Aumentar la productividad del técnico de campo | Instalaciones finalizadas conformes ÷ horas-técnico disponibles | 0,50 inst./hora-técnico *(supuesto)* | 0,525 (+5%) | 6 meses desde la puesta en producción |
| O2 | Reducir la latencia de registro del cierre de la orden | % de órdenes cerradas dentro de los 15 minutos de terminada la visita, y tiempo medio entre asignación y cierre | 20% · 26 h *(supuesto)* | ≥90% · ≤8 h | Mes 4, sostenido 3 meses |
| O3 | Reducir las visitas fallidas por causa evitable | Órdenes reprogramadas por "técnico sin competencia" o "kit incompleto" ÷ órdenes despachadas | 12% *(supuesto)* | ≤6% | 6 meses desde la puesta en producción |
| O4 | Asegurar el cumplimiento de la priorización de la cola | % de órdenes despachadas según el orden del motor, y % de cumplimiento del SLA de primera respuesta | No medible en la situación actual — esa imposibilidad **es** la definición de R07 | ≥95% · ≥90% | Mes 3 desde la puesta en producción |

> **Sobre las líneas base.** Los valores marcados como *supuesto* son estimaciones: las Etapas 1 y 2 no relevaron indicadores de operación. La propuesta es declararlos explícitamente como supuestos y **poner su medición formal como entregable propio de la fase de Relevamiento y análisis**, recalibrando las metas sobre los valores reales. Es la consulta 2 del final.

---

### 3. ALTERNATIVAS Y SELECCIÓN

Las tres alternativas resuelven el mismo problema y construyen el mismo alcance; cambia el modo de construcción.

<!-- cols: 26,74 -->

| Alternativa | Descripción |
|---|---|
| **A1 — Desarrollo interno** | El área de sistemas de Personal diseña y desarrolla la plataforma, adquiriendo de mercado solo componentes acotados: servicio de mapas y geolocalización, MDM, dispositivos rugerizados e infraestructura |
| **A2 — SaaS FSM configurable** | Se contrata una plataforma de *Field Service Management* de mercado y se configura |
| **A3 — Desarrollo tercerizado** | Una consultora la desarrolla a medida, con hosting en infraestructura de Personal |

#### Justificación de los pesos

Los pesos reflejan el análisis de riesgos que el propio grupo hizo en la Etapa 2. Allí se identificaron **R03** (firewall sin reglas segmentadas) y **R05** (credenciales de contratistas sin baja) **ambos en severidad 15**, los dos más altos del trabajo: para este proceso, el control de accesos y el perímetro dominan. Además, cinco de los seis componentes de la solución dependen de integrarse con SGOT, CRM, base de datos y NMS, de modo que la integración no es un criterio más sino el núcleo técnico. Y por tratarse de un proceso operativo central, la dependencia de un proveedor externo compromete la continuidad del negocio.

#### Matriz de selección

<!-- cols: 41,10,16,16,17 -->

| Criterio | Peso | A1 Interno | A2 SaaS | A3 Tercerizado |
|---|---|---|---|---|
| Seguridad y cumplimiento (Ley 25.326, R03, R05) | 20% | 5 | 3 | 4 |
| Integración con SGOT / CRM / BD / NMS | 20% | 5 | 3 | 4 |
| Dependencia del proveedor | 15% | 5 | 2 | 3 |
| Costo total de propiedad a 3 años | 10% | 2 | 4 | 3 |
| Tiempo hasta la puesta en producción | 10% | 2 | 5 | 4 |
| Mantenimiento y evolución | 10% | 4 | 5 | 3 |
| Escalabilidad | 10% | 3 | 5 | 3 |
| Conocimiento disponible en el equipo | 5% | 3 | 4 | 3 |
| **Ponderado** | **100%** | **4,00** | **3,60** | **3,50** |

#### Alternativa seleccionada

Se selecciona el **desarrollo interno (A1)** porque obtiene el mayor resultado ponderado (4,00) bajo criterios que priorizan la seguridad, la integración con los sistemas existentes y la independencia de proveedores, coherentes con los riesgos R03 y R05 identificados en la Etapa 2 en severidad 15. Los datos personales de clientes no salen del perímetro de la organización y la integración con SGOT, CRM y NMS se resuelve sin intermediarios. **Como contrapartida, es la alternativa de mayor plazo hasta la puesta en producción y de mayor inversión inicial**, lo que se compensa por la ausencia de licenciamiento recurrente por usuario a partir del segundo año.

Si la objeción fuera el plazo, la alternativa de repliegue es **A3, desarrollo tercerizado con hosting propio** (3,50), que mantiene los datos dentro del perímetro y acorta el tiempo hasta la puesta en producción.

---

### CONSULTAS

1. **¿Se valida la alternativa seleccionada?** En particular, ¿es aceptable que los pesos de la matriz se justifiquen con el análisis de riesgos de la Etapa 2, como se explica en el punto 3?
2. **Líneas base.** No están medidas porque las etapas anteriores no relevaron indicadores de operación. ¿Es correcto declararlas como supuestos y poner su medición como entregable de la fase de Relevamiento y análisis dentro de la EDT?
3. **Cronograma.** ¿Se acepta un Gantt en meses relativos (Mes 1, Mes 2…) contados desde la aprobación del Acta de Proyecto, o se requieren fechas de calendario?
4. **Fecha de entrega** de la Etapa 3.
