UNIVERSIDAD ABIERTA INTERAMERICANA
FACULTAD DE TECNOLOGÍA INFORMÁTICA
TECNOLOGÍA
DE LAS
COMUNICACIONES
“MEDIOS DE TRANSMISIÓN”
Año 2016

Contenido
Medios de transmisión guiados ............................................................................................................................. 3
Medios magnéticos ............................................................................................................................................. 3
Par trenzado ........................................................................................................................................................ 3
Tipos: ............................................................................................................................................................... 3
Categorías: ....................................................................................................................................................... 4
Características de la transmisión: .................................................................................................................... 4
Ventajas: .......................................................................................................................................................... 4
Desventajas: .................................................................................................................................................... 4
Conectores: ..................................................................................................................................................... 5
Cable coaxial ........................................................................................................................................................ 5
Conectores: ..................................................................................................................................................... 6
Fibra óptica .......................................................................................................................................................... 6
Cables de fibra óptica ...................................................................................................................................... 7
Tipos ................................................................................................................................................................ 7
Conectores....................................................................................................................................................... 8
Pérdida en los cables de Fibra Óptica ............................................................................................................. 9
Comparación de la fibra óptica y el alambre de cobre ................................................................................. 10
Medios de trasmisión no guiados ........................................................................................................................ 10
El espectro electromagnético ............................................................................................................................ 10
Transmisión inalámbrica ................................................................................................................................... 11
Radiotransmisión ........................................................................................................................................... 11
Microondas .................................................................................................................................................... 11
Ondas infrarrojas y milimétricas ................................................................................................................... 12
Satélites de comunicaciones ............................................................................................................................. 12
Satélites geoestacionarios ............................................................................................................................. 13
Satélites de Órbita Terrestre Media .............................................................................................................. 14
Satélites de Órbita Terrestre Baja ................................................................................................................. 14
Antenas .............................................................................................................................................................. 14
Tipos de antenas ........................................................................................................................................... 14
Medios de Transmisión Página 2 de 16

MMMMeeeeddddiiiioooossss ddddeeee ttttrrrraaaannnnssssmmmmiiiissssiiiióóóónnnn gggguuuuiiiiaaaaddddoooossss
El propósito de la capa física es transportar flujo de datos puro de una maquina a otra. Es posible utilizar varios
medios físicos para la transmisión real. Cada uno tiene su propio nicho en términos de ancho de banda, retardo,
costo, facilidad de instalación y mantenimiento. Los medios se clasifican de manera general en medios guiados,
como cable de cobre y fibra óptica y medios no guiados como radio y laser a través de aire.
Medios magnéticos
Una de las formas más comunes para transportar datos de una computadora a otra es almacenarlos en cintas
magnéticas o medios extraíbles; transportar físicamente la cinta o los discos a la máquina de destino y leer
dichos datos ahí. Este método no es tan avanzado como utilizar un satélite de comunicaciones geosíncrono, con
frecuencia es más rentable, especialmente para aplicaciones en las que un ancho de banda alto o el costo por
bit transportado es un factor clave.
Un ejemplo claro del uso de los medios magnéticos es el cálculo de cantidad y el costo de datos que podemos
almacenar en una cinta de 60x60x60 contra la cantidad y costo de usar otra tecnología cuando la distancia es
enorme.
Par trenzado
Uno de los medios de transmisión más viejos y todavía el más común, es el cable de par trenzado. Éste consiste
en dos alambres de cobre aislados, por lo regular de 1mm de grueso. Los alambres se trenzan en forma
helicoidal. Esto se hace porque dos alambres paralelos constituyen una antena simple. Cuando se trenzan los
alambres, las ondas de diferentes vueltas se cancelan, por lo que la radiación del cable es menos efectiva.
La aplicación más común es el sistema telefónico y la distancia que se puede recorrer con estos cables es de
varios kilómetros sin necesidad de amplificar las señales. Cuando muchos los cables de par trenzados recorren
de manera paralela distancias considerables, se suelen atar en haces y se cubren con una envoltura protectora.
Esto se hace porque los cables pueden sufrir interferencias.
Los cables de par trenzado se pueden utilizar para transmisión tanto analógica como digital. El ancho de banda
depende del grosor del cable y de la distancia que recorre. Hay varios tipos de cableado de par trenzado:
Tipos:
• Unshielded twisted pair (UTP) o par trenzado sin blindaje: son cables de pares trenzados sin blindar que
se utilizan para diferentes tecnologías de redes locales. Son de bajo costo y de fácil uso, pero producen
más errores que otros tipos de cable y tienen limitaciones para trabajar a grandes distancias sin
regeneración de la señal, su impedancia es de 100 ohmios.
• Shielded twisted pair (STP) o par trenzado blindado: se trata de cables de cobre aislados dentro de una
cubierta protectora, con un número específico de trenzas por pie. STP se refiere a la cantidad de
aislamiento alrededor de un conjunto de cables y, por lo tanto, a su inmunidad al ruido. Se utiliza en
redes de ordenadores como Ethernet o Token Ring. Es más caro que la versión sin blindaje y su
impedancia es de 150 ohmios.
• Foiled twisted pair (FTP) o par trenzado con blindaje global: son cables de pares que poseen una
pantalla conductora global en forma trenzada. Mejora la protección frente a interferencias y su
impedancia es de 120 ohmios.
• Screened fully shielded twisted pair (SFTP) o par trenzado totalmente blindado: es un tipo especial de
cable que utiliza múltiples versiones de protección metálica, estos son blindados y apantallados.
Antes de 1988, la mayoría de los edificios de oficinas tenía un cable de categoría 3 que iba desde un gabinete de
cableado central en cada piso hasta cada oficina. Este era el esquema que permitió que hasta cuatro teléfonos
comunes o dos de múltiples líneas en cada oficina se conectaran con el equipo de la compañía telefónica.
Medios de Transmisión Página 3 de 16

A comienzos de 1988 se introdujeron los cables de par trenzado categoría 5. Son similares a los de la categoría
3, pero con más vueltas por centímetro, lo que produce una menor diafonía y una señal de mejor calidad a
distancias más largas.
Como se observa en el cuadro, las siguientes categorías fueron mejorando y tienen capacidad para manejar
señales con anchos de banda superiores.
Categorías:
| Categoría  | Ancho de banda  |                                      | Aplicación  |     |
| ---------- | --------------- | ------------------------------------ | ----------- | --- |
| 1          | 0,4 MHz         | Líneas telefónicas y módems          |             |     |
| 2          | 4 MHz           | Cable para conexión de terminales    |             |     |
| 3          | 16 MHz          | 10BASE-T y 100BASE-T 4               |             |     |
| 4          | 20 MHz          | 16 Mbits  (Token Ring)               |             |     |
| 5          | 100 MHz         | 10BASE-T y 100BASE-TX  (Ethernet)    |             |     |
| 5 e        | 160 MHz         | 100BASE-TX y 1000BASE-T  (Ethernet)  |             |     |
| 6          | 250 MHz         | 1000BASE-T (Ethernet)                |             |     |
| 6 e        | 250 – 500 MHz   | 10GBASE-T (Ethernet)                 |             |     |
7  600 MHz  Telefonía, Televisión y Ethernet 1000BASE-T en el mismo
| 7 e  | 1000 MHz   | cable  |     |     |
| ---- | ---------- | ------ | --- | --- |
| 8    | 1200 MHz   | -      |     |     |
| 9    | 25000 MHz  | -      |     |     |
| 10   | 75000 MHz  | -      |     |     |

Características de la transmisión:
Está limitado en distancia, ancho de banda y tasa de datos. También destacar que la atenuación es una función
fuertemente dependiente de la frecuencia. La interferencia y el ruido externo también son factores importantes,
por eso se utilizan coberturas externas y el trenzado. Para señales analógicas se requieren amplificadores cada
5 o 6 kilómetros, para señales digitales cada 2 ó 3. En transmisiones de señales analógicas punto a punto, el
ancho de banda puede llegar hasta 250 kHz. En transmisión de señales digitales a larga distancia, el data rate no
es demasiado grande, no es muy efectivo para estas aplicaciones o dispositivos.
En redes locales que soportan ordenadores locales, el data rate puede llegar a 10 Mbps (Ethernet) y 100 Mbps
(Fast Ethernet).
En el cable par trenzado de cuatro pares, normalmente solo se utilizan dos pares de conductores, uno para
recibir (cables 3 y 6) y otro para transmitir (cables 1 y 2), aunque no se pueden hacer las dos cosas a la vez,
teniendo una trasmisión half-dúplex. Si se utilizan los cuatro pares de conductores la transmisión es full-dúplex.

Ventajas:
•  Bajo costo en su contratación.
•  Alto número de estaciones de trabajo por segmento.
•  Facilidad para el rendimiento y la solución de problemas.
•
Puede estar previamente cableado en un lugar o en cualquier parte.

Desventajas:
•  Altas tasas de error a altas velocidades.
•
Ancho de banda limitado.
| Medios de Transmisión  |     |     |     |     Página 4 de 16  |
| ---------------------- | --- | --- | --- | ------------------- |

• Baja inmunidad al ruido.
• Baja inmunidad al efecto crosstalk (diafonía)
• Alto costo de los equipos.
• Distancia limitada (100 metros por segmento).
Conectores:
Cable coaxial
Otro medio común de transmisión es el cable coaxial. Este cable tiene mejor blindaje que el de par trenzado, así
que puede abarcar tramos más largos a velocidades mayores. Hay dos clases de clave coaxial que con las más
utilizadas. Una clase: el cable de 50 ohms, se usa por lo general para transmisión digital. La otra clase, el cable
de 75 ohms, se utiliza comúnmente para la transmisión analógica y la televisión por cable.
Un cable coaxial consiste en un alambre de cobre rígido como núcleo, rodeado por un material aislante. El
aislante está reforzado con un conductor cilíndrico, que con frecuencia es una malla de tejido fuertemente
trenzado. El conductor externo se cubre con una envoltura protectora de plástico.
La construcción y el blindaje del cable coaxial le confieren una buena combinación de ancho de banda alto y
excelente inmunidad al ruido. El ancho de banda posible depende de la calidad y longitud del cable, y de la
relación señal a ruido de la señal de datos. Los cables coaxiales solían ser ampliamente utilizados en el sistema
telefónico para las líneas de larga distancia, pero en la actualidad han sido reemplazados por la fibra óptica en
rutas de distancias considerables. Sin embargo, el cable coaxial aún se utiliza en la televisión por cable y en las
redes de área metropolitana.
Medios de Transmisión Página 5 de 16

Conectores:
Fibra óptica
Un sistema de transmisión óptico tiene tres componentes: la fuente de luz, el medio de transmisión y el detector.
Convencionalmente, un pulso de luz indica un bit 1 y la ausencia de luz indica un bit 0. El medio de transmisiones
una fibra de vidrio ultra delgada. El detector genera un pulso eléctrico cuando la luz incide en él. Al agregar una
fuente de luz en un extremo de una fibra óptica y un detector en el otro, se tiene un sistema de transmisión de
datos unidireccional que acepta una señal eléctrica, la convierte y transmite mediante pulsos de luz y luego,
reconvierte la salida a una señal eléctrica en el extremo receptor.
Este sistema de transmisión tendría fugas de luz y sería inútil en la práctica excepto por un principio interesante
de la física. Cuando un rayo de luz pasa por un medio a otro, por ejemplo de sílice fundida al aire, el rayo se
refracta (se dobla) en la frontera de la sílice y el aire como se muestra en la figura.
Como se observa, un rayo de luz que incide en la frontera con el ángulo α1 emerge con un ángulo β1. El grado
de refracción depende de las propiedades de los dos medios. Por lo tanto, un rayo de luz que incide en un ángulo
mayor o igual que el crítico queda atrapado dentro de la fibra, como se observa en la figura anterior, y se puede
propagar por varios kilómetros prácticamente sin perdida.
El diagrama de la figura únicamente muestra un rayo atrapado, pero puesto que cualquier rayo de luz que incida
en la frontera con un ángulo mayor al crítico se reflejará internamente, muchos rayos estarán rebotando con
ángulos diferentes. Se dice que cada rayo tiene un modo diferente, por lo que una fibra que tiene esta propiedad
se denomina fibra multimodo.
Por otro lado, si el diámetro de la fibra se reduce a unas cuantas longitudes de ondas de luz, a fibra actúa como
una guía de ondas y la luz se puede propagar sólo en línea recta, sin rebotar, lo cual da como resultado una fibra
monomodo. Las fibras monomodo son más caras, pero se pueden utilizar en distancias más grandes. Las fibras
monomodo disponibles en al actualizada pueden transmitir datos a 50Gbps a una distancia de 100km sin
amplificación.
Medios de Transmisión Página 6 de 16

La longitud de los pulsos de luz transmitidos por una fibra aumenta conforme se propagan. Este fenómeno se
llama dispersión cromática. La magnitud de esta depende de la longitud de onda.
Cables de fibra óptica
Son similares a los coaxiales excepto por el trenzado. Como se observa en la figura, al centro se encuentra el
núcleo de vidrio, a través del cual se propaga la luz. En las fibras multimodo el diámetro es de 50 micras,
aproximadamente el grosor de un cabello humano. En las fibras monomodo el núcleo es de 8 a 10 micras.
El núcleo está rodeado por un revestimiento de vidrio con un índice de refracción menor que el del núcleo, con
el fin de mantener toda la luz en este último. A continuación está una cubierta plástica delgada para proteger al
revestimiento. Las fibras se agrupan en haces, protegidas por una funda exterior.
Las fibras pueden conectarse de tres formas diferentes. Primera, pueden terminar en conectores en insertarse
en enchufes de fibra. Los conectores pierden entre un 10 y 20% de la luz, pero facilitan la reconfiguración de los
sistemas. Segunda, se pueden empalmar de manera mecánica. Los empalmes mecánicos acomodan dos
extremos cortados con cuidado, uno junto a otro, en una manga especial y los sujetan en su lugar. La alineación
se puede mejorar pasando luz a través de la unión y haciendo pequeños ajustes para maximizar la señal. Tercera,
se pueden fusionar (fundir) dos tramos de fibra para formar una conexión sólida.
Tipos
Las diferentes trayectorias que puede seguir un haz de luz en el interior de una fibra se denominan modos de
propagación. Y según el modo de propagación tendremos dos tipos de fibra óptica: multimodo y monomodo.
Fibra multimodo
Una fibra multimodo es aquella en la que los haces de luz pueden circular por más de un modo o camino. Esto
supone que no llegan todos a la vez. Una fibra multimodo puede tener más de mil modos de propagación de
luz. Las fibras multimodo se usan comúnmente en aplicaciones de corta distancia, menores a 2 km, es simple
de diseñar y económico.
El núcleo de una fibra multimodo tiene un índice de refracción superior, pero del mismo orden de magnitud,
que el revestimiento. Debido al gran tamaño del núcleo de una fibra multimodo, es más fácil de conectar y
tiene una mayor tolerancia a componentes de menor precisión.
Medios de Transmisión Página 7 de 16

Dependiendo el tipo de índice de refracción del núcleo, tenemos dos tipos de fibra multimodo:
• Índice escalonado: en este tipo de fibra, el núcleo tiene un índice de refracción constante en toda la sección
cilíndrica, tiene alta dispersión modal.
• Índice gradual: mientras en este tipo, el índice de refracción no es constante, tiene menor dispersión modal
y el núcleo se constituye de distintos materiales.
Además, según el sistema ISO 11801, para clasificación de fibras multimodo, según su ancho de banda se incluye
el formato OM3 (monomodo sobre láser) a los ya existentes OM1 y OM2 (monomodo sobre LED).
• OM1: Fibra 62.5/125 µm, soporta hasta Gigabit Ethernet (1 Gbit/s), usan LED como emisores
• OM2: Fibra 50/125 µm, soporta hasta Gigabit Ethernet (1 Gbit/s), usan LED como emisores
• OM3: Fibra 50/125 µm, soporta hasta 10 Gigabit Ethernet (300 m), usan láser (VCSEL) como emisores.
Bajo OM3 se han conseguido hasta 2000 MHz km (10 Gbit/s), es decir, una velocidad 10 veces mayor que con
OM1.
Alcances máximos
Fibra monomodo
Una fibra monomodo es una fibra óptica en la que sólo se propaga un modo de luz. Se logra reduciendo el
diámetro del núcleo de la fibra hasta un tamaño (8,3 a 10 micrones) que sólo permite un modo de
propagación. Su transmisión es paralela al eje de la fibra. A diferencia de las fibras multimodo, las fibras
monomodo permiten alcanzar grandes distancias (hasta 400 km máximo, mediante un láser de alta intensidad)
y transmitir elevadas tasas de información (decenas de Gbit/s).
Conectores
Medios de Transmisión Página 8 de 16

Pérdida en los cables de Fibra Óptica
A la pérdida de potencia a través del medio se conoce como Atenuación, es expresada en decibelios, con un
valor positivo en dB, es causada por distintos motivos, como la disminución en el ancho de banda del sistema,
velocidad, eficiencia. La fibra de tipo multimodal, tiene mayor pérdida debido a que la onda luminosa se dispersa
originada por las impurezas. Las principales causas de pérdida en el medio son:
• Pérdidas por absorción
• Pérdida de Rayleigh
• Dispersión cromática
• Pérdidas por radiación
• Dispersión modal
• Pérdidas por acoplamiento
Pérdidas por absorción. Ocurre cuando las impurezas en la fibra absorben la luz, y esta se convierte en energía
calorífica; las pérdidas normales van de 1 a 1000 dB/km.
Pérdida de Rayleigh. En el momento de la manufactura de la fibra, existe un momento donde no es líquida ni
sólida y la tensión aplicada durante el enfriamiento puede provocar microscópicas irregularidades que se
quedan permanentemente; cuando los rayos de luz pasan por la fibra, estos se difractan haciendo que la luz
vaya en diferentes direcciones.
Dispersión cromática. Esta dispersión sólo se observa en las fibras tipo unimodal, ocurre cuando los rayos de
luz emitidos por la fuente y se propagan sobre el medio, no llegan al extremo opuesto en el mismo tiempo; esto
se puede solucionar cambiando el emisor fuente.
Pérdidas por radiación. Estas pérdidas se presentan cuando la fibra sufre de dobleces, esto puede ocurrir en la
instalación y variación en la trayectoria, cuando se presenta discontinuidad en el medio.
Dispersión modal. Es la diferencia en los tiempos de propagación de los rayos de luz.
Pérdidas por acoplamiento. Las pérdidas por acoplamiento se dan cuando existen uniones de fibra, se deben a
problemas de alineamiento.
Medios de Transmisión Página 9 de 16

Comparación de la fibra óptica y el alambre de cobre
La fibra tiene muchas ventajas. Para empezar puede manejar anchos de banda muchos mayores que el cobre.
Tan solo por esto, su uso sería indispensable en redes de alto rendimiento. Debido a la baja atenuación, solo se
necesitan repetidores cada 50km aprox. en líneas largas, contra casi cada 5 km cuando se usa cobre, lo que
implica un ahorro considerable. La fibra también tiene la ventaja de que las sobrecargas de energía, la
interferencia electromagnética o los cortes en el suministro de energía no la afectan. Las sustancias corrosivas
del ambiente tampoco la afectan, lo que hace ideal para ambientes fabriles pesados. Por último, las fibras no
tienen fugas de luz y es difícil intervenirlas y conectarse a ellas.
Su parte negativa consiste que requiere habilidades, y en que las fibras pueden dañarse con facilidad si se doblan
demasiado. Debido a que la transmisión óptica es unidireccional, la comunicación en ambos sentidos requiere
de dos fibras o dos bandas de frecuencia en una fibra. Por último, las interfaces de fibra cuestan más que las
eléctricas.
MMMMeeeeddddiiiioooossss ddddeeee ttttrrrraaaassssmmmmiiiissssiiiióóóónnnn nnnnoooo gggguuuuiiiiaaaaddddoooossss
El espectro electromagnético
En la figura se puede observar el espectro electromagnético. Las porciones de radio, microondas, infrarrojo y luz
visible del espectro pueden servir para transmitir información modulando la amplitud, frecuencia o fase de las
ondas. La luz ultravioleta, los rayos X y los rayos gamma serían mejores, debido a sus frecuencias más altas, pero
son difíciles de producir y modular, no se propagan bien entre edificios y son peligrosos para los seres vivos. Las
bandas que se listan en la parte inferior de la figura son los nombre oficiales de la ITU y se basan en las longitudes
de onda, de modo que la banda LF va de 1 a 10 km (aprox. 30 a 300 KHz). Los términos LF, MF y HF se refieren a
las frecuencias baja, media y alta, respectivamente. Como podrá observarse, cuando se asignaron los nombres,
nadie esperaba que se sobrepasarían los 10 MHz, por lo que posteriormente a las bandas más altas se les
nombro como VHF (frecuencia muy alta), UHF (frecuencia ultra alta), EHF (frecuencia extremadamente alta) y
THF (frecuencia tremendamente alta).
Medios de Transmisión Página 10 de 16

Transmisión inalámbrica
Radiotransmisión
Las ondas de radio son fáciles de generar, pueden viajar distancias largas y penetrar edificios sin problemas, y
por ello su uso está muy generalizado en la comunicación. Las ondas de radio también son omnidireccionales,
lo que significa que viajan en todas direcciones a partir de la fuente, por lo que no es necesario que el
transmisor y el receptor se encuentren alineados físicamente.
Las propiedades de las ondas de radio dependen de la frecuencia. A bajas frecuencias, esas ondas cruzan bien
casi cualquier obstáculo, pero la potencia se reduce de manera drástica a medida que se aleja de la fuente. A
frecuencias altas, las ondas de radio tienden a viajar en línea recta y a rebotar en los obstáculos. También son
absorbidas por la lluvia. En todas las frecuencias, las ondas de radio están sujetas a interferencia por los
motores y otros equipos eléctricos.
En las bandas VLF, LF y MF las ondas de radio siguen la curvatura de la Tierra. Estas bandas cruzan con facilidad
los edificios, y es por ello que las radios portátiles funcionan en interiores.
En las bandas HF y VHF, las ondas a nivel del suelo tienden a ser absorbidas por la Tierra, sin embargo las
ondas que alcanzan la ionosfera, se refractan y se envían de regreso a nuestro planeta. En ciertas condiciones
atmosféricas, las señales pueden rebotar varias veces. Los operadores de radio aficionados usan estas bandas
para conversar a larga distancia. El ejército se comunica también en las bandas HF y VHF.
Microondas
Por encima de los 100 MHz las ondas viajan en línea recta y, por lo tanto, se pueden enfocar en un haz
estrecho. Concentrar toda la energía en un haz pequeño con una antena parabólica produce una relación señal
a ruido mucho más alta, pero las antenas transmisora y receptora deben estar bien alineadas entre s.
Medios de Transmisión Página 11 de 16

Antes de la fibra óptica, estas microondas formaron durante décadas el corazón del sistema de transmisión
telefónica de larga distancia.
Cuanto más altas sean las torres, más separadas pueden estar. La distancia entre los repetidores se eleva en
forma muy aproximada con la raíz cuadrada de la altura de las torres. Con torres de 100m de altura, los
repetidores pueden estar separados 80km de distancia.
A diferencia de las ondas de radio a frecuencias más bajas, las microondas no atraviesan bien los edificios.
Algunas ondas pueden refractarse en las capas atmosféricas más bajas y tardar un poco más en legar que las
ondas directas. Las ondas diferidas pueden llegar fuera de fase con la onda directa y cancelar así la señal. Este
efecto se llama desvanecimiento por múltiples trayectorias y con frecuencia es un problema serio que
depende del clima y de la frecuencia.
La creciente demanda de espectro obliga a los operadores a usar frecuencias más altas. Las bandas de hasta
10GHz ahora son de uso rutinario, pero con las de aproximadamente 4GHz surge un problema: son absorbidas
por el agua. Estas ondas solo tienen unos centímetros de longitud y la lluvia las absorbe.
Resumiendo, las comunicaciones por microondas se utilizan tanto para la comunicación telefónica de larga
distancia, los teléfonos celulares, la distribución de la televisión, etcétera, que el espectro se ha vuelto muy
escaso. Las microondas son relativamente baratas. Erigir dos torres sencillas y poner antenas en cada una
puede costar menos que enterrar 50km de fibra a través de un área urbana congestionada o sobre montaña
por ejemplo.
Ondas infrarrojas y milimétricas
Las ondas infrarrojas y milimétricas no guiadas se usan mucho para la comunicación de corto alcance. Todos
los controles remotos de los televisores, grabadoras de video, estéreos, etc., utilizan comunicación infrarroja.
Estos controles son relativamente direccionales, económicos y fáciles de construir, pero tienen un
inconveniente importante: no atraviesan los objetos sólidos. Este inconveniente también es una ventaja, esto
significa que un sistema infrarrojo en un cuarto de un edificio no interferirá con un sistema similar en cuartos
adyacentes. Por esta razón, la seguridad de estos sistemas contra el espionaje es mejor que la de los sistemas
de radio. Además, no es necesario obtener licencia del gobierno para operar un sistema infrarrojo.
La comunicación infrarroja tiene un uso limitado en el escritorio; por ejemplo, para conectar notebooks,
impresoras y otros dispositivos móviles.
Satélites de comunicaciones
En su forma más simple, un satélite de comunicaciones se puede considerar como un enorme repetidor de
microondas desde el cielo. Contiene numerosos transpondedores, cada uno de los cuales se encarga de una
parte del espectro, amplifica la señal entrante y a continuación la retransmite en otra frecuencia para evitar
interferencias con la señal entrante. Los haces pueden ser amplios y cubrir una fracción sustancial de la
superficie de la Tierra, o estrechos y abarcar sólo algunos cientos de kilómetros de diámetro. Este modo de
operación se conoce como de tubo doblado.
Entre más alto esté el satélite, más largo es el periodo. Cerca de la superficie de la Tierra, el periodo es de
aproximadamente 90minutos. En consecuencia, los satélites con orbitas bajas desaparecen de la vista
rápidamente, aunque alguno de ellos son necesarios para proporcionar una cobertura continua.
Otro aspecto importante para determinar dónde colocar un satélite es la presencia de los cinturones de Van
Allen, capas de partículas altamente cargadas de energía, atrapadas por el campo magnético de la Tierra.
Cualquier satélite que vuele dentro de ellas sería destruido rápidamente por las partículas con una alta carga
de energía.
Como se observa en la figura, hay tres regiones para colocar con seguridad los satélites.
Medios de Transmisión Página 12 de 16

Satélites geoestacionarios
Los satélites geoestacionarios son satélites que permanecen siempre en la misma vertical sobre la Tierra. Esto
se consigue luego que el satélite da una vuelta completa a su órbita alrededor de la Tierra en el mismo tiempo
en que la Tierra da una vuelta completa sobre su eje.
La gran ventaja que aportan es que se puede considerar como un punto fijo en cielo, de manera que pueden
encargarse de la transmisión de las comunicaciones entre dos puntos, o del envío de imágenes periódicas,
como enlace de telefonía móvil o para aplicaciones militares, entre muchas otras más.
Cuando se termina el combustible de los motores, por lo general a los 10 años, el satélite comienza a navegar
a la deriva y cae sin remedio, por lo cual es necesario desactivarlo. Con el tiempo la órbita se deteriora y el
satélite reingresa a la atmosfera y se incendia o en ocasiones se estrella contra la Tierra.
Las bandas de frecuencias específicas asignadas a los usuarios de satélites son las que se muestran en la
siguiente imagen.
La banda C fue la primera destinada al tráfico comercial por satélite. Tiene dos rangos de frecuencia, el inferior
para el tráfico descendente o de bajada y el superior para el tráfico ascendente o de subida. Para permitir que
le trafico fluya en ambos sentidos al mismo tiempo, se requieren dos canales, uno para cada sentido. Estas
bandas están sobresaturadas debido a que las empresas portadoras también las utilizan para los enlaces de
microondas terrestres. Las bandas L y S fueron incorporadas en el año 2000 mediante un acuerdo
internacional.
La siguiente banda más ancha disponible para los operadores de telecomunicaciones es la banda Ku (K abajo) y
luego Ka (K arriba) pero el inconveniente en estas bandas es la lluvia y los costos.
Los primeros satélites geoestacionarios tenían un solo haz espacial que iluminaba cerca de un tercio de la
superficie de la Tierra, el cual se conoce como huella. Con la reducción de costos, tamaño y requerimiento de
energía de los componentes microelectronicos, se ha vuelto posible una estrategia de difusión mucho más
refinada. Cada satélite está equipado con múltiples antenas y transpondedores. Cada haz descendente se
puede concentrar en un área geográfica más pequeña, de tal forma que es posible llevar a cabo
simultáneamente una gran cantidad de transmisiones hacia y desde el satélite.
Medios de Transmisión Página 13 de 16

Un avance en el mundo de los satélites de comunicaciones es el desarrollo de microestaciones de bajo costo,
llamadas VSATs (Terminales de Apertura Muy Pequeña). Estas terminales tienen antenas de un metro o
menos.
Satélites de Órbita Terrestre Media
Los satélites MEO (Órbita Terrestre Media) se encuentran a altitudes mucho más bajas, entre los cinturones de
Van Allen. Estos satélites se desplazan lentamente y tardan alrededor de seis horas para dar la vuelta a la
Tierra. Puesto que son menores que los GEO, tienen una huella más pequeña y se requieren transmisores
menos potentes para alcanzarlos.
Un ejemplo de estos satélites son los GPS (Sistema de Posicionamiento Global).
Satélites de Órbita Terrestre Baja
En una altitud más baja se encuentran los satélites LEO (Órbita Terrestre Baja). Debido a la rapidez de su
movimiento, se requieren grandes cantidades de ellos para conformar un sistema completo. Como los satélites
se encuentran tan cercanos a la Tierra, las estaciones terrestres no necesitan mucha potencia y el retardo del
viaje de ida y vuelta es de tan solo algunos milisegundos.
Antenas
Una antena es un dispositivo diseñado con el objetivo de emitir o recibir ondas electromagnéticas hacia el
espacio libre. Una antena transmisora transforma energía eléctrica en ondas electromagnéticas, y una antena
receptora realiza la función inversa.
Existe una gran diversidad de tipos de antenas. Los sistemas de comunicaciones utilizan antenas para realizar
enlaces punto a punto, difundir señales de televisión o radio, o bien transmitir o recibir señales en equipos
portátiles.
Las características de las antenas dependen de la relación entre sus dimensiones y la longitud de onda de la
señal de radiofrecuencia transmitida o recibida. Si las dimensiones de la antena son mucho más pequeñas que
la longitud de onda las antenas se denominan elementales, si tienen dimensiones del orden de media longitud
de onda se llaman resonantes, y si su tamaño es mucho mayor que la longitud de onda son directivas.
Las antenas se caracterizan por una serie de parámetros; los más habituales son:
• Diagrama de radiación
• Ancho de banda
• Directividad
• Ganancia
• Eficiencia
• Impedancia de entrada
• Apertura de haz
• Polarización
• Relación delante/atrás
• Resistencia de radiación
Tipos de antenas
Existen tres tipos básicos de antenas: antenas de hilo, antenas de apertura y antenas planas. Asimismo, las
agrupaciones de estas antenas (arrays) se suelen considerar en la literatura como otro
• Antenas de Hilo
Las antenas de hilo son antenas cuyos elementos radiantes son conductores de hilo que tienen una sección
despreciable respecto a la longitud de onda de trabajo. Las dimensiones suelen ser como máximo de una
longitud de onda. Se utilizan extensamente en las bandas de MF, HF, VHF y UHF. Ejemplos de antenas de hilo
son:
Medios de Transmisión Página 14 de 16

o El monopolo vertical
o El dipolo y su evolución, la antena Yagi
o La antena espira
o La antena helicoidal es un tipo especial de antena que se usa principalmente en VHF y UHF. Un
conductor describe una hélice, consiguiendo así una polarización circular.
• Antenas de Apertura
Las antenas de apertura son aquellas que utilizan superficies o aperturas para direccionar el haz
electromagnético de forma que concentran la emisión y recepción de su sistema radiante en una dirección. La
más conocida y utilizada es la antena parabólica, tanto en enlaces de radio terrestres como de satélite. La
ganancia de dichas antenas está relacionada con la superficie de la parábola, a mayor tamaño mayor colimación
del haz tendremos y por lo tanto mayor directividad.
El elemento radiante es el alimentador, el cual puede iluminar de forma directa a la parábola o en forma
indirecta mediante un subreflector. El alimentador está generalmente ubicado en el foco de la parábola. El
alimentador, en sí mismo, también es una antena de apertura (se denominan antenas de bocina) que puede
utilizarse sin reflector, cuando el objetivo es una cobertura más amplia (ej. cuando se pretende cubrir la totalidad
de la superficie de la tierra desde un satélite en órbita geoestacionaria).
Hay varios tipos de antenas de apertura, como la antena de bocina, la antena parabólica, la antena parabólica
del Radar Doppler y superficies reflectoras en general.
o La antena de bocina
o La antena parabólica
o La antena parabólica del Radar Doppler y
o Superficies reflectoras en general
• Antenas Planas
Un tipo particular de antena plana son las antenas de apertura sintética, típicas de los radares de apertura
sintética (SAR).
• Antena de Array
Antena de Array
Las antenas de array están formadas por un conjunto de dos o más antenas idénticas distribuidas y ordenadas
de tal forma que en su conjunto se comportan como una única antena con un diagrama de radiación propio.
La característica principal de los arrays de antenas es que su diagrama de radiación es modificable, pudiendo
adaptarlo a diferentes aplicaciones/necesidades. Esto se consigue controlando de manera individual la amplitud
y fase de la señal que alimenta a cada uno de los elementos del array.
Medios de Transmisión Página 15 de 16

Atendiendo a la distribución de las antenas que componen un array podemos hacer la siguiente clasificación:
o Arrays lineales: Los elementos están dispuestos sobre una línea.
o Arrays Planos: Los elementos están dispuestos bidimensionalmente sobre un plano.
o Arrays conformados: Los elementos están dispuestos sobre una superficie curva.
A nivel de aplicación los arrays de antenas se utilizan para la construcción de antenas inteligentes.
Medios de Transmisión Página 16 de 16