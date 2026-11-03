# Episodio 6: Simulacro: el área, las preguntas BP y las confusiones

> Fuente para el podcast de repaso del parcial de **Aprobación Directa** de Ingeniería y
> Calidad de Software (opción múltiple, a libro abierto en papel). Contiene los capítulos
> 1, 24, 25 y 26 del resumen de estudio `resumen-ad.md`, con su numeración original: las
> referencias a otros capítulos remiten a ese resumen.
> Al final hay un anexo con todas las preguntas de los parciales AD de 2024 y 2025.

## 1. El parcial y su temario

El parcial de Aprobación Directa es **presencial**, de **opción múltiple** —entre 15 y 20 preguntas,
según la cátedra, aunque la cantidad es orientativa— y **a libro abierto, sólo en papel**: no se
permite ningún dispositivo electrónico. Se aprueba con el **60 % del total de puntos**. Para
promocionar la materia hay que aprobar los dos parciales, Regularización y Aprobación Directa, y
entregar los trabajos prácticos de clase. Si se desaprueba éste, queda el **Globalizador** de
Aprobación Directa.

A diferencia del parcial de Regularización, acá no hay recorte de páginas: entra **todo el
programa**.

| Unidad | Tema | Capítulos |
|---|---|---|
| **1 — Modelos de calidad** | Calidad, ingeniería del software, CMMI, niveles de madurez | 2 a 6 |
| **2 — Gestión de procesos** | OPF, OPD, OT, activos de proceso, SPEM y RUP | 7 a 9 |
| **3 — Gestión de proyectos** | PP, PMC, estimación y puntos función, riesgos, ciclos de vida | 10 a 13 |
| **4 — Requerimientos** | RD, REQM y gestión de solicitudes de cambio | 14 y 15 |
| **5 — Verificación y validación** | VER, VAL, pruebas, técnicas dinámicas y estáticas | 16 a 19 |
| **6 — Gestión de configuración** | CM: elementos, líneas base, versionado, cambios | 20 |
| **7 — Aseguramiento de calidad** | PPQA: auditorías, no conformidades, escalamiento | 21 |
| **8 — Medición y análisis** | MA: métricas de proceso, proyecto y producto | 22 |
| **9 — Pericias informáticas** | Evidencia digital, cadena de custodia, protocolo | 23 |

**Lo que muestran los parciales de 2024 y 2025.** Aunque entra todo, el peso estuvo en las
unidades que **no** estaban en el parcial de Regularización: **configuración, aseguramiento de la
calidad, requerimientos y medición**, más alguna pregunta de planificación y de verificación y
validación. Riesgos y pericias no aparecieron, pero entran.

Las preguntas tienen tres formas que se repiten. La primera es la pregunta **BP**: se describe cómo
trabaja una software factory y hay que decir si esa práctica **puede generar problemas de calidad**
y por qué; el capítulo 25 explica cómo resolverlas. La segunda pide reconocer **qué área de proceso
—y a veces qué práctica— corresponde a una actividad** descripta; para eso está el capítulo 24. La
tercera son ejercicios cortos con números: calcular cuántos años sobrevive un esquema de versión,
cuántas releases mínimas tiene un proyecto, o qué casos de prueba salen de una partición.

> ⚠️ En las preguntas de selección múltiple, **marcar una opción incorrecta además de la correcta
> deja la pregunta en cero**. Pasó en el parcial de 2024. Ante la duda, es mejor marcar sólo lo que
> se puede justificar.

## 24. Cómo reconocer el área de proceso en un enunciado

El ejercicio más repetido de la materia es una variación de la misma consigna: *"relacione la
actividad descripta con el área de proceso y la práctica específica que corresponda, o indique
NINGUNA"*. Parece de memoria y no lo es. Casi cualquier actividad se puede forzar en dos o tres
áreas, y lo que decide es leer bien **quién** hace **qué**, **sobre qué objeto**, **contra qué** lo
compara y **en qué momento** ocurre. Este capítulo junta los criterios de los capítulos anteriores
en un solo lugar, para consultarlo durante el examen.

### 24.1 El método en cinco preguntas

1. **¿Es de un proyecto o de toda la organización?** Si dice "en el proyecto X", la respuesta está
   entre PP, PMC, REQM, RD, CM, VER, VAL, RSKM y PPQA. Si dice "en la software factory" o "para
   todos los proyectos", lo más probable es OPD, OPF, OT, o MA cuando define cómo se mide en toda
   la organización.
2. **¿Cuál es el objeto?** Un requerimiento, un elemento de configuración, un plan, un producto de
   trabajo, un activo, la formación de la gente. El objeto descarta áreas enteras: un activo nunca
   lo controla VER.
3. **¿Contra qué se compara y quién participa?** Contra la especificación o los artefactos del
   proyecto, por el equipo → **VER**. Con el cliente, contra lo que necesita → **VAL**. Contra un
   estándar de la organización, por alguien externo al proyecto → **PPQA**. Contra una convención
   del propio proyecto → **CM**. Contra el plan → **PMC**.
4. **¿En qué momento está el relato?** El tiempo verbal elige la práctica dentro del área y separa
   áreas vecinas (24.2).
5. **¿La opción tiene la sigla correcta?** Una práctica real con la sigla de otra área es falsa, y
   si ninguna opción encaja, la respuesta es **NINGUNA**.

Un ejemplo de punta a punta. *"Ayer, dos analistas controlaron los casos de uso de otro analista
contra las minutas aprobadas; los hallazgos ya se documentaron; en este momento se almacenan las
identidades de los participantes donde sólo accede Calidad."* Es un proyecto; el objeto es un
producto de trabajo; se compara contra artefactos del proyecto, entre pares: **VER**. Y como la
revisión ya ocurrió, se **protegen los datos**: **VER SP 2.3**. La mención de Calidad es un
distractor.

### 24.2 El tiempo decide la práctica

| Lo que dice el enunciado | Lo que corresponde |
|---|---|
| "Se distribuirá", "será chequeada" (futuro) | **Preparar**: SG 1 de VER o de VAL, o VER SP 2.1 si es una revisión entre pares |
| "Está chequeando", "se realiza un control" (presente) | **Realizar** o **llevar a cabo** |
| "Ya se revisó y se documentó; ahora se almacena…" | **Analizar los datos**: VER SP 2.3 |
| "Previo al inicio"; reunión de lanzamiento **futura** | **PP** |
| "En la última reunión de avance", "respecto a lo planificado" | **PMC** |
| "Se concluyó que la causa es…" / "se determinó reemplazar…" / "ahora se evalúa si funcionó" | **PMC SP 2.1 / 2.2 / 2.3** |
| Un cambio cuyo impacto **todavía se evalúa** / uno **ya aceptado** en trámite | **REQM SP 1.3 / CM SP 2.1** |
| Una mejora **propuesta**, a probar en pilotos / una **ya aceptada**, a desplegar | **OPF SG 2 / SG 3** |

### 24.3 Los pares que se confunden

| Par | Cómo se corta |
|---|---|
| **PPQA / VER** | PPQA controla que el producto **respete el estándar** de la organización; VER, que su contenido **sea correcto** contra lo especificado |
| **PPQA / VAL** | Un checklist del estándar aplicado **antes de entregar**, sin el cliente, es PPQA SP 1.2; con el cliente, VAL |
| **PPQA / CM** | Estándar **de la organización**, controlado por alguien **externo** → PPQA; convención **del propio proyecto** → CM |
| **PPQA / PMC** | Comparar cómo se ejecutaron las tareas contra el **proceso definido** → PPQA SP 1.1; contra **el plan** → PMC |
| **PPQA / OPF** | PPQA **evalúa e informa**; OPF **analiza** esos informes y propone la mejora |
| **OPF / OPD** | OPF **propone, pilotea y despliega**; OPD **crea y deja asentado** el activo |
| **OT / PP SP 2.5** | Capacidades para **la organización** → OT; cursos para la gente **de un proyecto** → PP SP 2.5 |
| **PP SP 1.2 / SP 1.4** | **Tamaño** → SP 1.2; **esfuerzo o costo** derivados del tamaño → SP 1.4 |
| **PP SP 2.3 / MA** | Qué datos se registran **en un proyecto** → PP SP 2.3; cómo se mide **en toda la organización** → MA |
| **MA / OPD** | MA especifica medidas y procedimientos; la **estructura del repositorio** de la organización es OPD SP 1.4 |
| **MA / PMC** | MA produce la medición; **usarla** para corregir el proyecto es PMC |
| **REQM / RD** | RD **produce** requisitos todavía no acordados; REQM **gestiona** los acordados |
| **RD SP 3.5 / VAL** | Validar los **requisitos** antes de construir → RD; el **producto** con el cliente → VAL |
| **VER / OPD** | Pares que revisan un **producto de un proyecto** → VER; un **activo** aún no publicado → OPD |
| **PP / PMC / RSKM** | Riesgos **para el plan** → PP SP 2.2; seguirlos → PMC SP 1.3; fuentes, parámetros, estrategia y planes de mitigación → RSKM |

### 24.4 De la palabra del enunciado al área

La tabla junta las expresiones que se repiten en los finales y en la práctica del AD. No reemplaza al
método: sirve para confirmar una respuesta o para destrabarse cuando dos áreas parecen posibles.

| Lo que aparece en el enunciado | Área / práctica |
|---|---|
| Una plantilla o un procedimiento **para toda la SF** | OPD SP 1.1 |
| Las fases "**desde que nace la idea hasta que el software es retirado**"; aprobar los ciclos de vida | OPD SP 1.2 |
| "**En base a qué características**" se elige un ciclo de vida o una plantilla; pedir una **excepción** | OPD SP 1.3 |
| La **base de datos** de métricas de **todos** los proyectos | OPD SP 1.4 |
| El **sitio de Intranet** con los documentos del proceso | OPD SP 1.5 |
| Herramienta o software **estándar** para todas las PC de la SF | OPD SP 1.6 |
| Comparar los procesos con CMMI; **puntos fuertes y débiles** | OPF SP 1.2 |
| Qué **proyectos piloto** hacen falta para verificar una **propuesta** | OPF SP 2.2 |
| Qué **proyectos en curso** deben incorporar la **reciente modificación** | OPF SP 3.2 |
| Incorporar **lecciones aprendidas** a los activos | OPF SP 3.4 |
| **Conseguir un instructor**; formar a alguien para que capacite a otros | OT SP 1.4 |
| Guía **para todos los proyectos** de cómo y cuándo registrar las horas | MA SP 1.3 |
| Calcular los **puntos función** / las **horas** a partir del tamaño | PP SP 1.2 / SP 1.4 |
| **Cantidad de personas y dedicación** del equipo | PP SP 2.4 |
| **Tabla de roles** con la dedicación de los interesados por fase | PP SP 2.6 |
| Si los usuarios clave **asisten a las reuniones** o **responden los mails** | PMC SP 1.5 |
| Informar el **aumento de probabilidad** de un riesgo respecto de lo planificado | PMC SP 1.3 |
| "**Toda solicitud que no cumpla será devuelta**" | REQM SP 1.1 |
| **Acordar con el Sponsor** que la fecha se corre por un cambio | REQM SP 1.2 |
| **Matriz de trazabilidad** | REQM SP 1.4 |
| Un requisito **vago** que hay que volver medible y confirmar con el cliente | RD |
| **Códigos** de los casos de uso; responsable de cada artefacto | CM SP 1.1 |
| Procedimiento de **back up**; carpetas y permisos del repositorio | CM SP 1.2 |
| Artefactos revisados y acordados como "**basamento**" del desarrollo | CM SP 1.3 |
| Documento con las **diferencias** entre una compilación y la anterior | CM SP 3.1 |
| Personal **externo** controla un artefacto contra las directrices de la SF | PPQA SP 1.2 |
| **Elevar** un informe al Director tras observaciones reiteradas | PPQA SP 2.1 |
| Qué **clases entran en la prueba de integración**; controlar **por inspección** | VER SP 1.1 |
| **Cargar la base de datos de pruebas** | VER SP 1.2 |
| **Distribuir** un caso de uso que **será chequeado**; definir que será un **walkthrough** | VER SP 2.1 |
| Qué casos de uso entran en la **prueba de aceptación** | VAL SP 1.1 |
| Los criterios con los que el cliente da por **cumplido el contrato** | VAL SP 1.3 |

### 24.5 Trampas que ya se tomaron

**Leer la sigla, no sólo el texto.** Si la respuesta es VER y la opción dice "VAL / SP 2.1 Preparar
las revisiones entre pares", la respuesta es **NINGUNA**.

**El área la define la actividad, no el tema.** Elevar al Gerente General un informe porque se
cambian requerimientos sin seguir el circuito de REQM es **PPQA SP 2.1**: lo que se hace es escalar
una no conformidad. Un enunciado que menciona la línea base de requerimientos no es por eso REQM: si
se avisa que aumentó la probabilidad de un problema, es riesgo (PMC SP 1.3).

**Nombrar a Calidad no lo vuelve PPQA.** PPQA aparece cuando se controla la **adherencia a un
estándar o a un proceso** de la organización, no cuando aparece la palabra "Calidad".

**Las pruebas no se reparten por fase.** La aceptación es VAL y la de sistema es VER, aunque las dos
se hagan sobre el producto terminado.

**RSKM casi nunca es la respuesta.** En los finales no aparece, y en la práctica oficial del AD ni
siquiera figuraba entre las opciones. Sólo va cuando el enunciado habla de fuentes, parámetros,
umbrales, estrategia o planes de mitigación.

En algunos enunciados las resoluciones de alumnos dan prácticas distintas, pero casi siempre el
**área** no se discute. Si dos prácticas parecen posibles, elegí la que aparezca entre las opciones.

## 25. Las preguntas BP

En los AD de 2024 y 2025, el formato que más pesó no pide una definición: describe cómo trabaja
una software factory —una política, un procedimiento, una plantilla— y pide decidir si esa práctica
**puede generar problemas de calidad** y **por qué**. Lo que se evalúa es si se entiende **para qué
sirve** cada práctica de CMMI: se muestra una práctica a la que le falta algo, y hay que darse
cuenta de qué falta y qué consecuencia tiene.

### 25.1 El método

1. **Leer la práctica como un proceso**: quién hace qué, contra qué criterio, cuándo y, sobre todo,
   **qué pasa al final**. El problema casi siempre está en la última oración: el escalamiento, el
   archivo, el registro, quién aprueba.
2. **Identificar el área de proceso** con los criterios del capítulo 24.
3. **Buscar el eslabón que falta** (25.3). Si falta uno, **sí** hay problema. "No genera problemas"
   es correcto sólo si la práctica cumple lo que pide el área.
4. **Evaluar cada razón por separado.** Un "Sí… porque X" es correcto sólo si X es **cierto**,
   **ataca el eslabón que falta** y pertenece **al área en juego**.
5. **Aplicar la regla de no mezclar** y recién ahí marcar.

### 25.2 La regla de no mezclar

La consigna lo dice textualmente: pueden elegirse varias opciones, pero **no pueden combinarse** las
que consideran que sí hay problemas de calidad con las que consideran que no. Si se marcan varias,
tienen que ser todas del mismo lado y todas con razones verdaderas. Y si hay un problema pero
ninguna de las razones ofrecidas lo describe, la respuesta es **NINGUNA**, no la menos mala.

> ⚠️ Un "Sí… porque X" con un X falso es tan incorrecto como un "No". Buena parte de los
> distractores dicen "Sí" y fallan en la razón.

### 25.3 Señales de problema por área

| Área | Señales de problema | Lo que falta |
|---|---|---|
| **PPQA** | Evaluador bajo **la misma gerencia** que decide sobre el proyecto · no conformidades que **nadie sigue hasta el cierre** · sin escalamiento · la no conformidad se **archiva o se sanciona** | Independencia · **escalar y seguir hasta la resolución** (SP 2.1) |
| **CM** | Artefactos versionados **sin relación entre sí** · sólo se guarda **la última versión** · documentos en **carpetas personales** · cambios **sin petición** ni autorización · pase a producción **verbal** | **Líneas base** (SP 1.3) · control de cambios (SG 2) · registros (SP 3.1) |
| **PP** | Estimar **sólo por experiencia** · tareas sin EDT · no se planifican **los roles del cliente** · riesgos sin identificar | EDT · estimaciones con datos (SP 1.2, 1.4) · involucración (SP 2.6) |
| **PMC** | Reuniones de avance **sin el cliente** · desvíos que no se analizan | Monitorizar contra el plan · acciones correctivas |
| **REQM** | Cambio pedido **por mail al programador**, que lo acepta solo · **sin análisis de impacto** · sin trazabilidad | Gestionar los cambios (SP 1.3) · trazabilidad (SP 1.4) |
| **RD** | Requisitos **verbales** · el cliente no ve nada hasta la instalación · relevamiento **sin técnicos** | Desarrollar y **validar** los requerimientos |
| **MA** | Se mide **sin objetivo** · factor de productividad **de mercado** nunca recalibrado · métricas para **evaluar personas** | Objetivos (SP 1.1) · uso apropiado de los datos |
| **VER** | El **programador prueba su propio programa** · datos de prueba decididos **al ejecutar** · casos sin resultado esperado · en mantenimiento se prueba **sólo lo modificado** | Procedimientos y criterios · revisiones entre pares · registro |
| **VAL** | La **única** prueba es la del usuario · sin criterios de aceptación acordados | Preparar y realizar la validación |
| **OPF** | Mejoras **comunicadas por mail** y nada más · lecciones aprendidas **archivadas** sin que nadie las consulte | Desplegar · monitorizar la implementación · incorporar experiencias |
| **OPD** | Cada grupo usa **su propia estructura** de documento · sin guías de adaptación | Procesos estándar · guías de adaptación |
| **OT** | Personal **sin formación** en las técnicas que usa la SF · no se mide si la capacitación sirvió | Plan de formación · registros · eficacia |
| **RSKM** | Los riesgos se tratan **cuando ya ocurrieron** | Preparar, identificar y mitigar antes |

Una práctica puede fallar **por defecto** —no se mide nada— o **por exceso o mala aplicación**: se
mide todo sin objetivo, o un proyecto chico completa la plantilla de uno grande porque no hay guías
de adaptación. Las dos formas generan problemas de calidad.

### 25.4 Lo que no es un problema

Hay rasgos que parecen sospechosos y son exactamente lo que pide el modelo. Que haya **testers
dedicados exclusivamente** a probar es la independencia que piden los principios de Myers. Que la no
conformidad se intente resolver **primero dentro del proyecto** es lo que pide CMMI. Que el **líder
de proyecto sea responsable de corregir** es cierto; lo que no puede faltar es que QA siga la no
conformidad y la escale. Un QA **hecho por pares** en una organización chica es válido si se cumplen
las condiciones del capítulo 21. Y que el repositorio sea **por proyecto** no es lo que exige CM.

### 25.5 Los distractores que se repiten

| Patrón del distractor | Por qué es falso |
|---|---|
| "No genera problemas: es una implementación **correcta** (o **completa**) de X" | Justamente le falta un eslabón de X; y a veces X ni siquiera es el área en juego |
| Una razón **de otra área**: "SQA no verifica que se cumplan los requisitos" (VER), "no se guarda en un repositorio organizacional" (OPD) | La razón tiene que atacar la falla del área que se está implementando |
| Una razón **inventada**: "faltan almacenar métricas de las no conformidades escaladas al área de testing" | No es lo que pide el modelo ni lo que falla en el enunciado |
| La **sanción** como solución: "si no las resuelve, es sancionado en su legajo" | Sancionar no resuelve la no conformidad, y usar datos para evaluar personas es un uso inapropiado |
| La **buena comunicación** en lugar del mecanismo | No reemplaza la independencia ni el registro |
| "**No es necesario** definirlo en cada proyecto: está en los manuales de la empresa" | CMMI lo pide por proyecto |

Los tres casos de los AD están resueltos en sus capítulos: el plan de proyecto sin los roles del
cliente (10.2), el versionado sin línea base (20.9) y SQA en sus dos versiones (21.5). Un cuarto, de
un final, completa el cuadro: una software factory con **testers dedicados** que deciden los datos
de prueba al ejecutar **sí** tiene un problema, pero **por los datos, no por los testers**: faltan
casos documentados antes de ejecutar, que además permitan repetir las pruebas en mantenimiento. Una
opción que dijera "Sí, porque los testers no deberían dedicarse sólo a probar" sería falsa aunque el
"Sí" fuera correcto.

> ⚠️ En una recomendación de PPQA, el **escalamiento** no es opcional: es la idea que decidió los BP
> de SQA del AD de 2024 y de 2025.

## 26. Confusiones frecuentes

Para cerrar, las confusiones que más se repiten. No son trucos de examen: cada una es un concepto
mal entendido, y casi todas aparecieron como opción incorrecta en algún parcial o final.

**Sobre la calidad y CMMI.** Creer que asegurar la calidad es probar el producto, cuando las
pruebas son **control** y el aseguramiento es **preventivo** y mira el **proceso**. Confundir el
mantenimiento **perfectivo**, que mejora la calidad interna, con el **evolutivo**, que cambia lo que
el sistema hace. Creer que las prácticas son obligatorias, cuando lo requerido son **sólo las
metas**. Creer que un nivel superior exime de las metas de los anteriores, cuando los niveles son
**acumulativos**: si falla un área de nivel 2, la organización queda en **nivel 1**. Y creerle a las
erratas de la traducción: OT y RSKM son de **nivel 3**.

**Sobre la gestión de procesos.** Confundir OPF con OPD: **OPF diagnostica y despliega, OPD define y
guarda**. Atribuir a MA el repositorio de medidas de la organización, que es de **OPD**. Llamar OT a
la capacitación de la gente de un proyecto, que es **PP SP 2.5**. Y confundir la plantilla de caso
de uso, que es un **activo**, con el caso de uso, que es un **producto de trabajo**.

**Sobre la planificación y los riesgos.** Sumar **duración** donde se pide **esfuerzo**: el esfuerzo
se suma; la duración sale del camino crítico. Confundir **tamaño** (PP SP 1.2) con **esfuerzo** (PP
SP 1.4). Creer que cualquier desvío debe resolverse, cuando PMC actúa sobre los **significativos** y
RSKM, al superar un **umbral**. Creer que el análisis de riesgos va antes que la identificación. Y
confundir **mitigación**, que actúa antes, con **contingencia**, que responde cuando el riesgo ya
ocurrió.

**Sobre los ciclos de vida.** Creer que en un incremental el análisis y la prueba de sistema se
hacen sólo una vez, cuando **cada incremento es una cascada completa**. Confundir incremental, que
agrega pedazos distintos, con iterativo, que **vuelve sobre los mismos** requisitos. Y elegir cascada
con requisitos poco claros, cuando es **el menos adecuado**.

**Sobre los requerimientos.** Creer que los no funcionales son opcionales. Elegir la opción en la
que el equipo **decide solo**, cuando RD exige confirmar con el cliente. Elegir la que **implementa
antes de evaluar el impacto**. Separar REQM de CM por quién pide el cambio, cuando decide si el
cambio **altera un requisito** y en qué **momento** está. Y atribuir las solicitudes de cambio a
REQM, cuando son de **CM** y cubren también defectos.

**Sobre verificación, validación y pruebas.** Creer que las pruebas de sistema son validación porque
se hacen sobre el producto terminado, cuando son **verificación**. Atribuir a VAL las revisiones
entre pares, que existen **sólo en VER**. Creer que probar es demostrar que el programa funciona,
cuando es **buscar errores**. Creer que re-ejecutar los casos que fallaron alcanza, cuando eso es
**confirmación** y falta la **regresión**. Y leer mal el enunciado: "superior a 65" empieza en
**66**, y la inválida de "mayor a cero" es **≤ 0**.

**Sobre la gestión de configuración.** Creer que conservar todas las versiones de cada artefacto es
hacer gestión de configuración, cuando sin **línea base** no se sabe qué versión de cada uno compone
el producto. Dejar afuera las **herramientas** con que se construyó el producto. Contar como release
cada versión interna, cuando release es **lo que se hace público**. Llamar versión a una adaptación
a otra plataforma, que es una **variante**. Y creer que CM exige un repositorio organizacional, que
es de **OPD**.

**Sobre el aseguramiento de la calidad.** Creer que la auditoría termina con el informe, cuando
termina cuando las no conformidades **se resuelven**. Creer que el escalamiento es opcional, o que
archivar el informe o sancionar al líder lo reemplaza. Creer que alcanza con escalar a un gerente
"con quien hay buena comunicación", cuando si también manda sobre los proyectos es **juez y parte**.
Y creer que PPQA verifica requerimientos, cuando evalúa la **adherencia a procesos y estándares**.

**Sobre la medición.** Creer que toda métrica que menciona fases es de proceso, cuando el
cumplimiento de plazos compara plan contra real y es de **proyecto**. Creer que conviene empezar a
medir cuanto antes, cuando primero se **alinea** con los objetivos. Y creer que medir la
productividad de cada desarrollador para premiarlo o sancionarlo es buena práctica.

**Sobre las pericias.** Creer que el perito hace un backup, cuando hace una **imagen forense bit a
bit**. Tomar el disco antes que la memoria, cuando el orden va de **mayor a menor volatilidad**. Y
creer que la cadena de custodia empieza cuando el material llega al perito, cuando arranca en el
**primer contacto** con la evidencia.

## Anexo. Las preguntas de los AD 2024 y 2025

Todas las preguntas de los dos parciales de Aprobación Directa que circulan, con su respuesta y el
criterio que la decide. Cada una está desarrollada en el capítulo que se indica del resumen
completo.

### AD 2024

**Configuración: el año 2002.** Una software factory desarrolla desde 2002 aplicaciones de
escritorio en un lenguaje A; hace dos años sumó apps móviles en un lenguaje B; aplica un estándar de
interfaces desde 2010; sus manuales eran PDF hechos con MS-Word 2002. ¿Qué debería haber quedado
bajo gestión de configuración en 2002? → Lo que **existía entonces y hace falta para reconstruir**
el software: la documentación del sistema, la app de escritorio, su **código fuente**, el **lenguaje
A**, **MS-Word 2002** y los manuales en PDF. Marcar el **lenguaje B** dejó la pregunta en cero:
todavía no existía. (Capítulo 20.)

**Releases mínimos.** Un producto llamado "ALFA 3" se desarrolla con un ciclo incremental de 4
incrementos → **4 releases**: cada incremento se entrega. En cascada sería **1**. El "3" es parte
del nombre. (Capítulos 13 y 20.)

**Supervivencia de un esquema de versión.** Versión `<x>.<y>` de dos dígitos cada uno; `x` cambia
cada trimestre, `y` cada quince días y vuelve a 0 cuando cambia `x` → **24 años**: `y` nunca pasa de
06 o 07 en un trimestre, así que manda `x`, y 99 valores / 4 por año ≈ 24,75. (Capítulo 20.)

**Fin de una auditoría.** "Una auditoría de aseguramiento de la calidad termina cuando…" → **se
resuelven las no conformidades**, no cuando se presenta el informe. (Capítulo 21.)

**BP de SQA.** SQA informa las no conformidades, revisa a los 15 y a los 30 días y, si siguen
abiertas, las reporta al gerente de desarrollo, del que dependen tanto SQA como los líderes de
proyecto → **Sí** genera problemas, porque **SQA debería depender de otra gerencia** para evitar el
conflicto de intereses al escalar. (Capítulo 21.)

**BP de versionado.** Cada artefacto tiene su número de versión independiente y no se guarda la
relación con las versiones de los otros → **Sí** genera problemas, porque **si hay que volver a una
versión anterior no hay información sobre la relación de versiones entre artefactos**: falta la línea
base. "El problema es que no se usa un repositorio organizacional" es **incorrecta**. (Capítulo 20.)

**Requisito de acceso móvil sin dispositivos.** → **Definir una lista** de dispositivos y sistemas
operativos y **confirmarla con el cliente**. Las opciones en que el equipo decide solo son
incorrectas. (Capítulo 14.)

**Requisitos de usabilidad vagos.** → **Reunirse con el cliente para definir métricas** y actualizar
la documentación; no completar con métricas estándar de la industria. (Capítulo 14.)

**Cambio con impacto en la privacidad.** El cliente quiere registrar la navegación de los usuarios →
**consultar con legales y privacidad** y reflejar el impacto en la matriz de trazabilidad.
(Capítulo 15.)

**Cambio que afecta a varios subsistemas.** → **Analizar cómo afecta a los otros subsistemas y
actualizar la matriz de trazabilidad antes de proceder**. La trampa era "registrar, actualizar la
matriz y comenzar la implementación". (Capítulo 15.)

**Métricas de proceso y de proyecto.** (1) cumplimiento de plazos por fase, (2) defectos por fase,
(3) horas planificadas contra reales, (4) tareas a tiempo, (5) tiempo de aprobación de código en
revisiones → **proceso 2 y 5; proyecto 1, 3 y 4**. (Capítulo 22.)

### AD 2025

**Indicadores de un checklist.** De 30 casos de uso auditados, ¿qué indicadores salen del
checklist? → Sólo **"10 casos de uso sin meta"**. Los otros dos no salen, porque ninguna pregunta del
checklist permite contarlos. (Capítulo 21.)

**Verdadero o falso sobre auditorías.** "El trabajo de auditoría termina cuando se presentan las no
conformidades" → **Falso**. "Las no conformidades se intentan resolver a nivel proyecto" →
**Verdadero**. "El escalamiento es un aviso que dice que no hay no conformidades" → **Falso**.
(Capítulo 21.)

**BP de SQA.** Igual que en 2024, pero si la no conformidad sigue abierta el informe se archiva en
"proyectos incumplidores" y queda en el legajo del líder → **Sí** genera problemas, porque **no
contempla un mecanismo para controlar, por un grupo externo, que se resuelvan las no conformidades
hasta su fin, escalándolas** si hace falta. (Capítulo 21.)

**BP del plan de proyecto.** La plantilla pide incluir sólo roles de la software factory, más
responsabilidades de OT, OPF y OPD → **Sí** genera problemas, porque **no contempla que los miembros
del proyecto por parte del cliente sepan qué tienen que hacer**: falta PP SP 2.6. (Capítulo 10.)

**Casos de prueba desde particiones.** ¿Qué se tiene en cuenta al definirlos? → Las **entradas**,
las **salidas esperadas**, el **comportamiento esperado** y la **técnica** a emplear. No: si la
prueba es alfa o beta, quién la ejecuta ni las limitaciones del lenguaje. (Capítulo 18.)

**Afirmaciones sobre medición.** → Son coherentes con MA **sólo la 1, la 3 y la 4**: alinear las
métricas con los objetivos del negocio, documentar cómo y cuándo se toman y quién las analiza, y
medir para tener evidencia objetiva. No lo es "empezar a recopilar ya, sin procedimientos".
(Capítulo 22.)

**Verificación y validación con diagramas.** Con S (especificación), P (producto) y Test (pruebas):
el planteo con las pruebas casi enteras **dentro de S** es **VER**; el que las tiene casi enteras
**dentro de P**, probando el producto real en su entorno, es **VAL**. (Capítulo 16.)
