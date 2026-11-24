# Comunicación de Datos — Banco de ejercicios de finales (práctica)

Banco armado con **todos** los enunciados de práctica de finales que hay en `fuentes/finales/Práctica/` (2011–2025) y en el PDF «Comunicaciones - Finales Viejos» (finales del plan viejo, cátedra Di Santo, ~2000–2006). Cada número está verificado con Python.

**Convenciones**

- $\lg x = \log_2 x$. En la calculadora: $\lg x = \ln x/\ln 2 \approx 3{,}32\,\log_{10} x$.
- Método de la cátedra: «Práctica - Fórmulas y pasos para los ejercicios» (Joel Arnold, 2020, **no oficial**), más los apuntes resueltos de práctica. Cuando algo sale de otro lado lo marco como *(conocimiento general)*. Cuando el método del «Santo Resumen» o de las resoluciones de alumnos difiere, queda anotado en «Dudas / pendientes» (al final).
- «F1»…«F13» son los «Examen Final N°k» del PDF de finales viejos (sin fecha). Las demás hojas viejas se citan por la fecha impresa.
- Los finales 2011–2021 y los viejos son del plan anterior. El único del plan actual es el del **04/04/2025**, y dos de sus tres problemas repiten números de 2021.

---

## Tabla de frecuencia

| Tipo de ejercicio | Finales 2011–2025 | Finales viejos (plan anterior) | Total |
|---|---|---|---|
| §1. Transmisión multinivel ($M(T)$, $I$, $R$, $r$, $s$, duplicar $R$) | 18/02/2011, 09/03/2012, 13/03/2015, 15/02/2017, 28/08/2020, 23/10/2020, 20/11/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021, **04/04/2025** | F2, F6, F9 (×2), F10, 29/11/2002, ¿07/02/2005?, 25/02/2005, 23/09/2005, 22/12/2005, 03/03/2006 | **23** |
| §6. TDM – PCM (ancho de banda de la trama) | 09/03/2012, 13/03/2015, 18/12/2015, 21/02/2020, 28/08/2020, 23/10/2020, 20/11/2020, 18/12/2020, 10/09/2021, 19/11/2021, **04/04/2025** | F1, F4, F7, F12, 17/02/2006, 03/03/2006, sin fecha (pág. 22) | **18** |
| §8. Teoría de colas M/M/1 | 18/02/2011, 20/11/2020, 18/12/2020, 19/11/2021, 17/12/2021, **04/04/2025** | F1, F2, F4, F6, F13, 29/11/2002, 07/05/2004, 22/12/2005, 17/02/2006 | **15** |
| §7. FDM (cantidad de señales, ancho de banda, portadoras) | 18/02/2011, 04/12/2015, 15/02/2017, 28/08/2020 | F3, F6, F8, F9, F13, ¿07/02/2005?, 25/02/2005, 23/09/2005, 22/12/2005 | **13** |
| §2. Canal binario / ternario (entropías, información mutua) | 04/12/2015, 18/12/2015, 21/02/2020, 23/10/2020, 10/09/2021, 17/12/2021 | F12, sin fecha (pág. 22) | **8** |
| §3. Código compacto (Huffman), L, η, Kraft | 09/03/2012, 13/03/2015 | F3, F13, 29/11/2002, ¿07/02/2005?, 07/05/2004, 23/09/2005, 03/03/2006 | **9** |
| §4. Códigos lineales (H → G → V → síndromes, diseño) | 04/12/2015 | F1, F4, F5, F10, F11, 07/05/2004, 25/02/2005, 17/02/2006 | **9** |
| §5. Hamming | 18/12/2015, 15/02/2017, 21/02/2020 | F8, F12 | **5** |
| §9. Asignación de capacidad / retardo de enlace | — | F3, F10, F11, sin fecha (pág. 22) | **4** |
| §10. Entropía de fuente + Shannon; FSK | — | F5 (×2), F7 | **3** |

**Lectura rápida.** En las 9 hojas de 2020–2025 la práctica sale casi siempre de este menú: **multinivel** (8 de 9), **TDM-PCM** (8 de 9), y un tercer problema que alterna entre **canal binario simétrico** (siempre $P(a_1)=0{,}65$, $P(b_1/a_1)=0{,}75$) y **colas M/M/1** (sala de emergencias o caja única, con números repetidos). Hamming (último: 21/02/2020) y FDM (último: 28/08/2020) no volvieron. Huffman y códigos lineales son casi exclusivos de los finales viejos.

Repeticiones textuales (mismos números):

- Multinivel 13 pulsos × 58 niveles: 23/10/2020 = ejercicio 11 del apunte resuelto de multinivel.
- Multinivel 10 pulsos × 64 niveles: 17/12/2021 = ejercicio 12 del apunte resuelto.
- 15 pulsos (1 binario + 14 de 11 niveles): 18/12/2020 = 19/11/2021.
- CBS 0,65 / 0,75: 18/12/2015, 23/10/2020, 10/09/2021, 17/12/2021.
- Trama PCM 25+2, 400–3500 Hz, 7 dígitos: 19/11/2021 = 04/04/2025.
- Sala de emergencias: 20/11/2020 = 17/12/2021 = 04/04/2025.
- Caja única 7–14 h, 100 personas/día: 19/11/2021 = 18/12/2020 = ejercicio 3 de la práctica de colas.
- 32 señales × 4 kHz × 8 bits: 18/12/2015 = 21/02/2020 = 28/08/2020.
- 22/12/2005 es idéntico a 18/02/2011.

---

## 1. Transmisión multinivel — $M(T)$, $I$, $R$, $r$, $s$

### Receta

Fuente: «Fórmulas y pasos», «2 - Ejercitación Transmisión Multinivel (RESUELTO)», «Resumen 1° Parcial Práctica».

| Magnitud | Fórmula | Unidad |
|---|---|---|
| Mensajes distintos | $M(T)=\mu^{n}=\mu^{t/\tau}$ | mensajes |
| Información | $I=\lg M(T)=n\,\lg\mu$ | bits |
| Tasa de información | $R=\dfrac{I}{T}$ | bps |
| Tasa de dígitos | $r=\dfrac{N}{T}$ | dígitos/s (binits/s) |
| Velocidad de señalización | $s=\dfrac{1}{\tau_{\min}}$ | baudios |

- $\mu$: niveles por pulso; $n$: pulsos **de información**; $N$: pulsos **totales** (con arranque, parada, sincronismo, paridad); $T$: duración **total** del grupo (todos los pulsos); $\tau_{\min}$: el pulso más corto.
- **Varios bloques** con distinta cantidad de niveles: los mensajes se multiplican y la información se suma: $M=M_1\cdot M_2$, $I=n_1\lg\mu_1+n_2\lg\mu_2$.

Pasos:

1. Separá los pulsos en: fijos (arranque, parada, sincronismo, paridad → **no aportan información**, sí tiempo y dígitos) y de información (por bloque, con su $\mu$).
2. Contá niveles: «entre +4 y −4 incluido el 0» son **9** niveles; el 0 cuenta si el enunciado o el gráfico lo incluye.
3. $T=\sum$ duraciones de **todos** los pulsos. Cuidado con las unidades mezcladas (µs y ms).
4. $I=\sum n_i\lg\mu_i$; $R=I/T$; $r=N/T$; $s=1/\tau_{\min}$.
5. **Duplicar (o cuadruplicar) $R$ sin tocar tiempos**: sólo queda aumentar niveles. Planteás $k\cdot R\cdot T = I_{\text{fijo}} + n\lg\mu'$, despejás $\mu'=2^{(\dots)}$ y **redondeás para arriba**. $r$ y $s$ no cambian (mismos pulsos, mismas duraciones).
6. Gráfica: eje $t$ con los pulsos uno al lado del otro, eje de amplitud con los niveles; arranque y parada a su valor fijo, el resto «cualquiera de los $\mu$ niveles» (se dibujan barras de altura variable). Marcar $\tau$ y $T$.

### Ejercicios

#### 1.1 — 23/10/2020 (= ej. 11 del apunte resuelto) — resuelto

> Una transmisión multinivel considera grupos de 13 pulsos de 58 niveles c/u. La transmisión tiene 1 pulso fijo de arranque de +3 V y 1 pulso fijo de stop de −3 V. Cada pulso dura 10 µs. Calcular: a) $M(T)$ e $I_x$; b) $R$; c) gráfica.

1. Pulsos de información $n=13$, $\mu=58$. Pulsos totales $N=15$.
2. $T=15\times10\ \mu s=150\ \mu s$ (arranque y stop **sí** suman tiempo).
3. $M(T)=58^{13}\approx 8{,}41\times10^{22}$ mensajes.
4. $I=13\lg58=13\times5{,}858=76{,}15$ bits.
5. $R=I/T=76{,}15/150\ \mu s=507{,}7$ kbps.
   - El apunte de la cátedra redondea $I$ para arriba a 77 bits y da $R=77/150\ \mu s=513$ kbps. Las dos respuestas salen del mismo planteo; ver Dudas.
6. Gráfica:

```
 +3V ┌──┐                                            
     │A │ ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮   (13 pulsos, cada uno en uno de 58 niveles)
  0 ─┘  └─────────────────────────────┐   ┌──→ t
                                      │ S │
 -3V                                  └───┘
     |10µs|<------- 13 × 10 µs ------->|10µs|
     |<-------------- T = 150 µs ------------>|
```

#### 1.2 — 04/04/2025 (plan actual) — resuelto

> Una transmisión multinivel considera grupos de 27 pulsos de 128 niveles c/u. Tiene 1 pulso fijo de arranque de +4 V y 1 pulso fijo de stop de −4 V. Cada pulso dura 10 µs. Calcular: a) $M(T)$ e $I_x$; b) $R$; c) gráfica.

1. $n=27$, $\mu=128=2^7$, $N=29$.
2. $T=29\times10\ \mu s=290\ \mu s$.
3. $M(T)=128^{27}=2^{189}\approx7{,}85\times10^{56}$ mensajes.
4. $I=27\lg128=27\times7=189$ bits (exacto, sin redondeo).
5. $R=189\ \text{bits}/290\ \mu s=651{,}7$ kbps.
6. Gráfica igual a 1.1 con +4 V / −4 V y 27 pulsos.

#### 1.3 — 15/02/2017 — resuelto (R, r, s y duplicar)

> Transmisión asincrónica: 2 pulsos de arranque de 0,5 µs c/u (valor «1»), 5 pulsos cuaternarios (0,1,2,3) de 1 µs c/u, 3 pulsos binarios de 1 µs c/u y 1 pulso de parada «1» de 1 µs. a) Gráfica. b) $R$. c) $r$. d) $s$. e) Parámetro a modificar para duplicar $R$ sin modificar arranque, parada, binarios ni tiempos. f) ¿Cambian $r$ y $s$?

1. $T=2(0{,}5)+5(1)+3(1)+1=10\ \mu s$; $N=2+5+3+1=11$ pulsos.
2. $I=5\lg4+3\lg2=10+3=13$ bits.
3. b) $R=13/10\ \mu s=1{,}3$ Mbps.
4. c) $r=11/10\ \mu s=1{,}1\times10^6$ dígitos/s.
5. d) $\tau_{\min}=0{,}5\ \mu s\Rightarrow s=2\times10^6$ baudios.
6. e) Sólo se pueden cambiar los niveles de los cuaternarios: $2R\cdot T=26=5\lg\mu+3\Rightarrow\lg\mu=4{,}6\Rightarrow\mu=24{,}25\Rightarrow$ **25 niveles**.
7. f) $r$ y $s$ **no cambian**: misma cantidad de pulsos y mismas duraciones.
8. a) Gráfica: dos pulsos angostos en «1», cinco pulsos de 1 µs en alguno de 4 niveles, tres de 1 µs en 0/1, parada en «1».

#### 1.4 — 09/03/2012 — resuelto (R, r, s y duplicar con dos alternativas)

> Bloques de: un dígito de arranque «1» de 0,5 µs, dos dígitos de 8 niveles de 1 µs c/u, cinco dígitos cuaternarios de 2 µs c/u, dos dígitos binarios de 1 µs c/u y un dígito de parada «0» de 3,5 µs. a) Tasa de dígitos, tasa de información y velocidad de señalización. b) Cómo aumentar la velocidad al doble sin tocar comienzo, fin, ni los dígitos de 8 niveles ni los binarios.

1. $T=0{,}5+2(1)+5(2)+2(1)+3{,}5=18\ \mu s$; $N=11$.
2. $I=2\lg8+5\lg4+2\lg2=6+10+2=18$ bits.
3. $r=11/18\ \mu s=611{,}1\times10^3$ dígitos/s; $R=18/18\ \mu s=1$ Mbps; $s=1/0{,}5\ \mu s=2$ Mbaudios.
4. b) Sólo se pueden tocar los cinco cuaternarios. Dos caminos:
   - **Más niveles, mismos tiempos**: $36=8+5\lg\mu\Rightarrow\lg\mu=5{,}6\Rightarrow\mu=48{,}5\Rightarrow$ **49 niveles**.
   - **Mismos niveles, pulsos más cortos** (el enunciado no prohíbe tocar la duración de los cuaternarios): $T'=18/2\ \text{Mbps}=9\ \mu s$; lo fijo suma $0{,}5+2+2+3{,}5=8\ \mu s$, quedan 1 µs para 5 pulsos → **0,2 µs cada cuaternario**. Ojo: entonces $s$ sube a $1/0{,}2\ \mu s=5$ Mbaudios.

#### 1.5 — 28/08/2020 — resuelto

> 2 pulsos de arranque (+5 V y −5 V), 9 pulsos de datos de 128 niveles c/u, 1 pulso de stop (+2 V). Todos duran 2 ms, excepto el stop que dura 4 ms. a) $R$. b) Si los 9 de datos pasan a binarios, nueva $R$ sin cambiar duraciones.

1. $T=2(2)+9(2)+4=26$ ms.
2. a) $I=9\lg128=63$ bits; $R=63/26\ \text{ms}=2423$ bps.
3. b) $I=9$ bits; $R=9/26\ \text{ms}=346{,}2$ bps.

#### Resto de los multinivel (enunciado + resultados)

| Origen | Enunciado (resumido) | Resultados |
|---|---|---|
| 10/09/2021 | 1 arranque fijo, 10 datos de 128 niveles, 1 stop; todos 5 ms salvo stop 7 ms. a) $R$; b) datos binarios. | $T=62$ ms; $I=70$ bits; $R=1129$ bps. b) $I=10$ bits, $R=161{,}3$ bps. |
| 17/12/2021 (= ej. 12 apunte) | 10 pulsos de 64 niveles, sin control, 2 ms c/u. a) mensajes; b) $I_x$; c) $R$; d) gráfica. | $M=64^{10}=2^{60}\approx1{,}15\times10^{18}$; $I=60$ bits; $T=20$ ms; $R=3$ kbps. |
| 20/11/2020 (= ej. 8 apunte + R) | 5 pulsos de igual duración: el 1° binario, el resto cualquier nivel entre +4 y −4 con 0. a) mensajes; b) $R$; c) todos binarios. | $\mu=9$; $M=2\cdot9^4=13122$; $I=\lg13122=13{,}68$ bits. **No se da $\tau$**: $R=13{,}68/(5\tau)=2{,}736/\tau$ bps. c) $I=5$ bits, $R=1/\tau$. (Si fuese binario: $\lceil13{,}68\rceil=14$ pulsos para igualar los mensajes, como en el apunte.) |
| 18/12/2020 = 19/11/2021 | 15 pulsos de igual duración: el 1° binario, el resto entre +5 y −5 con 0. a) mensajes; b) $R$; c) los multinivel pasan a binarios. | $\mu=11$; $M=2\cdot11^{14}\approx7{,}59\times10^{14}$; $I=1+14\lg11=49{,}43$ bits. Sin $\tau$: $R=49{,}43/(15\tau)=3{,}295/\tau$. Con $\tau=1\ \mu s$ (supuesto del alumno de 18/12/2020): $R=3{,}295$ Mbps. c) $I=15$ bits, $R=1/\tau$ (1 Mbps con $\tau=1\ \mu s$). |
| 18/02/2011 = 22/12/2005 = F10 | Carácter de impulsos de 8 niveles equiprobables (8,6,…,−6), duración 12 ms. a) pulsos si $R=1{,}5$ kbps; b) duración de cada impulso; c) capacidad mínima. | $I=R\,T=18$ bits; $n=18/\lg8=6$ pulsos; $\tau=2$ ms; $C_{\min}=R=1{,}5$ kbps. (Coincide con la «Rta» impresa.) |
| F2 / 29/11/2002 | 6 pulsos: 1° arranque «1», último parada «0», el resto 4 niveles equiprobables. Cada pulso 2 ms (2 µs en 2002) salvo el 1° de 5 ms (5 µs). $r$, $R$; duplicar $R$ sin variar tiempos. | $T=15$ ms; $N=6$; $r=400$ dígitos/s; $I=4\lg4=8$ bits; $R=533{,}3$ bps (en µs: $r=400\times10^3$/s, $R=533{,}3$ kbps). Duplicar: $4\lg\mu=16\Rightarrow\mu=16$ niveles. |
| 13/03/2015 / ¿07/02/2005? | 6 pulsos binarios: inicio «1» de 30 µs, 4 de información de 20 µs, parada «1» que dura el doble que los de información. 1) $R$. 2) Cuadruplicar $R$ con las mismas duraciones. | $T=30+80+40=150\ \mu s$; $I=4$ bits; $R=26{,}67$ kbps. Cuadruplicar: $4\lg\mu=16\Rightarrow\mu=16$ niveles. |
| 25/02/2005 / F6 | 8 pulsos de igual duración (1,25 ms); el 1° siempre «1», el resto binarios equiprobables. $R$; cuadruplicar sin tocar tiempos. | $T=10$ ms; $I=7$ bits; $R=700$ bps. Cuadruplicar: $7\lg\mu=28\Rightarrow\mu=16$ niveles. |
| 03/03/2006 | Arranque «1» de 5 µs, 2 cuaternarios de 10 µs, 6 dígitos de 8 niveles de 10 µs, 3 de parada (nivel «2») que suman 15 µs. $s$, $r$, $R$; duplicar $R$ sin variar duraciones ni los cuaternarios. | $T=100\ \mu s$; $N=12$; $s=200$ kbaudios; $r=120\times10^3$ dígitos/s; $I=4+18=22$ bits; $R=220$ kbps. Duplicar: $6\lg\mu=40\Rightarrow\mu=101{,}6\Rightarrow$ **102 niveles**. |
| F9 P2 | 14 pulsos: 1 arranque, 1 sincronismo, 9 datos, 1 paridad, 2 parada. Todos 25 ms salvo el arranque de 30 ms. Velocidad de dígitos, de señalización y $R$. | $T=30+13(25)=355$ ms; $r=14/0{,}355=39{,}44$ dígitos/s; $s=1/25\ \text{ms}=40$ baudios; datos binarios (supuesto) → $I=9$ bits, $R=25{,}35$ bps. La paridad no agrega información nueva. |
| F9 P3 | Canal digital, mensajes de 8 bits, $\tau=4$ ms. a) mensajes distintos y $R$. b) 1° pulso fijo 1,5 V, los otros 7 cualquier entero entre −2 y +4 (con 0). Mensajes, $R$ y conclusiones. | a) $M=256$; $T=32$ ms; $R=8/32\ \text{ms}=250$ bps. b) $\mu=7$; $M=7^7=823543$; $I=7\lg7=19{,}65$ bits; $R=614{,}1$ bps. Conclusión: aun perdiendo un pulso en sincronismo, más niveles por pulso dan más del doble de $R$ con el mismo $\tau$. |
| 23/09/2005 | Transmisión binaria de $T=100$ ms con $\tau=0{,}05$ ms. a) Niveles necesarios para mandar el mismo mensaje en 40 ms sin acortar $\tau$. b) Con 8 niveles, ¿qué $\tau$ mantiene $T=40$ ms? Misma información. | $I=100/0{,}05=2000$ bits. a) En 40 ms entran 800 pulsos: $800\lg\mu=2000\Rightarrow\mu=2^{2{,}5}=5{,}66\Rightarrow$ **6 niveles**. b) $2000/3=666{,}7\Rightarrow667$ pulsos; $\tau=40/667=0{,}0600$ ms ≈ 60 µs. |

### Trampas frecuentes

- **$T$ incluye arranque, parada y todo pulso de control**; $I$ no. Error típico: dividir $I$ por el tiempo de los pulsos de información solamente.
- Contar mal los niveles: «entre +5 y −5 incluido el 0» son 11, no 10.
- $s$ usa el pulso **más corto**, aunque sea el de arranque.
- Redondear niveles **hacia arriba** (con menos no se alcanza la $R$ pedida).
- Si el enunciado no da $\tau$, dejá $R$ en función de $\tau$ y aclaralo; no inventes un valor sin decirlo.
- El ejercicio 2 del apunte resuelto tiene un error: escribe $I=\lg7^6=2{,}81$ bits (es $\lg7$). Lo correcto es $I=6\lg7=16{,}84$ bits y $R=168{,}4$ bps.

---

## 2. Canal binario simétrico y canal ternario — entropías e información mutua

### Receta

Fuente: «Fórmulas y pasos», «1 - Información, Codificación y Canales».

| Paso | Fórmula |
|---|---|
| Matriz del CBS | $P(b_1/a_1)=P(b_2/a_2)=p$, $P(b_2/a_1)=P(b_1/a_2)=1-p$ |
| Probabilidad de salida | $P(b_j)=\sum_i P(a_i)\,P(b_j/a_i)$ |
| Conjunta | $P(a_i,b_j)=P(a_i)\,P(b_j/a_i)$ |
| Hacia atrás (Bayes) | $P(a_i/b_j)=\dfrac{P(a_i)\,P(b_j/a_i)}{P(b_j)}$ |
| Entropía de entrada | $H(A)=\sum_i P(a_i)\lg\dfrac{1}{P(a_i)}$ |
| Entropía de salida | $H(B)=\sum_j P(b_j)\lg\dfrac{1}{P(b_j)}$ |
| Entropía del canal (equivocación de B respecto de A) | $H(B/A)=\sum_i\sum_j P(a_i)\,P(b_j/a_i)\lg\dfrac{1}{P(b_j/a_i)}$ |
| Información mutua | $I(A,B)=H(B)-H(B/A)$ [bits/símbolo] |

Atajo útil en el CBS: $H(B/A)=H(p)=p\lg\frac1p+(1-p)\lg\frac1{1-p}$, **no depende de $P(a_1)$**.

Concepto que piden explicar: $I(A,B)$ es la información que en promedio realmente llega al receptor por símbolo: la incertidumbre de la salida menos la que agrega el ruido del canal. Es simétrica ($I(A,B)=I(B,A)=H(A)-H(A/B)$) y su máximo sobre las fuentes posibles es la capacidad $C$.

### Ejercicios

#### 2.1 — 18/12/2015 = 23/10/2020 = 10/09/2021 = 17/12/2021 — resuelto

> Canal binario simétrico con $P(a_1)=0{,}65$ y $P(b_1/a_1)=0{,}75$. a) Entropía a la salida. b) Entropía del canal $H(B/A)$. c) Información mutua y concepto.

1. Datos: $P(a_2)=0{,}35$; $P(b_1/a_1)=P(b_2/a_2)=0{,}75$; $P(b_2/a_1)=P(b_1/a_2)=0{,}25$.
2. Salida:
   - $P(b_1)=0{,}65(0{,}75)+0{,}35(0{,}25)=0{,}4875+0{,}0875=0{,}575$
   - $P(b_2)=1-0{,}575=0{,}425$
3. a) $H(B)=0{,}575\lg\frac1{0{,}575}+0{,}425\lg\frac1{0{,}425}=0{,}4591+0{,}5246=\mathbf{0{,}9837}$ bits/símbolo.
4. b) $H(B/A)$, término a término:
   - $0{,}65(0{,}75)\lg\frac1{0{,}75}=0{,}2023$
   - $0{,}65(0{,}25)\lg4=0{,}3250$
   - $0{,}35(0{,}25)\lg4=0{,}1750$
   - $0{,}35(0{,}75)\lg\frac1{0{,}75}=0{,}1089$
   - Suma: $H(B/A)=\mathbf{0{,}8113}$ bits/símbolo (igual a $H(0{,}75)$).
5. c) $I(A,B)=0{,}9837-0{,}8113=\mathbf{0{,}1724}$ bits/símbolo. De cada símbolo emitido, que trae $H(A)=0{,}934$ bits, llegan efectivamente 0,172 bits; el resto lo «tapa» el ruido del canal (error del 25 %).

#### 2.2 — 21/02/2020 — resuelto ($P(a_1)=0{,}05$)

> Canal binario simétrico, $P(a_1)=0{,}05$, $P(b_1/a_1)=0{,}75$. Mismas preguntas.

1. $P(b_1)=0{,}05(0{,}75)+0{,}95(0{,}25)=0{,}0375+0{,}2375=0{,}275$; $P(b_2)=0{,}725$.
2. a) $H(B)=0{,}5122+0{,}3364=\mathbf{0{,}8485}$ bits/símbolo.
3. b) $H(B/A)=H(0{,}75)=\mathbf{0{,}8113}$ bits/símbolo (mismo canal).
4. c) $I(A,B)=\mathbf{0{,}0373}$ bits/símbolo. La fuente casi siempre emite $a_2$ ($H(A)=0{,}286$ bits), así que hay poca información para transferir y el canal ruidoso deja pasar muy poco.

Es probable que el 0,05 sea un error de tipeo de 0,65 (ver Dudas). Resolvé lo que dice la hoja.

#### 2.3 — 04/12/2015 — resuelto (caso degenerado)

> CBS con $P(a_1)=0$ y $P(b_1/a_1)=0{,}7$ (impreso «07»). A) Entropía a la salida. B) Información mutua y concepto.

1. $P(a_2)=1$; $P(b_1/a_2)=0{,}3$, $P(b_2/a_2)=0{,}7$.
2. $P(b_1)=0(0{,}7)+1(0{,}3)=0{,}3$; $P(b_2)=0{,}7$.
3. A) $H(B)=H(0{,}3)=\mathbf{0{,}8813}$ bits/símbolo.
4. $H(B/A)=1\cdot H(0{,}7)=0{,}8813$ bits/símbolo.
5. B) $I(A,B)=0$. La fuente emite siempre lo mismo ($H(A)=0$), no hay incertidumbre que resolver; toda la incertidumbre de la salida es ruido. Verificado en el PDF original: la hoja dice literalmente «P(a1)=0».

#### 2.4 — sin fecha (pág. 22 de finales viejos) — resultados

> Fuente A con $p(0)=0{,}6$, $p(1)=0{,}4$, conectada a un CBS con $p_e=0{,}1$. a) Entropía de la fuente; b) probabilidades de salida; c) probabilidades hacia atrás; d) probabilidades conjuntas.

- a) $H(A)=0{,}9710$ bits/símbolo.
- d) Conjuntas: $P(a_0,b_0)=0{,}54$; $P(a_0,b_1)=0{,}06$; $P(a_1,b_0)=0{,}04$; $P(a_1,b_1)=0{,}36$.
- b) $P(b_0)=0{,}58$; $P(b_1)=0{,}42$.
- c) $P(a_0/b_0)=0{,}54/0{,}58=0{,}9310$; $P(a_1/b_0)=0{,}0690$; $P(a_0/b_1)=0{,}06/0{,}42=0{,}1429$; $P(a_1/b_1)=0{,}8571$.
- Extra: $H(B)=0{,}9815$; $H(B/A)=H(0{,}9)=0{,}4690$; $I=0{,}5125$ bits/símbolo.

#### 2.5 — F12 (canal ternario) — resuelto

> Calcular la información mutua de un canal ternario del cual se conoce que el símbolo $x_1$ (entrada) tiene $P(x_1)=0{,}6$, $x_2$ se transmite sin error, $P(y_1)=0{,}52$ y $P(y_3)=0{,}18$ a la salida, siendo $P(y_1/x_1)=0{,}8$ y $P(y_1/x_3)=0{,}4$.

(Lectura de los subíndices reconstruida con la resolución del alumno; ver Dudas.)

1. $x_2$ sin error: $P(y_2/x_2)=1$ y $x_2$ no produce ni $y_1$ ni $y_3$.
2. De $P(y_1)$: $0{,}52=0{,}6(0{,}8)+P(x_3)(0{,}4)\Rightarrow P(x_3)=0{,}1$, $P(x_2)=0{,}3$.
3. $P(y_2)=1-0{,}52-0{,}18=0{,}30=P(x_2)$, así que ni $x_1$ ni $x_3$ van a $y_2$: $P(y_3/x_1)=0{,}2$ y $P(y_3/x_3)=0{,}6$. Control: $0{,}6(0{,}2)+0{,}1(0{,}6)=0{,}18$ ✓.
4. Matriz:

```
         y1    y2    y3
  x1    0,8    0    0,2
  x2     0     1     0
  x3    0,4    0    0,6
```

5. $H(Y)=0{,}52\lg\frac1{0{,}52}+0{,}3\lg\frac1{0{,}3}+0{,}18\lg\frac1{0{,}18}=0{,}4906+0{,}5211+0{,}4453=\mathbf{1{,}4570}$ bits/símbolo.
6. $H(Y/X)=0{,}6\,H(0{,}8;0{,}2)+0{,}3(0)+0{,}1\,H(0{,}4;0{,}6)=0{,}6(0{,}7219)+0{,}1(0{,}9710)=0{,}4332+0{,}0971=\mathbf{0{,}5303}$ bits/símbolo.
7. $I(X,Y)=1{,}4570-0{,}5303=\mathbf{0{,}9267}$ bits/símbolo.

### Trampas frecuentes

- $H(B/A)$ se pondera con $P(a_i)$; si te olvidás del peso, te da $2H(p)$.
- La «entropía del canal» del enunciado es $H(B/A)$, no $H(A/B)$.
- $I(A,B)\ge0$ siempre. Si te da negativa, sumaste mal.
- La «Práctica N°1 RESUELTO» calcula $H(A,B)$ sumando probabilidades (da «1»). Es incorrecto: con $p=(0{,}45;0{,}55)$ y $P=0{,}8$, las conjuntas son 0,36; 0,09; 0,11; 0,44 y $H(A,B)=1{,}7147$ bits.

---
## 3. Códigos compactos — Huffman r-ario, longitud media, rendimiento, Kraft

### Receta

Fuente: «Fórmulas y pasos» (Códigos compactos), «2 - Codificación».

| Magnitud | Fórmula |
|---|---|
| ¿Hacen falta símbolos falsos? | $\omega=r+\alpha(r-1)$ con $\alpha$ entero; si no, agregar símbolos de probabilidad 0 de a uno |
| Longitud media | $L=\sum_i P(s_i)\,l_i$ [dígitos r-arios/símbolo] |
| Entropía | $H(S)=\sum_i P(s_i)\lg\dfrac1{P(s_i)}$ [bits/símbolo] |
| Entropía en unidades r-arias | $H_r(S)=\dfrac{H(S)}{\lg r}$ |
| Rendimiento (eficiencia) | $\eta=\dfrac{H_r(S)}{L}$ |
| Redundancia | $1-\eta=\dfrac{L-H_r(S)}{L}$ |
| Kraft | $\sum_i r^{-l_i}\le1$ ⇔ existe un código instantáneo con esas longitudes |
| Cota inferior | $L\ge H_r(S)$ |

$\omega$: cantidad de símbolos de la fuente; $r$: cantidad de símbolos del alfabeto código.

Pasos (Huffman r-ario):

1. Verificar $\omega=r+\alpha(r-1)$. Si $\alpha$ no es entero, agregar símbolos falsos con $P=0$ hasta que lo sea.
2. Ordenar de mayor a menor probabilidad.
3. Fundir los **$r$** menos probables en uno (sumar probabilidades) y reordenar. Repetir hasta que queden exactamente $r$.
4. Asignar los $r$ dígitos a esos $r$ símbolos y volver hacia atrás: cada símbolo que se desdobla le pasa su palabra a sus «hijos», que agregan un dígito cada uno.
5. Calcular $L$, $H$, $H_r$, $\eta$, redundancia.
6. «¿Puede haber otro código instantáneo de menor longitud media?» → **No**: Huffman es compacto (demostrado en el apunte). Puede haber otro distinto con la **misma** $L$ (empates).

### Ejercicios

#### 3.1 — 09/03/2012 — resuelto (código dado)

> Código de la tabla. a) ¿Es instantáneo? b) ¿Es compacto? c) Longitud media. d) Kraft e interpretación. e) Rendimiento y redundancia.

```
 Símbolo  P      Código
   A     27/64   0
   B      9/64   100
   C      9/64   101
   D      9/64   110
   E      3/64   11100
   F      3/64   11101
   G      3/64   11110
   H      1/64   11111
```

1. a) **Sí**: ninguna palabra es prefijo de otra («0» es la única que empieza con 0; las de 3 dígitos no son prefijo de las de 5, porque todas las de 5 empiezan con 111 y no hay palabra «111»).
2. c) $L=\frac{27}{64}(1)+3\cdot\frac{9}{64}(3)+3\cdot\frac{3}{64}(5)+\frac1{64}(5)=\frac{27+81+45+5}{64}=\frac{158}{64}=\mathbf{2{,}46875}$ binits/símbolo.
3. d) Kraft: $2^{-1}+3\cdot2^{-3}+4\cdot2^{-5}=0{,}5+0{,}375+0{,}125=\mathbf{1}\le1$. Existe un código instantáneo con esas longitudes (este mismo), y como da exactamente 1 no sobra ninguna palabra posible: el árbol está completo.
4. $H(S)=2{,}4338$ bits/símbolo (es la tercera extensión de una fuente binaria $\{3/4,1/4\}$: $3\,H(0{,}75)=3(0{,}8113)$).
5. b) Huffman binario sobre la misma fuente da también $L=2{,}46875$: **el código es compacto**.
6. e) $\eta=2{,}4338/2{,}46875=\mathbf{0{,}9859}$ (98,6 %); redundancia $=\mathbf{0{,}0141}$.

#### 3.2 — 03/03/2006 = 13/03/2015 — resuelto (ternario con símbolo falso)

> Hallar un código compacto ternario y su longitud promedio. $P(a)=0{,}40$, $P(b)=0{,}17$, $P(c)=0{,}0125$, $P(d)=0{,}04$, $P(e)=0{,}21$, $P(f)=0{,}13$, $P(g)=0{,}0125$, $P(h)=0{,}025$. ¿Podrá encontrarse otro código instantáneo ternario de menor longitud promedio? (2015 pide también el rendimiento.)

1. $\omega=8$, $r=3$: $8=3+2\alpha\Rightarrow\alpha=2{,}5$ → agrego **1 símbolo falso** $z$ con $P=0$ ($\omega=9$, $\alpha=3$).
2. Reducciones (de a 3):

```
 S0 (orden)     S1            S2            S3
 a  0,40        a  0,40       a  0,40       a    0,40  → 0
 e  0,21        e  0,21       e  0,21       bf*  0,39  → 1
 b  0,17        b  0,17       b  0,17       e    0,21  → 2
 f  0,13        f  0,13       f  0,13
 d  0,04        d  0,04       dh* 0,09
 h  0,025       h  0,025
 c  0,0125      gcz 0,025
 g  0,0125
 z  0
```

3. Vuelta atrás: $a=0$, $e=2$; el grupo 0,39 = 1 se abre en $b=10$, $f=11$, (0,09)=12; el 0,09 se abre en $d=120$, $h=121$, (0,025)=122; ese se abre en $c=1220$, $g=1221$, $z=1222$ (se descarta).
4. $L=0{,}40(1)+0{,}21(1)+0{,}17(2)+0{,}13(2)+0{,}04(3)+0{,}025(3)+0{,}0125(4)+0{,}0125(4)=\mathbf{1{,}505}$ dígitos ternarios/símbolo.
5. $H(S)=2{,}2957$ bits/símbolo; $H_3(S)=2{,}2957/\lg3=2{,}2957/1{,}5850=1{,}4484$ ternarios/símbolo.
6. $\eta=1{,}4484/1{,}505=\mathbf{0{,}9624}$; redundancia $\mathbf{0{,}0376}$.
7. No existe otro instantáneo ternario con $L<1{,}505$: Huffman es compacto. Cota: $L\ge H_3=1{,}448$.

#### 3.3 — F3 (cuaternario) — resuelto

> Codificar en un código compacto cuyo alfabeto código sea A, B, C, D. b) Longitud media y eficiencia. $S_1=0{,}22$, $S_2=0{,}03$, $S_3=0{,}12$, $S_4=0{,}03$, $S_5=0{,}02$, $S_6=0{,}11$, $S_7=0{,}05$, $S_8=0{,}06$, $S_9=0{,}33$, $S_{10}=0{,}03$.

1. $\omega=10=4+3\alpha\Rightarrow\alpha=2$: **no** hacen falta falsos.
2. Reducciones (de a 4):

```
 S0                S1                 S2
 S9  0,33          S9   0,33          S9     0,33 → A
 S1  0,22          S1   0,22          (S6,G,S8,S7) 0,33 → B
 S3  0,12          S3   0,12          S1     0,22 → C
 S6  0,11          S6   0,11          S3     0,12 → D
 S8  0,06          G    0,11
 S7  0,05          S8   0,06
 S2  0,03          S7   0,05
 S4  0,03
 S10 0,03     G = S2+S4+S10+S5
 S5  0,02
```

3. Palabras: $S_9=A$, $S_1=C$, $S_3=D$, $S_6=BA$, $S_8=BC$, $S_7=BD$, $S_2=BBA$, $S_4=BBB$, $S_{10}=BBC$, $S_5=BBD$.
4. $L=(0{,}33+0{,}22+0{,}12)(1)+(0{,}11+0{,}06+0{,}05)(2)+(0{,}03\cdot3+0{,}02)(3)=0{,}67+0{,}44+0{,}33=\mathbf{1{,}44}$ cuaternarios/símbolo.
5. $H=2{,}7536$ bits; $H_4=2{,}7536/2=1{,}3768$; $\eta=\mathbf{0{,}9561}$; redundancia $\mathbf{0{,}0439}$.

#### Resto (enunciado + resultados)

| Origen | Fuente y pedido | Resultado |
|---|---|---|
| F13 = 07/05/2004 | Ternario (A,B,C / a,b,c): $S_1=0{,}22$, $S_2=0{,}03$, $S_3=0{,}12$, $S_4=0{,}03$, $S_5=0{,}02$, $S_6=0{,}11$, $S_7=0{,}11$, $S_8=0{,}33$, $S_9=0{,}03$. Longitud media y redundancia. | $\omega=9=3+2\cdot3$, sin falsos. Longitudes: $S_8$→1; $S_1,S_3,S_6,S_7,S_9$→2; $S_2,S_4,S_5$→3. Una solución: $S_8=B$, $S_1=AA$, $S_3=AB$, $S_7=AC$, $S_6=CA$, $S_9=CC$, $S_2=CBA$, $S_4=CBB$, $S_5=CBC$. $L=1{,}75$; $H=2{,}6442$ bits; $H_3=1{,}6683$; $\eta=0{,}9533$; redundancia $0{,}0467$. |
| 23/09/2005 | Ternario con alfabeto (1,2,3): $a=0{,}2$, $b=0{,}15$, $c=0{,}35$, $d=0{,}02$, $e=0{,}04$, $f=0{,}15$, $g=0{,}06$, $h=0{,}02$, $i=0{,}01$. ¿Otro instantáneo más corto? $L$ y «velocidad de información». | Sin falsos. $c=2$, $a=3$, $b=11$, $f=12$, $g=131$, $e=133$, $d=1321$, $h=1322$, $i=1323$. $L=1{,}65$; $H=2{,}5371$ bits; $H_3=1{,}6007$; $\eta=0{,}9701$. No hay instantáneo más corto. $R$ no se puede calcular: no se da la duración de los dígitos. |
| 29/11/2002 | Ternario: $A=0{,}2$, $B=0{,}04$, $C=0{,}05$, $D=0{,}01$, $E=0{,}1$, $F=0{,}06$, $G=0{,}025$, $H=0{,}3$, $I=0{,}2$, $J=0{,}015$. $L$ y rendimiento; ¿otro más corto? | $\omega=10$ → 1 falso. $H=1$; $A=00$, $I=01$, $E=02$, $F=21$, $C=22$, $B=200$, $G=201$, $J=2020$, $D=2021$. $L=1{,}815$; $H=2{,}7178$ bits; $H_3=1{,}7147$; $\eta=0{,}9448$. |
| ¿07/02/2005? | Igual a 3.2 pero con $P(a)=0{,}2575$, $P(c)=0{,}125$ (la tabla suma 0,97). | Ver Dudas. Con esos pesos (normalizados): $L=1{,}7655$, $\eta=0{,}9300$. |
| F5 P1 c-d | Codificar en forma compacta con $k_i=0,1,2,3$ una fuente de caracteres equiprobables. | Falta la cantidad de caracteres de la fuente → ver Dudas. |

### Trampas frecuentes

- En r-ario se funden **$r$** símbolos por paso, no 2.
- Olvidar los símbolos falsos: la última reducción no queda con $r$ símbolos y el código no es compacto.
- El rendimiento se calcula con $H_r$, no con $H$ en bits (salvo binario).
- Kraft $\le1$ **no** garantiza que un código dado sea instantáneo; sólo que **existe** uno con esas longitudes (ejercicio de la práctica de codificación).
- Con empates, el código puede cambiar pero $L$ no.

---

## 4. Códigos lineales — H → G → V → síndromes, y diseño

### Receta

Fuente: «Fórmulas y pasos» (Códigos lineales, ejemplo = F5 ej. 3), «3 - Detección y Corrección de errores», «4 - Ejemplos Códigos Lineales».

| Objeto | Tamaño |
|---|---|
| $H$ (control de paridad) | $(n-m)\times n$ |
| $G$ (generadora) | $m\times n$ |
| Código de grupo $V$ | $2^m$ palabras de $n$ dígitos |
| Síndromes no nulos | $2^{n-m}-1$ |

Pasos (H dada):

1. Leer $n$ (columnas) y $n-m$ (filas) → $m$ y $2^m$ palabras.
2. Plantear $X\cdot H^T=0$: $n-m$ ecuaciones (suma sin acarreo, módulo 2).
3. Despejar $n-m$ incógnitas en función de $m$ libres.
4. Tabla: dar todos los valores a las $m$ libres → $V$.
5. Elegir $m$ palabras linealmente independientes de $V$ → $G$ (no es única).
6. Síndromes: para cada síndrome $S\neq0$, la palabra de error simple que lo produce es la **columna de $H$ igual a $S$** (es lo mismo que resolver $X\cdot H^T=S$ y mirar la solución con un solo 1, como hace el apunte con las «familias»).
   - Una sola columna igual a $S$ → **detecta y corrige** error simple en ese dígito.
   - Dos o más columnas iguales → **sólo detecta** (no sabe cuál).
   - Ninguna columna igual → ese síndrome sólo aparece con errores múltiples.
   - Columna nula → error en ese dígito **no se detecta**.
7. Condición para corregir error simple en todos los dígitos: columnas de $H$ **no nulas y distintas** entre sí ⇔ $d_{\min}\ge3$ ⇔ $2^{n-m}-1\ge n$.

Pasos (diseño, «enviar X mensajes con corrección simple»):

1. $2^m\ge X$ → $m$.
2. Menor $k=n-m$ con $2^k-1\ge m+k$.
3. Armar $H$ con $n$ columnas distintas no nulas (cómodo: forma sistemática $[P\,|\,I]$).
4. Seguir con los pasos 2–6 de arriba.

### Ejercicios

#### 4.1 — F5 P3 (es el ejemplo resuelto de «Fórmulas y pasos») — resuelto

> $H=\begin{bmatrix}1&1&1&0&0\\1&0&0&0&1\\0&1&0&1&0\end{bmatrix}$. a) Código de grupo $V$ y matriz $G$. b) Corrección de errores.

1. $n=5$, $n-m=3\Rightarrow m=2$, $V$ tiene $2^2=4$ palabras.
2. $X H^T=0$:
   - $x_1+x_2+x_3=0$
   - $x_1+x_5=0$
   - $x_2+x_4=0$
3. Libres $x_1,x_2$: $x_5=x_1$, $x_4=x_2$, $x_3=x_1+x_2$.
4. Tabla:

```
 x1 x2 | x3 x4 x5 | palabra
  0  0 |  0  0  0 | 00000
  0  1 |  1  1  0 | 01110
  1  0 |  1  0  1 | 10101
  1  1 |  0  1  1 | 11011
```

5. $G=\begin{bmatrix}1&0&1&0&1\\1&1&0&1&1\end{bmatrix}$ (10101 y 11011, como en la guía).
6. b) Columnas de $H$ (síndrome = fila1 fila2 fila3): $x_1=110$, $x_2=101$, $x_3=100$, $x_4=001$, $x_5=010$. Todas distintas y no nulas → **corrige error simple en cualquier dígito**. Síndromes 011 y 111 no corresponden a errores simples (011 = dobles en $x_1x_2$ o $x_4x_5$; 111 = dobles en $x_1x_4$ o $x_2x_5$): detectan, no corrigen. $d_{\min}=3$.

#### 4.2 — F1 — resuelto (corrección parcial)

> $H=\begin{bmatrix}0&0&1&1&0&1&1\\0&1&0&1&1&0&1\\1&0&0&0&0&1&1\end{bmatrix}$. a) Código de grupo. b) Matriz generadora. c) Comportamiento frente a errores.

1. $n=7$, $n-m=3\Rightarrow m=4$, 16 palabras.
2. Ecuaciones: $x_3+x_4+x_6+x_7=0$; $x_2+x_4+x_5+x_7=0$; $x_1+x_6+x_7=0$.
3. Libres $x_4,x_5,x_6,x_7$: $x_1=x_6+x_7$, $x_2=x_4+x_5+x_7$, $x_3=x_4+x_6+x_7$.
4. a) $V$ = {0000000, 0000111, 0011011, 0011100, 0100011, 0100100, 0111000, 0111111, 1001001, 1001110, 1010010, 1010101, 1101010, 1101101, 1110001, 1110110}.
5. b) Una $G$ (filas para $x_4,x_5,x_6,x_7$ = 1 de a una): $G=\begin{bmatrix}0&1&1&1&0&0&0\\0&1&0&0&1&0&0\\1&0&1&0&0&1&0\\1&1&1&0&0&0&1\end{bmatrix}$.
6. c) Columnas: $x_1=001$, $x_2=010$, $x_3=100$, $x_4=110$, $x_5=010$, $x_6=101$, $x_7=111$.
   - 001 → corrige $x_1$; 100 → $x_3$; 110 → $x_4$; 101 → $x_6$; 111 → $x_7$.
   - **010 → error en $x_2$ o en $x_5$: detecta pero no corrige.**
   - 011 → sólo errores dobles ($x_1x_2$, $x_1x_5$, $x_3x_7$, $x_4x_6$).
   - $d_{\min}=2$ (hay palabras de peso 2: 0100100).

#### 4.3 — 04/12/2015 — resuelto (diseño)

> Transmitir mensajes protegidos así: detectar y corregir error simple en el 1° y 2° dígito, sólo detectar errores simples en el resto, excepto el menos significativo, en el que no se desea detectar error alguno. Aplicando códigos lineales, encontrar el código.

El enunciado no fija la cantidad de mensajes, así que se elige la menor estructura que cumpla (supuesto propio).

1. Traducción a columnas de $H$:
   - $x_1$, $x_2$: columnas no nulas, distintas entre sí y **distintas de todas las demás** (corregir).
   - $x_3\dots x_{n-1}$: columnas no nulas (detectar), pueden repetirse entre ellas.
   - $x_n$ (menos significativo): columna **nula** (no detectar).
2. Con $n-m=2$ filas hay 3 síndromes no nulos: 10, 01, 11. Asigno $x_1=10$, $x_2=01$, y el resto $=11$.
3. Con $n=5$: $H=\begin{bmatrix}1&0&1&1&0\\0&1&1&1&0\end{bmatrix}$, $m=3$ → 8 mensajes.
4. Ecuaciones: $x_1+x_3+x_4=0$, $x_2+x_3+x_4=0$ → $x_1=x_2=x_3+x_4$; $x_5$ libre.
5. $V$ = {00000, 00001, 00110, 00111, 11010, 11011, 11100, 11101}; $G$ = {11010, 11100, 00001}.
6. Verificación: síndrome 10 → $x_1$ (corrige), 01 → $x_2$ (corrige), 11 → $x_3$ o $x_4$ (detecta), $x_5$ no aparece en ninguna ecuación → error no detectado. ✓
7. Si se quieren más dígitos en «el resto», se agregan columnas 11 (cada una suma un mensaje-bit).

#### Resto (enunciado + resultados)

| Origen | Dato | Resultado |
|---|---|---|
| F10 | $H=\begin{bmatrix}0&0&1&1&0&1&1\\0&1&0&1&1&0&1\\1&0&0&0&1&1&1\end{bmatrix}$ | $m=4$, 16 palabras: 0000000, 0001110, 0010101, 0011011, 0100011, 0101101, 0110110, 0111000, 1000111, 1001001, 1010010, 1011100, 1100100, 1101010, 1110001, 1111111. Columnas 001,010,100,110,011,101,111: las 7 distintas → **corrige error simple en todos los dígitos** (es un Hamming (7,4) permutado). $d_{\min}=3$. |
| F4 | $H=\begin{bmatrix}0&0&1&1&0&1\\0&1&0&1&1&0\\1&0&0&0&1&1\end{bmatrix}$ | $m=3$, 8 palabras: 000000, 000111, 011011, 011100, 101001, 101110, 110010, 110101. Columnas 001,010,100,110,011,101: distintas → corrige error simple en los 6 dígitos. Síndrome 111 sólo por dobles ($x_1x_4$, $x_2x_6$, $x_3x_5$): detecta. $d_{\min}=3$. |
| 25/02/2005 | $H=\begin{bmatrix}1&0&0&1&1\\0&0&1&0&0\\0&1&0&0&1\end{bmatrix}$ | $m=2$: $V$ = {00000, 01011, 10010, 11001}; $G$ = {10010, 01011}. Columnas: $x_1=100$, $x_2=001$, $x_3=010$, $x_4=100$, $x_5=101$. Corrige $x_2,x_3,x_5$; **100 → $x_1$ o $x_4$: sólo detecta**. $d_{\min}=2$. |
| 07/05/2004 | $G$ de dimensión 2 con base 00111 y 01010. a) Matriz $H$. b) Síndromes para error en b1) $x_1,x_2,x_4$; b2) $x_3$. | $V$ = {00000, 00111, 01010, 01101}. $V'$ (ortogonal) tiene 8 palabras; una base: $H=\begin{bmatrix}1&0&0&0&0\\0&0&1&0&1\\0&1&0&1&1\end{bmatrix}$. Columnas: $x_1=100$, $x_2=001$, $x_3=010$, $x_4=001$, $x_5=011$. b2) error en $x_3$: síndrome 010 (corrige). b1) leído como error **triple** simultáneo en $x_1,x_2,x_4$: $100+001+001=100$, igual al de error simple en $x_1$ → se «corrige» mal. Leído como errores simples por separado: $x_1$→100 (corrige), $x_2$ y $x_4$→001 (sólo detecta). Los síndromes dependen de la $H$ elegida. |
| F11 / 17/02/2006 | Enviar 8 (F11) o 7 (2006) mensajes con código lineal binario que detecte y corrija error simple. | $2^m\ge8$ (o 7) → $m=3$; $2^k-1\ge3+k$ → $k=3$, $n=6$. Una $H=\begin{bmatrix}1&1&0&1&0&0\\1&0&1&0&1&0\\0&1&1&0&0&1\end{bmatrix}$ ($x_4=x_1+x_2$, $x_5=x_1+x_3$, $x_6=x_2+x_3$). $V$ = {000000, 001011, 010101, 011110, 100110, 101101, 110011, 111000}; $d_{\min}=3$. Columnas 110,101,011,100,010,001: corrige los 6. Ejemplo: se manda 101101, llega 100101 → síndrome 011 = columna de $x_3$ → corrijo $x_3$. |

### Trampas frecuentes

- El síndrome depende del error, no de la palabra enviada (por eso se lee de las columnas de $H$).
- Un síndrome repetido en dos columnas **no** corrige; anotarlo como «detecta».
- $G$ y $H$ no son únicas; lo que no cambia es $V$ (dada $H$) y si corrige o no.
- Errores iguales a una palabra del código **no se detectan** (síndrome 0).
- Suma sin acarreo: $1+1=0$.

---

## 5. Hamming — código de control por zonas

### Receta

Fuente: «Fórmulas y pasos» (Hamming), «2 - Codificación», «Resumen 1° Parcial Práctica».

1. Dígitos de información: $2^m\ge X$ (mensajes). Para 9–16 mensajes, $m=4$.
2. Dígitos de control: $2^n\ge n+m+1$. Con $m=4$, $n=3$ → palabra de 7.
3. Diagrama de Venn con tres zonas $C_1,C_2,C_3$; información en las intersecciones:
   - $I_1\in C_1\cap C_2$, $I_2\in C_1\cap C_3$, $I_3\in C_2\cap C_3$, $I_4\in C_1\cap C_2\cap C_3$.
4. Ecuaciones (paridad par):
   - $C_1=I_1\oplus I_2\oplus I_4$
   - $C_2=I_1\oplus I_3\oplus I_4$
   - $C_3=I_2\oplus I_3\oplus I_4$
5. «Tira» de 7 posiciones: $C_1$ en $2^0=1$, $C_2$ en $2^1=2$, $C_3$ en $2^2=4$; cada $I$ va en la suma de las posiciones de sus zonas: $I_1\to3$, $I_2\to5$, $I_3\to6$, $I_4\to7$.

```
 pos:  1   2   3   4   5   6   7
       C1  C2  I1  C3  I2  I3  I4
```

6. Tabla de código (16 palabras, I1I2I3I4 | C1C2C3):

```
 0000|000  0001|111  0010|011  0011|100  0100|101  0101|010  0110|110  0111|001
 1000|110  1001|001  1010|101  1011|010  1100|011  1101|100  1110|000  1111|111
```

7. Detección: en el receptor recalculás $C_1C_2C_3$ con la información recibida y hacés la diferencia (XOR) con los controles recibidos. Leído como binario $C_3C_2C_1$, da en decimal **la posición del error** (0 = sin error).

### Ejercicios

#### 5.1 — 18/12/2015 = 21/02/2020 — resuelto

> Transmitir 12 mensajes protegidos contra error simple. a) Código por Hamming. b) Ejemplo de error en un dígito de información. c) Ejemplo de error en un dígito de control.

1. a) $2^m\ge12\Rightarrow m=4$ (16 combinaciones, uso 12). $2^n\ge n+5\Rightarrow n=3$ ($8\ge8$). Palabras de 7 dígitos; zonas y tabla de arriba (se usan, por ejemplo, las 12 primeras filas).
2. b) Error en información. Quiero enviar $I=0110$: $C_1=0\oplus1\oplus0=1$, $C_2=0\oplus1\oplus0=1$, $C_3=1\oplus1\oplus0=0$. Tira: $C_1C_2I_1C_3I_2I_3I_4=1\,1\,0\,0\,1\,1\,0$.
   - Llega $1\,1\,0\,0\,1\,\mathbf{0}\,0$ (error en posición 6 = $I_3$).
   - Recalculo con $I=0100$: $C_1=1$, $C_2=0$, $C_3=1$.
   - Recibidos $C_1C_2C_3=1\,1\,0$. Diferencia: $C_1:0$, $C_2:1$, $C_3:1$ → $C_3C_2C_1=110_2=6$ → error en la posición 6 ($I_3$). Corrijo: $I=0110$.
3. c) Error en control. Misma palabra $1100110$; llega $1\,\mathbf{0}\,0\,0\,1\,1\,0$ (error en $C_2$).
   - Información recibida $0110$ → recalculo $C_1C_2C_3=110$.
   - Recibidos $100$. Diferencia: sólo $C_2$ → $010_2=2$ → posición 2 = $C_2$. La información estaba bien.

#### 5.2 — 15/02/2017 — resultados

> Codificar 13 mensajes fuente protegidos ante error simple en todos los dígitos, con notación $(X_1,\dots,X_n)$. Ejemplos de error en información y en control.

- $2^4=16\ge13\Rightarrow m=4$; $n=3$; $(X_1,\dots,X_7)=(C_1,C_2,I_1,C_3,I_2,I_3,I_4)$.
- Controles: $X_1=X_3\oplus X_5\oplus X_7$; $X_2=X_3\oplus X_6\oplus X_7$; $X_4=X_5\oplus X_6\oplus X_7$.
- Ejemplo: $I=1011$ → $0110011$. Error en $X_3$: llega $0100011$; con $I=0011$ recalculo $C_1C_2C_3=100$; recibido $C_1C_2C_3=010$; diferencia $C_1C_2C_3=110$ → leído $C_3C_2C_1=011_2=3$ → $X_3$. Error en $X_4$: llega $0111011$; recalculo $010$, recibido $011$; diferencia sólo $C_3$ → $100_2=4$ → $X_4$ (control).

#### 5.3 — F8 (09/03/2000) y F12 — resultados

- F8: «Se transmiten 14 mensajes (lectura dudosa) … establecer el código de detección y corrección de errores simples aplicando Hamming; ejemplificar.» → Igual que 5.1: $m=4$, $n=3$.
- F12: «Aplicando Hamming, escribir el código (4 dígitos) completo indicando zonas y ecuaciones. Ejemplo de recepción con error unitario.» → $m=4$ dígitos de información, $n=3$, tabla completa de 16 palabras de arriba.

### Trampas frecuentes

- La desigualdad es $2^n\ge n+m+1$ (el «+1» es el caso «sin error»).
- El síndrome se lee $C_3C_2C_1$ (el de mayor peso es $C_3$, posición 4). Si lo leés al revés, señalás la posición equivocada.
- Si sólo cambia **un** control, el error está en ese control y la información está bien.
- Rendimiento del Hamming (7,4): $4/7=57{,}1\,\%$.

---
## 6. TDM – PCM: ancho de banda de una trama digital

### Receta

Fuente: «Fórmulas y pasos» (TDM), «5 - Comunicaciones Digitales» págs. 21–24.

Se reconoce porque dan $n$ (bits por muestra) o hablan de «canal digital» / «trama PCM».

| Magnitud | Fórmula |
|---|---|
| Nyquist | $f_s\ge2f_{\max}$ (se toma $f_s=2f_{\max}$); si $f_{\min}\ll f_{\max}$, $W\approx f_{\max}$ |
| Período de trama | $T_s=\dfrac1{f_s}=N\cdot T_m$ |
| Duración de una muestra | $T_m=n\cdot\tau$ |
| Ancho del pulso | $\tau=\dfrac{1}{N\,n\,f_s}$ |
| Ancho de banda (cruce por cero del espectro) | $B_w=\dfrac1\tau=N\cdot n\cdot2f_{\max}$ |
| Tasa de dígitos de la línea | $r=N\,n\,f_s$ [bps] (numéricamente igual a $B_w$) |

$N$: muestras por trama (incluye las de control/señalización: «25+2» → $N=27$); $n$: bits por muestra.

Pasos:

1. Identificar $N$ (todas las muestras de la trama), $n$ y $f_{\max}$.
2. $f_s=2f_{\max}$ → $T_s=1/f_s$.
3. $T_m=T_s/N$, $\tau=T_m/n$.
4. $B_w=1/\tau=N\,n\,2f_{\max}$.
5. Técnica: **multiplexado TDM con modulación PCM** (muestreo → cuantificación → codificación binaria).
6. Gráficas (tres o cuatro):

```
 (1) Señal y muestreo (PAM)        (2) Trama TDM
  A│   ╭─╮       ╭              A│ ┌─┐┌─┐┌─┐     ┌─┐┌─┐
   │ ╭─┤ ├╮ ╭─╮╭─┤                │ │1││2││3│ ... │N││1│ ...
   │─┤ │ │├─┤ ├┤ │ → t            └─┴─┴┴─┴┴─┴─────┴─┴┴─┴──→ t
     |<Ts>|                         |<Tm>|
                                    |<-------- Ts -------->|
 (3) Una muestra = n pulsos         (4) Espectro del pulso
  │┌┐  ┌┐┌┐   ┌┐                    A│▔▔▔╲
  ││└──┘││└───┘│ ...  → t             │    ╲___      (|sinc|, 1er cero en 1/τ)
   |τ|                                 └───────┼────→ f
   |<----- Tm = n·τ ----->|                    1/τ = Bw
```

### Ejercicios

#### 6.1 — 04/04/2025 = 19/11/2021 — resuelto

> Trama PCM de 25 muestras de información + 2 de control. Señales con $f_{\min}=400$ Hz y $f_{\max}=3500$ Hz; cada muestra con 7 dígitos. Ancho de banda para transmitir cada trama, gráficos y técnica.

1. $N=25+2=27$; $n=7$; $f_{\max}=3500$ Hz ($f_{\min}=400$ Hz $\ll f_{\max}$, se muestrea con $f_{\max}$).
2. $f_s=2(3500)=7000$ Hz → $T_s=1/7000=142{,}86\ \mu s$.
3. $T_m=T_s/27=5{,}291\ \mu s$; $\tau=T_m/7=0{,}7559\ \mu s=755{,}9$ ns.
4. $B_w=1/\tau=27\times7\times7000=\mathbf{1{,}323\ MHz}$ (1 323 000 Hz).
5. Técnica: TDM-PCM. Gráficos como en la receta, con 27 ranuras por trama y 7 pulsos por ranura.

#### 6.2 — 18/12/2015 = 21/02/2020 = 28/08/2020 — resuelto

> 32 señales de $f_{\max}=4$ kHz; cada muestra con 8 bits. a) Ancho de banda del canal. b) Multiplexación y modulación. c) Gráficas temporales y frecuenciales.

1. $f_s=8$ kHz → $T_s=125\ \mu s$.
2. $T_m=125/32=3{,}906\ \mu s$; $\tau=3{,}906/8=0{,}4883\ \mu s=488{,}3$ ns.
3. a) $B_w=32\times8\times8000=\mathbf{2{,}048\ MHz}$ (es la trama E1 de 32 canales).
4. b) TDM con modulación PCM.

#### 6.3 — 10/09/2021 — resuelto (inverso)

> Señal compuesta por 900 señales PAM por un canal digital; ocupa 2 MHz; código de 7 bits por muestra. Esquemas y fórmulas. ¿Ancho de banda $W$ de cada señal analógica original?

1. $B_w=N\,n\,2W\Rightarrow W=\dfrac{B_w}{2Nn}=\dfrac{2\times10^6}{2\times900\times7}$.
2. $W=\mathbf{158{,}7\ Hz}$ ($f_s=317{,}5$ Hz, $\tau=0{,}5\ \mu s$).
3. Valor muy chico para señales reales, pero es lo que dan los datos. Ver Dudas.

#### 6.4 — 09/03/2012 = F7 P2 — resuelto (N máximo)

> Transmitir N señales por un canal con frecuencia inferior de corte 100 MHz y superior 300 MHz. Cada señal se muestrea a 8000 Hz como mínimo y se codifica con 8 bits. Número máximo de señales, técnica, esquemas y frecuencia máxima del mensaje.

1. Ancho de banda del canal: $B_w=f_{\max\,corte}-f_{\min\,corte}=300-100=200$ MHz.
2. $f_s=8000$ Hz → $f_{\max}$ del mensaje $=f_s/2=\mathbf{4\ kHz}$.
3. $N=\dfrac{B_w}{n\,f_s}=\dfrac{200\times10^6}{8\times8000}=\mathbf{3125}$ señales.
4. $T_s=125\ \mu s$; $\tau=1/B_w=5$ ns; $T_m=40$ ns.
5. Técnica: TDM-PCM. Como el canal es pasabanda (100–300 MHz), la trama se transmite modulando una portadora dentro de esa banda *(conocimiento general; la guía sólo usa la diferencia de cortes)*.

#### Resto (enunciado + resultados)

| Origen | Datos | Resultado |
|---|---|---|
| 23/10/2020 | 42 señales, $f_{\max}=6$ kHz, 8 bits | $f_s=12$ kHz; $T_s=83{,}33\ \mu s$; $\tau=248{,}0$ ns; $B_w=4{,}032$ MHz |
| 18/12/2020 | 75 señales, $f_{\max}=30$ kHz, 8 bits | $f_s=60$ kHz; $T_s=16{,}67\ \mu s$; $T_m=222{,}2$ ns; $\tau=27{,}78$ ns; $B_w=36$ MHz |
| 20/11/2020 | Trama 25+2, 300–3400 Hz, 8 dígitos | $f_s=6800$ Hz; $T_s=147{,}06\ \mu s$; $\tau=680{,}8$ ns; $B_w=1{,}4688$ MHz |
| F1 | 30 señales telefónicas, $f_{\max}=3$ kHz, 8 bits | $f_s=6$ kHz; $\tau=694{,}4$ ns; $B_w=1{,}44$ MHz (coincide con la resolución del alumno) |
| 17/02/2006 (y práctica) | 2200 señales, $f_{\max}=4$ kHz, 8 dígitos | $B_w=2200\times8\times8000=140{,}8$ MHz; $\tau=7{,}10$ ns |
| F4 | $f_{\max}=2$ kHz, canal de 1050 MHz, TDM-PCM, 8 bits. ¿Cuántas señales? | $N=1050\times10^6/(8\times4000)=32812{,}5\Rightarrow$ **32 812** señales (redondeo hacia abajo) |
| F12 | $AB=30{,}7$ MHz, $f_{\max}=20$ kHz, 46 muestras + 2 de señalización. ¿Dígitos por muestra? Gráfico temporal. | $N=48$, $f_s=40$ kHz: $n=30{,}7\times10^6/(48\times40\,000)=15{,}99$. El alumno toma $n=16$ (da 30,72 MHz, un 0,07 % más que el canal); estrictamente entran 15. Ver Dudas. |
| 03/03/2006 | Seis señales por canal digital de $B_w=2{,}4$ MHz: $S_1$: $f_{\min}=2$ kHz, $W=8$ kHz; $S_2$: $W=16$ kHz; $S_3$: $f_{\min}=10$, $f_{\max}=20$ kHz; $S_4$: $f_{\max}=6$ kHz, $W=4$ kHz; $S_5$: $f_{\max}=12$ kHz; $S_6$: $W=4$ kHz. ¿Bits por muestra? | Todas se muestrean a la tasa de la más rápida: $f_{\max}=20$ kHz ($S_3$) → $f_s=40$ kHz. $n=2{,}4\times10^6/(6\times40\,000)=\mathbf{10}$ bits. |
| 13/03/2015 | 30 señales de distinta frecuencia (S1–S4 $f_{\max}=3$ kHz; S5–S12 $f_{\max}=2$ kHz, $w=2$ kHz; S13–S17 $f_{\min}=0{,}5$, $f_{\max}=1{,}5$ kHz; S18–S25 $f_{\max}=1{,}5$ kHz; S26–S30 $f_{\min}=1$ kHz, $w=3$ kHz) + 2 de sincronismo y señalización; 8 dígitos. | $N=32$; la mayor $f_{\max}$ es la de S26–S30: $1+3=4$ kHz → $f_s=8$ kHz; $B_w=32\times8\times8000=\mathbf{2{,}048\ MHz}$. Lectura parcial, ver Dudas. |
| Sin fecha (pág. 22) | 28 canales de 3,4 kHz; 7 bits por muestra + 1 de paridad por señal, 1 de sincronismo por muestra y 1 de señalización por trama. Tasa de dígitos y ancho de banda. | Interpretación A (trama $=28\times8+1+1=226$ bits): $r=226\times6800=1{,}5368$ Mbps, $B_w=1{,}5368$ MHz. Interpretación B (sincronismo en cada muestra: $28\times9+1=253$ bits): $r=B_w=1{,}7204$ MHz. Ver Dudas. |

### Trampas frecuentes

- Contar en $N$ las muestras de control («25+2» son 27).
- $f_s=2f_{\max}$, **no** $2W$, aunque den $f_{\min}$ (la cátedra muestrea con $f_{\max}$ cuando $f_{\min}\ll f_{\max}$).
- Con señales distintas en TDM, todas se muestrean con la $f_s$ de la más rápida.
- En «cuántas señales» se redondea **hacia abajo**; en «cuántos bits» el resultado es lo que entra en el canal.
- No confundir con FDM: si no dan bits por muestra, es FDM.

---

## 7. FDM: cantidad de señales, ancho de banda, portadoras

### Receta

Fuente: «Fórmulas y pasos» (FDM), «5 - Comunicaciones Digitales» págs. 9–10, respuesta impresa del final 18/02/2011.

Se reconoce porque hablan de señales analógicas «simultáneas», de canal analógico, o no dan bits por muestra.

| Magnitud | Fórmula |
|---|---|
| Ancho de banda (AM, doble banda lateral) | $B_w=\sum_i 2f_{\max,i}=N\cdot2f_{\max}$ |
| Ancho de banda del canal | $B_w=f_{\max\,corte}-f_{\min\,corte}$ |
| Ancho del mensaje | $W=f_{\max}-f_{\min}$ (la guía usa $W\approx f_{\max}$) |
| Portadoras | cada una en el centro de su banda de $2f_{\max}$: $f_{c,k}=f_{\min\,corte}+\sum_{j<k}2f_{\max,j}+f_{\max,k}$ |

Pasos:

1. $N=B_w/(2f_{\max})$ (redondeo hacia abajo) o $B_w=\sum2f_{\max,i}$.
2. Ubicar las bandas una al lado de la otra dentro del canal y dar las portadoras.
3. Técnica: **multiplexado FDM** con **modulación de amplitud (AM-DSB)**.
4. Gráficas:

```
 (1) Espectro de una señal          (2) Espectro modulado: dos bandas laterales
  A│╲   ╱                           A│      ╱│╲
   │ ╲ ╱                              │     ╱ │ ╲
 ──┴──┼──→ f                          └────┴──┼──┴──→ f
  -fmax 0 fmax                          fc-fmax fc fc+fmax   (ancho 2fmax)

 (3) Canal con N señales
  A│  ┌──────┬──────┬── ··· ──┬──────┐
   │  │ /│\  │ /│\  │         │ /│\  │
 ──┴──┴──────┴──────┴── ··· ──┴──────┴──→ f
     fmin corte  fc1    fc2         fcN   fmax corte
```

### Ejercicios

#### 7.1 — 18/02/2011 = 22/12/2005 — resuelto (con portadoras)

> Ancho de banda del canal para transmitir cuatro señales, si la frecuencia de corte máxima del canal es 200 MHz: $S_A$: $f_{\max}=6$ kHz; $S_B$: $f_{\min}=2$ kHz y $W=10$ kHz; $S_C$: $f_{\max}=10$ kHz, $f_{\min}=6$ kHz; $S_D$: $W=20$ kHz. Dar las portadoras; gráficos y justificación. (Rta impresa: $B_w=96$ kHz.)

1. $f_{\max}$ de cada una: $S_A=6$; $S_B=2+10=12$; $S_C=10$; $S_D=20$ kHz (banda base: $W=f_{\max}$).
2. Cada señal en AM-DSB ocupa $2f_{\max}$: 12, 24, 20 y 40 kHz.
3. $B_w=12+24+20+40=\mathbf{96\ kHz}$ ✓ (coincide con la respuesta del final).
4. Canal: de $200-0{,}096=199{,}904$ MHz a 200 MHz. Apilando desde arriba:
   - $S_D$: 199,960–200,000 MHz → $f_{cD}=199{,}980$ MHz
   - $S_B$: 199,936–199,960 MHz → $f_{cB}=199{,}948$ MHz
   - $S_C$: 199,916–199,936 MHz → $f_{cC}=199{,}926$ MHz
   - $S_A$: 199,904–199,916 MHz → $f_{cA}=199{,}910$ MHz
5. El orden es libre; lo que importa es que no se superpongan y que el total sea 96 kHz.

#### 7.2 — 15/02/2017 y 04/12/2015 — resuelto

> ¿Cuántas señales se pueden transmitir si cada una tiene $f_{\max}=20$ kHz (2017) / 10 kHz (2015), por un canal de 2 MHz? Multiplexado y modulación. Gráficas.

1. Sin bits → FDM con AM-DSB. Cada señal ocupa $2f_{\max}$.
2. 2017: $N=2\times10^6/(2\times20\times10^3)=\mathbf{50}$ señales.
3. 2015: $N=2\times10^6/(2\times10\times10^3)=\mathbf{100}$ señales.
4. Portadoras: $f_{c,k}=f_{\min\,corte}+(2k-1)f_{\max}$; por ejemplo, en 2017, 20, 60, 100 kHz… por encima del corte inferior.
5. *(Conocimiento general)* con banda lateral única entrarían el doble (100 y 200); la cátedra trabaja con doble banda.

#### 7.3 — F9 (y F8) — resuelto (frecuencia mínima de corte)

> Transmitir 200 señales como la del gráfico (espectro de −3,2 a 3,2 kHz) por un canal telefónico con frecuencia máxima de corte de 5 MHz. Diagrama, técnica, y ancho de banda mínimo para transmitir sin distorsión optimizando el rendimiento del canal.

1. $f_{\max}=3{,}2$ kHz; cada señal en AM-DSB ocupa 6,4 kHz.
2. $B_w=200\times6{,}4\ \text{kHz}=\mathbf{1{,}28\ MHz}$.
3. Para no desperdiciar canal: $f_{\min\,corte}=5-1{,}28=\mathbf{3{,}72\ MHz}$.
4. F8 (09/03/2000): 2000 señales iguales, $f_{\max\,corte}=15$ MHz → $B_w=12{,}8$ MHz, $f_{\min\,corte}=2{,}2$ MHz (igual a la resolución manuscrita de la hoja).

#### Resto (enunciado + resultados)

| Origen | Datos | Resultado |
|---|---|---|
| 28/08/2020 | 16 señales simultáneas: 1–4 $f_{\max}=16$ kHz; 5–8: 12 kHz; 9–12: 14 kHz; 13–16: 10 kHz | $B_w=4\cdot2(16+12+14+10)=\mathbf{416\ kHz}$; FDM + AM-DSB |
| F3 | Canal de 400 kHz con $f_{\max\,corte}=10{,}4$ MHz; señales de $W=40$ kHz | $N=400/(2\cdot40)=5$; canal 10,0–10,4 MHz; portadoras 10,04 / 10,12 / 10,20 / 10,28 / 10,36 MHz (coincide con el alumno) |
| F13 | $AB=200$ kHz, $f_{\max\,corte}=5{,}2$ MHz, señales de $f_{\max}=20$ kHz | $N=5$; canal 5,0–5,2 MHz; portadoras 5,02 / 5,06 / 5,10 / 5,14 / 5,18 MHz |
| F6 | Canal con $f_{\max}=5$ MHz y $AB=200$ kHz; señales con $f_{\max}=20$ kHz y $f_{\min}=16$ kHz | Con la regla de la cátedra ($2f_{\max}$): $N=5$, portadoras 4,82 / 4,86 / 4,90 / 4,94 / 4,98 MHz. Si se usa $2W$ ($W=4$ kHz): 25. Ver Dudas. |
| 23/09/2005 | 8 señales de $f_{\max}=3{,}8$ kHz, canal con $f_{\min}=450$ kHz. a) Técnica; b) ancho de banda mínimo sin distorsión. | FDM + AM-DSB; $B_w=8\times7{,}6=60{,}8$ kHz → canal 450–510,8 kHz; portadoras 453,8 + 7,6k kHz (453,8; 461,4; …; 507,0) |
| ¿07/02/2005? | 6 canales telefónicos de 4 kHz por un canal de 60 a 108 kHz (figura), modulación de amplitud: distribución de canales y portadoras | $6\times8=48$ kHz $=108-60$ ✓. Portadoras 64, 72, 80, 88, 96, 104 kHz |
| 25/02/2005 | Señales de $f_m=10$ kHz por FDM. a) Frecuencia mínima de muestreo y por qué. b) Canal de 1,2 MHz: ¿cuántas señales? | a) Nyquist: $f_s\ge2f_m=20$ kHz (para recuperar la señal; en FDM no hace falta muestrear, ver Dudas). b) $N=1{,}2\ \text{MHz}/20\ \text{kHz}=60$ |

### Trampas frecuentes

- La cátedra usa $2f_{\max}$ por señal, no $2W$, aunque la señal no arranque en 0 (respuesta oficial de 2011: 96 kHz).
- Si dan $W$ y $f_{\min}$, primero calculá $f_{\max}=f_{\min}+W$.
- Las portadoras van al **centro** de cada banda.
- «Sin distorsión» y «optimizando» → el canal tiene que medir exactamente $\sum2f_{\max}$ y empezar donde termina la última banda.

---

## 8. Teoría de colas — M/M/1 abierta

### Receta

Fuente: «Teoría de Colas» págs. 6–9 (fórmulas tomadas del Santo Resumen, que las transcribe), práctica «Ejercitación Teoría de cola».

| Magnitud | Fórmula |
|---|---|
| Frecuencia de arribo | $\lambda$ = arribos / tiempo de atención (¡pasar a la misma unidad!) |
| Tiempo medio de servicio | $E[s]=1/\mu$ |
| Factor de utilización | $\rho=\lambda E[s]=\lambda/\mu<1$ |
| Tiempo medio en cola | $W_q=\dfrac{\rho\,E[s]}{1-\rho}$ |
| Tiempo medio en el sistema | $W=W_q+E[s]=\dfrac{E[s]}{1-\rho}$ |
| Usuarios en cola (Little) | $L_q=\lambda W_q$ |
| Usuarios en el sistema (Little) | $L=\lambda W$ |

Pasos:

1. $\lambda$ = arribos por día ÷ minutos de atención del día (ej.: 7 a 14 h = 420 min).
2. $\rho=\lambda E[s]$; si $\rho\ge1$, un servidor no alcanza.
3. $W_q$, $W$, $L_q$, $L$ con las fórmulas. Definir cada término y poner unidades.
4. Problemas «inversos» (dan $L_q$, $W$, $\rho$): usar **sólo Little y $W=W_q+E[s]$**, porque esos datos no siempre son consistentes con M/M/1.

### Ejercicios

#### 8.1 — 04/04/2025 = 17/12/2021 = 20/11/2020 — resuelto

> Sala de emergencias atendida por un doctor. Llegadas Poisson, un paciente cada media hora. Atención exponencial, 20 min en promedio. a) Tiempo promedio que el paciente espera para ser atendido. b) Tiempo promedio en la sala de espera de emergencias. c) N° promedio de pacientes en cola. d) N° promedio de pacientes en sala de espera de emergencias.

1. $\lambda=1/30$ pac/min $=0{,}0333$ pac/min; $E[s]=20$ min ($\mu=0{,}05$ pac/min).
2. $\rho=\lambda E[s]=20/30=\mathbf{0{,}667}$ (el doctor está ocupado el 66,7 % del tiempo).
3. a) $W_q=\dfrac{0{,}667\times20}{1-0{,}667}=\mathbf{40\ min}$.
4. b) $W=W_q+E[s]=40+20=\mathbf{60\ min}$ (tiempo total en emergencias: espera + atención).
5. c) $L_q=\lambda W_q=40/30=\mathbf{1{,}33}$ pacientes.
6. d) $L=\lambda W=60/30=\mathbf{2}$ pacientes.

Interpretación de a)/b) y c)/d) en Dudas.

#### 8.2 — 19/11/2021 = 18/12/2020 (= ej. 3 de la práctica) — resuelto

> Caja única de 7 a 14 h. Arribos Poisson, 100 personas/día; servicio ≈ 3 min. Definiendo términos y unidades: a) tiempo promedio en cola; b) tiempo promedio en la empresa; c) N° de usuarios promedio en el sistema [en cola]; d) N° de usuarios promedio en la empresa.

1. Horario: 7 h = 420 min → $\lambda=100/420=\mathbf{0{,}2381}$ usuarios/min. $E[s]=3$ min ($\mu=0{,}333$/min).
2. $\rho=0{,}2381\times3=\mathbf{0{,}7143}$.
3. a) $W_q=\dfrac{0{,}7143\times3}{0{,}2857}=\mathbf{7{,}5\ min}$.
4. b) $W=7{,}5+3=\mathbf{10{,}5\ min}$.
5. c) $L_q=0{,}2381\times7{,}5=\mathbf{1{,}786}$ usuarios.
6. d) $L=0{,}2381\times10{,}5=\mathbf{2{,}5}$ usuarios.

La resolución del alumno del 18/12/2020 redondea $\rho=0{,}72$ y obtiene 7,7 / 10,7 / 1,85 / 2,57: diferencias de redondeo.

#### 8.3 — 18/02/2011 = 22/12/2005 — resuelto (inverso)

> Frecuencia de arribos 0,2 cliente/min, velocidad de atención 0,25 cliente/min, tiempo promedio en cola 16 min. ¿Factor de utilización y tiempo de servicio? (Rta impresa: 4 min y 0,8.)

1. $E[s]=1/\mu=1/0{,}25=\mathbf{4\ min}$.
2. $\rho=\lambda/\mu=0{,}2/0{,}25=\mathbf{0{,}8}$.
3. Control: $W_q=0{,}8\times4/0{,}2=16$ min ✓ (el dato es consistente con M/M/1).

#### 8.4 — F2 — resuelto (inverso, sólo Little)

> En un sanatorio el número de pacientes en cola para internación es 3, el tiempo total en el sistema 25 min y el factor de uso 0,6. Frecuencia de arribo, tiempo promedio en cola y tiempo de servicio.

1. Tres relaciones: $L_q=\lambda W_q$; $\rho=\lambda E[s]$; $W=W_q+E[s]$.
2. Multiplico la tercera por $\lambda$: $\lambda W=L_q+\rho\Rightarrow\lambda\cdot25=3+0{,}6\Rightarrow\lambda=\mathbf{0{,}144}$ pac/min.
3. $W_q=L_q/\lambda=3/0{,}144=\mathbf{20{,}83\ min}$.
4. $E[s]=\rho/\lambda=0{,}6/0{,}144=\mathbf{4{,}17\ min}$.
5. Ojo: con M/M/1 y $\rho=0{,}6$ sería $L_q=\rho^2/(1-\rho)=0{,}9$, no 3. Los datos no son M/M/1; por eso se resuelve sólo con Little.

#### Resto (enunciado + resultados)

| Origen | Datos | Resultado |
|---|---|---|
| F4 | Banco de 10 a 16 h, 30 personas/día, atención exponencial de 10 min. $\rho$, $W_q$, $W$, $L_q$, $L$. | $\lambda=30/360=0{,}0833$/min; $\rho=0{,}833$; $W_q=50$ min; $W=60$ min; $L_q=4{,}17$; $L=5$ (coincide con el alumno). |
| F6 | Servidor de impresión de 8 a 14 h, lunes a viernes; 70 trabajos/semana; impresión exponencial de 5 min/trabajo. Resultados en minutos. | Semana = 5 × 360 = 1800 min; $\lambda=0{,}0389$/min; $\rho=0{,}194$; $W_q=1{,}21$ min; $W=6{,}21$ min; $L_q=0{,}047$; $L=0{,}241$. |
| F1 = F13 = 17/02/2006 | $\lambda=0{,}015$ mensajes/s; «frecuencia [tiempo] de servicio» = 18 s/mensaje; longitud media 72 caracteres/mensaje. a) Factor de utilización; b) velocidad del servidor; c) tiempo de espera. | Con $E[s]=18$ s (así lo dice 17/02/2006): a) $\rho=0{,}015\times18=0{,}27$; b) $72/18=4$ caracteres/s; c) $W_q=0{,}27\times18/0{,}73=6{,}66$ s ($W=24{,}66$ s). La resolución del alumno lee 18 s como retardo total; ver Dudas. |
| 29/11/2002 (= práctica de capacidad) | Centro de cómputos: 120 mensajes/h; longitud exponencial de media 144 caracteres; servidor del enlace a 8 caracteres/s. a) Tiempo medio de espera; b) utilización del enlace. | $\lambda=1/30$ msj/s; $E[s]=144/8=18$ s; b) $\rho=0{,}6$; a) $W_q=27$ s ($W=45$ s). |
| 07/05/2004 | Aeropuerto: 10 pasajeros en cola, tiempo total en el sistema 30 min, factor de uso 0,9. Frecuencia de arribo, tiempo en cola, tiempo de servicio. | Igual que 8.4: $30\lambda=10+0{,}9\Rightarrow\lambda=0{,}363$/min; $W_q=27{,}52$ min; $E[s]=2{,}48$ min. (M/M/1 daría $L_q=8{,}1$: datos no M/M/1.) |

### Trampas frecuentes

- Unidades: $\lambda$ por minuto y $E[s]$ en minutos (o ambos en horas). «100 personas/día» se divide por los minutos **de atención**, no por 1440.
- $W$ incluye el servicio; $W_q$ no.
- Little vale siempre; las fórmulas de $W_q$ con $\rho$ sólo para M/M/1.
- $\rho\ge1$ → la cola crece sin límite: hay que decirlo, no seguir calculando.

---

## 9. Asignación de capacidad y retardo en un enlace

### Receta

Fuente: «Asignación de Capacidad de Canales» (Kleinrock, regla de la raíz cuadrada); fórmulas como las transcribe el Santo Resumen y la resolución del alumno de F3.

| Magnitud | Fórmula |
|---|---|
| Longitud media del mensaje | $1/\eta_i$ [bits/mensaje] |
| Tasa de servicio del enlace | $\mu_i=\eta_i C_i$ [mensajes/s] |
| Retardo medio en el enlace (M/M/1) | $T_i=\dfrac{1}{\eta_iC_i-\lambda_i}$ |
| Utilización | $\rho_i=\dfrac{\lambda_i}{\eta_iC_i}<1$ |
| Tráfico total y utilización de la red | $\gamma=\sum\lambda_i$; $\rho=\dfrac{1}{C}\sum\dfrac{\lambda_i}{\eta_i}$ |
| Capacidad óptima | $C_i^{opt}=\dfrac{\lambda_i}{\eta_i}+C(1-\rho)\dfrac{\sqrt{\lambda_i/\eta_i}}{\sum_j\sqrt{\lambda_j/\eta_j}}$ |
| Retardo mínimo de la red | $T_{\min}=\dfrac{\left(\sum_i\sqrt{\lambda_i/\eta_i}\right)^2}{\gamma\,C(1-\rho)}$ |

($\lambda_i/\eta_i=\lambda_i\cdot$ longitud media = tráfico ofrecido en bps.)

Pasos:

1. $\lambda_i$ de cada enlace = terminales del nodo × frecuencia por terminal (en mensajes/s).
2. Tabla con $\lambda_i$, $\lambda_i/\eta_i$ [bps], $\sqrt{\lambda_i/\eta_i}$, sumas.
3. $\rho$, $C(1-\rho)$, $C_i^{opt}$ (control: $\sum C_i^{opt}=C$), $T_i$ y $T_{\min}$.

### Ejercicios

#### 9.1 — F3 P3 — resuelto

> Capacidad total del sistema 3500 bps; longitud promedio de los mensajes 140 bits/mensaje; frecuencia 1 mensaje cada 25 s por terminal; red estrella de 6 nodos (terminales por nodo: 4, 6, 9, 8, 3, 12). a) Capacidades óptimas por enlace. b) Tiempo de retorno promedio mínimo de la red.

1. $\lambda_i=$ terminales$/25$ s:

```
 nodo  term  λi [msj/s]  λi/ηi [bps]  √(λi/ηi)   Ci opt [bps]   Ti [s]
  1     4     0,16         22,4        4,7329      444,37       0,3318
  2     6     0,24         33,6        5,7966      550,41       0,2709
  3     9     0,36         50,4        7,0993      683,36       0,2212
  4     8     0,32         44,8        6,6933      641,56       0,2346
  5     3     0,12         16,8        4,0988      382,24       0,3831
  6    12     0,48         67,2        8,1976      798,07       0,1916
  Σ    42     1,68        235,2       36,6183     3500,00
```

2. $\rho=235{,}2/3500=0{,}0672$; $C(1-\rho)=3264{,}8$ bps.
3. a) Ejemplo nodo 1: $C_1=22{,}4+3264{,}8\times4{,}7329/36{,}6183=22{,}4+421{,}97=444{,}37$ bps.
4. $T_1=1/(444{,}37/140-0{,}16)=1/(3{,}174-0{,}16)=0{,}3318$ s.
5. b) $T_{\min}=\dfrac{36{,}6183^2}{1{,}68\times3264{,}8}=\dfrac{1340{,}9}{5484{,}9}=\mathbf{0{,}2445\ s}$ (igual al promedio ponderado $\sum\lambda_iT_i/\gamma$).
6. «Opcional» de la resolución del alumno (un solo concentrador con toda la capacidad, 1 terminal): $T=1/(3500/140-1/25)=1/(25-0{,}04)=0{,}04$ s.

#### 9.2 — sin fecha (pág. 22) — resuelto

> Red estrella; capacidad total 5000 bps. Frecuencia de cada terminal 2 mensajes/min. Nodo 1: 6 terminales, 100 bits/mensaje; nodo 2: 4 terminales, 120 bits/mensaje; nodo 3: 8 terminales, 90 bits/mensaje. a) Capacidades óptimas (raíz cuadrada); b) tiempo de cada enlace; c) tiempo de respuesta de la red.

1. $\lambda_1=6\times2/60=0{,}2$; $\lambda_2=0{,}1333$; $\lambda_3=0{,}2667$ msj/s; $\gamma=0{,}6$.
2. $\lambda_i/\eta_i$: 20, 16, 24 bps (suma 60); raíces 4,4721; 4,0; 4,8990 (suma 13,3711).
3. $\rho=60/5000=0{,}012$; $C(1-\rho)=4940$ bps.
4. a) $C_1=1672{,}24$; $C_2=1493{,}81$; $C_3=1833{,}94$ bps (suman 5000).
5. b) $T_1=1/(1672{,}24/100-0{,}2)=0{,}0605$ s; $T_2=0{,}0812$ s; $T_3=0{,}0497$ s.
6. c) $T_{\min}=13{,}3711^2/(0{,}6\times4940)=\mathbf{0{,}0603\ s}$.

#### 9.3 — F10 = F11 — resuelto

> Nodo concentrador de 1200 bps al que llegan mensajes de 120 bits. a) Máxima frecuencia de arribos para que el retardo no exceda 2 s. b) Si $\lambda\to\eta_iC_i$, ¿qué pasa?

1. $\eta C=1200/120=10$ mensajes/s.
2. a) $T=\dfrac1{10-\lambda}\le2\Rightarrow10-\lambda\ge0{,}5\Rightarrow\lambda\le\mathbf{9{,}5}$ mensajes/s ($\rho=0{,}95$).
3. b) $\rho\to1$: el denominador tiende a 0 y el retardo crece sin límite (el buffer se llena; el enlace no da abasto).

### Trampas frecuentes

- $1/\eta$ es la **longitud** (bits/mensaje); $\eta C$ son mensajes/s.
- Verificar $\sum C_i^{opt}=C$.
- $\lambda$ por terminal × cantidad de terminales, y en mensajes **por segundo**.

---

## 10. Otros: entropía de fuente con capacidad de canal, y FSK

### 10.1 — F7 P1 — resuelto

> Se codifican los símbolos $s_i$ de una fuente equiprobable con un código cuyo alfabeto son pulsos de nivel (0,1,2,3,4) y longitud constante $l=16$. a) Entropía de la fuente. b) Si se transmiten por un canal de $C=0{,}625$ bps, duración mínima de los pulsos según Shannon. c) Velocidad de señalización en b). d) Con pulsos de 0,5 ms, capacidad necesaria.

Supuesto: la fuente tiene tantos símbolos como palabras posibles, $5^{16}$ (ver Dudas).

1. a) $H=\lg5^{16}=16\lg5=16(2{,}3219)=\mathbf{37{,}15}$ bits/símbolo.
2. b) Shannon: $R\le C$. $R=\dfrac{H}{16\tau}\le0{,}625\Rightarrow\tau\ge\dfrac{37{,}15}{16\times0{,}625}=\mathbf{3{,}715\ s}$.
3. c) $s=1/\tau=\mathbf{0{,}269}$ baudios.
4. d) $C\ge\dfrac{37{,}15}{16\times0{,}5\ \text{ms}}=\mathbf{4644\ bps}$.

### 10.2 — F5 P1 — parcial

> Fuente S de caracteres equiprobables, almacenados en un buffer y transmitidos por un canal de $C=1{,}25$ bps. Los $S_i$ se codifican con un código K de alfabeto (0,1,2,3); cada nivel es un pulso de duración $\tau$ en correspondencia biunívoca con los $k_i$. a) $\tau$ para que $R\le C$. b) Tiempo para transmitir un carácter. c) Codificar S en forma compacta. d) Rendimiento.

1. a) Cada pulso lleva como máximo $\lg4=2$ bits: $R=2/\tau\le1{,}25\Rightarrow\tau\ge\mathbf{1{,}6\ s}$.
2. b–d) Dependen de la cantidad de caracteres de S, que la hoja no da. El alumno supone 4 dígitos cuaternarios por carácter (8 bits): $T=8/1{,}25=6{,}4$ s. Ver Dudas.

### 10.3 — F5 P2 — modulación FSK

> Señal digital de ancho de pulso $\tau=100\ \mu s$ modulada en FSK con dos portadoras $f_{p1}$ y $f_{p2}$. Esquemas (banda base y modulada) con valores característicos y ancho de banda de transmisión.

1. Banda base: $s=1/\tau=10$ kbaudios; primer cero del espectro en $1/\tau=\mathbf{10\ kHz}$ (respuesta del alumno: $B_w=1/\tau=10$ kHz).
2. FSK = dos ASK superpuestas: un «1» enciende $f_{p1}$ y un «0» enciende $f_{p2}$.
3. *(Conocimiento general)* Cada ASK ocupa $\pm1/\tau$ alrededor de su portadora, así que $B_{FSK}\approx|f_{p2}-f_{p1}|+2/\tau=|f_{p2}-f_{p1}|+20$ kHz.
4. Gráficas: tren binario; portadora $f_{p1}$ en los «1»; portadora $f_{p2}$ en los «0»; suma (señal FSK de amplitud constante y frecuencia que salta).

---

## Dudas / pendientes

**Discrepancias de método**

1. **TDM, $B_w=1/\tau$ o $1/(2\tau)$.** La guía y el apunte 5 (pág. 24) usan el primer cruce por cero: $B_w=1/\tau=N\,n\,2f_{\max}$. El apunte 1 (pág. 12) dice que en binario $B=s/2=1/(2\tau)$ (Nyquist). El Santo Resumen marca la misma tensión. Usé $1/\tau$, que es lo que usan la guía y las resoluciones de alumnos (2020-12-18: 36 MHz; F1: 1440 kHz). Con Nyquist todos los $B_w$ de la sección 6 se dividen por 2.
2. **FDM, $2f_{\max}$ o $2W$.** La respuesta impresa del 18/02/2011 (96 kHz) usa $2f_{\max}$ también para la señal pasabanda $S_C$ (6–10 kHz). El Santo Resumen da $B_w=N\cdot2W$; con eso, en 2011 saldría 80 kHz. Seguí la respuesta oficial. Esto cambia el resultado en F6: 5 señales con $2f_{\max}$, 25 con $2W$.
3. **Redondeo de $I$ en el apunte resuelto (ej. 11 = 23/10/2020).** El apunte sube 76,15 bits a 77 y da $R=513$ kbps; el Santo Resumen copia ese 77. La información no se redondea: lo exacto es 76,15 bits y 507,7 kbps. En el final conviene escribir 76,15, aclarando que el apunte redondea.
4. **«Fórmulas y pasos» (FDM)** incluye «Tiempo de muestreo $T_s=T_m\times N$», que es de TDM; en FDM no hay muestreo. También dice que en Hamming «siempre da m=4, n=3»: vale para 9–16 mensajes; con 8 mensajes $m=3$ (F11).
5. **Colas F1/F13/2006** ($\lambda=0{,}015$, 18 s, 72 caracteres): F1 y F13 dicen «frecuencia de servicio = 18 seg/mensaje»; la hoja de 2006 dice «tiempo de servicio $T_s=18$ seg/mje». Tomé $E[s]=18$ s ($\rho=0{,}27$; 4 car/s; $W_q=6{,}66$ s). La resolución del alumno (resol-viejos-1, pág. 3) lo toma como retardo total del enlace: $T=1/(\eta C-\lambda)=18\Rightarrow C=5{,}08$ car/s, $\rho=0{,}21$, $W_q\approx3{,}8$ s («4 s»).
6. **Canal ternario F12**: el alumno obtiene $H(Y)=0{,}93$, $H(Y/X)=0{,}2$, $I=0{,}81$. Su $H(Y)$ deja afuera el término de $y_2$. Con la matriz reconstruida: $H(Y)=1{,}4570$, $H(Y/X)=0{,}5303$, $I=0{,}9267$ bits/símbolo.
7. **F3 (resolución del alumno)**: $T_{\min}=0{,}248$ s y $C_6=788$ bps, contra 0,2445 s y 798,07 bps de este banco. Son errores de redondeo en las raíces (usa $\sum\sqrt{\ }=36{,}58$). En el Huffman cuaternario, su $H_4$ y su redundancia no se leen bien («1,85», «0,50»): lo correcto es $H_4=1{,}377$, $\eta=0{,}956$, redundancia 0,044 ($L=1{,}44$ coincide).
8. **Errores en apuntes resueltos** (no son de finales, pero confunden): multinivel ej. 2 ($I=2{,}81$ en vez de 16,84 bits); Práctica N°1, $H(A,B)=1$ (lo correcto es 1,7147 bits); fuente telegráfica, $R=1{,}53$ bps (divide $H$ por la suma de duraciones; lo correcto es $H/\bar\tau=0{,}918/0{,}2667=3{,}44$ bps).

**Supuestos tomados**

9. **Multinivel sin $\tau$** (20/11/2020, 18/12/2020, 19/11/2021): el enunciado no da la duración del pulso; dejé $R$ en función de $\tau$. El alumno de 18/12/2020 supone 1 µs y usa $I=49$ bits (truncado; exacto 49,43).
10. **Sala de emergencias**: «espera para ser atendido» (a) y «espera en sala de espera» (b) significan casi lo mismo. Tomé a) $=W_q$ y b) $=W$ (total en emergencias). Lo mismo con c) $L_q$ y d) $L$. En la caja única, c) «en el sistema» lo tomé como $L_q$, siguiendo la hoja de práctica de origen («en la cola»).
11. **Sanatorio (F2) y aeropuerto (07/05/2004)**: los datos no cumplen M/M/1 ($L_q=\rho^2/(1-\rho)$ daría 0,9 y 8,1, no 3 y 10). Resolví sólo con Little.
12. **04/12/2015 (diseño de código lineal)**: no da cantidad de mensajes; elegí $n=5$, $m=3$.
13. **07/05/2004, b1) «$x_1,x_2,x_4$»**: puede ser un error triple simultáneo o tres errores simples por separado; están las dos respuestas. Los síndromes dependen de la $H$ elegida (no es única).
14. **F7**: «fuente equiprobable» sin cantidad de símbolos; supuse $5^{16}$ (una palabra código por símbolo).
15. **F9 P2**: supuse binarios los 9 pulsos de datos (la hoja no dice niveles).
16. **F12 PCM**: $n=15{,}99$. El alumno toma 16 bits (30,72 MHz > 30,7 MHz); estrictamente entran 15. La intención de la cátedra parece 16.
17. **10/09/2021**: $W=158{,}7$ Hz es irrealmente chico para «señales analógicas», pero sale de los datos. Con $B=1/(2\tau)$ daría 317,5 Hz.
18. **2012 / F7 P2**: canal pasabanda 100–300 MHz; usé $B_w=200$ MHz como la guía.
19. **25/02/2005 P3**: pide «frecuencia mínima de muestreo» en un problema FDM; respondí Nyquist (20 kHz) y aclaré que en FDM no se muestrea.

**Enunciados ilegibles o dudosos**

20. **13/03/2015 P1** (JPG muy borroso, 2 intentos de ampliación): la línea S5–S12 se lee «$f_{MAX}=2$ (¿3?) kHz, $w=2$ kHz» y los subíndices son dudosos. El resultado (2,048 MHz) no cambia mientras la mayor $f_{\max}$ sea la de S26–S30 ($1+3=4$ kHz). Si se aplicara «$w=f_{\max}$» a S26–S30 (3 kHz), daría 1,536 MHz. Los problemas 2 y 3 de esa hoja coinciden con 03/03/2006 P1 y con ¿07/02/2005? P3.
21. **21/02/2020, $P(a_1)=0{,}05$**: probable errata de 0,65 (el resto de la hoja es igual a 18/12/2015). Lo resolví tal cual.
22. **04/12/2015, «$P(a_1)=0$ y $P(b_1/a_1)=07$»**: verificado en el PDF original; resuelto literal ($I=0$). Probable errata.
23. **Pág. 20 del PDF viejo**: fecha «¿07/02/2005?» poco legible; la tabla de Huffman suma 0,97 ($P(a)=0{,}2575$, $P(c)=0{,}125$; quizá $P(a)=0{,}2875$); en el P3 no se lee la duración del pulso de inicio (resolví la versión de 13/03/2015).
24. **Pág. 22 del PDF viejo** (sin fecha): $p_e=0{,}1$ leído con dificultad; el armado de la trama (paridad, sincronismo y señalización) es ambiguo: interpretaciones A y B en la tabla de TDM.
25. **F3 P3**: la cantidad de terminales del nodo 3 no se lee en la hoja; tomé 9 de la resolución del alumno (encaja con su tabla: $\lambda_3=0{,}36$).
26. **F5 P1**: falta la cantidad de caracteres de la fuente; b–d no se pueden resolver sin un supuesto (el alumno supone caracteres de 8 bits).
27. **F8**: «14 mensajes» es lectura dudosa del manuscrito; no cambia el resultado ($m=4$, $n=3$).
28. **F12 canal ternario**: los subíndices de $P(y_1/x_1)$ y $P(y_1/x_3)$ se reconstruyeron con la resolución del alumno; con esa lectura el sistema cierra exacto ($P(y_2)=P(x_2)=0{,}3$).
29. **2020-12-18 (md vacío)**: el enunciado se tomó de los PNG escaneados; 15 pulsos, 75 señales de 30 kHz y caja 7–14 h.

**Contraste con el Santo Resumen**

30. Coincide en las fórmulas de multinivel, canal, Huffman ($\omega=r+\alpha(r-1)$), síndromes/familias, M/M/1 y raíz cuadrada. Difiere en FDM ($N\cdot2W$ contra $2f_{\max}$ de la respuesta oficial, punto 2) y repite el redondeo a 77 bits (punto 3). Su afirmación de que 2021 y 2025 repiten números se confirma: 19/11/2021 P1 = 04/04/2025 P2, y 17/12/2021 P3 = 04/04/2025 P3.
