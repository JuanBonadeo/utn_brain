Ancho de Banda: es la diferencia entre la frecuencia más alta y la más baja contenidas en una señal, y se mide en Hz.

Modulación:

* ¿Qué es? Modular es trasladar un mensaje (información) que está en baja frecuencia a una señal portadora de alta frecuencia
* ¿Para qué modulamos? Para poder transmitir el mensaje a una mayor distancia
* ¿Cómo se modula? Modular es trasladar el mensaje a la frecuencia de la portadora para que llegue más lejos

La modulación puede ser Analógica o Digital, esto dependerá de la portadora. Si la portadora es analógica entonces la modulación es analógica y si la portadora es digital, entonces la modulación es digital.

¿Quién modula a quién? Es el mensaje quien modula a la portadora

MODULACIÓN ANALÓGICA

1er caso: mensaje analógico y portadora analógica

Diagrama de bloques:

Una vez que llega el mensaje , del otro lado lo recibe un modem que vuelve a modularizar el mensaje y lo trae nuevamente a baja frecuencia .

Dado a que es el mensaje quien modula a la portadora, en este tipo de modulación, el mensaje no queda “visible” pero queda escondido en la amplitud máxima de la portadora.

Gráfica de ambas señales:

2do caso: Cuando el mensaje es digital y la portadora es analógica se pueden modular por 3 parámetros: amplitud, frecuencia y fase.

Por amplitud: Modulación por movimiento de amplitud (A.S.K). Se modula la portadora en función a la amplitud del mensaje logrando que el mensaje quede nuevamente escondido en la portadora.

Por frecuencia: Modulación por movimiento de frecuencia (F.S.K). Se modula la portadora en función de la frecuencia de la señal digital.

Por fase: Modulación por movimiento de fase (P.S.K). La frecuencia y la amplitud de la señal portadora es la misma pero cuando el mensaje cambia de dígito, la señal cambia de fase.

Algunas conclusiones del 2do caos:

* Para sistemas binarios P.S.K es el más eficiente
* Para sistemas multiniveles F.S.K es el más eficiente
* En multinivel, si bien se reduce el ancho de banda para la misma transmisión de información, empeora el ruido y hay mayor probabilidad de error.

Muestreo de Señales

Dada una señal analógica, la misma puede ser particionada en muestras a una frecuencia de muestreo tal, que a partir de estas muestras puede ser reconstruida, ya que no es necesario estar atendiendo continuamente una señal analógica para rescatar de ella toda su información, sino que basta con tomar muestras de ella.

Para elegir la frecuencia de muestreo tengo que conocer cómo es la señal que voy a muestrear y la máxima frecuencia de la evolución de dicha señal.

Ej: conocer la velocidad máxima de un auto de carreras por más de que no esté siempre andando en esa velocidad

En este caso vamos a tener un mensaje analógico y una señal muestreadora (es una portadora de pulsos)

Esta señal muestreadora también es de alta frecuencia, pero es de pulsos, siendo la amplitud máxima de cada pulso la de la señal del mensaje.

1er caso: Modulación por amplitud de pulso (P.A.M). La señal muestreada es la señal muestreadora (portadora) con su frecuencia, pero con la amplitud de la señal del mensaje en cada muestra.

2do caso: Modulación por ancho/duración (P.D.M o P.W.M). Se modula el ancho del pulso según la amplitud de cada instante de muestreo.

3er caso: Modulación de la posición del pulso (P.P.M). Se modula la posición (desfase) del pulso según la amplitud de cada instante de muestreo (Se mueve el pulso conforme la altura de la señal del mensaje).

! La frecuencia de muestreo para todos los casos siempre es alta

MODULACIÓN DIGITAL

Las señales analógicas pueden ser digitalizadas, para ello siguen un conjunto de 3 etapas: Muestreo, Cuantificación y Codificación.

Muestreo: Se toma la señal analógica y se divide en intervalos de igual duración con una misma frecuencia de muestreo (estas muestras van a tener distintas amplitudes entre sí ya que siguen la forma de la señal del mensaje).

Cuantificación: Se redondean las muestras a el valor de amplitud más cercano entre todas las muestras.

Codificación: Se traducen los valores obtenidos en la cuantificación a código binario.

1er caso: Modulación por pulsos codificados (P.C.M). Reemplazo cada valor de la muestra, que es analógica, por bits (pulsos binarios)

2do caso: Multiplexación por división de tiempo (T.D.M)

A veces sucede que se quiere transmitir una señal que está conformada por muestras pero que hay mucho tiempo ocioso entre cada muestra, por lo que se opta por multiplexar dicha señal con otras a fin de aprovechar más el tiempo.

De esta forma se transmiten varias señales juntas, al mismo tiempo. A su vez, se indica la trama, que es el conjunto de 1 muestra de cada canal, para dar noción de las distintas señales.

Cuando la señal multiplexada llega al destino, se separan las distintas señales y se logra entender cada mensaje.

El proceso de TDM se lleva a cabo de la siguiente manera:

Multiplexación: Las señales individuales se dividen en segmentos de tiempo, y cada señal se asigna a un intervalo de tiempo específico dentro de un marco de tiempo periódico. Por ejemplo, si tienes tres señales para transmitir, se asignan tres intervalos de tiempo dentro de cada marco de tiempo.

Transmisión: Los datos se transmiten secuencialmente en el medio compartido en función de los intervalos de tiempo asignados. Cada señal se envía durante su intervalo de tiempo respectivo.

Recepción: En el extremo receptor, se realiza la demultiplexación para separar las señales individuales. Cada señal se extrae del flujo de datos en función de la información de tiempo y se reconstruye en su forma original.

3er caso: T.D.M - P.C.M

Multiplexación por división de frecuencia (F.D.M)

Se usa para transmitir múltiples señales a través de un medio de transmisión compartido. Las señales se transmiten en distintas frecuencias, lo que permite que múltiples señales viajen simultáneamente a través del mismo medio sin interferirse entre sí (sin que se pisen entre ellas).

FDM se utiliza en diversos sistemas de comunicación, como la radiodifusión de radio FM, la televisión por cable, etc.