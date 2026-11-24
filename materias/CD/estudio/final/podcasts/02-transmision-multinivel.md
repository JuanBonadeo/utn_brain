# Podcast CD 2 de 8 — Transmisión multinivel: M(T), información y velocidades

Fuente para un episodio de podcast de estudio. Materia: Comunicación de Datos (UTN Facultad
Regional Rosario, Ingeniería en Sistemas, 3.er año). Sirve para rendir el final: tres problemas
de práctica y tres preguntas de teoría para desarrollar. Las respuestas de las preguntas son
respuestas modelo armadas por nosotros a partir de los apuntes de la cátedra, no la corrección
oficial.

## Indicaciones para el episodio

La idea de mandar más de dos niveles por pulso, la receta del problema que sale en casi todos los finales (pulsos de arranque y stop, M(T), I, R) y la diferencia entre R, r y s. Explicá por qué subir los niveles aumenta la velocidad sin tocar los baudios.

## Contenido principal

### 2.6 Las velocidades: R, r y s

| Magnitud | Definición de la cátedra | Fórmula | Unidad |
|---|---|---|---|
| **Tasa de información** $R$ | información **promedio** que produce la fuente **por unidad de tiempo** | $R = r \cdot H$ | bps |
| **Tasa de dígitos** $r$ | **dígitos transmitidos por segundo**, informen o no | $r = N/T$ | dígitos/s |
| **Velocidad de señalización** $s$ | inversa de la duración del pulso **más corto** | $s = 1/\tau_{min}$ | baudios |

Ejemplo: pulsos de 1 ms con 4 niveles equiprobables dan $s = 1000$ baudios, $r = 1000$ dígitos/s y, como cada dígito lleva $\log_2 4 = 2$ bit, $R = 2000$ bps. Con pulsos **binarios** equiprobables, $R = s$: la capacidad coincide con la velocidad de señalización, y el ancho de banda mínimo es $B = s/2$.

> **Ojo:** $R = r \cdot H$, o sea $r = R/H$. Un resumen de alumnos escribe "$r = H(A)/R$": está mal. En el *multiple choice*, la tasa de información lleva la palabra "**promedio**".

### 3. Transmisión multinivel

*Fuentes: Principios Básicos (práctica), Transmisión Multinivel resuelta y "Fórmulas y pasos". Sale en 8 de cada 9 finales.*

#### 3.1 La idea y la receta

Tenés 6 pulsos y cada uno vale +2 V o −2 V: hay $2^6 = 64$ mensajes y cada grupo lleva $\log_2 64 = 6$ bit. Si cada pulso puede tomar 7 niveles (de −3 V a +3 V), con los **mismos** 6 pulsos en el **mismo** tiempo hay $7^6 = 117\,649$ mensajes y $6 \log_2 7 = 16{,}84$ bit. **Más niveles por pulso es más información en el mismo tiempo.** Es la idea que después acelera los módems (§6.3).

| Magnitud | Fórmula | Unidad |
|---|---|---|
| Mensajes distintos | $M(T) = \mu^n$ | mensajes |
| Información | $I = \log_2 M(T) = n \log_2 \mu$ | bit |
| Tasa de información | $R = I/T$ | bps |
| Tasa de dígitos | $r = N/T$ | dígitos/s |
| Velocidad de señalización | $s = 1/\tau_{min}$ | baudios |

$\mu$ son los niveles por pulso, $n$ los pulsos **de información**, $N$ los pulsos **totales** y $T$ la duración **total** del grupo. Con mensajes equiprobables, $I = \log_2 M(T)$ sin calcular entropías.

**Pasos:**

1. **Separá los pulsos.** Los fijos (arranque, parada, sincronismo) tienen un solo nivel posible: **no aportan información** ($\log_2 1 = 0$), pero **sí suman tiempo** y dígitos. El receptor tiene que esperar el grupo entero para tener un mensaje, pero el arranque y el stop no le dicen nada nuevo.
2. **Contá los niveles.** "Entre +4 y −4 incluido el 0" son **9**.
3. **Sumá el tiempo de todos los pulsos.** Cuidado si mezclan μs y ms.
4. **Calculá** $I$, $R$, $r$ y $s$. Si hay bloques con distinta cantidad de niveles, las informaciones se suman: $I = n_1 \log_2 \mu_1 + n_2 \log_2 \mu_2$.
5. **Graficá**: pulsos uno al lado del otro, arranque y parada en su valor fijo, los de información con alturas variables. Marcá $\tau$ y $T$.

#### 3.2 Ejercicio resuelto: final 2025

**Enunciado.** Una transmisión multinivel usa grupos de 27 pulsos de 128 niveles cada uno, con un pulso fijo de arranque de +4 V y uno fijo de stop de −4 V. Cada pulso dura 10 μs. Calcular a) $M(T)$ e $I_x$, b) $R$ y c) graficar.

**Datos.** $n = 27$, $\mu = 128 = 2^7$, $\tau = 10\ \mu\text{s}$, $N = 29$.

1. **Tiempo del grupo:** $T = 29 \cdot 10\ \mu\text{s} = 290\ \mu\text{s}$.
2. **a)** $M(T) = 128^{27} = 2^{189} \approx$ **7,85 × 10⁵⁶ mensajes**.
3. **a)** $I_x = 27 \cdot \log_2 128 = 27 \cdot 7 =$ **189 bit**.
4. **b)** $R = \dfrac{189\ \text{bit}}{290\ \mu\text{s}} =$ **651,7 kbps**.
5. **Extra**: $r = 29/290\ \mu\text{s} = 100\,000$ dígitos/s; $s = 1/10\ \mu\text{s} = 100$ kbaudios.
6. **c) Gráfica:**

**Criterio a declarar.** Se tomó que los 27 pulsos son de datos y se suman los 2 de control, como en el ejercicio 11 del apunte resuelto. Si los 27 incluyeran arranque y stop: $n = 25$, $T = 270\ \mu\text{s}$, $I = 175$ bit y $R = 648{,}1$ kbps.

**Variante: duplicar $R$ sin tocar los tiempos.** Lo único libre es $\mu$:

$$2 \cdot 189 = 27 \log_2 \mu' \;\Rightarrow\; \log_2 \mu' = 14 \;\Rightarrow\; \mu' = 16\,384 \text{ niveles}$$

Si no da entero, se redondea **para arriba**. $r$ y $s$ no cambian: son los mismos pulsos con las mismas duraciones.

#### 3.3 Otras variantes

| Final | Qué cambia | Resultado |
|---|---|---|
| 10/09/2021 | 1 arranque, 10 datos de 128 niveles, 1 stop; todos de 5 ms salvo el stop, de 7 ms | $T = 62$ ms, $I = 70$ bit, $R = 1129$ bps. Con datos binarios: $R = 161{,}3$ bps |
| 15/02/2017 | el arranque dura 0,5 μs y es el más corto | $s = 2$ Mbaudios, aunque ese pulso no informe |
| 23/10/2020 | 13 pulsos de 58 niveles, $T = 150\ \mu\text{s}$ | $I = 76{,}15$ bit, $R = 507{,}7$ kbps. El apunte redondea a 77 bit: la información no se redondea |
| 18/12/2020 | no dan $\tau$ | dejá $R$ en función de $\tau$ y aclaralo |

> **Ojo:** el ejercicio 2 del apunte resuelto escribe $I = 6 \log_2 7 = 2{,}81$ bit, pero 2,81 es $\log_2 7$. Lo correcto es 16,84 bit.

## Ejercicios de finales sobre este tema (contar el procedimiento, no dictar números)

### 1. Transmisión multinivel — $M(T)$, $I$, $R$, $r$, $s$

#### Receta

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

#### Ejercicios

##### 1.1 — 23/10/2020 (= ej. 11 del apunte resuelto) — resuelto

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

##### 1.2 — 04/04/2025 (plan actual) — resuelto

> Una transmisión multinivel considera grupos de 27 pulsos de 128 niveles c/u. Tiene 1 pulso fijo de arranque de +4 V y 1 pulso fijo de stop de −4 V. Cada pulso dura 10 µs. Calcular: a) $M(T)$ e $I_x$; b) $R$; c) gráfica.

1. $n=27$, $\mu=128=2^7$, $N=29$.
2. $T=29\times10\ \mu s=290\ \mu s$.
3. $M(T)=128^{27}=2^{189}\approx7{,}85\times10^{56}$ mensajes.
4. $I=27\lg128=27\times7=189$ bits (exacto, sin redondeo).
5. $R=189\ \text{bits}/290\ \mu s=651{,}7$ kbps.
6. Gráfica igual a 1.1 con +4 V / −4 V y 27 pulsos.

##### 1.3 — 15/02/2017 — resuelto (R, r, s y duplicar)

> Transmisión asincrónica: 2 pulsos de arranque de 0,5 µs c/u (valor «1»), 5 pulsos cuaternarios (0,1,2,3) de 1 µs c/u, 3 pulsos binarios de 1 µs c/u y 1 pulso de parada «1» de 1 µs. a) Gráfica. b) $R$. c) $r$. d) $s$. e) Parámetro a modificar para duplicar $R$ sin modificar arranque, parada, binarios ni tiempos. f) ¿Cambian $r$ y $s$?

1. $T=2(0{,}5)+5(1)+3(1)+1=10\ \mu s$; $N=2+5+3+1=11$ pulsos.
2. $I=5\lg4+3\lg2=10+3=13$ bits.
3. b) $R=13/10\ \mu s=1{,}3$ Mbps.
4. c) $r=11/10\ \mu s=1{,}1\times10^6$ dígitos/s.
5. d) $\tau_{\min}=0{,}5\ \mu s\Rightarrow s=2\times10^6$ baudios.
6. e) Sólo se pueden cambiar los niveles de los cuaternarios: $2R\cdot T=26=5\lg\mu+3\Rightarrow\lg\mu=4{,}6\Rightarrow\mu=24{,}25\Rightarrow$ **25 niveles**.
7. f) $r$ y $s$ **no cambian**: misma cantidad de pulsos y mismas duraciones.
8. a) Gráfica: dos pulsos angostos en «1», cinco pulsos de 1 µs en alguno de 4 niveles, tres de 1 µs en 0/1, parada en «1».

##### 1.4 — 09/03/2012 — resuelto (R, r, s y duplicar con dos alternativas)

> Bloques de: un dígito de arranque «1» de 0,5 µs, dos dígitos de 8 niveles de 1 µs c/u, cinco dígitos cuaternarios de 2 µs c/u, dos dígitos binarios de 1 µs c/u y un dígito de parada «0» de 3,5 µs. a) Tasa de dígitos, tasa de información y velocidad de señalización. b) Cómo aumentar la velocidad al doble sin tocar comienzo, fin, ni los dígitos de 8 niveles ni los binarios.

1. $T=0{,}5+2(1)+5(2)+2(1)+3{,}5=18\ \mu s$; $N=11$.
2. $I=2\lg8+5\lg4+2\lg2=6+10+2=18$ bits.
3. $r=11/18\ \mu s=611{,}1\times10^3$ dígitos/s; $R=18/18\ \mu s=1$ Mbps; $s=1/0{,}5\ \mu s=2$ Mbaudios.
4. b) Sólo se pueden tocar los cinco cuaternarios. Dos caminos:
   - **Más niveles, mismos tiempos**: $36=8+5\lg\mu\Rightarrow\lg\mu=5{,}6\Rightarrow\mu=48{,}5\Rightarrow$ **49 niveles**.
   - **Mismos niveles, pulsos más cortos** (el enunciado no prohíbe tocar la duración de los cuaternarios): $T'=18/2\ \text{Mbps}=9\ \mu s$; lo fijo suma $0{,}5+2+2+3{,}5=8\ \mu s$, quedan 1 µs para 5 pulsos → **0,2 µs cada cuaternario**. Ojo: entonces $s$ sube a $1/0{,}2\ \mu s=5$ Mbaudios.

##### 1.5 — 28/08/2020 — resuelto

> 2 pulsos de arranque (+5 V y −5 V), 9 pulsos de datos de 128 niveles c/u, 1 pulso de stop (+2 V). Todos duran 2 ms, excepto el stop que dura 4 ms. a) $R$. b) Si los 9 de datos pasan a binarios, nueva $R$ sin cambiar duraciones.

1. $T=2(2)+9(2)+4=26$ ms.
2. a) $I=9\lg128=63$ bits; $R=63/26\ \text{ms}=2423$ bps.
3. b) $I=9$ bits; $R=9/26\ \text{ms}=346{,}2$ bps.

##### Resto de los multinivel (enunciado + resultados)

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

#### Trampas frecuentes

- **$T$ incluye arranque, parada y todo pulso de control**; $I$ no. Error típico: dividir $I$ por el tiempo de los pulsos de información solamente.
- Contar mal los niveles: «entre +5 y −5 incluido el 0» son 11, no 10.
- $s$ usa el pulso **más corto**, aunque sea el de arranque.
- Redondear niveles **hacia arriba** (con menos no se alcanza la $R$ pedida).
- Si el enunciado no da $\tau$, dejá $R$ en función de $\tau$ y aclaralo; no inventes un valor sin decirlo.
- El ejercicio 2 del apunte resuelto tiene un error: escribe $I=\lg7^6=2{,}81$ bits (es $\lg7$). Lo correcto es $I=6\lg7=16{,}84$ bits y $R=168{,}4$ bps.
