# REDES DE DATOS - Práctica

**Comisión 403 Germán Baró**

**Cuestionario para el segundo parcial: Capa de Red**

## Cómo usarlo

Son todas las preguntas conceptuales de Capa de Red que tenemos, sin repetir. Cada una indica de dónde sale:
- **[Guía]:** guía de estudio de Baró.
- **[Parcial 2024]:** su 2do parcial del 29/10/2024.
- **[Práctica]:** práctica de Capa de Red de la cátedra.
- **[Medín]:** preguntas de Capa de Red que tomó Medín en el 1er parcial.
- **[2025]:** 2dos parciales de 2025 de otras comisiones, solo las que caen dentro del temario de Baró.

**Las respuestas están al final**, en página aparte, con la misma numeración. Los ejercicios numéricos (subnetting, fragmentación, vector distancia) están en el banco de ejercicios de Baró.

## Servicios de la capa de red

**1) Explique la diferencia entre servicio orientado a la conexión y servicio sin conexión.** [2025]

**2) ¿Qué es un circuito virtual y en qué tipo de servicio se usa?** [2025]

**3) ¿Qué diferencia hay entre el encabezado de un datagrama y el de un paquete de circuito virtual?** [Medín]

**4) Mencione dos aplicaciones donde convenga un servicio orientado a conexión y dos donde convenga uno sin conexión.** [Práctica]

**5) Si todos los routers y hosts funcionan bien, ¿puede un paquete ser entregado a un destino equivocado?** [Práctica]

## Ruteo

**6) Defina el concepto de ruteo en Internet.** [Guía]

**7) ¿En qué consiste una tabla de ruteo? ¿Quién la arma?** [Guía]

**8) ¿Qué es una ruta default? ¿Por qué existe esa entrada en la tabla de ruteo?** [Guía]

**9) ¿Qué es una métrica y para qué sirve? Dé ejemplos.** [Guía]

**10) ¿Qué es el sink tree (árbol óptimo)?** [2025]

**11) Defina inundación de red. ¿Cómo se evita que colapse la red?** [2025]

**12) ¿Qué campo de IPv4 evita que una inundación, o un paquete en un bucle, colapse la red?** [2025]

**13) ¿Qué diferencia operativa existe entre un protocolo de vector distancia y uno de estado de enlace?** [Guía]

**14) ¿A qué algoritmo pertenece el problema de la cuenta a infinito? Explíquelo.** [Medín] [2025]

**15) ¿En qué entorno trabaja el protocolo RIP?** [Guía]

## Protocolo IP

**16) ¿Qué campo o subcampo de la cabecera IP indica la prioridad del datagrama?** [Guía]

**17) El indicador "T" del campo Tipo de Servicio tiene una finalidad específica: ¿cuál es?** [Guía]

**18) Dentro del campo de opciones del datagrama IP hay una opción que se usa como "registro de ruta": ¿cuál es su utilidad?** [Guía]

**19) ¿Qué significa el valor 5 en el campo IHL? ¿Cómo se indica el tamaño del encabezado en IPv4?** [Medín] [2025]

**20) Describa el funcionamiento y la importancia del campo TTL.** [2025]

**21) ¿Qué contiene el campo Protocolo de IPv4?** [2025]

**22) ¿Qué campos controla el checksum del encabezado IPv4? ¿Cómo se hace el control de errores en IPv4?** [2025]

## Direcciones IP

**23) Explique el concepto de prefijo de red y de máscara de subred.** [2025]

**24) ¿Qué diferencia hay entre el direccionamiento por clases y el direccionamiento por agrupación de prefijos (CIDR)?** [2025]

**25) ¿Cuál es la función de definir rangos de direcciones privadas dentro de cada clase?** [Guía]

**26) ¿Qué es una caja NAT y para qué sirve?** [2025]

## Protocolos de control

**27) ¿Con qué finalidad se hace una petición ARP dentro de una LAN?** [Guía] [Medín]

**28) ¿A qué capa del modelo OSI pertenece el protocolo ICMP?** [Guía]

**29) ¿Qué es ICMP? Dé un ejemplo de uso.** [Medín] [2025]

**30) ¿Qué protocolo emite los mensajes de destino inalcanzable, tiempo excedido, problema en parámetro, bajar tráfico de fuente y ruta alternativa?** [Medín]

**31) Cuando se usan las opciones "registro de ruta" y "marca de tiempo", ¿qué protocolo de control se utiliza?** [Guía]

**32) ¿Cómo funciona traceroute?** [Medín]

**33) ¿Cómo funciona DHCP?** [2025]

**34) ¿Para qué se emplean ARP, ICMP y DHCP?** [Medín]

## OSPF, BGP y Sistemas Autónomos

**35) ¿En qué consiste un Sistema Autónomo? ¿Cómo está conformado? Describa.** [Guía]

**36) ¿Qué es un IGP? Funciones que cumple y entorno de aplicación.** [Guía]

**37) ¿Qué principios de funcionamiento tiene OSPF? ¿Qué ventajas tiene sobre los protocolos de vector distancia?** [Guía]

**38) Enuncie 4 ventajas de OSPF sobre RIP.** [Parcial 2024]

**39) ¿Qué quiere decir que OSPF reconoce jerarquías de ruteo?** [Guía]

**40) ¿Qué es un área dentro de un Sistema Autónomo y qué tipos de áreas existen?** [Guía]

**41) ¿Cómo están compuestos los paquetes de estado de enlace en OSPF?** [Guía]

**42) ¿En qué consiste un grafo en OSPF y con qué fin se realiza?** [Guía]

**43) ¿Cuáles son los 5 pasos que ejecuta OSPF para aprender y difundir rutas óptimas?** [Guía]

**44) ¿En qué consiste el protocolo BGP? ¿En qué entorno se aplica? ¿Qué filosofía de ruteo utiliza?** [Guía]

**45) Explique OSPF y BGP y en qué se diferencian.** [2025]

## Respuestas

### Servicios de la capa de red

**1)** **Sin conexión (datagramas):** no hay establecimiento previo; cada paquete lleva las IP de origen y destino y viaja por su cuenta, así que pueden llegar desordenados. **Orientado a conexión (circuito virtual):** primero se establece una ruta y después todos los paquetes la siguen; tiene 3 fases (establecimiento, transferencia, liberación) y permite reservar recursos (QoS). IP es sin conexión.

**2)** Es una **ruta fija que se arma antes de transmitir**: cada router del camino guarda una entrada en su tabla para ese circuito, y después cada paquete lleva solo el número de circuito. Se usa en el **servicio orientado a conexión**, por ejemplo en MPLS o ATM.

**3)** El **datagrama** lleva las **direcciones completas de origen y destino**, porque cada router decide la ruta paquete por paquete. El paquete de **circuito virtual** lleva solo el **número de CV**, porque la ruta ya quedó fijada al establecer el circuito y los routers la tienen en su tabla.

**4)** Con conexión: **homebanking** (no tolera pérdidas ni errores) y **correo electrónico**. Sin conexión: **transmisión en vivo** de un partido (no hay tiempo para retransmitir) y **videoconferencia o VoIP**.

**5)** **Sí.** Una interferencia en el medio que no se pueda corregir puede alterar el campo de dirección destino.

### Ruteo

**6)** Es el proceso por el cual los **routers deciden por qué línea de salida reenviar cada datagrama** para que llegue a su red destino, usando una tabla de ruteo que arman con algoritmos y protocolos de ruteo (IGP dentro de cada SA, BGP entre SA). Se distingue el **reenvío** (consultar la tabla para cada paquete) del **ruteo** (armar y actualizar esa tabla).

**7)** Es la tabla del router que asocia cada **red destino** con la **línea de salida o próximo salto** y su **métrica**. La arma **cada router**: dinámicamente, con un protocolo de ruteo, o la carga a mano el administrador si es estática.

**8)** Es la entrada que se usa **cuando el destino no coincide con ninguna otra** (`0.0.0.0/0`). Existe porque un router **no puede tener todas las redes de Internet** en su tabla: lo desconocido se manda al router de salida o al ISP.

**9)** Es el **costo** asignado a un enlace o a una ruta para **comparar caminos y elegir el mejor**. Ejemplos: cantidad de saltos (RIP), retardo, ancho de banda (OSPF: 1 Gbps → 1, 100 Mbps → 10), carga, distancia, costo económico.

**10)** Es el árbol formado por **las rutas óptimas desde todos los routers hacia un destino** (o desde uno hacia todos). Sale del **principio de optimalidad**: si J está en la ruta óptima de I a K, la ruta óptima de J a K va por el mismo camino. No tiene bucles, así que todo paquete llega en una cantidad finita de saltos.

**11)** **Inundación:** cada paquete se reenvía **por todas las líneas excepto por la que llegó**. Es muy robusta y siempre encuentra el camino más corto, pero genera muchos duplicados. Para que no colapse la red: un **contador de saltos** en el header que se decrementa en cada router y descarta el paquete al llegar a 0, y un **número de secuencia** por origen para descartar los duplicados.

**12)** El **TTL** (*Time To Live*): cada router le resta 1 y, al llegar a 0, el datagrama se descarta y se avisa al origen con un ICMP 11. Funciona como contador de saltos.

**13)** En **vector distancia** (RIP), cada router envía **su tabla completa solo a sus vecinos** y no conoce la topología; converge lento y tiene cuenta a infinito. En **estado de enlace** (OSPF), cada router envía **solo el estado de sus enlaces a todos** por inundación; todos conocen la topología completa y cada uno calcula con Dijkstra; converge rápido, a cambio de más memoria y CPU.

**14)** Al de **vector distancia**. Cuando cae un enlace, los routers se siguen informando rutas viejas entre sí y van sumando de a 1 en cada intercambio: la mala noticia se propaga muy lento. Las buenas noticias se propagan rápido; las malas, lento. Se mitiga fijando un "infinito" bajo.

**15)** **Dentro de un Sistema Autónomo**: es un **IGP** de vector distancia, con la **cantidad de saltos** como métrica. Funciona bien en **redes chicas** y empeora en redes grandes, porque converge lento y sufre la cuenta a infinito. *(Su máximo de 15 saltos, con 16 como infinito, es conocimiento general: no está en las fuentes.)*

### Protocolo IP

**16)** El subcampo **Prioridad** (3 bits, de 0 a 7) del campo **Tipo de Servicio**.

**17)** El bit **T** (*Throughput*) pide **alto rendimiento**: transmitir el mayor volumen de datos en el menor tiempo. Es una sugerencia a los routers, que pueden respetarla o no.

**18)** Cada router por el que pasa el datagrama **agrega su IP** en esa opción, así se sabe **qué camino siguió**. Sirve para diagnosticar y depurar el ruteo. Entran unas 9 direcciones.

**19)** El **IHL** (o HLEN) indica el **largo del encabezado en palabras de 32 bits** (4 bytes). El valor **5 es el mínimo**: 5 × 4 = **20 bytes**, un header sin opciones. El máximo es 15, o sea 60 bytes.

**20)** Es un campo de **8 bits** (máximo 255). **Cada router le resta 1**, y al llegar a 0 el datagrama se descarta y se avisa al origen con un **ICMP 11** (tiempo excedido). Es importante porque **evita que un paquete dé vueltas para siempre** si hay un bucle de ruteo. Además, traceroute se basa en él.

**21)** Indica **qué protocolo viaja en el campo de datos**: **1 ICMP, 2 IGMP, 6 TCP, 17 UDP**. Con eso, el destino sabe a qué protocolo entregarle el contenido.

**22)** Controla **solo los campos del encabezado**, no los datos. Es una suma en complemento a uno; si al recibir no cierra, el datagrama se descarta. Se **recalcula en cada router** porque el TTL cambia en cada salto. Los datos los controlan las capas superiores con el checksum de TCP o UDP, y la trama con el CRC de capa 2. Ojo: es un control de errores, no de seguridad.

### Direcciones IP

**23)** El **prefijo de red** es la parte de la dirección, de longitud variable, que es igual para todos los hosts de una red; el resto de los bits identifica al host. Se anota con una barra: 192.168.1.0/24 tiene 24 bits de red. La **máscara** tiene 1 en el prefijo y 0 en la parte de host (/24 = 255.255.255.0); aplicándole un **AND** a una IP se obtiene la dirección de red.

**24)** **Con clases**, el prefijo es **fijo** según la clase: /8 en A, /16 en B y /24 en C. Eso desperdicia muchas direcciones (por ejemplo, una empresa con 300 hosts necesitaba una clase B entera). Con **CIDR** el prefijo es de **longitud variable**: se asigna el tamaño justo y se **agrupan prefijos contiguos en una sola entrada** de la tabla (superredes). Esto redujo las tablas de los routers y extendió la vida de IPv4.

**25)** Permiten armar redes internas **sin contratar IPs públicas** y **sin conflictos con Internet**, porque esos rangos nunca se asignan públicamente. Todas las organizaciones pueden **reusarlos**, lo que ahorra direcciones, y los hosts privados **no son accesibles desde afuera**: salen a Internet a través de un router, proxy o NAT con IP pública. Rangos: 10.0.0.0, 172.16.0.0 a 172.31.0.0 y 192.168.0.0 a 192.168.255.0.

**26)** Es el equipo que **traduce las IP privadas de una red interna a una IP pública** para salir a Internet. Las conexiones de cada máquina interna se distinguen por el **número de puerto**. Sirve para que muchas máquinas compartan una sola IP pública. Se critica porque rompe el principio de que una máquina tiene una IP única; con IPv6 se seguiría usando como firewall.

### Protocolos de control

**27)** Para obtener la **dirección MAC** que corresponde a una IP: la trama necesita la MAC destino y el datagrama solo trae la IP. Si el destino está en otra red, se pregunta por la MAC del **gateway**. La pregunta va por broadcast y la respuesta vuelve directa; el resultado se guarda en la caché ARP.

**28)** A la **capa 3 (red)**, aunque sus mensajes viajan dentro de datagramas IP.

**29)** Es el protocolo que **informa errores y transporta mensajes de control** de la capa de red. Solo informa, no decide: qué hacer queda para las capas superiores. Ejemplo: el **ping** manda un ICMP 8 (solicitud de eco) y recibe un ICMP 0 (respuesta) para ver si un host está activo. Otro ejemplo: cuando un router no tiene camino al destino, devuelve un ICMP 3 (destino inaccesible).

**30)** **ICMP**: destino inaccesible (tipo 3), tiempo excedido (11), problema de parámetros (12), source quench (4, en desuso) y redireccionar (5).

**31)** **ICMP**. Las dos opciones se usan con los mensajes de eco (`ping -r` registra la ruta y `ping -s` los horarios), y ICMP tiene además los mensajes de marca de tiempo (tipos 13 y 14).

**32)** Manda paquetes con **TTL = 1, 2, 3…** (hasta 30). Cada router donde el TTL llega a 0 descarta el paquete y devuelve un **ICMP 11** con su IP; así se descubre cada salto. El destino final responde con un ICMP 0. **Windows (`tracert`) usa ICMP echo; Unix (`traceroute`) usa UDP.**

**33)** El host arranca sin IP y pide una por **broadcast** (**DHCP DISCOVER**), identificándose con su MAC. El servidor le asigna una IP libre (**DHCP OFFER**) por un **tiempo de arriendo**, y además le pasa máscara, gateway y DNS. Antes de que venza, el host tiene que renovarlo. Si el servidor está en otra red, el router reenvía los pedidos. Usa UDP, puertos 67 y 68. *(El intercambio completo de 4 mensajes, DORA, suma REQUEST y ACK: es conocimiento general.)*

**34)** **ARP:** traducir una IP a una MAC dentro de la LAN. **ICMP:** informar errores y diagnosticar (ping, traceroute). **DHCP:** asignar automáticamente IP, máscara, gateway y DNS al conectarse.

### OSPF, BGP y Sistemas Autónomos

**35)** Es una red o un conjunto de redes **operado de manera independiente**, bajo una única administración (un ISP, una empresa, una universidad), con **su propia política de ruteo** y un número que lo identifica. Internet es la interconexión de Sistemas Autónomos. Tiene **routers internos**, que rutean con un IGP, y **routers de frontera**, que se conectan con otros SA mediante BGP.

**36)** Un **IGP** (*Interior Gateway Protocol*) es un protocolo de ruteo **intradominio**. **Funciones:** calcular las **rutas de menor costo** entre las redes del SA y adaptarse rápido a los cambios; como hay un solo administrador, no maneja políticas, solo busca eficiencia. **Entorno:** **dentro de un Sistema Autónomo**. Ejemplos: RIP, OSPF, IS-IS.

**37)** **Principios:** es de **estado de enlace** y estándar abierto. Descubre vecinos con Hello, mide costos, inunda paquetes de estado de enlace y calcula con Dijkstra. Admite varias métricas, balancea carga entre caminos de igual costo (ECMP), es jerárquico (áreas), autentica los mensajes y elige un router designado por LAN. **Ventajas sobre vector distancia:** converge rápido sin cuenta a infinito, cada router conoce la topología completa, escala con áreas y solo envía cambios.

**38)** (1) **Converge rápido y no tiene cuenta a infinito**, porque cada router conoce la topología completa. (2) **Mejor métrica:** costo según ancho de banda, no solo saltos. (3) **Escala** gracias a las áreas. (4) **Solo envía cambios**, no la tabla entera periódicamente. También: balanceo ECMP y autenticación.

**39)** Que divide el SA en **áreas** conectadas a un **backbone (área 0)**. Cada router conoce en detalle **solo la topología de su área**; de las demás ve los destinos, pero no la topología. El tráfico entre áreas **pasa siempre por el backbone**. Así se achican las tablas, los mensajes y los cálculos.

**40)** Un área es **una red o un conjunto de redes contiguas** dentro del SA; las áreas no se superponen. Tipos: **backbone (área 0)**, que conecta a todas; **aislada (*stub*)**, con un solo router de frontera, que resuelve todo lo externo con una ruta default; y las **áreas comunes**. Los routers pueden ser internos, del backbone, de frontera de área (también forman parte del backbone) o de límite del SA.

**41)** Cada paquete de estado de enlace (LSP) lleva: la **identidad del emisor**, un **número de secuencia** (para descartar duplicados y paquetes viejos), una **edad** (al llegar a 0 se descarta) y la **lista de vecinos con el costo a cada uno**.

**42)** Con los LSP de todos los routers, **cada router arma el grafo de la red**: los routers son los nodos y los enlaces con su costo son las aristas (cada enlace aparece una vez por sentido). Se arma para **correr Dijkstra** y calcular localmente la ruta más corta a cada destino.

**43)** (1) Descubrir a los vecinos y sus direcciones (Hello). (2) Medir el costo a cada vecino. (3) Armar el paquete de estado de enlace. (4) Enviarlo a todos los routers por inundación y recibir los de los demás. (5) Calcular la ruta más corta a cada router con Dijkstra.

**44)** Es el protocolo de ruteo **interdominio**: rutea **entre Sistemas Autónomos**, en Internet a nivel de ISP y organizaciones. Lo corren los routers de frontera, sobre **conexiones TCP**. **Filosofía: ruteo por políticas**: decide qué tráfico acepta llevar y para quién, por razones económicas, de seguridad o políticas, y no solo la ruta más corta. Usa **vector de ruta**: anuncia el camino completo de SA, lo que le permite detectar bucles.

**45)** **OSPF** rutea **dentro** de un SA (IGP): busca la ruta **más eficiente**, con estado de enlace, Dijkstra y áreas. **BGP** rutea **entre** SA (interdominio): elige rutas según **políticas**, con vector de ruta sobre TCP. Diferencia de fondo: OSPF optimiza el costo; BGP respeta acuerdos y políticas.
