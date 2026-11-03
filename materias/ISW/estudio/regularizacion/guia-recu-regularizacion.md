# ISW — Guía para el recuperatorio de Regularización

**Ingeniería y Calidad de Software · UTN · 4.º año**

**Recuperatorio: sábado 24/10/2026 · Entran U1, U2, U3 y U5 · Marco: CMMI 1.2**

Guía teórica revisada contra la wiki y el banco de parciales, el parcial del 26/09/2026 resuelto, y un cuestionario de práctica con las respuestas al final.

## 1. Cómo es el examen

- **Formato:** Google Forms impreso, en papel y sin dispositivos. El parcial del 26/09/2026 tuvo **8 consignas y 9 puntos** (una valía 2) y se aprobaba con **5,40 (60 %)**. En 2025 fueron 12 puntos y se aprobaba con 8. La respuesta incorrecta vale 0.
- **Tipos de pregunta:**
  - **Selección única** con "Ninguna de las opciones". Es una opción real: en los parciales de regularización a veces fue la correcta. No la descartes de entrada.
  - **Selección múltiple:** si marcás una de más, perdés el punto.
  - **Grillas** (activo / producto de trabajo / ambos; Sí / No): se reciclan las mismas filas entre años.
  - **Caso corto:** "¿qué área o técnica corresponde?". Es el formato dominante: hay que clasificar una situación, no recitar teoría.
  - **Cálculo** (particiones, valores límite, duración con recursos, escenarios de CU): un solo error tira el punto entero.
- **CMMI es el eje transversal.** Saber ubicar rápido "esta situación → esta área → esta práctica" vale más que memorizar definiciones sueltas.
- **El parcial 2026 cargó sobre U5:** 5 de los 9 puntos, y 3 de esos fueron de particiones. U2 no tuvo ninguna pregunta, pero entra y fue de lo más preguntado otros años.

## 2. U1 — Modelos de calidad de software

### Calidad y tipos de calidad

**Calidad:** totalidad de características de un producto o proceso que satisfacen las expectativas del cliente, explícitas e implícitas. Es medible y a la vez subjetiva.

| Tipo (Rozas) | Qué es | Ejemplo |
|---|---|---|
| **Externa** | La que percibe el cliente directamente, mirando el producto desde afuera | Cumplimiento de los requerimientos |
| **Interna** | Se define dentro de la empresa: cómo está hecho el software por dentro (código, arquitectura, documentación). El cliente no la percibe | Mantenibilidad, claridad del código, respeto de estándares |
| **En uso** | Solo se ve cuando el producto ya está en su ambiente real de trabajo. Es la más difícil de anticipar, porque depende de cómo lo usa el usuario en su contexto | El sistema anda, pero a la media hora de uso real aparece el problema |

**Atributos de calidad.** Se preguntan como "facilidad de…" y hay que nombrar el atributo: **mantenibilidad** = facilidad para corregir, adaptar y mejorar el software; **usabilidad** = facilidad de uso.

**Modelo FURPS+.** Hay una sola pregunta confirmada: *la adaptabilidad se clasifica como Soporte (S)*. El resto de la tabla es conocimiento general del modelo: confirmalo antes de memorizarlo a fondo. *(conocimiento general)*

| Letra | Significa | Incluye |
|---|---|---|
| **F** | Funcionalidad | Prestaciones, capacidades del sistema, seguridad |
| **U** | Usabilidad | Facilidad de uso, estética, consistencia de la interfaz, documentación y ayuda |
| **R** | Fiabilidad | Frecuencia y severidad de fallas, exactitud de resultados, tiempo entre fallas, recuperación |
| **P** | Rendimiento | Tiempos de respuesta, throughput, uso de memoria y CPU |
| **S** | Soporte | Adaptabilidad, mantenibilidad, configurabilidad, instalación, testeabilidad, compatibilidad |
| **+** | Restricciones | De diseño, de implementación, de interfaz y físicas. No son atributos de calidad: son restricciones del proyecto |

**Aseguramiento vs. control de calidad.** En software no alcanza con controlar al final, porque ya es tarde: el aseguramiento de la calidad tiene que estar metido durante todo el proceso de desarrollo.

### CMMI 1.2: madurez y capacidad

Modelo de mejores prácticas para mejorar procesos. Tiene dos representaciones:

- **Madurez (por etapas):** para estar en un nivel hay que cumplir **todas** las áreas de proceso de ese nivel **y de los inferiores**. CMMI-DEV 1.2 tiene 22 áreas de proceso.
- **Capacidad (continua):** mide el nivel de **una sola** área de proceso, independiente del resto.

| Nivel | Nombre | Idea clave |
|---|---|---|
| 1 | Inicial | No hay proceso: depende de "héroes" individuales. Impredecible |
| 2 | Gestionado | Gestión a nivel **proyecto**: planificación, seguimiento, recursos definidos. Se institucionalizan prácticas básicas. Reactivo |
| 3 | Definido | Procesos **estándar de la organización**, adaptados a cada proyecto (adaptación permitida, no ciega). Proactivo |
| 4 | Gestionado cuantitativamente | Métricas y control estadístico: **predictibilidad cuantitativa** (pregunta del parcial 2026). Se actúa ante variaciones de causa especial |
| 5 | En optimización | **Mejora continua:** se trabaja sobre las causas comunes para reducir la variación general |

**Ojo:** los niveles son acumulativos y de todo o nada. "La empresa cumple nivel 3 salvo un área de nivel 2" → está en **nivel 1**, no en el 2. Alcanzar un nivel superior tampoco exime de las áreas inferiores: si una empresa nivel 3 deja de hacer estimaciones (PP, nivel 2), cae a nivel 1.

### Áreas de proceso por nivel

Las 22 áreas de CMMI-DEV 1.2. Las marcadas con ✔ entran en el parcial; de las demás solo hay que saber el nivel.

| Nivel | Sigla | Área de proceso | Entra |
|---|---|---|---|
| 2 | REQM | Gestión de requisitos | |
| 2 | PP | Planificación de proyecto | ✔ U3 |
| 2 | PMC | Monitorización y control de proyecto | ✔ U3 |
| 2 | SAM | Gestión de acuerdos con proveedores | |
| 2 | MA | Medición y análisis | |
| 2 | PPQA | Aseguramiento de calidad de proceso y producto | |
| 2 | CM | Gestión de configuración | |
| 3 | RD | Desarrollo de requisitos | |
| 3 | TS | Solución técnica | |
| 3 | PI | Integración del producto | |
| 3 | VER | Verificación | ✔ U5 |
| 3 | VAL | Validación | ✔ U5 |
| 3 | OPF | Enfoque en procesos de la organización | ✔ U2 |
| 3 | OPD | Definición de procesos de la organización | ✔ U2 |
| 3 | OT | Formación organizativa | ✔ U2 |
| 3 | IPM | Gestión integrada de proyecto | |
| 3 | RSKM | Gestión de riesgos | |
| 3 | DAR | Análisis y resolución de decisiones | |
| 4 | OPP | Rendimiento de procesos de la organización | |
| 4 | QPM | Gestión cuantitativa de proyecto | |
| 5 | OID | Innovación y despliegue organizativo | |
| 5 | CAR | Análisis causal y resolución | |

### A qué nivel pertenece una meta

Si te dan el nombre de una meta suelta (por ejemplo, "Establecer estimaciones") y te preguntan su nivel, buscá a qué área pertenece: el área ya tiene su nivel fijo.

| Nivel | Área | Metas específicas (SG) |
|---|---|---|
| 2 | PP | SG1 Establecer estimaciones · SG2 Desarrollar un plan de proyecto · SG3 Obtener el compromiso con el plan |
| 2 | PMC | SG1 Monitorizar el proyecto frente al plan · SG2 Gestionar las acciones correctivas hasta su cierre |
| 3 | OPD | SG1 Establecer los activos de proceso de la organización |
| 3 | OPF | SG1 Determinar las oportunidades de mejora de procesos · SG2 Planificar e implementar las mejoras de procesos · SG3 Desplegar los activos de proceso e incorporar las lecciones aprendidas |
| 3 | OT | SG1 Establecer una capacidad de formación organizativa · SG2 Proporcionar la formación necesaria |
| 3 | VER | SG1 Preparar la verificación · SG2 Realizar revisiones entre pares · SG3 Verificar los productos de trabajo seleccionados |
| 3 | VAL | SG1 Preparar la validación · SG2 Validar el producto o los componentes de producto |

Ejemplo: "Establecer estimaciones" es la SG1 de PP, y PP es de nivel 2 → **nivel 2**.

**Regla rápida** si no te acordás del área:

- Estimar, planificar, plan de proyecto, compromiso, monitorizar, acciones correctivas → **nivel 2** (PP o PMC).
- Activos de proceso, biblioteca, repositorio de mediciones, mejora de procesos, formación, verificar, validar, revisión entre pares → **nivel 3** (OPD, OPF, OT, VER o VAL).

### Componentes de un área de proceso

| Tipo | Qué incluye | Obligatorio |
|---|---|---|
| **Requeridos** | Metas específicas y metas genéricas | Sí: es lo único obligatorio |
| **Esperados** | Prácticas específicas y prácticas genéricas | No: se pueden alcanzar las metas con prácticas alternativas |
| **Informativos** | Subprácticas, productos típicos de trabajo, declaración de propósito, notas introductorias, áreas relacionadas, elaboraciones de prácticas genéricas, ejemplos, referencias | No |

**Ojo:** el parcial 2026 pidió los **informativos**: subprácticas, declaraciones de propósito y productos típicos de trabajo. Las prácticas genéricas son esperadas y los "objetivos genéricos" (metas genéricas) son requeridos. Otros años se pidieron los **requeridos** (salió 4 veces): solo las metas.

**Trampa recurrente:** "¿Las prácticas específicas son obligatorias?" → **No.** Lo obligatorio son las metas.

**Institucionalización.** Que un proceso quede incorporado de verdad a la organización, y no dependa de una persona, se logra con las **metas y prácticas genéricas**, no con las específicas:

- Las **específicas** son el contenido técnico propio de cada área (VER tiene las suyas, PP las suyas). Dicen si esa vez se hizo el trabajo.
- Las **genéricas** son la misma plantilla en todas las áreas: política, recursos asignados, gente capacitada, seguimiento, revisión por la gerencia. Dicen si el proceso se sostiene en el tiempo.

### Principios de la Ingeniería del Software

Se preguntan como selección múltiple con distractores.

- ✅ **Verdaderos:** "Haz de la calidad la razón de trabajar" · "Probar, probar y probar".
- ❌ **Falsos** (suenan razonables pero no son principios): que las personas y el tiempo son intercambiables (agregar gente a un proyecto atrasado no lo acelera) · que todos los proyectos deben seguir el mismo ciclo de vida · que hay que entregar o probar solo al final · "primero rápido, después correcto".

## 3. U2 — Gestión de procesos

### Proceso y SPEM

**Proceso (Rozas):** conjunto de tareas que producen un producto o servicio, y es **repetible**. El **proyecto**, en cambio, es único, tiene incertidumbre y restricciones.

**SPEM:** como un UML, pero para modelar procesos. El **contenido de métodos** define los bloques estáticos (roles, tareas, artefactos); el **proceso** los organiza en una secuencia temporal. Está orientado específicamente a procesos de desarrollo de software y sistemas, y sirve con distintos estilos, culturas y ciclos de vida.

**Representación de un proceso según SPEM:**

| Pregunta | Elemento | Representa |
|---|---|---|
| ¿Quién? | **Rol** | Quién hace el trabajo |
| ¿Qué? | **Producto de trabajo** | Las entradas que se usan y las salidas que se producen |
| ¿Cómo? | **Tarea** | El esfuerzo a realizar |

**Elementos de SPEM**, de más grande a más chico:

- **Delivery Process** (proceso de entrega): un proceso completo, tal como se necesita para cierto tipo de proyecto.
- **Capability Pattern** (patrón de capacidad): un fragmento de proceso reutilizable, que se puede usar más de una vez dentro de un Delivery Process.
- **Activity** (actividad): elemento básico para definir procesos; agrupa productos de trabajo y tareas.
- **Task** (tarea): la porción más chica de trabajo en un modelo de proceso.

### RUP, basado en SPEM

RUP construye sus elementos de proceso sobre SPEM. Granularidad de más grande a más chico: **Disciplina → Actividad → Tarea**. Ejemplo: disciplina Entorno → actividad "Preparar el entorno del proyecto" → tarea "Personalizar el proceso de desarrollo para el proyecto".

| Elemento | Qué es |
|---|---|
| **Fase** | Período entre dos hitos importantes. Son 4: Concepción, Elaboración, Construcción y Transición |
| **Disciplina** | Agrupa tareas por similitud de preocupaciones y cooperación. Ej.: Modelado de negocio, Requisitos, Análisis y diseño, Implementación, Prueba, Despliegue, Configuración y gestión de cambios, Gestión de proyectos, Entorno. Tiene una o más actividades |
| **Actividad** | Agrupación lógica de tareas, roles y productos de trabajo. Admite anidación. Tiene una o más tareas |
| **Tarea** | Unidad de trabajo que hace un rol específico; dura de horas a días y suele afectar a uno o pocos productos de trabajo |
| **Rol** | Conjunto de habilidades, competencias y responsabilidades. Ej.: Analista de sistemas, Arquitecto de software, Diseñador, Revisor técnico |
| **Producto de trabajo** | Resultado significativo de un proceso. Tres tipos: **artefacto** (tangible, p. ej. un documento de diseño), **resultado** (intangible, un estado logrado) y **entregable** (empaquetado de otros productos para entregar a una parte interna o externa) |
| **Guías** | Todo lo que explica cómo hacer algo: plantilla, directriz, lista de comprobación, ejemplo, concepto, guía de herramientas, documentación, informe |

**Ojo:** el temario incluye la PPT de Proceso y RUP solo hasta la pág. 46. Los **objetivos de las fases** y los **propósitos de las disciplinas** (págs. 52 a 74) no entran.

**Equivalencia RUP ↔ SPEM:** disciplina y actividad de RUP ≈ capability pattern y activity de SPEM (fragmentos reutilizables) · tarea de RUP ≈ task de SPEM · el proceso completo de un proyecto RUP ≈ un delivery process.

**Las 3 dimensiones críticas (SEI)** en las que se apoya la mejora de procesos: **personas · métodos y procedimientos · herramientas y equipamiento.** El SEI (Software Engineering Institute, de Carnegie Mellon) creó CMM y CMMI.

### OPF, OPD y OT

Son las áreas de gestión de procesos de nivel 3 y lo más preguntado de la unidad.

| Área | Propósito | Frase gatillo en el examen |
|---|---|---|
| **OPF** — Enfoque en procesos de la organización | Planificar, implementar y desplegar mejoras de procesos, a partir de comprender sus fortalezas y debilidades | "Evaluar cómo trabaja la factory", "comparar contra otras organizaciones (benchmarking)", "analizar tendencias de lecciones aprendidas", planes de acción de procesos |
| **OPD** — Definición de procesos de la organización | Crear y mantener el conjunto de activos de proceso que usan todos los proyectos (la biblioteca de activos) | "Repositorio de medición de la organización", "criterios y guías de adaptación", "modelos de ciclo de vida" |
| **OT** — Formación organizativa | Desarrollar las habilidades del personal para que cumpla sus roles con eficacia y eficiencia | Cualquier mención a capacitación (obligatoria u optativa, presencial o virtual) |

**Regla mental:** **OPD define y guarda** (biblioteca de activos, repositorio de mediciones) · **OPF evalúa y mejora** · **OT capacita.**

Lo que diga **IPPD** no entra: era un enfoque absorbido en versiones nuevas de CMMI.

### Activo de proceso vs. producto de trabajo

Es una grilla de 4 o 5 ítems, un punto cada uno. Salió en 2022, 2024 y 2025. Las opciones son **activo / producto de trabajo / ambos**.

- **Activo:** algo que la organización tiene **para usar en sus proyectos**. Señales: plantilla, guía, directriz, modelo, estándar. También la documentación de las **herramientas que la organización adquiere**.
- **Producto de trabajo:** el resultado concreto de una tarea **de un proyecto**. Señales: "del cliente", "del sistema desarrollado", un artefacto puntual (regla de negocio, minuta, código).

| Ítem | Respuesta confirmada |
|---|---|
| Plantilla de casos de uso | Activo |
| Plantilla de manual de instalación | Activo |
| Plantilla para la presentación de la reunión de lanzamiento | Activo |
| Guía para confeccionar el manual de usuario | Activo |
| Directrices para conformar el equipo del proyecto | Activo |
| Manual de usuario del compilador Java | Activo (es documentación de una herramienta) |
| Descripción del proceso de negocio del cliente | Producto de trabajo |
| Manual de instalación del sistema desarrollado para el cliente | Producto de trabajo |
| Manual de usuario del sistema desarrollado para el cliente | Producto de trabajo |
| Regla de negocio | Producto de trabajo |

**Ojo:** en los 10 ítems confirmados, **"Ambos" nunca fue la respuesta correcta**. El par que confunde: la plantilla del manual es un activo (el molde es de la organización); el manual del sistema del cliente es un producto de trabajo (lo moldeado es del proyecto).

### Metas y prácticas de OPD, OPF y OT

**OPD — SG 1 Establecer los activos de proceso de la organización**

- SP 1.1 Establecer los procesos estándar
- SP 1.2 Establecer las descripciones de los modelos de ciclo de vida (cascada, espiral, evolutivo, incremental, iterativo)
- SP 1.3 Establecer los criterios y las guías de adaptación
- SP 1.4 Establecer el repositorio de medición de la organización
- SP 1.5 Establecer la biblioteca de activos de proceso de la organización
- SP 1.6 Establecer los estándares del entorno de trabajo

(La SG 2 "Facilitar la gestión IPPD" no entra.)

**OPF — SG 1 Determinar las oportunidades de mejora de procesos**

- SP 1.1 Establecer las necesidades de procesos de la organización
- SP 1.2 Evaluar los procesos de la organización
- SP 1.3 Identificar las mejoras de procesos de la organización

**OPF — SG 2 Planificar e implementar las mejoras de procesos**

- SP 2.1 Establecer planes de acción de procesos
- SP 2.2 Implementar los planes de acción de procesos

**OPF — SG 3 Desplegar los activos de proceso e incorporar las lecciones aprendidas**

- SP 3.1 Desplegar los activos de proceso de la organización
- SP 3.2 Desplegar los procesos estándar
- SP 3.3 Monitorizar la implementación
- SP 3.4 Incorporar las experiencias relativas al proceso en los activos de proceso de la organización

**Trampa clásica:** la SP 3.4 de OPF menciona "activos de proceso" y se confunde con OPD. Pero OPD **define y crea** los activos; OPF es quien los **actualiza** con las lecciones aprendidas.

**OT — SG 1 Establecer una capacidad de formación organizativa**

- SP 1.1 Establecer las necesidades de formación estratégicas
- SP 1.2 Determinar qué necesidades de formación son responsabilidad de la organización
- SP 1.3 Establecer un plan táctico de formación organizativa
- SP 1.4 Establecer la capacidad de formación

**OT — SG 2 Proporcionar la formación necesaria**

- SP 2.1 Impartir la formación
- SP 2.2 Establecer los registros de formación
- SP 2.3 Evaluar la eficacia de la formación

### Ciclos de vida

Se elige según dos factores: qué tan **estables** son los requerimientos, y si hace falta poner en producción **partes** del producto antes de terminarlo.

| Situación | Ciclo de vida recomendado |
|---|---|
| Requerimientos conocidos y estables | Cascada (también incremental, si además hay que entregar por partes) |
| Requerimientos inestables | Iterativo (cascada es el que peor se adapta) |
| Hacen falta entregas tempranas | Incremental (permite más de un release; cascada entrega una sola vez, al final) |

Los modelos de ciclo de vida que menciona CMMI (OPD SP 1.2): cascada, espiral, evolutivo, incremental, iterativo.

En un ciclo **incremental**, cada incremento pasa por sus propias pruebas: no se acumula todo el testing para el final.

**Variantes de cascada** (cómo se organizan las tareas de la EDT):

- **Tradicional:** por fases. Primero todo el análisis, después todo el diseño, después toda la codificación.
- **Por módulos:** primero por componentes del sistema; dentro de cada módulo se aplican las fases.

**"El diseño siempre precede a la codificación": por qué a veces es Falso.** Dentro de un mismo módulo, sí: la codificación necesita el diseño de ese módulo (axioma 1, ver U3). Como afirmación global del proyecto es falsa apenas hay más de un módulo en paralelo: la codificación del módulo A puede correr al mismo tiempo, o antes, que el diseño del módulo B.

## 4. U3 — Gestión de proyectos

### Proyecto y mantenimiento

**Proyecto:** producto o servicio único, con restricciones de tiempo y costo. Sus parámetros son **duración, esfuerzo y costo**. Apunta a un único producto final, aunque internamente se divida en módulos o incrementos; eso lo distingue del proceso, que es repetible.

**Ojo:** el **mantenimiento no es parte del proyecto de desarrollo**: son proyectos aparte. Se estima que se gasta ~20 % del tiempo en desarrollar y ~80 % en mantener.

| Tipo de mantenimiento | Objetivo |
|---|---|
| **Correctivo** | Corregir errores detectados con el software en uso |
| **Adaptativo** | Adaptarlo a cambios del **entorno** (hardware, sistema operativo, gestor de BD, comunicaciones) sin tocar la funcionalidad |
| **Perfectivo** | Mejorar la **calidad interna** (rendimiento, mantenibilidad) sin agregar funcionalidad. Ej.: optimizar código y base de datos |
| **Evolutivo** | Altas, bajas y modificaciones por **expansión o cambio de las necesidades** del usuario |

### EDT y precedencia

**EDT (estructura de desglose de trabajo):** lista de actividades que descompone el producto en partes manejables (análisis → diseño → codificación → testing; con dos módulos se puede repetir por cada uno: análisis A1, análisis A2…).

**Precedencia entre tareas.** Para armarla hay que conocer **todas las tareas** y el **ciclo de desarrollo** elegido, porque el ciclo define cómo se agrupan (por fase, por módulo, por iteración).

- **Axioma 1:** una tarea precede a otra cuando el producto de trabajo que genera es necesario para la otra.
- **Axioma 2:** una tarea predecesora garantiza una mejor ejecución de la sucesora.

### Estimación

- **Técnica de 3 puntos (distribución beta):** (optimista + 4 × normal + pesimista) / 6.
- **Método Delphi:** estimación grupal de expertos, independiente y anónima, iterativa hasta converger.
- **Puntos de función:** métrica objetiva del **tamaño funcional** del software (entradas, salidas, consultas, archivos lógicos internos y de interfaz externa, cada uno con su complejidad), sin importar la tecnología ni quién lo desarrolla. Sirve para contratos, presupuestos y comparar productividad entre equipos. Se calcula apenas están los requerimientos.
- **Puntos de historia:** estimación **relativa** del esfuerzo de un equipo específico (ágil, tipo Planning Poker). No es comparable entre equipos y necesita historial (la velocidad de sprints anteriores).
- **Distribución 40-20-40:** 40 % análisis y diseño, 20 % codificación, 40 % testing. Sirve para **repartir** un esfuerzo total que ya tenés, no para calcularlo desde cero. Si una estimación detallada no cierra así, falta estimar algo: no hay que estirar números.

### Esfuerzo vs. duración

**Duración** = tiempo de calendario (días hábiles). **Esfuerzo** = horas de trabajo. Con un solo recurso coinciden; con varios, no:

| Forma de trabajo | Esfuerzo | Duración |
|---|---|---|
| **Secuencial** (uno termina y arranca el otro) | La suma | La suma |
| **En paralelo** (se reparten la tarea) | La suma (más una penalización por integrar) | Baja |
| **De a par** (los dos sobre lo mismo) | El de dos personas (con alguna reducción por menos errores) | Igual que con una sola persona |

**Ojo:** la guía original daba porcentajes (10-15 % de penalización en paralelo, 20 % de reducción de a par) que no están ni en la wiki ni en el banco. La regla segura: **el esfuerzo es la suma y no cambia por cómo se repartan las tareas**; lo que baja con el paralelo es la duración. La excepción es cuando el orden cambia el trabajo (si un módulo ya analizado abarata el análisis de otro).

**Definiciones que se confunden:**

- **Hito:** marca de avance; no consume recursos ni tiempo (p. ej. "Entrega del módulo A").
- **Entregable:** producto de trabajo cuyo destinatario es el cliente; evidencia de avance.
- **Compromiso:** acuerdo con el cliente sobre algo que está fuera del alcance del proyecto.
- **Punto de control:** momento donde el líder contrasta lo planeado contra lo real (en el camino crítico, en momentos de riesgo o periódicamente). Se definen **en la planificación**, no en la ejecución.
- **Avance de una tarea:** se mide con tres parámetros juntos: esfuerzo consumido, esfuerzo restante y estado de los productos de trabajo. El esfuerzo consumido solo no alcanza.

### Metas y prácticas de PP

**SG 1 Establecer estimaciones**

- SP 1.1 Estimar el alcance del proyecto
- SP 1.2 Establecer las estimaciones de los atributos de los productos de trabajo y de las tareas
- SP 1.3 Definir el ciclo de vida del proyecto
- SP 1.4 Determinar las estimaciones de esfuerzo y de coste

**SG 2 Desarrollar un plan de proyecto**

- SP 2.1 Establecer el presupuesto y el calendario
- SP 2.2 Identificar los riesgos del proyecto
- SP 2.3 Planificar la gestión de los datos
- SP 2.4 Planificar los recursos del proyecto
- SP 2.5 Planificar el conocimiento y las habilidades necesarias
- SP 2.6 Planificar la involucración de las partes interesadas
- SP 2.7 Establecer el plan de proyecto

**SG 3 Obtener el compromiso con el plan**

- SP 3.1 Revisar los planes que afectan al proyecto
- SP 3.2 Reconciliar los niveles de trabajo y de recursos
- SP 3.3 Obtener el compromiso con el plan

### Metas y prácticas de PMC

**SG 1 Monitorizar el proyecto frente al plan**

- SP 1.1 Monitorizar los parámetros de planificación del proyecto
- SP 1.2 Monitorizar los compromisos
- SP 1.3 Monitorizar los riesgos del proyecto
- SP 1.4 Monitorizar la gestión de los datos
- SP 1.5 Monitorizar la involucración de las partes interesadas
- SP 1.6 Llevar a cabo revisiones del progreso
- SP 1.7 Llevar a cabo revisiones de hitos

**SG 2 Gestionar las acciones correctivas hasta su cierre**

- SP 2.1 Analizar los problemas
- SP 2.2 Llevar a cabo las acciones correctivas
- SP 2.3 Gestionar las acciones correctivas

**Ojo:** PMC solo dispara acciones correctivas cuando el desvío es **significativo**, es decir, cuando sin resolverlo el proyecto no cumple sus objetivos. "Cualquier desvío debe ser resuelto" es **Falso**: salió en 2020, 2021 y 2026.

**Trampa recurrente: PP o PMC.** Si todavía se está acordando o comprometiendo algo (antes de que haya un compromiso firme) → **PP**. Si ya hay un plan y se está siguiendo un desvío → **PMC**.

De nivel 2, en el temario solo entran PP y PMC. CM, PPQA y las demás solo hay que ubicarlas por nivel.

## 5. U5 — Verificación y validación

### VER vs. VAL

- **Verificación (VER):** ¿estoy construyendo el producto **correctamente**? Comprueba que el producto cumple su **especificación** o el estándar acordado.
- **Validación (VAL):** ¿estoy construyendo el producto **correcto**? Asegura que el producto satisface las **necesidades reales** del usuario (pilotos, aceptación, uso en su entorno real).

**Regla para clasificar:** mirá **contra qué se contrasta**, no quién lo hace ni en qué fase.

- Contra especificaciones, documentos o estándares (lo que se acordó construir) → **VER**.
- Directamente con el usuario o cliente, en su entorno real (lo que de verdad necesita) → **VAL**.

**Trampa más repetida:** si se controla contra un documento acordado, es **VER aunque el cliente haya participado en acordarlo**. Una prueba de sistema contra la especificación también es VER, aunque el producto esté terminado.

| Área | Propósito |
|---|---|
| **VER** | Asegurar que los productos de trabajo seleccionados cumplen los requisitos especificados |
| **VAL** | Demostrar que un producto o componente cumple su uso previsto cuando se coloca en su entorno previsto |

### Metas y prácticas de VER y VAL

**VER — SG 1 Preparar la verificación**

- SP 1.1 Seleccionar los productos de trabajo a verificar
- SP 1.2 Establecer el entorno de verificación
- SP 1.3 Establecer los procedimientos y los criterios de verificación

**VER — SG 2 Realizar revisiones entre pares**

- SP 2.1 Preparar las revisiones entre pares
- SP 2.2 Llevar a cabo las revisiones entre pares
- SP 2.3 Analizar los datos de las revisiones entre pares

**VER — SG 3 Verificar los productos de trabajo seleccionados**

- SP 3.1 Realizar la verificación
- SP 3.2 Analizar los resultados de la verificación

**VAL — SG 1 Preparar la validación**

- SP 1.1 Seleccionar los productos a validar
- SP 1.2 Establecer el entorno de validación
- SP 1.3 Establecer los procedimientos y los criterios de validación

**VAL — SG 2 Validar el producto o los componentes de producto**

- SP 2.1 Realizar la validación
- SP 2.2 Analizar los resultados de la validación

**Estructura:** VER tiene 3 metas (la revisión entre pares es una meta propia); VAL tiene 2. Si te dan 3 metas con revisiones entre pares, es VER.

**Entorno de validación (VAL SP 1.2)** — pregunta del parcial 2026: hay que replicar el entorno real del usuario (mismo sistema operativo, red con las mismas restricciones, los mismos periféricos, una base con datos representativos y usuarios con los mismos perfiles y permisos). Revisar el código contra estándares o hacer pruebas unitarias no es armar el entorno de validación.

### Revisiones

- **Informales:** sin proceso definido, sin roles asignados, no planificadas.
- **Formales:** objetivos definidos, roles asignados, checklist, recolección de datos e informe. La más formal es la **inspección**, dirigida por un **moderador** (no por el autor).

**Buenas prácticas:**

- ✅ Establecer una agenda y respetarla · enunciar las áreas de problemas sin intentar resolver cada uno (en la reunión se detectan defectos, no se corrigen) · revisar el producto, no al productor · limitar el número de participantes e insistir en la preparación previa · limitar el debate y las réplicas · tomar notas por escrito.
- ❌ Evitar documentar para que la reunión sea más ágil (siempre hay que documentar) · corregir los errores en el momento · guardar en el legajo de cada persona cuántos defectos se le encontraron (es revisar al productor).

**Etapas del proceso básico de revisión** (todas las revisiones las comparten; las formales agregan documentación y medición):

1. Identificar los entregables a revisar.
2. Armar la lista de participantes.
3. Los revisores estudian el documento.
4. Los revisores identifican problemas y se los comunican al autor.
5. El autor responde a los comentarios y actualiza el documento.

**Roles en una revisión formal:**

| Rol | Función |
|---|---|
| **Moderador** | Dirige el proceso. Con el autor decide el tipo de revisión y arma el equipo; valida la entrada, lidera la reunión, marca el ritmo y hace el seguimiento |
| **Autor** | Escribió el documento. Busca mejorar su calidad y su propia habilidad para escribir los próximos |
| **Documentador** | Anota cada defecto y las sugerencias de mejora del proceso (en la práctica, suele ser el autor) |
| **Revisor** (inspector) | Antes de la reunión analiza el material buscando defectos |
| **Supervisor** | Decide si se destina tiempo del proyecto a la revisión y si se cumplieron sus objetivos. Gestiona la formación de los participantes |

**Trampa:** no confundir **moderador** (controla el proceso de una revisión puntual) con **supervisor** (decide si y cuándo se hace, a nivel planificación).

### Testing: conceptos base

- **Probar** es ejecutar un programa con la intención de **encontrar errores**, no de demostrar que funciona.
- **Caso de prueba exitoso** = el que encontró un error (la salida no coincidió con la esperada).
- **Regresión:** volver a ejecutar casos de prueba ya existentes para confirmar que lo que antes andaba sigue andando. Se hace **después de modificar el software y cuando cambia el entorno** (parcial 2026); no "todas las semanas" ni "cuando lo diga el jefe de proyecto".
- **Regresión vs. confirmación:** la **confirmación** verifica que el defecto corregido realmente se solucionó; la **regresión**, que el arreglo no rompió otra cosa.
- **Por qué un desarrollador no es buen tester:** tiene mentalidad constructiva y no destructiva, puede haber entendido mal el requerimiento (y prueba con el mismo error), y no tiene incentivo para encontrar sus propios errores.
- **Los errores se agrupan:** donde encontraste uno, probablemente haya más cerca.

### Pruebas estáticas vs. dinámicas

| | Estáticas | Dinámicas |
|---|---|---|
| ¿Ejecutan el código? | No ("técnicas de no ejecución") | Sí, con datos de entrada |
| ¿Quién las hace? | Un equipo de revisión, o herramientas de análisis estático | El técnico de pruebas, comparando salida real contra esperada |
| ¿Sobre qué? | Cualquier documento: requisitos, diseño, planes de prueba, manuales, código sin ejecutar | Solo sobre código construido |
| ¿Qué encuentran? | **Defectos** (causas) | **Fallos** (síntomas) |
| ¿Cuándo? | Desde etapas tempranas, antes de que exista código | Necesitan código ejecutable |

**Ojo:** INTECO dice que las estáticas están más orientadas a verificación y las dinámicas a validación, pero es una tendencia, no una regla. En el examen manda el criterio de **contra qué se contrasta**: una prueba dinámica de sistema contra la especificación es **VER**.

### Técnicas de prueba

**Clasificación de las técnicas dinámicas:**

- **Basadas en la especificación (caja negra):** particiones de equivalencia, valores límite, tablas de decisión, transición de estados, casos de uso.
- **Basadas en la estructura (caja blanca):** pruebas de sentencia, de decisión y de caminos.
- **Basadas en la experiencia:** adivinación de errores (el tester usa su experiencia para anticipar dónde hay defectos, cuando no hay tiempo o especificación suficiente) y pruebas exploratorias.

**Qué técnica corresponde a cada señal del enunciado:**

| Señal | Técnica |
|---|---|
| Un campo con rango, longitud o formato; "valores válidos e inválidos"; extremos | Particiones o valores límite |
| "Todas las combinaciones", matriz, reglas de negocio que se cruzan | Tablas de decisión |
| Secuencia de estados, "pasa de X a Y" | Transición de estados |
| Flujo básico y alternativos, escenarios de punta a punta | Casos de uso |
| Se tiene el código, cobertura de sentencias o decisiones | Caja blanca |
| Volver a probar lo que ya andaba, después de un cambio | Regresión |

**Particiones de equivalencia:** agrupar las entradas en particiones válidas e inválidas. Un representante por partición alcanza, porque todo el grupo se comporta igual.

**Valores límite:** en lugar de un representante cualquiera, se toman los **extremos** de cada partición. En cada transición entre dos particiones va el par (último valor de una, primer valor de la siguiente). Rango válido 10 a 100 → **9, 10, 100, 101**.

**Ojo:** valores límite se aplica a toda partición que sea un **rango**: números, **longitudes de cadenas** (máximo 20 caracteres → 1, 19, 20, 21) y fechas. Para las particiones que no son rango (letras, caracteres especiales, un valor de una lista) se queda en partición pura.

Ejemplo con varios tramos: pedido inválido si es menor que 2; 20 % de descuento de 2 a 5; 30 % de 6 a 9; 40 % de 10 a 14.

| Transición | Par de valores límite |
|---|---|
| Inválido → 2 a 5 | 1 y 2 |
| 2 a 5 → 6 a 9 | 5 y 6 |
| 6 a 9 → 10 a 14 | 9 y 10 |

Conjunto: {1, 2, 5, 6, 9, 10}. Dos valores por transición, nunca un valor del medio de una partición.

**Tablas de decisión:** condiciones arriba, acciones abajo; **cada columna es una regla de negocio y un caso de prueba**. Se preguntan conteos: condiciones, acciones, columnas, casos válidos.

- Una condición de **más de dos valores** multiplica: 3 categorías × cuota al día sí/no = **6 columnas**, no 4.
- Se pueden unificar dos columnas si difieren en una sola condición y tienen la misma acción.
- Las **condiciones incompatibles** reducen los casos (si el usuario no existe, la contraseña es irrelevante).

**Transición de estados:** para sistemas modelables como máquina de estados. Las transiciones válidas se ven fácil; las inválidas son difíciles de detectar con el diagrama solo.

**Casos de uso:** se arma una tabla de escenarios (camino básico más alternativos) y después se cruzan con datos reales de la base. También sirve para pruebas de carga, estrés o seguridad, cruzando los casos existentes con distintos volúmenes.

### Particiones: cómo armar los casos (lo que se tomó en 2026)

- **Misma partición = el sistema trata igual a esos valores** (mismo comportamiento), aunque la salida cambie: 22 años con 2 días y 23 años con 3 días pagan distinto, pero se les aplica la misma regla.
- **Para definir las particiones** se tienen en cuenta las **entradas**, las **salidas esperadas** (particiones de salida), el **comportamiento esperado** y las **restricciones del negocio**, que dan los puntos de corte. La técnica (partición o límites) no: decide qué valores tomar de particiones ya definidas.
- **Ojo:** si la pregunta es "qué tener en cuenta al definir **los casos de prueba a partir de** las particiones" (AD 2025), la técnica **sí** va. Leé qué paso te preguntan.
- **Bordes del enunciado:** "menores de 25" es < 25 (el 25 va en la partición siguiente); "de 25 a 65" incluye a los dos; "más de 15" es > 15.
- **Inválidas:** por debajo del rango, por encima, tipo incorrecto y vacío (si el campo es obligatorio).
- **Armado de casos:** las **válidas se combinan** (cada caso lleva una partición de cada entrada). Las **inválidas van de a una**, con el resto de los datos válidos, porque el primer error corta el proceso y tapa al segundo.
- **Mínimo de casos para cubrir las válidas** = la cantidad de particiones de la entrada que más tiene. Si te dan casos ya armados, contá solo los que aportan una partición nueva.
- **Por qué alcanza con combinar:** la técnica supone entradas independientes. Si una regla de negocio cruza entradas ("menores de 25 con alquiler prolongado pagan recargo"), hace falta una **tabla de decisión**.
- **Zona muerta:** "se enciende por encima de 25 y se apaga por debajo de 20" → de 20 a 25 inclusive también es una partición (no pasa nada).
- **Ruido:** los datos que no intervienen en el cálculo (edad de jubilación, período de prueba) no generan particiones.

### Prestaciones, alfa y beta

| Prueba | Qué busca |
|---|---|
| **Carga** | Con el volumen de usuarios esperado (el de los requisitos), validar tiempos de respuesta y concurrencia |
| **Capacidad** | Aumentar la carga hasta encontrar el **punto umbral** donde las prestaciones se degradan |
| **Estrés** | Ir **más allá** de los límites de capacidad y verificar que el sistema se siga comportando de forma adecuada (sin corromper datos ni caerse mal) |
| **Escalabilidad** | Qué tan fácil absorbe el sistema mayores requisitos de prestaciones (más servidores, más usuarios) |
| **Estabilidad** | Carga estable, por debajo de la capacidad, durante mucho tiempo: busca degradaciones por mala gestión de recursos (p. ej. pérdidas de memoria) |

**Alfa y beta** (pruebas de aceptación, para productos de mercado masivo):

| | Alfa | Beta |
|---|---|---|
| Entorno | De desarrollo, controlado | Del cliente, su entorno real |
| Presencia | El cliente prueba con un experto del desarrollo al lado | El cliente queda solo con el producto |
| Quién registra los errores | El desarrollador, mientras observa | El cliente, que informa los fallos |
| Orden | Primero | Después de la alfa |

## 6. Trampas recurrentes

Para repasar en los últimos minutos antes de entrar.

1. **VER vs. VAL:** contra un documento o estándar acordado = VER; contra el uso real y la necesidad del usuario = VAL. Es la regla más preguntada.
2. **Lo obligatorio en CMMI son las metas** (específicas y genéricas). Las prácticas son esperadas. Las genéricas institucionalizan; las específicas son el contenido técnico de cada área.
3. **Nivel de madurez:** todas las áreas del nivel y de los inferiores. Si falta una sola, cae al nivel anterior completo (falta un área de nivel 2 → nivel 1).
4. **Activo** (reutilizable: plantillas, guías) vs. **producto de trabajo** (de un proyecto o cliente). "Ambos" nunca fue la correcta.
5. **OPD define y guarda** (biblioteca de activos, repositorio de mediciones) · **OPF evalúa y mejora** (planes de acción, benchmarking, incorpora lecciones aprendidas) · **OT capacita**.
6. **PP** = planificar y comprometer antes de ejecutar · **PMC** = monitorear y corregir solo los desvíos significativos.
7. **"¿Hay problema de calidad?"** con selección múltiple: no mezcles opciones del "sí" con las del "no". Primero decidí de qué lado estás y después marcá todas las razones de ese lado.
8. **"Ninguna de las opciones" existe y a veces es la correcta.** Sobre todo en preguntas de prácticas puntuales, donde los distractores vienen con el título alterado a propósito.
9. **Valores límite** se aplica a cualquier partición que sea un rango (números, longitudes, fechas), con pares en cada transición. Si no hay rango, es partición pura.
10. **Particiones:** las válidas se combinan; las inválidas van de a una. Mínimo de casos = particiones de la entrada que más tiene.
11. **"El diseño siempre precede a la codificación"** → Falso a nivel proyecto si hay módulos en paralelo. Solo vale dentro de la cadena de un mismo módulo.
12. **Estáticas** = no ejecutan, buscan defectos, las hace un equipo de revisión. **Dinámicas** = ejecutan, buscan fallos, las hace el tester. Para VER/VAL, igual manda contra qué se contrasta.
13. **Alfa** = en desarrollo, con experto al lado, registra el desarrollador. **Beta** = en el entorno del cliente, solo, registra el cliente. Alfa antes que beta.
14. **Ciclo de vida:** requerimientos estables → cascada; inestables → iterativo; entregas tempranas → incremental.
15. **Regresión:** después de modificar el software y cuando cambia el entorno.
16. **Avance de una tarea:** esfuerzo consumido, esfuerzo restante y estado de los productos de trabajo, los tres juntos.

## 7. Preguntas del parcial del 26/09/2026

El parcial original, resuelto. Sirve para ver el estilo: el recuperatorio va sobre los mismos temas con otros enunciados.

**1) ¿Cuál es el nivel de madurez que se centra en la predictibilidad cuantitativa?**

Opciones: 2 · 3 · 4 · 5 · Ninguno de los mencionados.

**Respuesta: 4** (Gestionado cuantitativamente). El 2 se centra en el proyecto, el 3 en la estandarización de la organización y el 5 en la mejora continua.

**2) ¿Cuáles de los elementos que se mencionan son elementos informativos dentro del CMMI?**

Opciones: Prácticas genéricas · Subprácticas · Declaraciones de propósito · Productos típicos de trabajo · Objetivos genéricos · Ninguno de los mencionados.

**Respuesta: Subprácticas, declaraciones de propósito y productos típicos de trabajo.** Las prácticas genéricas son componentes esperados y los objetivos (metas) genéricos son requeridos.

**3) ¿Cuál es el área de proceso que se encarga de establecer los recursos necesarios para un proyecto?**

Opciones: PMC · OPD · PP · OPF · Ninguno de los mencionados.

**Respuesta: PP** (SP 2.4 Planificar los recursos del proyecto).

**4) Cualquier desvío encontrado dentro del control y monitoreo de un proyecto debe ser resuelto. ¿Verdadero o falso?**

**Respuesta: Falso.** Solo se actúa sobre los desvíos significativos. Es la tercera vez que sale (2020, 2021 y 2026).

**5) Indique qué se debe tener en cuenta al definir las particiones de equivalencia para armar los casos de prueba.**

Opciones: Las restricciones del negocio · El comportamiento esperado del sistema · Las salidas esperadas del sistema · Las entradas al sistema · La técnica a emplear (particiones o valores límite) · Si la prueba es alfa o beta · Si la prueba la va a realizar personal del área de desarrollo · Si se cuenta con una herramienta de automatización.

**Respuesta: las cuatro primeras.** Las restricciones del negocio dan los puntos de corte; el comportamiento esperado define qué es "tratar igual"; las salidas generan particiones de salida; las entradas son lo que se particiona. Alfa/beta, quién la ejecuta y la herramienta tienen que ver con la ejecución, no con el diseño. La técnica decide qué valores tomar de particiones ya definidas.

**6) ¿Cuál es el mínimo de casos de prueba adicionales para garantizar la cobertura completa de todas las particiones de equivalencia de entrada válidas? (2 puntos)**

Un sistema de alquiler de vehículos determina la tarifa según la edad del conductor y los días de alquiler. Conductores menores de 25: tratamiento diferente; de 25 a 65: categoría estándar; mayores de 65: categoría especial. De 1 a 3 días: tarifa corta; de 4 a 7: semanal; de 8 a 15: extendida; más de 15: prolongada. Casos ya definidos: CP1 (22 años, 2 días) · CP2 (40, 10) · CP3 (23, 3).

**Respuesta: 2.**

| Entrada | Particiones válidas |
|---|---|
| Edad | E1 < 25 · E2 25 a 65 · E3 > 65 |
| Días | D1 1 a 3 · D2 4 a 7 · D3 8 a 15 · D4 > 15 |

CP1 cubre E1 + D1; CP2 cubre E2 + D3; **CP3 repite E1 + D1**, así que no aporta nada. Faltan E3, D2 y D4, y las válidas se combinan: CP4 (70, 5) cubre E3 + D2 y CP5 (30, 20) cubre E2 + D4. Las trampas: **1** (creer que CP3 suma), **3** (un caso por partición faltante, sin combinar) y **10** (todas las combinaciones: 3 × 4 = 12 menos 2; eso sería tabla de decisión).

**10) Antes de la validación final de un sistema web de pedidos para sucursales (PCs con Windows, red corporativa con restricciones de seguridad, impresoras de tickets y lectores de código de barras), ¿qué acciones son apropiadas para establecer el entorno de validación?**

Opciones: Configurar una PC con la misma versión de Windows de las sucursales · Revisar el código fuente contra los estándares de programación · Modificar los requisitos funcionales para que coincidan con el comportamiento actual · Configurar condiciones de red similares a las de la red corporativa · Incorporar una impresora de tickets equivalente · Preparar una base de datos con información representativa de situaciones reales · Ejecutar pruebas unitarias sobre cada módulo antes de integrar · Configurar usuarios con perfiles y permisos equivalentes a los de los vendedores.

**Respuesta: Windows, red, impresora, base de datos representativa y perfiles de usuario.** Es VAL SP 1.2: replicar el entorno real del usuario. Revisar código contra estándares y las pruebas unitarias son verificación; cambiar los requisitos para que coincidan con el sistema no se hace nunca.

**11) Las pruebas de regresión deberían realizarse: v) todas las semanas · w) después de que el software haya sido modificado · x) tan frecuentemente como sea posible · y) cuando el entorno haya cambiado · z) cuando lo indique el jefe de proyecto.**

**Respuesta: w e y son verdaderas; v, x y z son falsas.** La regresión responde a un cambio (en el software o en el entorno), no a un calendario ni a una orden.

## 8. Preguntas de práctica

Son 60 preguntas del cuestionario de la cursada, filtradas a los temas del recuperatorio y revisadas contra la wiki y el banco de parciales. Las respuestas están al final, en la sección Respuestas, para que puedas practicar sin verlas.

### CMMI: modelo, niveles y componentes

**1) Determine los elementos que tratan en CMMI la institucionalización de un proceso.**

- a) Metas genéricas
- b) Metas específicas
- c) Prácticas genéricas
- d) Prácticas específicas
- e) Ninguna de las mencionadas

*Puede haber más de una correcta.*

**2) Son componentes requeridos de un área de proceso CMMI:**

- a) Metas genéricas
- b) Sub-prácticas genéricas
- c) Metas específicas
- d) Herramientas

*Puede haber más de una correcta.*

**3) Determine la veracidad de la siguiente afirmación: el nivel de madurez al que corresponde el aseguramiento de la calidad, y en el cual nace, es el nivel 3.**

- a) Verdadero
- b) Falso

**4) ¿Cuál es el nivel de madurez de la software factory que se describe?**

La software factory “ATodooNada” tiene todas las áreas de proceso de nivel 3 implementadas; solo le falta el área PMC, que no es de nivel 3.

- a) 1
- b) 2
- c) 3
- d) 4
- e) 5

**5) Determine el/las área/s de proceso que son necesarias para alcanzar el nivel de madurez 2 de CMMI.**

- a) PP
- b) PMC
- c) OPD
- d) VER

*Puede haber más de una correcta.*

**6) Estoy en una software factory con nivel de madurez 2. Esto es importante porque voy a encontrar en cada proyecto:**

- a) Un cronograma del proyecto.
- b) Un proceso de prueba definido a nivel organización.
- c) Un plan de proyecto.
- d) Una lista de puntos de control del cronograma del proyecto.
- e) Estándares.

*Puede haber más de una correcta.*

### OPD y OPF: gestión de procesos de la organización

**7) ¿Cuál es el/las área(s) de CMMI que se encarga(n) de verificar y almacenar los productos de trabajo a nivel organizacional (es decir, los que se usan en todos los proyectos)?**

- a) PP
- b) NINGUNA de las anteriores
- c) OPF
- d) PMC
- e) OPD
- f) OT

*Puede haber más de una correcta.*

**8) ¿Cuál es el área que se encarga de mantener el repositorio de medidas de producto y proceso que están relacionadas con el conjunto de procesos estándar de la organización?**

- a) OPF
- b) OPD
- c) OPP
- d) MA

**9) Cuando se almacenan las métricas de un proyecto en el repositorio de mediciones de la software factory, ¿cuál es el/las área(s) de CMMI que intervienen?**

- a) OT (Formación Organizativa)
- b) PP (Planificación de Proyecto)
- c) OPF (Enfoque de Procesos de la Organización)
- d) OPD (Definición de Procesos de la Organización)

*Puede haber más de una correcta.*

**10) Relacione la actividad descripta con el área de proceso de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

Detallar en qué tipo de proyectos puede no realizarse el Modelado de Negocio (apartándose del proceso estándar), invocando causas justificadas.

- a) OPD (Definición de Procesos de la Organización)
- b) NINGUNA de las otras áreas
- c) PMC (Monitorización y Control del Proyecto)
- d) PP (Planificación de Proyecto)
- e) OT (Formación Organizativa)
- f) VAL (Validación)
- g) OPF (Enfoque de Procesos de la Organización)
- h) VER (Verificación)

**11) Relacione la actividad descripta con el área de proceso y la práctica específica de CMMI que correspondan (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

Escribir el procedimiento por el cual deberá pedirse la excepción en un proyecto en particular, indicando motivos justificados, para no incluir Testing Automatizado (a diferencia de lo determinado por el proceso establecido).

- a) RD / SP 3.4 Analizar los requerimientos para alcanzar el equilibrio
- b) NINGUNA de las otras opciones
- c) OPD / SP 1.2 Establecer las descripciones de los modelos de ciclo de vida
- d) CM / SP 2.1 Seguir las peticiones de cambio
- e) VER / SP 1.3 Establecer los procedimientos y los criterios de verificación
- f) PP / SP 1.3 Definir el ciclo de vida del proyecto
- g) PP / SP 2.1 Establecer el presupuesto y el calendario
- h) REQM / SP 1.1 Obtener una comprensión de los requerimientos
- i) OT / SP 1.4 Establecer la capacidad de formación
- j) OPF / SP 1.2 Evaluar los procesos de la organización
- k) MA / SP 1.3 Especificar los procedimientos de recogida y de almacenamiento de datos
- l) PP / SP 2.7 Establecer el plan de proyecto
- m) PPQA / SP 1.2 Evaluar objetivamente los productos de trabajo y los servicios
- n) OPD / SP 1.1 Establecer los procesos estándar
- o) OPD / SP 1.3 Establecer los criterios y las guías de adaptación
- p) PMC / SP 2.3 Gestionar las acciones correctivas
- q) PMC / SP 1.2 Monitorizar los compromisos
- r) PMC / SP 2.1 Analizar problemas

**12) Relacione la actividad descripta con el área de proceso de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

Realizar una reunión con 3 Project Managers para analizar el procedimiento definido (y aún no publicado) para el seguimiento de los proyectos, con el objetivo de encontrar y eliminar probables inconsistencias y/o errores. Dicho procedimiento fue redactado por otro Project Manager, quien está colaborando con la redacción de los procedimientos iniciales.

- a) PMC (Monitorización y Control del Proyecto)
- b) OPF (Enfoque de Procesos de la Organización)
- c) VER (Verificación)
- d) OT (Formación Organizativa)
- e) NINGUNA de las otras áreas
- f) PP (Planificación de Proyecto)
- g) VAL (Validación)
- h) OPD (Definición de Procesos de la Organización)

**13) ¿Qué área se encarga de evaluar los procesos de la organización contra los de otras organizaciones?**

- a) OPD (Definición de Procesos de la Organización)
- b) OT (Formación Organizativa)
- c) OPF (Enfoque de Procesos de la Organización)
- d) PP (Planificación de Proyecto)

**14) Relacione la actividad descripta con el área de proceso de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

El gerente de QA de la software factory decidió impulsar un proceso de evaluación de la forma en que trabaja la empresa, con el objeto de determinar cuáles son sus puntos sólidos y cuáles los endebles. Para ello, está presentando en la reunión de gerencia los objetivos, la dedicación necesaria del personal y los plazos de la iniciativa, con el fin de lograr el consenso necesario para llevarla a cabo.

- a) VAL (Validación)
- b) PP (Planificación de Proyecto)
- c) NINGUNA de las otras áreas
- d) OPF (Enfoque de Procesos de la Organización)
- e) OPD (Definición de Procesos de la Organización)
- f) VER (Verificación)
- g) OT (Formación Organizativa)
- h) PMC (Monitorización y Control del Proyecto)

**15) Relacione la actividad descripta con el área de proceso de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

Analizar tendencias en los informes de lecciones aprendidas de los proyectos terminados, para detectar cambios que podrían introducirse en los procesos.

- a) OPD (Definición de Procesos de la Organización)
- b) OT (Formación Organizativa)
- c) OPF (Enfoque de Procesos de la Organización)
- d) VAL (Validación)
- e) PMC (Monitorización y Control del Proyecto)
- f) NINGUNA de las otras áreas
- g) PP (Planificación de Proyecto)
- h) VER (Verificación)

**16) Relacione la actividad descripta con el área de proceso y la práctica específica de CMMI que correspondan (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

Revisar los informes de no conformidad de procesos generados por el área de SQA, para diseñar posibles cambios a la plantilla de casos de uso.

- a) CM / SP 3.2 Realizar auditorías de configuración
- b) REQM / SP 1.5 Identificar las inconsistencias entre el trabajo del proyecto y los requerimientos
- c) PPQA / SP 1.2 Evaluar objetivamente los productos de trabajo y los servicios
- d) PPQA / SP 1.1 Evaluar objetivamente los procesos
- e) RD / SP 1.2 Desarrollar los requerimientos de cliente
- f) REQM / SP 1.1 Obtener una comprensión de los requerimientos
- g) PPQA / SP 2.2 Establecer registros
- h) NINGUNA de las otras áreas
- i) MA / SP 2.4 Comunicar los resultados
- j) PPQA / SP 2.1 Comunicar y asegurar la resolución de las no conformidades
- k) PMC / SP 1.2 Monitorizar los compromisos

### Ciclos de vida y gestión de proyectos

**17) El ciclo de vida que mejora las posibilidades de salir antes a producción con un producto de software es:**

- a) Cascada
- b) Iterativo
- c) Incremental

**18) Determine la/las afirmaciones que son válidas y que aplican en un proyecto de desarrollo de software basado en un ciclo de vida incremental.**

- a) La prueba unitaria se realiza en cada incremento.
- b) La prueba de sistema no aplica al primer incremento, pero sí al resto de los incrementos.
- c) La prueba de aceptación aplica al último incremento, pero no a los anteriores.

*Puede haber más de una correcta.*

**19) El ciclo de vida de desarrollo de software que permite trabajar con requerimientos no estabilizados es:**

- a) Cascada
- b) Incremental
- c) Iterativo

**20) El ciclo de vida que menos colabora con un desarrollo de software cuando los requerimientos son inestables es:**

- a) Cascada
- b) Incremental
- c) Iterativo

**21) ¿Cuál(es) es el ciclo de vida que permite, al ser usado como base para un proyecto, reducir el riesgo de subestimación del esfuerzo?**

- a) Cascada
- b) Iterativo
- c) Incremental
- d) Prototipado

*Puede haber más de una correcta.*

**22) Determine el ciclo de vida que más se ajusta a la situación que se plantea.**

Estamos frente a un proyecto de mantenimiento correctivo. Se ha estimado que la funcionalidad estará lista en un par de semanas. Las correcciones son ajustes a requerimientos que ya están implementados.

- a) Cascada
- b) Iterativo
- c) Incremental
- d) Prototipado

**23) Señale el/los ciclos de vida que se usan como base en proyectos de desarrollo donde los requerimientos son conocidos y estables.**

- a) Cascada
- b) Incremental
- c) Iterativo
- d) Ninguno de los mencionados

*Puede haber más de una correcta.*

**24) Dado el caso planteado, ¿cuál es el ciclo de vida que mejor se adapta al desarrollo de los requerimientos?**

Se han definido una serie de requerimientos para un producto de software y se han organizado en los siguientes módulos: Alumnos, Inscripciones, Horarios y Asignaturas. El esfuerzo está dado en horas.

| Módulo | ID | Requerimiento | Esfuerzo (h) |
|---|---|---|---|
| Alumnos | 1 | Registrar datos personales | 4 |
| Alumnos | 2 | Actualizar datos personales | 3 |
| Alumnos | 3 | Visualizar los datos de un alumno | 4 |
| Asignaturas | 4 | Registrar asignaturas | 4 |
| Asignaturas | 5 | Ver asignaturas por plan | 4 |
| Horarios | 6 | Mostrar horarios de asignaturas en comisión | 10 |
| Horarios | 7 | Mostrar horarios de asignatura | 6 |
| Horarios | 8 | Crear horario | 4 |
| Horarios | 9 | Actualizar horario | 3 |
| Horarios | 10 | Crear comisión | 4 |
| Horarios | 11 | Validar solapamiento entre horarios | 2 |
| Horarios | 12 | Validar solapamiento de docentes entre horarios | 2 |
| Inscripciones | 13 | Registrar inscripciones a carreras | 4 |
| Inscripciones | 14 | Registrar inscripción a comisión | 4 |
| Inscripciones | 15 | Generar lista de inscriptos a comisión | 3 |
| Inscripciones | 16 | Registrar alumno en horario de comisión | 4 |
| Inscripciones | 17 | Validar condiciones de correlatividad de inscripción de alumno en asignatura y horario | 8 |
| Inscripciones | 18 | Anular horario de inscripción | 2 |
| Inscripciones | 19 | Controlar cupos | 2 |

- a) Cascada
- b) Iterativo
- c) Incremental

**25) Estamos frente a un proyecto que se ha basado en un ciclo de vida cascada. Indique en qué fase se confecciona el manual de usuario.**

- a) Análisis
- b) Diseño
- c) Codificación
- d) Prueba

**26) A continuación se presentan una serie de artefactos. Indique cuáles revisten importancia para realizar el manual de usuario.**

- a) GUI
- b) Caso de uso
- c) Código fuente
- d) Informe de pruebas unitarias realizadas

*Puede haber más de una correcta.*

**27) Estamos frente a un proyecto basado en un ciclo de vida incremental con X incrementos y se nos consulta en cuáles incrementos se debe disponer de prueba de sistema. Nuestra respuesta es:**

- a) Todos.
- b) En los últimos.
- c) En los incrementos pares.
- d) En el último incremento.
- e) En ninguno, la prueba de sistema no hace falta.

**28) En un proyecto de desarrollo de software basado en un ciclo incremental, el análisis se realiza solo en el primer incremento.**

- a) Verdadero
- b) Falso

**29) En un proyecto de desarrollo de software basado en un ciclo incremental, la prueba de sistema se realiza solo en el último incremento.**

- a) Verdadero
- b) Falso

**30) ¿Cuál/cuáles de las siguientes variables inciden sobre la elección de un ciclo de vida genérico de desarrollo como base para nuestro proyecto?**

- a) Necesidad de poner en producción el producto de software, incluso antes de estar terminado
- b) Estabilidad en los requerimientos
- c) Disponibilidad presupuestaria del cliente
- d) Cantidad de recursos disponibles para el desarrollo
- e) Tipo de lenguaje de programación
- f) Ninguna de las mencionadas

*Puede haber más de una correcta.*

**31) Determine cuál es el ciclo de vida que más se adecua a las necesidades planteadas para el proyecto en cuestión.**

Un cliente nos ha convocado para desarrollar un sistema de información mediante una aplicación web. El cliente necesita salir al mercado lo antes posible: como consecuencia de la pandemia, sus sistemas actuales no están adaptados para el home office.

- a) Cascada
- b) Prototipado
- c) Incremental
- d) Iterativo

### PP y PMC: planificación y control del proyecto

**32) Las siguientes actividades/procesos pueden formar parte de la gestión de proyectos:**

- a) Definir las actividades del proyecto
- b) Estimar la duración de las actividades del proyecto
- c) Elaborar presupuestos de proyecto
- d) Definir el equipo de proyecto

*Puede haber más de una correcta.*

**33) Forma parte de lo que se realiza en el proceso "Definir el equipo del proyecto":**

- a) Determinar los roles del proyecto
- b) Estimar el esfuerzo previsto para cada rol
- c) Determinar las responsabilidades de cada rol
- d) Controlar el cronograma de cada rol

*Puede haber más de una correcta.*

**34) Relacione la actividad descripta con el área de proceso de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

En el marco del proyecto "Fila de espera virtual", luego de una charla en la que el responsable de TI del cliente informó que hasta el tercer mes del proyecto no estará disponible el equipo para manejar los monitores de la sala de espera, el PM está modificando las fechas de la etapa de capacitación e implementación, originalmente previstas para el fin del segundo mes de proyecto. Esta modificación está siendo documentada en el producto de trabajo que será presentado la semana que viene en la reunión donde se informará a todo el equipo de proyecto las actividades a realizar.

- a) PP (Planificación de Proyecto)
- b) VER (Verificación)
- c) OT (Formación Organizativa)
- d) OPF (Enfoque de Procesos de la Organización)

**35) Relacione la actividad descripta con el área de proceso de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

El cliente ha informado que el server destinado al ambiente de producción que compró recientemente estará disponible con 10 días de retraso (respecto a lo acordado en la primera conversación al respecto). Por lo tanto, en este momento el equipo del proyecto está determinando si es necesario tomar medidas para compensar dicho retraso, de manera de informarlo en la reunión donde se reunirá a todo el equipo de trabajo por primera vez para establecer compromiso sobre roles, objetivos y plazos del proyecto.

- a) PPQA / SP 2.2 Establecer registros
- b) CM / SP 3.2 Realizar auditorías de configuración
- c) NINGUNA de las otras áreas
- d) PMC / SP 1.2 Monitorizar los compromisos
- e) CM / SP 2.1 Seguir las peticiones de cambio
- f) PMC / SP 2.1 Analizar los problemas
- g) REQM / SP 1.1 Obtener una comprensión de los requerimientos
- h) PP / SP 1.1 Estimar el alcance del proyecto
- i) PPQA / SP 1.2 Evaluar objetivamente los productos de trabajo y los servicios
- j) PP / SP 2.4 Planificar los recursos del proyecto
- k) PPQA / SP 2.1 Comunicar y asegurar la resolución de las no conformidades

**36) Relacione la actividad descripta con el área de proceso de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

El cliente ha informado que el server destinado al ambiente de producción que compró recientemente estará disponible con 20 días de retraso (respecto a lo acordado en la reunión donde se juntó a todo el equipo de trabajo por primera vez para establecer compromiso sobre roles, objetivos y plazos del proyecto). Por lo tanto, en este momento el equipo del proyecto está determinando si es necesario tomar medidas para compensar dicho retraso.

- a) PP / SP 3.3 Obtener el compromiso con el plan
- b) OPD / SP 1.3 Establecer los criterios y las guías de adaptación
- c) VER / SP 1.2 Establecer el entorno de verificación
- d) OPD / SP 1.6 Establecer los estándares del entorno de trabajo
- e) PP / SP 2.7 Establecer el plan de proyecto
- f) VER / SP 2.3 Analizar los datos de la revisión entre pares
- g) PMC / SP 1.5 Monitorizar la involucración de las partes interesadas
- h) VAL / SP 1.2 Establecer el entorno de validación
- i) PMC / SP 2.1 Analizar problemas
- j) VAL / SP 2.1 Realizar la validación
- k) VER / SP 3.2 Analizar los resultados de la verificación
- l) VER / SP 2.1 Preparar las revisiones entre pares
- m) PP / SP 1.1 Estimar el alcance del proyecto
- n) VER / SP 1.3 Establecer los procedimientos y los criterios de verificación
- o) PP / SP 2.4 Planificar los recursos del proyecto
- p) PPQA / SP 1.2 Evaluar objetivamente los productos de trabajo y los servicios
- q) PP / SP 1.4 Determinar las estimaciones de esfuerzo y de coste
- r) PMC / SP 1.2 Monitorizar los compromisos
- s) VAL / SP 2.2 Analizar los resultados de la validación
- t) NINGUNA de las otras áreas

**37) Relacione la actividad descripta con el área de proceso de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

En la última reunión de avance del proyecto quedó claro que hay un retraso respecto a lo planificado en el relevamiento del proceso de ventas. Analizando la situación, se concluyó que la causa radica en el desconocimiento del usuario clave respecto al proceso del cual es responsable, es decir, que debe reemplazarse al usuario clave por otra persona con mayor experiencia en el sector. Por lo tanto, en este momento se está realizando una reunión con el usuario clave y el jefe del sector para confirmar que el usuario clave actual se desvincula del proyecto y que el jefe del sector participará en las reuniones semanales de relevamiento.

- a) VER (Verificación)
- b) NINGUNA de las otras áreas
- c) VAL (Validación)
- d) OT (Formación Organizativa)
- e) PMC (Monitorización y Control del Proyecto)
- f) OPD (Definición de Procesos de la Organización)
- g) PP (Planificación de Proyecto)
- h) OPF (Enfoque de Procesos de la Organización)

**38) Relacione la actividad descripta con el área de proceso de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

Corroborar si los usuarios clave, que forman parte del equipo de proyecto, están respondiendo a los mails que envía el analista para confirmar la exactitud del contenido de las minutas de reunión publicadas. Estas reuniones fueron convocadas de acuerdo a la agenda de trabajo previamente pactada con el cliente.

- a) OT (Formación Organizativa)
- b) PMC (Monitorización y Control del Proyecto)
- c) OPD (Definición de Procesos de la Organización)
- d) NINGUNA de las otras opciones
- e) OPF (Enfoque de Procesos de la Organización)
- f) PP (Planificación de Proyecto)
- g) VER (Verificación)
- h) VAL (Validación)

**39) ¿En qué momento del ciclo de vida de un proyecto definiría los controles (puntos de control y monitoreo) de un proyecto?**

- a) Inicio
- b) Planificación
- c) Fin
- d) Ejecución

**40) Cualquier desvío encontrado dentro del control y monitoreo de un proyecto debe ser resuelto.**

- a) Verdadero
- b) Falso

**41) Cuando el estado real de un proyecto se desvía significativamente de los valores esperados, se llevan a cabo acciones correctivas según sea apropiado, y esto puede llevar a replanificar. Si esto sucede, ¿se deben redefinir los controles (puntos de control y monitoreo) del proyecto?**

- a) Falso
- b) Verdadero

**42) Sobre PMC: ¿en cuáles de las tareas mencionadas existen elementos para presumir un problema?**

Al realizar el monitoreo de una tarea, aproximadamente al 50 % de su avance, el responsable del proyecto encuentra que el esfuerzo se ha cumplido y que los profesionales han trabajado, pero no existe evidencia documental del trabajo. Cada tarea tiene una duración de 20 días y se trabaja jornada completa de 8 horas.

- a) La tarea es de análisis
- b) La tarea es de codificación
- c) La tarea es de prueba

*Puede haber más de una correcta.*

### Verificación y validación

**43) La actividad de Validación intenta asegurar que:**

- a) Estamos construyendo el producto correctamente
- b) El software se ajusta a su especificación
- c) El producto o componente de un producto se ajusta a su uso previsto cuando se sitúa en su entorno previsto
- d) El software hace lo que el usuario (cliente) requiere (necesita)
- e) Estamos construyendo el producto correcto

*Puede haber más de una correcta.*

**44) La actividad de Verificación intenta asegurar que:**

- a) El software hace lo que el usuario (cliente) requiere (necesita)
- b) Los productos de trabajo seleccionados cumplen sus requerimientos especificados
- c) Estamos construyendo el producto correctamente
- d) El software se ajusta a su especificación
- e) Estamos construyendo el producto correcto

*Puede haber más de una correcta.*

**45) Indique qué área se ajusta mejor a cada artefacto: Verificación, Validación o Ninguna.**

Los siguientes artefactos se usan habitualmente en los proyectos de la empresa en estudio, y sobre ellos se realizan actividades de revisión dentro del programa de calidad.

- a) Lista inicial de requerimientos funcionales
- b) Lista inicial de requerimientos no funcionales
- c) Minuta
- d) La lista de casos de prueba armada a partir de las particiones de equivalencia
- e) Base de datos de programación

**46) Indique qué área se ajusta mejor a cada artefacto o aspecto: Verificación, Validación o Ninguna.**

Los siguientes artefactos y aspectos del desarrollo de software se usan habitualmente en los proyectos de la empresa en estudio, y sobre ellos se realizan actividades de revisión dentro del programa de calidad.

- a) Un documento minuta que refleja lo hablado en una reunión de requerimientos
- b) Lista inicial de requerimientos no funcionales
- c) La mantenibilidad del software (que tiene un impacto directo en los costos del cliente que compra el producto)
- d) El software desarrollado

**47) Indique verdadero o falso para cada afirmación.**

- a) Muchos usuarios tienen pocas expectativas respecto al software y pueden soportar que se produzcan fallas.
- b) Una compañía de software puede decidir lanzar al mercado un programa antes de que esté plenamente probado y depurado.
- c) El objetivo final de los procesos de verificación y validación es establecer confianza de que el sistema de software es adecuado.
- d) El objetivo final de los procesos de verificación y validación es establecer confianza de que el sistema de software realiza las funciones correctamente.
- e) Algunas pruebas funcionales pueden realizarse sin conocimiento de cómo funciona el programa.
- f) Para probar si un requerimiento se cumple, alcanza con armar un caso de prueba.

**48) Relacione la actividad descripta con el área de proceso y la práctica específica de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

En el marco del proyecto "Reserva de hoteles on-line", distribuir entre los analistas elegidos para participar de la reunión la descripción del último caso de uso, que acaba de ser terminada por otro analista y que será chequeada en dicha reunión.

- a) VAL/SP 1.2 Establecer el entorno de validación
- b) REQM/SP 1.3 Gestionar los cambios de los requerimientos
- c) VER/SP 2.3 Analizar los datos de la revisión entre pares
- d) VER/SP 3.1 Realizar la verificación
- e) VER/SP 3.2 Analizar los resultados de la verificación
- f) VER/SP 1.2 Establecer el entorno de verificación
- g) VER/SP 1.3 Establecer los procedimientos y los criterios de verificación
- h) VER/SP 2.2 Llevar a cabo las revisiones entre pares
- i) VAL/SP 1.3 Establecer los procedimientos y los criterios de validación
- j) PMC/SP 1.2 Monitorizar los compromisos
- k) RD/SP 3.4 Analizar los requerimientos para alcanzar el equilibrio
- l) VER/SP 2.1 Preparar las revisiones con usuarios
- m) PPQA/SP 2.1 Comunicar y asegurar la resolución de las no conformidades
- n) CM/SP 2.2 Controlar los elementos de configuración
- o) VAL/SP 2.2 Analizar los resultados de la validación
- p) VAL/SP 2.1 Preparar las revisiones entre pares
- q) PMC/SP 2.3 Gestionar las acciones correctivas
- r) PPQA/SP 2.2 Establecer registros
- s) PPQA/SP 1.2 Evaluar objetivamente los productos de trabajo y los servicios
- t) PMC/SP 1.5 Monitorizar la involucración de las partes interesadas
- u) CM/SP 2.1 Seguir las peticiones de cambio
- v) PMC/SP 2.1 Analizar problemas
- w) NINGUNA de las otras opciones
- x) REQM/SP 1.5 Identificar las inconsistencias entre el trabajo del proyecto y los requerimientos

**49) Relacione la actividad descripta con el área de proceso y la práctica específica de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

En el marco del proyecto "Liquidación y Cobranza a Obras Sociales", personal del equipo de proyecto de la software factory realiza un control respecto a si el contenido de los casos de uso cumple con lo documentado en las Minutas de Relevamiento.

- a) REQM/SP 1.1 Obtener una comprensión de los requerimientos
- b) CM/SP 2.2 Controlar los elementos de configuración
- c) PPQA/SP 1.2 Evaluar objetivamente los productos de trabajo y los servicios
- d) RD/SP 1.1 Obtener las necesidades
- e) MA/SP 1.3 Especificar los procedimientos de recogida y de almacenamiento de datos
- f) CM/SP 3.2 Realizar auditorías de configuración
- g) MA/SP 2.2 Analizar los datos de la medición
- h) PPQA/SP 2.1 Comunicar y asegurar la resolución de las no conformidades
- i) PPQA/SP 2.2 Establecer registros
- j) VER/SP 2.2 Llevar a cabo las revisiones entre pares
- k) VAL/SP 2.1 Realizar la validación
- l) VER/SP 3.1 Realizar la verificación
- m) PMC/SP 1.2 Monitorizar los compromisos
- n) PMC/SP 1.5 Monitorizar la involucración de las partes interesadas
- o) RD/SP 3.5 Validar los requerimientos

**50) Relacione la actividad descripta con el área de proceso de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

Realizar un control respecto a si los nombres de las etiquetas de los campos de ingreso por pantalla cumplen las definiciones estándar planteadas en el Glosario, en el marco del proyecto "Liquidación y Cobranza a Obras Sociales".

- a) VER/SP 2.1 Preparar las revisiones entre pares
- b) VER/SP 3.2 Analizar los resultados de la verificación
- c) VER/SP 3.1 Realizar la verificación
- d) PP/SP 1.4 Determinar las estimaciones de esfuerzo y de coste
- e) OPD/SP 1.6 Establecer los estándares del entorno de trabajo
- f) VAL/SP 2.1 Realizar la validación
- g) PMC/SP 1.5 Monitorizar la involucración de las partes interesadas
- h) VAL/SP 1.2 Establecer el entorno de validación
- i) PP/SP 1.1 Estimar el alcance del proyecto
- j) PPQA/SP 1.2 Evaluar objetivamente los productos de trabajo y los servicios
- k) OPD/SP 1.3 Establecer los criterios y las guías de adaptación
- l) NINGUNA de las otras áreas
- m) PMC/SP 1.2 Monitorizar los compromisos
- n) VER/SP 1.3 Establecer los procedimientos y los criterios de verificación
- o) PP/SP 2.4 Planificar los recursos del proyecto
- p) PP/SP 2.7 Establecer el plan de proyecto
- q) PMC/SP 2.1 Analizar problemas
- r) VER/SP 2.3 Analizar los datos de la revisión entre pares
- s) VAL/SP 2.2 Analizar los resultados de la validación
- t) VER/SP 1.2 Establecer el entorno de verificación
- u) PP/SP 3.3 Obtener el compromiso con el plan

**51) Relacione la actividad descripta con el área de proceso de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

Realizar un control con el usuario respecto a si los nombres de las etiquetas de los campos de ingreso por pantalla se entienden adecuadamente y si se corresponden con los conceptos de negocio correctos, en el marco del proyecto "Liquidación y Cobranza a Obras Sociales".

- a) VER/SP 2.1 Preparar las revisiones entre pares
- b) VAL/SP 2.1 Realizar la validación
- c) VER/SP 2.3 Analizar los datos de la revisión entre pares
- d) PP/SP 2.7 Establecer el plan de proyecto
- e) PP/SP 3.3 Obtener el compromiso con el plan
- f) OPD/SP 1.6 Establecer los estándares del entorno de trabajo
- g) VER/SP 3.2 Analizar los resultados de la verificación
- h) PMC/SP 2.1 Analizar problemas
- i) VER/SP 1.3 Establecer los procedimientos y los criterios de verificación
- j) PMC/SP 1.5 Monitorizar la involucración de las partes interesadas
- k) VER/SP 1.2 Establecer el entorno de verificación
- l) VAL/SP 2.2 Analizar los resultados de la validación
- m) VAL/SP 1.2 Establecer el entorno de validación
- n) OPD/SP 1.3 Establecer los criterios y las guías de adaptación
- o) PPQA/SP 1.2 Evaluar objetivamente los productos de trabajo y los servicios
- p) VER/SP 3.1 Realizar la verificación
- q) PP/SP 1.4 Determinar las estimaciones de esfuerzo y de coste
- r) NINGUNA de las otras áreas
- s) PP/SP 2.4 Planificar los recursos del proyecto
- t) PP/SP 1.1 Estimar el alcance del proyecto
- u) PMC/SP 1.2 Monitorizar los compromisos

**52) Relacione la actividad descripta con el área de proceso de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

Determinar que se controlarán mediante Inspección los diagramas de secuencia del proyecto "Aplicativo para gestión on-line de solicitudes de compra de moneda extranjera".

- a) NINGUNA de las otras áreas
- b) OPD (Definición de Procesos de la Organización)
- c) VAL (Validación)
- d) PP (Planificación de Proyecto)
- e) OT (Capacitación Organizacional)
- f) VER (Verificación)
- g) PMC (Monitorización y Control del Proyecto)
- h) OPF (Enfoque de Procesos de la Organización)

**53) Relacione la actividad descripta con el área de proceso y la práctica específica de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

En el marco del proyecto "Autoconsulta servicios de larga distancia", dos analistas elegidos para participar de la reunión chequean el último caso de uso que acaba de ser terminado por otro analista, planteando las observaciones pertinentes.

- a) PPQA/SP 1.2 Evaluar objetivamente los productos de trabajo y los servicios
- b) VER/SP 2.3 Analizar los datos de la revisión entre pares
- c) PMC/SP 2.3 Gestionar las acciones correctivas
- d) PPQA/SP 2.2 Establecer registros
- e) RD/SP 3.4 Analizar los requerimientos para alcanzar el equilibrio
- f) PMC/SP 2.1 Analizar problemas
- g) VER/SP 2.2 Llevar a cabo las revisiones entre pares
- h) REQM/SP 1.5 Identificar las inconsistencias entre el trabajo del proyecto y los requerimientos
- i) VAL/SP 1.3 Establecer los procedimientos y los criterios de validación
- j) CM/SP 2.1 Seguir las peticiones de cambio
- k) REQM/SP 1.3 Gestionar los cambios de los requerimientos
- l) VER/SP 1.2 Establecer el entorno de verificación
- m) PMC/SP 1.5 Monitorizar la involucración de las partes interesadas
- n) VAL/SP 1.2 Establecer el entorno de validación
- o) PPQA/SP 2.1 Comunicar y asegurar la resolución de las no conformidades
- p) VER/SP 3.2 Analizar los resultados de la verificación
- q) VER/SP 2.1 Preparar las revisiones entre pares
- r) NINGUNA de las otras opciones
- s) VAL/SP 2.1 Realizar la validación
- t) VER/SP 3.1 Realizar la verificación
- u) VAL/SP 2.2 Analizar los resultados de la validación
- v) PMC/SP 1.2 Monitorizar los compromisos
- w) CM/SP 2.2 Controlar los elementos de configuración
- x) VER/SP 1.3 Establecer los procedimientos y los criterios de verificación

**54) Relacione la actividad descripta con el área de proceso y la práctica específica de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

Ayer se realizó una reunión con 2 analistas para controlar los casos de uso escritos por otro de los analistas. Como consecuencia, los 2 analistas detectaron algunos problemas que deben corregirse en los casos de uso, para que el software a construir cumpla con lo definido en las minutas de reunión y en el artefacto de reglas de negocio, ya aprobados por el cliente. Ya se documentaron los hallazgos de la reunión y se envió ese documento al autor de los casos de uso, para que tenga el listado de los problemas a corregir. En este momento se está almacenando la información de las identidades de los analistas involucrados en una parte del repositorio a la que solo tiene acceso el personal del área de Calidad. Es decir, en la parte pública del repositorio solo queda la información relativa a los problemas a corregir, sin ninguna mención a los participantes de la reunión ni al autor de los casos de uso.

- a) VAL/SP 2.2 Analizar los resultados de la validación
- b) PMC/SP 2.3 Gestionar las acciones correctivas
- c) VAL/SP 2.1 Realizar la validación
- d) REQM/SP 1.2 Obtener el compromiso sobre los requerimientos
- e) PPQA/SP 1.2 Evaluar objetivamente los productos de trabajo y los servicios
- f) NINGUNA de las otras opciones
- g) VER/SP 2.2 Llevar a cabo las revisiones entre pares
- h) CM/SP 2.1 Seguir las peticiones de cambio
- i) PMC/SP 2.1 Analizar problemas
- j) CM/SP 2.2 Controlar los elementos de configuración
- k) PMC/SP 1.2 Monitorizar los compromisos
- l) VER/SP 2.3 Analizar los datos de la revisión entre pares
- m) REQM/SP 1.1 Obtener una comprensión de los requerimientos
- n) REQM/SP 1.5 Identificar las inconsistencias entre el trabajo del proyecto y los requerimientos
- o) RD/SP 3.4 Analizar los requerimientos para alcanzar el equilibrio
- p) VER/SP 2.1 Preparar las revisiones entre pares

**55) Relacione la actividad descripta con el área de proceso y la práctica específica de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

En el marco del proyecto "Autoconsulta servicios de larga distancia", distribuir entre los analistas elegidos para participar de la reunión la descripción del último caso de uso, que acaba de ser terminada por otro analista y que será chequeada en dicha reunión.

- a) REQM/SP 1.3 Gestionar los cambios de los requerimientos
- b) VER/SP 2.2 Llevar a cabo las revisiones entre pares
- c) PPQA/SP 2.2 Establecer registros
- d) VER/SP 3.1 Realizar la verificación
- e) CM/SP 2.2 Controlar los elementos de configuración
- f) VAL/SP 2.1 Realizar la validación
- g) VER/SP 1.2 Establecer el entorno de verificación
- h) PPQA/SP 2.1 Comunicar y asegurar la resolución de las no conformidades
- i) VAL/SP 1.3 Establecer los procedimientos y los criterios de validación
- j) VER/SP 3.2 Analizar los resultados de la verificación
- k) PMC/SP 2.3 Gestionar las acciones correctivas
- l) NINGUNA de las otras opciones
- m) VER/SP 2.3 Analizar los datos de la revisión entre pares
- n) CM/SP 2.1 Seguir las peticiones de cambio
- o) RD/SP 3.4 Analizar los requerimientos para alcanzar el equilibrio
- p) PMC/SP 1.5 Monitorizar la involucración de las partes interesadas
- q) PMC/SP 1.2 Monitorizar los compromisos
- r) VAL/SP 2.2 Analizar los resultados de la validación
- s) PMC/SP 2.1 Analizar problemas
- t) VER/SP 2.1 Preparar las revisiones entre pares
- u) VER/SP 1.3 Establecer los procedimientos y los criterios de verificación
- v) REQM/SP 1.5 Identificar las inconsistencias entre el trabajo del proyecto y los requerimientos
- w) PPQA/SP 1.2 Evaluar objetivamente los productos de trabajo y los servicios
- x) VAL/SP 1.2 Establecer el entorno de validación

**56) Relacione la actividad descripta con el área de proceso y la práctica específica de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

Coordinar con precisión la agenda de horarios en que puede utilizarse el server en instalaciones del cliente para realizar la prueba de aceptación.

- a) VAL/SP 2.2 Analizar los resultados de la validación
- b) CM/SP 2.2 Controlar los elementos de configuración
- c) PPQA/SP 1.2 Evaluar objetivamente los productos de trabajo y los servicios
- d) VAL/SP 1.2 Establecer el entorno de validación
- e) VER/SP 2.1 Preparar las revisiones entre pares
- f) VAL/SP 2.1 Realizar la validación
- g) CM/SP 2.1 Seguir las peticiones de cambio
- h) VER/SP 2.3 Analizar los datos de la revisión entre pares
- i) REQM/SP 1.1 Obtener una comprensión de los requerimientos
- j) VER/SP 1.2 Establecer el entorno de verificación
- k) PP/SP 2.1 Establecer el presupuesto y el calendario
- l) NINGUNA de las otras opciones
- m) PMC/SP 2.1 Analizar problemas
- n) VER/SP 2.2 Llevar a cabo las revisiones entre pares
- o) VER/SP 1.3 Establecer los procedimientos y los criterios de verificación
- p) REQM/SP 1.2 Obtener el compromiso sobre los requerimientos
- q) PP/SP 2.4 Planificar los recursos del proyecto

**57) Relacione la actividad descripta con el área de proceso de CMMI que corresponda (solo una), o indique NINGUNA si no encuadra con ninguna de las opciones.**

Coordinar con antelación la agenda en que serán citados los usuarios clave para realizar la prueba de aceptación.

- a) VAL (Validación)
- b) PP (Planificación de Proyecto)
- c) OPF (Enfoque de Procesos de la Organización)
- d) OPD (Definición de Procesos de la Organización)
- e) OT (Capacitación Organizacional)
- f) NINGUNA de las otras áreas
- g) VER (Verificación)
- h) PMC (Monitorización y Control del Proyecto)

### Técnicas de prueba: particiones y valores límite

**58) Calificación por edad y peso: ¿cuáles de las siguientes premisas son verdaderas?**

Un sistema de entrenamiento emite una calificación (de Bajo a Excelente) según la edad y el peso que se ingresan de una persona. El criterio que emplea el sistema se representa en la siguiente tabla (rangos de peso para cada calificación):

| Edad | Excelente | Muy bueno | Bueno | Regular | Bajo |
|---|---|---|---|---|---|
| 7 | 27–31 | 32 | 33–34 | 35–37 | menos de 27 o más de 37 |
| 8 | 30–34 | 35 | 36–40 | 41–42 | menos de 30 o más de 42 |
| 9 | 34–39 | 40–41 | 42–45 | 46–47 | menos de 34 o más de 47 |
| 10 | 40–46 | 47–50 | 51–55 | 56–58 | menos de 40 o más de 58 |
| 11 | 42–46 | 47–50 | 51–52 | 53–55 | menos de 42 o más de 55 |
| 12 | 45–52 | 53 | 54–55 | 56–60 | menos de 45 o más de 60 |
| 13 | 55–59 | 60 | 61–62 | 63–65 | menos de 55 o más de 65 |
| 14 | 60–65 | 66–67 | 68–72 | 73–75 | menos de 60 o más de 75 |

- a) Para la edad hay una sola partición de equivalencia, que contiene los valores 7 a 14.
- b) Para la edad hay 8 particiones de equivalencia.
- c) Para la calificación hay una sola partición de equivalencia, que contiene los valores Bajo a Excelente.
- d) Para la calificación hay 6 particiones de equivalencia.
- e) Tablas de decisión sería una técnica más apropiada en este caso.
- f) Para la edad 11, algunos de los valores límite de peso son: 41, 42, 46, 47, 55, 56.
- g) Para la edad 11, algunos de los valores límite de peso son: 40, 42, 47, 55, 57.
- h) Para la edad, los valores límite son: 7, 8, 9, 10, 11, 12, 13, 14.
- i) Para la edad, los valores límite son: 7 y 14.
- j) Tablas de estados sería una técnica más apropiada en este caso.
- k) Casos de uso sería una técnica más apropiada en este caso.

*Puede haber más de una correcta.*

**59) ¿Cuál de los siguientes es un conjunto mínimo de valores de entrada que cubre las particiones de equivalencia del campo de cantidad?**

Un sistema de pedidos de materia prima para panaderías acepta pedidos de distintos productos. Los productos más caros se venden por gramo y los más baratos por kilo. Independientemente de las unidades, la cantidad de pedido válida más pequeña es 0,5 g (por ejemplo, medio gramo de vainas de cardamomo) y la válida más grande es 25 kg (por ejemplo, 25 kilos de harina). La precisión del campo de unidades es de 0,1.

- a) 10; 28
- b) 0,2; 0,9; 29,5
- c) 12,3
- d) 0,4; 0,5; 25; 25,1

**60) Indique cuáles de los siguientes grupos de valores están en la misma partición de equivalencia.**

Un programa determina el ingreso y el porcentaje de descuento en un servicio a partir de la edad de la persona. Si tiene menos de 18 años, no permite el ingreso. Si tiene entre 18 y 30 años, aplica un descuento del 20 %. Si tiene más de 30, ingresa sin descuento.

- a) 30, 31, 32
- b) 17, 18, 19
- c) 18, 29, 30
- d) 31, 32, 100
- e) 29, 30, 31
- f) 17, 29, 31

*Puede haber más de una correcta.*

## Respuestas

✅ confirmada por la nota del cuestionario, la wiki o un parcial anterior · ⚠️ deducida (la fuente no la da explícita; el motivo está en cada una).

### CMMI: modelo, niveles y componentes

**1)** **a) y c).** Según el modelo CMMI (pág. 144), las metas genéricas y las prácticas genéricas son las que tratan directamente la institucionalización del proceso. Las específicas tratan lo particular de cada área. ✅

**2)** **a) y c).** Los componentes requeridos son solo las metas (específicas y genéricas). Las prácticas son esperadas, las subprácticas son informativas y las herramientas ni siquiera son componentes del modelo. La nota habla de "objetivos genéricos", que es otra traducción de metas genéricas. ✅

**3)** **b) Falso.** El aseguramiento de la calidad es PPQA, un área de soporte de nivel 2, no de nivel 3. ✅

**4)** **a) 1.** PMC es de nivel 2. Los niveles son acumulativos y todo-o-nada: si falta un área de nivel 2 no se alcanza el nivel 2, y por lo tanto tampoco el 3, aunque se cumplan todas sus áreas. ✅

**5)** **a) y b).** PP y PMC son de nivel 2. OPD y VER son de nivel 3. ✅

**6)** **a), c) y d).** El cronograma y el plan de proyecto son de PP, y la lista de puntos de control del cronograma es de PP/PMC, todas de nivel 2. Un proceso de prueba definido a nivel organización y los estándares son de OPD, nivel 3. ✅

### OPD y OPF: gestión de procesos de la organización

**7)** **b) NINGUNA de las anteriores.** "Verificar", "almacenar" y "nivel organizacional" empujan hacia OPD, pero los productos de trabajo surgen de cada proyecto (código fuente, minutas). Si dijera "activos", sí sería OPD. ✅

**8)** **b) OPD.** Es OPD / SP 1.4 Establecer el repositorio de medición de la organización. La trampa es MA, que es de nivel 2 y mide el proyecto; el repositorio atado a los procesos estándar es un activo organizacional. ✅

**9)** **d) OPD (Definición de Procesos de la Organización).** El repositorio de mediciones es de la organización: OPD / SP 1.4 Establecer el repositorio de medición de la organización. Confirmada en el parcial 2021. ✅

**10)** **a) OPD (Definición de Procesos de la Organización).** Definir en qué casos un proyecto puede apartarse del proceso estándar es OPD / SP 1.3 Establecer los criterios y las guías de adaptación. ✅

**11)** **o) OPD / SP 1.3 Establecer los criterios y las guías de adaptación.** La subpráctica 3 pide especificar los procedimientos para proponer y aprobar excepciones al conjunto de procesos estándar. Misma respuesta para la variante "no incluir un Diseñador Gráfico". ✅

**12)** **h) OPD (Definición de Procesos de la Organización).** Es una revisión entre pares, pero sobre un procedimiento de la organización aún no publicado (un activo, no un producto de trabajo del proyecto): OPD / SP 1.1, subpráctica 8. La trampa es VER. ✅

**13)** **c) OPF (Enfoque de Procesos de la Organización).** El benchmarking frente a los procesos de otras organizaciones es una de las fuentes de mejoras candidatas de OPF. Confirmada en el parcial 2021. ✅

**14)** **d) OPF (Enfoque de Procesos de la Organización).** Evaluar los procesos para comprender sus fortalezas y debilidades es OPF / SP 1.2 Evaluar los procesos de la organización; presentar la iniciativa a la gerencia es obtener el patrocinio (subpráctica 1). ✅

**15)** **c) OPF (Enfoque de Procesos de la Organización).** Es OPF / SP 1.3 Identificar las mejoras de procesos de la organización. Las lecciones aprendidas las registra cada proyecto (PMC), pero analizarlas para mejorar los procesos es de OPF. ✅

**16)** **h) NINGUNA de las otras áreas.** PPQA emite las no conformidades; revisarlas para proponer cambios a un activo es de OPF (SP 1.3 según la wiki), y OPF no está entre las opciones. La trampa es PPQA / SP 2.1. ✅

### Ciclos de vida y gestión de proyectos

**17)** **c) Incremental.** Según la guía de V&V de INTECO, después del primer incremento el equipo ya puede entregar al menos una porción de la funcionalidad planificada. ✅

**18)** **a).** Cada incremento es una mini-cascada que termina en un producto funcional, así que en todos se hacen todas las pruebas: unitaria, de sistema y de aceptación. Por eso b) y c) son falsas. ✅

**19)** **c) Iterativo.** Busca reducir el riesgo de malentendidos entre las necesidades del usuario y el producto final: los requisitos se refinan en cada iteración. ✅

**20)** **a) Cascada.** Una vez cerrado el análisis, los requerimientos no se vuelven a analizar hasta terminar la prueba, así que los cambios no se contemplan. ✅

**21)** **d) Prototipado.** Construir la maqueta obliga a entrar en el detalle del requerimiento y eso mejora la estimación del esfuerzo. El incremental no ayuda: si se subestimó el último módulo, se descubre recién al hacerlo. ✅

**22)** **a) Cascada.** En el mantenimiento correctivo prevalecen la programación y la prueba, y con un par de semanas de duración no vale la pena repartir en incrementos de pocos días, con su versionado y despliegue. ✅

**23)** **a) y b).** Con requerimientos estables sirven tanto cascada (entrega todo al final) como incremental (reparte los requisitos en versiones). El iterativo apunta a requerimientos inestables. ✅

**24)** **c) Incremental.** Los requerimientos están definidos, estimados y agrupados en cuatro módulos: son estables y se pueden repartir, cada módulo es un incremento natural. No hay inestabilidad que justifique iterativo. ⚠️ Deducida: la nota está vacía y la wiki la deja abierta ("apunta a Incremental"); cascada también encaja con requisitos estables, lo que inclina hacia incremental es la partición en módulos.

**25)** **d) Prueba.** Según INTECO, el proceso de pruebas incluye, además de definir, elaborar, ejecutar y evaluar las pruebas, la elaboración de la documentación de usuario (manuales de usuario y de administración). ✅

**26)** **a) y b).** La GUI y el caso de uso muestran qué ve el usuario y qué pasos sigue. El código fuente y el informe de pruebas unitarias no le sirven a quien usa el sistema. ⚠️ Deducida: la nota aclara que no hay clave; es el razonamiento del autor del cuestionario, que la wiki repite.

**27)** **a) Todos.** Cada incremento se plantea para terminar en un producto funcional, así que en todos se hace la prueba de sistema. ✅

**28)** **b) Falso.** Cada incremento es una mini-cascada con su propio análisis, diseño, codificación y prueba de los requisitos de ese incremento. ✅

**29)** **b) Falso.** La prueba de sistema se hace en todos los incrementos, no solo en el último (ver pregunta 11). ✅

**30)** **a) y b).** La urgencia por desplegar una versión y la estabilidad de los requerimientos son las que definen el ciclo. El esquema de la nota lo resume: sin estabilidad → iterativo o prototipado; con estabilidad → incremental si hay que tener algo funcionando lo más rápido posible, cascada si lo importante es el producto final. Presupuesto, recursos y lenguaje no inciden. ✅

**31)** **c) Incremental.** Salir al mercado lo antes posible pide entregas tempranas y parciales: después del primer incremento ya hay algo en producción. La nota está vacía, pero la wiki la resuelve así y es coherente con la pregunta 1. ✅

### PP y PMC: planificación y control del proyecto

**32)** **a), b), c) y d).** Las cuatro son procesos de gestión de proyectos de la Guía práctica: definir las actividades (alcance), estimar la duración (tiempo), elaborar presupuestos (costes) y definir el equipo (personal). En el parcial 2012 la marcada fue "Todas las anteriores". ✅

**33)** **a) y c).** Según la Guía avanzada de Gestión de Proyectos, definir el equipo consiste en determinar los roles y las responsabilidades del proyecto. Estimar el esfuerzo es estimación y controlar el cronograma es del grupo Tiempo. ✅

**34)** **a) PP (Planificación de Proyecto).** La reunión donde se informa al equipo las actividades es la semana que viene: todavía se está planificando, no monitorizando. La Nota y la wiki lo resuelven como PP / SP 2.4 Planificar los recursos del proyecto. ✅

**35)** **j) PP / SP 2.4 Planificar los recursos del proyecto.** La reunión de lanzamiento (todo el equipo por primera vez) está en el futuro, así que todavía se planifica: se ajusta el cronograma por la demora de un recurso. Si esa reunión ya hubiera pasado, sería PMC. ✅

**36)** **i) PMC / SP 2.1 Analizar problemas.** La reunión de lanzamiento ya ocurrió, así que se está monitorizando contra el plan; determinar si hay que compensar el retraso es recoger y analizar el problema y decidir las acciones correctivas. La Nota cita además GP 2.7 y SP 1.2 sin decidir; la wiki da SP 2.1. ✅

**37)** **e) PMC (Monitorización y Control del Proyecto).** El desvío se detectó en una reunión de avance que ya pasó y ahora se actúa sobre la involucración de las partes interesadas (reemplazar al usuario clave). La Nota se apoya en GP 2.7 y la wiki agrega SP 1.5 y las acciones correctivas de SG 2. ✅

**38)** **b) PMC (Monitorización y Control del Proyecto).** Se controla si los usuarios clave participan como estaba previsto, contra una agenda ya pactada: el plan está cerrado, así que no es PP. Corresponde a SP 1.5 Monitorizar la involucración de las partes interesadas. ✅

**39)** **b) Planificación.** Los puntos de control y los hitos se definen al planificar, en la EDT; en ejecución se usan, no se definen. Confirmada en los parciales 2020 y 2021. ✅

**40)** **b) Falso.** Solo se actúa sobre las desviaciones significativas: las que, si se dejan sin resolver, impiden al proyecto cumplir sus objetivos. Confirmada en los parciales 2020 y 2021. ✅

**41)** **b) Verdadero.** Los controles forman parte del plan; si se replanifica, cambian fechas, hitos y tareas, y los puntos de control tienen que acompañar al nuevo plan. ⚠️ Deducida: la Nota solo dice que la replanificación puede incluir corregir el plan original, sin mencionar los controles.

**42)** **a), b) y c).** El problema es la falta de evidencia documental, sea cual sea el tipo de tarea: una tarea no está terminada si no incluye su documentación o evidencia. El error es creer que en codificación o prueba alcanza con el trabajo técnico. ✅

### Verificación y validación

**43)** **c), d) y e).** La nota cita el propósito de VAL en CMMI: el producto se ajusta a su uso previsto cuando se sitúa en su entorno previsto, es decir, "se construye la cosa correcta". a) y b) describen la verificación. ✅

**44)** **b), c) y d).** Según la nota, el propósito de VER es asegurar que los productos de trabajo seleccionados cumplen sus requerimientos especificados: "se construye correctamente", de acuerdo con la especificación. a) y e) describen la validación. ✅

**45)** **a) VAL · b) VAL · c) VER o VAL, según cómo se controle · d) VER · e) Ninguna.** Minuta: es VAL si se controla en una reunión con el cliente y VER si se controla contra artefactos internos (nota). Los casos de prueba armados por particiones son VER, porque se comparan contra las particiones sin intervención del usuario (nota). La fuente cita CMMI pág. 561 para la lista de requerimientos funcionales: los requerimientos figuran entre lo que se valida con el usuario. ⚠️ Deducida en b) y e): la nota no las resuelve. La lista de no funcionales sigue la misma lógica que la de funcionales; la base de datos de programación es parte del entorno de desarrollo, no un producto a revisar, y la wiki la marca como dudosa.

**46)** **a) VER o VAL, según cómo se controle · b) VAL · c) VER · d) VAL.** Minuta: si se pasa el documento a otros analistas para una reunión de revisión, es VER (ejemplo de la nota); si se repasa con el cliente, es VAL. El software desarrollado se confronta con el uso previsto, así que es VAL (wiki U5, ejercicio 3). ⚠️ Deducida en b) y c): la nota no las cubre. La lista de no funcionales se resuelve igual que en la pregunta 3. La mantenibilidad es calidad interna que el cliente no percibe y figura en las listas de comprobación de las revisiones entre pares (VER SP 2.1); la mención a los costos del cliente es un distractor.

**47)** **a) V · b) V · c) V · d) V · e) V · f) F.** De b) a f) salen de la wiki (U5, ejercicio 16): se puede lanzar antes de terminar de probar si hay pocos competidores; las pruebas funcionales sin conocer el código son de caja negra; un solo caso de prueba no alcanza para probar un requerimiento. ⚠️ Deducida en a): la nota está vacía. La wiki ("Grados de confianza") dice que los usuarios toleran fallos cuando los beneficios superan las desventajas, y la frase coincide con Sommerville (conocimiento general, no está textual en la wiki).

**48)** **w) NINGUNA de las otras opciones.** Son pares (mismo rol) y el chequeo es a futuro: corresponde VER/SP 2.1 Preparar las revisiones entre pares, y esa opción no está. La p) tiene mal el área, porque las revisiones entre pares solo existen en VER; la l) tiene mal el nombre de la práctica. ✅

**49)** **l) VER/SP 3.1 Realizar la verificación.** Se compara un artefacto (casos de uso) contra otro (minutas) sin el cliente, así que es VER, y se está haciendo en este momento. No es VAL porque no participa el cliente, ni PPQA porque no se controla un estándar de la organización. ✅

**50)** **c) VER/SP 3.1 Realizar la verificación.** El glosario es del proyecto, no un estándar organizacional, así que no es PPQA. El control se hace en el momento; si fuera armar la lista de etiquetas a controlar, sería preparar la verificación. ✅

**51)** **b) VAL/SP 2.1 Realizar la validación.** Participa el usuario y se juzga contra los conceptos de negocio, no contra un artefacto: es VAL, y se está haciendo en el momento. ✅

**52)** **f) VER (Verificación).** La inspección es un tipo de revisión, una técnica de control estática, y las revisiones se vinculan con la verificación (nota). Elegir qué productos se controlan y con qué método es VER SP 1.1 (wiki). ✅

**53)** **g) VER/SP 2.2 Llevar a cabo las revisiones entre pares.** Son pares revisando el trabajo de otro analista, y el chequeo ocurre ahora, no se está preparando. ✅

**54)** **l) VER/SP 2.3 Analizar los datos de la revisión entre pares.** La revisión entre pares y la documentación de hallazgos ya pasaron. Lo que se hace ahora es almacenar y proteger los datos de la revisión, subprácticas de SP 2.3 (nota y wiki). ✅

**55)** **t) VER/SP 2.1 Preparar las revisiones entre pares.** Es la misma situación que la pregunta 6, pero acá la opción correcta sí está. Distribuir el producto a revisar antes de la reunión es una subpráctica de la preparación (wiki). ✅

**56)** **d) VAL/SP 1.2 Establecer el entorno de validación.** La prueba de aceptación es VAL (nota). Coordinar el uso del server en las instalaciones del cliente es preparar el entorno de validación (wiki U5, ejercicio 11). Si dijera prueba de sistema, sería VER. ✅

**57)** **a) VAL (Validación).** Citar a los usuarios clave para la prueba de aceptación es VAL: el usuario juzga el producto en su uso previsto (nota). ✅

### Técnicas de prueba: particiones y valores límite

**58)** **b), e), f) y i).** Cada edad tiene su propio criterio, así que hay 8 particiones de edad, y tablas de decisión es lo más apropiado porque dos condiciones (edad y peso) combinadas dan la calificación (nota y wiki U5, ejercicio 17). Para la edad 11, las fronteras de peso son 41/42, 46/47, 50/51, 52/53 y 55/56: g) incluye 40 y 57, que no son límites. ⚠️ Deducida en parte: la última frase de la nota sugiere que todas las edades de 7 a 14 son valores límite (opción h); la wiki toma solo 7 y 14, y se sigue a la wiki. c) y d) no las cubre ninguna fuente: la calificación tiene 5 valores distintos, así que no son ni 1 ni 6 particiones.

**59)** **b) 0,2; 0,9; 29,5.** Hay tres particiones: inválida menor a 0,5, válida de 0,5 a 25 e inválida mayor a 25 (nota). El conjunto mínimo toma un representante de cada una. d) son valores límite, no un conjunto mínimo; a) y c) no cubren la partición inválida de abajo. ✅

**60)** **c) y d).** Las particiones son: menos de 18 (no ingresa), de 18 a 30 (20 % de descuento) y más de 30 (sin descuento). 18, 29 y 30 caen en la segunda; 31, 32 y 100, en la tercera; las demás opciones mezclan particiones. ⚠️ Deducida: la nota tiene un error de tipeo ("18 <= x <= 31", que se superpone con x > 30); vale el enunciado, que dice de 18 a 30.
