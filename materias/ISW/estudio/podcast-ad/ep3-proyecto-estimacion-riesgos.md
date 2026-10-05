# Episodio 3: Proyecto, estimación, riesgos y ciclos de vida

> Fuente para el podcast de repaso del parcial de **Aprobación Directa** de Ingeniería y
> Calidad de Software (opción múltiple, a libro abierto en papel). Contiene los capítulos
> 10, 11, 12 y 13 del resumen de estudio `resumen-ad.md`, con su numeración original: las
> referencias a otros capítulos remiten a ese resumen.

## 10. El proyecto y su planificación

Todo proyecto de software arranca con una promesa: un producto, para una fecha, por un costo.
Cumplirla es difícil porque el terreno se mueve —el cliente pide algo nuevo, alguien se enferma, una
estimación resulta optimista—, y la gestión de proyectos existe para que esos imprevistos se manejen
con método y no a pulmón. CMMI le dedica dos áreas de **nivel 2** que son las dos caras de la misma
tarea: **PP** arma el plan y **PMC** lo sigue y lo corrige.

### 10.1 Qué es un proyecto

> **Proyecto:** conjunto de actividades coordinadas y controladas, con **inicio y fin definidos**,
> que crea un producto o servicio **único** conforme a requisitos específicos, dentro de límites de
> tiempo, coste y recursos. Se desarrolla **en pasos**, en lo que se llama elaboración gradual.

Tres precisiones que se derivan de la definición. Un proyecto **siempre tiene fin**: termina cuando
se logran los objetivos o cuando se cancela; lo que no termina no es un proyecto sino una
operación. Los proyectos de software **no son sólo de desarrollo**: existen los de
**mantenimiento** —con los cuatro tipos del capítulo 3— y los de **despliegue o implantación**, y la
categoría cambia qué tareas entran en la planificación. Y tener un diagrama de Gantt **no es tener
un plan de proyecto**: el Gantt es una vista del cronograma, mientras que el plan incluye alcance,
estimaciones, recursos, riesgos, calidad y comunicación.

La contracara del proyecto es el **proceso**, que es **repetitivo y reiterativo y produce siempre
el mismo producto**. Esa repetibilidad es exactamente lo que el proyecto no tiene. Entre los
participantes conviene distinguir al **patrocinador**, que aporta los recursos financieros, del
**cliente o usuario**, que es quien va a usar el producto.

### 10.2 PP — Planificación de proyecto

Su propósito es **establecer y mantener los planes** que definen las actividades del proyecto:
desarrollar el plan, interactuar con las partes interesadas, **obtener el compromiso** con él y
mantenerlo. La planificación arranca **con los requerimientos**, que son los que definen producto y
proyecto. Y **el plan necesitará corregirse**: cambian los requerimientos y los compromisos, y las
estimaciones resultan inexactas. Eso no es un fracaso de la planificación; PP cubre también la
replanificación.

- **SG 1 Establecer estimaciones.** SP 1.1 Estimar el **alcance** del proyecto (la EDT) · SP 1.2
  Establecer las estimaciones de los **atributos** de los productos de trabajo y de las tareas
  (tamaño y complejidad) · SP 1.3 Definir el **ciclo de vida** del proyecto · SP 1.4 Determinar las
  estimaciones de **esfuerzo y de coste**.
- **SG 2 Desarrollar un plan de proyecto.** SP 2.1 Establecer el **presupuesto y el calendario** ·
  SP 2.2 Identificar los **riesgos** del proyecto · SP 2.3 Planificar la gestión de los **datos** ·
  SP 2.4 Planificar los **recursos** del proyecto · SP 2.5 Planificar el **conocimiento y las
  habilidades** necesarios · SP 2.6 Planificar la **involucración de las partes interesadas** · SP
  2.7 Establecer el plan de proyecto.
- **SG 3 Obtener el compromiso con el plan.** SP 3.1 Revisar los planes que afectan al proyecto ·
  SP 3.2 Reconciliar los niveles de trabajo y de recursos · SP 3.3 Obtener el compromiso con el plan.

> ⚠️ La planificación **incluye** estimar las tareas, determinar los recursos e identificar los
> riesgos. **No incluye** el pago a los recursos ni la especificación detallada de la arquitectura
> del software, que corresponde a **TS** (Solución técnica). Y fijate el **alcance** del enunciado:
> la formación o el registro de datos planificados **para un proyecto puntual** son PP (SP 2.5 o SP
> 2.3), no OT ni MA, que trabajan para la organización.

La SP 2.6 decidió una pregunta BP del AD de 2025. La plantilla de plan de proyecto de una software
factory pedía incluir **sólo los roles de la software factory**, más responsabilidades de OT, OPF y
OPD. **Sí** podía generar problemas de calidad, porque los miembros del proyecto por parte del
cliente no sabrían qué tienen que hacer: el plan debe tener los roles de **todas** las partes
interesadas relevantes, y el cliente lo es. Lo de OT, OPF y OPD era un segundo error: son áreas de
la organización, no roles de un proyecto.

### 10.3 PMC — Monitorización y control del proyecto

También es de **nivel 2**, y su propósito es proporcionar una comprensión del progreso del
proyecto para poder tomar **acciones correctivas apropiadas** cuando el rendimiento se desvía
significativamente del plan.

El progreso se mide comparando la calidad de los productos de trabajo, el esfuerzo, el coste y el
calendario **reales contra el plan**, en los **hitos o niveles de control** definidos en la EDT. Si
hay desvío, las acciones correctivas posibles son la **replanificación**, el establecimiento de
**nuevos acuerdos**, o la inclusión de **actividades adicionales de mitigación** dentro del plan
actual.

> **Desvío significativo:** aquel que, si se deja sin resolver, **impide al proyecto cumplir sus
> objetivos**. Por eso es falso que cualquier desvío deba resolverse: el modelo pide criterio, no
> reacción automática.

- **SG 1 Monitorizar el proyecto frente al plan.** SP 1.1 Monitorizar los **parámetros de
  planificación** · SP 1.2 Monitorizar los **compromisos** · SP 1.3 Monitorizar los **riesgos** ·
  SP 1.4 Monitorizar la **gestión de los datos** · SP 1.5 Monitorizar la **involucración de las
  partes interesadas** · SP 1.6 Llevar a cabo **revisiones de progreso** · SP 1.7 Llevar a cabo
  **revisiones de hitos**.
- **SG 2 Gestionar las acciones correctivas hasta su cierre.** SP 2.1 **Analizar** los problemas ·
  SP 2.2 **Llevar a cabo** las acciones correctivas · SP 2.3 **Gestionar** las acciones correctivas.

Dentro de la segunda meta, el tiempo verbal decide la práctica: "analizando la situación se concluyó
que la causa es…" es **SP 2.1**; "se determinó reemplazar al usuario clave", **SP 2.2**; "el cambio
se hizo hace dos semanas y ahora se evalúa si resolvió el problema", **SP 2.3**.

Los **puntos de control y monitoreo se definen durante la planificación**, no durante la
ejecución. En ejecución se usan.

> ⚠️ Para distinguir PP de PMC en un enunciado, fijate dónde está la reunión respecto del momento
> narrado. Si la reunión está **en el futuro** —"para informarlo en la reunión donde se juntará por
> primera vez todo el equipo"— todavía se está planificando: es **PP**. Si la reunión **ya
> ocurrió** —"en la última reunión de avance…"— se está monitorizando: es **PMC**.

### 10.4 Los diez grupos de procesos de gestión

La guía práctica de gestión de proyectos de INTECO organiza el trabajo en diez grupos. Son buenas
prácticas, pero no todos tienen que estar presentes en cada proyecto. Vale la pena tener presente a
cuál pertenece cada proceso, porque los ejercicios juegan con procesos que suenan a un grupo y
pertenecen a otro.

| Grupo | Procesos |
|---|---|
| **Coordinación** | Iniciar el proyecto · Desarrollar el plan · Gestionar la ejecución · Supervisar el trabajo · Control integrado de cambios · Cerrar el proyecto |
| **Alcance** | Definir el alcance · **Definir las actividades** · Controlar y verificar el alcance |
| **Tiempo** | Establecer la secuencia de actividades · Estimar la duración · Desarrollar el cronograma · Controlar el cronograma |
| **Costes** | Estimar los costos · Elaborar los presupuestos · Controlar los costos |
| **Calidad** | Planificar la calidad · Aseguramiento de calidad · Control de calidad |
| **Recursos** | Planificar los recursos · Controlar los recursos |
| **Personal** | Definir el equipo del proyecto · Gestionar el equipo |
| **Comunicación** | Planificar las comunicaciones · Gestionar la información y los interesados |
| **Riesgos** | Planificar la gestión · Identificar · Analizar · Planificar la respuesta · Controlar |
| **Adquisiciones** | Planificar las adquisiciones · Planificar la contratación · Solicitar respuesta a proveedores · Seleccionar proveedores · Administrar el contrato · Cerrar el contrato |

Tres detalles que se preguntan. **Definir las actividades** pertenece a **Alcance**, no a Tiempo,
aunque suene a cronograma. **Desarrollar el cronograma** debe identificar explícitamente el
**camino crítico**, que es el de mayor duración en la red de actividades, y de ahí salen las
actividades críticas y los hitos. Y **definir el equipo del proyecto** consiste en determinar
**roles y responsabilidades**; no incluye estimar el esfuerzo por rol ni controlar el cronograma.
Además, *elaborar los presupuestos* debe incluir **reservas para contingencias**, y *cerrar el
proyecto* vale tanto para el completado como para el cancelado.

### 10.5 La EDT, las precedencias y el esfuerzo

La secuencia de trabajo es siempre la misma: se arma la **EDT**, se identifican las **tareas
típicas** del ciclo de vida elegido, y se establecen las **órdenes de precedencia** entre ellas.

> **EDT (estructura de desglose del trabajo):** descomposición del proyecto en **paquetes de
> trabajo** manejables, que sirve de base para asignar esfuerzo, calendario y responsables.

La EDT **lista** las tareas —verbos concretos: "Analizar módulo A", no "Análisis"—; el orden y las
dependencias van en el cronograma. Al leer una red de tareas, una **predecesora directa** es la
inmediatamente anterior: si A precede a B y B precede a C, A **no** es predecesora directa de C,
aunque tenga que ocurrir antes. Y los **módulos independientes arrancan en paralelo**: si un
producto se compone de tres módulos independientes, las tareas que dan inicio al proyecto son
**tres**, una de análisis por módulo.

> ⚠️ **Esfuerzo y duración no son lo mismo y no se suman igual.** El **esfuerzo** se mide en
> días-persona u horas-persona y **se suma**. La **duración** se mide en días o meses y **no se
> suma**: sale del **camino crítico**, porque las tareas independientes corren en paralelo. Dos
> tareas de 4 y 5 semanas suman siempre 9 semanas de esfuerzo, pero duran 9 si van en secuencia y 5
> si van en paralelo. Por eso reordenar tareas cambia la duración, no el esfuerzo. Cuando un
> ejercicio pide esfuerzo, hay que leer la columna de esfuerzo y convertir: 1 día-persona = 8 horas.

> **Hito:** evento en el que se planea una entrega relevante o se requiere una decisión.

Un hito bien redactado es **un producto terminado o una aprobación**: "especificación de requisitos
aprobada", "sistema instalado y aceptado". Los **puntos de control**, en cambio, se ubican **en
función de los riesgos**: más controles donde es más probable que algo salga mal, y siempre antes de
que la etapa termine, con margen para corregir.

## 11. La estimación del esfuerzo

Estimar es decidir cuánto va a costar algo que todavía no existe. La materia presenta cuatro
métodos, que no compiten entre sí: se usan en momentos distintos y con información distinta.

El **valor esperado**, o **técnica de tres puntos**, estima cada tarea en tres escenarios
—optimista, normal y pesimista— y los combina en un único valor. La ponderación más difundida le da
peso cuatro al escenario normal: `(O + 4N + P) / 6` (conocimiento general). Es rápida y sirve
cuando la incertidumbre está acotada.

**Delphi** es una estimación **grupal e independiente de expertos**: cada uno vuelca su
perspectiva en números sin ver la del resto. Es **iterativa**, y en cada vuelta se suma
información buscando la **convergencia**. Sirve cuando no hay datos históricos pero sí gente con
experiencia.

Los **puntos de función** miden el tamaño del software desde una perspectiva funcional,
independiente de la tecnología. Son una medida **indirecta del tamaño**, no del esfuerzo: el
esfuerzo se deriva después. Los **puntos de historia** son la estimación relativa de las
metodologías ágiles.

Un consejo que la cátedra repite: **tomar nota de las decisiones tomadas**, sobre todo en la etapa
de estimación. Es lo que después permite explicar un desvío en PMC en lugar de improvisar una
justificación.

### 11.1 Del tamaño al esfuerzo

Los puntos función, las líneas de código o la cantidad de requerimientos miden **tamaño**. Para
llegar a horas hace falta un **indicador de productividad** —puntos función por mes, horas por punto
función— sacado de **proyectos similares**: promediar proyectos que no se parecen da un indicador
que no sirve para ninguno.

> ⚠️ **Tamaño no es esfuerzo**, y en CMMI son prácticas distintas. "Se cuentan las entradas,
> salidas, consultas y ficheros y se obtienen 320 PF" es **PP SP 1.2**. "Con la productividad
> histórica de 12 PF por mes, el desarrollo lleva 26,7 meses-persona" es **PP SP 1.4**.

### 11.2 La distribución 40-20-40

Es una regla de reparto del esfuerzo total de un proyecto: **40 % análisis y diseño** —de los
cuales 10 a 15 puntos van al análisis y 25 a 30 al diseño—, **20 % codificación** y **40 %
pruebas**.

La lectura que importa no es el número exacto sino su consecuencia: **codificar es apenas la
quinta parte del proyecto**, y se prueba tanto como se analiza y diseña junto.

### 11.3 Análisis de puntos función

El APF mide el tamaño del software **entregado al usuario**. Como los puntos función de un sistema
no cambian con el lenguaje ni la plataforma, sirven para **comparar productividad** entre
herramientas u organizaciones, y para **seguir los cambios de alcance**: si los puntos función
medidos van creciendo de una fase a otra, hubo cambios de alcance. La guía lo describe en dos
etapas: primero se identifican y clasifican las funciones, y después se ponderan y se ajusta el
total.

**Identificar y clasificar.** Se fija el **límite del sistema**, que determina qué queda adentro y
qué es externo, y se reconocen cinco componentes: **entradas** (datos que cruzan el límite hacia
adentro), **salidas** (datos que lo cruzan hacia afuera), **consultas** (combinación de entrada y
salida para obtener datos), **ficheros lógicos internos** o FLI (datos que residen dentro de la
aplicación y son actualizados por las entradas) y **ficheros de interfaz externos** o FIE (datos que
residen fuera y son mantenidos por otra aplicación).

**Ponderar.** La complejidad se establece por la diversidad de atributos en tipo y cantidad: en las
transacciones se cruzan los **ficheros referenciados** con los **tipos de datos**; en los ficheros,
los **elementos de registro** con los tipos de datos. Con más de cada cosa, la complejidad sube de
baja a media y a alta. Cada componente se multiplica por el peso de su complejidad:

| Componente | Baja | Media | Alta |
|---|:---:|:---:|:---:|
| Entradas | 3 | 4 | 6 |
| Salidas | 4 | 5 | 7 |
| Consultas | 3 | 4 | 6 |
| Ficheros internos (FLI) | 7 | 10 | 15 |
| Ficheros externos (FIE) | 5 | 7 | 10 |

La suma da los **PFD**, puntos función sin ajustar.

**Ajustar.** El factor de ajuste incorpora características no funcionales del entorno. Se califican
**14 características** de 0 a 5 —comunicaciones de datos, procesamiento distribuido, rendimiento,
utilización masiva, tasa de transacción, entrada de datos on-line, eficiencia para el usuario,
actualización on-line, procesamiento complejo, reutilización, facilidad de instalación, facilidad de
operación, puestos múltiples y facilidad de cambio—. La suma de los 14 valores es el **TDI**, que va
de 0 a 70:

```
Factor de ajuste = (65 + TDI) / 100
PF ajustados     = PFD × Factor de ajuste
```

Con el TDI entre 0 y 70, el factor va de **0,65 a 1,35**: el ajuste puede mover el tamaño estimado
hasta un 35 % para cada lado. Por ejemplo, 200 PFD con un TDI de 42 dan un factor de 1,07 y **214
PF**.

### 11.4 Puntos función de una mejora

La guía avanzada mide también **mejoras**, es decir, cambios sobre un sistema que ya existe. Cada
función afectada mide sus puntos función sin ajustar multiplicados por un **factor de impacto**:
una función **añadida** vale 1; una **eliminada**, 0,4; una **modificada**, entre 0,25 y 1,5 según
el porcentaje de cambio, que sale de una tabla. En el ejemplo de la guía, un informe de 5 PF con un
factor de impacto de 0,75 mide **3,75 PF** de mejora.

```
PFM = (añadidos + modificados) × FA después + eliminados × FA antes
```

> ⚠️ El factor de ajuste de **después** de la mejora se aplica a lo **añadido y modificado**; el de
> **antes**, a lo **eliminado**.

Las siglas del glosario, que también entra: **PFD** (puntos función sin ajustar), **PFDM** (sin
ajustar de la mejora), **PFM** (de la mejora) y **PFP** (de las pruebas, que miden aparte las
funciones del sistema mejorado que intervienen en las pruebas). Un **fichero referenciado** es un
FLI leído o modificado por una transacción, o un FIE leído por ella.

## 12. La gestión de riesgos (RSKM)

Todo proyecto convive con cosas que pueden salir mal: el único que conoce la base de datos renuncia,
el proveedor entrega tarde, el cliente descubre a mitad de camino que necesitaba otra cosa. En nivel
2 el proyecto ya **identifica** riesgos al planificar (PP) y los **monitoriza** durante la ejecución
(PMC), pero en general **reacciona** cuando se materializan. La gestión de riesgos es el paso
siguiente: prepararse, prevenir y mitigar de forma **sistemática**, porque detectar un riesgo
temprano es más fácil, más barato y menos dañino que corregir sus efectos en una fase tardía.

> **Propósito de RSKM:** identificar los problemas potenciales **antes de que ocurran**, para que
> las actividades de tratamiento de riesgos puedan planificarse e invocarse según sea necesario,
> para mitigar los impactos adversos en el logro de los objetivos.

Es un proceso **continuo** que mira hacia adelante, y necesita un entorno de **divulgación libre**:
se identifican riesgos, no culpables. Es de **nivel 3**; la carátula de la traducción que dice
nivel 2 es una errata.

### 12.1 Qué es un riesgo

> **Riesgo de un proyecto:** evento o condición **incierto** que, si ocurre, tiene un efecto
> **positivo o negativo** sobre al menos un objetivo del proyecto: tiempo, coste, alcance o calidad.

Tiene tres componentes: un **evento**, su **probabilidad** y su **consecuencia** o impacto. Y la
definición trae una sorpresa que se pregunta: un riesgo **también puede ser una oportunidad**.
Los riesgos pueden ser **conocidos**, que se identifican y planifican, o **desconocidos**, que se
cubren con una reserva; e **internos**, controlables por el equipo, o **externos**, como una ley
nueva o una huelga.

### 12.2 Metas y prácticas

CMMI divide la gestión de riesgos en tres partes, que son sus tres metas: prepararse, identificar y
analizar, y mitigar.

- **SG 1 Preparar la gestión de riesgos.** SP 1.1 Determinar las **fuentes y las categorías** de los
  riesgos · SP 1.2 Definir los **parámetros** de los riesgos (probabilidad, consecuencia y
  **umbrales**) · SP 1.3 Establecer una **estrategia** de gestión de riesgos.
- **SG 2 Identificar y analizar los riesgos.** SP 2.1 **Identificar** los riesgos · SP 2.2
  **Evaluar, categorizar y priorizar** los riesgos.
- **SG 3 Mitigar los riesgos.** SP 3.1 Desarrollar los **planes de mitigación** · SP 3.2
  **Implementar** los planes de mitigación.

> ⚠️ El orden es **identificar → analizar → priorizar**. Es falso que "el análisis de riesgos es
> previo a su identificación": un riesgo tiene que estar identificado antes de poder analizarse. Y
> los riesgos se identifican **desde la planificación** del proyecto.

### 12.3 Umbrales, mitigación y contingencia

Los **umbrales** son lo que separa "anotar el riesgo" de "actuar". Con ellos, un riesgo puede quedar
**aceptado**, cuando es demasiado bajo para justificar una mitigación formal o no hay forma de
reducirlo —y entonces la razón **debe documentarse**—, o **vigilado**, cuando hay límites objetivos
y documentados que, al superarse, activan el plan de mitigación o el de contingencia.

> ⚠️ Por eso es **falso** que "cualquier desvío en un riesgo habilita actividades de tratamiento":
> se actúa al **superar el umbral**. Es la misma lógica del desvío significativo de PMC.

La **mitigación** actúa **antes** de que el riesgo ocurra, para reducir su probabilidad o su
impacto. La **contingencia** responde **después**, cuando el riesgo ocurre a pesar de todo. Las dos
se planifican de antemano. Ante el riesgo de que renuncie el único DBA, capacitar desde ahora a un
segundo DBA es **mitigación**; dejar previsto que, si renuncia, se contrata a una consultora es
**contingencia**.

Para decidir qué hacer con cada riesgo, las dos fuentes de la materia usan listas que no coinciden,
y eso se presta a trampas. Para **CMMI**, aceptar es reconocer el riesgo **sin tomar ninguna
acción**, y transferir es **reasignar requerimientos**. Para **INTECO**, la aceptación puede ser
pasiva o **activa** —con una reserva y un plan de contingencia—, y transferir es trasladar el
impacto a un **tercero**: seguros, garantías, contratos. INTECO agrega estrategias para las
oportunidades: explotar, compartir y mejorar.

### 12.4 El proceso y las reservas según INTECO

La guía práctica de gestión de riesgos baja todo esto a seis actividades, que se actualizan durante
todo el proyecto, y en todas la responsabilidad final es del **jefe de proyecto**. Se arma el **plan
de gestión de riesgos**, que dice **cómo** se va a gestionar —ojo: **no contiene los planes de
respuesta** de cada riesgo—. Se **identifican** los riesgos en un **registro de riesgos**, con
técnicas como la tormenta de ideas, **Delphi** o las listas de control. Se **analizan**: el análisis
**cualitativo** cruza probabilidad e impacto en una matriz que da la prioridad, y el
**cuantitativo** calcula el **valor esperado = probabilidad × impacto**. Se **planifica la
respuesta**, con un **propietario** por riesgo y los **riesgos residuales** que quedan después de
ella. Y se **controla** y se **cierra** registrando las lecciones aprendidas.

Responder a un riesgo cuesta, y la guía distingue de dónde sale ese dinero. La **reserva de
contingencia** cubre el valor esperado de los riesgos **aceptados** y **residuales**, es decir, de
riesgos conocidos. La **reserva de gestión** cubre los **desconocidos**. Y el costo de evitar,
transferir o mitigar **no va a ninguna reserva**: va al **presupuesto**, porque se sabe cuánto cuesta.
Un riesgo con probabilidad 0,70 y un impacto de $20.000 tiene un valor esperado de $14.000; si se
acepta, ese monto suma a la reserva de contingencia.

### 12.5 Riesgos en PP, PMC y RSKM

Las tres áreas hablan de riesgos, y es uno de los cortes más finos al reconocer el área de un
enunciado.

| Actividad del enunciado | Área / práctica |
|---|---|
| Identificar riesgos **para armar el plan** y obtener el acuerdo de los interesados sobre ellos | **PP SP 2.2** |
| Revisar los riesgos **contra los del plan** y **comunicar su estado** | **PMC SP 1.3** |
| Definir fuentes, parámetros, umbrales o la estrategia; armar o ejecutar los planes de mitigación | **RSKM** |

Dos ítems de la práctica oficial para el AD muestran el corte. "Informar a los stakeholders que
aumentaron las chances, respecto de lo planificado, de que un módulo no pueda desarrollarse; aún es
posible resolverlo" es **PMC SP 1.3**: se compara contra el plan y el riesgo todavía no ocurrió; si
ya hubiera ocurrido, sería un problema, PMC SP 2.1. "Previo al inicio del desarrollo, revisar con el
cliente si están de acuerdo con el impacto documentado para los riesgos" es **PP SP 2.2**: es
planificación.

En los verdadero o falso del tipo "¿es un riesgo posible en este proyecto?", un riesgo con impacto
positivo o de baja probabilidad **sigue siendo un riesgo posible**; la afirmación es falsa sólo si el
enunciado **lo descarta**. Y en formato BP, una software factory que registra los riesgos recién
cuando el problema aparece **sí** tiene un problema de calidad: es la postura reactiva que RSKM viene
a superar.

## 13. Los ciclos de vida

Elegir un ciclo de vida es decidir **cuándo** se hace cada cosa, y esa decisión determina cuándo
se detectan los defectos y cuánto cuesta corregirlos.

> **Ciclo de vida:** conjunto de fases por las que pasa el sistema **desde que nace la idea inicial
> hasta que el software es retirado o reemplazado**.

Quién lo decide depende del alcance: elegir el ciclo de un proyecto es **PP SP 1.3**; establecer
las opciones de ciclos de vida de toda la organización es **OPD SP 1.2**, y fijar con qué criterio se
elige entre ellas, **OPD SP 1.3**.

| Ciclo | Cómo funciona | Cuándo conviene |
|---|---|---|
| **Cascada** | Cada etapa espera a que termine la anterior. Las pruebas van al final | Requerimientos **conocidos y estables**; proyectos cortos; mantenimiento correctivo corto. Es **el que menos sirve con requerimientos inestables** |
| **Modelo en V** | Cada etapa de desarrollo tiene su **nivel de prueba asociado**, planificado desde el comienzo | Cuando se quiere detectar defectos temprano sin abandonar la estructura secuencial |
| **Incremental** | Secuencias lineales escalonadas; cada una entrega un **incremento operativo**. Cada incremento es una mini-cascada completa | Cuando hay que **salir a producción antes** de tener todo terminado |
| **Iterativo** | Varias pasadas sobre el producto; en cada una se **refinan los mismos** requisitos | **Requerimientos poco claros o no estabilizados** |
| **Espiral** | Vueltas con **análisis de riesgos** explícito; las características **evolucionan** con prototipos | Proyectos largos, caros o riesgosos, cuando el equipo **no puede especificar por adelantado** |
| **Prototipado** | **Diseño rápido** de lo visible para el usuario, evaluación del cliente, refinamiento | El cliente define objetivos generales pero **no los requisitos detallados**. Reduce el riesgo de **subestimar el esfuerzo** |

La desventaja crítica de la cascada es que concentra las pruebas al final, de modo que los
defectos se detectan cerca de la implementación, que es donde más caro sale corregirlos. El modelo
en V nace como respuesta: la aceptación se apoya en los requisitos de usuario, la prueba de sistema
en la especificación, la de integración en el diseño, y las unitarias en el código.

Incremental, iterativo y espiral se confunden porque los tres repiten. En el **incremental** cada
incremento es un **pedazo distinto** del producto que se pone en funcionamiento; en el **iterativo**
cada vuelta retoma **los mismos** requisitos para mejorarlos. Y entre incremental y espiral la
diferencia es la **incertidumbre**: el incremental parte de que se conoce el problema y lo divide;
el espiral la asume alta y la gestiona con análisis de riesgos.

> ⚠️ Como cada incremento es una cascada completa, **el análisis se hace en todos los
> incrementos** y **las pruebas de sistema también**, no solamente en el último. Y como cada
> incremento se entrega, un incremental de cuatro incrementos tiene como mínimo **cuatro
> releases**, mientras que una cascada tiene **uno** (capítulo 20).

En los ejercicios el ciclo hay que **justificarlo con elementos del enunciado**. Según el
cuestionario de la cátedra, lo que incide en la elección es la **estabilidad de los
requerimientos** y la **necesidad de poner algo en producción antes de terminar**; el presupuesto,
la cantidad de recursos y el lenguaje, no. Con requisitos incompletos, la cascada es el menos
adecuado: el riesgo de no haberlos entendido se materializa al final, cuando el cliente ve el
producto. Un dato que se tomó: en una cascada, el **manual de usuario** se confecciona en la fase de
prueba, a partir de las interfaces y los casos de uso.
