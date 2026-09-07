# IPP — Simulacro Axure (parcial 07-09-2026)

> **[NUESTRO]** Enunciado inventado para practicar. No es de la cátedra.
> Construido con la misma estructura que el CU "Pedir un libro" del parcial 2022
> (`repaso-parcial.md` sección 5), combinando las piezas del CU del hotel
> (contador +/- y cálculo en el comprobante) con las del CU de libros
> (droplist → variable, filtro compuesto, orden mixto Text/Number, `Update Rows`,
> `Now`, número de operación incremental).
>
> ⚠️ **No se puede auditar un `.rp` desde afuera.** Axure lo guarda en formato
> binario propio, comprimido con un esquema que no es zip ni zlib (probado).
> A diferencia del `.bpm`, la corrección va por capturas del panel Interactions
> y del Preview.

---

## Enunciado — CU Reservar una función de cine

Actor primario e iniciador: **Cliente**. Precondición: **el cliente está logueado**.
Postcondición de éxito: **la reserva quedó registrada y las butacas disponibles fueron
actualizadas**.

**Paso 1.** El cliente selecciona el **género** y presiona "Buscar funciones". El sistema
muestra en **cabecera** el nombre del cliente y el género seleccionado, y lista las
funciones de ese género que tengan **butacas disponibles ≥ 1**, mostrando **película,
sala, horario, butacas y precio**, ordenadas por **"Horario más temprano"**.

- **1.a** — el cliente puede reordenar por: Horario más temprano, Horario más tarde,
  Precio más bajo, Precio más alto.

**Paso 2.** El cliente indica la **cantidad de entradas** (entre **1 y 6**, con botones
`-` y `+`, valor inicial **2**) y presiona "Reservar" sobre una función. El sistema
registra la reserva, **descuenta las butacas** y muestra el comprobante con: **número de
operación, fecha de hoy, cliente, película, horario, cantidad de entradas y total**.

- **2.a** — el cliente presiona "Cancelar" y vuelve al listado.

**Total = precio de la función × cantidad de entradas.**

**Entrega:** guardar como `Apellido_Nombre.rp`. **Tiempo sugerido: 60 minutos.**

### Dataset

Precios y butacas **pelados**, sin `$` ni separador de miles (si no, `Sort as: Number`
deja de funcionar).

| Genero | Pelicula | Sala | Horario | Butacas | Precio |
|---|---|---|---|---|---|
| Accion | Duro de matar | 1 | 14:30 | 40 | 6500 |
| Accion | Mad Max | 2 | 22:15 | 0 | 8000 |
| Accion | John Wick | 1 | 18:00 | 12 | 7000 |
| Drama | El padrino | 3 | 16:45 | 25 | 6000 |
| Drama | Perfectos desconocidos | 2 | 20:30 | 8 | 7500 |
| Drama | Whiplash | 3 | 12:00 | 0 | 5500 |

Dos géneros y **una función con 0 butacas en cada uno**: es lo que le permite al corrector
ver que el `≥ 1` está implementado.

---

## Corrección

Se completa cuando llegue el intento.
