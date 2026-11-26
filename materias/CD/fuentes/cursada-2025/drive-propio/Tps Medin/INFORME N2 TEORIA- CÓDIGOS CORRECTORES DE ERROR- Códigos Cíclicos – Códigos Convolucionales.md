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

**Trabajo Práctico:** Códigos correctores de error: Códigos cíclicos y códigos convolucionales

**Año:** 2024

**Índice**

[**Introducción 2**](#_r3hiaummn4gb)

[**Desarrollo 4**](#_6at6m7fnojbw)

[Códigos detectores y Códigos detectores correctores 4](#_pdgy208kj2v1)

[Distancia Hamming 6](#_hf7t8vyjdlle)

[Grado de un código detector o corrector de error 7](#_vez5ijkqd1sj)

[Códigos detectores de error 7](#_y0aacbqs05id)

[Códigos de paridad 9](#_n4khxflu6ggz)

[Códigos de peso constante 10](#_ex6u1zwqq67z)

[Por mayoría 11](#_11l9bthqd4gr)

[Repetición 11](#_z117at6njccw)

[Corrección de errores 12](#_tadecz2kqcec)

[Regla de decisión 12](#_3f31dhna8szu)

[Códigos correctores de errores 15](#_glhvgxj7149z)

[Codigo Hamming (Paridad por zonas) 18](#_xm8yek4a91mo)

[Hamming(7/4) 19](#_qjzr7xk4is3)

[Códigos Cíclicos 20](#_ay0szvw7bh8f)

[Codificación con códigos cíclicos 21](#_7ch7ck9scrxz)

[Cálculo del síndrome para detección de error 25](#_evnvz7lzvkap)

[Códigos Bose - Chaudhuri - HOCQUENQHEM (BCH) 25](#_nswqz3b8etti)

[Código Reed-Solomon 25](#_jg1iy3jmsh1e)

[Códigos Convolucionales 26](#_cpeee6ci8w98)

[Representación gráfica de los Códigos Convolucionales 27](#_6m9wmtrz7jud)

[Respuesta impulsiva y función transferencia 32](#_o49bt1wcg43q)

[Codificación: diagrama de “Trellis” 33](#_6d0t0bv18nut)

[Códigos catastróficos 35](#_ws5qpq1vuj5l)

[Decodificación de máxima probabilidad: algoritmo de Viterbi 37](#_rtji4uxsy0sm)

[Capacidad de corrección de errores 38](#_xr06qcblj3a)

[Aplicaciones de los códigos convolucionales 39](#_b21scaiq01xc)

[**Conclusión 41**](#_c8zxwep38cuc)

[**Bibliografía 42**](#_k2wg7k13obqr)

[**Anexo: Autoevaluación con Preguntas y Respuestas 43**](#_brdj9lnykq9l)

# Introducción

Quizás no resulte familiar el concepto de código corrector de error para cualquier lector del trabajo, por ello, nos parece útil dedicar la introducción a presentar conceptos básicos para poder entender el desarrollo del trabajo de manera más amena.

Garantizar la integridad y precisión de la información transmitida es crucial en lo relacionado a la comunicación de datos. Pueden producirse errores debido a una variedad de razones, como interferencias electromagnéticas, fallas en el hardware o ruido en el canal de comunicación. Las técnicas de corrección de errores se utilizan para reducir estos errores y cerciorarse de que los datos lleguen correctamente a su destino.

La familia de códigos de bloque incluye códigos cíclicos, que se distinguen por su estructura algebraica que facilita la detección y corrección de errores. Debido a su eficiencia y facilidad de implementación, estos códigos son muy utilizados. Su aplicación es notable en estándares de comunicación como Ethernet y CDMA, donde la capacidad de gestión de errores es esencial para mantener la calidad de la transmisión.

A diferencia de los códigos cíclicos, los códigos convolucionales se utilizan principalmente en sistemas de transmisión continua y funcionan sobre secuencias de datos de longitud arbitraria. En aplicaciones como las comunicaciones por satélite y la transmisión de datos en tiempo real, donde es necesario corregir errores en un flujo constante de datos, estos códigos son vitales. Las técnicas de codificación y decodificación más complejas, como el algoritmo de Viterbi, se utilizan en los códigos convolucionales para optimizar la corrección de errores en condiciones adversas.

La idea de este trabajo es analizar en detalle las características, los beneficios y las aplicaciones de los códigos correctores de error, como lo pueden ser los códigos cíclicos, convolucionales u otros. Se buscará explicar la teoría relacionada a cada tipo de código, sus esquemas de implementación y cómo ayudan a mejorar la confiabilidad de las transmisión. De esta manera, el presente trabajo tiene como objetivo obtener una comprensión completa de cómo estos códigos correctores de errores permiten, en la comunicación moderna, garantizar que la información transmitida sea recibida de manera eficiente y precisa.

# Desarrollo

## Códigos detectores y Códigos detectores correctores

Como dijimos en la introducción, es imposible asegurar que una transmisión esté exenta de errores.

Entre las razones más comunes de los errores en transmisiones podemos encontrar:

* **Interferencias Electromagnéticas (EMI)**: La presencia de señales electromagnéticas de otros dispositivos electrónicos puede inducir corrientes parásitas en el medio de transmisión, causando alteraciones en los datos transmitidos.
* **Ruido Térmico**: También conocido como ruido blanco, es generado por el movimiento térmico de los electrones en los conductores y puede provocar fluctuaciones aleatorias en la señal.
* **Distorsión de la señal**: Diferentes componentes de la señal pueden viajar a diferentes velocidades, causando una alteración en la forma de la señal original, lo que resulta en errores.
* **Ruido Impulsivo**: Picos breves y de alta energía en el medio de transmisión, a menudo causados por conmutaciones eléctricas o descargas estáticas, pueden corromper los datos.
* **Interferencias de Frecuencia**: Las señales de otras transmisiones en frecuencias cercanas pueden mezclarse con la señal original, causando errores.
* **Errores de Sincronización**: Desajustes en la sincronización entre el emisor y el receptor pueden provocar que los datos se interpreten incorrectamente.
* **Desvanecimiento (Fading)**: Variaciones en la amplitud de la señal debido a cambios en el entorno de transmisión, como el movimiento de objetos o cambios en la atmósfera, pueden causar pérdidas temporales de señal.
* **Problemas de Hardware**: Fallos en los componentes del hardware, como transceptores defectuosos, cables dañados o conectores sueltos, pueden introducir errores en la transmisión.
* **Multipath Propagation**: La recepción de múltiples versiones de la misma señal, debido a reflejos en obstáculos, puede causar interferencias y errores en la decodificación.

Podemos notar que muchos de estos errores son evitables, ya sea mejorando la calidad del hardware usado en la transmisión o asegurando que los componentes relacionados a la transmisión estén sincronizados. Sin embargo, muchos otros errores provienen de la naturaleza de las herramientas que usamos o a raíz de las condiciones climáticas que se estén atravesando durante el momento de la comunicación. Este último subconjunto de causantes resulta ser *ineludible*.

Entonces, dado que siempre va a haber posibilidad de errores en la transmisión, nos encontramos con la necesidad de solucionar los posibles errores que se generen en la comunicación, o, al menos poder detectar que la transmisión fue perjudicada.

De aquí, surgen como solución a estos errores los códigos **detectores de error** y **correctores de error**:

* Los **códigos detectores de error** consisten en incluir en los datos transmitidos, una cantidad de bits redundantes de forma que permita al receptor detectar que se ha producido un error, pero no qué tipo de error ni dónde, de forma que tenga que solicitar *retransmisión*.
* Por su parte, los **códigos correctores de error** consisten en la misma filosofía que los anteriores, incluir información redundante pero en este caso, la suficiente como para permitirle al receptor deducir cuál fue el bit que se transmitió, por lo tanto, el receptor tiene capacidad para corregir un número limitado de errores.

Antes de adentrarnos a entender íntegramente los códigos detectores y correctores de error, nos parece adecuado presentar el concepto de **distancia Hamming**. Esto se debe a que el concepto de distancia Hamming es necesario para entender a fondo la idea de los códigos detectores y correctores de error.

### Distancia Hamming

Llamamos **distancia Hamming** entre dos secuencias de binits *de mismo largo* a la cantidad de posiciones en donde sus símbolos son diferentes. Dicho de otro modo, mide la cantidad mínima de reemplazos que debemos hacer en una de las palabras para transformarla en la otra. También puede verse como, el mínimo número de errores **unitarios** que hubieran transformado una de las palabras en la otra

| *Ejemplos:*  La **distancia Hamming** entre:   * 1111 y 0010 es **3** . * 0001 y 1011 es **2** . * 111 y 10010 no es válida pues ambas secuencias de binits deben tener *el mismo largo* |
| --- |

En el caso de un alfabeto binario, y dependiendo el largo de la palabra, es posible construir figuras geométricas que nos ayudan a entender este concepto. Cada arista de las figuras representa un cambio en algún bit de la palabra. En el caso de una palabra de 3 posiciones, puede conformarse un cubo de la siguiente manera:

![](data:image/png;base64...)

Teniendo en cuenta siempre el mínimo recorrido entonces podemos observar que para llegar de, por ejemplo:

* de la palabra 010 a la palabra 111, hay que recorrer únicamente 2 aristas.
* de la palabra 100 a la palabra 011, hay que recorrer necesariamente 4 aristas.

![](data:image/png;base64...)

A partir de ahora llamaremos **distancia de un código con respecto a otro** a la **distancia Hamming**.

### Grado de un código detector o corrector de error

El concepto de **grado** de un código detector o corrector de error viene dado por la capacidad que éste tiene para detectar/corregir errores. En otras palabras, esta medida indica cuántos errores puede detectar o corregir el código sin que se pierda la funcionalidad del mensaje.

Un código con un grado más alto puede manejar más errores, lo que lo hace más robusto frente a problemas en la transmisión de datos.

| *Ejemplo:*   * Un código **detector** de errores de **grado 1** va a poder **detectar** únicamente **errores unitarios**. Es decir, errores producidos al variar un dígito en la transmisión. * Un código **corrector** de errores de **grado 3** va a poder, no solo **detectar** errores de variación de 3 binits sino que también **corregirlos**. |
| --- |

### Códigos detectores de error

Reiterando sobre esta idea, los **códigos detectores de error** son una colección de códigos cuya función principal es determinar si se ha producido o no un error en la transmisión de la palabra de código. Aunque no pueden corregirlo de inmediato, su detección evita el uso de información incorrecta. El error se soluciona repitiendo la transmisión hasta que éste desaparezca. En este caso, solo se repite el mensaje en caso de error.

No obstante, si en un código binario de longitud constante se utilizaran todas las combinaciones posibles de sus n dígitos binarios ($2^{n}$), resultaría imposible detectar si se ha producido error, ya que una combinación del código se transformaría en otra que también pertenece a él. Quiere esto decir, que la posibilidad de detectar errores se logra no utilizando todas las combinaciones posibles, de forma que al recibir una determinada combinación se puede identificar como errónea si no pertenece al código. Sin embargo, esta condición es **necesaria** pero no **suficiente**.

| *Ejemplo:*  Queremos transmitir dígitos decimales para lo que usamos el código BCD natural. En éste no se emplean más que **10** de las **16** combinaciones posibles con 4 dígitos binarios.  Supongamos que se emite la combinación 0111 y tras producirse error en un dígito binario durante la transmisión se recibe la 1111; como no pertenece al código utilizado es inmediato deducir que nunca ha podido ser transmitida, por lo que el error será detectado  Ahora, supongamos que al transmitir la combinación 0011 se produce el error en el primer dígito, recibiendo la 0010. Como también pertenece al código el centro receptor la considerará correcta, identificando, erróneamente, al dígito decimal 2 como el mensaje emitido |
| --- |

De lo expuesto es fácil deducir intuitivamente que la condición necesaria y suficiente para poder detectar error en un dígito binario es que toda combinación del código se transforme, al variar uno cualquiera de sus dígitos, en una combinación que no pertenezca al código.

![](data:image/png;base64...)

Los códigos que cumplen esta condición son aquellos cuya distancia mínima es mayor o igual a 2. Relacionando ambas afirmaciones se puede concluir que la condición necesaria y suficiente para que un código sea detector de error en un dígito binario es que su distancia mínima sea, como mínimo, dos.

Generalizando el razonamiento anterior se puede afirmar que la condición necesaria y suficiente para que un código permita detectar el error producido por la variación de un número de dígitos igual o menor que **k** durante la transmisión de la palabra de código, es que su distancia mínima sea, al menos, **k+1**.

![](data:image/png;base64...)

De los múltiples códigos detectores de error cabe destacar, de entre los detectores de un solo error, a losde **paridad** y a los de **peso constante**.

#### Códigos de paridad

Este es un criterio de detección de error que consiste en agregar a la palabra codificada un binit llamado ‘de paridad’(ip) que posee un valor obtenido al realizar el siguiente cálculo:

Si se trabaja con paridad par (bit que es 1 si la palabra es par y 0 si la palabra es impar)

$ip= i\_{1}⊕i\_{2}⊕i\_{3}⊕...⊕i\_{n}$

Siendo:

* ip : bit de paridad (impar o par).
* $⊕$: función “or exclusive”.
* n : longitud de la palabra código

Se puede trabajar tanto con paridad par como con paridad impar, aunque en este último caso se tendrá que tener el cuidado de agregar un $"+1"$ a la ecuación definida anteriormente. Quedandonos:

$ip= i\_{1}⊕i\_{2}⊕i\_{3}⊕...⊕i\_{n}+1$

Al recepcionar se controla si $ip$ cumple con el cálculo de paridad teniendo en cuenta si se utiliza paridad par o si se utiliza paridad impar. Si en el camino se produjo algún error unitario se altera la paridad de la palabra, siendo posible detectarlo en el destino.

Con este tipo de control no solo se puede llegar a detectar sino también **a corregir** empleando los chequeos de paridad horizontal y vertical. Como explicaremos en el apartado del código Hamming.

#### Códigos de peso constante

Se codifica para que la cantidad de "1s" sea igual a la cantidad de "0s".

Se puede deducir entonces que las palabras codificadas resultantes tendrán una longitud (**l**) que es par. Esto se debe a que para que el número de unos y ceros sea igual en cada palabra, la longitud de la palabra debe ser un número par. Por ejemplo, si una palabra codificada tiene una longitud de 8 bits, habrá 4 unos y 4 ceros.

En resumen, el método de igual peso en la codificación tiene como objetivo garantizar que la cantidad de unos y ceros en cada palabra codificada sea igual. Dado que cualquier discrepancia en el número de unos y ceros en la palabra recibida puede indicar un error en la transmisión, esto ayuda a proporcionar una forma de detección de errores más robusta.

| *Ejemplo:*  Si suponemos que codificamos utilizando el método de igual peso podemos obtener los siguientes códigos:  $\{ 10, 01, 0011, 0101, 1001, 1010, 1100, 000111, 001011, 010011, ...\}$ |
| --- |

#### Por mayoría

La idea principal de este enfoque es codificar los datos de tal manera que haya una diferencia significativa entre el número de unos y ceros en cada palabra.

| *Ejemplo:*  Si suponemos que codificamos con una longitud constante de 5 y peso 3 de unos:  Para poder saber cuántos códigos diferentes podemos plantear las combinaciones de 5 elementos tomados de 3:  $C\_{5}^{3}=\frac{5!}{3! ⋅ (3-5)!}=\frac{5 ⋅ 4 ⋅ 3 ⋅ 2}{3 ⋅ 4}=10$  Y si ahora nos tomamos la molestia de plantear todos los códigos posibles que cumplan con esas condiciones obtenemos los 10 códigos posibles:  $\{ 00111, 01011, 10110, 10101, 11010, 10011, 01011, 01101, 11100, 11001 \}$  Observe que si hubiéramos codificado con una longitud constante de 5 y sin limitaciones habríamos tenido $2^{5}=32$ códigos diferentes |
| --- |

Este método se usa principalmente para encontrar errores de transmisión de datos y es especialmente útil cuando se espera que ocurran errores en la comunicación. Sin embargo, **solo detecta los errores**, no los corrige.

#### Repetición

Otro código usado para detectar y corregir posibles errores unitarios se trata de la **repetición**. Consiste, en determinado un número de repetición $n$ para cada binit, repetir cada binit $n$ veces y pasar al siguiente binit. Por supuesto, la cantidad de repeticiones del mismo símbolo debe ser determinado previo a la transmisión. Si los $n$ símbolos recibidos son iguales, se supondrá que en ninguna de las transmisiones ha existido error y, por lo tanto, el centro receptor identificará como símbolo transmitido al $n$ veces repetido.

Si los $n$ símbolos recibidos no son todos iguales, implicará algún error en alguna de las transmisiones.

| *Ejemplo:*  Si suponemos un número de repetición $n=3$ , y debemos transmitir el binit $1$. La transmisión será:  $111$ |
| --- |

Sin embargo, este método se vuelve más ineficiente a medida aumentamos el número de repetición. Pues, estamos exigiendo a la transferencia enviar $n$ veces el mismo binit para poder detectar y corregir errores. Por lo que el procedimiento repetitivo descrito plantea un compromiso entre la velocidad de los mensajes y su fiabilidad. Este método de corrección de errores aunque efectivo, no es el más eficaz que se puede utilizar

### Corrección de errores

Como podemos pensar, cuando el dispositivo receptor detecta algún error, querrá encontrar una forma de corregir esos errores. Para ello, hay diversas técnicas que se pueden implementar, entre ellas, la más común es definir una **regla de decisión.**

#### Regla de decisión

Una **regla de decisión** es un conjunto de criterios que se utiliza para determinar si un mensaje recibido contiene errores y, en caso afirmativo, cuál es la corrección adecuada para esos datos. La aplicación de esta **regla de decisión** permite al receptor modificar una palabra recibida que se sabe que está incorrecta, de tal manera que adopte la forma de una *palabra sin errores*. Es importante destacar que esta modificación conlleva una cierta probabilidad de cometer un nuevo error como también de corregir el existente.

Por lo tanto, es fundamental seleccionar una Regla de Decisión que minimice esta probabilidad de error, asegurando así la integridad de la información transmitida.

| *Ejemplo:*  Si nuestros símbolos de fuentes están compuestos por un único tipo de cifra binaria, ya sea uno o cero. Nuestros códigos se verán de la siguiente manera:   | $S\_{1}$ | 111 | | --- | --- | | $S\_{2}$ | 000 |   Si sabemos que el canal tiene una probabilidad relativamente elevada debe provocar cambios unitarios y en mucho menor grado, errores de orden superior. La regla de decisión es evidente:  $Siempre que se reciba:$   * $001 se decodificara como 000$ * $110 se decodificara como 111$ * $101 se decodificara como 111$ * … |
| --- | --- | --- | --- | --- |

Ahora, podemos dar el ejemplo de un código de transmisión en el que se ha adoptado un esquema de **repetición**. Con un número de repetición $n=2$, de manera que los códigos son:

| $S\_{1}$ | 0 |
| --- | --- |
| $S\_{2}$ | 1 |

Si, por ejemplo, fuéramos el receptor y recibiéramos un mensaje como el siguiente:

$mensaje = 0 ... 1$

Podríamos dar por hecho que se ha producido un error que ha alterado la comunicación de alguna manera, ahora bien, no tendríamos forma alguna de saber el mensaje que se ha querido transmitir. Esto se debe a que podrían haber ocurrido dos situaciones:

* El mensaje originalmente contenía al código asociado a $S\_{1}$, es decir, $"1"$. De esta manera, el primer mensaje de repetición fue recibido con un error, mientras que el segundo mensaje fue recibido correctamente.
* El mensaje originalmente contenía al código asociado a $S\_{2}$, es decir, $"0"$. En consecuencia, el primer mensaje fue recibido correctamente y el segundo mensaje fue recepcionado con error.

Entonces, ¿qué hacemos?, ¿cómo resolvemos?, en este caso particular, no podemos. Inevitablemente deberemos pedir retransmisión hasta poder recepcionar de manera consecutiva dos mensajes compatibles y descubrir el mensaje que se quería enviar.

Podemos evitar este tipo de casos si ahora tuviéramos que el número de repetición es $n=3$ pues así, si recibiéramos un mensaje como el siguiente:

$mensaje = 0 ... 1 ... 0$

Nuevamente, vemos que se ha alterado uno de los tres mensajes asociados a la repetición. Sin embargo, esta vez podemos descifrar el mensaje que se ha querido transmitir originalmente. Podríamos asumir que el mensaje que se ha querido enviar ha sido el código asociado a $S\_{1}$, puesto a que la probabilidad de que se produzcan dos errores en la comunicación es considerablemente inferior a que se haya producido un solo error.

Esta asunción que realizamos podría formalizarse como una **regla de decisión** en la comunicación que estamos realizando, aclarandole al receptor que:

* Si recepciona dos mensajes relacionados a un código y uno diferente, se decodificara por el mensaje del que se haya recibido la mayoría.

De esta forma, adoptando **reglas de decisión**, podemos agregar a la capacidad detectar errores del receptor, la posibilidad de corregir mensajes.

| *Ejemplo:*  Consideremos un canal BSC con una probabilidad de error de 0.01, lo que significa que el 99% de los símbolos binarios transmitidos se reciben correctamente. Para mejorar la confiabilidad del canal, repetimos **tres** veces el envío de cada dígito binario. El siguiente esquema de emisión-transmisión de un dígito binario muestra el proceso:  ![](data:image/png;base64...)  Para este caso:   * La probabilidad de que no exista error en la transmisión es:$ (1 - p)^{3} = ( \overline{p} )^{3}$ * La probabilidad de un solo error es: $3⋅(p⋅(\overline{p})^{2})$ * La probabilidad de 2 errores es: $3⋅(p^{2}⋅\overline{p})$ * Y la probabilidad de que los tres símbolos binarios recibidos sean erróneos es: $p^{3}$   Si pensamos en la **regla de decisión** correcta, un símbolo será erróneamente interpretado en los casos que se produzcan 2 o 3 errores. Por ende, debemos sumar las probabilidades de que varíen 2 o 3 símbolos:  $3⋅(p^{2}⋅\overline{p})+p^{3}≃3⋅10^{-4}$  La probabilidad de error ha pasado de $p=10^{-2}$ si no existe repetición en la transmisión a $3⋅10^{-4}$ si repetimos 3 veces cada símbolo emitido. |
| --- |

### Códigos correctores de errores

Estos códigos añaden a la capacidad de detectar el error, la posibilidad de corregirlo sin necesidad de repetir la transmisión. De forma general, se puede decir que la técnica empleada para la corrección consiste en identificar como combinación correcta, a la perteneciente al código que sea más cercana a la errónea recibida, o sea, aquella cuya distancia de la combinación incorrecta sea menor.

![](data:image/png;base64...)

Como también es necesario detectar el error, no deben de usarse todas las combinaciones posibles (como se vio en el apartado de códigos detectores de error), pero, además, como el proceso de corrección ha de ser no ambiguo, sólo debe de haber una posible combinación del código que diste una unidad de cada combinación no usada.

Se puede concluir, que la condición **necesaria y suficiente** para que un código sea corrector de **orden uno** es que su distancia mínima sea **tres**.

| *Ejemplo:*  Queremos transmitir dos mensajes: **S1** y **S2**.  Si la distancia mínima del código usado es *menos que tres*, es imposible una corrección no ambigua. El código usado podría ser   | $S\_{1}$ | 00 | | --- | --- | | $S\_{2}$ | 11 |   Supongamos que usando este código se recibe la combinación 01, evidentemente ha existido un error, y suponiendo que ha sido en un solo dígito es imposible discernir si la combinación enviada ha sido la 00 o la 11 ya que ambas distan una unidad de la recibida.  Creemos ahora un código de distancia mínima tres. En este caso el código nos quedaría:   | $S\_{1}$ | 000 | | --- | --- | | $S\_{2}$ | 111 |   Las entradas y salidas del canal serían (suponiendo que no puede haber más de un error en la transmisión de cada combinación):  ![](data:image/png;base64...)  Es inmediato ver como en el proceso de corrección no existe ninguna ambigüedad:  ![](data:image/png;base64...) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Aunque la restricción de que no existe más de un error en la transmisión de cada combinación aplicable en numerosos canales reales, es conveniente generalizar el proceso de corrección a un **orden k**.

Si durante la transmisión de una combinación varían un número de dígitos **igual o inferior a k**, se recibirá una combinación no perteneciente al código; para que este error pueda ser corregido, debe de cumplirse que la combinación emitida sea la única perteneciente al código cuya distancia de la recibida sea igual o inferior a **k**.

Se puede llegar a la conclusión, generalizando el razonamiento a cualquier combinación transmitida, que la condición necesaria y suficiente para que un código sea corrector de **orden k** es que su distancia mínima sea de **2k+1**. Solo en este caso, el proceso de corrección será no ambiguo.

![](data:image/png;base64...)

#### Codigo Hamming (Paridad por zonas)

El código Hamming es un código que, además de la detección, permite la corrección de errores a través de la utilización de bits de paridad que permiten triangular que binit fue el culpable del error para así poder corregirlo.

Para ello, el código Hamming aplica una cierta estrategia a la hora de decidir que rol cumplirá cada bit de paridad de manera que tenga ciertas características que permiten detectar y corregir errores. Como dijimos, este código utiliza control de paridad, pero no sobre la palabra completa que se va a transmitir, sino por grupos de bits.

Todos los códigos pueden ser transformados en códigos Hamming que permitan la detección y corrección de errores. No obstante, veremos el código Hamming relacionado a una palabra de 7 binits con 4 bits de paridad, más comúnmente referido como **Hamming(7,4)**:

##### Hamming(7/4)

Este código se trata de un código que codifica cuatro bits de información en siete bits, agregando tres bits de paridad.![](data:image/png;base64...)

El beneficio de este código es que permite detectar y corregir cualquier error unitario y detectar errores de dos bits. Dicho de otra forma, la mínima distancia de Hamming entre dos códigos correctos es de 3, y la mayoría de palabras recibidas puede ser decodificada correctamente si están como máximo a una distancia del código transmitido por el emisor.

Los mensajes son distribuidos de la siguiente manera:

$d\_{1}, d\_{2}, d\_{3}, d\_{4}, p\_{1}, p\_{2}, p\_{3}$

¿Cómo se procede a desglosar el mensaje y entender los bits de paridad?

La idea es obtener los bits de paridad y haber predeterminado el rol de cada bit de paridad para la transmisión, en el caso del código **Hamming(7,4)** cada bit de paridad siempre estará relacionado a tres bits de información. Por ejemplo:

* $p\_{1}$ cubre $d\_{1}$, $d\_{2}$ y $d\_{4}$. Es decir, $p\_{1}=d\_{1}⊕d\_{2}⊕d\_{4}$
* $p\_{2}$ cubre $d\_{1}$, $d\_{3}$ y $d\_{4}$. Es decir, $p\_{2}=d\_{1}⊕d\_{3}⊕d\_{4}$
* $p\_{3}$ cubre $d\_{2}$, $d\_{3}$ y $d\_{4}$. Es decir, $p\_{3}=d\_{2}⊕d\_{3}⊕d\_{4}$

Podemos determinar si ha ocurrido un error al calcular la paridad de cada conjunto de bits (tanto los bits de paridad como los bits de datos) y, si es así, en qué posición. De esta manera, podemos determinar qué bits causaron el error observando cuál paridad no coincide con el resto. Si se eligen correctamente los bits de paridad, se pueden detectar y corregir todos los errores con una **distancia Hamming de 1**.

De manera que es un código muy efectivo para transmisiones más propensas a tener errores unitarios y no tantos errores de mayor orden. El medio debería tener mucho ruido para que se produjeran errores de mayores órdenes y/o ráfagas de errores.

## Códigos Cíclicos

Se dice que un **código** es un **código de bloque** cuando sus palabras códigos tienen **longitud constante** ($l\_{i} = n$ para todo $i$). El código bloque admite una estructura algebraica de grupo y de espacio vectorial. En este caso, los elementos del código bloque son vectores que se corresponden a las palabras código.

Ahora bien, sabemos que todo *subespacio vectorial* del espacio vectorial asociado a un código en bloque constituye un **código lineal**. Si el código en bloque del cual proviene el subespacio es binario entonces a todo código de bloque proveniente de su subespacio le llamaremos **Código de grupo**.

Entonces, habiendo recordado tales definiciones, nos centraremos exclusivamente en los **códigos cíclicos**.

Los **códigos cíclicos** son una subclase de los códigos de bloque lineales (códigos de grupo), los cuales poseen un esquema de decodificación eficiente, es decir que pueden ser decodificados mediante el uso de algoritmos relativamente simples. Se dice que un código es cíclico cuando cualquier desplazamiento en lazo cerrado de una palabra-código da como resultado otra palabra-código existente dentro del conjunto empleado para codificar los posibles mensajes. Es más sencillo comprender esta propiedad mediante el uso de un ejemplo:

Supongamos que tenemos una palabra código ‘a’ = 100100. Si ‘a’ es una palabra perteneciente a un código cíclico entonces se darán las siguientes propiedades:

* Si desplazamos ‘a’ hacia la izquierda:

![](data:image/png;base64...)

Donde 001001 es una palabra perteneciente al código cíclico (Llamémosle ‘b’)

* Si desplazamos ‘a’ hacia la derecha:

![](data:image/png;base64...)

Donde 010010 es una palabra perteneciente al código cíclico (Llamémosle ‘c’)

Por lo tanto podemos decir que un código es cíclico si y sólo si para todo ‘a’ perteneciente al código y conformado a1, a2, …, an caracteres (En el caso del ejemplo, a6 pues nuestros códigos están conformados por 6 caracteres binarios) existen palabras ‘b’ y ‘c’ pertenecientes al código tal que:

b1  = a0, b2 = a1, …, bn = an - 1, b0 = an

c0  = a1, c1 = a2, …, cn - 1 = an, cn = a0

En términos matemáticos: Un subconjunto S de Fqn es cıclico si (an−1, a0, , . . . , an−2) ∈ S siempre que (a0, a1, . . . , an−1) ∈ S. Un código lineal C es llamado código cíclico si C es un conjunto cíclico. Se dice que la palabra (un−r, . . . , un−1, u0, u1, . . . , un−r−1) se obtiene a partir de la palabra (u0, u1, . . . , un−1) ∈ Fqn desplazando cíclicamente ‘r’ posiciones.

Polinomio generador

Un código cíclico (n, r) es especificado por un conjunto de polinomios de palabra-código de grado n - 1 o menos, el cual contiene un polinomio de grado mínimo n-k como un factor. Este factor especial, denotado por g(x) es seleccionado como el Polinomio Generador del código.

### Codificación con códigos cíclicos

Existen dos formas principales de codificar códigos cíclicos:

**Codificación no sistemática**

De forma análoga al trabajo realizado con los códigos lineales, un mensaje *m* ∈ Fqn-r, es decir, cuando se encuentra en su forma vectorial, se codifica como la palabra código C = *m*G ∈ Fqn, donde G es la matriz generadora para C.

**Codificación sistemática**

Para definir una codificación sistemática, vamos a hacer uso del carácter polinómico de los códigos cíclicos ya que, para permitirnos codificar sistemáticamente dichos códigos, necesariamente debemos escribir las cadenas mensaje del código en términos polinomiales.

Dado un mensaje fuente a = a1, a2, …, an-r-1 ∈ Fqn-r, se forma el polinomio mensaje

a\*(x) = a0xn-1 + a1xn-2+ … + an-r-1xr

De esta manera, se ha formado el polinomio a\*(x), el cual no tiene términos de grado menor que r. El paso siguiente consiste en dividir a a\*(x) por g(x) (polinomio generador de a):

a\*(x) = q(x)g(x) + s(x) con s(x) = 0 o grad [s(x)] < r

*(Donde s(x) es el síndrome de a(x))*

De esta manera llegamos a que la codificación de a\* es

c(x) = a\*(x) - s(x) = q(x)g(x)

**Ejemplo:**

Consideremos un $[8,2]$-código sobre $F\_{3}$, generado por $g(x)=(x^{2}+1)(x^{2}+x+2)(x^{2}+2x+2)=x^{6}+x^{4}+x^{2}+1$.

Este código, capaz de codificar 9 mensajes de longitud 2, codifica el conjunto de información $F\_{3}^{2}=\{00, 10, 01, 20, 02, 12, 21, 11, 22\}$. La información se almacena en las primeras $n-r=8-6=2$ coordenadas, mientras que las 6 restantes son símbolos de redundancia.

Para una mejor comprensión, primero vamos a construir el código del que partimos. Para encontrar todos los códigos cíclicos de longitud 8 sobre $F\_{3}$ debemos factorizar el polinomio $x^{8}-1 ϵ F\_{3}(x)$ de la siguiente manera:

$x^{8}-1=(x+2)(x+1)(x^{2}+1)(x^{2}+x+2)(x^{2}+2x+2)$

De estos factores, podemos construir el generador del $[8,2]$-código usando la combinación de todos menos uno de los factores, asegurando que el producto sea de grado 6:

$g(x)=(x^{2}+1)(x^{2}+x+2)(x^{2}+2x+2)=x^{6}+x^{4}+x^{2}+1$

A continuación, se presentan los polinomios mensaje con sus sus respectivos cocientes y residuos, obteniendo a partir del algoritmo de la división:

$00 = a\_{1}(x)=0=(x^{6}+x^{4}+x^{2}+1)(0)+0,$

$10=a\_{2}(x)=x^{7}=(x^{6}+x^{4}+x^{2}+1)(x)+(2x^{5}+2x^{3}+2x),$

$01=a\_{3}(x)=x^{6}=(x^{6}+x^{4}+x^{2}+1)(1)+(2x^{4}+2x^{2}+2),$

$20=a\_{4}(x)=2x^{7}=(x^{6}+x^{4}+x^{2}+1)(2x)+(x^{5}+x^{3}+x),$

$02=a\_{5}(x)=2x^{6}=(x^{6}+x^{4}+x^{2}+1)(2)+(x^{4}+x^{2}+1),$

$12=a\_{6}(x)=x^{7}+2x^{6}=(x^{6}+x^{4}+x^{2}+1)(x+2)+(2x^{5}+x^{4}+2x^{3}+x^{2}+2x+1),$

$21=a\_{7}(x)=2x^{7}+x^{6}=(x^{6}+x^{4}+x^{2}+1)(2x+1)+(x^{5}+2x^{4}+x^{3}+2x^{2}+x+2).$

Así, la codificación final $c\_{i}(x)=a\_{i}(x)-r\_{i}(x)$ para cada $a\_{i}$ es la siguiente:

$00 = a\_{1}(x)\rightarrow c\_{1}(x)=0,$

$10 = a\_{2}(x)\rightarrow c\_{2}(x)=x^{7}+x^{5}+x^{3}+x,$

$01 = a\_{3}(x)\rightarrow c\_{3}(x)=x^{6}+x^{4}+x^{2}+1,$

$20= a\_{4}(x)\rightarrow c\_{4}(x)=2x^{7}+2x^{5}+2x^{3}+2x,$

$02= a\_{5}(x)\rightarrow c\_{5}(x)=2x^{6}+2x^{4}+2x^{2}+2,$

$12= a\_{6}(x)\rightarrow c\_{6}(x)=x^{7}+2x^{6}+x^{5}+2x^{4}+x^{3}+2x^{2}+x+2,$

$21= a\_{7}(x)\rightarrow c\_{7}(x)=2x^{7}+x^{6}+2x^{5}+x^{4}+2x^{3}+x^{2}+2x+1,$

$11= a\_{8}(x)\rightarrow c\_{8}(x)=x^{7}+x^{6}+x^{5}+x^{4}+x^{3}+x^{2}+x+1,$

$22= a\_{9}(x)\rightarrow c\_{9}(x)=2x^{7}+2x^{6}+2x^{5}+2x^{4}+2x^{3}+2x^{2}+2x+2.$

La codificación de la información se realiza de la siguiente manera:

$00 \rightarrow c\_{1}(x)=00000000,$

$10\rightarrow c\_{2}(x)=10101010,$

$01\rightarrow c\_{3}(x)=01010101,$

$20\rightarrow c\_{4}(x)=20202020,$

$02\rightarrow c\_{5}(x)=02020202,$

$12\rightarrow c\_{6}(x)=12121212,$

$21\rightarrow c\_{7}(x)=21212121,$

$11\rightarrow c\_{8}(x)=11111111,$

$22\rightarrow c\_{9}(x)=22222222.$

Es evidente que el proceso de codificación anterior es complejo de realizar manualmente cuando aumenta el tamaño del conjunto de mensajes, debido al esfuerzo y tiempo que requiere. Para simplificar y comprender mejor este proceso, se puede utilizar una herramienta informática como el software SAGE, que facilita la codificación de manera eficiente.

### Cálculo del síndrome para detección de error

Considerando que la palabra-código recibida con error sea $Y(D)=y\_{0}+y\_{1}D, ...,+y\_{n-1}D^{n-1}$, el polinomio del síndrome se obtiene con el residuo de la división del polinomio de la palabra-código entre el polinomio generador $g(D)$.

$\frac{Y(D)}{g(D)}=q(D)+\frac{s(D)}{g(D)} $, donde q es el cociente y s es el síndrome.

De manera similar al código Hamming, con el síndrome y el patrón de errores se hace la detección del error o los errores y su posición dentro de la palabra-código.

### Códigos Bose - Chaudhuri - HOCQUENQHEM (BCH)

Es un código cíclico con una gran variedad de parámetros. Para $m\geq 3 y t<(2m-1)/2$ existen códigos BCH con los siguientes parámetros:

Para tamaños de unos pocos cientos de bits o menos, los códigos BCH son los mejores para un mismo tamaño de bloque e índice de código (relación entre el bloque de entrada y el bloque de salida).

Las características principales se resumen básicamente en que el código obtenido va a ser sistemático, sin ser alterados por los bits de paridad; y además con el BCH es posible detectar y corregir más de un error, en lugar de uno sólo como en los códigos Hamming.

### Código Reed-Solomon

Un código Reed Solomon (RS) es una subclase de los códigos BCH no binarios. Se distingue de los códigos binarios porque éste opera con símbolos de *b* bits cada uno en lugar de bits individuales. Es útil cuando los errores ocurren en ráfagas, como en los sistemas de grabación de discos compactos digitales.

![](data:image/png;base64...)

El código obtenido mediante un código RS es sistemático, sin ser la palabra-código alterada por los símbolos de paridad. Dependiendo del ejemplo, es posible detectar y corregir sólo un símbolo de error.

## Códigos Convolucionales

Los códigos convolucionales fueron introducidos en 1955, son códigos lineales al igual que los códigos bloque (como los códigos de Hamming, por ejemplo) y es por esto que se utilizan para garantizar la integridad de la información por medio de agregar redundancia a la misma, logrando que las palabras del código tengan la distancia mínima necesaria. Son ampliamente utilizados en enlaces de radio de línea de vista y en comunicaciones móviles, tal como telefonía celular.

![](data:image/png;base64...)

Lo que diferencia a los códigos convolucionales de los códigos lineales que ya hemos visto es que estos códigos no solo se generan a partir de la información transmitida en un momento determinado, sino que los mismos cuentan con acceso a información que ya ha sido transmitida anteriormente, es decir que, los códigos convolucionales se destacan principalmente por su capacidad de **memoria**.

Profundizando estas definiciones, podemos decir que los códigos convolucionales son un tipo de códigos correctores de errores caracterizados por la terna (*n, m, k*). Donde ‘*n*’ es el número de entradas al codificador, ‘*m*’ es el número de salidas y ‘*k*’ la profundidad del código. Las salidas del código convolucional serán definidas por la entrada actual y las *k* − 1 entradas previas (Capacidad de memoria del código convolucional).

En general ‘*n*’ y ‘*m*’ son enteros pequeños con *n < m*, por otro lado, la memoria ‘*k*’ debe ser lo suficientemente amplia para poder lograr alcanzar bajas probabilidades de error, pero no excesivamente grande como para requerir un nivel significativo de procesamiento en el decodificador.

A partir de esta definición más detallada, definiremos el concepto de **tasa de código** como la relación entre el número de entradas y el número de salidas *n / m.* Esta tasa nos indica que la proporción de bits efectivos de información que serán transmitidos sin tomar en cuenta la redundancia.

### Representación gráfica de los Códigos Convolucionales

Veremos 3 formas principales de representar gráficamente un código convolucional:

**Diagramas de Conexiones**

En el siguiente diagrama de conexiones representamos un código convolucional (1, 2, 4) es decir: 1 entrada, 2 salidas y 4 como longitud de memoria:

**![](data:image/png;base64...)**

* *‘u’* es la entrada
* V1 y V2 son las salidas, dichas salidas están determinadas por una suma mod-2[[1]](#footnote-0) y el valor de las entradas ingresadas anteriormente.

Otra forma de representar un diagrama de conexiones es:

![](data:image/png;base64...)

Como la suma mod-2 es una operación lineal, estos códigos pueden ser vistos como sistemas lineales, es decir, podemos encontrar una matriz **G** tal que la salida **v** sea lograda a partir de la entrada ***‘u’*** según

**v = uG**

En los diagramas de conexión vistos anteriormente, los bits de la secuencia *‘u’* van entrando uno a uno y se van obteniendo las salidas V1 y V2. La primera salida se obtiene de la suma mod-2 del bit entrante con los bits en t − 2 y t − 3. La segunda salida se obtiene de la suma mod-2 del bit entrante con los bits en t − 1, t − 2 y t − 3. Finalmente, V1 y V2 se multiplexan[[2]](#footnote-1) logrando un único flujo de salida.

Si a la entrada colocamos una delta de Kronecker[[3]](#footnote-2), por ejemplo. u = (1, 0, 0, . . . ), y observamos las salidas, obtendremos las respuestas al impulso h1 = (1, 0, 1, 1) y h2 = (1, 1, 1, 1) correspondientes a las salidas V1 y V2 respectivamente. Y como el sistema es lineal, se cumple que:

**V1 = u \* h1**

**V2 = u \* h2**

Luego, no es difícil ver cómo para este código convolucional (1, 2, 4) la matriz G de la ecuación se logra según

![](data:image/png;base64...)

Finalmente, en cualquier sistema lineal, operaciones en el dominio del tiempo que involucran convoluciones pueden ser reemplazadas por operaciones en cierto espacio de transformación que involucran operaciones con polinomios. En particular, aplicando la Transformada-Z a la ecuación vista anteriormente obtenemos que

$V\_{1}(Z) = U(Z)H\_{1}= U(Z) X (1 + Z^{-2} + Z^{-3})$

$V\_{2}(Z) = U(Z)H\_{2}= U(Z) X (1 +Z^{-1} + Z^{-2} + Z^{-3})$

donde todas las operaciones son mod-2 y

$U(Z) = u\_{0} + u\_{1}Z^{-1} + u\_{2}Z^{-2} + . . . ;$

la multiplexación de ambas salidas en un único flujo se obtiene según

$V(Z) = V\_{1}(Z^{2}) + Z^{-1}V\_{2}(Z^{2})$

Nótese que el evaluar tanto a V1 como a V2 en Z2 y no en Z sugiere que al multiplexar ambas salidas lo que se está haciendo es un cambio en la tasa de bits, un sobre muestreo racional igual *m/n*.

Todo lo presentado hasta este punto puede ser extendido a códigos con diferente número de entradas *n*, diferente número de salidas *m*, diferente cantidad de registros de memoria *k − 1* y diferente diagrama de conexión.

**Diagrama de estados**

Dado que un codificador convolucional es un circuito secuencial, su operación puede ser descrita por un diagrama de estados. El estado del codificador es definido por el contenido de sus registros de desplazamiento, y, en función del valor de la entrada, podremos saber el valor del próximo estado. El diagrama de estados del codificador convolucional (1, 2, 4) con el que venimos trabajando es el siguiente:![](data:image/png;base64...)

Los estados son etiquetados según $S\_{0}, S\_{1}, . . . , S\_{2^{(k - 1)^{n}}- 1}$. donde *k − 1* representa el número de registros de desplazamiento. Las flechas que llevan de un estado a otro en el diagrama de estados dan información de la entrada necesaria para tomar ese camino dado el estado presente, y de los dos bits de salida una vez llevada a cabo la transición. Asumiendo que el estado inicial del diagrama es con todos sus registros en cero (S0), es posible obtener la palabra de código correspondiente a cualquier secuencia de entrada u simplemente recorriendo el diagrama de estados.

**Puncturing**

El puncturing es una técnica empleada en la transmisión de códigos para lograr tasas *n / m* sin aumentar la complejidad en la decodificación en el receptor. Consiste en codificar las palabras con un codificador de menor complejidad, llamado "madre", que tiene una sola entrada y varias salidas (denominadas *mmadre*​); por lo tanto, tiene una tasa de *1 / mmadre*. Luego, se eliminan ciertos bits codificados para alcanzar la tasa deseada del código. Tanto el codificador como el decodificador conocen (Y deben conocer para que el método en sí sea aplicable) qué bits no se transmiten, ya que posteriormente se utiliza una matriz de puncturing que indica qué bits se deben desechar. La información descartada se agrega en el receptor como bits "dummy" y luego se "corrige" utilizando el algoritmo de decodificación. La ventaja del puncturing es que la decodificación del nuevo código es idéntica a la del código madre que, como mencionamos anteriormente, es un código cuya complejidad de codificación es notablemente menor al código original, lo que justamente hace mucho más simple su posterior decodificación.

Por ejemplo, las matrices mostradas debajo son algunas de las más comúnmente utilizadas y están definidas en el estándar de televisión digital terrestre ISDB-T. Para cada salida V1 y V2​, los ceros representan bits descartados y los unos representan bits transmitidos. En la columna de la derecha de la tabla se muestra la secuencia final transmitida.

![](data:image/png;base64...)

### Respuesta impulsiva y función transferencia

Desde el punto de vista de la teoría de señales y sistemas, un codificador convolucional es un sistema lineal e invariante en el tiempo (LTI), discreto y con memoria. Por este motivo, el código de salida $y(t)$ del codificador cumple la expresión:

$y(t) = x(t) \* h(t)$

donde $ x(t)$ son los *k* bits de entrada, $h(t)$ es la **respuesta impulsiva** del sistema y la operación “$\*$” representa la ***convolución*** temporal de ambos. De ahí que el código generado por el sistema reciba el nombre de convolucional.

La teoría de sistemas también nos enseña que la igualdad anterior puede expresarse en la forma transformada, en este caso aplicando la transformada $z$ por ser un sistema discreto, obteniendo:

$Y(z) = X(z).H(z)$ o lo que es lo mismo: $H(z)=\frac{Y(z)}{X(z)}$

donde $H(z)$ recibe el nombre de **función transferencia** del sistema.

La respuesta impulsiva se puede hallar fácilmente sin más que ver cuál es la secuencia de salida cuando introducimos un impulso unidad en la entrada.

El impulso unidad está formado por una cadena de *k* bits en la que todos son ceros menos el primero que ha de ser un uno. Dado que el codificador parte del estado **0 0 0 … 0**, es preciso completar la cadena anterior con los $(L-1).k$ ceros necesarios para dejar la memoria del codificador en el estado inicial.

Observemos estos conceptos para el caso particular de un codificador [2, 1, 3] de ejemplo.

El impulso unidad es la cadena (**1 0 0**), la cual al ser introducida en el diagrama de estados, produce la transición de estados $00\rightarrow 10\rightarrow 01\rightarrow 00$ que genera la secuencia de salida (**11 01 11**).

La respuesta impulsiva también se puede obtener a partir de las secuencias generadoras $g\_{1}=$ (**1 0 1**) y $g\_{2}=$ (**1 1 1**), alternando un bit de $g\_{1}$ con un bit de $g\_{2}$.

Para hallar la función transferencia, solo basta con aplicar la transformada $z$ a cada una de las salidas del sistema.

$y\_{1}(t)=x(t)+x(t-2)\rightarrow Y\_{1}(z)=X(z)+z^{-2}.X(z)$

$y\_{2}(t)=x(t)+x(t-1)+x(t-2)\rightarrow Y\_{2}(z)=X(z)+z^{-1}.X(z)+z^{-2}.X(z)$

Por tanto, para cada salida obtenemos la función transferencia:

$H\_{1}(z)=1+z^{-2}=\frac{z^{2}+1}{z^{2}}$

$H\_{2}(z)=1+z^{-1}+z^{-2}=\frac{z^{2}+z+1}{z^{2}}$

### Codificación: diagrama de “Trellis”

El diagrama de estados proporciona una buena información sobre las distintas transiciones de la máquina de estados del codificador, pero no permite ver la evolución de dichas transiciones ni sus salidas asociadas con el paso del tiempo, es decir, a medida que van llegando cadenas de *k* bits al codificador.

Por este motivo, en los códigos convolucionales se suele utilizar el denominado diagrama de Trellis que sí permite ver la evolución temporal.

Siguiendo con el ejemplo del codificador convolucional [2, 1, 3], el diagrama de Trellis del mismo se vería algo así:

![](data:image/png;base64...)

En dicho diagrama, las flechas con trazo continuo representan un cero en la entrada del codificador mientras que las flechas con trazo discontinuo representan la entrada de un uno. Junto a las flechas se indica la salida del codificador correspondiente a cada entrada, y la dirección de las flechas indica los estados inicial y final de cada transición.

La codificación de una cadena de entrada conlleva un camino concreto en el diagrama de Trellis que determina la secuencia de salida y las transiciones entre estados. Así, la codificación de la cadena $k=$**(1 1 0 0)** da como resultado el camino siguiente en el diagrama Trellis, cuya secuencia de salida es la palabra código $n=$**(11 10 10 11).**

**![](data:image/png;base64...)**

Aquel camino que partiendo del estado inicial **0 0 0 … 0** regresa a dicho estado con el menor número de unos en la secuencia de salida, determina lo que se denomina la distancia libre del código ($d\_{free}$), la cual es igual al número de unos de dicha secuencia, esto es, el peso Hamming de la misma.

La distancia libre de un código convolucional es similar a la distancia Hamming de un código bloque y, por tanto, se puede demostrar que $d\_{free}$ representa la mínima de las distancias de dos palabras código cualesquiera.

Así, a la vista del diagrama de Trellis de nuestro ejemplo, se constata que la distancia libre queda determinada por el camino $00\rightarrow 10\rightarrow 01\rightarrow 00$ el cual genera la secuencia de salida (**11 01 11**). Por tanto, en nuestro ejemplo $d\_{free}=5$.

### Códigos catastróficos

Todo código convolucional debe mapear una cadena de bits de entrada, normalmente larga, en palabras de código con el fin de proporcionar un mayor nivel de protección frente al ruido, que puede introducir el canal de transmisión o el soporte de almacenamiento que se utilice. Obviamente, no es deseable que el codificador traduzca cadenas de información distintas en secuencias de código parecidas ya que éstas podrían confundirse en la decodificación, provocando un aumento en los bits de información erróneos.

El peor caso lo tendríamos si dos cadenas de entrada que difieren en infinitos bits son mapeadas en dos secuencias de código que difieren en unos pocos bits, ya que con un código así, existe una alta probabilidad de decodificar erróneamente las palabras código, provocando un número infinito de errores en los bits de información.

Un código que se comporta de dicha manera se dice que es un código catastrófico y, si bien puede tener interés matemático, en la práctica se debe evitar su uso. Veámoslo con un ejemplo.

La siguiente figura muestra el esquema y el diagrama de estados de un codificador convolucional cuyas secuencias generadoras son g1 = (**1 1 0**), g2 = (**0 1 1**)

![](data:image/png;base64...)

Se observa que los bucles de los estados 00 y 11 generan la misma secuencia en la salida del codificador. Así, la cadena de entrada k = (11111111 … 1100) genera el código de salida n = (10 01 00 00 00 00 00 … 00 00 10 01) que tiene una distancia Hamming igual a 4 con respecto al código asociado a otra cadena de entrada con todo ceros.

Por tanto, tenemos dos entradas cuya distancia tiende a infinito mientras que los respectivos códigos de salida están a una distancia fija de tan sólo 4 bits. Es evidente que dichos códigos podrían confundirse en la decodificación si aparecen errores en unos pocos bits.

### Decodificación de máxima probabilidad: algoritmo de Viterbi

La memoria de un codificador convolucional funciona como una máquina de estados que cambia de un estado a otro a medida que llegan los bits a codificar. Se puede demostrar que la secuencia de estados forma una cadena de Markov[[4]](#footnote-3) oculta de orden (L-1)·k, lo que significa que en la salida del codificador no se entregan los valores de los estados, sino los bits que dependen de ellos.

Esto permite deducir la secuencia de estados más probable si se conoce previamente el diagrama de estados, observando únicamente la secuencia de salida del codificador con el paso del tiempo. Existen varias técnicas para esto, pero la más sencilla de implementar es el algoritmo de Viterbi.

Un decodificador que utiliza el algoritmo de Viterbi almacena la secuencia de bits que recibe y calcula la secuencia de estados más probable mediante los caminos en el diagrama de Trellis que tienen menor distancia acumulada. Por cada grupo de bits recibidos, se calcula la distancia entre la secuencia recibida y la correspondiente a cada transición en el diagrama de Trellis, descartando las transiciones con mayor distancia acumulada.

El algoritmo termina cuando se encuentra el camino que lleva al estado inicial (todo ceros) con la menor distancia acumulada. Una vez deducido este camino en el diagrama de Trellis, se puede obtener la cadena de bits de información asociada a las transiciones sucesivas.

El algoritmo de Viterbi puede utilizar dos tipos de distancias: la distancia euclidiana para la decodificación con decisión blanda o la distancia de Hamming para la decodificación con decisión dura. Ambas distancias son útiles en diferentes contextos (Canales digitales de paso banda y de banda base respectivamente). A continuación, se muestra un ejemplo de decodificación dura usando el algoritmo de Viterbi.

Dado un codificador convolucional [2,1,3] y una secuencia de código recibida r = (01 10 11 11 01 00 01), que consta de 14 bits, la cadena de información decodificada tendrá 7 bits, requiriendo 7 transiciones de estado para finalizar la decodificación. Además, la cadena de información decodificada termina con ceros de relleno (L-1)·k, lo que en este caso significa que las dos últimas transiciones deben corresponder a ceros de información para terminar en el estado inicial 00. El siguiente diagrama de Trellis resume en forma concisa este proceso de decodificación:

![](data:image/png;base64...)

### Capacidad de corrección de errores

De la misma manera que en un código de bloque la capacidad de corrección de errores viene determinada por la distancia Hamming del código, en un código convolucional es la distancia libre $d\_{free}$ la que determina la capacidad de corrección de errores.

Todo código convolucional es capaz de corregir $(d\_{free}-1)/2$ errores por cada $n.L$ bits de código. Así, nuestro código convolucional [2,1,3] ejemplo es capaz de corregir 2 errores por cada 6 bits de código, dado que $d\_{free}=5$. Eso significa que si transmitimos nuestro código por un canal BSC cuya probabilidad de error es $p=10^{-3}$, la probabilidad de error de bit ($P\_{eb}$) después de decodificar será siempre inferior a la probabilidad de que ocurran 2 errores por cada 6 bits en dicho canal, es decir:

![](data:image/png;base64...)

Sin embargo, el propio algoritmo de Viterbi reduce dicha tasa de error ya que, según se puede demostrar, con decodificación dura y para valores pequeños de $p$ ($10^{-2} $o inferior) $P\_{eb}$ es aproximadamente:

$P\_{eb}\leq \frac{1}{k}(2\sqrt{p})^{d\_{free}}$

Por lo tanto, particularizando dicha expresión para el código ejemplo y utilizando el canal BSC anterior, resulta:

$P\_{eb}\leq (2\sqrt{10^{-3}})^{5}=32.10^{-15/2}=1,012.10^{-6}$

Cabe destacar con este ejemplo, cómo un código convolucional sencillo permite utilizar un canal BSC de mala calidad, obteniendo una tasa de error aceptable.

### Aplicaciones de los códigos convolucionales

Los códigos convolucionales se utilizan comúnmente como códigos de canal para corregir errores en canales ruidosos, ya sea debido a limitaciones de potencia (típico en los canales digitales banda base) o a limitaciones en banda (propias de los canales digitales paso banda).

En algunas aplicaciones, se combinan con otros códigos, como Reed-Solomon, donde este último actúa como código exterior y el código convolucional como el código interior del canal. Esta combinación se prefiere para obtener una mayor capacidad de corrección de errores, en lugar de utilizar un código convolucional con mayor distancia libre, debido a la simplicidad del decodificador.

Además, se encuentran en sistemas audiovisuales que requieren corrección de errores en tiempo real, como los estándares de televisión digital por satélite (DVB-S), por cable (DVB-C) y terrestre (DVB-T), así como en algunos estándares de telefonía móvil como GSM. También se incluyen en algunos sistemas de transmisión para el bucle de abonado, como los antiguos módems telefónicos V.32bis y V.34, y los modernos estándares xDSL como ADSL2+ y SHDSL. Es común su uso en sistemas de comunicación para el espacio profundo (sondas espaciales, misiones no tripuladas, etc.).

Como hemos visto, los códigos convolucionales son capaces de mejorar significativamente la probabilidad de error en un canal BSC de baja calidad, el problema que surge es que esto conlleva duplicar la velocidad binaria en el canal. En el caso de canales con limitaciones en banda, la única manera de aumentar la velocidad binaria sin incrementar la velocidad de símbolo es mediante el uso de una técnica de modulación más eficiente, es decir, que considere un mayor número de bits por símbolo. Sin embargo, una modulación más eficiente implica una constelación de símbolos más densa, lo que resulta en una menor distancia entre símbolos adyacentes y, por ende, una menor energía por bit, ambos factores que incrementan la tasa de error de bit.

Para poder compensar este incremento en la tasa de error de bit, los códigos convolucionales pueden combinarse con técnicas de modulación digital para generar la denominada modulación codificada Trellis o TCM (por sus siglas en inglés) que permite un alto nivel de corrección de errores.

# Conclusión

Hemos definido y desarrollado la importancia de los códigos detectores de error, los códigos cíclicos y los códigos convolucionales en la comunicación de datos, analizando profundamente su funcionamiento.

En resumen, los códigos detectores de error son aquellos esenciales para detectar y corregir errores en la transmisión de información, garantizando la integridad de los datos. Los códigos de paridad y los códigos de peso constante son los dos pilares esenciales que se utilizan en la detección y posterior corrección de errores en la transmisión de información.

Por otra parte, los códigos cíclicos son comunes en varios estándares de comunicación y se destacan por su estructura algebraica que facilita la detección y corrección de errores, siendo más eficientes y fáciles de implementar.

Por último, los códigos convolucionales en los sistemas de transmisión continua deben corregir errores en flujos constantes de datos. Para aplicaciones como las comunicaciones por satélite y la transmisión de datos en tiempo real, estos últimos ofrecen una alta capacidad de corrección de errores en condiciones adversas.

Finalmente, concluimos que los códigos analizados forman parte de un proceso muy importante de la comunicación de datos, ya que la corrección de errores es lo que garantiza la integridad y precisión de la información transmitida. Los consideramos ampliamente necesarios para que las transmisiones sean confiables y que la calidad de la comunicación sea consistente en una variedad de sistemas y tecnologías.

#

# Bibliografía

Alvarado Escamilla, R. (2004). Códigos para detección y corrección de errores en comunicaciones digitales. Ingenierías, 7(25), 51-60.

Diaz Portillo, J. O. (2016). Introducción a la teoría de códigos cíclicos.

Estran Gea, S. (2009). Códigos convolucionales.

Guridi, P. F. Códigos Convolucionales y Algoritmo Viterbi.

Mamani Mamani, V. *Códigos cíclicos con una aplicación a la corrección de errores de ráfaga* (Doctoral dissertation).

Martın, J. I. F. Códigos Correctores de Errores.

# Anexo: Autoevaluación con Preguntas y Respuestas

**1. ¿Por qué se distinguen los códigos cíclicos? ¿Cuál es su aplicación?**

Los códigos cíclicos distinguen por su estructura algebraica que facilita la detección y corrección de errores.

Debido a su eficiencia y facilidad de implementación, estos códigos son muy utilizados, y su aplicación es notable en estándares de comunicación como Ethernet y CDMA, donde la capacidad de gestión de errores es esencial para mantener la calidad de la transmisión.

**2. ¿Es posible asegurar una transmisión exenta de errores? Enumere las razones comunes de los errores en transmisiones.**

No, es imposible asegurar que una transmisión esté exenta de errores.

Las razones comunes en los errores en transmisiones pueden ser:

* **Interferencias Electromagnéticas (EMI)**: La presencia de señales electromagnéticas de otros dispositivos electrónicos puede inducir corrientes parásitas en el medio de transmisión, causando alteraciones en los datos transmitidos.
* **Ruido Térmico**: También conocido como ruido blanco, es generado por el movimiento térmico de los electrones en los conductores y puede provocar fluctuaciones aleatorias en la señal.
* **Distorsión de la señal**: Diferentes componentes de la señal pueden viajar a diferentes velocidades, causando una alteración en la forma de la señal original, lo que resulta en errores.
* **Ruido Impulsivo**: Picos breves y de alta energía en el medio de transmisión, a menudo causados por conmutaciones eléctricas o descargas estáticas, pueden corromper los datos.
* **Interferencias de Frecuencia**: Las señales de otras transmisiones en frecuencias cercanas pueden mezclarse con la señal original, causando errores.
* **Errores de Sincronización**: Desajustes en la sincronización entre el emisor y el receptor pueden provocar que los datos se interpreten incorrectamente.
* **Desvanecimiento (Fading)**: Variaciones en la amplitud de la señal debido a cambios en el entorno de transmisión, como el movimiento de objetos o cambios en la atmósfera, pueden causar pérdidas temporales de señal.
* **Problemas de Hardware**: Fallos en los componentes del hardware, como transceptores defectuosos, cables dañados o conectores sueltos, pueden introducir errores en la transmisión.
* **Multipath Propagation**: La recepción de múltiples versiones de la misma señal, debido a reflejos en obstáculos, puede causar interferencias y errores en la decodificación.

**3.** **¿Los errores son evitables? Justifique.**

La mayoría de los errores mencionados en la pregunta anterior son evitables mejorando la calidad del hardware usado en la transmisión o asegurando que los componentes relacionados a la transmisión estén sincronizados.

**4.** **¿Hay errores ineludibles?**

Sí, pues hay otros muchos errores que provienen de la naturaleza de las herramientas que usamos o a raíz de las condiciones climáticas que se estén atravesando durante el momento de la comunicación.

**5. ¿Qué significa el concepto de grado en un código detector o corrector de error? Ejemplifique.**

El concepto de grado de un código detector o corrector de error viene dado por la capacidad que éste tiene para detectar/corregir errores. Por ejemplo, un código detector de errores de **grado 1** va a poder detectar únicamente **errores unitarios**. Es decir, errores producidos al variar un dígito en la transmisión. Un código corrector de errores de **grado 3** va a poder, no solo detectar errores de variación de 3 binits sino que también corregirlos.

**6. Defina código cíclico.**

Los códigos cíclicos son una subclase de los códigos de bloque lineales (códigos de grupo), los cuales poseen un esquema de decodificación eficiente, es decir que pueden ser decodificados mediante el uso de algoritmos relativamente simples. Se dice que un código es cíclico cuando cualquier desplazamiento en lazo cerrado de una palabra-código da como resultado otra palabra-código existente dentro del conjunto empleado para codificar los posibles mensajes.

**7. ¿Qué son los códigos convolucionales?**

Los códigos convolucionales pertenecen a la familia de los códigos lineales al igual que los códigos de bloque, se utilizan para garantizar la integridad de la información por medio de agregar redundancia a la misma, logrando que las palabras código tengan la distancia mínima necesaria. Entonces, los códigos convolucionales son un tipo de códigos correctores de errores caracterizados por la terna (*n, m, k*). Donde ‘*n*’ es el número de entradas al codificador, ‘*m*’ es el número de salidas y ‘*k*’ la profundidad del código. Las salidas del código convolucional serán definidas por la entrada actual y las *k* − 1 entradas previas (Capacidad de memoria del código convolucional).

**8. Enumere las representaciones gráficas de los códigos convolucionales.**

Hay tres formas principales de representar gráficamente un código convolucional:

* *Diagrama de conexiones*
* *Diagrama de estados*
* *Puncturing*

**9. ¿De dónde surge que el código generado por el sistema se defina “convolucional”?**

Desde el punto de vista de la teoría de señales y sistemas, un codificador convolucional es un sistema lineal e invariante en el tiempo (LTI), discreto y con memoria. Por este motivo, el código de salida $y(t)$ del codificador cumple la expresión:

$y(t) = x(t) \* h(t)$

donde $x(t)$ son los k bits de entrada, $h(t)$ es la respuesta impulsiva del sistema y la operación “\*” representa la convolución temporal de ambos. De ahí que el código generado por el sistema reciba el nombre de convolucional.

**10. ¿Qué se define como “código catastrófico”?**

Un código catastrófico es aquel que, al ser utilizado en un codificador convolucional, mapea dos cadenas de entrada que difieren en un número infinito de bits en secuencias de código que solo difieren en unos pocos bits. Esto provoca una alta probabilidad de decodificar erróneamente las palabras código, resultando en un número infinito de errores en los bits de información. Es importante evitar el uso de estos códigos en la práctica debido a su alto riesgo de errores de decodificación.

1. Cuando se menciona "mod-2" se refiere a la operación módulo-2, también conocida como suma XOR (exclusive OR). En términos simples, en una operación de módulo-2, el resultado es 1 si el número de unos en los bits que se están sumando es impar, y 0 si es par.

   Por ejemplo:

   * 0 + 0 = 0
   * 0 + 1 = 1
   * 1 + 0 = 1
   * 1 + 1 = 0

   [↑](#footnote-ref-0)
2. En el contexto de los códigos convolucionales, multiplexar significa combinar varias secuencias de salida en una sola secuencia de salida. Esta combinación se realiza en base a algún criterio establecido por el sistema, como puede ser alternar entre las distintas secuencias de salida en intervalos de tiempo específicos o combinarlas de manera simultánea de alguna otra forma. [↑](#footnote-ref-1)
3. La delta de Kronecker es una función de dos variables que es igual a 1 cuando sus argumentos son iguales y es igual a 0 cuando sus argumentos son diferentes. [↑](#footnote-ref-2)
4. Una cadena de Markov es un modelo matemático de un proceso estocástico en el que la probabilidad de transición a un futuro estado depende únicamente del estado actual, sin considerar los estados previos. [↑](#footnote-ref-3)