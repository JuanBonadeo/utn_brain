# Ingeniería y Calidad de Software — Wiki

## Índice

1. Unidad 1 — Modelos de calidad de software y CMMI
2. Unidad 2 — Gestión de procesos (OPF, OPD, OT, RUP, SPEM)
3. Unidad 3 — Gestión de proyectos de software (PP, PMC y áreas de soporte)
4. Unidad 4 — Gestión efectiva de la calidad del producto (economía de las pruebas)
5. Unidad 5 — Verificación y Validación

> **Nota sobre la numeración:** las unidades 1, 2, 3 y 5 vienen rotuladas así en las fuentes.
> La unidad 4 es una inferencia mía: el bloque "Gestión efectiva calidad producto"
> (`Resumen de ISW.md`) no trae número en ninguna fuente. Confirmar contra el programa
> de cátedra. Ver [Dudas / pendientes](#dudas--pendientes-3) de esa unidad.

---

## Desarrollo

### Unidad 1 — Modelos de calidad de software y CMMI

#### Conceptos clave

- **Calidad** = *idoneidad de uso*. Tres definiciones que conviven en la materia:
  - **Juran / clásica:** características del producto que satisfacen las necesidades del
    cliente + **inexistencia de deficiencias**.
  - **CMMI:** capacidad de un conjunto de características inherentes de un producto,
    componente o **proceso** de satisfacer por completo los requisitos del cliente.
  - **ISO:** conjunto de propiedades y características que le confieren aptitud para
    satisfacer necesidades **explícitas o implícitas**.
- **Elementos que influyen en la calidad:** procesos y buenas prácticas · herramientas ·
  personas · medidas y métricas.
- **Tres niveles de gestión de la calidad:** producto (pruebas en paralelo a cada etapa) ·
  proyecto (controlar fases y áreas de gestión) · **proceso** (gestionar las áreas de
  proceso de toda la organización mediante una metodología → es el nivel donde juega CMMI).
- **Software = programas + datos + documentos.** Es un elemento **lógico**: se **desarrolla**,
  no se fabrica; **no se estropea pero se deteriora** (por los cambios del mantenimiento).
- **Ingeniería del software (IEEE):** aplicación de un enfoque **sistemático, disciplinado y
  cuantificable** al desarrollo, operación y mantenimiento del software.
- **Tecnología multicapa:** sobre una base de **compromiso con la calidad** se apoyan
  **Procesos** → **Métodos** → **Herramientas**.
- **CMMI: 5 niveles de madurez** (1 Inicial · 2 Gestionado · 3 Definido · 4 Gestionado
  cuantitativamente · 5 En optimización) y **22 áreas de proceso**.
- **Componentes de un área de proceso:** requeridos (metas SG/GG) · esperados (prácticas
  SP/GP) · informativos (todo lo demás).

#### Desarrollo

**Metodología y por qué sirve un modelo.** Una guía de buenas prácticas aporta un punto de
partida, la experiencia acumulada de otras empresas, un lenguaje y visión común, y técnicas
para crear un modelo. Trabajar con un modelo probado permite predecir mejor el comportamiento
y el rendimiento de la empresa, y produce: menos defectos totales, menos tiempo de entrega,
menor costo, más satisfacción del cliente, más beneficios.

**Características del software (por qué necesita ingeniería).**

- Se **desarrolla**, no se fabrica: no hay línea de producción, cada producto es distinto
  porque se construye para requisitos únicos de un cliente.
- El recurso principal son **las personas**, y no son intercambiables con tiempo: agregar
  gente no acelera linealmente porque el desarrollo requiere coordinación y comunicación.
  Un nuevo integrante no es productivo de inmediato y consume tiempo de los que ya están.
- **No se estropea, se deteriora:** cada cambio de mantenimiento tiene probabilidad de
  introducir defectos nuevos.
- La **reutilización** existe pero está lejos de su potencial: identificar componentes
  reutilizables es difícil justamente porque cada producto es único.

**Tipos y aplicaciones del software.** Dos grandes categorías: **de aplicaciones** (dan
servicio al negocio) y **de sistemas** (operan y mantienen el sistema informático). Por
aplicación: sistemas, tiempo real, gestión (SIG), ingeniería/científico, empotrado, basado en
web, inteligencia artificial. Un criterio de clasificación es el **determinismo de la
información**: predictibilidad del orden y momento de llegada de los datos (un análisis de
ingeniería es determinado; un SO multiusuario es **indeterminado**).

**Etapas de la ingeniería del software.** Análisis de requisitos → Especificación → Diseño y
arquitectura → Programación → Prueba → Mantenimiento.

**Tipos de mantenimiento** (entra seguido en examen):

| Tipo | Qué hace |
|---|---|
| **Perfectivo** | Mejorar la calidad **interna** del sistema |
| **Evolutivo** | Altas/bajas/modificaciones por expansión o cambio de necesidades del usuario |
| **Adaptativo** | Cambios por el **entorno** (hardware, software de base, DBMS, comunicaciones) |
| **Correctivo** | Corrección de errores |

**Las tres capas.**

- **Proceso** — marco de trabajo que permite al jefe de proyecto controlar la gestión y las
  actividades de ingeniería. Un proceso definido responde: quién se comunica con quién, cómo
  se coordinan las actividades interdependientes, quién es responsable de qué, quién produce
  qué producto de trabajo y cómo se evalúa. Un proceso debe: identificar actividades y tareas,
  definir el flujo entre ellas, identificar los productos de trabajo, y **especificar los
  puntos de control de calidad**.
- **Métodos** — el "**cómo**" técnico: análisis, diseño, codificación, pruebas, mantenimiento.
- **Herramientas** — automatización de soporte a las dos capas anteriores. Cuando se usan
  herramientas, la documentación pasa a ser parte integral del trabajo en vez de una actividad
  adicional.

---

##### CMMI — Niveles de madurez

Un **nivel de madurez** es una meseta evolutiva definida para la mejora de procesos: consta de
prácticas específicas y genéricas para un **conjunto predefinido de áreas de proceso**. Se
miden por el **logro de las metas específicas y genéricas** de ese conjunto.

| Nivel | Nombre | Núcleo |
|---|---|---|
| 1 | **Inicial** | Procesos ad-hoc y caóticos. El éxito depende de la competencia y **heroicidad** del personal, no de procesos probados. Producen productos que funcionan, pero **exceden presupuesto y no cumplen calendario**. Se comprometen en exceso, **abandonan los procesos en crisis**, e **incapaces de repetir sus éxitos**. |
| 2 | **Gestionado** | Los proyectos planifican y realizan según **políticas**; personal con habilidad y recursos; se involucran las partes interesadas; se **monitoriza, controla y revisa**. Estado visible para la dirección en **hitos**. La disciplina se mantiene incluso bajo estrés. |
| 3 | **Definido** | Procesos **bien caracterizados y comprendidos**, descritos en estándares, procedimientos, herramientas y métodos. Existe el **conjunto de procesos estándar de la organización**; los proyectos lo **adaptan** según guías de adaptación. |
| 4 | **Gestionado cuantitativamente** | La organización y los proyectos fijan **objetivos cuantitativos** de calidad y rendimiento del proceso. Medidas analizadas **estadísticamente** e incorporadas al **repositorio de medición**. Se identifican y corrigen las **causas especiales** de variación. |
| 5 | **En optimización** | **Mejora continua** basada en comprensión cuantitativa de las **causas comunes** de variación. Mejoras **incrementales e innovadoras**, de proceso y tecnológicas, con objetivos cuantitativos de mejora como criterio de gestión. |

**Las dos distinciones que se preguntan siempre:**

- **2 vs 3** — *alcance y consistencia*. En nivel 2 los estándares, descripciones de proceso y
  procedimientos pueden ser **bastante distintos en cada instancia** del proceso. En nivel 3
  se **adaptan desde el conjunto estándar de la organización**, y por lo tanto son
  **consistentes**, salvo las diferencias que permitan las **guías de adaptación**. Además, en
  nivel 3 los procesos se gestionan más proactivamente usando la comprensión de las
  interrelaciones entre actividades y medidas detalladas.
- **4 vs 5** — *tipo de variación tratada*. Nivel 4 trata las **causas especiales** y provee
  **predictibilidad estadística**. Nivel 5 trata las **causas comunes** y **cambia el proceso**
  para mejorar su rendimiento. Complementariamente: en nivel 4 el rendimiento es predecible
  **cuantitativamente**; en nivel 3, sólo **cualitativamente**.

**Reglas operativas del modelo escalonado (clave para los ejercicios):**

- Para estar en un nivel hay que satisfacer **TODAS** las áreas de proceso de ese nivel **y de
  los anteriores**. Si falta una sola, no se está en ese nivel.
- Los niveles son **acumulativos**: una organización nivel 5 sigue ejecutando PP y PMC
  (nivel 2) todos los días.
- Se puede instanciar un área de nivel superior al propio si el contexto de negocio lo
  justifica, pero se corre el riesgo de intentar prácticas **sin la base institucional que las
  soporte** — funciona hasta que aparece el estrés, que es justo cuando más se la necesita.

---

##### CMMI — Componentes de un área de proceso

Un **área de proceso** es un grupo de prácticas relacionadas que, implementadas conjuntamente,
satisfacen un conjunto de objetivos importantes para la mejora en esa área.

| Categoría | Qué es | Componentes |
|---|---|---|
| **Requeridos** | Lo que la organización **debe** realizar para satisfacer el área. Base de las evaluaciones. | **Metas específicas (SG)** · **Metas genéricas (GG)** |
| **Esperados** | Lo que la organización **puede** implementar para lograr un componente requerido. Guían a implementadores y evaluadores. | **Prácticas específicas (SP)** · **Prácticas genéricas (GP)** |
| **Informativos** | Detalles que ayudan a pensar cómo aproximarse a lo requerido y esperado. | Subprácticas · productos de trabajo típicos · ampliaciones · elaboraciones de GP · títulos y notas de metas y prácticas · referencias · declaración de propósito · notas introductorias · áreas de proceso relacionadas · ejemplos |

- **"Genérico"** significa que la **misma declaración se aplica a múltiples áreas de proceso**.
  Las **metas y prácticas genéricas son las que tratan la institucionalización** del proceso
  (pregunta directa de examen).
- **Ampliación** = nota o ejemplo relevante para una **disciplina particular** (ingeniería del
  hardware, de sistemas, del software).
- **Numeración:** `SG n` / `GG n` (secuencial) · `SP x.y` y `GP x.y`, donde **x = número de la
  meta** a la que pertenece e **y = número de secuencia** de la práctica dentro de esa meta.

##### Las 22 áreas de proceso

| Sigla | Nombre | Nivel |
|---|---|---|
| REQM | Gestión de requerimientos | 2 |
| PP | Planificación de proyecto | 2 |
| PMC | Monitorización y control del proyecto | 2 |
| SAM | Gestión de acuerdos con proveedores | 2 |
| MA | Medición y análisis | 2 |
| PPQA | Aseguramiento de la calidad de proceso y de producto | 2 |
| CM | Gestión de configuración | 2 |
| RD | Desarrollo de requerimientos | 3 |
| TS | Solución técnica | 3 |
| PI | Integración de producto | 3 |
| VER | Verificación | 3 |
| VAL | Validación | 3 |
| OPF | Enfoque en procesos de la organización | 3 |
| OPD (+IPPD) | Definición de procesos de la organización | 3 |
| OT | Formación organizativa | 3 |
| IPM (+IPPD) | Gestión integrada del proyecto | 3 |
| RSKM | Gestión de riesgos | 3 |
| DAR | Análisis de decisiones y resolución | 3 |
| OPP | Rendimiento del proceso de la organización | 4 |
| QPM | Gestión cuantitativa de proyecto | 4 |
| OID | Innovación y despliegue en la organización | 5 |
| CAR | Análisis causal y resolución | 5 |

> ⚠️ **Los nombres y siglas de las 22 áreas salen de las fuentes. La columna "Nivel" NO está
> completa en las fuentes**: sólo confirman explícitamente PP/PMC/REQM/PPQA/CM/MA = 2 y
> OPD/OPF/VER/VAL/RD = 3. El resto lo completé con CMMI-DEV v1.2 (que es la versión del
> apunte: 22 áreas, con OID e IPPD). Verificar contra el PDF de cátedra.

##### Guía de discriminación entre áreas (el ejercicio estrella del parcial)

El formato recurrente es: *"relacione la actividad descripta con el área de proceso (y la
práctica específica) que corresponda, o indique NINGUNA"*. Dos ejes deciden casi todo:

**Eje 1 — ¿Contra qué se compara y quién participa?**

| Situación | Área |
|---|---|
| Se compara un producto de trabajo contra **artefactos internos del propio proyecto** (CU vs. minutas, etiquetas vs. glosario del proyecto) | **VER** |
| Participa el **cliente / usuario** y se chequea si es lo que necesita (prueba de aceptación, revisar etiquetas con el usuario) | **VAL** |
| Se compara contra un **estándar o plantilla de la organización**, y lo hace **personal externo al proyecto** | **PPQA** |
| Se compara contra **convenciones definidas dentro del proyecto** (nomenclatura de archivos, líneas base, versiones) | **CM** |
| Reunión entre **pares** (mismo rol) revisando el trabajo de otro | **VER** — revisiones entre pares (SP 2.x) |

**Eje 2 — ¿En qué momento estoy?**

| Tiempo verbal del enunciado | Práctica |
|---|---|
| "se distribuirá / será chequeada / se determinará que se controlará" (futuro) | **Preparar** (SP 1.x o 2.1) |
| "está chequeando / realiza un control / se está revisando" (presente) | **Realizar / Llevar a cabo** |
| "ya se documentó, ahora se está almacenando la información" | **Analizar los datos / almacenar para futura referencia** |

**Trampas frecuentes registradas en el cuestionario:**

- Si la respuesta correcta es VER pero la opción ofrecida dice **VAL/SP 2.1 Preparar las
  revisiones entre pares**, la respuesta es **NINGUNA**: "revisiones entre pares" es de VER, no
  de VAL. Leer la sigla, no sólo el texto de la práctica.
- **Prueba de aceptación → VAL. Prueba de sistema → VER.**
- **Inspección** es un tipo de revisión → técnica **estática** → vinculada a **VER**.
- PMC vs PP se decide por **dónde está la reunión de avance**: si la reunión de lanzamiento/
  avance está **en el futuro**, todavía estoy planificando (**PP**); si **ya pasó**, estoy
  monitorizando (**PMC**).
- Si el enunciado plantea un problema **de un proyecto específico**, difícilmente sea OPD, OPF
  u OT (que son organizacionales). Excepción típica: seguimiento de un proceso nuevo en un
  **proyecto piloto** → OPF.

#### Ejercicios resueltos tipo

**1. ¿Qué componentes tratan la institucionalización de un proceso?**
→ **Metas genéricas** y **prácticas genéricas**. (Las específicas tratan lo particular del
área; las genéricas son las que se repiten en todas las áreas y son las que institucionalizan).

**2. ¿Cuáles son componentes *requeridos* de un área de proceso?**
→ **Metas genéricas** y **metas específicas**. (Las sub-prácticas son informativas; las
herramientas ni siquiera son componentes del modelo).

**3. La software factory "ATodooNada" tiene todas las áreas de nivel 3 implementadas, sólo le
falta PMC, que no es de nivel 3. ¿En qué nivel está?**
→ **Nivel 1.** PMC es de **nivel 2**. Como para estar en un nivel hay que cumplir **todas** las
áreas de ese nivel y de los anteriores, al fallar un área de nivel 2 no alcanza ni el nivel 2 —
queda en nivel 1, por más que tenga completo el nivel 3.

**4. ¿Qué áreas son necesarias para alcanzar el nivel 2? (PP · PMC · OPD · VER)**
→ **PP y PMC**. OPD y VER son de nivel 3.

**5. Estoy en una software factory de nivel 2. ¿Qué voy a encontrar en cada proyecto?**

| Elemento | Área | Nivel | ¿Está en una SF nivel 2? |
|---|---|---|---|
| Cronograma del proyecto | PP | 2 | ✅ |
| Plan de proyecto | PP | 2 | ✅ |
| Lista de puntos de control del cronograma | PP / PMC | 2 | ✅ |
| Proceso de prueba definido **a nivel organización** | OPD | 3 | ❌ |
| Estándares | OPD | 3 | ❌ |

**6. "El nivel de madurez al que corresponde el aseguramiento de calidad, y en el cual nace, es
el nivel 3."**
→ **Falso.** **PPQA** es un área de **soporte de nivel 2**.

**7. Tarea 1 — Contrastes y similitudes entre una organización nivel 1 y una nivel 5 en un
proyecto de desarrollo.**

*Escenario común:* **AdHoc S.A.** (nivel 1) y **Optima S.A.** (nivel 5) reciben el mismo
encargo (sistema de gestión académica, 19 requerimientos en 4 módulos, ~77 h, 3 meses) y sufren
el mismo imprevisto a mitad de proyecto: el server de producción llega 10 días tarde y el
cliente pide cambiar la regla de correlatividades.

| Momento | AdHoc (nivel 1) | Optima (nivel 5) |
|---|---|---|
| **Estimación** | A ojo del líder, sin dato histórico (nadie midió). Se compromete con lo que el cliente quiere oír | PP calibrado con el **repositorio de medición** (OPP): entrega un rango con confianza estadística, no un número |
| **Seguimiento** | "Vamos bien" hasta que se prueba y no anda | PMC + QPM: control estadístico de subprocesos; el desvío salta **antes** de impactar el cronograma |
| **El server tarde** | Horas extra y fin de semana; se saltean las pruebas de sistema. *Abandona el proceso en crisis*. Se salva por **heroicidad** | El riesgo ya estaba en RSKM con contingencia; se dispara **PMC/SP 2.1 Analizar problemas** y acción correctiva documentada. **El proceso no se abandona: se ejecuta** |
| **El cambio de requerimiento** | Se acuerda por teléfono; no se actualiza CU ni diseño. El código queda como única documentación | REQM (trazabilidad bidireccional) + CM (petición de cambio) + PPQA (audita la propagación) |
| **Prueba y entrega** | Se prueba lo que el tiempo permite, sin criterios de salida. Los defectos los encuentra el cliente | VER/VAL con entorno, procedimientos y **criterios** definidos de antemano; defectos contados por fase contra objetivo cuantitativo |
| **Cierre** | No pasa nada. Lo aprendido se va con la gente. *Incapacidad para repetir sus éxitos* | **CAR** busca **causas comunes** ("nuestra estimación subestima los requerimientos con reglas de negocio complejas"); **OID** pilotea la mejora, la mide y la despliega a toda la organización |

*Similitudes (la parte que se olvida):*

1. **Las dos pueden entregar software que funciona** — el modelo dice explícitamente que las
   organizaciones nivel 1 *a menudo producen productos y servicios que funcionan*. El problema
   es que llegan tarde, caras y sin poder repetirlo.
2. **Hacen las mismas actividades técnicas.** CMMI no agrega actividades: cambia si están
   definidas, institucionalizadas, medidas y mejoradas.
3. **Ambas pueden tener gente excelente.** El nivel califica al **proceso**, no al talento.
4. **Enfrentan los mismos riesgos.** Difiere la respuesta (improvisada vs. planificada), no el
   evento.
5. **Ambas pueden fallar.** Nivel 5 no garantiza éxito ni cero defectos: garantiza que la
   desviación se detecta, se mide, se explica y alimenta una mejora.
6. **Las áreas de niveles inferiores siguen vigentes** — el nivel 5 no las reemplaza, las
   contiene.

*Conclusión:* la diferencia no está en si el proyecto sale bien, sino en **si la organización
sabe por qué salió como salió y si el próximo va a salir mejor**.

#### Dudas / pendientes

- **Nivel de OT.** El resumen dice textualmente que Formación Organizativa "es un área de
  proceso de gestión del proceso en el **nivel de madurez 4**" (`Resumen Unidad 1,2y3.md:666`).
  Eso **se contradice con la propia fuente**, que dos páginas después lista OT entre las "áreas
  de gestión de procesos **básicas**" junto a OPF y OPD (ambas nivel 3), y separa OPP y OID
  como "avanzadas". En CMMI-DEV **OT es nivel 3**. Tratarlo como nivel 3 y confirmar con la
  cátedra — si en el parcial aparece "OT nivel 4", es un error del resumen, no del modelo.
- La tabla de nivel por área para los niveles **4 y 5** (OPP/QPM y OID/CAR) la completé yo;
  no está explícita en las fuentes.
- El resumen remite a "ver ejemplo página 62 y 63 del PDF del apunte de CMMI"
  (`Resumen Unidad 1,2y3.md:509`) — falta ingerir ese PDF.

#### Fuentes

- `fuentes/ICS/Resumen Unidad 1,2y3.md` — secciones "U1 – Modelos de Calidad de Software",
  "Comprender los niveles de madurez", "Componentes del área de proceso".
- `fuentes/ICS/Preguntas de Cuestionario.md` — sección "CMMI" y las secciones por área de
  proceso.
- Pendiente: PDF del apunte de CMMI de cátedra (referenciado por número de página en ambas
  fuentes).

---

### Unidad 2 — Gestión de procesos (OPF, OPD, OT, RUP, SPEM)

#### Conceptos clave

- **Tres dimensiones críticas** de una organización: personas · métodos y procedimientos ·
  herramientas y equipamiento.
- **Activos de proceso de la organización**: descripciones de procesos y de elementos de
  proceso, descripciones de modelos de ciclo de vida, guías de adaptación, documentación y
  datos.
- **Jerarquía de definición:** conjunto de procesos estándar → **procesos estándar** →
  **elementos de proceso** (unidad fundamental), conectados según una **arquitectura de
  proceso**.
- **Las tres áreas básicas de gestión de procesos:** **OPF** (enfoque) · **OPD** (definición) ·
  **OT** (formación). Las **avanzadas**: **OPP** y **OID**.
- **RUP:** 4 fases (Inicial/Concepción, Elaboración, Construcción, Transición) × 9 disciplinas,
  con iteraciones dentro de cada fase.

#### Desarrollo

**Biblioteca de activos vs. repositorio de medición.** Son dos cosas distintas y se preguntan
por separado:

- **Biblioteca de activos de proceso** — colección de elementos que la organización mantiene
  para uso del personal y los proyectos: políticas, descripciones del proceso definido,
  procedimientos (p. ej. de estimación), planes de desarrollo y de adquisición, planes de
  aseguramiento de la calidad, material de formación, ayudas al proceso (checklists), informes
  de **lecciones aprendidas**. Da soporte al aprendizaje y la mejora al permitir compartir
  mejores prácticas.
- **Repositorio de medición de la organización** — contiene medidas de **producto y de
  proceso** relacionadas con el conjunto de procesos estándar, más la información necesaria
  para entenderlas e interpretarlas. La **definición operativa** de cada medida especifica el
  procedimiento de recolección y **en qué punto del proceso** se recogen los datos.
  Se establece en **OPD / SP 1.4**.

**Elemento de proceso — atributos críticos.** Roles · estándares aplicables · procedimientos,
métodos, herramientas y recursos · objetivos de rendimiento · **criterios de entrada** ·
entradas · medidas a recoger · puntos de verificación · salidas · interfaces · **criterios de
salida**.

**Criterios y guías de adaptación.** Describen cómo usar los activos para crear los procesos
definidos, qué requerimientos son obligatorios, qué opciones existen y con qué criterio
elegir, y qué procedimientos seguir para documentar la adaptación. Deben equilibrar
**flexibilidad** (adaptarse al contexto) con **consistencia** (que se respeten estándares,
objetivos y estrategias de la organización). Ejemplos de acciones de adaptación: modificar un
modelo de ciclo de vida, combinar elementos de modelos distintos, modificar / reemplazar /
reordenar elementos del proceso.

**Estándares del entorno de trabajo.** Permiten beneficiarse de herramientas, formación y
mantenimiento comunes, y ahorrar por volumen de compra: procedimientos de operación/
protección/seguridad del entorno, hardware y software de puesto estándar, software de
aplicación estándar y guías de adaptación, equipo de producción y calibración, y el proceso
para **solicitar y aprobar excepciones**.

---

##### OPF — Enfoque en procesos de la organización (nivel 3)

Trata la **planificación, implementación y despliegue de las mejoras** de procesos, basadas en
la comprensión de las fortalezas y debilidades actuales.

**De dónde salen las mejoras candidatas:** medición de procesos · lecciones aprendidas ·
resultados de evaluaciones de procesos · resultados de evaluación de productos · **evaluación
comparativa (benchmarking) frente a otras organizaciones** · recomendaciones de otras
iniciativas.

**Cadena de planes** (ojo con distinguirlos):

1. **Plan de mejora de procesos** — resultado de la planificación general.
2. **Plan de evaluación** — cronología, alcance, recursos, **modelo de referencia** contra el
   que se evalúa, logística.
3. **Plan de acción de procesos** — resulta de la evaluación; documenta cómo se implementarán
   las mejoras que atacan las debilidades detectadas.
4. **Plan piloto** — si la mejora se prueba primero en un grupo acotado.
5. **Plan de despliegue** — cuándo y cómo se despliega la mejora a toda la organización.

> La aceptación que se gana durante una evaluación **se deteriora rápido si no la sigue un plan
> de acción**.

**Roles en los planes de acción:** comités de dirección de gerencia (estrategia y supervisión)
· personal del grupo de procesos (facilitar y gestionar) · equipos de acción de procesos
(definir e implementar) · propietarios del proceso (gestionar el despliegue) · profesionales
(ejecutar).

##### OPD — Definición de procesos de la organización (nivel 3)

Establece y mantiene el **conjunto de activos de proceso** y los **estándares del entorno de
trabajo**. Prácticas que aparecen en los ejercicios:

- **SP 1.1** Establecer los procesos estándar
- **SP 1.2** Establecer las descripciones de los modelos de ciclo de vida
- **SP 1.3** Establecer los **criterios y guías de adaptación** ← la de las "excepciones"
- **SP 1.4** Establecer el **repositorio de medición** de la organización
- **SP 1.6** Establecer los estándares del entorno de trabajo

##### OT — Formación organizativa (nivel 3)

Desarrollar las habilidades y el conocimiento de las personas para que desempeñen sus roles
eficaz y eficientemente.

**Reparto de responsabilidades (se pregunta):** la organización trata las necesidades de
formación **comunes** a proyectos y grupos de soporte; los **proyectos y grupos de soporte**
identifican y tratan sus necesidades **específicas**. Que la organización cubra alguna
necesidad particular de un proyecto es posible, pero **debe acordarse**.

**Tipos de habilidades:** **técnicas** (usar equipo, herramientas, datos y procesos) ·
**de la organización** (comportamiento según la estructura, rol, responsabilidades, principios
y métodos) · **de contexto** (auto-gestión, comunicación, habilidades interpersonales).

**Necesidades estratégicas:** miran **2 a 5 años** hacia adelante, para introducir nuevas
tecnologías o cambios organizativos importantes.

---

##### RUP y SPEM

**SPEM (Software Process Engineering Meta-Model)** — meta-modelo para representar métodos,
ciclos de vida, roles, actividades y procesos, sin atarse a ninguna disciplina. Facilita la
comprensión y comunicación humana, la reutilización, y da soporte a la gestión y mejora de
procesos.

| Elemento SPEM | Qué es |
|---|---|
| **Delivery Process** | Un proceso completo, tan complejo como se necesite |
| **Capability Pattern** | Fragmento de proceso **reutilizable** más de una vez dentro de un delivery process |
| **Activity** | Elemento central para organizar los elementos básicos de proceso |
| **Task** | **Unidad elemental de trabajo** del modelo |

**Jerarquía RUP:** Fase → (iteraciones) → Disciplina → **Actividad** → **Tarea** (la lleva a
cabo un **rol**; granularidad de **horas a días**; puede desglosarse en pasos).

**Productos de trabajo:** **artefacto** (tangible) · **resultado** (intangible: un estado o
consecuencia) · **entregable** (empaquetado de otros productos, se entrega a una parte interna
o externa).

**Guías (tipos):** plantilla · directriz · lista de comprobación · ejemplo · concepto · guías
de herramientas · documentación · informe.

**Las 4 fases y sus objetivos:**

| Fase | Objetivos |
|---|---|
| **Inicial / Concepción** | Establecer el ámbito y los límites (visión operativa, criterios de aceptación, contenido del producto) · identificar los **casos de uso más importantes** · definir una arquitectura posible · **estimar coste global y planificación total** · estimar riesgos potenciales · preparar el entorno de soporte |
| **Elaboración** | Garantizar que arquitectura, requisitos y planes son **estables** y los riesgos están mitigados, para poder determinar coste y fin del desarrollo · tratar todos los riesgos **arquitectónicamente significativos** · establecer el entorno de soporte |
| **Construcción** | Minimizar costes optimizando recursos y evitando reconstrucciones · conseguir la calidad adecuada · conseguir versiones útiles · **completar análisis, diseño, desarrollo y prueba de toda la funcionalidad** |
| **Transición** | Prueba **beta** para validar contra las expectativas del usuario · convertir bases de datos operativas · **formación de usuarios** · realizar el despliegue · corregir defectos y mejorar rendimiento y usabilidad |

**Las 9 disciplinas y su propósito (resumido):**

| Disciplina | Propósito clave |
|---|---|
| Modelado de negocio | Entender problemas actuales e identificar mejoras; evaluar impacto del cambio; comprensión común de la organización; obtener los requisitos necesarios |
| Requisitos | Acordar con el cliente qué debe hacer **y qué NO debe hacer** el sistema; informar a los desarrolladores; definir la interfaz de usuario |
| Análisis y diseño | Transformar requisitos en diseño; evolucionar la arquitectura; ajustar al entorno de implementación |
| Implementación | Organizar el código en subsistemas; implementar los elementos de diseño; probar componentes **como unidades**; integrar |
| Prueba | Buscar y documentar defectos; validar suposiciones de diseño y requisitos; validar que funciona según lo diseñado y que los requisitos se implementaron adecuadamente |
| Despliegue | Garantizar disponibilidad para los usuarios; definir modalidades (instalación personalizada, producto comercializable, acceso por internet) |
| Configuración y gestión de cambios | Controlar los productos de trabajo; evitar confusiones por **actualización simultánea**, **notificación limitada** y **versiones múltiples** |
| Gestión de proyectos | Infraestructura para gestionar proyectos y **riesgos**; directrices de planificación, personal, ejecución y supervisión |
| Entorno | Proveer al equipo el entorno de desarrollo: **procesos y herramientas** |

**Cascada vs RUP.** Cada fase RUP se desglosa en **iteraciones**; una iteración es un bucle de
desarrollo completo que resulta en una **versión ejecutable**. La diferencia con cascada es que
el ciclo iterativo e incremental **produce resultados visibles para el usuario** desde temprano.

#### Ejercicios resueltos tipo

**1. ¿Qué área se encarga de mantener el repositorio de medidas de producto y proceso
relacionadas con el conjunto de procesos estándar? (OPF · OPD · OPP · MA)**
→ **OPD**, práctica **SP 1.4 Establecer el repositorio de medición de la organización**.
Igual respuesta para "cuando se almacenan las métricas de un proyecto en el repositorio de
mediciones de la software factory".

**2. ¿Qué área se encarga de verificar y almacenar los *productos de trabajo* a nivel
organizacional?**
→ **NINGUNA.** Trampa: "verificar", "almacenar" y "nivel organizacional" empujan hacia OPD,
pero los **productos de trabajo** son los que surgen de cada proyecto (código fuente, minutas).
Si dijera **activos**, sí sería OPD.

**3. ¿Qué área evalúa los procesos de la organización contra los de otras organizaciones?**
→ **OPF** (benchmarking está listado entre sus fuentes de mejoras candidatas).

**4. "Escribir el procedimiento por el cual deberá pedirse la excepción, con motivos
justificados, para no incluir Testing Automatizado en un proyecto particular."**
→ **OPD / SP 1.3 Establecer los criterios y las guías de adaptación.** Misma respuesta para la
variante "no incluir un Diseñador Gráfico" y para "detallar en qué proyectos puede no
realizarse el Modelado de Negocio".

**5. "Analizar tendencias en los informes de lecciones aprendidas de proyectos terminados para
detectar cambios que podrían introducirse en los procesos."**
→ **OPF.**

**6. "Revisar los informes de no conformidad generados por SQA para diseñar posibles cambios a
la plantilla de casos de uso."**
→ **OPF.** Cadena: **PPQA** emite y documenta las no conformidades → **OPF** las revisa y
propone la mejora → **OPD** materializa el cambio en el activo.

**7. "El gerente de QA impulsa una evaluación de cómo trabaja la SF para determinar puntos
sólidos y endebles, y presenta objetivos, dedicación y plazos en la reunión de gerencia para
lograr consenso."**
→ **OPF** (evaluar los procesos de la organización, comprensión de fortalezas y debilidades).

**8. "Reunión con 3 Project Managers para analizar un procedimiento definido y aún no
publicado, para encontrar y eliminar inconsistencias, redactado por otro PM."**
→ **OPD** (establecer y mantener los activos de proceso de la organización).

#### Dudas / pendientes

- El nivel de OT — ver [Unidad 1 → Dudas](#dudas--pendientes).
- El ejercicio 8 está clasificado como OPD en la fuente, pero es discutible: revisar un
  documento entre pares para encontrar defectos encaja también con **VER / revisiones entre
  pares**. La fuente resuelve por el **contenido** del artefacto (un activo organizacional, no
  un producto de trabajo de proyecto). Consultar en clase.
- Falta el detalle de **IPM** y **DAR**: aparecen en la lista de 22 áreas pero ninguna fuente
  las desarrolla.

#### Fuentes

- `fuentes/ICS/Resumen Unidad 1,2y3.md` — "U2: Gestión de procesos", "Enfoque de procesos de la
  organización (OPF)", "Formación Organizativa (OT)", "Introducción a procesos y RUP".
- `fuentes/ICS/Resumen de ISW.md` — "U2: Introducción a procesos y RUP" (elementos del proceso
  según RUP, con más detalle en fase/disciplina/guías).
- `fuentes/ICS/Preguntas de Cuestionario.md` — secciones OPD y OPF.

---

### Unidad 3 — Gestión de proyectos de software (PP, PMC y áreas de soporte)

#### Conceptos clave

- **Proyecto:** conjunto de actividades coordinadas y controladas, con **inicio y fin
  definidos**, que crea un **producto o servicio único** conforme a requisitos específicos,
  dentro de límites de tiempo, coste y recursos. **Se desarrolla en pasos** (elaboración
  gradual).
- **PP (nivel 2):** establecer y mantener planes que definan las actividades del proyecto.
- **PMC (nivel 2):** comprender el progreso para tomar **acciones correctivas** cuando el
  rendimiento se desvía del plan.
- **Desviación significativa:** aquella que, si se deja sin resolver, **impide al proyecto
  cumplir sus objetivos**.
- **APF (Análisis de Puntos Función):** medir el tamaño del software desde una perspectiva
  **funcional**, independiente de la tecnología.

#### Desarrollo

##### PP — Planificación de proyecto (nivel 2)

Se encarga de: **desarrollar el plan** · interactuar con las partes interesadas · **obtener el
compromiso con el plan** · **mantener el plan**.

La planificación arranca **con los requerimientos** que definen producto y proyecto. Incluye
estimar atributos de los productos de trabajo y las tareas, determinar recursos, elaborar
calendario, e **identificar y tratar riesgos**. El plan **necesitará corregirse** a lo largo del
proyecto: cambios en requerimientos, cambios en compromisos y estimaciones inexactas.

**Prácticas que aparecen en los ejercicios:** SP 1.1 Estimar el alcance · SP 1.3 Definir el
ciclo de vida del proyecto · SP 1.4 Determinar las estimaciones de esfuerzo y coste ·
SP 2.1 Establecer el presupuesto y el calendario · **SP 2.4 Planificar los recursos** ·
SP 2.7 Establecer el plan de proyecto · SP 3.3 Obtener el compromiso con el plan.

**Áreas relacionadas:** REQM (gestión de los requerimientos para planificar y replanificar) ·
RSKM (identificación y gestión de riesgos) · TS (transformar requerimientos en soluciones).

##### PMC — Monitorización y control del proyecto (nivel 2)

Se analiza frecuentemente el **plan documentado**. Las áreas comunican su estado en momentos
definidos y, si hay desvío, se toman acciones correctivas.

El progreso se mide comparando **calidad de los productos de trabajo, esfuerzo, coste y
calendario reales** contra el plan, en los **hitos o niveles de control** definidos en la
**WBS/EDT**.

**Acciones correctivas posibles:** **replanificación** (con o sin corrección del plan original)
· establecimiento de **nuevos acuerdos** · inclusión de **actividades adicionales de
mitigación** dentro del plan actual.

**Prácticas de los ejercicios:** SP 1.2 Monitorizar los compromisos · SP 1.5 Monitorizar la
involucración de las partes interesadas · **SP 2.1 Analizar problemas** · SP 2.3 Gestionar las
acciones correctivas.

**Áreas relacionadas:** PP y **MA**.

> **PP vs PMC — la regla de oro del parcial.** Fijarse dónde está la reunión de lanzamiento /
> de avance respecto del momento narrado:
> - Reunión **en el futuro** ("de manera de informarlo en la reunión donde se reunirá por
>   primera vez a todo el equipo") → todavía estoy planificando → **PP**.
> - Reunión **ya ocurrida** ("en la última reunión de avance…", "respecto a lo acordado en la
>   reunión de lanzamiento") → **PMC**.

##### Áreas de soporte que se preguntan junto con la gestión de proyectos

**REQM — Gestión de requerimientos (nivel 2).** Documenta los cambios a los requerimientos y su
razón, y mantiene la **trazabilidad bidireccional** entre requerimientos fuente y todos los
requerimientos de producto y de componentes.

- **SP 1.1** Obtener una comprensión de los requerimientos
- **SP 1.2** Obtener el compromiso sobre los requerimientos
- **SP 1.3** Gestionar los cambios de los requerimientos ← *mientras se evalúa el cambio*
- **SP 1.4** Mantener la trazabilidad bidireccional
- **SP 1.5** Identificar las inconsistencias entre el trabajo del proyecto y los requerimientos

> **REQM vs CM ante un cambio del cliente:** si **todavía se está chequeando cómo afecta** el
> cambio → **REQM / SP 1.3**. Si **ya se decidió aceptarlo** y ahora se tramita → **CM / SP 2.1
> Seguir las peticiones de cambio**.

**PPQA — Aseguramiento de la calidad de proceso y producto (nivel 2).** Evalúa
**objetivamente** procesos y productos de trabajo contra las descripciones de proceso,
**estándares y procedimientos** de la organización.

- La **objetividad** se logra con **independencia**. Tradicionalmente, un grupo de QA
  independiente del proyecto. En organizaciones con cultura abierta orientada a la calidad
  puede realizarse **parcial o totalmente por pares**, y la función puede embeberse en el
  proceso (suele ser lo más factible para organizaciones pequeñas).
- **Excluye** de evaluar un producto de trabajo a quien **participó en armarlo**.
- **No conformidad** = problema identificado en la evaluación que refleja falta de adherencia a
  estándares, descripciones de proceso o procedimientos.
- **Flujo de una no conformidad:** se trata **primero dentro del proyecto** y se resuelve ahí
  si es posible; si no puede resolverse, se **escala** al nivel de gerencia apropiado. Se
  **sigue hasta su resolución** y se **establecen registros**. Formas de resolverla: corregir,
  **cambiar la descripción de proceso / estándar / procedimiento incumplido**, u **obtener una
  excepción**.
- **SP 1.1** Evaluar objetivamente los procesos · **SP 1.2** Evaluar objetivamente los
  productos de trabajo y los servicios · **SP 2.1** Comunicar y asegurar la resolución de las
  no conformidades · **SP 2.2** Establecer registros.

**CM — Gestión de configuración (nivel 2).** Importa porque: asegura la correcta configuración
del software · da **capacidad de controlar los cambios** · **reduce los sobreesfuerzos por
problemas de integridad** · garantiza que todo el equipo trabaja sobre la **misma línea base**
· permite saber **qué se entregó al cliente** y minimiza el riesgo de entregar una versión
incorrecta.

- **SP 1.3** Crear o liberar **líneas base** · **SP 2.1** Seguir las peticiones de cambio ·
  **SP 2.2** Controlar los elementos de configuración · **SP 3.1** Establecer registros de
  gestión de configuración · **SP 3.2** Realizar auditorías de configuración.
- **Desde la perspectiva de testing**, CM sirve para: controlar la **versión de los casos de
  prueba**, **identificar la versión del software que se está probando**, y hacer
  **seguimiento de los cambios a los casos de prueba**. (No para *desarrollar* casos nuevos ni
  para *detectar la necesidad* de casos nuevos.)
- **Producto de trabajo vs activo** (aparece en varios ejercicios): el **producto de trabajo**
  es el resultado de una tarea del proyecto (minuta, informe de taller, código fuente, .class).
  El **activo** es un artefacto producido **para ser usado en las tareas de los proyectos**
  (plantillas). Las **herramientas** (Word 2013, Java SE 7, OpenOffice) también cuentan como
  activos, del grupo que la organización **adquiere** en lugar de desarrollar.

**MA — Medición y análisis (nivel 2).** Distinción que se pregunta:

| Tipo | Qué evalúa | Ejemplos |
|---|---|---|
| **Métricas de proyecto** | Progreso, esfuerzo, costo, planificación | % de cumplimiento de hitos de entrega · costo total de horas por iteración |
| **Métricas de producto** | Calidad o desempeño del software | Tasa de defectos encontrados en producción · cobertura de pruebas unitarias automatizadas |

Prácticas de los ejercicios: SP 1.3 Especificar los procedimientos de recogida y almacenamiento
de datos · SP 2.2 Analizar los datos de la medición · SP 2.4 Comunicar los resultados.

**RSKM — Gestión de riesgos.**

- **Orden correcto: identificar → analizar → priorizar.** (Afirmación falsa típica: "el
  análisis de riesgos es previo a su identificación").
- Los riesgos **se identifican desde la planificación** del proyecto.
- **Parámetros de riesgo (SP 1.2):** **probabilidad** de ocurrencia · **consecuencia**
  (impacto y gravedad) · **umbrales** que disparan las actividades de gestión.
- Un riesgo puede ser **aceptado** (cuando es demasiado bajo para mitigación formal o no hay
  forma viable de reducirlo — debe **documentarse la razón**) o **vigilado** (cuando hay
  límites objetivos y documentados que activan el plan de mitigación o de contingencia).
  → Por eso es **falso** que "cualquier desvío en un riesgo habilita actividades de
  tratamiento": depende del umbral.

**RD — Desarrollo de requerimientos (nivel 3).** Elicitación (obtener información completa) →
análisis (dependencias, restricciones, variaciones) → validación (confirmar con los
interesados). Prácticas citadas: SP 1.1 Obtener las necesidades · SP 1.2 Desarrollar los
requerimientos de cliente · SP 2.2 Asignar los requerimientos de componentes · SP 3.4 Analizar
los requerimientos para alcanzar el equilibrio · SP 3.5 Validar los requerimientos.

---

##### Guía práctica de gestión de proyectos (ISO 10006 / PMBOK-like)

**Gestión de proyectos:** aplicación de conocimientos, habilidades, herramientas y técnicas a
las actividades del proyecto para satisfacer sus requisitos. El tiempo/coste/esfuerzo dedicado
a gestionar **nunca es una pérdida**: es imprescindible para la calidad del resultado.

**Participantes destacados:** **patrocinador** (provee los recursos financieros) ·
**influyentes** (no están directamente relacionados pero pueden influir positiva o
negativamente).

**Los 10 grupos de procesos:**

| Grupo | Procesos |
|---|---|
| **Coordinación** | Iniciar el proyecto · Desarrollar el plan · Gestionar la ejecución · Supervisar el trabajo · Control integrado de cambios · Cerrar el proyecto |
| **Alcance** | Definir el alcance · **Definir las actividades** · Controlar y verificar el alcance |
| **Tiempo** | Establecer la secuencia de actividades · **Estimar la duración** · Desarrollar el cronograma · Controlar el cronograma |
| **Costes** | Estimar los costos · **Elaborar los presupuestos** · Controlar los costos |
| **Calidad** | Planificar la calidad · Realizar **aseguramiento** de calidad · Realizar **control** de calidad |
| **Recursos** | Planificar los recursos · Controlar los recursos |
| **Personal** | **Definir el equipo del proyecto** · Gestionar el equipo del proyecto |
| **Comunicación** | Planificar las comunicaciones · Gestionar la información y los interesados |
| **Riesgos** | Planificar la gestión · Identificar · Analizar · Planificar la respuesta · Controlar |
| **Adquisiciones** | Planificar las adquisiciones · Planificar la contratación · Solicitar respuesta a proveedores · Seleccionar proveedores · Administrar el contrato · Cerrar el contrato |

**Detalles que se preguntan:**

- **Desarrollar el cronograma** debe identificar **explícitamente el camino crítico** (el de
  mayor duración en la red de actividades), y de ahí salen las **actividades críticas** y los
  **hitos**.
- **Elaborar los presupuestos** debe incluir las **reservas para contingencias de gestión**.
- **Definir el equipo del proyecto** = determinar **roles y responsabilidades** y crear el plan
  de gestión de personal (organigramas + descripciones de responsabilidades). **No** incluye
  estimar el esfuerzo por rol ni controlar el cronograma.

##### APF — Análisis de Puntos Función

Mide el tamaño del software desde una perspectiva **funcional**, independiente de la
tecnología. Permite **comparar productividad** entre herramientas, lenguajes o entornos, y
**seguir los cambios de alcance** comparando PF entre fases del ciclo de vida.

**Etapa 1 — Identificar y clasificar componentes.** Primero se establece el **límite del
sistema** (qué queda adentro y qué es externo). Luego, cinco tipos:

| Componente | Definición |
|---|---|
| **Entradas** | Datos que cruzan el límite **hacia adentro** |
| **Salidas** | Datos que cruzan el límite **hacia afuera** |
| **Consultas** | Combinación de entrada + salida para obtener datos |
| **Ficheros lógicos internos (FLI)** | Datos que residen **dentro** de la aplicación y son actualizados por las entradas |
| **Ficheros de interfaz externos (FIE)** | Datos que residen **fuera** y son mantenidos por **otra** aplicación |

**Etapa 2 — Complejidad y ponderación.** A cada componente se le asigna complejidad baja/media/
alta según cantidad de datos y ficheros involucrados, y se multiplica:

| Componente | Baja | Media | Alta |
|---|:---:|:---:|:---:|
| Entradas | ×3 | ×4 | ×6 |
| Salidas | ×4 | ×5 | ×7 |
| Consultas | ×3 | ×4 | ×6 |
| Ficheros internos (FLI) | ×7 | ×10 | ×15 |
| Ficheros externos (FIE) | ×5 | ×7 | ×10 |

La suma da los **PFD (puntos función sin ajustar)**.

**Factor de ajuste.** Se califican **14 características del entorno** de 0 a 5
(0 ninguna · 1 insignificante · 2 moderada · 3 media · 4 significativa · 5 fuerte):

1. Comunicaciones de datos · 2. Datos o procesamiento distribuidos · 3. Objetivos de
rendimiento · 4. Configuración para utilización masiva · 5. Tasa de transacción · 6. Entrada de
datos on-line · 7. Eficiencia para el usuario · 8. Actualización on-line · 9. Procesamiento
complejo · 10. Reutilización · 11. Facilidad de instalación · 12. Facilidad de operación ·
13. Puestos múltiples · 14. Facilidad de cambio.

La suma de los 14 valores es el **TDI** (grado de influencia total, 0–70), y:

```
Factor de ajuste = 0,65 + (TDI / 100)
PF ajustados     = PFD × Factor de ajuste
```

Con TDI entre 0 y 70, el factor va de **0,65 a 1,35**: el ajuste puede mover el tamaño ±35 %.

**Glosario APF:** **PFD** sin ajustar · **PFM** puntos función de la mejora · **PFDM** sin
ajustar de la mejora · **PFP** puntos función de las pruebas · **fichero referenciado** = un
FLI leído o modificado por una transacción, o un FIE leído por una transacción · **factor de
impacto** = grado de cambio en una función.

#### Ejercicios resueltos tipo

**1. "El cliente informa que el server llegará con 10 días de retraso respecto a lo acordado en
la **reunión de lanzamiento**. El equipo está determinando si tomar medidas para compensarlo."**
→ **PMC / SP 2.1 Analizar problemas.** La reunión de lanzamiento **ya ocurrió** → estoy
monitorizando. "Recoger y analizar los problemas y determinar las acciones correctivas".

**2. Mismo enunciado, pero: "…de manera de informarlo en la reunión donde se reunirá a todo el
equipo por primera vez para establecer compromiso sobre roles, objetivos y plazos."**
→ **PP / SP 2.4 Planificar los recursos del proyecto.** La reunión está **en el futuro** →
todavía estoy planificando; estoy retocando el Gantt por el retraso.

**3. "El responsable de TI informa que hasta el 3er mes no estará el equipo; el PM está
modificando las fechas de capacitación e implementación, y lo documenta en el producto que se
presentará la semana que viene en la reunión donde se informará al equipo las actividades."**
→ **PP / SP 2.4 Planificar los recursos.** Mismo criterio: la reunión es **futura**.

**4. "Hay retraso en el relevamiento porque el usuario clave desconoce el proceso; se está
reuniendo con el usuario clave y el jefe de sector para confirmar el reemplazo y que el jefe
participe de las reuniones semanales."**
→ **PMC.** Se apoya en **GP 2.7 Identificar e involucrar a las partes interesadas relevantes**
y **SP 1.5 Monitorizar la involucración de las partes interesadas**.

**5. "El cliente pide una nueva variante de descuento no acordada. En este momento se está
chequeando con el contador cómo afecta al esquema impositivo."**
→ **REQM / SP 1.3 Gestionar los cambios de los requerimientos** (todavía se evalúa el impacto).

**6. Mismo caso, pero "ya se ha decidido aceptar esta variante; ahora se chequean las
modificaciones a hacer en los C.U."**
→ **CM / SP 2.1 Seguir las peticiones de cambio.**

**7. "Reunión con el Sponsor para acordar posponer 3 semanas la implementación, para incorporar
los cambios del Gerente de Ventas; sin su aprobación el proyecto sigue como estaba."**
→ **REQM / SP 1.2 Obtener el compromiso sobre los requerimientos.**

**8. "Personal de la SF **externo al equipo de proyecto** controla si los C.U. cumplen con las
directrices de escritura de C.U. **de la software factory**."**
→ **PPQA / SP 1.2 Evaluar objetivamente los productos de trabajo y los servicios.** Dos señales:
externo al proyecto (independencia) + estándar **organizacional**.

**9. "Controlar si los nombres de los archivos de los artefactos cumplen las reglas de nombres
definidas **en el proyecto**."**
→ **CM / SP 2.2 Controlar los elementos de configuración.** La nomenclatura es **del proyecto**,
no un estándar organizacional → no es PPQA.

**10. "A pesar de tres informes observando que se introdujeron cambios sin ejecutar el workflow
de REQM, la situación no cambió, y se eleva un informe al Gerente General."**
→ **PPQA / SP 2.1 Comunicar y asegurar la resolución de las no conformidades** (mecanismo de
**escalado**).

**11. "Establecer que un conjunto de artefactos, luego de revisados y acordados formalmente,
constituyen el basamento sobre el cual se realizará el resto del desarrollo."**
→ **CM / SP 1.3 Crear o liberar líneas base.**

**12. "Cada vez que se genera una compilación se genera un documento con las modificaciones
respecto de la anterior."**
→ **CM / SP 3.1 Establecer registros de gestión de configuración.**

**13. Riesgos — verdadero o falso.**

| Afirmación | |
|---|---|
| La actividad de hacer análisis de riesgos es previa a su identificación | **Falso** — primero identificar, después analizar, después priorizar |
| La probabilidad de un riesgo es un parámetro de riesgo | **Verdadero** (SP 1.2) |
| Cualquier desvío en un riesgo habilita actividades de tratamiento | **Falso** — hay riesgos aceptados y vigilados; se dispara al superar el **umbral** |
| Los riesgos se identifican desde la planificación del proyecto | **Verdadero** |

#### Dudas / pendientes

- El resumen corta la fórmula del factor de ajuste como `65+TDI100`
  (`Resumen Unidad 1,2y3.md:1212`), sin decimales ni división visible — es un artefacto de la
  conversión. La reconstruí como **0,65 + TDI/100**, que es la fórmula estándar de IFPUG y la
  única que cierra con la escala 0–5 × 14 ítems. **Verificar contra el apunte original.**
- La tabla de asignación de puntos función está en la fuente **sin los criterios** para decidir
  si un componente es de complejidad baja, media o alta (dependen de la cantidad de tipos de
  dato y de ficheros referenciados). Falta esa tabla.
- Falta desarrollar **SAM** (gestión de acuerdos con proveedores, nivel 2): no aparece en
  ninguna fuente más allá del listado de las 22 áreas.
- Las secciones "Proyecto - EDT - Esfuerzo - Recursos - Mantenimiento" y "BP" del cuestionario
  están **vacías** — quedaron sin completar por quien armó el archivo.

#### Fuentes

- `fuentes/ICS/Resumen Unidad 1,2y3.md` — "U3 – Gestión de Proyectos de Software": Áreas CMMi PP
  y PMC, Guía práctica de gestión de proyectos, Guías avanzadas de puntos de función.
- `fuentes/ICS/Preguntas de Cuestionario.md` — secciones PMC, REQM, PP, PPQA, CM, RSKM, MA, RD.
- Referenciados pero no ingeridos: `IS-TEOR-PP01_Guia_practica_de_Gestion_de_Proyectos_v1_01.pdf`,
  `IS-TEOR-PP02_Guia_avanzada_de_Gestion_de_Proyectos_v1_01.pdf`,
  `U6-IS-TEOR-CM02_Guia_practica_Gestion_Configuracion_v1_01.pdf`.

---

### Unidad 4 — Gestión efectiva de la calidad del producto (economía de las pruebas)

> ⚠️ **Numeración inferida.** Ninguna fuente rotula este bloque con un número de unidad.
> Ver [Dudas / pendientes](#dudas--pendientes-3).

#### Conceptos clave

- **Dos tercios de los proyectos** fallan o terminan con funcionalidades reducidas. Las fases
  más críticas son **prueba** y **mantenimiento**.
- **Corregir un defecto en mantenimiento cuesta 100 veces más que en ingeniería de
  requisitos.**
- **Cero defectos es inviable.** El objetivo no es eliminar todos los defectos sino
  **equilibrar cuánto se prueba contra cuánto se invierte**, decidiendo con **análisis de
  riesgo**.
- **KPI:** herramienta de gestión del rendimiento que visualiza indicadores empresariales,
  típicamente con **códigos semafóricos** que establecen alertas.

#### Desarrollo

**Análisis de riesgo para decidir cuánto probar.** Para cada **función de negocio** se evalúan
dos dimensiones:

| Dimensión | Criterios |
|---|---|
| **Impacto** (si falla) | Tipo de proceso · implicaciones del negocio · frecuencia de uso · número de clientes afectados |
| **Probabilidad** (de que falle) | Tasa de cambio · madurez del software · tasa de defectos |

Impacto × probabilidad = **riesgo** (alto / medio / bajo), y de ahí sale el procedimiento:

| Riesgo | Procedimiento de prueba |
|---|---|
| **Alto** | Pruebas sistemáticas con **particiones de equivalencia con combinaciones** + análisis de **causa raíz** |
| **Medio** | Pruebas sistemáticas con o sin particiones de equivalencia, **sin combinaciones**, + análisis causal |
| **Bajo** | Pruebas **ad-hoc** |

Complementariamente se analiza la **complejidad** de cada función de negocio como estimación
del esfuerzo de probarla (criterios: nº de objetos afectados, nº de ventanas afectadas).

**Factores que afectan al esfuerzo de pruebas:**

- Existencia de buena documentación del proyecto
- Tipo de características **no funcionales** a probar
- **Tamaño** del producto
- Disponibilidad de herramientas y entornos de pruebas
- **Madurez del proceso** y protocolos establecidos en la empresa
- **Presión del tiempo**
- Factores humanos: disponibilidad de recursos, conocimientos y **actitud**

**Automatización vs manual.** La automatización aumenta la calidad a menor costo, pero **sólo
para determinados proyectos**: implica inversión inicial y conocimientos adicionales. Se
justifica cuando las pruebas se ejecutan con frecuencia y el costo de implementarlas puede
recuperarse.

**Definición de la estrategia de test — pasos:**

1. Evaluar la **complejidad** de los requisitos de las pruebas.
2. Ver la **viabilidad** de las estrategias.
3. Calcular **coste/esfuerzo** de cada aproximación: % manual vs automatizado, % in-house vs
   outsourced.
4. Considerar recursos y tiempo disponibles.
5. Definir objetivos de **ROI** a medio/largo plazo y la inversión óptima en automatización
   para alcanzarlo.
6. **Priorizar** las pruebas de requisitos según el **análisis de riesgos**.
7. Criterios de priorización para automatizar: pruebas con **menor nº de ciclos para el ROI** ·
   pruebas con **mayor riesgo** · pruebas con **menor complejidad**.

**KPIs.** Permiten monitorizar, controlar y gestionar los procesos de la organización mediante
alertas semafóricas, dando una visión completa del rendimiento de la compañía.

#### Ejercicios resueltos tipo

*(No hay ejercicios de esta unidad en el cuestionario. Los que más se le acercan son los de
métricas de proyecto vs producto — ver [Unidad 3 → MA](#unidad-3--gestión-de-proyectos-de-software-pp-pmc-y-áreas-de-soporte).)*

#### Dudas / pendientes

- **Numeración de la unidad.** El bloque aparece en `Resumen de ISW.md` bajo el título
  "Gestión efectiva calidad producto", después de "U2: Introducción a procesos y RUP" y sin
  rótulo de unidad. Puede ser U4, o parte de U5, o un tema transversal del programa. **Definir
  contra el programa de cátedra** — si resulta que pertenece a U5, hay que fusionarlo con la
  sección "Estrategia de pruebas" de esa unidad, que trata lo mismo desde otro ángulo.
- La fuente referencia una imagen para el balance automatización/manual
  (`Resumen de ISW.md:143`) que no está transcrita.
- La sección de **KPIs** está apenas esbozada: dos párrafos, sin ejemplos de KPIs concretos de
  calidad de software. Falta material.
- El dato "el coste de corregir en mantenimiento es 100× el de requisitos" viene sin cita de
  origen. Si se pide fundamentarlo, la referencia clásica es Boehm — **conocimiento mío, no de
  las fuentes**.

#### Fuentes

- `fuentes/ICS/Resumen de ISW.md` — "Gestión efectiva calidad producto", "El costo de la
  prueba", "Factores que afectan al esfuerzo de pruebas", "Automatización y Manual",
  "Estrategias de test", "KPIs".

---

### Unidad 5 — Verificación y Validación

#### Conceptos clave

- **Verificación (VER, nivel 3):** asegurar que los **productos de trabajo seleccionados
  cumplen sus requerimientos especificados**. Cuestión **interna**.
  → **¿Estoy construyendo *correctamente* el producto?** — "se construye correctamente".
- **Validación (VAL, nivel 3):** demostrar que un **producto o componente se ajusta a su uso
  previsto cuando se sitúa en su entorno previsto**. Involucra al **cliente/usuario**.
  → **¿Estoy construyendo el producto *correcto*?** — "se construye la cosa correcta".
- Ambas son **procesos de evaluación de productos**, se ejecutan **frecuentemente de forma
  concurrente** y pueden compartir parte del entorno.
- **Grado de confianza:** V&V no busca ausencia total de defectos, sino que el software sea
  **suficientemente bueno para su uso previsto**.
- **Técnicas estáticas** (sin ejecutar código, buscan **defectos**) vs **dinámicas** (ejecutan
  el código, buscan **fallos**). Son **complementarias**.
- *"Las pruebas sólo pueden demostrar la presencia de errores, no su ausencia."*

#### Desarrollo

##### VER vs VAL — metas y prácticas específicas

| **Verificación (VER)** | **Validación (VAL)** |
|---|---|
| **SG1 Preparar la verificación** — SP 1.1 Seleccionar los productos de trabajo a verificar · SP 1.2 Establecer el entorno · SP 1.3 Establecer procedimientos y criterios | **SG1 Preparar la validación** — SP 1.1 Seleccionar los productos a validar · SP 1.2 Establecer el entorno · SP 1.3 Establecer procedimientos y criterios |
| **SG2 Realizar revisiones entre pares** — SP 2.1 Preparar · SP 2.2 Llevar a cabo · SP 2.3 Analizar los datos | *(VAL no tiene revisiones entre pares)* |
| **SG3 Verificar los productos de trabajo seleccionados** — SP 3.1 Realizar la verificación · SP 3.2 Analizar los resultados | **SG2 Validar el producto o los componentes** — SP 2.1 Realizar la validación · SP 2.2 Analizar los resultados |

> ⚠️ **"Revisiones entre pares" existe SÓLO en VER.** Si un enunciado describe pares y la opción
> ofrecida dice `VAL/SP 2.1 Preparar las revisiones entre pares`, la respuesta es **NINGUNA**.

**Qué se valida:** productos de trabajo (requerimientos, diseños, prototipos) y el producto y
sus componentes. Se hace **temprana e incrementalmente**, no al final.

**Cómo se valida:** el entorno debe **representar el entorno previsto**; se puede usar el
entorno completo o sólo una parte. Métodos: discusión con usuarios (tal vez en revisión
formal), demostraciones de prototipos, demostraciones funcionales, **pilotos** de materiales de
formación, pruebas por los usuarios finales, análisis (simulaciones, modelado).

**Qué es validable:** requerimientos y diseños · producto y componentes · **interfaces de
usuario** · **manuales de usuario** · **materiales de formación** · documentación del proceso.

**La verificación es incremental:** empieza por la **verificación de los requerimientos**,
sigue con los productos de trabajo a medida que evolucionan, y culmina en la verificación del
**producto finalizado**.

**Áreas relacionadas:** VAL ↔ RD (validación de requerimientos), TS (acción correctiva cuando
el problema afecta al diseño), PMC. VER ↔ VAL, RD, REQM.

##### Grados de confianza

El nivel de confianza requerido depende de:

- **Propósito/criticidad del sistema:** crítico → confianza alta; prototipo → confianza menor.
- **Expectativas del usuario:** la tolerancia a fallos está decreciendo.
- **Entorno de mercado:** con **pocos competidores** se puede lanzar antes de estar
  completamente probado, para llegar primero; con **precio bajo**, los clientes toleran más
  defectos.

V&V son **procesos costosos** — en ciertos sistemas superan **la mitad del presupuesto total**
de desarrollo. Por eso hay que planificarlos **desde etapas tempranas**.

##### Ciclos de vida y su relación con V&V

**Cascada.** Cada etapa espera a que termine la anterior. **Desventaja crítica:** las pruebas
van al final, así que los defectos se detectan cerca de la implementación → **costo de
corrección muy elevado**. Es el que **menos colabora cuando los requerimientos son inestables**:
una vez cerrado el análisis, los requisitos no se vuelven a tocar hasta terminar las pruebas.

**Modelo en V.** Nace como respuesta a esa limitación: integra V&V **desde las primeras fases,
en paralelo al desarrollo**. Los técnicos de prueba trabajan junto a desarrolladores y analistas
de negocio, usando los productos de cada etapa como base de un nivel de prueba.

- **Validación temprana:** revisión de los requisitos de usuario.
- **Validación tardía:** pruebas de aceptación de usuario.
- Correspondencias: pruebas de **integración** ↔ diseño · pruebas de **sistema y rendimiento**
  ↔ especificación de requisitos software · pruebas de **aceptación** ↔ requisitos de usuario.
- Las **pruebas unitarias** se hacen a medida que se genera el código.
- La **verificación encaja en todas las fases**, porque en todas hay que comprobar que las
  tareas se desarrollan como se planificaron.

**Verificaciones sobre el documento de especificación de requisitos** (bloque de examen):

| Verificación | Qué comprueba |
|---|---|
| **Validez** | Que las funciones pedidas sean realmente las necesarias (el análisis puede identificar funciones adicionales o distintas) |
| **Consistencia** | Que los requisitos **no se contradigan** entre sí |
| **Completitud** | Que estén **todas** las funciones y restricciones propuestas |
| **Realismo** | Que se puedan implementar, considerando **presupuesto y planificación** |
| **Verificabilidad** | Que se pueda construir un conjunto de pruebas que demuestre que cada requisito se cumple. Reduce discusiones cliente–contratista |

**Incremental.** Secuencias lineales escalonadas; cada secuencia produce un **incremento**. El
primer incremento suele ser el **producto esencial** (requisitos básicos). Cada incremento es
una mini-cascada completa: **análisis, diseño, desarrollo y pruebas**. Las funcionalidades se
prueban a medida que se agregan, sin esperar la implementación completa.

**Espiral.** Las características **evolucionan** en el tiempo. Útil cuando el equipo **no puede
especificar por adelantado** las características del sistema. Se construye un prototipo inicial
y se prueba para identificar características; prueba, rediseño y prototipado son **continuos**
hasta terminar el conjunto de características. Riesgo: **entregar como producto final un
prototipo que no está listo**, típicamente por presión de tiempo.

**Prototipado.** Útil cuando el cliente define **objetivos generales** pero **no identifica los
requisitos detallados** de entrada, proceso o salida. Paradigma: recolección de requisitos →
**diseño rápido** (centrado en lo visible para el usuario) → construcción del prototipo →
evaluación por el cliente → se refinan los requisitos e itera.

##### Actividades de V&V — pruebas

**Caso de prueba:** conjunto de **entradas, condiciones de ejecución y resultados esperados**,
desarrollado para un objetivo o condición particular. Requiere definir **precondiciones y
postcondiciones**, identificar valores de entrada, y conocer el comportamiento esperado.

**Nunca se prueba en producción.** El entorno de pruebas debe estar **físicamente separado** y
recrear las condiciones de producción.

**Sistema de pruebas — 4 componentes:** **equipo** de pruebas (ingenieros, técnicos,
responsable) · **recursos** (casos, datos, herramientas) · **procesos** (formales/informales,
documentados o no) · **entorno** (hardware, software, red, oficina y laboratorio).

Se mide su calidad con **ISO 9126**: debe ser funcional (cubrir los riesgos críticos), fiable
(mismos resultados ante la misma prueba), robusto, flexible (ejecutar en distinto orden), útil
(curva de aprendizaje corta), consistente en el registro de resultados si es automatizado,
portable, eficiente y mantenible.

##### Estrategias de prueba

| Estrategia | Núcleo | Variantes |
|---|---|---|
| **Analítica** | Técnicas analíticas en requisitos y diseño; lo analizado se llama **base de las pruebas**. Minuciosas y buenas para mitigar riesgos, pero **caras en tiempo** | Orientada a objetos (requiere buena documentación) · **Basada en riesgos** |
| **Basada en el modelo** | Construir modelos de cómo debería comportarse el sistema | Basada en escenario · basada en el dominio · basada en un modelo |
| **Metódica** | Enfoque ordenado y predecible; usa **estándares como objetivos**. Rápida en sistemas estables o similares a otros ya probados | Basada en el aprendizaje (checklists de errores previos) · basada en funciones o estados · basada en la calidad (ISO 9126) |
| **Proceso/estándar conformista** | Sigue un estándar externo conocido, con poca personalización. Hace el proceso **transparente** para gente ajena a las pruebas | — |
| **Dinámica** | Minimiza la planificación previa; enfatiza las **últimas etapas**. Valora flexibilidad y facilidad de encontrar errores | Intuitiva · **exploratoria** |
| **Filosófica** | Parte de una creencia sobre las pruebas | **Exhaustiva** (buscar todos los errores) · **shotgun** (no se puede probar todo, se aceptan errores) · **guiada externamente** (confía en que usuarios/soporte los encuentren) |

**Regresión** — chequea la mala conducta de algo previamente correcto:

- **Local:** al cambiar o arreglar algo, **se crea un error nuevo**.
- **De exposición:** el cambio **revela errores que ya existían**.
- **Remota:** el cambio en un área **rompe otra área** del sistema.
- Estrategia más simple: **fuerza bruta** (repetir todas las pruebas) → por eso conviene
  automatizar.

**Automatización.** Ventajas: reduce drásticamente el esfuerzo de regresión, permite validar en
ciclos de cambio con poco tiempo, asegura **consistencia y cobertura**. Desventaja: **costo
alto**. Para decidir qué automatizar: **trazabilidad** (relacionar pruebas con requisitos,
diseño o riesgos) · **análisis de cambios** · **análisis de riesgos de calidad**.

##### Niveles de pruebas

| Nivel | Qué prueba | Quién y cómo |
|---|---|---|
| **Unitarias** | Cada módulo/componente aislado, antes de integrar | El **propio desarrollador**, junto con el diseño y construcción. Usa **stubs y drivers** para aislar. Se recomienda **automatizar** |
| **Integración** | Interacción entre módulos ya integrados; defectos de **interconexión** | Referencia: documentos de análisis y sobre todo **diseño** |
| **Sistema** | Comportamiento **global** contra la especificación funcional (requisitos funcionales **y no funcionales**) | Equipo **independiente** de técnicos especializados, incluso **externo** o de analistas de negocio. Usa técnicas de **caja negra**; requiere entorno controlado lo más similar a producción |
| **Aceptación** | Que el producto satisface las **necesidades del usuario** | Lo realiza **un usuario o cliente**; requiere entorno que represente producción |

> **Ningún nivel reemplaza a otro.** Que haya pruebas de integración no quita que se hagan las
> unitarias, y viceversa.

**Estrategias de integración:**

| Estrategia | Cómo | Pros / contras |
|---|---|---|
| **Big-bang** | Todo se ensambla de una y se prueba | No requiere simular nada, pero consume mucho tiempo rastreando causas y **descubre problemas al final** → más caro |
| **Bottom-up** | Desde los módulos inferiores hacia arriba | Requiere **test-drivers** en cada nivel · **no encuentra problemas de diseño hasta muy avanzado** · apropiado para **orientado a objetos** y necesario para componentes críticos |
| **Top-down** | Desde los componentes superiores hacia abajo | Requiere **stubs** que simulen los módulos inferiores · **descubre rápidamente errores de arquitectura** · se usa junto al desarrollo top-down |

**Tipos de pruebas de sistema:** funcionales · instalación, configuración y **carga inicial de
datos** · usabilidad · migración de datos · prestaciones · seguridad.
En esta fase **también se elaboran los manuales de usuario y de administración**.

**Pruebas de aceptación — modalidades:**

| Modalidad | Quién | Dónde |
|---|---|---|
| **Alfa** | Conjunto **acotado** de clientes preseleccionados | Entorno controlado (p. ej. oficinas de la empresa) |
| **Beta** | Conjunto **más amplio** de clientes | En o fuera de las instalaciones del cliente, con algún control |
| **Piloto** | Conjunto **reducido de departamentos** del cliente | Instalaciones del cliente, en **ambiente de producción** |

**Clasificación de las pruebas (según presentación):**

- **Por quién prueba:** internas (equipo de desarrollo) · externas (cliente, con o sin ayuda del
  equipo: alfa, beta, piloto).
- **Por qué se prueba:** unitarias · integración · sistema · aceptación.
- **Por cómo se diseñan:** **caja negra** (funcionales y no funcionales) · **caja blanca**
  (estructurales).

**Tipos de prueba vs niveles de prueba** — distinción que se pregunta: el **tipo** define el
**objetivo** (seguridad, rendimiento, usabilidad); el **nivel** define **cuándo y sobre qué
parte** se aplica.

**Pruebas de prestaciones:**

| Prueba | Objetivo |
|---|---|
| **Carga** | Validar los requisitos de prestaciones definidos (p. ej. tiempo máximo de respuesta), con escenarios realistas |
| **Capacidad** | Encontrar el **punto umbral** a partir del cual las prestaciones se degradan, incrementando la carga hasta la saturación |
| **Estrés** | Comportamiento en **sobrecarga**, excediendo los límites de procesamiento y almacenamiento. Foco en la **integridad** |
| **Escalabilidad** | Capacidad de **absorber requisitos mayores** de prestaciones |
| **Estabilidad** | Comportamiento **en el tiempo** bajo carga normal: detectar mala gestión y liberación de recursos |

**Pruebas de usabilidad.** Miden cuán fácil, cómoda e intuitivamente interactúan los usuarios.
Se prueba: navegación y secuencia de pasos · presencia y organización de la información ·
flexibilidad en las operaciones · etiquetas y mensajes apropiados · información de estado.

**Regresión vs confirmación.** La **confirmación** verifica que **un defecto corregido
realmente se solucionó** (misma prueba, mismas condiciones, mismos datos). La **regresión**
verifica que **el arreglo no rompió otra cosa**. Se usan juntas.

**Buenas prácticas en pruebas:**

- Proceso **continuo e iterativo** a lo largo de todo el ciclo de vida.
- Las de sistema, en un entorno **lo más parecido a producción**.
- Proceso ordenado, metódico, repetitivo y sistemático: previsto, planificado, gestionado y
  documentado.
- Cada caso de prueba **codificado y asociado al menos a un requisito** → **trazabilidad**.
- Las pruebas, en especial las de regresión, **repetibles y automatizables**.
- El entorno debe **controlar la promoción de nuevas versiones** mientras se prueba.
- **Los desarrolladores no deben probar su propio código.**
- Los elementos de prueba construidos van **al repositorio de gestión de configuración**.

##### Técnicas dinámicas

**Basadas en la especificación (caja negra).**

- **Particionamiento de equivalencia.** Agrupa condiciones de entrada lógicamente iguales: si
  falla/funciona para una, se asume igual para todas las de la partición. Directrices:
  - **Rango** ("10 a 100") → 1 partición válida + **2 inválidas** (menor y mayor).
  - **Conjunto de valores discretos** ("ROJO, BLANCO, NEGRO") → 1 válida + 1 inválida (todos
    los demás).
  - **Condición de obligación** ("letras mayúsculas") → 1 válida + 1 inválida.
  - También hay **particiones de salida** (agrupar por resultado: p. ej. las tres tasas de
    interés 0,5 % / 1 % / 1,5 %).
- **Análisis de valor de frontera.** Prueba los **valores extremos** de las particiones, porque
  ahí se agrupan los errores. Rango 10–100 → probar **9, 10, 100 y 101**. Conjuntos ordenados →
  primer y último elemento. Valores especiales: en minutos siempre probar **0 y 59**, y en
  fechas incluir meses, **años bisiestos y no bisiestos**.
- **Tablas de decisión.** Para cuando **múltiples combinaciones de entradas** generan
  resultados distintos. Se centra en la **lógica y las reglas de negocio**: filas de condición +
  filas de acción; **cada columna es una regla de negocio**.
- **Transición de estados.** Para sistemas modelables como **máquina de estados finitos**,
  donde la salida ante la misma entrada depende del estado anterior. Una prueba completa debe
  incluir **transiciones no válidas** (intentos fallidos, timeouts) y **eventos no
  especificados** (cancelar). Es floja para identificar pruebas negativas.
- **Pruebas de casos de uso.** Ejercitan el sistema de punta a punta. Proceso: definir **flujo
  básico** (camino feliz) y **flujos alternativos** → **derivar escenarios** (secuencias que
  recorren el básico y se desvían por alternativos) → **un caso de prueba por escenario**, con
  ID, condiciones de entrada y resultado esperado → sumar las **especificaciones
  complementarias** (rendimiento/fiabilidad, acceso/seguridad, configuración, instalación).

**Basadas en la estructura (caja blanca).** Parten del **código fuente** y de tres estructuras:
**secuencia**, **selección**, **iteración**.

| Técnica | Objetivo |
|---|---|
| **Pruebas de sentencia** | Ejecutar cada sentencia ejecutable al menos una vez (cobertura 100 %) |
| **Pruebas de decisión** | Evaluar cada decisión (IF-THEN-ELSE, DO-WHILE) en **verdadero y falso** |
| **Pruebas de caminos** | Probar cada camino de ejecución independiente. **No** prueba todas las combinaciones: con bucles son infinitas |

> Un defecto puede manifestarse **aunque todas las sentencias se hayan ejecutado una vez**,
> porque el problema aparece al **combinarse ciertos caminos**.

**Basadas en la experiencia.** Se usan cuando **no hay especificación adecuada** o **no hay
tiempo**:

- **Adivinación de errores (error guessing)** — complementa técnicas formales; depende de la
  habilidad, intuición y experiencia del técnico.
- **Pruebas exploratorias** — explorar el software para entender qué hace, qué no hace y dónde
  está débil, aprendiendo y diseñando pruebas mientras se ejecutan.

##### Técnicas estáticas

**Revisiones.** Primera forma de prueba aplicable en el ciclo de vida; detectan defectos
**antes de que lleguen al código ejecutable**. Vinculadas principalmente a **verificación**.
Se aplican a requisitos (claridad, ausencia de contradicciones), diseños (alineación con
requisitos) y código (buenas prácticas).

**Beneficios:** mejoran la calidad y comprensión de los entregables · validan que soportan la
solución final · gestionan expectativas del negocio · identifican tareas de alto riesgo ·
forman al equipo · detectan problemas temprano. Al reducir los errores que llegan a pruebas,
**acortan los periodos de prueba y bajan sus costes**. Las organizaciones tienden a
**sobreestimar su costo y subestimar sus beneficios**, y por eso a veces no las implementan.

**Formalidad:**

| Informales | Formales |
|---|---|
| No hay proceso definido · no hay roles · usualmente no planeadas. Cualquier interacción entre pares ("¿te parece bien este código?") | Objetivos definidos · proceso documentado · roles definidos y personas entrenadas · checklists, reglas y métodos · **reporte de resultados** · recolección de datos para control del proceso |

La formalidad importa porque deja **trazabilidad documentada** de acciones y decisiones,
demostrando que los procedimientos se cumplieron.

**Proceso básico (común a todas):** identificar los entregables a revisar → armar la lista de
participantes → los revisores **estudian** el documento → identifican problemas y los
**comunican al autor** (verbal o por documento) → el autor **responde y actualiza**.

**Tipos de revisión:**

| Tipo | Quién dirige | Foco | Formalidad |
|---|---|---|---|
| **Revisión informal** | — | Encontrar defectos; documentar es **opcional** | Mínima |
| **Walkthrough** | **El propio autor** | Entendimiento común, evaluar contenidos, discutir validez de soluciones y alternativas | Media; reuniones previas **opcionales** |
| **Revisión técnica** | Moderador capacitado o experto técnico | **Consenso técnico**, no búsqueda de defectos. Revisores **expertos** (arquitectos, usuarios clave) | Variable; checklists opcionales |
| **Revisión entre pares (peer review)** | Colegas del mismo proyecto | Identificar y eliminar defectos **temprano**, de forma incremental | Media |
| **Inspección** | **Moderador formado, NO el autor** | **Registrar defectos** eficientemente (las discusiones se posponen); seguimiento formal con **criterios de salida** | **Máxima** |

**Guías para revisiones entre pares:** crear un **entorno seguro** (no amenazante) · capacitar
al personal en sus roles · **documentar los defectos** (ubicación, descripción, comentarios,
acciones) · **enfocarse en el producto, no en la persona** · comunicar los defectos al
desarrollador principal · **incluirlas en la planificación del proyecto** para que tengan tiempo
asignado. Se aplican a artefactos de gestión del proyecto (planes), de gestión del proceso
(descripciones de procesos) y de soporte (documentación, material de formación).

**Los 5 roles de una revisión:**

1. **Moderador** — dirige el proceso; con el autor determina el tipo de revisión y la
   composición del equipo; hace validación de entrada y seguimiento para controlar la calidad
   del proceso de revisión.
2. **Autor** — creó el documento; su objetivo es mejorar su calidad y su propia habilidad de
   escritura.
3. **Documentador** — anota cada defecto y sugerencia (en la práctica, suele hacerlo el autor).
4. **Revisor** (validador / inspector) — valida el material buscando defectos **antes** de la
   reunión.
5. **Supervisor** — decide **destinar tiempo del proyecto** a las revisiones, determina si se
   cumplieron los objetivos, y atiende las solicitudes de formación de los participantes.

**Análisis estático.** Busca defectos **sin ejecutar**, pero **una vez escrito el código**, en
el código fuente y en los modelos. Usa **analizadores estáticos**.

- **Ventajas:** detección temprana · mejora la **mantenibilidad** (identifica código complejo) ·
  **prevención** (ataca la causa raíz) · encuentra **inconsistencias en los modelos**, cosa que
  las pruebas dinámicas no pueden.
- **Defectos que detecta:** variables **no inicializadas** · variables **no utilizadas** ·
  inconsistencias entre módulos (uno pide más datos de los que otro provee) · **código
  inalcanzable** · vulnerabilidades de seguridad · violaciones de estándares de programación.
- **Métricas de código:** **complejidad ciclomática** (= nº de sentencias de decisión binarias
  + 1; sirve para **estimar cuántas pruebas** necesita un componente) · frecuencia de
  comentarios · profundidad de anidamiento.
- Sin herramientas, **aplicar un estándar de codificación en una organización probablemente
  falle**.

#### Ejercicios resueltos tipo

**1. "La actividad de Validación intenta asegurar que…"**
→ *El producto o componente se ajusta a su uso previsto cuando se sitúa en su entorno previsto*
· *El software hace lo que el usuario requiere* · *Estamos construyendo el producto correcto*.

**2. "La actividad de Verificación intenta asegurar que…"**
→ *Los productos de trabajo seleccionados cumplen sus requerimientos especificados* · *El
software se ajusta a su especificación* · *Estamos construyendo el producto correctamente*.

**3. Clasificar artefactos en VER / VAL / Ninguna:**

| Artefacto | Área | Por qué |
|---|---|---|
| Lista de casos de prueba armada a partir de particiones de equivalencia | **VER** | Se compara contra las particiones, sin intervención del usuario |
| El software desarrollado | **VAL** | Se confronta con el uso previsto |
| Minuta de una reunión de requerimientos | **Depende** | **VAL** si se controla en reunión con el cliente; **VER** si se controla contra artefactos internos (p. ej. "pasamos el documento de Juancito para revisarlo entre nosotros la semana que viene") |

**4. "Determinar que se controlarán mediante Inspección los diagramas de secuencia."**
→ **VER.** La inspección es un tipo de revisión → técnica de control **estática** → vinculada a
verificación.

**5. "Distribuir entre los analistas la descripción del último caso de uso terminada por otro
analista, que **será chequeada** en la reunión."**
→ **VER / SP 2.1 Preparar las revisiones entre pares.** Son **pares** (mismo rol) y el chequeo
está **en futuro**. ⚠️ Si la opción listada dice `VAL/SP 2.1 Preparar las revisiones entre
pares`, la respuesta correcta es **NINGUNA**.

**6. "Dos analistas **chequean** el último caso de uso terminado por otro analista, planteando
las observaciones pertinentes."**
→ **VER / SP 2.2 Llevar a cabo las revisiones entre pares.** Presente, no preparación.

**7. "Ya se documentaron los hallazgos y se enviaron al autor. **En este momento se está
almacenando** la información de las identidades de los analistas en una parte del repositorio a
la que sólo accede Calidad."**
→ **VER / SP 2.3 Analizar los datos de la revisión entre pares** (subpráctica: *almacenar los
datos para futura referencia y análisis*).

**8. "Personal del equipo de proyecto controla si el contenido de los casos de uso cumple con lo
documentado en las **Minutas de Relevamiento**."**
→ **VER / SP 3.1 Realizar la verificación.** No es VAL (no participa el cliente) ni PPQA (no se
chequea un estándar organizacional).

**9. "Controlar si los nombres de las etiquetas de pantalla cumplen las definiciones estándar
del **Glosario**."**
→ **VER / SP 3.1 Realizar la verificación.** El glosario es del proyecto, no un estándar
organizacional → no es PPQA. Si dijera "hacer la lista de etiquetas a controlar", sería
**preparar**.

**10. "Controlar **con el usuario** si los nombres de las etiquetas se entienden y se
corresponden con los conceptos de negocio correctos."**
→ **VAL / SP 2.1 Realizar la validación.** Involucra al cliente y se hace en el momento.

**11. "Coordinar la agenda de horarios del server en instalaciones del cliente para realizar la
**prueba de aceptación**."**
→ **VAL / SP 1.2 Establecer el entorno de validación.** ⚠️ Si dijera **prueba de sistema**,
sería **VER**.

**12. Ciclos de vida — banco de respuestas:**

| Consigna | Respuesta | Razón |
|---|---|---|
| Ciclo que mejora las posibilidades de **salir antes a producción** | **Incremental** | Después del primer incremento ya se puede entregar parte de la funcionalidad planificada |
| Ciclo que permite trabajar con **requerimientos no estabilizados** | **Iterativo** | Reduce el riesgo entre necesidades del usuario y producto final por malentendidos en el relevamiento |
| Ciclo que **menos colabora** con requerimientos inestables | **Cascada** | Cerrado el análisis, los cambios no se contemplan hasta terminar las pruebas |
| Ciclo que reduce el riesgo de **subestimar el esfuerzo** | **Prototipado** | Al construir la pantalla se entiende mejor el requerimiento; el incremental no ayuda porque si subestimás el último módulo te enterás recién al hacerlo |
| Requerimientos **conocidos y estables** | **Cascada o Incremental** | Ambos sirven; cascada entrega al final, incremental divide en versiones |
| **Mantenimiento correctivo**, un par de semanas, ajustes a requerimientos ya implementados | **Cascada** | Prevalecen programación y prueba; no vale la pena armar incrementos de 3 días con su versionado y despliegue |
| Cliente necesita **salir al mercado lo antes posible** (caso pandemia/home office) | **Incremental** | Entregas tempranas y parciales |

**13. Pruebas en un ciclo incremental:**

- "El análisis se realiza sólo en el primer incremento" → **FALSO**. Cada incremento es una
  mini-cascada con análisis, diseño, codificación y prueba.
- "La prueba de sistema se realiza sólo en el último incremento" → **FALSO**.
- ¿En qué incrementos hay prueba de sistema? → **En todos.** Cada incremento se plantea para
  terminar en un producto funcional, así que se hacen todas las pruebas en todos.
- Afirmaciones válidas: **la prueba unitaria se realiza en cada incremento**.

**14. Variables que inciden en la elección del ciclo de vida:**
→ **Necesidad de poner en producción antes de estar terminado** y **estabilidad de los
requerimientos**. (No: presupuesto del cliente, cantidad de recursos, ni tipo de lenguaje.)

**15. En cascada, ¿en qué fase se confecciona el **manual de usuario**?**
→ **Prueba.** El proceso de pruebas contempla, además de definir/elaborar/ejecutar/evaluar
pruebas, la elaboración de la documentación de usuario (manuales de usuario y de
administración).
→ **Artefactos relevantes para hacerlo:** **GUI** y **caso de uso**. (No el código fuente ni el
informe de pruebas unitarias: no le sirven a un usuario para usar el sistema.)

**16. V o F sobre V&V:**

| Afirmación | |
|---|---|
| El objetivo final de V&V es establecer **confianza** de que el sistema es adecuado | **V** |
| El objetivo final de V&V es establecer confianza de que el sistema **realiza las funciones correctamente** | **V** |
| Una compañía puede decidir lanzar al mercado antes de estar plenamente probado y depurado | **V** (entorno de mercado con pocos competidores) |
| Algunas pruebas funcionales pueden realizarse **sin conocer cómo funciona** el programa | **V** (caja negra) |
| Para probar si un requerimiento se cumple **alcanza con armar un caso de prueba** | **F** |

**17. Particiones de equivalencia — caso "calificación por edad y peso" (tabla 7–14 años):**

- Para la **edad** hay **8 particiones** de equivalencia, no una sola: el criterio de
  calificación **cambia para cada edad**, así que el sistema trata cada edad de forma distinta.
- **Valores límite de la edad:** **7 y 14** (los extremos del rango soportado).
- Para **edad 11** (Excelente 42-46, Muy Bueno 47-50, Bueno 51-52, Regular 53-55, Bajo fuera de
  42-55), los valores límite de peso incluyen **41, 42, 46, 47, 55, 56**.
- **Tablas de decisión** es la técnica **más apropiada** para este caso: hay **múltiples
  condiciones** (edad Y peso) que combinadas llevan a distintas acciones (la calificación).

#### Dudas / pendientes

- El cuestionario titula esta sección "**Validación y Verificación (Nivel de Madurez 3)**", lo
  cual es correcto para VER y VAL. Pero el mismo archivo pone **PPQA en nivel 2** y **VER/VAL en
  3**, así que cuidado al mezclar: la pregunta "¿en qué nivel nace el aseguramiento de la
  calidad?" se refiere a **PPQA = nivel 2**, no a VER/VAL.
- La consigna del ejercicio de asignación de módulos por esfuerzo
  (`Preguntas de Cuestionario.md:63`, tabla de 19 requerimientos y 77 h) quedó **sin resolver**
  en la fuente ("Nota:" vacía). Resolverlo: por la agrupación clara en 4 módulos con esfuerzos
  acotados y requerimientos estables, apunta a **Incremental**, pero conviene confirmarlo.
- El cuestionario tiene la marca "**Quedé página 41**" (`:87`) y varias filas vacías: el archivo
  está **incompleto**. Faltan las secciones "BP", "Requerimientos - Requisitos" y buena parte de
  "Proyecto - EDT - Esfuerzo - Recursos - Mantenimiento".
- La sección "Proceso de pruebas" de `Unidad 5.md:364` tiene una nota del autor —
  "?? ver si lo pongo" — o sea que ese bloque puede estar recortado respecto del original.
- Falta el detalle de las **causas y criterios de complejidad** en las tablas de decisión y la
  imagen del cuadro "Tipo de revisión y nivel de formalidad" (`Unidad 5.md:874`).

#### Fuentes

- `fuentes/ICS/Unidad 5.md` — fuente principal y más detallada de la unidad (V&V, ciclos de
  vida, estrategias, niveles y tipos de prueba, técnicas dinámicas y estáticas, revisiones).
- `fuentes/ICS/Resumen Unidad 1,2y3.md` — "U5 – Verificación y Validación" (versión más
  resumida del mismo contenido).
- `fuentes/ICS/Preguntas de Cuestionario.md` — secciones "Ciclo de vida - Incrementos",
  "Validación y Verificación", "Particiones de equivalencia".
- Referenciado pero no ingerido: "Guía de validación y verificación" (PDF de la UNECO), citado
  por número de página en el cuestionario.

---

## Log

- 2026-08-10: Ingesta inicial de la materia. Se cargaron 4 fuentes en `fuentes/ICS/`
  (`Resumen Unidad 1,2y3.md`, `Unidad 5.md`, `Resumen de ISW.md`,
  `Preguntas de Cuestionario.md`). Se creó el índice completo y se desarrollaron las
  unidades 1, 2, 3, 4 y 5 desde cero (el archivo estaba vacío). Se resolvió además la
  Tarea 1 de CMMI (contrastes y similitudes entre nivel 1 y nivel 5), integrada en la
  Unidad 1. Pendientes principales: confirmar la numeración de la Unidad 4, el nivel de
  madurez de OT, y la fórmula del factor de ajuste de APF.
- 2026-08-20: tarea de la Clase 2 (Brozo) — casos de prueba por valores límite
  para la aplicación bancaria (punto 3). Fuente: página de Notion "Clase 2
  Brozo". Derivado en `tarea-casos-prueba-valores-limite.md` (+ .docx/.pdf).
