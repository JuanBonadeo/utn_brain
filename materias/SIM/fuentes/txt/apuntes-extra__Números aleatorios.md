Prof. Alfredo Lascano
| 10/04/2019 | 2018 - UTN Rosario | 1   |
| ---------- | ------------------ | --- |

Agenda
 Números aleatorios. Generalidades y propiedades.
 Generador “Cuadrado de los medios”
 Familia de generadores congruenciales lineales
 Tests para verificar uniformidad e independencia en forma
empírica.
 Test de Chi-cuadrado
 Test de Corridas
10/04/2019 2010 - UTN Rosario 2

Números aleatorios I
 Propiedades de un buen generador de números aleatorios
 Los valores generados están distribuidos uniforme en el intervalo (0,1)
 Los valores generados son valores no correlacionados es decir
independientes en términos
 estadísticos.
 Es posible regenerar una secuencia de números aleatorios. Necesario
cuando se quiere comparar 2
 o más alternativas y se desea someterlas a la misma situación de eventos
generados.
 Computacionalmente eficiente
 Los números obtenidos por generadores que no cumplen con alguna de
las propiedades se los llama “pseudo aleatorios”.
10/04/2019 2010 - UTN Rosario 3

Números aleatorios I I
| Método cuadrado de los medios |     |     |     |     | Consiste en: |     |
| ----------------------------- | --- | --- | --- | --- | ------------ | --- |
 Obtener un entero de 4 cifras como la
semilla del generador (Z )
|     | i   | Z   | U   | Z 2 |     |     |
| --- | --- | --- | --- | --- | --- | --- |
0
|     |     | i    | i   | i        |  Elevar cada Zial cuadrado               |     |
| --- | --- | ---- | --- | -------- | ----------------------------------------- | --- |
|     | 0   | 7182 | …   | 51581124 | Completar con ceros a la izquierda si el  |     |

número obtenido no tiene 8 cifras
|     | 1   | 5811 | 0,5811 | 33767721 |     |     |
| --- | --- | ---- | ------ | -------- | --- | --- |
 Tomar las 4 cifras centrales como el
|     | 2   | 7677 | 0,7677 | 58936329 | próximo Zi |     |
| --- | --- | ---- | ------ | -------- | ---------- | --- |
 Calcular Ui= Zi/ 10000
|     | 3   | 9363 | 0,9363 | 87665769 |     |     |
| --- | --- | ---- | ------ | -------- | --- | --- |
 Iterar
…
Se puede comprobar que este método
tiende a cero rápidamente (probar con
Z0 = 1009) y no vuelve a valores
cercanos a 1, por lo tanto no es un
método aplicable en simulación dado
que no cumple con la propiedad de
uniformidad en el intervalo (0,1).
| 10/04/2019 |     |     |     | 2010 - UTN Rosario |     | 4   |
| ---------- | --- | --- | --- | ------------------ | --- | --- |

Números aleatorios III
Método cuadrado de los medios - Ejercicio
Aplique el método descripto iniciando con un valor de Z = 1009 y genere tantos
0
valores hasta identificar un comportamiento significativo.
MOSTRAR ESTE TEXTO DESPUES DE QUE LOS ALUMNOS HAYAN OBTENIDO
LOS RESULTADOS
Se puede comprobar que este método tiende a cero rápidamente y no vuelve a valores
cercanos a 1, por lo tanto no es un método aplicable en simulación dado que no cumple
con la propiedad de uniformidad en el intervalo (0,1) y de independencia dado que todo
U está determinado por U .
i i-1
10/04/2019 2010 - UTN Rosario 5

Números aleatorios III
Consiste en:
-Una vez determinados los parámetros
Generador Congruencial lineal mixto (c > 0)
del generador
-Obtener la semilla del generador
Z = (a * Z + c)modm
i i−1 -Calcular
-Iterar
donde:
aes el multiplicador y entero > 0
ces el incremento y entero > 0
m es el módulo
Z es entero > 0
i
Z es la semilla a partir de la cual se puede
0
regenerar una secuencia
Ademas debe ser
m > 0
m > a
m > c
m > Z
0
10/04/2019 2010 - UTN Rosario 6
U
i
=
Z
m
i

Números aleatorios III
Método GCL Mixto (C > 0) - Ejercicio
Aplique el método descripto iniciando con los siguientes valores
 Z = 7
0
 a = 5
 c = 3
 m = 16
genere tantos valores hasta identificar un comportamiento significativo.
MOSTRAR ESTE TEXTO DESPUES DE QUE LOS ALUMNOS HAYAN OBTENIDO
LOS RESULTADOS
Se puede comprobar que este método
le en simulación dado que no cumple con la propiedad de uniformidad en el intervalo
(0,1) y de independencia dado que todo U está determinado por U .
i i-1
10/04/2019 2010 - UTN Rosario 7

Números aleatorios IV
Generador Congruencial lineal mixto (c > 0) (continuación)
Si bien, los valores que puede tomar Zi, están determinados por la función módulo m, es posible
que el generado no alcance a los m números distintos, debido a la selección de los parámetros Z ,
0
a, c y m.
Por lo tanto se hace necesario conocer cuándo el generado permite obtener m números aleatorios
distintos. Cuando esto sucede se está en presencia de un generador de período completo, es decir
p (el período del generador) = m (el parámetro m del generador GCL)
Para saber si estamos en presencia de un generador de período completo sin tener que generar
todos los valores posible ( de 0 a m-1) se aplica el siguiente teorema a partir de los valores de los
parámetros:
Teorema: dado un GCL mixto se puede saber si es de período completo si se cumple lo siguiente
• El único entero que divide amy cen forma simultanea (primos entre si) es 1.
• Si qes un número primo que divide a m, entonces qdivide a a-1
• Si 4divide a m, entonces 4divide a a-1
10/04/2019 2010 - UTN Rosario 8

Números aleatorios V
| Generador Congruencial | lineal mixto (c > 0) (continuación) |     |     |                |                  |     |     |
| ---------------------- | ----------------------------------- | --- | --- | -------------- | ---------------- | --- | --- |
|                        | Parámetros                          |     |     | GCL deperíodo  | GCL sin período  |     |     |
|                        |                                     |     |     | completo       | completo         |     |     |
|                        |                                     | Z   |     | 7              |                  | 7   |     |
0
|     |     | a   |     | 5   |     | 6   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | c   |     | 3   |     | 4   |     |
|     |     | m   |     | 16  |     | 16  |     |
Criterios
√
x
|     | m y c primos entre  |     |                       | Cumplido | No se cumple       |        |     |
| --- | ------------------- | --- | --------------------- | -------- | ------------------ | ------ | --- |
|     | sí                  |     | Soloel 1 divide a 16  |          | También 2 dividea  |        |     |
|     |                     |     |                       | y 3      |                    | 16 y 4 |     |
x
√
|     | q(primo) divide a  |     |                    | Cumplido       | No se cumple        |     |     |
| --- | ------------------ | --- | ------------------ | -------------- | ------------------- | --- | --- |
|     | m y a a-1          |     | 2 (primo) dividea  |                | 2divide a 16 pero   |     |     |
|     |                    |     |                    | 16 y a 4 (5-1) | no divide a 5 (6-1) |     |     |
x
√
|            | 4 dividea m y a a-1 |     |        | Cumplido             | No se cumple         |     |     |
| ---------- | ------------------- | --- | ------ | -------------------- | -------------------- | --- | --- |
|            |                     |     |        | 4 divide a 16 y a 4  | 4divide a 16 pero    |     |     |
|            |                     |     |        | (5-1)                | no divide a 5 (6 -1) |     |     |
| 10/04/2019 |                     |     | 2010 - | UTN Rosario          |                      |     | 9   |

Números aleatorios VI
Generador Congruencial lineal multiplicativo (c = 0)
10/04/2019 10
Z
i
= ( a * Z
i − 1
) m o d m
Consiste en:
-Una vez determinados los parámetros
del generador
-Obtener la semilla del generador
-Calcular
-Iterar
Si bien no se puede aplicar el teorema
que permite saber si el generador es de
período completo, es posible encontrar
Donde a es el multiplicador y entero > 0
valores de a, m y Z que permitan que p
Z es entero > 0
0
i
= m
En particular Z es la semilla a partir de la cual se puede
0
regenerar una secuencia de números aleatorios
m es el módulo
Además deben ser m > 0, m > a, m > Z
0
U
i
=
Z
m
i

Números aleatorios VII
Ejemplos de generadores que tiene buen comportamiento para ser usados en simulación
Mixtos
|         | 1 5   |               | 3 5           |                 |                  |
| ------- | ----- | ------------- | ------------- | --------------- | ---------------- |
| Z = ( 5 | * Z   | + c ) ( m o d | 2 )   p r o p | u e s t o   p o | r  C o v e y o u |
| i       | i − 1 |               |               |                 |                  |
Z = ( 3 1 4 . 1 5 9 . 2 6 9 * Z ) ( m o d 2 3 1 ) )   p r o p u e s t o   p o r  K o b a y a s h i
| i   |     | i − | 1   |     |     |
| --- | --- | --- | --- | --- | --- |
Multiplicativos
| Z = ( | 7 5 * Z ) | ( m o d 2 3 | 1 − 1 ) |     |     |
| ----- | --------- | ----------- | ------- | --- | --- |
| i     | i − 1     |             |         |     |     |
Otros generadores congruenciales más generales se pueden obtener
combinando operaciones aritméticas sobre 2 o más Zi anteriores
| Z = | g ( Z , | Z , . . . | ) ( m o d m ) |     |     |
| --- | ------- | --------- | ------------- | --- | --- |
| i   | i − 1   | i − 2     |               |     |     |
10/04/2019 11

Números aleatorios VIII
Testspara evaluar uniformidad e independencia de los generadores de números aleatorios
Pueden ser:
• Teóricos: los que trabajan con la expresión del generado, para evaluar a los generados si los
números que generaría son uniformes e independientes
• Empíricos: aquellos que trabajan con los números obtenidos del generador para verificar
esas propiedades.
10/04/2019 12

Números aleatorios VIII
Test empírico de Chi-cuadrado
Asume independencia y chequea uniformidad
Pasos:
10/04/2019 13
1
2
3
c
4
5
d
1
S
n
- D i v i d i r
- G e n e r a
- C a l c u l a
a y e r o n e n
- C a l c u l a
- C o m p a
2 o n d e X
k
e l n i v
i l a d e s i g
u l a d e q u
e l i n t e r
r U c o
i
r f d o
j
e l i n t e
r l a v a
2 r a r X
e s
1 ,1
e l d e c
u a l d a d
e l o s n
v a l o ( 0 ,1 ) e n
n i 1 , n c o n
n d e f e s l a f
j
r v a l o j
r i a b l e d e C h i
2 X
k 1 ,1
e l v a l o r d e t a
o n f i a n z a
s e c o m p r u e b
ú m e r o s a l e a t o
k s
n d
r e c
- c u
b l a
a e
r i o
u b i n t e
e t e r m
u e n c i
a d r a d
d e u n
n t o n c
s s e c
r
i n
a
o
a
e
o
v a
a d
a b
X
C
s s
m
l o
o
s
2
h
e
p o
s
o
i
r
d
d e
l u
- c
e c
r t a
e i g u a l l o n
m a n e r a q
t a d e l a c a
k k
( f
j
n
j 1
u a d r a d o c
h a l a H h
0
n U n i f o r m
g i t u d
n
u e
k
n t i d a
n
2 )
k
o n k
i p ó t e
e s ( n
d
s
o
c o
5
d
1
i s
s
e
g
o
n k
U
r a
n
i
d
u
q
o
n
5
u
s
i f
e
d
o
e
r m
l i b
e
e
s
r
)
t
.
a d y


 −
− −

=
− −
= 
=
−

−


Números aleatorios IX
• Test empírico de Series
• Chequea uniformidad y asume independencia
• Es una generalización del test de Chi-cuadrado, se aplica el mismo método pero en 2
o más dimensiones, trabajando con vectores de números aleatorios
• Tiene mayor precisión en evaluar la uniformidad
10/04/2019 14

Números aleatorios IX
Test empírico de Series
Si los U  fueran vectores aleatorios de una variable IID  U(0,1) las d -tuplas no superpuestas
i
| U = (U | ,U ,,,U | ),     U | = (U | ,U ,,,U | ),... |     |     |     |     |
| ------ | ------- | -------- | ---- | ------- | ----- | --- | --- | --- | --- |
| 1      | 1 2     | d        | 2    | d+1 d+2 | 2d    |     |     |     |     |
deberían ser vectores aleatorios IID distribuidos uniformemente en el hipercubo unitario
d -dimensional
Método:
1- Dividir el hipercubo [0,1]d en k subintervalos de igual longitud con k 100
2-Generar U ,U ,,,U  vectores (se requieren m = n*d números aleatorios)
|     |     | 1 2 | n   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n
Los valores de k y n deben ser determinados de manera que   5
kd
3-Calcular f  donde  f  es la frecuencia absoluta de la cantidad de vectores U  que
|     |     | j j ,,,j | j j ,,,j |     |     |     |     |     | i   |
| --- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- |
|     |     | 1 2 d    | 1 2      | d   |     |     |     |     |     |
tienen su primer componente en el intervalo  j , la segunda componente en el  j  y así sucesivamente
|     |     |     |     |     | 1   |          |     | 2   |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
|     |     |     |     |     |     | kd k k k |     | n   |     |
4-Calcular la variable de Chi-cuadrado X 2(d) = ,,, ( f − )2
j j ,,,j
|              |     |        |     |     |     | n              | 1 2 d | kd  |     |
| ------------ | --- | ------ | --- | --- | --- | -------------- | ----- | --- | --- |
|              |     |        |     |     |     | j =1 j =1 j =1 |       |     |     |
|              |     |        |     |     |     | 1 2 d          |       |     |     |
| 5-Comparar X |     | 2(d)  | X 2 |     |     |                |       |     |     |
kd−1,1−
|         | 2   |  es el valor de tabla de una Chi-cuadrado con kd |     |     |     |                         |     |     |     |
| ------- | --- | ------------------------------------------------ | --- | --- | --- | ----------------------- | --- | --- | --- |
| donde X |     |                                                  |     |     |     | −1 grados de libertad y |     |     |     |
kd−1,1−
1− el nivel de confianza
Si la desigualdad se comprueba entonces se recha la H  hipótesis
0
10/04/2019 15
nula de que los números aleatorios se comportan Uniformes (no son uniformes).

Números aleatorios X
• Test empírico de Corridas
Pasos:
| 1- Generar  U |  con i =1,n con n |  4000 |     |     |     |
| ------------- | ----------------- | ------ | --- | --- | --- |
i
2 - Examinar los  U  generados identifica ndo las subsecuencias crecientes y contínuas
i
de U  de longitud máxima
i
| 3- Calcular los r |  donde |     |     |     |     |
| ----------------- | ------ | --- | --- | --- | --- |
i
| cantidad  de subsecuencias de longitud i para i |     |     | =1,2,3,4,5 |     |     |
| ------------------------------------------------ | --- | --- | ----------- | --- | --- |
r =  
i
|  cantidad de subsecuencias de longitud  |     |     | 6 para i | = 6  |     |
| ----------------------------------------- | --- | --- | -------- | ----- | --- |
1 6 6
4 - Calcular la variable  Chi - cuadrado  R =  a (r − nb )(r − nb )
|     |     |     | ij  | i i j | j   |
| --- | --- | --- | --- | ----- | --- |
n
i=1 j=1
2 2
| 5- Comparar X |  X |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- |
6,1−
donde X 2  es el valor de tabla de una Chi - cuadrado con 6 grados de libertad y
6,1−
1− el nivel de confianza
Si la desigualdad se comprueba entonces se recha la H  hipótesis
0
nula de que los números aleatorios son independientes (no están correlacionados).
10/04/2019 16

Números aleatorios XI
• Test empírico de Corridas (cont.)
La matriz a
ij
El vector b o b
i j
10/04/2019 17