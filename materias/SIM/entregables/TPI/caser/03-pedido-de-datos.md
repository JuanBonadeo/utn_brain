# Pedido de datos a la empresa

> Para mandar tal cual. La **base común** sirve para cualquiera de las opciones y permite hacer la clasificación
> ABC y elegir los artículos. Lo específico se pide después de elegir la opción.

## Base común (pedir ya)

Exportar del ABM, en Excel o CSV, últimos 24 meses:

1. **Ventas**: fecha, cliente (puede ir codificado), artículo, cantidad, precio unitario.
2. **Maestro de artículos**: código, descripción, familia, unidad, precio de lista, costo estándar (puede ir en índice), stock actual, origen (fabricado / importado / comprado nacional).
3. **Órdenes de fabricación**: artículo, cantidad, fecha de inicio, fecha de fin, máquina si se registra.
4. **Compras**: fecha de pedido, fecha de recepción, proveedor, artículo o materia prima, cantidad, costo. Separar importaciones.
5. **Stock valorizado actual** por artículo.

Con esto se hace el ABC, se ve qué se vende, qué se fabrica, qué se importa y cuánto hay parado.

## Específico por opción

**Opción 1 (stock vs. contra pedido)**
- Tiempo de cambio de matrices en estampadora y laminadora (registro o estimación).
- Plazo ida y vuelta del zincado tercerizado (remitos).
- Pedidos pendientes / faltantes, si se registran.
- Qué artículos ya son contra pedido y por qué.

**Opción 2 (fabricar vs. importar)**
- Lo de la Opción 1, más:
- Historial de importaciones: fecha de pedido, fecha de llegada a planta, cantidad, costo puesto en planta, mínimo de compra, condición de pago.
- Costo de fabricación por artículo (o relación fabricar/importar en índice).

**Opción 3 (horno)**
- Registro de cargas del horno: fecha, kg o piezas, artículos, duración del ciclo, consumo si lo anotan.
- Capacidad máxima por carga y costo energético por ciclo (o por hora).
- Criterio actual para lanzar una carga (entrevista de 10 minutos).

**Opción 4 (cambios de matrices)**
- Estudio/registro de tiempos de cambio de matrices por máquina y tipo de cambio.
- Tiempos de ciclo (piezas/hora) por máquina y familia.
- Secuencia real de ejecución de las órdenes.
- Máquinas operativas y operarios por sector.

## Preguntas de entrevista (10 minutos con quien maneja producción)

1. ¿Cómo deciden hoy cuándo fabricar un artículo de stock y cuánto?
2. ¿Qué artículos se fabrican solo contra pedido? ¿Por qué esos?
3. ¿Cuánto tarda un cambio de matrices? ¿De qué depende?
4. ¿Cuándo lanzan una carga del horno?
5. ¿Cuánto tarda el zincado en volver? ¿Cuál es el peor caso?
6. ¿Qué nivel de servicio consideran aceptable? ¿Pierden ventas por falta de stock?
7. ¿Qué importan hoy, a quién, con qué plazo y mínimo?

---

## Pedido para el Tema 1 (horno) — 2026-09-16

> Complemento de la base común, armado después de que la empresa confirmó que entrega ventas, maestro, OF,
> compras, stock valorizado, clientes/proveedores, cargas de horno, rechazos, trazabilidad, energía (consumo
> con y sin campaña, potencia contratada, tarifa) y demanda no atendida. Para mandar tal cual.

### A. Datos que no estaban en la lista

- **Zincado tercerizado**: remitos de ida y vuelta (fecha de salida, fecha de regreso, artículo, kg), 24 meses,
  y costo por kg.
- **Gas del generador endotérmico**: facturas o consumo mensual, 24 meses; consumo por hora en arranque y en
  régimen; si arranca junto con el horno o tiene su propio tiempo de arranque.
- **Ficha técnica del horno**: potencia total y por resistencia (kW); cuántas ULI viajan en la cinta a la vez y
  tiempo de residencia (largo / velocidad); si la velocidad de cinta o la temperatura cambian por artículo; si
  las 36 h de calentamiento son a plena potencia.
- **Mantenimiento del horno**: reemplazos (resistencias, cinta, mufla, retorta del generador) con costo y fecha,
  y cuántos encendidos hubo en ese lapso.
- **Capacidades aguas arriba**: piezas/hora por máquina o familia en estampado y laminado, tiempo de cambio de
  matrices, máquinas operativas.
- **Calendario de planta** en los 24 meses: horario del turno, feriados, vacaciones, paradas.
- **Estado actual**: ULI esperando el horno hoy y estado del horno (apagado / campaña en curso).
- **Tasa de costo del capital** que usan (costo financiero mensual), en índice.

### B. Preguntas para el encargado (15 minutos)

1. Regla de encendido: ¿solo "cuando hay 70-80 ULI"? ¿Adelantan por pedidos comprometidos o clientes grandes?
   ¿Quién decide y mirando qué?
2. Fin de campaña: ¿las ULI que se producen con el horno caliente se meten en la misma campaña? ¿Cuánto esperan
   con la cinta vacía antes de apagar? ¿Alguna vez lo dejaron encendido entre campañas?
3. Turnos de carga por día durante la campaña (1, 2 o 3) y horario. ¿Queda supervisado de noche?
4. Qué es una ULI: kg y piezas por ULI por artículo, o rango. ¿Varía mucho?
5. ¿El ciclo varía por artículo o familia (profundidad de capa, temperatura)? ¿Se pierde tiempo al cambiar de
   artículo dentro de la campaña?
6. ¿Cómo deciden cuándo y cuánto fabricar de cada artículo de stock (punto de pedido, lote mínimo, a ojo)?
7. Plazo comprometido con el cliente: stock (inmediato) vs. contra pedido (X días). ¿Qué nivel de servicio
   consideran aceptable? ¿Pierden ventas por falta de stock?
8. Registro de cargas: ¿desde cuándo? ¿Hay de antes de la parada? ¿Enero-febrero 2026 fue puesta a punto?

### C. Cómo pedir lo que ya van a mandar

- Excel/CSV, un archivo por tabla, 24 meses, con un diccionario mínimo de campos (estados de OF, códigos de
  familia, unidades).
- **Ventas**: fecha, cliente codificado, artículo, cantidad, precio y **fecha de entrega/remito**. Presupuestos
  con estado (convertido o no) y NV canceladas.
- **OF**: artículo, cantidad, fecha de emisión, inicio, fin, máquina; si se ve cuándo quedó lista para el horno
  y cuándo se cargó, mejor.
- **Cargas del horno**: por ULI o por carga: fecha y hora, artículo, kg, piezas, ciclo, campaña a la que
  pertenece, y encendido/apagado de cada campaña. Si es papel, foto de todo.
- **Rechazos**: por etapa (horno, zincado, otro), cantidad y motivo.
- **Energía**: factura completa de cada mes (kWh por franja horaria si la tarifa la tiene, potencia contratada,
  potencia máxima registrada, penalidades), y si tienen lectura de medidor por campaña.
- **Maestro**: por artículo: familia, ruta (pasa por horno sí/no, zincado sí/no), stock / contra pedido /
  importado, piezas y kg por ULI, costo estándar en índice.
- **Artículos representativos**: qué porcentaje del volumen del horno (kg o ULI) representan los elegidos, o
  que el registro de cargas identifique el artículo por ULI. El horno tiene que ver el volumen completo: los
  elegidos se modelan uno por uno y el resto como flujo agregado.

## Recibido y estado (2026-09-24)

- **Maestro comercial — parcialmente resuelto con "Casermeiro SRL - Lista CASER.xlsx"** (recibida
  2026-09-24). Es la lista de precios impresa exportada a Excel (con datos bancarios y todo, al final —
  no es una tabla plana). Hoja `CASER`: bloques por familia comercial real —
  **CASER-Fix, CASER-Wall, CASER-Drill, CASER-Max, CASER-Plast, CASER-Maq, CASER-Rosc** — cada uno con
  sub-bloques por tipo de cabeza/rosca/terminación y su tabla de código × medida × precio (a veces con un
  segundo código para la versión "estuche"). Hoja `Lista Exportable`: la misma lista pero ya en tabla plana
  (código, precio, unidades por envase, tipo de envase) — 1002 filas, 956 con código `C...`.
  Cruce hecho (`datos-locales/_perfil/maestro_lista_caser.csv`): 995 de 1002 códigos de `Lista Exportable`
  quedaron con familia asignada. Contra `Codigos y Planos.xlsm` (539 códigos), solo **286 cruzan** — quedan
  **253 artículos técnicos sin precio en esta lista** (¿discontinuados? ¿fuera de lista oficial?
  **a confirmar**).
  **Unidad de venta — aclarado (2026-09-25) por la empresa**: cada código granel/base (p. ej. `C1003551`)
  se vende por **millar** aunque se entregue en Caja Master de otra cantidad física (ej: se entregan cajas
  pero se facturan 2,5 millares); el código de **estuche** correspondiente (p. ej. `C10035515`) se vende por
  **unidad de estuche**, con el contenido de piezas indicado en la propia lista. Esto es exactamente lo que
  ya codifica la columna `Tipo de Envase` de `Lista Exportable` (Caja Master vs. Estuche), así que no hace
  falta pedir nada nuevo: se agregó `PrecioPorPieza = Precio / Unidades por Envase` al CSV cruzado, que sí es
  comparable entre artículos (el `Precio` crudo no lo era — mezclaba escala de millar y de estuche). Costo
  estándar ahora se aplica sobre `PrecioPorPieza` (× 0,335), no sobre el precio de envase.
  Sigue faltando: **origen** por artículo (aunque ya sabemos que el grupo 94-96 es todo fabricado, así que
  es poco crítico).
  **Stock/contra pedido — confirmado (2026-09-25) por la empresa, sin necesidad de archivo**: no manejan
  stock de seguridad reglado; por decantación es todo contra pedido, salvo excepciones puntuales todavía sin
  identificar. Ver la implicación de diseño en `05-respuestas-al-docente.md` §1.5.
- **Stock valorizado**: pendiente, sin novedad. Con "todo contra pedido" como supuesto, importa menos para
  la política de reposición (no hay s,Q que inicializar) pero sigue haciendo falta para el estado inicial del
  modelo (§5.1: material en cola/WIP al arrancar la corrida).
- **Compras**: pendiente, sin novedad. Baja prioridad para el Tema 1.
- **Ventas — recibidos dos reportes del ABM, pero NO son el listado transaccional pedido**:
  `REPORTE_0000001603.XLS` ("Estadística Anual De Venta", grupo 94-96, desde 09/2025, en unidades):
  cantidad vendida por artículo **por mes** (13 meses, 782 artículos, con total anual). Sirve para ABC y
  estacionalidad mensual, no da fecha de operación ni precio.
  `REPORTE_0000001604.XLS` ("Estadística De Venta Por Artículo", mismo período y grupo): cantidad total
  por **cliente × artículo** en todo el período (869 clientes), no por operación individual. Sirve para ver
  concentración de clientes, no da fecha ni precio.
  Ninguno de los dos alcanza para ajustar tiempo entre pedidos y tamaño de pedido por operación (lo que
  necesita `Source pedidos` en `05-respuestas-al-docente.md` §1.5). **Sigue pendiente pedir el listado
  transaccional línea por línea** (fecha, cliente, artículo, cantidad, precio), aclarando que no es una
  "Estadística" sino un listado o libro de ventas — puede que exista en el sistema aparte de los reportes
  ya recibidos. Si no existe, el respaldo es modelar demanda mensual agregada en vez de pedidos
  individuales, declarado como supuesto más débil (afecta la varianza de la cola del horno).
  Confirmado (2026-09-24): el grupo 94-96 es **todo el catálogo CASER, solo fabricados**; no incluye
  importados (que no se tratan térmicamente y quedan fuera del Tema 1 igual). `1603`/`1604` son entonces el
  universo completo de artículos relevantes para este tema, sin necesidad de filtrar nada más.

- **Demanda no atendida — RESUELTO, y es el hallazgo más importante de esta tanda.** Dos reportes nuevos,
  `REPORTE_0000001606.XLS` (presupuestado vs. facturado por cliente y artículo) y `REPORTE_0000001607.XLS`
  (lo mismo, agregado por artículo — 390 filas, sin desagregar por cliente), mismo período (01/09/2025 a
  31/08/2026), mismo grupo 94-96. Cada línea trae **Cantidad** (presupuestada) y **Entrega** (facturada).
  Cruzando ambos (`datos-locales/_perfil/analisis_1606.md` y `analisis_1607.md`):
  - **Fill rate global por unidades: 49-51%** (51,1% agregando 1606 por mi cuenta; 49,3% con el agregado
    directo de 1607 — consistentes).
  - **~20% de los artículos (77 de 386) tuvieron entrega CERO en los 12 meses** — demanda completamente
    perdida, no solo demorada.
  - Solo 31% de los artículos tuvo entrega completa.
  Esto reemplaza lo que hasta ahora era un supuesto ("la venta perdida es solo salida del modelo") por un
  **dato histórico real para calibrar y validar el nivel de servicio** — es la línea "Demanda no atendida
  histórica" de `05-respuestas-al-docente.md` §2.1, que estaba marcada `[confirmar]`.
  **Limitaciones a declarar**: (1) no distingue el motivo de la pérdida (stock, plazo, precio, el cliente
  compró en otro lado) — solo mide la brecha cantidad-entrega, no la causa; (2) el corte a fin de período
  censura: un presupuesto de agosto/2026 con entrega en septiembre/2026 cae como "cero" en este reporte
  aunque se haya cumplido después — puede estar subestimando el fill rate real; (3) hay códigos tipo `KIT`
  (p. ej. `KIT131`) que son combos, no artículos simples — excluir de la selección de representativos.
  Archivos: `REPORTE_...1603/1604/1606/1607.XLS`, `lista-caser.xlsx`, guardados en `datos-locales/abm/`
  (gitignoreados, no versionados).
