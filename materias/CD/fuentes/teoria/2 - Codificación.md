CCCooodddiiifffiiicccaaaccciiióóónnn – Unidad N°4
Comunicaciones  -
Ingeniería en Sistemas de Información

CCCOOODDDIIIFFFIIICCCAAACCCIIIÓÓÓNNN

4.1   IIINNNTTTRRROOODDDUUUCCCCCCIIIÓÓÓNNN
  Desde  el  momento  que  nos  planteamos  el  problema  del  manejo  de  la
información (ej.: transmisión, recepción, almacenamiento, etc.); surge la necesidad de
representar de alguna manera, esta información, que vendrá dada por eventos o sucesos,
para de esta forma poder transmitirlas por un “canal” o línea de comunicación, en forma
de señal eléctrica, lumínicas, electromagnéticas, etc. Y de igual modo poder registrar o
almacenar esta información, ya sea electrónica, magnética o mecánicamente, etc.

Definición:  Si denominamos S = (s ; s ; ..........; s ) al conjunto de símbolos de un
1 2 q
alfabeto dado; queda definida una codificación al poner en correspondencia todas las
secuencias posibles de símbolos de S con secuencia de símbolos de algún otro alfabeto
Z = (z ; z ; ...........; z). Entonces “S” recibe el nombre de alfabeto fuente y “Z” alfabeto
|     | 1 2 |     | r   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
código.

| 4.2   CCCÓÓÓDDDIIIGGGOOO    |     | BBBLLLOOOQQQUUUEEE  |     |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- | --- |
  Es  aquel  que  asigna  a  cada  uno  de  los  símbolos  del  código  fuente  S  una
secuencia fija de símbolos del alfabeto código Z. Estas secuencias fijas (secuencias Z)
j
reciben el nombre de palabras código.
|     | S   |     | Z  (z | ; z   | ; ..........; z | )   |
| --- | --- | --- | ----- | ----- | --------------- | --- |
|     | 1   |     | 1     | 11 12 |                 | 1r  |
|     | S   |     | Z  (z | ; z   | ; ..........; z | )   |
|     | 2   |     | 2     | 21 22 |                 | 2r  |

|     | S  j |     | Z (z j | j1 ; z j2 ; ............; z |     | jr )  |
| --- | ---- | --- | ------ | --------------------------- | --- | ----- |

| 4.3   CCCÓÓÓDDDIIIGGGOOO   NNNOOO |     |     | ---SSSIIINNNGGGUUULLLAAARRR  |     |     |     |
| --------------------------------- | --- | --- | ---------------------------- | --- | --- | --- |
  Es aquel en que todas sus palabras son distintas:
|     | S 1   |     | 1   |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- |
|     | S     |     | 11  |     |     |     |
|     | 2     |     |     |     |     |     |
|     | S     |     | 00  |     |     |     |
3
|     | S   |     | 10  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
4

| 4.4   CCCÓÓÓDDDIIIGGGOOOSSS    |     |     | UUUNNNÍÍÍVVVOOOCCCAAAMMMEEENNNTTTEEE   DDDEEECCCOOODDDIIIFFFIIICCCAAABBBLLLEEESSS  |     |     |     |
| ------------------------------ | --- | --- | ---------------------------------------------------------------------------------- | --- | --- | --- |
  Se dice que un código es unívocamente decodificable si a cualquier secuencia de
palabras código, le corresponde una y sólo una secuencia de símbolos de la fuente.
  Por Ejemplo
|     |     |     | S   |     | 1   |     |
| --- | --- | --- | --- | --- | --- | --- |
1
|     |     |     | S   |     | 11  |     |
| --- | --- | --- | --- | --- | --- | --- |
|     |     |     | 2   |     |     |     |
|     |     |     | S   |     | 00  |     |
3
|     |     |     | S 4   |     | 10  |     |
| --- | --- | --- | ----- | --- | --- | --- |
  Si se recepciona: 1100 puede corresponder a S  y S  o a S , S  y S .
2 3 1 1 3
Veamos que este código es no singular al considerar los símbolos individuales,
pero es singular considerando alguna secuencia.

CCCooodddiiifffiiicccaaaccciiióóónnn – Unidad N°4
Comunicaciones  -
Ingeniería en Sistemas de Información

  Por lo que podemos dar otra definición de código unívoco: Un código bloque se
dice unívocamente decodificado sí y solo sí su extensión de orden n es no singular para
cualquier valor finito de n.

  Consideremos una codificación cuyas palabras código son de igual longitud. En
este  caso,  indudablemente  el  código  es  unívoco.  (siempre  que  sea  no  singular  el
original).
  Otro  caso  son  los  llamado  códigos  “coma”;  este  nombre  se  debe  a  que  el
comienzo o el fin de cada palabra está señalizada por un cero o por un uno.

Ejemplo
|     |     |       | Código A  |   Código B  |     |
| --- | --- | ----- | --------- | ----------- | --- |
|     |     | S     |      0    |       1     |     |
1
|     |     | S 2     |      01    |       01    |     |
| --- | --- | ------- | ---------- | ----------- | --- |
|     |     | S 3     |      011   |       001   |     |
|     |     | S       |      0111  |       0001  |     |
4
  De esta forma se identifica cada palabra.

| 4.5   CCCÓÓÓDDDIIIGGGOOOSSS    | IIINNNSSSTTTAAANNNTTTÁÁÁNNNEEEOOOSSS  |     |     |     |     |
| ------------------------------ | ------------------------------------- | --- | --- | --- | --- |
  Retomando el ejemplo anterior, donde los códigos A y B eran unívocos. Si
estamos  recepcionando  palabras  según  el  código  A  no  seriamos  capaces  de
decodificarlas instantáneamente  según las vamos recibiendo. Por ejemplo, si recibimos
la palabra 01, no podemos decir que corresponde a S 2  hasta que hayamos recibido el
símbolo siguiente. Si el próximo es un 0 (cero) entonces si decimos que correspondía a
S , si es un 1 (uno) debemos esperar el próximo, etc.
2
  Si  en  cambio,  utilizamos  el  código  B,  podemos  decodificar  las  palabras
instantáneamente.

CONDIDCeIOfinNi ción: Sea Z = z ; z ; .........; z  una palabra de código. Se denomina prefijo de
|                               | i   | i1 i2 | im                          |     |     |
| ----------------------------- | --- | ----- | --------------------------- | --- | --- |
| esta palabra a la secuencia z |     | ; z   | ; .........; z  con j  m.  |     |     |
|                               |     | i1 i2 | ij                          |     |     |
  A partir de esto se puede enunciar: “La condición necesaria y suficiente para que
un código sea instantáneo es que ninguna palabra del código coincida con el prefijo de
otra.

| 4.6   IIINNNEEECCCUUUAAACCCIIIÓÓÓNNN   DDDEEE    |     | KKKRRRAAAFFFTTT  |     |     |     |
| ------------------------------------------------ | --- | ---------------- | --- | --- | --- |

Teorema
|   Si los enteros l |     | ; l ; ..........; l |  satisfacen la inecuación:  |     |     |
| ------------------ | --- | ------------------- | --------------------------- | --- | --- |
|                    |     | 1 2                 | q                           |     |     |

Comunicaciones -
CCCooodddiiifffiiicccaaaccciiióóónnn
– Unidad N°4
Ingeniería en Sistemas de Información
Entonces esta es condición suficiente y necesaria para que exista al menos un
código instantáneo de r símbolos en su alfabeto y cuyas q palabras códigos tienen las
longitudes l ; l ; ..........; l respectivamente.
1 2 q
Nota: el teorema no dice que cualquier código cuyas longitudes cumplan la condición
(4.6.1) es un código instantáneo.
Ejemplo
S 0
1
S 00
2
S 11
3
este código satisface la ec.(4.6.1) sin embargo no es un código, instantáneo. El teorema
dice que existe algún código de longitud 1,2,2 que es instantáneo, por ejemplo el:
S 0
1
S 10
2
S 11
3
4.7 EEECCCUUUAAACCCIIIÓÓÓNNN DDDEEE MMMCCC MMMIIILLLLLLAAANNN
Dado que los códigos instantáneos son una sub-clase de los unívocos, la
condición suficiente para que exista, al menos un código unívoco, es que las longitudes
l verifiquen la expresión:
i
( 4.7.1 )
es decir, si las longitudes l ; l ; ...........; l satisfacen la relación pueden
1 2 q
construirse con ellas un código unívoco. La condición necesaria fue demostrada por Mc.
Millan.

CCCooodddiiifffiiicccaaaccciiióóónnn – Unidad N°4
Comunicaciones  -
Ingeniería en Sistemas de Información

4.8   LLLOOONNNGGGIIITTTUUUDDD   MMMEEEDDDIIIAAA   DDDEEE   UUUNNN   CCCÓÓÓDDDIIIGGGOOO
  Hasta  ahora  hemos  visto    las  condiciones  que  debe  cumplí  un  código
instantáneo. Dado el caso real de una fuente de información  que emite símbolos.
Codificamos con A y B.
|     |     |     | Código A  |     | Código B  |     |
| --- | --- | --- | --------- | --- | --------- | --- |
|     | S   |     |      00   |     |     1     |     |
1
|     | S     |     |      10  |     |     10   |     |
| --- | ----- | --- | -------- | --- | -------- | --- |
|     | 2     |     |          |     |          |     |
|     | S 3   |     |      11  |     |     110  |     |

  Existiendo  la  probabilidad  de  crearse  otros  distintos  de  los  precedentes.
Entonces, ¿cuál es el más conveniente desde el punto de vista de la economía?
  Indudablemente, cabría la pregunta: ¿Qué frecuencia de aparición tienen los
símbolos?

| DDDEEEFFFIIINNNIIICCCIIIOOONNNEEESSS | :::    |     |     |     |     |     |
| ------------------------------------ | ------ | --- | --- | --- | --- | --- |

Frecuencia Relativa: la frecuencia relativa de aparición de un evento es la suma
de las veces que este aparece dividido por la cantidad total de eventos que componen la
muestra.

    Ejemplo:
      a b c a a c b b a b a a c c a a a b                 -es una muestra-
|   frecuencia relativa de a = 9/ |     |     |     |  = 1/   |     |     |
| ------------------------------- | --- | --- | --- | ------- | --- | --- |
|                                 |     |     | 18  | 2       |     |     |

  Muestra Significativa o representativa: es aquella en que podemos tomar a la
frecuencia relativa como probabilidad.

Pasamos a codificar a los eventos “a”, “b” y “c”.
|   a - - - -  con palabra código de longitud l |     |     |     |     | a   |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- |
|   b - - - -  con palabra código de longitud l |     |     |     |     |     |     |
b
| c - - - -  con palabra código de longitud l |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- |
c

Entonces la longitud de la muestra (4.8.1) con los eventos codificados será
|     | L   |  = l  . N |  + l  . N |  + l  . N   |     |     |
| --- | --- | --------- | --------- | ----------- | --- | --- |
|     | M   | a a       | b b       | c c         |     |     |

  donde N es el número de veces que aparece el evento i en la muestra.
i

| L (longitud promedio) = LM/ |     |     |  = N | /  l  + N / |  l  + N / |  l   |
| --------------------------- | --- | --- | ---- | ----------- | --------- | ---- |
|                             |     |     | TM a | TM a b      | TM b c    | TM c |

|     |     |     |     | f f                  |              f |     |
| --- | --- | --- | --- | -------------------- | -------------- | --- |
|     |     |     |     | a                    | b c            |     |

donde:
  TM: total de eventos de la muestra.
|   f       es la frecuencia relativa del suceso i.  |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
i:

  Si  la  frecuencia  es  representativa,  la  frecuencia  relativa  coincide  con  la
probabilidad del suceso a.

Comunicaciones -
CCCooodddiiifffiiicccaaaccciiióóónnn
– Unidad N°4
Ingeniería en Sistemas de Información
Luego:
L = P(a) l + P(b) l + P(c) l
a b c
RRREEESSSUUUMMMIIIEEENNNDDDOOO :::
Dado un código bloque que asocia los símbolos de una fuente S ; S ; .......; S
1 2 N
con las palabras Z ; Z ; .........; Z y las probabilidades de los símbolos son
1 2 N
P ; P ; .....; P . La longitud media del código L se define como:
1 2 N
Desde el punto de vista económico nos interesan aquellos códigos en que la
longitud es mínima.
Definición: dada la fuente S diremos que un código instantáneo aplicado a S es
compacto (respecto a S) si su longitud media es igual o menor que la longitud media de
todos los códigos instantáneos que puedan aplicarse a la misma fuente y al mismo
alfabeto.
Es indudable que para obtener una longitud mínima, si el esquema de
probabilidades tiene la forma ( I ) el esquema de longitudes deberá ser de la forma ( II ).
La mayor probabilidad – menor longitud de palabra
Si la fuente tiene un esquema equiprobable de símbolos, las longitudes de las
palabras códigos se independizan del esquema de probabilidades.
Dado que las P son  0 y las l  0 de (4.8.1) resulta que L  0.
i i
4.9 CCCOOOTTTAAA IIINNNFFFEEERRRIIIOOORRR DDDEEE LLLAAA LLLOOONNNGGGIIITTTUUUDDD MMMEEEDDDIIIAAA ...
Dado que a nosotros nos interesa obtener una longitud mínima de la
codificación, comenzaremos con una pregunta; ¿Hasta dónde podemos disminuir la
longitud media?
Teorema: La longitud media de un código es mayor o igual que la entropía de la fuente
dividida por el log del número de símbolos del alfabeto código.
2

Comunicaciones -
CCCooodddiiifffiiicccaaaccciiióóónnn
– Unidad N°4
Ingeniería en Sistemas de Información
H(s)/log r  L (logaritmo base 2 de x: log x)
Demostración:
Es fácil demostrar que: ln xz-1 (4.9.1)
multiplicando (4.9.1) por –1 :
ln 1/  1-z (4.9.2)
X
Sean Z (z ; z ; ..........; z ) e Y(y ; y ; ..........; y ) dos conjuntos de
1 2 q 1 2 q
probabilidades; es decir: z  0, y  0 i,j
i j
(4.9.3)
podemos escribir, haciendo uso de: log z = 1/log a
a b
o sea:
Y aplicando la inecuación (4.9.1) a cada término de la  ( I ) obtenemos:

Comunicaciones -
CCCooodddiiifffiiicccaaaccciiióóónnn
– Unidad N°4
Ingeniería en Sistemas de Información
Luego:
que será una igualdad,  valor de i si y sólo si z = y
i i
Consideremos una fuente de memoria de símbolos S ; S ; .........; S con sus
1 2 q
probabilidades P ; P ; ..........; P . Supongamos un código bloque que codifica a la fuente
1 2 q
S con un alfabeto de r símbolos y l la longitud de la palara que codifica a S. La
1 i i
entropía valdrá:
Supongamos además que Q ; Q ; ...........; Q son números tales que Q  0
1 2 q 1
Luego, de acuerdo a la (4.9.5) podemos escribir:
Igualdad para todo i si y sólo Q = P
i i
La (4.9.6) es valida para conjunto de números positivos, Q, cuya suma sea la
i
unidad. En particular para:
Luego:

Comunicaciones -
CCCooodddiiifffiiicccaaaccciiióóónnn
– Unidad N°4
Ingeniería en Sistemas de Información
Si exigimos que el código sea instantáneo por Kraft; ( II ) es  1  log. ( II )  0
- H(s)  log r L –
- H(s) / log r  L donde H(s) = bits
Pudiendo expresar el cociente H(s) / log r, como la entropía en unidades r-arias
quedando:
Hr(s)  L (4.9.7)
O sea la (4.9.7) expresa que nunca podremos obtener un código cuya longitud
media sea menor que la Hr(s) (entropía en unidades r-arias).
Por otro lado, hemos puesto en relación dos magnitudes: la Hr(s) con otra, la
longitud media, que no depende de H(s).
4.11 FFFUUUEEENNNTTTEEESSS PPPAAARRRTTTIIICCCUUULLLAAARRREEESSS ... CCCOOODDDIIIFFFIIICCCAAACCCIIIÓÓÓNNN
Nuestro deseo no es solo ver hasta dónde se puede disminuir L sino también de
qué forma lograrlo. Entonces, veremos cuando la (4.9.7) es una igualdad.
El signo desigualdad se introdujo en dos puntos, primero en la (4.9.6) y luego en
la (4.9.6)bis cuando suprimimos el término II.
Entonces, la (4.9.6) es una igualdad para la condición P = Q i o sea:
i i
Si se cumple la (4.9.8) y además:
Entonces, de la (4.9.6)bis obtenemos:
H(s) = log L
r
Resumiendo, el código mínimo en longitud media, lo obtenemos si se cumplen
la (4.9.8) y la (4.9.9) o sea:
O de otra forma:
Un código instantáneo y una fuente de memoria nula L debe ser igual o mayor
que Hr(s). Además L será mínima sí y sólo sí pueden elegirse las l iguales a log (1/P);
i r i
esto se podrá lograr indudablemente si log (1/P) es es un número entero i.
r i
Esto significa que L = Hr(s) se logra si las probabilidades de los símbolos Pi son
de la forma (1/)i para cada palabra código de cada símbolo.
r

CCCooodddiiifffiiicccaaaccciiióóónnn – Unidad N°4
Comunicaciones  -
Ingeniería en Sistemas de Información

    Ejemplo:
|     |     | P           |     | S     |     |     |
| --- | --- | ----------- | --- | ----- | --- | --- |
|     |     | i           |     | i     |     |     |
|     |     | ½           |     | S 1   |     |     |
1/
|     |     |       |     | S   |     |     |
| --- | --- | ----- | --- | --- | --- | --- |
|     |     | 8     |     | 2   |     |     |
|     |     | 1/    |     | S   |     |     |
|     |     | 8     |     | 3   |     |     |
|     |     | 1/    |     | S   |     |     |
|     |     | 8     |     | 4   |     |     |
|     |     | 1/    |     | S   |     |     |
|     |     | 8     |     | 5   |     |     |

   Un código podría ser:
|     |     | S    |     | 0    |     |     |
| --- | --- | ---- | --- | ---- | --- | --- |
|     |     | 1    |     |      |     |     |
|     |     | S    |     | 101  |     |     |
|     |     | 2    |     |      |     |     |
|     |     | S    |     | 100  |     |     |
|     |     | 3    |     |      |     |     |
|     |     | S 4  |     | 111  |     |     |
|     |     |      |     |      |     |     |
|     |     | S    |     | 110  |     |     |
|     |     | 5    |     |      |     |     |

  Si calculamos la longitud promedio: L = ½  1 + 1/   ( 3 x 4) = 2 binit/símb. Que
8
comparándola con la entropía, debe ser igual.

| H(s) /log 2 = H |     | (s) = ½  log 2 + 4 x 1/ |     |  = ½ + 3/ |     | = 2 bit.  |
| --------------- | --- | ----------------------- | --- | --------- | --- | --------- |
|                 |     | r                       |     | 8         | 2   |           |

O sea, ya que el código es instantáneo, y de longitud media mínima implica que es un
código compacto.

Nota: indudablemente esta fuente tenía un esquema de probabilidades muy particular.

| 4.12   PPPRRRIIIMMMEEERRR    |     | TTTEEEOOORRREEEMMMAAA   DDDEEE    |     | SSSHHHAAANNNNNNOOONNN     |     |     |
| ---------------------------- | --- | --------------------------------- | --- | ------------------------- | --- | --- |
  En  el punto anterior vimos la solución al problema de códigos compactos si
log (1/P) es un número entero. Ahora plantearemos un problema más amplio o general,
r i
que es el del vector de probabilidades arbitrarias.
  Dado que log 1/P  no es un número entero, parece lógico tratar de elegir las l
|     |     | r   | i   |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- |
iguales al número entero inmediatamente superior.
Por lo tanto, hacemos que l cumpla:
i

|     |  1/P       l       log |     |     |  1/P + 1  |     |              |
| --- | ------------------------ | --- | --- | --------- | --- | ------------ |
|     | log r                    | i i |     | r i       |     |   (4.12.1)   |

  Primeramente veremos que eligiendo las l de forma tal que cumplan con la
i
(4.12.1), se pueda construir un código instantáneo, esto es, cumplen con la inecuación
de Kraft.
Aplicando antilogaritmo a la (4.12.1):

|     |     |     | 1/P      r li  |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- |
i
|     |     |     |                           | o bien  |     |           |
| --- | --- | --- | ------------------------- | ------- | --- | --------- |
|     |     |     | P i             r –li    |         |     | (4.12.2)  |

Comunicaciones -
CCCooodddiiifffiiicccaaaccciiióóónnn
– Unidad N°4
Ingeniería en Sistemas de Información
Sumando esta expresión, para todos los i:
relación esta que nos dice que este código cumple con la inecuación de Kraft lo
que implica que es instantáneo.
Multiplicando la (4.12.1) por Pi y haciendo la sumatoria para todo i, se obtiene:
Hr(s)  L < H (s) + 1 (4.12.3)
r
La (4.12.3) se cumple sí y sólo sí para codificar usamos el criterio enunciado en
la (4.12.1).
La (4.12.3) es válida para cualquier fuente de memoria nula, en particular, para
una extensión de orden n, de la fuente original.
H (sn)  L < H (sn) + 1 (4.12.4)
r n r
Donde Ln es la longitud media de las palabras código correspondientes a los
símbolos de la fuente extendida, es decir, si  es la longitud de la palabra
i
correspondiente al símbolo  y P() su probabilidad, L será:
i i n
La (4.12.4) puede escribirse:
n . H (s)  L < n . H (s) + 1
r n r
dividiendo esta por n:
H (s)  L / n < H (s) + 1/ (4.12.6)
r n r n
Donde Ln/ es el número medio de símbolos empleados en cada símbolo siempre
n
de S. No debe confundirse L con Ln/ ; si bien ambos se refieren al número medio de
n
símbolos del alfabeto código, empleados por símbolos de la fuente, Ln/ indica que con
n
objeto de alcanzar este valor medio de longitud; los símbolos Si de la fuente se han
codificado en grupos de n, en lugar de hacerlo independiente.
Observando la (4.12.6) vemos que es posible encontrar un valor de Ln/ tan
n
próximo a H(s) como queramos, sin más que agrandar el valor de la extensión, ya que
r
haciendo límite en la (4.12.6) se obtiene:
La ecuación (4.12.6) se conoce como el primer teorema de Shannon o teorema
de la codificación sin ruido.
La (4.12.7) muestra que el número medio de símbolos con que codificamos un
símbolo de la fuente, puede hacerse tan pequeño como lo deseáramos, pero no inferior a
la entropía en unidades r-arias.

Comunicaciones -
CCCooodddiiifffiiicccaaaccciiióóónnn
– Unidad N°4
Ingeniería en Sistemas de Información
El problema de aumentar el orden de la extensión es la complejidad de la
codificación empleada, dado que ahora tenemos qn símbolos que codificar.
4.13 MMMÉÉÉTTTOOODDDOOO DDDEEE HHHUUUFFFFFFMMMAAANNN PPPAAARRRAAA LLLAAA CCCOOONNNSSSTTTRRRUUUCCCCCCIIIÓÓÓNNN DDDEEE CCCÓÓÓDDDIIIGGGOOOSSS
CCCOOOMMMPPPAAACCCTTTOOOSSS
4.13.1 CCCÓÓÓDDDIIIGGGOOO CCCOOOMMMPPPAAACCCTTTOOO BBBIIINNNAAARRRIIIOOO
Veremos un método para crear un código compacto en el caso de un alfabeto
binario, para luego generalizar para un alfabeto r-ario.
Ambos procedimientos fueron desarrollados por huffman.
Consideremos una fuente S de símbolos S , S , ........., S y probabilidades
1 2 q
P ; P ; ..........; P . Supongamos ordenarlos de forma que: P  P  .........  P .
1 2 q 1 2 q
Si los dos últimos símbolos los fundimos en uno solo (sumando sus
probabilidades), se tiene una nueva fuente de q-1 símbolos. La denominaremos fuente
reducida de S. Los nuevos símbolos los ordenamos de igual forma que anteriormente, y
realizamos el agrupamiento de los dos últimos. Así sucesivamente hasta llegar a una
fuente de dos símbolos. Este es el primer paso.
El segundo paso consiste en asignarle un código compacto a la última fuente
reducida, que precisamente es 0 y 1. El paso siguiente es retroceder en el procedimiento
hasta que, habiendo partido de un código compacto, se obtenga en S un código
1
compacto.
Ejemplo
011

Comunicaciones -
CCCooodddiiifffiiicccaaaccciiióóónnn
– Unidad N°4
Ingeniería en Sistemas de Información

CCCooodddiiifffiiicccaaaccciiióóónnn – Unidad N°4
Comunicaciones  -
Ingeniería en Sistemas de Información

Al decir retroceder nos referimos a:
  Sea S el código compacto correspondiente a una de las fuentes reducidas, uno
j
de sus símbolos, S  , estará formado por dos símbolos de la fuente procedente S que
j-1
denominamos S 0  y S 1 ; todos los demás símbolos se identifican con uno solo de S .
j-1
  Según esto el código compacto (instantáneo) correspondiente a S se deduce del
j-1
S de acuerdo a la siguiente regla:
j
|     |     |     |     |     | Se asigna a cada símbolo de S |     |     |     |  (excepto S |     | y S )  la  |
| --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | ----------- | --- | ---------- |
|     |     |     |     |     |                               |     |     |     | j-1         |     | 0  1     |
palabra correspondiente al símbolo de S. Las palabras correspondiente a S y S se
|     |     |     |     |     |     | j   |     |     |     |     | 0  1  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- |
forman añadiendo un 0 y un 1 respectivamente, a la palabra asignada a S .


  Se pone en evidencia que en algunas ocasiones resulta innecesario continuar la
secuencia  de  reducciones  de  la  fuente  original  hasta  la  fuente  de  dos  símbolos.
Unicamente deberá reducirse hasta llegar hasta una reducción para la cual se pueda
encontrar fácilmente un código compacto. Por ejemplo, si el esquema de probabilidades
de los símbolos resulta (½)i. A partir de aquí se vuelve hacia atrás de forma vista.

  ¿Este código hasta aquí es compacto?, demostramos que si.

| Supongamos la reducción S.  |     |       |          | j                   |     |     |     |     |     |     |     |
| --------------------------- | --- | ----- | -------- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
|                             |     | L = P |  l       | + ............. + P |     |  l  |     |     |     |     |     |
|                             |     | j     | j1  j1   |                     |     |  jn |  jn |     |     |     |     |

Supongamos además que esta reducción está codificada de forma compacta con
C.  j
|     | La reducción anterior S |     |     |       | tendrá una L |     | .   |     |     |     |     |
| --- | ----------------------- | --- | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- |
|     |                         |     |     | j-1   |              |     | j-1 |     |     |     |     |

    L  = P( )  l( ) + ....................+ P( )  l( ) + P( )  l( )
|     |     | j-1 | j-1, 1 | j-1, 1 |     |     |     | j-1, n | j-1, n | j-1, n+1 | j-1, n+1 |
| --- | --- | --- | ------ | ------ | --- | --- | --- | ------ | ------ | -------- | -------- |

Donde:
|     | P(     | )   =   P( | )      |     |     |     |     |     |     |     |     |
| --- | ------ | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     | j-1, 1 |            | j,1    |     |     |     |     |     |     |     |     |
|     | P(     | )   =   l( | )      |     |     |     |     |     |     |     |     |
|     | j-1, 1 |            | j-1, 1 |     |     |     |     |     |     |     |     |

Además:
|     | l( j-1, n | )   =  l( | j-1, n+1 )   =  l( | j, n | ) + 1  |     |     |     |     |     |     |
| --- | --------- | --------- | ------------------ | ---- | ------ | --- | --- | --- | --- | --- | --- |
|     | P(        | )   = P(  | )   =   P(         |      | )      |     |     |     |     |     |     |
|     | j-1, n    |           | j-1, n+1           |      | j, n   |     |     |     |     |     |     |

Luego:
|                       | L j-1  = P | j1   l  j1          |  + .............. + {( l |                                           | j,1   |  +1)  ( P | (j-1, n)    | P  j-1, n     | +1)} =  |     |     |
| --------------------- | ---------- | ------------------- | ------------------------ | ----------------------------------------- | ----- | --------- | ----------- | ------------- | ------- | --- | --- |
|                   = P |            |   l                 |  + .............. + l    |                                           |  P    |  + P      |             | + P           |         |     |     |
|                       |            | j1  j1              |                          |                                           | jn jn |           | (j-1, n)    |  (j-1, n+1)   |         |     |     |
|                       |            |                   L |                          |                                           |       |           | P         P |               |         |     |     |
|                       |            |                     |                          | j                                         |       |           | 0          | 1            |         |     |     |

O sea:
|     | L j-1  = L | j    +     | P 0   +  P | 1   |     |     |     | (4.13.1.1)  |     |     |     |
| --- | ---------- | ---------- | ----------- | ---- | --- | --- | --- | ----------- | --- | --- | --- |

CCCooodddiiifffiiicccaaaccciiióóónnn – Unidad N°4
Comunicaciones  -
Ingeniería en Sistemas de Información

  Donde P y P son las probabilidades de los símbolos S y S : símbolos que
|     | 0  1  |     | 0  1 |     |
| --- | ------- | --- | ------ | --- |
provienen de haber desdoblado el S ; donde S es el símbolo menos probable de la
|     |     |    |     |     |
| --- | --- | ---- | --- | --- |
reducción compacta S.
j

|                               | DDDEEEMMMOOOSSSTTTRRRAAACCCIIIÓÓÓNNN    |                |                 |     |
| ----------------------------- | --------------------------------------- | -------------- | --------------- | --- |
|   Se desea demostrar que si C |                                         | es compacta, C | también lo es.  |     |
|                               |                                         | j              | j-1             |     |
  Se  hará  por  reducción  al  absurdo,  queremos  demostrar  que  si  L  la  menor
j
longitud media de un código instantáneo correspondiente a S; L (dado por la ecuación
j j-1
4.13.1.1) es también la longitud media mínima para S de longitud media L y sean
|     |     |     | j-1  | j-1  |
| --- | --- | --- | ---- | ---- |
X’ ,X’ ,X’ 0 ,X’ 1 , las palabras de dicho código de longitudes l’ , ........., l’ 0 , l’ 1 .
1 2 j-1
  Supongamos  los  subíndices  ordenados  según  el  orden  decrecientes  de  las
probabilidades de los símbolos respectivos, es decir
|     | l’ < .........  <  l |   <  l   |     |     |
| --- | -------------------- | -------- | --- | --- |
|     | 1                    | 0 1    |     |     |
Ahora construyamos C, código correspondiente a S, combinando X’  y X’  y
|     |     | j   | j   | 0 1 |
| --- | --- | --- | --- | ----- |
suprimiendo el último binit sin alterar los demás. El resultado es un código instantáneo
| para S; de longitud media L’; que debe cumplir.  j |     | j   |     |     |
| -------------------------------------------------- | --- | --- | --- | --- |

|     | L’   =   L’  +  P |   +  P    |     |     |
| --- | ----------------- | --------- | --- | --- |
j 0 1

Esta ecuación comparada con la (4.13.1.1) implica que existe un código de longitud
| media L’  <  L lo que es absurdo ya que se puso que el C era compacto.  j | j   |     | j   |     |
| ------------------------------------------------------------------------- | --- | --- | --- | --- |

|       4.13.2   CCCÓÓÓDDDIIIGGGOOO    | CCCOOOMMMPPPAAACCCTTTOOO      RRR | ---AAARRRIIIOOO  |     |     |
| ------------------------------------ | --------------------------------- | ---------------- | --- | --- |
  Por extensión, se puede ver que la obtención de un código compacto r-arios es
similar al binario. Salvo que los símbolos se agrupon de a “r”.
  De esta manera cada fuente reducida tendrá r-1 símbolos menos que la anterior.
¿Pero en la última reducción habrá r símbolos?
  Esta pregunta es afirmativa si se cumple que, la fuente original esta formada por
 símbolos donde  = r + (r -1) siendo  un número entero.
  Si esto no ocurre se deberá añadir símbolos “falsos”, en número suficiente como
para que se cumpla la (4.15.2.1). A los falsos símbolos se les asigna probabilidad nula,
de modo que pueden ser ignorados una vez que el código haya sido construido.

4.14   RRREEENNNDDDIIIMMMIIIEEENNNTTTOOO   YYY   RRREEEDDDUUUNNNDDDAAANNNCCCIIIAAA   DDDEEE   UUUNNN   CCCÓÓÓDDDIIIGGGOOO
Se define rendimiento de un código a:

|     | Como H(s)  <  L implica    1  |     |     |     |
| --- | ------------------------------ | --- | --- | --- |
r
  Así mismo puede definirse la redundancia de un código según la expresión:

  Es interesante graficar el n en función del n° de símbolos del código.
  Si el alfabeto código tiene r símbolos, y el alfabeto de la fuente tiene un esquema
de probabilidades (¼)xi; resulta:

Comunicaciones -
CCCooodddiiifffiiicccaaaccciiióóónnn
– Unidad N°4
Ingeniería en Sistemas de Información
4.15 CCCOOONNNFFFIIIAAABBBIIILLLIIIDDDAAADDD (((VVVSSS ... EEECCCOOONNNOOOMMMÍÍÍAAA )))
La información y codificación de una fuente, cuando se transmite la información
por un canal real, el ruido de este cambia la información que se desea transmitir.
O sea:
Se emite 001 se recepciona 011
Es imprescindible entonces, estudiar la forma de poder detectar u aún más
corregir ciertos tipos de errores introducidos en el canal.
Se define Ruido Unitario al cambio, en una palabra de un binit por su
complemento (en codificación binaria).
4.15.1 PPPAAARRRIIIDDDAAADDD
Este es un criterio de detección de error que consiste en agregar a la palabra
codificada un bimit (ip) más (redundante), de forma tal que éste tome el valor.
(((aaa))) ip = i + i + .................. + i (4.15.1.1)
1 2 n
si se adapta el criterio de paridad par y
(((bbb))) ip = i + i + .................. + i + 1 (4.15.1.2)
1 2 n
donde: i, con i = 1 ........n, son los binit que conforman la palabra código.
i
ip : binit de paridad (impar o par).
 : función “or exclusive”.
n : longitud de la palabra código.
Luego la palabra que se transmite será:
i , i , .............., i , ip
1 2 n
Al recepcionar se controla si ip cumple con la (4.15.1.1) si se utiliza paridad par
o con la (4.15.1.2) si se utiliza paridad impar.
Si en el camino se produjo algún error unitario se altera la paridad de la palabra,
siendo posible detectarlo en el destino.
Es evidente que también se detectan los cambios de orden K toda vez que K sea
impar.

Comunicaciones -
CCCooodddiiifffiiicccaaaccciiióóónnn
– Unidad N°4
Ingeniería en Sistemas de Información
Con este tipo de control no solo se puede llegar a detectar sino también a
corregir de la siguiente forma:
Antes de transmitir se forman grupos de palabras, de forma tal que conformando
una matriz de m x n; se completan las filas y las columnas con el binit de paridad de la
fila y de la columna obteniéndose una nueva matriz (m +1) x (n +1).
De esta forma, si al recepcionar esta matriz; el canal ha introducido un ruido
unitario y se alteró, por ejemplo i , al controlar paridad, el recepcionista verá que no
22
cumplen la regla i r i , quedando unívocamente identificado el binit alterado.
2f 2c
Si el alterado es una de los binit de paridad, es detectado por el incumplimiento
de la paridad i .
pt
¿ Dónde se pone en evidencia la redundancia, como factor de absorción del
ruido?
Pensemos: tenemos 3 símbolos en nuestro alfabeto código. Con esto podemos
codificar 23 símbolos de una fuente, o sea 8 símbolos. Si ahora agregamos un binit de
paridad seguiremos codificando 23 símbolos (ahora con protección).
Pero con 4 símbolos en el alfabeto código, se pueden codificar 24 símbolos
fuente o sea 16.
De esto se deduce que no se utilizan:
24 - 23 = 3 configuraciones
Estas son precisamente las configuraciones que nos absorben el ruido.
4.15.2 PPPOOORRR MMMAAAYYYOOORRRÍÍÍAAA
Este método consiste en codificar de forma tal que una palabra haya mayor
“peso” de “1s” o de “0s” de forma tal que al recepcionar se controla so se violó esa
regla.
Ejemplo:
Codificaremos con una longitud constante, l = 5 y peso 3 de unos.
Existen un número de palabras que cumplen con este peso igual a:
Nótese que con cinco símbolos en un alfabeto
código, se pueden codificar (sin protección) 25 = 32
símbolos fuentes. Este método detecta todos los errores
unitarios.
En los errores de orden mayor no se puede
asegurar su eficacia.

Comunicaciones -
CCCooodddiiifffiiicccaaaccciiióóónnn
– Unidad N°4
Ingeniería en Sistemas de Información
4.15.3 DDDEEE IIIGGGUUUAAALLL PPPEEESSSOOO
Es muy similar al de mayoría, salvo que ahora se codifica de forma tal de que el
número de “1s” sea igual al número de “0s”.
Indudablemente, las palabras códigos resultarán de longitud l, con l par.
4.16 RRREEEGGGLLLAAA DDDEEE DDDEEECCCIIISSSIIIÓÓÓNNN
Hemos visto hasta ahora, que algunos criterios de protección detectan errores
pero no los corrigen.
En algunas aplicaciones, esto se soluciona pidiendo (en el caso de haber
detectado un error) que se retransmita la información.
En otras aplicaciones, esto no es posible. En estas aplicaciones entonces, se debe
buscar otra solución.
Esta puede ser adoptar una Regla de Decisión.
Consiste en recibida una palabra que se sabe con equivocación: modificarla
según una regla, de manera tal que adopte la forma de una palabra sin equivocación.
Es indudable que esto trae asociado una improbabilidad de error (o acierto).
De ahí que esta regla de decisión debe ser adoptada de forma tal que proporcione
una probabilidad de error, lo más baja posible.
Ejemplo:
Símbolo Fuente Palabra Código
S 000
1
S 111
2
Si sabemos que el canal tiene una probabilidad relativamente elevado debe
provocar cambios unitarios y en mucho menor grado, errores de orden superior.
La regla de decisión es evidente:
Si se recibe: 001 se decodifica como recibido 000
011 se decodifica como recibido 111
...............................................................
...............................................................
4.17 HHHAAAMMMMMMIIINNNGGG (((PPPAAARRRIIIDDDAAADDD PPPOOORRR ZZZOOONNNAAASSS )))
Este es un método que consiste en controlar la paridad de zonas. Estas zonas son
forradas por conjuntos de binits.

CCCooodddiiifffiiicccaaaccciiióóónnn – Unidad N°4
Comunicaciones  -
Ingeniería en Sistemas de Información

  Veamos en un diagrama de Venn:

Acá los binits que transportan información (y por lo tanto juegan libremente) son
| i , i ,  y  i | .   |     |     |     |
| ------------- | --- | --- | --- | --- |
| 0 1           | 3   |     |     |     |
  Pero se observa que las zonas delimitadas, poseen además otros binits, C , C  y
1 2
C  que son los binits de control.
3
  Se los denomina binits de control, pues estos se acomodan de forma tal que,
conjuntamente con los binits de información de su zona, conserven una determinada
paridad.
|     | C   =  i     i |     i   |     |     |
| --- | --------------- | -------- | --- | --- |
|     | 1 0             | 1 2      |     |     |
|     | C   =  i     i |     i   |     |     |
|     | 2 0             | 2 3      |     |     |
|     | C   =  i     i |     i   |     |     |
|     | 3 0             | 1 3      |     |     |
  Recordar que, C ,C , C , i , i , i , i  pueden adoptar los valores 0 ó 1.
|     |     | 1 2 3 | 0 1 2 3 |     |
| --- | --- | ----- | ------- | --- |
Luego:
|     | C   controla a  i | , i , i y  a C |     |   (4.17.4)  |
| --- | ----------------- | -------------- | --- | ----------- |
|     | 1                 | 0 1 2          | 1   |             |
|     | C   controla a  i | , i , i y  a C |     |   (4.17.5)  |
|     | 2                 | 0 2 3          | 2   |             |
|     | C   controla a  i | , i , i y  a C |     |   (4.17.6)  |
|     | 3                 | 0 1 3          | 3   |             |

La palabra a ser transmitida ahora tendrá la forma:
|     | i    i    i    i    C |    C    C   |     | (4.17.7)  |
| --- | --------------------- | ----------- | --- | --------- |
|     | 0 1 2 3               | 1 2 3       |     |           |
Al recepcionar se controla la paridad de las zonas.
  Por ejemplo: Supongamos que se alteró el valor de i .
2
  Esto trae aparejado que las ecuaciones que no se cumplen son (4.17.1) y la
(4.17.2), o en otras palabras  se modifico la paridad de las zonas  I  y  II  quedando
| unívocamente determinado el binit cambiado: i |     |     |     | .   |
| --------------------------------------------- | --- | --- | --- | --- |
2
  Si el error proviene de un cambio en un binits de control; esto se pone en
evidencia pues la zona modificada es solo una, la correspondiente a dicho binit de
control.
    PPPRRREEEGGGUUUNNNTTTAAA :::      si se realiza un código con m dígitos de información. ¿Cuántos
dígitos de control se deben agregar?
  Se deben agregar n dígitos de control.
  Con n dígitos de control se puede tener 2n configuraciones distintas.
  Cada una de estas configuraciones, indicará error en un dígito, existiendo m + n
dígitos. Pero además deberá existir una configuración que indique la no existencia de
error. Luego se deberá cumplir con la relación:

Comunicaciones -
CCCooodddiiifffiiicccaaaccciiióóónnn
– Unidad N°4
Ingeniería en Sistemas de Información
2n  m + n + 1 (4.17.8)
En nuestro ejemplo, m = 4, luego m debe valer 3 para que:
23  4 + 3 + 1 se verifique
Hagamos una parte del problema
Notar que las configuraciones de los dígitos de control se repiten pero existen
ocho configuraciones (que no son las mostradas en *) que me indican la:
(((aaa))) equivocación en dígitos de información 4
equivocación en dígitos de control. 3
(((bbb))) La configuración que dice todo O.K. 1
Total 8
Vimos que, chequeando las zonas cuyas paridades se han alterado según sea
utilizando el diagrama de Venn, o las tablas (16.5.4) (16.5.5), (16.5.6) se identifica el
dígito que proporciona el problema. Este es el método cuando la palabra protegida se
envía de la forma mostrada en (16.5.7).
Pero existe otro método que, indica como elegir las zonas; y como intercalar,
entre los dígitos de información, los dígitos de control; de forma tal que (enumerando la
posición de los dígitos en la palabra transmitida), si se produce un error, la
configuración que adoptan los dígitos del control, debido a ese error, me indica (en
decimal) el n° del dígito que fue alterado. Falta aclarar que la configuración de los
dígitos de control se obtiene así.
Si la Cj fue alterada, el dígito de control correspondiente se coloca en 1. De lo
contrario en cero. O sea zona C Alterada C = 1
j j
zona C no Alterada C = 0
j j

Comunicaciones -
CCCooodddiiifffiiicccaaaccciiióóónnn
– Unidad N°4
Ingeniería en Sistemas de Información
Veamos ahora como numeramos e intercalamos los dígitos de control en la
palabra codificada.
Esta es la palabra y se han numerado los dígitos. Los dígitos de control se
intercalan en las posiciones 2n con n  IR (dígitos rayados).
Los dígitos que quedan libres, se usan para transportar información.
Falta ahora ver como elegimos las zonas.
Ya que la elección de esta depende la identificación del dígito alterado, esta
elección no puede ser arbitraria.
Ejemplo:
3 binits de control
4 binits de información
En la palabra las posiciones serán las siguientes:
Recordemos ahora lo que deseamos obtener:
(((aaa))) Se coloca un “uno” en el dígito de
control si al recepcionar, se detecta que en esa zona no se conserva la paridad
pre-establecida.
(((bbb))) Colocando luego los dígitos de
control en orden; el n° formado en decimal, es el número del dígito alterado.
Ejemplo:
Zona I alterada C = 1
1
Zona II alterada C = 1
2
Zona III correcta C = 0
3
C C C
1 3 2
0 0 1 3  alterado el 3° dígito

Comunicaciones -
CCCooodddiiifffiiicccaaaccciiióóónnn
– Unidad N°4
Ingeniería en Sistemas de Información
Diagrama propuesto:
7
Luego:
C { 1, 3, 5, 7 }
1
C { 2, 3, 6, 7 } = (16.5.9)
2
C { 4, 5, 6, 7 }
3
Si lo planteamos sobre un diagrama de Karnauch, este debe tener 8 cuadraditos.
Cada cuadrito, representa, en decimal, el n° del dígito. El 000, lo reservamos
para indicar que no hubo ningún error; pues esto, implica C = 0, C = 0, C = 0.
1 2 3
La reglas prácticas para determinar las zonas que controlan C , C , C es:
1 2 3
(((aaa))) Se ubican los dígitos de control en sus respectivos lugares.
(((bbb))) Se observa que a cada dígito de control, por estar en las
posiciones 2n; le corresponde un n° en binario con un solo “1”.
(((ccc))) Cada dígito de control, controla aquellos dígitos que en binario,
posean un “1” en el binit en el cual dicho dígito de control lo posea.
Ejemplo:
C le corresponde 0 1 0
2
Luego C controla aquellos dígitos que en binario posean un “1” en el binit
2
señalado con una | o sea:
0 1 1 3er dígito ( i )
0
1 1 1 7° dígito ( i )
3

CCCooodddiiifffiiicccaaaccciiióóónnn – Unidad N°4
Comunicaciones  -
Ingeniería en Sistemas de Información

| 0 1 0    | 2do      dígito  ( es C | )   |     |
| -------- | ----------------------- | --- | --- |
2
| 0 1 1    | 3er      dígito  (i | )   |     |
| -------- | ------------------- | --- | --- |
0
| 1 1 0    | 6°       dígito  (i | )   |     |
| -------- | ------------------- | --- | --- |
2

Supongamos querer transmitir la palabra:
|     |     |     | 1 1 0 1  |
| --- | --- | --- | -------- |

La ubicación será:
1   0   1   0   1   0   1

Ahora deben colocar, con el valor adecuado los dígitos de control.
  De acuerdo a   (16.5.9)

| C  = 1  1  1  = 1  |     |     | (**)  |
| -------------------- | --- | --- | ----- |
1
| C  = 1  0  1  = 0  |     |     |     |
| -------------------- | --- | --- | --- |
2
| C  = 1  0  1  = 0  |     |     |     |
| -------------------- | --- | --- | --- |
3

Luego la palabra que se transmite es:
1   0   1   0   1   0   1

Supongamos que al recepcionar se obtiene:
1   0   1   0   1   1   1
  Se  controla  la  paridad  de  la  zonas  nuevamente  realizando  el  cálculo  (**)
Observando que:

|     | zona I  | no alterada  |   C  = 0  |
| --- | ------- | ------------ | --------- |
1
|     | zona II   | alterada  |   C 2  = 1  |
| --- | --------- | --------- | ----------- |
|     | zona III  | alterada  |   C  = 1    |
3

|     | 1   1   0  | 6    | 6° dígito alterado  |
| --- | ---------- | ---- | ------------------- |

  En este ejemplo,  analizándolo en detalle se ve que se puede desechar cualquier
dígito cumpliéndose siempre que la probabilidad de error doble no detectado es siempre
igual.