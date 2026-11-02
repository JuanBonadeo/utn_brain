# Simulación — Resumen para el Parcial 1

> **SIM · UTN-ISI · sábado 7/11/2026 · formato probable: multiple choice**
>
> Junta en un solo lugar todo lo que entra, con el nivel de detalle que pide un multiple choice: la definición exacta, la fórmula exacta y la condición exacta. El desarrollo largo de cada tema está en la wiki y en los resúmenes por tema (`resumen-probabilidad.md`, `resumen-colas.md`, `resumen-inventario.md`). Para practicar: `banco-preguntas.md`.

## 0. Qué entra y cómo se toma

**Alcance 2026** (lo dijo el profe el 14/10):

- **Ross cap. 2, §2.1 a §2.9.** No entran: las variables gamma, §2.10, los ejercicios del libro ni el cap. 1.
- **Todo lo visto antes en el apunte de Weitz**: Law cap. 1 (sistema, modelo, DES, cola simple, inventario), los 10 pasos y Weitz cap. 13 (colas).
- **No entra el análisis de resultados.** Va en la entrega final del TPI.
- **Números aleatorios (Naylor cap. 4 y pseudoaleatorios) y AnyLogic**: el resumen de los alumnos de 2025, *"tiene todo lo que entra"*, incluye las dos cosas. Además, en las preguntas reales que recopilaron, **la mitad son de números aleatorios**. **Tomalos como que entran**, a nivel concepto (§8 y §9).

**El formato 2025**, el único multiple choice que tenemos:

- 15 preguntas de opción múltiple (A a E).
- 17 de verdadero/falso o de selección múltiple.
- 1 ejercicio numérico de inventario.

De las 32 preguntas: 8 de colas, 11 de Law cap. 1, 4 de probabilidad y proceso de Poisson, 3 de números aleatorios, 1 de inventario y **5 de "cultura de cátedra"** (AnyLogic, GIS, LaTeX, POO, historia).

**También entran preguntas de estadística básica** que no están en ninguna unidad: media y frecuencia absoluta y relativa (§9).

**Reglas para el multiple choice** (salen de los errores del 2025):

1. **"A y B son correctas" casi nunca es la respuesta.** Fue correcta en 3 de 15. Antes de marcarla, verificá que **B sea verdadera por sí sola**.
2. **Palabras absolutas** como *siempre, solo, totalmente, asegura* o *nunca*: sospechá que es falsa.
3. **"Según el texto"** quiere decir que la opción correcta es la **definición textual** de Law o Ross.
4. **Un dato de entrada no es una medida de rendimiento**, y **un cambio de estado no es un evento**.
5. **En selección múltiple marcar de menos también resta.** Evaluá cada opción por separado.
6. **Doble negación**: en "la POO **no** es imprescindible", la respuesta es **V**.

## 1. Sistema, modelo y simulación (Law cap. 1)

### Definiciones textuales

| Concepto | Definición |
|---|---|
| **Sistema** | Colección de **entidades** (personas, máquinas) que **actúan e interactúan** juntas hacia el logro de algún **fin lógico**. Qué es el sistema depende de los objetivos del estudio |
| **Estado** | Colección de variables necesarias para describir el sistema en un momento dado, **relativas a los objetivos** |
| **Modelo** | Conjunto de **supuestos**, expresados como relaciones lógicas y matemáticas, que representan el comportamiento del sistema. Es un **recorte** de la realidad |
| **Simulación** | Uso de la computadora para **evaluar numéricamente** un modelo y **estimar** sus características. Genera una "historia artificial" del sistema |

**Trampa típica**: "un conjunto de ecuaciones" es un **modelo matemático**, y "un programa que imita al sistema" es una **simulación**. Ninguna de las dos es un sistema.

### Sistema discreto vs. continuo

- **Discreto**: las variables de estado cambian **instantáneamente** en puntos separados del tiempo. Ejemplo: la cola de un banco.
- **Continuo**: las variables de estado cambian **continuamente**. Ejemplo: la posición de un avión.

### Formas de estudiar un sistema

```
Sistema ─┬─ Experimentar con el sistema real
         └─ Experimentar con un modelo ─┬─ Modelo físico
                                        └─ Modelo matemático ─┬─ Solución analítica
                                                              └─ Simulación
```

- Experimentar con el sistema real **rara vez es factible**: es caro, perjudicial o el sistema no existe todavía.
- La **solución analítica es exacta**. **Si existe y es eficiente, se usa**: la simulación **no la reemplaza**.
- La simulación se usa cuando el modelo es **demasiado complejo** para resolverlo analíticamente. Las dos son **complementarias**: la simulación verifica supuestos del modelo analítico, y el analítico sugiere alternativas que después se simulan.

### Clasificación de modelos de simulación

Son tres ejes independientes:

| Eje | | |
|---|---|---|
| Tiempo | **Estático**: un instante, sin papel del tiempo (Montecarlo) | **Dinámico**: evoluciona en el tiempo |
| Azar | **Determinístico**: sin VA; la salida queda fija | **Estocástico**: con VA; **la salida es una estimación** |
| Cambio | **Continuo**: ecuaciones diferenciales | **Discreto**: eventos puntuales |

- Un modelo discreto **no** tiene por qué representar un sistema discreto. Se elige según los **objetivos**.
- Los modelos de la cátedra (cola, inventario) son **dinámicos, estocásticos y discretos**.

### Cuándo conviene simular y cuándo no

| ✅ Conviene | ❌ No conviene |
|---|---|
| Sistema complejo con elementos estocásticos sin solución analítica | Hay solución analítica eficiente (por ejemplo M/M/1) |
| Comparar diseños o políticas | El problema no tiene variabilidad |
| Control experimental, comprimir o expandir el tiempo | Se busca **optimizar**: un modelo analítico es mejor |
| El sistema no existe todavía | No hay datos ni estimaciones de la realidad |

**Desventajas que se toman**:

- **Cada corrida da una estimación, no un valor exacto**, así que hacen falta varias réplicas.
- Desarrollar un modelo es caro y lento.
- Se corre el riesgo de **confiar de más** en un modelo que no es válido.

**Para simular hace falta información de la realidad o estimaciones.** No hace falta POO ni que el modelo esté "totalmente testeado". Y **un modelo no necesita computadora**: puede ser físico o resolverse analíticamente.

## 2. Simulación a eventos discretos (DES)

- **Evento**: ocurrencia **instantánea** que **puede** cambiar el estado. **No siempre lo cambia**: también sirve para terminar la simulación o para programar decisiones.
- **DES**: modelo en el que las variables de estado cambian solo en un número **contable** de instantes.
- **Reloj de simulación**: guarda el tiempo **simulado**, que no tiene relación con el tiempo de CPU.

### Avance del tiempo

| | **Próximo evento** (next-event) | **Incremento fijo** (fixed-increment) |
|---|---|---|
| Cómo avanza | El reloj **salta** al evento más próximo de la lista | El reloj avanza de a $\Delta t$ |
| Inactividad | **La salta.** Es la ventaja principal: ahorra cómputo | **No la salta** |
| Error | Ninguno por discretizar | Los eventos se procesan **al final** del intervalo, y eso introduce error y obliga a desempatar |
| Uso | Casi todo el software comercial | Datos disponibles por período, por ejemplo anuales |

### Los componentes de un modelo DES

- Estado del sistema.
- **Reloj**.
- **Lista de eventos**.
- **Contadores estadísticos**.
- Rutina de **inicialización**.
- Rutina de **temporización**: busca el próximo evento y avanza el reloj.
- **Rutinas de evento**: una por tipo de evento.
- **Rutinas de librería**: generan las VA.
- **Generador de reportes**.
- **Programa principal**: llama a la rutina de temporización, después a la rutina del evento y al final revisa si hay que terminar.

### Variables, en el vocabulario de la cátedra

| Tipo | Qué son | Ejemplos en la cola |
|---|---|---|
| **Exógenas** | VA que **entran** al modelo | tiempo entre arribos, tiempo de servicio |
| **De estado** | Describen el sistema en un instante | servidor libre u ocupado, nº en cola, tiempos de arribo de los que esperan |
| **Endógenas** | Medidas de **rendimiento**: lo que sale del modelo | $d(n)$, $q(n)$, $u(n)$ |

## 3. La cola simple, simulada (Law)

- **Eventos**: **arribo** y **partida** (fin de servicio), nada más. "Servidor ocupado o libre" es un **estado**. "Inicio" es la rutina de inicialización.
- **Estado**: estado del servidor, número en cola y tiempos de arribo de los que esperan, que sirven para calcular la demora.
- **Corte**: cuando se completan $n$ demoras.

**Las tres medidas de rendimiento**:

| Medida | Fórmula | Promedia sobre |
|---|---|---|
| **$d(n)$**: demora promedio **en cola** | $\dfrac{\sum_{i=1}^n D_i}{n}$ | **clientes**; incluye las demoras $D_i=0$ |
| **$q(n)$**: nº promedio **en cola** | $\dfrac{\int_0^{T(n)} Q(t)\,dt}{T(n)}$, el área bajo $Q(t)$ | **tiempo** |
| **$u(n)$**: utilización | $\dfrac{\int_0^{T(n)} B(t)\,dt}{T(n)}$, con $B=1$ si está ocupado | **tiempo** |

- La **demora no incluye el servicio**.
- El tiempo de servicio y el tiempo de arribo son **entradas**, no medidas de rendimiento.
- En cada evento: `área += (reloj − tiempo del último evento) × valor viejo`.

## 4. Inventario (s, S) (Law)

**Política (s, S) con revisión periódica**, al **inicio de cada mes**:

- Si $I < s$, se pide $Z = S - I$.
- Si $I \ge s$, no se pide y no se paga nada.
- El pedido llega después de una demora $L$ (en clase, $U(0{,}5;\,1)$ meses). La política **no asegura** que $I$ quede entre $s$ y $S$: puede caer por debajo de $s$ y **hacerse negativo** (backlog).
- **Diferencia con IO**: en IO el control es **continuo** y se pide apenas se toca el punto de reorden. En simulación es **periódico**, y por eso hay backlog.

**Los niveles de inventario**:

- $I(t)$ puede ser negativo.
- $I^+(t) = \max(I,0)$ es lo que hay en stock.
- $I^-(t) = \max(-I,0)$ es lo que se debe.

### Costos

| Costo | Fórmula | Va con |
|---|---|---|
| **Pedido** | $K + iZ$, solo si $Z>0$ | $K$ es el costo fijo, $i$ el costo **unitario** y $Z$ la **cantidad** |
| **Mantenimiento** (holding) | $h\,\bar I^+$, con $\bar I^+ = \dfrac{\int_0^n I^+\,dt}{n}$ | **$h$ con $I^+$** |
| **Faltante** (backlog) | $\pi\,\bar I^-$, con $\bar I^- = \dfrac{\int_0^n I^-\,dt}{n}$ | **$\pi$ con $I^-$** |

$$\boxed{\text{CTPM} = \frac{\sum(K+iZ)}{n} + h\,\bar I^+ + \pi\,\bar I^-} \qquad n = \text{meses}$$

### Eventos y su orden

Ante empates se ejecutan en este orden:

1. Llegada de pedido.
2. Demanda.
3. **Fin de simulación**.
4. Evaluación.

En $t=n$ va primero el fin, para no hacer un pedido que no se va a contabilizar. Cuando llega un pedido, **primero cubre el backlog**.

### El ejercicio numérico

**Procedimiento**:

1. Armá los tres generadores por transformada inversa:
   - tiempo entre demandas: $-\text{media}\cdot\ln r$;
   - tamaño de demanda: acumulada y tramos;
   - demora: $a+(b-a)r$.
2. Hacé la **tabla de cada $r$ en sus tres usos**.
3. Corré los eventos y acumulá las áreas con el **nivel anterior** al evento.
4. Calculá el CTPM.

Resuelto con los datos de 2025, y las dudas de ese enunciado, en `banco-preguntas.md`, Parte 3. Un ejemplo que cierra completo está en `resumen-inventario.md` §7.3.

## 5. Los 10 pasos de un estudio de simulación

**Weitz.** Es la lista que usan las opciones del parcial. **Memorizá el orden**:

| # | Paso | Clave |
|---|---|---|
| 1 | Definición del sistema bajo estudio | objetivos, supuestos, variables de decisión, modelo conceptual |
| **2** | **Generación del modelo de simulación base** | traducir al lenguaje de simulación, **no demasiado detallado** |
| 3 | Recolección y análisis de datos | distribuciones de las VA |
| 4 | Generación del modelo preliminar | integra datos y supuestos |
| 5 | **Verificación** | ¿está bien **programado**? Es debugging |
| 6 | **Validación** | ¿representa a la **realidad**? Se compara con datos reales y con el cliente |
| 7 | Generación del modelo final | modelo raíz, contra el que se comparan los escenarios |
| 8 | Determinación de escenarios | pesimista, optimista e intermedio |
| 9 | Análisis de sensibilidad | intervalos de confianza de los mejores escenarios |
| 10 | Documentación, sugerencias y conclusiones | |

**Law**, por si aparece:

1. Formular el problema.
2. **Recopilar datos y definir el modelo**.
3. **Validar el documento de supuestos**.
4. Programar y **verificar**.
5. Corridas piloto.
6. **Validar el modelo programado**.
7. Diseñar experimentos.
8. Corridas de producción.
9. Analizar las salidas.
10. Documentar.

**Verificación vs. validación**:

- **Verificación**: el programa hace lo que quise programar.
- **Validación**: el modelo representa al sistema real.
- **Orden**: en Weitz se verifica (5) y después se valida (6). En Law hay una validación **antes** de programar (paso 3) y otra después (paso 6).

## 6. Probabilidad (Ross cap. 2)

### Esperanza y varianza

**Propiedades**, demostrables:

- $E[aX+b]=aE[X]+b$
- $\mathrm{Var}(aX+b)=a^2\,\mathrm{Var}(X)$: **$b$ no aporta varianza**.
- $\mathrm{Var}(X)=E[X^2]-E[X]^2$
- $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y+2\,\mathrm{Cov}(X,Y)$. Si $X$ e $Y$ son independientes, $\mathrm{Cov}=0$.
- $E\left[\sum X_i\right]=\sum E[X_i]$ **siempre**. La varianza de la suma es la suma de las varianzas **solo si son independientes**.

### Desigualdades y leyes

| Resultado | Enunciado | Notas |
|---|---|---|
| **Markov** | $X\ge0,\ a>0 \Rightarrow P\{X\ge a\}\le \dfrac{E[X]}{a}$ | |
| **Chebyshev** | $P\{\lvert X-\mu\rvert\ge k\sigma\}\le \dfrac{1}{k^2}$ | Markov aplicado a $(X-\mu)^2/\sigma^2$ con $a=k^2$, después raíz |
| **Ley débil** | $P\{\lvert\bar X_n-\mu\rvert>\varepsilon\}\to0$ cuando $n\to\infty$ | Usa $\mathrm{Var}(\bar X)=\sigma^2/n$, que **requiere independencia**, y Chebyshev con $k=\varepsilon\sqrt n/\sigma$: cota $\sigma^2/(n\varepsilon^2)\to0$ |
| **Ley fuerte** | $\bar X_n\to\mu$ con probabilidad 1 | lo que tiende a $\infty$ es **$n$**, no el tiempo |
| **TCL** | $\dfrac{\bar X_n-\mu}{\sigma/\sqrt n}$ es aproximadamente $N(0,1)$ para $n$ grande | **cualquiera** sea la distribución de las $X_i$ (i.i.d., varianza finita). Es aproximado, no exacto |

### Discretas

| VA | Qué cuenta | $P\{X=i\}$ | $E$ | Var |
|---|---|---|---|---|
| Bernoulli | éxito (1) o fracaso (0) | $p$ / $1-p$ | $p$ | $p(1-p)$ |
| **Binomial** | éxitos en $n$ ensayos; **suma de $n$ Bernoulli independientes** | $\binom ni p^i(1-p)^{n-i}$ | $np$ | $np(1-p)$ |
| **Poisson** | eventos en un intervalo | $e^{-\lambda}\lambda^i/i!$ | $\lambda$ | $\lambda$ |
| **Geométrica** | **nº de ensayo** del primer éxito | $(1-p)^{i-1}p$ | $1/p$ | $(1-p)/p^2$ |
| Binomial negativa | nº de ensayos hasta el $r$-ésimo éxito | $\binom{i-1}{r-1}p^r(1-p)^{i-r}$ | $r/p$ | $r(1-p)/p^2$ |
| Hipergeométrica | claras en $n$ extracciones **sin reposición** ($N$ claras, $M$ oscuras) | $\binom Ni\binom M{n-i}/\binom{N+M}n$ | $np$, con $p=\frac N{N+M}$ | $np(1-p)\frac{N+M-n}{N+M-1}$ |

- **Binomial → Poisson**: con $n$ grande y $p$ chico, la binomial se aproxima por una **Poisson con $\lambda = np$**. Ross no da umbrales: una opción con "**solo** si $n>100$" es falsa.
- **Recurrencias**: binomial $P_{i+1}=\frac{n-i}{i+1}\frac p{1-p}P_i$ y Poisson $P_{i+1}=\frac{\lambda}{i+1}P_i$. Se usan porque la fórmula directa es cara de calcular, y es lo que usa AnyLogic. Hay que saber para qué sirven, no demostrarlas.
- La **Poisson** es la única con $E = \mathrm{Var}$.

### Continuas

| VA | Densidad | $E$ | Var | Para recordar |
|---|---|---|---|---|
| **Uniforme** $(a,b)$ | $\frac1{b-a}$ | $\frac{a+b}2$ | $\frac{(b-a)^2}{12}$ | base de todo generador |
| **Normal** $(\mu,\sigma^2)$ | campana | $\mu$ | $\sigma^2$ | $aX+b$ sigue siendo normal; $Z=\frac{X-\mu}\sigma$ es $N(0,1)$ |
| **Exponencial** (tasa $\lambda$) | $\lambda e^{-\lambda x}$ | $\frac1\lambda$ | $\frac1{\lambda^2}$ | $F(x)=1-e^{-\lambda x}$ |

**La exponencial**:

- **No tiene memoria**: $P\{X>s+t\mid X>s\}=P\{X>t\}$. Es la **única continua** con esta propiedad.
- Si $X$ es exponencial de tasa $\lambda$, $cX$ es exponencial de tasa $\lambda/c$.
- El mínimo de exponenciales independientes es exponencial, con la **suma de las tasas**.
- Es el **tiempo entre eventos** de un proceso de Poisson. Por eso es la "M" de Kendall.

### Proceso de Poisson (prioridad 1)

**Homogéneo, de tasa $\lambda>0$.** Se cumplen las cinco condiciones:

- (a) $N(0)=0$.
- (b) **Incrementos independientes**: lo que pasa en intervalos disjuntos es independiente.
- (c) **Incrementos estacionarios**: la distribución depende **solo de la longitud** del intervalo.
- (d) $\lim_{h\to0}P\{N(h)=1\}/h=\lambda$.
- (e) $\lim_{h\to0}P\{N(h)\ge2\}/h=0$: los eventos ocurren **de a uno**.

**Consecuencias**:

- $N(t)$ es **Poisson de media $\lambda t$**.
- Los **tiempos entre eventos** son **exponenciales i.i.d. de media $1/\lambda$**. **No son Poisson**, error clásico.

**No homogéneo, con intensidad $\lambda(t)$**:

- Se pierde **solo** la condición (c). Los incrementos **siguen siendo independientes**.
- La tasa **varía con el tiempo**. Ejemplo: a un banco no llega la misma gente a las 10 que a las 15.
- Con $m(t)=\int_0^t\lambda(y)\,dy$, $N(t+s)-N(t)$ es Poisson de media $m(t+s)-m(t)$.

**Trampas del no homogéneo**:

- "La propiedad de incrementos independientes no se mantiene" es **falso**.
- "La característica que lo distingue" es que **λ varía en el tiempo**.

## 7. Colas analíticas (Weitz cap. 13)

**Población**:

- **Infinita**: la tasa de llegadas es constante.
- **Finita**: la tasa **disminuye a medida que aumenta el número de clientes en el sistema**, porque quedan menos clientes afuera que puedan llegar. Depende del **estado**, no del reloj.

**Kendall A/B/c/K/N**:

- **A**: tiempos entre llegadas.
- **B**: tiempos de **servicio**.
- **c**: servidores.
- **K**: capacidad del **sistema**.
- **N**: población.
- **M** = exponencial (markoviana), **D** = determinística, **G** = general.
- Si se omiten K y N, son infinitos.

**Intensidad de tráfico**: $\rho=\lambda/\mu$, la tasa de llegadas sobre la tasa de servicio. Con $c$ servidores, $\lambda/(c\mu)$.

**Relaciones universales** (Little), valen para cualquier modelo en estado estable:

- $L=\lambda W$
- $L_q=\lambda W_q$
- $W = W_q + 1/\mu$

### M/M/1

**Supuestos**:

- Población infinita.
- Llegadas Poisson de tasa $\lambda$.
- Una sola cola, infinita, FIFO.
- Un servidor exponencial de tasa $\mu$.

**Estado estable si y solo si $\mu>\lambda$**, o sea $\rho<1$. Si $\lambda\ge\mu$ **se puede simular igual**, pero la cola crece sin límite y no hay estado estable ni fórmula. Con $\rho<1$ **sí** hay solución analítica.

| | |
|---|---|
| $P_0 = 1-\rho$ (sistema vacío) | $P_n=(1-\rho)\rho^n$ |
| $L_q=\dfrac{\rho^2}{1-\rho}$ | $L=\dfrac{\rho}{1-\rho}$ |
| $W_q=L_q/\lambda$ | $W=W_q+1/\mu$ |
| Utilización $U=\rho$ | Probabilidad de esperar $=\rho$ |

### Otros modelos

- **M/M/c**: $c$ servidores en paralelo y **una sola cola**. Estable si $\lambda<c\mu$. **Solo concepto, sin fórmulas.**
- **Cola finita**, denegación de servicio: $p_{\text{rechazo}} = 1-(P_0+\dots+P_K)$, por complemento.
- **Análisis económico** (Weitz 13.5): el costo total es $c_s\cdot c + c_w\cdot L$, o sea el costo de los servidores más el de la espera. Con **cola limitada** (M/M/c/K) se suma el **costo de negación**: costo por rechazo × llegadas × probabilidad de rechazo. Se busca el $c$ que minimiza el total.
- **Fases** de todo sistema de colas: **transitoria**, que depende de las condiciones iniciales, y **estado estable**. Las fórmulas valen **solo en estado estable**.
- ⚠️ El resumen 2025 dice "población **finita**" para M/M/1. **Está mal: es infinita.** No te dejes llevar si aparece así.

## 8. Números aleatorios (concepto)

| | Verdaderos | Pseudoaleatorios |
|---|---|---|
| Origen | fuente **física**: cuántica (teóricamente impredecible) o caótica (prácticamente impredecible) | algoritmo **determinístico**, secuencial |
| Reproducibles | **no** | **sí**: la **semilla** determina toda la sucesión |
| Velocidad y costo | lentos y caros | **rápidos**, poca memoria, cualquier computadora |
| En simulación | no se prefieren | **se prefieren**, porque permiten repetir la corrida y comparar escenarios |

**Para qué sirven**: son la base de todo estudio de simulación estocástica. Con ellos se **generan VA de cualquier distribución** y se simulan las ocurrencias del modelo probabilístico.

**Un buen generador** produce valores:

- uniformes en $(0,1)$;
- independientes;
- reproducibles;
- con **período largo**;
- rápidos de calcular;
- con poca memoria.

**Cuadrados centrales** (von Neumann, 1946): **no está vigente**. Cae en ciclos cortos y en cero.

**GCL**: $Z_i=(aZ_{i-1}+c)\bmod m$, con $U_i=Z_i/m$.

- Es **mixto** si $c>0$ y **multiplicativo** si $c=0$.
- **Período completo** quiere decir $p=m$: recorre **todos** los valores antes de repetir. **No** quiere decir que "repite siempre el mismo número".
- **Teorema de Hull–Dobell**, para el mixto. Tiene período completo si se cumplen las tres:
  1. $m$ y $c$ son primos relativos.
  2. Todo primo que divide a $m$ divide a $a-1$.
  3. Si 4 divide a $m$, 4 divide a $a-1$.

**Generadores famosos**:

- **RANDU** (años 60 y 70): un GCL malo. Las ternas consecutivas caen en **pocos planos**, o sea que tienen correlación.
- **Todo GCL** tiene el mismo defecto: en dimensiones altas los puntos quedan sobre pocos hiperplanos.
- **`rand` de Matlab** hasta 1995: era un GCL multiplicativo, $7^5$ módulo $2^{31}-1$.
- **Mersenne Twister** (Matsumoto y Nishimura, **1997**): período $2^{19937}-1$, mejor distribución en varias dimensiones y pasa los tests. Es el de **Python, R, Ruby, C++, Excel y Matlab**, el estándar actual.

**Pruebas de aleatoriedad**:

- Hay **dos tipos**:
  - **empíricas**: se hacen sobre los números generados;
  - **teóricas**: se hacen sobre los parámetros del generador, sin generar números.
- Chi-cuadrado, series, corridas, póker y Kolmogórov-Smirnov son **pruebas concretas**, no tipos.
- **Hay que testear un generador antes de usarlo** (V).
- El ojo humano no distingue bien qué es aleatorio, y por eso se usan tests.

**Transformada inversa**: si $U\sim U(0,1)$, entonces $X=F^{-1}(U)$ tiene distribución $F$.

- **Exponencial**: $X=-\frac1\lambda\ln U$. Vale con $U$ o con $1-U$, porque tienen la misma distribución.
- **Discreta**: $X=x_j$ si $F(x_{j-1})\le U<F(x_j)$.
- **Uniforme** $(a,b)$: $X=a+(b-a)U$.

**Los tres métodos de Naylor (cap. 4) y cuándo se usa cada uno**:

| Método | Idea | Cuándo |
|---|---|---|
| **Transformada inversa** | $X=F^{-1}(U)$ | la inversa de la FDA es **fácil de obtener** (exponencial, uniforme, discretas) |
| **Rechazo** | generar candidatos y aceptarlos o rechazarlos según la densidad objetivo | la inversa **no tiene forma cerrada** |
| **Composición** (mezclas) | combinar distribuciones más simples | la densidad es una mezcla |

- **Normal**: no tiene inversa cerrada. Se genera con **Box-Muller** (exacto), con el **TCL** (sumar $K$ uniformes, por ejemplo 12, y restar 6) o con rechazo.
- Naylor también genera gamma, chi-cuadrado, lognormal, geométrica, Pascal, binomial, hipergeométrica, Poisson y **empíricas** (con una tabla de frecuencias observadas). Los **procesos de Markov** se simulan con una **matriz de transición**.
- **Montecarlo** se asocia con la simulación de procesos **estocásticos**, aunque en su origen también se aplicaba a problemas determinísticos.

## 9. Cultura de cátedra: AnyLogic, GIS, LaTeX, historia y estadística básica

> *(Conocimiento general. Salvo lo que se tomó en 2025, no está en la wiki.)*

**AnyLogic** es multimétodo. Tiene **tres paradigmas**, que son los de *AnyLogic en 3 días*:

| Paradigma | Abstracción | Elementos |
|---|---|---|
| **Eventos discretos** (DES) | proceso: entidades que pasan por recursos | Process Modeling Library: `Source → Queue → Delay/Service → Sink`, `ResourcePool`, `Seize/Release` |
| **Basado en agentes** (ABM) | individuos con comportamiento propio | agentes, **statecharts**, entorno; ejemplo: difusión de un producto |
| **Dinámica de sistemas** (SD) | agregados continuos | **stocks** (niveles), **flows** (flujos), variables auxiliares, lazos de realimentación; ecuaciones diferenciales |

- **Peatones, Road Traffic, Rail, Fluid y Material Handling son bibliotecas**, no paradigmas. Tampoco son paradigmas "GIS" ni "sistemas en tiempo real".

**M/M/1 en AnyLogic** (*The Art of Process-Centric Modeling*, en el resumen 2025):

| Bloque | Qué hace |
|---|---|
| **Source** | genera las llegadas; tiempo entre llegadas `exponential(λ)`, que es un proceso de Poisson |
| **Queue** | la cola de espera |
| **Seize** | **captura** un recurso, el servidor |
| **Delay** | el tiempo de servicio, `exponential(μ)` |
| **Release** | **libera** el recurso |
| **ResourcePool** | el conjunto de servidores: define la capacidad |
| **Sink** | la salida del sistema |
| **TimeMeasureStart / TimeMeasureEnd** | miden el tiempo en el sistema y en la cola |

- Los promedios de cantidad en el sistema y en cola se llevan con variables o con objetos *Statistics*, que se actualizan en los *On enter / On exit*.
- Las fórmulas de M/M/1 se incluyen **para compararlas con la simulación**.
- El **servicio exponencial no es realista**: se usa **por conveniencia matemática**, porque da solución cerrada.
- La exponencial es **la única continua sin memoria**.

**Estadística básica**, que se tomó:

- **Media aritmética**: medida de tendencia central, es "el promedio". **V.**
- **Frecuencia absoluta** $f_i$: cantidad de veces que se repite un valor o evento en la muestra. **V.**
- **Frecuencia relativa**: el **cociente** $f_i/N$. Si el enunciado dice "suma", es **F**.
- **GIS** es un *espacio* de AnyLogic para poner agentes sobre mapas reales.
- **GIS**, Sistema de Información Geográfica, es **multicapa**: superpone capas de datos georreferenciados. Por eso "monocapa" es **falso**.
- **LaTeX**: sistema de composición tipográfica de alta calidad, muy usado en artículos y libros científicos con matemática. **V.**
- **POO**: ayuda a modelar entidades y agentes, pero **no es imprescindible** para simular.
- **Historia**: la simulación por computadora viene de los **años 40**, con el método de Montecarlo y el Proyecto Manhattan. **No** surgió "en los últimos 30 años". GPSS es de 1961.
- **Los TP de clase** (cola M/M/1 e inventario):
  - Son modelos simples que se pueden simular **y** que tienen solución analítica.
  - Lo simulado se **compara** con lo analítico y da **parecido**.
  - Se pueden simular sin conocer la solución analítica.

## 10. Las 20 trampas, en una línea cada una

1. La **suma de Bernoulli** es binomial, no geométrica.
2. La **geométrica** cuenta el **nº de ensayo** del primer éxito: $E=1/p$.
3. Las **medidas de Law** son demora **en cola**, nº **en cola** y utilización. No el tiempo de servicio ni el nº en el sistema.
4. La política **(s, S)** no garantiza que $I$ quede entre $s$ y $S$, porque puede ser negativo.
5. **Sistema**, **modelo** y **simulación** son cosas distintas.
6. Con **población finita**, la tasa de llegadas **baja** cuando sube el número de clientes en el sistema.
7. $\rho=\lambda/\mu$. **Estable si $\mu>\lambda$.** $P_0=1-\rho$.
8. El **next-event** salta la inactividad. "Más fácil de programar" no es su ventaja.
9. Verificar = está bien programado. Validar = representa la realidad.
10. **Binomial → Poisson** con $\lambda=np$, sin umbrales fijos.
11. **No homogéneo**: $\lambda(t)$, con incrementos **independientes** pero **no estacionarios**.
12. **Tiempos entre arribos: exponenciales.** La cantidad de arribos es Poisson.
13. **Paso 2 de Weitz**: modelo de simulación **base**. Recolección de datos es el paso 3.
14. La **simulación no reemplaza** a la solución analítica. **La analítica es exacta.**
15. Con $\lambda>\mu$ **se puede simular**. Con $\lambda<\mu$ **hay** solución analítica.
16. **Ciclo completo** quiere decir $p=m$. La parte media del cuadrado **no está vigente**. Hay **dos tipos** de prueba: empíricas y teóricas.
17. Los **pseudoaleatorios** se prefieren a los verdaderos por velocidad y reproducibilidad.
18. Los **eventos** de la cola son arribo y partida. "Servidor ocupado" es un estado.
19. $\mathrm{Var}(aX+b)=a^2\mathrm{Var}X$, y $\mathrm{Var}(\bar X)=\sigma^2/n$ **necesita independencia**.
20. En la **ley de grandes números** lo que crece es **$n$**, la cantidad de variables, no el tiempo.

## Fuentes

- Wiki `SIM.md`: Unidades 1 a 8.
- `estudio/parcial1-alcance-2026.md` (clase del 14/10).
- `estudio/banco-preguntas.md` (parcial 2025 con la clave corregida).
- `estudio/resumen-probabilidad.md`, `resumen-colas.md`, `resumen-inventario.md`.
- Weitz cap. 13: `fuentes/txt/apuntes-catedra__Weitz__p41-60.md`.
- Resumen de alumnos 2025: `fuentes/resumenes/Resumen Simulación 2025 (con preguntas de parcial).docx`.
