# Podcast SIM 5 de 8 — Teoría de colas II: varios servidores, colas finitas y costos

Fuente para un episodio de podcast de estudio. Materia: Simulación (UTN, Ingeniería en
Sistemas, 4.º año). Sirve para el primer parcial, el sábado 7 de noviembre de 2026: integrado
teórico-práctico y probablemente multiple choice. Las respuestas del banco son la clave revisada
por nosotros, no la corrección oficial de la cátedra.

## Indicaciones para el episodio

M/M/c con una sola cola, población finita (la tasa de llegadas baja con el estado), capacidad limitada y probabilidad de negación de servicio, M/G/c (media y desvío del servicio) y el análisis económico: cuándo conviene agregar un servidor. Usar los ejemplos resueltos como historia.

## Contenido principal

#### 7.5 Otros modelos

- **M/M/c**: $c$ servidores idénticos en paralelo y **una sola cola**. Es estable si $\lambda < c\mu$. Hay que entender cómo funciona; **las fórmulas no se piden**.
- **Población finita** (M/M/c/K con K = tamaño de la población): la tasa de llegadas baja a medida que hay más clientes adentro. Se resuelve con software.
- **Capacidad de espera limitada** (M/M/c/K con K = capacidad máxima): los que llegan con el sistema lleno **se pierden**. La **probabilidad de negación de servicio** es la de encontrar el sistema lleno, y se calcula por complemento: $1 - (P_0 + \dots + P_K)$.
- **M/G/c**: el servicio tiene una distribución **general**, no exponencial. Hace falta conocer la **media y el desvío estándar** del tiempo de servicio. Un desvío de 0 corresponde a un servicio **determinístico**. Se resuelve con software (en el libro, STORM).

**Análisis económico (13.5).** El costo total es

$$c_s \cdot c + c_w \cdot L$$

o sea, costo por servidor por número de servidores, más costo de espera por clientes en el sistema. Con capacidad limitada se suma el **costo de negación**: costo por cliente perdido × tasa de llegadas × probabilidad de negación. Se elige el $c$ que **minimiza** el total.

## Ampliación

### La población de clientes

Conjunto de todos los posibles clientes del sistema.

- **Infinita**: el número de clientes potenciales es muy grande frente a la capacidad del sistema (clientes de un supermercado o un banco). Es el supuesto de todos los modelos básicos.
- **Finita**: número limitado de clientes. **El análisis es más complejo.**

➕ **Por qué la población finita complica todo** (Weitz §13.6.1, y es la pregunta 1.6 del parcial 2025):
cuando la población es finita, **la tasa de llegada no es constante: depende de cuántos clientes ya
están en el sistema**. Si hay 50 computadoras y 10 ya están rotas esperando reparación, solo quedan
40 que pueden romperse — la tasa de llegada baja. Con población infinita, en cambio, que haya
clientes en el sistema no cambia en nada la tasa a la que llegan los siguientes.

Ejemplos de población finita del apunte: 50 microcomputadoras atendidas por un equipo de
mantenimiento; 30 edificios cuyos ascensores mantiene una empresa; una flota de autos disponible
para 20 directivos.

### Modelo M/M/c

#### Condiciones (pregunta textual: Globalizador 2023 P9)

1. Una población de clientes **infinita**.
2. Llegadas según un **proceso de Poisson** con tasa promedio $\lambda$.
3. Un proceso de colas de **una sola línea** con disciplina **FIFO**.
4. **$c$ servidores idénticos** en paralelo, cada uno atendiendo según una **distribución exponencial** con promedio de $\mu$ clientes por unidad de tiempo.

**Condición de estado estable**: $\dfrac{\rho}{c} < 1$, equivalentemente $\lambda < c\,\mu$.

⚠️ En tu resumen esta condición aparece garabateada por la conversión como *"ρ = λ/µ . c < 1"*. Lo
correcto es $\dfrac{\lambda}{c\mu} < 1$, o sea $\dfrac{\rho}{c} < 1$ con la ρ de Weitz.

> 📌 **La clase pre-examen dice explícitamente que de M/M/c (§13.4) se pide "sólo un entendimiento
> general, no las fórmulas".** Prioridad: entender **en qué se diferencia del M/M/1** y saber las
> condiciones. Las fórmulas de abajo están para completitud, no para memorizarlas.

#### Tabla de fórmulas

Con $\rho = \lambda/\mu$ (ojo: puede ser > 1):

| Medida | Fórmula |
|---|---|
| Sistema vacío | $P_0 = \dfrac{1}{\left(\sum_{n=0}^{c-1}\frac{\rho^{n}}{n!}\right) + \frac{\rho^{c}}{c!}\cdot\frac{c}{c-\rho}}$ |
| Número promedio en la fila | $L_q = \dfrac{\rho^{\,c+1}}{(c-1)!}\cdot\dfrac{1}{(c-\rho)^{2}}\cdot P_0$ |
| Probabilidad de esperar | $p_w = \dfrac{1}{c!}\cdot\rho^{c}\cdot\dfrac{c}{c-\rho}\cdot P_0$ |
| Estado, si $n \le c$ | $P_n = \dfrac{\rho^{n}}{n!}\,P_0$ |
| Estado, si $n > c$ | $P_n = \dfrac{\rho^{n}}{c!\;c^{\,n-c}}\,P_0$ |
| Utilización | $U = 1 - \left[P_0 + \frac{c-1}{c}P_1 + \frac{c-2}{c}P_2 + \dots + \frac{1}{c}P_{c-1}\right]$ |

$W_q$, $W$ y $L$ salen de las tres relaciones universales, igual que en M/M/1.

#### Ejemplo resuelto — OTC con dos básculas

> Continuación del caso: **λ = 70, μ = 40, c = 2.**

$$\rho = \frac{70}{40} = 1.75 \qquad (\text{estable porque } \rho/c = 0.875 < 1)$$

$$\sum_{n=0}^{1}\frac{\rho^n}{n!} = 1 + 1.75 = 2.75 \qquad
\frac{\rho^{2}}{2!}\cdot\frac{2}{2-1.75} = 1.53125 \times 8 = 12.25$$

$$P_0 = \frac{1}{2.75 + 12.25} = \frac{1}{15} = 0.06667$$

$$L_q = \frac{(1.75)^3}{1!}\cdot\frac{1}{(2-1.75)^2}\cdot 0.06667 = 5.359375 \times 16 \times 0.06667 = 5.7167$$

$$W_q = \frac{5.7167}{70} = 0.0817 \text{ h} \approx 5 \text{ min}$$
$$W = 0.0817 + \frac{1}{40} = 0.1067 \text{ h} \approx 7 \text{ min}$$
$$L = 70 \times 0.1067 = 7.4667$$
$$p_w = \frac{1}{2!}(1.75)^2\cdot\frac{2}{0.25}\cdot 0.06667 = 0.8167$$
$$U = 1 - [0.06667 + 0.5 \times 0.11667] = 0.875$$

→ Cada báscula ocupada el **87.5% del tiempo** — que es exactamente $\rho/c$. ✓

### Colas finitas y denegación de servicio

Preguntado en 2021-10 P15 y Final 2021-11 P9, textual:

> Dada una cola finita de tamaño $n$ en un sistema de una cola y un servidor, ¿cómo se calcula la
> probabilidad de que un cliente no pueda entrar a la cola? (Denegación de servicio)

#### El planteo

Cuando el área de espera es limitada, los clientes que llegan y la encuentran llena son **rechazados**
(y pueden o no volver). Ejemplos del apunte: un sistema de reservas telefónicas que solo mantiene un
número limitado de llamadas; una cinta transportadora de capacidad limitada entre dos etapas de
producción; un estacionamiento lleno.

#### El cálculo

Para un sistema con **cola de tamaño finito $n-1$ y un servidor**, la capacidad máxima del sistema es
$n$ (contando el que está en servicio). La probabilidad de denegación de servicio es la probabilidad
de que el sistema esté lleno:

$$p_d = P_{n+1} + P_{n+2} + P_{n+3} + \dots$$

o, más práctico, por complemento:

$$\boxed{p_d = 1 - (P_0 + P_1 + P_2 + \dots + P_n)}$$

> **Cómo responderlo bien**: aclarar que $P_n$ se calcula con la distribución de estado del modelo
> ($P_n = \rho^n P_0$ en M/M/1), y que se suman **todos** los estados en que el sistema está lleno o
> desbordado. La versión por complemento es la que conviene, porque la sumatoria infinita no se
> puede evaluar término a término.

➕ Este es exactamente el cálculo que hace Weitz en §13.3.2 para la rampa de OTC: la probabilidad de
que haya 17 o más camiones es $1 - \sum_{n=0}^{16} P_n = 0.20$.

### Análisis económico de los sistemas de colas

Preguntado en 2023 P5 (*"desarrolle brevemente algún aspecto del análisis económico"*). La clase
pre-examen lo marca explícitamente: **"Leer análisis económico"**.

#### La idea

Hay un **trade-off**: más servidores cuestan más, pero reducen la espera, que también cuesta. El
objetivo es encontrar el número de servidores que **minimiza el costo total por unidad de tiempo**.

#### Los componentes de costo

| Componente | Fórmula | Qué es |
|---|---|---|
| **Costo de los servidores** | $c_s \cdot c$ | Costo por servidor por unidad de tiempo × número de servidores |
| **Costo de la espera** | $c_w \cdot L$ | Costo por unidad de tiempo por cliente en el sistema × número promedio en el sistema |
| **Costo de negación** *(solo si la cola es finita)* | $c_d \cdot \lambda \cdot p_d$ | Costo por cliente perdido × tasa de llegada × probabilidad de negación |

$$\boxed{\text{Costo total} = c_s\,c + c_w\,L + c_d\,\lambda\,p_d}$$

Sin denegación de servicio (cola infinita), el tercer término desaparece:
$\text{Costo total} = (c_s \cdot c) + (c_w \cdot L)$.

> ➕ **Qué incluye el costo de espera** $c_w$ — esto se pregunta: costos **explícitos** (ganancias no
> obtenidas, producción perdida) y costos **implícitos** (pérdida de buena voluntad del cliente si no
> se cumple con la fecha de entrega). Los implícitos son difíciles de estimar y ahí está la parte
> subjetiva del análisis.

#### Ejemplo resuelto — American Weavers, Inc.

> Del apunte §13.5. Máquinas tejedoras que se atascan y un equipo de reparadores.

**El modelado**: los "clientes" son las máquinas que se atascan; los "servidores" son los reparadores.
Hay muchas máquinas, así que se supone población infinita. Siete reparadores independientes e
idénticos, disciplina FIFO, una sola fila. Datos:

- Atascos ≈ proceso de Poisson con **λ = 25 por hora**.
- Reparación ≈ exponencial con tiempo promedio de 15 minutos → **μ = 4 máquinas/hora por reparador**.

→ Se modela como **M/M/7** con λ = 25, μ = 4.

**Los costos**: cada reparador cuesta $c_s$ = \$50/hora (con impuestos y cargas). Cada hora de máquina
parada cuesta $c_w$ = \$100.

**Con 7 reparadores** ($L$ = 12.0973 máquinas fuera de operación en promedio):

$$\text{Costo total} = (50 \times 7) + (100 \times 12.0973) = 350 + 1209.73 = \$1559.73 \text{ por hora}$$

Repitiendo el cálculo para cada tamaño de personal, el mínimo se alcanza con **9 reparadores**, a
**\$1128.63/hora**.

**La recomendación**: contratar dos reparadores más. Cuestan \$100/hora adicionales, pero el ahorro
por tener menos máquinas paradas es de unos **\$430/hora netos**.

> 📌 **La estructura del razonamiento es lo que se evalúa**, no las cuentas: identificar el sistema
> como un modelo de colas → estimar λ y μ de los datos → calcular $L$ para cada alternativa → armar
> la tabla de costo total → elegir el mínimo → traducirlo a una recomendación en pesos. Es
> exactamente el esqueleto del TPI.

### En el TP 3: M/M/1/K (cola finita): probabilidad de denegación

La capacidad del sistema es C = K + 1. Las fórmulas son P₀ = (1−ρ)/(1−ρ^(C+1)), Pₙ = P₀·ρⁿ y P(denegación) = P_C. El sistema es estable siempre, incluso con ρ ≥ 1. Con K = 0 es un sistema de pérdida pura: Pb = ρ/(1+ρ).

| K | ρ = 0,75 (Py / teo / AL) | ρ = 1,00 (Py / teo / AL) | ρ = 1,25 (Py / teo / AL) |
|---|---|---|---|
| 0 | 0,426 / 0,429 / 0,431 | 0,499 / 0,500 / 0,494 | 0,557 / 0,556 / 0,560 |
| 2 | 0,152 / 0,154 / 0,151 | 0,250 / 0,250 / 0,244 | 0,338 / 0,339 / 0,338 |
| 5 | 0,050 / 0,051 / 0,053 | 0,140 / 0,143 / 0,143 | 0,251 / 0,253 / 0,246 |
| 10 | 0,011 / 0,011 / 0,010 | 0,081 / 0,083 / 0,080 | 0,213 / 0,215 / 0,221 |
| 50 | 0,000 / 0,000 / 0,000 | 0,017 / 0,019 / 0,021 | 0,195 / 0,200 / 0,191 |

**El hallazgo del TP.** Con ρ < 1, agrandar la cola elimina el rechazo. Con ρ > 1 no: Pb tiende a 1 − 1/ρ (0,20 para ρ = 1,25) por más grande que sea K. El problema es de capacidad de servicio, no de tamaño de cola.

## Preguntas de parcial y de práctica sobre este tema

**1.6** (parcial 2025) **Con población de clientes finita, la tasa de llegada…**
A) varía con el tiempo · B) aumenta con el nº de clientes en el sistema · C) disminuye conforme aumenta el nº de clientes en el sistema · D) es constante · E) A y C

✅ **C**, textual del recuadro "Características clave" de Weitz (cap. 13): *"con un número finito de clientes, la tasa de llegadas disminuye conforme aumenta el número de clientes en el sistema"*. La tasa depende del **estado**, de cuántos clientes ya entraron, y no del reloj. Por eso A no es la característica.
*Unidad 8 · `resumen-colas.md` §2.1.*

**P31** (práctica, no oficial) Para analizar una cola **M/G/c** hace falta, además de $\lambda$: A) solo la media del servicio · B) la media y el desvío estándar del tiempo de servicio · C) que el servicio sea exponencial · D) que la población sea finita · E) C y D

→ Respuesta: **B**. Un desvío de 0 equivale a un servicio determinístico.

**P39** (práctica, no oficial) En un sistema de colas con capacidad limitada, el costo total incluye: A) solo servidores · B) servidores + espera + negación de servicio · C) solo espera · D) servidores + inventario · E) A y C

→ Respuesta: **B**. Weitz 13.5.
