DETECCION DE ERRORES
DISTANCIA DE UN CÓDIGO
Supongamos un código binario de 3 Dígitos => un   => 23 = 8 Palabras Códigos
000      La Distancia de un código  es la cantidad de dígitos (Binits) que cambian entre
001
| 010    |   dos palabra del código. Ejemplo:     |     |     |     |     |     |     |
| ------ | -------------------------------------- | --- | --- | --- | --- | --- | --- |
| 011    |   Dist. entre 100 y 101 es d=1         |     |     |     |     |     |     |
| 100    |   Dist. entre 000 y 011 es d=2         |     |     |     |     |     |     |
| 101    |   Dist. entre 011 y 100 es d=3         |     |     |     |     |     |     |
110
111
DISTANCIA MÍNIMA DE UN CÓDIGO
Es la menor cantidad de dígitos que cambian entre dos palabras del mismo código.
En nuestro caso dmin = 1
Entonces si al transmitir una palabra código y por efecto de ruido se cambia uno de los dígitos la
palabra código se convierte en otra palabra del mismo código => ERROR
Si se transmite la palabra 100  y se recibe la palabra 101  que también pertenece al código no es
posible detectar el error
Por lo tanto si se pretende detectar un error simple en la palabra código que se recibe se deberá
aumentar la Distancia Mínima del Código
BIT DE PARIDAD
Una manera de aumentar la distancia mínima es agregar un dígito a la derecha que represente la
paridad par o impar de unos de la palabra código, es decir la nueva palabra tendrá una cantidad par o
impar de unos según:
I  I  I BP          BP = I + I +I + ......+ I I  I  I BP          BP = I + I +I + ......+ I  +1
| 2 1 0 | par 0  | 1  2  | n   | 2 1 0 | impar 0  | 1  2  | n   |
| ----- | ------ | ----- | --- | ----- | -------- | ----- | --- |
0 0 0 0  + : Suma sin acarreo    0 0 0 1  + : Suma sin acarreo
| 0 0 1 1  |     |     |     | 0 0 1 0  |     |     |     |
| -------- | --- | --- | --- | -------- | --- | --- | --- |
| 0 1 0 1  |     |     |     | 0 1 0 0  |     |     |     |
| 0 1 1 0  |     |     |     | 0 1 1 1  |     |     |     |
| 1 0 0 1  |     |     |     | 1 0 0 0  |     |     |     |
| 1 0 1 0  |     |     |     | 1 0 1 1  |     |     |     |
| 1 1 0 0  |     |     |     | 1 1 0 1  |     |     |     |
| 1 1 1 1  |     |     |     | 1 1 1 0  |     |     |     |

Ahora nuestro código si bien tiene 4 dígitos => un   => 24 = 16 Combinaciones , el código solo usa 8
palabras códigos. Las restantes 8 combinaciones que no se utilizan representan los errores, se dice
que esas combinaciones absorben el error simple.
Ejemplo:
Se transmite 1010 por un canal real:
|     |     | Ruido  |     |     |     |
| --- | --- | ------ | --- | --- | --- |
  TX         1 0 1 0                      1 0 1 0    RX   1 0 1 0
CANAL
|     |     |     |     |           BP |  =0  |
| --- | --- | --- | --- | ------------ | ---- |
par
                                               Iguales => Palabra OK “101”
            En el receptor se calcula nuevamente el bit de paridad
                                                       y se compara con el recibido

Se transmite 010 por un canal real:
|     |     | Ruido  |     |     |     |
| --- | --- | ------ | --- | --- | --- |
  TX         0 1 0 1                      0 1 1 1    RX   0 1 1 1
CANAL
|     |     |     |     |           BP |  =0  |
| --- | --- | --- | --- | ------------ | ---- |
par
|     |     |     |     |                                             |    No iguales => Palabra ERROR  |
| --- | --- | --- | --- | ------------------------------------------- | ------------------------------- |
|     |     |     |     | Se debe descartar y solicitar retransmitir  |                                 |
|     |     |     |     |                                             |                                 |
En el receptor se calcula nuevamente el bit de paridad
|     |     |     |     | y se compara con el recibido   |     |
| --- | --- | --- | --- | ------------------------------ | --- |
|     |     |     |     |                                |     |
Se transmite 1010 por un canal real:
|     |     | Ruido  |     |     |     |
| --- | --- | ------ | --- | --- | --- |
  TX         0 1 0 1                      0 1 0 0    RX   0 10 0
CANAL
|     |     |     |     |           BP |  =1  |
| --- | --- | --- | --- | ------------ | ---- |
par
|     |     |     |     |                                             |    No iguales => Palabra ERROR  |
| --- | --- | --- | --- | ------------------------------------------- | ------------------------------- |
|     |     |     |     | Se debe descartar y solicitar retransmitir  |                                 |
(Aunque la parte de Información está correcta no se
puede saber dónde está el error)

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

CÁLCULO DEL RENDIMIENTO Y LA REDUNDANCIA
Si consideramos que en el código original los mensajes son equiprobables resulta:
La cantidad de mensajes (palabra código) M= un = 23
La Probabilidad de uno de mensajes (palabra código) es p = 1 / M = 1/ un
(M)
Al ser equiprobables la cantidad de Información promedio (Entropía de la fuente) resulta igual a la
Información de un mensaje:
H(s) = I = lg 1/p = lg 1/ 1/M = lg M = lg un = lg 23 = 3 .lg2 = 3 bit
(M) (M)
La longitud promedio del código L = ∑ p . li
i
Pero como mensajes son equiprobables y el código es de longitud constante resulta
L = 3 binits
En este caso si calculamos el rendimiento Rend. = H/ L = 3/3 = 1 o sea un rendimIento del 100%
Y la redundancia Redun. = 1 – Rend. = 1 – 1 = 0 es decir el código resulta el de menor longitud
promedio y no tiene redundancia
Ahora si calculamos estos indicadores para el mismo código con bit de paridad para la detección de
errores simples resulta:
H(s) = I = lg 1/p = lg 1/ 1/M = lg un = lg 23 = 3 lg2 = 3 bit
(M) (M)
Ahora si bien también los mensajes también son equiprobables y el código es de longitud constante
pero ahora es:
L = 4 binits
Por lo tanto el rendimiento Rend. = H/ L = 3/4 = 0,75 o sea un rendimIento del 75%
Y la redundancia Redun. = 1 – Rend. = 1 – 0,75 = 0,25 , es decir hay una redundancia de 0,25
Lo cual se ve claramente ya que estamos usando cuatro bit para codificar ocho mensajes.
Esta baja en la calidad del código en cuanto a su rendimiento trae el beneficio de la detección de
errores simples.

CORRECCIÓN DE ERRORES SIMPLES
PARIDAD POR FILAS Y COLUMNAS
En este caso de arma un bloque de palabras códigos de la siguiente manera:
1001010
1010101
1100110
0100011
Y se agrega una columna y una fila de paridad par por ejemplo:
10010101
10101010
11001100
01000111
10110100

Se transmite el bloque al recibirlo se verifican la paridad de cada fila y cada
columna y se comparan
Bloque recibido        Bit Par generado p/fila en el Recepor         Comparación
| 10010101      |     |   1  |     |     |     |     | =   Fila Ok  |     |
| ------------- | --- | ---- | --- | --- | --- | --- | ------------ | --- |
| 10101010      |     |   0  |     |     |     |     | =   Fila Ok  |     |
=
| 11011100  |     |   1  |   Hay error en esta fila   |     |     |     | Fila c/error  |     |
| --------- | --- | ---- | -------------------------- | --- | --- | --- | ------------- | --- |
| 01000111  |     |   1  |                            |     |     |     | =   Fila Ok   |     |
| 10110100  |     |   0  |                            |     |     |     | =   Fila Ok   |     |

| 10100100  | Bit Par generado p/columna en el Recepor           |     |     |     |     |     |     |     |
| --------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
======== Comparación
         Hay error en esta columna

Por lo tanto el digito con error se encuentra en la intersección de la fila y
columna donde los bit de paridad recibidos y generados en el receptor No
coinciden.
Entonces la Información correcta es:
1001010
1010101
1100110
0100011
Es decir recuperada la información correcta los dígitos de paridad se descartan
Otro Ejemplo:
Bloque recibido Bit Par generado p/fila en el Recepor Comparación
10010101 1 = Fila Ok
10101011 0 Hay error en esta fila = Fila c/error
=
11001100 0 Fila Ok
01000111 1 = Fila Ok
10110100 0 = Fila Ok
10100101 Bit Par generado p/columna en el Recepor
======== Comparación
Hay error en esta columna
Por lo tanto el digito con error se encuentra en unos de los bit de paridad
Entonces la Información correcta es:
1001010
1010101
1100110
0100011
Nuevamente los dígitos de paridad se descartan

El inconveniente de este método es que se debe armar bloques de palabras
códigos, no corrige por palabra
PARIDAD POR ZONAS - CÓDIGO HAMMING
En este caso desarrollaremos “conceptualmente” Códigos Hamming
Consideremos una palabra código de cuatro dígitos I I I I
3 2 1 0
Consideramos tres zonas de control incluyendo un dígito de información en cada
intersección de zonas:
C1
I
1
C2
I
I 2
0
I
3
C3

Cada dígito de control será la paridad par del conjunto de dígitos de información
incluidos en su zona:
C1 = I + I + I
0 1 2
C2 = I + I + I
1 2 3
C3 = I + I + I
0 2 3
(Cada uno puede armar otras zonas dando por ende otras ecuaciones)
Observar que hay tres dígitos de información que impactan en dos zonas de
control respectivamente y el cuarto dígito de información impacta en las tres
zonas de control.
Ahora construimos el código completo identificando cada dígito:
I I I I C C C
3 2 1 0 3 2 1
0 0 0 0 0 0 0
0 0 0 1 1 0 1
0 0 1 0 0 1 1
0 0 1 1 1 1 0
0 1 0 0 1 1 1
0 1 0 1 0 1 0
0 1 1 0 1 0 0
0 1 1 1 0 0 1
1 0 0 0 1 1 0
1 0 0 1 0 1 1
. . . . . . .
. . . . . . .
. . . . . . .
1 1 1 1 1 1 1

Entonces si se transmite las palabras por un canal con ruido se pueden dar las
siguientes situaciones :
RUIDO
1 0 0 0 1 1 0 1 0 1 0 1 1 0
TX RX
CANAL
i I I I C C C
3 2 1 0 3 2 1
1 0 1 0 1 1 0
= = =
1 0 1
En el receptor genero nuevamente los dígitos de control y los comparo con los dígitos
de control recibidos
En este caso los dígitos que cambiaron fueron C1 y C2 y observando el diagrama el
dígito de Información común a ambos es I
1
Por lo tanto la información correcta es : 1000
Los dígitos de control se descartan una vez realizada el control y la corrección
Otro ejemplo:
RUIDO
0 1 1 1 0 0 1 0 1 1 1 1 0 1
TX RX
CANAL
i I I I C C C
3 2 1 0 3 2 1
0 1 1 1 1 0 1
= = =
0 0 1
Al estar sólo uno de los dígitos de control cambiados , el error no puede estar en
ninguno de los dígito de información, por lo que el error está en I y la información
3
correcta es : 0111 (Los dígitos de control se descartan efectuada la verificación).

Otro Ejemplo:
RUIDO
1 0 0 1 0 1 1 1 0 0 1 0 1 1
TX RX
CANAL
i I I I C C C
3 2 1 0 3 2 1
1 0 0 1 0 1 1
= = =
0 1 1
En este caso como todos los dígitos de control generados en el receptor son iguales a
1001
los recibidos , la palabra es correcta :
OBSERVACION:
El inconveniente del código Hamming es la de tener dos campos, uno para la
información y otro de control.
En nuestro ejemplo en total se transmiten 7 dígitos lo cual daría 27 = 128 palabras
posibles, pero el campo de información es solo de 4 digitos es decir solo se usan 16
palabras de Información. El campo de control no es información, solo se usa para el
control de errores simples.
Si queremos calcular su rendimiento considerando mensajes equiprobables:
H(s) = I = lg 1/p = lg 1/ 1/M = lg un = lg 24 = 4 lg2 = 4 bit
(M) (M)
(Sólo cuatro dig. de inf., I I I I )
3 2 1 0
Ahora si bien también los mensajes también son equiprobables y el código es de longitud constante
pero ahora es: L = 7 binits
Por lo tanto el rendimiento Rend. = H/ L = 4/7= 0,571 o sea un rendimIento del 57,1%
Y la redundancia Redun. = 1 – Rend. = 1 – 0,571 = 0,43 , es decir hay una redundancia de 0,43

CODIGOS LINEALES
n
Cómo se detalló anteriormente si bien un código de longitud constante de n dígitos y 2 palabras
equiprobables es compacto con un rendimiento del 100% tiene el inconveniente de que su distancia
mínima dm =1 con lo cual el error de un dígito en una palabra es decodificada como otra palabra del
mismo código, por lo tanto si necesitamos un código para la detección y/o corrección de errores
simples se debe aumentar la distancia mínima.
Antes de avanzar haremos un relación entre códigos y Espacios Vectoriales
n
Consideramos un Espacio Vectorial de n columnas y 2 filas con sus elementos binarios
n columnas
0000…000
0000…001
0000…010
E.V = …………… 2n filas
……………
1111….101
1111….110
1111….101
Como se necesita un código de n dígitos con posibilidad de detección y corrección de
errores simples se debe aumentar la distancia mínima tomado una cantidad menor de
palabras códigos (filas)
Esto significa considerar un Sub Espacio Vectorial
V
de n columnas y
2m
filas con m<n
n columnas
0101…010
S.E.V.= V= (..... x ……) 2m filas con m<n Filas = Vectores v
ij i
……vi……. Vector v (x x x x
i = i1 , i2….. ij… in)
1011….100 Siendo el elemento x = 0 ó 1
ij

Como todo espacio vectorial o sub-espacio vectorial tiene una base generadora:
n columnas
…………….
|     | G =       …… g ……     m  filas   con m<n      |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i

La condición para que G sea Base Generadora del SEV =V es que sus vectores sean
Linealmente Independientes, es decir que ninguno de los vectores  g resulte de la
i
combinación lineal de los restantes vectores de G y que además la combinación lineal
de todos los vectores de G debe generar el sub espacio vectorial V. Es decir:
g =  ∑  k x g para Todo j = i      Siendo k una constante que puede vale 0 ó 1
|     | i   | j   | j    |     |     |     |     | j   |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     | v  = k |  x g | + k |  x g |     | + K | x g |     |     |     |     |     |     |
| --- | ------ | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Es decir  cada vector de V es una
|     | i   | 1   | 1      | 2   | 2  ………. |     | m  m     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- |
combinación lineal de los vectores de G. La base NO ES UNICA, HAY MÁS DE UNA
Recordar que la suma + es suma sin acarreo.

Así mismo existe otro Sub Espacio vectorial que llamaremos V’ cuyas dimensiones son:

      n columnas
      0101…010
……)     2n-m  filas                       Filas = Vectores v’
| S.E.V.= V’=  |     |                |   (..... x |     |     |     |     |           |            |       |     |     |     |
| ------------ | --- | -------------- | ---------- | --- | --- | --- | --- | --------- | ---------- | ----- | --- | --- | --- |
|              |     |                |            | ij  |     |     |     |           |            | i     |     |     |     |
|              |     |                |            |     |     |     |     | Vector v’ | (x’        | x’    | x’  | x’  | )   |
|              |     |       ……vi…….  |            |     |     |     |     |           |            |       |     |     |     |
|              |     |                |            |     |     |     |     |           | i =  i1 ,  | i2….. | ij… | in  |     |
x’ = 0 ó 1
|     |     |       1011….100  |     |     |     |     |     |   Siendo el elemento  |     | ij  |     |     |     |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- |

Nuevamente todo espacio vectorial o sub-espacio vectorial tiene una base generadora:
n columnas
…………….
|     | H =       …… h ……     n-m  filas                    |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

La condición para que H sea Base Generadora del SEV =V’ es que sus vectores sean
Linealmente Independientes, es decir que ninguno de los vectores  h resulte de la
i

combinación lineal de los restantes vectores de H y que además la combinación lineal
de todos los vectores de H debe generar el sub espacio vectorial V’. Es decir:
| ∑   |     |      |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- |
h =  k x h para Todo j = i Siendo k una constante que puede vale 0 ó 1
| i j | j    |     |     | j   |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- |
v’  = k  x h +  h  x h + K x h Es decir  cada vector de V’ es una
| i 1 | 1     2 | 2  ………. | n-m  | n-m     |     |     |     |     |
| --- | ------- | ------- | ---- | ------- | --- | --- | --- | --- |
combinación lineal de los vectores de H. – Recordar  que la base no es única, se
puede elegir cualquiera que cumpla las condiciones..
Este Sub Espacio vectorial V’ resulta ortogonal al sub espacio vectorial V , es decir que
se cumple la siguiente condición:
Para todo v € V resulta    v x HT = 0          siendo HT la matriz transpuesta de H
| i   |     | i   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Para todo v’ € V’ resulta  v’ x GT = 0           siendo GT la matriz transpuesta de G
| i   |     | i   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Recordar que son productos de matrices (v
es una matriz de una sola fila) por lo tanto
i
la  propiedad conmutativa no aplica. Solo vale la propiedad asociactiva:
A , B y  C  matrices cualquiera
A x B = B x A
(A + B) x C = A x C + B x C
Dada una matriz A , la matriz AT resulta de cambiar filas por columnas.

 …………………………………………………………………………………………………………………….
Breve descripción de la nomenclatura utilizada:
En mayúscula espacios vectoriales:  V , V’ , G, H , GT  y HT
En minúscula con un subíndice: Vector i de un espacio vectorial: v , v’  , g’ , h
|     |     |     |     |     | i i | i i  |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- |
En minúscula con dos subíndices, es un elemento de un vector : v  , v’  , g h’
|     |     |     |     |     | ij ij | ij  ,  ij  |     |     |
| --- | --- | --- | --- | --- | ----- | ---------- | --- | --- |
K minúscula con un subíndice: Constante de valor 0 ó 1
Vamos a considerar la siguiente identificación  de los vectores:  v = (v ,v , …….v )
|     |     |     |     |     | i  i1  |   i2  |   in   |     |
| --- | --- | --- | --- | --- | ------ | ----- | ------ | --- |
………………………………………………………………………………………………………………………
APLICACIÓN A CÓDIGOS BINARIOS
Habiendo hecho el repaso de Algebra,  vemos de aplicar los visto a la transmisión de palabras
códigos por un canal con ruido

Consideremos un Código que llamaremos Código de Grupo V compuesto por
2m
palabras códigos
(vectores ó filas) n dígitos (n columnas)
n columnas
0101…010
V= (..... x ……) 2m palabras códigos (filas ) - con m<n Esto permite
ij
que V tenga una mayor distancia mínima
……v…….
i
1011….100
Si transmitimos una palabra código v por un canal con ruido:
i
RUIDO
v v
TX i i? RX
CANAL
La palabra v recibida no puede saberse si tiene error, entonces en el receptor podemos aplicar lo
i? ,
visto anteriormente, es decir si multiplicamos la palabra recibida por HT podemos concluir lo siguiente:
T
v x H = 0
=> Palabra Correcta ya que por la condición de ortogonalidad
i?
pertenece al Código de Grupo V
(ó error no detectable, esto lo veremos más adelante)
Si en cambio:
T
v x H = 0
=> Palabra CON ERROR ya que por la condición de ortogonalidad
i?
NO pertenece al Código de Grupo V
Por lo tanto se ha detectado un error simple sin necesidad de agregar dígitos de control, es
decir todos los dígitos son de información.
Ahora bien consideremos un par de palabras códigos pertenecientes a V y modelicemos el error con
una palabra que contenga todos ceros menos en la posición que pretendemos generar un error por
ejemplo e = 000100 (considerando que e € V )
a a

|  Entonces  sea  |     | v € V  | 101110   y  v |     | € V  | 111001     |     |
| --------------- | --- | ------ | ------------- | --- | ---- | ---------- | --- |
|                 |     | 1      |               |     | 2    |            |     |
 e 000100
y el  error modelizo esto mediante la suma sin acarreo  (+    ):
a
            v        101110                     v     111001
|     | 1   |     |     |     |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | +   |     |     | +   | +   |     |
+
            e        000100                     e      000100
|               | a    |                                  |     |     |     | a       |         |
| ------------- | ---- | -------------------------------- | --- | --- | --- | ------- | ------- |
|             v |      |     101010                     v |     |     |     |         | 111101  |
|               | 1ea  |                                  |     |     |     | 2ea     |         |
Entonces aplicamos la detección de errores vista anteriormente suponiendo recibir estas dos palabras
códigos con error en el cuarto dígito
|                                                    | T     |      | T        |     | T     |      | T    |
| -------------------------------------------------- | ----- | ---- | -------- | --- | ----- | ---- | ---- |
| V x H                                              |  = (v |  + e |  ).H = V | x H | + e   |  x H | = 0  |
| 1ea                                                |       | 1    | a        | 1   |       | a    |      |
|                                             = 0 (v |       |      |          |     | € V)  |      |      |
1
S
ea

|                                                    | T     |      | T        |     | T     |      | T    |
| -------------------------------------------------- | ----- | ---- | -------- | --- | ----- | ---- | ---- |
| V x H                                              |  = (v |  + e |  ).H = V | x H | + e   |  x H | = 0  |
| 2ea                                                |       | 2    | a        | 2   |       | a    |      |
|                                             = 0 (v |       |      |          |     | € V)  |      |      |
|                                                    |       |      |          |     | 2     |      |      |

Cómo el error e  es el mismo en ambos casos ambos resultados distintos de cero son iguales y se lo
a
| denomina Síndrome asociado al error e |     |     |     |     | (S )    |     |     |
| ------------------------------------- | --- | --- | --- | --- | ------- | --- | --- |
|                                       |     |     |     |     | a  ea   |     |     |
En principio cada vez que al recibir una palabra y al multiplicarla por HT el resultado dé el síndrome
S  sabremos que el error está en el cuarto dígito pudiendo entonces corregir , las palabras correctas
ea
serán 101110 y 111001
LA MARIZ H SE DENOMINA MATRIZ DE CONTROL DE PARIDAD

Importante:
Al ser un producto de matrices, puede darse esta situación:
T
| e  x H | = S1  |     |     |     |     |     |     |
| ------ | ----- | --- | --- | --- | --- | --- | --- |
a
| e  x H | T   = S1  |     |     |     |     |     |     |
| ------ | --------- | --- | --- | --- | --- | --- | --- |
b
Es decir que dos errores simples diferentes generen el mismo Síndrome, en este caso sólo se
| podrá detectar error e |     |     | ó e  pero NO corregir.  |     |     |     |     |
| ---------------------- | --- | --- | ----------------------- | --- | --- | --- | --- |
|                        |     |     | a   b,                  |     |     |     |     |
|                        |     |     |                         |     |     |     |     |

Si se pretende detectar y corregir errores simples en cada uno de los n dígitos de la palabra código se
debe tener en cuenta lo siguiente:
Dada una palabra código genérica que modelizamos cómo x = (x ,x , …….x )
|     |     |     |     |     |     |     |     | i   | i1  |   i2  |   in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- |
Si se pretende detectar y corregir error simple en cada uno de los n dígitos debe haber tantos
síndromes distintos como dígitos tenga la palabra código:
| x = (x | , x        | , ……..x | )    |     |     |     |     |     |     |     |     |
| ------ | ---------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| i      | i1     i2  |         |   in |     |     |     |     |     |     |     |     |

|       S | S   | ……. S |     |     |     |     |     |     |     |     |     |
| ------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
en
| e1 ,  | e2  |     |     |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Es decir para detectar y corregir error simple en cada uno de los n dígitos de la palabra código
debe ser la cantidad de síndromes mayor o igual a la cantidad de dígitos.
Veamos esto desde el punto de vista de las dimensiones de los vectores y espacios:
La dimensión de vector que modeliza el error (e ) es : 1 fila x n columnas
a
La dimensión de la matriz de control  HT  es: n filas x n-m columnas
Por lo tanto el Síndrome que es el resultado del producto del vector que modeliza el error por
la matriz de control tendrá como dimensión: 1 fila  x n-m columnas
T
| e  x  H | =  S |           |     |     |     |     |     |     |     |     |     |
| ------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a       |      | ea        |     |     |     |     |     |     |     |     |     |
1xn     nx(n-m)     1x(n-m)
Entonces al ser los elementos binarios, la cantidad de Síndromes distintos será 2n-m - 1

(no se considera el cero ya que corresponde a palabra OK )
 ------------------------------------------------------------------------------------------------------------------
RESUMEN
V : Código de Grupo – Dimensión 2m filas x n columnas
G: matriz generadora de V – Dimensión m filas x n columnas
V’: Espacio Ortogonal a V – Dimensión 2n-m filas x n columnas
H: Matriz generadora de V’ llamada matriz Control de paridad –
Dimensión n-m filas x n columnas
| v x HT = 0           siendo  v |     |     |     | = (x | ,x        | , …….x |      | )   |     |     |     |
| ------------------------------ | --- | --- | --- | ---- | --------- | ------ | ---- | --- | --- | --- | --- |
| i                              |     |     |     | i    | i1    i2  |        |   in |     |     |     |     |
v’ x GT = 0
|       |          |     | siendo  v’ | = (x’             | ,x’    | , …….X’ |              | )   |     |     |     |
| ----- | -------- | --- | ---------- | ----------------- | ------ | ------- | ------------ | --- | --- | --- | --- |
| i     |          |     |            | i                 | i1     | i2      |              | in  |     |     |     |
|       | T        |     | T          |                   |        |         |              |     |     |     |     |
| V x H |  = e x H |     | = S        |                   | siendo |         | e = (0…1..0) |     |     |     |     |
| 1ei   |          | i   |            | i                 |        |         | i            |     |     |     |     |
  -------------------------------------------------------------------------------------------------------

Observación: Dado el siguiente Código de Grupo, siendo la palabra código v = ( x , x ,
i 1 2
x , x , x , x ):
3 4 5 6
000000 Observando el Código de Grupo V , podemos decir qué
001101 errores NO SE DETECTAN , observando lo siguiente:
010110 si a la palabra Nula (000000) le generamos un error triple
V= 011011 en x , x , x y si modelizamos el error con una palabra
1 3 5
100111 con todos ceros y un uno en las posiciones 1, 3 y5 , es decir
111100 e = (101010) , resulta:
135
110001 v 000000
1
+ +
e 101010
135
v 101010 Y esta palabra pertenece al Código ,
1 e135
por lo tanto cuando en el receptor se multiplique por la Matriz HT el resultado será
CERO como si fuera palabra correcta. Tomemos otra palabra cualquiera del código y
generemos el mismo error v 110001
8
+ +
e 101010
135
v 011011 Que también pertenece al Código
8 e135
Esto es porque la palabra generadora de error también pertenece al Código, si
probamos con el resto de las palabras código podemos concluir lo siguiente:
Dado un Código de Grupo, los errores que NO se detectan son aquellos que
coinciden con sus palabras códigos o sea donde hay unos en las palabras
códigos.
Entonces observado nuestro código podemos decir que NO se detectan los siguientes
errores:
Error Triple en x , x x Error Triple en x , x x
3 4 y 6 - 2 4 y 5
Error Triple en x , x x Error Triple en x , x x
1 3 y 5 - 1 2 y 6
Error Cuádruple en x , x , x x Error Cuádruple en x , x , x x
2 3 5 y 6 - 1 4 5 y 6
Error Cuádruple en x , x , x x
1 2 3 y 4
Todos los demás errores caerán en alguna de las familias asociadas a cada
síndrome