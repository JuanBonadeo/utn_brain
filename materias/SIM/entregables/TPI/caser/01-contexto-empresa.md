# TPI Simulación — Caso Casermeiro SRL (CASER)

> Carpeta del grupo de Gonzalo Casermeiro. Separada de `../` (grupo Bonadeo + Estevez).
> En el informe la empresa va con **nombre ficticio** y los montos en índices. Acá se usa el nombre real.

## Datos confirmados

Fuente: brief armado por la familia (2026-09-13) + respuestas de Gonzalo en la misma fecha.

**Empresa**
- Casermeiro SRL, Alvear (Santa Fe). Marca CASER / "Tornillo Caser".
- Fabrica y comercializa tornillos: autoperforantes, para techos, para muebles, especiales, otros elementos de fijación.
- ISO 9001:2015, renovada 11/2025 sin no conformidades → **hay registros de proceso obligatorios** (órdenes de fabricación, cargas de horno, rechazos, trazabilidad). Es la mejor fuente de datos de tiempos.
- Exportó a Uruguay, Paraguay, Brasil y Canadá (~10 contenedores/año durante ~4 años).
- Concurso preventivo desde 22/06/2026. Objetivo declarado: sostener la actividad, conservar puestos, recuperar equilibrio operativo.
- Dotación: ~23 personas (antes 55-60). Cerró el local comercial de Rosario; todo centralizado en Alvear.

**Planta** (~3.500 m²)
- Nave Norte (~1.000 m²): producción primaria.
- Nave Central (~1.000 m²): envasado, almacenamiento, comercial, logística.
- Entrepiso (~600 m²): oficinas y almacenes.
- Nave Sur (~900 m²): tratamientos térmicos y materia prima.
- Horno propio de cementación y temple, **reactivado en 01/2026**. Relevado 2026-09-15/16:
  - Eléctrico, 27 resistencias. ~36 h de calentamiento, ~48 h de enfriamiento.
  - **Cinta continua**: las ULI (unidad de transporte interno) pasan de a una; ~15 ULI por turno.
    Se enciende con ~70-80 ULI acumuladas; campaña de ~1 semana.
  - Tiene **generador de gases endotérmicos** (atmósfera de cementación): consume gas mientras el
    horno está caliente y tiene su propio arranque. Es un costo más por encendido y por hora caliente.
  - Cada encendido/apagado **desgasta** el horno (resistencias, cinta, mufla): costo fijo por encendido
    a estimar del registro de mantenimiento.
  - Cuando había mucha producción **convenía dejarlo encendido** entre campañas. Es el escenario
    "mantener caliente" cruzado con el nivel de demanda.
  - La empresa preguntó si se puede estudiar **cuántas ULI conviene esperar antes de encender**: es
    la variable de decisión del Tema 1 (barrido del umbral con réplicas e intervalos de confianza).
  - **Revenido es un equipo y un proceso aparte** (confirmado con las planillas 2026-09-22: horno grande
    "TKN + generador endotérmico", 145 kW, hace cementación + temple en un solo ciclo; el revenido se hace
    en un horno chico separado, "POTE", 15 kW) y **no se le hace a todos los productos**. Con muchos menos
    registros que el de cementación (192 completos contra 1032), no entra en la cola/lote del modelo — ver
    Supuestos.
- Línea de cincado electrolítico propia, **desinstalada / no operativa**.

**Proceso productivo** (confirmado por Gonzalo; casi todo interno)
1. Compra de alambre de acero listo para usar (no hay trefilado). Proveedor histórico: Acindar/ArcelorMittal.
2. Estampado (= recalcado en frío de la cabeza; la máquina es la estampadora/recalcadora; el setup es el **cambio de matrices**).
3. Laminado de rosca.
4. Tratamiento térmico (cementación y temple) en horno propio.
5. Lavado.
6. **Cincado — tercerizado** (fosfatizado también).
7. Envasado.
8. Almacenamiento y despacho.

**Sistemas y datos**
- Sistema de gestión / ABM en servidor local. **Se puede exportar sin problemas.**
- Muchas planillas Excel con información. "Hay data de sobra".
- Hay registros de fabricación.
- Posiblemente hay estudio/registros de los cambios de matrices (a confirmar).
- **Ya importan** algunos productos, forzados por el costo de fabricar → hay datos de compras importadas (plazo, costo, mínimos).

**Contexto económico** (condiciona qué vale la pena estudiar)
- Caída de demanda, importaciones, competencia china, costos financieros, sin crédito, cheques a plazo largo.
- El producto propio es de mayor calidad pero **caro de fabricar**.
- La capacidad instalada **no es el cuello de botella**: la planta está subutilizada. El problema es de mix, costo y capital, no de throughput.

## Supuestos que el modelo va a declarar (a validar con la empresa)

- Demanda estacionaria dentro del horizonte simulado (o estacionalidad simple si los datos la muestran).
- Un solo turno.
- Capacidad agregada por familia de producto, no máquina por máquina.
- Precios y costos constantes en el horizonte (en índices).
- Zincado tercerizado con plazo aleatorio; no se modela al tercero por dentro.
- **Revenido fuera del alcance del modelo de eventos discretos**: es un proceso aparte, en otro equipo, que
  no se aplica a todos los artículos. Para los artículos donde aplica se trata como una demora fija adicional
  (estimada de la mediana histórica), no como una cola/lote simulado. Los artículos representativos del Tema 1
  se eligen priorizando los que no pasan por revenido, para no ensuciar el modelo con un segundo régimen de
  campaña.

## Datos que la empresa entrega (confirmado 2026-09-16, exportación prevista 2026-09-17)

- ABM: ventas, maestro de artículos, órdenes de fabricación, compras, stock valorizado, clientes y proveedores.
- ISO: órdenes de fabricación, cargas de horno, rechazos, trazabilidad.
- Energía: consumo con y sin campaña, potencia contratada, tarifa.
- Demanda no atendida.
- Familias de productos con artículos representativos de buen movimiento.

Lo que falta pedir además de esto está en `03-pedido-de-datos.md` §Pedido para el Tema 1 (horno).

## Pendiente de relevar

- ~~Qué artículos son hoy stock / contra pedido~~ **Confirmado (2026-09-25)** por la empresa: en la práctica
  no manejan stock de seguridad reglado — por decantación, es **todo contra pedido**, salvo excepciones
  puntuales todavía sin identificar. Declarado como supuesto (ver `05-respuestas-al-docente.md` §1.5 y
  Supuestos). Importados: confirmado que el grupo 94-96 son solo fabricados (ver `03-pedido-de-datos.md`).
- Tiempos de cambio de matrices por máquina y tiempos de ciclo (piezas/hora) por operación.
- Plazo ida y vuelta del zincado tercerizado.
- Registro de cargas del horno: capacidad por carga, duración, consumo, criterio actual para lanzar una carga.
- Plazos, costos y mínimos de los proveedores importados.
- Nivel de servicio que consideran aceptable; cómo registran faltantes / pedidos pendientes.
- Máquinas operativas vs. fuera de servicio, operarios por sector, turnos históricos.

## Preguntas para la empresa (en orden)

1. ¿Cuál de las opciones de `02-opciones-de-estudio.md` le parece útil? Eso define todo lo demás.
2. ¿Hay artículos que hoy ya se fabrican solo contra pedido? ¿Cuáles y por qué?
3. ¿Cuánto tarda un cambio de matrices en estampadora y en laminadora? ¿Hay registro?
4. ¿Cuánto tarda el zincado tercerizado, ida y vuelta? ¿Varía mucho?
5. ¿Cómo deciden hoy cuándo lanzar una carga del horno? ¿Esperan a llenarlo o corren con lo que hay?
6. ¿Qué importan hoy, a quién, con qué plazo, costo puesto en planta y mínimo de compra?
7. ¿Qué nivel de servicio consideran aceptable? ¿Registran ventas perdidas o pedidos pendientes?

## Restricciones del TPI que aplican a este caso

Ver sección TPI de `../../../SIM.md`. Resumen: AnyLogic (Process Modeling Library), informe LaTeX con los 10 pasos, escenario base + ≥1 alternativo, corridas múltiples + test de medias, video de 3 min. No hay optimización ni flujo de caja: se comparan escenarios.
