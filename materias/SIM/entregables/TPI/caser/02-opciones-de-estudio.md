# Opciones de estudio para el TPI sobre CASER

> Menú para discutir con la empresa. Cada opción es un problema de decisión distinto sobre la misma planta.
> Todas se hacen con un modelo de eventos discretos en AnyLogic (Process Modeling Library), con escenario
> base + alternativo(s), 30 réplicas por escenario y test de medias. Elegir **una** como principal; las otras
> pueden ir como segundo y tercer tema del formulario.

> **Nota de estado (2026-09-22)**: tras relevar las planillas reales de producción, el horno (Opción 3 acá
> abajo) pasó a ser el **tema principal** — ver `04-formulario-eleccion-tema.md`, que tiene la versión vigente
> y ya acoplada con stock. Esta numeración (1-4) se conserva como catálogo de opciones consideradas; no
> refleja la prioridad final.

## Criterio para elegir

Como la capacidad no es el cuello de botella (la planta está subutilizada), los estudios que sirven son los
de **mix, costo y capital inmovilizado**, no los de throughput. Las opciones están ordenadas por ese criterio.
La 4 se deja por completitud.

---

## Opción 1 — Stock vs. contra pedido: cuánta plata dejar parada en estantería

**Pregunta**: para un conjunto de artículos, ¿pasar los de baja rotación de "fabricar para stock" a "fabricar
solo contra pedido / lote mínimo" reduce el inventario inmovilizado sin que el nivel de servicio baje de un
mínimo aceptable?

**Por qué le sirve a la empresa**: en concurso y sin crédito, el capital atado en stock de baja rotación es
plata que no está. Es la decisión de menor riesgo y más rápida de aplicar.

**Escenarios**
- Base: política actual de reposición (aunque sea "a ojo", se reconstruye de las órdenes de fabricación históricas).
- Alt 1: artículos clase C contra pedido; A y B con punto de pedido y lote.
- Alt 2 (opcional): lotes más chicos para todos, con punto de pedido.

**Salidas**: inventario promedio valorizado, fill rate (% pedidos servidos completos y a tiempo), horas de
cambio de matrices, tiempo de entrega promedio.

**Datos a buscar**
- ABM: ventas por artículo con fecha y cantidad, 24 meses → tasa de pedidos y distribución del tamaño por artículo.
- ABM: maestro de artículos (familia, precio, costo estándar, stock actual).
- ABM / planillas: órdenes de fabricación históricas (artículo, cantidad, fecha inicio, fecha fin) → lote típico y lead time real de producción.
- Planillas: tiempo de cambio de matrices (o estimación del encargado).
- Plazo del zincado tercerizado (remitos de ida y vuelta).
- Pedidos pendientes / faltantes, si se registran. Si no, se asume backorder.

**AnyLogic**: ejemplo oficial *Supply Chain* (política estacionaria de inventario, backlog, costos de holding y faltante). Es la Unidad 4 (modelo (s, S)) en DES.

**Riesgo**: bajo. Es el más acotado y el más alineado con la materia. Animación poco vistosa para el video (se compensa mostrando gráficos de stock en vivo).

---

## Opción 2 — Fabricar vs. importar, artículo por artículo

**Pregunta**: dado que ya importan algunos productos, ¿para qué artículos conviene importar y para cuáles
fabricar, considerando que importar es más barato por unidad pero exige lotes grandes, plazo largo y
variable, y capital adelantado?

**Por qué le sirve**: es la decisión estratégica que la empresa ya está tomando a la fuerza. El modelo le
pone números a algo que hoy se decide por intuición, y captura lo que el costo unitario no muestra: el
stock que genera un contenedor y el riesgo de quedarse sin producto durante 90 días.

**Escenarios**
- Base: mix actual fabricado/importado.
- Alt 1: importar también los artículos de alta rotación que hoy se fabrican.
- Alt 2: volver a fabricar algo de lo que hoy se importa (si el costo lo justifica) — sirve para mostrar que "no hay diferencia" también es resultado.

**Salidas**: margen de contribución acumulado, inventario promedio valorizado, fill rate, días sin stock por artículo.

**Datos a buscar**
- Todo lo de la Opción 1, más:
- ABM / planillas: compras importadas (fecha de pedido, fecha de llegada, cantidad, costo puesto en planta, mínimo de compra) → distribución del plazo de importación.
- Costo de fabricación por artículo (o índice fabricar/importar).
- Condiciones de pago al importar (anticipo) — solo si quieren medir capital adelantado.

**AnyLogic**: mismo modelo de la Opción 1 con dos ramas de reposición (producción: plazo corto; importación: plazo largo lognormal + lote grande). Ejemplo oficial *Flexible Manufacturing Supply Chain* (elección entre proveedores).

**Riesgo**: medio. Depende de que haya datos de importación suficientes (varias compras, no una). Si hay pocas, el plazo se estima con cotizaciones y se declara como supuesto.

---

## Opción 3 — Horno de tratamiento térmico: cuándo lanzar una carga

**Pregunta**: el horno trabaja por cargas (lotes). Con poco volumen, ¿conviene esperar a llenarlo (menos
energía por kilo, más demora) o correr cargas parciales (más rápido, más caro por kilo)? ¿Qué regla de
lanzamiento minimiza el costo sin disparar el tiempo de entrega?

**Por qué le sirve**: el horno se reactivó en 01/2026 seguramente para dejar de tercerizar el tratamiento.
Con volumen bajo, la regla de carga define si esa reactivación conviene o no. Es un costo energético
grande y una decisión que hoy alguien toma todos los días a criterio.

**Escenarios**
- Base: regla actual (a relevar: "se corre cuando hay X kg" o "cada N días").
- Alt: regla umbral + tiempo máximo de espera (lanzar cuando la carga llega al X % **o** cuando la pieza más vieja espera más de T días), con dos o tres valores de X y T.

**Salidas**: costo de energía por kg tratado, espera promedio antes del horno, lead time total de la orden, cantidad de cargas por mes, ocupación promedio por carga.

**Datos a buscar**
- Registro de cargas del horno (obligatorio por ISO): fecha, kg o piezas, artículos, duración del ciclo, consumo de gas/energía si lo anotan.
- Capacidad máxima por carga.
- Órdenes de fabricación con fechas → cuánto llega al horno por día y con qué variabilidad.
- Criterio actual de lanzamiento (entrevista).

**AnyLogic**: `Source` → `Queue` → `Batch` (con condición de umbral / timeout) → `Seize` horno → `Delay` ciclo → `Unbatch` → `Sink`. Es una cola con servidor por lotes (Unidad 3/8, versión batch). No hay ejemplo oficial calcado; los bloques están todos en la Process Modeling Library.

**Alcance del "horno" en el modelo**: cementación + temple, que la empresa hace en un solo ciclo en el horno
grande (confirmado en planillas: máquina "TKN + generador endotérmico", 145 kW). El revenido es un proceso
aparte, en un horno chico separado ("POTE", 15 kW), que no se aplica a todos los artículos y tiene muchos
menos registros — queda fuera de la cola/lote simulada; para los artículos donde aplica se estima como una
demora fija adicional, no como un segundo régimen de campaña.

**Riesgo**: medio-bajo. Muy acotado y original (el profe valora originalidad). Depende de que el consumo energético por carga sea conocido o estimable.

---

## Opción 4 — Agrupar la producción para reducir cambios de matrices

**Pregunta**: con pocas órdenes, ¿conviene fabricar en el orden en que llegan (FIFO) o agrupar por familia /
diámetro en "campañas" para reducir cambios de matrices, aunque algunas órdenes esperen más?

**Por qué le sirve**: cada cambio de matrices son horas de operario sin producir. Con 23 personas, las horas
hombre son el costo. Menos setups = menor costo por pieza.

**Escenarios**: FIFO vs. agrupado por familia vs. campañas periódicas (una familia por semana).

**Salidas**: horas de setup por mes, lead time de una orden, utilización de máquinas y operarios, órdenes atrasadas.

**Datos a buscar**
- Tiempos de cambio de matrices por máquina y por tipo de cambio (el estudio que mencionó Gonzalo, si existe).
- Tiempos de ciclo (piezas/hora) por máquina y familia.
- Órdenes de fabricación con secuencia real de ejecución.
- Máquinas y operarios disponibles por sector.

**AnyLogic**: ejemplo oficial *Job Shop* (tutorial en 5 fases). `Source` órdenes con atributo familia → `Queue` con prioridad → `Seize` máquina + operario → `Delay` setup condicional (si cambia la familia) → `Delay` ciclo → `Release`.

**Riesgo**: medio. Es el más vistoso en pantalla pero el que más datos de tiempos necesita, y el menos relevante mientras la planta esté subutilizada. Si sobra capacidad, el resultado probable es "no hay diferencia significativa en lead time" — válido pero poco útil para la empresa.

---

## Qué NO conviene estudiar

- **Dotación / turnos** (cuántos operarios necesita el volumen actual): técnicamente simulable, pero el objetivo declarado del concurso es conservar puestos. No es una pregunta que la empresa quiera que un TP responda.
- **Flujo de caja, punto de equilibrio, recupero de inversión**: es contabilidad, no simulación. Queda fuera del TPI.
- **Instalar la línea de cincado propia**: requiere datos de inversión y volumen futuro que no existen. Puede ir como "trabajo futuro" en las conclusiones.

## Recomendación

Principal: **Opción 1**, con la **Opción 2** como extensión natural (es el mismo modelo con una rama más).
Tercer tema del formulario: **Opción 3** (horno), que es la más original y la más acotada.

Cómo plantearlo a la empresa: preguntar cuál de estas tres decisiones se está tomando hoy a ojo y les gustaría
ver con números. Esa es la que va.

## Ejemplos oficiales de AnyLogic (verificado 2026-09-13 en AnyLogic Cloud, "Examples by AnyLogic team")

| Ejemplo | Qué modela | Opción |
|---|---|---|
| [Job Shop](https://cloud.anylogic.com/model/e2181700-6ffa-47f0-9177-302c09c2cc49?mode=SETTINGS) (+ [tutorial en 5 fases](https://anylogic.help/tutorials/job-shop/index.html)) | Taller chico con máquinas CNC, almacenamiento, operarios; utilización y costos | 4 |
| [Supply Chain](https://cloud.anylogic.com/model/a17b5bbe-7c9d-4460-9be7-15c9820ebec0?mode=SETTINGS) | Minorista + mayorista + fábrica con política estacionaria de inventario, backlog, costos | 1, 2 |
| [Flexible Manufacturing Supply Chain](https://cloud.anylogic.com/model/aca0a876-e208-4f1d-ac1c-a03d97399bb6?mode=SETTINGS) | Productores con umbral de stock que eligen entre proveedores alternativos | 2 |
| Maintenance (tutorial en 7 fases) | Máquinas que fallan y se reparan; correctivo vs. preventivo | agregado opcional |
| Activity Based Costing Analysis | Piso de fábrica con costo por recurso ocupado/ocioso | medir costo en cualquiera |
| Inventory Workforce, Stock Management Game, Widgets with Material Inventory | System Dynamics (importados de Vensim) | **no** — no es el paradigma de la cátedra |

Los modelos de la cátedra (`fuentes/practica/anylogic/`: MM1, Peaje, Airport) son todos Process Modeling Library.
