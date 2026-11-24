# Comunicación de Datos — Banco de preguntas de teoría (finales)

UTN FRRo · ISI · 3° año · Teoría: Ing. Jorge A. Campanaro.

**Qué hay acá.** Todas las preguntas de teoría de los finales disponibles, agrupadas por tema y con **respuesta modelo** de extensión de examen escrito. Las preguntas equivalentes están fusionadas, con todas sus fechas.

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

Rutas de las citas, relativas a `materias/CD/fuentes/`. "(conocimiento general)" = no está en el material de la cátedra.

---

## Frecuencia de temas

★ = salió en 4 o más finales · ★★ = salió en 6 (todos los que tenían ese bloque).

| Tema | 28/08/20 | 18/12/20 | 10/09/21 | 19/11/21 | 17/12/21 | 04/04/25 | FAQ (s/f) | Finales |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Inecuación de Kraft | X | X | X | X | X | X | X | **6 ★★** |
| Cota inferior de la longitud media | X | X | X | X | X | X | X | **6 ★★** |
| Elección del medio de acceso (zona × velocidad) | X | X | X | X | X | X | X | **6 ★★** |
| Código unívoco | X | | X | X | X | X | X | **5 ★** |
| Código compacto | X | | X | X | X | X | X | **5 ★** |
| Código bloque / palabra código / no singular | X | X | X | X | X | | X | **5 ★** |
| Distancia de un código / $d_{min}=1$ | X | X | X | X | X | | | **5 ★** |
| Tasa de información / tasa de dígitos | X | X | X | X | X | | X | **5 ★** |
| FDM (concepto, ancho de banda, duplicar señales) | X | X | X | X | X | | X | **5 ★** |
| TDM (concepto) | X | X | X | X | X | | X | **5 ★** |
| Digitalización: muestreo, Nyquist, PCM | X | X | X | X | X | | X | **5 ★** |
| AM (definición, bandas laterales, portadora suprimida) | X | X | X | X | X | | | **5 ★** |
| Mensaje digital por red analógica (ASK/FSK/PSK, multinivel) | X | X | X | | | X | X | **4 ★** |
| Código instantáneo y su condición | X | X | X | | | X | X | **4 ★** |
| Información mutua | X | | X | X | X | | X | **4 ★** |
| Familia de errores de un síndrome | X | | X | X | X | | | **4 ★** |
| Medios: fibra, radio, satélite (propiedades) | X | X | X | | | X | X | **4 ★** |
| Entropía de la fuente | X | X | X | | | | X | 3 |
| Canal binario simétrico / entropía del canal | | X | | X | X | | X | 3 |
| Síndrome (concepto) | | X | | X | X | | X | 3 |
| Matriz generadora / base de un código de grupo | X | | X | | | | X | 2 |
| Colas: punto de saturación, intensidad de tráfico | | | | X | X | | X | 2 |
| Errores de canal / ruido impulsivo | | | | | | | X | 0 (solo FAQ) |
| Huffman, extensión r-aria | | | | | | | X | 0 (solo FAQ) |
| Asignación de capacidad, OSI/TCP-IP, CDM/WDM | | | | | | | | 0 |

**Lectura rápida.** El núcleo que se repite en todos los finales es **codificación de fuente** (unívoco, instantáneo, Kraft, compacto, cota inferior) y **elección de medio de acceso**. Lo segundo más frecuente: **FDM/TDM/muestreo/AM** y **distancia/síndrome**. El final de 2025 (plan actual) pasó a desarrollo pero repitió exactamente esos tres bloques: modulación digital sobre red analógica, códigos y medios de acceso.

---

## 1. Teoría de la información

### 1.1 Entropía de la fuente: concepto, fórmula, cuándo es máxima
**Salió:** 18/12/2020 (MC "La entropía de la fuente es…"), 28/08/2020 y 10/09/2021 (MC "La función entropía es…"), FAQ ("Definir entropía", "¿Cuándo la entropía es máxima?").

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
**Salió:** tasa de información en 18/12/2020, 19/11/2021 y 17/12/2021 (MC); tasa de dígitos en 28/08/2020 y 10/09/2021 (MC); FAQ "Concepto de entropía, tasa de información, tasa de dígitos y velocidad de señalización. Dar ejemplos".

**Respuesta.**
- **Tasa (velocidad) de información $R$:** cantidad de bits **en promedio** que se transmiten en 1 segundo, es decir, la información **promedio** que produce la fuente **por unidad de tiempo**. $R = H'(A)$ [bit/s]. Con canal ruidoso, a la salida llega $R = H'(A) - H'(A/B)$.
- **Tasa de dígitos (binits) $r$:** cantidad de **dígitos transmitidos por segundo** [dígitos/s]. Se relaciona con la anterior por $R = r\cdot H(A)$: $H$ mide información en bit/símbolo, $R$ en bit/s.
- **Velocidad de señalización $s$:** inversa de la duración del pulso más corto, $s = 1/\tau_{min}$ [baudios]. Con pulsos de $n$ niveles equiprobables e iguales duraciones: $R = \frac{1}{\tau}\lg n = s\,\lg n$.

**Ejemplo:** pulsos de $\tau = 1$ ms con 4 niveles equiprobables → $s = 1000$ baudios, $r = 1000$ dígitos/s, $H = \lg 4 = 2$ bit/dígito, $R = r\,H = 2000$ bit/s. Si los pulsos fueran binarios, $R = s = 1000$ bit/s: en binario equiprobable **la capacidad coincide con la señalización**.

**En el MC:** tasa de información = "la información **promedio** que emite la fuente **por unidad de tiempo**" (la que dice "la información que emite…" sin "promedio" no es la definición). Tasa de dígitos = "la cantidad de dígitos transmitidos por segundo" (no son "dígitos de información" ni "dígitos de señalización").

(teoria/1 - Información, Codificación y Canales.md)

### 1.3 Canal binario simétrico (BSC)
**Salió:** 18/12/2020, 19/11/2021, 17/12/2021 (MC).

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
**Salió:** información mutua en 28/08/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC); FAQ "Concepto de entropía, de información mutua y de entropía del canal", "En un canal real, ¿cuál es la entropía que lo define y cuál es su concepto?".

**Respuesta.**
- **Entropía a priori** $H(A)$: incertidumbre sobre la fuente antes de recibir.
- **Equivocación de A respecto de B** $H(A/B)$: incertidumbre que **queda** sobre la fuente después de recibir. Es la información que "bloquea" el canal.
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

---

## 3. Codificación de fuente

> Bloque más preguntado. En el MC las opciones difieren en una palabra: hay que saber la definición textual del apunte.

### 3.1 Código bloque y palabra código
**Salió:** código bloque en 18/12/2020; palabra código en 28/08/2020, 10/09/2021, 19/11/2021 y 17/12/2021 (MC).

**Respuesta.** Codificar es poner en correspondencia las secuencias del **alfabeto fuente** $S=\{s_1,\dots,s_q\}$ con secuencias de un **alfabeto código** $Z=\{z_1,\dots,z_r\}$.
- **Código bloque:** asigna a **cada símbolo del alfabeto fuente una secuencia fija de símbolos del alfabeto código**.
- **Palabra código:** cada una de esas **secuencias fijas de símbolos del alfabeto código**.

Ejemplo: $s_1\to 00,\ s_2\to 01,\ s_3\to 10,\ s_4\to 11$. Cada $s_i$ tiene asignada siempre la misma palabra.

**En el MC:** código bloque = "asigna a cada uno de los símbolos del alfabeto fuente una secuencia fija de símbolos del alfabeto código" (las otras invierten fuente y código). Palabra código = "una secuencia **fija** de símbolos **códigos**": "una secuencia fija de símbolos" no dice de qué alfabeto, y "una secuencia de símbolos códigos" omite *fija*.

(teoria/2 - Codificación.md)

### 3.2 Código no singular, unívoco e instantáneo (definiciones y ejemplos)
**Salió:** no singular en 18/12/2020; unívoco en 28/08/2020, 10/09/2021, 19/11/2021, 17/12/2021 y **04/04/2025** (desarrollo); instantáneo en 18/12/2020 y **04/04/2025**; condición necesaria y suficiente de instantáneo en 28/08/2020, 18/12/2020 y 10/09/2021; FAQ ("Definir código no singular, unívoco e instantáneo. Dar ejemplos", "Concepto de código unívoco, instantáneo y compacto. Condiciones necesarias").

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

**En el MC:** unívoco = "si a cualquier **secuencia de palabras** código le corresponde una y solo una **secuencia de símbolos** de la fuente". "Si a cualquier palabra código le corresponde un único símbolo" describe un código no singular, no uno unívoco. Instantáneo = "puede decodificarse sin esperar la llegada de la próxima palabra código" y su condición = "ninguna palabra código sea **prefijo** de otra" (no "terminación"/"subfijo", y la longitud variable no tiene nada que ver).

(teoria/2 - Codificación.md; resumenes/El Santo Resumen/el-santo-resumen.md, sección Final)

### 3.3 Inecuación de Kraft (y McMillan)
**Salió:** 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC "Un código que cumple la inecuación de Kraft es…") y **04/04/2025** ("Explicar la inecuación de Kraft").

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
**Salió:** compacto en 28/08/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC) y **04/04/2025**; FAQ ("Concepto de código compacto y ventajas de su aplicación", "¿Para qué sirve el método de Huffman? ¿Qué puede suceder si el alfabeto código tiene r=2?").

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
**Salió:** 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC) y **04/04/2025** ("Dar la cota inferior de la long. media"); FAQ.

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
**Salió:** concepto en 18/12/2020, 19/11/2021, 17/12/2021 (MC); FAQ ("Concepto de síndrome y aplicaciones. Ejemplo. Condiciones necesarias para corregir errores simples en cada uno de los dígitos de la palabra código", "¿Por qué el síndrome de una palabra con error coincide con el síndrome de la palabra que modela el error?").

**Respuesta.**
- **Síndrome:** resultado de multiplicar la **palabra recibida (posiblemente con error) por la matriz de control de paridad transpuesta**: $S = v^{*}\cdot H^T$. Dimensiones: $(1\times n)(n\times(n-m)) = 1\times(n-m)$.
- **Aplicación:** si $S=0$, la palabra pertenece al código de grupo (es correcta, o tiene un error no detectable). Si $S\ne 0$ hubo error, y el síndrome **identifica qué error fue** → se corrige sumándolo. Si hay ambigüedad, se usa máxima verosimilitud: la palabra del código a menor distancia de Hamming.
- **¿Por qué $S(v^{*})=S(e)$?** Modelando el error como una palabra $e$ con unos en las posiciones alteradas, $v^{*}=v\oplus e$:
$$S(v^{*})=(v\oplus e)\,H^T = \underbrace{v\,H^T}_{=0\ (v\in V)} \oplus\; e\,H^T = S(e)$$
El síndrome depende solo del error, no de la palabra transmitida. Por eso el mismo error en dos palabras distintas da el mismo síndrome.
- **Condición para corregir error simple en cada uno de los $n$ dígitos:** cada error simple $e_i$ debe dar un síndrome **distinto y no nulo**. Hacen falta al menos $n$ síndromes no nulos: $2^{n-m}-1\ge n$. Como $e_i H^T$ es la columna $i$ de $H$, eso equivale a que **las columnas de $H$ sean todas distintas y no nulas** (esto último es derivación propia). Si dos errores simples $e_a$ y $e_b$ dan el mismo síndrome, se **detecta** el error pero **no se corrige**.

**Ejemplo** (apunte): $v_1=101110$ y $v_2=111001$ con el error $e=000100$ → $v_1\oplus e=101010$ y $v_2\oplus e=111101$. Las dos dan el mismo $S=e\,H^T\neq0$ → error en el 4.º dígito; se corrige y se recupera $v_1$ y $v_2$.

**En el MC:** "El resultado de multiplicar una palabra **con error** por la matriz de **control de paridad transpuesta**". No es una palabra correcta (daría 0) ni la matriz generadora.

(teoria/3 - Detección y Corrección de errores.md)

### 4.4 Familia de errores de cada síndrome; errores no detectables
**Salió:** familia en 28/08/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC); FAQ ("En qué condiciones no se detecta y corrige un error").

**Respuesta.**
- **Errores no detectables:** los que **coinciden con palabras del código de grupo** (distintas de la nula). Como $e\in V$, $v\oplus e\in V$ y el síndrome sigue siendo 0: el receptor lo toma como palabra correcta. En el ejemplo del apunte (código de 8 palabras de 6 dígitos), no se detectan los errores triples y cuádruples cuyo patrón es una palabra del código (`101010`, `011011`, …).
- **Familia de un síndrome:** todos los patrones de error que producen ese mismo síndrome. Según el apunte, **todos los demás errores caen en alguna de las familias asociadas a cada síndrome**. En cada familia hay errores simples, dobles, múltiples, etc., y son $2^m$ patrones por síndrome: el error "representante" sumado a cada palabra del código (conocimiento general, *coclase*). Por eso el decodificador asume el de **menor peso** (el más probable).

**En el MC:** "**Todos** los errores de las palabras código asociadas a ese síndrome". No "solo simples" ni "solo simples y dobles".

(teoria/3 - Detección y Corrección de errores.md)

---

## 5. Comunicaciones digitales: modulación

### 5.1 Mensaje digital por una red analógica: tipos, aplicación, cómo aumentar la velocidad, gráficas
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

### 5.2 Modulación de amplitud (AM): definición, ubicación del mensaje, portadora suprimida, banda lateral única
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

---

## 6. Muestreo, digitalización y PCM

### 6.1 ¿Qué hay que hacer primero para digitalizar un mensaje analógico? (Nyquist)
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

### 6.2 PCM (modulación por pulsos codificados)
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

---

## 8. Medios de transmisión y elección del medio de acceso

### 8.1 Propiedades de los medios (MC verdadero/falso y opciones)
**Salió:** fibra y ruido eléctrico en 28/08/2020, 18/12/2020, 10/09/2021; "la fibra transmite por…" en 18/12/2020; atenuación de ondas de radio en 28/08/2020, 18/12/2020, 10/09/2021; ventaja del satélite en 28/08/2020 y 10/09/2021; cablemodem en 10/09/2021.

**Respuestas.**
- **"El ruido eléctrico, interferencias y acoplamientos eléctricos afectan a la fibra óptica" → FALSO.** La fibra transporta **luz**, así que las sobrecargas de energía, la interferencia electromagnética y los cortes de suministro no la afectan.
- **"La transmisión por fibra óptica se realiza por…" → pulsos de luz.** Un pulso de luz es un 1 y su ausencia es un 0. El sistema tiene fuente de luz, medio (fibra) y detector.
- **"La atenuación de las ondas de radio depende de la frecuencia y de la distancia recorrida" → VERDADERO.** Las propiedades de las ondas de radio dependen de la frecuencia: a baja frecuencia atraviesan obstáculos pero la potencia cae drásticamente con la distancia; a alta frecuencia viajan en línea recta, rebotan y la lluvia las absorbe (microondas desde unos 4 GHz).
- **"Una de las ventajas de las microondas satelitales es…" → poder llegar con la señal a lugares muy lejanos e inaccesibles.** El satélite es un repetidor en el cielo con gran cobertura. Las demás opciones son falsas: el ancho de banda satelital es caro y menor que el de la fibra, el aire no da "más velocidad" y la instalación del enlace no es barata.
- **"Una empresa de zona urbana que requiere gran ancho de banda contrata cablemodem por coaxil a la empresa de TV cable" → FALSO.** Según la cátedra, el coaxil queda **solo para cablemodem de usuarios residenciales** por la red de TV cable. Para una empresa urbana con gran BW se usa fibra óptica.

(practica/3 - Medios de transmisión.md; teoria/Elección medio de acceso V03.md)

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
**Salió:** **04/04/2025** (3-b, cuatro casos) y MC de 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021; FAQ (dos variantes con tres casos cada una).

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

**Segurización.** Si el servicio no admite cortes, se agrega un segundo acceso con **recursos disjuntos**:
- recorridos de fibra que no compartan tramo hasta la sala de equipos;
- y, mejor, **otro operador con infraestructura propia** (si el operador 2 alquila infraestructura al 1, una caída del 1 tira ambos).

(teoria/Elección medio de acceso V03.md; resumenes/El Santo Resumen/el-santo-resumen.md, "Elección del medio de acceso")

---

## 9. Teoría de colas

### 9.1 Punto de saturación de un sistema de cola cerrada
**Salió:** 19/11/2021 y 17/12/2021 (MC); FAQ ("Explique brevemente y grafique adecuadamente el punto de saturación de un sistema de cola cerrada").

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

(teoria/Teoría de Colas.md)

### 9.2 Intensidad de tráfico y factor de utilización
**Salió:** 19/11/2021 y 17/12/2021 (MC).

**Respuesta.** La **intensidad de tráfico** $u$ es la relación entre el **tiempo de servicio promedio** $E[s]$ y el **intervalo promedio entre arribos** $E[\tau]$:
$$u=\frac{E[s]}{E[\tau]}=\lambda\,E[s]\qquad(\lambda=1/E[\tau]=\text{frecuencia de arribos})\quad[\text{Erlang}]$$
Determina la **cantidad mínima de servidores**: con $E[s]=15$ s y $E[\tau]=10$ s, $u=1{,}5$ → hacen falta al menos 2 servidores.
El **factor de utilización del servicio** es $\rho=u/c$ (intensidad de tráfico por servidor): la probabilidad de que un servidor esté ocupado. Con un solo servidor, $\rho=u$.

**En el MC:** "Respuestas **A y D** correctas". A es "tiempo de servicio promedio sobre el intervalo promedio entre arribos" y D es "tiempo de servicio promedio **por** la frecuencia de arribos": son la misma magnitud, porque $\lambda=1/E[\tau]$.

(teoria/Teoría de Colas.md)

### 9.3 Notación de Kendall: ¿qué simboliza la segunda M de M/M/1?
**Salió:** FAQ.

**Respuesta.** La notación de Kendall es $A/B/c/k/n/Z$:
- $A$: distribución del **intervalo entre arribos**;
- $B$: distribución del **tiempo de servicio**;
- $c$: número de servidores;
- $k$: capacidad del sistema;
- $n$: tamaño de la población;
- $Z$: disciplina de la cola.

La forma corta $A/B/c$ supone cola sin límite, población infinita y disciplina FIFO. En **M/M/1**, la **segunda M** indica que el **tiempo de servicio tiene distribución exponencial** (Markoviana: servicio "aleatorio"), la primera M indica intervalos entre arribos exponenciales (arribos de Poisson), y el 1 indica un solo servidor.

(teoria/Teoría de Colas.md)

---

## 10. Temas sin preguntas de teoría en los finales relevados

- **Asignación de capacidad de canales**, **OSI / TCP-IP / hardware de redes** y **multiplexado CDM/WDM**: no aparecen en ningún final de teoría disponible (2020–2025). CDM/WDM, colas abiertas y asignación de capacidad sí aparecen en el **2° parcial** (según el *Santo Resumen*) y entran en la práctica del final (problema de colas en 04/04/2025). Para el final de teoría, la prioridad es baja.

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
