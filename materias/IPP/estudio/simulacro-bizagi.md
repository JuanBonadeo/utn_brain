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

## Corrección

Se completa después de la entrega, contrastando el `.bpm` con `scripts/bpm-dump.py`.
