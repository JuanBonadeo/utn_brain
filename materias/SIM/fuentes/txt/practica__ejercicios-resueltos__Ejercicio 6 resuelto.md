Simulación
Ejercicio 6
Este sistema tiene bastantes diferencias con respecto a los anteriores:
 La población de clientes se reduce a solo 5 máquinas. Este tipo de población se llama Finita; una
población finita delimita también el tamaño de la cola.
 Cuando la población es finita, cada cliente se considera individualmente, y su arribo es
exclusivo, un cliente no puede arribar nuevamente al sistema hasta que haya salido de él. En
este caso, una máquina se podría descomponer o romper siempre y cuando este operativa y
funcionando, es decir, una máquina que está en cola esperando a ser reparada no puede
romperse nuevamente.
 En este caso el servicio es la reparación de las maquinas, por lo que en realidad no salen
físicamente del sistema, sino que quedan inutilizadas para trabajar.
 Los operarios (que son los servidores) atienden a las maquinas rotas por su tiempo de
reparación, es decir que la cola no es FIFO, sino que tiene una prioridad; En este caso, la cola se
convierte en un vector que guarda los tiempos de reparación ordenados de menor a mayor.
 Según el enunciado, la cantidad de servidores va variando, por lo que en realidad el problema
se redefine para servidores 1..k.
 La medida de rendimiento es un Costo que se determina según las horas de pérdida de
maquinas sin utilizar.
 Una máquina está detenida desde que se descompone hasta que esta operativa lista para
funcionar.
Nota: En los ejercicios se suele pedir un esquema del sistema real, que sería un esquema dibujado.
Diagrama de desencadenamiento de eventos
Si Sk =’D’ Si n>0
Di i: 1..5
R k k:1..5
Eventos
Di: Descompostura máquina i
Rk : Reparación realizada por el operario k
Cuando se termina de reparar la máquina i, recién en ese momento se puede determinar cuando se
descompondrá nuevamente (flecha que va desde el evento Rk hasta el evento Di)
Variables exógenas
Tiempo de descompostura: Tiempo entre dos descomposturas de una máquina.
Tiempo de servicio operarios: Tiempo que tarda un operario k en reparar una máquina.
Parte a)
Variable endógena
Costo promedio por hora de máquinas detenidas k: 50 x Ahd + 10 x k
800
Ahd: acumulada de horas detenidas
k: cantidad de operarios
Algoritmo parte a)
En este caso como se deben comparar los costos para distintas cantidades de operarios, se deberá
hacer una corrida por cada k.
S. De Federico 1

Simulación

Principal
Para k= 1 hasta 5
Inicialización
|     | Mientras reloj <=800 horas                           |                          |     |     |     |
| --- | ---------------------------------------------------- | ------------------------ | --- | --- | --- |
|     |   Tiempos                                            |                          |     |     |     |
|     |   Si evento seleccionado =’Di’ ir a Descompostura i  |                          |     |     |     |
|     |                                                      | Sino  ir a Reparación k  |     |     |     |
|     | Fin Si                                               |                          |     |     |     |
|     | Fin mientras                                         |                          |     |     |     |
Reporte parcial
Fin Para
Reporte final

Tiempos
Buscar en la LEV el evento con menor tiempo de ocurrencia
Reloj = Tiempo en LEV

Inicialización
Reloj=0
| hd=0   |   acumulada de horas de máquinas detenidas   |     |     |     |     |
| ------ | -------------------------------------------- | --- | --- | --- | --- |
| N=0    |   número de clientes en cola, es un vector   |     |     |     |     |
Para i=1 hasta 5
Generar tiempo descompostura maquina i
| Imdi=0   |   Inicio de maquina i detenida  |     |     |     |     |
| -------- | ------------------------------- | --- | --- | --- | --- |
Guardar en LEV(Di, tiempo descompostura)
Ok  = ‘D’
Guardar en LEV(Rk, ∞)      Cuidado: en este caso se puede hacer esto en este para porque
casualmente son la misma cantidad de operarios que de maquinas, sino debe hacerse por separado
Fin Para

Descompostura i
| Imdi=Reloj  |     |   Se guarda el momento en que se descompone  |     |     |     |
| ----------- | --- | -------------------------------------------- | --- | --- | --- |
Generar tiempo de reparación   Se calcula en cualquier caso, entre al operario o a la cola
Si Ok=’O’              Servidor está ocupado
N= N+ 1
Guardar en N el tiempo de reparación
Ordenar cola por menor tiempo de reparación
  Sino
|     | Ok=’O’                                                  |     |     |     |     |
| --- | ------------------------------------------------------- | --- | --- | --- | --- |
|     | Guardar en LEV (Rk, Reloj + tiempo de reparación)       |     |     |     |     |
Fin Si

Reparación k
-------------------------------------------Sobre la maquina que acaba de reparar--------------------------------------
Ahd=Ahd + (Reloj –Imdi)    Se acumula las horas que estuvo detenida
Generar próxima descompostura
Guardar en LEV (Di, Reloj + tiempo de descompostura)   Se genera la próxima descompostura

| S. De Federico  |     |     |     |     |                2  |
| --------------- | --- | --- | --- | --- | ----------------- |

Simulación
-------------------------------------------Lo que hace el operario k--------------------------------------------------------
Si N=0
  Ok=’D’
|   Guardar en LEV (Rk,  |     | )   |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- |
  Sino
|     | Guardar en LEV (Rk, Reloj + tiempo de reparación)  |     |     |     |     |
| --- | -------------------------------------------------- | --- | --- | --- | --- |
|     | N=N-1                                              |     |     |     |     |
Fin Si

Reporte parcial
Mostrar Costo promedio k = Ahd x 50 + 10 x k
|     |     |   800  |     |     |     |
| --- | --- | ------ | --- | --- | --- |
Reporte Final
Mostrar todos los Costos promedio

Parte b)

Variable endógenas

Costo promedio por hora de máquinas detenidas k:    50  x  Ahd  +  10 x k
|     |     |     |     |     800   |     |
| --- | --- | --- | --- | --------- | --- |
Ahd: acumulada de horas detenidas
k: cantidad de operarios

t T
mop
t
t 0
Número promedio en el tiempo de máquinas en servicio
T

∆mopt: Acumulada de maquinas operativas (en servicio) en el tiempo t

Esta medida es similar a q(t), se guarda la cantidad de maquinas operativas en cada porción del
tiempo. Por lo tanto se utilizan las mismas variables de estado para acumular los valores deseados.

Algoritmo parte b)   (en rosa todo lo que se ha modificado para la parte b)
Principal
Para k= 1 hasta 5
Inicialización
|     | Mientras reloj <=800 horas                           |                          |     |     |     |
| --- | ---------------------------------------------------- | ------------------------ | --- | --- | --- |
|     |   Tiempos                                            |                          |     |     |     |
|     |   Si evento seleccionado =’Di’ ir a Descompostura i  |                          |     |     |     |
|     |                                                      | Sino  ir a Reparación k  |     |     |     |
|     | Fin Si                                               |                          |     |     |     |
|     | Fin mientras                                         |                          |     |     |     |
Reporte parcial
Fin Para
Reporte final

Tiempos
Buscar en la LEV el evento con menor tiempo de ocurrencia
Reloj = Tiempo en LEV

| S. De Federico  |     |     |     |     |                3  |
| --------------- | --- | --- | --- | --- | ----------------- |

Simulación
Inicialización
Reloj=0
| hd=0   |   acumulada de horas de máquinas detenidas   |     |     |     |
| ------ | -------------------------------------------- | --- | --- | --- |
| N=0    |   número de clientes en cola, es un vector   |     |     |     |
Para i=1 hasta 5
Generar tiempo descompostura maquina i
| Imdi=0   |   Inicio de maquina i detenida  |     |     |     |
| -------- | ------------------------------- | --- | --- | --- |
Guardar en LEV(Di, tiempo descompostura)
Ok  = ‘D’
Guardar en LEV(Rk, ∞)      Cuidado: en este caso se puede hacer esto en este para porque
casualmente son la misma cantidad de operarios que de maquinas, sino debe hacerse por separado
Fin Para
| mop=0        |   Acumulada de máquinas operativas  |     |     |     |
| ------------ | ----------------------------------- | --- | --- | --- |
TUM=0       Tiempo de última medición de máquinas operativas
mo=5  Cantidad  de  máquinas  operativas.  Todas  están  en  servicio  al  inicio  del
algoritmo

Descompostura i
Imdi=Reloj          Se guarda el momento en que se descompone
mop =  mop + (Reloj – TUM) x mo  Se guarda el área de máquinas operativas
| mo= mo – 1  |     |     | Una  máquinas operativas se descompuso   |     |
| ----------- | --- | --- | ---------------------------------------- | --- |
TUM+ Reloj          Se guarda la última medición de máquinas operativas
Generar tiempo de reparación   Se calcula en cualquier caso, entre al operario o a la cola
Si Ok=’O’              Servidor está ocupado
N= N+ 1
Guardar en N el tiempo de reparación
Ordenar cola por menor tiempo de reparación
  Sino
|     | Ok=’O’                                                  |     |     |     |
| --- | ------------------------------------------------------- | --- | --- | --- |
|     | Guardar en LEV (Rk, Reloj + tiempo de reparación)       |     |     |     |
Fin Si

Reparación k
-------------------------------------------Sobre la maquina que acaba de reparar--------------------------------------
Ahd=Ahd + (Reloj –Imdi)    Se acumula las horas que estuvo detenida
Generar próxima descompostura
Guardar en LEV (Di, Reloj + tiempo de descompostura)   Se genera la próxima descompostura

mop =  mop + (Reloj – TUM) x mo  Se guarda el área de máquinas operativas
mo= mo + 1          Una  máquina se reparó y pasa a operativa
TUM+ Reloj          Se guarda la última medición de máquinas operativas
-------------------------------------------Lo que hace el operario k--------------------------------------------------------
Si N=0
  Ok=’D’
|   Guardar en LEV (Rk,  |     | )   |     |     |
| ---------------------- | --- | --- | --- | --- |
  Sino
|     | Guardar en LEV (Rk, Reloj + tiempo de reparación)  |     |     |     |
| --- | -------------------------------------------------- | --- | --- | --- |
|     | N=N-1                                              |     |     |     |
Fin Si

| S. De Federico  |     |     |     |                4  |
| --------------- | --- | --- | --- | ----------------- |

Simulación

Reporte parcial
Mostrar Costo promedio k = Ahd x 50 + 10 x k
|     |     |   800  |     |     |
| --- | --- | ------ | --- | --- |
Mostrar Número promedio de maquinas operativas =  mop
|     |     |     |              Reloj  |     |
| --- | --- | --- | ------------------- | --- |
Reporte Final
Mostrar todos los Costos promedio
Mostrar todos los Números promedio

| S. De Federico  |     |     |     |                5  |
| --------------- | --- | --- | --- | ----------------- |