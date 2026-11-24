# Podcast CD 6 de 8 — Muestreo, PCM y multiplexado: TDM, FDM y ADSL

Fuente para un episodio de podcast de estudio. Materia: Comunicación de Datos (UTN Facultad
Regional Rosario, Ingeniería en Sistemas, 3.er año). Sirve para rendir el final: tres problemas
de práctica y tres preguntas de teoría para desarrollar. Las respuestas de las preguntas son
respuestas modelo armadas por nosotros a partir de los apuntes de la cátedra, no la corrección
oficial.

## Indicaciones para el episodio

Nyquist, las etapas de PCM, la trama TDM y su ancho de banda (el problema que sale en casi todos los finales), FDM y el reparto de frecuencias de ADSL. Aclará que hay dos criterios para el ancho de banda (1/τ y s/2) y por qué conviene declarar cuál se usa.

## Contenido principal

### 7. Muestreo, PCM y multiplexado

*Fuentes: apunte 5 (Comunicaciones Digitales, págs. 9–10 y 21–24), apunte 6 (ADSL), Ejercitación Comunicación Digital y "Fórmulas y pasos". El ejercicio de PCM sale en 8 de cada 9 finales.*

#### 7.1 Muestreo y PCM

Para digitalizar un mensaje analógico, **el primer paso es muestrearlo** con un tren de pulsos: quedarse con su valor cada $T_s = 1/f_s$. Al muestrear, el espectro del mensaje (de ancho $w$) se **repite** alrededor de $f_s$, $2f_s$, etc. Para recuperarlo, la primera copia no puede pisar al original:

$$f_s - w \ge w \;\Rightarrow\; f_s \ge 2w \approx 2 f_{max} \qquad \text{(teorema de Nyquist)}$$

Si no, las copias se superponen (*aliasing*). Conviene la $f_s$ **mínima**: un $T_s$ más largo deja lugar para más muestras de otros mensajes.

Con portadora digital, el mensaje modula un parámetro del pulso: la amplitud (**PAM**), la duración (**PDM**) o la posición (**PPM**). **PCM** va un paso más allá: cuantifica y codifica cada muestra.

1. **Muestreo** a $f_s \ge 2 f_{max}$.
2. **Cuantificación**: cada muestra se redondea al **nivel cuántico** más cercano. El intervalo de cada nivel es el **cuanto**. Ejemplo del apunte: de −4,5 a 4,5 con 7 niveles separados 1,5.
3. **Codificación**: cada nivel se escribe con $n$ dígitos binarios (con 7 u 8 niveles, $n = 3$).
4. **Multiplexado TDM** de varias señales en una trama, con sincronismo y señalización.

Ejemplo real: la **PCM 30 + 2** lleva 30 canales de voz y 2 de sincronismo y señalización: $32 \cdot 8 \cdot 8000 = 2{,}048$ Mbps *(conocimiento general: es el E1)*.

> **Ojo:** en el *multiple choice*, "muestrear el mensaje con un tren de pulsos digital con una frecuencia **mínima** igual al **doble de la frecuencia máxima** del mensaje". No una portadora analógica, ni el doble de la mínima, ni codificar primero.

#### 7.2 TDM y la trama

**TDM** (multiplexación por división de tiempo) reparte el canal **en el tiempo**. Entre dos muestras de un mensaje queda un tiempo muerto, y ahí se intercalan las de los otros. **Durante su ranura, cada muestra ocupa todo el ancho de banda del canal.** Un conmutador en el emisor toma las muestras y otro en el receptor, **sincronizado**, las reparte.

La **trama** es una muestra de cada mensaje más las de control, y dura un período de muestreo:

| Símbolo | Qué es | Relación |
|---|---|---|
| $N$ | muestras por trama, **incluidas las de control** | — |
| $n$ | bits por muestra | — |
| $T_s$ | duración de la trama | $T_s = 1/f_s = N \cdot T_M$ |
| $T_M$ | duración de una muestra | $T_M = n \cdot \tau$ |
| $\tau$ | ancho de cada pulso | $\tau = 1/(N\, n\, f_s)$ |
| $B_w$ | ancho de banda | $B_w = 1/\tau = N \cdot n \cdot 2 f_{max}$ |

#### 7.3 El ancho de banda de un tren de pulsos

Un pulso rectangular de ancho $\tau$ tiene un espectro con forma de **sinc**. En teoría es infinito, pero casi toda la energía está antes del **primer cruce por cero**, en $1/\tau$, y en la práctica se recorta ahí.

| Criterio | Fórmula | De dónde sale | Cuándo |
|---|---|---|---|
| Primer cruce por cero | $B_w = 1/\tau$ | apunte 5, pág. 24 | **ejercicio de PCM/TDM** (guía y resoluciones) |
| Mínimo de Nyquist | $B = s/2 = 1/(2\tau)$ | apunte 1, pág. 12 | canal binario, $C = s$ |

**En el examen usá $1/\tau$ y escribí que es el primer cruce por cero de la sinc.** Con el otro criterio todos los anchos se dividen por 2. Modulada en ASK, la señal ocupa unos $2/\tau$.

#### 7.4 Ejercicio resuelto: final 2025

**Enunciado** (04/04/2025, igual al 19/11/2021). Una trama PCM tiene 25 muestras de información y 2 de control. Las señales van de 400 a 3500 Hz y cada muestra se codifica con 7 dígitos. Calcular el ancho de banda para transmitir la trama, graficar e indicar la técnica.

**Datos.** $N = 25 + 2 = 27$ (las de control también ocupan ranura); $n = 7$; $f_{max} = 3500$ Hz.

1. **Técnica**: **multiplexado TDM con modulación PCM** (muestreo, cuantificación y codificación binaria).
2. **Nyquist**: $f_s = 2 f_{max} = 7000$ Hz, así que la trama dura $T_s = 1/7000 = 142{,}86\ \mu\text{s}$.
3. **Una muestra**: $T_M = T_s/N = 142{,}86/27 = 5{,}291\ \mu\text{s}$.
4. **Un pulso**: $\tau = T_M/n = 5{,}291/7 = 0{,}756\ \mu\text{s}$.
5. **Ancho de banda**:
$$B_w = \frac{1}{\tau} = N \cdot n \cdot 2 f_{max} = 27 \cdot 7 \cdot 7000 = \mathbf{1\,323\,000\ \text{Hz} \approx 1{,}323\ \text{MHz}}$$
6. **Gráficos**: el mensaje con los instantes de muestreo; el espectro muestreado con las réplicas en $f_s$ y la condición $f_s \ge 2 f_{max}$; la trama de 27 ranuras (Figura 13); una muestra de 7 pulsos de ancho $\tau$; la sinc con el primer cero en $1/\tau$ (Figura 14).

**Criterios a declarar.** Se muestreó con $2 f_{max}$, como el apunte y la guía, porque $f_{min} = 400$ Hz es chica. Con $w = 3100$ Hz daría 1,172 MHz, pero muestrear a $2w$ sólo funciona en casos particulares *(conocimiento general)*. Con el criterio $s/2$ daría 661,5 kHz.

**Otras variantes:**

| Final | Qué piden | Resultado |
|---|---|---|
| 18/12/2015, 21/02/2020, 28/08/2020 | 32 señales de 4 kHz, 8 bits | $B_w = 32 \cdot 8 \cdot 8000 =$ **2,048 MHz** |
| 10/09/2021 (inverso) | 900 señales en 2 MHz, 7 bits: ¿$W$ de cada una? | $W = B_w/(2Nn) =$ **158,7 Hz** |
| 09/03/2012 | canal de 100 a 300 MHz, $f_s = 8$ kHz, 8 bits: ¿cuántas señales? | $N = 200 \times 10^6/(8 \cdot 8000) =$ **3125** |
| 03/03/2006 | 6 señales de distinta $f_{max}$ (la mayor, 20 kHz) en 2,4 MHz: ¿bits por muestra? | todas a la $f_s$ de la más rápida (40 kHz): $n =$ **10 bits** |

> **Ojo:** en $N$ van **todas** las muestras ("25 + 2" son 27). Si piden cuántas señales entran, se redondea **para abajo**. Si no dan bits por muestra, no es TDM: es FDM.

#### 7.5 FDM y ADSL

**FDM** (multiplexación por división de frecuencia): cada señal **modula una portadora distinta**, así que todas **viajan simultáneamente** y cada una ocupa **una banda determinada dentro del ancho de banda del canal**. En recepción, filtros pasabanda separan cada canal.

$$\text{DSB: } B_w = N \cdot 2W \qquad\qquad \text{SSB: } B_w = N \cdot W$$

**Para duplicar la cantidad de señales en el mismo canal hay que transmitir en banda lateral única.** Suprimir la portadora ahorra potencia, no espectro.

| | FDM | TDM |
|---|---|---|
| Qué se reparte | la **frecuencia**: cada señal tiene su banda | el **tiempo**: cada señal tiene su ranura |
| Simultaneidad | todas a la vez | una muestra por vez |
| Ancho de cada señal | sólo su banda ($2W$ o $W$) | **todo** el canal, en su ranura |
| Portadora | analógica, una por señal | tren de pulsos, único |
| Separación | filtros pasabanda | conmutador sincronizado |
| Ejemplos | radio AM y FM, ADSL | PCM 30 + 2 |

**"¿Cada mensaje ocupa un lugar determinado del ancho de banda?"** En FDM sí: su banda. En TDM no: usa todo el canal, y lo que tiene asignado es un lugar en el **tiempo**.

**Ejercicio tipo FDM.** Cuatro señales telefónicas de 300 a 3400 Hz por un canal que arranca en 400 kHz. En DSB cada una ocupa 6,8 kHz y $B_w = 4 \cdot 6{,}8 =$ **27,2 kHz**: el canal va de 400 a 427,2 kHz, con las portadoras en el centro de cada banda (403,4; 410,2; 417 y 423,8 kHz). En SSB, **13,6 kHz**.

> **Ojo:** con señales que no arrancan en 0, la respuesta oficial del final 18/02/2011 usa $2 f_{max}$ por señal, no $2W$; El Santo Resumen usa $N \cdot 2W$. Seguí la oficial y aclaralo.

**ADSL: el reparto del par de cobre** (apunte 6).

| Banda | Rango | Ancho | Uso |
|---|---|---|---|
| Voz | 0 – 4 kHz | 4 kHz | telefonía, en banda base |
| Guarda | 4 – 25,875 kHz | — | separa voz y datos |
| Subida | 25,875 – 138 kHz | 112,1 kHz | cliente → red |
| Bajada | 138 – 1104 kHz | 966 kHz | red → cliente |

Es **asimétrico**: la bajada tiene unas 8,6 veces más espectro que la subida, porque el usuario típico descarga mucho más de lo que sube.

**Cómo reconocer el ejercicio.** Si dan bits por muestra o hablan de trama o canal digital → **TDM-PCM**. Si piden señales analógicas simultáneas por un canal analógico y no dan bits → **FDM con AM**.

## Preguntas reales de teoría de los finales, con su respuesta

### 6. Muestreo, digitalización y PCM

#### 6.1 ¿Qué hay que hacer primero para digitalizar un mensaje analógico? (Nyquist)
**Salió:** 28/08/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC); TDM "las señales se muestrean con…" en 28/08/2020 y 18/12/2020 (MC); FAQ ("Cómo digitalizar una señal analógica").

**Respuesta.** El primer paso es **muestrear** el mensaje con un **tren de pulsos (portadora digital) de frecuencia $f_s\ge 2f_{max}$** del mensaje (**tasa de Nyquist** o teorema del muestreo).

**Por qué:** muestrear (PAM) es multiplicar el mensaje por un tren de pulsos. El espectro del mensaje (ancho $w$) se repite alrededor de $0, f_s, 2f_s,\dots$. Para que la copia centrada en $f_s$ no se superponga con la original hace falta $f_s-w\ge w$, es decir, $f_s\ge 2w\approx 2f_{max}$. Si no, hay superposición (aliasing) y el mensaje no se recupera.
```
 │ ┌──┐            ┌──┬──┐            ┌──┬──┐
 │ │  │            │  │  │            │  │  │
 └─┴──┴──────...───┴──┴──┴─────...────┴──┴──┴─── f
 0    w        fs−w  fs  fs+w     2fs−w 2fs
     sin superposición  ⇔  fs − w ≥ w  ⇔  fs ≥ 2·fmax
```
Conviene bajar $f_s$ al mínimo posible: un período $T_s=1/f_s$ más largo deja lugar para más muestras de otros mensajes (TDM).

Etapas de la digitalización: **muestreo → cuantificación → codificación** (→ multiplexado TDM y código de línea).

**En el MC:** "Muestrear el mensaje con un tren de pulsos digital con una frecuencia **mínima** igual al **doble de la frecuencia máxima** del mensaje". No con una portadora analógica, no al doble de la frecuencia mínima, y no codificar primero.

(teoria/5 - Comunicaciones Digitales.md)

#### 6.2 PCM (modulación por pulsos codificados)
**Salió:** 18/12/2020 (MC "En una transmisión PCM las muestras de cada señal…"); FAQ (PCM en Parte 2).

**Respuesta.** Primero, las técnicas de portadora digital con mensaje analógico: el mensaje modula un parámetro de cada pulso.
- **PAM:** varía la amplitud.
- **PDM:** varía la duración.
- **PPM:** varía la posición.

**PCM** es la cuarta técnica y la que se usa hoy: la amplitud de cada muestra PAM se **cuantifica y codifica**.
1. **Muestreo** a $f_s\ge2f_{max}$.
2. **Cuantificación:** las muestras pueden tomar infinitos valores, pero solo se puede codificar un número finito. Se preestablecen **niveles cuánticos** y cada muestra se redondea al nivel más cercano. El intervalo asociado a cada nivel es el **cuanto**. Ejemplo del apunte: rango $[-4{,}5;\,4{,}5]$ con niveles $-4{,}5;\,-3;\,-1{,}5;\,0;\,1{,}5;\,3;\,4{,}5$.
3. **Codificación:** cada nivel se representa con una palabra de $n$ dígitos binarios (con 7–8 niveles, $n=3$).
4. **Multiplexado TDM** de muestras de varios canales en una **trama**: la PCM 30+2 lleva 30 canales de información y 2 de sincronismo y señalización.

Cuentas: $T_s=1/f_s=N\cdot T_M$, $T_M=n\cdot\tau$, $B_w=1/\tau=N\cdot n\cdot f_s$.

```
 Muestreadores → MUX (PAM/TDM) → Cuantificador → MUX sinc./señalización → Codificador de línea → señal PCM
```

**En el MC:** "Se codifican y se transmiten a una velocidad del doble de la frecuencia máxima del mensaje". Las muestras de cada señal salen a $f_s=2f_{max}$ muestras/s y se codifican **en el emisor**, no en el receptor.

(teoria/5 - Comunicaciones Digitales.md)

### 7. Multiplexación

#### 7.1 FDM: concepto
**Salió:** 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC); FAQ.

**Respuesta.** **Multiplexación por división de frecuencia:** cada señal **modula una portadora distinta y única** ($f_{c1}, f_{c2},\dots$), así que todas **viajan simultáneamente** por el mismo canal y cada una ocupa **una banda de frecuencia determinada dentro del ancho de banda del canal**. Los mensajes no se mezclan porque cada uno queda a ambos lados de su propia portadora, con separación suficiente (bandas de guarda). En recepción, filtros pasabanda separan cada canal y se demodula.

**En el MC:** "Las señales viajan simultáneamente y ocupan una determinada banda de frecuencia dentro del ancho de banda del canal". "Time slice" y "muestrean a 2·fmax ocupando todo el BW" describen TDM.

(teoria/5 - Comunicaciones Digitales.md)

#### 7.2 FDM con AM: ancho de banda para N señales y cómo duplicar la cantidad de señales
**Salió:** 19/11/2021, 17/12/2021 (dos MC).

**Respuesta.** Con $N$ señales de frecuencia máxima $W=f_{max}$ (si $f_{min}\ll f_{max}$):
$$\text{DSB (doble banda lateral): } B_w=N\cdot 2W \qquad\qquad \text{SSB/BLU: } B_w=N\cdot W$$
```
 DSB: │[BLI|BLS][BLI|BLS][BLI|BLS][BLI|BLS]│      N·2W
         fc1      fc2      fc3      fc4
 SSB: │[BLS][BLS][BLS][BLS][BLS][BLS][BLS][BLS]│   N·W → en el mismo canal entran 2N señales
```
Por lo tanto, **para duplicar la cantidad de señales en el mismo canal hay que transmitir en banda lateral única**. Suprimir solo la portadora ahorra potencia pero no ancho de banda. Duplicar la frecuencia de la portadora solo traslada el espectro, y la frecuencia de muestreo o los bits por muestra son conceptos de TDM/PCM.

**En el MC:**
- Ancho de banda: "Respuestas **C y E**" ($N\cdot f_{max}$ para BLU y $N\cdot2f_{max}$ para DBL).
- Duplicar: "**transmitiendo en banda lateral única**".

(teoria/5 - Comunicaciones Digitales.md)

#### 7.3 TDM: concepto, trama y diferencia con FDM
**Salió:** 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC "En una transmisión con multiplexado TDM las señales…"); FAQ ("Explique detalladamente la técnica TDM", "Explicar la diferencia entre FDM y TDM. Ejemplo con gráfico", "¿En una transmisión, cada mensaje ocupa un lugar determinado del ancho de banda del canal? ¿Por qué?").

**Respuesta.**
- **TDM (multiplexación por división de tiempo):** se divide el uso del canal **en el tiempo**. Se muestrea cada mensaje ($f_s\ge2f_{max}$) y, como entre pulsos queda un **tiempo muerto**, ahí se intercalan muestras de los otros mensajes. Los usuarios toman su turno en forma circular y, **en su intervalo, cada muestra ocupa todo el ancho de banda del canal**, una por vez: no hay simultaneidad.
- **Trama:** el conjunto de una muestra de cada mensaje. Dura $T_s=1/f_s$ y lleva además pulsos o canales de **sincronismo**.
- **Esquema:** un conmutador rotativo C1 toma muestras alternadas de cada canal, y en recepción otro conmutador C2 **sincronizado** con el emisor las reparte.

```
 A ─┐                                   ┌─ A'
 B ─┤  C1 ⟳ ──── medio físico ──── ⟳ C2 ├─ B'
 C ─┘           (sincronismo)            └─ C'

 canal │ A1 │ B1 │ C1 │ S │ A2 │ B2 │ C2 │ S │ A3 …
       │◄──── trama Ts = 1/fs ────►│
```

| | FDM | TDM |
|---|---|---|
| Recurso que se reparte | La **frecuencia**: cada señal tiene su banda | El **tiempo**: cada señal tiene su ranura |
| Simultaneidad | Todas viajan a la vez | Una muestra por vez |
| Ancho de banda que ocupa cada señal | Solo su banda (2W o W) | **Todo** el BW del canal durante su ranura |
| Portadora | Analógica, distinta por señal | Tren de pulsos (digital), único |
| Separación en recepción | Filtros pasabanda | Conmutador sincronizado |
| Ejemplo | Radio AM/FM, ADSL | PCM 30+2 (telefonía digital) |

```
 FDM:  f │ ████████████ señal 3          TDM:  f │ █ █ █ █ █ █ █ █
         │ ████████████ señal 2                  │ █ █ █ █ █ █ █ █
         │ ████████████ señal 1                  │ A B C A B C A B
         └──────────────── t                     └──────────────── t
```

**¿Cada mensaje ocupa un lugar determinado del ancho de banda?** **Depende de la técnica.** En **FDM sí**: cada mensaje ocupa una banda fija dada por su portadora, para que no se superpongan los espectros y se puedan separar y demodular. En **TDM no**: cada muestra usa **todo** el ancho de banda, y lo que tiene asignado es un **lugar determinado en el tiempo** (su ranura dentro de la trama).

**En el MC:**
- "Se transmiten muestras de cada señal en un tiempo determinado **ocupando todo el ancho de banda del canal**".
- "Las señales se muestrean con una frecuencia mínima igual al doble de la frecuencia **máxima** del mensaje".

(teoria/5 - Comunicaciones Digitales.md)
