# Redes de Datos — Wiki

> **1er Parcial — comisión Prof. Medin.** Material de la Cátedra de Redes de Información (UTN-FRR; teóricos Ings. Vitri, Baró, Travaglino; base bibliográfica: Tanenbaum & Wetherall, *Computer Networks*, 5th ed.).
>
> ⚠️ **Alcance del parcial (confirmado 2026-07-21):** es **multiple choice, 10 preguntas**, y entra **solo Capa de Enlace + Capa de Red** (Unidades 1 y 2). La **Unidad 3 (Transporte) NO entra** en este parcial — se conserva para el final. Los **ejercicios reales** de Medin están al final de las Unidades 2 y 3.

> 📌 **2do Parcial — PRÁCTICA, Prof. Germán Baró (mails del 30/09 y 01/10/2026).** Entra **solo Capa de Red = Unidad 2**. Temario por Tanenbaum (5ª ed.), **Cap. 5**:
> - **5.1** completo (págs. 305-311) — servicios con y sin conexión
> - **5.2.1 a 5.2.5** (págs. 311-325) — principio de optimalidad, camino más corto, inundación, vector distancia, estado de enlace
> - **5.6.1 y 5.6.2** (págs. 374-390) — protocolo IP, direcciones IP, subredes
> - **5.6.4** (págs. 398-403) — protocolos de control (ICMP, ARP, DHCP)
> - **5.6.6 y 5.6.7** (págs. 405-414) — OSPF y BGP
>
> Además: apunte de Baró (ICMP, ARP, comandos ping/tracert), práctica de **máscaras de subred** (problemas) y una **guía de estudio** con preguntas tipo. Todo está en `fuentes/Baro-2do-parcial/`.
>
> **Fechas (mail de Medín, 01/10):** si tu apellido va de Aguirre a Fassine (Bonadeo entra acá), rendís **práctica (Baró) el mié 21/10** y **teoría (Medín) el mar 27/10**. Si va después, rendís **teoría el 20/10** y **práctica el 28/10**. Siempre en el horario y aula habituales; **si llegás 10 min tarde, no rendís**. Por ahora **no hay mail sobre el temario del 2do teórico de Medín**.

## Índice
1. Unidad 1 — Capa de Enlace: control de flujo y errores
2. Unidad 2 — Capa de Red: servicios, ruteo, IPv4, congestión y protocolos de control  📌 *(entra en el 2do parcial práctico de Baró. No entran: broadcast/multicast/anycast, jerarquías, móviles, ad-hoc, Control de Congestión ni MPLS)*
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
- **Foco del 2do parcial de Baró (práctico):** **subnetting a mano** (dirección de red = IP AND máscara; broadcast = IP OR NOT máscara; hosts = 2ʰ − 2), clases y direcciones especiales/privadas, **campos del header IP** (prioridad y bits D/T/R del Tipo de Servicio, opciones *registro de ruta* y *marca de tiempo*, fragmentación), **ARP/ICMP** con ping y tracert, y **ruteo**: tabla de ruteo, ruta default, Sistema Autónomo, IGP, métrica, RIP vs OSPF, áreas, BGP.

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
| Differentiated Services (ex **Tipo de Servicio**) | 1 byte | QoS: 6 bits clase de servicio + 2 bits congestión (ECN). Lectura original en el recuadro de abajo |
| Total Length | 2 bytes | Largo total en bytes; máx **65.535 = 2¹⁶−1** |
| Identificación | 2 bytes | Junto con origen, destino y protocolo identifica al datagrama. **Todos los fragmentos llevan la misma** |
| Flags | 3 bits | 1 sin uso + **DF** (*Don't Fragment*; "NF" en el apunte): 1 = prohibido fragmentar; si hace falta, se descarta + **MF** (*More Fragments*): 1 = faltan fragmentos, 0 en el último |
| Fragment Offset | 13 bits | Posición del fragmento dentro del datagrama original, **en unidades de 8 bytes** (64 bits). Por eso todo fragmento menos el último lleva datos múltiplos de 8. Máx **8191** |
| TTL (Time to Live) | 8 bits | −1 por router; máx **255 saltos**; a 0 se descarta y se manda **ICMP tipo 11 (tiempo excedido)** al origen (evita loops) |
| Protocol | 8 bits | Qué lleva en el campo de datos: **1 = ICMP, 2 = IGMP, 6 = TCP, 17 = UDP** |
| Header Checksum | 16 bits | Verifica **solo el header** (los datos los controlan las capas superiores); se recalcula en cada router porque cambia el TTL. El apunte lo llama "CRC cabecera", pero es una **suma de comprobación** (complemento a uno), no un CRC |
| Source / Destination | 32 bits c/u | IP origen / destino |
| Opciones + Relleno | 0–40 bytes | Opcionales; el relleno completa hasta múltiplo de 32 bits |

> **Tipo de Servicio, lectura original (RFC 791, la que usa el apunte de Baró y la que pregunta la guía):**
> - **Prioridad / Precedencia** (3 bits): 0 = baja … 7 = máxima. **Es el subcampo que indica la prioridad del datagrama.**
> - **Bit D** (*Delay*): pide **bajo retardo** ("enviar rápido").
> - **Bit T** (*Throughput*): pide **alto rendimiento**, o sea mucho caudal en el menor tiempo ("enviar mucho").
> - **Bit R** (*Reliability*): pide **alta confiabilidad**, o sea minimizar pérdida o daño ("enviar bien").
> - 2 bits sin uso.
>
> D/T/R son **sugerencias**: cada router las puede respetar o ignorar. Hoy ese byte se redefinió como **DiffServ (6 bits) + ECN (2 bits)**.

- **Opciones** (raramente usadas; pensadas para pruebas y depuración de red):
  - **Seguridad:** indica qué tan secreto es el datagrama.
  - **Ruteo estricto desde el origen** (*strict source routing*): el emisor da el camino completo.
  - **Ruteo libre desde el origen** (*loose source routing*): el emisor da una lista de routers por los que no debe dejar de pasar.
  - **Registro de ruta** (*record route*): cada router que atraviesa agrega su IP. Sirve para **ver qué camino siguió el paquete**, por ejemplo para depurar ruteo. Como el espacio de opciones es chico, entran pocas direcciones (≈9).
  - **Marca de tiempo** (*timestamp*): como registro de ruta, pero cada router agrega también **su IP y una marca de 32 bits con la hora**. Sirve para medir demoras por tramo.
  - Estas dos opciones de diagnóstico se usan con mensajes **ICMP**: `ping -r` manda un *echo* con *record route*; además existen los tipos ICMP 13/14 (*timestamp*).

##### Fragmentación (MTU)
- **MTU:** la mayor cantidad de datos que entra en una trama de esa red (Ethernet **1500 B**; Token Ring 8192 B). Si el próximo tramo tiene una MTU menor que el datagrama, **el router lo fragmenta**. Cada fragmento es un datagrama nuevo con **la misma Identificación**, su propio Offset y su propio MF.
- **Solo el destino reensambla.** Los routers intermedios no lo hacen, porque les costaría trabajo y memoria. Los fragmentos pueden llegar desordenados sin problema. Si **DF = 1** y hace falta fragmentar, el router **descarta** el datagrama.
- *Ejemplo del apunte:* A manda **1400 B de datos** (1420 B en total, con un header de 20 B). Cruza la red 1 (MTU 1500) sin cambios, pero la red 2 tiene **MTU 620**:

```
Fragmento  Long. total  Datos      Offset en bytes  Offset en el campo (÷8)  MF
1          620          0–599      0                0                        1
2          620          600–1199   600              75                       1
3          220          1200–1399  1200             150                      0
```
  ⚠️ El apunte escribe el desplazamiento **en bytes** (0, 600, 1200). En el campo real va **dividido por 8** (0, 75, 150). Si te piden el valor del campo, dividí por 8. Ojo: los datos de cada fragmento salvo el último tienen que ser múltiplo de 8 (600 sí lo es).

##### Direccionamiento
- Direcciones de **32 bits (4 bytes)** → **2³² ≈ 4.294 millones**. Se escriben en decimal separando bytes por punto. Cada interfaz (RJ-45) tiene su IP → un router tiene una IP por interfaz.
- **Prefijo de red (network) + host:** el prefijo (longitud variable) es igual para toda la red; los bits de la derecha distinguen al host. Se anota como *IP menor de la red* + `/bits`. *Ej.:* `128.208.2.0/24` (24 bits red, 8 bits host).
- **Máscara de subred:** todos 1 en el prefijo y 0 en la parte de host; `AND` entre máscara y una IP → da el prefijo de red. *Ej.:* `/24` → `255.255.255.0`.

##### Clases (hasta 1993, obsoleto) y CIDR (actual)
- **Clases:** prefijo **fijo** por clase; la clase se reconoce por los **primeros bits**.

| Clase | Primeros bits | Formato (r = red, h = host) | Rango del 1er byte | Redes | Hosts por red | Máscara por defecto |
|---|---|---|---|---|---|---|
| A | `0` | r.h.h.h | 0–127 | 128 | 16.777.214 | 255.0.0.0 (/8) |
| B | `10` | r.r.h.h | 128–191 | 16.384 | 65.534 | 255.255.0.0 (/16) |
| C | `110` | r.r.r.h | 192–223 | 2.097.152 | 254 | 255.255.255.0 (/24) |
| D | `1110` | grupo multicast | 224–239 | — | — | — |
| E | `1111` | reservadas, no se usan | 240–255 | — | — | — |

  Hosts utilizables = 2ʰ − 2, porque se restan la dirección de red y la de broadcast. Por eso la clase C da 254 y no 256.
- **CIDR (Classless InterDomain Routing):** agrupa prefijos en **superredes** (*route aggregation*, RFC 4632) → una sola entrada en la tabla del router para muchas subredes. Redujo los prefijos a ~200.000 en el mundo (por eso IPv4 "aguantó").

##### Direcciones especiales · subredes · NAT
- **Especiales:** su significado depende del host que las use.

| Bits de red | Bits de host | Significado | Ejemplo |
|---|---|---|---|
| todos 0 | todos 0 | Este host (se usa al bootear) | `0.0.0.0` |
| todos 0 | host | Ese host **dentro de mi red** | `0.0.0.10` |
| red | todos 0 | **La red** (no se asigna a un host) | `192.168.1.0` |
| todos 1 | todos 1 | Broadcast a **mi** red | `255.255.255.255` |
| red | todos 1 | Broadcast a **la red indicada** (*directed broadcast*) | `192.168.1.255` |
| 127 | cualquiera | **Loopback**: mi propio host; prueba que TCP/IP está instalado | `127.0.0.1` |

- **Públicas vs privadas:** las **públicas** son únicas y visibles en todo Internet; las asigna **ICANN** y se contratan. Las **privadas** solo son visibles dentro de la red propia: salen a Internet a través de un router/proxy/NAT con IP pública, y **desde Internet no se puede llegar a ellas**.
  - **Para qué sirven los rangos privados (pregunta de la guía):** permiten armar intranets **sin pedir ni pagar IPs públicas** y **sin chocar con ninguna dirección de Internet**, porque esos rangos nunca se asignan a hosts públicos. Además, cualquier organización puede reusar el mismo rango, lo que **ahorra direcciones IPv4**, y los hosts internos quedan **inaccesibles desde afuera**, que es una protección.
  - **Rangos por clase:** A `10.0.0.0`; B `172.16.0.0`–`172.31.0.0`; C `192.168.0.0`–`192.168.255.0`. En CIDR: `/8`, `/12` y `/16`.
- **Estáticas vs dinámicas:** una **estática** es siempre la misma; la usan los servidores para ser localizables. Una **dinámica** cambia en cada conexión: el ISP o el DHCP la presta mientras estás conectado, porque el ISP tiene más clientes que direcciones.
- **Intranet / extranet / Internet:** una intranet es una red privada TCP/IP; una extranet es la unión de dos o más intranets, por líneas dedicadas o a través de Internet; Internet es la mayor red pública TCP/IP.
- **Subred:** red dentro de otra; cada una con su prefijo → tablas de routers más chicas. Desventaja: si un host cambia de red debe cambiar su IP (la **MAC** no cambia nunca).
- **NAT (Network Address Translation):** el ISP traduce IPs **privadas** en una pública; las máquinas de una casa se distinguen por el **puerto** (16 bits; puertos 0–1023 reservados, ej. **80 = web**). Rangos privados: **10.0.0.0/8**, **172.16.0.0/12**, **192.168.0.0/16**. Crítica: viola el principio de que una máquina no debería cambiar su IP; con IPv6 se seguiría usando como **firewall**.

##### Subnetting a mano (núcleo del parcial práctico de Baró)
> Para el 1er parcial de Medin alcanzaba con entender qué son el prefijo, la máscara, CIDR y NAT. **Para Baró sí se calcula a mano**: la práctica de máscaras forma parte del temario.

- **Para qué sirve la máscara:** un host la usa para decidir si el destino está **en su misma subred**, y entonces entrega directo (ARP al destino), o **en otra**, y entonces se lo manda al **gateway/router** (ARP al gateway). Ningún host está aislado: todos tienen IP y máscara. Si no se especifica la máscara, se toma la de su clase.
- **Las tres operaciones:**

```
Dirección de red        = IP AND máscara
Dirección de broadcast  = IP OR (NOT máscara)
Hosts utilizables       = 2^(bits de host) − 2
Primer host = red + 1        Último host = broadcast − 1
```

- **Ejemplo (misma subred o no):** máscara 255.255.0.0.
```
148.120.33.110  10010100.01111000.00100001.01101110
255.255.0.0     11111111.11111111.00000000.00000000
AND →           148.120.0.0
148.120.33.89   AND → 148.120.0.0   misma subred: entrega directa
148.115.89.3    AND → 148.115.0.0   otra subred: va al router
```

- **Subnetting de una clase C:** se toman bits de host para hacer subredes.

```
Máscara           Último byte  Subredes  Hosts/subred  Saltos entre subredes
255.255.255.0     00000000         1         254        —
255.255.255.128   10000000         2         126        x.0, x.128
255.255.255.192   11000000         4          62        de 64 en 64
255.255.255.224   11100000         8          30        de 32 en 32
255.255.255.240   11110000        16          14        de 16 en 16
255.255.255.248   11111000        32           6        de 8 en 8
255.255.255.252   11111100        64           2        de 4 en 4  (enlaces punto a punto)
255.255.255.254   11111110       128           0        ninguna posible
```
  **Truco del salto:** salto = 256 − (byte interesante de la máscara). Las subredes arrancan en múltiplos del salto; el broadcast es el siguiente múltiplo − 1. Con un byte de máscara distinto de 0 o 255 también se parten redes A o B. Por ejemplo, 255.255.192.0 divide una clase B en 4 subredes de 2¹⁴ − 2 = 16.382 hosts.

> ⚠️ **Convención de la cátedra: subredes válidas = 2ⁿ − 2** (práctica IPv4 resuelta, `fuentes/Baro-2do-parcial/8 - Práctica IPV4 resuelto.pdf`). Así como en cada subred se descartan la dirección de red y la de broadcast, **la práctica descarta también la primera subred (la de bits de subred en 0, *subnet zero*) y la última (bits de subred en 1)**. Es la regla clásica de la RFC 950; hoy los equipos usan todas las subredes, pero **las respuestas de Baró salen con −2**:
> - /28 sobre una clase C da 16 bloques, de los cuales **14 son subredes válidas** con 14 hosts cada una (ej. 16).
> - /30 sobre una clase C da 64 bloques: **62 subredes** de 2 hosts (ej. 10).
> - Para pedir *n* subredes: el menor *k* tal que **2ᵏ − 2 ≥ n**. Para 10 subredes, k = 4 (14 ≥ 10); para 55, k = 6 (62 ≥ 55).
> - **Cómo se numeran:** en las tablas de la práctica, el bloque que empieza en la red base es el **N° 1**. En los ejercicios que piden "la subred N", tomé **subred N = base + N × salto** (el bloque 0, *subnet zero*, no cuenta como subred válida). Si en clase las numeran distinto, corré un salto.

- **Caso práctico del apunte (diseño):** una empresa tiene contratadas las públicas **194.143.17.8/29** (red .8, broadcast .15, máscara 255.255.255.248, 6 hosts útiles: .9 a .14) y necesita **3 servidores** (correo, web, proxy) **+ 20 PCs**.
  - **Red pública /29:** router .9 (gateway de los servidores), proxy .10, y web y correo en dos de las restantes (.11–.14). Los servidores y el router van con IP pública para ser accesibles desde Internet.
  - **Red privada 192.168.1.0/24:** las 20 PCs usan IPs privadas con **gateway 192.168.1.1**, que es la IP privada del **proxy**.
  - **El proxy tiene dos IPs**, una por red: deja salir a la red privada y **bloquea el acceso desde afuera**.
  - **Idea:** las IPs públicas son caras, así que solo se le dan a lo que tiene que verse desde Internet.

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

- **ICMP es de capa 3 (red)**, aunque viaja **encapsulado dentro de un datagrama IP** (campo Protocolo = 1). **Solo informa, no decide**: qué hacer queda en manos de las capas superiores. Si se pierde un mensaje ICMP **no se genera otro ICMP por eso**; simplemente se descarta.
- **Tipos ICMP** (campo de 8 bits al inicio del mensaje):

```
Tipo  Mensaje
0     Respuesta de eco (Echo Reply)            ← ping
3     Destino inaccesible
4     Disminución de tráfico (Source Quench)   ← en desuso
5     Redireccionar (cambio de ruta)
8     Solicitud de eco (Echo)                  ← ping
11    Tiempo excedido (TTL = 0)                ← tracert/traceroute
12    Problema de parámetros
13/14 Solicitud/Respuesta de marca de tiempo
17/18 Solicitud/Respuesta de máscara
(15/16 Solicitud/Respuesta de información: obsoletos)
```

- **PING:** manda **tipo 8**; el destino contesta **tipo 0**. Comprueba las capas **física, de enlace y de red** (cableado, placas, configuración IP) entre los dos hosts. **No dice nada de transporte ni de aplicación**: el correo puede fallar aunque el ping ande. Algunos hosts tienen el eco desactivado por seguridad.
  - **Diagnóstico** (A hace `ping B`):
    - **Respuesta:** el cableado, las placas y la configuración IP están bien, y el router intermedio, si hay uno, deja pasar el tráfico en los dos sentidos.
    - **Tiempo de espera agotado:** revisar el host B y el cableado hasta B. Si hay router, primero hacé ping al gateway.
    - **Host de destino inaccesible** (ICMP 3, lo devuelve el gateway): no hay camino. Revisá IP y máscara (¿A y B están en la misma red?) o el **gateway** configurado en A.
    - **Error:** TCP/IP mal instalado en A. Probá `ping 127.0.0.1`, que testea la pila TCP/IP pero **no la placa de red**.
  - En una red de redes se hace ping **router por router** para ubicar en qué tramo está la falla.
- **TRACERT / traceroute:** manda datagramas con **TTL = 1, 2, 3…** (por defecto hasta 30 saltos). Cada router que lleva el TTL a 0 descarta el paquete y devuelve un **ICMP 11**, y así revela su IP. El conjunto de respuestas arma la traza del camino. **Windows `tracert` usa ICMP echo; Unix `traceroute` usa UDP.** Si la comunicación se corta, muestra en qué salto.

##### ARP (Address Resolution Protocol)
- Traduce **IP → MAC** en la LAN. Si un host necesita la MAC de una IP, manda un **broadcast** preguntando "¿quién tiene tal IP?"; el dueño responde con su MAC. (RFC 826.) Si el destino está en otra red, se resuelve la MAC del **default gateway** (IP más baja de la red). Clave: las **IP origen/destino son fijas**, las **MAC cambian** en cada LAN.
- **Para qué se hace una petición ARP (pregunta de la guía):** para averiguar la **dirección física (MAC)** que corresponde a una IP dentro de la LAN, porque la trama Ethernet necesita la MAC de destino y el datagrama solo trae la IP. Si el destino está en otra red, se pregunta por la MAC del **router/gateway**.
- **Mecánica:** la **pregunta va por broadcast** y lleva la IP y la MAC de quien pregunta. La **respuesta va directa (unicast)** a quien preguntó.
- **Ejemplo:** A (192.168.0.10) le manda a B (10.10.0.7), que está en otra red. A pregunta por ARP la MAC de **R1** (192.168.0.1) y le manda la trama a esa MAC con el datagrama adentro (IP origen A, IP destino B). Del otro lado, R1 hace ARP para conocer la MAC de B. **Es el mismo datagrama viajando en dos tramas distintas.**
- **Tabla o caché ARP:** cada host guarda los pares IP↔MAC que va resolviendo, así no repite preguntas. Las entradas tienen un **tiempo de vida** y se borran al vencer, por si cambian la IP o la placa. **Optimización:** como todos escuchan el broadcast, el destino y las demás estaciones pueden anotar al que preguntó sin necesidad de preguntar ellos.
- **Trama Ethernet**, donde viaja el datagrama: preámbulo (8 B) | MAC destino (6 B) | MAC origen (6 B) | tipo (2 B) | datos (64–1500 B) | CRC (4 B).
- **BOOTP:** el mail de Baró dice que el apunte lo trata, pero **el apunte que llegó no lo incluye**. *Esto es conocimiento general, no sale de las fuentes:* es el **antecesor de DHCP** y asigna la configuración IP al arrancar, pero de forma **estática** (tabla fija que arma el administrador, sin arriendo). DHCP lo reemplazó. Para más detalle, ver Tanenbaum 5.6.4.

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

---

> **Práctica de Baró — Direcciones IP y máscaras de subred** (`fuentes/Baro-2do-parcial/Práctica Direcciones IP - Máscaras de Subred.docx`). Los resultados son los del apunte; los verifiqué a mano y tienen **una errata**, marcada abajo.

**P1) Red y broadcast con máscara por defecto, o la indicada:**
```
IP / máscara                    Red             Broadcast
18.120.16.250   (A, /8)         18.0.0.0        18.255.255.255
18.120.16.255   /255.255.0.0    18.120.0.0      18.120.255.255   (.255 al final es un host válido: el host es de 16 bits)
155.4.220.39    (B, /16)        155.4.0.0       155.4.255.255    ⚠️ el apunte dice 155.24.255.255: errata
194.209.14.33   (C, /24)        194.209.14.0    194.209.14.255
190.33.109.133  /255.255.255.0  190.33.109.0    190.33.109.255
```

**P2) Mi host es 192.168.5.65/24. ¿Qué significan estas direcciones?**
`0.0.0.0` es mi propio host · `0.0.0.29` es el host .29 de mi red, o sea 192.168.5.29 · `192.168.67.0` es la red 192.168.67.0 · `255.255.255.255` es broadcast a mi red (192.168.5.0) · `192.130.10.255` es broadcast a la red 192.130.10.0 · `127.0.0.1` es loopback, mi propio host.

**P3) Red y broadcast con máscaras no estándar.** Método: pasar a binario **solo el byte "interesante"**, el que en la máscara no es ni 0 ni 255.
```
IP / máscara                       Byte IP    Byte másc.  Red              Broadcast
190.33.109.133 /255.255.255.128    10000101   10000000    190.33.109.128   190.33.109.255
192.168.20.25  /255.255.255.240    00011001   11110000    192.168.20.16    192.168.20.31
192.168.20.25  /255.255.255.224    00011001   11100000    192.168.20.0     192.168.20.31
192.168.20.25  /255.255.255.192    00011001   11000000    192.168.20.0     192.168.20.63
140.190.20.10  /255.255.192.0      00010100   11000000    140.190.0.0      140.190.63.255
140.190.130.10 /255.255.192.0      10000010   11000000    140.190.128.0    140.190.191.255
140.190.220.10 /255.255.192.0      11011100   11000000    140.190.192.0    140.190.255.255
```
Con el truco del salto: /255.255.192.0 da salto 256 − 192 = 64 en el 3er byte, así que las subredes son .0, .64, .128 y .192. El 130 cae en [128, 192), con red .128.0 y broadcast .191.255.

**P4) Los hosts públicos de una empresa van de 194.143.17.145 a 194.143.17.158. ¿Red, broadcast y máscara?**
```
145 = 1001 0001
158 = 1001 1110
      ^^^^ los 4 bits en común son la parte de red; los últimos 4 son de host
red = 1001 0000 = 144     broadcast = 1001 1111 = 159
```
Red **194.143.17.144**, broadcast **194.143.17.159**, máscara **255.255.255.240** (/28, 14 hosts: .145 a .158 ✔).

**P5) Caso práctico de diseño** (194.143.17.8/29 + 20 PCs privadas detrás de un proxy): está resuelto en *Subnetting a mano*, más arriba.

---

> **Práctica de la cátedra — Direccionamiento IPv4 resuelto** (`fuentes/Baro-2do-parcial/8 - Práctica IPV4 resuelto.pdf`). Son 29 ejercicios, casi todos **multiple choice**. Los ej. 1 a 20 vienen resueltos en el original; los verifiqué con Python y están bien, salvo 4 erratas del desarrollo (no de la respuesta), marcadas abajo. Los ej. 21 a 28 venían **sin resolver**: los resolví yo, también verificados. El 29 repite el 3. Todos usan la convención **subredes válidas = 2ⁿ − 2** (ver *Subnetting a mano*). Los enunciados completos, en formato para practicar, están en `estudio/banco-ejercicios-2do-parcial.md`.

```
Ej  Enunciado (resumido)                                         Respuesta
1   Clase B en 8 subredes, 2500 hosts/subred: ¿máscara?          255.255.240.0 (/20: 14 subredes válidas, 4094 hosts)
2   ¿Cuáles binarias son clase B? (1er byte 128–191)             153.120.109.194 · 185.200.55.76 · 159.75.63.43
3   Máscara 255.255.224.0: ¿cuál no es de la misma subred?       172.16.63.51 (subred .32.0; las otras, .64.0)
4   191.168.10.11 en binario                                     10111111.10101000.00001010.00001011
5   00001010.10101001.00001011.10001011 en decimal               10.169.11.139
6   ¿Cuál es privada clase A?                                    00001010.… = 10.120.109.248
7   172.18.71.2 / 255.255.248.0: ¿red y broadcast?               red 172.18.64.0 · bc 172.18.71.255
8   ¿Qué máscara tiene prefijo /24?                              255.255.255.0
9   192.168.85.129 / 255.255.255.192: ¿red y broadcast?          red 192.168.85.128 · bc 192.168.85.191
10  192.168.1.0 con /30: ¿subredes y hosts?                      62 subredes de 2 hosts
11  156.233.42.56 (clase B) con 7 bits de subred                 126 subredes de 510 hosts (máscara 255.255.254.0)
12  Clase B con 500 hosts por subred                             255.255.254.0 (510 hosts)
13  172.16.45.14/30: ¿subred?                                    172.16.45.12
14  Asignables en la subred de 192.168.15.19/28                  .17 y .29 (subred .16–.31)
15  Clase C, 10 subredes con el máximo de hosts                  255.255.255.240 (14 subredes × 14 hosts)
16  /28 sobre 210.10.2.0: ¿subredes y nodos?                     14 subredes y 14 nodos
17  172.16.210.0/22: ¿subred?                                    172.16.208.0 (hasta .211.255)
18  Binario a decimal (A, B, C)                                  100.10.235.39 · 172.18.158.15 · 192.167.178.69
19  Sobre esas 3: ¿qué es cierto?                                A pública clase A · B privada clase B · C pública clase C
```
**Erratas del original (solo en el desarrollo):** ej. 1 dice "/19" y 255.255.240.0 es **/20**; ej. 7 dice "/20" y escribe la máscara en binario como `11110000`, pero 255.255.248.0 es **/21** = `11111000`; ej. 3 y 13 escriben "172.168…" por **172.16…**. Ej. 19, opción C: 192.**167**.x.x es pública (el rango privado de clase C es 192.**168**).

**Ej. 21–28, resueltos (no venían resueltos).** Método: la máscara dada define la **red base** (IP AND máscara); se agregan bits de subred o se dejan bits de host según lo pedido; **subred N = base + N × salto**; **host H de una subred = dirección de la subred + H**.
```
21  6 subredes, 180.10.1.0 / 255.255.254.0
    base 180.10.0.0/23 · 2³−2 = 6 ≥ 6 → 3 bits → /26 (salto 64)
    subredes 1–6: 180.10.0.64 · 0.128 · 0.192 · 1.0 · 1.64 · 1.128
22  Subredes de ≥120 hosts, 172.15.35.0 / 24
    7 bits de host → /25 → 172.15.35.0/25 y 172.15.35.128/25 (126 hosts c/u)
    Ojo: con la regla 2ⁿ−2 un solo bit de subred no da ninguna subred válida; acá hay que usar las dos.
23  ≥100 subredes, 10.0.0.0/8
    2⁷−2 = 126 → 7 bits → /15 (255.254.0.0, salto 2 en el 2do byte)
    subred 39 = 10.78.0.0 · 76 = 10.152.0.0 · 87 = 10.174.0.0 · 99 = 10.198.0.0
24  ≥2000 hosts, 153.15.0.0 / 255.255.192.0
    base /18 · 11 bits de host → /21 (salto 8 en el 3er byte) · 2³−2 = 6 subredes válidas
    a) host 1312 (el enunciado no dice de qué subred; tomando la 1): 153.15.8.0 + 1312 = 153.15.13.32
    b) host 287 de la subred 5: 153.15.40.0 + 287 = 153.15.41.31
    c) host 1898 de la subred 6: 153.15.48.0 + 1898 = 153.15.55.106
25  ≥30 subredes, 190.10.0.0 / 255.255.192.0
    base /18 · 2⁵−2 = 30 → 5 bits → /23 (salto 2 en el 3er byte)
    subred 15 = 190.10.30.0 · 20 = 190.10.40.0 · 30 = 190.10.60.0
26  ≥500 hosts, 172.15.0.0 / 255.224.0.0
    base = 172.15.0.0 AND 255.224.0.0 = 172.0.0.0/11 · 9 bits de host → /23 (bloques de 512)
    a) host 254 de la subred 3854: 172.30.28.254
    b) host 64 de la subred 198:   172.1.140.64
    c) host 487 de la subred 2670: 172.20.221.231
27  ≥12 hosts, 201.154.10.0 / 255.255.255.224
    base /27 · 4 bits de host → /28 (salto 16) · 1ª subred = .0, 2ª = .16
    1ª: hosts 4, 7, 9 = .4 · .7 · .9      2ª: hosts 3, 8, 11 = .19 · .24 · .27
28  172.30.0.0/16, hoy 25 y a futuro 55 subredes de ≥1000 hosts
    2⁶−2 = 62 ≥ 55 → /22 → 1022 hosts ≥ 1000 → 255.255.252.0 (opción C)
```
Para pasar de "host H" a la dirección: H = 256·q + r → se suma q al 3er byte y r al 4to. Por ejemplo, 1312 = 5·256 + 32, así que 153.15.8.0 + 1312 = 153.15.13.32.

---

> **Guía de Estudio de Baró — preguntas tipo de parcial** (`fuentes/Baro-2do-parcial/GUIA DE ESTUDIO DE CAPA DE RED.docx`). Baró dice que **complementan la práctica de problemas**. Al lado de cada pregunta está **dónde está la respuesta en esta wiki**; las marcadas con 🔶 no tienen desarrollo suficiente en las fuentes actuales y requieren Tanenbaum (ver Dudas).

*Protocolo IP – Direcciones IP – Subnetting*
1. ¿Qué campo/subcampo de la cabecera IP indica la **prioridad**? → Tipo de Servicio, subcampo **Prioridad (3 bits)**. Ver *Encabezamiento IPv4*.
2. ¿Qué finalidad tiene el **bit T** del Tipo de Servicio? → pedir **alto throughput**. Ver *Encabezamiento IPv4*.
3. ¿Para qué sirve la opción **registro de ruta**? → registra las IP de los routers por los que pasa, para depurar el camino. Ver *Encabezamiento IPv4*, Opciones.
4. ¿Para qué se definen **rangos privados** en cada clase? → Ver *Direcciones especiales · subredes · NAT*.

*Protocolos de Control de Internet*
1. ¿Con qué finalidad se hace una **petición ARP** en una LAN? → Ver *ARP*.
2. ¿A qué capa OSI pertenece **ICMP**? → **Capa 3 (red)**, aunque viaja dentro de IP. Ver *ICMP*.
3. Con las opciones **registro de ruta** y **marca de tiempo**, ¿qué protocolo de control se usa? → **ICMP**. Ver *Encabezamiento IPv4*, Opciones.

*Protocolos de Ruteo*
1. Defina **ruteo** en Internet. → Ver *Ruta Óptima Origen-Destino*. 🔶 Falta una definición formal (Tanenbaum 5.2).
2. ¿Qué es una **tabla de ruteo**? ¿Quién la arma? → 🔶 Solo mencionada ("tabla interna" del router).
3. ¿Qué es una **ruta default** y por qué existe en la tabla? → 🔶 No está desarrollado.
4. ¿Qué es un **Sistema Autónomo** y cómo está conformado? → Mencionado en *Estructura de Internet* y *OSPF/BGP*. 🔶 Falta la definición.
5. ¿Qué es un **IGP**? Funciones y entorno. → OSPF y RIP son intradominio. 🔶 Falta el término "IGP" y sus funciones.
6. Diferencia operativa entre **vector distancia** y **estado de enlace**. → Ver *Vector Distancia* y *Estado de Enlaces*.
7. ¿Qué es una **métrica**? Ejemplos. → Saltos, retardo, costo y ancho de banda; ver *Ruta Óptima* y *Estado de Enlaces*.
8. ¿En qué entorno trabaja **RIP**? → Vector distancia, **intradominio (IGP)**, para redes chicas (máx. 15 saltos). 🔶 Ampliar con Tanenbaum.
9. Principios de **OSPF** y ventajas sobre vector distancia. → Ver *Estado de Enlaces* y *OSPF*.
10. ¿Qué significa que OSPF reconoce **jerarquías de ruteo**? → Áreas + backbone (área 0). Ver *OSPF*. 🔶 Ampliar.
11. ¿Qué es un **área** y qué **tipos de áreas** hay? → 🔶 Solo backbone/área 0; faltan los tipos (backbone, stub, etc.).
12. ¿En qué consiste **BGP**, en qué entorno se aplica y qué filosofía usa? → Ver *BGP*: interdominio, políticas, path vector.
13. ¿Cómo se componen los **paquetes de estado de enlace** en OSPF? → 🔶 No está desarrollado (identidad del emisor, nº de secuencia, edad y lista de vecinos con costos; Tanenbaum 5.2.5).
14. ¿Qué es un **grafo** en OSPF y para qué se arma? → 🔶 No está desarrollado. Es el mapa de la topología armado con los LSP, sobre el que se corre Dijkstra.
15. ¿Cuáles son los **5 pasos** de OSPF para aprender y difundir rutas óptimas? → Ver *Estado de Enlaces*, los 5 pasos.

#### Dudas / pendientes
- Confirmar con Medin si toma el **diagrama de ISP** dibujado a mano o basta describirlo.
- **2do parcial Baró:** faltan las secciones de **Tanenbaum 5.2.1–5.2.5, 5.6.6 y 5.6.7**, base de las preguntas 🔶 de ruteo de la guía: tabla de ruteo, ruta default, SA, IGP, tipos de área, LSP, grafo. **No hay PDF del libro en el repo.** Baró ofrece mandarlo si se le pide; si no, mirar `archivo/Resumenes/` ("Resumen Tanenebaum.pdf", "Redes Resumen 2024 Parcial 2.pdf", "Resumen para 2º parcial") y copiar lo útil a `fuentes/`.
- **Inundación (*flooding*) como algoritmo de ruteo (5.2.3):** acá solo aparece como método de broadcast. Falta desarrollarla como algoritmo de ruteo en sí.
- **BOOTP:** el mail lo anuncia en el apunte, pero el apunte que llegó no lo trae.
- **Erratas del apunte de Baró:** (a) dice que un ping a un host inexistente devuelve "ICMP tipo 11". En la práctica, si el host no contesta **no llega ningún ICMP** y el ping solo muestra "tiempo de espera agotado"; el tipo 11 aparece cuando el TTL llega a 0. (b) Llama "CRC" al checksum del header. (c) Escribe el desplazamiento de fragmento en bytes en vez de en unidades de 8 bytes. (d) La errata de P1 (155.24 por 155.4).
- **Diferencia entre fuentes:** el apunte de Baró describe el byte 2 del header como **Tipo de Servicio** (prioridad + D/T/R); las diapositivas de Medin y Tanenbaum 5ª ed. lo describen como **Differentiated Services + ECN**. Para el parcial de Baró, contestá con la versión de ToS, que es la que pregunta la guía.

#### Fuentes
- `fuentes/RD/Medin-1er-parcial/1 - Capa de Red - Servicios y distribución.pdf`
- `fuentes/RD/Medin-1er-parcial/2 - Capa de Red - Ruta óptima origen-destino.pdf`
- `fuentes/RD/Medin-1er-parcial/3 - Capa de Red - IPv4.pdf`
- `fuentes/RD/Medin-1er-parcial/4 - Capa de Red - Control de Congestión.pdf`
- `fuentes/RD/Medin-1er-parcial/6 - Capa de Red - Protocolos de control.pdf`
- `fuentes/RD/Medin-1er-parcial/Capa de Red.pdf` (compilado de los anteriores)
- `fuentes/Baro-2do-parcial/mails-temario-y-fechas.md` (temario por páginas de Tanenbaum + fechas del 2do parcial)
- `fuentes/Baro-2do-parcial/Apunte 2do parcial (Capa de Red).docx` (TCP/IP, direcciones, máscaras, datagrama IP, fragmentación, ARP, ICMP, ping, tracert)
- `fuentes/Baro-2do-parcial/Práctica Direcciones IP - Máscaras de Subred.docx` (es un extracto del apunte: §2.2–2.3 + ejercicios)
- `fuentes/Baro-2do-parcial/GUIA DE ESTUDIO DE CAPA DE RED.docx` (preguntas tipo de parcial)
- `fuentes/Baro-2do-parcial/8 - Práctica IPV4 resuelto.pdf` (práctica de la cátedra: 29 ejercicios de direccionamiento IPv4; del Drive, `archivo/Material de Cursado/Práctica/`)
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
- 2026-10-05: Ingesta del material del **2do parcial práctico de Baró** (dos mails reenviados por Gonza + el de fechas de Medín). Fuentes en `fuentes/Baro-2do-parcial/`: los mails, apunte de Capa de Red, práctica de máscaras de subred y guía de estudio. Unidad 2: nuevo bloque de alcance y fechas (práctica el 21/10 y teoría el 27/10 para el grupo A–Fassine); header IPv4 ampliado con Tipo de Servicio (prioridad, D/T/R), números de protocolo, opciones y fragmentación con ejemplo; tabla de clases y de direcciones especiales; utilidad de los rangos privados; nueva sección *Subnetting a mano* con el caso práctico; tipos ICMP, diagnóstico con ping y tracert; caché ARP; práctica de máscaras resuelta y verificada; guía de Baró mapeada a la wiki. Pendiente: Tanenbaum 5.2/5.6.6/5.6.7 para las preguntas de ruteo marcadas 🔶.
- 2026-10-05: Ingesta de la **práctica IPv4 resuelta** de la cátedra (del Drive). Unidad 2: convención **subredes válidas = 2ⁿ − 2** en *Subnetting a mano*; ejercicios 1–20 verificados (4 erratas de desarrollo marcadas) y 21–28 resueltos (no venían resueltos). Banco nuevo: `estudio/banco-ejercicios-2do-parcial.md`.
