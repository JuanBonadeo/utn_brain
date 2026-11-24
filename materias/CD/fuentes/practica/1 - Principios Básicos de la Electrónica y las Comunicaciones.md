***UNIVERSIDAD TECNOLÓGICA NACIONAL***

***FACULTAD REGIONAL ROSARIO***

**Principios básicos de la Electrónica y las Comunicaciones**

**Año 2025**

Contenido

[**Principios básicos de la electrónica** 3](#_Toc39244751)

[Polaridad 3](#_Toc39244752)

[El Volt 3](#_Toc39244753)

[El Ampere 3](#_Toc39244754)

[El Ohm 3](#_Toc39244755)

[Ley de Ohm 4](#_Toc39244756)

[Corriente Continua (C.C.) 4](#_Toc39244757)

[Corriente Alternada (C.A.) 4](#_Toc39244758)

[Materiales básicos en electrónica 8](#_Toc39244759)

[**Introducción a las comunicaciones** 9](#_Toc39244760)

[Niveles 9](#_Toc39244761)

[Ganancias y Atenuación 10](#_Toc39244762)

[El decibel relativo (db) 11](#_Toc39244763)

[Respuesta en frecuencia 12](#_Toc39244764)

[Rango dinámico 13](#_Toc39244765)

[Relación señal / ruido 13](#_Toc39244766)

[**Sistema de Telecomunicaciones** 14](#_Toc39244767)

[Tipos de sistemas de comunicaciones 15](#_Toc39244768)

[Técnicas de análisis y síntesis de sistemas de comunicación 17](#_Toc39244769)

[Características generales de los canales de comunicación 17](#_Toc39244770)

[Ruido como elemento limitante 18](#_Toc39244771)

[Distintas técnicas de modulación 20](#_Toc39244772)

[Algunos conceptos fundamentales 21](#_Toc39244773)

[**Detección y corrección de errores** 25](#_Toc39244774)

# **Principios básicos de la electrónica**

## **Polaridad**

El estudio de la electricidad estática llevó a la conclusión que dos cuerpos con distinta carga eléctrica proveen la fuerza requerida para producir el movimiento de electrones en un conductor que une estos dos cuerpos. Si conocemos de antemano cual de esos dos cuerpos lleva carga positiva o negativa, es posible predecir la dirección de del flujo de electrones. Esta cualidad direccional es conocida como “polaridad”.

Cuando existe una diferencia de carga eléctrica entre dos puntos, se dice que uno de ellos tiene polaridad positiva o negativa con respecto al otro. Los artefactos productores de energía eléctrica tienen sus terminales marcados (+) o (-) para indicar la polaridad en los terminales respectivos. Es fundamental conocer la polaridad para realizar las conexiones en forma correcta y lograr así un adecuado funcionamiento del equipo.

## **El Volt**

La diferencia de carga eléctrica entre dos puntos u objetos cargados eléctricamente posee la facultad de producir trabajo eléctrico originando un movimiento de electrones a través de un conductor conectado entre ambos.

La energía potencial que existe entre los cuerpos que tienen cargas eléctricas de distinto signo se denominan comúnmente “diferencia de potencial” (d.d.p.) o simplemente “potencial entre dos puntos”.

Este potencial eléctrico puede ser tanto positivo como negativo con respecto a un cuerpo considerado neutro (la tierra).

La unidad que utilizamos para medir la diferencia de potencial o potencial eléctrico es el “volt” o “voltio”.

El concepto fuerza electromotriz (f.e.m.) expresa la fuerza establecida entre dos cuerpos cargados eléctricamente. También se la puede denominar tensión eléctrica y se mide en voltios.

Existen muchos métodos para producir tensión: fricción, energía calorífica, energía lumínica, energía química, energía mecánica y energía atómica entre otros.

## **El Ampere**

Se define la corriente eléctrica como el flujo de electrones a través de un material o medio conductor, desde un punto de potencial negativo hacia otro de potencial positivo.

La cantidad de flujo de electrones se mide en “ampere”.

## **El Ohm**

Es el término que se aplica a la unidad de resistencia eléctrica, que ofrecen los diversos materiales al paso de una corriente eléctrica.

Se dice que un material tiene una resistencia de “un ohm”, si al aplicar una tensión de un volt circula por el mismo una corriente de un ampere. El uso del ohm puede ser aplicado en términos generales tanto a conductores como a aisladores. Estos últimos tienen un valor óhmico (resistencia eléctrica) muchas veces mayor que el de los conductores.

## **Ley de Ohm**

Una corriente (I) circulando por una resistencia (R), genera entre sus extremos una tensión igual al producto de la R por la I.

![Forma, Flecha  El contenido generado por IA puede ser incorrecto.](data:image/png;base64...)Tapando la incógnita que queremos averiguar, obtendremos la ecuación

$$I=\frac{V}{R} ; V=R∙I ; R=\frac{V}{I}$$

## **Corriente Continua (C.C.)**

La corriente eléctrica ha sido descripta como el “flujo direccional de electrones”. La dirección de este flujo está determinada por la polaridad de la fuente de tensión. Por ejemplo: en una batería, la polaridad de los terminales es fija, por lo tanto, la corriente eléctrica fluye en una sola dirección cuando la batería está conectada a un aparato eléctrico. Este tipo de corriente se denomina “corriente continua” (C.C.).

## **Corriente Alternada (C.A.)**

La acción de una corriente alternada puede comprenderse fácilmente si se observa el péndulo de un reloj: primer oscila en una dirección hasta cierta altura, luego vuelve por el mismo camino en dirección opuesta hasta una altura equivalente pasando por una posición central.

Este movimiento del péndulo es muy similar al de la corriente alternada: primero fluye en una dirección y luego en dirección opuesta, pasando por la posición central que corresponde al valor nulo de amplitud (ver gráficos).

![](data:image/png;base64...)

**Valores típicos de las magnitudes de C.A.**

**Valor instantáneo**

En ciertas ocasiones, se necesita conocer el valor en un cierto instante de la tensión o de la corriente generada para un determinado ángulo α o wt. Esto es:

![](data:image/png;base64...)

Donde Emax e Imax son los valores máximos de los vectores tensión y corriente respectivamente.

Definición: valor instantáneo es el valor que toma la corriente punto a punto o instante a instante

**Valor máximo**

También denominado valor de pico o valor de cresta (Vmax = Vp = Vc o V), es el máximo valor instantáneo producido en un ciclo. Puede ser positivo o negativo, siendo igual en ambos casos la amplitud del valor de pico, como se observa en la siguiente figura.

![](data:image/jpeg;base64...)

**Valor de pico a pico**

El valor de pico a pico (Vpap = V2p) se mide desde el máximo valor positivo de pico hasta el máximo valor negativo de la sinusoide (ver gráfico anterior)

**Valor Medio**

Es otro de los valores que se emplean en corriente alterna, siendo el valor medio de una corriente sinusoidal igual a cero, puesto que sus dos semiciclos son iguales y opuestos en polaridad (signo). Sin embargo, el termino valor medio se aplica a un semiciclo de la onda.

El valor medio de una sinusoide es el promedio de todos los valores instantáneos de un semiciclo.

![](data:image/png;base64...)

El valor medio exacto de la tensión o corriente es igual al valor máximo multiplicado por 0.636, una de las maneras de obtener este valor como la superficie de un semiciclo dividido por la base (π).

**Valor eficaz**

El valor eficaz (Vef o R.M.S.), es el valor de C.A. equivalente a uno de C.C que disipa la misma potencia o produce el mismo trabajo

Para poder obtener el valor eficaz, se realiza la raíz cuadrada de la suma de los valores instantáneos elevados al cuadrado, dividido por n (número de valores). A este valor se lo denomina valor de la raíz cuadrada del promedio cuadrático. Para poder obtenerlo:

![](data:image/jpeg;base64...)

Y si hablamos del valor eficaz de una corriente alterna senoidal, se obtiene como el Vmax por 0,707, como vemos en la siguiente grafica de conversión:

![](data:image/jpeg;base64...)

Tabla de conversión para tensiones o corrientes senoidales

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Eficaz (rms)** | **Medio** | **Pico** | **Pico a Pico** |
| **Eficaz (rms)** | - | 0,901 | 1,414 | 2,828 |
| **Medio** | 1,110 | - | 1,570 | 3,714 |
| **Pico** | 0,707 | 0,637 | - | 2,00 |
| **Pico a Pico** | 0,354 | 0,318 | 0,500 | - |

Para obtener alguno de los valores de la primera fila, se multiplica el valor correspondiente de la primera columna (dato) por el valor numérico intersección de tabla.

Ejemplo: Valor eficaz = valor pico x 0,707

Para obtener alguno de los valores de la primera columna, se divide el valor correspondiente de la primera fila por el valor numérico de intersección de la tabla:

Valor pico a pico = valor pico / 0,500 = valor pico x 2

**Prefijos usados para unidades eléctricas o informáticas**

|  |  |  |  |
| --- | --- | --- | --- |
| **Prefijo** | **Magnitud** | **Potencia equivalente de 10** | **Unidad** |
| Yotta (Y) | 1.000.000.000.000.000.000.000.000 | 10 24 | Yottabyte |
| Zetta (Z) | 1.000.000.000.000.000.000.000 | 10 21 | Zettabyte |
| Exa (E) | 1.000.000.000.000.000.000 | 10 18 | Exabyte, Exahercios |
| Peta (P) | 1.000.000.000.000.000 | 10 15 | Petabyte |
| Tera (T) | 1.000.000.000.000 | 10 12 | Terahercio, Terabit |
| Giga (G) | 1.000.000.000 | 10 9 | Gigabyte, Gigawatt |
| Mega (M) | 1.000.000 | 10 6 | Megohm, Megaciclo |
| Kilo (K) | 1.000 | 10 3 | Kilociclo, Kilovolt, Kilowatt |
| Mili (m) | 1/1.000 | 10 -3 | milivolt, miliampere, milihenry |
| Micro (µ) | 1/1.000.000 | 10 -6 | Microvolt, microfaradio |
| Nano (n) | 1/1.000.000.000 | 10 -9 | Nanohenry, nanoampere |
| Pico (p) | 1/1.000.000.000.000 | 10 -12 | Picofaradio |
| Femto (f) | 1/1.000.000.000.000.000 | 10 -15 | Femtoamperio, femtosegundo |
| Atto (a) | 1/1.000.000.000.000.000.000 | 10 -18 | Attosegundo, attohercio |
| Zepto (z) | 1/1.000.000.000.000.000.000.000 | 10 -21 | Zeptosegundo |
| Yocto (y) | 1/1.000.000.000.000.000.000.000.000 | 10 -24 | Yoctohercio, yoctosegundo |

**Frecuencia**

Se denomina “frecuencia” de la corriente alternada al número de veces que cambia la polaridad de la corriente por segundo

La frecuencia de la red domiciliaria es de 60 ciclos por segundos (un ciclo es el tiempo requerido por la corriente para completar el flujo en ambas direcciones). Las frecuencias comprendidas entre 20ciclos/seg y 20.000 ciclos/seg se llaman audiofrecuencias y pueden ser oídas por el oído humano si se aplican aparatos adecuados. Las frecuencias superiores a 20.000ciclos/seg se denominan radiofrecuencias y no pueden escucharse.

La unidad de frecuencia es el Hertz (Hz). Un Hertz equivale a un ciclo/seg.

**Periodo**

Es el tiempo que tarda en completarse un ciclo. El periodo es la inversa de la frecuencia, y se mide en segundos por ser una medida temporal.

![](data:image/jpeg;base64...)

![](data:image/png;base64...)

## **Componentes básicos en electrónica**

Existen tres componentes básicos que debemos conocer. Estos son: bobina, resistencia y capacitor.

**Bobina:** es un arrollamiento que genera un campo magnético proporcional a la corriente que lo circula y a las características físicas del mismo. Su resistencia eléctrica se denomina reactancia inductiva (XL). En corriente continua actúa como un conductor (cable), siendo XL = 0. En corriente alterna:

![](data:image/jpeg;base64...)

Siendo el valor numérico de la inductancia en Henry (unidad utilizada para bobinas).

**Resistencia:** como su nombre lo indica, es un componente que se opone al paso de la corriente eléctrica generando una caída de tensión sobre la misma

![](data:image/jpeg;base64...)

**Capacitor o Condensador:** el mismo tiene la propiedad de oponerse a cambios de tensión. Su resistencia se denomina como XC (reactancia capacitiva).

![](data:image/jpeg;base64...)

C: valor numérico del capacitor en submúltiplos de faradio (unidad utilizada para capacitores).

# **Introducción a las comunicaciones**

El gran desarrollo tecnológico de los últimos tiempos ha permitido al hombre ampliar su posibilidad de comunicación, es decir su posibilidad de intercambiar información cada vez a mayores distancias, con mayor rapidez y simplicidad. Además, nos permite lograr la comunicación entre maquinas o entre hombres y maquinas, para servir de soporte técnico a las relaciones humanas.

Los sistemas de telecomunicaciones (tele: a gran distancia) nos permiten intercambiar información en forma de sonidos, imágenes, textos, etc.; aprovechando los medios de captación y expresión que posee el hombre (oído, voz, vista y escritura) y a través de sistemas tales como:

1. Teléfono: permite conversación entre dos o más personas en forma simultanea
2. Radio: permite la transmisión de información y entretenimiento en forma masiva
3. Televisión: permite la transmisión de imágenes en movimiento y sonidos para información y entretenimientos, también en forma masiva. Además, se utiliza en sistemas de control, seguridad, etc.
4. Facsímil: permite la transmisión de imágenes estáticas tales como fotos, planos, cartas, etc.
5. Teletipo: es un sistema netamente informático, en el sentido que permite solamente intercambio de información, la cual se manifiesta a través del medio escrito.
6. Telecontrol: sistema de enlace hombre-maquina, que permite controlar a distancia un proceso
7. Telemedida: está relacionado con el anterior, pero en este caso es el hombre el que recibe la información del estado de un proceso o de una máquina.
8. Teleproceso: este sistema permite una “conversación” entre un hombre y una maquina (computadora), es decir, permite que una maquina ubicada a distancia procese la información que se le envía y devuelva los resultados pedidos

##

## **Niveles**

Un sistema de telecomunicaciones trabaja con señales eléctricas que sufren distintas modificaciones durante su procesamiento y traslado a través del emisor, el canal y finalmente el receptor. Uno de los parámetros más importantes es el nivel o amplitud de la señal, que se incrementará o reducirá según la etapa que se analiza del sistema, presente ganancia o atenuación respectivamente.

Definición: el nivel de la señal se expresa normalmente en las unidades fundamentales de tensión, corriente o potencia; pero también es posible expresarlo como una relación entre la magnitud eléctrica que representa el nivel de la señal y una magnitud eléctrica de igual naturaleza que se toma de referencia. Por ejemplo, supongamos tener un sistema al cual se entrega una potencia de 1watt y el mismo entrega a la carga una potencia de 10watts.

![](data:image/jpeg;base64...)

Podemos decir entonces que el nivel de salida es de 10W, o que el nivel de salida es de 10 unidades si tomamos 1W como potencia de referencia; y también podemos decir que el nivel de salida es 10 veces o 10 unidades respecto del nivel de entrada (tomando a este como referencia)

Esta nueva forma de expresión es utilizada en Comunicaciones, y vemos que consiste en expresar un nivel como una relación entre dos magnitudes eléctricas de igual naturaleza. Pero como los niveles de señal que intervienen en sistemas de telecomunicaciones tienen un rango muy amplio, estas relaciones deben expresarse en forma logarítmica. Esta forma de expresión permite comprimir los rangos de señales y permiten obtener fácilmente las atenuaciones o ganancias totales por suma de las parciales:

GT = G1 . G2 . G3

Log GT = log G1 + log G2 + log G3

En algunos casos también se justifica el uso de unidades logarítmicas, por el hecho que estas unidades nacieron con la telefonía y por lo tanto está asociada a la respuesta del oído humano, que es esencialmente logarítmica.

La magnitud eléctrica tomada como referencia puede ser una tensión, una corriente o una potencia fija utilizada como patrón para todas las mediciones en cuyo caso estamos en presencia de un **“nivel absoluto”**. Si en cambio la magnitud de referencia es variable, es decir se puede elegir arbitrariamente, estamos en presencia de un **“nivel relativo”**

Resumiendo, tendremos un nivel absoluto si establecemos la amplitud de la señal en un único punto de un sistema y relacionamos a esta con la de referencia; en cambio tendremos un nivel relativo, si sobre un sistema medimos dos señales y a estas las relacionamos entre sí.

## **Ganancia y Atenuación**

Los niveles relativos son sumamente utilizados en comunicaciones para relacionar entre si las magnitudes de entrada y salida de un sistema, a fin de conocer la acción del mismo sobre la amplitud de la señal.

Damos la denominación genérica de ganancia a la relación entre la magnitud de salida de un sistema y la correspondiente magnitud de entrada que ocasiona dicha salida:

Gp = Po / Pi Ganancia de potencia

Gv = Vo / Vi Ganancia de tensión

Gi = Io / Ii Ganancia de corriente

Llamamos atenuación a la relación entre la magnitud de entrada de un sistema y la salida que ella provoca; es decir la inversa de la ganancia:

A = 1/G

La forma normal de expresar la transferencia de un sistema es a través de la ganancia, pero en caso de sistemas pasivos tales como cables o redes resistivas en los cuales siempre existe atenuación, se utiliza a esta última como expresión normal de la transferencia de un sistema.

## **El decibel relativo (db)**

El db es la décima parte de un BELL, y es la unidad por excelencia utilizada para expresar niveles. El BELL era unidad utilizada antiguamente y lleva este nombre en honor del inventor del teléfono Graham Bell.

En comunicaciones la magnitud eléctrica más utilizada es la potencia, ya que ella expresa totalmente la acción de un sistema sobre las señales que se manejan, a diferencia de la tensión o la corriente que siempre dependen de los parámetros del circuito en cuestión.

Para el estudio de la atenuación en líneas telefónicas se comenzó a buscar una unidad de atenuación de potencia que permitiese la comparación entre distintos tipos de líneas, llegándose así a obtener la definición de U.T. (una Unidad de Transmisión), la cual representa una atenuación de 10 veces, Pi / Po = 10, medida sobre una línea patrón de 10millas de cable telefónico común a una frecuencia de 886Hz.

Vemos que, si duplicamos el largo del cable, la atenuación para 20millas será

AT = A10millas . A10millas = ( A10millas)2 , y así sucesivamente

Por lo tanto, podemos expresar en forma genérica la atenuación como:

A = Pi / Po = 10n/10 , donde n: n° de millas

Si expresamos esta relación como un nivel relativo de potencia en forma logarítmica, nos queda:

Log Pi / Po = n/10 = X BELL

Diremos entonces que la atenuación en BELL es el logaritmo de la relación Pi / Po

Si multiplicamos por 10 a esta relación, obtengo la atenuación expresada en db:

X dB = 10 log Pi / Po

Si queremos determinar la potencia mediante una medición de tensión o corriente, tendremos que conocer también la impedancia Z (resistencia eléctrica) sobre la cual realizamos esa medición:

![](data:image/jpeg;base64...)

Vemos entonces que si la Z sobre la cual se realiza esta determinación es constante (Z1 = Z2), se puede medir directamente la atenuación o ganancia en dB, a través de una relación de tensión o de corriente. Esto es:

X db = 20 . log E1 / E2 ó X db = 20 . log I1 / I2

## **Respuesta en frecuencia**

Otro parámetro determinante en un sistema de comunicaciones es la respuesta en frecuencia de dicho sistema, que viene especificada por el margen de fase en el cual este responde correctamente a las señales de entrada. Ya que es evidente que ningún elemento puede reproducir por igual a todas las frecuencias, provocando variaciones en la amplitud y en la fase de la señal entrante, deben especificarse los limites dentro de los cuales pueden trabajar. Para ello se definen las frecuencias inferiores y superiores de corte, como aquellas en las cuales la potencia de la señal se reduce a la mitad de su valor máximo, es decir, son aquellas frecuencias en las cuales la gráfica de amplitud versus frecuencia cae en 3db.

![](data:image/jpeg;base64...)

Al especificar estas dos frecuencias se está dando la “banda pasante” del sistema, que define totalmente la respuesta en frecuencia del mismo. Pero como en muchos casos es posible desplazar en el espectro de frecuencias a f1 y f2 sin alterar el contenido entre ambas, es también muy útil la especificación del “ancho de banda” que representa el “tamaño” de la porción del espectro de frecuencias que se puede reproducir:

AB = f2 - f1

Tabla descriptiva de niveles auditivos

|  |  |  |
| --- | --- | --- |
| **Descripción** | **Nivel (db)** | **Relación de magnitud** |
| Despegue de un reactor | 150 | 1015 |
| Umbral del dolor (ej auto F1) | 130 | 1013 |
| Concierto de rock | 120 | 1012 |
| Martillo neumático | 110 | 1011 |
| Ambiente industrial | 100 | 1010 |
| Tráfico intenso (camiones) | 90 | 109 |
| Tráfico denso | 70 | 107 |
| Conversación normal | 50 | 100.000 |
| Interior de casa en ciudad | 40 | 10.000 |
| Estudio de grabación | 20 | 100 |
| Umbral de audición | 0 | 1 |

**Consideraciones adicionales:** el oído no es capaz de distinguir diferencias inferiores a 3db. La intensidad de un sonido decrece aproximadamente en 6db cada vez que se doble la distancia.

![](data:image/png;base64...)

## **Rango dinámico**

Diferencia entre el nivel máximo que el dispositivo puede emitir y el nivel de ruido existente cuando no hay señal (el ruido de fondo). Cuanto mayor sea esta diferencia, más “limpio” será el sonido del dispositivo electrónico.

En una cadena de varios dispositivos de audio (emisor, amplificador, parlante, etc.) el valor real, es decir el mayor rango dinámico que se puede apreciar, corresponde al del dispositivo con peores características. En aparatos de calidad, el rango dinámico está en el intervalo [80, 95]db

**Discos compactos:** el oído humano capta hasta 20Khz => Fs ≥ 40Khz -> Fs = 44.100hz

Rango dinámico (db) = 10 log 10 [ (amp max)2 / (amp min)2 ]

Suponiendo amp min = 1 y amp max = 2(n° de bits)

En un sistema de conversión de 8 bits: rango dinámico ≈ 48db

En un sistema de conversión de 16 bits: rango dinámico = 10 log (216)2 / 12 = 96,32db

96,32db < 130db (umbral del dolor) -> con 32bits te dolería

Por lo tanto, el estándar = 96db (sistema digital)

## **Relación señal / ruido**

Una relación señal / ruido (SNR del inglés Signal to Noise Ratio) compara un nivel de potencia de la señal con un nivel de potencia de ruido. Se expresa con mayor frecuencia como una medida en decibelios (db). Los números más altos significan mejor especificación, ya que hay mayor información útil en la señal que datos no deseados.

En conclusión, diremos que la relación señal / ruido es la relación entre el nivel de la señal que corresponde a la información que nos interesa del sistema bajo análisis y el ruido consecuencia de todas aquellas fuentes ajenas al fenómeno analizado.

# **Sistema de Telecomunicaciones**

Podemos resumir un sistema de telecomunicaciones con el siguiente diagrama de bloques:

Destino

Fuente

Transductor de entrada

Tx

Canal

Rx

Transductor de salida

Observamos que está constituido por tres elementos básicos:

* **Transductor de entrada y salida:** permite realizar la adaptación de las señales (mensajes) de entrada y salida, tal que el sistema pueda ser manejado por el hombre. Esto es necesario porque el emisor y el receptor son dispositivos que trabajan con señales eléctricas, mientras que las entradas y las salidas normales no lo son (acústicas, visuales, alfanuméricas)
* **Sistemas de emisión y recepción:** permiten adaptar las señales entregadas por el transductor de entrada al canal mediante el emisor o transmisor, y luego convertirlas en señales útiles al transductor de salida a través del receptor. Esta adaptación se realiza cambiando los niveles de potencia de la señal, su frecuencia e incluso, en algunos casos, su forma de onda.
* **El canal:** representa el enlace entre un emisor y su correspondiente receptor, es decir, es el camino por el cual se envía la información. En él es donde pueden presentarse perturbaciones como la **Distorsión**, la **Interferencia** y el **Ruido**. Las dos primeras, teóricamente se pueden eliminar, mientras que el ruido no.

La fuente genera **Información** (mensajes a transmitir), y no necesariamente en forma de impulsos eléctricos. Información es todo aquello que elimina una incertidumbre y que ayuda a tomar una decisión.

Analicemos ahora el corazón del sistema de comunicaciones: Transmisor – Canal – Receptor.

El transmisor consta de tres partes o etapas: filtrado, procesamiento de la señal y amplificación. En el transmisor se lleva a cabo la modulación de la señal a transmitir. Modular significa hacer un corrimiento en frecuencia. Una de las razones por la que se modula es para **adaptar la señal a transmitir al medio** (canal). Ej. Cuando hablamos, estamos modulando nuestra voz a través de las cuerdas vocales y los labios. Luego esa voz se transmite por el aire (canal) hasta llegar al oído (receptor) del que escucha. Otra de las razones por la cual se modula es para **eliminar la interferencia y el ruido**. Se lleva a cabo mediante técnicas especiales que analizaremos luego en detalle. Ej. FM (frecuencia modulada). Esta técnica de transmisión requiere un costo: mayor ancho de banda

Una tercera razón para modular sería lograr la **multiplexación de señales**: Ej.: varias señales telefónicas transmitidas por un mismo canal conductor.

Existen otras técnicas de transmisión además de la modulación, que son las técnicas digitales y tienen que ver con la codificación de señales.

El transmisor deberá tener un buen sistema de filtrado de manera que no exista solapamiento de ancho de banda en las transmisiones, por ej.: en AM (amplitud modulada)

El **receptor** en cambio será lo suficientemente capaz de recibir la señal adecuada, es decir que tendrá que realizar el **trabajo inverso al transmisor**. Pero la tarea del mismo (Rx) es aún más fácil, puesto que recibe también las perturbaciones introducidas en el canal y deberá eliminarlas.

Analizaremos ahora los tipos de perturbaciones en el canal:

* Distorsión: todo canal en general es un atenuador, pero no atenúa en forma constante y por lo tanto tendremos una distorsión de amplitud en la señal que lo atraviesa. Esta distorsión es eliminable casi en un 100%. Una de las más difíciles de eliminar es la distorsión de fase.

Se puede hablar también de tiempo de retardo de grupo (idealmente la señal debería demorar lo mismo para cualquier frecuencia). Si las distorsiones son lineales, será posible corregirlas. En caso contrario no.

* Interferencia: tiene que ver con toda señal parecida a la que se transmite y que se mete en el canal de transmisión. Teóricamente, la interferencia al igual que la distorsión pueden ser eliminadas.
* Ruido: es toda señal que tiene un comportamiento aleatorio (impredecible), independientemente de la señal, y es inevitable. Lo único que puedo hacer es mejorar la relación señal a ruido (S/N). Esto se logra aumentando la calidad de la señal a transmitir, por ejemplo, en AM y FM, utilizando distintas técnicas

## **Tipos de sistemas de comunicaciones**

* Según el procesamiento de la información tenemos dos tipos de sistemas:

1. Banda base (B.B)
2. Modulación
3. El termino banda base se refiere a la banda de frecuencia producida por un transductor, tal como un micrófono u otro dispositivo generador de señales que no es necesario adaptarlo al medio por el que se lo va a transmitir.

Banda base es la señal de una sola transmisión en un canal, banda ancha significa que lleva más de una señal y cada una de ellas se transmite en diferentes canales, hasta su número máximo de canal

En los sistemas de banda base (BB) no hay un corrimiento del espectro de frecuencias, mientras que en la modulación si lo hay. Ejemplo modulación de amplitud (AM).

![](data:image/jpeg;base64...)

Los sistemas BB pueden analógicos (comunicación telefónica) o digitales (telex, codificación)

1. Se denomina modulación, a la operación mediante la cual ciertas características de una onda denominada portadora se modifican en función de otra denominada moduladora, que contiene información, para que esta última pueda ser transmitida. También podemos decir, que la modulación es una técnica empleada para modificar una señal con la finalidad de posibilitar el transporte de informaciones a través de un canal de comunicación y recuperar la señal en su forma original en la otra extremidad. El concepto de modulación se basa en poder controlar la variación de alguno de los parámetros (amplitud, frecuencia, fase) de una señal, denominada portadora. Tiene por objeto adaptar la información digital al medio radioeléctrico mediante la analogización a frecuencias de microondas. El modulador es un circuito de producto realizado generalmente mediante un puente de diodos (modulador balanceado) que trabaja a una frecuencia intermedia (35, 70, 140 MHz, etc.) entre la banda base y la radiofrecuencia.

Los sistemas de modulación se dividen en tres partes:

1. De onda continua (CW) Ejemplo: radio, TV, algunos satélites
2. Portadora de pulsos
3. Modulación digital (caso particular de CW)

CW es un corrimiento en frecuencia, pero los parámetros varían en forma continua:

![](data:image/jpeg;base64...)

En la portadora de pulsos se transmite una secuencia de pulsos. Son variaciones analógicas en pulsos (generalmente rectangulares) separados en el tiempo:

![](data:image/jpeg;base64...)

En la modulación digital, la onda es continua, pero tiene saltos bruscos:

![](data:image/jpeg;base64...)

* Otro tipo de clasificación de los sistemas de comunicaciones es el siguiente:

1. **Analógicos:** tanto la fuente de información como las técnicas de modulación son analógicas: Ej.: radio, TV. Ventajas: utilizan un ancho de banda económico, son sencillos y existe una gran experiencia en lo que respecta a sistemas de esta naturaleza.
2. **Digitales:** la información y las técnicas de modulación son digitales. Ej.: telex, comunicación de datos. Una de las ventajas fundamentales de la relación señal a ruido se mantiene constante (no se deteriora), independientemente de la longitud de la onda. Los sistemas digitales necesitan principalmente de un sincronismo.
3. **Híbridos:** aquí necesitaremos de un bloque que realice la conversión analógico-digital

## **Técnicas de análisis y síntesis de sistemas de comunicación**

Una de las técnicas utilizadas es la serie de Fourier, a través de la cual podemos analizar una señal en el tiempo. Si a esta le aplicamos la transformada de Fourier, la podremos analizar en frecuencia (ver desarrollo en apunte “Tres Teoremas (Fourier\_Nyquist\_Shannon)”).

![](data:image/jpeg;base64...)

Otra de las técnicas para el estudio de sistemas de comunicación, es el estudio probabilístico, el cual no analizaremos en detalle.

## **Características generales de los canales de comunicación**

Existen canales eléctricos y electromagnéticos. Los primeros transmiten señales eléctricas y funcionan por traslado de cargas eléctricas (electrones) a través de cables. Los canales electromagnéticos basan su funcionamiento en las propiedades de propagación de las ondas electromagnéticas. Estas se transmiten a través de espacios confinados o de espacios no confinados. Dentro de los primeros se encuentran las guías de onda (por ej. Un caño a través del cual se transmiten señales lumínicas), y las fibras ópticas. Los no confinados son: el éter (espacio libre), visión directiva y sobre horizonte. Aquí tendrá mucha importancia la influencia del ruido y la interferencia.

Los espacios confinados en cambio son inmunes a las interferencias, en especial las fibras ópticas.

Los conductores eléctricos tienen ruido provocado por excitación térmica, pero los canales de electromagnéticos en cambio tienen otro tipo de interferencias o perturbaciones.

Los ruidos que nos interesan principalmente son los ruidos aditivos y los ruidos multiplicativos. El aditivo se denomina también “ruido blanco” y como su nombre lo indica se suma a la señal en cuestión. Los multiplicativos son los de tipos “cuántico” y se deben fundamentalmente a la alinealidad de los elementos que componen el sistema de comunicación, por ejemplo, el receptor. Las fibras ópticas generan ruido multiplicativo dado que a medida que aumenta la energía lumínica, aumenta el ruido.

## **Ruido como elemento limitante**

Existen factores limitantes en un sistema de comunicaciones.

En general, los transmisores son fáciles de hacer. Lo complicado es diseñar un receptor, pues deberá ser lo suficientemente selectivo como para poder desenmascarar la señal del ruido. El receptor deberá tener un nivel mínimo de sensibilidad por debajo del cual no sabrá discernir entre señal o ruido.

En cuanto al transmisor, será necesario trabajar sobre la potencia de transmisión y de acuerdo a ello, junto con la sensibilidad del receptor, me dará la distancia máxima posible entre Rx y Tx.

Otro de los factores a tener en cuenta, es el canal de transmisión, que deberá ser el más adecuado según la aplicación.

Existe una relación importante entre la longitud del canal, ancho de banda, velocidad de transmisión y la sensibilidad del receptor (relación s/n mínima). Así, a mayor velocidad de transferencia, necesitaré un mayor ancho de banda. Además, a medida que aumento la longitud del cable, por ejemplo, se atenúa aún más la señal y aumenta notablemente el ruido.

Básicamente tendremos como limitaciones todo lo que respecta a las perturbaciones, pero también existen otros tipos de limitaciones: la relación “tiempo-ancho de banda”, que está relacionada con el “costo” de la comunicación, y por otro lado el “techo tecnológico”.

Durante la transmisión ocurren ciertos efectos no deseados que afectan directamente la calidad de la señal. El menos perjudicial es la atenuación, el cual reduce la intensidad de la señal; otros más serios son la distorsión, la interferencia y el ruido, los cuales se manifiestan como alteraciones de la forma de la señal. Al introducirse estas perturbaciones al sistema, es una práctica común y conveniente imputárselas, pues el transmisor y el receptor son considerados ideales. En términos generales, cualquier perturbación no intencional de la señal se puede clasificar como “ruido”, y algunas veces es difícil distinguir las diferentes causas que originan una señal contaminada. Existen buenas razones y bases para separar estos tres efectos, de la manera siguiente: distorsión, interferencia y ruido.

1. **Distorsión:** Es la alteración de la forma de la señal deseada debida a la respuesta imperfecta del sistema a ella misma. A diferencia del ruido y la interferencia, la distorsión desaparece cuando la señal deja de aplicarse.
2. **Interferencia:** Es la contaminación por señales extrañas con formas similares a la de la señal original y cuyo origen es generalmente artificial. Este problema es particularmente común en emisiones de radio, donde pueden ser captadas dos o más señales simultáneamente por el receptor. La solución al problema de la interferencia es obvia; eliminar en una u otra forma la señal interferente o su fuente. En este caso es posible una solución perfecta, si bien no siempre práctica.

Podemos también definir a la interferencia como el efecto no deseado del ruido. Si un voltaje de ruido causa que un circuito opere de manera inapropiada, eso es interferencia. El ruido no puede ser eliminado, pero sólo se puede reducir en magnitud, hasta que no cause más interferencia.

**Fuentes de Interferencia:** La interferencia básicamente es producida por el hombre, pero también existen otras fuentes como las condiciones atmosféricas y el clima. La más importante fuente natural son los rayos, ya que son descargas eléctricas muy altas, pero de muy corta duración. A continuación, se mencionan algunos ejemplos de fuentes de interferencia:

* + Sistema de encendido de vehículos
  + Motores eléctricos, líneas de alta tensión
  + Luces de neón y fluorescentes
  + Computadoras
  + Otros tipos de transmisión, tales como la radio amateur, CB (Banda Civil), radio de la policía y otros servicios públicos, inclusive otras estaciones de FM o TV.

Generalmente las fuentes que irradian señales periódicas e intermitentes son llamadas fuentes de impulso. Algunos ejemplos son los interruptores eléctricos, las luces de neón, el sistema de encendido del automóvil, los rayos, etc. Los impulsos son de corta duración (microsegundos) y frecuentemente tienen amplitudes más grandes que la señal que está siendo recibida. La interferencia puede ser irradiada como interferencia electromagnética (EMI), o conducida sobre las líneas eléctricas, en el caso de los equipos con alimentación de corriente alterna (AC).

Existe otro tipo de interferencia como la interferencia de canales adyacentes que es muy común en áreas metropolitanas donde las estaciones (de AM o FM por ejemplo) son asignadas en frecuencias muy cercanas una de la otra. En esas áreas donde la congestión de canales existe, los efectos pueden ser minimizados (si las estaciones están en diferentes direcciones) usando un rotor para orientar la antena para la mínima interferencia.

1. **Ruido:** Por ruido se debe de entender las señales aleatorias e impredecibles de tipo eléctrico originadas en forma natural dentro o fuera del sistema. Cuando estas señales se agregan a la señal portadora de la información, ésta puede quedar en gran parte oculta o eliminada totalmente. Por supuesto que podemos decir lo mismo en relación a la interferencia y a la distorsión; y en cuanto al ruido éste no puede ser eliminado nunca completamente, ni aún en teoría. También podemos denominar ruido a cualquier señal eléctrica en un circuito, con excepción de la señal deseada. Esta definición no se aplica a la distorsión producida en un circuito debido a las no linealidades. Aunque esta distorsión puede ser no deseada, no se considera ruido a menos que se acople con otra parte del circuito. Por tanto, una señal deseada en una parte del circuito es considerada ruido solo si se acopla a alguna otra parte del circuito.

**Tipos de ruido:** Existen numerosos tipos de ruido conocidos, algunos tienen su origen en la misma naturaleza y otros son hechos por el hombre; incluso existen algunos tipos que pueden ser fácilmente eliminados o filtrados, pero en cambio hay otros que son imposibles de eliminar y siempre estarán presentes a pesar de los esfuerzos que se hagan. A continuación, enumeramos algunos de los tipos de ruidos conocidos:

* + **Ruido atmosférico:** Este tipo de ruido es debido principalmente a las descargas atmosféricas que se propagan en todas las direcciones por reflexión ionosférica y es producido mayormente por descargas eléctricas en tormentas. El nivel del ruido varía inversamente con la frecuencia, siendo mayor en las frecuencias más bajas y menor en las frecuencias más altas, pero además depende también del momento del día, del clima, de la estación del año y de la ubicación geográfica.
  + **Ruido térmico:** Está producido por la agitación térmica de los electrones en las resistencias y está presente en toda la naturaleza. Sólo en condiciones de cero absoluto (0 K) este movimiento de electrones cesaría, por tanto, siempre va a existir y es inevitable.

Este **“ruido blanco”** se genera en una amplia banda de frecuencias y la porción que coincide con la banda de paso del sistema del receptor contribuye a la salida de ruido del sistema. Por tanto, la limitación del ancho de banda del sistema tenderá a limitar el ruido térmico. Este ruido térmico tiene lugar en la antena receptora, la línea de alimentación y el propio receptor, siendo el nivel de ruido de la etapa de entrada del receptor particularmente crítico para el funcionamiento del sistema

* + **Ruido hecho por el hombre:** Tiende a disminuir cuando aumenta la frecuencia, aunque puede ser máximo en algunas frecuencias, dependiendo de las características eléctricas de la fuente de ruido. Puede ser originado por utensilios eléctricos de todas las clases, tales como receptores de televisión, sistemas de encendido de automóviles, motores eléctricos, diatermia, generadores industriales de calefacción e incluso por fugas en líneas de alta tensión. La intensidad de campo debido a estas fuentes es muy grande en poblaciones de alta densidad y en zonas industriales. Se propaga por transmisión directa en las líneas de energía y por radiación, inducción y algunas veces por reflexión ionosférica.
  + **Ruido Impulsivo:** Es el ruido ocasionado por agentes ajenos a la línea de transmisión. Por ejemplo, un fenómeno meteorológico, el rayo. Es de corta duración y de gran amplitud. No debemos confundirlo con el ruido atmosférico que también es ocasionado por agentes externos pero que tiene una duración prolongada.
  + **Diafonía:** Aparece a partir del hecho físico de que al circular una corriente eléctrica por un conductor se genera un campo magnético en torno al mismo y si cerca de este conductor se encuentra un segundo conductor que también está transmitiendo, el campo magnético generado por el primero se superpone con el segundo. Un ejemplo claro de esto es cuando hablamos por teléfono y se oye a otra persona. La forma de evitar este tipo de ruido es o bien, apantallando los cables o entrelazando unos cables con otros.

## **Distintas técnicas de modulación**

Cuando hablamos de portadora, hablamos de modulación

Un ejemplo de mensaje analógico en banda base (BB), es la voz y la música que reproduce un equipo de audio. Ejemplos de mensajes con portadoras, pueden ser: armónicas (transmisión de radio en frecuencia o amplitud modulada); o de pulsos, donde la portadora es un tren de pulsos. Si estos son no codificados, estamos en presencia de una modulación analógica de pulsos (cuidado, no es digital). En este caso, tendremos:

* P.A.W.: modulación por amplitud de pulso
* P.W.M.: modulación por ancho de pulso
* P.P.M.: modulación por posición de pulso

Dentro de la modulación por pulso codificados, básicamente tendremos la modulación Delta y la P.C.M. Ambos métodos consisten en muestrear la señal, cuantificarla con un numero de determinado de niveles y asignarle un conjunto de bits a cada uno de ellos; en el caso de P.C.M. una palabra y en el caso de la modulación Delta se le asigna a cada muestra un bit.

Un resumen de las distintas técnicas utilizadas, se bosquejan en el siguiente diagrama

![](data:image/jpeg;base64...)

## **Algunos conceptos fundamentales**

**Velocidad de información y de señalización:** se denomina **velocidad o tasa de información (R)** a la cantidad de bits en promedio, que se transmite en 1 segundo. Esto es, la cantidad de información promedio producida por una fuente en un segundo.

[R] : bits por segundo (bps) en promedio, de información

Se denomina **velocidad o tasa de dígitos o binits (r)**, a la cantidad de dígitos por segundo transmitidos

[r] : dígitos por segundo transmitidos (de información o no)

Se denomina **velocidad de señalización (s)**, a la inversa del tiempo mínimo que dura un pulso

S = 1 / τmin / [s] : 1/seg ó baudios

Ejemplo: Consideremos la transmisión de una señal como la de la figura, donde se indican los pulsos de arranque y parada y los que corresponden al carácter a transmitir, como asimismo los tiempos

![](data:image/jpeg;base64...)

El tiempo mínimo que dura cada pulso será τmin = 20mseg

Esto implica que la velocidad de señalización es de

S = 1/ τmin => S = 1/20mseg => S = 50 baudios

La información transmitida será:

r = 7binits / 150mseg => r = 46 pulsos/seg

Como la señal de arranque y la de parada no dan información útil y los dígitos del código se consideran equiprobables (esto es que cada uno aporta un bit de información), resulta una tasa de información (R) de:

R = 5bits / 150mseg => R = 33bps

Si todos los pulsos tuvieran el mismo ancho, resultaría r = s

Los baudios son la cantidad de pulsos por segundo que habría si todos los pulsos durarán lo que dura τmin

**Capacidad de un canal y velocidad de información:** la capacidad de un canal es su capacidad de transportar información, es decir, la cantidad de información que puede ser relativamente transmitida sobre un canal de comunicación.

Se mide en bits/seg (bps) y como veremos luego, depende de su ancho de banda y de la relación señal/ruido (S/N).

Además, es importante tener en cuenta, que la capacidad del canal también depende de la naturaleza del medio; la fibra óptica, cobre, etc. tienen un límite; Nyquist demostró la existencia de ese límite y se estudiará luego.

Sea una fuente de información con tasa R (bits/seg). Si R < C (capacidad del canal), existirá una codificación tal que la salida de la fuente podrá ser transmitida sobre el canal con una frecuencia arbitrariamente pequeña de error, a pesar de la existencia del ruido. Si R > C no es posible transmitir sin error

**Transmisión multinivel:**

Un aumento de la velocidad de modulación sin aumento del ancho de banda hace que la tasa de errores aumente y puede resultar inútil la comunicación. Se denomina transmisión multinivel a aquella en la que el numero de niveles que puede tomar una señal es mayor a 2.

Se supone un mensaje de duración T compuesto por pulsos de duración τ. Resultará r = s, esto es, la cantidad de pulsos por segundos transmitidos es el máximo para cierto s. Los pulsos podrán tener µ niveles distintos.

![](data:image/jpeg;base64...)

La longitud del mensaje (cantidad de pulsos) será T

Es posible preguntarse:

¿Cuál será la cantidad de símbolos distintos que pueden representarse?

Esta cantidad resulta igual a los µ niveles,

¿pero qué cantidad de mensajes distintos pueden transmitirse?

Esta cantidad será la cantidad de posibilidades de combinación en Tseg, esto es:

M(T) = µT/τ

Luego, la cantidad de bits de información será:

I = lg M(T)  ,donde: lg x = Log x / log 2

Para obtener R basta dividir por T, y con ello se halla la tasa de información (R) en bits/seg

R = I/T = 1/T . lg M(T)  = 1/T lg µT/τ = 1/τ . lgµ

Si τ = τmin => 1/ τ = s => R = s . lg µ

Si son sucesos equiprobables y τ = τmin => R es máxima y C ≥ Rmax

El cual deberá tener una capacidad, por lo menos igual a R

Si el sistema es binario, la cantidad de niveles será 2 (µ = 2); lo cual implica una capacidad de canal coincidente con la señalización:

C (bits/seg) = s (baudios)

![](data:image/jpeg;base64...)La velocidad de señalización s está relacionada con una característica del canal que se denomina ancho de banda (B), de la siguiente manera

B ≥ s/2

**Ejemplo:** un sistema facsímil tiene 250 líneas y 250 puntos por cada línea. Cada punto tiene 32 niveles de brillo equiprobables. La señal resultante se envía a línea con una velocidad de 43bit/seg. ¿Cuánto se tarda en transmitir una imagen completa?

R = 43bps

µ = 32 I = lg 32 = 5bits por punto

Tp = I/R = 5bits por punto / 43bits por seg

Tp = 1/8,6 seg por punto

T = Tp x 250lineas /imagen x 250puntos/línea

T = 7268seg ≈ 2horas

# **Detección y corrección de errores**

![](data:image/jpeg;base64...)

**Confiabilidad**

Cuando trabajamos en condiciones normales (no ideales), la fuente de información emite mensajes que luego se transmiten codificados por un canal real. El ruido que “se mete” en este, cambia la información que se desea transmitir haciendo que los mensajes lleguen a destino con error. Por ejemplo, si se transmite 001 y se recibe 011, se produjo un error simple (un bit) en el canal, en el segundo bit.

Es imprescindible entonces, estudiar la forma de poder detectar y aún más corregir ciertos tipos de errores introducidos en el canal.

Se define **Ruido Unitario**, al cambio de un bit por su complemento (en codificación binaria), en una palabra, trasmitida.

**Códigos detectores de errores**

Existen diversos tipos de códigos detectores de errores, entre ellos los Códigos de Paridad, Códigos por Mayoría y los Códigos de Peso Constante (se entiendo por peso de una combinación binaria, el número de “unos lógicos” de la misma)

**Códigos de Paridad**

Se obtienen añadiendo a las combinaciones de los códigos de distancia unidad, un bit de paridad (bit redundante).

Si deseo obtener un código de paridad par, dicho bit será tal que el número de unos en cada combinación del nuevo código sea par.

Si deseo obtener un código de paridad impar, dicho bit será tal que el número de unos en cada combinación del nuevo código sea impar.

La detección de errores en estos códigos consiste en comprobar si el número de unos de la combinación recibida es par (si uso un código de paridad par) o impar (si uso un código de paridad impar)

Una combinación recibida en el destino se considera “errónea”, si su paridad no coincide con la de su respectivo código emitido en la fuente.

Notar que estos códigos permiten “detectar” errores de un numero impar de bits (1, 3, 5, etc.), ya que, si el número de bits erróneo es par, no altera la paridad.

El binit de paridad también puede modificarse en el canal por efecto del ruido.

Este tipo de paridad (par o impar) también recibe los nombres de bit de paridad transversal, bit de paridad vertical o comprobación de redundancia vertical (VRC).

**Redundancia como factor de absorción del ruido**

Supongamos tener 3 símbolos de nuestro alfabeto código. Así podremos codificar 23 símbolos de una fuente, o sea 8 símbolos. Si ahora agregamos un binit de paridad, seguiremos codificando 23 símbolos (ahora con protección)

Pero con 4 símbolos en el alfabeto código, se pueden codificar 24 símbolos, o sea 16. De esto se deduce que no se utilizan:

24  - 23 = 8 configuraciones

Estas son precisamente las configuraciones que nos absorben el ruido

**Método de redundancia cíclica**

El método consiste en que la estación emisora agregue al final de cada bloque de datos una información calculada de acuerdo con una fórmula polinómica, cuyas variables son los ceros y unos enviados en el bloque de datos.

La estación destino realiza el mismo calculo. Si le produce el mismo resultado, la transmisión es correcta, pero si no ha sido así, solicita a la estación emisora que repita el proceso.

La información añadida recibe el nombre de Código de Redundancia Cíclica (CRC), Carácter de Comprobación de Bloque (BCC) o simplemente Redundancia.

**Códigos por Mayoría**

Este método consiste en codificar de forma tal que en una palabra haya mayor “peso” de unos lógicos que de ceros lógicos; y luego en el receptor, se controla si se viola esta regla cuando recibimos el mensaje.

Por ejemplo: codificamos con una longitud constante I = 5 y peso 3 de unos

Existe un numero de palabras que cumplen con este peso, igual a:

C53 = $\frac{5 x 4 x 3}{3 x 2}$ = 10

Estas son

00111

01110

11100

10101

11001

01011

11010

10011

10110

01101

Pero nótese que con 5 símbolos en un alfabeto código, se puede codificar (sin protección) 25 = 32 símbolos fuente. Este método detecta todos los errores unitarios. En el caso de tener errores de orden mayor, no se puede asegurar su eficacia

**Códigos de igual peso**

Es muy similar al de mayoría, salvo que ahora se codifica de forma tal que el numero “1” sea igual al de “0” dentro de la palabra código a transmitir por el canal.

Indudablemente, las palabras código resultarán de longitud 1, con 1 par.

**Regla de decisión**

Hemos visto hasta ahora, que algunos criterios de protección detectan errores, pero no los corrigen. En algunas aplicaciones, esto se soluciona pidiendo (en el caso de haber detectado un error) que se retransmita la información. En otras aplicaciones, esto no es posible y por lo tanto se debe buscar otra solución que puede ser adoptar una regla de decisión. Esta consiste en, recibida una palabra, que se sabe con equivocación, modificarla según una regla de manera tal que adopte la forma de una palabra sin equivocación.

Es indudable que esto trae asociado una probabilidad de error (o acierto). De ahí que esta regla de decisión debe ser adoptada de forma tal que nos proporcione una probabilidad de error lo más baja posible.

Ejemplo:

![](data:image/jpeg;base64...)

Si sabemos que el canal tiene una probabilidad relativamente elevada de provocar cambios unitarios, y en mucho menor grado, errores de orden superior, la regla de decisión es evidente:

Si se recibe 001, se codifica como recibido 000

011, “ “ “ “ 111

. “ “ “ “ .

. “ “ “ “ .

**Códigos correctores de errores**

Los códigos correctores de errores no solo indican la existencia de un error, sino que proporcionan información de cuál es el digito o dígitos binarios erróneos, y por lo tanto, permiten su corrección invirtiendo simplemente el bit correspondiente. Estos códigos son utilizados en la transmisión de información digitalizada.

Código de Hamming (Paridad por zonas)

Es un código corrector de error, cuyo método consiste en controlar la paridad por zonas formadas por conjunto de binits.

Veremos un método para construir un código Hamming capaz de corregir errores en un bit.

Diagrama de Venn:

![](data:image/png;base64...)

En este diagrama los binits que transportan información (y por lo tanto juegan libremente), son i0, i1, i2 y i3

Se observa que las zonas delimitadas, poseen además otros binits: C1, C2, C3 que son los binits de control.

Se los denomina binits de control, pues estos se acomodan de forma tal que, conjuntamente con los binits de información de su zona conserven una determinada paridad.

O sea, si adoptamos el criterio de paridad par, C1, C2, C3 deberán tener los siguientes valores:

C1 = i0 + i1 + i2 (4.17.1)

C2 = i0 + i2 + i3 (4.17.2)

C3 = i0 + i1 + i3 (4.17.3)

Recordar que C1, C2, C3, i0, i1, i2, i3 pueden adoptar valores 0 o 1

Luego

C1 controla a i0, i1, i2 y a C1 (4.17.4)

C2 controla a i0, i2, i3 y a C2 (4.17.5)

C3 controla a i0, i1, i3 y a C3 (4.17.6)

La palabra a ser transmitida ahora tendrá la forma

i0 i1 i2 i3 C1 C2 C3 (4.17.7)

Al recepcionar se controla la paridad de las zonas. Por ejemplo, supongamos que se alteró el valor de i2. Esto trae aparejado que las ecuaciones que no se cumplen son la (4.17.1) y la (4.17.2); o en otras palabras se modificó la paridad de las zonas I y II quedando unívocamente determinado el binit cambiado: i2

Si el error proviene de un cambio en un binit de control, este se pone en evidencia pues la zona modificada es sólo una, la correspondiente a dicho binit de control.

Cabe la pregunta: si se realiza un código con m dígitos de información ¿Cuántos dígitos de control se deben agregar? Se deben agregar n dígitos de control.

Con n dígitos de control se pueden tener 2n configuraciones distintas. Cada una de estas configuraciones, indicará error en un digito, existiendo m + n dígitos. Pero, además, deberá existir una configuración que indique la no existencia de error. Luego se deberá cumplir con la relación

2n ≥ m + n +1 (4.17.8)

En nuestro ejemplo, m = 4. Luego n debe valer 3 para que:

23 ≥ 4 + 3 +1 se verifique

A continuación, hagamos una parte del problema

Dígitos de información Dígitos de control

i0 i1 i2 i3 C1 C2 C3

0 0 0 1 0 1 1

0 0 1 0 1 1 0

0 0 1 1 1 0 1

1 1 0 1 1 0 1 \*

: : : : : : :

: : : : : : :

1 1 1 1 : : :

Notar que las configuraciones de los dígitos de control se repiten; pero en ocho configuraciones (que no son las mostradas \*) que me indican la:

1. Equivocación en dígitos de información 4

Equivocación en dígitos de control 3

1. La configuración que dice todo ok 1

Total ---------> 8

Entonces vimos que, chequeando las zonas cuyas paridades se han alterado según sea utilizado el diagrama de Venn, o las tablas, se identifica el digito que provoca el problema. Este es el método cuando la palabra protegida se envía de la forma mostrada.

Pero existe otro método que, indica cómo elegir las zonas y como intercalar, entre los dígitos de información, los dígitos de control, de forma tal que (enumerando la posición de los dígitos en la palabra transmitida), se produce un error, la configuración que adoptan los dígitos de control, debido a ese error, me indica (en decimal) el n del digito que fue alterado. Falta aclarar que la configuración de los dígitos de control se obtiene así:

Si la Zona Cj fue alterada, el digito de control correspondiente se coloca en 1. De lo contrario es cero.

Vemos ahora como numeramos e intercalamos los dígitos de control en la palabra codificada

1 2 3 4 5 6 7 8 9 n

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

Esta es la palabra y se han numerado los dígitos.

Los dígitos de control se intercalan en las posiciones 2n con n € Z (dígitos rayados)

Los dígitos que quedan libres, se usan para transportar información. Falta ahora ver como elegimos las zonas; ya que de la elección de estas depende la identificación del digito alterado, esta elección no puede ser arbitraria

Hagámoslo sobre un ejemplo

3 binits de control

4 binits de información

En la palabra, las posiciones serán las siguientes:

![](data:image/png;base64...)

Recordemos ahora lo que deseamos obtener

1. Se coloca un “uno” en el digito de control, si al recepcionar se detecta que en esa zona no se conserva la paridad pre-establecida.
2. Colocando luego los dígitos de control en orden, el n formado n decimal es el n° del digito alterado.

Ejemplo:

Zona I alterada ------- C1 = 1

Zona II alterada ------ C2 = 1

Zona III alterada ----- C3 = 0

![](data:image/png;base64...)

Diagrama propuesto:

![](data:image/png;base64...)

Luego:

C1 = {1, 3, 5, 9}

C2 = {2, 3, 6, 7}

C3 = {4, 5, 6, 7}

Si lo planteamos sobre un diagrama de Karnaugh, este debe tener 8 cuadraditos

![](data:image/png;base64...)

Cada cuadradito me representa en decimal, el número del digito. El 000 lo reservamos par indicar que no hubo ningún error, pues esto implica C1 = 0; C2 = 0; C3 = 0

La regla practica para determinar las zonas que controlan C1; C2; C3 es

1. Se ubican los dígitos de control en sus respectivos lugares
2. Se observa que a cada digito de control, por estar en las posiciones 2n; le corresponde un n° en binario con un solo “1”
3. Cada digito de control controla a aquellos dígitos que, en binario, posean un 1 en el binit en el cual dicho digito de control lo posea.

Ejemplo:

C2 le corresponde 0 1 0

Luego C2 controla aquellos dígitos que en binario posean un “1” en el binit señalado con una | ; o sea:

![](data:image/png;base64...)

Supongamos querer transmitir la palabra 1 1 0 1

La ubicación será 1 0 1 0 1 0 1

Ahora se deben colocar con el valor adecuado los dígitos de control

![](data:image/png;base64...) \*\*

Luego la palabra que se transmite es

1 0 1 0 1 0 1

Supongamos que al recepcionar se obtenga

1 0 1 0 1 1 1

Se controla la paridad de las zonas nuevamente realizando el cálculo \*\*

Observamos que

![](data:image/png;base64...)

En este ejemplo, analizando en detalle se puede ver que puedo desechar cualquier digito cumpliéndose siempre que la probabilidad de error doble no detectado es siempre igual.