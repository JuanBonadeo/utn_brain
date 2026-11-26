Resumen de **Comunicación de datos - 1er parcial**

**(Explicación de conceptos - Parcial Medin y Baró)**

# Información, Codificación y Canales

## Información

La Cantidad de Información I(A) que aporta un suceso A es función inversa de la probabilidad de ocurrencia de ese suceso es decir de la p(A).

$I(A) = función 1/ p(A)$

A través de esta fórmula podemos intuir tres propiedades:

* Dado el suceso con $p(A)≃1$, la cantidad de información otorgada es $I(A)≃0$
* Dado el suceso con $p(A)≃0$, la cantidad de información otorgada es $I(A)≃\infty $
* Para dos sucesos independientes A y B cada uno con su respectiva probabilidad de ocurrencia p(A y p(B) , donde A trae cantidad de información I(A) y B trae cantidad de información I(B).
  + La probabilidad del suceso conjunto es: $p(A∩B) = p(A) \* p(B)$
  + La información del suceso conjunto es: $I\_{(A∩B)} = I(A) + I(B)$

Como trabajamos con dígitos binarios, la función trabajada será el logaritmo en base dos, quedandonos:

$I(A)= log\_{2} \frac{1}{p(A)}=lg \frac{1}{p(A)}$

## Modelos aleatorios univariados

El modelo aleatorio univariado es un modelo probabilístico del comportamiento de una fuente de información o de un receptor de la misma.

Supongamos que tenemos una fuente S que emite tres símbolos R, A, y V y que una muestra significativa es la siguiente:

![](data:image/png;base64...)

Cada símbolo al aparecer nos dará una cantidad de información dada I(A), I(V) e I(R)

La fórmula para calcular la cantidad de información promedio es:

$Inf. Prom=\frac{N(A)⋅ I(A)+N(V)⋅I(V)+N(R)⋅I(R)}{N\_{tot}}$

* $N\_{tot}$ es el número total de la muestra
* Ahora bien, cada cociente $N\_{(i)}/N=fr\_{i}=P(i)$

Por lo tanto, la Cantidad de Información promedio que emite una fuente será:

$H(S)=\sum\_{}^{}p\_{i} ⋅ lg \frac{1}{p\_{i}}=-\sum\_{}^{}p\_{i} ⋅ lg p\_{i}$

### Entropía de la fuente

Para una caracterización univariada denominamos “**entropía**” – y la notamos **H(x)** – a la esperanza matemática de la información por símbolo de la fuente, esto es:

$H(S)=-\sum\_{}^{}p\_{i} ⋅ lg p\_{i}$

La función entropía tiene su máximo valor, para un determinado número de símbolos fuente, cuando estos son equiprobables.

## Modelos aleatorios bivariados

Se puede definir un canal de información como determinado por un alfabeto de salida $B = (b\_{j}), J = 1, 2, 3, ........, s$; y un conjunto de probabilidades condicionales $p(b\_{j}/a\_{i})$ siendo esta la probabilidad de recibir a la salida el símbolo $b\_{j}$ cuando se envía el símbolo de entrada $a\_{i}$.

![](data:image/png;base64...)

A un canal se lo denomina **transparente** cuando no introduce error, esto es si, su

matriz de probabilidades condicionales es diagonal

### Canal binario simétrico

Un canal de importancia teórica es el **binario simétrico** (**BSC**). Este canal posee dos símbolos de entrada ($a\_{1} = 0, a\_{2} = 1$) y dos de salida ($b\_{1}= 0, b\_{2}= 1$). Es simétrico por ser iguales las probabilidades de recibir un cero al enviar un uno y viceversa. Esta probabilidad se denomina probabilidad de error (p).

![](data:image/png;base64...)

Se verán las llamadas probabilidades hacia atrás, esto es, p(ai/bj) que significa la probabilidad de que habiéndose dado bj a la salida, provenga de un ai a la entrada del canal. Entonces, usando Bayes:

* $P(ai) \* P(bj/ai) = P(bj) \* P(ai/bj)$

Por lo tanto, se puede calcular la incertidumbre de un símbolo de entrada dado un

símbolo a la salida

* $P(ai/bj) =\frac{ P(ai) \* P(bj/ai) }{P(bj)}$

La incertidumbre de aparición en el sistema, es decir, la información media al emitir ai y recepcionar bj, se denomina **entropía del sistema**:

* Se denomina $P(a\_{i})$ a la **probabilidad a priori** de los símbolos de entrada.
  + La fórmula es: $H(A) = Σ p(a\_{i}) \* lg\frac{1}{p(a\_{i})}$
* Y a $P(a\_{i}/b\_{j})$ se la denomina **probabilidad a posteriori**,
  + La fórmula es: $H (A/B) = Σ P(b\_{j}) \* P(a\_{i}/b\_{j}) \* lg P(a\_{i}/b\_{j})$
* Como se conoce la $P(\frac{a\_{i}}{b\_{j}})$ que caracteriza al canal, en forma similar se obtiene la **entropía del canal** (equivocación de B respecto de A).
  + La fórmula es: $H (B/A) = Σ P(a\_{i}) \* P(b\_{j}/a\_{i}) \* lg P(b\_{j}/a\_{i})$

## Información Mutua

La información mutua es la información transferida desde la fuente al receptor a través del canal, esto es, la información **real** que llega al receptor en promedio.

Para calcular la información promedio real recepcionada bastará obtener la diferencia entre la entropía a priori y la equivocación de A respecto a B.

Una importante propiedad de la información mutua es la simetría con respecto a las variables de entrada y salida, entonces es válido decir que:

$I(A, B) = I(B, A) = H(B) – H(B/A)$

## Capacidad y eficiencia de Canales.

### Capacidad

La capacidad de un canal será función exclusivamente de las probabilidades condicionales y no dependerá de las probabilidades de los símbolos de entrada.

$C = max H(A)$

### Eficiencia

Se define a eficiencia de transmisión para cada canal y fuente, a:

$FF = \frac{I(A, B)}{C}$

Y redundancia de transmisión a:

$RED = 1 - FF$

Esta redundancia es la parte no aprovechada de la capacidad portante de información del canal.

## Otros Conceptos Fundamentales

### Velocidad de información y señalización

Se denomina velocidad o tasa de información (R), a la cantidad de bits en promedio que se transmiten en 1 segundo, esto es, la cantidad de información promedio producida por una fuente en 1 (un) segundo.

Si se considera un canal con ruido, a la salida se tiene una tasa de información de:

$R = H’(A) - H’(A/B)$

Se denomina velocidad o tasa de dígitos o binits ($r$) a la cantidad de dígitos por segundo transmitidos. Como la entropía es la información promedio (o bits por símbolos en promedio - $H$), resulta:

$R = r H(A)$

R y H son dos formas de medir información promedio, una en bits por segundos y otra

en bits por símbolo.

Se denomina velocidad de señalización ($s$) a la inversa del tiempo mínimo que dura un pulso:

$s =\frac{1}{τ}$, $\left[s\right]=\frac{1}{s} o baudio$

### Capacidad de un canal y velocidad de información

La **capacidad** de un canal es su capacidad de transportar información. Se mide en bits/seg. y una fuente con tasa de información promedio R, si $R<C$ existe una codificación tal que la salida de la fuente puede ser transmitida sobre el canal con una frecuencia arbitrariamente pequeña de error, a pesar de la existencia de ruido. Si sucediera que $R > C$ no sería posible transmitir sin error.

El **ancho de banda** se refiere a la gama de frecuencias dentro de un sistema de comunicación que puede ser utilizada para transmitir información. En otras palabras, es la diferencia entre la frecuencia más alta y la frecuencia más baja de una señal. Cuanto mayor es el ancho de banda, mayor cantidad de datos puede ser transmitida en un período de tiempo dado. En el contexto de las señales electrónicas, un ancho de banda más amplio permite una mayor velocidad de transmisión de datos. Se mide en hertzios (Hz).

# Codificación

*Nota: De esta parte voy a hacer un repaso breve de conceptos que podrían entrar. No hay práctica por ende no voy a poner casi fórmulas.*

## Código

Definición: Si denominamos $S = (s\_{1}; s\_{2}; ..........; s\_{q})$ al conjunto de símbolos de un alfabeto dado; queda definida una codificación al poner en correspondencia todas las secuencias posibles de símbolos de S con secuencia de símbolos de algún otro alfabeto $Z = (z\_{1}; z\_{2}; ...........; z\_{r})$. Entonces “S” recibe el nombre de **alfabeto fuente** y “Z” **alfabeto código**.

## Código Bloque

Es aquel que asigna a cada uno de los símbolos del código fuente S una secuencia fija de símbolos del alfabeto código Z. Estas **secuencias** fijas (secuencias Zj) reciben el nombre de palabras código.

## Código no-singular

Es aquel en que todas sus palabras son distintas

## Códigos unívocamente decodificables

Se dice que un código es unívocamente decodificable si a cualquier secuencia de palabras código, le corresponde una y sólo una secuencia de símbolos de la fuente.

Por lo que podemos dar otra definición de código unívoco: Un código bloque se dice unívocamente decodificado sí y solo sí su extensión de orden n es no singular para cualquier valor finito de n.

### Códigos coma

Este nombre se debe a que el comienzo o el fin de cada palabra está señalizada por un cero o por un uno.

## Códigos instantáneos

Código Instantáneo es todo Código Unívoco cuyas palabras códigos pueden ser decodificadas **ni bien se reciben** sin esperar la llegada de la próxima palabra código.

Para que un código sea instantáneo, ninguna palabra código debe ser prefijo de otra palabra código.

## Inecuación de Kraft

![](data:image/png;base64...)

Básicamente la inecuación dice que de cumplirse, existe algún código instantáneo de $r$ símbolos en su alfabeto y cuyas q palabras códigos tienen las longitudes

| *Nota*: el teorema no dice que cualquier código cuyas longitudes cumplan la condición es un código instantáneo. |
| --- |

## Longitud media

Dado un código bloque que asocia los símbolos de una fuente $S\_{1}; S\_{2}; .......; S\_{n}$ con las palabras $Z\_{1}; Z\_{2}; .........; Z\_{n}$ y las probabilidades de los símbolos son$P\_{1}; P\_{2}; .....; P\_{n}$. La longitud media del código L se define como:

$L\_{med}=\sum\_{}^{}P\_{i} . l\_{i}$

Desde el punto de vista económico nos interesan aquellos códigos en que la longitud es mínima.

### Cota inferior de la longitud media

Este teorema expresa el límite inferior de la longitud media que es igual o mayor a la Entropía r-aria de la fuente.

Teorema: La longitud media de un código es mayor o igual que la entropía de la fuente dividida por el log2 del número de símbolos del alfabeto código.

$\frac{H(s)}{lg r} \leq L$

Luego, se llama a la entropía de la fuente dividida por el $log\_{2}$ del número de símbolos del alfabeto del código como **entropía n-aria**, quedando:

$H\_{r}(s) \leq L$

Expresa que nunca podremos obtener un código cuya longitud media sea menor que la Hr(s) (entropía en unidades r-arias).

# Códigos lineales

## Código bloque

Se dice que un código es un código de bloqueo cuando sus palabras códigos tienen longitud constante, es decir $l\_{i}=n$ para todo i.

## Espacio Nulo

## Síndrome

Se define **el síndrome** de una palabra código como el producto del vector asociado por la matriz de control de paridad transpuesta.

Es el resultado de multiplicar una palabra con error por la matriz de control de paridad transpuesta.

Se utiliza para corregir errores. Si el síndrome es cero, ésta corresponde al grupo. Si es ≠ de cero, el mensaje tiene algún error.

En la familia de errores asociada a cada síndrome se pueden observar sólo los errores simples y dobles de las palabras códigos asociadas a ese síndrome.

# Baro

## Sistema de comunicación

![](data:image/png;base64...)

* **La fuente** genera Información (mensajes a transmitir), es decir, es de donde parte la información.
* **Transductor de entrada y salida**: permite realizar la *adaptación* de las señales (mensajes) de entrada y salida, tal que el sistema pueda ser manejado por el hombre. Esto es necesario porque el emisor y el receptor son dispositivos que trabajan con señales eléctricas, mientras que las entradas y las salidas normales no lo son (acústicas, visuales, alfanuméricas)
* **Sistemas de emisión y recepción**: permiten adaptar las señales entregadas por el transductor de entrada al canal mediante el emisor o transmisor, y luego convertirlas en señales útiles al transductor de salida a través del receptor. Esta adaptación se realiza cambiando los niveles de potencia de la señal, su frecuencia e incluso, en algunos casos, su forma de onda.
* El **transmisor** en el transmisor se lleva a cabo la modulación de la señal a transmitir. Modular significa hacer un corrimiento en frecuencia. Consta de tres partes o etapas: **filtrado,** **procesamiento de la señal** y **amplificación**. Una de las razones por la que se modula es para adaptar la señal a transmitir al medio (canal).
* El **canal** representa el enlace entre un emisor y su correspondiente receptor, es decir, es el camino por el cual se envía la información.
* El **destino** es a donde enviamos la información
* El **receptor**, es el encargado de **demodular** la señal que recibe a través del canal. El procesamiento de **demodulación** requiere que el receptor sea lo suficientemente *sensible* y *selectivo* como sea posible.
* **Perturbaciones**: es una alteración y/o molestia que se introduce al canal y afecta la señal transmitida. Las mismas pueden ser de tres tipos: distorsión, interferencia o ruido. Las dos primeras, teóricamente se pueden eliminar, mientras que el ruido no.
  + ***Distorsión:*** altera la amplitud de la señal que viaja por el canal. Generada por el canal, debido a la atenuación no constante.
  + ***Interferencia***: tiene que ver con toda señal parecida a la que se transmite y que se mete en el canal de transmisión. Es la contaminación por señales extrañas con formas similares a la de la señal original y cuyo origen es generalmente artificial. Teóricamente, la interferencia al igual que la distorsión ***pueden ser eliminadas***.
  + ***Ruido***: es toda señal que tiene un comportamiento aleatorio (impredecible), independientemente de la señal, y es inevitable. Lo único que puedo hacer es mejorar la relación señal a ruido (S/N). Esto se logra aumentando la calidad de la señal a transmitir. Además, en cuanto al ruido éste no puede ser eliminado nunca completamente, ni aún en teoría.

## Atenuación y Ganancia

Se define la **ganancia** como el cociente entre la magnitud de salida de un sistema y la correspondiente magnitud de entrada:

$Ganancia=\frac{Salida}{Entrada}$

$E.g.: G\_{V}=\frac{V\_{0}}{V\_{f}}, G\_{P}=\frac{P\_{0}}{P\_{f}}, G\_{I}=\frac{I\_{0}}{I\_{f}}$

Por su parte, llamamos **atenuación** al cociente entre la magnitud de entrada de un sistema y la salida; es decir la inversa de la ganancia:

$Atenuación=\frac{Entrada}{Salida}=\frac{1}{Ganancia}$

Utilizando esta información sabemos que teniendo la atenuación, es posible calcular la ganancia y viceversa. De hecho, si tuviéramos la información respecto al valor de la atenuación o ganancia y el valor de la magnitud de entrada o de salida, podríamos calcular el restante.

**Importante**: Tanto la ganancia como la atenuación, **NO** tienen unidad. Se miden en ‘veces’

Si tuviéramos un sistema conformado por dos componentes conectados en serie, ambos con atenuación de 10 veces. Y midieramos la atenuación del sistema, nos daría como resultado 100 veces, que es el resultado de ***multiplicar***las atenuaciones respectivas a cada componente

### Unidad de transmisión

Si quisiéramos calcular ya sea la ganancia o la atenuación en decibeles, deberíamos aplicar la fórmula:

$A\_{H\_{db}}=10 . log\_{10}(A\_{H})$

O, en el caso de la ganancia:

$G\_{db}=10 . log\_{10}(G)$

## Velocidad de transmisión y velocidad de modulación. El BIT

Se define el BIT como la cantidad de información que posee la aparición de un elemento de código alfabeto binario y es la unidad de información.

Para un alfabeto n-ario, la cantidad de información producida por la aparición de un carácter será I = log2 n (logaritmo de n en base 2).

### Velocidad de información y de señalización

Se denomina velocidad o tasa de información (**R**) a la cantidad de bits en promedio, que se transmite en 1 segundo. Esto es, la cantidad de información promedio producida por una fuente en un segundo

$[R]: bits por segundo (bps) en promedio, de información$

Se denomina velocidad o tasa de dígitos o binits (**r**), a la cantidad de dígitos por segundo transmitidos

$[r]: dígitos por segundo transmitidos (de información o no)$

Se denomina velocidad de señalización (**s**), a la inversa del tiempo mínimo que dura un pulso

$s= \frac{1 }{τ\_{min}} / [s] : 1/seg ó baudios$

## Capacidad de un canal y velocidad de información

La capacidad de un canal es su capacidad de transportar información, es decir, la cantidad de información que puede ser relativamente transmitida sobre un canal de comunicación.

Se mide en **bits/seg** (bps) y como veremos luego, depende de su ancho de banda y de la relación señal/ruido (S/N)

Además, es importante tener en cuenta, que la capacidad del canal también depende de *la naturaleza del medio*; la fibra óptica, cobre, etc. tienen un límite

Sea una fuente de información con tasa **R** (*bits/seg*). Si **R < C** (capacidad del canal), existirá una codificación tal que la salida de la fuente podrá ser transmitida sobre el canal con una frecuencia arbitrariamente pequeña de error, a pesar de la existencia del ruido. Si R > C no es posible transmitir sin error.

## Rango dinámico

El rango dinámico es la diferencia entre el nivel máximo que un dispositivo puede emitir y el nivel de ruido existente cuando no hay señal (de fondo). Cuanto mayor sea este rango, más ‘limpia’ será la comunicación.

En una cadena de varios dispositivos de audio (emisor, amplificador, parlante, etc.) el *valor real*, es decir, el mayor rango dinámico que se pueda apreciar corresponde al del dispositivo con peores características. En aparatos de calidad, el rango dinámico aceptable es [80; 95] db.

## Relación señal Ruido

Es el cociente entre la potencia relacionada a la señal y la potencia relacionada al ruido.

Siendo, S la potencia relacionada a la señal (**S**ignal en inglés) y N la potencia relacionada al ruido (**N**oise en inglés), nos queda:

$\frac{S}{N}=\frac{P\_{señal}}{P\_{ruido}}$

$[\frac{S}{N}]=db=decibel$

## Transmisión multinivel

Se denomina transmisión multinivel a aquella en la que el número de niveles que puede tomar una señal es mayor a 2.

Se supone un mensaje de duración T compuesto por pulsos de duración τ. Resultará r = s. Los pulsos podrán tener μ niveles distintos. La longitud del mensaje (cantidad de pulsos) será T.

![](data:image/png;base64...)

La longitud del mensaje (cantidad de pulsos) será T

*¿Cuál será la cantidad de símbolos distintos que pueden representarse?*

Esta cantidad resulta igual a los μ niveles.

*¿Pero qué cantidad de mensajes distintos pueden transmitirse?*

Esta cantidad será la cantidad de posibilidades de combinación en Tseg, esto es:

$M\_{(T)}=μ^{T/τ}$

Luego, la cantidad de bits de información será:

$I = lg M(T)$

Para obtener R basta dividir por T, y con ello se halla la tasa de información (R) en bits/seg.

$R = \frac{I}{T} = \frac{1}{T}⋅lg M(T) = \frac{1}{T}⋅lg μ\frac{T}{τ} = \frac{1}{τ}. lg μ$

Si $τ = τ\_{min} => 1/ τ = s => R = s . lg μ$

## Detección y corrección de errores

$m = Cantidad de bits de Ix$

$n = Cantidad de bits de control$

Para averiguar **n** debemos plantear la siguiente inecuación e ir probando:

$$

$2^{n} \geq m+n+1$

Por ejemplo, dado un $m=4$ y $n=3$

$2^{2}=4\geq 4+2+1=7$

como no se cumple, probamos con un número más grande:

$2^{3}=8\geq 4+3+1=8$, si, por ende $n=3$

### Por diagramas de Venn

A través de diagramas de Venn podríamos graficar esto de la siguiente manera:

![](data:image/png;base64...)

* $I: C\_{1}⊕i\_{0}⊕i\_{1}⊕i\_{2}=0$
* $II: C\_{2}⊕i\_{0}⊕i\_{1}⊕i\_{3}=0$
* $III: C\_{3}⊕i\_{0}⊕i\_{2}⊕i\_{3}=0$

### Método analítico

$m = 4$

$n = 3$

![](data:image/png;base64...)

$C\_{i}=2^{x}(posición)$

* $1°⇒C\_{1}=2^{0}\rightarrow 00$$1$
  + $11$$1$$=7°\rightarrow i\_{3}$
  + $01$$1$$=3°\rightarrow i\_{0}$
  + $10$$1$$=5°\rightarrow i\_{1}$
    - $I: C\_{1}⊕i\_{0}⊕i\_{1}⊕i\_{2}=0$
* $2°⇒C\_{2}=2^{1}\rightarrow 010$
  + $1$$1$$1=7°\rightarrow i\_{3}$
  + $0$$1$$1=3°\rightarrow i\_{0}$
  + $1$$1$$0=6°\rightarrow i\_{2}$
    - $II: C\_{2}⊕i\_{0}⊕i\_{1}⊕i\_{3}=0$
* $3°⇒C\_{3}=2^{2}\rightarrow 100$
  + $1$$1$$1=7°\rightarrow i\_{3}$
  + $1$$0$$1=5°\rightarrow i\_{0}$
  + $1$$00=4°\rightarrow i\_{2}$
    - $III: C\_{3}⊕i\_{0}⊕i\_{2}⊕i\_{3}=0$