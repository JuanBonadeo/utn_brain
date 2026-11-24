        UNIVERSIDAD TECNOLOGICA NACIONAL
           FACULTAD REGIONAL ROSARIO


     INGENIERIA EN SISTEMAS DE INFORMACION


              Asignatura: Comunicaciones



           Apunte: Comunicaciones Digitales

(Grabación de consultas con el Ing. Jorge A. Campanaro
Indice

Indice .......................................................................................................................... 2
Introducción ................................................................................................................. 3
Señal Analógica – Portadora Analógica ............................................................................. 4
  FDM: Multiplexación por División de Frecuencias............................................................. 9
Señal Digital – Portadora Analógica ............................................................................... 11
  FSK Multinivel .......................................................................................................... 13
  PSK Multinivel (QAM o APSK) ..................................................................................... 13
Demodulación ............................................................................................................. 16
  ASK - Sincronica o Coherente ..................................................................................... 16
  ASK - Asincronica - Incoherente – Detección de Envolvente .......................................... 17
  FSK - Sincronica o Coherente .................................................................................... 17
  FSK - Asincronica - Incoherente – Detección de Envolvente .......................................... 17
  PSK - Sincronica o Coherente .................................................................................... 17
Señal Analógica – Portadora Digital ............................................................................... 18
  TDM – Multiplexación por división de tiempo ................................................................ 18
  PCM - Modulación por Pulsos Codificados ..................................................................... 20
Anexo 1 ..................................................................................................................... 26




                                                                                                                                      2
Introducción


MODULACION DE SEÑALES


El concepto general de la Modulación, es que consiste en “adaptar” una señal mensaje, la que
se quiere transmitir, al medio de transmisión.
Por ejemplo, una señal digital (como la de la computadora) no puede viajar muy lejos debido a que
es muy sensible al ruido y a las interferencias. Hay que adaptarla al medio de transmisión (par de
cobre, por ejemplo). Esto se hace a través del MODEM (MODulador, DEModulador).

Por otro lado, la Modulación consiste también en un traslado en frecuencia del mensaje (fm) a
una frecuencia mucho mayor, la frecuencia de la señal portadora (fc), que siempre es de alta
frecuencia comparándola con el mensaje (fm << fc ).

Por ejemplo, en Radio AM (Amplitud Modulada), el mensaje de voz del locutor o la música
transmitida al aire, es de baja frecuencia (de 20 Hz a 20 KHz). La portadora, en cambio, es
de alrededor de 1000 KHz (20 KHz << 1000 KHz).

Otro ejemplo sería Radio FM (Frecuencia Modulada), donde el mensaje es el mismo que en AM, de
baja frecuencia, y la portadora es aún mayor, de 100 MHz (20 KHz << 100 MHz).

Por último, MUY IMPORTANTE, siempre en la señal modulada el Mensaje modula a                          la
Portadora.

En una transmisión determinada, podemos tener dos tipos de señales:

    1- Señal Analógica
    2- Señal Digital

Lo que vamos a tratar de hacer es transmitir o transportar de un punto hacia otro una señal de
Información (mensaje) que, tal cual está, no se puede transmitir. Para ello vamos a hacer uso de
otra señal u onda, que va a ser la encargada de TRANSPORTAR la Información.

Es decir, el mensaje (analógico ó digital) que tiene la Información, va a ser transportado por otra
señal u onda, que puede ser analógica o digital, y que se denomina PORTADORA.

Resumiendo, habrá DOS señales:

Mensaje con la información a transmitir
Portadora necesaria para transportar el mensaje de origen a destino.

Las combinaciones posibles, serán:

    I-      Señal Analógica (Mensaje)
            Portadora Analógica

    II-     Señal Digital (Mensaje)
            Portadora Analógica

    III-    Señal Analógica (Mensaje)
            Portadora Digital

Nota: vamos a realizar los 3 casos aunque en realidad los I y II (que tiene portadora analógica) son
similares, y el análisis es el mismo lo que cambia es el tipo de señal que vamos a transmitir. Todo
lo que se diga de aquí en adelante para el caso I vale para el caso II.




                                                                                                      3
Señal Analógica – Portadora Analógica

La portadora es la señal encargada de transmitir el mensaje, es decir las variaciones de alguna
magnitud de la misma: Amplitud (de tensión o corriente), Frecuencia ó Fase.

Entonces, la MODULACION consiste en variarle (modularle) algún parámetro a la portadora, de
acuerdo al mensaje que quiero transmitir. Estos parámetros a modificar en la portadora, serán:
amplitud, frecuencia o fase. Uno por vez.

Sea una Onda Senoidal (Mensaje):          Xm = Am . cos (2.л. fm .t + φm)

Y sea una Onda Portadora:      Xc = Ac . cos (2.л. fc .t + φc)

Los parámetros de la misma son:

Amplitud (Ac) = valor máximo

Frecuencia (fc) = cantidad de ciclos por unidad de tiempo (Hz).

Fase(φ)= fase o ángulo inicial (grados)




                                                                        AM



  Xm

                                                                        FM
                                                                    t


   Xc

                                                                        PM
                                                                    t



AM (Modulación de Amplitud): Cuando el mensaje crece, la portadora aumenta el valor; cuando
el mensaje disminuye, la portadora también disminuye su amplitud.
La amplitud de la portadora varía de acuerdo al mensaje.
El hecho de variar la amplitud (disminuir o aumentar una magnitud) se denomina Modulación de
Amplitud (AM). La fase y la frecuencia permanecen constantes.
Se modula para transmitir el mensaje.

FM (Modulación de Frecuencia): Mantengo constantes la amplitud y la fase de la portadora y
vario la frecuencia de la portadora. De acuerdo a la amplitud del mensaje cambia la
frecuencia de la portadora.

PM (Modulación de Fase): Es muy difícil hacer el dibujo de la Modulación de Fase, porque lo que
se hace es variar un ángulo, entonces se vería como si fuese modulación de frecuencia, porque la
fase y la frecuencia afectan por igual el argumento de la onda senoidal de la portadora.
El dibujo se refiere a una modulación discreta (cambios bruscos de la fase) porque es la única
forma de verlo. Con una modulación continua no se diferencia la gráfica de la FM. La Fase es la
distancia al origen.
La amplitud y la frecuencia son constantes. La fase varia (en el dibujo, si es negativo se va a
positivo, o sea 180° por ejemplo).

La modulación que vamos a ver en detalle es AM, porque es la más sencilla. La idea es ver como la
portadora transporta el mensaje.


                                                                                                  4
AM- Análisis Temporal y Espectral (o de Frecuencias)

   Representación del mensaje y la portadora:

   1) En el TIEMPO.




                                                      t


   2) En FRECUENCIA

   Xm          Am


          fn

                                          f
               fm

   Xc                              Ac
                                                                 : Significa un corte en la
                     fn                                      escala de frecuencia para que
                                                             pueda graficarse en la página
                                   fc     f

        fc > fn  la frecuencia de la portadora siempre es mucho mayor que la del mensaje.

   3) Análisis funcional: (como la fase se mantiene constante vamos a considerar en ambos casos
      que es cero)

   Función del Mensaje:    X m  Am (cos 2 f m t )
   Función de la Portadora: X c  Ac (cos 2 f c t )

   Ahora se quiere saber es cómo es la señal modulada, entonces se afecta a la amplitud ya que
   se está viendo modulación de amplitud.
   Afectando la amplitud de la portadora de acuerdo al mensaje:

    X AM  ( Ac  Am cos(2f m t )) * cos(2 f c t )  SEÑAL MODULADA
                                                           AM:
         Amplitud     Mensaje       No cambia                      #    señal (mensaje)      AC
         portadora                                                 #    señal (mensaje)      AC


             ( se afecta la amplitud de
              la portadora sumándole
              el mensaje)
Distribuyendo:


        X AM  Ac cos(2fct)  Am cos(2fmt) *cos(2fct)
                                 producto de cosenos
                                                      1
                                  cos  * cos         (cos(    )  cos(    ))
                                                      2


                                                                                                   5
                                        Am                         A
        X AM  Ac cos( 2 f c t )         cos( 2t[ f c  f m ])  m cos( 2 t[ f c  f m ])
                                        2                           2
Analizando, tenemos:
       Una componente AC en frecuencia fC
       Una componente Am / 2 en frecuencia fC - fm
       Una componente Am / 2 en frecuencia fC + fm

               XAM


            Xcm                         Ac
                                 Am/2         Am/2




                                         fc          f
                    fm


Se tiene lo necesario como para recuperar el mensaje: Amplitud y Frecuencia.
Antes el mensaje tenía una frecuencia baja, ahora viaja a una frecuencia alta.
Si bien se tiene fC + fm ; si fC = 1230 y fC + fm = 1260 se puede saber cuál es la frecuencia del
mensaje, en este caso será de 30 KHz, (cuando se quiere identificar una emisora la identificamos
con el número, ese número que representa a la emisora es la frecuencia de la portadora, es decir
cada emisora tiene una portadora determinada, no puede tener cualquier portadora, porque sino no
la encontraremos, siempre tiene la misma frecuencia en un valor fijo en el espectro)
Si fC = 1230 y fC + fm = 1260  la frecuencia del mensaje es fm = 30 KHz o Kc/s
Ya se tiene el valor de la frecuencia y el valor de la amplitud como se tiene el valor A m / 2, solo
resta multiplicar por 2 y da el valor de Am

      Sabemos por Fourier que una señal (mensaje) No senoidal está compuesto por una serie de
       sumas de señales senoidales.
      Por una cuestión de convensión graficamos un espectro cualquiera en este caso triangular.

   FIG.1)
        se modula c/u de las
           componentes                                   Ac
                             mensaje con infinitas
            frecuenciales
                                componentes
                                 armonicas



         f1                f2                            fc


            Banda w = f2 - f1



   Por cuestión de convensión las bajas frecuencias se grafican de menor amplitud (estarán más a
   la izquierda) y las altas frecuencias se grafican con mayor amplitud (más a la derecha), de esta
   manera vemos gráficamente donde está la información de las bajas frecuencias y donde está la
   información de las altas frecuencias.

    f 1  f 2  f c si se cumple w  f 2  f 1  f 2




                                                                                                  6
FIG 2) (I) BSD (Doble Banda Lateral)
                                 BCI (banda                BCS (banda
                               lateral inferior)         lateral superior)
                                                    Ac

                                     fc - f1                  fc + f1




                                                    fc
                     fc + f2          w                            w           fc + f2
                     fc + w                                                    fc + w
                                                   2w
                                                   2fmax


           fC – f2

            FC - w


En el caso que fmin sea despreciable frente a fmax. Se puede tomar 2 x fmax=2 x W

Tenemos:

f1 = frecuencia mínima del mensaje = fmín
f2 = frecuencia máxima del mensaje = fMáx

con las infinitas componentes armónicas, se produce la suma y resta con la frecuencia de la
portadora por lo tanto se tendrá una suma mínima y una suma máxima y una resta mínima y
una resta máxima, y en el medio sumas de las frecuencias intermedias y restas de las
frecuencias intermedias.

La banda de la FIG. 1) la vemos repetida dos veces en la FIG 2), es decir el mensaje aparece
repetido a ambos lados de la portadora (BCI, BCS).
No sería necesario transmitir las dos bandas laterales porque una sola banda alcanza (la
superior o la inferior) para recuperar la información del mensaje (frecuencia y amplitud de cada
componente). Se puedeinclusive no enviar la portadora o sea suprimir la portadora, e inclusive
se puede enviar una sola banda lateral y con la portadora suprimida, a los efectos de ahorrar
energía en la transmisión (esto es muy útil en equipos móviles donde el suministro de energía
es crítico).

FIG. 3 SSB o BLU se transmite la portadora y una banda solamente.

    A
        Comunicación Punto a Punto o Movil




                                                         fc                      f

                                                                  fc + f Máx

FIG. 4 DSB SC se transmite las dos bandas sin la portadora.




                                                                                              7
       A
       Llego a muchos receptores,
         receptor barato y no me
          importa gastar energia



                                                       fc
                                                                                   f




   FIG. 5 SSB SC mandar una banda lateral sin la portadora.
        A
         Problema de energia y para llegar a
                 pocos receptores




                                                       fc
                                                                                   f
                                                               fc – fMáx




   Esto es, sin portadora en (III) y en (IV).

     Xm * Xc
                                                             No significa que la
                         Am cos 2f m t  Ac cos 2f c t    portadora no exista
                                                            pero esta porque la
                                                               multiplicamos


ADSBSC= Am.cos2ϖfmt . Ac cos 2ϖ fc t = ½ Am Ac Cos 2ϖ (fc –fm) t + ½ AmAc.Cos2ϖ(fc+fm) t

Si consideramos que Ac es una constante para esa transmisión podemos tomar Ac = 1, quedando
entonces :

ADSBSC= ½ Am .Cos 2ϖ (fc –fm) t + ½ Am.Cos2ϖ(fc+fm) t

Observaciones:

Cuando ((II) y (IV)) disminuyo la potencia.
Al no mandar la portadora ((III) y (IV)) disminuyo la potencia.




                                                                                              8
FDM: Multiplexación por División de Frecuencia

Cada Señal Modula a una Portadora diferente y única para cada señal, entonces se puede transmitir
todas las señales por un mismo canal ocupando cada una banda de frecuencia distinta. Esto es, se
transmite varios mensajes simultáneamente por un mismo canal, dividiendo por bandas de
frecuencia, una banda por señal, y en un mismo instante de tiempo se transmiten todos los
mensajes juntos (dividimos el canal en slots de frecuencia).

Diagrama F.D.M.:



           mensaje 1
                   f                                                                  f
       w
                            fc1

           mensaje 2
                  f                                                                   f
      w
                                             fc2

           mensaje 3
                  f                                                                   f
      w
                                                        fc2

           mensaje 4
                  f                                                                   f
       w                                                             fc3


                                                                                      f
No se mezclan los mensajes entre si, porque cada mensaje modula una portadora distinta y de esta
manera cada señal se ubica en una banda de frecuencia distinta dada por la portadora
correspondiente (a ambos lados de esa portadora). Cada una de las señales (mensaje) tiene
asignado una portadora fija para que no interfiera a las restantes señales ( fc1 , fc2 , fc3 , …).

Se podría eliminar una de las bandas laterales de cada señal. Por ejemplo, en el esquema de
siguiente, si tengo un canal que tiene un ancho Bw =fmax – fmin, se pueden transmitir 4 señales,
pero si se transmite un sola banda lateral en lugar de ambas, se ocupará la mitad del espectro, lo
cual implica que se puede transmitir 8 señales en el mismo Ancho de Banda del Canal anterior. De
esta manera, aprovecho al máximo el canal.




                                                       N SEÑALES




                                   f c Mín                                                f c MAX       f

                                              BW = f c MÁX - f c Mín = N . 2.fMáx = N . 2.W


                                                                                                    9
                                            N SEÑALES




                              f c Mín                            f c MAX               f

                                BW = f c MÁX - f c Mín = N . fMáx = N . W


Entonces, si tengo un canal que tiene un determinado Ancho de Banda, delimitado por sus
frecuencias máxima y mínima de corte (fmax y fmin ), el cálculo del Ancho de Banda utilizado del
canal (Bw) en cada caso, será:

                SSB (Una banda lateral):      Bw= N * W
                DSB (doble banda lateral):    Bw= N * 2W

Donde:

N = número de mensajes o señales a transmitir por ese único canal
W = fmax Frecuencia Máxima del mensaje (Sii la Frec Mínima del mensaje es mucho menor que la
Frec Máx.)
Bw = Ancho de Banda utilizado del canal
f c MÁX Frec. de Corte Máx. del Canal (Máxima frecuencia que el canal deja pasar)
f c Mín Frec. de Corte Mín. del Canal (Mínima frecuencia que el canal deja pasar )




                                                                                                   10
Señal Digital – Portadora Analógica
Se utiliza para transmitir información de computadora (señal digital) a través de la línea telefónica
como una señal analógica.
Procedimiento: se convierte la señal digital en analógica a través del MODEM, y viceversa en el
extremo receptor.

                             RED TELEFONíA (RED TECNOLGÍA DIGITAL QUE
PROCESA SEÑALES ANALÓGICA (VOZ) – Recibe señales analógicas (Voz)

  PC                MODEM                                                     MODEM                             PC
        Señal                       Señal                           Señal                     Señal
        Digital                   Analogica                       Analogica                   Digital
                    D                                RED                      A
                            A                     ANALOGICA                           D


                                                   MODEM


         1    0 0       1   0 0    1                    1     0     0     1       1   0   0      1

                                                                                                                ASK
                                                                                                            t
 Xm
                                              t



                                                                                                                FSK
                                                                                                        t


  Xc
                                              t
                                                                                                                PSK
                                                                                                        t




Los tres tipos de Modulación que existe, son:

ASK (Manipulación por desplazamiento de la Amplitud): cuando hay un “1” en la señal digital,
hay portadora; cuando hay un “0” no hay portadora. Entonces:

1 * Portadora = portadora
0 * Portadora = 0

ESTA MODULACIÓN ACTUALMENTE NO SE USA


FSK(Manipulación por desplazamiento de la Frecuencia): al “1” le asigno una frecuencia
portadora, y al “0” le asigno otra frecuencia portadora. Esto quiere decir que modulo dos
portadoras distintas, equivalente a dos transmisiones ASK superpuestas.

PSK(Manipulación por desplazamiento de la Fase): vengo con una determinada fase para el
“1” binario, y se producirá un cambio de fase cuando se cambia del “1” al “0”, o del “0” al “1” (ver
esquema anterior).




                                                                                                                      11
ANÁLISIS ESPECTRAL DE UN TREN DE PULSOS

Se entiende como tren de pulsos, a una señal de pulsos periódica en el
tiempo.

                                                                                                 = ANCHO DEL PULSO
  Amplitud
     Xm
                                                   senx
                                     sin c X 
  X1
                                                       x                                           T
                                                                                                        PERIODO = K *   
                                                                                                                 X




             f1                                                                                                             f
    0
                                                                                           
                  w
        Xc




                                                                 fc                                                             f
  Amplitud
                             fc - fm                                                      fc + fm




         restas          fc - w
                                                                                              fc + w
                                                                                                               sumas

                                                                 fc                                                             f
                                      fc -                                   fc +


                                                                                                           ESPECTRO
                                                                                                              ASK



                                                                                              fc + w
                            fc - w


                                                                 fc                                                             f
                                      fc -                                   fc +
              Filtro

                                                            Bw como tengo un espectro
       ESPECTRO                                                 infinito recorto en
         SEÑAL
                                                                      
    las frecuencia que                   Modulo
 estan por encima de 1/ 
        las elimana          Xn acotada en 1/      

                                                                                                                                    12
         w = 1/ (banda de frecuencias práctico de un tresn de pulsos)
         Bw  2 * 1/


La modulación ASK no se utiliza, sólo si se utiliza es FSK o PSK.
Para aumentar la velocidad, se utilizan los siguientes métodos.

FSK Multinivel

Se utilizan dos frecuencias y dos amplitudes, transmito más dígitos en la misma unidad de tiempo.
Varío tanto amplitud como frecuencia.
Tenemos entonces, cuatro posibilidades para transmitir:
                                                                f1
  1      0         0        1    0        0   1        1
                                                           A1

                                                                f2
                                                                f3

                                                           A2

                                                                f4

        f1             f2            f1           f2

En el mismo tiempo antes, enviaba 0 o 1, ahora enviamos 00, 01. 10,11 (2 digitos, cuatro
mensajes distintos)


PSK Multinivel (QAM o APSK)

Se varia la Fase y la Amplitud

2 Amplitud
4 Fases
Grafica Angular o Polar: 2 amplitudes para cada fase  8 posibilidades 3 digitos o bits c/u
                   90°
                   011

                   010
 180°
      101 100       000 001     0°
           110

             111
                   270°
Tengo 8 combinaciones, por lo cual estoy mandando 8 mensajes distintos.




                                                                                               13
    MODULACIÓN FSK

                                  1       11



                                                    1       0   1 1 0 0


                            f1
                                                   Salida señal Analógica




1     0   1 1   0 0                   0        0        0
                             f0



    Entrada señal Digital




                                                                            14
    MODULACIÓN PSK
    El esquema es el mismo salvo que en vez de ingresar con dos portadoras una con f1
    y otra portadora con f0 se ingresa con una portadora de frecuencia única pero una

    portadora con fase   ꬾ1 y otra portadora con fase ꬾ0
                                                            Cambio de Fase
                                   1       1 1         (cambia de 1 a 0 ó de 0 a 1)


                                                      1       0   1 1 0 0


                           ꬾ1
                                                     Salida señal Analógica




1     0   1 1     0 0
                            ꬾ0         0         0        0




    Entrada señal Digital




                                                                                   15
Demodulación

ASK - Sincronica o Coherente
Sincrónica porque la portadora tiene la misma frecuencia en el origen y receptor.
Se requiere la presencia de la portadora en el lugar de recepción, y además esta portadora debe
estar en sincronismo con la de emisión.
Esto es un inconveniente porque provoca un aumento de costo.
                                                                                 1   2
                                           fcm      SEÑAL EN A.S.K
                                                                                     CR

  SEÑAL DE                    SEÑAL EN
 MODULACION                     A.S.K    TRANSMISION
                                                                         fR
                                                                      LUGAR DE
           SEÑAL PORTADORA                                           RECEPCION
           DE FRECUENCIA FC


donde:
   (1) es el Filtro pasa basos (elimina las altas frecuencias)
   (2) circuito regenerador
        [cos 2 t ( f c  f m )  cos 2 t ( f c  f m )] cos 2 t f c =
        cos 2 t [ f c  ( f c  f m )]  cos 2 t [ f c  ( f c  f m )] 
        cos 2 t [ f c  ( f c  f m )]  cos 2 t [ f c  ( f c  f m )] 
        cos 2 t f m  cos 2 t [2 f c  f m ]  cos 2 t f m  cos 2 t [2 f c  f m ]
                         Pong un filtro que me deje pasar las bajas frecuencias
                          porque lo único que quiero recuperar es el mensaje
  A




                                                            No me interesa



         fm                2fc - fm      2fc + fm       f
  A




         fm                                         f




                                                                                                  16
ASK - Asincronica - Incoherente – Detección de Envolvente
Por posos sucesivos vamos recuperando la forma de la envolvente.
        absolutor o rectificador
            1             2         3                4
 SEÑAL                                                    SEÑAL
                                          CR
  ASK                                                    BINARIA


    1




    2



    3



    4



FSK - Sincronica o Coherente
Se hace necesaria la presencia de la portadora (en este caso 2 portadoras) en el lugar de destino.
                   f1




 SEÑAL
                                                             CR
 F.S.k.
                                               "1"
                                   inversor



                   f2
FSK - Asincronica - Incoherente – Detección de Envolvente



  0101
                                                                                 CR    SEÑAL
                                                                                      BINARIA

                                                            inversor




PSK - Sincronica o Coherente
(no existe incoherente)
  SEÑAL
  P.S.K.

                                                                        SEÑAL
                                                            CR
                                                                       BINARIA

                  Recuperacion
                  de Protadora




                                                                                                 17
Señal Analógica – Portadora Digital

Se basa en el concepto de mandar muestras en lugar de toda la información.
Si se tiene un mensaje analógico (señal analógica), en lugar de transmitir la señal completa se
puede transmitir sólo las muestras del mensaje.


                                    muestreo
                                    con cierto
                           t         tiempo                                                 t




La distancia entre pulsos es mayor que la duración de ellos, y es precisamente este tiempo muerto
el que se aprovecha para mandar otra información en un proceso de multiplexación en el tiempo.
Los pulsos de la portadora tienen un tiempo de ocurrencia. En ese instante se toma una muestra de
la señal de modulación y se varía algún parámetro del pulso. Los parámetros utilizados son:
amplitud, duración o posición, dando lugar a tres tipos de modulación:
                    X(t)




                     t1        t2        t3      t4      t

      PAM
   Modulación
  por amplitud
    de pulso

                                                         t
         PDM
      Modulación
     por duración
     de pulso=FM
                                                         t
      PPM
  Modulación
  por posición
 de pulso = PM
                                                         t

PAM varía sólo las amplitudes de los pulsos de acuerdo al mensaje
PDM varía sólo frecuencia, vario el ancho del pulso de acuerdo al mensaje
PPM varía sólo posición del pulso de acuerdo al mensaje.
PCM es una cuarta técnica, es la que se usa actualmente, se cuantifica y codifica la amplitud de
cada muestra PAM con un código dado (modulación por pulso codificado)

TDM – Multiplexación por división de tiempo

Si se tiene que enviar distintos mensajes (A, B, C, D) por un mismo canal (Bw):
 A        t1                                                 t1
                                                                  A'
          t2         Existen circuitos sin sincronismo       t2
 B                                                                B'

 C        t3                                                 t3
                                                                  C'
                                       Bw
 D         t4                                                t4   D'

Se transmite una muestra de A en un tiempo t1 y se recibe en A’. El tiempo en que A no se está
transmitiendo, se usa el canal para la transmitir la muestra de otro mensaje en tiempo distinto
(t2), en un tiempo t2 entonces se transmite una muestra de B y llegará B’. Luego se transmite una


                                                                                                   18
muestra de C en t3 y D en t4. En t5 se transmite la segunda muestra del mensaje A, y así
secuencialmente.
Son distintas muestras de cada mensaje (A, B, C y D) que se transmiten en cada instantes . El
conjunto de una muestra de cada mensaje se denomina TRAMA (dura Ts).
En un instante dado, cada muestra de cada señal viaja sola, esto es, ocupa el canal una muestra
por vez. No hay simultaneidad en el envío de las muestras, es una después de otra.
Se divide el uso del canal en el tiempo, un intervalo de tiempo para cada muestra.

 X(t)
                B
   A                D
            C


                                      Ts= Tiempo o periodo de muestreo. Tiempo
                                      hasta desde se toma una muestra hasta que
                                      volvamos a tomar otra (del mismo mensaje)

                                     fs= Frecuencia de muestreo (o frecuencia
                                           con que se toma una muestra)

                                      Tm= duración de lamuestra
                                t
    Ts = 1/fs
Importante (repito): en un instante de tiempo viaja una única señal por el canal, es decir lo usa o la
tiene con exclusividad (se divide el canal en el tiempo)
t1  A
t2  B
t1  t2

Esquema:
  canal 1                                                                        canal 1

                               C1    Medio físco de   C2
  canal 2                                                                        canal 2
                                      transmisión
                                      sincronismo
  canal 3                                                                        canal 3

En este esquema se han tomado señales X1(t), X2(t), X3(t) en PAM (X1(t) del canal 1, X2(t) del canal
2 y X3(t) del canal 3). El conmutador C1, rotativo, ha tomada muestras alternativas de cada canal.
En la recepción hay otro conmutador rotativo (C2) sincronizado con el emisor, que invierte el
proceso y entrega finalmente al destino X1(t), X2(t), X3(t).




                                                                                                   19
       Señal
       PAM
      Canal 1

                                                t
       Señal
       PAM
      Canal 2
                                                t
      Señal
      PAM
     Canal 3
                                                t



  Señal PAM
 Multiplexada


                                                t


                       trama
MUY IMPORTANTE: Notar de esta última gráfica, que la Trama comprende una muestra de c/u de
las señales de arriba, y dura Ts.

PCM - Modulación por Pulsos Codificados

Primero debemos explicar:

Cuantificación y Codificación de Niveles: de una señal analógica pueden ser tomadas muestras
cuyas amplitudes pueden alcanzar infinitos valores, pero solo es posible codificar un número finito
de valores de la amplitud de las muestras (es necesario definir una serie finita de valores posibles
de ser codificados)
El método consiste en: tomada una muestra, redondear el valor de esta, el valor más cercano de
entre los preestablecidos.
Ejemplo: dada una señal, cuyo intervalo de variación de amplitudes [-4.5; 4.5] se adopta como
valores a codificar a:-4.5; -3; -1.5; 0; 1.5; 3; 4.5, estos calores se preestablecen y se denominan
NIVELES CUANTICOS (tienen asociados un intervalo) si la muestra cae dentro de ese intervalo, el
valor es redondeado a ese nivel, este intervalo se llama CUANTO.



                        Niveles                               Nivel
                                                                      Codigo
                       Cuanticos                             Cuantico
                                                               4.5     111
                                                                3      101
  -4.5   -3     -1.5                                           1.5     100
                                                                0      000
                           0       1.5   3   4.5 Valor de la  -1.5     001
                                                  muestra       3      010
                                                  Amplitud     1.5     011




                                                                                                  20
       Señal
     Analógica



              4.5
               3
      Muestra 1.5

                -1.5
                4.5
                 3
 Cuantificacion 1.5
                                                               Esto es lo que se manda, 0
                -1.5                                             y 1 donde cada palabra
                                                                representa una amplitud
       Señal
                         1 0 1         1   1   1 00 1
      Binaria

Este hecho de mandar la amplitud digitalizada, cuantificada y codificada y en vez de mandar una
sola muestra, aprovecho y mando 30 muestra se le da nombre de PCM.
Usamos el :
               PCM 30+2
Donde:
 30 Canales de información
 2 Canales de incronización y señalización.
Con estos (canales de información, sincronización y señalización ) se arma lo que se llama TRAMA.
 Muestrador
                                Señal                                Señalización y         Codigo de
                              PAM / TDM                               Sincronismo             Linea
 Muestrador
      .                Multiplex               Cuantificador          Multiplexdor          Codificador
      .
      .
                                                                                  Señal PCM
      .                                                  Señal Multiplex          Monopolar
 Muestrador                                               Digitalizada


¿Cual es el límite que hay entre dos muestra?
¿Si se analizan 2 o más muestras como se que corresponde a un mensaje o a otro?
Desde el punto de vista temporal no tengo una justificación, la única forma de saberlo es a traves
del Análisis Frecuencial.

                           Dos mensajes disntintos don muestreo
                           igual (desde el punto de vista temporal
                          no hay diferencia entre una y otra señal)


¿Qué forma tiene el mensaje original? ¿Cuál es la correcta? ¿Tengo garantías de recuperar el
mensaje original?
Para esto trabajamos con el espectro frecuencial cuando hacemos por ejemplo la Modulación PAM
(+ sencilla), haremos un simple producto




                                                                   PAM



  Mensaje Analógico fm             t
                                                                              t
                                                                                                          21
Recordemos:
Espectro de un tren de pulsos
                         senx
         sin c X 
                          x

  1/Ts
                                 

     fs      2fs   3fs

                           4fs 5fs 6fs
                                                            Distintas componentes
                                                              dela función SincX



         PAM
                          Espectro que tiene la
                             información a
                               transmitir



     w=                                                   f




                     w      fs - w                fs                 fs - w   2 fs - w   2fs   2fs - w   3fs - w   3fs   3fs - w


Estas muestras en realidad no son un pedacito aislado del mensaje, sino que esta repetido infinitas
veces, si para recuperar mi señal necesito el espectro, lo tengo infinitas veces.

Entre una muestra y otra muestra quiero que el tiempo de muestreo sea lo más grande posible
para que me pueda entrar mayor cantidad de mensajes (muchas muestras).

         N           ==>          Ts ==>               fs



AL BAJAR LA FRECUENCIA ME ACERCO AL ORIGEN.

Donde:
N = cantidad de mensajes muestrados o transportados.
Ts= tiempo o periodo de muestreo (tiempo desde que se toma una muestra hasta que volvamos a
tomar otra del mismo mensaje)
Fs= frecuencia de muestreo




                                                                                                                                   22
                                                            SE CORREN ACERCANDOSE




                  w          fs - w                 fs              fs - w 2 fs - w   2fs   2fs - w

Lo que se hace es disminur la frecuencia de muestreo fs lo máximo posible para poder mandar más
cantidad de señales en el mismo canal.
Hay un p unto que es fs – w que si lo sigo tirando hacia el origen se me junta con el w.
          SUPERPOSICIÓN DE
            INFORMACION




                       w
                                         fs                fs - w
              fs - w

¿Cuál es el limite?

fs – w  w  fs  2w                      w = fmax- fmin  fmax

Por Tasa de Nyquist o Teorema de Muestreo; la frecuencia minimade muestreo fs siempre tiene que
ser mayor o igual que las 2 frecuencias maximas del mensaje.
Condición para que pueda recuperar el mensaje


                           fs  2 fmax
                                      Estamos fijando cual es la mínima
                                        frecuencia del tren de pulsos

Observación: en analógica teníamos que fc >> fm y a cada señal modulada en portadoras distintas,
y la ubico para que estén una al lado de la otra.
Ahora, tengo una sola portadora, como hay un solo mensaje por vez no me interesa lo que ocupe
pero como quiero poner varias muestras quiero achicar la frecuencia de la portadora para que el
período se agrande. Para agrandar el período tengo que achicar la frecuencia y si achico la
frecuencia (mucho) se me mezclan los espectros y no puedo recuperar el mensaje original.

¿Si al periodo no lo puedo agrandar más? ¿Puedo achicar la muestra? ¿Cuál es el límite?
En realidad lo que voy a mandar es un tren de pulsos, conjunto de ceros y unos que me
representan la amplitud del pulso.

 *  TM  n      Lo que dura la muestra
n = cantidad de dígitos del código de la muestra
 = Ancho del pulso
Ts  TM * N
N = cantidad de muestras.

Voy a estar mandando este conjunto de ceros y unos, tiene un espectro y para que pase, el ancho
de banda del canal tiene que ser mayor o igual que al cruce en cero.




                                                                                                      23
             N Muestras


                                            B2
                             A1                  C2
       B0                                  A2
                                  C1

      A0                      B1
            C0



      TM                                              t
                    Ts




                 n Dígitos



            1 0 11001 01

                                       t
            Ƭ        TM




Ts = N.TM = N.n.Ƭ = N.n.1/Bw = 1 / fs      ===> Bw = N.n.fs

TM = n.Ƭ

Bw = 1/Ƭ

Ts = 1/fs




                                                              24
                                     LIMITACION
                                     Bw     1/

                                   El cruce por 0 me lo define el ancho
                                   del pulso (si hago el pulso más
                                       chiquito se agranda el cruce)


Si achico    ==> El espectro del pulso va a ser >> Bw

                                       
                                   Si el      cae fuera del Bw
                                   va a caer fuera de lo que
                                   puede pasar por el canal


                  Bw
                           




                                                                          25
Anexo 1

ESPECTRO DE UN TREN DE PULSOS
Supongamos una señal:
Tren de pulso de amplitud A, Frecuencia f(=1/T), Ancho de Pulso 
                                                 X(t)
                                                   A




                                  -To                        To

                                                       T


Para estudiar eso definimos la función:
                                           senx
                            sin c X 
                                                 x
                                        sinc X




                   -3      -2     -1              1     2         3

De acuerdo a Fourier el Tren de Pulsos puede ser expresado como:

          A   
                            n
x(t )         2 A sin c( ) * cos 2  n f 0 t
          T0   1            T0
                                                            Frecuencia de cada armónica
                  Amplitud de las Armónicas

T0  componente continua
n  orden de las armónicas
f = n f0
Frecuencia Fundamental = f0 = 1/T0
La Amplitud de las armónicas se puede expresar como:
2 A       n   2 A
     sin c( )       sin c n f 0 
 T0        T0    T0
Para una envolvente de la amplitud de las armónicas dada por:
2 A
     sin c f  ; si se expresa tenemos:
 T0
Observación:
La separación entre armónicas = a la frecuencia del tren de pulso.
Las armónicas de mayor amplitud se encuentran entre 0 y 1/ 

                        1/To = fo
  To
                                

          1/To 2/To 3/To




                                                                                          26
