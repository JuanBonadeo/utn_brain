**ÍNDICE**

[**Unidad temática 1**](#_gxa5ts1uf8ej) **2**

[Simulación](#_54cuehrev80v) 2

[1.1 Sistemas, clasificación y componentes.](#_r59j6wt8ipz4) 2

[1.2 Modelo matemático de un sistema. Uso de modelos matemáticos para el análisis o la toma de decisiones en relación al comportamiento de sistemas. Tratamiento analítico versus tratamiento numérico de un modelo matemático.](#_jtx343ni05l4) 3

[1.3 La simulación como técnica numérica que permite experimentar acerca del comportamiento de un sistema dinámico siguiendo la evolución en el tiempo de un modelo matemático del sistema en estudio.](#_63mlsc8vhii2) 3

[Ventajas y desventajas de la simulación.](#_9nltfa1blc28) 3

[1.4 Pasos involucrados en la realización de un estudio de simulación](#_xlg26nqaj6c6) 4

[**Unidad temática 2**](#_yziqnliwcvjm) **4**

[2.1 Identificación de la distribución de probabilidad de una variable aleatoria. Pruebas de bondad de ajuste.](#_8qtw1x4qg6mh) 4

[2.2 Algoritmos generadores de números seudo-aleatorios. Distintos tipos. Propiedades fundamentales.](#_o1yqlrrjjmd) 5

[2.3 Métodos para generar valores de variables aleatorias discretas y continuas con distribución teórica conocida o a partir de distribuciones empíricas.](#_hao026afcbim) 5

[**Unidad temática 3**](#_z1gncaut11z7) **5**

[3.1 Sistemas de eventos discretos.](#_zd466f2o509q) 5

[Los sistemas de espera (colas) ¿Modelos de sistemas de colas con solución analítica conocida.?](#_3of0tuuuvimr) 5

[Simulación de sistemas de eventos discretos.](#_g3hqma2u7q05) 6

[3.2 Distintos enfoques para la construcción de modelos de eventos discretos: orientación a los eventos , orientación a los procesos. Mecanismos de avance en el tiempo.](#_t56eepe4k0z) 6

[3.3 Obtención y evaluación de los datos de entrada del modelo.](#_fe9ycp178z6m) 6

[3.4 Software de Simulación. Lenguajes de simulación versus simuladores. Visualización y animación en Simulación.](#_5qtd5tskcle9) 6

[3.5 Herramientas para la validación y verificación del modelo de simulación.](#_h1xj2ycow836) 6

[3.6 Casos de estudio.](#_3h0y5cm1r9eu) 6

[**Unidad temática 4**](#_yvkjgkdohrd) **6**

[**Unidad temática 5**](#_72mbcqwa1d3g) **7**

[**SEGÚN CONSULTA**](#_qkdbiw7obmyy) **7**

[Descripción clase de consulta](#_pqk75599m4lw) 7

# Unidad temática 1

***Eje Conceptual:*** *El proceso de simulación.*

***Objetivo:*** *Presentar la técnica de simulación como herramienta para sustentar la toma de decisiones en relación a sistemas dinámicos y comprender el proceso que implica su aplicación.*

## Simulación

**Simulación a eventos discretos** , el conjunto de relaciones lógicas, matemáticas y probabilísticas que integran el comportamiento de un sistema bajo estudio cuando se presenta un evento determinado. El objetivo del modelo de simulación consiste, en comprender, analizar y mejorar las condiciones de operación relevantes del sistema.

## 1.1 Sistemas, clasificación y componentes.

**Sistema**, se trata de un conjunto de elementos que se interrelacionan para funcionar como un todo desde el punto de vista de la simulación, tales elementos deben tener una frontera clara. Cada uno puede dividirse en elementos que son relevantes para la construcción de lo que constituirá su modelo de simulación; entre ellos tenemos entidades, estado del sistema, eventos actuales y futuros, localizaciones, recursos, atributos, variables y reloj de la simulación.

Una **entidad** es la representación de los flujos de entrada al sistema, este es el elemento responsable de que el estado del sistema cambie.

El **estado del sistema** es la condición que guarda el sistema bajo estudio en un momento determinado; fotografía de lo que está pasando en el sistema en cierto instante. Se compone de variables o características de operación puntuales y de variables o características de operación acumuladas, o promedio.

Un **evento** es un cambio en el estado actual del sistema, como la entrada o salida de una entidad, finalización de un proceso. Se califican en dos tipos: **eventos actuales**, que son aquellos que están sucediendo en el sistema en un momento dado, y **eventos futuros**, que son cambios que se representarán en el sistema después del tiempo de simulación, de acuerdo con la programación específica.

Las  **localizaciones** son todos aquellos lugares en los que una “pieza” puede detenerse para ser transformada o esperar a serlo.

Los **recursos** son aquellos dispositivos - distintos de localizaciones - necesarios para llevar a cabo una operación.

Un **atributo** característica de una entidad.

Las  **variables** son condiciones cuyos valores se crean y modifican por medio de ecuaciones matemáticas y relaciones lógicas. Pueden ser continuas o discretas.

El **reloj de la simulación** es el contador de tiempo de la simulación, función => responder cuánto tiempo se ha utilizado en el modelo y cuanto tiempo total requiere . Se relaciona con la tabla de eventos futuros.

**Reloj de la simulación absoluto** parte de cero y termina en un tiempo total de simulación definido y el **reloj de simulación relativo** tiempo entre dos eventos.

Los **modelos** representan situaciones reales de diferentes tipos. Físicos o modelos matemáticos.

Se diferencian también según el tipo de ecuaciones matemáticas que lo componen, **modelos continuos** las relaciones entre variables se definen por medio de ecuaciones diferenciales, permiten conocer el comportamiento de las variables en un lapso de tiempo continuo. Y en los **modelos discretos**, el comportamiento se representa por medio de ecuaciones evaluadas en un punto determinado.

Otro tipo de clasificación es **modelos dinámicos**, que son aquellos en los que el estado del sistema cambia con respecto al tiempo. Y los **modelos estáticos** representan un conjunto de situaciones o condiciones determinadas (Ej un dado), este tipo de simulación se la conoce como Simulación de Monte Carlo.

Los **modelos determinísticos** refieren a relaciones constantes entre los cambios de las variables del modelo. Y **modelos probabilísticos o estocásticos** se da una distribución de probabilidad en el proceso.

**Réplica o corrida** cuando ejecutamos el modelo en una ocasión.

El **estado transitorio** se presenta al principio de la simulación, hay mucha variación entre los valores promedios de las variables de decisión, por lo que formular conclusiones con base a ellos sería muy arriesgado. Y en el **estado estable** los valores de las variables de decisión permanecen muy estables, variaciones poco significativas. En este momento las decisiones son mucho más confiables. No todas las variables convergen al estado estable con la misma rapidez.

Otros factores importantes son el tiempo de simulación y el costo de corrida

## 1.2 Modelo matemático de un sistema. Uso de modelos matemáticos para el análisis o la toma de decisiones en relación al comportamiento de sistemas. Tratamiento analítico versus tratamiento numérico de un modelo matemático.

⇒ Experimentar con el sistema real vs Experimentar con un modelo del sistema:

Si es posible y rentable alterar físicamente el sistema y luego dejarlo operar bajo las nuevas condiciones, probablemente sea lo mejor. Esto, pocas veces sucede. Suele ser muy costoso o perjudicial para el sistema, o simplemente el sistema puede no existir. Por eso generalmente se usan los modelos.

⇒ Modelo físico vs Modelo matemático:

Muchas veces armar un modelo físico que represente lo más posible al sistema puede ser útil, pero no es típicamente el modelo que se utilice. La mayoría de los modelos son matemáticos, representando al sistema con relaciones lógicas y cuantitativas que se manipulan y cambian para entender como reacciona el modelo, y como reaccionaría el sistema si este estuviese correcto.

⇒ Solucion analitica vs Simulación:

Construido el modelo matemático, se debe usar para responder preguntas de interés del sistema que representa. Si el modelo es simple, pueden usarse métodos matemáticos para responder estas preguntas y así llegar a las soluciones analiticas. Cuando los sistemas son complejos o no hay métodos matemáticos que se puedan aplicar, el estudio se da a través de la simulación.

## 1.3 La simulación como técnica numérica que permite experimentar acerca del comportamiento de un sistema dinámico siguiendo la evolución en el tiempo de un modelo matemático del sistema en estudio.

## Ventajas y desventajas de la simulación.

Ventajas de la Simulación

* Conocer el impacto de los cambios sin llevarlos a la realidad.
* Mejora el conocimiento del proceso actual, permite ver como se comporta el modelo en diferentes escenarios.
* Medio de capacitación para la toma de decisiones.
* Es más económico hacer un estudio de la simulación que hacer muchos cambios en los procesos reales.
* Permite probar varios escenarios.
* En problemas de gran complejidad, permite generar una buena solución.
* Los paquetes de software tienden a ser más sencillos y facilitan su aplicación.
* Gracias a las herramientas permite ver cómo se comportará un proceso mejorado.

Desventajas de la Simulación

* Simulación no es una herramienta de optimización¿?
* Puede ser costoso emplearla en problemas relativamente sencillos de resolver.
* Se requiere de bastante tiempo para realizar un buen estudio de la simulación, puede que el analista no tenga esa disponibilidad.
* Se requiere que el analista domine la herramienta y que tenga sólidos conocimientos de estadística para interpretar los resultados.

## 1.4 Pasos involucrados en la realización de un estudio de simulación

* **Definición del sistema bajo estudio:** Conocer el sistema a modelar. Información necesaria para lograr un modelo conceptual del sistema bajo estudio.
* **Generacion del modelo de simulacion base:** Un modelo base, no muy detallado.
* **Recolección y análisis de datos:** Recopilación de la información estadística de las variables. Qué información es útil para la determinación de las distribuciones de probabilidad.
* **Generación del modelo preliminar:** Se integra la información del análisis de datos + supuestos del modelo + datos que se quieran tener en cuenta para que el modelo sea lo más cercano a la realidad.
* **Verificación del modelo:** Verificación de datos para comprobar la programación y que los parámetros usados funcionen correctamente.
* **Validación del modelo:** Comparación con la realidad. Se realizan pruebas utilizando información real y se observa comportamiento y resultados.
* **Generación del modelo final:** Una vez validado, se puede realizar la simulación y estudiar el comportamiento del proceso. Este será el “Modelo Raíz”.
* **Determinación de los escenarios para el análisis:** Se acuerda con el cliente los escenarios a analizar. Se pueden utilizar un escenario pesimista, uno optimista y uno intermedio.
* **Análisis de sensibilidad:** Obtenidos los resultados de los escenarios se realizan las pruebas estadísticas que permitan comparar los escenarios con los mejores resultados finales.
* **Documentación del modelo, sugerencias y conclusiones:** Realizado el análisis de los resultados se realiza la documentación del mismo. Permitirá un mejor uso del modelo en caso de ajustes futuros. Se incluyen supuestos, distribuciones de probabilidad, alcances y limitaciones, sugerencias, y conclusiones del proyecto.

# **Unidad temática 2**

## 2.1 Identificación de la distribución de probabilidad de una variable aleatoria. Pruebas de bondad de ajuste.

## 2.2 Algoritmos generadores de números seudo-aleatorios. Distintos tipos. Propiedades fundamentales.

## 2.3 Métodos para generar valores de variables aleatorias discretas y continuas con distribución teórica conocida o a partir de distribuciones empíricas.

# **Unidad temática 3**

## 3.1 Sistemas de eventos discretos.

## Los sistemas de espera (colas) ¿Modelos de sistemas de colas con solución analítica conocida.?

**Características de un sistema de colas.**

* Una población de clientes.
* Proceso de llegadas, forma en la que llegan los clientes.
* Un proceso de colas. La manera en que los clientes esperan para ser atendidos y la forma en la que son elegidos para el servicio.
* Un proceso de servicio.
* Un proceso de salida. Pueden salir completamente del sistema o pueden ser procesados en otra “estación”, red de colas.

**La población de clientes**

“Tamaño de la población”, si es muy grande se la considera infinita, es más complicado el análisis con poblaciones finitas que con infinitas.

**El proceso de llegada**

Forma en que llegan a solicitar el servicio, importante “tiempo entre llegadas”.

Existen dos clases de tiempo entre llegadas:

* Deterministico, intervalo de tiempo, fijo y conocido.
* Probabilístico, el tiempo entre llegadas es incierto y variable. Se describen con una distribución de probabilidad.

**λ** Número promedio de llegadas por unidad de tiempo.

**El proceso de Colas**

Forma en la que los clientes esperan, puede ser en una sola fila o en varias filas. también el número de clientes que pueden esperar. Las condiciones de espacio de espera finito o infinito requieren de análisis matemáticos diferentes.

Otra característica es la disciplina de colas, forma en la que esperan a ser atendidos:

* Primero en entrar, primero en salir (peps / fifo)
* Último en en entrar primero en salir(ueps)
* Selección de prioridad

**El proceso de servicio**

Como son atendidos los clientes. Pueden ser de canal múltiple o de canal simple. Se pueden atender varios clientes al mismo tiempo en una estación. ¿Se permite la prioridad?. Se necesita saber cuánto tiempo se necesita para llevar a cabo el servicio. Como las llegadas pueden ser determinísticas o probabilísticas, con un tiempo de servicio probabilístico cada cliente requiere la misma cantidad de tiempo y con un servicio probabilístico, cada cliente requiere una cantidad distinta e incierta de tiempo de servicio.

**𝜇** número promedio de clientes atendidos por unidad de tiempo.

**Clasificaciones de los modelos de colas**

Los símbolos describen las características del sistema:

* El proceso de llegada, tiempo entre llegadas
  + - D tiempo de llegada determinístico
    - M tiempos entre llegadas probabilísticos y siguen una distribución exponencial
    - G tiempos entre llegadas probabilísticos y una distribución diferente a exponencial
* El proceso de servicio, distribución de tiempos de servicio
  + - D servicio determinístico
    - M tiempos de servicio probabilísticos con una distribución exponencial
    - G tiempos de servicio probabilísticos con una distribución distinta a exponencial
* El proceso de colas, cuantas estaciones o canales existen en el sistema.
* Un número K, máximo de clientes que pueden existir en el sistema
* Un número L, total de clientes en la población.

**Medidas de rendimiento**

Valor numérico que se utiliza para evaluar los méritos de un sistema de colas en estado estable.

* Tiempo promedio de espera **Wq**
* Tiempo promedio en el sistema **W**
* Longitud media de la cola **Lq**
* Número medio en el sistema **L**
* Probabilidad de bloqueo **p**
* Utilización **U**

VER SI TOMA TEMA FORMULAS (relaciones entre las medidas de rendimiento)

## Simulación de sistemas de eventos discretos.

## 3.2 Distintos enfoques para la construcción de modelos de eventos discretos: orientación a los eventos , orientación a los procesos. Mecanismos de avance en el tiempo.

## 3.3 Obtención y evaluación de los datos de entrada del modelo.

## 3.4 Software de Simulación. Lenguajes de simulación versus simuladores. Visualización y animación en Simulación.

## 3.5 Herramientas para la validación y verificación del modelo de simulación.

## 3.6 Casos de estudio.

**M/M/1**

# **Unidad temática 4**

4.1 Importancia del diseño de los experimentos de simulación. Diferencias entre experimentos físicos y experimentos de simulación. Planificación estratégica versus planificación táctica del experimento.

4.2 Experimentos mono y multifactoriales.

4.3 Tipos de simulación con respecto al análisis de resultados: simulaciones terminales y de estado estacionario. Medidas de rendimiento apropiadas en cada caso.

4.4 Estimación puntual y por intervalos de confianza de las medidas de rendimiento. Procedimientos a aplicar según se trate de un estudio terminal o de estado estacionario y según el número de configuraciones alternativas del sistema a comparar Métodos de reducción de varianza.

4.5 Casos de estudio

# **Unidad temática 5**

5.1 Simulación de sistemas continuos y mixtos.

5.2 Simulación de Monte Carlo.

5.3 Otros tipos de Simulación.

# SEGÚN CONSULTA

## Descripción clase de consulta

Neylor “Generación de números aleatorios” = distribuciones de probabilidad, como se generan los números aleatorios, distribuciones de probabilidad, generación de congruencia lineal.Distribuciones Exponencial, poisson, binomial, triangular.

Primera parte “Simulación básica”, a experimentos discretos, avance de tiempos, gráficos a lo largo del tiempo, medidas de rendimiento, Utilización del servicio = tiempo promedio que se utiliza el servidor(que está ocupado)

Como son las rutinas o como se piensan? en cada uno de los procesos. Análisis de salida.

Simulación sistema de inventario, “revisión periódica”, se define un periodo de tiempo, por ejemplo un mes, y cada un mes de revisión y se toma nota de los productos que hay. Lo “malo” que en revisión la mercadería está debajo del punto pedido, por eso este sistema trabaja con consideración de faltante. Análisis de cómo se piensa el análisis de cuando está en negativo, análisis de la salida. Cuánto vamos a permitir de mínimo y cuánto de máximo. “s” punto pedido /// “S” tope. Tienen costo de preparación, holding y shortish (mientras hay pérdida) se suma las 3 para promedio total

Corrida de simulación, “una sola muestra”, muchas iteraciones, sacamos promedio = una muestra, Se necesitan ejecutar varias muestras para tener valores que sirvan. Estudiar escenarios, comparar escenarios, “Con que policits me quedo”.

Conceptos básicos simulación, 10 pasos de la simulación.

Desarrollo analitico del modelo de colas. fórmulas del modelo de una cola , conocer significado lambda y mu, análisis MM1. Como funciona lambda y mu en MMC, no formulas, entender como se diferencia con MM1.

Interpretación de medidas de rendimiento, análisis de costos y “planteo de ejemplo” de costos.

La denegación de servicio, ¿Que pasa? cuando se llena la cola, como se calcula. ANÁLISIS ECONÓMICO.

Análisis de las salidas de la simulación , una corrida es UNA SOLA muestra, se necesitan “n” corridas. Se toman múltiples muestras independientes entre sí, Ejecutar varias corridas y lograr esta cuestión estadística. Luego de n réplicas, arrancando cada una con una semilla aleatoria diferente. Evaluar una simulación. Para saber que tan bien funciona un escenario se necesita un intervalo de confianza, no basta con un promedio. Solo así se garantiza que una simulación represente a la realidad.

Estado transiente y estacionario, la simulación recorre un estado transitorio y transiente hasta que llega a un estado estable. Como se calculan los intervalos de confianza.

Si quiero calcular el intervalo con un error predefinido, ¿Cuántas corridas tengo que hacer? “Beta” valor absoluto , “gama” error porcentual. Si yo quisiera un error de …. ¿Cuántas corridas tengo que hacer? Factor de utilización. Como comparar dos sistemas, intervalos de confianza de cada sistema y luego test de medias para comparar si las medias poblacionales que generan los escenarios diferentes. Hecho eso tenés dos distribuciones y verificas los valores. “Ver como funciona para dos casos”