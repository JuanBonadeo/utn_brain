# Intro a la Práctica Profesional — Wiki

## Índice
1. Unidad 1 — Modelado de procesos con BPMN (Bizagi Modeler)
2. Unidad 2 — Prototipado con Axure RP 9

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
  → gateway **inclusivo** (O).
- **C**: revisado puede salir rechazado / aprobado / con correcciones
  → gateway **exclusivo** (X) de tres salidas, con loop al autor en la tercera.

Si entra este caso, la trampa es resolver B con un exclusivo. No es exclusivo:
redacción va siempre y diseño a veces, o sea **una o más** ramas.

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

La cátedra trabaja con **Axure RP 9** (v9.0.0.3727, feb 2021), con licencia UTN
provista y una VM preparada. Ojo: el entregable
`entregables/prototipoRegistrarPrestamo.rp` está guardado con **Axure RP 11** —
RP 9 no abre archivos de RP 11. Verificar con qué versión se rinde.

Un prototipo sin navegación es un dibujo. Lo que lo vuelve prototipo:
seleccionar el widget → panel **Interactions** → *Click or Tap* → *Open Link* →
página destino. Probar siempre con **Preview** antes de entregar.

Piezas que usa la cátedra:
- **Repeater**: la grilla con dataset propio. Es el corazón del CU Reservar
  habitación.
- **Dynamic Panel**: estados múltiples (mostrar/ocultar, modales, tabs).
- **Masters**: elementos repetidos entre páginas (header, nav).
- **Bootstrap 3 Library** (`bootstrap_3-v0.1.1.rplib`): librería de widgets
  provista por la cátedra.

#### Desarrollo — CU 001 Reservar habitación

Fuente: `TP_Repeater_CU_Reservar_habitacion_v1_02.pdf` (Enrique Porta, v1.02,
13-05-2019).

- **Actor** primario e iniciador: Cliente. **Precondición**: cliente logueado.
- **Postcondición (éxito)**: la reserva de la estadía quedó registrada.
- Nivel: usuario. Alcance: sistema. Caja: negra. Interacción: dialogal.

**Paso 1.** El cliente ingresa ciudad, fecha de entrada, fecha de salida y
cantidad de personas. El sistema muestra los hoteles disponibles para ese
período **con capacidad ≥ cantidad de personas**, mostrando por cada uno: foto,
denominación, dirección, estrellas y precio por noche.

Además muestra la ciudad ingresada, el filtro **Estrellas** con "Todas las
estrellas" por defecto, y **Ordenado por** con "Más estrellas" por defecto.

- **1.a** — el cliente ordena por: Precio más bajo, Precio más alto, Menos
  estrellas o Más estrellas.
- **1.b** — el cliente filtra por cantidad de estrellas.

**Paso 2.** El cliente selecciona un hotel. El sistema **registra la estadía** y
muestra el comprobante: apellido y nombre del cliente, denominación del hotel,
ciudad, fecha de ingreso, fecha de salida y costo de la estadía.

Ejemplo del enunciado:
`Cliente: Pérez, Juan | Hotel: Holiday Inn | Ciudad: Rosario |
Fecha ingreso: 4/12/2017 | Fecha salida: 5/12/2017 | Costo estadía: 1630`

**Lo que el repeater tiene que soportar**: ordenar por dos campos numéricos
(Precio, Estrellas) en ambas direcciones, y filtrar por Estrellas. Por eso
Precio y Estrellas se cargan como **número sin formato** — sin `$` ni separador
de miles. El formato visual se aplica en el widget, no en el dato.

**Dataset**: `entregables/hoteles-repeater.csv` — los 4 hoteles que tienen foto
en `fuentes/Axure_RP9/Caso_Reservar_Habitacion/`. Tres en Rosario y uno en
Córdoba, para que el filtro por ciudad tenga sentido.

La columna **Foto** del repeater es de tipo imagen: guarda una referencia interna
de Axure, no texto. **El CSV no la puede llenar** — las imágenes se arrastran a
mano celda por celda.

#### Dudas / pendientes
- `Axure_RP9_CU_Reservar_Habitacion_v1_02.pdf` (1 MB, capturas de las pantallas):
  el PDF no da texto en la conversión, hay que leerlo con visión. **Es el diseño
  de pantallas esperado** — pendiente y de alto valor.
- `Caso_Registrar_Prestamo/` (docx + 2 PDFs): sin ingerir. Es el CU que ya
  prototipaste.
- `Consejos/`: búsqueda predictiva y cálculos con fechas, con sus `.rp` de
  ejemplo. Los cálculos con fechas son directamente aplicables al costo de la
  estadía (noches × precio). Sin ingerir.
- `Enlaces_en_Axure_RP_9_y_Axure_RP_10.pdf`: sin ingerir.

#### Fuentes
- `fuentes/Axure_RP9/Caso_Reservar_Habitacion/TP_Repeater_CU_Reservar_habitacion_v1_02.pdf` ✅ ingerido
- `fuentes/Axure_RP9/` — resto pendiente
- `entregables/prototipoRegistrarPrestamo.rp` (Axure RP 11)
- `entregables/hoteles-repeater.csv`

## Log
- Archivo creado.
- 2026-09-06: ingesta inicial. Descomprimidos `Axure_RP9.zip` y `BPMN.zip` en
  `fuentes/`. Creadas Unidad 1 (BPMN/Bizagi) y Unidad 2 (Axure RP 9). Ingeridos
  los enunciados de los 7 casos BPMN y el TP del repeater del CU Reservar
  habitación. Corregido `hoteles-repeater.csv` al dataset real de la cátedra.
  Instaladores `.exe` de Bizagi gitignorados (389 MB).
