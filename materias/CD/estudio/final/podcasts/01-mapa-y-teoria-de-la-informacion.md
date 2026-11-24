# Podcast CD 1 de 8 — El mapa del sistema y la teoría de la información

Fuente para un episodio de podcast de estudio. Materia: Comunicación de Datos (UTN Facultad
Regional Rosario, Ingeniería en Sistemas, 3.er año). Sirve para rendir el final: tres problemas
de práctica y tres preguntas de teoría para desarrollar. Las respuestas de las preguntas son
respuestas modelo armadas por nosotros a partir de los apuntes de la cátedra, no la corrección
oficial.

## Indicaciones para el episodio

Primero el recorrido completo de un mensaje, de la fuente al destino, para ubicar cada tema de la materia. Después información, entropía, el canal binario simétrico, las entropías del sistema y la información mutua: qué mide cada una y cómo se relacionan. Contá el procedimiento del ejercicio del canal binario, no leas los números.

## Contenido principal

### 0. Qué entra y cómo se toma

#### 0.1 El formato del final

El último final disponible es el del **04/04/2025**, el único del plan actual:

| Parte | Qué se tomó en 2025 | Dónde |
|---|---|---|
| **Práctica**: 3 problemas | Multinivel: 27 pulsos de 128 niveles, arranque +4 V y stop −4 V, 10 μs por pulso | §3.2 |
| | Trama PCM: 25 + 2 muestras, señales de 400 a 3500 Hz, 7 dígitos por muestra | §7.4 |
| | Cola M/M/1: sala de emergencias, un paciente cada 30 min, atención de 20 min | §9.3 |
| **Teoría**: 3 preguntas para desarrollar | Mensajes digitales por una red analógica: modulaciones, cómo aumentar la velocidad, aplicación y gráficas | §6.3 |
| | Propiedades de los códigos: unívoco, instantáneo, compacto, Kraft, cota inferior de la longitud media | §4 |
| | Medios de acceso: ventajas y desventajas, y cuál elegir según zona y velocidad | §8 |

En 2020–2021 la teoría era *multiple choice*. En 2025 pasó a desarrollo, pero repitió los mismos bloques, y dos de los tres problemas repiten números exactos de 2021.

#### 0.2 Qué sale más

Síntesis de los dos bancos: 9 hojas de práctica y 6 finales de teoría de 2020–2025.

| Tema | Parte | Cuánto sale | Sección |
|---|---|---|---|
| **Transmisión multinivel** | práctica | 8 de 9 hojas | §3 |
| **TDM-PCM** (ancho de banda de la trama) | práctica | 8 de 9 | §7 |
| **Cola M/M/1** | práctica | 5 de 9 | §9 |
| **Canal binario simétrico** | práctica | 4 de 9 | §2 |
| **Kraft**, **cota inferior de la longitud media**, **elección del medio de acceso** | teoría | 6 de 6 | §4, §8 |
| Código unívoco, compacto, bloque; distancia de un código; tasa de información; FDM, TDM, muestreo, AM | teoría | 5 de 6 | §2, §4–§7 |
| Modulación digital por red analógica; código instantáneo; información mutua; familia de errores; medios | teoría | 4 de 6 | §2, §4–§6, §8 |
| FDM numérico, Hamming, Huffman, códigos lineales | práctica | casi sólo antes de 2020 | §4, §5, §7 |
| Asignación de capacidad, OSI y TCP/IP, CDM y WDM | — | nunca en 2020–2025 | §9.6, §10 |

**Lectura rápida.** La práctica es casi siempre **multinivel + PCM + (colas o canal binario)**. La teoría, **códigos + medio de acceso + modulación o multiplexado**.

#### 0.3 Reglas para el examen

1. **Si hay ambigüedad, escribí el criterio que usás.** Los casos conocidos:
   - ancho de banda de la trama: $B_w = 1/\tau$ (el de la cátedra) o $B = s/2$ (§7.3);
   - muestrear con $2f_{max}$ o con $2(f_{max} - f_{min})$ (§7.4);
   - si los pulsos de arranque y stop están dentro del total o se suman aparte (§3.2);
   - en colas, qué inciso es tiempo en cola y cuál tiempo en el sistema (§9.3);
   - en el medio de acceso, si hay espacio físico y si hace falta segurización (§8.2).
2. **En PCM y FDM piden siempre tres cosas**: la técnica, los gráficos y los cálculos con unidades.
3. **No redondees la información** $I$. Los niveles se redondean **para arriba**; la cantidad de señales que entran en un canal, **para abajo**.
4. **En colas, definí cada término** antes de calcularlo.
5. **En teoría vale la definición textual del apunte.** En los *multiple choice* las opciones difieren en una palabra.

### 1. El mapa: el sistema de comunicación de punta a punta

*Fuentes: apuntes 1 y 5 de teoría y El Santo Resumen.*

Pensá en una videollamada. Tu voz es analógica: la computadora la muestrea y la pasa a bits, los comprime, les agrega bits de control y los convierte en una señal que el cable o el aire puedan llevar. Del otro lado se deshace todo en orden inverso. Cada bloque de esa cadena es un tema de la materia.

| Bloque | Qué hace | Sección |
|---|---|---|
| **Fuente** | emite símbolos con ciertas probabilidades: información, entropía | §2 |
| **Codificador de fuente** | achica el mensaje: menos dígitos por símbolo (Kraft, Huffman) | §4 |
| **Codificador de canal** | agrega redundancia para detectar y corregir errores | §5 |
| **Modulador y multiplexor** | adapta la señal al medio y reparte el canal (AM, ASK, PCM, FDM, TDM) | §6, §7 |
| **Canal y medio** | lleva la señal; ahí aparece el ruido | §2, §8 |
| **Red** | los mensajes esperan su turno en los nodos | §9 |

**Bit y binit.** El **bit** es la unidad de **información**; el **binit** es un **dígito binario**. Un binit lleva como máximo un bit, y menos si los dígitos no son equiprobables.

**Modular** es usar el mensaje para variar un parámetro de una **portadora**, de modo que su espectro se traslade a otra zona de frecuencias. Siempre **el mensaje modula a la portadora**. Mensaje y portadora pueden ser analógicos o digitales, y con eso la cátedra arma tres casos:

| Caso | Mensaje | Portadora | Técnicas | Multiplexado |
|---|---|---|---|---|
| I | analógico | analógica | AM, FM, PM | FDM |
| II | **digital** | **analógica** | **ASK, FSK, PSK** (el módem) | FDM |
| III | analógico | digital (tren de pulsos) | PAM, PDM, PPM, **PCM** | TDM |

### 2. Teoría de la información

*Fuentes: apunte 1 (Información, Codificación y Canales), Errores en Canales y Práctica N°1 resuelta.*

#### 2.1 Información y entropía

Si te dicen "mañana sale el sol", no te enterás de nada: era seguro. Si te dicen "nieva en Rosario en enero", te enterás de muchísimo. **La información de un suceso crece cuando su probabilidad baja.** La cátedra pide que valga 0 si $p = 1$, que tienda a infinito si $p \to 0$ y que se sume para sucesos independientes. La única función que cumple las tres condiciones es el logaritmo:

$$I(A) = \log_2 \frac{1}{p(A)} \quad [\text{bit}]$$

La **entropía** $H(S)$ es la **esperanza matemática de la información por símbolo de la fuente**:

$$H(S) = \sum_i p_i \log_2 \frac{1}{p_i} \quad [\text{bit/símbolo}]$$

- Es **máxima** cuando los $q$ símbolos son **equiprobables**: $H_{max} = \log_2 q$. Vale 0 si un símbolo es seguro.
- Fuente binaria: $H(p) = p \log_2 \frac{1}{p} + (1-p) \log_2 \frac{1}{1-p}$, con máximo de 1 bit en $p = 0{,}5$.
- Ejemplos: 1/2, 1/4, 1/8, 1/8 da 1,75 bit; 0,75 / 0,25 da 0,811 bit.
- La cátedra trabaja con fuentes **de memoria nula** (cada símbolo es independiente de los anteriores).

> **Ojo:** en el *multiple choice* la correcta es "la esperanza matemática de la información por símbolo **de la fuente**", y la fórmula correcta usa $\log_2$ y $1/p_i$. Con $\ln$ da *nats*; con $\log p_i$ sin el signo da negativo.

#### 2.2 El canal y el canal binario simétrico

Un canal sin memoria queda definido por su entrada $A = \{a_i\}$, su salida $B = \{b_j\}$ y la **matriz del canal** con las probabilidades $P(b_j/a_i)$: una fila por entrada, y cada fila suma 1. Un canal **transparente** no introduce errores y su matriz es diagonal.

El **canal binario simétrico** (BSC) tiene dos entradas, dos salidas y la misma probabilidad de error $p$ en los dos sentidos: $P(b_2/a_1) = P(b_1/a_2) = p$.

$$P = \begin{pmatrix} 1-p & p \\ p & 1-p \end{pmatrix}$$

| Cuenta | Fórmula |
|---|---|
| Conjunta | $P(a_i, b_j) = P(a_i)\,P(b_j/a_i)$ |
| Salida | $P(b_j) = \sum_i P(a_i)\,P(b_j/a_i)$ |
| Hacia atrás (Bayes) | $P(a_i/b_j) = P(a_i, b_j) / P(b_j)$ |

$P(a_i)$ es la probabilidad **a priori**; $P(a_i/b_j)$, la **a posteriori**, la que tenés después de ver la salida.

> **Ojo:** la simetría es del **canal**, no de la fuente: el BSC no exige entradas equiprobables. En el *multiple choice*: "posee **dos** entradas y $P(b_1/a_2) = P(b_2/a_1)$".

#### 2.3 Las entropías del sistema

| Entropía | Nombre de la cátedra | Qué mide |
|---|---|---|
| $H(A)$ | a priori | incertidumbre de la entrada |
| $H(B)$ | de salida | incertidumbre de la salida |
| $H(A/B)$ | a posteriori, **equivocación de A respecto de B** | lo que no se sabe de la fuente después de recibir: lo que el canal "bloquea" |
| $H(B/A)$ | **entropía del canal**, equivocación de B respecto de A | lo que agrega el ruido |
| $H(A,B)$ | del sistema | información media de emitir $a_i$ y recibir $b_j$ |

Todas se calculan con la misma forma, $\sum (\text{probabilidad}) \log_2 \frac{1}{\text{probabilidad}}$. La más usada es:

$$H(B/A) = \sum_{i,j} P(a_i)\,P(b_j/a_i) \log_2 \frac{1}{P(b_j/a_i)}$$

En el BSC vale $H(p)$, sea cual sea la fuente. Para verificar *(conocimiento general)*: $H(A,B) = H(A) + H(B/A) = H(B) + H(A/B)$.

> **Ojo:** la "entropía del canal" es $H(B/A)$, no $H(A/B)$. Unas "Preguntas frecuentes" de alumnos la definen como "la probabilidad de aparición de $b_j$ cuando se envió $a_i$": eso es $P(b_j/a_i)$, una probabilidad.

#### 2.4 Información mutua y capacidad

La **información mutua** es la **información transferida desde la fuente al receptor a través del canal**: la información real que llega, en promedio. Es lo que emite la fuente menos lo que el canal bloquea:

$$I(A,B) = H(A) - H(A/B) = H(B) - H(B/A)$$

- Es **simétrica**: $I(A,B) = I(B,A)$.
- Se calcula como $H(B) - H(B/A)$, porque $H(B/A)$ sale directo de la matriz.
- Canal transparente: $I(A,B) = H(A)$. Si la fuente emite siempre lo mismo, $I = 0$.

La **capacidad** es el máximo de la información mutua sobre todas las fuentes posibles: $C = \max I(A,B)$. **Depende sólo del canal.** Canal transparente de $n$ símbolos: $C = \log_2 n$. BSC: $C = 1 - H(p)$, con entrada equiprobable *(conocimiento general)*.

| Concepto | Fórmula |
|---|---|
| Eficiencia y redundancia del canal | $FF = I(A,B)/C$; $RED = 1 - FF$ |
| Teorema del canal (Shannon) | si $R \le C$ se puede transmitir con error tan chico como se quiera; si $R > C$, no |
| Shannon–Hartley (ruido blanco) | $C = B \log_2 (1 + S/N)$ [bps] |

Ejemplo: con $B = 1000$ Hz y $S/N = 3$, $C = 1000 \cdot \log_2 4 = 2000$ bps. **El ruido limita la capacidad.**

#### 2.5 Ejercicio resuelto: el canal binario de los finales

**Enunciado** (18/12/2015, 23/10/2020, 10/09/2021, 17/12/2021). Canal binario simétrico con $P(a_1) = 0{,}65$ y $P(b_1/a_1) = 0{,}75$. Calcular a) la entropía a la salida, b) la entropía del canal y c) la información mutua, explicando el concepto.

**Datos.** $P(a_2) = 0{,}35$. El canal es simétrico, así que $p = 1 - 0{,}75 = 0{,}25$.

1. **Conjuntas:** $P(a_1,b_1) = 0{,}4875$; $P(a_1,b_2) = 0{,}1625$; $P(a_2,b_1) = 0{,}0875$; $P(a_2,b_2) = 0{,}2625$.
2. **Salidas:** $P(b_1) = 0{,}4875 + 0{,}0875 = 0{,}575$; $P(b_2) = 0{,}425$.
3. **a)** $H(B) = 0{,}575 \log_2 \frac{1}{0{,}575} + 0{,}425 \log_2 \frac{1}{0{,}425} = 0{,}4591 + 0{,}5246 =$ **0,9837 bit/símbolo**.
4. **b)** $H(B/A) = 0{,}75 \log_2 \frac{1}{0{,}75} + 0{,}25 \log_2 4 = 0{,}3113 + 0{,}5 =$ **0,8113 bit/símbolo**. Es $H(0{,}25)$: no depende de la fuente.
5. **c)** $I(A,B) = 0{,}9837 - 0{,}8113 =$ **0,1724 bit/símbolo**.
6. **Concepto.** La fuente emite $H(A) = 0{,}934$ bit por símbolo, pero al receptor llegan en promedio 0,172. El resto lo tapa el ruido, que invierte uno de cada cuatro símbolos.
7. **Verificación.** Con Bayes, $H(A/B) = 0{,}7616$ y $H(A) - H(A/B) = 0{,}1725$ ✓.

Extra *(conocimiento general)*: $C = 1 - 0{,}8113 = 0{,}1887$ bit/símbolo y $FF = 0{,}914$.

> **Ojo:** $H(B/A)$ se pondera con $P(a_i)$; sin los pesos da $2H(p)$. $I(A,B)$ nunca es negativa. Y la Práctica N°1 resuelta calcula $H(A,B)$ **sumando probabilidades**: está mal, hay que sumar $p \log_2 (1/p)$.

#### 2.6 Las velocidades: R, r y s

| Magnitud | Definición de la cátedra | Fórmula | Unidad |
|---|---|---|---|
| **Tasa de información** $R$ | información **promedio** que produce la fuente **por unidad de tiempo** | $R = r \cdot H$ | bps |
| **Tasa de dígitos** $r$ | **dígitos transmitidos por segundo**, informen o no | $r = N/T$ | dígitos/s |
| **Velocidad de señalización** $s$ | inversa de la duración del pulso **más corto** | $s = 1/\tau_{min}$ | baudios |

Ejemplo: pulsos de 1 ms con 4 niveles equiprobables dan $s = 1000$ baudios, $r = 1000$ dígitos/s y, como cada dígito lleva $\log_2 4 = 2$ bit, $R = 2000$ bps. Con pulsos **binarios** equiprobables, $R = s$: la capacidad coincide con la velocidad de señalización, y el ancho de banda mínimo es $B = s/2$.

> **Ojo:** $R = r \cdot H$, o sea $r = R/H$. Un resumen de alumnos escribe "$r = H(A)/R$": está mal. En el *multiple choice*, la tasa de información lleva la palabra "**promedio**".

## Preguntas reales de teoría de los finales, con su respuesta

### 1. Teoría de la información

#### 1.1 Entropía de la fuente: concepto, fórmula, cuándo es máxima
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

#### 1.2 Tasa de información, tasa de dígitos y velocidad de señalización
**Salió:** tasa de información en 18/12/2020, 19/11/2021 y 17/12/2021 (MC); tasa de dígitos en 28/08/2020 y 10/09/2021 (MC); FAQ "Concepto de entropía, tasa de información, tasa de dígitos y velocidad de señalización. Dar ejemplos".

**Respuesta.**
- **Tasa (velocidad) de información $R$:** cantidad de bits **en promedio** que se transmiten en 1 segundo, es decir, la información **promedio** que produce la fuente **por unidad de tiempo**. $R = H'(A)$ [bit/s]. Con canal ruidoso, a la salida llega $R = H'(A) - H'(A/B)$.
- **Tasa de dígitos (binits) $r$:** cantidad de **dígitos transmitidos por segundo** [dígitos/s]. Se relaciona con la anterior por $R = r\cdot H(A)$: $H$ mide información en bit/símbolo, $R$ en bit/s.
- **Velocidad de señalización $s$:** inversa de la duración del pulso más corto, $s = 1/\tau_{min}$ [baudios]. Con pulsos de $n$ niveles equiprobables e iguales duraciones: $R = \frac{1}{\tau}\lg n = s\,\lg n$.

**Ejemplo:** pulsos de $\tau = 1$ ms con 4 niveles equiprobables → $s = 1000$ baudios, $r = 1000$ dígitos/s, $H = \lg 4 = 2$ bit/dígito, $R = r\,H = 2000$ bit/s. Si los pulsos fueran binarios, $R = s = 1000$ bit/s: en binario equiprobable **la capacidad coincide con la señalización**.

**En el MC:** tasa de información = "la información **promedio** que emite la fuente **por unidad de tiempo**" (la que dice "la información que emite…" sin "promedio" no es la definición). Tasa de dígitos = "la cantidad de dígitos transmitidos por segundo" (no son "dígitos de información" ni "dígitos de señalización").

(teoria/1 - Información, Codificación y Canales.md)

#### 1.3 Canal binario simétrico (BSC)
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

#### 1.4 Información mutua, entropía del canal (canal real)
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

### 2. Errores de canal

#### 2.1 Efecto del ruido de canal y sus causas; ruido impulsivo
**Salió:** FAQ ("¿Qué efecto produce el ruido de canal? Nombre tres causas", "Ruido impulsivo: definirlo y explicar sus fuentes", "Causas de errores de canal").

**Respuesta.** El ruido **limita la capacidad del canal** para transmitir información e introduce errores cuando cae en la banda de la señal. Por Hartley-Shannon, $C = B\,\lg(1+S/N)$ [bit/s]: a igual ancho de banda, más ruido implica menos capacidad.

- **Ruido blanco:** se debe a la agitación térmica de átomos y moléculas. Es aleatorio y **no se puede eliminar**.
- **Causas de error de canal:**
  1. **Ruido impulsivo** (la principal): picos grandes de amplitud sobre el ruido blanco que saturan el canal y alteran **varios binits seguidos (ráfaga)**. Causas **externas**: acoplamientos capacitivos o inductivos por canales paralelos, conmutación mecánica, señales de supervisión y fenómenos atmosféricos. Causas **internas**: variaciones de impedancia en conexiones, sobrecarga de amplificadores y armónicas espurias generadas por filtros. Se contrarresta con módems adecuados.
  2. **Modulaciones espurias:** **cruzada** (captación de otros canales por acoplamiento), **intermodulación** (alinealidad de amplificadores en canales multiplex; se corrige con módems o bajando la amplitud) y **eco** (reflexiones por variación de impedancia; se usan supresores de eco).
  3. **Variaciones de nivel (desvanecimiento):** variaciones de impedancia, fallas de contactos o de amplificadores, lluvia en microondas.
  4. **Distorsión** que introduce el propio canal: atenuación, distorsión fase/frecuencia, variación de la frecuencia de la portadora y variación del nivel de muestreo. Es sistemática, así que se corrige por diseño.

(teoria/Errores en Canales.md)
