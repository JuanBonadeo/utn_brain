# Podcast SIM 4 de 8 — Teoría de colas I: Kendall, Little y M/M/1

Fuente para un episodio de podcast de estudio. Materia: Simulación (UTN, Ingeniería en
Sistemas, 4.º año). Sirve para el primer parcial, el sábado 7 de noviembre de 2026: integrado
teórico-práctico y probablemente multiple choice. Las respuestas del banco son la clave revisada
por nosotros, no la corrección oficial de la cátedra.

## Indicaciones para el episodio

Las partes de un sistema de colas, la notación de Kendall, las medidas de rendimiento y las tres relaciones universales (ley de Little). El M/M/1: supuestos, por qué hace falta que ρ sea menor que 1 y qué pasa si no. Dar la intuición de las fórmulas en vez de enumerarlas.

## Contenido principal

### 7. Modelos analíticos de colas

*Fuente: Weitz cap. 13 (Rardin) completo y diapositivas "Teoría de colas".*

#### 7.1 Las características de un sistema de colas

**Población de clientes.**

- **Infinita**: la tasa de llegadas no cambia, sin importar cuántos clientes hayan llegado.
- **Finita**: **la tasa de llegadas disminuye a medida que aumenta el número de clientes en el sistema**, porque quedan menos clientes afuera que puedan llegar. Ejemplo: 100 telares que pueden romperse. La tasa depende del **estado** del sistema, no del reloj.

**Proceso de llegada.** Puede ser determinístico o probabilístico. Lo habitual es suponer un proceso de Poisson, es decir, tiempos entre llegadas exponenciales.

**Proceso de colas.** Tiene tres características:

- cuántas colas hay (una o varias);
- la capacidad (finita o infinita);
- la disciplina: FIFO (o PEPS), LIFO o por prioridad. En la materia se ve **FIFO**.

**Proceso de servicio.** Tiene tres características:

- uno o varios servidores en paralelo;
- servidores **idénticos** (todos atienden a la misma velocidad) o no;
- atención de a uno o en lotes.

**Fases.** Todo sistema pasa primero por una fase **transitoria**, que depende de las condiciones iniciales, y después llega al **estado estable**. **Las fórmulas analíticas valen solo en estado estable.**

#### 7.2 Notación de Kendall

> **Ojo:** la segunda letra es el tiempo de **servicio**, no el de llegadas. Y K es la capacidad del **sistema** (los que esperan más los que están siendo atendidos), no solo la de la cola.

#### 7.3 Medidas de rendimiento y ley de Little

| Símbolo | Medida |
|---|---|
| $L$ | número promedio de clientes **en el sistema** |
| $L_q$ | número promedio **en cola** |
| $W$ | tiempo promedio **en el sistema** |
| $W_q$ | tiempo promedio de espera **en cola** |
| $P_0$, $P_n$ | probabilidad de que haya 0 o $n$ clientes |
| $p_w$ | probabilidad de que un cliente que llega tenga que esperar |
| $U$ | utilización del servidor |
| $\rho = \lambda/\mu$ | **intensidad de tráfico**: tasa de llegadas sobre tasa de servicio (con $c$ servidores, $\lambda/(c\mu)$) |
| — | probabilidad de **negación de servicio** (en colas con capacidad limitada) |

**Relaciones universales**, que valen en estado estable para cualquier modelo:

$$L = \lambda W \qquad L_q = \lambda W_q \qquad W = W_q + \frac{1}{\mu}$$

Las dos primeras son la **ley de Little**. Con una medida y las relaciones, salen todas las demás.

#### 7.4 M/M/1

**Supuestos**:

- población **infinita**;
- llegadas **Poisson** de tasa $\lambda$;
- **una sola cola**, infinita, FIFO;
- **un servidor** con servicio **exponencial** de tasa $\mu$.

**Condición de estado estable: $\mu > \lambda$**, o sea $\rho < 1$.

| | |
|---|---|
| $P_0 = 1 - \rho$ | $P_n = (1-\rho)\,\rho^n$ |
| $L_q = \dfrac{\rho^2}{1-\rho}$ | $L = \dfrac{\rho}{1-\rho}$ |
| $W_q = L_q/\lambda$ | $W = W_q + 1/\mu$ |
| $U = \rho$ | $p_w = \rho$ |

> **Ojo:** con $\lambda > \mu$ **sí se puede simular**: la cola crece sin límite y se ve el servidor ocupado casi el 100% del tiempo. Lo que no existe es el estado estable, y por eso no hay solución analítica. Y con $\lambda < \mu$ **sí hay** solución analítica. Las dos preguntas salieron en 2025. Además, el resumen de alumnos de 2025 dice "población **finita**" para M/M/1: **está mal, es infinita**.

## Ampliación

### Las dos miradas sobre una cola

Esto es lo que la materia quiere que entiendas, y es la pregunta conceptual de fondo:

| | **Simulación** (Unidad 3) | **Modelo analítico** (esta unidad) |
|---|---|---|
| Fuente | Law cap. 1 §1.4 | Weitz cap. 13 |
| Qué hace | Corre el sistema evento a evento y **observa** | Aplica **fórmulas cerradas** |
| Qué produce | $\hat{d}(n)$, $\hat{q}(n)$, $\hat{u}(n)$ — **estimadores muestrales** de una corrida | $W_q$, $L_q$, $U$ — **valores exactos** de estado estacionario |
| Cuándo vale | Siempre; sirve para cualquier distribución | Solo si el sistema alcanzó el **estado estable** y las distribuciones son las supuestas |
| Precisión | Cada corrida da un número distinto | Un único valor exacto |

**La regla de la materia**: *si hay solución analítica disponible y computacionalmente eficiente,
usala; no simules*. Se simula cuando el sistema es demasiado complejo para una fórmula cerrada —
colas no exponenciales, servidores en serie, prioridades, balking, etc.

> **Pregunta de final oral** (aparece en el final resuelto 2020-08): *"¿Qué relación tiene el modelo
> M/M/1 con el modelo analítico?"* → El M/M/1 es el caso donde **las dos miradas se tocan**: podés
> simularlo y podés resolverlo con fórmula, y los resultados deben coincidir. Por eso se usa como
> **caso de validación**: si programás un simulador de M/M/1 y sus resultados no convergen a
> $L_q = \rho^2/(1-\rho)$, el simulador está mal. Es verificación por contraste.

➕ **Correspondencia entre ambas notaciones** (esto no está explícito en ninguna fuente y confunde):

| Simulación | Analítico | Qué mide |
|---|---|---|
| $\hat{d}(n)$ — demora promedio | $W_q$ | Tiempo promedio esperando en la cola |
| $\hat{q}(n)$ — nº promedio en cola | $L_q$ | Clientes promedio en la cola |
| $\hat{u}(n)$ — utilización | $U$ | Fracción de tiempo con el servidor ocupado |
| (no se calcula directo) | $W$, $L$ | Los mismos, pero **en el sistema** (cola + servicio) |

**Trampa**: $d$ y $q$ son de **cola**; $W$ y $L$ son de **sistema**. La simulación de Law mide cola;
las fórmulas de Weitz dan las cuatro. No las mezcles.

### Las tres relaciones universales

**Esto es lo más preguntado de toda la unidad.** Valen para **cualquier** sistema de colas con
población infinita y espacio de espera ilimitado, **sin importar las distribuciones**. No hace falta
saber si es M/M/1, M/G/3 ni nada: solo λ y μ.

Con:
- $\lambda$ = número promedio de **llegadas** por unidad de tiempo
- $\mu$ = número promedio de **clientes atendidos** por unidad de tiempo **en una estación**

#### (1) Tiempo en el sistema = espera + servicio

$$\boxed{W = W_q + \frac{1}{\mu}}$$

**La lógica**: el tiempo total que un cliente pasa en el sistema es lo que espera en la fila más lo
que dura su atención. Si se atienden 4 clientes por hora, cada uno requiere en promedio 1/4 de hora
de servicio. En general el tiempo promedio de servicio es $1/\mu$.

#### (2) Ley de Little, en el sistema

$$\boxed{L = \lambda \cdot W}$$

**La lógica intuitiva de Weitz** (vale la pena poder contarla, no solo escribir la fórmula):
imaginá un cliente que acaba de llegar y que va a permanecer en el sistema media hora. Durante esa
media hora siguen llegando otros a razón de λ = 12 por hora. Cuando este cliente se va, deja detrás
suyo en promedio $(1/2)\times 12 = 6$ clientes nuevos. Es decir: en promedio hay 6 clientes en el
sistema en cualquier momento dado.

#### (3) Ley de Little, en la cola

$$\boxed{L_q = \lambda \cdot W_q}$$

Mismo razonamiento aplicado solo a la fila.

#### Cómo se usan: conocido uno, salen todos

Weitz lo muestra así: sabiendo λ = 12, μ = 4, y habiendo determinado $L_q = 3$:

$$W_q = \frac{L_q}{\lambda} = \frac{3}{12} = \frac{1}{4} \quad \text{[de (3)]}$$
$$W = W_q + \frac{1}{\mu} = \frac{1}{4} + \frac{1}{4} = \frac{1}{2} \quad \text{[de (1)]}$$
$$L = \lambda W = 12 \cdot \frac{1}{2} = 6 \quad \text{[de (2)]}$$

> **Estrategia de examen**: las fórmulas específicas de cada modelo (§6 y §7) solo hacen falta para
> obtener **$P_0$ y $L_q$**. De ahí en adelante, las tres relaciones universales te dan $W_q$, $W$ y
> $L$ sin necesidad de recordar nada más. Memorizá $L_q$ y $P_0$ de cada modelo, y el resto se
> deduce.

➕ **Equivalentes en la notación de Law** (Apéndice 1B), por si el enunciado usa esa:

$$Q = \lambda d \qquad L = \lambda w \qquad w = d + E(S)$$

donde $d$ = demora promedio (≡ $W_q$), $w$ = tiempo promedio en el sistema (≡ $W$), $Q$ = número
promedio en cola (≡ $L_q$). **Son las mismas tres ecuaciones**, que Law llama *ecuaciones de
conservación*.

### Ejemplo resuelto completo — la estación de pesado de OTC

> Del apunte de cátedra §13.3. Camiones que llegan a una báscula. **λ = 60 camiones/hora,
> μ = 66 camiones/hora.**

**Intensidad de tráfico:**
$$\rho = \frac{\lambda}{\mu} = \frac{60}{66} = 0.9091$$

**1 · Probabilidad de sistema vacío:**
$$P_0 = 1 - \rho = 1 - 0.9091 = 0.0909$$
→ Aproximadamente el **9% del tiempo** un camión que llega no espera, porque la estación está vacía.
Dicho de otro modo, el 91% del tiempo tiene que esperar.

**2 · Número promedio en la fila:**
$$L_q = \frac{\rho^2}{1-\rho} = \frac{(0.9091)^2}{1-0.9091} = 9.0909$$
→ En estado estable hay en promedio **unos 9 camiones esperando** (sin contar el que se está pesando).

**3 · Tiempo promedio de espera en la cola:**
$$W_q = \frac{L_q}{\lambda} = \frac{9.0909}{60} = 0.1515 \text{ horas}$$
→ Unos **9 minutos** en la fila antes de empezar a pesarse.

**4 · Tiempo promedio en el sistema:**
$$W = W_q + \frac{1}{\mu} = 0.1515 + \frac{1}{66} = 0.1667 \text{ horas}$$
→ **10 minutos** desde que llega hasta que sale.

**5 · Número promedio en el sistema:**
$$L = \lambda W = 60 \times 0.1667 = 10$$
→ **10 camiones** en total, en la báscula o esperando.

**6 · Probabilidad de tener que esperar:**
$$p_w = 1 - P_0 = \rho = 0.9091$$

**7 · Distribución de estado:**
$$P_n = \rho^{\,n} P_0$$

| $n$ | $P_n$ |
|---|---|
| 0 | 0.0909 |
| 1 | 0.0826 |
| 2 | 0.0751 |
| 3 | 0.0683 |

→ *"¿Probabilidad de que no haya más de tres camiones?"* = suma de las cuatro = **0.3169**.

**8 · Utilización:**
$$U = \rho = 0.9091$$
→ La báscula está en uso el **91% del tiempo**; ociosa el 9%.

**Interpretación gerencial** (§13.3.2 — este tipo de cierre es lo que piden cuando dicen "interprete
las medidas"): W = 10 minutos es razonable y $L_q$ = 9 camiones es tolerable, porque la rampa de
salida tiene capacidad para 15. Pero la gerencia calcula la probabilidad de que haya **17 o más**
camiones (uno en servicio + 16 en la rampa) sumando $P_{17} + P_{18} + \dots$ y obtiene **0.20**: el
20% del tiempo la cola desborda hacia la autopista. Eso **no es aceptable**, y además se prevé que λ
suba a 70. De ahí nace el análisis del M/M/c.

### Errores y trampas

| # | Trampa | Lo correcto |
|---|---|---|
| 1 | ⚠️ Tu resumen dice que **M/M/1 tiene población finita** | **Infinita**, igual que M/M/c. Las etiquetas están intercambiadas en la pág. 20 |
| 2 | Confundir **cola** con **sistema** | $W_q$ y $L_q$ son de la cola; $W$ y $L$ incluyen el servicio. $W = W_q + 1/\mu$ |
| 3 | Dos definiciones de **ρ** | Weitz: $\rho = \lambda/\mu$ (con c>1 puede ser >1). Law: $\rho = \lambda/(c\mu)$ (siempre = utilización) |
| 4 | Decir que los **tiempos entre arribos son Poisson** | Poisson **cuenta eventos**; **exponencial** mide el tiempo entre ellos. El error está en un parcial resuelto |
| 5 | Aplicar las fórmulas **fuera del estado estable** | Todo el capítulo 13 vale **solo en estado estable**. Si $\lambda \ge \mu$, no hay estado estable |
| 6 | Olvidar que $\mu$ es **por estación** | En M/M/c, $\mu$ es la tasa de **un** servidor; la del sistema completo es $c\mu$ |
| 7 | Memorizar las 8 fórmulas de cada modelo | Alcanza con $P_0$ y $L_q$; el resto sale de las 3 relaciones universales |
| 8 | Confundir **población finita** con **cola finita** | Población finita → cambia λ (§2.1). Cola finita → aparece $p_d$ (§8). Son cosas distintas |

### En el TP 3: M/M/1 (cola infinita)

μ = 1 fijo y λ = 0,25 / 0,50 / 0,75 / 1,00 / 1,25, de modo que ρ = λ/μ va del 25 % al 125 %. Diez corridas de 20 000 unidades de tiempo por punto.

Fórmulas: L = ρ/(1−ρ), Lq = ρ²/(1−ρ), W = 1/(μ−λ), Wq = ρ/(μ−λ), U = ρ, P(n) = (1−ρ)·ρⁿ. Se cumple la ley de Little: L = λW y Lq = λWq.

| ρ | L sim / teo | Lq sim / teo | W sim / teo | U sim / teo |
|---|---|---|---|---|
| 0,25 | 0,329 / 0,333 | 0,083 / 0,083 | 1,313 / 1,333 | 0,249 / 0,250 |
| 0,50 | 1,006 / 1,000 | 0,500 / 0,500 | 2,012 / 2,000 | 0,505 / 0,500 |
| 0,75 | 2,863 / 3,000 | 2,113 / 2,250 | 3,838 / 4,000 | 0,748 / 0,750 |
| 1,00 | 106,9 ± 40 / ∞ | — / ∞ | 106,9 / ∞ | ≈ 1 |
| 1,25 | 2486 ± 55 / ∞ | — / ∞ | 2000 / ∞ | ≈ 1 |

**Resultados clave.** Con ρ < 1, la simulación coincide con la teoría, y la distribución P(n) simulada reproduce la geométrica: el simulador captura la distribución completa, no solo los promedios. Con ρ ≥ 1 no hay estado estacionario: L no converge y crece con el tiempo simulado.

## Preguntas de parcial y de práctica sobre este tema

**1.7** (parcial 2025) **¿Qué es la intensidad de tráfico ρ?**
✅ **B**: $\rho=\lambda/\mu$. D es falsa porque la probabilidad de sistema vacío es $P_0 = 1-\rho$, no $\rho$. Con $c$ servidores, $\rho = \lambda/(c\mu)$.
*`resumen-colas.md` §4.*

**1.8** (parcial 2025) **Condición de estado estable en M/M/1**
✅ **B**: $\mu>\lambda$, o sea $\rho<1$. Si $\lambda \ge \mu$ la cola crece sin límite y no hay estado estable.

**2.14** (parcial 2025) **Si la tasa de arribos es mayor que la de servicio, no se puede simular.** → ✅ **F**
Se puede simular igual: la cola crece sin límite y no se alcanza el estado estable. Lo que no existe es la **solución analítica** de estado estable.

**2.15** (parcial 2025) **Si la tasa de arribos es menor que la de servicio, no hay solución analítica.** → ✅ **F**
Es justamente al revés: con $\rho<1$ valen las fórmulas de M/M/1.

**E9** (pregunta inventada por alumnos de 2025) Estabilidad M/M/1: A) λ>μ · B) λ<μ · C) λ=μ · D) siempre

→ Respuesta: **B**

**P21** (práctica, no oficial) Ley de Little: A) $L=\lambda W$ · B) $L_q=\lambda W_q$ · C) $W=W_q+1/\mu$ · D) A y B · E) todas

→ Respuesta: **E**. Son las tres relaciones universales.

**P22** (práctica, no oficial) En el M/M/1, la probabilidad de que haya $n$ clientes en el sistema es: A) $(1-\rho)\rho^n$ · B) $\rho^n$ · C) $e^{-\rho}\rho^n/n!$ · D) $1-\rho$ · E) A y D

→ Respuesta: **A**. Geométrica en $n$. D es $P_0$.

**P23** (práctica, no oficial) Notación de Kendall A/B/c/K/N: ¿qué indica la segunda letra? A) distribución de los tiempos entre llegadas · B) distribución de los tiempos de servicio · C) nº de servidores · D) capacidad del sistema · E) población

→ Respuesta: **B**. A/**B**/c: llegadas / **servicio** / servidores.
