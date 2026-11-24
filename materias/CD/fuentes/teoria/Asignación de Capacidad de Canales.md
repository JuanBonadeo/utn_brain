Comunicaciones – AAAsssiiigggnnnaaaccciiióóónnn   dddeee   CCCaaapppaaaccciiidddaaaddd   dddeee   CCCaaannnaaallleeesss
Ingeniería en Sistemas de Información

AAASSSIIIGGGNNNAAACCCIIIÓÓÓNNN   DDDEEE   CCCAAAPPPAAACCCIIIDDDAAADDDEEESSS   DDDEEE   CCCAAANNNAAALLLEEESSS

Enfocaremos el problema de determinar: ¿qué capacidad debe tener cada enlace

(bps) para suministrar una determinada performance?

Se supone una cierta distribución estadística de tráfico (promedio de longitud de
mensajes, frecuencia de ingreso, promedio del número de mensajes entre dos puntos de
la red).

Se  comienza  con  la  asignación  de  capacidades  para  luego  abordar  temas  tales

como: elección de topología, conexión entre concentradores, ruteo de mensajes, etc.

Existen distintos criterios para la asignación de capacidades. Se adopta el criterio
debido a L. KLEINROCK, que supone le costo linealmente proporcional a la capacidad.
Esto  es,  el  costo  equivale  a  una  determinada  capacidad  total  de  la  red.  Luego,  se
asignarán  las  capacidades  enlace  por  enlace,  con  el  criterio  de  tiempo  promedio  de
retardo mínimo. Esto da lugar a la llamada “estrategia de asignación de capacidades de
la  raíz  cuadrada”.  En  la  cual  la  capacidad  de  cada  enlace  es  proporcional  a  la  raíz
cuadrada del flujo de tráfico a través del enlace.

Consideramos el caso más simple, se tienen 7 ciudades, cada una de ellas con un
determinado  número  de  terminales  de  datos  (TTY)  a  conectarse  a  una  computadora
central en Rosario. Se adopta la configuración de red, (la topología) estrella.

Comunicaciones – AAAsssiiigggnnnaaaccciiióóónnn   dddeee   CCCaaapppaaaccciiidddaaaddd   dddeee   CCCaaannnaaallleeesss
Ingeniería en Sistemas de Información

Cada terminal (TTY) se supone que producen un mensaje, en promedio, 30 seg.
Cada  mensaje  se  supone  con  una  longitud  promedio  de  120  bits.  El  objetivo  es
determinar las capacidades troncales (Ci), en bps, para cada uno de los siete enlaces.

Antes  de  comenzar  analizaremos  que  sucede  en  el  concentrador  en  un  nodo
típico,  que  se  utiliza para  combinar  los  mensajes  entrantes  y  rutearlos,  luego,  hacia  el
enlace  apropiado  (previamente  hubo  efectuado  los  procesamientos  y  almacenamientos
necesarios).    El  modelo  más  simple  supone  todos  los  puestos  de  entrada  explorados
instantáneamente,  con  mensajes  en  un  buffer  FIFO  (se  considera  multiplexado
estadístico o asincrónico). Luego de un cierto procesamiento los mensajes destinados al
enlace i se rutean uno a la vez sobre la línea de salida del concentrador ( en el ejemplo
resulta un único buffer debido a que en configuración estrella cada  concentrador tiene
un solo enlace de salida).

Para  la  asignación  de  capacidades  ignoremos  detalles  de  las  operaciones  de
concentración  y almacenamiento.  Una  simplificación importante  surge  de  suponer que
el tiempo de procesamiento nodal es despreciable frente al retardo de espera de enlace
(línea disponible).

El modelo se reducirá a:

La frecuencia promedio de mensajes i del enlace i es la suma de las frecuencias
de los mensajes de todas las líneas entrantes al nodo. Por ejemplo: en la red estrella de
la figura cada terminal tiene la misma frecuencia promedio de mensajes (1/30 mensajes/seg.),
entonces, i para el i-esimo enlace es el número de terminales conectados a este por el
número de mensajes por segundo. Para el enlace 1 se tiene, en promedio:

en correspondencia con los 10 terminales conectados al concentrador de Mendoza.

Comunicaciones – AAAsssiiigggnnnaaaccciiióóónnn   dddeee   CCCaaapppaaaccciiidddaaaddd   dddeee   CCCaaannnaaallleeesss
Ingeniería en Sistemas de Información

La  teoría  de  la  cola  puede  aplicarse  a  este  modelo.  Se  supone  para  ello,
frecuencia  de  arribo  de mensajes  Poisson  con  mensajes  de  longitud  exponencialmente
distribuidos  con  una  longitud  promedio  de  mensajes  de  1/i
bits/mensajes  y  un  buffer  de
capacidad infinita, resultando un tiempo de retardo promedio del mensaje de:

donde:  i  es  la  frecuencia  de  mensajes  por  segundo  a  la  salida,  no  siendo  más  que  la
capacidad  del canal  (Ci)  –en  bps-  al  multiplicarla  por  la  longitud  promedio  en  bits en
promedio de los mensajes –longitud promedio 1/i-, luego:

luego:

 i  =  i  Ci

Este  retardo  incluye  el  tiempo  necesario  para  transmitir  un  mensaje  más  el
retardo del mensaje en el buffer. Los buffer reales presentan una probabilidad de bloque
inferior a 10e-3, por lo tanto pueden suponerse como buffer infinito.

Cuando de la frecuencia de flujo de tráfico es cercana al valor i Ci el tiempo de
retardo crece sin límites. Es común definir un parámetro de intensidad de tráfico que por
tener un único servidor coincide con el factor de utilización  (ui = i), luego:

En términos de este parámetro:

Para  i  <  1  el  retardo  será  Ti  =  1/i  C  i  exactamente  el  tiempo  necesario  para

transmitir el mensaje completo. Para  i  1, T i resulta muy grande.

Si  1 = 0,33 mens./seg. y 1/ i = 120 bits por mensaje, y si C1 = 100 bps se produce

un retardo por mensaje transmitido sobre el canal de salida de:

De este tiempo el necesario para transmitir el mensaje será:

Y el tiempo de almacenamiento es:

Resulta:

Comunicaciones – AAAsssiiigggnnnaaaccciiióóónnn   dddeee   CCCaaapppaaaccciiidddaaaddd   dddeee   CCCaaannnaaallleeesss
Ingeniería en Sistemas de Información

El  tiempo  de  retardo  sobre  el  canal  Rosario-Buenos  Aires  con  la  misma

capacidad (100 bps) se tiene:

Mientras que entre Corrientes y Rosario será, para la misma capacidad:

Incrementando  la  capacidad  del  canal  a  900  bps,  disminuye  el  tiempo  de  retardo,
resultando:

Considerando  la  red  como  un  conjunto  de  enlaces  (uno  por  nodo),  el  buffer
asociado  con  el  enlace  i-esimo  tiene  una  frecuencia  de  arribo  de  i  y  y  la  longitud
promedio de mensaje emitido será 1/, se tiene:

Se  considera,  que  esta  forma,  la  red  como  una  “caja  negra”,    observando  los
arribos a la caja, se tienen  mensajes ingresando a la caja por unidad de tiempo, donde:

Comunicaciones – AAAsssiiigggnnnaaaccciiióóónnn   dddeee   CCCaaapppaaaccciiidddaaaddd   dddeee   CCCaaannnaaallleeesss
Ingeniería en Sistemas de Información

La caja negra se comporta como una cola para la cual, por el teorema de Little,

tenemos:

N =  E[T]  =  E[n]

Para el promedio estadístico se tiene:

Sumado sobre todos los buffer de la red y aplicando el teorema de Little a cada

uno, nos da:

Con la ecuación para tiempo de retardo, podemos iniciar el manejo del problema

de asignación de capacidades de canales en una red (figura anterior).

Suponemos el objetivo es minimizar el tiempo de retardo promedio sobre la red

completa con una capacidad total supuesta fija. La frecuencia total de la red será:

El, retardo promedio de mensajes para la red se puede calcular por medio de la

ecuación(*).

Donde E[T] presenta el tiempo de retardo “pesado” con los Ti en el rango de 1 a

7. Suponiendo la capacidad total como la suma de las capacidades Ci, resulta:

Este valor se toma constante, debiendo elegirse los Ci tal que minimicen el valor
E[T].  Estos  valores  se  pueden  hallar  utilizando  los  multiplicadores  de  Lagrange:  se
puede  demostrar  que  el  mínimo  se  puede  hallar  minimizando    E[T]  +  C.  El
multiplicador de Lagrange  se elige para asegurar la constancia de C.

Minimizando por diferenciación de E[T] + C con respecto a Ci, se encuentra la

solución óptima dada por:

Comunicaciones – AAAsssiiigggnnnaaaccciiióóónnn   dddeee   CCCaaapppaaaccciiidddaaaddd   dddeee   CCCaaannnaaallleeesss
Ingeniería en Sistemas de Información

 cumple la función de parámetro intensidad de trafico para toda la red.

Con  esta  relación  de  capacidades,  canal  por  canal  es  posible  sustituir  en  la
ecuación (* *) y luego hallar Ti para cada canal. Luego se puede calcular la expresión
Tmin, siendo:

Esta  asignación  de  capacidad  se  denomina  la  “regla  de  asignación  de  la  raíz
cuadrada del flujo de información. El Tmin depende inversamente de C (o sea del costo).
Siempre es posible disminuir el tiempo de retardo, aumentado el valor de C y con ello el
costo. La ecuación de Tmin da el mínimo tiempo de retardo posible para un determinado
costo.

La ecuación de Ci opt. Tiene dos partes:

    La primera  parte  i/i es es el valor  mínimo necesario  que  puede ser
dado a Ci para habilitar el tráfico sobre el canal donde i es el promedio de mensajes ha
ser manejados y  1/i su longitud promedio, luego el cociente representa el promedio de
flujo ofrecido sobre el canal i en bps. Debe ser por supuesto menor que Ci.

    La segunda parte indica la capacidad remanente según la estrategia de

la raíz cuadrada.

¿Como se aplica, ahora, la estrategia de la raíz cuadrada al circuito de la figura 1?

La  inversa  de  la  longitud  i  =    =  1/120  para  todos  los  enlaces.  Entonces,  y  en

base a cada i se halla:

Luego,  para  C  =  4500  bps.  Como  la  capacidad  total  de  la  red,  resulta  un    =
0,0453.  –En  la  práctica  se  realizan  varias  elecciones  de  C,  y  cada  una  corresponde  a
diferentes costos, se encuentra el valor de tiempo de retardo mínimo para cada una y se
grafica el tiempo de retardo vs. el costo. De ello se obtiene la C apropiada para un cierto
tiempo mínimo.- Así se obtiene:

Comunicaciones – AAAsssiiigggnnnaaaccciiióóónnn   dddeee   CCCaaapppaaaccciiidddaaaddd   dddeee   CCCaaannnaaallleeesss
Ingeniería en Sistemas de Información

Luego,  se  debe  seleccionar  valores  de  capacidad  reales.  En  este  caso  se

seleccionan canales de 450 o 900 bps.

El costo de la línea de 450 bps es de aproximadamente 1 U$S por Km, y el de
900  bps  es  de  1,2  U$S  por  Km.  Es  claro  que  el  costo  sería  menor  si  adoptamos  una
topología árbol.

Consideremos  ahora  el  mismo  problema,  pero  con  una  estructura  árbol  para
observar  como  se  modifican  los  parámetros  de  la  red  y  el  costo.  Inmediatamente  se
percibe que la disminución de los Kilómetros de canales es notable.

Comunicaciones – AAAsssiiigggnnnaaaccciiióóónnn   dddeee   CCCaaapppaaaccciiidddaaaddd   dddeee   CCCaaannnaaallleeesss
Ingeniería en Sistemas de Información

Para  analizar  esta  red  y  determinar  la  asignación  de  capacidad  apropiada,
debemos tener en cuenta en el cálculo del retardo de  la cola no solamente en el de los
mensajes  de  los  terminales  que  entran  en  cada  nodo  sino  también  los  mensajes  de
concentradores  previos. Suponiendo  multiplex estadístico,  la  frecuencia de  arribos,  las
frecuencias de arribos se pueden sumar para determinar la frecuencia de arribo total al
nodo,  pero  las  estadísticas  de  mensajes  sobre  los  sucesivos  enlaces  están  ahora
relacionadas a otros. Esto es verdad si vale la suposición de independencia, esto es, se
ignoran las dependencias entre las distintas colas.

Bajo esta suposición los mensajes se suponen generados independientemente por
cada nodo con longitudes independientes seleccionadas de una distribución exponencial.
Luego  se  suma  simplemente  las  frecuencias  de  arribos.  De  los  enlaces  previos  a
aquellos que entran al concentrador por el puerto de entrada, tratándolos como si fuesen
generados por terminales equivalentes.

Resulta así:

Comunicaciones – AAAsssiiigggnnnaaaccciiióóónnn   dddeee   CCCaaapppaaaccciiidddaaaddd   dddeee   CCCaaannnaaallleeesss
Ingeniería en Sistemas de Información

Notar  que  esta  red  resulta  con  un  tiempo  promedio  mayor  que  en  la  topología
estrella. El costo es menor por la eliminación de cuatro largos tramos. Podemos reducir
el  retardo  incrementando  la capacidad.  Puede  suceder  de  que  el  costo  no  crezca  tanto
como  en  la  topología  estrella  y  obtener  tiempos  de  retardos  similares  en  ambas
estructuras.

