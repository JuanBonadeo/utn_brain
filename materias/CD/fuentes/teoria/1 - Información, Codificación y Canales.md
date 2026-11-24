Comunicaciones -
IIInnnfffooorrrmmmaaaccciiióóónnn,,, CCCooodddiiifffiiicccaaaccciiióóónnn yyy CCCaaannnaaallleeesss
–
Ingeniería en Sistemas de Información
1 Introducción
El objetivo del pte. estudio es medir la Cantidad de Información que
contiene (lleva) un determinado suceso o mensaje.
Hasta ahora la información tenía un valor cualitativo como ser precisa, estar
en tiempo y forma disponible para la toma de decisiones, etc. Ahora bien si
la información debe ser transmitida se debe cuantificar a fin de poder
dimensionar el medio por el cual va a ser transmitida
Entonces para cuantificar la cantidad de información que aporta un suceso o
mensaje debemos pensar qué función la puede representar, en principio
vemos que un suceso cualquiera nos aporta más información cuanto menos
certidumbre tengamos de dicho suceso, es decir si sabemos que un suceso
va a ocurrir no nos trae mucha información en cambio si ocurre algo que no
se espera la cantidad de información que aporta dicho suceso es mayor,
recordemos que la certidumbre o incertidumbre de ocurrencia de un suceso
no es más que la probabilidad de ocurrencia de dicho suceso, entonces la
Cantidad de Información I que aporta un suceso A es función
(A)
inversa de la probabilidad de ocurrencia de ese suceso es decir de la p
(A)
I = función 1/ p
(A) (A)
Esta función de la probabilidad debe cumplir las siguientes tres condiciones:
-Para un suceso del cual tenemos total certidumbre de ocurrencia (p =1)
(A)
la cantidad de información I que trae es cero, es decir
(A)
Dado el suceso A con p =1 ===> la Cant. de Inf. es cero -I = 0
(A) (A)
-Para un suceso del cual tenemos la certidumbre de ocurrencia es muy
baja, la cantidad de información que trae es muy alta, es decir
Dado el suceso A con p 0 ==> la Cant. de Inf. es muy elevada I ->∞
(A) (A)
-Para dos sucesos independientes A y B cada uno con su respectiva
probabilidad de ocurrencia p y p , donde A trae cantidad de
(A (B)
información I y B trae cantidad de información I
(A) (B)
Resulta que la probabilidad del suceso conjunto es p = p p
(A.B) (A) * (B)

Comunicaciones -
IIInnnfffooorrrmmmaaaccciiióóónnn,,, CCCooodddiiifffiiicccaaaccciiióóónnn yyy CCCaaannnaaallleeesss
–
Ingeniería en Sistemas de Información
Así mismo la Información del suceso conjunto es la suma de las
Informaciones I = I + I
(A.B) (A) (B)
Por lo tanto, la única función que en 1 es cero, en cero tiende a infinito y
transforma un producto en una suma es la función logaritmo, y en particular
como trabajamos con mensajes binarios usaremos el logaritmo en base 2
cuya unidad de medida será el “bit” reservando por ahora el término “Binit”
para el dígito binario.
Entonces dado un suceso A con probabilidad de ocurrencia p la Cantidad
(A) ,
de Información I que aporta ese suceso es :
(A)
I = lg 1/ p = (Bit) ó también I = - lg p
(A) 2 (A) (A) 2 (A)
Observación:
Recordando que la función logaritmo (decimal) de un número es el exponente
al que hay que elevar la base (10) para obtener el número:
log N = X  10X = N
De igual manera para el logaritmo en base 2 que nos ocupa:
Lg N = X  2X = N
2
Aplicando logaritmo en base 10 a esta última expresión
Log 2X = log N  X.log 2 = log N  X = log N/log2
o sea lg N = log N /log 2 ~ 3.32 log N
2
Mismo análisis se puede hacer partiendo del logaritmo Neperiano (en base
e), es decir
lg N = ln N /ln 2
2

Comunicaciones -
IIInnnfffooorrrmmmaaaccciiióóónnn,,, CCCooodddiiifffiiicccaaaccciiióóónnn yyy CCCaaannnaaallleeesss
–
Ingeniería en Sistemas de Información
1.2 Entropía, Fuente y Canal
En la formación de la teoría, encontramos una magnitud que cumple con las
especificaciones que se le imponen a la medida de la información y que por tener una
expresión formal mente idéntica a la que posee la magnitud termodinámica conocida
como “entropía”, se la conoce con el mismo nombre.
1.2.1 Modelos aleatorios univariados
El modelo aleatorio univariado es un modelo probabilístico del comportamiento
de una fuente de información o de un receptor de la misma.
Nuestro universo de sucesos elementales estará constituido por símbolos de la
fuente, xi (binario, etc.).
De acuerdo a las características de los símbolos se le asigna a cada uno su
probabilidad de ocurrencia.
Tenemos así una caracterización univariada, esto es unidimensional, de la
fuente.
Su representación es:
Función que provea una magnitud que represente la cantidad de información
asociada al suceso que representa la aparición de un símbolo de la fuente. Se propone:
donde:
I(x) es la cantidad de información asociada al suceso x
i j
p(x) es la probabilidad de ocurrencia del suceso x.
i i
OBSERVACIÓN: Centraremos el estudio en fuentes ergódicas
(probabilidad de los símbolos independiente del tiempo) y fuentes de
memoria nula

Comunicaciones -
IIInnnfffooorrrmmmaaaccciiióóónnn,,, CCCooodddiiifffiiicccaaaccciiióóónnn yyy CCCaaannnaaallleeesss
–
Ingeniería en Sistemas de Información
INTRODUCCIÓN:
Supongamos que tenemos una fuente S que emite tres símbolos R, A, y V
y que una muestra significativa es la siguiente:
S
….R R A A A V A A R R ……
Cada símbolo al aparecer nos dará una cantidad de información dada I ,
(A)
I e I
(V) (R)
Si pretendemos tener la cantidad de Información promedio será:
Cant.Inf. Prom = N .I + N .I + N .I
(A) (A) (V) (V) (R) (R)
N
N es el número total de la muestra
Ahora bien cada cociente N /N = fr = P
(i) i (i)
fri es la frec. relativa del símbolo i
P es la probabilidad de ocurrencia del símbolo i y por ser una muestra
(i)
significativa se puede igualar a la frecuencia relativa
Por lo tanto, la Cantidad de Información promedio que emite una fuente
será:
∑ ∑
H (S) = p . lg 1/p = - p . lg p
i i i i
ENTROPÍA DE LA FUENTE
Para una caracterización univariada denominamos “entropía” – y la notamos H(x) – a la
esperanza matemática de la información por símbolo de la fuente, esto es:
La función entropía tiene su máximo valor, para un determinado número de
símbolos fuente, cuando estos son equiprobables.

Comunicaciones -
IIInnnfffooorrrmmmaaaccciiióóónnn,,, CCCooodddiiifffiiicccaaaccciiióóónnn yyy CCCaaannnaaallleeesss
–
Ingeniería en Sistemas de Información
1.2.2- Modelos aleatorios bivariados
Se puede definir un canal de información como determinado por un alfabeto de
salida B = (bj), J = 1, 2, 3, ........, s; y un conjunto de probabilidades condicionales
p(bj/ai) siendo esta la probabilidad de recibir a la salida el símbolo bj cuando se envía el
símbolo de entrada a.
i
RUIDO
P (b/a)
j i
a b
1 1
FUENTE RECEPTOR
a b
2 2
a b
3 3
CANAL
Puede Representarse esquemáticamente:
Un canal sin memoria queda descripto por medio de la matriz de
probabilidades condicionales siguiente:
donde Pij = P(bj/ai)
Cada fila de la matriz corresponde a una entrada del canal y cada columna a una
salida.
A un canal se lo denomina transparente cuando no introduce error, esto es si, su
matriz de probabilidades condicionales es diagonal.
Un canal de importancia teórica es el binario simétrico (BSC). Este canal posee dos
símbolos de entrada (a1 = 0, a2 = 1) y dos de salida (b1 = 0, b2 = 1). Es simétrico por

Comunicaciones -
IIInnnfffooorrrmmmaaaccciiióóónnn,,, CCCooodddiiifffiiicccaaaccciiióóónnn yyy CCCaaannnaaallleeesss
–
Ingeniería en Sistemas de Información
ser iguales las probabilidades de recibir un cero al enviar un uno y viceversa. Esta
probabilidad se denomina probabilidad de error (p).
p = p
(bj/ai)
a b
1 1-p 1
a b
2 2
Dado un canal definido por los símbolos de entrada y salida y una matriz de
probabilidades condicionales P. Considerando la probabilidades de los símbolos de
entrada p(a), i = 1, 2, ........., r y la matriz de probabilidades condicionales del canal (p),
i
se puede determinar otro conjunto de probabilidades p(b), j = 1, 2, ........, s que
j
representa la probabilidad de aparición del símbolo b a la salida del canal.
j
Cabe destacar que conociendo las probabilidades de salida y la matriz de
probabilidades condicionales, en general no pueden calcularse las probabilidades de
entrada.
Se verán las llamadas probabilidades hacia atrás, esto es, p(a/b) que significa la
i j
probabilidad de que habiéndose dado b a la salida, provenga de un a a la entrada del
j i
canal. Según Bayes:
El numerador de la expresión (4), es la probabilidad del suceso (a, b), es decir la
i j
probabilidad conjunta de la aparición de a a la entrada y b a la salida.
i j
Entonces:
P(ai) * P(bj/ai) = P(bj) * P(ai/bj)
Por lo tanto se puede calcular la incertidumbre de un símbolo de entrada dado un
símbolo a la salida
P(ai/bj) = P(ai) * P(bj/ai) / P(bj)
Se puede luego, obtener una matriz de probabilidades conjunta P(A,B).
La caracterización bivariada del sistema, se da:
La incertidumbre de aparición en el sistema, la información media al emitir a y
i
recepcionar b – Se denomina entropía del sistema:
j

Comunicaciones -
IIInnnfffooorrrmmmaaaccciiióóónnn,,, CCCooodddiiifffiiicccaaaccciiióóónnn yyy CCCaaannnaaallleeesss
–
Ingeniería en Sistemas de Información
Se denomina P(a) a la probabilidad a priori de los símbolos de entrada. Y a
i
P(a/b) se la denomina probabilidad a posteriori, por ser esta la probabilidad del
i j
símbolo, luego de sucedido b. Es posible calcular la entropía del conjunto de símbolos
j
de entrada según ambas probabilidades.
Así la entropía a priori será:
∑
H(A) = p(ai) * lg 1/p(ai)
i
y la entropía a posteriori:
∑
H (A/B) = P(bj) * P(ai/bj) * lg P(ai/bj)
∑
H (A/B) = - P(bj) * P(ai/bj) * lg P(ai/bj)
i j
Como los símbolos a la salida presentan una probabilidad P(b) es posible
j
calcular la entropía media a posteriori como
esto no es más que la entropía de la fuente conociendo la recepción
(equivocación de A respecto de B).
Como se conoce la P(bj/ai) que caracteriza al canal, en forma similar se obtiene
la entropía del canal (equivocación de B respecto de A).

Comunicaciones -
IIInnnfffooorrrmmmaaaccciiióóónnn,,, CCCooodddiiifffiiicccaaaccciiióóónnn yyy CCCaaannnaaallleeesss
–
Ingeniería en Sistemas de Información
∑
H (B/A) = - P(ai) * P(bj/ai) * lg P(bj/ai)
i j
1.3- Información Mutua.
La información mutua es la información transferida desde la fuente al receptor a
través del canal, esto es, la información real que llega al receptor en promedio.
Analizando la ecuación (3) se observa que ella representa la incertidumbre con
respecto a la fuente luego de recepcionar un símbolo bj. Al promediarla a todo el
alfabeto de salida (según –9- ) resulta la información promedio (de la fuente) que
bloquea el canal. Luego para calcular la información promedio real recepcionada
bastará obtener la diferencia entre la entropía a priori y la equivocación de A respecto a
B.
Una importante propiedad de la información mutua es la simetría con respecto a
las variables de entrada y salida, entonces es valido decir que:
I(A, B) = I(B, A) = H(B) – H(B/A) ( 12 )
En el caso de canales transparentes:
H(A) = H(B) = H(A, B) = I(A, B)
H(A/B) = H(B/A) = 0
1.4- Capacidad y eficiencia de Canales.
1.4.1- Capacidad
Supuesto un canal de alfabeto de salida B y probabilidades condicionales P(b/a)
j i
la información mutua resulta:
ya que:

Comunicaciones -
IIInnnfffooorrrmmmaaaccciiióóónnn,,, CCCooodddiiifffiiicccaaaccciiióóónnn yyy CCCaaannnaaallleeesss
–
Ingeniería en Sistemas de Información
Analizando la expresión (13) se nota que I(A, B) depende de la probabilidad de
los símbolos de entrada y de las características del canal. Entonces para un canal
determinado se estudia la variación de la información mutua en función de las
probabilidades de entrada.
Con el solo hecho que la probabilidad de entrada de un símbolo sea 1, la
información mutua será nula. Es decir que el valor mínimo I(A, B) es creo.
Quedaría ahora analizar el valor máximo de la misma, este valor es posible
lograrlo sintonizando la fuente que provee los símbolos de entrada al canal. Este valor
máximo es lo que se denomina capacidad del canal, simbolizándola con C.
(*) Se a introducido dentro de la sumatoria sobre j la expresión de la H(A), esto
es posible ya que ella es independiente de ese subíndice. Ahora, si reemplazamos P(ai)
por P(ai, bj) la expresión no cambia ya que al sumar sobre todos los símbolos de la
salida (cuando se realiza la sumatoria sobre j) resulta P(ai) nuevamente.
(**) Es válido ya que P(ai/bj) P(bj) = P(ai, bj).
La capacidad de un canal será función exclusivamente de las probabilidades
condicionales y no dependerá de la probabilidades de los símbolos de entrada.
En los canales transparentes H(A/B) = 0 y resulta:
I(A, B) = H(A) – H(A/B) = H(A)
entonces:
C = max H(A)
Si la fuente resultara equiprobable (caso de máxima entropía) y emitiera un
símbolo:
H(A) = lg n (bit/simb)
C = lg n (bit/simb)
Notar que si n aumenta, la capacidad sube, lo cual es lógico ya que el canal no
bloquea la información por es transparente.
Para una fuente binaria equiprobable:

Comunicaciones -
IIInnnfffooorrrmmmaaaccciiióóónnn,,, CCCooodddiiifffiiicccaaaccciiióóónnn yyy CCCaaannnaaallleeesss
–
Ingeniería en Sistemas de Información
resulta C = lg 2 = 1 bit/simb
La capacidad puede expresarse también, en unidades b.p.s. (bit/seg.). Esto
proviene de que si cada símbolo dura  seg., y estamos en el caso binario equiprobable
la capacidad C resulta:
C = 1/ b.p.s.

1.4.2- Eficiencia
Se define a eficiencia de transmisión para cada canal y fuente, a:
FF = I(A, B) / C ( 16 )
Y redundancia de transmisión a:
RED = 1 - FF
Esta redundancia es la parte no aprovechada de la capacidad portánte de
información del canal.
1.5- Otros Conceptos Fundamentales
1.5.1- Velocidad de información y señalización
Se denomina velocidad o tasa de información (R), a la cantidad de bits en
promedio que se transmiten en 1 segundo, esto es, la cantidad de información promedio
producida por una fuente en 1 (un) segundo.
R = H’(A)
Si se considera un canal con ruido, a la salida se tiene una tasa de información
de:
R = H’(A) - H’(A/B)
Se denomina velocidad o tasa de dígitos o binits (r) a la cantidad de dígitos por
segundo transmitidos.
Como la entropía es la información promedio (o bits por símbolos en promedio
-H), resulta:
R = r H(A)
R y H son dos formas de medir información promedio, una en bits por segundos
y otra en bits por símbolo.

Comunicaciones -
IIInnnfffooorrrmmmaaaccciiióóónnn,,, CCCooodddiiifffiiicccaaaccciiióóónnn yyy CCCaaannnaaallleeesss
–
Ingeniería en Sistemas de Información
Se denomina velocidad de señalización (s) a la inversa del tiempo mínimo que
dura un pulso.
s = 1/ 1/seg. ó baudios
min
1.5.2- Capacidad de un canal y velocidad de información
La capacidad de un canal es su capacidad de transportar información. Se mide en
bits/seg. y una fuente con tasa de información promedio R, si R  C existe una
codificación tal que la salida de la fuente pude ser transmitida sobre el canal con una
frecuencia arbitrariamente pequeña de error, a pesar de la existencia de ruido. S R > C
no es posible transmitir sin error.
Se supone de duración T compuesto por pulsos de duración , resulta r = s, esto
es, la cantidad de pulsos por segundo transmitidos es el máximo para un cierto s. Los
pulsos pueden tener  niveles distintos.
Es posible preguntarse, ¿Cuál será la cantidad de símbolos distintos que podrán
representarse?. Esta cantidad resulta igual a los  niveles. ¿Pero que cantidad de
mensajes distintos pueden transmitirse?. Esta cantidad será igual al número de
posibilidades de arreglos con repetición en T segundos.
M(T) = n Si todos los pulsos son de inf.y de igual duración n = T/ τ
Si son equiprobables se tiene la máxima cantidad de información, la cual resulta:
P(M) = 1/
M(T)
luego:
I = lg M(T)
Para obtener R basta con dividir por T, con ello se halla la tasa de información,
R, en bits por segundos. No es necesario calcular la entropía, ya que al ser
equiprobables coincide con I.
Entonces el calculo de R es:
R = I/ lg M(T) = 1/ lg n
T T
R = 1/  lg  (solo si todos los pulsos son de inf.y de igual duración)

| Comunicaciones  -   | IIInnnfffooorrrmmmaaaccciiióóónnn,,,   CCCooodddiiifffiiicccaaaccciiióóónnn   yyy   CCCaaannnaaallleeesss –  |     |
| ------------------- | ------------------------------------------------------------------------------------------------------------ | --- |
Ingeniería en Sistemas de Información

| Si    =   | luego    1/ | =  s   |
| ----------- | ----------- | ------ |
| min         |             |       |

  Si son sucesos equiprobables y   =   , entonces R es máximo y deberá ser C
min
=  R . Esto es, el canal deberá tener una capacidad al menos igual a R. Si el sistema es
max
binario, la cantidad de niveles será , lo que implica una capacidad de canal coincidente
con la de señalización.

|     |   C  =  s  |     |
| --- | ---------- | --- |

  La velocidad de señalización está ligada con una caracteristica del canal que se
denomina ancho de banda, B. Este valor resulta:

|     |   B  =  s/2  |     |
| --- | ------------ | --- |

  Ensayando el canal el ancho de banda resulta aproximadamente igual al valor
para el cual la relación entre la salida y la entrada disminuye una determinada cantidad.