# TPI Simulación — Propuesta de tema (grupo Casermeiro)

> Primera actividad del TP Integrador. Ver [SIM.md](../../../SIM.md) §3.
> Formato tomado del enunciado (integrantes + tres temas candidatos, cada uno con "Tema" y "Observaciones").
> Gonzalo cursa en otra comisión: el formato exacto puede variar, pero sirve para presentarle la propuesta al docente.
> La prioridad se asigna **por fecha de entrega**: conviene mandarlo temprano.
> **No arrancar el modelado antes de la confirmación del docente.**

---

## Datos del grupo

| Integrante | Legajo |
|---|---|
| Gonzalo Casermeiro | *(completar)* |
| *(completar si hay más integrantes)* | |

Comisión: *(completar)*

---

## Tema 1 — Régimen de campañas del horno de tratamiento térmico (opción prioritaria)

**Tema:**

> Simulación de la cadena interna de producción y abastecimiento de stock de una PyME metalúrgica fabricante
> de elementos de fijación, para evaluar el efecto de la regla de lanzamiento de campañas del horno de
> cementación y temple sobre el nivel de servicio, el tiempo de entrega, el capital inmovilizado en inventario
> y el costo energético por kilogramo tratado.

**Observaciones:**

> Elegimos este tema porque el horno es un proceso por lotes con un costo de preparación desproporcionado
> respecto del tiempo productivo, y porque la decisión de cuándo encenderlo se toma hoy por criterio del
> encargado, sin ningún respaldo cuantitativo. El horno requiere aproximadamente 36 horas de calentamiento y
> 48 horas de enfriamiento, y se enciende recién cuando se acumulan unas 70 a 80 unidades de transporte
> interno, que se procesan a razón de 15 por turno a lo largo de una campaña de aproximadamente una semana:
> eso da del orden de 84 horas de preparación por unas 40 horas de proceso efectivo. Como la planta está
> operando muy por debajo de su capacidad instalada, el tiempo que tarda en acumularse el lote que justifica
> el encendido puede extenderse varias semanas, durante las cuales el material queda inmovilizado antes del
> tratamiento y los pedidos no pueden comprometerse con un plazo firme. El sistema es por lo tanto una cola
> con servidor por lotes y preparación fija, con aleatoriedad relevante en los arribos, y se implementa
> íntegramente con la Process Modeling Library. El caso es real, es una empresa en concurso preventivo donde
> cada decisión sobre capital y energía es crítica, y tenemos acceso directo al sistema de gestión y a los
> registros de proceso, que son obligatorios por la certificación ISO 9001:2015 vigente.

---

## Tema 2 — Fabricar, comprar o importar, artículo por artículo

**Tema:**

> Simulación de la política de abastecimiento de productos terminados de una PyME metalúrgica, para evaluar
> para qué artículos conviene la fabricación propia, la compra a un proveedor nacional o la importación
> directa, considerando que la importación tiene menor costo unitario pero exige lote mínimo grande, plazo de
> reposición largo y variable, y capital adelantado.

**Observaciones:**

> Es la decisión estratégica que la empresa ya está tomando bajo presión y hoy resuelve por intuición: ante el
> costo de fabricar, algunos artículos pasaron a importarse. El modelo pone números sobre lo que el costo
> unitario no muestra, que es el inventario que genera un contenedor completo y el riesgo de quedarse sin
> producto durante el plazo de reposición. Se modela como un sistema de inventario con dos ramas de reposición
> con distribuciones de plazo muy distintas, comparando el mix actual contra alternativas de mayor o menor
> integración vertical. El sistema de gestión permite exportar el historial de compras con fecha de pedido y
> fecha de recepción, lo que permite ajustar la distribución del plazo con datos reales; si la cantidad de
> operaciones de importación registradas resultara insuficiente para ajustar una distribución, se estimaría a
> partir de cotizaciones y se declararía explícitamente como supuesto, con análisis de sensibilidad.

---

## Tema 3 — Política de abastecimiento de materia prima

**Tema:**

> Simulación del abastecimiento de alambre de acero de una PyME metalúrgica, para evaluar qué combinación de
> proveedor, punto de pedido y tamaño de lote minimiza el costo total de abastecimiento sin provocar
> detenciones de producción por falta de materia prima.

**Observaciones:**

> La empresa se abastece de tres proveedores con perfiles claramente distintos: uno entrega en
> aproximadamente 30 días con financiación, otro en un plazo similar pero exigiendo anticipo parcial, y un
> tercero en 15 días con pago anticipado y percepciones impositivas que agregan alrededor de un 11% de
> exigencia financiera inmediata. La elección entre ellos no es trivial porque el más barato por kilogramo no
> es el más rápido ni el que menos capital adelanta. El sistema de gestión registra fecha de pedido y fecha de
> recepción de cada compra, de modo que el plazo real de cada proveedor es una variable medible sobre datos
> históricos y no una estimación. El estudio se plantea explícitamente como un problema de inventario y plazo
> de reposición, no como un análisis financiero.

---

## Anexo — respaldo técnico

### Verificación de los criterios de selección del enunciado

| Criterio | Tema 1 — Horno | Tema 2 — Fabricar/comprar/importar | Tema 3 — Materia prima |
|---|---|---|---|
| **1. Aleatoriedad relevante** | Arribos al horno, demanda, plazo del zincado tercerizado | Demanda, plazo de importación (alta varianza) | Consumo de alambre, plazo de entrega por proveedor |
| **2. Datos disponibles** | Registros ISO del horno + exportación del sistema de gestión | Exportación de ventas, compras y maestro de artículos | Exportación de compras con fechas de pedido y recepción |
| **3. Hipótesis de mejora** | Regla umbral + tiempo máximo de espera vs. umbral solo | Cambiar el mix fabricado/comprado/importado | Cambiar proveedor, punto de pedido y lote |
| **4. Alcance acotable** | 3-5 familias, 10-30 artículos, horizonte 12 meses | Mismo subconjunto de artículos | Las calidades y diámetros de mayor consumo |
| **Originalidad / aplicabilidad** | Alta — proceso por campañas poco frecuente en TPs; decisión semanal real | Alta — decisión estratégica en curso | Media-alta |

### Estado de los datos

| Fuente | Contenido | Estado |
|---|---|---|
| Sistema de gestión (servidor local) | Ventas, maestro de artículos, órdenes de fabricación, compras, stock valorizado, clientes y proveedores | Exportable a planilla de cálculo. Confirmado por la empresa |
| Registros de proceso ISO 9001:2015 | Órdenes de fabricación, cargas de horno, rechazos, trazabilidad | Existen por requisito de la norma. Pendiente de relevamiento |
| Facturación de energía | Consumo con y sin campaña, potencia contratada, tarifa | Pendiente de relevamiento |
| Presupuestos y notas de venta canceladas | Demanda no atendida | **Pendiente de confirmar** si el sistema las conserva y exporta |

### Alcance propuesto para el Tema 1

- 3 a 5 familias de productos, 10 a 30 artículos representativos, incluyendo artículos de alta rotación,
  de alto margen, especiales, y artículos que atraviesan y que no atraviesan el horno.
- Horizonte simulado: 12 meses. Historia para el ajuste de distribuciones: 24 meses.
- Escenario base (regla actual) más dos o tres escenarios alternativos de regla de lanzamiento.
- 30 réplicas por escenario y test de medias sobre las medidas de salida.
- Análisis de sensibilidad sobre el nivel de demanda (−20%, actual, +20%).

### Medidas de salida

Nivel de servicio (proporción de pedidos servidos completos y a tiempo), tiempo de entrega, inventario
promedio valorizado, material en espera antes del horno, campañas por mes, ocupación promedio por campaña,
costo energético incremental por kilogramo tratado.

### Validación prevista

Contra la operación histórica: la cantidad de campañas por mes, las toneladas procesadas por campaña y los
tiempos de entrega que devuelva el modelo deben ser consistentes con el registro real de cargas del horno y
con las fechas de inicio y fin de las órdenes de fabricación.

### Supuestos a declarar en el informe

- La empresa se presenta con **nombre ficticio** y los montos en números índice.
- Demanda estacionaria dentro del horizonte simulado, o estacionalidad simple si los datos la muestran.
- Un solo turno de trabajo, salvo durante las campañas del horno.
- Capacidad agregada por familia de producto, no máquina por máquina.
- Zincado tercerizado modelado como un retardo aleatorio; no se modela al tercero por dentro.
- El costo de la potencia eléctrica contratada es un costo fijo hundido para la decisión de corto plazo: la
  comparación entre escenarios se hace sobre el **consumo incremental** de encender y operar el horno.
- El histórico de ventas refleja **demanda atendida**, no demanda real de mercado. La venta perdida por
  falta de disponibilidad es una salida del modelo, no una entrada, salvo que se confirme que el sistema
  conserva los presupuestos no concretados y las notas de venta canceladas.

### Fuera del alcance

Flujo de caja, punto de equilibrio y tiempo de supervivencia de la empresa: exceden el objeto de un estudio
de simulación y dependen de datos financieros que no están relevados. Las salidas del modelo —compras,
inventario, campañas y ventas por período— quedan disponibles para alimentar una proyección de caja externa,
que se menciona como trabajo futuro. Tampoco se aborda el dimensionamiento de la dotación ni la reinstalación
de la línea de cincado propia.
