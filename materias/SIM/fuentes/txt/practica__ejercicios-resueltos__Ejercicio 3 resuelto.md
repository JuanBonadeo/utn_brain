Simulación
Ejercicio 3
Diagrama de desencadenamiento de eventos
Este sistema tiene la misma estructura de eventos que la cola simple, con la diferencia que son k
servidores en vez de uno, habiendo k eventos de partida, todos con la misma característica. Para
representarlo en el DDE se utiliza un nodo de doble línea

|     |     |        |          |         | S: servidor           |     |
| --- | --- | ------ | -------- | ------- | --------------------- | --- |
|     |     |        |  Si=’D’  | Si n>0  |                       |     |
|     |     |        |          |         | ‘D’: Desocupado       |     |
|     |     |   A    |          |         | n: tamaño de la cola  |     |
Pi
|     |     |     |     |     | i: 1..k servidores  |     |
| --- | --- | --- | --- | --- | ------------------- | --- |

Eventos
A: Arribo
Pi: i Partidas, con i variando de 1 a k.

Variables exógenas
  Tiempo de arribo: Tiempo en que llegan los clientes al sistema.
  Tiempo  de  servicio:  Tiempo  que  tarda  el  servidor  en  atender  a  un  cliente,  todos  los
servidores poseen la misma distribución.

Variables endógenas parte a)
En este caso se utiliza una notación mas sencilla para determinar los acumuladores ya que se deben
usar  subíndices.  La  variable  tiempo promedio de  espera  en  cola  es  equivalente  a  la  demora
promedio en el tiempo.

|     |     |     | t T |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
q

|                                                  |     |     | t 0 |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
| Tamaño promedio en el tiempo de la cola:    q(t) |     |     |     |     |     |     |
T
t T
b
|                                     |     |      | i   |     |     |     |
| ----------------------------------- | --- | ----- | --- | --- | --- | --- |
| Utilización de los servidores:    b |     | (t) t | 0   |     |     |     |
|                                     |     | i     | T   |     |     |     |

t T
d

| Tiempo promedio de espera en cola:    d(cli_at) |     |     | t 0 |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- |

cli_at

Algoritmo parte a)
Principal
Inicialización
  Mientras reloj <=Fin simulación
|     | Tiempos                                  |     |     |     |     |     |
| --- | ---------------------------------------- | --- | --- | --- | --- | --- |
|     | Si evento seleccionado =’A’ ir a Arribo  |     |     |     |     |     |
      Sino ir a Partidai   En este caso no se desglosa la condición de cada partida
sino se indica genéricamente con un subíndice i el hecho de que son varias partidas.
|     | Fin Si    |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- |
  Fin mientras
Reporte

Tiempos
Buscar en la LEV el evento con menor tiempo de ocurrencia
| S. De Federico  |     |     |     |     |     |                1  |
| --------------- | --- | --- | --- | --- | --- | ----------------- |

Simulación
Guardar en el Reloj este tiempo Reloj = Tiempo en LEV
Inicialización
Reloj=0
q=0
bi=0
d=0
cli_at=0 número de clientes atendidos
n=0 número de clientes en cola
Generar tiempo de arribo El Arribo es el evento que inicia el sistema (ver Diagrama de
Desencadenamiento
Guardar en LEV(A, Tiempo de arribo) el tiempo en que va a ocurrir el primer arribo se guarda en
la LEV
Guardar en LEV(P, ∞) la partida se pone en un nro muy grande (infinito) para que la rutina
tiempos seleccione sí o sí al Arribo inicialmente
Crear vector de tiempos de arribo en VTA=0
TUE=0 Tiempo de último evento es para ir acumulando las áreas
TIOSi=0 Tiempo de inicio en que el servidor empieza a estar ocupado
Arribo
Si Si=’O’ Servidor está ocupado
Acumular área de la cola q= q+ (Reloj-TUE) * n
Incrementar en 1 el nº de clientes en cola n= n + 1
Guardar en VTA el reloj
Sino
Si=’O’
TIOS= Reloj Tiempo en que el servidor empieza a estar ocupado
cli_at = cli_at + 1 Aumenta en 1 la cantidad de clientes atendidos, o sea que
entraron al servidor
Generar Tiempo de servicio todos los servidores tienen el mismo tiempo de servicio
Guardar en LEV (Pi, Reloj + tiempo de servicio)
Fin Si
Generar próximo arribo El evento Arribo llama a sí mismo (ver Diagrama de Desencadenamiento)
Guardar en LEV (A, Reloj + tiempo de próximo arribo)
Guardar TUE Tiempo de último evento para el cálculo de la próxima área TUE=Reloj
Partidai
Si n=0
Si=’D’
Guardar en LEV (Pi, )
Sino
Acumular área de la cola q= q+(Reloj-TUE) *n
Acumular área del servidor bi = bi + (Reloj-TIOSi)
Decrementar en 1 el nº de clientes en cola n= n-1 (el primero de la cola entra al
Servidor i
Acumular la demora d= d + (Reloj - VTA(tiempo de ingreso de
ese cliente))
cli_at = cli_at + 1
Generar Tiempo de servicio el cliente que entró al servidor va a ser atendido
Guardar en LEV (Pi, Reloj + tiempo de servicio)
Fin Si
Guardar TUE Tiempo de último evento para el cálculo de la próxima área
S. De Federico 2

Simulación
Reporte
Mostrar todas las medidas de rendimiento con las fórmulas tal como se describió más arriba.
Variables endógenas parte b)
Se reemplaza el tiempo promedio de espera en cola por una nueva variable, proporción de clientes
que no tuvieron que esperar en cola, es decir la proporción de clientes que al arribar entraron
directamente al servidor:
cnc
Proporción de clientes que no tuvieron que esperar en cola: pcnc
cli_at
Cnc: clientes atendidos que no hicieron cola
Cli_at: clientes atendidos
Algoritmo parte b)
El algoritmo se modifica (en color rojo) para incorporar las nuevas variables, y eliminar las
variables correspondientes a la demora (en este ejemplo aparecen tachadas)
Principal
Inicialización
Mientras reloj <=Fin simulación
Tiempos
Si evento seleccionado =’A’ ir a Arribo
Sino ir a Partidai En este caso no se desglosa la condición de cada partida
sino se indica genéricamente con un subíndice i el hecho de que son varias partidas.
Fin Si
Fin mientras
Reporte
Tiempos
Buscar en la LEV el evento con menor tiempo de ocurrencia
Guardar en el Reloj este tiempo Reloj = Tiempo en LEV
Inicialización
Reloj=0
q=0
bi=0
d=0
cli_at=0 número de clientes atendidos
n=0 número de clientes en cola
Generar tiempo de arribo El Arribo es el evento que inicia el sistema (ver Diagrama de
Desencadenamiento
Guardar en LEV(A, Tiempo de arribo) el tiempo en que va a ocurrir el primer arribo se guarda en
la LEV
Guardar en LEV(P, ∞) la partida se pone en un nro muy grande (infinito) para que la rutina
tiempos seleccione sí o sí al Arribo inicialmente
Crear vector de tiempos de arribo en VTA=0
TUE=0 Tiempo de último evento es para ir acumulando las áreas
TIOSi=0 Tiempo de inicio en que el servidor empieza a estar ocupado
Cnc=0 Clientes que no tuvieron que hacer cola
S. De Federico 3

Simulación
Arribo
Si Si=’O’ Servidor está ocupado
Acumular área de la cola q= q+ (Reloj-TUE) * n
Incrementar en 1 el nº de clientes en cola n= n + 1
Guardar en VTA el reloj
Sino
Si=’O’
TIOS= Reloj Tiempo en que el servidor empieza a estar ocupado
cli_at = cli_at + 1 Aumenta en 1 la cantidad de clientes atendidos, o sea que
entraron al servidor
Generar Tiempo de servicio todos los servidores tienen el mismo tiempo de servicio
Guardar en LEV (Pi, Reloj + tiempo de servicio)
Cnc=cnc +1 Este cliente acaba de arribar y entro directamente a la cola.
Fin Si
Generar próximo arribo El evento Arribo llama a sí mismo (ver Diagrama de Desencadenamiento)
Guardar en LEV (A, Reloj + tiempo de próximo arribo)
Guardar TUE Tiempo de último evento para el cálculo de la próxima área TUE=Reloj
Partidai
Si n=0
Si=’D’
Guardar en LEV (Pi, )
Sino
Acumular área de la cola q= q+(Reloj-TUE) *n
Acumular área del servidor bi = bi + (Reloj-TIOSi)
Decrementar en 1 el nº de clientes en cola n= n-1 (el primero de la cola entra al
Servidor i
Acumular la demora d= d + (Reloj - VTA(tiempo de ingreso de
ese cliente))
cli_at = cli_at + 1
Generar Tiempo de servicio el cliente que entró al servidor va a ser atendido
Guardar en LEV (Pi, Reloj + tiempo de servicio)
Fin Si
Guardar TUE Tiempo de último evento para el cálculo de la próxima área
Reporte
Mostrar todas las medidas de rendimiento con las fórmulas tal como se describió más arriba.
S. De Federico 4