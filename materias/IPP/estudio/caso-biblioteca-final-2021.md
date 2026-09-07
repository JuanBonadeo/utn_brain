# IPP — Caso "Gestión de préstamo en una biblioteca" (final 2021 v2)

> **[CÁTEDRA]** Enunciado de un final, versión 2021 v2 (v03, LRI 4-oct-2021).
> ⚠️ **No es el caso de la biblioteca que el docente hizo en clase.** El de clase
> (rúbrica de tipos de tarea, `repaso-parcial-cursada.md` 1.5) tiene al bibliotecario
> recibiendo la solicitud y buscando el libro. Este tiene reserva, cancelación,
> no-retiro, devolución y sanciones. Mismo dominio, estructura distinta.

## Enunciado

1. El proceso comienza cuando un lector registra en una aplicación la reserva de un libro
   para un determinado día.
2. Cuando el lector retira el libro de la biblioteca, el bibliotecario registra mediante una
   aplicación el préstamo del libro.
3. La fecha teórica de devolución se calcula como 2 días hábiles después de la fecha de retiro.
4. Cuando el lector decide cancelar la reserva, puede cancelar la reserva mediante una aplicación.
5. Si el lector no retira el libro antes de las 10 AM del día de reserva, el bibliotecario
   mediante una aplicación registra la reserva como anulada.
6. Cuando el lector devuelve el libro en la biblioteca, el bibliotecario recibe el libro y luego
   registra la devolución del libro mediante una aplicación.
7. Si el lector devuelve el libro después de la fecha teórica de devolución, el bibliotecario le
   hace firmar al lector el registro de sanciones.
8. Se pide realizar un diagrama del proceso descripto utilizando la notación BPMN.

## Resolución propuesta **[NUESTRO]**

### Pools
- **`Lector`** — vacío, sin lanes. Caja negra.
- **`Biblioteca`** — un lane: **`Bibliotecario`**.

*(El lector es de otra organización → pool aparte, criterio explícito del docente. Ponerlo
como lane también pasa —precedente del TP grupal del Caso Hotel—, pero como pool sale mejor
la carrera del punto 5.)*

### Flujo

    ◉ Reserva recibida  (inicio de MENSAJE)
      → ◈ compuerta BASADA EN EVENTOS, 3 salidas sin etiquetar, todas a eventos de captura:
          ├─ ✉ Libro retirado  (mensaje)
          │    → 👤 Registrar el préstamo del libro
          │    → 📜 Calcular fecha teórica de devolución
          │    → ✋ Recibir el libro
          │    → 👤 Registrar la devolución del libro
          │    → ◇ ¿Devolvió el libro fuera de término?
          │         Sí → ✋ Hacer firmar el registro de sanciones ─┐
          │         No →─────────────────────────────────────────┴→ ◉ Préstamo finalizado
          ├─ ✉ Cancelación recibida  (mensaje)
          │    → 👤 Registrar la cancelación de la reserva → ◉ Reserva cancelada
          └─ 🕐 Llegaron las 10 AM del día de reserva  (temporizador)
               → 👤 Registrar la reserva como anulada → ◉ Reserva anulada

### Tipos de tarea

El enunciado dice **"mediante una aplicación" cinco veces**: son las cinco de usuario.

| Tarea | Tipo |
|---|---|
| Registrar el préstamo del libro | 👤 Usuario |
| Calcular fecha teórica de devolución | 📜 Script |
| Registrar la cancelación de la reserva | 👤 Usuario |
| Registrar la reserva como anulada | 👤 Usuario |
| **Recibir el libro** | ✋ **Manual** |
| Registrar la devolución del libro | 👤 Usuario |
| **Hacer firmar el registro de sanciones** | ✋ **Manual** |

Script vs Servicio: *"el script lo programo en el lenguaje del BPM, en la misma herramienta"*;
servicio sería invocar un web service externo.

### Flujos de mensaje — solo dos

- `Lector` → **Reserva recibida**
- `Lector` → **Cancelación recibida**

Son los dos que el enunciado marca como "mediante una aplicación" = información.
**El retiro y la devolución del libro NO llevan flujo de mensaje**: el libro es físico, y
*"no es flujo de información, esto es flujo de mercadería"* (docente, 13-04).

### Las dos trampas

1. **El punto 7 NO es una carrera.** "Si devuelve después de la fecha teórica" se evalúa
   *después* de la devolución, comparando fechas → **compuerta exclusiva**, no temporizador.
   Un timer ahí modelaría "si no devuelve nunca", que el enunciado no pide.
2. **Los puntos 2, 4 y 5 hay que leerlos juntos**, no por separado: son tres cosas
   mutuamente excluyentes que compiten después de la reserva → compuerta basada en eventos.

### Recuento para la verificación final

1 inicio · 3 fines · 7 tareas · 1 compuerta basada en eventos · 1 exclusiva (etiquetada Sí/No)
· 3 eventos de captura · 2 flujos de mensaje. **Sin subproceso** — este enunciado no lo pide.
