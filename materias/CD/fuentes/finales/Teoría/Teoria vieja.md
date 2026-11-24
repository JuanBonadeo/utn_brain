Explique brevemente y grafique adecuadamente el punto de saturación de un sistema de cola cerrada.

Considerando la figura, en ella se grafica el tiempo de respuesta medio W en función de N (número de terminales):

 EMBED PBrush  

El punto de saturación de un sistema de cola cerrada es el número máximo de terminales que pueden ser incluidos de tal forma de no causar interferencia mutua.
Para N =1 no hay cola (solamente se tiene un terminal) por lo tanto el tiempo de respuesta será E[s].
Para pocos terminales N la interferencia entre usuarios es mínima, esto quiere decir que cuando uno de los usuarios busca una interacción con la CPU los demás generalmente están en el modo de pensamiento, por lo tanto, ocasionalmente se formara una cola de espera. Es posible entonces considerar la curva estratégica a W = E[s] cuando se tiene pocos terminales. 
Cuando el número de terminales tiende a infinito, la probabilidad de tener la CPU desocupada (p0) tiende a cero, consecuentemente la curva será asintótica a la recta N x E[s] – E[t] con N tendiendo a infinito.
La intersección de las dos asíntotas se produce en N* tal como:
N* = (E[s] + E[t]) / E[s]
Este valor de N se llama punto de saturación del sistema.

Concepto de entropía. Concepto de información mutua y concepto de entropía del canal

La Entropía puede ser considerada como una medida de la incertidumbre. También puede ser entendida como la cantidad de información promedio que contienen los símbolos de la fuente.
Cuanto más equiprobables sean los símbolos de la fuente mayor será la entropía, puesto que no tengo certeza sobre que símbolo emitirá la fuente.

La información mutua es la información transferida desde la fuente al receptor a través del canal, es decir, el promedio de la información que llega al receptor

La entropía del canal es la probabilidad de aparición de un símbolo bj a la salida del canal, cuando se envió un símbolo ai

Concepto de código instantáneo y condición de existencia, de código compacto y cota de longitud promedio. Ejemplos

Un código es instantáneo cuando es posible decodificar las palabras de una secuencia sin precisar el conocimiento de lo símbolos que las suceden. La condición para que un código sea instantáneo  es que ninguna palabra código coincida con el prefijo de otra. Ejemplo:

S11
S201
S3001
S40001

La condición necesaria y suficiente para que un código sea instantáneo es que ninguna palabra del código coincida con el prefijo de otra.

Un código compacto es aquel código instantáneo cuya longitud media tiene la menor longitud posible. Para obtener la longitud mínima se debe seguir el esquema de “A mayor probabilidad, menor longitud de palabra”. Estos códigos se pueden encontrar por medio del método de Huffman.
Ejemplo:
S102
S21
S301
S42
S5001
S6002
S7000
	
La longitud media de un código es mayor o igual que la entropía de la fuente dividida por el log2 del número de símbolos del alfabeto código. 
				Hr(s)<=L
Esto expresa que no se puede conseguir un código cuya longitud media sea menor que Hr(s)

Modulación FSK, PSK y multinivel. Gráficas y aplicación

FSK (Modulación de Frecuencia). Mantengo constantes la amplitud y la fase de la portadora y vario la frecuencia de la portadora. Varía su frecuencia según la señal de modulación tenga un nivel alto o bajo. Se hace necesaria la presencia de la portadora en el lugar de destino
PSK La amplitud y la frecuencia son constantes. La fase varía
FSK Multinivel
Se utilizan dos frecuencias y dos amplitudes, transmito más dígitos en la misma unidad de tiempo.
Varío tanto amplitud como frecuencia.
Tenemos entonces, cuatro posibilidades para transmitir:
 EMBED Visio.Drawing.6  
PSK Multinivel (QAM o APSK)
Se varia la Fase y la Amplitud

2 Amplitud
4 Fases
Grafica Angular o Polar    2 amplitudes para cada fase  8 posibilidades 3 digitos
 EMBED Visio.Drawing.6  
Tengo 8 combinaciones por lo cual estoy mandando 8 dígitos.

Concepto de código unívoco, instantáneo y compacto. Condiciones necesarias. Ejemplos

Código instantáneo: un código es instantáneo si ninguna palabra código coincide con el prefijo de otra. Otra definición es que un código es instantáneo cuando es posible decodificar las palabras de una secuencia sin precisar el conocimiento de lo símbolos que las suceden. Ejemplo:

S11
S201
S3001
S40001

Código unívoco: Un código es unívocamente decodificable  si a cualquier secuencia de palabras código le corresponde una y sólo una secuencia de símbolos de la fuente. Otra definición es que un código es unívocamente decodificable si la extensión de orden n es no singular para cualquier valor finito de n. Ejemplo:

S11
S201
S3001
S40001

Código compacto: Un código unívoco que asocia los símbolos de una fuente con palabras formadas por símbolos de un alfabeto r-ario es compacto si la longitud media es igual o menor que la longitud media de todos los códigos unívocos que pueden aplicarse a la misma fuente y al mismo alfabeto. Ejemplo:

S102
S21
S301
S42
S5001
S6002
S7000

¿En una transmisión, cada mensaje ocupa un lugar determinado del ancho de banda del canal? ¿Por qué? Justificarlo.

Si ya que viaja en una portadora digital o analógica según sea el caso, que transporta el mensaje para que no sea afectado por los diversos tipos de ruidos posibles.
Cada mensaje ocupa un lugar determinado de la portadora para evitar la superposición o destrucción de los mensajes y su posterior correcta demodulación.

Concepto de entropía, tasa de información, tasa de dígitos, y velocidad de señalización. Dar ejemplos.

Entropía: cantidad media de información por símbolo de la fuente.

Velocidad o tasa de información: cantidad de bits en promedio que se transmiten en 1 segundo, esto es, la cantidad de información promedio producida por una fuente en 1 (un) segundo:

R  =  H’(A) = I / T

Velocidad o tasa de dígitos: cantidad de dígitos por segundo transmitidos:

r  =   H(A) / R = N / T

Velocidad de señalización: inversa del tiempo mínimo que dura un pulso:

s  =  1/τmin

¿Para qué sirve el método de Huffman? ¿Qué puede suceder si el alfabeto código tiene r=2? Explique

El método de Huffman sirve para crear un código compacto a partir de un alfabeto r-ario.
Lo que sucede es que los símbolos se agrupan de a 2 y cada fuente reducida tendrá 1 símbolo menor que la anterior. En la última reducción habrá 2 símbolos.

Definir entropía

La Entropía puede ser considerada como una medida de la incertidumbre. También puede ser entendida como la cantidad de información promedio que contienen los símbolos de la fuente. Cuanto más equi-probables sean los símbolos de la fuente mayor será la entropía, puesto que no tengo certeza sobre que símbolo emitirá la fuente.

¿Cuándo la entropía es máxima?

Cuando los símbolos de la fuente son equi-probables.

En el caso de un canal real, cuál es la entropía que la define y cual es su concepto

La entropía que la define es la entropía del canal, la cual es:
 EMBED PBrush  

La entropía del canal es la probabilidad de aparición de un símbolo bj a la salida del canal, cuando se envió un símbolo ai

Explicar modulación con señal digital y portadora analógica. Dar ejemplos de aplicación y cómo se aumenta la velocidad

En la transmisión analógica, la información digital es soportada por una onda (generalmente senoidal) denominada onda portadora. El parámetro a modular puede ser:
la amplitudASK
la frecuenciaFSK
la fasePSK
La modulación de una señal analógica se utiliza para transmitir información de computadora (señal digital) a través de una línea telefónica (señal analógica).
Se convierte la señal digital en analógica a través del MODEM y viceversa.
Para aumentar velocidad se utilizan los siguientes métodos.
FSK Multinivel
Se utilizan dos frecuencias y dos amplitudes, transmito más dígitos en la misma unidad de tiempo.
Varío tanto amplitud como frecuencia.
PSK Multinivel (QAM o APSK)
Se varía la Fase y la Amplitud


Qué efecto produce el ruido de canal. Explique. Nombre tres causas posibles.

El ruido en un canal tiene el efecto de limitar la capacidad de este para transmitir información. El ruido tiende a introducir errores en los mensajes enviados cuando se presenta en la  HYPERLINK "http://es.wikipedia.org/w/index.php?title=Banda_de_frecuencias&action=edit&redlink=1" \o "Banda de frecuencias (aún no redactado)" banda de frecuencias del espectro de la  HYPERLINK "http://es.wikipedia.org/wiki/Se%C3%B1al" señal.
Ruidos Impulsivos: Los ruidos impulsivos provocan grandes picos en la amplitud de la señal de ruido blanco que llegan a saturar el canal, por lo tanto, llegan a provocar perturbaciones de varios binits constituyendo lo que se denomina ráfaga.
Modulaciones Espureas: Otro tipo de errores de canal es debido a modulaciones espureas, se puede presentar bajo tres formas:

modulación Cruzada (1),
intermodulación (2) y 
eco (3).

Variaciones de nivel (desvanecimiento): Entre las causas que pueden provocar variaciones de nivel encontramos:
Variaciones de impedancia del canal;
Fallas en contactos y
Fallas en amplificadores.

Distorsión: Otra causa de error en canales es provocada por distorsiones introducidas por el propio canal. Entre las distorsiones mas comunes encontramos:
Atenuación,
Distorsión fase/frecuencia,
Variación de frecuencia de la portadora y
Variación del nivel de muestreo.

Definir código no singular, código unívoco y código instantáneo. Dar ejemplos.

Código instantáneo: un código es instantáneo si ninguna palabra código coincide con el prefijo de otra. Otra definición es que un código es instantáneo cuando es posible decodificar las palabras de una secuencia sin precisar el conocimiento de lo símbolos que las suceden. Ejemplo:

S11
S201
S3001
S40001

Código unívoco: Un código es unívocamente decodificable  si a cualquier secuencia de palabras código le corresponde una y sólo una secuencia de símbolos de la fuente. Otra definición es que un código es unívocamente decodificable si la extensión de orden n es no singular para cualquier valor finito de n. Ejemplo:

S11
S201
S3001
S40001

Código no singular: Es aquel que tiene todas sus palabras código distintas. Ejemplo:

S11
S201
S3001
S40001

Aplicación de modulación analógica con mensaje digital. Tipos y gráficos. De que manera se puede aumentar la velocidad de transmisión. Ejemplos

Se utiliza para transmitir información de computadora (señal digital) a través de la línea telefónica (señal analógica).
Se convierte la señal digital en analógica a través del MODEM y viceversa.
ASK(Manipulación por desplazamiento de la Amplitud)
FSK(Manipulación por desplazamiento de la Frecuencia)
PSK(Manipulación por desplazamiento de la Fase)
Para aumentar velocidad se utilizan los siguientes métodos.
FSK Multinivel
Se utilizan dos frecuencias y dos amplitudes, transmito más dígitos en la misma unidad de tiempo.
Varío tanto amplitud como frecuencia.
PSK Multinivel (QAM o APSK)
Se varia la Fase y la Amplitud



En el modelo de cola M/M/1 ¿Qué simboliza la segunda M de la notación de Kendal?

Simboliza una distribución de tiempo de servicio o de intervalo entre arribos exponencial.

Explique detalladamente la técnica TDM

Los usuarios toman su turno en forma circular, obteniendo todo el ancho de banda por un momento en dicho turno. Se utiliza el tiempo muerto entre pulsos para intercalar otros pulsos correspondientes a otros canales de información.





Explique ASK conceptualmente y realice los gráficos correspondientes

ASK (Amplitude Shift Keying – Modulación por cambio de amplitud).
Se utiliza una portadora senoidal con una señal también senoidal. Por el canal migra una señal de frecuencia fp que lleva como envolvente la señal de modulación. La amplitud de la portadora varia de acuerdo al mensaje, la fase y la frecuencia permanecen constantes.

Espectro de señal en el tiempo:
 EMBED Visio.Drawing.6  

Espectro de señal en frecuencia:
 EMBED Visio.Drawing.6  
fc > fn  la frecuencia de la portadora siempre es mucho mayor que la del mensaje.


Demodulación ASK coherente

La portadora tiene la misma frecuencia en el origen y receptor. Se requiere la presencia de la portadora en el lugar de recepción, y además esta portadora debe estar en sincronismo con la de emisión. Esto es un inconveniente porque provoca un aumento de costo.


Concepto de banda ancha y concepto de espectro de mensaje (o señal). Dar en un solo ejemplo como se aplica estos conceptos

La banda ancha es el espectro para la transmisión de datos entre dos puntos.
La señal es lo que se quiere transmitir de un punto a otro.
Para la transmisión de información, se envían mensajes compuestos por señales, los cuales se encuentran dentro del espectro de la banda ancha y viajan a través del mismo con el objetivo de llegar a destino.

Ruido impulsivo, definirlo y explicar cuales pueden ser sus fuentes

Ruidos Impulsivos: Los ruidos impulsivos provocan grandes picos en la amplitud de la señal de ruido blanco que llegan a saturar el canal, por lo tanto, llegan a provocar perturbaciones de varios binits constituyendo lo que se denomina ráfaga.
 Dentro de las fuentes externas de ruido impulsivo se tienen:
Acoplamientos Capacitivos o inductivos debido a:
Acción de canales paralelos.
Equipos de conmutación mecánica.
Señales de supervisión
Fenómenos atmosféricos.

 Las fuentes internas pueden deberse a:
Variaciones en la impedancia debido a conexiones.
Señales que sobrecargan los amplificadores.
Interferencias debido a armónicas espureas generadas por filtros.


Explicar brevemente la diferencia entre FDM y TDM. Dar un ejemplo sencillo haciendo un gráfico correspondiente
En la FDM, el espectro de frecuencias se divide entre los canales lógicos, donde cada uno de los usuarios posee una banda de frecuencia exclusiva. Por otra parte en la TDM, los usuarios toman su turno, durante el cual, cada uno, obtiene todo el ancho de banda por un corto tiempo.
Por otro lado, en TDM se utiliza el tiempo muerto entre cada pulso para intercalar otros pulsos correspondientes a otros canales de información, mientras que en FDM distintas frecuencias se asignan a distintos canales lógicos, cada uno de ellos funcionando en una parte del espectro, con una separación entre canales suficientemente grande para evitar que ocurran efectos de interferencia.

Gráfica TDM
 EMBED Visio.Drawing.6  
Gráfica FDM


Concepto de código compacto y ventajas de su aplicación

Un código compacto es aquel código instantáneo cuya longitud media tiene la menor longitud posible. Para obtener la longitud mínima se debe seguir el esquema de “A mayor probabilidad, menor longitud de palabra”. Estos códigos se pueden encontrar por medio del método de Huffman.
La ventaja es que son códigos con la menor longitud posible y esto influencia en los costos de transmisión de datos.

¿Cuál es la aplicación de la modulación analógica, donde el mensaje es digital? Nombrar los distintos tipos y hacer los esquemas correspondientes

La aplicación es la transmisión de información de computadora a través de una línea telefónica. Se convierte la señal digital en analógica a través del MODEM t viceversa.
En cuanto a modulación analógica, existen 3 tipos: ASK, FSK y PSK

Concepto de síndrome y aplicaciones. Ejemplo. Condiciones necesarias para corrección de errores simples en cada uno de los dígitos de la palabra código.

Síndrome: se define el síndrome de una palabra código S(Vj), como el producto del vector asociado por la matriz de control de paridad transpuesta:

S(Vj) = Vj * HT

Se utiliza para la detección de errores. Si el síndrome de una palabra código es cero, esta corresponde al código de grupo; si es distinto de cero el mensaje tuvo un error y se lo tiene que decodificar aplicando alguna regla de decisión.

¿Cuál es el ancho de banda práctico ocupado por una señal digital real? Explique.

El ancho de banda práctico de una señal digital real es w = 1/τ.



En los códigos lineales, explique porqué el síndrome de una palabra con error –S(u*)- coincide con el síndrome de la palabra que modela el error –S(g)-

S(u*) = u* . HT = (u + gi) . HT = u.HT + gi.HT   ⇒      S(u*) = gi.HT = S(gi)

¿Cómo se puede transmitir una señal digital por un canal analógico? Tipos de aplicaciones. ¿Qué modificaciones se pueden realizar para aumentar la velocidad?

Para transmitir una señal digital por un canal analógico se utiliza la modulación analógica. En donde la señal digital es transportada mediante una onda portadora. Los parámetros que se pueden modular son:

Amplitud: ASK
Frecuencia: FSK
Fase: PSK

Se utiliza para canales telegráficos y/o de voz referidos a la transmisión de datos. El equipo utilizado para la modulación y demodulación es el modem.
Para aumentar la velocidad se pueden utilizar las técnicas de FSK y PSK multinivel.
