# Redes de Datos — Simulacro Multiple Choice (Enlace + Red)

> **48 preguntas** difíciles (distractores muy parecidos), generadas y verificadas desde tu wiki. Solo entra **Capa de Enlace + Capa de Red**.
>
> **Cómo hacerlo:** respondé sin mirar las respuestas (están en `simulacro-respuestas.md`). Anotá tus respuestas (ej. `1-b, 2-c, 3-a…`) y me las pasás para corregir. Podés ir por tandas.

**1.** El campo Differentiated Services del encabezamiento IPv4 ocupa 1 byte. Segun la wiki, ¿como se reparte internamente?
- a) 2 bits de clase de servicio (QoS) + 6 bits de notificacion de congestion (ECN)
- b) 8 bits enteros de clase de servicio (QoS), sin bits reservados a congestion
- c) 6 bits de clase de servicio (QoS) + 2 bits de notificacion de congestion (ECN)
- d) 6 bits de notificacion de congestion (ECN) + 2 bits de clase de servicio (QoS)

**2.** ¿Por que motivo el Header Checksum del IPv4 debe recalcularse en cada router del camino?
- a) Porque el TTL se decrementa en cada salto, lo que altera el contenido del header
- b) Porque el Fragment Offset se modifica en cada router por el que pasa el paquete
- c) Porque la direccion de destino se reescribe en cada salto hasta llegar al host final
- d) Porque el campo Identification se renueva en cada router para rearmar la secuencia

**3.** Segun la wiki, ¿cual afirmacion sobre el campo TTL del header IPv4 es correcta?
- a) Ocupa 16 bits y su maximo es 65.535 saltos
- b) Se incrementa en 1 en cada router y, al alcanzar 255, el paquete se descarta
- c) Al llegar a 0 el router reenvia el paquete igual, pero sin avisar al origen
- d) Se decrementa en 1 por router, su maximo son 255 saltos, y al llegar a 0 se descarta (evita loops)

**4.** ¿Cual es la descripcion correcta del campo IHL (largo de header) del IPv4?
- a) Ocupa 4 bits; un valor de 5 indica 60 bytes de header y un valor de 15 indica 20 bytes
- b) Ocupa 4 bits; un valor de 5 indica 20 bytes (minimo) y un valor de 15 indica 60 bytes (maximo)
- c) Ocupa 8 bits e indica el largo total del paquete incluyendo los datos
- d) Ocupa 4 bits; un valor de 5 indica 20 bits y un valor de 15 indica 60 bits

**5.** Sobre los bits de fragmentacion (DF y MF) del header IPv4, ¿cual afirmacion es correcta segun la wiki?
- a) MF vale 1 mientras falten fragmentos y 0 en el ultimo; DF en 1 significa 'no fragmentar'
- b) MF vale 0 mientras falten fragmentos y 1 en el ultimo; DF en 1 significa 'no fragmentar'
- c) MF vale 1 solo en el ultimo fragmento; DF en 1 obliga a fragmentar el paquete
- d) DF en 1 significa que faltan mas fragmentos, y MF en 1 significa 'no fragmentar'

**6.** ¿Cual de las siguientes afirmaciones sobre los campos del header IPv4 es correcta segun la wiki?
- a) El campo Total Length ocupa 2 bytes y su valor maximo es 8.191 bytes
- b) El campo Identification indica el protocolo de capa 4 utilizado (TCP o UDP)
- c) El campo Protocol indica el numero de fragmento para rearmar la secuencia en el receptor
- d) El campo Total Length ocupa 2 bytes y su valor maximo es 65.535 (2¹⁶−1) bytes

**7.** Según la wiki, ¿cómo procede el algoritmo del paso más corto (Dijkstra, 1959) para hallar la ruta óptima?
- a) Elige sucesivamente los nodos de menor distancia total al origen, asignando distancia cero a los nodos aún no explorados.
- b) Elige sucesivamente los nodos de menor distancia total al origen, asignando distancia infinita a los nodos aún no explorados.
- c) Elige sucesivamente los nodos de menor distancia total al destino, asignando distancia infinita a los nodos aún no explorados.
- d) Elige sucesivamente los nodos de mayor distancia total al origen, asignando distancia infinita a los nodos aún no explorados.

**8.** En el ruteo por Vector Distancia (Bellman-Ford / RIP), ¿qué describe correctamente el problema de la 'cuenta a infinito' y su mitigación?
- a) Las buenas noticias se propagan lentamente y las malas rápido; se mitiga fijando un 'infinito' alto.
- b) Las malas noticias se propagan lentamente sumando saltos; se mitiga aumentando la memoria de cada router.
- c) Las malas noticias se propagan lentamente sumando saltos; se resuelve enviando el estado del enlace a toda la red por flooding.
- d) Las malas noticias (una caída) se propagan lentamente sumando saltos y las buenas rápido; se mitiga fijando un 'infinito' bajo (máx. saltos + 1).

**9.** Comparado con Vector Distancia, ¿qué afirma la wiki sobre el ruteo por Estado de Enlaces (Link State)?
- a) Consume más memoria y procesamiento, pero converge más rápido; hoy lo usan IS-IS y OSPF.
- b) Consume menos memoria y procesamiento, pero converge más rápido; hoy lo usan IS-IS y OSPF.
- c) Consume más memoria y procesamiento, pero converge más lento; hoy lo usan IS-IS y OSPF.
- d) Consume más memoria y procesamiento y converge más rápido; hoy lo usan RIP y OSPF.

**10.** Sobre el ruteo jerárquico por regiones (Kamoun & Kleinrock, 1979), ¿qué afirma la wiki?
- a) Cada router conoce solo su región, lo que achica las tablas y además acorta los caminos; niveles óptimos = Ln(N).
- b) Cada router conoce toda la red, lo que achica las tablas a costa de caminos más largos; niveles óptimos = Ln(N).
- c) Cada router conoce solo su región, lo que achica las tablas a costa de caminos algo más largos; niveles óptimos = Ln(N), con e·Ln(N) entradas por router.
- d) Cada router conoce solo su región, lo que achica las tablas a costa de caminos más largos; niveles óptimos = e·Ln(N), con Ln(N) entradas por router.

**11.** Para un usuario móvil, ¿cómo llega el tráfico al dispositivo cuando está en una red visitada?
- a) El móvil obtiene una Care-of-Address en su red de origen (Home Location) y el Home Agent le reenvía el tráfico por un túnel.
- b) El móvil obtiene una Care-of-Address en la red visitada y el Home Agent le reenvía el tráfico mediante un túnel (tunneling).
- c) El Home Agent obtiene una Care-of-Address en la red visitada y el móvil le reenvía el tráfico por un túnel.
- d) El móvil obtiene una Care-of-Address en la red visitada y el Home Agent le reenvía el tráfico por flooding con nº de secuencia.

**12.** ¿Qué caracteriza a las redes ad-hoc (MANETs) según la wiki?
- a) Los nodos actúan también como routers y el descubrimiento de ruta se hace por flooding con nº de secuencia; algoritmos como DSR, AODV y GPSR (geográfico).
- b) Los nodos actúan también como routers y el descubrimiento de ruta se hace por flooding con nº de secuencia; algoritmos como DSR, AODV y RIP.
- c) Existe un router raíz fijo por red y el descubrimiento de ruta se hace por flooding con nº de secuencia; algoritmos como DSR, AODV y GPSR.
- d) Los nodos actúan también como routers, pero el descubrimiento de ruta usa Vector Distancia sin nº de secuencia; algoritmos como DSR, AODV y GPSR.

**13.** Se aplica un AND bit a bit entre una dirección IP y su máscara de subred. ¿Qué se obtiene como resultado?
- a) La parte de host de la dirección.
- b) El prefijo de red al que pertenece la dirección.
- c) La dirección de broadcast de la red.
- d) La cantidad de bits del prefijo, es decir el valor N de la notación /N.

**14.** En la dirección 128.208.2.0/24, ¿qué indica correctamente el /24?
- a) 24 bits identifican la red (prefijo) y 8 bits identifican al host.
- b) 24 bits identifican al host y 8 bits identifican la red.
- c) 24 bits identifican la red y otros 24 al host, sumando 48 bits en total.
- d) La red admite exactamente 24 subredes posibles.

**15.** Respecto del direccionamiento por clases (vigente hasta 1993) según la wiki, ¿cuál afirmación es correcta?
- a) La clase C está reservada a multicast y la clase D a uso futuro.
- b) En el esquema de clases el prefijo es de longitud variable según cada red.
- c) La clase A tiene prefijo de 14 bits y admite 16.384 redes.
- d) La clase D está reservada a multicast y la clase E a uso futuro, con prefijo fijo por clase.

**16.** ¿Qué permite CIDR (Classless InterDomain Routing) según la wiki?
- a) Fijar un prefijo de longitud fija determinado por la clase de la dirección.
- b) Dividir una red en subredes más chicas asignando un puerto distinto a cada host.
- c) Agrupar varios prefijos en una superred (route aggregation), dejando una sola entrada en la tabla del router para muchas subredes.
- d) Traducir direcciones privadas en una pública distinguiéndolas por el puerto.

**17.** ¿Cuál de estas correspondencias de direcciones especiales es la correcta según la wiki?
- a) 0.0.0.0 = broadcast local; 255.255.255.255 = loopback; 127.x.x.x = booteo/propia red.
- b) 0.0.0.0 = booteo/propia red; 255.255.255.255 = broadcast local; 127.x.x.x = loopback.
- c) 0.0.0.0 = loopback; 255.255.255.255 = booteo/propia red; 127.x.x.x = broadcast local.
- d) 0.0.0.0 = booteo/propia red; 255.255.255.255 = loopback; 127.x.x.x = broadcast local.

**18.** ¿Cuál afirmación es correcta respecto de las direcciones privadas y su uso en NAT, según la wiki?
- a) Los rangos privados son 10.0.0.0/8, 172.16.0.0/16 y 192.168.0.0/12, y las máquinas internas se distinguen por su dirección MAC.
- b) NAT traduce una IP pública en varias privadas, distinguiéndolas por el TTL del paquete.
- c) Los rangos privados son 10.0.0.0/8, 172.16.0.0/12 y 192.168.0.0/16, y las máquinas internas se distinguen por su número de puerto.
- d) Las direcciones privadas son únicas en todo Internet; por eso las asigna ICANN a cada host individual.

**19.** ¿Qué funciones cumple la capa de enlace y con qué capas se relaciona en cuanto a servicio?
- a) Control de errores y control de flujo; usa el servicio de la capa física y le brinda uno nuevo a la capa de red.
- b) Control de errores y control de flujo; usa el servicio de la capa de red y le brinda uno nuevo a la capa física.
- c) Control de congestión y control de flujo; usa el servicio de la capa física y le brinda uno nuevo a la capa de red.
- d) Control de errores y control de congestión; usa el servicio de la capa física y le brinda uno nuevo a la capa de transporte.

**20.** En la estructura de la trama (header / datos / trailer), ¿qué función principal cumple cada extremo?
- a) El header lleva principalmente el control de errores; el trailer marca dónde empieza la trama y las direcciones.
- b) El header marca dónde empieza la trama y lleva las direcciones; el trailer lleva el número de secuencia para el control de flujo.
- c) El header marca dónde empieza la trama y lleva las direcciones origen/destino; el trailer (bits de cola) sirve principalmente para control de errores.
- d) El header lleva las direcciones origen/destino y el número de secuencia; el trailer marca el comienzo de la trama.

**21.** Sobre el método de framing 'contar bytes de trama', ¿cuál es su problema y por qué no se usa en la práctica?
- a) Si un byte de datos coincide con el flag se pierde el sincronismo; por eso se combina con byte-stuffing.
- b) Consume demasiados bits de relleno por trama y baja la eficiencia; por eso se reemplazó por el flag de comienzo.
- c) Si el trailer llega con error se pierde el conteo y no se puede re-sincronizar; por eso casi no se usa.
- d) Si el header llega con error se pierde el sincronismo y cuesta re-sincronizar la cadena de tramas; por eso no se usa en la práctica.

**22.** ¿Cuál asociación entre técnica de framing con flag y protocolo es correcta?
- a) Byte-stuffing (intercala bits de relleno) → PPP; bit-stuffing (antepone un byte ESC) → HDLC y USB.
- b) Byte-stuffing (antepone un byte ESC al flag accidental) → PPP; bit-stuffing (intercala bits de relleno) → HDLC y USB.
- c) Byte-stuffing (antepone un byte ESC) → HDLC; bit-stuffing (intercala bits de relleno) → PPP y USB.
- d) Byte-stuffing (antepone un byte ESC) → PPP y USB; bit-stuffing (intercala bits de relleno) → HDLC.

**23.** En HDLC, ¿cuál es el flag y cuándo inserta el emisor un bit de relleno (bit-stuffing)?
- a) El flag es 01111110; cuando el emisor detecta un 0 seguido de seis 1 en los datos, inserta un 0.
- b) El flag es 01111110; cuando el emisor detecta un 0 seguido de cinco 1 en los datos, inserta un 1 para romper el flag.
- c) El flag es 01111110; cuando el emisor detecta un 0 seguido de cinco 1 en los datos, inserta un 0 para romper el flag.
- d) El flag es 01111100; cuando el emisor detecta un 0 seguido de cinco 1 en los datos, inserta un 0.

**24.** Sobre el framing por violación de codificación 4B/5B, ¿cuál afirmación es correcta?
- a) En 4B/5B hay palabras de 5 bits no usadas; una de ellas marca inicio/fin de trama; lo usan FDDI y Fast-Ethernet.
- b) En 4B/5B hay palabras de 5 bits no usadas; una de ellas marca inicio/fin de trama; lo usan FDDI y WiFi (802.11).
- c) En 4B/5B se usan palabras de 4 bits no usadas para marcar inicio/fin de trama; lo usan FDDI y Fast-Ethernet.
- d) En 4B/5B hay palabras de 5 bits no usadas; una de ellas marca inicio/fin de trama; lo usan PPP y HDLC.

**25.** Según la Unidad 2 (Control de Congestión), agregar más memoria (buffers) a los routers para combatir la congestión:
- a) Ayuda, porque con buffers más grandes los paquetes ya no se pierden y no hace falta retransmitir.
- b) No ayuda; con memoria infinita el problema se mantiene exactamente igual (Nagle, 1987).
- c) Ayuda, pero solo en la capa 4, no en la capa 3 (Nagle, 1987).
- d) No ayuda; incluso con memoria infinita el problema empeora (Nagle, 1987).

**26.** ¿Como distingue la wiki el control de flujo del control de congestion?
- a) El control de flujo involucra muchos nodos; la congestion es entre un solo emisor y un solo receptor.
- b) Ambos involucran muchos nodos, pero el flujo actua en capa 2 y la congestion en capa 3.
- c) El control de flujo es entre un emisor y un receptor; la congestion involucra muchos nodos.
- d) El control de flujo es entre un emisor y un receptor; la congestion tambien, pero medida de extremo a extremo.

**27.** ¿Cual es el orden correcto de las 5 etapas de control de congestion?
- a) Provisioning -> Admission Control -> Traffic-Aware Routing -> Traffic Throttling -> Load Shedding
- b) Provisioning -> Traffic-Aware Routing -> Admission Control -> Traffic Throttling -> Load Shedding
- c) Provisioning -> Traffic-Aware Routing -> Admission Control -> Load Shedding -> Traffic Throttling
- d) Traffic-Aware Routing -> Provisioning -> Admission Control -> Traffic Throttling -> Load Shedding

**28.** Sobre las 3 tecnicas de atenuacion de fuentes (traffic throttling), ¿cual afirmacion es correcta?
- a) El ECN (paquete 'choke'): el router marca el paquete y el receptor avisa a la fuente; no carga a los routers pero es mas lento (extremo a extremo).
- b) El ECN (paquete 'choke'): el router avisa directamente al emisor; carga a los routers pero es la tecnica mas rapida.
- c) El hop-by-hop backpressure: cada router avisa hacia atras al anterior; es la mas lenta pero no carga a los routers.
- d) El aviso al emisor con paquete 'tagged' es la tecnica mas rapida y la que menos carga a los routers.

**29.** En load shedding (descarte de paquetes), ¿que conviene descartar primero segun el tipo de trafico?
- a) En transferencia de archivos, los paquetes mas viejos; en streaming, los mas nuevos.
- b) En cualquier caso, siempre los paquetes de control antes que los de datos.
- c) En transferencia de archivos, los ultimos paquetes; en streaming, los mas nuevos.
- d) En transferencia de archivos, los ultimos paquetes; en streaming, los mas viejos.

**30.** ¿Como actua el algoritmo RED (Random Early Detection) usado en load shedding?
- a) Descarta paquetes de forma aleatoria recien cuando la cola se lleno por completo (Nagle, 1987).
- b) Descarta paquetes segun el promedio de la cola, antes de que esta se llene (Floyd & Jacobson, 1993).
- c) Descarta paquetes segun el promedio de la cola, pero solo una vez que la cola esta totalmente llena (Floyd & Jacobson, 1993).
- d) Descarta primero los paquetes de control segun el promedio de la cola (Floyd & Jacobson, 1993).

**31.** Según la wiki, ¿cuál de estas afirmaciones sobre los mensajes ICMP es correcta?
- a) El mensaje "Eco" es el que usa traceroute, que envía TTL=1, 2, 3… y recibe el ICMP de cada router del camino.
- b) El mensaje "Tiempo excedido" es el que usa ping para saber si un host está vivo, respondiendo "echo reply".
- c) El mensaje "Tiempo excedido" (TTL a 0) es el que usa traceroute, que envía TTL=1, 2, 3… y recibe el ICMP de cada router.
- d) El mensaje "Destino inalcanzable" es el que usa ping y responde "echo reply" para confirmar que el host está vivo.

**32.** En ARP, cuando el destino está en otra red distinta, ¿qué dirección MAC se resuelve por broadcast?
- a) La MAC del host destino directamente, ya que su IP destino es fija a lo largo de todo el camino.
- b) La MAC del default gateway, que es el que tiene la IP más baja de la red.
- c) La MAC del default gateway, que es el que tiene la IP más alta de la red.
- d) La MAC del servidor DHCP, que fue quien asignó la IP del destino.

**33.** ¿Cuál afirmación sobre DHCP coincide con la wiki?
- a) Asigna IP dinámica mediante un unicast dirigido al servidor, con un tiempo de arriendo que expira o se renueva.
- b) Asigna IP dinámica por broadcast y entrega gateway y DNS, pero fue reemplazado por BOOTP y RARP.
- c) Entrega la IP con tiempo de arriendo, pero el gateway y el DNS los resuelve ARP por separado.
- d) Asigna IP dinámica por broadcast y también entrega gateway y DNS; reemplazó a BOOTP y RARP.

**34.** ¿Cuál descripción de MPLS coincide con la wiki?
- a) Agrega una etiqueta (label) y rutea por ella; se lo llama capa 2,5, usa routers LSR y su header es de 32 bits (20 de label).
- b) Agrega una etiqueta y rutea por ella; se lo llama capa 3,5, usa routers LSR y su header es de 32 bits.
- c) Agrega una etiqueta al paquete pero igual rutea por la dirección IP; se lo llama capa 2,5 y usa routers LSR.
- d) Agrega una etiqueta (label) y rutea por ella; se lo llama capa 2,5, usa routers LSR y su header es de 20 bits en total.

**35.** Según la wiki, ¿cuál par protocolo–característica es correcto?
- a) OSPF es interdominio y usa path vector; BGP es intradominio y usa estado de enlaces.
- b) OSPF es intradominio, usa estado de enlaces y divide el Sistema Autónomo en áreas conectadas al backbone (área 0).
- c) BGP es intradominio, maneja políticas y establece enlaces TCP entre routers de un mismo Sistema Autónomo.
- d) OSPF es intradominio pero usa vector distancia, y sus áreas se conectan al backbone, que es el área 1.

**36.** Según la wiki, ¿en qué se diferencian IS-IS y OSPF?
- a) Ambos usan vector distancia; IS-IS es multiprotocolo y OSPF es solo para IP.
- b) IS-IS usa estado de enlaces y OSPF usa vector distancia; ambos son solo para IP.
- c) Ambos usan estado de enlaces, pero IS-IS es multiprotocolo mientras que OSPF es solo para IP.
- d) Ambos usan estado de enlaces, pero OSPF es multiprotocolo mientras que IS-IS es solo para IP.

**37.** Según la wiki (Unidad 2), ¿cuál afirmación describe correctamente al router como elemento principal de la capa 3?
- a) Reenvía cada paquete de inmediato, sin almacenarlo, dirigiéndolo al puerto de salida según su tabla interna.
- b) Almacena temporalmente cada trama, chequea errores y la dirige al puerto de salida según su tabla interna.
- c) Almacena temporalmente cada paquete, chequea errores y lo dirige al puerto de salida según su tabla interna.
- d) Almacena temporalmente cada paquete, chequea errores y lo dirige al puerto de salida según la dirección MAC destino.

**38.** ¿Cuál de estas afirmaciones sobre el servicio orientado a conexión (circuito virtual) en capa 3 es correcta según la wiki?
- a) Cada paquete lleva la IP de origen y de destino, y puede seguir una ruta independiente.
- b) Cada router necesita mantener memoria/estado del CV y todos los paquetes siguen la misma ruta.
- c) No requiere establecimiento previo, pero todos los paquetes siguen la misma ruta.
- d) El router no necesita información de estado, y ante una falla en el camino se cambia la ruta.

**39.** Según la wiki, ¿cuál asociación entre forma de transmitir en capa 3 y su descripción/ejemplo es la correcta?
- a) Broadcast: se entrega al nodo más cercano según la métrica; lo usa DNS.
- b) Anycast: uno a todos en la red local; ejemplo, DHCP Discover (solo IPv4).
- c) Unicast: uno a muchos suscriptos a una dirección de grupo; ejemplo, streaming.
- d) Multicast: uno a muchos, un grupo suscripto a una dirección multicast; ejemplo, streaming.

**40.** ¿Qué es el sink tree (árbol óptimo) según la wiki?
- a) El árbol de menor costo desde un router hacia todos los demás.
- b) El árbol que queda tras podar del sink tree los enlaces que no pertenecen a un grupo multicast.
- c) El conjunto de rutas independientes que sigue cada datagrama hacia su destino.
- d) El árbol de mayor ancho de banda entre dos routers específicos.

**41.** En Reverse Path Forwarding (RPF), ¿cómo decide el router si reenvía un paquete de broadcast?
- a) Si llegó por el enlace del sink tree lo descarta; si no, lo copia a los demás enlaces.
- b) Si llegó por cualquier enlace con el número de secuencia esperado lo copia; si no, lo descarta.
- c) Si llegó por el enlace que pertenece al sink tree lo copia a los demás enlaces; si no, lo descarta por considerarlo duplicado.
- d) Si llegó por el enlace de menor costo hacia el destino lo copia a los demás; si no, lo descarta.

**42.** Según la wiki, ¿cómo se arma el árbol de distribución multicast y qué protocolo real lo implementa?
- a) Se inunda toda la red usando número de secuencia (Dalal & Metcalfe); el protocolo real es PIM.
- b) Se poda el sink tree dejando solo los enlaces del grupo (Deering & Cheriton); el protocolo real es PIM.
- c) Se poda el sink tree dejando solo los enlaces del grupo (Deering & Cheriton); el protocolo real es OSPF.
- d) Se arma un Core-Based Tree con un router raíz por grupo (Ballardie); el protocolo real es BGP.

**43.** Según la wiki, ¿cuál de estas asociaciones entre tipo de servicio de capa 2 y su ejemplo es la correcta?
- a) Orientado a conexión → Ethernet; sin conexión best effort → WiFi; con confirmación de tramas → satélite.
- b) Orientado a conexión → satélite/telefónica de larga distancia; sin conexión best effort → Ethernet; con confirmación de tramas → WiFi (802.11).
- c) Orientado a conexión → WiFi; sin conexión best effort → Ethernet; con confirmación de tramas → satélite.
- d) Orientado a conexión → satélite; sin conexión best effort → WiFi; con confirmación de tramas → Ethernet.

**44.** Sobre Stop-and-Wait y su ineficiencia en enlaces satelitales, ¿qué afirma la wiki?
- a) Con ventana = 1 el emisor manda una trama y espera la confirmación antes de mandar la siguiente; en satélite el tiempo total supera 2× el tiempo de propagación, desperdiciando el canal.
- b) Con ventana = 1 el emisor manda una trama y espera la confirmación antes de mandar la siguiente; en satélite el tiempo total supera 2× el tiempo de transmisión, desperdiciando el canal.
- c) Con ventana = N el emisor manda N tramas y espera la confirmación de la primera; en satélite el tiempo total supera 2× el tiempo de propagación.
- d) Con ventana = 1 el emisor manda una trama sin esperar la confirmación; en satélite el tiempo total supera 2× el tiempo de propagación.

**45.** En Go-Back-N, tras un error/timeout en la trama 2, ¿qué hacen emisor y receptor según la wiki?
- a) El emisor reenvía solo la trama 2; el receptor guarda las tramas 3 a 8 hasta recibir la 2.
- b) El emisor reenvía desde la trama 2 en adelante; el receptor guarda las tramas 3 a 8 y las entrega al recuperarse la 2.
- c) El emisor reenvía solo la trama 2; el receptor descarta las tramas 3 a 8.
- d) El emisor reenvía desde la trama 2 en adelante; el receptor descarta las tramas 3 a 8 porque su ventana es de tamaño 1.

**46.** En Selective Repeat, con confirmación acumulativa, si faltó la trama 2 pero ya llegaron la 3, la 4 y la 5, ¿qué ocurre al recibirse finalmente la 2 (según la wiki)?
- a) El receptor confirma solo la trama 2 y el emisor reenvía la 3, la 4 y la 5.
- b) El receptor confirma directamente la trama 5 y el emisor reenvía la 3 y la 4 por precaución.
- c) El receptor confirma directamente la trama 5 y el emisor asume que la 3 y la 4 llegaron bien.
- d) El receptor confirma la trama 4 y el emisor asume que la 3 llegó bien y reenvía la 5.

**47.** La regla de oro dice que el contador de secuencia debe ser el doble del tamaño de la ventana. Con ventana 7, ¿cuál es la justificación de la wiki?
- a) El contador llega hasta 14; si se pierden los ACK y el emisor retransmite las tramas 1–7, el receptor (que esperaba 8–14) no las confunde con tramas nuevas.
- b) El contador llega hasta 14 para que el emisor pueda tener 14 tramas en tránsito sin ACK antes de detenerse.
- c) El contador llega hasta 7; si se pierden los ACK, el receptor reinicia la numeración para no confundir las retransmisiones.
- d) El contador llega hasta 14 para que el receptor pueda almacenar 14 tramas fuera de orden en su buffer.

**48.** ¿Qué es el piggybacking según la wiki?
- a) Agrupar varios ACK en una única trama de confirmación para no saturar el canal.
- b) Enviar el ACK del receptor montado dentro de otro mensaje que ya iba de vuelta hacia el emisor, para no gastar una trama solo en confirmar.
- c) Enviar el ACK en una trama dedicada inmediatamente después de cada trama de datos recibida.
- d) Enviar el ACK del emisor montado dentro de la siguiente trama de datos que va hacia el receptor.
