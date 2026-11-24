1. Graficar el sistema de telecomunicaciones con sus elementos y describir cada uno.

Los sistemas de telecomunicaciones que permiten intercambiar información a distancia responder en menor o mayor medida al siguiente gráfico:

En el mismo vemos que está conformado por distintos elementos, siendo ellos:

* **Transductor de entrada y de salida**: la función de un transductor es convertir señales a fin de que el mensaje de dicha señal pueda ser entendido por el hombre. En el caso del transductor de entrada convierte una señal a eléctrica y en el caso del transductor de salida desconvierte una señal eléctrica.
* **Fuente**: es el lugar de donde parte la información.
* **Destino**: es el lugar a donde la información fue enviada.
* **Sistemas de emisión y recepción**: estos sistemas trabajan con señales eléctricas, el emisor recibe la señal eléctrica del transductor de entrada, le hace algunas modificaciones de ser necesario y la envía por el canal, donde luego el receptor la recibirá y pasará al transductor de salida.
* **Canal**: es medio por el cual viajará la señal eléctrica y quien conecta el emisor y receptor.
* **Perturbación**: es una alteración y/o molestia que se introduce al canal y afecta la señal transmitida. Las mismas pueden ser de tres tipos: distorsión, interferencia o ruido.

1. Definición de atenuación y cómo se calcula.

La **atenuación** es la relación entre la magnitud de entrada de un sistema y la salida que ella provoca.

1. Definición de Tasa de información y de dígitos y compararlas con información.

La **tasa de información o velocidad** es la cantidad de bits en promedio que se transmiten en un segundo, es decir, la cantidad de información promedio que emite/produce una fuente por unidad de tiempo.

La **tasa de dígitos** es la cantidad de dígitos que transmite una fuente por segundo.

1. Definición de los distintos tipos de perturbaciones y como se pueden eliminar.

Existen 3 tipos de perturbaciones: distorsión, interferencia y ruido.

**Distorsión**: altera la forma (amplitud) de la señal que viaja por el canal. Se puede eliminar casi en un 100%.

**Interferencia**: sucede cuando una señal con forma similar a la que se está transfiriendo por el canal se introduce al canal. Puede ser eliminada.

**Ruido:** se produce cuando una señal con comportamiento impredecible irrumpe en el canal. Este tipo de perturbación es inevitable e imposible de eliminar, lo único que se puede hacer es aumentar la calidad de la señal a transmitir para que no sea tan opacada por los ruidos.

1. Ejercicio 11 de la guía. - 6. Ejercicio de Fax de la guía.

**Información mutua:** Es la información transferida desde la fuente al receptor a través del canal.

**Palabra código**: Es una secuencia fija de símbolos.

**Capacidad**: La capacidad de un canal es la cantidad de información que puede transmitir. Se mide en bits por segundos y depende del ancho de banda y del ruido que pueda inferir en el canal.

Si la tasa de información es menor a la capacidad, entonces la señal transmitida tendrá una pequeña frecuencia para errores. Si es mayor, no es posible transmitir sin error.

**Entropía de la fuente**: es la esperanza matemática de la información por símbolo de la fuente.

**Código Bloque**: asigna a cada símbolo del código fuente S una secuencia fija de símbolos del alfabeto código Z (por ende, todas las palabras de código tienen la misma longitud). Estas secuencias fijas se denominan palabras código.

**Código no-singular:** es aquel donde todas sus palabras son distintas.

**Código Unívoco:** es aquel en el que a cualquier secuencia de palabras código le corresponde una y sólo una secuencia de símbolos de la fuente.

**Código Instantáneo:** código que puede decodificar las palabras código sin precisar el conocimiento de la próxima palabra código. Para que un código sea instantáneo, ninguna palabra código debe ser prefijo de otra palabra código.

**Código compacto**: código instantáneo que tiene la menor longitud promedio de todos los códigos instantáneos que pueden encontrarse en la misma fuente y alfabeto.

**Método de Huffman:** sirve para crear un código compacto a partir de un alfabeto n-ario. Si el alfabeto tiene r=2, los símbolos se agrupan de a 2 y cada fuente reducida tendrá un símbolo menos que la anterior. En la última reducción habrá 2 símbolos.

**Longitud media de un código**: Se define como longitud media de un código como la sumatoria de los términos $P\_{i}\*l\_{i}$ , donde $P\_{i}$ es la probabilidad de ocurrencia del símbolo y $l\_{i}$ es la longitud de su palabra código.

**Síndrome:** se define el síndrome de una palabra código como el producto del vector asociado por la matriz de control de paridad transpuesta.
Es el resultado de multiplicar una palabra con error por la matriz de control de paridad transpuesta.

Se utiliza para corregir errores. Si el síndrome es cero, ésta corresponde al grupo. Si es ≠ de cero, el mensaje tiene algún error.

En la familia de errores asociada a cada síndrome se puede n observar sólo los errores simples y dobles de las palabras códigos asociadas a ese síndrome.

**Distancia de un código**: Es la cantidad de dígitos que difieren entre una palabra código y otra palabra del mismo código.

**Cota inferior de la longitud promedio**: Expresa el límite inferior de la longitud media que es igual o mayor a la Entropía r-aria de la fuente.