# 2025-10-04.pdf — Examen Parcial de Simulación

> El PDF tiene 2 páginas; cada una es la foto de **dos hojas del examen** puestas lado a lado.
> El texto fluye de la hoja izquierda a la hoja derecha. Las respuestas están marcadas a
> mano con un círculo sobre la letra de la opción elegida; se indican abajo con **(marcada)**.
> El nombre del alumno está tachado con marcador verde en la carátula.

--- pág. 1 del PDF — hoja izquierda ---

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

--- pág. 1 del PDF — hoja derecha ---

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

--- pág. 2 del PDF — hoja izquierda ---

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

--- pág. 2 del PDF — hoja derecha ---

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
