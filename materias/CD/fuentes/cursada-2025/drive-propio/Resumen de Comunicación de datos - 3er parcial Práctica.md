Resumen de **Comunicación de datos - 3er parcial Práctica**

**(Explicación de conceptos - Parcial Baró)**

# Conceptos

## Modulación

El concepto general de la **Modulación**, es que consiste en “adaptar” una señal mensaje, la que se quiere transmitir, al medio de transmisión.

Por otro lado, la **Modulación** consiste también en un traslado en frecuencia del mensaje ($f\_{m}$)a una frecuencia mucho mayor, la frecuencia de la señal portadora ($f\_{p}$), que siempre es de alta frecuencia comparándola con el mensaje ($f\_{m}<<f\_{p}$) ).

Modular significa modificar algún parámetro (*amplitud, frecuencia, periodo, …*)

Son necesarias dos señales:

* Mensaje (contiene la información) de **baja frecuencia**
* Portadora de **alta frecuencia**

Siempre en la señal modulada el Mensaje modula a la Portadora.

¿Para qué modulamos? Para poder adaptar el mensaje/señal al canal, nos permite transmitir mensajes a distancias mayores y evitar el ruido de baja frecuencia.

La portadora es la señal encargada de transmitir el mensaje, es decir las variaciones de alguna magnitud de la misma: Amplitud (de tensión o corriente), Frecuencia o Fase.

Entonces, la **Modulación** consiste en variarle (modularle) algún parámetro a la portadora, de acuerdo al mensaje que quiero transmitir. Estos parámetros a modificar en la portadora, serán: amplitud, frecuencia o fase. Uno por vez.

En nuestro caso, vamos a tener en cuenta dos casos:

* Modulación analógica: La portadora **es analógica**. No importa el mensaje
* Modulación digital: La portadora **es** **de pulsos**.

Todo el proceso de modulación y demodulación es realizado por el modem y el modem demodulador, respectivamente.

### AM (Amplitud modulada o Modulación de amplitud)

El parámetro que se altera es la amplitud. Es decir, cuando el mensaje crece, la portadora aumenta el valor; cuando el mensaje disminuye, la portadora también disminuye su amplitud.

**La amplitud de la portadora varía de acuerdo al mensaje.** La fase y la frecuencia permanecen constantes.

Se trabaja con una $f\_{p}=1000 KHz$

### FM (Frecuencia modulada o Modulación de Frecuencia)

Mantengo constantes la amplitud y la fase de la portadora y vario la frecuencia de la portadora. **De acuerdo a la amplitud del mensaje cambia la frecuencia de la portadora**.

Se trabaja con una $f\_{p}=100 KHz$

### PM (Modulación de Fase)

Es muy difícil hacer el dibujo de la Modulación de Fase, porque lo que se hace es variar un ángulo, entonces se vería como si fuese modulación de frecuencia, porque la fase y la frecuencia afectan por igual el argumento de la onda senoidal de la portadora.

### Señal/Mensaje digital - Portadora analógica

Se utiliza para transmitir información de computadora (señal digital) a través de la línea telefónica como una señal analógica.

Procedimiento: se convierte la señal digital en analógica a través del MODEM, y viceversa en el extremo receptor.

Los tres tipos de Modulación que existe, son:

* **ASK (Amplitude Shift Keying o Manipulación por desplazamiento de la Amplitud)**: El mensaje digital le pone un límite a la amplitud a la portadora de tal manera que cuando emito un 0, la portadora no transmite y cuando emito un 1, la portadora emite.

![](data:image/png;base64...)

* **FSK (Frequency Shift Keying o Manipulación por desplazamiento de la frecuencia)**: Se utilizan dos portadoras con diferentes frecuencias para transmitir el mensaje. Al “1” le asigno una frecuencia portadora y al “0” le asigno otra frecuencia portadora.

![](data:image/png;base64...)

* **PSK (Phase Shift Keying o Manipulación por desplazamiento de fase)**: vengo con una determinada fase para el “1” binario, y se producirá un cambio de fase cuando se cambia del “1” al “0”, o del “0” al “1” (ver esquema anterior).

![](data:image/png;base64...)

### Demodulación

Para demodulación se utiliza ASK. Pero no tengo anotado mucho más

### Modulación digital

#### Multiplexación por división de tiempo (TDM)

Previo a todo, se realiza el proceso denominado **Multiplexación por división de tiempo**. Este proceso nos permite enviar distintos mensajes por un mismo canal.

![](data:image/png;base64...)

Se transmite una muestra de A en un tiempo t1 y se recibe en A’. El tiempo en que A no se está transmitiendo, se usa el canal para transmitir la muestra de otro mensaje en tiempo. El conjunto de una muestra de cada mensaje se denomina **TRAMA** (dura Ts).

![](data:image/png;base64...)

#### Muestreo

El problema acá es que nuestra señal $x(t)$ es infinita y no podemos transmitirla tal cual es.

Se realiza un proceso llamado **Muestreo**, el proceso consiste en combinar la señal del mensaje con una señal de *tren de pulsos unitarios*. Al combinar ambas señales vamos a obtener una serie de **muestras** de la señal del mensaje.

$x(t): analógica (señal a muestrear)$

$s(t):tren de pulsos unitarios$

Si combinamos ambas señales:

![](data:image/png;base64...)

El muestreo en este caso, se realiza a través de la técnica de **PAM** (**Modulación por amplitud de pulso**) donde se varían las amplitudes de los pulsos de acuerdo al mensaje.

*Alternativa a esto*:

* **PDM o PWM** varía sólo frecuencia, vario el ancho del pulso de acuerdo al mensaje.
* **PPM** varía sólo la posición del pulso de acuerdo al mensaje.

![](data:image/png;base64...)

Luego del muestreo nos queda una sucesión de muestras de diferentes valores cada una. de una señal analógica pueden ser tomadas muestras cuyas amplitudes pueden alcanzar infinitos valores, pero solo es posible codificar un número finito de valores de la amplitud de las muestras.

#### Cuantificación

Para hacer que estas muestras tengan valores coherentes o similares con los que podamos trabajar se realiza el proceso de **Cuantificación**. Este proceso consiste en definir una serie finita de valores posibles de ser codificados y redondear el valor de la amplitud de las muestras al valor más cercano de los definidos.

En resumen, el método de **Cuantificación** nos permite pasar de un conjunto de valores infinitos a un conjunto de valores finitos.

| Ejemplo:  Dada una señal, cuyo intervalo de variación de amplitudes [-4.5; 4.5] se adopta como valores a codificar a:-4.5; -3; -1.5; 0; 1.5; 3; 4.5, estos calores se preestablecen y se denominan **NIVELES CUÁNTICOS** (tienen asociados un intervalo) si la muestra cae dentro de ese intervalo, el valor es redondeado a ese nivel, este intervalo se llama **CUANTO** |
| --- |

#### Codificación

Por último, se realiza la **codificación** que consiste en codificar los valores de cada muestra en los bits que tengamos disponibles. Este último proceso de codificación se denomina **PCM** o **Modulación por codificación de pulsos**. Un resumen de los pasos entonces sería:

![](data:image/png;base64...)

### Límite entre dos muestras

¿Si se analizan 2 o más muestras como se que corresponde a un mensaje o a otro?

Desde el punto de vista temporal no tengo una justificación, la única forma de saberlo es a través del Análisis Frecuencial.

¿Qué forma tiene el mensaje original? ¿Cuál es la correcta? ¿Tengo garantías de recuperar el mensaje original?

Para esto trabajamos con el espectro frecuencial cuando hacemos por ejemplo la Modulación PAM (+ sencilla), haremos un simple producto.

![](data:image/png;base64...)

![](data:image/png;base64...)

Estas muestras en realidad no son un pedacito aislado del mensaje, sino que está repetido infinitas veces, si para recuperar mi señal necesito el espectro, lo tengo infinitas veces.

Entre una muestra y otra muestra quiero que el tiempo de muestreo sea lo más grande posible para que me pueda entrar mayor cantidad de mensajes (muchas muestras).

![](data:image/png;base64...)

Donde:

* $N:$ cantidad de mensajes muestrados o transportados.
* $Ts:$ tiempo o periodo de muestreo (tiempo desde que se toma una muestra hasta que volvamos a tomar otra del mismo mensaje)
* $fs:$ frecuencia de muestreo

Sin embargo, al bajar la frecuencia me acerco al origen.

![](data:image/png;base64...)

Lo que se hace es disminuir la frecuencia de muestreo $fs$ lo máximo posible para poder mandar más cantidad de señales en el mismo canal.

Sin embargo, llegamos a un punto en que si sigo bajando $fs$ se me van a superponer las frecuencias.

![](data:image/png;base64...)

¿Entonces cuál es el límite?

$fs-w \geq w⇒fs\geq 2w, siendo w=f\_{max}-f\_{min}≃f\_{max}$

Por Tasa de Nyquist o Teorema de Muestreo; la frecuencia mínima de muestreo fs siempre tiene que ser mayor o igual que las 2 frecuencias máximas del mensaje.

Condición para que pueda recuperar el mensaje:

$fs\geq 2 f\_{max\_{msg}}$

# Ejercicios de Baró

## Primer ejercicio

Tenemos que transmitir treinta señales de voz y dos señales de control (una de señalización y otra de sincronización) por trama. Teniendo en cuenta que la frecuencia máxima de una señal de voz es de $4 KHz$. Calcular la velocidad a la que se transportará el mensaje.

### Resolución

Aplicamos el Teorema de Nyquist para obtener la mínima frecuencia de muestreo con la que vamos a trabajar sabiendo que $W=4 KHz$.

$fs=2W=8 KHz$

Ahora, con la frecuencia de muestreo podemos determinar el tiempo de muestreo (o **periodo de muestreo**)

$Ts=\frac{1}{fs}=\frac{1}{8 KHz}=0.125 ms=125 μs$

Como necesidad del ejercicio (si bien no lo dice), hay que plantear las gráficas del Muestreo, Cuantificación y Codificación (con datos arbitrarios). Algo a tener en cuenta es que si bien no lo menciona, por práctica común se codifica con 8 bits, a menos que se especifique de otra forma en el enunciado

![](data:image/png;base64...)

Ahora planteamos que:

$Tiempo de muestreo=32⋅Tiempo de cada muestra$

$Ts=32⋅Tm$

$Tm=\frac{Ts}{32}=\frac{125 μs}{32}=3,9 μs$

Pero, el tiempo de cada muestra puede ser pensado como 8 veces el tiempo de un bit($τ$), por lo tanto:

$Tm=8⋅τ$

$τ=\frac{Tm}{8 bits}=\frac{3,9 μs}{8 bits}=0,4875 μs=487,5 \frac{ns}{bit}$

A partir de haber despejado $τ$ podemos calcular la velocidad de transmisión ($r$):

$r=\frac{1}{τ}=\frac{1}{487,5 ns}=\frac{1}{0,4875 μs}=2,05 Mbps$

## Segundo ejercicio

Tenemos que transmitir veinticuatro señales de voz y se agrega un bit de sincronización **por canal** y un bit de señalización **por trama**. Teniendo en cuenta que la frecuencia máxima de una señal de voz es de $4 KHz$ y se codifica con 7 bits por canal. Calcular la velocidad a la que se transportará el mensaje.

### Resolución

Nuevamente trabajamos con una frecuencia máxima de $W=4 KHz$ así que por Teorema de Nyquist $⇒fs=8 KHz$

Ahora, con la frecuencia de muestreo podemos determinar el tiempo de muestreo (o **periodo de muestreo**)

$Ts=\frac{1}{fs}=\frac{1}{8 KHz}=0.125 ms=125 μs$

Ahora realizamos los gráficos:

![](data:image/png;base64...)

*Nota: El Ts de PCM* ***no*** *es el mismo que el Ts del TDM pues en PCM se agregan los bits de sincronización y señalización. Sin embargo la diferencia entre ambos valores de tiempo de muestreo es despreciable.*

Luego, podemos calcular el valor de la duración de un bit teniendo en cuenta los bits de control.

$Ts=24⋅Tm=[(24⋅7)+(24⋅1)+1]⋅τ$

$125 μs=193⋅τ$

$τ=\frac{125 μs}{193 bits}=0,647 \frac{μs}{bit}$

Y luego, podemos calcular la velocidad de transmisión ($r$):

$∴ r=\frac{1}{τ}=1,544 Mbps$

#

# Parcial random de Baró

## Ejercicio 1 - Definiciones

* **Ancho de banda:** Es la diferencia entre la max y min frecuencia que puede pasar por un canal de comunicaciones. Se mide en Hz, y se calcula con la diferencia entre Fmax y Fmin
* **Señal portadora** (describir su utilidad): Es una señal de alta frecuencia que sirve para transportar el mensaje de origen a destino. Podemos decir que su funcionalidad es la de transmitir información mediante una modificación en la misma generada por una señal de entrada
* **Muestreo:** Es un proceso que consiste en combinar la señal del mensaje con una señal de tren de pulsos unitarios. Al realizar este proceso obtenemos una serie de muestras de la señal del mensaje.
* **Cuantificación:** Proceso que consiste en definir una serie finita de valores posibles de ser codificados y redondear el valor de la amplitud de las muestras al valor más cercano de los definidos. Esto nos permite pasar de un conjunto de valores infinitos a un conjunto de valores finitos.
* **Codificación:** Se trata del último proceso que realizamos en la Modulación donde codificamos los valores de cada muestra en los bits que tengamos disponibles.

## Ejercicio 2

Se desea transmitir una trama digital con:

* 25 muestras de Ix
* 2 muestras de control

Se sabe que la frecuencia máxima de las señales es 3000Hz y se codifica a cada muestra con 7 bits.

Calcular ancho de banda e indicar técnicas utilizadas y gráficos.

Por el teorema de Nyquist podemos obtener la frecuencia mínima de muestreo:

$fs = 2f\_{max}= 6000 Hz = 6 kHz$

Luego la tasa de muestreo:

$Ts =\frac{1}{fs} =\frac{1}{6 kHz}=0,166 mseg =166 μseg $

Con esto podemos calcular la tasa de una sola muestra, teniendo en cuenta las 2 muestras de control.

$Tm = \frac{Ts}{N}= \frac{166 μseg}{27 muestras}=6,15 \frac{μseg}{muestra} $

Usamos esto para calcular la duración de 1 bit, recordar que este ejercicio nos pedía codificar las muestras a 7 bits.

$τ = \frac{Tm}{n}=\frac{6,15}{7}=0,88 μseg$

Por último, para calcular el Ancho de Banda podemos aplicar la siguiente fórmula:

$Bw = \frac{1}{τ}=\frac{1}{0,88 μseg}=1,136 mHz$

Tener en cuenta que también hay otra fórmula para calcular el Ancho de Banda con la que podríamos haber ahorrado varios pasos:

$Bw = N⋅n⋅2 fmax = 27⋅ 7⋅6 kHz = 1134 kHz = 1,134 mHz$

![](data:image/png;base64...)

Obviamente utilizamos TDM para multiplexación y PCM para la codificación

# Otro parcial de Baró

1. Defina **claramente** los siguientes conceptos:
   1. Tasa de Nyquist

La tasa de Nyquist es un teorema que nos permite determinar la frecuencia de muestreo mínima evitando que se solape la información y permitiendo recuperar el mensaje original. Este teorema enuncia que la frecuencia de muestreo es por lo menos 2 veces la máxima frecuencia del mensaje.

$fs\geq 2W$

* 1. Modulación P.D.M.

La modulación por P.D.M. es una técnica que se puede utilizar en el muestreo, en esta técnica se modula el ancho de pulso de acuerdo a la amplitud del mensaje.

![](data:image/png;base64...)

* 1. Armónico de la Serie de Fourier

Un armónico en la serie de Fourier es una onda sinusoidal que tiene una frecuencia entera múltiplo de la frecuencia fundamental de una señal periódica. En otras palabras, cuando una señal periódica se descompone en sus componentes sinusoidales mediante la serie de Fourier, cada componente sinusoidal individual se llama armónico.

1. Se desea transmitir una **trama digital**, que consta de 38 muestras de información + 2 muestras de control (sincronización y señalización). Por otro lado, se sabe que las señales intervinientes tienen una frecuencia máxima de $5 KHz$, y que se codifica cada muestra con 8 dígitos. Calcular **la velocidad de transmisión** ($r$), realizando todos los **gráficos** correspondientes e indicando todas las **técnicas empleadas** en el proceso de transmisión.

![](data:image/png;base64...)

Por teorema de Nyquist sabemos que la frecuencia de muestreo es, por lo menos dos veces la frecuencia máxima de la señal interviniente. Por ende $W=5 KHz ⇒fs = 10 KHz$

Ahora, con la frecuencia de muestreo despejo el tiempo de muestreo o periodo de muestreo.

$Ts=\frac{1}{fs}=\frac{1}{10 KHz}=0,1 μs$

![](data:image/png;base64...)

A partir de esto podemos determinar el valor de duración de un bit ($τ$):

$Ts=40⋅Tm=40⋅8⋅τ$

$τ=\frac{Ts}{40⋅8 bits}=\frac{0,1 μs}{40⋅8 bits}=0,3125 \frac{ns}{bit}$

$r=\frac{1}{τ}=\frac{1}{0,3125}=3,2 Gbps$