COMUNICACIÓN DE DATOS

Año 2025

  HARDWARE DE REDES
  MODELOS DE REFERENCIA

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

Contenido

HARDWARE DE REDES ................................................................................................................................. 3

Redes de área local ......................................................................................................................................... 4

Redes de área metropolitana ......................................................................................................................... 6

Redes de área amplia ..................................................................................................................................... 7

Redes inalámbricas ......................................................................................................................................... 9

Redes domésticas ......................................................................................................................................... 12

Interredes ..................................................................................................................................................... 15

MODELOS DE REFERENCIA ....................................................................................................................... 16

El modelo de referencia OSI ......................................................................................................................... 16

La capa física ............................................................................................................................................. 17

La capa de enlace de datos ...................................................................................................................... 17

La capa de red .......................................................................................................................................... 18

La capa de transporte ............................................................................................................................... 18

La capa de sesión ...................................................................................................................................... 19

La capa de presentación ........................................................................................................................... 19

La capa de aplicación ................................................................................................................................ 19

El modelo de referencia TCP/IP .................................................................................................................... 20

La capa de interred ................................................................................................................................... 20

La capa de transporte ............................................................................................................................... 21

La capa de aplicación ................................................................................................................................ 22

La capa host a red ..................................................................................................................................... 23

Comparación entre los modelos de referencia OSI y TCP/IP ....................................................................... 23

Crítica al modelo OSI y los protocolos .......................................................................................................... 25

Aparición inoportuna ............................................................................................................................... 25

Mala tecnología ........................................................................................................................................ 26

Malas implementaciones ......................................................................................................................... 27

Malas políticas .......................................................................................................................................... 27

Crítica del modelo de referencia TCP/IP ...................................................................................................... 27

Mg. Medín Cristian

  Página | 2

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

HARDWARE DE REDES

     Por  lo  general,  no  hay  una  sola  clasificación  aceptada  en  la  que  se  ajusten  todas  las  redes  de

computadoras, pero hay dos que destacan de manera importante: la tecnología de transmisión y la

escala. Examinaremos cada una a la vez.

     En  un  sentido  amplio,  hay  dos  tipos  de  tecnología  de  transmisión  que  se  utilizan  de  manera

extensa.

     Son las siguientes:

1.  Enlaces de difusión.

2.  Enlaces de punto a punto.

     Las  redes  de  difusión  (broadcast)  tienen  un  solo  canal  de  comunicación,  por  lo  que  todas  las

máquinas  de  la  red  lo  comparten.  Si  una  máquina  envía  un  mensaje  corto  —en  ciertos  contextos

conocido como paquete—, todas las demás lo reciben. Un campo de dirección dentro del paquete

especifica el destinatario. Cuando una máquina recibe un paquete, verifica el campo de dirección. Si

el paquete va destinado a esa máquina, ésta lo procesa; si va destinado a alguna otra, lo ignora.

     En una analogía, imagine a alguien que está parado al final de un corredor con varios cuartos a los

lados y que grita: “Jorge, ven. Te necesito”. Aunque en realidad el grito (paquete) podría haber sido

escuchado (recibido), por muchas personas, sólo Jorge responde (lo procesa). Los demás simplemente

lo ignoran. Otra analogía es la de los anuncios en un aeropuerto que piden a todos los pasajeros del

vuelo 644 se reporten en la puerta 12 para abordar de inmediato.

     Por lo general, los sistemas de difusión también permiten el direccionamiento de un paquete a

todos los destinos utilizando un código especial en el campo de dirección. Cuando se transmite un

paquete con este código, todas las máquinas de la red lo reciben y procesan. Este modo de operación

se  conoce  como  difusión  (broadcasting).  Algunos  sistemas  de  difusión  también  soportan  la

transmisión a un subconjunto de máquinas, algo conocido como multidifusión (multicasting).

     Un esquema posible es la reserva de un bit para indicar la multidifusión. Los bits de dirección n –

1 restantes pueden contener un número de grupo. Cada máquina puede “suscribirse” a alguno o a

todos los grupos. Cuando se envía un paquete a cierto grupo, se distribuye a todas las máquinas que

se suscriben a ese grupo.

     En contraste, las redes punto a punto constan de muchas conexiones entre pares individuales de

máquinas. Para ir del origen al destino, un paquete en este tipo de red podría tener que visitar primero

una o más máquinas intermedias. A menudo es posible que haya varias rutas o longitudes diferentes,

de manera que encontrar las correctas es importante en redes de punto a punto. Por regla general, las

redes más pequeñas localizadas en una misma área geográfica tienden a utilizar la difusión, mientras

Mg. Medín Cristian

  Página | 3

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

que las más grandes suelen ser de punto a punto. La transmisión de punto a punto con un emisor y un

receptor se conoce como unidifusión (unicasting).

     Un criterio alternativo para la clasificación de las redes es su escala. En la figura 1-6 clasificamos

los sistemas de procesadores múltiples por tamaño físico. En la parte superior se muestran las redes

de área personal, que están destinadas para una sola persona. Por ejemplo, una red inalámbrica que

conecta una computadora con su ratón, teclado e impresora, es una red de área personal.

     A continuación de las redes de área personal se encuentran redes más grandes. Se pueden dividir

en redes de área local, de área metropolitana y de área amplia. Por último, la conexión de dos o más

redes se conoce como interred.

     Internet  es  un  ejemplo  bien  conocido  de  una  interred.  La  distancia  es  importante  como  una

clasificación en metros porque se utilizan diferentes técnicas en diferentes escalas.

Redes de área local
     Las redes de área local (conocidas como LANs) son redes de propiedad privada que se encuentran

en un solo edificio o en un campus de pocos kilómetros de longitud. Se utilizan ampliamente para

conectar computadoras personales y estaciones de trabajo en oficinas de una empresa y de fábricas

para compartir recursos (por ejemplo, impresoras) e intercambiar información.

     Las  LANs  son  diferentes  de  otros  tipos  de  redes  en  tres  aspectos:  1)  tamaño;  2)  tecnología  de

transmisión, y 3) topología.

     Las LANs están restringidas por tamaño, es decir, el tiempo de transmisión en el peor de los casos

es limitado y conocido de antemano. El hecho de conocer este límite permite utilizar ciertos tipos de

diseño, lo cual no sería posible de otra manera. Esto también simplifica la administración de la red.

     Las LANs podrían utilizar una tecnología de transmisión que consiste en un cable al cual están

unidas todas las máquinas, como alguna vez lo estuvo parte de las líneas de las compañías telefónicas

Mg. Medín Cristian

  Página | 4

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

en áreas rurales. Las LANs tradicionales se ejecutan a una velocidad de 10 a 100 Mbps, tienen un

retardo bajo (microsegundos o nanosegundos) y cometen muy pocos errores. Las LANs más nuevas

funcionan hasta a 10 Gbps.

     Para las LANs de difusión son posibles varias topologías. La figura 1-7 muestra dos de ellas.

     En una red de bus (es decir, un cable lineal), en cualquier instante al menos una máquina es la

maestra y puede transmitir. Todas las demás máquinas se abstienen de enviar. Cuando se presenta el

conflicto de que dos o más máquinas desean transmitir al mismo tiempo, se requiere un mecanismo

de  arbitraje.  Tal  mecanismo  podría  ser  centralizado  o  distribuido.  Por  ejemplo,  el  IEEE  802.3,

popularmente  conocido  como  Ethernet,  es  una  red  de  difusión  basada  en  bus  con  control

descentralizado, que por lo general funciona de 10 Mbps a 10 Gbps. Las computadoras que están en

una Ethernet pueden transmitir siempre que lo deseen; si dos o más paquetes entran en colisión, cada

computadora espera un tiempo aleatorio y lo intenta de nuevo más tarde.

     Un segundo tipo de sistema de difusión es el de anillo. En un anillo, cada bit se propaga por sí

mismo, sin esperar al resto del paquete al que pertenece. Por lo común, cada bit navega por todo el

anillo  en  el  tiempo  que  le  toma  transmitir  algunos  bits,  a  veces  incluso  antes  de  que  se  haya

transmitido el paquete completo. Al igual que con todos los demás sistemas de difusión, se  requieren

algunas  reglas  para  controlar  los  accesos  simultáneos  al  anillo.  Se  utilizan  varios  métodos,  por

ejemplo, el de que las máquinas deben tomar su turno. El IEEE 802.5 (el token ring de IBM) es una

LAN basada en anillo que funciona a 4 y 16 Mbps. El FDDI es otro ejemplo de una red de anillo.

     Las  redes  de  difusión  se pueden  dividir  aún  más  en  estáticas  y  dinámicas,  dependiendo  de

cómo se asigne el canal. Una asignación estática típica sería dividir el tiempo en intervalos discretos

y utilizar un algoritmo round-robin, permitiendo que cada máquina transmita sólo cuando llegue

su turno. La asignación estática desperdicia capacidad de canal cuando una máquina no tiene nada

Mg. Medín Cristian

  Página | 5

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

que transmitir al llegar su turno, por lo que la mayoría de los sistemas trata de asignar el canal de

forma dinámica (es decir, bajo demanda).

     Los  métodos  de  asignación  dinámica  para  un  canal  común  pueden  ser  centralizados  o

descentralizados. En el método centralizado hay una sola entidad, por ejemplo, una unidad de arbitraje

de  bus,  la  cual  determina  quién  sigue.  Esto  se  podría  hacer  aceptando  solicitudes  y  tomando

decisiones de acuerdo con algunos algoritmos internos. En el método descentralizado de asignación

de canal no hay una entidad central; cada máquina debe decidir por sí misma cuándo transmitir. Usted

podría pensar que esto siempre conduce al caos, pero no es así. Más adelante estudiaremos muchos

algoritmos designados para poner orden y evitar el caos potencial.

Redes de área metropolitana
     Una red de área metropolitana (MAN) abarca una ciudad. El ejemplo más conocido de una

MAN es la red de televisión por cable disponible en muchas ciudades. Este sistema creció a partir de

los primeros sistemas de antena comunitaria en áreas donde la recepción de la televisión al aire era

pobre. En dichos sistemas se colocaba una antena grande en la cima de una colina cercana y la señal

se canalizaba a las casas de los suscriptores.

     Al principio eran sistemas diseñados de manera local con fines específicos. Después las compañías

empezaron a pasar a los negocios, y obtuvieron contratos de los gobiernos de las ciudades para cablear

toda una ciudad. El siguiente paso fue la programación de televisión e incluso canales designados

únicamente para cable. Con frecuencia, éstos emitían programas de un solo tema, como sólo noticias,

deportes, cocina, jardinería, etcétera. Sin embargo, desde su inicio y hasta finales de la década de

1990, estaban diseñados únicamente para la recepción de televisión.

     A partir de que Internet atrajo una audiencia masiva, los operadores de la red de TV por cable se

dieron cuenta de que con algunos cambios al sistema, podrían proporcionar servicio de Internet de

dos  vías en las partes sin uso del espectro. En ese punto, el sistema de TV por cable empezaba a

transformarse de una forma de distribución de televisión a una red de área metropolitana. Para que se

dé una idea, una MAN podría verse como el sistema que se muestra en la figura 1-8, donde se aprecia

que  las  señales  de  TV  e  Internet  se  alimentan  hacia  un  amplificador  head  end  para  enseguida

transmitirse a las casas de las personas.

Mg. Medín Cristian

  Página | 6

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

     La televisión por cable no es solamente una MAN. Desarrollos recientes en el acceso inalámbrico

a alta velocidad a Internet dieron como resultado otra MAN, que se estandarizó como IEEE 802.16.

Redes de área amplia
     Una red de área amplia (WAN), abarca una gran área geográfica, con frecuencia un país o un

continente. Contiene un conjunto de máquinas diseñado para programas (es decir, aplicaciones) de

usuario. Los hosts están conectados por una subred de comunicación, o simplemente subred, para

abreviar. Los clientes son quienes poseen a los hosts (es decir, las computadoras personales de los

usuarios), mientras que, por lo general, las compañías telefónicas o los proveedores de servicios de

Internet poseen y operan la subred de comunicación. La función de una subred es llevar mensajes de

un host a otro, como lo hace el sistema telefónico con las palabras del que habla al que escucha. La

separación  de  los  aspectos  de  la  comunicación  pura  de  la  red  (la  subred)  de  los  aspectos  de  la

aplicación (los hosts), simplifica en gran medida todo el diseño de la red.

     En la mayoría de las redes de área amplia la subred consta de dos componentes distintos:

líneas de transmisión y elementos de conmutación. Las líneas de transmisión mueven bits entre

máquinas. Pueden estar hechas de cable de cobre, fibra óptica o, incluso, radioenlaces. Los elementos

de conmutación son computadoras especializadas que conectan tres o más líneas de transmisión.

     Cuando los datos llegan a una línea de entrada, el elemento de conmutación debe elegir una línea

de  salida en  la  cual  reenviarlos.  Estas  computadoras  de  conmutación  reciben  varios  nombres;

conmutadores y enrutadores son los más comunes.

Mg. Medín Cristian

  Página | 7

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

     En este modelo, que se muestra en la figura 1-9, cada host está conectado frecuentemente a una

LAN en la que existe un enrutador, aunque en algunos casos un host puede estar conectado de manera

directa a un enrutador. El conjunto de líneas de comunicación y enrutadores (pero no de hosts) forma

la subred.

     A continuación, se presenta un breve comentario acerca del término “subred”. Originalmente, su

único significado era el conjunto de enrutadores y líneas de comunicación que movía paquetes del

host  de  origen  al  de  destino.  Sin  embargo,  algunos  años  más  tarde  también  adquirió  un  segundo

significado junto con el direccionamiento de redes. Desgraciadamente, no existe una alternativa de

amplio uso con respecto a su significado inicial por lo que, con algunas reservas, utilizaremos este

término en ambos sentidos. El contexto dejará en claro su significado.

     En la mayoría de las WANs, la red contiene numerosas líneas de transmisión, cada una de las

cuales conecta un par de enrutadores. Si dos enrutadores que no comparten una línea de transmisión

quieren conectarse, deberán hacerlo de manera indirecta, a través de otros enrutadores. Cuando un

paquete  es  enviado  desde  un  enrutador  a  otro  a  través  de  uno  o  más  enrutadores  intermedios,  el

paquete se recibe en cada enrutador intermedio en su totalidad, se almacena ahí hasta que la línea de

salida requerida esté libre y, por último, se reenvía. Una subred organizada a partir de este principio

se conoce como subred de almacenamiento y reenvío (store and forward) o de conmutación de

paquetes. Casi todas las redes de área amplia (excepto las que utilizan satélites) tienen subredes de

almacenamiento y reenvío. Cuando los paquetes son pequeños y tienen el mismo tamaño, se les llama

celdas.

     En general, cuando un proceso de cualquier host tiene un mensaje que se va a enviar a un proceso

de algún otro host, el host emisor divide primero el mensaje en paquetes, los cuales tienen un número

Mg. Medín Cristian

  Página | 8

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

de secuencia. Estos paquetes se envían entonces por la red de uno en uno en una rápida sucesión. Los

paquetes se transportan de forma individual a través de la red y se depositan en el host receptor, donde

se reensamblan en el mensaje original y se entregan al proceso receptor. En la figura 1-10 se ilustra

un flujo de paquetes correspondiente a algún mensaje inicial.

     En esta figura todos los paquetes siguen la ruta ACE en vez de la ABDE o ACDE. En algunas

redes  todos  los  paquetes  de  un  mensaje  determinado  deben  seguir  la  misma  ruta;  en  otras,  cada

paquete se enruta por separado. Desde luego, si ACE es la mejor ruta, todos los paquetes se podrían

enviar a través de ella, incluso si cada paquete se enruta de manera individual.

     Las decisiones de enrutamiento se hacen de manera local. Cuando un paquete llega al enrutador

A, éste debe decidir si el paquete se enviará hacia B o hacia C. La manera en que el enrutador

A toma esa decisión se conoce como algoritmo de enrutamiento.

     No todas las WANs son de conmutación de paquetes. Una segunda posibilidad para una WAN es

un sistema satelital. Cada enrutador tiene una antena a través de la cual puede enviar y recibir.

     Todos los enrutadores pueden escuchar la salida desde el satélite  y, en algunos casos, también

pueden  escuchar  las  transmisiones  de  los  demás  enrutadores  hacia  el  satélite.  Algunas  veces  los

enrutadores están conectados a una subred de punto a punto elemental, y sólo algunos de ellos tienen

una antena de satélite. Por naturaleza, las redes satelitales son de difusión y son más útiles cuando la

propiedad de difusión es importante.

Redes inalámbricas
     La comunicación inalámbrica digital no es una idea nueva. A principios de 1901, el físico italiano

Guillermo Marconi demostró un telégrafo inalámbrico desde un barco a tierra utilizando el código

Morse (después de todo, los puntos y rayas son binarios). Los sistemas inalámbricos digitales de la

actualidad tienen un mejor desempeño, pero la idea básica es la misma.

Mg. Medín Cristian

  Página | 9

     Como  primera  aproximación,  las  redes  inalámbricas  se  pueden  dividir  en  tres  categorías

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

principales:

1.  Interconexión de sistemas.

2.  LANs inalámbricas.

3.  WANs inalámbricas.

     La  interconexión  de  sistemas  se  refiere  a  la  interconexión  de  componentes  de  una

computadora que utiliza radio de corto alcance. La mayoría de las computadoras tiene un monitor,

teclado, ratón e impresora, conectados por cables a la unidad central. Son tantos los usuarios nuevos

que tienen dificultades para conectar todos los cables en los enchufes correctos (aun cuando suelen

estar codificados por colores) que la mayoría de los proveedores de computadoras ofrece la opción

de enviar a un técnico  a la casa del usuario para que realice esta tarea. En consecuencia, algunas

compañías se reunieron para diseñar una red inalámbrica de corto alcance llamada Bluetooth para

conectar  sin  cables  estos  componentes.  Bluetooth  también  permite  conectar  cámaras  digitales,

auriculares,  escáneres  y  otros  dispositivos  a  una  computadora  con  el  único  requisito  de  que  se

encuentren dentro del alcance de la red. Sin cables, sin instalación de controladores, simplemente se

colocan,  se  encienden  y  funcionan.  Para  muchas  personas,  esta  facilidad  de  operación  es  algo

grandioso.

     En la forma más sencilla, las redes de interconexión de sistemas utilizan el paradigma del maestro

y el esclavo de la figura 1-11(a). La unidad del sistema es, por lo general, el maestro que trata al ratón,

al teclado, etcétera, como a esclavos. El maestro le dice a los esclavos qué direcciones utilizar, cuándo

pueden difundir, durante cuánto tiempo pueden transmitir, qué frecuencias pueden utilizar, etcétera.

     El siguiente paso en la conectividad inalámbrica son las LANs inalámbricas. Son sistemas en los

que  cada  computadora  tiene  un  módem  de  radio  y  una  antena  mediante  los  que  se  puede

comunicar  con  otros  sistemas.  En  ocasiones,  en  el  techo  se  coloca  una  antena  con  la  que  las

máquinas se comunican, como se ilustra en la figura 1-11(b). Sin embargo, si los sistemas están lo

suficientemente cerca, se pueden comunicar de manera directa entre sí en una configuración de igual

a igual.

Mg. Medín Cristian

  Página | 10

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

     Las LANs inalámbricas se están haciendo cada vez más comunes en casas y oficinas pequeñas,

donde instalar Ethernet se considera muy problemático, así como en oficinas ubicadas en edificios

antiguos, cafeterías de empresas, salas de conferencias y otros lugares. Existe un estándar para las

LANs inalámbricas, llamado IEEE 802.11, que la mayoría de los sistemas implementa y que se ha

extendido ampliamente.

     El tercer tipo de red inalámbrica se utiliza en sistemas de área amplia. La red de radio utilizada

para teléfonos celulares es un ejemplo de un sistema inalámbrico de banda ancha baja. Este sistema

ha pasado por tres generaciones. La primera era analógica y sólo para voz. La segunda era digital y

sólo para voz. La tercera generación es digital y es tanto para voz como para datos. En cierto sentido,

las redes inalámbricas celulares son como las LANs inalámbricas, excepto por que las distancias

implicadas  son  mucho  más  grandes  y  las  tasas  de  bits  son  mucho  más  bajas.  Las  LANs

inalámbricas pueden funcionar a tasas de hasta 50 Mbps en distancias de decenas de metros.  Los

sistemas  celulares  funcionan  debajo  de  1  Mbps,  pero  la  distancia  entre  la  estación  base  y  la

computadora o teléfono se mide en kilómetros más que en metros.

     Además de estas redes de baja velocidad, también se han desarrollado las redes inalámbricas

de área amplia con alto ancho de banda. El enfoque inicial es el acceso inalámbrico a Internet a

alta velocidad, desde los hogares y las empresas, dejando a un lado el sistema telefónico. Este servicio

se suele llamar servicio de distribución local multipuntos. Lo estudiaremos más adelante. También se

ha desarrollado un estándar para éste, llamado IEEE 802.16.

     La mayoría de las redes inalámbricas se enlaza a la red alámbrica en algún punto para proporcionar

acceso  a  archivos,  bases  de  datos  e  Internet.  Hay  muchas  maneras  de  efectuar  estas  conexiones,

Mg. Medín Cristian

  Página | 11

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

dependiendo de las circunstancias. Por ejemplo, en la figura 1-12(a) mostramos un aeroplano con una

serie de personas que utilizan módems y los teléfonos de los respaldos para llamar a la oficina. Cada

llamada es independiente de las demás. Sin embargo, una opción mucho más eficiente es la LAN

dentro del avión de la figura 1-12(b), donde cada asiento está equipado con un conector Ethernet al

cual  los  pasajeros  pueden  acoplar  sus  computadoras.  El  avión  tiene  un  solo  enrutador,  el  cual

mantiene un enlace de radio con algún enrutador que se encuentre en tierra, y cambia de enrutador

conforme avanza el vuelo. Esta configuración es una LAN tradicional, excepto porque su conexión

al mundo exterior se da mediante un enlace por radio en lugar de una línea cableada.

     Muchas personas creen que lo inalámbrico es la onda del futuro (por ejemplo, Bi y cols., 2001;

Leeper, 2001;  Varshey  y Vetter, 2000) pero se ha escuchado una voz disidente. Bob Metcalfe, el

inventor  de  Ethernet,  ha  escrito:  “Las  computadoras  inalámbricas  móviles  son  como  los  baños

portátiles  sin  cañería:  bacinicas  portátiles.  Serán  muy  comunes  en  los  vehículos,  en  sitios  en

construcción  y  conciertos  de  rock.  Mi  consejo  es  que  coloque  cables  en  su  casa  y  se  quede  ahí”

(Metcalfe, 1995).

La  historia  podría  colocar  esta  cita  en  la  misma  categoría  que  la  explicación  de  T.J.  Watson,

presidente de IBM en 1945, de por qué esta empresa no entraba en el negocio de las computadoras:

“Cuatro o cinco computadoras deberán ser suficientes para todo el mundo hasta el año 2000”.

Redes domésticas
     La conectividad doméstica está en el horizonte. La idea fundamental es que en el futuro la mayoría

de los hogares estarán preparados para conectividad de redes. Cualquier dispositivo del hogar será

capaz de comunicarse con todos los demás dispositivos y todos podrán accederse por Internet. Éste

es uno de esos conceptos  visionarios que nadie solicitó (como los controles remotos de TV o los

teléfonos celulares), pero una vez que han llegado nadie se puede imaginar cómo habían podido vivir

Mg. Medín Cristian

  Página | 12

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

sin ellos. Muchos dispositivos son capaces de estar conectados en red. Algunas de las categorías más

evidentes son las siguientes:

1.  Computadoras (de escritorio, portátiles, PDAs, periféricos compartidos).

2.  Entretenimiento (TV, DVD, VCR, videocámara, cámara fotográfica, estereofónicos, MP3).

3.  Telecomunicaciones (teléfono, teléfono móvil, intercomunicadores, fax).

4.  Aparatos  electrodomésticos  (horno  de  microondas,  refrigerador,  reloj,  horno,  aire

acondicionado, luces).

5.  Telemetría (metro utilitario, alarma contra fuego y robo, termostato, cámaras inalámbricas).

     La  conectividad  de  computadoras  domésticas  ya  está  aquí,  aunque  limitada.  Muchas  casas  ya

cuentan con un dispositivo para conectar varias computadoras para una conexión rápida a Internet.

     El entretenimiento por red aún no existe, pero cuanto más y más música y películas se puedan

descargar de Internet, habrá más demanda para que los equipos de audio y las televisiones se conecten

a Internet. Incluso las personas desearán compartir sus propios vídeos con amigos y familiares, por

lo que deberá haber una conexión en ambos sentidos. Los dispositivos de telecomunicaciones ya están

conectados  al mundo exterior, pero pronto serán  digitales  y tendrán  capacidad de funcionar sobre

Internet.  Un  hogar  promedio  tal  vez  tiene  una  docena  de  relojes  (los  de  los  aparatos

electrodomésticos), y todos se tienen que reajustar dos veces al año cuando inicia y termina el tiempo

de ahorro de luz de día (horario de verano). Si todos los relojes estuvieran conectados a Internet, ese

reajuste se haría en forma automática. Por último, el monitoreo remoto de la casa y su contenido es

el probable ganador. Es muy factible que muchos padres deseen invertir en monitorear con sus PDAs

a sus bebés dormidos cuando van a cenar fuera de casa, aun cuando contraten a una niñera. Si bien

podemos imaginar una red separada para cada área de aplicación, la integración de todas en una sola

red es probablemente una mejor idea.

     La  conectividad  doméstica  tiene  algunas  propiedades  diferentes  a  las  de  otro  tipo  de  redes.

Primero, la red y los dispositivos deben ser fáciles de instalar. El autor ha instalado numerosas piezas

de  hardware  y  software  en  varias  computadoras  durante varios  años  con  resultados  diferentes.  Al

realizar una serie de llamadas telefónicas al personal de soporte técnico del proveedor por lo general

recibió respuestas como: 1) Lea el manual; 2) Reinicie la computadora; 3) Elimine todo el hardware

y software, excepto los nuestros, y pruebe de nuevo; 4) Descargue de nuestro sitio Web el controlador

más reciente y, si todo eso falla, 5) Reformatee el disco duro y reinstale Windows desde el CD-ROM.

Decirle al comprador de un refrigerador con capacidad de Internet que descargue e instale una nueva

versión del sistema operativo del refrigerador, no conduce a tener clientes contentos. Los usuarios de

computadoras están acostumbrados a soportar productos que no funcionan; los clientes que compran

Mg. Medín Cristian

  Página | 13

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

automóviles,  televisiones  y  refrigeradores  son  mucho  menos  tolerantes.  Esperan  productos  que

trabajen al 100% desde que se compran.

     Segundo, la red y los dispositivos deben estar plenamente probados en operación. Los equipos de

aire acondicionado solían tener una perilla con cuatro parámetros: OFF, LOW, MEDIUM y HIGH

(apagado, bajo, medio, alto). Ahora tienen manuales de 30 páginas. Una vez que puedan conectarse

en red, no se le haga extraño que tan sólo el capítulo de seguridad tenga 30 páginas. Esto estará más

allá de la comprensión de prácticamente todos los usuarios.

     Tercero, el precio bajo es esencial para el éxito. Muy pocas personas, si no es que ninguna, pagarán

un precio adicional de $100 por un termostato con capacidad de Internet, debido a que no considerarán

que monitorear la temperatura de sus casas desde sus trabajos sea algo importante. Tal vez por $20 sí

lo comprarían.

     Cuarto, la principal aplicación podría implicar multimedia, por lo que la red necesita capacidad

suficiente. No hay mercado para televisiones conectadas a Internet que proyecten películas inseguras

a una resolución de 320 × 240 píxeles y 10 cuadros por segundo. Fast Ethernet, el caballo de batalla

en la mayoría de las oficinas, no es bastante buena para multimedia. En consecuencia, para que las

redes domésticas lleguen a ser productos masivos en el mercado, requerirán mejor desempeño que el

de las redes de oficina actuales, así como precios más bajos.

     Quinto, se podría empezar con uno o dos dispositivos y expandir de manera gradual el alcance de

la red. Esto significa que no habrá problemas con el formato. Decir a los consumidores que adquieran

periféricos con interfaces IEEE 1394 (FireWire) y años después retractarse y decir que USB 2.0 es la

interfaz  del  mes,  es  hacer  clientes  caprichosos.  La  interfaz  de  red  tendrá  que  permanecer  estable

durante muchos años; el cableado (si lo hay) deberá permanecer estable durante décadas.

     Sexto, la seguridad y la confianza serán muy importantes. Perder algunos archivos por un virus de

correo electrónico es una cosa; que un ladrón desarme su sistema de seguridad desde su PDA y luego

saquee su casa es algo muy diferente.

     Una pregunta interesante es si las redes domésticas serán alámbricas o inalámbricas. La mayoría

de los hogares ya tiene seis redes instaladas: electricidad, teléfono, televisión por cable, agua, gas y

alcantarillado.  Agregar  una  séptima  durante  la  construcción  de  una  casa  no  es  difícil,  pero

acondicionar  las  casas  existentes  para  agregar  dicha  red  es  costoso.  Los  costos  favorecen  la

conectividad inalámbrica, pero la seguridad favorece la conectividad alámbrica. El problema

con la conectividad inalámbrica es que las ondas de radio que utiliza traspasan las paredes con mucha

facilidad. No a todos les gusta la idea de que cuando vaya a imprimir, se tope con la conexión de su

vecino y pueda leer el correo electrónico de éste.

Mg. Medín Cristian

  Página | 14

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

     Para abreviar, la conectividad doméstica ofrece muchas oportunidades y retos. La mayoría de ellos

se relaciona con la necesidad de que sean fáciles de manejar, confiables y seguros, en particular en

manos de usuarios no técnicos, y que al mismo tiempo proporcionen alto desempeño a bajo costo.

Interredes
     Existen muchas redes en el mundo, a veces con hardware y software diferentes. Con frecuencia,

las personas conectadas a una red desean comunicarse con personas conectadas a otra red diferente.

     La  satisfacción  de  este  deseo  requiere  que  se  conecten  diferentes  redes,  con  frecuencia

incompatibles,  a  veces  mediante  máquinas  llamadas  puertas  de  enlace  (gateways)  para  hacer  la

conexión y proporcionar la traducción necesaria, tanto en términos de hardware como de software.

Un conjunto de redes interconectadas se llama interred.

     Una forma común de interred es el conjunto de LANs conectadas por una WAN. De hecho, si

tuviéramos que reemplazar la etiqueta “subred” en la figura 1-9 por “WAN”, no habría nada más que

cambiar en la figura. En este caso, la única diferencia técnica real entre una subred y una WAN es si

hay hosts presentes. Si el sistema que aparece en el área gris contiene solamente enrutadores, es

una subred; si contiene enrutadores y hosts, es una WAN. Las diferencias reales se relacionan con

la propiedad y el uso.

     Subredes,  redes  e  interredes  con  frecuencia  se  confunden.  La  subred  tiene  más  sentido  en  el

contexto  de  una  red  de  área  amplia,  donde  se  refiere  a  un  conjunto  de  enrutadores  y  líneas  de

comunicación poseídas por el operador de redes. Como una analogía, el sistema telefónico consta de

oficinas de conmutación telefónica que se conectan entre sí mediante líneas de alta velocidad, y a  los

hogares  y  negocios,  mediante  líneas  de  baja  velocidad.  Estas  líneas  y  equipos,  poseídas  y

administradas por la compañía de teléfonos, forman la subred del sistema telefónico. Los teléfonos

mismos (los hosts en esta analogía) no son parte de la subred. La combinación de una subred y sus

hosts forma una red. En el caso de una LAN, el cable y los hosts forman la red. En realidad, ahí

no hay una subred.

     Una interred se forma cuando se interconectan redes diferentes. Desde nuestro punto de vista,

al  conectar  una  LAN  y  una  WAN  o  conectar  dos  LANs  se  forma  una  interred,  pero  existe  poco

acuerdo en la industria en cuanto a la terminología de esta área. Una regla de oro es que si varias

empresas  pagaron  por  la  construcción  de  diversas  partes  de  la  red  y  cada  una  mantiene  su  parte,

tenemos una interred más que una sola red. Asimismo, si la terminología subyacente es diferente en

partes diferentes (por ejemplo, difusión y punto a punto), probablemente tengamos dos redes.

Mg. Medín Cristian

  Página | 15

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

MODELOS DE REFERENCIA

     Ahora que hemos visto en teoría las redes con capas, es hora de ver algunos ejemplos. En las dos

secciones siguientes veremos dos arquitecturas de redes importantes: los modelos de referencia OSI

y TCP/IP. Aunque los protocolos asociados con el modelo OSI ya casi no se usan, el modelo en sí es

muy general y aún es válido, y las características tratadas en cada capa aún son muy importantes. El

modelo  TCP/IP  tiene  las  propiedades  opuestas:  el  modelo  en  sí  no  se  utiliza  mucho  pero  los

protocolos sí. Por estas razones analizaremos con detalle ambos modelos. Además, a veces podemos

aprender más de las fallas que de los aciertos.

El modelo de referencia OSI
     El modelo OSI se muestra en la figura 1-20 (sin el medio físico). Este modelo está basado en una

propuesta desarrollada por la ISO (Organización Internacional de Estándares) como un primer paso

hacia  la  estandarización  internacional  de  los  protocolos  utilizados  en  varias  capas  (Day  y

Zimmermann, 1983). Fue revisado en 1995 (Day, 1995). El modelo se llama OSI (Interconexión de

Sistemas  Abiertos)  de  ISO  porque  tiene  que  ver  con  la  conexión  de  sistemas  abiertos,  es  decir,

sistemas  que  están  abiertos  a  la  comunicación  con  otros  sistemas.  Para  abreviar,  lo  llamaremos

modelo OSI.

Mg. Medín Cristian

  Página | 16

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

     El modelo OSI tiene siete capas. Podemos resumir brevemente los principios que se aplicaron

para llegar a dichas capas:

1.  Una capa se debe crear donde se necesite una abstracción diferente.

2.  Cada capa debe realizar una función bien definida.

3.  La función de cada capa se debe elegir con la intención de definir protocolos estandarizados

internacionalmente.

4.  Los límites de las capas se deben elegir a fin de minimizar el flujo de información a través de

las interfaces.

5.  La cantidad de capas debe ser suficientemente grande para no tener que agrupar funciones

distintas  en  la  misma  capa  y  lo  bastante  pequeña  para  que  la  arquitectura  no  se  vuelva

inmanejable.

     A continuación, analizaremos una por una cada capa del modelo, comenzando con la capa inferior.

Observe que el modelo OSI no es en sí una arquitectura de red, debido a que no especifica los

servicios y protocolos exactos que se utilizarán en cada capa. Sólo indica lo que debe hacer cada

capa. Sin embargo, ISO también ha producido estándares para todas las capas, aunque éstos no son

parte  del  modelo  de referencia  mismo.  Cada  uno  se  ha publicado  como  un  estándar  internacional

separado.

La capa física
     En esta capa se lleva a cabo la transmisión de bits puros a través de un canal de comunicación.

Los aspectos del diseño implican asegurarse de que cuando un lado envía un bit 1, éste se reciba en

el otro lado como tal, no como bit 0. Las preguntas típicas aquí son: ¿cuántos voltios se deben emplear

para  representar  un  1  y  cuántos  para  representar  un  0?,  ¿cuántos  nanosegundos  dura  un  bit?,  ¿la

transmisión se debe llevar a cabo en ambas direcciones  al mismo tiempo?, ¿cómo se establece la

conexión inicial y cómo se finaliza cuando ambos lados terminan?, ¿cuántos pines tiene un conector

de red y para qué se utiliza cada uno? Los aspectos de diseño tienen que ver mucho con interfaces

mecánicas, eléctricas y de temporización, además del medio físico de transmisión, que está bajo la

capa física.

La capa de enlace de datos
     La  tarea  principal  de  esta  capa  es  transformar  un  medio  de  transmisión  puro  en  una  línea  de

comunicación que, al llegar a la capa de red, aparezca libre de errores de transmisión. Logra esta tarea

haciendo que el emisor fragmente los datos de entrada en tramas de datos (típicamente, de algunos

cientos o miles de bytes) y transmitiendo las tramas de manera secuencial. Si el servicio es confiable,

Mg. Medín Cristian

  Página | 17

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

el receptor confirma la recepción correcta de cada trama devolviendo una trama de confirmación

de recepción.

     Otra cuestión que surge en la capa de enlace de datos (y en la mayoría de las capas superiores) es

cómo hacer que un transmisor rápido no sature de datos a un receptor lento. Por lo general se necesita

un mecanismo de regulación de tráfico que indique al transmisor cuánto espacio de búfer tiene el

receptor  en  ese  momento.  Con  frecuencia,  esta  regulación  de  flujo  y  el  manejo  de  errores  están

integrados.

     Las redes de difusión tienen un aspecto adicional en la capa de enlace de datos: cómo controlar el

acceso al canal compartido. Una subcapa especial de la capa de enlace de datos, la subcapa de control

de acceso al medio, se encarga de este problema.

La capa de red
     Esta capa controla las operaciones de la subred. Un aspecto clave del diseño es determinar cómo

se enrutan los paquetes desde su origen a su destino. Las rutas pueden estar basadas en tablas estáticas

(enrutamiento estático) codificadas en la red y que rara vez cambian. Si hay demasiados paquetes en

la subred al mismo tiempo, se interpondrán en el camino unos y otros, lo que provocará que se formen

cuellos de botella. La responsabilidad de controlar esta congestión también pertenece a la capa de

red, aunque esta responsabilidad también puede ser compartida por la capa de transmisión. De manera

más general, la calidad del servicio proporcionado (retardo, tiempo de tránsito, inestabilidad, etcétera)

también corresponde a la capa de red. Cuando un paquete tiene que viajar de una red a otra para llegar

a  su  destino,  pueden  surgir  muchos  problemas.  El  direccionamiento  utilizado  por  la  segunda  red

podría  ser  diferente  del  de  la  primera.  La  segunda  podría  no  aceptar  todo  el  paquete  porque  es

demasiado largo. Los protocolos podrían ser diferentes, etcétera. La capa de red tiene que resolver

todos estos problemas para que las redes heterogéneas se interconecten.

     En las redes de difusión, el problema de enrutamiento es simple, por lo que la capa de red a veces

es delgada o, en ocasiones, ni siquiera existe.

La capa de transporte
     La función básica de esta capa es aceptar los datos provenientes de las capas superiores, dividirlos

en unidades más pequeñas si es necesario, pasar éstas a la capa de red y asegurarse de que todas las

piezas lleguen correctamente al otro extremo. Además, todo esto se debe hacer con eficiencia y de

manera que aísle a las capas superiores de los cambios inevitables en la tecnología del hardware.

     La capa de transporte también determina qué tipo de servicio proporcionar a la capa de sesión

y, finalmente, a los usuarios de la red. El tipo de conexión de transporte más popular es un canal

Mg. Medín Cristian

  Página | 18

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

punto  a  punto  libre  de  errores  que  entrega  mensajes  o  bytes  en  el  orden  en  que  se  enviaron.  Sin

embargo, otros tipos de servicio de transporte posibles son la transportación de mensajes aislados,

que no garantiza el orden de entrega, y la difusión de mensajes a múltiples destinos. El tipo de servicio

se determina cuando se establece la conexión. (Como observación, es imposible alcanzar un canal

libre de errores; lo que se quiere dar a entender con este término es que la tasa de error es tan baja

que se puede ignorar en la práctica.)

     La capa de transporte es una verdadera conexión de extremo a extremo, en toda la ruta desde el

origen hasta el destino. En otras  palabras, un programa en la máquina de origen lleva a cabo una

conversación con un programa similar en la máquina de destino, usando los encabezados de mensaje

y los mensajes de control. En las capas inferiores, los protocolos operan entre cada máquina y sus

vecinos inmediatos, y no entre las máquinas de los extremos, la de origen y la de destino, las cuales

podrían estar separadas por muchos enrutadores. En la figura 1-20 se muestra la diferencia entre las

capas 1 a 3, que están encadenadas, y las capas 4 a 7, que operan de extremo a extremo.

La capa de sesión
     Esta capa permite que los usuarios de máquinas diferentes establezcan sesiones entre ellos. Las

sesiones ofrecen varios servicios, como el control de diálogo (dar seguimiento de a quién le toca

transmitir),  administración  de  token  (que  impide  que  las  dos  partes  traten  de  realizar  la  misma

operación  crítica  al  mismo  tiempo)  y  sincronización  (la  adición  de  puntos  de  referencia  a

transmisiones largas para permitirles continuar desde donde se encontraban después de una caída).

La capa de presentación
     A diferencia de las capas inferiores, a las que les corresponde principalmente mover bits, a la capa

de presentación le corresponde la sintaxis y la semántica de la información transmitida. A fin de que

las computadoras con diferentes representaciones de datos se puedan comunicar, las estructuras de

datos que se intercambiarán se pueden definir de una manera abstracta, junto con una codificación

estándar  para  su  uso  “en  el  cable”.  La  capa  de  presentación  maneja  estas  estructuras  de  datos

abstractas y permite definir e intercambiar estructuras de datos de un nivel más alto (por ejemplo,

registros bancarios).

La capa de aplicación
     Esta capa contiene varios protocolos que los usuarios requieren con frecuencia. Un protocolo de

aplicación de amplio uso es HTTP (Protocolo de Transferencia de Hipertexto), que es la base de

World Wide Web. Cuando un navegador desea una página Web, utiliza este protocolo para enviar al

Mg. Medín Cristian

  Página | 19

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

servidor el nombre de dicha página. A continuación, el servidor devuelve la página. Otros protocolos

de aplicación se utilizan para la transferencia de archivos, correo electrónico y noticias en la red.

El modelo de referencia TCP/IP
     Tratemos ahora el modelo de referencia usado en la abuela de todas las redes de computadoras de

área amplia, ARPANET, y en su sucesora, la Internet mundial. Aunque daremos más adelante una

breve historia de ARPANET, es útil mencionar algunos de sus aspectos ahora. ARPANET fue una

red de investigación respaldada por el DoD (Departamento de Defensa de Estados Unidos).

     Con el tiempo, conectó cientos de universidades e instalaciones gubernamentales mediante líneas

telefónicas alquiladas. Posteriormente, cuando se agregaron redes satelitales y de radio, los protocolos

existentes  tuvieron  problemas  para  interactuar  con  ellas,  por  lo  que  se  necesitaba  una  nueva

arquitectura de referencia. De este modo, la capacidad para conectar múltiples redes en una manera

sólida fue una de las principales metas de diseño desde sus inicios. Más tarde, esta arquitectura se

llegó a conocer como el modelo de referencia TCP/IP, de acuerdo con sus dos protocolos primarios.

Su primera definición fue en (Cerf y Kahn, 1974). Posteriormente se definió en (Leiner y cols., 1985).

La filosofía del diseño que respalda al modelo se explica en (Clark, 1988).

     Ante el temor del DoD de que algunos de sus valiosos hosts, enrutadores y puertas de enlace de

interredes explotaran en un instante, otro objetivo fue que la red pudiera sobrevivir a la pérdida de

hardware de la subred, sin que las conversaciones existentes se interrumpieran. En otras palabras, el

DoD quería que las conexiones se mantuvieran intactas en tanto las máquinas de origen y destino

estuvieran  funcionando,  aunque  algunas  de  las  máquinas  o  líneas  de  transmisión  intermedias

quedaran fuera de operación repentinamente. Además, se necesitaba una arquitectura flexible debido

a  que  se  preveían  aplicaciones  con  requerimientos  divergentes,  desde  transferencia  de  archivos  a

transmisión de palabras en tiempo real.

La capa de interred
     Todos  estos  requerimientos  condujeron  a  la  elección  de  una  red  de  conmutación  de  paquetes

basada en una capa de interred no orientada a la conexión. Esta capa, llamada capa de interred, es

la pieza clave que mantiene unida a la arquitectura. Su trabajo es permitir que los hosts inyecten

paquetes  dentro  de  cualquier  red  y  que  éstos  viajen  a  su  destino  de  manera  independiente

(podría ser en una red diferente). Tal vez lleguen en un orden diferente al que fueron enviados, en

cuyo caso las capas más altas deberán ordenarlos, si se desea una entrega ordenada. Observe que aquí

el concepto “interred” se utiliza en un sentido genérico, aun cuando esta capa se presente en Internet.

Mg. Medín Cristian

  Página | 20

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

     Aquí  la  analogía  es  con  el  sistema  de  correo  tradicional.  Una  persona  puede  depositar  una

secuencia  de  cartas  internacionales  en  un  buzón  y,  con  un  poco  de  suerte,  la  mayoría  de  ellas  se

entregará en la dirección correcta del país de destino. Es probable que, durante el trayecto, las cartas

viajen a través de una o más puertas de enlace de correo internacional, pero esto es transparente para

los usuarios. Además, para los usuarios también es transparente el hecho de que cada país (es decir,

cada red) tiene sus propios timbres postales, tamaños preferidos de sobre y reglas de entrega.

     La capa de interred define un paquete de formato y protocolo oficial llamado IP (Protocolo de

Internet). El  trabajo de la capa de interred es entregar paquetes IP al destinatario. Aquí,  el

enrutamiento de paquetes es claramente el aspecto principal, con el propósito de evitar la congestión.

Por  estas  razones  es  razonable  decir  que  la  capa  de  interred  del  modelo  TCP/IP  es  similar  en

funcionalidad a la capa de red del modelo OSI. La figura 1-21 muestra esta correspondencia.

La capa de transporte
     La capa que está arriba de la capa de interred en el modelo TCP/IP se llama capa de transporte.

Está diseñada para permitir que las entidades iguales en los hosts de origen y destino puedan llevar a

cabo  una  conversación,  tal  como  lo  hace  la  capa  de  transporte  OSI.  Aquí  se  han  definido  dos

protocolos  de  transporte  de  extremo  a  extremo.  El  primero,  TCP  (Protocolo  de  Control  de

Transmisión), es un protocolo confiable, orientado a la conexión, que permite que un flujo de bytes

que se origina en una máquina se entregue sin errores en cualquier otra máquina en la interred. Divide

el flujo de bytes entrantes en mensajes discretos y pasa cada uno de ellos a la capa de interred. En el

destino, el proceso TCP receptor reensambla en el flujo de salida los mensajes recibidos. TCP también

maneja el control de flujo para asegurarse de que un emisor rápido no sature a un receptor lento con

más mensajes de los que puede manejar.

Mg. Medín Cristian

  Página | 21

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

     El segundo protocolo de esta capa, UDP (Protocolo de Datagrama de Usuario), es un protocolo

no  confiable  y  no  orientado  a  la  conexión  para  aplicaciones  que  no  desean  la  secuenciación  o  el

control de flujo de TCP y que desean proporcionar el suyo. También tiene un amplio uso en consultas

únicas de solicitud-respuesta de tipo cliente-servidor en un solo envío, así como aplicaciones en las

que la entrega puntual es más importante que la precisa, como en la transmisión de voz o vídeo. La

relación de IP, TCP y UDP se muestra en la figura 1-22. Puesto que el modelo se desarrolló, se ha

implementado IP en muchas otras redes.

La capa de aplicación
     El modelo TCP/IP no tiene capas de sesión ni de presentación. No se han necesitado, por lo que

no se incluyen. La experiencia con el modelo OSI ha probado que este punto de vista es correcto: son

de poco uso para la mayoría de las aplicaciones.

     Arriba de la capa de transporte está la capa de aplicación. Contiene todos los protocolos de nivel

más alto. Los primeros incluyeron una terminal virtual (TELNET), transferencia de archivos (FTP) y

correo  electrónico  (SMTP),  como  se  muestra  en  la  figura  1-22.  El  protocolo  de  terminal  virtual

permite que un usuario en una máquina se registre en una máquina remota y trabaje ahí. El protocolo

de transferencia de archivos proporciona una manera de mover con eficiencia datos de una máquina

a otra. El correo electrónico era originalmente sólo un tipo de transferencia de archivos, pero más

tarde  se  desarrolló  un  protocolo  especializado  (SMTP)  para  él.  Con  el  tiempo,  se  han  agregado

muchos otros protocolos: DNS (Sistema de Nombres de Dominio) para la resolución de nombres de

host en sus direcciones de red; NNTP, para transportar los artículos de noticias de USENET; HTTP,

para las páginas de World Wide Web, y muchos otros.

Mg. Medín Cristian

  Página | 22

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

La capa host a red
     Debajo de la capa de interred hay un gran vacío. El modelo de referencia TCP/IP en realidad no

dice mucho acerca de lo que pasa aquí, excepto que puntualiza que el host se tiene que conectar a la

red  mediante  el  mismo  protocolo  para  que  le  puedan  enviar  paquetes  IP.  Este  protocolo  no  está

definido y varía de un host a otro y de una red a otra. Este tema rara vez se trata en libros y artículos

sobre TCP/IP.

Comparación entre los modelos de referencia OSI y TCP/IP
     Los modelos de referencia OSI y TCP/IP tienen mucho en común. Los dos se basan en el concepto

de una pila de protocolos independientes. Asimismo, la funcionalidad de las capas es muy parecida.

Por ejemplo, en ambos modelos las capas que están arriba de, incluyendo a, la capa de transporte está

ahí para proporcionar un servicio de transporte independiente de extremo a extremo a los procesos

que  desean  comunicarse.  Estas  capas  forman  el  proveedor  de  transporte.  De  nuevo,  en  ambos

modelos, las capas que están arriba de la de transporte son usuarias orientadas a la aplicación del

servicio de transporte.

    Tres conceptos son básicos para el modelo OSI:

1.  Servicios.

2.  Interfaces.

3.  Protocolos.

     Probablemente la contribución más grande del modelo OSI es que hace explícita la distinción entre

estos tres conceptos. Cada capa desempeña algunos servicios para la capa que está arriba de

ella. La definición de servicio indica qué hace la capa, no la forma en que la entidad superior tiene

acceso a ella, o cómo funciona dicha capa. Define el aspecto semántico de la capa.

     La  interfaz  de  una  capa  indica  a  los  procesos  que  están  sobre  ella  cómo  accederla.  Especifica

cuáles son los parámetros y qué resultados se esperan. Incluso, no dice nada sobre cómo funciona

internamente la capa.

     Por último, una capa es quien debe decidir qué protocolos de iguales utilizar. Puede usar cualquier

protocolo  que  desee,  en  tanto  consiga  que  se  haga  el  trabajo  (es  decir,  proporcione  los  servicios

ofrecidos). También puede cambiarlos cuando desee sin afectar el software de las capas superiores.

Estas ideas encajan muy bien con las ideas modernas sobre la programación orientada a objetos. Un

objeto, como una capa, cuenta con un conjunto de métodos (operaciones) que pueden ser invocados

por  procesos  que  no  estén  en  dicho  objeto.  La  semántica  de  estos  métodos  define  el  conjunto  de

servicios que ofrece el objeto.  Los parámetros  y  resultados de los métodos forman la interfaz del

Mg. Medín Cristian

  Página | 23

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

objeto. El código interno del objeto es su protocolo y no es visible o no tiene importancia fuera del

objeto.

     Originalmente, el modelo TCP/IP no distinguía entre servicio, interfaz  y protocolo, aunque las

personas han tratado de readaptarlo con el propósito de hacerlo más parecido al OSI. Por ejemplo,

los únicos servicios ofrecidos realmente por la capa de interred son SEND IP PACKET y RECEIVE

IP PACKET.

     Como  consecuencia,  los  protocolos  del  modelo  OSI  están  mejor  ocultos  que  los  del  modelo

TCPI/IP y se pueden reemplazar fácilmente conforme cambia la tecnología. La facilidad para realizar

tales cambios es uno de los objetivos principales de tener protocolos en capas. El modelo de referencia

OSI se vislumbró antes de que se inventaran los protocolos correspondientes.

     Esta  clasificación  significa  que  el  modelo  no  estaba  diseñado  para  un  conjunto  particular  de

protocolos, un hecho que lo hizo general. Una deficiencia de esta clasificación es que los diseñadores

no tenían mucha experiencia con el asunto y no tenían una idea concreta de qué funcionalidad poner

en qué capa. Por ejemplo, originalmente la capa de enlace de datos sólo trataba con redes de punto a

punto.

     Cuando  llegaron  las  redes  de  difusión,  se  tuvo  que  extender  una  nueva  subcapa  en  el  modelo.

Cuando las personas empezaron a construir redes reales utilizando el modelo OSI y los protocolos

existentes,  se  descubrió  que  estas  redes  no  coincidían  con  las  especificaciones  de  los  servicios

solicitados (maravilla de maravillas), por lo que se tuvieron que integrar subcapas convergentes en el

modelo para proporcionar un espacio para documentar las diferencias. Por último, el comité esperaba

en un principio que cada país tuviera una red, controlada por el gobierno y que utilizara los protocolos

OSI, pero nunca pensaron en la interconectividad de redes. Para no hacer tan larga la historia, las

cosas no sucedieron como se esperaba.

     Con TCP/IP sucedió lo contrario: los protocolos llegaron primero y el modelo fue en realidad una

descripción de los protocolos existentes. No había problemas para ajustar los protocolos al modelo.

Encajaban a la perfección. El único problema era que el modelo no aceptaba otras pilas de protocolos.

Como consecuencia, no era útil para describir otras redes que no fueran TCP/IP.

     Volviendo de los asuntos filosóficos a los más específicos, una diferencia patente entre los dos

modelos es el número de capas: el modelo OSI tiene siete y el TCP/IP sólo cuatro. Los dos tienen

capas de (inter)red, transporte y aplicación, pero las otras capas son diferentes.

     Otra diferencia está en el área de la comunicación orientada a la conexión comparada con la no

orientada a la conexión. El modelo OSI soporta ambas comunicaciones en la capa de red, pero sólo

la de comunicación orientada a la conexión en la capa de transporte, donde es importante (porque el

Mg. Medín Cristian

  Página | 24

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

servicio de transporte es transparente para los usuarios). El modelo TCP/IP sólo tiene un modo en la

capa de red (no orientado a la conexión) pero soporta ambos modos en la capa de transporte, lo que

da a los usuarios la oportunidad de elegir. Esta elección es importante especialmente para protocolos

sencillos de solicitud-respuesta.

Crítica al modelo OSI y los protocolos
     Ni el modelo OSI y sus protocolos ni el modelo TCP/IP  y sus protocolos son perfectos. Se les

pueden  hacer,  y  se  les  han  hecho,  críticas.  Empezaremos  con  el  modelo  OSI  y  más  adelante

examinaremos el modelo TCP/IP.

En la época en la que se publicó la segunda edición de este libro (1989), a muchos expertos en el

campo les pareció que el modelo OSI y sus protocolos iban a dominar el mundo y a desplazar a todos

los demás. Eso no sucedió. ¿Por qué? Sería útil echar un vistazo a algunas lecciones.

Éstas se pueden resumir así:

1.  Aparición inoportuna.

2.  Mala tecnología.

3.  Malas implementaciones.

4.  Malas políticas.

Aparición inoportuna
     Primero  veamos  la razón  número  uno:  aparición  inoportuna.  El  tiempo  en  que se  establece un

estándar es absolutamente crítico para el éxito. David Clark, del M.I.T., tiene una teoría de estándares

que llama apocalipsis de los dos elefantes, la cual se ilustra en la figura 1-23.

     Esta figura muestra la cantidad de actividad que rodea  a un sujeto nuevo. Cuando se descubre

primero  el  sujeto,  hay  una  explosión  de  actividad  de  investigación  en  forma  de  exposiciones,

documentos y reuniones. Después de un tiempo esta actividad disminuye, las empresas descubren el

sujeto y surge la ola de miles de millones de dólares de inversión.

     Es esencial que los estándares se escriban en el punto intermedio entre los dos “elefantes”. Si los

estándares se escriben demasiado pronto, antes de que se termine la investigación, el tema podría no

estar  entendido  por  completo;  el  resultado  son  malos  estándares.  Si  se  escriben  demasiado  tarde,

varias empresas podrían haber hecho  ya inversiones importantes en diversas maneras de hacer las

cosas que los estándares han ignorado. Si el intervalo entre los dos elefantes es muy corto (porque

cada  cual  tiene  prisa  por  empezar),  las  personas  que  están  desarrollando  los  estándares  podrían

fracasar.

Mg. Medín Cristian

  Página | 25

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

    Al parecer, los protocolos OSI estándar han sido vencidos. Los protocolos TCP/IP competidores

ya eran ampliamente utilizados por las universidades investigadoras al momento en que aparecieron

los protocolos OSI. Mientras la ola de los miles de millones de inversión aún no golpeaba, el mercado

académico  era  bastante  grande  para  que  los  proveedores  empezaran  a  hacer  ofertas  cautas  de  los

productos TCP/IP. Cuando OSI llegó, no quisieron soportar una segunda pila de protocolos hasta que

se vieran forzados, por lo que no hubo ofertas iniciales. Puesto que cada empresa esperaba que la otra

diera el primer paso, ninguna lo hizo y OSI nunca prosperó.

Mala tecnología
     La segunda razón por la que OSI no tuvo éxito es que tanto el modelo como los protocolos tienen

defectos. La elección de las siete capas fue más política que técnica, y dos de las capas (la de sesión

y la de presentación) están casi vacías, mientras que las otras dos (la de enlace de datos y la de red)

están saturadas.

     El modelo OSI, junto con el servicio asociado de definiciones y protocolos, es extraordinariamente

complejo. Si se apilan, los estándares impresos ocupan una fracción importante de un metro de papel.

Incluso son difíciles de implementar y de operación deficiente. En este contexto, nos viene a la mente

un enigma propuesto por Paul Mockapetris y citado en (Rose, 1993):

P: ¿Qué obtiene cuando cruza un gángster con un estándar internacional?

R: Alguien que le hace una oferta que usted no entiende.

     Además  de  ser  incomprensible,  otro  problema  con  OSI  es  que  algunas  funciones,  como

direccionamiento, control de flujo y control de errores, reaparecen una y otra vez en cada capa. Por

ejemplo, Saltzer y cols. (1984) han apuntado que para ser efectivo el control de errores, se debe hacer

Mg. Medín Cristian

  Página | 26

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

en la capa superior, puesto que repetirlo una y otra vez en cada una de las capas inferiores suele ser

innecesario e ineficaz.

Malas implementaciones
     Ante  la  enorme  complejidad  del  modelo  y  los  protocolos,  no  es  de  sorprender  que  las

implementaciones iniciales fueran grandes, pesadas y lentas. Todos los que lo intentaron fracasaron.

No  le  tomó  mucho  tiempo  a  las  personas  asociar  OSI  con  “baja  calidad”.  Aunque  los  productos

mejoraron con el paso del tiempo, la imagen persistió.

     En contraste, una de las primeras implementaciones de TCP/IP era parte de UNIX de Berkeley y

fue bastante buena (sin mencionar que era gratis). Las personas pronto empezaron a utilizarla, lo que

la llevó a un uso mayor por la comunidad, y esto a su vez condujo a mejoras que la llevaron a un

mayor uso en la comunidad. Aquí la espiral fue ascendente en vez de descendente.

Malas políticas
     A  causa  de  la  implementación  inicial,  muchas  personas,  sobre  todo  en  el  nivel  académico,

pensaban que TCP/IP era parte de UNIX, y en la década de 1980, UNIX no parecía tener paternidad

alguna en la universidad.

     Por otra parte, se tenía la idea de que OSI sería la criatura de los ministerios de telecomunicación

de Europa, de la comunidad europea y más tarde del gobierno de los Estados Unidos. Esta creencia

era  cierta  en  parte,  pero  no  ayudaba  mucho  la  idea  de  un  manojo  de  burócratas  gubernamentales

intentando  poner  en  marcha  un  estándar  técnicamente  inferior  al  mando  de  los  investigadores  y

programadores pobres que estaban en las trincheras desarrollando realmente redes de computadoras.

Algunas personas compararon este desarrollo con la ocasión en que IBM anunció, en la década de

1960, que PL/I era el lenguaje del futuro, o cuando más tarde el DoD corregía esto anunciando que

en realidad era Ada.

Crítica del modelo de referencia TCP/IP
     El modelo de referencia TCP/IP y los protocolos también tienen sus problemas. En primer lugar,

el  modelo  no  distingue  claramente  los  conceptos  de  servicio,  interfaz  y  protocolo.  Una  buena

ingeniería de software requiere la diferenciación entre la especificación y la implementación, algo

que OSI hace con mucho cuidado y que TCP/IP no hace. En consecuencia, el modelo TCP/IP no es

una guía para diseñar redes nuevas mediante tecnologías nuevas.

Mg. Medín Cristian

  Página | 27

Universidad Tecnológica Nacional - FRRO

Asignatura: Comunicación de Datos

     En segundo lugar, el modelo TCP/IP no es general del todo y no está bien ajustado para describir

ninguna pila de protocolos más que de TCP/IP. Por ejemplo, es completamente imposible tratar de

utilizar el modelo TCP/IP para describir Bluetooth.

     En tercer lugar, la capa host a red no es en realidad una capa del todo en el sentido normal del

término, como se utiliza en el contexto de los protocolos de capas. Es una interfaz (entre la capa de

red y la de enlace de datos). La distinción entre una interfaz y una capa es crucial y nadie debe ser

descuidado al respecto.

     En cuarto lugar, el modelo TCP/IP no distingue (ni menciona) las capas físicas  y de enlace de

datos.  Son  completamente  diferentes.  La  capa  física  tiene  que  ver  con  las  características  de

transmisión de comunicación por cable de cobre, por fibra óptica e inalámbrica. El trabajo de la capa

de enlace de datos es delimitar el inicio y fin de las tramas y captarlas de uno a otro lado con el grado

deseado  de  confiabilidad.  Un  modelo  adecuado  debería  incluir  ambas  como  capas  separadas.  El

modelo TCP/IP no hace esto.

     Por  último,  aunque  los  protocolos  IP  y  TCP  se  idearon  e  implementaron  con  sumo  cuidado,

muchos de los demás protocolos fueron hechos con fines específicos, producidos por lo general por

estudiantes  de  licenciatura  que  los  mejoraban  hasta  que  se  aburrían.  Posteriormente,  las

implementaciones de tales protocolos se distribuyeron de manera gratuita, lo que dio como resultado

un uso amplio y profundo y, por lo tanto, que fueran difíciles de reemplazar. Algunos de ellos ahora

están en apuros. Por ejemplo, el protocolo de terminal virtual, TELNET, se diseñó para una terminal

de teletipo mecánica de 10 caracteres por segundo. No sabe nada de interfaces gráficas de usuario ni

de ratones. No obstante, 25 años más tarde aún tiene un amplio uso.

     En resumen, a pesar de sus problemas, el modelo OSI (excepto las capas de sesión y presentación)

ha probado ser excepcionalmente útil en la exposición de redes de computadoras. En contraste, los

protocolos  OSI  no  han  sido  muy  populares.  Sucede  lo  contrario  con  TCP/IP:  el  modelo  es

prácticamente inexistente, pero los protocolos tienen un amplio uso.

Mg. Medín Cristian

  Página | 28

