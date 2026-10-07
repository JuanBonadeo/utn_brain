# TPI Simulación — Respuestas al docente sobre el Tema 1 (horno)

> Respuesta a las cinco preguntas recibidas el 2026-09-16 sobre la propuesta
> [`04-formulario-eleccion-tema.md`](04-formulario-eleccion-tema.md), Tema 1.
> Van en el mismo orden. Lo marcado **[confirmar]** depende de un dato que la empresa tiene pero
> todavía no exportamos, o de una pregunta puntual al encargado; se cierra antes de empezar a modelar.
> La última sección son notas internas que **no** van al docente.

---

## 1. Cómo se modela el horno en AnyLogic

### 1.1 Qué es el horno físicamente, y por qué no es `Batch` → `Delay`

El horno no trata las 70-80 ULI juntas. Es un horno eléctrico de 27 resistencias que, una vez a
temperatura, procesa las ULI **de a una**, a razón de unas 17 por día en 3 turnos de 8 h (≈ 85 min por ULI). Lo
que lo convierte en un sistema "por lotes" no es la capacidad sino el **costo de arranque**: 36 h de
calentamiento antes de la primera ULI y 48 h de enfriamiento después de la última, durante las cuales
no está disponible. En vocabulario de colas es un servidor con **tiempo de preparación y política de
encendido por umbral** (se enciende cuando se acumulan N clientes), no un servidor batch de capacidad N.

Por eso el bloque `Batch` no representa al horno. Agrupar 75 ULI en un lote y pasarlas por un `Delay`
de 40 h perdería justamente lo que se quiere medir: la espera individual de cada ULI (la primera en
llegar espera semanas; la última, horas), la incorporación a la campaña de las ULI que llegan mientras
el horno está caliente, y el consumo de energía por estado (calentar, mantener, enfriar). La ULI
circula como agente individual; la campaña es un **estado del horno**, no una entidad.

### 1.2 Bloques

Flujo de las ULI (Process Modeling Library):

```
ULI lavada ─► colaHorno   Wait, capacidad ilimitada; la espera se mide de la entrada al despacho.
                          (El lavado es previo al horno: en el 99 % de las ULI del seguimiento es
                          del mismo día o anterior al cementado. Es parte de "aguas arriba", §1.5.)
                          Implementado (07/10/2026) como bloque Wait: la ULI sale solo cuando
                          despachar() la libera con free(), así el horno elige cuál carga
                          (urgentes primero, después FIFO) y solo en Procesando.
          ─► horno        Delay, minPorULI = 1440 / 17 ≈ 85 min, capacidad 1. Reemplaza al
                          Hold + Seize/Release del diseño original: con un solo horno y operación
                          24 h, el recurso no agrega nada que no haga la capacidad 1 del Delay.
                          Regla de fin de campaña confirmada el 07/10/2026: el horno carga
                          mientras haya cola (work-conserving); el Hold con cupo por campaña de la
                          regla del 27/09 quedó como modo alternativo (modoFinCampana = cupo).
          ─► revenido     Delay con distribución empírica, solo si el artículo lo lleva (§1.5).
          ─► zincado (Delay, plazo aleatorio del tercero) ─► envasado (Delay)
          ─► entrega      Sink. TimeMeasureEnd pedido → entrega: tiempo de entrega y nivel de servicio.
                          No hay ingreso a stock: la producción es contra pedido (§1.5).
```

Si el registro de cargas muestra que el horno aloja varias ULI a la vez (horno continuo de empuje), el
`Delay` pasa a capacidad k con tiempo k × 85 min: mismo caudal, distinta residencia. Se decide con el
registro, no cambia nada más.

Control del horno: un **statechart** en `Main`, con una variable acumuladora de kWh.

| Estado | Cómo se entra | Cómo se sale | Potencia imputada |
|---|---|---|---|
| `Apagado` | inicio del modelo; fin del enfriamiento | hay ULI en cola → `Acumulando` (inmediato) | 0 |
| `Acumulando` | primera ULI en cola | por **condición** `colaHorno.size() >= umbralULI`, o por **timeout** de espera máxima cuando la regla lo tiene → `Calentando` | 0 |
| `Calentando` | regla cumplida | **timeout** `hCalentamiento` = 36 h → `Procesando` | P_cal |
| `Procesando` (subestados `Cargando` / `CalienteEnVacio`) | fin del calentamiento | `Cargando` mientras haya ULI en cola; con la cola vacía pasa a `CalienteEnVacio`, y de ahí **timeout** `horasEnVacio` → `Enfriando`, salvo que llegue una ULI (vuelve a `Cargando`). `horasEnVacio` = 48 h (07/10/2026: el registro muestra huecos de 1-2 días sin carga dentro de campañas). Un encendido por prioridad trata solo las urgentes y enfría sin espera | P_mant |
| `Enfriando` | fin de la campaña | **timeout** `hEnfriamiento` = 48 h → `Apagado` | 0 |

**Confirmado con el encargado (2026-09-27) — corrige el supuesto original**: las ULI que llegan mientras el
horno está prendido **no** se suman a la campaña en curso por defecto — se guardan para la próxima. Y
`horasEnVacio` **no** es "hasta el fin del turno": la regla es apagar apenas la cola queda vacía, salvo una
excepción puntual por **prioridad**: si se sabe que en el corto plazo va a entrar un producto que hay que
tratar y que tiene una entrega comprometida que no puede esperar a la próxima campaña, ahí sí se mantiene
caliente para esperarlo (confirmado también que adelantan el encendido por el mismo motivo). En el modelo:
`horasEnVacio` pasa a ser corto por default (a ajustar con el registro — puede ser casi 0) y solo se
extiende cuando una ULI marcada `prioridad=true` (producto con entrega comprometida, conocido de antemano
por una OF o un pedido) está en camino; esa marca también dispara el adelanto de `Acumulando → Calentando`
antes de llegar al umbral. El escenario E3 ("mantener caliente") pasa a ser esto, no un buffer de tiempo
fijo.
Si la regla se cumple durante `Enfriando`, en el modelo base se espera el fin del enfriamiento y se
recalienta con las 36 h completas (supuesto conservador: a lo sumo 48 h de demora extra); el
recalentamiento parcial desde tibio queda como sensibilidad.

Registro por campaña (acción al salir de `Procesando`): ULI tratadas, kg, kWh, instantes de encendido
y apagado, espera de la ULI más vieja. Va a un `Dataset` y a una tabla de la base de datos interna del
modelo; es lo que se compara con el registro ISO de cargas (§4).

### 1.3 Dónde queda cada número

| Dato relevado | En el modelo |
|---|---|
| 36 h de calentamiento | timeout de `Calentando → Procesando` (parámetro `hCalentamiento`) |
| 48 h de enfriamiento | timeout de `Enfriando → Apagado` (parámetro `hEnfriamiento`) |
| ~17 ULI/día (corrige "15 por turno") | **Confirmado (2026-09-27)**: son **3 turnos de 8 h** cubriendo las 24 h, no un turno por día. `Delay` de 1440/17 ≈ 85 min con capacidad 1 (el registro `Termico 2026` da mediana 18 ULI/día y media 16 en los días intermedios de campaña), `operadorHorno` con `Schedule` de 3 turnos continuos durante `Procesando` |
| Umbral de 70-80 ULI | parámetro `umbralULI = 75`; 70 y 80 como sensibilidad |
| Campaña de ~1 semana | **no es un parámetro, es una salida**: 75 ULI / 17 por día ≈ 4,4 días de carga + 36 h + 48 h ≈ 7,9 días. Que el modelo devuelva ~1 semana es una verificación |
| 84 h de preparación por 40 h de proceso | idem: emerge de los tres puntos anteriores |
| 27 resistencias | potencia nominal instalada; acota P_cal y P_mant (§2.3) |

### 1.4 Qué dispara el encendido

Por **evento**, no por reloj ni por revisión periódica:

- El umbral solo puede pasar a cumplirse cuando entra una ULI a la cola. AnyLogic reevalúa las
  transiciones y eventos disparados por condición cada vez que ocurre algo en el agente (otro evento,
  una transición, un cambio de parámetro), y la entrada a `colaHorno` es un evento de `Main`, así que
  la transición por condición `colaHorno.size() >= umbralULI` se dispara en el instante exacto de la
  llegada que completa el umbral. No hay polling.
- La espera máxima, cuando la regla la tiene, es un **timeout** del estado `Acumulando`, calculado al
  entrar como `esperaMax − (time() − tPrimeraULI)`, de modo que vale también si la primera ULI llegó
  durante el enfriamiento. Si el umbral se cumple antes, salir del estado cancela el timeout solo.
  No se usa una condición sobre `time()` porque AnyLogic no reevalúa condiciones en función del reloj,
  solo después de eventos: para eso está el timeout.
- La única regla "programada" es el turno del operador (`Schedule`), que fija cuándo se cargan ULI.

Alternativa equivalente sin statechart: variable `estadoHorno` más `Event` de tipo *Condition* para el
umbral (reactivado con `restart()` tras cada disparo, porque un evento por condición se desactiva al
ejecutarse) y `Event` de tipo *Timeout* para calentamiento, enfriamiento y espera máxima. Preferimos el
statechart porque los estados quedan visibles en la animación y en el video.

### 1.5 El resto del modelo

El horno es el núcleo, pero el nivel de servicio y el capital inmovilizado exigen modelar de dónde
vienen las ULI y adónde va lo tratado. Tres subsistemas, deliberadamente agregados:

- **Demanda y producción contra pedido**, por artículo (10-30 artículos cargados desde una tabla de la
  base de datos interna de AnyLogic, importada del ABM): `Source pedidos` con tiempo entre pedidos
  ajustado y artículo/cantidad sorteados de la distribución empírica → cada pedido dispara directo una OF
  (`inject` en `Source OF`), sin pasar por un chequeo de stock. La empresa confirmó (2026-09-25) que no
  maneja stock de seguridad reglado: por decantación, es todo contra pedido, salvo excepciones puntuales
  todavía sin identificar — así que se cae la política (s, Q) que se iba a reconstruir de las OF, y con ella
  la rama `SelectOutput`/`Queue pendientes` del diseño original. `TimeMeasureStart/End` del pedido a la
  entrega mide el tiempo de entrega, que ahora es directamente el lead time de producción de punta a punta
  (aguas arriba + horno + aguas abajo): es la variable que explica el fill rate bajo medido en §2.1 (49-51%
  histórico) mejor que un modelo con stock intermedio. **Pendiente**: si alguno de los artículos
  representativos elegidos resulta ser una de las excepciones con stock, se le agrega el chequeo puntual
  para ese artículo — no para todos.
- **Aguas arriba** (estampado + laminado + lavado, agregado por familia): `Delay` con tiempo = preparación +
  cantidad / tasa, ajustado de las OF históricas y de los tiempos entre etapas del seguimiento (§2.1) →
  `Split` en ⌈cantidad / piezas por ULI⌉ ULI → `colaHorno`, o directo a zincado vía `SelectOutput` si el
  artículo no lleva tratamiento térmico.
- **Aguas abajo**: revenido donde aplica, zincado tercerizado (`Delay` con plazo ajustado de los remitos),
  envasado y entrega.

No incluye **revenido**: es un tratamiento posterior a la cementación, en un horno distinto ("POTE", de
mucha menor potencia que el de cementación) y que no se aplica a todo el catálogo — lo llevan el 15 % de
las ULI del seguimiento 2023-2026, concentradas en 24 artículos de CASER-Drill. Agregarlo exigiría un
segundo régimen de campaña (otro umbral, otro statechart) para una fracción del flujo, y el estudio varía
la regla del horno de cementación, no la del de revenido. Los artículos con revenido **sí** entran en la
selección (son el 22 % del volumen y los peor servidos); para ellos el revenido se suma como una demora
aleatoria con la distribución empírica (mediana 5 días, media 11,7, p90 31), no como un servidor con cola
propia. Limitación declarada: si la regla de cementación cambiara el ritmo de llegada de ULI al revenido,
esa demora no se adaptaría.

Las entidades son el **pedido** y la **ULI**, nunca la pieza: no aporta al análisis y la edición PLE
limita a 50.000 agentes creados por corrida.

### 1.6 Construcción en dos etapas

1. **Etapa 1 — horno con arribos exógenos.** Las ULI llegan a `colaHorno` con tiempo entre arribos
   ajustado del registro de OF y cargas. Responde campañas por mes, espera pre-horno, ocupación por
   campaña y kWh por kg, y es lo primero que se valida contra el registro ISO.
2. **Etapa 2 — arribos endógenos.** Se acopla demanda, política de stock y aguas arriba/abajo. Agrega
   tiempo de entrega, nivel de servicio y capital inmovilizado.

La Etapa 1 es un entregable completo por sí sola (escenarios, réplicas, test de medias). Si el tiempo
aprieta, la Etapa 2 se recorta en cantidad de artículos, no en rigor. Es el "empezar simple y crecer"
del paso 2 de Law.

---

## 2. Datos

### 2.1 Qué hay y para qué sirve

Todo lo que sigue existe y está confirmado por la empresa; el sistema de gestión (servidor local)
exporta a planilla sin restricción. Lo que falta es ejecutar la exportación.

| Entrada del modelo | Fuente | Cómo se obtiene |
|---|---|---|
| Tiempo entre pedidos y tamaño de pedido, por artículo | ✅ Resuelto (2026-09-25): facturas de venta transaccionales, 12 meses, validadas contra la estadística mensual | Ajuste por artículo o familia (tiempo entre pedidos: exponencial / gamma; tamaño: empírica discreta) |
| Demanda no atendida histórica | ✅ Resuelto (2026-09-24): reportes "Artículos Presupuestados/facturados" del ABM, por cliente y por artículo, 12 meses | Fill rate histórico global 49-51%, con 20% de artículos en entrega cero. Válido para validar nivel de servicio (§4.1), no distingue motivo de la pérdida |
| Política de reposición | — | **No aplica**: confirmado que es todo contra pedido (sin (s, Q) reglado), salvo excepciones puntuales a identificar entre los artículos elegidos |
| Tiempo aguas arriba (estampado + laminado + lavado) | Resuelto (07/10/2026): `Seguimiento TR ulis`, 12.527 ULI con fecha de inicio de cada etapa (2023-2026) | Medido por tramo, en días (mediana / media / p90): Prensa→Laminado 3 / 8,2 / 20; Laminado→Lavado 2 / 5,0 / 8. Ajuste por familia o empírica. Las cantidades por lote salen de las OF |
| Tiempo entre arribos de ULI al horno (Etapa 1) | ISO: registro de cargas + OF | Ajuste sobre las fechas en que cada ULI quedó lista |
| Tiempo de ciclo por ULI | ISO: registro de cargas | Determinístico (≈ 85 min = 24 h / 17), salvo que el registro muestre diferencias por familia |
| Kg por ULI, por artículo | `Seguimiento TR ulis` ("Cant. x U.L.I." × "P. Pieza") | ✅ Resuelto (2026-09-28): ambas columnas están en **millares** ("Cant. x U.L.I." = cantidad de millares, "P. Pieza" = kg por millar), no en piezas sueltas — corregido tras confirmación de la empresa. kg/ULI = Cant. x U.L.I. × P. Pieza directo, sin dividir por mil. Sobre 310 artículos: media 143 kg/ULI, mediana 136, rango 5,9-362,5. **Corregido (07/10/2026)**: la cuenta anterior asumía 75 ULI por campaña (≈10 t), pero las campañas reales tratan una mediana de 114 ULI. Medido mes a mes: **31 t/mes en 2024-2025 y 20 t/mes en 2026** (máximo 65,5 t en mayo/2025), contra los "60-90 t/mes" de capacidad instalada del brief: 42 % y 26 % de utilización (sobre 75 t), consistente con "planta subutilizada" |
| Plazo del zincado tercerizado | Resuelto (07/10/2026): `Seguimiento TR ulis` (Enviado→Recibido, 12.325 ULI) | Mediana 2 días, media 3,0, p90 6. Demora previa al envío (Cementado→Enviado, sin revenido): mediana 5, media 12,3, p90 28. Ajuste (lognormal / gamma) o empírica |
| P_cal y P_mant (potencia media calentando y a temperatura) | Resuelto en parte (05/10/2026). El medidor "Horno" fue **exclusivo del horno** hasta abril/2026 (confirmado por la empresa); con 28 meses de sus facturas contra días con cementado (`Seguimiento TR ulis`): kWh = 2.013 + 1.384 × campañas + 2.445 × días activos, R² = 0,89. **P_mant ≈ 102 kW** (2.445 ± 179 kWh/día), ≈70 % de los 145 kW instalados. El término por encendido (1.384 ± 1.288 kWh) es impreciso, pero queda ~3 errores estándar por debajo del techo teórico de 145 kW × 36 h = 5.220 kWh: **caso base = la estimación empírica, sensibilidad de 0 a 5.220 kWh**. No hay un antes/después limpio por reactivación — el horno operó intermitente todo el período | §2.3 |
| Costo estándar y precio por artículo | Lista de precios de la empresa (Lista CASER) | Directo, en números índice. `PrecioPorPieza` ya calculado y comparable entre artículos |
| Campañas por mes, ULI y kg por campaña, duración, espera | ISO: registro de cargas desde 01/2026 | **No son entradas**: se reservan para la validación (§4) |
| Tasa de costo del capital inmovilizado | Empresa (quien maneje finanzas, no el encargado de producción) | Parámetro, con sensibilidad. Pregunta sugerida: "si tuvieran esa plata en la cuenta en vez de en producto en proceso, ¿qué tasa mensual le pondrían a tenerla inmovilizada?" — alcanza una estimación gruesa |

Formato del registro ISO de cargas **[confirmar: planilla o papel]**; si es papel se transcribe (del
orden de 10 campañas × 75 ULI).

### 2.2 Cómo se ajustan las distribuciones

El mismo procedimiento para cada entrada, documentado en el informe (paso 2):

1. Depuración: unidades, duplicados, valores imposibles y período. Si el arranque del horno
   (01-02/2026) muestra un transitorio de puesta a punto, se excluye del ajuste y de la validación.
2. Estacionariedad: medias por mes. Si la demanda tiene tendencia clara, se ajusta sobre los últimos
   12 meses y el resto se usa para sensibilidad.
3. Histograma y candidatas según la naturaleza de la variable: tiempos → exponencial, gamma,
   lognormal, Weibull; cantidades → empírica discreta.
4. Estimación de parámetros por máxima verosimilitud.
5. Bondad de ajuste: chi-cuadrado y Kolmogorov-Smirnov, con nivel de significación y p-valor en el
   informe.
6. Si ninguna teórica ajusta, distribución empírica (`CustomDistribution` de AnyLogic).
7. Tabla final por variable: n, distribución, parámetros, test, p-valor.

Herramienta: Python (scipy.stats); AnyLogic 8 PLE no incluye ajuste de distribuciones. Referencia:
Law, *Simulation Modeling and Analysis*, cap. 6.

### 2.3 Energía

El consumo no es una variable aleatoria de entrada: es una función determinística del estado del
horno. Lo que se estima son dos potencias medias, P_cal (durante las 36 h de calentamiento) y P_mant
(a temperatura, durante el procesamiento), por tres vías que se cruzan:

- **Facturas** (hecho, 05/10/2026): el medidor del horno fue exclusivo hasta abril/2026, así que no hace
  falta un año de control sin horno ni restar una base. Regresión sobre 28 meses (ene/2024-abr/2026),
  `kWh_mes = a + b · campañas_mes + c · días_activos_mes`, con las campañas y días tomados de las fechas de
  cementado de `Seguimiento TR ulis`: a = 2.013, b = 1.384 ± 1.288 kWh por encendido, c = 2.445 ± 179 kWh
  por día activo (≈102 kW), R² = 0,89. Se usó días activos y no ULI como regresor porque explica más
  (R² = 0,89 contra 0,73 con ULI cementadas): el horno consume por estar caliente, no por la cantidad que
  trata. c da P_mant; b es impreciso (no se distingue de cero) pero queda ~3 errores estándar por debajo del
  techo teórico de 5.220 kWh, así que el caso base usa la estimación empírica y la sensibilidad (§2.4)
  barre de 0 a 5.220 kWh.
- **Potencia nominal**: 27 resistencias × potencia unitaria acota P_cal por arriba y da el factor de
  uso.
- **Registro ISO**: si anota lectura de medidor o consumo por campaña, es medición directa y reemplaza
  a la regresión **[confirmar]**.

Si la tarifa penaliza el exceso de potencia y una campaña lo dispara, se agrega como costo fijo por
campaña. La potencia contratada no entra: es costo hundido para esta decisión.

**Gas y desgaste.** El horno es de cinta continua con generador de gases endotérmicos para la atmósfera de
cementación, y cada encendido desgasta resistencias, cinta y mufla. Ninguno de los dos cambia la lógica del
modelo: ambos entran en los dos coeficientes que ya existen, **costo fijo por encendido** (energía de
calentamiento + gas de arranque + desgaste por ciclo, este último estimado del registro de mantenimiento
dividido por la cantidad de encendidos) y **costo por hora caliente** (energía + gas de régimen). El gas se
estima con la misma regresión que la electricidad sobre sus facturas. Si algún término no se consigue, se
excluye, se declara, y se hace sensibilidad (desgaste = 0 %, 25 % y 50 % del costo energético de arranque);
como los dos empujan el costo fijo hacia arriba, el umbral óptimo real es al menos el que dé el modelo sin
ellos.

### 2.4 Lo que falta o es débil, y qué se hace

| Dato débil | Supuesto declarado | Sensibilidad |
|---|---|---|
| Separación P_cal / P_mant si las facturas solo dan totales mensuales | Coeficientes b y c de la regresión | ±30 % en cada uno |
| Recalentamiento desde tibio | 36 h completas (conservador) | Calentamiento proporcional al enfriamiento transcurrido |
| Estacionariedad de la demanda | Estacionaria en el horizonte | Factor de demanda 0,8 / 1,0 / 1,2 |
| Tasa de costo del capital | Valor dado por la empresa | Tres niveles |
| Plazo de zincado si hay pocos remitos (< 20) | Triangular con mínimo, moda y máximo del encargado (recomendación de Law cuando solo hay estimación de expertos) | ±20 % en la moda |
| Tiempo de ciclo por ULI | ≈ 85 min determinístico | ±20 % |

Método: un factor por vez alrededor del caso base, 30 réplicas, intervalo de confianza apareado de la
diferencia contra la base. Un factor es crítico si mueve la medida primaria más que la semi-amplitud
del intervalo; los críticos se reportan con su rango de validez (paso 6 de Law).

---

## 3. Regla actual, alternativas y medidas de salida

### 3.1 Regla actual

Relevada con la empresa: el horno se enciende cuando se acumulan **unas 70-80 ULI**. No hay tiempo
máximo de espera formal ni regla escrita; la decisión es del encargado **[confirmar en la entrevista
si adelanta el encendido por pedidos comprometidos; si lo hace, se modela como prioridad de la ULI,
no como cambio de regla]** — **confirmado (2026-09-27)**: sí lo hace. En el modelo (07/10/2026):
`umbralULI = 75`, `esperaMaxDias = ∞`, `horasEnVacio = 48` h, carga mientras haya cola, y una ULI urgente
(`pPrioridad` = 0,0095 por ULI) enciende bajo el umbral y se trata sola. Ver `07-modelo-anylogic.md`.

### 3.2 Escenarios

| Escenario | `umbralULI` | `esperaMaxDias` | `horasEnVacio` | Qué cambia |
|---|---|---|---|---|
| E0 base | 75 | ∞ | 48 | Regla actual (con prioridad en todos los escenarios) |
| E1 umbral bajo | 45 | ∞ | 48 | Campañas más frecuentes y cortas: menos espera, más kWh/kg |
| E2 umbral + espera máxima | 75 | 15 | 48 | Se enciende al cumplirse cualquiera de las dos: acota el peor caso de espera |
| E3 mantener caliente | 75 | ∞ | 96 | Evita 36 + 48 h entre campañas cercanas. Redefinido el 07/10/2026: la base ya mantiene 48 h, la alternativa es el doble |

Los valores de umbral y espera (dos o tres por parámetro) se eligen con las corridas piloto (paso 5)
para cubrir el rango donde la respuesta cambia. El E4 (turno adicional de carga) se cayó: el horno ya
opera en 3 turnos (24 h).

### 3.3 Parametrización en AnyLogic

Parámetros de `Main`: `umbralULI` (int), `esperaMaxDias` (double; ∞ = sin límite), `horasEnVacio`
(double), `hCalentamiento`, `hEnfriamiento`, `factorDemanda` (double), `semilla` (int),
`tasaCapitalMensual`, `tarifaKWh`, `minPorULI`. Por artículo, en la tabla de la base de datos: piezas por
ULI, kg por ULI, costo índice, pasa por horno (sí/no). Todo se varía desde el experimento sin tocar el
modelo.

### 3.4 Medidas de salida y regla de decisión

| Medida | Rol | Cómo se obtiene |
|---|---|---|
| Costo energético incremental por kg tratado | primaria | Σ kWh de las campañas / Σ kg tratados en el horizonte, por réplica, × tarifa |
| Costo financiero del capital inmovilizado | primaria | tasa mensual × promedio temporal del valor de (WIP pre-horno + stock de producto terminado), en índice |
| Nivel de servicio | restricción | proporción de líneas de pedido servidas completas dentro del plazo comprometido |
| Tiempo de entrega de pedidos | secundaria | media y percentil 90 (`TimeMeasureEnd` pedido → entrega) |
| Espera en cola del horno | secundaria | media y máximo (`TimeMeasureEnd` cola → salida del horno) |
| Campañas por mes, ULI por campaña, ocupación (ULI / 80) | secundarias y validación | registro por campaña |
| Inventario promedio valorizado | secundaria | promedio temporal de stock × costo índice |

Decisión: **costo relevante por kg = energía incremental + costo financiero del capital inmovilizado**,
sujeto a nivel de servicio ≥ objetivo (a fijar con la empresa). Se recomienda la regla de menor costo
relevante entre las que cumplen el nivel de servicio, **solo si** el intervalo de confianza del 95 % de
la diferencia contra E0 no contiene al cero. Si lo contiene, la conclusión es que no hay evidencia
para cambiar la regla, y se informa así. Los kWh se reportan aparte del costo para que el resultado no
dependa de la tarifa.

### 3.5 Costo energético incremental por kg

Por campaña: `kWh = P_cal · 36 h + P_mant · (duración de Procesando)`; el enfriamiento no consume. El gas
del generador y el desgaste por encendido (§2.3) se suman con la misma estructura: un término fijo por
campaña y uno por hora caliente.
Por réplica: `kWh/kg = Σ kWh / Σ kg` sobre todas las campañas del horizonte, cociente de totales y no
promedio de cocientes, para que cada campaña pese por lo que trató. Costo = kWh/kg × tarifa en índice.
Con umbral bajo el término fijo se reparte entre menos kg: esa pendiente es la que se compara con la
espera.

---

## 4. Validación

### 4.1 Contra qué, y con qué tolerancia

**Corregido (2026-09-27)**: no hubo reactivación puntual en 01/2026 — el horno opera intermitente desde
antes. La historia útil sigue siendo ~8 meses (enero-agosto 2026) porque es lo que cubre `Termico 2026`,
pero ya no hay que excluir un "transitorio de puesta a punto" post-reactivación: son 12 agrupamientos de
fechas de cementado en ese lapso (contados directo del registro, no eran 8-12 campañas limpias como se
estimaba — varias duran un solo día, ver `01-contexto-empresa.md`). Falta todavía confirmar si hay
registros de antes de enero 2026 y si el formato es planilla o papel. Escenario base, corrido con el mismo
lapso y nivel de demanda que la historia:

| Métrica histórica | Fuente | Tolerancia |
|---|---|---|
| Campañas por mes | registro de cargas | error relativo de la media ≤ 10 % |
| ULI (y kg) por campaña | registro de cargas | ≤ 10 % |
| Duración de campaña | registro de cargas | ≤ 10 % |
| Espera de una ULI antes del horno | fecha de lavado → fecha de cementado (`Seguimiento TR ulis`): **mediana 4 días, media 10,2, p90 26** (11.353 ULI) | ≤ 15 % en la media; percentil 90 dentro del intervalo del modelo |
| Tiempo de entrega de pedidos (Etapa 2) | NV → remito | ≤ 20 % |
| Nivel de servicio (Etapa 2) | reportes presupuestado/facturado — 49-51 % histórico | ≤ 15 % (con el motivo de la brecha aún sin separar; ver §2.1) |
| kWh mensuales | facturas 2026 | ≤ 15 % |

Tres criterios combinados, porque con ~10 campañas ningún test tiene mucha potencia por sí solo:

1. **Error relativo** de la media del modelo (30 réplicas) contra el valor histórico, con las
   tolerancias de la tabla.
2. **Intervalo de confianza de Welch** para la diferencia entre las observaciones reales (n₁ ≈ 10
   campañas) y las réplicas del modelo (n₂ = 30): no exige n₁ = n₂ ni varianzas iguales, que es
   exactamente la situación de validar contra un sistema real. Aceptable si contiene al cero al 95 %.
3. **Juicio del encargado**: se le muestran líneas de tiempo de campañas reales y simuladas sin decir
   cuál es cuál (test de Turing), más la animación.

Antes de eso, la validación del modelo conceptual (paso 3): revisión del documento de supuestos con el
encargado y con quien opera el ABM, antes de programar. Y la verificación (paso 4): traza de eventos en
una corrida corta, balance de flujo (ULI que entran = tratadas + en cola + en horno), animación, y un
caso degenerado con solución analítica: umbral 1, calentamiento y enfriamiento en 0, operador 24 h,
tiempos exponenciales → el horno es un M/M/1 y el modelo tiene que reproducir L, W y ρ.

### 4.2 Si el modelo no reproduce la historia

En orden, documentando cada cambio en el documento de supuestos:

1. Entradas: estacionariedad de los arribos (el arranque de 2026 puede tener un transitorio que hay
   que excluir de la historia y del ajuste) y unidades (kg por ULI varía por artículo).
2. Regla: si el encargado adelanta campañas por pedidos comprometidos, la regla real no es umbral
   puro; se agrega la prioridad y se vuelve a correr.
3. Tasa de ~17 ULI/día en 3 turnos: verificar contra las fechas de carga del registro.
4. Fin de campaña: si en la práctica no se procesan las ULI que llegan durante la campaña (o se
   mantiene el horno caliente más de lo supuesto), se corrige `horasEnVacio` o la condición de salida.

Lo que no se hace es mover parámetros hasta que coincida: calibrar no es validar. Si después de revisar
entradas y lógica alguna métrica sigue fuera de tolerancia, se declara la limitación y las conclusiones
se restringen a las métricas que sí validaron.

---

## 5. Diseño de experimentos

### 5.1 Tipo de simulación y horizonte

No terminante: la planta no se vacía en ningún momento natural. Se inicializa con el estado real
exportado del ABM (stock por artículo, ULI en cola, estado del horno) y se determina el período de
calentamiento con el método gráfico de Welch sobre el WIP y el stock valorizado (Law §9.5.1); se
descarta ese período y se recogen estadísticas durante 12 meses simulados. El horizonte de validación
(§4.1) es otro: ahí se simula el mismo lapso que la historia.

### 5.2 Experimento en AnyLogic

`Parameters Variation` sobre `Main`, variando `umbralULI`, `esperaMaxDias`, `horasEnVacio`,
`factorDemanda` y `semilla`:

- Configuraciones: E0-E3 × demanda {0,8; 1,0; 1,2} = 12.
- Réplicas: **30 por configuración**, implementadas variando `semilla` de 1 a 30 como parámetro, no
  con la opción de replicaciones del experimento, que asigna semillas al azar. Total 360 corridas; el
  modelo es liviano (miles de agentes por año), del orden de segundos por corrida.
- 30 es el n₀ del procedimiento de tamaño fijo, no un número cerrado: con las corridas piloto se
  estima S² de cada medida primaria; si la precisión relativa no llega a γ = 0,10, se agregan
  réplicas con el procedimiento secuencial.

### 5.3 Semillas y números aleatorios comunes

La réplica j usa la semilla j en todos los escenarios. Implementación: un generador `Random` propio
por fuente de aleatoriedad (tiempo entre pedidos, tamaño de pedido, tiempos aguas arriba, zincado,
ciclo), creados en `Main` a partir de la semilla (`new Random(semilla * 10 + k)`) y pasados como
último argumento a cada función de distribución (`exponential(lambda, rngPedidos)`,
`triangular(min, max, moda, rngZincado)`), incluidas las expresiones de los bloques `Source` y `Delay`.
La opción *Randomness* del experimento se deja en *Fixed seed* para que cualquier aleatoriedad residual
del motor también sea reproducible.

Con un generador por fuente, la demanda y los arribos de la réplica j son idénticos entre escenarios
aunque el horno se encienda en momentos distintos (sincronización): es la técnica de números
aleatorios comunes, que induce correlación positiva entre escenarios y reduce la varianza de la
diferencia. Es lo que habilita el test apareado.

### 5.4 Test de medias

Para cada alternativa contra E0 y cada medida primaria, intervalo de confianza **t-apareado** al 95 %
sobre las diferencias por réplica, Z_j = X_E0,j − X_Ek,j (j = 1 … 30):

- Z̄(n) = Σ Z_j / n; varianza estimada de Z̄: Σ (Z_j − Z̄)² / [n (n − 1)];
  intervalo Z̄ ± t_{n−1; 0,975} · √(varianza estimada).
- Contiene al cero → no hay diferencia significativa: resultado válido, se informa como tal. No lo
  contiene → la diferencia es significativa y el intervalo dice cuánto.
- Con tres medidas primarias, corrección de Bonferroni: α = 0,05 / 3 por intervalo, para que la
  conclusión conjunta mantenga el 95 %.
- Complemento: proporciones y cuantiles (proporción de pedidos con más de 30 días de entrega,
  percentil 90 de la espera pre-horno), porque comparar solo medias esconde diferencias en las colas
  de la distribución.

Las fórmulas van en el informe con la tabla de los Z_j como anexo.

### 5.5 Sensibilidad a la demanda

`factorDemanda` multiplica la tasa de pedidos de todos los artículos (0,8; 1,0; 1,2), con las mismas
semillas. Diseño factorial regla × demanda: además del efecto de cada regla, muestra si la mejor regla
cambia con el nivel de demanda (interacción). Se reporta una tabla regla × demanda con el intervalo de
la diferencia contra E0 en cada celda.

### 5.6 Registro de resultados

En *After simulation run* del experimento se escribe una fila por corrida (escenario, umbral, espera
máxima, horas en vacío, factor de demanda, semilla y cada medida de salida) en una tabla de la base de
datos interna de AnyLogic, exportada a CSV. Los intervalos y los gráficos se calculan con un script de
Python versionado junto al modelo, y la tabla cruda va como anexo del informe: cualquier número del
informe se reconstruye desde ahí.

### Referencias usadas en estas respuestas

- Law, A. M. *Simulation Modeling and Analysis*, McGraw-Hill: caps. 6 (modelado de entradas), 9
  (análisis de salidas) y 10 (comparación de sistemas).
- Grigoryev, I. *The Big Book of Simulation Modeling. Multimethod Modeling with AnyLogic 8*, The
  AnyLogic Company: cap. 8 (eventos por condición y timeout) y cap. 15 (generadores, semillas,
  `Random` como último argumento de las funciones de distribución).

---

## Notas internas (no van al docente)

**Lo que hay que cerrar con la empresa antes de mandar esto** (los `[confirmar]` del texto; la lista completa
para mandar a fábrica está en `03-pedido-de-datos.md` §Pedido para el Tema 1):

1. ~~¿Las ULI que llegan mientras el horno está caliente se suman a la campaña en curso? ¿Cuánto se
   mantiene caliente con la cola vacía antes de apagar?~~ **Resuelto (2026-09-27)**: no se suman por
   defecto — se guardan para la próxima campaña. Se mantiene caliente (o se adelanta el encendido) solo por
   **prioridad**: cuando se sabe que entra pronto un producto con entrega comprometida que no puede esperar
   a la próxima. Corregido el statechart en §1.2.
2. ~~¿Cuántos turnos de carga por día?~~ **Resuelto**: son **3 turnos de 8 h (24 h corridas)**, ~17
   ULI/día, no "15 por turno con un turno diario". Esto además **reconcilia** el "~1 semana" del brief
   original: 75 ULI / 17 por día ≈ 4,4 días de procesamiento; sumando 36 h de calentamiento y 48 h de
   enfriamiento da ≈ 7,9 días de campaña completa — consistente con "~1 semana". Corregido en §1.3.
3. ~~¿El encargado adelanta el encendido por pedidos comprometidos?~~ **Resuelto: sí** (mismo mecanismo
   de prioridad del punto 1).
4. Registro ISO de cargas: ¿planilla o papel? ¿Anota consumo o lectura de medidor por campaña?
   **Parcialmente resuelto**: el encargado aclaró que **el horno no tuvo un reencendido puntual en 01/2026**
   — viene funcionando **intermitente desde antes**, lo que contradice el "reactivado en 01/2026" que
   traíamos del brief inicial de la familia **[a reconciliar — ver `01-contexto-empresa.md`]**. Sobre
   cuántas campañas hubo, se contaron directo de `Termico 2026` en vez de preguntarle de memoria: **12
   agrupamientos** de fechas de cementado entre enero y agosto 2026 (`datos-locales/_perfil/campanas_termico2026.md`),
   pero varios duran un solo día — no son 12 campañas limpias de "acumular y tratar", varias parecen ser
   justamente los encendidos por prioridad del punto 1. **Simplificado (2026-09-27)**: que es planilla ya
   está probado — es literalmente `Termico 2026.xlsx`. Lo único que falta es una pregunta bien puntual:
   ¿alguien anota, en esa planilla u otra, el consumo real de gas o luz de una campaña, o una lectura de
   medidor antes/después? Si no lo anotan, el costo energético queda como estimado (ya calculado, §2.3) en
   vez de medido, y se declara así.
5. ~~¿El ABM conserva presupuestos (PV) no convertidos y NV canceladas?~~ **Resuelto (2026-09-24)**: sí,
   vía los reportes de presupuestado/facturado. Fill rate histórico 49-51%. **Motivo, resuelto (2026-09-27)**:
   el encargado lo resume en dos causas — **stock y plazo**. Sin desglose por línea individual, pero
   confirma que las dos causas dominantes son justo las que el modelo captura (disponibilidad y tiempo de
   entrega vía el horno), no precio ni competencia — valida la relevancia del Tema 1.
6. ~~¿Un turno adicional de carga durante la campaña es operable?~~ **Ya no aplica**: el punto 2 mostró
   que ya son 3 turnos (24 h), no queda un turno adicional que agregar. El encargado no entendió la
   pregunta porque, con la info real, no tenía sentido — se cae el escenario E4.
7. ~~Facturas de energía: 24 meses, con potencia contratada y si hay penalización por exceso.~~ **Recibidas
   y procesadas (28/09-05/10/2026)**: 64 facturas, ene/2024-ago/2026, con potencia convenida y registrada. El
   medidor "Horno" era exclusivo del horno hasta abril/2026; ver la fila de P_cal y P_mant en §2.1 y
   `03-pedido-de-datos.md`. Pendiente solo el GLP del generador endotérmico.
8. ~~De los 10-30 artículos elegidos, ¿cuáles requieren revenido?~~ **Resuelto (07/10/2026)** con la
   columna "Revenido" de `Seguimiento TR ulis`: 4 de los 15 propuestos (los de CASER-Drill). La demora a
   sumar es la distribución empírica Cementado→Revenido→Envío, no una constante (ver
   `06-articulos-seleccionados.md`).
9. De los artículos elegidos, ¿alguno es una de las excepciones que sí se mantienen con stock? (la regla
   general confirmada es "todo contra pedido" — ver §1.5).
10. ~~**Regla de fin de campaña — bloquea el `Hold` de §1.2 (07/10/2026).**~~ **Resuelto el mismo 07/10/2026**:
    el encargado respondió "las cargamos igual". Work-conserving es la regla base del modelo y el cupo queda
    como modo alternativo. Contexto original: el diseño del `Hold` con cupo por
    campaña (las ULI que llegan con el horno prendido esperan la próxima) sale de la entrevista del 27/09,
    pero el registro no lo respalda. Sobre 39 campañas de 2024 a 2026 (`datos-locales/_perfil/campanas_cola.md`):
    la cola al encender tiene mediana de 77 ULI (confirma el umbral de 70-80), pero las 22 campañas de 7 días
    o más tratan una mediana de 186 ULI (máximo 757 en 77 días) y apagan con la cola casi vacía (mediana 15).
    Eso solo es posible si las ULI que llegan se cargan mientras haya cola. Las otras 17 campañas son chicas
    (mediana 5 ULI, cola al encender 39): los encendidos por prioridad, el 44 % del total. **Hipótesis a
    confirmar**: el horno es "work-conserving" (procesa mientras haya cola, apaga al vaciarse) y lo que se
    guarda para la próxima son las ULI que llegan una vez iniciado el apagado. Si se confirma, el `Hold` con
    cupo se reemplaza por una condición sobre el tamaño de la cola en `Procesando`, y `horasEnVacio ≈ 0`.
    **Pregunta para el encargado**: *"Cuando el horno ya está procesando y llegan ULI nuevas, ¿las cargan
    igual a medida que llegan mientras haya cola, o las dejan esperando para la próxima encendida?"*

**Supuestos que quedaron escritos en la respuesta** (si alguno está mal, corregir ahí):
**3 turnos de 8 h (24 h), ~17 ULI/día** (corregido 2026-09-27, antes decía "un turno por día"); horno de una
ULI a la vez (≈ 85 min); **las ULI que llegan durante la campaña NO se procesan en ella — se guardan para la
próxima, salvo prioridad por entrega comprometida** (corregido 2026-09-27, antes era al revés); sin
recalentamiento parcial desde tibio en la base; campaña actual sin límite de espera fijo, con adelanto de
encendido y extensión de `horasEnVacio` por prioridad (confirmado); revenido fuera del modelo (otro equipo,
no aplica a todo el catálogo, demora aleatoria empírica donde corresponda); sin política de stock (s, Q) —
todo contra pedido, confirmado por la empresa, salvo excepciones puntuales a identificar entre los
artículos elegidos.

**Qué sale de la wiki y qué no**: la parte estadística (réplicas, precisión, procedimiento secuencial,
paired-t, Welch, números aleatorios comunes, Bonferroni, cuantiles) y los 10 pasos salen de SIM.md,
Unidades 5, 9 y 10. Los bloques y la mecánica de AnyLogic (statechart, Hold, Split, evaluación de
condiciones, semillas por stream) son conocimiento general verificado contra el Big Book de AnyLogic
(caps. 8 y 15), no material de la cátedra.
