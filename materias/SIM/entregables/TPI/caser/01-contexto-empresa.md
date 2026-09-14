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
- Horno propio de cementación y temple, **reactivado en 01/2026**.
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

## Pendiente de relevar

- Qué artículos son hoy stock / contra pedido / importados, y por qué.
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
