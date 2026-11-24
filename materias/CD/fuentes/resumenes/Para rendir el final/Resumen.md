**Teoría De La Información**

**Entropía De Una Fuente**

Es la información media por símbolos de la fuente. Se define:

**Entropía De Un Sistema**

Es la incertidumbre de aparición en el sistema. La información media al emitir y recepcionar . Se define:

**Información Mutua**

Es la cantidad de información transmitida del emisor al receptor, esto es, la información real que llega al receptor en promedio. Se define:

**Capacidad De Un Canal De Información**

Es la capacidad para transportar información. Se define:

Si la fuente fuera equiprobable y emitiera un símbolo:

En el caso binario equiprobable:

Siendo la tasa de información, si , es posible transmitir por el canal a una frecuencia en la que relativamente no hay error. Si, no es posible transmitir sin error.

**Eficiencia Y Redundancia**

Se define la eficiencia como:

Y la redundancia como la parte no aprovechada de la capacidad del canal:

**Velocidad O Tasa De Información**

Es la cantidad de bits en promedio que se transmiten en 1 segundo, es decir, la cantidad de información producida por la fuente en 1 segundo.

Si se considera un canal con ruido:

En el caso de ser equiprobables los símbolos de la fuente:

**Velocidad O Tasa De Dígitos**

Es la cantidad de dígitos transmitidos en 1 segundo. Se define:

En el caso de ser equiprobables los símbolos de la fuente:

**Velocidad De Señalización**

Es la inversa del tiempo mínimo que dura un pulso. Se define:

**Errores De Canal**

**Ruido Blanco**

Ocurre por la excitación de átomos y moléculas producida por la temperatura. Esto genera una reducción en la capacidad del canal para transmitir información. No se lo puede eliminar debido a su aleatoriedad.

**Causas De Los Errores De Canal**

* Ruidos impulsivos: producen grandes picos en la amplitud de la señal de ruido blanco, provocando perturbaciones de varios binits, constituyendo lo que se denomina ráfaga. Las causas que provocan el ruido impulsivo pueden ser externas o internas. Las causas externas son:
* Acoplamientos capacitivos o inductivos.

Las causas internas son:

* Variaciones en la impedancia,
* Sobrecarga de amplificadores,
* Interferencia debido a armónicas espurias.

El ruido impulsivo se puede tratar con la utilización de módems.

* Modulaciones espurias: pueden ser de tres tipos.
* Modulación cruzada: los acoplamientos inductivos generan captación de otras señales.
* Intermodulación: producida por la variación en la linealidad de los amplificadores. Al amplificar las señales estas se superponen. Esto se puede reducir utilizando módems o reduciendo la amplitud de las señales.
* Eco: las variaciones de impedancia producen reflexiones en la señal provocando eco. Esto se puede corregir utilizando supresores de eco.
* Variaciones de nivel: afecta la transmisión de datos. Las causas que las provocan son:
* Variaciones en la impedancia del canal.
* Enmascaramiento de la señal.
* Falla en los contactos.
* Falla en los amplificadores.
* Distorsión: es introducida por el propio canal. Las más conocidas son:
* Atenuación: producida por las variaciones en la impedancia.
* Fase/Frecuencia: se debe a que el canal introduce retardos para frecuencias distintas, provocando desfasaje entre las armónicas.
* Variación de frecuencia de la portadora: se puede corregir mediante una señal sub-portadora de sincronismo en frecuencia.
* Variación del nivel de muestreo: ocurre en la recepción, al demodular. Produce una modificación en el ancho de los pulsos de la señal.

**Codificación**

**Código De Bloque**

Es aquel que asigna a cada elemento del alfabeto fuente una secuencia fija de símbolos del alfabeto código. Estas secuencias fijas se denominan palabras código.

**Código No Singular**

Es aquel que tiene todas sus palabras código distintas. Ejemplo:

S1 0

S2 11

S3 00

S4 01

**Código Unívocamente Decodificable**

Un código es unívocamente decodificable si a cualquier secuencia de palabras código le corresponde una y sólo una secuencia de símbolos de la fuente. La condición para que un código sea unívocamente decodificable es que su extensión de orden *n* sea no singular para cualquier valor finito de *n*.

S1 00

S2 01

S3 10

S4 11

**Código Instantáneo**

Un código es instantáneo cuando es posible decodificar las palabras de una secuencia sin precisar el conocimiento de lo símbolos que las suceden. La condición para que un código sea instantáneo es que ninguna palabra código coincida con el prefijo de otra.

S1 0

S2 10

S3 110

S4 1110

**Inecuación De Kraft**

Es la condición necesaria para que exista al menos un código instantáneo de símbolos en su alfabeto y cuyas palabras código tienen una longitud :

**Inecuación De McMillan**

Es la condición necesaria para que exista al menos un código unívoco de símbolos en su alfabeto y cuyas palabras código tienen una longitud :

**Código Compacto**

Un código unívoco que asocia los símbolos de una fuente con palabras formadas por símbolos de un alfabeto r-ario es compacto si la longitud media es igual o menor que la longitud media de todos los códigos unívocos que pueden aplicarse a la misma fuente y al mismo alfabeto.

**Longitud Media De Un Código**

Dado un código bloque que asocia los símbolos de una fuente con palabras , y sus probabilidades de los símbolos son , la longitud media se define:

**Cota Inferior De La Longitud Media**

La longitud media de un código es mayor o igual que la entropía de la fuente dividida por el logaritmo en base dos de número de símbolos del alfabeto código:

**Códigos Lineales**

**Código De Bloque**

Se dice que un código es de bloque cuando su longitud es constante. El código de bloque admite que se le asocie una estructura algebraica de grupo y espacio vectorial.

**Código De Grupo**

Todo sub-esquema vectorial del espacio vectorial asociado a un código de bloque constituye un código lineal. Si el código de bloque del cual proviene es binario, entonces éste código lineal es denominado código de grupo. Un código de grupo queda definido por su matriz generadora G, donde sus filas están constituidas por palabras código que forman la base. La combinación lineal de las filas forma el código de grupo.

**Síndrome**

Definimos al síndrome de una palabra código al producto del vector asociado por la matriz de control de paridad transpuesta:

El síndrome de una palabra código es cero sí pertenece al código de grupo. Si es distinto de cero, el mensaje tuvo un error y debe decodificarse adoptando una regla de decisión. Esta regla de decisión puede ser la de máxima verosimilitud, que consiste en decodificar la palabra código con ruido asignándole la palabra del código de grupo que esté a menos distancia de Hamming.

**Matriz De Control De Paridad**

A partir de una base generadora, se puede obtener la matriz de control de paridad. Si se tiene la base generadora:

Y haciendo:

, siendo

Resolviendo el sistema de ecuaciones, se obtiene una matriz:

, con

De esta matriz obtenemos la matriz de control de paridad, seleccionando filas linealmente independientes:

**Comunicación Digital**

**ASK**

En la modulación ASK se mantiene constante la fase y la frecuencia y se varía la amplitud. La amplitud varía de acuerdo al tamaño del mensaje.

El proceso de modulación es el siguiente:

![](data:image/x-emf;base64...)

![](data:image/x-emf;base64...)

La señal de frecuencia lleva como envolvente la señal de modulación:

![](data:image/x-emf;base64...)

El análisis armónico es:

![](data:image/x-emf;base64...)

El espectro de frecuencias es:

![](data:image/x-emf;base64...)

El ancho de banda de una señal ASK es igual a .

Para la demodulación se pueden utilizar las técnicas de demodulación sincrónica o asincrónica. En la demodulación sincrónica la portadora se encuentra en el receptor y está en sincronismo de fase con el emisor. El proceso es el siguiente:

![](data:image/x-emf;base64...)

El proceso de demodulación asincrónica es:

![](data:image/x-emf;base64...)

![](data:image/x-emf;base64...)

**FSK**

En la modulación FSK se varía la frecuencia y se mantiene constante la amplitud y la fase. La portadora varía su frecuencia dependiendo de si la señal de modulación tiene un nivel alto o bajo. Se puede pensar que la modulación FSK es la superposición de dos señales ASK de distintas frecuencias.

El proceso de modulación es:

![](data:image/x-emf;base64...)

![](data:image/x-emf;base64...)

Obteniendo el siguiente espectro de frecuencias:

![](data:image/x-emf;base64...)

El ancho de banda depende de la señal en banda base.

La demodulación puede realizarse en forma sincrónica o asincrónica. Para la modulación sincrónica, la portadora se encuentra en el receptor y debe estar en sincronismo de fase con el emisor. El proceso es el siguiente:

![](data:image/x-emf;base64...)

El proceso de demodulación asincrónica es:

![](data:image/x-emf;base64...)

**FSK Multinivel**

Se utilizan dos amplitudes y dos frecuencias, dando lugar a cuatro posibilidades con dos dígitos. Se transmiten más dígitos en la misma unidad de tiempo.

![](data:image/x-wmf;base64...)

**PSK**

En la modulación PSK se mantiene constante la frecuencia y la amplitud y se varía la fase. Para generar la señal PSK se multiplica una señal binaria bipolar por la portadora. El proceso de modulación es:

![](data:image/x-emf;base64...)

![](data:image/x-emf;base64...)

Obteniendo el siguiente espectro de frecuencias:

![](data:image/x-emf;base64...)

Esta modulación suministra mayor cantidad de información que la FSK, en el mismo ancho de banda.

Sólo se puede utilizar la demodulación asincrónica. El proceso es:

![](data:image/x-emf;base64...)

**PSK Multinivel**

Se tienen dos fases y cuatro amplitudes. Dos amplitudes para cada fase, eso da ocho posibilidades con tres dígitos:

![](data:image/x-wmf;base64...)

**TDM**

En la multiplexación por división de tiempo los usuarios toman su turno en forma circular, obteniendo en cada turno todo el ancho de banda. Se utiliza el tiempo muerto entre pulsos para intercalar señales de otros canales. El proceso de modulación se ve en el siguiente esquema:

![](data:image/x-emf;base64...)

![](data:image/x-emf;base64...)

Se agregan pulsos de sincronismo al principio y fin de cada trama.

**FDM**

El espectro de frecuencias se divide entre los canales lógicos, donde cada usuario recibe una banda de frecuencia exclusiva.

Consiste en un generador de ondas portadoras separadas por un ancho de banda que crece con la jerarquía de empleo. Cada portadora se utiliza para modelar una señal de información, siendo luego transmitidas por el mismo medio. En la recepción se utilizan filtros pasa-banda para invertir este proceso.

![](data:image/png;base64...)

**Teoría De Colas**

**Punto De Saturación De Un Sistema**

El punto de saturación de un sistema es el número máximo de servidores que se pueden agregar sin que haya interferencia entre ellos. Siendo el tiempo de respuesta medio y el tiempo promedio de servicio:

![](data:image/png;base64...)

Para pocas terminales, la interferencia entre usuarios es mínima, por lo que ocasionalmente se formará cola, podemos considerar entonces que será igual a .

Cuando el número de terminales tiende a infinito, la probabilidad de tener el servidor desocupado tiende a cero, por lo que será igual a .

La intersección de las dos asíntotas se produce en . Este valor de N se llama punto de saturación.