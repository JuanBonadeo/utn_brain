Velocidad de información y señalización

Se denomina velocidad o tasa de información a la cantidad de bits en promedio que se transmiten en 1 segundo, esto es, la cantidad de información promedio producida por una fuente en un segundo.

**R: Tasa de Información [R]: bits/seg.**

Se denomina velocidad o tasa de dígitos a la cantidad de dígitos por segundo transmitidos.

**r : Tasa de Dígitos [r]: dígitos/seg. ó binits/seg.**

Se denomina velocidad de señalización a la inversa del tiempo mínimo que dura un pulso (**τmin**):

**s = 1/τmin ; [s]: 1/seg. ó baudios**

**Ejemplo**:

Consideremos la emisión de una **Teleimpresora**, la cuál transmite una señal de pulsos como la de la figura siguiente. Cada caracter transmitido (LETRA) tiene 5 pulsos, y está enmarcado por un pulso de arranque y otro de parada. O sea que en total son 7 pulsos por cada carácter (1 ARR, 5 de información (LETRA) y 1 PARADA).

El pulso de PARADA dura 30 mseg. Todos los demás, el de ARRANQUE y los de información, duran 20 mseg. c/u.

Amplitud

t

ARR L E T R A PARADA

20ms 20ms 20ms 20ms20ms20ms 30ms

T = 150 mseg.

El tiempo mínimo que dura un pulso será: τmin= 20 mseg.

Esto implica una velocidad de Señalización de: s = 1/ τmin = 1/20 mseg. = 50 Baudios

La velocidad o tasa de dígitos, será: r = 7 binits / 150 mseg. = 46 binits / seg.

Son 7 pulsos en total, 2 de control (arranque y parada) y 5 de información (letra). Como son pulsos en general (combinación de control e información) se denominan “binits”.

Los binits de control no dan información útil.

Finalmente, la tasa de Información será: R = 5 bits / 150 mseg. = 33 bps

Ahora sí, la unidad de la tasa de Información es bits por segundo (bps), puesto que todos los pulsos son de información (los 5 de la letra transmitida).

Notar que el tiempo considerado en el cálculo de R es el total de la letra: T = 150 mseg.

Por lo tanto, podemos afirmar que la velocidad máxima a la que se puede transmitir será s = 50 Baudios.

Si todos los pulsos duraran lo mismo, r = s = 50 Baudios.

Luego, **R < r < s**

Capacidad de un canal y velocidad de información

![](data:image/png;base64...)

Sea una fuente de Información que emite pulsos por segundo (xi), los cuales son transmitidos a través de un canal de comunicaciones.

La capacidad de dicho canal (C), es su capacidad de transportar información. Se mide en bits/seg. [C]: bps

La fuente emitirá entonces con tasa de información promedio R.

Si R ≤ C existe una codificación tal que la salida de la fuente pude ser transmitida sobre el canal con una frecuencia arbitrariamente pequeña de error, a pesar de la existencia de ruido en el mismo.

Si R > C no será posible transmitir sin error. Por lo tanto, deberá ser R ≤ C.

Transmisión Multinivel

Supongamos una transmisión de duración T compuesto por n pulsos de duración τ como la de la figura de abajo. Los pulsos pueden tener μ niveles distintos.

![](data:image/png;base64...)

t

Entonces será:

T: duración del bloque de pulsos transmitidos

V: amplitud de los pulsos transmitidos

μ: cantidad de niveles posibles de amplitud de c/u de los pulsos transmitidos

τ: duración de c/u de los pulsos transmitidos

T/τ : n (cantidad de pulsos transmitidos)

Es posible preguntarse, ¿Cuál será la cantidad de símbolos distintos que podrán representarse? Esta cantidad resulta igual a los μ niveles (cada símbolo resulta un nivel de amplitud). ¿Pero que cantidad de mensajes distintos pueden transmitirse? Esta cantidad será igual al número de posibilidades (combinaciones) de arreglos con repetición en T segundos, o sea:

**M (T) = μT/τ**  donde: M(T) es la cantidad de mensajes

distintos generados en el tiempo T.

luego: **I = lg M(T)**

I será la **cantidad de información** en bits, transmitida en un tiempo T. ; [ I ]: bits

Para obtener R basta con dividir por T, con ello se halla la tasa de información R en bits por segundo.

Entonces el cálculo de R será:

**R = I/T . lg M(T) = 1/T  . lg μT/τ**

Si τ = τmin luego  **1/τ = s**

Si τ = τmin, entonces R es máximo y deberá ser C = R. Esto es, el canal deberá tener una capacidad C al menos igual a R. Si el sistema es binario, la cantidad de niveles será μ, lo que implica una capacidad de canal coincidente con la de señalización.

**C = s**

La velocidad de señalización está ligada con una característica del canal de transmisión, que se denomina ancho de banda (B). Este valor resulta:

**B = s/2**

Ensayando el canal, el ancho de banda B resulta aproximadamente igual al valor para el cual la relación entre la salida y la entrada disminuye una determinada cantidad.

![](data:image/png;base64...)

Amplitud

0 frecuencia

Esta cantidad es 3 dB, y equivale a una pérdida del 50 % de la potencia de entrada al canal. A partir de allí, la característica seguirá disminuyendo hasta 0 (ver gráfica de arriba).

Cualquier señal que se quiera transmitir por ese canal, deberá estar en un rango de frecuencias de 0 a B para no sufrir atenuación.