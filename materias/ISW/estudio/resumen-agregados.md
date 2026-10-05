# Agregados al resumen impreso

> Lo que cambió al alinear el resumen con el temario oficial, con la **numeración de tu impreso**
> (22 páginas). Diez de sus 17 capítulos siguen igual.

## Cómo intercalar estas hojas

La **página 1** (esta) va adelante de todo. Las **páginas 2 a 6** van juntas entre la pág. 5 y la 7
de tu impreso. Si imprimís doble faz, mandá esta página sola: va en otro lugar que las demás.

| Pág. | Simple faz | Doble faz |
|---|---|---|
| **6** | Sacala: el capítulo 6 queda reemplazado y el final de 5.3 está repetido en las hojas nuevas | Está al dorso de la 5: tachá desde **"6. La gestión de procesos"** |
| **7** | Tachá la sección **6.4**, que viene actualizada | Igual |
| **20** | Tachá desde **"15. El aseguramiento de la calidad"** hasta el final | Igual |
| **21** | Sacala: capítulos 15 y 16, no entran | Está al dorso de la 22: tachala entera |
| **22** | Tachá el párrafo de **RSKM** y, en el capítulo 17, la oración **"Confundir PPQA con VER"** | Igual |

## El parcial y su temario

**Sábado 26 de septiembre, 9:30.** Presencial, **no es a libro abierto**, se aprueba con el **60 %**
de los puntos. Entran las unidades **1, 2, 3 y 5**, recortadas a lo que lista el temario:

| Unidad | Qué entra | En tu impreso |
|---|---|---|
| **1** Modelos de calidad | Introducción a la calidad · Guía de ingeniería del software · CMMI: componentes de un área de proceso y niveles de madurez | Caps. 1 a 5, y 5.4 de las hojas nuevas |
| **2** Gestión de procesos | OPF, OPD y OT **sin subprácticas** · Presentación de Proceso y RUP, págs. 1 a 46 | Caps. 6 y 6 bis de las hojas nuevas, y cap. 7 |
| **3** Gestión de proyectos | PP y PMC · Guía práctica de gestión de proyectos · Puntos función (metodología y glosario) | Caps. 8 y 9 |
| **5** Verificación y validación | VER y VAL · Guía de V&V · Principios de Myers · Casos de prueba desde casos de uso | Caps. 10 a 14 |

**Quedan afuera** la unidad 4 (gestión de requerimientos), la guía avanzada de gestión de proyectos,
la guía de mejores prácticas de calidad de producto y, de RUP, los objetivos de cada fase y los
propósitos de cada disciplina. De REQM, PPQA, CM, MA, RSKM y RD alcanza con saber el nivel de
madurez: por eso salen los capítulos 15 y 16.


<div style="break-before: page; page-break-before: always;"></div>

## 5.3 Madurez y capacidad (continuación)

La **madurez**, que es la representación **por etapas**, mide a la **organización entera** contra
los conjuntos fijos de áreas de cada nivel. Es la que se certifica y la que usan todos los
ejercicios de la materia.

La **capacidad**, que es la representación **continua**, mide el nivel alcanzado en **un área de
proceso puntual**, con independencia del resto. Sirve para que la organización elija en qué área
quiere crecer primero, según lo que le duela al negocio.

### 5.4 Qué áreas hay en cada nivel

Las 22 áreas se reparten así entre los niveles 2 a 5:

| Nivel | Áreas de proceso |
|---|---|
| **2** | **PP** Planificación de proyecto · **PMC** Monitorización y control del proyecto · REQM Gestión de requerimientos · MA Medición y análisis · PPQA Aseguramiento de la calidad de proceso y de producto · CM Gestión de configuración · SAM Gestión de acuerdos con proveedores |
| **3** | **OPF** Enfoque en procesos · **OPD** Definición de procesos · **OT** Formación organizativa · **VER** Verificación · **VAL** Validación · RD Desarrollo de requerimientos · TS Solución técnica · PI Integración de producto · RSKM Gestión de riesgos · IPM Gestión integrada de proyecto · DAR Análisis de decisiones y resolución |
| **4** | OPP Rendimiento de procesos de la organización · QPM Gestión cuantitativa de proyecto |
| **5** | OID Innovación y despliegue en la organización · CAR Análisis causal y resolución |

En negrita, las siete que el temario desarrolla. Del resto alcanza con el nivel: es lo que hace
falta para resolver un caso como "cumple todo el nivel 3 pero le falta MA", que deja a la
organización en nivel 1 porque MA es de nivel 2.

> ⚠️ La traducción castellana del CMMI que usa la cátedra tiene una errata: la carátula del área
> de **OT** dice "nivel de madurez 4". Las tablas del mismo libro y la presentación de la cátedra
> la ponen en **nivel 3**, que es lo correcto.

## 6. La gestión de procesos de la organización

Tres áreas de nivel 3 se ocupan de los procesos de la organización como un todo, y son las que más
se confunden entre sí porque sus nombres se parecen. La forma más rápida de separarlas es por el
verbo que las define.

> **OPF diagnostica y despliega. OPD define y guarda. OT capacita.**

El temario incluye las tres áreas completas **salvo las subprácticas y la extensión IPPD**. Lo que
hay que dominar de cada una es el **propósito** y sus **metas y prácticas específicas**, que se
listan a continuación con el texto oficial.

### 6.1 OPF — Enfoque en procesos de la organización

> **Propósito:** planificar, implementar y desplegar las mejoras de procesos de la organización,
> basadas en una comprensión completa de las **fortalezas y debilidades actuales** de los procesos
> y de los activos de proceso.

Es el área del **diagnóstico y la mejora**. Evalúa dónde está parada la organización —incluso
comparándose con otras organizaciones—, arma los planes de acción para corregir las debilidades
que encuentra, y después despliega los cambios e incorpora lo aprendido. Sus tres metas siguen
exactamente ese recorrido:

- **SG 1 Determinar las oportunidades de mejora de procesos.** SP 1.1 Establecer las necesidades
  de procesos de la organización · SP 1.2 **Evaluar los procesos** de la organización · SP 1.3
  Identificar las mejoras de procesos.
- **SG 2 Planificar e implementar las mejoras de procesos.** SP 2.1 **Establecer planes de acción
  de procesos** · SP 2.2 Implementar los planes de acción de procesos.
- **SG 3 Desplegar los activos de proceso e incorporar las lecciones aprendidas.** SP 3.1
  Desplegar los activos de proceso · SP 3.2 Desplegar los procesos estándar · SP 3.3 Monitorizar la
  implementación · SP 3.4 **Incorporar las experiencias relativas al proceso en los activos de
  proceso** de la organización.

### 6.2 OPD — Definición de procesos de la organización

> **Propósito:** establecer y mantener un conjunto **usable** de **activos de proceso** de la
> organización y de **estándares del entorno de trabajo**.

Es el área que **define y guarda**. Todo lo que la organización tiene para que sus proyectos lo
reutilicen —el proceso estándar, los modelos de ciclo de vida, las reglas para adaptarlos, el
repositorio de mediciones, la biblioteca de documentos— lo establece OPD. Tiene una sola meta
dentro del temario, y cada práctica crea uno de esos activos:

- **SG 1 Establecer los activos de proceso de la organización.** SP 1.1 Establecer los **procesos
  estándar** · SP 1.2 Establecer las descripciones de los **modelos de ciclo de vida** · SP 1.3
  Establecer los **criterios y las guías de adaptación** · SP 1.4 Establecer el **repositorio de
  medición** de la organización · SP 1.5 Establecer la **biblioteca de activos de proceso** · SP 1.6
  Establecer los **estándares del entorno de trabajo**.

La segunda meta, *facilitar la gestión IPPD*, pertenece a la extensión IPPD y no entra.

> ⚠️ Cuando un enunciado menciona un **repositorio de medidas ligado a los procesos estándar de la
> organización**, la respuesta es **OPD** (SP 1.4), no MA. MA es de nivel 2 y mide **el proyecto**;
> el repositorio de la organización es un **activo**, y los activos son de OPD.

### 6.3 OT — Formación organizativa

> **Propósito:** desarrollar las **habilidades y el conocimiento** de las personas para que puedan
> realizar sus **roles** eficaz y eficientemente.

Primero se construye la capacidad de formar y después se forma. Un punto que suele preguntarse es
el reparto de responsabilidades: la organización cubre las necesidades de formación **comunes** a
los proyectos, y cada proyecto cubre las **específicas** suyas. Las necesidades **estratégicas**
miran varios años hacia adelante; el **plan táctico** baja eso a cursos concretos.

- **SG 1 Establecer una capacidad de formación organizativa.** SP 1.1 Establecer las necesidades de
  formación **estratégicas** · SP 1.2 Determinar qué necesidades de formación son
  **responsabilidad de la organización** · SP 1.3 Establecer un **plan táctico** de formación ·
  SP 1.4 Establecer la capacidad de formación.
- **SG 2 Proporcionar la formación necesaria.** SP 2.1 Impartir la formación · SP 2.2 Establecer
  los **registros** de formación · SP 2.3 Evaluar la **eficacia** de la formación.

### 6.4 Las prácticas que se cruzan entre OPF y OPD

En los exámenes aparece la misma lista de prácticas preguntada dos veces, una pidiendo las de OPF
y otra las de OPD. La regla para no mezclarlas: si la práctica **crea** un activo, es OPD; si
**evalúa, planifica, despliega o actualiza** lo que ya existe, es OPF.

| Práctica | Área |
|---|---|
| Establecer el repositorio de medición de la organización | **OPD** |
| Establecer las descripciones de los modelos de ciclo de vida | **OPD** |
| Establecer los criterios y las guías de adaptación | **OPD** |
| Evaluar los procesos de la organización | **OPF** |
| Establecer planes de acción de procesos | **OPF** |
| Incorporar las experiencias relativas al proceso en los activos de proceso | **OPF** |

## 6 bis. El proceso de desarrollo: SPEM y RUP

Los capítulos anteriores hablaron de procesos en abstracto: que hay que definirlos, guardarlos y
mejorarlos. Este capítulo baja a cómo se **escribe** un proceso concreto: con qué elementos se
describe, quién hace qué, y qué material de apoyo lo acompaña.

### Por qué gestionar procesos

Las organizaciones concentran su mejora en tres **dimensiones críticas**: las **personas**, los
**métodos y procedimientos**, y las **herramientas y el equipamiento**. Los procesos son lo que
sostiene a las tres: permiten alinear el modo de operar de la organización, incorporar el
conocimiento sobre cómo hacer mejor las cosas, aprovechar mejor los recursos y entender las
tendencias de la propia actividad.

Las áreas de **gestión de procesos** de CMMI contienen las actividades **transversales a los
proyectos**: definir, planificar, desplegar, implementar, monitorizar, controlar, evaluar, medir y
mejorar los procesos. Se dividen en **básicas** —OPF, OPD y OT, las del capítulo 6— y **avanzadas**
—OPP y OID—.

### SPEM

> **SPEM** (*Software Process Engineering Meta-Model*): estándar de la OMG —el mismo consorcio que
> mantiene UML— que establece los elementos clave para representar métodos, ciclos de vida,
> técnicas, roles, actividades, procesos, metodologías y plantillas de la ingeniería del software.

Es un **meta-modelo**: no describe un proceso en particular, sino el vocabulario con el que se
describe cualquier proceso. Por eso su alcance se limita a los **elementos mínimos** necesarios, sin
características de un dominio o disciplina en particular, y sirve para procesos de distintos
estilos, culturas, niveles de formalismo y ciclos de vida. No es un lenguaje de modelado de procesos
en general: está orientado al software.

Lo que aporta es facilitar la **comprensión y la comunicación** entre personas, facilitar la
**reutilización**, dar soporte a la **mejora** y a la **gestión** de procesos, y guiar su
**automatización**.

La idea central es que todo proceso se representa respondiendo tres preguntas:

| Pregunta | Elemento | Qué representa |
|---|---|---|
| **¿Quién?** | **Rol** | Quién hace el trabajo |
| **¿Qué?** | **Producto de trabajo** | Las entradas que usan las tareas y las salidas que producen |
| **¿Cómo?** | **Tarea** | El esfuerzo a realizar |

Además, SPEM define cuatro **niveles de detalle** para representar ese esfuerzo, de mayor a menor.
El **delivery process** es un proceso completo, tan complejo como se necesite, que sirve de base
para un tipo de proyecto. El **capability pattern** es un fragmento de proceso **reutilizable** más
de una vez dentro de un delivery process. La **actividad** es el elemento central, que organiza
roles, productos de trabajo y tareas. Y la **tarea** es la porción **más pequeña** de trabajo del
modelo.

Un ejemplo recorre los cuatro niveles: el ciclo de vida típico de RUP contiene la disciplina
*Entorno*, que contiene la actividad *Preparar el entorno para el proyecto*, que contiene la tarea
*Personalizar el proceso de desarrollo para el proyecto*.

### Los elementos del proceso en RUP

**RUP** (*Rational Unified Process*) es un proceso iterativo e incremental construido sobre SPEM.
Sus elementos son los siguientes.

**Fase.** El ciclo de vida se descompone en fases, y cada fase es un **período de tiempo entre dos
objetivos importantes**. RUP tiene cuatro: **Concepción** (o Inicial), **Elaboración**,
**Construcción** y **Transición**.

**Disciplina.** Una **categorización de tareas** según la similitud de sus preocupaciones y la
cooperación del esfuerzo. RUP tiene nueve: modelado de negocio, requisitos, análisis y diseño,
implementación, prueba, despliegue, configuración y gestión de cambios, gestión de proyectos, y
entorno.

Las fases y las disciplinas son dos ejes distintos: las fases **ordenan el tiempo**, las
disciplinas **agrupan el tipo de trabajo**. Por eso se cruzan, y a lo largo de las fases se trabaja
en varias disciplinas a la vez.

**Actividad.** Agrupa lógicamente elementos de proceso relacionados. **Una disciplina tiene una o
más actividades, y una actividad tiene una o más tareas.**

**Tarea.** Describe una **unidad de trabajo**. La llevan a cabo **roles específicos**, dura entre
**unas horas y unos días**, suele afectar a uno o pocos productos de trabajo y puede desglosarse en
**pasos**. Una tarea bien descripta reúne el **rol responsable**, los **productos de trabajo de
entrada y de salida**, y las guías que la apoyan: **directrices, plantillas y listas de
comprobación**.

> Ejemplo: la tarea *Desarrollar la visión* la ejecuta el **analista de sistemas**; toma como
> entrada las **solicitudes del interesado** y produce como salida la **visión**. Sus pasos son
> acordar el problema, identificar a los interesados, definir los límites del sistema, identificar
> las restricciones, formular el problema y definir las características del sistema. La apoyan la
> directriz *Entrevista*, la plantilla *Visión* y la lista de comprobación *Visión*.

**Rol.** Un conjunto de **habilidades, competencias y responsabilidades** relacionadas: analista de
sistemas, arquitecto de software, diseñador, revisor técnico.

**Producto de trabajo.** Un **resultado significativo del proceso**: los roles los usan para
realizar tareas y los producen al realizarlas. Hay tres tipos:

| Tipo | Qué es |
|---|---|
| **Artefacto** | Un producto **tangible**, no trivial: un documento, un modelo, el código |
| **Resultado** | Un producto **intangible**: un estado o una consecuencia del trabajo |
| **Entregable** | Un **empaquetado** de otros productos de trabajo, que se entrega a una parte interna o externa |

### Las guías

Una **guía** es todo contenido cuyo objetivo principal es **explicar otros elementos** del proceso.
RUP enumera nueve tipos —conceptos, directrices, materiales de soporte, documentación, plantillas,
listas de comprobación, ejemplos, informes y guías de herramientas— y la presentación de la cátedra
desarrolla ocho:

| Guía | Qué es |
|---|---|
| **Plantilla** | La **estructura** de un producto de trabajo: secciones, formato y cómo completarlas |
| **Directriz** | Indicaciones sobre **cómo hacer** algo concreto; se aplica a tareas y productos de trabajo |
| **Lista de comprobación** | Elementos que deben **completarse o verificarse**; se usa en revisiones e inspecciones |
| **Ejemplo** | Una instancia **parcialmente completa** de un producto, para mostrar cómo queda |
| **Concepto** | Una **idea fundamental**, más general que una directriz |
| **Guía de herramientas** | Cómo usar una **herramienta específica** para producir parte de un producto |
| **Documentación** | Documentos publicados **fuera** de RUP a los que el proceso hace referencia |
| **Informe** | Un resultado **generado automáticamente** por una herramienta a partir de otros productos |

Las guías se conectan con el capítulo 7, que sigue a esta hoja: una plantilla, una directriz o una lista de
comprobación de la organización son **activos**, y el documento que se produce al usarlas en un
proyecto es un **producto de trabajo**.

## Agregados cortos a los capítulos 8 y 9

**Al final de 8.3, sobre PMC (pág. 8).** Sus dos metas son **monitorizar el proyecto frente al plan** —parámetros de planificación,
compromisos, riesgos, gestión de datos, involucración de los interesados, revisiones de progreso y
revisiones de hitos— y **gestionar las acciones correctivas hasta su cierre**: analizar problemas,
llevar a cabo las acciones correctivas y gestionarlas.

**Al final de 9.2, sobre puntos función (pág. 11).** El temario incluye también el **glosario** de la guía de puntos función. Los términos que conviene
reconocer son: **PFD**, puntos función sin ajustar; **PFM**, puntos función de la mejora (cuando se
mide un cambio sobre una aplicación existente); **PFDM**, puntos función sin ajustar de la mejora;
**PFP**, puntos función de las pruebas; **fichero referenciado**, un fichero lógico interno leído o
modificado por una transacción, o un fichero de interfaz externo leído por ella; y **factor de
impacto**, el grado de cambio que sufre una función.
