# TPA — Explicación completa del TP (apunte de estudio)

> El TP explicado de punta a punta, en criollo, para **entenderlo a fondo** (no
> para memorizar). Es el recorrido que hicimos paso a paso.
> Complementa a [`banco-preguntas.md`](banco-preguntas.md) (preguntas de defensa)
> y [`guion-defensa.md`](guion-defensa.md) (el speech oral).
>
> Convención: **[ustedes]** = decisión/dato de la entrega (informe/código).
> **[teoría]** = concepto general de control/IoT.

## Índice
0. La foto grande (qué hace el sistema)
1. Etapa 1 — La planta: hardware y modelo
2. Etapa 2 — El controlador (PID)
3. Etapa 3 — Integración IoT (NodeMCU, MQTT, ThingsBoard)
4. Etapa 4 — El dashboard y el cierre
5. Recap en una carilla

---

## 0. La foto grande

### Qué hace el sistema
Mantener un **nivel de luz** constante, solo, y poder verlo/ajustarlo por internet.
En chico: un **LED** (foco) y un **LDR** (sensor de luz) enfrentados dentro de una
caja de cartón cerrada. El sistema mide cuánta luz hay, la compara con la que
querés, y ajusta el LED para que coincida — aunque metas perturbaciones (abrir una
ventanita de la caja para que entre luz de afuera). La caja aísla la luz ambiente:
así lo único que mide el sensor es la luz del LED.

### El concepto central: lazo cerrado (realimentación) [teoría]
Es lo más importante del TP (control = 40% de la nota). Igual que **ajustar la
ducha**: sentís el agua (medís), la comparás con la que querés (setpoint), y
corregís la canilla; y repetís todo el tiempo. Los nombres formales:
- **r** (referencia/setpoint): la luz que querés. La ponés vos.
- **y** (variable medida): lo que mide el LDR ahora.
- **e** (error): e = r − y. Cuánto falta.
- **u** (señal de control): el PWM que le mandás al LED para corregir.

El **controlador** hace la cuenta "miro el error y decido cuánto corregir", 500
veces por segundo. "Lazo cerrado" = la salida (y) **vuelve** a la entrada para
calcular el error. Si cortás esa vuelta, es **lazo abierto** (así se hace el ensayo
de la Etapa 1).

### Las cuatro capas (la arquitectura) [ustedes]
1. **Planta física** — LED + LDR en la caja. Lo que se controla.
2. **Arduino UNO** — el control en tiempo real (cada 2 ms). No sabe de internet.
3. **NodeMCU ESP8266** — puente a internet. No hace control, solo comunica.
4. **ThingsBoard (nube)** — guarda datos, grafica, y deja mandar comandos.

**Por qué separar control (Arduino) de comunicación (NodeMCU):** el control tiene
que ser rapidísimo y puntual (2 ms), e internet es lento e impredecible. Si los
mezclaras, la red arruinaría el control. Regla: **el control va pegado a la planta
(el "borde"), la nube es solo para mirar y ajustar.**

---

## 1. Etapa 1 — La planta: hardware y modelo

### 1.1 El hardware (los circuitos) [ustedes]

**Circuito del sensor: LDR + divisor de tensión** — *la pregunta clásica*.
El Arduino, por A0, lee **voltaje** (0–5 V → 0–1023). Pero el LDR cambia de
**resistencia** con la luz. No podés enchufar "resistencia" a un lector de voltaje:
el **divisor de tensión** es el traductor.
Circuito: **5 V → LDR → nodo (a A0) → resistencia fija 10 kΩ → GND.**
$$V_{A0} = 5\,V \cdot \frac{10k}{R_{LDR}+10k}$$
Más luz → el LDR baja su resistencia → A0 sube. El 10 kΩ se elige en el medio del
rango del LDR para tener buena sensibilidad.

**Circuito del actuador: LED.** Pin 9 → resistencia 220 Ω → LED → GND.
- **La resistencia de 220 Ω** es **limitadora de corriente**: sin ella, el LED y el
  pin se queman. Fija ~9–10 mA.
- **Pin 9** porque es de los que tienen **PWM** (`~`: 3, 5, 6, 9, 10, 11). **A0**
  porque es entrada analógica (solo A0–A5 tienen ADC).

**La caja (maqueta):** cartón cerrado, LED apuntando al LDR, agujero del cable
sellado (que no se filtre luz), y una **ventanita lateral** = la entrada de
perturbación (la abrís para probar si el control compensa la luz de afuera).

> Este hardware **es** la planta: el "camino óptico LED→LDR" que modelamos con
> $G(s)$ son, físicamente, estos dos circuitos dentro de la caja.

### 1.2 El modelo (identificación) [ustedes + teoría]

**Por qué modelar** [teoría]: antes de controlar, hay que saber cómo reacciona la
planta (como tantear el acelerador de un auto nuevo). Modelar = ponerle números.

**El ensayo a lazo abierto** [ustedes]: sin realimentación, mandás una entrada fija
y mirás la salida en crudo.
- Reposo (PWM = 0): el LDR marcaba **y₀ = 187**.
- Escalón de PWM **0 → 150** (un salto brusco).
- La lectura trepó hasta **y∞ = 804**.

**El modelo de primer orden** [teoría]: cuando le pegás el salto, el sensor no salta
de golpe: **trepa suave y se estaciona** (como la temperatura de una pieza al
prender una estufa). Eso es un sistema de **primer orden**, descrito por dos números:
$$G(s) = \frac{K}{\tau s + 1}$$
- **K = ganancia estática** = cuánto cambia al final:
  $K = \frac{804 - 187}{150} = 4{,}11$ cuentas por unidad de PWM.
- **τ = constante de tiempo** = qué tan rápido llega (tiempo al 63,2% del cambio):
  **τ = 10 ms**. A las 4τ = 40 ms ya cubrió el 98%.
- Resultado: $G(s) = \dfrac{4{,}11}{0{,}01\,s + 1}$.

**La letra chica (importante):** es una **aproximación lineal** de una planta **no
lineal** (el LDR). Y τ = 10 ms se midió grueso: captura la parte *rápida* de la
respuesta, pero el LDR tiene una **cola lenta** que el modelo no incluye. El modelo
fue una **herramienta de diseño para arrancar**, no un predictor exacto. (Esto
reaparece en la Etapa 2.)

---

## 2. Etapa 2 — El controlador (PID)

### 2.1 El latido: Ts = 2 ms [ustedes]
El control es digital: "late" cada 2 ms. Cada latido:
**leer LDR → calcular e = r − y → calcular PID → actualizar PWM** (500 Hz).
El 2 ms sale de la regla **Ts ≤ τ/5** (con τ = 10 ms): muestrear bastante más
rápido que la planta para no perderle el paso.

### 2.2 El PID: tres miradas del error [teoría]
El PID mira el error y decide la corrección combinando tres puntos de vista.
Analogía: **control crucero** (mantener una velocidad); el error es cuánto te falta.
- **P — Proporcional:** reacciona al error de **ahora**. Más lejos, más fuerte
  corregís. *Problema:* solo con P **queda un error residual** (para sostener el
  empuje necesita que sobre error).
- **I — Integral:** reacciona al error **acumulado** (la historia). Mientras haya
  error, lo acumula y corrige más hasta eliminarlo. **Por eso el PI mata el error
  que el P deja.**
- **D — Derivativo:** reacciona a la **tendencia** (qué tan rápido cambia), para
  anticipar. **Ustedes lo pusieron en 0** (Kd = 0): la planta es simple y el LDR
  tiene ruido; derivar ruido lo amplifica. Corre como **PI**.

Se suman: **u = P + I + D**, y se recorta al rango del PWM (**0–255**).

### 2.3 Los tres detalles finos (nivel defensivo) [teoría + ustedes]
*Cartón de emergencia por si preguntan:*
- **Anti-windup:** si el PWM se satura, la integral **deja de acumular** para no
  descontrolarse (si no, sobreimpulso enorme al desaturar). *La cuesta empinada:
  pisás a fondo y el auto igual no llega; una integral ingenua acumula de más.*
- **Derivada sobre la medición:** se deriva la señal medida, **no el error**, para
  que un cambio de setpoint no pegue un **golpe** (derivative kick). *El volantazo.*
- **Bumpless:** al cambiar de modo (AUTO/MANUAL) se **precarga la integral** para
  que el PWM no salte. *Como pasar el volante de un auto en movimiento.*

### 2.4 Sintonía: de dónde salen los números [ustedes + teoría]
Tres tipos de parámetros:
- **De la planta (medidos):** K = 4,11 · τ = 10 ms.
- **Tu decisión de diseño:** λ (lambda) = qué tan rápido querés el lazo cerrado.
- **Del controlador (calculados):** Ti, Kp, Ki, Kd.

**No a prueba y error, sino calculado desde el modelo.** No usaron Ziegler-Nichols
porque ese método necesita retardo (L > 0) y la planta no tiene. Usaron **síntesis
directa / IMC**:
1. **Ti = τ** → cancela la lentitud propia de la planta (deja el lazo limpio).
2. **Kp = τ / (K·λ)**.
3. Eligieron **λ = τ = 10 ms** (lazo tan rápido como la planta; y λ = 5·Ts).

Las cuentas:

| Parámetro | Fórmula | Valor |
|---|---|---|
| Ti | = τ | 10 ms |
| Kp | τ/(K·λ); como λ=τ → **1/K** = 1/4,11 | **0,243** |
| Ki | Kp/Ti | **24,33** |
| Kd | — | 0 |

**Dato clave:** como Kp = 1/K, entonces **Kp·K = 1** (porque elegiste λ = τ). Es la
llave del P vs PI.

### 2.5 El experimento P vs PI [ustedes + análisis]
Escalón de setpoint 187 → 600, corrido **dos veces**: P (Ki = 0) y PI (Ki = 24,33),
con el **mismo Kp** (para aislar el efecto de la integral).

**Lo que predice la teoría:** el P deja error (la planta es **tipo 0**, sin
integrador propio); y con Kp·K = 1, el P llega **justo a la mitad** del cambio
(y = 187 + ½·(600−187) = 393,5). El PI elimina el error → llega a 600.

**Lo que pasó (datos reales):**

| Métrica | P | PI |
|---|---|---|
| Valor final y∞ | 517 | 607 |
| Sobreimpulso | 4,67 % | 3,17 % |
| Error estacionario | 83 | −7 |
| IAE | 200,47 | 49,33 |

El PI gana claro: error estacionario **−91,6 %**, IAE **−75,4 %**. *Ese es el
resultado central de la etapa.*

**Las tres "joyas" (lo que las diferencias enseñan)** — *no están explícitas en el
informe; son para lucirte*:
1. **El P llegó al 80%, no al 50%** → la ganancia real es más grande que la medida.
   Se cuantifica: 517 = 187 + K_real·0,243·(600−517) → **K_real ≈ 16 ≈ 4×K**. O
   sea: la diferencia mide cuánto se equivoca el modelo. Si dicen "su modelo está
   mal", respondés "sí, y le medimos el error: la ganancia real es 4× la nominal".
2. **El P sobrepasó 4,67% — imposible en primer orden puro** → la planta tiene
   dinámica de orden superior/retardo no modelado (o ruido del LDR).
3. **Tiempo real ~1900 ms vs simulado ~26 ms (~75×)** → el τ capturó solo la parte
   rápida; el LDR tiene cola lenta. Modelo = punto de partida, no predictor.

**Conclusión de la etapa:** el PI es claramente superior; la sintonía analítica dio
un lazo estable de entrada; las diferencias sim-vs-real se explican por la no
linealidad, la cuantización del ADC y el ruido. **No es un fracaso: es lo esperable
al modelar linealmente una planta que no lo es.**

---

## 3. Etapa 3 — Integración IoT

Objetivo: verlo y controlarlo por internet, con **una regla de oro: no tocar el
control**. La cadena de dos saltos:
$$\text{Arduino} \xrightarrow{\text{serie}} \text{NodeMCU} \xrightarrow{\text{WiFi+MQTT}} \text{ThingsBoard}$$

### 3.1 El enlace físico Arduino ↔ NodeMCU [ustedes]
- **SoftwareSerial (9600 baudios):** el puerto serie de hardware está ocupado por
  el USB en ambas placas, y el UNO tiene uno solo → emulan un segundo puerto por
  software.
- **Divisor de tensión (1,8k/3,3k):** el TX del Arduino manda 5 V y el NodeMCU solo
  tolera 3,3 V → el divisor baja a ~3,24 V. Al revés (NodeMCU→Arduino) va directo:
  3,3 V ya alcanza para leerse como "1".
- **D5/D6 y no D7/D8:** en D7/D8 el enlace era inestable. El porqué (que suma): en
  el NodeMCU, **D8 (GPIO15) es pin de arranque** que debe estar en bajo al bootear;
  el cable lo mantenía alto. D5/D6 (GPIO14/12) están libres de eso.

### 3.2 MQTT y ThingsBoard [teoría + ustedes]
**MQTT** [teoría]: protocolo **publicar/suscribir**, liviano, típico de IoT. Como
un **tablón de anuncios con etiquetas**: publicás bajo una etiqueta (**topic**),
y el que está suscripto se entera; nadie se habla directo, todo pasa por el
**broker**. Acá el broker es **ThingsBoard**.
**ThingsBoard** [ustedes]: es broker MQTT **y** plataforma (guarda, grafica,
dashboard). El NodeMCU se autentica con un **token** — el token es la identidad del
dispositivo, sin usuario ni contraseña. *(QoS 0: "mandar y olvidar", bien para
telemetría periódica.)*

### 3.3 Los dos canales [ustedes]
- **⬆ Telemetría (cada 500 ms):** el Arduino arma un JSON `{y, r, e, u, kp, ki,
  mode}`, lo manda al NodeMCU por serie, y el NodeMCU lo publica en
  `v1/devices/me/telemetry`.
- **⬇ Comandos RPC:** el NodeMCU está suscripto a `v1/devices/me/rpc/request/+`.
  Movés algo en el dashboard → ThingsBoard manda un RPC → el NodeMCU lo traduce a
  un comando serie (`SP:600`) → el Arduino lo aplica. Métodos: setSetpoint, setKp,
  setKi, setKd, setPwm, setMode.

### 3.4 El tema de los topics ⭐ (la pregunta estrella de IoT)
El enunciado sugería topics tipo `utn/2026/c01/g01/telemetry`, pero usaron
`v1/devices/me/telemetry`. **Por qué:** la API de dispositivos de ThingsBoard
**obliga topics fijos**; vos no elegís la ruta, la identidad va en el **token**. El
esquema `utn/2026/...` sería para un broker genérico (Mosquitto). No ignoraron el
enunciado: usaron la convención correcta para la plataforma elegida.

### 3.5 ⚠️ Detalle a verificar antes de la defensa
El NodeMCU busca la clave `value` en el JSON del RPC, pero ThingsBoard, cuando el
widget dispara el RPC, suele mandar el número en `params`. Si no coinciden, **los
sliders del dashboard no cambiarían nada** (solo andaría la herramienta manual
"Make an RPC request"). **Probá cada control del dashboard antes del día.**

### 3.6 Pruebas de integración [ustedes]
- Telemetría: en "Latest telemetry" se veían y, r, e, u, kp, ki, mode cada 500 ms.
- RPC: un setSetpoint de prueba cambió el setpoint de 323 a 484 y se reflejó en la
  telemetría → recorrido completo ThingsBoard→MQTT→NodeMCU→Arduino confirmado.

---

## 4. Etapa 4 — El dashboard y el cierre

La **capa de presentación**, sobre ThingsBoard. Toda la maquinaria pesada ya estaba
hecha; el dashboard solo le pone cara web.

**Widgets de visualización (mirar) [ustedes]:**
- Gráfico **y(t) vs r(t)** (luz medida vs pedida) — el gráfico principal.
- Gráfico **u(t)** (señal de control, PWM 0–255).
- Gráfico **e(t)** (error).
- Indicador de **modo** (AUTO/MANUAL).
- Indicador **online/offline** (atributo `active` de ThingsBoard).

**Widgets de control (operar) [ustedes]:** cada uno dispara un RPC.
- Slider de **setpoint** → setSetpoint.
- Perillas de **Kp, Ki, Kd** → setKp/setKi/setKd.
- Slider de **PWM manual** → setPwm.
- Botón **AUTO/MANUAL** → setMode.

*(Detalle informe vs realidad: el informe dice "sliders" y "dos botones"; el
`dashboard.json` real tiene perillas (knobs) y un power_button. Describí el JSON.)*

**El cierre del proyecto ⭐ (la conclusión más fuerte):**
Para exponer **todo** el sistema a una interfaz web de supervisión y control, **no
se cambió ni una línea del firmware** (Arduino ni NodeMCU): el dashboard reusa los
mismos comandos RPC que ya existían. **Esa es la prueba de que la separación en
capas —control / comunicación / presentación— fue la decisión correcta.** El
sistema cubre el ciclo completo: identificar la planta, diseñar el control,
integrarlo con la nube y operarlo por web.

---

## 5. Recap en una carilla

- **Sistema:** control de iluminación (LED+LDR en caja) con supervisión/control por
  internet. Lazo cerrado: e = r − y, corregido con PWM.
- **Etapa 1 — Planta:** circuito sensor (divisor LDR + 10k) y actuador (LED + 220Ω)
  en caja cerrada. Ensayo lazo abierto (PWM 0→150, y 187→804) → modelo de primer
  orden **K = 4,11, τ = 10 ms**. Modelo = punto de partida (planta no lineal).
- **Etapa 2 — Control:** PID (opera como PI, Kd = 0) en el Arduino, Ts = 2 ms.
  Sintonía IMC: Ti = τ, **Kp = 0,243, Ki = 24,33**. P deja error (planta tipo 0);
  PI lo elimina (**−91,6 %**). Diferencias sim-vs-real por no linealidad del LDR.
- **Etapa 3 — IoT:** NodeMCU de gateway (enlace serie con divisor, D5/D6). MQTT a
  ThingsBoard (token). Dos canales: telemetría (JSON, 500 ms) y RPC (comandos).
  Topics fijos de ThingsBoard (`v1/devices/me/...`).
- **Etapa 4 — Dashboard:** gráficos (y/r, u, e), indicadores (modo, online) y
  controles remotos (setpoint, Kp/Ki/Kd, modo). **Cero cambios de firmware** →
  valida la separación en capas.
- **Frase de cierre:** el TP cubre el ciclo completo de ingeniería de control, con
  componentes de bajo costo, y funciona de punta a punta.
