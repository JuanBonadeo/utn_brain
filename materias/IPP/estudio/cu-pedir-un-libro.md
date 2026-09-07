# CU Pedir un libro — mapeo contra el simulacro de Axure

> **[CÁTEDRA]** Enunciado real: `fuentes/Axure_RP9/Caso_Pedir_un_Libro/CU_Pedir_un_Libro_con_repeater_IPP_v1_02.pdf`
> (Enrique Porta, v1.02, 17-05-2019). Es el mismo CU que tomaron en el parcial del 08-08-2022.
>
> **No hay receta nueva acá.** La guía paso a paso está en
> [`simulacro-axure.md`](simulacro-axure.md). Este documento es sólo el delta: qué cambia
> del simulacro del cine a este caso.

---

## La buena noticia: este CU es el simulacro MENOS dos bloques

| Bloque del simulacro | En "Pedir un libro" |
|---|---|
| 0 — Setup | igual |
| 1 — Inicio | igual (droplist Categoría en vez de Género) |
| 2 — Repeater y datos | igual, con 4 columnas en vez de 6 |
| 3 — Ítem del repeater | igual, 3 widgets en vez de 5 |
| 4 — Botón (el más caro) | igual, pero el descuento es fijo: `- 1` |
| 5 — Cabecera, filtro y orden | igual |
| **6 — Contador de entradas** | **NO VA.** Se compra un libro, no hay cantidad |
| 7 — Droplist de orden | igual, con Título en vez de Horario |
| 8 — Comprobante | **4 campos en vez de 7, y sin cálculo de total** |

Te ahorrás el contador `+/-` y el `Cbte_Total = Precio × Cantidad`. Son los dos únicos
lugares del simulacro con aritmética además del descuento de stock.

## Tabla de reemplazos

| Simulacro (cine) | Este CU (libros) |
|---|---|
| `Var_Genero` | `Var_Categoria` |
| `Var_Pelicula` | `Var_Titulo` |
| `Var_NroOperacion` | `Var_NroPedido` |
| `Var_CantEntradas` | *(no existe)* |
| `Var_Precio` | *(no hace falta: el comprobante no muestra precio)* |
| repeater `Funciones` | repeater `Libros` |
| columnas `Genero, Pelicula, Sala, Horario, Butacas, Precio` | `Categoria, Titulo, Existencia, Precio` |
| `Butacas >= 1` | `Existencia >= 1` |
| botón "Reservar" | botón "Comprar" |

## Los tres puntos donde el texto cambia de verdad

**1. El filtro compuesto** (Bloque 5, `Page Loaded` de MostrarLibros):

    Add Filter
      Libros | Name: CategoriaYExistencia
      Rule: [[Item.Categoria == Var_Categoria && Item.Existencia >= 1]]
      [x] Remove other filters

Un solo `Add Filter` con regla compuesta, igual que en el simulacro. Si aparecen libros con
existencia 0, forzar el número: `(Item.Existencia * 1) >= 1`.

**2. El `Update Rows` del botón Comprar** (Bloque 4, **dentro del ítem**):

    1. Set Variable Value
         Var_Titulo     to "[[Item.Titulo]]"
         Var_NroPedido  to "[[Var_NroPedido + 1]]"
    2. Update Rows
         Repeater: Libros | Rows: This
         Column: Existencia | Value: [[Item.Existencia - 1]]
    3. Open Link -> Comprobante

Es `- 1` pelado, no `- Var_CantEntradas`. Cubre la postcondición del CU:
*"La existencia del libro fue actualizada."*

**3. El orden por Título va como TEXT** (Bloque 7):

| Caso del droplist | Column | Sort as | Order |
|---|---|---|---|
| Título de A a Z *(default, tildado)* | Titulo | **TEXT** | Ascending |
| Título de Z a A | Titulo | **TEXT** | Descending |
| Precio más bajo | Precio | **NUMBER** | Ascending |
| Precio más alto | Precio | **NUMBER** | Descending |

Misma lección que el Horario del simulacro: como Number, Axure lee el título como 0 y no
ordena nada. Y el mismo `Add Sort` con `Titulo / TEXT / Ascending` va en el `Page Loaded`,
porque el CU dice que la lista arranca ordenada por "Título de A a Z".

## Dataset

**[NUESTRO]** Los tres de Tecnología salen de la captura del enunciado; el resto es
invento para que el filtro por categoría tenga algo que filtrar.

| Categoria | Titulo | Existencia | Precio |
|---|---|---|---|
| Tecnologia | Aprendiendo UML 2.0 | 15 | 1900 |
| Tecnologia | UML Destilado | 20 | 1800 |
| Tecnologia | UML y Patrones | 3 | 2500 |
| Tecnologia | Clean Code | **0** | 2200 |
| Arte | Historia del Arte | 8 | 3100 |
| Arte | El Bosco | 4 | 2700 |
| Historia | Sapiens | 12 | 2400 |
| Historia | 1492 | 6 | 2000 |
| Negocios | El Metodo Lean Startup | 9 | 2600 |
| Negocios | Padre Rico Padre Pobre | 11 | 1500 |

**El libro con existencia 0 es a propósito.** Sin él no podés demostrar que el filtro
`Existencia >= 1` hace algo. Si el docente prueba con Tecnología y ve cuatro títulos en la
tabla pero tres en pantalla, el filtro quedó probado sin decir una palabra.

Números pelados: sin `$` ni separador de miles, o el orden por Precio como Number se rompe.

## Las pantallas, según las capturas del enunciado

**Pantalla 1 — DatosBusqueda.** Arriba a la derecha `Usuario` (text field) con el nombre.
Abajo a la izquierda `Categoría` (droplist: Arte, Historia, Negocios, Tecnología) y el
botón `Buscar`.

**Pantalla 2 — MostrarLibros.** Arriba a la derecha `Usuario`. A la izquierda `Categoria`
(text field de sólo lectura con la categoría elegida). A la derecha `Ordenado por`
(droplist). Debajo, encabezados `Título / Existencia / Precio` **fuera** del repeater, y el
repeater con las filas + botón `Comprar` por fila. Abajo a la izquierda, botón `Cancelar`
**fuera** del repeater.

**Pantalla 3 — Comprobante.** Cuatro campos apilados: `Pedido Nro`, `Fecha`, `Cliente`, `Libro`.

    Page Loaded -> un Set Text con cuatro Add Target:
      Cbte_NroPedido to value of Var_NroPedido
      Cbte_Cliente   to value of Var_Cliente
      Cbte_Libro     to value of Var_Titulo
      Cbte_Fecha     to [[Now.addHours(-3).toISOString().substr(8,2)]]/[[Now.addHours(-3).toISOString().substr(5,2)]]/[[Now.addHours(-3).toISOString().substr(0,4)]]

La captura muestra `01/05/2019`, con día y mes de dos dígitos: por eso `toISOString()` y no
`Now.getDate()`, que sale con un dígito. El `addHours(-3)` es porque ISO es UTC y después de
las 21:00 argentinas te adelanta el día.

## El paso 2.a, que es la única pieza que el simulacro no tiene

    2.a  El cliente selecciona el botón cancelar
    2.a.1  Termina el CU.

El `Cancelar` de la **pantalla 2** (no el del comprobante) corta el caso de uso: `Click or Tap`
-> `Open Link` -> `DatosBusqueda`. Es un flujo alternativo del CU, así que si no lo cableás,
falta un requisito explícito del enunciado. Son diez segundos.

## Entrega

**[CÁTEDRA]** Nota al pie del enunciado, textual:

- Guardar el prototipo en `Apellido_Nombre.rp`
- Enviar por mail con asunto **"Parcial Axure"** a la cuenta que indique el docente

Confirmá el canal el día del parcial: en 2026 Bizagi fue por Classroom, pero para Axure el
enunciado de 2019/2022 dice mail. Si dice mail, copiá el asunto tal cual.
