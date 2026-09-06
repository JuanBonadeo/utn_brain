# IPP — Parcial: material de repaso

> Documento de repaso final. Todo lo que ya está explicado en `materias/IPP/IPP.md` (los 3 gateways, los 7 casos BPMN, el paso a paso del CU Reservar habitación, el machete de expresiones de Axure) **no se repite acá**: esto es el delta para el parcial.
>
> Convención de origen, respetada en todo el documento:
> - **[CÁTEDRA]** = sale de material de la cátedra (parciales 2022 y 2026, enunciados, apuntes de Porta).
> - **[NUESTRO]** = análisis propio, no está verificado por la cátedra.

---

## 1. Cómo viene el parcial

**[CÁTEDRA]** Dos partes independientes.

| Parte | Qué es | Entregable |
|---|---|---|
| A.1 — Teoría BPMN | 10 preguntas multiple choice, **de respuesta múltiple** | Cuestionario del aula virtual |
| A.2 — Práctica BPMN | Modelar un caso en Bizagi Modeler, con subproceso | `Apellido_pp.jpg` + `Apellido_sub.jpg` + el archivo `.bpm` |
| B — Axure | Prototipar un CU en Axure RP 9 | `Apellido_Nombre.rp` |

Puntos duros del formato:

- **No hay número fijo de correctas por pregunta.** Hay preguntas con 3 o 4 tildadas (Eventos, Eventos de fin, Tipos de compuertas basada en datos, Flujo de secuencia) y otras con una sola (Compuertas inclusivas, Compuerta basada en eventos, Eventos intermedios). No busques simetría.
- **Desde 2026 se entrega también el `.bpm`**, no alcanza con los jpg. Y son **dos imágenes**, principal y subproceso por separado.
- **El apellido va escrito como objeto de texto DENTRO de cada diagrama.** Viaja incrustado en el jpg: si exportás antes de escribirlo, lo perdiste.
- Canal: Bizagi por **Google Classroom** (2026). Axure en 2022 iba por **mail con asunto exacto "Parcial Axure"**. **[NUESTRO]** Como es virtual, confirmá el canal de Axure en el enunciado del día; si dice mail, copiá el asunto textual.

**[NUESTRO]** Reparto de tiempo sugerido: la teoría se contesta rápido si venís con los distractores identificados (sección 3), el modelado es donde se define la nota de la parte A, y Axure conviene atacarlo con el cronograma de la sección 5 sin improvisar el orden.

---

## 2. Teoría BPMN — banco de preguntas

**[CÁTEDRA]** Reconstruido de los parciales 2022 y 2026. `[x]` = correcta, `[ ]` = incorrecta. La columna "año" indica en qué parcial apareció esa opción.

### 2.1 Eventos

**Respecto de Eventos de fin** *(2022)*

- [ ] Indica dónde comienza el flujo de secuencia del proceso
- [x] Indica dónde finaliza un flujo de secuencia del proceso
- [x] No debe tener ningún flujo de secuencia de salida
- [x] Un proceso puede tener varios eventos de fin

> Por qué: el fin cierra **un** camino y **consume** el token, por eso no tiene salidas. Varios fines es lo normal, uno por desenlace.

**Respecto de Eventos intermedios** *(2026)*

- [ ] Indican dónde comienza un flujo de secuencia del proceso
- [ ] Indican dónde finaliza un flujo de secuencia del proceso
- [x] Ocurre entre un evento de inicio y uno de fin

> ⚠️ **AVISO — trampa de reuso.** "Indican dónde finaliza un flujo de secuencia" es **verdadera en 2022** (bajo *Eventos de fin*) y **falsa en 2026** (bajo *Eventos intermedios*). No es contradicción de contenido: cambió el sujeto de la pregunta. Si memorizás la opción y no el concepto, caés.

**Respecto de eventos intermedios** *(2022)*

- [x] Indican cómo un proceso puede ser interrumpido o demorado
- [x] Puede estar adjunto a una tarea o a un subproceso

> Por qué: temporizador que demora / evento que interrumpe; y el evento **adjunto al borde** (boundary), el del "puede ser cancelado en cualquier momento".

**Respecto de Eventos (generalidades)** *(2026)* — las cuatro van tildadas

- [x] Un Evento es algo que sucede durante la ejecución de un proceso de negocio, el cual afecta la ejecución del flujo
- [x] Pueden definirse varios eventos de inicio para un proceso
- [x] Pueden definirse varios eventos intermedios para un proceso
- [x] Pueden definirse varios eventos de fin para un proceso

> Por qué: definición textual del estándar + no hay límite de cantidad en ninguno de los tres tipos.

### 2.2 Compuertas

**Respecto de Compuertas Exclusivas basada en datos** *(2022)*

- [ ] Todas las combinaciones de caminos pueden ocurrir, desde cero a todos
- [x] Sólo uno de los caminos será seleccionado
- [ ] La selección de los caminos alternativos está basada en la ocurrencia de eventos
- [ ] Requiere que todos los caminos hayan producido un token

> Por qué: la 1ª es la **inclusiva**, la 3ª es la **basada en eventos**, la 4ª es la sincronización de la **paralela** al cerrar.

**Respecto de Compuertas Inclusivas** *(2026)*

- [ ] La selección de los caminos alternativos está basada en la ocurrencia de eventos
- [ ] Todos los caminos deben completarse antes de que el proceso continúe
- [x] Todas las combinaciones de caminos pueden ocurrir

> ⚠️ **AVISO — la trampa número uno del parcial.** La frase *"todas las combinaciones de caminos pueden ocurrir, desde cero a todos"* es **FALSA en 2022** (colgada de la exclusiva) y **VERDADERA en 2026** (colgada de la inclusiva). Misma frase, valor invertido, porque cambió el sujeto. Leé el encabezado antes que las opciones, siempre.
>
> ⚠️ **AVISO — precisión contra la wiki.** La wiki dice inclusiva = "uno o más". La formulación de la cátedra en el parcial es más amplia: **"desde cero a todos"**. Si en el multiple choice aparece "desde cero", va tildada igual.

**Con respecto a los tipos de Compuertas** *(2022)*

- [x] Las compuertas representan la división y unión de flujos
- [ ] En compuertas inclusivas sólo uno de los caminos será seleccionado
- [ ] En compuertas paralelas basada en datos solo uno de los caminos será seleccionado

> Por qué: la 2ª describe la exclusiva. La 3ª es doblemente falsa: la paralela activa **todas** las ramas y ni siquiera evalúa datos.

**Respecto de Compuerta Basada en Eventos** *(2026)*

- [x] Un punto en el proceso donde la selección de los caminos alternativos está basada en la ocurrencia de eventos
- [ ] Pueden ser usados para dividir y unir flujos

> ⚠️ **AVISO — la única que exige criterio y no memoria.** "División y unión de flujos" es **verdadera** en 2022 como afirmación **genérica sobre compuertas**, y **falsa** en 2026 aplicada a la **basada en eventos**, porque esa **solo divide**: para converger hay que usar otra compuerta. Lo genérico vale para el conjunto, no para el caso particular.

**Son Tipos de Compuertas basada en datos** *(2022)*

- [x] Inclusiva
- [x] Exclusiva
- [x] Paralela
- [ ] Recursiva

**Son Tipos de Compuertas Basadas en Eventos** *(2026)*

- [x] Exclusiva
- [x] Paralela
- [ ] Compleja

> Por qué: existen las dos variantes event-based. La **exclusiva** es la clásica (gana el primer evento que ocurre); la **paralela** basada en eventos espera que ocurran **todos**. La **Compleja** existe en BPMN pero es basada en **datos**: ocupa el lugar de distractor que en 2022 tenía "Recursiva".

**[NUESTRO]** Machete de las cuatro semánticas, que es lo que resuelve 3 o 4 de las 10 preguntas:

| Compuerta | Cuántas ramas | Clasificación |
|---|---|---|
| Exclusiva (X) | **una sola**: la primera condición que se cumple | datos (y también existe event-based) |
| Inclusiva (O) | **de cero a todas**, según condiciones por rama | datos |
| Paralela (+) | **todas**, y al cerrar sincroniza (espera todos los tokens) | datos (y también existe event-based) |
| Basada en eventos | gana **el primer evento** que ocurre; **solo divide** | eventos |

### 2.3 Flujos

**Respecto de un Flujo de Secuencia** *(opciones de 2022 y 2026 juntas)*

- [x] Es usado para representar el orden de ejecución de las actividades en un proceso — *(ambos años)*
- [x] **No** puede cruzar los límites de un Contenedor (Pool) — *(2026)*
- [ ] Puede cruzar los límites de un Contenedor (Pool) — *(2022)*
- [x] El origen y el destino de un flujo de secuencia debe ser uno de los objetos de flujo: eventos, actividades y compuertas — *(2026)*
- [ ] Es usado para representar el flujo de mensajes entre dos participantes que están preparados para enviar y recibir mensajes — *(2026)*

> ⚠️ **AVISO — misma regla, enunciada al derecho y al revés.** 2022 la puso en positivo (falsa), 2026 negada (verdadera). No son contradictorias: **leé si la opción está negada antes de tildar.** Es la regla que la wiki marca como "nunca se perdona".
>
> Por qué la última es falsa: eso es el **flujo de mensaje** (línea punteada, flecha hueca).

### 2.4 Token

**Respecto de un Token**

- [x] Un Token es usado para representar la ejecución de una instancia de un proceso — *(ambos años)*
- [x] El comportamiento de un proceso puede ser descrito siguiendo el camino del Token, ya que atraviesa el flujo de secuencia, actividades, eventos y compuertas del proceso — *(2026)*
- [ ] Un evento de fin genera un Token — *(ambos años)*

> Por qué: el **inicio genera** el token, el **fin lo consume**. Distractor idéntico en los dos parciales.

### 2.5 Tipos de tareas

**Respecto de Tipos de Tareas** *(opciones de ambos años)*

- [x] Tipo **Servicio**: representa un servicio automatizado provisto por una aplicación — *(ambos)*
- [x] Tipo **Manual**: una tarea que es ejecutada **sin** la asistencia de una aplicación — *(2026)*
- [ ] Tipo **Manual**: una tarea donde una persona ejecuta la tarea **con** la asistencia de una aplicación de software — *(2022)*
- [x] Tipo **Usuario**: una tarea donde una persona ejecuta la tarea con la asistencia de una aplicación de software — *(2026)*
- [ ] Tipo **Recepción**: representa el **envío** de un mensaje a un participante externo — *(2022)*
- [ ] Tipo **Script**: una tarea que es ejecutada sin la asistencia de una aplicación — *(2022)*

> ⚠️ **AVISO — no es contradicción, es intercambio de definiciones.** El texto "una persona ejecuta con asistencia de software" es correcto para **Usuario** y falso para **Manual**. La cátedra evalúa siempre por este mecanismo: te da la definición correcta pegada al tipo equivocado. Los pares que intercambia son **Manual ↔ Usuario** y **Script ↔ Manual**.
>
> Regla mínima: **Manual** = persona sin sistema. **Usuario** = persona con sistema. **Servicio** = sistema solo. **Script** = el motor corre un script (lo más automatizado de todos, jamás "sin aplicación"). **Envío** manda, **Recepción** recibe.

### 2.6 Marcadores de actividad

**Respecto de Marcadores de Actividad**

- [x] **Ad-Hoc**: las actividades no son ejecutadas en un orden particular — *(ambos)*
- [x] **Loop**: la ejecución repetida de una tarea en forma secuencial — *(ambos)*
- [x] **Instancias Múltiples**: la ejecución de múltiples instancias de la tarea — *(2026)*
- [ ] **Compensación**: representa la ejecución de una instancia de una tarea — *(2022)*
- [ ] **Escalamiento**: representa la ejecución del nivel siguiente — *(2022)*

> Por qué: Compensación **deshace** el efecto de una actividad ya completada. Escalamiento **no es un marcador de actividad**: es un tipo de **evento**.

### 2.7 Subprocesos

**Respecto de Subproceso Embebido**

- [x] Usado para definir un alcance dentro de un proceso: visibilidad, manejo de transacciones, excepciones, eventos o compensaciones — *(ambos)*
- [x] Puede ser visualizado en forma colapsada o expandida — *(2026)*
- [ ] Es un subproceso definido dentro de un proceso pero puede ser reusado en el contexto de actividades de otro proceso — *(ambos)*

> Por qué: lo reusable es el **subproceso reutilizable** (call activity). El **embebido** vive dentro de su padre y no se reusa. Distractor textual repetido en los dos años.

---

## 3. Los distractores que se repiten

**[CÁTEDRA]** Afirmaciones **falsas** que la cátedra recicla. Si las reconocés de una, descartás sin pensar y ganás tiempo.

| Distractor | Por qué es falso | Dónde aparece |
|---|---|---|
| "Un evento de fin genera un Token" | lo genera el **inicio**; el fin lo consume | 2022 y 2026, textual |
| "El [subproceso embebido] puede ser reusado en el contexto de actividades de otro proceso" | eso es el **reutilizable** | 2022 y 2026, textual |
| "**Recursiva**" como tipo de compuerta | no existe en BPMN | 2022 |
| "**Compleja**" como compuerta basada en eventos | existe, pero es basada en **datos** | 2026 |
| "La selección está basada en la ocurrencia de eventos", pegada a la exclusiva o a la inclusiva | esa es la definición de la **basada en eventos** | 2022 y 2026 |
| "Sólo uno de los caminos será seleccionado", pegada a inclusiva o a paralela | esa es la **exclusiva** | 2022 |
| "Requiere que todos los caminos hayan producido un token", pegada a la exclusiva | esa es la **paralela** al cerrar | 2022 |
| "El flujo de secuencia puede cruzar los límites de un Pool" | entre pools va **flujo de mensaje** | 2022 |
| "Tipo Manual: con la asistencia de una aplicación de software" | esa es la tarea de **Usuario** | 2022 |
| "Tipo Script: sin la asistencia de una aplicación" | esa es **Manual**; Script es lo más automatizado | 2022 |
| "Tipo Recepción representa el envío de un mensaje" | invierte el sentido: la que envía es **Envío** | 2022 |
| "Compensación representa la ejecución de una instancia de una tarea" | Compensación **deshace**, no ejecuta | 2022 |
| "Escalamiento" como marcador de actividad | es un tipo de **evento** | 2022 |

**[NUESTRO]** Los tres mecanismos con que arma cada distractor, para que los detectes aunque cambie el texto:
1. **Cambio de sujeto**: definición correcta pegada al elemento equivocado (el más usado).
2. **Inversión de sentido**: "Recepción envía", "el fin genera el token".
3. **Elemento inventado o mal clasificado**: "Recursiva", "Compleja" como event-based, "Escalamiento" como marcador.

---

## 4. Práctica BPMN — el caso de junio 2026, corregido

### 4.1 El enunciado, resumido

**[CÁTEDRA]** *Proceso de solicitud de capacitación externa.*

1. Cualquier empleado puede solicitar una capacitación externa a través de una aplicación interna. Cuando envía la solicitud, el jefe de área la evalúa.
2. Si el jefe **rechaza**, el proceso concluye con una notificación enviada al empleado.
3. Si **aprueba**, se inicia un **subproceso** destinado a gestionar la inscripción: el empleado selecciona entre las opciones de capacitación disponibles y el área de **Compras** revisa; si Compras solicita modificaciones, el empleado ajusta y reenvía (**loop**).
4. Finanzas evalúa el pago. Si lo **rechaza**, se informa al empleado.
5. Si lo aprueba, se espera la **confirmación del pago dentro de un plazo determinado**. Si no se confirma en ese tiempo, la inscripción se cancela y se notifica al empleado.
6. Antes del inicio de la capacitación, esta **puede ser cancelada por circunstancias externas**; si eso pasa, el empleado recibe una notificación. Si no, llega la fecha y asiste.

Consigna de entrega: poner el apellido como texto en los diagramas y exportar `Apellido_pp.jpg` y `Apellido_sub.jpg`, más el archivo de Bizagi.

**[NUESTRO]** Los patrones que pide son exactamente los de los 7 casos del curso ya documentados en la wiki: subproceso colapsado (caso 5), gateway exclusivo con loop de correcciones (casos 1 y 3C), temporizador de plazo (caso 6), evento adjunto de cancelación (caso 7) y compuerta basada en eventos (caso 4).

### 4.2 La resolución del compañero

> ⚠️ **Importante:** la resolución que circula (`ProcesoPrincipal.jpg` / `SubProceso.jpg`) es de un compañero. **No está verificada ni corregida por la cátedra.** Todo lo que sigue —aciertos y errores— es **[NUESTRO]** análisis.

**Estructura del principal:** un pool "Proceso de Solicitud de Capacitación Externa" con tres lanes (Empleado / Jefe de Área / Finanzas). 8 tareas + 1 subproceso colapsado, 1 inicio, 6 fines, 2 compuertas exclusivas, 1 basada en eventos, 1 evento adjunto temporizador, 2 eventos intermedios de captura (timer y mensaje).

**Estructura del subproceso:** pool "Gestión Inscripción" con lanes Empleado / Compras. 2 tareas, 1 inicio, 1 fin, 1 exclusiva con loop de vuelta a "Seleccionar opción de capacitación".

#### Qué hizo bien (copiá esto)

1. **La compuerta basada en eventos** para "antes del inicio, la capacitación puede ser cancelada": es una carrera real entre un intermedio **temporizador** ("llega la fecha de inicio") y un intermedio de **mensaje** ("recibe mensaje de cancelación"). Es justo para lo que existe ese gateway. Y lo hizo bien en los tres detalles que se controlan: símbolo correcto, las dos salidas apuntan a **eventos de captura** (una event-based solo puede apuntar a eventos de captura o receive tasks), y las salidas **no** están etiquetadas — que es lo correcto para este tipo.
2. **El evento adjunto al borde (boundary) temporizador** sobre "Esperar confirmación de pago", **interruptor** (doble círculo de línea llena), con el flujo de salida etiquetado "Se vence el plazo". Está pegado al borde, no metido en el flujo. Resuelve bien el punto 5 del enunciado.
3. **Un solo pool con lanes** para todo lo interno. El empleado es interno → va como **lane**, no como pool aparte. Bien decidido.
4. **Cero flujos de secuencia cruzando un pool.** Todos los saltos son entre **lanes** del mismo pool, que es legal. Es el error que más descuenta y no está.
5. **Ninguna rama colgada**: los seis caminos del principal y los dos del subproceso cierran en un evento de fin. El loop también cierra bien.
6. **Subproceso colapsado** (rectángulo con "+") para "Gestión Inscripción", que es lo que pide el enunciado y lo que habilita entregar las dos imágenes.
7. **Compras dentro del subproceso**, revisando opciones, con el **loop** de "solicitar modificaciones → el empleado ajusta y reenvía" resuelto con una exclusiva que vuelve a "Seleccionar opción".
8. **Las compuertas no hacen trabajo**: la tarea que consigue el dato ("Evaluar la pertinencia…", "Evaluar pago", "Revisar opciones…") va **siempre antes** del rombo, y el rombo está nombrado como pregunta. Exactamente lo que la cátedra controla.
9. **Nombres de tarea del núcleo bien construidos**: infinitivo + sustantivo ("Evaluar la pertinencia de la capacitación solicitada", "Evaluar pago", "Seleccionar opción de capacitación", "Asistir a la capacitación").

#### Los dos errores confirmados

**[NUESTRO]** Son los únicos hallazgos que sobrevivieron a la verificación adversarial. El resto de las objeciones se descartaron (ver 4.3).

| # | Dónde | Problema | Corrección |
|---|---|---|---|
| 1 | Compuerta exclusiva **"Está aprobado?"** (lane Finanzas) — **sintaxis** | Las **dos salidas están sin etiquetar**. Ni la que sube a "Pago rechazado" ni la que va a la espera de confirmación tienen texto. En una exclusiva **cada salida lleva su condición**: es ítem de corrección directo. | Etiquetar "no" / "Pago rechazado" y "si" / "Pago aprobado". Y poner los signos: **"¿Está aprobado el pago?"**. |
| 2 | Tres tareas del lane Empleado: "Recibe notificación: solicitud cancelada", "Recibe notificado: Pago rechazado", "Recibe notificación de cancelación" — **estilo** | Verbo **conjugado** en 3ª persona, contra la regla tarea = **infinitivo + sustantivo**. Además "Recibe notificado" es agramatical (mezcla "recibe notificación" con "es notificado"). | Pasar todo a infinitivo: **"Recibir notificación de rechazo"**, etc. |

**[NUESTRO]** Lo que te llevás para tu propio diagrama de mañana: **etiquetá TODAS las salidas de toda compuerta exclusiva e inclusiva** (la paralela no se etiqueta, la basada en eventos tampoco) y **escribí todos los nombres de tarea en infinitivo**, incluidas las de notificación. Son los dos únicos errores reales en un diagrama por lo demás sólido: es barato no cometerlos.

### 4.3 Lo que NO es error (no pierdas tiempo "arreglándolo")

**[NUESTRO]** Estas objeciones se plantearon y se refutaron. Las listo para que no te ganen la cabeza si mañana ves algo parecido en tu propio modelo:

- El proceso arranca con un inicio simple en el lane del Jefe ("Recibe solicitud de empleado") y no modela el acto del empleado de enviar la solicitud: **aceptable**.
- Modelar las notificaciones como tareas de **recepción** en el lane Empleado en vez de tareas de **emisión** en el lane que decide: **aceptable**.
- El evento intermedio de mensaje sin pool externo emisor, y la ausencia de un pool para el proveedor externo de capacitación: **aceptable** en este caso.
- "Solicitud cancelada" en vez de "rechazada"; "Cancelar inscripción y notificar empleado" con dos verbos y ubicada en Finanzas; "Esperar confirmación de pago" como tarea sin tipo.
- El retorno del loop entrando directo a la tarea sin compuerta de convergencia (merge implícito).
- Que el subproceso tenga pool y lanes propios, incluido el lane "Compras" que no existe en el pool padre.
- Faltas de tildes y de signos "¿" en general, y eventos de fin sin nombre.
- El recorte del subproceso (dejar Finanzas afuera).

⚠️ La única excepción: el **cuadro de anotación vacío** arriba a la izquierda en ambos diagramas. Ahí va **tu apellido**, y es requisito explícito del enunciado. En el archivo del compañero está vacío. **No lo dejes vacío vos.**

---

## 5. Axure — plan de ataque

**[CÁTEDRA]** CU **"Pedir un libro"** (Enrique Porta, v1.02, 17-05-2019). Nivel usuario, alcance sistema, caja negra, instanciación real, interacción dialogal, usabilidad no contemplada. Actor primario e iniciador: **Cliente**. Precondición: **el cliente está logueado**. Postcondición de éxito: **el pedido quedó registrado Y la existencia del libro fue actualizada**.

- **Paso 1** — el cliente selecciona la **categoría** y presiona "Buscar libro". El sistema muestra en **cabecera** nombre y apellido del cliente y la categoría seleccionada, y lista los libros (**título, existencia y precio**) ordenados por "Título de A a Z", que sean de esa categoría y tengan **existencia ≥ 1**.
  - **1.a** — ordenar por: Título A-Z, Título Z-A, Precio más bajo, Precio más alto.
- **Paso 2** — el cliente elige un libro y presiona "Comprar". El sistema **registra el pedido**, **actualiza la existencia** y muestra: **número de pedido, fecha del pedido (now), nombre y apellido del cliente, título del libro**.
  - **2.a** — el cliente presiona "Cancelar" → termina el CU.
- Nota del enunciado (**se descuenta si no se cumple**): guardar como `Apellido_Nombre.rp` y enviarlo por mail con asunto **"Parcial Axure"** a la cuenta que indique el docente.

### 5.1 Es el CU del hotel con menos piezas

**[NUESTRO]** Mismo esqueleto que Reservar habitación, y todo lo que está en la wiki se reutiliza tal cual:

| | Hotel (wiki) | Libros (parcial) |
|---|---|---|
| Páginas | 4 | **3** (Inicio · MostrarLibros · Comprobante) |
| Variables globales | 8 + OnLoadVariable | **4** |
| Columnas del repeater | 6 (con Foto) | **4**: Categoria, Titulo, Existencia, Precio |
| Add Filter | 2 encadenados, con la trampa del tilde | **1 solo**, regla compuesta |
| Cálculo de fechas | Date.parse + Math.floor | **ninguno** (solo `Now`) |
| RadioButtons + Assign Radio Group | sí | **no van** |

Se reutiliza **sin cambios**: la arquitectura de páginas con `Open Link`; variables globales con defaults cargados en `Project → Global Variables`; el repeater completo (nombrarlo en Style, `Fit to Content in HTML`, renombrar `Column0`, `Add Column`, cargar el DATA a mano); `Item Loaded` con **un** `Set Text` y varios `Add Target`; el botón de acción **dentro** del ítem leyendo `[[Item.Campo]]`; el droplist de orden con `Selection Changed` + `Enable Cases` + 4 casos con `Else If` + `Remove Sort (All)` antes de cada `Add Sort`; el `Page Loaded` del listado como lugar de cabecera + filtro + orden por defecto; el `Page Loaded` del comprobante como cadena de `Set Text`; números sin `$` ni puntos; y la **Console del Preview** para depurar variables.

**Lo genuinamente nuevo es uno solo: `Update Rows`.**

### 5.2 Las 4 variables globales

| Variable | Default | Para qué |
|---|---|---|
| `Var_Cliente` | **Juan Perez** | la precondición "cliente logueado" se modela con el **default**, no con un login |
| `Var_Categoria` | (vacía) | la setea el botón Buscar libro |
| `Var_TituloLibro` | (vacía) | la setea el botón Comprar |
| `Var_NroPedido` | **1000** (numérico) | se incrementa en el Comprar |

### 5.3 Lo nuevo respecto del hotel

**[NUESTRO]** salvo donde se indique.

- **Cabecera.** En el hotel el cliente solo salía en el comprobante; acá va **también arriba del listado**. En `Page Loaded` de MostrarLibros: `Set Text` sobre dos labels, uno a value of `Var_Cliente` y otro a value of `Var_Categoria`. Es el mismo mecanismo que "CiudadIngresada".
- **La categoría sale de un Droplist**, no de Text Fields. Lo más rápido: **ninguna interacción en el droplist**; todo en el botón "Buscar libro" → `Click or Tap` → `Set Variable Value Var_Categoria to [[Categoria.selectedOption]]` → `Open Link` MostrarLibros. Plan B si sale vacío: `[[Categoria.text]]`. Plan C blindado: `Selection Changed` con un caso por categoría seteando un literal.
- **Un solo `Add Filter` con regla compuesta.** Name `CategoriaYStock`, Rule `[[Item.Categoria == Var_Categoria && Item.Existencia >= 1]]`, tilde **Remove other filters PUESTO**. Con un solo filtro el tilde deja de ser trampa: siempre va tildado. Los casos del droplist de orden solo tocan sorts, así que el filtro sobrevive.
  - Si en el Preview aparecen libros con existencia 0, forzá el número: `[[Item.Categoria == Var_Categoria && (Item.Existencia * 1) >= 1]]`.
- **Los 4 criterios de orden ya no son todos Number.** Este es el error específico de este parcial:

| Criterio | Column | Sort as | Order |
|---|---|---|---|
| Titulo de A a Z *(default)* | Titulo | **TEXT** | Ascending |
| Titulo de Z a A | Titulo | **TEXT** | Descending |
| Precio más bajo | Precio | **NUMBER** | Ascending |
| Precio más alto | Precio | **NUMBER** | Descending |

  Con Titulo como Number, Axure lo lee como 0 y no ordena nada: parece que el caso está roto y lo que está mal es el tipo. El `Add Sort` del `Page Loaded` tiene que ser el mismo que el default (Titulo, Text, Ascending): el CU dice que la lista llega ya ordenada así.
- **`Update Rows` — la única mecánica nueva.** Está en `Add Action → Repeaters`, al lado de `Add Sort` / `Add Filter`. En el botón **Comprar** (que está **dentro** del ítem): `Update Rows → Repeater: Libros → Rows: This → Column: Existencia → Value: [[Item.Existencia - 1]]`. Si el selector de Rows no ofrece "This", usá `Rows: Rule` con `[[Item.Titulo == Var_TituloLibro]]` — pero entonces el `Set Variable Value` de `Var_TituloLibro` tiene que ejecutarse **antes** dentro del mismo `Click or Tap`.
- **Que el descuento no se vea al volver no es un bug.** El dataset del repeater se reinicia en cada carga de página y `Open Link` recarga. Lo que se corrige es que la acción esté bien armada. No lo debuguees.
- **Fecha del pedido (now).** Todo el bloque `Date.parse` / `Math.floor` del hotel desaparece. **[CÁTEDRA]** (apunte *Consejos para cálculo con fechas* v1.03), formato DD/MM/YYYY:
  `[[Now.toISOString().substr(8,2)]]/[[Now.toISOString().substr(5,2)]]/[[Now.toISOString().substr(0,4)]]`
  Evitá `[[Now.getDate()]]/[[Now.getMonth()]]/[[Now.getFullYear()]]`: el mes sale con un dígito y `getMonth()` de Axure ya devuelve 1-12. `toISOString()` es UTC: después de las 21:00 hora argentina adelanta el día → `Now.addHours(-3).toISOString()`.
- **Número de pedido.** `Var_NroPedido` con default **1000** y, en el botón Comprar antes del `Open Link`: `Set Variable Value Var_NroPedido to [[Var_NroPedido + 1]]`. El default **tiene** que ser un número: con la variable vacía, `+1` concatena o da NaN. Alternativa de una línea: `Set Text Cbte_NroPedido to [[Math.floor(Math.random() * 100000)]]`.
- **Botón Cancelar (2.a).** Va en la página del **listado**, al lado del droplist de orden, porque 2.a es la alternativa al paso 2. Una sola interacción: `Click or Tap → Open Link → Inicio`. Sin `Update Rows` ni `Set Variable Value`. Si querés cubrir la otra lectura, poné un segundo botón igual en el comprobante: son 20 segundos.
- **Validación del botón Buscar.** El CU no la pide explícitamente pero es el patrón que la cátedra corrige. Acá es una sola fila: `Enable Case → [[Var_Categoria]] does not equal (vacío) → Open Link`. Alternativa: dejar una categoría tildada como default en Edit List Items.

### 5.4 El cronograma

| Tiempo | Bloque |
|---|---|
| **0:00-0:03** | **Setup.** Abrí **Axure RP 9** (ver trampas). `Project → Global Variables`: las 4, con sus defaults. Pages: Inicio, MostrarLibros, Comprobante. **Guardá ya como `Apellido_Nombre.rp`** y Ctrl+S al cerrar cada bloque. |
| **0:03-0:08** | **Página Inicio.** Label "Pedir un libro" + Droplist `Categoria` (Edit List Items: `Novela`, `Tecnico` — sin tilde, exactamente como van en el repeater) + Primary Button "Buscar libro" con `Set Variable Value Var_Categoria to [[Categoria.selectedOption]]` + `Open Link`. Preview y mirá la Console: **no sigas hasta que esa variable se llene.** |
| **0:08-0:18** | **Repeater y datos.** Arrastrá Repeater, nombralo `Libros`, tildá Fit to Content in HTML. Columnas: Categoria, Titulo, Existencia, Precio. 6 filas, dos categorías, **al menos un libro con existencia 0 en cada una**: `Novela/Cien años de soledad/3/12000`, `Novela/Rayuela/0/15000`, `Novela/El Aleph/2/9000`, `Tecnico/UML y Patrones/4/22000`, `Tecnico/Writing Effective Use Cases/1/30000`, `Tecnico/Clean Code/0/25000`. Precios pelados. |
| **0:18-0:26** | **Ítem del repeater.** Doble click. Tres widgets `Titulo`, `Existencia`, `Precio` + Button "Comprar". Volvé al canvas, seleccioná el repeater, `Item Loaded`: **un** `Set Text` con **tres Add Target**. Preview: 6 filas con 3 datos. Si ves solo el título, faltan los Add Target. |
| **0:26-0:31** | **Botón Comprar (dentro del ítem).** `Click or Tap`, **en este orden**: (1) `Set Variable Value Var_TituloLibro to "[[Item.Titulo]]"`; (2) `Set Variable Value Var_NroPedido to "[[Var_NroPedido + 1]]"`; (3) `Update Rows` (Libros, This, Existencia, `[[Item.Existencia - 1]]`); (4) `Open Link → Comprobante`. |
| **0:31-0:37** | **Cabecera + Page Loaded de MostrarLibros.** (1) `Set Text` Cab_Cliente ← Var_Cliente, Add Target Cab_Categoria ← Var_Categoria; (2) `Add Filter` CategoriaYStock con la regla compuesta y **Remove other filters tildado**; (3) `Add Sort` TituloAZ (Titulo, Text, Ascending). **Este es el paso 1 completo del CU: si acá anda, tenés la mitad del puntaje.** |
| **0:37-0:45** | **Droplist de orden.** `OrdenadoPor`, 4 ítems (el A-Z tildado como default), `Selection Changed → Enable Cases`, 4 casos con Else If, cada uno con `Remove Sort (All)` **antes** del `Add Sort`. Probá los cuatro y verificá que el filtro de categoría no se rompa. |
| **0:45-0:47** | **Botón Cancelar** en MostrarLibros, fuera del repeater: `Open Link → Inicio`. |
| **0:47-0:54** | **Comprobante.** Cuatro Text Field (`Cbte_NroPedido`, `Cbte_Fecha`, `Cbte_Cliente`, `Cbte_Titulo`) y un `Set Text` con cuatro Add Target. Acá **no hay dependencias de orden**, a diferencia del comprobante del hotel. |
| **0:54-1:02** | **Prueba de punta a punta**, dos veces con categorías distintas: categoría → Buscar → cabecera + filtro + sin existencia 0 + orden A-Z → los 4 criterios → Comprar → comprobante con nro incrementado, fecha, cliente y título → Cancelar. Console abierta con las 4 variables. Si algo sale vacío, casi siempre es el nombre de la variable o un Add Target que falta. |
| **1:02-1:05** | **Entrega.** `File → Save As → Apellido_Nombre.rp`. Verificá que exista y pese. Mandalo con asunto exacto **"Parcial Axure"**. **Hacé esto aunque te falte algo.** |

**Orden de sacrificio si vas corto:** primero la validación del botón Buscar; después dos de los cuatro criterios de orden (dejá **Titulo A-Z** y **Precio más bajo**, que muestran que sabés Text y Number); después la prolijidad visual del ítem. **Nunca se saca**: el filtro compuesto, el `Item Loaded`, el botón Comprar con `Update Rows` (está en la postcondición explícita del CU) y el comprobante con los cuatro datos.

### 5.5 Trampas de Axure

**[NUESTRO]**

1. **Entregar un `.rp` que no abra.** `entregables/prototipoRegistrarPrestamo.rp` está guardado con **RP 11**, y **RP 9 no abre archivos de RP 11**. Si el docente abre con RP 9 no ve nada: es un cero de hecho. **Confirmá la versión antes de arrancar**; si tenés la VM con RP 9, usá la VM.
2. **`Sort as: Number` para Titulo.** El error específico de este parcial, porque en el hotel los cuatro eran Number y la mano va sola.
3. **Olvidar `Remove Sort → All`** antes de cada `Add Sort`. Va en los cuatro casos.
4. **Poner el botón Comprar FUERA del ítem del repeater.** Si no está adentro, `[[Item.Titulo]]` no resuelve, `[[Item.Existencia - 1]]` tampoco y `Rows: This` no tiene fila actual. **Se cae todo el paso 2 junto.** Es el error más caro.
5. **Buscar `Update Rows` en el menú equivocado**: está en `Add Action → Repeaters`, no en Widgets ni en Variables. Si no te ofrece "This", es que estás editando desde afuera del repeater (ver #4).
6. **`Var_NroPedido` con default vacío** → concatena ("1", "11") o NaN.
7. **`Var_Cliente` sin default** → cabecera y comprobante sin nombre: dos requisitos explícitos perdidos con un solo olvido.
8. **Precios con `$` o separador de miles** → `Sort as: Number` deja de funcionar. El `$` ponelo en el label de al lado.
9. **No cargar ningún libro con existencia 0** → el corrector no tiene cómo ver que implementaste el ≥ 1 y asume que no está.
10. **Que el string de categoría no coincida** ("Técnico" con tilde en el droplist vs "Tecnico" en el repeater) → lista vacía y diez minutos buscando el error en la Rule. Copiá y pegá el mismo string. Lo mismo con los 4 textos del droplist de orden.
11. **Armar dos `Add Filter` separados** por inercia del hotel y caer en la trampa del tilde. Acá va uno solo.
12. **Reconstruir los RadioButtons con Assign Radio Group.** No van: la categoría se elige en la página anterior.
13. **Agregar columna Foto.** El CU no la pide y cargar imágenes con Import Image celda por celda es el mayor devorador de tiempo del TP del hotel.
14. **`[[Now.getMonth()]]` / `[[Now.getDate()]]`** para armar la fecha → un solo dígito. Usá el `substr` del apunte.
15. **No guardar como `Apellido_Nombre.rp` ni mandar el asunto "Parcial Axure".** Está escrito dos veces en el enunciado.

---

## 6. Checklist de entrega

**[CÁTEDRA]** Los 30 segundos finales. No los saltees por apuro.

**Bizagi**

- [ ] ¿Está mi **apellido como texto visible DENTRO** del diagrama principal **y también** dentro del subproceso? (no solo en el nombre del archivo)
- [ ] ¿Exporté **después** de poner el apellido, y no antes?
- [ ] ¿Son **dos imágenes separadas**: principal y subproceso?
- [ ] ¿Formato **jpg**, no png ni pdf ni captura pegada en un Word?
- [ ] ¿Nombres exactos **`Apellido_pp.jpg`** y **`Apellido_sub.jpg`**, sin espacios ni tildes?
- [ ] ¿Abrí los dos jpg y se leen los nombres de tareas, compuertas y pools sin pixelarse ni cortarse?
- [ ] ¿Adjunté **también el archivo `.bpm`**, no solo las imágenes? (**[NUESTRO]** nombralo `Apellido.bpm`: el enunciado no lo pauta)
- [ ] ¿El `.bpm` que subo es la versión final guardada (**Ctrl+S antes de exportar**)?

**Axure**

- [ ] ¿Guardado como **`Apellido_Nombre.rp`** — apellido primero, nombre después?
- [ ] ¿Con la versión que pide la cátedra? **RP 9 no abre archivos de RP 11.**

**Cierre**

- [ ] ¿Confirmé el canal: **Classroom** para Bizagi, y para Axure lo que haya dicho el docente hoy? Si es mail, asunto textual **"Parcial Axure"**.
- [ ] ¿**Contesté y envié** la teoría multiple choice, o quedó abierta en otra pestaña?
- [ ] ¿Le di **"Entregar"/"Enviar"** en Classroom y **veo los archivos ya adjuntos** en la tarea, no solo cargados?