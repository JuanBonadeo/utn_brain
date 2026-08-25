# Redes de Datos — Multiple Choice (1er Parcial, Prof. Medin)

> **Formato del parcial:** 10 preguntas multiple choice. **Alcance:** Capa de Enlace + Capa de Red (Transporte NO entra).
>
> **Cómo usarlo:** tapá la línea **"Respuesta"** y elegí. Cada explicación aclara por qué las otras opciones están mal — ahí está el jugo para no caer en los distractores. Hay 32 preguntas → alcanzan para 3 simulacros de 10.

---

## Capa de Enlace

**1. ¿Cuáles son las dos funciones centrales de la capa de enlace?**
- a) Ruteo y direccionamiento lógico
- b) Control de errores y control de flujo
- c) Control de congestión y multiplexación por puertos
- d) Cifrado y compresión de datos

**Respuesta: b.** Enlace hace control de errores + control de flujo. El ruteo/direccionamiento lógico (a) es capa 3; congestión y multiplexación (c) son de capas 3/4.

**2. En una trama, ¿en qué parte van los bits de control de errores (checksum/CRC)?**
- a) En el header
- b) En el campo de datos
- c) En el trailer (bits de cola)
- d) En un paquete ICMP separado

**Respuesta: c.** El trailer lleva el control de errores. El header lleva la delimitación (flag) y las direcciones.

**3. ¿Qué método de framing NO se usa en la práctica y por qué?**
- a) Flag de inicio, porque es muy lento
- b) Contar bytes, porque si el conteo llega con error el receptor pierde el sincronismo
- c) Bit-stuffing, porque agrega demasiados bits
- d) 4B/5B, porque desperdicia ancho de banda

**Respuesta: b.** Si el campo de longitud se corrompe, no se sabe dónde cortar y cuesta re-sincronizar.

**4. El byte-stuffing (insertar un byte ESC) es característico del protocolo:**
- a) HDLC
- b) Ethernet
- c) PPP
- d) WiFi

**Respuesta: c.** PPP usa byte-stuffing. HDLC usa bit-stuffing.

**5. En HDLC, el flag `01111110` se protege insertando un 0 cuando en los datos aparecen:**
- a) Seis 1 seguidos
- b) Un 0 y cinco 1 seguidos
- c) Dos flags consecutivos
- d) Cinco 0 seguidos

**Respuesta: b.** Ante un 0 y cinco 1, se mete un 0 (bit-stuffing) para no formar la falsa bandera.

**6. La técnica de framing por "violación de codificación" (4B/5B) la usan:**
- a) PPP y USB
- b) FDDI y Fast-Ethernet
- c) HDLC y enlaces satelitales
- d) DHCP y ARP

**Respuesta: b.**

**7. Ethernet clásica, como servicio de capa 2, es:**
- a) Orientado a conexión con confirmación
- b) Sin conexión "best-effort": no detecta ni retransmite tramas perdidas
- c) Sin conexión pero con confirmación de cada trama
- d) Orientado a conexión con 3 fases

**Respuesta: b.** Ethernet = best-effort; los errores los resuelven las capas superiores. El "sin conexión con confirmación" (c) es WiFi.

**8. ¿Qué caracteriza a Stop-and-Wait?**
- a) Ventana de tamaño N
- b) El receptor guarda tramas fuera de orden
- c) Ventana de tamaño 1: envía una trama y espera su ACK antes de la siguiente
- d) Usa confirmación acumulativa

**Respuesta: c.**

**9. En Go-Back-N, cuando una trama llega con error, el receptor:**
- a) La guarda y pide que le reenvíen solo esa
- b) Descarta todas las tramas que llegan fuera de orden
- c) Sigue aceptando las siguientes aunque estén en desorden
- d) Cierra la conexión

**Respuesta: b.** El receptor descarta lo fuera de orden; el emisor reenvía desde la trama que falló en adelante.

**10. ¿Cuál afirmación sobre Selective Repeat es correcta?**
- a) Necesita menos memoria en el receptor que Go-Back-N
- b) El emisor reenvía todas las tramas desde la que falló
- c) El receptor guarda las tramas fuera de orden y el emisor reenvía solo la que falló
- d) Tiene ventana de tamaño 1

**Respuesta: c.** Justamente por guardar fuera de orden necesita MÁS memoria (por eso (a) es falsa).

**11. Para que un reenvío no se confunda con tramas nuevas, el contador de secuencia debe ser:**
- a) Igual al tamaño de la ventana
- b) El doble del tamaño de la ventana
- c) La mitad del tamaño de la ventana
- d) Siempre 1

**Respuesta: b.**

**12. El piggybacking consiste en:**
- a) Enviar el ACK montado dentro de otro mensaje que ya iba de vuelta al emisor
- b) Reenviar todas las tramas ante un error
- c) Insertar bits de relleno en el flag
- d) Descartar las tramas más viejas en congestión

**Respuesta: a.**

---

## Capa de Red

**13. El elemento principal de la capa de red es:**
- a) El switch
- b) El router
- c) El host
- d) El módem

**Respuesta: b.** El router decide por su tabla interna. El switch es de capa 2.

**14. ¿Cuál es una diferencia correcta entre servicio de datagrama y de circuito virtual?**
- a) En datagrama todos los paquetes siguen la misma ruta
- b) En circuito virtual cada paquete lleva las IP de origen y destino completas
- c) En datagrama cada paquete viaja independiente y puede llegar desordenado
- d) El circuito virtual no necesita establecimiento previo

**Respuesta: c.** El CV fija una ruta única, requiere establecimiento y el paquete lleva solo el nº de circuito.

**15. La forma de transmisión "al nodo más cercano de un grupo" se llama:**
- a) Broadcast
- b) Multicast
- c) Unicast
- d) Anycast

**Respuesta: d.** Anycast (uno al más cercano; DNS, IPv6). Multicast es a un grupo suscripto; broadcast es a todos.

**16. El "Reverse Path Forwarding" (RPF) se usa para:**
- a) Traducir IP a MAC
- b) Hacer broadcast eficiente: reenvía si el paquete llegó por el enlace del sink tree, si no lo descarta
- c) Asignar direcciones IP dinámicas
- d) Controlar la congestión

**Respuesta: b.**

**17. El problema de la "cuenta a infinito" es propio del algoritmo de ruteo:**
- a) Estado de Enlaces (OSPF)
- b) Dijkstra
- c) Vector Distancia (RIP)
- d) BGP

**Respuesta: c.** El Vector Distancia propaga lento las caídas y el nº de saltos crece sin freno.

**18. Comparado con Vector Distancia, el Estado de Enlaces (OSPF):**
- a) Usa menos memoria y converge más lento
- b) Usa más memoria y CPU, pero converge más rápido
- c) No necesita conocer a sus vecinos
- d) También sufre la cuenta a infinito

**Respuesta: b.**

**19. ¿Para qué sirve el campo TTL del header IPv4?**
- a) Indica el tamaño total del paquete
- b) Se resta 1 en cada router y evita que un paquete quede dando vueltas para siempre
- c) Traduce la IP en dirección MAC
- d) Indica qué protocolo de capa 4 viaja adentro

**Respuesta: b.** TTL máx. 255; a 0 se descarta. (a) es Total Length; (d) es el campo Protocol.

**20. El Header Checksum de IPv4 se recalcula en cada router porque:**
- a) Cambia la IP de destino
- b) Cambia el campo TTL en cada salto
- c) El paquete siempre se fragmenta
- d) Cambia el número de puerto

**Respuesta: b.**

**21. Las direcciones IPv4 tienen una longitud de:**
- a) 16 bits
- b) 48 bits
- c) 32 bits
- d) 64 bits

**Respuesta: c.** 32 bits. (48 bits es la dirección MAC.)

**22. ¿Cuál de estos es un rango de direcciones IP privadas?**
- a) 127.0.0.0/8
- b) 192.168.0.0/16
- c) 255.255.255.255
- d) 8.8.8.0/24

**Respuesta: b.** Privadas: 10/8, 172.16/12 y 192.168/16. (127 es loopback.)

**23. La dirección 127.0.0.1 corresponde a:**
- a) Broadcast local
- b) La puerta de enlace por defecto
- c) Loopback (no sale a la red)
- d) Una dirección pública de un Tier 1

**Respuesta: c.**

**24. Con NAT, varias máquinas de IP privada comparten una IP pública distinguiéndose por:**
- a) La dirección MAC
- b) El número de puerto
- c) El TTL
- d) El prefijo de red

**Respuesta: b.** Además, NAT funciona como una especie de firewall (bloquea lo entrante).

**25. ¿Cuál es el orden correcto de las 5 etapas de control de congestión?**
- a) Load shedding → throttling → admission → traffic-aware → provisioning
- b) Provisioning → traffic-aware routing → admission control → traffic throttling → load shedding
- c) Admission → provisioning → load shedding → throttling → traffic-aware
- d) Throttling → load shedding → provisioning → admission → traffic-aware

**Respuesta: b.** De la prevención (provisioning) al último recurso (load shedding).

**26. El "load shedding" (descarte de paquetes):**
- a) Agrega memoria a los routers
- b) Es la primera medida ante una congestión
- c) Es el último recurso: se tiran paquetes (y nunca primero los de control)
- d) Crea nuevos circuitos virtuales

**Respuesta: c.**

**27. La técnica de throttling en la que el router marca el paquete y el receptor avisa a la fuente ("choke") se llama:**
- a) Hop-by-hop backpressure
- b) ECN (Explicit Congestion Notification)
- c) Load shedding
- d) Admission control

**Respuesta: b.** ECN no carga a los routers, pero es más lento (actúa recién al llegar al receptor).

**28. ¿Qué protocolo traduce una dirección IP en su dirección MAC dentro de la LAN?**
- a) ICMP
- b) DHCP
- c) ARP
- d) DNS

**Respuesta: c.** ARP, preguntando por broadcast. ICMP = errores/diagnóstico; DHCP = IP dinámica.

**29. Los mensajes "destino inalcanzable" y "tiempo excedido" pertenecen al protocolo:**
- a) ARP
- b) ICMP
- c) DHCP
- d) OSPF

**Respuesta: b.** ICMP; lo usan ping (echo) y traceroute.

**30. ¿Cuál asociación es correcta?**
- a) OSPF = interdominio (entre Sistemas Autónomos)
- b) BGP = intradominio (dentro de un SA)
- c) OSPF = intradominio (estado de enlaces); BGP = interdominio (corre sobre TCP)
- d) Ambos usan Vector Distancia puro

**Respuesta: c.**

**31. MPLS se considera "capa 2,5" porque:**
- a) Es más lento que IP
- b) Rutea por una etiqueta (label) en lugar de por la IP, ubicándose entre las capas 2 y 3
- c) Reemplaza al protocolo ARP
- d) Solo funciona en redes WiFi

**Respuesta: b.**

**32. Al encenderse, un host obtiene su dirección IP automáticamente (más gateway y DNS) enviando un broadcast mediante:**
- a) ARP
- b) ICMP
- c) DHCP
- d) BGP

**Respuesta: c.**

---

### Respuestas (clave rápida)
1-b · 2-c · 3-b · 4-c · 5-b · 6-b · 7-b · 8-c · 9-b · 10-c · 11-b · 12-a · 13-b · 14-c · 15-d · 16-b · 17-c · 18-b · 19-b · 20-b · 21-c · 22-b · 23-c · 24-b · 25-b · 26-c · 27-b · 28-c · 29-b · 30-c · 31-b · 32-c
