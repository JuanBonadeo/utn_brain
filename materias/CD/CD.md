# Comunicación de Datos — Wiki

> Materia de 3° (pendiente: se rinde el final). En los finales viejos aparece como "Comunicaciones".
>
> **Cursada 2025, comisión 303** (`fuentes/cursada-2025/`, mails de la cátedra). Responsable de cátedra: **Ing. Jorge A. Campanaro**. En la 303 dieron teoría **Ing. Cristian Medín** y práctica **Ing. Germán Baró**. Sin aprobación directa: los parciales no llegaron a 6, así que va a final como regular (si los informes quedaron aprobados).
> - **Condiciones (presentación 2025):** la aprobación directa pedía los 5 informes aprobados y 4 parciales con 6 o más, con un recuperatorio por parte. Para la aprobación no directa (regular) bastaba con presentar y aprobar el 100 % de los informes. El "examen globalizador" de las mesas de diciembre, con recuperatorio en marzo, se tomaba **sobre el 100 % de los informes**. ⚠️ Confirmar con la cátedra qué formato tiene hoy el final para regulares: el del 04/04/2025 tiene la forma de abajo.
> - **Informes de teoría 2025:** (1) codificación y códigos lineales; (2) códigos correctores de error: **cíclicos y convolucionales**; (3) teoría de colas y asignación de capacidad; (4) IoT; (5) seguridad en la transmisión de datos. Práctica: una monografía con tema de la lista de Baró.
> - **Lo que se tomó en los parciales 2025:** el 1er parcial de práctica (Baró, fin de junio) entró con *Principios básicos E & Cx*, *Medios de transmisión*, *Práctica Transmisión Multinivel* y *Velocidades de transmisión – Capacidad de un canal – Multinivel*. El 2do parcial de teoría (Medín, 23/10) entró con elección del medio de acceso, asignación de capacidad, OSI/TCP‑IP y teoría de colas. Antes del 2do parcial, Medín mandó ejercicios de colas y de asignación de capacidad.
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
8. Unidad 8 — Códigos correctores de error: códigos cíclicos y convolucionales  📌 *(informe 2 de la cursada 2025)*
9. Unidad 9 — Internet de las cosas (IoT) y seguridad en la transmisión de datos  📌 *(informes 4 y 5 de la cursada 2025)*

**Cómo está armada cada unidad:** Conceptos clave → Desarrollo → Ejercicios resueltos tipo → Dudas / pendientes → Fuentes.

## Desarrollo

### Unidad 1 — Teoría de la información: información, entropía, canales

#### Conceptos clave
- **Cantidad de información** de un suceso A: $I_{(A)} = \lg \frac{1}{p_{(A)}} = -\lg p_{(A)}$ [bit]. $\lg$ = log en base 2. **bit** = unidad de información; **binit** = dígito binario (no son lo mismo).
- Calculadora: $\lg N = \frac{\log N}{\log 2} \approx 3{,}32 \log N = \frac{\ln N}{\ln 2}$.
- **Entropía de la fuente**: esperanza matemática de la información por símbolo, $H(S) = \sum_i p_i \lg \frac{1}{p_i}$ [bit/símbolo]. Máxima si los símbolos son equiprobables: $H_{max} = \lg n$.
- **Canal**: alfabeto de entrada A = (aᵢ), de salida B = (bⱼ) y matriz de probabilidades condicionales $P_{ij} = P(b_j/a_i)$ (fila = entrada, columna = salida). **Transparente**: no introduce error, matriz diagonal. **Binario simétrico (BSC)**: dos entradas, dos salidas, $P(b_2/a_1) = P(b_1/a_2) = p$ (probabilidad de error).
- Salida: $P(b_j) = \sum_i P(a_i)\,P(b_j/a_i)$. Hacia atrás (Bayes): $P(a_i/b_j) = \frac{P(a_i)\,P(b_j/a_i)}{P(b_j)}$.
- **H(A)** entropía a priori · **H(A/B)** entropía a posteriori o equivocación de A respecto de B · **H(B/A)** entropía del canal o equivocación de B respecto de A · **H(A,B)** entropía del sistema.
- **Información mutua**: información real que llega al receptor en promedio. $I(A,B) = H(A) - H(A/B) = H(B) - H(B/A)$ (simétrica).
- **Capacidad**: $C = \max I(A,B)$, maximizando sobre las probabilidades de entrada ("sintonizando la fuente"). Depende sólo del canal. Transparente + equiprobable: $C = \lg n$.
- **Eficiencia** del canal $FF = I(A,B)/C$; **redundancia** $RED = 1 - FF$.
- **R** tasa de información [bit/s] · **r** tasa de dígitos [binit/s o dígitos/s] · **s** velocidad de señalización $= 1/\tau_{min}$ [baudios]. $R = r\,H(A)$.
- **M(T)** mensajes distintos en T: $M(T) = \mu^n$ (μ niveles, n pulsos de información). $I = \lg M(T)$, $R = I/T$. Si todos los pulsos son de información y duran τ: $R = \frac{1}{\tau}\lg\mu$.
- Binario equiprobable: $C = s$; ancho de banda $B = s/2$.
- **Teorema del canal**: si $R \le C$ existe una codificación con error arbitrariamente pequeño; si $R > C$, no.
- **Shannon–Hartley** (canal con ruido blanco): $C = B \lg(1 + S/N)$ [bps].

#### Desarrollo

##### Cantidad de información
Ejemplo primero: si sé que mañana sale el sol (p = 1), el anuncio no me informa nada; si me anuncian nieve en Rosario en enero (p ≈ 0), me informa muchísimo. La información es función inversa de la probabilidad, y la cátedra exige tres condiciones:
1. $p_{(A)} = 1 \Rightarrow I_{(A)} = 0$.
2. $p_{(A)} \to 0 \Rightarrow I_{(A)} \to \infty$.
3. A y B independientes: $p_{(A \cdot B)} = p_{(A)}\,p_{(B)}$ y $I_{(A\cdot B)} = I_{(A)} + I_{(B)}$.

La única función que vale 0 en 1, tiende a ∞ en 0 y convierte productos en sumas es el logaritmo; se usa base 2 porque se trabaja con mensajes binarios:
$$I_{(A)} = \lg \frac{1}{p_{(A)}} \quad [\text{bit}]$$

##### Entropía de la fuente (modelo univariado)
El modelo univariado describe una fuente (o un receptor) por sus símbolos xᵢ y sus probabilidades. La cátedra trabaja con fuentes **ergódicas** (probabilidades independientes del tiempo) y **de memoria nula** (cada símbolo independiente de los anteriores).

Ejemplo de la cátedra: fuente S con símbolos R, A, V y una muestra significativa `…R R A A A V A A R R…`. La información promedio es $\frac{N_A I_A + N_V I_V + N_R I_R}{N}$. Como $N_i/N$ es la frecuencia relativa y en una **muestra significativa** la frecuencia relativa se toma como probabilidad:
$$H(S) = \sum_i p_i \lg\frac{1}{p_i} = -\sum_i p_i \lg p_i \quad [\text{bit/símbolo}]$$

Propiedad: para un número dado de símbolos, H es máxima cuando son equiprobables. Fuente binaria con probabilidades p y 1−p: $H(p) = -p\lg p - (1-p)\lg(1-p)$, vale 0 en p = 0 o 1 y es máxima (1 bit) en p = 0,5.

| Fuente | H [bit/símb] |
|---|---|
| Muestra binaria 13 ceros / 17 unos de 30 | 0,987 |
| Moneda cargada, p(cara) = 2/3 | 0,918 |
| x₁, x₂, x₃ con 0,2 / 0,5 / 0,3 | 1,486 |
| 1/2, 1/4, 1/8, 1/16, 1/16 | 1,875 |

##### El canal (modelo bivariado)
Esquema: FUENTE → (aᵢ) → CANAL, con RUIDO que actúa sobre P(bⱼ/aᵢ) → (bⱼ) → RECEPTOR.

Un canal sin memoria queda definido por la matriz
$$P = \begin{pmatrix} P(b_1/a_1) & \cdots & P(b_s/a_1)\\ \vdots & & \vdots \\ P(b_1/a_r) & \cdots & P(b_s/a_r)\end{pmatrix}$$
Cada fila suma 1. Para el BSC:
$$P = \begin{pmatrix} 1-p & p \\ p & 1-p \end{pmatrix}$$

Con las probabilidades de entrada y la matriz se obtienen las de salida $P(b_j)$. **Al revés no**: conociendo las salidas y la matriz, en general no se pueden calcular las entradas. Las probabilidades **hacia atrás** $P(a_i/b_j)$ salen de Bayes, a partir de la conjunta:
$$P(a_i, b_j) = P(a_i)\,P(b_j/a_i) = P(b_j)\,P(a_i/b_j)$$

$P(a_i)$ es la probabilidad **a priori**; $P(a_i/b_j)$, la **a posteriori** (después de ver bⱼ).

##### Las entropías del sistema
| Nombre | Fórmula | Qué mide |
|---|---|---|
| A priori | $H(A) = \sum_i P(a_i)\lg\frac{1}{P(a_i)}$ | incertidumbre de la entrada |
| Salida | $H(B) = \sum_j P(b_j)\lg\frac{1}{P(b_j)}$ | incertidumbre de la salida |
| A posteriori / equivocación de A resp. de B | $H(A/B) = -\sum_j P(b_j)\sum_i P(a_i/b_j)\lg P(a_i/b_j)$ | lo que sigue sin saberse de la fuente después de recibir; la información que "bloquea" el canal |
| Del canal / equivocación de B resp. de A | $H(B/A) = -\sum_i P(a_i)\sum_j P(b_j/a_i)\lg P(b_j/a_i)$ | lo que introduce el canal (ruido) |
| Del sistema | $H(A,B) = -\sum_{i,j} P(a_i,b_j)\lg P(a_i,b_j)$ | información media al emitir aᵢ y recibir bⱼ |

Relación útil para verificar (conocimiento general): $H(A,B) = H(A) + H(B/A) = H(B) + H(A/B)$.

##### Información mutua
Es la información transferida desde la fuente al receptor a través del canal: la entropía a priori menos lo que el canal bloquea.
$$I(A,B) = H(A) - H(A/B) = H(B) - H(B/A) = \sum_i\sum_j P(a_i,b_j)\lg\frac{P(a_i,b_j)}{P(a_i)\,P(b_j)}$$
- Es simétrica: $I(A,B) = I(B,A)$.
- En la práctica se calcula por $H(B) - H(B/A)$, porque H(B/A) sale directo de la matriz del canal.
- Canal transparente: $H(A/B) = H(B/A) = 0$ y $H(A) = H(B) = H(A,B) = I(A,B)$.
- Mínimo: 0 (basta con que un símbolo de entrada tenga probabilidad 1).

##### Capacidad y eficiencia
I(A,B) depende de la fuente y del canal. Su máximo, variando las probabilidades de entrada, es la **capacidad**: $C = \max I(A,B)$. Es función exclusiva de las probabilidades condicionales.
- Canal transparente: $C = \max H(A) = \lg n$ (fuente equiprobable). Binario: C = 1 bit/símbolo. Si cada símbolo dura τ: $C = 1/\tau$ bps.
- BSC con probabilidad de error p (conocimiento general; el apunte no da la fórmula cerrada): $C = 1 - H(p)$ bit/símbolo, alcanzada con entrada equiprobable.
- Eficiencia de transmisión $FF = I(A,B)/C$; redundancia $RED = 1 - FF$ (parte no aprovechada de la capacidad).

##### Velocidades: R, r, s y M(T)
- **R (tasa de información)**: información promedio que produce la fuente en 1 s. $R = H'(A)$; con ruido, a la salida $R = H'(A) - H'(A/B)$ (H' = entropía por segundo). $R = r\,H(A)$.
- **r (tasa de dígitos)**: dígitos transmitidos por segundo, informen o no (incluye arranque y parada).
- **s (velocidad de señalización)**: $s = 1/\tau_{min}$ [baudios]; supone que todos los pulsos duran lo que el más corto.

Mensajes de pulsos: en T segundos con n pulsos de μ niveles hay arreglos con repetición, $M(T) = \mu^n$. Si son equiprobables, $P(M) = 1/M(T)$ e $I = \lg M(T)$ (no hace falta calcular la entropía: coincide con I). Entonces $R = I/T$.
- Si todos los pulsos son de información y de igual duración, $n = T/\tau$ y $R = \frac{1}{\tau}\lg\mu$.
- Pulsos de arranque/parada: suman a T y a r, **no** a la información (valor fijo).
- Varios bloques: los mensajes se multiplican y las informaciones se suman, $M = M_1 M_2$, $I = \lg M_1 + \lg M_2$.
- Para duplicar R sin tocar los tiempos, sólo queda subir niveles: se plantea $I' = 2R\,T$, se despeja μ y se **redondea para arriba**.

Equiprobable, binario y $\tau = \tau_{min}$: R es máximo, $C = R_{max} = s$; el ancho de banda es $B = s/2$.

##### Errores de canal (apunte "Errores en Canales")
- **Ruido blanco**: agitación molecular y atómica por temperatura. Aleatorio, imposible de eliminar; limita la capacidad. Su amplitud sigue una curva normal.
- **Ancho de banda**: $B = f_2 - f_1$, frecuencias de corte donde la ganancia cae 3 dB respecto de las frecuencias medias. Si f₁ es chica, B ≈ f₂.
- **Capacidad con ruido (Hartley–Shannon)**: con potencia de ruido N y señal de potencia S (distribución normal):
$$H(Y/X) = B\lg(2\pi e N),\quad H(Y) = B\lg(2\pi e (N+S)),\quad C = H(Y) - H(Y/X) = B\lg\left(1+\frac{S}{N}\right)\ [\text{bps}]$$
  Ej.: B = 1000 Hz, S/N = 3 → C = 1000·lg 4 = 2000 bps.
- **Causas de error de canal**:
  - *Ruido impulsivo*: la principal fuente de error. Picos que saturan el canal y afectan varios binits (**ráfaga**). Externas: acoplamientos capacitivos/inductivos (canales paralelos, conmutación mecánica, señales de supervisión, fenómenos atmosféricos). Internas: variaciones de impedancia en conexiones, sobrecarga de amplificadores, armónicas espurias de filtros. Se combate con módems adecuados.
  - *Modulaciones espurias*: modulación cruzada (captación de otros canales por acoplamiento), intermodulación (no linealidad de amplificadores en canales multiplex; señales repetitivas como discado y supervisión), eco (reflexiones por variación de impedancia; supresores de eco).
  - *Variaciones de nivel (desvanecimiento)*: impedancia, fallas en contactos o amplificadores, lluvia en microondas.
  - *Distorsión*: atenuación (varía con la frecuencia; se corrige con ecualizadores), fase/frecuencia (retardos distintos por frecuencia, desfasa armónicas), variación de frecuencia de la portadora (sub-portadora de sincronismo), variación del nivel de umbral de muestreo (alarga o acorta pulsos). Ventaja: es sistemática, se corrige por diseño.

#### Ejercicios resueltos tipo

**Ejercicio 1 (finales 2015-12-18, 2020-10-23, 2021-09-10, 2021-12-17).** Canal binario simétrico con P(a₁) = 0,65 y P(b₁/a₁) = 0,75. Calcular a) la entropía a la salida, b) la entropía del canal H(B/A), c) la información mutua y explicar el concepto.

1. Datos: P(a₂) = 0,35. Como es simétrico, la probabilidad de error es p = 1 − 0,75 = 0,25:
$$P = \begin{pmatrix} 0{,}75 & 0{,}25 \\ 0{,}25 & 0{,}75\end{pmatrix}$$
2. Conjuntas $P(a_i,b_j) = P(a_i)P(b_j/a_i)$: P(a₁,b₁) = 0,4875; P(a₁,b₂) = 0,1625; P(a₂,b₁) = 0,0875; P(a₂,b₂) = 0,2625.
3. Salida: P(b₁) = 0,4875 + 0,0875 = **0,575**; P(b₂) = 0,1625 + 0,2625 = **0,425**.
4. a) $H(B) = 0{,}575\lg\frac{1}{0{,}575} + 0{,}425\lg\frac{1}{0{,}425} = 0{,}4591 + 0{,}5246 = $ **0,9837 bit/símb**. Es la incertidumbre (información media) de lo que se observa a la salida.
5. b) $H(B/A) = \sum_i P(a_i)\left[0{,}75\lg\frac{1}{0{,}75} + 0{,}25\lg 4\right] = (0{,}65+0{,}35)(0{,}3113 + 0{,}5) = $ **0,8113 bit/símb**. En un BSC no depende de la fuente: es H(p).
6. c) $I(A,B) = H(B) - H(B/A) = 0{,}9837 - 0{,}8113 = $ **0,1724 bit/símb**: de los H(A) = 0,9341 bit que emite la fuente, en promedio llegan 0,17 bit por símbolo; el resto lo bloquea el ruido.
7. Verificación por el otro lado: a posteriori P(a₁/b₁) = 0,8478, P(a₂/b₁) = 0,1522, P(a₁/b₂) = 0,3824, P(a₂/b₂) = 0,6176 → H(A/B) = 0,7616 y H(A) − H(A/B) = 0,1725 ✓ (redondeo). H(A,B) = 1,7453 = H(A) + H(B/A) ✓.
8. Extra (conocimiento general): C = 1 − H(0,25) = 0,1887 bit/símb → FF = 0,1724/0,1887 = 0,914.

**Ejercicio 2 (final 2021-09-10).** 1 pulso de arranque fijo de 5 V, 10 pulsos de datos de 128 niveles y 1 pulso de stop fijo. Todos duran 5 ms salvo el stop, de 7 ms. Calcular M(T), I, R, r y s.

1. Sólo informan los 10 pulsos de datos: $M(T) = 128^{10} = 2^{70}$ mensajes.
2. $I = \lg 2^{70} = 10\lg 128 = $ **70 bits**.
3. T = 5 ms (arranque) + 10·5 ms + 7 ms (stop) = **62 ms**.
4. R = 70 / 0,062 s = **1129 bps**.
5. r = 12 dígitos / 0,062 s = **193,5 dígitos/s** (cuentan arranque y stop).
6. s = 1/τ_min = 1/5 ms = **200 baudios**.

**Ejercicio 3 (práctica N°1, ej. de fuente de 3 símbolos + canal).** Fuente x₁, x₂, x₃ con 0,2 / 0,5 / 0,3 conectada a un canal ternario con matriz (reconstruida de la resolución, ver Dudas)
$$P = \begin{pmatrix} 0{,}5 & 0 & 0{,}5 \\ 0 & 0{,}6 & 0{,}4 \\ 0{,}2 & 0 & 0{,}8\end{pmatrix}$$
1. Conjuntas no nulas: 0,1; 0,1; 0,3; 0,2; 0,06; 0,24 → $H(A,B) = $ **2,387 bit**.
2. $H(B/A) = 0{,}1\cdot1 + 0{,}1\cdot1 + 0{,}3\lg\frac{1}{0{,}6} + 0{,}2\lg\frac{1}{0{,}4} + 0{,}06\lg 5 + 0{,}24\lg\frac{1}{0{,}8} = 0{,}1+0{,}1+0{,}221+0{,}264+0{,}139+0{,}077 = $ **0,902 bit**.
3. Salida: P(y₁) = 0,16; P(y₂) = 0,30; P(y₃) = 0,54 → H(B) = 0,423 + 0,521 + 0,480 = **1,424 bit**.
4. $I(A,B) = 1{,}424 - 0{,}902 = $ **0,522 bit/símb**. Verificación: H(A) = 1,486 y H(A,B) = H(A) + H(B/A) = 2,388 ✓.

#### Dudas / pendientes
- **Error en la práctica resuelta** (`Práctica N°1 … RESUELTO`): para el BSC con P = 0,8 y fuente 0,45/0,55 obtiene H(A,B) = 0,36 + 0,09 + 0,11 + 0,44 = 1 bit: suma las probabilidades conjuntas en vez de $-p\lg p$. El valor correcto es **H(A,B) = 1,7147 bit** (verificado; = H(A) 0,9928 + H(B/A) 0,7219).
- **Fuente telegráfica de la práctica resuelta** (punto 2/3 con 0,2 s, raya 1/3 con 0,4 s): la resolución hace R = H/(0,2 + 0,4) = 0,918/0,6 = 1,53 bps. La duración media por símbolo es $\bar\tau = \sum p_i\tau_i = 0{,}2667$ s, de modo que **R = H/τ̄ = 3,44 bps** (conocimiento general; el apunte no trata pulsos de distinta duración y probabilidad). Consultar qué criterio acepta la cátedra.
- **Preguntas frecuentes (Parte 1)** tiene dos errores: define la entropía del canal como "la probabilidad de aparición de bⱼ…" (es una entropía, no una probabilidad: la equivocación de B respecto de A) y escribe "r = H(A)/R" (lo correcto, según el apunte, es R = r·H(A), o sea r = R/H(A)).
- **"Errores en Canales"** está mal impreso en la capacidad con ruido: se pierde π en $\lg(2\pi e N)$, dice "distribución mal" (normal) y "C = H(Y) = H(Y/X)" (es la resta). El Santo Resumen hace la misma corrección.
- **Decibeles**: "Errores en Canales" usa 10 log G también para relaciones de amplitud; para tensión/corriente con igual impedancia corresponde 20 log (lo señala el Santo Resumen citando "Principios Básicos"). Para el final, 10 log para potencias y 20 log para amplitudes.
- El apunte imprime "S R > C" (falta la "i"): es "Si R > C no es posible transmitir sin error".
- La matriz del canal ternario del Ejercicio 3 y las del resto de la práctica eran imágenes que se perdieron en la conversión; la del Ej. 3 la reconstruí con los productos que muestra la resolución (verificada: todos los resultados cierran).
- Agregado de conocimiento general: $C_{BSC} = 1 - H(p)$, la relación H(A,B) = H(A) + H(B/A) y el criterio τ̄ para R. En el final 2020-02-21 el enunciado dice p(a₁) = 0,05: probablemente es un error de tipeo por 0,65, que se repite en los otros finales.

#### Fuentes
- `fuentes/teoria/1 - Información, Codificación y Canales.md` (+ `.pdf`)
- `fuentes/teoria/Errores en Canales.md`
- `fuentes/practica/Práctica N°1 -Teoría de la Información-RESUELTO.md`
- `fuentes/practica/Ejercitación Teoría de la Información.md`
- `fuentes/resumenes/Para rendir el final/Práctica - Fórmulas y pasos para los ejercicios.md`
- `fuentes/resumenes/Para rendir el final/Resumen.md`
- `fuentes/resumenes/Para rendir el final/Teoría - Preguntas frecuentes (Parte 1).md` y `(Parte 2).md`
- `fuentes/resumenes/1° Parcial/Resumen 1° Parcial Teoría (Parte 1).md`
- `fuentes/resumenes/El Santo Resumen/el-santo-resumen.md` (secciones "Información, entropía y canal", "Capacidad con ruido" y "Transmisión multinivel")
- Finales: `fuentes/finales/Práctica/2015/…2015-12-18.md`, `…/2020/…2020-10-23.md`, `…/2021/…2021-09-10.md`, `…/2021/…2021-12-17.md`; teoría: `fuentes/finales/Teoría/2020/*.md`, `fuentes/finales/Teoría/2021/*.md`

### Unidad 2 — Codificación: códigos unívocos, instantáneos, Kraft, compactos

#### Conceptos clave
- **Codificación**: correspondencia entre secuencias del **alfabeto fuente** S = (s₁ … s_q) y secuencias del **alfabeto código** Z = (z₁ … z_r) (r = cantidad de símbolos código; binario r = 2).
- **Código bloque**: asigna a cada símbolo del alfabeto fuente una secuencia **fija** de símbolos del alfabeto código. Esa secuencia es la **palabra código**.
- **No singular**: todas sus palabras son distintas.
- **Unívoco** (unívocamente decodificable): a cualquier secuencia de palabras código le corresponde una y sólo una secuencia de símbolos fuente. Equivalente: su extensión de orden n es no singular para todo n finito.
- **Instantáneo**: se decodifica cada palabra sin esperar los símbolos siguientes. Condición **necesaria y suficiente**: ninguna palabra es prefijo de otra.
- Jerarquía: instantáneo ⊂ unívoco ⊂ no singular ⊂ bloque.
- **Inecuación de Kraft**: $\sum_{i=1}^{q} r^{-l_i} \le 1$ es condición necesaria y suficiente para que **exista al menos un** código instantáneo con esas longitudes. Un código que la cumple **puede ser** instantáneo (no necesariamente lo es).
- **McMillan**: la misma inecuación es condición necesaria y suficiente para la existencia de un código unívoco.
- **Longitud media**: $L = \sum_i P_i\, l_i$ [binit/símbolo].
- **Compacto**: código instantáneo cuya longitud media es igual o menor que la de todos los códigos instantáneos aplicables a la misma fuente y el mismo alfabeto.
- **Cota inferior**: $L \ge \frac{H(S)}{\lg r} = H_r(S)$ (entropía en unidades r-arias). Igualdad sii $P_i = r^{-l_i}$ (probabilidades potencias de 1/r).
- **Primer teorema de Shannon** (codificación sin ruido): $H_r(S) \le \frac{L_n}{n} < H_r(S) + \frac{1}{n}$ para la extensión de orden n; $\lim_{n\to\infty} L_n/n = H_r(S)$.
- **Huffman**: construye códigos compactos. r-ario: la cantidad de símbolos ω debe cumplir $\omega = r + \alpha(r-1)$ con α entero; si no, se agregan **símbolos falsos** de probabilidad 0.
- **Rendimiento** $\eta = H_r(S)/L$; **redundancia** $1 - \eta = \frac{L - H_r(S)}{L}$.

#### Desarrollo

##### Familia de códigos, con ejemplos
| Código | S₁ | S₂ | S₃ | S₄ | Qué es |
|---|---|---|---|---|---|
| Singular | 0 | 11 | 0 | 01 | dos palabras iguales |
| No singular, no unívoco | 1 | 11 | 00 | 10 | `1100` puede ser S₂S₃ o S₁S₁S₃ |
| Unívoco, no instantáneo (A, código "coma") | 0 | 01 | 011 | 0111 | al recibir `01` hay que esperar: si sigue 0 era S₂, si sigue 1 hay que seguir esperando |
| Instantáneo (B) | 1 | 01 | 001 | 0001 | ninguna palabra es prefijo de otra |
| Instantáneo (longitud constante) | 00 | 01 | 10 | 11 | todo código no singular de longitud constante es unívoco |

Los códigos "coma" señalan el comienzo (A: cada palabra empieza con 0) o el fin (B: cada palabra termina en 1) de cada palabra. Ambos son unívocos; sólo B es instantáneo.

**Prefijo**: de la palabra $Z_i = z_{i1} z_{i2}\ldots z_{im}$ es cualquier secuencia $z_{i1}\ldots z_{ij}$ con j ≤ m.

##### Inecuación de Kraft y McMillan
$$\sum_{i=1}^{q} r^{-l_i} \le 1$$
Si los enteros l₁ … l_q la cumplen, existe al menos un código instantáneo r-ario con esas longitudes; y todo código instantáneo la cumple. **El teorema habla de longitudes, no de un código concreto.**

Ejemplo de la cátedra: S₁ = 0, S₂ = 00, S₃ = 11 → $2^{-1}+2^{-2}+2^{-2} = 1$, cumple Kraft, pero no es instantáneo (0 es prefijo de 00). Con las mismas longitudes 1, 2, 2 sí existe uno instantáneo: 0, 10, 11.

Más casos: longitudes (1, 2, 2, 3) binarias → 1/2 + 1/4 + 1/4 + 1/8 = 9/8 > 1 → no existe ningún código instantáneo (ni unívoco, por McMillan) con esas longitudes.

Como los instantáneos son una subclase de los unívocos, la misma suma ≤ 1 alcanza para que exista un unívoco (suficiente); McMillan demostró que también es necesaria. Consecuencia práctica: pasar de instantáneo a unívoco no permite acortar las longitudes.

##### Longitud media y cota inferior
Ejemplo: muestra `a b c a a c b b a b a a c c a a a b` (18 eventos, a aparece 9 veces → f(a) = 1/2). Si se codifica cada evento con palabras de longitud l_a, l_b, l_c, la longitud total de la muestra es $L_M = l_a N_a + l_b N_b + l_c N_c$ y la longitud promedio por evento es $L_M / TM = f_a l_a + f_b l_b + f_c l_c$. En una muestra significativa f = P:
$$L = \sum_i P_i\, l_i$$
Para minimizar L: **a mayor probabilidad, menor longitud**. Si la fuente es equiprobable, las longitudes no dependen de las probabilidades.

**Teorema (cota inferior)**: $\frac{H(S)}{\lg r} \le L$, o sea $H_r(S) \le L$.

Esquema de la demostración del apunte:
1. Se usa $\ln z \le z - 1$ (igualdad sólo en z = 1).
2. Para dos distribuciones $P_i$ y $Q_i$ (ambas suman 1): $\sum_i P_i \lg\frac{Q_i}{P_i} \le 0$, o sea $H(S) \le \sum_i P_i\lg\frac{1}{Q_i}$, con igualdad sii $Q_i = P_i$.
3. Se elige $Q_i = \frac{r^{-l_i}}{\sum_j r^{-l_j}}$. Queda $H(S) \le L\lg r + \lg\sum_j r^{-l_j}$.
4. Si el código es instantáneo, por Kraft $\sum_j r^{-l_j} \le 1$ → el logaritmo es ≤ 0 → $H(S) \le L\lg r$.

La igualdad exige $\sum r^{-l_j} = 1$ y $P_i = r^{-l_i}$, es decir $l_i = \log_r\frac{1}{P_i}$ entero. Ejemplo de la cátedra: P = 1/2, 1/8, 1/8, 1/8, 1/8 con código 0, 101, 100, 111, 110:
$L = \frac12\cdot1 + 4\cdot\frac18\cdot3 = 2$ binit/símb y $H = \frac12\lg2 + 4\cdot\frac18\lg8 = \frac12 + \frac32 = 2$ bit → L = H_r(S): instantáneo y de longitud mínima, por lo tanto **compacto**.

##### Primer teorema de Shannon
Si $\log_r(1/P_i)$ no es entero, se elige el entero inmediato superior:
$$\log_r\frac{1}{P_i} \le l_i < \log_r\frac{1}{P_i} + 1$$
1. Estas longitudes cumplen Kraft: $r^{-l_i} \le P_i$ → $\sum r^{-l_i} \le \sum P_i = 1$ → existe un código instantáneo.
2. Multiplicando por $P_i$ y sumando: $H_r(S) \le L < H_r(S) + 1$.
3. Aplicado a la **extensión de orden n** (los símbolos se codifican de a n; $H_r(S^n) = n\,H_r(S)$ para memoria nula): $n H_r(S) \le L_n < n H_r(S) + 1$; dividiendo por n:
$$H_r(S) \le \frac{L_n}{n} < H_r(S) + \frac{1}{n} \qquad \lim_{n\to\infty}\frac{L_n}{n} = H_r(S)$$
$L_n/n$ es el número medio de símbolos código por símbolo de S cuando se codifica en grupos de n. Se puede acercar a la entropía tanto como se quiera, nunca bajar de ella. Costo: hay $q^n$ símbolos que codificar (complejidad).

Ejemplo (armado para la wiki, verificado): fuente binaria 0,7 / 0,3, H = 0,881 bit.
- n = 1: cualquier código binario necesita 1 binit por símbolo → L = 1; η = 0,881.
- n = 2: símbolos 0,49 / 0,21 / 0,21 / 0,09; Huffman da longitudes 1, 2, 3, 3 → L₂ = 1,81 → L₂/2 = 0,905; η = 0,974.

##### Método de Huffman (binario)
**Paso 1 — reducciones**: ordenar las probabilidades de mayor a menor; fundir los dos últimos símbolos en uno (sumando probabilidades) y reordenar: es la **fuente reducida**. Repetir hasta tener dos símbolos.
**Paso 2**: a la última reducción se le asigna el código compacto 0 y 1.
**Paso 3 — retroceder**: cada símbolo conserva su palabra, salvo el que provenía de la fusión ($S_\alpha$): sus dos componentes reciben la palabra de $S_\alpha$ más un 0 y más un 1, respectivamente.

No siempre hace falta reducir hasta dos símbolos: basta con llegar a una reducción cuyo código compacto sea evidente (por ejemplo, probabilidades potencias de 1/2).

Ejemplo de la cátedra: 0,4 / 0,3 / 0,1 / 0,1 / 0,06 / 0,04.

Reducciones (en cada paso se funden los dos menores; entre paréntesis, el símbolo nuevo):
- S: 0,4 · 0,3 · 0,1 · 0,1 · 0,06 · 0,04
- Red. 1: 0,4 · 0,3 · (0,1 = S₅+S₆) · 0,1 · 0,1
- Red. 2: 0,4 · 0,3 · (0,2 = dos de 0,1) · 0,1
- Red. 3: 0,4 · (0,3 = 0,2 + 0,1) · 0,3
- Red. 4: (0,6 = 0,3 + 0,3) → **0** · 0,4 → **1**

Hacia atrás:
- Red. 3: 0,4 = 1 · 0,3 = 00 · 0,3 = 01 (las dos mitades de 0,6 = 0).
- Red. 2: el 0,3 = 01 que venía de fundir se abre en 0,2 = 010 y 0,1 = 011.
- Red. 1: 0,2 = 010 se abre en S₃ = 0100 y S₄ = 0101; el 0,1 = 011 es S₅+S₆.
- S: S₅ = 0110, S₆ = 0111.

| Sᵢ | S₁ | S₂ | S₃ | S₄ | S₅ | S₆ |
|---|---|---|---|---|---|---|
| Pᵢ | 0,4 | 0,3 | 0,1 | 0,1 | 0,06 | 0,04 |
| Código | 1 | 00 | 0100 | 0101 | 0110 | 0111 |

$L = 0{,}4\cdot1 + 0{,}3\cdot2 + 4\cdot(0{,}1+0{,}1+0{,}06+0{,}04) = 2{,}2$ binit/símb. H = 2,1435 bit → η = 0,9743, redundancia 0,0257.

**Por qué es compacto** (demostración del apunte, por reducción al absurdo): si $C_j$ es compacto para la reducción $S_j$, el código $C_{j-1}$ obtenido al desdoblar tiene $L_{j-1} = L_j + P_{\alpha0} + P_{\alpha1}$. Si existiera para $S_{j-1}$ un código instantáneo con $L'_{j-1} < L_{j-1}$, juntando sus dos palabras más largas (las de los símbolos menos probables) y quitando el último binit se obtendría para $S_j$ un código con $L'_j = L'_{j-1} - P_{\alpha0} - P_{\alpha1} < L_j$: absurdo, porque $C_j$ era compacto. Como la reducción de dos símbolos (0, 1) es trivialmente compacta, por inducción el código final lo es.

##### Huffman r-ario y símbolos falsos
Se agrupan de a r: cada reducción tiene r − 1 símbolos menos. Para que la última reducción tenga exactamente r símbolos:
$$\omega = r + \alpha(r-1),\quad \alpha \text{ entero}$$
Si α no es entero, se agregan símbolos falsos de probabilidad 0 (de a uno hasta que dé entero); una vez construido el código se descartan.
- Práctica: ω = 13, r = 4 → α = 9/3 = 3 → **no** hace falta agregar. ω = 14, r = 4 → α = 10/3 → con 16 símbolos α = 4 → hay que agregar **2** falsos.

##### Rendimiento y redundancia
$$\eta = \frac{H_r(S)}{L} = \frac{H(S)}{L\lg r}, \qquad \text{Red} = 1 - \eta$$
Al aumentar r baja L pero baja también η en general (los símbolos falsos y el redondeo pesan más). El caso extremo de la práctica: con r = q (una señal por símbolo) L = 1, el mínimo posible, pero hay que manejar q niveles de señal distintos: ése es el inconveniente.

#### Ejercicios resueltos tipo

**Ejercicio 1 (final 2012-03-09).** Código: A = 0 (27/64), B = 100, C = 101, D = 110 (9/64 c/u), E = 11100, F = 11101, G = 11110 (3/64 c/u), H = 11111 (1/64). a) ¿Instantáneo? b) ¿Compacto? c) L. d) Kraft. e) η y redundancia.

1. a) Ninguna palabra es prefijo de otra (0 sólo inicia A; 100, 101, 110 no inician ninguna de 5 dígitos, que empiezan con 111) → **instantáneo**.
2. c) $L = \frac{27\cdot1 + 3\cdot9\cdot3 + 3\cdot3\cdot5 + 1\cdot5}{64} = \frac{27+81+45+5}{64} = \frac{158}{64} = $ **2,469 binit/símb**.
3. d) $2^{-1} + 3\cdot2^{-3} + 4\cdot2^{-5} = \frac12 + \frac38 + \frac18 = $ **1** ≤ 1 → existen códigos instantáneos con esas longitudes, y como la suma es exactamente 1 no "sobra" ninguna rama del árbol (no se puede acortar ninguna palabra sin violar Kraft).
4. e) $H = \frac{27}{64}\lg\frac{64}{27} + 3\cdot\frac{9}{64}\lg\frac{64}{9} + 3\cdot\frac{3}{64}\lg\frac{64}{3} + \frac{1}{64}\lg64 = $ **2,434 bit** (es la extensión de orden 3 de una fuente binaria 3/4, 1/4: 3·0,8113). η = 2,434/2,469 = **0,986**; redundancia **0,014**.
5. b) Aplicando Huffman a esas probabilidades se obtienen exactamente las longitudes 1, 3, 3, 3, 5, 5, 5, 5 → L mínima = 2,469 → el código es **compacto** (L > H porque las probabilidades no son potencias de 1/2, pero ningún instantáneo lo mejora).

**Ejercicio 2 (tipo práctica "Ejercitación Codificación").** Fuente de 6 símbolos 0,3 / 0,25 / 0,15 / 0,12 / 0,10 / 0,08. Código compacto **ternario** (r = 3), rendimiento.

1. ¿Símbolos falsos? ω = 6: α = (6 − 3)/2 = 1,5 → no entero. Con 7: α = 2 → agrego **1** símbolo falso de probabilidad 0.
2. Reducción 1 (fundo los tres menores 0,10 + 0,08 + 0): 0,3 / 0,25 / 0,18 / 0,15 / 0,12.
3. Reducción 2 (0,18 + 0,15 + 0,12 = 0,45): 0,45 / 0,3 / 0,25 → código 0, 1, 2.
4. Hacia atrás: 0,45 = 0 → 0,18 = 00, 0,15 = 01, 0,12 = 02; 0,18 = 00 → 0,10 = 000, 0,08 = 001, falso = 002 (se descarta).
5. Código: 0,3 → 1; 0,25 → 2; 0,15 → 01; 0,12 → 02; 0,10 → 000; 0,08 → 001.
6. L = 0,3 + 0,25 + 2(0,15 + 0,12) + 3(0,10 + 0,08) = **1,63 dígitos ternarios/símb**.
7. H = 2,4224 bit → $H_3 = 2{,}4224/\lg3 = 1{,}5284$ → η = 1,5284/1,63 = **0,938**, redundancia 0,062. Kraft: $2\cdot3^{-1} + 2\cdot3^{-2} + 2\cdot3^{-3} = 26/27 \le 1$ ✓ (el 1/27 que falta es la rama del falso).

**Ejercicio 3 (práctica N°1, último punto: puente entre unidades 1 y 2).** Pulsos de 1 ms con 4 niveles de probabilidades 1/2, 1/4, 1/8, 1/8, codificados a = 00, b = 01, c = 10, d = 11. a) R. b) Duración de un binit. c) Binits por bit.

1. H = 1/2·1 + 1/4·2 + 2·1/8·3 = **1,75 bit/símb** → R = 1,75/1 ms = **1750 bps**.
2. Cada símbolo (1 ms) se reemplaza por 2 binits → cada binit dura **0,5 ms** (r = 2000 binit/s).
3. 2 binit/símb ÷ 1,75 bit/símb = **1,143 binit/bit**. Con un Huffman (0, 10, 110, 111) L = 1,75 = H → 1 binit/bit (probabilidades potencias de 1/2: código compacto con η = 1).

#### Dudas / pendientes
- **Kraft: ¿necesaria o suficiente?** El apunte (`2 - Codificación`, §4.6) dice "condición suficiente y necesaria para que exista al menos un código instantáneo". El `Resumen.md` de "Para rendir el final" la llama sólo "condición necesaria" (y lo mismo para McMillan). Vale el apunte. En el multiple choice la respuesta es "**puede ser** instantáneo".
- **Definición de compacto**: el apunte lo define entre **instantáneos** ("igual o menor que la longitud media de todos los códigos instantáneos que puedan aplicarse a la misma fuente y al mismo alfabeto"). `Resumen.md` y Preguntas frecuentes lo definen entre **unívocos**. Por McMillan da lo mismo en longitud, pero para el multiple choice usar la redacción del apunte: instantáneo, todos los instantáneos, misma fuente **y mismo alfabeto**.
- **Errata en el Huffman del apunte** (pág. 12, cuadro de la reducción 1): imprime "0,1 − 001" para el símbolo S₅+S₆; debería ser **011** (001 tendría a 00 = S₂ como prefijo). El código final del apunte (S₃ = 0100, S₄ = 0101, S₅ = 0110, S₆ = 0111) es consistente con 011. Otra opción de Huffman igual de válida (empatando distinto) es 1, 00, 011, 0100, 01010, 01011, también con L = 2,2.
- La demostración de compacidad del apunte (pág. 13) tiene erratas: "P(j−1,1) = l(j−1,1)" (son longitudes l = l) y "P(j−1,n) = P(j−1,n+1) = P(j,n)" (es la suma). El Santo Resumen las corrige igual.
- El Santo Resumen ilustra el primer teorema con 0,7/0,3 usando longitudes de Shannon (1 y 2 → L = 1,3); ese código no es compacto (con 1 binit por símbolo, L = 1). No contradice el teorema, pero no es el código óptimo.
- **Shannon–Fano** no aparece en ninguna fuente de la cátedra; sólo Huffman. Las "longitudes de Shannon" $\lceil\log_r(1/P_i)\rceil$ sí aparecen, dentro de la demostración del primer teorema.
- El apunte `2 - Codificación` lleva el rótulo "Unidad N°4" de un programa viejo; en la wiki va como Unidad 2. Los ejercicios del apunte de práctica con las tablas de probabilidades están como imágenes perdidas (EMBED PBrush): enunciados incompletos.
- La demostración de la cota inferior la reconstruí desde el PDF/Santo Resumen (la conversión perdió las fórmulas 4.9.x); los pasos son los estándar.

#### Fuentes
- `fuentes/teoria/2 - Codificación.md` (+ `.pdf`, págs. 1–14 y 12–13 para el Huffman)
- `fuentes/practica/Ejercitación Codificación.md`
- `fuentes/practica/Ejercitación Códigos extra.md`
- `fuentes/practica/Práctica N°1 -Teoría de la Información-RESUELTO.md` (último ejercicio)
- `fuentes/resumenes/Para rendir el final/Práctica - Fórmulas y pasos para los ejercicios.md`
- `fuentes/resumenes/Para rendir el final/Resumen.md`
- `fuentes/resumenes/Para rendir el final/Teoría - Preguntas frecuentes (Parte 1).md` y `(Parte 2).md`
- `fuentes/resumenes/1° Parcial/Resumen 1° Parcial Teoría (Parte 2).md`, `fuentes/resumenes/1° Parcial/Resumen Parcial 1 (2025).md`
- `fuentes/resumenes/El Santo Resumen/el-santo-resumen.md` (secciones "Códigos", "Primer teorema de Shannon", "Huffman" y "Final")
- Finales: `fuentes/finales/Práctica/2012/Comunicaciones - Final - 2012-03-09.md`, `fuentes/finales/Práctica/2015/…2015-12-04.md`; teoría: `fuentes/finales/Teoría/2020/*.md`, `fuentes/finales/Teoría/2021/*.md`

### Unidad 3 — Detección y corrección de errores: códigos lineales

#### Conceptos clave
- **Ruido unitario**: cambio de un binit por su complemento.
- **Distancia** entre dos palabras: cantidad de dígitos en que difieren (distancia de Hamming). **Distancia mínima** $d_{min}$: la menor entre palabras del código. Con $d_{min} = 1$ un error simple transforma una palabra en otra del código y no se detecta.
- Detectar/corregir exige **redundancia**: usar menos palabras que las combinaciones posibles; las no usadas "absorben" el error.
- **Bit de paridad** (par: $i_p = i_1 \oplus \ldots \oplus i_n$; impar: $\oplus 1$): detecta todo error de orden impar, no corrige. 3 + 1 dígitos: η = 3/4.
- **Paridad por filas y columnas**: corrige error simple en la intersección fila/columna; requiere armar bloques.
- **Hamming (paridad por zonas)**: m dígitos de información y n de control con $2^n \ge m + n + 1$. Para m = 4 → n = 3 (código 7 dígitos, η = 4/7 = 0,571). Con los controles en las posiciones 2ᵏ, el número binario C₃C₂C₁ da la posición del error.
- **Código lineal / de grupo V**: subespacio de $2^m$ palabras de n dígitos (m < n), con suma sin acarreo (⊕).
- **G (matriz generadora)**: m × n, filas linealmente independientes; V = todas las combinaciones lineales $v = k_1g_1 + \ldots + k_mg_m$, kᵢ ∈ {0,1}. La base no es única.
- **V'** espacio ortogonal ($2^{n-m}$ palabras); **H (matriz de control de paridad)**: base de V', (n − m) × n.
- Ortogonalidad: $v_i \cdot H^T = 0\ \forall v_i \in V$; $v'_i \cdot G^T = 0\ \forall v'_i \in V'$ (equivalente: $G\,H^T = 0$).
- **Síndrome**: $S = v_{recibida}\cdot H^T$ (1 × (n−m)). S = 0 → palabra del código (correcta o error no detectable). S ≠ 0 → error. Como $(v + e)H^T = eH^T$, **el síndrome depende sólo del error**.
- Cantidad de síndromes distintos no nulos: $2^{n-m} - 1$. Para corregir error simple en los n dígitos: $2^{n-m} - 1 \ge n$.
- **Errores no detectables**: los que coinciden con palabras del código (sumados a una palabra dan otra palabra).
- **Familia de errores** de un síndrome: todas las palabras (todos los errores, de cualquier orden) que dan ese síndrome. Se corrige si en la familia hay **un único** vector de peso mínimo (criterio de mayor probabilidad / máxima verosimilitud).

#### Desarrollo

##### Distancia y redundancia
Código de 3 binits con las 8 combinaciones: 000 … 111. Distancias: d(100, 101) = 1; d(000, 011) = 2; d(011, 100) = 3; $d_{min} = 1$. Si se envía 100 y llega 101, que también es palabra del código, el error pasa inadvertido. Para detectar hay que aumentar $d_{min}$: usar sólo parte de las combinaciones.

(Conocimiento general, no está explícito en el apunte: con $d_{min}$ se detectan hasta $d_{min} - 1$ errores y se corrigen hasta $\lfloor (d_{min}-1)/2 \rfloor$. Por eso Hamming (7,4), con $d_{min} = 3$, corrige 1.)

##### Bit de paridad
Se agrega un dígito para que la cantidad de unos sea par (o impar). Con 3 de información + 1 de paridad hay 2⁴ = 16 combinaciones y se usan 8 → $d_{min} = 2$; las otras 8 absorben el error simple.
- TX `1010` (101 + paridad par 0) → RX `1010`: el receptor recalcula la paridad de 101 = 0, coincide → OK.
- TX `0101` → RX `0111`: la paridad recalculada de 011 = 0 ≠ 1 recibido → error detectado, pero **no se sabe dónde**. Se descarta y se pide retransmisión.
- Detecta todos los errores de orden K impar; los de orden par pasan.

Costo: mensajes equiprobables, $H = \lg 2^3 = 3$ bit; sin paridad L = 3 → η = 1, redundancia 0. Con paridad L = 4 → η = 3/4 = **0,75**, redundancia 0,25.

Otros criterios de detección del apunte: **por mayoría** (palabras de longitud fija con peso fijo de unos, ej. l = 5 con tres unos: $\binom{5}{3} = 10$ palabras de las 32; detecta todos los errores unitarios) y **de igual peso** (igual cantidad de unos que de ceros, l par).

**Regla de decisión**: cuando no se puede retransmitir, se transforma la palabra errónea en la palabra válida más probable. Ej.: S₁ = 000, S₂ = 111; si llega 001 se decide 000, si llega 011 se decide 111 (se asume que el error simple es mucho más probable que el doble).

##### Paridad por filas y columnas
Se arma un bloque m × n de palabras, se agrega paridad por fila y por columna → (m+1) × (n+1). En recepción se recalculan: el dígito con error está en la **intersección** de la fila y la columna que no coinciden. Si sólo falla una fila (o una columna), el error está en un bit de paridad. Inconveniente: hay que armar bloques; no corrige palabra por palabra.

##### Hamming: paridad por zonas
Con diagrama de Venn de tres zonas (apunte `3 - Detección…`): cada control es la paridad par de los dígitos de información de su zona, con un dígito de información en cada intersección:
$$C_1 = I_0 \oplus I_1 \oplus I_2,\quad C_2 = I_1 \oplus I_2 \oplus I_3,\quad C_3 = I_0 \oplus I_2 \oplus I_3$$
Palabra $I_3I_2I_1I_0\,C_3C_2C_1$. En recepción se recalculan los controles y se comparan con los recibidos:
- TX `1000 110`, RX `1010 110`: recalculados con 1010 → C₃C₂C₁ = 101; comparados con 110 recibidos cambian **C₁ y C₂** → el único dígito común a las zonas I y II es **I₁** → información correcta 1000.
- Si cambia **un solo** control, el error está en ese dígito de control (la información está bien).
- Si no cambia ninguno → palabra correcta.

**¿Cuántos controles?** Con n controles hay $2^n$ configuraciones; deben indicar error en cada uno de los m + n dígitos más una que indique "todo bien":
$$2^n \ge m + n + 1$$
m = 4: n = 2 → 4 ≥ 7 no; n = 3 → 8 ≥ 8 ✓. Rendimiento: $H = \lg 2^4 = 4$ bit, L = 7 → η = 4/7 = **0,571**, redundancia 0,43.

**Versión posicional** (apunte `2 - Codificación`, §4.17): se numeran las posiciones 1 … 7 y los controles van en las posiciones $2^k$ (1, 2, 4); la información, en el resto. Cada control mira las posiciones que tienen un 1 en su mismo bit de la representación binaria:

| Posición | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Dígito | C₁ | C₂ | i₀ | C₃ | i₁ | i₂ | i₃ |
| Binario | 001 | 010 | 011 | 100 | 101 | 110 | 111 |

- C₁ = {1, 3, 5, 7} → $C_1 = i_0 \oplus i_1 \oplus i_3$
- C₂ = {2, 3, 6, 7} → $C_2 = i_0 \oplus i_2 \oplus i_3$
- C₃ = {4, 5, 6, 7} → $C_3 = i_1 \oplus i_2 \oplus i_3$

En recepción se pone 1 en cada zona alterada; el número **C₃C₂C₁ en decimal es la posición errónea** (000 = sin error). Ejemplo del apunte: información i₀i₁i₂i₃ = 1101 → C₁ = 1, C₂ = 0, C₃ = 0 → TX `1010101`. Llega `1010111`: zona I bien (C₁ = 0), II alterada (C₂ = 1), III alterada (C₃ = 1) → 110 = **6** → se invierte la posición 6.

##### Códigos lineales: estructura algebraica
Un código de longitud constante de n dígitos con las $2^n$ palabras es compacto (η = 1) pero tiene $d_{min} = 1$. Para detectar/corregir se toma un **subespacio** V de $2^m$ palabras (m < n): todos los dígitos viajan juntos, sin un campo de control separado como en Hamming.

| Objeto | Qué es | Dimensión |
|---|---|---|
| V | código de grupo | $2^m$ × n |
| G | base de V (matriz generadora) | m × n |
| V' | espacio ortogonal a V | $2^{n-m}$ × n |
| H | base de V' (matriz de control de paridad) | (n − m) × n |
| $H^T$ | transpuesta | n × (n − m) |
| S | síndrome | 1 × (n − m) |

La suma es sin acarreo: a + b = 0 ⇔ a = b; a + b = 1 ⇔ a = 1 + b; a + a = 0. Como son productos de matrices, no vale la conmutativa ($v H^T$, no $H^T v$).

**Base**: filas linealmente independientes (ninguna es combinación lineal de las otras) que generan todo el espacio. Si, por ejemplo, $h_3 = h_1 + h_2$, ese conjunto no es base.

##### Síndrome
Se recibe $v_{i?}$. Si $v_{i?} H^T = 0$, pertenece a V: correcta (o error no detectable). Si ≠ 0, hay error. Modelando el error como un vector e con unos donde se invirtieron dígitos:
$$v_{ie}H^T = (v_i + e)H^T = v_iH^T + eH^T = 0 + eH^T = S_e$$
Ejemplo del apunte: $v_1 = 101110$, $v_2 = 111001$, $e = 000100$ → llegan 101010 y 111101, y ambas dan **el mismo** síndrome $S_e$: sabiendo qué error produce $S_e$, se corrigen las dos.

Reglas:
- Si dos errores simples distintos dan el mismo síndrome ($e_aH^T = e_bH^T$), ese síndrome **sólo detecta**, no corrige.
- Hay $2^{n-m} - 1$ síndromes no nulos. Para corregir error simple en cada uno de los n dígitos hace falta uno distinto por dígito: $2^{n-m} - 1 \ge n$.
- Con $e_i$ = vector unitario en la posición i, $e_iH^T$ = **fila i de $H^T$**. Entonces: corrige error simple en todos los dígitos ⇔ las filas de $H^T$ son no nulas y distintas entre sí. Una fila nula = error no detectado en ese dígito; filas repetidas = sólo se detecta.
- **No se detectan** los errores que coinciden con palabras del código.

##### Familia de errores asociada a un síndrome
Para cada $S_i \ne 0$ se plantea $(x_1, \ldots, x_n)H^T = S_i$: n − m ecuaciones binarias con n incógnitas. Se eligen como independientes las variables que más se repiten, se les dan todos los valores y se despejan las demás. Las $2^m$ soluciones son la **familia**: todas las palabras del código con un mismo error, **de cualquier orden**. La palabra que viene de 000…0 muestra el error "desnudo":
- un único vector de peso 1 → se **detecta y corrige** error simple en ese dígito;
- ninguno de peso 1 y varios de peso 2 → **sólo se detecta** error doble;
- el mismo síndrome lo producen también errores dobles, triples, etc.; se decide por el más probable (el de menor peso).

##### Los tres tipos de ejercicio (resumen del apunte)
1. **Dan G**: combinación lineal → V; $v'G^T = 0$ → V' → elegir base H → $H^T$; $xH^T = S_i$ → familias.
2. **Dan H**: $vH^T = 0$ → V (y una G eligiendo m palabras independientes); $xH^T = S_i$ → familias.
3. **Dan cantidad de mensajes y requisitos de corrección**: $2^m \ge$ mensajes → m; $2^{n-m} - 1 \ge$ síndromes necesarios → n (por prueba y error); se proponen los síndromes de cada error simple (contando en binario) → filas de $H^T$; $vH^T = 0$ → V; se eligen las palabras necesarias.

#### Ejercicios resueltos tipo

**Ejercicio 1 (finales 2015-12-18, 2017-02-15, 2020-02-21).** Transmitir 12 mensajes protegidos contra error simple aplicando Hamming. Ejemplo de error en un dígito de información y en uno de control.

1. Información: $2^m \ge 12$ → m = 3 da 8 (no alcanza) → **m = 4**.
2. Control: $2^n \ge m + n + 1$ → n = 3: 8 ≥ 8 ✓ → **n = 3**, palabra de 7.
3. Posiciones: C₁ C₂ i₀ C₃ i₁ i₂ i₃; $C_1 = i_0 \oplus i_1 \oplus i_3$, $C_2 = i_0 \oplus i_2 \oplus i_3$, $C_3 = i_1 \oplus i_2 \oplus i_3$.
4. Código (mensaje k = i₃i₂i₁i₀ en binario → palabra en posiciones 1…7):

| k | i₃i₂i₁i₀ | palabra | k | i₃i₂i₁i₀ | palabra |
|---|---|---|---|---|---|
| 0 | 0000 | 0000000 | 6 | 0110 | 1100110 |
| 1 | 0001 | 1110000 | 7 | 0111 | 0010110 |
| 2 | 0010 | 1001100 | 8 | 1000 | 1101001 |
| 3 | 0011 | 0111100 | 9 | 1001 | 0011001 |
| 4 | 0100 | 0101010 | 10 | 1010 | 0100101 |
| 5 | 0101 | 1011010 | 11 | 1011 | 1010101 |

5. Error en información: TX k = 6 `1100110`; se invierte la posición 5 (i₁) → RX `1100010`. Zona C₁ {1,3,5,7}: 1⊕0⊕0⊕0 = 1 (alterada). C₂ {2,3,6,7}: 1⊕0⊕1⊕0 = 0 (bien). C₃ {4,5,6,7}: 0⊕0⊕1⊕0 = 1 (alterada). C₃C₂C₁ = 101 = **5** → se invierte la posición 5 → `1100110` ✓.
6. Error en control: TX `1100110`; se invierte la posición 2 (C₂) → RX `1000110`. C₁: 1⊕0⊕1⊕0 = 0; C₂: 0⊕0⊕1⊕0 = 1; C₃: 0⊕1⊕1⊕0 = 0 → 010 = **2** → el error es el dígito de control C₂; la información no se toca.

**Ejercicio 2 (apunte `4 - Ejemplos Códigos Lineales`, ej. 1; tipo "dan G").** G con filas g₁ = 100011, g₂ = 101101, g₃ = 111000 (n = 6, m = 3). a) V. b) Errores no detectados. c) Comportamiento ante errores simples.

1. a) Las 8 combinaciones $k_1g_1 + k_2g_2 + k_3g_3$: V = {000000, 100011, 101101, 001110, 111000, 011011, 010101, 110110}. $d_{min} = 3$.
2. b) No se detectan los errores iguales a palabras del código: triples en (x₁,x₅,x₆), (x₃,x₄,x₅), (x₁,x₂,x₃), (x₂,x₄,x₆); cuádruples en (x₁,x₃,x₄,x₆), (x₂,x₃,x₅,x₆), (x₁,x₂,x₄,x₅).
3. c) $v'G^T = 0$ da: $x'_1 + x'_5 + x'_6 = 0$; $x'_1 + x'_3 + x'_4 + x'_6 = 0$; $x'_1 + x'_2 + x'_3 = 0$. Libres x'₁, x'₃, x'₆ → V' = {000000, 000111, 011100, 011011, 110110, 110001, 101010, 101101}. Base elegida (independiente): H = {011100, 011011, 110110}. Verificado: $GH^T = 0$.
4. $H^T$ por filas (fila i = síndrome del error simple en xᵢ): x₁ → 001, x₂ → 111, x₃ → 110, x₄ → 101, x₅ → 011, x₆ → 010.
5. Tabla de síndromes (verificada enumerando los 64 vectores):

| S | Vector(es) de peso mínimo en la familia | Conclusión |
|---|---|---|
| 001 | 100000 | corrige error simple en x₁ |
| 010 | 000001 | corrige x₆ |
| 011 | 000010 | corrige x₅ |
| 100 | 100100, 010010, 001001 | **sólo detecta** error doble (x₁x₄, x₂x₅ o x₃x₆) |
| 101 | 000100 | corrige x₄ |
| 110 | 001000 | corrige x₃ |
| 111 | 010000 | corrige x₂ |

6. Ejemplo: llega 111011 → S = 001 → error en x₁ → palabra correcta **011011** ✓ (está en V).
7. Familia de 001 completa: {100000, 000011, 001101, 101110, 110101, 010110, 011000, 111011}: incluye el error simple en x₁, dobles (x₅x₆, x₂x₃), triples, cuádruples y un quíntuple.

**Ejercicio 3 (final 2015-12-04; `Códigos Lineales` de práctica).** Transmitir 6 mensajes: detectar y corregir error simple en el 1° y 2° dígito, sólo detectar en el resto excepto el menos significativo, en el que no se detecta nada.

1. $2^m \ge 6$ → **m = 3**.
2. Síndromes no nulos necesarios: uno exclusivo para x₁, otro para x₂ y uno compartido para "sólo detectar" → 3. $2^{n-m} - 1 \ge 3$ → n − m = 2 → **n = 5** (con n = 4, 2¹ − 1 = 1 no alcanza).
3. Filas de $H^T$ (= síndrome de cada error simple): x₁ → 01; x₂ → 10; x₃ → 11; x₄ → 11; x₅ → **00** (no se detecta).
4. Ortogonalidad $vH^T = 0$: columna 1 → $x_2 + x_3 + x_4 = 0$; columna 2 → $x_1 + x_3 + x_4 = 0$. Libres x₃, x₄, x₅: $x_1 = x_2 = x_3 + x_4$.
5. V = {00000, 00001, 00110, 00111, 11010, 11011, 11100, 11101}. Se eligen 6 cualesquiera, ej. sin 00000 ni 00001.
6. Comprobación: e = 10000 → S = 01 (único → corrige x₁); e = 01000 → 10 (corrige x₂); e = 00100 y 00010 → 11 (sólo detecta); e = 00001 → 00: ¡00001 es palabra del código!, el error en x₅ no se detecta, como pedía el enunciado.

#### Dudas / pendientes
- **Error en el apunte `4 - Ejemplos Códigos Lineales`, ej. 1**: en los síndromes 100, 101, 110 y 111 despeja mal x₁ (cuando la primera ecuación vale 1, los dos "1 +" se cancelan y el apunte deja uno). Resultado: rotula **mal** las familias. El apunte dice 100 → corrige x₄; 101 → sólo detecta doble; 110 → x₂; 111 → x₃. Lo correcto, verificado con su propia $H^T$ y enumerando todo, es **100 → sólo detecta doble (x₁x₄, x₂x₅, x₃x₆); 101 → x₄; 110 → x₃; 111 → x₂**. Los conjuntos de vectores que lista sí son familias reales, pero bajo el síndrome equivocado. Las conclusiones generales (6 dígitos corregibles + un síndrome de sólo detección) no cambian. El Santo Resumen no lo señala. Los ej. 3 y 4 del mismo apunte los verifiqué y están bien.
- **"Familia de errores": contradicción entre resúmenes.** `Resumen 1° Parcial Teoría (Parte 2)` y `Resumen Parcial 1 (2025)` dicen que en la familia "se pueden observar sólo los errores simples y dobles". El apunte de la cátedra muestra que la familia contiene **todos** los errores (simples, dobles, triples, cuádruples, quíntuples). En el multiple choice (finales 2021-11-19 y 2021-12-17, 1° parcial 2021) corresponde "**Todos los errores de las palabras códigos asociadas a ese síndrome**".
- **Notación cruzada**: en Hamming (`2 - Codificación`) **m = información y n = control** ($2^n \ge m + n + 1$); en códigos lineales **n = total y m = información** (n − m = control). "Fórmulas y pasos" usa la de Hamming. No mezclar en el examen: aclarar la notación al empezar.
- **Dos convenciones de Hamming**: Venn con campos separados (`3 - Detección…`: $I_3I_2I_1I_0C_3C_2C_1$, C₁ = I₀+I₁+I₂…) y posicional intercalada (`2 - Codificación`: controles en 1, 2, 4). Las dos están en la cátedra; la posicional permite leer la posición del error directamente. En los finales piden "aplicando Hamming" sin especificar.
- Errata del apunte posicional (pág. 20): imprime "C₁ C₃ C₂ / 0 0 1 → 3"; con zonas I y II alteradas lo correcto es **C₃C₂C₁ = 011 = 3**.
- En `3 - Detección…` el ejemplo "errores no detectables" lista un código de grupo con 7 palabras; falta la octava (101010, que es justamente el error triple x₁x₃x₅ que analiza).
- `Ejercitación Códigos extra` pide un **código cíclico** con g(x) = 1 + x + x², n = 6: no hay teoría de códigos cíclicos en las fuentes (fuera de alcance; conocimiento general: G se arma con los corrimientos de los coeficientes 111000, 011100, 001110, 000111).
- Agregados de conocimiento general: relación $d_{min}$ ↔ errores detectables/corregibles, $GH^T = 0$ y "fila i de $H^T$ = síndrome del error en xᵢ" como atajo (el apunte llega a lo mismo planteando $e_iH^T = S_i$).

#### Fuentes
- `fuentes/teoria/3 - Detección y Corrección de errores.md`
- `fuentes/teoria/4 - Ejemplos Codigos Lineales.md` (ej. 1 a 6 y "Resumiendo")
- `fuentes/teoria/2 - Codificación.md` (+ `.pdf` págs. 15–22: confiabilidad, paridad, mayoría, igual peso, regla de decisión, Hamming)
- `fuentes/practica/Códigos Lineales.md`
- `fuentes/practica/Ejercitación Códigos extra.md`, `fuentes/practica/Ejercitación Codificación.md` (ej. de paridad por zonas para 10 símbolos)
- `fuentes/resumenes/Para rendir el final/Práctica - Fórmulas y pasos para los ejercicios.md`
- `fuentes/resumenes/Para rendir el final/Resumen.md`, `…/Teoría - Preguntas frecuentes (Parte 1).md` y `(Parte 2).md`
- `fuentes/resumenes/1° Parcial/Resumen 1° Parcial Teoría (Parte 1).md`, `…/Resumen 1° Parcial Teoría (Parte 2).md`, `…/Resumen Parcial 1 (2025).md`
- `fuentes/resumenes/El Santo Resumen/el-santo-resumen.md` (secciones "Detección y corrección de errores", "Hamming", "Códigos lineales", "Familia de errores")
- Finales: `fuentes/finales/Práctica/2015/…2015-12-04.md`, `…/2015/…2015-12-18.md`, `…/2017/…2017-02-15.md`, `…/2020/…2020-02-21.md`, `…/2011/…2011-02-18.md`, `…/2012/…2012-03-09.md`; teoría: `fuentes/finales/Teoría/2021/*.md`

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
- **$B_w = 1/\tau$ vs. $B = s/2$.** La guía y el apunte 5 (pág. 24) toman el primer cruce por cero de la sinc, $B_w = 1/\tau$, y eso es lo que usan este archivo y `estudio/final/banco-ejercicios.md`. El apunte 1 (pág. 12) da para binario $B = s/2 = 1/(2\tau)$ (Nyquist); con ese criterio todos los anchos de banda TDM se dividen por 2. En el examen, indicar el criterio. El mismo problema aparece en FDM: la respuesta oficial de 2011 usa $2f_{max}$ por señal y el Santo Resumen usa $N\cdot 2W$.
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

### Unidad 8 — Códigos correctores de error: códigos cíclicos y convolucionales

#### Conceptos clave
- **Capacidad de un código según $d_{min}$** (el informe lo enuncia como condición necesaria y suficiente): detecta hasta k errores ⇔ $d_{min} \ge k+1$; corrige hasta k ⇔ $d_{min} \ge 2k+1$. Corrector de orden 1 ⇔ $d_{min} = 3$ (Hamming (7,4)).
- **Repetición**: cada binit se manda n veces y se decide por mayoría. Con n = 3 sobre un BSC con p = 0,01: $P_e = 3p^2(1-p) + p^3 \approx 3 \cdot 10^{-4}$, contra $10^{-2}$ sin repetir. Paga con rendimiento: η = 1/3.
- **Código de bloque**: palabras de longitud fija n; cada palabra depende sólo del bloque de información actual. **Código convolucional**: la salida depende de la entrada actual y de las anteriores (**memoria**). Trabaja sobre flujos continuos.
- **Código cíclico**: código lineal (de grupo) en el que todo **corrimiento circular** de una palabra del código es otra palabra del código.
- **Notación polinómica**: la palabra $v = (v_1 \ldots v_n)$ se escribe $v(x) = v_1x^{n-1} + \ldots + v_{n-1}x + v_n$, con el primer dígito como coeficiente de mayor grado, igual que en el informe y en CRC. Aritmética módulo 2: $x^i + x^i = 0$.
- **Polinomio generador g(x)**: de grado n − m (= cantidad de dígitos de control), **divide a $x^n + 1$**. Toda palabra del código es múltiplo de g(x): $c(x) = q(x)\,g(x)$. Se mantiene la notación de la U3: n = dígitos totales, m = información.
- **Codificación sistemática**: $c(x) = x^{n-m}\,i(x) + R_{g(x)}\!\left[x^{n-m}\,i(x)\right]$, donde $R_g[\cdot]$ es el resto de dividir por g(x). Quedan la información adelante y el resto como control.
- **Síndrome**: $s(x) = R_{g(x)}[v'(x)]$. Si s = 0, la palabra es del código; si s ≠ 0, hay error. Es lo mismo que $S = v' \cdot H^T$ de la U3 y también **depende sólo del error**: $R_g[c + e] = R_g[e]$.
- **CRC**: código cíclico usado sólo para **detectar** (Ethernet usa CRC‑32).
- **BCH**: cíclicos binarios que corrigen t > 1 errores. **Reed–Solomon**: BCH no binario que trabaja con símbolos de b bits y es bueno contra **ráfagas**.
- **Convolucional (1 entrada, 2 salidas, K = 3)**: tasa $R = 1/2$, **longitud de restricción** K = entrada actual + 2 de memoria, $2^{K-1} = 4$ estados. Lo definen sus **secuencias generadoras** (ej. $g_1 = 111$, $g_2 = 101$).
- **Distancia libre $d_{free}$**: peso mínimo de un camino que sale del estado 0 y vuelve a él. Cumple el papel de $d_{min}$: corrige $\lfloor (d_{free}-1)/2 \rfloor$ errores "cercanos".
- **Viterbi**: decodificación de **máxima verosimilitud** sobre el trellis. Conserva en cada estado el camino sobreviviente de menor distancia acumulada.
- **Código catastrófico**: entradas que difieren en infinitos bits producen salidas que difieren en pocos bits. Un error finito en el canal causa entonces infinitos errores de información, y por eso se evita.

#### Desarrollo

##### Detectar vs corregir (lo que el informe agrega a la U3)
- **Detector**: con la redundancia el receptor sabe que hubo error, pero no dónde, y pide **retransmisión**. **Corrector**: con más redundancia deduce qué se transmitió y corrige un número limitado de errores.
- Usar todas las $2^n$ combinaciones hace imposible detectar. Dejar combinaciones sin usar es condición **necesaria pero no suficiente**: en BCD (10 de 16 combinaciones) 0011 → 0010 no se detecta porque 0010 también es del código.
- **Regla de decisión**: cuando no se puede retransmitir, la palabra errónea se reemplaza por la palabra del código más cercana, que es la más probable si los errores simples dominan. Corregir así también puede introducir un error nuevo.
- Repetición con n = 2: llega "0 … 1" y es imposible decidir. Con n = 3 se decide por mayoría. Las probabilidades del ejemplo BSC: sin error $\bar p^3$, un error $3p\bar p^2$, dos errores $3p^2\bar p$, tres errores $p^3$. Se decodifica mal con 2 o 3 errores.

##### Códigos cíclicos
**Definición y ejemplo (informe).** Si $a = 100100$ pertenece a un código cíclico, también pertenecen su corrimiento a izquierda 001001 y a derecha 010010. Un corrimiento a izquierda equivale a multiplicar por x módulo $x^n + 1$, porque $x^n \equiv 1$ (conocimiento general). Por eso las palabras son los múltiplos de g(x) y g(x) tiene que dividir a $x^n + 1$.

**Matrices (conocimiento general, enlaza con la U3).**
- **G no sistemática**: sus m filas son g(x) y sus corrimientos $x\,g(x), \ldots, x^{m-1}g(x)$. Para g = 1011 y n = 7: 1011000, 0101100, 0010110, 0001011.
- **G sistemática**: la fila i es $x^{n-i} + R_g[x^{n-i}]$, con i = 1 … m (información ‖ resto).
- **H**: con $h(x) = (x^n + 1)/g(x)$ (polinomio de paridad), las filas de H son los corrimientos de h(x) leído al revés. También sirve tomar como $H^T$ la tabla de restos $R_g[x^{n-i}]$, porque el resto es lineal y su núcleo es el código: es otra base de V'.
- **Atajo de la U3**: el resto de un error simple en la posición i es la **fila i de $H^T$**. Si todos los restos de $x^{n-1}, \ldots, x^0$ son no nulos y distintos, el código corrige error simple.

**Codificación sistemática por división (el procedimiento del informe, en binario).**
1. Se multiplica la información por $x^{n-m}$: se agregan n − m ceros a la derecha.
2. Se divide por g(x) en módulo 2 (restas = XOR, sin acarreo) y se toma el resto $r(x)$, de grado < n − m.
3. $c(x) = x^{n-m}i(x) + r(x)$, porque en binario "− r" es "+ r". La palabra resultante es múltiplo de g(x).

El informe llama "síndrome" a ese resto. Es correcto si se mira $x^{n-m}i(x)$ como una palabra recibida, pero en la codificación conviene llamarlo **resto o control** para no mezclarlo con el síndrome de recepción.

**Ejemplo del informe en $\mathbb{F}_3$ (verificado).** Es un código [8,2] con $g(x) = (x^2+1)(x^2+x+2)(x^2+2x+2) = x^6 + x^4 + x^2 + 1$, factores de $x^8 - 1 = (x+1)(x+2)(x^2+1)(x^2+x+2)(x^2+2x+2)$. Codifica los 9 mensajes de 2 símbolos: 10 → 10101010, 12 → 12121212, 22 → 22222222, etc. Los restos y las palabras del informe están bien. Sólo describe mal cómo armó g: dice "todos menos uno de los factores" y en realidad dejó afuera dos, $(x+1)$ y $(x+2)$. El ejemplo sirve para ver la mecánica; en el final se trabaja en binario.

**Recepción.** Se divide lo recibido $v'(x)$ por g(x). Resto 0: correcta, o con un error no detectable (un error que es múltiplo de g(x), es decir, igual a una palabra del código). Resto ≠ 0: hay error, y con la tabla síndrome → patrón de error se corrige, igual que en Hamming.

**Implementación (conocimiento general).** La división se hace con un **registro de desplazamiento con realimentación** de n − m celdas y compuertas XOR en las posiciones de los coeficientes de g(x). Por eso los cíclicos son baratos en hardware y "fáciles de decodificar", como dice el informe.

**CRC: propiedades de detección (conocimiento general).** Con g(x) de grado r:
- detecta todo error simple si g tiene más de un término;
- detecta todo error de cantidad impar de bits si $(x+1)$ divide a g;
- detecta toda **ráfaga de longitud ≤ r**;
- no detecta los errores múltiplos de g(x).

CRC‑32 de Ethernet: r = 32.

**BCH y Reed–Solomon.**

| | BCH (binario) | Reed–Solomon |
|---|---|---|
| Alfabeto | bits | símbolos de b bits ($\mathbb{F}_{2^b}$) |
| Parámetros (conocimiento general) | $n = 2^q - 1$, $n - m \le q\,t$, $d_{min} \ge 2t+1$ | $n = 2^b - 1$ símbolos, corrige $t = (n-m)/2$ símbolos |
| Fuerte en | errores aleatorios múltiples, bloques de pocos cientos de bits | **ráfagas**: un símbolo errado cubre hasta b bits errados |
| Usos | — | CD/DVD, DVB, QR, código exterior junto con un convolucional |

Los dos son sistemáticos y corrigen más de un error, a diferencia de Hamming.

##### Códigos convolucionales
**Idea.** Son de 1955 (Elias, conocimiento general). Son lineales como los de bloque, pero el codificador es un circuito secuencial con memoria: un registro de desplazamiento y sumadores módulo 2. Cada bit de entrada produce n bits de salida que dependen de él y de los K − 1 bits anteriores. Las salidas se **multiplexan** (se intercalan) en un único flujo.

**Codificador de referencia (R = 1/2, K = 3, $g_1 = 111$, $g_2 = 101$, el clásico "(7,5)" en octal):**
$$v_1(t) = u_t \oplus u_{t-1} \oplus u_{t-2}, \qquad v_2(t) = u_t \oplus u_{t-2}$$
- **Respuesta impulsiva**: es la salida ante u = 1 0 0 (el 1 más los ceros de vaciado): 11 10 11. Se obtiene intercalando bit a bit $g_1$ y $g_2$.
- **Función de transferencia**: como es un sistema LTI discreto, $v = u * h$ (convolución, de ahí el nombre). Con la transformada z, $H_1(z) = 1 + z^{-1} + z^{-2}$ y $H_2(z) = 1 + z^{-2}$. Matricialmente, $v = u\,G$.
- El informe usa el mismo código con el orden invertido ($g_1 = 101$, $g_2 = 111$). Sale el mismo código con los dos bits de cada par intercambiados: respuesta impulsiva 11 01 11; la entrada 1100 da 11 10 10 11, verificado.

**Representaciones.**
1. **Diagrama de conexiones**: registro, sumadores y conmutador de salida.
2. **Diagrama de estados**: el estado es el contenido de la memoria, $(u_{t-1}u_{t-2})$; cada flecha se rotula "entrada/salida".
3. **Diagrama de Trellis**: el diagrama de estados desplegado en el tiempo. Cada columna repite los $2^{K-1}$ estados y codificar es recorrer un camino.

Además existe el **árbol** (conocimiento general). El *puncturing* no es una representación (ver Dudas).

**Tabla de transiciones (equivale al diagrama de estados; el trellis repite esta tabla en cada instante):**

| Estado actual $u_{t-1}u_{t-2}$ | Entrada 0 → próximo / salida | Entrada 1 → próximo / salida |
|---|---|---|
| 00 | 00 / 00 | 10 / 11 |
| 01 | 00 / 11 | 10 / 00 |
| 10 | 01 / 10 | 11 / 01 |
| 11 | 01 / 01 | 11 / 10 |

**Distancia libre.** El camino 00 → 10 → 01 → 00 (entrada 100) da 11 10 11, de peso 5, y ningún otro camino que vuelva a 00 pesa menos (verificado por enumeración). Entonces $d_{free} = 5$ y el código corrige 2 errores en la ventana de unas pocas longitudes de restricción.

**Viterbi (decisión dura).**
1. En cada instante se calcula, para cada transición, la distancia de Hamming entre el par recibido y la salida de la rama: es la métrica de rama.
2. A cada estado llegan dos caminos. Se suma la métrica acumulada y se queda el **sobreviviente** de menor métrica; el otro se descarta.
3. Al final, con la cola de K − 1 ceros que devuelve el codificador a 00, se toma el camino que termina en 00 y se lee la entrada de sus ramas.

Con **decisión blanda** se usa la distancia euclidiana sobre las muestras sin cuantizar, y rinde mejor. La secuencia de estados es una cadena de Markov oculta: se observan las salidas, no los estados.

**Probabilidad de error (informe).** Para p chico, con decisión dura:
$$P_{eb} \lesssim \frac{1}{k}\,(2\sqrt{p})^{d_{free}}$$
Para p = 10⁻³ y $d_{free} = 5$: $(2\sqrt{10^{-3}})^5 = 32 \cdot 10^{-7{,}5} \approx 1{,}01 \cdot 10^{-6}$ (verificado). Un BSC malo pasa a ser utilizable a costa de duplicar la velocidad binaria, porque R = 1/2.

**Códigos catastróficos (ejemplo del informe, verificado).** Con $g_1 = 110$ y $g_2 = 011$, los lazos de los estados 00 y 11 emiten 00. La entrada 111…1100 produce 10 01 00 00 … 00 10 01, a distancia 4 de la salida de la entrada nula, mientras que las entradas difieren en infinitos bits. Criterio general (conocimiento general): el código es catastrófico si $\text{mcd}(g_1(D), g_2(D)) \ne D^\ell$. Acá $g_1 = 1 + D$ y $g_2 = D(1 + D)$, que tienen el factor común $1 + D$.

**Puncturing.** Se parte de un código "madre" de tasa $1/n$ y se eliminan bits de salida según una matriz de perforación conocida por los dos extremos, para obtener tasas mayores (2/3, 3/4, …; ISDB‑T). El receptor rellena los huecos con bits "dummy" y decodifica con el mismo Viterbi del código madre.

**Aplicaciones.** Enlaces de radio y celulares (GSM), satélite y espacio profundo, DVB‑S/C/T, módems V.32bis/V.34, ADSL2+ y SHDSL. Es habitual la **concatenación**: RS como código exterior, contra ráfagas, y convolucional como código interior. La **TCM** (modulación codificada Trellis) combina el código con la modulación para recuperar el margen que se pierde al densificar la constelación (vínculo con la U4).

**Bloque vs convolucional.**

| | Cíclicos / bloque | Convolucionales |
|---|---|---|
| Unidad | bloque de m → n dígitos | flujo continuo, R = k/n |
| Memoria | no | sí (K − 1 bits) |
| Métrica de protección | $d_{min}$ | $d_{free}$ |
| Decodificación | síndrome (resto de dividir por g) | Viterbi sobre el trellis |
| Típico | detección (CRC), ráfagas (RS) | corrección en tiempo real en canales ruidosos |

#### Ejercicios resueltos tipo

**Ejercicio 1: cíclico (7,4) sistemático, $g(x) = x^3 + x + 1$ (1011).** Codificar i = 1001, verificar que es cíclico y corregir un error simple.
1. $x^3\,i(x) = x^6 + x^3$ → 1001**000**.
2. División módulo 2:
```
1001000
1011           (XOR en las posiciones del 1 líder)
-------
0010000
  1011
-------
0000110   → resto r = 110  (x² + x)
```
3. c = 1001 ‖ 110 = **1001110**, es decir, $c(x) = x^6 + x^3 + x^2 + x$. Verificación: $R_g[c] = 000$ ✓.
4. Es cíclico: el corrimiento 0011101 también es palabra del código. Las 16 palabras cumplen la propiedad, con $d_{min} = 3$ (verificado).
5. Tabla de síndromes (resto de cada error simple = fila de $H^T$):

| Posición | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Error | $x^6$ | $x^5$ | $x^4$ | $x^3$ | $x^2$ | $x$ | 1 |
| Síndrome | 101 | 111 | 110 | 011 | 100 | 010 | 001 |

Los 7 síndromes son no nulos y distintos, y $2^{3} - 1 = 7 \ge 7$: corrige error simple en todos los dígitos. Es un Hamming (7,4) en forma cíclica.

6. Llega 1011110 (error en la posición 3). $R_g = 110$ → posición 3 → se invierte → 1001110 ✓.

**Ejercicio 2: CRC con $g(x) = x^4 + x + 1$ (10011).** Mensaje M = 1101011111 (es el ejemplo clásico de Tanenbaum).
1. Se agregan 4 ceros: 1101011111**0000**. Dividido por 10011, el resto es **0010**.
2. Trama transmitida: **11010111110010**. En recepción, el resto da 0000 ✓.
3. Una ráfaga de 3 bits (posiciones 4 a 6) da 11001011110010, con resto 1000 ≠ 0: detectada. Tiene longitud ≤ r = 4, así que la detección está garantizada.
4. Con un error $e(x) = x^4 g(x)$ (bits 100110000 desde la posición 6) llega 11010011000010, con resto **0000**: **no se detecta**, porque el error es múltiplo de g.

**Ejercicio 3: convolucional R = 1/2, K = 3, $g_1 = 111$, $g_2 = 101$.** Codificar u = 1011 y decodificar con Viterbi una recepción con 2 errores.
1. Se agrega la cola 00: u = 1011**00**. Usando la tabla de transiciones, los estados son 00 → 10 → 01 → 10 → 11 → 01 → 00.
2. Salida: **11 10 00 01 01 11**.
3. Se invierten los bits 2 y 7 del flujo. Llega r = **10 10 00 11 01 11**.
4. Métricas acumuladas de los sobrevivientes ("—" = estado todavía inalcanzable):

| t | r | 00 | 01 | 10 | 11 |
|---|---|---|---|---|---|
| 1 | 10 | 1 | — | 1 | — |
| 2 | 10 | 2 | **1** | 2 | 3 |
| 3 | 00 | 2 | 3 | **1** | 3 |
| 4 | 11 | 3 | 2 | 2 | **2** |
| 5 | 01 | 3 | **2** | 3 | 2 |
| 6 | 11 | **2** | 3 | 3 | 3 |

5. Termina en 00 con métrica 2. El trace-back da los estados 00‑10‑01‑10‑11‑01‑00 → û = 1011 00 ✓. Se corrigieron 2 errores, consistente con $d_{free} = 5$. No hubo empates (verificado con un decodificador en Python).

**Ejercicio 4 (`Ejercitación Códigos extra`; queda resuelto el pendiente de la U3).** $g(x) = 1 + x + x^2$, n = 6. Pide G, H y si se detectan errores simples.
1. $x^6 + 1 = (x^3 + 1)^2 = (x+1)^2(x^2+x+1)^2$, así que g divide a $x^6 + 1$ ✓. Grado 2 → n − m = 2, **m = 4**: hay 16 palabras.
2. **G** (corrimientos): 111000, 011100, 001110, 000111. La forma sistemática es 100011, 010010, 001001, 000111, y genera el mismo código.
3. $h(x) = (x^6+1)/g(x) = x^4 + x^3 + x + 1$ (11011, simétrico). **H** = {110110, 011011}. Se verifica $G H^T = 0$ y que V' = {000000, 011011, 101101, 110110}.
4. Filas de $H^T$ (síndrome de cada error simple): x₁ → 10, x₂ → 11, x₃ → 01, x₄ → 10, x₅ → 11, x₆ → 01.
5. Conclusión: ninguna fila es nula, así que **se detecta todo error simple**, en información y en control. Las filas se repiten de a pares (x₁/x₄, x₂/x₅, x₃/x₆), así que **no se corrige**. Además $2^{2} - 1 = 3 < 6$ y $d_{min} = 2$: por ejemplo, 001001 ($x^3 + 1$) es palabra del código. Todo verificado enumerando las 64 palabras de 6 dígitos.

#### Dudas / pendientes
- **Errores del informe N° 2** (verificados):
  - Cubo de 3 bits: dice que de 100 a 011 "hay que recorrer necesariamente **4** aristas". Son **3**, que es la distancia máxima en 3 bits.
  - Presenta Hamming(7,4) como "palabra de 7 binits con **4** bits de paridad". Son **3** de paridad y 4 de información, como el mismo informe dice después.
  - Combinaciones por mayoría: escribe $\frac{5!}{3!(3-5)!}$, que debe ser $(5-3)!$. La lista de 10 palabras repite 01011 y le falta **01110**.
  - Paridad par: "bit que es 1 si la palabra es par" está al revés. Con paridad par, $i_p = 1$ cuando la información tiene cantidad **impar** de unos.
  - Llama "de peso constante" al código de **igual peso** (tantos unos como ceros). Igual peso es un caso particular de peso constante. "Por mayoría" lo describe de forma vaga; la U3 lo define como peso fijo.
  - Dice que Hamming(7,4) corrige error simple "y detecta errores de dos bits". Con $d_{min} = 3$ se puede **o** corregir 1 **o** detectar 2, no las dos cosas a la vez. Hacerlo a la vez exige el Hamming extendido (8,4) (conocimiento general).
  - BCH: la condición está mal transcripta ("t < (2m − 1)/2"; es $t < (2^m - 1)/2$) y faltan los parámetros. Los de la tabla son de conocimiento general.
  - RS: "es posible detectar y corregir sólo un símbolo de error" es falso en general. Un RS corrige $(n-m)/2$ símbolos; por ejemplo, RS(255,223) corrige 16.
  - Notación convolucional inconsistente: primero usa (n, m, k) con n = entradas y m = salidas, y después [2,1,3] con 2 = salidas, 1 = entrada, 3 = longitud de restricción. La literatura usa (n, k, K) con n = salidas. Las etiquetas de estado "$S_{2^{(k-1)^n}-1}$" deberían ser $2^{(K-1)\cdot k}$ estados.
  - Pone el **puncturing** entre las "representaciones gráficas" (y lo repite en la pregunta 8 del anexo). Es una técnica para subir la tasa; la tercera representación es el **Trellis** (o el árbol).
  - Asocia la distancia euclidiana/Hamming con canales "paso banda / banda base". La distinción real es decisión blanda vs dura.
  - "Corrige $(d_{free}-1)/2$ errores por cada n·L bits" es aproximado: la capacidad vale para errores suficientemente separados, no para una ventana rígida de 6 bits.
- **Ejemplo de Viterbi del informe** (r = 01 10 11 11 01 00 01): la solución está sólo en una imagen. Recalculado por enumeración con los generadores que declara ($g_1 = 101$, $g_2 = 111$), el camino de máxima verosimilitud es û = 11000 (+00), con 4 discrepancias, que es más de lo que garantiza $d_{free} = 5$. Con el orden invertido (111/101) da 10011 (+00) con 3. No se puede saber cuál muestra la figura. Para estudiar, usar el Ejercicio 3.
- **Notación**: en la U3, m = información y n = total. El informe usa (n, r), k y m indistintamente. En el final, aclarar la notación al empezar.
- Conocimiento general agregado: G/H desde g y h, LFSR, propiedades de CRC, parámetros BCH/RS, criterio del mcd, árbol y tabla de transiciones.
- ⚠️ No hay apunte de la cátedra sobre cíclicos y convolucionales en `fuentes/teoria/`. Todo sale del informe del grupo y de conocimiento general. Confirmar con Medín qué nivel piden (¿división polinómica y Viterbi a mano o sólo conceptos?).

#### Fuentes
- `fuentes/cursada-2025/drive-propio/Tps Medin/INFORME N2 TEORIA- CÓDIGOS CORRECTORES DE ERROR- Códigos Cíclicos – Códigos Convolucionales.md`, incluido el anexo de autoevaluación de 10 preguntas.
- `fuentes/practica/Ejercitación Códigos extra.md` (ejercicio del código cíclico con $g(x) = 1 + x + x^2$).
- Ejemplo de CRC: Tanenbaum, *Redes de computadoras* (conocimiento general).

### Unidad 9 — Internet de las cosas (IoT) y seguridad en la transmisión de datos

#### Conceptos clave
- **IoT**: objetos con sensores, software y conectividad que recopilan y comparten datos por la red de forma autónoma. Origen: Kevin Ashton, RFID en la cadena de suministro de Procter & Gamble (1999, año: conocimiento general).
- **Impulsores**: conectividad ubicua y barata, adopción de IP, más cómputo con menos consumo, miniaturización, analítica y nube.
- **Arquitectura**: percepción → red → aplicación (el modelo mínimo; hay de 4, 5 y 7 capas).
- **Servicios de seguridad**: confidencialidad, integridad, autenticación y no repudio (los 4 de la PKI), más disponibilidad.
- **Criptografía** (protocolos, algoritmos y hashes) ⊃ **cifrado** (texto plano ↔ cifrado con clave).
- **Simétrica**: un secreto compartido (DES, AES). **Asimétrica**: un par pública/privada; lo que cifra una lo descifra la otra.
- **Hash**: resumen de longitud fija. **MAC**: hash con clave compartida. **Firma digital**: hash cifrado con la privada del emisor.
- **PKI / X.509 / AC**: el certificado asocia una clave pública con una identidad y lo firma una Autoridad de Certificación. **TLS**: canal seguro (HTTPS). **VPN**: túnel cifrado sobre una red pública.

#### Desarrollo

##### A. Internet de las cosas

| Rama de aplicación | Ejemplos del informe |
|---|---|
| Consumo | domótica (HomeKit, Echo, Home Assistant), vestibles, asistencia a adultos mayores |
| Comercial | IoMT médica (monitoreo remoto, camas inteligentes), transporte (telepeaje, flotas) |
| Industrial (IIoT) | agricultura de precisión, manufactura (mantenimiento predictivo), marítima (Sigfox) |
| Infraestructura | ciudad inteligente (Songdo), red eléctrica inteligente / AMI, iluminación remota |
| Militar | reconocimiento y vigilancia (radar Xaver 1000) |

| Capa | Función |
|---|---|
| Percepción | sensores (temperatura, humo, presencia) y actuadores |
| Red | lleva los datos a Internet por una pasarela (Wi‑Fi, celular o cableada) |
| Aplicación | servicios: hogar, ciudad o fábrica inteligente |

**Tecnologías de comunicación.** Datos del informe N° 4; *(cg)* = conocimiento general.

| Tecnología | Banda | Alcance | Velocidad | Rasgo |
|---|---|---|---|---|
| RFID | LF/HF/UHF *(cg)* | cm–m | baja | tag (chip + antena) + lector + host; anticolisión |
| NFC | 13,56 MHz | pocos cm | ≤ 424 kbit/s | sin emparejamiento; tags pasivos; pagos |
| BLE | 2,4 GHz | ~10 m | ~1,4 Mbps (LE 2M) | punto a punto, broadcast, malla; años con una pila |
| Zigbee | 2,4 GHz | 75–100 m en interiores | ≤ 250 kbps | **malla** con coordinador/router/dispositivo final; 65 000 nodos; AES‑128 |
| Z‑Wave | < 1 GHz | 100 m | 40–100 kbps | malla propietaria; 232 nodos, 4 saltos |
| Wi‑Fi 6 | 2,4/5/6 GHz | decenas de m | alta | TWT: despierta sólo para recibir |
| LoRaWAN / Sigfox / NB‑IoT *(cg)* | sub‑GHz / celular | km | kbps o menos | LPWAN; LoRaWAN cifra con AES (informe N° 5) |

**Protocolos de aplicación** (la seguridad es del informe N° 5; el resto *(cg)*):

| | MQTT | CoAP |
|---|---|---|
| Modelo | publicación/suscripción vía *broker* | cliente/servidor REST |
| Transporte | TCP | UDP |
| Seguridad | no trae; **TLS** + usuario/contraseña o certificados | **DTLS** |

**Sistemas embebidos.** Hardware y software dedicados a una función, con recursos limitados, bajo costo y bajo consumo. Componentes: microcontrolador (CPU + RAM + ROM + periféricos), E/S, sensores, actuadores, PCB, SO y aplicación. **Arduino**: placa libre con microcontrolador, para prototipar. **Raspberry Pi**: una computadora completa con GNU/Linux.

**Cloud.**
- Relación con el IoT: el IoT genera volúmenes masivos de datos y la nube los almacena y procesa de forma escalable y bajo demanda.
- Modelos de servicio: **SaaS** (la aplicación; capa alta), **PaaS** (la plataforma de desarrollo) e **IaaS** (servidores, disco y red; capa baja).
- Despliegue: pública, privada, híbrida y comunitaria.
- Contras: depende de la conexión y los datos quedan fuera del control del usuario.
- **Edge computing**: procesar cerca de la fuente, con menos latencia y menos tráfico.

**Analítica.** Bodega de datos, dashboards, alertas y KPIs. Permite decidir en tiempo real y anticiparse a los problemas (mantenimiento predictivo), con cuestiones éticas de consentimiento.

**Internet vs Web.** Internet es la red física que transporta los datos; la Web es una capa de aplicación encima. Fases de la Web: investigación → *brochureware* → transaccional → social. Siguiendo a Evans (Cisco), el IoT sería "la primera evolución real de Internet".

**Retos.**
- **IPv6**: direcciones para miles de millones de sensores, con una coexistencia con IPv4 costosa que no da seguridad por sí sola.
- **Energía**: sensores autosuficientes (piezoeléctricos, solares, eólicos).
- **Estándares e interoperabilidad**.
- **Disponibilidad**.
- **Almacenamiento y procesamiento** (big data, IA).
- **Seguridad y privacidad**.

##### B. Seguridad en la transmisión de datos

| Servicio | Mecanismo |
|---|---|
| Confidencialidad | cifrado (simétrico para los datos) |
| Integridad | hash / MAC |
| Autenticación | certificados, desafío‑respuesta, MAC |
| No repudio | **firma digital**; un MAC no alcanza porque la clave es compartida *(cg)* |

| | Simétrica | Asimétrica |
|---|---|---|
| Claves | un secreto compartido | par pública/privada |
| Velocidad | alta | lenta *(cg)* |
| Problema | **distribuir la clave** | saber que la pública es de quien dice ser → PKI |
| Ejemplos | DES (56 bits, inseguro *(cg)*), AES | RSA (PKCS#1), curvas elípticas *(cg)* |
| Uso | cifrar los datos | cifrar con la **pública del destinatario**; firmar con la **privada del emisor** |

**Sobre digital (esquema híbrido).** Los datos se cifran con una clave simétrica y esa clave se cifra con la pública de cada destinatario: una copia de los datos y n copias de la clave. Es lo que hace TLS. El informe recomienda **dos pares de claves por usuario**: uno de firma, sin copia, y uno de cifrado, con respaldo, porque si se pierde la privada de cifrado lo cifrado no se recupera.

**Hash.** Propiedades *(cg)*: longitud fija, unidireccional, resistente a colisiones.

| Algoritmo | Salida | Estado |
|---|---|---|
| MD5 (1992) | 128 bits | colisiones conocidas → no usar |
| SHA‑1 (1995) | 160 bits | vulnerable |
| SHA‑2 (2001) | 224–512 bits | seguro |
| RIPEMD‑160 | 160 bits | se usa en Bitcoin |

Usos:
- contraseñas guardadas hasheadas;
- **checksums** de descargas (integridad);
- **blockchain**: cada bloque guarda el hash del anterior, así que alterar uno obliga a rehacer todos los siguientes; la prueba de trabajo y la mayoría de los nodos lo impiden.

Vínculo con la U8 *(cg)*: un **CRC** detecta errores accidentales, pero no manipulación, porque cualquiera lo recalcula. Para eso hace falta un MAC o una firma.

**MAC**: CBC‑MAC (último bloque de un cifrado CBC), **HMAC** (hash + clave; HMAC‑SHA‑256) y UMAC (hash universal).

**PBKDF** (lentos a propósito, contra la fuerza bruta en GPU): PBKDF2 (itera un hash), bcrypt (Blowfish), scrypt (mucha RAM) y Argon2 (ganador de la Password Hashing Competition).

**Firma digital.**
1. El emisor calcula h = hash(M), cifra h con su privada y envía M + firma.
2. El receptor recalcula hash(M), descifra la firma con la pública del emisor y compara.
3. Si coinciden, quedan verificados el origen y la integridad.

**Desafío‑respuesta.** A manda un desafío; B lo devuelve cifrado con su privada; si A, al descifrarlo con la pública de B, recupera el desafío, B queda autenticado.

**PKI.**
- **Certificado X.509**: sujeto (identificado por un **DN** único), su clave pública, la AC emisora y la validez, todo **firmado por la AC**.
- **Componentes**:
  - **Documento de prácticas de certificación**: público; rige el ciclo de vida.
  - **AC**: firma certificados y **CRL**. Su privada está en un **HSM**, en una red aislada; la AC raíz es la única **autofirmada**.
  - **Autoridad de Registro**: es la interfaz con el exterior; verifica la identidad y pide la emisión o la revocación.
  - **Directorio**: LDAP sobre SSL/TLS.
- **Confianza**: se instala el certificado de la AC y con él se verifican las firmas (las AC raíz de los navegadores).
- **PKCS**: #1 = RSA, #7 = mensajes, #11 = dispositivos criptográficos.

**SSL/TLS.**
- **Historia**: Netscape creó SSL en 1994 (la 1.0 no se publicó; siguieron 2.0 y 3.0). TLS deriva de SSL 3.0. El RFC 7568 (2015) declaró obsoleto SSL 3.0. TLS 1.3: RFC 8446, **2018**.
- **Qué protege**: los datos **en tránsito**, no en los extremos.
- **Handshake** (simplificado):
  1. El cliente ofrece versiones y suites de cifrado.
  2. El servidor elige una y manda su **certificado**, que contiene su clave pública.
  3. El cliente lo valida contra las AC en las que confía y genera el secreto. En TLS ≤ 1.2 con RSA lo cifra con la pública del servidor.
  4. Los dos derivan el **secreto maestro** y las claves de sesión simétricas.
  5. Intercambian *Finished* cifrados; desde ahí, datos cifrados con MAC/AEAD.
- **TLS 1.3** *(cg)*: sólo (EC)DHE, con secreto hacia adelante; 1 RTT; el certificado va cifrado.

**VPN.**
- Túnel cifrado **cliente VPN ↔ servidor VPN** sobre Internet; red virtual (enlaces lógicos) y privada.
- Usos: acceso remoto, teletrabajo, unir sedes sin enlaces dedicados.
- Protocolos: PPTP (obsoleto *(cg)*), L2TP (encapsula; cifra con IPsec) e **IPsec** (autentica y cifra paquetes IP, gestiona claves); *(cg)* OpenVPN y WireGuard.
- Seguridad: autenticación fuerte y chequeo del estado del equipo remoto.

**Seguridad en IoT.**
- Por qué es débil: los dispositivos priorizan la función, tienen poca CPU y memoria, hay muchísimos (gran superficie de ataque) y suelen no tener cifrado ni autenticación.
- Amenazas: MitM, suplantación, manipulación de comandos, DDoS.
- Protocolos: MQTT+TLS, CoAP+DTLS, LoRaWAN (AES), Zigbee (AES‑128 y autenticación mutua).

**Man in the Middle.**
- Fases: intercepción (Wi‑Fi pública o falsa) → lectura y modificación si el tráfico no va cifrado → suplantación.
- Prevención según el informe: desconfiar del Wi‑Fi, instalar software de fuentes conocidas y usar antivirus (detecta el envenenamiento ARP).
- Defensa de fondo *(cg)*: **TLS con validación de certificados**.

**Metadatos** *(cg; el título del informe los nombra, pero no los desarrolla)*:
- TLS oculta el contenido, pero no las IPs, puertos, tamaños y tiempos, ni el nombre del sitio en el SNI (salvo ECH).
- Una VPN oculta el destino al ISP, pero no al proveedor de la VPN.
- Para ocultar quién habla con quién hace falta algo como Tor.

#### Preguntas tipo
Respuestas cortas, a partir de los anexos de autoevaluación de los informes N° 4 y N° 5.

**IoT**
1. *¿Concepto básico de IoT?* Interconexión de objetos cotidianos por la red, que recopilan y comparten datos de forma autónoma.
2. *¿Ramas de aplicación?* Consumo, comercial, industrial, infraestructura y militar.
3. *¿Diferencia entre Internet y la Web?* Internet es la red de routers y enlaces que transporta datos. La Web es una capa de aplicación encima, que hace accesibles esos datos.
4. *¿Por qué IPv6 en IoT?* El pool de IPv4 se agotó y cada sensor necesita una dirección única. IPv6 agrega espacio de direcciones casi ilimitado y autoconfiguración.
5. *¿Desafío energético?* Que los sensores sean autosuficientes (vibración, sol, viento), porque cambiar pilas en miles de dispositivos no escala.
6. *¿Características de un sistema embebido?* Función específica, sensores y actuadores, recursos limitados, tamaño chico, bajo costo y bajo consumo.
7. *¿Importancia de Arduino?* Es una plataforma abierta y barata para prototipar dispositivos que leen sensores, procesan y se comunican, con mucha comunidad y documentación.
8. *¿Relación cloud–IoT?* El IoT genera volúmenes masivos de datos y la nube los almacena y procesa de forma escalable y accesible bajo demanda.
9. *¿Fases de la Web?* Investigación → brochureware → transaccional → social.
10. *¿Qué es RFID y cómo se compone?* Identificación por radiofrecuencia con un chip y antena en lugar de un código impreso. Se compone de tags (transponders), lectores/escritores con antena y un host con software.

**Seguridad**
1. *¿Criptografía vs cifrado?* La criptografía es el campo (protocolos, algoritmos, hashes para proteger mensajes). El cifrado es la operación de pasar de texto plano a cifrado y volver con la clave.
2. *¿Cuándo simétrica y cuándo asimétrica?* Simétrica para el volumen de datos, por velocidad. Asimétrica para intercambiar claves y para firmar, porque no exige compartir la privada. En la práctica se combinan (sobre digital, TLS).
3. *¿Desafío‑respuesta?* Se manda un desafío y el otro lo devuelve cifrado con su privada. Si al descifrarlo con su pública aparece el desafío original, queda identificado.
4. *¿Qué es un hash y para qué sirve?* Un resumen de longitud fija. Sirve para verificar integridad y, cifrado con la privada del emisor, es la firma digital.
5. *¿Qué es un MAC y qué tipos hay?* Un hash con clave compartida que da integridad y autenticidad. Tipos: CBC‑MAC, HMAC y UMAC.
6. *¿PBKDF comunes?* PBKDF2, bcrypt, scrypt y Argon2.
7. *¿Dos usos del hashing?* Checksums de descargas y blockchain (además, almacenar contraseñas).
8. *¿Qué es una PKI?* El conjunto de hardware, software, personas, políticas y procedimientos para crear, gestionar, distribuir y revocar certificados de clave pública.
9. *¿Los 4 aspectos que aborda la PKI?* Confidencialidad, autenticación, integridad y no repudio.
10. *¿Por qué HTTP no es seguro y qué protocolos lo resuelven?* Viaja en texto plano y se puede interceptar. SSL y su sucesor TLS lo resuelven (HTTPS).

#### Dudas / pendientes
- **Errores del informe N° 4**:
  - Arduino: "todas son AVR de Atmel" es falso. Due usa ARM SAM3X, Nano 33 BLE usa nRF52840 y Uno R4 usa Renesas RA4M1.
  - El agotamiento de IPv4 en IANA fue el **3/2/2011**, no en "febrero de 2010".
  - "25 billones" de dispositivos y "4–5 trillones" de dólares son calcos del inglés: son **miles de millones** y **billones**.
  - "Wi‑Fi 6, la última versión": ya existe Wi‑Fi 7.
  - Zigbee: en 2,4 GHz son 250 kbps; 20 y 40 kbps corresponden a 868 y 915 MHz.
  - Usa "IoMT" para el IoT médico y también para el militar (el militar suele llamarse IoBT).
  - "Facebook = nube comunitaria" y "AWS = nube híbrida" son ejemplos dudosos: AWS es pública.
  - La "historia de los embebidos" (ferias de 1934 y 1938) es historia de la domótica.
  - Dice que la capa de aplicación "garantiza confidencialidad e integridad" y que la de red "digitaliza". La seguridad atraviesa todas las capas y la conversión analógico-digital ocurre en la percepción.
- **Errores del informe N° 5**:
  - TLS 1.3 es de **2018** (RFC 8446), no de 2020.
  - **NAT** no es un protocolo de VPN y no "asigna IPs dinámicas" (eso es DHCP).
  - Bajo "vulnerabilidades de SSL" lista ventajas de TLS. Vulnerabilidades reales *(cg)*: POODLE, BEAST y Heartbleed (bug de OpenSSL).
  - "Versiones basadas en MD4 (como SHA‑2) son seguras" es confuso: MD4 está roto.
  - Presenta MD5 y SHA‑1 como "los más utilizados" sin advertir que no sirven para firmas.
  - El paso 3 del handshake está confuso ("se ofrece a verificar la clave privada") y describe el intercambio RSA, que TLS 1.3 eliminó.
  - "La asimétrica es la más segura" es engañoso: depende del algoritmo y la clave, y en la práctica se usa en esquema híbrido.
  - "La simétrica brinda cierta autenticidad": sin MAC, no la garantiza.
  - "Maximizar la velocidad" como razón de una VPN: el túnel agrega overhead.
  - "Firmar = cifrar con la privada" vale para RSA, no para ECDSA.
- **Hueco del informe N° 5**: la "encriptación de los metadatos" del título no se desarrolla. Lo de Desarrollo es conocimiento general.
- ⚠️ No hay apunte de cátedra de estos temas. Si el final de regulares es "sobre el 100 % de los informes", probablemente entren como preguntas conceptuales. Confirmar con la cátedra.

#### Fuentes
- `fuentes/cursada-2025/drive-propio/Tps Medin/INFORME N4- INTERNET DE LAS COSAS (IoT).md`, con el anexo de 10 preguntas.
- `fuentes/cursada-2025/drive-propio/Tps Medin/INFORME N5- SEGURIDAD EN LA TRANSMISIÓN DE DATOS.md`, con el anexo de 10 preguntas.

## Log
- 2026-11-24: Alta de la materia (código CD). Se bajó el Drive de la facu (`3º AÑO/Comunicación de Datos`, 102 archivos) a `archivo/`. Las unidades salen de la teoría de la cátedra y del final de 2025. Todavía no se ingirió nada.
- 2026-11-24: Ingesta de la teoría, la práctica, los resúmenes (incluido *El Santo Resumen*) y los finales. Desarrollo completo de las Unidades 4–7 (comunicaciones digitales, PCM y ADSL; medios y elección del medio de acceso; asignación de capacidad y colas; OSI/TCP-IP), con ejercicios del final 2025 resueltos. Erratas de las fuentes anotadas en Dudas: el ancho de banda PCM con $f_{min}$ (2·fmax vs fmax−fmin), W del ejemplo 3 del apunte de colas y I del ej. 2 de la práctica de multinivel.
- 2026-11-24: Desarrollo completo de las Unidades 1–3 (teoría de la información y canales; codificación, Kraft, Huffman, cota de longitud media; paridad, Hamming y códigos lineales con síndrome y familias). Erratas de las fuentes anotadas en Dudas: síndromes mal rotulados en el ej. 1 de *Ejemplos Códigos Lineales*, H(A,B) del BSC en la práctica resuelta y Kraft como condición «necesaria» en un resumen.
- 2026-11-24: `estudio/final/banco-preguntas-teoria.md` — banco de teoría de los finales (6 finales 2020–2025 + preguntas frecuentes + teoría vieja): 29 entradas por tema, respondidas, con tabla de frecuencia. Kraft, cota de longitud media y elección del medio de acceso salen en los 6 finales. 16 errores corregidos en las soluciones de alumnos.
- 2026-11-24: `estudio/final/banco-ejercicios.md` — banco de práctica de los finales 2011–2025 y de los finales viejos, agrupado por tipo (multinivel, TDM‑PCM, colas, FDM, códigos compactos y lineales, BSC, Hamming, capacidad), con receta, ejercicios resueltos y trampas. En 2020–2025 se repiten multinivel, TDM‑PCM y BSC/colas. Unidad 4: anotada la diferencia entre $B_w = 1/\tau$ y $B = s/2$.
- 2026-11-24: `estudio/final/resumen-final.md` + pdf (35 págs.) — resumen para el final ordenado por prioridad, con los 3 problemas y las 3 preguntas del final 2025 resueltos, hoja de fórmulas y 17 figuras (`figs/cd-*.png`, de `scripts/cd/cd-figs-final.py`).
- 2026-11-24: `estudio/final/podcasts/` — 8 fuentes para NotebookLM (de `scripts/cd/cd-podcasts.py`, a partir del resumen y los bancos) + README con los prompts por episodio.
- 2026-11-26: Ingesta de los mails de la cursada 2025 (comisión 303, Medín y Baró) en `fuentes/cursada-2025/`: presentación y condiciones, prácticas de Baró (multinivel, velocidades y capacidad) y de Medín (codificación, asignación de capacidad, teoría de colas). Encabezado de la wiki: cátedra, condiciones, informes 2025 (incluyen códigos cíclicos y convolucionales, IoT y seguridad, que no están en la wiki) y temario de los parciales. Ojo: *Ejercicio de Teoría de Colas* escribe ρ = μ/λ, cuando es ρ = λ/μ (el valor 0,8 está bien). *ejercicios teoria de colas.pdf* es un escaneo sin texto.
- 2026-11-26: Unidades nuevas 8 (códigos cíclicos y convolucionales: g(x), síndrome por resto, CRC, convolucional R=1/2 K=3, trellis, Viterbi) y 9 (IoT y seguridad: capas, tecnologías, MQTT/CoAP, criptografía, PKI, TLS, VPN), sacadas de los informes 2, 4 y 5 de la cursada 2025. Errores de los informes anotados en Dudas: el ejemplo de Viterbi del informe 2 no sirve para estudiar. Ninguno de los dos temas tiene apunte de cátedra.
- 2026-11-26: `estudio/final/banco-preguntas-teoria.md` ampliado con la cursada 2025: el multiple choice de medios del 2do parcial de Baró (34 ítems; la marca de VSAT estaba mal, porque es *Aperture*), una sección de atenuación, dB y S/R, preguntas nuevas de información, modulación, colas y segurización, y la columna "cursada 2025" en la tabla de frecuencia.
- 2026-11-26: `estudio/final/banco-ejercicios.md` ampliado con las prácticas de la cursada 2025: 16 ejercicios resueltos nuevos (M/M/2, modelo cerrado N* = 5,5, costos obrero x/y, 4 concentradores con Tmin = 8,46 ms, Huffman cuaternario con 2 símbolos fantasma, multinivel y TDM de Baró), sección nueva de atenuación y dB, recetas de colas y capacidad ampliadas, y la columna "cursada 2025" en la tabla de frecuencia. Errores de las fuentes en Dudas 31–47.
- 2026-11-26: `estudio/final/apuntes-podcasts/02-transmision-multinivel.md` + pdf — apunte en limpio del podcast 2 (idea, R/r/s con la teleimpresora de Baró, receta, final 2025 resuelto, variante de duplicar R, errores típicos y autoevaluación).
