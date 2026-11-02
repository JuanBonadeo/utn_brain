# Podcast SIM 7 de 8 — Números aleatorios y generación de variables

Fuente para un episodio de podcast de estudio. Materia: Simulación (UTN, Ingeniería en
Sistemas, 4.º año). Sirve para el primer parcial, el sábado 7 de noviembre de 2026: integrado
teórico-práctico y probablemente multiple choice. Las respuestas del banco son la clave revisada
por nosotros, no la corrección oficial de la cátedra.

## Indicaciones para el episodio

Verdaderos contra pseudoaleatorios, qué pide un buen generador, el congruencial lineal y el teorema de período completo, por qué fallan los cuadrados medios y RANDU, el Mersenne Twister, los dos tipos de pruebas (empíricas y teóricas) y los métodos para generar variables: transformada inversa, rechazo y composición.

## Contenido principal

### 9. Números aleatorios y generación de variables

*Fuentes: TP 2.1 (generadores), TP 2.2 (Naylor cap. 4), el capítulo de números pseudoaleatorios que citan los TP y random.org.*

#### 9.1 Generar números aleatorios

**Para qué sirven.** Son la base de toda simulación estocástica. A partir de una $U(0, 1)$ se genera **cualquier** distribución, y con eso se simulan las ocurrencias del modelo.

| | Verdaderos | Pseudoaleatorios |
|---|---|---|
| Origen | una fuente **física**: cuántica (teóricamente impredecible) o caótica (prácticamente impredecible). Ejemplos: random.org, que usa ruido atmosférico; ERNIE; la tabla de RAND de 1955 | un **algoritmo determinístico** que los genera de a uno, en secuencia |
| ¿Reproducibles? | **No** | **Sí**: la **semilla** determina toda la sucesión |
| Velocidad y costo | lentos y caros; **menos prácticos** | **rápidos**, poca memoria, cualquier computadora |
| En simulación | no se prefieren | **se prefieren**: permiten repetir una corrida y comparar escenarios en las mismas condiciones |

Los pseudoaleatorios buscan **comportarse como** los verdaderos, es decir, imitar sus propiedades estadísticas. Un pseudoaleatorio se define por una **semilla**, una **función de transición** y una **función de salida**.

**Un buen generador** produce números:

- uniformes en $(0, 1)$;
- independientes, sin patrones;
- reproducibles;
- con **período largo**;
- rápidos de calcular;
- con poco uso de memoria.

**Métodos y generadores conocidos**:

| Método | Qué hay que saber |
|---|---|
| **Cuadrados centrales** (von Neumann, 1946) | Se eleva al cuadrado y se toman los dígitos del medio. **No está vigente**: cae en ciclos cortos y, si aparece un cero, se queda en cero para siempre |
| **Generador congruencial lineal (GCL)** | $Z_i = (aZ_{i-1} + c) \bmod m$, con $U_i = Z_i/m$. Es **mixto** si $c > 0$ y **multiplicativo** si $c = 0$. Período máximo: $m$ |
| **RANDU** (IBM, años 60 y 70) | Un GCL **malo**: las ternas de números consecutivos caen en **pocos planos** (correlación). Todo GCL tiene ese defecto en dimensiones altas |
| **Mersenne Twister** (Matsumoto y Nishimura, 1997) | Período $2^{19937} - 1$, buena distribución en muchas dimensiones, pasa los tests. Es el de Python, R, Ruby, C++, Excel y Matlab. **Es el estándar actual** |

**Período completo** quiere decir $p = m$: el generador recorre **todos** los valores posibles antes de repetirse. No es "repetir siempre el mismo número", que sería una degeneración.

**Teorema de Hull–Dobell**, para el GCL mixto. Tiene período completo si y solo si se cumplen **las tres**:

1. $m$ y $c$ son primos relativos.
2. Todo primo que divide a $m$ divide también a $a - 1$.
3. Si 4 divide a $m$, 4 divide a $a - 1$.

**Pruebas de aleatoriedad.** Hay **dos tipos**:

- **empíricas**: se aplican a los números generados (chi-cuadrado, series, corridas, póker, Kolmogórov-Smirnov);
- **teóricas**: se aplican a los parámetros del generador, sin generar ningún número.

Hay que **testear el generador antes de usarlo**. El ojo humano no distingue bien qué es aleatorio.

#### 9.2 Generar variables aleatorias

**Transformada inversa.** Si $U \sim U(0, 1)$, entonces $X = F^{-1}(U)$ tiene distribución $F$.

- **Exponencial de media $m$**: $x = -m\,\ln(1 - u)$. Como $1 - U$ tiene la misma distribución que $U$, también vale $x = -m\,\ln u$, que es lo que se usa en el ejercicio de inventario.
- **Uniforme en $(a, b)$**: $x = a + (b - a)\,u$.
- **Discreta**: $X = x_j$ si $F(x_{j-1}) \le u < F(x_j)$.

**Los tres métodos de Naylor:**

| Método | Idea | Cuándo se usa |
|---|---|---|
| **Transformada inversa** | $X = F^{-1}(U)$ | cuando la inversa de la acumulada es **fácil de obtener** |
| **Rechazo** | se generan candidatos y se aceptan o rechazan según la densidad objetivo | cuando la inversa **no tiene forma cerrada** |
| **Composición** | se combinan (mezclan) distribuciones más simples | cuando la densidad es una mezcla |

**Las 9 distribuciones del TP 2.2:**

| Distribución | Tipo | Cómo se genera |
|---|---|---|
| Uniforme | continua | inversa: $a + (b-a)u$ |
| Exponencial | continua | inversa: $-m\ln u$ |
| Gamma (Erlang $k$) | continua | **suma de $k$ exponenciales** |
| Normal | continua | **TCL** (sumar 12 uniformes y restar 6) o **Box-Muller** (exacto). **No** por inversa, porque no tiene forma cerrada |
| Pascal | discreta | suma de geométricas: contar intentos hasta el $r$-ésimo éxito |
| Binomial | discreta | **suma de $n$ Bernoulli** |
| Hipergeométrica | discreta | simular las $n$ extracciones **sin reposición** |
| Poisson | discreta | contar cuántos tiempos exponenciales entran en una unidad de tiempo (o multiplicar uniformes hasta bajar de $e^{-\lambda}$) |
| Empírica discreta | discreta | inversa discreta con la tabla de frecuencias. Es la que usa el modelo de inventario |

## Ampliación

### TP 2.1 — Generadores pseudoaleatorios

> **En criollo.** La compu no puede tirar dados: los números "al azar" salen de una fórmula que, arrancando de una semilla, siempre da la misma secuencia. Programamos dos de esas fórmulas (el GCL y los cuadrados medios de von Neumann), las comparamos con la de Python y las pasamos por seis pruebas para ver si los números parecen azar de verdad. El GCL y el de Python aprueban todo. Cuadrados medios, al rato de arrancar, se queda trabado repitiendo los mismos cuatro números, y las pruebas lo agarran.

**Qué pedía la consigna.** Investigar generadores reales y pseudoaleatorios, y los tests para evaluarlos. Programar al menos dos generadores, entre ellos un GCL, y testear el GCL con al menos cuatro pruebas. Compararlos con otros, incluido el de Python, idealmente en una tabla de resultados.

**Qué se hizo.** Se programaron dos generadores y se compararon con el de Python, generando n = 10 000 valores con semilla fija:

- **GCL** (congruencial lineal mixto): Xᵢ₊₁ = (a·Xᵢ + c) mod m y Uᵢ = Xᵢ/m, con a = 1 103 515 245, c = 12 345, m = 2³¹ y X₀ = 5731.
- **Cuadrados medios** (von Neumann): se eleva al cuadrado y se toman los 4 dígitos centrales, con X₀ = 5731.
- **Python** `random.random()` (Mersenne Twister), como referencia.

Se aplicaron seis tests con α = 0,05: media, varianza, χ² con 10 intervalos (crítico 16,919), Kolmogorov-Smirnov (crítico 1,36/√n = 0,0136), corridas arriba y abajo de 0,5, y autocorrelación de lag 1.

| Test (criterio) | GCL | Cuadrados medios | Python |
|---|---|---|---|
| Media (Z < 1,96) | 0,044 ✓ | 3,32 ✗ | 0,886 ✓ |
| Varianza (Z < 1,96) | 0,017 ✓ | 27,99 ✗ | 0,240 ✓ |
| χ² (< 16,919) | 3,15 ✓ | 14 795,75 ✗ | 4,70 ✓ |
| KS (< 0,0136) | 0,0049 ✓ | 0,2078 ✗ | 0,0090 ✓ |
| Corridas (Z < 1,96) | 0,997 ✓ | 0,060 ✓ | 0,434 ✓ |
| Autocorrelación (Z < 1,96) | 1,259 ✓ | 0,182 ✓ | 0,121 ✓ |

**Resultado:** el GCL y Python pasan los seis tests. Cuadrados medios falla los cuatro que miran la distribución.

**Qué mostrar:** el histograma. Las cuatro barras naranjas son el TP.

**Lo que el informe no dice y conviene saber (verificado corriendo el código).** Con semilla 5731, cuadrados medios cae en el paso 71 en el ciclo **6100 → 2100 → 4100 → 8100 → 6100** y no sale más. De los 10 000 valores, solo 75 son distintos; el resto repite 0,61 / 0,21 / 0,41 / 0,81. Eso explica toda la tabla:

- **χ² y KS enormes:** el 99 % de los valores cae en 4 de los 10 intervalos.
- **Media rechazada:** el ciclo promedia 0,51 en vez de 0,50.
- **Por qué pasa corridas y autocorrelación.** El ciclo queda arriba, abajo, abajo, arriba de 0,5: corridas de largo 2, que es justo lo que se espera de una secuencia aleatoria. Y la autocorrelación de lag 1 del ciclo da exactamente 0. Cada test mira una sola propiedad, y por eso se aplica una batería y no un test suelto.

**Por qué el GCL anda** *(conocimiento general; el teorema está en la Unidad 7.4 de la wiki)*: con m = 2³¹, c impar y a − 1 múltiplo de 4 se cumple el teorema del GCL mixto, así que el período es completo (2³¹). Son los parámetros del `rand()` de ANSI C. Su debilidad conocida es que los bits bajos tienen período corto y que, en varias dimensiones, los puntos caen sobre hiperplanos.

**Consigna:** cumplida de punta a punta, y con más de lo pedido: tres generadores y seis tests donde se pedían dos y cuatro.

### TP 2.2 — Variables aleatorias de 9 distribuciones

> **En criollo.** El generador te da números entre 0 y 1, todos con la misma chance. Pero para simular necesitás otras formas de azar: tiempos entre llegadas (exponencial), medidas que se amontonan en el medio (normal), cuántos clientes llegan en una hora (Poisson). Este TP es el recetario para transformar esos uniformes en nueve distribuciones distintas, siguiendo el libro de Naylor, y comprobar que lo que sale tiene la media, la varianza y la forma que tiene que tener. Las nueve dieron bien.

**Qué pedía la consigna.**

- Para cada distribución: la teoría (parámetros, función de probabilidad, gráficas), el paso a paso de la acumulada y su inversa, un programa en Python y un test.
- El código tenía que ir dentro del informe.
- Una tabla guía de la cátedra marcaba qué hacer con cada una: transformada inversa para las 9, **método de rechazo para la uniforme, la exponencial y la normal**, y test al menos para uniforme, exponencial, normal, binomial, Poisson y empírica.

**Qué se hizo.** A partir de U(0,1) (`random.random()`, semilla 42) se generaron 10 000 valores de nueve distribuciones. Cada una se validó contra la teoría con la media, la varianza y una prueba de ajuste: Kolmogorov-Smirnov para las continuas y χ² para las discretas.

| Distribución (parámetros) | Método | Media obs / teo | Var obs / teo | Ajuste |
|---|---|---|---|---|
| Uniforme (a = 2, b = 8) | Inversa: X = a + (b − a)·U | 5,002 / 5 | 2,98 / 3 | KS 0,006 ✓ |
| Exponencial (λ = 1,5) | Inversa: X = −ln(1 − U)/λ | 0,670 / 0,667 | 0,435 / 0,444 | KS 0,010 ✓ |
| Gamma/Erlang (k = 3, λ = 1,2) | Suma de k exponenciales | 2,488 / 2,5 | 2,061 / 2,083 | KS 0,010 ✓ |
| Normal (μ = 10, σ = 2) | Box-Muller | 10,028 / 10 | 3,996 / 4 | KS 0,010 ✓ |
| Pascal (r = 4, p = 0,35) | Bernoulli hasta r éxitos, cuenta fallas | 7,423 / 7,429 | 20,91 / 21,22 | χ² 31,2 < 40,1 ✓ |
| Binomial (m = 12, p = 0,4) | Cuenta éxitos en m Bernoulli | 4,772 / 4,8 | 2,839 / 2,88 | χ² 8,8 < 18,3 ✓ |
| Hipergeométrica (N = 50, K = 18, n = 10) | Extracción sin reemplazo | 3,604 / 3,6 | 1,902 / 1,881 | χ² 4,7 < 15,5 ✓ |
| Poisson (λ = 4) | Multiplicativo: producto de U hasta < e^(−λ) | 4,005 / 4 | 3,976 / 4 | χ² 13,1 < 21,0 ✓ |
| Empírica (1…5 con 0,10/0,20/0,35/0,25/0,10) | Inversa discreta con acumuladas | 3,056 / 3,05 | 1,245 / 1,248 | χ² 2,6 < 9,5 ✓ |

**Resultado:** las nueve pasan. Las medias quedan a menos del 1 % de la teórica y las varianzas a menos del 2,5 %; la mayor diferencia es la de la exponencial.

**Qué mostrar:** una continua (la normal por Box-Muller) y el método de cada distribución. La idea fuerte es que **no hay un único método**; cada distribución pide el suyo:

- **Inversa:** cuando F tiene inversa cerrada (uniforme, exponencial, empírica).
- **Suma de exponenciales:** para la gamma con k entero (Erlang), porque su F no se invierte en forma cerrada.
- **Box-Muller:** para la normal, porque Φ no tiene inversa elemental. Dos uniformes dan dos normales independientes.
- **Simular el experimento:** para Pascal, binomial e hipergeométrica, con ensayos de Bernoulli con o sin reemplazo.
- **Método multiplicativo:** para Poisson. Cuenta cuántos arribos de un proceso de Poisson caen en un intervalo de largo 1; multiplicar uniformes equivale a sumar −ln U, que son tiempos exponenciales.

Esto es la Unidad 7.6–7.7 de la wiki (Naylor cap. 4).

**Ojo (consigna):** la tabla guía pedía el **método de rechazo** para la uniforme, la exponencial y la normal. El informe lo explica en general (sección 2.1), pero no lo aplica a ninguna de las tres. Es la diferencia más visible con la consigna. Si preguntan:

- Se priorizaron los métodos directos, que son más simples y no descartan números.
- Cómo sería con rechazo para una densidad acotada en (a, b): se sortea x = a + (b − a)·U₁ y se acepta si U₂ ≤ f(x)/máx f; si no, se repite. Para la exponencial y la normal hay que truncar el soporte, porque no es acotado. Es la Unidad 7.6 B de la wiki.

Lo demás se cumplió, y con más de lo pedido: se testearon las nueve y el código de las nueve está en el informe.

**Ojo:** la fuente uniforme es `random.random()` y no el GCL del TP 2.1. Es defendible, porque el 2.1 mostró que los dos pasan los tests, pero conviene tener la respuesta pensada.

## Preguntas de parcial y de práctica sobre este tema

**1.14** (parcial 2025) **¿Propósito principal de los números aleatorios?**
✅ **E**, todas. Generan variables con distribuciones arbitrarias, porque toda VA sale de una $U(0,1)$ transformada. Simulan las ocurrencias del modelo probabilístico. Y son la base de cualquier estudio de simulación estocástica.
*Unidad 7.*

**2.9** (parcial 2025) **Sobre los números pseudoaleatorios… (puede haber más de una correcta)**
- A) se generan secuencialmente con un algoritmo determinístico → ✅ **V**
- B) "ciclo completo" es cuando repite siempre el mismo número tras generar muchos distintos → ❌ **F**. El **período completo** es $p=m$: el generador recorre **todos** los valores posibles antes de repetir. Lo que describe la opción es una **degeneración**, como el cero que se propaga en el método de los cuadrados centrales.
- C) el método de la parte media del cuadrado sigue vigente → ❌ **F**. Cae en ciclos cortos y en cero, y no cumple uniformidad ni independencia. Es histórico.
- D) se pueden generar con cualquier computadora a altas velocidades → ✅ **V**. Velocidad y poco almacenamiento son propiedades de un buen generador.

**Clave: A y D.** El alumno marcó A, B y C: dos de más y una de menos.
*Unidad 7, §7.1 a §7.4.*

**2.10** (parcial 2025) **Verdaderos números aleatorios.**
- A) en simulaciones de alto rendimiento es preferible usar verdaderos aleatorios y no pseudoaleatorios → ❌ **F**. Los verdaderos son **lentos, caros y no reproducibles**. Para simular se prefieren los pseudoaleatorios: rápidos y **reproducibles** con la misma semilla, que es lo que permite comparar escenarios.
- B) se basan en una fuente física de aleatoriedad, cuántica o caótica → ✅ **V**, textual de la Unidad 7.

**Clave: B.**

**2b.1** (parcial real, otra fecha) **¿Cuáles son algunas características de los generadores aleatorios verdaderos?**
A) solo generan conjuntos finitos · B) en general son menos prácticos que otros generadores · C) el tiempo de generación importa más que la calidad · D) están basados en algoritmos procesados en computadoras
✅ **B** (ellos: B). Son caros, lentos y no reproducibles. D describe a los **pseudo**aleatorios.

**2b.3** (parcial real, otra fecha) **¿Cuáles son los *tipos* de pruebas de aleatoriedad?**
A) empíricas · B) póker · C) bondad de ajuste · D) tests de Cooper · E) subidas y bajadas · F) teóricas · G) prueba de espera
✅ **A y F** (ellos: A y F). Law §7.4 dice que hay **dos tipos**:
- **Empíricas**: se aplican sobre los $U_i$ generados (chi-cuadrado, series, corridas, Kolmogórov-Smirnov).
- **Teóricas**: se aplican sobre los **parámetros** del generador, sin generar ningún número.
Póker, corridas o espera son **pruebas**, no tipos.

**2b.5** (parcial real, otra fecha) **V/F: hacer tests sobre los valores de un generador pseudoaleatorio es obligatorio antes de usarlo en simulación.** → ✅ **V** (ellos: V)
Los generadores básicos caen en patrones o ciclos. Por eso existen los tests, y la pregunta frecuente #2 apunta a lo mismo.

**2b.6** (parcial real, otra fecha) **V/F: se espera que los números pseudoaleatorios tengan un "comportamiento" similar al de los aleatorios verdaderos.** → ✅ **V**
Es el objetivo: que imiten las propiedades estadísticas de una muestra i.i.d. $U(0,1)$.

**E1** (pregunta inventada por alumnos de 2025) El **Mersenne Twister** se destaca porque: A) período extremadamente largo · B) lo diseñó von Neumann en 1946 · C) es más lento que los GCL · D) está implementado en Python, R y Excel

→ Respuesta: **A y D**. Es de 1997, de Matsumoto y Nishimura

**E2** (pregunta inventada por alumnos de 2025) Característica deseable de un generador: A) período corto · B) patrones claros para depurar · C) alta velocidad · D) no reproducible

→ Respuesta: **C**

**E3** (pregunta inventada por alumnos de 2025) ¿Qué problema tenía **RANDU**? A) ceros perpetuos · B) las ternas caían en pocos planos · C) período infinito pero lento · D) no reproducible

→ Respuesta: **B**. A es el defecto de la parte media del cuadrado

**E4** (pregunta inventada por alumnos de 2025) El **método de rechazo** se usa cuando: A) la inversa de la FDA no tiene forma cerrada · B) la densidad es uniforme · C) se quiere reducir el cómputo · D) todas

→ Respuesta: **A**

**E5** (pregunta inventada por alumnos de 2025) El **método de composición**: A) usa trigonometría · B) combina distribuciones simples para formar una más compleja · C) es la transformada inversa · D) solo para exponenciales

→ Respuesta: **B**

**E8** (pregunta inventada por alumnos de 2025) La **normal** se genera con: A) transformada inversa · B) Box-Muller · C) TCL (sumar uniformes) · D) rechazo

→ Respuesta: ⚠️ Los alumnos ponían **B y C**. **También D es válida**: Ross genera la normal por rechazo con una exponencial. La A **no**, porque $\Phi$ no tiene inversa cerrada. Si es de opción única, B

**E14** (pregunta inventada por alumnos de 2025) Ventaja de los pseudoaleatorios frente a los verdaderos: A) más realistas · B) reproducibles y eficientes · C) no requieren semilla · D) nunca muestran patrones

→ Respuesta: **B**

**E16** (pregunta inventada por alumnos de 2025) Un buen generador es: A) lento y preciso · B) rápido, reproducible y con buen comportamiento estadístico · C) basado en fenómenos físicos · D) de período corto

→ Respuesta: **B**

**E17** (pregunta inventada por alumnos de 2025) Característica de los **verdaderamente** aleatorios: A) algoritmos determinísticos · B) reproducibles con semilla · C) basados en fenómenos físicos como los cuánticos · D) ciclos cortos

→ Respuesta: **C**

**E18** (pregunta inventada por alumnos de 2025) ¿Qué condición **NO** es necesaria para el período completo de un GCL mixto? A) $m$ y $c$ primos relativos · B) $a-1$ divisible por todos los primos que dividen a $m$ · C) si 4 divide a $m$, 4 divide a $a-1$ · D) el multiplicador debe ser primo

→ Respuesta: **D**. Ojo: el resumen redacta mal la B, al revés. Lo correcto es "**todo primo que divide a $m$ divide a $a-1$**"

**E19** (pregunta inventada por alumnos de 2025) La **transformada inversa** se usa cuando: A) la inversa de la FDA es fácil de obtener · B) no hay inversa cerrada · C) se mezclan distribuciones · D) se aceptan o rechazan candidatos

→ Respuesta: **A**. B lleva a rechazo, C es composición y D es rechazo

**P24** (práctica, no oficial) ¿Qué es la **semilla** de un generador pseudoaleatorio? A) el valor inicial que determina toda la sucesión · B) el módulo $m$ · C) el período · D) un número verdaderamente aleatorio obligatorio · E) A y D

→ Respuesta: **A**.

**P25** (práctica, no oficial) Un GCL mixto $Z_i=(aZ_{i-1}+c) \bmod m$ tiene período completo si: A) $m$ y $c$ son primos relativos · B) todo primo que divide a $m$ divide a $a-1$ · C) si 4 divide a $m$, 4 divide a $a-1$ · D) solo si $c=0$ · E) A, B y C a la vez

→ Respuesta: **E**. Teorema de Hull–Dobell: tienen que cumplirse las tres.
