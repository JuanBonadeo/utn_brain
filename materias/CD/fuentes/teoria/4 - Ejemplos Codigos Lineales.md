EJEMPLOS  CODIGOS LINEALES
1 -Dada la siguiente Matriz Generadora del Código de Grupo encontrar:
a) El Código de Grupo
b) Que errores no se detectan
c) analizar cómo se comporta el Código frente a los errores simples, realizando el
análisis para todos los síndromes.

    n=6 columnas (dígitos)
           100011      g

1
|   G =   101101      g |     |       m = 3 Filas   |     |     |     |     |     |     |     |
| --------------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
2
|            111000      g |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3

a) Para hallar el Código de Grupo V se debe realizar la combinación lineal de los
vectores g de G:
i

|     | v  = k |  x g +  | k  x g | + K | x g |     |     |     |     |
| --- | ------ | ------- | ------ | --- | --- | --- | --- | --- | --- |
+ : Suma sin Acarreo
|     | i   | 1 1     | 2   | 2  ………. | m  m                |     |     |     |     |
| --- | --- | ------- | --- | ------- | ------------------- | --- | --- | --- | --- |

Entonces damos todas las combinaciones posibles de K obteniendo los
vectores de V

|     | x x x    | x x x k   |  k  k  |     |     |     |     |     |     |
| --- | -------- | --------- | ------ | --- | --- | --- | --- | --- | --- |
|     | 1  2  3  | 4 5  6    | 3 2 1  |     |     |     |     |     |     |
0  0  0  0  0  0   0  0  0    v = k xg + k xg +k xg = 0xg + 0xg +0xg
|     |     |     |     | 1 1 | 1     2 2  |   3 3  | 1     | 2    | 3     |
| --- | --- | --- | --- | --- | ---------- | ------ | ----- | ---- | ----- |
1  0  0  0  1  1   0  0  1    v = k xg + k xg +k xg = 1xg + 0xg +0xg
|     |                                 |     |     | 2 1    | 1     2 2  |   3 3       | 1     | 2    | 3     |
| --- | ------------------------------- | --- | --- | ------ | ---------- | ----------- | ----- | ---- | ----- |
|     | 1  0  1  1  0  1   0  1  0    v |     |     |        |            |             |       |      |       |
|     |                                 |     |     | = k xg | + k xg     | +k xg = 0xg | + 1xg | +0xg |       |
|     |                                 |     |     | 3  1   | 1     2 2  |   3 3       | 1     | 2    | 3     |
0  0  1  1  1  0   0  1  1    v = k xg + k xg +k xg = 1xg + 1xg +0xg
|     |     |     |     | 4  1 | 1     2 2  |   3 3  | 1     | 2    | 3     |
| --- | --- | --- | --- | ---- | ---------- | ------ | ----- | ---- | ----- |
1  1  1  0  0  0   1  0  0    v = k xg + k xg +k xg = 0xg + 0xg +1xg
|     |     |     |     | 5 1 | 1     2 2  |   3 3  | 1     | 2    | 3     |
| --- | --- | --- | --- | --- | ---------- | ------ | ----- | ---- | ----- |
0  1  1  0  1  1   1  0  1    v
|     |     |     |     | = k xg | + k xg     | +k xg = 1xg | + 0xg | +1xg |     |
| --- | --- | --- | --- | ------ | ---------- | ----------- | ----- | ---- | --- |
|     |     |     |     | 6 1    | 1     2 2  |   2 3       | 1     | 2    | 3   |
0  1  0  1  0  1   1  1  0     v = k xg + k xg +k xg = 1xg + 1xg +0xg
|     |     |     |     | 7 1 | 1     2 2  |   3 3  | 1     | 2    | 3   |
| --- | --- | --- | --- | --- | ---------- | ------ | ----- | ---- | --- |
1  1  0  1  1  0   1  1  1    v = k xg + k xg +k xg = 1xg + 1xg +1xg
|     |     |     |     | 8 1 | 1     2 2  |   3 3  | 1     | 2    | 3   |
| --- | --- | --- | --- | --- | ---------- | ------ | ----- | ---- | --- |

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Quedando entonces el Código de Grupo:

0  0  0  0  0  0
1  0  0  0  1  1
1  0  1  1  0  1
0  0  1  1  1  0   = V  2m   filas (palabras código)   x  n Columnas = 8 x 6

1  1  1  0  0  0
0  1  1  0  1  1         (8 palabras códigos de 6 dígitos cada una)
0  1  0  1  0  1
1  1  0  1  1  0

b) Los errores que no se detectan son donde hay unos en las palabras códigos
(es decir los errores que no se detectan coinciden con las palabras códigos)
| Error Triple en x    | , x | x       |         |
| -------------------- | --- | ------- | ------- |
|                      | 1   | 5 y  6  |         |
| Error Triple en x    | , x | x       |         |
|                      | 3   | 4 y  5  |         |
| Error Triple en x    | , x | x       |         |
|                      | 1   | 2 y  3  |         |
| Error Triple en x    | , x | x       |         |
|                      | 2   | 4 y  6  |         |
| Error Cuádruple en x |     | , x , x | x       |
|                      |     | 1 3     | 4 y  6  |
| Error Cuádruple en x |     | , x , x | x       |
|                      |     | 2 3     | 5 y  6  |
| Error Cuádruple en x |     | , x , x | x       |
|                      |     | 1 2     | 4 y  5  |

c) Para realizar el análisis del comportamiento del  código frente a los errores se
debe encontrar primero la Matriz de Control de Paridad H base de V’
Para esto primero aplicamos la condición de ortogonalidad que permite encontrar  V’:
| Para todo v’ | € V’ resulta  v’ |     | x GT = 0      entonces:  |
| ------------ | ---------------- | --- | ------------------------ |
|              | i                |     | i                        |
                                                    1   1  1
                                                    0   0  1
 (x’ ,x’ ,x’ ,x’ , x’ ,x’ ) x  0   1  1    = ( 0 )  = (0 , 0 , 0)
| 1    2  |   3   4  |   5    6  |     |
| ------- | -------- | --------- | --- |
0  1  0

1  0  0
                                                    1   1  0
|     |     |     |     |
| --- | --- | --- | --- |

Recordando el procedimientopara el producto de matrices resulta:
| x’ x1 + x’ | x0 + x’ | x0 +x’ | x0 +x’ | x1 + x’ |     |  x1 = 0   |
| ---------- | ------- | ------ | ------ | ------- | --- | --------- |
| 1          | 2       |   3    |   4    |   5     |     | 6         |
| x’ x1 + x’ | x0 + x’ | x1 +x’ | x1 +x’ | x0 + x’ |     |  x1 = 0   |
| 1          | 2       |   3    |   4    |   5     |     | 6         |
| x’ x1 + x’ | x1 + x’ | x1 +x’ | x0 +x’ | x0 + x’ |     |  x0 = 0   |
| 1          | 2       |   3    |   4    |   5     |     | 6         |

Queda entonces un sistema de ecuaciones de 6 incógnitas con tres
ecuaciones:
x’  + x’  +x’  = 0                         Si fueran variables naturales tendría infinitas
| 1   | 5   6  |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- |
x’ + x’ +x’ + x’  = 0                  soluciones , pero como las variables son
| 1   | 3    4  |   6 |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- |
x’ + x’ + x’  = 0                          binarias podemos darle todos los valores
| 1   | 2    3 |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- |
a tres de las variables, de manera de obtener un
sistema de ecuaciones  de 3 ecuaciones con 3
variables (3x3)
Para esto es conveniente elegir aquellas 3 variables que más se repten en las
ecuaciones de manera de tener todas las variables independientes de un lado de la
igualdad.
Además debemos recordar que la suma es sin acarreo y las variables binarias con lo
cual las ecuaciones se resuelven según:
Si a y b son variables binarias resulta:
a + b = 0   a = b  (ambas variables son 0 o´ 1)
a + b = 1   a = 1 + b        ( a = b y esto lo representamos sumando 1)
a + a  = 0   Siempre para todo valor de a (0 ó 1)
Entonces observando nuestro sistema de ecuaciones vemos que las variables que más
| se repiten en las ecuaciones pueden ser ( x |     |     |     |     |  , x |  , x  )    |
| ------------------------------------------- | --- | --- | --- | --- | ---- | ---------- |
|                                             |     |     |     |     | 1    | 3 6        |
Con lo cual ahora despejamos según lo visto anteriormente:
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

| x’  = x’ |  + x’    |     |     |
| -------- | -------- | --- | --- |
| 5        | 1  6     |     |     |
| x’  = x’ | + x’ +x’ |     |     |
| 4        | 1  3     | 6   |     |
| x’ = x’  | + x’     |     |     |
| 2        | 1    3   |     |     |
Ahora dando todos los valores a ( x’  , x’  , x’  ) obtenemos el espacio
1 3 6
ortogonal V´y luego extraemos la matriz H
                     n  = 6 columnas
|             x’ |  x’  x’ |  x’  x’  |  x’       |
| -------------- | ------- | -------- | --------- |
|                | 1    2  |   3   4  |   5  6    |
            0     0     0    0    0    0
            0     0     0    1   1     1
            0     1     1    1    0    0
  V’ =    0    1     1     0    1   1       2n-m   filas    = 26-3   = 23   = 8
            1     1     0    1    1    0
            1     1     0    0    0    1
            1     0     1    0    1    0
            1     0     1    1    0    1

Ahora hay que elegir una base de n x (n-m) = 6 columnas x 3filas cuyos
vectores  sean independientes
Si elegimos los vectores:
            0     0     0    1    1    1          Vemos que el vector h  = h  + h
3 1 2
            0     1     1    1    0    0    = H    Por lo tanto no es Base Generadora
            0     1     1    0    1    1              de V’

Debemos elegir otro conjunto de 3 vectores que resulten linealmente independientes:
1     1     0    1    1    0
1     1     0    0    0    1   = H           Vemos que el vector h  = h  + h
3 1 2
1     0     1    0    1    0

Podríamos elegir también:
0 1 1 1 0 0
0 1 1 0 1 1 = H Vemos que el vector h = h + h
3 1 2
1 1 0 1 1 0
Cada uno puede elegir una base distinta obteniendo iguales resultados
No quedamos con esta última:
0 1 1 1 0 0
0 1 1 0 1 1 = H
1 1 0 1 1 0
Ahora planteamos que una palabra de V con error multiplicada por HT debe dar distinto
de cero (síndrome):
T
V x H = S
ie i
Como no conocemos la palabra con error será una incógnita de nuestra ecuación,
(x , x , x , x , x , x ), conocemos HT y el síndrome conocemos sus dimensiones (1x
1 2 3 4 5 6
n-m), así que lo proponemos :
(x , x , x , x , x , x ) x HT = Si
1 2 3 4 5 6
No concemos el error dato proponemos Si = 0
SÍNDROME 001
0 0 1
1 1 1
(x , x , x , x , x , x ) x 1 1 0 = 0 0 1 Podemos elegir cualquier síndrome,
1 2 3 4 5 6
1 0 1 en particular y por una cuestión de
0 1 1 comodidad elegimos contar
0 1 0 en binario ( 1, 2, 3, 4, 5, 6 y 7) ya
que son 2n-m - 1 = 23 – 1 = 7 Síndromes distintos
Queda entonces un sistema de ecuaciones de 6 incógnitas con tres
ecuaciones:

x  + x  +x = 0                              Si fueran variables naturales tendría infinitas
| 2   | 3   4   |     |     |     |     |
| --- | ------- | --- | --- | --- | --- |
x + x +x +x = 0                        soluciones , pero como las variables son
| 2   | 3    5     | 6   |     |     |     |
| --- | ---------- | --- | --- | --- | --- |
x + x + x  +x = 1                       binarias podemos darle todos los valores
| 1   | 2    4   | 5   |     |     |     |
| --- | -------- | --- | --- | --- | --- |
a tres de las variables, de manera de obtener un
sistema de ecuaciones  de 3 ecuaciones con 3
variables (3x3)
Para esto es conveniente elegir aquellas 3 variables que más se repiten en las
ecuaciones de manera de tener todas las variables independientes de un lado de la
| igualdad, por ejemplo . x |     | , x y x |     |     |     |
| ------------------------- | --- | ------- | --- | --- | --- |
|                           |     | 2  3    | 5   |     |     |
Además debemos recordar que la suma es sin acarreo y las variables son binarias con
lo cual las ecuaciones se resuelven según:

|    x  = x |  + x   |                                       |     |     |     |
| --------- | ------ | ------------------------------------- | --- | --- | --- |
|   4       | 2    3 |                                       |     |     |     |
    x = x + x + x                                                                x +x  = 0
| 6   | 2  3   | 5   |     |     | 2 2 |
| --- | ------ | --- | --- | --- | --- |
    x = 1 + x + x + x  =  1 + x + x  + x  + x = 1 + x + x
| 1   | 2   | 4    5 | 2    5 | 2   3  | 3    5 |
| --- | --- | ------ | ------ | ------ | ------ |

| x  = x    |  + x     |        |     |     |     |
| --------- | -------- | ------ | --- | --- | --- |
| 4         | 2   3    |        |     |     |     |
| x = x     | + x + x  |        |     |     |     |
| 6         | 2  3     | 5      |     |     |     |
| x = 1 + x | + x      |        |     |     |     |
| 1         | 3        | 5      |     |     |     |
Ahora damos todos los valores a las variables  x , x , x  y obtenemos los valores de
|          |               |          |     | 2     3  5   |     |
| -------- | ------------- | -------- | --- | ------------ | --- |
| x , x    | y x           |          |     |              |     |
| 1     4  |    6          |          |     |              |     |
|     x    | x  x x  x     | x        |     |              |     |
| 1        | 2   3    4    | 5    6   |     |              |     |
 1    0   0   0   0    0                           Esta es la Familia de palabras de V que

    0    0   0   0   1    1                           tienen un determinado error que dá como
    0    0   1   1   0    1                           resultado el Síndrome S  = 001, resumiendo es
1
    1    0   1   1   1    0                           Familia de Errores asociadas al Síndrome 001
    1    1   0   1   0    1
    0    1   0   1   1    0                            Observando el Código V y una palabra
    0    1   1   0   0    0                            código con error por ejem. 111011 , no
    1    1   1   0   1    1                             no se puede deducir en cuál dígito  está el error.

Pero en el Código hay una palabra muy particular, la (000000) , entonces si a esa
palabra le generamos un error simple por ejemplo en x  resulta:
1
    X       0 0 0 0 0 0
1
| +   | +   |     |     |     |
| --- | --- | --- | --- | --- |
   e       1 0 0 0 0 0
x1
 x        1 0 0 0 0 0               Queda como resultado la palabra con error e
ex1 x1
Entonces observando la Familia de Errores  Asociadas al Síndrome 001 vemos que
todas las palabras se corresponden a las palabras códigos con un error en x , en
1
particular la 000000  000001   Por ejemplo retomando la palabra 111011 la palabra
correcta es la 011011
La conclusión es que con el Síndrome 001 se detecta y corrige error simple en x
1
También podría ser este síndrome causado por :
| Error Doble en x     |     | yx  |             |          |
| -------------------- | --- | --- | ----------- | -------- |
|                      |     | 5   |   6         |          |
| Error Doble en x     |     | yx  |             |          |
|                      |     | 2   |   3         |          |
| Error Triple en x    |     | , x | x           |          |
|                      |     | 3   | 4 y  6      |          |
| Error Triple en x    |     | , x | yx          |          |
|                      |     | 2   | 4    5      |          |
| Error Cuádruple en x |     |     | , x , x     | yx       |
|                      |     |     | 1 3 4       |   5      |
| Error Cuádruple en x |     |     | , x , x     | yx       |
|                      |     |     | 1 2 4       |   6      |
| Error Quíntuple en x |     |     | , x , x , x | y x      |
|                      |     |     | 1 2 3       | 5     6  |
Pero vamos a considerar el criterio de la mayor probabilidad, en este caso Error unitario
en x .
1
SÍNDROME 010
Veamos ahora la Familia de Errores asociadas al Síndrome 010

                                      0 0 1
|             |       |              |     1 1 1                   |     |
| ----------- | ----- | ------------ | --------------------------- | --- |
|     (x ,    | x , x | , x , x      | , x ) x   1 1 0    = 0 1 0  |     |
| 1           | 2     | 3      4     | 5     6                     |     |
                                                1 0 1
                                       0 1 1
                                                0 1 0

Las ecuaciones quedan ahora:
| x  + x |  +x = 0                                 |                                 |
| ------ | --------------------------------------- | ------------------------------- |
| 2      | 3   4                                   |                                 |
| x + x  | +x +x                                   | = 1                             |
| 2      | 3    5                                  | 6                               |
| x + x  | + x  +x                                 | = 0                             |
| 1      | 2    4                                  | 5                               |
Elegimos las mismas tres variables como independientes  x , x , x  quedando las
2     3  5
ecuaciones:
| x  = x    |  + x       |        |
| --------- | ---------- | ------ |
| 4         | 2   3      |        |
| x = 1 + x | + x        | + x    |
| 6         | 2  3       | 5      |
| x = x     | + x        |        |
| 1         | 3    5     |        |

Ahora damos todos los valores a las variables  x , x , x  y obtenemos los valores de
2     3  5
| x , x    | y x      |     |
| -------- | -------- | --- |
| 1     4  |    6     |     |

|     x | x  x x  x     | x        |
| ----- | ------------- | -------- |
| 1     | 2   3    4    | 5    6   |
 0    0   0   0   0    1                           Esta es la Familia de palabras de V que

    1    0   0   0   1    0                           tienen un determinado error que dá como
    1    0   1   1   0    0                           resultado el Síndrome S  = 010 , resumiendo es
2
    0    0   1   1   1    1                           Familia de Errores asociadas al Síndrome 010
    0    1   0   1   0    0
    1    1   0   1   1    1                            Al igual que en el síndrome anterior nos fijamos
    1    1   1   0   0    1                            en el error en la palabra nula , es decir vemos
    0    1   1   0   1    0                             la palabra con todos ceros y un solo uno

Entonces vemos que el error se produce en el dígito x , además valen las mismas
6
consideraciones en cuanto a los errores de orden superior
 .
La conclusión es que con el Síndrome 010 se detecta y corrige error simple en x
6
SÍNDROME 011
Veamos ahora la Familia de Errores asociadas al Síndrome 011:

0 0 1
1 1 1
(x , x , x , x , x , x ) x 1 1 0 = 0 1 1
1 2 3 4 5 6
1 0 1
0 1 1
0 1 0
Las ecuaciones quedan ahora:
x + x +x = 0
2 3 4
x + x +x +x = 1
2 3 5 6
x + x + x +x = 1
1 2 4 5
Elegimos las mismas tres variables como independientes x , x , x quedando las
2 3 5
ecuaciones:
x = x + x
4 2 3
x = 1 + x + x + x
6 2 3 5
x = 1 +x + x
1 3 5
Ahora damos todos los valores a las variables x , x , x y obtenemos los valores de
2 3 5
x , x y x
1 4 6
x x x x x x
1 2 3 4 5 6
1 0 0 0 0 1 Esta es la Familia de palabras de V que
0 0 0 0 1 0 tienen un determinado error que dá como
0 0 1 1 0 0 resultado el Síndrome S = 011 , resumiendo es
3
1 0 1 1 1 1 Familia de Errores asociadas al Síndrome 011
1 1 0 1 0 0
0 1 0 1 1 1 Al igual que en el síndrome anterior nos fijamos
0 1 1 0 0 1 en el error en la palabra nula , es decir vemos
1 1 1 0 1 0 la palabra con todos ceros y un solo uno

Entonces vemos que el error se produce en el dígito x , además valen las mismas
5
consideraciones en cuanto a los errores de orden superior
 .
La conclusión es que con el Síndrome 011 se detecta y corrige error simple en x
5

SÍNDROME 100
Veamos ahora la Familia de Errores asociadas al Síndrome 100

                                      0 0 1
|             |       |        |          |     1 1 1                   |
| ----------- | ----- | ------ | -------- | --------------------------- |
|     (x ,    | x , x | , x    | , x      | , x ) x   1 1 0    = 1 0 0  |
| 1           | 2     | 3      | 4     5  |    6                        |
                                                1 0 1
                                       0 1 1
                                                0 1 0
Las ecuaciones quedan ahora:
| x  + x |  +x  | = 1                                 |                                 |     |
| ------ | ---- | ----------------------------------- | ------------------------------- | --- |
| 2      | 3    | 4                                   |                                 |     |
| x + x  | +x   | +x                                  | = 0                             |     |
| 2      | 3    | 5                                   | 6                               |     |
| x + x  | + x  |  +x                                 | = 0                             |     |
| 1      | 2    | 4                                   | 5                               |     |
Elegimos las mismas tres variables como independientes  x , x , x  quedando las
2     3  5
ecuaciones:
| x  = 1 +x |      |  + x   |     |     |
| --------- | ---- | ------ | --- | --- |
| 4         | 2    |        | 3   |     |
| x = x     | + x  | + x    |     |     |
| 6         | 2    | 3      | 5   |     |
| x = x     | + x  |        |     |     |
| 1         | 3    | 5      |     |     |

Ahora damos todos los valores a las variables  x , x , x  y obtenemos los valores de
2     3  5
| x , x y  | x      |     |     |     |
| -------- | ------ | --- | --- | --- |
| 1     4  |    6   |     |     |     |

x x x x x x
1 2 3 4 5 6
0 0 0 1 0 0 Esta es la Familia de palabras de V que
1 0 0 1 1 1 tienen un determinado error que dá como
1 0 1 0 0 1 resultado el Síndrome S = 100, resumiendo es
4
0 0 1 0 1 0 Familia de Errores asociadas al Síndrome 100
0 1 0 0 0 1
1 1 0 0 1 0 Al igual que en el síndrome anterior nos fijamos
1 1 1 1 0 0 en el error en la palabra nula , es decir vemos
0 1 1 1 1 1 la palabra con todos ceros y un solo uno
Entonces vemos que el error se produce en el dígito x , además valen las mismas
4
consideraciones en cuanto a los errores de orden superior
.
La conclusión es que con el Síndrome 100 se detecta y corrige error simple en x
4
SÍNDROME 101
Veamos ahora la Familia de Errores asociadas al Síndrome 101
0 0 1
1 1 1
(x , x , x , x , x , x ) x 1 1 0 = 1 0 1
1 2 3 4 5 6
1 0 1
0 1 1
0 1 0
Las ecuaciones quedan ahora:
x + x +x = 1
2 3 4
x + x +x +x = 0
2 3 5 6
x + x + x +x = 1
1 2 4 5
Elegimos las mismas tres variables como independientes x , x , x quedando las
2 3 5
ecuaciones:

x = 1 +x + x
4 2 3
x = x + x + x
6 2 3 5
x = 1 + x + x
1 3 5
Ahora damos todos los valores a las variables x , x , x y obtenemos los valores de
2 3 5
x , x y x
1 4 6
x x x x x x
1 2 3 4 5 6
1 0 0 1 0 0 Esta es la Familia de palabras de V que
0 0 0 1 1 1 tienen un determinado error que dá como
0 0 1 0 0 1 resultado el Síndrome S = 101, resumiendo es
5
1 0 1 0 1 0 Familia de Errores asociadas al Síndrome 101
1 1 0 0 0 1
0 1 0 0 1 0 Al igual que en el síndrome anterior nos fijamos
0 1 1 1 0 0 en el error en la palabra nula, es decir vemos
1 1 1 1 1 1 la palabra con todos ceros y un solo uno
En este caso no hay ninguna palabra con todos ceros y un solo uno, entonces
debemos ver lo que sigueen probabilidad de error, en este caso el error doble, si hay
una sola palabra con todos ceros y dos unos , se detecta y corrige error doble, vemos
que hay tres palabras con todos ceros y dos unos , por lo tanto no se puede corregir y
solo podemos detectar
La conclusión es que con el Síndrome 101 SOLO se detecta error DOBLE en:
x x ó x x ó x x
1 4 3 6 2 5
SÍNDROME 110
Veamos ahora la Familia de Errores asociadas al Síndrome 110
0 0 1
1 1 1
(x , x , x , x , x , x ) x 1 1 0 = 1 1 0
1 2 3 4 5 6
1 0 1
0 1 1
0 1 0

Las ecuaciones quedan ahora:
| x  + x |  +x = 1                                 |                                 |
| ------ | --------------------------------------- | ------------------------------- |
| 2      | 3   4                                   |                                 |
| x + x  | +x +x                                   | = 1                             |
| 2      | 3    5                                  | 6                               |
| x + x  | + x  +x                                 | = 0                             |
| 1      | 2    4                                  | 5                               |
Elegimos las mismas tres variables como independientes  x , x , x  quedando las
2     3  5
ecuaciones:

| x  = 1 +x |  + x       |        |
| --------- | ---------- | ------ |
| 4         | 2          | 3      |
| x = 1 + x | + x        | + x    |
| 6         | 2  3       | 5      |
| x = x     | + x        |        |
| 1         | 3    5     |        |

Ahora damos todos los valores a las variables  x , x , x  y obtenemos los valores de
2     3  5
| x , x    | y x           |          |
| -------- | ------------- | -------- |
| 1     4  |    6          |          |
|     x    | x  x x  x     | x        |
| 1        | 2   3    4    | 5    6   |
 0    0   0   1   0    1                           Esta es la Familia de palabras de V que

    1    0   0   1   1    0                           tienen un determinado error que dá como
    1    0   1   0   0    0                           resultado el Síndrome S  = 110, resumiendo es
5
    0    0   1   0   1    1                           Familia de Errores asociadas al Síndrome 110
    0    1   0   0   0    0
    1    1   0   0   1    1                            Al igual que en el síndrome anterior nos fijamos
    1    1   1   1   0    1                            en el error en la palabra nula, es decir vemos
    0    1   1   1   1    0                             la palabra con todos ceros y un solo uno
 Entonces vemos que el error se produce en el dígito x , además valen las mismas
2
consideraciones en cuanto a los errores de orden superior
 .
La conclusión es que con el Síndrome 110 se detecta y corrige error simple en x
2

SÍNDROME 111
Veamos ahora la Familia de Errores asociadas al Síndrome 111

0 0 1
1 1 1
(x , x , x , x , x , x ) x 1 1 0 = 1 1 1
1 2 3 4 5 6
1 0 1
0 1 1
0 1 0
Las ecuaciones quedan ahora:
x + x +x = 1
2 3 4
x + x +x +x = 1
2 3 5 6
x + x + x +x = 1
1 2 4 5
Elegimos las mismas tres variables como independientes x , x , x quedando las
2 3 5
ecuaciones:
x = 1 +x + x
4 2 3
x = 1 + x + x + x
6 2 3 5
x = 1 + x + x
1 3 5
Ahora damos todos los valores a las variables x , x , x y obtenemos los valores de
2 3 5
x , x y x
1 4 6
x x x x x x
1 2 3 4 5 6
1 0 0 1 0 1 Esta es la Familia de palabras de V que
0 0 0 1 1 0 tienen un determinado error que dá como
0 0 1 0 0 0 resultado el Síndrome S = 111, resumiendo es
5
1 0 1 0 1 1 Familia de Errores asociadas al Síndrome 111
1 1 0 0 0 0
0 1 0 0 1 1 Al igual que en el síndrome anterior nos fijamos
0 1 1 1 0 1 en el error en la palabra nula, es decir vemos
1 1 1 1 1 0 la palabra con todos ceros y un solo uno

 Entonces vemos que el error se produce en el dígito x , además valen las mismas
3
consideraciones en cuanto a los errores de orden superior
 .
La conclusión es que con el Síndrome 111 se detecta y corrige error simple en x
3
 ----------------------------------------------------------------------------------------------------------------
2 -Dada la siguiente Matriz Generadora del Código de Grupo encontrar:
a) El Código de Grupo
b) Que errores no se detectan
c) analizar cómo se comporta el Código frente a los errores simples, realizando el
análisis para todos los síndromes.

    n = 5 columnas (5 dígitos)
           11000      g
1
  G =   00011      g
|     |       m = 3 Filas   |     |     |     |     |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
2
           01110      g
3

d) Para hallar el Código de Grupo V se debe realizar la combinación lineal de los
vectores g de G:
i

| v  = k |  x g +  | k  x g |         | + K x g |                  | + : Suma sin Acarreo |     |     |     |
| ------ | ------- | ------ | ------- | ------- | ---------------- | -------------------- | --- | --- | --- |
| i      | 1 1     | 2      | 2  ………. | m       | m                |                      |     |     |     |

Entonces damos todas las combinaciones posibles de K obteniendo los
vectores de V

| x x x    | x x k       |  k  k |     |     |     |     |     |     |     |
| -------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| 1  2  3  | 4 5       3 | 2 1   |     |     |     |     |     |     |     |
0  0  0  0  0     0  0  0    v = k xg + k xg +k xg = 0xg + 0xg +0xg
|     |     |     | 1   | 1 1     2 2  |   3 | 3   | 1     | 2    | 3     |
| --- | --- | --- | --- | ------------ | --- | --- | ----- | ---- | ----- |
1  1  0  0  0     0  0  1    v = k xg + k xg +k xg = 1xg + 0xg +0xg
|     |     |     |     |              |     |     |       |      |     |
| --- | --- | --- | --- | ------------ | --- | --- | ----- | ---- | --- |
|     |     |     | 2   | 1 1     2 2  |   3 | 3   | 1     | 2    | 3   |
0  0  0  1  1     0  1  0    v = k xg + k xg +k xg = 0xg + 1xg +0xg
|     |     |     | 3   | 1 1     2 2  |   3 | 3   | 1     | 2    | 3     |
| --- | --- | --- | --- | ------------ | --- | --- | ----- | ---- | ----- |
1  1  0  1  1     0  1  1    v = k xg + k xg +k xg = 0xg + 0xg +0xg
|                                |     |     | 4   | 1 1     2 2  |   3   | 3     | 1     | 2    | 2     |
| ------------------------------ | --- | --- | --- | ------------ | ----- | ----- | ----- | ---- | ----- |
| 0  1  1  1  0     1  0  0    v |     |     |     |              |       |       |       |      |       |
|                                |     |     | = k | xg + k xg    | +k xg | = 1xg | + 0xg | +0xg |       |
|                                |     |     | 5   | 1 1     2 2  |   3   | 3     | 1     | 2    | 3     |
1  0  1  1  0     1  0  1    v = k xg + k xg +k xg = 1xg + 0xg +1xg
|     |     |     | 6   | 1 1     2 2  |   3 | 3   | 1     | 2    | 3   |
| --- | --- | --- | --- | ------------ | --- | --- | ----- | ---- | --- |
0  1  1  0  1     1  1  0     v = k xg + k xg +k xg = 1xg + 1xg +0xg
|     |     |     | 7   | 1 1     2 2  |   3 | 3   | 1     | 2    | 3   |
| --- | --- | --- | --- | ------------ | --- | --- | ----- | ---- | --- |
1  0  1  0  1     1  1  1    v
|     |     |     | = k | xg + k xg    | +k xg | = 1xg | + 1xg | +1xg |     |
| --- | --- | --- | --- | ------------ | ----- | ----- | ----- | ---- | --- |
|     |     |     | 8   | 1 1     2 2  |   3   | 3     | 1     | 2    | 3   |

Quedando entonces:

0  0  0  0  0
1  1  0  0  0
0  0  0  1  1
1  1  0  1  1    = V  2m   filas    x  n Columnas

0  1  1  1  0
1  0  1  1  0
0  1  1  0  1
1  0  1  0  1

e) Los errores que no se detectan son donde hay unos en las palabras códigos
(es decir los errores que no se detectan coinciden con las palabras códigos)
| Error Doble en x     | y x |         |         |
| -------------------- | --- | ------- | ------- |
|                      | 1   | 2       |         |
| Error Doble en x     | y x |         |         |
|                      | 5   | 6       |         |
| Error Triple en x    | , x | x       |         |
|                      | 2   | 3 y  4  |         |
| Error Triple en x    | , x | x       |         |
|                      | 1   | 3 y  4  |         |
| Error Triple en x    | , x | x       |         |
|                      | 2   | 3 y  5  |         |
| Error Triple en x    | , x | x       |         |
|                      | 1   | 3 y  5  |         |
| Error Cuádruple en x |     | , x , x | x       |
|                      |     | 1 2     | 4 y  5  |

f)  Para realizar el análisis del comportamiento del  código frente a los errores se
debe encontrar primero la Matriz de Control de Paridad H base de V’
Para esto primero aplicamos la condición de ortogonalidad que permite encontrar  V’:
| Para todo v’ | € V’ resulta  v’ |     | x GT = 0      entonces:  |
| ------------ | ---------------- | --- | ------------------------ |
|              | i                |     | i                        |
                                             1   0  0
1   0  1
 (x’ ,x’ ,x’ ,x’ , x’ ) x  0   0  1      = ( 0 )  = (0 , 0 , 0)
| 1    2  |   3   4  |   5   |     |
| ------- | -------- | ----- | --- |
                                             0   1  1
|     |     | 0   | 1  0  |
| --- | --- | --- | ----- |

|     |     |     |     |
| --- | --- | --- | --- |

Recordando el procedimientopara el producto de matrices resulta:
| x’ x1 + x’ | x1 + x’ | x0 +x’ | x0 +x’ | x0 = 0      |
| ---------- | ------- | ------ | ------ | ----------- |
| 1          | 2       |   3    |   4    |   5         |
| x’ x0 + x’ | x0 + x’ | x0 +x’ | x1 +x’ | x1 = 0      |
| 1          | 2       |   3    |   4    |   5         |
| x’ x0 + x’ | x1 + x’ | x1 +x’ | x01 +  | x’ x0 = 0   |
| 1          | 2       |   3    |   4    |   5         |

Queda entonces un sistema de ecuaciones de 5 incógnitas con tres
ecuaciones:
x’ + x’  = 0                         Si fueran variables naturales tendría infinitas
| 1  2 |     |     |     |     |
| ---- | --- | --- | --- | --- |
x’ + x’  = 0                          soluciones , pero como las variables son
| 4  5 |     |     |     |     |
| ---- | --- | --- | --- | --- |
x’ + x’ + x’  = 0                  binarias podemos darle todos los valores
| 2  3  |   4 |     |     |     |
| ----- | --- | --- | --- | --- |
                                                    a dos  de las variables, de manera de obtener un
sistema de ecuaciones  de 3 ecuaciones con 3 incognitas (3x3)
Para esto es conveniente elegir aquellas 2 variables que más se repten en las
ecuaciones de manera de tener todas las variables independientes de un lado de la
igualdad.
Entonces observando nuestro sistema de ecuaciones vemos que las variables que más
| se repiten en las ecuaciones pueden ser ( x |     |     |     |  , x )    |
| ------------------------------------------- | --- | --- | --- | --------- |
2 4
Con lo cual ahora despejamos según lo visto anteriormente:
| x’  = x’ |         |     |     |     |
| -------- | ------- | --- | --- | --- |
| 1        | 2       |     |     |     |
| x’  = x’ |         |     |     |     |
| 5 4      |         |     |     |     |
| x’ = x’  | + x’    |     |     |     |
| 3  2     |   4     |     |     |     |
Ahora dando todos los valores a ( x’  , x’  ) obtenemos el espacio ortogonal
2 4
V´y luego extraemos la matriz H

                n  = 5 columnas
|             x’ |  x’  x’ |  x’  x’  |        |
| -------------- | ------- | -------- | ------ |
|                | 1    2  |   3   4  |   5    |
            0     0     0    0    0
 V’  =   0     0     1    1    1            2n-m   filas    = 25-3   = 22   = 4
            1     1     1    0    0
            1     1     0    1    1

Ahora hay que elegir una base de n x (n-m) = 5 columnas x 2 filas cuyos
vectores  sean independientes
En este caso cualquier par de vectores que NO contengan al vector Nulo
será base

            0     0     1    1    1
    H =  1     1     1    0    0

Ahora planteamos que una palabra de V con error multiplicada por HT debe dar distinto
de cero (síndrome):
| v  x H | T   = S   |     |     |
| ------ | --------- | --- | --- |
| ie     | i         |     |     |
Como no conocemos la palabra con error, será una incógnita de nuestra ecuación,
), conocemos HT y el síndrome conocemos sus dimensiones (1x n-
| (x , x , x | , x , x      |     |     |
| ---------- | ------------ | --- | --- |
| 1     2    | 3      4     | 5   |     |
m), así que lo proponemos :

) x HT  = Si
| (x , x , x | , x , x      |     |     |
| ---------- | ------------ | --- | --- |
| 1     2    | 3      4     | 5   |     |
No concemos el error  dato    proponemos Si = 0

SÍNDROME 01
                                 0 1
|             |     |                0 1   |     |
| ----------- | --- | -------------------- | --- |
    (x , x , x , x , x ) x   1 1     =  0 1         Podemos elegir cualquier síndrome,
| 1     | 2  3      4  |    5  |     |
| ----- | ------------ | ----- | --- |
                                          1 0                         en particular y por una cuestión de
                                 1 0                         comodidad elegimos contar  en

 en binario ( 1, 2, 3) - Ya que son 2n-m  - 1 = 25-3 – 1 = 3  Síndromes distintos
Queda entonces un sistema de ecuaciones de 5 incógnitas con dos
ecuaciones:
x  + x  +x = 0                              Si fueran variables naturales tendría infinitas
| 3   | 4   5   |     |     |
| --- | ------- | --- | --- |
x + x + x = 1                        soluciones , pero como las variables son
| 1   | 2      3   |     |     |
| --- | ---------- | --- | --- |
                                                  binarias podemos darle todos los valores
a tres de las variables, de manera de obtener un  sistema de 2 ecuaciones con 2
variables (2x2)
Para esto es conveniente elegir aquellas 3 variables que más se repiten en las
ecuaciones de manera de tener todas las variables independientes de un lado de la
| igualdad, por ejemplo . x |     | , x y x |     |
| ------------------------- | --- | ------- | --- |
|                           |     | 2  3    | 4   |
Además debemos recordar que la suma es sin acarreo y las variables son binarias con
lo cual las ecuaciones se resuelven según:
|     X  |  = x  + x |                                       |     |
| ------ | --------- | ------------------------------------- | --- |
|   5    | 3         | 4                                     |     |
|      X | = 1 + x   | + x                                   |     |
| 1      | 2         | 3                                     |     |

Ahora damos todos los valores a las variables  x , x , x  y obtenemos los valores de
2     3  4

x y x
1     5
|     x | x  x x  x     |         |     |
| ----- | ------------- | ------- | --- |
| 1     | 2   3    4    | 5       |     |
 1    0   0   0   0                            Esta es la Familia de palabras de V que

    1    0   0   1   1                            tienen un determinado error que dá como
    0    0   1   0   1                            resultado el Síndrome S  = 01, resumiendo es
1
    0    0   1   1   0                             Familia de Errores asociadas al Síndrome 01
    0    1   0   0   0
    0    1   0   1   1
    1    1   1   0   1
    1    1   1   1   0                                Entonces observando la Familia de Errores
Asociadas al Síndrome 01 vemos que hay
dos palabras con todos ceros y un solo uno en x  y en x , por lo tanto no podemos
1 2
corregir sólo se puede detectar.

La conclusión es que con el Síndrome 01 SOLO se detecta error simple en x ó x
1  2
También podría ser este síndrome causado por :
| Error Doble en x |     | yx  |
| ---------------- | --- | --- |
3    5
| Error Doble en x |     | yx  |
| ---------------- | --- | --- |
3    4
| Error Triple en x |     | , x x |
| ----------------- | --- | ----- |
1 4 y  5
| Error Triple en x |     | , x yx |
| ----------------- | --- | ------ |
2 4    5
| Error Cuádruple en x |     | , x , x yx |
| -------------------- | --- | ---------- |
1 3 4    5
| Error Cuádruple en x |     | , x , x yx |
| -------------------- | --- | ---------- |
1 2 3    4
Pero vamos a considerar el criterio de la mayor probabilidad, en este caso detección de
| Error unitario en x |     |  ó x   |
| ------------------- | --- | ------ |
1 2
SÍNDROME 10
Veamos ahora la Familia de Errores asociadas al Síndrome 10

                                 0 1
|             |           |                0 1                  |
| ----------- | --------- | ----------------------------------- |
|     (x ,    | x , x , x | , x ) x   1 1     =  1 0            |
| 1           | 2  3      | 4     5                             |
                                          1 0
                                 1 0
 Queda entonces un sistema de ecuaciones de 5 incógnitas con dos
ecuaciones:
| x  + x |  +x = 1                                 |     |
| ------ | --------------------------------------- | --- |
| 3      | 4   5                                   |     |
| x + x  | + x = 0                                 |     |
| 1      | 2      3                                |     |

Elegimos las mismas variables anteriores  x , x y x

2  3  4
|     X  = 1 +x |  + x    |                                       |
| ------------- | ------- | ------------------------------------- |
|   5           | 3       |   4                                   |
|      X        | = x + x |                                       |
| 1             | 2  3    |                                       |

Ahora damos todos los valores a las variables  x , x , x  y obtenemos los valores de
2     3  4
| x y x5 |      |     |
| ------ | ---- | --- |
| 1      | 6    |     |

|     x | x  x x  x     |         |
| ----- | ------------- | ------- |
| 1     | 2   3    4    | 5       |
 0    0   0   0   1                            Esta es la Familia de palabras de V que

    0    0   0   1   0                            tienen un determinado error que dá como
    1    0   1   0   0                            resultado el Síndrome S  = 10, resumiendo es
2
    1    0   1   1   1                             Familia de Errores asociadas al Síndrome 10
    1    1   0   0   1
    1    1   0   1   0
    0    1   1   0   0
    0    1   1   1   1                                Entonces observando la Familia de Errores
Asociadas al Síndrome 01 vemos que hay
dos palabras con todos ceros y un solo uno en x  y en x , por lo tanto no podemos
4 5
corregir sólo se puede detectar.
La conclusión es que con el Síndrome 10 SOLO se detecta error simple en x ó x
4  5
SÍNDROME 11
Veamos ahora la Familia de Errores asociadas al Síndrome 10

                                 0 1
|             |              |                0 1                  |
| ----------- | ------------ | ----------------------------------- |
|     (x      | , x , x , x  | , x ) x   1 1     =  1 1            |
| 1           |    2  3      | 4     5                             |
                                          1 0
                                 1 0
 Queda entonces un sistema de ecuaciones de 5 incógnitas con dos
ecuaciones:
| x  + x |  +x = 1                                 |     |
| ------ | --------------------------------------- | --- |
| 3      | 4   5                                   |     |
| x + x  | + x = 1                                 |     |
| 1      | 2      3                                |     |

Elegimos las mismas variables anteriores  x , x y x

2  3  4
|     X  |  = 1 +x + x |                                       |
| ------ | ----------- | ------------------------------------- |
|   5    | 3           | 4                                     |
|      X | = 1 +x + x  |                                       |
| 1      | 2           | 3                                     |

   Ahora damos todos los valores a las variables  x
, x , x  y obtenemos los valores
2     3  4
| de     x | y x5 |      |     |
| -------- | ---- | ---- | --- |
1     6

|     x | x  x x   |  x           |     |
| ----- | -------- | ------------ | --- |
| 1     | 2   3    | 4    5       |     |
 1    0   0   0   1                            Esta es la Familia de palabras de V que

    1    0   0   1   0                            tienen un determinado error que dá como
    0    0   1   0   0                            resultado el Síndrome S  = 11, resumiendo es
2
    0    0   1   1   1                             Familia de Errores asociadas al Síndrome 11
    0    1   0   0   1
    0    1   0   1   0
    1    1   1   0   0
    1    1   1   1   1                                Entonces observando la Familia de Errores
Asociadas al Síndrome 01 vemos que hay
una palabras con todos ceros y un solo uno en x  por lo tanto podemos corregir
3
La conclusión es que con el Síndrome 11 se detecta y corrige error simple en x
3 .
 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
3 -Dada la siguiente Matriz de Control de Paridad H encontrar:
a) El Código de Grupo y una de sus matrices generadoras
b) Indicar que errores no se detectan
c) Analizar cómo se comporta el Código frente a los errores simples, realizando el
análisis para todos los síndromes.
0 0 1 1 1             (n-m) x n = 2 x 5
H =   1 1 0  0 1

a) Para hallar el Código de Grupo V aplicamos la condición de ortogonalidad, donde
T
Para todo vector perteneciente a Código de Grupo V es: v x H = 0
i
|     |            |         |   0 1                        |
| --- | ---------- | ------- | ---------------------------- |
|     | (x  ,x  ,x |  ,x  ,x | ) x 0 1     =  0   = (0, 0)  |
|     | 1 2        | 3 4     | 5                            |
|     |            |         |   1 0                        |
                                1 0
|     |     |     |         1 1  |
| --- | --- | --- | ------------ |
|     |     |     |              |

|     | X  + X |  + X  = 0       |     |     |     |     |     |     |
| --- | ------ | --------------- | --- | --- | --- | --- | --- | --- |
|     | 3 4    | 5               |     |     |     |     |     |     |
X  + X  + X  = 0               Nos queda un Sistema de 2 ecuaciones con 5
|     | 1 2 | 5   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
incógnitas, por lo tanto podemos darle valores a 3 de ellas y obtener el
|     | resto de las variables , por ejemplo elegimos  x |     |     |     |     |     |  ,x  ,x    |     |
| --- | ------------------------------------------------ | --- | --- | --- | --- | --- | ---------- | --- |
|     |                                                  |     |     |     |     |     | 1 3 5      |     |
Quedando entonces:
|     | X  = X |  + X    |     |     |     |     |     |     |
| --- | ------ | ------- | --- | --- | --- | --- | --- | --- |
|     | 4 3    | 5       |     |     |     |     |     |     |
X  = X  + X          Ahora damos todos los valores x  ,x  ,x y obtenemos
|     | 2 1              | 5   |     |     |     |     | 2 3 4  |     |
| --- | ---------------- | --- | --- | --- | --- | --- | ------ | --- |
|     | los valores de x |     |  ,x |     |     |     |        |     |
1 5 :
|     | x  x  x |  x  x |     |     |     |     |     |     |
| --- | ------- | ----- | --- | --- | --- | --- | --- | --- |
|     | 1 2 3   | 4 5   |     |     |     |     |     |     |
0   0  0   0  0
0   1  0   1  1
0   0  1   1  0
0   1  1   0  1     = V   Código de Grupo
1   1  0   0  0
1   0  0   1  1                Una matriz Generadora es:
|     | 1   1  1   1  0  |     |     |     |               |     | 0   0  1   1  0  |     |
| --- | ---------------- | --- | --- | --- | ------------- | --- | ---------------- | --- |
|     | 1   0  1   0  1  |     |     |     |          G =  |     | 0   1  1   0  1  |     |
|     |                  |     |     |     |               |     | 1   1  0   0  0  |     |

Donde verificamos que ningún vector de G resulta combinación lineal de los
|     | restantes vectores, por ejemplo: g |     |     |  = g |  + g |     |     |     |
| --- | ---------------------------------- | --- | --- | ---- | ---- | --- | --- | --- |
|     |                                    |     |     | 3    | 1 2  |     |     |     |

b) Los errores que no se detectan son aquellos que coinciden con las
palabras códigos, o sea donde tengo unos en las palabras código:

| Error Doble en x     |     | yx4       | -   Error Doble en x |      | yx          |     |     |     |
| -------------------- | --- | --------- | -------------------- | ---- | ----------- | --- | --- | --- |
|                      |     | 3    5    |                      |      | 1    2      |     |     |     |
| Error Triple en x    |     | , x x     | -  Error Triple en x |      | , x yx      |     |     |     |
|                      |     | 2 4 y     | 5                    |      | 2 3    5    |     |     |     |
| Error Triple en x    |     | , x yx    | -  Error Triple en x |      | , x yx      |     |     |     |
|                      |     | 1 4       | 5                    |      | 1 3    5    |     |     |     |
| Error Cuádruple en x |     |           | , x , x yx           |      |             |     |     |     |
|                      |     | 1         | 2 3                  |   4  |             |     |     |     |
|                      |     |           |                      |      |             |     |     |     |

c) Ahora planteamos que una palabra de V con error multiplicada por HT debe dar
distinto de cero (síndrome):
T
| v  x H = S |     |     |
| ---------- | --- | --- |
| ie         | i   |     |
Como no conocemos la palabra con error, será una incógnita de nuestra ecuación,
), conocemos HT y el síndrome conocemos sus dimensiones (1x n-
| (x , x , x , x  | , x       |     |
| --------------- | --------- | --- |
| 1     2  3      | 4     5   |     |
m) = 1 x (5 -3) = 1fila x 2 columnas ,  así que lo proponemos :

) x HT  = Si
| (x , x , x , x  | , x       |     |
| --------------- | --------- | --- |
| 1     2  3      | 4     5   |     |
No concemos el error  dato    proponemos Si = 0

SÍNDROME 01

T
| x  x H | = S   |     |
| ------ | ----- | --- |
| ie     | I     |     |
                                     0 1
                                     0 1
| (x  ,x  ,x |  ,x  ,x | ) x 1 0     = 01   |
| ---------- | ------- | ------------------ |
| 1 2        | 3 4     | 5                  |
                                1 0
                                     1 1

| X  + X |  + X  = 0       |     |
| ------ | --------------- | --- |
| 3 4    | 5               |     |
X  + X  + X  = 1               Nos queda un Sistema de 2 ecuaciones con 5
| 1 2 | 5   |     |
| --- | --- | --- |
incógnitas, por lo tanto damos valores a 3 de ellas y obtener el resto de
las variables , elegimos igual que antes  x  ,x  ,x
1 3 5
Quedando entonces:
| X  = X     |  + X    |            |
| ---------- | ------- | ---------- |
| 4 3        | 5       |            |
| X  = 1 + X |  + X    |            |
| 2          | 1       | 5          |

Ahora damos todos los valores x  ,x  ,x y obtenemoslos valores
1 3 5
de x  ,x
| 2   | 4 :  |     |
| --- | ---- | --- |
|     |      |     |

| x  x  x  x  x |     |     |     |
| ------------- | --- | --- | --- |
| 1 2 3 4       | 5   |     |     |
0   1  0   0  0
0   0  0   1  1      Esta es la Familia de palabras de V que
0   1  1   1  0      tienen un determinado error y que dá como
0   0  1   0  1          resultado el Síndrome S  = 01, resumiendo es la
1
1   0  0   0  0      Familia de Errores asociadas al Síndrome 01
1   1  0   1  1
| 1   0  1   1  0  |     |     |     |
| ---------------- | --- | --- | --- |
| 1   1  1   0  1  |     |     |     |
 Entonces observando la Familia de Errores  asociadas al Síndrome 01
vemos que hay dos palabras con todos ceros y un solo uno en x  y en x , por lo tanto
1 2
no podemos corregir sólo se puede detectar.
La conclusión es que con el Síndrome 01 SOLO se detecta error simple en x ó x
1  2
SÍNDROME 10
                                     0 1
                                     0 1
) x 1 0     = 10
| (x  ,x  ,x  ,x |  ,x |     |     |
| -------------- | --- | --- | --- |
| 1 2 3 4        | 5   |     |     |
                                1 0
                                     1 1

| X  + X  + X                 |  = 1                 |                                |     |
| --------------------------- | -------------------- | ------------------------------ | --- |
| 3 4 5                       |                      |                                |     |
| X  + X  + X                 |  = 0                 |                                |     |
| 1 2 5                       |                      |                                |     |
| Elegimos igual que antes  x |                      |  ,x  ,x  - Quedando entonces:  |     |
1 3 5
| X  = 1 + X  + X |            |     |     |
| --------------- | ---------- | --- | --- |
| 4 3             | 5          |     |     |
| X  = X  + X     |            |     |     |
| 2 1 5           |            |     |     |

Ahora damos todos los valores x  ,x  ,x y obtenemoslos valores
1 3 4
de x  ,x
2 4 :
|     |     |     |     |
| --- | --- | --- | --- |

| x  x  x  x  x |     |     |     |
| ------------- | --- | --- | --- |
| 1 2 3 4       | 5   |     |     |
0   0  0   1  0
0   1  0   0  1      Esta es la Familia de palabras de V que
0   0  1   0  0      tienen un determinado error y que dá como
0   1  1   1  1          resultado el Síndrome S  = 10, resumiendo es la
1
1   1  0   1  0      Familia de Errores asociadas al Síndrome 10
1   0  0   0  1
| 1   1  1   0  0  |     |     |     |
| ---------------- | --- | --- | --- |
| 1   0  1   1  1  |     |     |     |
 Entonces observando la Familia de Errores  asociadas al Síndrome 10
vemos que hay dos palabras con todos ceros y un solo uno en x  y en x , por lo tanto
3 4
no podemos corregir sólo se puede detectar.
La conclusión es que con el Síndrome 10 SOLO se detecta error simple en x ó x
3  4
SÍNDROME 11
                                     0 1
                                     0 1
) = 1 0     = 11
| (x  ,x  ,x  ,x |  ,x |     |     |
| -------------- | --- | --- | --- |
| 1 2 3 4        | 5   |     |     |
                                1 0
                                     1 1

| X  + X  + X                 |  = 1                 |                                |     |
| --------------------------- | -------------------- | ------------------------------ | --- |
| 3 4 5                       |                      |                                |     |
| X  + X  + X                 |  = 1                 |                                |     |
| 1 2 5                       |                      |                                |     |
| Elegimos igual que antes  x |                      |  ,x  ,x  - Quedando entonces:  |     |
1 3 5
| X  = 1 + X  + X |            |     |     |
| --------------- | ---------- | --- | --- |
| 4 3             | 5          |     |     |
| X  = 1 + X  + X |            |     |     |
| 2 1             | 5          |     |     |

Ahora damos todos los valores x  ,x  ,x y obtenemoslos valores
1 3 4
de x  ,x
2 4 :
|     |     |     |     |
| --- | --- | --- | --- |

x x x x x
1 2 3 4 5
0 1 0 1 0
0 0 0 0 1 Esta es la Familia de palabras de V que
0 1 1 0 0 tienen un determinado error y que dá como
0 0 1 1 1 resultado el Síndrome S = 11, resumiendo es la
1
1 0 0 1 0 Familia de Errores asociadas al Síndrome 11
1 1 0 0 1
1 0 1 0 0
1 1 1 1 1
Entonces observando la Familia de Errores asociadas al Síndrome 11 vemos que hay
una palabras con todos ceros y un solo uno en x , por lo tanto podemos corregir
5
La conclusión es que con el Síndrome 11 se detecta y corrige error simple en x
5
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4 –Se requiere transmitie 7 mensajes protegidos contra error simple, encontrar el
código lineal que lo verifica:
Para dar respuesta a estas condiciones debemos recordar las dimensiones de los
espacios y las condiciones de detección y corrección de errores simples que se
deben cumplir.
n columnas (n dígitos de la palabra código)
0101…010
Código de Grupo V= (.....vi ……) 2m filas (palabras Códigos) con m<n
…… ……. Vector v (x x x x
i = 1 , 2….. j… n)
011….100 Siendo el elemento x = 0 ó 1
j
n columnas
…………….
Matriz generadora de V G = …… g …… m filas con m<n
i
g Linealmente Independientes
i :

                   n columnas
                     0101…010
 S.E.V             V’=    (.....vi ……)     2n-m  filas
| ortogonal a V |     |                       |     |     | v’     | (x’ x’    | x’ x’ ) |
| ------------- | --- | --------------------- | --- | --- | ------ | --------- | ------- |
|               |     |               …… …….  |     |     |   i =  | 1 ,  2….. | j… n    |
                    1011….100          Siendo el elemento  x’ = 0 ó 1
j

Cuya  base generadora llamada Matriz de Control de Paridad H:
n columnas
…………….
|   H = |      …… h ……     n- m  filas                    |     |     |     |     |     |     |
| ----- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
i
|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

 T
Condición de ortogonalidad  V     V’
x HT = 0            siendo HT la matriz transpuesta de H
| Para todo v | € V resulta    v |     |     |     |     |     |     |
| ----------- | ---------------- | --- | --- | --- | --- | --- | --- |
|             | i                |     | i   |     |     |     |     |
Para todo v’ € V’ resulta  v’ x GT = 0           siendo GT la matriz transpuesta de G
|     | i   |     | i   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

Por lo tanto el SÍNDROME es el resultado del producto del vector V con error o lo que es igual
I
al vector que modeliza el error por la matriz de control de paridad que tendrá como dimensión:
1 fila  x n-m columnas
v  x  H T    =  S   La cantidad de Síndromes distintos será 2n-m – 1
| ea  |     | ea           |     |     |     |     |     |
| --- | --- | ------------ | --- | --- | --- | --- | --- |


 (La combinación 0..0 corresponde a palabra OK no es síndrome)
1xn     nx(n-m)     1x(n-m)

Si se pretende detectar y corregir error simple en cada uno de los n dígitos de la palabra código
debe haber tantos síndromes distintos como dígitos tenga la palabra código:
| x = (x | , x , ……..x | )   |     |     |     |     |     |
| ------ | ----------- | --- | --- | --- | --- | --- | --- |
| i      | 1     2     |   n |     |     |     |     |     |

|       S | S ……. S   |     |     |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- | --- | --- |
|         | e1 ,  e2  |     | en  |     |     |     |     |
Es decir para detectar y corregir error simple en cada uno de los n dígitos de la palabra código
debe cumplirse que  la cantidad de síndromes distintos debe ser mayor ó igual  a n:
2n-m – 1 >  n
|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

RESOLUCIÓN
Habiendo realizado el repaso procedemos a resolver lo solicitado

Se solicita codificar 7 mensajes por lo tanto el Código de Grupo debe tener al menos 7
palabras código es decir :
        n dígitos
| V=   (.....vi ……)     2m    |     |     | >   |     |
| --------------------------- | --- | --- | --- | --- |
7   = = >  m = 3

Se requiere que se detecte y corrija error simple en cada uno de los n dígitos de las
palabras código, entonces:
x = (x , x , ……..x )        Se requiere un síndrome distinto para el error en cada uno
| i  1  |    2  |   n |     |     |
| ----- | ----- | --- | --- | --- |
      S S …... S de los n dígitoses decir  es decir “n Síndromes distintos”
| e1 ,  | e2  | en          |     |     |
| ----- | --- | ----------- | --- | --- |

Como la cantidad de Síndromes es :
T
v  x  H =  S   La cantidad de Síndromes distintos será 2n-m - 1
| ea  |     | ea           |     |     |
| --- | --- | ------------ | --- | --- |

1xn     nx(n-m)     1x(n-m)
| Deberá ser  2 |     | n-m  – 1 >  n       con m = 3 en nuestro caso  |     |     |
| ------------- | --- | ---------------------------------------------- | --- | --- |
Quedando
2 n-3  – 1 >  n       como n se encuentra en el numerador y como potencia  no se
puede despejar y se debe encontrar por prueba y error
4-3
| Con n=4    2 |     |  – 1 >  4         |     |     |
| ------------ | --- | ----------------- | --- | --- |
5-3
| Con n=5    2 |     |  – 1 >  5  |     |     |
| ------------ | --- | ---------- | --- | --- |
6-3
Con n=6    2  – 1 >  6  por lo tanto la cantidad de dígitos será  n = 6

T
| Ahora planteamos v |     |     |  x  H =  S |           |
| ------------------ | --- | --- | ---------- | --------- |
|                    |     |     | ea         | ea        |

Donde si bien no conocemos las palabras con error simple conocemos que
   -
la palabra nula con error simple es una palabra con todos ceros y un “1” en la
posición del error.
- La matriz HT no la conocemos, sólo tenemos sus dimensiones:
n filas x (n-m) columnas , en nuestro caso será de 6 filas x (6-3) columnas es
decir 6x3
-Los síndromes asociados a cada error los proponemos sabiendo que todos
son distintos de cero y de dimensión 1 x (n – m) es decir  1x3 . Puede igualarse a
cualquier  configuración de tres dígitos, pero lo más adecuado es contar en
binario ( 1, 2, 3, 4 , 5 y 6)
|                          h |          |   h | h         |     |     |     |     |
| -------------------------- | -------- | --- | --------- | --- | --- | --- | --- |
|                            |          | 11  | 12    13  |     |     |     |     |
|                            |        h |   h | h         |     |     |     |     |
|                            |          | 21  | 22    23  |     |     |     |     |
(1 0 0 0 0 0) x  h h h = 0 0 1    haciendo el producto resulta:
|     |     |    31   32     | 33       |     |     |     |              |
| --- | --- | -------------- | -------- | --- | --- | --- | ------------ |
|     |     | h h            | h        | h   |   h | h   | =  0 0 1     |
                                        41   42      43                               11 12    13
|      |        h | h            | h   |     |     |     |     |
| ---- | -------- | ------------ | --- | --- | --- | --- | --- |
|      |          | 51   52      | 53  |     |     |     |     |
|      |        h | h            | h   |     |     |     |     |
|      |          | 61   62      | 63  |     |     |     |     |

|                          h |          |   h | h         |     |     |     |     |
| -------------------------- | -------- | --- | --------- | --- | --- | --- | --- |
|                            |          | 11  | 12    13  |     |     |     |     |
|                            |        h |   h | h         |     |     |     |     |
|                            |          | 21  | 22    23  |     |     |     |     |
(0 1 0 0 0 0) x  h h h = 0 1 0      ===>  h   h h = 0 1 0
|                                         |          |    31   32     | 33          |     | 21  | 22    23  |     |
| --------------------------------------- | -------- | -------------- | ----------- | --- | --- | --------- | --- |
|                                         |          | h h            | h           |     |     |           |     |
|                                         |          | 41   42        | 43          |     |     |           |     |
|                                         |        h | h              | h           |     |     |           |     |
|                                         |          | 51   52        | 53          |     |     |           |     |
|                          h              |          | h              | h           |     |     |           |     |
|                                         |          | 61   62        | 63          |     |     |           |     |

|                          h              |          |   h            | h                        |     |      |        |          |
| --------------------------------------- | -------- | -------------- | ------------------------ | --- | ---- | ------ | -------- |
|                                         |          | 11             | 12    13                 |     |      |        |          |
|                                         |        h |   h            | h                        |     |      |        |          |
|                                         |          | 21             | 22    23                 |     |      |        |          |
| (0 0 1 0 0 0) x                         |          | h h            | h = 0 1 1       ===>   h |     | h    | h      | = 0 1 1  |
|                                         |          |    31   32     | 33                       |     | 31   | 32     | 33       |
|                                         |          | h h            | h                        |     |      |        |          |
|                                         |          | 41   42        | 43                       |     |      |        |          |
|                                         |        h | h              | h                        |     |      |        |          |
|                                         |          | 51   52        | 53                       |     |      |        |          |
|                          h              |          | h              | h                        |     |      |        |          |
|                                         |          | 61   62        | 63                       |     |      |        |          |

|                          h              |          |   h          | h           |               |              |            |
| --------------------------------------- | -------- | ------------ | ----------- | ------------- | ------------ | ---------- |
|                                         |          | 11 12        | 13          |               |              |            |
|                                         |        h |   h          | h           |               |              |            |
|                                         |          | 21 22        | 23          |               |              |            |
| (0 0 0 1 0 0) x                         |          | h h          | h = 1 0 0   |       ===>  h | h            | h = 1 0 0  |
|                                         |          | 31   32      | 32          |               | 41   42      | 43         |
|                                         |          | h h          | h           |               |              |            |
|                                         |          | 41   42      | 43          |               |              |            |
|                                         |        h | h            | h           |               |              |            |
|                                         |          | 51   52      | 53          |               |              |            |
|                          h              |          | h            | h           |               |              |            |
|                                         |          | 61   62      | 63          |               |              |            |

|                          h |          |   h      | h   |     |     |     |
| -------------------------- | -------- | -------- | --- | --- | --- | --- |
|                            |          | 11 12    | 13  |     |     |     |
|                            |        h |   h      | h   |     |     |     |
|                            |          | 21 22    | 23  |     |     |     |
(0 0 0 0 1 0) x  h h h = 1 0 1         ===>   h h h = 1 0 1
|                                         |          | 31   32      | 33          |     | 51   52      | 53   |
| --------------------------------------- | -------- | ------------ | ----------- | --- | ------------ | ---- |
|                                         |          | h h          | h           |     |              |      |
|                                         |          | 41   42      | 43          |     |              |      |
|                                         |        h | h            | h           |     |              |      |
|                                         |          | 51   52      | 53          |     |              |      |
|                          h              |          | h            | h           |     |              |      |
|                                         |          | 61   62      | 63          |     |              |      |

|                          h |          |   h      | h   |     |     |     |
| -------------------------- | -------- | -------- | --- | --- | --- | --- |
|                            |          | 11 12    | 13  |     |     |     |
|                            |        h |   h      | h   |     |     |     |
|                            |          | 21 22    | 23  |     |     |     |
(0 0 0 0 0 1) x  h h h = 1 1 0         ===>   h h h = 1 1 0
|                                         |          | 31   32      | 33         |     | 61   62      | 63   |
| --------------------------------------- | -------- | ------------ | ---------- | --- | ------------ | ---- |
|                                         |          | h h          | h          |     |              |      |
|                                         |          | 41   42      | 43         |     |              |      |
|                                         |        h | h            | h          |     |              |      |
|                                         |          | 51   52      | 53         |     |              |      |
|                          h              |          | h            | h          |     |              |      |
|                                         |          | 61   62      | 63         |     |              |      |

Entonces la matriz HT encontrada es:
|                |     | 0 0 1  |     |     |     |     |
| -------------- | --- | ------ | --- | --- | --- | --- |
|                |     | 0 1 0  |     |     |     |     |
|          HT =  |     | 0 1 1  |     |     |     |     |
|                |     | 1 0 0  |     |     |     |     |
|                |     | 1 0 1  |     |     |     |     |
|                |     | 1 1 0  |     |     |     |     |
|                |     |        |     |     |     |     |

Ahora solo resta aplicar la condición de ortogonalidad para encontrar los
vectores de V:
| Para todo v | € V resulta    v |     | x HT = 0  |
| ----------- | ---------------- | --- | --------- |
|             | i                |     | i         |

|                       |           |             0 0 1          |     |
| --------------------- | --------- | -------------------------- | --- |
|                       |           |             0 1 0          |     |
| (x , x , x            | , x , x   | , x ) x  0 1 1   = 0 0 0   |     |
| 1     2               | 3    4    | 5    6                     |     |
|                       |           |             1 0 0          |     |
|                       |           |             1 0 1          |     |
|                       |           |             1 1 0          |     |

x +x +x =  0                  Queda un Sistema de 3 ecuaciones con 6 incógnitas
| 4     5  |   6    |     |     |
| -------- | ------ | --- | --- |
x +x +x =  0                   Cómo son variables binarias le doy todos los valores
| 2     3  |   6    |     |     |
| -------- | ------ | --- | --- |
x +x + x =  0                    posibles a 3 ( que más se repiten en las ecuaciones y
| 1    3  |    5    |     |     |
| ------- | ------- | --- | --- |
                                              obtenemos las restantes 3 variables:
| x =x +x                           |                                |          |                 |
| --------------------------------- | ------------------------------ | -------- | --------------- |
| 4     5                           |   6                            |          |                 |
| x =x +x                           |                                |          |                 |
| 2     3                           |   6                            |          |                 |
| x =x +                            | x                              |          |                 |
| 1     3                           |    5                           |          |                 |
|                                 x |                                |   x      |   x   x   x   x |
|                                   |                                | 1     2  | 3 4    5    6   |
     0    0    0    0   0    0

|                 |     |      0    1    0    1   0    1  |     |
| --------------- | --- | ------------------------------- | --- |
|                 |     |      1    0    0    1   1    0  |     |
           1    1    0    0   1    1    = V   Código de Grupo
|     |     |      1    1    1    0   0    0    |     |
| --- | --- | --------------------------------- | --- |
|     |     |      1    0    1    1   0    1    |     |
|     |     |      0    1    1    1   1    0    |     |
|     |     |      0    0    1    0   1    1    |     |

El código requerido es de 7 palabras códigos por lo tanto  debemos elegirlas de
las 8 que tiene V . cualquiera de las 8 no hay criterio de elección)

     0    1    0    1   0    1
|     |     |      1    0    0    1   1    0  |
| --- | --- | ------------------------------- |
           1    1    0    0   1    1    = Código solicitado (una propuesta)
|     |     |      1    1    1    0   0    0    |
| --- | --- | --------------------------------- |
|     |     |      1    0    1    1   0    1    |
|     |     |      0    1    1    1   1    0    |
|     |     |      0    0    1    0   1    1    |

OBSERVACIÓN : Como todos los errores simples son detectados y corregidos
entonces el síndrome S  = 111 corresponderá a un error de orden superior
7

                                0 0 1
|            |           |             0 1 0          |
| ---------- | --------- | -------------------------- |
| (x , x , x | , x , x   | , x ) x  0 1 1   = 1 1 1   |
| 1     2    | 3    4    | 5    6                     |
|            |           |             1 0 0          |
|            |           |             1 0 1          |
|            |           |             1 1 0          |

x +x +x =  1                  Queda un Sistema de 3 ecuaciones con 6 incógnitas
| 4     5  |   6    |     |
| -------- | ------ | --- |
x +x +x =  1                   Cómo son variables binarias le doy todos los valores
| 2     3  |   6    |     |
| -------- | ------ | --- |
x +x + x =  1                    posibles a 3 ( que más se repiten en las ecuaciones y
| 1    3  |    5    |     |
| ------- | ------- | --- |
                                              obtenemos las restantes 3 variables:
| x =1 + x | +x        |                                |
| -------- | --------- | ------------------------------ |
| 4        | 5    6    |                                |
| x =1 + x | +x        |                                |
| 2        | 3    6    |                                |
| x =1 + x | + x       |                                |
| 1        | 3     5   |                                |

|     |     |      x   | x   x   x |   x   x       |     |     |     |
| --- | --- | -------- | --------- | ------------- | --- | --- | --- |
|     |     | 1        | 2  3      | 4    5    6   |     |     |     |
     1    1    0    1   0    0

|                 |     |      1    0    0    0   0    1  |     |     |     |     |     |
| --------------- | --- | ------------------------------- | --- | --- | --- | --- | --- |
|                 |     |      0    1    0    0   1    0  |     |     |     |     |     |
           0    0    0    1   1    1      Familia de errores asociadas al
|     |     |      0    0    1    1   0    0      Síndrome S7 = 111  |     |     |     |     |     |
| --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- |
           0    1    1    0   0    1       Con el Síndrome 111 sólo se detectan
           1    0    1    0   1    0        errores Dobles en x x ó x x ó x   x
|     |     |                                   |     |     | 1  6       | 2  5      3 | 4    |
| --- | --- | --------------------------------- | --- | --- | ---------- | ----------- | ---- |
|     |     |      1    1    1    1   1    1    |     |     |            |             |      |

 ---------------------------------------------------------------------------------------------------------------
5 –Se requiere transmitie 6 mensajes protegidos contra error simple los dos bit
más significativos y sólo detectar el resto, encontrar el código lineal que lo
verifica:
        n dígitos
| V=   (.....vi ……)     2m    |     | >   | 6   = = >  m = 3  |     |     |     |     |
| --------------------------- | --- | --- | ----------------- | --- | --- | --- | --- |

Se requiere que se detecte y corrija error simple en los dos dígitos más significativos de
las palabras código y sólo detectar error simple en el resto de los dígitos, entonces:
x = (x , x , ……..x )        Se requiere un síndrome distinto para el error en x y x
| i  1    |    2  |   n |     |     |     | 1     | 2    |
| ------- | ----- | --- | --- | --- | --- | ----- | ---- |
|       S | S   S |     |     |     |     |       |      |
       y otro síndrome distinto para solo detectar el resto de los
| e1 ,  | e2  | e3          |     |     |     |     |     |
| ----- | --- | ----------- | --- | --- | --- | --- | --- |
     errores  simples en los restantes dígitos
Como la cantidad de Síndromes es :
v  x  H T    =  S   La cantidad de Síndromes distintos será 2n-m - 1
| ea  |     | ea            |     |     |     |     |     |
| --- | --- | -------------- | --- | --- | --- | --- | --- |
1xn     nx(n-m)     1x(n-m)
|     | n-m |     |     |     | n-3 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Deberá ser  2  – 1 >  3       con m = 3 en nuestro caso    2  – 1 >  3
4-3
| Con n=4    2 |     |  – 1 >  3         |     |     |     |     |     |
| ------------ | --- | ----------------- | --- | --- | --- | --- | --- |

5-3
Con n=5    2  – 1 >  3  por lo tanto la cantidad de dígitos será  n = 5

T
| Ahora planteamos v |     |     |  x  H | =  S |           |     |     |     |     |
| ------------------ | --- | --- | ----- | ---- | --------- | --- | --- | --- | --- |
|                    |     |     | ea    |      | ea        |     |     |     |     |

Donde si bien no conocemos las palabras con error simple conocemos que la
-
palabra nula con error simple es una palabra con todos ceros y un “1” en la
posición del error.
- La matriz HT no la conocemos, sólo tenemos sus dimensiones:
n filas x (n-m) columnas , en nuestro caso será de 5 filas x (5-3) columnas es
decir 5x2
-Los síndromes asociados a cada error los proponemos sabiendo que todos
son distintos de cero y de dimensión 1 x (n – m) es decir  1x2 . Puede igualarse a
cualquier  configuración de dos dígitos, pero lo más adecuado es contar en
binario ( 1, 2, 3)
|                          h              |          |   h          |                     |     |       |               |     |     |     |
| --------------------------------------- | -------- | ------------ | ------------------- | --- | ----- | ------------- | --- | --- | --- |
|                                         |          | 11           | 12                  |     |       |               |     |     |     |
|                                         |        h |   h          |                     |     |       |               |     |     |     |
|                                         |          | 21           | 22                  |     |       |               |     |     |     |
| (1 0 0 0 0) x                           |          | h h          | = 0 1 ===>          |     | h   h | =  0 1        |     |     |     |
|                                         |          | 31           | 32                  |     | 11    | 12            |     |     |     |
|                                         |          | h h          |                     |     |       |               |     |     |     |
|                                         |          | 41   42      |                     |     |       |               |     |     |     |
|                                         |        h | h            |                     |     |       |               |     |     |     |
|                                         |          | 51   52      |                     |     |       |               |     |     |     |

|                          h |          |   h |         |     |     |     |     |     |     |
| -------------------------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- |
|                            |          | 11  | 12      |     |     |     |     |     |     |
|                            |        h |   h |         |     |     |     |     |     |     |
|                            |          | 21  | 22      |     |     |     |     |     |     |
(0 1 0 0 0) x    h h   = 1 0  ===>   h   h = 1 0      este síndrome debe ser
|                                         |          |    31   32     |      |     | 21  | 22    |     |                             |     |
| --------------------------------------- | -------- | -------------- | ---- | --- | --- | ----- | --- | --------------------------- | --- |
|                                         |          | h h            |      |     |     |       |     | distinto al anterior para   |     |
|                                         |          | 41   42        |      |     |     |       |     |                             |     |
|                                         |        h | h              |      |     |     |       |     | poder corregir error simple |     |
|                                         |          | 51   52        |      |     |     |       |     |                             |     |

|                          h |          |   h |          |     |     |     |     |     |
| -------------------------- | -------- | --- | -------- | --- | --- | --- | --- | --- |
|                            |          | 11  | 12       |     |     |     |     |     |
|                            |        h |   h |          |     |     |     |     |     |
|                            |          | 21  | 22       |     |     |     |     |     |
(0 0 1 0 0 ) x    h h = 1 1  ===>       h h = 1 1     este síndrome debe ser
|                                         |          |   31   32        |      |     | 31   32    |     |                               |     |
| --------------------------------------- | -------- | ---------------- | ---- | --- | ---------- | --- | ----------------------------- | --- |
|                                         |          | h h              |      |     |            |     | distinto a los anterior para  |     |
|                                         |          | 41   42          |      |     |            |     |                               |     |
|                                         |        h | h                |      |     |            |     | poder corregir  error simple  |     |
|                                         |          | 51   52          |      |     |            |     |                               |     |
|                          h              |          | h                |      |     |            |     |                               |     |
|                                         |          | 61   62          |      |     |            |     |                               |     |

|                          h |          |   h |         |     |     |     |     |     |
| -------------------------- | -------- | --- | ------- | --- | --- | --- | --- | --- |
|                            |          | 11  | 12      |     |     |     |     |     |
|                            |        h |   h |         |     |     |     |     |     |
|                            |          | 21  | 22      |     |     |     |     |     |
(0 0 0 1 0 ) x  h h = 1 1  ===>        h h = 1 1      este síndrome debe ser
|     |       | 31   32         |     |     | 41   42    |     |     |     |
| --- | ----- | --------------- | --- | --- | ---------- | --- | --- | --- |
h h                                                     igual al anterior porque
|                                         |     | 41   42      |     |     |     |     |     |     |
| --------------------------------------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
            h h                                                 sólo pide detectar error simple
|     |     | 51   52      |     |     |     |     |     |     |
| --- | --- | ------------ | --- | --- | --- | --- | --- | --- |

|                          h |          |   h |         |     |     |     |     |     |
| -------------------------- | -------- | --- | ------- | --- | --- | --- | --- | --- |
|                            |          | 11  | 12      |     |     |     |     |     |
|                            |        h |   h |         |     |     |     |     |     |
|                            |          | 21  | 22      |     |     |     |     |     |
(0 0 0 0 1 ) x    h h     = 1 1  ===>   h h = 1  1         este síndrome debe ser
|                                         |     |    31   32     |      |     | 51   52    |     |                          |     |
| --------------------------------------- | --- | -------------- | ---- | --- | ---------- | --- | ------------------------ | --- |
|                                         |     | h h            |      |     |            |     | igual al anterior porque |     |
|                                         |     | 41   42        |      |     |            |     |                          |     |
            h h                 sólo pide detectar error simple
|     |     | 51   52      |     |     |     |     |     |     |
| --- | --- | ------------ | --- | --- | --- | --- | --- | --- |

Entonces la matriz HT encontrada es:
|                |     | 0 1  |     |     |     |     |     |     |
| -------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
|                |     | 1 0  |     |     |     |     |     |     |
|          HT =  |     | 1 1  |     |     |     |     |     |     |
|                |     | 1 1  |     |     |     |     |     |     |
|                |     | 1 1  |     |     |     |     |     |     |
|                |     |      |     |     |     |     |     |     |
Ahora solo resta aplicar la condición de ortogonalidad para encontrar los
vectores de V:
x HT = 0
| Para todo v | € V resulta    v |     |     |     |     |     |     |     |
| ----------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
|             | i                |     | i   |     |     |     |     |     |

|                       |           |             0 1          |     |
| --------------------- | --------- | ------------------------ | --- |
|                       |           |             1 0          |     |
|      (x ,             | x , x , x | , x ) x  1 1   = 0 0     |     |
| 1                     | 2  3      | 4    5                   |     |
|                       |           |             1 1          |     |
|                       |           |             1 1          |     |
|                       |           |                          |     |

X +x + x +x =  0                  Queda un Sistema de 2 ecuaciones con 5 incógnitas
| 2     3 |    4     5   |     |     |
| ------- | ------------ | --- | --- |
X +x +x +x =  0                   Cómo son variables binarias le doy todos los valores
| 1     3  |   4     5   |     |     |
| -------- | ----------- | --- | --- |
posibles a 3 ( que más se repiten en las ecuaciones y
                                              obtenemos las restantes 2 variables:
| X =x +                             | x +x           |                                |            |
| ---------------------------------- | -------------- | ------------------------------ | ---------- |
| 2     3                            |    4     5     |                                |            |
| X =x                               | +x +x          |                                |            |
| 1     3                            |   4     5      |                                |            |
|                                  x |                |   x   x   x                    |   x        |
|                                    |                | 1     2  3                     | 4    5     |
     0    0    0    0   0

|                 |     |      1    1    0    0   1                            |     |
| --------------- | --- | ---------------------------------------------------- | --- |
|                 |     |      1    1    0    1   0                            |     |
|                 |     |      0    0    0    1   1     = V   Código de Grupo  |     |
|                 |     |      1    1    1    0   0                            |     |
|                 |     |      0    0    1    0   1                            |     |
|                 |     |      0    0    1    1   0                            |     |
|                 |     |      1    1    1    1   1                            |     |

El código requerido es de 6 palabras códigos por lo tanto  debemos elegirlas de
las 8 que tiene V   (cualquiera de las 8 no hay criterio de elección)
                                   0    1    0    0   1
|     |     |         1    0    0    1   0                         |     |
| --- | --- | ---------------------------------------------------- | --- |
|     |     |         0    0    0    1   1     = Código requerido  |     |
|     |     |         1    1    1    0   0                         |     |
|     |     |         0    0    1    0   1                         |     |
|     |     |         0    0    1    1   0                         |     |

6 –Se requiere transmitie 5 mensajes protegidos contra error simple el bit más
significativos y sólo detectar el resto, excepto el bit menos significativo que no
se necesita detectar error - encontrar el código lineal que lo verifica:
n dígitos
V= (.....vi ……) 2m > 5 = = > m = 3
Se requiere que se detecte y corrija error simple en el bit más significativo sólo detectar
error simple en el resto excepto en el menos significativo que no se requiere detectar
error simple:
x = (x ,x , …x ,x ) Se requiere un síndrome para el error en x
i 1 2 n-1 n 1
S S =0 y otro síndrome distinto para solo detectar el resto de los
e1 , e2
errores simples excepto en el menos significativo que no se
requiere detectar error simple
Como la cantidad de Síndromes es :
v x H T = S La cantidad de Síndromes distintos será 2n-m - 1
ea ea

1xn nx(n-m) 1x(n-m)
n-m n-3
Deberá ser 2 – 1 > 2 con m = 3 en nuestro caso 2 – 1 > 2
4-3
Con n=4 2 – 1 > 2
5-3
Con n=5 2 – 1 > 2 por lo tanto la cantidad de dígitos será n = 5
T
Ahora planteamos v x H = S
ea ea
Donde si bien no conocemos las palabras con error simple conocemos que la
-
palabra nula con error simple es una palabra con todos ceros y un “1” en la
posición del error.

- La matriz HT no la conocemos, sólo tenemos sus dimensiones:
n filas x (n-m) columnas , en nuestro caso será de 5 filas x (5-3) columnas es
decir 5x2
-Los síndromes asociados a cada error los proponemos sabiendo que todos
son distintos de cero y de dimensión 1 x (n – m) es decir  1x3 . Puede igualarse a
cualquier  configuración de dos dígitos, pero lo más adecuado es contar en
binario ( 1, 2, 3, 4 , 5)
|                          h              |          |   h          |                     |     |       |               |     |     |     |
| --------------------------------------- | -------- | ------------ | ------------------- | --- | ----- | ------------- | --- | --- | --- |
|                                         |          | 11           | 12                  |     |       |               |     |     |     |
|                                         |        h |   h          |                     |     |       |               |     |     |     |
|                                         |          | 21           | 22                  |     |       |               |     |     |     |
| (1 0 0 0 0) x                           |          | h h          | = 0 1 ===>          |     | h   h | =  0 1        |     |     |     |
|                                         |          | 31           | 32                  |     | 11    | 12            |     |     |     |
|                                         |          | h h          |                     |     |       |               |     |     |     |
|                                         |          | 41   42      |                     |     |       |               |     |     |     |
|                                         |        h | h            |                     |     |       |               |     |     |     |
|                                         |          | 51   52      |                     |     |       |               |     |     |     |

|                          h |          |   h |         |     |     |     |     |     |     |
| -------------------------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- |
|                            |          | 11  | 12      |     |     |     |     |     |     |
|                            |        h |   h |         |     |     |     |     |     |     |
|                            |          | 21  | 22      |     |     |     |     |     |     |
(0 1 0 0 0) x    h h   = 1 0  ===>   h   h = 1 0      este síndrome debe ser
|                                         |          |    31   32     |      |     | 21  | 22    |     |                             |     |
| --------------------------------------- | -------- | -------------- | ---- | --- | --- | ----- | --- | --------------------------- | --- |
|                                         |          | h h            |      |     |     |       |     | distinto al anterior para   |     |
|                                         |          | 41   42        |      |     |     |       |     |                             |     |
|                                         |        h | h              |      |     |     |       |     | poder corregir error simple |     |
|                                         |          | 51   52        |      |     |     |       |     |                             |     |
|                                         |          |                |      |     |     |       |     |                             |     |
|                                         |          |                |      |     |     |       |     |                             |     |

|                          h |          |   h |          |     |     |     |     |     |     |
| -------------------------- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- |
|                            |          | 11  | 12       |     |     |     |     |     |     |
|                            |        h |   h |          |     |     |     |     |     |     |
|                            |          | 21  | 22       |     |     |     |     |     |     |
(0 0 1 0 0 ) x    h h = 1 0  ===>       h h = 1 0     este síndrome debe ser
|                                         |          |   31   32        |      |     | 31   | 32    |     |                               |     |
| --------------------------------------- | -------- | ---------------- | ---- | --- | ---- | ----- | --- | ----------------------------- | --- |
|                                         |          | h h              |      |     |      |       |     | distinto a los anterior para  |     |
|                                         |          | 41   42          |      |     |      |       |     |                               |     |
|                                         |        h | h                |      |     |      |       |     | poder corregir  error simple  |     |
|                                         |          | 51   52          |      |     |      |       |     |                               |     |
|                          h              |          | h                |      |     |      |       |     |                               |     |
|                                         |          | 61   62          |      |     |      |       |     |                               |     |

|                          h |     |   h |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- |
11 12
|     |        h |   h |         |     |     |     |     |
| --- | -------- | --- | ------- | --- | --- | --- | --- |
|     |          | 21  | 22      |     |     |     |     |
(0 0 0 1 0 ) x  h h = 1 0  ===>        h h = 1 0      este síndrome debe ser
|     |       | 31   32         |     |     | 41   42    |     |     |
| --- | ----- | --------------- | --- | --- | ---------- | --- | --- |
h h                                                     igual al anterior porque
|                                         |     | 41   42      |     |     |     |     |     |
| --------------------------------------- | --- | ------------ | --- | --- | --- | --- | --- |
            h h                                                 sólo pide detectar error simple
51   52

|                          h |          |   h |         |     |     |     |     |
| -------------------------- | -------- | --- | ------- | --- | --- | --- | --- |
|                            |          | 11  | 12      |     |     |     |     |
|                            |        h |   h |         |     |     |     |     |
|                            |          | 21  | 22      |     |     |     |     |
(0 0 0 0 1 ) x    h h     = 0 0  ===>   h h = 0  0         Como no se desea
|                                         |     |    31   32     |      |     | 51   52    |                        |     |
| --------------------------------------- | --- | -------------- | ---- | --- | ---------- | ---------------------- | --- |
|                                         |     | h h            |      |     |            | detectar error debe    |     |
|                                         |     | 41   42        |      |     |            |                        |     |
            h h  ser el producto igual a cero como si fuera palabra ok
|     |     | 51   52      |     |     |     |     |     |
| --- | --- | ------------ | --- | --- | --- | --- | --- |

Entonces la matriz HT encontrada es:
|     |     | 0 1  |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- |
|     |     | 1 0  |     |     |     |     |     |
       HT =
|     |     | 1 0  |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- |
|     |     | 1 0  |     |     |     |     |     |
|     |     | 0 0  |     |     |     |     |     |
|     |     |      |     |     |     |     |     |
Ahora solo resta aplicar la condición de ortogonalidad para encontrar los
vectores de V:
| Para todo v | € V resulta    v |     | x HT = 0  |     |     |     |     |
| ----------- | ---------------- | --- | --------- | --- | --- | --- | --- |
|             | i                |     | i         |     |     |     |     |

|                       |         |             0 1            |     |     |     |     |     |
| --------------------- | ------- | -------------------------- | --- | --- | --- | --- | --- |
|                       |         |             1 0            |     |     |     |     |     |
|      (x ,             | x , x , | x , x ) x  1 0   = 0 0     |     |     |     |     |     |
| 1                     | 2  3    |    4    5                  |     |     |     |     |     |
|                       |         |             1 0            |     |     |     |     |     |
|                       |         |             0 0            |     |     |     |     |     |
|                       |         |                            |     |     |     |     |     |

X +x + x =  0                  Queda un Sistema de 2 ecuaciones con 4 incógnitas (en
| 2     3 |    4   |     |     |     |
| ------- | ------ | --- | --- | --- |
X +x +x =  0                   realidad  son 5 incógnitas)  aunque x  no figure en las
| 1     3  |   4   |     |     | 5   |
| -------- | ----- | --- | --- | --- |
ecuaciones también se le debe dar todos los valores posibles
| X =x +                             | x                                 |             |            |     |
| ---------------------------------- | --------------------------------- | ----------- | ---------- | --- |
| 2     3                            |    4                              |             |            |     |
| X =x                               | +x                                |             |            |     |
| 1     3                            |   4                               |             |            |     |
|                                  x |                                   |   x   x   x |   x        |     |
|                                    |                                   | 1     2  3  | 4    5     |     |
     0    0    0    0   0

|                 |        0    0    0    0   1                            |     |     |     |
| --------------- | ------------------------------------------------------ | --- | --- | --- |
|                 |        1    1    0    1   0                            |     |     |     |
|                 |        1    1    0    1   1     = V   Código de Grupo  |     |     |     |
           1    1    1    0   0               Cómo se puede observar en el
           1    1    1    0   1              código de grupo, la palabra código
           0    0    1    1   0             con error unitario en x  no va a ser
5
           0    0    1    1   1          detectada como error porque pertenece al
   código

El código requerido es de 5 palabras códigos por lo tanto  debemos elegirlas de
las 8 que tiene V (cualquiera de las 8 no hay criterio de elección)
                                1    1    0    1   0
|     |        1    1    0    1   1     = Código solicitado  |     |     |     |
| --- | ---------------------------------------------------- | --- | --- | --- |
|     |        1    1    1    0   0                          |     |     |     |
|     |        1    1    1    0   1                          |     |     |     |
|     |        0    0    1    1   0                          |     |     |     |

 ==============================================================
|     |     |     |     |     |
| --- | --- | --- | --- | --- |

RESUMIENDO
SE PUEDEN PRESENTAR TRES TIPOS DE REQUERIMIENTOS
- Datos G – Obtener V y análisis de Síndromes
G  Comb. Lin.  V - Aplic. Con. Ortog. v’ x GT = 0  V’  H base  HT 
i
v x HT = S Se tiene la familia de errores asociados a cada síndrome
ie i
- Datos H - Obtener V y Análisis de Síndromes
Aplic. Con. Ortog. v x HT = 0  V - Teniendo H  HT  v x HT = S Se tiene la
i ie i
familia de errores asociados a cada síndrome
- Datos cant. Palabras Códigos y Condición de Detección y Corrección de
Errores Simples - Obtener V
-Cant. Palabras Códigos = 2m  m
-Cond. Detecc y Correcc. 2n-m -1 > Cant Sind Neces.  n
-Planteando e x HT = S , siendo e = (00..010..0) Todos ceros y un 1
i i i
donde hay error, se adopta los S se encuentran las filas de HT
i
- Planteando la cond. Ortog. v x HT = 0 se encuentra V se eligen las
i
palabras códigos que se necesitan.