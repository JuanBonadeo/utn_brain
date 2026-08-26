# Elementos de probabilidad — Ross, capítulo 2

> **SIM · UTN-ISI · para el parcial 1**
>
> El capítulo 2 de Ross es el más denso del resumen, pero **más de la mitad no se toma nunca**.
> Este apunte se queda con lo que sí cayó en los nueve exámenes de `fuentes/examenes/`, ordenado
> por frecuencia y no por el orden del libro, y con la intuición antes de la fórmula.

---

## 0. Qué estudiar de acá

Cruzando el capítulo con los nueve parciales, globalizadores y finales guardados:

| Prioridad | Tema | Veces que cayó | Sección |
|---|---|---|---|
| **1** | **Proceso de Poisson** (homogéneo y no homogéneo) | **7** — en casi todos | §5 |
| **2** | **Esperanza y varianza**, con la demostración | **4** | §3 |
| **3** | **Distribuciones discretas** (binomial, Poisson, geométrica) | **6** | §4 |
| 4 | **Exponencial** y su papel en colas | 2 | §4 |
| 5 | **Axiomas** de probabilidad | 1 | §2 |
| — | Hipergeométrica *(no está en tu resumen)* | 1 | §4 |
| **0** | **Chebyshev, Markov, Leyes de los Grandes Números** | **nunca** | §6 — saltear |

**El dato más útil**: la sección 2.7 completa —Markov, Chebyshev, Ley Débil y Ley Fuerte— son las
páginas más difíciles del resumen (23 a 25, tres carillas de derivaciones) y **no aparecen en ningún
examen del archivo**. Ver §6 antes de gastar tiempo ahí.

---

## 1. El vocabulario mínimo

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

---

## 2. Axiomas de probabilidad

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

---

## 3. Esperanza y varianza

Es la **prioridad 2**, y siempre piden **demostrar**, no solo enunciar. Las dos demostraciones
están abajo, paso por paso.

### 3.1 Qué son

**Esperanza $E[X]$**: el promedio ponderado de los valores que puede tomar la VA, donde el peso de
cada valor es su probabilidad. Es "el valor al que tiende el promedio si repetís el experimento
muchísimas veces".

$$E[X] = \sum_i x_i\,p(x_i) \quad \text{(discreta)} \qquad\qquad E[X] = \int_{-\infty}^{\infty} x f(x)\,dx \quad \text{(continua)}$$

**Varianza $\mathrm{Var}(X)$**: cuánto se dispersan los valores alrededor de la media. Se mide con
el **promedio del cuadrado de la distancia a la media**:

$$\mathrm{Var}(X) = E\big[(X - \mu)^2\big] \qquad \text{donde } \mu = E[X]$$

> **Por qué el cuadrado**: si promediaras $(X - \mu)$ a secas te daría siempre cero, porque las
> desviaciones para arriba cancelan las de para abajo. El cuadrado las hace todas positivas.

### 3.2 La fórmula práctica de la varianza

Casi nunca se calcula con la definición: se usa esta versión, y **saber deducirla es parte de lo
que piden**.

$$\boxed{\mathrm{Var}(X) = E[X^2] - (E[X])^2}$$

**Demostración** (partiendo de la definición):

| Paso | Justificación |
|---|---|
| $\mathrm{Var}(X) = E[(X-\mu)^2]$ | definición |
| $= E[X^2 - 2\mu X + \mu^2]$ | desarrollo el cuadrado del binomio |
| $= E[X^2] - E[2\mu X] + E[\mu^2]$ | la esperanza de una suma es la suma de las esperanzas |
| $= E[X^2] - 2\mu E[X] + \mu^2$ | $2\mu$ y $\mu^2$ son **constantes**, salen afuera |
| $= E[X^2] - 2\mu\cdot\mu + \mu^2$ | porque $E[X] = \mu$ |
| $= E[X^2] - \mu^2 = E[X^2] - (E[X])^2$ | se cancelan dos de los tres términos |

### 3.3 Demostración 1 — $E[aX + b] = aE[X] + b$

> Pedida textual en **2022 P7** (*"Demuestre, en el caso de una variable aleatoria discreta X…"*)
> y en el **Globalizador 2023 P1** (*"…la esperanza de una variable aleatoria multiplicada por una
> constante y sumada con un término independiente"*).

| Paso | Justificación |
|---|---|
| $E[aX+b] = \sum_x (ax + b)\,p(x)$ | definición de esperanza, aplicada a la VA $(aX+b)$ |
| $= \sum_x \big[ax\,p(x) + b\,p(x)\big]$ | distribuyo $p(x)$ |
| $= \sum_x ax\,p(x) + \sum_x b\,p(x)$ | separo en dos sumatorias |
| $= a\sum_x x\,p(x) + b\sum_x p(x)$ | $a$ y $b$ son constantes, salen de la sumatoria |
| $= a\,E[X] + b\cdot 1$ | porque $\sum x\,p(x) = E[X]$ y $\sum p(x) = 1$ |
| $= a\,E[X] + b$ | ∎ |

> **La intuición**: si a todos los valores los estirás por $a$ y los corrés por $b$, el promedio se
> estira y se corre exactamente igual.

**Propiedad hermana** (se usa todo el tiempo, no requiere independencia):

$$E[X_1 + X_2] = E[X_1] + E[X_2] \qquad\text{y en general}\qquad E\left[\sum_{i=1}^{n} X_i\right] = \sum_{i=1}^{n} E[X_i]$$

### 3.4 Demostración 2 — $\mathrm{Var}(aX + b) = a^2\,\mathrm{Var}(X)$

> Pedida textual en **2024 P6** (*"Enuncie y demuestre a qué es equivalente la expresión
> Var(aX + b), siendo a y b constantes"*).

| Paso | Justificación |
|---|---|
| $\mathrm{Var}(aX+b) = E[(aX+b)^2] - \big(E[aX+b]\big)^2$ | fórmula práctica de §3.2 |
| $= E[a^2X^2 + 2abX + b^2] - \big(aE[X]+b\big)^2$ | desarrollo el cuadrado; en el segundo uso §3.3 |
| $= a^2E[X^2] + 2abE[X] + b^2 - \big(a^2(E[X])^2 + 2abE[X] + b^2\big)$ | esperanza de la suma; desarrollo el otro cuadrado |
| $= a^2E[X^2] - a^2(E[X])^2$ | se cancelan $2abE[X]$ y $b^2$ |
| $= a^2\big(E[X^2] - (E[X])^2\big)$ | factoreo $a^2$ |
| $= a^2\,\mathrm{Var}(X)$ | ∎ |

> **La intuición, y el punto que conviene decir en el examen**: **la $b$ desaparece.** Sumar una
> constante **corre** toda la distribución pero no la **dispersa** más, así que la varianza no
> cambia. Multiplicar por $a$, en cambio, estira las distancias a la media, y como la varianza mide
> distancias **al cuadrado**, queda multiplicada por $a^2$.

---

## 4. Las distribuciones

Son nueve y parecen un zoológico. **No lo son: están todas emparentadas.** Ese árbol es la mejor
forma de acordarse de cuál es cuál.

### 4.1 El árbol de familia

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

### 4.2 Discretas

| Distribución | Qué cuenta | Función de masa $p(x)$ | $E[X]$ | $\mathrm{Var}(X)$ |
|---|---|---|---|---|
| **Bernoulli** $Bi(1,p)$ | Un solo intento: 1 si éxito, 0 si fracaso | $p$ si $x=1$; $1-p$ si $x=0$ | $p$ | $p(1-p)$ |
| **Binomial** $Bi(n,p)$ | Nº de **éxitos** en $n$ intentos independientes | $\binom{n}{i} p^i (1-p)^{n-i}$ | $np$ | $np(1-p)$ |
| **Poisson** $\lambda$ | Nº de **eventos** en un intervalo, con tasa media $\lambda$ | $e^{-\lambda}\dfrac{\lambda^i}{i!}$ | $\lambda$ | $\lambda$ |
| **Geométrica** $p$ | Nº de intentos **hasta el primer éxito** | $p\,(1-p)^{n-1}$ | $\dfrac{1}{p}$ | $\dfrac{1-p}{p^2}$ |
| **Binomial negativa** (Pascal) | Nº de intentos **hasta el r-ésimo éxito** | $\binom{n-1}{r-1}p^r(1-p)^{n-r}$ | $\dfrac{r}{p}$ | $\dfrac{r(1-p)}{p^2}$ |
| **Hipergeométrica** | Como la binomial pero **sin reemplazo** | $\dfrac{\binom{N}{i}\binom{M}{n-i}}{\binom{N+M}{n}}$ | $np$ | $np(1-p)\dfrac{N-n}{N-1}$ |

**Notas cortas sobre cada una:**

- **Binomial**: $\binom{n}{i}$ es el **coeficiente binomial** — la cantidad de subconjuntos distintos de $i$ elementos que se pueden elegir de $n$. Una binomial es la **suma de $n$ Bernoulli IID**, y de ahí salen $E$ y $\mathrm{Var}$ directamente: $E[X] = \sum_{i=1}^n E[X_i] = np$, y lo mismo con la varianza. **Es la que más cayó** (2024 P7, Globalizador P2).
- **Poisson**: la única con $E[X] = \mathrm{Var}(X) = \lambda$. Se deduce de la binomial haciendo $\lambda = np$: $E = np = \lambda$, y $\mathrm{Var} = np(1-p) \approx \lambda$ porque $p$ es chiquísima.
- **Geométrica** (parcial 2025, pregunta 1.1): ojo que **hay dos convenciones** — Ross cuenta el **número del intento** en que ocurre el primer éxito (empieza en 1, $E = 1/p$); Naylor cuenta el **número de fracasos antes** del primer éxito (empieza en 0, $E = q/p$). **En el parcial usá la de Ross**, que es la del resumen.
- **Hipergeométrica**: urna con $N+M$ bolas, $N$ claras y $M$ oscuras; se saca una muestra de $n$ **sin reponer**, y $X$ = cuántas claras salieron. Al no reponer, los intentos **no** son independientes, y por eso no es binomial. El factor $\frac{N-n}{N-1}$ es la corrección por población finita.

### 4.3 Continuas

| Distribución | Cuándo se usa | Densidad $f(x)$ | $E[X]$ | $\mathrm{Var}(X)$ |
|---|---|---|---|---|
| **Uniforme** $(a,b)$ | Todos los valores del intervalo igual de probables | $\dfrac{1}{b-a}$ para $a<x<b$ | $\dfrac{a+b}{2}$ | $\dfrac{(b-a)^2}{12}$ |
| **Exponencial** $\lambda$ | **Tiempo entre eventos** de un proceso de Poisson | $\lambda e^{-\lambda x}$ para $x>0$ | $\dfrac{1}{\lambda}$ | $\dfrac{1}{\lambda^2}$ |
| **Normal** $(\mu,\sigma^2)$ | Suma de muchos efectos chicos (campana) | $\dfrac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$ | $\mu$ | $\sigma^2$ |

**La exponencial** es la única continua que se tomó (2021-10 P13, Final 2021-11 P6), y siempre con
la misma segunda parte: *"¿para qué usamos esta fórmula en un modelo de colas?"*

Su acumulada sale fácil y conviene saberla, porque es la que se invierte para generar tiempos:

$$F(x) = \int_0^x \lambda e^{-\lambda t}\,dt = 1 - e^{-\lambda x}$$

> **La respuesta completa a esa pregunta**: en un modelo **M/M/1**, tanto los tiempos entre arribos
> como los tiempos de servicio siguen una distribución exponencial. Las dos **M** de la notación de
> Kendall significan exactamente eso. Y como el tiempo entre eventos es exponencial, el número de
> eventos por unidad de tiempo es Poisson — por eso se dice que los arribos "siguen un proceso de
> Poisson con tasa λ" sin contradecir lo anterior.

**La normal** aparece en el resumen con la estandarización y el Teorema Central del Límite:

$$Z = \frac{X - \mu}{\sigma} \qquad \text{tiene } E[Z]=0,\ \mathrm{Var}(Z)=1$$

Se deduce en dos líneas con las propiedades de §3, tomando $a = 1/\sigma$ y $b = -\mu/\sigma$:
$E[Z] = \frac{1}{\sigma}\mu - \frac{\mu}{\sigma} = 0$ y $\mathrm{Var}(Z) = \frac{1}{\sigma^2}\sigma^2 = 1$.

> **Sobre el TCL**: no se tomó nunca como pregunta de este capítulo, pero **no lo ignores del
> todo** — es la base de los intervalos de confianza (Unidad 9) y del método que usa Naylor para
> generar normales sumando $K$ uniformes (Unidad 7). Alcanza con saber **qué dice**: la suma de
> muchas VA independientes con la misma distribución tiende a una normal, sin importar cuál era la
> distribución original.

---

## 5. El proceso de Poisson

**Es la prioridad 1: cayó en siete de los nueve exámenes**, y en 2022, 2023 y 2024 con la misma
redacción, palabra por palabra:

> Enuncie y describa las condiciones que hacen que la ocurrencia de ciertos "eventos" constituya un
> *Proceso de Poisson*. ¿Qué caracteriza a un proceso de Poisson *no homogéneo*?

### 5.1 Primero la idea

Pensá en las llamadas que entran a un call center. No sabés cuándo va a entrar cada una, pero sabés
que entran **a un ritmo parejo** de, digamos, 30 por hora. Un proceso de Poisson es la
formalización de eso: **eventos que ocurren de a uno, al azar, a un ritmo constante λ, sin que unos
afecten a otros.**

Llamamos $N(t)$ al **número de eventos ocurridos hasta el instante $t$**.

### 5.2 Las cinco condiciones

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

### 5.3 El no homogéneo

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

---

## 6. Lo que podés saltear

**Sección 2.7 completa — Desigualdad de Markov, Desigualdad de Chebyshev, Ley Débil y Ley Fuerte de
los Grandes Números.**

Son las páginas 23 a 25 de tu resumen, las más densas del capítulo: tres carillas de derivaciones
encadenadas. **Revisé los nueve exámenes del archivo —parciales 2021-10, 2021-12, 2022, 2023, 2024,
2025, globalizador 2023, finales 2020-08 y 2021-11— y no aparecen en ninguno.** Ni la palabra
"Chebyshev", ni "Markov", ni "grandes números".

Tampoco se tomaron nunca, aunque sí están en el resumen:

- **2.1** espacio muestral y eventos (más allá del vocabulario de §2)
- **2.3** probabilidad condicional e independencia
- **2.4** la definición formal de variable aleatoria
- La **binomial negativa** y la **normal** como preguntas propias
- El **Teorema Central del Límite** como pregunta de este capítulo

> **La salvedad honesta**: esto sale del archivo de exámenes viejos, no de un programa oficial. La
> propia transcripción de la clase pre-examen termina con *"Ojo, por ahí cambian los temas"*. Si te
> sobra tiempo el día antes, leé 2.7 por arriba para saber **qué dice** cada resultado, sin las
> demostraciones. Si andás justo, es lo primero que se recorta.

---

## 7. Checklist de repaso

- [ ] Enuncio las **cinco condiciones** del proceso de Poisson y explico cada una en castellano.
- [ ] Digo en una línea qué distingue al **no homogéneo** (se pierde el incremento estacionario).
- [ ] **Demuestro** $E[aX+b] = aE[X]+b$ justificando cada paso.
- [ ] **Demuestro** $\mathrm{Var}(aX+b) = a^2\mathrm{Var}(X)$ y explico por qué la $b$ desaparece.
- [ ] Deduzco $\mathrm{Var}(X) = E[X^2] - (E[X])^2$ desde la definición.
- [ ] Defino esperanza y varianza **en los dos mundos**, discreto y continuo.
- [ ] Escribo la función de masa, $E$ y $\mathrm{Var}$ de la **binomial**, la **Poisson** y la **geométrica**.
- [ ] Explico la relación **binomial → Poisson** (n grande, p chica, λ = np).
- [ ] Explico la relación **Poisson ↔ exponencial** y no las confundo.
- [ ] Digo para qué se usa la **exponencial en un modelo de colas** (las dos M de M/M/1).
- [ ] Enuncio los **tres axiomas** y deduzco $P(A^C) = 1 - P(A)$.
- [ ] Sé qué es la **hipergeométrica** y por qué no es binomial (sin reemplazo → no independientes).

---

## Fuentes

- `fuentes/Resumen Simulación.pdf` — Ross, capítulo 2, secciones 2.1 a 2.9 (págs. 21–29)
- `fuentes/examenes/` — parciales 2021-10, 2021-12, 2022, 2023, 2024, 2025; globalizador 2023; finales 2020-08 y 2021-11
- `fuentes/resumenes/Resumen 5.pdf` — Naylor caps. 3 y 4, para la hipergeométrica y las dos convenciones de la geométrica
- `fuentes/clase-preexamen/` — recortes de temas de la clase previa al examen
