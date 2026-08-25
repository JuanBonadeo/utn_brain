# Redes de Datos — Banco de Preguntas y Respuestas (1er Parcial, Prof. Medin)

> **Cómo usarlo:** tapá la respuesta e intentá responder de memoria. Las marcadas **[REAL]** fueron efectivamente tomadas por Medin (del documento original de parciales); las **[EXTRA]** son adicionales probables, en su mismo estilo conceptual, para cubrir temas que las reales no tocan (sobre todo Capa de Enlace, ruteo e IPv4).
>
> ⚠️ **El parcial cambió a multiple choice (10 preguntas) sobre Enlace + Red.** Para practicar el formato real usá `multiple-choice.md`. Las preguntas de **Capa de Transporte** (17-25) quedaron **FUERA de este parcial** (sirven para el final).

---

## Capa de Enlace

**1. [EXTRA] ¿Qué funciones cumple la capa de enlace y cómo está formada una trama?**
Hace **control de errores** y **control de flujo**. Toma los bits de la capa física, los corta en **tramas** y le brinda un servicio confiable a la capa de red. Una trama tiene: **header** (delimita el inicio + direcciones origen/destino), **datos** (de capas superiores) y **trailer / bits de cola** (para el control de errores, ej. checksum/CRC).

**2. [EXTRA] Enumere los métodos de separación en tramas (framing) y explique uno.**
Tres: ① **contar bytes** (el header dice el largo; *no se usa*, porque un error en ese dato desincroniza); ② **flag de inicio** (patrón fijo de bits que marca el comienzo; el más usado) con **byte-stuffing** (inserta un byte ESC — protocolo PPP) o **bit-stuffing** (inserta bits de relleno — HDLC, flag `01111110`); ③ **violación de codificación** (en 4B/5B se usa una palabra inválida — FDDI, Fast-Ethernet).
*Ejemplo (bit-stuffing en HDLC):* si el emisor ve un 0 seguido de cinco 1 en los datos, mete un 0 para romper la falsa bandera `01111110`; el receptor lo quita al decodificar.

**3. [EXTRA] Compare Stop-and-Wait, Go-Back-N y Selective Repeat.**
- **Stop-and-Wait:** ventana 1; manda una trama y espera su ACK. Simple pero desperdicia el canal si la propagación es grande.
- **Go-Back-N:** ventana N; ante un error reenvía **desde la trama que falló en adelante**; el receptor **descarta** todo lo que llega fuera de orden.
- **Selective Repeat:** ventana N; el receptor **guarda** las tramas fuera de orden y el emisor **reenvía solo la que falló** (usa ACK acumulativo). Es el más eficiente pero exige más memoria en el receptor.
- *Regla:* el contador de secuencia debe ser el **doble** del tamaño de la ventana.

**4. [EXTRA] ¿Qué es el piggybacking?**
Es enviar el **ACK montado dentro de otro mensaje** que ya iba de vuelta hacia el emisor, en vez de mandar una trama solo para confirmar. Aprovecha el viaje y mejora la eficiencia.

---

## Capa de Red

**5. [REAL] En la 3ra capa del modelo OSI existen distintas formas de transmitir un mensaje. Enumerar y desarrollar una.**
Cuatro: **Unicast** (uno a uno, a una IP específica — ej. navegar web), **Broadcast** (uno a todos en la red local — ej. DHCP Discover; solo IPv4), **Multicast** (uno a un grupo suscripto a una dirección multicast — ej. streaming), **Anycast** (uno al **más cercano**; la red entrega al nodo más próximo según la métrica — muy usado en IPv6 y en el DNS).

**6. [REAL] Realice un diagrama de capa 3 donde se observen los distintos tipos de ISP.**
Jerarquía en 3 niveles: **Tier 1** (backbones globales interconectados entre sí con *peering* sin costo de tránsito), **Tier 2** (ISP regionales/nacionales que compran a Tier 1 y redistribuyen), **Tier 3** (locales; conectan al usuario final: hogares, empresas, cable, WiMAX, Ethernet; dependen de Tier 2). Es de capa 3 porque muestra cómo se interconectan **routers** de distintos proveedores hasta el usuario final. *(Dibujar 3 franjas: Tier 1 arriba interconectados, Tier 2 colgando, Tier 3 y usuarios abajo.)*

**7. [REAL] Enumere las etapas de control de congestión y explique una.**
Las 5: ① **Planificación** (*network provisioning*), ② **Ruteo según tráfico** (*traffic-aware routing*), ③ **Admisión de circuitos virtuales** (*admission control*), ④ **Atenuación de fuentes** (*traffic throttling*), ⑤ **Descarte de paquetes** (*load shedding*).
*Planificación:* anticipar los cuellos de botella reforzando routers/enlaces de mayor capacidad **antes** de que se produzca la congestión (medida preventiva, a largo plazo).

**8. [REAL] ¿Qué protocolo da estos mensajes: destino inalcanzable, tiempo excedido, problema en parámetro, bajar tráfico de fuente, ruta alternativa?**
**ICMP** (Internet Control Message Protocol), capa 3, para diagnóstico y control de IP. *Destino inalcanzable:* el router no puede entregar el paquete. *Tiempo excedido:* el TTL llegó a 0. *Bajar tráfico de fuente:* pedir menor velocidad de envío (source quench). Lo usan **ping** (echo) y **traceroute**.

**9. [REAL] ¿Para qué se emplean los protocolos de control ARP, ICMP y DHCP?**
**ARP:** traduce una dirección **IP en su MAC** dentro de la LAN (pregunta por broadcast). **ICMP:** informa errores y hace diagnóstico (ping, traceroute). **DHCP:** asigna automáticamente **IP dinámica** y otros parámetros (gateway, DNS) a los dispositivos que se conectan.

**10. [EXTRA] Diferencie el servicio de datagrama (sin conexión) del de circuito virtual.**
**Datagrama:** cada paquete viaja independiente, puede llegar desordenado, sin establecimiento previo; cada paquete lleva IP origen y destino; ante una falla se cambia la ruta. Es el modo de **IP**. **Circuito virtual:** se fija una única ruta antes de enviar (3 etapas: establecimiento → intercambio → desconexión); cada paquete lleva solo el nº de CV; el router necesita memoria para el circuito; ante una falla, finaliza la comunicación.

**11. [EXTRA] Enumere los algoritmos de ruteo y explique el problema de la cuenta a infinito.**
**Dijkstra** (paso más corto), **Vector Distancia** (Bellman-Ford / RIP) y **Estado de Enlaces** (OSPF, IS-IS).
*Cuenta a infinito (propio del Vector Distancia):* cuando un nodo cae, la noticia se propaga muy lento; los routers siguen creyendo que lo alcanzan a través del vecino y el número de saltos **crece indefinidamente**. Se mitiga fijando un valor bajo como "infinito" (el máximo de saltos + 1). *Las buenas noticias se propagan rápido; las malas, lento.*

**12. [EXTRA] Compare Vector Distancia y Estado de Enlaces.**
**Vector Distancia:** cada router guarda la distancia a todos los demás y la comparte solo con sus vecinos; simple pero lento en converger y sufre la cuenta a infinito (RIP). **Estado de Enlaces:** cada router inunda a **toda la red** el costo de sus enlaces y con esa foto completa calcula el mejor camino; usa **más memoria y CPU** pero **converge más rápido** (OSPF, IS-IS).

**13. [EXTRA] ¿Para qué sirve el campo TTL del header IPv4 y por qué el checksum se recalcula en cada router?**
**TTL (Time to Live):** se resta 1 en cada router y, al llegar a 0, el paquete se descarta y se avisa al origen. Sirve para **evitar que un paquete quede dando vueltas para siempre** (por ejemplo, si se corrompió una tabla de ruteo). El **Header Checksum se recalcula en cada router** justamente porque el TTL cambió, y el checksum cubre el encabezamiento.

**14. [EXTRA] ¿Qué es NAT y qué rangos de IP privadas existen?**
**NAT (Network Address Translation):** como las IP públicas escasean, dentro de una red se usan IP **privadas** y el ISP las **traduce** a una pública; las máquinas se distinguen por el **número de puerto**. Funciona además como una especie de **firewall** (bloquea lo entrante). Rangos privados: **10.0.0.0/8**, **172.16.0.0/12** y **192.168.0.0/16**.

**15. [EXTRA] Explique las 3 técnicas de atenuación de fuentes (traffic throttling).**
① El router congestionado **avisa directo al emisor** con un paquete para que baje el tráfico. ② El router **marca** el paquete y es el **receptor** quien avisa a la fuente (paquete **"choke"** = **ECN**, no carga a los routers pero es más lento porque actúa recién al llegar al receptor). ③ **Hop-by-hop backpressure:** cada router avisa hacia atrás al router anterior, que reduce el tráfico enseguida; es la **más rápida** pero **carga de trabajo** a los routers.

**16. [EXTRA] Diferencie OSPF y BGP.**
**OSPF** es un protocolo **intradominio** (dentro de un mismo Sistema Autónomo), basado en **estado de enlaces**, que divide el SA en áreas conectadas a un backbone. **BGP** es **interdominio** (entre Sistemas Autónomos distintos), maneja **políticas** (económicas y de seguridad), usa **path vector** (tiene en cuenta el camino recorrido, detecta bucles) y corre sobre **TCP**.

---

## Capa de Transporte
> ⚠️ **FUERA del 1er parcial.** Estas preguntas (17-25) no entran en el parcial actual (Enlace + Red). Quedan para el final.

**17. [REAL] ¿Qué responsabilidades tiene la capa de transporte?**
Ofrecer comunicación **extremo a extremo** confiable y eficiente entre aplicaciones. Funciones: **dividir en segmentos y reensamblar**, entrega **ordenada y confiable** (en TCP), **control de errores**, **control de flujo** (ajustar la velocidad al receptor), **multiplexación por puertos** y **control de congestión** (solo TCP).

**18. [REAL] ¿Cómo controla la congestión el protocolo UDP?**
**No la controla.** UDP no implementa control de congestión ni de flujo: envía los datagramas al ritmo que indica la aplicación, sin adaptarse al estado de la red, por lo que puede saturarla. Si hace falta control, lo debe implementar la propia aplicación.

**19. [REAL] ¿Qué sucede si UDP detecta un error? ¿Y TCP?**
**UDP:** si el datagrama llega corrupto (detectado por checksum), simplemente lo **descarta**; no hay retransmisión ni recuperación. **TCP:** detecta el error y **retransmite** los segmentos perdidos o dañados hasta recibir el ACK de entrega correcta, manteniendo orden y confiabilidad.

**20. [REAL] Grafique un ejemplo de conexión 3-way handshake.**
`Cliente → SYN → Servidor`; `Servidor → SYN-ACK → Cliente`; `Cliente → ACK → Servidor`; y a partir de ahí, flujo bidireccional. El cliente inicia con **SYN** (ejecuta CONNECT), el servidor (en LISTEN) responde **SYN-ACK** indicando que puede empezar, y el cliente confirma con **ACK**.

**21. [REAL] Enuncie diferencias entre TCP y UDP.**
| | TCP | UDP |
|---|---|---|
| Conexión | Orientado a conexión (3-way handshake) | Sin conexión (envío inmediato) |
| Confiabilidad | Garantiza entrega y orden; retransmite | No garantiza nada |
| Flujo/congestión | Sí controla | No |
| Cabecera | 20+ bytes | 8 bytes |
| Servicio | Byte-stream (flujo de bytes) | Mensajes individuales |
| Usos | HTTP, FTP, correo, archivos | Voz/video, DNS, DHCP, multicast |

**22. [EXTRA] Enumere las primitivas (sockets) del servidor en TCP y su orden.**
`SOCKET` (crea el extremo de comunicación) → `BIND` (le asigna un **puerto** local) → `LISTEN` (reserva la cola de espera de clientes) → `ACCEPT` (acepta un pedido de conexión). El cliente usa `CONNECT` (no necesita BIND). El cierre es un `CLOSE` **simétrico** de ambos lados.

**23. [EXTRA] Explique el problema de los dos ejércitos y con qué se relaciona.**
Dos divisiones del ejército azul deben atacar **coordinadas** para vencer, pero se comunican por mensajeros que pueden ser capturados. El problema es que **nunca se puede estar 100% seguro de que el último mensaje llegó** (siempre falta la confirmación de la confirmación). Se relaciona con la **desconexión** en TCP: por eso la desconexión es un handshake de 3 vías y, si un mensaje se pierde, cada lado corta igual mediante un **timeout**.

**24. [EXTRA] ¿Qué es AIMD y cómo funciona el slow-start?**
**AIMD (Additive Increase, Multiplicative Decrease):** la ley de control de congestión de TCP; la ventana **sube de a poco** (incremento aditivo) y, cuando detecta una pérdida, **baja a la mitad** (decremento multiplicativo), logrando converger al punto óptimo. **Slow-start:** al comenzar, TCP **duplica** el tamaño de la ventana con cada ACK recibido (midiendo el RTT) hasta que aparece una pérdida; ahí achica la ventana a la mitad.

**25. [EXTRA] ¿Para qué sirven los flags SYN, ACK, FIN y RST del header TCP?**
**SYN:** sincroniza / **abre** la conexión (3-way handshake). **ACK:** indica que el segmento lleva un **acuse de recibo** válido. **FIN:** el emisor **no tiene más datos** y quiere cerrar. **RST:** *reset*, fuerza a **recomenzar** la conexión ante un problema.
