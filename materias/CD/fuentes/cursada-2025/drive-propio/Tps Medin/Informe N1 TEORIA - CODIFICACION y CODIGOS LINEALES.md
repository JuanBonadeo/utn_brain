UNIVERSIDAD TECNOLÓGICA NACIONAL![](data:image/png;base64...)

Facultad Regional Rosario

Ingeniería en Sistemas de Información

**Asignatura:** Comunicación de datos

**Profesores:** Germán Bernardo Baró y Cristian Medin

**Comisión:** 303

**Integrantes:**

* Juan Pedro Casañas (Legajo: 50373)
* Maria Sofia Ochoa (Legajo: 50452)
* Martin Quagliardi (Legajo: 51657)
* Mateo Regodesebes (Legajo: 51079)

**Trabajo Práctico:**  Codificación y Códigos lineales

**Año:** 2024

Índice

[**Introducción 3**](#_a61h1maopi1g)

[**Codificación 6**](#_heuy52ct8v9c)

[Propiedades de la codificación 6](#_lqs1f88hb5ll)

[Inecuación de Kraft 9](#_idx1wfrod51n)

[¿Cuál es la interpretación que nos da? 10](#_ur7fvfw6pulq)

[Ecuación de Mc. Millan 12](#_7lj2mw6qqgdl)

[Longitud media de un código 12](#_n6hy9em74fud)

[Conceptos previos 12](#_xbuthhogq77m)

[Desarrollo 13](#_vpbfd2r3h964)

[Definición 14](#_bqihuwsog31u)

[Códigos compactos 15](#_k4vhu8hrlr31)

[Definición 15](#_cyjta5rn2px4)

[Cota inferior de la longitud media 17](#_szi6pcwsrw1r)

[Teorema 17](#_eyxyu0dkccdl)

[Fuentes particulares de codificación 17](#_fkt3fbzfio22)

[Primer Teorema de Shannon 19](#_mtdi8edtrlhr)

[Codificación de Shannon Fano 21](#_zqpa3y23yqj)

[Método de Huffman para la construcción de códigos compactos 22](#_1yyzvl7b399d)

[Construcción de código compacto binario 22](#_awhx7ez4l111)

[Código compacto r-ario 25](#_k6lnydrpiua9)

[Rendimiento y redundancia de un código 25](#_uy0r0r9rag1i)

[Confiabilidad VS Economía 26](#_qfaw1u9jtwa9)

[Paridad 26](#_ey8gdfunehwd)

[¿ Dónde se pone en evidencia la redundancia, como factor de absorción del ruido? 29](#_truj64uhb98x)

[Por mayoría 30](#_11l9bthqd4gr)

[De igual peso 30](#_8ebvzaruruuh)

[Repetición 31](#_nrgfg6sctpbz)

[Regla de decisión 32](#_ubleav4493m7)

[Hamming (Paridad por Zonas) 33](#_l5svyg52k95x)

[Distancia Hamming 34](#_t72jtluqlj3u)

[Hamming(7,4) 35](#_817xg7e70d8p)

[**Códigos Lineales 37**](#_gm9563j9v7mi)

[Códigos de Bloques 37](#_tqqgwyawztjr)

[Códigos de Grupo 39](#_cfuey3r55d6g)

[Espacio nulo 40](#_3nrj80epy66k)

[Síndrome 40](#_h778h28ov7xm)

[**Conclusiones 42**](#_38wvun4soq6v)

[**Bibliografía 43**](#_nk1ei1r7py0m)

[**Anexo: Autoevaluación con Preguntas y Respuestas 44**](#_2cp76r5k8459)

# Introducción

Un sistema de comunicación general está compuesto por varias partes esenciales.

* Una **fuente** que genera el mensaje destinado a ser recibido por el destinatario.
* Un **transmiso**r, encargado de convertir el mensaje generado por la fuente en una señal lista para ser transmitida. En casos donde se codifica la información, el proceso de codificación también es llevado a cabo por el transmisor.
* A continuación, encontramos el **canal**, que actúa como el medio a través del cual la señal es transmitida desde el transmisor hasta el receptor. Este canal puede ser diverso, desde un cable hasta una fibra óptica o incluso una señal inalámbrica.
* Después, el **receptor** entra en juego, encargado de reconstruir el mensaje original a partir de la señal recibida.
* Por último, está el **destinatario**, quien recibe y finaliza el proceso de comunicación.

**Figura 1**

*Esquema básico de transmisión de datos*

![](data:image/png;base64...)

*Nota. Esquema básico de transmisión de datos [Diagrama], por Holik, Federico. 2016. "Teoría de la información de Claude E. Shannon". En Diccionario Interdisciplinar Austral, editado por Claudia E. Vanney, Ignacio Silva y Juan F. Franck.*

La fuente S es un sistema que contiene un conjunto de estados diferentes llamados usualmente **símbolos**. Cada uno de estos símbolos tiene una probabilidad de presentarse en la entrada. A su vez, cada uno de estos símbolos es sometido a una **codificación** para poder circular por el canal y alcanzar al receptor. Un mismo conjunto de símbolos puede ser codificado a través de muchas codificaciones, pero no todas tienen los mismos beneficios o desventajas.

En este sentido, el presente trabajo tiene como objetivo explicar en primer lugar qué es la codificación en cuanto a conceptos como los códigos de bloque, códigos no singulares y códigos unívocamente decodificables a través del proceso de transformar los datos de entrada de una manera específica para que cumpla con ciertas propiedades deseables para la transmisión y la decodificación a posteriori.

En otros términos, la codificación en estos contextos específicos implica aplicar técnicas y algoritmos para transformar los datos de entrada en una forma que cumpla con las propiedades requeridas para una transmisión y decodificación confiables, como la detección y corrección de errores, la reversibilidad y la univocidad en la decodificación.

Entonces la definición formal de codificación es: “*Si denominamos S = (s1; s2; ..........; sq) al conjunto de símbolos de un alfabeto dado; queda definida una codificación al poner en correspondencia todas las secuencias posibles de símbolos de S con secuencia de símbolos de algún otro alfabeto Z = (z1; z2; ...........; zr). Entonces “S” recibe el nombre de alfabeto fuente y “Z” alfabeto código.*”.

No obstante la definición formal resulta más comprensible si se analiza en partes:

* Símbolos de un alfabeto dado (S): Estos son los elementos individuales que forman parte del conjunto de datos que se desea transmitir. Por ejemplo, en el contexto del lenguaje natural, los símbolos podrían ser letras, números, caracteres especiales, etc.
* Alfabeto Fuente (S): Se refiere al conjunto de símbolos disponibles para la codificación. Es el conjunto desde el cual se extraen las secuencias de símbolos que se van a codificar.
* Alfabeto Código (Z): Es el conjunto de símbolos utilizados para representar las secuencias de símbolos del alfabeto fuente mediante codificación. En la mayoría de los casos, el alfabeto código consiste en un conjunto de símbolos binarios (bits).

En definitiva, habiendo visto las diversas definiciones podemos concluir que la codificación es el proceso de asignar secuencias de símbolos del alfabeto fuente (S) a secuencias de símbolos de algún otro alfabeto (Z) donde Z es generalmente un conjunto de símbolos binarios (0 y 1) cuya utilidad es facilitar la transmisión y el almacenamiento de la información.

Desarrollo

# Codificación

## Propiedades de la codificación

Los códigos poseen ciertas propiedades suplementarias:

* Código Bloque

Es aquel que asigna a cada uno de los símbolos del código fuente S una secuencia fija de símbolos del alfabeto código Z. Estas secuencias fijas (secuencias Zj) reciben el nombre de palabras código.

En la codificación bloque la fuente de información como por ejemplo una secuencia binaria (“0” o “1”) es segmentada en bloques de longitud fija de largo *k* y se codifica en bloques de n bits de código (*n<k*)

| Ejemplos de código bloque | |
| --- | --- |
| Mensajes (S) | Palabras código (Z) |
| (0000) | (0000000) |
| (1000) | (1101000) |
| (0100) | (0110100) |
| … | … |

* Código no-singular

Se denomina **código no singular** a aquel bloque de código en el cual a cada símbolo codificado le corresponde una única codificación.

| Ejemplos de código no-singular | |
| --- | --- |
| Mensajes (S) | Palabras código (Z) |
| S1 | 0 |
| S2 | 11 |
| S3 | 00 |
| S4 | 01 |

* Códigos unívocamente decodificables

| Para poder definir esta propiedad, se necesita una nueva definición. **La extensión de orden 𝑛** de un bloque de código, que hace corresponder los símbolos con las palabras de código , puede ser vista como la concatenación de **𝑛** instancias de dicho bloque de código. En otras palabras, **la extensión de orden 𝑛** es el bloque de código que hace corresponder las secuencias de símbolos de la fuente (, ,......., ) con las secuencias de las palabras de código (, , ......, ).  Por ejemplo, la extensión de orden 2 del bloque de código no singular del ejemplo anterior se vería como la siguiente tabla:   | Símbolos de la fuente | Código | Símbolos de la fuente | Código | | --- | --- | --- | --- | | s1s1 | 00 | s3s1 | 000 | | s1s2 | 011 | s3s2 | 0011 | | s1s3 | 000 | s3s3 | 0000 | | s1s4 | 001 | s3s4 | 0001 | | s2s1 | 110 | s4s1 | 010 | | s2s2 | 1111 | s4s2 | 0111 | | s2s3 | 1100 | s4s3 | 0100 | | s2s4 | 1101 | s4s4 | 0101 | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Cabe destacar que se puede decir que un código es **unívocamente decodificable** sí y solo sí su extensión de orden n es no singular para cualquier valor finito de n. Es decir que un código es unívocamente decodificable si a cualquier secuencia de palabras código, le corresponde una y sólo una secuencia de símbolos de la fuente.

En este sentido, el ejemplo dado para código de bloque no-singular no cumple esta condición pues si recepcionamos un código ‘000’ no sabremos si le corresponde a la secuencia de símbolos s1s3 o s3s1.

Entonces consideremos una codificación cuyas palabras código son de igual longitud. En este caso, indudablemente el código es unívoco (siempre que sea no singular el original).

Otro caso son los llamados códigos “coma”. Este nombre se debe a que el comienzo o el fin de cada palabra está señalizada por un cero o por un uno, de manera de identificarlas.

| Ejemplos de código coma | | |
| --- | --- | --- |
| Mensajes (S) | Palabras código A (Z1) | Palabras código B (Z2) |
| S1 | 0 | 1 |
| S2 | 01 | 01 |
| S3 | 011 | 001 |
| S4 | 0111 | 0001 |

* Código instantáneo

Un código unívocamente decodificable se denomina **instantáneo** cuando es posible decodificar las palabras de una secuencia sin precisar el conocimiento de los símbolos que las suceden.

Retomando el ejemplo anterior, donde los códigos A y B eran unívocos: si estamos recepcionando palabras según el código A no seríamos capaces de decodificarlas instantáneamente según las vamos recibiendo. Por ejemplo, si recibimos la palabra 01, no podemos decir que corresponde a S2 hasta que hayamos recibido el símbolo siguiente. Si el próximo es un 0 (cero) entonces si decimos que correspondía a S2, si es un 1 (uno) debemos esperar el próximo, etc. Si en cambio utilizamos el código B, podemos decodificar las palabras instantáneamente.

La condición específica a la que se hace referencia puede ser expresada a través del término “prefijo”:

Sea Zi = zi1; zi2; .........; zim una palabra de código. Se denomina **prefijo** de esta palabra a la secuencia zi1; zi2; .........; zij con . A partir de esto se puede enunciar: “La condición necesaria y suficiente para que un código sea instantáneo es que ninguna palabra del código coincida con el prefijo de otra”.

En el siguiente gráfico se muestra un resumen de las distintas clases de códigos tratadas anteriormente, hasta llegar a los códigos instantáneos y no instantáneos.

**Figura 2**

*Diagrama de los tipos de código*

![](data:image/png;base64...)

*Nota. Esquema de códigos [Diagrama], por Sanromán, G. (s. f.). “Estrategias de decodificación” [Universidad Nacional de La Plata].*

## Inecuación de Kraft

En la teoría de códigos ''la inecuación de Kraft'' esgrime las condiciones suficientes para la existencia de un código prefijo y las condiciones necesarias para la existencia de un código unívocamente decodificable para un grupo dado de longitudes de palabra.

La condición necesaria y suficiente para la existencia de un código instantáneo de longitudes L1, L2, …, Lq es

Donde:

* es la cantidad de mensajes de la fuente
* es el número de símbolos diferentes que constituyen el alfabeto base del código.
  + En el caso de alfabeto binario, la inecuación de Kraft se transforma en:
* son las longitudes de las palabras de código instantáneo.

Hay que tener en cuenta que:

* Es condición necesaria para que un código sea uno de los códigos instantáneos.
* Es condición suficiente para que exista algún código instantáneo con la secuencia de longitudes: L1, L2, …, Lq

| *Nota*: El teorema no dice que cualquier código cuyas longitudes cumplan la condición es un código instantáneo. |
| --- |

### ¿Cuál es la interpretación que nos da?

En base a dos únicos resultados posibles:

* Si el resultado es menor o igual que uno quiere decir es posible realizar un código instantáneo con las longitudes que se nos plantea.
* Si el resultado es mayor que uno nos quiere decir que no se puede realizar un código instantáneo con las longitudes dadas

**Ejemplos:**

| Símbolo de la fuente | Código A | Código B | Código C |
| --- | --- | --- | --- |
| S1 | 00 | 0 | 0 |
| S2 | 01 | 100 | 10 |
| S3 | 10 | 110 | 110 |
| S4 | 11 | 111 | 11 |

Para los códigos de la tabla anterior determinaremos si las longitudes de una secuencia dada pueden constituir las longitudes de las palabras de un código instantáneo

*Código A:*

Por lo tanto, las longitudes de las palabras de A son aceptables para proceder a realizar un código instantáneo.

*Código B:*

Por lo tanto, las longitudes de las palabras de B pueden constituir un código instantáneo.

*Código C:*

Por lo tanto, las longitudes de las palabras de C **NO** pueden constituir un código instantáneo.

## Ecuación de Mc. Millan

Posee una fuerte relación con la Inecuación de Kraft puesto que se utiliza la misma ecuación. La diferencia radica en que Kraft la definió para códigos prefijo, mientras que McMillan para códigos unívocamente decodificables.

La ecuación de MacMillan plantea que:

“*La condición suficiente para que exista, al menos un código unívoco, es que las longitudes li verifiquen la expresión:*

”

es decir, si las longitudes l1; l2; ...........; lq satisfacen la relación pueden construirse con ellas un código unívoco. La condición necesaria fue demostrada por Mc. Millan.

## Longitud media de un código

Previo a entender la definición de longitud media de un código debemos entender los conceptos de frecuencia relativa y muestra significativa en términos de probabilidades.

### Conceptos previos

* *Frecuencia relativa.* Se entiende por frecuencia relativa de un evento particular a la suma de las veces que este evento aparece en la muestra dividido por la cantidad total de eventos que componen la muestra.
* *Muestra significativa.* En términos de comunicación, hace referencia a recopilar los símbolos que una fuente entrega en un cierto periodo determinado con anterioridad (puede que en vez de tener en cuenta un periodo se detenga la colección de la muestra al alcanzar una cantidad de símbolos entregados). Es aquella en la que se puede tomar la frecuencia relativa como probabilidad.

| *Ejemplo:*  frecuencia relativa de la |
| --- |

### Desarrollo

Ahora, codificamos a los eventos como:

* posee una palabra código de largo
* posee una palabra código de largo
* posee una palabra código de largo

Por ende la longitud de la muestra podrá ser expresada como:

Donde es el número de veces que aparece el evento en la muestra.

Luego, la longitud promedio puede ser expresada como:

donde:

* tamaño total de la muestra o cantidad de símbolos en la muestra
* frecuencia relativa del evento i

Si la muestra es representativa, la frecuencia relativa coincide con la probabilidad del suceso a.

Por ende podemos reescribir la ecuación anterior como:

### Definición

Dado un código bloque que asocia los símbolos de una fuente S1; S2; .......; Sn con las palabras Z1; Z2; .........; ZN y las probabilidades de los símbolos son P1; P2; .....; Pn. La **longitud media** del código L se define como:

| *Ejemplo:*  Si suponemos un código:   |  |  | | --- | --- | |  |  | |  |  | |  |  | |  |  |   Un código podría ser:   |  | 0 | | --- | --- | |  | 10 | |  | 110 | |  | 111 |   Tenemos entonces que las longitudes son:   * Longitud de * Longitud de * Longitud de * Longitud de   Entonces, aplicando la fórmula obtenemos la longitud media:  Y reemplazando con los valores: |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Códigos compactos

### Definición

Dada la fuente S diremos que un código instantáneo aplicado a S es **compacto** (respecto a S) si su longitud media es **igual o menor** que la longitud media de todos los códigos instantáneos que puedan aplicarse a la misma fuente y al mismo alfabeto.

Al ser códigos de longitud variable que minimizan la longitud promedio (o entropía) se denominan de *alto rendimiento*. Además son instantáneos, por lo que ninguna palabra de código puede aparecer como prefijo de una con mayor longitud.

En esencia, la codificación consiste en asignar las palabras de menor cantidad de símbolos a aquel mensaje de mayor probabilidad, y así sucesivamente. Quedándonos una distribución como:

Gráficamente puede apreciarse de la siguiente manera:

![](data:image/png;base64...)

Si la fuente tiene un esquema equiprobable de símbolos, las longitudes de las palabras códigos se independizan del esquema de probabilidades. Dado que las Pi ≥ 0 y las li ≥ 0 resulta que L ≥ 0.

Es decir, si cada símbolo de la fuente tiene igual probabilidad de ser enviado (Es decir, en un mensaje de una fuente que contiene S1, S2, S3, S4 todos esos símbolos tienen un 25% de chances de aparecer) entonces las longitudes de las palabras códigos dejan de depender de las probabilidades. Esto se debe a que, al ser probabilidades iguales ya no podemos optimizar la codificación basado en qué símbolo vaya a aparecer más veces, por ende la longitud de la codificación dejaría de depender de las probabilidades.

Como las probabilidades de que aparezcan los símbolos son equitativas (ningún símbolo tiene 0% de probabilidad de aparecer) y además los símbolos tienen una longitud mayor a 0 entonces en cualquier mensaje completo de la fuente necesariamente vamos a tener una longitud total L mayor a 0.

Sin embargo, estos códigos presentan el inconveniente de que la distribución de la fuente puede ser desconocida cuando se diseña el código.

## Cota inferior de la longitud media

En base a lo que hemos visto, podemos comprender que a medida que disminuye la longitud media de un código, mayor rendimiento tiene a la hora de usarse en una codificación. Como consecuencia de estos hallazgos inevitablemente surge la siguiente duda: Dado un código X ¿Cuál sería la menor longitud media posible para dicho código? Para esclarecer dicha incógnita contamos con el siguiente teorema:

### Teorema

La longitud media de un código es mayor o igual que la entropía de la fuente dividida por el del número de símbolos del alfabeto código. Es decir:

**donde H(s) = bits**

Si exigimos que el código sea instantáneo por Kraft, entonces

Pudiendo expresar el cociente, como la **entropía en unidades r-arias** quedando:

Esta ecuación expresa que nunca podremos obtener un código cuya longitud media sea menor que la Hr(s) (entropía en unidades r-arias).

Por otro lado, hemos puesto en relación dos magnitudes: la Hr(s) con la longitud media, que no depende de H(s).

## Fuentes particulares de codificación

Luego de asimilar la idea de la cota inferior de la longitud media, nos interesa averiguar de qué manera es posible lograr llegar a esa longitud media mínima.

A partir de la demostración del teorema anterior, podemos también deducir que el código de longitud media mínima se obtiene si se cumple:

No obstante la demostración del teorema anterior también nos provee una fórmula más sencilla que sigue verificando la igualdad anterior

De otra forma:

Un código instantáneo y una fuente de memoria nula L debe ser igual o mayor que Hr(s). Además L será mínima sí y sólo sí pueden elegirse las iguales a ; esto se podrá lograr indudablemente si es un número entero i.

Esto significa que L = Hr(s) se logra si las probabilidades de los símbolos Pi son de la forma para cada palabra código de cada símbolo.

| *Ejemplo:*   |  |  | | --- | --- | |  |  | |  |  | |  |  | |  |  | |  |  |   Un código que cumpla con estas condiciones podría ser:   |  | 0 | | --- | --- | |  | 10 | |  | 100 | |  | 111 | |  | 110 |   Si ahora calculamos la longitud promedio, obtenemos que:  La comparamos con el cálculo de la entropía:  O sea, ya que el código es instantáneo, y de longitud media mínima implica que es un código compacto. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

###

## Primer Teorema de Shannon

El primer teorema de Shannon proporciona un marco teórico que define cómo de eficiente puede ser la transmisión de datos a través de un canal sin ruido. Este teorema establece que la entropía de un alfabeto de símbolos específica dentro de un bit cuántos bits en promedio deben usarse para enviar el alfabeto.

De esta manera, el primer teorema de Shannon establece una cota inferior y superior de la longitud mínima posible de los bits de información como función de la entropía.

Sin ahondar en detalle de desarrollo de ecuaciones, el teorema concluye demostrando que:

Se conoce a esta ecuación como el primer teorema de Shannon o teorema de la codificación sin ruido. De esta forma, la entropía del alfabeto específica dentro de un bit cuántos bits en promedio deben usarse para enviar el alfabeto. Cuanto menor sea la entropía de un alfabeto, menos bits se requieren para la transmisión digital de archivos expresados en ese alfabeto.

| *Ejemplo:*  Un alfabeto de cuatro símbolos tiene las siguientes probabilidades.   |  |  | | --- | --- | |  |  | |  |  | |  |  | |  |  |   y una entropía de 1.75 bits. El código más simple para probar se conoce como el **código binario simple**: convierte el índice del símbolo en un número binario y usa el mismo número de bits para cada símbolo incluyendo ceros a la cabeza cuando sea necesario.   |  | 00 | | --- | --- | |  | 01 | |  | 10 | |  | 11 |   Siempre que el número de símbolos en el alfabeto sea una potencia de dos (como en este caso), el número promedio de bits.  La entropía de la fuente es . El código binario simple usa por símbolo. Para cumplir con el Teorema de Codificación Fuente de Shannon, el número promedio de bits por símbolo del código debería ser como mínimo igual y no mucho mayor a la entropía.  En este caso:  Esto muestra que el código binario simple cumple con el Teorema de Codificación Fuente porque:   1. El código es eficiente puesto que el **número promedio de bits por símbolo** (2 bits) es cercano a la **entropía de la fuente** (1.75 bits). 2. La diferencia es mínima, indicando que aunque **no es el código más eficiente posible**, tampoco es exageradamente ineficiente. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Codificación de Shannon Fano

La codificación Shannon-Fano es una técnica para construir un código **prefijo** basado en un conjunto de símbolos y sus probabilidades (estimadas o medidas). No es óptimo en el sentido de que no consigue la menor longitud de palabra código esperada posible como en la codificación Huffman; aunque a diferencia de la codificación Huffman, garantiza que todas las longitudes de palabras de código están a un bit de su ideal teórico.

Se toman los mensajes y se los ordena con probabilidades decrecientes de acuerdo con un análisis de tráfico que debe ser realizado previamente. Se agrupan los mensajes de tal forma que la suma de las probabilidades de ocurrencia sean aproximadamente equivalentes. Cada grupo se lo designa mediante el símbolo 1 o 0 y así sucesivamente.

| *Ejemplo:*   |  | Probabilidad | Secuencia de codificación | | | | Código | Entropía | | --- | --- | --- | --- | --- | --- | --- | --- | |  |  | 1 | 1 | | | 11 |  | |  |  | 0 | | | 10 |  | |  |  | 0 | 1 | 1 | | 011 |  | |  |  | 0 | | 010 |  | |  |  | 0 | 1 | 1 | 0011 |  | |  |  | 0 | 0010 |  | |  |  | 0 | 1 | 0001 |  | |  |  | 0 | 0000 |  | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##

## Método de Huffman para la construcción de códigos compactos

Primero, nos limitaremos a crear un código compacto relacionado a un alfabeto binario y luego nos extenderemos a crear un código compacto para un alfabeto r-ario.

### Construcción de código compacto binario

Consideremos una fuente S de símbolos y probabilidades. Supongamos ordenarlos de forma que:. Si los dos últimos símbolos los fundimos en uno solo (sumando sus probabilidades), se tiene una nueva fuente de símbolos. La denominaremos **fuente reducida de S**.

Ahora volvemos a ordenar los símbolos de igual forma y repetimos el proceso de ‘fundir’ los últimos dos símbolos, hasta llegar a una fuente de dos símbolos

El segundo paso consiste en asignarle un código compacto a la última fuente reducida, que precisamente es 0 y 1. Luego se *retrocede* en el procedimiento hasta que, habiendo partido de un código compacto, se obtenga en un código compacto.

| *Ejemplo:*   |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | |  |  |  |  |  |  |  |  | |  |  |  |  |  |  |  |  | |  |  |  |  |  |  |  |  | |  |  |  |  |  |  |  |  | |  |  |  |  |  |  |  |  |   Y ahora recorremos la tabla de manera inversa para obtener el código relativo a cada símbolo:   |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | |  |  |  |  |  |  |  |  | |  |  |  |  |  |  |  |  | |  |  |  |  |  |  |  |  | |  |  |  |  |  |  |  |  | |  |  |  |  |  |  |  |  |   O, de una manera más gráfica:  ![](data:image/png;base64...) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Al decir retroceder nos referimos a:

Sea el código compacto correspondiente a una de las fuentes reducidas, uno de sus símbolos, , estará formado por dos símbolos de la fuente procedente que denominamos y ; todos los demás símbolos se identifican con uno solo de . Según esto el código compacto (instantáneo) correspondiente a se deduce del de acuerdo a la siguiente regla:

Se asigna a cada símbolo de (excepto y ) la palabra correspondiente al símbolo de . Las palabras correspondiente a y se forman añadiendo un 0 y un 1 respectivamente, a la palabra asignada a .

Este proceso se repite de manera intermitente hasta que se llega a la fuente original.

Es posible demostrar que el código obtenido es compacto a través de una demostración matemática que no parece pertinente incluir en este trabajo.

### Código compacto r-ario

Por extensión, se puede ver que la obtención de un código compacto r-arios es similar al binario. Salvo que los símbolos se agrupan de a “**r**”.

De esta manera cada fuente reducida tendrá **r-1** símbolos menos que la anterior. Ahora nos cuestionamos, ¿la última iteración tendrá **r** símbolos ?

* La respuesta a esta pregunta es afirmativa si se cumple que, la fuente original está formada por símbolos donde siendo un número entero.
  + Si esto no ocurre se deberan añadir símbolos “falsos”. A los falsos símbolos se les asigna probabilidad nula, de modo que pueden ser ignorados una vez que el código haya sido construido.

## Rendimiento y redundancia de un código

El primer teorema de Shannon demuestra la existencia de una unidad común con la que puede medirse cualquier fuente de información.

El valor de símbolo de una fuente S puede definirse en términos del número equivalente de dígitos binarios necesario para representarlo. El teorema establece que el valor medio de un símbolo S es H(S), llamado entropía de la fuente.

Supongamos que L es la longitud media de un código de la fuente S, L no puede ser inferior a H(S). Según esto, se define el rendimiento de un código como:

Por otro lado, la redundancia es la información *superflua* o *innecesaria* para interpretar el significado de los datos originales. La introducción de redundancia en la codificación tiene como finalidad mejorar la fiabilidad de la transmisión. Se puede definir como:

## Confiabilidad VS Economía

Cuando transmitimos información de una fuente a través de un canal real, el ruido presente en este canal puede distorsionar la información que estamos tratando de enviar.

O sea:

* Se emite 001
* Se recepciona 011

Por lo tanto, resulta crucial investigar cómo detectar e incluso corregir ciertos tipos de errores que puedan surgir en el canal de comunicación.

Se define como **Ruido Unitario** al cambio, en una palabra de un binit por su complemento (con el requerimiento de que hablemos de codificación binaria).

### Paridad

Este es un criterio de detección de error que consiste en agregar a la palabra codificada un binit llamado ‘de paridad’(ip) que posee un valor obtenido al realizar el siguiente cálculo:

Si se trabaja con paridad par (bit que es 1 si la palabra es par y 0 si la palabra es impar)

En el caso de que se trabaje con paridad impar, el bit de paridad quedará determinado por el siguiente cálculo:

| *Nota*: Otra forma más simple de encontrar el valor del bit de paridad, evitando usar las compuertas lógicas or exclusivas, es realizando la siguiente observación:   * Cuando se utiliza la paridad **par**, se realiza un **conteo** de **unos** en los datos a enviar.   + Si la cantidad de unos es un número impar, se agrega un bit de paridad establecido en uno para que la suma total, incluyendo este bit de paridad, sea par.   + Por otro lado, si el conteo de unos es un número par, el bit de paridad permanece en cero, ya que la suma total es ya par. * Por otro lado, en el caso de la paridad **impar**, el proceso es similar pero inverso. Se cuenta el número de unos en los datos   + Si este total es impar, se agrega un bit de paridad establecido en cero para que la suma total sea impar.   + Si el conteo de unos es par, se añade un bit de paridad establecido en uno para garantizar que la suma total sea impar. |
| --- |

Siendo:

* ip : bit de paridad (impar o par).
* : función “or exclusive”.
* n : longitud de la palabra código

donde: , con , son los bit que conforman la palabra código

Y luego la palabra que se transmite es la palabra código con el bit de paridad agregado al final(es decir, a la derecha):

Al recepcionar se controla si cumple con el cálculo de paridad teniendo en cuenta si se utiliza paridad par o si se utiliza paridad impar. Si en el camino se produjo algún error unitario se altera la paridad de la palabra, siendo posible detectarlo en el destino.

Con este tipo de control no solo se puede llegar a detectar sino también **a corregir** empleando los chequeos de paridad horizontal y vertical. Para ello, se siguen la siguientes instrucciones con los datos:

1. Los caracteres a transmitir se ordenan en una matriz de m filas y n columnas. Quedándonos una matriz de dimensiones
2. Se calcula el bit de paridad de cada fila y se añade al principio (o al final, según convenio) de la fila
3. La nueva columna estará formada por los bits de paridad horizontal de todas las filas
4. Se calcula el bit de paridad de cada columna y se añade al principio (o al final, según convenio) de la columna
5. La nueva fila estará formada por los bits de paridad vertical de todas las columnas.
6. El bloque final a transmitir tendrá por tanto una fila y una columna más que el original. Es decir, se obtendrá una matriz de dimensiones
7. Adicionalmente se puede emplear un bit de paridad cruzada que se calcula a partir de los bits de paridad de filas y columnas.
8. Se envían los datos dispuestos en la matriz, incluyendo los bits de paridad. Se supone que se pre-determinó el valor de m y el valor de n con el receptor.

Cuando se recibe esta matriz, si un binit ha sido alterado por el ruido del canal de comunicación, la paridad de la fila y la columna afectadas ya no coincidirá con los bits de paridad correspondientes. Por lo tanto, el receptor puede identificar fácilmente qué binit ha sido alterado simplemente revisando las paridades de fila y columna. Si el alterado es una de los bit de paridad, es detectado por el incumplimiento de la paridad cruzada.

La redundancia se introduce mediante la adición de bits de paridad. Aunque estos binits no transmiten información directa, actúan como medidas de control para detectar y, en algunos casos, corregir errores.

| *Ejemplo:*  Supongamos un código que determina un mensaje de 48 binit que decidimos partir en bloques de 8 de largo y 6 de alto (m=8 y n=6).  Si ahora planteamos la matriz de , nos queda:   |  | Bit 1 | Bit 2 | Bit 3 | Bit 4 | Bit 5 | Bit 6 | Bit 7 | Bit 8 | Paridad Horizontal | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | |  | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | |  | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | |  | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | |  | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | |  | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | |  | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | | Paridad Vertical | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | **0** | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### ¿ Dónde se pone en evidencia la redundancia, como factor de absorción del ruido?

Pensemos que tenemos 3 símbolos en nuestro alfabeto código. Con esto podemos codificar símbolos de una fuente, o sea 8 símbolos. Si ahora agregamos un bit de paridad seguiremos codificando símbolos (ahora con protección). Pero con 4 símbolos en el alfabeto código, se pueden codificar símbolos fuente o sea 16. De esto se deduce que no se utilizan:

- = 3 configuraciones

Estas son precisamente las configuraciones que nos absorben el ruido.

En este contexto, la redundancia proporcionada por los bits de paridad ayuda a absorber el ruido introducido por el canal de comunicación.

Cuando se utilizan más bits para la redundancia, como en el caso de agregar un bit de paridad adicional, se aumenta la capacidad de detectar y corregir errores, lo que hace que la comunicación sea más robusta frente al ruido.

### Por mayoría

La clave de este método es codificar los datos de manera que el número de unos o ceros en cada palabra sea significativamente diferente.

| *Ejemplo:*  Si suponemos que codificamos con una longitud constante de 5 y peso 3 de unos:  Para poder saber cuántos códigos diferentes podemos plantear las combinaciones de 5 elementos tomados de 3:  Y si ahora nos tomamos la molestia de plantear todos los códigos posibles que cumplan con esas condiciones obtenemos los 10 códigos posibles:  Observe que si hubiéramos codificado con una longitud constante de 5 y sin limitaciones habríamos tenido códigos diferentes |
| --- |

Este método se utiliza principalmente para detectar errores en la transmisión de datos y es especialmente útil cuando se espera que ocurran errores en la comunicación. Sin embargo, no permite corregir los errores, solo detectarlos.

### De igual peso

Es muy similar al de mayoría, salvo que ahora se codifica de forma tal de que el número de “1s” sea igual al número de “0s”. Esto se logra mediante un diseño cuidadoso de las palabras de código, de modo que el número total de unos sea igual al número total de ceros

Las palabras codificadas resultantes tendrán una longitud (l) que es par. Esto se debe a que para que el número de unos y ceros sea igual en cada palabra, la longitud de la palabra debe ser un número par. Por ejemplo, si una palabra codificada tiene una longitud de 8 bits, habrá 4 unos y 4 ceros.

En resumen, el método de igual peso en la codificación busca equilibrar el número de unos y ceros en cada palabra codificada, asegurando que haya una cantidad igual de cada uno. Esto ayuda a proporcionar una forma de detección de errores más robusta, ya que cualquier discrepancia en el número de unos y ceros en la palabra recibida puede indicar un posible error en la transmisión.

| *Ejemplo:*  Si suponemos que codificamos utilizando el método de igual peso podemos obtener los siguientes códigos: |
| --- |

### Repetición

Otro código usado para detectar y corregir posibles errores unitarios se trata de la **repetición**. Consiste en predeterminar un número de repetición para cada binit para luego durante la comunicación, repetir cada binit veces y pasar al siguiente binit.

| *Ejemplo:*  Si suponemos un número de repetición , y debemos transmitir el binit . La transmisión será: |
| --- |

La utilidad de este método se ve en que si al recibir tres bits, estos no son idénticos, sabremos que ha ocurrido un error. Mejor aún, si tenemos un canal en el que los fallos que se producen son unitarios, podríamos establecer una **regla de decisión** en donde:

Prestando atención a que la mayor cantidad de dígitos establece de qué binit se trata, es decir, como se reciben 2 unos y 1 único cero, sabremos que se tratará del binit 1.

Sin embargo, este método se vuelve más ineficiente a medida aumentamos el número de repeticion. Pues, estamos exigiendo a la transferencia enviar veces el mismo binit para poder detectar y corregir errores.

## Regla de decisión

Hasta ahora hemos observado que ciertos métodos de protección de datos son capaces de detectar errores, pero carecen de la capacidad de corregirlos. En algunos contextos, esta limitación se aborda solicitando una retransmisión de la información una vez que se ha detectado un error. Sin embargo, en ciertas aplicaciones, esta solución no es viable.

En estos casos, es necesario buscar alternativas, como la adopción de una Regla de Decisión. Esta estrategia implica **modificar** una palabra recibida que se sabe está incorrecta, de tal manera que adopte la forma de una palabra sin errores. Es importante destacar que esta modificación conlleva una cierta probabilidad de cometer un nuevo error o de corregir el existente.

Por lo tanto, es fundamental seleccionar una Regla de Decisión que minimice esta probabilidad de error, asegurando así la integridad de la información transmitida.

| *Ejemplo:*  Si nuestros símbolos de fuentes están compuestos por un único tipo de cifra binaria, ya sea uno o cero. Nuestros códigos se verán de la siguiente manera:   |  | 111 | | --- | --- | |  | 000 |   Si sabemos que el canal tiene una probabilidad relativamente elevada debe provocar cambios unitarios y en mucho menor grado, errores de orden superior. La regla de decisión es evidente:   * … |
| --- | --- | --- | --- | --- |

##

## Hamming (Paridad por Zonas)

Al igual que los códigos anteriormente vistos, el **código Hamming** permite la detección y corrección de errores que pueden ocurrir durante la transmisión de datos. También incluye la idea de lograr esa detección y corrección de errores agregando bits de paridad adicionales a los datos iniciales.

Sin embargo, el código Hamming aplica una cierta estrategia a la hora de decidir que rol cumplirá cada bit de paridad de manera que tenga ciertas características que permiten detectar y corregir errores.. Como dijimos, este código utiliza control de paridad, pero no sobre la palabra completa que se va a transmitir, sino por grupos de bits.

¿Cómo funciona esto?

La idea es que se agrupen los bits que forman la palabra en subgrupos de bits. Cada grupo posee un bit de paridad, por ende, al existir varios grupos habrán varios bits de paridad que deben agregarse a la palabra código para formar la palabra de transmisión. Al agregar esos bits de paridad a la palabra, obtendremos una palabra completa de bits.

Podemos denotar un código de Hamming mediante un par , donde:

* es la longitud de la palabra
* es el número de bits de datos de la palabra original sin codificar
* el número de bits de paridad será

La forma de una palabra de código es la siguiente:

O sino, unificando todo como símbolos C:

Cualquier código relacionado a Hamming es notado con esta expresión de tipo dupla, un ejemplo es el código Hamming(7-4) que veremos luego.

La adición de bits de paridad a una palabra original influirá en posiciones específicas de la nueva palabra de código, por lo que cada bit de paridad tendrá un valor apropiado para cumplir con el criterio de paridad (par o impar) establecido en las subcombinaciones afectadas por cada bit de paridad. Este es el método utilizado para analizar la corrección de un error simple.

## Distancia Hamming

Llamamos **distancia Hamming** entre dos palabras *de mismo largo* a la cantidad de posiciones en donde sus símbolos son diferentes. Dicho de otra manera, mide la cantidad mínima de sustituciones que tenemos que hacer en una de las palabras para transformarla en la otra. También puede verse como, el mínimo número de errores **unitarios** que hubieran transformado una de las palabras en la otra

Los símbolos dependen del alfabeto que se haya determinado usar en la transmisión pero pueden ser letras, bits, número decimales, entre otros.

| *Ejemplos:*  La **distancia Hamming** entre:   * 1111 y 0010 es **3** . * 2873496 y 2233796 es **3**. * Pedro y Pedre es **1**. * Jorge y Jorgelina no es válida pues ambas palabras deben tener *el mismo largo* |
| --- |

En el caso de un alfabeto binario, y dependiendo el largo de la palabra, es posible construir figuras geométricas que nos ayudan a entender este concepto. Cada arista de las figuras representa un cambio en algún bit de la palabra. En el caso de una palabra de **3** posiciones, puede conformarse un cubo de la siguiente manera:

![](data:image/png;base64...)

Teniendo en cuenta siempre el **mínimo recorrido** entonces podemos observar que para llegar de, por ejemplo:

* La palabra 010 a la palabra 111, hay que recorrer únicamente 2 aristas.
* La palabra 100 a la palabra 011, hay que recorrer necesariamente 4 aristas.

![](data:image/png;base64...)

## Hamming(7,4)

Uno de los ejemplos más famosos de Hamming es el código llamado Hamming (7-4), este se trata de un código que codifica cuatro bits de información en siete bits, agregando tres bits de paridad.![](data:image/png;base64...)

El código Hamming(7,4) agrega tres bits adicionales de paridad por cada cuatro bits de información del mensaje original. El beneficio de este código es que permite detectar y corregir cualquier error unitario y detectar errores de dos bits. Dicho de otra forma, la mínima distancia de Hamming entre dos códigos correctos es de 3, y la mayoría de palabras recibidas puede ser decodificada correctamente si están como máximo a una distancia del código transmitido por el emisor.

Los mensajes son distribuidos de la siguiente manera:

¿Cómo se procede a desglosar el mensaje y entender los bits de paridad?

La idea es obtener los bits de paridad y haber predeterminado el rol de cada bit de paridad para la transmisión, en el caso del código Hamming(7,4) cada bit de paridad siempre estará relacionado a tres bits de información. Por ejemplo:

* cubre , y . Es decir,
* P2 cubre , y . Es decir,
* P3 cubre , y . Es decir,

Podemos determinar si ha ocurrido un error al calcular la paridad de cada conjunto de bits (tanto los bits de paridad como los bits de datos) y, si es así, en qué posición. Por ejemplo, si ocurre un error en el bit , esto tendría un impacto en la paridad de los bits que están bajo el control de y . Dicho de otra manera, si simultáneamente viéramos que no se cumple ni la paridad establecida por el bit ni tampoco la paridad establecida por el bit , sin dudar podríamos saber que el bit ha sido alterado, ya que es el bit compartido por ambas reglas de paridad.

De esta manera, podemos determinar qué bits causaron el error observando cuál paridad no coincide con el resto. Si se eligen correctamente los bits de paridad, se pueden detectar y corregir todos los errores con una **distancia Hamming de 1**, que es el objetivo de utilizar un código Hamming.

| *Ejemplo:*  Supongamos que se ha decidido usar Hamming(7,4) para una transmisión. Luego, en un momento dado de la transmisión al receptor le llega el mensaje:  Procedemos ahora a descomponer este mensaje:   |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | |  |  |  |  | 1 | 0 |  |   Ahora analicemos los bits de paridad:   * ![](data:image/png;base64...)   Como vemos que las reglas de paridad establecidas por y no se cumplen, podríamos asumir que el bit erróneo es . De esta manera, si cambiamos podríamos obtener el mensaje original: |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

De manera que es un código muy efectivo para transmisiones más propensas a tener errores unitarios y no tantos errores de mayor orden. El medio debería tener mucho ruido para que se produjeran errores de mayores órdenes y/o ráfagas de errores.

# Códigos Lineales

## Códigos de Bloques

Se dice que un código es un código de bloque cuando sus palabras códigos tienen longitud constante (Ii = n para todo i). El código bloque admite una estructura algebraica de grupo y de espacio vectorial. En este caso, los elementos del código bloque son vectores que se corresponden a las palabras código.

Para empezar, definimos el cuerpo conmutativo (K, +, \*). En el caso de la codificación binaria resulta ser ([0, 1], +, \*) que se define de la siguiente forma:

| **(a, b)** | **+** | **(a, b)** | **\*** |
| --- | --- | --- | --- |
| 00 | 0 | 00 | 0 |
| 01 | 1 | 01 | 0 |
| 10 | 1 | 10 | 0 |
| 11 | 0 | 11 | 1 |

(+) Suma Binaria

(\*) Producto Binario

También se define el grupo (V, +) que son los vectores asociados a cada palabra código, donde los elementos de cada vector pertenecen a nuestro conjunto [0, 1] y la ley de descomposición binaria “+” es la suma binaria de vectores:

**V1 + V2 = (X1, .............., Xn) + (g1, ........, gn)**

**V1 + V2 = (X1 + g1, .............., Xn + gn)**

*Ejemplo:*

Consideramos un bloque con li = 3, la base serán tres vectores linealmente

independientes:

**V1 = (0, 0, 1); V2 = (0, 1, 0); V3 = (1, 0, 0)**

Toda palabra código de este bloque se generará a partir de esta base de la siguiente forma:

***Vi = k1 \* V1 + k2 \* V2 + k3 \* V3 ; con ki ε K***

Confeccionamos la tabla para la generación de este código:

| **(k1, k2, k3)** | **Vi** |
| --- | --- |
| 000 | 000 |
| 001 | 100 |
| 010 | 010 |
| 100 | 001 |
| 101 | 101 |
| 110 | 011 |
| 111 | 111 |

Por otro lado, dentro de los códigos de bloques se define una distancia o métrica conocida como la *distancia de Hamming,* donde y son dos palabras de código. El resultado numérico de esta distancia entre y es la cantidad de dígitos que difieren entre ellos. Por ejemplo:

Sean y . Entonces .

En caso de estar trabajando con código binario la expresión puede abreviarse de la siguiente manera: donde y peso de unos (cantidad de “1” presentes en la palabra de código).

## Códigos de Grupo

Sabemos que todo subespacio vectorial del espacio vectorial asociado a un código en bloque constituye un código lineal. Si el código en bloque del cual proviene el subespacio es binario entonces a todo código de bloque proveniente de su subespacio le llamaremos **Código de grupo**.

Los códigos de grupo tienen la particularidad de permitirnos detectar errores en mensajes alterados por ruido y en ciertas ocasiones incluso corregirlos adoptando una regla de decisión para decodificar el mensaje alterado; La regla de decisión es sencilla: Consiste en asignar al mensaje alterado (Lo llamaremos U\*) la palabra perteneciente al código que esté a menor distancia Hamming de U\* .

Como la palabra alterada U\* no pertenece al código entonces su distancia mínima es si o si mayor o igual a 1, llamaremos a esta distancia “μ”. Con este dato podemos concluir que solo será posible detectar (μ - 1) errores pero solamente será posible corregir hasta el (μ - 1) / 2 errores.

## Espacio nulo

Se conoce como espacio nulo V’ al espacio vectorial que contiene todas las palabras que **no** pertenecen al código que estemos trabajando. Como dichas palabras no pertenecen al código entonces matemáticamente sus vectores serán necesariamente ortogonales a aquellos pertenecientes al código del grupo V.

Si definimos una matriz base de V’ de n x m dimensiones compuesta por palabras código que no pertenecen al código original y que además son linealmente independientes entre sí entonces podemos definir una matriz generadora ‘H’ que contiene a dichas palabras. A esta matriz H base de V’ la denominamos **matriz de control de paridad.**

## Síndrome

Se define como síndrome de una palabra código S(vj) al producto de el vector de la palabra código por la matriz de control de paridad transpuesta

**S(vj) = vj . HT**

*Por lo tanto*

**S(vj) = 0 Si y sólo si vj pertenece a V, es decir es una palabra código y no pertenece al espacio nulo.**

Si se da el caso en el cual el síndrome de una palabra código es distinto de cero entonces necesariamente el mensaje tuvo un error y debe decodificarse utilizando una regla de decisión o solicitar un reenvío del mismo.

Para corregir un mensaje con error ‘U\*’ utilizando el síndrome podemos definir la siguiente igualdad:

U\* = U + gi

Donde gi es una palabra perteneciente a V’ con el objetivo de modelar el error. Calculando el síndrome de todos los gi terminaremos eligiendo el gi que tenga el menor número de cambios afectando la palabra código.

# Conclusiones

En conclusión, una investigación exhaustiva de la codificación y los códigos lineales nos ha demostrado que estos conceptos son cruciales en la teoría de la información y las comunicaciones. Demostramos como la inecuación de Kraft destaca la necesidad de eficiencia en la transmisión de datos y se presenta como una herramienta fundamental para evaluar la posibilidad de crear códigos instantáneos. Por otra parte, el primer teorema de Shannon proporciona un marco teórico en el cual se destaca la capacidad de transmitir información sin errores siempre y cuando se cumplan ciertas condiciones fundamentales. Finalmente, al estudiar códigos de bloque y grupo comprendemos por qué estos son cruciales para la transmisión confiable de datos en el campo de los códigos lineales cuya estructura y características ayudan a aumentar la confiabilidad de los sistemas de comunicación permitiendo una detección y corrección eficientes de errores.

Haciendo un breve resumen de este trabajo hacemos hincapié en el rol esencial que cumple la codificación y los códigos lineales al momento de optimizar la transmisión de datos y garantizar una comunicación eficiente e integrada a través de canales que se ven afectados por fuentes de ruido. Consideramos que estos conceptos cobran una importancia vital a la hora de aplicarlos al mundo actual atravesado por la tecnología de la información, ya que en este ámbito resulta indispensable comprender dichos conceptos en pos de diseñar e implementar sistemas de comunicación robustos y confiables.

# Bibliografía

Cátedra de Comunicación de Datos. (2024). “*Codificación”*. Universidad Tecnológica Nacional. Facultad Regional Rosario.

Cátedra de Comunicación de Datos. (2024). “*Códigos lineales”*. Universidad Tecnológica Nacional. Facultad Regional Rosario.

*“Hamming”*. (2019). Universidad Tecnológica Nacional. Facultad Regional Córdoba. <https://www.profesores.frc.utn.edu.ar/electronica/tecnicasdigitalesi/pub/file/Publicaciones/Hamming.pdf>

Holik, Federico. 2016. "*Teoría de la información de Claude E. Shannon*". En Diccionario Interdisciplinar Austral, editado por Claudia E. Vanney, Ignacio Silva y Juan F. Franck. URL=[http://dia.austral.edu.ar/Teoría\_de\_la\_información\_de\_Claude\_E.\_Shannon](http://dia.austral.edu.ar/Teor%C3%ADa_de_la_informaci%C3%B3n_de_Claude_E._Shannon)

Loja, K. (2021). “*Deber 4 U2. DETALLADO DE LA INECUACIÓN DE KRAFT”*. En *Studocu*. Universidad del Norte (México). <https://www.studocu.com/es-mx/document/universidad-del-norte-mexico/teorias-de-la-comunicacion/deber-4-u2-inecuacion-de-kraff/16435934>

Sanromán, G. (s. f.). “*Estrategias de decodificación”* [Universidad Nacional de La Plata]. <https://sedici.unlp.edu.ar/bitstream/handle/10915/22493/Documento_completo.pdf?sequence=1&isAllowed=y#:~:text=Se%20denomina%20c%C3%B3digo%20no%20singular,le%20corresponde%20una%20%C3%BAnica%20codificaci%C3%B3n>.

Teorema de Codificación Fuente. (2022, October 30). Rice University. [https://espanol.libretexts.org/@go/page/85513](https://espanol.libretexts.org/%40go/page/85513)

# Anexo: Autoevaluación con Preguntas y Respuestas

1. **En un sistema de comunicación, ¿Qué es una fuente? ¿Y el alfabeto fuente?**

Una fuente se encarga de generar el mensaje destinado a ser recibido por el destinatario. Es un sistema que contiene un conjunto de estados diferentes llamados símbolos. El conjunto de símbolos disponibles para la codificación forman el Alfabeto Fuente (S) desde el cual se extraen las secuencias de símbolos que se van a codificar.

1. **Defina formalmente el término “codificación” y luego explique con sus palabras.**

Si denominamos S = (s1; s2; ..........; sq) al conjunto de símbolos de un alfabeto dado; queda definida una *codificación* al poner en correspondencia todas las secuencias posibles de símbolos de S con secuencia de símbolos de algún otro alfabeto Z = (z1; z2; ...........; zr). Entonces “S” recibe el nombre de alfabeto fuente y “Z” alfabeto código.

En otras palabras, la codificación es el proceso de asignar secuencias de símbolos del alfabeto fuente (S) a secuencias de símbolos de algún otro alfabeto (Z) donde Z es generalmente un conjunto de símbolos binarios (0 y 1) cuya utilidad es facilitar la transmisión y el almacenamiento de la información.

1. **Enumere y explique brevemente las propiedades de la codificación.**

Las propiedades de la codificación son:

* Código Bloque: aquel que asigna a cada uno de los símbolos del código fuente S una secuencia fija (palabras código) de símbolos del alfabeto código (Z).
* Código no singular: aquel bloque de código en el cual a cada símbolo codificado le corresponde una única codificación.
* Código unívocamente decodificable: si a cualquier secuencia de palabras código, le corresponde una y sólo una secuencia de símbolos de la fuente.
  + Instantáneo: un código es unívocamente decodificable instantáneo cuando es posible decodificar las palabras de una secuencia sin precisar el conocimiento de los símbolos que la suceden.

1. **¿Para qué se utiliza la inecuación de Kraft?**

La inecuación de Kraft nos permite saber rápidamente si, dada una longitud, cantidad de mensajes y símbolos diferentes en un código, es posible formarse un código instantáneo o no.

Si el resultado es menor o igual que uno quiere decir es posible realizar un código instantáneo con las longitudes que se nos plantea, y si el resultado es mayor que uno nos quiere decir que no se puede realizar un código instantáneo con las longitudes dadas.

1. **¿Cuál es la diferencia entre H(S) y Hr(S)?**

Hr(S) es una simplificación de una de las expresiones de la ecuación de longitud media, que permite expresarcomo la entropía en unidades r-arias, de lo que resulta Hr(S). Por otro lado, hemos puesto en relación dos magnitudes: la Hr(s) con la longitud media, que no depende de H(s).Esto también pone en relación dicha magnitud.

1. **¿En qué parte del proceso suelen presentarse errores en la transmisión de información?**

Los errores más comunes en la transmisión suelen presentarse al momento de transferir información de una fuente a través de un canal real. Estos canales de comunicación pueden potencialmente presentar ruido, ya sea por el material del canal o por algún fenómeno externo (Como un campo electromagnético generado por un motor cercano al canal) que genera una variación en el mensaje enviado por la fuente haciendo que el mismo llegue al receptor de manera truncada y necesite ser corregido mediante algún algoritmo o ser reenviado.

1. **¿Cuáles son los criterios de detección de errores?**

Los criterios de detección de errores son:

* Paridad: consiste en agregar a la palabra codificada un binit llamado "de paridad" que posee un valor obtenido al realizar ciertos cálculos específicos. Estos bits de paridad no transmiten información directa, sólo actúan como medidas de control para detectar y a veces corregir errores.
* Por mayoría: La idea principal de este enfoque es codificar los datos de tal manera que haya una diferencia significativa en el número de unos o ceros en cada palabra. Este criterio es especialmente útil cuando se espera que ocurran errores en la comunicación. A diferencia del criterio de paridad, este método sólo detecta errores, no permite corregirlos.
* De igual peso: Similar al anterior, sólo que en este criterio se codifica de manera tal que la cantidad de unos sea igual a la cantidad de ceros. Proporciona una forma de detección de errores robusta, ya que cualquier discrepancia en el número de unos y ceros en la palabra recibida puede indicar un posible error en la transmisión.
* Repetición: Consiste en predeterminar un número de repetición n para cada binit para luego durante la comunicación, repetir cada binit n veces y pasar al siguiente binit. Es ineficiente a medida que se aumenta el número de repeticiones.

1. **¿Por qué es importante minimizar la probabilidad de error? Justifique.**

Hay que asegurar la integridad de la información transmitida mediante la minimización de las probabilidades de error. Más allá de detectarlos, hay que ser capaces de corregirlos adoptando, por ejemplo, una Regla de Decisión que implica modificar una palabra recibida que se sabe de antemano que es incorrecta, de tal manera que adopte la forma de una palabra sin errores. Cabe aclarar que dicha Regla de Decisión puede conllevar a su vez a cometer nuevos errores.

1. **¿En qué se diferencian los códigos de bloque de los códigos de grupo?**

La diferencia característica es que los códigos de grupo están construidos exclusivamente con un alfabeto binario mientras que los códigos de bloque pueden contener palabras que no pertenezcan a dicho alfabeto. Por lo tanto, todo código de grupo es un código de bloque, pero no todo código de bloque es un código de grupo.

1. **¿Cuál es la utilidad de hallar el espacio nulo asociado a un código?**

La utilidad de hallar el espacio nulo asociado a un código radica en utilizarla para generar la matriz de control de paridad. Dicha matriz será utilizada a la hora de encontrar el síndrome de las palabras del código y determinar si las mismas pertenecen al mismo (Si el síndrome de una palabra es 0 entonces la misma pertenece al código original, si se da el caso contrario entonces ha ocurrido un error en la transmisión). Posteriormente utilizaremos el síndrome para corregir posibles errores de transmisión así que podemos concluir que determinar el espacio nulo asociado a un código es de vital importancia para llevar a cabo operaciones de comunicación y corrección de errores.