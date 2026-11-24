COMUNICACIONES

Preguntas frecuentes de teoría
(Las preguntas del final no suelen salir de estas)

IMPORTANTE: este es un documento NO oficial, no pertenece a la documentación de

la cátedra. Puede contener errores u omisiones. Está confeccionado para que sirva

para rendir, no para entender los temas. Para entender el origen de los temas es

necesario buscar información en internet o perder tiempo interpretando los apuntes

de la cátedra, que están bastante mal redactados en su mayoría o son poco claros.

TEORÍA DE LA INFORMACIÓN

Tasa de información: cantidad de bits en promedio que se transmiten en un segundo,
es decir, la cantidad de información promedio que produce una fuente en un segundo.

Tasa de dígitos: cantidad de dígitos transmitidos por segundo por una fuente.

Velocidad de señalización: número de unidades de señal por segundo.

Entropía de una fuente: cantidad promedio de información por símbolo de la fuente. Es
máxima cuando los símbolos son equiprobables.

Entropía del canal: entropía calculada conociendo la equivocación de B respecto de A.

Información  Mutua:  información  transferida  desde  la  fuente  al  receptor  a  través  del
canal, es decir, la información real que llega al receptor en promedio.

Causas de los errores de canal:

ERRORES DE CANAL

 Ruidos impulsivos: producen grandes picos en la amplitud de la señal de ruido blanco,
provocando perturbaciones de varios binits, constituyendo lo que se denomina ráfaga.
Las causas que provocan el ruido impulsivo pueden ser externas o internas. Se puede
tratar con la utilización de módems.

Las causas externas son:

  Acoplamientos capacitivos o inductivos.

Las causas internas son:

  Variaciones en la impedancia.
  Sobrecarga de amplificadores.
  Interferencia debido a armónicas espurias.

Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

 Modulaciones espurias: pueden ser de tres tipos.

  Modulación  cruzada:  los  acoplamientos  inductivos  generan  captación  de  otras

señales.

  Intermodulación: producida por la variación en la linealidad de los amplificadores. Al
amplificar las señales estas se superponen. Esto se puede reducir utilizando módems
o reduciendo la amplitud de las señales.

  Eco: las variaciones de impedancia producen reflexiones en la señal provocando eco.

Esto se puede corregir utilizando supresores de eco.

 Variaciones de nivel: afecta la transmisión de datos. Las causas que las provocan son:

  Variaciones en la impedancia del canal.
  Enmascaramiento de la señal.
  Falla en los contactos.
  Falla en los amplificadores.

 Distorsión: es introducida por el propio canal. Las más conocidas son:

  Atenuación: producida por las variaciones en la impedancia.
  Fase/Frecuencia: se debe a que el canal introduce retardos para frecuencias distintas,

provocando desfasaje entre las armónicas.

  Variación de frecuencia de la portadora: se puede corregir mediante una señal sub-

portadora de sincronismo en frecuencia.

  Variación del nivel de muestreo: ocurre en la recepción, al demodular. Produce una

modificación en el ancho de los pulsos de la señal.

CODIFICACIÓN

Código  de  Bloque:  es  aquel  que  asigna  a  cada  elemento  del  alfabeto  fuente  una
secuencia  fija  de  símbolos  del  alfabeto  código.  Estas  secuencias  fijas  se  denominan
palabras código.

Ejemplo:

S1
S2
S3
S4

00
01
10
11

Código no-singular: es aquel donde todas sus palabras son distintas.

Ejemplo:

S1
S2
S3
S4

0
11
00
01

Código  unívoco:  es  aquel  en  el  que  a  cualquier  secuencia  de  palabras  código  le
corresponde una y sólo una secuencia de símbolos de la fuente. La condición para que
un  código  sea  unívocamente  decodificable  es  que  su  extensión  de  orden  n  sea  no
singular para cualquier valor finito de n.

Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

Ejemplo:

S1
S2
S3
S4

  1
11
00
10

En  este  ejemplo,  si  recibo  1100,  podría
corresponder a 𝑆2 y 𝑆3 o a 𝑆1, 𝑆1 y 𝑆3. Por lo
tanto, este código no es univoco.

Código instantáneo: un código es instantáneo cuando es posible decodificar las palabras
de  una  secuencia  sin  precisar  el  conocimiento  de  lo  símbolos  que  las  suceden.  La
condición para que un código sea instantáneo es que ninguna palabra código coincida
con el prefijo de otra.

Ejemplo:

S1
S2
S3
S4

0
10
110
1110

Código compacto: código unívoco cuya longitud media es menor o igual que la longitud
media de todos los códigos unívocos que pueden encontrarse para la misma fuente y
alfabeto. Reduce los costos de transmisión de datos.

Ejemplo:

S1
S2
S3
S4

02
1
01
2

S5
S6
S7

001
002
000

Método de Huffman: sirve para crear un código compacto a partir de un alfabeto r-ario.
Si el alfabeto tiene r=2, los símbolos se agrupan de a 2 y cada fuente reducida tendrá un
símbolo menos que la anterior. En la última reducción habrá 2 símbolos.

CÓDIGOS LINEALES

Matriz  generadora:  base  generadora  del  código  de  grupo.  Lo  genera  mediante  la
combinación  lineal  de  sus  vectores,  que  son  linealmente  independientes.  Tiene
dimensión “m x n”.

Matriz de control de paridad: base del espacio nulo V’ con “n-m” vectores linealmente
independientes. Permite determinar si una palabra código pertenece al código de grupo.

Síndrome:  se define  el  síndrome de  una palabra  código  como  el  producto  del  vector
asociado por la matriz de control de paridad transpuesta:

𝑆(𝑉𝑗) = 𝑉𝑗 × 𝐻𝑇
Se utiliza para corregir errores. Si el síndrome es cero, ésta corresponde al grupo. Si es
≠ de cero, el mensaje tiene algún error.

Error no detectable conociendo el Código de Grupo: es aquel que transforma la palabra
del  Código  de  Grupo  en  otra  del  Código  de  Grupo  y  que,  por  lo  tanto,  su  síndrome
continúa siendo cero.

Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

Punto de saturación de un sistema de cola cerrada:

TEORIA DE COLAS

Tiempo de respuesta medio en función del número de terminales

El  punto  de  saturación  de  un  sistema  de  cola  cerrada  es  el  número  máximo  de

terminales que pueden ser incluidos sin causar interferencia mutua.

Para 𝑁 = 1 no hay cola (solamente se tiene un terminal) por lo tanto el tiempo de
respuesta será E[s]. Para pocas terminales la interferencia es mínima. Pero, cuando
el número de terminales tiende a infinito, la probabilidad de tener la CPU desocupada
tiende a cero. Por lo tanto, la curva (w) será asintótica a la recta  𝑤 = 𝑁. 𝐸(𝑠) − 𝐸(𝑡).

La  intersección  de  la  asíntota  𝑤 = 𝐸(𝑠)  con  la  mencionada  anteriormente  se

producen en 𝑁∗:

A este punto se lo llama “Punto de saturación del sistema”.

𝑁∗ =

(𝐸(𝑠) + 𝐸(𝑡))
𝐸(𝑠)

COMUNICACIONES DIGITALES

TDM

Multiplexación por división de tiempos. Es una técnica de multiplexado donde se le
asigna a cada canal el ancho de banda completo del medio de transmisión por turnos
(intervalos de tiempo).

FDM

Multiplexación por división de frecuencias. En esta técnica se divide el ancho de
banda disponible en sub-bandas de frecuencias distintas para transportar diferentes
señales en simultaneo.

Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

Los mensajes no se mezclan porque cada uno está en una banda de frecuencias distinta y
suficientemente grande dada por la portadora (𝑓𝑐1, 𝑓𝑐2, 𝑓𝑐3, …).

Modulación con señal digital y portadora analógica:

En  la  transmisión  analógica  la  información  digital  es  soportada  por  una  onda,

generalmente senoidal, denominada portadora.

Se pueden modular 3 parámetros:

  Amplitud (técnica ASK -no se utiliza más-)
  Frecuencia (técnica FSK)
  Fase (técnica PSK)

Un  ejemplo  de  aplicación  es  la  transmisión  de  información  de  una  computadora
(señal digital) por una línea telefónica (señal analógica). Para esto se utiliza un MODEM
(Modulador-Demodulador) que convierte la señal analógica en digital y viceversa.

Para aumentar la velocidad de transmisión se utilizan los métodos FSK multinivel y

PSK multinivel:

  FSK multinivel: modulación por cambio de frecuencias y amplitudes. Varía tanto
la  amplitud  como  la  frecuencia,  por  lo  tanto,  se  transmiten  más  dígitos  en  la  misma
unidad de tiempo. Se tienen 4 posibilidades para transmitir:

Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

  PSK multinivel: modulación por cambio de fases y amplitudes. En esta técnica se
varían tanto la fase como la amplitud. Si se usan, por ejemplo, 2 amplitudes y 4 fases, se
tienen 8 combinaciones posibles para transmitir:

Técnica ASK:

Modulación por cambio de amplitud: se utiliza una portadora senoidal con una señal
también  senoidal.  Por  el  canal  migra  una  señal  de  frecuencia    𝑓𝑐    que  lleva  como
envolvente  la  señal  de  modulación.  La  amplitud  de  la  portadora  varía  de  acuerdo  al
mensaje. La fase y frecuencia permanecen constantes.

Espectro de señal en el tiempo:

Espectro de señal en el tiempo:

𝑓𝑐 y 𝑓𝑛 (la frecuencia de la portadora siempre es mucho mayor que la del mensaje).

Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

ASK coherente:
La  portadora  tiene  la  misma  frecuencia  en  el  origen  y  el  receptor.  Se  requiere  la
portadora en el lugar de recepción en sincronismo con la de emisión. Eso aumenta el
costo.

PCM:
Modulación  por  pulsos  codificados.  Técnica  de  cuantificación  y  codificación  de
niveles. Se preestablece un numero finito de niveles para asignarle a los distintos valores
de  la  señal,  mediante  redondeo.  Estos  niveles  están  codificados.  Cuando  la  señal
muestreada  se  encuentra  en  un  rango  determinado  de  valores  se  le  asigna  el  nivel
correspondiente al mismo.

Ejemplo: dada una señal, cuyo intervalo de variación de amplitudes es [-4.5; 4.5], se
adoptan como valores a codificar: -4.5; -3; -1.5; 0; 1.5; 3; 4.5. Estos valores se denominan
“Niveles cuánticos” y tienen asociados un intervalo.

Concepto de banda ancha y concepto de espectro de mensaje (o señal):

La banda ancha es el espectro de frecuencias para la transmisión de datos entre dos
puntos. La señal es lo que se quiere transmitir de un punto a otro. Para la transmisión
de información, se envían mensajes compuestos por señales, los cuales se encuentran
dentro del espectro de la banda ancha y viajan a través del mismo con el objetivo de
llegar a destino.

Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

Ancho de banda práctico ocupado por una señal digital real:

El ancho de banda práctico de una señal digital real es  𝜔 =

1
. Como tengo espectro

𝜏

1
infinito, recorto el 𝐵𝑤 en
, que me garantiza que si se recupera todo lo que está antes
𝜏
de ese punto, se recupera el 98% de la información.

Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

