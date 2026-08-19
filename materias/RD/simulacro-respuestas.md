# Simulacro — Respuestas y explicaciones

> ⚠️ No mires esto hasta terminar de responder.

**1. Respuesta: c.** La wiki (Unidad 2, header IPv4) define Differentiated Services como 1 byte = 6 bits de clase de servicio (QoS) + 2 bits de congestion (ECN). La opcion a invierte la particion (2+6), la d invierte los roles de cada grupo de bits, y la b niega la existencia de los bits ECN.

**2. Respuesta: a.** La wiki indica que el Header Checksum detecta errores del header y se recalcula en cada router porque cambia el TTL (se resta 1 por salto). El Fragment Offset, la direccion de destino y el Identification NO cambian salto a salto: destino/origen son fijos e Identification sirve para rearmar en el receptor, no se renueva por router.

**3. Respuesta: d.** La wiki: TTL de 8 bits, se resta 1 por router, maximo 255 saltos, y al llegar a 0 se descarta y se avisa (evita loops). La a le da tamaño y maximo equivocados (esos son de Total Length), la b invierte el sentido (incrementa en vez de decrementar) y la c invierte el comportamiento (reenvia sin avisar en vez de descartar y avisar).

**4. Respuesta: b.** La wiki: IHL de 4 bits, donde 5 = 20 bytes (minimo) y 15 = 60 bytes (maximo). La a invierte la correspondencia de los valores, la c lo confunde con Total Length (largo total en 2 bytes) y la d cambia la unidad (bits en lugar de bytes).

**5. Respuesta: a.** La wiki: MF (More Fragments) en 1 = faltan mas fragmentos y 0 en el ultimo; DF (Don't Fragment) en 1 = no fragmentar. La b invierte los valores de MF, la c invierte tanto el valor de MF como el significado de DF, y la d intercambia por completo los roles de DF y MF.

**6. Respuesta: d.** La wiki: Total Length son 2 bytes con maximo 65.535 = 2¹⁶−1. La a usa 8.191, que es el maximo del Fragment Offset (13 bits), no de Total Length. La b atribuye a Identification la funcion de Protocol (indicar TCP/UDP), y la c atribuye a Protocol la funcion de Identification (rearmar la secuencia): ambos intercambian los roles reales de esos campos.

**7. Respuesta: b.** La wiki (Unidad 2, Paso más corto — Dijkstra) dice que se eligen nodos de menor distancia total al origen y se da distancia infinita (∞) a los no explorados. (a) cambia ∞ por cero; (c) invierte origen por destino; (d) cambia 'menor' por 'mayor'.

**8. Respuesta: d.** La wiki (Unidad 2, Vector Distancia): 'buenas noticias se propagan rápido; malas, lento' y la solución es fijar un infinito bajo (máx. saltos + 1). (a) invierte buenas/malas y pone 'infinito alto'; (b) da una solución falsa (más memoria); (c) mezcla la solución del Estado de Enlaces (flooding). En b y c la primera cláusula es cierta pero la mitigación es falsa, por lo que la única íntegramente correcta es d.

**9. Respuesta: a.** La wiki (Unidad 2, Estado de Enlaces): usa más memoria/procesamiento pero converge más rápido, y hoy lo usan IS-IS y OSPF. (b) invierte a 'menos memoria'; (c) invierte a 'converge más lento'; (d) sustituye IS-IS por RIP, que la wiki clasifica como Vector Distancia.

**10. Respuesta: c.** La wiki (Unidad 2, Jerarquías por regiones): cada router conoce solo su región (tablas más chicas) a costa de caminos algo más largos; niveles óptimos = Ln(N) y e·Ln(N) entradas por router. (a) dice que acorta los caminos (falso); (b) dice 'conoce toda la red' (falso); (d) intercambia las fórmulas Ln(N) y e·Ln(N).

**11. Respuesta: b.** La wiki (Unidad 2, Usuarios móviles): en la red visitada el móvil pide una Care-of-Address y el Home Agent le reenvía por túnel (tunneling / IP-Mobility). (a) ubica la Care-of-Address en la red de origen (es en la visitada); (c) invierte los roles de móvil y Home Agent; (d) usa flooding (mecanismo de broadcast/MANET), no tunneling.

**12. Respuesta: a.** La wiki (Unidad 2, Redes ad-hoc): en las MANETs los nodos son también routers, el descubrimiento de ruta es por flooding con nº de secuencia, y los algoritmos son DSR, AODV y GPSR (geográfico). (b) reemplaza GPSR por RIP; (c) inventa un 'router raíz fijo' (eso es el Core-Based Tree de multicast, otra sección de la wiki); (d) cambia el flooding con nº de secuencia por Vector Distancia.

**13. Respuesta: b.** La wiki dice: 'máscara (todos 1 en el prefijo y 0 en el host); AND entre máscara y una IP -> da el prefijo de red'. (a) invierte el concepto: la máscara pone en 0 los bits de host, así que no los conserva. (c) confunde con 255.255.255.255, que es el broadcast local y no surge de ese AND. (d) confunde el resultado del AND con la longitud del prefijo.

**14. Respuesta: a.** La wiki usa ese mismo ejemplo: '128.208.2.0/24 (24 bits red, 8 bits host)'. (b) invierte prefijo y host. (c) ignora que la dirección es de 32 bits. (d) confunde la longitud del prefijo con una cantidad de subredes.

**15. Respuesta: d.** La wiki: 'D (multicast), E (uso futuro). Prefijo fijo por clase'. (a) desplaza los roles: multicast es D (no C) y uso futuro es E (no D). (b) contradice el 'prefijo fijo por clase' (la longitud variable es propia de CIDR). (c) le da a la clase A los valores de la clase B (A es 7 bits / 128 redes; B es 14 bits / 16.384 redes).

**16. Respuesta: c.** La wiki: 'CIDR agrupa prefijos en superredes (route aggregation, RFC 4632) -> una sola entrada en la tabla del router para muchas subredes'. (a) describe justamente el esquema de clases, que CIDR reemplaza. (b) mezcla subnetting con puertos. (d) describe NAT, no CIDR.

**17. Respuesta: b.** La wiki: '0.0.0.0 (booteo/propia red), 255.255.255.255 (broadcast local), 127.x.x.x (loopback)'. Las demás intercambian esos tres roles; (d) es la más traicionera porque acierta 0.0.0.0 pero cruza broadcast local y loopback. Sólo (b) respeta la asignación exacta de los tres.

**18. Respuesta: c.** La wiki: 'NAT... traduce IPs privadas en una pública; las máquinas de una casa se distinguen por el puerto (16 bits)... Rangos privados: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16'. (a) intercambia las máscaras de 172.16 y 192.168 y usa la MAC en vez del puerto. (b) invierte el sentido de la traducción (privada->pública) y usa el TTL. (d) contradice a la wiki: las privadas son sólo internas (no únicas ni ruteables), las únicas son las públicas.

**19. Respuesta: a.** La wiki (U1, Conceptos clave e Introducción) dice que la capa de enlace hace control de errores y de flujo, y que usa el servicio de la capa física para brindarle uno nuevo a la capa de red. (b) invierte las capas; (c) mete congestion (que es capa 3/4, no de enlace); (d) suma congestion y ademas apunta a la capa de transporte, no a la de red.

**20. Respuesta: c.** La wiki (U1, Introduccion): el header son los bits del inicio para reconocer donde empieza la trama mas las direcciones origen/destino, y el trailer (bits de cola) va al final principalmente para control de errores. (a) invierte header y trailer; (b) tiene el header correcto pero atribuye al trailer un numero de secuencia de control de flujo (el trailer hace control de errores); (d) pone al trailer marcando el comienzo, que es tarea del header.

**21. Respuesta: d.** La wiki (U1, Framing) dice que en 'contar bytes' el header indica cuantos bits lleva la trama, y si ese header llega con error se pierde el sincronismo y cuesta re-sincronizar, por eso no se usa. (a) describe el problema del flag, no del conteo; (b) atribuye overhead de bits de relleno (eso es bit-stuffing); (c) cambia header por trailer (el conteo esta en el header).

**22. Respuesta: b.** La wiki (U1, Framing): byte-stuffing antepone un byte ESC al flag accidental y lo usa PPP; bit-stuffing intercala bits de relleno y lo usan USB y HDLC. (a) intercambia las definiciones de las dos tecnicas; (c) intercambia los protocolos (pone HDLC en byte-stuffing y PPP en bit-stuffing); (d) mueve USB al byte-stuffing, cuando USB usa bit-stuffing.

**23. Respuesta: c.** La wiki (U1, Framing): el flag de HDLC es 01111110 (un 0, seis 1, un 0) y si el emisor ve un 0 y cinco 1 seguidos en los datos inserta un 0 para romper el flag. (a) usa seis 1 en vez de cinco como disparador; (b) inserta un 1 en lugar de un 0; (d) altera el patron del flag (01111100).

**24. Respuesta: a.** La wiki (U1, Framing): en 4B/5B hay palabras de 5 bits no usadas, una marca inicio/fin de trama, y lo usan FDDI y Fast-Ethernet. (b) cambia Fast-Ethernet por WiFi (segun la wiki, WiFi usa flag largo de 72 bits, no 4B/5B); (c) dice palabras de 4 bits, cuando las no usadas son de 5 bits; (d) atribuye 4B/5B a PPP y HDLC, que usan byte- y bit-stuffing.

**25. Respuesta: d.** La wiki (U2, Control de Congestión) dice textualmente que más memoria NO ayuda y que, con memoria infinita, el problema empeora (Nagle, 1987). 'a' invierte el efecto; 'b' cambia 'empeora' por 'se mantiene igual'; 'c' inventa una restriccion de capa que la wiki no menciona.

**26. Respuesta: c.** La wiki (U2): el control de flujo es 1 emisor-1 receptor y la congestion involucra muchos nodos. 'a' invierte ambos lados; 'b' agrega una distincion de capas inventada; 'd' niega que la congestion involucre muchos nodos.

**27. Respuesta: b.** La wiki (U2) lista: 1) provisioning, 2) traffic-aware routing, 3) admission control, 4) traffic throttling, 5) load shedding. 'a' intercambia las etapas 2 y 3; 'c' intercambia 4 y 5 (dejando load shedding antes que throttling); 'd' intercambia 1 y 2.

**28. Respuesta: a.** La wiki (U2, etapa 4): en ECN el router marca el paquete, el receptor avisa a la fuente, no carga a los routers pero es mas lento (extremo a extremo). 'b' cambia el mecanismo (avisar al emisor) y le atribuye 'la mas rapida'; 'c' invierte los atributos del backpressure (que es la MAS rapida y SI carga a los routers); 'd' atribuye al aviso 'tagged' las cualidades del backpressure.

**29. Respuesta: d.** La wiki (U2, etapa 5): en archivos se descartan los ultimos paquetes y en streaming los mas viejos; ademas los paquetes de control valen mas que los de datos. 'a' invierte ambos casos; 'c' acierta en archivos pero invierte streaming; 'b' contradice que el control es mas importante (habria que conservarlo, no tirarlo).

**30. Respuesta: b.** La wiki (U2, etapa 5): RED descarta por promedio de la cola ANTES de que se llene (Floyd & Jacobson, 1993). 'c' cambia 'antes de llenarse' por 'una vez llena'; 'a' cambia el autor y el momento; 'd' contradice que los paquetes de control son los mas importantes (no se descartan primero).

**31. Respuesta: c.** La wiki asocia "Tiempo excedido" (TTL a 0) con traceroute (envía TTL=1,2,3… y recibe el ICMP de cada router) y "Eco" con ping (responde "echo reply"). a) y b) invierten esos dos mensajes; d) le atribuye la función de ping a "Destino inalcanzable", que en la wiki es cuando el router no localiza el destino.

**32. Respuesta: b.** La wiki dice que si el destino está en otra red, ARP resuelve la MAC del default gateway, y que el gateway es la IP más baja de la red. c) cambia "más baja" por "más alta"; a) ignora que la MAC que se resuelve es la del gateway (aunque la IP destino sea fija, las MAC cambian en cada LAN); d) mete al DHCP, que no cumple ese rol.

**33. Respuesta: d.** Según la wiki, la PC manda un broadcast pidiendo IP, el servidor DHCP se la asigna con tiempo de arriendo, además entrega gateway y DNS, y DHCP reemplazó a BOOTP y RARP. a) cambia broadcast por unicast; b) invierte la relación histórica (DHCP reemplazó a esos protocolos, no al revés); c) le saca a DHCP la entrega de gateway/DNS y se la asigna erróneamente a ARP.

**34. Respuesta: a.** La wiki define MPLS como capa 2,5, con routers LSR, header de 32 bits (20 de label) y ruteo por la etiqueta (más rápido que por IP). b) cambia "capa 2,5" por "capa 3,5"; c) dice que rutea por IP en vez de por la etiqueta; d) confunde los 20 bits del label con el tamaño total del header, que es de 32 bits.

**35. Respuesta: b.** La wiki: OSPF es intradominio, de estado de enlaces, y divide el SA en áreas que se conectan al backbone, que es el área 0. a) intercambia por completo OSPF y BGP; c) dice que BGP es intradominio cuando es interdominio (entre Sistemas Autónomos); d) cambia estado de enlaces por vector distancia y el área 0 por área 1.

**36. Respuesta: c.** La wiki ubica a IS-IS y OSPF como protocolos de estado de enlaces y señala "IS-IS (multiprotocolo), OSPF (solo IP)". d) invierte cuál es multiprotocolo y cuál es solo IP; a) y b) cambian estado de enlaces por vector distancia (total o parcialmente).

**37. Respuesta: c.** La wiki dice que el router 'almacena temporalmente cada paquete, chequea errores y lo dirige al puerto de salida según su tabla interna' (mirando la IP destino). (a) contradice el almacenamiento temporal; (b) cambia paquete por trama, que es la unidad de capa 2, no de capa 3; (d) rutea por su tabla interna / IP destino, no por MAC (rutear por MAC es propio de un switch de capa 2).

**38. Respuesta: b.** Según la tabla de la wiki, en circuito virtual el router 'necesita memoria para el CV' y 'todos siguen la misma ruta'. (a) y (d) describen el servicio sin conexión (datagrama: IP origen/destino en cada paquete, ruta independiente, se cambia la ruta ante falla); (c) es falsa porque el CV sí exige establecimiento previo (3 etapas: establecimiento, intercambio, desconexión).

**39. Respuesta: d.** La wiki define Multicast como 'uno a muchos, grupo suscripto a una dirección multicast — streaming'. (a) describe en realidad Anycast (más cercano según la métrica, DNS), no Broadcast; (b) describe Broadcast (uno a todos, DHCP Discover, solo IPv4), no Anycast; (c) Unicast es uno a uno (navegar web), no uno a muchos.

**40. Respuesta: a.** La wiki: 'Sink tree (árbol óptimo): árbol de menor costo de un router a todos los demás', y la ruta óptima = sink tree. (b) es el árbol multicast podado (Deering & Cheriton), que se deriva del sink tree pero no es el sink tree; (c) corresponde al servicio datagrama; (d) contradice el criterio de menor costo y no figura en la wiki.

**41. Respuesta: c.** La wiki: en RPF 'si el paquete llegó por el enlace del sink tree se copia a los demás; si no, se descarta (duplicado)'. (a) invierte la lógica de copiar/descartar; (b) confunde RPF con el mecanismo de número de secuencia propio del flooding; (d) cambia el criterio: la decisión es por el enlace del sink tree (camino inverso hacia el origen), no 'de menor costo hacia el destino'.

**42. Respuesta: b.** La wiki: multicast 'poda el sink tree dejando solo los enlaces del grupo (Deering & Cheriton 1990)' y el 'Protocolo real: PIM'. (a) describe flooding/RPF (Dalal & Metcalfe), no la poda multicast; (c) tiene el método correcto pero el protocolo equivocado (OSPF es ruteo intradominio, no multicast); (d) el Core-Based Tree (Ballardie) sí es un concepto real de multicast en la wiki, pero el protocolo real sigue siendo PIM, no BGP (que es interdominio).

**43. Respuesta: b.** La wiki (U1, Tipos de servicio) mapea: orientado a conexión = red satelital/telefónica de larga distancia, best effort = Ethernet, con confirmación = WiFi 802.11. Las otras tres opciones intercambian al menos un par de esas asociaciones (ponen WiFi o satélite como best effort, o Ethernet como servicio con confirmación).

**44. Respuesta: a.** La wiki (U1, Control de flujo a) define Stop-and-Wait como ventana = 1 que envía una trama y espera la confirmación, y dice que con propagación no despreciable (satélite) el tiempo total supera 2× el tiempo de propagación. (b) cambia 'propagación' por 'transmisión'; (c) usa ventana N (eso es Go-Back-N); (d) invierte el comportamiento clave: S&W sí espera la confirmación.

**45. Respuesta: d.** La wiki (U1, Control de flujo b) dice que en Go-Back-N el emisor reenvía desde la trama perdida en adelante y el receptor descarta todo lo que llega fuera de orden (su ventana es de tamaño 1): descarta 3,4,5,6,7,8. (a) y (c) dicen 'solo la trama 2' (eso es Selective Repeat); (a) y (b) dicen que el receptor guarda las fuera de orden (también Selective Repeat, no Go-Back-N).

**46. Respuesta: c.** La wiki (U1, Control de flujo c) dice textualmente que al recibir la trama 2 (que faltaba) el receptor confirma directamente la 5 y el emisor asume que 3 y 4 llegaron bien. (a) describe una confirmación no acumulativa; (b) contradice el 'asume que 3 y 4 llegaron bien' agregando una retransmisión; (d) confirma un número de trama equivocado.

**47. Respuesta: a.** La wiki (U1, Contador de secuencia) explica que con ventana 7 el contador debe llegar hasta 14 para que, si se pierden los ACK y el emisor retransmite las tramas 1–7, el receptor (que esperaba 8–14) no las confunda con tramas nuevas. (b) confunde el contador con la cantidad de tramas en tránsito (eso es el tamaño de ventana); (c) da un contador de 7 (no el doble); (d) lo confunde con el tamaño del buffer del receptor.

**48. Respuesta: b.** La wiki (U1, Stop-and-Wait / piggybacking) lo define como enviar el ACK del receptor montado dentro de otro mensaje que ya iba de vuelta hacia el emisor, aprovechando el viaje y sin gastar una trama solo para confirmar. (d) invierte el sentido (habla del ACK del emisor hacia el receptor); (a) describe un ACK agrupado; (c) describe justo lo contrario: una trama dedicada solo para el ACK.
