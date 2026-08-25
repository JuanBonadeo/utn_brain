UNIVERSIDAD TECNOLÓGICA NACIONAL
FACULTAD REGIONAL ROSARIO
SIMULACIÓN
Autor: Pagliaro, Luis

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN
Contenido
1. La simulación ........................................................................................................................................................3
1.1. Sistemas, modelos y simulación ....................................................................................................................3
2. Simulación de eventos discretos ..........................................................................................................................4
2.1. Mecanismos de avance en el tiempo ............................................................................................................4
2.2. Componentes y organización de un modelo de simulación de eventos discretos .......................................4
2.3. Diagrama de flujo del mecanismo de avance al próximo evento .................................................................5
3. Simulación de un sistema de espera de un solo servidor ....................................................................................5
3.1 Medidas de desempeño .................................................................................................................................5
3.2 Diagramas de flujo para las rutinas de arribo y partida .................................................................................6
4. Simulación de un sistema de inventario ...............................................................................................................7
4.1. Componentes ................................................................................................................................................7
4.2. Diagramas de flujo para las rutinas ...............................................................................................................8
5. Etapas de un estudio de simulación .....................................................................................................................8
6. Modelos de colas ..................................................................................................................................................9
6.1. Características de un sistema de colas ..........................................................................................................9
6.2. Clasificación de los modelos de colas ......................................................................................................... 10
6.3. Medidas de rendimiento para evaluar un sistema de colas....................................................................... 10
6.3.1. Medidas de rendimiento ..................................................................................................................... 10
6.3.2. Relaciones entre medidas de rendimiento ......................................................................................... 11
7. Análisis de los datos de salida de un único sistema .......................................................................................... 12
7.1. Comportamiento del estado transiente y estacionario de un proceso estocástico .................................. 12
7.2. Tipos de simulación respecto al análisis de los datos de salida ................................................................. 12
7.3. Análisis estadístico para simulaciones terminales ..................................................................................... 12
7.3.1. Estimación de la media ........................................................................................................................ 12
7.3.2. Eligiendo condiciones iniciales ............................................................................................................ 14
8. Medidas múltiples de rendimiento ................................................................................................................... 14
9. Comparando configuraciones de sistemas alternativos ................................................................................... 14
9.1. Intervalos de confianza para la diferencia entre las medidas de rendimiento de dos sistemas ............... 14
9.1.1. Intervalo de confianza t-apareado ...................................................................................................... 14
9.1.2. Intervalo de confianza de Welch ......................................................................................................... 15
9.2. Intervalos de confianza para comparar más de dos sistemas .................................................................... 15
9.2.1. Método de ranking y selección ........................................................................................................... 15
10. Método de media de lotes .............................................................................................................................. 16
11. Números aleatorios comunes.......................................................................................................................... 16
Pagliaro, Luis 2

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN
1. La simulación
Llamamos sistema a un proceso de interés, y para estudiarlo científicamente tenemos que hacer suposiciones
de cómo funciona.
Estas suposiciones que usualmente toman forma de relaciones lógicas o matemáticas, constituyen un modelo
que se usa para tratar de obtener un entendimiento de cómo el sistema se comporta.
Si las relaciones que componen éste modelo son simples, podría ser posible usar métodos matemáticos para
obtener la información exacta de las preguntas de interés; a esto se le llama una solución analítica. Sin
embargo, la mayoría de los sistemas del mundo real son demasiados complejos para ser evaluados
analíticamente, por lo que deben ser estudiados por simulación
1.1. Sistemas, modelos y simulación
Un sistema se define como una colección de entidades, como gente o máquinas, que actúan e interactúan
juntos para lograr un objetivo lógico. En la práctica, lo que se refiere a “sistemas” depende de los objetivos de
un estudio en particular.
Definimos el estado de un sistema como una colección de variables necesarias para describir un sistema en
un momento en particular, relativo a los objetivos del estudio.
Categorizaremos a los sistemas en dos tipos: discretos y continuos. Un sistema discreto es aquel para el cual
las variables de estado cambian instantáneamente en puntos de tiempo separados. Un sistema continuo es
aquel para el cual las variables de estado cambian continuamente respecto al tiempo.
En algún punto en la vida de la mayoría de los sistemas, hay una necesidad de estudiarlos para lograr una
comprensión en las relaciones entre varios componentes:
• Experimentar con el sistema real vs. Experimentar con un modelo del sistema:
Si es posible (y rentable), alterar el sistema físicamente y luego dejarlo operar bajo las nuevas condiciones. Sin
embargo, raramente se hace esto, porque tal experimento costaría demasiado o perjudicaría al sistema.
Usualmente es necesario construir un modelo como representación del sistema y estudiarlo como reemplazo
del sistema real. Cuando usamos un modelo, siempre está la pregunta de si refleja con precisión al sistema
para los propósitos de las decisiones a ser tomadas.
• Modelo físico vs. Modelo matemático:
Los modelos físicos no son del típico tipo de modelos que son de interés en búsqueda de operaciones y
análisis de sistemas.
Los modelos matemáticos representan a un sistema en términos de relaciones lógicas y cuantitativas que
luego son manipuladas y cambiadas para ver cómo el modelo reacciona, y por consiguiente, cómo reaccionaría
si el modelo matemático es válido.
• Soluciones analíticas vs. Simulación:
Una vez que construimos el modelo matemático, luego debe ser examinado para ver cómo puede ser usado
para responder las preguntas de interés sobre el sistema que se supone representa. Si el modelo es simple,
podría ser posible trabajar con sus relaciones y cantidades para obtener una solución exacta, analítica.
Sin embargo, muchos sistemas son altamente complejos, por lo que modelos matemáticos válidos de ellos
son también complejos, descartando toda posibilidad de una solución analítica. En éste caso, el modelo debe
ser estudiado por medio de la simulación, trabajando numéricamente el modelo para las entradas en cuestión
para ver cómo afectan las medidas de desempeño de salida.
Pagliaro, Luis 3

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN
Dado que tenemos un modelo matemático a ser estudiado por medio se simulación, debemos buscar
herramientas particulares para hacer esto. Es útil para éste propósito clasificar los modelos de simulación por
tres diferentes dimensiones:
• Simulación de modelos estática vs. dinámica:
Una simulación estática de un modelo es una representación de un sistema en un momento particular, o uno
que puede ser usado para representar un sistema en el cual el tiempo no juega ningún papel. Una simulación
dinámica de un modelo representa un sistema mientras evoluciona en el tiempo.
• Simulación de modelos determinística vs. estocástica:
Si un modelo de simulación no posee componentes probabilísticos, se llama determinístico. Si un modelo de
simulación tiene componentes de entrada aleatorios se llama estocástico.
• Simulación de modelos discretos vs. continuos:
Se define análogamente a sistemas discretos y continuos.
2. Simulación de eventos discretos
La simulación de eventos discretos concierne el modelado de un sistema mientras evoluciona en el tiempo
por una representación en el cual las variables de estado cambian instantáneamente en puntos de tiempo
separados. Estos puntos en el tiempo son en los cuales los eventos ocurren; donde un evento se define como
una ocurrencia instantánea que podría cambiar el estado del sistema.
2.1. Mecanismos de avance en el tiempo
Debido a la naturaleza de los modelos de simulación de eventos discretos, debemos hacer un seguimiento del
valor actual del tiempo simulado mientras la simulación procede, también necesitamos un mecanismo para
avanzar el tiempo simulado de un valor a otro. Llamamos a la variable que da el valor actual del tiempo
simulado, reloj de simulación.
Se han sugerido dos métodos para avanzar el reloj de simulación: avance al próximo evento y avance de
tiempo a incremento fijo.
Con el avance de tiempo al próximo evento, el reloj de simulación es inicializado en cero y los tiempos de
ocurrencia de eventos futuro son determinados. El reloj de simulación avanza al tiempo de ocurrencia del
evento futuro más inminente, a tal punto, el estado del sistema se actualiza por el hecho de que tal evento ha
ocurrido, y nuestro conocimiento de los tiempos de ocurrencia de eventos futuros es actualizado. Luego, el
reloj de simulación avanza al tiempo de evento más inminente, el estado del sistema es actualizado y tiempo
de eventos futuros son determinado.
2.2. Componentes y organización de un modelo de simulación de eventos discretos
• Estado del sistema: es la colección de variables de estado necesarias para describir al sistema en un tiempo
particular.
• Reloj de simulación: variable que da el valor actual del tiempo simulado.
• Lista de eventos: lista que contiene el próximo tiempo en que cada tipo de evento ocurrirá.
• Contadores estadísticos: variables utilizadas para almacenar información estadística sobre el desempeño del
sistema.
• Rutina de inicialización: es un subprograma que inicializa el modelo de simulación al tiempo cero.
• Rutina de tiempo: subprograma que determina el próximo evento de la lista de eventos y luego actualiza el
reloj de simulación al tiempo donde este evento ocurrirá.
Pagliaro, Luis 4

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN
• Rutina de eventos: subprograma que actualiza el estado del sistema cuando un tipo de evento particular
ocurre.
• Rutina de librería: conjunto de subprogramas utilizados para generar observaciones aleatorias de
distribuciones de probabilidad que fueron determinadas como parte del modelo de simulación.
• Generador de reportes: es un subprograma que computa estimadores de las medidas de desempeño
deseadas y produce un reporte cuando la simulación termina.
• Programa principal: es un subprograma que invoca la rutina de tiempo para determinar el próximo evento y
luego transfiere el control a la rutina de evento correspondiente para actualizar apropiadamente el estado del
sistema. El programa principal podría también comprobar la terminación e invocar al generador de reportes
cuando la simulación finalice.
2.3. Diagrama de flujo del mecanismo de avance al próximo evento
Comienzo
Rutina de inicialización
Programa principal
1. Establecer el reloj de simulación en 0. 0 0. Invocar la rutina de inicialización. Rutina de tiempos
2. Inicializar variables del sistema y 1. Invocar la rutina de tiempos. 1
contadores estadísticos. 2. Invocar la rutina de evento i. 1. Determinar el próximo tipo de evento (i).
3. Inicializar la lista de eventos. 2. Avanzar el reloj de simulación.
i
Rutina de evento i 2
1. Actualizar el estado del sistema. Rutina de librería
2. Actualizar contadores estadísticos.
Generar variaciones aleatorias
3. Generar eventos futuros y agregarlos a la
lista de eventos.
No
¿Terminó la
simulación?
Sí
Generador de reporte
1. Computar estimadores de interés.
2. Escribir el reporte.
Fin
3. Simulación de un sistema de espera de un solo servidor
3.1 Medidas de desempeño
Para medir el desempeño del sistema, observaremos estimadores de tres cantidades. Primero, estimaremos
la demora promedio en cola esperada de los clientes que completaron sus demoras durante la simulación.
Denotamos esta cantidad como . De una corrida de simulación, resultan las demoras , por lo
𝑛𝑛
tanto, el estimador es:
𝑑𝑑(𝑛𝑛) 𝐷𝐷1,𝐷𝐷2,…,𝐷𝐷𝑛𝑛
𝑛𝑛
∑𝑖𝑖=1𝐷𝐷𝑖𝑖
𝑑𝑑̂(𝑛𝑛) =
Otra medida de rendimiento es el número promedio de clientes en cola esperado, denotada . Para
𝑛𝑛
definir esta medida utilizaremos los valores , el número de clientes en cola en el tiempo y , el
𝑞𝑞(𝑛𝑛)
tiempo requerido para observar las demoras en cola. Entonces:
𝑄𝑄(𝑡𝑡) 𝑡𝑡 𝑇𝑇(𝑛𝑛)
𝑛𝑛
Pagliaro, Luis 5

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN
𝑇𝑇(𝑛𝑛)
∫0 𝑄𝑄(𝑡𝑡)𝑑𝑑𝑡𝑡
𝑞𝑞�(𝑛𝑛) =
La tercera medida de desempeño es una medida de cua𝑇𝑇n (o𝑛𝑛c)upado está el servidor. La utilización del servidor
es la proporción esperada de tiempo durante la simulación que el servidor está ocupado, denotado .
Definimos la función “ocupado”:
𝑢𝑢(𝑛𝑛)
1 si el servidor está ocupado en el tiempo 𝑡𝑡
𝐵𝐵(𝑡𝑡) = �
Entonces: 0 si el servidor está desocupado en el tiempo 𝑡𝑡
𝑇𝑇(𝑛𝑛)
∫0 𝐵𝐵(𝑡𝑡)𝑑𝑑𝑡𝑡
𝑢𝑢�(𝑛𝑛) =
3.2 Diagramas de flujo para las rutinas de arribo y𝑇𝑇 p(𝑛𝑛a)rtida
Evento partida
Evento arribo
Sí ¿Cola vacia? No
Planificar el próximo
evento arribo
Establecer el Computar demora
servidor como del cliente que
desocupado entra y acumular
estadísticos
¿Servidor
Sí No
ocupado?
Eliminar el evento
Sustraer 1 del
partida de
Agregar 1 al número Establecer demora consideración número de clientes
en 0 para éste en cola
de clientes en cola
cliente y acumular
estadísticos
Agregar 1 al número
de clientes que
Almacenar tiempo completaron su
Agregar 1 al número
de arribo de éste demora
de clientes que
cliente
completaron su
demora Planificar un evento
partida para éste
cliente
Establecer el
servidor como
ocupado
Mover cada cliente
en la cola un lugar
Planificar un evento
partida para éste
cliente
Volver Volver
Pagliaro, Luis 6

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN

4. Simulación de un sistema de inventario
4.1. Componentes
•  Tiempos entre demandas.
| •  Tamaño de las demandas ( |     | ).  |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- |
•  Costo del pedido:  , donde   es el costo base,   es el costo incremental por ítem y   la cantidad
𝐷𝐷
pedida.
|     | 𝑘𝑘+(𝑖𝑖∗𝑍𝑍) | 𝑘𝑘  |     | 𝑖𝑖  | 𝑍𝑍  |
| --- | ---------- | --- | --- | --- | --- |
•  Retardo de envío: tiempo requerido para que llegue un pedido.
•  Política estacionaria  :  , donde   es el nivel de inventario al momento de la
| evaluación de inventario.        |         | 𝑆𝑆−𝐼𝐼 si 𝐼𝐼     | < 𝑠𝑠 |     |     |
| -------------------------------- | ------- | --------------- | ---- | --- | --- |
|                                  | (𝑠𝑠,𝑆𝑆) | 𝑍𝑍 = �          |      | 𝐼𝐼  |     |
|                                  |         | 0  s i  𝐼𝐼 ≥    | 𝑠𝑠   |     |     |
| •  Nivel de inventario a tiempo  |         | , deno t a d o  | .    |     |     |
•  Número de ítems en posesión en el inventario a tiempo  :  .
|     |     | 𝑡𝑡  | 𝐼𝐼(𝑡𝑡) |     |     |
| --- | --- | --- | ------ | --- | --- |
•  Número de ítems faltantes en el inventario a tiempo  :  + .
𝑡𝑡 𝐼𝐼 (𝑡𝑡) = 𝑚𝑚𝑚𝑚𝑚𝑚{𝐼𝐼(𝑡𝑡),0}
•  Costo de mantenimiento de ítems por unidad de tiempo−, denotado .
|     |     |     |     | 𝑡𝑡 𝐼𝐼 (𝑡𝑡) = 𝑚𝑚𝑚𝑚𝑚𝑚{−𝐼𝐼(𝑡𝑡),0} |     |
| --- | --- | --- | --- | ------------------------------ | --- |
•  Número de ítems en el inventario para el  -ésimo período de tiemp oℎ:  .
𝑛𝑛
+
+ ∫0 𝐼𝐼 (𝑡𝑡)𝑑𝑑𝑡𝑡
•
Promedio de costo de mantenimiento por𝑛𝑛 unidad de tiempo:  .  𝐼𝐼 = 𝑛𝑛
•  +
| Costo de faltante de ítems por unidad de tiempo, denotado  |     |     |     | .   |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- |
ℎ∗𝐼𝐼
•  Número de ítems faltantes en el inventario para el  -ésimo p𝜋𝜋eríodo de tiempo:  .
𝑛𝑛 −
− ∫0 𝐼𝐼 (𝑡𝑡)𝑑𝑑𝑡𝑡
•
| Promedio de costo de faltante por unidad de tiempo:  |     |     |     | .       |     |
| ---------------------------------------------------- | --- | --- | --- | ------- | --- |
|                                                      |     |     |     | 𝑛𝑛 𝐼𝐼 = | 𝑛𝑛  |
−
𝜋𝜋∗𝐼𝐼
| Pagliaro, Luis  |     |     |     |     |   7  |
| --------------- | --- | --- | --- | --- | ---- |

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN
4.2. Diagramas de flujo para las rutinas
Evento evaluación
de inventario
Sí ¿Es I(t) < s? No
Evento demanda
Determinar la
cantidad a ordenar
(S - I(t))
Generar el tamaño
Evento arribo de
de esta demanda Calcular el costo del
una orden
pedido y acumular
Incrementar el nivel Disminuir el nivel Determinar el
del inventario en la del inventario por el evento arribo de
cantidad tamaño de esta una orden para esta
previamente demanda orden
ordenada
Definir cuándo será
Eliminar el evento
el siguiente evento
arribo de una orden
demanda Determinar el próximo evento
de consideración
evaluación de inventario
Volver Volver Volver
5. Etapas de un estudio de simulación
1. Formular el problema y planificar el estudio:
Cada estudio debe comenzar con una declaración de los objetivos. Los diseños alternativos del sistema a ser
estudiado deber ser delineados, y los criterios para evaluar la eficacia de estas alternativas deben ser dados. El
estudio debe ser planteado en términos del número de personas, el costo y el tiempo requerido para cada
aspecto del estudio.
2. Recolectar datos y definir el modelo:
Información y datos deben ser recolectados del sistema de interés y deben ser usado para especificar
procedimientos para operar y distribuciones de probabilidad para las variables aleatorias usadas en el modelo.
3. ¿Es válido el modelo?
Es imperativo para el modelador involucrar personas en el estudio relacionadas con el uso actual del sistema.
También debería haber interacción con la persona que toma las decisiones. En adición, la adecuación de las
distribuciones de probabilidad especificadas para generar variables de entrada aleatorias debería ser
comprobada usando la prueba de bondad de ajuste.
4. Construir un programa de computadora y verificar:
Se debe decidir si usar un lenguaje de programación de propósitos generales o uno diseñado para
simulaciones.
5. Hacer corridas piloto:
Pagliaro, Luis 8

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN
Se hacen corridas piloto del modelo verificado por propósito de validación.
6. ¿Es válido el modelo?
Las corridas piloto pueden ser usadas para probar la sensibilidad de la salida del modelo ante pequeños
cambios en un parámetro de entrada. Si la salida cambia significantemente, un mejor estimador para el
parámetro de entrada debe ser obtenido.
7. Diseño de experimentos:
Para cada diseño del sistema a ser simulado, se tienen que tomar decisiones en temas como las condiciones
iniciales de las corridas de la simulación, la longitud del período de calentamiento, la longitud de las corridas de
la simulación y el número de corridas independientes de la simulación para cada alternativa.
8. Realizar corridas de producción:
Las corridas de producción se hacen para proveer datos sobre el desempeño de los diseños del sistema.
9. Analizar los datos de salida:
Se utiliza un intervalo de confianza para una medida de desempeño para un diseño en particular del sistema
o para decidir qué sistema simulado es mejor relativo a alguna medida de desempeño especificada.
10. Documentar, presentar e implementar resultados:
Es importante documentar las cosas que se asumieron en el modelo, así como el programa.
6. Modelos de colas
6.1. Características de un sistema de colas
• Población de clientes: conjunto de todos los posibles clientes de un sistema de colas. Para problemas en
donde el número de clientes potenciales es bastante grande (cientos o miles), el tamaño de la población se
considera como si fuera infinito.
• Proceso de llegada: es la forma en que los clientes llegan a solicitar un servicio. La característica principal del
proceso de llegada es el tiempo entre llegadas, que es el intervalo de tiempo que existe entre dos llegadas
sucesivas. Mientras menor sea el intervalo de tiempo, con más frecuencia llegarán los clientes, lo cual aumenta
la demanda de servidores disponibles. Existen dos clases de tiempos entre llegadas: determinísticos, en el que
los clientes sucesivos llegan en un mismo intervalo de tiempo, fijo y conocido; y probabilístico, en el que el
tiempo entre llegadas sucesivas es incierto y variable. Se describe mediante una distribución de probabilidad.
• Proceso de colas: es la forma en que los clientes esperan para ser atendidos. Si los clientes esperan en una
sola línea para tener acceso al siguiente prestador de servicio disponible en el sistema, el sistema se llama de
colas de una solo línea. Si los clientes pueden elegir entre varias filas en la que deben esperar a ser atendidos,
el sistema es de colas de líneas múltiples.
Otra característica del proceso de colas es el número de espacios de espera en cada fila, es decir, el número
de clientes que pueden esperar (o que esperarán) para ser atendidos en cada línea. Este número puede ser
finito o infinito.
Otra característica del proceso de colas es la disciplina de colas, es decir, la forma en que los clientes que
esperan son seleccionados para ser atendidos. Estas pueden ser: FIFO, LIFO o selección por prioridad.
• El proceso de servicio: es la forma en que los clientes son atendidos. Puede existir más de una estación en el
sistema en la cual se proporcione el servicio requerido. Los sistemas pueden ser de colas de canal múltiple, en
los cuales los clientes que llegan pueden pasar a una de varias estaciones de trabajo posibles; y sistemas de
colas de canal sencillo, en los cuales los clientes que llegan pasan por una sola estación de trabajo.
En los sistemas de canal múltiple, los servidores pueden ser idénticos, en el sentido de que proporcionan el
mismo servicio, o no idénticos. En los sistemas de canal sencillo pueden existir muchos servidores, que juntos,
llevan a cabo la tarea necesaria.
Pagliaro, Luis 9

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN
Otra característica del proceso de servicio es el número de clientes atendidos al mismo tiempo en una
estación.
Otra característica más de un proceso de servicio es si se permite o no la prioridad, esto es si un servidor
puede detener el proceso con el cliente que está atendiendo para dar lugar a un cliente que acaba de llegar.
Cualquiera que sea el proceso de servicio, es necesario tener una idea de cuánto tiempo se requiere para
llevar a cabo el servicio. Esta cantidad es importante debido a que cuanto más dure el servicio, más tendrán
que esperar los clientes que llegan. Este tiempo se denomina tiempo de servicio, y puede ser determinístico, en
el que cada cliente requiere la misma cantidad conocida de tiempo para ser atendido; y probabilístico, en el
que cada cliente requiere una cantidad distinta e incierta de tiempo de servicio.
6.2. Clasificación de los modelos de colas
La notación utilizada para describir los modelos de colas es la notación Kendall. En ella se describe el proceso
de llegada, el proceso de servicio, el proceso de colas, la cantidad de clientes en el sistema y la cantidad de
clientes de la población.
• Proceso de llegada: estos símbolos describen la distribución de tiempos entre llegadas:
D: tiempos entre llegadas determinísticos.
o
M: tiempos entre llegadas probabilísticos con distribución exponencial.
o
G: tiempos entre llegadas probabilísticos con distribución general.
o
• Proceso de servicio: estos símbolos describen la distribución de tiempos de servicio:
D: tiempos de servicio determinísticos.
o
M: tiempos de servicio probabilísticos con distribución exponencial.
o
G: tiempos de servicio probabilísticos con distribución general.
o
• Proceso de colas: este número, , representa cuantas estaciones paralelas existen en el sistema.
• Un número , que representa el número máximo de clientes que pueden estar en el sistema en cualquier
𝑐𝑐
momento.
𝐾𝐾
• Un número , que representa el número total de clientes de la población.
𝐿𝐿
Cuando se omite alguno de los símbolos, se considera que el número es infinito.
6.3. Medidas de rendimiento para evaluar un sistema de colas
Cualquier sistema de colas pasa por dos fases lógicas. La fase transitoria, que es el período inicial de un
sistema de colas en que se conservan los efectos de las condiciones iniciales, y la fase de estado estable, que es
la condición del sistema después de que se han eliminado las condiciones iniciales.
Todos los modelos analíticos son válidos siempre que el sistema haya llegado al estado estable.
6.3.1. Medidas de rendimiento
Las medidas de rendimiento son un valor numérico que se utiliza para evaluar los méritos de un sistema de
colas en estado estable.
• Tiempo promedio de espera en cola ( ): tiempo promedio que un cliente que llega tiene que esperar en la
cola antes de ser atendido.
𝑊𝑊𝑞𝑞
• Tiempo promedio en el sistema ( ): tiempo promedio que un cliente invierte desde su llegada hasta su
salida en un sistema de colas.
𝑊𝑊
• Longitud media de la cola ( ): número promedio de clientes que se encuentran en la fila esperando a ser
atendidos.
𝐿𝐿𝑞𝑞
Pagliaro, Luis 10

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN
• Número medio de clientes en el sistema ( ): número promedio de clientes que se encuentran en el sistema
en cualquier tiempo dado.
𝐿𝐿
• Probabilidad de bloqueo ( ): probabilidad de que un cliente que llega tenga que esperar a ser atendido.
• Utilización del servidor ( ): fracción de tiempo, en promedio, que un servidor está ocupado.
𝑃𝑃𝑤𝑤
• Distribución de probabilidad de estado: probabilidad de que se encuentren clientes en el sistema de colas
𝑈𝑈
cuando está estable.
𝑛𝑛
• Probabilidad de negación de servicio ( ): probabilidad de que un cliente que llega no pueda entrar al
sistema debido a que la cola está llena.
𝑃𝑃𝑖𝑖
6.3.2. Relaciones entre medidas de rendimiento
Siendo:
número promedio de llegadas por unidad de tiempo
número p𝜆𝜆ro=medio de clientes atendidos por unidad de tiempo en una estación
Podemos def𝜇𝜇in=ir las siguientes relaciones:
1
𝑊𝑊 = 𝑊𝑊𝑞𝑞 +
𝜇𝜇
𝐿𝐿 = 𝜆𝜆∗𝑊𝑊
𝐿𝐿𝑞𝑞 = 𝜆𝜆∗𝑊𝑊𝑞𝑞
Pagliaro, Luis 11

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN

7. Análisis de los datos de salida de un único sistema
7.1. Comportamiento del estado transiente y estacionario de un proceso estocástico
Sean   procesos estocásticos de salida y   para  , donde   es un
número real e   representa las condiciones iniciales para iniciar la simulación a tiempo  . Llamamos a
|     | 𝑌𝑌1,𝑌𝑌2,… |     |     |     |     | 𝐹𝐹𝑖𝑖(𝑦𝑦|𝐼𝐼) | = 𝑃𝑃(𝑌𝑌𝑖𝑖  ≤ 𝑦𝑦|𝐼𝐼) | 𝑖𝑖 = 1,2,… |     | 𝑦𝑦  |     |
| --- | --------- | --- | --- | --- | --- | ----------- | ------------------- | ---------- | --- | --- | --- |
distribución de estado transiente del proceso estocástico de salida a tiempo discreto   para las condiciones
|     |     | 𝐼𝐼  |     |     |     |     |     |     | 0   |     | 𝐹𝐹𝑖𝑖(𝑦𝑦|𝐼𝐼) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- |
iniciales  . Si   cuando  , para toda   y para cualquier condición inicial  , entonces,   se
𝑖𝑖
llama distribución de estado estacionario de los procesos estocásticos de salida  .
𝐹𝐹𝑖𝑖(𝑦𝑦|𝐼𝐼)
|     | 𝐼𝐼  |     | → 𝐹𝐹(𝑦𝑦) | 𝑡𝑡 → | ∞   | 𝑦𝑦  |     |     | 𝐼𝐼  |     | 𝐹𝐹(𝑦𝑦) |
| --- | --- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | ------ |
7.2. Tipos de simulación respecto al análisis de los datos de salida  𝑌𝑌1,𝑌𝑌2,…
Las operaciones disponibles al diseñar y analizar experimentos de simulación dependen del tipo de
simulación. Los tipos de simulación son: terminal y no terminal.
Una simulación terminal es una en la cual hay un evento “natural”   que especifica la duración de cada
corrida (réplica). El evento   generalmente ocurre en un tiempo más allá del cual no se obtiene información
𝐸𝐸
útil del sistema o en un tiempo en donde el sistema es “limpiado”. Este evento se especifica antes de cualquier
𝐸𝐸
corrida, y el tiempo de ocurrencia del mismo para una corrida es una variable aleatoria. Dado que las
condiciones iniciales para una simulación terminal afectan las medidas de desempeño deseadas, estas
condiciones deberían ser representativas de aquellas para el sistema real.
Una simulación no terminal es aquella para la cual no hay un evento “natural”   que especifique la duración
de una corrida. Dentro de las simulaciones no terminales se tienen varios parámetros para las medidas de
𝐸𝐸
desempeño, estos son: parámetro de estado estacionario, parámetro de ciclo de estado estacionario, otros
parámetros.
Una medida de desempeño es parámetro de estado estacionario si es característica de la distribución de
| estado estacionario de algún proceso estocástico de salida  |     |     |     |     |     |     | .   |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Sean   procesos estocásticos de salida para una sim𝑌𝑌1u,la𝑌𝑌c2i,ó…n no terminal que no tiene una distribución
de estado estacionario. Supongamos que dividimos el eje de tiempo en intervalos continuos y de igual duración
𝑌𝑌1,𝑌𝑌2,…
llamados ciclos. Sea   una variable aleatoria definida en el  -ésimo ciclo, y asumiendo que   son
comparables. Suponga𝑐𝑐mos que los procesos   tienen una distribución de estado estac𝑐𝑐ion𝑐𝑐ario  , tal
|     |     |     | 𝑌𝑌𝑖𝑖 |     |     |     | 𝑖𝑖  |     |     | 𝑌𝑌1,𝑌𝑌2,… |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --------- | --- |
que  . Entonces, una medida de desemp𝑐𝑐eño𝑐𝑐 es parámetro de ciclo de estado estacionario si es
𝑐𝑐
|     |     |     |     |     | 𝑌𝑌1,𝑌𝑌2,… |     |     |     |     |     | 𝐹𝐹  |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
caract𝑐𝑐eríst𝑐𝑐ica de   como  . Por lo tanto, un parámetro de ciclo de estado estacionario es un
𝑌𝑌 ~𝐹𝐹
parámetro de estad𝑐𝑐o estacio𝑐𝑐nario de𝑐𝑐l ciclo apropiado del proceso  .
|                                                         |     |     | 𝑌𝑌 𝑣𝑣 = 𝐸𝐸(𝑌𝑌 | )   |     |     |           |     |     |     |     |
| ------------------------------------------------------- | --- | --- | ------------- | --- | --- | --- | --------- | --- | --- | --- | --- |
|                                                         |     |     |               |     |     |     | 𝑐𝑐        | 𝑐𝑐  |     |     |     |
| 7.3. Análisis estadístico para simulaciones terminales  |     |     |               |     |     |     | 𝑌𝑌1,𝑌𝑌2,… |     |     |     |     |
7.3.1. Estimación de la media
Supongamos que queremos obtener un punto de estimación y un intervalo de confianza para la media
, donde   es la variable aleatoria definida en una réplica. Si hacemos   réplicas independientes de la
|     |     |     |     |     |     |     |     |     |     |     | 𝜇𝜇 = |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
simulación, y   son las variables aleatorias independientes distribuidas idénticamente resultantes.
| 𝐸𝐸[𝑋𝑋] |     | 𝑋𝑋  |     |     |     |     |     | 𝑛𝑛  |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Podemos obtener:
𝑋𝑋1,𝑋𝑋2,…,𝑋𝑋𝑛𝑛

∑𝑋𝑋𝑖𝑖
|     |     |     |     |     |     | 𝑋𝑋𝑛𝑛 = |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
Que es un punto estimador imparcial para , y un intervalo de confianza de   para   es:
𝑛𝑛
|     |                 |     |     |     |  𝜇𝜇 |     |     | 100∗(1−𝛼𝛼) |     |     | 𝜇𝜇    |
| --- | --------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | ----- |
|     | Pagliaro, Luis  |     |     |     |     |     |     |            |     |     |   12  |

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN

2
𝑆𝑆 (𝑛𝑛)
|                                                 |     |     |     |     | 𝑋𝑋𝑛𝑛 | ±𝑡𝑡𝑛𝑛−1,1−𝛼𝛼⁄2� |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | ---- | --------------- | --- | --- | --- | --- |
| Llamamos a esto, procedimiento de tamaño fijo.  |     |     |     |     |      |                 | 𝑛𝑛  |     |     |     |
7.3.1.1. Obtener una precisión especificada
Una desventaja de los procedimientos de tamaño fijo basados en   réplicas es que el analista no tiene control
sobre la mitad del intervalo de confianza; para   fijos, la mitad dependerá de la varianza de la población de los
𝑛𝑛
.
𝑛𝑛
𝑋𝑋𝑗𝑗A continuación desarrollaremos el número de réplicas requeridas para estimar la media
 con un
error específico. Comenzamos definiendo dos formas de medir el error en el estimador  .
𝜇𝜇 = 𝐸𝐸[𝑋𝑋]
Si el estimador   es aquel tal que  , entonces decimos que   tiene un error𝑋𝑋 absoluto de  , con
una probabilidad de  . Supongamos que hemos construido un intervalo de confianza para  basado en un
|     | 𝑋𝑋  |     |     | �𝑋𝑋−𝜇𝜇� | = 𝛽𝛽 |     |     | 𝑋𝑋  |     | 𝛽𝛽  |
| --- | --- | --- | --- | ------- | ---- | --- | --- | --- | --- | --- |
número fijo de   réplicas. Si asumimos que nuestro estimador de la varianza poblacional no cambiará al
|     |     | 1−𝛼𝛼 |     |     |     |     |     |     |  𝜇𝜇 |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
aumentar el número de réplicas, el número total de réplicas,  , requerido para obtener un error absoluto
𝑛𝑛
| de   es:  |     |     |     |     |     |     | ∗   |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑛𝑛𝑎𝑎(𝛽𝛽)
𝛽𝛽

2
|     |     |     |     | ∗        |           |                  |     | 𝑆𝑆 (𝑛𝑛) |     |     |
| --- | --- | --- | --- | -------- | --------- | ---------------- | --- | ------- | --- | --- |
|     |     |     |     | 𝑛𝑛𝑎𝑎(𝛽𝛽) |           | ∶ 𝑡𝑡𝑖𝑖−1,1−𝛼𝛼⁄2� |     |         |     |     |
|     |     |     |     | =        | 𝑚𝑚𝑖𝑖𝑛𝑛�𝑖𝑖 | ≥ 𝑛𝑛             |     | ≤       | 𝛽𝛽� |     |
𝑖𝑖
Otra forma de medir el error en   es si el estimador   es aquel tal que  , entonces decimos
que   tiene un error relativo de  , con una probabilidad de  . Supongamos que hemos construido un
|     |     |     |     | 𝑋𝑋  |     | 𝑋𝑋  |     | �𝑋𝑋−𝜇𝜇��|𝜇𝜇| | = 𝛾𝛾 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | --- |
intervalo de confianza para  basado en un número fijo de   réplicas. Si asumimos que nuestros estimadores
| 𝑋𝑋  |     |     |     | 𝛾𝛾  |     |     | 1−𝛼𝛼 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
de la varianza poblacional y la media poblacional no cambiarán al aumentar el número de réplicas, el número
|                     |     |                                                |  𝜇𝜇 |     |     |     | 𝑛𝑛  |       |     |     |
| ------------------- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- |
| total de réplicas,  |     | , requerido para obtener un error relativo de  |     |     |     |     |     |  es:  |     |     |
∗
|     | 𝑛𝑛𝑟𝑟(𝛾𝛾) |     |     |     |     |     |     | 𝛾𝛾  |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |          |     |     |     |     |     |     | 2   |     |     |
𝑆𝑆 (𝑛𝑛)
|     |     |     |     |     | ⎧   |     | �   |     | ⎫   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | ∗   |     |     |     |     |     | 𝛾𝛾  |     |
𝑖𝑖
|     |     |     | 𝑛𝑛𝑟𝑟(𝛾𝛾) | = 𝑚𝑚𝑖𝑖𝑛𝑛 | 𝑖𝑖 ≥ | 𝑛𝑛 ∶ 𝑡𝑡𝑖𝑖−1,1−𝛼𝛼⁄2 |          | ≤     |     |     |
| --- | --- | --- | -------- | -------- | ---- | ------------------ | -------- | ----- | --- | --- |
|     |     |     |          |          | ⎨    |                    | �𝑋𝑋(𝑛𝑛)� | 1+𝛾𝛾⎬ |     |     |
La dificultad al utilizar la ecuación de  ⎩ directamente para obtener un estim⎭ador de   con un error
relativo de   es que   y   podría∗n no ser estimadores precisos de sus correspondiente parámetros de
𝑛𝑛𝑟𝑟(𝛾𝛾)
𝑋𝑋
población. Si   es más gr2ande que el número de réplicas requeridas, entonces, un número significante de
| 𝛾𝛾  |     | 𝑋𝑋(𝑛𝑛) | 𝑆𝑆 (𝑛𝑛) |     |     |     |     |     |     |     |
| --- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
réplicas innece∗sarias se pueden haber producido, desperdiciando recursos computacionales. Contrariamente,
𝑛𝑛𝑟𝑟(𝛾𝛾)
si   es muy chico, el  estimador de   basado en   réplicas podría no ser preciso. Por esto se utiliza un
proc∗edimiento secuencial (nuevas réplicas son agregad∗as una a la vez) para obtener un estimador de   con un
| 𝑛𝑛𝑟𝑟(𝛾𝛾) |     |     |     |     |     | 𝑛𝑛𝑟𝑟(𝛾𝛾) |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
𝑋𝑋
error relativo específico que solo tomas tantas réplicas como se necesiten.
𝜇𝜇
Para realizar el procedimiento secuencial, elegimos un número inicial de réplicas  , y sea
 el intervalo de confianza de mitad de tamaño, hacemos:  𝑛𝑛0 ≥ 2 𝛿𝛿(𝑛𝑛,𝛼𝛼) =
2
𝑆𝑆 (𝑛𝑛)
| 𝑡𝑡𝑛𝑛 − 1, 1− 𝛼𝛼 ⁄ 2� |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 ré𝑛𝑛plicas de la simulación y fijar
| 1 .  H a ce r   |        |           |      |                |      | .   |     |     |     |       |
| --------------- | ------ | --------- | ---- | -------------- | ---- | --- | --- | --- | --- | ----- |
| 2. Computar     |        |  y        |  de  |                | .    |     |     |     |     |       |
| 𝑛𝑛0             |        |           |      |                | 𝑛𝑛 = | 𝑛𝑛0 |     |     |     |       |
|                 | 𝑋𝑋(𝑛𝑛) | 𝛿𝛿(𝑛𝑛,𝛼𝛼) |      | 𝑋𝑋1,𝑋𝑋2,…,𝑋𝑋𝑛𝑛 |      |     |     |     |     |       |
| Pagliaro, Luis  |        |           |      |                |      |     |     |     |     |   13  |

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN

3. Si   , usar   como punto de estimación de   y parar. Si no reemplazar a   por
𝛾𝛾
, hacer una réplica adicional y volver al paso 1.
| 𝛿𝛿(𝑛𝑛,𝛼𝛼)⁄�𝑋𝑋(𝑛𝑛)� | ≤   | 𝑋𝑋(𝑛𝑛) |     |     |     | 𝜇𝜇  |     | 𝑛𝑛  | 𝑛𝑛+ |
| ------------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
1+𝛾𝛾
17.3.2. Eligiendo condiciones iniciales
Las medidas de rendimiento para una simulación terminal dependen explícitamente del estado del sistema a
tiempo  , por lo que se debe tener cuidado al elegir las condiciones iniciales.
8. Medidas múltiples de rendimiento  0
Supongamos que   es un intervalo de confianza de   por ciento para la medida de rendimiento
 de una simulación terminal o no terminal. Entonces, la probabilidad de que todos los
|     | 𝐼𝐼𝑠𝑠 |     |     | 100(1−𝛼𝛼) |     |     |     |     |     |
| --- | ---- | --- | --- | --------- | --- | --- | --- | --- | --- |
intervalos contengan simultáneamente sus respectivas medidas satisface:
| 𝜇𝜇𝑠𝑠 (𝑠𝑠 = 1,2,…,𝑘𝑘) |     |     |     |     |     |     |     | 𝑘𝑘  |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

𝑘𝑘
|     |     | 𝑃𝑃(𝜇𝜇𝑠𝑠 | ∈ 𝐼𝐼𝑠𝑠∀ 𝑠𝑠 | = 1,2,…,𝑘𝑘) | ≥ 1−�𝛼𝛼𝑠𝑠 |     |     |     |     |
| --- | --- | ------- | ---------- | ----------- | --------- | --- | --- | --- | --- |
Este resultado se conoce como inecuación de Bonferroni. Esta inecua𝑠𝑠=ci1ón tiene un problema, supongamos
que se construye un intervalo de confianza de   por ciento de confianza, esto es   para todas las
para diez medidas de rendimiento distintas. Entonces, la probabilidad de que cada uno de los diez intervalos
𝛼𝛼𝑠𝑠
|     |     |     | 90  |     |     |     | = 0,1 |     | 𝑠𝑠  |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
contenga su medida de rendimiento verdadera sólo puede ser más grande o igual a cero. Por lo tanto, no se
puede tener mucha confianza al sacar conclusiones. Para solucionar el problema anterior de cuando   es chico,
si uno quiere el nivel de confianza asociado a   intervalos, que tengan al menos una confianza de
𝑘𝑘
por ciento, elegimos los   tal que  . Se recomienda que   no sea mayor que  .
|     |     |     | 𝑘𝑘  |     |     |     |     | 100(1−𝛼𝛼) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
𝑘𝑘
|     | 𝛼𝛼𝑠𝑠 | ∑𝑠𝑠=1𝛼𝛼𝑠𝑠 | = 𝛼𝛼 |     |     | 𝑘𝑘  | 10  |     |     |
| --- | ---- | --------- | ---- | --- | --- | --- | --- | --- | --- |
9. Comparando configuraciones de sistemas alternativos
9.1. Intervalos de confianza para la diferencia entre las medidas de rendimiento de dos
sistemas
Para  , sea   observaciones  independientes distribuidas idénticamente del sistema  ,
y sea   el valor de interés, queremos construir un intervalo de confianza para  .
| 𝑖𝑖 = 1,2 | 𝑋𝑋𝑖𝑖1,𝑋𝑋𝑖𝑖2,…,𝑋𝑋𝑖𝑖𝑛𝑛𝑖𝑖,𝑛𝑛𝑖𝑖 |     |     |     |     |     |     |     | 𝑖𝑖  |
| -------- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
9.1.1.𝜇𝜇 I𝑖𝑖n=ter𝐸𝐸v(a𝑋𝑋lo𝑖𝑖𝑗𝑗 )de confianza t-apareado  𝜉𝜉 = 𝜇𝜇1−𝜇𝜇2
Este método no requiere que   y   sean independientes. Si  , podemos emparejar   con
|  para definir   |     | , para      |     | .   |     |            |     |       |     |
| --------------- | --- | ----------- | --- | --- | --- | ---------- | --- | ----- | --- |
|                 |     | 𝑋𝑋1𝑗𝑗 𝑋𝑋2𝑗𝑗 |     |     | 𝑛𝑛1 | = 𝑛𝑛2 = 𝑛𝑛 |     | 𝑋𝑋1𝑗𝑗 |     |
𝑋𝑋2E𝑗𝑗ntonces, los  𝑍𝑍 𝑗𝑗so=n  v𝑋𝑋a1r𝑗𝑗ia−bl e𝑋𝑋s 2a𝑗𝑗leatoria𝑗𝑗s =ind1e,p2e,…nd,i𝑛𝑛entes distribuidas idénticamente y  . Por lo tanto,
podemos hacer:
|     | 𝑍𝑍𝑗𝑗 |     |     |     |     |     | 𝐸𝐸�𝑍𝑍𝑗𝑗� |     |     |
| --- | ---- | --- | --- | --- | --- | --- | -------- | --- | --- |
|     |      |     |     |     |     |     | =        | 𝜉𝜉  |     |

𝑛𝑛
∑𝑗𝑗=1𝑍𝑍𝑗𝑗
|     |     |     |     | 𝑍𝑍(𝑛𝑛) = | 𝑛𝑛  |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |

𝑛𝑛
2
|     |     |     |                 | [𝑍𝑍𝑗𝑗 | −𝑍𝑍(𝑛𝑛)] |     |     |     |     |
| --- | --- | --- | --------------- | ----- | -------- | --- | --- | --- | --- |
|     |     |     | 𝑉𝑉�𝑚𝑚𝑉𝑉�𝑍𝑍(𝑛𝑛)� | = �   |          |     |     |     |     |
𝑛𝑛∗(𝑛𝑛−1)
| Y formamos el intervalo de confianza para  |     |     | :   | 𝑗𝑗=1 |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
𝜉𝜉

𝑍𝑍(𝑛𝑛)±𝑡𝑡𝑛𝑛−1,1−𝛼𝛼⁄2�𝑉𝑉�𝑚𝑚𝑉𝑉�𝑍𝑍(𝑛𝑛)�
| Pagliaro, Luis  |     |     |     |     |     |     |     |     | 14  |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN

9.1.2. Intervalo de confianza de Welch
Este método no empareja las observaciones de dos sistemas, pero requiere que   sea independiente de
|     | , sin embargo,  |  puede ser distinto de  |     |     | .   |     |     |     |     |     |     |
| --- | --------------- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑋𝑋1𝑗𝑗
| 𝑋𝑋2H𝑗𝑗acemos para  |     | 𝑛𝑛1 :  |     | 𝑛𝑛2 |     |     |     |     |     |     |     |
| ------------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑖𝑖 = 1,2
|     |     |     |     |     |     | 𝑛𝑛𝑖𝑖   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
∑𝑗𝑗=1𝑋𝑋𝑖𝑖𝑗𝑗
𝑋𝑋𝑖𝑖(𝑛𝑛𝑖𝑖)
=
𝑛𝑛𝑖𝑖
𝑛𝑛𝑖𝑖
2
|     |     |     |     | 2           | [𝑋𝑋𝑖𝑖𝑗𝑗 | −𝑋𝑋𝑖𝑖(𝑛𝑛𝑖𝑖)] |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | ------- | ------------ | --- | --- | --- | --- | --- |
|     |     |     |     | 𝑆𝑆𝑖𝑖 (𝑛𝑛𝑖𝑖) | = �     |              |     |     |     |     |     |
𝑛𝑛𝑖𝑖
|     | Luego, usamos como un intervalo de confianza pa𝑗𝑗r=a1  |     |     |     | :   | −1  |     |     |     |     |     |
| --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝜉𝜉

|     |     |     |     |     |     | 2 2 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑆𝑆1(𝑛𝑛1) 𝑆𝑆2(𝑛𝑛2)
𝑋𝑋1(𝑛𝑛1)−𝑋𝑋2(𝑛𝑛2)±𝑡𝑡𝑓𝑓̂,1−𝛼𝛼⁄2�
+
|         |     |     |     |     |     | 𝑛𝑛1 𝑛𝑛2 |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
| Siendo  |     | .   |     |     |     |         |     |     |     |     |     |
9.2. Int𝑓𝑓̂e=rva𝑔𝑔l(o𝑠𝑠s1 ,d𝑠𝑠2e, 𝑛𝑛co1,n𝑛𝑛f2ia)nza para comparar más de dos sistemas
9.2.1. Método de ranking y selección
| 9.2.1.1. Seleccionar el mejor de  |     |     |  sistemas  |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Sea  , una variable aleatoria independiente de interés de la  -ésima réplica del  -ésimo sistema, y sea
𝑘𝑘
.
|     | 𝑋𝑋𝑖𝑖𝑗𝑗 |     |     |     |     | 𝑗𝑗  | 𝑖𝑖  |     |     |     | 𝜇𝜇𝑖𝑖 = |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
𝐸𝐸S(𝑋𝑋ea𝑖𝑖𝑗𝑗 ) , el  -ésimo más chico de los  , tal que  . El objetivo es seleccionar el sistema con
el   más chico.
|     | 𝜇𝜇𝑖𝑖𝑖𝑖 𝐿𝐿 |     | 𝜇𝜇𝑖𝑖 |     | 𝜇𝜇1 ≤ 𝜇𝜇2 | ≤ ⋯ ≤ 𝜇𝜇𝑖𝑖𝑘𝑘 |     |     |     |     |     |
| --- | --------- | --- | ---- | --- | --------- | ------------ | --- | --- | --- | --- | --- |
1
S𝜇𝜇e a   el evento selección correcta. Queremos que  , provisto por  , donde   y
|                                 |      |     | , ambos parámetros especifi∗cados por el analista.  |     |          |      |         |     | ∗   |     | ∗ 1  |
| ------------------------------- | ---- | --- | --------------------------------------------------- | --- | -------- | ---- | ------- | --- | --- | --- | ---- |
| la cantidad de indiferencia es  |      |     |                                                     |     |          |      | 𝜇𝜇1−𝜇𝜇2 |     |     |     |      |
|                                 | 𝐶𝐶𝑆𝑆 |     |                                                     |     | 𝑃𝑃(𝐶𝐶𝑆𝑆) | ≥ 𝑃𝑃 |         | ≥   | 𝑑𝑑  | 𝑃𝑃  | > 𝑘𝑘 |
∗
En la primera etapa hacemos𝑑𝑑  > 0  réplicas de cada uno de los   sistemas y definimos para  :
𝑛𝑛0
|     |     |     | ≥ 2 |     |     | 𝑘𝑘  |     |     | 𝑖𝑖 = | 1,2,…,𝑘𝑘 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | --- |
𝑛𝑛0
|     |     |     |     |     | (1)          | ∑𝑗𝑗=1𝑋𝑋𝑖𝑖𝑗𝑗 |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | ----------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | 𝑋𝑋𝑖𝑖 (𝑛𝑛0) = |             |     |     |     |     |     |
𝑛𝑛0
𝑛𝑛0
(1)
2
|     |     |     |     | 2          | [𝑋𝑋𝑖𝑖𝑗𝑗 | −𝑋𝑋𝑖𝑖 (𝑛𝑛0)] |     |     |     |     |     |
| --- | --- | --- | --- | ---------- | ------- | ------------ | --- | --- | --- | --- | --- |
|     |     |     |     | 𝑆𝑆𝑖𝑖 (𝑛𝑛0) | = �     |              |     |     |     |     |     |
𝑛𝑛 0 − 1
|     | Luego, computamos el tamaño de la muestra  |     |     |     |  p𝑗𝑗=a1ra el sis | t em a   :  |     |     |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | ---------------- | ----------- | --- | --- | --- | --- | --- |
|     |                                            |     |     |     | 𝑁𝑁𝑖𝑖             | 𝑖𝑖          |     |     |     |     |     |

2 2
ℎ1𝑆𝑆𝑖𝑖 (𝑛𝑛0)
|     |                                                     |     |     | 𝑁𝑁𝑖𝑖 = 𝑚𝑚𝑚𝑚𝑚𝑚�𝑛𝑛0+1,� |     | ∗ 2 �� |     |     |     |     |     |
| --- | --------------------------------------------------- | --- | --- | --------------------- | --- | ------ | --- | --- | --- | --- | --- |
|     | Donde   es una constante que se obtiene por tabla.  |     |     |                       |     | (𝑑𝑑 )  |     |     |     |     |     |
A continℎu1ación, hacemos   réplicas más del sistema  , y obtenemos las medidas de la segunda etapa:
𝑁𝑁𝑖𝑖 −𝑛𝑛0
𝑖𝑖
|     | Pagliaro, Luis  |     |     |     |     |     |     |     |     |     | 15  |
| --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

UNIVERSIDAD TECNOLÓGICA NACIONAL – FACULTAD REGIONAL ROSARIO
SIMULACIÓN

|                                     |     |     |            |       | 𝑁𝑁𝑖𝑖            |     |     |
| ----------------------------------- | --- | --- | ---------- | ----- | --------------- | --- | --- |
|                                     |     |     | (2)        |       | ∑𝑗𝑗=𝑛𝑛0+1𝑋𝑋𝑖𝑖𝑗𝑗 |     |     |
|                                     |     |     | 𝑋𝑋𝑖𝑖 (𝑁𝑁𝑖𝑖 | −𝑛𝑛0) | =               |     |     |
| Y la media de tamaño ponderado es:  |     |     |            |       | 𝑁𝑁𝑖𝑖 −𝑛𝑛0       |     |     |

|                                                   |     |            |               | (1)                |     | (2)          |     |
| ------------------------------------------------- | --- | ---------- | ------------- | ------------------ | --- | ------------ | --- |
|                                                   |     | 𝑋𝑋𝑖𝑖(𝑁𝑁𝑖𝑖) | = �𝑊𝑊𝑖𝑖1∗𝑋𝑋𝑖𝑖 | (𝑛𝑛0)�+�𝑊𝑊𝑖𝑖2∗𝑋𝑋𝑖𝑖 |     | (𝑁𝑁𝑖𝑖 −𝑛𝑛0)� |     |
| Luego, seleccionamos el sistema con el más chico  |     |            |               |                    | .   |              |     |
 que𝑋𝑋 c𝑖𝑖o(𝑁𝑁nt𝑖𝑖i)ene al mejor de
| 9.2.1.2. Seleccionar un subconjunto de tamaño  |     |     |     |     |     |  sistemas  |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- |
El procedimiento es similar al de ‘seleccionar el mejor de k sistemas’ excepto que en el cálculo de   se
|              |       |            |     | 𝑛𝑛  |     | 𝑘𝑘  |     |
| ------------ | ----- | ---------- | --- | --- | --- | --- | --- |
| reemplaza a  |  por  | . Además,  |  y  |     | .   |     |     |
𝑁𝑁𝑖𝑖
|                               |     |                 | ∗                          |     | ∗   |     |     |
| ----------------------------- | --- | --------------- | -------------------------- | --- | --- | --- | --- |
| 9.2.1.3. Selecℎci1onar lℎo2s  |     |  mejores𝑃𝑃 de>  |  𝑚𝑚sis⁄t𝑘𝑘ema𝜇𝜇s𝑖𝑖 1−𝜇𝜇𝑖𝑖2 | ≥   | 𝑑𝑑  |     |     |
El procedimiento es similar al de ‘seleccionar un subconjunto de tamaño n que contiene al mejor de k
|     |     | 𝑚𝑚  | 𝑘𝑘  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
sistemas’ excepto que en el cálculo de   se reemplaza a   por  . Además,   y
| .   |     |     |      |     |       | ∗                     |         |
| --- | --- | --- | ---- | --- | ----- | --------------------- | ------- |
|     |     |     | 𝑁𝑁𝑖𝑖 |     | ℎ2 ℎ3 | 𝑃𝑃 > 𝑚𝑚!∗(𝑘𝑘−𝑚𝑚)!⁄𝑘𝑘! | 𝜇𝜇𝑚𝑚+1− |
∗
𝜇𝜇𝑚𝑚 ≥ 𝑑𝑑
10. Método de media de lotes
Este método se utiliza para el análisis de las simulaciones no terminales. Trabaja de la siguiente manera:
1. Correr la simulación el tiempo suficiente como para remover cualquier efecto transiente y proveer una
cantidad de datos representativos del estado estacionario.
2. Dividir la duración restante de la corrida de simulación en sub-intervalos de tiempo correspondientes a
“lotes” de datos.
3. Computar medidas de rendimiento promedio para cada lote, y usar técnicas clásicas para desarrollar
estimadores, tratando las medias de lotes como réplicas independientes.

Los lotes sucesivos poseen cierta auto-correlación. Una manera de reducir esto es eliminar ciertos lotes (por
ejemplo, eliminar los lotes pares o impares), aunque esto reduce el número de observaciones independientes,
lo que resulta en intervalos de confianza más débiles.
11. Números aleatorios comunes
Si nuestro objetivo es determinar diferencias en las respuestas de un sistema debido al cambio en algún
parámetro del sistema, es intuitivamente razonable comparar la respuesta del sistema bajo las mismas
circunstancias. Esto implica utilizar los mismos números aleatorios para generar los tiempos de arribo y partida
para las corridas a comparar.
Si   es el tiempo de espera promedio obtenido a través de una simulación con un valor de retraso 1; y  es
el valor correspondiente para un valor de retraso 2, entonces, la varianza de la diferencia será:
| 𝑚𝑚1 |     |     |     |     |     |     | 𝑚𝑚2 |
| --- | --- | --- | --- | --- | --- | --- | --- |

Si variables aleatorias com𝑣𝑣u𝑚𝑚n𝑉𝑉e(s𝑚𝑚 s1o−n u𝑚𝑚t2i)liz=ad𝑣𝑣a𝑚𝑚s,𝑉𝑉 h(𝑚𝑚a1b)rá− co𝑣𝑣r𝑚𝑚r𝑉𝑉e(la𝑚𝑚c2i)ón+ e(n2tr∗e 𝑐𝑐la𝑐𝑐s𝑣𝑣 d(𝑚𝑚o1s, r𝑚𝑚e2s)p)uestas   y  , y la varianza
de su diferencia será reducida si el término de la covarianza es positivo.
𝑚𝑚1 𝑚𝑚2
| Pagliaro, Luis  |     |     |     |     |     |     |   16  |
| --------------- | --- | --- | --- | --- | --- | --- | ----- |

Capítulo 1: Modelado de Simulación Básico (Law & Kelton)
La naturaleza de la simulación
Sistema: empresa o proceso de interés a modelizar.
Modelo: representación del sistema en términos de relaciones cuantitativas y
lógicas.
Aplicaciones:
 Diseño y análisis de sistemas de fabricación.
 Evaluar requerimientos de hardware y software para un sistema informático.
 Evaluar nuevos sistemas de armas o tácticas militares.
 Determinar políticas de pedidos para un sistema de inventarios.
 Diseñar sistemas de comunicaciones y protocolos de mensajes para ellos.
 Diseñar y operar instalaciones de transporte.
 Evaluar diseños para organizaciones de servicios.
 Analizar sistemas financieros o económicos.
Sistemas, modelos y simulación
Un sistema se define como una colección de entidades que actúan e interactúan
juntos hacia el cumplimiento de un fin lógico. Definimos el estado de un sistema
como una colección de variables necesarias para describir un sistema en un
momento determinado, relativos a los objetivos de estudio.
Los sistemas se categorizan en dos tipos: discretos o continuos. Un sistema
discreto es aquel en el que las variables de estado cambian instantáneamente en
puntos separados del tiempo. En un sistema continuo en cambio las variables de
estado cambian continuamente con respecto al tiempo.
Diferentes maneras en que un sistema puede ser estudiado:
 Experimentos con el sistema real vs. Experimentos con un modelo del
sistema: si es posible alterar el sistema físico y luego dejar que opere bajo
las nuevas condiciones, es probable que sea conveniente hacerlo, porque en
este caso no hay duda acerca de si lo que estudiamos es relevante. Sin
embargo, rara vez es posible hacer esto. Por esto, es necesario construir un
modelo como una representación del modelo y estudiarlo como un sustituto
del sistema real.
 Modelos físicos vs. Modelos matemáticos: los modelos físicos son
construcciones en escala reducida o simplificada del sistema real para
estudiar en ellos su comportamiento. Los modelos matemáticos representan
un sistema en términos de relaciones lógicas y cuantitativas que son luego
manipuladas y modificadas para ver como el sistema reacciona
 Solución analítica vs. Simulación: si las relaciones que componen el modelo
son suficientemente simples, puede ser posible utilizar métodos
matemáticos para obtener información exacta sobre cuestiones de interés, lo
que se llama solución analítica. Muchos sistemas son demasiados complejos
para ser estudiados analíticamente, y deben ser estudiados por medio de la
simulación. En una simulación, usamos la computadora para evaluar un
modelo numéricamente, y los datos se recogen con el fin de estimar las
características del modelo.
Clasificación de los modelos de simulación:
 Estáticos vs. Dinámicos: un modelo de simulación estático es una
representación de un sistema en un momento determinado, o uno que
puede ser utilizado para representar un sistema en el que el tiempo
simplemente no juega ningún papel. Un modelo de simulación dinámica
representa un sistema a medida que evoluciona en el tiempo.
 Estocásticos vs. Determinísticos: Si un modelo de simulación no contiene
componentes probabilísticas (es decir aleatorias) se conoce como
determinístico, en estos modelos la salida se “determina” una vez que se

especifica el conjunto de relaciones (ecuaciones) y los valores de entrada.
En cambio los modelos estocásticos contienen variables aleatorias de
entrada sujetas a una distribución probabilística de algún tipo.
 Continuos vs. Discretos: definimos los modelos de simulación discreta y
continua de manera análoga a la forma en que los sistemas discretos y
continuos se definieron anteriormente.
Simulación de Eventos Discretos:
La simulación de eventos discretos comprende el modelado de un sistema a
medida que este evoluciona a través del tiempo por medio de una representación
en la cual las variables de estado cambian instantáneamente en puntos separados
en el tiempo. Estos puntos en el tiempo son aquellos en los cuales un evento
ocurre, donde un evento se define como una ocurrencia instantánea que puede
cambiar el estado del sistema.
Mecanismo de Avance del Tiempo
Debido a la naturaleza dinámica de los modelos de simulación de eventos
discretos, tenemos que realizar un seguimiento del valor actual del tiempo simulado
a medida que avanza la simulación, y también necesitamos un mecanismo para
avanzar el tiempo simulado de un valor a otro. Llamamos reloj de la simulación a la
variable de un modelo de simulación que contiene el valor actual del tiempo
simulado. La unidad del reloj nunca se enuncia explícitamente y se asume que está
en las mismas unidades que los parámetros de entrada.
Existen dos enfoques para el mecanismo de avance del tiempo:
 Avance del tiempo al siguiente evento: Con este enfoque el reloj de la
simulación se inicializa a cero y se determinan los tiempos de ocurrencia de
eventos futuros, luego el reloj se avanza al tiempo de ocurrencia del evento
futuro más próximo, en este punto el estado del sistema se actualiza para
determinar que un evento ha ocurrido y los tiempos de futuros eventos
también se actualizan. Este proceso continua hasta que se cumple con una
condición de parada pre especificada.
 Avance del tiempo a incrementos fijos: La diferencia con el método
anterior es que este enfoque no saltea periodos de inactividad en el sistema,
lo que supone una mayor cantidad de cómputo.
Componentes y organización de un modelo de simulación de eventos discretos
 Estado del sistema: el conjunto de variables de estado necesarias para
describir el sistema en un momento dado.
 Reloj de simulación: una variable que indica el valor actual del tiempo
simulado.
 Lista de eventos: una lista que contiene la próxima vez en el que cada tipo
de evento ocurrirá.
 Contadores estadísticos: variables usadas para almacenar información
estadística sobre el rendimiento del sistema.
 Rutina de inicialización: un sub-programa que inicializa el modelo de
simulación en el tiempo cero.
 Rutina de tiempo: un sub-programa que determina el siguiente evento de la
lista de eventos y luego avanza el reloj de simulación al momento en que
ocurre ese evento.
 Rutina de evento: un sub-programa que actualiza el estado del sistema
cuando un tipo particular de evento ocurre (hay una rutina de evento por
cada tipo de evento).
 Rutinas de biblioteca: un conjunto de sub-programas utilizados para generar
observaciones aleatorias a partir de distribuciones de probabilidad que
fueron determinadas como parte del modelo de simulación.
 Generador de informes: un sub-programa que calcula estimaciones de las
medidas de rendimiento deseadas y elabora un informe cuando la simulación
finaliza.

 Programa principal: un sub-programa que invoca la rutina de tiempo para
determinar el siguiente evento y luego transfiere el control a la
correspondiente rutina de evento para actualizar el estado del sistema
apropiadamente. También controla la terminación e invoca al generador de
informes cuando la simulación acaba.
Simulación de un Sistema de Colas de un solo Servidor
(M/M/1):
En un sistema de colas de un solo servidor, los tiempos entre arribos A , A ,…, A
1 2 n
(de cada cliente al sistema) son variables aleatorias IID (independientes e
idénticamente distribuidas). Un cliente que arriba y encuentra al servidor
desocupado se atiende inmediatamente, y los tiempos de servicio S , S ,…, S (de
1 2 n
cada cliente) son también variables aleatorias IID independientes de los tiempos de
arribo. Si un cliente arriba y encuentra al servidor ocupado se une al final de cola.
Al producirse una partida (un cliente completa el servicio) el servidor elige un
cliente de la cola según la disciplina FIFO. La simulación comenzará sin clientes en
el sistema y el servidor en estado desocupado. El sistema se simula hasta que un
número fijo (n) de clientes hayan completados sus demoras en cola, es decir
cuando el n-esimo cliente entre en servicio.
Medidas de Rendimiento: Para medir el rendimiento de este sistema observamos
las estimaciones de tres parámetros (más un parámetro opcional que es w(n)):
 Demora promedio esperada en cola de los n clientes. Llamada d(n).
 Número de clientes promedio esperado en la cola. Denotado por q(n).
 Utilización del servidor. Denominada u(n).
 Demora promedio esperada en el sistema de los n clientes. Llamada w(n).
Demora promedio esperada en cola de los “n-clientes”:
La demora promedio en una corrida determinada de la simulación es considerada
propiamente como una variable aleatoria en sí. Lo que queremos estimar, d(n), es
el valor esperado para esta variable aleatoria. d(n) es el promedio de una gran
numero de demoras promedio de n clientes. A partir de una sola corrida de la
simulación podemos estimar este parámetro a través de:
∑
̂( )
Esta fórmula es el promedio de las n demoras que fueron obtenidas durante la
simulación.
Este estimador está basado en una muestra de tamaño 1 ya que estamos
haciendo solamente una sola corrida de la simulación. Un estimador de este tipo no
tendrá demasiada precisión, pues el sistema seguramente se encuentra en estado
transitorio.
Es un ejemplo de una estadística de tiempo discreto.
Número de clientes promedio esperado en la cola:
Este promedio se toma sobre el periodo de tiempo necesarios para observar las
n demoras que definen nuestra regla de parada. Esta es una clase diferente de
promedio que el anterior, ya que se toma sobre el tiempo (continuo) en lugar de los
clientes (discreto).
Definimos Q(t) como el número de clientes en cola en el momento t (para
cualquier t ≥ 0) y T(n) como el tiempo requerido para observar n demoras en cola.
Para cualquier momento t entre 0 y T(n), Q(t) es no negativo. Si llamamos p a la
i
proporción esperada (entre 0 y 1) del tiempo en que Q(t) es igual a i, una
definición de q(n) seria:
( ) ∑
Para estimar q(n) en una simulación, simplemente reemplazamos p con sus
i
respectivas estimaciones y obtenemos:

̂( ) ∑ ̂
Donde ̂ es la proporción observada del tiempo en que hubo i clientes en la cola
(en la simulación).
Sin embargo una manera más sencilla de obtener ̂( ) es mediante algunas
consideraciones geométricas. Si llamamos T al tiempo total durante la simulación
i
en que la cola es de tamaño i, luego:
( ) ∑ y ⁄ ( )
Y el estimador puede escribirse como:
∑
̂( )
( )
La sumatoria en el numerador de la ecuación anterior es solo el área bajo la
curva de Q(t), que puede escribirse como una integral de 0 hasta T(n), quedando
finalmente la expresión:
( )
∫ ( )
̂( )
( )
Es un ejemplo de una estadística de tiempo continuo.
Utilización esperada del servidor:
La utilización esperada del servidor es la proporción esperada de tiempo durante
la simulación en que el servidor está ocupado y por eso es un número entre 0 y 1.
El estimador ̂( ) es la proporción observada de tiempo durante la simulación en
que el servidor está ocupado. Para esto definimos la “función ocupado” B(t).
( ) {
De esta manera ̂( ) puede expresarse como la proporción de tiempo en que
B(t) es igual a 1.
( )
∫ ( )
̂( )
( )
El numerador puede ser visto como el área bajo la función B(t) durante el curso
de la simulación.
̂( ) es el promedio continuo de la función B(t). La integral de B(t) puede
fácilmente ser acumulada por la suma de las áreas de los rectángulos. Las
estadísticas de uso son muy informativos en la identificación de cuellos de botella o
exceso de capacidad.
Es un ejemplo de una estadística de tiempo continuo.
Demora o Tiempo de espera promedio esperado en el sistema (cola + servidor):
Esta medida se define como el intervalo de tiempo desde el instante que un
cliente arriba a la cola hasta el instante en que el cliente completa el servicio y
parte.
El estimador usual de w(n) seria:
∑ ∑
̂( ) ̂( ) (̅ )
Donde Si es el tiempo de espera de los n clientes en el servidor y ̅( ) es el
promedio de los n tiempos de servicio de los clientes. Ya que el tiempo de servicio
medio o esperado E(S) es conocido un estimador alternativo seria ̃( ) ̂( )
( )
En casi todas las simulaciones de colas ̃( ) será mejor que ̂( ). Ambos son
estimadores no sesgados.
Eventos y variables de estado: Los eventos de este sistema son el arribo de un
cliente y la partida de un cliente. Las variables de estado necesarias para estimar

d(n), q(n) y u(n) son el estado del servidor, el número de clientes en cola, el
tiempo de arribo de cada cliente en cola y el tiempo del ultimo evento.
Observaciones:
 El elemento clave in la dinámica de una simulación es la interacción entre el
reloj de la simulación y la lista de eventos.
 Mientras se procesa un evento, no transcurre el tiempo de simulación.
 A veces es fácil pasar por alto las contingencias que parecen fuera de lo
común, pero que sin embargo hay que tener en cuenta.
 En algunas simulaciones puede suceder que 2 o más entradas en la lista de
eventos empatan en menor, y deba incorporarse una regla de decisión para
romper empates, que afectará el resultado de la simulación.
Reglas de interrupción alternativas
La simulación puede terminar:
 Cuando el número de clientes atendidos llega a una determinada cantidad
fija. El valor final del reloj de la simulación es una variable aleatoria.
 Cuando el reloj llega a una cantidad fija de tiempo. El número de clientes
atendidos es una variable aleatoria.
Determinando los eventos y variables
En el método de eventos gráficos, los eventos propuestos, cada uno
representado por un nodo, están conectados por arcos dirigidos que representan
cómo los eventos se pueden programar de otros eventos y de ellos mismos. Los
eventos gráficos conectan el conjunto propuesto de eventos por los arcos que
indican el tipo de programación de eventos que pueden ocurrir. Las flechas lisas
gruesas indican que un evento al final de la flecha se puede programar desde el
evento en el comienzo de la flecha en una cantidad no nula de tiempo, y la flecha
dentada delgada indica que el evento en su extremo está programado inicialmente.
Uno de los usos de los gráficos de eventos es simplificar la estructura de eventos
de una simulación mediante la eliminación de eventos innecesarios. Hay varias
reglas que permiten la simplificación, y una de ellas es que si un nodo de evento
tiene arcos entrantes que son todos delgados y lisos, este evento puede ser
eliminado del modelo y su acción integrada en los eventos que se programan en
tiempo cero.
Otra regla tiene que ver con la inicialización. El gráfico de eventos se
descompone en componentes fuertemente conectados, dentro de cada uno de los
cuales es posible viajar desde cada nodo a todos los demás nodos siguiendo los
arcos en sus direcciones indicadas. La regla de inicialización establece que en
cualquier componente fuertemente conectado de nodos que no tenga arcos
entrantes de otros nodos de eventos fuera del componente, debe haber al menos
un nodo que se programa inicialmente.
Simulación distribuida
En los últimos años la tecnología informática ha permitido que las computadoras
o procesadores individuales se asocien entre sí en entornos de computación
paralela o distribuida. En estos tipos de entornos, puede ser posible distribuir
diferentes partes de una tarea computacional a través de procesadores individuales
que operan al mismo tiempo y por lo tanto reducir el tiempo total para completar la
tarea.
Hay muchas formas posibles de dividir una simulación dinámica para distribuir su
trabajo sobre diferentes procesadores:
 Asignar las distintas funciones de apoyo a diferentes procesadores. La lógica
de ejecución de la simulación sigue siendo secuencial, pero el programa
principal de la simulación puede delegar la ejecución de las funciones de
soporte a otros procesadores y seguir adelante con su trabajo.

 Descomponer el modelo en distintos sub-modelos, que luego son asignados
a diferentes procesadores para la ejecución. Los procesadores deben
comunicarse entre sí siempre que sea necesario para mantener las
relaciones lógicas correctas entre los sub-modelos.
Pasos en un estudio de simulación
1. Formular el problema y planificar el estudio: todo estudio debe comenzar
con una declaración clara de los objetivos generales del estudio y las
cuestiones específicas que se abordarán.
2. Recolectar datos y definir un modelo: información y datos deben
recolectarse del sistema de interés y utilizarse para especificar los
procedimientos operativos y distribuciones de probabilidad de las variables
aleatorias utilizadas en el modelo.
3. Validar: en la construcción del modelo, es imperativo para los modeladores
involucrar en el estudio a las personas que están íntimamente familiarizadas
con las operaciones del sistema real.
4. Construir un programa de computación y verificar: el modelador de la
simulación debe decidir si se debe programar el modelo en un lenguaje de
propósito general o en un lenguaje de simulación de diseño especial.
5. Hacer corridas piloto: se hacen pruebas piloto del modelo verificado.
6. Validar: las pruebas piloto pueden usarse para probar la sensibilidad de las
salidas del modelo a pequeños cambios en un parámetro de entrada.
7. Diseñar experimentos: hay que decidir qué diseño de sistema simular si hay
más de una alternativa que pueda razonablemente simularse.
8. Hacer corridas de producción: se hacen corridas de producción para
proporcionar datos de rendimiento sobre los diseños de los sistemas de
interés.
9. Analizar los datos de salida: se usan técnicas estadísticas para analizar los
datos de salida de las corridas.
10. Documentar presentar e implementar los resultados: es importante
documentar los supuestos que entraron en el modelo, así como el propio
programa informático.
Otros tipos de simulación
 Simulación continua: se refiere a la modelización a lo largo del tiempo de un
sistema por una representación en la que las variables de estado cambian
continuamente con respecto al tiempo. Involucra ecuaciones diferenciales
que dan las relaciones de las tasas de variación de las variables de estado
con el tiempo.
 Simulación combinada discreta-continua: puesto que algunos sistemas no
son ni completamente discretos ni completamente continuo, puede surgir la
necesidad de construir un modelo con aspectos tanto de simulación de
eventos discretos y continuos.
 Simulación de Monte Carlo: es un esquema de empleo de números
aleatorios que se utiliza para solucionar determinados problemas
estocásticos o deterministas en donde el paso del tiempo no juega ningún
papel sustantivo.
Ventajas, desventajas y dificultades de la simulación
Ventajas:
 Muchos sistemas complejos no pueden describirse con precisión mediante un
modelo matemático que puede evaluarse analíticamente. Por lo tanto, una
simulación es a menudo el único tipo de investigación posible.
 Permite estimar el rendimiento de un sistema existente bajo un conjunto de
condiciones de operación proyectados.

 Diseños alternativos del sistema propuesto se pueden comparar a través de
la simulación para poder ver los que mejor se adaptan a los requerimientos
especificados.
 En una simulación podemos mantener mejor control sobre las condiciones
experimentales de lo que generalmente sería posible cuando
experimentamos con el propio sistema.
 Permite estudiar un sistema con un horizonte temporal largo en tiempo
comprimido, o bien estudiar los pormenores del funcionamiento de un
sistema en tiempo expandido.
Desventajas:
 Cada corrida de un modelo de simulación estocástico produce solo
estimaciones de las verdaderas características del modelo para un conjunto
particular de parámetros de entrada.
 Los modelos de simulación suelen ser costosos y requieren mucho tiempo
para desarrollarlos.
 El gran volumen de números producidos por un estudio de simulación o el
impacto persuasivo de una animación realista crea a menudo una tendencia
a poner mayor confianza en los resultados de un estudio que la que se
justifica.

Capitulo 9: Análisis de datos de salida para un sistema único
9.1 Introducción:
En muchos estudios de simulación se invierte una gran cantidad de dinero y tiempo en un modelo de
desarrollo y programación, pero se realiza poco esfuerzo en analizar los datos de salida de la simulación
apropiadamente. De hecho, un modo común de operación es hacer una sola corrida de la simulación de
longitud arbitraria y luego tratar a las estimaciones de la simulación como las características del modelo
verdadero. Ya que las muestras aleatorias de distribuciones de probabilidad son típicamente usadas para
llevar adelante un modelo de simulación a través del tiempo, estas estimaciones dependen de los valores
particulares de variables aleatorias que pueden sufrir variaciones. Como resultado, estas estimaciones en
una corrida particular de la simulación, pueden diferir de las verdaderas características del modelo. El efecto
neto es que hay una gran probabilidad de cometer errores en las inferencias sobre el sistema bajo estudio.
Históricamente, hay algunas razones por las cuales los analistas de los datos de salida no se manejan de
manera apropiada. Primero, los usuarios generalmente tienen la impresión que la simulación consiste en
programación complicada. Consecuentemente, muchos estudios de simulación comienzan con la
construcción de un modelo heurístico y codificación, y terminan con una sola corrida del estudio de
simulación que produce “las respuestas”. De hecho, la simulación es un experimento de muestreo
estadístico usando computadoras. En consecuencia, si los resultados de un estudio de simulación tienen un
significado, hay que utilizar apropiadas técnicas estadísticas para diseñar y analizar experimentos
estadísticos. Una segunda razón para inadecuados análisis estadísticos es que los procesos de salida de
simulaciones virtuales son no estacionarios y autocorrelacionados (ej. Los clientes que llegan afectan a los
que llegaran). Por esta razón las técnicas estadísticas basadas en observaciones independientes e
idénticamente distribuidas (IID) no son directamente aplicables.
Ahora vamos a describir más precisamente la naturaleza aleatoria de la salida de una simulación. Sea Y ,
1
Y ,…, Y las salidas de una sola corrida de simulación de un proceso estocástico. Por ejemplo, Y podría ser el
2 m i
rendimiento (producción) en la i-ésima hora en una empresa de manufactura. Las Y son variables aleatorias
i
que en general no son IID. En el caso de nuestro ejemplo, no son independientes ya que la producción de
una determinada hora depende de la hora anterior. Sean y , y ,…, y el resultado de realizar una corrida
11 12 1m
de simulación de longitud de m observaciones utilizando los números aleatorios u , u ,…, u (el i-ésimo
11 12 1m
número aleatorio que es utilizado en la j-ésima corrida se denota u ). Si realizamos otra corrida de la
ji
simulación con una diferente secuencia de números aleatorios u , u ,…, u , entonces obtendremos otros
21 22 2m
valores y , y ,…, y de las variables aleatorias Y , Y ,…, Y . Suponga que realizamos n replicas
21 22 2m 1 2 m
independientes de la simulación (se utilizan diferentes números aleatorios para cada réplica, se reinician los
contadores estadísticos para cada réplica y cada replica utiliza las mismas condiciones iniciales) de longitud
m, obteniendo como resultado las siguientes observaciones.
Secuencia 1: y , y ,…, y ,…, y
11 12 1i 1m
Secuencia 2: y , y ,…, y ,…, y
21 22 2i 2m
. . . .
. . . .
Secuencia n: y , y ,…, y ,…, y
n1 n2 ni nm
Las observaciones de una réplica particular (fila) no son IID. (Hay problemas de independencias porque hay
correlación). Sin embargo, si observamos y , y ,…, y (de la i-ésima columna) son observaciones IID de la
1i 2i ni
1

variable aleatoria Y, para i=1,2,…, m. Esta independencia de corridas cruzadas es la clave para los simples
i
métodos de análisis de datos de salida que se describen en las siguientes secciones. Entonces, toscamente
hablando, la clave del análisis de salida es usar las observaciones y (i=1,2,…, m; j=1,2,…, n) para hacer
ji
inferencias sobre variables aleatorias Y , Y ,…, Y .
1 2 m
9.2 Comportamiento transiente y estado estacionario de un proceso estocástico:
Considerar la salida de un proceso estocástico Y , Y ,…, Y . Sea F(y|I) P(Y<=y|I) para i=1,2,…, n, donde y es
1 2 n i i
un número real e I representa las condiciones iniciales utilizadas para comenzar la simulación en tiempo
cero. (La probabilidad condicional P(Y<=y|I) es la probabilidad que el evento Y<=y ocurre dadas las
i i
condiciones iniciales I). Para un sistema de manufactura, I puede representar el número de trabajos
pendientes y si la maquina esta libre u ocupada en tiempo cero. Llamamos F(y/I) la distribución transiente
i
de un proceso de salida en un tiempo discreto i para condiciones iniciales I. (En la etapa transiente son muy
importantes las condiciones iniciales). Las funciones de densidad para distribuciones transientes
correspondientes a las variables aleatorias pueden variar de una réplica a otra. Hay un cambio permanente
en la distribución de probabilidad (ley de los grandes números).
Para valores fijos de y e I, las probabilidades F (y|I) F (y|I),… son solo números. Si F(y|I) F(y) cuando i∞
1 2 i
para toda y y para cualquier condición inicial I, F(y) es llamada distribución en estado estacionario de los
proceso de salida Y , Y ,…, Y . Estrictamente hablando, la distribución en estado estacionario F(y) solo se
1 2 n
obtiene cuando i∞. En la práctica, sin embargo, en general habrá un tiempo, K+1, en el cual las
distribuciones, desde este punto en adelante, serán aproximadamente las mismas. El tiempo estacionario se
dice que comienza en un tiempo K+1. Notar que el estado estacionario no implica que las variables
aleatorias Y , Y ,…, Y tomaran el mismo valor en una corrida particular de simulación sino que significa
k+1 k+2 k+n
que tendrán aproximadamente la misma distribución. Además, estas variables aleatorias no serán
independientes.
La distribución de probabilidad no varía con estado estacionario y se independiza de las condiciones
iniciales.
La distribución en estado estacionario F(Y) no depende de las condiciones iniciales I, sin embargo la
velocidad de convergencia de la distribución transiente F(y|I) a la F(y) sí.
i
9.3 Tipos de simulaciones en relación con el análisis de resultados:
Las opciones disponibles para diseñar y analizar experimentos de simulación dependen del tipo de
simulación. Las simulaciones pueden ser terminales o no terminales, dependiendo si hay o no una manera
obvia de determinar la longitud de la corrida. Además, las medidas de rendimiento para simulaciones no
terminales pueden ser de varios tipos.
Simulación Terminal.
 No terminalParámetros de estado estacionario.
Ciclos de estado estacionario.
Otros parámetros.
Una simulación terminal es una para la cual existe un evento natural E, que especifica la longitud de cada
corrida o réplica. Como las diferentes corridas utilizan números aleatorios independientes y la misma regla
de inicialización, esto implica que las variables aleatorias comparables de distintas corridas son IID. El evento
E ocurre en un punto en el tiempo en el cual no se obtiene más información útil del sistema o el sistema se
limpia. Este evento debe especificarse antes de hacer las corridas y el tiempo de ocurrencia de E en una
corrida particular puede ser una variable aleatoria. Como las condiciones iniciales de una simulación
terminal generalmente afectan las medidas iniciales de rendimiento, estas deben ser muy representativas
de lo que ocurre en el sistema real.
2

Una simulación no terminal es aquella para la que no existe evento natural E para especificar la longitud de
una corrida. Una medida de rendimiento para este tipo de simulaciones es el parámetro de estado
estacionario, si es una característica de la distribución de estado estacionario de algún proceso estocástico
Y , Y ,…, Y . Si una variable aleatoria Y tiene una distribución de estado estacionario, entonces podemos
1 2 n
estar interesados en estimar el promedio de estado estacionario v=E(Y).
Sean 𝑌,,… procesos estocásticos de salida para una simulación no terminal que no tiene una distribución de
12
estado estacionario. Supongamos que dividimos el eje de tiempo en intervalos continuos y de igual duración
llamados ciclos. Sea 𝑌
𝑖
c una variable aleatoria definida en el 𝑖-ésimo ciclo, y asumiendo que 𝑌
1
c,
2
c,… son
comparables. Supongamos que los procesos 𝑌
1
c,
2
c,… tienen una distribución de estado estacionario 𝐹c, tal
que 𝑌 c ~𝐹 c . Entonces, una medida de desempeño es parámetro de ciclo de estado estacionario si es
característica de 𝑌 c como 𝑣 c =(𝑌 c). Por lo tanto, un parámetro de ciclo de estado estacionario es un
parámetro de estado estacionario del ciclo apropiado del proceso 𝑌 c, c,….
1 2
9.4 Análisis estadístico para simulaciones terminales:
Suponga que hacemos n replicas independientes de una simulación terminal, donde cada réplica finaliza por
el evento E y comienza con las mismas condiciones iniciales. La independencia de las replicas se lleva a cabo
utilizando diferentes números aleatorios para cada réplica. Asumir por simplicidad que hay una sola medida
de rendimiento de interés. Sea X una variable aleatoria definida en la j-ésima replica con j=1,2,…, n; las X
j j
son variables aleatorias IID. Para el ejemplo de un banco X puede ser la demora promedio de un cliente en
j
cola. Para el sistema de inventario, el costo total promedio mensual.
9.4.1 Estimación de la media:
Suponga que queremos obtener un punto de estimación y un intervalo de confianza para la media μ=E(X),
donde X es una variable aleatoria definida en una réplica como se describe arriba. Hacer n réplicas
independientes de la simulación y tomando a X , X ,…, X como las variables aleatorias IID resultantes. Luego
1 2 n
a partir de las X, obtenemos un punto de estimación imparcial para μ y un intervalo de confianza con
j
aproximadamente 100(1-α)% de confianza para μ dado por:
(1)
Llamaremos este intervalo de confianza Procedimiento de la muestra de tamaño fijo.
Obteniendo una precisión específica:
Una desventaja del procedimiento de la muestra de tamaño fijo basada en n réplicas, es que el analista no
tiene control sobre la longitud media del intervalo de confianza(o de la precisión de X (n)); para n fija, la
longitud media depende de Var(X), la varianza de la población de los X. En lo que sigue discutiremos
j
procedimientos para determinar el número de réplicas requerido para estimar la media μ=E(X), con un error
o precisión específicos.
Empezamos definiendo dos caminos para medir el error en la estimación X (la dependencia de n se suprime,
ya que el número de réplicas puede ser una variable aleatoria). Si la estimación de X es tal que | X - μ|=β
entonces decimos que X tiene un error absoluto β.
Supongamos que hemos construido un intervalo de confianza para μ basado en un número fijo de réplicas n.
2
Si asumimos que nuestra estimación de la varianza S (n) no cambiara mientras el número de réplicas sube,
3

una aproximación de la expresión para el número total de réplicas, n *(β), requerido para obtener el error
a
absoluto de β está dado por:
(2)
Voy aumentando i de uno en uno hasta que obtenga un valor menor a β, dicho valor de i es el número de
réplicas que tengo que realizar.
Luego la estimación X basada en todas las n *(β) réplicas debería tener un error absoluto de
a
aproximadamente β. La precisión de la ecuación (2) depende de lo cercano que esta la estimación S2(n) a
Var(X).
Ahora discutiremos otra forma de medir el error en X . Si la estimación X es tal que | X - μ|/|μ|= γ, entonces
decimos que X tiene un error relativo de γ o que el porcentaje de error en X es de 100γ %.
Suponga una vez más que construimos un intervalo de confianza de μ basado en un número fijo de réplicas
n, si asumimos que nuestras estimaciones de la media y de la varianza de la población no cambian mientras
el número de réplicas crece, una expresión aproximada para el número de réplicas, n*( γ) requerido para
r
obtener el error relativo de γ dado por:
(3)
Donde γ’= γ /(1+ γ) es el error relativo ajustado necesario para obtener el error relativo actual γ. Si n*( γ)>n y
r
si hacemos n*( γ)-n réplicas adicionales de la simulación, luego la estimación X basada en todas las n*( γ)
r r
replicas deberían tener un error relativo de aproximadamente γ.
La dificultad de usar la ecuación (3) directamente para obtener un estimador X con un error relativo de γ es
que X (n) y S2(n) pueden o no ser estimadores precisos de sus correspondientes parámetros poblacionales. Si
*
n ( γ ) es mayor que el número de réplicas realmente necesarias, entonces un número significativo de
r
réplicas innecesarias se realizarían, resultando una pérdida de recursos computacionales. A la inversa, si n *(
r
γ) es demasiado pequeño, entonces el estimador X basado en n*( γ) réplicas podría no ser preciso. Ahora
r
presentamos un procedimiento secuencial (nuevas réplicas son añadidas de a una por vez) para obtener un
estimador μ con un error relativo especifico que sólo utiliza las réplicas que son realmente necesarias. El
procedimiento asume que X , X ,…, X es una secuencia de variables aleatorias IID.
1 2 n
El objetivo especifico del procedimiento es obtener un estimador de μ con un error relativo de γ (0< γ
<1) y un nivel de confianza de 100(1-α)%. Eligiendo un número inicial de réplicas con n ≥2 y sea:
0
Es el intervalo de confianza de longitud media. Luego el procedimiento secuencia es como sigue:
0- Hacer n réplicas de la simulación y setear n=n .
0 0
1- Calcular X (n) y δ(n,α) desde X , X ,…, X .
1 2 n
^
2- Si δ(n,α)/ | X (n)|<= γ’, usar X(n) como el punto de estimación para μ y finalizar.
4

Equivalente,
^ ^
I(α,Y)=* X(n) - δ(n,α); X(n) + δ(n,α)+
Es aproximadamente un intervalo de confianza de 100(1-α)% para μ con la precisión deseada. Sino,
reemplazar n por n+1 y hacer una réplica adicional de la simulación e ir al paso 1.
Notar que el procedimiento calcula un nuevo estimador de Var(X) después de que se obtiene cada réplica, y
el número total de réplicas requeridas por el procedimiento es una variable aleatoria.
9.4.3 Elección de condiciones iniciales:
Como vimos anteriormente las medidas de rendimiento para una simulación terminal depende
explícitamente del estado del sistema a tiempo cero, entonces debemos tener cuidado cuando elegimos las
condiciones iniciales. Ilustramos este problema con un ejemplo. Suponga que queremos estimar la demora
promedio esperada de todos los clientes quienes arriban y completan su demora entre las 12pm del
mediodía y la 1pm en el banco. Como el banco va a estar probablemente lleno al mediodía, empezar la
simulación sin clientes presentes va a causar que nuestra estimación de la demora promedio sea
parcialmente baja. Ahora se discuten 2 enfoques heurísticos para este problema, el primero se utiliza más
ampliamente.
El primer enfoque, es el cual asumimos que el banco abre a las 9am sin clientes presentes. Entonces
podemos correr la simulación por 4hs. Para estimar el tiempo de demora promedio, solo utilizaremos las
demoras de los clientes que llegan y completan la espera entre el mediodía y la 1pm. La evolución de la
simulación entre las 9am y el mediodía, determina las condiciones apropiadas para la simulación del
mediodía. Una desventaja de este enfoque es que las 3hs de tiempo simulado, no son utilizadas para
estimar. Como resultado, uno puede comenzar la simulación en algún otro horario, por ejemplo a las 11am.
Sin embargo, no hay garantía de que las condiciones de la simulación de las 12pm serán representativas de
las condiciones reales del banco a esa hora.
Un enfoque alternativo es recolectar datos de números de clientes presentes en el banco al mediodía en
diferentes días. Tomamos p como la proporción de estos días en que están presentes i clientes (i=1,2,…, n)
i
al mediodía. Luego simulamos el banco desde el mediodía hasta al 1pm con el número de clientes presentes
al mediodía siendo seleccionados al azar desde la distribución de p.
i
9.7 Múltiples medidas de rendimiento:
En las secciones 9.4 y 9.6 se presentaron procedimientos para construir intervalos de confianza para una
sola medida de rendimiento. Sin embargo para la mayoría de las simulaciones del mundo real varias
medidas de rendimiento son requeridas simultáneamente.
Suponga que I es un intervalo de confianza con el 100(1-α)% de confianza para la medida de rendimiento
S S
μ (donde s=1,2,…, K). (Los μ pueden ser todas medidas de rendimiento para una simulación terminal o no
S S
terminal). Luego la probabilidad de que todos los K intervalos de confianza simultáneamente contengan sus
respectivas verdades medidas satisface:
Donde las I pueden ser independientes o no. Este resultado es conocido como la inecuación de Bonferroni.
S
Por ejemplo, suponer que se construyen intervalos de confianza con el 90% de confianza, esto es α=0,1,
S
para todas las s para 10 medidas de rendimiento distintas. Entonces, la probabilidad de que cada uno de los
10 intervalos de confianza contenga su verdadera medida de rendimiento solo puede afirmarse que es
mayor o igual a cero. Entonces no se puede tener la totalidad de la confianza en cualquier conclusión sacada
de este estudio. Esta dificultad se conoce en estadística como problema de múltiples comparaciones.
Ahora describimos una solución práctica para el problema cuando K es pequeño. Si se quiere tener todo el
5

nivel de confianza asociado con K intervalos de confianza para que sea al menos 100(1-α) porciento, elegir
las α para que ∑ α = α (notar que los α no tienen que ser iguales. Entonces los α correspondientes a
S S S S
medidas más importantes pueden ser menores). Por lo tanto, uno puede construir 10 intervalos de
confianza con el 99% de confianza y tener todo el nivel de confianza de al menos 90%. La dificultad con esta
solución es que los intervalos de confianza serán más grandes que lo que eran originalmente, utilizando el
procedimiento de la muestra de tamaño fijo, o se necesitan más datos para especificar los K errores, si se
utiliza el procedimiento secuencial. Por esta razón, se recomienda que K no sea mayor de 10.
Si se tiene un número muy grande de medidas de rendimiento, el único recurso disponible es construir los
intervalos de confianza de 90% o 95% de confianza pero estando atento de que uno o más de estos
intervalos probablemente no contenga la verdadera medida.
Capitulo 10
10.1 Introducción:
10.2 Métodos para determinar el intervalo de confianza para la diferencia de las medidas de rendimiento
de 2 sistemas:
Acá consideramos un caso especial de comparación entre 2 sistemas sobre la base de alguna medida de
rendimiento o respuesta esperada. Realizamos esta comparación formando un intervalo de confianza de la
diferencia de las 2 expectativas, en lugar de hacer un test de hipótesis para ver si la diferencia observada es
significativamente diferente de cero.
Para i =1,2, tomamos X , X ,…, X como una muestra de n IID observaciones para el sistema i y sea μ =
i1 i2 i ni i i
E(X ) la respuesta esperada de interés; queremos construir un intervalo de confianza para 𝜉= μ – μ . El
ij 1 2
hecho de que X y X sean independientes depende de cómo se ejecuten las simulaciones y esto determina
1j 2j
cual de los 2 enfoques de intervalos de confianza se utilizará.
10.2.1 Intervalo de confianza t-apareado:
Si n = n = n, o estamos dispuestos a descartar algunas observaciones del sistemas, podemos emparejar X
1 2 1j
con X para definir Z = X - X para j=1,2,…, n. Luego las Z son variables aleatorias IID y E(Z)= 𝜉, la cantidad
2j j 1j 2j j j
para la cual queremos construir el intervalo de confianza. Entonces podemos tomar:
∑ [ ̅( )]
̂ [ ̅( )]
( )
Y el intervalo de confianza de 100(1-α)% de confianza es:
Un punto importante a destacar es que no fue necesario asumir que X y X son independientes ni tampoco
1j 2j
fue necesario asumir que Var(X ) = Var(X ).
1j 2j
6

10.2.2 Intervalo de confianza Welch:
Un segundo enfoque para formar un intervalo de confianza para 𝜉 no empareja las observaciones de los 2
sistemas, pero requiere que las X sean independientes de las X . Sin embargo n y n pueden ser diferentes
1j 2j 1 2
para aplicar el clásico enfoque two-sample-t debemos asegurar que Var(X ) = Var(X ), si estas varianzas no
1j 2j
son iguales, el intervalo de confianza two-sample-t sufre una degradación. Sin embargo, si n = n , el
1 2
enfoque two-sample-t es bastante seguro incluso si las varianzas difieren. Ya que la igualdad de varianzas es
una suposición poco segura, no se recomienda usar el enfoque two-sample-t.
En lugar de este, se recomienda usar los problemas de varianzas distintas cuando las X son distribuidas
ij
normalmente la solución obtenida por Welch es:
∑ [ ̅( )]
( )
Para i=1,2. Luego,
Este es el intervalo de confianza con aproximadamente 100(1-α)% de confianza para 𝜉. Como f^ en general
no es un entero, se necesitara la interpolación en las tablas t. El intervalo de confianza anterior, el cual
llamamos intervalo de confianza de Welch, puede ser utilizado para validar un modelo de simulación para
un sistema real. Si el sistema 1 es un sistema del mundo real para el cual tenemos datos físicamente
recolectados y el sistema 2 que se corresponde con un modelo de simulación para el cual se tiene datos de
la salida de la simulación, es muy probable que n sea mucho menor que n .
1 2
Características:
 n puede ser distinto de n .
1 2
 Es indispensable asegurar independencia de las réplicas.
 No es necesario que las variables sean iguales.
10.3 Intervalos de confianza para comparar más de 2 sistemas:
Si solo tenemos que comparar 2 sistemas, los métodos en la sección 10.2 proveen una forma de construir
los intervalos de confianza para la diferencia entre medidas de rendimiento. Sin embargo, en algunos
estudios hay más de 2 sistemas, pero todavía podemos utilizar un enfoque de intervalo de confianza.
Haremos varias declaraciones de intervalos de confianza, entonces cada uno de sus niveles de confianza
individual, debe superar el nivel de confianza total.
Utilizaremos la inecuación de Bonferroni para asegurarnos que el nivel de confianza total sea al menos de 1-
α. Recordando, la inecuación de Bonferroni implica que si queremos realizar c intervalos de confianza,
entonces haremos cada intervalo de confianza individual con un nivel de confianza de 1-α/c, así el nivel de
7

confianza total será de al menos 1-α. Por ejemplo, si queremos construir c=10 intervalos y tener un nivel de
confianza total de 100(1-α)%=90 debemos hacer cada intervalo individual con un nivel de confianza del 99%.
10.4 Selección y Ranking:
10.4.1 Seleccionar el mejor de K sistemas:
Tomamos X como la variable aleatoria de interés (medida de rendimiento) de la j-ésima réplica del i-ésimo
ij
sistema y sea μ=E(X ). Para esta selección, así como también para las de las selecciones siguientes, los X se
i ij ij
asumen independientes entre sí.
Tomamos μ como el l-ésimo menor de todos los μ de tal forma que μ ≤ μ ≤…≤ μ . Nuestro objetivo en esta
il i i1 i2 ik
sección es seleccionar el sistema con la menor respuesta esperada, μ (si quisiéramos el mayor promedio μ ,
il ik
los signos de los X y los μ pueden ser revertidos).
ij i
Tomamos a CS como el evento de selección correcta.
La aleatoriedad inherente de los X implica que nunca estaremos totalmente seguros de que haremos la CS,
ij
pero estamos en condiciones de pre-especificar la probabilidad de CS. Además, si μ y μ son muy cercanos,
i1 i2
podríamos no preocuparnos si elegimos incorrectamente el sistema i (el que tiene promedio μ ), entonces
2 i2
queremos un método que evite realizar un gran número de réplicas para resolver esta diferencia
* *
insignificante, la formulación exacta del problema es que queremos que P(CS)≥P previendo que μ + μ ≥d ,
i2 i1
donde la probabilidad mínima aceptada P*> y la cantidad de indiferencia d*>0 ambos especificados por el
analista. Es natural preguntar qué pasa si la probabilidad es de al menos P*, la respuesta esperada del
sistema no será mayor que μ + d*.
i1
El procedimiento estadístico para resolver este problema involucra dos etapas de muestreo de cada uno de
los K sistemas, en la primer etapa hacemos un número fijo de réplicas de cada sistema, y luego utilizando las
estimaciones de la varianza obtenidas determinamos cuantas réplicas más son necesarias para cada sistema,
en la segunda etapa de muestreo. Debe asumirse que las X son normalmente distribuidas pero no es
ij
necesario asumir que σ2=Var(X ) ni tampoco que σ2 son las mismas para los diferentes i.
i ij
En la primera etapa, hacemos n ≥2 réplicas de cada uno de los K sistemas y definimos las medias y varianzas
0
de la primer etapa.
∑ [ ̅( )( )]
( )
Para i=1,2,…, K. Luego calculamos el total de muestras N necesarias para el sistema i:
i
(1)
Donde [X] es el entero más chico el cual es mayor o igual al verdadero numero X y h (la cual depende de K,
1
P* y n ) es una constante que se obtiene de una tabla. Luego, hacemos N-n réplicas más del sistema i
0 i 0
(i=1,2,…, K) y obtenemos las medias de la segunda etapa de muestreo.
8

Finalmente
Y seleccionamos el sistema con menor X (N).
i i
* *
Las elecciones de P y d dependen de los objetivos del analista y el sistema bajo estudio. Sin embargo elegir
el n es más complicado y en base a experiencia y algunas literaturas se sabe que n tiene que ser al menos
0 0
20. Si n es muy chico, se obtienen estimaciones pobres de S2(n ). Por otra parte, si n es muy grande,
0 i 0 0
podemos hacer demasiadas réplicas innecesarias para algunos sistemas.
10.4.2 Seleccionar un subconjunto de tamaño m que contiene al menor de K sistemas.
Ahora consideraremos un problema de selección distinto, que es seleccionar un subconjunto de
exactamente m de K sistemas con probabilidad de al menos P*. El subconjunto seleccionado contendrá el
sistema con la respuesta media más pequeña μ . Esto podría ser un objetivo en las etapas iniciales de una
i1
simulación, donde podría haber un numero grande K de sistemas alternativos y podríamos querer eliminar
aquellos que claramente son inferiores.
Definimos X , μ, μ y σ2 como en la sección 10.4.1. Otra vez, todas las X son independientes y normales, y
ij i il i ij
para un valor fijo i, X , X ,…, X son IID; las σ2 son desconocidas y no necesitan ser iguales. Acá, la correcta
i1 i2 ik i
selección (CS) es que el subconjunto de tamaño m que fue seleccionado contenga el sistema con media μ y
i1
queremos que P(CS) ≥P* previendo que μ - μ ≥d*. Acá debemos tener que 1≤m≤K-1, P*>m/k y d*>0. (Si μ -
i2 i1 i2
μ <d* con probabilidad de al menos P*, el subconjunto contendrá al sistema con una respuesta esperada
i1
*
que no es más grande que μ + d ).
i2
El procedimiento es muy similar al de la sección 10.4.1. En una primera etapa tomamos una muestra de n ≥2
0
réplicas de cada sistema y definimos X (1)(n ) y S2(n ) para i=1,2,…, K, exactamente como en la sección 10.4.1.
i 0 i 0
Luego calculamos el número total de réplicas, N, necesitadas para el i-ésimo sistema (Ecuación 1), excepto
i
que h es reemplazado por h (lo cual depende de m, K, P*y n ) que se encuentra en una tabla. Luego
1 2 0
hacemos N – n réplicas mas para la segunda etapa. Definimos X (2)(N-n ), los pesos W y W y obtenemos
i 0 i i 0 i1 i2
X (N), exactamente como en la sección 10.4.1. Finalmente, seleccionamos el subconjunto de m sistemas con
i i
los m menores valores de X (N).
i i
10.4.3 Seleccionar los m mejores de K sistemas:
Consideraremos como objetivo seleccionar un subconjunto de un tamaño especificado m
(1≤m≤K-1) con probabilidad de al menos P*, de tal forma que las respuestas esperadas del subconjunto
seleccionado sean las m respuestas con menor μ (μ , μ ,…, μ ). Es importante notar que los m sistemas con
i1 i2 im
las respuestas esperadas más chicas están desordenados. Esta selección puede ser útil si queremos
identificar varias opciones buenas, ya que el sistema puede ser inaceptable por otras razones, por ejemplo
políticas o ambientales.
La situación (independencia, normalidad, varianzas distintas y desconocidas, etc.) es la misma que en la
sección 10.4.2 excepto que la constante P* puede ser cambiada. Queremos que P(CS)≥P* previendo que μ
im+1
- μ ≥d*. CS se redefine como que las respuestas del subconjunto seleccionado son iguales a aquellas de los
im
m sistemas mejores.
9

(Si la condición de que μ - μ =>d* falla, con probabilidad de al menos P*, las respuestas esperadas de los
im+1 im
* *
m sistemas seleccionados no excederá μ + d ). También, debemos tener que P >m!(K-m)!/K! El
im
procedimiento para la solución es exactamente el mismo que el procedimiento para la solución de la sección
10.4.2, excepto que la constante h se reemplaza por h , que se puede encontrar en una tabla.
2 3
10