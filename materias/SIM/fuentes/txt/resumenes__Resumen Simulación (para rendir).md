SIMULACIÓN
(Apunte NO oficial)

ACLARACIONES Y COMENTARIOS

  Este resumen / apunte surge de lo extraído de toda la bibliografía indicada por Leale (actual
jefe de cátedra de Simulación) en consultas, de material que me pasó por correo y de lo que vi
que tomó en los últimos finales. Lo que no significa que pueda faltar algo (o sobrar); creería
que no, pero lo aclaro por las dudas.

  No importa con quien la cursaste, a partir del año pasado Leale unificó todo el material de la

cátedra, es decir, que a todos se le toma lo mismo en los finales.

 Creería que lo que está en este apunte es suficiente para rendir, pero no lo puedo garantizar.

Lo ideal es ir mirando en paralelo el material indicado por la cátedra.

 En este resumen no se incluye el capítulo 4 del Naylor pero es recomendable pegarle una leída.
Dudo  tomen  algo  de  ahí  en  un  final  con  la  modalidad  actual  (virtual/oral)  pero  sirve  para
refrescar las diferentes distribuciones y conocer técnicas de generación de números aleatorios
para esas distribuciones.

 Los profesores hacen el final llevadero y los 3 te preguntan algo. No entran mucho en detalle
y esperan que uno desarrolle sin interrumpirlo. Leale siempre pregunta por el “Método de
muestras apareadas”, hay que saberlo.

Apunte NO oficial – Joel Arnold – Marzo 2021

INDICE

MODELADO DE SIMULACIÓN BÁSICO ..................................................................................................... 3

Formas de estudiar un sistema ............................................................................................................ 3

Algunas definiciones............................................................................................................................ 4

Clasificación de los modelos de simulación ......................................................................................... 4

Simulación de un “Sistema de Inventario” .......................................................................................... 5

Análisis de la salida.......................................................................................................................... 7

PASOS PARA REALIZAR UN ESTUDIO DE SIMULACIÓN ............................................................................ 7

TEORÍA DE COLAS .................................................................................................................................... 8

Clasificación de los modelos de colas .................................................................................................. 8

Medidas de rendimiento ..................................................................................................................... 9

Cola M/M/1 ..................................................................................................................................... 9

Cola M/M/C................................................................................................................................... 10

Análisis de costos .......................................................................................................................... 10

Población de clientes finita (M/M/c/k) ......................................................................................... 10

Capacidad de espera limitada (capacidad cola ≠ ∞) ...................................................................... 11

Cola con distribución de servicio general (M/G/c) ......................................................................... 11

Consideraciones gerenciales adicionales ........................................................................................... 11

ANÁLISIS DE RESULTADOS ..................................................................................................................... 12

Intervalo de confianza para μ ............................................................................................................ 12

Obteniendo una precisión especifica (valor absoluto)....................................................................... 12

Comparación de muestras (método de “Muestras apareadas”) ........................................................ 12

NÚMEROS ALEATORIOS ........................................................................................................................ 13

Características de un buen generador de números aleatorios........................................................... 14

Generador congruencial lineal .......................................................................................................... 14

Parámetros: ................................................................................................................................... 14

Características importantes: .......................................................................................................... 14

Prueba de test aleatoriedad Chi-cuadrado (χ2): ................................................................................ 15

Apunte NO oficial – Joel Arnold – Marzo 2021

MODELADO DE SIMULACIÓN BÁSICO

Un modelo es un conjunto de suposiciones que, generalmente, adoptan la forma de relaciones
matemáticas lógicas y que nos permite comprender cómo se comporta determinado sistema en
estudio.

Estos sistemas pueden ser instalaciones o procesos de diversos tipos del mundo real.

 Si  las  relaciones  que  componen  el  modelo  son  bastante  sencillas  es  posible  usar  métodos
matemáticos para obtener información exacta respecto a  las preguntas  de  interés. En este
caso, se denomina la solución como “solución analítica”.

 Si el modelo resulta complejo para ser estudiado analíticamente debe ser estudiado mediante
la simulación. En este caso, se utiliza una computadora para evaluar el modelo numéricamente
y la información reunida se usa para estimar las características deseadas del modelo.

Formas de estudiar un sistema

SISTEMA

Experimentar con el
sistema actual

Experimentar con un
modelo del sistema

Modelo físico

Modelo matemático

Solución analítica

Simulación

Apunte NO oficial – Joel Arnold – Marzo 2021

Algunas definiciones

Sistema: colección de entidades (personas, maquinas, etc.) que interactúan para el cumplimiento
de un objetivo.

Estado del sistema: colección de variables necesarias para describir un sistema en un momento
determinado, en relación al objetivo de estudio.

Evento: ocurrencia instantánea que podría cambiar el estado del sistema.

¿Por qué podemos querer estudiar el comportamiento de un sistema?
Para  entender  mejor  las  relaciones  entre  componentes  que  lo  conforman  o  para

predecir el rendimiento que puede llegar a tener bajo nuevas condiciones.

Clasificación de los modelos de simulación

  Estáticos  vs.  Dinámicos:  los  modelos  estáticos  sirven  para  representar  un  sistema  en  un
momento  determinado  o  para  sistemas  donde  el  tiempo  no  es  influyente.  En  los  modelos
dinámicos se representa la evolución del sistema a lo largo del tiempo.

  Determinísticos vs. Estocásticos: los modelos determinísticos no tienen ningún componente
probabilístico. En los estocásticos hay, al menos, algún componente aleatorio de entrada y se
producen  salidas  que  son  aleatorias;  sirven  para  estimar  verdaderas  características  del
sistema.

  Continuos vs. Discretos: los modelos continuos se utilizan para estudiar sistemas donde  las
variables de estado cambian constantemente en el tiempo. Los discretos para casos donde las
variables de estado cambian instantáneamente entre puntos separados en el tiempo.

A  partir  de  lo  visto  hasta  acá,  recomiendo  leer  y  comprender  todo  el  punto  “1.3
Simulación de eventos discretos” y “1.4 Simulación de un sistema de colas de un solo
servidor”,  junto  con  sus  ejemplos.  Si  bien  es  algo  largo,  se  hace  llevadero  y  con  los
ejemplos del final se interpreta mejor. Hay partes que tranquilamente se pueden pasar
por alto o leer por arriba, pero nos sirve para entender el funcionamiento y conocer las
fórmulas que se usan para modelar. Dudo que tomen algo muy específico de estos 2
puntos en el final oral pero no así de lo que viene a continuación (ejemplo del “Sistema

de inventario”), ese lo toman siempre.

Apunte NO oficial – Joel Arnold – Marzo 2021

Simulación de un “Sistema de Inventario”

El objetivo de esta simulación es decidir cuántos ítems deben tenerse en inventario los próximos
meses para minimizar los costos. Es decir, elegir la mejor política de inventario.

  La empresa vende un solo producto.

  Los  tiempos  entre  demandas  son  variables  aleatorias  exponenciales  independientes  del

momento de ocurrencia e idénticamente distribuidas (IID) con una media de 0,1 mes.

  Las probabilidades de la cantidad demandada son:

D =

1  1/6

2  1/3

3  1/3

4 1/6

  Eventos:

  Llegada de un pedido desde el proveedor a la empresa.

  Demanda de productos por parte de un cliente.

  Evaluación de inventario al inicio del mes.

  Pedido al proveedor: tiene una demora de entrega representada por una variable aleatoria

uniformemente distribuida entre 0,5 y 1 mes.

  Costo de la orden: K + i.Z; donde K es el costo fijo, i es el costo por unidad y Z es la cantidad de

unidades pedidas.

  Política de pedidos: es una política estacionaria (s,S) con ‘s’ siendo el nivel mínimo deseado en

existencia y ‘S’ el nivel máximo.

Z =

S - I
  0

 si
 si

I < s
I ≥ s

Siendo I el nivel de inventario.

  Valores y variables:

 I(t): nivel de inventario al momento t (puede ser positivo, negativo o cero)

 I+(t): número de unidades que realmente están en existencia.

 I–(t): número de unidades demandadas y no entregadas.

 h: costo por ítem por mes de inventario.

 π: costo por ítem por mes de atraso en la entrega.

Apunte NO oficial – Joel Arnold – Marzo 2021

𝐼+ =

𝑛
∫ 𝐼+(𝑡) 𝑑𝑡
0
𝑛

𝐼− =

𝑛
∫ 𝐼−(𝑡) 𝑑𝑡
0
𝑛

 I+.h: costo promedio mensual por ítems en existencia.

 I-.π: costo promedio mensual por ítems adeudados.

Una representación de I(t), I+(t) e I-(t) a lo largo del tiempo.

  Rutinas:

Evento: Llegada de pedido

 Incrementar nivel de inventario.
 Eliminar el evento de llegada de pedidos de consideración.

Evento: Demanda

 Generar el tamaño de la demanda.
 Reducir el nivel de inventario.
 Programar el próximo evento de demanda.

Evento: Evaluación de inventario

 Si I (+) ≥ s, programar próxima evaluación.
 Si I (+) < s:

-  Determinar el tamaño del pedido [𝑆 –  𝐼 (𝑡) ]
-  Hacer estadísticas.
-  Programar llegada de la orden.
-  Programar próxima evaluación.

Apunte NO oficial – Joel Arnold – Marzo 2021

Análisis de la salida

En este punto hay un análisis de diferentes corridas de simulación aplicando diferentes políticas
de inventario mínimo (s) y máximo (S).

En primer lugar, se observa cómo varían los diferentes costos (de pedido, de mantenimiento de
unidades en inventario y de demora en la entrega) según la política utilizada y cuál de ellas resulta
conveniente (menor costo total).

En segundo lugar, se menciona que con una corrida de simulación (por más que sea de 120 meses)
solo obtenemos un valor “estimado” pero, para obtener el costo mensual promedio “esperado”,
es necesario realizar varias corridas de simulación.

--------------------------------------------

PASOS PARA REALIZAR UN ESTUDIO DE SIMULACIÓN

1) Definición del sistema en estudio: definición de las variables de decisión, la interacción entre
ellas  y  los  alcances  y  limitaciones  del  modelo.  Determinar  qué  motivó  (objetivo  de  la
simulación) el estudio de simulación.

2) Generación de un modelo de simulación base: creación de un modelo no muy detallado con

la información que se tiene al momento.

3) Recolección y análisis de datos: en este paso se recopila y analiza la información estadística
necesaria  para  determinar  las  distribuciones  de  probabilidad  de  cada  una  de  las  variables
aleatorias del modelo.

4) Generación  del  modelo  preliminar:  en  esta  etapa  se  integra  toda  la  información  obtenida

hasta el momento para lograr un modelo lo más cercano posible al sistema en estudio.

5) Verificación  del  modelo:  en  este  paso  se  comprueba  que  todos  los  parámetros  usados
funcionen  correctamente  y  que  el  comportamiento  del  modelo  sea  cercano  a  lo  que  se
esperaba.

6) Validación del modelo: este proceso consiste en realizar una serie de pruebas sobre el modelo,
utilizando  información  real  en  la  entrada  para  observar  cómo  se  comporta  y  analizar  los
resultados.

7) Generación del modelo final: modelo resultante luego de validar y verificar el preliminar.

8) Determinación de los escenarios: junto con el cliente, se determinan los escenarios que se
quieren analizar. Una opción es definir un escenario pesimista, uno optimista y uno intermedio
para la variable de respuesta más importante. Tener en cuenta que no todas las variables de
respuesta se comportan igual ante los cambios en los distintos escenarios.

Apunte NO oficial – Joel Arnold – Marzo 2021

9) Análisis de sensibilidad: realización de pruebas estadísticas para comparar los escenarios con
los mejores resultados finales para determinar el ganador. Si dos escenarios tienen resultados
similares  será  necesario  comparar  sus  intervalos  de  confianza  respecto  de  la  variable  de
respuesta  final.  También  puede  ser  necesario  realizar  más  réplicas  (ver  sección  Análisis  de
resultados).

10)  Documentación del modelo, sugerencias y conclusiones: acá se incluye toda la información
recolectada, sugerencias de uso del modelo y de los resultados y, por último, las conclusiones
de la simulación.

--------------------------------------------

TEORÍA DE COLAS

 Población  de  clientes:  cuando  el  número  de  clientes  potenciales  es  bastante  grande,  se

considera infinita.

 Proceso de llegada: forma en que los clientes llegan a solicitar servicio. La característica más

importante es el tiempo entre llegadas, que puede ser determinístico o probabilístico.

 Proceso de colas: puede importar la cantidad de colas (una o varias), si la cola es infinita o

finita y la disciplina de colas (PEPS, UEPS, prioridad, etc.).

 Proceso de servicio: esto es cómo son atendidos los clientes. El sistema puede ser de cola
simple (con un solo servidor) o de canal múltiple (con varios). La característica más importante
es el tiempo requerido para llevar a cabo el servicio.

Clasificación de los modelos de colas

Se supone población infinita, una sola cola de espera y espacio en cola infinito.

  D: determinístico.
  M: probabilístico, exponencial.
  G: probabilístico, pero no exponencial.

Ejemplo:

M        /    M        /      2

Servidores en paralelo

Tiempo de servicio

Tiempo entre llegadas

Apunte NO oficial – Joel Arnold – Marzo 2021

Medidas de rendimiento

Cualquier  sistema  de  colas  tiene  dos  fases:  la  inicial,  donde  se  conservan  los  efectos  de  las
condiciones  iniciales,  se  llama  “fase  transitoria”.  La  final,  donde  esos  efectos  desaparecen,  se
llama “estado estable”.

Las medidas de rendimiento son valores numéricos que se utilizan para evaluar cómo funciona
un sistema de colas en estado estable.

Para  obtener  las  diferentes  medidas  de  rendimiento  es  necesario  conocer  los  valores  de  los
siguientes parámetros, correspondientes a los procesos de llegada y de servicio.

  λ = número promedio de llegadas por unidad de tiempo.

  μ = número promedio de clientes atendidos por unidad de tiempo por estación.

𝝀

  ρ =
𝝁

  (“intensidad de tráfico”).

Cola M/M/1

 Para que el sistema alcance un estado estable se tiene que dar que μ > λ.

 Población: infinita.

 Llegadas:  proceso  de  Poisson  (relacionada  con  la  distribución  exponencial  mediante  el

parámetro λ) con λ clientes por unidad de tiempo.

Ejemplo: “P(número de llegadas en 10 min = 2) = x”

 Cola: única, con capacidad infinita. Disciplina PEPS.

 Servicio: distribución exponencial. μ clientes promedio por unidad de tiempo.

Número promedio en fila:

𝐿𝑞    =

𝜌2
1 −  𝜌

Tiempo promedio de espera en la cola:

𝑊𝑞   =

𝐿𝑞
𝜆

Tiempo promedio de espera en el sistema:

𝑊 =   𝑊𝑞   +

1
𝜇

Tiempo que lleva
atender un cliente
en el servidor

Apunte NO oficial – Joel Arnold – Marzo 2021

Número promedio en el sistema:

𝐿 = 𝑊. 𝜆

Probabilidad de que no haya clientes en el sistema:

𝑃0   =  1 –  𝜌

Probabilidad de que un cliente que llegue espere:

Probabilidad de que haya n clientes en el sistema:

𝑃𝑤   =  1 – 𝑃0 =  𝜌

𝑃𝑛   =   𝜌𝑛. 𝑃0

𝑈 =  𝜌

Utilización (del servidor):

Cola M/M/C

Tiene  las  mismas  características  que  el  M/M/1  (población  infinita,  disciplina  de  cola  PEPS  y
capacidad de cola infinita) solo que en lugar de un servidor puede haber varios.

Para  que  el  sistema  alcance  un  estado  estable  se  tiene  que  dar  que  c.μ  >  λ  (c:  cantidad  de
servidores en paralelo).

Análisis de costos

En un sistema de colas donde se puede controlar el número de servidores o su tasa de servicio,
para conocer el costo total por unidad de tiempo, es necesario saber:

 El costo por servidor por unidad de tiempo (Cs).

 El costo por unidad de tiempo por cliente esperando en el sistema (Cw).

 El número promedio de clientes por unidad de tiempo en el sistema (L).

Luego,

Costo total por unidad de tiempo para c servidores = (𝐶𝑠. 𝑐) + (𝐶𝑤. 𝐿)

Población de clientes finita (M/M/c/k)

En estos casos la tasa de llegadas disminuye a medida que aumenta el número de clientes en el
sistema porque existen menos clientes que aún no llegaron.  El proceso de llegada se describe

Apunte NO oficial – Joel Arnold – Marzo 2021

considerando la tasa de llegada de cada cliente individual. No se puede describir mediante una
tasa fija.

Capacidad de espera limitada (capacidad cola ≠ ∞)

En este caso, para poder realizar el análisis de costos, es necesario conocer la  probabilidad de
negación  del  servicio  (Pd).  La  misma  indica  la  probabilidad  de  que  un  cliente  que  llega  sea
rechazado y se le niegue el servicio porque el área de espera está llena.

Entonces, para el cálculo del costo total por unidad de tiempo se debe tener en cuenta, además
del costo por servidor (Cs) y el costo por esperar (Cw), el costo asociado a la pérdida de un cliente
(Cd).

Luego,

𝐶𝑜𝑠𝑡𝑜 𝑡𝑜𝑡𝑎𝑙 𝑝𝑜𝑟 𝑢𝑛𝑖𝑑𝑎𝑑 𝑑𝑒 𝑡𝑖𝑒𝑚𝑝𝑜 = (𝐶𝑠. 𝑐)   +   (𝐶𝑤. 𝐿)   +   (𝐶𝑑. 𝜆. 𝑃𝑑)

Cola con distribución de servicio general (M/G/c)

En este tipo de sistemas para calcular las medidas de rendimiento es necesario conocer, además
de la tasa promedio de llegadas (λ), el tiempo promedio por servicio y la desviación estándar del
tiempo de servicio. Si la desviación estándar es igual a 0, es determinístico.

Consideraciones gerenciales adicionales

 Elección del modelo adecuado: puede que el sistema en cuestión no se adapte a los modelos
conocidos. En estos casos se pueden hacer algunas suposiciones para aproximarlo a  dichos
modelos.

 Sistema  de  colas  adicionales:  pueden  existir  sistemas  con  características  distintas  a  las

estudiadas, como, por ejemplo:

  Sistema con clientes que llegan en lotes.

  Sistema con clientes que esperan en múltiples filas.

  Sistema con atención en grupo.

  Sistema con diferentes disciplinas de atención.

  Sistema con clientes que pueden renunciar a esperar.

  Sistema con red de estaciones de trabajo.

 Análisis de sensibilidad: consiste en calcular repetidamente las medidas de rendimiento y los
análisis económicos para el modelo, cambiando en cada caso los datos de interés (cantidad de
servidores, tasa de llegada, tasa de servicio, etc.) para encontrar la mejor solución.

Apunte NO oficial – Joel Arnold – Marzo 2021

 Análisis  de  equilibrio:  hace  referencia  a  la  elección  de  los  parámetros  del  sistema  en  la
búsqueda de valores en particular para ciertas medidas de rendimiento y cómo eso afecta a
otras. Por lo tanto, es necesario hacerlo procurando obtener valores aceptables para todas las
medidas de rendimiento.

--------------------------------------------

ANÁLISIS DE RESULTADOS

Una réplica o corrida es una ejecución del modelo en una ocasión. Como, muy probablemente,
los valores en las variables de interés sean distintos si se corre el modelo nuevamente, muchas
veces  es  necesario  efectuar  un  número  de  corridas  independientes  y  obtener  un  intervalo  de
confianza sobre el cual, con cierto grado de seguridad, esté el verdadero valor de la variable.

Intervalo de confianza para μ

𝑋̅(𝑛) ± 𝑡𝑛−1,1−(

𝛼

2). √

𝑆2(𝑛)
𝑛

Con una confianza aproximada del 100.(1-α)% ; (0<α<1)

Obteniendo una precisión especifica (valor absoluto)

Suponiendo que tenemos construido un intervalo de confianza para μ basado en un número fijo
de  n  réplicas  y  si  asumimos  que  la  estimación  de  la  varianza  poblacional  no  va  a  cambiar
sustancialmente a medida que el número de réplicas aumente, entonces, para saber el número
aproximado de réplicas necesarias para obtener un error absoluto de β (=|𝑿̅-μ|), calculamos:

∗ (𝛽) = 𝑚𝑖𝑛 {𝑖 ≥ 𝑛: 𝑡𝑖−1,1−(
𝑛𝑎

𝛼
2

). √

𝑆2 (𝑛)
𝑖

≤ 𝛽}

Comparación de muestras (método de “Muestras apareadas”)

Este método sirve para comparar 2 sistemas distintos (o 2 diseños distintos de un mismo sistema)
respecto a una medida de rendimiento en particular. Se calcula un intervalo de confianza para la
diferencia entre las 2 esperanzas (μ1-μ2).

Apunte NO oficial – Joel Arnold – Marzo 2021

Condiciones:

  n1 = n2 = n son la cantidad de observaciones de cada sistema (si uno tiene de más, hay

que quitar algunas para igualar).

  X11, X12…, X1n son las observaciones o réplicas IID del sistema 1.

  X21, X22…, X2n son las observaciones IID del sistema 2.

  Cada X1J y X2j (j = 1, 2, …, n) son variables aleatorias definidas para una réplica completa.
Por ejemplo, X13 es el valor promedio de  la variable en análisis para el sistema 1 en  la
réplica número 3.

Luego, se define la variable aleatoria ZJ = X1J - X2J, con E(Zj) = ζ = μ1 - μ2 como la cantidad para la
que se constituye el intervalo de confianza (justamente, la esperanza de las diferencias).

1°) Media muestral:

2°) Varianza:

𝑍̅(𝑛) =

𝑍𝑗

𝑛
∑
𝑗=1
𝑛

𝑉𝑎𝑟 ̂[𝑍(𝑛)

̅̅̅̅̅̅] =

2

𝑛
𝑗=1

∑ [𝑍𝑗 − 𝑍̅(𝑛)]
𝑛(𝑛 − 1)

3°) Finalmente, se calcula el intervalo de confianza aproximada de 100 (1-α) %:

𝑍̅ ± 𝑡𝑛−1,1−𝛼/2. √𝑉𝑎𝑟̂ ⌈𝑍̅(𝑛)⌉

NOTA: Si la distribución de los ZJ es normal, entonces el intervalo de confianza es exacto (es
decir, cubre ζ con una confianza de 1-α). Sino, basándonos en el Teorema Central del Límite,
hay que usar un n alto para que la distribución se aproxime a la normal.

--------------------------------------------

NÚMEROS ALEATORIOS

En general, los números aleatorios surgen de alguna fuente de aleatoriedad física impredecible.
Generar números pseudoaleatorios implica generar secuencias de números que “parezcan”
aleatorias (variable aleatoria IID).

Apunte NO oficial – Joel Arnold – Marzo 2021

Características de un buen generador de números aleatorios

  Que no muestre ningún patrón o regularidad aparente desde un punto de vista estadístico.

  Que, dada una semilla inicial, se puedan generar muchos valores antes de repetir el ciclo.

Generador congruencial lineal

Tiene la forma:

𝑋𝑛+1 = (𝑎. 𝑋𝑛 + 𝐶) 𝑚𝑜𝑑 (𝑚)

Parámetros:

 Módulo: m (>0)

 Multiplicador: a (0 < a < m)

 Incremento: c (≤ X0 < m)

 Semilla: X0 (0 ≤ X0 < m)

En cada iteración, el número aleatorio generado es:

𝑈𝑖 =

𝑋𝑛 + 1
𝑚

Características importantes

  La  longitud  del  ciclo  depende  de  m  ya  que  el  generador  no  puede  producir  más  de  m

elementos.

  El  tamaño  de  m  influye  en  la  velocidad  del  generador  porque  m  muy  grande  puede

requerir mucha capacidad de cómputo.

  La longitud del ciclo (p) se denomina período y cuando p = m el generador es de “período

completo”.

G.C.L. sea de período completo

 M y c tienen que ser primos relativos (único divisor común --> 1).

 Si q es un número primo que divide a m, también tiene que dividir a “a – 1”.

 Si 4 divide a m, entonces también divide a “a – 1”.

Apunte NO oficial – Joel Arnold – Marzo 2021

Prueba de test aleatoriedad Chi-cuadrado (χ2):

1)  Se divide el intervalo [0,1] en c subintervalos.

2)  Se generan n números aleatorios.

3)  Se calcula:

𝑐
𝑋2 = ∑
𝑖=1

(𝑜𝑖 − 𝑒𝑖)2
𝑒𝑖

Siendo:

𝒏
 : el valor esperado en cada subintervalo

  𝒆𝒊 =
  𝒐𝒊 : cantidad de observaciones que se efectivamente se encuentran en el

𝒄

subintervalo i.

4)  Finalmente podemos decir, con un grado de confianza 100.(1 - α)%, que Ui es una variable
c-1,1-α” (valor crítico

aleatoria IID si lo calculado en el punto anterior es menos al valor “χ2
superior de la distribución chi-cuadrado con “c-1” grados de libertad).

Apunte NO oficial – Joel Arnold – Marzo 2021

