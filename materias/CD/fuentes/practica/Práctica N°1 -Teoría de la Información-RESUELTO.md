PRÁCTICA N°1 – 

TEORÍA DE LA INFORMACIÓN


Dada la Siguiente fuente, determinar la probabilidad de cada símbolo y calcular la entropía de la misma:
Se tiene una fuente cuyos símbolos son el “0” y el “1”, una muestra significativa resulta:  000101101111010110011000111101.

RESOLUCION
Fuente -> alfabeto {0,1}
Muestra significativa  …….000101101111010110011000111101………
fr(0) = frecuencia relativa de ceros (cantidad de ceros en al muestra significativa sobre la cantidad de símbolos de la muestra)

fr(0) =  13/30 = 0,433…
fr(1) = 17/30 = 0,566….

Por lo tanto p(0) ≈ fr(0)  = 0,43
                 p(1) ≈ fr(1)  = 0,57

H(f) = - p(0) lg p(0)  -  p(1) lg p(1)    =>     H(f) = -0,43 lg 0,43  -   0,57 lg 0,57

El logaritmo utilizado para el calculo de la entropía es en base 2 con lo cual la entropía resulta en bits por símbolo. Utilizando calculadora para el calculo del logaritmo este será base 10, por lo cual para obtenerlo en base 2 es necesaria aplicar el cambio de base

Lg2 p(0) =  Lg10 p(0)  /  Lg10 2    =    lg 0,43 / lg 2   =   -1,2176

Lg2 p(1) =  Lg10 p(1)  /  Lg10 2    =    lg 0,57 / lg 2   =   -0,811

H(f) = -0,43 x (-1,2176) – 0,57 x (-0,811)
H(f) = 0,5236 + 0,4623  
H(f) = 0,986


Una fuente emite colores ( R = rojo, V = verde, B = blanco), tal que una muestra significativa resulta: RVBBVVVRVRBBVRBBBBVVVVRVBRVVV RVRR.

Una fuente tiene como alfabeto de salida las letras minúsculas del alfabeto y una muestra significativa resulta:   abaaacbdeiiioeeaaabbcduaabbbbbbcbecdabdd dioeuaaaiiiibebeeecdbdddciiioeuee.

Se tiene una moneda de tal forma que la probabilidad de obtener cara resulta el doble de la probabilidad de obtener cruz.

RESOLUCION

Fuente -> A={cara, cruz}

p(cara) = 2 p(cruz)

p(cara) + p(cruz) = 1  => ya que ∑ p = 1

2 p(cruz)  +  p(cruz)  = 1

p(cruz) = 1/3       por lo tanto      p(cara) = 2/3

H(moneda careada) = 2/3 lg 3/2 + 1/3 lg 3
                       
                       = 0,39 + 0,528

	            =  0,918 bits/simbolo


Si se considera un dado normal arrojado.

Un dado cargado de tal manera que la probabilidad de obtener caras pares resulta el doble de la de obtener caras impares constituye la fuente.


Si se considera como fuente emisora de números decimales de un dígito la sucesión de números telefónicos de una guía telefónica, se pide encontrar una muestra significativa, obtener las frecuencias relativas para cada valor y considerándolas como probabilidades calcular la entropía de la fuente. 

Nota: Se sugiere comenzar con 20 (veinte) números sucesivos y duplicar la muestra hasta considerar que se ha hallado una muestra significativa.



Se tiene un canal binario simétrico (P = 0.8) conectado a una fuente binaria cuyo esquema de probabilidad resulta (0.45 y 0.55) se puede calcular H(A,B).

RESOLUCION

p(0) = 0,45
p(1) = 0,55

H(A,B) = - ∑  p(ai, bj) lg p(ai, bj)
                  i,j
 

H(A,B) = - p(0,0) lg p(0,0)  -  p(0,1) lg p(0,1) - p(1,0) lg p(1,0)  -  p(1,1) lg p(1,1)       


p(0,0) = p(0)  .   p(0/0)  = 0,45  .  0,8  = 0,36
p(0,1) = p(0)  .   p(1/0)  = 0,45  .  0,2  = 0,09
p(1,0) = p(1)  .   p(0/1)  = 0,55  .  0,2  = 0,11
p(1,1) = p(1)  .   p(1/1)  = 0,55  .  0,8  = 0,44


H(A,B) = 0,36 + 0,09 + 0,11 + 0,44
           = 1 bits por símbolo


Si se conecta una fuente equiprobable al canal del esquema calcular la cantidad de información de los símbolos a la entrada y a la salida del canal.



Dado una fuente de dos símbolos, calcular la entropía de la fuente en función de la probabilidad de los símbolos (PX1, PX2) y graficar los valores de tal forma que se compruebe que el máximo valor de entropía se obtiene para el caso que ambos símbolos resultan equiprobable.

SUGERENCIA:  Tomar como valores de probabilidad de símbolos desde el 0 al 0,5 en intervalos de 0,1.



Se tiene una fuente que emite tres símbolos diferentes (x1, x2, x3), con las siguientes probabilidades P(X1) = 0,2; P(X2) = 0,5 y P(X3) = 0,3. Calcular:
La cantidad de información de cada símbolo.

La información promedio por símbolo de la fuente.

RESOLUCION

Fuente -> {x1, x2, x3}

P(X1) = 0,2
P(X2) = 0,5 
P(X3) = 0,3

I(x1) = - lg 0,2  =  2,32bits
      I(x2) = - lg 0,5  =  1bits
      I(x3) = - lg 0,3  =  1,74bits

H(F) = 0,2  .  2,32  +   0,5  .   1    +  0,3  .   1,74
  =  0,464  +  0,5  +  0,522
  =  1,486 bits/símbolo


Calcular la información promedio por símbolo de la fuente para las siguientes fuentes.


















Se dispone de un canal con una matriz de probabilidades condicionales P. Calcular:
¿Cuál es la probabilidad de obtener un símbolo “y” a la salida? P(a) = 0,4 y P(b) = 0,6.

La caracterización bivariada del sistema, con la fuente anterior conectada.

La entropía del sistema.

La entropía del canal.









Dado el siguiente canal:


¿Cuál es la probabilidad de que habiendo obtenido un “0” (cero) a la salida este provenga de un “1” en la entrada?

¿Cuál es la probabilidad de obtener un 0 (cero) a la salida producto de un 0 (cero) a la entrada?

Conectado a una fuente equiprobable, calcular la matriz de probabilidades conjunta.

Calcular la equivocación de x respecto de y.

Calcular la información mutua.

Si el canal tiene una capacidad de 0,8 bpsimbolo calcular la eficiencia y el rendimiento del canal. Analizar si es posible que este valor de probabilidad pueda pertenecer al canal del problema. 










Si la fuente del problema 6 se conecta a un canal cuya matriz de probabilidades condicionales resulta P. Calcular:
La entropía del Sistema.

La entropía del canal.

La información mutua.










RESOLUCION


Fuente -> {x1, x2, x3}



La entropía del sistema:
H(A,B) = - p(x1, y1) lg p(x1, y1)   -    p(x1, y3) lg p(x1, y3)    -     p(x2, y2)  lg p(x2, y2)   -    p(x2, y3) lg p(x2, y3)     -    p(x3, y1) lg p(x3, y1)    -    p(x3, y3) lg p(x3, y3)    (NOTA: el resto es 0 -cero-)

p(x1, y1) = 0,2 x 0,5 = 0,1
p(x1, y3) = 0,2 x 0,5 = 0,1
p(x2, y2) = 0,5 x 0,6 = 0,3
p(x2, y3) = 0,5 x 0,4 = 0,2
p(x3, y1) = 0,3 x 0,2 = 0,06
p(x3, y3) = 0,3 x 0,8 = 0,24

H(A,B) = - 0,1 lg 0,1   -    0,1 lg 0,1    -     0,3 lg 0,3   -   0,2 lg 0,2     -    0,06 lg 0,06    -    0,24 lg 0,24    

H(A,B) = 0,332 + 0,332 + 0,521 + 0,464 + 0,244 + 0,494
H(A,B) = 2,387 bits por símbolo





 Entropía del canal: 
H(B/A) = - ∑ p(ai, bj) lg p(bj, ai)
                ij


H(B/A) = - p(x1, y1) lg p(y1, x1)   -   p(x1, y2) lg p(y2, x1)  -   p(x1, y3) lg p(y3, x1)    -   p(x2, y1) lg p(y1, x2)    -      p(x2, y2)  lg p(y2, x2)   -    p(x2, y3) lg p(y3, x2)     -    p(x3, y1) lg p(y1, x3)    -    p(x3, y2) lg p(y2, x3)   -     p(x3, y3) lg p(y3, x3)    

H(B/A) = 0,1 lg 0,5 – 0,1 lg 0,5 – 0,3 lg 0,6 – 0,2 lg 0,4 – 0,06 lg 0,2 – 0,24 lg 0,8
H(B/A) = 0,1 + 0,1 + 0,22 + 0,264 + 0,14 + 0,077
H(B/A) = 0,9 bits por símbolo

La información mutua
I(A, B) = H(B)  -  H(B/A)
H(B)  (entropía de la salida)       p(y1) = ∑ p(xi)  p(y1/xi)
					         i

p(y1) = 0,2 x 0,5 + 0,3 x 0,2 = 0,16
p(y2) = 0,5 x 0,6 = 0,3
p(y3) = 0,2 x 0,5 + 0,5 x 0,4 + 0,3 x 0,8 + = 0,54

H(B) = - 0,16 lg 0,16 – 0,3 lg 0,3 – 0,54 lg 0,54
       = 0,423 + 0,521 + 0,48 = 1,424 bit por símbolo


I(A, B) = H(B)  -  H(B/A)
I(A, B) = 1,424 – 0,9
I(A, B) = 0,524 bit por simbolo














Dado el siguiente sistema de comunicación:













Calcular H(B) e indicar que significa.

Calcular H(A), la relación cuantitativa entre H(A) y H(B) y explicar.

Si se tiene un canal de 0,2 bits por símbolo y la señal transmitida tiene una duración  τ = 1seg. Explicar hasta que valor de velocidad de información puede transmitirse con un error tan pequeño como se desee.

Además, analizar si el canal del problema puede ser el del punto “c”.



Calcular la velocidad de información de una fuente telegráfica tal que:
P(punto) = 2/3				p(raya) = 1/3
		τ(punto) = 0,2 seg.			τ(raya) = 0,4 seg.


RESOLUCION

I(pto) = - 2/3 lg 2/3 = 0,39bits

I(raya) = - 1/3 lg 1/3 = 0,53bits

R = (0,39bits + 0,53bits) / 0,6seg 
R = 0,92 bits / 0,6seg
R = 1,53bits por seg



Una fuente produce 5 símbolos con probabilidades 1/2, 1/4, 1/8, 1/16  y  1/16. Calcular la entropía. 

Una fuente tiene 8 símbolos equiprobables y emite en bloque de tres a una velocidad de 1.000 bloques por segundo. Si el primer símbolo de cada bloque es siempre el mismo (sincronización) y los dos restantes pueden ser cualquiera de los ocho. Calcular R.


Se transmiten trenes de pulsos (4 pulsos cada tren), cada pulso dura 1 mseg. Los pulsos son de cuatro niveles y equiprobables, excepto el primer pulso, que tiene un nivel fijo (1 volt.).Calcular R.


Se envía un mensaje enviando 5 pulsos de igual duración. El primero es binario y el resto pueden usar cualquier nivel entre +4 y –4, incluido el 0 (cero).
¿Cuántos mensajes se pueden enviar en un grupo simple de 5 pulsos?

Si el mensaje fuese binario, ¿cuántos pulsos necesitaríamos?

RESOLUCION

5 pulsos: 1 – binario 
	    4 – 9 niveles

M = 2{ µT/τ}
M = 2 { 94}
M = 13122 mensajes

Si fuese binario µ = 2

13122 ≤   2T/τ 

T/τ ≥ lg 13122
T/τ ≥  13,68
T/τ = 14pulsos

Una fuente tiene 16 símbolos equiprobables  (1 mseg.). Se emiten en bloques de 15, separados por un pulso de sincronismo de 5 mseg. Calcular R.


Una imagen de TV tiene 625 líneas con 500 puntos por líneas y 128 niveles de brillo por punto. Si se transmiten 25 imágenes por segundo calcular R.


Si la señal del problema anterior se envía por un canal de transmisión de 2,5 Mbps, calcular el tiempo de transmisión.


Si transmiten pulsos de 1 mseg. De duración tal que los pulsos adoptan 4 niveles con probabilidades  1/2, 1/4, 1/8, 1/8. Calcular R.


Al tren de pulsos anterior se lo codifica:

a	00	1/2
b	01	1/4
c	10	1/8
d	11	1/8
¿Cuál es la duración de 1 binit a la salida del codificador?

Calcular cuántos binit por bit se necesitan para la transmisión.








Comunicaciones – Teoría: Teoría de la Información
– Ingeniería de Sistemas de Información -


 Comunicación de Datos


 EMBED PBrush  

 EMBED PBrush  

 EMBED PBrush  

 EMBED PBrush  

 EMBED PBrush  

 EMBED PBrush  

 EMBED PBrush  

 EMBED PBrush  

 EMBED PBrush  

 EMBED PBrush  



