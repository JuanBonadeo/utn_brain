# IPP — Guía paso a paso: prototipo Axure "Pedir un libro"

> **[CÁTEDRA]** CU `fuentes/Axure_RP9/Caso_Pedir_un_Libro/CU_Pedir_un_Libro_con_repeater_IPP_v1_02.pdf`
> (Enrique Porta, v1.02, 17-05-2019). Es el mismo CU que tomaron en el parcial 2022.
> Nivel usuario · alcance sistema · caja negra · instanciación real · interacción dialogal ·
> usabilidad no contemplada. Actor primario e iniciador: **Cliente**.
> Precondición: **el cliente está logueado**. Postcondición de éxito: **el pedido quedó
> registrado y la existencia del libro fue actualizada**.
>
> Las categorías, los libros y el layout salen de las **capturas de la cátedra**
> (pantallas de Inicio, listado y comprobante).
>
> Complementa `repaso-parcial.md` sección 5 (cronograma y trampas). Acá está la receta
> operativa en orden de construcción.

## 1. Setup

`Project → Global Variables`:

| Variable | Default | Para qué |
|---|---|---|
| `Var_Cliente` | `Carlos Perez` | la precondición "cliente logueado" se modela con el default |
| `Var_Categoria` | *(vacía)* | la setea el botón Buscar |
| `Var_TituloLibro` | *(vacía)* | la setea el botón Comprar |
| `Var_NroPedido` | `12361` | +1 en cada compra → el primero sale 12362, como la captura |

Pages: `Inicio`, `MostrarLibros`, `Comprobante`. Guardar ya como `Apellido_Nombre.rp`.

## 2. Página Inicio

Text Field `Usuario` (arriba a la derecha) · Droplist `Categoria` · Primary Button `Buscar`.

Droplist → Edit List Items: **Arte, Historia, Negocios, Tecnología**.

    (página)  Page Loaded   → Set Text: Usuario to value of Var_Cliente
    Buscar    Click or Tap  → Set Variable Value Var_Categoria to [[Categoria.selectedOption]]
                            → Open Link: MostrarLibros

Preview + Console: no seguir hasta ver `Var_Categoria` con valor.

## 3. Repeater y datos

Repeater → Style: nombre **`Libros`**, tildar **Fit to Content in HTML**.
Columnas: `Categoria`, `Titulo`, `Existencia`, `Precio`.

| Categoria | Titulo | Existencia | Precio |
|---|---|---|---|
| Tecnología | Aprendiendo UML 2.0 | 15 | 1900 |
| Tecnología | UML Destilado | 20 | 1800 |
| Tecnología | UML y Patrones | 3 | 2500 |
| Tecnología | Clean Code | 0 | 3200 |
| Arte | Historia del Arte | 8 | 2100 |
| Arte | El Renacimiento | 0 | 1700 |
| Historia | Sapiens | 12 | 2800 |
| Negocios | El Metodo Lean Startup | 5 | 2300 |

Los tres primeros son los de la captura de la cátedra. Los dos con **existencia 0** son a
propósito: es lo que le permite al corrector ver que el `>= 1` está implementado.

⚠️ Precios y existencias **pelados** (sin `$` ni separador de miles), y **`Tecnología`
escrito idéntico** en el droplist y en el repeater — copiar y pegar el mismo string.

## 4. Ítem del repeater

Doble click en el repeater → Text Fields `Titulo`, `Existencia`, `Precio` + Button `Comprar`.

Volver al canvas, **seleccionar el repeater**, evento `Item Loaded` → **un** `Set Text` con
**tres Add Target**: `[[Item.Titulo]]`, `[[Item.Existencia]]`, `[[Item.Precio]]`.

Si en el Preview se ve solo el título, faltan los Add Target — no está roto.

## 5. Botón Comprar (DENTRO del ítem)

`Click or Tap`, **en este orden**:

    1. Set Variable Value  Var_TituloLibro  to  [[Item.Titulo]]
    2. Set Variable Value  Var_NroPedido    to  [[Var_NroPedido + 1]]
    3. Update Rows         Libros | Rows: This | Column: Existencia | [[Item.Existencia - 1]]
    4. Open Link           Comprobante

`Update Rows` está en `Add Action → Repeaters`. Si Rows no ofrece **This**, estás editando
desde afuera del ítem.

Fuera del repeater se cae todo el paso 2 junto: `[[Item.Titulo]]` no resuelve,
`[[Item.Existencia - 1]]` tampoco y `Rows: This` no tiene fila actual.

## 6. Page Loaded de MostrarLibros

**En este orden** — es el paso 1 completo del CU:

    1. Set Text     Usuario   to value of Var_Cliente
                    Categoria to value of Var_Categoria        (Add Target)
    2. Add Filter   Libros | Name: CategoriaYStock
                    Rule: [[Item.Categoria == Var_Categoria && Item.Existencia >= 1]]
                    ☑ Remove other filters
    3. Add Sort     Libros | Name: TituloAZ | Titulo | Sort as: TEXT | Ascending

**Un solo `Add Filter`** con regla compuesta, no dos encadenados como en el hotel: con uno
solo el tilde va siempre puesto y deja de ser trampa.

Si aparecen libros con existencia 0, forzar el número:
`[[Item.Categoria == Var_Categoria && (Item.Existencia * 1) >= 1]]`.

## 7. Droplist OrdenadoPor

Items: `Titulo de A a Z` (Selected por defecto), `Titulo de Z a A`, `Precio más bajo`,
`Precio más alto`.

`Selection Changed` → **Enable Cases** → 4 casos con **Else If**. Cada uno:

    If selected option of This equals <texto del ítem>
        Remove Sort → Libros, Sort: All        ← NO es opcional
        Add Sort    → Libros | <columna> | <tipo> | <orden>

| Caso | Column | Sort as | Order |
|---|---|---|---|
| Titulo de A a Z | Titulo | **Text** | Ascending |
| Titulo de Z a A | Titulo | **Text** | Descending |
| Precio más bajo | Precio | **Number** | Ascending |
| Precio más alto | Precio | **Number** | Descending |

⚠️ **`Sort as: Text` para Titulo.** En el hotel los cuatro eran Number y la mano va sola;
con Titulo como Number, Axure lo lee como 0 y no ordena.

## 8. Botón Cancelar

En MostrarLibros, fuera del repeater: `Click or Tap` → `Open Link` → `Inicio`. (Paso 2.a.)

## 9. Página Comprobante

Text Fields `Cbte_NroPedido`, `Cbte_Fecha`, `Cbte_Cliente`, `Cbte_Libro`.
`Page Loaded` → un `Set Text` con cuatro Add Target:

    Cbte_NroPedido  [[Var_NroPedido]]
    Cbte_Fecha      [[Now.toISOString().substr(8,2)]]/[[Now.toISOString().substr(5,2)]]/[[Now.toISOString().substr(0,4)]]
    Cbte_Cliente    value of Var_Cliente
    Cbte_Libro      value of Var_TituloLibro

**Sin dependencias de orden**, a diferencia del comprobante del hotel.
No usar `getDate()/getMonth()/getFullYear()` (mes de un dígito). `toISOString()` es UTC:
después de las 21:00 hora argentina adelanta el día → `Now.addHours(-3).toISOString()`.

## 10. Prueba y entrega

Dos vueltas completas con categorías distintas:

- [ ] cabecera con cliente y categoría
- [ ] solo la categoría elegida, **sin los de existencia 0**
- [ ] llega ordenado por Título A-Z
- [ ] los 4 criterios andan y **el filtro no se rompe** al cambiarlos
- [ ] Comprar → comprobante con nro incrementado, fecha DD/MM/AAAA, cliente y título
- [ ] Cancelar vuelve a Inicio
- [ ] Console con las 4 variables cargadas

`File → Save As → Apellido_Nombre.rp`. Enviar con asunto **"Parcial Axure"**.
**Hacerlo aunque falte algo.**

Que la existencia descontada no se vea al volver **no es un bug**: el dataset del repeater se
reinicia en cada carga de página y `Open Link` recarga. No debuguearlo.

⚠️ **RP 9 no abre archivos de RP 11.** Verificar la versión antes de arrancar.
