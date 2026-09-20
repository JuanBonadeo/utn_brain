# TPI Simulación — Propuesta de tema

> **Versión 2 (2026-09-20)** — reemplaza la propuesta del 31/07. El docente confirmó el tema del subte
> por mail el 2026-09-20 ("Vamos con lo del subte… Completen el formulario con este tema. Editen su
> último envío.") y pidió llegar al miércoles 23/09 con el caso definido.
> El respaldo completo, con el perfilado del dataset, está en
> [`subte/01-definicion-del-caso.md`](subte/01-definicion-del-caso.md).
> Versión entregable en Word: [`TPI_Simulacion_Propuesta_de_Tema.docx`](TPI_Simulacion_Propuesta_de_Tema.docx)
> — **pendiente de regenerar con este contenido.**

---

## Datos del grupo

| Integrante | Legajo |
|---|---|
| Juan Cruz Bonadeo | 53533 |
| Matias Estevez | 53528 |

Comisión 401 — Facultad Regional Rosario.

---

## Tema

> Simulación de la línea de molinetes del vestíbulo principal de la estación Constitución de la Línea C
> del subte de Buenos Aires durante el pico de la mañana de los días hábiles, para evaluar el efecto de
> la cantidad de molinetes habilitados y de la velocidad de validación sobre el tiempo de espera de los
> pasajeros que llegan en tandas desde la terminal ferroviaria Roca.

## Observaciones

> Elegimos este caso porque es el punto del sistema donde el fenómeno de cola es más nítido y porque los
> datos de entrada son públicos y de granularidad fina. El Gobierno de la Ciudad publica, para cada
> molinete individual y cada ventana de 15 minutos, la cantidad de pasajeros que lo atravesaron; sobre la
> serie de enero a junio de 2026 verificamos que las catorce ventanas de quince minutos más cargadas de
> todo el subte corresponden a Constitución, que en el pico de 08:15 a 08:45 el vestíbulo principal recibe
> unos 2.066 pasajeros cada cuarto de hora con alrededor de veinte molinetes activos sobre veintiocho
> instalados, y que la franja de 07:00 a 09:30 concentra 17.482 pasajeros por día hábil. Lo que hace que
> el caso justifique simulación, y no una fórmula de colas, es que a esa intensidad cada molinete recibe
> un pasajero cada ocho segundos y medio contra un tiempo de validación del orden de dos a tres segundos:
> en promedio el sistema está lejos de saturarse y un modelo analítico concluiría que no hay cola, cuando
> en la práctica sí la hay. La cola se forma porque Constitución es la terminal del Ferrocarril Roca y los
> pasajeros no llegan de a uno sino en tandas, cada vez que arriba una formación. Es un caso de congestión
> transitoria por arribos en lote sobre un sistema subutilizado en promedio, que es exactamente donde la
> simulación de eventos discretos aporta lo que el cálculo no da. La hipótesis de mejora es concreta y de
> costo bajo: habilitar los molinetes instalados que hoy permanecen cerrados en la franja pico, redistribuir
> el flujo hacia el segundo vestíbulo de la estación, que absorbe solo el quince por ciento del total, o
> acelerar la validación con pago contactless, que la estación ya tiene instalado en un molinete y por lo
> tanto es medible y no un supuesto.

---

## Anexo — respaldo técnico

### Definición del caso, según lo pedido el 2026-09-20

| Qué pidió el docente | Respuesta |
|---|---|
| Qué línea en específico | **Línea C**, estación **Constitución**, **vestíbulo Principal** (84,7 % del flujo de la estación) |
| Qué horarios o franjas | **07:00 – 09:30**, con pico en **08:15 – 08:45** |
| Qué días | **Días hábiles**, excluyendo 11 feriados que el propio dato identifica |
| Medidas de rendimiento | Espera en cola (media y **percentil 90**), **proporción de pasajeros con espera > 30 s**, **tiempo de disipación de la tanda**; como secundarias Lq, utilización por molinete y throughput |

### Verificación de los criterios de selección del enunciado (§5)

| Criterio | Cómo lo cumple |
|---|---|
| **1. Aleatoriedad relevante** | Arribos en tandas de tamaño e intervalo aleatorios y tiempo de validación variable. El CV del flujo entre días en la ventana pico es 0,24 |
| **2. Datos disponibles** | ✅ Verificado: serie 2013-2026 por molinete individual cada 15 min. Perfilados 117 días hábiles de 2026 |
| **3. Hipótesis de mejora** | Molinetes habilitados (E1), redistribución entre vestíbulos (E2), validación contactless (E3) |
| **4. Alcance acotable** | Una estación, un vestíbulo, una franja de dos horas y media |

### Escenarios

- **E0** — base: ~19,5 molinetes activos de 28, con la distribución de carga observada.
- **E1** — abrir los 28 molinetes instalados durante la franja pico.
- **E2** — redistribuir flujo hacia el vestíbulo Plaza, hoy con el 15 % del total.
- **E3** — validación contactless EMV/QR: cambia el tiempo de servicio, no la cantidad de servidores.

### Estado de los datos

| Dataset | Origen | Estado |
|---|---|---|
| Subte — Viajes Molinetes 2026 (ene-jun), por molinete y 15 min | [BA Data](https://data.buenosaires.gob.ar/dataset/subte-viajes-molinetes) | ✅ Descargado y perfilado (45 MB zip → 548 MB CSV) |
| Series 2013-2025 | mismo dataset | Disponibles para ampliar el horizonte |
| **Tiempo de servicio del molinete** | no existe en ningún dataset | ⏳ **Medición en campo pendiente** |
| **Estructura de las tandas** | el agregado de 15 min la borra | ⏳ **Medición en campo pendiente** |

Reproducible con [`scripts/sbase-perfil.py`](../../../../scripts/sbase-perfil.py). Los CSV no se commitean.

### Limitaciones a declarar en el informe

- Los molinetes registran a quien **pasó**, no a quien **esperó**: la cola es salida del modelo y no puede
  validarse contra el dataset. Se resuelve midiendo el largo de cola en campo.
- Posible **censura por capacidad** en el pico: si los molinetes saturan, el conteo mide el caudal máximo
  del molinete y no la demanda real.
- El campo de hora **cambia de formato según el mes** (marzo y abril de 2026 usan `HH:MM`, el resto
  `HH:MM:SS`). Agregar sin normalizar parte cada hora en dos, en silencio.
- Molinetes con registro casi nulo en seis meses (`Turn07`, 3 pasajeros) — fuera de servicio o mal
  identificados. Se excluyen.

### Historial de la propuesta

La versión del 31/07 presentaba dos temas: **Ecobici** (rebalanceo en el corredor Constitución/Retiro–
Catalinas) y **despacho de emergencias de San Francisco**. Ecobici quedó descartado porque otro grupo lo
tomó primero. El tema de molinetes de subte figuraba en esa versión como candidato de reserva y es el que
el docente aprobó el 2026-09-20.
