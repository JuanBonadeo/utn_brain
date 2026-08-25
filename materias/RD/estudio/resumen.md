# Redes de Datos — Resumen 1er Parcial (Prof. Medin)

> Abarca **dos capas del modelo OSI**: **Enlace** y **Red**. *(Capa de Transporte quedó fuera de este parcial.)* El examen es **multiple choice, 10 preguntas**, conceptual (no numérico). La idea de este resumen es que puedas **explicar y reconocer** cada tema.

**Ubicación de las capas (de abajo hacia arriba):** Física (1) → **Enlace (2)** → **Red (3)** → Transporte (4) → Aplicación. Cada capa usa el servicio de la de abajo y le brinda un servicio nuevo a la de arriba. Un dato que conviene tener claro: la unidad de información cambia de nombre según la capa → **trama** (capa 2) y **paquete** (capa 3).

---

## 1. Capa de Enlace (capa 2)

### Funciones y estructura de la trama
La capa de enlace toma el "chorro" de bits que le entrega la capa física y lo organiza para que sea confiable. Sus dos tareas centrales son el **control de errores** (detectar/corregir bits dañados) y el **control de flujo** (que el emisor no mande más rápido de lo que el receptor puede procesar).

Para eso corta la cadena de bits en **tramas**. Una trama tiene tres partes:
- **Header (encabezamiento):** bits al inicio que sirven para reconocer dónde empieza la trama y qué direcciones (origen/destino) tiene.
- **Datos:** la información que viene de las capas superiores.
- **Trailer (bits de cola):** van al final, principalmente para el **control de errores** (checksum/CRC).

El protocolo de enlace tiene que ser **el mismo en emisor y receptor** para que puedan "entenderse".

### Framing (cómo separar la cadena de bits en tramas)
El problema es: ¿cómo sabe el receptor dónde termina una trama y empieza la siguiente? Hay tres técnicas:

1. **Contar bytes:** el header indica cuántos bits mide la trama. **No se usa en la práctica**, porque si ese número llega con un error, el receptor pierde el sincronismo y ya no sabe dónde cortar; peor aún, cuesta recuperarse.
2. **Flag (bandera) de inicio:** se usa un patrón fijo de bits, conocido por el receptor, para marcar el comienzo de cada trama. Es el método **más usado**. El problema es qué pasa si ese mismo patrón aparece por casualidad en los datos; se resuelve así:
   - **Byte-stuffing:** antes del byte "problemático" se inserta un byte especial de escape (**ESC**), que el receptor sabe quitar. Lo usa el protocolo **PPP**.
   - **Bit-stuffing:** en vez de bytes se insertan bits de relleno. Lo usa **HDLC**, cuyo flag es `01111110` (un 0, seis 1, un 0): si el emisor detecta un 0 seguido de cinco 1 en los datos, mete un 0 para "romper" la falsa bandera. También lo usa el **USB**. Ventaja extra: agrega transiciones que ayudan a la capa física a no perder sincronismo.
3. **Violación de la codificación:** en codificaciones como **4B/5B** hay combinaciones de bits que no representan ningún dato válido; se usa una de esas combinaciones "prohibidas" para marcar inicio/fin. Lo usan **FDDI** y **Fast-Ethernet**.

### Tipos de servicio
Según cuánta garantía ofrezca, el servicio de capa 2 puede ser:
- **Orientado a conexión:** se arma un circuito virtual con **3 fases** (establecimiento, intercambio de datos, desconexión). Se usa en canales largos y poco confiables. *Ej.: enlace satelital / telefónico de larga distancia* (en el establecimiento se mide la tasa de error para ver si conviene comunicar).
- **Sin conexión "best-effort":** el más simple, sin control ni retransmisiones. Sirve si el canal es muy confiable o si es tráfico en tiempo real (no tiene sentido retransmitir un píxel o un instante de voz que ya pasó). *Ej.: Ethernet* — si se pierde una trama, la capa 2 ni se entera; lo resuelven las capas superiores.
- **Sin conexión pero con confirmación:** cada trama se numera y el receptor confirma su llegada; si no llega, se reenvía. Es imprescindible en medios ruidosos. *Ej.: WiFi (802.11).*

### Control de flujo por ventana deslizante
La idea general: el emisor puede tener varias tramas "en el aire" sin haber recibido aún su confirmación (ACK). Ese conjunto de tramas pendientes es la **ventana**. Hay tres esquemas:

| Método | Ventana | Ante un error, el emisor… | El receptor… | Memoria RX | Eficiencia |
|---|---|---|---|---|---|
| **Stop-and-Wait** | 1 | reenvía la única trama pendiente (cuando expira su timeout) | espera y confirma **cada** trama antes de la siguiente | mínima | baja |
| **Go-Back-N** | N | reenvía **desde la trama que falló en adelante** | **descarta** todo lo que llega fuera de orden | mínima | media |
| **Selective Repeat** | N | reenvía **solo la trama que falló** | **guarda** las que llegan fuera de orden y usa ACK acumulativo | alta | alta |

- **Stop-and-Wait** desperdicia el canal cuando la propagación es grande (satélite): el emisor pasa mucho tiempo esperando el ACK sin transmitir.
- **Go-Back-N** es más simple para el receptor (no guarda nada) pero reenvía de más.
- **Selective Repeat** aprovecha mejor el canal pero exige más memoria en el receptor.
- **Regla importante:** el **contador de secuencia debe ser el doble del tamaño de la ventana**. Si no, ante un reenvío el receptor podría confundir tramas repetidas con tramas nuevas.
- **Piggybacking:** para ser eficiente, el receptor no manda un ACK "solo"; lo monta **dentro de otro mensaje** que ya iba de vuelta hacia el emisor, aprovechando el viaje.

---

## 2. Capa de Red (capa 3)

### Servicios y distribución
La capa de red se encarga de llevar **paquetes** desde el origen hasta el destino final atravesando **varias redes**. Su elemento clave es el **router**, que recibe cada paquete, lo revisa y lo reenvía al puerto de salida correcto según su **tabla interna**.

Ofrece dos tipos de servicio:
- **Datagrama (sin conexión):** cada paquete viaja independiente y puede llegar desordenado; no hay un "establecimiento de llamada" previo. Es el modo del **protocolo IP**, la base de Internet.
- **Circuito virtual (orientado a conexión):** primero se fija **una única ruta** (el CV) y recién después se mandan los paquetes por ahí. Tiene **3 etapas** (establecimiento → intercambio → desconexión). El router necesita más memoria para recordar cada circuito.

**Las 4 formas de transmitir un mensaje en capa 3** (pregunta clásica):
- **Unicast** — uno a uno (una IP específica). Ej.: navegar una web.
- **Broadcast** — uno a todos en la red local. Ej.: DHCP Discover. Solo en IPv4.
- **Multicast** — uno a un grupo suscripto a una dirección multicast. Ej.: streaming de video.
- **Anycast** — uno al **más cercano** de un grupo; la red entrega al nodo más próximo según la métrica. Muy usado en IPv6 y en el **DNS**.

Para hacer **broadcast** de forma eficiente se usa el **sink tree** (árbol de menor costo desde un router a todos los demás) y **RPF (Reverse Path Forwarding):** si el paquete llegó por el enlace que pertenece al árbol óptimo, se reenvía; si no, se descarta (es un duplicado). El **multicast** se logra podando ese árbol para dejar solo al grupo (protocolo **PIM**).

### Ruteo (encontrar la ruta óptima)
La tarea central de la capa 3 es decidir por dónde mandar cada paquete. Los algoritmos son **dinámicos/adaptativos** (se ajustan al estado de la red):
- **Dijkstra (paso más corto):** calcula el camino de menor costo según una métrica (retardo, costo económico, saltos), no la distancia geométrica.
- **Vector Distancia** (Bellman-Ford, usado por **RIP**): cada router guarda en su tabla la distancia hacia todos los demás y la comparte con sus vecinos. Su gran problema es la **cuenta a infinito**: cuando un nodo cae, la noticia se propaga muy lento y el número de saltos crece indefinidamente; se mitiga poniendo un valor bajo como "infinito". *Regla: las buenas noticias se propagan rápido, las malas lento.*
- **Estado de Enlaces** (usado por **OSPF** e **IS-IS**): cada router averigua a sus vecinos, mide el costo a cada uno, arma un mensaje y lo **inunda a toda la red**; con esa foto completa calcula el mejor camino. Consume **más memoria y CPU**, pero **converge más rápido** y con información más precisa.
- **Extras:** jerarquías por regiones (cada router solo conoce su región → tablas más chicas) · usuarios móviles (**Home Agent** en la casa + **Care-of-Address** en el lugar visitado + **tunneling**) · redes ad-hoc **MANETs**, donde los propios nodos son routers (AODV, DSR, GPSR).

### IPv4 y direccionamiento
El **protocolo IP** es el que une toda Internet. La dirección IPv4 tiene **32 bits** (4 bytes en decimal separados por puntos). El header del paquete mide **entre 20 y 60 bytes** (20 fijos + opciones). Campos que conviene tener claros:
- **Total Length:** largo total del paquete, máximo **65.535 bytes** (2¹⁶−1).
- **TTL (Time to Live):** se resta 1 en cada router; al llegar a 0 el paquete se descarta y se avisa al origen. **Sirve para evitar que un paquete quede dando vueltas para siempre** (por ejemplo, si se corrompió una tabla de ruteo).
- **Protocol:** indica qué protocolo de capa 4 viaja adentro (TCP o UDP).
- **Header Checksum:** detecta errores del header y **se recalcula en cada router**, justamente porque el TTL cambió.
- **Fragmentación:** bits **DF** (no fragmentar), **MF** (faltan fragmentos) y **Fragment Offset** (número de fragmento).

**Cómo se estructura una dirección:** un **prefijo de red** (a la izquierda, igual para toda la red) + una parte de **host** (a la derecha, distinta por usuario). La **máscara de subred** tiene todos 1 en el prefijo y 0 en el host; haciendo un **AND** entre la máscara y una IP se obtiene el prefijo de red. Con **CIDR** (*Classless InterDomain Routing*) se agrupan varias redes en una **superred** de una sola entrada en la tabla del router (*route aggregation*); esto evitó que se agotaran las IPv4.
- Clases (ya obsoletas): A / B / C / **D = multicast** / E = uso futuro.
- **Direcciones especiales:** `0.0.0.0` (booteo / la propia red), `255.255.255.255` (broadcast local), `127.x.x.x` (loopback, no sale a la red).
- **Rangos privados:** `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`.
- **NAT (Network Address Translation):** como las IP públicas escasean, se usan IP **privadas** dentro de la casa/empresa y el ISP las **traduce** a una pública; las máquinas se distinguen por el **número de puerto**. Además funciona como una especie de **firewall** (bloquea lo entrante). Se lo critica porque viola el principio de que una máquina no debería cambiar su IP.

### Control de congestión (5 etapas)
**Congestión = retardo excesivo por demasiados paquetes en tránsito.** La gestionan en conjunto la capa 3 y la 4. Un detalle contraintuitivo: **más memoria en los routers no ayuda** (Nagle, 1987), porque los paquetes esperan tanto en la cola que igual se retransmiten y empeoran todo. Diferencia clave: el **control de flujo** es entre un solo emisor y un solo receptor; la **congestión** involucra muchos nodos a la vez.

Las 5 etapas (en orden, de prevención a último recurso):
1. **Planificación** (*network provisioning*) — anticiparse: reforzar routers/enlaces antes de que se saturen. Es preventivo y lento (meses).
2. **Ruteo según tráfico** (*traffic-aware routing*) — desviar tráfico por rutas menos cargadas; el peso del enlace incluye una parte fija + una variable (el tráfico). Riesgo: **oscilación** (todos se van a la ruta libre y la saturan) → se resuelve con *multipath routing*.
3. **Admisión de circuitos virtuales** (*admission control*) — no permitir crear CV nuevos que pasen por la zona congestionada.
4. **Atenuación de fuentes** (*traffic throttling*) — pedirle a las fuentes que bajen el tráfico. Tres técnicas:
   - el router congestionado **avisa directo al emisor** con un paquete;
   - el router **marca** el paquete y el **receptor** avisa a la fuente (paquete **"choke"** = **ECN**, no carga a los routers pero es más lento);
   - **hop-by-hop backpressure**: cada router avisa hacia atrás al anterior (la técnica **más rápida**, pero **carga de trabajo** a los routers).
5. **Descarte de paquetes** (*load shedding*) — último recurso: tirar paquetes (mejor que colapsar). El algoritmo **RED** descarta antes de llenar el buffer. Qué tirar primero: en archivos, los **últimos** paquetes; en streaming, los **más viejos**; y **nunca** los paquetes de control (son los más importantes).

### Protocolos de control
Además de IP (que transporta los datos), hay protocolos que **controlan** el tráfico. Sus mensajes suelen viajar de router a router.

| Protocolo | Para qué sirve |
|---|---|
| **ICMP** | Informa **errores** y hace diagnóstico: destino inalcanzable, tiempo excedido (TTL a 0), problema en parámetro, bajar tráfico de fuente (*source quench*), ruta alternativa, echo. Lo usan **ping** (echo) y **traceroute** (mandando TTL = 1, 2, 3…). |
| **ARP** | Traduce una **IP en su dirección MAC** dentro de la LAN, preguntando por **broadcast** "¿quién tiene tal IP?". Clave: las IP origen/destino son fijas, las MAC cambian en cada red. |
| **DHCP** | Asigna una **IP dinámica** automáticamente (por broadcast) junto con gateway y DNS. La IP tiene un tiempo de arriendo que expira o se renueva. |
| **MPLS** | Rutea por una **etiqueta (label)** en vez de por la IP → más rápido. Se lo ubica como **"capa 2,5"**; usa routers especiales **LSR**. |
| **OSPF** | Protocolo **intradominio** (dentro de un Sistema Autónomo). Usa **estado de enlaces**. Divide el SA en **áreas** conectadas a un **backbone (área 0)**. |
| **BGP** | Protocolo **interdominio** (entre Sistemas Autónomos distintos). Maneja **políticas** (económicas, de seguridad); usa *path vector*; corre sobre **TCP**; soporta multihoming y peering. |

---

## Datos que conviene saber de memoria
- **Unidades:** trama (capa 2) · paquete (capa 3).
- El reenvío en las capas 1-2-3 es **salto a salto** (nodo a nodo vecino).
- **Framing:** byte-stuffing = **PPP** · bit-stuffing = **HDLC** · 4B/5B = **FDDI / Fast-Ethernet**.
- **Ventana deslizante:** contador de secuencia = **doble** de la ventana; en Go-Back-N el receptor **descarta** lo fuera de orden, en Selective Repeat lo **guarda**.
- **IPv4 = 32 bits** · **TTL máx. 255** · **Total Length máx. 65.535** · header 20–60 bytes.
- **Transmisión capa 3:** unicast · broadcast · multicast · anycast.
- **5 etapas de congestión:** provisioning → traffic-aware routing → admission control → traffic throttling → load shedding.
- **Protocolos de control:** ICMP (errores/diagnóstico) · ARP (IP→MAC) · DHCP (IP dinámica).
- **IP privadas:** 10/8, 172.16/12, 192.168/16.
- **Ruteo:** Vector Distancia → cuenta a infinito · Estado de Enlaces → converge más rápido · **OSPF** intradominio · **BGP** interdominio.
