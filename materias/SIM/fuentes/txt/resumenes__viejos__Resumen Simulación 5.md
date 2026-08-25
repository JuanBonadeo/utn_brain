Resumen de Simulación

Índice

[Capítulo 1: Introducción a la simulación en computadoras (Naylor) 2](#_Toc363319714)

[Definición de la simulación en computadoras 2](#_Toc363319715)

[Fundamentos racionales de la simulación en computadoras 2](#_Toc363319716)

[Propiedades de los modelos de simulación 3](#_Toc363319717)

[Clasificación de los modelos para simulación 3](#_Toc363319718)

[Capítulo 2: Planeación de los experimentos de simulación en computadora (Naylor) 3](#_Toc363319719)

[Etapas de la simulación 3](#_Toc363319720)

[1)Formulación del problema 3](#_Toc363319721)

[2)Recolección y procesamiento de datos tomados de la realidad 4](#_Toc363319722)

[3)Formulación de los modelos matemáticos 4](#_Toc363319723)

[4)Estimación de los parámetros de las características operacionales a partir de los datos reales 4](#_Toc363319724)

[5)Evaluación del modelo y de los parámetros estimados 5](#_Toc363319725)

[6)Formulación de un programa para la computadora 5](#_Toc363319726)

[7)Validación 5](#_Toc363319727)

[8)Diseño de los experimentos de simulación 5](#_Toc363319728)

[9)Análisis de los datos simulados 5](#_Toc363319729)

[Capítulo 3: Técnicas para la generación de los números aleatorios (Naylor) 5](#_Toc363319730)

[Introducción 5](#_Toc363319731)

[Métodos de congruencias para generar números pseudo-aleatorios 6](#_Toc363319732)

[Pruebas estadísticas para los números pseudo-aleatorios 7](#_Toc363319733)

[Capítulo 4: Generación de valores de las variables estocásticas empleadas en simulación (Naylor) 8](#_Toc363319734)

[Introducción 8](#_Toc363319735)

[Distribuciones continúas de probabilidad 9](#_Toc363319736)

[Distribuciones discretas de probabilidad 11](#_Toc363319737)

[Capítulo 1: Modelado de Simulación Básico (Law & Kelton) 12](#_Toc363319738)

[La naturaleza de la simulación 12](#_Toc363319739)

[Sistemas, modelos y simulación 12](#_Toc363319740)

[Simulación de Eventos Discretos: 13](#_Toc363319741)

[Simulación de un Sistema de Colas de un solo Servidor (M/M/1): 14](#_Toc363319742)

[Reglas de interrupción alternativas 16](#_Toc363319743)

[Determinando los eventos y variables 16](#_Toc363319744)

[Simulación distribuida 16](#_Toc363319745)

[Pasos en un estudio de simulación 16](#_Toc363319746)

[Otros tipos de simulación 17](#_Toc363319747)

[Ventajas, desventajas y dificultades de la simulación 17](#_Toc363319748)

[Capítulo 9: Modelo Analítico para una cola M/M/1 (Mc Millan - Gonzalez). 17](#_Toc363319749)

[Tipos de sistemas de colas: 17](#_Toc363319750)

[Caso M/M/1: 18](#_Toc363319751)

[Medidas de rendimiento: 20](#_Toc363319752)

[Capítulo 15: Verificación de los resultados de simulación (Gordon) 21](#_Toc363319753)

[Naturaleza del problema 21](#_Toc363319754)

[Métodos de estimación 21](#_Toc363319755)

[Estadísticas de corridas de simulación 22](#_Toc363319756)

[Repetición de corridas 22](#_Toc363319757)

[Eliminación del sesgo inicial 22](#_Toc363319758)

[Medias de lotes 22](#_Toc363319759)

[Análisis de series de tiempo 23](#_Toc363319760)

[Análisis espectral 23](#_Toc363319761)

[Capítulo 9: Análisis de Datos de Salida (Law & Kelton) 23](#_Toc363319762)

[Comportamiento transitorio y en estado estacionario de un proceso estocástico 24](#_Toc363319763)

[Tipos de simulaciones con respecto al análisis de la salida 24](#_Toc363319764)

[Análisis Estadístico para Simulaciones Terminales 25](#_Toc363319765)

[Múltiples medidas de rendimiento 27](#_Toc363319766)

[Resumen: Construcción de Intervalos de Confianza 27](#_Toc363319767)

[Capítulo 10: Comparando las configuraciones del sistema alternativas (Law & Kelton) 27](#_Toc363319768)

[Introducción 27](#_Toc363319769)

[Intervalos de confianza para la diferencia entre las medidas de rendimiento de 2 sistemas 27](#_Toc363319770)

[Intervalos de confianza para comparar más de 2 sistemas 29](#_Toc363319771)

# Capítulo 1: Introducción a la simulación en computadoras (Naylor)

## Definición de la simulación en computadoras

Simulación es una técnica numérica para conducir experimentos en una computadora digital, los cuales requieren ciertos tipos de modelos lógicos y matemáticos, que describen el comportamiento de un negocio o un sistema económico en períodos extensos de tiempo real.

Variantes:

* Juegos operacionales: simulaciones que se caracterizan por alguna forma de interés en conflicto entre los jugadores o los seres humanos que toman decisiones dentro del marco de referencia del medio ambiente simulado. Dentro de estos se encuentran los juegos militares y los juegos de gerencia.
* Análisis de Monte Carlo: es una técnica de simulación para problemas que tienen una base estocástica o probabilística. Existen 2 tipos: aquellos problemas que implican algún tipo de proceso estocástico y aquellos problemas matemáticos completamente determinísticos, que no pueden resolverse fácilmente por métodos estrictamente determinísticos.

## Fundamentos racionales de la simulación en computadoras

* Búsqueda constante del hombre por adquirir conocimientos relativos a la predicción del futuro.
* Puede ser imposible o extremadamente costoso observar ciertos procesos en el mundo real.
* El sistema observado puede ser tan complejo que sea imposible describirlo en términos de un sistema de ecuaciones matemáticas.
* Puede no obtenerse una solución del modelo por medio de técnicas analíticas directas.
* Resultaría casi imposible o muy costoso realizar experimentos de validación en los modelos matemáticos que describen al sistema.

Otras razones:

* La simulación hace posible estudiar y experimentar con las complejas interacciones que ocurren en el interior de un sistema dado.
* A través de la simulación se pueden estudiar los efectos de ciertos cambios en la operación de un sistema.
* La observación detallada del sistema que se está simulando, conduce a un mejor entendimiento del mismo y proporciona sugestiones para mejorarlo.
* La simulación puede utilizarse como recurso pedagógico.
* Los juegos operacionales han demostrado constituir un medio excelente para estimular el interés y el entendimiento de parte del participante y son particularmente útiles en la orientación de las personas con experiencia en la disciplina relativa al juego.
* La experiencia que se adquiere al diseñar un modelo de simulación en una computadora, puede ser más valiosa que la simulación en sí misma.
* La simulación de sistemas complejos puede producir un valioso y profundo conocimiento acerca de cuáles variables son más importantes y como ellos obran entre sí.
* La simulación puede emplearse para experimentar con situaciones nuevas.
* La simulación puede servir como una prueba de pre-servicio.
* Proporcionan una forma conveniente de dividir un sistema complicado en subsistemas.
* Para ciertos tipos de problemas estocásticos, la secuencia de los eventos puede ser muy importante.
* Las simulaciones de Monte Carlo pueden realizarse para verificar soluciones analíticas.
* La simulación permite estudiar los sistemas dinámicos.
* Cuando se presentan nuevos componentes de un sistema, la simulación puede emplearse para ayudar a descubrir los obstáculos y otros problemas.
* La simulación convierte a los especialistas en técnicos generales.

## Propiedades de los modelos de simulación

El objeto del modelo científico es permitir al analista la determinación de uno o más cambios en los aspectos del sistema modelado que afectan otros aspectos del sistema. Para que un modelo científico sea útil, debe ser realista (debe servir como una aproximación razonable al sistema real y debe incorporar la mayor parte de los aspectos importantes de este) y simple.

Los modelos constan de 4 elementos: componentes, variables, parámetros y relaciones funcionales.

Los componentes de los modelos económicos tienden a variar ampliamente. (Son los elementos del sistema que se estudiarán)

Las variables relacionan un componente con otro y se clasifican en:

* *Exógenas*: son las independientes o de entrada, han sido predeterminadas y proporcionadas independientemente del sistema que se modela. Actúan sobre el sistema, pero no reciben acción alguna de parte de él. Se subdividen en controlables y no controlables, según sean susceptibles de manipulación o control por quienes toman decisiones o crean políticas para el sistema.
* *De estado*: describen el estado de un sistema o uno de sus componentes. Interaccionan con las variables exógenas y endógenas, de acuerdo a relaciones funcionales. El valor de una variable de estado puede depender no solo de variables exógenas, sino también de ciertas variables de salida en períodos anteriores. En estos casos decimos que ocurre una retroalimentación.
* *Endógenas*: son las dependientes o de salida del sistema y son generadas por la interacción de las variables exógenas con las de estado.

La clasificación de la variable depende del propósito de la investigación. Las variables exógenas se pueden tratar como parámetros, las cuales tienen que estimarse con anterioridad, o como variables estocásticas, pudiendo ser generadas por computadora.

Los parámetros se denominan factores, los cuales se varían para ver sus efectos sobre las variables endógenas.

Hay 2 relaciones funcionales que describen la interacción de las variables y los componentes, usados para generar el comportamiento del sistema:

* *Identidades*: tomarán la forma de definiciones o declaraciones tautológicas, relativas a los componentes del modelo.
* *Característica de operación*: es una hipótesis que relaciona las variables endógenas y de estado con sus variables exógenas. En los procesos estocásticos toman la forma de funciones de densidad de probabilidad. Los parámetros de las características de operación los derivamos sobre la base de inferencias estadísticas.

## Clasificación de los modelos para simulación

Modelos determinísticos: Ni las variables exógenas ni a las endógenas se les permite ser variables al azar. Se suponen relaciones exactas para las características de operación. Es posible resolverlos analíticamente.

Modelos estocásticos: Aquellos modelos en los que por lo menos una de las características de operación está dada por una función de probabilidad. Son más complejos que los modelos determinísticos.

Modelos estáticos: No toman en cuenta la variable tiempo.

Modelos dinámicos: Modelos matemáticos que tratan de las interacciones que varían con el tiempo.

# Capítulo 2: Planeación de los experimentos de simulación en computadora (Naylor)

La decisión de emplear la simulación como técnica para resolver un problema no es una tarea sencilla. Tal decisión se apoya en la aplicabilidad, el costo y la simplicidad.

## Etapas de la simulación

### Formulación del problema

Deben tomarse 2 decisiones importantes antes de comenzar a trabajar con cualquier experimento de simulación: hay que decidir los objetivos de nuestra investigación y es necesario decidir el conjunto de criterios para evaluar el grado de satisfacción al que deba sujetarse el experimento.

### Recolección y procesamiento de datos tomados de la realidad

Razones por las cuales es necesario disponer de un sistema eficiente para el procesamiento de datos:

* La información descriptiva y cuantitativa constituye un requisito previo a la formulación del problema.
* Los datos que hayan sido reducidos a una forma significativa pueden sugerir hipótesis de cierta validez, las cuales se usarán en la formulación de los modelos matemáticos.
* Los datos también pueden sugerir mejoras o refinamientos en los modelos matemáticos que existen en el sistema por simularse.
* Es necesario que los datos se utilicen para estimar los parámetros de las características de operación relativas a las variables endógenas, exógenas y de estado del sistema.
* Sin tales datos sería imposible probar la validez de un modelo para la simulación.

Funciones del procesamiento de datos:

* *Recolección*: proceso de captación de los hechos disponibles.
* *Almacenamiento* de los datos recolectados.
* *Conversión* de los datos de una forma a otra.
* *Transmisión* de la información al lugar en donde será procesada.
* *Manipulación*: operaciones como clasificar, cotejar, intercalar, recuperar información y otras, como las operaciones aritméticas y lógicas.
* *Salida*: informe sobre los resultados obtenidos.

### Formulación de los modelos matemáticos

Consiste en:

1. Especificación de los componentes.
2. Especificación de las variables y los parámetros.
3. Especificación de las relaciones funcionales.

Consideraciones a tener en cuenta:

* Cantidad de variables que se deben incluir en el modelo: Hay poca dificultad con las variables endógenas. La dificultad surge en la elección de las variables exógenas. Pocas variables pueden llevar a modelos inválidos, una abundancia hace imposible la simulación.
* Complejidad: Estamos interesados en la formulación de modelos matemáticos que produzcan descripciones o predicciones, razonablemente exactas, referentes al comportamiento de un sistema dado y reduzcan a la vez, el tiempo de computación y programación.
* Cantidad de tiempo de cómputo requerida para lograr algún objetivo experimental específico: los objetivos pueden ser:
  + Reducir el tiempo de cómputo requerido para generar los valores de nuestras variables endógenas sobre un período específico.
  + Reducir el tiempo de computación requerido para lograr algún nivel de precisión estadística previamente determinado.
* El tiempo consumido en la programación de la computadora.
* Cantidad de realismo incorporado en ellos.
* Compatibilidad con el tipo de experimentos que se van a realizar con ellos.

Dificultades potenciales:

* Quizás sea imposible cuantificar o medir ciertos tipos de variables.
* El número de variables posiblemente exceda la capacidad de la computadora.
* Podemos desconocer algunas de las variables exógenas significativas.
* Podemos desconocer algunas de las relaciones entre variables exógenas y endógenas.
* Las relaciones entre las variables que afectan el comportamiento del sistema son en muchos casos tan complejas que no pueden expresarse como una o más ecuaciones matemáticas.

Tipos básicos de diseño:

* Diseños generalizados: describe el comportamiento de un sistema completo.
* Diseños modulares o de bloques: conjunto de modelos que describen los componentes principales del sistema.

### Estimación de los parámetros de las características operacionales a partir de los datos reales

Se estiman los valores de los parámetros de los modelos y se prueba su significación estadística.

### Evaluación del modelo y de los parámetros estimados

Es necesario hacer un juicio del valor inicial de la suficiencia de nuestro modelo una vez que formulamos un conjunto de modelos matemáticos y estimamos los parámetros. Nuestro interés reside en probar las suposiciones o entradas que se programarán en la computadora.

### Formulación de un programa para la computadora

Se deben considerar las siguientes actividades:

1. *Diagrama de flujo*: bosqueja la secuencia lógica de los eventos que realizará la computadora.
2. *Lenguaje de la computadora*: una vez terminado el diagrama de flujo, se puede escribir el código para la computadora. Se pueden usar lenguajes de propósitos generales o lenguajes de simulación de propósitos específicos. Estos últimos permiten un ahorro en tiempo de programación.
3. *Búsqueda de errores*: los lenguajes de simulación de propósitos específicos proporcionan técnicas para la búsqueda de errores superiores a las provistas por los lenguajes de propósitos generales.
4. *Datos de entrada y condiciones iniciales*: se debe determinar el valor que se les debería asignar a las variables y parámetros del modelo en el momento en que comenzamos a simular el sistema.
5. *Generación de datos*: consiste en el desarrollo de técnicas numéricas para la generación de datos.
6. *Reportes de salida*: necesarios para dar la información relativa al comportamiento de nuestro sistema bajo simulación.

### Validación

Implica un sinnúmero de complejidades de tipo práctico, teórico, estadístico e inclusive filosófica. Hay 2 pruebas para validar los modelos de simulación:

* ¿Qué tan bien coinciden los valores simulados de las variables endógenas con datos históricos conocidos?
* ¿Qué tan exactas son las predicciones del comportamiento del sistema real hechas por el modelo de simulación, para períodos futuros?

### Diseño de los experimentos de simulación

Metas:

* Seleccionar los niveles de los factores y las combinaciones de niveles, así como el orden de los experimentos.
* Asegurar que los resultados queden razonablemente libres de errores fortuitos.

### Análisis de los datos simulados

Pasos:

* Recolección y procesamiento de los datos simulados.
* Cálculo de la estadística de las pruebas.
* Interpretación de los resultados.

# Capítulo 3: Técnicas para la generación de los números aleatorios (Naylor)

## Introducción

El término *variable aleatoria* se emplea para nombrar una función de valor real, definida sobre un espacio muestral asociado con los resultados de un experimento conceptual de naturaleza azarosa. El resultado particular de un experimento se llama *valor de la variable aleatoria*. F(x), la función de la distribución acumulativa para una variable aleatoria X, indica la probabilidad de que X sea menor o igual al particular valor x de la variable aleatoria. f(x) representa el valor de la función de densidad de probabilidad de la variable aleatoria X cuando X = x.

Función de densidad de probabilidad uniforme:

Los valores de x, en el intervalo unitario, se llamarán *valores uniformes de las variables aleatorias*.

En la práctica, se suelen requerir *sucesiones de números aleatorios*, y uno de los requisitos principales es el de la independencia estadística.

Métodos para generar sucesiones de números aleatorios:

* *Métodos manuales*: son menos prácticos, más simples y muy lentos. Es imposible de reproducir una sucesión.
* *Tablas de biblioteca*: tuvieron que ser generados con uno de los otros métodos. Siempre pueden reproducirse. No son rápidos. Ciertos problemas requieren más números de los publicados.
* *Métodos de computación analógica*: son mucho más rápidos. Las sucesiones no son reproducibles.
* *Métodos de computación digital*
  + *Provisión externa*: graba las tablas de números aleatorios en una cinta magnética.
  + *Generación interna por medio de procesos físicos aleatorios*: uso de un aditamento especial de la computadora digital capaz de registrar los resultados de algún proceso aleatorio y además reduzca estos resultados a sucesiones de dígitos. No se pueden reproducir. Los procesos aleatorios pueden salirse de control.
  + *Generación interna por medio de una relación de recurrencia*: generación de los números pseudo-aleatorios por medio de una transformación indefinidamente continuada, aplicada a un grupo de números elegidos en forma arbitraria.

En el método de los *cuadrados centrales*, cada número de la sucesión se obtiene tomando los dígitos centrales del cuadrado del número precedente. Resultó difícil de analizarse, relativamente lento y estadísticamente poco satisfactorio. (La semilla debe tener 3 o más dígitos. Este método tiende a números cada vez más pequeños.)

Un método para generar números aleatorios debe producir sucesiones de números que sean:

* Uniformemente distribuidos.
* Estadísticamente independientes.
* Reproducibles.
* Sin repetición dentro de una longitud determinada de la sucesión.
* Generar números aleatorios a grandes velocidades.
* Requerir un mínimo de la capacidad de almacenamiento.

Procedimiento para generar números aleatorios:

1. Un proceso que produce números aproximadamente aleatorios.
2. Un proceso, que aplicado a las sucesiones de números, mejore la aleatoriedad de la sucesión.
3. Un conjunto de pruebas de aleatoriedad.
4. El uso de un método de almacenamiento que permita leer una gran cantidad de números aleatorios a una velocidad proporcional a su velocidad de operación.

## Métodos de congruencias para generar números pseudo-aleatorios

Son métodos determinísticos, ya que los procesos aritméticos que se incluyen en los cálculos determinan unívocamente cada término de la sucesión de números. Aunque estos procesos no son del todo aleatorios, las sucesiones que resultan de ellos superan las pruebas estadísticas, por lo que nos permiten considerarlos como si en efecto lo fueran.

Se basan en una relación fundamental de congruencia , donde , a, c y m son enteros no negativos.

Los términos ni son todos enteros y para toda ni. A partir de la sucesión { ni }, se pueden obtener números racionales en el intervalo ( 0,1 ), { ri } = { ni/m }.

Existe un mínimo valor positivo para i, h, tal que nh = n0 en donde h es el *período* de la sucesión {ni}. El valor máximo de h depende de m. Es imposible obtener sucesiones que no se repiten, utilizando los métodos de congruencias.

Método aditivo de congruencias: Presupone k valores iniciales

Si k = 1 genera la sucesión de Fibonacci. Este es el único método que produce períodos mayores que m.

Método multiplicativo de congruencias:

Es un caso especial de la relación de congruencia, con c = 0.

Método mixto de congruencias: Tanto a como c son mayores a cero. Su principal ventaja radica en su período completo. Las condiciones que se imponen sobre a y c, a fin de lograr un período completo para m:

* c y m son primos relativos.
* si p es un factor primo de m.
* si 4 es un factor de m.

## Pruebas estadísticas para los números pseudo-aleatorios

Las propiedades estadísticas de los números pseudo-aleatorios generados por los métodos que se han delineado deben coincidir con las propiedades estadísticas de los generados por un instrumento aleatorio idealizado. En la medida en que nuestros números pseudo-aleatorios puedan pasar las pruebas estadísticas, denotadas por el instrumento aleatorio idealizado, estos números pseudo-aleatorios pueden tratarse como verdaderos números aleatorios aunque no lo sean.

Prueba de la frecuencia

Se usa para comprobar la uniformidad de una sucesión de M conjuntos consecutivos de N números pseudo-aleatorios. Para cada conjunto dividimos el intervalo (0, 1) en x sub-intervalos iguales. El número esperado de números pseudo-aleatorios que se encontrarán en cada sub-intervalo es N/x. Si fj, con j = 1, 2,…, x, denota el número que realmente se tiene en el sub-intervalo . Entonces la estadística

Tiene aproximadamente una distribución chi cuadrado con x - 1 grados de libertad. Si Fj denota el número que resulta de los M valores de , se calcula

La hipótesis de que los números pseudo-aleatorios en la sucesión son verdaderos números aleatorios debe rechazarse si con u – 1 grados de libertad excede al valor crítico fijado por el nivel de significancia deseado.

Prueba de series

Comprueba el grado de aleatoriedad entre los números sucesivos en una sucesión. Se genera una sucesión de M conjuntos consecutivos de números pseudo-aleatorios, y calculamos la estadística chi cuadrado para cada conjunto. A continuación, para cada conjunto, fjk denota el total de números pseudo-aleatorios que satisfacen y con j, k = 1, 2,…, x. Luego calculamos la estadística

Para cada conjunto. Sin embargo, tiene una distribución chi cuadrado con x2 – x grados de libertad. Luego calculamos para cada conjunto y dejamos que sj denote el número de M valores de que se encuentran entre el (j - 1)-esimo y el j-esimo cuartil. Finalmente

La cual tiene u – 1 grados de libertad. La aleatoriedad resulta aceptable, a cierto nivel dado de significancia, si los valores y no son inconsistentes con la hipótesis de que fueron derivados al azar, a partir de distribuciones chi cuadrado, con los grados de libertad adecuados.

Prueba del producto rezagado

Mide la independencia entre los números pseudo-aleatorios. Si k es la longitud del rezago, el coeficiente del producto rezagado Ck se define como

Si no existe correlación entre y , los valores de se distribuyen normalmente con esperanza 0,25 y desvió estándar

Pruebas de corridas

*Corridas arriba y abajo*

Para una sucesión de N números pseudo-aleatorios r1, r2,…, rN definimos una sucesión binaria S de N – 1 bits, cuyo i-esimo término es igual a 0 si ri < ri+1 y es igual a 1 si ri > ri+1. Una sub-sucesión de k ceros, enmarcada por unos en cada extremo, recibe el nombre de corrida de ceros de longitud k; similarmente se definen las corridas de unos. La prueba implica determinar las ocurrencias de corridas de distinta longitud y comparar estos conteos con sus valores teóricos correspondientes esperados.

para el número total de corridas

para corridas de longitud k, con k < N – 1

para corridas de longitud N - 1

Nuevamente, la confiabilidad del ajuste se prueba con el criterio de chi cuadrado.

*Corridas encima y debajo de los promedios*

Para una sucesión de N números pseudo-aleatorios r1, r2,…, rN definimos una sucesión binaria S de N bits, cuyo i-esimo término es igual a 0 si ri < 1/2 y es igual a 1 si ri > 1/2. Deben contarse las corridas en S; el número de corridas de longitud k esperadas es , y el número total de corridas que se esperan es . Se puede emplear una prueba de chi cuadrado para comprobar si el generador resulta aceptable.

Prueba de distancia

Para cualquier digito dado d, estamos interesados en las longitudes de las distancias de los dígitos que no son d, entre 2 dígitos dados cualesquiera. Una distancia de longitud k ocurre cuando k de los dígitos que no son d se encuentran entre 2 dígitos d. Para una sucesión verdaderamente aleatoria, la probabilidad de obtener una distancia de longitud k es .

Para una sucesión dada de dígitos, se hacen correspondencias entre el número de distancias que ocurren para cada longitud. Se puede usar una prueba de chi cuadrado para analizar la confiabilidad del ajuste y compararlo con el número de distancias esperadas y reales de longitud k.

Prueba de máximos

Para un conjunto de N números aleatorios independientes y uniformes en el intervalo unitario (0, 1), podemos definir una variable aleatoria max (r1, r2,…, rN), que tenga una distribución de probabilidad definida por estadísticas de orden, tales que RN esté uniformemente distribuida en (0, 1). La prueba de los valores observados para RN es una simple prueba de frecuencias.

Prueba de Poker

Es una prueba de frecuencia especial para combinaciones de 5 o más dígitos en un número aleatorio. Cuenta con pares, 2 pares, tercias, fulles, etc. que se prueban contra la frecuencia esperada de sus ocurrencias.

# Capítulo 4: Generación de valores de las variables estocásticas empleadas en simulación (Naylor)

## Introducción

Al considerar los procesos estocásticos que involucran variables continuas o discretas, definimos la función F(x) *función de distribución acumulativa de x* como la probabilidad de que una variable aleatoria X tome un valor menor o igual a x. Si la variable es discreta, x tendrá valores específicos y F(x) será una función escalonada. Si F(x) es continua en el dominio de x, se podrá diferenciar. es la función de densidad de probabilidad.

f(t) representa el valor de la función de densidad de probabilidad de la variable aleatoria X cuando X = t.

Denotamos con r los valores de variables aleatorias uniformes cuando y .

Se tienen 3 métodos para generar los valores de variables aleatorias a partir de las distribuciones de probabilidad.

Método de la transformación inversa

Si deseamos generar los valores xi a partir de f(x), debemos obtener F(x). Puesto que F(x) se define sobre el rango de 0 a 1, podemos generar números aleatorios distribuidos uniformemente y además hacer F(x) = r. Para cualquier valor particular de r, siempre es posible encontrar el valor de x, debido a la función inversa de F, si es conocida

es la transformación inversa de r sobre el intervalo unitario en el dominio de x.

es una variable que tiene a f(x) como función de densidad de probabilidad.

Método de rechazo

Si f(x) es una función acotada y x tiene además un rango finito . Etapas:

1. Normalizar el rango de f:
2. Definir a x como una función lineal de r:
3. Generar parejas de números aleatorios (r1 r2)
4. Siempre que se encuentre una pareja de números aleatorios que satisfagan la relación , dicho par será aceptado y se utilizará a como el valor generado de la variable aleatoria.

Método de composición

Se expresa a f(x) como una mezcla probabilística de las funciones de densidad gn(x).

La guía para la selección de las está dada sobre las consideraciones relativas a la bondad del ajuste y al objetivo de minimizar , donde Tn es el tiempo esperado de computación para generar valores de variables aleatorias a partir de .

## Distribuciones continúas de probabilidad

Distribución uniforme

Constante en el intervalo (a, b) y cero fuera de él.

Para simular una distribución uniforme en el intervalo (a, b) se obtiene la función inversa de F(x)

Cada número aleatorio r determina, de manera única, un valor de la variable aleatoria x uniformemente distribuida.

Distribución exponencial

Se deben satisfacer las siguientes suposiciones:

* La probabilidad de que ocurra un evento en el intervalo es .
* es una constante que no depende de t o de algún otro factor.
* La probabilidad de que durante un intervalo ocurra más de un evento, tiende a 0 a medida que , y su orden de magnitud deberá ser menor que el de

Puesto que F(x) existe explícitamente, se puede aplicar la técnica de transformación inversa. Debido a la simetría que existe entre la distribución uniforme sigue que la intercambiabilidad de F(x) y 1 – F(x).

Para cada valor del número pseudo-aleatorio r se determina un único valor para x. Los valores de x toman tan solo magnitudes no negativas.

Distribución gamma (Erlang)

Si un determinado proceso consiste de k eventos sucesivos y si el total del tiempo transcurrido para dicho proceso se puede considerar igual a la suma de k valores independientes de la variable aleatoria con distribución exponencial, cada uno de los cuales tiene un parámetro definido α, la distribución de esta suma coincidirá con una distribución gamma con parámetros α y k.

No existe una forma explícita para describir la función acumulativa de la distribución gamma.

A medida que k se incrementa, la distribución tiende en forma asintótica a la distribución normal.

Para generar valores de variable aleatoria con distribución gamma, se debe reproducir el proceso aleatorio sobre el cual se basa la distribución. Se debe tomar la suma de los k valores de variable aleatoria con distribución exponencial x1, x2,…, xk, cuyo valor esperado es el mismo e igual a

Distribución normal

Si la variable aleatoria tiene una función de densidad

Entonces X tiene una distribución normal o gaussiana con parámetros y . Si y , la función recibe el nombre distribución normal estándar, con función de densidad

Cualquier distribución normal se puede convertir a la forma estándar

La función de distribución acumulativa no existe en forma explícita

A fin de simular una distribución normal con media y variancia , se debe proponer la siguiente interpretación del teorema central del límite. Si r1, r2,…, rN representan variables aleatorias independientes, cada una de las cuales posee la misma distribución de probabilidad caracterizada por y , entonces

Donde , y

Se sigue que z es un valor de variable aleatoria con distribución normal estándar.

Para simular valores normales, se requiere la suma de K valores de variable aleatoria distribuidos uniformemente, con .

Despejando x se tiene que

## Distribuciones discretas de probabilidad

Solamente toman valores discretos (enteros no negativos).

Donde f(x) es la frecuencia o función de probabilidad de X

Distribución geométrica

Los ensayos de Bernoulli son experimentos independientes al azar, en los que el resultado de cada ensayo queda registrado como un éxito o un fracaso. La probabilidad de éxito se denota p () y se supone que es constante. La probabilidad de fracaso se denota q = 1 – p.

Los valores de variable aleatoria que se generan al contar el número de fracasos de una sucesión de ensayos antes que ocurra el primer éxito, son valores de variable aleatoria que se ajustan a una distribución geométrica.

y como , el rango de F(x) es . Por otra parte, , lo que implica que y además

Para generar valores de variable aleatoria con distribución geométrica se emplea la técnica de transformación inversa y la fórmula . Al observar que el rango de es unitario, resulta que , y consecuentemente , donde al valor x siempre se lo redondea al entero menor.

Distribución binomial

Las variables aleatorias definidas por el número de eventos exitosos en una sucesión de n ensayos independientes de Bernoulli, para los cuales la probabilidad de éxito es p en cada ensayo, siguen una distribución binomial.

La distribución binomial proporciona la probabilidad de que un evento o acontecimiento tenga lugar x veces en un conjunto de n ensayos, donde la probabilidad de éxito está dada por p.

Los valores de variable aleatoria con distribución binomial se pueden generar con el método de rechazo. Genera n números aleatorios después de fijar x0=0. Para cada número aleatorio ri () se efectúa una prueba y la variable xi se incrementa según el siguiente criterio:

Después de haberse generado n números aleatorios, el valor de xn será igual al valor de la variable aleatoria con distribución binomial.

Distribución hipergeométrica

Considere una población de N elementos tales que cada uno de ellos pertenece a la clase I o a la II. Denotemos por Np al número de elementos que pertenecen a la clase I y por Nq al número de elementos miembros de la clase II, donde p + q = 1. Si en una población de N elementos se toma una muestra aleatoria de n elementos (n < N) sin que tenga lugar algún reemplazo, entonces el número de elementos x de la clase I en la muestra de n elementos tendrá una distribución hipergeométrica.

Con y y donde n, x y N son enteros.

Para generar valores hipergeométricos, debemos alterar el método de ensayos de Bernoulli para generar valores binomiales, con objeto que N y p varíen en forma dependiente respecto al número total de elementos que previamente se han obtenido entre la población y el número de elementos de la clase I que se han extraído. A medida que se extrae un elemento de una muestra de n elementos, se reduce el valor de N=N0: , con . De la misma forma, el valor de p=p0 se transforma según

Donde S=1 si el elemento de muestra i – 1 pertenece a la clase I y 0 de lo contrario

Distribución de Poisson

Si tomamos una serie de n ensayos independientes de Bernoulli, en cada uno de los cuales se tenga una probabilidad p muy pequeña relativa a la ocurrencia de un cierto evento, a medida que n tiende a infinito, la probabilidad de x ocurrencias está dada por la distribución de Poisson

Siempre y cuando permitamos que p se aproxime a 0 de manera que se satisfaga la relación constantemente.

Si

* El número total de eventos que ocurren durante un intervalo de tiempo dado es independiente del número de eventos que ya han ocurrido
* La probabilidad de que un evento ocurra en el intervalo de t a t + Δt es aproximadamente

Entonces

* La función de densidad del intervalo t entre las ocurrencias de eventos consecutivos es
* La probabilidad de que ocurran x eventos durante el tiempo t es

Para simular una distribución de Poisson con parámetro , el valor poissoniano x se determina haciendo uso de la desigualdad

Donde los valores ti se generan por medio de la fórmula

Otra forma es

# Capítulo 1: Modelado de Simulación Básico (Law & Kelton)

## La naturaleza de la simulación

Sistema: empresa o proceso de interés a modelizar.

Modelo: representación del sistema en términos de relaciones cuantitativas y lógicas.

Aplicaciones:

* Diseño y análisis de sistemas de fabricación.
* Evaluar requerimientos de hardware y software para un sistema informático.
* Evaluar nuevos sistemas de armas o tácticas militares.
* Determinar políticas de pedidos para un sistema de inventarios.
* Diseñar sistemas de comunicaciones y protocolos de mensajes para ellos.
* Diseñar y operar instalaciones de transporte.
* Evaluar diseños para organizaciones de servicios.
* Analizar sistemas financieros o económicos.

## Sistemas, modelos y simulación

Un sistema se define como una colección de entidades que actúan e interactúan juntos hacia el cumplimiento de un fin lógico. Definimos el estado de un sistema como una colección de variables necesarias para describir un sistema en un momento determinado, relativos a los objetivos de estudio.

Los sistemas se categorizan en dos tipos: discretos o continuos. Un sistema discreto es aquel en el que las variables de estado cambian instantáneamente en puntos separados del tiempo. En un sistema continuo en cambio las variables de estado cambian continuamente con respecto al tiempo.

Diferentes maneras en que un sistema puede ser estudiado:

* Experimentos con el sistema real vs. Experimentos con un modelo del sistema: si es posible alterar el sistema físico y luego dejar que opere bajo las nuevas condiciones, es probable que sea conveniente hacerlo, porque en este caso no hay duda acerca de si lo que estudiamos es relevante. Sin embargo, rara vez es posible hacer esto. Por esto, es necesario construir un modelo como una representación del modelo y estudiarlo como un sustituto del sistema real.
* Modelos físicos vs. Modelos matemáticos: los modelos físicos son construcciones en escala reducida o simplificada del sistema real para estudiar en ellos su comportamiento. Los modelos matemáticos representan un sistema en términos de relaciones lógicas y cuantitativas que son luego manipuladas y modificadas para ver como el sistema reacciona
* Solución analítica vs. Simulación: si las relaciones que componen el modelo son suficientemente simples, puede ser posible utilizar métodos matemáticos para obtener información exacta sobre cuestiones de interés, lo que se llama solución analítica. Muchos sistemas son demasiados complejos para ser estudiados analíticamente, y deben ser estudiados por medio de la simulación. En una simulación, usamos la computadora para evaluar un modelo numéricamente, y los datos se recogen con el fin de estimar las características del modelo.

Clasificación de los modelos de simulación:

* Estáticos vs. Dinámicos: un modelo de simulación estático es una representación de un sistema en un momento determinado, o uno que puede ser utilizado para representar un sistema en el que el tiempo simplemente no juega ningún papel. Un modelo de simulación dinámica representa un sistema a medida que evoluciona en el tiempo.
* Estocásticos vs. Determinísticos: Si un modelo de simulación no contiene componentes probabilísticas (es decir aleatorias) se conoce como determinístico, en estos modelos la salida se “determina” una vez que se especifica el conjunto de relaciones (ecuaciones) y los valores de entrada. En cambio los modelos estocásticos contienen variables aleatorias de entrada sujetas a una distribución probabilística de algún tipo.
* Continuos vs. Discretos: definimos los modelos de simulación discreta y continua de manera análoga a la forma en que los sistemas discretos y continuos se definieron anteriormente.

## Simulación de Eventos Discretos:

La simulación de eventos discretos comprende el modelado de un sistema a medida que este evoluciona a través del tiempo por medio de una representación en la cual las variables de estado cambian instantáneamente en puntos separados en el tiempo. Estos puntos en el tiempo son aquellos en los cuales un evento ocurre, donde un evento se define como una ocurrencia instantánea que puede cambiar el estado del sistema.

Mecanismo de Avance del Tiempo

Debido a la naturaleza dinámica de los modelos de simulación de eventos discretos, tenemos que realizar un seguimiento del valor actual del tiempo simulado a medida que avanza la simulación, y también necesitamos un mecanismo para avanzar el tiempo simulado de un valor a otro. Llamamos *reloj* de la simulación a la variable de un modelo de simulación que contiene el valor actual del tiempo simulado. La unidad del reloj nunca se enuncia explícitamente y se asume que está en las mismas unidades que los parámetros de entrada.

Existen dos enfoques para el mecanismo de avance del tiempo:

* **Avance del tiempo al siguiente evento**: Con este enfoque el reloj de la simulación se inicializa a cero y se determinan los tiempos de ocurrencia de eventos futuros, luego el reloj se avanza al tiempo de ocurrencia del evento futuro más próximo, en este punto el estado del sistema se actualiza para determinar que un evento ha ocurrido y los tiempos de futuros eventos también se actualizan. Este proceso continua hasta que se cumple con una condición de parada pre especificada.
* **Avance del tiempo a incrementos fijos:** La diferencia con el método anterior es que este enfoque no saltea periodos de inactividad en el sistema, lo que supone una mayor cantidad de cómputo.

Componentes y organización de un modelo de simulación de eventos discretos

* *Estado del sistema*: el conjunto de variables de estado necesarias para describir el sistema en un momento dado.
* *Reloj de simulación*: una variable que indica el valor actual del tiempo simulado.
* *Lista de eventos*: una lista que contiene la próxima vez en el que cada tipo de evento ocurrirá.
* *Contadores estadísticos*: variables usadas para almacenar información estadística sobre el rendimiento del sistema.
* *Rutina de inicialización*: un sub-programa que inicializa el modelo de simulación en el tiempo cero.
* *Rutina de tiempo*: un sub-programa que determina el siguiente evento de la lista de eventos y luego avanza el reloj de simulación al momento en que ocurre ese evento.
* *Rutina de evento*: un sub-programa que actualiza el estado del sistema cuando un tipo particular de evento ocurre (hay una rutina de evento por cada tipo de evento).
* *Rutinas de biblioteca*: un conjunto de sub-programas utilizados para generar observaciones aleatorias a partir de distribuciones de probabilidad que fueron determinadas como parte del modelo de simulación.
* *Generador de informes*: un sub-programa que calcula estimaciones de las medidas de rendimiento deseadas y elabora un informe cuando la simulación finaliza.
* *Programa principal*: un sub-programa que invoca la rutina de tiempo para determinar el siguiente evento y luego transfiere el control a la correspondiente rutina de evento para actualizar el estado del sistema apropiadamente. También controla la terminación e invoca al generador de informes cuando la simulación acaba.

## Simulación de un Sistema de Colas de un solo Servidor (M/M/1):

En un sistema de colas de un solo servidor, los tiempos entre arribos A1, A2,…, An (de cada cliente al sistema) son variables aleatorias IID (independientes e idénticamente distribuidas). Un cliente que arriba y encuentra al servidor desocupado se atiende inmediatamente, y los tiempos de servicio S1, S2,…, Sn (de cada cliente) son también variables aleatorias IID independientes de los tiempos de arribo. Si un cliente arriba y encuentra al servidor ocupado se une al final de cola. Al producirse una partida (un cliente completa el servicio) el servidor elige un cliente de la cola según la disciplina FIFO. La simulación comenzará sin clientes en el sistema y el servidor en estado desocupado. El sistema se simula hasta que un número fijo (n) de clientes hayan completados sus demoras en cola, es decir cuando el n-esimo cliente entre en servicio.

Medidas de Rendimiento: Para medir el rendimiento de este sistema observamos las estimaciones de tres parámetros (más un parámetro opcional que es *w(n)*):

* Demora promedio esperada en cola de los n clientes. Llamada *d(n).*
* Número de clientes promedio esperado en la cola. Denotado por *q(n).*
* Utilización del servidor. Denominada *u(n).*
* Demora promedio esperada en el sistema de los n clientes. Llamada *w(n)*.

Demora promedio esperada en cola de los “n-clientes”:

La demora promedio en una corrida determinada de la simulación es considerada propiamente como una variable aleatoria en sí. Lo que queremos estimar, d(n), es el valor esperado para esta variable aleatoria. d(n) es el promedio de una gran numero de demoras promedio de n clientes. A partir de una sola corrida de la simulación podemos estimar este parámetro a través de:

Esta fórmula es el promedio de las n demoras que fueron obtenidas durante la simulación.

Este estimador está basado en una muestra de tamaño 1 ya que estamos haciendo solamente una sola corrida de la simulación. Un estimador de este tipo no tendrá demasiada precisión, pues el sistema seguramente se encuentra en estado *transitorio*.

Es un ejemplo de una estadística de tiempo discreto.

Número de clientes promedio esperado en la cola:

Este promedio se toma sobre el periodo de tiempo necesarios para observar las n demoras que definen nuestra regla de parada. Esta es una clase diferente de promedio que el anterior, ya que se toma sobre el tiempo (continuo) en lugar de los clientes (discreto).

Definimos Q(t) como el número de clientes en cola en el momento t (para cualquier t ≥ 0) y T(n) como el tiempo requerido para observar n demoras en cola. Para cualquier momento t entre 0 y T(n), Q(t) es no negativo. Si llamamos pi a la proporción esperada (entre 0 y 1) del tiempo en que Q(t) es igual a i, una definición de q(n) seria:

Para estimar q(n) en una simulación, simplemente reemplazamos pi con sus respectivas estimaciones y obtenemos:

Donde es la proporción observada del tiempo en que hubo i clientes en la cola (en la simulación).

Sin embargo una manera más sencilla de obtener es mediante algunas consideraciones geométricas. Si llamamos Ti al tiempo total durante la simulación en que la cola es de tamaño i, luego:

y

Y el estimador puede escribirse como:

La sumatoria en el numerador de la ecuación anterior es solo el área bajo la curva de Q(t), que puede escribirse como una integral de 0 hasta T(n), quedando finalmente la expresión:

Es un ejemplo de una estadística de tiempo continuo.

Utilización esperada del servidor:

La utilización esperada del servidor es la proporción esperada de tiempo durante la simulación en que el servidor está ocupado y por eso es un número entre 0 y 1. El estimador es la proporción observada de tiempo durante la simulación en que el servidor está ocupado. Para esto definimos la “función ocupado” B(t).

De esta manera puede expresarse como la proporción de tiempo en que B(t) es igual a 1.

El numerador puede ser visto como el área bajo la función B(t) durante el curso de la simulación.

es el promedio continuo de la función B(t). La integral de B(t) puede fácilmente ser acumulada por la suma de las áreas de los rectángulos. Las estadísticas de uso son muy informativos en la identificación de cuellos de botella o exceso de capacidad.

Es un ejemplo de una estadística de tiempo continuo.

Demora o Tiempo de espera promedio esperado en el sistema (cola + servidor):

Esta medida se define como el intervalo de tiempo desde el instante que un cliente arriba a la cola hasta el instante en que el cliente completa el servicio y parte.

El estimador usual de w(n) seria:

Donde Si es el tiempo de espera de los n clientes en el servidor y es el promedio de los n tiempos de servicio de los clientes. Ya que el tiempo de servicio medio o esperado E(S) es conocido un estimador alternativo seria

En casi todas las simulaciones de colas será mejor que . Ambos son estimadores no sesgados.

Eventos y variables de estado: Los eventos de este sistema son el arribo de un cliente y la partida de un cliente. Las variables de estado necesarias para estimar d(n), q(n) y u(n) son el estado del servidor, el número de clientes en cola, el tiempo de arribo de cada cliente en cola y el tiempo del ultimo evento.

Observaciones:

* El elemento clave in la dinámica de una simulación es la interacción entre el reloj de la simulación y la lista de eventos.
* Mientras se procesa un evento, no transcurre el tiempo de simulación.
* A veces es fácil pasar por alto las contingencias que parecen fuera de lo común, pero que sin embargo hay que tener en cuenta.
* En algunas simulaciones puede suceder que 2 o más entradas en la lista de eventos empatan en menor, y deba incorporarse una regla de decisión para romper empates, que afectará el resultado de la simulación.

## Reglas de interrupción alternativas

La simulación puede terminar:

* Cuando el número de clientes atendidos llega a una determinada cantidad fija. El valor final del reloj de la simulación es una variable aleatoria.
* Cuando el reloj llega a una cantidad fija de tiempo. El número de clientes atendidos es una variable aleatoria.

## Determinando los eventos y variables

En el método de eventos gráficos, los eventos propuestos, cada uno representado por un nodo, están conectados por arcos dirigidos que representan cómo los eventos se pueden programar de otros eventos y de ellos mismos. Los eventos gráficos conectan el conjunto propuesto de eventos por los arcos que indican el tipo de programación de eventos que pueden ocurrir. Las flechas lisas gruesas ​​indican que un evento al final de la flecha se puede programar desde el evento en el comienzo de la flecha en una cantidad no nula de tiempo, y la flecha dentada delgada indica que el evento en su extremo está programado inicialmente.

Uno de los usos de los gráficos de eventos es simplificar la estructura de eventos de una simulación mediante la eliminación de eventos innecesarios. Hay varias reglas que permiten la simplificación, y una de ellas es que si un nodo de evento tiene arcos entrantes que son todos delgados y lisos, este evento puede ser eliminado del modelo y su acción integrada en los eventos que se programan en tiempo cero.

Otra regla tiene que ver con la inicialización. El gráfico de eventos se descompone en componentes fuertemente conectados, dentro de cada uno de los cuales es posible viajar desde cada nodo a todos los demás nodos siguiendo los arcos en sus direcciones indicadas. La regla de inicialización establece que en cualquier componente fuertemente conectado de nodos que no tenga arcos entrantes de otros nodos de eventos fuera del componente, debe haber al menos un nodo que se programa inicialmente.

## Simulación distribuida

En los últimos años la tecnología informática ha permitido que las computadoras o procesadores individuales se asocien entre sí en entornos de computación paralela o distribuida. En estos tipos de entornos, puede ser posible distribuir diferentes partes de una tarea computacional a través de procesadores individuales que operan al mismo tiempo y por lo tanto reducir el tiempo total para completar la tarea.

Hay muchas formas posibles de dividir una simulación dinámica para distribuir su trabajo sobre diferentes procesadores:

* *Asignar las distintas funciones de apoyo a diferentes procesadores*. La lógica de ejecución de la simulación sigue siendo secuencial, pero el programa principal de la simulación puede delegar la ejecución de las funciones de soporte a otros procesadores y seguir adelante con su trabajo.
* *Descomponer el modelo en distintos sub-modelos*, que luego son asignados a diferentes procesadores para la ejecución. Los procesadores deben comunicarse entre sí siempre que sea necesario para mantener las relaciones lógicas correctas entre los sub-modelos.

## Pasos en un estudio de simulación

1. *Formular el problema y planificar el estudio*: todo estudio debe comenzar con una declaración clara de los objetivos generales del estudio y las cuestiones específicas que se abordarán.
2. *Recolectar datos y definir un modelo*: información y datos deben recolectarse del sistema de interés y utilizarse para especificar los procedimientos operativos y distribuciones de probabilidad de las variables aleatorias utilizadas en el modelo.
3. *Validar*: en la construcción del modelo, es imperativo para los modeladores involucrar en el estudio a las personas que están íntimamente familiarizadas con las operaciones del sistema real.
4. *Construir un programa de computación y verificar*: el modelador de la simulación debe decidir si se debe programar el modelo en un lenguaje de propósito general o en un lenguaje de simulación de diseño especial.
5. *Hacer corridas piloto*: se hacen pruebas piloto del modelo verificado.
6. *Validar*: las pruebas piloto pueden usarse para probar la sensibilidad de las salidas del modelo a pequeños cambios en un parámetro de entrada.
7. *Diseñar experimentos*: hay que decidir qué diseño de sistema simular si hay más de una alternativa que pueda razonablemente simularse.
8. *Hacer corridas de producción*: se hacen corridas de producción para proporcionar datos de rendimiento sobre los diseños de los sistemas de interés.
9. *Analizar los datos de salida*: se usan técnicas estadísticas para analizar los datos de salida de las corridas.
10. *Documentar presentar e implementar los resultados*: es importante documentar los supuestos que entraron en el modelo, así como el propio programa informático.

## Otros tipos de simulación

* *Simulación continua*: se refiere a la modelización a lo largo del tiempo de un sistema por una representación en la que las variables de estado cambian continuamente con respecto al tiempo. Involucra ecuaciones diferenciales que dan las relaciones de las tasas de variación de las variables de estado con el tiempo.
* *Simulación combinada discreta-continua*: puesto que algunos sistemas no son ni completamente discretos ni completamente continuo, puede surgir la necesidad de construir un modelo con aspectos tanto de simulación de eventos discretos y continuos.
* *Simulación de Monte Carlo*: es un esquema de empleo de números aleatorios que se utiliza para solucionar determinados problemas estocásticos o deterministas en donde el paso del tiempo no juega ningún papel sustantivo.

## Ventajas, desventajas y dificultades de la simulación

Ventajas:

* Muchos sistemas complejos no pueden describirse con precisión mediante un modelo matemático que puede evaluarse analíticamente. Por lo tanto, una simulación es a menudo el único tipo de investigación posible.
* Permite estimar el rendimiento de un sistema existente bajo un conjunto de condiciones de operación proyectados.
* Diseños alternativos del sistema propuesto se pueden comparar a través de la simulación para poder ver los que mejor se adaptan a los requerimientos especificados.
* En una simulación podemos mantener mejor control sobre las condiciones experimentales de lo que generalmente sería posible cuando experimentamos con el propio sistema.
* Permite estudiar un sistema con un horizonte temporal largo en tiempo comprimido, o bien estudiar los pormenores del funcionamiento de un sistema en tiempo expandido.

Desventajas:

* Cada corrida de un modelo de simulación estocástico produce solo estimaciones de las verdaderas características del modelo para un conjunto particular de parámetros de entrada.
* Los modelos de simulación suelen ser costosos y requieren mucho tiempo para desarrollarlos.
* El gran volumen de números producidos por un estudio de simulación o el impacto persuasivo de una animación realista crea a menudo una tendencia a poner mayor confianza en los resultados de un estudio que la que se justifica.

**Capítulo 9: Modelo Analítico para una cola M/M/1 (Mc Millan - Gonzalez).**

## Tipos de sistemas de colas:

Un sistema de colas se distingue de otro por cierto número de atributos. Los principales son:

1. El número de fases:
   1. Fase simple: no hay colas secuenciales.
   2. Multifásico: varias colas secuenciales.
2. El número de canales:
   1. Canal simple: no hay servidores paralelos.
   2. Canal múltiple: varios servidores paralelos
3. La disciplina de las colas.

La disciplina de las colas se refiere al hecho de si los clientes se acomodan de acuerdo con una norma de servicio por orden de llegada (FIFO, LIFO, etc.) o se aplica alguna otra regla de prioridad especial.

Por conducta de un sistema de colas se entiende el modo en que los clientes que llegan interactúan con sus instalaciones de servicio.

Entendemos por clientes a entidades cuyas llegadas ejercen demandas sobre alguna instalación (servidor).

Interacciones de colas

El fenómeno de las colas es el resultado de la interacción de las llegadas aleatorias y el tiempo aleatorio de servicio. El patrón de llegadas depende de:

1. El tamaño del universo de clientes posibles (que “genera” clientes que necesitan atención).
2. El nivel de sus actividades, que hace que necesiten servicios de vez en cuando.

## Caso M/M/1:

Sistema monofásico de canal simple. En este caso se supone que el tiempo entre llegadas tiene una distribución exponencialmente negativa y que el tiempo de servicio tiene el mismo tipo de distribución. Puesto que la misma es un producto del proceso de Poisson, nuestro sistema de colas será totalmente de Poisson.

La instalación de servicio podrá acomodar sólo a un cliente a la vez y que las llegadas se atienden de acuerdo al orden de llegada. Nos interesa desarrollar un modelo para predecir (analíticamente):

1. La probabilidad de varios números de clientes en la cola. (También llamado *número de clientes promedio esperado en la cola q(n)* en Law-Kelton).
2. El tiempo esperado o promedio que pasara un cliente en las instalaciones de servicio.
3. La probabilidad de que las instalaciones de servicio estén ociosas. (También llamado *factor de utilización del servidor [1-u(n)]* en Law-Kelton).

Para empezar suponemos que nuestro sistema puede dar atender (dar servicio) a μ clientes por unidad de tiempo (en promedio). De esta manera μ también es el número esperado de salidas (partidas) del sistema durante cada unidad de tiempo. Llamamos al promedio de llegadas por unidad de tiempo λ.

A continuación consideramos que *t* es un momento en el tiempo y que es la probabilidad de que haya n clientes en el sistema en el momento *t*. Si a su vez consideramos una porción de tiempo después de t denominada podríamos pensar que Δt es tan pequeño que aun cuando exista una llegada o una partida durante el intervalo Δt, es imposible más de una llegada o salida durante ese intervalo (modelo de Poisson). Para enfrentarnos a este problema nos preguntamos cual es la probabilidad de que haya n clientes en el sistema en el intervalo , o sea . Ahora bien, n clientes en el sistema durante ese intervalo puede presentarse de cuatro modos distintos:

Modo 1:

Tener n clientes en el sistema en el tiempo *t*, cero llegadas y cero salidas durante el intervalo Δt. Esto se puede obtener a partir del siguiente razonamiento:

La probabilidad de 1 llegada es:

La probabilidad de 0 llegada es:

La probabilidad de 1 partida es:

La probabilidad de 0 partida es:

Entonces la probabilidad del modo uno es:

Modo 2:

Tener n - 1 clientes en el sistema en el tiempo *t*, una llegada y cero salidas durante el intervalo Δt.

Probabilidad del modo dos:

Modo 3:

Tener n + 1 clientes en el sistema en el tiempo *t*, cero llegadas y una salida durante el intervalo Δt.

Probabilidad del modo tres:

Modo 4:

Tener n clientes en el sistema en el tiempo *t*, una llegada y una salida durante el intervalo Δt.

Probabilidad del modo cuatro:

La probabilidad total de tener n clientes en el sistema en el momento t + Δt es la suma de las probabilidades de los cuatro modos anteriores, quedando la expresión como:

Luego de trabajar esta expresión se llega a

Si hacemos que en el límite de la expresión anterior Δt tienda a 0, la misma se transforma en una ecuación diferencial:

La expresión anterior hace referencia a un sistema de infinitas ecuaciones diferenciales con n+1 ecuaciones y n + 1 incógnitas, llamado *cadena de Markov*, en la cual la probabilidad de que un evento pueda ocurrir depende del evento anterior. El caso anterior se aplica a n ≥ 1 si hacemos el caso especial en que n = 0, entonces , y la expresión se transforma en:

Dado a que cuando n = 0 el sistema está vacío y no se producen salidas, el segundo término se desecha y finalmente:

Dado que la derivada es una función del tiempo, las probabilidades de que haya distintos números de clientes en el sistema cambian con el tiempo.

Mientras el sistema se está asentando para llegar a una condición estable decimos que se encuentra en *estado transitorio*, una vez alcanzado su condición estable se encuentra en *estado estacionario*.

Si nos interesamos exclusivamente por el estado estacionario, la derivada de la probabilidad de que haya varios números de clientes en el sistema sea cero, o sea , se convierte en

A partir de estas ecuaciones resulta evidente que:

Para n = 1 tenemos:

Para n = 2 siguiendo los mismos pasos obtenemos:

Por ende para el n-esimo término la *probabilidad de que haya n elementos en el sistema* resulta:

Ahora bien si queremos determinar tenemos que:

Por ende:

El denominador de la expresión anterior es una serie geométrica donde a = 1 y r = λ/μ, y para todos los valores de r < 1 la serie converge y su suma es

Finalmente:

Por lo tanto la expresión final de pn seria:

Este es un modelo general para determinar la probabilidad de que haya n clientes en el sistema de colas de canal simple, en el estado estacionario, donde el ritmo de llegadas (λ) es menor que el índice medio de servicio (μ). Sin embargo nuestro modelo está limitado al hecho de que λ/μ < 1(esto es ![](data:image/png;base64...)una condición para que exista la solución estacionaria). Desde el punto de vista lógico resulta obvia esa condición ya que si λ/μ ≥ 1entonces el índice de llegadas siempre será más alto que la capacidad del servidor de atender esas llegadas, con lo cual la cantidad de gente en cola se haría cada vez más grande a medida que pasa el tiempo y la probabilidad de que haya n elementos en el sistema tendería hacia el infinito a medida que n aumenta.

Fig. 1. El estado más probable es que haya 0 clientes en cola si λ/μ < 1.

## Medidas de rendimiento:

A partir del análisis se pueden obtener las siguientes medidas de rendimiento:

Porcentaje de tiempo y ocioso y porcentaje de utilización

El porcentaje de tiempo ocioso es la probabilidad de 0 clientes en el sistema

La utilización fraccionaria de la capacidad total de la instalación de servicio es

Número de elementos esperado en el sistema

Esto es la probabilidad de 1 en el sistema por 1, más la probabilidad de 2 por 2, más la de 3 por 3, y así sucesivamente. Esto resulta una serie infinita de la forma , donde y . La suma de la serie es , por lo tanto

Número de elementos esperado en la cola

El número esperado en la cola es el número esperado en el sistema menos el número esperado en la instalación de servicio.

El número esperado en el punto de servicio es igual al número en el punto de servicio cuando esté ocupado por la probabilidad de que esté ocupado más el número en la instalación de servicio cuando esté ociosa por la probabilidad de que este ociosa. Esto es .

Por lo tanto, el número esperado en cola es

Tiempo esperado en el sistema

El número esperado en el sistema es , por el tiempo esperado en el sistema. Entonces el tiempo esperado en el sistema es el número esperado en el sistema dividido entre

Tiempo promedio de espera

Es el tiempo total esperado en el sistema menos el tiempo esperado en el punto de servicio

Probabilidad de N en la cola

La probabilidad de n en cola es simplemente la probabilidad de n + 1 en el sistema (esto solo aplica cuando n > 0, la probabilidad de 0 en la cola es la de 0 en el sistema más la de 1 en el sistema).

Con un fijo y variando de 0 a , vemos que hay una probabilidad variable de encontrar 1, 2, 3,… en el sistema. Se llega a un punto máximo a medida que aumenta y luego comienza a disminuir.

El tiempo que se puede esperar que el sistema permanezca ocioso es una línea recta, de 1 para y que llega a ser muy pequeña cuando se acerca a .

En cualquier punto, .

Si los clientes llegan a un ritmo cercano al índice que se les puede atender, el tiempo en el sistema será muy grande. Si es pequeño en comparación con , un aumento de la capacidad de servicio dará una ligera disminución del tiempo en el sistema.

Modos de mejorar el servicio:

* Aumento del número de canales.
* Reunión de instalaciones.

Probabilidad de N en función del tiempo

El estado estacionario es una condición que se supone que prevalece después de que el sistema ha tenido tiempo de asentarse y acercarse a su estado esperado. Excepto en el estado estacionario, Pn es una función del tiempo, lo mismo que y .

Probabilidad de una llegada en función de la longitud de la cola

En el modelo, se supone que la población de clientes potenciales es infinita. Cuando la población de clientes potenciales sea pequeña, la probabilidad de una llegada en el siguiente período es función de la longitud de la cola, además de serlo de y .

El estado transitorio y la truncación

En teoría, cuando el sistema tendría solamente un estado transitorio. En la práctica, conforme la línea de espera y el tiempo necesario crecen, los clientes se impacientan y no esperan; o bien no se deja que la cola crezca más allá de un cierto límite. De este modo, estos sistemas se ven truncados en alguna longitud de cola y se descubre que, incluso para , los sistemas de cola pueden tener un estado estacionario.

# Capítulo 15: Verificación de los resultados de simulación (Gordon)

## Naturaleza del problema

Por lo general se planea un estudio de simulación como una serie de corridas cuyo objetivo es comparar una diversidad de sistemas alternos o condiciones de operación.

Experimento: prueba de un sistema determinado que opere bajo un conjunto de condiciones.

Corrida: una sola ejecución de una configuración experimental.

Observación: una sola medición de una variable del sistema.

Un experimento es la colección de todas las corridas con una configuración de sistemas y el estudio es la configuración de todos los experimentos.

Problemas estadísticos asociados con un estudio de simulación:

* Problemas de planificación estratégica: referido al diseño de un conjunto de experimentos. La planificación estratégica debe determinar las medidas según las cuales se juzga el sistema y cómo probar la significancia en las diferencias en estas medidas.
* Problemas de planificación táctica: referido a especificar la manera en que debe de realizarse cada experimento. La planificación táctica debe decidir cómo tomar las medidas de cada corrida y cuántas corridas deben hacerse para cada experimento.

## Métodos de estimación

Si se hacen n observaciones independientes de la variable, la media de la muestra también es una variable aleatoria. Según el teorema central del límite, x tiende a una distribución normal con media y variancia . Se sigue que

Tiene distribución aproximadamente normal con media 0 y variancia 1. La integral de a un valor u es la probabilidad de que z sea menor o igual a u. Suponga que se elige un valor u tal que (). Entonces , por simetría de la distribución normal respecto de la media. Por lo tanto

es el nivel de confianza y el intervalo es el intervalo de confianza.

En la práctica no se conoce , en cuyo caso se reemplaza por una estimada

La variable z ya no está distribuida en forma normal, sino que tiene una distribución t de Student. La cantidad debe deducirse integrando la distribución. La desviación entre estas distribuciones disminuye al aumentar n, y para un n suficientemente grande () se puede utilizar la distribución normal. El intervalo de confianza para es .

## Estadísticas de corridas de simulación

El método de determinar un intervalo de confianza supone que:

* La distribución de la cual se obtienen las observaciones es estacionaria.
* Las observaciones son independientes.

La media de la muestra depende de la cantidad de observaciones que se toman.

Los tiempos de espera no son independientes, ya que el tiempo de espera de cada entidad depende de los tiempos de espera de sus predecesores. Se dice que esta auto-correlacionada. La auto-correlación aumenta conforme aumenta la utilización del servidor. La media de la muestra de datos auto-correlacionados se aproxima a una distribución normal conforme aumenta el tamaño de la muestra. La fórmula para estimar el valor medio de la distribución es válida, pero la variancia de los datos auto-correlacionados no está relacionada con la de la población por . Es necesario agregar un término para tomar en cuenta la correlación.

Al iniciar una corrida de simulación con el sistema en algún estado inicial (con frecuencia el de ocio), las primeras llegadas tienen una probabilidad mayor de obtener rápidamente el servicio, de manera que estará sesgada una media de muestra que incluya las primeras llegadas. El efecto de sesgo disminuye al extender la longitud de la corrida de simulación y aumentar el tamaño de la muestra.

## Repetición de corridas

Al repetir el experimento con distintos números aleatorios para el mismo tamaño n de la muestra se obtiene un conjunto de determinaciones independientes de la media de la muestra, que pueden utilizarse para estimar la variancia de la distribución. Suponga que el experimento se repite p veces con series de números aleatorios independientes. Sea xij la i-esima observación de la j-esima corrida, y sea la media de la muestra para la j-esima corrida, entonces

Se pueden utilizar las estimaciones para establecer un intervalo de confianza. La media en que se basa el intervalo de confianza depende de . En ausencia de sesgo inicial, el mismo aumento en n o p tiene efectos equivalentes en el tamaño del intervalo de confianza. Para aumentar la probabilidad de reducir el sesgo inicial, es preferible extender las corridas manteniendo el número de repeticiones a un nivel en que el tamaño de la muestra es suficientemente grande para justificar la aproximación a la distribución normal.

## Eliminación del sesgo inicial

Se pueden seguir 2 enfoques:

* *Iniciar cada sistema en una condición inicial más representativa*: en algunos sistemas, se puede disponer de información sobre las condiciones esperadas, lo que permite elegir mejores condiciones iniciales. Debe utilizarse un rango de valores que permita escoger un estado inicial distinto para cada repetición.
* *Ignorar la primera parte de cada corrida de simulación*: es el enfoque más común. La corrida se inicia a partir de un estado de ocio y se detiene después de un determinado período. Se dejan como están las entidades que existen en el sistema en ese momento y se reinicia la corrida recabando estadísticas desde el punto de reinicio. No hay reglas simples para decidir el largo del intervalo eliminado. Se aconseja usar pruebas piloto.

## Medias de lotes

Otro enfoque para estimar la precisión de los resultados utiliza una sola corrida larga, preferentemente quitando el sesgo inicial. La corrida se divide en segmentos para separar las mediciones en lotes de igual tamaño. Se toma la media de cada lote y se las considera como observaciones independientes. El valor estimado de la variable que se está midiendo es la media de las medias de los lotes, que es igual a la media de todas las mediciones. Al suponer que las medias de los lotes son independientes, se considera a las observaciones de las medias de los lotes como distribuidos normalmente (por teorema central del límite) y se pueden aplicar las fórmulas para estimar la variancia de la media y calcular un intervalo de confianza.

No se puede aplicar el método a una estadística acumulada, debido a que la distribución de la media de la muestra depende de la longitud de la corrida.

Una corrida completa consiste en N observaciones que se descomponen en p lotes de tamaño n. Esto equivale a repetir un experimento de longitud n un total de p veces, en que el estado final de una corrida es el inicial de la siguiente. Este es un estado inicial más razonable que el de ocio, pero introduce correlación. Se puede separar los lotes en intervalos en que se descartan las mediciones para eliminar la correlación.

## Análisis de series de tiempo

Un enfoque para estimar la precisión de los resultados es estimar la variancia de una media de muestra, a partir de resultados obtenidos en el estudio de series de tiempo. El experimento se realiza como una sola corrida quitando el sesgo inicial. Se conservan las observaciones individuales y se tratan como los datos de una serie de tiempo. Suponga que los cálculos se realizan a intervalos unitarios y el registro es para una longitud T de tiempo.

La auto-correlación se mide con una serie de coeficientes de auto-covariancia que muestran el grado en que se afectan entre sí los valores separados por un intervalo de unidades. Los coeficientes se definen mediante

En que es la observación al tiempo t y

El caso especial de , R(0), es una estimación de la variancia de la distribución de la que se toma . La estimación de la variancia de la media de la muestra es

estima la variancia de la media de la muestra que se esperaría si las observaciones fueran independientes. El término adicional representa la contribución de la auto-correlación. Los valores de los coeficientes disminuyen al aumentar . El valor de M debe ser suficientemente grande para incluir los coeficientes significativos.

## Análisis espectral

Se puede considerar a una serie de tiempo como la suma de las oscilaciones de distintas frecuencias. Se puede relacionar el espectro de las frecuencias y las amplitudes de las oscilaciones con la auto-correlación.

Un análisis espectral puede dar más información que la contenida en la estimación de un valor medio. Dos sistemas pueden no mostrar diferencia significativa en sus valores medios, aunque su comportamiento transitorio puede ser significativamente distinto.

# Capítulo 9: Análisis de Datos de Salida (Law & Kelton)

En muchos estudios de simulación una gran cantidad de tiempo y dinero se gasta en el desarrollo y programación del modelo, pero se hace poco esfuerzo para analizar los datos de salida de la simulación apropiadamente. Un modo muy común de operación consiste en hacer una sola corrida de simulación de longitud algo arbitraria y luego tratar las estimaciones de los resultados de la simulación como las verdaderas características del modelo. Estas estimaciones son sólo realizaciones particulares de variables aleatorias que pueden tener grandes variaciones. Como resultado, estas estimaciones podrían diferir en gran medida de las verdaderas características correspondientes para el modelo, llevando a hacer inferencias erróneas sobre el sistema.

Existen varias razones por las cuales el análisis de datos de salida de una simulación no pueden ser tratados en forma apropiada. Primero debe considerarse que una simulación es un experimento de muestreo estadístico basado en computadoras, por lo tanto deben usarse las técnicas estadísticas apropiadas para diseñar y analizar los experimentos de simulación. Una segunda razón para análisis estadísticos inadecuados es que los procesos de salida de virtualmente todas las simulaciones son no estacionarios y auto correlacionados. Por este motivo las técnicas estadísticas clásicas basadas en observaciones IID no son aplicables directamente. Otro obstáculo para obtener estimaciones precisas de los verdaderos parámetros o características de un modelo es el costo del tiempo de computadora necesario para reunir la cantidad necesaria de datos de salida de la simulación.

Llamamos Y1, Y2,… a un proceso estocástico de salida a partir de una sola corrida de simulación. Los Yi son variables aleatorias que en general no son IID.

Llamamos yij a una observación de la variable Yj en la i-esima corrida o replica. Si corremos la simulación con un conjunto de números aleatorios diferentes obtendremos distintos valores de yij

Suponga que hacemos n corridas de la simulación independientes (con distintos números aleatorios en cada corrida) de tamaño m, resultando en las observaciones:

y11, y12,…, y1m

y21, y22,…, y2m

yn1, yn2,…, ynm

Las observaciones de una fila son no IID, además representan los valores de las distintas variables Yj en la corrida “i”. Las observaciones de una columna en cambio sí son IID, y representan los distintos valores que asume una única variable Yj a través de las m corridas “i”. Esta independencia a través de las corridas es la clave para los relativamente simples métodos de análisis de datos de salida, el objetivo de este análisis es usar las observaciones yji (i= 1,2,…, m; j=1,2,…n) para trazar inferencias acerca de las distribuciones de las variables aleatorias Yj.

## Comportamiento transitorio y en estado estacionario de un proceso estocástico

Considere las salidas de los procesos estocásticos Y1, Y2,… Sea para i = 1, 2,…, donde y es un número real e I representa las condiciones iniciales usadas para iniciar la simulación en el tiempo 0. Llamamos a la distribución transitoria del proceso de salida en el tiempo i para las condiciones iniciales I. será diferente para cada valor de i y cada conjunto de condiciones iniciales I.

Para I e y fijos, las probabilidades son solo una secuencia de números. Si cuando para toda y y para cualesquiera condiciones iniciales I, entonces se llama la distribución en estado estacionario del proceso de salida Y1, Y2,… El estado estacionario significa que todos ellos tendrán aproximadamente la misma distribución. Estas variables aleatorias no serán independientes, sino que constituyen aproximadamente un proceso estocástico de covarianza estacionaria.

La distribución en estado estacionario F(y) no depende de las condiciones iniciales I.

## Tipos de simulaciones con respecto al análisis de la salida

Una *simulación terminal* es aquella para la cual hay un evento natural E que especifica la longitud de cada corrida. Dado que las diferentes corridas usan números aleatorios independientes y la misma norma de inicialización, esto implica que las variables aleatorias comparables en las diferentes corridas son IID. El evento E a menudo ocurre en un instante a partir del cual no se obtiene información útil o en un instante cuando el sistema se limpia. Se especifica antes de realizar cualquier corrida, y el tiempo de ocurrencia de E para una ejecución en particular puede ser una variable aleatoria. Dado que las condiciones iniciales para una simulación terminal afectan generalmente a las medidas deseadas de rendimiento, estas condiciones deben ser representativas de aquellas para el sistema real.

Una *simulación no terminal* es aquella en la cual no hay un evento natural E que especifique la longitud de la corrida. Una medida de rendimiento para una simulación tal se dice que es un *parámetro de estado estacionario* si se trata de una característica de la distribución en estado estacionario de algún proceso estocástico de salida Y1, Y2,…

Los procesos estocásticos para la mayoría de los sistemas reales no tienen distribuciones en estado estacionario, ya que las características del sistema cambian con el tiempo. Por otra parte, un modelo de simulación puede tener distribuciones en estado estacionario, ya que las características del modelo a menudo se suponen que no cambian con el tiempo.

Una simulación para un sistema particular puede ser terminal o no terminal, dependiendo de los objetivos del estudio de simulación.

Considere un proceso estocástico Y1, Y2,… para una simulación no terminal que no tiene una distribución en estado estacionario. Suponga que se divide el eje del tiempo en intervalos de tiempo de igual longitud y contiguos llamados ciclos. Sea una variable aleatoria definida en el i-esimo ciclo, y asuma que son comparables. Suponga que tiene una distribución en estado estacionario y que . Entonces una medida de rendimiento se dice que es un *parámetro de ciclo en estado estacionario* si se trata de una característica de como la media . Así, un parámetro de ciclo en estado estacionario es solo un parámetro en estado estacionario del proceso del ciclo correspondiente .

Para una simulación no terminal, supongamos que el proceso estocástico Y1, Y2,… no tiene una distribución en estado estacionario, y que no existe una definición de ciclo apropiada de tal manera que el proceso correspondiente tenga una distribución en estado estacionario. En estos casos, normalmente habrá una cantidad fija de datos que describen cómo los parámetros de entrada cambian con el tiempo. Esto proporciona, en efecto, un evento E de terminación para la simulación y, por lo tanto, las técnicas de análisis para la terminación de simulaciones son apropiado. Las medidas de ejecución de los parámetros de tales simulaciones suelen cambiar con el tiempo y se incluyen en la categoría de otros parámetros.

## Análisis Estadístico para Simulaciones Terminales

Supongamos que hacemos n repeticiones independientes de una simulación terminal, donde cada repetición se termina por el evento E y se comienza con las mismas condiciones iniciales. La independencia de las repeticiones se logra mediante el uso de diferentes números aleatorios para cada réplica. Supongamos por simplicidad que hay una sola medida de rendimiento de interés. Sea Xj una variable aleatoria definida en la réplica j-ésima para j = 1, 2,..., n, y se supone que las Xj son variables aleatorias IID.

Estimación de Medias

Suponga que nos interesaría obtener una estimación puntual y el intervalo de confianza para la media donde X es una variable aleatoria definida sobre una corrida. Si se hacen n corridas independientes de la simulación y siendo X1, X2,..., Xn las variables aleatorias IID resultantes obtenemos que es un estimador puntual no sesgado para μ y un intervalo de confianza aprox. del 100(1 - α)% con (0 < α < 1) para μ está dado por:

Dicho intervalo de confianza se denomina *procedimiento de muestra de tamaño fijo*. La exactitud de este intervalo depende de la suposición de que los Xj son variables aleatorias normales.

La cobertura realmente obtenida a partir del intervalo de confianza depende del modelo de simulación sobre la muestra de tamaño n.

Obtención de una precisión especificada: Una desventaja del procedimiento anterior es que en analista no tiene control sobre la mitad del tamaño del intervalo de confianza (es decir la precisión de ), por este motivo existen dos métodos que estiman el número de corridas requeridas para estimar la media con una precisión o error especificado.

Estos métodos son: el número de corridas para establecer un error absoluto β y el número de corridas para establecer un error relativo γ.

Comenzamos definiendo el primero, si la estimación es tal que , entonces decimos que tiene un error absoluto de β. Si hacemos corridas de una simulación hasta que la mitad del tamaño del intervalo de confianza de 100(1 - α)% es menor o igual que β, entonces:

( = mitad de tamaño del intervalo de confianza.)

tiene un error absoluto de a lo sumo β con una probabilidad de aprox. 1 – α. Si hemos construido un intervalo de confianza para μ basado en un número fijo de corridas n y si asumimos que nuestra estimación S2(n) de la varianza poblacional no cambiara a medida que el número de corridas se incrementa, entonces obtenemos la siguiente expresión:

La fórmula obtenida indica el número total de corridas que se necesitan para obtener un error absoluto de β. Los dos puntos se leen como “tal que”. Dicha fórmula se itera incrementando el valor de hasta obtener un valor de i para el cual el lado a continuación de los 2 puntos de la expresión sea válido. La precisión de la formula depende de cuan cercana es S2(n) de la Var(x).

Definimos ahora la segunda fórmula, si el valor de estimado es tal que , entonces decimos que tiene un error relativo de γ. Si hacemos corridas de una simulación hasta que la mitad del tamaño del intervalo de confianza de 100(1 - α)% divido por es menor o igual que γ, entonces:

Así, tiene un error relativo de a lo sumo con una probabilidad de aprox. 1 - α. Si hemos construido un intervalo de confianza para μ basado en un número fijo de corridas n y si asumimos que nuestras estimaciones de la media y varianza poblacional no cambiaran a medida que el número de corridas se incrementa, entonces obtenemos la siguiente expresión:

Esta fórmula indica el número total de corridas necesarias para obtener un error relativo de γ. Donde es el error relativo ajustado necesario para obtener un error relativo real de γ. Como en la formula anterior los dos puntos indica que esta fórmula se itera para valores de hasta obtener un valor de i para el cual el lado a continuación de los 2 puntos de la expresión sea válido.

La dificultad con el uso de la ecuación directamente para obtener una estimación con un error relativo de es que y no pueden ser estimaciones precisas de sus correspondientes parámetros de la población. Presentamos un procedimiento secuencial para obtener una estimación de μ con un error relativo especificado que sólo toma tantas repeticiones como sean realmente necesarias. El procedimiento supone que X1, X2,… es una secuencia de variables aleatorias IID que necesitan no ser normal.

El objetivo específico del procedimiento es obtener una estimación de μ con un error relativo de y un nivel de confianza de 100(1 - α) porciento. Elija un número inicial de réplicas y

es el intervalo de confianza de longitud media habitual. Procedimiento:

1. Hacer n0 réplicas de la simulación y fijar .
2. Calcular y δ(n,α) de X1, X2,…, Xn.
3. Si , usar como el punto estimado para μ y parar.

Equivalentemente, es aproximadamente un intervalo de confianza del 100(1 - α) por ciento de μ con la precisión deseada. De lo contrario, reemplazar n por n + 1, hacer una réplica adicional de la simulación, e ir al paso 1.

Uso recomendado de los procedimientos: Si se está realizando un experimento exploratorio donde la precisión del intervalo de confianza no puede ser abrumadoramente importante, se recomienda utilizar el procedimiento de la muestra de tamaño fijo.

A partir de un experimento exploratorio que consiste en n repeticiones, se puede estimar el coste por réplica y la varianza de la población de las Xj y, a continuación, obtener una estimación aproximada del número de réplicas, , necesaria para estimar μ con un error absoluto deseado . Alternativamente, se puede obtener una estimación aproximada del número de réplicas, , requerida para estimar μ con un error relativo deseado . A veces, la elección de o puede tener que ser atenuada por el costo asociado con el número requerido de réplicas.

Estimando otras medidas de rendimiento

Sea X una variable aleatoria definida en una réplica. Supongamos que queremos calcular la probabilidad , donde B es un conjunto de números reales. Hacemos n réplicas independientes y sea X1, X2,…,Xn las variables aleatorias IID resultantes. Sea S el número de Xj que caen en el conjunto B. Luego S tiene una distribución binomial con parámetros n y p, y un estimador puntual insesgado de p es .

Supongamos que queremos estimar el q-cuartil xq de la distribución de la variable aleatoria X. Si X(1), X(2),…, X(n) son las estadísticas de orden correspondientes a las Xj de n replicas independientes, entonces un estimador puntual para xq es la muestra q-cuartil

Eligiendo condiciones iniciales

Supongamos que queremos estimar la demora promedio esperada de todos los clientes que llegan y terminan sus demoras entre las 12 y la 1 pm (el período más activo) en un banco.

Supongamos que el banco abre a las 9 am, sin clientes presentes. Entonces podemos empezar la simulación a las 9 am, sin clientes presentes y ejecutarlo durante 4 horas simuladas. En la estimación de la demora media esperada deseada, utilizamos sólo las demoras de los clientes que llegan y completan sus demoras entre el mediodía y la 1 pm. Una desventaja de este enfoque es que 3 horas de tiempo simulado no se utilizan directamente en la estimación.

Un enfoque alternativo es recolectar datos sobre el número de clientes presentes en el banco al mediodía en diferentes días. Sea la proporción de estos días en que i clientes (i = 0, 1,…) están presentes al mediodía. A continuación se simula el banco del mediodía a 1 pm, con el número de clientes presentes al mediodía siendo elegido aleatoriamente de la distribución .

## Múltiples medidas de rendimiento

Para la mayoría de las simulaciones del mundo real una serie de medidas de rendimiento son de interés al mismo tiempo. Supongamos que Is es un intervalo de confianza del 100(1 - α)% para la medida de rendimiento μs (donde s = 1, 2,…, k). Entonces la probabilidad de que todos los k intervalos de confianza contengan simultáneamente sus respectivas medidas verdaderas satisface ya sea o no que los Is son independientes.

Cuando el valor de k es pequeño, si se desea que el nivel de confianza global asociado con k intervalos de confianza sea al menos de 100(1 - α)%, elegir los de modo que

## Resumen: Construcción de Intervalos de Confianza

**Si la población es Normal:**

Procedimiento de muestra de tamaño fijo: Sirve para estimar un intervalo de confianza de la media poblacional

**Si la población no es Normal:**

Número de corridas para un error absoluto β: Sirve para estimar el número de corridas na suponiendo que la varianza estimada no cambiara a medida que el número de corridas se incrementa.

Número de corridas para un error relativo γ: Sirve para estimar el número de corridas nr suponiendo que la media y varianza estimadas no cambiaran a medida que el número de corridas se incrementa.

# Capítulo 10: Comparando las configuraciones del sistema alternativas (Law & Kelton)

## Introducción

La dificultad de muchos estudios de simulación es que los datos de salida de la simulación son estocásticos, por lo que la comparación de dos sistemas sobre la base de sólo una única corrida de cada uno es un enfoque muy poco fiable.

Un requerimiento básico para usar muchos métodos estadísticos para comparar configuraciones alternativas es la capacidad de recoger observaciones IID con expectativa igual a la medida de rendimiento deseada. Si queremos comparar sistemas alternativos sobre la base del comportamiento en estado estacionario, la situación se vuelve más complicada ya que no podemos obtener fácilmente observaciones IID teniendo expectativa igual a la medida de rendimiento en estado estacionario deseada.

## Intervalos de confianza para la diferencia entre las medidas de rendimiento de 2 sistemas

Aquí consideramos el caso especial de la comparación de dos sistemas sobre la base de algunas de las medidas de rendimiento, o la respuesta esperada. Efectuamos esta comparación mediante la formación de un intervalo de confianza para la diferencia en las dos expectativas, en lugar de hacerlo por un test de hipótesis para ver si la diferencia observada es significativamente diferente de cero.

Para i = 1, 2, sea Xi1, Xi2,…, Xin una muestra de ni observaciones IID del sistema i, y sea la respuesta de interés esperada; queremos construir un intervalo de confianza para . Ya sea o no que X1i y X2i son independientes depende en como la simulación se ejecute.

Un intervalo de confianza t-apareada

Si , o están dispuestos a descartar algunas observaciones del sistema en el que en realidad tenemos más datos, se puede emparejar X1i con X2i para definir , para j=1, 2,…, n. Entonces Zj son variables aleatorias IID y , la cantidad por la que queremos construir un intervalo de confianza. Por lo tanto, podemos hacer y y formar el (aproximado) 100(1 - α) % intervalo de confianza . Si los Zj está distribuido normalmente, este intervalo de confianza es exacto, de lo contrario, nos basamos en el teorema central del límite. No tenemos que asumir que X1i y X2i son independientes; ni que . Permitir correlación positiva entre X1i y X2i puede ser de gran importancia, ya que esto conduce a una reducción en Var(Zj) y por lo tanto a un intervalo de confianza más pequeño. El intervalo de confianza se conoce como intervalo de confianza t apareadas, y en su derivación redujimos esencialmente el problema de los dos sistema a uno que implica una sola muestra. Los Xij son variables aleatorias definidas sobre toda una réplica.

Un intervalo de confianza de 2 muestras t modificado

Un segundo enfoque para la formación de un intervalo de confianza para no empareja las observaciones de los 2 sistemas, pero requiere que las X1i sean independientes de las X2i. Sin embargo, n1 y n2 pueden ser diferentes.

Para aplicar el clásico enfoque de 2 muestras, debemos tener Var(X1i) = Var(X2i). Aunque la igualdad de variancias no es probablemente una suposición segura cuando simulamos sistemas reales, recomendamos usar este enfoque.

El problema de comparación de 2 sistemas con variancia desigual y desconocida cuando las X2i están distribuidas normalmente. Sea

Para i = 1, 2. Luego calculamos los grados de libertad estimados

Y usamos como una aproximación del intervalo de confianza para con un nivel de confianza de 100(1 – α)%. El intervalo de confianza, conocido como el intervalo de confianza de Welch, puede también usarse para validar un modelo de simulación de un sistema existente.

Comparando los 2 métodos

La elección del método a usar usualmente se hará de acuerdo a la situación. Una consideración es que el uso de números aleatorios comunes para simular los 2 sistemas puede a veces conducir a una considerable reducción en Var(Zj) y, por lo tanto, a un intervalo de confianza más pequeño; esto implica que n1 = n2 y que X1j y X2j no serán independientes, por eso el enfoque t-apareada es requerido. Por otro lado, si se debe usar el método Welch.

Comparaciones basadas en las medidas de rendimiento en estado estacionario

El ingrediente básico de la mayoría de las técnicas de comparación es una muestra de observaciones IID con expectativa igual a la medida de rendimiento sobre la cual se hace la comparación.

En algunos casos, queremos comparar 2 o más sistemas sobre la base de una medida de rendimiento en estado estacionario. Aquí ya no podemos simplemente replicar los modelos, ya que los efectos de inicialización pueden sesgar los resultados. Es más difícil efectuar una comparación válida basada en las medidas de rendimiento en estado estacionario. El método de replicación/borrado para el análisis en estado estacionario puede adaptarse al problema de construir un intervalo de confianza para la diferencia entre 2 medias en estado estacionario.

## Intervalos de confianza para comparar más de 2 sistemas

Haremos distintos declaraciones de intervalos de confianza simultáneamente, por lo que sus niveles individuales tendrán que ajustarse hacia arriba para que el nivel de confianza global de la cobertura de todos los intervalos de sus respectivos objetivos esté en el nivel deseado 1 – α. Usamos para asegurar que el nivel de confianza global es al menos 1 – α.

Comparaciones con un estándar

Supongamos que uno de las variantes del modelo es un estándar. Si llamamos al estándar sistema 1 y a las otras variantes sistemas 2, 3,…, k, el objetivo es construir k – 1 intervalos de confianza para las k – 1 diferencias , con un nivel de confianza global 1 – α. Hacemos c = k – 1 intervalos individuales con un nivel de . Entonces podemos decir que para todo i = 2, 3,…, k, el sistema i difiere del estándar si el intervalo para no alcanza 0, y que el sistema i no es significativamente diferente del estándar si este intervalo contiene 0.

Todas las comparaciones por pares

En algunos estudios, queremos comparar cada sistema con cada otro para detectar y cuantificar cualquier diferencia de pares significativa. Un enfoque consistiría en formar intervalos de confianza para las diferencias , para todo e entre 1 y k, con . Aquí habrá intervalos individuales, por eso cada uno debe hacerse con un nivel en orden de tener un nivel de confianza de al menos 1 – α para todos los intervalos juntos.