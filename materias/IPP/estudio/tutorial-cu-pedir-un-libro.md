# CU Pedir un libro — tutorial completo de Axure RP 9

> **[CÁTEDRA]** Enunciado real:
> `fuentes/Axure_RP9/Caso_Pedir_un_Libro/CU_Pedir_un_Libro_con_repeater_IPP_v1_02.pdf`
> (Enrique Porta, v1.02, 17-05-2019). Es el CU que tomaron en el parcial del 08-08-2022.
>
> **Este documento es autocontenido**: no hay que sustituir nada mentalmente. Fusiona
> [`simulacro-axure.md`](simulacro-axure.md) (la mecánica, verificada contra el paso a paso
> de 36 páginas del CU Reservar habitación) con el enunciado y las capturas reales de este CU.
> Los otros dos archivos quedan como referencia; para hacer el prototipo alcanza con éste.
>
> Marcas: **[CÁTEDRA]** sale del material de la cátedra · **[WIKI]** verificado contra el TP
> del hotel · **[NUESTRO]** análisis propio.

**Tiempo total: ~55 minutos**, prueba incluida.

---

## Enunciado

**[CÁTEDRA]** Actor primario e iniciador: **Cliente**. Precondición: **el cliente está
logueado**. Postcondición de éxito: **el pedido quedó registrado. La existencia del libro
fue actualizada.**

**Paso 1.** El cliente selecciona la **categoría** del libro y presiona "Buscar libro". El
sistema muestra en **cabecera** nombre y apellido del cliente y la categoría seleccionada, y
lista los libros (**título, existencia y precio**) ordenados por **"Título de A a Z"**, que
respondan a la categoría seleccionada y tengan **existencia ≥ 1**.

- **1.a** — el cliente reordena por: Título de A a Z, Título de Z a A, Precio más bajo,
  Precio más alto.

**Paso 2.** El cliente elige un libro y presiona **Comprar**. El sistema registra el pedido,
**actualiza la existencia** del libro pedido, y muestra el comprobante con: **número de
pedido, fecha del pedido (now), nombre y apellido del cliente, y título del libro**.

- **2.a** — el cliente presiona **Cancelar**. **2.a.1** — termina el CU.

**Entrega:** guardar como `Apellido_Nombre.rp` y enviar por mail con asunto **"Parcial Axure"**
a la cuenta que indique el docente.

---

## Dataset

**[NUESTRO]** Los tres de Tecnología salen de la captura del enunciado; el resto es invento
para que el filtro por categoría tenga algo que filtrar.

| Categoria | Titulo | Existencia | Precio |
|---|---|---|---|
| Tecnologia | Aprendiendo UML 2.0 | 15 | 1900 |
| Tecnologia | UML Destilado | 20 | 1800 |
| Tecnologia | UML y Patrones | 3 | 2500 |
| Tecnologia | Clean Code | **0** | 2200 |
| Arte | Historia del Arte | 8 | 3100 |
| Arte | El Bosco | 4 | 2700 |
| Arte | Impresionismo | **0** | 1700 |
| Historia | Sapiens | 12 | 2400 |
| Historia | 1492 | 6 | 2000 |
| Negocios | El Metodo Lean Startup | 9 | 2600 |
| Negocios | Padre Rico Padre Pobre | 11 | 1500 |

Precios y existencias **pelados**, sin `$` ni separador de miles: si no, `Sort as: Number`
deja de funcionar.

**Los dos libros con existencia 0 son a propósito.** Son lo que le permite al corrector ver
que el `≥ 1` está implementado: la tabla tiene cuatro títulos de Tecnología y la pantalla
muestra tres.

---

## Bloque 0 — Setup (3 min)

`Project → Global Variables`. Cuatro, y los defaults no son opcionales:

| Variable | Default | Por qué |
|---|---|---|
| `Var_Cliente` | **Carlos Perez** | la precondición "cliente logueado" se modela con el default |
| `Var_Categoria` | (vacía) | la setea el botón Buscar |
| `Var_Titulo` | (vacía) | lo setea el botón Comprar |
| `Var_NroPedido` | **12361** | **numérico**: si queda vacía, `+1` concatena en vez de sumar |

Con 12361 de default, el primer pedido sale **12362**, que es el número de la captura del
enunciado. Detalle gratis.

No hace falta `Var_Precio`: **el comprobante de este CU no muestra el precio.**

Páginas: `DatosBusqueda`, `MostrarLibros`, `Comprobante`.

**Guardá ya como `Apellido_Nombre.rp`.** Y antes de arrancar, `Help → About`: **RP 9 no abre
archivos de RP 11.**

## Bloque 1 — DatosBusqueda (4 min)

Widgets: text field `Usuario` (arriba a la derecha), droplist `Categoria`, botón `Buscar`.

Droplist `Categoria` → **Edit List Items**: `Arte`, `Historia`, `Negocios`, `Tecnologia`.

⚠️ Los strings tienen que ser **idénticos** a los de la columna `Categoria` del repeater,
tilde por tilde. Si el droplist dice `Tecnología` y el repeater `Tecnologia`, la lista sale
vacía y perdés diez minutos buscando el error. Lo más seguro: **sin tilde en los dos lados**.

`Page Loaded` de la página:

    Set Text   Usuario  to value of Var_Cliente

Botón `Buscar` → `Click or Tap`:

    Set Variable Value   Var_Categoria to [[Categoria.selectedOption]]
    Open Link            MostrarLibros

Preview + Console: no sigas hasta ver que `Var_Categoria` se llena. Plan B si sale vacía:
`[[Categoria.text]]`.

## Bloque 2 — Repeater y datos (10 min)

En `MostrarLibros`, arrastrá el widget **Repeater** desde Libraries. Con el repeater
seleccionado, en el panel **Style**: nombre `Libros`, y tildar **Fit to Content in HTML**.

En el panel **DATA**: renombrar `Column0` como `Categoria` (doble click sobre el header), y
con **Add Column** agregar `Titulo`, `Existencia`, `Precio`. Cargar las 11 filas.

## Bloque 3 — Ítem del repeater (7 min)

**Doble click en el repeater** para abrir la ventana de diseño del ítem. Adentro: tres text
fields nombrados `Titulo`, `Existencia`, `Precio` + un Button `Comprar`.

Los encabezados `Título / Existencia / Precio` van **fuera** del repeater, en el canvas
—si no, se repiten en cada fila.

Volvé al canvas, seleccioná **el repeater** (no el ítem), evento `Item Loaded` → **un solo**
`Set Text` con **tres Add Target**:

    Titulo      to  "[[Item.Titulo]]"
    Existencia  to  "[[Item.Existencia]]"
    Precio      to  "[[Item.Precio]]"

**[WIKI]** Si en el Preview se ve sólo el primer dato, faltan los `Add Target`.

## Bloque 4 — Botón Comprar (6 min) — el más caro

**Tiene que estar DENTRO del ítem.** Afuera, `[[Item.…]]` no resuelve y `Rows: This` no tiene
fila actual: se cae el paso 2 entero.

`Click or Tap`, en este orden:

    1. Set Variable Value
         Var_Titulo     to "[[Item.Titulo]]"
         Var_NroPedido  to "[[Var_NroPedido + 1]]"
    2. Update Rows
         Repeater: Libros  | Rows: This
         Column: Existencia | Value: [[Item.Existencia - 1]]
    3. Open Link -> Comprobante

`Update Rows` está en `Add Action → Repeaters`. **Si no te ofrece `This`, estás editando desde
afuera del ítem.**

Es `- 1` pelado, no una variable: se compra un libro por vez. Esto cubre la postcondición
explícita del CU, *"La existencia del libro fue actualizada"*, y es lo que separa este CU del
de Reservar habitación, donde no se actualizaba nada.

**[WIKI]** Que el descuento no se vea al volver al listado **no es un bug**: el dataset del
repeater se reinicia en cada carga de página.

## Bloque 5 — Cabecera, filtro y orden por defecto (7 min)

Widgets fuera del repeater: `Usuario` y `CategoriaSeleccionada` (text fields de lectura) y el
droplist `OrdenadoPor`.

`Page Loaded` de `MostrarLibros`, **en este orden**:

    1. Set Text
         Usuario                to value of Var_Cliente
         CategoriaSeleccionada  to value of Var_Categoria
    2. Add Filter
         Libros | Name: CategoriaYExistencia
         Rule: [[Item.Categoria == Var_Categoria && Item.Existencia >= 1]]
         [x] Remove other filters
    3. Add Sort
         Libros | Name: TituloAZ
         Column: Titulo | Sort as: TEXT | Order: Ascending

**Esto es el paso 1 completo del CU.** Un solo `Add Filter` con regla compuesta, no dos
encadenados: con uno solo el tilde de "Remove other filters" va siempre puesto y deja de ser
trampa.

Si aparecen libros con existencia 0, forzá el número: `(Item.Existencia * 1) >= 1`.

## Bloque 6 — Droplist de orden (8 min)

`OrdenadoPor` → **Edit List Items**, con el primero **tildado por defecto**:

    Titulo de A a Z    <- tildado
    Titulo de Z a A
    Precio mas bajo
    Precio mas alto

`Selection Changed` → **Enable Cases** → cuatro casos con **Else If**, cada uno con
`Remove Sort (All)` **antes** del `Add Sort`:

| Caso | Column | Sort as | Order |
|---|---|---|---|
| Titulo de A a Z *(default)* | Titulo | **TEXT** | Ascending |
| Titulo de Z a A | Titulo | **TEXT** | Descending |
| Precio mas bajo | Precio | **NUMBER** | Ascending |
| Precio mas alto | Precio | **NUMBER** | Descending |

**Título va como TEXT.** Como Number, Axure lee el título como 0 y los dos criterios de título
no hacen absolutamente nada. Es el mismo error que con el Horario en el simulacro del cine.

## Bloque 7 — Comprobante (5 min)

Cuatro text fields: `Cbte_NroPedido`, `Cbte_Fecha`, `Cbte_Cliente`, `Cbte_Libro`.

`Page Loaded` → **un solo** `Set Text` con cuatro Add Target:

    Cbte_NroPedido  to value of Var_NroPedido
    Cbte_Cliente    to value of Var_Cliente
    Cbte_Libro      to value of Var_Titulo
    Cbte_Fecha      to [[Now.addHours(-3).toISOString().substr(8,2)]]/[[Now.addHours(-3).toISOString().substr(5,2)]]/[[Now.addHours(-3).toISOString().substr(0,4)]]

**Acá no hay dependencias de orden**, a diferencia del comprobante del hotel (donde
`Cbte_Costo` tenía que ir después del `Set Variable Value` de `Var_CantidadDias`): las tres
variables ya vienen cargadas desde el botón Comprar.

**[CÁTEDRA]** (*Consejos para cálculo con fechas*, v1.03): no uses
`[[Now.getDate()]]/[[Now.getMonth()]]/[[Now.getFullYear()]]` — sale con un dígito, y la captura
del enunciado muestra `01/05/2019` con dos. `toISOString()` es UTC, así que el `addHours(-3)`
evita que después de las 21:00 argentinas te adelante el día.

## Bloque 8 — El paso 2.a (1 min)

Botón `Cancelar`, **fuera** del repeater, abajo a la izquierda de `MostrarLibros`:

    Click or Tap -> Open Link -> DatosBusqueda

"Termina el CU". Es un flujo alternativo explícito del enunciado: si no lo cableás, falta un
requisito. Son diez segundos.

---

## Prueba de punta a punta (5 min)

Correla **dos veces con categorías distintas**, con la Console abierta:

1. Elegir categoría → Buscar
2. Cabecera con nombre y categoría
3. **Ningún libro con existencia 0 en la lista**
4. Orden inicial por título ascendente
5. Los cuatro criterios de orden, sin que se rompa el filtro
6. Comprar → comprobante con los cuatro datos y el número incrementado
7. Cancelar → vuelve a la búsqueda

Si algo sale vacío: nombre de variable mal escrito, o falta un `Add Target`.

## Los errores que se cobran

1. Botón Comprar **fuera** del ítem → se cae el paso 2 entero.
2. `Sort as: Number` en Título → los dos criterios de título no hacen nada.
3. Olvidar `Remove Sort → All` en alguno de los cuatro casos.
4. `Var_NroPedido` con default vacío → concatena en vez de sumar.
5. `Var_Cliente` sin default → cabecera y comprobante sin nombre.
6. Precios con `$` o puntos → muere el orden numérico.
7. String de la categoría distinto entre droplist y repeater → lista vacía.
8. Olvidar el `Update Rows` → falta una postcondición explícita del CU.
9. No cablear el botón Cancelar → falta el paso 2.a.
10. **Guardar con Axure RP 11.** `Help → About` antes de arrancar.

## Orden de sacrificio si vas corto

Primero se caen **dos de los cuatro criterios de orden** (dejá "Título de A a Z" y "Precio más
bajo", que demuestran Text y Number). Después, los libros con existencia 0 del dataset.

**Nunca se saca:** el filtro compuesto, el `Item Loaded`, el botón Comprar con `Update Rows`
(es postcondición explícita) y el comprobante completo.
