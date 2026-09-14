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
