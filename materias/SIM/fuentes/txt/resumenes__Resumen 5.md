Resumen de Simulación
Índice
Capítulo 1: Introducción a la simulación en computadoras (Naylor) .............................................. 2
Definición de la simulación en computadoras ..................................................................................... 2
Fundamentos racionales de la simulación en computadoras ............................................................. 2
Propiedades de los modelos de simulación ........................................................................................ 2
Clasificación de los modelos para simulación ..................................................................................... 3
Capítulo 2: Planeación de los experimentos de simulación en computadora (Naylor) ................. 3
Etapas de la simulación ....................................................................................................................... 3
1)Formulación del problema ............................................................................................................ 3
2)Recolección y procesamiento de datos tomados de la realidad .................................................. 3
3)Formulación de los modelos matemáticos ................................................................................... 4
4)Estimación de los parámetros de las características operacionales a partir de los datos reales 4
5)Evaluación del modelo y de los parámetros estimados ............................................................... 4
6)Formulación de un programa para la computadora ..................................................................... 4
7)Validación ..................................................................................................................................... 5
8)Diseño de los experimentos de simulación .................................................................................. 5
9)Análisis de los datos simulados ................................................................................................... 5
Capítulo 3: Técnicas para la generación de los números aleatorios (Naylor) ................................ 5
Introducción ......................................................................................................................................... 5
Métodos de congruencias para generar números pseudo-aleatorios ................................................. 6
Pruebas estadísticas para los números pseudo-aleatorios ................................................................ 6
Capítulo 4: Generación de valores de las variables estocásticas empleadas en simulación
(Naylor) ................................................................................................................................................... 8
Introducción ......................................................................................................................................... 8
Distribuciones continúas de probabilidad ............................................................................................ 9
Distribuciones discretas de probabilidad ........................................................................................... 10
Capítulo 1: Modelado de Simulación Básico (Law & Kelton) ......................................................... 12
La naturaleza de la simulación .......................................................................................................... 12
Sistemas, modelos y simulación ....................................................................................................... 12
Simulación de Eventos Discretos: ..................................................................................................... 13
Simulación de un Sistema de Colas de un solo Servidor (M/M/1): ................................................... 13
Reglas de interrupción alternativas ................................................................................................... 15
Determinando los eventos y variables .............................................................................................. 15
Simulación distribuida ........................................................................................................................ 16
Pasos en un estudio de simulación ................................................................................................... 16
Otros tipos de simulación .................................................................................................................. 16
Ventajas, desventajas y dificultades de la simulación ...................................................................... 17
Capítulo 9: Modelo Analítico para una cola M/M/1 (Mc Millan - Gonzalez). ................................... 17
Tipos de sistemas de colas: .............................................................................................................. 17
Caso M/M/1: ...................................................................................................................................... 17
Medidas de rendimiento: ................................................................................................................... 19
Capítulo 15: Verificación de los resultados de simulación (Gordon) ............................................ 21
Naturaleza del problema ................................................................................................................... 21
Métodos de estimación ...................................................................................................................... 21
Estadísticas de corridas de simulación ............................................................................................. 21
Repetición de corridas ....................................................................................................................... 22
Eliminación del sesgo inicial .............................................................................................................. 22
Medias de lotes ................................................................................................................................. 22
Análisis de series de tiempo .............................................................................................................. 22
Análisis espectral ............................................................................................................................... 23
Capítulo 9: Análisis de Datos de Salida (Law & Kelton) .................................................................. 23
Comportamiento transitorio y en estado estacionario de un proceso estocástico ............................ 24
Tipos de simulaciones con respecto al análisis de la salida ............................................................. 24
Análisis Estadístico para Simulaciones Terminales .......................................................................... 24
Múltiples medidas de rendimiento ..................................................................................................... 27
Resumen: Construcción de Intervalos de Confianza ........................................................................ 27
Capítulo 10: Comparando las configuraciones del sistema alternativas (Law & Kelton) ........... 27
Introducción ....................................................................................................................................... 27
Intervalos de confianza para la diferencia entre las medidas de rendimiento de 2 sistemas ........... 27
Intervalos de confianza para comparar más de 2 sistemas .............................................................. 28

Capítulo 1: Introducción a la simulación en computadoras (Naylor)
Definición de la simulación en computadoras
Simulación es una técnica numérica para conducir experimentos en una computadora digital, los
cuales requieren ciertos tipos de modelos lógicos y matemáticos, que describen el comportamiento de
un negocio o un sistema económico en períodos extensos de tiempo real.
Variantes:
✓ Juegos operacionales: simulaciones que se caracterizan por alguna forma de interés en con-
flicto entre los jugadores o los seres humanos que toman decisiones dentro del marco de re-
ferencia del medio ambiente simulado. Dentro de estos se encuentran los juegos militares y
los juegos de gerencia.
✓ Análisis de Monte Carlo: es una técnica de simulación para problemas que tienen una base
estocástica o probabilística. Existen 2 tipos: aquellos problemas que implican algún tipo de
proceso estocástico y aquellos problemas matemáticos completamente determinísticos, que
no pueden resolverse fácilmente por métodos estrictamente determinísticos.
Fundamentos racionales de la simulación en computadoras
✓ Búsqueda constante del hombre por adquirir conocimientos relativos a la predicción del futu-
ro.
✓ Puede ser imposible o extremadamente costoso observar ciertos procesos en el mundo real.
✓ El sistema observado puede ser tan complejo que sea imposible describirlo en términos de un
sistema de ecuaciones matemáticas.
✓ Puede no obtenerse una solución del modelo por medio de técnicas analíticas directas.
✓ Resultaría casi imposible o muy costoso realizar experimentos de validación en los modelos
matemáticos que describen al sistema.
Otras razones:
✓ La simulación hace posible estudiar y experimentar con las complejas interacciones que ocu-
rren en el interior de un sistema dado.
✓ A través de la simulación se pueden estudiar los efectos de ciertos cambios en la operación
de un sistema.
✓ La observación detallada del sistema que se está simulando, conduce a un mejor entendi-
miento del mismo y proporciona sugestiones para mejorarlo.
✓ La simulación puede utilizarse como recurso pedagógico.
✓ Los juegos operacionales han demostrado constituir un medio excelente para estimular el in-
terés y el entendimiento de parte del participante y son particularmente útiles en la orientación
de las personas con experiencia en la disciplina relativa al juego.
✓ La experiencia que se adquiere al diseñar un modelo de simulación en una computadora,
puede ser más valiosa que la simulación en sí misma.
✓ La simulación de sistemas complejos puede producir un valioso y profundo conocimiento
acerca de cuáles variables son más importantes y como ellos obran entre sí.
✓ La simulación puede emplearse para experimentar con situaciones nuevas.
✓ La simulación puede servir como una prueba de pre-servicio.
✓ Proporcionan una forma conveniente de dividir un sistema complicado en subsistemas.
✓ Para ciertos tipos de problemas estocásticos, la secuencia de los eventos puede ser muy im-
portante.
✓ Las simulaciones de Monte Carlo pueden realizarse para verificar soluciones analíticas.
✓ La simulación permite estudiar los sistemas dinámicos.
✓ Cuando se presentan nuevos componentes de un sistema, la simulación puede emplearse
para ayudar a descubrir los obstáculos y otros problemas.
✓ La simulación convierte a los especialistas en técnicos generales.
Propiedades de los modelos de simulación
El objeto del modelo científico es permitir al analista la determinación de uno o más cambios en los
aspectos del sistema modelado que afectan otros aspectos del sistema. Para que un modelo científi-
co sea útil, debe ser realista (debe servir como una aproximación razonable al sistema real y debe
incorporar la mayor parte de los aspectos importantes de este) y simple.
Los modelos constan de 4 elementos: componentes, variables, parámetros y relaciones funciona-
les.
Los componentes de los modelos económicos tienden a variar ampliamente. (Son los elementos
del sistema que se estudiarán)
Las variables relacionan un componente con otro y se clasifican en:
Página 2 de 29

✓ Exógenas: son las independientes o de entrada, han sido predeterminadas y proporcionadas
independientemente del sistema que se modela. Actúan sobre el sistema, pero no reciben ac-
ción alguna de parte de él. Se subdividen en controlables y no controlables, según sean sus-
ceptibles de manipulación o control por quienes toman decisiones o crean políticas para el
sistema.
✓ De estado: describen el estado de un sistema o uno de sus componentes. Interaccionan con
las variables exógenas y endógenas, de acuerdo a relaciones funcionales. El valor de una va-
riable de estado puede depender no solo de variables exógenas, sino también de ciertas va-
riables de salida en períodos anteriores. En estos casos decimos que ocurre una retroalimen-
tación.
✓ Endógenas: son las dependientes o de salida del sistema y son generadas por la interacción
de las variables exógenas con las de estado.
La clasificación de la variable depende del propósito de la investigación. Las variables exógenas
se pueden tratar como parámetros, las cuales tienen que estimarse con anterioridad, o como varia-
bles estocásticas, pudiendo ser generadas por computadora.
Los parámetros se denominan factores, los cuales se varían para ver sus efectos sobre las varia-
bles endógenas.
Hay 2 relaciones funcionales que describen la interacción de las variables y los componentes,
usados para generar el comportamiento del sistema:
✓ Identidades: tomarán la forma de definiciones o declaraciones tautológicas, relativas a los
componentes del modelo.
✓ Característica de operación: es una hipótesis que relaciona las variables endógenas y de es-
tado con sus variables exógenas. En los procesos estocásticos toman la forma de funciones
de densidad de probabilidad. Los parámetros de las características de operación los deriva-
mos sobre la base de inferencias estadísticas.
Clasificación de los modelos para simulación
Modelos determinísticos: Ni las variables exógenas ni a las endógenas se les permite ser variables
al azar. Se suponen relaciones exactas para las características de operación. Es posible resolverlos
analíticamente.
Modelos estocásticos: Aquellos modelos en los que por lo menos una de las características de
operación está dada por una función de probabilidad. Son más complejos que los modelos determi-
nísticos.
Modelos estáticos: No toman en cuenta la variable tiempo.
Modelos dinámicos: Modelos matemáticos que tratan de las interacciones que varían con el tiem-
po.
Capítulo 2: Planeación de los experimentos de simulación en
computadora (Naylor)
La decisión de emplear la simulación como técnica para resolver un problema no es una tarea
sencilla. Tal decisión se apoya en la aplicabilidad, el costo y la simplicidad.
Etapas de la simulación
1) Formulación del problema
Deben tomarse 2 decisiones importantes antes de comenzar a trabajar con cualquier experimento
de simulación: hay que decidir los objetivos de nuestra investigación y es necesario decidir el conjun-
to de criterios para evaluar el grado de satisfacción al que deba sujetarse el experimento.
2) Recolección y procesamiento de datos tomados de la realidad
Razones por las cuales es necesario disponer de un sistema eficiente para el procesamiento de
datos:
✓ La información descriptiva y cuantitativa constituye un requisito previo a la formulación del
problema.
✓ Los datos que hayan sido reducidos a una forma significativa pueden sugerir hipótesis de
cierta validez, las cuales se usarán en la formulación de los modelos matemáticos.
✓ Los datos también pueden sugerir mejoras o refinamientos en los modelos matemáticos que
existen en el sistema por simularse.
✓ Es necesario que los datos se utilicen para estimar los parámetros de las características de
operación relativas a las variables endógenas, exógenas y de estado del sistema.
✓ Sin tales datos sería imposible probar la validez de un modelo para la simulación.
Página 3 de 29

Funciones del procesamiento de datos:
✓ Recolección: proceso de captación de los hechos disponibles.
✓ Almacenamiento de los datos recolectados.
✓ Conversión de los datos de una forma a otra.
✓ Transmisión de la información al lugar en donde será procesada.
✓ Manipulación: operaciones como clasificar, cotejar, intercalar, recuperar información y otras,
como las operaciones aritméticas y lógicas.
✓ Salida: informe sobre los resultados obtenidos.
3) Formulación de los modelos matemáticos
Consiste en:
1. Especificación de los componentes.
2. Especificación de las variables y los parámetros.
3. Especificación de las relaciones funcionales.
Consideraciones a tener en cuenta:
✓ Cantidad de variables que se deben incluir en el modelo: Hay poca dificultad con las variables
endógenas. La dificultad surge en la elección de las variables exógenas. Pocas variables
pueden llevar a modelos inválidos, una abundancia hace imposible la simulación.
✓ Complejidad: Estamos interesados en la formulación de modelos matemáticos que produzcan
descripciones o predicciones, razonablemente exactas, referentes al comportamiento de un
sistema dado y reduzcan a la vez, el tiempo de computación y programación.
✓ Cantidad de tiempo de cómputo requerida para lograr algún objetivo experimental específico:
los objetivos pueden ser:
• Reducir el tiempo de cómputo requerido para generar los valores de nuestras varia-
bles endógenas sobre un período específico.
• Reducir el tiempo de computación requerido para lograr algún nivel de precisión esta-
dística previamente determinado.
✓ El tiempo consumido en la programación de la computadora.
✓ Cantidad de realismo incorporado en ellos.
✓ Compatibilidad con el tipo de experimentos que se van a realizar con ellos.
Dificultades potenciales:
✓ Quizás sea imposible cuantificar o medir ciertos tipos de variables.
✓ El número de variables posiblemente exceda la capacidad de la computadora.
✓ Podemos desconocer algunas de las variables exógenas significativas.
✓ Podemos desconocer algunas de las relaciones entre variables exógenas y endógenas.
✓ Las relaciones entre las variables que afectan el comportamiento del sistema son en muchos
casos tan complejas que no pueden expresarse como una o más ecuaciones matemáticas.
Tipos básicos de diseño:
✓ Diseños generalizados: describe el comportamiento de un sistema completo.
✓ Diseños modulares o de bloques: conjunto de modelos que describen los componentes prin-
cipales del sistema.
4) Estimación de los parámetros de las características operacionales a partir de los
datos reales
Se estiman los valores de los parámetros de los modelos y se prueba su significación estadística.
5) Evaluación del modelo y de los parámetros estimados
Es necesario hacer un juicio del valor inicial de la suficiencia de nuestro modelo una vez que for-
mulamos un conjunto de modelos matemáticos y estimamos los parámetros. Nuestro interés reside
en probar las suposiciones o entradas que se programarán en la computadora.
6) Formulación de un programa para la computadora
Se deben considerar las siguientes actividades:
1. Diagrama de flujo: bosqueja la secuencia lógica de los eventos que realizará la computadora.
2. Lenguaje de la computadora: una vez terminado el diagrama de flujo, se puede escribir el có-
digo para la computadora. Se pueden usar lenguajes de propósitos generales o lenguajes de
simulación de propósitos específicos. Estos últimos permiten un ahorro en tiempo de progra-
mación.
3. Búsqueda de errores: los lenguajes de simulación de propósitos específicos proporcionan
técnicas para la búsqueda de errores superiores a las provistas por los lenguajes de propósi-
tos generales.
Página 4 de 29

4. Datos de entrada y condiciones iniciales: se debe determinar el valor que se les debería asig-
nar a las variables y parámetros del modelo en el momento en que comenzamos a simular el
sistema.
5. Generación de datos: consiste en el desarrollo de técnicas numéricas para la generación de
datos.
6. Reportes de salida: necesarios para dar la información relativa al comportamiento de nuestro
sistema bajo simulación.
7) Validación
Implica un sinnúmero de complejidades de tipo práctico, teórico, estadístico e inclusive filosófica.
Hay 2 pruebas para validar los modelos de simulación:
✓ ¿Qué tan bien coinciden los valores simulados de las variables endógenas con datos históri-
cos conocidos?
✓ ¿Qué tan exactas son las predicciones del comportamiento del sistema real hechas por el
modelo de simulación, para períodos futuros?
8) Diseño de los experimentos de simulación
Metas:
✓ Seleccionar los niveles de los factores y las combinaciones de niveles, así como el orden de
los experimentos.
✓ Asegurar que los resultados queden razonablemente libres de errores fortuitos.
9) Análisis de los datos simulados
Pasos:
✓ Recolección y procesamiento de los datos simulados.
✓ Cálculo de la estadística de las pruebas.
✓ Interpretación de los resultados.
Capítulo 3: Técnicas para la generación de los números aleatorios
(Naylor)
Introducción
El término variable aleatoria se emplea para nombrar una función de valor real, definida sobre un
espacio muestral asociado con los resultados de un experimento conceptual de naturaleza azarosa.
El resultado particular de un experimento se llama valor de la variable aleatoria. F(x), la función de la
distribución acumulativa para una variable aleatoria X, indica la probabilidad de que X sea menor o
igual al particular valor x de la variable aleatoria. f(x) representa el valor de la función de densidad de
probabilidad de la variable aleatoria X cuando X = x.
Función de densidad de probabilidad uniforme:
0, 𝑥 ≤0
𝐹(𝑥)={𝑥, 0<𝑥 <1
1, 𝑥 ≥1
Los valores de x, en el intervalo unitario, se llamarán valores uniformes de las variables aleatorias.
En la práctica, se suelen requerir sucesiones de números aleatorios, y uno de los requisitos princi-
pales es el de la independencia estadística.
Métodos para generar sucesiones de números aleatorios:
✓ Métodos manuales: son menos prácticos, más simples y muy lentos. Es imposible de repro-
ducir una sucesión.
✓ Tablas de biblioteca: tuvieron que ser generados con uno de los otros métodos. Siempre pue-
den reproducirse. No son rápidos. Ciertos problemas requieren más números de los publica-
dos.
✓ Métodos de computación analógica: son mucho más rápidos. Las sucesiones no son repro-
ducibles.
✓ Métodos de computación digital
• Provisión externa: graba las tablas de números aleatorios en una cinta magnética.
• Generación interna por medio de procesos físicos aleatorios: uso de un aditamento
especial de la computadora digital capaz de registrar los resultados de algún proceso
aleatorio y además reduzca estos resultados a sucesiones de dígitos. No se pueden
reproducir. Los procesos aleatorios pueden salirse de control.
• Generación interna por medio de una relación de recurrencia: generación de los nú-
meros pseudo-aleatorios por medio de una transformación indefinidamente continua-
da, aplicada a un grupo de números elegidos en forma arbitraria.
Página 5 de 29

En el método de los cuadrados centrales, cada número de la sucesión se obtiene tomando los dí-
gitos centrales del cuadrado del número precedente. Resultó difícil de analizarse, relativamente lento
y estadísticamente poco satisfactorio. (La semilla debe tener 3 o más dígitos. Este método tiende a
números cada vez más pequeños.)
Un método para generar números aleatorios debe producir sucesiones de números que sean:
✓ Uniformemente distribuidos.
✓ Estadísticamente independientes.
✓ Reproducibles.
✓ Sin repetición dentro de una longitud determinada de la sucesión.
✓ Generar números aleatorios a grandes velocidades.
✓ Requerir un mínimo de la capacidad de almacenamiento.
Procedimiento para generar números aleatorios:
a. Un proceso que produce números aproximadamente aleatorios.
b. Un proceso, que aplicado a las sucesiones de números, mejore la aleatoriedad de la suce-
sión.
c. Un conjunto de pruebas de aleatoriedad.
d. El uso de un método de almacenamiento que permita leer una gran cantidad de números
aleatorios a una velocidad proporcional a su velocidad de operación.
Métodos de congruencias para generar números pseudo-aleatorios
Son métodos determinísticos, ya que los procesos aritméticos que se incluyen en los cálculos de-
terminan unívocamente cada término de la sucesión de números. Aunque estos procesos no son del
todo aleatorios, las sucesiones que resultan de ellos superan las pruebas estadísticas, por lo que nos
permiten considerarlos como si en efecto lo fueran.
Se basan en una relación fundamental de congruencia 𝑛 =(𝑎𝑛 +𝑐) 𝑚𝑜𝑑 𝑚, donde 𝑛 , a, c y m
𝑖+1 𝑖 𝑖
son enteros no negativos.
𝑛 =(𝑎𝑖𝑛 +
𝑐(𝑎𝑖−1)
)𝑚𝑜𝑑 𝑚, 𝑖 =1,2,…
𝑖 0 (𝑎−1)
Los términos n son todos enteros y 𝑛 ≤𝑚 para toda n. A partir de la sucesión { n }, se pueden
i 𝑖 i i
obtener números racionales en el intervalo ( 0,1 ), { r } = { n/m }.
i i
Existe un mínimo valor positivo para i, h, tal que n = n en donde h es el período de la sucesión
h 0
{n}. El valor máximo de h depende de m. Es imposible obtener sucesiones que no se repiten, utilizan-
i
do los métodos de congruencias.
Método aditivo de congruencias: Presupone k valores iniciales
𝑛 =(𝑛 + 𝑛 )𝑚𝑜𝑑 𝑚
𝑖+1 𝑖 𝑖−𝑘
Si k = 1 genera la sucesión de Fibonacci. Este es el único método que produce períodos mayores
que m.
Método multiplicativo de congruencias:
𝑛 =(𝑎𝑛 ) 𝑚𝑜𝑑 𝑚
𝑖+1 𝑖
Es un caso especial de la relación de congruencia, con c = 0.
Método mixto de congruencias: Tanto a como c son mayores a cero. Su principal ventaja radica en
su período completo. Las condiciones que se imponen sobre a y c, a fin de lograr un período comple-
to para m:
✓ c y m son primos relativos.
✓ 𝑎 ≡1 (𝑚𝑜𝑑 𝑝) si p es un factor primo de m.
✓ 𝑎 ≡1 (𝑚𝑜𝑑 4) si 4 es un factor de m.
Pruebas estadísticas para los números pseudo-aleatorios
Las propiedades estadísticas de los números pseudo-aleatorios generados por los métodos que
se han delineado deben coincidir con las propiedades estadísticas de los generados por un instru-
mento aleatorio idealizado. En la medida en que nuestros números pseudo-aleatorios puedan pasar
las pruebas estadísticas, denotadas por el instrumento aleatorio idealizado, estos números pseudo-
aleatorios pueden tratarse como verdaderos números aleatorios aunque no lo sean.
Prueba de la frecuencia
Se usa para comprobar la uniformidad de una sucesión de M conjuntos consecutivos de N núme-
ros pseudo-aleatorios. Para cada conjunto dividimos el intervalo (0, 1) en x sub-intervalos iguales. El
número esperado de números pseudo-aleatorios que se encontrarán en cada sub-intervalo es N/x. Si
Página 6 de 29

f, con j = 1, 2,…, x, denota el número que realmente se tiene en el sub-intervalo (𝑗−1)⁄𝑥 ≤𝑟 ≤𝑗⁄𝑥.
j 𝑖
Entonces la estadística
𝑥 𝑥 𝑁 2
𝜒 2 =( )∑(𝑓 − )
1 𝑁 𝑗 𝑥
𝑗=1
Tiene aproximadamente una distribución chi cuadrado con x - 1 grados de libertad. Si F denota el
j
número que resulta de los M valores de 𝜒 2, se calcula
1
𝑢 𝑢 𝑀 2
𝜒 2 =( )∑(𝐹 − )
𝐹 𝑀 𝑗 𝑢
𝑗=1
La hipótesis de que los números pseudo-aleatorios en la sucesión son verdaderos números alea-
torios debe rechazarse si 𝜒 2 con u – 1 grados de libertad excede al valor crítico fijado por el nivel de
𝐹
significancia deseado.
Prueba de series
Comprueba el grado de aleatoriedad entre los números sucesivos en una sucesión. Se genera una
sucesión de M conjuntos consecutivos de números pseudo-aleatorios, y calculamos la estadística chi
cuadrado para cada conjunto. A continuación, para cada conjunto, f denota el total de números
jk
pseudo-aleatorios que satisfacen (𝑗−1)⁄𝑥 ≤𝑟 ≤𝑗⁄𝑥 y (𝑘−1)⁄𝑥 ≤𝑟 ≤𝑘⁄𝑥 con j, k = 1, 2,…, x.
𝑖 𝑖
Luego calculamos la estadística
𝑥2 𝑥 𝑥 𝑁−1 2
𝜒 2 =( )∑∑(𝑓 − )
2 𝑁−1 𝑗𝑘 𝑥2
𝑗=1𝑘=1
Para cada conjunto. Sin embargo, 𝜒 2−𝜒 2 tiene una distribución chi cuadrado con x2 – x grados
2 1
de libertad. Luego calculamos 𝜒 2−𝜒 2 para cada conjunto y dejamos que s denote el número de M
2 1 j
valores de 𝜒 2−𝜒 2 que se encuentran entre el (j - 1)-esimo y el j-esimo cuartil. Finalmente
2 1
𝑢 𝑢 𝑀 2
𝜒 2 =( )∑(𝑠 − )
𝑆 𝑀 𝑗 𝑢
𝑗=1
La cual tiene u – 1 grados de libertad. La aleatoriedad resulta aceptable, a cierto nivel dado de
significancia, si los valores 𝜒 2 y 𝜒 2 no son inconsistentes con la hipótesis de que fueron derivados al
𝐹 𝑆
azar, a partir de distribuciones chi cuadrado, con los grados de libertad adecuados.
Prueba del producto rezagado
Mide la independencia entre los números pseudo-aleatorios. Si k es la longitud del rezago, el coe-
ficiente del producto rezagado C se define como
k
𝑁−𝑘
1
𝐶 = ∑𝑟𝑟
𝑘 𝑁−𝑘 𝑖 𝑖+𝑘
𝑖=1
Si no existe correlación entre 𝑟 y 𝑟 , los valores de 𝐶 se distribuyen normalmente con esperan-
𝑖 𝑖+𝑘 𝑘
za 0,25 y desvió estándar √13𝑁−19𝑘⁄12(𝑁−𝑘)
Pruebas de corridas
Corridas arriba y abajo
Para una sucesión de N números pseudo-aleatorios r , r ,…, r definimos una sucesión binaria S
1 2 N
de N – 1 bits, cuyo i-esimo término es igual a 0 si r < r y es igual a 1 si r > r . Una sub-sucesión de
i i+1 i i+1
k ceros, enmarcada por unos en cada extremo, recibe el nombre de corrida de ceros de longitud k;
similarmente se definen las corridas de unos. La prueba implica determinar las ocurrencias de corri-
das de distinta longitud y comparar estos conteos con sus valores teóricos correspondientes espera-
dos.
(2𝑁−1)
para el número total de corridas
3
2[(𝑘2+3𝑘+1)𝑁−(𝑘3+3𝑘2−𝑘−4)]
para corridas de longitud k, con k < N – 1
(𝑘+3)!
2
para corridas de longitud N - 1
𝑁!
Nuevamente, la confiabilidad del ajuste se prueba con el criterio de chi cuadrado.
Corridas encima y debajo de los promedios
Para una sucesión de N números pseudo-aleatorios r , r ,…, r definimos una sucesión binaria S
1 2 N
de N bits, cuyo i-esimo término es igual a 0 si r < 1/2 y es igual a 1 si r > 1/2. Deben contarse las
i i
Página 7 de 29

corridas en S; el número de corridas de longitud k esperadas es (𝑁−𝑘+3)2−𝑘−1, y el número total
de corridas que se esperan es (𝑁+1)⁄2. Se puede emplear una prueba de chi cuadrado para com-
probar si el generador resulta aceptable.
Prueba de distancia
Para cualquier digito dado d, estamos interesados en las longitudes de las distancias de los dígitos
que no son d, entre 2 dígitos dados cualesquiera. Una distancia de longitud k ocurre cuando k de los
dígitos que no son d se encuentran entre 2 dígitos d. Para una sucesión verdaderamente aleatoria, la
probabilidad de obtener una distancia de longitud k es 𝑃(𝑘)=(0,9)𝑘(0,1).
Para una sucesión dada de dígitos, se hacen correspondencias entre el número de distancias que
ocurren para cada longitud. Se puede usar una prueba de chi cuadrado para analizar la confiabilidad
del ajuste y compararlo con el número de distancias esperadas y reales de longitud k.
Prueba de máximos
Para un conjunto de N números aleatorios independientes y uniformes en el intervalo unitario (0,
1), podemos definir una variable aleatoria max (r , r ,…, r ), que tenga una distribución de probabili-
1 2 N
dad definida por estadísticas de orden, tales que RN esté uniformemente distribuida en (0, 1). La
prueba de los valores observados para RN es una simple prueba de frecuencias.
Prueba de Poker
Es una prueba de frecuencia especial para combinaciones de 5 o más dígitos en un número alea-
torio. Cuenta con pares, 2 pares, tercias, fulles, etc. que se prueban contra la frecuencia esperada de
sus ocurrencias.
Capítulo 4: Generación de valores de las variables estocásticas
empleadas en simulación (Naylor)
Introducción
Al considerar los procesos estocásticos que involucran variables continuas o discretas, definimos
la función F(x) función de distribución acumulativa de x como la probabilidad de que una variable
aleatoria X tome un valor menor o igual a x. Si la variable es discreta, x tendrá valores específicos y
F(x) será una función escalonada. Si F(x) es continua en el dominio de x, se podrá diferenciar. 𝑓(𝑥)=
𝑑𝐹(𝑥)⁄𝑑𝑥 es la función de densidad de probabilidad.
𝑥
𝐹(𝑥)=𝑃(𝑋 ≤𝑥)=∫ 𝑓(𝑡)𝑑𝑡, 0≤𝐹(𝑥)≤1
−∞
f(t) representa el valor de la función de densidad de probabilidad de la variable aleatoria X cuando
X = t.
Denotamos con r los valores de variables aleatorias uniformes cuando 0≤𝑟 ≤1 y 𝐹(𝑟)=𝑟.
Se tienen 3 métodos para generar los valores de variables aleatorias a partir de las distribuciones
de probabilidad.
Método de la transformación inversa
Si deseamos generar los valores x a partir de f(x), debemos obtener F(x). Puesto que F(x) se defi-
i
ne sobre el rango de 0 a 1, podemos generar números aleatorios distribuidos uniformemente y ade-
más hacer F(x) = r. Para cualquier valor particular de r, siempre es posible encontrar el valor de x,
debido a la función inversa de F, si es conocida
𝑥 =𝐹−1(𝑟 )
0 0
𝐹−1(𝑥) es la transformación inversa de r sobre el intervalo unitario en el dominio de x.
𝑟 =𝐹(𝑥)=𝑃(𝑋 ≤𝑥)=𝑃[𝑟 ≤𝐹(𝑥)]=𝑃[𝐹−1(𝑟)≤𝑥]
𝐹−1(𝑟) es una variable que tiene a f(x) como función de densidad de probabilidad.
Método de rechazo
Si f(x) es una función acotada y x tiene además un rango finito 𝑎 ≤𝑥 ≤𝑏. Etapas:
1. Normalizar el rango de f: 𝑐.𝑓(𝑥)≤1 , 𝑎≤𝑥 ≤𝑏
2. Definir a x como una función lineal de r: 𝑥 =𝑎+(𝑏−𝑎)𝑟
3. Generar parejas de números aleatorios (r r )
1 2
4. Siempre que se encuentre una pareja de números aleatorios que satisfagan la relación 𝑟 ≤
2
𝑐.𝑓[𝑎+(𝑏−𝑎)𝑟 ], dicho par será aceptado y se utilizará a 𝑥 =𝑎+(𝑏−𝑎)𝑟 como el valor
1 1
generado de la variable aleatoria.
Método de composición
Se expresa a f(x) como una mezcla probabilística de las funciones de densidad g (x).
n
Página 8 de 29

|     |     |     |     |     | 𝑓(𝑥)=∑𝑔 |     | (𝑥)𝑝  |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | ----- | --- | --- | --- | --- |
|     |     |     |     |     |         |     | 𝑛 𝑛   |     |     |     |     |
La guía para la selección de las 𝑔 (𝑥) está dada sobre las consideraciones relativas a la bondad
𝑛
del ajuste y al objetivo de minimizar ∑𝑇 𝑝 , donde T n  es el tiempo esperado de computación para
𝑛 𝑛
| generar valores de variables aleatorias a partir de 𝑔 |     |     |     |     |     | (𝑥).  |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
𝑛
Distribuciones continúas de probabilidad
Distribución uniforme
Constante en el intervalo (a, b) y cero fuera de él.
1
|           |        | ,                  𝑎             |                                  | <𝑥 <𝑏                    |                           |        | 𝑥         | 1         | 𝑥−𝑎 |           |     |
| --------- | ------ | -------------------------------- | -------------------------------- | ------------------------ | ------------------------- | ------ | --------- | --------- | --- | --------- | --- |
| 𝑓(𝑥)={𝑏−𝑎 |        |                                  |                                  |                          |                           | 𝐹(𝑥)=∫ |           |           |     | 0≤𝐹(𝑥)≤1  |     |
|           |        |                                  |                                  |                          |                           |        |           | 𝑑𝑡 =      | ,   |           |     |
|           |        |                                  |                                  |                          |                           |        | 𝑏−𝑎       |           | 𝑏−𝑎 |           |     |
|           |        | 0     ,𝑓𝑢𝑒𝑟𝑎 𝑑𝑒𝑙 𝑖𝑛𝑡𝑒𝑟𝑣𝑎𝑙𝑜 (𝑎,𝑏) |                                  |                          |                           |        | 𝑎         |           |     |           |     |
|           |        | 𝑏                                | 1                                | 𝑏+𝑎                      |                           |        |           | 𝑏(𝑥−𝐸(𝑋)) | 2   | (𝑏−𝑎)2    |     |
|           | 𝐸(𝑋)=∫ |                                  | 𝑥𝑑𝑥                              | =                        |                    𝑉(𝑋)=∫ |        |           |           | 𝑑𝑥  | =         |     |
|           |        | 𝑏−𝑎                              |                                  |                          | 2                         |        |           | 𝑏−𝑎       |     | 12        |     |
|           |        | 𝑎                                |                                  |                          |                           |        | 𝑎         |           |     |           |     |
|           |        |                                  | 𝑎=𝐸(𝑋)−√3𝑉(𝑋)                  𝑏 |                          |                           |        | =2𝐸(𝑋)−𝑎  |           |     |           |     |
Para simular una distribución uniforme en el intervalo (a, b) se obtiene la función inversa de F(x)
|     |     |     |     | 𝑥 =𝑎+(𝑏−𝑎)𝑟, |     |     | 0≤𝑟 | ≤1  |     |     |     |
| --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Cada número aleatorio r determina, de manera única, un valor de la variable aleatoria x uniforme-
mente distribuida.
Distribución exponencial
Se deben satisfacer las siguientes suposiciones:
✓  La probabilidad de que ocurra un evento en el intervalo [𝑡,(𝑡+∆𝑡)] es 𝛼∆𝑡.
✓  𝛼 es una constante que no depende de t o de algún otro factor.
✓  La probabilidad de que durante un intervalo [𝑡,(𝑡+∆𝑡)] ocurra más de un evento, tiende a 0 a
medida que ∆𝑡 →0, y su orden de magnitud deberá ser menor que el de 𝛼∆𝑡
𝑥
|     |     | 𝑓(𝑥)=𝛼𝑒−𝛼𝑥, |     | 𝛼 >0 𝑦 𝑥 | ≥0              𝐹(𝑥)=∫ |     |     | 𝛼𝑒−𝛼𝑡𝑑𝑡 | =1−𝑒−𝛼𝑥  |     |     |
| --- | --- | ----------- | --- | -------- | ---------------------- | --- | --- | ------- | -------- | --- | --- |
0
|     |     | ∞   |     |     |     |     | ∞   | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | 1   |     |     | 1   |     | 1   |     | 2   |
𝐸(𝑋)=∫ 𝑥𝛼𝑒−𝛼𝑡𝑑𝑥 =              𝑉(𝑋)=∫ (𝑥− ) 𝛼𝑒−𝛼𝑡𝑑𝑥 = =(𝐸(𝑋))
|     |     |     |     | 𝛼   |     |     | 𝛼   |     | 𝛼2  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 0   |     |     |     |     | 0   |     |     |     |     |
1
|     |     |     |     |     |     | 𝛼 = |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝐸(𝑋)
Puesto que F(x) existe explícitamente, se puede aplicar la técnica de transformación inversa. De-
bido a la simetría que existe entre la distribución uniforme sigue que la intercambiabilidad de F(x) y 1
– F(x).
1
𝑟=𝑒−𝛼𝑥                𝑥
|     |     |     |     |     |     | =−( | )log𝑟 =−𝐸(𝑋)log𝑟  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
𝛼
Para cada valor del número pseudo-aleatorio r se determina un único valor para x. Los valores de
x toman tan solo magnitudes no negativas.
Distribución gamma (Erlang)
Si un determinado proceso consiste de k eventos sucesivos y si el total del tiempo transcurrido pa-
ra dicho proceso se puede considerar igual a la suma de k valores independientes de la variable alea-
toria con distribución exponencial, cada uno de los cuales tiene un parámetro definido α, la distribu-
ción de esta suma coincidirá con una distribución gamma con parámetros α y k.
𝛼𝑘𝑥𝑘−1𝑒−𝛼𝑥
|     |     | 𝑓(𝑥)= |     |     | ,   | 𝛼 >0,𝑘 | >0 𝑦 𝑥 𝑛𝑜 𝑛𝑒𝑔𝑎𝑡𝑖𝑣𝑜  |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | ------ | ------------------- | --- | --- | --- | --- |
(𝑘−1)!
No existe una forma explícita para describir la función acumulativa de la distribución gamma.
|     |     |     |     |       | 𝑘                            |     |     | 𝑘   |     |     |     |
| --- | --- | --- | --- | ----- | ---------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | 𝐸(𝑋)= |                        𝑉(𝑋)= |     |     |     |     |     |     |

|     |     |     |     |     | 𝛼   |     |     | 𝛼2  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A medida que k se incrementa, la distribución tiende en forma asintótica a la distribución normal.
|     |     |     |     |     | 𝐸(𝑋) |                       | 𝐸(𝑋)2 |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --------------------- | ----- | --- | --- | --- | --- |
|     |     |     |     | 𝛼   | =    |                     𝑘 | =     |     |     |     |     |
|     |     |     |     |     | 𝑉(𝑋) |                       | 𝑉(𝑋)  |     |     |     |     |
Para generar valores de variable aleatoria con distribución gamma, se debe reproducir el proceso
aleatorio sobre el cual se basa la distribución. Se debe tomar la suma de los k valores de variable
aleatoria con distribución exponencial x 1 , x 2 ,…, x k , cuyo valor esperado es el mismo e igual a 1⁄𝛼
Página 9 de 29

|     |     |     |     | 𝑘     |     | 𝑘     |     |             | 𝑘   |     |     |
| --- | --- | --- | --- | ----- | --- | ----- | --- | ----------- | --- | --- | --- |
|     |     |     |     |       |     | 1     |     | 1           |     |     |     |
|     |     |     |     | 𝑥 =∑𝑥 | =−  | ∑log𝑟 |     | =− (log∏𝑟)  |     |     |     |
|     |     |     |     |       | 𝑖   | 𝛼     | 𝑖   | 𝛼           |     | 𝑖   |     |
|     |     |     |     | 𝑖=1   |     | 𝑖=1   |     |             | 𝑖=1 |     |     |
Distribución normal
Si la variable aleatoria tiene una función de densidad
|     |     |     |     |       | 1   | 1       | 𝑥−𝜇𝑥) 2 |      |     |     |     |
| --- | --- | --- | --- | ----- | --- | ------- | ------- | ---- | --- | --- | --- |
|     |     |     |     | 𝑓(𝑥)= |     | 𝑒 − 2 ( | 𝜎𝑥 ,    | −∞<𝑥 |     | <∞  |     |
𝜎 √2𝜋
𝑥
Entonces X tiene una distribución normal o gaussiana con parámetros 𝜇  y 𝜎 . Si 𝜇 =0 y 𝜎 =1,
|     |     |     |     |     |     |     |     |     |     | 𝑥 𝑥 | 𝑥 𝑥 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
la función recibe el nombre distribución normal estándar, con función de densidad
|     |     |     |     |       |     | 1 1 |     |         |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | ------- | --- | --- | --- |
|     |     |     |     | 𝑓(𝑧)= |     | 𝑒−  | 𝑧2  |         |     |     |     |
|     |     |     |     |       |     | 2   | ,   | −∞<𝑧<∞  |     |     |     |
√2𝜋
Cualquier distribución normal se puede convertir a la forma estándar
𝑥−𝜇
𝑥
|     |     |     |     |     |     | 𝑧=  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝜎
𝑥
La función de distribución acumulativa no existe en forma explícita
2
|     |     |     |     |     | 𝐸(𝑋)=𝜇 |             𝑉(𝑋)=𝜎 |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | ------------------ | --- | --- | --- | --- | --- |
|     |     |     |     |     |        | 𝑥                  |     |     | 𝑥   |     |     |
2, se debe proponer la siguien-
| A fin de simular una distribución normal con media 𝜇 |     |     |     |     |     |     |     |  y variancia 𝜎 |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- |
|                                                      |     |     |     |     |     |     |     | 𝑥              |     | 𝑥   |     |
te interpretación del teorema central del límite. Si r , r ,…, r  representan variables aleatorias inde-
|     |     |     |     |     |     |     | 1   | 2   | N   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pendientes, cada una de las cuales posee la misma distribución de probabilidad caracterizada por
𝐸(𝑟)=𝜃 y 𝑉(𝑟)=𝜎2, entonces
| 𝑖   | 𝑖   |     |     |     |       |       |      |     |      |       |     |
| --- | --- | --- | --- | --- | ----- | ----- | ---- | --- | ---- | ----- | --- |
|     |     |     |     |     | ∑𝑁    |       |      |     | 𝑏    |       |     |
|     |     |     |     |     |       | 𝑟 −𝑁𝜃 |      | 1   |      | 1 𝑧2  |     |
|     |     |     | lim | 𝑃[𝛼 | < 𝑖=1 | 𝑖     | <𝑏]= |     | ∫ 𝑒− | 2 𝑑𝑧  |     |
|     |     |     | 𝑁→∞ |     |       | √𝑁𝜎   |      | √2𝜋 |      |       |     |
𝑎
∑𝑁
| Donde 𝐸(∑𝑁 |     | 𝑟)=𝑁𝜃, 𝑉(∑𝑁 |     | 𝑟)=𝑁𝜎2 y 𝑧= |     |     | 𝑟𝑖−𝑁𝜃 |     |     |     |     |
| ---------- | --- | ----------- | --- | ----------- | --- | --- | ----- | --- | --- | --- | --- |
|            |     |             |     |             |     |     | 𝑖=1   |     |     |     |     |
|            | 𝑖=1 | 𝑖           |     | 𝑖=1 𝑖       |     |     | 𝜎√𝑁   |     |     |     |     |
Se sigue que z es un valor de variable aleatoria con distribución normal estándar.
Para simular valores normales, se requiere la suma de K valores de variable aleatoria distribuidos
| uniformemente, con 0≤𝑟 |     |     | 𝑖 ≤1.  |     |                 |     |       |        |                 |         |     |
| ---------------------- | --- | --- | ------ | --- | --------------- | --- | ----- | ------ | --------------- | ------- | --- |
|                        |     |     |        |     |                 |     |       |        |                 | ∑𝐾 −𝐾⁄2 |     |
|                        |     | 𝑎+𝑏 | 0+1    |     | 1               |     | 𝑏−𝑎   | 1      |                 | 𝑖=1 𝑟 𝑖 |     |
|                        |     | 𝜃 = | =      | =   |               𝜎 | =   |       | =      |              𝑧= |         |     |
|                        |     | 2   |        | 2   | 2               |     |       |        |                 |         |     |
|                        |     |     |        |     |                 |     | √12   | √12    |                 | √𝐾⁄12   |     |
|                        |     |     |        |     | 𝑥−𝜇             |     | ∑𝐾    | 𝑟 −𝐾⁄2 |                 |         |     |
|                        |     |     |        |     |                 | 𝑥   | 𝑖=1   | 𝑖      |                 |         |     |
|                        |     |     |        |     | 𝑧=              |     | =     |        |                 |         |     |
|                        |     |     |        |     |                 | 𝜎   | √𝐾⁄12 |        |                 |         |     |
𝑥
Despejando x se tiene que
|     |     |     |     |     |      | 12    | 𝐾   | 𝐾     |     |     |     |
| --- | --- | --- | --- | --- | ---- | ----- | --- | ----- | --- | --- | --- |
|     |     |     |     |     | 𝑥 =𝜎 | √ (∑𝑟 |     | − )+𝜇 |     |     |     |
|     |     |     |     |     | 𝑥    | 𝐾     | 𝑖   | 2     | 𝑥   |     |     |
𝑖=1
Distribuciones discretas de probabilidad
Solamente toman valores discretos (enteros no negativos).
𝑥
|     |     |     |     |     | 𝐹(𝑥)=𝑃(𝑋 |     | ≤𝑥)= | ∑𝑓(𝑥)  |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | ---- | ------ | --- | --- | --- |
𝑋=0
Donde f(x) es la frecuencia o función de probabilidad de X
|     |     |     |     | 𝑓(𝑥)=𝑃(𝑋 |     | =𝑥), |     | 𝑥 =0,1,2,…  |     |     |     |
| --- | --- | --- | --- | -------- | --- | ---- | --- | ----------- | --- | --- | --- |
Distribución geométrica
Los ensayos de Bernoulli son experimentos independientes al azar, en los que el resultado de ca-
da ensayo queda registrado como un éxito o un fracaso. La probabilidad de éxito se denota p (0≤
𝑝≤1) y se supone que es constante. La probabilidad de fracaso se denota q = 1 – p.
Los valores de variable aleatoria que se generan al contar el número de fracasos de una sucesión
de ensayos antes que ocurra el primer éxito, son valores de variable aleatoria que se ajustan a una
distribución geométrica.
𝑥
|     | 𝑓(𝑥)=𝑝𝑞𝑥, |     |     | 𝑥 =0,1,2,…               𝐹(𝑥)= |     |     |     | ∑𝑝𝑞𝑥, |     | 𝑋=0,1,2,…,𝑥  |     |
| --- | --------- | --- | --- | ------------------------------ | --- | --- | --- | ----- | --- | ------------ | --- |
𝑋=0
Página 10 de 29

𝐹(𝑥)=𝑃(𝑋 ≤𝑥) y como 𝑃(𝑋 =0)=𝐹(0)=𝑝, el rango de F(x) es 𝑝≤𝐹(𝑥)≤1. Por otra parte,
𝑃(𝑋 >𝑥)=1−𝐹(𝑥), lo que implica que 𝑃(𝑋 >0)=𝑞 y además 1−𝐹(𝑥)=𝑞𝑥+1
𝑞 𝑞 𝐸(𝑋) 1
𝐸(𝑋)= 𝑉(𝑋)= = 𝑝=
𝑝 𝑝2 𝑝 1+𝐸(𝑋)
Para generar valores de variable aleatoria con distribución geométrica se emplea la técnica de
transformación inversa y la fórmula 1−𝐹(𝑥)=𝑞𝑥+1. Al observar que el rango de 1−𝐹(𝑥)⁄𝑞 es unita-
rio, resulta que 𝑟 =𝑞𝑥, y consecuentemente 𝑥 = log𝑟 , donde al valor x siempre se lo redondea al ente-
log𝑞
ro menor.
Distribución binomial
Las variables aleatorias definidas por el número de eventos exitosos en una sucesión de n ensa-
yos independientes de Bernoulli, para los cuales la probabilidad de éxito es p en cada ensayo, siguen
una distribución binomial.
La distribución binomial proporciona la probabilidad de que un evento o acontecimiento tenga lugar
x veces en un conjunto de n ensayos, donde la probabilidad de éxito está dada por p.
𝑛
𝑓(𝑥)=( )𝑝𝑥𝑞𝑛−𝑥, 𝑥 =0,1,2,… 𝑞 =1−𝑝
𝑥
𝐸(𝑋)=𝑛𝑝 𝑉(𝑋)=𝑛𝑝𝑞
2
(𝐸(𝑋)−𝑉(𝑋)) (𝐸(𝑋))
𝑝= 𝑛=
𝐸(𝑋) (𝐸(𝑋)−𝑉(𝑋))
Los valores de variable aleatoria con distribución binomial se pueden generar con el método de re-
chazo. Genera n números aleatorios después de fijar x =0. Para cada número aleatorio r (1≤𝑖 ≤𝑛)
0 i
se efectúa una prueba y la variable x se incrementa según el siguiente criterio:
i
𝑥 =𝑥 +1, 𝑠𝑖 𝑟 ≤𝑝
𝑖 𝑖−1 𝑖
𝑥 =𝑥 , 𝑠𝑖 𝑟 >𝑝
𝑖 𝑖−1 𝑖
Después de haberse generado n números aleatorios, el valor de x será igual al valor de la varia-
n
ble aleatoria con distribución binomial.
Distribución hipergeométrica
Considere una población de N elementos tales que cada uno de ellos pertenece a la clase I o a la
II. Denotemos por Np al número de elementos que pertenecen a la clase I y por Nq al número de
elementos miembros de la clase II, donde p + q = 1. Si en una población de N elementos se toma una
muestra aleatoria de n elementos (n < N) sin que tenga lugar algún reemplazo, entonces el número
de elementos x de la clase I en la muestra de n elementos tendrá una distribución hipergeométrica.
(𝑁𝑝)(𝑁𝑞)
𝑓(𝑥) = 𝑥 𝑛−𝑥
(𝑁)
𝑛
Con 0≤𝑥 ≤𝑁𝑝 y 0≤𝑛−𝑥 ≤𝑁𝑞 y donde n, x y N son enteros.
𝑁−𝑛
𝐸(𝑋)=𝑛𝑝 𝑉(𝑋)=𝑛𝑝𝑞( )
𝑁−1
Para generar valores hipergeométricos, debemos alterar el método de ensayos de Bernoulli para
generar valores binomiales, con objeto que N y p varíen en forma dependiente respecto al número
total de elementos que previamente se han obtenido entre la población y el número de elementos de
la clase I que se han extraído. A medida que se extrae un elemento de una muestra de n elementos,
se reduce el valor de N=N : 𝑁 =𝑁 −1, con 𝑖 =0,1,2…,𝑛. De la misma forma, el valor de p=p se
0 𝑖 𝑖−1 0
transforma según
𝑁 𝑝 −𝑆
𝑖−1 𝑖−1
𝑝 = , 𝑖 =0,1,2,…,𝑛
𝑖 𝑁 −1
𝑖−1
Donde S=1 si el elemento de muestra i – 1 pertenece a la clase I y 0 de lo contrario
Distribución de Poisson
Si tomamos una serie de n ensayos independientes de Bernoulli, en cada uno de los cuales se
tenga una probabilidad p muy pequeña relativa a la ocurrencia de un cierto evento, a medida que n
tiende a infinito, la probabilidad de x ocurrencias está dada por la distribución de Poisson
𝜆𝑥
𝑓(𝑥)=𝑒−𝜆 , 𝜆 >0 𝑦 𝑥 =0,1,2,…
𝑥!
Siempre y cuando permitamos que p se aproxime a 0 de manera que se satisfaga la relación 𝜆 =
𝑛𝑝 constantemente.
Página 11 de 29

𝐸(𝑋)=𝑉(𝑋)=𝜆
Si
✓ El número total de eventos que ocurren durante un intervalo de tiempo dado es independiente
del número de eventos que ya han ocurrido
✓ La probabilidad de que un evento ocurra en el intervalo de t a t + Δt es aproximadamente 𝛼Δ𝑡
Entonces
✓ La función de densidad del intervalo t entre las ocurrencias de eventos consecutivos es
𝑓(𝑡)=𝜆𝑒−𝜆𝑡
✓ La probabilidad de que ocurran x eventos durante el tiempo t es 𝑓(𝑥)=𝑒−𝜆𝑡(𝜆𝑡)𝑥⁄𝑥!
Para simular una distribución de Poisson con parámetro 𝜆, el valor poissoniano x se determina ha-
ciendo uso de la desigualdad
𝑥 𝑥+1
∑𝑡 ≤𝜆 <∑𝑡 , 𝑥 =0,1,2,…
𝑖 𝑖
𝑖=0 𝑖=0
Donde los valores t se generan por medio de la fórmula 𝑡 =−log𝑟
i 𝑖 𝑖
Otra forma es ∏𝑥 𝑟 ≥𝑒−𝜆 >∏𝑥+1𝑟
𝑖=0 𝑖 𝑖=0 𝑖
Capítulo 1: Modelado de Simulación Básico (Law & Kelton)
La naturaleza de la simulación
Sistema: empresa o proceso de interés a modelizar.
Modelo: representación del sistema en términos de relaciones cuantitativas y lógicas.
Aplicaciones:
✓ Diseño y análisis de sistemas de fabricación.
✓ Evaluar requerimientos de hardware y software para un sistema informático.
✓ Evaluar nuevos sistemas de armas o tácticas militares.
✓ Determinar políticas de pedidos para un sistema de inventarios.
✓ Diseñar sistemas de comunicaciones y protocolos de mensajes para ellos.
✓ Diseñar y operar instalaciones de transporte.
✓ Evaluar diseños para organizaciones de servicios.
✓ Analizar sistemas financieros o económicos.
Sistemas, modelos y simulación
Un sistema se define como una colección de entidades que actúan e interactúan juntos hacia el
cumplimiento de un fin lógico. Definimos el estado de un sistema como una colección de variables
necesarias para describir un sistema en un momento determinado, relativos a los objetivos de estu-
dio.
Los sistemas se categorizan en dos tipos: discretos o continuos. Un sistema discreto es aquel en
el que las variables de estado cambian instantáneamente en puntos separados del tiempo. En un
sistema continuo en cambio las variables de estado cambian continuamente con respecto al tiempo.
Diferentes maneras en que un sistema puede ser estudiado:
✓ Experimentos con el sistema real vs. Experimentos con un modelo del sistema: si es posible
alterar el sistema físico y luego dejar que opere bajo las nuevas condiciones, es probable que
sea conveniente hacerlo, porque en este caso no hay duda acerca de si lo que estudiamos es
relevante. Sin embargo, rara vez es posible hacer esto. Por esto, es necesario construir un
modelo como una representación del modelo y estudiarlo como un sustituto del sistema real.
✓ Modelos físicos vs. Modelos matemáticos: los modelos físicos son construcciones en escala
reducida o simplificada del sistema real para estudiar en ellos su comportamiento. Los mode-
los matemáticos representan un sistema en términos de relaciones lógicas y cuantitativas que
son luego manipuladas y modificadas para ver como el sistema reacciona
✓ Solución analítica vs. Simulación: si las relaciones que componen el modelo son suficiente-
mente simples, puede ser posible utilizar métodos matemáticos para obtener información
exacta sobre cuestiones de interés, lo que se llama solución analítica. Muchos sistemas son
demasiados complejos para ser estudiados analíticamente, y deben ser estudiados por medio
de la simulación. En una simulación, usamos la computadora para evaluar un modelo numéri-
camente, y los datos se recogen con el fin de estimar las características del modelo.
Clasificación de los modelos de simulación:
Página 12 de 29

✓ Estáticos vs. Dinámicos: un modelo de simulación estático es una representación de un sis-
tema en un momento determinado, o uno que puede ser utilizado para representar un sistema
en el que el tiempo simplemente no juega ningún papel. Un modelo de simulación dinámica
representa un sistema a medida que evoluciona en el tiempo.
✓ Estocásticos vs. Determinísticos: Si un modelo de simulación no contiene componentes pro-
babilísticas (es decir aleatorias) se conoce como determinístico, en estos modelos la salida se
“determina” una vez que se especifica el conjunto de relaciones (ecuaciones) y los valores de
entrada. En cambio los modelos estocásticos contienen variables aleatorias de entrada suje-
tas a una distribución probabilística de algún tipo.
✓ Continuos vs. Discretos: definimos los modelos de simulación discreta y continua de manera
análoga a la forma en que los sistemas discretos y continuos se definieron anteriormente.
Simulación de Eventos Discretos:
La simulación de eventos discretos comprende el modelado de un sistema a medida que este evo-
luciona a través del tiempo por medio de una representación en la cual las variables de estado cam-
bian instantáneamente en puntos separados en el tiempo. Estos puntos en el tiempo son aquellos en
los cuales un evento ocurre, donde un evento se define como una ocurrencia instantánea que puede
cambiar el estado del sistema.
Mecanismo de Avance del Tiempo
Debido a la naturaleza dinámica de los modelos de simulación de eventos discretos, tenemos que
realizar un seguimiento del valor actual del tiempo simulado a medida que avanza la simulación, y
también necesitamos un mecanismo para avanzar el tiempo simulado de un valor a otro. Llamamos
reloj de la simulación a la variable de un modelo de simulación que contiene el valor actual del tiempo
simulado. La unidad del reloj nunca se enuncia explícitamente y se asume que está en las mismas
unidades que los parámetros de entrada.
Existen dos enfoques para el mecanismo de avance del tiempo:
✓ Avance del tiempo al siguiente evento: Con este enfoque el reloj de la simulación se inicia-
liza a cero y se determinan los tiempos de ocurrencia de eventos futuros, luego el reloj se
avanza al tiempo de ocurrencia del evento futuro más próximo, en este punto el estado del
sistema se actualiza para determinar que un evento ha ocurrido y los tiempos de futuros
eventos también se actualizan. Este proceso continua hasta que se cumple con una condición
de parada pre especificada.
✓ Avance del tiempo a incrementos fijos: La diferencia con el método anterior es que este
enfoque no saltea periodos de inactividad en el sistema, lo que supone una mayor cantidad
de cómputo.
Componentes y organización de un modelo de simulación de eventos discretos
✓ Estado del sistema: el conjunto de variables de estado necesarias para describir el sistema en
un momento dado.
✓ Reloj de simulación: una variable que indica el valor actual del tiempo simulado.
✓ Lista de eventos: una lista que contiene la próxima vez en el que cada tipo de evento ocurrirá.
✓ Contadores estadísticos: variables usadas para almacenar información estadística sobre el
rendimiento del sistema.
✓ Rutina de inicialización: un sub-programa que inicializa el modelo de simulación en el tiempo
cero.
✓ Rutina de tiempo: un sub-programa que determina el siguiente evento de la lista de eventos y
luego avanza el reloj de simulación al momento en que ocurre ese evento.
✓ Rutina de evento: un sub-programa que actualiza el estado del sistema cuando un tipo parti-
cular de evento ocurre (hay una rutina de evento por cada tipo de evento).
✓ Rutinas de biblioteca: un conjunto de sub-programas utilizados para generar observaciones
aleatorias a partir de distribuciones de probabilidad que fueron determinadas como parte del
modelo de simulación.
✓ Generador de informes: un sub-programa que calcula estimaciones de las medidas de rendi-
miento deseadas y elabora un informe cuando la simulación finaliza.
✓ Programa principal: un sub-programa que invoca la rutina de tiempo para determinar el si-
guiente evento y luego transfiere el control a la correspondiente rutina de evento para actuali-
zar el estado del sistema apropiadamente. También controla la terminación e invoca al gene-
rador de informes cuando la simulación acaba.
Simulación de un Sistema de Colas de un solo Servidor (M/M/1):
En un sistema de colas de un solo servidor, los tiempos entre arribos A , A ,…, A (de cada cliente
1 2 n
al sistema) son variables aleatorias IID (independientes e idénticamente distribuidas). Un cliente que
arriba y encuentra al servidor desocupado se atiende inmediatamente, y los tiempos de servicio S ,
1
Página 13 de 29

S ,…, S (de cada cliente) son también variables aleatorias IID independientes de los tiempos de arri-
2 n
bo. Si un cliente arriba y encuentra al servidor ocupado se une al final de cola. Al producirse una par-
tida (un cliente completa el servicio) el servidor elige un cliente de la cola según la disciplina FIFO. La
simulación comenzará sin clientes en el sistema y el servidor en estado desocupado. El sistema se
simula hasta que un número fijo (n) de clientes hayan completados sus demoras en cola, es decir
cuando el n-esimo cliente entre en servicio.
Medidas de Rendimiento: Para medir el rendimiento de este sistema observamos las estimaciones
de tres parámetros (más un parámetro opcional que es w(n)):
✓ Demora promedio esperada en cola de los n clientes. Llamada d(n).
✓ Número de clientes promedio esperado en la cola. Denotado por q(n).
✓ Utilización del servidor. Denominada u(n).
✓ Demora promedio esperada en el sistema de los n clientes. Llamada w(n).
Demora promedio esperada en cola de los “n-clientes”:
La demora promedio en una corrida determinada de la simulación es considerada propiamente
como una variable aleatoria en sí. Lo que queremos estimar, d(n), es el valor esperado para esta
variable aleatoria. d(n) es el promedio de una gran numero de demoras promedio de n clientes. A
partir de una sola corrida de la simulación podemos estimar este parámetro a través de:
∑𝑛 𝐷
𝑑̂(𝑛) = 𝑖=1 𝑖
𝑛
Esta fórmula es el promedio de las n demoras que fueron obtenidas durante la simulación.
Este estimador está basado en una muestra de tamaño 1 ya que estamos haciendo solamente
una sola corrida de la simulación. Un estimador de este tipo no tendrá demasiada precisión, pues el
sistema seguramente se encuentra en estado transitorio.
Es un ejemplo de una estadística de tiempo discreto.
Número de clientes promedio esperado en la cola:
Este promedio se toma sobre el periodo de tiempo necesarios para observar las n demoras que
definen nuestra regla de parada. Esta es una clase diferente de promedio que el anterior, ya que se
toma sobre el tiempo (continuo) en lugar de los clientes (discreto).
Definimos Q(t) como el número de clientes en cola en el momento t (para cualquier t ≥ 0) y T(n)
como el tiempo requerido para observar n demoras en cola. Para cualquier momento t entre 0 y T(n),
Q(t) es no negativo. Si llamamos p a la proporción esperada (entre 0 y 1) del tiempo en que Q(t) es
i
igual a i, una definición de q(n) seria:
∞
𝑞(𝑛) = ∑ 𝑖𝑝
𝑖
𝑖=0
Para estimar q(n) en una simulación, simplemente reemplazamos p con sus respectivas estima-
i
ciones y obtenemos:
∞
𝑞̂(𝑛) = ∑ 𝑖𝑝̂
𝑖
𝑖=0
Donde 𝑝̂ es la proporción observada del tiempo en que hubo i clientes en la cola (en la simula-
𝑖
ción).
Sin embargo una manera más sencilla de obtener 𝑞̂(𝑛) es mediante algunas consideraciones
geométricas. Si llamamos T al tiempo total durante la simulación en que la cola es de tamaño i, luego:
i
𝑇(𝑛) = ∑𝑛 𝑇 = 𝑇 +𝑇 +𝑇 +⋯+𝑇 y 𝑃 = 𝑇⁄𝑇(𝑛)
𝑖=0 𝑖 0 1 2 𝑛 𝑖 𝑖
Y el estimador puede escribirse como:
∑∞ 𝑖𝑇
𝑖=0 𝑖
𝑞̂(𝑛) =
𝑇(𝑛)
La sumatoria en el numerador de la ecuación anterior es solo el área bajo la curva de Q(t), que
puede escribirse como una integral de 0 hasta T(n), quedando finalmente la expresión:
𝑇(𝑛)
∫ 𝑄(𝑡)𝑑𝑡
𝑞̂(𝑛) = 0
𝑇(𝑛)
Es un ejemplo de una estadística de tiempo continuo.
Utilización esperada del servidor:
La utilización esperada del servidor es la proporción esperada de tiempo durante la simulación en
que el servidor está ocupado y por eso es un número entre 0 y 1. El estimador 𝑢̂(𝑛) es la proporción
Página 14 de 29

observada de tiempo durante la simulación en que el servidor está ocupado. Para esto definimos la
“función ocupado” B(t).
1 𝑠𝑖 𝑒𝑙 𝑠𝑒𝑟𝑣𝑖𝑑𝑜𝑟 𝑒𝑠𝑡á 𝑜𝑐𝑢𝑝𝑎𝑑𝑜 𝑒𝑛 𝑒𝑙 𝑡𝑖𝑒𝑚𝑝𝑜 𝑡
𝐵(𝑡)={
0 𝑠𝑖 𝑒𝑙 𝑠𝑒𝑟𝑣𝑖𝑑𝑜𝑟 𝑒𝑠𝑡á 𝑑𝑒𝑠𝑜𝑐𝑢𝑝𝑎𝑑𝑜 𝑒𝑛 𝑒𝑙 𝑡𝑖𝑒𝑚𝑝𝑜 𝑡
De esta manera 𝑢̂(𝑛) puede expresarse como la proporción de tiempo en que B(t) es igual a 1.
𝑇(𝑛)
∫ 𝐵(𝑡)𝑑𝑡
𝑢̂(𝑛) = 0
𝑇(𝑛)
El numerador puede ser visto como el área bajo la función B(t) durante el curso de la simulación.
𝑢̂(𝑛) es el promedio continuo de la función B(t). La integral de B(t) puede fácilmente ser acumula-
da por la suma de las áreas de los rectángulos. Las estadísticas de uso son muy informativos en la
identificación de cuellos de botella o exceso de capacidad.
Es un ejemplo de una estadística de tiempo continuo.
Demora o Tiempo de espera promedio esperado en el sistema (cola + servidor):
Esta medida se define como el intervalo de tiempo desde el instante que un cliente arriba a la cola
hasta el instante en que el cliente completa el servicio y parte.
El estimador usual de w(n) seria:
∑𝑛 𝐷 ∑𝑛 𝑆
𝑤̂(𝑛) = 𝑖=1 𝑖 + 𝑖=1 𝑖 = 𝑑̂(𝑛)+𝑆̅(𝑛)
𝑛 𝑛
Donde Si es el tiempo de espera de los n clientes en el servidor y 𝑆̅(𝑛) es el promedio de los n
tiempos de servicio de los clientes. Ya que el tiempo de servicio medio o esperado E(S) es conocido
un estimador alternativo seria 𝑤̃(𝑛)=𝑑̂(𝑛)+𝐸(𝑆)
En casi todas las simulaciones de colas 𝑤̃(𝑛) será mejor que 𝑤̂(𝑛). Ambos son estimadores no
sesgados.
Eventos y variables de estado: Los eventos de este sistema son el arribo de un cliente y la partida
de un cliente. Las variables de estado necesarias para estimar d(n), q(n) y u(n) son el estado del ser-
vidor, el número de clientes en cola, el tiempo de arribo de cada cliente en cola y el tiempo del ultimo
evento.
Observaciones:
✓ El elemento clave in la dinámica de una simulación es la interacción entre el reloj de la simu-
lación y la lista de eventos.
✓ Mientras se procesa un evento, no transcurre el tiempo de simulación.
✓ A veces es fácil pasar por alto las contingencias que parecen fuera de lo común, pero que sin
embargo hay que tener en cuenta.
✓ En algunas simulaciones puede suceder que 2 o más entradas en la lista de eventos empatan
en menor, y deba incorporarse una regla de decisión para romper empates, que afectará el
resultado de la simulación.
Reglas de interrupción alternativas
La simulación puede terminar:
✓ Cuando el número de clientes atendidos llega a una determinada cantidad fija. El valor final
del reloj de la simulación es una variable aleatoria.
✓ Cuando el reloj llega a una cantidad fija de tiempo. El número de clientes atendidos es una
variable aleatoria.
Determinando los eventos y variables
En el método de eventos gráficos, los eventos propuestos, cada uno representado por un nodo,
están conectados por arcos dirigidos que representan cómo los eventos se pueden programar de
otros eventos y de ellos mismos. Los eventos gráficos conectan el conjunto propuesto de eventos por
los arcos que indican el tipo de programación de eventos que pueden ocurrir. Las flechas lisas grue-
sas indican que un evento al final de la flecha se puede programar desde el evento en el comienzo de
la flecha en una cantidad no nula de tiempo, y la flecha dentada delgada indica que el evento en su
extremo está programado inicialmente.
Uno de los usos de los gráficos de eventos es simplificar la estructura de eventos de una simula-
ción mediante la eliminación de eventos innecesarios. Hay varias reglas que permiten la simplifica-
ción, y una de ellas es que si un nodo de evento tiene arcos entrantes que son todos delgados y lisos,
este evento puede ser eliminado del modelo y su acción integrada en los eventos que se programan
en tiempo cero.
Página 15 de 29

Otra regla tiene que ver con la inicialización. El gráfico de eventos se descompone en componen-
tes fuertemente conectados, dentro de cada uno de los cuales es posible viajar desde cada nodo a
todos los demás nodos siguiendo los arcos en sus direcciones indicadas. La regla de inicialización
establece que en cualquier componente fuertemente conectado de nodos que no tenga arcos entran-
tes de otros nodos de eventos fuera del componente, debe haber al menos un nodo que se programa
inicialmente.
Simulación distribuida
En los últimos años la tecnología informática ha permitido que las computadoras o procesadores
individuales se asocien entre sí en entornos de computación paralela o distribuida. En estos tipos de
entornos, puede ser posible distribuir diferentes partes de una tarea computacional a través de proce-
sadores individuales que operan al mismo tiempo y por lo tanto reducir el tiempo total para completar
la tarea.
Hay muchas formas posibles de dividir una simulación dinámica para distribuir su trabajo sobre di-
ferentes procesadores:
✓ Asignar las distintas funciones de apoyo a diferentes procesadores. La lógica de ejecución de
la simulación sigue siendo secuencial, pero el programa principal de la simulación puede de-
legar la ejecución de las funciones de soporte a otros procesadores y seguir adelante con su
trabajo.
✓ Descomponer el modelo en distintos sub-modelos, que luego son asignados a diferentes pro-
cesadores para la ejecución. Los procesadores deben comunicarse entre sí siempre que sea
necesario para mantener las relaciones lógicas correctas entre los sub-modelos.
Pasos en un estudio de simulación
1. Formular el problema y planificar el estudio: todo estudio debe comenzar con una declaración
clara de los objetivos generales del estudio y las cuestiones específicas que se abordarán.
2. Recolectar datos y definir un modelo: información y datos deben recolectarse del sistema de
interés y utilizarse para especificar los procedimientos operativos y distribuciones de probabi-
lidad de las variables aleatorias utilizadas en el modelo.
3. Validar: en la construcción del modelo, es imperativo para los modeladores involucrar en el
estudio a las personas que están íntimamente familiarizadas con las operaciones del sistema
real.
4. Construir un programa de computación y verificar: el modelador de la simulación debe decidir
si se debe programar el modelo en un lenguaje de propósito general o en un lenguaje de si-
mulación de diseño especial.
5. Hacer corridas piloto: se hacen pruebas piloto del modelo verificado.
6. Validar: las pruebas piloto pueden usarse para probar la sensibilidad de las salidas del mode-
lo a pequeños cambios en un parámetro de entrada.
7. Diseñar experimentos: hay que decidir qué diseño de sistema simular si hay más de una al-
ternativa que pueda razonablemente simularse.
8. Hacer corridas de producción: se hacen corridas de producción para proporcionar datos de
rendimiento sobre los diseños de los sistemas de interés.
9. Analizar los datos de salida: se usan técnicas estadísticas para analizar los datos de salida de
las corridas.
10. Documentar presentar e implementar los resultados: es importante documentar los supuestos
que entraron en el modelo, así como el propio programa informático.
Otros tipos de simulación
✓ Simulación continua: se refiere a la modelización a lo largo del tiempo de un sistema por una
representación en la que las variables de estado cambian continuamente con respecto al
tiempo. Involucra ecuaciones diferenciales que dan las relaciones de las tasas de variación de
las variables de estado con el tiempo.
✓ Simulación combinada discreta-continua: puesto que algunos sistemas no son ni completa-
mente discretos ni completamente continuo, puede surgir la necesidad de construir un modelo
con aspectos tanto de simulación de eventos discretos y continuos.
✓ Simulación de Monte Carlo: es un esquema de empleo de números aleatorios que se utiliza
para solucionar determinados problemas estocásticos o deterministas en donde el paso del
tiempo no juega ningún papel sustantivo.
Página 16 de 29

Ventajas, desventajas y dificultades de la simulación
Ventajas:
✓ Muchos sistemas complejos no pueden describirse con precisión mediante un modelo mate-
mático que puede evaluarse analíticamente. Por lo tanto, una simulación es a menudo el úni-
co tipo de investigación posible.
✓ Permite estimar el rendimiento de un sistema existente bajo un conjunto de condiciones de
operación proyectados.
✓ Diseños alternativos del sistema propuesto se pueden comparar a través de la simulación pa-
ra poder ver los que mejor se adaptan a los requerimientos especificados.
✓ En una simulación podemos mantener mejor control sobre las condiciones experimentales de
lo que generalmente sería posible cuando experimentamos con el propio sistema.
✓ Permite estudiar un sistema con un horizonte temporal largo en tiempo comprimido, o bien es-
tudiar los pormenores del funcionamiento de un sistema en tiempo expandido.
Desventajas:
✓ Cada corrida de un modelo de simulación estocástico produce solo estimaciones de las ver-
daderas características del modelo para un conjunto particular de parámetros de entrada.
✓ Los modelos de simulación suelen ser costosos y requieren mucho tiempo para desarrollar-
los.
✓ El gran volumen de números producidos por un estudio de simulación o el impacto persuasivo
de una animación realista crea a menudo una tendencia a poner mayor confianza en los re-
sultados de un estudio que la que se justifica.
Capítulo 9: Modelo Analítico para una cola M/M/1 (Mc Millan - Gon-
zalez).
Tipos de sistemas de colas:
Un sistema de colas se distingue de otro por cierto número de atributos. Los principales son:
1. El número de fases:
a. Fase simple: no hay colas secuenciales.
b. Multifásico: varias colas secuenciales.
2. El número de canales:
a. Canal simple: no hay servidores paralelos.
b. Canal múltiple: varios servidores paralelos
3. La disciplina de las colas.
La disciplina de las colas se refiere al hecho de si los clientes se acomodan de acuerdo con una
norma de servicio por orden de llegada (FIFO, LIFO, etc.) o se aplica alguna otra regla de prioridad
especial.
Por conducta de un sistema de colas se entiende el modo en que los clientes que llegan interac-
túan con sus instalaciones de servicio.
Entendemos por clientes a entidades cuyas llegadas ejercen demandas sobre alguna instalación
(servidor).
Interacciones de colas
El fenómeno de las colas es el resultado de la interacción de las llegadas aleatorias y el tiempo
aleatorio de servicio. El patrón de llegadas depende de:
a. El tamaño del universo de clientes posibles (que “genera” clientes que necesitan atención).
b. El nivel de sus actividades, que hace que necesiten servicios de vez en cuando.
Caso M/M/1:
Sistema monofásico de canal simple. En este caso se supone que el tiempo entre llegadas tiene
una distribución exponencialmente negativa y que el tiempo de servicio tiene el mismo tipo de distri-
bución. Puesto que la misma es un producto del proceso de Poisson, nuestro sistema de colas será
totalmente de Poisson.
La instalación de servicio podrá acomodar sólo a un cliente a la vez y que las llegadas se atienden
de acuerdo al orden de llegada. Nos interesa desarrollar un modelo para predecir (analíticamente):
1. La probabilidad de varios números de clientes en la cola. (También llamado número de clien-
tes promedio esperado en la cola q(n) en Law-Kelton).
2. El tiempo esperado o promedio que pasara un cliente en las instalaciones de servicio.
3. La probabilidad de que las instalaciones de servicio estén ociosas. (También llamado factor
de utilización del servidor [1-u(n)] en Law-Kelton).
Página 17 de 29

Para empezar suponemos que nuestro sistema puede dar atender (dar servicio) a μ clientes por
unidad de tiempo (en promedio). De esta manera μ también es el número esperado de salidas (parti-
das) del sistema durante cada unidad de tiempo. Llamamos al promedio de llegadas por unidad de
tiempo λ.
A continuación consideramos que t es un momento en el tiempo y que 𝑝 (𝑡) es la probabilidad de
𝑛
que haya n clientes en el sistema en el momento t. Si a su vez consideramos una porción de tiempo
después de t denominada (𝑡+ ∆𝑡) podríamos pensar que Δt es tan pequeño que aun cuando exista
una llegada o una partida durante el intervalo Δt, es imposible más de una llegada o salida durante
ese intervalo (modelo de Poisson). Para enfrentarnos a este problema nos preguntamos cual es la
probabilidad de que haya n clientes en el sistema en el intervalo (𝑡+ ∆𝑡), o sea 𝑝 (𝑡+∆𝑡). Ahora
𝑛
bien, n clientes en el sistema durante ese intervalo puede presentarse de cuatro modos distintos:
Modo 1:
Tener n clientes en el sistema en el tiempo t, cero llegadas y cero salidas durante el intervalo Δt.
Esto se puede obtener a partir del siguiente razonamiento:
| La probabilidad de 1 llegada es: 𝑝 |     | =𝜆∆𝑡  |     |     |
| ---------------------------------- | --- | ----- | --- | --- |
1
| La probabilidad de 0 llegada es: 𝑝 |     | =1−𝑝  | =(1−𝜆∆𝑡)  |     |
| ---------------------------------- | --- | ----- | --------- | --- |
|                                    |     | 0     | 1         |     |
| La probabilidad de 1 partida es: 𝑝 |     | =𝜇∆𝑡  |           |     |
1
| La probabilidad de 0 partida es: 𝑝          |     | =1−𝑝 | =(1−𝜇∆𝑡)            |     |
| ------------------------------------------- | --- | ---- | ------------------- | --- |
|                                             |     | 0    | 1                   |     |
| Entonces la probabilidad del modo uno es: 𝑝 |     |      | (𝑡)=(1−𝜆∆𝑡)(1−𝜇∆𝑡)  |     |
𝑛
Modo 2:
Tener n - 1 clientes en el sistema en el tiempo t, una llegada y cero salidas durante el intervalo Δt.
| Probabilidad del modo dos: 𝑝 |     | (𝑡)=(𝜆∆𝑡)(1−𝜇∆𝑡)  |     |     |
| ---------------------------- | --- | ----------------- | --- | --- |
𝑛−1
Modo 3:
Tener n + 1 clientes en el sistema en el tiempo t, cero llegadas y una salida durante el intervalo Δt.
| Probabilidad del modo tres: 𝑝 |     | (𝑡)=(1−𝜆∆𝑡)(𝜇∆𝑡)  |     |     |
| ----------------------------- | --- | ----------------- | --- | --- |
𝑛+1
Modo 4:
Tener n clientes en el sistema en el tiempo t, una llegada y una salida durante el intervalo Δt.
| Probabilidad del modo cuatro: 𝑝 |     | (𝑡)=(𝜆∆𝑡)(𝜇∆𝑡)  |     |     |
| ------------------------------- | --- | --------------- | --- | --- |
𝑛
La probabilidad total de tener n clientes en el sistema en el momento t + Δt es la suma de las pro-
babilidades de los cuatro modos anteriores, quedando la expresión como:
𝑝 (𝑡+∆𝑡)=𝑝 (𝑡)(1−𝜆∆𝑡)(1−𝜇∆𝑡)+𝑝 (𝑡)(𝜆∆𝑡)(1−𝜇∆𝑡)+𝑝 (𝑡)(1−𝜆∆𝑡)(𝜇∆𝑡)
| 𝑛   | 𝑛   |     | 𝑛−1 | 𝑛+1 |
| --- | --- | --- | --- | --- |
(𝑡)(𝜆∆𝑡)(𝜇∆𝑡)
+𝑝 𝑛
Luego de trabajar esta expresión se llega a
|     | 𝑝 (𝑡+∆𝑡)−𝑝 | (𝑡)  |              |             |
| --- | ---------- | ---- | ------------ | ----------- |
|     | 𝑛          | 𝑛 =𝑝 | (𝑡)(−𝜆−𝜇)+𝜆𝑝 | (𝑡)+𝜇𝑝 (𝑡)  |
|     |            |      | 𝑛            | 𝑛−1 𝑛+1     |
∆𝑡
Si hacemos que en el límite de la expresión anterior Δt tienda a 0, la misma se transforma en una
ecuación diferencial:
|     | 𝑑𝑝  | (𝑡)      |               |      |
| --- | --- | -------- | ------------- | ---- |
|     | 𝑛   | =−(𝜆+𝜇)𝑝 | (𝑡)+𝜆𝑝 (𝑡)+𝜇𝑝 | (𝑡)  |
|     |     |          | 𝑛 𝑛−1         | 𝑛+1  |
𝑑𝑡
La expresión anterior hace referencia a un sistema de infinitas ecuaciones diferenciales con n+1
ecuaciones y n + 1 incógnitas, llamado cadena de Markov, en la cual la probabilidad de que un evento
pueda ocurrir depende del evento anterior. El caso anterior se aplica a n ≥ 1 si hacemos el caso es-
pecial en que n = 0, entonces 𝑝 (𝑡)=0, y la expresión se transforma en:
𝑛−1
𝑑𝑝 (𝑡)
|     |     | 0 =−𝜆𝑝 | (𝑡)−𝜇𝑝 (𝑡)+𝜇𝑝 | (𝑡)  |
| --- | --- | ------ | ------------- | ---- |
|     |     |        | 0 0           | 1    |
𝑑𝑡
Dado a que cuando n = 0 el sistema está vacío y no se producen salidas, el segundo término se
desecha y finalmente:
𝑑𝑝 (𝑡)
|     |     | 0   | (𝑡)+𝜇𝑝   |      |
| --- | --- | --- | -------- | ---- |
|     |     |     | =−𝜆𝑝 0 1 | (𝑡)  |
𝑑𝑡
Dado que la derivada es una función del tiempo, las probabilidades de que haya distintos números
de clientes en el sistema cambian con el tiempo.
Mientras el sistema se está asentando para llegar a una condición estable decimos que se en-
cuentra en estado transitorio, una vez alcanzado su condición estable se encuentra en estado esta-
cionario.
Página 18 de 29

Si nos interesamos exclusivamente por el estado estacionario, la derivada de la probabilidad de
𝑑𝑝𝑛(𝑡)
que haya varios números de clientes en el sistema sea cero, o sea   =0, se convierte en
𝑑𝑡
|     |     |     | (𝜆+𝜇)𝑝 | =𝜆𝑝    | +𝜇𝑝     |
| --- | --- | --- | ------ | ------ | ------- |
|     |     |     |        | 𝑛      | 𝑛−1 𝑛+1 |
|     |     |     |        | 𝜆𝑝 =𝜇𝑝 |         |
0 1
𝜆
| A partir de estas ecuaciones resulta evidente que: 𝑝 |     |     |     |     | = 𝑝   |
| ---------------------------------------------------- | --- | --- | --- | --- | ----- |
|                                                      |     |     |     |     | 1 𝜇 0 |
Para n = 1 tenemos:
|     |     |     | (𝜆+𝜇)𝑝 | =𝜆𝑝     | +𝜇𝑝   |
| --- | --- | --- | ------ | ------- | ----- |
|     |     |     |        | 1       | 0 2   |
|     |     |     | 0=𝜆𝑝   | −(𝜆+𝜇)𝑝 | +𝜇𝑝   |
|     |     |     |        | 0       | 1 2   |
𝜆 𝜆+𝜇
|     |     |     | 𝑝 =− | 𝑝 +   | 𝑝       |
| --- | --- | --- | ---- | ----- | ------- |
|     |     |     | 2    | 𝜇 0   | 𝜇 1     |
|     |     |     |      | 𝜆 𝜆+𝜇 | 𝜆       |
|     |     |     | 𝑝 =− | 𝑝 +(  | )( 𝑝 )  |
|     |     |     | 2    | 𝜇 0   | 𝜇 𝜇 0   |
2
|     |     |     |      | 𝜆    | 𝜆 𝜆       |
| --- | --- | --- | ---- | ---- | --------- |
|     |     |     | 𝑝 =− | 𝑝 +( | ) 𝑝 + 𝑝   |
|     |     |     | 2    | 0    | 0 0       |
|     |     |     |      | 𝜇    | 𝜇 𝜇       |
𝜆 2
|     |     |     |     | 𝑝 2 =( | ) 𝑝 0   |
| --- | --- | --- | --- | ------ | ------- |
𝜇
Para n = 2 siguiendo los mismos pasos obtenemos:
𝜆 3
|     |     |     |     | 𝑝 =( | ) 𝑝   |
| --- | --- | --- | --- | ---- | ----- |
|     |     |     |     | 3 𝜇  | 0     |
Por ende para el n-esimo término la probabilidad de que haya n elementos en el sistema resulta:
𝜆 𝑛
|     |     |     |     | 𝑝 =( | ) 𝑝   |
| --- | --- | --- | --- | ---- | ----- |
|     |     |     |     | 𝑛 𝜇  | 0     |
Ahora bien si queremos determinar 𝑝 0  tenemos que: 𝑝 0 +𝑝 1 +𝑝 2 +⋯+𝑝 𝑛 =1
|             |         | 2             | 𝑛   |     |     |
| ----------- | ------- | ------------- | --- | --- | --- |
|             | 𝜆       | 𝜆             | 𝜆   | =1  |     |
| Por ende: 𝑝 | 0 + 𝑝 0 | +( ) 𝑝 0 +⋯+( | ) 𝑝 | 0   |     |
|             | 𝜇       | 𝜇             | 𝜇   |     |     |
1
𝑝 0 =
|     |     |     |     | 𝜆 𝜆  | 2 𝜆 𝑛  |
| --- | --- | --- | --- | ---- | ------ |
|     |     |     | 1+  | +( ) | +⋯+( ) |
|     |     |     |     | 𝜇 𝜇  | 𝜇      |
El denominador de la expresión anterior es una serie geométrica donde a = 1 y r = λ/μ, y para to-
𝑎

dos los valores de r < 1 la serie converge y su suma es
1−𝑟
|               |     | 1   | 𝜆   |     |     |
| ------------- | --- | --- | --- | --- | --- |
| Finalmente: 𝑝 | =   | =1− | ⁄𝜇  |     |     |
0 1⁄[1−(𝜆⁄𝜇)]
|                                      |     |     |           |      | 𝜆 𝜆 𝑛  |
| ------------------------------------ | --- | --- | --------- | ---- | ------ |
| Por lo tanto la expresión final de p |     |     |  seria: 𝑝 | =(1− | )( )   |
|                                      |     |     | n         | 𝑛    | 𝜇 𝜇    |
Este es un modelo general para determinar la probabili-
dad de que haya n clientes en el sistema de colas de canal
simple, en el estado estacionario, donde el ritmo de llegadas
(λ) es menor que el índice medio de servicio (μ). Sin embar-
go nuestro modelo está limitado al hecho de que λ/μ < 1
(esto es una condición para que exista la solución estaciona-
ria). Desde el punto de vista lógico resulta obvia esa condi-
ción ya que si λ/μ ≥ 1 entonces el índice de llegadas siempre
será más alto que la capacidad del servidor de atender esas
llegadas, con lo cual la cantidad de gente en cola se haría
cada vez más grande a medida que pasa el tiempo y la pro-
babilidad de que haya n elementos en el sistema tendería
hacia el infinito a medida que n aumenta.

Fig. 1. El estado más probable es que haya 0 clientes en cola si λ/μ < 1.
Medidas de rendimiento:
A partir del análisis se pueden obtener las siguientes medidas de rendimiento:
Porcentaje de tiempo y ocioso y porcentaje de utilización
𝜆
El porcentaje de tiempo ocioso es la probabilidad de 0 clientes en el sistema 𝑝 =1− ⁄𝜇
0
Página 19 de 29

𝜆
La utilización fraccionaria de la capacidad total de la instalación de servicio es 1−𝑝
0
= ⁄𝜇
Número de elementos esperado en el sistema
Esto es la probabilidad de 1 en el sistema por 1, más la probabilidad de 2 por 2, más la de 3 por 3,
y así sucesivamente. Esto resulta una serie infinita de la forma 𝑎𝑟+2𝑎𝑟2+3𝑎𝑟3+⋯+𝑛𝑎𝑟𝑛, donde
𝑟
𝑎 =1−𝜆⁄𝜇 y 𝑟 =𝜆⁄𝜇. La suma de la serie es 𝑎× , por lo tanto
(1−𝑟)2
𝜆 𝜆⁄𝜇 𝜆
(1− )[ ]=
𝜇 (1−𝜆⁄𝜇)2 𝜇−𝜆
Número de elementos esperado en la cola
El número esperado en la cola es el número esperado en el sistema menos el número esperado
en la instalación de servicio.
El número esperado en el punto de servicio es igual al número en el punto de servicio cuando esté
ocupado por la probabilidad de que esté ocupado más el número en la instalación de servicio cuando
esté ociosa por la probabilidad de que este ociosa. Esto es 1×𝜆⁄𝜇+0×(1−𝜆⁄𝜇)=𝜆⁄𝜇.
Por lo tanto, el número esperado en cola es
𝜆 𝜆 𝜆2
− =
𝜇−𝜆 𝜇 𝜇(𝜇−𝜆)
Tiempo esperado en el sistema
El número esperado en el sistema es 𝜆, por el tiempo esperado en el sistema. Entonces el tiempo
esperado en el sistema es el número esperado en el sistema dividido entre 𝜆
𝜆
𝜇−𝜆 1
=
𝜆 𝜇−𝜆
Tiempo promedio de espera
Es el tiempo total esperado en el sistema menos el tiempo esperado en el punto de servicio
1 1 𝜆
− =
𝜇−𝜆 𝜇 𝜇(𝜇−𝜆)
Probabilidad de N en la cola
La probabilidad de n en cola es simplemente la probabilidad de n + 1 en el sistema (esto solo apli-
ca cuando n > 0, la probabilidad de 0 en la cola es la de 0 en el sistema más la de 1 en el sistema).
Con un 𝜇 fijo y 𝜆 variando de 0 a 𝜇, vemos que hay una probabilidad variable de encontrar 1, 2,
3,… en el sistema. Se llega a un punto máximo a medida que aumenta y luego comienza a disminuir.
El tiempo que se puede esperar que el sistema permanezca ocioso es una línea recta, de 1 para
𝜆 =0 y que llega a ser muy pequeña cuando 𝜆 se acerca a 𝜇.
En cualquier punto, ∑ 𝑝 =1.
𝑖 𝑖
Si los clientes llegan a un ritmo cercano al índice que se les puede atender, el tiempo en el siste-
ma será muy grande. Si 𝜆 es pequeño en comparación con 𝜇, un aumento de la capacidad de servicio
dará una ligera disminución del tiempo en el sistema.
Modos de mejorar el servicio:
✓ Aumento del número de canales.
✓ Reunión de instalaciones.
Probabilidad de N en función del tiempo
El estado estacionario es una condición que se supone que prevalece después de que el sistema
ha tenido tiempo de asentarse y acercarse a su estado esperado. Excepto en el estado estacionario,
P es una función del tiempo, lo mismo que 𝜆 y 𝜇.
n
Probabilidad de una llegada en función de la longitud de la cola
En el modelo, se supone que la población de clientes potenciales es infinita. Cuando la población
de clientes potenciales sea pequeña, la probabilidad de una llegada en el siguiente período es función
de la longitud de la cola, además de serlo de 𝜆 y 𝜇.
El estado transitorio y la truncación
En teoría, cuando 𝜆 >𝜇 el sistema tendría solamente un estado transitorio. En la práctica, confor-
me la línea de espera y el tiempo necesario crecen, los clientes se impacientan y no esperan; o bien
no se deja que la cola crezca más allá de un cierto límite. De este modo, estos sistemas se ven trun-
Página 20 de 29

cados en alguna longitud de cola y se descubre que, incluso para 𝜆 >𝜇, los sistemas de cola pueden
tener un estado estacionario.
Capítulo 15: Verificación de los resultados de simulación (Gordon)
Naturaleza del problema
Por lo general se planea un estudio de simulación como una serie de corridas cuyo objetivo es
comparar una diversidad de sistemas alternos o condiciones de operación.
Experimento: prueba de un sistema determinado que opere bajo un conjunto de condiciones.
Corrida: una sola ejecución de una configuración experimental.
Observación: una sola medición de una variable del sistema.
Un experimento es la colección de todas las corridas con una configuración de sistemas y el estu-
dio es la configuración de todos los experimentos.
Problemas estadísticos asociados con un estudio de simulación:
✓ Problemas de planificación estratégica: referido al diseño de un conjunto de experimentos. La
planificación estratégica debe determinar las medidas según las cuales se juzga el sistema y
cómo probar la significancia en las diferencias en estas medidas.
✓ Problemas de planificación táctica: referido a especificar la manera en que debe de realizarse
cada experimento. La planificación táctica debe decidir cómo tomar las medidas de cada co-
rrida y cuántas corridas deben hacerse para cada experimento.
Métodos de estimación
Si se hacen n observaciones independientes de la variable, la media de la muestra 𝑥̅ = 1 ∑𝑛 𝑥
𝑛 𝑖=1 𝑖
también es una variable aleatoria. Según el teorema central del límite, x tiende a una distribución
normal con media 𝜇 y variancia 𝜎2⁄𝑛. Se sigue que
𝑥̅−𝜇
𝑧=
𝜎⁄√𝑛
Tiene distribución aproximadamente normal con media 0 y variancia 1. La integral de −∞ a un va-
lor u es la probabilidad de que z sea menor o igual a u. Suponga que se elige un valor u tal que
Φ(𝑢)=1−𝛼⁄2 (𝑢 =𝑢 ). Entonces 𝑃(𝑧>𝑢 )=𝛼⁄2=𝑃(𝑧<−𝑢 ), por simetría de la distribu-
𝛼⁄2 𝛼⁄2 𝛼⁄2
ción normal respecto de la media. Por lo tanto
𝑃(−𝑢 ≤𝑧≤𝑢 )=1−𝛼
𝛼⁄2 𝛼⁄2
𝜎 𝜎
𝑃(𝑥̅− 𝑢 ≤𝜇 ≤𝑥̅+ 𝑢 )=1−𝛼
𝛼⁄2 𝛼⁄2
√𝑛 √𝑛
𝜎
1−𝛼 es el nivel de confianza y el intervalo 𝑥̅± 𝑢 es el intervalo de confianza.
√𝑛
𝛼⁄2
En la práctica no se conoce 𝜎2, en cuyo caso se reemplaza por una estimada
𝑛
1
𝑠2 = ∑(𝑥 −𝑥̅)2
𝑛−1 𝑖
𝑖=1
La variable z ya no está distribuida en forma normal, sino que tiene una distribución t de Student.
La cantidad 𝑢 debe deducirse integrando la distribución. La desviación entre estas distribuciones
𝛼⁄2
disminuye al aumentar n, y para un n suficientemente grande (≥30) se puede utilizar la distribución
𝑠
normal. El intervalo de confianza para 𝜇 es 𝑥̅± 𝑢 .
√𝑛
𝛼⁄2
Estadísticas de corridas de simulación
El método de determinar un intervalo de confianza supone que:
✓ La distribución de la cual se obtienen las observaciones es estacionaria.
✓ Las observaciones son independientes.
La media de la muestra 𝑥̅(𝑛) depende de la cantidad de observaciones que se toman.
Los tiempos de espera no son independientes, ya que el tiempo de espera de cada entidad de-
pende de los tiempos de espera de sus predecesores. Se dice que esta auto-correlacionada. La auto-
correlación aumenta conforme aumenta la utilización del servidor. La media de la muestra de datos
auto-correlacionados se aproxima a una distribución normal conforme aumenta el tamaño de la mues-
tra. La fórmula 𝑥̅ = 1 ∑𝑛 𝑥 para estimar el valor medio de la distribución es válida, pero la variancia
𝑛 𝑖=1 𝑖
de los datos auto-correlacionados no está relacionada con la de la población por 𝜎⁄√𝑛. Es necesario
agregar un término para tomar en cuenta la correlación.
Página 21 de 29

Al iniciar una corrida de simulación con el sistema en algún estado inicial (con frecuencia el de
ocio), las primeras llegadas tienen una probabilidad mayor de obtener rápidamente el servicio, de
manera que estará sesgada una media de muestra que incluya las primeras llegadas. El efecto de
sesgo disminuye al extender la longitud de la corrida de simulación y aumentar el tamaño de la mues-
tra.
Repetición de corridas
Al repetir el experimento con distintos números aleatorios para el mismo tamaño n de la muestra
se obtiene un conjunto de determinaciones independientes de la media 𝑥̅(𝑛) de la muestra, que pue-
den utilizarse para estimar la variancia de la distribución. Suponga que el experimento se repite p
veces con series de números aleatorios independientes. Sea x la i-esima observación de la j-esima
ij
corrida, y sea 𝑥̅ (𝑛) la media de la muestra para la j-esima corrida, entonces
𝑗
𝑝 𝑝 𝑛 𝑝
1 1 1
𝑥̿(𝑛)=𝑚(𝑛)= ∑𝑥̅ (𝑛)= ∑∑𝑥 𝑠2(𝑛)= ∑[𝑥̅ (𝑛)−𝑚(𝑛)] 2
𝑝 𝑗 𝑛𝑝 𝑖𝑗 𝑝−1 𝑗
𝑗=1 𝑗=1𝑖=1 𝑗=1
Se pueden utilizar las estimaciones para establecer un intervalo de confianza. La media en que se
basa el intervalo de confianza depende de 1⁄𝑛𝑝. En ausencia de sesgo inicial, el mismo aumento en
n o p tiene efectos equivalentes en el tamaño del intervalo de confianza. Para aumentar la probabili-
dad de reducir el sesgo inicial, es preferible extender las corridas manteniendo el número de repeti-
ciones a un nivel en que el tamaño de la muestra es suficientemente grande para justificar la aproxi-
mación a la distribución normal.
Eliminación del sesgo inicial
Se pueden seguir 2 enfoques:
✓ Iniciar cada sistema en una condición inicial más representativa: en algunos sistemas, se
puede disponer de información sobre las condiciones esperadas, lo que permite elegir mejo-
res condiciones iniciales. Debe utilizarse un rango de valores que permita escoger un estado
inicial distinto para cada repetición.
✓ Ignorar la primera parte de cada corrida de simulación: es el enfoque más común. La corrida
se inicia a partir de un estado de ocio y se detiene después de un determinado período. Se
dejan como están las entidades que existen en el sistema en ese momento y se reinicia la co-
rrida recabando estadísticas desde el punto de reinicio. No hay reglas simples para decidir el
largo del intervalo eliminado. Se aconseja usar pruebas piloto.
Medias de lotes
Otro enfoque para estimar la precisión de los resultados utiliza una sola corrida larga, preferente-
mente quitando el sesgo inicial. La corrida se divide en segmentos para separar las mediciones en
lotes de igual tamaño. Se toma la media de cada lote y se las considera como observaciones inde-
pendientes. El valor estimado de la variable que se está midiendo es la media de las medias de los
lotes, que es igual a la media de todas las mediciones. Al suponer que las medias de los lotes son
independientes, se considera a las observaciones de las medias de los lotes como distribuidos nor-
malmente (por teorema central del límite) y se pueden aplicar las fórmulas para estimar la variancia
de la media y calcular un intervalo de confianza.
No se puede aplicar el método a una estadística acumulada, debido a que la distribución de la
media de la muestra depende de la longitud de la corrida.
Una corrida completa consiste en N observaciones que se descomponen en p lotes de tamaño n.
Esto equivale a repetir un experimento de longitud n un total de p veces, en que el estado final de una
corrida es el inicial de la siguiente. Este es un estado inicial más razonable que el de ocio, pero intro-
duce correlación. Se puede separar los lotes en intervalos en que se descartan las mediciones para
eliminar la correlación.
Análisis de series de tiempo
Un enfoque para estimar la precisión de los resultados es estimar la variancia de una media de
muestra, a partir de resultados obtenidos en el estudio de series de tiempo. El experimento se realiza
como una sola corrida quitando el sesgo inicial. Se conservan las observaciones individuales y se
tratan como los datos de una serie de tiempo. Suponga que los cálculos se realizan a intervalos unita-
rios y el registro es para una longitud T de tiempo.
La auto-correlación se mide con una serie de coeficientes de auto-covariancia que muestran el
grado en que se afectan entre sí los valores separados por un intervalo de 𝜎 unidades. Los coeficien-
tes se definen mediante
Página 22 de 29

𝑇−𝜏
1
𝑅(𝜏)= ∑(𝑋 −𝑋̅)(𝑋 −𝑋̅), 𝜏=0,1,2,…,𝑇−1
𝑇−𝜏 𝑡 𝑡+𝜏
𝑡=1
En que 𝑋 es la observación al tiempo t y
𝑡
𝑇
1
𝑋̅ = ∑𝑋
𝑇 𝑡
𝑡=1
El caso especial de 𝜎=0, R(0), es una estimación de la variancia de la distribución de la que se
toma 𝑋 . La estimación de la variancia de la media de la muestra es
𝑡
𝑀
1 𝜏
𝑉(𝑋̅)= {𝑅(0)+2∑(1− )𝑅(𝜏)}, 𝑀 <𝑇
𝑇 𝑇
𝜏=1
𝑅(0)⁄𝑇 estima la variancia de la media de la muestra que se esperaría si las observaciones fueran
independientes. El término adicional representa la contribución de la auto-correlación. Los valores de
los coeficientes disminuyen al aumentar 𝜎. El valor de M debe ser suficientemente grande para incluir
los coeficientes significativos.
Análisis espectral
Se puede considerar a una serie de tiempo como la suma de las oscilaciones de distintas frecuen-
cias. Se puede relacionar el espectro de las frecuencias y las amplitudes de las oscilaciones con la
auto-correlación.
Un análisis espectral puede dar más información que la contenida en la estimación de un valor
medio. Dos sistemas pueden no mostrar diferencia significativa en sus valores medios, aunque su
comportamiento transitorio puede ser significativamente distinto.
Capítulo 9: Análisis de Datos de Salida (Law & Kelton)
En muchos estudios de simulación una gran cantidad de tiempo y dinero se gasta en el desarrollo
y programación del modelo, pero se hace poco esfuerzo para analizar los datos de salida de la simu-
lación apropiadamente. Un modo muy común de operación consiste en hacer una sola corrida de
simulación de longitud algo arbitraria y luego tratar las estimaciones de los resultados de la simula-
ción como las verdaderas características del modelo. Estas estimaciones son sólo realizaciones parti-
culares de variables aleatorias que pueden tener grandes variaciones. Como resultado, estas estima-
ciones podrían diferir en gran medida de las verdaderas características correspondientes para el mo-
delo, llevando a hacer inferencias erróneas sobre el sistema.
Existen varias razones por las cuales el análisis de datos de salida de una simulación no pueden
ser tratados en forma apropiada. Primero debe considerarse que una simulación es un experimento
de muestreo estadístico basado en computadoras, por lo tanto deben usarse las técnicas estadísticas
apropiadas para diseñar y analizar los experimentos de simulación. Una segunda razón para análisis
estadísticos inadecuados es que los procesos de salida de virtualmente todas las simulaciones son
no estacionarios y auto correlacionados. Por este motivo las técnicas estadísticas clásicas basadas
en observaciones IID no son aplicables directamente. Otro obstáculo para obtener estimaciones pre-
cisas de los verdaderos parámetros o características de un modelo es el costo del tiempo de compu-
tadora necesario para reunir la cantidad necesaria de datos de salida de la simulación.
Llamamos Y , Y ,… a un proceso estocástico de salida a partir de una sola corrida de simulación.
1 2
Los Y son variables aleatorias que en general no son IID.
i
Llamamos y a una observación de la variable Y en la i-esima corrida o replica. Si corremos la si-
ij j
mulación con un conjunto de números aleatorios diferentes obtendremos distintos valores de y
ij
Suponga que hacemos n corridas de la simulación independientes (con distintos números aleato-
rios en cada corrida) de tamaño m, resultando en las observaciones:
y , y ,…, y
11 12 1m
y , y ,…, y
21 22 2m
y , y ,…, y
n1 n2 nm
Las observaciones de una fila son no IID, además representan los valores de las distintas varia-
bles Y en la corrida “i”. Las observaciones de una columna en cambio sí son IID, y representan los
j
distintos valores que asume una única variable Y a través de las m corridas “i”. Esta independencia a
j
través de las corridas es la clave para los relativamente simples métodos de análisis de datos de sali-
da, el objetivo de este análisis es usar las observaciones y (i= 1,2,…, m; j=1,2,…n) para trazar infe-
ji
rencias acerca de las distribuciones de las variables aleatorias Y.
j
Página 23 de 29

Comportamiento transitorio y en estado estacionario de un proceso estocásti-
co
Considere las salidas de los procesos estocásticos Y , Y ,… Sea 𝐹(𝑦⁄𝐼)=𝑃(𝑌 ≤𝑦⁄𝐼) para i = 1,
1 2 𝑖 𝑖
2,…, donde y es un número real e I representa las condiciones iniciales usadas para iniciar la simula-
ción en el tiempo 0. Llamamos a 𝐹(𝑦⁄𝐼) la distribución transitoria del proceso de salida en el tiempo i
𝑖
para las condiciones iniciales I. 𝐹(𝑦⁄𝐼) será diferente para cada valor de i y cada conjunto de condi-
𝑖
ciones iniciales I.
Para I e y fijos, las probabilidades 𝐹 (𝑦⁄𝐼),𝐹 (𝑦⁄𝐼),… son solo una secuencia de números. Si
1 2
𝐹(𝑦⁄𝐼)→𝐹(𝑦) cuando 𝑖 →∞ para toda y y para cualesquiera condiciones iniciales I, entonces 𝐹(𝑦)
𝑖
se llama la distribución en estado estacionario del proceso de salida Y , Y ,… El estado estacionario
1 2
significa que todos ellos tendrán aproximadamente la misma distribución. Estas variables aleatorias
no serán independientes, sino que constituyen aproximadamente un proceso estocástico de cova-
rianza estacionaria.
La distribución en estado estacionario F(y) no depende de las condiciones iniciales I.
Tipos de simulaciones con respecto al análisis de la salida
Una simulación terminal es aquella para la cual hay un evento natural E que especifica la longitud
de cada corrida. Dado que las diferentes corridas usan números aleatorios independientes y la misma
norma de inicialización, esto implica que las variables aleatorias comparables en las diferentes corri-
das son IID. El evento E a menudo ocurre en un instante a partir del cual no se obtiene información
útil o en un instante cuando el sistema se limpia. Se especifica antes de realizar cualquier corrida, y el
tiempo de ocurrencia de E para una ejecución en particular puede ser una variable aleatoria. Dado
que las condiciones iniciales para una simulación terminal afectan generalmente a las medidas
deseadas de rendimiento, estas condiciones deben ser representativas de aquellas para el sistema
real.
Una simulación no terminal es aquella en la cual no hay un evento natural E que especifique la
longitud de la corrida. Una medida de rendimiento para una simulación tal se dice que es un paráme-
tro de estado estacionario si se trata de una característica de la distribución en estado estacionario de
algún proceso estocástico de salida Y , Y ,…
1 2
Los procesos estocásticos para la mayoría de los sistemas reales no tienen distribuciones en es-
tado estacionario, ya que las características del sistema cambian con el tiempo. Por otra parte, un
modelo de simulación puede tener distribuciones en estado estacionario, ya que las características
del modelo a menudo se suponen que no cambian con el tiempo.
Una simulación para un sistema particular puede ser terminal o no terminal, dependiendo de los
objetivos del estudio de simulación.
Considere un proceso estocástico Y , Y ,… para una simulación no terminal que no tiene una dis-
1 2
tribución en estado estacionario. Suponga que se divide el eje del tiempo en intervalos de tiempo de
igual longitud y contiguos llamados ciclos. Sea 𝑌𝐶 una variable aleatoria definida en el i-esimo ciclo, y
𝑖
asuma que 𝑌𝐶,𝑌𝐶,… son comparables. Suponga que 𝑌𝐶,𝑌𝐶,… tiene una distribución en estado esta-
1 2 1 2
cionario 𝐹𝐶 y que 𝑌𝐶 ~ 𝐹𝐶. Entonces una medida de rendimiento se dice que es un parámetro de ciclo
en estado estacionario si se trata de una característica de 𝑌𝐶 como la media 𝜐𝐶 =𝐸(𝑌𝐶). Así, un pa-
rámetro de ciclo en estado estacionario es solo un parámetro en estado estacionario del proceso del
ciclo correspondiente 𝑌𝐶,𝑌𝐶,….
1 2
Para una simulación no terminal, supongamos que el proceso estocástico Y , Y ,… no tiene una
1 2
distribución en estado estacionario, y que no existe una definición de ciclo apropiada de tal manera
que el proceso 𝑌𝐶,𝑌𝐶,… correspondiente tenga una distribución en estado estacionario. En estos ca-
1 2
sos, normalmente habrá una cantidad fija de datos que describen cómo los parámetros de entrada
cambian con el tiempo. Esto proporciona, en efecto, un evento E de terminación para la simulación y,
por lo tanto, las técnicas de análisis para la terminación de simulaciones son apropiado. Las medidas
de ejecución de los parámetros de tales simulaciones suelen cambiar con el tiempo y se incluyen en
la categoría de otros parámetros.
Análisis Estadístico para Simulaciones Terminales
Supongamos que hacemos n repeticiones independientes de una simulación terminal, donde cada
repetición se termina por el evento E y se comienza con las mismas condiciones iniciales. La inde-
pendencia de las repeticiones se logra mediante el uso de diferentes números aleatorios para cada
réplica. Supongamos por simplicidad que hay una sola medida de rendimiento de interés. Sea X una
j
variable aleatoria definida en la réplica j-ésima para j = 1, 2,..., n, y se supone que las X son variables
j
aleatorias IID.
Página 24 de 29

Estimación de Medias
Suponga que nos interesaría obtener una estimación puntual y el intervalo de confianza para la
media 𝜇 =𝐸(𝑋) donde X es una variable aleatoria definida sobre una corrida. Si se hacen n corridas
independientes de la simulación y siendo X , X ,..., X  las variables aleatorias IID resultantes obtene-
|     |     |     | 1 2 n |     |
| --- | --- | --- | ----- | --- |
mos que 𝑋̅(𝑛) es un estimador puntual no sesgado para μ y un intervalo de confianza aprox. del
100(1 - α)% con (0 < α < 1) para μ está dado por:
𝑆2(𝑛)
|     |     | 𝑋̅(𝑛)=±𝑡 |     | √   |
| --- | --- | -------- | --- | --- |
𝛼
|     |     |     | 𝑛−1 ;1− | 𝑛   |
| --- | --- | --- | ------- | --- |
2
Dicho intervalo de confianza se denomina procedimiento de muestra de tamaño fijo. La exactitud
| de este intervalo depende de la suposición de que los X son variables aleatorias normales.  |     |     |     | j   |
| ------------------------------------------------------------------------------------------- | --- | --- | --- | --- |
La cobertura realmente obtenida a partir del intervalo de confianza depende del modelo de simula-
ción sobre la muestra de tamaño n.
Obtención de una precisión especificada: Una desventaja del procedimiento anterior es que en
analista no tiene control sobre la mitad del tamaño del intervalo de confianza (es decir la precisión de
𝑋̅(𝑛)), por este motivo existen dos métodos que estiman el número de corridas requeridas para esti-
| mar la media 𝜇 | =𝐸(𝑋) con una precisión o error especificado.  |     |     |     |
| -------------- | ---------------------------------------------- | --- | --- | --- |
Estos métodos son: el número de corridas para establecer un error absoluto β y el número de co-
rridas para establecer un error relativo γ.
Comenzamos definiendo el primero, si la estimación 𝑋̅ es tal que | 𝑋̅− 𝜇 |=𝛽 , entonces decimos
que 𝑋̅ tiene un error absoluto de β. Si hacemos corridas de una simulación hasta que la mitad del
tamaño del intervalo de confianza de 100(1 - α)% es menor o igual que β, entonces:
|     |            | 1           | 1              | 1                 |
| --- | ---------- | ----------- | -------------- | ----------------- |
|     | 1−𝛼 ≈𝑃(𝑋̅− | 𝑡𝑎𝑚 ≤𝜇 ≤𝑋̅+ | 𝑡𝑎𝑚)=𝑃(|𝑋̅−𝜇|≤ | 𝑡𝑎𝑚)≤𝑃(|𝑋̅−𝜇|≤𝛽)  |
|     |            | 2           | 2              | 2                 |
(  1 𝑡𝑎𝑚 = mitad de tamaño del intervalo de confianza.)
2
𝑋̅ tiene un error absoluto de a lo sumo β con una probabilidad de aprox. 1 – α. Si hemos construi-
do un intervalo de confianza para μ basado en un número fijo de corridas n y si asumimos que nues-
tra estimación S2(n) de la varianza poblacional no cambiara a medida que el número de corridas se
incrementa, entonces obtenemos la siguiente expresión:
𝑆2(𝑛)
|     |     | 𝑛 ∗(𝛽)=min{𝑖 | ≥𝑛:𝑡     | √ ≤𝛽}  |
| --- | --- | ------------ | -------- | ------ |
|     |     | 𝑎            |          | 𝛼      |
|     |     |              | 𝑖−1 ; 1− | 2 𝑖    |
La fórmula obtenida indica el número total de corridas 𝑛∗(𝛽) que se necesitan para obtener un
𝑎
error absoluto de β. Los dos puntos se leen como “tal que”. Dicha fórmula se itera incrementando el
valor de 𝑖 hasta obtener un valor de i para el cual el lado a continuación de los 2 puntos de la expre-
sión sea válido. La precisión de la formula depende de cuan cercana es S2(n) de la Var(x).
Definimos ahora la segunda fórmula, si el valor de 𝑋̅ estimado es tal que | 𝑋̅−𝜇
|=𝛾, entonces de-
𝜇
cimos que 𝑋̅ tiene un error relativo de γ. Si hacemos corridas de una simulación hasta que la mitad
del tamaño del intervalo de confianza de 100(1 - α)% divido por 𝑋̅ es menor o igual que γ, entonces:
|          | 𝑋̅−𝜇 1⁄2𝑡𝑎𝑚 |                   | 1⁄2𝑡𝑎𝑚 |     |
| -------- | ----------- | ----------------- | ------ | --- |
| 1−𝛼 ≈𝑃(| | |≤          | )               ( | ≤𝛾)    |     |
|          | 𝑋̅          | |𝑋̅|              | |𝑋̅|   |     |
 ≤𝑃(|𝑋̅−𝜇|≤𝛾|𝑋̅|)
 =𝑃(|𝑋̅−𝜇|≤𝛾|𝑋̅−𝜇+𝜇|)
 ≤𝑃(|𝑋̅−𝜇|≤𝛾(|𝑋̅−𝜇|+|𝜇|))
 =𝑃((1−𝛾)|𝑋̅−𝜇|≤𝛾|𝜇|)
|     | 𝑋̅−𝜇     | 𝛾   |     |     |
| --- | -------- | --- | --- | --- |
|     |  =𝑃(| |≤ | )   |     |     |
|     | 𝜇        | 1−𝛾 |     |     |
𝛾
Así, 𝑋̅ tiene un error relativo de a lo sumo   con una probabilidad de aprox. 1 - α. Si hemos cons-
1+𝛾
truido un intervalo de confianza para μ basado en un número fijo de corridas n y si asumimos que
nuestras estimaciones de la media y varianza poblacional no cambiaran a medida que el número de
corridas se incrementa, entonces obtenemos la siguiente expresión:
Página 25 de 29

𝑆2(𝑛)
|     |     |           |     |          | √       |     |     |
| --- | --- | --------- | --- | -------- | ------- | --- | --- |
|     |     |           |     |   𝑡      | 𝛼       |     |     |
|     |     |           |     | 𝑖−1 ; 1− | 2       | 𝑖   |     |
|     |     | 𝑛∗(𝛾)=𝑚𝑖𝑛 |     | 𝑖 ≥𝑛:    |         | ≤𝛾′ |     |
|     |     | 𝑟         |     |          | |𝑋̅(𝑛)| |     |     |
|     |     |           |     |          |         |     |     |
|     |     |           |     |          |         |     |     |
|     |     |           |     | {        |         |     | }   |
Esta fórmula indica el número total de corridas 𝑛∗(𝛾) necesarias para obtener un error relativo de
𝑟
| γ. Donde 𝛾′ | 𝛾   |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- |
=  es el error relativo ajustado necesario para obtener un error relativo real de γ. Como
1+𝛾
en la formula anterior los dos puntos indica que esta fórmula se itera para valores de 𝑖 ≥1 hasta ob-
tener un valor de i para el cual el lado a continuación de los 2 puntos de la expresión sea válido.
La dificultad con el uso de la ecuación directamente para obtener una estimación 𝑋̅ con un error
relativo de 𝛾 es que 𝑋̅(𝑛) y 𝑆2(𝑛) no pueden ser estimaciones precisas de sus correspondientes pa-
rámetros de la población. Presentamos un procedimiento secuencial para obtener una estimación de
μ con un error relativo especificado que sólo toma tantas repeticiones como sean realmente necesa-
rias. El procedimiento supone que X , X ,… es una secuencia de variables aleatorias IID que necesi-
|     |     |     | 1   | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
tan no ser normal.
El objetivo específico del procedimiento es obtener una estimación de μ con un error relativo de 𝛾
y un nivel de confianza de 100(1 - α) porciento. Elija un número inicial de réplicas 𝑛 ≥2 y
0
𝑆2(𝑛)
|     |     |     | 𝛿(𝑛,𝛼)=𝑡 |          | 𝛼 √ |     |     |
| --- | --- | --- | -------- | -------- | --- | --- | --- |
|     |     |     |          | 𝑛−1 ; 1− |     | 𝑛   |     |
2
es el intervalo de confianza de longitud media habitual. Procedimiento:
| 0.  Hacer n                      | 0  réplicas de la simulación y fijar 𝑛 |     |           | =𝑛  | 0 .  |     |     |
| -------------------------------- | -------------------------------------- | --- | --------- | --- | ---- | --- | --- |
| 1.  Calcular 𝑋̅(𝑛) y δ(n,α) de X |                                        |     | , X ,…, X | .   |      |     |     |
|                                  |                                        |     | 1 2       | n   |      |     |     |
2.  Si 𝛿(𝑛,𝛼)⁄|𝑋̅(𝑛)|≤𝛾′, usar 𝑋̅(𝑛) como el punto estimado para μ y parar.
Equivalentemente, 𝐼(𝛼,𝛾)=[𝑋̅(𝑛)−𝛿(𝑛,𝛼),𝑋̅(𝑛)+𝛿(𝑛,𝛼) ] es aproximadamente un intervalo
de confianza del 100(1 - α) por ciento de μ con la precisión deseada. De lo contrario, reem-
plazar n por n + 1, hacer una réplica adicional de la simulación, e ir al paso 1.
Uso recomendado de los procedimientos: Si se está realizando un experimento exploratorio donde
la precisión del intervalo de confianza no puede ser abrumadoramente importante, se recomienda
utilizar el procedimiento de la muestra de tamaño fijo.
A partir de un experimento exploratorio que consiste en n repeticiones, se puede estimar el coste
| por réplica y la varianza de la población de las X y, a continuación, obtener una estimación aproxima- |     |     |     | j   |     |     |     |
| ------------------------------------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
da del número de réplicas, 𝑛∗(𝛽), necesaria para estimar μ con un error absoluto deseado 𝛽. Alterna-
𝑎
tivamente, se puede obtener una estimación aproximada del número de réplicas,  𝑛∗(𝛾), requerida
𝑟
para estimar μ con un error relativo deseado 𝛾. A veces, la elección de 𝛽 o 𝛾 puede tener que ser
atenuada por el costo asociado con el número requerido de réplicas.
Estimando otras medidas de rendimiento
Sea X una variable aleatoria definida en una réplica. Supongamos que queremos calcular la pro-
babilidad 𝑝=𝑃(𝑋 ∈𝐵), donde B es un conjunto de números reales. Hacemos n réplicas independien-
tes y sea X , X ,…,X  las variables aleatorias IID resultantes. Sea S el número de X que caen en el
1 2 n j
conjunto B. Luego S tiene una distribución binomial con parámetros n y p, y un estimador puntual
𝑆
| insesgado de p es 𝑝̂ | = .  |     |     |     |     |     |     |
| -------------------- | ---- | --- | --- | --- | --- | --- | --- |
𝑛
Supongamos que queremos estimar el q-cuartil x  de la distribución de la variable aleatoria X. Si
q
X , X ,…, X  son las estadísticas de orden correspondientes a las X de n replicas independientes,
| (1) (2)                              | (n) |     |                               |     |     |     | j   |
| ------------------------------------ | --- | --- | ----------------------------- | --- | --- | --- | --- |
| entonces un estimador puntual para x |     |     | q  es la muestra q-cuartil 𝑥̂ |     |     |     |     |
𝑞
|     |     |     |       | 𝑋 (𝑛𝑞) , 𝑠𝑖 𝑛𝑞 𝑒𝑠 𝑒𝑛𝑡𝑒𝑟𝑜 |     |     |     |
| --- | --- | --- | ----- | ------------------------ | --- | --- | --- |
|     |     |     | 𝑥̂ ={ |                          |     |     |     |
|     |     |     | 𝑞 𝑋   | , 𝑑𝑒 𝑜𝑡𝑟𝑎 𝑚𝑎𝑛𝑒𝑟𝑎         |     |     |     |
(⌊𝑛𝑞+1⌋)
Eligiendo condiciones iniciales
Supongamos que queremos estimar la demora promedio esperada de todos los clientes que lle-
gan y terminan sus demoras entre las 12 y la 1 pm (el período más activo) en un banco.
Supongamos que el banco abre a las 9 am, sin clientes presentes. Entonces podemos empezar la
simulación a las 9 am, sin clientes presentes y ejecutarlo durante 4 horas simuladas. En la estimación
de la demora media esperada deseada, utilizamos sólo las demoras de los clientes que llegan y com-
pletan sus demoras entre el mediodía y la 1 pm. Una desventaja de este enfoque es que 3 horas de
tiempo simulado no se utilizan directamente en la estimación.
Página 26 de 29

Un enfoque alternativo es recolectar datos sobre el número de clientes presentes en el banco al
mediodía en diferentes días. Sea 𝑝̂ la proporción de estos días en que i clientes (i = 0, 1,…) están
𝑖
presentes al mediodía. A continuación se simula el banco del mediodía a 1 pm, con el número de
clientes presentes al mediodía siendo elegido aleatoriamente de la distribución {𝑝̂ }.
𝑖
Múltiples medidas de rendimiento
Para la mayoría de las simulaciones del mundo real una serie de medidas de rendimiento son de
interés al mismo tiempo. Supongamos que I es un intervalo de confianza del 100(1 - α)% para la
s
medida de rendimiento μ (donde s = 1, 2,…, k). Entonces la probabilidad de que todos los k interva-
s
los de confianza contengan simultáneamente sus respectivas medidas verdaderas satisface 𝑃(𝜇 ∈
𝑠
𝐼 𝑝𝑎𝑟𝑎 𝑡𝑜𝑑𝑜 𝑠 =1,2,…,𝑘)≥1−∑𝑘 𝛼 ya sea o no que los I son independientes.
𝑠 𝑠=1 𝑠 s
Cuando el valor de k es pequeño, si se desea que el nivel de confianza global asociado con k in-
tervalos de confianza sea al menos de 100(1 - α)%, elegir los 𝛼 de modo que ∑𝑘 𝛼 =𝛼
𝑠 𝑠=1 𝑠
Resumen: Construcción de Intervalos de Confianza
Si la población es Normal:
Procedimiento de muestra de tamaño fijo: Sirve para estimar un intervalo de confianza de la media
poblacional 𝜇 =𝐸(𝑋)
Si la población no es Normal:
Número de corridas para un error absoluto β: Sirve para estimar el número de corridas n supo-
a
niendo que la varianza estimada no cambiara a medida que el número de corridas se incrementa.
Número de corridas para un error relativo γ: Sirve para estimar el número de corridas n suponien-
r
do que la media y varianza estimadas no cambiaran a medida que el número de corridas se incre-
menta.
Capítulo 10: Comparando las configuraciones del sistema alternati-
vas (Law & Kelton)
Introducción
La dificultad de muchos estudios de simulación es que los datos de salida de la simulación son es-
tocásticos, por lo que la comparación de dos sistemas sobre la base de sólo una única corrida de
cada uno es un enfoque muy poco fiable.
Un requerimiento básico para usar muchos métodos estadísticos para comparar configuraciones
alternativas es la capacidad de recoger observaciones IID con expectativa igual a la medida de ren-
dimiento deseada. Si queremos comparar sistemas alternativos sobre la base del comportamiento en
estado estacionario, la situación se vuelve más complicada ya que no podemos obtener fácilmente
observaciones IID teniendo expectativa igual a la medida de rendimiento en estado estacionario
deseada.
Intervalos de confianza para la diferencia entre las medidas de rendimiento de
2 sistemas
Aquí consideramos el caso especial de la comparación de dos sistemas sobre la base de algunas
de las medidas de rendimiento, o la respuesta esperada. Efectuamos esta comparación mediante la
formación de un intervalo de confianza para la diferencia en las dos expectativas, en lugar de hacerlo
por un test de hipótesis para ver si la diferencia observada es significativamente diferente de cero.
Para i = 1, 2, sea X , X ,…, X una muestra de n observaciones IID del sistema i, y sea 𝜇 =
i1 i2 in i 𝑖
𝐸(𝑋 ) la respuesta de interés esperada; queremos construir un intervalo de confianza para 𝜁 =𝜇 −
𝑖𝑗 1
𝜇 . Ya sea o no que X y X son independientes depende en como la simulación se ejecute.
2 1i 2i
Un intervalo de confianza t-apareada
Si 𝑛 =𝑛 , o están dispuestos a descartar algunas observaciones del sistema en el que en reali-
1 2
dad tenemos más datos, se puede emparejar X con X para definir 𝑍 =𝑋 −𝑋 , para j=1, 2,…, n.
1i 2i 𝑗 1𝑗 2𝑗
Entonces Z son variables aleatorias IID y 𝐸(𝑍)=𝜁, la cantidad por la que queremos construir un
j 𝑗
intervalo de confianza. Por lo tanto, podemos hacer 𝑍̅(𝑛)=
∑𝑛
𝑗=!
𝑍𝑗
y 𝑉̂𝑎𝑟[𝑍̅(𝑛)]=
∑𝑛
𝑗=1
[𝑍𝑗−𝑍̅(𝑛)] 2
y formar
𝑛 𝑛(𝑛−1)
el (aproximado) 100(1 - α) % intervalo de confianza 𝑍̅(𝑛)±𝑡
𝑛−1;1−
𝛼√𝑉̂𝑎𝑟[𝑍̅(𝑛)] . Si los Z
j
está distri-
2
buido normalmente, este intervalo de confianza es exacto, de lo contrario, nos basamos en el teore-
ma central del límite. No tenemos que asumir que X y X son independientes; ni que 𝑉𝑎𝑟(𝑋 )=
1i 2i 1𝑖
𝑉𝑎𝑟(𝑋 ). Permitir correlación positiva entre X y X puede ser de gran importancia, ya que esto con-
2𝑖 1i 2i
duce a una reducción en Var(Z) y por lo tanto a un intervalo de confianza más pequeño. El intervalo
j
Página 27 de 29

de confianza se conoce como intervalo de confianza t apareadas, y en su derivación redujimos esen-
cialmente el problema de los dos sistema a uno que implica una sola muestra. Los Xij son variables
aleatorias definidas sobre toda una réplica.
Un intervalo de confianza de 2 muestras t modificado
Un segundo enfoque para la formación de un intervalo de confianza para 𝜁 no empareja las obser-
vaciones de los 2 sistemas, pero requiere que las X  sean independientes de las X . Sin embargo, n
|     |     |     |     |     | 1i  |     |     |     | 2i  | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
y n 2  pueden ser diferentes.
Para aplicar el clásico enfoque de 2 muestras, debemos tener Var(X 1i ) = Var(X 2i ). Aunque la igual-
dad de variancias no es probablemente una suposición segura cuando simulamos sistemas reales,
recomendamos usar este enfoque.
El problema de comparación de 2 sistemas con variancia desigual y desconocida cuando las X
2i
están distribuidas normalmente. Sea
|     |      | ∑𝑛𝑖 |                              |     |     | ∑𝑛𝑖 |          | 2   |     |     |
| --- | ---- | --- | ---------------------------- | --- | --- | --- | -------- | --- | --- | --- |
|     |      |     | 𝑋                            |     |     |     | [𝑋 −𝑋̅(𝑛 | )]  |     |     |
|     | 𝑋̅(𝑛 | 𝑗=1 | 𝑖𝑗                      𝑆2(𝑛 |     |     | 𝑗=1 | 𝑖𝑗       | 𝑖 𝑖 |     |     |
|     |      | )=  |                              |     |     | )=  |          |     |     |     |
|     | 𝑖 𝑖  |     | 𝑛                            |     | 𝑖 𝑖 |     | 𝑛 −1     |     |     |     |
|     |      |     | 𝑖                            |     |     |     | 𝑖        |     |     |     |
Para i = 1, 2. Luego calculamos los grados de libertad estimados
|     |     |     |     | 𝑆2(𝑛 | ) 𝑆2(𝑛 | ) 2 |     |     |     |     |
| --- | --- | --- | --- | ---- | ------ | --- | --- | --- | --- | --- |
|     |     |     |     | 1    | 1 2    | 2   |     |     |     |     |
|     |     |     |     | [    | +      | ]   |     |     |     |     |
|     |     |     | 𝑓̂= | 𝑛 1  |        | 𝑛 2 |     |     |     |     |

|     |     |     |     | 𝑆2(𝑛  | 2 𝑆2(𝑛 |      | 2   |     |     |     |
| --- | --- | --- | --- | ----- | ------ | ---- | --- | --- | --- | --- |
|     |     |     |     |       | )      | )    |     |     |     |     |
|     |     |     |     | [ 1 1 | ] [    | 2 2  | ]   |     |     |     |
|     |     |     |     | 𝑛     |        | 𝑛    |     |     |     |     |
|     |     |     |     | 1     | +      | 2    |     |     |     |     |
|     |     |     |     | 𝑛 −1  |        | 𝑛 −1 |     |     |     |     |
|     |     |     |     | 1     |        | 2    |     |     |     |     |
|     |     |     | 2   |       | 2      |      |     |     |     |     |
Y usamos 𝑋̅ (𝑛 )−𝑋̅ (𝑛 )±𝑡 √ 𝑆1 (𝑛 1) 𝑆2 (𝑛 2)  como una aproximación del intervalo de con-
| 1   | 1 2 | 2 𝑓̂,   1− | 𝛼   | +   |     |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |            |     | 𝑛 1 | 𝑛 2 |     |     |     |     |     |
2
fianza para 𝜁 con un nivel de confianza de 100(1 – α)%. El intervalo de confianza, conocido como el
intervalo de confianza de Welch, puede también usarse para validar un modelo de simulación  de un
sistema existente.
Comparando los 2 métodos
La elección del método a usar usualmente se hará de acuerdo a la situación. Una consideración
es que el uso de números aleatorios comunes para simular los 2 sistemas puede a veces conducir a
una considerable reducción en Var(Z) y, por lo tanto, a un intervalo de confianza más pequeño; esto
j
implica que n  = n  y que X  y X  no serán independientes, por eso el enfoque t-apareada es requeri-
| 1 2                     | 1j                                     | 2j  |     |     |     |     |     |     |     |     |
| ----------------------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| do. Por otro lado, si 𝑛 | 1 ≠𝑛 2  se debe usar el método Welch.  |     |     |     |     |     |     |     |     |     |
Comparaciones basadas en las medidas de rendimiento en estado estacionario
El ingrediente básico de la mayoría  de las técnicas de comparación es una muestra de observa-
ciones IID con expectativa igual a la medida de rendimiento sobre la cual se hace la comparación.
En algunos casos, queremos comparar 2 o más sistemas sobre la base de una medida de rendi-
miento en estado estacionario. Aquí ya no podemos simplemente replicar los modelos, ya que los
efectos de inicialización pueden sesgar los resultados. Es más difícil efectuar una comparación válida
basada en las medidas de rendimiento en estado estacionario. El método de replicación/borrado para
el análisis en estado estacionario puede adaptarse al problema de construir un intervalo de confianza
para la diferencia entre 2 medias en estado estacionario.
Intervalos de confianza para comparar más de 2 sistemas
Haremos distintos declaraciones de intervalos de confianza simultáneamente, por lo que sus nive-
les individuales tendrán que ajustarse hacia arriba para que el nivel de confianza global de la cobertu-
ra de todos los intervalos de sus respectivos objetivos esté en el nivel deseado 1 – α. Usamos
𝑃(𝜇 ∈𝐼  𝑝𝑎𝑟𝑎 𝑡𝑜𝑑𝑜 𝑠=1,2,…,𝑘)≥1−∑𝑘 𝛼  para asegurar que el nivel de confianza global es al
| 𝑠 𝑠 |     |     | 𝑠=1 | 𝑠   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
menos 1 – α.
Comparaciones con un estándar
Supongamos que uno de las variantes del modelo es un estándar. Si llamamos al estándar siste-
ma 1 y a las otras variantes sistemas 2, 3,…, k, el objetivo es construir k – 1 intervalos de confianza
para las k – 1 diferencias 𝜇 −𝜇 , 𝜇 −𝜇 ,… , 𝜇 −𝜇 , con un nivel de confianza global 1 – α. Hace-
|     | 2   | 1   | 3 1 | 𝑘   | 1   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1−𝛼
mos c = k – 1 intervalos individuales con un nivel de  . Entonces podemos decir que para todo i = 2,
𝑘−1
3,…, k, el sistema i difiere del estándar si el intervalo para 𝜇 −𝜇  no alcanza 0, y que el sistema i no
|     |     |     |     |     |     | 𝑖   | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
es significativamente diferente del estándar si este intervalo contiene 0.

Página 28 de 29

Todas las comparaciones por pares
En algunos estudios, queremos comparar cada sistema con cada otro para detectar y cuantificar
cualquier diferencia de pares significativa. Un enfoque consistiría en formar intervalos de confianza
𝑘(𝑘−1)
para las diferencias 𝜇 −𝜇 , para todo 𝑖 e 𝑖 entre 1 y k, con 𝑖 <𝑖 . Aquí habrá intervalos
𝑖1 𝑖2 1 2 1 2 2
1−𝛼
individuales, por eso cada uno debe hacerse con un nivel en orden de tener un nivel de con-
[𝑘(𝑘−1)⁄2]
fianza de al menos 1 – α para todos los intervalos juntos.
Página 29 de 29