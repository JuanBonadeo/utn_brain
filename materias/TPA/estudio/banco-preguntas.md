# TPA — Banco de preguntas para la defensa del TPI

> Sistema IoT con control PID y supervisión en ThingsBoard (comisión 4K01).
> Defensa **individual**: cada integrante tiene que poder defender **todo** el TP.
> Fuentes: enunciado (TPI 2026), informe final (TP04), `arduino.ino`,
> `nodemcu.ino`, `dashboard.json`.

## Cómo usar este documento
- Las respuestas están comprimidas: son el **núcleo** de lo que tenés que decir,
  no un guion para leer. Practicá decirlas con tus palabras.
- **[I]** = sale de tu informe/código (lo entregaste, tenés que sostenerlo).
  **[G]** = teoría general de control/IoT que agrego para que no te agarren en
  frío. En la defensa conviene distinguir "esto lo medimos/implementamos" de
  "esto es la teoría de fondo".
- Empezá por la sección **0. Flancos críticos**: son las 4 preguntas que un
  profe atento va a usar para complicarte. Si esas las tenés, el resto es cuesta
  abajo.

## Dónde está la nota (pesos del enunciado)
| Ítem | Peso |
|---|---|
| Implementación PID | 25% |
| Estabilidad y desempeño | 15% |
| Integración MQTT | 15% |
| Dashboard funcional | 15% |
| Arquitectura correcta | 10% |
| Informe técnico | 10% |
| Presentación y video | 10% |

**Control (PID + estabilidad) = 40%.** La mayoría de las preguntas van para ahí.

---

## 0. Flancos críticos (las 4 preguntas que te van a hacer)

### 0.1 — El modelo no predice: ts simulado ~26 ms vs experimental 1939 ms
La tabla 12.2 muestra ts simulado 14–26 ms y experimental **1939 ms** (~75× más
lento). Te van a preguntar si el modelo sirve.

**Respuesta:** τ = 10 ms captura la **componente rápida** de la respuesta del LDR.
La fotorresistencia tiene además una **cola lenta** (efecto memoria / histéresis
lumínica, típico de LDR de sulfuro de cadmio) que un modelo de primer orden no
representa. Por eso el lazo real se establece en ~1,9 s y no en ~26 ms. **El
modelo sirvió para una sintonía estable de arranque por síntesis directa, no como
predictor cuantitativo.** No defiendas que el modelo "está bien": reconocelo con
la explicación física y sumás.

### 0.2 — El Control P sobrepasa 4,67%, y eso no debería pasar
Un sistema de **primer orden puro, sin retardo, bajo control P NO puede
sobrepasar** (la respuesta a lazo cerrado sigue siendo exponencial monótona).

**Respuesta:** Que el P muestre sobreimpulso demuestra que la planta **no es de
primer orden puro**: hay dinámica de orden superior o retardo no modelado (o, en
parte, ruido del LDR leído como sobreimpulso). Refuerza el punto 0.1.

### 0.3 — El P llegó al 80%, pero el informe dice "la mitad"
La sección 12.3 dice que con Kp·K = 1 el P llega a la **mitad** del cambio
(simulado 393,5 = 187 + 206,5 ✓). Pero **experimentalmente llegó a 517 = 80%**
del salto (330 de 413).

**Respuesta:** El 50% es la predicción **nominal** con K = 4,11. Que dé 80%
significa que la **ganancia real en ese punto es ~4× la identificada**. Cuenta en
vivo: 517 = 187 + K_real·0,243·(600−517) → K_real ≈ 16,3 ≈ 4·K. **La diferencia
393,5 vs 517 es una medición directa del error de ganancia del modelo** por no
linealidad del LDR. Si tirás esa cuenta, ganás el punto.

### 0.4 — ts = 1939 ms idéntico para P y PI (artefacto)
Que dé **exactamente igual** al ms para dos controladores distintos casi seguro
es un artefacto del script `analizar_ensayo.py` (misma ventana de análisis o la
banda ±5% cruza en el mismo instante). **Revisá tus gráficos (Fig. 7 y 8) antes
de la defensa.** Si te preguntan, explicá el artefacto o corregí el número; no lo
defiendas como coincidencia física.

---

## 1. Conceptos base de control (por si abren con lo elemental)

**¿Lazo abierto vs lazo cerrado?** [G] Abierto: la salida no se mide ni corrige
(aplicás un PWM y esperás). Cerrado: se mide y(t), se calcula el error e = r − y y
se ajusta u para llevar y a r. El ensayo de la Etapa 1 es a lazo abierto; el
control de la Etapa 2 es cerrado.

**¿Qué es realimentación negativa?** [G] Restar la medición al setpoint (e = r − y).
En el código, `ultimoError = setpoint - ultimaY`. Estabiliza y reduce el error.

**¿Qué es un sistema tipo 0 y tipo 1?** [G] Tipo = cantidad de integradores puros
(polos en s = 0) en lazo abierto. La planta LED–LDR es **tipo 0** (no integra) →
con control P queda error estacionario ante un escalón. Agregar acción integral
lo vuelve **tipo 1** → error estacionario cero al escalón. Esta es la razón de
fondo del P vs PI.

**¿Por qué control digital y no analógico?** [G] Flexibilidad (cambiás Kp/Ki/Kd
por software), repetibilidad, integración con la capa IoT, y la posibilidad de
lógica extra (anti-windup, bumpless, límites). Costo: hay que muestrear y
cuantizar → aparecen Ts y el ruido del ADC.

**¿Qué es PWM y cómo controla el brillo?** [G] Modulación por ancho de pulso: una
señal cuadrada a frecuencia fija con duty cycle variable (0–255 → 0–100%). El LED
se prende/apaga rápido; el promedio temporal define el brillo percibido por el
LDR. `analogWrite(pin9, u)`.

**¿Qué es la cuantización del ADC?** [G] El ADC del Arduino es de **10 bits** →
1024 niveles (0–1023) para 0–5 V, ~4,9 mV por cuenta. El ruido de cuantización es
±½ cuenta y, sumado al ruido del LDR, produce las oscilaciones que ven en y y en u.

---

## 2. Modelado e identificación de la planta (Etapa 1)

**¿Qué es la planta acá?** [I] El camino óptico LED → LDR dentro de la caja
cerrada. Entrada: PWM al LED. Salida: cuentas ADC del LDR en A0.

**¿Cómo obtuvieron K y τ?** [I] Ensayo a lazo abierto: escalón de PWM 0→150.
- y₀ = 187 (reposo, PWM = 0), y∞ = 804 (nuevo estacionario).
- **K = Δy/ΔPWM = (804 − 187)/150 = 4,11** cuentas ADC por unidad de PWM.
- **τ = 10 ms** = tiempo en que y alcanza el 63,2% del cambio total.
- Modelo: **G(s) = 4,11 / (0,01·s + 1)**.

**¿Por qué primer orden y no segundo?** [G] La respuesta al escalón no mostró
oscilación ni sobreimpulso → se aproxima con un solo polo real. Es el modelo
estándar para procesos tipo térmico/óptico de primer orden.

**¿Por qué 63,2%?** [G] En G(s) = K/(τs+1), la respuesta al escalón es
y(t) = K·A·(1 − e^(−t/τ)). En t = τ, e^(−1) = 0,368 → y alcanzó 1 − 0,368 =
**63,2%** del cambio. Es la definición de constante de tiempo.

**¿La planta es lineal?** [I/G] **No.** El LDR tiene relación
resistencia–iluminación aproximadamente potencial/logarítmica → la ganancia varía
con el punto de operación. Lo reconocen en Limitaciones y es la causa de los
flancos 0.1 y 0.3.

**¿τ = 10 ms no es sospechosamente rápido?** [I] Es la debilidad del modelo: en el
ensayo muestrearon relativamente lento y τ = 10 ms queda en el orden de una o
pocas muestras → la identificación de τ es **gruesa**. Postura: "lo tomamos como
orden de magnitud de la componente rápida; sabemos que hay dinámica lenta no
capturada".

**¿Qué unidades tiene K?** [G] Cuentas ADC por unidad de PWM (adimensional en
rigor, pero es "cuánto sube la lectura por cada escalón de PWM").

**¿Por qué el escalón a 150 y no a 255?** [I] Para quedarse en una zona de
operación razonable sin saturar el sensor cerca de 1023 y con y∞ = 804 aún dentro
de rango. (Si no lo justificaste explícito, decí esto.)

---

## 3. Período de muestreo y controlador discreto (Etapa 2)

**¿Por qué Ts = 2 ms?** [I] Regla práctica Ts ≤ τ/5 con τ = 10 ms → 2 ms. [G] La
idea: 5–10 muestras por constante de tiempo para que la discretización no degrade
la dinámica ni desestabilice.

**¿Qué pasa si Ts es muy grande? ¿Y muy chico?** [G] Muy grande → el control "ve"
la planta con retardo, pierde información entre muestras, puede desestabilizar.
Muy chico → amplifica ruido en la derivada y gasta CPU sin beneficio. 2 ms es un
compromiso conservador.

**¿El loop() realmente cierra en 2 ms?** [I] Sí, se temporiza con `micros()` y
`if (ahoraUs - ultimaMuestraUs >= TS_US) { ultimaMuestraUs += TS_US; ... }`. El
`analogRead` tarda ~110 µs y las cuentas en float suman cientos de µs — cómodo
dentro de 2 ms. Detalle: usan `+= TS_US` en vez de `= ahoraUs` para **no acumular
deriva temporal** (mantiene el período exacto).

**¿A qué frecuencia registran datos?** [I] Tres relojes desacoplados: control 2 ms
(500 Hz), telemetría USB 100 ms (10 Hz), telemetría IoT 500 ms (2 Hz). En los
ensayos de análisis de la Etapa 2 registraron más rápido para capturar el
transitorio.

**Escribí el PID discreto que implementaron.** [I]
```
e(k) = r − y(k)
P    = Kp · e(k)
I(k) = I(k−1) + Ki · Ts · e(k)     (con integración condicional / anti-windup)
D    = −Kd · (y(k) − y(k−1)) / Ts   (derivada sobre la medición)
u(k) = saturar(P + I(k) + D, 0, 255)
```
Es la **forma posicional (paralela)**, no incremental.

**¿Cómo discretizaron la integral y la derivada?** [G] Integral por **Euler hacia
adelante** (rectángulos): I acumula Ki·Ts·e. Derivada por diferencia hacia atrás:
(y(k) − y(k−1))/Ts. Son las aproximaciones discretas más simples del integral y
la derivada continuos.

---

## 4. Estructura del PID: anti-windup, derivada, bumpless (Etapa 2)

**¿Por qué la derivada sobre la medición y no sobre el error?** [I/G] Para evitar
el **derivative kick**: un escalón de setpoint metería un impulso en de/dt.
Derivando sobre −y (que no salta cuando cambia r), un cambio de referencia no
golpea la salida. En el código: `derivada = -(y - yPrev) / Ts`.

**¿Qué es el windup y cómo lo evitan?** [G/I] Windup: cuando el actuador **satura**
(u pegado a 255 o 0), el integrador sigue acumulando error → sobreimpulso enorme y
recuperación lenta al desaturar. Lo evitan por **clamping (integración
condicional)**: dejan de integrar cuando la salida está saturada **y** el error
empuja en el mismo sentido de la saturación. Las 3 líneas clave:
```
bool estaSaturado          = (tentativo != saturado);
bool empujaHaciaSaturacion = (error * (tentativo - saturado)) > 0.0f;
if (!estaSaturado || !empujaHaciaSaturacion) integral += Ki * Ts * error;
```
Si no está saturado, integra normal. Si está saturado pero el error va a
sacarlo de la saturación, también integra. Solo bloquea cuando saturaría más.

**¿Se satura en la práctica?** [I] No: en los ensayos u llegó a ~100 sobre un
máximo de 255. Igual el anti-windup está por robustez ante escalones grandes o
perturbaciones. (Lo dicen en Conclusiones Etapa 2.)

**¿Qué es el bumpless transfer y dónde está?** [I] Evita el salto de u al cambiar
de modo. AUTO→MANUAL: `pwmManual = ultimoPwm` (el manual arranca donde estaba el
auto). MANUAL→AUTO: `integral = ultimoPwm - Kp·ultimoError` (precarga el
integrador para que u(k) = P + I dé exactamente el PWM actual). En MANUAL se
mantiene esa precarga cada ciclo.

**¿Por qué reinician `integral = 0` al cambiar Ki en vivo?** [I] Porque la variable
`integral` guarda la **contribución** integral (ya multiplicada por Ki, en
unidades de PWM); con el Ki nuevo, el valor acumulado con el Ki viejo quedaría
inconsistente. Reiniciar evita ese término espurio, a costa de un pequeño
transitorio (una caída momentánea de u que se vuelve a recomponer). Es una
simplificación aceptable para tuning en vivo.

**¿Por qué Kd = 0?** [I] El modelo es primer orden sin retardo → la derivada no
aporta a la dinámica de lazo cerrado; y sobre la señal del LDR con ruido de
cuantización, una derivada ≠ 0 **amplificaría el ruido** en u. Por eso operan como
**PI**. (El PID queda igual implementado y configurable por si hiciera falta.)

---

## 5. Sintonización por síntesis directa / IMC (Etapa 2)

**¿Qué método de sintonía usaron y por qué no Ziegler-Nichols?** [I] Síntesis
directa (control por modelo interno, IMC). Z-N por curva de reacción necesita
retardo L > 0; el modelo tiene L ≈ 0 → no aplica. IMC sí sirve para primer orden
sin retardo.

**Derivá los parámetros.** [I] Para G(s) = K/(τs+1) y un PI
C(s) = Kp·(Ti·s + 1)/(Ti·s):
- Se **cancela el polo de la planta** haciendo **Ti = τ**.
- El lazo cerrado queda de primer orden con constante de tiempo λ (parámetro de
  diseño), y **Kp = τ/(K·λ)**.
- Eligieron **λ = τ = 10 ms**.
- **Kp = 0,01/(4,11·0,01) = 0,243**; **Ti = 10 ms**; **Ki = Kp/Ti = 24,33**; Kd = 0.
- Verificación: **Kp·K = 0,243·4,11 ≈ 1**.

**¿Por qué λ = τ?** [I/G] Trade-off: λ chico = lazo más rápido pero controlador más
agresivo (Kp alto, amplifica ruido, riesgo de saturar). λ = τ da un lazo tan
rápido como la planta y, además, **λ = 5·Ts**, condición para que la
discretización no lo degrade.

**¿Qué pasa si λ → 0?** [G] Kp → ∞: control infinitamente agresivo, satura el PWM,
amplifica ruido, se vuelve inestable en la práctica. Por eso λ no se elige
arbitrariamente chico.

**¿Por qué cancelar el polo (Ti = τ)?** [G] Al hacer Ti = τ, el cero del PI cancela
el polo de la planta y el lazo abierto queda como un integrador puro
Kp·K/(τ·s)... → lazo cerrado de primer orden limpio con constante λ. Simplifica el
diseño a un solo parámetro (λ).

---

## 6. Ensayos y métricas de desempeño (Etapa 2)

**Definí las métricas.** [G]
- **Sobreimpulso Mp (%):** cuánto se pasa del valor final, (y_pico − y∞)/y∞ ·100.
- **Tiempo de establecimiento ts (±5%):** cuándo y entra y se queda en la banda
  ±5% de y∞.
- **Error estacionario e∞:** r − y∞ cuando t → ∞.
- **IAE:** ∫|e(t)|dt, integral del error absoluto (penaliza error acumulado);
  acá sobre una ventana de 200 ms.

**¿Cómo montaron el ensayo P vs PI?** [I] Escalón de setpoint automático a los 3 s,
de SP = 187 a SP = 600. Ensayo 1 (P): Ki = 0, Kp = 0,243. Ensayo 2 (PI): Ki =
24,33, **mismo Kp**, para aislar el efecto de agregar la integral. Datos procesados
con `analizar_ensayo.py`.

**Resultados clave** [I]:
| Métrica | P exp. | PI exp. |
|---|---|---|
| y∞ | 517 | 607 |
| Mp | 4,67% | 3,17% |
| ts (±5%) | 1939 ms | 1939 ms (⚠ ver 0.4) |
| e∞ | 83 | −7 |
| IAE (200 ms) | 200,47 | 49,33 |

**¿Por qué el P deja error y el PI no?** [I/G] La planta es **tipo 0** (sin
integrador): con P, se necesita un error finito para sostener un u ≠ 0, entonces
queda e∞ ≠ 0. La acción integral acumula mientras haya error → lo lleva a cero
(vuelve el lazo tipo 1). Mejora medida: e∞ de 83 a −7 cuentas (**−91,6%**), IAE de
200,47 a 49,33 (**−75,4%**).

**¿Por qué con P llega justo a la mitad (nominal)?** [I/G] Con Kp·K = 1, la
ganancia DC de lazo cerrado del P sobre tipo 0 es Kp·K/(1+Kp·K) = 1/2. La salida
cubre la mitad del cambio pedido: y∞ = 187 + 0,5·(600−187) = 393,5. (Experimental
dio 517 → ver flanco 0.3.)

**El PI también sobrepasa (3,17%), ¿por qué?** [G] La integral agrega un polo (y un
cero) → el lazo cerrado pasa a ser de **segundo orden**, que sí puede sobrepasar.
Es esperable y aceptable.

**¿Por qué la respuesta real es más lenta y oscilatoria que la simulada?** [I] No
linealidad del LED–LDR (la K real varía con el punto de operación), cuantización
del ADC y ruido de medición. El modelo nominal subestima la dinámica lenta.

---

## 7. Arquitectura del sistema y separación de capas

**Describí la arquitectura en capas.** [I]
1. **Planta física:** LED (actuador, PWM) + LDR (sensor) en caja cerrada.
2. **Arduino UNO:** control en tiempo real (lazo cada 2 ms). NO hace MQTT.
3. **NodeMCU ESP8266:** gateway WiFi/MQTT. NO hace control.
4. **ThingsBoard Cloud:** broker MQTT, persistencia, dashboard, RPC.

**¿Por qué separar control (Arduino) de comunicaciones (NodeMCU)?** [I] Para que la
**dinámica del lazo (2 ms) no dependa de la latencia de red** ni del broker. El
control es duro en tiempo real; la telemetría a 2 Hz y los comandos RPC son
"blandos". Además simplifica debug y permitió cambiar el dashboard sin tocar el
firmware.

**Identificá controlador, planta, sensor y actuador (pedido en 4.4).** [I]
- Controlador: PID discreto en el Arduino (calcula u a partir de e).
- Actuador: LED + driver PWM (traduce u a brillo).
- Planta: camino óptico LED→LDR.
- Sensor: LDR + divisor resistivo → A0 (realimenta y con signo negativo, H = 1).

**¿Por qué NO poner el PID en la nube?** [I/G] Latencia y jitter de WiFi/MQTT
(cientos de ms, variable) son inadmisibles para un lazo de 2 ms. El control tiene
que estar en el borde (edge). La nube es supervisión y ajuste de parámetros, no
control en tiempo real. Lo dicen explícito en Limitaciones.

---

## 8. Comunicación Arduino ↔ NodeMCU (Etapa 3)

**¿Por qué SoftwareSerial y no el Serial de hardware?** [I/G] El UART de hardware
está tomado por el USB (debug/flasheo) en ambas placas, y el UNO tiene **un solo
UART**. SoftwareSerial deja libre el Monitor Serie. Velocidad del enlace: 9600
baudios.

**¿Por qué el divisor 1,8k/3,3k?** [I] Level shifting. El TX del Arduino es 5 V y
el NodeMCU tolera 3,3 V. 5·3,3/(1,8+3,3) = **3,24 V** → seguro para el ESP. En
sentido inverso (NodeMCU D6 → Arduino pin 11) va directo: los 3,3 V del ESP
superan el umbral HIGH del Arduino (0,6·5 = 3,0 V). Es **marginal** (3,3 apenas >
3,0); en producción usaría un conversor de nivel dedicado.

**¿Por qué fallaba con D7/D8 y anduvo con D5/D6?** [G — no está explicado en el
informe, agregalo] En el ESP8266, **D8 = GPIO15 es pin de boot-strapping**: debe
estar en LOW al arrancar. Si el Arduino lo mantiene alto, el ESP no bootea bien →
enlace inestable. **D5/D6 = GPIO14/GPIO12** están libres de esa restricción. Tu
informe solo dice "se movió a D5/D6"; agregar el **por qué** te suma mucho.

**¿Qué manda cada uno por el enlace?** [I] Arduino → NodeMCU: línea JSON de
telemetría cada 500 ms. NodeMCU → Arduino: comandos de texto `SP:`, `KP:`, `KI:`,
`KD:`, `PWM:`, `MODE:` cuando llega un RPC.

**¿Por qué el JSON se arma campo por campo en el Arduino?** [I] El `printf` de
AVR-libc **no soporta `%f`** (float). Por eso concatenan cada campo con
`nodeMCU.print(...)`. Está comentado en el código.

---

## 9. MQTT y ThingsBoard (Etapa 3)

**¿Qué es MQTT?** [G] Protocolo de mensajería **publish/subscribe** liviano sobre
TCP, pensado para IoT. Un **broker** central (ThingsBoard) recibe publicaciones en
**topics** y las entrega a los suscriptos. Desacopla emisor y receptor.

**¿Qué QoS usan?** [G/I] `PubSubClient` usa **QoS 0** por defecto (fire-and-forget,
sin confirmación). Aceptable para telemetría periódica a 2 Hz: si se pierde un
mensaje, el siguiente llega en 500 ms.

**El enunciado (9.1) pide topics `utn/2026/c01/g01/telemetry` pero ustedes usan
`v1/devices/me/telemetry`. ¿Por qué?** ⭐ [I/G] **Pregunta trampa estrella.** Porque
la **API MQTT de dispositivos de ThingsBoard obliga topics fijos**:
`v1/devices/me/telemetry`, `v1/devices/me/rpc/request/+`,
`v1/devices/me/attributes`. El **token de acceso identifica al dispositivo/grupo**,
no la ruta del topic. El esquema `utn/2026/...` correspondería a un broker MQTT
genérico (ej. Mosquitto). Saber esto demuestra que entendés MQTT **y**
ThingsBoard.

**¿Cómo se autentica el NodeMCU?** [I] `mqtt.connect("esp_tpi_g01", TB_TOKEN, "")`:
el **token va como usuario** y la contraseña vacía. ThingsBoard identifica el
dispositivo por ese token. Host `mqtt.thingsboard.cloud`, puerto **1883**.

**¿Qué es un RPC one-way?** [I/G] Remote Procedure Call de un solo sentido: el
dashboard/servidor invoca un método (`setSetpoint`, etc.) con un parámetro; el
dispositivo lo ejecuta y no necesita responder. Llegan por
`v1/devices/me/rpc/request/+` (el `+` es comodín del id de request).

**¿Cómo se ve un dispositivo offline?** [I] ThingsBoard gestiona el atributo
`active` según el keepalive MQTT; si el NodeMCU se desconecta, pasa a inactivo. El
NodeMCU además publica `{"status":"online"}` y el RSSI cada 30 s en `attributes`.

**¿Qué campos publican en telemetría?** [I] JSON con `y, r, e, u, kp, ki, mode`
cada 500 ms (2 Hz). (Nota: no publican `kd`; la consigna lo listaba en el ejemplo,
es un detalle menor.)

---

## 10. Dashboard y control remoto (Etapa 4)

**¿Cómo llega un cambio del slider al Arduino?** [I] Widget ejecuta RPC (ej.
`setSetpoint`) → ThingsBoard publica en `v1/devices/me/rpc/request/{id}` →
callback `onMqttMessage` del NodeMCU parsea el JSON → reenvía `SP:<valor>` por
SoftwareSerial → `aplicarComando()` en el Arduino aplica el cambio.

**¿Qué widgets tiene el dashboard?** [I]
- Gráfico y(t) vs r(t) (time series).
- Gráfico u(t) (time series, eje 0–255).
- Gráfico e(t).
- Indicador de modo (AUTO/MANUAL).
- Indicador online/offline (atributo `active`).
- Sliders/perillas: setpoint, Kp, Ki, Kd, PWM manual.
- Botón de modo AUTO/MANUAL.

**⚠ Discrepancia informe vs `dashboard.json`:** el informe (16.3) menciona
"sliders decimales" para Kp/Ki/Kd y "dos botones independientes" para el modo. El
JSON real tiene **perillas (knob_control)** para Kp/Ki/Kd y **un `power_button`**
que manda AUTO (on) / MANUAL (off). Si te preguntan por un widget puntual,
describí **lo que está en el JSON**.

**¿Por qué no un switch booleano para el modo?** [I] Porque `setMode` espera el
texto `AUTO` o `MANUAL`, no un booleano. El power_button mapea on→"AUTO",
off→"MANUAL" con valores constantes de RPC.

**¿Cómo mapea el setpoint (0–1023) con el brillo?** [I] El setpoint está en cuentas
ADC (0–1023, 10 bits), igual que y. Se controla directamente la **lectura del
LDR**, no una magnitud física en lux (no calibraron el LDR a lux). Es una
decisión válida: la variable controlada es la cuenta del sensor.

**¿Qué pruebas finales hicieron?** [I] Cambio de setpoint desde el slider; Ki = 0
vs 24,33 en vivo (aparece/desaparece el error); modo MANUAL con PWM directo; corte
de alimentación del NodeMCU (pasa a offline); apertura de la ventana lateral
(perturbación → el controlador compensa).

---

## 11. Seguridad, limitaciones y mejoras (el enunciado evalúa "Seguridad")

**¿Es seguro el sistema? ¿Qué mejorarías?** [I/G] Limitaciones actuales:
- **Credenciales WiFi y token hardcodeados** en `nodemcu.ino` → en producción,
  provisioning/almacenamiento seguro, no en el código.
- **MQTT en puerto 1883 sin TLS** → tráfico en claro. Mejora: TLS por **8883**.
- **Dashboard público por URL** → cualquiera con el link ve/opera. Mejora: acceso
  autenticado.
- **QoS 0** → sin garantía de entrega (aceptable para telemetría, no para comandos
  críticos).

**Limitaciones técnicas que ya reconocen** [I]:
- No linealidad LED–LDR: la K varía con el punto de operación (causa raíz de la
  diferencia sim vs experimental).
- Ruido de cuantización del ADC de 10 bits → oscilaciones en u, amplificadas por
  la integral.
- Latencia RPC depende de la red; sirve para operación interactiva, **no** para
  control en lazo cerrado por la nube.

**Si tuvieras que mejorar el control, ¿qué harías?** [G] Filtrar la medición del
LDR (media móvil / filtro pasa-bajos) antes del PID; re-identificar la planta con
mejor resolución temporal y en varios puntos de operación (para capturar la no
linealidad); eventualmente linealizar por tramos o usar ganancia programada
(gain scheduling).

---

## 12. Preguntas de cierre típicas

**¿Cumplieron todos los objetivos?** [I] Sí: planta identificada y modelada, PID
discreto funcional (PI con e∞ −91,6% e IAE −75,4% vs P), gateway bidireccional
Arduino–NodeMCU–ThingsBoard, y dashboard de supervisión y control remoto. El
dashboard no obligó a cambiar el firmware → validó la separación de capas.

**¿Qué fue lo más difícil?** [I] El enlace serial Arduino–NodeMCU (el tema
D7/D8 → D5/D6) y conciliar el modelo lineal con la respuesta real no lineal.

**¿Qué aprendiste?** [G] Ciclo completo de ingeniería de control: identificación →
diseño/sintonía → implementación embebida → integración de comunicaciones →
supervisión remota. Y que un modelo simple sirve para arrancar aunque no prediga
con exactitud.

**¿Escalarías esto a un caso industrial? ¿Qué cambiarías?** [G] Sensor/actuador
industrial calibrado, protección eléctrica, TLS y autenticación, QoS 1/2 para
comandos, watchdog y modo seguro ante pérdida de comunicación, y control siempre
en el borde (nunca por la nube).

---

## 13. Hoja de datos rápida (repaso de último minuto)

**Planta:** G(s) = 4,11/(0,01·s + 1) · K = 4,11 cuentas/PWM · τ = 10 ms.
**Ensayo lazo abierto:** PWM 0→150 · y: 187→804 · y₀=187, y∞=804.
**Muestreo:** control 2 ms (τ/5, 500 Hz) · USB 100 ms (10 Hz) · IoT 500 ms (2 Hz).
**PID (PI):** Kp = 0,243 · Ki = 24,33 · Kd = 0 · Ti = 10 ms · λ = 10 ms · Kp·K ≈ 1.
**Sintonía:** IMC/síntesis directa · Ti = τ (cancela polo) · Kp = τ/(K·λ).
**Saturación:** PWM 0–255 (8 bits) · setpoint 0–1023 (ADC 10 bits).
**Métricas P:** y∞=517 · Mp=4,67% · e∞=83 · IAE=200,47.
**Métricas PI:** y∞=607 · Mp=3,17% · e∞=−7 · IAE=49,33 · (mejora e∞ −91,6%, IAE −75,4%).
**Pinout Arduino:** LDR→A0 · LED PWM→pin 9 · SoftSerial RX=11, TX=10.
**Pinout NodeMCU:** SoftSerial RX=D5, TX=D6 · divisor 1,8k/3,3k en TX Arduino.
**MQTT:** mqtt.thingsboard.cloud:1883 · auth por token (usuario=token, pass vacía).
**Topics:** `v1/devices/me/telemetry` · `.../rpc/request/+` · `.../attributes`.
**RPC:** setSetpoint, setKp, setKi, setKd, setPwm, setMode.
**Serial cmds:** SP:, KP:, KI:, KD:, PWM:, MODE:.
**Integrantes:** Alonso (52904), Bonadeo (53533), Casermeiro (52674), Estevez (53528).

---

## 14. "Explicá esta línea/fragmento" (defensa de código)

Te pueden abrir el `.ino` y pedir que expliques un fragmento. Los más probables:

**Anti-windup** (`arduino.ino`): las 3 líneas de `estaSaturado` /
`empujaHaciaSaturacion` / `if` → ver 4.

**Derivada sobre medición**: `derivada = -(y - yPrev) / Ts;` → evita derivative
kick; el signo negativo es porque la derivada del error −de/dt = −d(r−y)/dt = dy/dt
(con r constante) → −(y−yPrev)/Ts.

**Bumpless** (`aplicarComando`, rama MODE): `integral = ultimoPwm - Kp*ultimoError;`
→ precarga el integrador para que u no salte al pasar a AUTO. Ver 4.

**Temporización del lazo**: `if (ahoraUs - ultimaMuestraUs >= TS_US) {
ultimaMuestraUs += TS_US; ... }` → período fijo de 2 ms sin deriva.

**Parser de comandos** (`aplicarComando`): parte la línea en `clave:valor`,
convierte y aplica límites con `constrain`/`max`. Ej.: `setpoint =
constrain(valor.toFloat(), 0, 1023);`.

**NodeMCU — extracción de RPC** (`onMqttMessage`): `if (s.indexOf("setSetpoint") >=
0) { arduinoLink.print("SP:"); arduinoLink.println(extractInt(s, "value")); }` →
detecta el método, extrae `value` del JSON y reenvía el comando serial.

**NodeMCU — publicación**: en `loop()`, si llega una línea que empieza con `{` y
termina con `}` y hay conexión, `mqtt.publish(TOPIC_TEL, line.c_str())` → reenvía
el JSON del Arduino tal cual a ThingsBoard.
