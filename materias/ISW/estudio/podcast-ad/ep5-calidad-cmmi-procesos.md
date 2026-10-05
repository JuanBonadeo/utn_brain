# Episodio 5: Calidad, CMMI y gestión de procesos

> Fuente para el podcast de repaso del parcial de **Aprobación Directa** de Ingeniería y
> Calidad de Software (opción múltiple, a libro abierto en papel). Contiene los capítulos
> 2, 3, 4, 5, 6, 7, 8 y 9 del resumen de estudio `resumen-ad.md`, con su numeración original: las
> referencias a otros capítulos remiten a ese resumen.

## 2. Qué significa calidad en software

La palabra calidad arrastra un problema: todos creen saber qué quiere decir, y cada uno entiende
algo distinto. En la materia se trabaja con una idea central —**calidad es idoneidad de uso**— y
varias definiciones que la precisan desde ángulos diferentes. En una opción múltiple, cada una se
reconoce por la palabra que aporta.

La definición **clásica**, de Juran, la plantea en dos mitades: las características del producto
que satisfacen las necesidades del cliente, y la **inexistencia de deficiencias**. Un producto
puede tener todas las funciones pedidas y aun así fallar la segunda mitad. **Deming** la mira desde
el otro lado: calidad es lo que **aumenta la satisfacción del cliente**.

**CMMI** la define como la capacidad de un conjunto de características inherentes de un producto,
componente o **proceso** de satisfacer **por completo** los requisitos del cliente. Lo importante
acá es que incluye al proceso: para CMMI, un proceso también tiene calidad.

**ISO 8402** habla del conjunto de propiedades y características que le confieren aptitud para
satisfacer necesidades **explícitas o implícitas**. La palabra que aporta es *implícitas*: hay
expectativas que el cliente nunca escribió y que igual espera que se cumplan. **ISO 9000** la
vuelve una cuestión de grado: el **nivel** al que las características inherentes satisfacen los
requisitos.

### 2.1 De qué depende la calidad

Cuatro elementos la determinan: los **procesos y buenas prácticas** que se siguen, las
**herramientas** disponibles, las **personas** que hacen el trabajo, y las **medidas y métricas**
con las que se controla. Ninguno alcanza por sí solo. Un equipo excelente con un proceso caótico
produce resultados irrepetibles, y un proceso impecable no compensa a un equipo sin formación.

### 2.2 Tres tipos de calidad de producto

No toda la calidad se ve desde afuera, y esa distinción explica por qué a veces un sistema que
"anda bien" es un problema.

La **calidad interna** es la que **el cliente no percibe**: facilidad de mantenimiento, claridad
del código, respeto de los estándares, reusabilidad. No la ve, pero la paga: es la que determina
cuánto cuesta cada cambio futuro.

La **calidad externa** es la visible: que el producto cumpla los requerimientos acordados.

La **calidad de uso** es la que algunos llaman *calidad futura*. Es la que no se tuvo en cuenta y
aparece recién cuando el software se usa de verdad: el sistema pasa todas las pruebas, se entrega,
y a la media hora de operación real se nota el problema que nadie había previsto.

### 2.3 Los tres niveles de gestión de la calidad

La calidad se puede gestionar en tres escalas distintas, y cada una tiene sus herramientas.

A nivel de **producto** se gestiona con pruebas ejecutadas en paralelo a cada etapa del
desarrollo. A nivel de **proyecto** se gestiona controlando las fases y las áreas de gestión de
ese proyecto en particular. A nivel de **proceso** se gestionan las áreas de proceso de **toda la
organización** mediante una metodología.

Ese tercer nivel es el que ocupa la mayor parte de la materia, y es donde juega CMMI. La apuesta
de fondo es que **la calidad de un producto está muy influenciada por la calidad del proceso
empleado para desarrollarlo y mantenerlo**: si el proceso es bueno, los productos buenos dejan de
ser casualidad.

Conviene fijar desde ya la diferencia entre **proceso** y **proyecto**, porque atraviesa toda la
materia. El proceso es **genérico y repetitivo**, no tiene fechas y **produce siempre el mismo
producto**; el proyecto es **único**, tiene inicio y fin, y trabaja con restricciones de tiempo,
dinero y recursos. Un proyecto es, en el fondo, una instancia de los procesos de la organización.

### 2.4 Aseguramiento y control de la calidad

Dentro de la gestión de la calidad conviven dos actitudes que se confunden seguido: **prevenir**
los defectos o **detectarlos**.

| | **QA — Aseguramiento** | **QC — Control** |
|---|---|---|
| Naturaleza | **Preventivo** | **Reactivo** |
| Mira | El **proceso** | El **producto** |
| Ejemplos | Auditorías de proceso, definición de procesos, formación | Revisiones, inspecciones, pruebas |

El ejemplo de clase lo deja claro. Una fábrica produce mil tazas, al final controla que pesen menos
de 150 gramos y descarta las diez que no cumplen: eso es **control**. Si salen quinientas
defectuosas y, en vez de descartarlas, se revisa el proceso productivo para que no vuelva a pasar,
eso es **aseguramiento**. El área PPQA de CMMI (capítulo 21) es aseguramiento en este sentido; las
pruebas son control.

> ⚠️ La presentación de INTECO asocia además la verificación con QA y la validación con QC. Eso
> **no coincide con CMMI**, donde la prueba de sistema es verificación. Para ubicar una actividad en
> un área, usá siempre CMMI (capítulo 16).

## 3. El software como objeto de ingeniería

Antes de hablar de procesos conviene entender por qué el software necesita una ingeniería propia
y no le sirven las de otras disciplinas.

> **Software** = programas + datos + documentos. Es un elemento **lógico**, no físico.

La percepción común —y equivocada— es que el software son sólo los programas. La norma IEEE 610
agrega un cuarto componente, los procedimientos, pero en los parciales la respuesta esperada fue la
de INTECO: **programas, datos y documentos**.

Esa naturaleza lógica trae cuatro consecuencias que condicionan todo lo demás.

**El software se desarrolla, no se fabrica.** No hay línea de producción: cada producto se
construye para los requisitos únicos de un cliente. No se pueden amortizar costos repitiendo
unidades, porque no hay unidades que repetir.

**El recurso principal son las personas, y no son intercambiables con el tiempo.** Agregar gente
no acelera un proyecto de forma lineal: el desarrollo requiere coordinación y comunicación, y cada
integrante nuevo no es productivo de inmediato y además consume tiempo de los que ya están. Por
eso es falso el principio de que "las personas y el tiempo son intercambiables".

**El software no se estropea, pero se deteriora.** Un engranaje se desgasta por uso; el software
no. Lo que lo degrada son los **cambios**: cada modificación de mantenimiento tiene probabilidad
de introducir defectos nuevos, y con los años el producto acumula complejidad y fragilidad.

**La reutilización está lejos de su potencial.** Identificar componentes reutilizables es difícil
justamente porque cada producto se construye para requisitos únicos.

### 3.1 Qué es la ingeniería del software

> **Ingeniería del software (IEEE):** aplicación de un enfoque **sistemático, disciplinado y
> cuantificable** al desarrollo, operación y mantenimiento del software.

Las tres palabras importan. *Sistemático* excluye improvisar; *disciplinado* excluye abandonar el
método cuando aprieta el tiempo; *cuantificable* excluye opinar sin medir.

Se suele representar como una **tecnología multicapa**: sobre una base de **compromiso con la
calidad** se apoyan los **procesos**, sobre ellos los **métodos**, y encima las **herramientas**.
El orden no es decorativo: comprar herramientas sin proceso debajo no produce calidad. El proceso
es la capa que mantiene unidas a las demás: define quién hace qué, cómo se coordinan las
actividades y dónde están los **puntos de control de calidad**. Todo equipo tiene un proceso,
aunque muchas veces sea ad hoc, invisible y caótico.

### 3.2 Las etapas y el mantenimiento

Las etapas clásicas son: análisis de requisitos, especificación, diseño y arquitectura,
programación, **prueba** y mantenimiento. La etapa que comprueba que el software realiza
correctamente las tareas indicadas en la especificación es la de **prueba**, y es buena práctica
que pruebe alguien distinto de quien programó.

El mantenimiento no es una sola cosa. Distinguir los cuatro tipos es una de las preguntas
recurrentes de la materia:

| Tipo | Qué persigue |
|---|---|
| **Correctivo** | Corregir errores detectados en el producto |
| **Evolutivo** | Incorporaciones, modificaciones y **eliminaciones** para cubrir la expansión o el cambio en las **necesidades del usuario** |
| **Adaptativo** | Responder a cambios del **entorno** donde opera el sistema: hardware, software de base, base de datos, comunicaciones |
| **Perfectivo** | Mejorar la **calidad interna** del sistema, sin cambio funcional visible |

> ⚠️ **Perfectivo no es sinónimo de evolutivo**: el evolutivo cambia lo que el sistema **hace**; el
> perfectivo mejora **cómo está hecho**. Y que un cambio lo pida el cliente no lo vuelve evolutivo:
> llevar el sistema a sucursales de otra ciudad, que la tecnología actual no soporta, es
> **adaptativo**, porque lo que cambia es el entorno.

### 3.3 Los principios de la disciplina

De la lista de principios de INTECO, dos aparecen una y otra vez como correctos: **haz de la
calidad la razón de trabajar** y **probar, probar y probar**. Otros dos que conviene reconocer:
el **compromiso del cliente es el factor más crítico** de la calidad, e **itera en todas las fases
excepto en la codificación**. Y tres aparecen como distractores porque enuncian exactamente lo
contrario de lo que sostiene la disciplina: que las personas y el tiempo son intercambiables, que
conviene hacerlo rápido primero y correcto después, y que hay que forzar el mismo modelo de ciclo
de vida en todos los proyectos.

## 4. CMMI: qué es y para qué sirve

**CMMI** son las siglas de *Capability Maturity Model Integration*: modelo de madurez de
capacidades integrado, desarrollado por el SEI. La cátedra usa la versión **CMMI-DEV v1.2** en
castellano. No es una metodología ni un manual de procedimientos. Es una **guía de buenas
prácticas** que no dice *cómo* hacer las cosas, sino **qué** hay que lograr.

Esa distinción es la clave para entender el modelo entero. CMMI define objetivos; cada
organización decide con qué prácticas los alcanza, y puede usar prácticas propias distintas de las
que el modelo sugiere, siempre que cumpla el objetivo.

Trabajar con un modelo probado da tres cosas que una organización sola tarda años en construir: la
**experiencia acumulada** de otras empresas, un **lenguaje y una visión común** dentro de la
organización, y un **punto de partida** para no inventar desde cero. Los resultados que se le
atribuyen son menos defectos, menos tiempo de entrega, menor costo, más satisfacción del cliente y
más beneficios.

Hay algo que CMMI **no** hace: agregar actividades técnicas. Una organización sin ningún nivel
también analiza, diseña, programa y prueba. Lo que cambia con la madurez es si esas actividades
están **definidas, institucionalizadas, medidas y mejoradas**.

### 4.1 Área de proceso

> **Área de proceso:** grupo de prácticas relacionadas que, implementadas conjuntamente,
> satisfacen un conjunto de objetivos importantes para la mejora en esa área.

CMMI define **22 áreas de proceso**, repartidas en los niveles de madurez 2 a 5 y agrupadas en
cuatro categorías: **gestión de procesos**, **gestión de proyectos**, **ingeniería** y **soporte**.
Cada una cubre un aspecto del trabajo: planificar proyectos, gestionar requerimientos, verificar
productos, formar gente.

## 5. Anatomía de un área de proceso

Toda área de proceso está construida con las mismas piezas, y esas piezas tienen distinto peso.
Entender cuál es obligatoria y cuál no es probablemente el concepto más preguntado de la materia.

| Categoría | Qué es | Qué incluye |
|---|---|---|
| **Requeridos** | Lo que la organización **debe** lograr para satisfacer el área. Es la base de las evaluaciones | **Metas específicas (SG)** y **metas genéricas (GG)** |
| **Esperados** | Lo que **puede** implementar para lograr lo requerido. Se admiten alternativas propias | **Prácticas específicas (SP)** y **prácticas genéricas (GP)** |
| **Informativos** | Material que ayuda a entender cómo aproximarse a lo requerido y lo esperado | Subprácticas, productos de trabajo típicos, ampliaciones, elaboraciones de prácticas genéricas, notas, ejemplos, referencias, declaración de propósito, áreas relacionadas |

> ⚠️ Lo **requerido son sólo las metas**. Las prácticas —aunque el modelo las liste y las
> explique— son **esperadas**, no obligatorias. Una organización puede sustituir una práctica por
> otra si con ella alcanza la misma meta. Las subprácticas son informativas, aunque en los
> ejercicios de discriminación son las que justifican la respuesta (capítulo 24).

### 5.1 Qué significa "genérico"

Un componente es **genérico** cuando la misma declaración se aplica a **múltiples áreas de
proceso**. Las metas y prácticas específicas son propias de un área; las genéricas se repiten en
todas.

El papel de las genéricas es tratar la **institucionalización**: que el proceso no dependa de la
buena voluntad de quien lo ejecuta, sino que esté incorporado a la manera de trabajar de la
organización. Esa es la respuesta cuando preguntan qué componentes tratan la institucionalización.

Dos genéricas aparecen en los ejercicios. La **GP 2.9 Evaluar objetivamente la adherencia** está
en todas las áreas y se implementa a través de PPQA (capítulo 21). La **GP 2.6 Gestionar
configuraciones** pone bajo control los productos de cada área con el sistema de gestión de
configuración (capítulo 20).

### 5.2 La numeración

Las metas se numeran secuencialmente: `SG1`, `SG2`, `GG1`. Las prácticas llevan dos números,
`SP x.y`, donde **x es el número de la meta** a la que pertenecen e **y el número de secuencia**
dentro de esa meta. Así, `SP 2.3` es la tercera práctica de la segunda meta específica.

Saber leer la numeración sirve para descartar opciones: si un área tiene dos metas específicas,
una opción que diga `SP 3.1` es imposible.

## 6. Los niveles de madurez

CMMI organiza la mejora en cinco escalones. Cada uno describe un estado de la organización, no una
lista de tareas cumplidas.

| Nivel | Nombre | Cómo se reconoce |
|---|---|---|
| **1** | Inicial | Caos: el éxito depende de la **heroicidad** del personal. Suelen entregar productos que funcionan, pero exceden el presupuesto y el calendario, **abandonan los procesos en las crisis** y no pueden repetir sus éxitos |
| **2** | Gestionado | Los proyectos se **planifican y se monitorizan**, y la disciplina **se mantiene bajo estrés**. Los procedimientos pueden ser **distintos en cada proyecto** |
| **3** | Definido | Existe un **conjunto de procesos estándar de la organización** y cada proyecto **adapta** el suyo desde ahí, siguiendo **guías de adaptación**. El rendimiento es predecible, pero sólo **cualitativamente** |
| **4** | Gestionado cuantitativamente | Se gestiona con **objetivos cuantitativos y estadística**. Se tratan las **causas especiales** de variación. El rendimiento pasa a ser predecible **cuantitativamente** |
| **5** | En optimización | **Mejora continua**. Se atacan las **causas comunes** de variación y se **cambia el proceso** para mejorar su rendimiento |

> **Causa especial:** la propia de una **circunstancia transitoria**, que no forma parte del
> proceso. **Causa común:** la variación que producen las **interacciones normales** entre los
> componentes del proceso.

Un servidor que llega diez días tarde y atrasa un proyecto es una causa especial. Una técnica de
estimación que subestima siempre los requerimientos complejos es una causa común: está metida en el
proceso, y se va a repetir en cada proyecto hasta que se cambie la técnica.

### 6.1 Las dos comparaciones que hay que poder explicar

**Nivel 2 frente a nivel 3: el alcance de los estándares.** En nivel 2 cada proyecto puede tener
sus propios procedimientos; lo que se exige es que los tenga, los siga y los sostenga. En nivel 3
los procedimientos **se adaptan desde el conjunto estándar de la organización**, y por lo tanto
son consistentes entre proyectos salvo por las diferencias que las guías de adaptación permitan.

**Nivel 4 frente a nivel 5: el tipo de variación que se trata.** El nivel 4 ataca las **causas
especiales** —las anomalías puntuales— y logra predictibilidad estadística. El nivel 5 ataca las
**causas comunes**, las que están incorporadas al proceso mismo, y para eliminarlas **cambia el
proceso**.

### 6.2 Cómo se avanza: las reglas del modelo escalonado

De estas tres reglas salen casi todos los ejercicios de niveles.

**Primera: para estar en un nivel hay que satisfacer todas las áreas de ese nivel y de los
anteriores.** Si falta una sola área, no se está en ese nivel. Una organización que cumple
perfectamente las áreas de nivel 3 pero incumple una de nivel 2 no está en nivel 3 ni en nivel 2:
está en **nivel 1**, que es el nivel por defecto porque no exige nada. Si lo que falta es de nivel
3, queda **como máximo en nivel 2**, y sólo si cumple todas las de nivel 2.

**Segunda: los niveles son acumulativos.** Alcanzar un nivel superior no exime de las metas de los
anteriores. Una organización nivel 5 sigue planificando y monitorizando proyectos todos los días.
Si dejara de hacerlo, se caería hasta nivel 1.

**Tercera: se puede instanciar un área de nivel superior al propio** si el contexto de negocio lo
justifica, pero se corre el riesgo de intentar prácticas **sin la base institucional que las
soporte**. Eso funciona hasta que aparece el estrés, que es justamente cuando más se las necesita.
Por eso saltar niveles es, en general, contraproducente.

> ⚠️ "El aseguramiento de la calidad nace en el nivel 3" es **falso**: PPQA es de nivel 2. Lo que
> no se puede dar por supuesto en una organización de nivel 2 son los estándares organizacionales,
> que son de OPD, nivel 3.

### 6.3 Madurez y capacidad

CMMI admite dos formas de mirar el progreso.

La **madurez**, que es la representación **por etapas**, mide a la **organización entera** contra
los conjuntos fijos de áreas de cada nivel. Es la que se certifica y la que usan todos los
ejercicios de la materia.

La **capacidad**, que es la representación **continua**, mide el nivel alcanzado en **un área de
proceso puntual**, con independencia del resto. Sirve para que la organización elija en qué área
quiere crecer primero, según lo que le duela al negocio. En la versión 1.2 los niveles de
capacidad van de **0 a 5**; los resúmenes que dicen 0 a 3 hablan de la versión 1.3.

### 6.4 Qué áreas hay en cada nivel

| Nivel | Áreas de proceso |
|---|---|
| **2** | **PP** Planificación de proyecto · **PMC** Monitorización y control del proyecto · **REQM** Gestión de requerimientos · **MA** Medición y análisis · **PPQA** Aseguramiento de la calidad de proceso y de producto · **CM** Gestión de configuración · SAM Gestión de acuerdos con proveedores |
| **3** | **OPF** Enfoque en procesos · **OPD** Definición de procesos · **OT** Formación organizativa · **VER** Verificación · **VAL** Validación · **RD** Desarrollo de requerimientos · **RSKM** Gestión de riesgos · TS Solución técnica · PI Integración de producto · IPM Gestión integrada de proyecto · DAR Análisis de decisiones y resolución |
| **4** | OPP Rendimiento de procesos de la organización · QPM Gestión cuantitativa de proyecto |
| **5** | OID Innovación y despliegue en la organización · CAR Análisis causal y resolución |

En negrita, las trece que este resumen desarrolla; del resto alcanza con el nivel. Las categorías:
**gestión de procesos** son OPF, OPD, OT, OPP y OID; **gestión de proyectos**, PP, PMC, SAM, IPM,
RSKM y QPM; **ingeniería**, REQM, RD, TS, PI, VER y VAL; y **soporte**, CM, PPQA, MA, DAR y CAR.

> ⚠️ La traducción castellana tiene erratas: en las carátulas, **OT** figura como nivel 4, **OID**
> como nivel 3 y **RSKM** como nivel 2. Lo correcto, según las tablas del mismo libro, es **OT = 3,
> OID = 5 y RSKM = 3**.

### 6.5 Nivel 1 y nivel 5 frente al mismo proyecto

Un ejercicio de clase muestra qué cambia de verdad entre niveles. Ante el mismo imprevisto —el
servidor llega diez días tarde y el cliente pide cambiar una regla de negocio—, la organización de
**nivel 1** estima a ojo, hace horas extra, se saltea las pruebas y acuerda el cambio por teléfono:
**abandona el proceso en la crisis**. La de **nivel 5** ya tenía el retraso registrado como riesgo,
hace entrar el cambio por gestión de requerimientos y de configuración, y al cierre busca las
causas comunes de los desvíos: **el proceso no se abandona, se ejecuta**. Lo que se olvida son las
similitudes: las dos **pueden entregar software que funciona**, hacen las mismas actividades
técnicas y las dos **pueden fallar**; el nivel 5 no garantiza cero defectos.

## 7. La gestión de procesos de la organización

Tres áreas de nivel 3 se ocupan de los procesos de la organización como un todo, y son las que más
se confunden entre sí porque sus nombres se parecen. La forma más rápida de separarlas es por el
verbo que las define.

> **OPF diagnostica y despliega. OPD define y guarda. OT capacita.**

Las tres trabajan **para toda la organización**, no para un proyecto: cuando un enunciado plantea
un problema de un proyecto puntual, difícilmente la respuesta sea una de ellas. Lo que hay que
dominar de cada una es el **propósito** y sus **metas y prácticas específicas**, que se listan a
continuación con el texto oficial.

### 7.1 OPF — Enfoque en procesos de la organización

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

> ⚠️ **SG 2 frente a SG 3** se pregunta siempre. La SG 2 trabaja con mejoras **todavía no
> aprobadas**, que se prueban en **proyectos piloto**. La SG 3 **despliega** a toda la organización
> una mejora **ya aceptada**. Fijate si el enunciado habla de una **propuesta** o de una
> **modificación ya introducida**.

**Su lugar entre PPQA y OPD.** PPQA **evalúa e informa**: emite no conformidades y tendencias de
calidad. OPF **analiza** esos informes y propone la mejora: si varios informes dicen que los
proyectos completan mal la plantilla de casos de prueba, OPF puede proponer una guía de llenado.
OPD **deja asentada** la mejora en el activo. El sector de SQA de una empresa suele hacer las dos
primeras cosas a la vez, así que no hay que confundir el departamento con el área de proceso.

### 7.2 OPD — Definición de procesos de la organización

> **Propósito:** establecer y mantener un conjunto **usable** de **activos de proceso** de la
> organización y de **estándares del entorno de trabajo**.

Es el área que **define y guarda**. Todo lo que la organización tiene para que sus proyectos lo
reutilicen —el proceso estándar, los modelos de ciclo de vida, las reglas para adaptarlos, el
repositorio de mediciones, la biblioteca de documentos— lo establece OPD. Tiene una sola meta que
entra en la materia, y cada práctica crea uno de esos activos:

- **SG 1 Establecer los activos de proceso de la organización.** SP 1.1 Establecer los **procesos
  estándar** · SP 1.2 Establecer las descripciones de los **modelos de ciclo de vida** · SP 1.3
  Establecer los **criterios y las guías de adaptación** · SP 1.4 Establecer el **repositorio de
  medición** de la organización · SP 1.5 Establecer la **biblioteca de activos de proceso** · SP 1.6
  Establecer los **estándares del entorno de trabajo**.

La segunda meta, *facilitar la gestión IPPD*, pertenece a la extensión IPPD y no entra.

Tres prácticas se preguntan con un rasgo que las delata. Las **guías de adaptación** (SP 1.3) dicen
cómo se arma el proceso de un proyecto a partir del estándar, y son la práctica de las
**excepciones**: el procedimiento para pedir que un proyecto no incluya cierta actividad es OPD SP
1.3. El **repositorio de medición** (SP 1.4) guarda **medidas** de los proyectos —"la base de datos
donde se registrarán métricas de todos los proyectos"—, mientras que la **biblioteca de activos**
(SP 1.5) guarda **documentos**: políticas, plantillas, checklists, lecciones aprendidas —"el sitio
de Intranet donde se consultan los documentos del proceso"—.

> ⚠️ Cuando un enunciado menciona un **repositorio de medidas ligado a los procesos estándar de la
> organización**, la respuesta es **OPD** (SP 1.4), no MA. MA es de nivel 2 y mide **el proyecto**;
> el repositorio de la organización es un **activo**, y los activos son de OPD.

> ⚠️ **No toda revisión entre pares es VER.** Si tres jefes de proyecto revisan un **procedimiento
> de la organización aún no publicado**, la respuesta es **OPD SP 1.1**: se revisa un activo, no un
> producto de un proyecto.

### 7.3 OT — Formación organizativa

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

> ⚠️ **OT no es PP SP 2.5.** Elegir qué cursos tienen que hacer los programadores **del proyecto
> X** antes de empezar es **PP SP 2.5** Planificar el conocimiento y las habilidades necesarios.
> Conseguir un instructor, o mandar a alguien a formarse para que después capacite a otros, sí es
> **OT** (SP 1.4), aunque lo aprovechen los proyectos.

### 7.4 Las prácticas que se cruzan entre OPF y OPD

En los exámenes aparece la misma lista de prácticas preguntada dos veces, una pidiendo las de OPF
y otra las de OPD. La regla para no mezclarlas: si la práctica **crea** un activo, es OPD; si
**evalúa, planifica, despliega o actualiza** lo que ya existe, es OPF.

| Práctica | Área |
|---|---|
| Establecer el repositorio de medición de la organización | **OPD** |
| Establecer las descripciones de los modelos de ciclo de vida | **OPD** |
| Establecer los criterios y las guías de adaptación | **OPD** |
| Establecer la biblioteca de activos de proceso | **OPD** |
| Evaluar los procesos de la organización | **OPF** |
| Establecer planes de acción de procesos | **OPF** |
| Desplegar los activos de proceso | **OPF** |
| Incorporar las experiencias relativas al proceso en los activos de proceso | **OPF** |

## 8. Activos de proceso y productos de trabajo

Esta distinción es corta de explicar y sorprendentemente fácil de errar, porque los dos conceptos
se refieren a documentos que a veces tienen nombres casi idénticos.

> Un **activo** es un artefacto que la organización produce **para ser usado en las tareas de los
> proyectos**. Un **producto de trabajo** es el resultado concreto de una tarea **de un proyecto**.

La pregunta que resuelve cualquier caso es: *¿esto existe para ser usado en muchos proyectos, o
salió de uno?*

Las señales de **activo** son las palabras plantilla, guía, directriz, modelo, estándar, política y
checklist. También son activos las **herramientas que la organización adquiere** en lugar de
desarrollar, junto con su documentación: el manual de usuario del compilador Java es un activo,
porque no es producto de ningún proyecto.

Las señales de **producto de trabajo** son las referencias a un proyecto concreto: "del cliente",
"del sistema desarrollado". Una minuta, el código fuente, una regla de negocio, la descripción del
proceso de negocio del cliente.

El par que fija el criterio es este: la **plantilla de manual de instalación** es un activo —es el
molde, y pertenece a la organización—, mientras que el **manual de instalación del sistema
desarrollado para el cliente** es un producto de trabajo —es lo moldeado, y pertenece al proyecto.

Lo mismo vale para las áreas que los tocan. El **caso de uso** es un producto de trabajo: lo
verifica **VER**, lo valida **VAL** con el cliente, y **PPQA** controla que respete el estándar. La
**plantilla de caso de uso** es un activo: la define **OPD** y la despliega **OPF**.

> ⚠️ Pregunta trampa: "¿qué área se encarga de verificar y almacenar los **productos de trabajo** a
> nivel organizacional?" La respuesta es **NINGUNA**. "Nivel organizacional" empuja hacia OPD,
> pero los productos de trabajo salen de cada proyecto; si la pregunta dijera **activos**, sí sería
> OPD.

## 9. El proceso de desarrollo: SPEM y RUP

Los capítulos anteriores hablaron de procesos en abstracto: que hay que definirlos, guardarlos y
mejorarlos. Este capítulo baja a cómo se **escribe** un proceso concreto: con qué elementos se
describe, quién hace qué, y qué material de apoyo lo acompaña.

### 9.1 Por qué gestionar procesos

Las organizaciones concentran su mejora en tres **dimensiones críticas**: las **personas**, los
**métodos y procedimientos**, y las **herramientas y el equipamiento**. Los procesos son lo que
sostiene a las tres. Las áreas de **gestión de procesos** de CMMI contienen las actividades
**transversales a los proyectos**, y se dividen en **básicas** —OPF, OPD y OT, las del capítulo
7— y **avanzadas** —OPP y OID—.

### 9.2 SPEM

> **SPEM** (*Software Process Engineering Meta-Model*): estándar de la OMG —el mismo consorcio que
> mantiene UML— que establece los elementos clave para representar métodos, ciclos de vida,
> técnicas, roles, actividades, procesos, metodologías y plantillas de la ingeniería del software.

Es un **meta-modelo**: no describe un proceso en particular, sino el vocabulario con el que se
describe cualquier proceso. Por eso su alcance se limita a los **elementos mínimos** necesarios, sin
características de un dominio o disciplina en particular, y sirve para procesos de distintos
estilos, culturas, niveles de formalismo y ciclos de vida. No es un lenguaje de modelado de procesos
en general —una afirmación que aparece como falsa—: está orientado al software.

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

### 9.3 Los elementos del proceso en RUP

**RUP** (*Rational Unified Process*) es un proceso **iterativo e incremental**, adaptable y no
prescriptivo, construido sobre SPEM. Sus elementos son los siguientes.

**Fase.** El ciclo de vida se descompone en fases, y cada fase es un **período de tiempo entre dos
objetivos importantes**. RUP tiene cuatro. **Concepción** (o Inicial) fija el alcance y los límites
del producto y estima el costo global. **Elaboración** estabiliza la arquitectura, los requisitos y
los planes, y trata los riesgos arquitectónicos. **Construcción** completa el desarrollo y la
prueba de toda la funcionalidad, con versiones alfa y beta. **Transición** entrega el producto:
prueba beta con operación en paralelo, conversión de datos y formación de los usuarios.

**Disciplina.** Una **categorización de tareas** según la similitud de sus preocupaciones y la
cooperación del esfuerzo. RUP tiene nueve: modelado de negocio, requisitos, análisis y diseño,
implementación, prueba, despliegue, configuración y gestión de cambios, gestión de proyectos, y
entorno.

Las fases y las disciplinas son dos ejes distintos: las fases **ordenan el tiempo**, las
disciplinas **agrupan el tipo de trabajo**. Por eso se cruzan, y a lo largo de las fases se trabaja
en varias disciplinas a la vez. Y aunque las cuatro fases hagan parecer a RUP una cascada, dentro de
cada fase hay **iteraciones**, y cada una termina en una versión ejecutable.

**Actividad.** Agrupa lógicamente elementos de proceso relacionados. **Una disciplina tiene una o
más actividades, y una actividad tiene una o más tareas.**

**Tarea.** Describe una **unidad de trabajo**. La llevan a cabo **roles específicos**, dura entre
**unas horas y unos días**, suele afectar a uno o pocos productos de trabajo y puede desglosarse en
**pasos**. Una tarea bien descripta reúne el **rol responsable**, los **productos de trabajo de
entrada y de salida**, y las guías que la apoyan: **directrices, plantillas y listas de
comprobación**.

> Ejemplo: la tarea *Desarrollar la visión* la ejecuta el **analista de sistemas**; toma como
> entrada las **solicitudes del interesado** y produce como salida la **visión**. La apoyan la
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

### 9.4 Las guías

Una **guía** es todo contenido cuyo objetivo principal es **explicar otros elementos** del proceso.
La presentación de la cátedra desarrolla ocho tipos:

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

Las guías se conectan con el capítulo anterior: una plantilla, una directriz o una lista de
comprobación de la organización son **activos**, y el documento que se produce al usarlas en un
proyecto es un **producto de trabajo**.
