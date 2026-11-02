# Podcast SIM 6 de 8 — Probabilidad para simular (Ross cap. 2)

Fuente para un episodio de podcast de estudio. Materia: Simulación (UTN, Ingeniería en
Sistemas, 4.º año). Sirve para el primer parcial, el sábado 7 de noviembre de 2026: integrado
teórico-práctico y probablemente multiple choice. Las respuestas del banco son la clave revisada
por nosotros, no la corrección oficial de la cátedra.

## Indicaciones para el episodio

Esperanza y varianza, las desigualdades de Markov y Chebyshev, la ley de los grandes números (lo que crece es n), el teorema central del límite, cuándo se usa cada distribución discreta y continua, y el proceso de Poisson homogéneo y no homogéneo. Remarcar: Poisson cuenta eventos, la exponencial mide el tiempo entre ellos.

## Contenido principal

### 8. Elementos de probabilidad

*Fuente: Ross caps. 1 y 2, hasta el proceso de Poisson no homogéneo. Lo que el profe dijo que no entra: §2.10 y las variables gamma.*

#### 8.1 Esperanza y varianza

**Propiedades.** Las tres primeras pueden pedirse con demostración:

- $E[aX + b] = a\,E[X] + b$
- $\mathrm{Var}(aX + b) = a^2\,\mathrm{Var}(X)$: **sumar una constante no cambia la dispersión**.
- $\mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) + 2\,\mathrm{Cov}(X, Y)$. Si son independientes, la covarianza es 0.
- $\mathrm{Var}(X) = E[X^2] - E[X]^2$
- $E\left[\sum X_i\right] = \sum E[X_i]$ vale **siempre**. Para la varianza de la suma hace falta **independencia**.

#### 8.2 Desigualdades y leyes de los grandes números

| Resultado | Enunciado | Cómo se demuestra |
|---|---|---|
| **Markov** | si $X \ge 0$ y $a > 0$: $P\{X \ge a\} \le \dfrac{E[X]}{a}$ | |
| **Chebyshev** | $P\{\lvert X - \mu \rvert \ge k\sigma\} \le \dfrac{1}{k^2}$ | Markov aplicado a $(X-\mu)^2/\sigma^2$, que tiene esperanza 1, con $a = k^2$ |
| **Ley débil** | $P\{\lvert \bar X_n - \mu \rvert > \varepsilon\} \to 0$ cuando $n \to \infty$ | con $\mathrm{Var}(\bar X) = \sigma^2/n$, que **necesita independencia**, y Chebyshev: la cota $\sigma^2/(n\varepsilon^2) \to 0$ |
| **Ley fuerte** | $\bar X_n \to \mu$ con probabilidad 1 | lo que tiende a infinito es **$n$**, la cantidad de variables, no el tiempo |

#### 8.3 Variables discretas

| Variable | Qué cuenta | $P\{X = i\}$ | $E$ | $\mathrm{Var}$ |
|---|---|---|---|---|
| **Bernoulli** | éxito (1) o fracaso (0) en un intento | $p$ / $1-p$ | $p$ | $p(1-p)$ |
| **Binomial** | éxitos en $n$ intentos independientes. Es la **suma de $n$ Bernoulli** | $\binom{n}{i} p^i (1-p)^{n-i}$ | $np$ | $np(1-p)$ |
| **Poisson** | eventos en un intervalo | $e^{-\lambda} \lambda^i / i!$ | $\lambda$ | $\lambda$ |
| **Geométrica** | **número del intento** del primer éxito | $(1-p)^{i-1} p$ | $1/p$ | $(1-p)/p^2$ |
| **Binomial negativa** (Pascal) | intentos hasta el $r$-ésimo éxito | $\binom{i-1}{r-1} p^r (1-p)^{i-r}$ | $r/p$ | $r(1-p)/p^2$ |
| **Hipergeométrica** | claras en $n$ extracciones **sin reposición**, de $N$ claras y $M$ oscuras | $\binom{N}{i}\binom{M}{n-i} / \binom{N+M}{n}$ | $np$ con $p = \frac{N}{N+M}$ | $np(1-p)\frac{N+M-n}{N+M-1}$ |

Tres cosas que se toman:

- **De binomial a Poisson.** Con $n$ grande y $p$ chico, la binomial se aproxima por una Poisson con $\lambda = np$. Ross no da umbrales numéricos, así que una opción que diga "**solo** si $n > 100$" es falsa.
- **Fórmulas de recurrencia.**
  - Binomial: $P_{i+1} = \frac{n-i}{i+1}\cdot\frac{p}{1-p}\,P_i$.
  - Poisson: $P_{i+1} = \frac{\lambda}{i+1}\,P_i$.
  
  Existen porque la fórmula directa (factoriales y potencias) es cara de calcular, y es lo que usa AnyLogic. Hay que saber para qué sirven; la demostración no se pide.
- La **Poisson** es la única de la tabla con $E = \mathrm{Var}$.

#### 8.4 Variables continuas y el TCL

| Variable | Densidad | $E$ | $\mathrm{Var}$ | Para recordar |
|---|---|---|---|---|
| **Uniforme** $(a, b)$ | $\frac{1}{b-a}$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | es la base de todo generador |
| **Normal** $(\mu, \sigma^2)$ | campana simétrica | $\mu$ | $\sigma^2$ | $aX + b$ sigue siendo normal; $Z = \frac{X-\mu}{\sigma}$ es $N(0, 1)$ |
| **Exponencial** (tasa $\lambda$) | $\lambda e^{-\lambda x}$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ | $F(x) = 1 - e^{-\lambda x}$ |

**La exponencial**:

- **No tiene memoria**: $P\{X > s + t \mid X > s\} = P\{X > t\}$. Es la **única continua** con esta propiedad.
- Si $X$ es exponencial de tasa $\lambda$, $cX$ es exponencial de tasa $\lambda/c$.
- El mínimo de exponenciales independientes es exponencial, con tasa igual a la **suma de las tasas**.
- En colas se usa para el servicio **por conveniencia matemática**, porque da soluciones cerradas, no porque sea realista.

**Teorema central del límite.** Si $X_1, X_2, \dots$ son i.i.d. con media $\mu$ y varianza $\sigma^2$ finitas, entonces para $n$ grande

$$\frac{\bar X_n - \mu}{\sigma/\sqrt{n}}\ \text{es aproximadamente}\ N(0, 1)$$

**sea cual sea** la distribución de las $X_i$. El profe dijo que es "muy importante". Ojo con dos trampas: la normal que se obtiene es **aproximada**, no exacta, y el teorema **no** exige que las $X_i$ sean normales.

#### 8.5 El proceso de Poisson

**Homogéneo, de tasa $\lambda > 0$.** $N(t)$ cuenta los eventos ocurridos en $[0, t]$, y se cumplen cinco condiciones:

1. $N(0) = 0$.
2. **Incrementos independientes**: lo que pasa en intervalos que no se superponen es independiente.
3. **Incrementos estacionarios**: la distribución del número de eventos en un intervalo depende **solo de su longitud**, no de dónde está.
4. $\lim_{h \to 0} P\{N(h) = 1\}/h = \lambda$: en un intervalo chico, la probabilidad de un evento es aproximadamente $\lambda h$.
5. $\lim_{h \to 0} P\{N(h) \ge 2\}/h = 0$: los eventos ocurren **de a uno**.

**Lo que se deduce de las cinco condiciones:**

- $N(t)$ tiene distribución **Poisson de media $\lambda t$**.
- Los **tiempos entre eventos** son **exponenciales i.i.d. de media $1/\lambda$**.

> **Ojo:** "los tiempos entre arribos siguen una distribución de Poisson" es **falso**, y es el error más repetido en los parciales viejos. La Poisson cuenta **cuántos** eventos hay (es discreta). La exponencial mide **cuánto tiempo pasa entre** eventos (es continua).

**No homogéneo, con intensidad $\lambda(t)$.** La tasa **varía con el tiempo**. Ejemplo: a un banco no llega la misma gente a las 10 que a las 15.

- Se pierde **solo** la condición 3, la estacionariedad.
- Los incrementos **siguen siendo independientes**.
- Con $m(t) = \int_0^t \lambda(y)\,dy$, el número de eventos en $(t, t+s]$ es Poisson de media $m(t+s) - m(t)$.

> **Ojo:** "en el no homogéneo no se mantienen los incrementos independientes" es **falso**. Lo que lo distingue del homogéneo es que **$\lambda$ varía con el tiempo**.

## Ampliación

### El vocabulario mínimo

Antes de las fórmulas, cuatro objetos. Todo el capítulo se mueve entre ellos.

**Variable aleatoria (VA)**: un número que sale de un experimento con azar. Nada más que eso.
"Cuántos clientes llegan en una hora" es una VA. "Cuánto tarda la atención" es otra.

Las VA se parten en dos mundos, y **casi todo el capítulo consiste en hacer lo mismo dos veces**,
una por mundo:

| | **Discreta** | **Continua** |
|---|---|---|
| Qué valores toma | Valores sueltos y contables: 0, 1, 2, 3… | Cualquier valor de un intervalo |
| Ejemplo | Nº de clientes que llegan | Tiempo que dura una atención |
| Se describe con | **Función de masa de probabilidad** $p(x) = P(X = x)$ | **Función de densidad** $f(x)$ |
| ¿Qué vale en un punto? | Una probabilidad de verdad | **No es una probabilidad**; hay que integrar |
| Suma / integra a 1 | $\sum_i p(x_i) = 1$ | $\int_{-\infty}^{\infty} f(x)\,dx = 1$ |
| Esperanza | $E[X] = \sum_i x_i\,p(x_i)$ | $E[X] = \int_{-\infty}^{\infty} x f(x)\,dx$ |

> **La regla para traducir de un mundo al otro**: donde la discreta suma, la continua integra; donde
> la discreta usa $p(x)$, la continua usa $f(x)\,dx$. Si te sabés una versión, te sabés las dos.

**Función de distribución acumulada $F(x)$**: la misma para los dos mundos.

$$F(x) = P(X \le x)$$

"La probabilidad de que la VA salga **como mucho** $x$". En la discreta es una escalera (salta en
cada valor posible); en la continua es una curva suave, y se cumple $f(x) = \dfrac{dF(x)}{dx}$.

> **Por qué importa $F$**: es la que se invierte en el **método de la transformada inversa** para
> generar variables aleatorias (Unidad 7 de la wiki). Todo el capítulo 2 existe para que ese método
> tenga sentido.

### Axiomas de probabilidad

Cayó una sola vez (parcial 2021-12 P7). Es media carilla: leelo y seguí.

Dado un experimento con espacio muestral $S$, a cada evento $A$ le asignamos un número $P(A)$ que
cumple tres axiomas:

| Axioma | Enunciado | En castellano |
|---|---|---|
| **1** | $0 \le P(A) \le 1$ | Una probabilidad va de 0 a 1, nunca fuera |
| **2** | $P(S) = 1$ | Algo del espacio muestral tiene que pasar |
| **3** | $P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i)$ para eventos **mutuamente excluyentes** | Si no pueden pasar juntos, las probabilidades se suman |

**Vocabulario que va con esto:**

- $S$ = **espacio muestral**: todos los resultados posibles. $A$ = **evento**: un subconjunto de $S$.
- $A \cup B$ (**unión**): los resultados que están en A, en B o en ambos.
- $AB$ (**intersección**): los que están en A **y** en B.
- $A^C$ (**complemento**): todo lo que está en $S$ y no en $A$. Ocurre $A^C$ ⟺ no ocurre $A$.
- **Mutuamente excluyentes**: $AB = \emptyset$, no pueden ocurrir a la vez.

**La consecuencia que se usa todo el tiempo** (y que conviene saber deducir): como $A$ y $A^C$ son
mutuamente excluyentes y $A \cup A^C = S$, por los axiomas 2 y 3:

$$1 = P(S) = P(A \cup A^C) = P(A) + P(A^C) \;\Longrightarrow\; \boxed{P(A^C) = 1 - P(A)}$$

**Probabilidad condicional e independencia** (nunca se tomó, pero es una línea):

$$P(A\mid B) = \frac{P(AB)}{P(B)}$$

Si $P(A \mid B) = P(A)$, entonces $A$ y $B$ son **independientes**, y ahí vale $P(AB) = P(A)P(B)$.
La relación es simétrica: si A es independiente de B, B lo es de A.

### El árbol de familia de las distribuciones

```
                    ENSAYO DE BERNOULLI
              (un intento: éxito con prob. p)
                            │
       ┌────────────────────┼────────────────────┐
       │                    │                    │
  fijo n intentos,    ¿cuántos intentos    igual que binomial
  ¿cuántos éxitos?    hasta el 1er éxito?   pero SIN reemplazo
       │                    │                    │
   BINOMIAL            GEOMÉTRICA          HIPERGEOMÉTRICA
    Bi(n,p)                 │
       │                    │ ¿y hasta r éxitos?
       │                    ▼
       │            BINOMIAL NEGATIVA
       │                (Pascal)
       │
       │  n muy grande, p muy chica, λ = n·p
       ▼
    POISSON  ◄──────────────────────►  EXPONENCIAL
  (cuenta eventos              (mide el TIEMPO
   por unidad de tiempo)        entre dos eventos)
```

**Las dos relaciones que se preguntan:**

1. **Binomial → Poisson** (parcial 2025, pregunta 1.12): cuando $n$ es grande y $p$ chica, con
   $\lambda = np$ fijo, la binomial se vuelve Poisson. Es la razón de ser de la Poisson.
2. **Poisson ↔ Exponencial**: son **el mismo fenómeno visto de dos maneras**. Si los eventos
   ocurren según Poisson con tasa $\lambda$, entonces el **tiempo entre eventos consecutivos** es
   exponencial con media $1/\lambda$. Una cuenta, la otra cronometra.

> ⚠️ **El error clásico**: decir "los tiempos entre arribos siguen una distribución de Poisson".
> **Está mal**, y aparece así en un parcial resuelto del archivo. Poisson **cuenta** (es discreta,
> da 0, 1, 2… eventos); exponencial **mide tiempo** (es continua). Lo correcto: *el número de
> arribos* en un intervalo es Poisson; *el tiempo entre arribos* es exponencial.

### El proceso de Poisson

**Es la prioridad 1: cayó en siete de los nueve exámenes**, y en 2022, 2023 y 2024 con la misma
redacción, palabra por palabra:

> Enuncie y describa las condiciones que hacen que la ocurrencia de ciertos "eventos" constituya un
> *Proceso de Poisson*. ¿Qué caracteriza a un proceso de Poisson *no homogéneo*?

#### Primero la idea

Pensá en las llamadas que entran a un call center. No sabés cuándo va a entrar cada una, pero sabés
que entran **a un ritmo parejo** de, digamos, 30 por hora. Un proceso de Poisson es la
formalización de eso: **eventos que ocurren de a uno, al azar, a un ritmo constante λ, sin que unos
afecten a otros.**

Llamamos $N(t)$ al **número de eventos ocurridos hasta el instante $t$**.

#### Las cinco condiciones

| | Condición | Qué dice en castellano |
|---|---|---|
| **a** | $N(0) = 0$ | Empezamos a contar desde cero |
| **b** | **Incrementos independientes**: el número de eventos en intervalos de tiempo **disjuntos** son independientes | Lo que pasó entre las 9 y las 10 no me dice nada de lo que va a pasar entre las 11 y las 12 |
| **c** | **Incrementos estacionarios**: la distribución del número de eventos en un intervalo depende **solo de su longitud**, no de su posición | Una hora cualquiera es igual a cualquier otra hora. Da lo mismo a las 3 AM que a las 6 PM |
| **d** | $\displaystyle\lim_{h\to 0}\frac{P(N(h)=1)}{h} = \lambda$ | En un intervalo chiquito de longitud $h$, la probabilidad de que ocurra **exactamente un** evento es aproximadamente $\lambda h$ |
| **e** | $\displaystyle\lim_{h\to 0}\frac{P(N(h)\ge 2)}{h} = 0$ | En un intervalo chiquito, la probabilidad de que ocurran **dos o más** es prácticamente cero: los eventos llegan de a uno |

> **En el multiple choice de 2025 (pregunta 1.5)** te dan las condiciones a), c) y d) por separado
> como opciones y la respuesta correcta es **"todas las anteriores"**. Reconocer que las tres
> juntas definen el proceso es justamente lo que evalúan.

#### El no homogéneo

**Lo único que cambia**: se cae la condición **(c)**, la de incrementos estacionarios. La tasa deja
de ser una constante $\lambda$ y pasa a ser una **función del tiempo $\lambda(t)$**.

| | Homogéneo | No homogéneo |
|---|---|---|
| Tasa | $\lambda$ constante | $\lambda(t)$, varía en el tiempo |
| Condición (a) $N(0)=0$ | ✓ | ✓ |
| Condición (b) incrementos independientes | ✓ | ✓ |
| **Condición (c) incrementos estacionarios** | **✓** | **✗ — es la que se pierde** |
| Condiciones (d) y (e) | con $\lambda$ | con $\lambda(t)$ |

**Por qué existe**: suponer que los eventos ocurren con la misma probabilidad en cualquier intervalo
de igual longitud **no siempre es realista**. A un banco no llega la misma cantidad de gente a las
10 de la mañana que a las 3 de la tarde. El no homogéneo permite modelar eso.

> **Cómo responder la pregunta en una línea**: *"Un proceso de Poisson homogéneo, a diferencia de
> uno no homogéneo, cumple la hipótesis de **incremento estacionario**: la distribución del número
> de eventos en un intervalo dado depende solamente de la longitud del intervalo y no de su
> posición en el tiempo."*

### TP 1.1 — Simulación de una ruleta

> **En criollo.** Hicimos una ruleta en Python que tira números del 0 al 36 y fuimos mirando cómo se comportan las cuentas tirada a tirada. Al principio es un caos: el 17 sale dos veces seguidas o no sale nunca. Con mil tiradas todo se acomoda a lo que dice la teoría: cada número sale 1 de cada 37 veces y el promedio da 18. Y si repetís el experimento 30 veces, los 30 promedios quedan amontonados alrededor de 18, en forma de campana. Es la ley de los grandes números y el teorema central del límite, vistos con los ojos.

**Qué pedía la consigna.**

- Un programa en Python que se corra como `python programa.py -c XXX -n YYY -e ZZ` (corridas, tiradas y número elegido), usando listas, `for` y Matplotlib.
- Cuatro gráficas mínimas para una corrida, cada una contra su valor esperado: frecuencia relativa del número, promedio, **desvío** y varianza.
- Después, varias corridas (con la cantidad justificada) en gráficas simultáneas, con un mínimo de 8 gráficas en total.
- Justificar cada cosa con la teoría (TCL, estadísticos) y entregar un informe en LaTeX con formato de paper (plantilla arXiv).

**Qué se hizo.** Una ruleta europea tiene 37 casilleros (del 0 al 36). Cada tirada es una uniforme discreta, generada con `random.randint(0, 36)`. El programa recibe por consola las corridas (`-c`), las tiradas (`-n`) y el número a estudiar (`-e`); se corrió con c = 30, n = 1000 y e = 17. Calcula tirada a tirada, en forma acumulada, la frecuencia absoluta y relativa del número elegido, la media, la varianza (estimador poblacional, divisor i) y el desvío. No usa NumPy: son bucles explícitos.

| Estadístico | Valor teórico (la línea roja de las gráficas) |
|---|---|
| P(X = e) | 1/37 ≈ 0,027 |
| Media μ | 18 |
| Varianza σ² | (37² − 1)/12 ≈ 114,33 |
| Desvío σ | ≈ 10,69 |
| Error estándar de la media (n = 1000) | σ/√n ≈ 0,338 |

**Resultados clave.**

- **Dentro de cada corrida se ve la ley de los grandes números.** Los estadísticos arrancan muy volátiles: la frecuencia relativa llega a 0,14, la media arranca en ≈ 31 y la varianza pica en ≈ 190. Se estabilizan cerca del valor teórico a partir de las 300 o 400 tiradas.
- **Entre corridas se ve el teorema central del límite.** Las 30 medias finales caen en (17,4; 18,6), dentro del μ ± 2σ/√n = 18 ± 0,676 que predice el TCL, y el histograma tiene forma de campana.
- Sobre las 30 000 tiradas, los 37 números quedan entre 0,025 y 0,029: el generador de Python se comporta como uniforme.

**Qué mostrar:** el embudo de las 30 corridas, que arrancan muy dispersas y terminan todas pegadas a 1/37, y el histograma de las medias finales. Con esas dos gráficas se cuentan la ley de los grandes números y el TCL.

**Ojo:** el informe se contradice en el orden de convergencia. Dice que primero converge la media (n ≈ 200), después la frecuencia relativa (n ≈ 400) y "finalmente" la varianza, pero a la varianza le asigna n ≈ 300. En error relativo, el orden real es media → varianza → frecuencia relativa. Con n = 1000, la media tiene un error relativo de ≈ 1,9 %, la varianza de ≈ 2,8 % y la frecuencia de un número puntual de ≈ 19 %, porque p = 1/37 es muy chica *(conocimiento general)*.

**Ojo (consigna):** la consigna pide la gráfica del **desvío** contra n, y el informe no la tiene. Tiene las de frecuencia absoluta, frecuencia relativa, media y varianza. La fórmula del desvío sí está (σ ≈ 10,69). Si lo marcan: el desvío es la raíz de la varianza, así que converge igual que ella, a 10,69. El mínimo de 8 gráficas se cumple (hay 9).

## Preguntas de parcial y de práctica sobre este tema

**1.1** (parcial 2025) **¿Qué propiedad caracteriza a una variable aleatoria geométrica?**
A) número de ensayos hasta el primer éxito · B) $E=1/p$, $\mathrm{Var}=(1-p)/p^2$ · C) es suma de Bernoulli independientes · D) A y B · E) todas

✅ **D.** A y B son la definición de Ross y sus momentos. C es falsa: la **suma de Bernoulli independientes es la binomial**, no la geométrica.
*Unidad 6, §2.8 de Ross.*

**1.5** (parcial 2025) **Proceso de Poisson homogéneo de tasa λ: ¿qué condición lo define?**
A) $N(0)=0$ e incrementos independientes · B) la distribución del nº de eventos depende solo de la longitud del intervalo · C) $\lim_{h\to0} P\{N(h)=1\}/h=\lambda$ · D) todas · E) A y C

✅ **D.** A, B y C son tres de las cinco condiciones de Ross. Falta $\lim P\{N(h)\ge 2\}/h = 0$, que no está entre las opciones. **B es la que distingue al homogéneo**, porque son los incrementos estacionarios.
*Unidad 6, §6.10 · `resumen-probabilidad.md` §5.2.*

**1.12** (parcial 2025) **Relación binomial–Poisson con n grande y p chico**
A) la binomial se aproxima a una Poisson con $\lambda=np$ · B) misma varianza · C) la Poisson es siempre aproximación exacta · D) solo cuando $n>100$ y $p<0{,}1$ · E) A y D

✅ **A.** D es falsa por el **"solo"**: Ross habla de "n grande, p chico", sin umbral. Esos umbrales son reglas prácticas y cambian según el libro. B también es falsa: $np(1-p)\neq np$, aunque se acercan cuando $p\to0$. C es falsa por el "siempre exacta".
*Unidad 6.*

**1.13** (parcial 2025) **¿Qué distingue al Poisson no homogéneo del homogéneo?**
A) la tasa λ varía en función del tiempo · B) los intervalos entre eventos no son exponenciales · C) no se mantienen los incrementos independientes · D) A y B · E) todas

◐ **A.** Es la definición de Ross: la intensidad $\lambda(t)$ depende de $t$.
C es **falsa**: el no homogéneo **mantiene** los incrementos independientes, y lo que pierde es la estacionariedad.
B es técnicamente **cierta**: con $\lambda(t)$ variable, los tiempos entre eventos dejan de ser exponenciales i.i.d. Pero Ross no lo dice en el cap. 2 y el profe no lo dio. Marcá **A**. Si en una variante aparece "A y B" junto a "todas", **"todas" es seguro falsa por C**.
*Unidad 6, §6.10 · `resumen-probabilidad.md` §5.3.*

**2b.2** (parcial real, otra fecha) **V/F: la frecuencia relativa se calcula como la *suma* de la frecuencia absoluta de algún valor entre el total de valores de la población o muestra.** → ✅ **F** (ellos: F)
La definición es el **cociente** $f_r = f_i/N$. El enunciado cambia "cociente" por "suma". Es una trampa de una sola palabra: leé cada palabra.

**2b.4** (parcial real, otra fecha) **V/F: la media o promedio es una medida de tendencia central; la media aritmética es el promedio estándar.** → ✅ **V**

**2b.7** (parcial real, otra fecha) **V/F: la frecuencia absoluta de un evento es el número de veces que se repite durante un experimento o muestra.** → ✅ **V**

**E6** (pregunta inventada por alumnos de 2025) La **exponencial**: A) modela tiempos entre eventos independientes · B) no tiene memoria · C) es la única continua sin memoria · D) solo para tiempos de servicio realistas

→ Respuesta: **A, B y C**. D es falsa: para servicio se usa **por conveniencia matemática**, no por realismo

**E7** (pregunta inventada por alumnos de 2025) ¿Cuáles son **discretas**? Normal · Binomial · Poisson · Hipergeométrica

→ Respuesta: **Binomial, Poisson e hipergeométrica**

**E15** (pregunta inventada por alumnos de 2025) Los **procesos de Markov** en simulación se representan con: A) tablas de frecuencias · B) matrices de transición de estados · C) uniformes · D) GIS

→ Respuesta: **B**

**P1** (práctica, no oficial) La desigualdad de Markov establece que, si $X \ge 0$ y $a>0$: A) $P\{X\ge a\}\le E[X]/a$ · B) $P\{X\ge a\}\ge E[X]/a$ · C) $P\{|X-\mu|\ge a\}\le \sigma^2/a^2$ · D) solo vale si $X$ es normal · E) A y C

→ Respuesta: **A**. Markov. C es Chebyshev con $a=k\sigma$, no Markov.

**P2** (práctica, no oficial) La desigualdad de Chebyshev $P\{|X-\mu|\ge k\sigma\}\le 1/k^2$ se demuestra: A) aplicando Markov a $(X-\mu)^2/\sigma^2$ con $a=k^2$ · B) con el teorema central del límite · C) aplicando la ley fuerte · D) solo para VA discretas · E) A y C

→ Respuesta: **A**. Markov sobre $(X-\mu)^2/\sigma^2$, que tiene esperanza 1, con $a=k^2$. Después se saca raíz.

**P3** (práctica, no oficial) En la ley débil de los grandes números, lo que tiende a infinito es: A) el tiempo de simulación · B) la cantidad $n$ de variables i.i.d. promediadas · C) la varianza · D) la media · E) A y B

→ Respuesta: **B**. Lo que crece es $n$, no el tiempo. Lo remarcó el profe.

**P4** (práctica, no oficial) Para probar la ley débil se usa que $\mathrm{Var}(\bar X)=\sigma^2/n$. Esto requiere: A) que las $X_i$ sean normales · B) que las $X_i$ sean independientes · C) que $n>30$ · D) nada · E) A y C

→ Respuesta: **B**. Independencia, para que se anulen las covarianzas.

**P5** (práctica, no oficial) $\mathrm{Var}(aX+b)$ es igual a: A) $a\,\mathrm{Var}(X)+b$ · B) $a^2\,\mathrm{Var}(X)$ · C) $a^2\,\mathrm{Var}(X)+b^2$ · D) $a\,\mathrm{Var}(X)$ · E) B y C

→ Respuesta: **B**. La constante $b$ no aporta varianza.

**P6** (práctica, no oficial) $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y$: A) siempre · B) solo si $\mathrm{Cov}(X,Y)=0$, por ejemplo si son independientes · C) nunca · D) solo si tienen la misma distribución · E) A y D

→ Respuesta: **B**. En general $+2\,\mathrm{Cov}(X,Y)$.

**P7** (práctica, no oficial) La binomial $(n,p)$ puede verse como: A) suma de $n$ Bernoulli$(p)$ independientes · B) nº de ensayos hasta el primer éxito · C) límite de la Poisson · D) una continua · E) A y B

→ Respuesta: **A**. B es la geométrica. Y la Poisson es límite de la binomial, no al revés.

**P8** (práctica, no oficial) ¿Por qué AnyLogic calcula la binomial y la Poisson con fórmulas de recurrencia? A) porque la fórmula directa (factoriales y potencias) es cara de calcular · B) porque la directa es inexacta por definición · C) porque la recurrencia es la definición · D) no las usa · E) B y C

→ Respuesta: **A**. Es lo que dijo el profe: la recurrencia es más barata.

**P9** (práctica, no oficial) La variable exponencial de tasa λ cumple: A) $E=1/\lambda$ · B) no tiene memoria: $P\{X>s+t\mid X>s\}=P\{X>t\}$ · C) es el tiempo entre eventos de un proceso de Poisson de tasa λ · D) A y B · E) todas

→ Respuesta: **E**. Las tres son ciertas.

**P10** (práctica, no oficial) En un proceso de Poisson de tasa λ, $N(t)$ tiene distribución: A) exponencial de media $1/\lambda$ · B) Poisson de media $\lambda t$ · C) binomial · D) uniforme en $(0,t)$ · E) A y B

→ Respuesta: **B**. Exponencial es el **tiempo entre** eventos. Poisson es la **cantidad**.

**P11** (práctica, no oficial) En un proceso de Poisson no homogéneo con intensidad $\lambda(t)$, el número de eventos en $(s, s+t]$ es: A) Poisson con media $\lambda t$ · B) Poisson con media $m(s+t)-m(s)$, con $m(t)=\int_0^t\lambda(y)\,dy$ · C) exponencial · D) no tiene distribución conocida · E) A y B

→ Respuesta: **B**. $m(t)$ es la función de valor medio.

**P12** (práctica, no oficial) El teorema central del límite dice que, para $n$ grande, la suma o el promedio de $n$ VA i.i.d.: A) tiende a la distribución de las $X_i$ · B) es aproximadamente normal, cualquiera sea la distribución de las $X_i$ · C) es exactamente normal · D) solo vale si las $X_i$ son normales · E) C y D

→ Respuesta: **B**. "Aproximadamente", para cualquier distribución con varianza finita.

**P13** (práctica, no oficial) Si $Z$ es normal estándar, $X=\mu+\sigma Z$ es: A) normal de media $\mu$ y varianza $\sigma$ · B) normal de media $\mu$ y varianza $\sigma^2$ · C) estándar · D) uniforme · E) A y C

→ Respuesta: **B**. La varianza es $\sigma^2$, no $\sigma$.

**P14** (práctica, no oficial) Una VA uniforme en $(a,b)$ tiene media y varianza: A) $(a+b)/2$ y $(b-a)^2/12$ · B) $(b-a)/2$ y $(b-a)/12$ · C) $(a+b)/2$ y $(b-a)/12$ · D) $0$ y $1$ · E) A y D

→ Respuesta: **A**.

**P15** (práctica, no oficial) V o F: los tiempos entre arribos de un proceso de Poisson siguen una distribución de Poisson.

→ Respuesta: **F**. Son **exponenciales**. Este error ya apareció en el parcial 2021-12.

**P16** (práctica, no oficial) V o F: en un proceso de Poisson los incrementos son independientes **y** estacionarios; en el no homogéneo deja de cumplirse la estacionariedad.

→ Respuesta: **V**.
