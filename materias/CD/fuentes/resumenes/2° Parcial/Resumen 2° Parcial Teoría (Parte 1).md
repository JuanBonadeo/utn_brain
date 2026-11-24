**Modelo OSI**![](data:image/jpeg;base64...)

El **modelo OSI** es un modelo de referencia.

Surge de la necesidad de crear un modelo estándar de los protocolos utilizados en capas.

Su nombre se debe al hecho de que se utiliza en sistemas que están abiertos a la comunicación con otros sistemas.

El modelo OSI consta de 7 capas, donde en cada una de ellas se realizará una tarea específica.

1. **Capa Física:** lleva a cabo la transmisión de bits puros a través de un canal de comunicación.

2. **Capa de enlace de datos:** transforma un medio de transmisión puro en una línea de comunicación que esté libre de errores de transmisión.

3. **Capa de Red:** controla las operaciones de la subred, la congestión de datos y la calidad del servicio proporcionado (retardo, tiempo de tránsito, inestabilidad, etcétera).

4. **Capa de Transporte:** acepta los datos que llegan, los pasa a la capa de red y se asegura de que lleguen correctamente a destino.

5. **Capa de Sesión:** permite que los usuarios de máquinas diferentes establezcan sesiones entre ellos.

6. **Capa de Presentación:** maneja estructuras de datos abstractas y permite definir e intercambiar estructuras de datos de un nivel más alto

7. **Capa de Aplicación:** contiene protocolos que los usuarios requieren con frecuencia, como el HTTP que se necesita para páginas web.

**Asignación de Capacidades de Canales**

La capacidad que debe tener cada enlace está determinada por un conjunto de factores que la condicionan, entre ellos:

- promedio de mensajes que genera

- frecuencia de mensajes que llegan

- promedio de mensajes entre dos terminales.

- etc

$λ\_{i} $ Frecuencia promedio de mensajes de enlace: nro de terminales conectadas \* nro de mensajes por segundo.

El nro de terminales conectadas y el de mensajes por segundo vienen como datos del problema

$∼\_{i}$ Longitud promedio de bits (bits)

$C\_{i}$ Capacidad del canal (bps)

$μ\_{i}$ frecuencia de mensajes a la salida por segundo → $μ\_{i }= ∼\_{i}\*C\_{i}$ (bps)

$T\_{i}$ tiempo de retardo promedio del mensaje → $T\_{i}=\frac{1}{μ\_{i}- λ\_{i}}$ (segundos)

$p\_{i}$ intensidad de tráfico → $p\_{i }=\frac{λ\_{i}}{μ\_{i}}$ (sin unidad). Idealmente $p\_{i}<1$

Explicación mediante un ejemplo:

Se tienen 7 ciudades (enlaces), cada una de ellas con un determinado nro de terminales, conectadas a una computadora central en Rosario.

Cada terminal emite 1 mensaje cada 30 segundos y cada mensaje tiene una longitud promedio de 120 bits.

Se busca determinar la capacidad ($C\_{i}$), en bps, para cada uno de los 7 enlaces.

Cada terminal tiene frecuencia promedio de mensajes = $\frac{1}{30}\frac{mensajes}{segundos}$

Por lo tanto, la frecuencia promedio de mensajes en cada enlace es igual al nro de terminales \* frecuencia promedio de mensajes de la terminal.

Ej: $λ\_{1}=10\*\frac{1}{30}\frac{mensajes}{segundos}=0,33\frac{mensajes}{segundos}$

**Teoría de Cola**

Una cola es una línea de espera y la teoría de cola es el estudio del fenómeno de la espera en la cola.

1. Enumere y explique los elementos de un sistema de colas abiertas

Dentro del sistema de colas abiertas se tienen 3 elementos:

1. Usuarios: los usuarios son aquellos que desean algún tipo de servicio de un conjunto de servicios que dispone el sistema
2. La cola o línea de espera: La cola de espera se origina cuando ingresan usuarios al sistema y no hay servidores que los puedan atender, ya sea porque están ocupados o por algún otro motivo. De esta forma, los usuarios conforman una cola de espera para ser atendidos.
3. Servidor: Es quien provee uno o más servicios que resultan de interés para los usuarios. Puede tener un único servidor, el cual puede atender un único usuario por vez o ser multiservidor y tener varios servidores idénticos que puedan atender hasta n usuarios simultáneamente.
4. Servicio: es una acción. El servicio puede ser establecer una comunicación, responder una pregunta, realizar un pedido, etc.
5. Explique el concepto de punto de saturación

El punto de saturación se da entre medidas, W: tiempo de respuesta medio y N: número de terminales. Para N>=1 no hay cola (ya que se tiene una sola terminal) y W va a tender a 0.

1. Cuando la cola de espera no tiene límites, la fuente de usuarios es infinita y la disciplina es FIFO, indique el significado de m/m/1.

M/M/1 es la notación que se utiliza para describir los parámetros y características de un sistema de cola. Suponiendo que la cola de espera no tiene límites, las fuentes de usuarios es infinita y la disciplina es FIFO, M/M/1 significa:

M: indica que el proceso de llegada de los usuarios sigue una distribución de Poisson

M: indica que el tiempo de servicio para cada usuario sigue una distribución Exponencial.

1: indica que hay un único servidor en el sistema.

Preguntas mías aparte:

1. ¿En qué consiste la disciplina de cola? La disciplina de cola es la regla para seleccionar el próximo usuario a recibir servicio. La disciplina más común es la FIFO (primero en llegar, primero en ser atendido), pero también hay otras como la LIFO (último en llegar, primero en ser atendido) u alguna otra de preferencia del usuario.
2. Notación A/B/c: donde A indica la distribución entre intervalos, B la distribución de tiempo y c el número de servidores. Es la notación más frecuente, se utiliza cuando la espera no tiene límites, la fuente de usuarios es infinita (que se permite a cualquier usuario que arribe) y la disciplina en FIFO.
3. Intensidad de tráfico: determina el número mínimo de servidores que se requieren para cumplir con el flujo entrante de usuarios. Es igual al tiempo de servicio promedio E[s] dividido el promedio entre arribos E[T].

1. Modelo de cola abierta (M/M/c): se considera abierto porque los usuarios entran al sistema desde el exterior, reciben el servicio y se van.
2. Modelo de cola en sistemas interactivos con población finita: En este sistema ningún usuario entra ni sale y se posee una población finita de usuarios.