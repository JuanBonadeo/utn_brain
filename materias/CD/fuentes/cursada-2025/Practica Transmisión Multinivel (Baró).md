**Transmisión Multinivel**

## **Ejercicios**

1. Indique cantidad de niveles (μ), pulsos (n), Información (I) y cantidad de mensajes en el tiempo T (M(T)).

![](data:image/png;base64...)

Resolución:

En este caso tenemos una transmisión de 6 pulsos que adoptan (c/u de ellos) 2 niveles posibles de amplitud, 2 y -2 (V).

Entonces: μ = 2 ; n = 6

I = lg μn = lg 26 = 6 x lg 2 = 6 bits (porque lg 2 =1)

M (T) = μn = 26 = 64 mensajes distintos

1. Indique cantidad de niveles, pulsos, Información, cantidad de mensajes y la Tasa de Información (R) a la que se está transmitiendo; siendo el periodo T=100mseg

![](data:image/png;base64...)

Resolución:

Aquí se ve de la gráfica: 7 niveles de amplitud (3, 2, 1, 0, -1, -2, -3) y 6 pulsos.

M(T) = μn = 76 = 117.649 mensajes distintos.

I = I = lg μn = lg 76 = 6 x lg 7 = 2,81 bits

R = I/T = 2,81 / 100 mseg. = 28,1 bps

1. Una transmisión considera grupos de 18 pulsos de 128 niveles de amplitud c/u. Calcular:
   1. M(T) e Ix
   2. R
   3. Realice la gráfica de la transmisión.

Cada pulso dura 1mseg

Resolución:

a. Tenemos n = 18 y μ = 128 , entonces: M(T) = μn = 12818 (un número muy

grande…) I = lg μn = lg 12818 = 18 x lg 128 = 18 x lg 27

I = 18 x 7 x lg 2 = 18 x 7 = 126 bits

1. R = I/T = 126/18 ms = 7 Kbps
2. Les dejo la gráfica a Uds ….
3. Indique cantidad de niveles, pulsos, Información, cantidad de mensajes y la Tasa de Información a la que se está transmitiendo en este caso: T=60 μseg.

![](data:image/png;base64...)

Resolución:

μ = 4 (4, 2, 0, -2) Los niveles se indican generalmente en el eje “y”de la gráfica.

n = 6

I = lg μn = lg 46 = 6 x lg 22 = 6 x 2 x lg 2 = 6 x 2 = 12 bits

R = I/T = 12 bits/60 μseg. = 0,2 x 106 bps = 200 Kbps (notar que el prefijo “μ” en el denominador, pasa al numerador como “Mega”, o sea 106).

1. Indique en el siguiente caso, cantidad de niveles, pulsos, Información y cantidad de mensajes. T=30 μseg.

![](data:image/png;base64...)

Resolución:

μ = 2 (0 y 2) n = 5 pulsos (binarios)

I = lg μn = lg 25 = 5 lg 2 = 5 bits

M(T) = 25 = 32 mensajes distintos

1. Una transmisión multinivel considera grupos de 13 pulsos de 58 niveles c/u. Teniendo en cuenta que la transmisión tiene 1 pulso fijo de arranque de +3V y 1 pulso fijo de stop de --3V. Cada pulso dura 10 μseg. Calcular:
   1. M(T) e Ix
   2. R
   3. Realice la gráfica de la transmisión

**Resolución**: c. Amp.

tiempo

ARR 13 pulsos multinivel STOP

a. M(T) = **μT/τ**

**μ** = 58 (cantidad de niveles posibles) T = 15 x 10 μseg = 150 μseg τ = 10 μseg

En el cálculo de T, hay que considerar TODOS los pulsos involucrados, no sólo los multinivel. Por eso es 150 μseg.

Por lo tanto: M(T) = 58**13** mensajes distintos

Ix = lg M(T) = lg 58**13** =13 xlg 58 = 13 x 5,86 = 76,16 bits ~ 77 bits (se aproxima para arriba)

donde: lg 58 = log10 58 / log10 2 = 5,86

b. R = Ix / T = 77 bits / 150 μseg = 0,513 x 106 bps = 513 Kbps

1. Una transmisión multinivel considera grupos de 10 pulsos de 64 niveles c/u, sin ningún pulso de control adicional. Calcular:
   1. Cantidad de mensajes
   2. Ix
   3. Tasa de información a la que se está transmitiendo.
   4. Realice la gráfica de la transmisión.

Cada pulso dura 2mseg.

Resolución:

a. M(T) = **μT/τ**  = 64**10** mensajes distintos

b. Ix = Ix = lg M(T) = lg 64**10**  = 10 x lg 26 = 10 x 6 x lg 2 = 10 x 6 = 60 bits

c. R = lg M(T) / T = 60 bits / 20 ms. = 3 Kbps

d. Tarea para uds….

1. Un sistema de fax tiene 400 líneas y 400 puntos c/línea. Cada punto tiene 64 niveles de brillo equiprobables. La velocidad de transmisión es de 4800 bps. ¿Cuánto tardará en transmitir 1 imagen completa?

Una imagen completa es representada por: 400 líneas x 400 ptos/línea = 160.000 puntos

Si cada punto tiene 64 niveles de brillo, suponemos a esos 64 niveles como niveles de amplitud posibles para cada uno de los puntos de una imagen (160.000 en total).

Por otro lado, nos dice que la R = 4.800 bps y quiero saber en cuanto tiempo transmito una imagen completa. Entonce aplico la fórmula de velocidad de Información:

R = 4.800 bps = lg M(T) / T = lg 64**160.000**  / T

Paso T multiplicando: 4.800 bps x T = lg 64**160.000**  = 160.000 x lg 64 = 160.000 x lg 2**6** =

4.800 bps x T = 160.000 x 6 x lg 2 = 160.000 x 6 = 960.000

T = 960.000 / 4.800 = 200 seg.

1. Sea la siguiente transmisión (esquema debajo), indique para cada subsistema:
   1. Cantidad de pulsos y niveles.
   2. Cantidad de mensajes posibles generados en un tiempo total (T).
   3. Ix
   4. R
   5. Como puedo duplicar la Velocidad de Información obtenida en d), sin variar la duración de los pulsos ni el periodo (T total)?

![](data:image/png;base64...)

**Resolución**:

a. Se aprecia de la gráfica de arriba, que hay dos subgrupos o subsistemas. El primero es un bloque de 5 pulsos multinivel que dura 100 μseg, y el segundo un bloque binario de 8 bits que dura 40 mseg. Por lo tanto, tendré dos M (cantidad de mensajes): M1 (para el multinivel) y M2 (para el binario).

b. El M(T) total, será: M1 x M2 (siempre es el producto de los distintos M)

Por lo tanto, calculemos cada uno de ellos: M1 = 7**5** y M2 = 2**8**

Entonces: M(T) = M1 x M2 = 7**5** x 2**8**

Se ha considerado el “0” como un nivel posible en ambos subgrupos de pulsos.

c. La cantidad de Información será: I = lg M(T) = lg (7**5** x 2**8**)

Por propiedad del logaritmo, puedo decir que el logaritmo de un producto es la suma de los logaritmos. Entonces:

I = lg 7**5** + lg 2**8** = 5 x lg 7 + 8 x lg 2 = 5 x lg 7 + 8 = 5 x 2,8 + 8 = 14 + 8 = 22 bits

Esto significa que el bloque multinivel representa 14 bits de información. Los otros 8 bits, son del bloque binario.

d. Ahora calculemos la Tasa de Información: R = I / T = 22 bits / T

Ojo que el T total es la suma de los tiempos parciales, los cuales tienen distinta unidad (el primer bloque son μseg y el segundo son mseg). Por lo tanto será: T = 100 μseg + 40 mseg = 40,1 mseg

Entonces: R = 22 bits / 40,1 mseg = 548,6 bps

e. Si duplicamos la velocidad, será: 2R = 1097 bps

Como el enunciado nos dice que no podemos modificar los tiempos de los pulsos ni el total, sólo podremos variar la cantidad de niveles de amplitud. Entonces tendremos dos opciones: variar la cantidad de niveles de la parte multinivel o la de la parte binaria (una de las dos).

Optaremos por la primera, aumentar la cantidad de niveles del bloque de pulsos multinivel.

Entonces el planteo es: 2R = 1097 bps = lg (μ**5** x 2**8**) / 40,1 mseg

Por propiedad del logaritmo:

1097 bps = ( lg μ**5** + lg 2**8**  ) / 40,1 mseg = ( 5 x lg μ + 8 lg 2 ) / 40,1ms

1097 bps = (5 x lg μ + 8) / 40,1 ms

Tengo que sacar (despejar) μ de adentro del logaritmo. Entonces, paso multiplicando 40,1 ms y restando 8 bits:

1097 bps x 40,1 ms – 8 bits = 5 x lg μ

43,99 bits – 8 bits = 5 x lg μ

35,99 bits = 5 x lg μ

7,19 bits = lg μ

El logaritmo pasa para la izquierda de la igualdad, como base de la exponencial:

27,19 = μ

146,8 = μ

Finalmente, redondeamos para arriba la cantidad de niveles: μ = 147 niveles de amplitud

Entonces, la respuesta del inciso e) del problema, será: “para duplicar la velocidad de Información, deberé aumentar la cantidad de niveles (del bloque multinivel) a 147.”

1. Una transmisión multinivel considera grupos de 13 pulsos de 58 niveles c/u. Teniendo en cuenta que la transmisión tiene 1 pulso de arranque (amplitud fija) y 1 pulso de stop (amplitud fija), indique:
   1. Ix
   2. R
   3. Como puedo duplicar la velocidad total de transmisión sin variar la duración de los pulsos ni el periodo.
   4. Realice la gráfica de la transmisión

El periodo de transmisión dura 100 μseg y todos los pulsos duran lo mismo.

1. Sea la transmisión graficada debajo. Indique:
   1. Cantidad de niveles y pulsos en cada subsistema
   2. Ix
   3. R
   4. Como puedo duplicar la velocidad total de transmisión (R) sin variar la duración de los pulsos ni el período?
   5. Si R = 5 Mbps cuanto pulsos son binarios?

Tenga en cuenta que todos los pulsos duran lo mismo y T=500 μseg.

![](data:image/png;base64...)

Resolución:

1. En este caso, como en el problema anterior, tenemos dos subsistemas dentro de T.

Por un lado M1 y por otro M2. Entonces será: M(T) = M1 x M2

Donde M1 = μ**5** = 65 = 7776 mensajes distintos

M2 = μ**n** = 2n (porque son bits)

Entonces: Cantidad de niveles en la primera parte: 6, pulsos: 5

Cantidad de niveles en la primera parte: 2, pulsos: n (incógnita)

1. Ix = lg M(T) = lg (M1 x M2) = lg (65 x 2n) , (queda expresado, porque me falta el

valor de “n”).

c. R = Ix / T = lg M(T) / T = lg (65 x 2n) / 500 μseg. , (idem arriba)

d. Si no puedo variar ninguno de los tiempos, no me queda más remedio que variar

(aumentar) la cantidad de niveles. Supongo que dejo los pulsos binarios como

están, y aumento la cantidad de niveles del primer subsistema. Entonces será:

2 x R = lg (m5 x 2n) / 500 μseg. , donde “m” será el número de niveles de

amplitud nuevo. Sólo lo planteo, no puedo

calcularlo, porque tengo ahora dos incógnitas (m y n).

* 1. Vuelvo a al punto c.

Arranco de: R = 5 Mbps = lg (65 x 2n) / 500 μseg.

Entonces, “desarmo” el lg para poder despejar “n”:

5 Mbps = (lg 65 + lg 2n)/ 500 μseg.

500 μseg. X 5 Mbps = lg 65 + lg 2n

(500 seg. x 5 bps) - lg 65  = lg 2n

2500 bits – 5 x lg 6 = n x lg 2 = n

2500 bits – 5 x 2,58 bits = n

2.487 bits = n