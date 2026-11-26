UNIVERSIDAD TECNOLÓGICA NACIONAL![](data:image/png;base64...)

Facultad Regional Rosario

Ingeniería en Sistemas de Información

**Asignatura:** Comunicación de datos

**Profesor:** Germán Bernardo Baró y Cristian Medin

**Comisión:** 303

**Integrantes:**

* Juan Pedro Casañas (Legajo: 50373)
* Maria Sofia Ochoa (Legajo: 50452)
* Martin Quagliardi (Legajo: 51657)
* Mateo Regodesebes (Legajo: 51079)

**Año:** 2024

**Trabajo Práctico:** Informe de HFC (Híbrido de fibra coaxial)

# Índice

[**Índice 1**](#_62cn0v7ju9p0)

[**Introducción 2**](#_19nrdr20u0zw)

[**Desarrollo 4**](#_3rf0drqa9yqh)

[Historia del HFC 4](#_r1cqwr9mefae)

[¿Qué es el HFC? 5](#_u15toepa5fx9)

[Arquitectura del HFC 9](#_kilaaq8lms75)

[La cabecera (head-end) 9](#_5zg186azoj9m)

[La red troncal 10](#_ca8wwyz2esae)

[La red de distribución 11](#_d4ijn2aavnc)

[Bucle Local del Abonado 11](#_vyv9w2aac3oo)

[El estándar DOCSIS 12](#_siay09nk943y)

[¿Qué es y cómo está relacionado al HFC? 12](#_lmg4rz53kkh6)

[**Bibliografía 16**](#_sizwfmw40ndl)

[**Anexo: Preguntas y Respuestas 17**](#_m2vrcmbsmd1s)

#

# Introducción

En la era digital en la que vivimos, donde la conectividad y la comunicación son esenciales para la vida cotidiana y el funcionamiento de la sociedad, las infraestructuras y los diferentes protocolos relacionados a las telecomunicaciones juegan un papel fundamental. Entre estas infraestructuras, una tecnología que ha revolucionado la transmisión de datos es el **Híbrido de Fibra Coaxial (HFC)**.

El **HFC** representa una innovadora combinación de tecnologías de transmisión de datos, que incluye tanto la *fibra óptica* como el *cable coaxial*. Esta convergencia de medios ha permitido la transmisión eficiente de una amplia gama de servicios, desde televisión por cable hasta internet de alta velocidad y telefonía digital. En un mundo donde la demanda de ancho de banda y velocidad de conexión sigue creciendo exponencialmente cada día, el HFC se destaca como una solución versátil y robusta para satisfacer estas necesidades.

Para comprender adecuadamente el funcionamiento y el impacto del HFC en nuestra sociedad moderna, es crucial explorar sus componentes y su arquitectura. La fibra óptica, con su capacidad para transportar grandes volúmenes de datos a velocidades ultra rápidas a través de pulsos de luz, constituye la columna vertebral de esta tecnología. Por otro lado, el cable coaxial, con su capacidad para transmitir señales de alta frecuencia a largas distancias, complementa la fibra óptica al llevar la conexión directamente a los hogares y las empresas.

Entonces, vamos a desarrollar en las siguientes páginas el mundo del Híbrido de Fibra Coaxial (HFC), explorando sus orígenes, su evolución y su papel en la revolución digital en curso. Desde las primeras implementaciones en los sistemas de televisión por cable hasta su papel crucial en el despliegue de la banda ancha de alta velocidad: esta tecnología transformó la manera en la que nos comunicamos, trabajamos y nos entretenemos.

Además, examinaremos los desafíos y oportunidades que el HFC enfrenta en un entorno caracterizado por la rápida evolución de las tecnologías de comunicación. Desde la creciente competencia de las redes de fibra óptica pura hasta los avances en tecnologías inalámbricas, analizaremos cómo el HFC se adapta y mejora para mantener su relevancia en un panorama cambiante.

# Desarrollo

Para comenzar, nos parece útil ponernos en contexto y profundizar en la historia que tiene este concepto, desde sus orígenes hasta como lo conocemos hoy en día.

## Historia del HFC

La primera aplicación del cable coaxial para la transmisión de señales de televisión surgió en los Estados Unidos a finales de la década de 1940, dando origen al concepto de televisión por cable (**CATV**), entonces conocida como televisión por antena comunitaria. John Walson, dueño de una tienda en la localidad de Mahanoy (Pensilvania), tuvo que lidiar con el desafío de vender televisores a los residentes locales, quienes evaluaban una señal de recepción extremadamente débil debido a la ubicación geográfica del valle en el que se encontraba la ciudad, a unos 150 kilómetros de distancia de la estación transmisora en Filadelfia. Las montañas alrededor obstaculizaban el flujo de la señal hasta los hogares. Fue entonces cuando Walson ideó la instalación de una antena en una colina cercana y la transmisión de la señal hasta su tienda mediante cable coaxial, utilizando amplificadores que él mismo construyó.

Posteriormente, hacia la década de 1950, se comenzaron a explorar sistemas de microondas para captar señales de televisión provenientes de ciudades lejanas. Otro hito importante en la historia de las redes de televisión por cable fue el desarrollo de la televisión de pago (pay-TV).

Dado el crecimiento de la demanda del número de canales se requirió aumentar el ancho de banda disponible en los sistemas de cable, esto de la mano con la atenuación natural que presentan las redes de cobre para transmisiones en altas frecuencias, hizo necesaria la implementación de largas cadenas de amplificadores electrónicos de radiofrecuencia, aportándose un mayor incremento del ruido y la distorsión de cada amplificador a lo largo de la red de accesos y distribución, originando así el deterioro progresivo de la calidad de la señal de TV. En base a estas limitaciones es que se origina la necesidad de introducir la fibra óptica, que ganó afianzamiento con las implementaciones de dispositivos de alta linealidad. Este es el origen de las redes **HFC**.

A medida que avanzaba la tecnología, las redes de TV por cable evolucionaron para ofrecer una gama más amplia de servicios multimedia, como el Video on Demand y Pay Per View. Posteriormente, se adaptaron para incluir telefonía y acceso a Internet de banda ancha, convirtiéndose en Operadores Multi-Servicio (**MSO**). Esta transformación implicó importantes modificaciones en las redes existentes, convirtiéndolas en redes HFC bidireccionales desbalanceadas. La introducción de tecnología óptica permitió, además, la transmisión bidireccional *a largas distancias*, de este modo las redes de cable pasaron de ser sistemas de pura distribución a convertirse en sistemas completos de telecomunicaciones, capaces de proporcionar servicios interactivos de voz y datos.

La década de 1990 marcó un hito con la introducción de la televisión digital, que aumentó significativamente la capacidad de los sistemas para transportar canales y ofrecer mayor calidad de imagen y sonido, así como nuevas funciones interactivas. Esta evolución se caracterizó por la reducción de costos, la integración de la fibra óptica en las redes de CATV, la aparición de amplificadores bidireccionales y la **estandarización** de tecnologías como DOCSIS y HFC para cable módems.

Hoy por hoy, el HFC continúa siendo una tecnología ampliamente utilizada en muchos lugares, especialmente en áreas urbanas y suburbanas. A lo largo de los años, ha habido avances significativos en la eficiencia y la capacidad de las redes HFC, con la implementación de tecnologías como DOCSIS 3.1 que permiten velocidades de Internet aún más rápidas y una mayor capacidad de transmisión de datos. Además, el HFC sigue siendo una opción popular para la entrega de servicios de televisión, Internet y telefonía debido a su confiabilidad y asequibilidad. Sin embargo, también se están explorando nuevas tecnologías, como las redes de fibra óptica pura, para satisfacer las demandas cada vez mayores de ancho de banda y velocidad en la era digital.

## ¿Qué es el HFC?

Un cable HFC puede tomar varías formas físicas dependiendo de su construcción. En su forma más básica consiste en un cable tipo taller que lleva en su interior un cable coaxial y un cable de fibra óptica (Figura 1) aunque también puede adquirir otras formas como la de la figura 2.

Figura 1. Figura 2.![fibra optica cable hfc docsis 3.1](data:image/jpeg;base64...)![](data:image/jpeg;base64...)

Definamos primero los dos cables que componen al cable híbrido:

Un cable coaxial consiste físicamente de un núcleo sólido de cobre envuelto en un aislante, un apantallamiento de alambre de tierra, blindaje y otra cubierta protectora. Una de las características principales del cable coaxial es la conexión de dispositivos a mayores distancias que el entonces cable par trenzado, lo que lo hacía más solicitado en redes ETHERNET y ARCNET.

La no obstrucción de señales externas y el eficiente transporte con atenuación mínima en un gran ancho de banda lo diferencian de un cable normal.

La principal desventaja del cable coaxial es el transporte en grandes distancias de señales de alta frecuencia pues el ruido se hace mayor que la señal lo que exige implementar amplificadores que terminan por aumentar el costo de la red.

Por su parte la fibra óptica se caracteriza por dos construcciones básicas según el cable: De estructura holgada y de estructura ajustada.

En el caso de un cable de fibra óptica de estructura holgada, la fibra está constituida por varios tubos de fibra protegidos por una cubierta protectora que rodean el refuerzo del cable. Los tubos tienen entre 2 y 3 milímetros de diámetro y generalmente se encuentran rellenos de gel para otorgarles resistencia al agua. La característica principal de esta construcción es que el tubo de holgado incomunica a la fibra y la protege de las fuerzas mecánicas del exterior.

![](data:image/png;base64...)

Por otra parte, en el cable de estructura ajustada, se encuentran presentes diversas fibras que rodean el centro del cable, cubiertas de una capa de protección exterior. El recubrimiento de la fibra óptica es de aproximadamente 250 μm y está, a su vez, protegido por una cubierta plástica de 900 μm. La protección secundaria que actúa como una protección adicional ante el entorno procede también como soporte físico, lo que admite que este sea conectado directamente sin protección en los empalmes de manera que, en algunos casos, este tipo de estructura disminuye el costo de la instalación.

![](data:image/png;base64...)

La principales ventajas de la fibra óptica por sobre otros cables son una mayor velocidad de transmisión ya que las señales son transmitidas a la velocidad de la luz, una mayor capacidad de transmisión con capacidad de cubrir grandes distancias sin repetidores, inmunidad total ante las interferencias producidas por aparatos electromagnéticos, puesto que la fibra no es un material conductor y una alta tolerancia a una gran amplitud de temperaturas (De -40°C a 400°C).

Por otra parte la fibra óptica tiene como desventajas principales su costo, su fragilidad antes daños físicos, el costo de sus transmisores y receptores y la dificultad de reparación.

Habiendo observado las propiedades de ambos materiales, el resultado que obtenemos al utilizar un cable HFC es un cable de un rendimiento casi tan alto como un cable puramente de fibra óptica pero con un costo de instalación mucho menor a la misma, además de ser un cable altamente resistente al ruido y la interferencia. Como desventaja principal tenemos que, al introducir un cable coaxial dentro del cable de fibra, perdemos su propiedad de no conductor y por ende el mismo se vuelve susceptible a impactos de rayos, bajadas de tensión y demás fenómenos eléctricos que no afectarían a un cable tradicional de fibra óptica.

## Arquitectura del HFC

![](data:image/png;base64...)

Una red HFC es una red de telecomunicaciones por cable que combina la fibra óptica y el cable coaxial como soportes para la transmisión de las señales. La arquitectura de una red HFC está compuesta por cuatro partes diferenciadas:

* La cabecera.
* La red troncal.
* La red de distribución.
* El Bucle local de abonado.

### La cabecera (head-end)

La cabecera, el epicentro desde el cual se gestiona toda la red, varía en complejidad según los servicios que debe brindar. Consiste en la instalación de una oficina de CATV, que origina y comunica los servicios de TV y cable módems a los suscriptores. Una cabecera de red puede atender millones de hogares.

Por ejemplo, para la distribución de señales unidireccionales de televisión, tanto analógicas como digitales, la cabecera cuenta con una variedad de equipos que recopilan todas las fuentes de información, ya sea vía satélite, enlaces terrestres o producción propia, para transmitirlas por la red, ubicándolas en los canales del espectro del cable. La cabecera agrega, comprime y multiplexa las distintas señales ofrecidas por el operador de cable. A la par de su función de distribución, la cabecera se encarga de monitorear y supervisar el correcto funcionamiento de la red.

### La red troncal

La red troncal es la encargada de repartir la señal compuesta, generada por la cabecera a todas las zonas de distribución que abarca la red de cable. Para ello, hace uso de una estructura interna compuesta por anillos, nodos primarios y nodos secundarios.

La red troncal se caracteriza por su estructura de anillos redundantes de fibra óptica, que conectan varios nodos primarios. Estos nodos, a su vez, alimentan a nodos secundarios mediante enlaces punto a punto o anillos. En los nodos secundarios, las señales ópticas se transforman en señales eléctricas y se distribuyen a los hogares de los suscriptores a través de una red de distribución de tipo bus de coaxial. Cada nodo sirve a un número limitado de hogares, lo que permite el uso de hasta 2 o 3 amplificadores de banda ancha como máximo.

La evolución de las redes de CATV hacia las redes HFC comenzó con la sustitución de las largas cascadas de amplificadores y el cable coaxial de la red troncal por enlaces punto a punto de fibra óptica. Con el tiempo, la fibra óptica ha penetrado más en la red de cable, transformando la red troncal en una estructura con anillos redundantes que unen nodos ópticos entre sí. En estos nodos ópticos, las señales downstream pasan de ópticas a eléctricas. Además, en sistemas bidireccionales, los nodos ópticos también reciben las señales del canal de retorno o ascendentes, las convierten en señales ópticas y las transmiten a la cabecera. En resumen la red troncal:

* Es una red óptica con una topología a dos niveles.
* Posee cobertura geográfica amplia.
* Se encarga del transporte de la señal desde la cabecera hasta los puntos de distribución.

![](data:image/png;base64...)

### La red de distribución

La red de distribución cumple la función crucial de llevar la señal desde la cabecera hasta los usuarios. Está formada por una estructura tipo bus de coaxial que transporta las señales downstream hasta la última derivación antes de llegar al hogar del abonado. Esta red incluye nodos secundarios donde se realiza la conversión óptica/eléctrica y se distribuyen las señales a los abonados a través del bus coaxial. Su principal objetivo es multiplexar la información y adaptar el sistema de transporte a las características específicas del bucle de abonado.

### Bucle Local del Abonado

Es la instalación interna del edificio, el último tramo antes de la base de conexión. Es crucial asegurar una instalación estética y de calidad para garantizar una óptima señal y así elevar la experiencia del usuario.

En esta instalación existe una interacción entre dos dispositivos, el Set Top Box, el CMTS y el cable módem dispuesto por el usuario

El Set Top Box (STB), o decodificador, es un dispositivo encargado de recibir y, opcionalmente, decodificar señales de televisión, ya sea analógicas o digitales, para mostrarlas en un dispositivo de televisión.

Por otro lado, el cable módem es un dispositivo que permite a los usuarios conectarse a la red de cable para la transmisión de datos y el acceso a Internet a velocidades de hasta 40Mbps. Este dispositivo sintoniza el canal de televisión elegido para los datos y extrae la información relevante, tanto para el usuario como para el envío de datos a otros usuarios, ya sea en la misma red (cabecera local) o en una red diferente. Se puede conectar al ordenador del usuario a través de la interfaz Ethernet de 10/100 Mbps, que ofrece alta velocidad y bajo costo, o mediante un puerto USB.

Entre las funciones de cable módem podemos mencionar:

* Captar/generar señal de radiofrecuencia
* Modular/demodular los datos
* Generar/verificar la información de control de errores (FEC)
* Encriptar/desencriptar la información
* Respetar el protocolo MAC en upstream
* Gestión y control del tráfico (Limitación del caudal, número de Pcs conectados)

## El estándar DOCSIS

### ¿Qué es y cómo está relacionado al HFC?

Con la creación de redes HFC debió especificar un conjunto de estándares llamado DOCSIS (Data Over Cable Service Interface Specification, en español: Especificación de Interfaz para Servicios de Datos por Cable).

DOCSIS no es más que un estándar internacional de telecomunicaciones que permite la adición de **transferencia de datos a alta velocidad** a un sistema de televisión por cable (CATV). Es usado por varios operadores de televisión por cable para proporcionar conexión a internet por cable sobre la preexistente infraestructura de HFC.

Haciendo énfasis en la preexistencia de una infraestructura de HFC o tan solo de cable coaxial que permitiese la transmisión de televisión por cable, el estándar DOCSIS **no** fue algo impuesto a la fuerza a lo que los operadores de cable tuvieron que adaptarse. Sino que fue una mejora que permitió a los operadores de cable, abstenerse de tener que desarrollar otra infraestructura para el servicio de transferencia de datos a alta velocidad.

Este estándar define los requisitos de la interfaz de comunicaciones y operaciones para los datos sobre sistemas de cable, lo que garantiza la interoperabilidad de la tecnología empleada en la transmisión de datos a alta velocidad en una red de cable.

Sin embargo, con la creciente popularidad y demanda de Internet de fibra óptica de alta velocidad, las redes de cable se enfrentan a un desafío importante que han enfrentado como resultado de la evolución continua del estándar DOCSIS. Esto les ha permitido seguir siendo competitivos y mejorar sus servicios.

Entre otras cosas, la tecnología DOCSIS permite:

* Acceso directo a Internet mediante un cable módem
* Puerta de enlace (“Gateway”) de voz para telefonía
* Dispositivo combinado con voz, conexión inalámbrica Wi-Fi e Internet
* Decodificadores para proporcionar servicios de Internet y video (TV)
* Integración en otros puntos dentro de una red de cable
* Monitoreo del estado de la red para los operadores de cable

Hoy por hoy, DOCSIS se encuentra en la versión 4.0 pero ha tenido un avance considerable desde su primera versión. En la versión 4.0 se define la misma velocidad de descarga de 10 Gbits/s que había en DOCSIS 3.0, pero se sube la de subida a otros 10 Gbits/s ofreciendo un servicio de alta velocidad simétrico, ya que ahora las comunicaciones ,llamadas de voz, video, tienen que permitirse de las altas velocidades que demandan sectores como el streaming y gaming.

DOCSIS 4.0 representa un avance significativo en la evolución de las redes de cable HFC, ofreciendo mejoras sustanciales en velocidades de transmisión y eficiencia espectral. Esta nueva especificación introduce capacidades avanzadas para soportar velocidades simétricas y asimétricas más rápidas como ya hemos mencionado, optimizando así la capacidad de las redes para manejar el creciente tráfico de datos. Además, Full Duplex DOCSIS, una innovación clave dentro del estándar DOCSIS 4.0, permite la transmisión simultánea de datos en ambos sentidos del cable coaxial, mejorando significativamente la eficiencia y la latencia. Esta capacidad bidireccional abre nuevas posibilidades para aplicaciones sensibles a la latencia y servicios emergentes que requieren altos niveles de rendimiento y fiabilidad en la red.

**Conclusiones**

Podemos concluir a partir del estudio detallado de los cables HFC, en conjunto con el estándar DOCSIS, que nos encontramos frente un canal actualizado y esencial en las infraestructuras de telecomunicaciones modernas. Estos cables, que combinan fibra óptica y coaxil, son fundamentales para proporcionar conexiones de banda ancha de alta velocidad tanto a hogares como a empresas.

Físicamente, los cables HFC consisten en un núcleo de coaxil que permite la distribución eficiente de señales de RF y una capa exterior de fibra óptica que transporta datos de alta velocidad. Esta combinación ofrece una solución robusta y escalable que puede adaptarse a diferentes necesidades de conectividad en entornos urbanos y suburbanos sin alcanzar el elevado costo que conlleva un cable de fibra óptica pura.

Con el objetivo de aprovechar al máximo las capacidades físicas de los cables HFC hemos visto cómo la evolución hacia estándares como DOCSIS 4.0 ha mejorado significativamente la capacidad de dichos cables para transportar grandes volúmenes de datos, permitiendo velocidades de descarga y carga más rápidas. En conjunto con el desarrollo de este estándar, la llegada de Full Duplex DOCSIS representa un avance crucial al permitir la transmisión bidireccional simultánea sobre el mismo segmento de cable coaxial. Esto no solo mejora la eficiencia de la red al reducir la latencia y aumentar la capacidad de respuesta para aplicaciones críticas, sino que también amplía las posibilidades para servicios avanzados como por ejemplo la comunicación en tiempo real.

En definitiva, los cables HFC y sus tecnologías asociadas no solo están moldeando el presente de las telecomunicaciones, sino que también están sentando las bases para un futuro conectado y eficiente.

# Bibliografía

* Arquitectura de Red HFC. (<https://es.scribd.com/presentation/316978426/Arquitectura-de-Red-HFC>)
* HENRY A. B. MELÉNDEZ y HÉCTOR D. C. NAVARRO, A. (2005) PASADO, PRESENTE Y FUTURO DE LAS REDES HÍBRIDAS FIBRA COAXIAL Monografía de Ingeniería de Sistemas y Computación UNIVERSIDAD TECNOLÓGICA DE BOLIVAR (<https://repositorio.utb.edu.co/handle/20.500.12585/1637>)
* HENRY A. B. MELÉNDEZ y HÉCTOR D. C. NAVARRO, A. (2005) TECNOLOGÍA DE REDES DE BANDA ANCHA REDES HFC. Tesis de ingeniería electrónica. UNIVERSIDAD TECNOLÓGICA DE BOLIVAR (<https://biblioteca.utb.edu.co/notas/tesis/0028401.pdf>)
* RED HFC (Hybrid fiber-coaxial) (<https://www.academia.edu/31779501/RED_HFC_Hibrid_fiber_coaxial>)
* UNIVERSAL COMMUNICATIONS GROUP NEW ZEALAND (<https://ucg.co.nz/hybrid-fibre-coaxial/>)

# Anexo: Preguntas y Respuestas

1. **¿Qué cables componen al cable híbrido?**

Un cable HFC puede tomar varias formas físicas dependiendo de su construcción. La más básica consiste en un cable tipo taller que lleva en su interior un cable coaxial y un cable de fibra óptica.

1. **¿En qué consisten los cables que componen al HFC?**

El cable coaxial consiste físicamente de un núcleo sólido de cobre envuelto en un aislante, un apantallamiento de alambre de tierra, blindaje y otra cubierta protectora. Una de las características principales del cable coaxial es la conexión de dispositivos a mayores distancias que el entonces cable par trenzado.

Por otro lado, la fibra óptica se caracteriza por dos construcciones básicas según el cable: De estructura holgada, donde la fibra está constituida por varios tubos de fibra protegidos por una cubierta protectora que rodean el refuerzo del cable; y de estructura ajustada, en el cual se encuentran presentes distintas fibras que rodean el centro del cable, cubiertas de una capa de protección exterior.

1. **¿Qué desventajas poseen los tipos de cable que componen el HFC?**

La principal desventaja del cable coaxial es el transporte en grandes distancias de señales de alta frecuencia pues el ruido se hace mayor que la señal lo que exige implementar amplificadores que terminan por aumentar el costo de la red.

Por otra parte la fibra óptica tiene como desventajas principales su costo, su fragilidad antes daños físicos, el costo de sus transmisores y receptores y la dificultad de reparación.

1. **¿Qué es una red HFC? ¿Cómo se compone?**

Una red HFC es una red de telecomunicaciones por cable que combina la fibra óptica y el cable coaxial como soportes para la transmisión de las señales. La arquitectura de una red HFC está compuesta por cuatro partes diferenciadas:

* La cabecera.
* La red troncal.
* La red de distribución.
* El Bucle local de abonado.

1. **Describa brevemente los componentes de una red HFC.**

* *Cabecera*: el epicentro desde el cual se gestiona toda la red, varía en complejidad según los servicios que debe brindar. Consiste en la instalación de una oficina de CATV, que origina y comunica los servicios de TV y cable módems a los suscriptores.
* *Red troncal*: encargada de repartir la señal compuesta, generada por la cabecera a todas las zonas de distribución que abarca la red de cable. Para ello, hace uso de una estructura interna compuesta por anillos, nodos primarios y nodos secundarios.
* *Red de distribución*: cumple la función crucial de llevar la señal desde la cabecera hasta los usuarios. Está formada por una estructura tipo bus de coaxial que transporta las señales downstream hasta la última derivación antes de llegar al hogar del abonado.
* *Bucle local del abonado:* Es la instalación interna del edificio, el último tramo antes de la base de conexión.

1. **¿Qué es el estándar DOCSIS?**

DOCSIS (Data Over Cable Service Interface Specification, en español: Especificación de Interfaz para Servicios de Datos por Cable) es un estándar internacional de telecomunicaciones que permite la adición de transferencia de datos a alta velocidad a un sistema de televisión por cable (CATV). El DOCSIS entonces proporciona una conexión a internet por cable sobre la preexistente infraestructura de HFC.

1. **¿Qué permite la tecnología DOCSIS?**

Entre otras cosas, la tecnología DOCSIS permite:

* Acceso directo a Internet mediante un cable módem
* Puerta de enlace (“Gateway”) de voz para telefonía
* Dispositivo combinado con voz, conexión inalámbrica Wi-Fi e Internet
* Decodificadores para proporcionar servicios de Internet y video (TV)
* Integración en otros puntos dentro de una red de cable
* Monitoreo del estado de la red para los operadores de cable

1. **Enumere las mejoras que la versión 4.0 de DOCSIS.**

Este estándar internacional de telecomunicaciones ha tenido considerables avances desde su primera versión hasta la actual. DOCSIS 4.0 define una velocidad de descarga de 10 Gbits/s ofreciendo un servicio de alta velocidad simétrico. Además representa un avance significativo en la evolución de las redes de cables HFC ofreciendo mejoras sustanciales en velocidades de transmisión y eficiencia espectral. Por otro lado, Full Duplex DOCSIS, una innovación clave dentro del estándar DOCSIS 4.0, permite la transmisión simultánea de datos en ambos sentidos del cable coaxial, mejorando significativamente la eficiencia y la latencia.