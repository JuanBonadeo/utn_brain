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

**Trabajo Práctico:**  Internet de las cosas (IoT)

**Año:** 2024

Índice

[**Introducción 3**](#_4e0qhiihdx8b)

[**Desarrollo 4**](#_8cw23tf1tq15)

[Evolución del internet de las cosas 4](#_jitf6qy1zb2)

[Dispositivos IoT 6](#_1rbiuz9u8cw)

[Aplicaciones de IoT 7](#_fiv95h1d048r)

[Aplicaciones de consumo 7](#_vl5sz5gsds02)

[Domótica 8](#_vsj3scmxo7qh)

[Cuidado de adultos mayores 8](#_dky8kh8dt0x1)

[Aplicaciones comerciales 9](#_w31cbgvaehw6)

[Medicina 9](#_fx0u95owqg0p)

[Transporte 10](#_gz92j59x8hf)

[Industrial 11](#_rl5297w2du0l)

[Infraestructura 12](#_6fxycixrsao1)

[Tecnología RFID 14](#_8cr66kcxq2b)

[Militares 16](#_lgzqnm80mh88)

[Arquitectura IoT 16](#_v0mlzgwt489b)

[Tecnologías de redes de corto alcance y bajo consumo 18](#_83b4b8qh01ax)

[Zigbee 18](#_k095y6d1s2vp)

[Bluetooth Low Energy (BLE) 18](#_n6b3c5evrn9i)

[Near Field Communication (NFC) 19](#_eg6t1vso5fpw)

[Wi-Fi/802.11 19](#_8l3wc8ru1nx2)

[Z-Wave 20](#_21sxyu20nn5)

[Sistemas embebidos 20](#_3hca7c4e3yp)

[Historia de los sistemas embebidos 20](#_rc5pupj6rby)

[Definición de un sistema embebido 21](#_9uy62szf7oha)

[Componentes de los sistemas embebidos 22](#_br4hacgv8czh)

[Arduino y su impacto en el IoT 23](#_m3h5nlyczumq)

[Raspberry Pi y su impacto en el mundo IoT 24](#_jsuk5s6kg3wl)

[Computación en la nube (o Cloud Computing) 25](#_altndyrlewij)

[¿Qué es la computación en la nube? 25](#_xy44gf2tu0i6)

[¿Qué relación guarda el Cloud Computing con el IoT? 25](#_is8v0frjxnfn)

[Modelos de computación en la nube 26](#_boofq6qiqv2)

[Tipos de Nube 26](#_uky9u5qrrxrd)

[Ventajas y desventajas del Cloud Computing 27](#_cswxcl4kt111)

[Métricas y analíticas en el IoT 28](#_ej4ryl7hqopi)

[Análisis de datos en el IoT 29](#_jg0tot6w22wi)

[Herramientas para el análisis de datos 30](#_zmpmuhujyxu)

[Beneficios de la Toma de Decisiones en Tiempo Real 31](#_yueiy7n1kgxh)

[Consideraciones Éticas 31](#_kjgpwyihq5vw)

[¿Por qué es importante el IoT? 32](#_kwqfrksudpjn)

[La evolución de la web 32](#_d0nn6qeffv3)

[IoT: La primera evolución del Internet 33](#_o6b3546fgptm)

[Retos y barreras para el IoT 33](#_2h69vvy3n9xx)

[La implementación de IPv6 33](#_i5yvegv9nsrq)

[Fuente de energía de los sensores. 34](#_t8li02bym4i7)

[Estándares. 35](#_ahp3kx5nfiqb)

[Disponibilidad y Confiabilidad 36](#_wb5rsmb0n251)

[Almacenamiento y Procesamiento de Datos 36](#_ghdnwj9op6q)

[Seguridad y Privacidad 36](#_bm4b6s9qbjdo)

[El futuro de IoT 37](#_petdntwsrlj6)

[**Conclusiones 39**](#_9gjzz6cpfz0j)

[**Bibliografía 40**](#_4t8zfg2jsaww)

[**Anexo: Autoevaluación con Preguntas y Respuestas 41**](#_frp14kkq8b1o)

# Introducción

En las últimas décadas, hemos sido testigos de un avance significativo en el desarrollo de dispositivos y electrodomésticos que no sólo resuelven problemas cotidianos, sino que también optimizan y simplifican nuestras actividades diarias. Sin embargo, hemos llegado a un punto en el que el verdadero potencial de estos dispositivos no reside únicamente en sus funciones individuales, sino en su capacidad para comunicarse y trabajar de manera coordinada. Este enfoque colaborativo es precisamente lo que define el concepto de Internet de las Cosas (**IoT**, por sus siglas en inglés).

El **IoT** se refiere a la *interconexión de dispositivos y objetos cotidianos a través de la red*, permitiéndoles recopilar y compartir datos entre sí de forma autónoma. Esta interconexión crea un ecosistema inteligente en el que los dispositivos, desde electrodomésticos hasta sistemas de seguridad y vehículos, no solo responden a nuestras necesidades de manera individual, sino que también cooperan entre sí para mejorar la eficiencia, la comodidad y la seguridad en nuestras vidas.

Este campo emergente va más allá de la simple automatización, integrando tecnologías avanzadas como la inteligencia artificial y el aprendizaje automático, lo que permite que los dispositivos no solo ejecuten tareas, sino que también aprendan y se adapten a nuestras preferencias y patrones de comportamiento. Así, el **IoT** se está convirtiendo en una parte integral de la revolución digital que transforma nuestra sociedad, conectando el mundo físico con el digital de maneras que apenas comenzamos a comprender.

En este trabajo ahondaremos en detalle sobre lo que es el IoT, explorando sus principales características y sus aplicaciones más relevantes en diversos sectores, entre otras cosas.

# Desarrollo

Retomando la introducción entonces, el Internet de las cosas se puede pensar como una red de dispositivos físicos, vehículos, electrodomésticos y otros objetos físicos que llevan incorporados sensores, software y conectividad de red, lo que les permite recopilar y compartir datos.

## Evolución del internet de las cosas

El concepto inicial presentado por Kevin Ashton se basa en agregar tecnología (RFID[[1]](#footnote-0)) en la cadena de suministro de la empresa Procter & Gamble, para de esta forma hacer posible que los objetos o cosas fueran capaces de generar o entregar información de manera directa, eliminando o sustituyendo la participación de las personas. Para esa época, este cambio en el enfoque de alimentar a los sistemas, aunque pareciera simple, en realidad era muy revolucionario pues, hasta ese entonces, prácticamente toda la información con la que se alimentaba a los sistemas provenía o era suministrada por personas.

Ashton, junto con otros investigadores como Chui, Loffer y Roberts (2010), realizaron una revisión de los avances en ese período y anticiparon un cambio significativo en las formas de generación de información, prediciendo que el mundo físico se convertiría en el principal generador de datos. Este cambio se caracterizaría por tres elementos clave: 1) la producción masiva de datos, 2) el desarrollo de tecnologías para su almacenamiento, procesamiento y análisis, y 3) el funcionamiento autónomo sin necesidad de intervención humana.

En la actualidad, cualquier dispositivo capaz de conectarse a otros se considera parte del Internet de las Cosas (IoT). Esta industria tiene un valor global valuado en los cientos de billones; Además de estos impresionantes números, el potencial de crecimiento de la industria sigue siendo considerable; algunos estudios sugieren que para el 2030 el número de dispositivos conectados superará los 25 billones y el valor económico alcanzará entre 4 y 5 trillones de dólares para 2025

![](data:image/png;base64...)

Entre los factores principales que han impulsado el crecimiento y desarrollo del Internet de las cosas hacia está enorme industria encontramos:

* **Conectividad Ubicua**: La expansión de tecnologías que permiten una conectividad constante y a bajo costo, con velocidades elevadas, facilita que prácticamente cualquier objeto pueda conectarse a la red.
* **Adopción Generalizada del Protocolo IP**: El protocolo IP se ha establecido como el estándar global para redes de datos y aplicaciones de software, lo que simplifica y abate el costo de integrarlo en una amplia variedad de dispositivos.
* **Progreso en la Industria de la Computación**: La constante mejora en la potencia de procesamiento de los dispositivos, junto con la reducción de costos y consumo energético, contribuye al avance de la tecnología.
* **Miniaturización de Componentes**: Los avances en la producción de componentes electrónicos y de comunicación cada vez más pequeños permiten integrarlos en objetos de dimensiones reducidas.
* **Avances en el Análisis de Datos**: La evolución de nuevos algoritmos y el aumento en capacidad de procesamiento, almacenamiento en la nube y servicios relacionados facilitan el análisis de grandes volúmenes de datos, así como la extracción de información valiosa.
* **Desarrollo del Cómputo en la Nube**: La disponibilidad de recursos computacionales de manera remota y la gestión de información en la nube permiten a los dispositivos pequeños acceder a capacidades de procesamiento y análisis avanzadas de forma remota.

## Dispositivos IoT

Los dispositivos **IoT** -también conocidos como "objetos inteligentes"- pueden ser desde dispositivos simples domésticos, como termostatos inteligentes, hasta dispositivos para llevar puestos, como relojes inteligentes y ropa con RFID, pasando por maquinaria industrial compleja y sistemas de transporte. Los tecnólogos incluso imaginan "ciudades inteligentes" enteras basadas en tecnologías **IoT**.

**IoT** permite a estos dispositivos inteligentes comunicarse entre sí y con otros dispositivos habilitados para Internet. Como los teléfonos inteligentes y las pasarelas, creando una vasta red de dispositivos interconectados que pueden intercambiar datos y realizar diversas tareas de forma autónoma. Esto puede incluir

* Controlar las condiciones ambientales en las granjas
* Gestión del tráfico con coches inteligentes y otros dispositivos de automoción inteligentes
* Control de máquinas y procesos en fábricas
* Seguimiento de inventarios y envíos en almacenes

Las aplicaciones potenciales de la IO son vastas y variadas, y su impacto ya se deja sentir en una amplia gama de sectores, como la fabricación, el transporte, la sanidad y la agricultura. A medida que aumente el número de dispositivos conectados a Internet, es probable que la IO desempeñe un papel cada vez más importante en la configuración de nuestro mundo. Transformará nuestra forma de vivir, trabajar e interactuar.

En el contexto empresarial, los dispositivos IoT se utilizan para controlar una amplia gama de parámetros, como la temperatura, la humedad, la calidad del aire, el consumo de energía y el rendimiento de las máquinas. Estos datos pueden analizarse en tiempo real para identificar patrones, tendencias y anomalías que pueden ayudar a las empresas a optimizar sus operaciones y mejorar sus resultados.

## Aplicaciones de IoT

Las aplicaciones para dispositivos conectados a internet son amplias. Múltiples categorías han sido sugeridas, pero la mayoría está de acuerdo en separar las aplicaciones en cinco principales ramas de uso: consumo, comerciales, industriales, de infraestructuras y militares.

La capacidad de conectar dispositivos embebidos con capacidades limitadas de CPU, memoria y energía significa que el IoT puede tener aplicaciones en casi cualquier área. Estos sistemas podrían encargarse de recolectar información en diferentes entornos: desde ecosistemas naturales hasta edificios y fábricas, por lo que podrían utilizarse para monitoreo ambiental y planeamiento urbanístico.

| *Ejemplo:*  Sistemas de compra inteligentes, por ejemplo, podrían seguir los hábitos de compra de un usuario específico rastreando su teléfono móvil. A estos usuarios se les podrían ofrecer ofertas especiales con sus productos preferidos o incluso guiarlos hacia la ubicación de los artículos que necesitan comprar. |
| --- |

###

### Aplicaciones de consumo

Una parte cada vez mayor de los dispositivos IoT se crea para uso del consumidor, incluidos vehículos conectados, domótica, tecnología vestible, salud conectada y electrodomésticos con capacidad de monitorización remota.

#### Domótica

Los dispositivos IoT forman parte del concepto más amplio de domótica, que puede incluir iluminación, calefacción y aire acondicionado, sistemas multimedia, sistemas de seguridad y sistemas de cámaras.

Los beneficios a largo plazo podrían incluir el ahorro de energía al asegurarse automáticamente de que las luces y los aparatos electrónicos están apagados o al concienciar a los residentes de la casa sobre su uso.

Una casa inteligente o automatizada podría basarse en una plataforma o concentradores que controlen dispositivos y electrodomésticos inteligentes.

| *Ejemplo:*  Hoy por hoy por ejemplo, mediante HomeKit de Apple, los fabricantes pueden hacer que sus productos y accesorios para el hogar estén controlados por una aplicación en dispositivos iOS como el iPhone y el Apple Watch. Podría tratarse de una app dedicada o de aplicaciones nativas de iOS como Siri. Esto se puede demostrar en el caso de Smart Home Essentials de Lenovo, que es una línea de dispositivos domésticos inteligentes que se controlan a través de la aplicación Home de Apple o Siri sin necesidad de un puente Wi-Fi.  También hay concentradores domésticos inteligentes dedicados que se ofrecen como plataformas independientes para conectar diferentes productos domésticos inteligentes. Entre ellos se encuentran Amazon Echo, Google Home, HomePod de Apple y SmartThings Hub de Samsung. Además de los sistemas comerciales, existen muchos ecosistemas de código abierto no propietarios, como Home Assistant, OpenHAB y Domoticz. |
| --- |

####

#### Cuidado de adultos mayores

Siguiendo un poco el concepto de domótica, una de las principales aplicaciones de las casas inteligentes es ayudar a ancianos y discapacitados. Estos sistemas domésticos utilizan tecnología de asistencia para adaptarse a las discapacidades específicas del propietario.

El control por voz puede ayudar a los usuarios con limitaciones de visión y movilidad, mientras que los sistemas de alerta pueden conectarse directamente a los implantes cocleares que llevan los usuarios con deficiencias auditivas.

También pueden equiparse con funciones de seguridad adicionales, como sensores que controlan emergencias médicas como caídas o convulsiones. La tecnología doméstica inteligente aplicada de esta forma puede proporcionar a los usuarios más libertad y una mayor calidad de vida.

### Aplicaciones comerciales

Esta categoría se refiere a los dispositivos utilizados en entornos empresariales y corporativos.

#### Medicina

El Internet de las Cosas Médicas (IoMT) es una de las aplicaciones de la IoT, en este caso, para fines médicos y relacionados con la salud, la recopilación y el análisis de datos para la investigación y la monitorización.

La IoMT se ha denominado "Cuidado de vida inteligente", como la tecnología para crear un sistema sanitario digitalizado, conectando los recursos médicos disponibles y los servicios sanitarios.

Los dispositivos IoT pueden utilizarse para habilitar sistemas remotos de control sanitario y notificación de emergencias (de manera similar a lo que plantean las [aplicaciones IoT de cuidado de adultos mayores](#_dky8kh8dt0x1)). Estos dispositivos de control de la salud pueden ir desde tensiómetros y pulsómetros hasta dispositivos avanzados capaces de controlar implantes especializados, como marcapasos, pulseras electrónicas o audífonos avanzados.

Algunos hospitales han empezado a implantar "camas inteligentes" que pueden detectar cuándo están ocupadas y cuándo un paciente intenta levantarse. También puede ajustarse para garantizar que se aplica al paciente la presión y el apoyo adecuados sin la interacción manual de las enfermeras.

Un informe de 2015 indicaba que los dispositivos IoT sanitarios "pueden ahorrar a Estados Unidos más de 300.000 millones de dólares en gastos sanitarios anuales al aumentar los ingresos y disminuir los costes.".

Además, el uso de dispositivos móviles para apoyar el seguimiento médico llevó a la creación de la "m-salud", que se utiliza para analizar las estadísticas sanitarias.

Es posible instalar sensores especializados en las viviendas para vigilar la salud y el bienestar general de las que hayan recibido el alta del hospital recientemente, al tiempo que se garantiza la administración del tratamiento adecuado y se ayuda a las personas a seguir un tratamiento adecuado en caso de intervención quirúrgica o a recuperar la movilidad perdida mediante terapia. Estos sensores crean una red de sensores inteligentes capaces de recopilar, procesar, transferir y analizar información valiosa en diferentes entornos, como la conexión de dispositivos de monitorización en el hogar a sistemas basados en hospitales.

Otros dispositivos médicos para fomentar una vida sana, como básculas conectadas o monitores cardíacos portátiles, también son una posibilidad con el IoT.

Asimismo existen plataformas IoT de monitorización sanitaria de extremo a extremo para pacientes prenatales y crónicos, que ayudan a gestionar las constantes vitales de salud y las necesidades recurrentes de medicación.

#### Transporte

El IoT puede contribuir a la integración de las comunicaciones, el control y el procesamiento de la información en diversos sistemas de transporte. La aplicación de el IoT se extiende a todos los aspectos de los sistemas de transporte (es decir, los vehículo, el control de la infraestructura y el conductor o usuario). La interacción dinámica entre estos componentes de un sistema de transporte permite la comunicación inter e intravehicular, el control inteligente del tráfico, el aparcamiento inteligente, los sistemas de telepeaje, la logística y la gestión de flotas, el control de vehículos, la seguridad y la asistencia en carretera.

#### Industrial

También conocidos como **IIoT**, los dispositivos **IoT** industriales adquieren y analizan datos de equipos conectados, tecnología operativa (OT), ubicaciones y personas. Combinado con dispositivos de supervisión de tecnología operativa (OT), IIoT ayuda a regular y supervisar los sistemas industriales. Además, la misma implementación puede llevarse a cabo para actualizaciones de registros automatizadas de colocación de activos en unidades de almacenamiento industrial, ya que el tamaño de los activos puede variar desde un pequeño tornillo hasta la pieza de repuesto de un motor completo, y la colocación incorrecta de dichos activos puede causar una pérdida de tiempo y dinero en mano de obra.

Se consideran tres subcampos de IoT Industrial: Agricultura, Manufactura y Marítima.

* **Agricultura**: Existen numerosas aplicaciones de IoT en la agricultura, como la recopilación de datos sobre temperatura, precipitaciones, humedad, velocidad del viento, infestación de plagas y contenido del suelo. Estos datos pueden utilizarse para automatizar las técnicas agrícolas, tomar decisiones informadas para mejorar la calidad y la cantidad, minimizar los riesgos y los residuos, y reducir el esfuerzo necesario para gestionar los cultivos. Por ejemplo, ahora los agricultores pueden controlar la temperatura y la humedad del suelo desde lejos e incluso aplicar los datos adquiridos mediante IoT a programas de fertilización de precisión. El objetivo general es que los datos de los sensores, unidos a los conocimientos y la intuición del agricultor sobre su explotación, puedan ayudar a aumentar la productividad agrícola y también a reducir costes.
* **Manufactura**: El IoT puede conectar varios dispositivos de fabricación equipados con capacidades de detección, identificación, procesamiento, comunicación, actuación y conexión en red. El control y la gestión en red de los equipos de fabricación, la gestión de activos y situaciones o el control de los procesos de fabricación permiten utilizar el IoT para aplicaciones industriales y fabricación inteligente. Los sistemas inteligentes del IoT permiten fabricar y optimizar rápidamente nuevos productos y responder con rapidez a las demandas de productos.

Los sistemas de control digital para automatizar los controles de procesos, las herramientas del operador y los sistemas de información de servicio para optimizar la seguridad de la planta están dentro del ámbito de la IIoT. IoT también puede aplicarse a la gestión de activos a través del mantenimiento predictivo, la evaluación estadística y las mediciones para maximizar la fiabilidad. Los sistemas de gestión industrial pueden integrarse con redes inteligentes, lo que permite la optimización de la energía. Las mediciones, los controles automatizados, la optimización de plantas, la gestión de la salud y la seguridad, y otras funciones son proporcionadas por sensores conectados en red.

Además de la fabricación en general, IoT también se utiliza para procesos en la industrialización de la construcción.

* **Marítima**: Muchos barcos de recreo permanecen desatendidos durante días en verano y meses en invierno, por lo que estos dispositivos proporcionan valiosas alertas tempranas de inundaciones, incendios y descargas profundas de las baterías. El uso de redes globales de datos por Internet, como Sigfox, combinado con baterías de larga duración y microelectrónica, permite supervisar constantemente las salas de máquinas, la sentina y las baterías y enviar informes a aplicaciones Android y Apple conectadas, por ejemplo.

#### Infraestructura

Hay varios despliegues previstos o en curso a gran escala del IoT, para permitir una mejor gestión de las ciudades y los sistemas.

| *Ejemplo:*  Songdo (Corea del Sur), la primera ciudad inteligente de su clase totalmente equipada y cableada, se está construyendo gradualmente, con aproximadamente el 70 % del distrito comercial terminado en junio de 2018. Está previsto que gran parte de la ciudad esté cableada y automatizada, con escasa o nula intervención humana. |
| --- |

En 2014, se llevó a cabo un proyecto en una ciudad para implementar una aplicación en smartphones conectada a miles de sensores, que permite servicios como la búsqueda de estacionamiento y el monitoreo ambiental. Este despliegue utiliza información contextual de la ciudad para beneficiar a los comerciantes mediante un mecanismo que maximiza el impacto de cada notificación.

Otras ciudades también están trabajando en implementaciones a gran escala, enfocándose en mejorar la calidad del aire y el agua, reducir la contaminación acústica y aumentar la eficiencia del transporte. En varias áreas, se han desarrollado redes públicas nacionales para transmisiones de datos de bajo ancho de banda, utilizando espectros no licenciados, similares al Wi-Fi. También se están construyendo redes inalámbricas de datos que cubren un gran número de ciudades, lo que convierte a algunos proveedores en líderes en cobertura de IoT en sus regiones.

Empresas tecnológicas participan en proyectos de ciudades inteligentes, desplegando tecnologías para Wi-Fi inteligente, seguridad y protección, iluminación inteligente, estacionamiento inteligente, transporte inteligente, paradas de autobús inteligentes, quioscos inteligentes, servicios gubernamentales remotos y educación inteligente en diversas áreas urbanas.

Otro ejemplo de una gran implementación es el despliegue de una red inalámbrica que conecta y monitorea en tiempo real los vehículos de una ciudad, permitiendo un control más efectivo de la flota y los pasajeros, además de habilitar aplicaciones como gestión de seguridad, energía, flota, señalización digital, Wi-Fi público, venta de boletos sin papel, entre otros.

Otra perspectiva sobre esto habla sobre que un número significativo de dispositivos que consumen energía (por ejemplo, lámparas, electrodomésticos, motores, bombas, etc.) ya integran conectividad a Internet, lo que les permite comunicarse con las empresas de servicios públicos no sólo para equilibrar la generación de energía, sino también para ayudar a optimizar el consumo de energía en su conjunto. Estos dispositivos permiten el control remoto por parte de los usuarios, o la gestión centralizada a través de una interfaz basada en la nube, y permiten funciones como la programación (por ejemplo, La red inteligente es una aplicación de IoT del lado de la empresa eléctrica; los sistemas recopilan información relacionada con la energía y la potencia y actúan sobre ella para mejorar la eficiencia de la producción y distribución de electricidad Mediante el uso de dispositivos conectados a Internet de infraestructura de medición avanzada (AMI), las empresas eléctricas no solo recopilan datos de los usuarios finales, sino que también gestionan dispositivos de automatización de la distribución como los transformadores. Por ejemplo, en Ámsterdam, la plaza Hoekenrodeplein dispone de un sistema de iluminación inteligente que se controla de manera remota y ajusta automáticamente su brillo según las condiciones ambientales.

### Tecnología RFID

El RFID, “Radio Frequency Identification” (Identificación por radio frecuencia), es una tecnología de captura de datos, muy parecido al sistema de código de barras, pero en lugar de código impreso utiliza un microchip y un circuito impreso a modo de antena dentro del cual se almacena el código alfanumérico, capaz de sustituir el actual sistema de leer las etiquetas de código de barras ante un lector.

La etiqueta se adhiere al equipo o producto que se desea inventariar, y pueden ser utilizadas para rastrearlos a distancia, facilitando así el control y la mecanización de la logística necesaria para la monitorización del producto.

Un sistema RFID está constituido por:

* Uno o más Tags (transponder) que incluye un chip semiconductor y una antena.
* Uno o más dispositivos de lectura/escritura incluye una antena.
* Un software de Aplicación y una computadora (Host).

Para transferir datos entre el tag RFID y el dispositivo de lectura/escritura se utilizan ondas de radio frecuencia. Ambos deben de estar sintonizados a la misma frecuencia. El lector envía una señal, que es recibida por todos los tags sintonizados a esa frecuencia presentes en el campo de RF. Los tags reciben la señal, y los seleccionados responden enviando los datos almacenados. Los tags pueden contener distintos tipos de datos acerca de un ítem, por ejemplo número de serie, datos de configuración, momento en que el ítem viajó por una cierta zona, temperatura y otros datos provistos por sensores.

El dispositivo de lectura/escritura recibe a través de su antena la señal del tag, la decodifica y transfiere los datos a un host. Si en el campo están presentes múltiples tags, las implementaciones más eficientes utilizan algoritmos de anticolisión que determinan el orden de respuesta tal que cada tag sea leído por vez y sólo una vez.

Las variables críticas en un sistema RFID, involucran el rango de frecuencia de la comunicación, el tamaño de la información contenida en el tag, la velocidad a la cual la comunicación con el tag puede tener lugar, la forma física del tag, la habilidad del sistema de comunicarse “simultáneamente” con múltiples tags, y la robustez de la comunicación respecto a la interferencia debida al material en el camino entre el lector y el tag.

En el marco del Internet de las Cosas, las etiquetas RFID pueden integrarse en objetos cotidianos para que puedan ser rastreados y gestionados automáticamente por sistemas IoT. Por ejemplo, en un almacén, las etiquetas RFID en los productos pueden comunicarse con una red IoT para automatizar el inventario en tiempo real.

También, los dispositivos IoT pueden usar RFID para recolectar datos de manera eficiente. Por ejemplo, en un entorno de producción, las etiquetas RFID pueden proporcionar datos sobre el estado y la ubicación de las piezas en el proceso de fabricación, que luego se pueden transmitir a través de la red IoT para su análisis y optimización.

En sectores como la logística, la salud, el comercio minorista y la fabricación, la combinación de RFID con IoT permite soluciones avanzadas como el monitoreo en tiempo real, la automatización de inventarios, la trazabilidad de productos y la gestión de activos.

#### Militares

La Internet de las Cosas Militar (IoMT) es la aplicación de tecnologías IoT en el ámbito militar con fines de reconocimiento, vigilancia y otros objetivos relacionados con el combate. Está fuertemente influenciada por las perspectivas futuras de la guerra en un entorno urbano e implica el uso de sensores, municiones, vehículos, robots, biometría humana y otras tecnologías inteligentes que son relevantes en el campo de batalla.

| *Ejemplo:*  Uno de los ejemplos de dispositivos de IoT utilizados en el ejército es el sistema Xaver 1000. El Xaver 1000 fue desarrollado por la israelí Camero Tech, y es el último de la línea de «sistemas de imágenes a través de la pared» de la empresa. La línea Xaver utiliza un radar de onda milimétrica (MMW), o radar en el rango de 30-300 gigahercios. Está equipada con un sistema de seguimiento de objetivos vivo basado en inteligencia artificial, así como con su propia tecnología 3D de «detección a través de la pared». |
| --- |

## Arquitectura IoT

Los elementos que constituyen el IoT se suele llamar "Arquitectura IoT", la cual se puede dividir en siete, cuatro o tres capas. Para citar el más simple, vamos a ver el modelo simplificado de tres capas:

* **Capa de Percepción o detección de objetos** (Sensores y Actuadores). Incluye sensores para detectar y recopilar información sobre el entorno, como temperatura, humedad, humo, seres vivos (cosas) e incluso otros objetos inteligentes. Los actuadores, por otro lado, realizan correcciones en tiempo real, como ajustar el nivel del aire acondicionado.
* **Capa de Red**: Es la responsable de recoger los datos suministrados por los sensores y convertirlos en un formato digital, permitiendo el procesamiento e intercambio de datos a través de una pasarela de Internet bien sea por una WAN 1 inalámbrica (Wi-Fi o celular) o una WAN cableada.
* **Capa de Aplicación**: Servicios de IoT para hogares inteligentes, ciudades inteligentes o fábricas inteligentes.

![](data:image/png;base64...)

La capa de aplicación garantiza la autenticidad, integridad y confidencialidad de los datos. En esta capa se logra el propósito de IoT que es la creación de entornos inteligentes.

## Tecnologías de redes de corto alcance y bajo consumo

Para implementar escenarios de Internet de las Cosas, es crucial considerar la tecnología de comunicación de los dispositivos IoT que se utilizarán. Nombraremos a continuación las tecnologías de comunicación más populares en la implementación de IoT

### Zigbee

Zigbee es una solución inalámbrica de bajo consumo de energía para escenarios IoT locales, gestionada por la Connectivity Standards Alliance. Utiliza una topología de malla que requiere un Hub o controlador para interactuar con Internet. La comunicación entre nodos puede realizar múltiples saltos hasta llegar al Hub, con un alcance promedio de hasta 300 metros en línea de vista y entre 75 y 100 metros en interiores. Zigbee soporta teóricamente hasta 65,000 nodos y ofrece velocidades de transferencia de 40 a 250 kbps en la banda de 2.4 GHz. La versión 3.0 garantiza la interoperabilidad entre productos de diferentes fabricantes. Zigbee gestiona automáticamente la red, reconfigurando dinámicamente las rutas según la entrada o salida de nodos. Los nodos en una red Zigbee pueden desempeñar roles como coordinador, router o dispositivo final, con la capacidad de entrar en modo de ahorro energético. Se usa en dispositivos como enchufes, sensores, alarmas y medidores de consumo de energía.

### Bluetooth Low Energy (BLE)

Bluetooth Low Energy (BLE) es una variante del Bluetooth diseñada para funcionar con muy bajo consumo de energía, manteniendo muchas características del Bluetooth clásico. Opera en la frecuencia de 2.4 GHz y su alcance típico es de unos 10 metros, aunque con la configuración adecuada puede superar 1 km, dependiendo de factores como el rango de frecuencias, la capa física, la sensibilidad del receptor, la potencia de transmisión, la ganancia de la antena y la pérdida de señal. La velocidad de transferencia de datos puede alcanzar hasta 1.4 Mbps usando la capa física LE 2M. BLE permite topologías punto a punto, broadcast y, desde 2017, también en malla. Además, BLE permite determinar la proximidad de un dispositivo y, próximamente, medir la distancia. Su enfoque principal es en aplicaciones que no requieren el intercambio de grandes cantidades de datos. Su bajo consumo de energía, con dispositivos que pueden operar durante meses o años sin cambiar la batería, y su bajo costo, lo hacen adecuado para IoT. Ejemplos de uso incluyen rastreadores de personas o mascotas, y desfibriladores automáticos.

### Near Field Communication (NFC)

La Near Field Communication (NFC) opera a 13.56 MHz y ofrece una velocidad de transferencia de hasta 424 kbit/s. Diseñada para funcionar en distancias muy cortas, generalmente unos pocos centímetros, NFC proporciona una seguridad adicional al dificultar la interceptación de la comunicación. No requiere emparejamiento previo como el Bluetooth y es de bajo consumo energético. Los dispositivos NFC generan un campo de radiofrecuencia (RF) para transferir energía a las etiquetas NFC, que son pasivas y no necesitan baterías. NFC puede ser utilizada de diversas maneras: escritura/lectura, intercambio de datos entre dispositivos (Peer to Peer), emulación de tarjetas para pagos, carga inalámbrica de dispositivos pequeños, y emulación de tarjetas mediante elementos seguros. NFC es útil para agregar inteligencia a objetos sin alimentación, facilitando aplicaciones como identificación, intercambio de datos, sincronización de dispositivos, automatización de acciones y pagos móviles.

### Wi-Fi/802.11

La tecnología Wi-Fi usada se basa en el estándar de comunicación inalámbrica 802.11 desarrollado por IEEE 802.11 WLAN, con mejoras continuas en velocidad y reducción de latencia. La Wi-Fi Alliance colabora para garantizar la interoperabilidad, seguridad y fiabilidad de Wi-Fi. Wi-Fi 6, la última versión, es retrocompatible con versiones anteriores y puede operar en frecuencias de 2.4 GHz, 5 GHz y la nueva banda de 6 GHz (Wi-Fi 6E). La frecuencia de 2.4 GHz ofrece mayor alcance pero menor velocidad, mientras que 5 GHz proporciona mayor velocidad pero menor alcance. Wi-Fi 6 incluye la tecnología Target Wake Time (TWT), que permite a los dispositivos entrar en modo de ahorro energético y activar la conexión solo cuando es necesario para recibir nuevos datos.

### Z-Wave

Z-Wave es un estándar propietario de Silicon Labs, ampliamente utilizado en productos para casas inteligentes. Al igual que Zigbee, utiliza una topología de red en malla. Cada dispositivo en la red actúa como repetidor de señal, mejorando la fuerza de la red a medida que se añaden más dispositivos. La señal de Z-Wave tiene un alcance de 100 metros en exteriores, y se recomienda colocar un dispositivo cada 9 metros. Cada red puede admitir hasta 232 dispositivos, con velocidades de 40 a 100 kbps. Z-Wave opera en frecuencias inferiores a 1 GHz, evitando interferencias con Wi-Fi. Sin embargo, la red admite hasta cuatro saltos de dispositivo para alcanzar el coordinador y puede tener un costo elevado, lo que lo convierte en una tecnología de gama alta.

## Sistemas embebidos

En los hogares modernos hay una gran cantidad de dispositivos que se usan a diario para controlar diferentes espacios y entornos, realizar procesos automáticos con diferentes elementos eléctricos o electrónicos mediante comandos de voz, teléfonos celulares o incluso relojes. Estos se denominan "Sistemas Embebidos".

Como vimos en el apartado de aplicaciones de IoT, los sistemas domóticos son una categoría de automatización que incluye hardware (como varios sensores, controladores y dispositivos domésticos) y software encargado de gestionar las tareas relacionadas con el hogar o el entorno, como programar la hora de las luces, controlar las luces o irrigar el jardín si la humedad no es adecuada.

### Historia de los sistemas embebidos

La implementación de sistemas embebidos en los hogares comenzó en 1934 en Chicago, Estados Unidos, y en 1938 en New York, durante las ferias mundiales que se llevaron a cabo en dichas ciudades. Además de estas ferias, a lo largo de la historia se han producido varios inventos relacionados, como la televisión, internet y las computadoras.

Durante el período comprendido entre 1901 y 1920, se introdujeron en los hogares los dispositivos eléctricos con el objetivo de reemplazar las tareas domésticas con herramientas relativamente costosas en aquel entonces. Entre los primeros dispositivos que se instalaron en los hogares se incluyeron la aspiradora, la plancha, la tostadora y la bombilla.

Posteriormente, en 1928, se lanzó la televisión en Inglaterra y Estados Unidos.

El desarrollo de todos estos dispositivos procuraban que fueran de uso sencillo, que cualquiera los pudiera integrar en diferentes proyectos y además que fueran de bajo costo, así surgieron lo que actualmente se conoce como Sistemas Embebidos.

### Definición de un sistema embebido

Los Sistemas Embebidos están diseñados para funciones particulares y son una integración entre software y hardware, usualmente están contenidos en aparatos domésticos, autos, incluso en teléfonos móviles; generalmente están compuestos por microcontroladores o en algunos casos pueden contener también microprocesadores.

Aunque el término "Sistemas Embebidos" suena bastante extraño, se trata de dispositivos que se encuentran en interacciones diarias, como un dispositivo que calcula el cobro en un taxi, un lector de carnet de estudiante en la universidad o incluso un teléfono móvil. Son cruciales para proyectos específicos y pequeños, así como para el desarrollo de tareas puntuales.

Algunas características de los sistemas embebidos son:

* Cuentan con sensores y actuadores
* No son equivalentes a sistemas de cómputo como las notebooks o equipos de escritorio
* Tienen recursos limitados y aplicaciones específicas que los hacen muy útiles
* Tamaños regularmente pequeños
* Bajo costo
* Consumos de energía bajos
* No requieren conocimientos avanzados para su manipulación

### Componentes de los sistemas embebidos

Son varios los tipos de componentes que podemos encontrar en un sistema embebido:

* **Microcontrolador**: Es el cerebro del sistema embebido y se encarga de procesar la información y controlar el funcionamiento del sistema. Está compuesto por una unidad central de procesamiento (CPU), memoria RAM, memoria ROM y periféricos.
* **Dispositivos de Entrada/Salida (E/S)**: Permiten la interacción con el mundo exterior. Algunos ejemplos son puertos USB, puertos seriales, interfaces de red, etc.
* **Sensores**: Detectan y recopilan información del entorno. Algunos ejemplos son sensores de temperatura, de luz, de movimiento, etc., pueden ser sensores analógicos o digitales.
* **Actuadores**: Controlan y modifican el entorno en base a la información de los sensores. Algunos ejemplos son motores, LEDs, válvulas, etc.
* **Placas de Circuito Impreso**: Es el componente que conecta eléctricamente y soporta físicamente todos los otros componentes mediante el uso de pistas, pads, y otras características grabadas en láminas de cobre laminadas sobre y/o entre capas de sustrato no conductor.

Los componentes tipo software, pueden ser:

* **Sistema operativo**: Controla la ejecución del software y administra los recursos del sistema.
* **Software de aplicación**: Implementa la funcionalidad específica del sistema embebido.

El diseño o arquitectura de un sistema embebido puede ser similar a una tarjeta electrónica con múltiples sensores y dispositivos conectados, o más complejo como una mini-computadora. Ambos tipos de sistemas realizan tareas específicas mediante el uso de varios lenguajes de programación o sistemas operativos. El Arduino y el Raspberry Pi son dos placas y dispositivos embebidos muy populares entre los estudiantes y desarrolladores.

### Arduino y su impacto en el IoT

Arduino es una plataforma de desarrollo basada en una placa electrónica de hardware libre que incorpora un microcontrolador re-programable y una serie de pines hembra. Estos permiten establecer conexiones entre el microcontrolador y los diferentes sensores y actuadores de una manera muy sencilla.

Una placa electrónica es una PCB (Printed Circuit Board o, en español, "Placa de Circuito Impreso"). Las PCBs son superficies planas fabricadas en un material no conductor, la cual consta de distintas capas de material conductor. Una PCB es la forma más compacta y estable de construir un circuito electrónico. Por lo tanto, la placa Arduino no es más que una PCB que implementa un determinado diseño de circuitería interna. De esta forma el usuario final no se debe preocupar por las conexiones eléctricas que necesita el microcontrolador para funcionar, y puede empezar directamente a desarrollar las diferentes aplicaciones electrónicas que necesite.

El uso de **placas Arduino** ha sido clave en el desarrollo de proyectos basados en el **Internet de las Cosas**. Existen una gran cantidad de modelos de Arduino, cada uno diseñado con diferentes características y propósitos, como el tamaño físico, el número de pines de entrada/salida y el modelo del microcontrolador. Estas placas permiten la creación de dispositivos IoT que pueden recopilar datos, procesarlos y comunicarse con otros sistemas, utilizando sensores y actuadores conectados a la red.

A pesar de la variedad de modelos de placas Arduino, todas pertenecen a la misma familia de microcontroladores (AVR marca Atmel), lo que implica que comparten características comunes en cuanto a software, como su arquitectura, librerías y documentación. Esto facilita el desarrollo de aplicaciones IoT, ya que los desarrolladores pueden aprovechar la amplia comunidad de soporte y la consistencia en la programación de las placas. Esta flexibilidad y facilidad de uso convierte a Arduino en una plataforma ideal para prototipos y proyectos IoT, desde pequeños experimentos caseros hasta soluciones más complejas de automatización y monitoreo.

En el contexto del IoT, las placas Arduino se pueden conectar a redes y plataformas en la nube para gestionar los datos generados por sensores, permitiendo el control remoto y la automatización en tiempo real. Esto hace que Arduino sea una herramienta valiosa para la creación de dispositivos IoT interconectados de bajo costo y fácilmente personalizables.

![](data:image/png;base64...)

### Raspberry Pi y su impacto en el mundo IoT

La Raspberry Pi Foundation se creó en 2009, en el mes de mayo. Con sede en Cambridge, Reino Unido, su propósito es promover el estudio de la informática o ciencias computacionales en las escuelas. Y para hacer esto posible, desarrolla sus ordenadores Raspberry Pi. Precisamente, su clave de éxito son estos pequeños dispositivos.

Una de las cosas interesantes, prácticas y quizás divertidas de la Raspberry es su funcionalidad en cuanto al software se refiere, pues en pocos segundos puede transformarla en una divertida consola de juegos, una laptop para trabajos del colegio, una plataforma de programación que se puede integrar incluso con arduino, u otra gran cantidad de proyectos interesantes.

Un ejemplo de uso de la Raspberry Pi, es un proyecto de mini computador con Raspberry Pi con elementos impresos en 3D. La Raspberry Pi usa principalmente sistemas operativos GNU/Linux. Raspbian, una distribución derivada de Debian que está optimizada para el hardware de Raspberry Pi, se lanzó durante julio de 2012 y es la distribución recomendada por la fundación para iniciarse. Aunque uno de los recomendados para estudiantes es la versión Pi-Top OS, muy útil para iniciar en proyectos con Arduino o robótica.

## Computación en la nube (o Cloud Computing)

La nube (cloud en inglés) es la forma abreviada de "computación en la nube" (cloud computing), son todas las cosas a las que puedes acceder de forma remota a través de Internet. Cuando algo está en la nube, significa que está almacenado en servidores de Internet en lugar del disco duro de tu computadora.

### ¿Qué es la computación en la nube?

La computación en la nube define un modelo para permitir el acceso de red ubicuo, conveniente y bajo demanda a un grupo compartido de recursos informáticos configurables (por ejemplo, redes, servidores, almacenamiento, aplicaciones y servicios) que se pueden aprovisionar y liberar rápidamente con un mínimo esfuerzo de administración o interacción con el proveedor de servicios.

### ¿Qué relación guarda el Cloud Computing con el IoT?

La computación en la nube y el Internet de las cosas están estrechamente relacionados porque permiten y apoyan el desarrollo de entornos digitales conectados. El Internet de las cosas produce grandes cantidades de datos a través de sus numerosos dispositivos y sensores distribuidos, lo que requiere un sistema sólido y escalable para almacenar, procesar y administrar esos datos de manera efectiva. La computación en la nube aporta una infraestructura adaptable y escalable para el procesamiento masivo de datos en este punto. La nube brinda el espacio y los recursos necesarios para manejar este gran volumen de datos, lo que permite que los datos recolectados por los dispositivos de Internet de las cosas sean accesibles de forma ubicua y bajo demanda.

### Modelos de computación en la nube

Existen diferentes tipos de servicios, esto ocurre porque "*la computación en la nube basa su arquitectura haciendo una separación entre hardware, plataforma y aplicaciones*” quedando las siguientes capas:

* **Software como Servicio**. Simplificada como SaaS (Software as a Service). Está en la capa más alta, consiste en la entrega de aplicaciones completas (software) como un servicio, con una distribución del tipo "uno a muchos", por ejemplo el servicio de correo electrónico o el Office 365 de Microsoft.
* **Plataforma como Servicio**. Simplificada como PaaS (Platform as a Service). Es un servicio de plataforma con todo lo necesario para dar soporte al desarrollo y puesta en marcha de aplicaciones y servicios web; es decir, es útil para desarrolladores para gestionar, distribuir y testear sus aplicaciones de software.
* **Infraestructura como Servicio**. Simplificada como IaaS (Infrastructure as a Service). Es la capa más baja. "*La idea básica es la de hacer uso externo de servidores para espacio en disco, base de datos, ruteadores, switches así como tiempo de cómputo evitando un servidor local y toda su infraestructura*" (Ibid), es útil para desplegar aplicaciones web, operar un CRM, realizar análisis de Big Data, backups, etc.

### Tipos de Nube

Según el modelo de implementación, se tienen los siguientes tipos de Nube:

* **Nube pública**: Es la que puede usarse por varios clientes que deben reunirse en servidores que son propiedad y administrados por los proveedores. Los usuarios acceden al servicio actual bajo demanda e inmediato a través de Internet o redes privadas virtuales (VPN). Por ejemplo: Google App Engine y Microsoft Azure.
* **Nube privada**: Se basa en las necesidades de los clientes individuales, brindando propiedad sobre los datos, seguridad y dedicación al cliente. "Los recursos ofrecidos pasan a ser propiedad de una sola institución, manteniendo la infraestructura en una red privada de uso y ofreciendo incluso la posibilidad de alojar los servicios en las propias instalaciones del cliente", lo que resulta seguro y costoso en comparación con una nube pública. Un ejemplo puede ser Eucalyptus System
* **Nube híbrida**: es el resultado de la unión de los modelos anteriores. Tanto las nubes públicas como las privadas son entidades separadas, pero se conectan mediante principios de comunicación y transferencia de aplicaciones y datos. Una nube híbrida se puede ver en Amazon Web Services.
* **Nube Comunitaria**: Diseñada para una comunidad específica de consumidores de diferentes organizaciones. Puede ser de propiedad, administrado y operado por una o más empresas de la comunidad. Útil en el sector educativo. Facebook es un ejemplo de una nube comunitaria.

### Ventajas y desventajas del Cloud Computing

La idea del Cloud Computing es muy innovadora y trae por un lado muchas ventajas:

* Capacidad de procesar y almacenar grandes volúmenes de información (Big Data).
* Alta disponibilidad, escalabilidad, flexibilidad, eficiencia.
* El ahorro, tanto en licencias como en la administración del servicio y en los equipos.
* Implementación rápida y baja en riesgos.
* Actualizaciones automáticas (Ibid.).
* Ahorro energético.
* Copias de seguridad.
* Trabajo colaborativo. Ofrece la posibilidad de hacer un trabajo conjunto de empleados, estudiantes, investigadores, etc. que se encuentran en puntos geográficos distantes.

Ahora, si bien no posee desventajas fuertes, tiene desventajas que surgen por la necesidad de mantener una conexión para acceder a sus recursos, podemos listar:

* Fallos en la prestación del servicio: Esto puedo ocurrir por fallas en los servidores.
* Amenaza de seguridad. "Tratamiento de la información fuera de los límites manejados por el usuario". Situación que aún genera desconfianza en algunos usuarios, en especial por la pérdida de privacidad, pese a las nuevas tecnologías de ciberseguridad.

## Métricas y analíticas en el IoT

A diario se realiza el proceso de medir el entorno, al desplazarse de un lugar a otro se tiene en cuenta los metros o kilómetros recorridos, se mide el tiempo de desplazamiento o, en la realización de una actividad, la capacidad de cargar un objeto el cual es medido en kilos, incluso cuando se va al gimnasio, se mide el esfuerzo realizado, todo esto es medido en diferentes unidades, dependiendo del escenario y características en que se realice.

¿Qué es Medición? La palabra medición deriva del verbo medir que a su vez viene de la palabra latina metriri, que significa "comparar un resultado o cantidad con una unidad de medida previa".

La medición sirve para determinar magnitudes de un objeto en relación a otro objeto que sirve de patrón, que es definido antes por un consenso. Hoy en día, estos modelos de comparación que se usan todos los días; por ejemplo, la masa, la temperatura y la longitud, están unificados en lo que se conoce como el Sistema Internacional de Unidades (SI).

En este sistema, se establecieron las unidades de medición que son usadas para relacionar individual, social y económicamente. En este sentido, la medición es importante porque facilita el intercambio de tiempos, espacios, objetos y teorías.

Una de las actividades esenciales del Internet de las Cosas, es realizar procesos apropiados de medición de los datos generados por los diferentes sensores que integran el ecosistema, pasando por la transferencia de estos mediante la red y su presentación en las herramientas apropiadas, dando cuenta de su interpretación con la mejor fidelidad y confiabilidad posible.

Muchas personas aún creen que al hablar de datos, métricas y analítica, particularmente en el entorno de IoT, solo se trata de entorno tecnológico o de estadísticas, pero los datos confiables y oportunos ofrecen la ventaja de tener comprensión del mundo cambiante en el que se vive. En la ciudad se acumula a diario una cantidad de datos, al acumularse suficientes de estos, es posible encontrar patrones de hábitos y comportamiento en la movilidad o el clima, pronósticos de sucesos en las vías o del transporte público, de averías, de fallas, etc, la correcta interpretación de estas permiten anticipar hechos que no se desean que sucedan y entrega mucha información aprovechable; para esto es necesario contar con herramientas de analítica

## Análisis de datos en el IoT

La capacidad de recopilar y analizar datos en tiempo real es una de las aplicaciones más significativas del IoT, lo que brinda un potencial sin precedentes para la toma de decisiones informadas y oportunas en una variedad de áreas. El análisis de datos es esencial en este contexto porque permite a las organizaciones tomar decisiones ágiles y efectivas en tiempo real de la avalancha de datos generada por los dispositivos IoT.

Los sensores integrados en dispositivos IoT recopilan una gran variedad de datos, desde mediciones ambientales y de rendimiento de máquinas hasta hábitos de los consumidores y patrones de tráfico. Estos datos son transmitidos a través de redes inalámbricas y almacenados en la nube, donde pueden ser procesados y analizados en tiempo real. Este flujo constante de información brinda a las organizaciones la capacidad de monitorear activos, identificar tendencias emergentes y tomar decisiones en función de datos concretos.

El análisis de datos en la IoT se ha convertido en un habilitador clave para la toma de decisiones informadas y en tiempo real. Los datos recopilados por los dispositivos IoT son inherentemente grandes y complejos, lo que requiere enfoques analíticos avanzados para extraer información significativa. Aquí es donde entran en juego técnicas como el aprendizaje automático y la inteligencia artificial. Estas técnicas permiten a las organizaciones descubrir patrones, tendencias y correlaciones en los datos que serían difíciles o imposibles de identificar mediante métodos tradicionales.

Por ejemplo, en el ámbito de la fabricación, los sensores en las máquinas pueden recopilar datos sobre su rendimiento, temperatura y otras variables relevantes. Mediante el análisis de estos datos en tiempo real, las organizaciones pueden detectar anomalías o signos de fallos inminentes, lo que permite tomar medidas correctivas antes de que ocurra una interrupción costosa. De manera similar, en la agricultura de precisión, los sensores en los campos pueden proporcionar información sobre la humedad del suelo, los niveles de nutrientes y las condiciones climáticas. El análisis de estos datos puede guiar la programación óptima de riego y fertilización, maximizando los rendimientos de los cultivos.

### Herramientas para el análisis de datos

Las métricas y la analítica en el IoT requieren un buen manejo de la información, y ante todo entender cuál es el propósito y el contexto de lo que está realizando y analizando:

* **La bodega de datos**. Es el espacio donde se almacenan los datos, estos deben guardarse de modo ordenado y lógico, deben estar dispuestos para un proceso de consulta para que sean ubicados ágilmente.
* **Los dashboards o tableros.** Los datos se representan de manera gráfica, visualizando los datos en la bodega. Es una forma de contar la historia de la información de manera más atractiva y asertiva.
* **Las alertas.** Se activan cuando se encuentran anomalías o si se programó en el proyecto IoT anuncios, esto sirve para clasificar los datos y detonarlas cuando se cumplen criterios específicos, ya sea de manera preventiva o informativa.
* **KPIs.** Son los indicadores de desempeño. Miden el rendimiento y/o avance de los procesos IoT, para ello es importante tener unos buenos datos, además permiten mejora continua y optimización de los procesos.

### Beneficios de la Toma de Decisiones en Tiempo Real

La capacidad de tomar decisiones en tiempo real basada en análisis de datos de Internet de las cosas ofrece una serie de beneficios significativos. Para empezar, permite a las organizaciones actuar de manera proactiva en lugar de reactiva. Las empresas pueden tomar medidas preventivas y reducir los riesgos antes de que se conviertan en problemas graves al detectar problemas y tendencias emergentes de manera temprana.

En segundo lugar, el proceso de toma de decisiones en tiempo real mejora la eficiencia de las operaciones. La optimización de rutas y la gestión de flotas en tiempo real basada en datos en vivo pueden reducir los costos y mejorar los tiempos de entrega en sectores como la logística y el transporte. Esto resulta en una mayor satisfacción del cliente y una ventaja competitiva.

En tercer lugar, la innovación es promovida por la toma de decisiones basada en análisis de datos en tiempo real. Las empresas pueden encontrar oportunidades para la mejora continua y la creación de nuevas soluciones al obtener información detallada sobre cómo se utilizan los productos o cómo funcionan los sistemas.

### Consideraciones Éticas

Considerar la ética es fundamental. La recopilación y el análisis de datos de Internet de las cosas plantean preguntas sobre quién puede ver los datos, cómo se utilizan y si los usuarios dan su consentimiento adecuado. La confianza de los usuarios y la prevención de problemas legales dependen de cómo se manejan los datos.

## ¿Por qué es importante el IoT?

Antes de que podamos comenzar a comprender la importancia del Internet de las cosas, debemos comprender las diferencias entre Internet y la World Wide Web (o Web), términos que con frecuencia se utilizan para referirse al mismo. Los enrutadores, los enrutadores y otros componentes componen la capa física o red de Internet. Su función principal es transferir datos de forma rápida, confiable y segura. Por el contrario, la Web es una capa de aplicaciones que se encuentra en la parte superior de la red. Su objetivo principal es crear una interfaz que haga que los datos que fluyen a través de Internet sean accesibles.

### La evolución de la web

La Web ha pasado por varias fases evolutivas diferentes:

* **1era Fase**: Primero fue la fase de investigación, durante este periodo, la Web era utilizada en su mayoría por las universidades para fines de investigación.
* **2da Fase**: La segunda fase de la red podría denominarse "*brochureware*". Esta etapa está caracterizada por la "fiebre del oro" de los nombres de dominio, y se enfoca en la necesidad de las empresas de compartir información a través de Internet para que la gente supiera más sobre los productos y servicios que proveían.
* **3era Fase**: En la tercera fase, la Web pasó de albergar datos estáticos a proporcionar información transaccional, gracias a la cual se podían comprar y vender productos y servicios, así como suministrar servicios.
* **4ta Fase**: En la cuarta fase, en la que nos encontramos ahora, predomina la Web "social" o de las "experiencias", ya que permiten a las personas comunicarse, conectarse y compartir información (texto, fotos y vídeos) sobre ellos mismos con amigos y familiares.

### IoT: La primera evolución del Internet

En comparación, Internet ha experimentado un continuo crecimiento y mejora, pero podría decirse que no ha experimentado un cambio significativo. Por ejemplo, en el principio existían varios protocolos de comunicación, incluidos AppleTalk, Token Ring e IP. En la actualidad, Internet se basa principalmente en el protocolo **IP**.

El Internet de las cosas es de gran importancia en este contexto porque es la primera evolución real de Internet; se trata de un salto que da lugar a aplicaciones revolucionarias que tienen el potencial de mejorar significativamente la vida, el aprendizaje, el trabajo y el entretenimiento de las personas. El Internet de las cosas ha permitido que se le otorgué una dinámica sensorial al Internet, pudiendo detectar y realizar acciones en base a la temperatura, la presión, la vibración, la luz y la humedad, entre otros. Permitiendo al humano ser más proactivo y menos reactivo.

Junto a esto Internet está llegando a lugares que antes eran inaccesibles. Los pacientes usan dispositivos habilitados para Internet para ayudar a los médicos a diagnosticar y determinar las causas de ciertas enfermedades. Los sensores extremadamente pequeños se pueden incorporar en plantas, animales y accidentes geológicos y conectarlos a Internet.

## Retos y barreras para el IoT

### La implementación de IPv6

El mundo agotó las direcciones IPv4 en febrero de 2010, lo que impulsó la adopción del protocolo IPv6. Este nuevo protocolo (La sexta versión del Protocolo de Internet) fue diseñado para superar las limitaciones de IPv4, especialmente en cuanto a la cantidad de direcciones disponibles. IPv4 tenía un número limitado de direcciones IP, lo que representaba un obstáculo significativo para el crecimiento exponencial del Internet de las cosas. En contraste, IPv6 ofrece un espacio de direcciones mucho más amplio, permitiendo asignar direcciones únicas a un número prácticamente ilimitado de dispositivos. Esto facilita la expansión del IoT y asegura que cada dispositivo pueda tener una identificación única y accesible en la red.

Sin embargo, aunque IPv6 ha sido fundamental para el crecimiento del IoT, también presenta desventajas y desafíos. La transición de IPv4 a IPv6 no es inmediata y requiere una coexistencia de ambos protocolos durante un periodo prolongado. Esta coexistencia puede complicar la gestión de redes y la interoperabilidad con dispositivos que aún usan IPv4. Además, muchas infraestructuras y sistemas antiguos siguen dependiendo de IPv4, y su actualización para ser compatibles con IPv6 puede resultar costosa y compleja.

Además, a pesar del amplio espacio de direcciones que ofrece IPv6, no resuelve todos los problemas relacionados con la seguridad y la privacidad en el IoT. La implementación de IPv6 no garantiza automáticamente una mejor protección contra ciberataques o vulnerabilidades. De hecho, la transición a IPv6 puede introducir nuevas vulnerabilidades si no se maneja adecuadamente, ya que muchos dispositivos IoT todavía presentan deficiencias en cuanto a seguridad. Por lo tanto, aunque IPv6 aporta beneficios significativos, su implementación debe gestionarse cuidadosamente para evitar problemas adicionales en términos de seguridad y compatibilidad.

### Fuente de energía de los sensores.

Los sensores de un dispositivo IoT deben ser autosuficientes para que el Internet de las cosas pueda explotar todo su potencial ya que si el dispositivo necesita un cambio de baterías paulatinamente para sostener su funcionamiento, nos encontraríamos frente a una fuerte debilidad cuando trabajemos con un número alto de dispositivos. Por esta razón, es necesario un método para que los sensores generen electricidad de manera autónoma, ya sea a partir de las vibraciones, la luz solar o el flujo de aire del entorno. En este contexto se han producido numerosos avances e invenciones para mejorar la autosuficiencia energética de los sensores.

Por ejemplo, se han desarrollado generadores piezoeléctricos que convierten las vibraciones del entorno en electricidad, lo que permite que los sensores alimenten sus propios sistemas a partir del movimiento o las vibraciones. También se han perfeccionado celdas solares de bajo consumo, que aprovechan la luz solar para generar energía suficiente para el funcionamiento de sensores en entornos bien iluminados. Además, se han implementado microgeneradores eólicos, que capturan la energía del flujo de aire para proporcionar electricidad a sensores ubicados en áreas con corrientes de viento constantes. Estas innovaciones no sólo extienden la vida útil de los sensores, sino que también reducen la necesidad de mantenimiento y reemplazo de baterías, facilitando la expansión y el despliegue masivo de dispositivos IoT.

### Estándares.

La falta de estándares adecuados crea desafíos significativos para mejorar la interoperabilidad e integración entre sistemas que emplean tecnologías diversas. Es esencial seguir desarrollando estándares que sean accesibles tanto para el público en general como para los fabricantes.

Aunque se han realizado importantes avances en los estándares para el Internet de las cosas, todavía queda mucho por mejorar, especialmente en áreas clave como seguridad, privacidad, arquitectura y comunicaciones. En particular, el desarrollo de estándares robustos es fundamental para asegurar que los dispositivos IoT puedan interoperar de manera efectiva y segura en una amplia gama de redes.

El Institute of Electrical and Electronics Engineers[[2]](#footnote-1) (IEEE) está trabajando para abordar estos desafíos mediante la creación de estándares que faciliten la compatibilidad y la integración de dispositivos IoT en diversas infraestructuras. Un aspecto crucial de estos esfuerzos es asegurar que los paquetes IPv6, que son esenciales para la expansión del IoT, puedan ser transmitidos de manera eficiente y segura a través de diferentes tipos de redes. Esto incluye la optimización de protocolos para mejorar la comunicación entre dispositivos, así como la implementación de medidas de seguridad para proteger la privacidad y la integridad de los datos. La colaboración continua en la estandarización ayudará a garantizar que el IoT pueda desarrollarse de manera segura y efectiva, apoyando la creación de un ecosistema más cohesionado y confiable.

### Disponibilidad y Confiabilidad

Los sistemas IoT a menudo necesitan estar disponibles en cualquier momento y en cualquier lugar, ofreciendo un alto nivel de confiabilidad en los servicios que brindan. Esto incluye operar en entornos altamente heterogéneos y dinámicos. Por ello, es crucial abordar desafíos relacionados con la disponibilidad y cobertura de redes de comunicación, especialmente en redes móviles e inalámbricas, así como garantizar un acceso eficiente a servicios e infraestructura en la nube.

### Almacenamiento y Procesamiento de Datos

Con la creciente necesidad de utilizar servicios en la nube para almacenar y procesar los datos recopilados por los sistemas IoT, surgen varios retos. Estos incluyen no solo el almacenamiento de datos, sino también el procesamiento avanzado mediante tecnologías como Big Data e inteligencia artificial. Además, es importante desarrollar capacidades para la visualización y representación de datos que mejoren la autonomía de las aplicaciones IoT, reduciendo la necesidad de intervención humana.

### Seguridad y Privacidad

La seguridad y la privacidad son cruciales para cualquier sistema digital, y el IoT no es una excepción, especialmente dada la complejidad de su diseño y la interacción con múltiples tecnologías y sistemas. Es necesario implementar esquemas robustos de autenticación, encriptación y protección de la integridad de la información. Además, se deben considerar aspectos sociales, legales y culturales para asegurar que los sistemas IoT sean seguros y respeten la privacidad de los usuarios.

##

## El futuro de IoT

El futuro de IoT es prometedor, con muchas implementaciones para empresas en el horizonte. A continuación se listan varias predicciones y tendencias para el futuro de IoT:

* **Crecimiento:** Es esperable que el número de dispositivos IoT crezca rápidamente, con estimaciones que sugieren que habrán diez billones de dispositivos IoT en uso en los próximos años. Este crecimiento estará impulsado por una mayor adaptación de esta tecnología en todos los sectores, así como por el desarrollo de nuevos casos de uso y aplicaciones.
* **Edge Computing:** cada vez más importante para IoT, ya que permite que los datos se procesen y analicen más cerca de la fuente de los datos, en lugar de un centro de datos especializado. Esto puede mejorar los tiempos de respuesta, reducir la latencia y reducir la cantidad de datos que es necesario transferir a través de las redes IoT.
* **Inteligencia Artificial y Machine Learning**: La IA y el machine learning toman cada vez más protagonismo para el IoT ya que se pueden utilizar para grandes cantidades de datos generados por dispositivos IoT y extraer información significativa. Esto puede ayudar a las empresas a tomar decisiones más informadas y optimizar sus operaciones.
* **Blockchain**: La tecnología blockchain está siendo utilizada como una manera de mejorar la seguridad y privacidad en el IoT. El blockchain puede utilizarse para crear redes seguras y descentralizadas para dispositivos IoT, lo que puede minimizar las vulnerabilidades de seguridad en los datos.
* **Sostenibilidad**: se está convirtiendo en una consideración cada vez más importante para IoT, ya que las empresas buscan formas de reducir su impacto medioambiental. El IoT puede utilizarse para optimizar el uso de la energía, reducir los residuos y mejorar la sostenibilidad en una amplia gama de sectores.

En definitiva, el futuro del IoT es apasionante, con muchos nuevos desarrollos e innovaciones en el horizonte, y con proveedores de dispositivos que ofrecen precios sumamente atractivos, a medida que disminuye el coste de producción de los dispositivos IoT. A medida que aumenta el número de dichos dispositivos, las empresas deben estar preparadas para adaptarse a estas nuevas tecnologías, adoptando nuevos casos de uso y aplicaciones. Aquellas que sean capaces de hacerlo estarán a la vanguardia, en condiciones de cosechar los beneficios de esta tecnología transformadora

# Conclusiones

Como hemos visto a lo largo de este informe el Internet de las Cosas representa una transformación tecnológica que ha cambiado profundamente nuestra forma de relacionarnos con el entorno. Hemos desarrollado y comprendido los principios básicos del IoT, su desarrollo histórico, las tecnologías que permiten su implementación y sus aplicaciones en diversas industrias. Asimismo, analizamos tanto sus ventajas como sus retos y riesgos, subrayando la importancia de la seguridad en un mundo cada vez más conectado.

Como hemos podido observar en la sección de aplicaciones, los beneficios del IoT son claros en términos de mejora de la calidad de vida, gestión eficiente de recursos y transformación de sectores enteros. Desde la automatización industrial hasta la agricultura de precisión y la atención médica remota, el IoT ha demostrado su capacidad para optimizar procesos y reducir costos.

No obstante, este progreso viene acompañado de desafíos significativos. La seguridad y la privacidad son preocupaciones cruciales que deben ser abordadas con seriedad. La falta de estándares de seguridad y la vulnerabilidad a ciberataques son aspectos que requieren atención continua.

En conclusión, el Internet de las Cosas cesa de ser meramente una tecnología emergente para convertirse en una fuerza transformadora que sigue configurando nuestro mundo. Comprendiendo sus fundamentos y desafíos, podemos aprovechar al máximo sus beneficios y avanzar hacia un futuro más conectado, eficiente y seguro.

#

# Bibliografía

Barrio, M. (2018). Internet de las cosas. Madrid: Reus.

Chang Faiconí, D., & Lozano Solís, A. (2013). Desarrollo e implementación de un sistema para el control e inventario continuo, utilizando tecnología RFID, para la biblioteca de la UPS sede Guayaquil (Bachelor's thesis).

Evans, D. (2011). The internet of things. How the Next Evolution of the Internet is Changing Everything, Whitepaper, Cisco Internet Business Solutions Group (IBSG), 1, 1-12.

Internet de las cosas Teoría y práctica - Armando Román Gallardo, José Román Herrera Morales, Sara Sandoval Carrillo, María Andrade Aréchiga, Erika Margarita Ramos Michel - Universidad de Colima - 2023

Montenegro, G. A., & Marchesin, A. E. (2007). Sistema de identificación por radiofrecuencia (RFID). Nuevas Tecnologías, (2).

Utilizando el análisis de datos en la IoT para tomar decisiones en tiempo real | SEIDOR. (2023, 13 septiembre). Utilizando el Análisis de Datos En la IoT Para Tomar Decisiones En Tiempo Real | SEIDOR. <https://www.seidor.com/blog/analisis-datos-iot-decisiones-tiempo-real>

What is the Internet of Things (IoT)? | IBM. (s. f.). <https://www.ibm.com/topics/internet-of-things>

# Anexo: Autoevaluación con Preguntas y Respuestas

1. **¿Cuál es el concepto básico de IoT?**

* El Internet de las cosas se refiere a la interconexión de dispositivos y objetos cotidianos a través de la red, permitiéndoles recopilar y compartir datos entre sí de forma autónoma.

1. **¿En qué ramas se dividen las aplicaciones posibles del IoT?**

* Las aplicaciones del IoT se suelen dividir en cinco principales ramas de uso: consumo, comerciales, industriales, de infraestructuras y militares.

1. **¿Cuál es la diferencia fundamental entre la Web y el Internet?**

* Por un lado, consideramos al Internet como la unificación que se obtiene compuesta de routers y otros componentes que permite la transferencia de datos rápida, confiable y segura.

Por su parte, la Web es una capa de aplicaciones en la parte superior de la red. Su objetivo principal es crear una interfaz que haga accesible el flujo de datos a través de Internet.

1. **¿Por qué se ha de implementar IPv6 al IoT?**

* En 2010, se agotaron las direcciones IPv4 en todo el mundo. Dado que los miles de millones de nuevos sensores potenciales requerirán direcciones IP únicas, esta situación podría obstaculizar el avance del Internet de las cosas. Implementar IPv6 permitirá solventar este agotamiento.

Además, IPv6 ofrece beneficios como lo son características de seguridad mejoradas y capacidades de configuración automática, lo que facilita la gestión de las redes.

1. **¿Qué desafíos exhibe en términos energéticos hoy por hoy el IoT?**

* Uno de los principales desafíos energéticos que enfrenta el Internet de las Cosas hoy en día es la autosuficiencia de los sensores. Es esencial que estos dispositivos sean capaces de operar de manera continua sin la necesidad de intervención humana frecuente, como el cambio de baterías. Este es un punto crítico, ya que tener que reemplazar baterías en una gran cantidad de dispositivos representa una debilidad significativa en la implementación del IoT a gran escala.

La solución a este desafío radica en el desarrollo de métodos que permitan a los sensores generar su propia electricidad aprovechando el entorno.

1. **¿Cuáles son las características de los sistemas embebidos?**

* Algunas características de los sistemas embebidos son:
  + Cuentan con sensores y actuadores
  + No son equivalentes a sistemas de cómputo como las notebooks o equipos de escritorio
  + Tienen recursos limitados y aplicaciones específicas que los hacen muy útiles
  + Tamaños regularmente pequeños
  + Bajo costo
  + Consumos de energía bajos
  + No requieren conocimientos avanzados para su manipulación

1. **Explique la importancia del uso de las placas Arduino para el desarrollo de proyectos basados en el IoT.**

* El uso de **placas Arduino** ha sido clave en el desarrollo de proyectos basados en el **Internet de las Cosas**. Existen una gran cantidad de modelos de Arduino, cada uno diseñado con diferentes características y propósitos, como el tamaño físico, el número de pines de entrada/salida y el modelo del microcontrolador. Estas placas permiten la creación de dispositivos IoT que pueden recopilar datos, procesarlos y comunicarse con otros sistemas, utilizando sensores y actuadores conectados a la red.

1. **Desarrolle la relación entre el Cloud Computing y el IoT.**

* La computación en la nube y el Internet de las cosas están estrechamente relacionados porque permiten y apoyan el desarrollo de entornos digitales conectados. El Internet de las cosas produce grandes cantidades de datos a través de sus numerosos dispositivos y sensores distribuidos, lo que requiere un sistema sólido y escalable para almacenar, procesar y administrar esos datos de manera efectiva. La computación en la nube aporta una infraestructura adaptable y escalable para el procesamiento masivo de datos en este punto. La nube brinda el espacio y los recursos necesarios para manejar este gran volumen de datos, lo que permite que los datos recolectados por los dispositivos de Internet de las cosas sean accesibles de forma ubicua y bajo demanda.

1. **¿Cuáles son las fases de evolución de la web?**

* La Web ha pasado por varias fases evolutivas diferentes:
* **1era Fase**: Primero fue la fase de investigación, durante este periodo, la Web era utilizada en su mayoría por las universidades para fines de investigación.
* **2da Fase**: La segunda fase de la red podría denominarse "*brochureware*". Esta etapa está caracterizada por la "fiebre del oro" de los nombres de dominio, y se enfoca en la necesidad de las empresas de compartir información a través de Internet para que la gente supiera más sobre los productos y servicios que proveían.
* **3era Fase**: En la tercera fase, la Web pasó de albergar datos estáticos a proporcionar información transaccional, gracias a la cual se podían comprar y vender productos y servicios, así como suministrar servicios.
* **4ta Fase**: En la cuarta fase, en la que nos encontramos ahora, predomina la Web "social" o de las "experiencias", ya que permiten a las personas comunicarse, conectarse y compartir información (texto, fotos y vídeos) sobre ellos mismos con amigos y familiares.

1. **¿Qué es la tecnología RFID? ¿Cómo está constituida?**

* El RFID, “Radio Frequency Identification” (Identificación por radio frecuencia), es una tecnología de captura de datos, muy parecido al sistema de código de barras, pero en lugar de código impreso utiliza un microchip y un circuito impreso a modo de antena dentro del cual se almacena el código alfanumérico, capaz de sustituir el actual sistema de leer las etiquetas de código de barras ante un lector.
* Un sistema RFID está constituido por:
  + Uno o más Tags (transponder) que incluye un chip semiconductor y una antena.
  + Uno o más dispositivos de lectura/escritura incluye una antena.
  + Un software de Aplicación y una computadora (Host).

1. Es una tecnología que permite identificar objetos mediante ondas de radio de manera única y pudiendo captar cientos de objetos a la vez. [↑](#footnote-ref-0)
2. El Instituto de Ingenieros Eléctricos y Electrónicos (IEEE) es una asociación mundial de ingenieros dedicada a lanormalización y el desarrollo en áreas técnicas. Según el mismo IEEE, su trabajo es promover la creatividad, el desarrollo y la integración, compartir y aplicar los avances en las tecnologías de la información, electrónica y ciencias en general para beneficio de la humanidad y de los mismos profesionales. [↑](#footnote-ref-1)