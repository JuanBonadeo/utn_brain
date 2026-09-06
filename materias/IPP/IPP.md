# Intro a la Práctica Profesional — Wiki

## Índice
1. Unidad 1 — Modelado de procesos con BPMN (Bizagi Modeler)
2. Unidad 2 — Prototipado con Axure RP 9

> **Parcial**: el repaso consolidado está en
> [`estudio/repaso-parcial.md`](estudio/repaso-parcial.md) — banco de teoría BPMN
> con respuestas verificadas, los distractores que la cátedra recicla, la
> corrección del caso de junio 2026 y el plan cronometrado de Axure.

## Desarrollo

### Unidad 1 — Modelado de procesos con BPMN (Bizagi Modeler)

#### Conceptos clave

**Pool** = participante / organización autónoma. **Lane** = rol o área dentro de
ese participante. Regla operativa: todo lo que pasa puertas adentro de la
organización va en **un solo pool con lanes**. El actor externo (cliente,
organismo de control, candidato, banda) va en **pool aparte y colapsado** — no se
modela su proceso interno, solo se le manda/recibe mensajes.

**Los dos tipos de flujo, y el error que más descuenta:**

| Flujo | Trazo | Dónde |
|---|---|---|
| Secuencia | línea llena, flecha sólida | **solo** dentro del mismo pool |
| Mensaje | línea punteada, flecha hueca | **solo** entre pools distintos |

Cruzar la frontera de un pool con línea llena es error de sintaxis BPMN, no de
criterio. Nunca se perdona.

**Los tres gateways.** Es lo que realmente se evalúa:

| Gateway | Símbolo | Semántica | ¿Etiqueta las salidas? |
|---|---|---|---|
| Exclusivo | rombo con **X** | se toma **un solo** camino | **Sí** (Sí/No, condición) |
| Paralelo | rombo con **+** | se toman **todos** los caminos | **No** |
| Inclusivo | rombo con **O** | se toman **uno o más** caminos | **Sí** |

Reglas que se controlan al corregir:
- El gateway **no hace trabajo**, solo enruta. La pregunta va en el rombo; la
  tarea que consigue el dato va **antes**.
- Gateway que abre, gateway que cierra, **del mismo tipo**.
- El paralelo no se etiqueta, porque salen todas las ramas.

**Nombres.** Tarea = infinitivo + sustantivo ("Registrar préstamo", "Elaborar
respuesta"). Evento = participio o sustantivo ("Requerimiento recibido").
Gateway = pregunta ("¿Respuesta definitiva?").

**Cierre.** Todo camino termina en un evento de fin (círculo de borde grueso).
Rama colgada = error.

**Eventos que aparecen en los enunciados de la cátedra:**
- **Temporizador** (reloj): "si no responde en una semana", "dos semanas antes
  de la salida", "dentro de las dos semanas siguientes".
- **Gateway basado en eventos** (rombo con pentágono): cuando la carrera es
  entre *recibir un mensaje* y *que venza un plazo*. Es el patrón de Quejas y
  Reclamos — no se resuelve con un exclusivo común.
- **Evento adjunto al borde** (boundary): "puede ser cancelado en cualquier
  momento". Se dibuja pegado al borde de la actividad/subproceso, no en el flujo.
- **Subproceso colapsado** (rectángulo con +): cuando el enunciado dice
  explícitamente "no detallado en este enunciado".

#### Desarrollo — los 7 casos del curso y qué patrón evalúa cada uno

Fuente: `PPT_Casos_Curso_BPMN_v1_02_Enunciados.pdf` (Enrique Porta, cátedra IPP,
UTN FRRo). Si el parcial da un caso, con alta probabilidad es uno de estos o uno
de la misma forma. Reconocer el patrón es la mitad del ejercicio.

**1. Requerimiento Organismo de Control** — *loop de revisión/aprobación.*
Pools: la organización (lanes: Director, Persona asignada) + Organismo de Control
colapsado. El Director revisa y decide si es definitiva; si no, **vuelve** a la
persona asignada. Ese retorno es un flujo de secuencia hacia atrás desde un
gateway exclusivo. Entrada y salida al Organismo, por flujo de mensaje.

**2. Gestión Evaluación** — *secuencial con handoff entre lanes.*
Lanes: RRHH, Empleado, Jefe inmediato, Jefe de RRHH. Autoevaluación → evaluación
del jefe → notificación → reporte. Sin gateways complejos: lo que se evalúa acá
es la correcta asignación de cada tarea a su lane.

**3. Publicación Artículos** — *el ejercicio de los tres gateways.* Tres
variantes del mismo proceso, y cada una pide un gateway distinto:
- **A**: redacción y diseño **en paralelo**, diagramación cuando ambas terminan
  → gateway **paralelo** (+) para abrir y otro (+) para cerrar.
- **B**: diseño solo si el artículo tiene ilustración, redacción siempre
  → **paralelo (+) para abrir**, y sobre la rama de diseño un **exclusivo (X)**
  "¿Tiene ilustraciones?" con by-pass por el "No"; cierra con **paralelo (+)**.
- **C**: lo mismo que B, precedido de un **exclusivo (X) de tres salidas**
  (Rechazado → fin / Aprobado → sigue / Correcciones necesarias → "Realizar
  correcciones" y vuelve a "Revisar artículo").

⚠️ **Corrección.** Una versión anterior de esta wiki decía que B se resolvía con
un gateway **inclusivo** y que usar un exclusivo era la trampa. **Es al revés.**
La solución oficial de la cátedra
(`fuentes/Introducción a la Práctica Profesional/Trabajo Práctico/Ejercicio 3 Caso Articulos/Caso_Articulos.pdf`,
fechada 11/05/2026) resuelve B y C con **paralelo + exclusivo**, no con inclusivo.

El inclusivo también sería semánticamente válido, pero no es lo que responde la
cátedra. El join paralelo funciona igual porque las dos ramas del exclusivo
desembocan en él: llegan dos tokens en cualquiera de los dos casos.

**4. Quejas y reclamos** — *el más completo.* Combina:
- **Paralelo**: el envío del formulario al cliente y la evaluación del director
  arrancan a la vez.
- **Gateway basado en eventos**: el formulario vuelve dentro de dos semanas
  (evento de mensaje) **o** vence el plazo (evento temporizador). Si vence, se
  genera un reporte vacío — ojo, el proceso **no termina** ahí.
- **Loop**: "Procesar la Queja" se repite hasta que el director acepta el
  resultado.

Lanes: Logística, Servicio Post-Venta (empleado), Director de Servicio
Post-Venta. Pool aparte para el Cliente.

**5. Selección de Personal** — *tres loops + subproceso.*
- Loop 1: info incompleta → devuelve al área solicitante.
- Loop 2: ningún candidato apto → republica la oferta y reevalúa.
- Loop 3: el candidato no acepta → el área selecciona otro.
- "Evaluación de los candidatos (subproceso no detallado)" → **subproceso
  colapsado**, con el +. No lo desarrolles.

Lanes: Área solicitante, Director de RRHH, Profesional de Selección. Pool
Candidato.

**6. Organizar Fiesta** — *el más largo.* Paralelo entre buscar lugar y buscar
música; adentro de cada rama, decisiones anidadas (cerrado/aire libre, vivo/CDs);
loop con **temporizador** (la banda no responde en una semana → se elige otra);
y una condición que salta de rama ("si no encuentran banda a tiempo, cambian a
CDs"). Al final, comida y bebida, con extra condicional si hubo banda.

**7. Agencia de viajes** — *el caso canónico del gateway inclusivo.* El cliente
puede tomar **ningún, uno, u otro, o los dos** seguros (cancelación y/o pérdida
de equipaje). Eso es inclusivo (O), no exclusivo ni paralelo — es el ejemplo con
el que se enseña el OR. Además: exclusivo de tres salidas (no interesado /
otras alternativas / elige una), loop en "otras alternativas", temporizador
(documentos dos semanas antes) y **evento adjunto** para la cancelación en
cualquier momento.

#### Dudas / pendientes
- `Patrones_de_Modelado_de_Procesos_Bizagi.pdf` y
  `PPT_Patrones_de_Modelado_de_Procesos_v1_03_2016.pdf`: sin ingerir.
- `Guia_de_Referencia_y_Modelado_BPMN.pdf` y `BPMN_Poster_Bizagi.pdf`: sin
  ingerir. El póster sirve como machete de notación.
- No hay resoluciones de los 7 casos en el material — los patrones de arriba son
  análisis propio del enunciado, no la solución oficial de la cátedra.

#### Fuentes
- `fuentes/BPMN/Ejercicios/PPT_Casos_Curso_BPMN_v1_02_Enunciados.pdf` ✅ ingerido
- `fuentes/BPMN/Apuntes/`, `fuentes/BPMN/Presentaciones/`,
  `fuentes/BPMN/Estandar_BPMN/` — pendientes
- Instaladores de Bizagi en `fuentes/BPMN/Bizagi/` (gitignorados, 389 MB):
  v2.6 (2014) y v3.6 (2020)

---

### Unidad 2 — Prototipado con Axure RP 9

#### Conceptos clave

La cátedra trabaja con **Axure RP 9** (v9.0.0.3727, feb 2021), con licencia UTN y
una VM preparada. Ojo: `entregables/prototipoRegistrarPrestamo.rp` está guardado
con **Axure RP 11** — RP 9 no abre archivos de RP 11.

Un prototipo sin interacciones es un dibujo. El TP se construye sobre cuatro
mecanismos, y todo el parcial sale de combinarlos:

1. **Variables globales** (`Project → Global Variables`) — la memoria entre
   páginas. Sin esto no se puede pasar un dato de una pantalla a otra.
2. **Eventos**: `Page Loaded` (al cargar la página), `Click or Tap`,
   `Text Changed`, `Lost Focus`, `Selection Changed` (droplist), `Selected`
   (radiobutton), `Item Loaded` (repeater).
3. **Acciones**: `Set Variable Value`, `Set Text`, `Set Image`, `Open Link`,
   `Add Sort` / `Remove Sort`, `Add Filter`.
4. **Expresiones** entre dobles corchetes: `[[Var_X]]`, `[[Item.Campo]]`,
   `[[This.text]]`.

#### Desarrollo — CU 001 Reservar habitación

Enunciado: `TP_Repeater_CU_Reservar_habitacion_v1_02.pdf`. Paso a paso resuelto:
`Axure_RP9_CU_Reservar_Habitacion_v1_02.pdf` (36 pág., Enrique Porta, v1.02,
24-05-2022). Ambos ingeridos.

**El CU.** Actor primario e iniciador: Cliente. Precondición: cliente logueado.
Postcondición de éxito: la reserva quedó registrada. Nivel usuario, alcance
sistema, caja negra, interacción dialogal.

- **Paso 1** — el cliente ingresa ciudad, fecha entrada, fecha salida y cantidad
  de personas. El sistema lista los hoteles disponibles con capacidad ≥ personas,
  mostrando foto, denominación, dirección, estrellas y precio por noche. Muestra
  la ciudad ingresada, el filtro Estrellas en "Todas las estrellas" y Ordenado
  por en "Más estrellas".
  - **1.a** ordenar por: Precio más bajo / más alto, Menos / Más estrellas.
  - **1.b** filtrar por cantidad de estrellas.
- **Paso 2** — el cliente selecciona un hotel. El sistema registra la estadía y
  muestra el comprobante (cliente, hotel, ciudad, fecha ingreso, fecha salida,
  costo estadía).

##### Las 4 páginas

`Inicio` → `DatosBusqueda` → `MostrarDatosHoteles` → `Comprobante`

##### Las 9 variables globales

`Var_Ciudad`, `Var_FechaEntrada`, `Var_FechaSalida`, `Var_CantPersonas`
(default **2**), `Var_DenominacionHotel`, `Var_PrecioHotel`, `Var_Cliente`
(default **Juan Perez**), `Var_CantidadDias`. Más `OnLoadVariable`, que ya viene.

Cargar los defaults es parte del TP: si `Var_Cliente` está vacía, el comprobante
sale sin nombre.

##### Página Inicio

Botón "Reservar Habitación" → `Click or Tap` → `Open Link` → `DatosBusqueda`.

##### Página DatosBusqueda

Cuatro `Text Field` nombrados **Ciudad, Entrada, Salida, CantPersonas**, más los
botones `-`, `+` y `Buscar`.

| Widget | Evento | Acción |
|---|---|---|
| (página) | `Page Loaded` | `Set Text` CantPers ← value of `Var_CantPersonas` |
| Ciudad | `Text Changed` | `Set Variable Value` `Var_Ciudad` ← text on Ciudad |
| Entrada | `Lost Focus` | `Set Variable Value` `Var_FechaEntrada` ← `"[[This.text]]"` |
| Salida | `Lost Focus` | `Set Variable Value` `Var_FechaSalida` ← `"[[This.text]]"` |

**Entrada y Salida se definen como `Input Type → Date`** (panel Interactions).
Eso hace que el navegador muestre el almanaque. Al asignar `"[[This.text]]"` la
fecha se guarda en formato **YYYY-MM-DD**, que es lo que después necesita
`Date.parse()`.

**Botón `-`** — `Click or Tap`, con condición:
- Si `value of Var_CantPersonas is greater than "1"`:
  - `Set Variable Value` `Var_CantPersonas` ← `"[[Var_CantPersonas - 1]]"`
  - `Set Text` CantPers ← value of `Var_CantPersonas`

**Botón `+`** — igual pero `is less than "5"` y `"[[Var_CantPersonas + 1]]"`.

**Botón Buscar** — `Click or Tap` → `Add Case` → Condition Builder, **Match All**
con cuatro filas:

    [[Var_Ciudad]]        does not equal        (vacío)
    [[Var_FechaEntrada]]  does not equal        (vacío)
    [[Var_FechaSalida]]   does not equal        (vacío)
    [[Var_CantPersonas]]  is greater than or equals   1

Si se cumple → `Open Link` → `MostrarDatosHoteles`. Esa condición **es** la
validación del CU: sin ella el TP está incompleto.

##### Página MostrarDatosHoteles — el Repeater

Arrastrar el widget **Repeater** desde Libraries. Nombrarlo **Hoteles** en el
panel Style, y tildar **Fit to Content in HTML**.

Columnas del DATA: `Ciudad, Denominacion, Direccion, Foto, Estrellas, Precio`.
La primera se renombra desde `Column0`; el resto con `Add Column`.

**Dataset de la cátedra** (`entregables/hoteles-repeater.csv`):

| Ciudad | Denominacion | Direccion | Estrellas | Precio |
|---|---|---|---|---|
| Rosario | Holiday Inn Express Rosario | Salta 1950 | 3 | 9000 |
| Rosario | Apart Hotel Alvear | Alvear 555 | 2 | 7000 |
| Rosario | Amérian Puerto Rosario Hotel | Mitre 1319 | 4 | 10000 |
| Córdoba | Holiday Inn Córdoba | Fray Luis Beltran Y Cardenosa | 3 | 8000 |

La columna **Foto** es de tipo imagen: botón derecho sobre la celda →
**Import Image** → elegir el `.jpg`. **No se puede cargar por CSV** — el CSV solo
sirve para las columnas de texto y número.

**Item Loaded del repeater.** Doble click en el repeater abre la ventana de
diseño del ítem. Ahí se arma la maqueta de una fila y se nombra cada widget en
Interactions. Después, en `Item Loaded`:

    Set Text
      Ciudad       to "[[Item.Ciudad]]"
      Denominacion to "[[Item.Denominacion]]"
      Direccion    to "[[Item.Direccion]]"
      Estrellas    to "[[Item.Estrellas]]"
      Precio       to "[[Item.Precio]]"
    Set Image
      Foto         to [[Item.Foto]]

Ojo: el repeater arranca mostrando **solo el primer atributo**. Si ves solo la
ciudad, es porque falta agregar los `Add Target` al `Set Text`.

La ciudad se termina **ocultando** (panel Style → ícono del ojo) junto con su
etiqueta "Alojado en:", porque ya se muestra arriba, fuera del repeater. Se
oculta, no se borra: el dato sigue haciendo falta para filtrar.

**Botón Reservar** (dentro del ítem del repeater) — `Click or Tap`:

    Set Variable Value
      Var_DenominacionHotel to "[[Item.Denominacion]]"
      Var_PrecioHotel       to "[[Item.Precio]]"
    Open Link
      Comprobante

Está **adentro** del repeater, por eso puede leer `[[Item.…]]` y sabe qué hotel
se eligió. Es el punto donde el paso 2 del CU se vuelve prototipo.

##### Ordenar — Droplist "OrdenadoPor"

Botón derecho sobre el droplist → **Edit List Items**: Más estrellas (tildado
por defecto), Menos estrellas, Precio más alto, Precio más bajo.

Evento `Selection Changed` → **Enable Cases**, cuatro casos encadenados con
`Else If`. Cada uno con la misma estructura:

    Case "Más estrellas"
      If selected option of This equals Más estrellas
        Remove Sort → Hoteles, Sort: All
        Add Sort    → Hoteles | Name: Más estrellas | Column: Estrellas
                      Sort as: Number | Order: Descending

Los otros tres cambian solo columna y orden: Menos estrellas (Estrellas, Number,
Ascending), Precio más alto (Precio, Number, Descending), Precio más bajo
(Precio, Number, Ascending).

**El `Remove Sort → All` antes de cada `Add Sort` no es opcional.** Sin él los
órdenes se acumulan y el resultado deja de tener sentido. Es el error clásico.

`Sort as: Number` es lo que obliga a cargar Precio y Estrellas sin `$` ni
separador de miles: como texto, 9000 ordena antes que 10000.

##### Filtrar — Page Loaded y los RadioButtons

**`Page Loaded` de MostrarDatosHoteles**, en este orden:

    Add Sort    → Hoteles add Estrellas as Number desc
    Add Filter  → Name: Ciudad
                  Rule: [[Item.Ciudad ==Var_Ciudad]]
                  ☑ Remove other filters
    Set Text    → CiudadIngresada to "[[Var_Ciudad]]"

Cuatro **RadioButton** fuera del repeater, todos con
`Assign Radio Group: GrupoFiltroEstrellas` (se seleccionan los 4 juntos y se
asigna el grupo de una). "Todas las estrellas" con la propiedad **Selected**
tildada, para que sea el default.

Cada uno lleva el evento **`Selected`** (no `Click`):

- **Todas las estrellas**: un solo `Add Filter` — el de Ciudad, con
  ☑ *Remove other filters*. No lleva filtro por estrellas, justamente porque las
  muestra todas.
- **4 / 3 / 2 estrellas**: **dos** `Add Filter` en este orden:
  1. Ciudad → `[[Item.Ciudad ==Var_Ciudad]]` con ☑ *Remove other filters*
  2. `N estrellas` → `[[Item.Estrellas =="4"]]` con ☐ *Remove other filters*
     **destildado**

**Ese tilde es la trampa del TP.** El primer filtro limpia lo anterior; el
segundo se suma. Si dejás tildado el segundo, borra el filtro de ciudad y te
aparecen hoteles de todas las ciudades. Si destildás el primero, se acumulan los
filtros de estrellas entre clicks y no queda nada.

##### Página Comprobante

Seis `Text Field`: `Cbte_Cliente`, `Cbte_Hotel`, `Cbte_Ciudad`, `Cbte_Entrada`,
`Cbte_Salida`, `Cbte_Costo`.

`Page Loaded`, **en este orden**:

    Set Text  Cbte_Ciudad  to value of Var_Ciudad
    Set Text  Cbte_Cliente to value of Var_Cliente
    Set Text  Cbte_Hotel   to value of Var_DenominacionHotel
    Set Text  Cbte_Entrada to value of Var_FechaEntrada
    Set Text  Cbte_Salida  to value of Var_FechaSalida
    Set Variable Value  Var_CantidadDias to
      [[Math.floor( (Date.parse(Var_FechaSalida).valueOf() -
        Date.parse(Var_FechaEntrada).valueOf()) / 1000 / 60 / 60 / 24 )]]
    Set Text  Cbte_Costo   to [[Var_CantidadDias * Var_PrecioHotel]]

**El `Set Text` de Cbte_Costo tiene que ir después del `Set Variable Value` de
Var_CantidadDias.** Lo aclara el propio apunte. Si lo ponés antes, el costo sale
en 0 o vacío, porque la variable todavía no se calculó.

**La fórmula de días**, desarmada: `Date.parse()` devuelve milisegundos desde
1970. La resta da los milisegundos entre ambas fechas, y las divisiones sucesivas
los llevan a días: `/1000` → segundos, `/60` → minutos, `/60` → horas, `/24` →
días. `Math.floor()` trunca. Para calcular una **edad** es la misma expresión con
un `/365` más al final.

Verificación: con el `Console` del Preview (ícono de Axure arriba a la derecha)
se ven todas las variables globales con su valor actual. Es la forma de depurar
cuando el comprobante sale vacío.

#### Machete de expresiones

| Expresión | Qué hace |
|---|---|
| `[[Var_X]]` | valor de una variable global |
| `[[Item.Campo]]` | valor de una columna del repeater, en la fila actual |
| `[[This.text]]` | texto del widget que disparó el evento |
| `[[Var_CantPersonas + 1]]` | aritmética dentro de la expresión |
| `[[Item.Ciudad ==Var_Ciudad]]` | regla de filtro del repeater |
| `[[Item.Estrellas =="4"]]` | filtro por valor literal (entre comillas) |
| `Math.floor(x)` | trunca hacia abajo |
| `Date.parse("2018-11-14")` | fecha → milisegundos desde 1970 |
| `Now.getFullYear()` | año actual |
| `"Hello, world!".slice(3, 10)` | → `lo, wor` |

#### Dudas / pendientes
- `Caso_Registrar_Prestamo/` (docx + 2 PDFs): sin ingerir. El paso a paso del
  repeater lo da por sabido ("se supone que ya se hizo el TP CU Registrar
  Préstamo"), así que ahí están las funcionalidades básicas que este apunte no
  vuelve a explicar.
- `Consejos/`: búsqueda predictiva y cálculos con fechas, con sus `.rp`. Sin
  ingerir.
- `Enlaces_en_Axure_RP_9_y_Axure_RP_10.pdf`: sin ingerir.
- Páginas 13-16 del paso a paso (armado fino de la maqueta del ítem): sin leer.
  Es disposición visual, no lógica.

#### Fuentes
- `fuentes/Axure_RP9/Caso_Reservar_Habitacion/TP_Repeater_CU_Reservar_habitacion_v1_02.pdf` ✅
- `fuentes/Axure_RP9/Caso_Reservar_Habitacion/Axure_RP9_CU_Reservar_Habitacion_v1_02.pdf` ✅ (leído con visión)
- `entregables/hoteles-repeater.csv` — dataset real de la cátedra
- `entregables/prototipoRegistrarPrestamo.rp` (Axure RP 11)

## Log
- Archivo creado.
- 2026-09-06: ingesta inicial. Descomprimidos `Axure_RP9.zip` y `BPMN.zip` en
  `fuentes/`. Creadas Unidad 1 (BPMN/Bizagi) y Unidad 2 (Axure RP 9). Ingeridos
  los enunciados de los 7 casos BPMN y el TP del repeater del CU Reservar
  habitación. Corregido `hoteles-repeater.csv` al dataset real de la cátedra.
  Instaladores `.exe` de Bizagi gitignorados (389 MB).
- 2026-09-06: unidad 2 completa. Leído con visión el paso a paso de 36 páginas
  del CU Reservar habitación (las 4 páginas, las 9 variables globales, Item
  Loaded, botón Reservar, ordenar con Add/Remove Sort, filtrar con el tilde de
  Remove other filters, y el cálculo de días del comprobante). Corregido
  `hoteles-repeater.csv` con el dataset real de la cátedra.
- 2026-09-06: ingeridos los parciales 2022 y 2026 (`fuentes/Parciales/`). Generado
  `estudio/repaso-parcial.md` a partir de ellos: 15 preguntas de teoría BPMN con
  respuesta verificada (el PDF de 2022 es el formulario corregido 10/10), 6
  contradicciones aparentes entre años analizadas, auditoría adversarial de la
  resolución práctica de 2026 (16 hallazgos → 2 confirmados, 14 refutados por
  verificación a tres lentes) y plan de ataque para el CU "Pedir un libro".
