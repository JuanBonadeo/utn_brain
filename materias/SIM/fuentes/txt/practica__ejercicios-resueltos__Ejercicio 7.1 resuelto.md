Simulación
Ejercicios grupo 7
En estos ejercicios se pide:
objetivo de optimización del sistema
medidas de rendimiento apropiadas
modelo de simulación que permita obtener la información de interés
Ejercicio 7. 1
Para obtener las respuestas solicitadas, se debe hacer un análisis del sistema. Para ello es muy útil
dibujar un esquema del mismo, y según los valores de las variables exógenas, prever los problemas
que puedan surgir.
Sección 1 Sección 2
Se puede observar que:
1) La sección 2, si bien tiene dos servidores, tiene una afluencia aumentada de unidades. Como no
se especifica los valores de los tiempos de servicio, el punto anterior puede significar:
a) Los servidores de la sección 2 están ociosos ya que su tiempo de servicio es muy bajo.
Objetivo de optimización: redistribuir los recursos
Medidas de rendimiento apropiadas: tiempo ocioso de servidores 2k, tamaño de la cola 2
t T
A
  b
Tiempo ocioso servidores k: 1 - b (t) b (t) t 0
k k T
En el algoritmo escrito en negro
b) La cola de la sección 2 está colapsada.
Objetivo de optimización: reorganizar el sistema para disminuir la cola
Medidas de rendimiento apropiadas: tiempo promedio en cola 2, tamaño de la cola 2,
tamaño máximo de la cola 2
En el algoritmo escrito en rojo
2) La tasa de arribo de la sección 1 es mucho menor que de la sección 2, por lo que puede estar
ociosa también.
Objetivo de optimización: redistribuir los recursos
Medidas de rendimiento apropiadas: tiempo ocioso del servidor 1, tamaño de la cola 1
En el algoritmo en verde
S. De Federico 1

Simulación
Diagrama de desencadenamiento de eventos

|     |        |             |   Si n1>0   |              |          |     |
| --- | ------ | ----------- | ----------- | ------------ | -------- | --- |
|     |        | Si S1 =’D’  |             |              | Si n2>0  |     |
|     |        |             |             | Si S2 k=’D’  |          |     |
|     |  A1    |             |             |              |          |     |
Sec1

Sec2 k
3)
4)
5)
|     |     | A2  |              |     |     |     |
| --- | --- | --- | ------------ | --- | --- | --- |
|     |     |     | Si S2 k=’D’  |     |     |     |

Eventos
A1: Arribo sección 1
A2: Arribo sección 2
Sec1: Sección 1
Sec2 k: Sección 2 k              k:1..2

Algoritmo sistema real

Principal
Inicialización
Mientras reloj <=800 horas
|     | Tiempos                                     |                                                    |     |     |     |     |
| --- | ------------------------------------------- | -------------------------------------------------- | --- | --- | --- | --- |
|     | Si evento seleccionado =’A1’ ir a Arribo 1  |                                                    |     |     |     |     |
|     |                                             | Sino  Si evento seleccionado = ‘A2’ ir a Arribo 2  |     |     |     |     |
          Sino Si evento seleccionado =’Sec1’ ir a Sección 1
|     |         |         |   Sino ir a Sec2 k  |     |     |     |
| --- | ------- | ------- | ------------------- | --- | --- | --- |
|     |         |         | Fin Si              |     |     |     |
|     |         | Fin Si  |                     |     |     |     |
|     | Fin Si  |         |                     |     |     |     |
Fin mientras
Reporte final

Tiempos
Buscar en la LEV el evento con menor tiempo de ocurrencia
Reloj = Tiempo en LEV

Inicialización
Reloj=0
| A2=0    |   acumulada del tamaño de cola 2        |     |     |     |     |     |
| ------- | --------------------------------------- | --- | --- | --- | --- | --- |
| b2.k=0  |   acumulada del servicio 2.k    k:1..2  |     |     |     |     |     |
n =0                               número de clientes en cola 1
1
n 2 =0                               número de clientes en cola 2
| IOS2.k=0  |   inicio ocupación servidor 2.k  |     |     |     |     |     |
| --------- | -------------------------------- | --- | --- | --- | --- | --- |
TUE2=0           Tiempo de último evento es para ir acumulando las áreas de la cola 2
d2=0
cli_at2=0
VTA2=0
n2Max=0
| S. De Federico  |     |     |     |     |     |                2  |
| --------------- | --- | --- | --- | --- | --- | ----------------- |

Simulación
A1=0
b21=0
IOS1=0
TUE1=0
Generar tiempo de arribo 1 El Arribo es el evento que inicia el sistema
Guardar en LEV(A1, Tiempo de arribo)
Generar tiempo de arribo 2 El Arribo es el evento que inicia el sistema
Guardar en LEV(A2, Tiempo de arribo)
Guardar en LEV(Sec1, ∞)
Guardar en LEV(Sec2k, ∞) k:1..2
Arribo 1
Si S =’O’ Servidor está ocupado
1
A1= A1+ (Reloj-TUE1) * n
1
n = n + 1
1 1
Sino
S =’O’
1
IOS1=Reloj
Generar Tiempo de servicio 1 tiempo del servidor 1
Guardar en LEV (Sec1, Reloj + tiempo de servicio 1)
Fin Si
Generar próximo arribo El evento Arribo llama a sí mismo (ver Diagrama de Desencadenamiento)
Guardar en LEV (A1, Reloj + tiempo de próximo arribo)
TUE1=Reloj
Arribo 2
Si S =’O’ Servidor está ocupado
2.k
A2= A2+ (Reloj-TUE2) * n
2
n = n + 1
2 2
Si n2 > n2Max entonces n2Max= n2
Guardar reloj en VTA2
Sino
S =’O’
2.k
IOS2.k=Reloj
cli_at2=cli_at2+1
Generar Tiempo de servicio 2 tiempo del servidor 2k
Guardar en LEV (Sec2.k ,Reloj + tiempo de servicio 2)
Fin Si
Generar próximo arribo El evento Arribo llama a sí mismo (ver Diagrama de Desencadenamiento)
Guardar en LEV (A2, Reloj + tiempo de próximo arribo)
Sec1
Este evento es doble, es decir en él ocurre la partida de la sección 1 y el cliente que sale de él va a la
sección 2, por lo que se sucede un Arribo a la misma.
--------------------------------------------(partida Sección 1)--------------------------------------------------------------
Si n =0
1
S =’D’
1
b1= b1 + (Reloj – IOS1)
Guardar en LEV (Sec1, )
Sino
A1= A1+ (Reloj-TUE1) * n
1
n = n -1
1 1
S. De Federico 3

Simulación
    Generar Tiempo de servicio 1     el cliente que entró al servidor va a ser atendido
|     | Guardar en LEV (Sec1, Reloj + tiempo de servicio1)  |     |     |
| --- | --------------------------------------------------- | --- | --- |
Fin Si
TUE1=Reloj
--------------------------------------------(Arribo Sección 2)--------------------------------------------------------------
Si S =’O’              Servidor está ocupado
2k
|   A2=   | A2+ (Reloj-TUE2) * n |     |     |
| ------- | -------------------- | --- | --- |
|         |                      | 2   |     |
|   n = n | + 1                  |     |     |
2 2
  Sino
|     | S =’O’  |     |     |
| --- | ------- | --- | --- |
2
|     | IOS2k=Reloj                                            |     |     |
| --- | ------------------------------------------------------ | --- | --- |
|     | Generar Tiempo de servicio 2    tiempo del servidor 2  |     |     |
    Guardar en LEV (Sec2k, Reloj + tiempo de servicio 2)
Fin Si
TUE2=Reloj

Sec 2 k
Si n =0
2
|   S 2k =’D’               |                          |     |     |
| ------------------------- | ------------------------ | --- | --- |
|   Guardar en LEV (Sec2k,  |                          | )   |     |
|   b2.k=                   | b2.k  +(Reloj – IOS2.k)  |     |     |
  Sino
|     | A2=  A2+ (Reloj-TUE2) * n |     |     |
| --- | ------------------------- | --- | --- |
|     |                           | 2   |     |
n 2 = n 2 -1
d2= d2+ (Reloj –VTA2)
cli_at2=cli_at2+1
    Generar Tiempo de servicio 2     el cliente que entró al servidor va a ser atendido
|     | Guardar en LEV (Sec2k, Reloj + tiempo de servicio2)  |     |     |
| --- | ---------------------------------------------------- | --- | --- |
Fin Si
Guardar TUE2

Reporte

| Mostrar    q | (t)                d(cli_at2)              q1(t)   |     |     |
| ------------ | -------------------------------------------------- | --- | --- |
2
|                   1-b | (t)        n2Max  |   1 – b1(t)  |     |
| --------------------- | ----------------- | ------------ | --- |
2.1

|                   1-b | (t)  |     |     |
| --------------------- | ---- | --- | --- |
2.2

Alternativa posible
Las alternativas posibles son varias, la que se detalla a continuación sirve para todos los objetivos
de optimización descriptos:
redistribuir los recursos. Se rearma el sistema para evitar colas, el servidor de la sección 1 se
capacita para atender tanto unidades del tipo 1 como las del tipo 2.

Sección única

| S. De Federico  |     |     |                4  |
| --------------- | --- | --- | ----------------- |

Simulación

DDE

Si n>0

Si S k=’D’

|     | A1  |     |     |     |
| --- | --- | --- | --- | --- |
Sec k

|     |     | Si S k=’D’  |     |     |
| --- | --- | ----------- | --- | --- |
A2

Algoritmo alternativa
Se toman utilizan todas las medidas de rendimiento descriptas anteriormente, solo que ahora la
cola no se va a llamar 2, sino que es cola única.

Principal
Inicialización
Mientras reloj <=800 horas
|   Tiempos                                     |                                                      |                       |     |     |
| --------------------------------------------- | ---------------------------------------------------- | --------------------- | --- | --- |
|   Si evento seleccionado =’A1’ ir a Arribo 1  |                                                      |                       |     |     |
|                                               |   Sino  Si evento seleccionado = ‘A2’ ir a Arribo 2  |                       |     |     |
|                                               |                                                      | Sino  ir a Sección k  |     |     |
|                                               |   Fin Si                                             |                       |     |     |
|   Fin Si                                      |                                                      |                       |     |     |
Fin mientras
Reporte final

Tiempos
Buscar en la LEV el evento con menor tiempo de ocurrencia
Reloj = Tiempo en LEV

Inicialización
Reloj=0
| A=0                                                    | acumulada del tamaño de cola 2  |     |     |     |
| ------------------------------------------------------ | ------------------------------- | --- | --- | --- |
| bk=0               acumulada del servicio k    k:1..3  |                                 |     |     |     |
n=0                               número de clientes en cola
| IOSk=0    | inicio ocupación servidor k  |     |     |     |
| --------- | ---------------------------- | --- | --- | --- |
TUE=0                         Tiempo de último evento es para ir acumulando las áreas de la cola
d=0
cli_at=0
VTA=0
nMax= 0
Generar tiempo de arribo 1   El Arribo es el evento que inicia el sistema (ver Diagrama de
          Desencadenamiento
Guardar en LEV(A1, Tiempo de arribo)
Generar tiempo de arribo 2   El Arribo es el evento que inicia el sistema (ver Diagrama de
          Desencadenamiento
Guardar en LEV(A2, Tiempo de arribo)
Para i=1 a k
Guardar en LEV(Seck, ∞)
Fin para
| S. De Federico  |     |     |     |                5  |
| --------------- | --- | --- | --- | ----------------- |

Simulación
Arribo 1
Si S =’O’ Servidores k están ocupados
k
A= A+ (Reloj-TUE) * n
n= n+ 1
Sino
S =’O’
k
IOSk=Reloj
Generar Tiempo de servicio tiempo del servidor
Guardar en LEV (Sec k, Reloj + tiempo de servicio )
Fin Si
Generar próximo arribo El evento Arribo llama a sí mismo (ver Diagrama de Desencadenamiento)
Guardar en LEV (A1, Reloj + tiempo de próximo arribo)
TUE=Reloj
Arribo 2
Si S =’O’ Servidor está ocupado
k
A= A+ (Reloj-TUE) * n
n= n+ 1
Guardar reloj en VTA
Si n > nMax entonces nMax= n
Sino
S =’O’
2.k
IOS2.k=Reloj
cli_at=cli_at+1
Generar Tiempo de servicio tiempo del servidor
Guardar en LEV (Seck ,Reloj + tiempo de servicio )
Fin Si
Generar próximo arribo El evento Arribo llama a sí mismo (ver Diagrama de Desencadenamiento)
Guardar en LEV (A2, Reloj + tiempo de próximo arribo)
Seck
Si n=0
S =’D’
k
bk= bk + (Reloj – IOSk)
Guardar en LEV (Seck, )
Sino
A= A+ (Reloj-TUE) * n
n= n-1
d= d+ (Reloj –VTA)
cli_at=cli_at+1
Generar Tiempo de servicio el cliente que entró al servidor va a ser atendido
Guardar en LEV (Seck, Reloj + tiempo de servicio)
Fin Si
TUE=Reloj
Reporte
Mostrar d(cli_at) nMax q(t) 1 – b1(t) 1 – b2(t) 1 – b3(t
S. De Federico 6

Simulación
Otras alternativas
Otras alternativas pueden ser:
 Agregar un servidor en la sección 1
 Agregar un servidor en la sección 2
 Cuando la cola 2 llegue a un valor máximo, el servidor 1 ayuda a la sección 2
S. De Federico 7