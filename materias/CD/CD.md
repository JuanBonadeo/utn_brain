# Comunicación de Datos — Wiki

> Materia de 3° (pendiente: se rinde el final). Cátedra: teoría **Jorge Alberto Campanaro**, práctica **Germán Baró** (según `archivo/LEER.pdf`). En los finales viejos aparece como "Comunicaciones".
>
> **Formato del final (último disponible, 04/04/2025):** dos partes.
> - **Práctica:** 3 problemas (transmisión multinivel, trama PCM y ancho de banda, teoría de colas M/M/1).
> - **Teoría:** 3 preguntas para desarrollar (modulación digital sobre red analógica, propiedades de los códigos, medios de acceso y cómo elegirlos).

## Índice
1. Unidad 1 — Teoría de la información: información, entropía, canales
2. Unidad 2 — Codificación: códigos unívocos, instantáneos, Kraft, compactos
3. Unidad 3 — Detección y corrección de errores: códigos lineales
4. Unidad 4 — Comunicaciones digitales: transmisión multinivel, PCM, modulación, ADSL
5. Unidad 5 — Medios de transmisión, multiplexación (CDM, WDM) y elección del medio de acceso
6. Unidad 6 — Asignación de capacidad de canales y teoría de colas
7. Unidad 7 — Modelo OSI, TCP/IP y hardware de redes

**Cómo está armada cada unidad:** Conceptos clave → Desarrollo → Ejercicios resueltos tipo → Dudas / pendientes → Fuentes.

## Desarrollo

### Unidad 1 — Teoría de la información: información, entropía, canales
*Pendiente de ingesta.*

### Unidad 2 — Codificación: códigos unívocos, instantáneos, Kraft, compactos
*Pendiente de ingesta.*

### Unidad 3 — Detección y corrección de errores: códigos lineales
*Pendiente de ingesta.*

### Unidad 4 — Comunicaciones digitales: transmisión multinivel, PCM, modulación, ADSL

#### Conceptos clave
- **Modular** = adaptar el mensaje al medio y trasladarlo en frecuencia a una portadora de alta frecuencia ($f_m \ll f_c$). Siempre **el mensaje modula a la portadora**.
- Tres combinaciones de la cátedra: (I) mensaje analógico / portadora analógica → AM, FM, PM (+ FDM); (II) mensaje digital / portadora analógica → ASK, FSK, PSK (MODEM); (III) mensaje analógico / portadora digital → PAM, PDM, PPM, **PCM** (+ TDM).
- **Multinivel**: $M(T)=\mu^{n}$, $I=\lg M(T)=n\lg\mu$ [bits], $R=I/T$ [bps]. $T$ incluye arranque y parada; $n$ cuenta sólo los pulsos de información.
- **Nyquist (muestreo)**: $f_s \ge 2 f_{max}$. **Trama TDM**: $T_s = N\,T_M = N\,n\,\tau = 1/f_s$ ⇒ $B_w = 1/\tau = N\,n\,f_s = N\,n\,2f_{max}$.
- **FDM**: DSB $B_w = N\cdot 2W$; SSB $B_w = N\cdot W$, con $W=f_{max}-f_{min}\approx f_{max}$.
- **Para aumentar la velocidad** de un módem sin tocar el ancho de banda: **multinivel** (FSK multinivel, PSK multinivel = QAM/APSK). ASK "no se usa".
- Demodulación: coherente (sincrónica, necesita portadora local en sincronismo, más cara) o incoherente (detección de envolvente). **PSK sólo coherente**.
- **ADSL** = FDM sobre el par de cobre del abonado: voz 0–4 kHz, subida 25,875–138 kHz, bajada 138–1104 kHz (asimétrico).

#### Desarrollo

##### 1. Transmisión multinivel
Ejemplo primero: 6 pulsos que pueden valer +2 V o −2 V → $\mu=2$, $n=6$, $M=2^6=64$ mensajes distintos, $I=\lg 64=6$ bits. Si en vez de 2 niveles uso 7 (−3…+3), con los mismos 6 pulsos: $M=7^6=117.649$, $I = 6\lg 7 = 16{,}84$ bits. **Más niveles en el mismo tiempo = más información.**

Fórmulas (apunte de Principios Básicos + "Fórmulas y pasos"):

| Magnitud | Fórmula | Unidad |
|---|---|---|
| Mensajes distintos | $M(T)=\mu^{n}=\mu^{t/\tau}$ | — |
| Información | $I=\lg M(T)=n\,\lg\mu$ | bits |
| Tasa de información | $R = I/T$ | bps |
| Tasa de dígitos | $r = N/T$ | dígitos/s (binits/s) |
| Velocidad de señalización | $s = 1/\tau_{min}$ | baudios |
| Con $\tau=\tau_{min}$ y equiprobables | $R = s\,\lg\mu$ | bps |
| Sistema binario | $C=s$; ancho de banda $B \ge s/2$ | — |

Referencias: $n$ y $t$ = cantidad y tiempo de los pulsos **de información** (sin arranque/parada); $N$ y $T$ = cantidad y tiempo **totales**. $\lg x = \log_{10}x / \log_{10}2 \approx 3{,}32\log_{10}x$.

Reglas de la práctica resuelta:
- Pulsos de arranque/parada de amplitud **fija** no aportan información (son 1 nivel → $\lg 1 = 0$), pero **sí suman tiempo** a $T$.
- Si hay subsistemas (bloque multinivel + bloque binario), $M(T)=M_1\cdot M_2$ e $I = \lg M_1 + \lg M_2$; $T$ es la suma de los tiempos (cuidado con las unidades, μs vs ms).
- "Entre +4 y −4 incluido el 0" = 9 niveles.
- **Duplicar R sin cambiar $\tau$ ni $T$**: la única variable libre es $\mu$. Se plantea $2R = (n\lg\mu' + \ldots)/T$, se despeja $\lg\mu'$ y $\mu' = 2^{(\ldots)}$, redondeando **para arriba**.
- Gráfica: eje $t$ con el pulso de arranque (amplitud fija), los $n$ pulsos multinivel de ancho $\tau$ con alturas arbitrarias entre los niveles posibles, y el de parada; marcar $\tau$ y $T$.

```
 V
+4 |██                                  arranque fijo
   |   ▄▄    ▄▄▄                         ...
   |   ██ ▄▄ ███    ▄▄         (μ = 128 niveles posibles)
 0 |---██-██-███-▄▄-██-------------------------------> t
   |                ...                ██
-4 |                                   ██  parada fija
   |<τ>|
   |<------------------- T = (n+2)·τ ------------->|
```

##### 2. Modulación con portadora analógica (casos I y II)
Portadora $x_c = A_c\cos(2\pi f_c t+\varphi_c)$: se varía **un** parámetro por vez → amplitud (AM), frecuencia (FM) o fase (PM).

**AM, análisis espectral.** Con $x_m=A_m\cos 2\pi f_m t$:
$$x_{AM}=(A_c + A_m\cos 2\pi f_m t)\cos 2\pi f_c t = A_c\cos 2\pi f_c t + \tfrac{A_m}{2}\cos 2\pi(f_c-f_m)t + \tfrac{A_m}{2}\cos 2\pi(f_c+f_m)t$$
Aparecen la portadora y **dos bandas laterales** (inferior y superior) que repiten el mensaje. Ej.: emisora en $f_c=1230$ kHz y componente en 1260 kHz ⇒ $f_m=30$ kHz. Para un mensaje de banda $W$: DSB ocupa $2W$; SSB/BLU ocupa $W$. DSB‑SC y SSB‑SC suprimen la portadora (ahorran potencia; SSB‑SC para móviles/punto a punto donde la energía es crítica).

**FDM.** Cada mensaje modula una portadora distinta; las bandas quedan una al lado de la otra dentro del canal $[f_{c\,min}, f_{c\,max}]$ y viajan **simultáneamente**:
$$\text{DSB: } B_w = N\cdot 2W \qquad \text{SSB: } B_w = N\cdot W$$

**Caso II — mensaje digital / portadora analógica (MODEM).** Aplicación: la PC (señal digital) que sale por la línea telefónica (red pensada para voz analógica): PC → MODEM (D/A) → red → MODEM (A/D) → PC.

| Técnica | Qué varía | "1" / "0" | Comentario de la cátedra |
|---|---|---|---|
| ASK | Amplitud | hay portadora / no hay | "Actualmente no se usa" (muy sensible al ruido) |
| FSK | Frecuencia | $f_1$ / $f_0$ | Equivale a dos ASK superpuestas |
| PSK | Fase | cambio de fase al cambiar de 1 a 0 o de 0 a 1 | Sólo demodulación coherente |
| FSK multinivel | Frecuencia + amplitud | 2 frec. × 2 amp. = 4 estados → 2 bits/símbolo | Más dígitos en la misma unidad de tiempo |
| PSK multinivel (QAM / APSK) | Fase + amplitud | 4 fases × 2 amp. = 8 estados → 3 bits/símbolo | Constelación polar (0°, 90°, 180°, 270°) |

Ancho de banda práctico de un tren de pulsos: el espectro es una $\mathrm{sinc}$ con armónicas separadas $1/T_0$ y la mayor parte de la energía entre 0 y $1/\tau$ ⇒ $w = 1/\tau$; modulado en ASK se duplica alrededor de $f_c$: $B_w \approx 2/\tau$. (El resumen de alumnos agrega que recortando en $1/\tau$ se recupera ~98 % de la información.)

**Cómo aumentar la velocidad (pregunta clásica de final).** Con $R = s\lg\mu$: si no puedo subir $s$ (el canal limita $B\ge s/2$), subo $\mu$ → **modulación multinivel**. Con 8 estados (QAM‑8) cada símbolo lleva 3 bits: a igual baudios, triple de bps.
*(Conocimiento general)* Límite: Nyquist sin ruido $C = 2B\lg\mu$; Shannon con ruido $C = B\lg(1+S/N)$ — más niveles exigen mejor S/N porque los estados quedan más juntos. La fórmula de Shannon aparece en el apunte "Errores en Canales".

**Demodulación.**
- *Coherente (sincrónica)*: el receptor multiplica por una portadora local de igual frecuencia y fase; da $f_m$ y $2f_c\pm f_m$; un pasa‑bajos deja $f_m$ y un circuito regenerador (CR) rearma los pulsos. Inconveniente: costo. FSK coherente necesita las dos portadoras en destino.
- *Incoherente (detección de envolvente)*: rectificador/absolutor + filtro + CR; existe para ASK y FSK. **PSK no tiene incoherente.**

##### 3. Mensaje analógico / portadora digital: muestreo, PAM y PCM
En vez del mensaje completo se mandan **muestras**; el tiempo muerto entre pulsos se aprovecha para muestras de otros mensajes (TDM).
- **PAM**: el mensaje varía la amplitud del pulso. **PDM**: la duración (análogo a FM). **PPM**: la posición (análogo a PM).
- **PCM**: además se **cuantifica** (redondea al nivel cuántico más cercano; el intervalo asociado es el *cuanto*) y se **codifica** cada nivel con $n$ dígitos binarios. Ej. del apunte: rango [−4,5; 4,5] con 7 niveles separados 1,5 → código de 3 bits.
- **Etapas de la digitalización** (diagrama del apunte): muestreador(es) → multiplex (PAM/TDM) → cuantificador → multiplexor con señalización y sincronismo → codificador → código de línea → señal PCM.
- **PCM 30+2**: trama con 30 canales de información + 2 de sincronismo/señalización (el E1 europeo; *conocimiento general*: 32·8·8000 = 2,048 Mbps).

**Teorema de muestreo (Nyquist).** Al muestrear, el espectro del mensaje (ancho $w$) se repite alrededor de $f_s, 2f_s, \ldots$ Para meter más mensajes conviene bajar $f_s$ (agranda $T_s$), pero si $f_s - w < w$ las réplicas se superponen (aliasing) y no se recupera el mensaje:
$$f_s - w \ge w \;\Rightarrow\; f_s \ge 2w,\qquad w = f_{max}-f_{min}\approx f_{max} \;\Rightarrow\; f_s \ge 2f_{max}$$

**Ancho de banda de una trama TDM/PCM** (apunte 5, pp. 23–24):

| Símbolo | Significado | Relación |
|---|---|---|
| $N$ | muestras por trama (info + control) | — |
| $n$ | dígitos por muestra | — |
| $\tau$ | ancho de cada dígito (pulso) | $\tau = T_M/n$ |
| $T_M$ | duración de una muestra | $T_M = n\tau$ |
| $T_s$ | duración de la trama = período de muestreo | $T_s = N T_M = 1/f_s$ |
| $B_w$ | ancho de banda (primer cruce por cero de la sinc) | $B_w = 1/\tau = N\,n\,f_s = N\,n\,2f_{max}$ |

**Cómo reconocer el ejercicio** ("Fórmulas y pasos"): si dan $n$ bits, hablan de canal digital o de trama → **TDM/PCM**. Si piden transmitir $N$ señales analógicas simultáneas por un canal analógico y no dan bits → **FDM/AM**. En el final siempre: **técnica** (multiplexado TDM + modulación PCM), **gráficos** y **cálculos con unidades**.

Gráficos que hay que hacer en el ejercicio PCM:
```
(1) Mensaje y muestreo        (2) Espectro muestreado (Nyquist)
 x(t)  .-.     .-.             |█|      |███|      |███|
      /   \   /   \            |█|      |███|      |███|
 ----+--|--\-/--|--\--> t      +-+------+-+-+------+-+-+--> f
     ↑  ↑  ↑ ↑  ↑   (Ts)       0 w   fs-w fs fs+w     2fs        fs ≥ 2w

(3) Trama TDM (dura Ts = 1/fs)            (4) Una muestra (TM = n·τ)
 |C1|C2|C3| ... |C25|ctl|ctl|C1|...        |1|0|1|1|0|0|1|
 |<-TM->|                                  |τ|
 |<------------- Ts ------------->|        |<--- TM --->|

(5) Espectro del tren de pulsos: sinc con primer cruce en 1/τ = Bw
```

##### 4. ADSL — asignación de frecuencias (apunte 6, escaneo)
El par de cobre del abonado se reparte en frecuencia (es un FDM):

| Banda | Rango | Ancho | Uso |
|---|---|---|---|
| PSTN | 0 – 4 kHz | 4 kHz | Telefonía (voz) |
| (guarda) | 4 – 25,875 kHz | — | separación voz/datos |
| Upstream | 25,875 – 138 kHz | 112,125 kHz | Subida: cliente → nube |
| Downstream | 138 – 1104 kHz | 966 kHz | Bajada: nube → cliente |

"Asimétrico": la bajada tiene ~8,6 veces más espectro que la subida, porque el usuario típico descarga mucho más de lo que sube. Voz y datos conviven en el mismo par al mismo tiempo; en el domicilio un *splitter/microfiltro* separa la banda de 0–4 kHz para el teléfono.
*(Conocimiento general, no está en el escaneo)*: ADSL usa DMT, 256 subportadoras de 4,3125 kHz (1104/4,3125 = 256), cada una modulada en QAM con tantos bits como permita su S/N — es la "modulación multinivel para aumentar la velocidad" llevada a la práctica. La subida empieza en la subportadora 6 (25,875 = 6·4,3125) y la bajada en la 32 (138 = 32·4,3125).

#### Ejercicios resueltos tipo

**E4.1 — Multinivel con arranque y parada (Final 04/04/2025).** Grupos de 27 pulsos de 128 niveles c/u, 1 pulso fijo de arranque +4 V y 1 de stop −4 V, cada pulso dura 10 μs. Calcular M(T), Ix, R y graficar.
1. Datos: $n = 27$ (información), $\mu = 128 = 2^7$, $\tau = 10\ \mu s$. Arranque y stop son fijos → no aportan información.
2. $T$ incluye todos los pulsos: $T = (27+2)\cdot 10\ \mu s = 290\ \mu s$.
3. $M(T) = 128^{27} = 2^{189}$ mensajes distintos.
4. $I_x = \lg 128^{27} = 27\cdot 7 = 189$ bits.
5. $R = I_x/T = 189 / 290\ \mu s = 0{,}6517\times10^6$ bps ≈ **651,7 kbps**.
6. Gráfica: como la del Desarrollo, con +4 V al inicio, 27 pulsos de alturas entre los 128 niveles y −4 V al final; $T = 290\ \mu s$.

**E4.2 — Pulsos de distinta duración (Final 10/09/2021).** 1 arranque fijo, 10 pulsos de 128 niveles, 1 stop fijo; todos duran 5 ms salvo el stop (7 ms). a) R. b) R si los 10 pulsos de datos pasan a binarios.
1. $T = 11\cdot5\ ms + 7\ ms = 62\ ms$.
2. a) $I = 10\cdot\lg128 = 70$ bits → $R = 70/0{,}062 = $ **1129 bps**.
3. b) $I = 10\cdot\lg 2 = 10$ bits → $R = 10/0{,}062 = $ **161,3 bps** (cae 7 veces: $\lg128/\lg2 = 7$).

**E4.3 — Trama PCM 25+2 (Final 04/04/2025 y 19/11/2021).** 25 muestras de información + 2 de control; señales de 400 a 3500 Hz; 7 dígitos por muestra. Calcular el ancho de banda, graficar e indicar la técnica.
1. Técnica: **multiplexado TDM** con **modulación PCM** (muestreo + cuantificación + codificación binaria). Cada muestra ocupa todo el canal durante su ranura.
2. $N = 25+2 = 27$ (las de control también ocupan ranura), $n = 7$.
3. Nyquist: $f_s \ge 2 f_{max} = 2\cdot 3500 = 7000$ Hz → $T_s = 1/f_s = 142{,}86\ \mu s$ (duración de la trama).
4. $T_M = T_s/N = 142{,}86/27 = 5{,}291\ \mu s$; $\tau = T_M/n = 5{,}291/7 = 0{,}756\ \mu s$.
5. $B_w = 1/\tau = N\,n\,2f_{max} = 27\cdot7\cdot7000 = $ **1.323.000 Hz ≈ 1,32 MHz**.
6. Gráficos: los cinco del Desarrollo (mensaje muestreado; espectro con réplicas en $f_s$; trama de 27 ranuras en $T_s$; muestra de 7 bits; sinc con cruce en $1/\tau$).
- Variante con $w = f_{max}-f_{min} = 3100$ Hz: $B_w = 27\cdot7\cdot6200 = 1.171.800$ Hz (ver Dudas).

**E4.4 — Problema inverso (Final 10/09/2021).** 900 señales PAM por un canal digital ocupan 2 MHz; código de 7 bits por muestra. ¿Ancho de banda $W$ de cada señal original?
1. $B_w = N\,n\,f_s$ → $f_s = B_w/(N n) = 2\times10^6/(900\cdot7) = 317{,}46$ Hz.
2. $f_s = 2W$ → $W = 158{,}7$ Hz.

Variantes rápidas (Ejercitación Comunicación Digital): 2200 señales de 4 kHz con 8 bits → $B_w = 2200\cdot8\cdot8000 = 140{,}8$ MHz. 2500 señales de 4 kHz con 8 bits → $\tau = 1/(2500\cdot8\cdot8000) = 6{,}25$ ns. 32 señales de 4 kHz, 8 bits → 2,048 MHz.

**E4.5 — FDM (Ejercitación Comunicación Digital).** 4 señales telefónicas de 300 a 3400 Hz por un canal con frecuencia mínima de corte de 400 kHz.
1. Técnica: modulación AM, cada señal con su portadora; multiplexado FDM.
2. $W \approx f_{max} = 3400$ Hz. DSB: $B_w = 4\cdot2\cdot3{,}4 = 27{,}2$ kHz → el canal usado va de 400 a 427,2 kHz (portadoras en 403,4; 410,2; 417; 423,8 kHz). SSB: $B_w = 4\cdot3{,}4 = 13{,}6$ kHz (400 a 413,6 kHz).
3. Gráfico: eje $f$ con 4 bloques triangulares (o 8 en DSB, espejados) contiguos a partir de 400 kHz, cada uno con su $f_{ci}$.

#### Dudas / pendientes
- **Ancho de banda PCM con $f_{min}$ no despreciable.** El apunte define $w = f_{max}-f_{min} \approx f_{max}$ y "Fórmulas y pasos" usa $B = N\,n\,2f_{max}$ (1,323 MHz para E4.3). Una resolución de alumno del final 19/11/2021 (mismo enunciado) usa $w = 3100$ Hz y da 1,1718 MHz; no se ve la nota. *(Conocimiento general)*: muestrear a $2(f_{max}-f_{min})$ sólo funciona como muestreo pasabanda en casos particulares, así que lo seguro es $2f_{max}$. Conviene mostrar las dos y justificar la elegida, o preguntarle a Baró qué criterio corrige.
- **Arranque/stop en el multinivel.** En E4.1 se toma que los 27 pulsos son de datos y se suman 2 (como en el ej. 11 resuelto: 13 + 2 = 15 → $T = 150\ \mu s$). Si se interpretara 27 en total ($n=25$, $T = 270\ \mu s$), $I = 175$ bits y $R = 648{,}1$ kbps.
- **Error en la práctica resuelta (ej. 2)**: escribe $I = 6\lg7 = 2{,}81$ bits y $R = 28{,}1$ bps; $2{,}81$ es $\lg 7$, no $6\lg7$. Lo correcto es $I = 16{,}84$ bits y $R = 168{,}4$ bps.
- **Redondeo de I.** En el ej. 11 resuelto la práctica redondea $76{,}16 \to 77$ bits y obtiene 513 kbps; sin redondear da 507,7 kbps. En el ej. 14 usa $\lg7 \approx 2{,}8$ y obtiene $\mu = 147$; con valores exactos da 148,5 → **149** niveles. Aclarar en el examen el criterio.
- **Contradicciones en resúmenes de alumnos**: "Resumen" (para el final) dice que PSK "sólo se puede demodular de forma asincrónica" y que PSK multinivel usa "dos fases y cuatro amplitudes"; el apunte de la cátedra dice lo contrario (PSK sólo coherente; 4 fases × 2 amplitudes). Vale el apunte.
- **Dos fórmulas de ancho de banda**: apunte 1 da $B \ge s/2$ (canal binario, Nyquist); apunte 5 usa $B_w = 1/\tau$ (cruce por cero de la sinc). Para el ejercicio PCM la cátedra usa $1/\tau$.
- El apunte de ADSL es sólo un gráfico; DMT, subportadoras de 4,3125 kHz y QAM por tono son conocimiento general. Nyquist $C=2B\lg\mu$ también es conocimiento general.
- Las fórmulas del apunte 5 salen como texto roto en la conversión (sinc, AM); se reconstruyeron con la forma estándar y coinciden con El Santo Resumen.

#### Fuentes
- `fuentes/teoria/5 - Comunicaciones Digitales.md`
- `fuentes/teoria/6 - Espectro de la señal ADSL - Asignación de Frecuencias.md` (+ escaneo del PDF)
- `fuentes/practica/1 - Principios Básicos de la Electrónica y las Comunicaciones.md` (multinivel, $B \ge s/2$)
- `fuentes/practica/2 - Ejercitación Practica Transmisión Multinivel (RESUELTO).md`
- `fuentes/practica/Ejercitación Comunicación Digital.md`
- `fuentes/resumenes/Para rendir el final/Práctica - Fórmulas y pasos para los ejercicios.md`
- `fuentes/resumenes/Para rendir el final/Teoría - Preguntas frecuentes (Parte 1).md` y `(Parte 2).md`
- `fuentes/resumenes/Para rendir el final/Resumen.md`
- `fuentes/resumenes/El Santo Resumen/el-santo-resumen.md` (secciones Modulación, Muestreo y PCM, TDM y la trama, Final)
- `fuentes/finales/Práctica/2025/2025-04-04.jpg`, `fuentes/finales/Práctica/2021/Comunicaciones - Final - 2021-09-10.md`, `… 2021-11-19.md` (+ PDF con resolución de alumno), `fuentes/finales/Práctica/2020/*.md`

---

### Unidad 5 — Medios de transmisión, multiplexación (CDM, WDM) y elección del medio de acceso

#### Conceptos clave
- Medios **guiados** (par trenzado, coaxil, fibra) vs **no guiados** (radio, microondas, infrarrojo, satélite).
- Fibra: mayor ancho de banda, repetidores cada ~50 km (cobre ~5 km), inmune a interferencia electromagnética; contra: frágil, unidireccional, interfaces caras.
- Microondas/radioenlace: línea de vista, torres altas (100 m → repetidores a 80 km), lluvia desde ~4 GHz, desvanecimiento multitrayecto; más barato que tender fibra en zonas difíciles.
- Satélite: repetidor en el cielo; GEO ~35.000 km (latencia alta), llega a lugares inaccesibles; VSAT = antena ≤ 1 m.
- Multiplexados: **FDM** (frecuencia), **TDM** (tiempo), **CDM** (código, espectro ensanchado, no guiado → CDMA), **WDM** (longitud de onda, sólo fibra; **DWDM** > 4 λ, hasta 80+). Con "A" (FDMA, TDMA, CDMA) = acceso a una red. FSK/PSK son **modulación**, no multiplexado.
- **Última milla** = medio de acceso de la organización a la red del operador; lo define el Ing. en Sistemas con el operador.
- Variables de elección: zona, permanencia, espacio físico, ancho de banda (bajo 4–8 M, medio 10–50 M, alto > 100 M), madurez, segurización, recursos.
- Segurización: recorridos **disjuntos** y **otro operador con infraestructura propia**.

#### Desarrollo

##### 1. Medios guiados

**Par trenzado.** Dos conductores de cobre aislados y trenzados (dos cables paralelos son una antena; trenzados, las ondas de vueltas distintas se cancelan). Uso clásico: telefonía (varios km sin amplificar). Atenuación muy dependiente de la frecuencia; amplificadores cada 5–6 km (analógico) o repetidores cada 2–3 km (digital).

| Tipo | Blindaje | Impedancia |
|---|---|---|
| UTP | Ninguno, barato, más errores | 100 Ω |
| STP | Blindaje por par | 150 Ω |
| FTP | Pantalla global | 120 Ω |
| SFTP | Blindaje + pantalla | — |

Categorías: Cat 3 = 16 MHz; Cat 5 = 100 MHz (más vueltas por cm que Cat 3 → menos diafonía); Cat 5e = 160 MHz; Cat 6 = 250 MHz. LAN: 100 m por segmento; con 2 pares half‑dúplex, con 4 full‑dúplex.

**Coaxil.** Núcleo rígido + aislante + malla + cubierta. Mejor blindaje que el par → tramos más largos a más velocidad. 50 Ω digital, 75 Ω analógico/TV por cable. Reemplazado por fibra en troncales; queda en TV por cable (cable módem residencial).

**Fibra óptica.** Fuente de luz (LED/láser) + fibra + detector; pulso de luz = 1, ausencia = 0. Funciona por **reflexión interna total** (rayos con ángulo ≥ crítico quedan atrapados en el núcleo, cuyo índice de refracción es mayor que el del revestimiento).

| | Multimodo | Monomodo |
|---|---|---|
| Núcleo | 50 (o 62,5) μm | 8–10 μm |
| Propagación | muchos modos (rebotes) → dispersión modal | un solo modo, en línea recta |
| Distancia | corta (< 2 km) | larga (hasta ~400 km con láser; 50 Gbps a 100 km sin amplificar) |
| Emisor | LED (OM1/OM2), VCSEL (OM3) | láser |
| Costo | simple y económica | más cara |

Pérdidas: absorción, Rayleigh, dispersión cromática, radiación (curvaturas), dispersión modal, acoplamiento (conectores pierden 10–20 % de la luz; empalme mecánico o por fusión).

##### 2. Medios no guiados
- **Radio** (VLF–VHF): omnidireccional, atraviesa edificios; en VLF/LF/MF sigue la curvatura terrestre, en HF/VHF rebota en la ionosfera.
- **Microondas** (> 100 MHz): viajan en línea recta, haz concentrado con antena parabólica (buena S/N) → exige **alineación y visión directa**. Distancia entre repetidores ∝ $\sqrt{h}$ de las torres (100 m → 80 km). Desde ~4 GHz las absorbe la lluvia. **Desvanecimiento por múltiples trayectorias**: ondas refractadas llegan desfasadas y cancelan la directa.
- **Infrarrojo**: corto alcance, no atraviesa sólidos (no interfiere con el cuarto vecino, más seguro), sin licencia.
- **Satélite**: repetidor de microondas con transpondedores que reciben y retransmiten en otra frecuencia ("tubo doblado").

| Órbita | Altura | Latencia (fig. del apunte) | Satélites para cubrir | Notas |
|---|---|---|---|---|
| GEO | ~35.800 km | ~270 ms | 3 | Fijo en el cielo; vida útil ~10 años (combustible) |
| MEO | ~10.000 km (entre cinturones de Van Allen) | 35–85 ms | 10 | ~6 h por vuelta; ej. GPS |
| LEO | baja | 1–7 ms | ~50 | Se mueven rápido, hacen falta muchos |

Bandas: L, S, **C (4/6 GHz, la primera comercial)**, Ku (11/14 GHz) y Ka (20/30 GHz, sufren la lluvia). Bajada en la frecuencia menor, subida en la mayor.

##### 3. Multiplexación: mapa completo

| Técnica | Qué se reparte | Señal / modulación | Medio | Acceso |
|---|---|---|---|---|
| FDM | bandas de frecuencia; todos a la vez | analógica, AM/FM/PM | guiado o no guiado | FDMA |
| TDM | ranuras de tiempo; cada uno usa todo el $B_w$ en su turno | PCM | guiado o no guiado | TDMA |
| CDM | códigos pseudoaleatorios; todos a la vez en toda la banda | espectro ensanchado | **no guiado** (radioenlaces spread spectrum) | CDMA |
| WDM / DWDM | longitudes de onda (colores de luz) | portadoras ópticas (láser/LED) | **sólo fibra óptica** | — |

**CDM.** Cada transmisión se multiplica por una palabra código tan larga que parece aleatoria (pseudoaleatoria): la energía se reparte en una banda muy ancha con amplitud casi a nivel de ruido → **espectro ensanchado**. No interfiere con servicios que tienen banda asignada, lo que permite dar servicio de datos urgente sin esperar asignación de frecuencia del regulador. Origen militar (encriptar).

**WDM.** Ejemplo concreto: una fibra tendida que transmitía una sola λ se saturó; tender fibra nueva es caro (fibra + obra), entonces se ponen MUX/DEMUX ópticos en los extremos y la misma fibra lleva $\lambda_1, \lambda_2, \ldots, \lambda_n$, cada una modulada por un láser con su propio conjunto de señales. **DWDM** = más de 4 λ, hasta 80 o más por fibra. *(Conocimiento general: WDM es un FDM en el dominio óptico.)*

##### 4. Elección del medio de acceso (última milla)
Medios de acceso hoy: **par telefónico, fibra óptica, radioenlace, satélite**; coaxil sólo para cable módem residencial; láser sin expansión de mercado.

| Medio | Ventajas | Desventajas | Cuándo |
|---|---|---|---|
| Par telefónico (+ xDSL/HDSL) | Ya está instalado en zona urbana, barato, rápido de habilitar | Poco ancho de banda, se degrada con distancia, ruido y diafonía | Organización chica, urbana, bajo BW, pocos recursos |
| Fibra óptica | Enorme BW, baja atenuación, inmune a EMI, difícil de intervenir, escalable | Costo de tendido y obra, frágil, requiere personal especializado | BW alto, ubicación definitiva, urbana/suburbana, o rural con crecimiento |
| Radioenlace (microondas) | Sin obra civil de tendido, más barato que fibra en zonas difíciles, rápido | Visión directa, mástil y espacio físico, lluvia, multitrayecto, licencia | Suburbana con BW bajo/medio y espacio para el mástil; segurización de fibra |
| Satélite (VSAT) | Llega a cualquier lado (rural, montaña, selva), se instala y se muda fácil | Latencia alta (GEO), costo por Mbps, lluvia (Ku/Ka), BW limitado | Zona inaccesible, ubicación transitoria, sin espacio; segurización |

Ejemplos de la cátedra:

| # | Organización | Zona | BW | Otros | Solución |
|---|---|---|---|---|---|
| 1 | Pequeña | Urbana | Bajo | sin segurización, pocos recursos | Par telefónico + módem HDSL |
| 2 | Madura | Urbana definitiva | Alto | segurización, recursos | Fibra en **anillo** |
| 3 | Madura | Rural transitoria | Bajo | sin espacio físico | Satelital |
| 4 | Madura | Suburbana definitiva | Bajo | con espacio, sin segurización | Radioenlace |
| 5 | Madura | Suburbana definitiva | Bajo | con espacio, con segurización | Radioenlace + backup satelital |
| 6 | Madura | Suburbana definitiva | Alto | segurización | Fibra en anillo |
| 7 | En crecimiento | Rural definitiva | Medio | segurización, con espacio | Fibra + backup por radioenlace |
| 8 | Pequeña | Montañosa/selva | Bajo | sin segurización | Satelital |

**Segurización.**
- Acceso y backup por fibra: los recorridos hasta la sala de equipos deben ser **disjuntos** (no compartir ningún tramo: una retroexcavadora corta las dos).
- Conviene que acceso y backup los den **operadores distintos**; y que el segundo tenga **infraestructura propia**, porque si alquila la del primero, al caer el operador 1 caen los dos.

**Radioenlace e instalación.** Necesita visión directa → altura. En un edificio alcanza un barral; si no, mástil arriostrado: el pie de rienda está al **60 % de la altura H** del mástil, por lo que se necesita un terreno libre de $2\cdot0{,}6H$ por lado.

#### Ejercicios resueltos tipo

**E5.1 — Elección del medio (Final 04/04/2025, teoría).** Nombrar al menos tres medios de acceso con ventajas/desventajas (tabla del Desarrollo) y elegir para:
- a) *Zona montañosa, no requiere gran velocidad* → **Satelital** (ej. 8): no hay tendido posible, no hay visión directa garantizada para radioenlace, y el BW bajo hace aceptable el costo por Mbps y la latencia.
- b) *Zona urbana, requiere gran velocidad* → **Fibra óptica**, en anillo si requiere segurización (ej. 2): en ciudad el operador ya tiene fibra cerca; es el único medio que da > 100 M con escalabilidad.
- c) *Zona suburbana, requiere gran velocidad* → **Fibra óptica en anillo** (ej. 6).
- d) *Zona suburbana, sin gran velocidad* → **Radioenlace** si hay espacio para el mástil (ej. 4), + satelital si requiere segurización (ej. 5).
- e) *Edificio provisorio que se muda pronto, suburbano, BW bajo* → **Satelital** o radioenlace desmontable: no se justifica la obra de fibra (criterio del ej. 3).
Como la consigna no dice espacio físico ni segurización, **explicitar la suposición**.

**E5.2 — Espacio para un radioenlace.** Se necesita un mástil arriostrado de 40 m.
1. Pie de rienda = 60 % de H = 0,6·40 = 24 m.
2. Riendas a ambos lados → 2·24 = 48 m.
3. Terreno libre ≈ **48 m × 48 m**. (Ej. del apunte: H = 30 m → 18 m → 36 × 36 m.) Si no se dispone de ese espacio, el radioenlace queda descartado.

**E5.3 — Repetidores fibra vs cobre.** Enlace troncal de 200 km.
1. Fibra: repetidor cada ~50 km → 200/50 = 4 tramos → **3 repetidores** intermedios.
2. Cobre: cada ~5 km → 40 tramos → **39 repetidores**. Explica el "ahorro considerable" que menciona el apunte.

**E5.4 — WDM.** Una fibra lleva una λ de 10 Gbps y se satura. Con DWDM de 80 λ de 10 Gbps cada una: 80·10 = **800 Gbps** sobre la misma fibra, sin obra civil. *(Valores de canal: conocimiento general.)*

#### Dudas / pendientes
- **Latencia GEO**: la figura del apunte (vía El Santo Resumen) dice 270 ms. *(Conocimiento general)*: sólo subir y bajar 35.786 km a la velocidad de la luz son ≈ 239 ms; 250–280 ms es lo habitual para un salto. El ida y vuelta completo ronda 500 ms.
- Rangos de BW de la cátedra (bajo 4–8 M, medio 10–50 M, alto > 100 M): quedan huecos (8–10 M, 50–100 M) sin clasificar.
- Ejemplo 1 usa **HDSL**; no se explica en el apunte. *(Conocimiento general)*: HDSL es simétrico (pensado para empresas), ADSL es asimétrico (residencial).
- El apunte de Medios es de la UAI (2016), usado como material de práctica; algunos datos (cat. 9 = 25 GHz, cat. 10 = 75 GHz) no son estándares reconocidos y no conviene citarlos.
- Los multiple choice de parciales preguntan por ley de Snell, retardo por km y longitud de onda: no están en los apuntes (lo advierte El Santo Resumen).

#### Fuentes
- `fuentes/practica/3 - Medios de transmisión.md`
- `fuentes/teoria/MULTIPLEXADO CDM-WDM-v03.md`
- `fuentes/teoria/Elección medio de acceso V03.md`
- `fuentes/resumenes/2° Parcial/Resumen Parcial 2 (2025).md` (tabla de elección)
- `fuentes/resumenes/Para rendir el final/Teoría - Preguntas frecuentes (Parte 1).md` (consignas de medio de acceso)
- `fuentes/resumenes/El Santo Resumen/el-santo-resumen.md` (Medios de transmisión, satélites, Otros multiplexados, Elección del medio de acceso, Final)
- `fuentes/finales/Teoría/2020/*.md`, `fuentes/finales/Teoría/Teoria vieja.md` (MC de medios), `fuentes/finales/Práctica/2020/Comunicaciones - Final - 2020-02-21.md`

---

### Unidad 6 — Asignación de capacidad de canales y teoría de colas

#### Conceptos clave
- Elementos de un sistema de colas abierto: **fuente** (finita/infinita), **proceso de arribo** (Poisson ⇔ intervalos exponenciales), **tiempo de servicio** (exponencial), **capacidad máxima**, **número de servidores**, **disciplina** (FIFO, LIFO, prioridades).
- Kendall **A/B/c/k/n/Z**; A/B/c cuando cola ilimitada, fuente infinita y FIFO. M = exponencial, D = determinística, $E_k$ = Erlang‑k, $H_k$ = hiperexponencial, G/GI = general.
- $u = E[s]/E[\tau] = \lambda E[s]$ (Erlang) → mínimo de servidores; $\rho = u/c$ (utilización).
- **Little**: $L = \lambda W$, $L_q = \lambda W_q$; $W = W_q + E[s]$.
- **M/M/1**: $W_q = \rho E[s]/(1-\rho)$, $W = E[s]/(1-\rho)$, $\pi_q(90) = W\ln(10\rho)$. Si $\rho \ge 1$ la cola crece sin límite.
- Modelo cerrado interactivo: **punto de saturación** $N^* = (E[s]+E[t])/E[s]$.
- Asignación de capacidad (Kleinrock): cada enlace es una M/M/1 con $\mu_i = \eta_i C_i$, $T_i = 1/(\eta_i C_i - \lambda_i)$; regla de la **raíz cuadrada** minimiza el retardo medio con capacidad total fija.

#### Desarrollo

##### 1. Teoría de colas: elementos y notación
Ejemplo concreto: una caja de banco. Los clientes (usuarios) llegan al azar desde una población (fuente), esperan en la fila (cola) si la caja (servidor) está ocupada, se atienden por orden de llegada (FIFO) y se van. El tiempo total en el banco es $t_w = t_q + t_s$.

| Símbolo | Significado |
|---|---|
| $\lambda$ | frecuencia media de arribos, $\lambda = 1/E[\tau]$ |
| $E[\tau]$ | intervalo medio entre arribos |
| $E[s]$, $\mu$ | tiempo medio de servicio; frecuencia de servicio por servidor $\mu = 1/E[s]$ |
| $c$ | número de servidores |
| $u$ | intensidad de tráfico $= \lambda E[s]$ [Erlang] |
| $\rho$ | factor de utilización $= u/c$ (probabilidad de que un servidor esté ocupado) |
| $L, L_q$ | usuarios promedio en el sistema / en la cola |
| $W, W_q$ | tiempo promedio en el sistema / en la cola |
| $\pi_q(90)$ | tiempo de cola que no supera el 90 % de los usuarios |
| $C(c,u)$ | fórmula C de Erlang: probabilidad de que los $c$ servidores estén ocupados |

Procesos: arribos Poisson, $P[\tau \le t] = 1 - e^{-\lambda t}$ y $P[n \text{ arribos en } t] = e^{-\lambda t}(\lambda t)^n/n!$; servicio exponencial, $W_s(t) = 1 - e^{-\mu t}$. Coeficiente de variación al cuadrado $C^2$: 0 constante, $1/k$ Erlang‑k, 1 exponencial (aleatorio), > 1 arribos agrupados.

Intensidad de tráfico: si $E[s]=15$ s y $E[\tau]=10$ s → $u = 1{,}5$ Erlang → hacen falta **al menos 2 servidores**.

Capacidad del sistema: infinita (todos esperan) o "sistema de pérdida" (cola nula: si está ocupado, el usuario se va).

##### 2. Modelo abierto M/M/c y su caso M/M/1
$$W_q = \frac{C(c,u)\,E[s]}{c(1-\rho)},\qquad W = W_q + E[s],\qquad \pi_q(90) = \frac{E[s]}{c(1-\rho)}\ln\big(10\,C(c,u)\big)$$
$$C(c,u) = \frac{u^c/c!}{(1-\rho)\sum_{n=0}^{c-1} u^n/n! + u^c/c!}\quad\text{(conocimiento general; la fórmula del apunte no se convirtió)}$$
Para $c=1$: $C = \rho$ y
$$\rho = \lambda E[s],\quad W_q = \frac{\rho\,E[s]}{1-\rho},\quad W = \frac{E[s]}{1-\rho},\quad L_q=\lambda W_q,\quad L=\lambda W,\quad \pi_q(90) = W\ln(10\rho)$$
*(Conocimiento general)*: el 90 percentil del tiempo **en el sistema** de una M/M/1 es $\pi_w(90) = W\ln 10 \approx 2{,}3\,W$.

Procedimiento (resolución tipo del final):
1. Pasar $\lambda$ y $E[s]$ a la **misma unidad** (ej.: 100 personas/día en un horario de 7 h → por minuto).
2. Verificar $\rho < 1$; si no, el sistema se satura y hay que agregar servidores ($c \ge u$).
3. Calcular $W_q$, $W$, $L_q$, $L$, $\pi_q(90)$ con unidades y **definir cada término**.
4. Concluir (¿la espera es aceptable? ¿conviene otro servidor?).

**Comportamiento cerca de la saturación**: $W = E[s]/(1-\rho)$ explota cuando $\rho\to1$. Con $\rho = 0{,}5$ la espera media en cola iguala al servicio; con $\rho = 0{,}9$ es 9 veces el servicio. Un servidor "ocioso 37 % del tiempo" (ej. del apunte, $\rho = 5/8$) igual hace esperar 50 min.

Ejemplo 2 del apunte (replanteo para $W_q \le 10$ min y $\pi_q(90) \le 15$ min): **una M/M/2** ($\rho=0{,}3125$, $C = 0{,}149$, $W_q = 3{,}25$ min, $\pi_q(90) = 8{,}67$ min) **cumple**; **dos M/M/1** separadas (cada una con $\lambda/2$, $W_q = 13{,}6$ min) **no cumplen**. Moraleja: una cola común a varios servidores es mejor que colas separadas.

##### 3. Modelo cerrado (sistema interactivo con población finita)
$N$ terminales; cada usuario alterna **pensar** ($E[t]$) → **esperar** → **ser atendido** por la CPU ($E[s]$). Nadie entra ni sale.
$$p_0 = \left[\sum_{k=0}^{N}\frac{N!}{(N-k)!}\left(\frac{E[s]}{E[t]}\right)^k\right]^{-1},\quad \rho = 1-p_0,\quad T = \frac{\rho}{E[s]},\quad W = \frac{N}{T} - E[t],\quad L = T\,W$$
(Fórmulas reconstruidas con conocimiento general; reproducen exactamente los números del ejemplo 3 del apunte.)

**Punto de saturación.** Gráfico de $W$ vs $N$: con pocos terminales casi no hay interferencia y $W \to E[s]$ (asíntota horizontal); con $N\to\infty$, $p_0\to0$ y $W \to N E[s] - E[t]$ (asíntota oblicua). Se cortan en
$$N^* = \frac{E[s]+E[t]}{E[s]}$$
**= número máximo de terminales sin interferencia mutua** (si cada interacción usara exactamente $E[s]$ y pensara exactamente $E[t]$). Más allá de $N^*$, cada terminal nuevo agrega ≈ $E[s]$ de respuesta a todos.

```
 W |                     /  W = N·E[s] − E[t]
   |                   /
   |                 /
   |              _/
   |          __-/
E[s]|______---/- - - - - - - -  W = E[s]
   +-----------|----------------> N
               N*
```
Ej. del apunte: $E[t]=3$ s, $E[s]=0{,}2$ s → $N^* = 16$. Con 20 terminales: $p_0 = 0{,}0456$, $\rho = 0{,}954$, $T = 4{,}77$ int/s, $W = 1{,}19$ s, $L = 5{,}68$. Con 30: $W = 3{,}00$ s, $T = 5$ int/s, $L = 15$ → +50 % de terminales da sólo +4,8 % de throughput y +152 % de tiempo de respuesta.

##### 4. Asignación de capacidad de canales (Kleinrock)
Problema: **¿qué capacidad $C_i$ (bps) darle a cada enlace** para una performance dada? Criterio de Kleinrock: costo ∝ capacidad total $C = \sum C_i$ fija; se reparte para **minimizar el retardo promedio** de la red.

Ejemplo concreto del apunte: 7 ciudades con terminales (TTY) conectadas en **estrella** a una computadora central en Rosario; cada terminal genera 1 mensaje cada 30 s ($1/30$ msg/s) de 120 bits en promedio. El concentrador de Mendoza con 10 terminales tiene $\lambda_1 = 10/30 = 0{,}33$ msg/s.

Modelo: cada concentrador es un **buffer FIFO** (multiplexado estadístico) con una línea de salida → cola **M/M/1**: arribos Poisson, longitud de mensaje exponencial con media $1/\eta_i$ bits, buffer infinito (bloqueo real < $10^{-3}$), procesamiento nodal despreciable.
$$\mu_i = \eta_i C_i\ \ [\text{msg/s}],\qquad T_i = \frac{1}{\eta_i C_i - \lambda_i} = \frac{1/(\eta_i C_i)}{1-\rho_i},\qquad \rho_i = \frac{\lambda_i}{\eta_i C_i} < 1$$
$T_i$ incluye **transmisión** ($1/\eta_iC_i$) + **espera en el buffer**. Si $\lambda_i \to \eta_i C_i$ ($\rho_i\to1$) el denominador tiende a 0 y **el retardo crece sin límites** (pregunta del 2° parcial 2025). Para $\rho_i \ll 1$, $T_i \approx 1/(\eta_iC_i)$, sólo el tiempo de transmitir.

Red como "caja negra" (Little): $\gamma = \sum\lambda_i$ y
$$E[T] = \frac{1}{\gamma}\sum_i \lambda_i T_i$$
Minimizando $E[T] + \alpha C$ (Lagrange) con $C$ fija:
$$C_i^{opt} = \frac{\lambda_i}{\eta_i} + C(1-\rho)\,\frac{\sqrt{\lambda_i/\eta_i}}{\sum_j \sqrt{\lambda_j/\eta_j}},\qquad \rho = \frac{1}{C}\sum_i\frac{\lambda_i}{\eta_i},\qquad \bar T_{min} = \frac{\left(\sum_i\sqrt{\lambda_i/\eta_i}\right)^2}{\gamma\,C\,(1-\rho)}$$
- Primer término $\lambda_i/\eta_i$: el flujo ofrecido en bps, **mínimo imprescindible** para que el enlace no se sature.
- Segundo término: la **capacidad remanente** $C(1-\rho)$ repartida en proporción a la **raíz cuadrada** del flujo → "regla de la raíz cuadrada".
- $\bar T_{min}$ ∝ $1/C$: siempre se baja el retardo subiendo $C$ (y el costo). En la práctica se prueban varias $C$, se grafica retardo vs costo y se eligen capacidades comerciales (ej. del apunte: canales de 450 o 900 bps).
- **Estrella vs árbol**: el árbol ahorra kilómetros (costo) pero los enlaces cercanos al centro suman los arribos de concentradores previos (hipótesis de independencia de Kleinrock) → mayor retardo medio a igual capacidad.

#### Ejercicios resueltos tipo

**E6.1 — M/M/1, sala de emergencias (Final 04/04/2025 y 20/11/2020).** Un doctor; llega un paciente cada media hora (Poisson); atención exponencial de 20 min promedio.
1. Unidades en minutos: $\lambda = 1/30$ pac/min; $E[s] = 20$ min.
2. $\rho = \lambda E[s] = 20/30 = 0{,}667$ (< 1, estable; el doctor está ocupado el 66,7 % del tiempo).
3. a) Espera para ser atendido (en cola): $W_q = \rho E[s]/(1-\rho) = 0{,}667\cdot20/0{,}333 = $ **40 min**.
4. b) Tiempo total en emergencias (sistema): $W = E[s]/(1-\rho) = 20/0{,}333 = $ **60 min** ($= W_q + E[s]$).
5. c) $L_q = \lambda W_q = 40/30 = $ **1,33 pacientes** en cola.
6. d) $L = \lambda W = 60/30 = $ **2 pacientes** en el sistema.
7. Extra: $\pi_q(90) = 60\ln(6{,}67) = 113{,}8$ min. Conclusión: con 2/3 de ocupación la espera ya duplica el tiempo de atención.

**E6.2 — M/M/1 con jornada (Final 19/11/2021; práctica).** Caja única de 7 a 14 h, 100 personas/día, servicio 3 min.
1. $\lambda = 100/(7\cdot60) = 0{,}238$ pers/min; $\rho = 0{,}238\cdot3 = 0{,}714$.
2. $W_q = 0{,}714\cdot3/0{,}286 = 7{,}5$ min; $W = 3/0{,}286 = 10{,}5$ min.
3. $L_q = 0{,}238\cdot7{,}5 = 1{,}79$; $L = 0{,}238\cdot10{,}5 = 2{,}5$; $\pi_q(90) = 10{,}5\ln(7{,}14) = 20{,}6$ min.
- Trampa (minibanco de la práctica): 60 personas en 10–15 h con 5 min → $\lambda = 0{,}2$/min, $\rho = 1$: **sistema saturado**, las fórmulas no aplican; hacen falta 2 cajas.
- M/M/2 (pago de haberes): 40 pers en 4 h, 4 min, 2 cajas → $u = 0{,}667$, $\rho = 0{,}333$, $C(2,u) = 0{,}167$, $W_q = 0{,}5$ min, $W = 4{,}5$ min, $L_q = 0{,}083$, $L = 0{,}75$, $\pi_q(90) = 1{,}53$ min.

**E6.3 — Asignación de capacidad (Ejercitación, tipo 2° parcial 2023/2024).** 4 concentradores en estrella hacia una CPU; cada terminal emite 10 msg/s de 6 bits. Santa Fe 20 terminales, Venado Tuerto 10, Villa Constitución 5, Cañada de Gómez 5. Capacidad total 5000 bps. Hallar $C^{opt}$ y $T_{min}$.
1. $\lambda_i$ = 200, 100, 50, 50 msg/s; $\gamma = 400$ msg/s; $1/\eta = 6$ bits.
2. Flujo ofrecido $\lambda_i/\eta$ = 1200, 600, 300, 300 bps → total 2400 bps.
3. $\rho = 2400/5000 = 0{,}48$; remanente $C(1-\rho) = 2600$ bps.
4. $\sum\sqrt{\lambda_i/\eta} = \sqrt{1200}+\sqrt{600}+2\sqrt{300} = 34{,}64+24{,}49+17{,}32+17{,}32 = 93{,}78$.
5. $C^{opt}$: Santa Fe $1200 + 2600\cdot34{,}64/93{,}78 = $ **2160,4 bps**; Venado Tuerto $600 + 2600\cdot24{,}49/93{,}78 = $ **1279,1 bps**; Villa Constitución y Cañada **780,2 bps** c/u. Suma = 5000 ✓.
6. Retardos: $T_i = 1/(C_i/6 - \lambda_i)$ → 6,25 ms; 8,83 ms; 12,49 ms; 12,49 ms.
7. $\bar T_{min} = 93{,}78^2/(400\cdot2600) = $ **8,46 ms** (coincide con $\frac1\gamma\sum\lambda_iT_i$ ✓).

**E6.4 — Retardo de un enlace (Ejercitación y apunte).**
- Nodo de 1200 bps, mensajes de 120 bits: $\eta C = 1200/120 = 10$ msg/s. Para $T \le 2$ s: $1/(10-\lambda) \le 2$ → $\lambda \le 9{,}5$ msg/s. Si $\lambda \to \eta C = 10$, $T\to\infty$.
- Ej. del apunte: $\lambda = 0{,}33$ msg/s, 120 bits, $C = 100$ bps → $\eta C = 0{,}833$, $T = 1/(0{,}833-0{,}33) \approx 2$ s, de los cuales 1,2 s son transmisión (120/100) y ~0,8 s espera en buffer.
- Centro de cómputos: 120 msg/h ($\lambda = 1/30$ msg/s), 144 caracteres a 8 car/s → $E[s] = 18$ s, $\rho = 0{,}6$ (utilización del enlace), $W_q = 27$ s, $W = 45$ s.

**E6.5 — Modelo cerrado (Ejercitación).** 5 terminales, $E[t] = 6$ s, CPU de 15.000 inst/s, 20.000 inst/interacción.
1. $E[s] = 20000/15000 = 1{,}333$ s; $N^* = (1{,}333+6)/1{,}333 = $ **5,5 terminales**.
2. $N=5$: $p_0 = 0{,}243$, $\rho = 0{,}757$, $T = 0{,}568$ int/s, $W = 5/0{,}568 - 6 = 2{,}81$ s, $L = 1{,}59$.
3. $N=7$ (> $N^*$): $p_0 = 0{,}090$, $\rho = 0{,}910$, $T = 0{,}682$ int/s, $W = 4{,}26$ s, $L = 2{,}91$. Pasar de 5 a 7 (+40 %) sube el throughput sólo 20 % y el tiempo de respuesta 52 %: ya se pasó el punto de saturación.

#### Dudas / pendientes
- **Errata del apunte de colas (ej. 3)**: imprime $W = 1{,}91$ s para 20 terminales; con las fórmulas del modelo da **1,19 s**, que es lo único consistente con $L = 5{,}68 = T\cdot W$ y con "+150 % de tiempo de respuesta" al pasar a 30 terminales (3,00 s). Verificado numéricamente.
- Las fórmulas de M/M/c, Erlang C, $p_0$ del modelo cerrado y $T_i$/$C^{opt}$ son imágenes no convertidas en los apuntes. Se reconstruyeron con conocimiento general y con El Santo Resumen; todas reproducen los números del apunte que sobrevivieron a la conversión (50/80/146,6 min del ej. 1; $p_0 = 0{,}0456$, $T = 4{,}772$, $L = 5{,}68$ y los valores para 30 terminales del ej. 3; ρ = 0,0453 de la red de 4500 bps) y la conclusión del ej. 2 (M/M/2 cumple, dos M/M/1 no). Los valores 3,25 y 8,67 min del ej. 2 son cálculo propio: el apunte perdió esos números.
- Final 2025, inciso b) "tiempo promedio que el paciente espera en sala de espera de emergencias": se interpreta como **tiempo en el sistema** $W$ (contrasta con a) = $W_q$); la resolución de alumno de 2021 lo toma igual. Redacción ambigua: aclararlo en el examen.
- "Resumen" (para el final) define el punto de saturación como "número máximo de **servidores**": incorrecto, son **terminales/usuarios** (apunte y Preguntas frecuentes).
- Notación: la cátedra usa $\mu$ tanto para frecuencia de servicio (colas) como para niveles (multinivel); en asignación de capacidad usa $\mu_i = \eta_iC_i$ y $1/\eta_i$ = longitud media. El apunte imprime $\delta$ donde va $\rho$ y un símbolo tipo ∝ para el multiplicador de Lagrange (erratas señaladas por El Santo Resumen).
- La práctica de colas pide "π(90) del tiempo de espera": se usó $\pi_q(90)$ (como el apunte, 146,6 min).

#### Fuentes
- `fuentes/teoria/Teoría de Colas.md`
- `fuentes/teoria/Asignación de Capacidad de Canales.md`
- `fuentes/practica/Ejercitación Teoría de cola.md`
- `fuentes/practica/Ejercitación Asignación de Capacidad.md`
- `fuentes/resumenes/Para rendir el final/Teoría - Preguntas frecuentes (Parte 1).md` y `(Parte 2).md` (punto de saturación, Kendall)
- `fuentes/resumenes/Para rendir el final/Resumen.md`
- `fuentes/resumenes/2° Parcial/Resumen Parcial 2 (2025).md`
- `fuentes/resumenes/El Santo Resumen/el-santo-resumen.md` (Teoría de colas, Asignación de capacidad)
- `fuentes/finales/Práctica/2025/2025-04-04.jpg`, `fuentes/finales/Práctica/2020/Comunicaciones - Final - 2020-11-20.md`, `fuentes/finales/Práctica/2021/Comunicaciones - Final - 2021-11-19.md` (+ PDF con resolución), `fuentes/finales/Teoría/2021/Comunicaciones - Final - 2021-12-17 (Solucion sin corregir).md`

---

### Unidad 7 — Modelo OSI, TCP/IP y hardware de redes

#### Conceptos clave
- Clasificación de redes por **tecnología de transmisión** (difusión vs punto a punto) y por **escala** (PAN, LAN, MAN, WAN, interred).
- **OSI** (ISO): 7 capas; es un modelo de referencia, **no una arquitectura** (dice qué hace cada capa, no qué protocolos usar). Capas 1–3 encadenadas salto a salto; 4–7 extremo a extremo.
- **TCP/IP**: 4 capas (host a red, interred, transporte, aplicación); los protocolos vinieron primero y el modelo los describe. Sin sesión ni presentación.
- OSI aporta la distinción **servicio / interfaz / protocolo**.
- **Capa 1** transmite bits puros (voltios, duración del bit, pines, medio); **capa 2** convierte ese medio en una línea libre de errores no detectados: tramas, acuse, control de flujo, subcapa MAC en redes de difusión.
- TCP confiable y orientado a conexión; UDP no confiable, sin conexión (voz, video, consultas únicas).

#### Desarrollo

##### 1. "Hardware de redes": clasificación
**Por tecnología de transmisión.**
- *Difusión (broadcast)*: un solo canal compartido; el paquete lo reciben todos y cada uno mira la dirección (como gritar "¡Jorge!" en un pasillo). Admite broadcast y multicast. Típico de redes chicas.
- *Punto a punto*: conexiones entre pares; el paquete puede pasar por máquinas intermedias y hay que encontrar la ruta. Un emisor y un receptor = unicast. Típico de redes grandes.

**Por escala.**

| Tipo | Alcance | Características del apunte |
|---|---|---|
| PAN | una persona (~1 m) | Bluetooth: maestro/esclavo |
| LAN | edificio o campus | Privada, retardo acotado y conocido, 10 Mbps–10 Gbps, pocos errores. Topologías bus (Ethernet 802.3, CSMA con reintento aleatorio) y anillo (Token Ring 802.5, FDDI). Asignación estática (round‑robin) o dinámica |
| MAN | ciudad | TV por cable devenida acceso a Internet; WiMAX (802.16) |
| WAN | país o continente | Hosts + **subred** (líneas de transmisión + elementos de conmutación = enrutadores); store‑and‑forward; también WAN satelitales (de difusión) |
| Interred | redes distintas conectadas | Vía **gateways**; ej. Internet, LANs unidas por una WAN |

Subred = sólo enrutadores y líneas del operador; red = subred + hosts; interred = varias redes de distintos dueños o tecnologías.

*(Conocimiento general, por si lo preguntan como "hardware de redes")*: dispositivos por capa — repetidor y hub (capa 1), puente y switch (capa 2), router (capa 3), gateway (capas 4–7).

##### 2. Modelo OSI
Principios: una capa donde haga falta otra abstracción; función bien definida; pensada para protocolos estandarizados; límites que minimicen el flujo entre interfaces; ni tan pocas capas que mezclen funciones ni tantas que se vuelva inmanejable.

| # | Capa | Qué hace |
|---|---|---|
| 7 | Aplicación | Protocolos que usan los usuarios: HTTP, transferencia de archivos, correo |
| 6 | Presentación | Sintaxis y semántica de los datos; codificación estándar "en el cable" |
| 5 | Sesión | Sesiones: control de diálogo, manejo de token, sincronización (puntos de control) |
| 4 | Transporte | Extremo a extremo: segmenta, entrega correcta y en orden, aísla a las capas superiores del hardware |
| 3 | Red | Opera la subred: enrutamiento, control de congestión, calidad de servicio, interconexión de redes heterogéneas |
| 2 | Enlace de datos | Tramas, confirmación, control de flujo; subcapa MAC (acceso al canal compartido) |
| 1 | Física | Bits puros por el canal: niveles de tensión, duración del bit, dúplex, conectores; el medio está debajo |

**Relación capa 1 – capa 2** (2° parcial 2025): la física sólo garantiza que un 1 enviado llegue como 1 —con errores posibles por ruido—; la de enlace toma ese flujo de bits crudo, lo **organiza en tramas**, **detecta/corrige errores** (acá viven los códigos de la Unidad 3: paridad, Hamming, CRC) y **regula el flujo**, entregándole a la capa de red una línea que parece libre de errores. Todo lo de las Unidades 4 y 5 (modulación, multiplexado, medios) es capa 1.

##### 3. Modelo TCP/IP y comparación

| OSI | TCP/IP | Protocolos |
|---|---|---|
| Aplicación / Presentación / Sesión | Aplicación | TELNET, FTP, SMTP, DNS, HTTP |
| Transporte | Transporte | TCP (confiable, con conexión, control de flujo), UDP (no confiable, sin conexión) |
| Red | Interred | IP: conmutación de paquetes **sin conexión**; los paquetes viajan independientes y pueden llegar desordenados |
| Enlace + Física | Host a red | No definido: "el host se conecta con algún protocolo que pueda mandar paquetes IP" |

| Aspecto | OSI | TCP/IP |
|---|---|---|
| Orden | Modelo antes que protocolos → general, pero sin experiencia práctica | Protocolos antes que modelo → encajan perfecto, pero no describe otras pilas |
| Capas | 7 | 4 |
| Servicio/interfaz/protocolo | Distinción explícita (como objetos: métodos, parámetros, implementación) | No los distingue |
| Conexión en capa de red | Con y sin conexión | Sólo sin conexión |
| Conexión en transporte | Sólo con conexión | Con (TCP) y sin (UDP) |
| Uso actual | El modelo sigue vigente, los protocolos no | Los protocolos se usan, el modelo poco |

Por qué fracasó OSI: **aparición inoportuna** (TCP/IP ya estaba instalado en las universidades), **mala tecnología** (7 capas por política, sesión y presentación casi vacías, funciones repetidas), **malas implementaciones** (lentas; TCP/IP venía gratis en UNIX de Berkeley) y **malas políticas**. Crítica a TCP/IP: no separa servicio/interfaz/protocolo y su capa host‑a‑red no es realmente una capa.

#### Ejercicios resueltos tipo

**E7.1 — "¿Qué hace la capa 1 de OSI y cómo se relaciona con la capa 2?" (2° parcial 23/10/2025).**
Respuesta modelo: la capa física transmite bits puros por un canal de comunicación; define cuántos voltios representan un 1 y un 0, cuánto dura un bit, si la transmisión es simultánea en ambos sentidos, cómo se establece y libera la conexión y qué tiene cada pin del conector; debajo está el medio físico. No garantiza ausencia de errores. La capa de enlace usa ese servicio: divide los datos en tramas, las envía en secuencia, el receptor confirma con tramas de acuse, controla el flujo para que un emisor rápido no sature a uno lento y, en redes de difusión, su subcapa MAC arbitra el acceso al canal. Así transforma el medio crudo en una línea que la capa de red ve libre de errores no detectados.

**E7.2 — Ubicar en capas los temas de la materia.**
1. Modulación ASK/FSK/PSK, PCM, FDM/TDM/WDM, par trenzado, fibra, satélite → **capa 1**.
2. Códigos detectores/correctores (Hamming, síndrome), tramas, control de flujo → **capa 2**.
3. Enrutamiento entre concentradores, congestión (lo que modela la asignación de capacidad) → **capa 3**.
4. Conexión TCP extremo a extremo entre la terminal y la CPU central → **capa 4**.

#### Dudas / pendientes
- El título del apunte habla de "hardware de redes", pero el contenido es la clasificación de redes (Tanenbaum, cap. 1), no dispositivos. La tabla de dispositivos por capa es conocimiento general.
- En las hojas de examen 2023–2025 leídas por El Santo Resumen sólo aparece "capa 1 y su relación con la capa 2". Prioridad baja para el final frente a las Unidades 4–6.
- La crítica a TCP/IP está cortada en la conversión (el .md termina a mitad de la sección); se completó con lo estándar de Tanenbaum (conocimiento general).

#### Fuentes
- `fuentes/teoria/OSI TCP_IP y HARDWARE DE REDES.md`
- `fuentes/resumenes/2° Parcial/Resumen Parcial 2 (2025).md` (OSI, TCP/IP, redes)
- `fuentes/resumenes/El Santo Resumen/el-santo-resumen.md` (Modelo OSI)

## Log
- 2026-11-24: Alta de la materia (código CD). Se bajó el Drive de la facu (`3º AÑO/Comunicación de Datos`, 102 archivos) a `archivo/`. Las unidades salen de la teoría de la cátedra y del final de 2025. Todavía no se ingirió nada.
- 2026-11-24: Ingesta de la teoría, la práctica, los resúmenes (incluido *El Santo Resumen*) y los finales. Desarrollo completo de las Unidades 4–7 (comunicaciones digitales, PCM y ADSL; medios y elección del medio de acceso; asignación de capacidad y colas; OSI/TCP-IP), con ejercicios del final 2025 resueltos. Erratas de las fuentes anotadas en Dudas: el ancho de banda PCM con $f_{min}$ (2·fmax vs fmax−fmin), W del ejemplo 3 del apunte de colas y I del ej. 2 de la práctica de multinivel.
