Resumen 1.0

ASIGNACIÓN DE CAPACIDADES DE CANALES
Frecuencia promedio de mensajes (λ): es la suma de las frecuencias de los mensajes de todas las
líneas entrantes al nodo.
T = [ 1 / (bits/mensajes) ]
Frecuencia de mensajes por segundo a la salida (μ):
μ = [ bps ]
Intensidad de tráfico (ρ):
Frecuencia total de red:
Retardo Promedio de Mensajes para la red (E[T]):
Promedio estadístico:
Frecuencia mínima de mensajes (λ):
Siempre es posible disminuir el tiempo de retardo, aumentado el valor de C y con ello el costo.

ELECCIÓN DEL MEDIO DE ACCESO

| Zona       | Requerimient | Segurizació | Espaci  | Recursos    | Medio de         |
| ---------- | ------------ | ----------- | ------- | ----------- | ---------------- |
|            | o de Ancho   | n           | o       | Económicos  | Acceso           |
|            | de Banda     |             | Físico  |             | Recomendado      |
| Urbana     | Bajo (4–8    | No          | Sí/No   | Bajos       | Par Telefónico   |
|            | Mbps)        |             |         |             | + HDSL           |
| Urbana     | Alto (>100   | Sí          | Sí      | Altos       | Fibra Óptica en  |
|            | Mbps)        |             |         |             | Anillo           |
| Suburbana  | Bajo (4–8    | No          | Sí      | Medios      | Radio Enlace     |
Mbps)
| Suburbana  | Bajo (4–8   | Sí  | Sí  | Medios/Altos  | Radio Enlace +    |
| ---------- | ----------- | --- | --- | ------------- | ----------------- |
|            | Mbps)       |     |     |               | Satelital backup  |
| Suburbana  | Alto (>100  | Sí  | Sí  | Altos         | Fibra Óptica en   |
|            | Mbps)       |     |     |               | Anillo            |
| Rural      | Bajo (4–8   | No  | No  | Bajos         | Antena Satelital  |
Mbps)
| Rural  | Medio (10–50  | Sí  | Sí  | Medios/Altos  | Fibra Óptica +  |
| ------ | ------------- | --- | --- | ------------- | --------------- |
|        | Mbps)         |     |     |               | Radio Enlace    |
| Rural  | Bajo (4–8     | No  | No  | Bajos         | Satelital       |
Mbps,
ubicación
transitoria)
| Montañosa  | Bajo (4–8  | No  | No  | Bajos  | Satelital  |
| ---------- | ---------- | --- | --- | ------ | ---------- |
| / Selva    | Mbps)      |     |     |        |            |
Residencia Medio (10–50  No  Sí  Bajos/Medios  Cable Coaxial
| l (TV  | Mbps)  |     |     |     | (Cable Módem)  |
| ------ | ------ | --- | --- | --- | -------------- |
Cable)

Organización pequeña en zona Urbana, requiere bajo ancho de banda no requiere segurización y no
se dispone de grandes recursos económicos:  Par telefónico + Modem HDSL

Organización Madura en Zona Urbana definitiva con gran requerimiento de ancho de banda y
segurización, se dispone de recursos ($$):  Fibra Óptica y conexión en anillo

Organización madura en zona Rural ubicación transitoria con bajo ancho de banda y no dispone de
espacio físico para infraestructura: Antena Satelital

Organización madura ubicada definitiva en zona suburbana con bajo requerimiento de ancho de
banda y dispone de espacio físico y no requiere segurización: Radio Enlace

Organización madura ubicada definitiva en zona suburbana con bajo requerimiento de ancho de
banda y dispone de espacio físico y requiere segurización: Radio Enlace y segurización por
Satélite
Organización madura ubicada definitiva en zona suburbana con gran requerimiento de ancho de
banda y requiere segurización: Fibra Óptica y conexión en anillo
Organización en crecimiento ubicada definitiva en zona rural con mediano requerimiento de ancho
de banda y requiere segurización, dispone de espacio físico: Fibra Óptica y segurización por
Radio Enlace
Organización pequeña en zona montañosa/selva, requiere bajo ancho de banda no requiere
segurización: Satelital
Acceso y Segurización por Fibra Óptica: los recorridos hasta llegar a la sala de equipos deben ser
disjuntos, es decir en ningún lugar deben compartir recorridos.
Acceso y Segurización por Radio Enlace o Fibra Óptica: Independientemente del tipo de Acceso
y Segurización es conveniente que el servicio lo realicen distintos operadores.

TEORÍA DE COLA
La teoría de redes de cola de espera (teoría de cola) es la fundamentación matemática para la
mayor cantidad de modelos analíticos de sistemas de computación.
Las relaciones establecidas por la teoría de cola son relaciones entre cantidades abstractas que no
pueden ser observadas directamente.
Elementos de un Sistema de Colas Abiertas
Una cola es una línea de espera y la teoría de cola es el estudio del fenómeno de la espera en la
cola.
Usuarios: significa una entidad que desea algún tipo de servicio de un conjunto de servicios que
ofrece el sistema.
Servicios: establecer una determinada comunicación (sistema telefónico), procesar una pregunta o
atender algún pedido de entrada / salida.

t(w) = t(q) + t(s)

Notaciones de un Sistema de Cola
Fuentes: es el conjunto de usuarios que pueden solicitar el servicio del sistema, puede ser una
fuente finita o infinita.
1. Fuente Infinita: la longitud de la cola está determinada por el número de usuarios en el
sistema.
2. Fuente Infinita: la cola es ilimitada, la frecuencia de arribos no está afectada por el número de
usuarios en el sistema.
Proceso de Arribo: se supone que los usuarios entran en el sistema en los tiempos: t < t < t < … <
0 1 2
t .
n
Las variables aleatorias k = tk – t (k-1), (donde k 1) se llaman intervalos entre arribos.
● Su patrón de arribo sigue una distribución de Poisson.
● Intervalo entre arribos y la probabilidad de n arribos en algún intervalo de tiempo t:
Distribución del Tiempo en Servicio: la función de distribución del tiempo de servicio en la teoría de
cola es exponencial, lo cual define el denominado servicio (o atención) aleatoria.
Coeficiente de variación al cuadrado: C2 (x)
● Para C2 (t) ≈ 0, el proceso de arribo tiene un patrón regular.
● Para C2 (t) ≈ 1, el proceso de arribo es aproximadamente aleatorio.
● Para C2 (t) > 1, los arribos tienden a agruparse.
Capacidad Máxima del Sistema de Cola:
● Cola infinita: siempre se permite el arribo de usuarios, nadie es rechazado.
● Cola nula (sistema de pérdida): no hay espera posible; si el servidor está ocupado, el usuario
se pierde.
● Cola finita: se admite esperar, pero hasta un número máximo de usuarios; si se supera, el
nuevo arribo es rechazado.
Número de Servidores: el sistema de cola más simple es el de servidor único, el cual puede atender
1 solo usuario por vez. Un sistema multi servidor tiene servidores idénticos y puede servir hasta n
usuarios simultáneamente.

Disciplina de Cola (disciplina de servidor): es la regla para seleccionar el próximo usuario a recibir
servicio.
● FIFO (primero en arribar, primero en atender).
● LIFO (último en arribar, primero en atender).
Notación Kendall: A/B/c/k/n/Z.
Usamos: A/B/c, se la utiliza cuando la cola de espera no tiene límites, la fuente de usuarios es
infinita y la disciplina es FIFO.
Intensidad del Tráfico: es la relación entre el tiempo de servicio promedio E[s] y el intervalo
promedio entre arribos E[t].
“u” determina el número mínimo de servidores que se requieren para cumplir con el flujo entrante de
usuarios.
Factor de utilización del servicio: es la probabilidad de que algún servidor esté ocupado. Para
sistemas de un único servidor coincide con la intensidad de tráfico.
Leyes de Little: medidas de performance primarias.
90 percentil del tiempo en el sistema: w(90) define la cantidad de tiempo necesaria tal que el 90% de
todos los que arribaron a la cola (o sea al sistema) no esperan más que ese tiempo.
Modelo de Cola Abierta
El sistema de cola M/M/c es un modelo de cola simple y abierta que puede ser usado para modelar
algún sistema de computo. Es abierto porque los usuarios entran al sistema desde el exterior,
reciben el servicio y parten.

Probabilidad de que todos los servidores (c) estén ocupados de tal forma de que un nuevo usuario
deba esperar servicio: C( c, u).
Cuando c = 1 las fórmulas se simplifican resultando:
Modelo de cola en sistemas interactivos con población finita
Se considerará ahora un modelo de cola más realista; modelo de cola cerrado (ningún usuario ni
entra ni sale) y con una población finita de usuarios.
Un sistema de procesamiento central consiste de una cola para la unidad central de proceso (CPU),
algunos terminales de entrada/salida y un sistema asociado de cola para cada uno de estos
dispositivos.

Los usuarios interactúan con la CPU a través de los n terminales. Cada usuario se supone en uno de
los siguientes estados en cada instante:
1. “Pensando” en el terminal (“tiempo de pensamiento”, t)
2. Esperando algún tipo de atención.
3. Recibiendo el servicio.
Modelo de multiprogramación para el servidor central
Es un modelo (ver figura) cerrado, pues contiene un número fijo de programas k, los cuales pueden
ser pensados como atendidos siguiendo un ciclo interminable, donde en cada momento hay un
programa realizando el ciclo de la CPU.

HARDWARE DE REDES (Clasificación)
Según la tecnología de transmisión:
Difusión (broadcast): todas las máquinas comparten un único canal. Los mensajes llegan a todos,
pero sólo el destinatario los procesa. Permite:
1. Broadcasting: envío a todos.
2. Multicasting: envío a un grupo específico.
3. Unicasting: envío de un emisor a un receptor.
Punto a punto: conexión directa entre pares de máquinas. Los paquetes pueden pasar por nodos
intermedios y pueden seguir distintas rutas. Es común en redes grandes.
Según la escala (tamaño físico):
PAN (Personal Area Network): redes personales de corto alcance, como Bluetooth, que conectan
dispositivos de un usuario.
LAN (Local Area Network): redes privadas en edificios o campus. Son rápidas (10 Mbps a 10 Gbps),
con baja latencia y baja tasa de errores.
1. Topologías comunes: bus (ej. Ethernet, IEEE 802.3) y anillo (ej. Token Ring, FDDI).
2. Pueden ser de asignación estática (por turnos) o dinámica (por demanda).
MAN (Metropolitan Área Network): cubren una ciudad. Ejemplo: TV por cable o Internet por cable,
estándar IEEE 802.16.
WAN (Wide Area Network): abarcan países o continentes. Conectan hosts mediante una subred
compuesta por líneas de transmisión (cobre, fibra, radio) y enrutadores. Generalmente usan
conmutación de paquetes (store and forward). También existen WAN satelitales.
Interred: unión de distintas redes, a veces incompatibles, conectadas con gateways que hacen
traducción de protocolos. Internet es el ejemplo principal.
Redes inalámbricas
Interconexión de sistemas: corto alcance, para conectar periféricos sin cables (ej. Bluetooth).
LANs inalámbricas (Wi-Fi, IEEE 802.11): comunicación en hogares y oficinas. Pueden conectarse
mediante un punto de acceso o de manera directa entre dispositivos.

WANs inalámbricas (redes celulares): cubren grandes áreas. Han evolucionado en generaciones:
● 1G: analógica, sólo voz.
● 2G: digital, voz.
● 3G: digital, voz y datos.
Redes domésticas
Buscan conectar todos los dispositivos del hogar:
● Computadoras y periféricos.
● Equipos de entretenimiento.
● Teléfonos y sistemas de comunicación.
● Electrodomésticos y aparatos inteligentes.
● Sistemas de seguridad y monitoreo.
● Características necesarias: facilidad de instalación, confiabilidad, bajo costo, alto desempeño
y seguridad.
● Pueden ser alámbricas (más seguras) o inalámbricas (más económicas y fáciles de instalar).
Interredes
Permiten que distintas redes se comuniquen entre sí y requieren hardware especial (gateways) que
traduce protocolos y formatos.
Modelo de referencia OSI
Propuesto por la ISO, tiene siete capas, cada una con funciones bien definidas. Principios:
1. Cada capa responde a una abstracción diferente.
2. Debe cumplir una función concreta.
3. Se busca estandarización internacional.
4. Se minimiza la información entre capas.
5. Debe haber suficientes capas para separar funciones, pero no tantas como para complicar la
arquitectura.

Las 7 capas del modelo OSI
1. Capa física:
○ Transmite bits puros a través del canal.
○ Define aspectos eléctricos, mecánicos y de temporización (voltajes, duración de un bit,
conectores, etc.).
2. Capa de enlace de datos:
○ Convierte el medio físico en una línea libre de errores.
○ Fragmenta en tramas, maneja errores y flujo de datos.
○ En redes de difusión, controla el acceso al medio (subcapa MAC).
3. Capa de red:
○ Controla el enrutamiento de paquetes en la subred.
○ Maneja congestión, calidad de servicio y diferencias entre redes heterogéneas.
○ Es esencial en WAN; en redes de difusión puede ser mínima o inexistente.
4. Capa de transporte:
○ Establece una comunicación de extremo a extremo entre aplicaciones.
○ Divide y asegura la llegada de datos en orden.
○ Ofrece distintos tipos de servicio: confiable, no confiable, orientado a mensajes o difusión.
5. Capa de sesión:
○ Permite iniciar, mantener y finalizar sesiones entre usuarios.
○ Ofrece control de diálogo, administración de turnos y sincronización en transmisiones largas.
6. Capa de presentación:
○ Se encarga de la sintaxis y semántica de la información.
○ Facilita la comunicación entre computadoras con diferentes representaciones de datos.
○ Define estructuras de datos y su codificación estándar.
7. Capa de aplicación:
○ Contiene protocolos usados directamente por los usuarios.
○ Ejemplos: HTTP (Web), FTP (transferencia de archivos), SMTP (correo electrónico), NNTP
(noticias).

Modelo de referencia TCP/IP
Objetivos principales:
1. Conectar múltiples redes de manera sólida y flexible.
2. Mantener la comunicación incluso si fallaban partes de la red.
3. Soportar aplicaciones diversas, desde archivos hasta transmisión de voz en tiempo real.
Capas del modelo TCP/IP
1. Capa de interred (Internet layer)
○ Similar a la capa de red de OSI.
○ Permite que los hosts envíen paquetes independientes a través de cualquier red.
○ Los paquetes pueden llegar fuera de orden; la capa superior se encarga de reordenarlos.
○ Protocolo principal: IP (Internet Protocol).
○ Se encarga del enrutamiento y evita la congestión.
○ Analogía: funciona como el correo internacional: cada país (red) tiene sus reglas y timbres,
pero el envío llega a destino.
2. Capa de transporte (Transport layer)
○ Proporciona comunicación de extremo a extremo entre aplicaciones.
○ Protocolos principales:
■ TCP: confiable, orientado a conexión, entrega los datos en orden y maneja control de
flujo.
■ UDP: no confiable, no orientado a conexión, útil cuando importa la rapidez más que la
entrega exacta (voz, video, consultas rápidas).
3. Capa de aplicación (Application layer)
○ Combina funciones de las capas aplicación, presentación y sesión de OSI.
○ Contiene protocolos de uso directo por usuarios y aplicaciones:
■ TELNET (terminal remota), FTP (transferencia de archivos), SMTP (correo electrónico).
■ Otros protocolos añadidos con el tiempo: DNS, NNTP, HTTP, etc.
4. Capa host a red (Host-to-network layer)

○ Se encarga de la conexión del host a la red física.
○ TCP/IP no define protocolos específicos para esta capa; depende de la red y del host.

Resumen 2.0

ASIGNACIÓN DE CAPACIDADES DE CANALES
Frecuencia promedio de mensajes (λ): es la suma de las frecuencias de los mensajes de todas las
líneas entrantes al nodo.
T = [ 1 / (bits/mensajes) ]
Frecuencia de mensajes por segundo a la salida (μ):
μ = [ bps ]
Intensidad de tráfico (ρ):
Frecuencia total de red:
Retardo Promedio de Mensajes para la red (E[T]):
Promedio estadístico:
Frecuencia mínima de mensajes (λ):
Siempre es posible disminuir el tiempo de retardo, aumentado el valor de C y con ello el costo.

HARDWARE DE REDES
Tipos de tecnología de transmisión que se utilizan de manera extensa
redes de Difusión (broadcast): tienen un solo canal de comunicación, por lo que todas las
máquinas de la red lo comparten. Si una máquina envía un mensaje corto (paquete), todas las
demás lo reciben.
Un campo de dirección dentro del paquete especifica el destinatario. Cuando una máquina recibe un
paquete, verifica el campo de dirección. Si el paquete va destinado a esa máquina, lo procesa; si va
destinado a otra, lo ignora.
● Difusión (broadcasting): permite enviar un paquete a todos los destinos. Todas las máquinas
lo reciben y procesan.
● Multidifusión (multicasting): permite enviar un paquete a un subconjunto de máquinas.
Enlaces Punto a Punto: constan de muchas conexiones entre pares individuales de máquinas.
Para ir del origen al destino, un paquete podría tener que visitar una o más máquinas intermedias.
● Redes de Unidifusión (unicasting): es transmisión de punto a punto con un emisor y un
receptor
Escalas de las Redes

Redes de Difusión
Redes LAN:
Son redes de propiedad privada que se encuentran en un solo edificio o en un campus de pocos
kilómetros de longitud.
Se utilizan ampliamente para conectar computadoras personales y estaciones de trabajo en oficinas
de una empresa / fábrica para compartir recursos e intercambiar información.
Están restringidas por tamaño, todas las máquinas están unidas por un cable, se ejecutan a una
velocidad entre 10 a 100 Mbps, tiene un retardo bajo y cometen pocos errores.
Red Bus:
En cualquier instante al menos una máquina es la maestra y puede
transmitir. Todas las demás máquinas se abstienen de enviar.
Si dos o más paquetes entran en colisión, cada computadora espera un
tiempo aleatorio y lo intenta de nuevo más tarde.
Red de Anillo:
Cada bit se propaga por sí mismo, sin esperar al resto del paquete al que
pertenece.
Asignación Estática: consiste en dividir el tiempo en intervalos discretos y utilizar un algoritmo
round-robin, permitiendo que cada máquina transmita sólo cuando llegue su turno. Cuando no tiene
que transmitir, se desperdicie capacidad de canal.
Asignación Dinámica:
● Centralizada: hay una sola entidad, la cual determina quién sigue.
● Descentralizada: no hay una entidad central; cada máquina decide cuándo transmitir.

Redes MAN:
Cubren una ciudad.
Redes WAN:
Líneas de transmisión: mueven bits entre máquinas.
Elementos de conmutación: son computadoras especializadas que conectan tres o más líneas de
transmisión.
Subred organizada / de almacenamiento y reenvío (store and forward) / de conmutación de
paquetes: Cuando un paquete es enviado desde un enrutador a otro, a través de uno o más
enrutadores intermedios, el paquete se recibe en cada enrutador intermedio en su totalidad, se
almacena ahí hasta que la línea de salida requerida esté libre y, por último, se reenvía.
Las decisiones de enrutamiento se hacen de manera local. La manera en que el enrutador A toma
esa decisión se conoce como algoritmo de enrutamiento.

Redes Inalámbricas:
Interconexión de sistemas: corto alcance, para conectar periféricos sin cables (ej. Bluetooth).
LANs inalámbricas: comunicación en hogares y oficinas. Pueden conectarse mediante un punto de
acceso o de manera directa entre dispositivos. Cada computadora tiene un módem de radio y una
antena mediante los que se puede comunicar con otros sistemas.
WANs inalámbricas (redes celulares): cubren grandes áreas. Han evolucionado en generaciones:
● 1G: analógica, sólo voz.
2G: digital, voz.
● 3G: digital, voz y datos.
Redes domésticas
Buscan conectar todos los dispositivos del hogar:
● Computadoras y periféricos.
● Equipos de entretenimiento.
● Teléfonos y sistemas de comunicación.
● Electrodomésticos y aparatos inteligentes.
● Sistemas de seguridad y monitoreo.
● Características necesarias: facilidad de instalación, confiabilidad, bajo costo, alto desempeño
y seguridad.
● Pueden ser alámbricas (más seguras) o inalámbricas (más económicas y fáciles de instalar).
“Los costos favorecen la conectividad inalámbrica, pero la seguridad favorece la conectividad
alámbrica. ”
Interredes
Es un conjunto de redes interconectadas. Permiten que distintas redes se comuniquen entre sí y
requieren hardware especial (gateways) que traduce protocolos y formatos.
Si el sistema que aparece en el área gris contiene solamente enrutadores, es una subred; si
contiene enrutadores y hosts, es una Red WAN.

Modelo OSI (Interconexión de Sistemas Abiertos)
Son sistemas que están abiertos a la comunicación con otros sistemas.

Las 7 capas del modelo OSI
1. Capa física:
En esta capa se lleva a cabo la transmisión de bits puros a través de un canal de
comunicación. Asegura que el bit recibido sea el mismo que el bit enviado.
Sus aspectos de diseño tienen que ver con interfaces mecánicas, eléctricas y de
temporización, además del medio físico de transmisión.
2. Capa de enlace de datos:
La tarea principal de esta capa es transformar un medio de transmisión puro en una línea de
comunicación, para que al llegar a la capa de red, aparezca libre de errores de transmisión.
El emisor fragmenta los datos de entrada en “tramas de datos” (cientos o miles de bytes) y los
transmite de manera secuencial.
El receptor confirma la recepción correcta de cada trama devolviendo una “trama de
confirmación de recepción”
3. Capa de red:
4. Capa de transporte:
5. Capa de sesión:
6. Capa de presentación:
7. Capa de aplicación:

Resumen 3.0

CAPA 1 Y 2 (Función y Objetivo)
Capa 1 - Capa física: su función es transmitir los bits puros, unos y ceros, a través de un canal de
comunicación. Asegura que el bit recibido sea el mismo que el bit enviado.
● Objetivo: asegurar que los datos digitales enviados por un dispositivo lleguen íntegros al otro,
transformando la información en señales físicas que puedan viajar por el canal de
comunicación.
Capa 2 - Capa de Enlace de Datos: su función es transformar un medio de transmisión puro en una
línea de comunicación, para que al llegar a la capa de red, aparezca libre de errores de transmisión.
● Objetivo: transformar los datos de entradas en “Tramas de Datos” para transmitirlos de
manera secuencial. Luego el receptor confirma la recepción correcta de cada trama
devolviendo una “trama de confirmación de recepción”.
Capa 3 - Capa de red.
Capa 4 - Capa de transporte.
Capa 5 - Capa de sesión.
Capa 6 - Capa de presentación.
Capa 7 - Capa de aplicación.
Punto de Saturación
Punto de Saturación: es el número máximo de terminales que pueden incluirse en un sistema
interactivo sin causar interferencia mutua entre los usuarios.
● E[s] = tiempo medio de servicio de la CPU por interacción.
● E[t] = tiempo medio de pensamiento del usuario.
Interpretación:
● Si el número de terminales N es menor o igual a N*, el sistema funciona eficientemente (sin
esperas significativas).
● Si N supera N*, el sistema entra en saturación, aumentando considerablemente el tiempo de
respuesta (W).
Si la tasa de arribo (λ) es mayor que la tasa de servicio (μ): El sistema entra en saturación y la cola
crece indefinidamente, y con ello el tiempo de espera.

Redes LAN, MAN y WAN:
Redes LAN (Local Area Network):
Son redes de propiedad privada que se encuentran en un solo edificio o en un campus de pocos
kilómetros de longitud.
Se utilizan ampliamente para conectar computadoras personales y estaciones de trabajo en oficinas
de una empresa o fábrica para compartir recursos e intercambiar información.
Están restringidas por tamaño, todas las máquinas están unidas por un cable, se ejecutan a una
velocidad entre 10 a 100 Mbps, tiene un retardo bajo y cometen pocos errores.
Redes MAN (Metropolitan Área Network):
Es una red que interconecta varias redes locales dentro de una misma ciudad, ofreciendo servicios
de comunicación y transmisión de datos a alta velocidad.
Redes Wan (Wide Area Network):
Es una red de comunicaciones que abarca grandes distancias geográficas, como países o
continentes, y que interconecta múltiples redes locales (LAN) o metropolitanas (MAN) para permitir
la comunicación entre ellas.
TEORÍA DE COLA
La teoría de redes de cola de espera o Teoría de Cola es la fundamentación matemática para la
mayor cantidad de modelos analíticos de sistemas de computación.
Las relaciones establecidas por la teoría de cola son relaciones entre cantidades abstractas que no
pueden ser observadas directamente.
Elementos de un Sistema de Colas Abiertas
Una cola es una línea de espera y la teoría de cola es el estudio del fenómeno de la espera en la
cola.

Usuarios: es una Entidad que desea algún tipo de servicio de un conjunto de servicios que ofrece el
sistema.
Cola o Línea de Espera: se origina cuando ingresan usuarios al sistema y no hay servidores
disponibles que los puedan atender. De esta forma, los usuarios conforman una cola de espera para
ser atendidos.
Servidor: Es quien provee uno o más servicios que resultan de interés para los usuarios. Puede
tener un único servidor, permitiendo atender un único usuario por vez, o ser multi-servidor y tener
varios servidores idénticos que puedan atender hasta “n” usuarios simultáneamente.
Servicios: establecen una determinada comunicación, procesan una pregunta o atienden algún
pedido de entrada / salida.
Notaciones de un Sistema de Cola
Fuentes: es el conjunto de usuarios que pueden solicitar el servicio del sistema, puede ser una
fuente finita o infinita.
1. Fuente finita: la longitud de la cola está determinada por el número de usuarios en el sistema.
2. Fuente Infinita: la cola es ilimitada, la frecuencia de arribos no está afectada por el número de
usuarios en el sistema.
Proceso de Arribo: supone que los usuarios entran en el sistema en los tiempos: t < t < t < … < t .
0 1 2 n
Distribución del Tiempo en Servicio: la función de distribución del tiempo de servicio en la teoría de
cola es exponencial, lo cual define el denominado servicio (o atención) aleatoria.
Coeficiente de variación al cuadrado: C2 (x)
● Para C2 (t) ≈ 0, el proceso de arribo tiene un patrón regular.
● Para C2 (t) ≈ 1, el proceso de arribo es aproximadamente aleatorio.
● Para C2 (t) > 1, los arribos tienden a agruparse.

Capacidad Máxima del Sistema de Cola:
● Cola infinita: siempre se permite el arribo de usuarios, nadie es rechazado.
● Cola nula (sistema de pérdida): no hay espera posible; si el servidor está ocupado, el usuario
se pierde.
● Cola finita: se admite esperar, pero hasta un número máximo de usuarios; si se supera, el
nuevo arribo, es rechazado.
M/M/1
M/M/1 es la notación que se utiliza para describir los Parámetros y Características de un Sistema de
Cola, suponiendo que la cola de espera no tiene límites, la fuentes de usuarios es infinita y la
disciplina es FIFO.
● M: indica que el proceso de llegada de los usuarios sigue una distribución de Poisson
● M: indica que el tiempo de servicio para cada usuario sigue una distribución exponencial.
● 1: indica que hay un único servidor en el sistema.
Disciplina de Cola (disciplina de servidor): es la regla para seleccionar el próximo usuario a recibir
servicio.
● FIFO (primero en arribar, primero en atender).
● LIFO (último en arribar, primero en atender).
Notación Kendall: A/B/c/k/n/Z.
Usamos: A/B/c, se la utiliza cuando la cola de espera no tiene límites, la fuente de usuarios es
infinita y la disciplina es FIFO.
Intensidad del Tráfico: es la relación entre el tiempo de servicio promedio E[s] y el intervalo promedio
entre arribos E[t]. Determina el número mínimo de servidores que se requieren para cumplir con el
flujo entrante de usuarios.
Factor de utilización del servicio: es la probabilidad de que algún servidor esté ocupado. Para
sistemas de un único servidor coincide con la intensidad de tráfico.
90 percentil del tiempo en el sistema: w(90) define la cantidad de tiempo necesaria tal que el 90% de
todos los que arribaron a la cola (o sea al sistema) no esperan más que ese tiempo.

Modelo de Cola Abierta
El sistema de cola M/M/c es un modelo de cola simple y abierta que puede ser usado para modelar
algún sistema de computo. Es abierto porque los usuarios entran al sistema desde el exterior,
reciben el servicio y parten.
Modelo de cola en sistemas interactivos con población finita
Se considerará ahora un modelo de cola más realista; modelo de cola cerrado (ningún usuario ni
entra ni sale) y con una población finita de usuarios.
Un sistema de procesamiento central consiste de una cola para la unidad central de proceso (CPU),
algunos terminales de entrada / salida y un sistema asociado de cola para cada uno de estos
dispositivos.
Los usuarios interactúan con la CPU a través de los “n” terminales. Cada usuario se supone en uno
de los siguientes estados en cada instante:
1. “Pensando” en el terminal (“tiempo de pensamiento”, t).
2. Esperando algún tipo de atención.
3. Recibiendo el servicio.

Respuestas Parciales Viejos

TEORÍA DE COLA
Elementos de un Sistema de Colas Abiertas
Una cola es una línea de espera y la teoría de cola es el estudio del fenómeno de la espera en la
cola.
Usuarios: es una entidad que desea algún tipo de servicio de un conjunto de servicios que ofrece el
sistema.
Cola o Línea de Espera: se origina cuando ingresan usuarios al sistema y no hay servidores
disponibles que los puedan atender. De esta forma, los usuarios conforman una cola de espera para
ser atendidos.
Servidor: Es quien provee uno o más servicios que resultan de interés para los usuarios. Puede
tener un único servidor, el cual puede atender un único usuario por vez, o ser multi servidor y tener
varios servidores idénticos que puedan atender hasta “n” usuarios simultáneamente.
Servicios: establecen una determinada comunicación, procesan una pregunta o atienden algún
pedido de entrada / salida.

Punto de Saturación
Punto de Saturación: es el número máximo de terminales que pueden incluirse en un sistema
interactivo sin causar interferencia mutua entre los usuarios.
● E[s] = tiempo medio de servicio de la CPU por interacción.
● E[t] = tiempo medio de pensamiento del usuario.
Interpretación:
● Si el número de terminales N es menor o igual a N*, el sistema funciona eficientemente (sin
esperas significativas).
● Si N supera N*, el sistema entra en saturación, aumentando considerablemente el tiempo de
respuesta (W).
Si la tasa de arribo (λ) es mayor que la tasa de servicio (μ): El sistema entra en saturación y la cola
crece indefinidamente, y con ello el tiempo de espera.
M/M/1
M/M/1 es la notación que se utiliza para describir los parámetros y características de un sistema de
cola, suponiendo que la cola de espera no tiene límites, la fuentes de usuarios es infinita y la
disciplina es FIFO.
● M: indica que el proceso de llegada de los usuarios sigue una distribución de Poisson
● M: indica que el tiempo de servicio para cada usuario sigue una distribución exponencial.
● 1: indica que hay un único servidor en el sistema.
fg fgf

Lambda es igual a (20 + 10 + 5 + 5) por 10 msj/seg porque todas las terminales comparten el mismo lambda
sub i.

HOJA DE FÓRMULAS

Asignación de Capacidad de Canales
λ (𝑙𝑎𝑚𝑏𝑎 → 𝑓𝑟𝑒𝑐𝑢𝑒𝑛𝑐𝑖𝑎 𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜 𝑑𝑒 𝑚𝑒𝑛𝑠𝑎𝑗𝑒𝑠 𝑑𝑒𝑙 𝑒𝑛𝑙𝑎𝑐𝑒) = [𝑀𝑒𝑛𝑠𝑎𝑗𝑒𝑠 / 𝑆𝑒𝑔𝑢𝑛𝑑𝑜]
𝑖
λ = 𝑐𝑎𝑛𝑡. 𝑡𝑒𝑟𝑚𝑖𝑛𝑎𝑙𝑒𝑠 × 𝑛𝑟𝑜. 𝑚𝑒𝑛𝑠𝑎𝑗𝑒𝑠 𝑝𝑜𝑟 𝑠𝑒𝑔𝑢𝑛𝑑𝑜.
Ejemplo:
𝐶𝑎𝑑𝑎 𝑡𝑒𝑟𝑚𝑖𝑛𝑎𝑙 10 [𝑚𝑒𝑛𝑠𝑎𝑗𝑒𝑠/𝑠𝑒𝑔𝑢𝑛𝑑𝑜] , 𝑠𝑖 ℎ𝑎𝑦 40 𝑡𝑒𝑟𝑚𝑖𝑛𝑎𝑙𝑒𝑠 𝑒𝑛𝑡𝑜𝑛𝑐𝑒𝑠 λ = 40 𝑡𝑒𝑟𝑚𝑖𝑛𝑎𝑙𝑒𝑠 × 10 𝑚𝑠𝑔/𝑠𝑒𝑔
𝑖
𝑛 (𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑 𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜) = [𝑏𝑖𝑡𝑠]
𝑖
Nota: Suele venir como dato del problema
1 1
(𝐿𝑜𝑛𝑔𝑖𝑡𝑢𝑑 𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜 𝑒𝑛 𝑓𝑟𝑒𝑐𝑢𝑒𝑛𝑐𝑖𝑎) = [𝑏𝑖𝑡𝑠 / 𝑚𝑒𝑛𝑠𝑎𝑗𝑒]
𝑛 𝑛
𝑖 𝑖
𝐶 (𝑐𝑎𝑝𝑎𝑐𝑖𝑑𝑎𝑑 𝑑𝑒𝑙 𝑐𝑎𝑛𝑎𝑙) [𝑏𝑝𝑠]
𝑖
µ
(𝑓𝑟𝑒𝑐𝑢𝑒𝑛𝑐𝑖𝑎 𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜 𝑑𝑒 𝑚𝑒𝑛𝑠𝑎𝑗𝑒𝑠 𝑎 𝑙𝑎 𝑠𝑎𝑙𝑖𝑑𝑎 𝑝𝑜𝑟 𝑠𝑒𝑔𝑢𝑛𝑑𝑜) =
𝑛 . 𝑐
[𝑏𝑝𝑠]
𝑖 𝑖
1 1
𝑇 (𝑇𝑖𝑒𝑚𝑝𝑜 𝑑𝑒 𝑟𝑒𝑡𝑎𝑟𝑑𝑜 𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜 𝑑𝑒𝑙 𝑚𝑒𝑛𝑠𝑎𝑗𝑒) = = [seg]
𝑖 ( (𝑛 . 𝑐) −λ) (µ − λ)
𝑖 𝑖
𝑖 𝑖 𝑖
1
𝐿𝑜𝑛𝑔𝑖𝑡𝑢𝑑 𝑃𝑟𝑜𝑚𝑒𝑑𝑖𝑜, 𝑒𝑛 𝑓𝑟𝑒𝑐𝑢𝑒𝑛𝑐𝑖𝑎 = [ bits / mensaje ]
𝐿
λ λ
=
ρ (𝑖𝑛𝑡𝑒𝑛𝑠𝑖𝑑𝑎𝑑 𝑑𝑒 𝑡𝑟á𝑓𝑖𝑐𝑜 𝑜 𝑓𝑎𝑐𝑡𝑜𝑟 𝑑𝑒 𝑢𝑡𝑖𝑙𝑖𝑧𝑎𝑐𝑖ó𝑛) =
µ
(𝑛 . 𝑐)
𝑖 𝑖
𝑁𝑜𝑡𝑎 : ρ < 1 , pasar a %
δ (𝐹𝑟𝑒𝑐𝑢𝑒𝑛𝑐𝑖𝑎 𝑡𝑜𝑡𝑎𝑙 𝑑𝑒 𝑟𝑒𝑑) =
∑ λ
[𝑀𝑒𝑛𝑠𝑎𝑗𝑒𝑠 / 𝑆𝑒𝑔𝑢𝑛𝑑𝑜]
𝑘
𝑘=1
NOTA: λ es λ de cada enlace. Es igual a λ
𝑘

( )2
λ
∑ 𝑖
𝑛
𝑇𝑖𝑒𝑚𝑝𝑜 𝑚í𝑛𝑖𝑚𝑜 = 𝑖 [seg]
δ . 𝐶 . (1 − ρ)
NOTA: δ = λ
Numerador = cantidad total de terminales por la raíz de( λ / 𝑛 )
𝑖 𝑖
λ
𝐶 . (1 − ρ).
λ
𝑛
𝐶𝑎𝑝𝑎𝑐𝑖𝑑𝑎𝑑 Ó𝑝𝑡𝑖𝑚𝑎 = + 𝑖 [bps]
𝑛 λ
𝑖 ∑ 𝑖
𝑛
𝑖
NOTA: Cuando decimos λ hablamos del dato que te da el ejercicio (por ejemplo 10
𝑖
msg/seg). Ahora, cuando decimos λ a secas nos referimos a la sumatoria (cant.
terminales * su respectivo λ )
𝑖
δ = sumatoria de (todas las terminales multpiclado por el número de mensaje por segundo).
denominador = cantidad total de terminales por la raíz de ( λ / 𝑛 )
𝑖 𝑖

TEORÍA DE COLAS
λ = 𝑓𝑟𝑒𝑐𝑢𝑒𝑛𝑐𝑖𝑎 𝑜 𝑣𝑒𝑙𝑜𝑐𝑖𝑑𝑎𝑑 𝑑𝑒 𝑎𝑟𝑟𝑖𝑏𝑜 𝑎𝑙 𝑠𝑖𝑠𝑡𝑒𝑚𝑎 𝑑𝑒 𝑐𝑜𝑙𝑎 [𝑐𝑙𝑖𝑒𝑛𝑡𝑒𝑠 / 𝑡𝑖𝑒𝑚𝑝𝑜]
µ = 𝑓𝑟𝑒𝑐𝑢𝑒𝑛𝑐𝑖𝑎 𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜 𝑑𝑒 𝑠𝑒𝑟𝑣𝑖𝑐𝑖𝑜 𝑝𝑜𝑟 𝑠𝑒𝑟𝑣𝑖𝑑𝑜𝑟 [𝑐𝑙𝑖𝑒𝑛𝑡𝑒𝑠 / 𝑡𝑖𝑒𝑚𝑝𝑜]
𝐸(𝑡) = 1/λ = 𝑒𝑠 𝑒𝑙 𝑖𝑛𝑡𝑒𝑟𝑣𝑎𝑙𝑜 𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜 𝑑𝑒 𝑡𝑖𝑒𝑚𝑝𝑜 𝑒𝑛𝑡𝑟𝑒 𝑎𝑟𝑟𝑖𝑏𝑜𝑠 [tiempo]
𝐸(𝑠) = 1/µ = 𝑒𝑠 𝑒𝑙 𝑡𝑖𝑒𝑚𝑝𝑜 𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜 𝑑𝑒 𝑠𝑒𝑟𝑣𝑖𝑐𝑖𝑜 𝑝𝑎𝑟𝑎 𝑢𝑛 𝑢𝑠𝑢𝑎𝑟𝑖𝑜. [tiempo]
λ/µ
ρ = = 𝑓𝑎𝑐𝑡𝑜𝑟 𝑑𝑒 𝑢𝑡𝑖𝑙𝑖𝑧𝑎𝑐𝑖ó𝑛 𝑑𝑒𝑙 𝑠𝑒𝑟𝑣𝑖𝑑𝑜𝑟
𝑐
𝑁𝑜𝑡𝑎 : ρ < 1 , pasar a %
NOTA: clientes / tiempo = clientes por segundo.
ρ ρ . 𝐸(𝑠)
𝑊 = = = 𝑇𝑖𝑒𝑚𝑝𝑜 𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜 𝑒𝑛 𝑙𝑎 𝑐𝑜𝑙𝑎 [tiempo]
𝑞 µ . (1−ρ) (1−ρ)
𝑊 = 𝑊𝑞 + 𝐸(𝑠) = 𝑇𝑖𝑒𝑚𝑝𝑜 𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜 𝑒𝑠𝑝𝑒𝑟𝑎𝑑𝑜 𝑒𝑛 𝑒𝑙 𝑠𝑖𝑠𝑡𝑒𝑚𝑎 𝑒𝑛 𝑒𝑠𝑡𝑎𝑑𝑜 𝑒𝑠𝑡𝑎𝑏𝑙𝑒 (𝑡𝑖𝑒𝑚𝑝𝑜 𝑡𝑜𝑡𝑎𝑙)
[𝑡𝑖𝑒𝑚𝑝𝑜]
𝐿 = λ .𝑊𝑞 = 𝑁ú𝑚𝑒𝑟𝑜 𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜 𝑑𝑒 𝑢𝑠𝑢𝑎𝑟𝑖𝑜𝑠 𝑒𝑛 𝑙𝑎 𝑐𝑜𝑙𝑎, 𝑠𝑖𝑛 𝑖𝑛𝑐𝑙𝑢𝑖𝑟 𝑙𝑜𝑠 𝑢𝑠𝑢𝑎𝑟𝑖𝑜𝑠 𝑟𝑒𝑐𝑖𝑏𝑖𝑒𝑛𝑑𝑜 𝑎𝑡𝑒𝑛𝑐𝑖ó𝑛
𝑞
[𝑐𝑙𝑖𝑒𝑛𝑡𝑒𝑠]
𝐿 = λ .𝑊 = 𝑛ú𝑚𝑒𝑟𝑜 𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜 𝑑𝑒 𝑢𝑠𝑢𝑎𝑟𝑖𝑜𝑠 𝑒𝑛 𝑒𝑙 𝑠𝑖𝑠𝑡𝑒𝑚𝑎 [clientes]
π = 𝑊 . 𝑙𝑛(10 . ρ) = 𝑒𝑙 90% 𝑑𝑒 𝑡𝑜𝑑𝑜𝑠 𝑙𝑜𝑠 𝑞𝑢𝑒 𝑎𝑟𝑟𝑖𝑏𝑎𝑟𝑜𝑛 𝑎 𝑙𝑎 𝑐𝑜𝑙𝑎 𝑛𝑜 𝑒𝑠𝑝𝑒𝑟𝑎𝑛 𝑚á𝑠 𝑞𝑢𝑒 𝑒𝑠𝑒 𝑡𝑖𝑒𝑚𝑝𝑜
𝑞
[𝑡𝑖𝑒𝑚𝑝𝑜]

Preguntas Multiple Choise

1- En una transmisión con Multiplexado FDM:
A. Las señales se muestran a 2x f max y ocupan todo el ancho de banda del canal
B. Las señales ocupan porciones de tiempo llamadas Time Slice
C. Las señales viajan simultáneamente y ocupan una determinada banda de frecuencia dentro
del ancho de banda del canal
D. Las señales ocupan todo el ancho de banda del canal pero no viajan simultáneamente.
2- Una Modulación en Amplitud con portadora suprimida es:
A. Una Modulación de Amplitud donde no se requiere la portadora en el proceso de modulación
B. Una modulación de Amplitud donde el espectro de la portadora se filtra con un filtro pasa
altos en el receptor
C. Una modulación de amplitud donde el espectro de la portadora no aparece después de
modular
D. Una modulación de amplitud donde el espectro de la portadora se filtra con un filtro pasa
bajos después de modular
3- Para digitalizar un mensaje analógico se debe primero:
A. Muestrear el mensaje con una portadora analógica de muy alta frecuencia
B. Muestrear el mensaje con un tren de pulsos digital con una frecuencia máxima igual a la
frecuencia máxima del mensaje.
C. Muestrear el mensaje con un tren de pulsos digital con una frecuencia mínima igual al doble
de la frecuencia máxima del mensaje.
D. Codificar el mensaje con 8 binits a la frecuencia máxima del mensaje
4- En una transmisión con multiplexado TDM las señales:
A. Se transmiten muestras de cada señal en un tiempo determinado ocupando cada muestra
una banda específica dentro del ancho de banda del canal
B. Se transmiten muestras de cada señal en un tiempo determinado ocupando todo el ancho de
banda del canal
C. Se transmiten muestras de cada señal simultáneamente con las muestras del resto de las
señales ocupando todo el ancho de banda del canal
D. Se transmiten muestras de cada señal simultáneamente con las muestras del resto de las
señales ocupando una banda especifica cada una dentro del ancho de banda del canal

5- Para aumentar la velocidad de transmisión de una FSK ó PSK sin aumentar el ancho de
banda del canal se debe:
A. Aumentar la frecuencia de la portadora
B. Aumentar el período de muestreo de la señal (frec. Muestreo>2.fmax)
C. Aumentar el número de niveles (multinivel)
D. Disminuir el tiempo de transmisión T
6- CMD significa:
A. Multiplexado por división de Ceros
B. Modulación media Cruzada
C. Modulación por Códigos
D. Multiplexado por División de Código
7- El Multiplexado WDM se aplica en:
A. Sólo en medios No Guiados
B. Sólo en Medios Guiados
C. Solo en Fibra óptica
D. En Fibra óptica y Coaxil
E. Solo por Radio Enlace
8- WDM significa:
A. Multiplexado por tiempo discreto
B. Multiplexado por Densidad de Onda
C. Multiplexado por División de Longitud de Onda
9- El Multiplexado CDM se aplica en:
A. Sólo en medios No Guiados
B. Sólo en Medios Guiados
C. Solo en Fibra óptica
D. En Fibra óptica y Coaxil
E. Solo por Par Telefónico
10- En la terminología TDMA /FDMA, etc la letra A significa:
A. Portadora Analógica – en una red Analógica con Multiplexado TDM /FDM, etc.
B. Señal Digital en una Red Analógica con Multiplexado TDM /FDM, etc.
C. Forma de acceder a la red con multiplexado TDM /FDM ,etc
D. Señal Analógica en una red digital con Multiplexado TDM /FDM, etc.

11- En una transmisión de N señales de frec mín = fmin y frec. Máx = fmax con Multiplexado
TDM modulación PCM el ancho de banda del canal dependerá de:
A. La cantidad de señales N, de 2x f min y la cantidad de dígitos totales codificación de las
muestras de la trama
B. La cantidad de Señales N, de 2x f máx y la cantidad de dígitos n de codificación de cada
muestra
C. La cantidad de Señales N, de 2x frecuencia de muestreo y la cantidad de dígitos n de
codificación de cada muestra
D. La cantidad de Señales N, de 2x frecuencia de muestreo y la cantidad de dígitos n de
codificación de cada muestra
12- Si se debe dar servicio de datos de alta velocidad en una Empresa ubicada en zona
urbana ¿qué tecnología usaría?
A. Satélite
B. Radio enlace
C. Fibra óptica
D. Par de cobre telefónico con modem HDSL
E. Laser
F. Cable Coaxil con cablemodem
13- Si se debe dar servicio de datos de baja velocidad en una Empresa ubicada en zona
suburbana y no tiene espacios físicos disponibles ¿qué tecnología usaría?
A. Satélite
B. Radio enlace
C. Fibra óptica
D. Par de cobre telefónico con modem HDSL Laser
E. Cable Coaxil con cablemodem
14- Si se debe dar servicio de datos de gran velocidad a una industria en la ruta 9 entre
Cañada de Gómez y Rosario, ¿qué tecnología usaría?
A. Satélite
B. Radio enlace
C. Fibra óptica
D. Par de cobre telefónico con modem HDSL
E. Laser
F. Cable Coaxial con cablemodem

15- Si se debe dar servicio de datos de baja velocidad en una Empresa ubicada en zona
selvática ¿qué tecnología usaría?
A. Satélite
B. Radio enlace
C. Fibra óptica
D. Par de cobre telefónico con modem HDSL
E. Laser
F. Cable Coaxil con cablemodem
16- Un estudio contable requiere acceso banda ancha para acceder a la web de la AFIP , se
encuentra en zona urbana, que medio de acceso le recomendarían:
A. Satélite
B. Radio enlace
C. Fibra óptica
D. Par de cobre telefónico con modem HDSL
E. E-Laser
F. Cable Coaxil con cablemodem
17- Si se requiere segurizar el servicio de datos de alta velocidad en una empresa ubicada en
zona urbana que tiene acceso por fibra óptica ¿qué tecnología usaría?
A. Satélite
B. Radio enlace
C. Fibra óptica
D. Par de cobre telefónico con modem HDSL
E. Laser
F. Cable Coaxil con cablemodem
18- El Punto de saturación de un Sistema de Cola se puede decir que es:
A. El punto correspondiente al número mínimo de usuarios que se pueden conectar con una
mínima interferencia mutua
B. El punto correspondiente al número máximo de usuarios que se pueden conectar con una
mínima interferencia mutua
C. El punto correspondiente al número máximo de usuarios que se pueden conectar con una
máxima interferencia mutua

19- En un sistema de colas el factor de utilización del servicio se define como:
A. Cantidad de servidores sobre la frecuencia de servicio
B. Intervalo promedio entre arribos sobre la frecuencia de arribos
C. La Intensidad de tráfico sobre la frecuencia de arribos
D. La intensidad de tráfico sobre la cantidad de servidores.
E. La frecuencia de arribos por tiempo de servicio promedio sobre la cantidad de servidores
F. Las respuestas A y C correctas
G. Las respuestas D y E Correctas
H. Las respuestas B y C Correctas
PREGUNTAS DEL PRIMER PARCIAL QUE TRANQUILAMENTE PODRÍAN ENTRAR EN EL
SEGUNDO PORQUE ESTA MATERIA ES UNA MIERDA (¿Te garcho?. Si)
ELECCIÓN DEL MEDIO DE ACCESO
1. Si se debe dar servicio de datos de mediana velocidad en una empresa ubicada en zona
suburbana disponiendo de espacio físico, ¿qué tecnología usaría?
a) Cable Coaxil con cablemódem
b) Láser
c) Par de cobre telefónico con módem HDSL
d) Fibra óptica
e) Satélite
f) Radio Enlace
2. Si se debe dar servicio de datos de alta velocidad en una gran organización ubicada en zona
urbana, ¿qué tecnología usaría?
a) Satélite
b) Radio enlace
c) Fibra óptica
d) Par de cobre telefónico con módem HDSL
e) Láser
3. Si se debe dar servicio de datos de baja velocidad en una empresa ubicada en zona urbana, ¿qué
tecnología usaría?
a) Satélite
b) Radio enlace
c) Fibra óptica
d) Par de cobre telefónica
e) Láser

4. Si se debe dar servicio de datos de gran velocidad a una industria en la ruta 9 entre Cañada de
Gómez y Rosario, ¿qué tecnología usaría?
a) Satélite
b) Radio enlace
c) Fibra óptica
d) Par de cobre telefónico con módem HDSL
e) Láser
f) Cable Coaxil con cablemódem
5. Si se debe dar servicio de datos de baja velocidad en una empresa ubicada en zona selvática,
¿qué tecnología usaría?
a) Satélite
b) Radio enlace
c) Fibra óptica
d) Par de cobre telefónico con módem HDSL
e) Láser
f) Cable Coaxil con cablemódem
6. Si se debe dar servicio de datos de baja velocidad en una empresa ubicada en zona montañosa,
¿qué tecnología usaría?
a) Satélite
b) Radio enlace
c) Fibra óptica
d) Par de cobre telefónico
e) Láser
7. Si se debe dar servicio de datos de baja velocidad en una empresa ubicada en zona suburbana,
¿qué tecnología usaría?
a) Satélite
b) Radio enlace
c) Fibra óptica
d) Par de cobre telefónico
e) Láser
8. Si se debe dar servicio de datos de baja velocidad en una empresa ubicada en zona suburbana
transitoriamente (luego se muda), ¿qué tecnología usaría?
a) Satélite
b) Radio enlace
c) Fibra óptica
d) Par de cobre telefónico
e) Láser
9. Una empresa que requiera gran ancho de banda y está en zona urbana, contrata el acceso y
transmisión de datos por Cablemódem y Cable Coaxial a la empresa de TV Cable local.

a) Verdadero
b) Falso
10. La transmisión por fibra óptica se realiza por:
a) Señales eléctricas
b) Pulsos de luz
c) a y b
d) Ninguna de las opciones
11. El ruido eléctrico, interferencias y acoplamientos eléctricos afectan a la fibra óptica:
a) Verdadero
b) Falso
12. La atenuación de las ondas de radio depende de la frecuencia y de la distancia recorrida:
a) Verdadero
b) Falso
13. Una de las ventajas de las transmisiones de microondas satelitales radica en:
a) El bajo costo del ancho de banda ofrecido por el proveedor del servicio
b) El gran ancho de banda comparándolo con la fibra
c) Poder llegar con la señal transmitida a lugares muy lejanos e inaccesibles
d) La alta velocidad de transmisión al utilizar el aire como medio
e) El bajo costo de sus componentes e instalación
14. Un satélite tiene una vida útil en órbita de aproximadamente:
a) 2 años
b) 5 años
c) Entre 5 y 8 años
d) Entre 10 y 15 años
e) 25 años
15. ¿Cuántos pelos de fibra se necesitan para transmitir y recibir señales?
a) 1 en todos los casos
b) 1 solo si es fibra multimodo
c) 1 solo si es fibra monomodo
d) 2

16. El hecho de trenzar los pares en el UTP se debe a:
a) Que se busca disminuir la interferencia entre los hilos de cada uno de los pares
b) Que así disminuye la atenuación de cada par
c) Que se busca disminuir la interferencia entre pares
d) Que de esa forma logra llegar a los 100 metros de longitud
e) Que de esa forma logra llegar a los 100 MHz de ancho de banda por par
17. Las ondas láser:
a) Tienen un haz muy estrecho (1 mm de ancho a 500 m de distancia)
b) Se pueden utilizar en una LAN con haces relativamente desenfocados
c) Utilizan emisores y receptores muy costosos
18. La comunicación por ondas infrarrojas no puede utilizarse en exteriores porque:
a) Interferirían con las ondas que rebotan en la ionosfera
b) El sol brilla con igual intensidad en el espectro infrarrojo y causaría interferencia
c) Interferirían con los enlaces de microondas
d) Ninguna de las anteriores
19. Un satélite de órbita media opera a una altura de:
a) 36.000 km
b) 10.000 km
c) 700 km
d) Ninguna de las anteriores
20. La Ley de Snell:
a) Especifica los ángulos de incidencia y reflexión de la luz dentro de la fibra óptica
b) Especifica los ángulos de incidencia y refracción de la luz dentro de la fibra óptica
c) Especifica la longitud de onda del haz de luz necesaria para que no se produzca refracción
d) Especifica la frecuencia de la onda necesaria para que no se produzca refracción
21. La transmisión por fibra óptica utiliza una longitud de onda aproximada de:
a) 4500 nm
b) 1300 nm
c) 4000 nm
d) Entre 2000 y 4000 nm
e) Ninguna de las anteriores

22. La fibra monomodo:
a) Es más económica que la multimodo por transmitir un solo haz
b) Es más económica por ser más delgada
c) Es más económica por estar contaminada con erbio
d) Se puede utilizar en distancias más grandes
e) Ninguna de las anteriores
23. El emisor en la fibra óptica se denomina:
a) Fotodiodo
b) Repetidor activo
c) Diodo emisor de luz
d) Estrella activa
e) LED láser
f) c y e son válidas
24. Las pérdidas en la fibra debido a un empalme se encuentran en el orden del:
a) 3%
b) 40%
c) 3 dB
d) 10%
25. En un satélite, cada transpondedor posee un ancho de banda disponible de:
a) 100 MHz
b) 25 MHz
c) De 25 a 50 MHz
d) De 36 a 50 MHz
e) De 50 a 100 MHz
26. Mediante torres de 100 m de altura, se pueden hacer enlaces de microondas punto a punto a una
distancia de:
a) 20 km
b) 40 km
c) 80 km
d) 150 km
e) 2 km
27. La velocidad de propagación en la fibra óptica es:
a) Mayor que en cualquier medio
b) Similar a la del par trenzado
c) Menor que en el aire
d) Igual a 300.000 km/s

28. Microondas se corresponde con una banda de frecuencias aproximadamente entre:
a) 300–3000 MHz
b) 1000–38.000 MHz
c) 300–3000 GHz
d) 20–400 GHz
29. La principal ventaja de la transmisión de microondas radica en:
a) El bajo costo del ancho de banda
b) El gran ancho de banda comparado con la fibra
c) La alta velocidad de transmisión al usar el aire
d) El bajo costo de componentes e instalación
e) Poder llegar a lugares muy lejanos
30. El desvanecimiento por trayectoria múltiple en microondas se debe a:
a) Las trayectorias de ondas AM que rebotan en la ionosfera
b) Radiaciones solares que inciden en las parábolas
c) Ondas que rebotan en la atmósfera y llegan desfasadas al receptor
d) La regeneración de la señal al rodear obstáculos climáticos
31. La tecnología VSAT significa:
a) Virtual Satellite Amplitude Transmission
b) Very Small Amplitude Terminals
c) Virtual Small Amplitude Transmission
d) Ninguna de las anteriores (significa Very Small Aperture Terminal)
32. La fibra multimodo:
a) Permite transmitir solo un haz de láser por pelo
b) Es más frágil que la monomodo
c) Tiene más atenuación por kilómetro que la monomodo
d) Requiere menos repetidores por kilómetro
33. La velocidad de propagación de una señal en el aire:
a) Es similar a la del par trenzado
b) Es menor que en la fibra óptica
c) Es igual a 200.000 km/s
d) Su retardo equivale a 3 µs/km
34. Las ondas por láser:
a) Deben tener licencia del gobierno para operar
b) Se utilizan prácticamente solo dentro de la fibra óptica
c) Son inmunes a las corrientes de convección

d) Son menos focalizadas que las de microondas
35. El cable coaxial solo se usa como medio de transmisión en redes de televisión por cable dando TV
y acceso a banda ancha a usuarios residenciales.
a) Verdadero
b) Falso
36. Un satélite de órbita baja, opera a una altura de:
a- 36.000 km sobre el plano del Ecuador
b- 72.000 km
c- 700 km aproximadamente
d- Ninguna de las anteriores
37. Verdadero o falso: banda ancha con cable coaxial, utiliza el cableado coaxial existente (50
ohms) para brindar el servicio de banda ancha:
a- Verdadero
b- Falso
38. El concepto de síndrome es:
a. El resultado de multiplicar una palabra correcta por la matriz de control de paridad
transpuesta
b. El resultado de multiplicar una palabra con error por la matriz generadora del código de
grupo
c. El resultado de multiplicar una palabra con error por la matriz de control de paridad
transpuesta.
d. El resultado de multiplicar una palabra con error por la matriz por la matriz generadora del
código de bloque.
39. Cuando un mensaje analógico modula en Amplitud una portadora analógica, la banda de
frecuencias del mensaje se encuentra:
a. En la banda base y en la banda lateral superior de la portadora
b. En la banda base y en la banda lateral inferior de la portadora
c. Solo en la banda lateral inferior de la portadora
d. En la Banda lateral superior y en la banda lateral inferior de la portadora
e. Sólo en la Banda lateral superior de la portadora
40. Si se tiene que transmitir una señal digital por una red que opera con señales analógicas se
debe:
a. Modular en amplitud, frecuencia o fase a una portadora analógica de muy baja frecuencia
b. Modular en amplitud una portadora digital de baja frecuencia

c. Modular en amplitud ó frecuencia ó fase una portadora analógica de alta frecuencia
d. Modular en frecuencia ó fase una portadora digital de alta frecuencia.
41. En una transmisión PCM las muestras de cada señal
a. Se transmiten a una velocidad igual a la frecuencia máxima del mensaje
b. Se codifican y se transmiten a una velocidad del doble de la frecuencia máxima del mensaje
c. Las muestras se transmiten a una velocidad del doble de la frecuencia máxima del mensaje
y se codifican en el receptor
42. Solo existen dos Multiplexados, por division de frecuencia y por división de tiempo
a. Verdadero
b. Falso
43. En una transmisión con multiplexado TDM:
a. Las señales modulan a portadoras de distintas frecuencias para ocupar una banda
determinada del ancho de banda del canal
b. Las señales se muestrean con una frecuencia mínima igual al doble de la frecuencia mínima
del mensaje
c. Las señales se muestrean con una frecuencia mínima igual al doble de la frecuencia
máxima del mensaje
d. Las señales se muestrean con una frecuencia mínima igual a la frecuencia máxima del
mensaje
44. En una Modulación de Amplitud Modulada
a. La información del mensaje está contenida en las variaciones de amplitud de una onda
senoidal de baja frecuencia llamada portadora
b. La información del mensaje está contenida en las variaciones de amplitud, frecuencia y fase
de una onda senoidal de muy alta frecuencia llamada portadora.
c. La información del mensaje está contenida en las variaciones de amplitud de una onda
senoidal de muy alta frecuencia llamada portadora.
d. La información está contenida en las variaciones de amplitud de un tren de pulsos
periódicos de baja frecuencia llamada portadora.
45. En la familia de errores asociadas a cada síndrome se pueden observar:
a. Sólo los errores simples de las palabras códigos asociadas a ese síndrome
b. Sólo los errores simples y dobles de las palabras códigos asociadas a ese síndrome.
c. Todos los errores de las palabras códigos asociadas a ese síndrome.
d. Sólo los errores múltiples de las palabras códigos asociadas a ese síndrome
46. Los objetivos de una codificación de línea son:
a. Sincronismo y transparencia
b. Capacidad de detección de errores
c. Baja probabilidad de errores
d. Eficiencia espectral
e. Ninguno

Respuestas Multiple Choise

En una transmisión con Multiplexado FDM:
A. Las señales se muestran a 2x f max y ocupan todo el ancho de banda del canal
B. Las señales ocupan porciones de tiempo llamadas Time Slice
C. Las señales viajan simultáneamente y ocupan una determinada banda de frecuencia
dentro del ancho de banda del canal
D. Las señales ocupan todo el ancho de banda del canal pero no viajan simultáneamente.
2- Una Modulación en Amplitud con portadora suprimida es:
A. Una Modulación de Amplitud donde no se requiere la portadora en el proceso de
modulación
B. Una modulación de Amplitud donde el espectro de la portadora se filtra con un filtro
pasa altos en el receptor
C. Una modulación de amplitud donde el espectro de la portadora no aparece después de
modular
D. Una modulación de amplitud donde el espectro de la portadora se filtra con un filtro
pasa bajos después de modular
3- Para digitalizar un mensaje analógico se debe primero:
A. Muestrear el mensaje con una portadora analógica de muy alta frecuencia
B. Muestrear el mensaje con un tren de pulsos digital con una frecuencia máxima igual a
la frecuencia máxima del mensaje.
C. Muestrear el mensaje con un tren de pulsos digital con una frecuencia mínima igual al
doble de la frecuencia máxima del mensaje.
D. Codificar el mensaje con 8 binits a la frecuencia máxima del mensaje
4- En una transmisión con multiplexado TDM las señales:
A. Se transmiten muestras de cada señal en un tiempo determinado ocupando cada
muestra una banda específica dentro del ancho de banda del canal
B. Se transmiten muestras de cada señal en un tiempo determinado ocupando todo el
ancho de banda del canal
C. Se transmiten muestras de cada señal simultáneamente con las muestras del resto de
las señales ocupando todo el ancho de banda del canal
D. Se transmiten muestras de cada señal simultáneamente con las muestras del resto de
las señales ocupando una banda especifica cada una dentro del ancho de banda del canaL
5- Para aumentar la velocidad de transmisión de una FSK ó PSK sin aumentar el ancho
de banda del canal se debe:
A. Aumentar la frecuencia de la portadora
B. Aumentar el período de muestreo de la señal (frec. Muestreo>2.fmax)
C. Aumentar el número de niveles (multinivel)
D. Disminuir el tiempo de transmisión T

6- CMD significa:
A. Multiplexado por división de Ceros
B. Modulación media Cruzada
C. Modulación por Códigos
D. Multiplexado por División de Código
7- El Multiplexado WDM se aplica en:
A. Sólo en medios No Guiados
B. Sólo en Medios Guiados
C. Solo en Fibra óptica
D. En Fibra óptica y Coaxil
E. Solo por Radio Enlace
8- WDM significa:
A. Multiplexado por tiempo discreto
B. Multiplexado por Densidad de Onda
C. Multiplexado por División de Longitud de Onda
9- El Multiplexado CDM se aplica en:
A. Sólo en medios No Guiados Apunte: Microsoft Word - MULTIPLEXADOS CDM Y WDM-V03)
B. Sólo en Medios Guiados
C. Solo en Fibra óptica
D. En Fibra óptica y Coaxil
E. Solo por Par Telefónico
10- En la terminología TDMA /FDMA, etc la letra A significa:
A. Portadora Analógica – en una red Analógica con Multiplexado TDM /FDM, etc.
B. Señal Digital en una Red Analógica con Multiplexado TDM /FDM, etc.
C. Forma de acceder a la red con multiplexado TDM /FDM ,etc
D. Señal Analógica en una red digital con Multiplexado TDM /FDM, etc.

11- En una transmisión de N señales de frec mín = fmin y frec. Máx = fmax con
Multiplexado TDM modulación PCM en ancho de banda del canal dependerá de:
A. La cantidad de señales N, de 2x f min y la cantidad de dígitos totales codificación de las
muestras de la trama
B. La cantidad de Señales N, de 2x f máx y la cantidad de dígitos n de codificación de
cada muestra
C. La cantidad de Señales N, de 2x frecuencia de muestreo y la cantidad de dígitos n de
codificación de cada muestra
D. La cantidad de Señales N, de 2x frecuencia de muestreo y la cantidad de dígitos n de
codificación de cada muestra
12- Si se debe dar servicio de datos de alta velocidad en una Empresa ubicada en zona
urbana ¿qué tecnología usaría?
A. Satélite
B. Radio enlace
C. Fibra óptica
D. Par de cobre telefónico con modem HDSL
E. Laser
F. Cable Coaxil con cablemodem
13- Si se debe dar servicio de datos de baja velocidad en una Empresa ubicada en zona
suburbana y no tiene espacios físicos disponibles ¿qué tecnología usaría?
A. Satélite
B. Radio enlace
C. Fibra óptica
D. Par de cobre telefónico con modem HDSL Láser ( )
esta también puede ser, por el espacio físico,chat te dice esta
E. Cable Coaxil con cablemodem
14- Si se debe dar servicio de datos de gran velocidad a una industria en la ruta 9 entre
Cañada de Gómez y Rosario, ¿qué tecnología usaría?
A. Satélite
B. Radio enlace
C. Fibra óptica
D. Par de cobre telefónico con modem HDSL
E. Laser
F. Cable Coaxial con cablemodem

15- Si se debe dar servicio de datos de baja velocidad en una Empresa ubicada en zona
selvática ¿qué tecnología usaría?
A. Satélite
B. Radio enlace
C. Fibra óptica
D. Par de cobre telefónico con modem HDSL
E. Laser
F. Cable Coaxil con cablemodem
16- Un estudio contable requiere acceso banda ancha para acceder a la web de la AFIP ,
se encuentra en zona urbana, que medio de acceso le recomendarían:
A. Satélite
B. Radio enlace
C. Fibra óptica
D. Par de cobre telefónico con modem HDSL
E. E-Laser
F. Cable Coaxil con cablemodem
17- Si se requiere segurizar el servicio de datos de alta velocidad en una empresa
ubicada en zona urbana que tiene acceso por fibra óptica ¿qué tecnología usaría?
A. Satélite
B. Radio enlace
C. Fibra óptica
D. Par de cobre telefónico con modem HDSL
E. Laser
F. Cable Coaxil con cablemodem
18- El Punto de saturación de un Sistema de Cola se puede decir que es:
A. El punto correspondiente al número mínimo de usuarios que se pueden conectar con
una mínima interferencia mutua
B. El punto correspondiente al número máximo de usuarios que se pueden conectar con
una mínima interferencia mutua (Soy Luca, para mi es este. Soy Genaro y opino igual que el
boludo que escribió primero. Soy Facundo y coincido con los otros mamertos así que la
cambio. Soy Alan y mientras lees esto, seguramente me esté pajeando. Bsos!
C. El punto correspondiente al número máximo de usuarios que se pueden conectar con
una máxima interferencia mutua ( opción marcada originalmente )

19- En un sistema de colas el factor de utilización del servicio se define como:
A. Cantidad de servidores sobre la frecuencia de servicio
B. Intervalo promedio entre arribos sobre la frecuencia de arribos
C. La Intensidad de tráfico sobre la frecuencia de arribos
D. La intensidad de tráfico sobre la cantidad de servidores.
E. La frecuencia de arribos por tiempo de servicio promedio sobre la cantidad de
servidores
F. Las respuestas A y C correctas
G. Las respuestas D y E Correctas (Para Luca (chad) y Genaro (virgin) es esta
H. Las respuestas B y C Correctas
RESPUESTAS A LAS PREGUNTAS DEL PRIMER PARCIAL QUE TRANQUILAMENTE PODRÍAN
ENTRAR EN EL SEGUNDO PORQUE ESTA MATERIA ES UNA MIERDA
ELECCIÓN DEL MEDIO DE ACCESO
1. Si se debe dar servicio de datos de mediana velocidad en una empresa ubicada en zona
suburbana disponiendo de espacio físico, ¿qué tecnología usaría?
a) Cable Coaxil con cablemódem
b) Láser
c) Par de cobre telefónico con módem HDSL
d) Fibra óptica
e) Satélite
f) Radio Enlace
2. Si se debe dar servicio de datos de alta velocidad en una gran organización ubicada en
zona urbana, ¿qué tecnología usaría?
a) Satélite
b) Radio enlace
c) Fibra óptica
d) Par de cobre telefónico con módem HDSL
e) Láser
3. Si se debe dar servicio de datos de baja velocidad en una empresa ubicada en zona
urbana, ¿qué tecnología usaría?
a) Satélite
b) Radio enlace
c) Fibra óptica
d) Par de cobre telefónica
e) Láser

4. Si se debe dar servicio de datos de gran velocidad a una industria en la ruta 9 entre
Cañada de Gómez y Rosario, ¿qué tecnología usaría?
a) Satélite
b) Radio enlace
c) Fibra óptica
d) Par de cobre telefónico con módem HDSL
e) Láser
f) Cable Coaxil con cablemódem
5. Si se debe dar servicio de datos de baja velocidad en una empresa ubicada en zona
selvática, ¿qué tecnología usaría?
a) Satélite
b) Radio enlace
c) Fibra óptica
d) Par de cobre telefónico con módem HDSL
e) Láser
f) Cable Coaxil con cablemódem
6. Si se debe dar servicio de datos de baja velocidad en una empresa ubicada en zona
montañosa, ¿qué tecnología usaría?
a) Satélite
b) Radio enlace
c) Fibra óptica
d) Par de cobre telefónico
e) Láser
7. Si se debe dar servicio de datos de baja velocidad en una empresa ubicada en zona
suburbana, ¿qué tecnología usaría?
a) Satélite
b) Radio enlace
c) Fibra óptica
d) Par de cobre telefónico
e) Láser

8. Si se debe dar servicio de datos de baja velocidad en una empresa ubicada en zona
suburbana transitoriamente (luego se muda), ¿qué tecnología usaría?
a) Satélite
b) Radio enlace
c) Fibra óptica
d) Par de cobre telefónico
e) Láser
9. Una empresa que requiera gran ancho de banda y está en zona urbana, contrata el
acceso y transmisión de datos por Cablemódem y Cable Coaxial a la empresa de TV
Cable local.
a) Verdadero
b) Falso
10. La transmisión por fibra óptica se realiza por:
a) Señales eléctricas
b) Pulsos de luz
c) a y b
d) Ninguna de las opciones
11. El ruido eléctrico, interferencias y acoplamientos eléctricos afectan a la fibra óptica:
a) Verdadero
b) Falso
12. La atenuación de las ondas de radio depende de la frecuencia y de la distancia
recorrida:
a) Verdadero
b) Falso
13. Una de las ventajas de las transmisiones de microondas satelitales radica en:
a) El bajo costo del ancho de banda ofrecido por el proveedor del servicio
b) El gran ancho de banda comparándolo con la fibra
c) Poder llegar con la señal transmitida a lugares muy lejanos e inaccesibles
d) La alta velocidad de transmisión al utilizar el aire como medio

e) El bajo costo de sus componentes e instalación
14. Un satélite tiene una vida útil en órbita de aproximadamente:
a) 2 años
b) 5 años
c) Entre 5 y 8 años
d) Entre 10 y 15 años
e) 25 años
15. ¿Cuántos pelos de fibra se necesitan para transmitir y recibir señales?
a) 1 en todos los casos
b) 1 solo si es fibra multimodo
c) 1 solo si es fibra monomodo
d) 2
16. El hecho de trenzar los pares en el UTP se debe a:
a) Que se busca disminuir la interferencia entre los hilos de cada uno de los pares
b) Que así disminuye la atenuación de cada par
c) Que se busca disminuir la interferencia entre pares
d) Que de esa forma logró llegar a los 100 metros de longitud
e) Que de esa forma logró llegar a los 100 MHz de ancho de banda por par
17. Las ondas láser:
a) Tienen un haz muy estrecho (1 mm de ancho a 500 m de distancia)
b) Se pueden utilizar en una LAN con haces relativamente desenfocados
c) Utilizan emisores y receptores muy costosos
(Segun Claudio IA son los 3)
18. La comunicación por ondas infrarrojas no puede utilizarse en exteriores porque:
a) Interferirían con las ondas que rebotan en la ionosfera
b) El sol brilla con igual intensidad en el espectro infrarrojo y causaría interferencia en ellas
c) Interferirían con los enlaces de microondas
d) Ninguna de las anteriores

19. Un satélite de órbita media opera a una altura de:
a) 36.000 km (órbita alta)
b) 10.000 km
c) 700 km (órbita baja)
d) Ninguna de las anteriores
20. La Ley de Snell:
a) Especifica los ángulos de incidencia y reflexión de la luz dentro de la fibra óptica
b) Especifica los ángulos de incidencia y refracción de la luz dentro de la fibra óptica
c) Especifica la longitud de onda del haz de luz necesaria para que no se produzca refracción
d) Especifica la frecuencia de la onda necesaria para que no se produzca refracción
21. La transmisión por fibra óptica utiliza una longitud de onda aproximada de:
a) 4500 nm
b) 1300 nm
c) 4000 nm
d) Entre 2000 y 4000 nm
e) Ninguna de las anteriores
22. La fibra monomodo:
a) Es más económica que la multimodo por transmitir un solo haz
b) Es más económica por ser más delgada
c) Es más económica por estar contaminada con erbio
d) Se puede utilizar en distancias más grandes
e) Ninguna de las anteriores
(según claudio IA es la d)(yo doctorculo digo lo mismo que claudio)
23. El emisor en la fibra óptica se denomina:
a) Fotodiodo
b) Repetidor activo
c) Diodo emisor de luz
d) Estrella activa
e) LED láser
f) c y e son válidas

24. Las pérdidas en la fibra debido a un empalme se encuentran en el orden del:
a) 3%
b) 40%
c) 3 dB
d) 10%
25. En un satélite, cada transpondedor posee un ancho de banda disponible de:
a) 100 MHz
b) 25 MHz
c) De 25 a 50 MHz
d) De 36 a 50 MHz
e) De 50 a 100 MHz
26. Mediante torres de 100 m de altura, se pueden hacer enlaces de microondas punto a
punto a una distancia de:
a) 20 km
b) 40 km
c) 80 km
d) 150 km
e) 2 km
27. La velocidad de propagación en la fibra óptica es:
a) Mayor que en cualquier medio
b) Similar a la del par trenzado
c) Menor que en el aire
d) Igual a 300.000 km/s
28. Microondas se corresponde con una banda de frecuencias aproximadamente entre:
a) 300–3000 MHz
b) 1000–38.000 MHz
c) 300–3000 GHz
d) 20–400 GHz
29. La principal ventaja de la transmisión de microondas radica en:
a) El bajo costo del ancho de banda
b) El gran ancho de banda comparado con la fibra
c) La alta velocidad de transmisión al usar el aire
d) El bajo costo de componentes e instalación
e) Poder llegar a lugares muy lejanos
(segun claudio IA es la e)

30. El desvanecimiento por trayectoria múltiple en microondas se debe a:
a) Las trayectorias de las ondas de AM que rebotan en la ionosfera
b) Radiaciones solares que inciden en las parábolas receptoras de los enlaces de
microondas, causando interferencia
c) Ondas emitidas en un radioenlace terrestre, que luego de rebotar en la atmósfera llegan al
receptor y causan interferencias
d) La regeneración de la señal del microondas, cuando se hace un “rodeo” para evitar
situaciones climáticas adversas
31. La tecnología VSAT significa:
a) Virtual Satellite Amplitude Transmission
b) Very Small Amplitude Terminals
c) Virtual Small Amplitude Transmission
d) Ninguna de las anteriores (significa Very Small Aperture Terminal)
32. La fibra multimodo:
a) Permite transmitir solo un haz de láser por pelo
b) Es más frágil que la monomodo
c) Tiene más atenuación por kilómetro que la monomodo
d) Requiere menos repetidores por kilómetro
33. La velocidad de propagación de una señal en el aire:
a) Es similar a la del par trenzado
b) Es menor que en la fibra óptica
c) Es igual a 200.000 km/s
d) Es tal que su retardo equivale a 3 microsegundo / km
34. Las ondas por láser:
a) Deben tener licencia del gobierno para operar
b) Prácticamente se utilizan sólo para transmitir dentro de la fibra óptica
c) Son inmunes a las corrientes de convección
d) Son menos focalizadas que las de microondas
35. El cable coaxial solo se usa como medio de transmisión en redes de televisión por
cable dando TV y acceso a banda ancha a usuarios residenciales.
a) Verdadero
b) Falso

36. Un satélite de órbita baja, opera a una altura de:
a- 36.000 km sobre el plano del Ecuador
b- 72.000 km
c- 700 km aproximadamente
d- Ninguna de las anteriores
37. Verdadero o falso: banda ancha con cable coaxial, utiliza el cableado coaxial existente
(50 ohms) para brindar el servicio de banda ancha:
a- Verdadero
b- Falso
38. El concepto de síndrome es:
a. El resultado de multiplicar una palabra correcta por la matriz de control de paridad
transpuesta
b. El resultado de multiplicar una palabra con error por la matriz generadora del código de
grupo
c. El resultado de multiplicar una palabra con error por la matriz de control de paridad
transpuesta.
d. El resultado de multiplicar una palabra con error por la matriz por la matriz generadora
del código de bloque.
39. Cuando un mensaje analógico modula en Amplitud la una portadora analógica la banda
de frecuencias del mensaje se encuentra:
a. En la banda base y en la banda lateral superior de la portadora
b. En la banda base y en la banda lateral inferior de la portadora
c. Solo en la banda lateral inferior de la portadora
d. En la Banda lateral superior y en la banda lateral inferior de la portadora
e. Sólo en la Banda lateral superior de la portadora
40. Si se tiene que transmitir una señal digital por una red que opera con señales
analógicas se debe:
a. Modular en amplitud, frecuencia o fase a una portadora analógica de muy baja
frecuencia
b. Modular en amplitud una portadora digital de baja frecuencia
c. Modular en amplitud o frecuencia o fase una portadora analógica de alta frecuencia
d. Modular en frecuencia o fase una portadora digital de alta frecuencia.
41. En una transmisión PCM las muestras de cada señal
a. Se transmiten a una velocidad igual a la frecuencia máxima del mensaje
b. Se codifican y se transmiten a una velocidad del doble de la frecuencia máxima del
mensaje

c. Las muestras se transmiten a una velocidad del doble de la frecuencia máxima del
mensaje y se codifican en el receptor
(Según Claudio IA es la B)
42. Solo existen dos Multiplexados, por división de frecuencia y por división de tiempo
a. Verdadero
b. Falso
43. En una transmisión con multiplexado TDM:
a. Las señales modulan a portadoras de distintas frecuencias para ocupar una banda
determinada del ancho de banda del canal
b. Las señales se muestrean con una frecuencia mínima igual al doble de la frecuencia
mínima del mensaje
c. Las señales se muestrean con una frecuencia mínima igual al doble de la frecuencia
máxima del mensaje
d. Las señales se muestrean con una frecuencia mínima igual a la frecuencia máxima del
mensaje
44. En una Modulación de Amplitud Modulada
a. La información del mensaje está contenida en las variaciones de amplitud de una onda
senoidal de baja frecuencia llamada portadora
b. La información del mensaje está contenida en las variaciones de amplitud, frecuencia y
fase de una onda senoidal de muy alta frecuencia llamada portadora.
c. La información del mensaje está contenida en las variaciones de amplitud de una onda
senoidal de muy alta frecuencia llamada portadora.
d. La información está contenida en las variaciones de amplitud de un tren de pulsos
periódicos de baja frecuencia llamada portadora.
45. En la familia de errores asociadas a cada síndrome se pueden observar:
a. Sólo los errores simples de las palabras códigos asociadas a ese síndrome
b. Sólo los errores simples y dobles de las palabras códigos asociadas a ese síndrome.
c. Todos los errores de las palabras códigos asociadas a ese síndrome.
d. Sólo los errores múltiples de las palabras códigos asociadas a ese síndrome
46. Los objetivos de una codificación de línea son:
a. Sincronismo y transparencia
b. Capacidad de detección de errores
c. Baja probabilidad de errores
d. Eficiencia espectral
e. Ninguno
Pregunta muy repetida por Campanaro:

Dado un Código de Grupo, los errores que NO se detectan:
1. son aquellos que coinciden con sus palabras códigos o sea donde hay unos en las palabras
códigos.
“Los errores que NO se detectan son aquellos que coinciden con sus palabras códigos o sea donde
hay unos en las palabras códigos.”
Resumen codigos de linea