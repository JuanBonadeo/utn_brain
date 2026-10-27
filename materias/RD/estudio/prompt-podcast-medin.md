# Prompts para el podcast de repaso — 2do teórico de Medín (mar 27/10)

Fuente: `resumen-2do-parcial-medin.pdf` (Transporte, Puertos y Firewall: el temario que confirmó
Medín por mail). Pensado para NotebookLM (Resumen de audio → Personalizar). Formato sugerido:
**Análisis en profundidad**, duración **Más larga**, idioma **Español**.

Hay dos opciones:
- **Un solo episodio** que repasa todo el temario. Sirve para una vuelta general.
- **Tres episodios**, uno por bloque, cargando el mismo PDF y cambiando el prompt. Entran en más
  detalle.

**Qué pesa más.** Las cinco preguntas del 2do teórico real de Medín (29/10/2024) fueron todas de
transporte: responsabilidades de la capa 4, UDP y la congestión, qué hacen UDP y TCP ante un error,
el 3-way handshake y TCP vs. UDP. Por eso los episodios 1 y 2 son los de prioridad máxima. Puertos y
Firewall entran por el mail, pero no hay preguntas reales: el episodio 3 los cubre por definición y
contraste. Con poco tiempo, escuchá el 2 y el 3.

En 2024 las preguntas fueron **para desarrollar**; el 1er parcial de 2026 fue multiple choice. Los
prompts entrenan las dos cosas: responder por escrito en pocas líneas y distinguir conceptos
parecidos.

Si el campo de personalización no acepta el texto largo, usá la versión corta.

## Episodio único — todo el temario

```text
Generá un podcast de repaso para un estudiante de 4.º año de Ingeniería en Sistemas (UTN) que rinde el 2do parcial de teoría de Redes de Datos con el profesor Medín. Entran tres bloques: capa de transporte (servicios, primitivas, características, TCP y UDP), puertos y firewall. El parcial real de 2024 fueron cinco preguntas para desarrollar, todas de transporte. Usá únicamente el documento cargado; no agregues temas que no estén ahí.

TONO Y FORMATO
- Español rioplatense, dos voces. Una explica; la otra hace de alumno que pregunta y cae en las confusiones típicas, para que la primera lo corrija.
- Para cada concepto: primero un ejemplo concreto de la vida diaria (abrir una web, una videollamada, una transferencia bancaria), después la idea, después la trampa.
- La primera vez que aparezca una sigla, decí qué significa (TCP, UDP, ARQ, AIMD, SCTP, RTP, NGFW, DMZ…).
- Cada tanto, frená con una pregunta estilo parcial, dejá un segundo para pensar y respondela como se respondería por escrito: en tres o cuatro líneas, con los términos exactos.
- Sin introducciones largas ni relleno.

CONTENIDO, EN ESTE ORDEN
1. Capa de transporte (alrededor del 35 %): por qué es la primera capa extremo a extremo y qué significa frente al salto a salto de las capas 1 a 3; segmento; responsabilidades; primitivas de sockets y el orden del servidor; puertos como dirección; el problema de los segmentos duplicados y la vida máxima; desconexión simétrica vs. asimétrica y el problema de los dos ejércitos; control de errores y de flujo extremo a extremo; multiplexación vs. multiplexación inversa (SCTP sí, TCP no); congestión como responsabilidad conjunta de las capas 3 y 4, tasa justa y AIMD.
2. TCP y UDP (alrededor del 40 %): características de TCP; header y flags (SYN, ACK, FIN, RST, PSH, URG); 3-way handshake y cierre en cuatro segmentos; ventana deslizante como control de flujo; slow start, incremento aditivo, Tahoe vs. Reno; SACK. UDP: header de 8 bytes, qué no hace, checksum opcional y pseudoencabezado; qué hace ante un error; RTP y RTCP para tiempo real; jitter y buffer. Cerrá el bloque con la tabla TCP vs. UDP.
3. Puertos y firewall (alrededor del 25 %): puerto y socket; rangos de la IANA y puerto efímero; estados abierto, cerrado y filtrado; SYN flood y predicción de secuencia; cómo se protegen los puertos. Firewall: qué es, componentes de una regla, denegar por defecto, orden de las reglas y regla de limpieza; stateless vs. stateful vs. proxy vs. NGFW y en qué capas trabaja cada uno; DMZ; SNAT y DNAT.

TRAMPAS QUE TIENEN QUE QUEDAR CLARAS
- Qué hace UDP si detecta un error: lo detecta con el checksum, no lo corrige ni retransmite y avisa a las capas superiores. Es la versión del apunte de Medín para este parcial.
- UDP no controla la congestión: manda al ritmo de la aplicación.
- TCP no es stop-and-wait: usa ventana deslizante y manda varios segmentos sin esperar cada ACK.
- En Tahoe lo que baja a la mitad es el umbral y la ventana vuelve a arrancar con slow start; Reno sigue desde la mitad.
- Un firewall stateless no sabe si un paquete entrante es una respuesta o un ataque; uno stateful sí.

RESOLVÉ EN VOZ ALTA
Las cinco preguntas del parcial real de 2024: responsabilidades de la capa de transporte; cómo controla la congestión UDP; qué pasa si UDP detecta un error, y si lo detecta TCP; el 3-way handshake contado paso a paso con SYN, ACK y los números de secuencia; diferencias entre TCP y UDP. Sumá qué protocolo conviene para streaming y cuál para una transferencia bancaria, y qué hace un stateful con un paquete que llega al puerto 51.234 de tu PC.

CIERRE
Terminá con las cinco ideas que más conviene llevar al parcial, en formato "si te preguntan X, respondé Y".
```

Versión corta (478 caracteres):

```text
Podcast de repaso en español rioplatense, dos voces (una explica, otra pregunta y se confunde), para el 2do parcial de teoría de Redes de Datos (UTN). Sólo con el documento. Cubrí transporte, TCP vs. UDP, puertos y firewall. Resolvé las 5 preguntas del parcial real: responsabilidades de la capa 4, UDP y la congestión, qué hacen UDP y TCP ante un error, 3-way handshake y diferencias TCP/UDP. UDP ante error: no corrige, avisa a las capas superiores. Cerrá con las ideas clave.
```

## Episodio 1 — La capa de transporte y UDP

```text
Generá un podcast de repaso para un estudiante de Ingeniería en Sistemas (UTN) que rinde el 2do parcial de teoría de Redes de Datos con Medín: preguntas para desarrollar o multiple choice. Este episodio cubre las secciones "Servicios y primitivas de transporte", "Características de transporte" y "Protocolo UDP" del documento. Usá únicamente el documento cargado.

TONO Y FORMATO
- Español rioplatense, dos voces: una explica, la otra pregunta y cae en las confusiones típicas.
- Ejemplo concreto primero (una videollamada, Spotify, una transferencia bancaria), después la idea, después la trampa.
- Decí qué significa cada sigla la primera vez que aparece.
- Frená cada tanto con una pregunta estilo parcial y respondela como por escrito, en tres o cuatro líneas.

CONTENIDO
1. Por qué la capa 4 es la primera extremo a extremo; host vs. router; segmento dentro del paquete dentro de la trama; entidad de transporte.
2. Responsabilidades de la capa de transporte (pregunta real de Medín): segmentar y reensamblar, entrega ordenada y confiable, control de errores y de flujo, multiplexación por puertos, control de congestión.
3. Servicio orientado a conexión vs. sin conexión. Primitivas de sockets y el orden del lado del servidor (SOCKET, BIND, LISTEN, ACCEPT).
4. Direccionamiento por puertos (TSAP, 16 bits, port mapper).
5. Establecimiento: el problema de los segmentos duplicados, la vida máxima de 120 s y el 3-way handshake. Desconexión simétrica vs. asimétrica y el problema de los dos ejércitos.
6. Control de errores y de flujo extremo a extremo: por qué hace falta si la capa 2 ya lo hace; ARQ; buffers y ventana dinámica.
7. Multiplexación vs. multiplexación inversa: quién hace cada una y por qué TCP no hace la inversa.
8. Congestión: por qué es responsabilidad conjunta de las capas 3 y 4, tasa justa (max-min) y AIMD. Caídas del receptor, WiFi que retransmite en la capa 2 y satélite con FEC.
9. UDP: header de 8 bytes, qué no hace, checksum opcional y pseudoencabezado (y por qué viola las capas), qué hace ante un error, RPC, RTP y RTCP, jitter y buffer de reproducción.

RESOLVÉ EN VOZ ALTA
- ¿Qué responsabilidades tiene la capa de transporte?
- ¿Cómo controla la congestión el protocolo UDP? (No la controla: explicá por qué y quién lo hace si hace falta.)
- ¿Qué sucede si UDP detecta un error? Respuesta del apunte: no corrige y avisa a las capas superiores.
- ¿Qué es la multiplexación inversa y qué protocolo la realiza?
- ¿Por qué Netflix tiene un buffer de unos 10 segundos y Zoom casi no tiene?

CIERRE
Las cuatro distinciones que no hay que confundir, en formato "si ves X, es Y".
```

Versión corta (444 caracteres):

```text
Podcast de repaso en español rioplatense, dos voces, para el 2do parcial de teoría de Redes (UTN). Sólo con el documento: secciones de servicios, características de transporte y UDP. Clave: capa 4 extremo a extremo, responsabilidades, dos ejércitos, multiplexación inversa (SCTP), tasa justa y AIMD, UDP sin control de congestión y que ante un error no corrige y avisa a las capas superiores, RTP/RTCP. Resolvé preguntas de parcial en voz alta.
```

## Episodio 2 — TCP a fondo y TCP vs. UDP

```text
Generá un podcast de repaso para un estudiante de Ingeniería en Sistemas (UTN) que rinde el 2do parcial de teoría de Redes de Datos con Medín: preguntas para desarrollar o multiple choice. Este episodio cubre las secciones "Protocolo TCP" y "TCP vs UDP" del documento. Es el bloque que más preguntas reales tuvo. Usá únicamente el documento cargado.

TONO Y FORMATO
- Español rioplatense, dos voces: una explica, la otra pregunta y cae en las confusiones típicas.
- Ejemplo concreto primero, después el mecanismo, después la trampa.
- Contá los intercambios de segmentos como un diálogo entre cliente y servidor, diciendo qué flags van prendidos y qué números de secuencia viajan, para que se puedan dibujar en el examen.
- Frená cada tanto con una pregunta estilo parcial y respondela como por escrito, en tres o cuatro líneas.

CONTENIDO
1. Características de TCP: confiable sobre una red que no lo es, full-duplex, unicast, flujo de bytes, por qué el segmento práctico es de 1460 bytes de datos.
2. Header: puertos, número de secuencia y de acknowledgement, ventana, checksum obligatorio y opciones (MSS, escala de ventana, SACK). Qué hace cada flag: SYN, ACK, FIN, RST, PSH, URG, ECE y CWR. Datos urgentes con URG y el puntero urgente.
3. 3-way handshake paso a paso y por qué el número de secuencia inicial es aleatorio. Cierre en cuatro segmentos y el timeout como salida a los dos ejércitos.
4. Control de flujo con ventana deslizante (el ejemplo del buffer de 4 KB y segmentos de 2 KB), Nagle y el temporizador de retransmisión ajustado al RTT.
5. Control de congestión: ventana de congestión vs. ventana del receptor, reloj de ACKs, slow start, incremento aditivo, baja a la mitad. Tahoe vs. Reno: qué hace cada uno ante tres ACK duplicados. Aclarar que en Tahoe lo que se fija en la mitad es el umbral y se vuelve a slow start, mientras que Reno sigue desde la mitad (fast recovery).
6. ARQ en TCP: ACK acumulativos, SACK, retransmisión por timeout o por tres ACK duplicados.
7. Tabla TCP vs. UDP, fila por fila, y cuándo conviene cada uno.

TRAMPA
El apunte de puertos dice que TCP es lento porque confirma cada paquete antes de mandar el siguiente. Eso es stop-and-wait; TCP usa ventana deslizante. Es más lento por el handshake, los ACK y el control de congestión.

RESOLVÉ EN VOZ ALTA
- Grafique un ejemplo de conexión 3-way handshake (contalo para que se pueda dibujar).
- ¿Qué sucede si TCP detecta un error? Comparalo con UDP.
- Enuncie diferencias entre TCP y UDP.
- ¿Cuál es el mecanismo de TCP para enviar datos urgentes?
- Explique slow start, incremento aditivo, TCP Tahoe y TCP Reno.
- ¿Qué protocolo conviene para streaming y cuál para una transferencia bancaria, y por qué?

CIERRE
Las cinco ideas que más conviene llevar al parcial, en formato "si te preguntan X, respondé Y".
```

Versión corta (434 caracteres):

```text
Podcast de repaso en español rioplatense, dos voces, para el 2do parcial de teoría de Redes (UTN). Sólo con el documento: secciones TCP y TCP vs. UDP. Clave: flags, 3-way handshake contado para dibujarlo, cierre en 4 segmentos, ventana deslizante (no es stop-and-wait), slow start, AIMD, Tahoe vs. Reno, datos urgentes, qué hace TCP ante un error. Resolvé las preguntas del parcial real y cerrá con la tabla TCP/UDP y las ideas clave.
```

## Episodio 3 — Puertos y firewall

```text
Generá un podcast de repaso para un estudiante de Ingeniería en Sistemas (UTN) que rinde el 2do parcial de teoría de Redes de Datos con Medín: preguntas para desarrollar o multiple choice. Este episodio cubre las secciones "Puertos" y "Firewall" del documento. Son temas nuevos del temario y no hay preguntas reales de años anteriores, así que importan las definiciones precisas y los contrastes. Usá únicamente el documento cargado.

TONO Y FORMATO
- Español rioplatense, dos voces: una explica, la otra pregunta y cae en las confusiones típicas.
- Ejemplo concreto primero (abrir una web desde casa, montar un servidor de juegos, la red de una empresa con un servidor web), después la idea, después la trampa.
- Decí qué significa cada sigla la primera vez que aparece.
- Frená cada tanto con una pregunta estilo parcial y respondela como por escrito, en tres o cuatro líneas.

CONTENIDO
1. Puertos: qué es un puerto, socket = IP + puerto, el puerto efímero de origen. Rangos de la IANA (conocidos, registrados, efímeros) y los puertos clave de la lista. Estados abierto, cerrado y filtrado. Reenvío de puertos y NAT: lo peligroso es el servicio expuesto, no el puerto.
2. Ataques: SYN flood y cómo se mitiga (SYN cookies), predicción de secuencia TCP, spoofing, manipulación de paquetes, tunneling.
3. Peligros de un puerto abierto y cómo protegerlos: todo cerrado por defecto, software actualizado, autenticación robusta, monitoreo e IDS/IPS. Los puertos UDP también se atacan: DNS, DHCP y SNMP (v2c vs. v3). Nmap y cómo clasifica un puerto según la respuesta.
4. TCP o UDP según el uso: VPN sobre UDP, QUIC y HTTP/3.
5. Firewall: qué es, la metáfora del aduanero, componentes de una regla (origen, destino, protocolo, puerto, acción). Denegar por defecto, mínimo privilegio, orden de lo más específico a lo más general y regla de limpieza.
6. Tipos: stateless, stateful, proxy y NGFW; en qué capas trabaja cada uno y por qué el stateful ya no alcanza cuando todo va por el 443. Servicios del NGFW.
7. Ubicación: perimetral, interno y DMZ. SNAT vs. DNAT y cómo trabajan junto con el firewall. Tendencias: Zero Trust, microsegmentación, FWaaS y SASE.

RESOLVÉ EN VOZ ALTA
- ¿Qué es un puerto efímero? Dé un ejemplo.
- ¿En qué consiste un ataque de inundación SYN y cómo se mitiga?
- ¿Qué diferencia hay entre un firewall stateless y uno stateful? Usá el paquete que llega al puerto 51.234 de tu PC.
- Diseñá las reglas para una DMZ con un servidor web: qué se permite, qué se deniega y cuál es la última regla.
- ¿Por qué SNMPv2c es un riesgo y qué cambia con la v3?

CIERRE
Las cinco distinciones que no hay que confundir, en formato "si ves X, es Y".
```

Versión corta (451 caracteres):

```text
Podcast de repaso en español rioplatense, dos voces, para el 2do parcial de teoría de Redes (UTN). Sólo con el documento: secciones Puertos y Firewall. Clave: rangos IANA, puerto efímero, estados, SYN flood, predicción de secuencia, protección de puertos, reglas del firewall, denegar por defecto y regla de limpieza, stateless vs. stateful vs. proxy vs. NGFW y sus capas, DMZ, SNAT/DNAT. Definiciones precisas y contrastes; cerrá con las ideas clave.
```

## Episodio 4 — El parcial de oct/2026 resuelto + 1 minuto de firewall

Cargá **dos** fuentes: `preguntas-parcial-medin.pdf` (tiene las 5 respuestas desarrolladas) y
`resumen-2do-parcial-medin.pdf` (de ahí sale el minuto de firewall). Es el episodio para escuchar
antes de entrar: las 5 preguntas que Medín tomó a otra comisión en oct/2026, que repiten 4 de las de 2024.

```text
Generá un podcast de repaso para un estudiante de Ingeniería en Sistemas (UTN) que rinde hoy el 2do parcial de teoría de Redes de Datos con Medín. El formato del examen es de 5 preguntas para desarrollar en 60 minutos, y se corrige por pertinencia (40 %), vocabulario técnico (30 %), fundamentación (25 %) y ortografía (5 %). El episodio resuelve, una por una, las 5 preguntas del parcial que Medín tomó a otra comisión en octubre de 2026, y cierra con un minuto de firewall. Usá únicamente los documentos cargados: las respuestas están en "Preguntas y respuestas de Medín", y el firewall en el resumen.

TONO Y FORMATO
- Español rioplatense, dos voces. Una hace de alumno que lee la consigna en voz alta y arranca a responder como lo haría en el examen, a veces con un error típico; la otra corrige y completa hasta dejar la respuesta "de 10".
- Para cada pregunta: (1) leer la consigna; (2) la respuesta corta en una frase; (3) el desarrollo con los términos técnicos exactos y la justificación; (4) un ejemplo concreto; (5) la trampa o lo que no hay que olvidar. Terminá cada pregunta diciendo en voz alta los términos que no pueden faltar en la hoja.
- Decí qué significa cada sigla la primera vez que aparece.
- Ritmo ágil, sin introducción larga ni relleno.

LAS 5 PREGUNTAS, EN ESTE ORDEN
1. "Enumere los propósitos de la capa de transporte y desarrolle al menos uno de ellos." Capa 4 como la primera extremo a extremo, frente al salto a salto de las capas 1 a 3. Los cuatro propósitos del apunte de Medín: seguimiento de conversaciones individuales, segmentación de datos, reensamble de segmentos e identificación de las aplicaciones. Desarrollar la identificación por puertos: 16 bits, socket = IP + puerto, rangos de la IANA, y el ejemplo del navegador que sale por un puerto efímero hacia el 443 mientras el Zoom usa la misma IP.
2. "¿Cómo controla la congestión el protocolo UDP?" Es una pregunta trampa: no la controla. Explicar por qué (sin ventana, sin ACK, sin números de secuencia, header de 8 bytes), que manda al ritmo de la aplicación y puede saturar la red, que si hace falta lo hace la aplicación (RTCP en streaming), y contrastar con TCP: slow start, AIMD, Tahoe y Reno.
3. "¿Qué sucede si UDP detecta un error? ¿Y si lo detecta TCP?" Los dos detectan con el checksum y el pseudoencabezado. UDP: checksum opcional, no corrige ni retransmite y avisa a las capas superiores, que deciden (versión de la diapositiva de Medín de 2026); en la práctica el datagrama se descarta. TCP: checksum obligatorio, descarta y no confirma, el emisor retransmite por timeout o por tres ACK duplicados (ARQ), y la aplicación recibe todo en orden sin enterarse. Cerrar con la síntesis: UDP detecta y deja decidir a la capa superior; TCP detecta y recupera solo.
4. "Explique al menos uno de los tipos de fragmentación que existe en una comunicación entre redes que tienen distintas tecnologías." Aclarar que es de capa de red. La MTU y por qué el router fragmenta. Contar el diagrama para que se pueda dibujar: origen, red de MTU 1500, router G1, red chica de MTU 620, router G2, red de MTU 1500, destino. Transparente: G1 fragmenta y G2 reensambla, todos los fragmentos salen por G2, y la red siguiente no se entera; sus desventajas. No transparente, la de IP: cada fragmento es un datagrama independiente y solo reensambla el destino, usando Identificación, desplazamiento en unidades de 8 bytes y el bit MF; ventajas y desventajas. Repasar el ejemplo de 1400 bytes de datos con MTU 620: tres fragmentos de 600, 600 y 200 bytes de datos, desplazamientos 0, 75 y 150, MF 1, 1 y 0. Mencionar el descubrimiento de la MTU de la ruta con DF.
5. "Mencione las principales diferencias entre TCP y UDP." Recorrer la tabla fila por fila: conexión, confiabilidad, control de errores, de flujo y de congestión, tamaño del encabezado (20 contra 8 bytes), flujo de bytes contra datagramas, unicast contra broadcast y multicast, velocidad y usos con sus puertos. Cerrar con la regla: TCP cuando no puede faltar nada (una transferencia bancaria), UDP cuando importa más llegar a tiempo (una videollamada).

UN MINUTO DE FIREWALL (al final, corto y concreto)
Qué es (filtra el tráfico entre redes según reglas; seguridad perimetral; el aduanero). Componentes de una regla: origen, destino, protocolo, puerto y acción. Denegar por defecto, el orden de lo más específico a lo más general y la regla de limpieza "denegar todo y registrar". Los cuatro tipos y su capa: stateless (capas 3 y 4), stateful (3 y 4, con tabla de conexiones), proxy (capa 7) y NGFW (3 a 7). El ejemplo clave: un paquete que llega al puerto 51.234 de tu PC; el stateless no sabe si es una respuesta o un ataque, el stateful sí. Una línea para la DMZ: la red intermedia donde van los servidores públicos.

CIERRE
Las cinco frases que hay que tener en la cabeza al entrar, una por pregunta, en formato "si te preguntan X, escribí Y", más una de firewall.
```

Versión corta (466 caracteres):

```text
Podcast en español rioplatense, dos voces (un alumno responde, el otro corrige), solo con los documentos. Resolvé las 5 preguntas del parcial de Medín de oct/2026: propósitos de la capa 4 (desarrollar puertos); UDP no controla la congestión; error en UDP (no corrige, avisa) vs TCP (retransmite, ARQ); fragmentación transparente vs no transparente con el ejemplo 1400 B / MTU 620; tabla TCP vs UDP. Cerrá con 1 minuto de firewall: reglas, stateless vs stateful, DMZ.
```
