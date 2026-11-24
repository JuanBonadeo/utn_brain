222...777...---     ERRORES DE CANAL

222...777...111...---      RUIDO BLANCO

El Ruido en un canal limita la capacidad de este para transmitir información.
El  principal  ruido  de  Canal  se  la  conoce  con  el  nombre  de  Ruido  Blanco.  Su

importancia reside en el hecho de que es imposible de eliminar dado su aleatoriedad.

Se  conoce  como  Ruido  Blanco  aquel  que  aparece  en  el  canal  debido  a  la

asitación molecular y atómica que produce la temperatura.

De la figura resulta que la señal con ruido presenta un valor medio (Vm) y una
evolución  aleatoria  alternante  en  el  tiempo.  Ahora  bien:  ¿Qué  información  nos
proporciona  la  curva  normal?  En  ella  podemos  hallar  la  probabilidad  que  existe  de
encontrar una señal de ruido superior a un determinado valor o entre dos valores. En la
figura la zona sombreada determina la probabiladad de tener una señal de ruido blanco
entre Vm(1) y Vm(2).

222...777...222...---      ANCHO DE BANDA DE UN CANAL

El ancho de banda de un canal resulta una caracteristica del mismo que describe

su comportamiento ante señales de distintas frecuencias.

Entendiendo  por  ganancia  (o  atenuación)  de  un  canal  a  la  relación  entre  la

amplitud de la señal en la recepción y amplitud de la señal en la emisión. Resulta:

donde:

Vr es la amplitud de la señal de salida.
Vs es la amplitud de la señal de entrada.

Esta  relación  entre  amplitudes,  o  entre  potencias,  es  muy  común  expresarla

mediante una unidad dimensional denominada decibeles (dB) que no es más que:

G[dB] = 10 log G
si G es una relación entre amplitud de señales; o

A[dB] = 10 log A
si A es una relación entre potencias.

 Se entiende por ancho de banda  a  la  diferencia  entre  la  frecuencia  superior  de
corte  (f2),  y  la  frecuencia  inferior  de  corte  (f1).  Siendo  ellas  las  frecuencias  donde  la
relación entre amplitudes de señales de salida y entrada disminuyen en 3 dB respecto de
la  ganancia  (G)  de las frecuencias  medias,  siendo  esta  la  frecuencia  de  uso  normal  de
canal.

Generalmente  cuando  la  frecuencia  inferior  de  corte  es  pequeña  se  puede

aproximar el ancho de banda a la frecuencia superior de corte.

222...777...333...---      CAPACIDAD DE UN CANAL CON RUIDO

Estudios de Hartley y posteriores trabajos de Shannon prueban que si:

La potencia media del ruido blanco es N, entonces, la entropía

media del canal o equivocación de Y respecto de X es:

H(Y/X) = B . lg (2 . | | . e . N)
En,  la  expresión,  B  es  el  ancho  de  banda  del  canal,  N  es  la

potencia media del ruido y e es el número neperiano.

La señal emitida es continua y con distribución mal, la entropía

en la recepción para una potencia media S es:

H(Y) = B . lg (2 . |  | . e . (N + S))

Entonces la capacidad del canal:

C = I(X,Y)

H(Y) = H(Y/X)
B . lg (1 + S/N)   [bps]

222...777...444...---      CAUSAS  DE  ERRORES  DE  CANAL

222...777...444...111...---      Ruidos Impulsivos: El ruido impulsivo constituye la principal fuente

de error dentro de los posibles errores de canal.

Los  ruidos  impulsivos  provocan  grandes  picos  en  la  amplitud  de  la  señal  de
ruido blanco que llegan a saturar el canal, por lo tanto, llegan a provocar perturbaciones
de varios binits constituyendo lo que se denomina ráfaga.

En  la  figura  se  observa  una  serie  de  gráficos  donde  se  visualiza  una  señal  a
emitir asociada a una tira de binits  que  constituyen el  dato a emitir,  la señal de ruidos
blancos con los picos debido a ruido impulsivo, la señal recepcionada que no es más que
la suma de la señales anteriores, y finalmente en función de esta ultima la determinación
del dato recibido y los binits equivocados (cabe destacar que las amplitudes graficadas
no guardan relación con respecto a la realidad, donde la amplitud de la señal de ruido es
mucho menor que la de la señal a transmitir).

Las causas que producen ruido impulsivo se pueden agrupar en causas externas e
internas  (  al  canal).  Se  analizan  distintas  situaciones  donde  puede  presentarse  ruidos
impulsivos:

 Dentro de las fuentes externas de ruido impulsivo se tienen:

  Acoplamientos Capacitivos o inductivos debido a:

  Acción de canales paralelos.
  Equipos de conmutación mecánica.
  Señales de supervisión
  Fenómenos atmosféricos.

 Las fuentes internas pueden deberse a:

  Variaciones en la impedancia debido a conexiones.
  Señales que sobrecargan los amplificadores.


Interferencias debido a armónicas espureas generadas por filtros.

Este tipo de errores pueden ser  contrarrestados por medio de la utilización de modems
(MOdulador  –  DEModulador)  adecuados  al  canal  y  al  ruido  impulsivo  que  en  el  se
puede presentar.

222...777...444...222...---           Modulaciones  Espureas:  Otro  tipo de errores  de  canal  es  debido a

modulaciones espureas, se puede presentar bajo tres formas:

  modulación Cruzada (1),
  intermodulación (2) y
  eco (3).

(1)  Los  acoplamientos  inductivos  o  capacitivos  entre  canales  pueden  provocar
captación  de  señales  de  otros  canales,  este  efecto  se  conoce  con  el  nombre  de
Modulación  Cruzada.  Este  tipo  de  captaciones  es  común  que  se  produzca  en  canales
pares,  canales  múltiples  y  antenas  de  microondas  comunes.  La  forma  de  tratar  esta
causa  de  error  es  similar  al  de  ruido  blanco,  su  nivel  resulta  mensurable,  y
generalmente, no es de fundamental importancia en la transmisión de datos.

 (2)  Variaciones  en  la  linealidad  de  los  amplificadores,  en  canales  multiplex
provocan  modulaciones  espureas  conocidas  con  el  nombre  de  Intermodulación.  Este
error es debido a que al amplificar las señales en conjunto esta falta de linealidad puede
producir armónicas que pueden afectar bandas de otros canales. La intermodulación es
común en señales de tipo repetitivo por su alto contenido armónico, señales de tal tipo
son  las  de  discado,  las  de  supervisión.  La  intermodulación  puede  ser  corregida
utilizando modems adecuados o reduciendo la amplitud de señales de tipo repetitivo.

(3)  Las  variaciones  de  impedancia  del  canal  puede  provocar  reflexiones de  las
señales  provocando  una  modulación  espurea  denominada  Eco,  en  canales  de  voz  con,
fin de eliminar este efecto se utilizan supresores de eco.

222...777...444...333...---     Variaciones de nivel (desvanecimiento): Las variaciones de nivel de la señal
también  pueden  afectar  la  transmisión  de  información  (datos),  en  especial  si  estas
variaciones ocurren en forma rapida.

Entre las causas que pueden provocar variaciones de nivel encontramos:

  Variaciones de impedancia del canal;
  Fallas en contactos y
  Fallas en amplificadores.

Como  así  también  el  enmascaramiento  de  la  señal  provocada  por  fenómenos
meteorológicos, como lluvias, que afectan canales de microondas. Este efecto se conoce
con el nombre de desvanecimiento. Es posible en emisiones radiales.

Este  tipo  de  error  hace  que  se  considere  a  este  canal  como  de  pobre  resultado

para la transmisión de datos.

222...777...444...444...---          Distorsión:  Otra  causa  de  error  en  canales  es  provocada  por  distorsiones
introducidas por el propio canal. Entre las distorsiones mas comunes encontramos:

  Atenuación,
  Distorsión fase/frecuencia,
  Variación de frecuencia de la portadora y
  Variación del nivel de muestreo.

La ventaja de esta causa de error es el admitir correcciones por medio del diseño,
ya  que  el  canal  las  introduce  en  forma  sistemática  (repetitivamente  y  en  forma
previsible).

La  atenuación  es  provocada  por  variaciones  en  la  impedancia  del  canal  con  la
frecuencia.  Se  puede  graficar  la  atenuación  en  función  de  la  frecuencia.  En  estos
gráficos como el de la figura, es posible encontrar canales como el “a” que solo pueden
utilizarse  en  un  entorno  reducido  de  la  banda  y  otros,  como  el  “b”,  que  admiten  un
mayor  ancho  de  banda.  Este  ultimo  tipo  de  canales  puede  llegar  a  lograrse  desde  el
primero mediante el uso de ecualizadores adecuados.

La distorsión fase/frecuencia se debe  a que el canal introduce distintos retardos
para frecuencias diferentes. Con la cual se varían las velocidades de transmisión para las
ondas de distintas frecuencias, esto provoca defasajes entre las distintas armónicas de la
señal.

Si  se desea transmitir una  seal, por medio de un componente fundamental y de
su  tercera  armónica  (descomposición  de  Fourier),  y  no  esta  presenta  la  distorsión
fase/frecuencia se observaría la forma de onda de la figura:

Si  en  cambio  se  tuviera  un  defasaje  entre  ambas  ondas  (fundamental  y  tercera

armónica) debido a esta distorsión la señal resultante presentaría  el siguiente aspecto:

Estos  primeros  dos  tipos  de  distorsión  suelen  encontrarse  relacionados  en el  momento
de pretender corregirlos, así, si se tratara de corregir la atenuación por medio de cables
bifilares (dos conductores) de larga distancia muy cargados se empeoraría la distorsión
fase/frecuencia.  Para  reducir  esta  última  se  tendrían  cables  coaxiles  y  circuitos  de
microondas.

Otro  tipo  de  distorsión  es  la  variación  de  frecuencia  de  la  portadora  (señal
soporte) con respecto a la frecuencia de emisión de la misma. Esta distorsión se puede
corregir  mediante  las  transmisiones  de  una  señal  sub-portadora  de  sincronismo  en
frecuencia.

La  distorsión  por  variación  del  nivel  de  Umbral  de  muestreo  se  produce  en  el
momento  de  la  demodulación  o  al  regenerar  los  pulsos  en  repetidoras.  Esta  distorsión
produce una modificación en el ancho de los pulsos de la señal. Así, se puede observar
en  la figura como  variaciones  positivas  o  negativas  de  este  nivel  de  Umbral  provocan
alargamientos  o  acortamientos  del  ancho  de  los  pulsos  que  representan  al  “uno”  o  al
“cero”.

