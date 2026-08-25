Modelado de Simulación y Análisis - Averill M. Law
Capítulo 1 - Modelado de Simulación Básico
1.1 Naturaleza de la Simulación
La simulación consiste en el uso de computadoras para imitar el funcionamiento de
sistemas o procesos reales. Para estudiarlos científicamente se construyen modelos, basados
en relaciones matemáticas o lógicas, que representan el comportamiento del sistema.
A pesar de su utilidad, enfrenta algunos impedimentos:
- Complejidad de los modelos (programación extensa y difícil).
- Alto costo y tiempo computacional (ha disminuido gracias a la tecnología).
- Percepción errónea de que la simulación es solo programar y correr un modelo una
vez, sin un análisis riguroso.
Estas limitaciones resaltan la importancia de una metodología adecuada, que asegure
conclusiones válidas a partir de los modelos simulados.
1.2 Sistemas, Modelos y Simulación
Un sistema es un conjunto de entidades que interactúan
para alcanzar un objetivo. En la práctica, la definición del
sistema depende de los objetivos del estudio.
El estado de un sistema se describe mediante la colección
de variables necesarias para describir el sistema en un
determinado momento.
Los sistemas se clasifican en:
● Discretos: las variables de estado cambian en momentos específicos (cliente llega o
se va).
● Continuos: las variables de estado cambian de manera continua en el tiempo
(posición y velocidad de avión).
En la práctica, pocos sistemas son completamente discretos o continuos, pero suele haber
un tipo predominante que permite clasificarlos.
En el gráfico se pueden ver diferentes formas en las que se puede estudiar un sistema:
- Experimentar con Sistema Real: ideal si es posible y no resulta costoso ni riesgoso,
aunque rara vez lo es.
- Experimentar con Modelo del Sistema: más habitual, evita costos o interrupciones.
Siempre está la pregunta si el modelo refleja correctamente el sistema.
● Modelos Físicos: representaciones tangibles, como maquetas o simuladores.
Son poco comunes en investigación de operaciones o análisis de sistemas.
1

● Modelos Matemáticos: representaciones mediante relaciones lógicas o
cuantitativas, que luego son manipulados para ver cómo el sistema reacciona.
Son los más usados.
- Solución Analítica: se obtiene una respuesta exacta a partir de fórmulas.
Es útil si el modelo es simple. En caso de poder resolverlo de esta
manera, hacerlo.
- Simulación: necesaria cuando los modelos son demasiado complejos y
no permiten solución analítica. Ejercitar el modelo para las entradas en
cuestión para ver cómo afectan la salida.
Para estudiar un modelo de simulación es útil clasificarlo en tres dimensiones:
● Estáticos: representan un sistema en un instante.
● Dinámicos: representan la evolución del sistema en el tiempo.
● Determinísticos: no incluyen componentes probabilísticos, como variables aleatorias,
los resultados se determinan sólo con los datos de entrada.
● Estocásticos: incorporan aleatoriedad, por lo que los resultados son estimaciones y
esa es la principal desventaja (modelos de colas, inventarios).
● Continuos: describen cambios con ecuaciones diferenciales (flujo de tráfico).
● Discretos: se enfocan en eventos puntuales (autos individuales en la autopista).
Nota: un modelo discreto no siempre se usa para modelar un sistema discreto, y viceversa.
La decisión de utilizar un modelo continuo o discreto depende de los objetivos del estudio.
1.3 Simulación de Eventos Discretos
La simulación de eventos discretos consiste en modelar un sistema que evoluciona en el
tiempo mediante una representación en la cual las variables de estado cambian en instantes
separados en el tiempo (solamente en un número contable de momentos en el tiempo).
Evento: suceso instantáneo que puede (o no) modificar el estado del sistema.
Ejemplo: sistema con un solo servidor (barbería o mesa de información)
Objetivo: estimar el tiempo promedio de espera en la cola (intervalo desde el instante que
llega hasta que es atendido)
Variables de estado:
- Estado del servidor (ocupado o libre): permite determinar si, al llegar un cliente,
puede ser atendido inmediatamente o no.
- Número de clientes en la cola: se usa para decidir si, al finalizar un servicio, el servidor
queda libre o atiende al siguiente cliente en espera.
- Tiempos de arribo de los clientes en cola: permiten calcular la demora (tiempo de
inicio de servicio - tiempo de arribo).
2

Eventos:
- Llegada de un cliente: puede hacer que el servidor pase de libre a ocupado, o que
aumente la cola en 1.
- Salida (fin del servicio): puede hacer que el servidor pase de ocupado a libre, o que
disminuya la cola en 1.
En el ejemplo, ambos eventos cambian el estado del sistema, pero en algunas simulaciones
de eventos discretos no siempre ocurre. Un evento también puede servir para finalizar la
simulación en un instante dado o programar decisiones en determinados momentos.
1.3.1 Mecanismos de Avance de Tiempo
En un modelo de simulación de eventos discretos, como los estados cambian en el tiempo,
es necesario llevar el registro del tiempo simulado, se hace con la variable reloj de
simulación. El tiempo simulado no está relacionado con el tiempo real que tarda la
computadora en correr la simulación.
También se necesita un método para avanzar el reloj de un valor a otro:
- Siguiente Evento: es el más utilizado en la mayoría del software de simulación. El reloj
comienza en cero y se calculan los tiempos de los eventos futuros. El reloj se avanza
hasta el evento más próximo, actualizando el estado del sistema y recalculando los
tiempos futuros. Este proceso continúa hasta que se cumpla una condición de parada
preestablecida. Los periodos de inactividad se omiten, lo que hace a la simulación más
eficiente. Los saltos del reloj no siempre son iguales en tamaño.
- Incremento Fijo: caso especial del anterior. No omite los periodos de inactividad, lo
que puede consumir más tiempo de cómputo. El tiempo avanza en intervalos iguales.
Ejemplo: método de siguiente evento para un sistema de un solo servidor (cola)
t = tiempo de arribo del cliente i (t = 0)
i 0
A = t - t = tiempo entre arribos entre el cliente i - 1 e i
i i i - 1
S = tiempo de servicio del cliente i
i
D = tiempo en cola del cliente i
i
c = t + D + S = tiempo en el que el cliente i completa su servicio y se va
i i i i
e = tiempo de ocurrencia del evento i (valor que toma el reloj en ese evento)
i
Cada una de estas variables generalmente será aleatoria. Se asume que los tiempos entre
arribos A , A , … y los tiempos de servicio S , S , … son conocidos y tienen funciones de
1 2 1 2
distribución acumuladas F y F respectivamente.
A S
1. Inicio. En e = 0, el servidor está inactivo. El primer tiempo de llegada t se obtiene
0 1
generando A de F y sumándolo a 0. El reloj avanza de e al tiempo del siguiente
1 A 0
evento e = t .
1 1
2. Primera Llegada. Primer cliente llega en t . Como el servidor está inactivo, comienza a
1
ser atendido inmediatamente (D = 0) y el servidor pasa a ocupado. El tiempo en que
1
este cliente termina el servicio c se calcula como S + t , S generado de F .
1 1 1 1 S
3

3. Segunda Llegada. Segundo cliente llega en t = t + A . Si t < c , el reloj avanza de e a e
2 1 2 2 1 1 2
= t . Dado que el servidor está ocupado, el número de clientes en cola pasa de 0 a 1. No
2
se genera el tiempo de servicio S en este momento.
2
4. Tercera Llegada. El tiempo de llegada del tercer cliente va a ser t = t + A .
3 2 3
5. Cambio de eventos. Si c < t , el reloj avanza de e a e = c . En ese instante, el primer
1 3 2 3 1
cliente termina el servicio y se va, el segundo cliente comienza su servicio, y se calcula
su retraso en la cola D = c - t y su tiempo de salida c = c + S . El número de clientes en
2 1 2 2 1 2
la cola se reduce en 1.
6. Fin. La simulación puede terminar cuando se alcanza un número específico de
observaciones de retrasos de los clientes.
1.3.2 Componentes de un Modelo de Simulación de Eventos Discretos
En los modelos que usan el método de avance por siguiente evento, suelen aparecer los
siguientes elementos:
● Estado del Sistema: conjunto de variables necesarias para describir el sistema en un
tiempo determinado.
● Reloj de Simulación: variable que indica el valor actual del tiempo simulado.
● Lista de Eventos: lista que contiene el próximo tiempo en que ocurrirá cada tipo de
evento.
● Contadores Estadísticos: variables que almacenan información sobre el desempeño
del sistema.
● Rutina de Inicialización: subprograma que inicializa la simulación en tiempo 0.
● Rutina de Temporización: subprograma que determina el siguiente evento de la lista
y avanza el reloj hacia el tiempo en el que ocurre.
● Rutinas de Eventos: subprograma que actualiza el estado del sistema cuando ocurre
un tipo de evento determinado (hay una rutina de evento para cada tipo de evento).
● Rutinas de Librería: conjunto de subprogramas usados para generar observaciones
aleatorias a partir de distribuciones de probabilidad definidas en el modelo.
● Generador de Reportes: subprograma que calcula estimaciones de desempeño y
produce un reporte al finalizar la simulación.
4

● Programa Principal: subprograma que invoca la rutina de temporización para
determinar el próximo evento y transfiere el control a la rutina correspondiente.
Además, revisa la finalización de la simulación e invoca el generador de reportes.
El flujo de control con el método del siguiente evento.
1. Programa Principal.
- Invoca a la rutina de inicialización.
2. Rutina de Inicialización.
- Se pone en 0 el reloj de la simulación.
- Inicializa el estado del sistema y los contadores estadísticos.
- Inicializa la lista de eventos.
3. Programa Principal (Repetidamente)
- Invoca a la rutina de temporización.
Rutina de Temporización.
- Determina el siguiente tipo de evento, i.
- Avanza el reloj de la simulación.
- Invoca la rutina de evento i.
Rutina de Evento i.
- Actualiza el estado del sistema.
- Actualiza los contadores estadísticos.
- Genera futuros eventos y los agrega a la lista de eventos
Cuando finaliza la simulación:
4. Generador de Reportes.
- Calcula las estimaciones de interés.
- Escribe el reporte.
5

1.4 Simulación de un Sistema de Cola con un Solo Servidor
1.4.1 Planteo del Problema
● Consideremos un sistema de colas con un solo servidor:
- Tiempos entre Arribos: A , A , … son variables aleatorias independientes e
1 2
idénticamente distribuidas (IID).
- Tiempos de Servicio: S , S , … son IID y son independientes de los arribos.
1 2
IID: significa que tienen la misma distribución probabilística.
● Un cliente que llega y encuentra el servidor libre entra en servicio inmediatamente. Si
está ocupado, se une al final de la cola FIFO (primero en entrar, primero en salir).
● La simulación comienza en estado vacío e inactivo (sin clientes y con el servidor libre).
● El primer arribo ocurre después del primer tiempo entre arribos A
1 .
● La simulación se ejecuta hasta que n clientes hayan completado su demora en cola y
entren en servicio.
● El tiempo de fin es una variable aleatoria, depende de los arribos y tiempos de servicio.
Para medir el desempeño del sistema, miramos los estimados de tres cantidades:
- d(n) tiempo promedio en cola: promedio del tiempo que los n clientes esperaron en la
cola antes de ser atendidos. Depende de los valores aleatorios de llegadas y servicios,
es una variable aleatoria. Lo que se busca es su valor esperado, el promedio teórico si
se repitiera el experimento muchas veces.
𝑛
∑ 𝐷
𝑖
𝑑(𝑛) = 𝑖=1 donde D es el tiempo de espera en cola del cliente i.
𝑛 i
No se excluyen en el promedio los valores D = 0, cuando llega y encuentra el sistema
vacío, ayuda a reflejar el buen desempeño del sistema.
- q(n) número promedio de clientes en cola: es el promedio del número de clientes
esperando en la cola durante el tiempo que duró la simulación (hasta que n clientes
fueron atendidos). A diferencia de d(n), que es un promedio por cliente, q(n) es un
promedio en el tiempo. Para definirlo:
● Q(t): número de clientes en la cola en el tiempo t (t ≥ 0).
● T(n): tiempo total para que n clientes completen sus demoras en cola.
● p : proporción de tiempo que hubo i clientes en la cola.
i
∞
𝑞(𝑛) = ∑ 𝑖 𝑝 promedio ponderado, se puede estimar observando su simulación
𝑖
𝑖=0
6

∞
∞ ∑𝑖 𝑇
𝑖
𝑞(𝑛) = ∑ 𝑖 𝑝 = 𝑖=0 donde T es el tiempo total en el cual hubo i clientes en cola
𝑖 𝑇(𝑛) i
𝑖=0
- u(n) utilización esperada del servidor: proporción esperada de tiempo, entre 0 y T(n),
en la que el servidor está ocupado, no inactivo. Su valor está entre 0 y 1.
Definimos la función de ocupación
Entonces 𝑢(𝑛) es la proporción de tiempo en que B(t) = 1.
Utilización cercana al 100%, significa colas largas y posibles cuello de botella. Mientras
que la utilización baja conlleva un exceso de capacidad, recursos no aprovechados.
Ejemplo: trayectoria temporal de Q(t) en este sistema para el caso n = 6.
● Llegadas: ocurren en los tiempos 0.4, 1.6, 2.1, 3.8, 4.0, 5.6, 5.8 y 7.2.
● Salidas: ocurren en los tiempos 2.4, 3.1, 3.3, 4.9 y 8.6.
● La simulación termina en T(6) = 8.6.
Para calcular , primero se obtienen los tiempos T , que representan cuánto tiempo la cola
i
tuvo longitud i. Sumar todos los tiempos en los que la cola fue de i (ver gráfico).
T = (1.6 - 0.0) + (4.0 - 3.1) + (5.6 - 4.9) = 3.2
0
T = (2.1 - 1.6) + (3.1 - 2.4) + (4.9 - 4.0) + (5.8 - 5.6) = 2.3
1
T = (2.4 - 2.1) + (7.2 - 5.8) = 1.7
2
T = (8.6 - 7.2) = 1.4
3
T = 0 para todo i ≥ 4
i
∞
La suma ponderada es ∑ 𝑖 𝑇 = (0 . 3.2) + (1 .2.3) + (2 . 1.7) + (3 . 1.4) = 9.9
𝑖
𝑖=0
∞
𝑖 𝑇
Entonces 𝑞(𝑛) = ∑ 𝑖 = 9.9 = 1.15
𝑇(𝑛) 8.6
𝑖=0
7

Podemos observar, la suma es el área bajo la curva Q(t) desde el inicio al fin de la simulación.
𝑇(𝑛)
| ∞       | 𝑇(𝑛)                     | ∫ 𝑄(𝑡)𝑑𝑡 |     |     |     |
| ------- | ------------------------ | -------- | --- | --- | --- |
| ∑ 𝑖 𝑇 = | ∫ 𝑄(𝑡)𝑑𝑡   entonces 𝑞(𝑛) | = 0      |     |     |     |
| 𝑖       |                          | 𝑇(𝑛)     |     |     |     |
| 𝑖=0     | 0                        |          |     |     |     |

Ejemplo:  sistema para el caso n = 6.
Mirando el gráfico calculamos el tiempo en el que el servidor estuvo ocupado:
(3.3 - 0.4) + (8.6 -3.8) = 7.7
Entonces la utilización del servidor es 𝑢(𝑛) = 7.7 = 7.7 = 0.9
|     |     |     | 𝑇(𝑛) 8.6 |     |     |
| --- | --- | --- | -------- | --- | --- |
𝑇(𝑛)
∫ 𝐵(𝑡)𝑑𝑡
Podemos observar que se puede representar con la integral  𝑢(𝑛) = 0 .
𝑇(𝑛)

Ejemplo: sistema de cola de un solo servidor.
●  Tiempos entre arribos: A  = 0.4, A  = 1.2 , A  = 0.5 , A  = 1.7 , A  = 0.2, A  = 1.6, A  = 0.2 , A  = 1.4,
|     |            | 1   | 2 3 | 4 5 6 | 7 8 |
| --- | ---------- | --- | --- | ----- | --- |
| A   |  = 1.9, …  |     |     |       |     |
9
●  Tiempos de servicio: S  = 2.0, S  = 0.7, S  = 0.2, S  = 1.1, S  = 3.7, S  = 0.6, …
|     |     | 1 2 | 3 4 | 5 6 |     |
| --- | --- | --- | --- | --- | --- |

t = 0, inicialización.
●  El reloj se inicia en t = 0.
●  El servidor está libre (estado = 0) y la cola se encuentra vacía.
●  Todos los contadores estadísticos comienzan en 0.
| ●  La siguiente llegada A queda programada en 0 + A |     |     |     |  = 0.4.  |     |
| --------------------------------------------------- | --- | --- | --- | -------- | --- |
1
●  La siguiente salida aún no existe, por lo que se fija en ∞.
●  Al ser el inicio, no hay área acumulada todavía Q(t) = 0 y B(t) = 0.
8

t = 0.4, llegada del primer cliente.
● Encuentra el servidor vacío (estado = 0), por lo que entra directamente al servicio.
● Su demora en cola es D = 0, se actualiza la cantidad de tiempos en colas completados
1
a 1 y el tiempo total en cola a 0.
● El servidor cambia a ocupado (estado = 1).
● La siguiente llegada se programa en 0.4 + A = 1.6.
2
● La siguiente salida será cuando el cliente termine su servicio 0.4 + S = 2.4.
1
● B(t) = 0 x (0.4 - 0) = 0
● Q(t) = 0 x (0.4 - 0) = 0
t = 1.6, llegada del segundo cliente.
● Encuentra el servidor ocupado (estado = 1), por lo que debe esperar en la primera
posición de la cola. El número en cola aumenta a 1 y se guarda su tiempo de arribo.
● La siguiente llegada queda programada en 1.6 + A = 2.1.
3
● La siguiente salida sigue siendo la del cliente 1 en t = 2.4.
● Como ningún cliente sale de la cola en este instante, la cantidad de tiempos en colas
completados y el tiempo total en cola no cambian.
● B(t) = 0 x 0.4 + (1.6 - 0.4) x 1 = 1.2
● Q(t) = 0 x 1.6 = 0
t = 2.1, llegada del tercer cliente.
● Encuentra el servidor ocupado (estado = 1), por lo que entra en la cola. El número en
cola aumenta a 2, y se guarda su tiempo de arribo.
● La siguiente llegada queda programada en 2.1 + A = 3.8.
4
9

● La siguiente salida sigue siendo la del cliente 1 en t = 2.4.
● Como ningún cliente sale de la cola en este instante, la cantidad de tiempos en colas
completados y el tiempo total en cola no cambian.
● B(t) = 0 x (0.4 - 0) + 1 x (2.1 - 0.4) = 1.7
● Q(t) = 0 x (1.6 - 0) + 1 x (2.1 - 1.6) = 0.5
t = 2.4, salida del primer cliente.
● Como hay clientes esperando, el servidor toma al cliente 2 de la cola y comienza a
atenderlo inmediatamente. El número en cola disminuye a 1 (queda el cliente 3).
● Se calcula su demora en cola: D = 2.4 − 1.6 = 0.8.
2
● Se actualizan la cantidad de tiempos en colas completados = 2 y el tiempo total en
cola = 0 + 0.8 = 0.8.
● La siguiente salida pasa a ser el fin de servicio del cliente 2, en 2.4 +S = 3.1.
2
● B(t) = 0 x (0.4 - 0) + 1 x (2.4 - 0.4) = 2
● Q(t) = 0 x (1.6 - 0) + 1 x (2.1 - 1.6) + 2 x (2.4 - 2.1) = 1.1
1.4.3 Organización y Lógica del Programa
Evento de Llegada
1. Programar el siguiente evento de llegada.
2. ¿El servidor está ocupado?
● Sí:
1. Agregar 1 al número en cola.
2. Está la cola llena?
● Sí: Escribir mensaje de error y detener la simulación.
● No: Guardar la hora de llegada de ese cliente.
● No:
1. Fijar el tiempo en cola = 0 para este cliente y recopilar estadísticas.
2. Incremenentar en 1 el número de clientes que completaron la cola.
3. Poner el servidor en estado ocupado.
4. Programar un evento de salida para este cliente.
3. Retorna.
10

Evento de Salida
1. ¿Está la cola vacía?
● Sí:
1. Poner el servidor en estado inactivo.
2. Eliminar el evento de salida de consideración.
● No:
1. Restar 1 al número de clientes en cola.
2. Calcular el tiempo en cola del cliente que entra en servicio y recopilar
estadísticas.
3. Incrementar en 1 el número de clientes que completaron tiempo en cola.
4. Programar un evento de salida para este cliente.
5. Mover cada cliente en cola, si hay, un lugar hacia delante.
2. Retorna.
1.5 Simulación de un Modelo de Inventarios
1.5.1 Planteo del Problema
En estos problemas buscamos comparar diferentes políticas de pedido (ordering policies).
Consideramos que una empresa vende un solo producto y su objetivo es decidir cuántos
ítems tener en inventario durante los próximos n meses.
● Tiempo entre Demandas: son variables aleatorias independientes e idénticamente
distribuidas (IID), con distribución exponencial y una media de 0.1 meses.
● Tamaño de la Demanda (D): también es una variable aleatoria IID (independiente del
momento en que ocurre la demanda), con la siguiente distribución:
wp es la probabilidad
Al comienzo de cada mes, la empresa revisa su nivel de inventario y decide cuántos artículos
pedir al proveedor. Si la empresa pide Z artículos, incurre en un costo de K + iZ, donde K es el
costo fijo de pedido e i es el costo por artículo pedido. Si Z = 0, no se incurre en ningún costo.
Cuando se hace una orden, tenemos un Tiempo de Entrega (lead time), que es una variable
aleatoria uniforme entre 0.5 y 1 mes. La empresa utiliza un Política de Reordenamiento (s, S)
para decidir cuánto pedir:
Donde I es el nivel de inventario al comienzo del mes.
Si hay suficiente inventario, la demanda se satisface de inmediato. Si la demanda supera el
inventario disponible, la demanda excedente se pone en espera (backlog) y se cubre con
futuras entregas. Esto puede hacer que el inventario sea negativo.
11

Cuando llega un pedido, se utiliza primero para cubrir cualquier backlog y luego el resto (si
queda) se agrega al inventario.
Además del costo de pedido, el sistema de inventario también incurre en:
● h Costo de Almacenamiento (holding cost): incluye alquiler del almacén, seguros,
impuestos, mantenimiento y el costo de oportunidad del capital inmovilizado.
● p Costo por Faltantes (shortage cost): representa costos administrativos y pérdida de
buena voluntad de los clientes.
I(t): nivel de inventario en el instante t (puede ser positivo, cero o negativo).
- I +(t) = max{I(t), 0} artículos en existencia física en el tiempo t
- I - (t) = max{-I(t), 0} cantidad en backlog en el tiempo t
El número promedio (por mes) de artículos almacenados en el inventario durante el
período de n meses es:
𝑛
+
∫𝐼 (𝑡)𝑑𝑡
+
𝐼 = 0 por lo que el costo promedio de almacenamiento por mes es h 𝐼 +
𝑛
El número promedio de artículos en retraso es
𝑛
−
∫𝐼 (𝑡)𝑑𝑡
−
𝐼 = 0 por lo que el costo promedio de retraso es π 𝐼 −
𝑛
Resumen de costos asociados a un modelo de simulación de inventarios
● Costo por pedido: Cp = K + iZ.
● Costo de Almacenamiento (h) o costo de mantenimiento de ítems por mes de
inventario.
● Costo de por faltante (p o ℼ) o costo por ítem por mes de atraso en la entrega.
𝑛
+
∫𝐼 (𝑡)𝑑𝑡
+ +
● Costo promedio de almacenamiento: 𝐼 = 0 ⇒ 𝐶𝑝𝑎 = 𝐼 • ℎ
𝑛
𝑛
−
∫𝐼 (𝑡)𝑑𝑡
− −
● Costo promedio de retraso: 𝐼 = 0 ⇒ 𝐶𝑝𝑟 = 𝐼 • π
𝑛
12

1.5.2 Organización y Lógica del Programa
Evento de Llegada de Pedido
1. Incrementar el nivel de inventario en la cantidad previamente pedida.
2. Eliminar el evento de llegada de pedido de la consideración.
3. Retornar.
Evento de Demanda
1. Generar el tamaño de esta demanda.
2. Disminuir el nivel de inventario en ese tamaño de demanda.
3. Programar el siguiente evento de demanda.
4. Retornar.
Evento de Evaluación de Inventario
1. Evaluar I(t) < s
● En caso que sí:
1. Determinar la cantidad a pedir [S - I(t)].
2. Incluir el costo de pedido y recopilar estadísticas.
3. Programar el evento de llegada de pedido para esta orden.
2. Programar el siguiente evento de evaluación de inventario.
3. Retornar.
Actualizar Acumuladores Estadísticos de Tiempo Promedio
1. Fue I(t) durante el intervalo anterior: negativo, cero o positivo?
● Negativo:
1. Actualiza el área debajo de I - (t)
● Positivo:
1. Actualiza el área debajo de I + (t)
2. Retorna.
1.7 Pasos en una Simulación
1. Formular el problema y planificar el estudio
a. El problema es planteado por el gerente, pero puede no estar bien definido.
Puede ser un proceso iterativo.
b. Reuniones iniciales con gerente, analistas y expertos (SMEs) para definir:
● Objetivos generales y preguntas específicas
● Métricas de desempeño
● Alcance del modelo y configuraciones del sistema a modelar
● Cronograma y recursos necesarios
c. Seleccionar software de simulación.
2. Recopilar datos y definir el modelo
a. Reunir información sobre la estructura y operación del sistema:
● Ninguna persona o documento por sí solo es suficiente
● Puede haber información errónea, identificar a los verdaderos expertos
13

● Los procedimientos pueden no estar formalizados
b. Obtener datos para parámetros del modelo y distribuciones de probabilidad.
c. Redactar un documento de supuestos que detalle datos y estructuras.
d. Si es posible, recopilar datos del sistema actual para futura validación.
e. Elegir nivel de detalle del modelo considerando:
● Objetivos y métricas
● Disponibilidad de datos
● Credibilidad
● Opiniones de los expertos
● Limitaciones técnicas y recursos
f. No debe haber una correspondencia uno a uno entre cada elemento del
modelo y cada elemento del sistema.
g. Empezar con un modelo simple y aumentarlo si es necesario.
h. Mantener interacción constante con los responsables del proyecto.
3. Validar el documento de supuestos
a. Revisión estructurada del documento ante gerentes, analistas y expertos:
● Asegura la corrección y completitud.
● Fomenta participación y apropiación del modelo.
● Debe realizarse antes de programar para evitar reprocesos.
4. Construir y verificar el programa
a. Programar el modelo en lenguaje o software de simulación.
b. Verificar el programa (debugging), asegurar que corre correctamente.
5. Realizar corridas piloto
a. Ejecuciones preliminares para preparar la validación del modelo.
6. Validar el modelo programado
a. Si existe un sistema real, comparar resultados del modelo con los datos reales.
b. Revisión del modelo por parte de analistas y expertos.
c. Realizar análisis de sensibilidad para identificar factores críticos del modelo.
7. Diseñar experimentos
a. Definir para cada configuración:
● Duración de la simulación
● Periodo de calentamiento (si aplica)
● Número de repeticiones independientes (diferentes números aleatorios).
8. Realizar corridas de producción
a. Corridas completas del modelo para análisis formal.
9. Analizar los datos de salida
a. Evaluar desempeño absoluto de configuraciones del sistema y la comparación
relativa entre configuraciones alternativas.
10. Documentar, presentar y utilizar resultados
a. Documentar supuestos, programa, resultados.
b. Presentar resultados:
● Usar animaciones para comunicar a audiencias no técnicas.
● Explicar el proceso de modelado y validación para ganar credibilidad.
14

● Usar resultados en la toma de decisiones, si son válidos y creíbles.
1.8 Ventajas, Desventajas y Riesgos de la Simulación
Ventajas
● Permite representar sistemas complejos del mundo real con elementos estocásticos
que no se pueden modelar correctamente con modelos matemáticos o analíticos.
● Permite estimar el desempeño de un sistema bajo diferentes condiciones operativas.
● Comparar diseños o políticas operativas para ver cuál cumple mejor con los requisitos.
● Control mucho mayor sobre las condiciones experimentales que en pruebas reales.
● Permite un horizonte temporal largo en un tiempo comprimido o estudiar detalles en
tiempo expandido.
Desventajas
● Cada simulación produce estimaciones, se requieren varias corridas independientes
para obtener resultados confiables.
● No es tan eficaz para optimización como un modelo analítico válido.
● Suelen ser costosos y requieren mucho tiempo para desarrollarse.
● Riesgo de exceso de confianza en resultados aunque el modelo no sea una
representación válida.
En algunos estudios, tanto la simulación como los modelos analíticos pueden ser útiles:
- La simulación verifica la validez de los supuestos necesarios en un modelo analítico.
- Un modelo analítico sugiere alternativas para investigar en un estudio de simulación.
Riesgos que pueden afectar el éxito de un estudio de simulación:
- Planificación y Comunicación:
● Objetivos mal definidos al inicio.
● Nivel inapropiado de detalle del modelo.
● No involucrar a todo el equipo del proyecto desde el principio.
● Falta de comunicación con la gerencia.
- Conocimiento y Enfoque:
● Tratar el estudio como solo programación.
● Falta de personal con conocimiento en simulación y estadística.
● No recopilar buenos datos del sistema real.
- Software y Herramientas:
● Uso de software inapropiado o con macros poco documentadas.
● Creer que un software fácil no requiere conocimiento técnico.
● Mal uso de la animación.
- Datos y Aleatoriedad:
● No considerar correctamente las fuentes de aleatoriedad del sistema real.
● Usar distribuciones arbitrarias (normal, uniforme, triangular) como entradas.
15

● No establecer un período de calentamiento para el estado estable.
- Análisis y Resultados:
● Basar el análisis en una sola corrida o replicación.
● Comparar diseños con una sola replicación por diseño.
● Medidas de desempeño incorrectas.
Apéndice 1A. Avance de Tiempo en Incrementos Fijos
El otro enfoque para avanzar un reloj en una simulación de eventos discretos es por
incrementos fijos, donde se avanza el reloj en exactamente Δt unidades de tiempo.
Después de cada actualización del reloj, se revisa si algún evento ocurrió durante ese
intervalo. Si había eventos programados, se considera que ocurrieron al final del intervalo.
Como varios eventos pueden considerarse simultáneos, es necesario definir reglas para
determinar el orden en que se procesan.
Las principales desventajas son:
● Introduce errores al procesar eventos al final del intervalo en el que ocurren.
● Necesidad de decidir qué evento procesar primero cuando eventos que no son
simultáneos se tratan como simultáneos.
Se pueden solucionar eligiendo un Δt más chico, pero esto aumenta el número de revisiones
y el tiempo de ejecución. Por esto, no se suele usar el método de avance de tiempo para
modelos donde los tiempos entre eventos varían mucho.
El principal uso es para sistemas donde los eventos ocurren en tiempos múltiplos n Δt . Por
ejemplo, si los datos sólo están disponibles anualmente.
Apéndice 1B. Introducción a los Sistemas de Colas
Un sistema de colas consiste en uno o más servidores que brindan servicio a clientes que
llegan. Los clientes que al llegar encuentran todos los servidores ocupados, se unen a una o
más colas en frente de los servidores.
1B.1 Componentes de un Sistema de Colas
Un sistema de colas se caracteriza por tres componentes:
● Proceso de Llegada: describe cómo los clientes llegan al sistema. Si los tiempos de
arribos A , A , … son variables aleatorias IID, el tiempo promedio (o esperado) entre
1 2
1
llegadas es E(A) y la tasa de llegada de clientes λ = .
𝐸(𝐴)
● Mecanismo de Servicio: se define especificando el número de servidores s, si hay una
cola para cada servidor o una única cola para todos, y la distribución de probabilidad
16

de los tiempos de servicio de los clientes. Si S , S … son variables aleatorias IID, el
1 2
1
tiempo promedio de servicio es E(S) y la tasa de servicio de un servidor ω =
𝐸(𝑆)
● Disciplina de la Cola: regla que determina qué cliente de la cola (si hay) se atiende
cuando un servidor queda libre. Las más utilizadas son:
- FIFO: primero en entrar, primero en salir.
- LIFO: último en entrar, primero en salir.
- Prioridad: según importancia o requerimientos de servicio.
1B.2 Notación para Sistemas de Colas
Algunos sistemas de colas son tan comunes en la práctica que se han desarrollado
notaciones estándar. Por ejemplo, consideremos un sistema con:
● s servidores en paralelo con una cola FIFO que los alimenta.
● A , A , … son variables aleatorias IID
1 2
● S , S … son variables aleatorias IID
1 2
● Los A y S son independientes
i i
A este sistema se lo llama GI/G/s donde:
● GI (general independent): distribución de los tiempos entre arribos A
i
● G (general): distribución de los tiempos de servicio S
i
Si se conocen las distribuciones específicas, se usan los símbolos en lugar de GI y G
● M: distribución exponencial
● E : distribución k-Erlang
k
● D: tiempos determinísticos o constantes
Un sistema de un solo servidor con tiempos exponenciales entre llegadas y de servicio, y
disciplina FIFO, se denomina M/M/1.
λ
Para cualquier GI/G/s definimos el factor de utilización del sistema se define como: ρ =
𝑠ω
donde λ es la tasa de arribos y 𝑠ω es la tasa de servicio del sistema cuando todos los
servidores están ocupados. Mide qué tan intensamente se utilizan los recursos del sistema.
1B.3 Medidas de Desempeño de un Sistema de Colas
Hay muchas medidas de desempeño para los sistemas de colas, las más comunes:
● D = tiempo que el cliente i pasó en cola
i
● W = D + S = tiempo de espera en el sistema del cliente i
i i i
● Q(t) = número de clientes en cola en el tiempo t
● L(t) = número de clientes en el sistema en el tiempo t [Q(t) + número de clientes en
servicio]
𝑛
∑𝐷
𝑖
● 𝑑 = lim 𝑖=1 = demora promedio en estado estacionario
𝑛
𝑛→∞
𝑛
∑𝑊
𝑖
● 𝑤 = lim 𝑖=1 = tiempo de espera promedio en estado estacionario.
𝑛
𝑛→∞
17

𝑇
∫𝑄(𝑡)𝑑𝑡
● 𝑄 = lim 0
𝑇
𝑇→∞
𝑇
∫𝐿(𝑡)𝑑𝑡
● 𝐿 = lim 0
𝑇
𝑇→∞
Para sistemas de colas donde estas medidas existen, las siguientes ecuaciones de
conservación se cumplen:
● El número promedio de clientes en la cola es igual a la tasa de llegada multiplicada
por el retraso promedio 𝑄 = λ𝑑 .
● El número promedio de clientes en el sistema es igual a la tasa de llegada
multiplicada por el tiempo de espera promedio 𝐿 = λ𝑤 .
También se cumple 𝑤 = 𝑑 + 𝐸(𝑆) donde E(S) es el tiempo esperado de servicio.
Para una cola M/M/1, se puede mostrar que el número promedio de clientes en el sistema en
estado estacionario es:
ρ
𝐿 = donde ρ es la tasa de utilización del sistema.
1 − ρ
Simulación - Darío Weitz
1.5 Pasos para Realizar un Estudio de Simulación
1. Definición del Sistema Bajo Estudio:
● Establecer objetivos y supuestos del estudio
● Definir variables de decisión, sus interacciones y alcances
● Desarrollar modelo conceptual con fronteras, elementos, flujos y variables clave
2. Generación del Modelo Base:
● Traducir modelo conceptual a lenguaje de simulación
● Incluir interrelaciones entre subsistemas
● Definir animaciones si son necesarias
● Incorporar variables aleatorias y sus distribuciones
3. Recolección y Análisis de Datos:
● Recopilar información estadística de variables aleatorias
● Validar calidad y formato de datos
● Realizar estudios estadísticos si la información es insuficiente
● Identificar distribuciones de probabilidad apropiadas
4. Generación del Modelo Preliminar:
● Integrar análisis de datos, supuestos e información requerida
● Estimar rangos de variación o valores constantes para nuevos procesos
● Sugerir distribuciones basadas en experiencia
● Preparar modelo para verificación
5. Verificación del Modelo:
● Comprobar correcta programación del modelo
● Validar funcionamiento de parámetros
18

● Detectar errores de programación o alimentación de datos
● Actualizar supuestos si han cambiado durante el desarrollo
6. Validación del Modelo
● Probar modelo con información real o condiciones actuales de operación
● Validar comportamiento con expectativas del cliente
● Justificar comportamientos contrarios a experiencias de especialistas
● Para nuevos procesos, usar escenarios sugeridos por el cliente
7. Generación del Modelo Final
● Modelo validado listo para simulación
● Será el modelo base para comparar escenarios
8. Definición de Escenarios
● Acordar con cliente escenarios a analizar
● Usar comúnmente: pesimista, optimista e intermedio
● Considerar múltiples variables de respuesta
● Utilizar herramientas de simulación para múltiples réplicas
● Sugerir escenarios clave para reducir combinaciones posibles
9. Análisis de Sensibilidad
● Comparar estadísticamente los mejores escenarios
● Analizar intersección de intervalos de confianza
● Realizar más réplicas o incrementar tiempo de simulación si hay traslape
● Acortar intervalos de confianza para diferenciar soluciones
10. Documentación y Conclusiones
● Documentar completamente el modelo para uso futuro
● Incluir: supuestos, distribuciones, alcances, limitaciones
● Agregar sugerencias de uso y sobre resultados
● Presentar conclusiones del proyecto
● Elaborar reportes ejecutivos para presentación final
13. Modelos de Colas
13.1 Características de un Sistema de Colas
Población de Clientes
● Infinita: número de clientes muy grande en comparación con la capacidad del
sistema (clientes en un supermercado).
● Finita: número limitado de clientes (4 máquinas en un taller). El análisis es más
complejo.
Tiempos entre Llegadas
● Determinístico: los clientes llegan en intervalos de tiempo fijos y conocidos.
● Probabilístico: los tiempos entre llegadas son inciertos y se modelan con
distribuciones de probabilidad. Usualmente se utiliza la exponencial.
19

Proceso de Espera en Cola
● Cantidad de Colas: puede existir una única cola o varias colas.
● Número de Espacios en Cola: puede ser limitado (finito) o ilimitado (infinito).
● Disciplina de Cola: regla que determina qué cliente recibe servicio primero (FIFO,
LIFO, Prioridad).
Proceso de Servicio
● Tipo de Servidores:
- Idénticos: todos atienden a la misma velocidad ( usual en los modelos básicos).
- No idénticos: los servidores difieren en su rapidez de atención.
● Cantidad de Servidores: puede haber un único o múltiples servidores en paralelo.
Cualquier sistema de colas tiene dos fases:
● Fase Transitoria: periodo inicial de un sistema donde se observan los efectos de las
condiciones iniciales.
● Estado Estable: condición del sistema después que se han eliminado las condiciones
iniciales.
13.2 Medidas de Rendimiento
● λ = número promedio de llegadas por unidad de tiempo
● µ = número promedio de clientes atendidos por unidad de tiempo en una estación
1
● = tiempo promedio de servicio
µ
● 𝐿 = λ 𝑊 número promedio de clientes en el sistema
𝐿
● 𝑊 = 𝑞 tiempo promedio de espera
𝑞 λ
1
● 𝑊 = 𝑊 + tiempo promedio en el sistema
𝑞 µ
2
ρ
● 𝐿 = número promedio de clientes en cola
𝑞 1 − ρ
● 𝑃 = 1 − ρ probabilidad de que no haya clientes en el sistema
0
● 𝑃 = 1 − 𝑃 = ρ probabilidad de que un cliente que llega tenga que esperar
𝑤 0
𝑛
● 𝑃 = ρ 𝑃 probabilidad de que haya n clientes en el sistema
𝑛 0
● 𝑈 = ρ utilización, tiempo promedio que un servidor está ocupado
λ
● ρ = intensidad de tráfico
µ
Modelo M/M/1:
● Población de clientes finita.
● Los clientes llegan de acuerdo con un proceso de Poisson con tasa promedio de λ
clientes por unidad de tiempo. Para que el sistema alcance un estado estable se tiene
que dar que µ > λ
● Proceso de colas con una sola línea con disciplina FIFO.
● Un sólo servidor que atiende con cliente de acuerdo con una distribución exponencial
con una cantidad promedio de µ clientes por unidad de tiempo.
20

Modelo M/M/c:
● Población de clientes infinita.
● Los clientes llegan de acuerdo con un proceso de Poisson con tasa promedio de λ
λ
clientes por unidad de tiempo. Condición de estado estable ρ = .𝑐 < 1
µ
● Proceso de colas con una sola línea con disciplina FIFO.
● C servidores idénticos, cada uno atiende a los clientes con una distribución
exponencial con una cantidad promedio de µ clientes por unidad de tiempo.
13.5 Análisis Económico de los Sistemas de Colas
Para evaluar el costo de un sistema de colas se necesitan:
● Costo por servidor por unidad de tiempo c .
s
● Costo por unidad de tiempo por cliente esperando en el sistema c .
w
● Número promedio de clientes en el sistema L.
= (𝑐 . 𝑐) + (𝑐 . 𝐿)
𝑠 𝑤
En el caso de un sistema M/M/c con capacidad de espera limitada M/M/c/K necesitamos:
● Costo total de los servidores = costo por servidor x número de servidores = 𝑐 . 𝑐
𝑠
● Costo total de espera = costo de la espera x número clientes en el sistema = 𝑐 . 𝐿
𝑤
● Costo total por negación = costo por negación x número de llegadas x probabilidad de
negación = 𝑐 . λ .𝑝 (asociado a la pérdida de un cliente)
𝑑 𝑑
Entonces, el costo total = costo servidores + costo espera + costo negación de servicio
Simulación - Sheldon M. Ross
Capítulo 2 - Elementos de Probabilidad
2.1 Espacio Muestral y Eventos
S es el espacio muestral del experimento, el conjunto de todos los resultados posibles. S = { }
A es un evento, subconjunto del espacio muestral formado por resultados posibles del
experimento.
Para dos eventos A y B definimos el nuevo evento la unión A ∪ B, los resultados están en A, B
o ambos. Definimos la intersección AB, los resultados están en A y en B.
La unión de los eventos A , A , … , A denotado por ∪n está formado por todos los
1 2 n i=1
resultados que están en cualquiera de los A . La intersección de A , A , … , A denotado por A
i 1 2 n 1
A … A está formado por todos los resultados que están en todos los A .
2 n i
21

Para cualquier evento A definimos AC, el complemento de A, como todos los resultados del
espacio muestral S que no están en A (AC ocurre ↔ A no ocurre). SC es el conjunto vacío o ∅
Si AB = ∅, A y B no pueden ocurrir a la vez, decimos que estas son mutuamente excluyentes.
2.2 Axiomas de Probabilidad
Supongamos que para cada evento A de un experimento con espacio muestral S hay un
número, P(A) y llamado la probabilidad del evento A, que cumple los tres axiomas:
Axioma 1. 0 ≤ P(A) ≤ 1
La probabilidad de que el resultado del experimento esté en A es un número entre 0 y 1.
Axioma 2. P(S) = 1
Con probabilidad 1, este resultado es un elemento del espacio muestral.
Axioma 3. Para cualquier secuencia de eventos mutuamente excluyentes A , A , …
1 2
( 𝑛 ) 𝑛
( )
𝑃 ⋃ 𝐴 = ∑ 𝑃 𝐴 𝑛 = 1,2, ... , ∞
𝑖 𝑖
𝐼=1 𝑖=1
Para cualquier conjunto de eventos mutuamente excluyentes, la probabilidad de que al
menos uno ocurra es igual a la suma de sus probabilidades respectivas.
Con los axiomas anteriores llegamos a que la probabilidad de que no ocurra un evento es 1
menos la probabilidad de que ocurra. Como A y AC son eventos mutuamente excluyentes, y
como A ∪ AC = S tenemos que 1 = P(S) = P(A ∪ AC) = P(A) + P(AC) entonces P(AC) = 1 - P(A)
2.3 Probabilidad Condicional e Independencia
𝑃(𝐴𝐵)
La probabilidad condicional de A dado que B ha ocurrido es 𝑃(𝐴|𝐵) =
𝑃(𝐵)
En el caso de que 𝑃(𝐴|𝐵) = 𝑃(𝐴) decimos que A y B son independientes y entonces también
se da que 𝑃(𝐴𝐵) = 𝑃(𝐴) . 𝑃(𝐵). Esta relación es simétrica, siempre que A sea independiente de
B, B es independiente de A.
2.4 Variables Aleatorias
Las cantidades numéricas determinadas por los resultados del experimento se conocen
como variables aleatorias. La función de distribución F de la variable aleatoria X se define
para cualquier número real x como F(x) = P(X ≤ x)
Una variable aleatoria si asume un número finito de valores es discreta. Para estas, la función
de masa de probabilidad p(x) = P(X = x) y si toma uno de los posibles valores x , x , … entonces
1 2
∞
∑ 𝑝(𝑥) = 1
𝑖
𝑖=1
La variable aleatoria X es continua si existe una función no negativa f(x) definida para todo
número real x, el conjunto de valores posibles es un intervalo, sea C un conjunto de reales
𝑃(𝑋 ϵ 𝐶) = ∫ 𝑓(𝑥)𝑑𝑥
𝐶
22

2.5 Esperanza
Si X es una variable aleatoria discreta que toma uno de los valores x  , x  , … , entonces la
1 2
esperanza o valor esperado de X es
| 𝐸[𝑋] = ∑𝑥 𝑃(𝑋 | = 𝑥)  |     |     |     |     |     |     |
| ------------- | ----- | --- | --- | --- | --- | --- | --- |
𝑖 𝑖
𝑖
∞
Si X es continua con función de densidad de probabilidad f, entonces 𝐸[𝑋] = ∫ 𝑥𝑓(𝑥)𝑑𝑥
−∞
Si a y b son constantes, entonces E[aX + b] = a E[X] + b
|     |     |     |     = ∑(𝑎𝑥 | + 𝑏) 𝑝(𝑥)  |     |     |     |
| --- | --- | --- | ---------- | ---------- | --- | --- | --- |
𝑥
|     |     |     |     = 𝑎∑𝑥 𝑝(𝑥) | +   | 𝑏∑𝑝(𝑥) = | 𝑎𝐸[𝑋] + 𝑏  |     |
| --- | --- | --- | -------------- | --- | -------- | ---------- | --- |
|     |     |     |                |     |          |            |     |
|     |     |     |                | 𝑥   | 𝑥        |            |     |
Cualesquiera variables aleatorias X  y X   entonces E[X  + X ] = E[X ] + E[X ], se generaliza como
|       |     | 1   | 2   | 1   | 2 1 | 2   |     |
| ----- | --- | --- | --- | --- | --- | --- | --- |
| ⎡ 𝑛 ⎤ | 𝑛   |     |     |     |     |     |     |
[ ]
| 𝐸⎢∑ 𝑋⎥= | ∑ 𝐸 𝑋   |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- |
| ⎢ 𝑖⎥    | 𝑖       |     |     |     |     |     |     |
| ⎣𝑖=1 ⎦  | 𝑖=1     |     |     |     |     |     |     |
2.6 Varianza
E[X] es el valor esperado de la variable aleatoria X, un promedio ponderado de los valores
posibles de la misma. La variación de tales valores se puede medir considerando el promedio
del cuadrado de la diferencia entre X y E[X].
2
Si X es una variable aleatoria con media μ, entonces la varianza de X, es 𝑉𝑎𝑟(𝑋) = 𝐸[(𝑋 − µ) ]
2
|  También podemos expresarla como 𝑉𝑎𝑟(𝑋) |     |     | =          | 𝐸[(𝑋 − µ) | ]              |          |     |
| --------------------------------------- | --- | --- | ---------- | --------- | -------------- | -------- | --- |
|                                         |     |     |            | 2         | 2              |          |     |
|                                         |     |     |          = | 𝐸[𝑋 − 2µ𝑋 | + µ ]          |          |     |
|                                         |     |     |            | 2         |                | 2        |     |
|                                         |     |     |          = | 𝐸[𝑋 ] −   | 𝐸[2µ𝑋] + 𝐸[µ   | ]        |     |
|                                         |     |     |          = | 𝐸[𝑋 2 ] − | 2µ𝐸[𝑋] + µ 2   |          |     |
|                                         |     |     |            | 2         | 2 2            | 2        |     |
|                                         |     |     |          = | 𝐸[𝑋 ] − µ | = 𝐸[𝑋 ] −      | (𝐸[𝑋])   |     |

|     |     |     |     | 2   |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Sean dos constantes a y b 𝑉𝑎𝑟(𝑎𝑋 + 𝑏) = 𝐸[(𝑎𝑋 + 𝑏) ] − (𝐸[𝑎𝑋 + 𝑏])  por definición
|     |     |               | 2     | 2      | 2              | 2      |     |
| --- | --- | ------------- | ----- | ------ | -------------- | ------ | --- |
|     |     |             = | 𝐸[𝑎 𝑋 | + 2𝑎𝑏𝑋 | + 𝑏 ] − (𝑎𝐸[𝑋] | + 𝑏)   |     |
|     |     |               | 2     | 2      | 2              | 2 2    | 2   |
                    = 𝑎 𝐸[𝑋 ] + 2𝑎𝑏𝐸[𝑋] + 𝑏 − (𝑎 𝐸[𝑋] + 2𝑎𝑏𝐸[𝑋] + 𝑏 )
|     |     |               | 2      | 2 2        | 2                 |     |     |
| --- | --- | ------------- | ------ | ---------- | ----------------- | --- | --- |
|     |     |             = | 𝑎 𝐸[𝑋  | ] − 𝑎 𝐸[𝑋] |                   |     |     |
|     |     |               | 2      | 2          | 2                 |     |     |
|     |     |             = | 𝑎 (𝐸[𝑋 | ] − 𝐸[𝑋]   | ) por definición  |     |     |
2
|     |     |           = | 𝑎  𝑉𝑎𝑟(𝑋)  |     |     |     |     |
| --- | --- | ----------- | ---------- | --- | --- | --- | --- |

2.7 Desigualdad de Chebyshev y Leyes de los Grandes Números
Desigualdad de Markov. Si X sólo toma valores no negativos, para cualquier valor a > 0
𝑃(𝑋 ≥ 𝑎) ≤ 𝐸[𝑋]  . Para demostrarlo definimos una variable aleatoria Y como
𝑎
23

Tomando estos valores, la esperanza se expresa como 𝐸[𝑌]  =  𝑎 𝑃(𝑋 ≥ 𝑎)  +  0  𝑃(𝑋 < 𝑎)
|     |     |     |     |     |     |     |     |     |  =  𝑎  𝑃(𝑋 ≥ 𝑎)  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- |

Como X ≥ 0, entonces X ≥ Y. Utilizando la expresiones anteriores 𝐸[𝑋] ≥ 𝐸[𝑌]
|     |     |     |     |     |     |     |     |     |         𝐸[𝑋] | ≥ 𝑎  𝑃(𝑋 | ≥ 𝑎)  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | ----- |
𝐸[𝑋]
|     |     |     |     |     |     |     |     |     |          | ≥ 𝑃(𝑋 | ≥ 𝑎)  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ----- |
𝑎
Desigualdad de Chebyshev. Si X es una variable aleatoria que tiene media μ y varianza σ2,
entonces para cualquier valor k > 0
| 𝑃(|𝑋 − | µ|≥ 𝑘σ) | ≤   | 1   |     |     |     |     |     |     |     |     |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑘 2
|     |     |     |     |     |     | 2   |     | 2⎤  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Creamos una variable aleatoria  (𝑋−µ)  entonces 𝐸⎢ ⎡(𝑋−µ) ⎥= 1 𝐸[(𝑋 − µ) 2 ] = 1 𝑣𝑎𝑟(𝑥) = 1
|     |     |     |     |     | σ 2 |     | ⎣   | σ 2 ⎦ | σ 2 |     | σ 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
  por definición de varianza de X

Entonces, para la Desigualdad de Markov nos queda
2
|     | 𝐸[𝑋] |     |     |     |     | (𝑋−µ) |     | 2   |     |     |     |
| --- | ---- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
𝑃(𝑋 ≥ 𝑎) ≤  si cambiamos a 𝑋 por   y a 𝑎 por 𝑘  entonces obtenemos
|     |     | 𝑎   |     |     |     | σ 2 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
| (𝑋−µ) | 2   | 1   |     |     |     |     |     |     |     | 2   |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑃( ≥ 𝑘 ) ≤  multiplicamos dentro de 𝑃 a ambos términos por σ
| σ 2 |     | 𝑘   | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
| (𝑋−µ) | 2   | 2 2 | 1   |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑃( σ ≥ 𝑘 σ ) ≤  aplicamos raíz cuadrada solamente a la parte positiva y por Markov
| 2             |     |     | 2            |     |     |                            |     |     |     |     |     |
| ------------- | --- | --- | ------------ | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
| σ             |     |     | 𝑘            |     |     |                            |     |     |     |     |     |
| sabemos que 𝑋 |     | ≥   | 0 entonces 𝑋 |     | −   | µ ≥ 0 y la ecuación queda  |     |     |     |     |     |
1
| 𝑃(|𝑋 − | µ|≥ 𝑘σ) | ≤   |     |     |     |     |     |     |     |     |     |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
𝑘

Ley Débil de los Grandes Números. Sea X  , X  , … una sucesión de variables aleatorias
1 2
independientes e idénticamente distribuidas con media μ. Entonces, para cada ϵ > 0
| (|𝑋  + ... + 𝑋 |     |     | )   |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|
| 𝑃 | 1                 | 𝑛 − | µ|> | ϵ → | 0 cuando 𝑛   |               | → ∞  |     |     |     |     |     |
| --------------------- | --- | --- | --- | ------------ | ------------- | ---- | --- | --- | --- | --- | --- |
| |                     | 𝑛   | |   |     |              |               |      |     |     |     |     |     |
|                       |     |     |     | 𝑋  + ... + 𝑋 |               |      |     |     |     |     |     |
| Creamos una variable  |     |     |     | 1            | 𝑛, entonces   |      |     |     |     |     |     |
𝑛
𝑋  + ... + 𝑋
| 𝐸 ⎡ 1 | 𝑛⎤ ⎥= | 1 𝐸[𝑋 | +...+ |  𝑋 ]  |     |     |     |     |     |     |     |
| ----- | ----- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
⎢
| ⎣ 𝑛 | ⎦   | 𝑛   | 1   | 𝑛   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |          = | (𝐸[𝑋 | ]   | +  ...  + |  𝐸[𝑋 | ]) si 𝐸[𝑋] | = µ    |     |     |     |     |
| --- | ---------- | ---- | --- | --------- | ---- | ---------- | ------ | --- | --- | --- | --- |
|     |            | 𝑛    | 1   |           | 𝑛    |            | 𝑖      |     |     |     |     |
1
|     |          = | (µ  | +  ...  | +  µ ) n veces   |     |     |     |     |     |     |     |
| --- | ---------- | --- | ------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
𝑛
1
|     |          = | 𝑛µ  | = µ  |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑛

2
| Como 𝑉𝑎𝑟[𝑎𝑋] |     | = 𝑎 |  𝑉𝑎𝑟[𝑋]  |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑋  + ... + 𝑋
| ⎡ 1   | 𝑛⎤  | 1   |        |       |                                 |     |     |     |     |     |     |
| ----- | --- | --- | ------ | ----- | ------------------------------- | --- | --- | --- | --- | --- | --- |
| 𝑉𝑎𝑟 ⎢ |     | ⎥=  | (𝑉𝑎𝑟(𝑋 | +...+ |  𝑋 )) si 𝑋 son independientes   |     |     |     |     |     |     |
| ⎣     | 𝑛   | ⎦ 2 |        | 1     | 𝑛                               | 𝑖   |     |     |     |     |     |
𝑛
2
|     |     | = 1 | (𝑉𝑎𝑟(𝑋 | ) +...+ |  𝑉𝑎𝑟(𝑋 | )) como 𝑉𝑎𝑟(𝑋) |     |     | = σ   |     |     |
| --- | --- | --- | ------ | ------- | ------ | -------------- | --- | --- | ----- | --- | --- |
|     |     | 𝑛 2 |        | 1       |        | 𝑛              |     | 𝑖   |       |     |     |
24

|     |     | 1   | 2    | 2                    |     |     |     |     |     |
| --- | --- | --- | ---- | -------------------- | --- | --- | --- | --- | --- |
|     |     | =   | (σ + |  ...  + σ ) n veces  |     |     |     |     |     |
2
𝑛
2
|     |     | 1   | 2    | σ                       | σ                   |     |     |     |     |
| --- | --- | --- | ---- | ----------------------- | ------------------- | --- | --- | --- | --- |
|     |     | =   | 𝑛σ = |   entonces el desvío =  |  (desvío muestral)  |     |     |     |     |
|     |     | 2   |      | 𝑛                       | 𝑛                   |     |     |     |     |
𝑛

1
Por desigualdad de Chebyshev 𝑃(|𝑋 − µ|≥ 𝑘σ) ≤  reemplazando con variable y desvío
2
𝑘
| (|           |     |     |     | )   |     |     |       |     |       |
| ------------ | --- | --- | --- | --- | --- | --- | ----- | --- | ----- |
| 𝑋  + ... + 𝑋 |     | |   | σ   | 1   | σ   | 2   | 2 σ 2 |     | σ 2 1 |
𝑃 | 1 𝑛 − µ |≥ 𝑘 ≤   llamamos ε = 𝑘  entonces  ε = 𝑘   por lo que  =
| |               | 𝑛   | |   |     | 2   |     |     | 𝑛   |     | 2 2   |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
|                 |     |     | 𝑛   | 𝑘   | 𝑛   |     |     |     | ε 𝑛 𝑘 |
| (| 𝑋  + ... + 𝑋 |     | |   | )   | σ 2 |     |     |     |     |       |
𝑃 | 1 𝑛 − µ |≥ ε ≤  cuando n tiende infinito el lado derecho tiende a 0
| |   |     | |   |     | 2   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 𝑛   |     |     | ε 𝑛 |     |     |     |     |     |
Para un epsilon pequeño el promedio de la variables se acerca a la media muestral.

Ley  Fuerte  de  los  Grandes  Números.  A  largo  plazo, el promedio de una sucesión de
variables independiente e idénticamente distribuidas convergerá a su media.
𝑋  + ... + 𝑋
| lim | 1   | 𝑛 = µ  |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
𝑛
𝑛→∞

2.8 Algunas Variables Aleatorias Discretas
Variables Aleatorias Binomiales
Se realizan n ensayos independientes, cada uno con una probabilidad de éxito de p y de
fracaso 1 - p. Sea X el número de éxitos en esos n ensayos, entonces:  𝑋~𝐵𝑖(𝑛,𝑝)

Función de Masa de Probabilidad:
es el coeficiente binomial, número de subconjuntos distintos de i elementos
que se pueden elegir de un conjunto de n elementos

Una Bernoulli es un caso particular de binomial con n = 1:  𝑋~𝐵𝑖(1,𝑝)
 p
1 - p
| 𝐸[𝑋] = | 1 𝑝  + |  0 (1  | −  𝑝)  |     |        |       | 2          | 2   |     |
| ------ | ------ | ------ | ------ | --- | ------ | ----- | ---------- | --- | --- |
|        |        |        |        |     | 𝑉𝑎𝑟[𝑋] | = 𝐸[𝑋 | ] − (𝐸[𝑋]) |     |     |
|        |        |        |        |     | 𝑖      |       | 𝑖          | 𝑖   |     |
         =  𝑝
2
 =  𝑝 − 𝑝

|     |     |     |     |     |     |  =  𝑝(1 | − 𝑝)  |         |     |
| --- | --- | --- | --- | --- | --- | ------- | ----- | ------- | --- |

Una  variable  binomial  X  puede  expresarse  como  la  suma  de  n  variables  de Bernoulli
independientes e idénticamente distribuidas IID:
𝑛
| 𝑋  = ∑ | 𝑋  entonces  |     |     |     |     |     |     |     |     |
| ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
𝑖
𝑖=1
|        | 𝑛      |        |     |     |        | 𝑛          |     |        |       |
| ------ | ------ | ------ | --- | --- | ------ | ---------- | --- | ------ | ----- |
| 𝐸[𝑋] = | ∑ 𝐸[𝑋] | = 𝑛.𝑝  |     |     | 𝑉𝑎𝑟[𝑋] | = ∑ 𝑉𝑎𝑟[𝑋] | =   | 𝑛.𝑝.(1 | − 𝑝)  |
|        |        | 𝑖      |     |     |        |            | 𝑖   |        |       |
|        | 𝑖=1    |        |     |     |        | 𝑖=1        |     |        |       |

25

Variables Aleatorias Poisson
Una variable aleatoria X que toma los valores 0, 1, 2, … se dice que es una variable de Poisson
con parámetro λ (donde λ > 0) si su función de masa de probabilidad está dada por:
𝑖
| Función de Masa de Probabilidad: 𝑝 |     |     |     |     |     | =   | 𝑃(𝑋 = | 𝑖) = 𝑒 −λ λ |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | --- | --- | --- |

|     |     |     |     |     |     | 𝑖   |     | 𝑖!  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Las variables de Poisson se utilizan para aproximar la distribución del número de éxitos en
un  gran  número  de  ensayos  n,  donde  cada  ensayo  tiene  una  probabilidad de éxito p.
Consideremos una variable binomial 𝑋~𝐵𝑖(𝑛,𝑝) y definimos λ =  𝑛𝑝 . Entonces:
|     |        | 𝑛!  | 𝑖      | 𝑛−𝑖  |     |     |     |     |     |     |     |     |
| --- | ------ | --- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| 𝑃(𝑋 | = 𝑖) = |     |  𝑝(1 − | 𝑝)   |     |     |     |     |     |     |     |     |
(𝑛−𝑖)! 𝑖!
|                   |     |                           | ( )𝑖( | )𝑛−𝑖 |                                 |     |     |     |     |     |     |     |
| ----------------- | --- | ------------------------- | ----- | ---- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                 = |     | 𝑛!                        | λ 1   | − λ  |  desarrollando los factoriales  |     |     |     |     |     |     |     |
|                   |     | (𝑛−𝑖)! 𝑖!                 | 𝑛     | 𝑛    |                                 |     |     |     |     |     |     |     |
|                   |     |                           |       | 𝑖    | ( λ)𝑛                           |     |     |     |     |     |     |     |
|                   |     | 𝑛 (𝑛 − 1) (𝑛 − 2) ... 2.1 |       | λ    | 1 −                             |     |     |     |     |     |     |     |
     = 𝑛   la i estaría entre el 1 y la n por lo que podemos
|     |     | (𝑛 − 𝑖) (𝑛 −𝑖 −1) ... 2.1 . 𝑖! |     | 𝑖   | ( 1 − λ)𝑖 |     |     |     |     |     |     |     |
| --- | --- | ------------------------------ | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
𝑛
𝑛
λ)𝑛
|                  |     |                          |     | 𝑖 ( 1 −      |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|                  |     | 𝑛 (𝑛 − 1) ... (𝑛 −𝑖 + 1) |     | λ            | 𝑛   |     |     |     |     |     |     |     |
|                = |     |                          |     |              |     |     |     |     |     |     |     |     |
|                  |     |                          | 𝑖   | 𝑖! ( 1 − λ)𝑖 |     |     |     |     |     |     |     |     |
𝑛
𝑛
Cuando n grande y p pequeña, la binomial se transforma en una Poisson, y se cumplen las
siguientes aproximaciones cuando n tiende a ∞:
| 𝑛 (𝑛 − 1) ... (𝑛 −𝑖 + 1) |     |     |     |     |     |     | )𝑛  |     |     |     | )𝑖  |      |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|                          |     | ≈   | 1   |     | (   |     | λ   | −λ  |     | (   | λ   |      |
|                          | 𝑖   |     |     |     | 1   | −   | ≈   | 𝑒   |     | 1   | −   | ≈ 1  |
|                          | 𝑛   |     |     |     |     |     | 𝑛   |     |     |     | 𝑛   |      |
−λ λ 𝑖
| Entonces 𝑃(𝑋 |     | =   | 𝑖) ≈ 𝑒 |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑖!
Dado que para una variable binomial  𝑌~𝐵𝑖(𝑛,𝑝) se tiene:
| 𝐸[𝑌] | = 𝑛.𝑝 | = λ  |     |     |     |     |     | 𝑉𝑎𝑟[𝑋] | = 𝑛.𝑝.(1 | − 𝑝) | ≈ λ  para p pequeña  |     |
| ---- | ----- | ---- | --- | --- | --- | --- | --- | ------ | -------- | ---- | -------------------- | --- |

Entonces para una variable de Poisson X con parámetro λ : 𝐸[𝑋] = 𝑉𝑎𝑟[𝑋] = λ

Variables Aleatorias Geométricas
Considere una secuencia de ensayos independientes, cada uno con una probabilidad de
éxito p. Cuántos intentos 𝑛 hasta lograr el primer éxito. Si X representa el número del primer
ensayo que resulta en un éxito, entonces:
𝑛−1
| 𝑃(𝑋 | = 𝑛) = | 𝑝 (1 − | 𝑝)  |     |     |     |     |     |     |     |     |     |
| --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Una variable aleatoria con esta función de masa de probabilidad se denomina variable
geométrica con parámetro p.
|      | ∞   |         |     |       |     |     |     |        | 1 − 𝑝 |     |     |     |
| ---- | --- | ------- | --- | ----- | --- | --- | --- | ------ | ----- | --- | --- | --- |
|      |     |         | 𝑛−1 |       |     |     |     | 𝑉𝑎𝑟[𝑋] | =     |     |     |     |
| 𝐸[𝑋] | = ∑ | 𝑛𝑝 (1 − | 𝑝)  | = 1   |     |     |     |        | 2     |     |     |     |
𝑝
𝑝
𝑛=1

Variable Aleatoria Binomial Negativa
Supongamos  que  X representa el número de ensayos necesarios para obtener r éxitos,
donde cada ensayo es independiente y tiene una probabilidad de éxito p. Entonces, X es una
variable aleatoria binomial negativa (o Pascal).

26

| Función de Masa de Probabilidad:   |     |      |     |     |     | 𝑛 ≥ | 𝑟      |            |     |          |
| ---------------------------------- | --- | ---- | --- | --- | --- | --- | ------ | ---------- | --- | -------- |
|                                    | 𝑟   |      |     |     |     |     |        | 𝑟          |     |          |
|                                    |     |      | 𝑟   |     |     |     |        |            |     | 𝑟(1 − 𝑝) |
| 𝐸[𝑋]                               | = ∑ | 𝐸[𝑋] | =   |     |     |     | 𝑉𝑎𝑟[𝑋] | = ∑ 𝑉𝑎𝑟[𝑋] | =   |          |
|                                    |     | 𝑖    | 𝑝   |     |     |     |        |            | 𝑖   | 2        |
|                                    | 𝑖=1 |      |     |     |     |     |        | 𝑖=1        |     | 𝑝        |

2.9 Variables Aleatorias Continuas
Variables Aleatorias Uniformemente Distribuidas
Una variable aleatoria X está distribuida uniformemente en el intervalo (a, b), donde a < b, si
su función de densidad de probabilidad es:

X está distribuida uniformemente en (a, b) si coloca toda su masa en ese intervalo y tiene la
misma posibilidad de estar cerca de cualquier punto de ese intervalo.
|     | ∞   |     |     |     |     |     | 𝑉𝑎𝑟[𝑋] | = 𝐸[𝑋 2 ] | − (𝐸[𝑋]) | 2   |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------- | -------- | --- |

| 𝐸[𝑋] | = ∫ | 𝑥𝑓(𝑥)𝑑𝑥    |     |     |     |     |     |     |     |     |
| ---- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
|      | −∞  |            |     |     |     |     |     | ∞   |     |     |
2 2
|     |     |     |     |     |     |     | 𝐸[𝑋 | ] = ∫ 𝑥 𝑓(𝑥)𝑑𝑥  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- |
𝑏
|         =  | 1     | ∫𝑥𝑑𝑥  la integral de x es x2/2  |      |     |     |     |             | −∞          |           |        |
| ---------- | ----- | ------------------------------- | ---- | --- | --- | --- | ----------- | ----------- | --------- | ------ |
|            | 𝑏 − 𝑎 |                                 |      |     |     |     |             | (           | 3)        |        |
|            |       | 𝑎                               |      |     |     |     |             | 1 𝑏 3       | 𝑎         |        |
|            |       |                                 |      |     |     |     |           = |             | −         |        |
|            |       | (                               | 2)   |     |     |     |             | 𝑏 − 𝑎 3     | 3         |        |
|            |       | 1 𝑏 2                           | 𝑎    |     |     |     |             |             |           |        |
|            | =     |                                 | −    |     |     |     |             |             |           |        |
|            | 𝑏 − 𝑎 | 2                               | 2    |     |     |     |             |             | 2         | 2      |
|            |       |                                 |      |     |     |     |             | 1 (𝑏 − 𝑎)(𝑏 |  + 𝑎𝑏 + 𝑎 | )      |
|            |       |                                 |      |     |     |     |           = |             |           |        |
|            |       |                                 |      |     |     |     |             | 𝑏 − 𝑎       | 3         |        |
|          = |       | 1 (𝑏 + 𝑎)(𝑏 − 𝑎)                |      |     |     |     |             |             |           |        |
|            | 𝑏 − 𝑎 |                                 | 2    |     |     |     |             | 1 2         |           | 2      |
|            |       |                                 |      |     |     |     |           = | (𝑏   +      |  𝑎𝑏  +    |  𝑎 )   |
3
|          = | 𝑏 + 𝑎 |     |     |     |     |     |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
|                 |                      |     | 1       | 2      |         | 2 (𝑏 + 𝑎)2     |            |        |     |     |
| --------------- | -------------------- | --- | ------- | ------ | ------- | -------------- | ---------- | ------ | --- | --- |
| Entonces 𝑉𝑎𝑟[𝑋] |                      |     | =       | (𝑏   + |  𝑎𝑏  +  |  𝑎 ) −         |            |        |     |     |
|                 |                      |     | 3       |        |         |                | 2          |        |     |     |
|                 |                      |     |         |        |         | 2              | 2          |        |     |     |
|                 |                      |     | 1       | 2      |         | 2 𝑏  + 2𝑎𝑏 + 𝑎 |            |        |     |     |
|                 |                    = |     |         | (𝑏   + |  𝑎𝑏  +  |  𝑎 ) −         |            |        |     |     |
|                 |                      |     | 3       |        |         |                | 4          |        |     |     |
|                 |                      |     | 1       | 2      |         | 2              | 2          | 2      |     |     |
|                 |                      |     |       = | (4𝑏    | + 4 𝑎𝑏  | + 4 𝑎 −        | 3𝑏 − 6𝑎𝑏 − | 3𝑎 )   |     |     |
12
|     |     |     | 1       |      | 2     |     |     |     |     |     |
| --- | --- | --- | ------- | ---- | ----- | --- | --- | --- | --- | --- |
|     |     |     |       = | (𝑎 − | 𝑏)    |     |     |     |     |     |
12

Variables Aleatorias Normales
Una variable aleatoria X se distribuye normalmente con media
µ y varianza σ 2  si su función de densidad de probabilidad es:
|      |     | −(𝑥−µ) | 2 /2σ 2 |     |       |        |     |     |     |     |
| ---- | --- | ------ | ------- | --- | ----- | ------ | --- | --- | --- | --- |
| 𝑓(𝑥) | =   | 1 𝑒    |         |     | − ∞ < | 𝑥 < ∞  |     |     |     |     |
2πσ
La curva tiene forma de campana y es simétrica alrededor de µ
| 𝐸[𝑋] | = µ  |     |     |     |     |     |        | 2     |     |     |
| ---- | ---- | --- | --- | --- | --- | --- | ------ | ----- | --- | --- |
|      |      |     |     |     |     |     | 𝑉𝑎𝑟[𝑋] | = σ   |     |     |
2
Si X es normal con media µ y varianza σ  cualesquiera constantes a y b, aX + b está distribuida
2 2
| normalmente con media  𝑎µ |     |     |     |     | + 𝑏 y varianza 𝑎 |     | σ .   |     |     |     |
| ------------------------- | --- | --- | --- | --- | ---------------- | --- | ----- | --- | --- | --- |
|                           |     |     |     | 1   | µ                |     |       |     |     |     |
| También, siendo 𝑍         |     |     | =   | 𝑋 − |                  |     |       |     |     |     |
|                           |     |     |     | σ   | σ                |     |       |     |     |     |
𝑋−µ
|     |     |     |            = |     |     |     |     |     |     |     |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
σ
27

2
Z tiene una distribución normal y se llama estandarizada, con media µ = 0 y varianza σ = 1.
Esto lo podemos demostrar aplicando las propiedades:
| E[aX + b] = a E[X] + b  |     |     |     | (1)2 |     |
| ----------------------- | --- | --- | --- | ---- | --- |
2
|     |     |     |     | 𝑉𝑎𝑟(𝑍) = | σ = 1  |
| --- | --- | --- | --- | -------- | ------ |
σ
| 𝐸[𝑍] = 1 | µ − µ = 0  |     |     |     |     |
| -------- | ---------- | --- | --- | --- | --- |
| σ        | σ          |     |     |     |     |
2
| 𝑉𝑎𝑟(𝑎𝑋 + | 𝑏) = 𝑎 𝑉𝑎𝑟(𝑋)  |     |     |     |     |
| -------- | -------------- | --- | --- | --- | --- |
Sea ϕ(𝑥) la función de distribución de una variable aleatoria normal estándar:
𝑥 2
1 −𝑥 /2
| ϕ(𝑥) = 𝑃(𝑍 | ≤ 𝑥) = | ∫ 𝑒 𝑑𝑥                         | − ∞ ≤ | 𝑥 ≤ ∞     |     |
| ---------- | ------ | ------------------------------ | ----- | --------- | --- |
2π
−∞
𝑋−µ
Como 𝑍 =  entonces podemos expresar la función de distribución de 𝑋 como:
σ
| 𝐹(𝑥) = 𝑃(𝑋 | ≤ 𝑥)  |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- |
(𝑋−µ 𝑥−µ)
|          = 𝑃 | ≤   |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- |
σ σ
( 𝑥−µ)
|          = 𝑃 | 𝑍 ≤   |     |     |     |     |
| ------------ | ----- | --- | --- | --- | --- |
σ
(𝑥−µ)
|          = ϕ |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- |
σ

Teorema Central del Límite
| X   | ,  X   ,  …  |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- |
Sea  una  sucesión  de  variables  aleatorias  independientes  e  idénticamentes
| 1   | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
2
distribuidas con media finita  µ y varianzafinita  σ  . Entonces
| {𝑋    |  + ... + 𝑋  − 𝑛µ | }           |     |     |     |
| ----- | ---------------- | ----------- | --- | --- | --- |
| lim 𝑃 | 1 𝑛              | < 𝑥 = ϕ(𝑥)  |     |     |     |
| 𝑛→∞   | σ 𝑛              |             |     |     |     |

Variables Aleatorias Exponenciales
Una variable aleatoria continua X sigue una distribución exponencial con parámetro  λ > 0 si
su función de densidad de probabilidad es:
−λ𝑥
| 𝑓(𝑥) = λ𝑒 |                          0 | < 𝑥 < ∞  |     |     |     |
| --------- | -------------------------- | -------- | --- | --- | --- |
𝑥
Su distribución acumulativa está dada por 𝐹(𝑥) = ∫λ𝑒 −λ𝑥 𝑑𝑥 = 1 − 𝑒 −λ𝑥

0
| 1      |     |       |     |          | 1   |
| ------ | --- | ----- | --- | -------- | --- |
| 𝐸[𝑋] = |     |       |     | 𝑉𝑎𝑟[𝑋] = |     |
| λ      |     |       |     |          | 2   |
λ
| Proceso Poisson  |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- |
Sea  N(t) el número de eventos que ocurren en el intervalo [0, t]. Estos eventos constituyen un
proceso de Poisson con razón  λ > 0 si:
a.  Condición Inicial: comienza en el instante 0, N(0) = 0
b.  Incremento Independiente: el número de eventos en intervalos de tiempo disjuntos
son independientes.
c.  Incremento  Estacionario:  (diferencia  si  es  homogéneo  o  no)  la  distribución  del
número de eventos en un intervalo determinado depende solo de su longitud, no de
su posición en el tiempo. Todos los intervalos tienen la misma probabilidad.
d.  En un intervalo pequeño de longitud h, la probabilidad de que ocurra exactamente un
evento es aproximadamente λh
28

𝑃(𝑁(ℎ)=1)
lim = λ
ℎ
ℎ→0
e. En un intervalo pequeño de longitud h, la probabilidad de que ocurran dos o más
evento es aproximadamente 0
𝑃(𝑁(ℎ)≥2)
lim = 0
ℎ
ℎ→0
Proceso Poisson No Homogéneo
El proceso de Poisson homogéneo asume que los eventos ocurren con la misma
probabilidad en cualquier intervalo de igual longitud. Esto no siempre es realista, por lo que
se introduce el proceso de Poisson no homogéneo, que permite que la tasa de ocurrencia
varíe en el tiempo.
Sea N(t) el número de eventos ocurridos hasta el instante t, entonces {N(t), t ≥ 0} es un proceso
de Poisson no homogéneo con función de intensidad λ(t), si:
a. Condición Inicial: comienza en el instante 0, N(0) = 0
b. Incremento Independiente: el número de eventos en intervalos de tiempo distintos
son independientes.
c. lim P {exactamente 1 evento entre t y t + h}/h = λ(t)
ℎ→0
d. lim P {2 o más eventos entre t y t + h}/h = 0
ℎ→0
En el proceso no homogéneo tenemos λ(t) varía con el tiempo, permitiendo modelar
situaciones donde la tasa de ocurrencia de eventos cambia a lo largo del tiempo.
29