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

## Guía paso a paso (resolución de referencia)

**[NUESTRO]**, salvo donde diga [WIKI] (verificado contra el paso a paso de 36 páginas del CU
Reservar habitación) o [CÁTEDRA]. Tiempos para una hora.

### Bloque 0 — Setup (3 min)

`Project -> Global Variables`. Siete, y los defaults no son opcionales:

| Variable | Default | Por qué |
|---|---|---|
| `Var_Cliente` | **Juan Perez** | la precondición "cliente logueado" se modela con el default |
| `Var_Genero` | (vacía) | la setea el botón Buscar |
| `Var_CantEntradas` | **2** | valor inicial del enunciado. **Numérico**: vacía, `+1` concatena |
| `Var_Pelicula` | (vacía) | |
| `Var_Horario` | (vacía) | |
| `Var_Precio` | (vacía) | |
| `Var_NroOperacion` | **1000** | numérico, por lo mismo |

Páginas: `Inicio`, `MostrarFunciones`, `Comprobante`. Guardar ya como `Apellido_Nombre.rp`.

### Bloque 1 — Inicio (4 min)

Droplist `Genero` -> Edit List Items: `Accion`, `Drama`. **Sin tildes, idénticos a los del
repeater.** Botón "Buscar funciones" -> `Click or Tap`:

    Set Variable Value   Var_Genero to [[Genero.selectedOption]]
    Open Link            MostrarFunciones

Preview + Console: no seguir hasta que `Var_Genero` se llene. Plan B: `[[Genero.text]]`.

### Bloque 2 — Repeater y datos (10 min)

Repeater desde Libraries, nombrarlo `Funciones` en el panel **Style**, tildar **Fit to Content
in HTML**. Columnas: `Genero, Pelicula, Sala, Horario, Butacas, Precio` (la primera se renombra
desde `Column0`, el resto con Add Column). Las 6 filas del dataset, números pelados.

### Bloque 3 — Ítem del repeater (8 min)

Doble click en el repeater. Cinco widgets nombrados `Pelicula`, `Sala`, `Horario`, `Butacas`,
`Precio` + Button "Reservar". Volver al canvas, seleccionar **el repeater**, evento
`Item Loaded` -> **un** `Set Text` con **cinco Add Target**:

    Pelicula  to  "[[Item.Pelicula]]"
    Sala      to  "[[Item.Sala]]"
    Horario   to  "[[Item.Horario]]"
    Butacas   to  "[[Item.Butacas]]"
    Precio    to  "[[Item.Precio]]"

[WIKI] Si en el Preview se ve solo el primer dato, faltan los `Add Target`.

### Bloque 4 — Botón Reservar (6 min) — el más caro

**DENTRO del ítem.** Afuera, `[[Item.…]]` no resuelve y `Rows: This` no tiene fila actual:
se cae el paso 2 entero. `Click or Tap`, en orden:

    1. Set Variable Value
         Var_Pelicula      to "[[Item.Pelicula]]"
         Var_Horario       to "[[Item.Horario]]"
         Var_Precio        to "[[Item.Precio]]"
         Var_NroOperacion  to "[[Var_NroOperacion + 1]]"
    2. Update Rows
         Repeater: Funciones | Rows: This
         Column: Butacas     | Value: [[Item.Butacas - Var_CantEntradas]]
    3. Open Link -> Comprobante

`Update Rows` está en `Add Action -> Repeaters`. Si no ofrece **This**, estás editando desde
afuera del ítem. Que el descuento no se vea al volver **no es un bug**: el dataset se reinicia
en cada carga de página.

### Bloque 5 — Cabecera, filtro y orden por defecto (7 min)

`Page Loaded` de MostrarFunciones, en este orden:

    1. Set Text
         Cab_Cliente    to value of Var_Cliente
         Cab_Genero     to value of Var_Genero
         CantEntradas   to value of Var_CantEntradas
    2. Add Filter
         Funciones | Name: GeneroYButacas
         Rule: [[Item.Genero == Var_Genero && Item.Butacas >= 1]]
         [x] Remove other filters
    3. Add Sort
         Funciones | Name: HorarioTemprano
         Column: Horario | Sort as: TEXT | Order: Ascending

**Es el paso 1 completo del CU.** Un solo `Add Filter` con regla compuesta, no dos encadenados:
con uno solo el tilde va siempre puesto y deja de ser trampa. Si aparecen funciones con 0
butacas, forzar el número: `(Item.Butacas * 1) >= 1`.

### Bloque 6 — Contador de entradas (5 min)

Botones `-` y `+` **fuera** del repeater. `Click or Tap` -> Add Case -> Condition Builder:

    Si  value of Var_CantEntradas  is greater than  "1"
          Set Variable Value  Var_CantEntradas to "[[Var_CantEntradas - 1]]"
          Set Text            CantEntradas     to value of Var_CantEntradas

El `+` igual, con `is less than "6"` y `+ 1`. La condición **es** la validación "entre 1 y 6".

### Bloque 7 — Droplist de orden (8 min)

`OrdenadoPor` -> Edit List Items (el primero tildado por defecto). `Selection Changed` ->
**Enable Cases** -> 4 casos con **Else If**, cada uno con `Remove Sort (All)` antes del
`Add Sort`:

| Caso | Column | Sort as | Order |
|---|---|---|---|
| Horario más temprano *(default)* | Horario | **TEXT** | Ascending |
| Horario más tarde | Horario | **TEXT** | Descending |
| Precio más bajo | Precio | **NUMBER** | Ascending |
| Precio más alto | Precio | **NUMBER** | Descending |

**Horario va como TEXT.** Como Number, Axure lee `"14:30"` como 0 y no ordena. Funciona como
texto porque las horas están con dos dígitos.

### Bloque 8 — Comprobante (7 min)

Siete widgets + botón "Cancelar". `Page Loaded` -> **un** `Set Text` con siete Add Target:

    Cbte_NroOperacion  to value of Var_NroOperacion
    Cbte_Cliente       to value of Var_Cliente
    Cbte_Pelicula      to value of Var_Pelicula
    Cbte_Horario       to value of Var_Horario
    Cbte_CantEntradas  to value of Var_CantEntradas
    Cbte_Total         to [[Var_Precio * Var_CantEntradas]]
    Cbte_Fecha         to [[Now.toISOString().substr(8,2)]]/[[Now.toISOString().substr(5,2)]]/[[Now.toISOString().substr(0,4)]]

Botón Cancelar -> `Open Link -> MostrarFunciones`.

**Acá no hay dependencias de orden**, a diferencia del comprobante del hotel (donde
`Cbte_Costo` iba después del `Set Variable Value` de `Var_CantidadDias`): `Var_Precio` y
`Var_CantEntradas` ya vienen cargadas.

[CÁTEDRA] (*Consejos para cálculo con fechas* v1.03): evitar
`[[Now.getDate()]]/[[Now.getMonth()]]/[[Now.getFullYear()]]`, sale con un dígito.
`toISOString()` es UTC: después de las 21:00 argentinas adelanta el día -> `Now.addHours(-3)`.

### Prueba de punta a punta (5 min)

Dos veces con géneros distintos: género -> Buscar -> cabecera -> ninguna función con 0 butacas
-> orden por horario ascendente -> los cuatro criterios sin que se rompa el filtro -> `+`/`-`
topando en 1 y 6 -> Reservar -> comprobante con los siete datos y el total -> Cancelar.
Console abierta. Si algo sale vacío: nombre de variable mal escrito, o falta un Add Target.

### Los errores que se cobran

1. Botón Reservar **fuera** del ítem -> se cae el paso 2 entero.
2. `Sort as: Number` en Horario -> los dos criterios de horario no hacen nada.
3. Olvidar `Remove Sort -> All` en alguno de los cuatro casos.
4. `Var_CantEntradas` / `Var_NroOperacion` con default vacío -> concatena o NaN.
5. `Var_Cliente` sin default -> cabecera y comprobante sin nombre.
6. Precios con `$` o puntos -> muere el orden numérico.
7. String del género distinto entre droplist y repeater -> lista vacía.
8. **Guardar con Axure RP 11.** Verificar `Help -> About` antes de arrancar: RP 9 no abre RP 11.

**Orden de sacrificio si va corto:** primero el contador `+`/`-` (fijo en 2), después dos de
los cuatro criterios de orden (dejar Horario temprano y Precio más bajo, que muestran Text y
Number). **Nunca se saca:** el filtro compuesto, el `Item Loaded`, el botón Reservar con
`Update Rows` (postcondición explícita del CU) y el comprobante completo.
