Resumen de **Comunicación de datos - 2do parcial Teoría**

**(Explicación de conceptos - Parcial Medin)**

# Elección de medio de acceso

En una empresa, la responsabilidad de decidir cuál es el mejor medio de acceso a la red recae en el responsable de sistemas. Este deberá tener en cuenta distintas variables y contextos de la organización, como pueden ser:

* Ubicación de la organización
  + Tipo de zona (Montañosa, Rural, Urbana, …)
  + Ubicación definitiva o temporal(La empresa se mudará pasado un tiempo).
* Disponibilidad de Espacio Físico para infraestructura
* Requerimiento de Ancho de Banda
* Grado de madurez de la Organización (Empresas chicas, en crecimiento o maduras)
* Segurización. (¿Es necesario que la comunicación sea constante o pueden haber cortes?)
* Disponibilidad de Recursos Económicos ($$$$)

[ver ejemplos del apunte]

## Segurización (o plan de contingencia)

El plan de contingencia se define como una alternativa por si lo normal falla. Específicamente en comunicaciones, vendría a ser el hecho de tener una segunda forma de comunicar dos puntos si el medio de comunicación principal sufre alguna falla.

Por supuesto que el plan de contingencia debe tratarse de un medio de acceso no tan costoso como el principal, ya que será usado ocasionalmente.

### Consideraciones sobre la segurización

Cuando los requerimientos de transmisión sean críticos que requiera segurización por no poder aceptar cortes de servicio se deben tener ciertas consideraciones:

* **Acceso y segurización por Fibra Óptica**: Si tanto el medio de acceso como la segurización son de fibra óptica, tenes que separar los recorridos de manera que no compartan recorrido.
* **Acceso y Segurización por Radio Enlace o Fibra Óptica**: Sería conveniente que el acceso y la segurización sean realizados por distintos operadores. *Si ambos servicios estuvieran dados por el mismo proveedor, ante una caída del mismo, perdemos el servicio (sin servicio principal y sin segurización)*.

## Consideraciones al instalar un sistema de radio enlaces

El radio enlace requiere que se tenga visión directa de un extremo al otro, no pueden haber obstáculos. Por lo tanto es muy factible instalar estos sistemas en organizaciones que dispongan de edificios en altura.

Pero si no contamos con edificación de gran altura se deberá instalar una estructura sostén de antenas, en este caso lo más usual es un mástil arriostrado.

Por ende, en caso de tener que realizar un mástil arriostrado, hay que tener en cuenta **el espacio físico** con el que cuenta la organización.

[Ejemplo de pie de rienda]

# Asignación de capacidad de canales

Para esto vamos a adoptar el criterio debido a **L. KLEINROCK**, que supone el costo linealmente proporcional a la capacidad.

Antes de comenzar analizaremos qué sucede en el concentrador en un nodo típico, que se utiliza para combinar los mensajes entrantes y rutearlos, luego, **hacia el enlace apropiado** (previamente hubo efectuado los procesamientos y almacenamientos necesarios).

El modelo más simple supone todos los puestos de entrada explorados instantáneamente, con mensajes en un **buffer FIFO**. Luego de un cierto procesamiento los mensajes destinados al enlace i se rutean uno a la vez sobre la línea de salida del concentrador ( en el ejemplo resulta un único buffer debido a que en configuración estrella cada concentrador tiene un solo enlace de salida).

![](data:image/png;base64...)

Para la asignación de capacidades ignoremos detalles de las operaciones de concentración y almacenamiento. Una simplificación importante surge de suponer que el tiempo de procesamiento nodal es despreciable frente al retardo de espera de enlace (línea disponible).

La **frecuencia promedio de mensajes** $λ\_{i}$ del enlace i es la suma de las frecuencias de los mensajes de todas las líneas entrantes al nodo.

$λ\_{i}=cant de terminales conectada \* \frac{cantidad de mensajes de esas terminales}{segundo}=\sum\_{i=1}^{n}(\frac{msg}{seg})\_{i}$

$\left[λ\_{i}\right]=seg=s$

$$

Luego, podemos definir el parámetro $η$ como **tasa media de mensajes por bit**. La fórmula es:

$promedio de mensajes=\frac{1}{η\_{i}}\frac{bits}{mensajes}⇒η\_{i}=\frac{1}{promedio de mensajes}$

Entonces, la teoría de la cola puede aplicarse a este modelo. Se supone para ello, frecuencia de arribo de mensajes Poisson con mensajes de longitud exponencialmente distribuidos con una longitud promedio de mensajes de $\frac{1}{η\_{i}}$ $\frac{bits}{mensajes}$ y un buffer de capacidad infinita, resultando un **tiempo de retardo promedio** del mensaje de:

$T\_{i}=\frac{1}{μ\_{i}-λ\_{i}}$

donde: $μ\_{i}$ es la **frecuencia de mensajes por segundo a la salida**, no siendo más que la capacidad del canal ($C\_{i}$) *–en bps-* al multiplicarla por la longitud promedio en bits en promedio de los mensajes –*longitud promedio* $\frac{1}{η\_{i}}$*-*, luego:

$μ\_{i}=η\_{i}⋅C\_{i}$

Reemplazando en la expresión del tiempo de retardo promedio del mensaje obtenemos que:

$T\_{i}=\frac{1}{η\_{i}⋅C\_{i}-λ\_{i}}$

Cuando de la frecuencia de flujo de tráfico es cercana al valor $η\_{i}⋅C\_{i}$ el tiempo de retardo crece sin límites. Es común definir un parámetro de **intensidad de tráfico** que por tener un único servidor coincide con el **factor de utilización** ($u\_{i}=ρ\_{i}$).

La fórmula para medir la **utilización** del sistema es:

$ρ\_{i}=\frac{λ\_{i}}{η\_{i}C\_{i}}<1$

Teniendo en cuenta a este parámetro podemos escribir:

$T\_{i}=\frac{1}{η\_{i}⋅C\_{i}⋅(1-ρ\_{i})}$

Para $ρ\_{i}<1$ el retardo será $T\_{i}=\frac{1}{η\_{i}⋅C\_{i}}$ exactamente el **tiempo necesario para transmitir el mensaje completo**. Para $ρ\_{i}\rightarrow 1$, $T\_{i}$ resulta muy grande.

![](data:image/png;base64...)

Considerando la red como un conjunto de enlaces (uno por nodo), el buffer asociado con el enlace i-ésimo tiene una frecuencia de arribo de $λ\_{i}$ y y la longitud promedio de mensaje emitido será $\frac{1}{η\_{i}}$, se tiene:

![](data:image/png;base64...)

Se considera, que esta forma, la red como una “caja negra”, observando los arribos a la caja, se tienen $δ$ mensajes ingresando a la caja por unidad de tiempo, donde:

$δ=\sum\_{i=0}^{n}λ\_{i}$

La caja negra se comporta como una cola para la cual, por el teorema de Little,

tenemos:

$N=δ⋅E[T]=E[n]$

Para el promedio estadístico se tiene:

$E[n]=\sum\_{i=0}^{n}E[n\_{i}]=\sum\_{i=0}^{n}λ\_{i}⋅E[T\_{i}]$

Sumado sobre todos los buffer de la red y aplicando el teorema de Little a cada uno, obtenemos la ecuación para calcular el retardo promedio de mensajes para la red:

$E[T]=\frac{1}{δ}\sum\_{i=1}^{x}λ\_{i}⋅E[T\_{i}]$

$C\_{i}^{opt}=\frac{λ\_{i}}{η\_{i}}+\frac{C(1-ρ) ⋅ \sqrt{\frac{λ\_{i}}{η\_{i}}}}{\sum\_{j=1}^{n}\sqrt{\frac{λ\_{j}}{η\_{j}}}}$

## Versión comprimida

Se utiliza el criterio de L. Kleinrock que asume el costo linealmente proporcional a la capacidad ($c≃C$).

La **frecuencia promedio de mensajes** $λ\_{i}$ del enlace i es la suma de las frecuencias de los mensajes de todas las líneas entrantes al nodo. También se la define como **tasa de llegada**, indicando que llegan una tasa de $λ$ mensajes por segundo

$λ\_{i}=cant de terminales conectada \* \frac{cantidad de mensajes de esas terminales}{segundo}=\sum\_{i=1}^{n}(\frac{msg}{seg})\_{i}$

$\left[λ\_{i}\right]=seg=s$

Luego, podemos definir el parámetro $η$ como **tasa media de mensajes por bit**. No se suele usar tanto esta definición sino que se suele decir que hay un promedio de mensajes de $\frac{1}{η}$. La fórmula es:

$promedio de mensajes=\frac{1}{η\_{i}}\frac{bits}{mensajes}⇒η\_{i}=\frac{1}{promedio de mensajes}$

$μ\_{i}$ es la **frecuencia de mensajes por segundo a la salida**, que se calcula de la siguiente manera:

$μ\_{i}=η\_{i}⋅C\_{i}$

A partir de las fórmulas vistas puede calcularse, y aplicando un sistema de colas M/M/1 y buffer infinito, el **tiempo de retardo** se define comoel **tiempo necesario para transmitir el mensaje completo**. Su fórmula es:

$T\_{i}=\frac{1}{μ\_{i}-λ\_{i}}=\frac{1}{η\_{i}⋅C\_{i}-λ\_{i}}$

Cuando de la frecuencia de flujo de tráfico es cercana al valor $η\_{i}⋅C\_{i}$ el tiempo de retardo crece sin límites. Es común definir un parámetro de intensidad de tráfico que por tener un único servidor coincide con el **factor de utilización** ($u\_{i}=ρ\_{i}$).

La fórmula para medir la **utilización** del sistema es:

$ρ\_{i}=\frac{λ\_{i}}{η\_{i}C\_{i}}$

El **punto de saturación** se define generalmente entre $0,8∼1$, y nos indica cuándo un enlace está saturado o cerca de saturarse. Comparar el factor de utilización con el valor elegido de punto de saturación nos permite saber qué tan saturado está nuestro enlace.

$C\_{i}^{opt}=\frac{λ\_{i}}{η\_{i}}+\frac{C(1-ρ) ⋅ \sqrt{\frac{λ\_{i}}{η\_{i}}}}{\sum\_{j=1}^{n}\sqrt{\frac{λ\_{j}}{n\_{j}}}}$

# Teoría de cola

## Introducción

La teoría de redes de cola de espera (teoría de cola) es la fundamentación matemática para la mayor cantidad de modelos analíticos de sistemas de computación.

Las relaciones establecidas por la teoría de cola son relaciones entre cantidades abstractas que no pueden ser observadas directamente. Para hallar las soluciones a estas relaciones se las simplifica.

## Elementos de un sistema de colas abiertas

Una cola es una **línea de espera** y la teoría de cola es el estudio del fenómeno de la espera en la cola.

![](data:image/png;base64...)

En la figura se pueden observar los elementos que integran un sistema de cola:

* “**Usuarios**” significa una entidad que desea algún tipo de servicio de un conjunto de servicios que ofrece el sistema.
* “**Servicios**” pueden ser: establecer una determinada comunicación (sistema telefónico ), procesar una pregunta, atender algún pedido de entrada/salida.

Si al ingresar un usuario al sistema **todos los servidores están ocupados**, aquel tendrá que formar una cola a la espera de la disponibilidad de alguno de ellos que pueda atenderlo.

![](data:image/png;base64...)

La figura muestra un conjunto de variables aleatorias utilizada para el estudio de sistemas de cola. Se usa $t(Q)$ representar el tiempo que un usuario arbitrario necesita estar en la cola a la espera de un servidor disponible (tiempo de espera). Y $t(s)$ tiempo requerido para que el servidor provea el servicio (tiempo de atención o de servicio).

Finalmente se tiene $t(w)$ que es el **tiempo total en el sistema de cola**, obviamente t(w)

será:

$t(w)=t(q)+t(s)$

Siendo entonces:

* $t(w)$ es el **"waiting time"** o **tiempo total de espera** en el sistema, que incluye tanto el tiempo que pasa esperando en la cola como el tiempo que tarda en recibir el servicio.
* $t(q)$ es el **"queue time"** o **tiempo en cola**, es decir, el tiempo que el cliente pasa esperando a ser atendido.
* $t(s)$ es el **"service time"** o **tiempo de servicio**, es el tiempo que tarda el servidor en procesar la solicitud del cliente una vez que ha comenzado a atenderlo.

## Notaciones de magnitudes de la teoría de colas

* $C(c, u)$: es la fórmula C de Erlang o la probabilidad de que todos los usuarios estén ocupados en un sistema de cola de espera M/M/c.
* $E[s]$: es el tiempo promedio de servicio para un usuario.
* $E[τ]$: es el intervalo promedio de tiempo entre arribos $E[τ]=\frac{1}{λ}$, con $λ$ velocidad o frecuencia promedio de arribos.
* $L$: es el número promedio de usuarios en el sistema cuando el sistema está en estado estable.
* $Lq$: es el número promedio de usuarios en la cola (*sin incluir a los usuarios que están actualmente recibiendo atención*) en un estado estable del sistema.
* $λ$: frecuencia o velocidad de arribo al sistema de cola $λ=\frac{1}{E[τ]}$.
* $λ^{T}$: es la frecuencia de atención media en tareas o interacciones por unidad de tiempo.
* $μ$: es la frecuencia promedio de servicio por servidor $μ=\frac{1}{E[s]}$.
* $N$: es una variable aleatoria que describe el número de usuarios en el sistema de cola de espera cuando el sistema está estable.
* $Nq$: es una variable aleatoria que describe el número de usuarios en la cola durante el estado estable del sistema.
* $Ns$: es una variable aleatoria que describe el número de usuarios que están recibiendo servicios durante un estado estable del sistema.
* $t(q), t(s) y t(w)$: son variables aleatorias que describen el tiempo de un usuario en la cola, en servicio o en el sistema respectivamente.
* $ρ$: es el factor de utilización del servidor. Así $ρ=\frac{intensidad de tráfico}{c}=\frac{λ⋅E[s]}{c}=\frac{\frac{λ }{μ}}{c}$.
* $τ$: es una variable aleatoria que describe el intervalo entre arribos.
* $W$: es el tiempo promedio esperado en el sistema en estado estable. $W=Wq+E[s]$
* $Wq$: es el tiempo promedio esperado en la cola(*tiempo de espera*), excluyendo el tiempo de servicio, para el sistema en estado estable.

## Nociones de un sistema de cola

* **Fuentes**: esto es el conjunto de usuarios que pueden solicitar el servicio del sistema, puede ser una fuente finita o infinita.
  + Si se tuviera un sistema de **fuente finita** la longitud de la cola estaría determinada por el número de usuarios en el sistema, ya que estos afectan la frecuencia de arribo a ella.
  + En cambio en un sistema con **fuente infinita**, la cola es ilimitada, por lo tanto la frecuencia de arribos no está afectada por el número de usuarios presentes en el sistema. Si la fuente fuese limitada pero con gran número de usuarios potenciales se supone una población infinita con el objeto de simplificar.
* **Proceso de arribo**: se supone que los usuarios entran en el sistema en los tiempos: $t\_{0}<t\_{1}<t\_{2}< ... <t\_{n}$. Las variables $τ\_{k}=t\_{k}-t⋅(k-1)$, (donde $k\geq 1$) se llaman **intervalos entre arribos**. Se supone que la $τ\_{k}$ forma una secuencia de variables aleatorias distribuidas independiente e idénticamente, y se usa el símbolo $τ$ para un intervalo arbitrario entre arribos.
* **Distribución del tiempo de servicio**: sea $s(k)$ el tiempo requerido para la atención del k-ésimo usuario. Supongamos los s(k) como una variable aleatoria independiente e idénticamente distribuidos. Por lo tanto se puede considerar un tiempo de servicio arbitrario s. Se supone también una función de distribución común Ws(t) = P[ s t] del tiempo de servicio para todos los usuarios. La función de distribución del tiempo de servicio en la teoría de cola es exponencial, lo cual define el denominado servicio (o atención) aleatoria. El símbolo se reserva para la frecuencia promedio de servicio y la función de reserva para la frecuencia promedio de servicio y la función de distribución para el servicio aleatorio será:

$W\_{s}(t)=1-e^{-μ⋅t}$

* + Coeficiente de variación al cuadrado: Un parámetro estadístico que es útil como una medida de la característica de la distribución de probabilidades para el intervalo de arribo y para el tiempo de servicio es el coeficiente de variación al cuadrado el que se defina para una variable aleatoria x como:

$C^{2}(x)=\frac{VAR[x]}{E^{2}[x]}$

* **Capacidad máxima del sistema de cola**: En algunos sistemas la capacidad de la cola se supone infinita. Esto significa que cualquier arribo de un usuario se permite.
  + Otros sistemas, llamados *sistemas de pérdida* tienen una capacidad de línea de ampers igual cero, en estos sistemas si un usuario arriba cuando las facilidades de servicio están cubiertas, no podrá esperar. SIn embargo, estos tienen una capacidad de cola positiva pero no infinita
* **Número de servidores**: el sistema de cola más simple es el de servidor único, el cual puede atender un usuario solamente por vez.
  + Un sistema multiservidor tiene **n** servidores idénticos y puede servir hasta **n** usuarios simultáneamente.
* **Disciplina de cola**: La disciplina de cola, a veces llamada disciplina de servidor es la regla para seleccionar el próximo usuario a recibir servicio. La disciplina más común de cola es la **FIFO** (*primero en llegar, primero en atender*). También existen disciplinas como **LIFO** (*último en llegar, primero en atender*) o disciplinas donde se consideran algunas prioridades de los usuarios.
* **Intensidad de tráfico**: La intensidad de tráfico $u$ es la relación entre el tiempo de un servicio promedio $E[s]$ y el intervalo promedio entre arribos $E[τ]$, esta relación es un parámetro importante de un sistema de cola y se define como:

$u=\frac{E[s]}{E[τ]}=λ⋅E[s]$

La **intensidad de tráfico u** determina el número mínimo de servidores que se requieren para cumplir con el flujo entrante de usuarios. De este modo, por ejemplo, si $E[s]$ es 15 segundos y $E[τ]$ es 10 segundos, luego, u = 1.5, esto indica que al menos se requerirán dos servidores. La unidad de intensidad de tráfico es el Erlang

* **Factor de utilización del servicio**: Otro parámetro importante es la intensidad de tráfico por servidor ($\frac{u}{c}$), llamado **factor de utilización del servicio** - $ρ$ - (cuando el tráfico se divide igualmente entre los servidores). Es la probabilidad de que algún servidor esté ocupado. Para sistemas de un único servidor coincide con la intensidad de tráfico.
* **Probabilidad de n usuarios estén en el sistema en el tiempo t**: Esta probabilidad, pn(t), depende no solo del tiempo t, si no también de las condiciones iniciales del sistema de cola, esto es, de número de usuarios presentes cuando se inicia el servicio y de las distribuciones y parámetros mencionados. Para los sistemas más útiles de cola, como t crece, pn(t) se aproxima al valor del estado estable, el es independiente de t y de las condiciones iniciales. El sistema se dice entonces que está en un estado estable. Consideraremos solamente soluciones en estados estables. Las soluciones a problemas de cola que dependan del tiempo o soluciones transitorias son más complejas de hallar.

La teoría de cola provee mediciones estadísticas de la performance de los sistemas de cola. Algunas mediciones estadísticas incluyen $Wq$, $W$, $L$ y $Lq$.

Las siguientes fórmulas llamadas leyes de Littlo, son bastante útiles relacionándolas con cuatro medidas de performance primarias:

$Lq=λ⋅Wq$

$L=λ⋅W$

Otra medición de performance útil es el valor del **90 percentil del tiempo en el sistema**,

$W(90)$, el cual define la cantidad de tiempo necesaria tal que el 90% de todos los que

arribaron a la cola (o sea al sistema) no esperan más que ese tiempo. Expresado

simbólicamente, $W(90)$, se define por la ecuación:

$P[W\leq π\_{w(90)}]=0.9$

De la misma manera se define al **90 percentil del tiempo en cola**.

## Modelo de cola abierta

El sistema de cola **M/M/c** es un modelo de cola simple, abierta, que puede ser usado para modelar, algún sistema de cómputo. Se considera **abierto**, pues los usuarios entran al sistema desde el exterior, reciben el servicio y parten. Los sistemas cerrados, en los cuales el usuario nunca deja el sistema, se consideran luego. Las ecuaciones del sistema de cola M/M/c se muestran a continuación:

$u=\frac{λ}{μ}=λ⋅E[s] \rightarrow intensidad de Tráfico$

$ρ=\frac{u}{c} \rightarrow factor de utilización del servidor$

[hay una fórmula de erlang complicadisima]

$Wq=\frac{C(c,u)⋅E[s]}{c⋅(1-ρ)}\rightarrow tiempo medio en cola$

$W=Wq+E[s] \rightarrow tiempo medio en el sistema$

$π\_{q}(90)=\frac{E[s]}{c⋅(1-ρ)}⋅ln(10⋅C\_{1})\rightarrow tiempo del 90 percentil en cola$

Cuando $c=1$ las fórmulas se simplifican resultando:

$C(c,u)=ρ=λ⋅E[s]$

$Wq=\frac{ρ⋅E[s]}{1-ρ}$

$W=\frac{E[s]}{1-ρ}$

$π(90)=W⋅ln(10⋅ρ)$

$π\_{q}(90)=W\_{q}⋅ln(10⋅ρ)$

## Modelo de cola en sistemas interactivos con población finita

Se considerará ahora un modelo de cola más realista; modelo de cola cerrado (ningún usuario ni entra ni sale) y con una población finita de usuarios.

![](data:image/png;base64...)

Un sistema de procesamiento central consiste de una cola para la unidad central de proceso (CPU), algunos terminales de entrada/salida y un sistema asociado de cola para cada uno de estos dispositivos. Los usuarios interactúan con la CPU a través de los **n** terminales. Cada usuario se supone en uno de los siguientes estados en cada instante:

* “Pensando” en el terminal. Se refiere al tiempo que el usuario pasa **procesando o preparando su próxima acción** antes de interactuar nuevamente con el sistema.
* Esperando algún tipo de atención. Vendría a ser cuando el usuario está esperando que se le provea el servicio.
* Recibiendo el servicio.

El sistema de procesamiento central tendrá un modelo de tiempo compartido si el tiempo de servicio de la CPU es continuo y se usa la disciplina de cola por muestreo por medio de la CPU. Esta disciplina supone que la potencia de procesamiento de la CPU se distribuye igualmente entre todos los pedidos. Sin embargo, si hay **n** interacciones pendientes para el servicio de la CPU cada una de ellas se sirven instantáneamente por el sistema con una velocidad (frecuencia) de $\frac{u}{n}$usuarios por unidad de tiempo, donde u es la velocidad de procesamiento de la CPU.

Para pocas terminales N la interferencia entre usuarios es mínima, esto quiere decir que cuando uno de los usuarios busca una interacción con la CPU los demás generalmente están en el modo de pensamiento, por lo tanto, escasamente se formará una cola de espera. Es posible entonces considerar la curva estratégica a $W = E[s]$ cuando se tiene pocas terminales.

Cuando el número de terminales tiende a infinito, la probabilidad de tener la CPU desocupada ($p\_{0}$) tiende a cero, consecuentemente la curva será asintótica a la recta $N⋅E[s] – E[t]$ con N tendiendo al infinito.

La intersección de las dos asíntotas se produce en N\* tal como:

$N\*=\frac{E[s] + E[t]}{E[s]}$

Este valor de $N$ se llama **punto de saturación del sistema**.

Se concluye que si cada interacción requiere exactamente E[s] unidades de tiempo de servicio de CPU y exactamente E[t] “tiempo de pensamiento”, N\* es el número máximo de terminales que pueden ser incluidos de tal forma de no causar ninguna interferencia mutua.

# Ejercicios propuestos

1. Se tiene una red con topología estrella con capacidad general de 3000 bps, la capacidad del ISP es de 5000 bps. De cada terminal, se envía 1 mensaje cada 1230 segundos. Cada mensaje tiene una longitud promedio de 1500 bits.

En base a esta topología una empresa evalúa incorporar una sucursal en capitán Bermudez cuando el enlace entre Pto San Martin y Rosario; pero hay que evaluar si la capacidad del enlace es acorde a la transmisión

![](data:image/png;base64...)

Hay dos formas diferentes de resolver estos ejercicios:

*Nota: recordar que* $ρ$ *representa al punto de saturación*

* Suponer que no está saturada y calcular el $ρ\_{ISP}$ total.
* Suponer que esta saturada e ir calculando el $ρ$ de cada localidad.

Para considerar que el enlace está saturado vamos a tomar que $0,8<ρ<1$, si $ρ<0,8$ el enlace no está saturado.

Primero vamos a hacerlo suponiendo que no está saturado y calculamos el $ρ\_{total}=ρ\_{ISP}$, para ello:

$ρ\_{ISP}=\frac{λ\_{ISP}}{η\_{ISP}⋅C\_{ISP}}$

Conocemos la capacidad del enlace del ISP que es $C\_{ISP}=5000 bps$ y a partir del promedio de longitud del mensaje podemos despejar $η\_{ISP}=η\_{cualquier localidad}=\frac{1}{1500}$ . Sin embargo, no conocemos el $λ\_{ISP}$ ya que vendría a ser la frecuencia promedio de mensajes del enlace del ISP (sería el promedio de mensajes que entran a ese nodo). Para calcular eso debemos:

$λ\_{ISP}=\sum\_{i=1}^{3}λ\_{i}$

Pero para calcular el $λ\_{ISP}$ resulta más ordenado calcular cada $λ\_{localidad}$, por separado, esto es:

$λ\_{Pto san martin}=cant de terminales conectadas en Pto San Martin⋅frecuencia de mensajes$

$λ\_{Pto san martin}=50⋅\frac{1}{1230}=\frac{50}{1230}$

De la misma manera, en Roldan:

$λ\_{Roldan}=10⋅\frac{1}{1230}=\frac{10}{1230}$

Ahora, tanto en la localidad de Bermudez como en la localidad de Rosario hay un cambio. Esto se trata de que en la localidad de Bermudez se deben tener en cuenta las conexiones que se reciben desde *Puerto San Martín*, para ello sumamos a las terminales de *Bermudez* las terminales de *Puerto San Martin*:

$λ\_{Bermudez}=(40+50)⋅\frac{1}{1230}=\frac{90}{1230}$

De la misma manera, en Rosario se deben tener en cuenta, **además de las terminales de Rosario**, las terminales de *Roldan, Bermudez y Puerto San Martín*. Entonces:

$λ\_{Rosario}=(40+50+50+10)⋅\frac{1}{1230}=\frac{150}{1230}$

Ahora, podemos calcular $λ\_{ISP}$. Si recordamos lo que representa $λ$, la **frecuencia de entrada de mensajes al nodo**, podemos notar que esta frecuencia será la misma en Rosario como en el ISP, pues no se agregan más terminales, por ende:

$λ\_{ISP}=\sum\_{i=1}^{3}λ\_{i}=λ\_{Rosario}=\frac{150}{1230}$

Habiendo calculado esto podemos ahora calcular el punto de saturación en el ISP ($ρ\_{ISP}$):

$ρ\_{ISP}=\frac{λ\_{ISP}}{η\_{ISP}⋅C\_{ISP}}=\frac{ \frac{150}{1230}}{\frac{1}{1500} ⋅ 5000}=0,03$

Como este valor es menor a $0,8$, podemos decir que los enlaces no están saturados. Por ende, puede incorporarse Capitan Bermudez a través del enlace de Pto San Martin y Rosario.

De la misma manera puede plantearse el otro camino en el que se supone el enlace saturado y se calcula el punto de saturación de cada localidad($ρ\_{localidad}$)

1. Una empresa desea evaluar el rendimiento de la red sobre el nodo central ya que allá se encuentra el DataCenter(**nodo 1**) con los servidores; para esto la dirección quiere conocer la utilización de los enlaces y una recomendación respecto a tiempos y capacidades

![](data:image/png;base64...)

Como **datos** se tiene que la capacidad general es de 4500 bps, y la frecuencia de mensajes es de 0,03 mensajes/segundo. Además, la longitud promedio de los mensajes es de 6 bits.

Pasándolo a parámetros entonces:

* frecuencia de mensajes por terminal$\rightarrow fr=0,03 \frac{mensaje}{segundo}$
* Capacidad general $\rightarrow C\_{i}=4500 bps$
* Longitud promedio $\rightarrow \frac{1}{η}=6 bits$

Calculamos cada $λ\_{i}$ entonces:

$λ\_{5}=6⋅0,03=0,18$

$λ\_{4}=6⋅0,03=0,18$

$λ\_{8}=2⋅0,03=0,06$

$λ\_{6}=6⋅0,03=0,18$

$λ\_{7}=6⋅0,03+λ\_{8}=0,18+0,06=0,24$

$λ\_{3}=2⋅0,03+λ\_{5}+λ\_{4}=0,06+0,18+0,18=0,42$

$λ\_{2}=2⋅0,03+λ\_{3}=0,06+0,42=0,48$

$λ\_{1}=10⋅0,03+λ\_{6}+λ\_{7}+λ\_{2}=0,3+0,18+0,24+0,48=1,2$

Luego, calculamos el factor de utilización ($ρ\_{1}$):

$ρ\_{1}=\frac{λ\_{1}}{\frac{1}{η} ⋅ C\_{1}}=\frac{1,2}{\frac{1}{6 bits}⋅ 4500 bps}=0,0016\%$

Y, además calculamos el **tiempo de retardo**:

$T\_{1}=\frac{λ\_{1}}{\frac{1}{η} ⋅ C\_{1}-(1-ρ\_{1})}=\frac{1}{\frac{1}{6 bits}⋅ 4500 bps-(1-0,0016)}=0,0013 seg$

1. La sala de emergencias de un hospital es atendida por **un doctor** y proporciona atención médica a los casos de emergencia que llegan en ambulancias o vehículos particulares.

Los casos de emergencia llegan aleatoriamente según un proceso de Poisson; **un paciente cada media hora**. El tiempo que necesita el doctor para atender a los pacientes sigue una distribución exponencial.

El doctor en promedio requiere **20 minutos** para atender al paciente.

Calcular:

* 1. Tiempo promedio que el paciente espera para ser atendido.
  2. Tiempo promedio que el paciente espera en la sala de espera de emergencias.
  3. N° de pacientes promedio en cola.
  4. N° de pacientes promedio en sala de espera de emergencias.
     1. El $π\_{(90)}$ del tiempo de espera

Resolución:

*Datos del enunciado:*

* Tiempo promedio que dura la atención$\rightarrow E[s]=20 minutos=0.3 horas$
* Tiempo promedio entre arribos$\rightarrow E[τ]=30 minutos=0.5 horas$
* frecuencia de arribo al sistema de cola$\rightarrow λ=\frac{1}{E[τ]}=\frac{1}{30 min}=\frac{1}{0.5 horas}$
* Capacidad = Número de doctores $\rightarrow C=1$

Ahora, el apartado a) nos pide el tiempo promedio que el paciente espera para ser atendido. Para ello necesitamos calcular $W$ ya que es el **tiempo promedio esperado en el sistema**. Utilizamos la siguiente fórmula

$W=\frac{E[s]}{1-ρ}$

Pero, no sabemos cuánto es $ρ$, así que lo calculamos de la siguiente forma:

$ρ=\frac{λ⋅E[s]}{c}=\frac{\frac{1}{30 min}⋅ 20 min}{1}=\frac{2}{3}=0,\overline{6}$

Entonces:

$W=\frac{E[s]}{1-ρ}=\frac{20 minutos}{1-0,\overline{6}}=60 minutos$

Ahora, el apartado b) nos pide el **tiempo promedio que el paciente espera en la sala de espera de emergencias**, puede pensarse como el **tiempo en la cola**. Esto se corresponde con $Wq$ que es **el tiempo promedio esperado en la cola**. Puede calcularse de dos formas:

$Wq=\frac{ρ⋅E[s]}{1-ρ}=\frac{0,\overline{6}⋅20 minutos}{1-0,\overline{6}}=40 minutos$

La otra forma es: $Wq=W-E[s]=60 minutos-20 minutos=40 minutos$

El apartado c) nos pide el **N° de pacientes promedio en cola**, esto se corresponde con $L$, que describe el **número promedio de usuarios en el sistema**. Puede calcularse:

$L=λ⋅W=\frac{1}{30 minutos}⋅60 minutos=2 usuarios$

De la misma manera el apartado d) nos pide el **N° de pacientes promedio en sala de espera de emergencias**, esto puede pensarse como el **número promedio de pacientes en cola**. Que se corresponde con el parámetro $Lq$. Puede calcularse de manera similar al $L$:

$Lq=λ⋅Wq=\frac{1}{30 minutos}⋅40 minutos=1,\overline{3} usuarios$

Por último, el apartado e) nos pide **el** $π\_{(90)}$ **del tiempo de espera**, para ello calculamos:

$π\_{q}(90)=W⋅ln(10⋅ρ)=60 minutos⋅ln(\frac{20}{3})=113,8272 minutos$

1. En una empresa, el gerente debe decidir qué obrero emplear. Uno con buena experiencia (**x**) o uno con menor experiencia (**y**). Sabiendo que la frecuencia con que se descomponen las máquinas sigue la ley de Poisson con un promedio de **1 descompostura/hora** y el costo de no producir de cualquier máquina es de **$25 x hora**.

Si el obrero x pide $20 x hora y el obrero Y pide $12 x hora, con tasa media de reparación de $μ\_{x}=2 \frac{máquina}{hora}$ y $μ\_{y}=1,2 \frac{máquina}{hora}$. El gerente necesita saber cual es el obrero más conveniente, sabiendo que las jornadas de trabajo son de $8 \frac{horas}{día}$.

$Costo de trabajo=costo de mano de obra+costo tiempo no productivo$

Explicitar la recomendación al gerente

Resolución:

*Datos del enunciado:*

* Promedio de descompostura/hora$\rightarrow λ=1\frac{descompostura}{hora}$
* Precio de los obreros$\rightarrow \$\_{x}=20\frac{\$}{hora}, \$\_{y}=12\frac{\$}{hora}$
* Tasa de reparación$\rightarrow μ\_{x}=2 \frac{máquina}{hora}⇒E[s]\_{x}=0,5\frac{hora}{máquina}$, $μ\_{y}=1,2 \frac{máquina}{hora}⇒E[s]\_{y}=0,8\overline{3}\frac{hora}{máquina}$
* Duración de jornadas diarias$\rightarrow d=8 \frac{horas}{dia}$

En general, vamos a tener que ver cual costo de trabajo es menor.

Primero hagamos los cálculos para el obrero x:

$ρ\_{x}=\frac{λ⋅E[s]\_{x}}{c}=1\frac{descompostura}{hora}⋅0,5\frac{hora}{máquina}=0,5$

$W\_{x}=\frac{E[s]\_{x}}{1-ρ\_{x}}=\frac{0,5 \frac{hora}{máquina}}{0,5}=1 \frac{hora}{descompostura}$

$L\_{x}=λ⋅W\_{x}=1 \frac{descompostura}{hora}⋅1\frac{hora}{descompostura}=1 máquina$

$Costo de trabajo\_{x}=costo de mano de obra\_{x}+costo tiempo no productivo\_{x}$

$\frac{Costo de trabajo}{hora}\_{x}=20\frac{\$}{hora}+L\_{x}⋅costo n/operativo$

$\frac{Costo de trabajo}{hora}\_{x}=20\frac{\$}{hora}+1 máquina⋅25\frac{\$}{hora}$

$\frac{Costo de trabajo}{hora}\_{x}=45\frac{\$}{hora}$

$\frac{Costo de trabajo}{jornada}\_{x}=45\frac{\$}{hora}⋅8\frac{horas}{jornada}=360\frac{\$}{jornada}$

Ahora repetimos todo para ver el costo de trabajo del obrero **y**:

$ρ\_{y}=\frac{λ⋅E[s]\_{y}}{c}=1\frac{descompostura}{hora}⋅0,8\overline{3}\frac{hora}{máquina}=0,8\overline{3}$

$W\_{y}=\frac{E[s]\_{y}}{1-ρ\_{y}}=\frac{0,8\overline{3}}{0,1\overline{6}}=5\frac{horas}{descompostura}$

$L\_{y}=λ⋅W\_{y}=1 \frac{descompostura}{hora}⋅5\frac{hora}{descompostura}=5 máquinas$

$Costo de trabajo\_{y}=costo de mano de obra\_{y}+costo tiempo no productivo\_{y}$

$\frac{Costo de trabajo}{hora}\_{y}=12\frac{\$}{hora}+L\_{y}⋅costo n/operativo\_{y}$

$\frac{Costo de trabajo}{hora}\_{y}=12\frac{\$}{hora}+5⋅25\frac{\$}{hora}$

$\frac{Costo de trabajo}{hora}\_{y}=137\frac{\$}{hora}$

$\frac{Costo de trabajo}{jornada}\_{y}=137\frac{\$}{hora}⋅8\frac{horas}{jornada}=1096\frac{\$}{jornada}$

Comparando los valores que obtuvimos con el obrero x y el obrero y ($360<<1096$), por ende nuestra recomendación sin duda sería de contratar al obrero **x**. Si bien tiene un costo de mano de obra más caro, se remedia con la cantidad de máquinas no productivas que hay en un momento.

# Parcial de la 305

1. Enumere los elementos de un sistema de colas abiertas y explíquelos

![](data:image/png;base64...)

Un sistema de colas abiertas se compone de tres elementos principales:

* La **población**, se trata del conjunto de usuarios. Los usuarios son aquellos que desean algún tipo de servicio de un conjunto de servicios que dispone el sistema.
* Los **servicios**, son aquellas facilidades que brinda nuestro sistema. Pueden ser establecer una comunicación, procesar una pregunta, o atender un pedido de entrada/salida, etc.
* **Servidor:** Es quien provee uno o más servicios que resultan de interés para los usuarios. Puede tener un único servidor, el cual puede atender un único usuario por vez o ser multiservidor y tener varios servidores idénticos que puedan atender hasta n usuarios simultáneamente.
* La **cola o línea de espera**. La cola de espera se origina cuando ingresan usuarios al sistema y no hay servidores que los puedan atender, ya sea porque están ocupados o por algún otro motivo. De esta forma, los usuarios conforman una cola de espera para ser atendidos. Hay diferentes **disciplinas** que determinan diferentes reglas para seleccionar al próximo usuario, la más común es FIFO (First In, First Out). Sin embargo existen otras como: LIFO (Last In, First Out) o disciplinas que determinan al próximo usuario por un sistema de prioridades

En el caso del sistema de colas abiertas, cabe destacar que la **capacidad de la cola de espera no tiene límites**, la **fuente de usuarios es infinita** y la disciplina es **FIFO**.

Se considera abierto porque los usuarios entran al sistemas desde el exterior, reciben el servicio y se van.

1. Explicar el concepto de punto de saturación.

El punto de saturación se define como el punto en el que la capacidad del enlace se ve sobrepasada por la intensidad de tráfico que circula por él. Se utiliza el **factor de utilización**($ρ$) para comparar con el punto de saturación y analizar que tan saturado se encuentra el enlace:

$ρ=\frac{λ}{η ⋅ C}$

1. 6 horas de atención, 50 personas por día, tiempo de servicio 7 minutos.
   1. tiempo promedio en la caja

Datos del enunciado:

tiempo de servicio de 7 minutos $⇒E[s]=7 min$

50 personas por día $⇒50 \frac{personas}{día}=50 \frac{personas}{día}⋅(\frac{1}{6}⋅\frac{día}{horas})⋅(\frac{1}{60}⋅\frac{hora}{minutos})=0,1389\frac{personas}{minuto}=λ$

$Wq=\frac{ρ⋅E[s]}{1-ρ}$

$u=λ⋅E[s]=7 min ⋅0,1389=0,9723$

$ρ=\frac{0,9723}{1}=0,9723$

$Wq=\frac{ρ⋅E[s]}{1-ρ}=\frac{0,9723⋅7}{0,0277}=245,70$

* 1. tiempo promedio en la compañía

$W=Wq+E[s]=245,70 + 7= 252,7$

* 1. Número de usuarios promedio en cola

$Lq=Wq⋅λ=245,70⋅0,1389=34,1278$

* 1. Número de usuarios promedio en el organismo

$L=W⋅λ=252⋅0,1389=35,0028$

* 1. Conclusiones y propuestas de solución

El tiempo de espera resulta **excesivamente alta**, se podrían agregar más cajas para subsanar esto.

![](data:image/png;base64...)

1. Qué es M/M/1 cuando es cola de espera sin límites, fuente de usuarios infinita y disciplina FIFO

**M/M/1** es la notación que se utiliza para describir los parámetros y características de un sistema de cola. Suponiendo que la cola de espera no tiene límites, la fuentes de usuarios es infinita y la disciplina es FIFO, **M/M/1** significa:

* **M**: indica que el proceso de llegada de los usuarios sigue una distribución de Poisson
* **M**: indica que el tiempo de servicio para cada usuario sigue una distribución Exponencial.
* **1**: indica que hay un único servidor en el sistema.

Se trata de un sistema en el que:

* el tiempo entre llegadas es exponencial, de media 1/λ,
* el tiempo de servicio también es exponencial, de media 1/μ,
* hay un único recurso para atender las peticiones,
* y la longitud de la cola no está limitada.