Simulación
Ejercicio 2
El ejercicio 2 en vez de ser una cola simple, tiene un par de servidores en serie. Por ello hay varias
modificaciones  al modelo inicial.
El sistema tiene dos servidores separados en serie, por lo cual hay dos colas esperando a ser
atendidas. Además, los clientes que van al servidor 2 son los que salen del servidor 1 (por ejemplo
si pensáramos en un consultorio individual, primero se pasa por la recepcionista que te controla la
orden y luego se espera al médico). Por ello NO existe una variable exógena que determine un
Arribo 2 (si fuera así sería como si uno pasa por la recepcionista y luego cuando espera al médico,
entrara otra persona por otro lado directamente al médico).

Nota: En los ejercicios se suele pedir un esquema del sistema real, que sería un esquema dibujado.

Diagrama de desencadenamiento de eventos

|     |     | Si S1 =’D’  | Si n1>0   |     | Si n2>0  |
| --- | --- | ----------- | --------- | --- | -------- |
|     |     |             |           |     |          |

|     | A   |     |        |     |     |
| --- | --- | --- | ------ | --- | --- |
|     |     |     | P1/A2  |     | P2  |

Eventos
A1: Arribo 1
P1/A2 : Partida del servidor 1 y arribo al servidor 2
P2: partida del servidor 2

Variables exógenas
  Tiempo de arribo: Tiempo en que llegan los clientes al sistema.
  Tiempo de servicio servidor 1: Tiempo que tarda el servidor 1 en atender a un cliente
  Tiempo de servicio servidor 2: Tiempo que tarda el servidor 2 en atender a un cliente

Parte a)
Variables endógenas
|     |     |     |    |    |     |
| --- | --- | --- | --- | --- | --- |
|     |     |    |    |     |     |
En la parte a del ejercicio pide solo q (t),  q (t), d (cli_at ), d (cli_at ) es decir las demoras y
|     |     | 1   | 2 1 1 | 2 2 |     |
| --- | --- | --- | ----- | --- | --- |
el tiempo promedio en cada cola. NO pide las utilizaciones de los servidores (observar el cambio en
el pseudocódigo del ej 1). Los promedios solicitados tienen la misma estructura que los del ejercicio
1, algunas variables de estado se duplican por dos.

Algoritmo parte a)
Nota importante!!!:  El pseudo código del ejercicio 1 estaba escrito literalmente, y al lado en azul la
fórmula correspondiente, a partir de ahora solo se escriben las fórmulas. No olvidar QUÉ significan
cada una de ellas.

Principal
Inicialización
  Mientras reloj <=Fin simulación
|     | Tiempos                                      |     |     |     |     |
| --- | -------------------------------------------- | --- | --- | --- | --- |
|     | Si evento seleccionado =’A1’ ir a Arribo 1   |     |     |     |     |
      Sino Si el evento seleccionado= ‘P1/A2’ ir a Partida1/Arribo2
|     |     | Sino ir a Partida 2  |     |     |     |
| --- | --- | -------------------- | --- | --- | --- |
Fin Si
|     | Fin Si    |     |     |     |     |
| --- | --------- | --- | --- | --- | --- |
  Fin mientras
| S. De Federico  |     |     |     |     |                1  |
| --------------- | --- | --- | --- | --- | ----------------- |

Simulación
Reporte
Tiempos
Buscar en la LEV el evento con menor tiempo de ocurrencia
Reloj = Tiempo en LEV
Inicialización
Reloj=0
A =0 acumulada del tamaño de cola 1
q1
A =0 acumulada del tamaño de cola 2
q2
d =0 acumulada de la demora en cola 1
1
d =0 acumulada de la demora en cola 2
2
cli_at =0 número de clientes atendidos en cola 1
1
cli_at =0 número de clientes atendidos en cola 2
2
n =0 número de clientes en cola 1
1
n =0 número de clientes en cola 2
2
Generar tiempo de arribo El Arribo es el evento que inicia el sistema (ver Diagrama de
Desencadenamiento
Guardar en LEV(A, Tiempo de arribo)
Guardar en LEV(P1/A2, ∞)
Guardar en LEV(P2, ∞)
Crear vector de tiempos de arribo en cola 1 VTA1=0
Crear vector de tiempos de arribo en cola 2 VTA2=0
TUE1=0 Tiempo de último evento es para ir acumulando las áreas de la cola 1
TUE2=0 Tiempo de último evento es para ir acumulando las áreas de la cola 2
Arribo 1
Si S =’O’ Servidor está ocupado
1
A = A + (Reloj-TUE1) * n
q1 q1 1
n = n + 1
1 1
Guardar en VTA1 el reloj
Sino
S =’O’
1
cli_at = cli_at + 1
1 1
Generar Tiempo de servicio 1 tiempo del servidor 1
Guardar en LEV (P1/A2, Reloj + tiempo de servicio 1)
Fin Si
Generar próximo arribo El evento Arribo llama a sí mismo (ver Diagrama de Desencadenamiento)
Guardar en LEV (A1, Reloj + tiempo de próximo arribo)
TUE1=Reloj
Partida 1/Arribo2
Este evento es doble, es decir en él ocurre la partida del servidor 1 y el cliente que sale de él va al
servidor 2, por lo que se sucede un Arribo al servidor 2. El módulo es único pero para mejor
clarificación del pseudocódigo hay una línea imaginaria que los separa.
--------------------------------------------(partida servidor 1)--------------------------------------------------------------
Si n =0
1
S =’D’
1
Guardar en LEV (P1/A2, )
Sino
S. De Federico 2

Simulación
|     |   A      | =  A + (Reloj-TUE1) * n |     |     |     |
| --- | -------- | ----------------------- | --- | --- | --- |
|     | q1       | q1                      |     | 1   |     |
|     | n = n    | -1                      |     |     |     |
|     | 1        | 1                       |     |     |     |
|     |   d =    | d  + (Reloj – VTA1)     |     |     |     |
|     | 1        | 1                       |     |     |     |
|     |   cli_at |  = cli_at  + 1          |     |     |     |
1 1
    Generar Tiempo de servicio 1     el cliente que entró al servidor va a ser atendido
|     |   Guardar en LEV (P1/A2, Reloj + tiempo de servicio1)  |     |     |     |     |
| --- | ------------------------------------------------------ | --- | --- | --- | --- |
Fin Si
Guardar TUE1
--------------------------------------------(Arribo servidor 2)--------------------------------------------------------------
Si S =’O’              Servidor está ocupado
2
|     | A =  A         | + (Reloj-TUE2) * n |     |     |     |
| --- | -------------- | ------------------ | --- | --- | --- |
|     | q2  q2         |                    | 2   |     |     |
|     | n 2 = n 2 + 1  |                    |     |     |     |
  Guardar en VTA2 el reloj
  Sino
|     |   S =’O’  |     |     |     |     |
| --- | --------- | --- | --- | --- | --- |
2
|     | cli_at                                                    | 2  = cli_at 2  + 1  |     |     |     |
| --- | --------------------------------------------------------- | ------------------- | --- | --- | --- |
|     |   Generar Tiempo de servicio 2    tiempo del servidor 2   |                     |     |     |     |
|     |   Guardar en LEV (P2, Reloj + tiempo de servicio 2)       |                     |     |     |     |
Fin Si
TUE2=Reloj

Nota: Observen que en este arribo NO hay una generación de arribo nuevo (por ello en el evento
P1/A2 NO hay una flecha entera apuntándose a sí mismo como en el Arribo 1)

Partida 2
Si n =0
2
|     | S =’D’  |     |     |     |     |
| --- | ------- | --- | --- | --- | --- |
2
|     | Guardar en LEV (P2,  | )   |     |     |     |
| --- | -------------------- | --- | --- | --- | --- |
  Sino
|     |   A      | =  A + (Reloj-TUE2) * n |     |     |     |
| --- | -------- | ----------------------- | --- | --- | --- |
|     | q2       | q2                      |     | 2   |     |
|     | n = n    | -1                      |     |     |     |
|     | 2        | 2                       |     |     |     |
|     |   d =    | d  + (Reloj – VTA2)     |     |     |     |
|     | 2        | 2                       |     |     |     |
|     |   cli_at |  = cli_at  + 1          |     |     |     |
2 2
    Generar Tiempo de servicio 1     el cliente que entró al servidor va a ser atendido
|     |   Guardar en LEV (P2, Reloj + tiempo de servicio2)  |     |     |     |     |
| --- | --------------------------------------------------- | --- | --- | --- | --- |
Fin Si
Guardar TUE2

Reporte
|           |              |        |             |     |     |
| --------- | -------------- | ------- | ------------ | --- | --- |
| Mostrar q | (t),  q (t), d | (cli_at | ), d (cli_at | )   |     |
|           | 1 2            | 1       | 1 2          | 2   |     |

Parte b)
En la parte b) se solicitan otras medidas de rendimiento que son interesantes para observar el
comportamiento de un sistema, y no tienen porque estar incluidas en el modelo analítico.
El algoritmo parte del realizado para la parte a) al que se le van a agregar las instrucciones para
calcular las medidas solicitadas. Para poder hacer eso hay que entender cómo se hace el cálculo de
cada una de las medidas.

En esta sección  se piden además de las de la parte a :
Número máximo de clientes en cada cola  (Agregado al algoritmo en Rojo)
| S. De Federico  |     |     |     |     |                3  |
| --------------- | --- | --- | --- | --- | ----------------- |

Simulación
Es el número más grande que llegan a tener las colas en una corrida. Cada vez que ingresa un
cliente a la cola 1, o a la cola2, se debe ver si el tamaño de la cola es el mayor hasta el momento.
Máxima demora (Agregado al algoritmo en Verde)
Se interpreta como la mayor demora de cualquiera de las dos colas durante la corrida del sistema.
Cada vez que un cliente entra a cualquiera de los servidores y ha tenido que esperar en alguna de
las colas, su demora (o sea el tiempo que estuvo esperando en cola) aparte de ser acumulada en su

promedio d (cli_at ) se debe observar si es la máxima demora durante la corrida del sistema.
i i
Máximo tiempo total en sistema: (Agregado al algoritmo en Violeta)
De define como el tiempo total del sistema al tiempo transcurrido desde la entrada de un cliente al
sistema hasta su salida del mismo. Por eso cada vez que entra un cliente al sistema se guarda su
tiempo de arribo en una estructura de datos parecida a la del VTA, que llamaremos VTS. Cuando
el cliente i termine de ser atendido por el servidor 2 (sale del sistema) se debe calcular su tiempo
transcurrido en el sistema y ver si es el máximo durante la corrida del mismo.
Proporción de clientes que demoraron un tiempo mayor que un valor t determinado: (Agregado al
0
algoritmo en Anaranjado)
Esta medida de rendimiento requiere un contador de clientes cuya demora fue mayor que t : cada
0
vez que un cliente que ha tenido que esperar en cola entra a cualquiera de los 2 servidores se
calcula su demora en la cola y se la compara con el valor t (ingresado en una variable del sistema);
0
si el valor es mayor entonces el contador se incrementa en 1. Al final de la corrida del modelo la
proporción se calcula contra la cantidad total de clientes que utilizaron los servidores (cli_at
1
+cli_at )
2
cdm
pdt
0 cli_at cli_at
1 2
Algoritmo parte b)
Principal
Inicialización
Mientras reloj <=Fin simulación
Tiempos
Si evento seleccionado =’A1’ ir a Arribo 1
Sino Si el evento seleccionado= ‘P1/A2’ ir a Partida1/Arribo2
Sino ir a Partida 2
Fin Si
Fin Si
Fin mientras
Reporte
Tiempos
Buscar en la LEV el evento con menor tiempo de ocurrencia
Reloj = Tiempo en LEV
Inicialización
Reloj=0
A =0 acumulada del tamaño de cola 1
q1
A =0 acumulada del tamaño de cola 2
q2
S. De Federico 4

Simulación
d =0 acumulada de la demora en cola 1
1
d =0 acumulada de la demora en cola 2
2
cli_at =0 número de clientes atendidos en cola 1
1
cli_at =0 número de clientes atendidos en cola 2
2
n =0 número de clientes en cola 1
1
n =0 número de clientes en cola 2
2
Maxn = 0
1
Maxn = 0
2
Maxd = 0
cdm = 0
t = valor predeterminado
0
Generar tiempo de arribo El Arribo es el evento que inicia el sistema (ver Diagrama de
Desencadenamiento
Guardar en LEV(A, Tiempo de arribo)
Guardar en LEV(P1/A2, ∞)
Guardar en LEV(P2, ∞)
Crear vector de tiempos de arribo en cola 1 VTA1=0
Crear vector de tiempos de arribo en cola 2 VTA2=0
Crear vector de tiempos de arribo al sistema VTS=0
Maxts=0
TUE1=0 Tiempo de último evento es para ir acumulando las áreas de la cola 1
TUE2=0 Tiempo de último evento es para ir acumulando las áreas de la cola 2
Arribo 1
Ingresar Reloj en VTS
Si S =’O’ Servidor está ocupado
1
A = A + (Reloj-TUE1) * n
q1 q1 1
n = n + 1
1 1
Si n >Maxn
1 1
Maxn =n
1 1
Fin Si
Guardar en VTA1 el reloj
Sino
S =’O’
1
cli_at = cli_at + 1
1 1
Generar Tiempo de servicio 1 tiempo del servidor 1
Guardar en LEV (P1/A2, Reloj + tiempo de servicio 1)
Fin Si
Generar próximo arribo El evento Arribo llama a sí mismo (ver Diagrama de Desencadenamiento)
Guardar en LEV (A1, Reloj + tiempo de próximo arribo)
TUE1=Reloj
Partida 1/Arribo2
Este evento es doble, es decir en él ocurre la partida del servidor 1 y el cliente que sale de él va al
servidor 2, por lo que se sucede un Arribo al servidor 2. El módulo es único pero para mejor
clarificación del pseudocódigo hay una línea imaginaria que los separa.
--------------------------------------------(partida servidor 1)--------------------------------------------------------------
Si n =0
1
S =’D’
1
S. De Federico 5

Simulación
|     | Guardar en LEV (P1/A2,  |     | )   |     |
| --- | ----------------------- | --- | --- | --- |
  Sino
|     |   A =                   | A + (Reloj-TUE1) * n |     |     |
| --- | ----------------------- | -------------------- | --- | --- |
|     | q1                      | q1                   | 1   |     |
|     | n = n -1                |                      |     |     |
|     | 1 1                     |                      |     |     |
|     |   d 1 = d 1             |  + (Reloj – VTA1)    |     |     |
|     |   Si (Reloj-VTA1)>Maxd  |                      |     |     |
|     |     Maxd = Reloj-VTA1   |                      |     |     |
|     |   Fin Si                |                      |     |     |
|     |   Si (Reloj-VTA1) > t   |                      |     |     |
0
cdm = cdm + 1
|     |                    |       |     |     |
| --- | ------------------ | ----- | --- | --- |
|     |   Fin Si           |       |     |     |
|     |   cli_at  = cli_at |  + 1  |     |     |
1 1
    Generar Tiempo de servicio 1     el cliente que entró al servidor va a ser atendido
|     |   Guardar en LEV (P1/A2, Reloj + tiempo de servicio1)  |     |     |     |
| --- | ------------------------------------------------------ | --- | --- | --- |
Fin Si
Guardar TUE1
--------------------------------------------(Arribo servidor 2)--------------------------------------------------------------
Si S 2 =’O’              Servidor está ocupado
|     | A q2  =  A q2  + (Reloj-TUE2) * n |     | 2   |     |
| --- | --------------------------------- | --- | --- | --- |
|     | n = n + 1                         |     |     |     |
2 2

|     | Si n 2 >Maxn 2    |     |     |     |
| --- | ----------------- | --- | --- | --- |
|     |   Maxn =n         |     |     |     |
2 2
Fin Si

  Guardar en VTA2 el reloj
  Sino
|     |   S =’O’  |     |     |     |
| --- | --------- | --- | --- | --- |
2
|     | cli_at 2  = cli_at                                        | 2  + 1  |     |     |
| --- | --------------------------------------------------------- | ------- | --- | --- |
|     |   Generar Tiempo de servicio 2    tiempo del servidor 2   |         |     |     |
|     |   Guardar en LEV (P2, Reloj + tiempo de servicio 2)       |         |     |     |
Fin Si
TUE2=Reloj

Nota: Observen que en este arribo NO hay una generación de arribo nuevo (por ello en el evento
P1/A2 NO hay una flecha entera apuntándose a sí mismo como en el Arribo 1)

Partida 2
Si (Reloj-VTS) > Maxts  en VTS está guardado el tiempo de ingreso al sistema del
Cliente que se retira
Maxts=Reloj-VTS
Fin Si
Si n 2 =0
|     | S =’D’  |     |     |     |
| --- | ------- | --- | --- | --- |
2
|     | Guardar en LEV (P2,  | )   |     |     |
| --- | -------------------- | --- | --- | --- |
  Sino
|     |   A =       | A + (Reloj-TUE2) * n |     |     |
| --- | ----------- | -------------------- | --- | --- |
|     | q2          | q2                   | 2   |     |
|     | n = n -1    |                      |     |     |
|     | 2 2         |                      |     |     |
|     |   d = d     |  + (Reloj – VTA2)    |     |     |
|     | 2 2         |                      |     |     |
Si (Reloj-VTA2) > Maxd
|                 |           Maxd = Reloj - VTA2  |     |     |                   |
| --------------- | ------------------------------ | --- | --- | ----------------- |
|                 |   Fin Si                       |     |     |                   |
| S. De Federico  |                                |     |     |                6  |

Simulación
Si (Reloj-VTA2) > t
0
Cdm = cdm + 1
|     |           |                 |     |     |
| --- | --------- | --------------- | --- | --- |
|     |   Fin Si  |                 |     |     |
|     |   cli_at  |  = cli_at  + 1  |     |     |
2 2
    Generar Tiempo de servicio 1     el cliente que entró al servidor va a ser atendido
|     |   Guardar en LEV (P2, Reloj + tiempo de servicio2)  |     |     |     |
| --- | --------------------------------------------------- | --- | --- | --- |
Fin Si
Guardar TUE2

Reporte
|           |               |                      |                |     |
| --------- | --------------- | --------------------- | --------------- | --- |
| Mostrar q | (t),  q (t), d  | (cli_at               | ), d (cli_at )  |     |
|           | 1 2             | 1                     | 1 2 2           |     |
|           |    Maxn ,  Maxn | ,  Maxd,  Maxts,  pdt |                 |     |
|           | 1               | 2                     | 0               |     |

Nota final: Así como se construyeron estas nuevas medidas de rendimiento se pueden hacer
infinidad de otras más. La intención es que el estudiante pueda crear las medidas de rendimiento
más convenientes para poder analizar óptimamente un problema dado.

Propuesta para analizar
Finalmente, este problema presenta un conjunto de medidas de rendimiento que cubren los eventos
del sistema. Analizar qué problema del sistema podría observarse a través del valor y/o un cambio
en el valor de cada medida de rendimiento.

| S. De Federico  |     |     |     |                7  |
| --------------- | --- | --- | --- | ----------------- |