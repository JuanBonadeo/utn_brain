# REDES DE DATOS - Teoría

**Comisión 403 Cristian Medín**

**Preguntas para el segundo parcial**

## Cómo usarlo

Son las preguntas que tomó Medín en la parte teórica del **2do parcial del 29/10/2024** (com. 403), todas de **Capa de Transporte**. Resolvé primero: **las respuestas están al final**, en página aparte.

El temario del 2do teórico de 2026 (27/10) **todavía no está confirmado**: cuando lo confirme Medín, se arma el resumen y se amplía esta lista.

## Parcial real de Medín (29/10/2024)

**1) ¿Qué responsabilidades tiene la capa de transporte?**

**2) ¿Cómo controla la congestión el protocolo UDP?**

**3) ¿Qué sucede si UDP detecta un error? ¿Y TCP?**

**4) Grafique un ejemplo de conexión 3-way handshake.**

**5) Enuncie diferencias entre TCP y UDP.**

## Respuestas

**1)** Comunicación extremo a extremo confiable y eficiente entre aplicaciones. Divide en segmentos y reensambla, garantiza entrega ordenada y confiable (TCP), hace control de errores y de flujo, multiplexa por puertos y controla la congestión (solo TCP).

**2)** No la controla. No tiene control de congestión ni de flujo: envía al ritmo de la aplicación. Si hace falta control, lo implementa la aplicación.

**3)** UDP no retransmite. El documento de preguntas de Medín dice que descarta el datagrama; la diapositiva de UDP de la cátedra dice que avisa a las capas superiores y deja que decidan (ver Unidad 3). TCP detecta el error y retransmite hasta recibir el ACK, manteniendo el orden.

**4)**

```
Cliente                 Servidor
   | ---- SYN (seq=x) ------> |
   | <-- SYN+ACK (seq=y,      |
   |      ack=x+1) ---------- |
   | ---- ACK (ack=y+1) ----> |
   |   conexión establecida   |
```

**5)** TCP es orientado a conexión, confiable (retransmite y ordena), con control de flujo y de congestión, header de 20 B o más y flujo de bytes; se usa en web, correo y transferencias. UDP es sin conexión, sin garantías ni controles, con header de 8 B y mensajes individuales; se usa en voz y video en tiempo real, DNS y DHCP.
