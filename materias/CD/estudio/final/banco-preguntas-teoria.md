# Comunicación de Datos — Banco de preguntas de teoría (finales)

UTN FRRo · ISI · 3° año · Teoría: Ing. Jorge A. Campanaro.

**Qué hay acá.** Todas las preguntas de teoría de los finales disponibles, agrupadas por tema y con **respuesta modelo** de extensión de examen escrito. Las preguntas equivalentes están fusionadas, con todas sus fechas. Desde la cursada 2025 suma también las preguntas conceptuales de los parciales de Medín y Baró, marcadas con su origen.

**Finales relevados** (en `materias/CD/fuentes/finales/Teoría/`):

| Código | Fecha | Formato | ¿Trae respuestas marcadas? |
|---|---|---|---|
| F1 | 28/08/2020 | Multiple choice (MC), virtual | Sí, de un alumno, "sin corregir" |
| F2 | 18/12/2020 | MC, virtual (escaneo) | Sí, de un alumno (resaltado amarillo) |
| — | 2020 s/f ("2020-00-00") | MC | **Es el mismo examen que el 18/12/2020** (mismas preguntas, mismas marcas). Se cuenta como F2. |
| F3 | 10/09/2021 | MC, virtual | Sí, de un alumno, "sin corregir" |
| F4 | 19/11/2021 | MC, virtual | No |
| F5 | 17/12/2021 | MC, virtual | Sí, de un alumno, "sin corregir" |
| F6 | 04/04/2025 | **Desarrollo** (3 consignas) | No. Es el único final del plan actual. |
| FAQ | s/f | Desarrollo | "Teoria vieja.md" + "Preguntas frecuentes (Parte 1 y 2)": preguntas de finales viejos con respuestas de alumnos (no oficiales). |

> Las marcas de los alumnos se leyeron de los PDF (relleno de color) y de los escaneos. **No son confiables**: los errores detectados están en [Dudas / pendientes](#dudas--pendientes). Las respuestas de este banco salen de los apuntes de la cátedra (`fuentes/teoria/`, `fuentes/practica/3 - Medios de transmisión.md`) y, donde el apunte no está en el repo, del *Santo Resumen*, que cita página del apunte.

**Material de la cursada 2025** (com. 303: teoría Medín, práctica Baró; en `fuentes/cursada-2025/drive-propio/`). No son finales, pero son el plan actual y comparten temas con el final. Se citan con estos códigos:

| Código | Fuente | Qué aporta |
|---|---|---|
| M1 | `Resumen Comunicación de Datos - Medin 1er Parcial.md` | Resumen del alumno del 1.er parcial: información, canales, codificación, síndrome. Parte Baró: sistema de comunicación, perturbaciones, ganancia/atenuación, dB, rango dinámico, S/R, multinivel, Hamming. |
| M2 | `Resumen de Comunicación de datos - 2do parcial teoría.md` | 2.º parcial de Medín: elección del medio de acceso, segurización, radioenlace, asignación de capacidad (Kleinrock), colas. Incluye un parcial resuelto de la com. 305 (código **305**). |
| B2 | `2do Parcial - Comunicacion De Datos - Baró.md` | Compendio de MC del 2.º parcial de Baró (medios de transmisión), con la opción marcada por un alumno. |
| B3 | `Resumen de Comunicación de datos - 3er parcial Práctica.md` | 3.er parcial de Baró: modulación AM/FM/PM, ASK/FSK/PSK, TDM, muestreo, cuantificación, PCM; "Ejercicio 1 – Definiciones". |
| HFC | `Tps Baro/TP N°1 - Cables HFC.md` | TP de práctica (2024) sobre redes HFC y DOCSIS. |

> Son resúmenes de alumnos. Las marcas dudosas del compendio B2 están en [Dudas E](#e-marcas-del-compendio-mc-de-baró-b2) y los errores de los resúmenes, en [Dudas F](#f-errores-en-los-resúmenes-de-la-cursada-2025-m1-m2-b3).

Rutas de las citas, relativas a `materias/CD/fuentes/`. "(conocimiento general)" = no está en el material de la cátedra.

---

## Frecuencia de temas

★ = salió en 4 o más finales · ★★ = salió en 6 (todos los que tenían ese bloque).
**Cursada 2025** (nota): en qué parcial de 2025 aparece el tema (M1, M2, B2, B3, 305; ver códigos arriba). No suma a la columna *Finales*.

| Tema | 28/08/20 | 18/12/20 | 10/09/21 | 19/11/21 | 17/12/21 | 04/04/25 | FAQ (s/f) | Finales | Cursada 2025 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Inecuación de Kraft | X | X | X | X | X | X | X | **6 ★★** | M1 |
| Cota inferior de la longitud media | X | X | X | X | X | X | X | **6 ★★** | M1 |
| Elección del medio de acceso (zona × velocidad) | X | X | X | X | X | X | X | **6 ★★** | M2 |
| Código unívoco | X | | X | X | X | X | X | **5 ★** | M1 |
| Código compacto | X | | X | X | X | X | X | **5 ★** | |
| Código bloque / palabra código / no singular | X | X | X | X | X | | X | **5 ★** | M1 |
| Distancia de un código / $d_{min}=1$ | X | X | X | X | X | | | **5 ★** | |
| Tasa de información / tasa de dígitos | X | X | X | X | X | | X | **5 ★** | M1 |
| FDM (concepto, ancho de banda, duplicar señales) | X | X | X | X | X | | X | **5 ★** | |
| TDM (concepto) | X | X | X | X | X | | X | **5 ★** | B3 |
| Digitalización: muestreo, Nyquist, PCM | X | X | X | X | X | | X | **5 ★** | B3 |
| AM (definición, bandas laterales, portadora suprimida) | X | X | X | X | X | | | **5 ★** | B3 |
| Mensaje digital por red analógica (ASK/FSK/PSK, multinivel) | X | X | X | | | X | X | **4 ★** | B3 |
| Código instantáneo y su condición | X | X | X | | | X | X | **4 ★** | M1 |
| Información mutua | X | | X | X | X | | X | **4 ★** | M1 |
| Familia de errores de un síndrome | X | | X | X | X | | | **4 ★** | M1 |
| Medios: fibra, radio, satélite (propiedades) | X | X | X | | | X | X | **4 ★** | **B2** (≈45 MC) |
| Entropía de la fuente | X | X | X | | | | X | 3 | M1 |
| Canal binario simétrico / entropía del canal | | X | | X | X | | X | 3 | M1 |
| Síndrome (concepto) | | X | | X | X | | X | 3 | M1 |
| Matriz generadora / base de un código de grupo | X | | X | | | | X | 2 | |
| Colas: punto de saturación, intensidad de tráfico | | | | X | X | | X | 2 | M2, 305 |
| Errores de canal / ruido impulsivo / perturbaciones | | | | | | | X | 0 (solo FAQ) | M1 |
| Huffman, extensión r-aria | | | | | | | X | 0 (solo FAQ) | |
| Colas abiertas: elementos, M/M/1, Little, percentil 90, Kendall | | | | | | | X | 0 (solo FAQ) | M2, 305 |
| Asignación de capacidad de canales (Kleinrock) | | | | | | | | 0 | M2 |
| Cantidad de información de un suceso; capacidad y eficiencia del canal | | | | | | | | 0 | M1 |
| Atenuación, ganancia, dB, rango dinámico, S/R | | | | | | | | 0 | M1 |
| Hamming: cantidad de bits de control | | | | | | | | 0 | M1 |
| Modulación (concepto, portadora, FM/PM), ancho de banda, armónicos | | | | | | | | 0 | B3 |
| OSI/TCP-IP, CDM/WDM | | | | | | | | 0 | |

**Lectura rápida.** El núcleo que se repite en todos los finales es **codificación de fuente** (unívoco, instantáneo, Kraft, compacto, cota inferior) y **elección de medio de acceso**. Lo segundo más frecuente: **FDM/TDM/muestreo/AM** y **distancia/síndrome**. El final de 2025 (plan actual) pasó a desarrollo pero repitió exactamente esos tres bloques: modulación digital sobre red analógica, códigos y medios de acceso.

**Cursada 2025.** Medín repite en el 1.er parcial el mismo núcleo de información y codificación (M1) y en el 2.º suma asignación de capacidad y colas (M2). Baró evalúa medios de transmisión con MC de datos puntuales (B2) y, en el 3.º, definiciones de modulación y PCM (B3). Los temas en 0 de esa parte (dB, S/R, Kleinrock, colas abiertas) no salieron en los finales relevados, pero son del programa actual.

---

## 1. Teoría de la información

### 1.1 Entropía de la fuente: concepto, fórmula, cuándo es máxima
**Salió:** 18/12/2020 (MC "La entropía de la fuente es…"), 28/08/2020 y 10/09/2021 (MC "La función entropía es…"), FAQ ("Definir entropía", "¿Cuándo la entropía es máxima?"); cursada 2025: M1, con la definición textual y el máximo en símbolos equiprobables (parcial Medín 2025, resumen del alumno).

**Respuesta.** La entropía $H(S)$ es la **esperanza matemática de la información por símbolo de la fuente**, o sea, la cantidad media de información que aporta cada símbolo emitido. Si el símbolo $s_i$ tiene probabilidad $p_i$, la información que aporta es $I(s_i)=\lg\frac{1}{p_i}$ (con $\lg=\log_2$, unidad *bit*), y entonces:

$$H(S)=\sum_{i=1}^{q} p_i\,\lg\frac{1}{p_i} = -\sum_{i=1}^{q} p_i\,\lg p_i \quad [\text{bit/símbolo}]$$

También se interpreta como medida de **incertidumbre**: cuanto más parejas son las probabilidades, menos se puede anticipar qué símbolo sale y mayor es $H$.

- **Máximo:** se alcanza cuando los $q$ símbolos son **equiprobables**: $H_{max}=\lg q$.
- **Mínimo:** $H=0$ si un símbolo tiene probabilidad 1 (no hay incertidumbre).
- **Ejemplo:** fuente de 4 símbolos equiprobables → $H=\lg 4=2$ bit/símbolo. Si las probabilidades son 1/2, 1/4, 1/8, 1/8 → $H=1{,}75$ bit/símbolo (menor, porque hay un símbolo "esperable").

Fuente binaria ($p$, $1-p$):
```
 H(p) [bit]
 1 ┤        ****
   │     **      **
   │   *            *
   │  *              *
   │ *                *
 0 ┼*──────────────────*── p
   0        0,5         1      máximo = 1 bit en p = 0,5
```

**En el MC:** la opción correcta es "la esperanza matemática de la información por símbolo **de la fuente**" (las otras omiten "de la información" o "de la fuente"). En la fórmula, la correcta es $H(x)=\sum p(x_i)\,\lg\frac{1}{p(x_i)}$ en bit/símbolo: el apunte escribe **lg** (logaritmo en base 2), que es lo que da *bits*. La opción con $\log p$ sin el $1/p$ da negativo; la de $\ln$ da *nats*, no binits.

(teoria/1 - Información, Codificación y Canales.md)

### 1.2 Tasa de información, tasa de dígitos y velocidad de señalización
**Salió:** tasa de información en 18/12/2020, 19/11/2021 y 17/12/2021 (MC); tasa de dígitos en 28/08/2020 y 10/09/2021 (MC); FAQ "Concepto de entropía, tasa de información, tasa de dígitos y velocidad de señalización. Dar ejemplos"; cursada 2025: M1, en la parte de Medín y en la de Baró, con la deducción de multinivel (parcial Medín y Baró 2025, resumen del alumno).

**Respuesta.**
- **Tasa (velocidad) de información $R$:** cantidad de bits **en promedio** que se transmiten en 1 segundo, es decir, la información **promedio** que produce la fuente **por unidad de tiempo**. $R = H'(A)$ [bit/s]. Con canal ruidoso, a la salida llega $R = H'(A) - H'(A/B)$.
- **Tasa de dígitos (binits) $r$:** cantidad de **dígitos transmitidos por segundo** [dígitos/s]. Se relaciona con la anterior por $R = r\cdot H(A)$: $H$ mide información en bit/símbolo, $R$ en bit/s.
- **Velocidad de señalización $s$:** inversa de la duración del pulso más corto, $s = 1/\tau_{min}$ [baudios]. Con pulsos de $n$ niveles equiprobables e iguales duraciones: $R = \frac{1}{\tau}\lg n = s\,\lg n$.
- **De dónde sale (Baró, M1):** un mensaje de duración $T$ tiene $T/\tau$ pulsos de $\mu$ niveles, así que hay $M(T)=\mu^{T/\tau}$ mensajes distintos. Lleva $I=\lg M(T)$ bits y $R=\frac{I}{T}=\frac{1}{\tau}\lg\mu$. Con $\tau=\tau_{min}$, $R=s\lg\mu$.

**Ejemplo:** pulsos de $\tau = 1$ ms con 4 niveles equiprobables → $s = 1000$ baudios, $r = 1000$ dígitos/s, $H = \lg 4 = 2$ bit/dígito, $R = r\,H = 2000$ bit/s. Si los pulsos fueran binarios, $R = s = 1000$ bit/s: en binario equiprobable **la capacidad coincide con la señalización**.

**En el MC:** tasa de información = "la información **promedio** que emite la fuente **por unidad de tiempo**" (la que dice "la información que emite…" sin "promedio" no es la definición). Tasa de dígitos = "la cantidad de dígitos transmitidos por segundo" (no son "dígitos de información" ni "dígitos de señalización").

(teoria/1 - Información, Codificación y Canales.md)

### 1.3 Canal binario simétrico (BSC)
**Salió:** 18/12/2020, 19/11/2021, 17/12/2021 (MC); cursada 2025: M1, con la definición de canal, el canal transparente (matriz diagonal) y el BSC (parcial Medín 2025, resumen del alumno).

**Respuesta.** Un canal queda definido por su alfabeto de entrada $A$, su alfabeto de salida $B$ y la matriz de probabilidades condicionales $P(b_j/a_i)$. El **canal binario simétrico** tiene **dos entradas** ($a_1=0$, $a_2=1$) y dos salidas ($b_1=0$, $b_2=1$), y es simétrico porque **la probabilidad de recibir un 0 cuando se envió un 1 es igual a la de recibir un 1 cuando se envió un 0**: $P(b_1/a_2)=P(b_2/a_1)=p$ (probabilidad de error).

```
        1−p
 a1=0 ───────→ b1=0          Matriz del canal:
      ╲      ╱
       ╲ p  ╱                  ┌ 1−p   p  ┐
        ╳                      └  p   1−p ┘
       ╱ p  ╲
      ╱      ╲
 a2=1 ───────→ b2=1
        1−p
```

La simetría es del **canal** (probabilidades condicionales), no de la fuente: no exige que las entradas sean equiprobables.

**En el MC:** "Posee dos entradas y la probabilidad condicional $P(b_1/a_2)=P(b_2/a_1)$". La opción "independientemente del número de entradas…" es falsa: el BSC es binario por definición.

(teoria/1 - Información, Codificación y Canales.md)

### 1.4 Información mutua, entropía del canal (canal real)
**Salió:** información mutua en 28/08/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC); FAQ "Concepto de entropía, de información mutua y de entropía del canal", "En un canal real, ¿cuál es la entropía que lo define y cuál es su concepto?"; cursada 2025: M1, con probabilidades a priori y a posteriori, Bayes, las dos equivocaciones y la información mutua (parcial Medín 2025, resumen del alumno).

**Respuesta.**
- **Entropía a priori** $H(A)$: incertidumbre sobre la fuente antes de recibir. Usa la **probabilidad a priori** $P(a_i)$.
- **Probabilidad a posteriori** ("hacia atrás") $P(a_i/b_j)$: probabilidad de que, recibido $b_j$, se haya enviado $a_i$. Sale por Bayes: $P(a_i/b_j)=\frac{P(a_i)\,P(b_j/a_i)}{P(b_j)}$.
- **Equivocación de A respecto de B** $H(A/B)=-\sum_j\sum_i P(b_j)\,P(a_i/b_j)\lg P(a_i/b_j)$ (entropía a posteriori): incertidumbre que **queda** sobre la fuente después de recibir. Es la información que "bloquea" el canal.
- **Entropía del canal** = **equivocación de B respecto de A**:
$$H(B/A) = -\sum_i\sum_j P(a_i)\,P(b_j/a_i)\,\lg P(b_j/a_i)$$
Es la incertidumbre sobre la salida conociendo la entrada: la mide **el ruido** del canal. Es la entropía que caracteriza a un canal real. En un canal transparente (matriz diagonal, sin error) vale 0.
- **Información mutua** $I(A,B)$: es la **información transferida desde la fuente al receptor a través del canal**, esto es, la información real que llega al receptor en promedio:
$$I(A,B)=H(A)-H(A/B)=H(B)-H(B/A)=I(B,A)$$
Es simétrica. Si el canal es transparente, $I(A,B)=H(A)$; si la salida es independiente de la entrada, $I=0$.
- **Capacidad** $C=\max I(A,B)$ sobre las probabilidades de entrada. Depende solo de la matriz del canal.

**Ejemplo:** BSC con $p=0{,}1$ y entrada equiprobable: $H(B/A)=0{,}1\lg 10+0{,}9\lg\frac{1}{0{,}9}\approx 0{,}469$ bit, $H(B)=1$, $I = 1-0{,}469 = 0{,}531$ bit/símbolo.

**En el MC:** "La información transferida desde la fuente al receptor a través del canal". El apunte agrega "esto es, la información real que llega al receptor **en promedio**", así que esa opción también reproduce el apunte (ver Dudas).

(teoria/1 - Información, Codificación y Canales.md)

### 1.5 Cantidad de información de un suceso; el bit
**Salió:** cursada 2025: M1 (Medín: propiedades de $I(A)$; Baró: definición de bit y alfabeto n-ario) (parcial Medín y Baró 2025, resumen del alumno). No salió en los finales relevados.

**Respuesta.** La cantidad de información $I(A)$ que aporta un suceso es función inversa de su probabilidad: cuanto menos esperable es, más informa.
$$I(A)=\lg\frac{1}{p(A)}\quad[\text{bit}]$$
- Si $p(A)\to1$, $I(A)\to0$: un suceso seguro no informa.
- Si $p(A)\to0$, $I(A)\to\infty$.
- Para sucesos independientes, $p(A\cap B)=p(A)\,p(B)$ y la información se **suma**: $I(A\cap B)=I(A)+I(B)$. Esa aditividad es la que lleva al logaritmo; con base 2 la unidad es el *bit*.
- **Bit:** cantidad de información que aporta la aparición de un símbolo de un alfabeto binario (equiprobable). En un alfabeto de $n$ símbolos equiprobables, cada carácter aporta $I=\lg n$.
- Si se promedia $I$ sobre todos los símbolos de la fuente, con las frecuencias relativas como probabilidades, se llega a la entropía (§1.1).

**Ejemplo:** un suceso de $p=1/8$ aporta $\lg 8=3$ bit; un dígito decimal equiprobable, $\lg 10\approx3{,}32$ bit.

(teoria/1 - Información, Codificación y Canales.md; cursada-2025/drive-propio/Resumen Comunicación de Datos - Medin 1er Parcial.md)

### 1.6 Capacidad del canal, eficiencia y redundancia; tasa $R$ frente a $C$
**Salió:** cursada 2025: M1 (parcial Medín y Baró 2025, resumen del alumno). En los finales solo aparece $C$ de pasada (§1.4).

**Respuesta.**
- **Capacidad:** $C=\max I(A,B)$, maximizando sobre las probabilidades de entrada (se "sintoniza" la fuente). Depende **solo** de la matriz $P(b_j/a_i)$. En un canal **transparente** $H(A/B)=0$, $I=H(A)$, y entonces $C=\max H(A)=\lg n$ bit/símbolo, con la fuente equiprobable. Binario: $C=1$ bit/símbolo, o $C=1/\tau$ bit/s.
- **Eficiencia de transmisión:** $FF=I(A,B)/C$.
- **Redundancia de transmisión:** $RED=1-FF$, la parte de la capacidad del canal que no se aprovecha.
- **Tasa vs. capacidad** (Shannon): si la fuente tiene tasa $R<C$, existe una codificación que transmite con probabilidad de error arbitrariamente pequeña pese al ruido. Si $R>C$, no es posible. En bit/s, $C$ depende del ancho de banda y de la S/N (§dB.4), y del medio (cobre, fibra).

**Ejemplo:** BSC con $p=0{,}1$ → $C=1-H(0{,}1)\approx0{,}531$ bit/símbolo, con entrada equiprobable. Si la fuente emite $P(0)=0{,}9$: $P(b_1)=0{,}82$, $H(B)\approx0{,}680$, $I=0{,}680-0{,}469=0{,}211$ bit → $FF\approx0{,}40$ y $RED\approx0{,}60$.

(teoria/1 - Información, Codificación y Canales.md; cursada-2025/drive-propio/Resumen Comunicación de Datos - Medin 1er Parcial.md)

---

## 2. Errores de canal

### 2.1 Efecto del ruido de canal y sus causas; ruido impulsivo
**Salió:** FAQ ("¿Qué efecto produce el ruido de canal? Nombre tres causas", "Ruido impulsivo: definirlo y explicar sus fuentes", "Causas de errores de canal").

**Respuesta.** El ruido **limita la capacidad del canal** para transmitir información e introduce errores cuando cae en la banda de la señal. Por Hartley-Shannon, $C = B\,\lg(1+S/N)$ [bit/s]: a igual ancho de banda, más ruido implica menos capacidad.

- **Ruido blanco:** se debe a la agitación térmica de átomos y moléculas. Es aleatorio y **no se puede eliminar**.
- **Causas de error de canal:**
  1. **Ruido impulsivo** (la principal): picos grandes de amplitud sobre el ruido blanco que saturan el canal y alteran **varios binits seguidos (ráfaga)**. Causas **externas**: acoplamientos capacitivos o inductivos por canales paralelos, conmutación mecánica, señales de supervisión y fenómenos atmosféricos. Causas **internas**: variaciones de impedancia en conexiones, sobrecarga de amplificadores y armónicas espurias generadas por filtros. Se contrarresta con módems adecuados.
  2. **Modulaciones espurias:** **cruzada** (captación de otros canales por acoplamiento), **intermodulación** (alinealidad de amplificadores en canales multiplex; se corrige con módems o bajando la amplitud) y **eco** (reflexiones por variación de impedancia; se usan supresores de eco).
  3. **Variaciones de nivel (desvanecimiento):** variaciones de impedancia, fallas de contactos o de amplificadores, lluvia en microondas.
  4. **Distorsión** que introduce el propio canal: atenuación, distorsión fase/frecuencia, variación de la frecuencia de la portadora y variación del nivel de muestreo. Es sistemática, así que se corrige por diseño.

(teoria/Errores en Canales.md)

### 2.2 Sistema de comunicación y perturbaciones: distorsión, interferencia y ruido
**Salió:** cursada 2025: M1, parte Baró (parcial Baró 2025, resumen del alumno). En los finales, solo la variante FAQ del §2.1.

**Respuesta.** Bloques del sistema:
- **Fuente:** genera el mensaje.
- **Transductores** de entrada y salida: convierten el mensaje (acústico, visual, alfanumérico) en señal eléctrica y viceversa.
- **Transmisor:** filtrado, procesamiento y amplificación. Ahí se **modula** (corrimiento en frecuencia para adaptar la señal al canal).
- **Canal:** el camino entre emisor y receptor. Ahí entran las perturbaciones.
- **Receptor:** demodula. Tiene que ser **sensible** (detectar señales débiles por encima del ruido) y **selectivo** (separar la señal útil de las demás).
- **Destino.**

```
 Fuente → Transductor → Transmisor ──── Canal ────► Receptor → Transductor → Destino
                         (modula)        ▲          (demodula)
                                   perturbaciones:
                         distorsión · interferencia · ruido
```

| Perturbación | Qué es | Origen | ¿Se elimina? |
|---|---|---|---|
| **Distorsión** | Alteración de la **forma** de la señal por la respuesta imperfecta del canal: atenúa distinto cada frecuencia (distorsión de amplitud) y la retrasa distinto (de fase o retardo de grupo). Desaparece cuando se deja de aplicar la señal. | El propio canal | Sí, en teoría: si es lineal se compensa. La de fase es la más difícil. |
| **Interferencia** | Señales extrañas, de forma parecida a la útil, que se meten en el canal | Generalmente artificial: canales adyacentes, encendido de motores, conmutación; natural: rayos | Sí, en teoría (filtrado, blindaje, separación de canales) |
| **Ruido** | Señal aleatoria e impredecible, independiente de la señal | Natural, sobre todo térmico | **No**, ni siquiera en teoría: solo se mejora la S/N (§dB.4) |

La **atenuación** es el efecto menos grave: solo baja la intensidad y se compensa amplificando.

(practica/1 - Principios Básicos de la Electrónica y las Comunicaciones.md; cursada-2025/drive-propio/Resumen Comunicación de Datos - Medin 1er Parcial.md)

---

## Atenuación, ganancia, dB y relación señal/ruido

> **Salió:** cursada 2025: M1, parte Baró (1.er parcial de Baró, resumen del alumno). No salió en los finales de teoría relevados; es el apunte «Principios Básicos» de la práctica.

### dB.1 Ganancia y atenuación
**Respuesta.**
- **Ganancia** = salida / entrada: $G_P=P_o/P_i$, $G_V=V_o/V_i$, $G_I=I_o/I_i$.
- **Atenuación** = entrada / salida $=1/G$. En sistemas pasivos (cables, redes resistivas), que siempre atenúan, se usa la atenuación como forma normal de expresar la transferencia.
- Las dos son **adimensionales** (se miden en "veces").
- **En cascada se multiplican:** dos tramos de atenuación 10 dan 100 veces. En dB se **suman** (10 dB + 10 dB = 20 dB), y por eso se usan logaritmos: comprimen rangos muy amplios y pasan productos a sumas.

### dB.2 El decibel
**Respuesta.**
- El **bel** es el logaritmo decimal de una relación de potencias; el **decibel** es su décima parte: $X_{dB}=10\log_{10}\frac{P_o}{P_i}$ (ganancia) o $10\log_{10}\frac{P_i}{P_o}$ (atenuación). Viene de la *Unidad de Transmisión* de la telefonía: una atenuación de 10 veces en 10 millas de línea patrón a 886 Hz.
- Con tensiones o corrientes **medidas sobre la misma impedancia**: $X_{dB}=20\log\frac{V_1}{V_2}=20\log\frac{I_1}{I_2}$, porque $P\propto V^2$.
- **Nivel relativo:** dos señales del mismo sistema comparadas entre sí. **Nivel absoluto:** una señal comparada con una referencia fija (p. ej. 1 mW → dBm; dBm es conocimiento general).
- Valores para tener a mano: ×2 de potencia ≈ +3 dB; ×10 = +10 dB; ×100 = +20 dB; mitad = −3 dB. Las frecuencias de corte de un sistema se definen a −3 dB (potencia mitad), y entre ellas queda su ancho de banda $AB=f_2-f_1$.

**Ejemplo:** amplificador con $P_i=1$ W y $P_o=10$ W → $G=10$ veces = 10 dB. Si antes hay un cable que atenúa 3 dB, la ganancia total es $10-3=7$ dB (≈ 5 veces).

### dB.3 Rango dinámico
**Respuesta.**
- Diferencia, en dB, entre el **nivel máximo** que puede entregar un dispositivo y el **ruido de fondo** que hay cuando no hay señal. Cuanto mayor, más "limpia" es la comunicación.
- En una cadena de dispositivos (emisor, amplificador, parlante), el rango dinámico real es el del **dispositivo con peores características**.
- Aparatos de calidad: de 80 a 95 dB. En un conversor digital de $n$ bits, $RD\approx20\log2^n\approx6n$ dB: 8 bits ≈ 48 dB, 16 bits ≈ 96 dB (el estándar del CD).

### dB.4 Relación señal/ruido (S/N)
**Respuesta.**
- $S/N=\frac{P_{señal}}{P_{ruido}}$: cociente de potencias, **adimensional**, que casi siempre se expresa en dB: $(S/N)_{dB}=10\log\frac{S}{N}$. Cuanto más alta, mejor: hay más información útil frente a lo no deseado.
- El ruido no se puede eliminar; lo único que se puede hacer es **mejorar la S/N** (más potencia o calidad de señal, mejor modulación, antenas directivas, receptor más sensible).
- Fija el techo de velocidad: Hartley-Shannon, $C=B\lg(1+S/N)$, con $S/N$ **en veces**, no en dB.

**Ejemplo:** canal telefónico con $B=3100$ Hz y $(S/N)=30$ dB → $S/N=1000$ → $C=3100\cdot\lg1001\approx30{,}9$ kbit/s.

(practica/1 - Principios Básicos de la Electrónica y las Comunicaciones.md; cursada-2025/drive-propio/Resumen Comunicación de Datos - Medin 1er Parcial.md; teoria/Errores en Canales.md para Hartley-Shannon)

---

## 3. Codificación de fuente

> Bloque más preguntado. En el MC las opciones difieren en una palabra: hay que saber la definición textual del apunte.

### 3.1 Código bloque y palabra código
**Salió:** código bloque en 18/12/2020; palabra código en 28/08/2020, 10/09/2021, 19/11/2021 y 17/12/2021 (MC); cursada 2025: M1, con alfabeto fuente/código, código bloque y palabra código (parcial Medín 2025, resumen del alumno).

**Respuesta.** Codificar es poner en correspondencia las secuencias del **alfabeto fuente** $S=\{s_1,\dots,s_q\}$ con secuencias de un **alfabeto código** $Z=\{z_1,\dots,z_r\}$.
- **Código bloque:** asigna a **cada símbolo del alfabeto fuente una secuencia fija de símbolos del alfabeto código**.
- **Palabra código:** cada una de esas **secuencias fijas de símbolos del alfabeto código**.

Ejemplo: $s_1\to 00,\ s_2\to 01,\ s_3\to 10,\ s_4\to 11$. Cada $s_i$ tiene asignada siempre la misma palabra.

**En el MC:** código bloque = "asigna a cada uno de los símbolos del alfabeto fuente una secuencia fija de símbolos del alfabeto código" (las otras invierten fuente y código). Palabra código = "una secuencia **fija** de símbolos **códigos**": "una secuencia fija de símbolos" no dice de qué alfabeto, y "una secuencia de símbolos códigos" omite *fija*.

(teoria/2 - Codificación.md)

### 3.2 Código no singular, unívoco e instantáneo (definiciones y ejemplos)
**Salió:** no singular en 18/12/2020; unívoco en 28/08/2020, 10/09/2021, 19/11/2021, 17/12/2021 y **04/04/2025** (desarrollo); instantáneo en 18/12/2020 y **04/04/2025**; condición necesaria y suficiente de instantáneo en 28/08/2020, 18/12/2020 y 10/09/2021; FAQ ("Definir código no singular, unívoco e instantáneo. Dar ejemplos", "Concepto de código unívoco, instantáneo y compacto. Condiciones necesarias"); cursada 2025: M1, con no singular, unívoco por la extensión de orden $n$, código coma, instantáneo y su condición (parcial Medín 2025, resumen del alumno).

**Respuesta.** Son clases anidadas: instantáneos ⊂ unívocos ⊂ no singulares ⊂ bloque.

- **No singular:** **todas sus palabras código son distintas**.
- **Unívoco (unívocamente decodificable):** **a cualquier secuencia de palabras código le corresponde una y solo una secuencia de símbolos de la fuente**. Equivalente: un código bloque es unívoco si y solo si **su extensión de orden $n$ es no singular para todo $n$ finito**. Todo código no singular de longitud constante es unívoco.
- **Instantáneo:** cada palabra se puede decodificar **sin esperar la llegada de la próxima palabra código**, sin conocer los símbolos que siguen. **Condición necesaria y suficiente:** **ninguna palabra del código es prefijo de otra**. El prefijo de $z_{i1}z_{i2}\dots z_{im}$ es cualquier $z_{i1}\dots z_{ij}$ con $j\le m$.

Ejemplos del apunte, uno por clase:

```
            No singular,      Unívoco,             Instantáneo
            NO unívoco        NO instantáneo       (código "coma")
 s1           1                 0                    1
 s2          11                01                   01
 s3          00               011                  001
 s4          10              0111                 0001
```
- 1.ª columna: si llega `1100`, puede ser $s_2s_3$ o $s_1s_1s_3$. Las palabras son distintas, pero una secuencia es ambigua.
- 2.ª columna: es unívoco (cada palabra empieza con 0, que marca el comienzo), pero al recibir `01` hay que esperar el siguiente símbolo para saber si es $s_2$ o el inicio de $s_3$: `0` es prefijo de `01`.
- 3.ª columna: ninguna palabra es prefijo de otra → se decodifica al terminar cada palabra.
- **Código coma:** el comienzo o el fin de cada palabra lo señala un dígito fijo (un 0 o un 1). La 3.ª columna es un código coma: el `1` cierra cada palabra.

**En el MC:** unívoco = "si a cualquier **secuencia de palabras** código le corresponde una y solo una **secuencia de símbolos** de la fuente". "Si a cualquier palabra código le corresponde un único símbolo" describe un código no singular, no uno unívoco. Instantáneo = "puede decodificarse sin esperar la llegada de la próxima palabra código" y su condición = "ninguna palabra código sea **prefijo** de otra" (no "terminación"/"subfijo", y la longitud variable no tiene nada que ver).

(teoria/2 - Codificación.md; resumenes/El Santo Resumen/el-santo-resumen.md, sección Final)

### 3.3 Inecuación de Kraft (y McMillan)
**Salió:** 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC "Un código que cumple la inecuación de Kraft es…") y **04/04/2025** ("Explicar la inecuación de Kraft"); cursada 2025: M1, con la nota "el teorema no dice que cualquier código que cumpla la condición sea instantáneo" (parcial Medín 2025, resumen del alumno).

**Respuesta.** **Teorema de Kraft:** si los enteros $l_1,\dots,l_q$ satisfacen
$$\sum_{i=1}^{q} r^{-l_i}\le 1$$
esa es condición **necesaria y suficiente para que exista al menos un** código instantáneo de $r$ símbolos en su alfabeto con palabras de esas longitudes.

**Matiz que se toma:** el teorema **no** dice que todo código cuyas longitudes cumplan Kraft sea instantáneo. Dice que **existe** uno con esas longitudes. Si un código no cumple Kraft, seguro **no** es instantáneo.

Ejemplo del apunte ($r=2$, longitudes 1, 2, 2): $2^{-1}+2^{-2}+2^{-2}=1\le 1$ ✓.
- `0, 00, 11` cumple Kraft y **no** es instantáneo (`0` es prefijo de `00`).
- `0, 10, 11` tiene las mismas longitudes y **sí** es instantáneo.

**McMillan:** la misma desigualdad es condición necesaria y suficiente para que exista un código **unívoco** con esas longitudes. Como los instantáneos son subclase de los unívocos, la suficiencia sale de Kraft, y McMillan demostró la necesidad. Consecuencia: pasar de instantáneo a unívoco no permite acortar las palabras.

**En el MC:** "**puede ser** instantáneo". No "es instantáneo", "es unívoco" ni "es compacto".

(teoria/2 - Codificación.md)

### 3.4 Código compacto, longitud media y Huffman
**Salió:** compacto en 28/08/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC) y **04/04/2025**; FAQ ("Concepto de código compacto y ventajas de su aplicación", "¿Para qué sirve el método de Huffman? ¿Qué puede suceder si el alfabeto código tiene r=2?"); cursada 2025: M1 trae solo la longitud media ("desde el punto de vista económico interesan los códigos de longitud mínima"), no el compacto (parcial Medín 2025, resumen del alumno).

**Respuesta.**
- **Longitud media:** $L=\sum_{i} P_i\, l_i$ [dígitos/símbolo].
- **Código compacto** (definición del apunte): dada la fuente $S$, un código **instantáneo** aplicado a $S$ es compacto si su longitud media es **igual o menor que la de todos los códigos instantáneos que puedan aplicarse a la misma fuente y al mismo alfabeto**.
- **Cómo se logra:** "a mayor probabilidad, menor longitud de palabra". Si la fuente es equiprobable, las longitudes no dependen de las probabilidades.
- **Ventaja:** es el código de **menor longitud media posible**. Se transmiten menos dígitos por símbolo, lo que reduce tiempo, ancho de banda y costo de transmisión.
- **Método de Huffman** (construye un código compacto):
  1. Ordenar los símbolos por probabilidad decreciente.
  2. **Reducir** la fuente juntando los $r$ símbolos menos probables en uno, cuya probabilidad es la suma. Reordenar y repetir hasta que queden $r$ símbolos.
  3. Asignar a la última fuente reducida los $r$ dígitos y **volver hacia atrás**, desdoblando cada símbolo compuesto: a su palabra se le agrega un dígito distinto por cada componente.
- **Binario ($r=2$):** se agrupa de a 2, cada fuente reducida tiene **un símbolo menos** que la anterior y **siempre** se llega a 2 símbolos, sin ninguna condición.
- **r-ario:** se agrupa de a $r$ y cada reducción quita $r-1$ símbolos. Se llega exactamente a $r$ símbolos solo si $q=r+\alpha(r-1)$ con $\alpha$ entero. Si no, se agregan **símbolos falsos de probabilidad nula** hasta cumplirlo, y después se descartan.

**Ejemplo binario:** $P=(0{,}5;\ 0{,}25;\ 0{,}125;\ 0{,}125)$ → Huffman da `0, 10, 110, 111`, $L=0{,}5\cdot1+0{,}25\cdot2+0{,}125\cdot3\cdot2=1{,}75$ = $H(S)$: compacto y con rendimiento 100 %.
**Ejemplo ternario** (FAQ, $q=7=3+2\cdot2$ ✓): `1, 2, 01, 02, 000, 001, 002`.

**En el MC:** "Aquel código instantáneo que tiene la menor longitud promedio de todos los códigos **instantáneos** que se pueden aplicar a esa fuente **con ese código**" (= con ese alfabeto código). La opción que termina en "…a esa fuente." omite el alfabeto. La que agrega "y de valor igual a la entropía r-aria" es falsa: $L=H_r$ solo en casos particulares (3.5).

(teoria/2 - Codificación.md)

### 3.5 Cota inferior de la longitud media
**Salió:** 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC) y **04/04/2025** ("Dar la cota inferior de la long. media"); FAQ; cursada 2025: M1, con el enunciado textual del MC (parcial Medín 2025, resumen del alumno).

**Respuesta.** Para un código instantáneo (y, por McMillan, para uno unívoco) aplicado a una fuente de memoria nula, la longitud media no puede bajar de la **entropía r-aria** de la fuente:
$$L \;\ge\; H_r(S)=\frac{H(S)}{\lg r}=\sum_i P_i\log_r\frac{1}{P_i}$$
Expresa el **límite inferior** de la longitud media: ningún código puede representar la fuente con menos dígitos r-arios por símbolo que su entropía r-aria. Para $r=2$, $L\ge H(S)$.

- **Igualdad** ($L=H_r$) si y solo si se pueden elegir $l_i=\log_r(1/P_i)$ enteros, o sea, si las probabilidades son de la forma $P_i=(1/r)^{l_i}$.
- Si no, codificando la **extensión de orden $n$** se puede acercar $L_n/n$ a $H_r(S)$ tanto como se quiera, a costa de complejidad (primer teorema de Shannon): $H_r(S)\le L_n/n< H_r(S)+1/n$.
- Rendimiento $\eta = H_r(S)/L\le 1$; redundancia $=1-\eta$.

**Ejemplo:** la fuente de 3.4 tiene $H=1{,}75$ bit y el código Huffman da $L=1{,}75$ → alcanza la cota porque las probabilidades son potencias de 1/2.

**En el MC:** "Expresa el límite **inferior** de la longitud media, que es igual o mayor a la entropía **r-aria** de la fuente". Con "la entropía de la fuente" (binaria) solo vale para $r=2$; "límite superior" es falso.

(teoria/2 - Codificación.md)

---

## 4. Detección y corrección de errores (códigos lineales)

### 4.1 Distancia de un código e inconveniente de la distancia mínima 1
**Salió:** distancia en 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021; $d_{min}=1$ en las mismas cinco fechas (MC).

**Respuesta.**
- **Distancia** (de Hamming) entre dos palabras: **cantidad de dígitos que difieren entre una palabra código y otra palabra del mismo código**. Ejemplo: $d(100,101)=1$, $d(000,011)=2$, $d(011,100)=3$.
- **Distancia mínima** $d_{min}$: la menor distancia entre dos palabras distintas del código.
- **Inconveniente de $d_{min}=1$:** ante un **error simple** (cambia un bit), una palabra código **se convierte en otra palabra del mismo código**, así que el receptor no puede detectar el error. Es lo que pasa con el código "completo" de $n$ dígitos y $2^n$ palabras: es compacto (rendimiento 100 % si son equiprobables), pero no detecta nada. Por ejemplo, si se envía `100` y se recibe `101`, la palabra recibida también es válida.
- **Solución:** aumentar $d_{min}$ agregando redundancia (bit de paridad → $d_{min}=2$, que detecta error simple; Hamming → $d_{min}=3$, que corrige error simple). La redundancia baja el rendimiento: confiabilidad y economía tiran para lados opuestos.
- Regla general: detectar $e$ errores exige $d_{min}\ge e+1$; corregir $t$ errores exige $d_{min}\ge 2t+1$ (conocimiento general).

**En el MC:** distancia = "cantidad de dígitos que difieren entre una palabra código y otra palabra del mismo código" (no "consecutivas" ni "de dos códigos"). $d_{min}=1$ = "ante un error simple (el cambio de un bit) una palabra código se convierte en otra palabra **del mismo** código".

(teoria/3 - Detección y Corrección de errores.md)

### 4.2 Matriz generadora y matriz de control de paridad
**Salió:** 28/08/2020, 10/09/2021 (MC "Para que una matriz sea generadora de un espacio vectorial debe…"); FAQ ("Cuál es la condición para obtener una base generadora de un código de grupo").

**Respuesta.** El conjunto de las $2^n$ palabras binarias de $n$ dígitos es un espacio vectorial (EV). Para tener $d_{min}>1$ se toma un **subespacio** $V$ de $2^m$ palabras ($m<n$): el **código de grupo** (código lineal binario).
- **Matriz generadora $G$** ($m\times n$): base de $V$. **Condición:** sus $m$ vectores deben ser **linealmente independientes** (ninguno es combinación lineal de los demás) y **generar el subespacio $V$**: toda palabra es $v=k_1g_1+\dots+k_mg_m$, con $k_j\in\{0,1\}$ y suma sin acarreo. **La base no es única.**
- **Matriz de control de paridad $H$** ($(n-m)\times n$): base del **espacio ortogonal** $V'$, con $n-m$ vectores linealmente independientes. Cumple $v\cdot H^T=0$ para toda $v\in V$ (y $v'\cdot G^T=0$).

**En el MC:** "Sus vectores deben ser linealmente independientes y generar el EV" (el subespacio del código). La opción "…y generar **todos** los EV (ortogonales)" es falsa: una base genera un único espacio.

(teoria/3 - Detección y Corrección de errores.md)

### 4.3 Síndrome: concepto, aplicación y condición para corregir errores simples
**Salió:** concepto en 18/12/2020, 19/11/2021, 17/12/2021 (MC); FAQ ("Concepto de síndrome y aplicaciones. Ejemplo. Condiciones necesarias para corregir errores simples en cada uno de los dígitos de la palabra código", "¿Por qué el síndrome de una palabra con error coincide con el síndrome de la palabra que modela el error?"); cursada 2025: M1, con la definición textual del MC y "síndrome 0 → la palabra pertenece al grupo"; Hamming en la parte Baró (parcial Medín y Baró 2025, resumen del alumno).

**Respuesta.**
- **Síndrome:** resultado de multiplicar la **palabra recibida (posiblemente con error) por la matriz de control de paridad transpuesta**: $S = v^{*}\cdot H^T$. Dimensiones: $(1\times n)(n\times(n-m)) = 1\times(n-m)$.
- **Aplicación:** si $S=0$, la palabra pertenece al código de grupo (es correcta, o tiene un error no detectable). Si $S\ne 0$ hubo error, y el síndrome **identifica qué error fue** → se corrige sumándolo. Si hay ambigüedad, se usa máxima verosimilitud: la palabra del código a menor distancia de Hamming.
- **¿Por qué $S(v^{*})=S(e)$?** Modelando el error como una palabra $e$ con unos en las posiciones alteradas, $v^{*}=v\oplus e$:
$$S(v^{*})=(v\oplus e)\,H^T = \underbrace{v\,H^T}_{=0\ (v\in V)} \oplus\; e\,H^T = S(e)$$
El síndrome depende solo del error, no de la palabra transmitida. Por eso el mismo error en dos palabras distintas da el mismo síndrome.
- **Condición para corregir error simple en cada uno de los $n$ dígitos:** cada error simple $e_i$ debe dar un síndrome **distinto y no nulo**. Hacen falta al menos $n$ síndromes no nulos: $2^{n-m}-1\ge n$. Como $e_i H^T$ es la columna $i$ de $H$, eso equivale a que **las columnas de $H$ sean todas distintas y no nulas** (esto último es derivación propia). Si dos errores simples $e_a$ y $e_b$ dan el mismo síndrome, se **detecta** el error pero **no se corrige**.
- **Cuántos bits de control hacen falta (Hamming, Baró en M1):** con $m$ bits de información y $k$ de control, corregir un error simple en cualquiera de los $m+k$ dígitos exige $2^k\ge m+k+1$: los $m+k$ errores simples más el caso "sin error". Para $m=4$: con $k=2$, $4<7$ ✗; con $k=3$, $8\ge8$ ✓ → Hamming (7,4). Es la misma condición $2^{n-m}-1\ge n$ de arriba, con $n=m+k$.

**Ejemplo** (apunte): $v_1=101110$ y $v_2=111001$ con el error $e=000100$ → $v_1\oplus e=101010$ y $v_2\oplus e=111101$. Las dos dan el mismo $S=e\,H^T\neq0$ → error en el 4.º dígito; se corrige y se recupera $v_1$ y $v_2$.

**En el MC:** "El resultado de multiplicar una palabra **con error** por la matriz de **control de paridad transpuesta**". No es una palabra correcta (daría 0) ni la matriz generadora.

(teoria/3 - Detección y Corrección de errores.md)

### 4.4 Familia de errores de cada síndrome; errores no detectables
**Salió:** familia en 28/08/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC); FAQ ("En qué condiciones no se detecta y corrige un error"); cursada 2025: M1, que copia la opción **incorrecta** "solo simples y dobles" (parcial Medín 2025, resumen del alumno; ver Dudas F).

**Respuesta.**
- **Errores no detectables:** los que **coinciden con palabras del código de grupo** (distintas de la nula). Como $e\in V$, $v\oplus e\in V$ y el síndrome sigue siendo 0: el receptor lo toma como palabra correcta. En el ejemplo del apunte (código de 8 palabras de 6 dígitos), no se detectan los errores triples y cuádruples cuyo patrón es una palabra del código (`101010`, `011011`, …).
- **Familia de un síndrome:** todos los patrones de error que producen ese mismo síndrome. Según el apunte, **todos los demás errores caen en alguna de las familias asociadas a cada síndrome**. En cada familia hay errores simples, dobles, múltiples, etc., y son $2^m$ patrones por síndrome: el error "representante" sumado a cada palabra del código (conocimiento general, *coclase*). Por eso el decodificador asume el de **menor peso** (el más probable).

**En el MC:** "**Todos** los errores de las palabras código asociadas a ese síndrome". No "solo simples" ni "solo simples y dobles".

(teoria/3 - Detección y Corrección de errores.md)

---

## 5. Comunicaciones digitales: modulación

### 5.1 Mensaje digital por una red analógica: tipos, aplicación, cómo aumentar la velocidad, gráficas
**Salió:** **04/04/2025** (desarrollo: "a) Qué tipos de modulación se aplican para transmitir mensajes digitales por una red que transporta señales analógicas; b) cómo se aumenta la velocidad; c) cuál es su principal aplicación práctica; d) hacer todas las gráficas"); 28/08/2020 y 10/09/2021 (MC "Si se tiene que transmitir una señal digital por una red que opera con señales analógicas se debe…"); 18/12/2020 (MC "Para aumentar la velocidad de una FSK o PSK sin aumentar el ancho de banda del canal se debe…"); FAQ, con seis variantes de la misma pregunta ("Modulación FSK, PSK y multinivel. Gráficas y aplicación", "Explicar modulación con señal digital y portadora analógica…", "Aplicación de modulación analógica con mensaje digital…", "¿Cómo se puede transmitir una señal digital por un canal analógico?…", "Explique ASK conceptualmente y realice los gráficos", "Demodulación ASK coherente"); cursada 2025: B3, con ASK/FSK/PSK y la aplicación (PC por línea telefónica con MODEM) (parcial Baró 2025, resumen del alumno).

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

### 5.2 Modulación de amplitud (AM): definición, ubicación del mensaje, portadora suprimida, banda lateral única
**Salió:** definición en 28/08/2020, 18/12/2020, 10/09/2021; "dónde queda la banda del mensaje" en 18/12/2020, 19/11/2021, 17/12/2021; portadora suprimida en 19/11/2021 y 17/12/2021 (MC); cursada 2025: B3, "la amplitud de la portadora varía de acuerdo al mensaje", con $f_c\approx1000$ kHz (parcial Baró 2025, resumen del alumno).

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

### 5.3 Ancho de banda práctico de una señal digital real
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

### 5.4 Banda ancha y espectro del mensaje
**Salió:** FAQ ("Concepto de banda ancha y concepto de espectro de mensaje (o señal). Dar en un solo ejemplo cómo se aplican").

**Respuesta.**
- **Espectro del mensaje:** representación del mensaje en función de la frecuencia (por Fourier, la suma de sus componentes senoidales con sus amplitudes). Ocupa una **banda** $w=f_{max}-f_{min}\approx f_{max}$ si $f_{min}$ es despreciable. Por ejemplo, la voz telefónica va de 300 Hz a 3,4 kHz.
- **Banda base vs. banda ancha:** en **banda base** el mensaje se transmite con su espectro original, **sin corrimiento en frecuencia**, y es una sola transmisión por el canal. En **banda ancha** el canal lleva **varias señales en canales (bandas) distintos**: cada mensaje se traslada con su portadora a una porción del ancho de banda del canal (modulación + FDM).
- **Ejemplo único (ADSL sobre el par telefónico):** el mismo par lleva la voz **en banda base** (0–4 kHz) y los datos en bandas trasladadas: subida de 25,875 a 138 kHz y bajada de 138 a 1104 kHz. El canal (par de cobre) tiene un ancho de banda mayor que el espectro de cada mensaje y se reparte en bandas, cada una ocupada por el espectro de una señal.

(resumenes/El Santo Resumen/el-santo-resumen.md, "Banda base y modulación" y ADSL, que citan el apunte «Principios Básicos» y teoria/6 - Espectro de la señal ADSL; teoria/5 - Comunicaciones Digitales.md)

### 5.5 Modulación: concepto y para qué se modula; señal portadora; ancho de banda
**Salió:** cursada 2025: B3 ("Ejercicio 1 – Definiciones": ancho de banda, señal portadora y su utilidad; concepto de modulación) y M1, parte Baró (para qué se modula) (parcial Baró 2025, resumen del alumno). En los finales aparece implícita en AM (§5.2).

**Respuesta.**
- **Modular** es variarle a una portadora **un** parámetro (amplitud, frecuencia o fase) de acuerdo con el mensaje. Tiene dos caras: **adaptar** el mensaje al medio y **trasladarlo en frecuencia**, de $f_m$ a $f_c\gg f_m$. Siempre el mensaje modula a la portadora.
- **Para qué:** adaptar la señal al canal (una señal digital en banda base no llega lejos por un par de cobre: es muy sensible al ruido); alcanzar mayores distancias; alejarse del ruido de baja frecuencia; compartir el canal entre varias señales con portadoras distintas (FDM). También permite antenas de tamaño razonable, porque se dimensionan con $\lambda$ (conocimiento general).
- **Señal portadora:** señal de alta frecuencia que **transporta** el mensaje de origen a destino. La información viaja en las variaciones que el mensaje le imprime. Puede ser analógica (senoidal) o digital (tren de pulsos).
- **Casos que estudia la cátedra** (por tipo de mensaje y de portadora):

```
 Mensaje      Portadora               Técnicas
 analógico    analógica (senoidal)    AM, FM, PM
 digital      analógica (senoidal)    ASK, FSK, PSK  → MODEM (§5.1)
 analógico    digital (pulsos)        PAM, PDM, PPM → PCM (§6.2)
```
Baró llama **modulación analógica** a la de portadora senoidal y **modulación digital** a la de portadora de pulsos, sin importar el mensaje.
- **Ancho de banda:** diferencia entre la frecuencia máxima y la mínima que deja pasar un canal (o que ocupa una señal): $AB=f_{max}-f_{min}$ [Hz]. En un sistema real, $f_{min}$ y $f_{max}$ son las frecuencias de corte a −3 dB (§dB.2). A más ancho de banda, más velocidad de transmisión posible.

**Ejemplo:** radio AM: voz y música de 20 Hz a 20 kHz sobre una portadora de ≈ 1000 kHz; radio FM: el mismo mensaje sobre ≈ 100 MHz.

(teoria/5 - Comunicaciones Digitales.md; practica/1 - Principios Básicos de la Electrónica y las Comunicaciones.md; cursada-2025/drive-propio/Resumen de Comunicación de datos - 3er parcial Práctica.md)

### 5.6 FM y PM
**Salió:** cursada 2025: B3 (parcial Baró 2025, resumen del alumno). No salió en los finales relevados.

**Respuesta.**
- **FM (modulación de frecuencia):** amplitud y fase de la portadora constantes; **la frecuencia de la portadora varía según la amplitud del mensaje**. Ejemplo: radio FM, portadora de ≈ 100 MHz.
- **PM (modulación de fase):** amplitud y frecuencia constantes; varía la **fase**. Fase y frecuencia están las dos dentro del argumento del coseno, así que con modulación continua la gráfica de PM no se distingue de la de FM. Por eso se dibuja con saltos discretos de fase (por ejemplo, 180°), que es el caso PSK (§5.1).
- Comparación (conocimiento general): FM es más inmune al ruido que AM, porque el ruido afecta sobre todo la amplitud, a cambio de ocupar más ancho de banda.

(teoria/5 - Comunicaciones Digitales.md; cursada-2025/drive-propio/Resumen de Comunicación de datos - 3er parcial Práctica.md)

### 5.7 Armónico de la serie de Fourier
**Salió:** cursada 2025: B3 ("Otro parcial de Baró": "Defina claramente… armónico de la serie de Fourier") (resumen del alumno).

**Respuesta.** Una señal periódica de período $T_0$ se puede descomponer (serie de Fourier) en una suma de senoides cuyas frecuencias son **múltiplos enteros** de la frecuencia **fundamental** $f_0=1/T_0$. Cada una de esas componentes, de frecuencia $n\,f_0$, es un **armónico**; el de $n=1$ es la fundamental. Las amplitudes de los armónicos forman el espectro de líneas de la señal.

**Ejemplo:** un tren de pulsos de período $T$ y ancho $\tau$ tiene armónicos en $1/T,\ 2/T,\ 3/T,\dots$, con una envolvente sinc que se anula en $1/\tau$. De ahí sale el ancho de banda práctico (§5.3).

(teoria/5 - Comunicaciones Digitales.md; cursada-2025/drive-propio/Resumen de Comunicación de datos - 3er parcial Práctica.md)

---

## 6. Muestreo, digitalización y PCM

### 6.1 ¿Qué hay que hacer primero para digitalizar un mensaje analógico? (Nyquist)
**Salió:** 28/08/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC); TDM "las señales se muestrean con…" en 28/08/2020 y 18/12/2020 (MC); FAQ ("Cómo digitalizar una señal analógica"); cursada 2025: B3, con las definiciones de muestreo ("Ejercicio 1") y de tasa de Nyquist ("Otro parcial de Baró") (resumen del alumno).

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

### 6.2 PCM (modulación por pulsos codificados)
**Salió:** 18/12/2020 (MC "En una transmisión PCM las muestras de cada señal…"); FAQ (PCM en Parte 2); cursada 2025: B3, con las definiciones de cuantificación y codificación ("Ejercicio 1") y de PDM ("Otro parcial de Baró"), más los cálculos de trama (resumen del alumno).

**Respuesta.** Primero, las técnicas de portadora digital con mensaje analógico: el mensaje modula un parámetro de cada pulso.
- **PAM:** varía la amplitud.
- **PDM (o PWM):** varía la duración (el ancho) del pulso según la amplitud del mensaje.
- **PPM:** varía la posición.

**PCM** es la cuarta técnica y la que se usa hoy: la amplitud de cada muestra PAM se **cuantifica y codifica**.
1. **Muestreo** a $f_s\ge2f_{max}$.
2. **Cuantificación:** las muestras pueden tomar infinitos valores, pero solo se puede codificar un número finito. Se preestablecen **niveles cuánticos** y cada muestra se redondea al nivel más cercano. El intervalo asociado a cada nivel es el **cuanto**. Ejemplo del apunte: rango $[-4{,}5;\,4{,}5]$ con niveles $-4{,}5;\,-3;\,-1{,}5;\,0;\,1{,}5;\,3;\,4{,}5$.
3. **Codificación:** cada nivel se representa con una palabra de $n$ dígitos binarios (con 7–8 niveles, $n=3$).
4. **Multiplexado TDM** de muestras de varios canales en una **trama**: la PCM 30+2 lleva 30 canales de información y 2 de sincronismo y señalización.

Cuentas: $T_s=1/f_s=N\cdot T_M$, $T_M=n\cdot\tau$, $B_w=1/\tau=N\cdot n\cdot f_s$.

Ejemplos resueltos en B3, con voz de $f_{max}=4$ kHz → $f_s=8$ kHz y $T_s=125$ µs:
- **PCM 30+2:** 32 canales × 8 bits = 256 bits en 125 µs → $r=2{,}048$ Mbps.
- **T1:** 24 canales × (7 bits + 1 de sincronismo) + 1 bit de señalización por trama = 193 bits en 125 µs → $r=1{,}544$ Mbps.

```
 Muestreadores → MUX (PAM/TDM) → Cuantificador → MUX sinc./señalización → Codificador de línea → señal PCM
```

**En el MC:** "Se codifican y se transmiten a una velocidad del doble de la frecuencia máxima del mensaje". Las muestras de cada señal salen a $f_s=2f_{max}$ muestras/s y se codifican **en el emisor**, no en el receptor.

(teoria/5 - Comunicaciones Digitales.md)

---

## 7. Multiplexación

### 7.1 FDM: concepto
**Salió:** 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC); FAQ.

**Respuesta.** **Multiplexación por división de frecuencia:** cada señal **modula una portadora distinta y única** ($f_{c1}, f_{c2},\dots$), así que todas **viajan simultáneamente** por el mismo canal y cada una ocupa **una banda de frecuencia determinada dentro del ancho de banda del canal**. Los mensajes no se mezclan porque cada uno queda a ambos lados de su propia portadora, con separación suficiente (bandas de guarda). En recepción, filtros pasabanda separan cada canal y se demodula.

**En el MC:** "Las señales viajan simultáneamente y ocupan una determinada banda de frecuencia dentro del ancho de banda del canal". "Time slice" y "muestrean a 2·fmax ocupando todo el BW" describen TDM.

(teoria/5 - Comunicaciones Digitales.md)

### 7.2 FDM con AM: ancho de banda para N señales y cómo duplicar la cantidad de señales
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

### 7.3 TDM: concepto, trama y diferencia con FDM
**Salió:** 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC "En una transmisión con multiplexado TDM las señales…"); FAQ ("Explique detalladamente la técnica TDM", "Explicar la diferencia entre FDM y TDM. Ejemplo con gráfico", "¿En una transmisión, cada mensaje ocupa un lugar determinado del ancho de banda del canal? ¿Por qué?"); cursada 2025: B3, con TDM y trama (parcial Baró 2025, resumen del alumno).

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

---

## 8. Medios de transmisión y elección del medio de acceso

### 8.1 Propiedades de los medios (MC verdadero/falso y opciones)
**Salió:** fibra y ruido eléctrico en 28/08/2020, 18/12/2020, 10/09/2021; "la fibra transmite por…" en 18/12/2020; atenuación de ondas de radio en 28/08/2020, 18/12/2020, 10/09/2021; ventaja del satélite en 28/08/2020 y 10/09/2021; cablemodem en 10/09/2021; cursada 2025: B2 repite "fibra y ruido eléctrico" (VF) y suma dos VF de coaxil. El resto del compendio de Baró está en [Multiple choice de medios de transmisión](#multiple-choice-de-medios-de-transmisión-2do-parcial-baró).

**Respuestas.**
- **"El ruido eléctrico, interferencias y acoplamientos eléctricos afectan a la fibra óptica" → FALSO.** La fibra transporta **luz**, así que las sobrecargas de energía, la interferencia electromagnética y los cortes de suministro no la afectan.
- **"La transmisión por fibra óptica se realiza por…" → pulsos de luz.** Un pulso de luz es un 1 y su ausencia es un 0. El sistema tiene fuente de luz, medio (fibra) y detector.
- **"La atenuación de las ondas de radio depende de la frecuencia y de la distancia recorrida" → VERDADERO.** Las propiedades de las ondas de radio dependen de la frecuencia: a baja frecuencia atraviesan obstáculos pero la potencia cae drásticamente con la distancia; a alta frecuencia viajan en línea recta, rebotan y la lluvia las absorbe (microondas desde unos 4 GHz).
- **"Una de las ventajas de las microondas satelitales es…" → poder llegar con la señal a lugares muy lejanos e inaccesibles.** El satélite es un repetidor en el cielo con gran cobertura. Las demás opciones son falsas: el ancho de banda satelital es caro y menor que el de la fibra, el aire no da "más velocidad" y la instalación del enlace no es barata.
- **"Una empresa de zona urbana que requiere gran ancho de banda contrata cablemodem por coaxil a la empresa de TV cable" → FALSO.** Según la cátedra, el coaxil queda **solo para cablemodem de usuarios residenciales** por la red de TV cable. Para una empresa urbana con gran BW se usa fibra óptica.
  - **Por qué es residencial:** la red de TV cable es **HFC** (híbrida fibra-coaxil). Desde la cabecera, una troncal de fibra en anillos redundantes llega a nodos ópticos; ahí la señal pasa a eléctrica y se distribuye en un **bus de coaxil de 75 Ω**, compartido por los abonados de la zona, hasta el cablemodem (estándar DOCSIS). Es una red de difusión pensada para hogares, con el ancho de banda de subida compartido (TP HFC de Baró, 2024).

(practica/3 - Medios de transmisión.md; teoria/Elección medio de acceso V03.md; cursada-2025/drive-propio/Tps Baro/TP N°1 - Cables HFC.md)

### 8.2 Características (ventajas y desventajas) de los medios de acceso: par telefónico, fibra óptica, radioenlace, satélite
**Salió:** **04/04/2025** (3-a, desarrollo); FAQ ("Indicar al menos tres medios de comunicación de acceso…").

**Respuesta.** El **medio de acceso** ("última milla") conecta la organización con la red del **operador de comunicaciones**, que cubre las grandes distancias con troncales propios. Hoy son par telefónico, fibra óptica, radioenlace y satélite. El coaxil queda para cablemodem residencial y el láser no tuvo expansión.

| Medio | Ventajas | Desventajas | Uso típico |
|---|---|---|---|
| **Par telefónico** (+ módem HDSL/xDSL) | Bajo costo de contratación; infraestructura ya tendida en zonas urbanas; fácil instalación | Ancho de banda limitado; atenuación muy dependiente de la frecuencia y la distancia (amplificadores cada 2–6 km); baja inmunidad al ruido y a la diafonía; altas tasas de error a alta velocidad | Organización pequeña en zona urbana con bajo ancho de banda |
| **Fibra óptica** | Ancho de banda muy superior al cobre; baja atenuación (repetidores cada unos 50 km contra unos 5 km en cobre); inmune a sobrecargas, interferencia electromagnética y corrosivos; difícil de intervenir (segura) | Costo del tendido (obra civil) y de las interfaces; requiere mano de obra calificada; se daña si se dobla; unidireccional (dos fibras o dos bandas para full-dúplex); solo llega donde hay red | Alto ancho de banda en zona urbana o suburbana; segurización en anillo |
| **Radioenlace** (microondas) | No requiere tendido; instalación rápida; relativamente barato frente a tender fibra; salva obstáculos naturales (ríos, rutas); buena relación S/N con antenas alineadas | **Requiere visión directa** e instalación en altura: mástil arriostrado, con pie de rienda de alrededor del 60 % de la altura (para 30 m hace falta un espacio de unos 36 × 36 m); la lluvia lo atenúa desde unos 4 GHz; desvanecimiento por múltiples trayectorias; espectro saturado y licencias | Zona suburbana o rural con espacio físico y BW bajo o medio; segurización de la fibra |
| **Satélite** (VSAT) | **Llega a lugares lejanos, aislados o inaccesibles**; el costo no depende de la distancia; antena chica (VSAT ≤ 1 m), instalación rápida y trasladable; no necesita mástil ni gran espacio | Ancho de banda bajo y caro; **retardo alto** (GEO, unos 270 ms); bandas Ku/Ka sensibles a la lluvia; dependencia de un único proveedor y vida útil del satélite (unos 10 años) | Zona montañosa o selvática; ubicación transitoria; segurización |

(teoria/Elección medio de acceso V03.md; practica/3 - Medios de transmisión.md)

### 8.3 Elegir un medio de acceso según la zona y la velocidad
**Salió:** **04/04/2025** (3-b, cuatro casos) y MC de 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021; FAQ (dos variantes con tres casos cada una); cursada 2025: M2, con las mismas variables de decisión ("ver ejemplos del apunte") (parcial Medín 2025, resumen del alumno).

**Criterio de la cátedra.** Se evalúan estas variables:
- ubicación (urbana, suburbana, rural, montañosa, bosque/selva);
- permanencia (definitiva o temporal);
- espacio físico para infraestructura (sí/no);
- ancho de banda: bajo de 4 a 8 M, medio de 10 a 50 M, alto de más de 100 M;
- madurez (pequeña, en crecimiento, madura);
- segurización (sí/no);
- recursos económicos.

Como las consignas no dan todas las variables, **conviene escribir el supuesto** (espacio, segurización, permanencia).

| Caso (fechas) | Medio | Justificación (ejemplo del apunte) |
|---|---|---|
| **Zona montañosa, baja velocidad** (28/08/20, 10/09/21, 04/04/25-b1) | **Satélite** | Ej. 8: pequeña en zona montañosa o selva, BW bajo → satelital. El relieve impide la visión directa del radioenlace y no hay red de cobre ni de fibra. |
| **Zona selvática, baja velocidad** (19/11/21, 17/12/21) | **Satélite** | Ej. 8 (montaña/selva). La vegetación obstruye el radioenlace. |
| **Zona urbana, alta velocidad** (28/08/20, 10/09/21, 19/11/21, 17/12/21, 04/04/25-b2) | **Fibra óptica** (en anillo si requiere segurización) | Ej. 2: madura, urbana definitiva, gran BW, segurización → FO en anillo. En la ciudad hay red de fibra del operador. |
| **Zona urbana, baja velocidad** (18/12/20; FAQ) | **Par telefónico + módem HDSL** | Ej. 1: pequeña, urbana, BW bajo, sin segurización y pocos recursos → par + HDSL (infraestructura existente y barata). |
| **Zona suburbana, alta velocidad** (04/04/25-b3; FAQ) | **Fibra óptica** (anillo) | Ej. 6: suburbana definitiva, gran BW, segurización → FO en anillo. Solo la fibra da más de 100 M. |
| **Zona suburbana, baja velocidad** (28/08/20, 10/09/21, 04/04/25-b4) | **Radioenlace** (supuesto: hay espacio físico para el mástil) | Ej. 4: suburbana definitiva, BW bajo, con espacio, sin segurización → RE. Si además pide segurización: RE + satélite (ej. 5). Sin espacio físico: satélite (o par + HDSL si llega la red). |
| **Zona suburbana, baja velocidad, edificio transitorio** (18/12/20; FAQ) | **Satélite** | Ej. 3: transitoria, sin espacio, BW bajo → satelital. No tiene sentido levantar un mástil ni tender fibra si se va a mudar; la VSAT se traslada. |
| **Zona suburbana, velocidad media, con espacio físico** (19/11/21, 17/12/21) | **Radioenlace** | El dato "disponiendo de espacio físico" apunta al mástil del RE, y el RE cubre BW medio. FO si hay presupuesto o segurización (ej. 7 usa FO + RE para BW medio). El cablemodem es residencial. |
| **Industria en la ruta 9 entre Cañada de Gómez y Rosario, gran velocidad** (18/12/20, 19/11/21, 17/12/21) | **Fibra óptica** | Gran BW (>100 M) solo lo da la fibra. Sobre el corredor Rosario–Córdoba el operador tiene troncales de fibra; zona suburbana o rural (ej. 6/7: FO, con segurización por RE). El satélite no da gran velocidad. |

**Segurización:** ver §8.4.

(teoria/Elección medio de acceso V03.md; resumenes/El Santo Resumen/el-santo-resumen.md, "Elección del medio de acceso")

### 8.4 Segurización (plan de contingencia) y consideraciones para instalar un radioenlace
**Salió:** cursada 2025: M2 (2.º parcial de Medín, "explicación de conceptos") (resumen del alumno). En los finales aparece dentro de los casos de §8.3 que piden segurización.

**Respuesta.**
- **Segurización (plan de contingencia):** un segundo medio de comunicación entre los mismos puntos para cuando falla el principal. Hace falta cuando el servicio **no admite cortes**. Como se usa ocasionalmente, conviene que sea **más barato** que el principal (p. ej., fibra principal con respaldo por radioenlace o satélite).
- **Consideraciones** (el respaldo tiene que usar **recursos disjuntos**):
  - Acceso y segurización **por fibra**: los dos recorridos no pueden compartir ningún tramo hasta la sala de equipos, porque una sola obra que corte el ducto tira los dos.
  - Acceso y segurización **por radioenlace o fibra**: conviene que los den **operadores distintos**, y que el segundo tenga infraestructura propia. Si los dos servicios son del mismo proveedor (o el operador 2 le alquila la red al 1), una caída del proveedor deja sin servicio principal y sin respaldo.
- **Radioenlace:** necesita **visión directa** entre los extremos, sin obstáculos. Es sencillo si la organización tiene un edificio en altura. Si no, hay que levantar una estructura sostén de antenas, normalmente un **mástil arriostrado**, cuyas riendas se anclan a una distancia del pie de alrededor del 60 % de la altura (para 30 m, un terreno de unos 36 × 36 m). Por eso el dato decisivo es el **espacio físico**: sin espacio, el radioenlace queda descartado (→ satélite, o par + HDSL si llega la red).

(teoria/Elección medio de acceso V03.md; cursada-2025/drive-propio/Resumen de Comunicación de datos - 2do parcial teoría.md)

---

## Multiple choice de medios de transmisión (2do parcial Baró)

**Salió:** compendio "2do parcial de Baró 2024 – compendio de preguntas para estudiar", usado en la cursada 2025 (B2): 44 preguntas, con la opción marcada por un alumno. Acá están fusionadas las repetidas (con distintas opciones) en 34 ítems. Para cada uno va la respuesta correcta y por qué; cuando la marca del alumno es distinta o dudosa, se aclara (resumen en [Dudas E](#e-marcas-del-compendio-mc-de-baró-b2)). Los valores salen del apunte de Medios de transmisión, que sigue a Tanenbaum, salvo donde dice "conocimiento general".

### MC.1 Par trenzado (UTP)
1. **Una diferencia entre UTP Cat. 5 y Cat. 6** (dos versiones). → Si está la opción: "**el Cat. 6 tiene más vueltas por metro que el Cat. 5**". En la versión que no la trae: "**ninguna de las anteriores**". Cat. 5 = 100 MHz y Cat. 6 = 250 MHz, así que "100/600 MHz" es falsa, y "16/100" o "16/200" también (16 MHz es Cat. 3). "Cat. 5 tiene más vueltas" está invertida: cada categoría trenza más apretado para bajar la diafonía. "Cat. 6 usa 2 pares y Cat. 5 usa 4" también está invertida: en Cat. 5e se usan los hilos 1-2 para Tx y 3-6 para Rx, y en Cat. 6 los cuatro pares.
2. **¿Por qué se trenzan los hilos del UTP?** (dos versiones) → "**para disminuir la interferencia entre pares**" (diafonía). Dos hilos paralelos forman una antena; al trenzarlos, los campos de vueltas sucesivas se cancelan. Baró: se trenzan para **disminuir, no anular**, el acoplamiento magnético entre pares. No es para bajar la atenuación ni para llegar a 100 m o a 100 MHz.
3. **Pines de cada puerto de conexión UTP** → **8** (RJ-45: 4 pares × 2 hilos).

### MC.2 Cable coaxil
4. **"Banda ancha con coaxil utiliza el cableado coaxial existente (50 Ω)"** → **Falso.** Banda ancha usa el coaxil de **75 Ω** (grueso: analógico, TV cable, ≈ 500 m, ≈ 500 MHz). El de **50 Ω** es el de banda base (fino: digital, ≈ 200 m).
5. **"El coaxil de banda base se usa actualmente para distribución de video, voz e internet"** → **Falso.** Eso lo hace el coaxil de **banda ancha** (75 Ω) en las redes HFC de TV cable (§8.1). El de banda base (50 Ω, Ethernet viejo) está en desuso.

### MC.3 Fibra óptica
6. **La ley de Snell** (dos versiones) → "especifica los ángulos de incidencia y **refracción** de la luz" / "relaciona los ángulos de incidencia y refracción con los **índices** de refracción": $n_1\sin\theta_1=n_2\sin\theta_2$. No es "reflexión": la reflexión total interna es una consecuencia, a partir del ángulo crítico. Tampoco tiene que ver con zonas de atenuación, anchos de banda ni dispersión cromática.
7. **Longitud de onda de transmisión** → **≈ 1300 nm**. Las ventanas típicas son 850, 1300 y 1550 nm, infrarrojo cercano (conocimiento general).
8. **La fibra monomodo…** ("más económica por un solo haz / por más delgada / por el erbio"; "distancias más grandes por ser más barata") → **ninguna**. La monomodo es **más cara**. Llega más lejos porque no tiene dispersión modal, no por precio. El erbio es de los amplificadores ópticos (EDFA, conocimiento general).
9. **La fibra multimodo…** (dos versiones) → "**es menos frágil y menos costosa que la monomodo**" y "**tiene más atenuación por km que la monomodo**". Su núcleo es grande (50–62,5 µm contra 8–10 µm): es más fácil de conectar y usa componentes más baratos (LED), pero tiene más pérdida y dispersión modal y se usa a menos de 2 km. Falsas: "un solo haz" (eso es monomodo), "más delgada" (es más gruesa), "menos repetidores".
10. **Emisor y receptor de la fibra** → emisor: **diodo emisor de luz (LED) o diodo láser** (opción "c y e"); receptor: **fotodiodo**.
11. **Pérdida por un empalme** → **≈ 10 %**. El apunte da 10–20 % para conectores; un empalme mecánico ronda el 10 % y uno por fusión pierde menos (Tanenbaum, conocimiento general). 3 dB sería perder el 50 %.
12. **Velocidad de propagación en la fibra** → "**es menor que en el aire**": con índice ≈ 1,5, va a ≈ 200.000 km/s. No es mayor que en cualquier medio ni igual a 300.000 km/s.
13. **¿Qué limita la velocidad (bps) en la fibra?** → **el fotodiodo**, es decir, la conversión óptico-eléctrica: su tiempo de respuesta (≈ 1 ns) limita la tasa a ≈ 1 Gbps, mientras que la fibra en sí tiene un ancho de banda enorme (Tanenbaum, conocimiento general). La atenuación limita la **distancia**, no los bps.

### MC.4 Microondas (radioenlace terrestre)
14. **Microondas es un tipo de señal…** (dos versiones) → En una: **ninguna de las anteriores**. "λ elevada y f pequeña" está al revés; "no requiere licencia en todo su espectro" es falso; "espectro audible", también; y "se propagan omnidireccionalmente" es falso, porque van en un haz. En la otra: "**de longitud de onda muy pequeña y frecuencia elevada**".
15. **Banda de frecuencias de microondas** → **1.000 a 38.000 MHz** (≈ 1–38 GHz). 300–3000 MHz es UHF y 300–3000 GHz ya es infrarrojo lejano.
16. **Longitud de onda de una señal de 2,48 GHz** → **121 mm**: $\lambda=c/f=3\cdot10^8/2{,}48\cdot10^9\approx0{,}121$ m. (Con 2,4 GHz da 125 mm.)
17. **Torres y distancia de un enlace punto a punto** (dos versiones) → torres de **100 m** ↔ repetidores a **80 km**. La distancia crece aproximadamente con la raíz cuadrada de la altura.
18. **Principal ventaja de las microondas** → "**el bajo costo de sus componentes e instalación, y la fácil instalación**": dos torres con antenas cuestan menos que enterrar 50 km de fibra. Falsas: "gran BW comparado con la fibra", "alta velocidad por usar el aire" y "llegar a lugares muy lejanos" (esa es la del satélite).
19. **Microondas…** ("haz estrecho para conectar PC", "costosa", "el medio inalámbrico más eficiente", "no se usa por su escasa velocidad") → "**es el medio inalámbrico más eficiente para enlaces terrestres**".
20. **Desvanecimiento por trayectoria múltiple** → "**ondas de un radioenlace terrestre que, tras rebotar (refractarse) en la atmósfera, llegan al receptor y causan interferencia**". Llegan con retardo y fuera de fase respecto de la onda directa, y pueden cancelarla. Depende del clima y de la frecuencia.

### MC.5 Infrarrojo y láser
21. **La transmisión por infrarrojo…** → "**requiere baja inversión**": emisores y receptores baratos y fáciles de construir, sin licencia. Falsas: "no tiene inconvenientes cuando llueve" y "trabaja en baja frecuencia" (está en THz). Ojo con "se utiliza en fibra óptica": la luz de la fibra (850–1550 nm) **es** infrarrojo cercano, pero la pregunta habla del infrarrojo como medio inalámbrico (Dudas E).
22. **¿Por qué el infrarrojo no se puede usar en exteriores?** → "**el sol brilla con igual intensidad en el infrarrojo que en el visible**" y lo interfiere.
23. **Las ondas infrarrojas…** → "**se pueden usar en una LAN con haces relativamente desenfocados para conectar las PC**". "1 mm de ancho a 500 m" describe al láser; no requieren licencia; los equipos son baratos. No atraviesan paredes: es una limitación de alcance, pero también una ventaja de seguridad.
24. **Banda del infrarrojo** → **del orden de los THz** ($\approx10^{12}$–$10^{14}$ Hz). $10^{10}$–$10^{12}$ Hz son microondas y milimétricas.
25. **El láser…** → "**tiene un haz demasiado estrecho y complicado para conectar PC**": apuntar un haz de 1 mm a un blanco a 500 m es difícil. Se usa punto a punto entre edificios. No es caro ni es el inalámbrico más eficiente.
26. **Las ondas por láser…** ("requieren licencia", "casi solo se usan dentro de la fibra", "son inmunes a las corrientes de convección", "son menos focalizadas que las microondas") → **el compendio no tiene marca**. Por descarte: "**prácticamente se utilizan solo para transmitir dentro de la fibra óptica**". No requieren licencia, **no** son inmunes a la convección (el aire caliente del techo desvía el haz) y son **más** focalizadas que las microondas. Además, la cátedra dice que el láser por aire no tuvo expansión (§8.2). Ver Dudas E.

### MC.6 Satélite
27. **Altura de un satélite de órbita baja (LEO)** → **≈ 700 km**. GEO: ≈ 36.000 km sobre el ecuador. MEO: ≈ 10.000 km, entre los cinturones de Van Allen (inferior, 1.000–5.000 km; superior, 15.000–20.000 km).
28. **Latencia de un satélite de órbita media (MEO)** → **35 a 87 ms**. LEO: 1–7 ms; GEO: ≈ 270 ms. "6 horas" es el período orbital de un MEO, no su latencia.
29. **Ancho de banda de cada transpondedor** → el compendio (y el resumen del alumno) marca "**50 a 100 MHz**". Según Tanenbaum (conocimiento general), el valor típico es **36 a 50 MHz**, que también está entre las opciones. **Dudoso**: ver Dudas E.
30. **Vida útil en órbita** → "**entre 10 y 15 años**". El apunte dice que el combustible se termina "por lo general a los 10 años".
31. **Banda L** → **1,5/1,6 GHz**. Las demás: S 1,9/2,2; C 4/6; Ku 11/14; Ka 20/30 GHz (bajada/subida). La C fue la primera comercial y está saturada; Ku y Ka sufren con la lluvia.
32. **¿Qué significa VSAT?** (dos versiones) → "**terminales de apertura muy pequeña**" (*Very Small Aperture Terminal*: antena de 1 m o menos). En la versión en inglés, la correcta es "**ninguna de las anteriores**". **"Very Small Amplitude Terminals" está mal** (amplitud ≠ apertura), aunque es la que marcó el alumno.
33. **Una ventaja de la transmisión por satélite** → "**versatilidad en las comunicaciones móviles**". Falsas: "más BW que la fibra"; "disponibilidad por debajo del 99 %" y "BER muy alto" (no son ventajas); "latencia muy baja" (GEO ≈ 270 ms, por eso no sirve bien para tiempo real). En los finales, la ventaja correcta era otra opción: "llegar a lugares muy lejanos e inaccesibles" (§8.1).

### MC.7 Velocidad de propagación en el aire
34. **La velocidad de propagación de una señal en el aire…** (dos versiones) → En una: "**es tal que su retardo equivale a ≈ 3 µs/km**" ($1/300.000$ km/s $\approx3{,}3$ µs/km). En la otra: "**es mayor que en cualquier medio de transmisión guiado**" (en cobre y fibra va a ≈ 2/3 de $c$). Falsas: "similar a la del par trenzado", "menor que en la fibra", "200.000 km/s". "Igual a 300.000 km/s" es casi cierta en el aire (Dudas E), pero la marcada es la más segura.

### MC.8 Datos sueltos del resumen B2 que pueden caer
- **Medios confinados (guiados):** par trenzado, coaxil, fibra, HFC. **No confinados:** radio, microondas, infrarrojo, láser, satélite.
- **Impedancias:** UTP 100 Ω, FTP 120 Ω, STP 150 Ω; coaxil 50 Ω (banda base) y 75 Ω (banda ancha). El STP se discontinuó por caro: había que blindar también las fichas.
- **UTP:** la atenuación limita el segmento a **100 m** (después, repetidor).
- **Fibra:** la transmisión es unidireccional, así que un enlace full-dúplex usa **2 pelos** (o dos bandas en una fibra).
- **Satélite GEO:** no es una solución óptima para aplicaciones de tiempo real (retardo).

(practica/3 - Medios de transmisión.md; cursada-2025/drive-propio/2do Parcial - Comunicacion De Datos - Baró.md; resumenes/2° Parcial/Resumen Parcial 2 (2025).md, que confirma VSAT)

---

## 9. Teoría de colas

### 9.1 Punto de saturación de un sistema de cola cerrada
**Salió:** 19/11/2021 y 17/12/2021 (MC); FAQ ("Explique brevemente y grafique adecuadamente el punto de saturación de un sistema de cola cerrada"); cursada 2025: M2 (sistema cerrado, mismo desarrollo) y parcial com. 305 ("Explicar el concepto de punto de saturación", respondido con el criterio del enlace; ver el recuadro al final) (resumen del alumno).

**Respuesta.** Modelo **cerrado** de población finita: $N$ terminales interactúan con una CPU y cada usuario alterna entre "pensando" (tiempo medio $E[t]$), esperando y recibiendo servicio (tiempo medio $E[s]$). Se grafica el tiempo de respuesta medio $W$ en función de $N$:
- Con $N=1$ no hay cola: $W=E[s]$.
- Con **pocos terminales**, la interferencia mutua es mínima: cuando uno pide CPU los demás suelen estar pensando, y la cola se forma solo ocasionalmente. Asíntota horizontal $W=E[s]$.
- Con $N\to\infty$, la probabilidad de CPU libre $p_0\to0$ y la curva tiende a la recta $W=N\,E[s]-E[t]$.
- La intersección de las dos asíntotas da el **punto de saturación**:
$$N^{*}=\frac{E[s]+E[t]}{E[s]}$$
Es el **número máximo de terminales que se pueden conectar sin causar interferencia mutua** (con tiempos exactamente iguales a las medias). Por encima de $N^*$, cada terminal agregada aumenta $W$ en aproximadamente $E[s]$ sin mejorar casi el rendimiento.

```
  W │                                  ╱  W = N·E[s] − E[t]
    │                                ╱
    │                              ╱ ·
    │                            ╱ ·       ← curva real de W(N)
    │                          ╱·
    │                       · ╱
    │               ·  ·    ╱
  E[s]┼·──·──·──·─────────╳──────────────  W = E[s]
    │                    ╱│
    │                  ╱  │
    └────────────────╱────┼──────────────── N
                          N* = (E[s] + E[t]) / E[s]
```
**Ejemplo** (apunte): $E[s]=0{,}2$ s y $E[t]=3$ s → $N^*=3{,}2/0{,}2=16$ terminales. Pasar de 20 a 30 terminales sube las interacciones un 4,78 % a costa de un 150 % más de tiempo de respuesta.

**En el MC:** "el punto correspondiente al número **máximo** de usuarios que se pueden conectar con una **mínima** interferencia mutua".

> **Dos usos de "punto de saturación".** En colas cerradas es $N^*$, un número de terminales. En **asignación de capacidad** (Medín 2025, parcial com. 305) se llama así al **umbral del factor de utilización** de un enlace, usualmente entre $0{,}8$ y $1$: si $\rho=\frac{\lambda}{\eta C}$ lo supera, el enlace está saturado o cerca (§9.6). Si la consigna no aclara cuál pide, conviene dar los dos.

(teoria/Teoría de Colas.md; cursada-2025/drive-propio/Resumen de Comunicación de datos - 2do parcial teoría.md)

### 9.2 Intensidad de tráfico y factor de utilización
**Salió:** 19/11/2021 y 17/12/2021 (MC); cursada 2025: M2, con el mismo ejemplo de 15 s y 10 s → 2 servidores (resumen del alumno).

**Respuesta.** La **intensidad de tráfico** $u$ es la relación entre el **tiempo de servicio promedio** $E[s]$ y el **intervalo promedio entre arribos** $E[\tau]$:
$$u=\frac{E[s]}{E[\tau]}=\lambda\,E[s]\qquad(\lambda=1/E[\tau]=\text{frecuencia de arribos})\quad[\text{Erlang}]$$
Determina la **cantidad mínima de servidores**: con $E[s]=15$ s y $E[\tau]=10$ s, $u=1{,}5$ → hacen falta al menos 2 servidores.
El **factor de utilización del servicio** es $\rho=u/c$ (intensidad de tráfico por servidor): la probabilidad de que un servidor esté ocupado. Con un solo servidor, $\rho=u$.

**En el MC:** "Respuestas **A y D** correctas". A es "tiempo de servicio promedio sobre el intervalo promedio entre arribos" y D es "tiempo de servicio promedio **por** la frecuencia de arribos": son la misma magnitud, porque $\lambda=1/E[\tau]$.

(teoria/Teoría de Colas.md)

### 9.3 Notación de Kendall: ¿qué simboliza la segunda M de M/M/1?
**Salió:** FAQ; cursada 2025: parcial com. 305 ("Qué es M/M/1 cuando es cola de espera sin límites, fuente de usuarios infinita y disciplina FIFO") (resumen del alumno).

**Respuesta.** La notación de Kendall es $A/B/c/k/n/Z$:
- $A$: distribución del **intervalo entre arribos**;
- $B$: distribución del **tiempo de servicio**;
- $c$: número de servidores;
- $k$: capacidad del sistema;
- $n$: tamaño de la población;
- $Z$: disciplina de la cola.

La forma corta $A/B/c$ supone cola sin límite, población infinita y disciplina FIFO. En **M/M/1**, la **segunda M** indica que el **tiempo de servicio tiene distribución exponencial** (Markoviana: servicio "aleatorio"), la primera M indica intervalos entre arribos exponenciales (arribos de Poisson), y el 1 indica un solo servidor.

**Para la consigna de la com. 305:** M/M/1 con cola ilimitada, población infinita y FIFO es el sistema en el que los intervalos entre arribos son exponenciales de media $1/\lambda$ (arribos de Poisson), el tiempo de servicio es exponencial de media $1/\mu$ y hay un único servidor.

(teoria/Teoría de Colas.md)

### 9.4 Elementos de un sistema de colas abiertas
**Salió:** cursada 2025: parcial com. 305 ("Enumere los elementos de un sistema de colas abiertas y explíquelos") y M2 (resumen del alumno). No salió en los finales relevados.

**Respuesta.** Una cola es una línea de espera; la teoría de colas estudia el fenómeno de esperar.
- **Fuente (población de usuarios):** las entidades que piden un servicio. **Infinita:** la frecuencia de arribos no depende de cuántos hay en el sistema. **Finita:** sí depende. Una población finita pero grande se aproxima como infinita.
- **Proceso de arribo:** intervalos entre arribos $\tau$ independientes e idénticamente distribuidos; en M/M, exponenciales (arribos de Poisson) de media $E[\tau]=1/\lambda$.
- **Servicio y servidores:** tiempo de servicio $s$ i.i.d.; el servicio "aleatorio" es exponencial, $W_s(t)=1-e^{-\mu t}$ con $\mu=1/E[s]$. Puede haber un servidor (atiende de a uno) o $c$ servidores idénticos.
- **Cola** y su **capacidad máxima:** infinita, o finita. En un *sistema de pérdida*, el que llega con todo ocupado no puede esperar.
- **Disciplina de cola:** FIFO (la habitual), LIFO o por prioridades.
- **Abierto** significa que los usuarios llegan del exterior, reciben el servicio y se van (a diferencia del cerrado, §9.1).

Tiempos: $t_w=t_q+t_s$, el tiempo en el sistema es el de cola más el de servicio.

```
 fuente ──λ──► [ cola ▯▯▯ ] ──► ( servidores 1..c, μ ) ──► salida
               ◄── t_q ───►     ◄──────── t_s ───────►
               ◄─────────────────── t_w ─────────────►
```

(teoria/Teoría de Colas.md; cursada-2025/drive-propio/Resumen de Comunicación de datos - 2do parcial teoría.md)

### 9.5 M/M/1 y M/M/c: medidas de performance, leyes de Little y percentil 90
**Salió:** cursada 2025: M2 y parcial com. 305 (ejercicios, con "conclusiones y propuestas de solución") (resumen del alumno). Es la teoría que se usa para interpretar el problema de colas del final práctico (04/04/2025).

**Respuesta.**
- $u=\lambda E[s]=\lambda/\mu$ (intensidad de tráfico) y $\rho=u/c$, que debe ser $<1$ para que el sistema sea estable.
- **M/M/c:** $W_q=\frac{C(c,u)\,E[s]}{c(1-\rho)}$. $C(c,u)$ es la fórmula C de Erlang: la probabilidad de que **todos los servidores** estén ocupados, o sea, de que el que llega tenga que esperar.
- **M/M/1** ($C=\rho$): $W_q=\frac{\rho\,E[s]}{1-\rho}$ y $W=W_q+E[s]=\frac{E[s]}{1-\rho}$.
- **Leyes de Little:** $L=\lambda W$ (usuarios en el sistema) y $L_q=\lambda W_q$ (en la cola).
- **Percentil 90:** $\pi_w(90)$ es el tiempo que no supera el 90 % de los usuarios, $P[t_w\le\pi_w(90)]=0{,}9$; ídem en la cola. En M/M/1: $\pi_w(90)=W\ln10\approx2{,}3\,W$ y $\pi_q(90)=W\ln(10\rho)$ (ver Dudas F).
- Cuando $\rho\to1$, $W$ y $L$ crecen sin límite. Por eso la conclusión típica es agregar servidores o separar el sistema en varios.

**Ejemplo** (apunte, ej. 1): $\lambda=1/48$ por min y $E[s]=30$ min → $\rho=5/8$, $W_q=50$ min, $W=80$ min, $\pi_q(90)=80\ln6{,}25\approx146{,}6$ min.

(teoria/Teoría de Colas.md; cursada-2025/drive-propio/Resumen de Comunicación de datos - 2do parcial teoría.md)

### 9.6 Asignación de capacidad de canales (Kleinrock): retardo y utilización de un enlace
**Salió:** cursada 2025: M2 (2.º parcial de Medín: conceptos y ejercicios con redes en estrella) (resumen del alumno). No salió en los finales de teoría relevados.

**Respuesta.** Se usa el criterio de **Kleinrock**: el costo es linealmente proporcional a la capacidad. El enlace de salida de cada concentrador se modela como una cola M/M/1: arribos de Poisson, longitudes de mensaje exponenciales, buffer FIFO infinito (los reales bloquean con probabilidad menor a $10^{-3}$) y tiempo de procesamiento nodal despreciable frente a la espera.
- $\lambda_i$ [mensajes/s]: frecuencia promedio de mensajes del enlace $i$, la suma de las de todas las líneas que entran al nodo (sus terminales más las de los nodos que cuelgan de él).
- $1/\eta_i$ [bits/mensaje]: longitud promedio del mensaje ($\eta_i$ = mensajes por bit).
- $\mu_i=\eta_iC_i$ [mensajes/s]: lo que puede despachar un enlace de capacidad $C_i$ [bps].
- **Retardo promedio:** $T_i=\frac{1}{\mu_i-\lambda_i}=\frac{1}{\eta_iC_i-\lambda_i}=\frac{1}{\eta_iC_i(1-\rho_i)}$. Incluye la transmisión y la espera en el buffer.
- **Utilización** (coincide con la intensidad de tráfico, porque hay un solo servidor): $\rho_i=\frac{\lambda_i}{\eta_iC_i}<1$. Si $\rho_i\to0$, $T_i\to\frac{1}{\eta_iC_i}$, que es el tiempo de transmitir un mensaje; si $\rho_i\to1$, $T_i\to\infty$. En 2025 se usó como umbral de saturación $0{,}8<\rho<1$ (§9.1).
- **Red completa:** aplicando Little a la red como "caja negra", $\delta=\sum\lambda_i$ y $E[T]=\frac{1}{\delta}\sum_i\lambda_iT_i$.
- **Regla de la raíz cuadrada** (capacidad total $C$ fija, minimizando $E[T]$ con multiplicadores de Lagrange): $C_i^{opt}=\frac{\lambda_i}{\eta_i}+C(1-\rho)\frac{\sqrt{\lambda_i/\eta_i}}{\sum_j\sqrt{\lambda_j/\eta_j}}$, con $\rho=\frac{1}{C}\sum_j\frac{\lambda_j}{\eta_j}$. Cada enlace recibe lo mínimo para su tráfico más una parte del sobrante proporcional a la raíz de su flujo. Más $C$ da menos retardo, pero más costo.

**Ejemplo** (apunte): $\lambda_1=0{,}33$ mens/s, $1/\eta_1=120$ bits, $C_1=100$ bps → $\eta_1C_1\approx0{,}833$ mens/s, $\rho_1\approx0{,}4$ y $T_1=\frac{1}{0{,}833-0{,}33}\approx2$ s.

(teoria/Asignación de Capacidad de Canales.md; cursada-2025/drive-propio/Resumen de Comunicación de datos - 2do parcial teoría.md)

---

## 10. Temas sin preguntas de teoría en los finales relevados

- **Asignación de capacidad de canales**, **OSI / TCP-IP / hardware de redes** y **multiplexado CDM/WDM**: no aparecen en ningún final de teoría disponible (2020–2025). CDM/WDM, colas abiertas y asignación de capacidad sí aparecen en el **2° parcial** (según el *Santo Resumen*) y entran en la práctica del final (problema de colas en 04/04/2025). En la cursada 2025, colas abiertas y asignación de capacidad se tomaron en el 2.º parcial de Medín (M2; ahora en §9.4–9.6). OSI/TCP-IP y CDM/WDM no aparecen en ningún material de 2025 relevado. Para el final de teoría, la prioridad sigue siendo baja.

---

## Dudas / pendientes

### A. Errores en las "soluciones sin corregir" (marcas de alumnos)

Las marcas se leyeron de los PDF (relleno verde o amarillo) y de los escaneos del 18/12/2020.

| Final | Pregunta | Marcó el alumno | Correcta según la cátedra | Por qué |
|---|---|---|---|---|
| 28/08/2020 | Palabra código | "Una secuencia fija de símbolos" | "Una secuencia fija de símbolos **códigos**" | El apunte: secuencias fijas del **alfabeto código** (§3.1). |
| 28/08/2020 | Código compacto | "…de todos los instantáneos que se pueden aplicar a esa fuente." | "…a esa fuente **con ese código**" | El apunte exige la misma fuente **y el mismo alfabeto** (§3.4). |
| 28/08/2020 | Matriz generadora | "LI y generar **todos** los EV" | "LI y generar **el** EV" | Una base genera un único (sub)espacio (§4.2). |
| 28/08/2020 | Familia de errores del síndrome | "Solo simples y dobles" | "**Todos** los errores" | Apunte: "todos los demás errores caerán en alguna de las familias" (§4.4). |
| 28/08/2020 | Zona montañosa, baja velocidad | Radioenlace | **Satélite** | Ej. 8 del apunte; el RE necesita visión directa (§8.3). |
| 28/08/2020 | Zona suburbana, baja velocidad | Par de cobre | **Radioenlace** (con espacio) | Ej. 4 del apunte. El par es discutible si hay red, pero no es la respuesta de la cátedra. |
| 10/09/2021 | Palabra código | "Una secuencia de símbolos códigos" | "Una secuencia **fija** de símbolos códigos" | Falta *fija* (§3.1). |
| 10/09/2021 | Código unívoco | "A cualquier **palabra** código le corresponde un único símbolo" | "A cualquier **secuencia** de palabras código le corresponde una única **secuencia** de símbolos" | Lo que marcó define *no singular*, no *unívoco* (§3.2). |
| 10/09/2021 | Matriz generadora | "LI y generar todos los EV ortogonales" | "LI y generar el EV" | Ídem 28/08/2020. |
| 10/09/2021 | Familia de errores | "Solo simples y dobles" | "Todos los errores" | Ídem. |
| 17/12/2021 | Punto de saturación | "Máximo de usuarios con **máxima** interferencia" | "Máximo de usuarios con **mínima** interferencia" | $N^*$ = máximo **sin** interferencia mutua (§9.1). |
| 17/12/2021 | Intensidad de tráfico | Solo D ($E[s]\cdot\lambda$) | **F (A y D)** | $E[s]/E[\tau]=\lambda E[s]$: las dos son correctas (§9.2). |
| 17/12/2021 | FDM con AM, ancho de banda | Solo E ($N\cdot2f_{max}$ DBL) | **G (C y E)** | También vale $N\cdot f_{max}$ para BLU (§7.2). |
| 17/12/2021 | Suburbana, velocidad media, con espacio físico | Cable coaxil con cablemodem | **Radioenlace** | El coaxil es solo residencial; "con espacio físico" apunta al mástil del RE (§8.3). |
| 17/12/2021 | Ruta 9, gran velocidad | **Satélite** | **Fibra óptica** | El satélite da BW bajo y caro; el mismo alumno de 2020 (y el 18/12/2020) marcó fibra (§8.3). |
| 17/12/2021 | Zona selvática, baja velocidad | Radioenlace | **Satélite** | Ej. 8 (montaña/selva) (§8.3). |

- Las marcas del **18/12/2020** (y del "2020-00-00", que es el mismo examen) coinciden todas con la respuesta de la cátedra.
- En **17/12/2021** el alumno marcó **dos** opciones en información mutua (D y E). Ver B.2.
- En **28/08/2020** y **10/09/2021** marcó la fórmula de entropía con "lg" (D), que es la del apunte. Ver B.3.

### B. Preguntas MC ambiguas (más de una opción defendible)
1. **Kraft (19/11/2021, 10/09/2021, 17/12/2021):** "Puede ser instantáneo" y "Puede ser compacto" son ciertas las dos: un código que cumple Kraft *puede* ser compacto. No hay opción combinada. **Tomé "Puede ser instantáneo"**, que es el texto de la nota del teorema en el apunte. Si te dejan, aclarálo por escrito.
2. **Información mutua:** el apunte la define como "la información transferida desde la fuente al receptor a través del canal, **esto es**, la información real que llega al receptor en promedio". Las opciones D y E reproducen el apunte. **Tomé D** (la definición principal). En 10/09/2021, E dice "la información real que llega al receptor" sin "en promedio", lo que refuerza D.
3. **Función entropía:** las opciones C ($\log$) y D ($\lg$) difieren solo en la notación del logaritmo. El apunte usa $\lg$ (base 2), que es lo que da bit/símbolo → **D**.
4. **Distancia de un código:** estrictamente, "la distancia de un código" es su distancia **mínima**. La opción que el examen da por buena (y que reproduce el apunte) es la distancia de Hamming entre dos palabras del mismo código.
5. **PCM 18/12/2020:** "se codifican y se transmiten a una velocidad del doble de $f_{max}$" es la mejor opción, pero es imprecisa: se transmiten **muestras** a $f_s\ge2f_{max}$; los **bits** salen a $n\cdot f_s$.
6. **Suburbana, baja velocidad (sin más datos):** la respuesta depende del supuesto de espacio físico. La cátedra (ej. 4) da radioenlace con espacio, y sin espacio el análogo es satélite (ej. 3). El 2° parcial 2025 pregunta justamente la variante "sin espacio físico".

### C. Errores o contradicciones en las "Preguntas frecuentes", "Teoria vieja" y "Resumen.md"
1. **Entropía del canal (FAQ P1 #2 y #11, Teoria vieja):** dice que "es la probabilidad de aparición de un símbolo $b_j$ a la salida cuando se envió $a_i$". **Es incorrecto:** eso es $P(b_j/a_i)$, una probabilidad, no una entropía. La entropía del canal es la equivocación $H(B/A)$ (§1.4). La FAQ P2 lo dice bien ("entropía calculada conociendo la equivocación de B respecto de A").
2. **Código compacto (FAQ P1 #5, FAQ P2, Resumen.md):** lo define como "código **unívoco** … menor o igual que todos los **unívocos**". El apunte y el *Santo* dicen "código **instantáneo** … todos los **instantáneos**". Por McMillan las longitudes mínimas coinciden, así que no hay contradicción de fondo, pero en el MC hay que usar la versión del apunte (instantáneo).
3. **"¿Cada mensaje ocupa un lugar determinado del BW?" (FAQ P1 #6):** responde "sí" para todos los casos. **Está mal planteado:** es cierto en FDM; en TDM cada muestra ocupa **todo** el BW y lo que se asigna es una ranura de tiempo (§7.3).
4. **Ancho de banda práctico (FAQ P2):** afirma que recortar en $1/\tau$ "recupera el 98 % de la información". El apunte no da ese porcentaje. Para un pulso rectangular, la energía hasta el primer cero ronda el 90 % (conocimiento general). **No lo uses como dato.** Además, el apunte 1 da $B=s/2$ (ancho mínimo de Nyquist) y el apunte 5 usa $B_w=1/\tau$ (cruce por cero). Son contextos distintos; el *Santo* recomienda preguntar cuál pide la comisión.
5. **Kendall (FAQ P1 #16):** dice que la segunda M simboliza "tiempo de servicio **o** de intervalo entre arribos". Es impreciso: la **posición** de la letra decide. La segunda letra es siempre el **tiempo de servicio** (§9.3).
6. **Huffman con $r=2$ (FAQ P1 #8):** lo que dice es correcto, pero omite el punto interesante, que es el caso **r-ario**: hace falta $q=r+\alpha(r-1)$ o agregar símbolos falsos de probabilidad nula (§3.4). Probablemente la pregunta original apuntaba a eso.
7. **Ejemplos de la FAQ P1 #5 y #14:** usa **el mismo** código (`1, 01, 001, 0001`) como ejemplo de no singular, unívoco e instantáneo. Es válido (un instantáneo es las tres cosas), pero **no sirve para distinguirlos**. En el examen conviene dar un ejemplo por clase (§3.2).
8. **Banda ancha (FAQ P1 #20, FAQ P2):** la definición ("la banda ancha es el espectro para la transmisión de datos entre dos puntos") es vaga. Usé la del apunte de Principios Básicos citada por el *Santo* (banda base vs. banda ancha) (§5.4).
9. **Resumen.md, PSK multinivel:** dice "dos fases y cuatro amplitudes". El apunte dice **4 fases × 2 amplitudes** (el total de 8 estados y 3 bits coincide).
10. **Resumen.md, demodulación PSK:** dice "solo se puede utilizar la demodulación **asincrónica**". **Es al revés:** el apunte dice que PSK es solo **sincrónica o coherente** ("no existe incoherente").
11. **Resumen.md, punto de saturación:** dice "número máximo de **servidores**". Son **terminales o usuarios**; el sistema cerrado tiene una sola CPU.
12. **FAQ P1 #4 / Teoria vieja, FSK:** "Se hace necesaria la presencia de la portadora en el lugar de destino" vale solo para la demodulación **coherente**. FSK también admite detección de envolvente.
13. **FAQ P1, listado final de temas:** el caso "zona urbana y requiere gran velocidad (**bajo** ancho de banda)" es contradictorio. Se tomó gran velocidad = alto ancho de banda → fibra.
14. **FSK multinivel:** el apunte lo describe como "2 frecuencias y 2 amplitudes" (en rigor sería ASK+FSK combinadas). El *Santo* lo resume como "más frecuencias en FSK". Para el examen, usá la versión del apunte y aclará que el aumento sale de tener más estados por símbolo.

### D. Pendientes
- **Respuestas oficiales:** no hay ninguna resolución de la cátedra en el Drive (lo confirma el *Santo*). Las respuestas de los MC de este banco son mías, argumentadas con el apunte.
- **"2020-00-00 (Solución sin corregir)":** no tiene fecha, pero sus preguntas y marcas son idénticas al escaneo del 18/12/2020. Lo traté como el mismo examen. Si fuera otra mesa, la frecuencia de los temas de ese examen sube en 1.
- **"Teoria vieja.md" y FAQ:** no tienen fecha y son del plan viejo. Las conté aparte (columna FAQ), no como finales.
- **El apunte de Medios de transmisión** está en `fuentes/practica/`, no en `fuentes/teoria/`. La parte de satélites y radioenlace de §8.2 se apoya en él y en el *Santo*.
- **Ruta 9:** que haya troncales de fibra sobre el corredor Rosario–Cañada de Gómez es contexto local, no está en el apunte. La elección de fibra se justifica igual por el ancho de banda ("gran velocidad" > 100 M → solo FO).
- **Transpondedor (MC.29):** confirmar con el material de Baró qué valor da (50–100 MHz o 36–50 MHz).

### E. Marcas del compendio MC de Baró (B2)
De las 44 preguntas, la marca del alumno está **mal en 1**, es **dudosa en 1** y **falta en 1**. Las demás coinciden con el apunte o con conocimiento general sólido.
1. **VSAT (MC.32), mal:** marcó "Very Small Amplitude Terminals". Es *Very Small **Aperture** Terminal* → "ninguna de las anteriores". El otro resumen del 2.º parcial (`resumenes/2° Parcial/Resumen Parcial 2 (2025).md`) lo corrige igual, y la otra versión de la misma pregunta ("terminales de apertura muy pequeña") el alumno la marcó bien.
2. **Transpondedor (MC.29), dudosa:** marcó "50 a 100 MHz", que repite en su resumen. Tanenbaum da 36–50 MHz por transpondedor (conocimiento general) y el apunte de la cátedra no da el número. Si Baró lo dio en clase, usá su valor; si no, "36 a 50 MHz".
3. **"Las ondas por láser" (MC.26), sin marca:** por descarte, "prácticamente se usan solo dentro de la fibra óptica". El otro resumen tampoco la resuelve.
4. **Ambiguas aunque la marca sea defendible:**
   - Velocidad en el aire, segunda versión (MC.34): "mayor que en cualquier medio guiado" y "igual a 300.000 km/s" son las dos casi ciertas (en el aire $v\approx c$; estrictamente, $c$ es en el vacío).
   - Infrarrojo, "se utiliza para transmisión en fibra óptica" (MC.21): la fibra trabaja en infrarrojo cercano, así que no es absurda; la pregunta apunta al infrarrojo inalámbrico.
   - Microondas, "se propagan unidireccionalmente" (MC.14): son direccionales (haz). La marcada, "λ muy pequeña y frecuencia elevada", es la segura.
5. **El resumen del mismo alumno ("Resumencirijillo", al final de B2) contradice sus propias marcas:**
   - "Ley de Snell: ángulos de incidencia y **reflexión**": en el MC marcó **refracción**, que es lo correcto (MC.6).
   - "Propagación FO: **mayor** que cualquier medio": es falso; en el MC marcó "menor que en el aire", que es lo correcto (MC.12).

### F. Errores en los resúmenes de la cursada 2025 (M1, M2, B3)
1. **M1, familia de errores:** "se pueden observar solo los errores simples y dobles" → **falso**: son **todos** los errores (§4.4). Es la misma marca errónea de los finales 2020/2021 (Dudas A).
2. **M1, capacidad:** pone $C=\max H(A)$ como definición general. Solo vale en un canal **transparente**; en general $C=\max I(A,B)$ (§1.6).
3. **M1, equivocaciones:** escribe $H(A/B)$ y $H(B/A)$ sin el signo menos; así, con $\lg P\le0$, dan negativas. Va $-\sum\sum$ o $\lg\frac{1}{P}$. El apunte tiene la misma errata en una línea y la corrige en la siguiente.
4. **M1, "código de bloque" en códigos lineales:** lo define como palabras de longitud constante $n$. En codificación de fuente, "código bloque" es otra cosa: cada símbolo va a una secuencia fija, de longitud que puede variar (§3.1). Mismo nombre, dos conceptos; si aparece, aclaralo.
5. **M1, S/R y dB:** "[S/N] = dB" → la S/N es adimensional (cociente de potencias) y el dB es una forma de expresarla. Además, la ganancia en dB con tensiones o corrientes es $20\log$, no $10\log$ (§dB.2).
6. **M1, Hamming:** el "método analítico" asigna $i_0,i_1,i_2,i_3$ a las posiciones 3, 5, 6 y 7, lo que da $C_1\oplus i_0\oplus i_1\oplus i_3$, $C_2\oplus i_0\oplus i_2\oplus i_3$ y $C_3\oplus i_1\oplus i_2\oplus i_3$. Pero después copia las ecuaciones del diagrama de Venn ($C_1\oplus i_0\oplus i_1\oplus i_2$, …), que corresponden a otra asignación. Las dos son códigos de Hamming válidos; no las mezcles en un mismo ejercicio.
7. **M1, distorsión:** "altera la amplitud de la señal". Altera la **forma**: amplitud y fase según la frecuencia (§2.2).
8. **M2, retardo:** "el tiempo de retardo se define como el tiempo necesario para transmitir el mensaje completo". Eso es solo el límite $\rho\to0$; en general $T_i$ incluye la espera en el buffer. El apunte dice "para $\rho_i<1$", pero el sentido es $\rho_i\ll1$ (§9.6).
9. **M2, $C(c,u)$:** "probabilidad de que todos los **usuarios** estén ocupados" → son los **servidores**.
10. **M2, percentil 90 en M/M/1:** escribe $\pi(90)=W\ln(10\rho)$ y $\pi_q(90)=W_q\ln(10\rho)$. Lo correcto es $\pi_q(90)=W\ln(10\rho)$ en la cola y $\pi_w(90)=W\ln10$ en el sistema. El ejemplo del hospital usa bien $\pi_q=W\ln(10\rho)\approx113{,}8$ min, y el apunte lo confirma (146,6 min $=80\ln6{,}25$).
11. **M2, hospital:** pasa $E[s]=20$ min a "0,3 h" (es $0{,}\overline{3}$ h) y llama $L$ a "pacientes en cola" ($L$ es en el sistema; en cola es $L_q$). Los resultados en minutos están bien.
12. **M2, ejercicios de asignación:** en el del ISP, $\rho=\frac{150/1230}{5000/1500}\approx0{,}037$ (pone 0,03; la conclusión no cambia). En el del DataCenter, $\rho_1=1{,}2/750=0{,}0016$ (no "0,0016 %"), y la fórmula del retardo está mal escrita: $T_1=\frac{1}{\eta C_1-\lambda_1}=\frac{1}{750-1{,}2}\approx1{,}34$ ms.
13. **B3, FM:** "se trabaja con $f_p=100$ kHz" → son **100 MHz** (radio FM, 88–108 MHz; el apunte 5 dice 100 MHz).
14. **B3, PDM/PWM:** "varía solo frecuencia" → varía el **ancho (duración)** del pulso. El mismo resumen lo dice bien más abajo.
15. **B3, último ejercicio (38 + 2 muestras, 8 bits, 5 kHz):** $T_s=1/10\text{ kHz}=0{,}1$ **ms**, no µs. Entonces $\tau=0{,}1\text{ ms}/320=0{,}3125$ µs y $r=3{,}2$ **Mbps**, no Gbps. En otro ejercicio, "1,136 mHz" es MHz.
16. **B3, demodulación:** "para demodulación se utiliza ASK" es una frase trunca; no la uses. La demodulación está en §5.1.
