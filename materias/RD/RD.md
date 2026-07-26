# Redes de Datos — Wiki

> **1er Parcial — comisión Prof. Medin.** Material de la Cátedra de Redes de Información (UTN-FRR; teóricos Ings. Vitri, Baró, Travaglino; base bibliográfica: Tanenbaum & Wetherall, *Computer Networks*, 5th ed.).
>
> ⚠️ **Alcance del parcial (confirmado 2026-07-21):** es **multiple choice, 10 preguntas**, y entra **solo Capa de Enlace + Capa de Red** (Unidades 1 y 2). La **Unidad 3 (Transporte) NO entra** en este parcial — se conserva para el final. Los **ejercicios reales** de Medin están al final de las Unidades 2 y 3.

## Índice
1. Unidad 1 — Capa de Enlace: control de flujo y errores
2. Unidad 2 — Capa de Red: servicios, ruteo, IPv4, congestión y protocolos de control
3. Unidad 3 — Capa de Transporte: servicios, características, TCP y UDP  ⚠️ *(FUERA del 1er parcial — queda para el final)*

**Cómo está armada cada unidad:** Conceptos clave (repaso rápido) → Desarrollo (por tema del teórico) → Ejercicios resueltos tipo → Dudas / pendientes → Fuentes.

## Desarrollo

### Unidad 1 — Capa de Enlace: control de flujo y errores

#### Conceptos clave
- La **Capa de Enlace (capa 2)** hace **control de errores** y **control de flujo**. Corta la cadena de bits en **tramas** (header + datos + trailer/cola).
- **Framing (separación en tramas):** contar bytes (no se usa), **flag de comienzo** (byte/bit-stuffing — sí se usa), violaciones de codificación (4B/5B).
- **Control de flujo por ventana deslizante:** **Stop-and-Wait** (ventana 1), **Go-Back-N** (reenvía desde el error), **Selective Repeat** (reenvía solo la que falló, guarda las demás).
- Regla de oro: el **contador de secuencia debe ser el doble** del tamaño de la ventana.
- El teórico trae un cálculo de ventana mínima (tramas que entran en el RTT), pero es **poco probable** en el parcial de Medin (conceptual).

#### Desarrollo

##### 1) Introducción
- La **capa física** define voltajes, frecuencias, ancho de banda, forma de pulsos, modulaciones. Ese es el servicio que le da a la Capa de Enlace.
- La **Capa de Enlace** usa el servicio de la física y le brinda uno nuevo a la **Capa de Red**. Añade encabezamiento y bits de cola.
- **Trama ("frame"):** cadena de bits de longitud fija, unidad de datos de capa 2.
- **Header:** bits al inicio para reconocer dónde empieza una trama + direcciones origen/destino. **Trailer (bits de cola):** al final, principalmente para control de errores.
- Los protocolos de capa 2 del **emisor y receptor deben ser los mismos**.

| Header (encabezamiento) | Información de capas superiores | Trailer (bits de cola) |
|---|---|---|

##### 2) Tipos de servicio
- **a) Orientado a conexión:** circuito virtual punto a punto con **3 fases** (establecimiento, intercambio, desconexión). *Ej.: red satelital / telefónica de larga distancia* (canal largo y poco confiable; en el establecimiento se inicializan contadores y se mide la tasa de error).
- **b) Sin conexión ("best effort"):** el más simple, sin control ni retransmisiones. Canales muy confiables o **streaming en tiempo real** (no tiene sentido retransmitir un píxel o instante de voz perdido). *Ej.: Ethernet* (si una trama se pierde por ruido, capa 2 no la detecta ni retransmite; lo resuelven las capas superiores).
- **c) Sin conexión pero con confirmación de tramas:** típico de **canales inalámbricos** con interferencia. Cada trama se numera y el receptor confirma; si no llega en un tiempo, se reenvía. *Ej.: WiFi (802.11).*

##### 3) Separación en tramas ("Framing")
1. **Contar bytes de trama:** el header dice cuántos bits lleva la trama. **Problema:** si el header llega con error se pierde el sincronismo y cuesta re-sincronizar → **no se usa en la práctica**.
2. **Indicar comienzo de trama (flag):** un patrón fijo de bits ("bandera") marca el inicio. Es el método **más usado**. Si el patrón aparece en los datos:
   - **Byte-stuffing:** se antepone un byte especial **ESC** al flag accidental; el receptor lo quita. Lo usa **PPP**.
   - **Bit-stuffing:** se intercalan bits de relleno. Lo usan el **puerto USB** y **HDLC**. En **HDLC** el flag es `01111110` (un 0, seis 1, un 0); si el emisor ve **un 0 y cinco 1** seguidos en los datos, inserta un 0 para romper el flag. También ayuda a la física a no perder sincronismo (agrega transiciones).
3. **Detectar violaciones de codificación:** en **4B/5B** hay palabras de 5 bits no usadas; una de ellas marca inicio/fin de trama (ej. `11000-10001`). Lo usan **FDDI** y **Fast-Ethernet**.
- **Combinación:** Ethernet clásica (802.3) y WiFi (802.11) usan flag de inicio + campo de longitud. En WiFi el flag es largo (**72 bits**) para que el receptor se prepare.

##### 4) Control de flujo (de velocidad)
- Si el emisor transmite más rápido de lo que el receptor procesa, **se pierden datos**. Hace falta un control de flujo.
- **Feedback:** el receptor avisa qué pasa en su extremo; si no llega en un tiempo, el emisor retransmite.
- **Secuencia:** al retransmitir se corre el riesgo de que el receptor acepte una trama duplicada como nueva → se **numeran las tramas** con número de secuencia.
- Dos métodos: **por ventana deslizante** (capa 2 y superiores) y **por velocidad** (TCP en capa 4).

**a) Stop-and-Wait ("1-bit Sliding Window", ventana = 1):** envía una trama y espera la confirmación; recién ahí manda la siguiente.
- **Temporizador:** si no llega la confirmación en un tiempo, reenvía.
- **Secuencia:** obligatoria para que el receptor distinga una retransmisión de una trama nueva.
- **Piggybacking:** el receptor manda el ACK **dentro de otro mensaje** que ya iba de vuelta (aprovecha el viaje).
- **Ineficiencia:** con propagación no despreciable (satélite), el tiempo total supera **2× el tiempo de propagación**; esperar todo ese tiempo **desperdicia el canal**.

**b) Go-Back-N (ventana = N):** el emisor manda N tramas mientras espera el ACK de la primera. Si una trama (p. ej. la 2) llega con error / expira su timeout, **reenvía desde la 2 en adelante**. El **receptor descarta todo lo que llega fuera de orden** (su ventana es de tamaño 1): descarta 3, 4, 5, 6, 7, 8.

**c) Selective Repeat (envío selectivo):** el receptor **almacena las tramas fuera de orden** y el emisor **reenvía solo la que falló**. Mejor uso del canal, pero el receptor necesita **más memoria**. Usa **confirmación acumulativa**: al recibir la trama 2 (que faltaba) confirma directamente la 5, y el emisor asume que 3 y 4 llegaron bien.

**Contador de secuencia:** debe ser el **doble** del tamaño de la ventana, para que un reenvío no se confunda con tramas nuevas. *Ej.: ventana 7 → el contador debe llegar hasta 14; si se pierden los ACK y el emisor retransmite las tramas 1–7, el receptor (que esperaba 8–14) no debe confundirlas.*

**Ventanas de TX y RX:** cada uno tiene su ventana. La del **TX** guarda las tramas enviadas esperando ACK; la del **RX** guarda las que espera recibir. Con cada ACK el TX avanza su ventana; con cada trama nueva el RX avanza la suya.

#### Ejercicios resueltos tipo
> El estilo de Medin es conceptual. La Unidad 1 no tiene preguntas registradas en los modelos, pero por contenido las candidatas son:

**P) ¿Qué funciones cumple la capa de enlace?** Control de **errores** y control de **flujo**; arma las **tramas** (framing) agregando header (delimitación + direcciones) y trailer (control de errores); usa el servicio de la capa física y se lo brinda a la capa de red.

**P) Enumere y explique los métodos de separación en tramas (framing).** Contar bytes (no se usa, pierde sincronismo ante error); **flag de comienzo** con **byte-stuffing** (PPP) o **bit-stuffing** (HDLC, USB); detección de **violaciones de codificación** (4B/5B en FDDI y Fast-Ethernet). *(Desarrollar uno, p. ej. bit-stuffing en HDLC con el flag `01111110`.)*

**P) Compare Stop-and-Wait, Go-Back-N y Selective Repeat.** (Ver tabla abajo.)

**P) ¿Qué es el piggybacking?** Enviar el ACK del receptor **montado dentro de otro mensaje** que ya iba de vuelta hacia el emisor, para aprovechar el viaje y no gastar una trama solo para confirmar.

**Tabla comparativa de los 3 métodos de ventana deslizante:**

| Método | Ventana TX | Receptor ante error | Retransmisión | Memoria RX | Eficiencia |
|---|---|---|---|---|---|
| Stop-and-Wait | 1 | Espera ACK de cada trama | La única pendiente (por timeout) | Mínima | Baja |
| Go-Back-N | N | Descarta todo fuera de orden | Desde la trama perdida en adelante | Mínima | Media |
| Selective Repeat | N | Guarda las fuera de orden | Solo la que falló (ACK acumulativo) | Alta | Alta |

> **Cálculos numéricos (del teórico — POCO PROBABLE en el parcial de Medin, dejados como referencia):**
> - *Ventana mínima en satélite:* RTT = 0,5 s, v = 50 kbps, trama = 1000 bits. Tiempo por trama = 1000/50k = 20 ms; el ACK vuelve en 520 ms; a 50 kbps entran 50 tramas/s → en 0,52 s ≈ **26 tramas**.
> - *Línea de alta velocidad:* RTT = 1 ms, v = 2 Gbps, trama = 1000 bits → 2×10⁹ × 10⁻³ = 2×10⁶ bits = 2000 tramas → ventana ≈ **2001 tramas**.
> - *Regla:* ventana mínima ≈ (bits transmitidos durante el RTT) / (bits por trama). El cuello de botella es un producto **retardo × ancho de banda** alto (retardo grande *o* velocidad grande).

#### Dudas / pendientes
- _(nada pendiente por ahora)_

#### Fuentes
- `fuentes/RD/Medin-1er-parcial/1 - Capa de Enlace - Control de Flujo.pdf`
- Tanenbaum & Wetherall, *Computer Networks*, 5th ed.

### Unidad 2 — Capa de Red: servicios, ruteo, IPv4, congestión y protocolos de control

#### Conceptos clave
- La **Capa 3 (Red)** lleva **paquetes** de origen a destino a través de múltiples redes. Elemento principal: el **router** (mira la IP destino y su tabla interna).
- **Dos servicios:** sin conexión (**datagrama**, IP) vs. orientado a conexión (**circuito virtual**).
- **4 formas de transmitir (pregunta típica):** **Unicast, Broadcast, Multicast, Anycast**.
- **Ruteo:** Dijkstra (paso más corto), **Vector Distancia** (Bellman-Ford / RIP; problema de la cuenta a infinito), **Estado de Enlaces** (OSPF, IS-IS; converge más rápido).
- **IPv4:** direcciones de 32 bits, header 20–60 bytes, prefijo de red + host, máscara, CIDR, **NAT** + rangos privados, **TTL**.
- **Congestión (5 etapas):** provisioning → traffic-aware routing → admission control → traffic throttling → load shedding.
- **Protocolos de control:** **ICMP** (errores/diagnóstico), **ARP** (IP→MAC), **DHCP** (IP dinámica), MPLS, OSPF, BGP.

#### Desarrollo

#### Servicios y Distribución
##### Introducción
- **Capa 3 (Red):** lleva paquetes desde el origen hasta el destino final atravesando múltiples redes. Debe conocer la topología y los routers del camino.
- **Router:** elemento principal. Almacena temporalmente cada paquete, chequea errores y lo dirige al puerto de salida según su **tabla interna**.
- **Paquete:** unidad de información de capa 3 (≠ *trama* de capa 2 ≠ *segmento* de capa 4).

##### Servicio sin conexión (datagrama)
- Cada paquete viaja por caminos independientes, puede llegar desordenado; sin establecimiento previo. Los paquetes se llaman **datagramas**. **IP** es el protocolo base de Internet y opera a modo datagrama.

##### Servicio orientado a conexión (circuito virtual)
- Primero se establece un **circuito virtual** (una única ruta) verificando su calidad; luego se envían los paquetes indicando el CV. **3 etapas:** establecimiento → intercambio → desconexión coordinada. Cada router necesita memoria para el CV.

| Suceso | Sin conexión | Orientado a conexión |
|---|---|---|
| Establecimiento del CV | No se necesita | Necesario |
| Direccionamiento | Cada paquete lleva IP origen y destino | Cada paquete lleva sólo el nº de CV |
| Info de estado | Router no necesita info extra | Router necesita memoria para el CV |
| Ruta | Independiente por paquete | Todos siguen la misma ruta |
| Falla | Se cambia la ruta | Finaliza la comunicación |
| QoS / Congestión | Difícil de gestionar | Se reservan recursos al establecer el CV |

##### Distribución de mensajes (broadcast / multicast / anycast)
- **Broadcast (a toda la red):** métodos → un paquete por usuario (lento); **multidestination routing** (lista de destinos en el paquete); **flooding/inundación** (a todos los enlaces, con **nº de secuencia** para no hacer "bola de nieve"). **Sink tree (árbol óptimo):** árbol de menor costo de un router a todos los demás. **Reverse Path Forwarding (RPF, Dalal & Metcalfe 1978):** si el paquete llegó por el enlace del sink tree se copia a los demás; si no, se descarta (duplicado).
- **Multicast (a un grupo):** **(Deering & Cheriton 1990)** poda el sink tree dejando solo los enlaces del grupo. **Core-Based Tree (Ballardie 1993):** router **raíz** por grupo. Protocolo real: **PIM**.
- **Anycast (al más cercano):** la red entrega al nodo más próximo según la métrica. Lo usa el **DNS**; muy usado en IPv6.

#### Ruta Óptima Origen-Destino (algoritmos de ruteo)
- **Tarea principal de la capa 3:** determinar la ruta origen→destino. **Estáticas (no adaptativas)** vs. **dinámicas (adaptativas)** → los routers usan dinámicas. **Ruta óptima = sink tree**; métricas: saltos, retardo, costo.

##### Paso más corto — Dijkstra (1959)
- Se eligen nodos de menor distancia total al origen (a los no explorados, distancia ∞). *Ej. del teórico:* mejor ruta A→D = **ABEFHD = 10** (por C daría 12).

##### Vector Distancia (Distance Vector / Bellman-Ford / RIP)
- Cada router guarda la distancia hacia todos los demás. Usado en ARPANET y en Internet como **RIP**. *Ej.:* router J con vecinos A(8), I(10), H(12), K(6) hacia G → por H = 18 ms (la mejor).
- **Problema de la cuenta a infinito:** lentísimo para notificar una caída; el error se propaga sumando saltos. Solución: fijar un "infinito" bajo (máx. saltos + 1). *Buenas noticias se propagan rápido; malas, lento.*

##### Estado de Enlaces (Link State)
- ARPANET 1979; hoy **IS-IS y OSPF**. **5 pasos:** (1) conocer vecinos y direcciones; (2) medir métrica a cada vecino; (3) armar mensaje; (4) enviarlo a **toda la red** (flooding) y recibir los de los demás; (5) calcular el mejor camino a cada router.
- Costo ≈ inversamente proporcional a la velocidad (1 Gbps→1; 100 Mbps→10). Vs. Vector Distancia: **más memoria/procesamiento** pero **converge más rápido**.

##### Protocolos de Internet · jerarquías · móviles · ad-hoc
- **Protocolos:** IS-IS (multiprotocolo), OSPF (solo IP), RIP (obsoleto).
- **Jerarquías por regiones:** dividir la red en regiones (cada router conoce solo la suya) → tablas más chicas, a costa de caminos algo más largos. **Kamoun & Kleinrock (1979):** niveles óptimos = **Ln(N)**, con **e·Ln(N)** entradas por router.
- **Usuarios móviles:** **Home Location** + **Home Agent**; en la red visitada pide una **Care-of-Address** y el Home Agent le reenvía por **túnel (tunneling / IP-Mobility)**.
- **Redes ad-hoc (MANETs):** los nodos son también routers; descubrimiento de ruta por flooding con nº de secuencia; algoritmos **DSR, AODV, GPSR** (geográfico).

#### IPv4
##### Estructura de Internet (Tiers) y protocolo IP
- Internet = conjunto de **Sistemas Autónomos** interconectados, con backbones jerárquicos. **Tier 1** (backbones globales, peering sin costo — Global Crossing, AT&T), **Tier 2** (ISP regionales con data servers — Claro, Personal), **Tier 3** (universidades, ISP chicos). Todo unido por **IP**.
- La capa de transporte recorta datos en paquetes de **~1500 bytes** (compatibilidad Ethernet; IP soporta hasta **64 KB**) y se los pasa a capa 3, que los lleva al destino y los reordena.

##### Encabezamiento IPv4 (20–60 bytes; 20 fijos, filas de 32 bits)
| Campo | Tamaño | Descripción |
|---|---|---|
| Versión | 4 bits | IPv4 / IPv6 |
| IHL (largo de header) | 4 bits | 5 = 20 bytes (mínimo); 15 = 60 bytes (máx.) |
| Differentiated Services | 1 byte | QoS: 6 bits clase de servicio + 2 bits congestión (ECN) |
| Total Length | 2 bytes | Largo total; máx **65.535 = 2¹⁶−1** |
| Identificación | 2 bytes | Para rearmar la secuencia en el receptor |
| DF (Don't Fragment) | 1 bit | "1" = no fragmentar |
| MF (More Fragments) | 1 bit | "1" = faltan más fragmentos (0 en el último) |
| Fragment Offset | 13 bits | Nº de fragmento; máx **8191** |
| TTL (Time to Live) | 8 bits | −1 por router; máx **255 saltos**; a 0 se descarta y se avisa (evita loops) |
| Protocol | — | Protocolo de capa 4: **TCP o UDP** |
| Header Checksum | — | Detecta errores del header; se recalcula en cada router (cambia el TTL) |
| Source / Destination | 32 bits c/u | IP origen / destino |
- **Opciones** (raramente usadas): Security, Strict/Loose source routing, Record route, Timestamp.

##### Direccionamiento
- Direcciones de **32 bits (4 bytes)** → **2³² ≈ 4.294 millones**. Se escriben en decimal separando bytes por punto. Cada interfaz (RJ-45) tiene su IP → un router tiene una IP por interfaz.
- **Prefijo de red (network) + host:** el prefijo (longitud variable) es igual para toda la red; los bits de la derecha distinguen al host. Se anota como *IP menor de la red* + `/bits`. *Ej.:* `128.208.2.0/24` (24 bits red, 8 bits host).
- **Máscara de subred:** todos 1 en el prefijo y 0 en la parte de host; `AND` entre máscara y una IP → da el prefijo de red. *Ej.:* `/24` → `255.255.255.0`.

##### Clases (hasta 1993, obsoleto) y CIDR (actual)
- **Clases:** A (prefijo 7 bits, 128 redes, 16M hosts), B (14 bits, 16.384 redes, 65.536 hosts), C (21 bits, 256 hosts), D (**multicast**), E (uso futuro). Prefijo **fijo** por clase.
- **CIDR (Classless InterDomain Routing):** agrupa prefijos en **superredes** (*route aggregation*, RFC 4632) → una sola entrada en la tabla del router para muchas subredes. Redujo los prefijos a ~200.000 en el mundo (por eso IPv4 "aguantó").

##### Direcciones especiales · subredes · NAT
- **Especiales:** `0.0.0.0` (booteo/propia red), `255.255.255.255` (broadcast local), `127.x.x.x` (loopback). IPs **públicas** (únicas, circulan por Internet) vs **privadas** (solo internas). Asigna **ICANN**.
- **Subred:** red dentro de otra; cada una con su prefijo → tablas de routers más chicas. Desventaja: si un host cambia de red debe cambiar su IP (la **MAC** no cambia nunca).
- **NAT (Network Address Translation):** el ISP traduce IPs **privadas** en una pública; las máquinas de una casa se distinguen por el **puerto** (16 bits; puertos 0–1023 reservados, ej. **80 = web**). Rangos privados: **10.0.0.0/8**, **172.16.0.0/12**, **192.168.0.0/16**. Crítica: viola el principio de que una máquina no debería cambiar su IP; con IPv6 se seguiría usando como **firewall**.

> **Subnetting numérico (ej. Universidad de Londres / 128.208.0.0/16):** el teórico trae repartos de direcciones con cálculo de prefijos y máscaras. Es **poco probable** que Medin tome subnetting a mano; alcanza con entender **qué es** el prefijo/máscara/CIDR/NAT.

#### Control de Congestión (capa de red)
- **Congestión:** retardo excesivo por demasiados paquetes en tránsito. La gestionan **capa 3 y capa 4** en conjunto. Al saturarse los buffers se pierden paquetes → se retransmiten → **empeora**. Más memoria **no** ayuda (Nagle, 1987: memoria infinita empeora el problema).
- **Dos caminos:** aumentar recursos o disminuir tráfico. **Flujo vs congestión:** el control de flujo es **1 emisor–1 receptor**; la congestión involucra **muchos** nodos.

**Las 5 etapas (pregunta típica):**

| # | Etapa | Inglés | Idea |
|---|---|---|---|
| 1 | Planificación de la red | *Network Provisioning* | Prevenir: reforzar routers/enlaces antes de saturar (proceso lento, meses) |
| 2 | Ruteo según tráfico | *Traffic-Aware Routing* | Repartir por rutas alternativas menos cargadas; peso = componente fija + variable (tráfico). Riesgo: **oscilación** → *multipath routing* |
| 3 | Admisión de circuitos virtuales | *Admission Control* | No crear nuevos CV que pasen por la zona congestionada; caracterizar el tráfico del nuevo CV |
| 4 | Atenuación de fuentes | *Traffic Throttling* | Pedir a las fuentes que bajen el tráfico (3 técnicas ↓) |
| 5 | Descarte de paquetes | *Load Shedding* | Última opción: tirar paquetes (mejor que colapsar) |

- **Etapa 4 — 3 técnicas:** (1) el router congestionado avisa **al emisor** con un paquete (puede marcar "tagged"); (2) el router **marca** el paquete y el **receptor** avisa a la fuente → paquete **"choke"**, es **ECN (Explicit Congestion Notification)**, no carga a los routers pero es más lento (extremo a extremo, junto con capa 4); (3) **Hop-by-hop backpressure**: cada router avisa hacia atrás al anterior → la **más rápida** pero **carga a los routers**.
- **Etapa 5 — qué descartar:** archivos → los **últimos** paquetes; streaming → los **más viejos**; MPEG → las modificaciones (conservar la imagen principal). Los **paquetes de control** son más importantes que los de datos. Algoritmo **RED (Random Early Detection):** descarta por promedio de la cola antes de llenarse (Floyd & Jacobson, 1993).

#### Protocolos de Control
- Además de IP (que lleva los datos), hay protocolos que **controlan** el tráfico. Sus mensajes viajan **router↔router** (los datos van host↔host).

##### ICMP (Internet Control Message Protocol) — capa 3
- Cuando pasa algo inesperado, el router manda un mensaje ICMP al origen (encapsulado en IP). Mensajes:

| Mensaje | Descripción |
|---|---|
| Destino inalcanzable | El router no localiza el destino (p. ej. paquete muy grande) |
| Tiempo excedido | El TTL llegó a 0; lo usa **traceroute** (envía TTL=1,2,3… y recibe el ICMP de cada router) |
| Problema en parámetro | Valor incorrecto en el header IP |
| Bajar tráfico de fuente | Pedir menor velocidad ante congestión (**source quench**, hoy en desuso) |
| Ruta alternativa | Existe una mejor ruta al destino |
| Eco | Lo usa **ping** (responde "echo reply") para ver si un host está vivo |

##### ARP (Address Resolution Protocol)
- Traduce **IP → MAC** en la LAN. Si un host necesita la MAC de una IP, manda un **broadcast** preguntando "¿quién tiene tal IP?"; el dueño responde con su MAC. (RFC 826.) Si el destino está en otra red, se resuelve la MAC del **default gateway** (IP más baja de la red). Clave: las **IP origen/destino son fijas**, las **MAC cambian** en cada LAN.

##### DHCP (Dynamic Host Configuration Protocol)
- Asigna **IP dinámica**: al encender, la PC manda un **broadcast** pidiendo IP; el servidor DHCP se la asigna con un **tiempo de arriendo** (expira/renueva). También entrega **gateway y DNS**. RFC 2131/2132; reemplazó a **BOOTP y RARP**.

##### MPLS · OSPF · BGP
- **MPLS (Multiprotocol Label Switching):** agrega una **etiqueta (label)** al paquete y rutea por ella (más rápido que por IP). Se lo llama **capa 2,5**; usa routers **LSR**; header de **32 bits** (20 bits label + QoS + bit "hay más labels" + TTL). RFC 3031.
- **OSPF (Open Shortest Path First):** protocolo **intradominio** (dentro de un Sistema Autónomo); usa **estado de enlaces**; IETF 1990 (RFC 2328), basado en IS-IS. Divide el SA en **áreas** que se conectan al **backbone (área 0)**; **routers frontera/border** entre áreas; se elige un **designated router** (+ backup) por LAN; mensajes **"Hello"** y **"Link State Update"**. Balanceo **ECMP (Equal Cost Multi Path)**.
- **BGP (Border Gateway Protocol):** protocolo **interdominio** (entre Sistemas Autónomos); maneja **políticas** (económicas, seguridad). Usa **path vector** (considera el camino recorrido, detecta bucles); establece **enlaces TCP** entre routers. Soporta **multihoming** (varios ISP) y **peering** (tráfico recíproco gratis). RFC 4271.

#### Ejercicios resueltos tipo
> Estos 5 son **preguntas reales** del parcial de Medin del **06/08/2024** (Capa de Red).

**1) En la 3ra capa del modelo OSI, ¿qué formas de transmitir un mensaje existen? Enumerar y desarrollar una.**
Cuatro: **Unicast** (uno a uno, IP específica — navegar web), **Broadcast** (uno a todos en la red local — DHCP Discover; solo IPv4), **Multicast** (uno a muchos, grupo suscripto a una dirección multicast — streaming), **Anycast** (uno al más cercano; la red entrega al nodo más próximo según la métrica — IPv6, DNS).

**2) Realice un diagrama de capa 3 con los distintos tipos de ISP.**
Jerarquía en 3 niveles: **Tier 1** (backbone global EE.UU./Europa/Asia; peering sin costo de tránsito entre ellos), **Tier 2** (regionales/nacionales; compran a Tier 1 y redistribuyen), **Tier 3** (locales; usuario final: hogares, empresas, cable, WiMAX, Ethernet; dependen de Tier 2). Es de capa 3 porque muestra cómo se interconectan routers de distintos proveedores hasta el usuario final.
*(Dibujar: 3 franjas jerárquicas, Tier 1 arriba interconectados entre sí, Tier 2 colgando de Tier 1, Tier 3 y usuarios finales abajo.)*

**3) Enumere las etapas de control de congestión y explique una.**
Las 5: (1) Planificación (*network provisioning*), (2) Ruteo según tráfico (*traffic-aware routing*), (3) Control de admisión de CV (*admission control*), (4) Atenuación de fuentes (*traffic throttling*), (5) Descarte de paquetes (*load shedding*). *Planificación:* anticipar cuellos de botella reforzando routers/enlaces antes de que se congestione (preventiva, a largo plazo).

**4) ¿Qué protocolo da estos mensajes? (destino inalcanzable, tiempo excedido, problema en parámetro, bajar tráfico de fuente, ruta alternativa).**
**ICMP**, capa 3, para diagnóstico y control de IP. Destino inalcanzable = el router no puede entregar; Tiempo excedido = TTL a 0; Bajar tráfico de fuente = reducir velocidad (source quench).

**5) ¿Para qué se emplean ARP, ICMP y DHCP?**
**ARP:** IP → MAC en la LAN. **ICMP:** informa errores y diagnostica (ping, traceroute). **DHCP:** asigna IP y parámetros (gateway, DNS) automáticamente al conectarse.

#### Dudas / pendientes
- Confirmar con Medin si toma el **diagrama de ISP** dibujado a mano o basta describirlo.

#### Fuentes
- `fuentes/RD/Medin-1er-parcial/1 - Capa de Red - Servicios y distribución.pdf`
- `fuentes/RD/Medin-1er-parcial/2 - Capa de Red - Ruta óptima origen-destino.pdf`
- `fuentes/RD/Medin-1er-parcial/3 - Capa de Red - IPv4.pdf`
- `fuentes/RD/Medin-1er-parcial/4 - Capa de Red - Control de Congestión.pdf`
- `fuentes/RD/Medin-1er-parcial/6 - Capa de Red - Protocolos de control.pdf`
- `fuentes/RD/Medin-1er-parcial/Capa de Red.pdf` (compilado de los anteriores)
- `fuentes/RD/Medin-1er-parcial/Preguntas y Respuestas Parciales de Medin.docx` (preguntas reales)
- Tanenbaum & Wetherall, *Computer Networks*, 5th ed.

### Unidad 3 — Capa de Transporte: servicios, características, TCP y UDP

> ⚠️ **FUERA del 1er parcial (Medin).** Este parcial es multiple choice sobre **Enlace + Red** únicamente. Transporte no entra; se conserva acá como material para el final.

#### Conceptos clave
- La **Capa 4 (Transporte)** da comunicación **extremo a extremo** (las capas 1–3 son salto a salto). Unidad de datos: **segmento**.
- **Dos protocolos:** **TCP** (orientado a conexión, confiable, byte-stream) y **UDP** (sin conexión, best-effort).
- **Responsabilidades:** segmentar/reensamblar, entrega ordenada y confiable (TCP), control de errores, control de flujo, **multiplexación por puertos**, control de congestión (TCP).
- **3-way handshake** (SYN → SYN-ACK → ACK) para abrir; desconexión simétrica con FIN/ACK en ambos sentidos.
- **Control de congestión TCP:** slow-start, **AIMD** (Additive Increase, Multiplicative Decrease), versiones **Tahoe / Reno**.
- **Puertos:** 16 bits (TSAP); conocidos: 20/21 FTP, 23 Telnet, 25 SMTP, 80 HTTP.

#### Desarrollo

#### Servicios y Primitivas
##### Introducción
- **Objetivo:** dar a la capa de aplicación un transporte **confiable, eficiente y costo-efectivo**. La **entidad de transporte** (SW+HW de capa 4) puede estar en el kernel, en librerías, en la placa de red o en un proceso.
- La capa 4 es la **primera que opera extremo a extremo** (las capas 1–2–3 trabajan **salto a salto / punto a punto**).

##### Servicios y segmentos
- **Orientado a conexión (TCP):** 3 fases (establecimiento, transferencia, liberación), con control de flujo y direccionamiento.
- **No orientado a conexión (UDP):** simple, sin controles.
- En capa 4 los **hosts** son el elemento principal (como los routers en capa 3). Arquitectura típica **cliente-servidor**.
- **Segmento:** unidad de datos de capa 4 (antes **TPDU**). Queda anidado dentro del paquete (capa 3) dentro de la trama (capa 2).

##### Primitivas (sockets)
- Las primitivas de capa 4 se llaman **sockets**. Ejemplo cliente-servidor con 5 primitivas: **LISTEN, CONNECT, SEND, RECEIVE, DISCONNECT**. El servidor hace `LISTEN` (se bloquea hasta que llega un cliente), luego `CONNECT`, luego `SEND`, etc.
- **Sockets de TCP** (Berkeley 4.2BSD, 1983; en Windows: *winsock*). Primitivas del **servidor**, en orden: **SOCKET** (crea el extremo), **BIND** (asigna dirección local / **puerto**), **LISTEN** (colas de espera), **ACCEPT** (acepta un pedido de conexión). Al final: **CLOSE** de ambos lados (**fin simétrico**). En el **cliente** `BIND` no es necesario.
- TCP = socket orientado a conexión → **"Reliable Byte Stream"**. Sin conexión → `CONNECT` fija el destino y `SEND`/`RECEIVE` mandan datagramas. Protocolos nuevos: **SCTP** (RFC 4960), **SST**.

#### Características de Transporte
##### Direccionamiento (puertos)
- **TSAP (Transport Service Access Point) = PUERTO**, de **16 bits** → **65.536** direcciones. Un host usa varios puertos con una sola IP. Conocidos: **Telnet 23, SMTP 25, HTTP 80, FTP 21**.
- Puerto destino desconocido: **port mapper** (puerto 111, mapea servicio→puerto) o **server process** (monitorea varios puertos como proxy).

##### Establecimiento de la conexión
- Se manda un **Connection Request** y se espera la aceptación. **Problema crítico: evitar segmentos duplicados** (*ej. transferencia bancaria duplicada* si el cliente reenvía por demora).
- Solución: **limitar la vida del segmento** (tiempo/saltos). Tiempo máx. **T ≈ 120 s** en Internet; no reusar un nº de secuencia antes de T.
- **Three-way handshake (Tomlinson 1975):** nº de secuencia en cada segmento (de un reloj en tiempo real, sin necesidad de sincronizar). TCP lo usa con **32 bits** de secuencia y **valor inicial aleatorio** (anti-predicción). *(RFC 1323, PAWS.)*

##### Desconexión
- **Simétrica** (dos canales unidireccionales independientes) o **asimétrica** (uno cuelga y corta, como el teléfono).
- **Problema de los dos ejércitos:** no hay forma de garantizar que el **último mensaje** fue recibido → por eso la desconexión también es un **handshake de 3 vías**, y cada lado corta por su cuenta con **timeout** si se pierden mensajes.

##### Control de errores y de flujo
- Mismos mecanismos que capa 2 pero **extremo a extremo**. **Checksum/CRC** al final del segmento: **obligatorio en TCP**, opcional en UDP.
- **Ventana deslizante** + nº de secuencia + reenvío por timeout = **ARQ (Automatic Repeat reQuest)**.
- Errores dentro de un **router** no los ve capa 2 → los detecta capa 4. En **WiFi** se usa stop-and-wait en capa 2. **Buffers:** mismo tamaño / distinto tamaño / **circular** (mejor). Cada ACK informa el segmento recibido y el **espacio libre**. Ventana **dinámica** ajusta a la capacidad de la red y a la memoria disponible.

##### Multiplexación
- Varias conexiones (Zoom, mail, WhatsApp…) comparten un enlace. **Multiplexación inversa: SCTP** usa varias conexiones en paralelo. **TCP no multiplexa (es unicast).**

##### Control de congestión (capa 4)
- Responsabilidad **conjunta** capa 3 + capa 4: **ocurre en el router** (la detecta capa 3) pero la **causa el tráfico** de capa 4. Objetivo: dar a cada fuente una **tasa de bits** buena sin congestionar.
- **Tasa justa (Máx-Mín Fair):** subir una fuente obliga a bajar otra. *Ej. 4 fuentes:* B, C, D = 1/3 y A = 2/3.
- **AIMD (Additive Increase, Multiplicative Decrease — Chiu & Jain, 1989):** sube de a poco, baja a la mitad → **converge** al óptimo. Es la ley de TCP (no del todo justa: favorece conexiones cortas por el RTT). Otros protocolos deben ser **"TCP-friendly"**. Variantes: **CUBIC** (Linux, pérdidas), **Compound** (Windows, pérdidas+retardo), **FAST TCP** (tiempo de propagación).

##### Crash recovery · inalámbricas
- Ante **crash del receptor** el emisor tiene 4 estrategias (retransmitir siempre / según S0 / según S1 / nunca) y **nunca es transparente** para las capas superiores.
- **WiFi:** pérdida normal ~10% (TCP toleraría ~1%) → se retransmite en **capa 2** (stop-wait), imperceptible para capa 4 (ms vs ~1 s). **Satélite:** tiempos de capa 2 ≈ capa 4 → se usa **FEC** o no se retransmite en transporte.

#### Protocolo TCP
##### Introducción
- **TCP (Transmission Control Protocol):** conexión **confiable extremo a extremo** sobre redes no confiables. RFC 793 (1981); guía RFC 4614. Se identifica por **puerto** (16 bits): <1024 reservados (root); listado en iana.org. Procesos en segundo plano = **daemon** (FTP daemon: puertos 20/21).

##### Características
- **Full-duplex, unicast, extremo a extremo.** No soporta multicast ni broadcast.
- Segmento hasta **64 KB**, pero típico **≤ 1460 bytes** para entrar en una **trama Ethernet (1500 bytes)** con los headers TCP/IP y no fragmentar (MTU).
- **Byte-stream** (no message-stream): el receptor no sabe cómo se particionaron los bytes al enviarlos.

##### Encabezamiento TCP (20 bytes fijos + opciones)
- Primeros campos: **puertos** origen/destino, **nº de secuencia**, **nº de acknowledgement**. Un campo de 4 bits indica el largo del header (dónde empiezan los datos).
- **Flags (banderas):**

| Flag | Significado |
|---|---|
| CWR / ECE | Congestión (ECN, RFC 3168): **ECE** avisa que baje la velocidad; **CWR** confirma que redujo |
| URG | Hay **datos urgentes** (con Urgent Pointer) |
| ACK | El segmento lleva un acknowledgement (=0: no lleva) |
| PSH | El receptor debe **volcar los datos a la aplicación** sin bufferear |
| RST | **Reset**: recomenzar la conexión |
| SYN | **Sincronizar** el establecimiento de la conexión |
| FIN | El emisor **no tiene más datos** (desconexión) |

- **Window Size:** tamaño de la ventana deslizante (control de flujo); máx **2¹⁶ = 64 KB**. **Checksum:** obligatorio (controla el pseudo-header IP). **Options:** hasta **40 bytes** — **MSS** (tamaño máx. de segmento, default 556), **Window Scale** (agranda la ventana hasta 2³⁰ = 1 GB para enlaces rápidos/largos), **Timestamp**, **SACK**.

##### Establecimiento y estados
- **3-way handshake:** servidor `LISTEN`; cliente `CONNECT` con **SYN=1, ACK=0** (envía IP, puerto destino, MSS); el servidor responde **SYN-ACK**; el cliente responde **ACK**. *(Seguridad: criptografía, RFC 4987.)*
- **Desconexión:** 4 primitivas (**FIN + ACK en cada dirección**); si se pierde uno, un **timeout** completa la desconexión (evita el problema de los dos ejércitos).

##### Ventana deslizante · temporizadores · congestión · SACK
- **Ventana deslizante (control de flujo):** *ej.* receptor con buffer 4 KB y segmentos de 2 KB → tras 2 segmentos se llena; cada ACK informa el espacio libre. Segmentos grandes = **algoritmo de Nagle**.
- **Temporizadores:** el clave decide la **retransmisión**; se ajusta **dinámicamente** (mínimo ~1 s en capa 4, ~1000× el de capa 2). Timeout muy grande → retardos; muy chico → retransmisiones de más.
- **Control de congestión:** ventana = bytes en tránsito sin ACK, ajustada por **AIMD**. **Acknowledgement-clock:** los ACK marcan el ritmo de envío. **Slow-start:** duplica la ventana con cada ACK (mide **RTT**) hasta que hay pérdida → la ventana se **achica a la mitad**.
- **Versiones:** **Tahoe (1988)** — slow-start + incremento aditivo; ante 3 ACK duplicados asume pérdida y **reinicia con la mitad** de la ventana. **Reno (1990)** — agrega **fast recovery** (retoma desde la mitad). Modernas: **CUBIC** (Linux), **Compound** (Windows).
- **SACK (Selective Acknowledgement, RFC 2883):** el receptor informa **rangos** de segmentos recibidos → el emisor sabe exactamente qué retransmitir. *Ej.:* perdidos 2 y 5 → ACK del 1 + SACK de 3, 4 y 6.

#### UDP (comparación con TCP)
- **UDP (User Datagram Protocol):** sin conexión, envío inmediato, header mínimo de **8 bytes**, message-oriented. **No** hace control de flujo ni de congestión (envía al ritmo de la aplicación → puede saturar). Ante error (checksum) **descarta** el datagrama, sin retransmitir. Usos: **voz/video en tiempo real, DNS, DHCP, multicast**.

| | TCP | UDP |
|---|---|---|
| Orientación | A conexión (3-way handshake) | Sin conexión (envío inmediato) |
| Confiabilidad | Entrega, orden, retransmite | No garantiza entrega ni orden |
| Flujo / congestión | Sí ajusta | No |
| Cabecera | 20+ bytes | 8 bytes |
| Servicio | Byte-stream | Mensajes individuales |
| Usos | HTTP, FTP, correo, archivos | Voz/video, DNS, DHCP, multicast |

#### Ejercicios resueltos tipo
> Estos 5 son **preguntas reales** de otro parcial de Medin (Capa de Transporte).

**1) ¿Qué responsabilidades tiene la capa de transporte?**
Comunicación **extremo a extremo** confiable y eficiente entre aplicaciones. Funciones: dividir en **segmentos** y reensamblar; entrega **ordenada y confiable** (TCP); **control de errores**; **control de flujo** (según el receptor); **multiplexación** por puertos; **control de congestión** (solo TCP).

**2) ¿Cómo controla la congestión el protocolo UDP?**
**No la controla.** UDP no implementa control de congestión ni de flujo: envía al ritmo de la aplicación, sin adaptarse al estado de la red → puede saturar. Si se necesita control, lo debe implementar la aplicación.

**3) ¿Qué sucede si UDP detecta un error? ¿Y TCP?**
**UDP:** si el datagrama llega corrupto (checksum), simplemente lo **descarta**; sin retransmisión ni recuperación. **TCP:** detecta el error y **retransmite** los segmentos perdidos/dañados hasta recibir el ACK; mantiene orden y confiabilidad.

**4) Grafique un ejemplo de conexión 3-way handshake.**
`Cliente → SYN → Servidor` · `Servidor → SYN-ACK → Cliente` · `Cliente → ACK → Servidor`, y a partir de ahí flujo bidireccional. El cliente inicia con SYN; el servidor responde SYN-ACK (puede empezar a enviar); el cliente confirma con ACK.

**5) Enuncie diferencias entre TCP y UDP.**
(Ver tabla de arriba: orientación, confiabilidad, control de flujo/congestión, tamaño de cabecera, byte-stream vs mensajes, usos.)

#### Dudas / pendientes
- _(nada pendiente por ahora)_

#### Fuentes
- `fuentes/RD/Medin-1er-parcial/1 - Capa de Transporte - Servicios y Primitivas.pdf`
- `fuentes/RD/Medin-1er-parcial/2 - Capa de Transporte - Características de transporte.pdf`
- `fuentes/RD/Medin-1er-parcial/3 - Capa de Transporte - Protocolo TCP.pdf`
- `fuentes/RD/Medin-1er-parcial/Preguntas y Respuestas Parciales de Medin.docx` (preguntas reales)
- Tanenbaum & Wetherall, *Computer Networks*, 5th ed.

## Log
- 2026-07-21: Ingesta inicial del material del 1er parcial de Medin (10 PDFs de teórico + doc de preguntas). Se crearon las 3 unidades (Enlace, Red, Transporte) y el índice. Fuentes en `fuentes/RD/Medin-1er-parcial/`. Ajuste: parcial de Medin es conceptual → ejercicios tipo = preguntas reales; cálculos numéricos marcados como poco probables.
