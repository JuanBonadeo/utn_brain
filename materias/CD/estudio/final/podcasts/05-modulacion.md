# Podcast CD 5 de 8 — Modulación: AM y mensajes digitales por una red analógica

Fuente para un episodio de podcast de estudio. Materia: Comunicación de Datos (UTN Facultad
Regional Rosario, Ingeniería en Sistemas, 3.er año). Sirve para rendir el final: tres problemas
de práctica y tres preguntas de teoría para desarrollar. Las respuestas de las preguntas son
respuestas modelo armadas por nosotros a partir de los apuntes de la cátedra, no la corrección
oficial.

## Indicaciones para el episodio

Qué es modular, AM y sus bandas laterales, y sobre todo ASK, FSK, PSK y QAM: cómo se ve cada una, cómo se aumenta la velocidad y dónde se usa (el módem, ADSL). Es la primera pregunta de teoría del final 2025.

## Contenido principal

### 6. Modulación

*Fuentes: apunte 5 (Comunicaciones Digitales), apunte 6 (ADSL) y El Santo Resumen.*

#### 6.1 Qué es modular

**Modular** es adaptar el mensaje al medio y **trasladarlo en frecuencia** a una portadora de alta frecuencia ($f_m \ll f_c$). La portadora es $A_c \cos(2\pi f_c t + \varphi_c)$, y se varía **un** parámetro por vez: la amplitud, la frecuencia o la fase.

#### 6.2 Modulación de amplitud (AM)

En AM, **la información del mensaje queda en las variaciones de amplitud de una onda senoidal de muy alta frecuencia llamada portadora**. Con un mensaje $A_m \cos 2\pi f_m t$:

$$x_{AM} = A_c \cos 2\pi f_c t + \frac{A_m}{2} \cos 2\pi (f_c - f_m) t + \frac{A_m}{2} \cos 2\pi (f_c + f_m) t$$

Aparecen la portadora y **dos bandas laterales**, inferior y superior, cada una con una copia del mensaje. Ejemplo: una emisora en 1230 kHz con una componente en 1260 kHz lleva un tono de 30 kHz.

| Variante | Qué se transmite | Ancho de banda | Para qué |
|---|---|---|---|
| **DSB** (doble banda lateral) | portadora + dos bandas | $2W$ | receptor barato: radiodifusión |
| **DSB-SC** (portadora suprimida) | dos bandas | $2W$ | ahorra potencia |
| **SSB** o BLU (banda lateral única) | una banda | $W$ | ahorra la mitad del espectro |
| **SSB-SC** | una banda, sin portadora | $W$ | máximo ahorro: móviles, punto a punto |

$W$ es el ancho del mensaje: $W = f_{max} - f_{min} \approx f_{max}$. Una sola banda alcanza para recuperarlo.

> **Ojo:** en el *multiple choice*, el mensaje queda "en la banda lateral **superior** y en la **inferior**". Portadora suprimida es "una AM donde **el espectro de la portadora no aparece después de modular**": la portadora sí se usa en el proceso.

#### 6.3 Mensajes digitales por una red analógica

Es la pregunta 1 de teoría del final 2025, con cuatro incisos.

**a) Los tipos.** Los bits **modulan una portadora analógica senoidal de alta frecuencia**:

| Técnica | Qué varía | "1" y "0" | Lo que dice la cátedra |
|---|---|---|---|
| **ASK** | amplitud | hay portadora / no hay | "**actualmente no se usa**": muy sensible al ruido |
| **FSK** | frecuencia | $f_1$ / $f_0$ | equivale a dos ASK superpuestas |
| **PSK** | fase | salto de 180° en cada transición | da más información que FSK en el mismo ancho de banda |

**Demodulación.** La **coherente** (sincrónica) genera en el receptor una portadora de igual frecuencia y fase, multiplica, filtra y regenera los pulsos; es más cara, y en FSK necesita las dos portadoras. La **incoherente** (detección de envolvente) existe para ASK y FSK. **PSK sólo se demodula en forma coherente.**

**b) Cómo aumentar la velocidad sin aumentar el ancho de banda: modulación multinivel.** Volvé a la fórmula de §3:

$$R = s \cdot \log_2 \mu$$

El ancho de banda depende de la velocidad de señalización $s$ (los baudios), así que el canal no deja subirla. Lo que sí se puede subir es la cantidad de **estados** por símbolo, $\mu$: cada símbolo pasa a llevar $\log_2 \mu$ bits.

- **FSK multinivel**: 2 frecuencias × 2 amplitudes = 4 estados → **2 bits por símbolo**.
- **PSK multinivel (QAM o APSK)**: fase y amplitud combinadas. **4 fases × 2 amplitudes = 8 estados → 3 bits por símbolo**.

Ejemplo *(QPSK y QAM-16 son conocimiento general; la cátedra usa el caso de 8 estados)*: a 2400 baudios, BPSK da 2400 bps, QPSK 4800 bps y QAM-16 9600 bps, **en el mismo ancho de banda**. El techo lo pone Shannon, $C = B \log_2 (1 + S/N)$: más estados exigen menos ruido. Subir la frecuencia de la portadora no sirve, porque sólo traslada el espectro.

**c) La aplicación: el MODEM.** Llevar los datos de una **computadora** (digital) por la **línea telefónica** (pensada para voz analógica). Hay un MODEM (MOdulador-DEModulador) en cada punta:

```
PC ── digital ──► MODEM ── analógica ──► red telefónica ── analógica ──► MODEM ── digital ──► PC
                  (D/A)                                                 (A/D)
```

El caso actual es **ADSL** *(conocimiento general, más allá del apunte)*: divide el par de cobre en unas 256 subportadoras y modula cada una en QAM con tantos bits como le permita su ruido. Es la modulación multinivel llevada a la práctica. Las bandas están en §7.5.

**d) Las gráficas que hay que hacer:**

1. ASK, FSK y PSK para una misma secuencia de bits (Figura 10).
2. El espectro ASK: la sinc del tren de pulsos (§7.3) trasladada a ambos lados de $f_c$, con un ancho de unos $2/\tau$. FSK son dos espectros ASK, en $f_0$ y en $f_1$.
3. La tabla de estados de FSK multinivel o la constelación de 8 puntos.
4. El esquema PC → MODEM → red → MODEM → PC.

> **Ojo:** en el *multiple choice*, "modular en amplitud, frecuencia o fase una **portadora analógica de alta frecuencia**", y para acelerar sin más ancho de banda, "**aumentar el número de niveles**". Un resumen de alumnos dice que PSK se demodula en forma asincrónica y que la PSK multinivel tiene "dos fases y cuatro amplitudes": las dos cosas están al revés en el apunte.

## Preguntas reales de teoría de los finales, con su respuesta

### 5. Comunicaciones digitales: modulación

#### 5.1 Mensaje digital por una red analógica: tipos, aplicación, cómo aumentar la velocidad, gráficas
**Salió:** **04/04/2025** (desarrollo: "a) Qué tipos de modulación se aplican para transmitir mensajes digitales por una red que transporta señales analógicas; b) cómo se aumenta la velocidad; c) cuál es su principal aplicación práctica; d) hacer todas las gráficas"); 28/08/2020 y 10/09/2021 (MC "Si se tiene que transmitir una señal digital por una red que opera con señales analógicas se debe…"); 18/12/2020 (MC "Para aumentar la velocidad de una FSK o PSK sin aumentar el ancho de banda del canal se debe…"); FAQ, con seis variantes de la misma pregunta ("Modulación FSK, PSK y multinivel. Gráficas y aplicación", "Explicar modulación con señal digital y portadora analógica…", "Aplicación de modulación analógica con mensaje digital…", "¿Cómo se puede transmitir una señal digital por un canal analógico?…", "Explique ASK conceptualmente y realice los gráficos", "Demodulación ASK coherente").

**Respuesta.**

**a) Tipos.** El mensaje digital (los bits) **modula una portadora analógica senoidal de alta frecuencia** ($f_c\gg$ que la frecuencia del mensaje), variando **uno** de sus parámetros:
- **ASK** (*Amplitude Shift Keying*): varía la **amplitud**, con frecuencia y fase constantes. "1" → hay portadora; "0" → no hay portadora ($1\cdot$portadora / $0\cdot$portadora). **Actualmente no se usa** porque es muy sensible al ruido.
- **FSK** (*Frequency Shift Keying*): varía la **frecuencia**, con amplitud y fase constantes. "1" → $f_1$, "0" → $f_0$. Equivale a dos ASK superpuestas de distinta portadora.
- **PSK** (*Phase Shift Keying*): varía la **fase**, con amplitud y frecuencia constantes. Hay un cambio de fase (180°) en cada transición 1→0 o 0→1. Se genera multiplicando la señal binaria bipolar por la portadora y suministra más información que FSK en el mismo ancho de banda.

**Demodulación:**
- **Sincrónica o coherente:** el receptor necesita la portadora **en sincronismo** con la del emisor (misma frecuencia y fase). Multiplica, filtra con un pasabajos y regenera. Es más cara. En FSK hacen falta las dos portadoras.
- **Asincrónica o incoherente** (detección de envolvente con rectificador y filtro): existe para ASK y FSK. **PSK solo se demodula en forma coherente** ("no existe incoherente").

**b) Cómo se aumenta la velocidad (sin aumentar el ancho de banda): modulación multinivel.** Con $n$ estados distinguibles por símbolo, cada símbolo lleva $\lg n$ bits: $R=s\cdot\lg n$. El ancho de banda depende de la velocidad de señalización $s=1/\tau$, que no cambia, así que se mandan más bits por segundo en el mismo canal. Subir la frecuencia de la portadora o la de muestreo no sirve.
- **FSK multinivel:** 2 frecuencias × 2 amplitudes = 4 estados → **2 bits por símbolo** (00, 01, 10, 11 en el tiempo en que antes iba 1 bit).
- **PSK multinivel (QAM o APSK):** se combinan **fase y amplitud**. Con **4 fases × 2 amplitudes = 8 estados → 3 bits por símbolo**.
- Límite: más estados implican estados más "juntos" y más sensibles al ruido. Shannon fija el techo con $C=B\lg(1+S/N)$.

**c) Aplicación práctica:** transmitir datos de una **computadora (señal digital) por la línea telefónica (red pensada para señales analógicas de voz)**. Se usa un **MODEM** (MOdulador-DEModulador) en cada extremo: convierte digital → analógico al transmitir y analógico → digital al recibir. También se aplica a canales telegráficos y de voz.

```
  PC ──digital──► MODEM ──analógica──► RED TELEFÓNICA ──analógica──► MODEM ──digital──► PC
                  (D/A)                                              (A/D)
```

**d) Gráficas.**

Formas de onda para el mismo mensaje (bits `1 0 1 1 0`):
```
 bits     │  1  │  0  │  1  │  1  │  0  │
 mensaje   ┌─────┐     ┌───────────┐
           │     │     │           │
          ─┘     └─────┘           └─────

 ASK      ∿∿∿∿∿∿ ────── ∿∿∿∿∿∿∿∿∿∿∿∿ ──────     portadora solo en los "1"

 FSK      ∿∿∿∿∿∿ ⌒⌒⌒⌒⌒⌒ ∿∿∿∿∿∿∿∿∿∿∿∿ ⌒⌒⌒⌒⌒⌒     f1 (alta) = "1", f0 (baja) = "0"

 PSK      ∿∿∿∿∿∿|∿∿∿∿∿∿|∿∿∿∿∿∿∿∿∿∿∿∿|∿∿∿∿∿∿     "|" = salto de fase de 180° en cada transición
```

Espectro ASK: un tren de pulsos de ancho $\tau$ tiene un espectro $\text{sinc}$ con la mayor parte de la energía entre 0 y $1/\tau$. Al modular, ese espectro se traslada a ambos lados de $f_c$:
```
  A │                  │ (portadora)
    │            ╱╲    │    ╱╲
    │        ╱╲ ╱  ╲   │   ╱  ╲ ╱╲
    └───────┴──┴────┴──┴──┴────┴──┴────── f
          fc−1/τ       fc       fc+1/τ
                 ◄─── Bw ≈ 2/τ ───►
```
Espectro FSK: dos espectros ASK, uno centrado en $f_0$ y otro en $f_1$.

Multinivel:
```
 FSK multinivel (2 frec × 2 ampl)       PSK multinivel / QAM (4 fases × 2 amplitudes = 8 estados)
  00 → f1, A1                                         90°
  01 → f1, A2                                          ● 011
  10 → f2, A1                                          ○ 010
  11 → f2, A2                          180° ● ○                  ○ ● 0°
                                           101 100            000 001
                                                       ○ 110
                                                       ● 111
                                                      270°
                                       ○ amplitud menor   ● amplitud mayor   → 3 bits/símbolo
```

**En los MC:**
- "Modular en amplitud, frecuencia o fase una **portadora analógica de alta frecuencia**" (no de baja frecuencia, no portadora digital).
- Para aumentar la velocidad sin aumentar el BW: "**aumentar el número de niveles (multinivel)**".

(teoria/5 - Comunicaciones Digitales.md; teoria/1 - Información, Codificación y Canales.md; resumenes/El Santo Resumen/el-santo-resumen.md, sección Final)

#### 5.2 Modulación de amplitud (AM): definición, ubicación del mensaje, portadora suprimida, banda lateral única
**Salió:** definición en 28/08/2020, 18/12/2020, 10/09/2021; "dónde queda la banda del mensaje" en 18/12/2020, 19/11/2021, 17/12/2021; portadora suprimida en 19/11/2021 y 17/12/2021 (MC).

**Respuesta.**
- **AM:** la información del mensaje queda contenida en las **variaciones de amplitud de una onda senoidal de muy alta frecuencia llamada portadora**. Modular es "adaptar" el mensaje al medio y **trasladarlo en frecuencia** ($f_m\ll f_c$; p. ej., radio AM: voz de 20 Hz–20 kHz sobre una portadora de unos 1000 kHz).
- Con mensaje $x_m=A_m\cos 2\pi f_m t$ y portadora $x_c=A_c\cos2\pi f_c t$:
$$x_{AM}=(A_c+A_m\cos2\pi f_mt)\cos2\pi f_ct = A_c\cos2\pi f_ct+\tfrac{A_m}{2}\cos2\pi(f_c-f_m)t+\tfrac{A_m}{2}\cos2\pi(f_c+f_m)t$$
Aparecen tres componentes: la portadora en $f_c$ y dos rayas de amplitud $A_m/2$ en $f_c\pm f_m$.
- **Dónde queda el mensaje:** para un mensaje con banda $[f_{min}, f_{max}]$, su espectro aparece **dos veces**, en la **banda lateral superior** ($f_c+f_{min}$ a $f_c+f_{max}$) y en la **banda lateral inferior** ($f_c-f_{max}$ a $f_c-f_{min}$, invertida). **No queda nada en banda base.** Ancho de banda DSB $=2f_{max}=2W$.
```
  A │                      Ac
    │        BLI           │          BLS
    │       ╱‾‾‾│          │          │‾‾‾╲
    │      ╱    │          │          │    ╲
    └─────┴─────┴──────────┴──────────┴─────┴──── f
       fc−fmax  fc−fmin    fc    fc+fmin  fc+fmax
             ◄──────────── 2·fmax ───────────►
```
- **Variantes** (una sola banda alcanza para recuperar frecuencia y amplitud de cada componente):
  - **DSB** (doble banda lateral, con portadora): $B=2W$. Receptor barato, para llegar a muchos receptores (radiodifusión).
  - **DSB-SC** (portadora suprimida): $x_m\cdot x_c=\tfrac{A_mA_c}{2}[\cos2\pi(f_c-f_m)t+\cos2\pi(f_c+f_m)t]$. **La portadora se usa para modular, pero no aparece en el espectro después de modular.** Ahorra potencia.
  - **SSB o BLU** (banda lateral única): $B=W$. Ocupa la mitad del espectro.
  - **SSB-SC:** una banda sin portadora; máximo ahorro de energía (equipos móviles, punto a punto).

**En el MC:**
- Definición: "…variaciones de amplitud de una onda senoidal de **muy alta** frecuencia llamada portadora" (no baja frecuencia, no amplitud+frecuencia+fase, no tren de pulsos).
- Banda del mensaje: "en la banda lateral **superior** y en la banda lateral **inferior** de la portadora".
- Portadora suprimida: "una modulación de amplitud donde **el espectro de la portadora no aparece después de modular**". "No se requiere la portadora en el proceso" es falso: se multiplica por ella.

(teoria/5 - Comunicaciones Digitales.md)

#### 5.3 Ancho de banda práctico de una señal digital real
**Salió:** FAQ ("¿Cuál es el ancho de banda práctico ocupado por una señal digital real? Explique").

**Respuesta.** Una señal digital real es un tren de pulsos de ancho $\tau$. Por Fourier, su espectro es una envolvente $\text{sinc}$ con armónicas separadas por la frecuencia del tren ($1/T$), y en teoría es **infinito**. Las armónicas de mayor amplitud están entre 0 y el primer cruce por cero, en $1/\tau$. En la práctica **se recorta el espectro en $1/\tau$**: ahí está la mayor parte de la energía y alcanza para reconstruir el pulso.
$$W_{práctico}=\frac{1}{\tau}$$
El canal debe tener un ancho de banda mayor o igual a ese cruce por cero. Modulada en ASK, la señal ocupa $\approx 2/\tau$.

```
 |X(f)| │█
        │█▇
        │█▇▅▃
        │█▇▅▃▁    ▁▂▂▁         ▁▁
        └──────────┴───────────┴────── f
        0        1/τ          2/τ
        ◄─ W práctico ─►
```

Ojo: el apunte 1 da también $B=s/2$ (ver Dudas).

(teoria/5 - Comunicaciones Digitales.md)

#### 5.4 Banda ancha y espectro del mensaje
**Salió:** FAQ ("Concepto de banda ancha y concepto de espectro de mensaje (o señal). Dar en un solo ejemplo cómo se aplican").

**Respuesta.**
- **Espectro del mensaje:** representación del mensaje en función de la frecuencia (por Fourier, la suma de sus componentes senoidales con sus amplitudes). Ocupa una **banda** $w=f_{max}-f_{min}\approx f_{max}$ si $f_{min}$ es despreciable. Por ejemplo, la voz telefónica va de 300 Hz a 3,4 kHz.
- **Banda base vs. banda ancha:** en **banda base** el mensaje se transmite con su espectro original, **sin corrimiento en frecuencia**, y es una sola transmisión por el canal. En **banda ancha** el canal lleva **varias señales en canales (bandas) distintos**: cada mensaje se traslada con su portadora a una porción del ancho de banda del canal (modulación + FDM).
- **Ejemplo único (ADSL sobre el par telefónico):** el mismo par lleva la voz **en banda base** (0–4 kHz) y los datos en bandas trasladadas: subida de 25,875 a 138 kHz y bajada de 138 a 1104 kHz. El canal (par de cobre) tiene un ancho de banda mayor que el espectro de cada mensaje y se reparte en bandas, cada una ocupada por el espectro de una señal.

(resumenes/El Santo Resumen/el-santo-resumen.md, "Banda base y modulación" y ADSL, que citan el apunte «Principios Básicos» y teoria/6 - Espectro de la señal ADSL; teoria/5 - Comunicaciones Digitales.md)
