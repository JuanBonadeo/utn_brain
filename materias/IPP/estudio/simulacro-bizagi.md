# IPP — Simulacro Bizagi (parcial 07-09-2026)

> **[NUESTRO]** Enunciado inventado para practicar. No es de la cátedra.
> Construido con la misma estructura que el parcial real de junio 2026
> (`repaso-parcial.md` 4.1): consigna numerada 1..N, un punto por paso, con
> las palabras clave del enunciado sirviendo de disparador léxico.
> Dificultad calibrada a "los ejercicios iniciales", que es lo que anunció
> el docente.

---

## Enunciado — Proceso de compra de materiales

1. Un empleado de cualquier área registra un pedido de materiales a través del
   sistema interno de compras. Al enviarlo, el Responsable de Compras evalúa el
   pedido.

2. Si el Responsable de Compras lo rechaza, el proceso concluye con una
   notificación al empleado.

3. Si lo aprueba, se inicia un **subproceso** destinado a seleccionar el
   proveedor: el Responsable de Compras pide cotizaciones a los proveedores y
   registra las que recibe; el Jefe de Compras las compara; si le parecen
   insuficientes, pide que se soliciten nuevas y el Responsable vuelve a
   pedirlas. Cuando el Jefe de Compras elige una cotización, el subproceso
   termina.

4. Finanzas verifica que haya presupuesto disponible. Si no lo hay, se le
   informa al empleado y el proceso termina.

5. Si hay presupuesto, el Responsable de Compras emite la orden de compra y se
   la envía al proveedor. A partir de ahí se espera la entrega de la mercadería
   dentro del plazo pactado. Si vence el plazo y la mercadería no llegó, se
   cancela la orden, se le avisa al proveedor y se notifica al empleado.

6. En cualquier momento anterior a la recepción, el área solicitante puede
   anular el pedido; si eso ocurre, se le notifica al proveedor y el proceso
   termina.

7. Cuando la mercadería llega, el Responsable de Compras la controla contra la
   orden de compra y registra la recepción. Por último, Finanzas paga la
   factura y el proceso termina.

**Entrega.** Escribí tu apellido como objeto de texto dentro de cada diagrama y
exportá `Apellido_pp.jpg` y `Apellido_sub.jpg`, más el archivo `.bpm`.

**Tiempo sugerido:** 45 minutos.

---

## Corrección — intento 1 (07-09-2026, `practica.bpm`)

**[NUESTRO]** Leído del XPDL con `scripts/bpm-dump.py` + parser de transiciones y grados.
Los dos diagramas se guardaron en el mismo `.bpm` (Diagrama 1 = principal,
Diagrama 2 = subproceso "Seleccionar Proveedor"). Punto 6 sin modelar.

### Sintaxis

| # | Dónde | Qué pasa | Patrón |
|---|---|---|---|
| 1 | Principal | **No hay evento de inicio.** "Registrar pedido de materiales" tiene grado de entrada 0. | 1 |
| 2 | Subproceso | **Tampoco hay evento de inicio.** "Pedir y registrar cotizaciones" solo recibe la flecha del loop. | 1 |
| 3 | Principal | **Rama colgada:** el 2º "Informar al empleado" (rama sin presupuesto) tiene grado de salida 0. Falta el fin. | 1 |
| 4 | Principal | **Evento intermedio múltiple con 2 flujos de secuencia salientes** = split incontrolado. Se disparan las dos ramas a la vez y "Controlar orden…" recibe 2 tokens: la cola corre dos veces. Mismo error que el EJ 6 (paralela cerrada con exclusiva). | — |
| 5 | Principal | "Cuando llega la mercadería" tipado como **Temporizador**. | — |
| 6 | Ambos | **No existe el pool Proveedor y hay cero flujos de mensaje.** El enunciado lo pide 4 veces. Criterio explícito del docente: otra organización = pool aparte. | 2 |

### Fidelidad y estilo
- Falta el punto 6 completo.
- Eventos nombrados con subordinada ("Cuando se cumple el plazo pactado") en vez de hecho
  narrado ("Plazo pactado vencido"). **Patrón 5.**
- Dos tareas homónimas "Informar al empleado".
- "Informar al empleado" de la rama de presupuesto quedó en el lane **Empleado** (y=677,
  lane 546-681); lo ejecuta Finanzas.
- **Sin objeto de texto con el apellido** en ninguno de los dos diagramas (cero artifacts).
- Tildes: "¿Llego mercaderia?", "¿Es Suficiente?".

### Bien resuelto
- Las 3 compuertas exclusivas con **todas** las salidas etiquetadas (Si/No).
- Ninguna compuerta hace trabajo: tarea → rombo nombrado como pregunta, las tres.
- Subproceso como SubFlow, con pool y lanes propios, y el loop bien cerrado.
- Cero flujos de secuencia cruzando pools.
- Asignación de lanes correcta salvo el caso de arriba.

### El punto 6: qué evento va

**Mensaje, no condicional.** Regla de elección:

| Tipo | Cuándo | Test |
|---|---|---|
| Mensaje | alguien manda algo | ¿hay emisor identificable? |
| Condicional | una condición del negocio se vuelve verdadera sola | "el stock baja de 10" — nadie lo manda |
| Temporizador | pasa el tiempo | |
| Señal | broadcast | lo escucha cualquiera que esté atento |

El **múltiple no sirve para bifurcar**: significa "cualquiera de varios disparadores prende
este evento" y tiene una sola salida. Va **compuerta basada en eventos** (rombo con
pentágono), tres ramas sin etiquetar apuntando a eventos de captura:

    Emitir orden de compra ──► ◈ basada en eventos
      ══► [Proveedor]           ├─ ◯ Mercadería recibida (mensaje) ──► Controlar orden y
      						  │                                       registrar recepción ──► Pagar factura ──► ◉
                                ├─ ◯ Plazo pactado vencido (timer) ─► Cancelar orden ──►
                                │                                     Notificar al empleado ══►[Proveedor] ──► ◉
                                └─ ◯ Anulación recibida (mensaje) ──► Notificar al proveedor ══►[Proveedor] ──► ◉

Desaparece la compuerta "¿Llegó mercadería?", hoy redundante. Alternativa válida: tarea
"Esperar recepción de mercadería" con dos eventos adjuntos al borde (timer + mensaje), que
es lo que hizo la resolución de junio 2026. Una u otra, no las dos.

⚠️ La mercadería llegando **no** se dibuja como flujo de mensaje: *"no es flujo de
información, esto es flujo de mercadería"* (docente, clase 13-04). El mensaje entrante es
el aviso o remito.

---

## Corrección — intento 2 (07-09-2026)

### Arreglado
Inicio en ambos diagramas · rama sin presupuesto cerrada en fin · **compuerta basada en
eventos correcta** (`<Route ExclusiveType="Event"/>` en el XPDL) con 3 salidas sin
etiquetar · "Plazo pactado vencido" con `<TriggerTimer/>` y nombre en hecho narrado ·
"Informar al empleado" movido al lane Finanzas · compuerta redundante "¿Llegó mercadería?"
eliminada · pool Proveedor creado.

### Pendiente

| # | Qué | Detalle |
|---|---|---|
| 1 | **Cero flujos de mensaje** | El pool Proveedor está pero sin conectar. Faltan 4 en el principal y 2 en el subproceso. |
| 2 | `Mercadería recibida` es **THROW** | `<TriggerResultMessage CatchThrow="THROW">`. Sobre relleno. Una event-based solo apunta a eventos de **captura**. |
| 3 | `Anulación recibida` es **None** | Sin tipo. Debe ser mensaje de captura. Mismo error que el TP grupal del Caso Hotel. |
| 4 | **Sin apellido** | Cero artifacts en los dos diagramas. |
| 5 | Subproceso sin pool Proveedor | Inconsistente con el principal. **Patrón 2.** |
| 6 | Menores | Dos "Informar al empleado" homónimos; "¿Es Suficiente?" con mayúscula. |

### El pool externo: cómo se conecta

**El pool vacío ES la caja negra.** En Bizagi los pools no se colapsan como los subprocesos:
un pool sin lanes ni elementos ya representa al participante como caja negra. No lleva
actividades.

El flujo de mensaje va **de un objeto del pool propio al borde del pool externo** (o al
revés). No necesita un elemento del otro lado. En la paleta, grupo de conectores →
**Message Flow** (punteada). Atajo: arrastrar un conector hasta otro pool lo convierte solo,
porque un flujo de secuencia no puede cruzar pools.

Verificación visual: **punteada, círculo hueco en el origen, punta de flecha hueca.**

Los que van:

| Desde | Hacia | Qué viaja |
|---|---|---|
| Emitir orden de compra a proveedor | pool Proveedor | la orden |
| pool Proveedor | Mercadería recibida | el **aviso de entrega**, no la mercadería |
| Notificar empleado y proveedor | pool Proveedor | la cancelación por vencimiento |
| Notificar anulación al proveedor | pool Proveedor | la anulación |
| *(subproceso)* Pedir y registrar cotizaciones | pool Proveedor | el pedido de cotización |
| *(subproceso)* pool Proveedor | Pedir y registrar cotizaciones | las cotizaciones |

`Anulación recibida` **no** lleva mensaje entrante: el emisor es el área solicitante, interna
(lane Empleado), y un flujo de mensaje solo cruza entre pools distintos. Evento de captura
sin emisor dibujado = aceptable (`repaso-parcial.md` 4.3).

**Regla visual:** sobre **blanco** = espero algo. Sobre **negro** = mando algo. Todo lo que
cuelga de una compuerta basada en eventos es blanco, siempre.
