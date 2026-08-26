# Banco de exámenes

> **SIM · UTN-ISI**
>
> Los quince exámenes de Simulación que hay en el archivo de la cátedra, transcriptos y en un solo
> lugar: seis parciales, un globalizador y cinco finales, de 2015 a 2025. Los que estaban como foto
> o PDF escaneado se transcribieron con lectura de imagen.

## Cómo leer este banco

**Cuatro exámenes traen las respuestas** del alumno que los rindió: los parciales 2021-10-23 y
2021-12-02, el final 2020-08-06 y el parcial 2025 (marcado a mano). Los demás son solo las
consignas.

> ⚠️ **Las respuestas incluidas NO son la corrección de la cátedra: son lo que contestó un alumno, y
> varias están mal.** Los errores detectados, contrastando contra el apunte oficial de Weitz y el
> original de Law:
>
> - **Costos de inventario**: el parcial 2021-12-02 (P5) intercambia $h$ y $\pi$, y también $i$ con
>   $Z$. Lo correcto: **$h$ (holding) va con $I^+$**, lo que tenés guardado; **$\pi$ va con $I^-$**,
>   lo que debés. Y en $K + iZ$, **$i$ es el costo unitario y $Z$ la cantidad**.
> - **Tiempos entre arribos**: el parcial 2021-12-02 (P2 y P3) dice que siguen una distribución de
>   Poisson. **Poisson cuenta eventos** (es discreta); **exponencial mide el tiempo entre ellos** (es
>   continua). Lo correcto: el *número* de arribos es Poisson, el *tiempo entre* arribos es exponencial.
> - **Parcial 2025**: entre las marcadas a mano, la 2.1 da por verdadero que la simulación reemplaza
>   a la solución analítica —la teoría dice lo contrario— y la 2.9 C da por vigente el método de la
>   parte media del cuadrado, que el propio apunte descarta por caer en ciclos cortos.
> - **Generador congruencial**: el parcial 2021-12-02 (P1) escribe $a = 7^5 = 1608$. El valor
>   correcto es $7^5 = 16807$.

**Formato de los parciales**: hasta 2024, diez consignas de desarrollo corto. El de **2025 cambió a
multiple choice** (15 preguntas de opción múltiple + 17 de verdadero/falso) más un ejercicio
numérico de inventario. Es el formato más reciente y conviene tenerlo presente.

---

## Parcial 2025-10-04  ·  32 preguntas multiple choice + ejercicio de inventario

> **Respuestas incluidas:** sí, marcadas a mano por un alumno (⚠ con errores)

**[404] Examen Parcial de Simulación. Apellido y Nombre:** ██████████ *(tachado con marcador verde)*

---

**1.1  Preg.** ¿Qué propiedad caracteriza a una variable aleatoria geométrica?
- A Representa el número de ensayos necesarios para obtener el primer éxito
- B Su media es $1/p$ y su varianza es $(1-p)/p^2$
- C Es la suma de variables aleatorias de Bernoulli independientes
- **D Las opciones A y B son correctas** *(marcada)*
- E Todas las opciones anteriores son correctas

**1.2  Preg.** En el sistema de colas de un solo servidor, ¿cuáles son las tres medidas de rendimiento principales que se estiman?
- A Tiempo promedio de servicio, número promedio de clientes en el sistema, utilización del servidor
- B Retraso promedio en cola, número promedio de clientes en cola, proporción de tiempo que el servidor está ocupado
- C Tiempo promedio de llegada, tiempo promedio de salida, longitud promedio de la cola
- D Solo el retraso promedio en cola y la utilización del servidor
- **E Las opciones A y B son correctas** *(marcada)*

**1.3  Preg.** En el sistema de inventario, ¿qué representa la política (s, S)?
- A Una política donde se ordena una cantidad fija s cuando el inventario llega a S
- B Una política donde se ordena hasta S si el inventario I es menor que s, y no se ordena nada si $I \geq s$
- C Una política donde se ordena s unidades cada S períodos
- D Una política que asegura que el inventario siempre está entre s y S unidades
- **E Las opciones B y D son correctas** *(marcada)*

**1.4  Preg.** Según el texto, ¿cuál es la definición de un sistema en el contexto de simulación?
- A Un conjunto de ecuaciones matemáticas que describen un proceso
- B Una colección de entidades que actúan e interactúan juntas hacia el logro de algún fin lógico
- C Un modelo computacional que imita el comportamiento de un proceso real
- D Un algoritmo que genera números aleatorios para simular eventos
- **E Todas las opciones anteriores son correctas** *(marcada)*

**1.5  Preg.** En un proceso de Poisson homogéneo con tasa $\lambda$, ¿cuál de las siguientes condiciones define correctamente el proceso?
- A $N(0) = 0$ y los números de eventos en intervalos disjuntos son independientes
- B La distribución del número de eventos depende solo de la longitud del intervalo
- C $\lim P\{N(h) = 1\}/h = \lambda$ cuando $h \to 0$
- **D Todas las opciones anteriores son correctas** *(marcada)*
- E Solo las opciones A y C son correctas

**1.6  Preg.** En los modelos de colas con población de clientes finita, la tasa de llegada...
- **A ...varía con el tiempo** *(marcada)*
- B ...aumenta conforme aumenta el número de clientes en el sistema.
- C ...disminuye conforme aumenta el número de clientes en el sistema
- D ...es constante
- E Las opciones A y C son correctas

**1.7  Preg.** ¿Qué representa la intensidad de tráfico ($\rho$) en un sistema de colas?
- A El número promedio de clientes en el sistema
- **B El cociente de la tasa de llegadas ($\lambda$) entre la tasa de servicio ($\mu$)** *(marcada)*
- C El tiempo promedio de espera en la cola
- D La probabilidad de que el sistema esté vacío
- E Las opciones B y D son correctas

**1.8  Preg.** ¿Qué condición debe cumplirse para que un sistema M/M/1 alcance el estado estable?
*(el número "1.8" queda cortado en el borde izquierdo de la foto; se deduce por secuencia)*
- A La tasa de llegadas debe ser mayor que la tasa de servicio

*(la pregunta 1.8 continúa en la hoja derecha)*

*(continuación de 1.8)*
- **B La tasa de servicio ($\mu$) debe ser mayor que la tasa de llegadas ($\lambda$)** *(marcada)*
- C El número de servidores debe ser mayor que 1
- D La capacidad del sistema debe ser finita
- E Las opciones A y C son correctas

**1.9  Preg.** ¿Cuál es la principal ventaja de usar el enfoque "next-event time advance" en simulación?
- A Proporciona mayor precisión en los cálculos
- B Permite saltar períodos de inactividad, ahorrando tiempo de computación
- C Es más fácil de programar que otros enfoques
- D Genera resultados más estables
- **E Las opciones B y C son correctas** *(marcada)*

**1.10  Preg.** ¿Cuál es la principal diferencia entre la verificación y la validación del modelo en un estudio de simulación?
- A La verificación comprueba que el modelo funcione correctamente, mientras que la validación compara el modelo con la realidad
- B La verificación se realiza antes de la validación
- C La verificación utiliza información de entrada real, mientras que la validación utiliza datos simulados
- D La verificación es opcional, mientras que la validación es obligatoria
- **E Las opciones A y B son correctas** *(marcada)*

**1.11  Preg.** En el mecanismo de avance de tiempo "next-event time advance", ¿qué sucede con los períodos de inactividad?
- A Se procesan paso a paso con incrementos fijos de tiempo
- **B Se saltan completamente, avanzando directamente al siguiente evento** *(marcada)*
- C Se simulan con mayor detalle para obtener mayor precisión
- D Se registran pero no se procesan
- E Las opciones A y C son correctas

**1.12  Preg.** ¿Cuál es la relación entre las variables aleatorias binomial y Poisson cuando n es grande y p es p[equeño]? *(el final de la línea queda cortado en el borde derecho de la foto)*
- A La distribución binomial se aproxima a la distribución Poisson con parámetro $\lambda = np$
- B Ambas distribuciones tienen la misma varianza
- C La distribución Poisson es siempre una aproximación exacta de la binomial
- D Solo cuando $n > 100$ y $p < 0.1$
- **E Las opciones A y D son correctas** *(marcada)*

**1.13  Preg.** En un proceso de Poisson no homogéneo, ¿qué característica lo diferencia del proceso hom[ogéneo]? *(cortado en el borde derecho)*
- **A La tasa $\lambda$ varía en función del tiempo** *(marcada)*
- B Los intervalos entre eventos no son exponenciales
- C La propiedad de incrementos independientes no se mantiene
- D Las opciones A y B son correctas
- E Todas las opciones anteriores son correctas

**1.14  Preg.** En el contexto de simulación, ¿cuál es el propósito principal de los "números aleatorio[s]"? *(cortado en el borde derecho)*
- A Generar valores de variables aleatorias con distribuciones arbitrarias
- B Simular posibles ocurrencias del modelo probabilístico
- C Proporcionar la base para estudios de simulación
- D Las opciones A y B son correctas
- **E Todas las opciones anteriores son correctas** *(marcada)*

**1.15  Preg.** ¿Cuál es el segundo paso en un estudio de simulación?
- A Recolección y análisis de datos
- **B Generación del modelo de simulación base** *(marcada)*
- C Validación del modelo
- D Determinación de escenarios
- E Las opciones A y B son correctas

**2.1  Preg.** La simulación reemplaza a la solución analítica como método de resolución de problemas complejos con solución.
- **V Verdadero** *(marcada)*
- F Falso

**2.2  Preg.** Para poder simular es necesario contar con información de funcionamiento de la realidad o estimaciones del mismo.
- **V Verdadero** *(marcada)*
- F Falso

**2.3  Preg.** Un modelo es un recorte de características observables de la realidad y solo puede ser usado si está totalmente testeado.
- V Verdadero
- **F Falso** *(marcada)*

**2.4  Preg.** Para la construcción de modelos es necesario herramientas informáticas siempre.
- V Verdadero
- **F Falso** *(marcada)*

**2.5  Preg.** La simulación por computadora surgió en los últimos 30 años.
- V Verdadero
- **F Falso** *(marcada)*

**2.6  Preg.** La programación orientada a objetos no es imprescindible para realizar simulaciones.
- V Verdadero
- **F Falso** *(marcada)*

**2.7  Preg.** La solución analítica es exacta.
- **V Verdadero** *(marcada)*
- F Falso

**2.8  Preg.** LaTeX es un sistema de composición de textos, orientado a la creación de documentos escritos que presenten una alta calidad tipográfica. Por sus características y posibilidades, es usado de forma especialmente intensa en la generación de artículos y libros científicos que incluyen, entre otros elementos, expresiones matemáticas.
- **V Verdadero** *(marcada)*
- F Falso

**2.9  Preg.** Sobre los números pseudoaleatorios...
- **A Se generan de manera secuencial con un algoritmo determinístico.** *(marcada)*
- **B Se denomina de ciclo completo cuando el conjunto de números pseudoaleatorios generados repite siempre el mismo número, luego de generar un gran conjunto de números distintos.** *(marcada)*
- **C El método de la parte media del cuadrado es un método vigente para la generación de números pseudoaleatorios.** *(marcada)*
- D Los números pseudoaleatorios pueden generarse con cualquier computadora a altas velocidades.

**2.10  Preg.** Verdaderos números aleatorios.
- **A Es preferible en simulaciones de alto rendimiento usar un conjunto de números aleatorios y no pseudoaleatorios.** *(marcada)*
- **B En general los números aleatorios se basan en alguna fuente de aleatoriedad física que puede ser teóricamente impredecible (cuántica) o prácticamente impredecible (caótica).** *(marcada)*

**2.11  Preg.** Los modelos de la cola simple y de inventario empleados durante los TPI de clase...
*(el número queda cortado en el borde izquierdo de la foto; se deduce por secuencia)*
- **A Son modelos simples que pueden ser simulados y que también se cuenta con la solución analítica de los mismos.** *(marcada)*
- B Solo pueden ser simulados si se tiene la solución analítica.
- C La solución analítica puede ser comparada con las respuestas obtenidas de las simulaciones.
- D Las respuestas obtenidas mediante simulaciones son generalmente similares al de la solución analítica.

**2.12  Preg.** Los eventos a tratar en el modelo de cola simple, en el paradigma de simulación basado en eventos discretos, son...
*(el número queda cortado en el borde izquierdo de la foto; se deduce por secuencia)*
- **A Arribo.** *(marcada)*

*(la pregunta 2.12 continúa en la hoja derecha)*

*(continuación de 2.12)*
- **B Partida.** *(marcada)*
- C Inicio.
- D Finalización.
- **E Poner el servidor ocupado/desocupado.** *(marcada)*

**2.13  Preg.** Las medidas de rendimiento más importantes a calcular en el problema de cola simple son...
- **A Tiempo de espera en el servidor.** *(marcada)*
- **B Tiempo de arribo.** *(marcada)*
- C Cantidad de veces que el cliente paso por el servidor.
- **D Utilización del servidor.** *(marcada)*

**2.14  Preg.** Si la tasa de arribos es mayor que la tasa de servicio no es posible realizar la simulación.
- V Verdadero
- **F Falso** *(marcada)*

**2.15  Preg.** Si la tasa de arribos es menor que la tasa de servicio no es posible obtener una solución analítica.
- V Verdadero
- **F Falso** *(marcada)*

**2.16  Preg.** ¿Cuáles paradigmas de simulación son los explicados en AnyLogic en 3 días?
- **A Basado en agentes.** *(marcada)*
- **B Sistemas dinámicos.** *(marcada)*
- **C Eventos discretos.** *(marcada)*
- D Peatones.
- E Caminos.
- F GIS.

**2.17  Preg.** GIS es un sistema geográfico monocapa para analizar cuestiones concretas de una zona particular.
- **V Verdadero** *(marcada)*
- F Falso

---

**3.**  Determine el costo total promedio mensual para un sistema de inventario con la política de pedidos vista en clase, y con estos datos:

Tiempo entre demandas: variable aleatoria exponencial con media 0,55.

Demora del proveedor: variable aleatoria uniforme en el intervalo $[0,5;\ 1]$.

Tamaño de la demanda:

$$D = \begin{cases} 3 & \text{con probabilidad } 1/3 \\ 4 & \text{con probabilidad } 1/6 \\ 5 & \text{con probabilidad } 1/6 \\ 6 & \text{con probabilidad } 1/3 \end{cases}$$

Parámetros para los costos: $K = 50$; $i = 5$; $h = 2,5$; $\pi = 6$.

Restantes parámetros: $s = 30$; $S = 60$; $I0 = 40$.

Números aleatorios: $0.9501 - 0.1304 - 0.9700 - 0.3546 - 0.9258$.

---

## Parcial 2024-10-19  ·  consignas 1 a 8 (9 y 10 no se fotografiaron)

> **Respuestas incluidas:** no

[encabezado cortado / ilegible]

#### Tema 1

1. Explique brevemente la diferencia entre las siguientes maneras de estudiar un sistema.
   - Modelo físico vs. Modelo matemático.
   - Solución analítica frente a Simulación.

2. Determine el costo total promedio mensual para un sistema de inventario con estos datos:

   Tiempo entre demandas: variable aleatoria exponencial con media 0,4.

   Demora del proveedor: variable aleatoria uniforme en el intervalo $[0{,}2;\,0{,}6]$.

   Tamaño de la demanda:

$$D = \begin{cases} 3 & \text{con probabilidad } 1/8 \\ 4 & \text{con probabilidad } 1/4 \\ 5 & \text{con probabilidad } 3/8 \\ 6 & \text{con probabilidad } 1/4 \end{cases}$$

   Parámetros para los costos: $K = 20$; $i = 5$; $h = 2{,}5$; $\pi = 6$.

   Restantes parámetros: $s = 15$; $S = 30$; $I_0 = 20$.

   Números aleatorios: 0.9015 - 0.1096 - 0.8901 - 0.3546 - 0.9317.

3. De los diez pasos de la simulación vistos en clase, desarrolle brevemente los siguientes: 6. Validación del modelo. 7. Generación del modelo final. 8. Determinación de los escenarios para el análisis.

4. En un modelo de colas (analítico), establezca la relación matemática entre la tasa de llegada (o número promedio de clientes que llegan por unidad de tiempo), y estas dos medidas de rendimiento: el número promedio de clientes en cola, y el tiempo promedio de cada cliente en la cola. Exprese dicha relación simbólicamente (señalando el significado de cada símbolo que utilice).

5. Describa la notación de Kendall para clasificar los distintos modelos de colas.

6. ¿Cómo se define la varianza de una variable aleatoria? Enuncie y demuestre a qué es equivalente la expresión $\mathrm{Var}(aX + b)$, siendo $a$ y $b$ constantes.

7. Defina y desarrolle las variables aleatorias binomiales.

8. Enuncie y describa las condiciones que hacen que la ocurrencia de ciertos "eventos" constituya un *proceso de Poisson*.

   ¿Qué caracteriza a un proceso de Poisson *no homogéneo*?

[fin de lo visible en la foto]

---

---

## Parcial 2023-09-16  ·  10 consignas de desarrollo

> **Respuestas incluidas:** no

#### Simulación (ISI) - Parcial - 16/9/2023

[Línea de Apellido y Nombre tachada con corrector blanco — ilegible/anonimizada]

#### Tema 1

1. Simulación de modelos a eventos discretos:

   a) Desarrolle e ilustre con un ejemplo en la línea de tiempo, el enfoque de avance en el tiempo al próximo evento para el sistema de una cola con un solo servidor.

   b) Describa las siguientes componentes: contadores estadísticos, rutina de eventos, biblioteca de rutinas y generador de informes.

2. Simulación de un sistema de inventario:

   a) Desarrolle el planteo del sistema, incluyendo: el tamaño de la demanda, la política de pedidos y la demora del proveedor.

   b) Defina los tres tipos de niveles de inventario al momento $t$: $I(t)$, $I^{+}(t)$ e $I^{-}(t)$; e ilustre con un ejemplo gráfico, cómo se pueden ir modificando a lo largo del tiempo.

3. De los diez pasos de la simulación vistos en clase, desarrolle brevemente los tres primeros.

4. En un modelo de colas (analítico), establezca la relación matemática entre la tasa de llegada (o número promedio de clientes que llegan por unidad de tiempo), y estas dos medidas de rendimiento: el número promedio de clientes en el sistema, y el tiempo promedio de cada cliente en el sistema. Exprese dicha relación simbólicamente (señalando el significado de cada símbolo que utilice).

5. Desarrolle brevemente algún aspecto del análisis económico de los sistemas de colas.

6. Defina los siguientes conceptos para variables aleatorias continuas: función de probabilidad acumulativa, esperanza y variancia. Enuncie y pruebe alguna propiedad que involucre al menos uno de dichos conceptos.

7. Defina y desarrolle alguna de las variables aleatorias discretas vistas en clase, incluyendo: el significado de sus parámetros, su función de masa de probabilidad, su esperanza y su variancia.

8. Enuncie y describa las condiciones que hacen que la ocurrencia de ciertos "eventos" constituya un *proceso de Poisson*.

   ¿Qué caracteriza a un proceso de Poisson *no homogéneo*?

9. Desarrolle el método congruencial multiplicativo para la generación de números aleatorios con distribución uniforme en el intervalo $(0;1)$.

   ¿Cómo se modifica la fórmula de dicho método en el método congruencial mixto?

10. Enuncie y demuestre el algoritmo de la transformada inversa para la generación de variables aleatorias continuas. Luego elija una variable aleatoria continua, y aplique dicho algoritmo para generarla.

> [NOTA pág. 1]: En el margen derecho de la foto asoma parcialmente otra hoja (cuadriculada, con escritura manuscrita). Solo se ven fragmentos de trazos sueltos, sin ninguna palabra completa: **ilegible**, no transcribible.

---

---

## Parcial 2022-09-24  ·  10 consignas de desarrollo

> **Respuestas incluidas:** no

#### Simulación (ISI) - Parcial - 24/9/2022

APELLIDO Y NOMBRES: [tachado con corrector blanco — ilegible/anonimizado]

#### Tema 1

1. Explique la diferencia entre los siguientes tipos de modelos por simulación:
   - Deterministas vs. estocásticos.
   - Continuos vs. discretos.

2. Desarrolle el diagrama de Control de Flujo para el mecanismo de avance en el tiempo al próximo evento, en una simulación de modelos a eventos discretos.

3. En la simulación del sistema formado por una cola con un solo servidor, defina y desarrolle las tres medidas de rendimiento vistas en clase.

4. En la simulación de un sistema de inventario, describa cada uno de los siguientes conceptos:
   - Política de pedidos.
   - Tamaño de la demanda.
   - Costo por pedido.

5. Luego de la definición del sistema bajo estudio y la generación del modelo de simulación base, se deben efectuar: a) la recolección y el análisis de datos, y b) la generación del modelo preliminar. Desarrolle los pasos a) y b) de un estudio de simulación.

6. Describa la notación de Kendall para clasificar los distintos modelos de colas.

7. ¿Cómo se define la esperanza de una variable aleatoria, tanto en el caso discreto como continuo? Demuestre, en el caso de una variable aleatoria discreta $X$, que: $E[aX + b] = aE[X] + b$ (si $a$ y $b$ son constantes).

8. Enuncie y describa las condiciones que hacen que la ocurrencia de ciertos "eventos" constituya un Proceso de Poisson.

   ¿Qué caracteriza a un proceso de Poisson no homogéneo?

9. Dada la fórmula de generación de números aleatorios $x_n = a x_{n-1}$ módulo $m$ (método congruencial multiplicativo), explique cuáles son las condiciones deseables para $a$ y $m$.

   ¿Cómo se modifica la fórmula anterior en el método congruencial mixto?

10. Enuncie y demuestre el algoritmo de la transformada inversa para la generación de variables aleatorias continuas. Luego elija una variable aleatoria continua, y aplique dicho algoritmo para generarla.

---

---

## Parcial 2021-12-02  ·  10 preguntas

> **Respuestas incluidas:** sí, resueltas (⚠ con errores)

Pregunta 1

Dada la fórmula de generación de números aleatorios xn = axn−1 modulo m, explique cuáles son las condiciones deseables para a y m

Las condiciones deseables para las constantes a y m son:

1. Para cualquier semilla inicial, la sucesion resultante tiene la "apariencia" de ser una sucesion de variables aleatorias independientes y uniformes en (0,1).

2. Para cualquier semilla inicial, la cantidad de variables generadas antes de que comience la repeticion es grande.

3. Los valores pueden calcularse eficientemente en una computadora digital.

Para las condiciones deseables suele elegirse para m un numero primo grande, aproximado al tamaño de la palabra del sistema. Por ejemplo para un sistema con palabras de 32 bits: m=2^(31)-1 y a=7^5=1608.

Pregunta 2

Describa las fórmulas y explique cómo se modela el arribo de clientes a una simulación de un sistema de colas

Para un sistema de colas, los tiempos entre arribos pueden ser de 3 tipos:

D: deterministicos. Los tiempos de arribos estan determinados al comenzar la simulacion.

G: general. Los tiempos entre arribos siguen una distribucion general, distinta a la exponencial.

M:exponencial. Los tiempos entre arribos independientes se vinculan con la distribucion de Poisson mediante el parametro lambda.

El que utilizamos para el modelo M/M/1 con llegadas exponenciales es aquel en el que el tiempo entre arribos es independiente y sigue una distribucion de Poisson con parametro lambda.

Este parametro lambda representa el promedio de arribos por unidad de tiempo.

La funcion de densidad para esta ditribucion es:

pi=e^(-lambda). lambda^(i)/i!   ,  i=0,1,2...


Pregunta 3

Enuncie la fórmula y explique bajo qué condiciones hablamos de una variable aleatoria de Poisson. Cite algún ejemplo

Cuando X toma uno de los valores 0,1,2... es una variable Poisson con parametro lambda, lambda<0, si su funcion de masa de probabilidad es


                                 pi=P{X=i}=e^(-lambda) . lambda^i/ i!   ,  i=0,1,....


Ejemplo: los tiempos entre arribos en un sistema M/M/1 siguen esta distribucion, en los cuales el parametro lambda representa el promedio arribos por unidad de tiempo.

Pregunta 4

Cuáles son las condiciones para un modelo M/M/1?

Las condiciones para un modelo M/M/1 son:

1. Una poblacion de tamaño infinita.

2. Una cola de una linea, con area de espera infinita

3. Un proceso de llegadas independientes que siguen una distribucion de Poisson con parametro lambda.

4. Un servidor de un canal que sirve siguendo una distribucion exponencial dando servicio con un promedio de u clientes por unidad de tiempo.

Pregunta 5

Describa los costos asociados a un modelo de simulación de inventarios

Estos costos son:

- Costo de la orden: K+Z.i , donde K es el costo fijo, Z es el costo por unidad pedida e i es la cantidad de unidades pedidas.

- Costo por items almacenados: I^(+).Π , donde I^(+) es el valor de los items fisicos en inventario y Π es el costo por items almacenados por mes.

- Costo por items adeudados: I^(-).h, donde I^(-) es la cantidad de items faltantes y h es el costo por items adeudados por mes.

Pregunta 6

Desarrolle los siguientes pasos a) y b), en la realización de un estudio de simulación: a) la determinación de los escenarios para el análisis, b) la documentación del modelo, sugerencias y conclusiones

a) Luego de la validacion del modelo se deben elegir los escenarios que se realizaran en la simulacion. Para esto se suele elegir un escenario pesimista, uno intermedio y uno optimista para la variable de rendimiento importante. El analista tambien puede sugerir un escenario alternativo.

b) Una vez realizado el estudio estadistico de los resultados, se debe realizar la documentacion del sistema como guia para el usuario y para posibles modificaciones futuras. Tambien el analista debe poner sus conclusiones sobre el sistema simulado y sus resultados, para poder luego generar un reporte ejecutivo.

Pregunta 7

Defina y explique los axiomas básicos de la probabilidad

Pregunta 8

Explique y aplique el Método de la Transformada Inversa para generar el valor de una variable aleatoria discreta X con la siguiente función de masa de probabilidad: P(X=1) = 1/6, P(X=2) = 1/3, P(X=3) = 1/3, P(X=4) = 1/6 (observe que 1/6 + 1/3 + 1/3 + 1/6 = 1)

Generamos un numero aleatorio U con distribucion uniforme entre (0,1) y luego:

Si U<1/6 hacer X=1 y terminar

Si U<1/2 hacer X=2 y terminar

Si U<5/6 hacer X=3 y terminar

Si lo anterior no se cumple hacer X=4 y terminar.

Asi, luego de generar U determinamos el valor de

x hallando el intervalo al que pertenece U.

Pregunta 9

Cómo debe ser la relación entre los parámetros lambda y mu para que un sistema de colas funcione?

En un sistema de colas, el parametro mu, cantidad promedio de servicios por unidad de tiempo, debe ser mayor que el parametro lambda, cantidad promedio de arribos por unidad de tiempo. De lo contrario el sistema no podria alcanzar un estado estable ya que siempre llegarian mas clientes de los que se les puede dar servicio, haciendo que la cola sea cada vez mas larga.

Pregunta 10

Enuncie y demuestre el Algoritmo de la Transformada Inversa para la generación de variables aleatorias continuas y aplíquelo para generar una variable aleatoria con distribución exponencial.

---

## Parcial 2021-10-23  ·  16 preguntas

> **Respuestas incluidas:** sí, resueltas (⚠ con errores)

#PREGUNTA 1

    Describa los costos asociados a un modelo de simulación de
inventarios

    - I-.π: costo promedio mensual por ítems adeudados. donde π: costo
por ítem por mes de atraso en la entrega

    - I+.h: costo promedio mensual por ítems en existencia. donde h:costo
por item por mes de inventario

    - Costo de la orden: K + i.Z; donde K es el costo fijo, i es el costo
por unidad y Z es la cantidad de
unidades pedidas.

#PREGUNTA 2

    Enuncie y demuestre el Algoritmo de la Transformada Inversa para la
generación de variables aleatorias continuas y aplíquelo para generar una
variable aleatoria con distribución uniforme.

    Proposición: Sea U una variable aleatoria uniƒormeen (0. 1). Para
cualquier función de distribución continua E invertible, la variable
aleatoria X definida como
                    X = F^-1(U)

    tiene distribución F. [F^-1 se define como el valor de x tal que F(x)
= u.]

    Demostración: Sea FX la función de distribución de X = F^-1(U).
Entonces

                    Fx(x) = P{F(F^-1(U) <= F(x)}
                          = P{U <= F(x)}    pues F(F^-1(U)) = U
                          = F(x)            pues U es uniforme en (0,1).

    La proposición anterior muestra entonces que para generar una
variable aleatoria X a partir de la función de distribución continua F,
generamos un número aleatorio U y hacemos entonces X = F^-1(U).

#PREGUNTA 3

    Dada la fórmula de generación de números aleatorios xn = axn−1 modulo
m, explique cuáles son las condiciones deseables para a y m

    En general. las constantes a y m deben satisfacer tres criterios:

    1. Para cualquier semilla inicial, la sucesión resultante tiene la
“apariencia” de ser una sucesión de variables aleatorias independientes y
uniformes en (0, 1).

    2. Para cualquier semilla inicial, el número de variables que se
pueden generar

antes de que comience la repetición es grande.
    3. Los valores se pueden calcular de manera eficiente en una
computadora digital.

    Las condiciones deseables son que m sea un numero primo de tamaño
aproximado al tamaño de la palabra del sistema de simulacion, para una
palabra de tamaño 32 se suele elegir m = 2^31-1 y a = 7^5 = 16807.

#PREGUNTA 4

    Qué condiciones debe cumplir un proceso de Poisson homogéneo?

    (a) N(0) = 0.

    (b) El número de eventos que ocurren en intervalos de tiempo
distintos son independientes.
    (c) La distribución del número de eventos que ocurren en un intervalo
dado depende solamente de la longitud del intervalo y no de su posición.
    (d) y (e) establecen que en un pequeño
intervalo de longitud h, la probabilidad de que ocurra un evento es
aproximadamente
lambda.h, mientras que la probabilidad de dos o más es aproximadamente 0.

#PREGUNTA 5

    Desarrolle los siguientes pasos a) y b), en la realización de un
estudio de simulación:

a) la determinación de los escenarios para el análisis, b) la
documentación del modelo, sugerencias y conclusiones

     a) Tras validar el modelo es necesario acordar con el cliente los
escenarios que se quiere analizar. Una manera muy sencilla de
determinarlos consiste en utilizar un escenario pesimista, uno optimista
y uno intermedio para la variable de respuesta mas importante.
       Por su parte el analista tambien puede contribuir a la seleccion
de escenarios, sugiriendo aquellos que considere mas importantes.

     b) Una vez realizado el analisis de los resultados, es necesario
efectuar toda la documentacion del modelo. Esta documentacion es muy
importante, pues permitira el uso del modelo generado en caso de que se
requieran ajustes futuros. Tambien es importante incluir sugerencias
tanto del uso del modelo como sobre los resultados obtenidos, con el
proposito de realizar un reporte mas completo. Por ultimo, deberan
presentarse asimismo las conclusiones del proyecto de simulacion, a
partir de las cuales es posible obtener los reportes ejecutivos para la
presentacion final.

#PREGUNTA 6

    Cuál es la diferencia entre un modelo analítico y una simulación?

    Si el modelo es bastante simple, puede ser posible trabajar con sus
relaciones y cantidades para obtener una solución exacta y analítica.

    Pero algunas soluciones analíticas pueden llegar a ser
extraordinariamente complejas, requiriendo vastos recursos informáticos.
Si una solución analítica a un modelo matemático están disponibles y es
computacionalmente eficiente, generalmente es deseable estudiar el modelo
de esta manera en lugar de a través de un simulación. Sin embargo, muchos
sistemas son altamente complejos, lo que impide cualquier posibilidad de
una solución analítica. En este caso, se debe estudiar el modelo mediante
simulación, es decir, ejercitando numéricamente el modelo para las
entradas en cuestión para ver cómo afectan a las medidas de rendimiento
de la producción.

#PREGUNTA 7

    En un modelo de colas, establezca la relación matemática entre la
tasa de servicio (o número promedio de clientes atendidos por unidad de
tiempo), y estas dos medidas de rendimiento: Tiempo promedio de espera en
la cola - Tiempo promedio en el sistema. Exprese dicha relación
simbólicamente (señalando el significado de cada símbolo que utilice)

    W = Wq + (1/u)

    donde:

    u = tasa de servicio

    1/u = tiempo promedio de servicio por cliente

    Wq = tiempo promedio en cola

    W= tiempo promedio en el sistema

#PREGUNTA 8

    Explique y aplique el Método de la Transformada Inversa para generar
el valor de una variable aleatoria discreta X con la siguiente función de
masa de probabilidad: P(X=1) = 1/6, P(X=2) = 1/3, P(X=3) = 1/3, P(X=4) =
1/6 (observe que 1/6 + 1/3 + 1/3 + 1/6 = 1)

    Generamos U y hacemos lo siguiente:
    - Si U < 1/6 hacemos X = 1 y terminamos
    - Si U < 1/2 hacemos X = 2 y terminamos
    - Si U < 5/6 hacemos X = 3 y terminamos
    - En caso contrario, hacemos X = 4

    Después de generar un número aleatorio U determinamos el valor de X
hallando el intervalo (F(xj-1), F(xj)) en el que está U [o, de forma
equivalente, hallando la inversa de F( U)]. Es por esta razón que el
anterior se llama método de la transformada inversa discreta para generar
X.

#PREGUNTA 9

    Cuáles son las condiciones para un modelo M/M/1?

    1. Una poblacion de clientes infita.
    2. Un proceso de llegada en el que los clientes se presentan de
acuerdo con un proceso de Poisson con una tasa promedio de lambda
clientes por unidad de tiempo.
    3. Un proceso de colas que consiste en una sola linea de espera de
capacidad infinita, con una disciplina de colas PEPS.
    4. Un proceso de servicio que consiste en un solo servidor que
atiende a los clientes de acuerdo con una distribucion exponencial con un
promedio de u clientes por unidad de tiempo.

    Para que este sistema alcance una condicion de estado estable, la
tasa de servicio promedio u debe ser mayor que la tasa de llegadas
promedio lambda.

#PREGUNTA 10

    Enuncie la fórmula y explique bajo qué condiciones hablamos de una
variable aleatoria hipergeométrica   (pag 32 Ross)

    Consideremos una urna con N+M bolas, de las cuales N tienen color
claro y M color oscuro. Si se elige una nuestra de tamano n de manera
aleatoria (en el sentido de que cada subconjunto de tamano n tiene la
misma probabilidad de ser elegido), entoces X, el numero de bolas de
color claro elegidas, tiene la funcion de masa de probabilidad:

                                /N\/ M \
                                \i/\n-1/
                       P[X=i] = ----------
                                 /N-M\
                                 \ n /

#PREGUNTA 11

    Cual es la diferencia entre un modelo del sistema y un experimento
con el sistema real?

    Si es posible (y rentable) alterar el sistema físicamente y luego
déjelo operar bajo las nuevas condiciones, probablemente sea deseable
hacerlo, porque en este caso no hay duda sobre si lo que estudiamos es
relevante. Sin embargo, rara vez es factible hacer esto, porque tal
experiencia, generalmente sería demasiada costosa o demasiada perjudicial
para el sistema.
    Por estas razones, generalmente es necesario construir un modelo.
como una representación del sistema y estudiarlo como un sustituto del
sistema. Cuando se utiliza un modelo, siempre existe la pregunta de si
refleja con precisión el sistema a los efectos de las decisiones que
deben tomarse.

#PREGUNTA 12

    Explique la diferencia entre un proceso de Poisson homogeneo y uno no
homogeneo.

    Un proceso de Poisson homogeneo, a diferencia de uno no homogeneo,
cumple con la condicion llamada hipótesis de incremento estacionario,
esto es, que la distribucion del numero de eventos que ocurren en un
intervalo dado depende solamente de la longitud del intervalo y no de su
posicion.

#PREGUNTA 13

    Explique la formula y el concepto de variable aleatoria exponencial.
Para que usamos esta formula en un modelo de colas?

    Una variable aleatoria continua con funcion de de densidad de
probabilidad
                f(x)= lambda.e^(-lambda.x) , 0<x<infinito
    para cierta lambda>0 es una variable aleatoria exponencial con
parametro lambda.

    En un modelo de colas mm1 tanto los tiempos de arribo como los
tiempos de servicios siguen una distribucion exponencial.

#PREGUNTA 14

    Luego de la definicion del sistema bajo estudio y la generacon del
modelo de simulacion base, se debe efectuar: a) la recoleccion y el
analisis de datos, y b) la generacion del modelo preliminar. Desarrolle
los pasos a) y b) de un estudio de simulacion.

    a)Recoleccion y analisis de los datos: en este paso se recopila y
analiza la informacion estadistica necesaria para determinar las
distribuciones de probabilidad de cada una de las variables aleatorias
del modelo.

    b)Generacion del modelo preliminar: en esta etapa se integra toda la
informacion obtenida hasta el momento para lograr un modelo lo mas
cercano posible al sistema en estudio.

#PREGUNTA 15

    Dada una cola finita de tamaño n en un sistema de una cola y un
servidor. Como se calcula la probabilidad de que un cliente no pueda
entrar a la cola?(Denegacion de servicio)

    Para un sistema con una cola de tamaño finito n-1 y un servidor, la
capacidad maxima de dicho sistema es n, contando a un cliente en
servicio. Por lo tanto la probabilidad de denegacion de servicio Pd es
igual a la sumatoria de las probabilidades de que hayan mas de n clientes
en el sistema. Entonces
            Pd = Pn+1 + Pn+2 + Pn+3....
    O bien se podria restar a 1 la sumatoria de probabilidades de que
hayan entre 0 y n clientes en el sistema
            Pd = 1 - (P0+P1+P2+...+Pn)

#PREGUNTA 16

    En el modelo de simulacion de inventarios desarrollado en clase,
describa el significado, las formulas que los involucran, y como varian
en el tiempo los niveles de inventario: I(t), I^+(t) e I^-(t)

    I(t): nivel de inventario al momento t (puede ser positivo, negativo
o cero)
    I +(t): número de unidades que realmente están en existencia.
    I –(t): número de unidades demandadas y no entregadas, por falta de
stock.

    I- = [integral entre 0 y n de I-(t).dt] / n
    I+ = [integral entre 0 y n de I+(t).dt] / n

    I+.h: costo promedio mensual por items en existencia , h:costo por
item por mes de inventario
    I-.π: costo promedio mensual por ítems adeudados ,     π: costo por
ítem por mes de atraso en la entrega.

---

## Parcial 2019 (recuperatorio) — Leale  ·  práctica: uniforme, congruencial, análisis de salidas

> **Respuestas incluidas:** no



---

## Parcial 2019 (recuperatorio) — Weitz  ·  teoría: comparación de sistemas

> **Respuestas incluidas:** no

Recuperatorio 2019
Weitz (2do parcial teoría):

1 Analisis de resultados MAS DE DOS SISTEMAS. Formulas.

2 Definir en no mas de 10 renglones:
 * Números Aleatorios Comunes

 * Procedimientos de precision relativa y absoluta. Las dos       formulas.

 * Simulacion NO Terminal.

 * 3 Medidas utilizadas para describir sistemas de    colas. (Letras, definiciones y relaciones).

---

## Globalizador 2023-03-16  ·  10 preguntas

> **Respuestas incluidas:** no

#### Simulación (ISI) - Globalizador - 16/3/2023

APELLIDO Y NOMBRE: ______________________________ &nbsp;&nbsp; LEGAJO: __________

1. ¿Cómo se define la esperanza de una variable aleatoria? Desarrolle a qué es igual la esperanza de una variable aleatoria multiplicada por una constante y sumada con un término independiente.

2. Enuncie la fórmula y explique bajo qué condiciones hablamos de una variable aleatoria binomial.

3. Dada la fórmula de generación de números aleatorios $x_n = a x_n - 1$ módulo $m$, explique cuáles son las condiciones deseables para $a$ y $m$.

   > [NOTA DE TRANSCRIPCIÓN]: la fórmula está impresa literalmente así en el original ($x_n = ax_n - 1$); se entiende que refiere a $x_n = a\,x_{n-1} \bmod m$.

4. Desarrolle el Método de la Transformada Inversa para la generación de variables aleatorias discretas.

5. Describa los costos asociados a un modelo de simulación de inventarios.

6. ¿Cuál es la diferencia entre un modelo determinístico y uno estocástico?

7. Luego de la definición del sistema bajo estudio y la generación del modelo de simulación base, se deben efectuar: a) la recolección y el análisis de datos, y b) la generación del modelo preliminar. Desarrolle los pasos a) y b) de un estudio de simulación.

8. En un modelo de colas, establezca la relación matemática entre la tasa de servicio (o número promedio de clientes atendidos por unidad de tiempo), y estas dos medidas de rendimiento: Tiempo promedio de espera en la cola - Tiempo promedio en el sistema. Exprese dicha relación simbólicamente (señalando el significado de cada símbolo que utilice).

9. Desarrolle las condiciones que caracterizan un modelo $M/M/c$.

10. Explique el procedimiento para determinar cuándo detener las corridas de simulación con el objetivo de obtener un desvío estandar determinado (pre-definido).

---

---

## Final 2021-11-29  ·  10 preguntas (Moodle)

> **Respuestas incluidas:** no

**Pregunta 1** [Finalizado — Puntúa como 1,00 — Marcar pregunta]

Dada la fórmula de generación de números aleatorios $x_n = a x_{n-1}$ modulo $m$, explique cuáles son las condiciones deseables para $a$ y $m$

**Pregunta 2** [Finalizado — Puntúa como 1,00 — Marcar pregunta]

Cuál es la diferencia entre un modelo del sistema y un experimento con el sistema real?

**Pregunta 3** [Sin contestar — Puntúa como 1,00 — Marcar pregunta]

Explique la diferencia entre un proceso de Poisson homogéneo y uno no homogéneo

**Pregunta 4** [Sin contestar — Puntúa como 1,00 — Marcar pregunta]

Explique y aplique el Método de la Transformada Inversa para generar el valor de una variable aleatoria discreta X con la siguiente función de masa de probabilidad: $P(X=1) = 1/6$, $P(X=2) = 1/3$, $P(X=3) = 1/3$, $P(X=4) = 1/6$ (observe que $1/6 + 1/3 + 1/3 + 1/6 = 1$)

**Pregunta 5** [Finalizado — Puntúa como 1,00 — Marcar pregunta]

En un modelo de colas, establezca la relación matemática entre la tasa de servicio (o número promedio de clientes atendidos por unidad de tiempo), y estas dos medidas de rendimiento: Tiempo promedio de espera en la cola - Tiempo promedio en el sistema. Exprese dicha relación simbólicamente (señalando el significado de cada símbolo que utilice)

**Pregunta 6** [Finalizado — Puntúa como 1,00 — Marcar pregunta]

Explique la fórmula y el concepto de variable aleatoria exponencial. Para qué usamos esta fórmula en un modelo de colas?

**Pregunta 7** [Sin contestar — Puntúa como 1,00 — Marcar pregunta]

Enuncie y demuestre el Algoritmo de la Transformada Inversa para la generación de variables aleatorias continuas y aplíquelo para generar una variable aleatoria con distribución uniforme.

**Pregunta 8** [Finalizado — Puntúa como 1,00 — Marcar pregunta]

Luego de la definición del sistema bajo estudio y la generación del modelo de simulación base, se deben efectuar: a) la recolección y el análisis de datos, y b) la generación del modelo preliminar. Desarrolle los pasos a) y b) de un estudio de simulación

**Pregunta 9** [Sin contestar — Puntúa como 1,00 — Marcar pregunta]

Dada una cola finita de tamaño n en un sistema de una cola y un servidor. Cómo se calcula la probabilidad de que un cliente no pueda entrar a la cola? (Denegación de servicio)

**Pregunta 10** [Finalizado — Puntúa como 1,00 — Marcar pregunta]

En el modelo de simulación de inventarios desarrollado en clase, describa el significado, las fórmulas que los involucran, y cómo varían en el tiempo los tres niveles de inventario: $I(t)$, $I^{\wedge}(t)$, $I^{\wedge}\{-\}(t)$ {}

---

## Final 2020-08-06  ·  oral: inventario, 10 pasos, M/M/1

> **Respuestas incluidas:** sí, resueltas

**Examen Final 06/08/2020 - Modalidad Virtual.**

La modalidad fue remota por lo cual el examen fue totalmente oral donde iban tomando uno a uno de forma individual donde los demás que rendían esperaban en la sala. Particularmente a mi (desconozco si fue lo mismo para los demás) me pidieron que desarrolle los siguientes 3 temas

1- Inventario

2- Pasos para realizar una simulación

3- Modelo de Cola MM1.

Donde a medida que iba explicando te iban haciendo preguntas, Leale me pregunto cosas de inventario como por ejemplo que variable introduciría para ser medida.

En el punto 2 luego de comentar el nombre de cada paso, Jorge me pregunto sobre los tipos de escenarios que hay (Pesimista, optimista intermedio), y por último en el punto 3, Juan me pregunto qué relación tenía con el Modelo Analítico.

Hubo algunas preguntas puntuales más al respecto de los temas, pero no recuerdo bien.

**Resolución**

La modalidad fue remota por lo cual el examen fue totalmente oral donde iban tomando uno a uno de forma individual donde los demás que rendían esperaban en la sala. Particularmente a mí (desconozco si fue lo mismo para los demás) me pidieron que desarrolle los siguientes 3 temas:

1. **Inventario**

**Componentes**

* Tiempo entre demandas
* Tamaño de demanda
* Costo del pedido: K+i.Z ; siendo K el costo base, i el costo incremental y Z la cantidad.
* Retardo de envío.
* Política estacionaria (Punto de pedido, Tope) (s,S): define Z.Si I < s, Z=S-I, si I >=s, Z=0.
* I(t) Nivel de inventario
* I+(t) Ítems en posesión en inventario MAX(I(t), 0)
* I-(t) Nivel ítems faltantes en inventario MAX(-I(t), 0)
* h Costo de mantenimiento
* Ī+ Items promedio para el n-ésimo periodo de tiempo
* Ī+.h Promedio de costo de mantenimiento por unidad de tiempo
* π Costo faltante ítems por unidad de tiempo
* Ī- Ítems faltantes promedio para el n-ésimo periodo de tiempo
* Ī-.π Promedio de costos faltantes por unidad de tiempo

**Rutinas**

*Evento Arribo de orden*

Incrementar nivel de inventario a la cantidad previamente ordenada

Eliminar el evento arribo de consideración

Volver

*Evento Demanda*

Generar tamaño de demanda

Disminuir el inventario por tamaño de demanda

Definir el siguiente evento demanda

Volver

*Evento Evaluación de Inventario*

I<s?

Si lo es

Determinar la cantidad a ordenar

Calcular costo pedido y acumular

Determinar tiempo de arribo de orden

Determinar próxima evaluación de inventario

Volver

**Modelo de desencadenamiento de eventos**

Se hace antes de la simulación, ver el sistema con un alto nivel de abstracción.

⇒ Control inventario (Auto ref) ⇒ Arribo pedido

⇒ Demanda (Auto ref)

**Medidas de desempeño**

CCP=ACP/reloj; Costo Cantidad Pedida

ACP Acumulado Cantidad Pedida

CUI=AIP.h Costo Unidades en Inventario

AIP Acumulado Inventario Positivo

CUP=AIN.π/reloj Costo unidades perdidas

AIN Acumulado Inventario Negativo

CMP = CCP+CUI+CUP Costo Mensual Promedio

1. **Pasos para realizar una simulación**

**Definición del sistema bajo estudio**, Conocer el sistema a modelar. Saber que origina el estudio de la simulación y los supuestos del modelo. Contar con información suficiente como para establecer un modelo conceptual.

**Generación del sistema de simulación base**, Generación de un modelo de simulación base. No demasiado detallado.

**Recolección y análisis de los datos**, Recopilación de la información estadística de las variables. Determinar qué información es útil para determinar distribuciones. De no contar con información necesaria se realiza un estudio estadístico del comportamiento de las variables.

**Generación del modelo preliminar**, Integra el análisis de los datos, los supuestos del modelo y todos los datos necesarios para hacer un modelo lo más cercano a la realidad.

**Verificación del modelo**, Verificación de datos para comprobar la programación del modelo y que los parámetros usados funcionen correctamente.

**Validación del modelo**, Se le realizan una serie de pruebas al mismo, utilizando información de una entrada real para observar su comportamiento y analizar sus resultados.

**Generación del modelo final**, Una vez que el modelo se ha validado, está listo para realizar la simulación y estudiar el comportamiento del proceso. Modelo Raíz.

**Determinación de los escenarios para el análisis**, Se acuerda con el cliente los escenarios que desea analizar. Se suele utilizar un escenario pesimista, optimista, e intermedio.

**Análisis de sensibilidad**, Una vez obtenidos los resultados se realizan pruebas estadísticas que permitan comparar los escenarios con los mejores resultados finales

**Documentación del modelo, sugerencias y conclusiones**, Se efectúa la documentación del modelo. Permitirá el uso del modelo generado en caso que se requieran ajustes futuros. Se deben incluir los supuestos, las distribuciones asociadas a las variables, los alcances y limitaciones, junto con las consideraciones de programación. Sugerencias para el uso del modelo como para el uso de los resultados. Y por último conclusiones del modelo.

1. **Modelo de Cola M/M/1.**

Consta de lo siguiente:

1- Una población de clientes infinita

2- Un proceso de llegada en el que los clientes se presentan de acuerdo a un proceso de Poisson con una tasa promedio de λ clientes por unidad de tiempo.

3- Un proceso de colas con una sola línea de espera, con una disciplina FIFO.

4- Un proceso de servicio de un solo servidor en el que se atiende a los clientes de acuerdo con una distribución exponencial con un promedio de 𝝁 clientes por unidad de tiempo.

**Cálculo de las medidas de rendimiento**

Intensidad de tráfico ρ=λ/𝝁, mientras más cerca esté de 1 más cargado estará el sistema.

Probabilidad que no haya clientes en el sistema P0 =1-ρ

Número promedio en la fila Lq=ρ2/(1-ρ)

Tiempo promedio de espera en la cola Wq=Lq/λ

Tiempo promedio de espera en el sistema W=Wq+1/𝝁

Número promedio en el sistema L=λ\*W

Probabilidad de que un cliente que llegue tenga que esperar pw= 1-P0=ρ

Probabilidad de que hay n clientes en el sistema Pn=ρn\*P0

Utilización U=ρ

Nos interesa desarrollar un modelo para predecir(Analíticamente):

1. (tamaño promedio de la cola) La probabilidad de varios números de clientes en la cola (Número promedio esperado en cola)
2. El tiempo esperado o promedio que pasará un cliente en las “instalaciones” del servicio.
3. La probabilidad que las instalaciones del servicio estén ociosas (también llamado factor de utilización)

Donde a medida que iba explicando te iban haciendo preguntas, Leale me pregunto cosas de inventario como por ejemplo qué variable introduciría para ser medida.

punto 3, Juan me preguntó qué relación tenía con el Modelo Analítico.

---

## Final 2019-07-02  ·  4 consignas

> **Respuestas incluidas:** no

1- Que estrategias utilizar para realizar el análisis de resultados para comparación de 2 sistemas

2- Describir los estados estacionario y transitorio de una experiencia de simulación

3- Definiciones y descripciones. Incluir gráficas, ecuaciones de ser posible 
- Disciplina de cola
- Simulación a eventos discretos 
- Política de pedido de Sistemas de inventario 
- Validación y verificación 
- Determinación de condiciones iniciales en simulaciones terminales 
- Me falta una pero no me acuerdo 

4- Función triangular 
- f(t) = 0 si t<0 o t>1
- f(t) = f0(1-t) si 0<=t<=1
- Encontrar f0
- Armar un generador de números aleatorios con la función

---

## Final 2017-07-04  ·  caso: guardia de hospital

> **Respuestas incluidas:** no

[Simulación Final 4-7-17]
Era una guardia de hospital a los que llegaban los pacientes entre las 22 y las 7 hs. Había 4 consultorios. En los consultorios analizaban a los pacientes y con cierta probabilidad (no decía) los derivaban a internación, cuidados ambulatorios (que dejaban el consultorio y el hospital) o laboratorios para análisis o rayos X. (Esa info de que los derivaban era al pedo porque no era parte del modelo)
No daba ninguna distribución de probabilidad ni números de medias.
A) Modelo a eventos (era un arribo simple y partida con doble círculo, para considerar los 4 consultorios, bien básico. Los desencadenamientos de siempre)
B) Datos faltantes
C) Medidas de rendimiento para hacer el estudio (también, las de siempre)
D) Hacer una rutina (pseudocódigo) en la que se pueda ver el cálculo de al menos una medida de rendimiento
E) Análisis de resultados (pedía que fuera específico al ejercicio, no general teórico. Yo puse lo del procedimiento de la muestra de tamaño fijo para calcular el número de réplicas)
F) De las técnicas de Probabilidad y Estadística usadas en Simulación, describir al menos dos (así bien general era. Yo desarrollé cómo se generan valores de variables aleatorias distribuidas uniformemente a partir de números aleatorios, y desarrollé el procedimiento de la muestra de tamaño incremental por error relativo)

NOTAS:
Un ejercicio de practica que te la re volaba pero en fin nada importaba para el objetivo en estudio. Terminaba SIENDO a un arribo y a una partida con 4 consultorios. osea doble circulo con i de uno a 4 para la partida. Que variables faltaban (como siempre), medidas de rendimiento. Analisis de Resultados para ese problema, que era terminal, y la ultima preguntaba que describas algo probabilistico o estadisitico que hayamos usado, yo hice la exponencial y la uniforme (Generadores de variables)

Algoritmo en donde se viera que acumulas los estadisticos para las medidas que planteaste. (Yo hice arribo de un paciente - basicamente el arribo clasico que esta en el resumen ese de teoria)

---

## Final 2016-07-05  ·  4 consignas

> **Respuestas incluidas:** no

**Final 05/07/2016
**
1) Desarrollar el algoritmo para generar números aleatorios con la siguiente función de densidad triangular: 
f(t) = 0 si 0>t
f(t) = 2(1-t) si 0<t<1
f(t) = 0 si t>1
2) En el estado estacionario la longitud media de la cola es constante, por lo que las demoras individuales también son constantes. ¿Es correcto? Justificar.
3) a) Definir simulación de eventos discretos.
b) ¿Dónde se usa y para qué?
c) ¿Se puede dar un modelo de simulación con eventos discretos y continuos al mismo tiempo? Justificar.
4) a) ¿Cómo realizaría el análisis de resultados en un sistema de estado estacionario (simulación no terminal)? 
b) Todos los sistemas se estabilizan cuando transcurre una gran cantidad de tiempo. ¿Es correcta esa afirmación? Justificar.

---

## Final agosto 2015  ·  caso: dos secciones con transporte único

> **Respuestas incluidas:** no

#### Simulación
#### Examen Final, agosto 2015

Alumnos: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Calificación:

———————————————————————————————————

En una empresa hay dos secciones de operación: A y B. Ciertos artículos arriban al sistema con distribución de Poisson para los tiempos entre arribos con frecuencia lambda. Los lotes de mercadería forman una línea de espera con disciplina Fifo. El servidor de A consiste en cargar la mercadería y transportarla hasta la sección B, en el cual se descarga y se la lleva a un deposito con una frecuencia de servicio mhu. Una vez completada la descarga, el sistema de transporte retorna al puesto A para recibir la nueva carga. La demora de ir de B hacia A posee distribución forme. Existe un único transporte.

Se desea:

1) Desarrollar el diagrama de desencadenamiento de eventos.
2) Falta alguna información y cual es.
3) Desarrolle un algoritmo para el tratamiento de la línea de espera en A
4) En el régimen estacionario se desea saber cómo influye el tiempo de retorno en el tiempo medio en el sistema. Que análisis de resultados hará.

---
