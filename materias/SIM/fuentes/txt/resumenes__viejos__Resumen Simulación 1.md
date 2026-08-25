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