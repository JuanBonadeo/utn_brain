# Sistemas de colas — resumen consolidado

> **SIM · UTN-ISI · para el parcial 1**
>
> Junta en un solo lugar todo lo que las cuatro fuentes dicen sobre colas: el resumen propio
> (`fuentes/Resumen Simulación.pdf`, que ya mezcla Law cap. 1 + Weitz cap. 13 + Ross cap. 2),
> el apunte oficial de cátedra (**Weitz cap. 13 completo**, `fuentes/apuntes-catedra/`), el
> resumen de Pagliaro (`fuentes/resumenes/Resumen 1.pdf`) y las consignas de los nueve exámenes
> viejos de `fuentes/examenes/`.
>
> Lo que **agregué** respecto del resumen propio, y las **correcciones** a los errores que tiene,
> van señaladas como tales a lo largo del texto.

---

## 0. Qué se toma de colas

Colas es, junto con inventarios, el tema con más presencia en el parcial. Del archivo de exámenes:

| Qué preguntan | Dónde cayó |
|---|---|
| **Relación entre medidas** (dada la tasa de servicio o de llegada, relacionar dos medidas, explicando cada símbolo) | 2021-10 P7, 2023 P4, 2024 P4, Globalizador P8, Final 2021-11 P5 — **5 veces** |
| **Condiciones del modelo M/M/1** | 2021-10 P9, 2021-12 P4, 2025 (1.8) |
| **Notación de Kendall** | 2022 P6, 2024 P5 |
| **Relación λ–μ para que el sistema funcione** | 2021-12 P9, 2025 (1.8) |
| **Las 3 medidas de la cola simple simulada** | 2022 P3, 2025 (1.2 y 2.13), 2019-Weitz |
| **Análisis económico** | 2023 P5 |
| **Denegación de servicio** (cola finita) | 2021-10 P15, Final 2021-11 P9 |
| **Condiciones del modelo M/M/c** | Globalizador P9 |
| **Intensidad de tráfico ρ** | 2025 (1.7) |
| **Población finita: qué pasa con la tasa de llegada** | 2025 (1.6) |
| **Exponencial: para qué la usamos en colas** | 2021-10 P13, Final 2021-11 P6 |

La forma más repetida, casi textual, es esta:

> En un modelo de colas (analítico), establezca la relación matemática entre la **tasa de servicio**
> (o número promedio de clientes atendidos por unidad de tiempo), y estas dos medidas de rendimiento:
> Tiempo promedio de espera en la cola — Tiempo promedio en el sistema. Exprese dicha relación
> simbólicamente (señalando el significado de cada símbolo que utilice).

Respuesta: $W = W_q + \frac{1}{\mu}$, aclarando qué es cada letra. La variante con **tasa de llegada**
pide $L = \lambda W$ (2023) o $L_q = \lambda W_q$ (2024). **Son tres fórmulas y el examen rota cuál pide.**

---

## 1. Las dos miradas sobre una cola

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

---

## 2. Anatomía de un sistema de colas

Un sistema de colas consiste en **uno o más servidores que brindan servicio a clientes que llegan**.
Los que encuentran todos los servidores ocupados se unen a una o más colas.

Se caracteriza por cuatro procesos. Weitz los enumera como cuatro (§13.1.1 a §13.1.4); Law los agrupa
en tres (mete la población dentro del proceso de llegada). **Para el examen conviene la versión de
Weitz, que es el apunte de cátedra.**

### 2.1 La población de clientes

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

### 2.2 El proceso de llegada

Cómo llegan los clientes a solicitar servicio. Su característica principal es el **tiempo entre
llegadas**: cuanto menor sea, más frecuentemente llegan los clientes y más se demanda a los servidores.

- **Determinístico**: los clientes llegan en intervalos fijos y conocidos.
- **Probabilístico**: los tiempos entre llegadas son inciertos, descriptos por una distribución. **Usualmente la exponencial.**

Si los tiempos entre arribos $A_1, A_2, \dots$ son **IID**, entonces:

$$E(A) = \text{tiempo promedio entre llegadas} \qquad \lambda = \frac{1}{E(A)} = \text{tasa de llegada}$$

> **IID** = independientes e idénticamente distribuidas: todas tienen la misma distribución de
> probabilidad y ninguna depende de las otras.

➕ **Por qué la exponencial** (pregunta 2021-10 P13 y Final 2021-11 P6): la exponencial es la
distribución de los **tiempos entre eventos** de un proceso de Poisson. Decir "los arribos siguen un
proceso de Poisson con tasa λ" y decir "los tiempos entre arribos son exponenciales con media 1/λ"
es **exactamente lo mismo**, visto desde el conteo o desde el intervalo. Por eso en M/M/1 los arribos
son Poisson y los tiempos entre arribos exponenciales, sin contradicción.

⚠️ **Error frecuente en los exámenes resueltos**: el parcial 2021-12 P3 dice *"los tiempos entre
arribos siguen esta distribución [Poisson]"*. Está mal dicho. **Poisson cuenta eventos por unidad de
tiempo (es discreta); exponencial mide el tiempo entre eventos (es continua).** Lo correcto: el
*número de arribos* en un intervalo es Poisson; el *tiempo entre arribos* es exponencial.

### 2.3 El proceso de colas

Cómo esperan los clientes para ser atendidos.

- **Cantidad de colas**: una sola línea (los clientes esperan en una única fila para pasar al próximo servidor que se libere) o **líneas múltiples** (eligen entre varias filas).
- **Número de espacios de espera**: finito o infinito.
- **Disciplina de cola**: la regla que determina qué cliente se atiende cuando un servidor queda libre.
  - **FIFO / PEPS**: primero en entrar, primero en salir. Es la de todos los modelos básicos.
  - **LIFO**: último en entrar, primero en salir.
  - **Prioridad**: según importancia o requerimientos de servicio.

### 2.4 El proceso de servicio

Cómo se atiende a los clientes.

- **Cantidad de servidores**: canal sencillo (una sola estación) o canal múltiple (varias estaciones en paralelo).
- **Tipo de servidores**: **idénticos** (todos atienden a la misma velocidad — el supuesto de los modelos básicos) o **no idénticos**.
- **Clientes atendidos simultáneamente** en una estación.
- **Prioridad / interrupción**: si un servidor puede detener la atención de un cliente para atender a otro que acaba de llegar.
- **Tiempo de servicio**: determinístico (cada cliente requiere la misma cantidad conocida) o probabilístico.

Si los $S_i$ son IID:

$$E(S) = \text{tiempo promedio de servicio} \qquad \mu = \frac{1}{E(S)} = \text{tasa de servicio de un servidor}$$

> Law usa $\omega$ para la tasa de servicio; Weitz usa $\mu$. **Son lo mismo.** En el parcial usá $\mu$,
> que es la del apunte de cátedra.

### 2.5 Las dos fases de todo sistema de colas

| Fase | Qué es |
|---|---|
| **Fase transitoria** | Período inicial en el que todavía se observan los efectos de las **condiciones iniciales** |
| **Estado estable** | Condición del sistema **después de que se han eliminado** los efectos de las condiciones iniciales |

> ⚠️ **Esto es crítico y se toma**: **todos los modelos analíticos de este resumen valen únicamente
> en estado estable.** Si el sistema no llegó al estado estable, las fórmulas no aplican. Por eso en
> simulación hay que descartar un **período de calentamiento** antes de medir (ver Unidad 9 de la wiki).

---

## 3. Notación de Kendall

Preguntada textual en 2022 P6 y 2024 P5: *"Describa la notación de Kendall para clasificar los
distintos modelos de colas."*

Formato completo: **A / B / c / K / L**

| Posición | Qué describe | Valores |
|---|---|---|
| **A** | Distribución de los **tiempos entre llegadas** | **D** determinística · **M** exponencial (markoviana) · **G** general, distinta de la exponencial |
| **B** | Distribución de los **tiempos de servicio** | **D** determinística · **M** exponencial · **G** general |
| **c** | Número de **estaciones o canales paralelos** (servidores idénticos en rapidez) | 1, 2, 3, … |
| **K** | Número **máximo de clientes en el sistema** (en servicio + esperando) | Se omite si es infinito |
| **L** | Número **total de clientes de la población** | Se omite si es infinito |

**Cuando se omite alguno de los dos últimos símbolos, se considera infinito.**

➕ **Símbolos adicionales que aparecen en Law** (Apéndice 1B) y no en Weitz:

- **GI** (*general independent*): tiempos entre arribos con distribución general, usado en la forma genérica **GI/G/s**.
- **$E_k$**: distribución **k-Erlang**.

Ejemplos:

| Notación | Significado |
|---|---|
| **M/M/1** | Llegadas exponenciales, servicio exponencial, 1 servidor, cola y población infinitas |
| **M/M/3** | Igual pero con 3 estaciones paralelas |
| **M/D/2** | Llegadas exponenciales, servicio **determinístico**, 2 servidores |
| **M/M/c/K** | c servidores, con **límite K** de clientes en el sistema (aparece denegación de servicio) |
| **GI/G/s** | Forma completamente genérica |

⚠️ **Nota sobre `M/M/c/K`**: el apunte de Weitz usa la misma sigla `M/M/c/K` para **dos cosas
distintas** — §13.6.1 la usa para *población finita* y §13.6.2 para *capacidad de espera limitada*.
Estrictamente, en la notación de cinco campos la población finita va en el **quinto** campo
(`M/M/c/∞/L`) y la capacidad limitada en el **cuarto** (`M/M/c/K`). Si te preguntan, definí qué campo
estás usando.

---

## 4. Catálogo de medidas de rendimiento

Weitz las organiza por el **tipo de pregunta** que responden. Esa estructura es útil para
memorizarlas:

### Preguntas de tiempo, centradas en el cliente

| Símbolo | Nombre | Qué responde |
|---|---|---|
| $W_q$ | **Tiempo promedio de espera** | ¿Cuánto espera en promedio un cliente **en la fila** antes de ser atendido? |
| $W$ | **Tiempo promedio en el sistema** | ¿Cuánto invierte en el sistema entero, **espera + servicio**? |

### Preguntas de cantidad de clientes

| Símbolo | Nombre | Qué responde |
|---|---|---|
| $L_q$ | **Longitud media de la cola** | ¿Cuántos clientes esperan en promedio **en la cola**? |
| $L$ | **Número medio en el sistema** | ¿Cuántos hay en promedio **en el sistema** (cola + en servicio)? |

### Preguntas probabilísticas

| Símbolo | Nombre | Qué responde |
|---|---|---|
| $p_w$ | **Probabilidad de bloqueo** | ¿Cuál es la probabilidad de que un cliente que llega tenga que esperar? |
| $U$ | **Utilización** | ¿Probabilidad de que un servidor esté ocupado? = fracción de tiempo que está ocupado |
| $P_n$ | **Distribución de probabilidad de estado** | ¿Probabilidad de que haya exactamente $n$ clientes en el sistema? |
| $p_d$ | **Probabilidad de negación de servicio** | Si el espacio de espera es finito: ¿probabilidad de que la cola esté llena y el cliente que llega no sea atendido? |

### Preguntas de costos

- ¿Cuál es el costo promedio por unidad de tiempo de operar el sistema?
- ¿Cuántas estaciones de trabajo se necesitan para la mayor efectividad de costos?

→ Ver sección 8.

### La intensidad de tráfico ρ

$$\rho = \frac{\lambda}{\mu}$$

> **Cuanto más cerca esté ρ de 1, más cargado está el sistema**, con colas más largas y esperas más
> grandes. Preguntada en 2025 (1.7).

⚠️➕ **Trampa grande: hay dos definiciones de ρ dando vueltas en tus fuentes.**

| Fuente | Definición | ¿Es la utilización? |
|---|---|---|
| **Weitz** (apunte de cátedra) | $\rho = \dfrac{\lambda}{\mu}$ | **Solo si c = 1.** Con c > 1 puede ser mayor que 1 |
| **Law** (Apéndice 1B) | $\rho = \dfrac{\lambda}{s\,\omega} = \dfrac{\lambda}{c\,\mu}$ | **Sí, siempre.** Es el "factor de utilización del sistema" |

En el ejemplo de M/M/c del propio apunte, con λ=70, μ=40, c=2: Weitz calcula **ρ = 1.75** —mayor
que 1— y sin embargo el sistema es estable, porque la utilización real es $U = \rho/c = 0.875$.

**Regla práctica**: en M/M/1 las dos definiciones coinciden y $\rho = U$. En M/M/c, con la notación
de Weitz, $U = \rho/c$. Si en el parcial te preguntan por "el factor de utilización", aclará con qué
definición trabajás.

---

## 5. Las tres relaciones universales

**Esto es lo más preguntado de toda la unidad.** Valen para **cualquier** sistema de colas con
población infinita y espacio de espera ilimitado, **sin importar las distribuciones**. No hace falta
saber si es M/M/1, M/G/3 ni nada: solo λ y μ.

Con:
- $\lambda$ = número promedio de **llegadas** por unidad de tiempo
- $\mu$ = número promedio de **clientes atendidos** por unidad de tiempo **en una estación**

### (1) Tiempo en el sistema = espera + servicio

$$\boxed{W = W_q + \frac{1}{\mu}}$$

**La lógica**: el tiempo total que un cliente pasa en el sistema es lo que espera en la fila más lo
que dura su atención. Si se atienden 4 clientes por hora, cada uno requiere en promedio 1/4 de hora
de servicio. En general el tiempo promedio de servicio es $1/\mu$.

### (2) Ley de Little, en el sistema

$$\boxed{L = \lambda \cdot W}$$

**La lógica intuitiva de Weitz** (vale la pena poder contarla, no solo escribir la fórmula):
imaginá un cliente que acaba de llegar y que va a permanecer en el sistema media hora. Durante esa
media hora siguen llegando otros a razón de λ = 12 por hora. Cuando este cliente se va, deja detrás
suyo en promedio $(1/2)\times 12 = 6$ clientes nuevos. Es decir: en promedio hay 6 clientes en el
sistema en cualquier momento dado.

### (3) Ley de Little, en la cola

$$\boxed{L_q = \lambda \cdot W_q}$$

Mismo razonamiento aplicado solo a la fila.

### Cómo se usan: conocido uno, salen todos

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

---

## 6. Modelo M/M/1

### Condiciones (pregunta textual: 2021-10 P9, 2021-12 P4)

1. Una población de clientes **infinita**.
2. Un proceso de llegada en el que los clientes se presentan de acuerdo con un **proceso de Poisson** con tasa promedio de $\lambda$ clientes por unidad de tiempo.
3. Un proceso de colas de **una sola línea de espera**, de **capacidad infinita**, con disciplina **FIFO/PEPS**.
4. Un proceso de servicio de **un solo servidor** que atiende según una **distribución exponencial**, con un promedio de $\mu$ clientes por unidad de tiempo.

**Condición de estado estable**: $\mu > \lambda$, equivalentemente $\rho < 1$.

> **Por qué** (pregunta 2021-12 P9, y 2025 1.8): si $\lambda \ge \mu$ llegan más clientes de los que
> se pueden atender, la cola crece indefinidamente y el sistema **nunca alcanza el estado estable**.
> Las fórmulas de abajo dejan de tener sentido — mirá que $L_q = \rho^2/(1-\rho)$ tiende a infinito
> cuando $\rho \to 1$.

⚠️ **ERROR EN TU RESUMEN.** En la página 20 dice, para M/M/1: *"Población de clientes **finita**"*.
**Está mal, es infinita.** Se ve claro por tres lados:

- El apunte de cátedra (Weitz §13.1.5) dice que esta clasificación *"pertenece a un sistema de colas en el que el tamaño de la población de clientes es **infinita**"*.
- La respuesta modelo del parcial 2021-10 P9 arranca con *"1. Una población de clientes infinita"*.
- Es lo que hace consistente el modelo: la población finita cambia la tasa de llegada (§2.1), y eso rompe todas las fórmulas de acá abajo.

Además, tu resumen le adjudica la población infinita al M/M/c — o sea que **las dos etiquetas están
intercambiadas**. Corregilo en tu copia: **ambos modelos suponen población infinita.**

### Tabla de fórmulas (Tabla 13.1 del apunte)

Con $\rho = \lambda/\mu$:

| Medida de rendimiento | Fórmula |
|---|---|
| Probabilidad de que **no haya clientes** en el sistema | $P_0 = 1 - \rho$ |
| **Número promedio en la fila** | $L_q = \dfrac{\rho^2}{1-\rho}$ |
| Tiempo promedio de espera en la cola | $W_q = L_q / \lambda$ |
| Tiempo promedio en el sistema | $W = W_q + \dfrac{1}{\mu}$ |
| Número promedio en el sistema | $L = \lambda \cdot W$ |
| Probabilidad de que un cliente que llega **tenga que esperar** | $p_w = 1 - P_0 = \rho$ |
| Probabilidad de que haya **n clientes** en el sistema | $P_n = \rho^{\,n} P_0$ |
| **Utilización** | $U = \rho$ |

➕ **Fórmula de Law que no está en la tabla de Weitz** (Apéndice 1B), útil como atajo:

$$L = \frac{\rho}{1-\rho}$$

Da directamente el número promedio **en el sistema** sin pasar por $L_q \to W_q \to W \to L$.
Comprobalo con el ejemplo de abajo: $0.9091/(1-0.9091) = 10$. ✓

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

---

## 7. Modelo M/M/c

### Condiciones (pregunta textual: Globalizador 2023 P9)

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

### Tabla de fórmulas

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

### Ejemplo resuelto — OTC con dos básculas

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

---

## 8. Colas finitas y denegación de servicio

Preguntado en 2021-10 P15 y Final 2021-11 P9, textual:

> Dada una cola finita de tamaño $n$ en un sistema de una cola y un servidor, ¿cómo se calcula la
> probabilidad de que un cliente no pueda entrar a la cola? (Denegación de servicio)

### El planteo

Cuando el área de espera es limitada, los clientes que llegan y la encuentran llena son **rechazados**
(y pueden o no volver). Ejemplos del apunte: un sistema de reservas telefónicas que solo mantiene un
número limitado de llamadas; una cinta transportadora de capacidad limitada entre dos etapas de
producción; un estacionamiento lleno.

### El cálculo

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

---

## 9. Análisis económico de los sistemas de colas

Preguntado en 2023 P5 (*"desarrolle brevemente algún aspecto del análisis económico"*). La clase
pre-examen lo marca explícitamente: **"Leer análisis económico"**.

### La idea

Hay un **trade-off**: más servidores cuestan más, pero reducen la espera, que también cuesta. El
objetivo es encontrar el número de servidores que **minimiza el costo total por unidad de tiempo**.

### Los componentes de costo

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

### Ejemplo resuelto — American Weavers, Inc.

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

---

## 10. Las tres medidas de la cola **simulada**

> Esto es de la Unidad 3 (simulación), pero cae seguido en las mismas preguntas que colas, así que
> va acá para tenerlo junto. Preguntado en 2022 P3, 2025 (1.2 y 2.13) y 2019-Weitz.

Sobre una corrida que termina cuando $n$ clientes completaron su demora, con $T(n)$ el tiempo total:

| Medida | Fórmula | Tipo de promedio |
|---|---|---|
| $\hat{d}(n)$ — **demora promedio** | $\dfrac{\sum_{i=1}^{n} D_i}{n}$ | **Sobre clientes** |
| $\hat{q}(n)$ — **nº promedio en cola** | $\dfrac{\int_0^{T(n)} Q(t)\,dt}{T(n)} = \dfrac{\sum_i i\,T_i}{T(n)}$ | **Sobre tiempo** |
| $\hat{u}(n)$ — **utilización** | $\dfrac{\int_0^{T(n)} B(t)\,dt}{T(n)}$ | **Sobre tiempo** |

**La distinción conceptual central**: $d(n)$ promedia **sobre clientes** (divide por $n$); $q(n)$ y
$u(n)$ promedian **sobre tiempo** (dividen por $T(n)$). Es la trampa clásica.

Detalles que se preguntan:
- La **demora no incluye el tiempo de servicio** — es solo lo que espera en la fila.
- **No se excluyen** los $D_i = 0$ (clientes que llegan y encuentran el sistema vacío); incluirlos refleja el buen desempeño del sistema.
- $B(t) = 1$ si el servidor está ocupado en $t$, 0 si está libre.
- $\sum_i i\,T_i$ **es el área bajo la curva $Q(t)$** — por eso la versión discreta y la integral son equivalentes.

---

## 11. Errores y trampas

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

---

## 12. Checklist de repaso

- [ ] Puedo enunciar las 4 condiciones de **M/M/1** y las 4 de **M/M/c**, con la condición de estado estable de cada uno.
- [ ] Escribo de memoria las **3 relaciones universales** y explico qué significa cada símbolo.
- [ ] Puedo contar la **lógica intuitiva** de $L = \lambda W$ (el cliente que se va deja λ·W detrás).
- [ ] Describo la **notación de Kendall** con los 5 campos y sé qué pasa cuando se omite uno.
- [ ] Sé la tabla de fórmulas de **M/M/1** (mínimo $P_0 = 1-\rho$ y $L_q = \rho^2/(1-\rho)$).
- [ ] Explico por qué $\mu > \lambda$ es necesario y qué pasa si no se cumple.
- [ ] Calculo la **denegación de servicio** por complemento.
- [ ] Armo un **análisis económico** con los 3 componentes de costo.
- [ ] Distingo las 3 medidas **simuladas** ($d$, $q$, $u$) de las **analíticas**, y sé cuál promedia sobre clientes y cuáles sobre tiempo.
- [ ] Explico qué relación tiene el M/M/1 con el modelo analítico (validación por contraste).

---

## Fuentes

- `fuentes/Resumen Simulación.pdf` — Law cap. 1 §1.4 y Apéndice 1B; Weitz §13.1, §13.2, §13.5
- `fuentes/apuntes-catedra/Apunte Weitz con hojas rotadas y acotado.pdf` — **capítulo 13 completo** (págs. 710–745 del libro), transcripto en `fuentes/txt/apuntes-catedra__Weitz__p41-60.md`
- `fuentes/resumenes/Resumen 1.pdf` (Pagliaro, UTN-FRRo) — sección 6
- `fuentes/examenes/` — parciales 2021-10, 2021-12, 2022, 2023, 2024, 2025; globalizador 2023; finales 2020-08 (resuelto) y 2021-11
- `fuentes/clase-preexamen/` — recortes de temas de la clase previa al examen
