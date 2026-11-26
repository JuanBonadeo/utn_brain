# Comunicación de Datos — Banco de ejercicios de finales (práctica)

Banco armado con **todos** los enunciados de práctica de finales que hay en `fuentes/finales/Práctica/` (2011–2025) y en el PDF «Comunicaciones - Finales Viejos» (finales del plan viejo, cátedra Di Santo, ~2000–2006). Cada número está verificado con Python.

Ampliado con las prácticas de la **cursada 2025 (com. 303: práctica Baró, teoría Medín)** de `fuentes/cursada-2025/`: práctica de multinivel de Baró, prácticas de codificación, colas y asignación de capacidad de Medín, el ejercicio del router, las resoluciones manuscritas escaneadas y los parciales que el alumno pasó a sus resúmenes (`drive-propio/`). El origen se marca así: «(práctica Baró 2025)», «(práctica Medín 2025)», «(parcial Baró, resumen del alumno)», «(cuaderno del alumno 2025)».

**Convenciones**

- $\lg x = \log_2 x$. En la calculadora: $\lg x = \ln x/\ln 2 \approx 3{,}32\,\log_{10} x$.
- Método de la cátedra: «Práctica - Fórmulas y pasos para los ejercicios» (Joel Arnold, 2020, **no oficial**), más los apuntes resueltos de práctica. Cuando algo sale de otro lado lo marco como *(conocimiento general)*. Cuando el método del «Santo Resumen» o de las resoluciones de alumnos difiere, queda anotado en «Dudas / pendientes» (al final).
- «F1»…«F13» son los «Examen Final N°k» del PDF de finales viejos (sin fecha). Las demás hojas viejas se citan por la fecha impresa.
- Los finales 2011–2021 y los viejos son del plan anterior. El único del plan actual es el del **04/04/2025**, y dos de sus tres problemas repiten números de 2021.

---

## Tabla de frecuencia

| Tipo de ejercicio | Finales 2011–2025 | Finales viejos (plan anterior) | Total finales | Cursada 2025 (com. 303) |
|---|---|---|---|---|
| §1. Transmisión multinivel ($M(T)$, $I$, $R$, $r$, $s$, duplicar $R$) | 18/02/2011, 09/03/2012, 13/03/2015, 15/02/2017, 28/08/2020, 23/10/2020, 20/11/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021, **04/04/2025** | F2, F6, F9 (×2), F10, 29/11/2002, ¿07/02/2005?, 25/02/2005, 23/09/2005, 22/12/2005, 03/03/2006 | **23** | Práctica Baró (11 ej., 1er parcial) + ejemplo de la teleimpresora |
| §6. TDM – PCM (ancho de banda de la trama) | 09/03/2012, 13/03/2015, 18/12/2015, 21/02/2020, 28/08/2020, 23/10/2020, 20/11/2020, 18/12/2020, 10/09/2021, 19/11/2021, **04/04/2025** | F1, F4, F7, F12, 17/02/2006, 03/03/2006, sin fecha (pág. 22) | **18** | Parciales de práctica de Baró (4 tramas en el resumen del alumno) |
| §8. Teoría de colas (M/M/1, M/M/c, modelo cerrado, costos) | 18/02/2011, 20/11/2020, 18/12/2020, 19/11/2021, 17/12/2021, **04/04/2025** | F1, F2, F4, F6, F13, 29/11/2002, 07/05/2004, 22/12/2005, 17/02/2006 | **15** | Práctica Medín (11 ej.), router/gateway, 2° parcial (propuestos) y parcial com. 305 |
| §7. FDM (cantidad de señales, ancho de banda, portadoras) | 18/02/2011, 04/12/2015, 15/02/2017, 28/08/2020 | F3, F6, F8, F9, F13, ¿07/02/2005?, 25/02/2005, 23/09/2005, 22/12/2005 | **13** | — |
| §2. Canal binario / ternario (entropías, información mutua) | 04/12/2015, 18/12/2015, 21/02/2020, 23/10/2020, 10/09/2021, 17/12/2021 | F12, sin fecha (pág. 22) | **8** | — (sólo teoría en el resumen del 1er parcial) |
| §3. Código compacto (Huffman), L, η, Kraft | 09/03/2012, 13/03/2015 | F3, F13, 29/11/2002, ¿07/02/2005?, 07/05/2004, 23/09/2005, 03/03/2006 | **9** | Práctica Medín de codificación (ej. 1–5: Kraft, fantasmas, Huffman cuaternario) |
| §4. Códigos lineales (H → G → V → síndromes, diseño) | 04/12/2015 | F1, F4, F5, F10, F11, 07/05/2004, 25/02/2005, 17/02/2006 | **9** | — |
| §5. Hamming | 18/12/2015, 15/02/2017, 21/02/2020 | F8, F12 | **5** | Práctica Medín ej. 6 (10 símbolos) |
| §9. Asignación de capacidad / retardo de enlace | — | F3, F10, F11, sin fecha (pág. 22) | **4** | Práctica Medín (3 ej.) + 2 redes del 2° parcial (estrella con ISP, árbol de 8 nodos) |
| §10. Entropía de fuente + Shannon; FSK | — | F5 (×2), F7 | **3** | — |
| §11. Atenuación, ganancia y dB | — | — | **0** | Teoría de Baró, 1er parcial (sin ejercicios numéricos) |

**Lectura rápida.** En las 9 hojas de 2020–2025 la práctica sale casi siempre de este menú: **multinivel** (8 de 9), **TDM-PCM** (8 de 9), y un tercer problema que alterna entre **canal binario simétrico** (siempre $P(a_1)=0{,}65$, $P(b_1/a_1)=0{,}75$) y **colas M/M/1** (sala de emergencias o caja única, con números repetidos). Hamming (último: 21/02/2020) y FDM (último: 28/08/2020) no volvieron. Huffman y códigos lineales son casi exclusivos de los finales viejos.

**Cursada 2025.** Baró tomó multinivel (1er parcial) y TDM-PCM (parciales de práctica); Medín, codificación, colas y asignación de capacidad. En colas, 2025 sumó tipos que ningún final tomó todavía: **M/M/2**, **modelo cerrado con punto de saturación** y **comparación de costos**. En capacidad sumó **redes en árbol**, donde los $\lambda$ se acumulan hacia el nodo central. Multinivel, TDM-PCM y la sala de emergencias se repiten con los mismos números que los finales.

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

#### 1.1 — 23/10/2020 (= ej. 11 del apunte resuelto = ej. 6 de la práctica Baró 2025) — resuelto

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

#### 1.6 — práctica Baró 2025, ej. 9 (= ej. 14 del apunte resuelto) — resuelto (dos subsistemas, unidades mezcladas)

> Transmisión con dos subsistemas (según el esquema): un bloque de 5 pulsos de 7 niveles (el 0 cuenta) que dura 100 µs y un bloque de 8 pulsos binarios que dura 40 ms. a) Pulsos y niveles de cada subsistema. b) $M(T)$. c) $I_x$. d) $R$. e) ¿Cómo duplicar $R$ sin variar la duración de los pulsos ni el período $T$?

1. a) Bloque 1: $n_1=5$, $\mu_1=7$. Bloque 2: $n_2=8$, $\mu_2=2$.
2. b) Los mensajes se multiplican: $M(T)=7^5\cdot2^8=16807\times256=4\,302\,592$ mensajes.
3. c) La información se suma: $I=5\lg7+8\lg2=14{,}04+8=\mathbf{22{,}04}$ bits.
4. d) $T=100\ \mu s+40\ ms=40{,}1$ ms (pasar a la misma unidad) → $R=22{,}04/40{,}1\ ms=\mathbf{549{,}5}$ bps.
5. e) Con $T$ fijo, duplicar $R$ es duplicar $I$. Tocando sólo los niveles del bloque multinivel:
   - $5\lg\mu'+8=2(5\lg7+8)\Rightarrow\lg\mu'=2\lg7+1{,}6=7{,}215$
   - $\mu'=2^{7{,}215}=148{,}5\Rightarrow$ **149 niveles** (redondeo para arriba).
   - La resolución de la práctica toma $\lg7\approx2{,}8$ ($I=22$ bits, $2R=1097$ bps) y llega a $\mu'=146{,}8\to147$. Con 147 niveles $R=1097{,}2$ bps, que no llega al doble exacto (1099,1 bps). Ver Dudas.

#### 1.7 — práctica Baró 2025, ej. 10 (= ej. 15 del apunte; sin resolución en la fuente) — resuelto

> Grupos de 13 pulsos de 58 niveles, más 1 pulso de arranque y 1 de stop de amplitud fija. El período dura 100 µs y todos los pulsos duran lo mismo. a) $I_x$. b) $R$. c) ¿Cómo duplicar la velocidad sin variar la duración de los pulsos ni el período? d) Gráfica.

1. $N=15$ pulsos en $T=100\ \mu s$ → $\tau=100/15=6{,}67\ \mu s$.
2. a) $I=13\lg58=\mathbf{76{,}15}$ bits (arranque y stop no informan).
3. b) $R=76{,}15/100\ \mu s=\mathbf{761{,}5}$ kbps.
4. c) Sólo quedan los niveles: $13\lg\mu'=2\cdot13\lg58\Rightarrow\mu'=58^2=\mathbf{3364}$ niveles.
   - Regla: si todos los pulsos de información tienen el mismo $\mu$, duplicar $I$ con los mismos pulsos es **elevar los niveles al cuadrado** (cuadruplicar: a la cuarta).
5. d) Gráfica como en 1.1, con $\tau=6{,}67\ \mu s$ y $T=100\ \mu s$.

#### 1.8 — práctica Baró 2025, ej. 11 (= ej. 16 del apunte) — resuelto (la incógnita es la cantidad de pulsos)

> Dos subsistemas: 5 pulsos de 6 niveles y $n$ pulsos binarios. Todos los pulsos duran lo mismo y $T=500\ \mu s$. a) Niveles y pulsos de cada subsistema. b) $I_x$. c) $R$. d) ¿Cómo duplicar $R$ sin variar la duración de los pulsos ni el período? e) Si $R=5$ Mbps, ¿cuántos pulsos son binarios?

1. a) Bloque 1: 5 pulsos, $\mu=6$ ($M_1=6^5=7776$). Bloque 2: $n$ pulsos, $\mu=2$ ($M_2=2^n$).
2. b) $I=5\lg6+n=12{,}92+n$ bits. c) $R=(12{,}92+n)/500\ \mu s$. Los dos quedan en función de $n$.
3. e) $I=R\,T=5\times10^6\times500\times10^{-6}=2500$ bits $\Rightarrow n=2500-12{,}92=2487{,}08$.
   - Con $n=2487$, $R=4{,}99985$ Mbps (apenas menos). Para **alcanzar** 5 Mbps hacen falta **2488** binarios. La práctica da 2487.
4. d) Con $n=2488$, duplicar $R$ es llegar a $I=5000$ bits con los mismos pulsos:
   - Sólo con el bloque de 6 niveles: $5\lg\mu'=5000-2488\Rightarrow\lg\mu'=502{,}4$. Absurdo ($2^{502}$ niveles).
   - Con los binarios: $2488\lg\mu_b=5000-12{,}92\Rightarrow\lg\mu_b=2{,}004\Rightarrow\mu_b=4{,}01\Rightarrow$ **5 niveles**. Con 4 niveles quedan 4988,9 bits: no alcanza.
   - La práctica deja d) planteado, porque lo resuelve antes de conocer $n$.

#### Resto de los multinivel (enunciado + resultados)

| Origen | Enunciado (resumido) | Resultados |
|---|---|---|
| 10/09/2021 | 1 arranque fijo, 10 datos de 128 niveles, 1 stop; todos 5 ms salvo stop 7 ms. a) $R$; b) datos binarios. | $T=62$ ms; $I=70$ bits; $R=1129$ bps. b) $I=10$ bits, $R=161{,}3$ bps. |
| 17/12/2021 (= ej. 12 apunte = ej. 7 práctica Baró 2025) | 10 pulsos de 64 niveles, sin control, 2 ms c/u. a) mensajes; b) $I_x$; c) $R$; d) gráfica. | $M=64^{10}=2^{60}\approx1{,}15\times10^{18}$; $I=60$ bits; $T=20$ ms; $R=3$ kbps. |
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
| práctica Baró 2025, ej. 1 (gráfico) | 6 pulsos binarios (+2 y −2 V). $\mu$, $n$, $I$, $M(T)$. | $\mu=2$; $n=6$; $I=6$ bits; $M=64$. |
| práctica Baró 2025, ej. 2 (gráfico, = ej. 2 apunte) | 6 pulsos de 7 niveles (−3…+3), $T=100$ ms. | $M=7^6=117\,649$; $I=6\lg7=16{,}84$ bits; $R=168{,}4$ bps. La práctica 2025 repite el error del apunte ($I=2{,}81$ bits, $R=28{,}1$ bps). |
| práctica Baró 2025, ej. 3 (= ej. 3 apunte) | 18 pulsos de 128 niveles, 1 ms c/u. $M(T)$, $I$, $R$, gráfica. | $M=128^{18}=2^{126}$; $I=126$ bits; $T=18$ ms; $R=7$ kbps (coincide). |
| práctica Baró 2025, ej. 4 (gráfico) | 6 pulsos de 4 niveles (4, 2, 0, −2), $T=60\ \mu s$. | $M=4^6=4096$; $I=12$ bits; $R=200$ kbps (coincide). |
| práctica Baró 2025, ej. 5 (gráfico, = ej. 7 apunte) | 5 pulsos binarios (0 y 2), $T=30\ \mu s$. | $M=32$; $I=5$ bits. ($R=166{,}7$ kbps, no lo pide.) |
| práctica Baró 2025, ej. 8 (= ej. 13 apunte) | Fax de 400 líneas × 400 puntos, 64 niveles de brillo equiprobables, a 4800 bps. ¿Cuánto tarda una imagen? | $I=160\,000\times\lg64=960\,000$ bits; $T=I/R=\mathbf{200\ s}$ (coincide). |
| Teoría Baró 2025 («Velocidades de transmisión…») | Teleimpresora: arranque y 5 pulsos de letra de 20 ms c/u, parada de 30 ms. $s$, $r$, $R$. | $T=150$ ms; $s=1/20\ ms=50$ baudios; $r=7/0{,}15=46{,}7$ binits/s; $R=5/0{,}15=33{,}3$ bps. Siempre $R<r\le s$ (la fuente redondea $r$ a 46). |

### Trampas frecuentes

- **$T$ incluye arranque, parada y todo pulso de control**; $I$ no. Error típico: dividir $I$ por el tiempo de los pulsos de información solamente.
- Contar mal los niveles: «entre +5 y −5 incluido el 0» son 11, no 10.
- $s$ usa el pulso **más corto**, aunque sea el de arranque.
- Redondear niveles **hacia arriba** (con menos no se alcanza la $R$ pedida).
- Si el enunciado no da $\tau$, dejá $R$ en función de $\tau$ y aclaralo; no inventes un valor sin decirlo.
- El ejercicio 2 del apunte resuelto tiene un error: escribe $I=\lg7^6=2{,}81$ bits (es $\lg7$). Lo correcto es $I=6\lg7=16{,}84$ bits y $R=168{,}4$ bps. La práctica de Baró 2025 (ej. 2) lo repite.
- No redondees $\lg\mu$ en pasos intermedios cuando después despejás un exponente: $\lg7\approx2{,}8$ en vez de 2,807 mueve la respuesta de 149 a 147 niveles (1.6).
- Si dan $T$ y «todos los pulsos duran lo mismo», $\tau=T/N$ con $N$ = **todos** los pulsos (1.7).

---

## 2. Canal binario simétrico y canal ternario — entropías e información mutua

### Receta

Fuente: «Fórmulas y pasos», «1 - Información, Codificación y Canales».

| Paso | Fórmula |
|---|---|
| Matriz del CBS ($p$ = probabilidad de **error**) | $P(b_2/a_1)=P(b_1/a_2)=p$, $P(b_1/a_1)=P(b_2/a_2)=1-p$ |
| Probabilidad de salida | $P(b_j)=\sum_i P(a_i)\,P(b_j/a_i)$ |
| Conjunta | $P(a_i,b_j)=P(a_i)\,P(b_j/a_i)$ |
| Hacia atrás (Bayes) | $P(a_i/b_j)=\dfrac{P(a_i)\,P(b_j/a_i)}{P(b_j)}$ |
| Entropía de entrada | $H(A)=\sum_i P(a_i)\lg\dfrac{1}{P(a_i)}$ |
| Entropía de salida | $H(B)=\sum_j P(b_j)\lg\dfrac{1}{P(b_j)}$ |
| Entropía del canal (equivocación de B respecto de A) | $H(B/A)=\sum_i\sum_j P(a_i)\,P(b_j/a_i)\lg\dfrac{1}{P(b_j/a_i)}$ |
| Información mutua | $I(A,B)=H(B)-H(B/A)$ [bits/símbolo] |

Atajo útil en el CBS: $H(B/A)=H(p)=p\lg\frac1p+(1-p)\lg\frac1{1-p}$, **no depende de $P(a_1)$**. Como $H(p)=H(1-p)$, da lo mismo usar la probabilidad de error o la de acierto, pero en este banco, en la wiki y en el resumen $p$ es siempre la de **error**: en los finales, $P(b_1/a_1)=0{,}75$ es el acierto y $p=0{,}25$.

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
   - Suma: $H(B/A)=\mathbf{0{,}8113}$ bits/símbolo (igual a $H(p)=H(0{,}25)$).
5. c) $I(A,B)=0{,}9837-0{,}8113=\mathbf{0{,}1724}$ bits/símbolo. De cada símbolo emitido, que trae $H(A)=0{,}934$ bits, llegan efectivamente 0,172 bits; el resto lo «tapa» el ruido del canal (error del 25 %).

#### 2.2 — 21/02/2020 — resuelto ($P(a_1)=0{,}05$)

> Canal binario simétrico, $P(a_1)=0{,}05$, $P(b_1/a_1)=0{,}75$. Mismas preguntas.

1. $P(b_1)=0{,}05(0{,}75)+0{,}95(0{,}25)=0{,}0375+0{,}2375=0{,}275$; $P(b_2)=0{,}725$.
2. a) $H(B)=0{,}5122+0{,}3364=\mathbf{0{,}8485}$ bits/símbolo.
3. b) $H(B/A)=H(0{,}25)=\mathbf{0{,}8113}$ bits/símbolo (mismo canal).
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
- La «Práctica N°1 RESUELTO» calcula $H(A,B)$ sumando probabilidades (da «1»). Es incorrecto: con $P(a_i)=(0{,}45;0{,}55)$ y probabilidad de acierto $1-p=0{,}8$ ($p=0{,}2$), las conjuntas son 0,36; 0,09; 0,11; 0,44 y $H(A,B)=1{,}7147$ bits.

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

#### 3.4 — práctica Medín 2025, ej. 5 — resuelto (cuaternario con fantasmas; comparación con $r=3$ y $r=11$)

> Fuente S: $S_1=0{,}15$, $S_2=0{,}04$, $S_3=0{,}08$, $S_4=0{,}12$, $S_5=0{,}10$, $S_6=0{,}03$, $S_7=0{,}22$, $S_8=0{,}05$, $S_9=0{,}06$, $S_{10}=0{,}1$, $S_{11}=0{,}05$. a) Código cuaternario por Huffman. b) Rendimiento. c) Redundancia. d) Si codificamos con tres niveles, ¿el rendimiento aumenta o disminuye? e) Mínimo número de señales para obtener la mínima longitud; valor de $L$. f) Código compacto de e). g) Inconveniente de e).

La tabla de probabilidades se leyó del PDF: el .md convertido la perdió (suma 1 ✓).

1. $\omega=11$, $r=4$: $11=4+3\alpha\Rightarrow\alpha=2{,}33$ → agrego **2 fantasmas** $z_1,z_2$ con $P=0$ ($\omega=13$, $\alpha=3$).
2. Reducciones (de a 4; $A=S_2+S_6+z_1+z_2=0{,}07$, $B=A+S_9+S_8+S_{11}=0{,}23$, $C=S_4+S_5+S_{10}+S_3=0{,}40$):

| $S_0$ | $S_1$ | $S_2$ | $S_3$ → dígito |
|---|---|---|---|
| $S_7$ 0,22 | $S_7$ 0,22 | $B$ 0,23 | $C$ 0,40 → 0 |
| $S_1$ 0,15 | $S_1$ 0,15 | $S_7$ 0,22 | $B$ 0,23 → 1 |
| $S_4$ 0,12 | $S_4$ 0,12 | $S_1$ 0,15 | $S_7$ 0,22 → 2 |
| $S_5$ 0,10 | $S_5$ 0,10 | $S_4$ 0,12 | $S_1$ 0,15 → 3 |
| $S_{10}$ 0,10 | $S_{10}$ 0,10 | $S_5$ 0,10 | |
| $S_3$ 0,08 | $S_3$ 0,08 | $S_{10}$ 0,10 | |
| $S_9$ 0,06 | $A$ 0,07 | $S_3$ 0,08 | |
| $S_8$ 0,05 | $S_9$ 0,06 | | |
| $S_{11}$ 0,05 | $S_8$ 0,05 | | |
| $S_2$ 0,04 | $S_{11}$ 0,05 | | |
| $S_6$ 0,03 | | | |
| $z_1$ 0 | | | |
| $z_2$ 0 | | | |

3. Vuelta atrás: $S_7=2$, $S_1=3$; $C=0$ → $S_4=00$, $S_5=01$, $S_{10}=02$, $S_3=03$; $B=1$ → $A=10$, $S_9=11$, $S_8=12$, $S_{11}=13$; $A=10$ → $S_2=100$, $S_6=101$ (102 y 103 son de los fantasmas, se descartan).
4. a) $L=1(0{,}22+0{,}15)+2(0{,}12+0{,}10+0{,}10+0{,}08+0{,}06+0{,}05+0{,}05)+3(0{,}04+0{,}03)=0{,}37+1{,}12+0{,}21=\mathbf{1{,}70}$ cuaternarios/símbolo.
5. b) $H(S)=3{,}2273$ bits/símbolo; $H_4=3{,}2273/2=1{,}6137$; $\eta=1{,}6137/1{,}70=\mathbf{0{,}9492}$.
6. c) Redundancia $=1-\eta=\mathbf{0{,}0508}$. Kraft: $2\cdot4^{-1}+7\cdot4^{-2}+2\cdot4^{-3}=0{,}96875$; lo que falta hasta 1 son las ramas de los fantasmas.
7. d) Ternario: $11=3+2\cdot4$, **sin fantasmas**. Huffman ternario: $S_7=2$; $S_1=01$, $S_4=02$, $S_5=11$, $S_{10}=12$; $S_3=000$, $S_9=001$, $S_8=002$, $S_{11}=100$, $S_2=101$, $S_6=102$.
   - $L_3=0{,}22+2(0{,}47)+3(0{,}31)=\mathbf{2{,}09}$ ternarios/símbolo; $H_3=3{,}2273/1{,}585=2{,}0362$; $\eta=\mathbf{0{,}9743}$.
   - El rendimiento **aumenta** (0,949 → 0,974): en cuaternario se desperdician dos ramas en fantasmas; en ternario no hace falta ninguno.
8. e) La longitud mínima posible es $L=1$: una señal distinta por símbolo → **11 señales** (niveles), $L=\mathbf{1}$.
9. f) Código 11-ario: $S_1\to0$, $S_2\to1$, …, $S_{11}\to10$. Rendimiento $\eta=H/\lg11=3{,}2273/3{,}4594=0{,}9329$.
10. g) Inconvenientes: hacen falta 11 niveles distinguibles; con la misma potencia quedan más juntos y el ruido los confunde más, y el equipo es más complejo *(conocimiento general)*. Además el rendimiento baja (0,933): con longitud fija ya no se aprovecha que unos símbolos sean más probables que otros.

#### Resto (enunciado + resultados)

| Origen | Fuente y pedido | Resultado |
|---|---|---|
| F13 = 07/05/2004 | Ternario (A,B,C / a,b,c): $S_1=0{,}22$, $S_2=0{,}03$, $S_3=0{,}12$, $S_4=0{,}03$, $S_5=0{,}02$, $S_6=0{,}11$, $S_7=0{,}11$, $S_8=0{,}33$, $S_9=0{,}03$. Longitud media y redundancia. | $\omega=9=3+2\cdot3$, sin falsos. Longitudes: $S_8$→1; $S_1,S_3,S_6,S_7,S_9$→2; $S_2,S_4,S_5$→3. Una solución: $S_8=B$, $S_1=AA$, $S_3=AB$, $S_7=AC$, $S_6=CA$, $S_9=CC$, $S_2=CBA$, $S_4=CBB$, $S_5=CBC$. $L=1{,}75$; $H=2{,}6442$ bits; $H_3=1{,}6683$; $\eta=0{,}9533$; redundancia $0{,}0467$. |
| 23/09/2005 | Ternario con alfabeto (1,2,3): $a=0{,}2$, $b=0{,}15$, $c=0{,}35$, $d=0{,}02$, $e=0{,}04$, $f=0{,}15$, $g=0{,}06$, $h=0{,}02$, $i=0{,}01$. ¿Otro instantáneo más corto? $L$ y «velocidad de información». | Sin falsos. $c=2$, $a=3$, $b=11$, $f=12$, $g=131$, $e=133$, $d=1321$, $h=1322$, $i=1323$. $L=1{,}65$; $H=2{,}5371$ bits; $H_3=1{,}6007$; $\eta=0{,}9701$. No hay instantáneo más corto. $R$ no se puede calcular: no se da la duración de los dígitos. |
| 29/11/2002 | Ternario: $A=0{,}2$, $B=0{,}04$, $C=0{,}05$, $D=0{,}01$, $E=0{,}1$, $F=0{,}06$, $G=0{,}025$, $H=0{,}3$, $I=0{,}2$, $J=0{,}015$. $L$ y rendimiento; ¿otro más corto? | $\omega=10$ → 1 falso. $H=1$; $A=00$, $I=01$, $E=02$, $F=21$, $C=22$, $B=200$, $G=201$, $J=2020$, $D=2021$. $L=1{,}815$; $H=2{,}7178$ bits; $H_3=1{,}7147$; $\eta=0{,}9448$. |
| ¿07/02/2005? | Igual a 3.2 pero con $P(a)=0{,}2575$, $P(c)=0{,}125$ (la tabla suma 0,97). | Ver Dudas. Con esos pesos (normalizados): $L=1{,}7655$, $\eta=0{,}9300$. |
| F5 P1 c-d | Codificar en forma compacta con $k_i=0,1,2,3$ una fuente de caracteres equiprobables. | Falta la cantidad de caracteres de la fuente → ver Dudas. |
| práctica Medín 2025, ej. 1 | Fuente con longitudes $l=3,5,3,3$. ¿Puede hallarse un código instantáneo? | Supongo binario (la hoja no da $r$). Kraft: $3\cdot2^{-3}+2^{-5}=0{,}40625\le1$ → **sí**, por ejemplo 000, 01100, 010, 001. |
| práctica Medín 2025, ej. 2 | $S_1=0$, $S_2=00$, $S_3=11$: verificar que cumple Kraft pero no es instantáneo. | $2^{-1}+2\cdot2^{-2}=1\le1$, pero 0 es prefijo de 00. Con las mismas longitudes 1, 2, 2 sí existe uno: 0, 10, 11. |
| práctica Medín 2025, ej. 3 | $P=1/2,\ 1/4,\ 1/8,\ 1/8$. ¿Se cumple $L=H$? Código instantáneo con esas longitudes. | $l_i=\lg(1/P_i)=1,2,3,3$ → 0, 10, 110, 111; $L=H=1{,}75$ bits/símbolo, $\eta=1$ (probabilidades potencias de 1/2). |
| práctica Medín 2025, ej. 4 | ¿Hay que agregar fantasmas? a) $\omega=13$, $r=4$. b) $\omega=14$, $r=4$. | a) $\alpha=(13-4)/3=3$ entero → **no**. b) $\alpha=10/3$ → agregar **2** ($16=4+3\cdot4$). |

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

#### 5.4 — práctica Medín 2025, ej. 6 — resuelto

> Transmitir un alfabeto de 10 símbolos con un código de longitud constante. a) Codificar de forma que, controlando paridad por zonas, se detecten y corrijan errores unitarios (la corrección se hace al recibir cada palabra). b) Ejemplo con un error en algún dígito.

1. a) $2^m\ge10\Rightarrow m=4$ (se usan 10 de las 16 combinaciones); $2^n\ge n+5\Rightarrow n=3$ → palabras de 7 dígitos, todas de la misma longitud.
2. Zonas, ecuaciones y tabla: las de la receta. Se asignan, por ejemplo, las 10 primeras filas a $S_1\dots S_{10}$.
3. b) Envío $I=1001$: $C_1=1\oplus0\oplus1=0$, $C_2=1\oplus0\oplus1=0$, $C_3=0\oplus0\oplus1=1$ → tira $C_1C_2I_1C_3I_2I_3I_4=0\,0\,1\,1\,0\,0\,1$ (fila 1001|001 de la tabla ✓).
   - Llega $0\,0\,1\,1\,\mathbf{1}\,0\,1$ (error en la posición 5, $I_2$).
   - Con la información recibida $I=1101$ recalculo $C_1C_2C_3=1\,0\,0$; los recibidos son $0\,0\,1$.
   - Diferencia: $C_1=1$, $C_2=0$, $C_3=1$ → $C_3C_2C_1=101_2=5$ → corrijo la posición 5: $I=1001$ ✓.

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

#### 6.5 — parcial Baró (resumen del alumno, cursada 2025) — resuelto (bits de control por canal y por trama)

> Transmitir 24 señales de voz ($f_{\max}=4$ kHz) codificadas con 7 bits por canal, agregando 1 bit de sincronismo **por canal** y 1 bit de señalización **por trama**. Velocidad de transmisión.

1. $f_s=2f_{\max}=8$ kHz → $T_s=125\ \mu s$.
2. Bits por trama: $24\times7+24\times1+1=\mathbf{193}$.
3. $\tau=125\ \mu s/193=0{,}6477\ \mu s$ → $r=1/\tau=193\times8000=\mathbf{1{,}544\ Mbps}$ (coincide con el alumno; es la trama T1 *(conocimiento general)*).
4. Diferencia con 6.1: el control viene en **bits** sueltos, no en muestras enteras; no sirve $N\,n\,2f_{\max}$ directo, hay que contar los bits de la trama.

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
| Parcial Baró (resumen del alumno, «Primer ejercicio») | 30 señales de voz + 2 de control (señalización y sincronismo), $f_{\max}=4$ kHz. Velocidad. No da bits: el alumno supone 8 («por práctica común»). | $N=32$; $T_s=125\ \mu s$; $T_m=3{,}906\ \mu s$; $\tau=488{,}3$ ns; $r=\mathbf{2{,}048}$ Mbps (E1). El alumno da 487,5 ns y 2,05 Mbps por redondear $T_m=3{,}9\ \mu s$. |
| «Parcial random» de Baró (resumen del alumno) | Trama de 25 muestras + 2 de control, $f_{\max}=3000$ Hz, 7 bits. Ancho de banda, técnicas, gráficos. Además: definir ancho de banda, portadora, muestreo, cuantificación y codificación. | $f_s=6$ kHz; $T_s=166{,}7\ \mu s$; $T_m=6{,}173\ \mu s$; $\tau=0{,}8818\ \mu s$; $B_w=27\cdot7\cdot6000=\mathbf{1{,}134}$ MHz; TDM-PCM. (El alumno escribe «mHz» y primero 1,136 MHz, por redondeo.) |
| «Otro parcial» de Baró (resumen del alumno) | Trama de 38 muestras + 2 de control, $f_{\max}=5$ kHz, 8 dígitos. Velocidad $r$, gráficos y técnicas. Además: definir tasa de Nyquist, PDM y armónico de Fourier. | $f_s=10$ kHz; $T_s=100\ \mu s$; $T_m=2{,}5\ \mu s$; $\tau=0{,}3125\ \mu s$; $r=40\cdot8\cdot10\,000=\mathbf{3{,}2}$ Mbps. **El alumno pone $T_s=0{,}1\ \mu s$ y llega a 3,2 Gbps**: error de unidades (es 0,1 ms). |

### Trampas frecuentes

- Contar en $N$ las muestras de control («25+2» son 27).
- $f_s=2f_{\max}$, **no** $2W$, aunque den $f_{\min}$ (la cátedra muestrea con $f_{\max}$ cuando $f_{\min}\ll f_{\max}$).
- Con señales distintas en TDM, todas se muestrean con la $f_s$ de la más rápida.
- En «cuántas señales» se redondea **hacia abajo**; en «cuántos bits» el resultado es lo que entra en el canal.
- No confundir con FDM: si no dan bits por muestra, es FDM. Excepción en los parciales de Baró: «señales de voz» sin bits → TDM con 8 bits supuestos (decilo explícitamente).
- Si el control viene en bits por canal o por trama (no en muestras), contá los bits de la trama (6.5).
- $1/10\ \text{kHz}=0{,}1$ **ms**, no 0,1 µs: verificá el orden de magnitud de $r$ (Mbps para tramas de voz, no Gbps).

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

## 8. Teoría de colas — M/M/1, M/M/c, modelo cerrado y costos

### Receta

Fuente: «Teoría de Colas» págs. 6–9 (fórmulas tomadas del Santo Resumen, que las transcribe), práctica «Ejercitación Teoría de cola» (= «5 - Práctica Teoría de Cola», Medín 2025), resolución manuscrita de Medín (escaneos), wiki Unidad 6.

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
5. Si con un servidor da $\rho\ge1$: calcular $u=\lambda E[s]$ y probar $c=\lceil u\rceil,\lceil u\rceil+1,\dots$ con M/M/c hasta cumplir lo pedido.

**Percentil 90** (lo pide toda la práctica de Medín 2025):

| Magnitud | Fórmula |
|---|---|
| $\pi_q(90)$, M/M/1: tiempo en cola que no supera el 90 % de los usuarios | $\pi_q(90)=W\ln(10\rho)$ |
| $\pi_w(90)$, M/M/1: tiempo en el sistema *(conocimiento general)* | $\pi_w(90)=W\ln10\approx2{,}3\,W$ |

Si $\rho\le0{,}1$, $\pi_q(90)=0$: más del 90 % no espera nada *(conocimiento general)*.

**M/M/c: $c$ servidores con una sola cola.** Fórmulas de la wiki (Unidad 6), reconstruidas con conocimiento general porque en los apuntes son imágenes:

| Magnitud | Fórmula |
|---|---|
| Intensidad de tráfico | $u=\lambda E[s]$ [Erlang]; hace falta $c>u$ |
| Utilización de cada servidor | $\rho=u/c<1$ |
| Probabilidad de sistema vacío | $P_0=\left[\displaystyle\sum_{n=0}^{c-1}\frac{u^n}{n!}+\frac{u^c}{c!\,(1-\rho)}\right]^{-1}$ |
| Erlang C (probabilidad de tener que esperar) | $C(c,u)=\dfrac{u^c}{c!\,(1-\rho)}\,P_0$ |
| Tiempo en cola | $W_q=\dfrac{C(c,u)\,E[s]}{c\,(1-\rho)}$ |
| Resto | $W=W_q+E[s]$; $L_q=\lambda W_q$; $L=\lambda W$ |
| Percentil 90 en cola | $\pi_q(90)=\dfrac{E[s]}{c(1-\rho)}\ln\big(10\,C(c,u)\big)$ |

Con $c=1$: $C=\rho$ y se vuelve a M/M/1. Con $c=2$: $P_0=\left[1+u+\dfrac{u^2}{2(1-\rho)}\right]^{-1}$.

**Modelo cerrado (sistema interactivo con $N$ terminales).** $E[s]$: servicio de CPU por interacción; $E[t]$: tiempo de pensamiento. Nadie entra ni sale.

| Magnitud | Fórmula |
|---|---|
| CPU libre | $p_0=\left[\displaystyle\sum_{k=0}^{N}\frac{N!}{(N-k)!}\left(\frac{E[s]}{E[t]}\right)^k\right]^{-1}$ |
| Utilización de la CPU | $\rho=1-p_0$ |
| Interacciones por unidad de tiempo | $T=\rho/E[s]$ (no confundir con el $T_i$ de §9) |
| Tiempo de respuesta | $W=\dfrac{N}{T}-E[t]$ |
| Interacciones pendientes en el sistema | $L=T\,W=N-T\,E[t]$ |
| Punto de saturación | $N^*=\dfrac{E[s]+E[t]}{E[s]}$ |

$N^*$ es el máximo de **terminales** sin interferencia mutua: corte de las asíntotas $W=E[s]$ (pocos terminales) y $W=N\,E[s]-E[t]$ ($N\to\infty$). Pasado $N^*$, cada terminal nuevo suma ≈ $E[s]$ al tiempo de respuesta de todos.

**Costos (elegir servidor u opción).** Costo por hora $=$ costo del servidor (sueldo o equipo) $+\ L\times$ costo por hora de cada unidad en el sistema (máquina parada, equipo fuera de servicio). Se usa $L$, no $L_q$: la unidad que está siendo atendida tampoco produce. Control por Little: arribos del período $\times W\times$ costo por hora da lo mismo.

### Ejercicios

#### 8.1 — 04/04/2025 = 17/12/2021 = 20/11/2020 (= ej. 6 de la práctica Medín 2025, que agrega $\pi(90)$) — resuelto

> Sala de emergencias atendida por un doctor. Llegadas Poisson, un paciente cada media hora. Atención exponencial, 20 min en promedio. a) Tiempo promedio que el paciente espera para ser atendido. b) Tiempo promedio en la sala de espera de emergencias. c) N° promedio de pacientes en cola. d) N° promedio de pacientes en sala de espera de emergencias.

1. $\lambda=1/30$ pac/min $=0{,}0333$ pac/min; $E[s]=20$ min ($\mu=0{,}05$ pac/min).
2. $\rho=\lambda E[s]=20/30=\mathbf{0{,}667}$ (el doctor está ocupado el 66,7 % del tiempo).
3. a) $W_q=\dfrac{0{,}667\times20}{1-0{,}667}=\mathbf{40\ min}$.
4. b) $W=W_q+E[s]=40+20=\mathbf{60\ min}$ (tiempo total en emergencias: espera + atención).
5. c) $L_q=\lambda W_q=40/30=\mathbf{1{,}33}$ pacientes.
6. d) $L=\lambda W=60/30=\mathbf{2}$ pacientes.
7. e) (práctica Medín 2025) $\pi_q(90)=W\ln(10\rho)=60\ln(20/3)=60\times1{,}897=\mathbf{113{,}8\ min}$: el 10 % de los pacientes espera más de casi 2 horas para ser atendido.

Interpretación de a)/b) y c)/d) en Dudas. La resolución manuscrita de Medín trabaja en horas ($\lambda=2$ p/h, $\mu=3$ p/h) y llega a los mismos valores, salvo $L$ (ver Dudas).

#### 8.2 — 19/11/2021 = 18/12/2020 (= ej. 3, 7 y 9 de la práctica Medín 2025) — resuelto

> Caja única de 7 a 14 h. Arribos Poisson, 100 personas/día; servicio ≈ 3 min. Definiendo términos y unidades: a) tiempo promedio en cola; b) tiempo promedio en la empresa; c) N° de usuarios promedio en el sistema [en cola]; d) N° de usuarios promedio en la empresa.

1. Horario: 7 h = 420 min → $\lambda=100/420=\mathbf{0{,}2381}$ usuarios/min. $E[s]=3$ min ($\mu=0{,}333$/min).
2. $\rho=0{,}2381\times3=\mathbf{0{,}7143}$.
3. a) $W_q=\dfrac{0{,}7143\times3}{0{,}2857}=\mathbf{7{,}5\ min}$.
4. b) $W=7{,}5+3=\mathbf{10{,}5\ min}$.
5. c) $L_q=0{,}2381\times7{,}5=\mathbf{1{,}786}$ usuarios.
6. d) $L=0{,}2381\times10{,}5=\mathbf{2{,}5}$ usuarios.

7. (Ej. 9 de la práctica 2025) $\pi_q(90)=10{,}5\ln(7{,}14)=\mathbf{20{,}6\ min}$. Conclusión: la espera media (7,5 min) es razonable, pero el 10 % de los usuarios espera más de 20 min; con $\rho=0{,}71$ un aumento de demanda dispara la cola, así que una segunda caja en horas pico es la propuesta natural.

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

#### 8.5 — práctica Medín 2025, ej. 2 — resuelto (M/M/2, pago de haberes)

> Pago de haberes en 2 cajas; los empleados llegan según Poisson, 40 personas/día, de 8 a 12 h. Cobro ≈ 4 min por empleado. a) Tiempo promedio en cola. b) Tiempo promedio en el banco. c) Usuarios promedio en cola. d) Usuarios promedio en el banco. e) $\pi(90)$ del tiempo de espera.

1. 4 h = 240 min → $\lambda=40/240=0{,}1667$ pers/min; $E[s]=4$ min.
2. $u=\lambda E[s]=0{,}667$ Erlang; $c=2$ → $\rho=u/c=\mathbf{0{,}333}$ (cada caja ocupada un tercio del tiempo).
3. $P_0=\left[1+u+\dfrac{u^2}{2(1-\rho)}\right]^{-1}=[1+0{,}667+0{,}333]^{-1}=\mathbf{0{,}5}$.
4. $C(2;\,0{,}667)=\dfrac{u^2}{2(1-\rho)}\,P_0=0{,}333\times0{,}5=\mathbf{0{,}1667}$: sólo 1 de cada 6 empleados tiene que esperar.
5. a) $W_q=\dfrac{0{,}1667\times4}{2\times0{,}667}=\mathbf{0{,}5\ min}$. b) $W=0{,}5+4=\mathbf{4{,}5\ min}$.
6. c) $L_q=0{,}1667\times0{,}5=\mathbf{0{,}083}$ personas. d) $L=0{,}1667\times4{,}5=\mathbf{0{,}75}$ personas.
7. e) $\pi_q(90)=\dfrac{4}{2(0{,}667)}\ln(10\times0{,}1667)=3\ln1{,}667=\mathbf{1{,}53\ min}$.

#### 8.6 — práctica Medín 2025, ej. 4 — resuelto (modelo cerrado, punto de saturación)

> Sistema interactivo con 5 terminales y tiempo de pensamiento medio de 6 s. La CPU ejecuta 15 000 instrucciones/s y cada interacción pide 20 000 en promedio. Tiempo de respuesta, interacciones promedio, utilización de la CPU, interacciones pendientes en el sistema y punto de saturación. ¿Qué pasa si se agregan 2 terminales?

1. $E[s]=20\,000/15\,000=1{,}333$ s; $E[t]=6$ s; $E[s]/E[t]=0{,}2222$.
2. Punto de saturación: $N^*=(1{,}333+6)/1{,}333=\mathbf{5{,}5}$ terminales.
3. $p_0$ con $N=5$. Términos $\frac{5!}{(5-k)!}(0{,}2222)^k$ para $k=0\dots5$: 1; 1,1111; 0,9877; 0,6584; 0,2926; 0,0650. Suma 4,1149 → $p_0=\mathbf{0{,}2430}$.
4. Utilización de la CPU: $\rho=1-p_0=\mathbf{0{,}757}$.
5. Interacciones por segundo: $T=\rho/E[s]=0{,}757/1{,}333=\mathbf{0{,}568}$ int/s.
6. Tiempo de respuesta: $W=N/T-E[t]=5/0{,}568-6=\mathbf{2{,}81\ s}$.
7. Interacciones pendientes: $L=T\,W=0{,}568\times2{,}81=\mathbf{1{,}59}$.
8. Con 7 terminales (más que $N^*$). Términos: 1; 1,5556; 2,0741; 2,3045; 2,0485; 1,3656; 0,6070; 0,1349. Suma 11,090 → $p_0=0{,}0902$; $\rho=0{,}910$; $T=0{,}682$ int/s; $W=7/0{,}682-6=\mathbf{4{,}26\ s}$; $L=2{,}91$.
9. Conclusión: +40 % de terminales da sólo +20 % de interacciones por segundo (0,568 → 0,682) y +52 % de tiempo de respuesta (2,81 → 4,26 s). Con 5 ya se estaba al borde de $N^*=5{,}5$; con 7 la CPU está ocupada el 91 % y se entra en la zona de la asíntota $W\approx N\,E[s]-E[t]$, donde cada terminal nuevo suma ≈1,33 s de respuesta para todos.

#### 8.7 — práctica Medín 2025, ej. 5 — resuelto (costos: obrero x vs obrero y)

> Las máquinas se descomponen según Poisson, 1 por hora; cada máquina ociosa cuesta \$25/h. El obrero x cobra \$20/h y repara $\mu_x=2$ máq/h; el obrero y cobra \$12/h y repara $\mu_y=1{,}2$ máq/h. Jornada de 8 h. Costo de trabajo = mano de obra + tiempo no productivo. Recomendación al gerente.

1. Un reparador = M/M/1 con $\lambda=1$ máq/h. La máquina no produce mientras espera **ni** mientras la reparan → se usa $L$.
2. Obrero x: $E[s]=0{,}5$ h; $\rho=0{,}5$; $W=0{,}5/0{,}5=1$ h; $L=\lambda W=\mathbf{1}$ máquina.
   - Costo por hora $=20+25\times1=\$45$; por jornada $45\times8=\mathbf{\$360}$.
3. Obrero y: $E[s]=0{,}8\overline{3}$ h; $\rho=0{,}8\overline{3}$; $W=0{,}8\overline{3}/0{,}1\overline{6}=5$ h; $L=\mathbf{5}$ máquinas.
   - Costo por hora $=12+25\times5=\$137$; por jornada $\mathbf{\$1096}$.
4. Recomendación: **contratar a x**. Cobra \$8/h más, pero con y hay en promedio 4 máquinas más paradas (\$100/h de pérdida extra). Con $\rho_y=0{,}83$ el taller queda cerca de la saturación.
5. Contraste: la resolución manuscrita de Medín redondea $\rho_y=0{,}83$ y da $W=4{,}88$ h, \$134/h y \$1072 por jornada. El resumen del 2° parcial del alumno da los valores exactos. La recomendación no cambia.

#### 8.8 — práctica Medín 2025, ej. 11 — resuelto (costos: mantenimiento manual vs con máquinas)

> «Computodos» revisa sus equipos una vez al año. Opción manual: \$750 000, servicio exponencial de media 6 h. Opción con máquinas: \$1 000 000, media 3 h. Los equipos llegan según Poisson, 3 por día. Un equipo parado cuesta \$150/h. La empresa trabaja 24 h, 365 días. ¿Qué alternativa conviene?

1. $\lambda=3/24=0{,}125$ equipos/h; año = 8760 h.
2. Manual: $\rho=0{,}125\times6=0{,}75$; $W=6/0{,}25=24$ h; $L=0{,}125\times24=3$ equipos parados en promedio.
   - Parada anual $=3\times150\times8760=\$3\,942\,000$; total $=\mathbf{\$4\,692\,000}$.
3. Con máquinas: $\rho=0{,}375$; $W=3/0{,}625=4{,}8$ h; $L=0{,}6$ equipos.
   - Parada anual $=0{,}6\times150\times8760=\$788\,400$; total $=\mathbf{\$1\,788\,400}$.
4. **Conviene el mantenimiento con máquinas**: ahorra ≈ \$2,9 millones por año. Control por Little: $3\times365=1095$ equipos/año $\times W\times\$150$ da los mismos costos de parada.
5. Supuesto: los \$750 000 y \$1 000 000 son anuales (la hoja no lo aclara). Aunque fuesen un pago único, la conclusión no cambia: la diferencia en paradas (\$3 153 600 por año) supera la diferencia de costo (\$250 000).

#### 8.9 — parcial Medín 2025, com. 305 (resumen del alumno) — resuelto + propuesta

> Caja con 6 horas de atención, 50 personas por día, tiempo de servicio 7 min. a) Tiempo promedio en la caja [en cola]. b) Tiempo promedio en la compañía. c) Usuarios promedio en cola. d) Usuarios promedio en el organismo. (El mismo parcial pedía también los elementos de un sistema de colas abierto y el concepto de punto de saturación.)

1. $\lambda=50/360=0{,}1389$ pers/min; $\rho=0{,}1389\times7=35/36=\mathbf{0{,}9722}$.
2. a) $W_q=\dfrac{(35/36)\times7}{1/36}=\mathbf{245\ min}$. b) $W=245+7=\mathbf{252\ min}$.
3. c) $L_q=0{,}1389\times245=\mathbf{34{,}03}$ personas. d) $L=0{,}1389\times252=\mathbf{35}$ personas.
4. Conclusión: con $\rho=0{,}97$ la espera media pasa las 4 horas; inaceptable. Con **2 cajas** (M/M/2): $u=0{,}972$, $\rho=0{,}486$, $P_0=0{,}346$, $C(2,u)=0{,}318$, $W_q=\mathbf{2{,}17\ min}$, $W=9{,}17$ min, $L_q=0{,}30$, $L=1{,}27$.
5. El alumno usa $\rho=0{,}9723$ y obtiene $W_q=245{,}70$ min y $L_q=34{,}13$: con $\rho$ tan cerca de 1, un redondeo en la cuarta cifra mueve el resultado. Conviene trabajar con la fracción ($35/36$).

#### 8.10 — práctica Medín 2025, ej. 10 («Panis») — enunciado incompleto, resuelto con supuesto

> Los clientes forman una sola cola frente a los empleados. Llegan según Poisson, 60 por hora; el servicio es exponencial de media 12 min. ¿Cuál es el tiempo medio de estancia del cliente hasta que fue atendido? Si el gerente agrega servidores, ¿cuál es el tiempo de espera?

1. $\lambda=1$ cliente/min; $E[s]=12$ min → $u=\lambda E[s]=\mathbf{12}$ Erlang: hacen falta **al menos 13 empleados** para que $\rho<1$. La hoja no dice cuántos hay (ver Dudas).
2. Supuesto ilustrativo, M/M/c con una sola cola ($W_q$ y $W$ en minutos):

| $c$ | $\rho$ | $C(c;12)$ | $W_q$ | $W$ |
|---|---|---|---|---|
| 13 | 0,923 | 0,704 | 8,45 | 20,45 |
| 14 | 0,857 | 0,482 | 2,89 | 14,89 |
| 15 | 0,800 | 0,319 | 1,28 | 13,28 |
| 16 | 0,750 | 0,205 | 0,61 | 12,61 |

3. Lectura: pasar de 13 a 14 empleados baja la espera en cola a un tercio; a partir de ahí la mejora es marginal. «Estancia hasta que fue atendido» se puede leer como $W$ (hasta terminar la atención) o $W_q$ (hasta empezarla): la tabla da los dos.

#### Resto (enunciado + resultados)

| Origen | Datos | Resultado |
|---|---|---|
| F4 | Banco de 10 a 16 h, 30 personas/día, atención exponencial de 10 min. $\rho$, $W_q$, $W$, $L_q$, $L$. | $\lambda=30/360=0{,}0833$/min; $\rho=0{,}833$; $W_q=50$ min; $W=60$ min; $L_q=4{,}17$; $L=5$ (coincide con el alumno). |
| F6 | Servidor de impresión de 8 a 14 h, lunes a viernes; 70 trabajos/semana; impresión exponencial de 5 min/trabajo. Resultados en minutos. | Semana = 5 × 360 = 1800 min; $\lambda=0{,}0389$/min; $\rho=0{,}194$; $W_q=1{,}21$ min; $W=6{,}21$ min; $L_q=0{,}047$; $L=0{,}241$. |
| F1 = F13 = 17/02/2006 | $\lambda=0{,}015$ mensajes/s; «frecuencia [tiempo] de servicio» = 18 s/mensaje; longitud media 72 caracteres/mensaje. a) Factor de utilización; b) velocidad del servidor; c) tiempo de espera. | Con $E[s]=18$ s (así lo dice 17/02/2006): a) $\rho=0{,}015\times18=0{,}27$; b) $72/18=4$ caracteres/s; c) $W_q=0{,}27\times18/0{,}73=6{,}66$ s ($W=24{,}66$ s). La resolución del alumno lee 18 s como retardo total; ver Dudas. |
| 29/11/2002 (= ej. 2 de la práctica de capacidad = ej. 8 de la práctica de colas, Medín 2025) | Centro de cómputos: 120 mensajes/h; longitud exponencial de media 144 caracteres; servidor del enlace a 8 caracteres/s. a) Tiempo medio de espera; b) utilización del enlace. | $\lambda=1/30$ msj/s; $E[s]=144/8=18$ s; b) $\rho=0{,}6$; a) $W_q=27$ s ($W=45$ s). |
| 07/05/2004 | Aeropuerto: 10 pasajeros en cola, tiempo total en el sistema 30 min, factor de uso 0,9. Frecuencia de arribo, tiempo en cola, tiempo de servicio. | Igual que 8.4: $30\lambda=10+0{,}9\Rightarrow\lambda=0{,}363$/min; $W_q=27{,}52$ min; $E[s]=2{,}48$ min. (M/M/1 daría $L_q=8{,}1$: datos no M/M/1.) |
| práctica Medín 2025, ej. 1 (minibanco) | Caja única de 10 a 15 h; 60 personas/día; servicio 5 min. $W_q$, $W$, $L_q$, $L$, $\pi(90)$. | $\lambda=60/300=0{,}2$/min; $\rho=0{,}2\times5=\mathbf{1}$: **sistema saturado**, la cola crece sin límite y las fórmulas no aplican. Propuesta: 2 cajas → $u=1$, $\rho=0{,}5$, $P_0=1/3$, $C=1/3$, $W_q=1{,}67$ min, $W=6{,}67$ min, $L_q=0{,}33$, $L=1{,}33$, $\pi_q(90)=5\ln(3{,}33)=6{,}02$ min. |
| «Ejercicio de Teoría de Colas» (Medín 2025), ej. 1 | Router M/M/1: llegan 100 paq/s, procesa 125 paq/s. $\rho$, $L$, $L_q$, $W$, $W_q$. | $\rho=100/125=0{,}8$; $L=\rho/(1-\rho)=4$; $L_q=3{,}2$; $W=L/\lambda=40$ ms; $W_q=32$ ms ($E[s]=8$ ms). Coincide con la fuente, que escribe mal $\rho=\mu/\lambda$ (ver Dudas). |
| ídem, ej. 2 | Gateway de LAN: $\lambda=10$ paq/s, $\mu=15$ paq/s. | $\rho=0{,}667$; $L_q=1{,}33$; $L=2$; $W_q=133{,}3$ ms; $W=200$ ms (coincide). |
| 2° parcial Medín 2025, propuestos (resumen del alumno) | Sala de emergencias (= 8.1) y obrero x/y (= 8.7). | Mismos números. El resumen asigna a) $=W$, b) $=W_q$, c) $=L$, d) $=L_q$, al revés que este banco y que Medín (ver Dudas). |

### Trampas frecuentes

- Unidades: $\lambda$ por minuto y $E[s]$ en minutos (o ambos en horas). «100 personas/día» se divide por los minutos **de atención**, no por 1440.
- $W$ incluye el servicio; $W_q$ no.
- Little vale siempre; las fórmulas de $W_q$ con $\rho$ sólo para M/M/1.
- $\rho\ge1$ → la cola crece sin límite: hay que decirlo, no seguir calculando (minibanco: $\rho=1$ exacto).
- $\rho=\lambda/\mu=\lambda E[s]$, nunca $\mu/\lambda$ (error escrito en el «Ejercicio de Teoría de Colas» 2025).
- Con $\rho$ cerca de 1 no redondees $\rho$: 0,83 en vez de $5/6$ cambia $W$ de 5 a 4,88 h (8.7); 0,9723 en vez de $35/36$ cambia $W_q$ de 245 a 245,7 min (8.9).
- En costos se multiplica por $L$ (unidades en el sistema), no por $L_q$.
- Varias cajas con **una sola cola** (M/M/c) son mejores que colas separadas; el M/M/c se calcula con Erlang C, no dividiendo $\lambda$ por $c$.
- «Punto de saturación» en teoría es $N^*$ del modelo cerrado (terminales), no «cuando $\rho$ llega a 1» ni «número de servidores».

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

Regla de la raíz cuadrada (Kleinrock): con costo proporcional a la capacidad total $C$ fija, el retardo medio $\frac1\gamma\sum\lambda_iT_i$ es mínimo si cada enlace recibe lo imprescindible ($\lambda_i/\eta_i$) más una parte del remanente $C(1-\rho)$ **proporcional a la raíz cuadrada** de su tráfico. $T_{\min}$ es inversamente proporcional a $C$: más capacidad (más costo), menos retardo.

Pasos:

1. $\lambda_i$ de cada enlace = terminales del nodo × frecuencia por terminal (en mensajes/s).
   - **Red en árbol** (Medín 2025): el $\lambda$ de un enlace suma los terminales del propio nodo **más** los $\lambda$ de todos los enlaces que llegan a ese nodo desde las hojas (hipótesis de independencia de Kleinrock). El enlace al nodo central lleva el tráfico de toda la red.
2. Tabla con $\lambda_i$, $\lambda_i/\eta_i$ [bps], $\sqrt{\lambda_i/\eta_i}$, sumas.
3. $\rho$, $C(1-\rho)$, $C_i^{opt}$ (control: $\sum C_i^{opt}=C$), $T_i$ y $T_{\min}$.
4. Si en vez de repartir $C$ te dan la capacidad de cada enlace («¿la capacidad es acorde?»): $\rho_i=\lambda_i/(\eta_iC_i)$ y $T_i=\dfrac{1}{\eta_iC_i-\lambda_i}=\dfrac{1/(\eta_iC_i)}{1-\rho_i}$ por enlace, y concluir (holgado, ajustado o saturado).

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

#### 9.3 — F10 = F11 (= ej. 3 de la práctica de capacidad, Medín 2025) — resuelto

> Nodo concentrador de 1200 bps al que llegan mensajes de 120 bits. a) Máxima frecuencia de arribos para que el retardo no exceda 2 s. b) Si $\lambda\to\eta_iC_i$, ¿qué pasa?

1. $\eta C=1200/120=10$ mensajes/s.
2. a) $T=\dfrac1{10-\lambda}\le2\Rightarrow10-\lambda\ge0{,}5\Rightarrow\lambda\le\mathbf{9{,}5}$ mensajes/s ($\rho=0{,}95$).
3. b) $\rho\to1$: el denominador tiende a 0 y el retardo crece sin límite (el buffer se llena; el enlace no da abasto).

#### 9.4 — práctica Medín 2025, ej. 1 — resuelto (4 concentradores, $C^{opt}$ y $T_{\min}$)

> 4 concentradores en estrella hacia una CPU central. Cada terminal transmite 10 mensajes/s de 6 bits en promedio. Santa Fe: 20 terminales; Venado Tuerto: 10; Villa Constitución: 5; Cañada de Gómez: 5. a) Tiempo mínimo para una red de capacidad total 5000 bps. b) $C^{opt}$.

1. $\lambda_i$ = terminales × 10 msg/s; $1/\eta=6$ bits → tráfico ofrecido $\lambda_i/\eta=6\lambda_i$ bps.

| Nodo | Term. | $\lambda_i$ [msg/s] | $\lambda_i/\eta$ [bps] | $\sqrt{\lambda_i/\eta}$ | $C_i^{opt}$ [bps] | $\rho_i$ | $T_i$ [ms] |
|---|---|---|---|---|---|---|---|
| Santa Fe | 20 | 200 | 1200 | 34,641 | 2160,43 | 0,555 | 6,25 |
| Venado Tuerto | 10 | 100 | 600 | 24,495 | 1279,13 | 0,469 | 8,83 |
| Villa Constitución | 5 | 50 | 300 | 17,321 | 780,22 | 0,385 | 12,49 |
| Cañada de Gómez | 5 | 50 | 300 | 17,321 | 780,22 | 0,385 | 12,49 |
| Σ | 40 | 400 | 2400 | 93,777 | 5000,00 | | |

2. $\rho=2400/5000=0{,}48$; remanente $C(1-\rho)=2600$ bps.
3. b) Santa Fe: $C_1=1200+2600\times34{,}641/93{,}777=1200+960{,}43=\mathbf{2160{,}43}$ bps. Igual los demás; suman 5000 ✓.
4. $T_1=\dfrac{1}{2160{,}43/6-200}=\dfrac{1}{160{,}07}=6{,}25$ ms.
5. a) $T_{\min}=\dfrac{93{,}777^2}{400\times2600}=\dfrac{8794{,}1}{1\,040\,000}=\mathbf{8{,}46\ ms}$ (igual a $\sum\lambda_iT_i/\gamma$ ✓).
6. Para ver qué gana la regla: repartiendo parejo (1250 bps por enlace), Santa Fe queda con $\eta C=208{,}3$ msg/s para $\lambda=200$ ($\rho=0{,}96$, $T=120$ ms) y el promedio de la red sube a 63,9 ms, unas 7,6 veces más.

#### 9.5 — red en árbol con datacenter (cuaderno del alumno y 2° parcial Medín 2025) — resuelto

> Una empresa quiere evaluar la red sobre el nodo central (nodo 1, donde está el datacenter): utilización de los enlaces y recomendación sobre tiempos y capacidades. Árbol: 4→3, 5→3, 3→2, 2→1, 6→1, 8→7, 7→1. Terminales por nodo: 1: 10; 2: 2; 3: 2; 4: 6; 5: 6; 6: 6; 7: 6; 8: 2. Capacidad 4500 bps, 0,03 mensajes/s por terminal, mensajes de 6 bits.

1. Acumulo desde las hojas ($f=0{,}03$ msg/s por terminal):
   - $\lambda_4=\lambda_5=\lambda_6=6f=0{,}18$; $\lambda_8=2f=0{,}06$
   - $\lambda_3=2f+\lambda_4+\lambda_5=0{,}42$; $\lambda_2=2f+\lambda_3=0{,}48$; $\lambda_7=6f+\lambda_8=0{,}24$
   - $\lambda_1=10f+\lambda_2+\lambda_6+\lambda_7=\mathbf{1{,}2}$ msg/s (= 40 terminales × 0,03)
2. $\eta C=4500/6=750$ msg/s → $\rho_1=1{,}2/750=\mathbf{0{,}0016}$ (0,16 %).
3. $T_1=\dfrac{1}{750-1{,}2}=\mathbf{1{,}335\ ms}$: prácticamente sólo el tiempo de transmitir ($1/750=1{,}333$ ms).
4. Si cada enlace tiene 4500 bps, todos quedan con $\rho_i<0{,}1\,\%$ y $T_i\approx1{,}334$ ms.
5. Recomendación: la red está muy sobredimensionada; se puede bajar capacidad (repartir una $C$ menor con $C^{opt}$, o canales comerciales más chicos) sin cambiar los tiempos de forma apreciable.
6. Con $f=1/30$ exacto (1 mensaje cada 30 s): $\lambda_1=40/30=1{,}333$ msg/s, $\rho_1=0{,}00178$, $T_1=1{,}336$ ms. Misma conclusión.

Errores de las fuentes (detalle en Dudas): el cuaderno mezcla $f=1/30$ y 0,03 ($\lambda_1=1{,}29$) y da $T_1=0{,}000035$ s; el resumen escribe «0,0016 %» y una fórmula de $T_1$ mal armada.

#### 9.6 — sucursal en Capitán Bermúdez (cuaderno del alumno y 2° parcial Medín 2025) — resuelto, dos versiones de datos

> Red: Pto. San Martín (50 terminales) → Cap. Bermúdez (40) → Rosario (50) ← Funes o Roldán (10); Rosario → ISP. Enlaces internos de 3000 bps; enlace al ISP de 5000 bps. Una empresa evalúa sumar la sucursal de Capitán Bermúdez sobre el enlace Pto. San Martín–Rosario: ¿la capacidad es acorde?

Datos según la fuente: el cuaderno dice 1 mensaje cada 30 s por terminal, de 8 bits (y Funes); el resumen del 2° parcial dice 1 mensaje cada «1230 s», de 1500 bits (y Roldán).

1. Terminales que pesan sobre cada enlace: PSM→CB 50; CB→Rosario $50+40=90$; Funes→Rosario 10; Rosario→ISP $50+40+50+10=150$.
2. Versión del cuaderno ($f=1/30$, 8 bits): $\eta C=3000/8=375$ msg/s en los internos y $5000/8=625$ msg/s al ISP.

| Enlace | $\lambda$ [msg/s] | $\rho$ | $T$ [ms] |
|---|---|---|---|
| PSM → CB | 1,667 | 0,0044 | 2,68 |
| CB → Rosario | 3,000 | 0,0080 | 2,69 |
| Funes → Rosario | 0,333 | 0,0009 | 2,67 |
| Rosario → ISP | 5,000 | 0,0080 | 1,61 |

Sobra capacidad: el enlace CB→Rosario recién se saturaría con $30\times375=11\,250$ terminales aguas arriba. Se puede incorporar Bermúdez.
3. Versión del resumen ($f=1/1230$, 1500 bits): $\lambda_{ISP}=150/1230=0{,}122$ msg/s; $\eta C_{ISP}=5000/1500=3{,}33$ msg/s → $\rho_{ISP}=\mathbf{0{,}0366}$ (el resumen da 0,03, truncado). En CB→Rosario: $\rho=0{,}0366$, $T=1/(2-0{,}073)=0{,}519$ s. También sobra capacidad.
4. Ojo: con 1500 bits y 1 mensaje cada 30 s, $\rho_{ISP}=5/3{,}33=1{,}5$ y $\rho_{CB\to Ros}=1{,}5$: **saturado**, la conclusión se invierte. Por eso importa el dato «1230» (ver Dudas).
5. Error del cuaderno: escribe «Frec prom = 0,03 seg»; es 0,0333 **mensajes/s** (la inversa de 30 s).

### Trampas frecuentes

- $1/\eta$ es la **longitud** (bits/mensaje); $\eta C$ son mensajes/s: capacidad **dividida** por la longitud, no multiplicada (error del cuaderno en 9.5).
- Verificar $\sum C_i^{opt}=C$.
- $\lambda$ por terminal × cantidad de terminales, y en mensajes **por segundo**.
- En árbol, cada enlace suma sus terminales **y** todo lo que le llega de los nodos anteriores.
- $\rho=0{,}0016$ es 0,16 %, no «0,0016 %».

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

## 11. Atenuación, ganancia y dB (teoría de Baró, 1er parcial 2025)

### Receta

Fuente: «Resumen Comunicación de Datos - Medin 1er Parcial» (sección Baró) y «Velocidades de transmisión de datos…» (Baró).

| Magnitud | Fórmula |
|---|---|
| Ganancia | $G=\dfrac{\text{salida}}{\text{entrada}}$, en «veces» (sin unidad): $G_V=V_0/V_f$, $G_P=P_0/P_f$, $G_I=I_0/I_f$ |
| Atenuación | $A=\dfrac{\text{entrada}}{\text{salida}}=\dfrac1G$ |
| En decibeles | $G_{dB}=10\log_{10}G$; $A_{dB}=10\log_{10}A$ |
| Etapas en serie | en veces se **multiplican**; en dB se **suman** |
| Relación señal/ruido | $S/N=P_{señal}/P_{ruido}$; en dB, $10\log_{10}(S/N)$ |

- Rango dinámico: diferencia entre el nivel máximo que puede emitir un dispositivo y el ruido de fondo sin señal. En una cadena manda el peor dispositivo; en equipos de calidad, 80–95 dB.
- Ancho de banda según Baró: frecuencia en la que la salida cae 3 dB (mitad de la potencia).
- *(Conocimiento general)* Las fórmulas con $10\log_{10}$ son para cocientes de **potencia**; para tensión o corriente se usa $20\log_{10}$.

### Ejercicio

#### 11.1 — ejemplo del resumen (Baró 2025)

> Dos componentes en serie, cada uno con una atenuación de 10 veces. Atenuación del sistema.

1. En veces: $A=10\times10=\mathbf{100}$ veces.
2. En dB: $10\log_{10}100=\mathbf{20\ dB}=10\ dB+10\ dB$.

Las fuentes de 2025 no traen ejercicios numéricos de este tema y ningún final lo tomó; no se inventaron.

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

**Cursada 2025 (com. 303): errores y supuestos**

31. **Multinivel, práctica Baró ej. 9 (= ej. 14 del apunte)**: redondea $\lg7\approx2{,}8$ y da 147 niveles para duplicar $R$. Con $\lg7=2{,}807$ son 149 ($\mu'=148{,}5$). Con 147, $R=1097{,}2$ bps, que no llega al doble exacto (1099,1 bps).
32. **Multinivel, práctica Baró ej. 2**: repite el error del apunte ($I=2{,}81$ bits en vez de 16,84; punto 8).
33. **Multinivel, práctica Baró ej. 11**: $n=2487{,}08$; la práctica toma 2487, que no alcanza los 5 Mbps (hacen falta 2488). Escribe «500 seg × 5 bps» por «500 µs × 5 Mbps» (los 2500 bits están bien). El inciso d) queda planteado sin resolver; ver 1.8.
34. **Baró, $B=s/2$ contra $B_w=1/\tau$**: el apunte teórico de Baró 2025 («Velocidades de transmisión…») define $B=s/2$ (Nyquist), pero en sus parciales de TDM-PCM el alumno usa $B_w=1/\tau$ y no hay corrección visible. Refuerza el punto 1: en el examen, aclarar cuál se usa.
35. **TDM, parciales de Baró (resumen del alumno)**: en el «Otro parcial» pone $T_s=1/10\ \text{kHz}=0{,}1\ \mu s$ (es 0,1 ms) y llega a $r=3{,}2$ Gbps; lo correcto es 3,2 Mbps. En el «Primer ejercicio» el enunciado no da bits por muestra y el alumno supone 8; redondea $T_m=3{,}9\ \mu s$ y da 2,05 Mbps (exacto 2,048). En el «Parcial random» escribe «mHz» por MHz.
36. **Codificación, práctica Medín 2025**: el .md convertido perdió todas las tablas (longitudes del ej. 1, código del ej. 2, probabilidades de los ej. 3 y 5); se leyeron del PDF renderizado, sin ambigüedades. El ej. 1 no dice el alfabeto: supuse binario. El ej. 3 dice «$L=H_N(s)$»: lo tomé como la entropía en la base del código (binaria).
37. **Sala de emergencias, a)–d)**: la resolución manuscrita de Medín toma a) $=W_q$ (40 min) y b) $=W$ (60 min), como este banco (punto 10). El resumen del 2° parcial del alumno los invierte: a) $=W$, b) $=W_q$, c) $=L$, d) $=L_q$. Seguí a Medín.
38. **Sala de emergencias, resolución manuscrita de Medín**: escribe «$L=2\cdot1\Rightarrow L=1$ p»; es $L=2$ pacientes (el producto está bien planteado). También anota «$\rho=\mu/c$» donde va $\rho=u/c$, y escribe $\pi(90)=1{,}8$ h truncado (es 1,897 h); el valor en minutos, 113,8, está bien.
39. **Obrero x vs y, resolución de Medín**: redondea $\rho_y=0{,}83$ → $W=4{,}88$ h, \$134/h y \$1072 por jornada. Exacto: 5 h, \$137 y \$1096. La recomendación (x) no cambia.
40. **«Ejercicio de Teoría de Colas» (router y gateway)**: escribe $\rho=\mu/\lambda$ y «125/100 = 0,8» (125/100 es 1,25). Lo correcto es $\rho=\lambda/\mu=100/125=0{,}8$. Los demás resultados están bien. Las fórmulas de $L$, $L_q$, $W$ y $W_q$ se perdieron en la conversión (eran imágenes).
41. **«Panis» (práctica Medín ej. 10)**: no da la cantidad de empleados. Con 60 clientes/h y 12 min de servicio, $u=12$ Erlang: con menos de 13 servidores el sistema se satura. La tabla de 8.10 es un supuesto ilustrativo ($c=13\dots16$).
42. **«Computodos» (práctica Medín ej. 11)**: no aclara si \$750 000 y \$1 000 000 son anuales; la conclusión no depende de eso (8.8).
43. **Parcial com. 305**: el alumno redondea $\rho=0{,}9723$ (exacto $35/36$) → $W_q=245{,}70$ y $L_q=34{,}13$ en vez de 245 min y 34,03. El mismo resumen define «punto de saturación» como el momento en que el tráfico supera la capacidad del enlace ($\rho\to1$) y toma «saturado» como $0{,}8<\rho<1$. La teoría de la cátedra lo define como $N^*$ del modelo cerrado (máximo de terminales sin interferencia mutua); el umbral 0,8 es un criterio práctico del alumno.
44. **Red en árbol (9.5)**: el cuaderno escribe $\lambda_4=0{,}03\times6=0{,}2$ (eso es $6/30$; con 0,03 da 0,18) y mezcla los dos valores hasta $\lambda_1=1{,}29$ (40/30 = 1,333 o 40 × 0,03 = 1,2). Su $T_1=0{,}000035$ s sale de usar $\eta C=6\times4500$ en vez de $4500/6$ ($1/27\,000=3{,}7\times10^{-5}$ s); lo correcto es 1,34 ms, y no «menor a 1 µs» como concluye. El resumen del 2° parcial escribe $\rho_1=0{,}0016\,\%$ (es 0,16 %) y $T_1=\lambda_1/(\eta C-(1-\rho_1))$; al evaluar pone 1 en el numerador y el número (0,0013 s) coincide con el correcto $1/(\eta C-\lambda_1)$ sólo porque $\lambda_1$ y $1-\rho_1$ son ≈1 frente a 750.
45. **Capitán Bermúdez (9.6)**: el cuaderno dice 1 mensaje cada 30 s y 8 bits; el resumen, 1 cada «1230 s» y 1500 bits, y nombra Roldán en vez de Funes. «1230» puede ser una mala transcripción de «1/30»: con 1 cada 30 s y 1500 bits, el enlace al ISP y el CB→Rosario quedarían con $\rho=1{,}5$ (saturados) y la conclusión se invierte. El resumen da $\rho_{ISP}=0{,}03$ (es 0,0366).
46. **Informe N3 de Medín (colas y capacidad)**: todas las fórmulas y las tablas del ejemplo de las 7 ciudades son imágenes no convertidas; no aporta números nuevos. Sus conclusiones (un M/M/1 con capacidad $m\mu$ da menor $W$ que un M/M/m, aunque el M/M/m espera algo menos en cola) coinciden con la wiki.
47. **Fuentes vacías**: `ejercicios teoria de colas.md` y `drive-propio/ejercicios.md` tienen 0 bytes; su contenido se tomó de los escaneos (`ejercicios-colas-medin-1..3`, `ejercicios-propio-1..2`).
