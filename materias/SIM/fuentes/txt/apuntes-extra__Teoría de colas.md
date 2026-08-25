|     |     |     |     | Teor´ıa | de Colas |     |     |
| --- | --- | --- | --- | ------- | -------- | --- | --- |
TC: Parte de la Investigacio´n Operativa que estudia el comportamiento de siste-
| mas      | cuyos     | elementos | incluyen | l´ıneas | de espera | (colas). |     |
| -------- | --------- | --------- | -------- | ------- | --------- | -------- | --- |
| IO 07/08 | - Teor´ıa | de Colas  |          |         |           |          | 1   |

|     |     |     | Teor´ıa | de Colas: | ejemplos |     |
| --- | --- | --- | ------- | --------- | -------- | --- |
• personas esperando por un servicio (bibliotecas, bancos, gasolineras, urgen-
| cias | en hospital, | . . . | ),  |     |     |     |
| ---- | ------------ | ----- | --- | --- | --- | --- |
• ma´quinas esperando por una reparacio´n, piezas de un producto esperando a
ser ensambladas,
• programas de ordenador esperando a ser ejecutados por un procesador,
• informacio´n de internet esperando en un nodo para ser transferida a su destino,
| • aviones |           | esperando | a despegar | o aterrizar, |     |     |
| --------- | --------- | --------- | ---------- | ------------ | --- | --- |
| IO 07/08  | - Teor´ıa | de Colas  |            |              |     | 2   |

|     |     |     | Teor´ıa | de Colas: | historia |     |
| --- | --- | --- | ------- | --------- | -------- | --- |
Se inicio´ con A. K. Erlang, en la compan˜´ıa telefo´nica estatal de Dinamarca (prin-
| cipios | del | siglo XX). |     |     |     |     |
| ------ | --- | ---------- | --- | --- | --- | --- |
Se analizaron los tiempos de espera de llamadas a centralitas automa´ticas (con-
| gestio´n | de  | tra´fico). |     |     |     |     |
| -------- | --- | ---------- | --- | --- | --- | --- |
• Objetivo: satisfacer la demanda incierta en el sistema telefo´nico con el menor
| coste    | para      | la compan˜´ıa. |     |     |     |     |
| -------- | --------- | -------------- | --- | --- | --- | --- |
| IO 07/08 | - Teor´ıa | de Colas       |     |     |     | 3   |

Teor´ıa de Colas
Introduccio´n.
| Elementos |     | y relaciones | en un | sistema. |     |
| --------- | --- | ------------ | ----- | -------- | --- |
M/M/1.
Modelo
| Modelo |     | M/M/s.   |     |     |     |
| ------ | --- | -------- | --- | --- | --- |
| Modelo |     | M/M/1/k. |     |     |     |
Aplicaciones.
| IO 07/08 | - Teor´ıa | de Colas |     |     | 4   |
| -------- | --------- | -------- | --- | --- | --- |

Introduccio´ n
Las l´ıneas de espera generan malestar, ineficiencia, retraso y otros problemas,
| lo que | origina | un coste | de  | tiempo | y econo´mico. |     |
| ------ | ------- | -------- | --- | ------ | ------------- | --- |
Es muy importante evaluar el balance entre el aumento del nivel de servicio y el
| taman˜o | de  | las colas | de espera. |     |     |     |
| ------- | --- | --------- | ---------- | --- | --- | --- |
Por tanto, es necesario entender la relacio´n entre el nu´mero de servidores en un
sistema (o eficacia de los mismos) y la cantidad de tiempo gastado en la cola (o
| cantidad | de  | clientes | en la | misma). |     |     |
| -------- | --- | -------- | ----- | ------- | --- | --- |
En sistemas de colas sencillos dichas relaciones se pueden encontrar anal´ıtica-
mente. En sistemas ma´s complejos se pueden analizar mediante simulacio´n.
| IO 07/08 | - Teor´ıa | de Colas |     |     |     | 5   |
| -------- | --------- | -------- | --- | --- | --- | --- |

Introduccio´ n
• Elementos ma´s importantes en un sistema de colas: clientes y servicio.
Los clientes se caracterizan por los intervalos de tiempo que separan sus llega-
das.
El servicio se caracteriza por el tipo y tiempo de servicio, adema´s de por el
nu´mero de servidores. El tipo de servicio o disciplina representa el orden en el
| que | los clientes | se  | seleccionan | de la | cola. |     |
| --- | ------------ | --- | ----------- | ----- | ----- | --- |
Las llegadas de clientes pueden ser deterministas o aleatorios (en este caso se
| modelan | mediante |     | una distribucio´n |     | estad´ıstica). |     |
| ------- | -------- | --- | ----------------- | --- | -------------- | --- |
Los tiempos de servicio tambie´n pueden ser deterministas o aleatorios (distribu-
| cio´n    | estad´ıstica). |          |     |     |     |     |
| -------- | -------------- | -------- | --- | --- | --- | --- |
| IO 07/08 | - Teor´ıa      | de Colas |     |     |     | 6   |

|     |     |     | Introduccio´ | n: tipos | de sistemas |     |
| --- | --- | --- | ------------ | -------- | ----------- | --- |
Las variaciones en un sistema de colas pueden ser mu´ltiples. So´lo se pueden
resolver de forma anal´ıtica un conjunto reducido de sistemas.
| IO 07/08 | - Teor´ıa | de Colas |     |     |     | 7   |
| -------- | --------- | -------- | --- | --- | --- | --- |

|            |       |         | Elementos     |          | de            | un    | sistema:      | Llegadas |     |
| ---------- | ----- | ------- | ------------- | -------- | ------------- | ----- | ------------- | -------- | --- |
| Pueden     |       | existir | una           | o varias | fuentes.      |       |               |          |     |
| Se         | suele | asumir  | independencia |          |               | entre | llegadas.     |          |     |
| Intervalos |       | entre   | llegadas:     |          | deterministas |       | o aleatorios. |          |     |
Tasa de llegadas: λ ≡ nu´mero medio de clientes que acceden al sistema por
| unidad |     | de tiempo. |     |     |     |     |     |     |     |
| ------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
1
| Tiempo |     | medio | entre | llegadas: |     | .   |     |     |     |
| ------ | --- | ----- | ----- | --------- | --- | --- | --- | --- | --- |
λ
| IO 07/08 | - Teor´ıa | de Colas |     |     |     |     |     |     | 8   |
| -------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |

|     |     | Elementos |     |     | de  | un  | sistema: |     | Fuente | de entrada |     |
| --- | --- | --------- | --- | --- | --- | --- | -------- | --- | ------ | ---------- | --- |
Puede ser infinita o finita (sistemas abiertos o cerrados, respectivamente).
Ejemplo de sistema abierto: un banco, ya que es pra´cticamente imposible que
| todos |     | los posibles |     | clientes |     | coincidan |     | en su | llegada. |     |     |
| ----- | --- | ------------ | --- | -------- | --- | --------- | --- | ----- | -------- | --- | --- |
Ejemplo de sistema cerrado: un servidor de internet con un nu´mero relati-
vamente pequen˜o de usuarios autorizados (es posible que en un momento
| determinado |     |     | se conecten |     |     | todos | los | usuarios | al servidor). |     |     |
| ----------- | --- | --- | ----------- | --- | --- | ----- | --- | -------- | ------------- | --- | --- |
Si la fuente es finita, entonces el nu´mero de clientes en la cola afecta al nu´me-
| ro  | de clientes |     | fuera | del | sistema. |     |     |     |     |     |     |
| --- | ----------- | --- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- |
La llegada puede ser en bloque o de forma unitaria. Frecuentemente el bloque
| se       | trata     | como     | un  | solo | cliente. |     |     |     |     |     |     |
| -------- | --------- | -------- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- |
| IO 07/08 | - Teor´ıa | de Colas |     |      |          |     |     |     |     |     | 9   |

|        |     |                  | Introduccio´ |     |     | n: Clientes |     |     |
| ------ | --- | ---------------- | ------------ | --- | --- | ----------- | --- | --- |
| Pueden |     | ser impacientes. |              |     |     |             |     |     |
Por tanto, los clientes se pueden perder, bien porque no entran en el sistema,
| bien | porque | abandonan |     | tras un | tiempo | en el | sistema. |     |
| ---- | ------ | --------- | --- | ------- | ------ | ----- | -------- | --- |
Tambie´n, los clientes pueden percibir un ritmo ma´s acelerado en una cola
| distinta |           | y por tanto | decidir | cambiarse. |     |     |     |     |
| -------- | --------- | ----------- | ------- | ---------- | --- | --- | --- | --- |
| IO 07/08 | - Teor´ıa | de Colas    |         |            |     |     |     | 10  |

|       | Elementos |         |               | de       | un sistema: |          | Cola | o canal | de espera |     |
| ----- | --------- | ------- | ------------- | -------- | ----------- | -------- | ---- | ------- | --------- | --- |
| Puede |           | ser de  | uno           | o varios | canales.    |          |      |         |           |     |
| Puede |           | existir | interferencia |          | entre       | canales. |      |         |           |     |
| Puede |           | ser de  | capacidad     |          | limitada.   |          |      |         |           |     |
Disciplina de la cola: orden de seleccio´n en el servicio (FIFO, LIFO, aleato-
| rio,     | orden     | de       | prioridad, |     | etc.). |     |     |     |     |     |
| -------- | --------- | -------- | ---------- | --- | ------ | --- | --- | --- | --- | --- |
| IO 07/08 | - Teor´ıa | de Colas |            |     |        |     |     |     |     | 11  |

|        |       |         | Elementos     |          | de          | un    | sistema: | Servicio     |     |
| ------ | ----- | ------- | ------------- | -------- | ----------- | ----- | -------- | ------------ | --- |
| Pueden |       | existir | uno           | o varios | servidores. |       |          |              |     |
| Se     | suele | asumir  | independencia |          |             | entre | tiempos  | de servicio. |     |
Duracio´n
|     |     | de  | los servicios: |     | deterministas |     | o aleatorios. |     |     |
| --- | --- | --- | -------------- | --- | ------------- | --- | ------------- | --- | --- |
Tasa de servicio: µ ≡ nu´mero medio de clientes que son atendidos por unidad
| de  | tiempo. |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
1
| Tiempo |     | medio | de servicio: |     | .   |     |     |     |     |
| ------ | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- |
µ
| IO 07/08 | - Teor´ıa | de Colas |     |     |     |     |     |     | 12  |
| -------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     | Ana´lisis |     | de sistemas |     | de colas |     |
| --- | --- | --- | --------- | --- | ----------- | --- | -------- | --- |
Una vez caracterizado el sistema, se pueden contestar a las siguientes pregun-
tas:
¿Que´ proporcio´n de tiempo esta´n los servidores desocupados?.
¿Cua´l es el tiempo medio de espera para un cliente?, ¿es e´ste un tiempo
razonable?, ¿se pierden clientes por tiempos de espera largos?.
|     |     |     | an˜adir | ma´s |     |     |     |     |
| --- | --- | --- | ------- | ---- | --- | --- | --- | --- |
¿Es conveniente servidores para reducir el tiempo medio de es-
pera?.
| ¿Cua´l |     | es el nu´mero |     | medio | de clientes | en cola?. |     |     |
| ------ | --- | ------------- | --- | ----- | ----------- | --------- | --- | --- |
¿Cua´l es la probabilidad de que la espera sea mayor que una determinada
| longitud |           | en un    | tiempo | determinado?. |     |     |     |     |
| -------- | --------- | -------- | ------ | ------------- | --- | --- | --- | --- |
| . .      | .         |          |        |               |     |     |     |     |
| IO 07/08 | - Teor´ıa | de Colas |        |               |     |     |     | 13  |

|     |     |     | Ana´lisis | de sistemas | de colas |     |
| --- | --- | --- | --------- | ----------- | -------- | --- |
• Notacio´n de Kendall: las caracter´ısticas del sistema se especifican por los
s´ımbolos:
A/B/s/k/t/d/
donde A y B denotan las distribuciones de los tiempos entre llegadas y de ser-
| vicio, | respectivamente. |     |     |     |     |     |
| ------ | ---------------- | --- | --- | --- | --- | --- |
s denota el nu´mero de servidores en paralelo o canales, k denota la capacidad
del sistema, t denota el taman˜o de la fuente de entrada, y d es la disciplina de
la cola.
| IO 07/08 | - Teor´ıa | de Colas |     |     |     | 14  |
| -------- | --------- | -------- | --- | --- | --- | --- |

|      |               |     |     |                | Ana´lisis |     | de sistemas | de colas |     |
| ---- | ------------- | --- | --- | -------------- | --------- | --- | ----------- | -------- | --- |
| • La | distribucio´n |     |     | puede          | ser       |     |             |          |     |
| M    | Exponencial   |     |     |                |           |     |             |          |     |
| D    | Constante     |     |     | o determinista |           |     |             |          |     |
| E    | Erlang        |     | de  | para´metro     |           | k   |             |          |     |
k
| G        | Gene´rica  |         |       | e independiente |        |        |     |     |     |
| -------- | ---------- | ------- | ----- | --------------- | ------ | ------ | --- | --- | --- |
| • La     | disciplina |         | puede |                 | ser    |        |     |     |     |
| FCFS     |            | First   | come, |                 | first  | served |     |     |     |
| LCFS     |            | Last    | come, |                 | first  | served |     |     |     |
| SIRO     |            | Service |       | in              | random | order  |     |     |     |
| GD       |            | General |       | discipline      |        |        |     |     |     |
| IO 07/08 | - Teor´ıa  | de      | Colas |                 |        |        |     |     | 15  |

|     |          |            | Ana´lisis |        | de sistemas |      | de colas |     |
| --- | -------- | ---------- | --------- | ------ | ----------- | ---- | -------- | --- |
| Por | ejemplo, | un sistema |           | que se | describe    | como |          |     |
M/M/1/∞/∞/FCFS
denota un sistema abierto que contiene un u´nico servidor con tiempos de lle-
gada y servicio exponenciales, capacidad infinita y disciplina primero que entra,
| primero | que | se sirve. |     |     |     |     |     |     |
| ------- | --- | --------- | --- | --- | --- | --- | --- | --- |
So´lo un nu´mero pequen˜o de sistemas se puede resolver anal´ıticamente.
| Modelos  | sencillos: |          | M/M/1/, | M/M/s/, |     | M/M/1/k. |     |     |
| -------- | ---------- | -------- | ------- | ------- | --- | -------- | --- | --- |
| IO 07/08 | - Teor´ıa  | de Colas |         |         |     |          |     | 16  |

Distribuciones
En los sistemas de colas normalmente se asume que tanto las llegadas de clien-
| tes como |     | los tiempos |     | de  | servicio | son aleatorios. |     |     |     |     |
| -------- | --- | ----------- | --- | --- | -------- | --------------- | --- | --- | --- | --- |
Es usual suponer que los tiempos entre llegadas y los de servicio se distribuyan
de forma exponencial. En este caso, la probabilidad instanta´nea de ocurrencia
| de un | suceso | en  | las | siguientes |      | t unidades | de  | tiempo | es: |     |
| ----- | ------ | --- | --- | ---------- | ---- | ---------- | --- | ------ | --- | --- |
|       |        |     |     |            | f(t) | = λe −λt   |     | t ≥ 0, |     |     |
para
| donde | λ denota |     | la  | tasa de | llegadas. |     |     |     |     |     |
| ----- | -------- | --- | --- | ------- | --------- | --- | --- | --- | --- | --- |
Esta distribucio´n es u´til ya que tiene la propiedad de falta de memoria y esta-
cionariedad (el sistema se comporta, transcurrido un plazo, de forma estable e
| independientemente |           |          |     | de las | condiciones |     | iniciales). |     |     |     |
| ------------------ | --------- | -------- | --- | ------ | ----------- | --- | ----------- | --- | --- | --- |
| IO 07/08           | - Teor´ıa | de Colas |     |        |             |     |             |     |     | 17  |

Distribuciones
Una distribucio´n exponencial de los tiempos entre llegadas implica una distribu-
cio´n de Poisson para las llegadas, es decir, el nu´mero de llegadas en el intervalo
(0, t] es una Poisson. Una distribucio´n de Poisson describe la probabilidad de
que lleguen n clientes en las siguientes t unidades de tiempo:
(λt)n
−λt
|     |     |     | P(X | = n) = | e   | para | n = 0, | 1, . . . |     |
| --- | --- | --- | --- | ------ | --- | ---- | ------ | -------- | --- |
t
n!
En la pra´ctica, se habla de llegadas Poisson y tiempos de servicio exponencial.
En general se supone que el sistema se encuentra en estado estacionario (es-
| tabilidad | independiente |          |     | del tiempo). |     |     |     |     |     |
| --------- | ------------- | -------- | --- | ------------ | --- | --- | --- | --- | --- |
| IO 07/08  | - Teor´ıa     | de Colas |     |              |     |     |     |     | 18  |

Notacio´ n universal
• Objetivo: dados los siguientes para´metros (se suelen estimar estad´ısticamen-
te)
| λ        | ≡ tasa    | de llegadas.   |     |
| -------- | --------- | -------------- | --- |
| µ        | ≡ tasa    | de servicio.   |     |
| s        | ≡ nu´mero | de servidores. |     |
| IO 07/08 | - Teor´ıa | de Colas       | 19  |

Notacio´ n universal
se calcula
λ
ρ = ≡ factor de utilizacio´n del sistema o intensidad de tra´fico (proporcio´n
sµ
de tiempo esperado en el que los servidores esta´n ocupados). Si ρ < 1 enton-
ces el sistema se estabiliza. En otro caso el nu´mero de clientes en el sistema
| se  | incrementa | sin l´ımite. |     |
| --- | ---------- | ------------ | --- |
L ≡ valor esperado del nu´mero de clientes en el sistema (la variable se denota
| por | N). |     |     |
| --- | --- | --- | --- |
L ≡ valor esperado del nu´mero de clientes en cola (la variable se denota por
q
| N   | ).  |     |     |
| --- | --- | --- | --- |
q
| IO 07/08 | - Teor´ıa | de Colas | 20  |
| -------- | --------- | -------- | --- |

Notacio´ n universal
y
W ≡ tiempo medio de espera en el sistema (la variable se denota por T).
W ≡ tiempo medio de espera en la cola (la variable se denota por T ).
q q
p ≡ probabilidad de que n clientes este´n en el sistema (en estado estacio-
n
nario).
| c¯       | ≡ nu´mero | medio    | de clientes | en servicio. |     |
| -------- | --------- | -------- | ----------- | ------------ | --- |
| IO 07/08 | - Teor´ıa | de Colas |             |              | 21  |

|            |     |            | Relaciones | ba´sicas: |      | Modelo | general |     |
| ---------- | --- | ---------- | ---------- | --------- | ---- | ------ | ------- | --- |
| • Fo´rmula |     | de Little: | L = λW     | y L       | = λW | .      |         |     |
|            |     |            |            | q         | q    |        |         |     |
1
| Adema´s, | W   | = W | + . |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- |
q
µ
| De estas | tres | fo´rmulas | se deduce: |     | L = L | + λ . |     |     |
| -------- | ---- | --------- | ---------- | --- | ----- | ----- | --- | --- |
q
µ
| IO 07/08 | - Teor´ıa | de Colas |     |     |     |     |     | 22  |
| -------- | --------- | -------- | --- | --- | --- | --- | --- | --- |

|     |     |     | Relaciones |     | ba´sicas: |     | Modelo |     | general |     |
| --- | --- | --- | ---------- | --- | --------- | --- | ------ | --- | ------- | --- |
Se dice que el sistema se encuentra en el estado n si existen exactamente n
| clientes | en  | el mismo. |     |     |     |     |     |     |     |     |
| -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
• Ecuaciones de balance de flujo (la tasa esperada de llegada al estado n es
igual a la tasa esperada de salida del estado n en estado estacionario):
|          |           |          |     |         |     | p λ   | =     | p µ   |       |     |
| -------- | --------- | -------- | --- | ------- | --- | ----- | ----- | ----- | ----- | --- |
|          |           |          |     |         |     | 0     | 0     | 1 1   |       |     |
|          |           |          |     |         | p λ | + p µ | =     | p λ + | p µ   |     |
|          |           |          |     |         | 0 0 | 2     | 2     | 1 1   | 1 1   |     |
|          |           |          |     |         | p λ | + p µ | =     | p λ + | p µ   |     |
|          |           |          |     |         | 1 1 | 3     | 3     | 2 2   | 2 2   |     |
|          |           |          |     |         |     | ·     | · · = | · · · |       |     |
|          |           |          |     | p λ     | + p | µ     | =     | p λ   | + p µ |     |
|          |           |          |     | n−1 n−1 | n+1 | n+1   |       | n n   | n n   |     |
|          |           |          |     |         |     | ·     | · · = | · · · |       |     |
| IO 07/08 | - Teor´ıa | de Colas |     |         |     |       |       |       |       | 23  |

|               |     |     | Relaciones     |     | ba´sicas:  |     | Modelo |      | general |     |
| ------------- | --- | --- | -------------- | --- | ---------- | --- | ------ | ---- | ------- | --- |
| Si resolvemos |     |     | las ecuaciones |     | anteriores |     | para   | p se | obtiene |     |
i
λ
0
|     |     |     |     |     | p   | = p |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | 1   | 0   |     |     |     |     |
µ
1
λ λ
1 0
|     |     |     |     |     | p   | =   | p   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | 2   |     | 0   |     |     |     |
µ µ
2 1
|     |     |     |     |     |       | λ λ     | λ       |     |     |     |
| --- | --- | --- | --- | --- | ----- | ------- | ------- | --- | --- | --- |
|     |     |     |     |     |       | 2 1     | 0       |     |     |     |
|     |     |     |     |     | p     | =       | p       |     |     |     |
|     |     |     |     |     | 3     |         | 0       |     |     |     |
|     |     |     |     |     |       | µ µ     | µ       |     |     |     |
|     |     |     |     |     |       | 3 2     | 1       |     |     |     |
|     |     |     |     |     | · · · | = · · · |         |     |     |     |
|     |     |     |     |     |       | λ       | · · · λ | λ   |     |     |
|     |     |     |     |     |       | n−1     |         | 1 0 |     |     |
|     |     |     |     |     | p     | =       |         | p   | .   |     |
|     |     |     |     |     | n     |         |         | 0   |     |     |
|     |     |     |     |     |       | µ       | · · · µ | µ   |     |     |
|     |     |     |     |     |       | n       | 2       | 1   |     |     |
Para calcular p (prob. de que el sistema este´ vac´ıo), se utiliza:
0
|          |           |          |     | p + | p + | p + · | · · + p | + · · | · = 1. |     |
| -------- | --------- | -------- | --- | --- | --- | ----- | ------- | ----- | ------ | --- |
|          |           |          |     | 0   | 1   | 2     |         | n     |        |     |
| IO 07/08 | - Teor´ıa | de Colas |     |     |     |       |         |       |        | 24  |

|         |       |     |     |        |     | Modelo |       | M/M/1  |      |     |           |     |
| ------- | ----- | --- | --- | ------ | --- | ------ | ----- | ------ | ---- | --- | --------- | --- |
| En este | caso, |     | λ   | = λ, µ | =   | µ, ρ   | = λ < | 1 para | todo | n.  | Entonces, |     |
|         |       |     | n   |        | n   |        |       |        |      |     |           |     |
µ
n
|        |     |     |        |     |     | p = | ρ p | , p | = 1 − | ρ,  |     |     |
| ------ | --- | --- | ------ | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
|        |     |     |        |     |     | n   | 0   |     | 0     |     |     |     |
| por lo | que | p   | = ρn(1 | −   | ρ). |     |     |     |       |     |     |     |
n
Por tanto,
∞
ρ
X
|     |     |     |     | L = | E(N) | =   | np  | =   |     | (ejercicio). |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ------------ | --- | --- |
n
|     |     |     |     |     |     |     |     |     | 1 − ρ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
n=0
| y de | la misma |     | forma, |     |     |     |     |     |     |     |     |     |
| ---- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∞
ρ2
X
|     |     |     | L   | = E(N | )   | =   | (n − | 1)p | =   |     | (ejercicio). |     |
| --- | --- | --- | --- | ----- | --- | --- | ---- | --- | --- | --- | ------------ | --- |
|     |     |     |     | q     | q   |     |      |     | n   |     |              |     |
|     |     |     |     |       |     |     |      |     | 1 − | ρ   |              |     |
n=1
| IO 07/08 | - Teor´ıa | de Colas |     |     |     |     |     |     |     |     |     | 25  |
| -------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |             |            |     | Modelo | M/M/1 |      |     |     |     |
| --- | ----------- | ---------- | --- | ------ | ----- | ---- | --- | --- | --- |
| Por | la fo´rmula | de Little: |     |        |       |      |     |     |     |
|     |             |            |     |        | L     | 1    |     |     |     |
|     |             |            | W = | E(T)   | = =   |      |     |     |     |
|     |             |            |     |        | λ µ(1 | − ρ) |     |     |     |
1 ρ
|          |     |         | W =  | E(T | ) = W − | =       | .   |     |     |
| -------- | --- | ------- | ---- | --- | ------- | ------- | --- | --- | --- |
|          |     |         | q    | q   |         |         |     |     |     |
|          |     |         |      |     |         | µ µ(1 − | ρ)  |     |     |
| Adema´s, | c¯  | = L − L | = ρ. |     |         |         |     |     |     |
q
La probabilidad de que haya ma´s de k clientes en el sistema es:
k−1 k−1
X X
|     |     |     |     |     | n   |     |     | k   | k   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P(N ≥ k) = 1 − p = 1 − ρ (1 − ρ) = 1 − (1 − ρ)(1 − ρ )/(1 − ρ) = ρ .
k
n=0 n=0
Por tanto,
k
|          |           |          |     | P(N | < k) = | 1 − ρ . |     |     |     |
| -------- | --------- | -------- | --- | --- | ------ | ------- | --- | --- | --- |
| IO 07/08 | - Teor´ıa | de Colas |     |     |        |         |     |     | 26  |

|     |     |     | Modelo | M/M/1: | Ejemplo |     |
| --- | --- | --- | ------ | ------ | ------- | --- |
La tasa de llegadas de estudiantes al mostrador de una biblioteca es de 10
por hora. En el mostrador existe una sola persona y atiende con una tasa de 5
minutos por persona. ¿Cua´les son las medidas de comportamiento del sistema?
• Datos: λ = 10 (tasa de llegadas), µ = 60/5 = 12 (tasa de servicio), s = 1
(nu´mero de servidores). Se suponen distribuciones exponenciales.
• Resultados:
|     |     |     | L   | 5   | p 0.16 |     |
| --- | --- | --- | --- | --- | ------ | --- |
0
|     |     |     | L   | 4.16 | p 0.14 |     |
| --- | --- | --- | --- | ---- | ------ | --- |
|     |     |     | q   |      | 1      |     |
|     |     |     | W   | 0.5  | p 0.11 |     |
2
|     |     |     | W   | 0.42 | p 0.09 |     |
| --- | --- | --- | --- | ---- | ------ | --- |
|     |     |     | q   |      | 3      |     |
|     |     |     | ρ   | 0.83 | p 0.08 |     |
4
| IO 07/08 | - Teor´ıa | de Colas |     |     |     | 27  |
| -------- | --------- | -------- | --- | --- | --- | --- |

|     |     |     |     | Modelo | M/M/s |     |     |     |
| --- | --- | --- | --- | ------ | ----- | --- | --- | --- |
En sistemas con mu´ltiples servidores (s > 1), la tasa de servicio depende del
nu´mero de clientes en el sistema. En este caso, ρ = λ < 1, y se puede probar
sµ
que
1
|     |     |     | p = |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
|     |     |     |     | Ps−1 | (λ/µ)n | (λ/µ)s |     |     |
| --- | --- | --- | --- | ---- | ------ | ------ | --- | --- |
+
|     |     |     |     | n=0 | n!  | s!(1−ρ) |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- |
y
(λ/µ)np
0
|     |     |     | p = |     | , si | 0 ≤ | n ≤ s |     |
| --- | --- | --- | --- | --- | ---- | --- | ----- | --- |
n
n!
(λ/µ)np
0
|     |     |     | p = |     | , si | n > | s.  |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- |
n
s!sn−s
| IO 07/08 | - Teor´ıa | de Colas |     |     |     |     |     | 28  |
| -------- | --------- | -------- | --- | --- | --- | --- | --- | --- |

|     |     |     |     | Modelo | M/M/s |     |     |     |     |
| --- | --- | --- | --- | ------ | ----- | --- | --- | --- | --- |
Adema´s,
|     |     |     |     |     | (λ/µ)s p ρ |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
0
L =
q
s! (1 − ρ)2
L
q
W =
q
λ
1
|     |     |     |     | W = | W + |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
q
µ
λ
|     |     |     |     | L = | λW = L + | .   |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
q
µ
|       |        |          |         |       |              |     | λ )s | p   |     |
| ----- | ------ | -------- | ------- | ----- | ------------ | --- | ---- | --- | --- |
| Prob. | de que | un nuevo | cliente | tenga | que esperar: | p = | (    | 0 . |     |
w
|          |           |          |     |     |     |     | µ s! | (1−ρ) |     |
| -------- | --------- | -------- | --- | --- | --- | --- | ---- | ----- | --- |
| IO 07/08 | - Teor´ıa | de Colas |     |     |     |     |      |       | 29  |

|     |     |     | Modelo | M/M/s: | Ejemplo |     |
| --- | --- | --- | ------ | ------ | ------- | --- |
Un banco dispone de 3 ventanillas de atencio´n. Los clientes llegan al banco con
tasa de 1 por minuto. El tiempo de servicio es de 2 minutos por persona.
• Datos: λ = 60 (tasa de llegadas), µ = 60/2 = 30 (tasa de servicio), s = 3
| (nu´mero | de  | servidores). |     |     |     |     |
| -------- | --- | ------------ | --- | --- | --- | --- |
• Resultados:
|     |     |     | L   | 2.89 | p 0.11 |     |
| --- | --- | --- | --- | ---- | ------ | --- |
0
|     |     |     | L   | 0.89  | p 0.22 |     |
| --- | --- | --- | --- | ----- | ------ | --- |
|     |     |     | q   |       | 1      |     |
|     |     |     | W   | 0.049 | p 0.22 |     |
2
|     |     |     | W   | 0.015 | p 0.15 |     |
| --- | --- | --- | --- | ----- | ------ | --- |
|     |     |     | q   |       | 3      |     |
|     |     |     | ρ   | 0.67  | p 0.10 |     |
4
| IO 07/08 | - Teor´ıa | de Colas |     |     |     | 30  |
| -------- | --------- | -------- | --- | --- | --- | --- |

|     |     |     |     | Modelo |     | M/M/1/k |     |     |     |
| --- | --- | --- | --- | ------ | --- | ------- | --- | --- | --- |
En este caso, si el sistema esta´ lleno (la capacidad es k) no se permite la en-
trada de nuevos clientes al sistema. Por tanto, la tasa de llegada efectiva no es
constante y var´ıa con el tiempo (en funcio´n de si el sistema esta´ lleno o no):
|         |       |     |     |     | λ   | = λ(1 − | p ). |     |     |
| ------- | ----- | --- | --- | --- | --- | ------- | ---- | --- | --- |
|         |       |     |     |     | ef  |         | k    |     |     |
| En este | caso, |     |     |     |     |         |      |     |     |
n
|      |        |        | p      | = ρ | p , | para n | = 0, 1, . . | . , k |     |
| ---- | ------ | ------ | ------ | --- | --- | ------ | ----------- | ----- | --- |
|      |        |        |        | n   | 0   |        |             |       |     |
| y no | existe | estado | k + 1. |     |     |        |             |       |     |
Por tanto,
|          |           |          |     | p + | p + | p + · · | · + p = 1. |     |     |
| -------- | --------- | -------- | --- | --- | --- | ------- | ---------- | --- | --- |
|          |           |          |     | 0   | 1   | 2       | k          |     |     |
| IO 07/08 | - Teor´ıa | de Colas |     |     |     |         |            |     | 31  |

|       |          |            |     | Modelo    |       | M/M/1/k |           |     |
| ----- | -------- | ---------- | --- | --------- | ----- | ------- | --------- | --- |
| De la | anterior | expresio´n |     | se deduce | que   |         |           |     |
|       |          |            |     |           | 1 − ρ |         |           |     |
|       |          |            |     | p =       |       | ,       | si λ 6= µ |     |
0
ρk+1
1 −
1
|     |     |     |     | p = | ,   | si λ | = µ. |     |
| --- | --- | --- | --- | --- | --- | ---- | ---- | --- |
0
1 + k
distribucio´n λ > µ).
| y siempre |           | existe   | una |     | estacionaria |     | (aunque |     |
| --------- | --------- | -------- | --- | --- | ------------ | --- | ------- | --- |
| IO 07/08  | - Teor´ıa | de Colas |     |     |              |     |         | 32  |

|          |     |          |     |                | Modelo | M/M/1/k     |        |      |        |     |
| -------- | --- | -------- | --- | -------------- | ------ | ----------- | ------ | ---- | ------ | --- |
| Adema´s, | se  | obtienen |     | las siguientes |        | relaciones: |        |      |        |     |
|          |     |          |     |                |        | 1)ρk        | kρk+1) |      |        |     |
|          |     |          |     | ρ(1 −          | (k +   | +           |        |      |        |     |
|          |     |          | L = |                |        |             |        | , si | λ 6= µ |     |
ρk+1)
|     |     |     |     | (1  | − ρ)(1 | −   |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
k
|     |     |     | L = | ,   | si λ = | µ.  |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
2
y
|     |     |     |     |     | L   | = L − (1 | − p | )   |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
|     |     |     |     |     | q   |          |     | 0   |     |     |
L
|     |     |     |     |     | W   | =   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
λ
ef
1
|     |     |     |     |     | W   | = W − | .   |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
q
µ
| IO 07/08 | - Teor´ıa | de Colas |     |     |     |     |     |     |     | 33  |
| -------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     | Limitaciones | de los | sistemas | de colas |     |
| --- | --- | ------------ | ------ | -------- | -------- | --- |
• La resolucio´n anal´ıtica de los sistemas se complica a medida que los sistemas
se hacen ma´s complejos. De hecho, para muchos sistemas no existe resolucio´n
anal´ıtica.
• Ejemplo: un sistema de servidores en paralelo y en serie con mu´ltiples canales
| y distribuciones |     | generales. |     |     |     |     |
| ---------------- | --- | ---------- | --- | --- | --- | --- |
• En sistemas de colas complejos conviene utilizar simulaciones para estudiar
su comportamiento.
| IO 07/08 | - Teor´ıa | de Colas |     |     |     | 34  |
| -------- | --------- | -------- | --- | --- | --- | --- |

|     |     |     | Aplicaciones |     | de Teor´ıa | de Colas |     |
| --- | --- | --- | ------------ | --- | ---------- | -------- | --- |
Se pueden usar los resultados de Teor´ıa de Colas para la toma de decisiones:
| ¿Cua´ntos |     | servidores | emplear | en el | sistema? |     |     |
| --------- | --- | ---------- | ------- | ----- | -------- | --- | --- |
¿Es mejor usar un u´nico servidor ra´pido o muchos servidores ma´s lentos?
¿Es mejor usar servidores ide´nticos o servidores espec´ıficos?
Objetivo: minimizar el coste total = coste de servicio + coste de espera.
| IO 07/08 | - Teor´ıa | de Colas |     |     |     |     | 35  |
| -------- | --------- | -------- | --- | --- | --- | --- | --- |

|     |     |     | Aplicaciones |     | de Teor´ıa | de Colas |     |
| --- | --- | --- | ------------ | --- | ---------- | -------- | --- |
• Coste de servicio: coste al aumentar la capacidad de servicio.
La capacidad del servicio se puede aumentar an˜adiendo ma´s servidores, s %,
| o haciendo |     | servidores | ma´s eficientes, |     | µ %, | etc. |     |
| ---------- | --- | ---------- | ---------------- | --- | ---- | ---- | --- |
Habitualmente, la funcio´n de coste de servicio viene dada por C s, donde C
s s
| representa |     | el coste | por unidad | de tiempo | y   | servidor. |     |
| ---------- | --- | -------- | ---------- | --------- | --- | --------- | --- |
Tambie´n se utiliza C µ, donde C representa el coste por unidad de tiempo y
|          |           |          | µ         | µ   |     |     |     |
| -------- | --------- | -------- | --------- | --- | --- | --- | --- |
| unidad   | de        | tasa de  | servicio. |     |     |     |     |
| IO 07/08 | - Teor´ıa | de Colas |           |     |     |     | 36  |

|     |     |     | Aplicaciones |     | de Teor´ıa | de Colas |     |
| --- | --- | --- | ------------ | --- | ---------- | -------- | --- |
• Coste de espera: coste asociado a la espera de los clientes.
La espera de clientes genera tiempo perdido, pe´rdida de los mismos, etc.
Habitualmente, la funcio´n de coste de espera viene dada por C L(s), donde C
l l
denota el coste de espera por unidad de tiempo y cliente y L(s) es el valor
esperado del nu´mero de clientes en el sistema para s servidores.
Tambie´n se utiliza C W(µ), donde C denota el coste de espera por unidad de
|     |     |     | w   |     | w   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
tiempo y cliente y W(µ) es el valor esperado del tiempo medio de espera en el
| sistema  | para      | una      | tasa de | servicio | de µ unidades. |     |     |
| -------- | --------- | -------- | ------- | -------- | -------------- | --- | --- |
| IO 07/08 | - Teor´ıa | de Colas |         |          |                |     | 37  |

|     |     |     | Aplicaciones |     | de Teor´ıa | de Colas |     |
| --- | --- | --- | ------------ | --- | ---------- | -------- | --- |
La siguiente figura representa un modelo t´ıpico de costes (en euros por unidad
de tiempo):
El coste del servicio aumenta con el incremento en el nivel del servicio pero el
| coste | por | espera | disminuye | con el | nivel. |     |     |
| ----- | --- | ------ | --------- | ------ | ------ | --- | --- |
Hay que buscar el nivel de servicio que minimiza el coste total.
| IO 07/08 | - Teor´ıa | de Colas |     |     |     |     | 38  |
| -------- | --------- | -------- | --- | --- | --- | --- | --- |

|     |     | Ejemplo: |     | ¿cua´ntos |     | servidores |     | utilizar? |     |
| --- | --- | -------- | --- | --------- | --- | ---------- | --- | --------- | --- |
Un banco dispone de 3 ventanillas de atencio´n. Los clientes llegan al banco a
una tasa de 40 por hora. El tiempo de servicio es de 3 minutos por persona.
El banco se plantea si le conviene aumentar el nu´mero de ventanillas para sa-
| tisfacer | mejor | a los | clientes. |     |     |     |     |     |     |
| -------- | ----- | ----- | --------- | --- | --- | --- | --- | --- | --- |
El coste que le supone abrir una nueva ventanilla es de 6 euros la hora. El coste
| horario | de  | espera | se ha | estimado | en  | 18 euros | por cliente. |     |     |
| ------- | --- | ------ | ----- | -------- | --- | -------- | ------------ | --- | --- |
• Datos: λ = 40 (tasa de llegadas), µ = 60/3 = 20 (tasa de servicio), s = 3
| (nu´mero | de        | servidores), |     | C = | 6, C = | 18. |     |     |     |
| -------- | --------- | ------------ | --- | --- | ------ | --- | --- | --- | --- |
|          |           |              |     | s   | l      |     |     |     |     |
| IO 07/08 | - Teor´ıa | de Colas     |     |     |        |     |     |     | 39  |

|     |     |     | Ejemplo: |     | ¿cua´ntos |     | servidores |     | utilizar? |     |
| --- | --- | --- | -------- | --- | --------- | --- | ---------- | --- | --------- | --- |
• Resultados:
|          |           |          |       |          |          | s =     | 3   | s = 4      | s = 5   |     |
| -------- | --------- | -------- | ----- | -------- | -------- | ------- | --- | ---------- | ------- | --- |
|          |           |          |       | L        |          | 2.88889 |     | 2.17391    | 2.03980 |     |
|          |           |          | Coste | de       | servicio | 18.00   |     | 24.00      | 30.00   |     |
|          |           |          | Coste | de       | espera   | 52.00   |     | 39.13      | 36.72   |     |
|          |           |          | Coste |          | total    | 70.00   |     | 63.13      | 66.72   |     |
|          |           |          |       |          |          | so´lo   |     |            | ma´s.   |     |
| Por      | tanto,    | al banco | le    | interesa | abrir    |         | una | ventanilla |         |     |
| IO 07/08 | - Teor´ıa | de Colas |       |          |          |         |     |            |         | 40  |

|     | Ejemplo: |     | ¿un | servidor | ra´pido | o muchos | lentos? |     |
| --- | -------- | --- | --- | -------- | ------- | -------- | ------- | --- |
En un servidor de Internet existen 3 nodos que atienden peticiones a razo´n de
50 por minuto. El tiempo medio de servicio de cada nodo es de 3 segundos por
peticio´n.
En el servidor se plantean la posibilidad de instalar un u´nico nodo con tiempo de
servicio de 1 segundo por peticio´n. ¿Es conveniente esta opcio´n para reducir el
| tiempo | medio | de espera |     | en el sistema? |     |     |     |     |
| ------ | ----- | --------- | --- | -------------- | --- | --- | --- | --- |
• Datos: λ = 50 (tasa de llegadas), µ = 20 (tasa de servicio) con s = 3 (nu´mero
| de servidores), |           | y µ      | = 60 con | s = 1. |     |     |     |     |
| --------------- | --------- | -------- | -------- | ------ | --- | --- | --- | --- |
| IO 07/08        | - Teor´ıa | de Colas |          |        |     |     |     | 41  |

|     | Ejemplo: |     | ¿un | servidor | ra´pido | o muchos | lentos? |     |
| --- | -------- | --- | --- | -------- | ------- | -------- | ------- | --- |
• Resultados:
|     |     |     |     | s        | = 3 s  | = 1 |     |     |
| --- | --- | --- | --- | -------- | ------ | --- | --- | --- |
|     |     |     |     | W 0.1202 | 0.1000 |     |     |     |
Por tanto, es ma´s conveniente utilizar un ordenador ma´s ra´pido.
| IO 07/08 | - Teor´ıa | de Colas |     |     |     |     |     | 42  |
| -------- | --------- | -------- | --- | --- | --- | --- | --- | --- |