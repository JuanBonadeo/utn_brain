UNIVERSIDAD TECNOLÓGICA NACIONAL![](data:image/png;base64...)

Facultad Regional Rosario

Ingeniería en Sistemas de Información

**Asignatura:** Comunicación de datos

**Profesores:** Germán Bernardo Baró y Cristian Medin

**Comisión:** 303

**Integrantes:**

* Juan Pedro Casañas (Legajo: 50373)
* Maria Sofia Ochoa (Legajo: 50452)
* Martin Quagliardi (Legajo: 51657)
* Mateo Regodesebes (Legajo: 51079)

**Trabajo Práctico:**  Teoría de Colas - Asignación de capacidad de canales

**Año:** 2024

Índice

[**Introducción 2**](#_9q9an536qh36)

[**Desarrollo 3**](#_d0bja71ige9g)

[**Asignación de capacidad de canales 3**](#_dkwep2xlxl1c)

[Aplicación de teoría de cola 5](#_v81df9fpnhvh)

[**Teoría de Colas 14**](#_24xpol82ukx2)

[Definición 14](#_carlzdj5yt9l)

[Nociones de un Sistema de Cola 16](#_m9bhw03vmmka)

[Variables de interés 18](#_t91idr8d8pl0)

[*Ejemplo 20*](#_dyt0e4pfmn80)

[Notación de Kendall 21](#_jxr8ph8jyzgn)

[*Ejemplos 22*](#_npzhrfwy67av)

[Teorema de Little 23](#_y8hipbqrhw6a)

[El sistema M/M/1 26](#_u2slxbrf9kz1)

[Sobre el significado de 27](#_kkpd2clg0wt1)

[Análisis de prestaciones básicas del sistema 28](#_kj9krwlqzt2)

[*Ejemplo 28*](#_b0xi8cc2rk1d)

[Relación entre N, T, W y Q 29](#_j0ae98c66ggo)

[Funciones de distribución del retardo FW y FT 30](#_ywwwzhjrsqp3)

[*Ejemplo 31*](#_xk23hdiqe4e7)

[Proceso de salida de un M / M / 1 32](#_qm35nv66zt5p)

[El sistema M / M / m 33](#_wcb7jy27kdzg)

[Cálculo de pn y probabilidad de espera en cola 36](#_7qltwa1loz3e)

[Prestaciones de un M/M/m vs. un M/M/1 con la misma capacidad 38](#_fiw2c2uaraq4)

[Modelo de Cola en Sistemas Interactivos con Población Finita 39](#_23zze3w1gw7v)

[**Conclusiones 43**](#_j7d4cfk1rorh)

[**Bibliografía 44**](#_44sxque8tmcu)

[**Anexo: Autoevaluación con Preguntas y Respuestas 45**](#_9c3q4o128beq)

# Introducción

En el área de la comunicación de datos, la eficiencia y la fiabilidad son aspectos cruciales que determinan el rendimiento de los sistemas de transmisión y recepción de datos. Dos conceptos fundamentales que influyen en la variabilidad de estos aspectos son la asignación de capacidades de canales y la teoría de colas.

Por un lado, la asignación de capacidades de canales se refiere a la distribución eficiente del ancho de banda disponible entre múltiples usuarios o aplicaciones, optimizando así el uso de los recursos de la red.

Por otro lado, la teoría de colas permite tener un marco matemático para analizar y gestionar las colas de espera en sistemas donde los recursos son limitados, como en servidores y enrutadores de red.

La asignación adecuada de la capacidad de los canales asegura que los datos se transmitan de manera efectiva, minimizando la latencia y maximizando el rendimiento de la red. Este proceso implica técnicas avanzadas de optimización y algoritmos adaptativos que se ajustan dinámicamente a las condiciones cambiantes del tráfico de datos. Por su parte, la teoría de colas ofrece herramientas analíticas para modelar y predecir el comportamiento del tráfico de datos, permitiendo a los ingenieros de red diseñar sistemas más robustos y eficientes.

El objetivo de este trabajo es explorar en profundidad estos dos conceptos interrelacionados y su impacto en el rendimiento relacionado a la comunicación de datos. La idea es realizar un análisis sobre los principios teóricos detrás de la asignación de capacidades de canales y la teoría de colas, así como sus aplicaciones prácticas en el diseño y gestión de redes modernas.

# Desarrollo

## Asignación de capacidad de canales

La idea es analizar el problema de determinar: ¿qué capacidad debe tener cada enlace(en **bps**) para suministrar un determinado rendimiento?

Se supone que el tráfico se distribuye de manera uniforme. Esto incluye la frecuencia de ingreso, la longitud media de los mensajes y la promedio de la cantidad de mensajes entre dos puntos de la red.

La asignación de capacidades es el primer paso antes de abordar problemas como la elección de topología, la conexión entre concentradores, el ruteo de mensajes, etc.

Existen distintos criterios para la asignación de capacidades.

Se adopta el criterio señalado por L. Kleinrock, que supone el costo **linealmente proporcional** a la capacidad.

Esto implica que *el costo equivale a una determinada capacidad total de la red*. Luego, se asignarán las capacidades enlace por enlace, con el criterio de tiempo promedio de retardo mínimo. Esto da lugar a un método denominado “*estrategia de asignación de capacidades de la raíz cuadrada*”. En la cual **la capacidad de cada enlace** es **proporcional** a **la raíz cuadrada del flujo de tráfico a través del enlace**.

*Ejemplo*:

Consideremos el caso más simple: hay **siete ciudades** con un número específico de terminales de datos (TTY) para conectarse a una computadora central en Rosario. Se elige la configuración de **red estrella**.

Cada terminal (TTY) se supone que producen un mensaje, en promedio, 30 seg. Cada mensaje cuenta con una longitud promedio de 120 bits.

El objetivo es determinar las capacidades troncales (Ci), en bps, para cada uno de los siete enlaces.

Como introducción a este tema, veremos lo que ocurre en el concentrador en un nodo típico. Este proceso consiste en **combinar** los mensajes entrantes y **redirigirlos** hacia el enlace adecuado después de haber completado los procesamientos y almacenamientos necesarios. El modelo más sencillo asume que todos los puestos de entrada se examinan instantáneamente y los mensajes se almacenan en un buffer FIFO(**First-In-First-Out**). Este método se considera multiplexado asincrónico o estadístico. Después de un proceso específico, los mensajes destinados al enlace **i** se envían uno a la vez a la línea de salida del concentrador.

En el ejemplo dado, debido a que cada concentrador tiene una configuración estrella, se produce un solo buffer. uno solo de los enlaces de salida).

**![](data:image/png;base64...)**

Ignoremos los detalles de las operaciones de concentración y almacenamiento al asignar capacidades. Además, suponemos que el retardo de espera de enlace (línea disponible) es menor que el tiempo de procesamiento nodal de manera de simplificar significativamente el entendimiento.

El modelo se reduce entonces a:

![](data:image/png;base64...)

La **frecuencia promedio de mensajes i del enlace i** es la suma de las frecuencias de los mensajes de todas las líneas entrantes al nodo.

Por ejemplo: en la red estrella de la figura cada terminal tiene la misma frecuencia promedio de mensajes (1/30 mensajes/seg.), entonces, i para el i-ésimo enlace es el número de terminales conectados a este por el número de mensajes por segundo.

Para el enlace 1 se tiene, en promedio:

en relación con los 10 terminales conectados al hub de Mendoza.

### Aplicación de teoría de cola

La teoría de cola puede aplicarse a este modelo. Se supone para ello, frecuencia de arribo de mensajes **Poisson** con mensajes de longitud exponencialmente distribuidos con una longitud promedio de mensajes de y un buffer de capacidad infinita, resultando un tiempo de retardo promedio del mensaje de:

donde

* es la frecuencia de mensajes por segundo a la salida

Este parámetro () tiene la particularidad de que no debe superar a valor resultante de multiplicar la capacidad del canal () por la longitud promedio en bits de los mensajes (). Quedándonos entonces:

Y reemplazando esto en la ecuación previa a este inciso:

Este retardo incluye el retraso del mensaje en el buffer y el tiempo necesario para transmitirlo. Los buffers reales pueden suponerse como buffers infinitos porque tienen una probabilidad de bloque inferior a .

El tiempo de retardo aumenta cuando la frecuencia de flujo de tráfico se acerca al valor . Es común establecer un parámetro de intensidad de tráfico que coincide con el factor de utilización por tener un solo servidor, es decir, . Por ende:

Utilizando este parámetro, entonces:

Si , el retardo será igual a , lo que indica el tiempo necesario para transmitir el mensaje completo. Si planteamos , será muy grande.

Siguiendo con el ejemplo, Si y , y si se produce un retardo por mensaje transmitido sobre el canal de salida de:

De este tiempo el necesario para transmitir el mensaje será:

Y el tiempo de almacenamiento es:

Resultando entonces:

El tiempo de retardo sobre el canal Rosario-Buenos Aires con la misma

capacidad (100 bps) se tiene:

Por su parte, para Corrientes y Rosario será, para la misma capacidad:

Si ahora incrementaramos el tiempo de retardo a 900 bps

![](data:image/png;base64...)

Considerando la red como un conjunto de enlaces (uno por nodo), el buffer asociado con el enlace i-ésimo tiene una frecuencia de arribo de y y la longitud promedio de mensaje emitido será , se tiene:

![](data:image/png;base64...)

Se considera que de esta manera, la red funciona como una "caja negra", monitoreando los ingresos y recibiendo mensajes por unidad de tiempo, donde:

La caja negra se comporta como una cola entonces, por el teorema de Little,

tenemos:

Para el promedio estadístico se tiene:

Cuando sumamos todos los buffers de la red y aplicamos el teorema de Little a cada uno de ellos, obtenemos:

Podemos comenzar a abordar el problema de asignación de capacidades de canales en una red utilizando la ecuación de tiempo de retardo.

Se supone que el objetivo es reducir el tiempo de espera promedio en la red completa con una capacidad total fija. La frecuencia de la red total será:

El retardo promedio de mensajes para la red se puede calcular por medio de la ecuación(\*).

donde exhibe un tiempo de retardo "pesado" con los que se encuentran entre 1 y 7. Se obtiene si se considera la capacidad total como la suma de las capacidades , resulta:

Para mantener constante , se deben elegir los valores de que minimicen . Esto se puede lograr utilizando multiplicadores de Lagrange. Luego del de proceso de minimización y diferenciación, se obtiene que:

cumple la función de parámetro representativo de la intensidad de tráfico para toda la red.

Es posible reemplazar cada canal en la ecuación y encontrar para cada canal con esta relación de capacidades. Luego se puede encontrar la expresión , que es:

Esta asignación de capacidad recibe el nombre de “*regla de asignación de la raíz cuadrada del flujo de información*”

El Tmin está inversamente relacionado con C, o el costo. Siempre se puede aumentar el valor de C y aumentar el costo. La ecuación de Tmin proporciona el tiempo de espera mínimo posible para un costo específico.

Podemos descomponer la ecuación relacionada al en dos factores:

* El primer factor es el valor mínimo necesario que puede asumir , de manera que permite el tráfico en un canal donde
  + es el promedio de mensajes manejados.
  + es la longitud promedio de los mensajes.
* La segunda parte indica la capacidad remanente según la estrategia de la raíz cuadrada.

| *Ejemplo:*  ¿Cómo aplicamos, ahora, la estrategia de la raíz cuadrada al ejemplo que venimos trabajando?  A través del enunciado dado podemos determinar la inversa de la longitud para todos los enlaces. Luego, teniendo como base a cada , hallamos:  Luego, para .  Como la capacidad total de la red, resulta un . |
| --- |

En la práctica, se realizan varias elecciones de , cada una de las cuales corresponde a diferentes costos; se encuentra el valor de tiempo de espera mínimo para cada una de ellas, y se grafica el tiempo de espera vs. el costo. Esto permite obtener la adecuada durante un período de tiempo determinado.- De esta manera se obtiene:

| **Enlace** |  |  |
| --- | --- | --- |
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |
| 4 |  |  |
| 5 |  |  |
| 6 |  |  |
| 7 |  |  |

Después de eso, se deben elegir los valores de capacidad reales. En este caso, se han elegido canales de 450 o 900 bps.

| **Enlace** |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |
| 6 |  |  |  |  |
| 7 |  |  |  |  |
|  |  |  | Costo Total: |  |

El costo de la línea de 450 bps es de aproximadamente 1 U$S por Km, y el de 900 bps es de 1,2 U$S por Km. Es claro que el costo sería menor si adoptamos una topología árbol.

Ahora consideraremos el mismo problema con una estructura de árbol para ver cómo cambian los parámetros de la red y el costo. Inmediatamente se nota una notable disminución en los kilómetros de canales.

![](data:image/png;base64...)

Para examinar esta red y elegir la asignación de capacidad adecuada, es importante considerar no solo los mensajes de los terminales que ingresan a cada nodo, sino también los mensajes de los concentradores previos. Si se utiliza un multiplex estadístico, se pueden sumar las frecuencias de llegada y llegada para calcular la frecuencia de llegada total al nodo. Sin embargo, las estadísticas de mensaje sobre los enlaces posteriores ahora están relacionadas con otros. Es cierto si se considera la idea de independencia, es decir, se desconocen las conexiones entre las diferentes colas.

Bajo esta suposición, se supone que cada nodo genera mensajes independientemente con longitudes independientes seleccionadas de una distribución exponencial.

Después, se agregan únicamente las tasas de llegada. de los enlaces anteriores a los que ingresan al concentrador a través del puerto de entrada, tratando cada uno de ellos como si fueran generados por terminales equivalentes.

|  | Caso óptimo | Caso discreto | | | |
| --- | --- | --- | --- | --- | --- |
| **Enlace** |  |  |  |  |  |
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |
| 4 |  |  |  |  |  |
| 5 |  |  |  |  |  |
| 6 |  |  |  |  |  |
| 7 |  |  |  |  |  |
|  |  |  |  | Costo Total: |  |

Observar que esta red produce más rápido en promedio que la topología estrella. La eliminación de cuatro largos tramos reduce el costo. Podemos aumentar la capacidad para reducir el retardo. El costo puede no aumentar tanto como en la topología estrella y ambas estructuras pueden tener tiempos de retardo similares.

##

## Teoría de Colas

Una cola es un sistema con uno o más recursos disponibles para una población de usuarios, que puede que tengan que esperar para poder acceder a los mismos por estar ocupados por otros usuarios. La “teoría de colas” se dedica al estudio de dichos sistemas, que sirven para modelar, por ejemplo, una central de conmutación de llamadas donde puede producirse saturación en las líneas, o un centro de atención a usuarios, donde las llamadas pueden quedar a la espera de que un operador quede disponible.

En el terreno de las comunicaciones, la teoría de colas se ha empleado tradicionalmente para modelar sistemas con conversaciones de voz. Recientemente también se aplica para modelar escenarios de conmutación de paquetes, más allá de que es preciso tener cierto cuidado en las suposiciones realizadas a la hora de modelar el sistema.

### Definición

En general, una cola es un sistema con una serie de recursos y una línea de espera, en la que las peticiones de una población de usuarios aguardan a que alguno de los recursos quede disponible para ser atendidos.

Figura 1.1: Caso general de una cola.![](data:image/png;base64...)

Tal como se ilustra en la Figura 1.1, se aprecian los siguientes elementos principales:

* Una **población** que genera peticiones al sistema. En un caso general, la tasa de generación de peticiones dependerá, entre otros factores, de si la población es finita o infinita. Si la población es finita, que un usuario haya generado una petición puede afectar a la cantidad de peticiones que se puedan generar a continuación. Si la población es infinita, la tasa de generación no dependerá, en principio, del número de peticiones en el sistema.
* Una **cola** en la que las peticiones generadas por la población aguardan a ser atendidas. Dicha cola podrá tener un tamaño limitado o ilimitado. En el primer caso, el sistema rechazará las peticiones que no tengan lugar, bien rechazando la nueva petición, o expulsando alguna que ya exista. En el caso extremo, la cola tendrá un tamaño nulo, por lo que las peticiones o acceden directamente a los recursos, o no accederán al sistema.

Además de esta política de rechazo, la cola también debe definir el tipo de políticas para atender las peticiones; si hay peticiones con mayor prioridad que otras, o si las peticiones se atienden una a una o en bloque.

* Una serie de **recursos** en paralelo, a los que los usuarios acceden tras pasar por la cola. Un usuario accede a un recurso, y en general dichos recursos serán idénticos, siendo el tiempo medio de servicio en cualquiera de ellos.

### Nociones de un Sistema de Cola

En esta sección definiremos conceptos clave para comprender un sistema de cola:

* **Fuentes**: Cuando hablamos de fuentes nos referimos al conjunto de usuarios que son capaces de solicitar el servicio del sistema. Las fuentes pueden ser finitas o infinitas.
   En el caso de trabajar con una fuente finita, la longitud de la cola estará determinada por el número de usuarios en el sistema, ya que estos son quienes afectan la frecuencia de arribo a ella. En cambio, en un sistema con fuente infinita, la cola es justamente ilimitada, por lo tanto la frecuencia de arribos no se ve alterada por el número de usuarios presentes en el sistema. Por lo general, si nos encontramos frente a una fuente limitada pero que posee un gran número de usuarios potenciales entonces suponemos a la población como infinita con el objetivo de simplificar la tarea matemática.
* **Proceso de arribo**: Supongamos que los usuarios entran en el sistema en los tiempos: t0 < t1 < t2 < … < tn. Denominamos ‘Intervalos de arribo’ a las variables aleatorias .En este caso forma una secuencia de variables aleatorias distribuidas independiente e idénticamente y se usa el símbolo para un intervalo arbitrario entre arribos.
   El patrón más común de arribos en la terminología de la teoría de cola es el patrón de arribo aleatorio (O proceso de arribo de Poisson) lo cual significa que la distribución de intervalos entre arribos será exponencial, esto es: .
   Para cada intervalo entre arribos y la probabilidad de n arribos en algún intervalo de tiempo t es: . Donde n = 0, 1, 2, …, n; es la frecuencia promedio de arribos y el número de arribos por unidad de tiempo tiene una distribución de Poisson.
* **Distribución del tiempo de servicio**: El tiempo de servicio se modela a omo una variable aleatoria con una distribución exponencial, donde la función de distribución es = 1. Para medir la variabilidad de los tiempos de servicio y los intervalos de arribo, se utiliza el coeficiente de variación al cuadrado C2, definido como:

  - para una variable constante.
  - para una distribución Erlang-k
  - para una distribución exponencial

   A partir de estos C2 sacamos las siguientes conclusiones:

  - Un C2 cercano a cero indica un patrón regular.
  - Un C2 cercano a uno indica aleatoriedad.
  - Un C2 mayor que uno sugiere agrupamiento de eventos.

   Valores similares de C2 se aplican a los tiempos de servicio: Valores bajos indican tiempos constantes, mientras que valores altos reflejan mayor variabilidad.
* **Capacidad máxima del sistema de cola**: En algunos sistemas de colas, se asume que la capacidad de la cola es infinita, lo que significa que cualquier usuario que llegue puede ser atendido sin restricciones. En contraste, los sistemas de pérdida, también conocidos como sistemas con capacidad de línea cero, no permiten la espera de nuevos usuarios cuando todos los recursos están ocupados. Aunque estos sistemas tienen una capacidad de cola limitada, no es infinita; si un usuario llega cuando el sistema está completo, no podrá esperar.
* **Número de Servidores**: Los sistemas de colas pueden contar con un único servidor (El sistemas de cola más simple) o con m cantidad de servidores idénticos que pueden servir hasta n usuarios diferentes; Esto se denomina Sistema Multiservidor.
* **Factor de utilización del servicio:** Otro parámetro clave es la intensidad de tráfico por servidor (u/c), también conocida como factor de utilización del servicio (ρ\rhoρ) cuando el tráfico se distribuye equitativamente entre los servidores. Este factor representa la probabilidad de que un servidor esté ocupado. En sistemas con un solo servidor, la intensidad de tráfico es equivalente al factor de utilización.

### Variables de interés

Las principales variables que se suelen estudiar en una cola son las siguientes:

* **Tiempo medio de estancia en el sistema (T)**: es el tiempo que transcurre desde que una petición llega al sistema (es generada en la población) hasta que ha sido finalmente atendida por un recurso (abandona el sistema). Dicho tiempo es en general una variable aleatoria en función de distribución .
* **Tiempo medio de estancia en la cola (W)**: es el tiempo que transcurre desde que una petición llega al sistema hasta que empieza a ser atendida por uno de los recursos. De forma análoga, se puede definir la función de distribución de dicho tiempo .

Se trata de retardos medios para todos los usuarios. Si representa el tiempo que pasó en el sistema el usuario *k,* el tiempo medio de estadía en el sistema puede definirse como

Resulta claro que el tiempo medio total de estadía en el sistema está relacionado con el tiempo medio de espera en cola y el tiempo medio del servicio:

Dado un tiempo medio de servicio , también se puede definir una tasa (máxima) de servicio , que se corresponde con el ritmo al que los usuarios “salen” de un recurso si éste siempre se encuentra ocupado. Por lo tanto, la expresión anterior también puede escribirse como

* **Número medio de usuarios en el sistema** (N): que es la media temporal del número de usuarios (o peticiones) que se encuentran en el sistema, ya sea en la cola o siendo atendidos por un recurso, a lo largo del tiempo.
* **Número medio de usuarios en la cola** (Q): variable similar a la anterior, pero en este caso en vez de considerarse el sistema completo, sólo se considera la cola.

En ambos casos se trata de medias a lo largo del tiempo. Por lo tanto, si representa el número de usuarios en el instante , el número medio de usuarios en el sistema durante el tiempo se define como

#### Ejemplo

Sea un sistema donde el número de usuarios a lo largo del tiempo es el indicado por la figura a continuación: al principio hay dos usuarios, en uno lo abandona y luego en aparecen dos usuarios más, hasta .

![](data:image/png;base64...)Figura 1.2: Número medio de usuarios en un sistema.

El número medio de usuarios en el sistema durante se puede calcular como

En general, se puede definir la **ocupación** de un recurso como la proporción de tiempo que dicho recurso está atendiendo a un usuario. Con dicho parámetro, el número medio de usuarios en un sistema será igual al número medio de usuarios en la cola más el número medio de usuarios en los recursos, esto es:

Cuando el tamaño de la cola sea finito y, por lo tanto, exista rechazo de usuarios, tiene interés tratar con otras dos variables que dependen de la longitud de la cola:

* **La probabilidad de pérdida, o probabilidad de bloqueo** (): probabilidad de que una determinada petición no pueda acceder al sistema, porque se encuentra lleno (todos los recursos y la cola están completamente ocupados).
* **La tasa efectiva de tráfico cursado**: si la población realiza peticiones a una tasa , pero existe dicha probabilidad de bloqueo , entonces el tráfico que se cursa en dicho sistema no es el total del ofrecido, sino una fracción inferior, esto es:

### Notación de Kendall

Aparece la **notación de Kendall** con el propósito de estandarizar la forma en que se definen los posibles sistemas de espera, empleando tres parámetros para especificar las características de una cola:

Dichos parámetros representan:

* **A:** especifica cómo se distribuye el tiempo entre peticiones, es decir, la variable aleatoria entre una petición que llega al sistema y la siguiente.
* **B**: especifica cómo es la variable aleatoria del tiempo de servicio, esto es, el tiempo que pasa desde que una petición accede a un recurso hasta que es atendida. Tanto A como B suelen servir para indicar alguna de las siguientes distribuciones de tiempo:
  + **M** (por Markov, o “sin memoria”): en este caso se trata de la variable aleatoria exponencial.
  + **D:** si se trata de un caso en que dicho tiempo es una constante (esto es, se trata de una variable determinista).
  + **G**: si se analiza un caso genérico, sin tener que especificar cómo se distribuye la variable aleatoria que determina alguno de los tiempos.
* **m:** número de recursos idénticos en paralelo.
* **K:** capacidad máxima de todo el sistema, esto es, número máximo de peticiones que caben a la vez (en la cola y en los servidores). Si representa el número máximo de peticiones que caben en la cola, se cumple entonces que

#### Ejemplos

* Un sistema es una cola en la que:

![](data:image/png;base64...)

* + El tiempo entre una petición y la siguiente es constante (D).
  + El tiempo de servicio para cada petición puede ser cualquier variable aleatoria (G).
  + Hay dos recursos en paralelo (2).
  + La cola tiene una capacidad máxima de dos usuarios, dado que el sistema puede albergar cuatro usuarios en total (4).
* En una cola ![](data:image/png;base64...)
  + El tiempo entre llegadas es exponencial (M).
  + El tiempo de servicio es constante para todos los usuarios (D).
  + Hay tres recursos en paralelo (3).
  + La longitud máxima de la cola puede suponerse ilimitada, dado que la capacidad del sistema es infinita ().

Además de estos parámetros en la notación de Kendall, en ocasiones se emplean dos variables más, por lo que la representación completa sería:

Donde los dos últimos parámetros significan:

* **N:** hace referencia al tamaño (finito o no) de la población, lo que determina cómo varía la tasa de peticiones en función de las que se encuentran en el sistema.
* **Z:** especifica la disciplina de la cola, por ejemplo, si en vez de FIFO se emplea algún tipo de mecanismo que da prioridad a unos usuarios frente a otros.

### Teorema de Little

Se trata de uno de los resultados fundamentales de la teoría de colas, que establece una relación muy sencilla entre la tasa efectiva de entrada de usuarios en un sistema, el número medio de usuarios en dicho sistema, y el tiempo medio total que pasan en el mismo. Se trata además de un teorema generalizado que puede ser aplicado a casi cualquier sistema.

Trabajemos con el sistema ilustrado en la siguiente diapositiva:

![](data:image/png;base64...)

En este sistema vemos que llegan usuarios según un proceso α(t) y del que salen según otro proceso β(t). Dado que el tiempo total que pasa un usuario *i*

en el sistema es la diferencia entre el instante en que sale y aquel en que entró, este tiempo Ti se corresponde con la separación en horizontal entre los procesos β(t) y α(t) (Las líneas punteadas T1, T2, …, etc).

Por otro parte, el número de usuarios en el sistema en un instante de tiempo t es la diferencia (en vertical) entre el proceso de llegadas y el de salidas, esto es:

N(t) = α(t) − β(t).

Como se ha visto anteriormente, el número medio de usuarios

en el sistema se puede calcular como:

![](data:image/png;base64...)

Como podemos ver, esta integral representa el área resultante de restar el área debajo de β(t) a el área debajo de α(t) dando como resultado el área intermedia entre ambas funciones la cual nos da como resultado el número de usuarios que presenta un sistema en promedio. Esta área resultante puede ser aproximada de la siguiente manera:

![](data:image/png;base64...)

Multiplicando la parte derecha por α(t)/α(t), reordenando términos y cálculos de los límites, resulta que:

![](data:image/png;base64...)

De lo que se obtiene que el número medio de usuarios en el sistema N es un producto de dos términos:

* El primer término es (el límite de) el cociente del número total de llegadas al sistema entre el tiempo. Por lo tanto, dicho cociente (si existe el límite) es la tasa media de llegadas al sistema:

![](data:image/png;base64...)

* El segundo término es la suma de todos los tiempos de estancia en el sistema Ti, dividida por el número total de llegadas al sistema. Por lo tanto, este cociente es el tiempo medio de estancia en el sistema:

![](data:image/png;base64...)

**De los dos incisos anteriores podemos expresar al teorema de Little como:**

**![](data:image/png;base64...)**

Veamos un breve ejemplo de su aplicación:

![](data:image/png;base64...)

Analicemos este sistema con dos llegadas, en el que la primera permanece dos unidades de tiempo, y la segunda tres unidades de tiempo. La tasa media de llegadas al sistema es:

![](data:image/png;base64...)

mientras que el tiempo medio de estancia en el sistema es:

![](data:image/png;base64...)

Se puede comprobar se cumple el teorema de Little, dado que el número medio de usuarios en el sistema es

![](data:image/png;base64...)

Que coincide con:

![](data:image/png;base64...)

***Nota:*** *Es importante tener en cuenta a la hora de aplicar el teorema de Little que λ es la tasa media de usuarios que pasan por el sistema, no la tasa ofrecida al sistema. Por lo tanto, en los sistemas donde haya usuarios rechazados habrá que tener en cuenta esta distinción a la hora de aplicar el teorema.*

### El sistema M/M/1

Se trata de un sistema en el que:

* el tiempo entre llegadas es exponencial, de media 1/λ,
* el tiempo de servicio también es exponencial, de media 1/μ,
* hay un único recurso para atender las peticiones,
* y la longitud de la cola no está limitada.

El M/M//1 es el sistema más básico y suele servir para modelar sistemas sencillos con un único recurso atendiendo a una población variada, como, por ejemplo, un punto de acceso WiFi que transmite los datos de varios usuarios.![](data:image/png;base64...)

### Sobre el significado de

El parámetro ρ se define como el cociente entre la tasa de llegadas al sistema y la tasa máxima de salida que proporciona el servidor.

,

Lo que también puede interpretarse como el tiempo medio de servicio entre el tiempo medio entre llegadas

.

Por lo tanto, el hecho de que para que el sistema tenga una solución resulta muy coherente pues: si , se tendría que la tasa media de llegada al sistema es mayor que la tasa máxima de salida (o que el tiempo medio para servir un usuario es mayor que el tiempo medio entre llegadas), por lo que el sistema no sería capaz de cursar la carga de trabajo que se le presenta. Dado que se trata de una cola , la longitud de la cola crecería de forma indefinida, por lo que el número de usuarios en el sistema tendería a infinito.

De esta forma, en un sistema sin rechazo donde el número máximo de usuarios no está ilimitado (número máximo finito de usuarios), si la tasa de llegadas es mayor que la tasa agregada de salida, el sistema se encontrará **congestionado** por lo que no tiene sentido realizar un modelado de sus prestaciones. Cuando el sistema sí rechaza usuarios la condición no resulta necesaria, dado que el número de estados de la cadena de Markov es finito.

### Análisis de prestaciones básicas del sistema

Una vez obtenida la distribución de probabilidades del sistema, se puede obtener cualquiera de las diferentes variables de interés en una cola. Para el resulta sencillo calcular, por ejemplo, el número medio de usuarios en el sistema mediante:

Una vez calculado N, el teorema de Little permite obtener

#### Ejemplo

Sea una línea de transmisión a 100 Mbps, a la que llegan tramas de una longitud que puede modelarse con una variable aleatoria exponencial de media 1500 octetos. El tiempo entre tramas es otra variable aleatoria exponencial de media 0.18 ms. Bajo estas suposiciones, se quiere calcular el retardo medio por trama y el tiempo medio de espera en cola.

Dado que las tramas tienen una longitud exponencial y la velocidad de la línea es constante, el tiempo de transmisión de cada trama será también una variable aleatoria exponencial, de media

y el sistema se puede modelar como un . La ocupación del mismo se puede obtener como

,

siendo el retardo medio

.

Dado que el tiempo de servicio es , el tiempo medio de espera en cola será

.

Dicho tiempo medio de espera en cola también se puede obtener como:

### Relación entre N, T, W y Q

A continuación se presenta un resumen de las expresiones para las prestaciones básicas de un sistema M/M/1. Dada una de ellas, resulta inmediato obtener cualquiera de las otras, bien aplicando el teorema de Little, bien por las expresiones básicas que relacionan las variables en una cola.

![](data:image/png;base64...)

##

### Funciones de distribución del retardo y

Para el caso de un no resulta demasiado complicado calcular la función de distribución del retardo en cola , esto es, la probabilidad de que el tiempo que tenga que esperar una petición hasta acceder al recurso sea menor o igual que t:

.

Para realizar este cálculo, se aplica el teorema de la probabilidad total sobre el número de usuarios que se encontraban en el sistema al llegar una petición:

.

es la probabilidad de que el tiempo de espera en cola W sea menor que t cuando hay n usuarios al llegar. En estas condiciones, W es la suma de los n tiempos de servicio de los usuarios por delante, por lo que su función de densidad es la convolución de n variables aleatorias exponenciales de media 1/μ. Sustituyendo el valor de y separando el caso , se tiene que la ecuación anterior se puede desarrollar como

![](data:image/png;base64...)

Que se puede simplificar como

![](data:image/png;base64...)

En esta expresión, el término de la integral se puede identificar como una variable aleatoria exponencial, de media . Por lo tanto, la ecuación principal queda como

![](data:image/png;base64...)

Siguiendo un razonamiento similar, se puede obtener que la función de distribución del tiempo total en un sistema viene dada por

![](data:image/png;base64...)

esto es, una variable aleatoria exponencial media .

#### Ejemplo

Sea un cajero al que llegan clientes según una tasa de 10 clientes/hora () y el tiempo medio de servicio minutos. La carga del sistema y el retardo medio son, respectivamente,

y minutos.

Por lo que el tiempo medio de espera en cola es minutos. La probabilidad de que un usuario esté más de t unidades de tiempo esperando a usar el cajero vendrá dada por

![](data:image/png;base64...)

por lo que la probabilidad de estar esperando más de 10 minutos será

![](data:image/png;base64...)

De forma análoga, la probabilidad de estar en el cajero más de 10 minutos se puede calcular como

![](data:image/png;base64...)

### Proceso de salida de un

Sea un sistema , con los tiempos entre llegadas y de servicio distribuidos según variables aleatorias exponenciales, de medias y , respectivamente, y –por lo tanto– con una probabilidad de ocupación ρ = λ/μ. A continuación se analiza el proceso de salida de los usuarios de dicho sistema (una vez que han sido servidos).

En un instante t al azar el sistema puede estar libre, con probabilidad , u ocupado, con probabilidad ρ. Gracias a la ley de la probabilidad total, la función de distribución del tiempo hasta la siguiente salida se puede expresar como

![](data:image/png;base64...)

donde es la función de distribución del tiempo hasta la siguiente salida cuando el sistema está vacío, y la función de distribución del tiempo hasta la siguiente salida cuando el sistema está ocupado (es decir, hay al menos un usuario en el recurso). Cuando el sistema está ocupado, el tiempo hasta la siguiente salida es una variable aleatoria exponencial de media 1/μ, por lo que la función de distribución es

![](data:image/png;base64...)

Cuando el sistema está libre, el tiempo hasta la siguiente salida es la suma de dos variables aleatorias exponenciales: el tiempo hasta la siguiente llegada más su tiempo de servicio. La función de distribución de dicha suma es

![](data:image/png;base64...)

Por lo tanto, la función de distribución del tiempo entre salidas en el sistema resulta ser

![](data:image/png;base64...)

Simplificando:

![](data:image/png;base64...)

Por lo tanto, el tiempo entre salidas en un sistema M/M/1 estable (ρ < 1) se distribuye según una variable aleatoria exponencial de media λ−1, al igual que el tiempo entre llegadas. El hecho de que el proceso de salida sea a la misma tasa que el de entrada no debe resultar sorprendente, dado que el sistema ni crea ni rechaza usuarios, sólo los retarda. Sí que resulta destacable que dicho tiempo sea también una variable aleatoria exponencial, por lo que el proceso de salida será de nuevo de Poisson.

##

### El sistema

Al igual que el M/M/1, se trata de un sistema con llegadas de Poisson y tiempos de servicio que siguen una variable aleatoria exponencial, pero en este caso hay m servidores idénticos en paralelo.

![](data:image/png;base64...)

Si hay varios servidores disponibles, un usuario que llegue al sistema será atendido por uno de ellos (no importa el que sea), mientras que si todos están ocupados, el usuario tendrá que esperar en cola hasta que uno quede libre. Se trata de un sistema que podría emplearse para modelar, por ejemplo, centros de atención telefónica, una granja de servidores que resuelven peticiones web, o un supermercado con varias cajas disponibles y una única línea de espera.

La cadena de Markov que modela el comportamiento será parecida a la del M/M/1, con la tasa de transición desde el estado n al n + 1 siempre igual a λ. Sin embargo, la tasa de transición cuando se reduce el número de usuarios n en el sistema es diferente y depende de si n es mayor o menor que m:

* Cuando n ≤ m, no hay usuarios en la cola sino que todos están siendo atendidos. En estas condiciones, la tasa de transición al estado n − 1 es n · μ.
* Cuando n > m, hay usuarios esperando en cola porque todos los recursos están ocupados, por lo que la tasa de transición será m · μ.

La cadena queda, por tanto:

![](data:image/png;base64...)

La forma en la que se calcula la distribución de probabilidades estacionaria es muy parecida al caso anterior, aunque más laboriosa. Por una parte, se tiene que para los estados n ≤ m, las relaciones son de tipo

![](data:image/png;base64...)

Por lo que la expresión para dichos estados queda:

![](data:image/png;base64...)

Por otra parte, para los estados n > m, las relaciones son:

![](data:image/png;base64...)

por lo que la expresión en este caso es:

![](data:image/png;base64...)

que, sustituyendo pm queda como:

![](data:image/png;base64...)

Antes de continuar con el análisis de la Cadena de Markov, conviene detenerse en los dos siguientes términos que hemos visto anteriormente:

![](data:image/png;base64...)

Por una parte, el término ρ se define como el cociente entre la tasa de entrada λ y la tasa máxima de salida con todos los servidores ocupados mμ. Por lo tanto, dado que la capacidad de la cola es infinita, para que se pueda obtener una solución del sistema será necesario que se cumpla (de forma similar al sistema M/M/1)

![](data:image/png;base64...)

Además, el término ρ admite la misma interpretación que en el caso del M/M/1, como valor de ocupación de un recurso. Esto puede verse interpretando los m recursos en paralelo como un sistema al que acceden usuarios a una tasa λ y pasan un tiempo ts = 1/μ. Aplicando Little, el número medio de usuarios en el sistema será

![](data:image/png;base64...)

Por lo que ρ coincide con el porcentaje de tiempo que un servidor está ocupado.

De hecho, este número medio de servidores ocupados mρ coincide con la expresión para el término I. Por lo tanto, I podría interpretarse como el mínimo número de servidores que serían necesarios para atender a una demanda de tráfico λ, si el tiempo medio de servicio es 1/μ.

### Cálculo de y probabilidad de espera en cola

Como se ha visto anteriormente, las probabilidades de cada estado se pueden expresar en función de p0:

![](data:image/png;base64...)

Para calcular se aplica la ecuación ∑ = 1, de lo que resulta

![](data:image/png;base64...)

lo que lleva al siguiente valor de la probabilidad de que el sistema se encuentre vacío:

![](data:image/png;base64...)

A partir de las anteriores expresiones es se puede calcular la probabilidad de que un usuario tenga que esperar, esto es, la probabilidad condicionada de que, al llegar al sistema, haya m o más usuarios:

![](data:image/png;base64...)

y puede obtenerse como

![](data:image/png;base64...)

La expresión para calcular PQ recibe el nombre de **Erlang-C**:

![](data:image/png;base64...)

*Nótese que la Erlang-C, como se ilustra en el ejemplo anterior, es una ecuación de análisis pero no de diseño: fijado un escenario en términos de λ, μ y m dicha expresión permite calcular pm, pero no es posible despejar el mínimo valor de m que garantiza unas prestaciones. Para ello, es preciso emplear un método de “prueba y error” o acudir a tablas precalculadas u otras herramientas numéricas.*

### Prestaciones de un M/M/m vs. un M/M/1 con la misma capacidad

Resulta interesante comparar las prestaciones de un sistema M/M/m donde cada servidor tiene una capacidad μ con las de un sistema M/M/1 con un servidor con capacidad m · μ, dado que en ambos casos la capacidad máxima de procesado es la misma, pero en el primero ésta se encuentra dividida entre varios servidores mientras que en el segundo se encuentra agregada en un único servidor.

Decidimos omitir el desarrollo matemático de esta comparativa ya que distrae de lo importante que son los resultados obtenidos al comparar estos dos sistemas:

* Considerando las prestaciones globales del sistema (el retardo medio total T), resulta mejor agrupar recursos en un único servidor que distribuirlos en dos servidores menos potentes.
* A cambio, el tiempo medio de espera en cola W para el M/M/1 resulta ligeramente mayor (además de otras consideraciones, como p.ej. que un servidor muy potente pueda ser más caro que varios servidores con la misma potencia agregada).

Agregar la capacidad de procesado en un único servidor mejora las prestaciones globales del sistema, siendo éste uno de los resultados fundamentales de la teoría de colas. La explicación para este comportamiento se puede deducir analizando el comportamiento en situaciones de alta y baja carga:

* Cuando la carga sea elevada, ambos sistemas tienen todos sus recursos ocupados, por lo que la salida de usuarios se produce a la máxima capacidad μ.
* Sin embargo, en situaciones de baja carga, en un sistema M/M/1 siempre se aprovechará toda la capacidad μ a partir del primer usuario, mientras que en un sistema M/M/m esto sólo ocurre si hay m o más usuarios en el mismo, por lo que se desaprovechan recursos.

Concluimos entonces que siempre será más óptimo optar por un sistema M/M/1 de igual o mayor capacidad de procesamiento que un sistema M/M/m si nuestro objetivo es exclusivamente la optimización del sistema y no nos concierne cuestiones externas como el costo monetario del mismo.

### Modelo de Cola en Sistemas Interactivos con Población Finita

Consideremos un modelo de cola cerrado (ningún usuario ni entra ni sale) y con una población finita de usuarios.

![](data:image/png;base64...)

Un sistema de procesamiento central consiste de una cola para la unidad central de proceso (CPU), algunas terminales de E/S y un sistema asociado de cola para cada uno de las terminales. Los usuarios interactúan con la CPU a través de las terminales. Cada usuario se supone en uno de los siguientes estados en cada instante:

1. “Pensando” en la terminal (“tiempo de pensamiento”, )
2. Esperando algún tipo de atención.
3. Recibiendo el servicio.

El tiempo de pensamiento *t* es el paso del tiempo entre el cumplimiento del servicio por parte de la CPU (para una interacción dada) y una nueva solicitud de servicio de la CPU por parte del usuario. Entonces, un usuario en la terminal no puede solicitar otro servicio hasta que el servicio pedido anteriormente no haya sido satisfecho.

El usuario puede representarse como una señal que circula en el sistema y que en algún instante está en la terminal, en el CPU o en la cola de espera.

La estructura de cola está determinada por el modelo que se selecciona para el sistema de procesamiento central. Las ecuaciones que describen el modelo en condiciones generales son:

tiempo de respuesta medio

interacción por unidad de tiempo

Donde:

* es el tiempo medio de servicio de la CPU por interacción.
* es la probabilidad de que el sistema esté libre.
* es el tiempo de pensamiento medio (tiempo entre la finalización de un servicio y el próximo pedido).

El sistema de procesamiento central tendrá un modelo de tiempo compartido si el tiempo de servicio de la CPU es continuo, y si se usa la disciplina de cola por muestreo por medio de la CPU. Esta disciplina supone que la potencia de procesamiento de la CPU se distribuye igualmente entre todos los pedidos. Sin embargo, si hay interacciones pendientes para el servicio de la CPU cada una de ellas se sirven instantáneamente por el sistema con una velocidad (frecuencia) de uno o muchos usuarios por unidad de tiempo, donde u es la velocidad de procesamiento de la CPU. SI existe un único CPU usando la disciplina de cola por muestreo, el se calcula de la siguiente forma:

También se puede calcular:

* el factor de ubicación de la CPU.
* la interacción por unidad de tiempo.

Para pocos terminales la interferencia entre usuarios es mínima, esto quiere decir que cuando uno de los usuarios busca una interacción con la CPU los demás generalmente están en el modo de pensamiento, por lo tanto, ocasionalmente se formará una cola de espera. Es posible entonces considerar la curva estratégica a cuando se tiene pocos terminales.

Cuando el número de terminales tiende a infinito, la probabilidad de tener la CPU desocupada () tiende a cero, consecuentemente la curva será asintótica a la recta con N tendiendo a infinito.

La intersección de las dos asíntotas se produce en tal como:

Este valor de se llama punto de saturación del sistema. Se concluye que si cada interacción requiere exactamente unidades de tiempo de servicio de CPU y exactamente “tiempo de pensamiento”, es el número máximo de terminales que pueden ser incluidos de tal forma de no causar ninguna interferencia mutua.

# Conclusiones

Repasando un poco, el concepto de Asignación de Capacidad de Canales se refiere a la distribución deficiente del ancho de banda del que se dispone entre múltiples usuarios o aplicaciones para optimizar el uso de recursos de red. Uno de los enfoques que destacamos es el criterio que propone L. Kleinrock, que sugiere que el costo es linealmente proporcional a la capacidad. Recorrimos los conceptos de lo que es el retardo, el tiempo de almacenamiento, el flujo de información, entre otros.

Por su parte, en Teoría de Colas, definimos este concepto como un marco matemático para analizar y gestionar las colas de espera en sistemas que poseen recursos limitados. Encontramos temas troncales como el Teorema de Little, el cual establece una relación entre la tasa de llegada de usuarios, el número medio de usuarios en el sistema y el tiempo medio que pasan en el sistema.

También introducimos el Sistema M/M/1, el que se trata de un modelo de cola simple donde las llegadas y los tiempos de servicio siguen una distribución exponencial. El análisis de este sistema permite calcular la tasa de llegadas, el tiempo medio de servicio, la ocupación del sistema, y el retardo medio, entre otros.

A su vez, discutimos cómo calcular y relacionar las prestaciones básicas de un sistema M/M/1, incluyendo la distribución del retardo y el tiempo total en el sistema.

Para concretar, la asignación de capacidad de canales y la teoría de colas son fundamentales para un diseño y gestión eficiente de redes de comunicación de datos. La primera asegura que los recursos se distribuyen adecuadamente para maximizar el rendimiento, mientras que la segunda proporciona herramientas analíticas para gestionar las colas de espera y optimizar el uso de los recursos.

# Bibliografía

Cátedra de Comunicación de Datos. (2024). “*Asignación de Capacidad de Canales”*. Universidad Tecnológica Nacional. Facultad Regional Rosario.

Cátedra de Comunicación de Datos. (2024). “*Teoría de Colas”*. Universidad Tecnológica Nacional. Facultad Regional Rosario.

De Giusti, M. R. (2006). Teoría de Colas.

Yáñez-Mingot, P. S., & Hernández Gutiérrez, J. A. (2018). Una introducción amable a la Teoría de Colas. *URL:* [*https://www.it.uc3m.es/pablo/teoria-colas/introduccion-teoriacolas.pdf*](https://www.it.uc3m.es/pablo/teoria-colas/introduccion-teoriacolas.pdf) *.(Visitado por última vez el: 28.08. 2021)*.

# Anexo: Autoevaluación con Preguntas y Respuestas

*1) En el sistema de Colas, ¿siempre se cuenta con un único servidor?*

No. Los sistemas de colas también pueden contar con m cantidad de servidores idénticos que pueden servir hasta n usuarios diferentes, esto se denomina Sistema Multiservidor.

*2) ¿Qué variables se estudian en una Cola?*

Se estudian:

* **Tiempo medio de estancia en el sistema (T):** es el tiempo que transcurre desde que una petición llega al sistema hasta que ha sido finalmente atendida por un recurso.
* **Tiempo medio de estancia en la cola (W):** es el tiempo que transcurre desde que una petición llega al sistema hasta que empieza a ser atendida por uno de los recursos.

*3) ¿Qué es un Sistema M/M/1?*

Se trata de un sistema en el que:

* el tiempo entre llegadas es exponencial, de media 1/λ,
* el tiempo de servicio también es exponencial, de media 1/μ,
* hay un único recurso para atender las peticiones,
* y la longitud de la cola no está limitada.

*4) ¿Y un sistema M/M/m?*

Similar al sistema M/M/1, se trata de un sistema con llegadas de Poisson y tiempos de servicio que siguen una variable aleatoria exponencial, pero en este caso hay m servidores idénticos en paralelo.

Si hay varios servidores disponibles, un usuario que llegue al sistema será atendido por uno de ellos, mientras que si todos están ocupados, el usuario tendrá que esperar en cola hasta que uno quede libre.

*5) ¿Cómo definimos el parámetro ρ?*

El parámetro ρ se define como el cociente entre la tasa de llegadas al sistema y la tasa máxima de salida que proporciona el servidor, y se puede interpretar como el tiempo medio de servicio entre el tiempo medio entre llegadas.

*6) ¿Qué enuncia el Teorema de Little?*

Se trata de uno de los resultados fundamentales de la teoría de colas, que establece una relación muy sencilla entre la tasa efectiva de entrada de usuarios en un sistema, el número medio de usuarios en dicho sistema, y el tiempo medio total que pasan en el mismo. En resumen se puede expresar de la siguiente manera:

![](data:image/png;base64...)

*7) ¿Qué es una fuente finita?*

Con fuentes nos referimos al conjunto de usuarios que son capaces de solicitar el servicio del sistema
Cuando una fuente es finita, la longitud de la cola estará determinada por el número de usuarios en el sistema, ya que estos son quienes afectan la frecuencia de arribo a ella.

*8) ¿Qué sucede en un sistema con cola finita?*

En los sistemas con cola finita, no sólo existe el rechazo de usuarios sino que también tenemos que estar pendientes de dos nuevas variables que dependen de la capacidad de la cola:

* **Probabilidad de bloqueo (PB):** probabilidad de que una determinada petición no pueda acceder al sistema, porque se encuentra lleno.
* **Tasa efectiva de tráfico cursado:** si la población realiza peticiones a una tasa , pero existe dicha probabilidad de bloqueo PB, entonces el tráfico que se cursa en dicho sistema no es el total del ofrecido, sino una fracción inferior.

*9) En un sistema que rechaza usuarios, ¿puedo aplicar el teorema de Little?*

Sí, pero hay que tener en cuenta un detalle. La variable λ utilizada en el teorema se refiere a la tasa media de usuarios que pasan por el sistema, y no a la tasa ofrecida al sistema. Por lo tanto hay que aplicar esta distinción en ese tipo de sistemas.

*10) Cuando hablamos del método de Kleinrock, ¿a qué se refiere con estrategia de asignación de capacidades de la raíz cuadrada?*

Este es un método en el cual la capacidad de cada enlace es proporcional a la raíz cuadrada del flujo de tráfico a través del enlace.