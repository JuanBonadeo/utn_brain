# IO — Teoría: análisis de sensibilidad, dualidad y parametrización

Fundamentos necesarios para la **Práctica 4**. Reconstruido de los capítulos 4 y 5 del
apunte (`PLC4.pdf`, `PLC5.pdf`, Torrent) más el `resumen-primer-parcial.docx`, con el
**Ejemplo 1-1 del apunte (el taller de alfarería) como hilo conductor de punta a punta**.
Todos los números están verificados por cálculo exacto con fracciones.

Ver también: [[practica-4-sensibilidad-dualidad]] (los ejercicios resueltos) y las
Unidades 4 y 5 de `IO.md`.

---

## Índice

0. [El mapa: qué son estas tres cosas](#parte-0--el-mapa)
1. [La tabla óptima *es* $B^{-1}$](#parte-1--la-tabla-óptima-es-b-1)
2. [Dualidad](#parte-2--dualidad)
3. [Los cinco casos de sensibilidad](#parte-3--los-cinco-casos-de-sensibilidad)
4. [Parametrización](#parte-4--parametrización)
5. [Simplex dual](#parte-5--simplex-dual)
6. [Qué ejercicio de la Práctica 4 usa qué](#parte-6--mapa-de-la-práctica-4)

---

# Parte 0 — El mapa

## El problema que resuelven las Unidades 4 y 5

Con el Simplex ya sabés resolver un programa lineal. Te da un plan óptimo y un número.
Pero ese resultado se apoya en **datos que son estimaciones**: el precio de venta, las
horas disponibles, cuánto insume cada producto. Ninguno de esos números es sagrado.

Entonces aparecen las preguntas que le importan al que decide de verdad:

- Si el precio del producto 1 baja \$3, ¿cambio el plan de producción o sigo igual?
- Me ofrecen horas extra de mano de obra. **¿Cuánto me conviene pagar por hora?**
- Consigo 10 kg más de materia prima. ¿Cuánto gano con eso?
- Apareció un producto nuevo. ¿Lo fabrico?
- El sindicato me impone una restricción nueva. ¿Se me cae el plan?

Podrías contestar todas volviendo a correr el Simplex desde cero cada vez. Pero es caro,
y sobre todo **no te dice hasta dónde podés moverte**: te da un punto, no un rango. El
análisis de sensibilidad contesta todo eso **leyendo la tabla óptima que ya tenés**.

## Las tres palabras del título de la práctica

| Nombre | Qué pregunta contesta | Herramienta |
|---|---|---|
| **Análisis de sensibilidad** | Cambio *un* dato una vez. ¿Qué pasa, y hasta dónde puedo cambiarlo sin que se rompa nada? | $B^{-1}$ |
| **Dualidad** | ¿Cuánto vale cada recurso? ¿Por qué este producto no entra en el plan? | El programa dual |
| **Parametrización** | Un dato varía **de forma continua** en todo un intervalo. ¿Cómo va cambiando el óptimo a lo largo de ese recorrido? | Sensibilidad, repetida |

No son tres temas sueltos: son **capas**. Sensibilidad es un caso discreto; parametrización
es el mismo análisis pero barriendo todo un rango; dualidad es la interpretación económica
que le da sentido a los números que aparecen en las dos.

## El orden en que se entienden

```
   1. Qué es realmente la tabla óptima  (todo es B^-1)
                    |
                    v
   2. Dualidad: los precios sombra y por qué existen
                    |
                    v
   3. Los 5 casos de sensibilidad  (salen solos de 1 y 2)
                    |
                    v
   4. Parametrización  (repetir 3 en un intervalo)
                    |
                    v
   5. Simplex dual  (cómo se arregla la tabla cuando se rompe)
```

Saltarse el paso 1 es lo que hace que todo esto parezca un recetario de fórmulas
arbitrarias. No lo es: hay **una sola idea** y cinco consecuencias.

## El ejemplo que usamos en todo el documento

El taller de alfarería (Ejemplo 1-1 del apunte, el mismo de la Unidad 1):

$$
\begin{aligned}
\text{Max } z = 20x_1 &+ 45x_2 && \text{(contribución marginal, \$)}\\
x_1 + 2x_2 &\leq 40 && \text{(horas de mano de obra disponibles)}\\
3x_1 + 1{,}5x_2 &\leq 75 && \text{(kg de arcilla disponibles)}\\
x_2 &\leq 15 && \text{(demanda máxima de cántaros)}\\
x_1, x_2 &\geq 0
\end{aligned}
$$

$x_1$ = vasijas por día, $x_2$ = cántaros por día. Forma estándar con holguras
$x_3, x_4, x_5$ (una por restricción, en orden). Tabla óptima:

```
              20    45     0     0     0
  cB   base   A1    A2    A3    A4    A5      X
  ----------------------------------------------
  20   A1      1     0     1     0    -2     10
   0   A4      0     0    -3     1   9/2   45/2
  45   A2      0     1     0     0     1     15
  ----------------------------------------------
       zj     20    45    20     0     5   z=875
       cj-zj   0     0   -20     0    -5
```

Se lee: **10 vasijas y 15 cántaros por día, \$875 de contribución**. Sobran $22{,}5$ kg de
arcilla ($x_4 = 45/2$). La mano de obra y la demanda están al límite ($x_3 = x_5 = 0$).

---

# Parte 1 — La tabla óptima *es* $B^{-1}$

## La idea, en una frase

> **Toda la tabla final del Simplex es la matriz $B^{-1}$ multiplicada por los datos
> originales del problema.** Nada más.

Esa es la única idea de la Unidad 4. Todo lo demás es aplicarla.

## Cómo llegar a eso

Partimos del programa en forma estándar: $\text{Max } z = cx$ sujeto a $Ax = b$, $x \geq 0$.

Elegir una **base** es elegir $m$ columnas de $A$ (una por restricción) y armar con ellas
una matriz cuadrada $B$. Las variables de esas columnas son las básicas; las demás valen
cero. Partimos el sistema en básicas y no básicas:

$$
Ax = b \;\Longrightarrow\; Bx_B + Nx_N = b
$$

Como las no básicas valen cero ($x_N = 0$), queda $Bx_B = b$, y despejando:

$$
\boxed{\;x_B = B^{-1}b\;}
$$

**Ahí está todo.** Resolver un LP no es más que elegir bien qué columnas van a $B$ y hacer
esa multiplicación. El Simplex es un procedimiento para elegir esas columnas probando
vértices; una vez elegidas, la solución sale de una cuenta de matrices.

Y si multiplicás **todo** el sistema por $B^{-1}$ para dejarlo en función de las básicas:

| Objeto | Fórmula | Qué es en la tabla |
|---|---|---|
| Valores de las básicas | $x_B = B^{-1}b$ | la columna $X$ |
| Columna de la variable $j$ | $Y_j = B^{-1}A_j$ | el cuerpo de la tabla |
| Valor implícito de cada restricción | $u = c_B B^{-1}$ | los $z_j$ bajo las holguras |
| Costo de sustitución de $x_j$ | $z_j = c_B Y_j$ | la fila $z_j$ |
| Funcional | $z^* = c_B x_B$ | la esquina |

Todo con la misma $B^{-1}$ adelante. **Cambiar un dato del problema es cambiar lo que va a
la derecha de $B^{-1}$, y volver a multiplicar.** Eso es el análisis de sensibilidad
entero.

## Dónde está $B^{-1}$, sin calcularla

No hace falta invertir nada a mano. En la tabla inicial, las columnas de las holguras
forman la identidad:

$$
A_3 = \begin{pmatrix}1\\0\\0\end{pmatrix}\quad
A_4 = \begin{pmatrix}0\\1\\0\end{pmatrix}\quad
A_5 = \begin{pmatrix}0\\0\\1\end{pmatrix}
$$

Y como la tabla final tiene $Y_j = B^{-1}A_j$ en cada columna, para esas tres:

$$
Y_3 = B^{-1}e_1,\quad Y_4 = B^{-1}e_2,\quad Y_5 = B^{-1}e_3
\;\Longrightarrow\;
(Y_3\,|\,Y_4\,|\,Y_5) = B^{-1}
$$

> **Las columnas de las holguras en la tabla final SON $B^{-1}$**, columna por columna, en
> el orden de las restricciones.

En la alfarería, leyendo las columnas $A_3, A_4, A_5$ de la tabla óptima:

$$
B^{-1} = \begin{pmatrix} 1 & 0 & -2 \\ -3 & 1 & 9/2 \\ 0 & 0 & 1 \end{pmatrix}
$$

Comprobación:

$$
x_B = B^{-1}b = \begin{pmatrix} 1 & 0 & -2 \\ -3 & 1 & 9/2 \\ 0 & 0 & 1 \end{pmatrix}
\begin{pmatrix} 40 \\ 75 \\ 15 \end{pmatrix}
= \begin{pmatrix} 40 - 30 \\ -120 + 75 + 67{,}5 \\ 15 \end{pmatrix}
= \begin{pmatrix} 10 \\ 22{,}5 \\ 15 \end{pmatrix}
$$

que son exactamente $x_1 = 10$, $x_4 = 22{,}5$, $x_2 = 15$ de la columna $X$. ✓

**Trampa: restricciones $\geq$ o $=$.** Ahí la columna que estaba en la identidad inicial
es la de la **ficticia**, no la de exceso. Se lee $B^{-1}$ bajo las **ficticias**. La
columna del exceso vale $-B^{-1}e_i$, o sea $B^{-1}$ con el signo cambiado.

## Por qué esto importa tanto

Fijate lo que se desbloquea con esta sola idea:

- Cambia $b_i$ → cambia el vector de la derecha → $x_B' = B^{-1}b'$. Se recalcula sin
  iterar nada.
- Cambia una columna $A_j$ o aparece una variable nueva → $Y_j = B^{-1}A_j$ con la $B^{-1}$
  que ya tengo.
- ¿Cuánto sube $z$ por unidad de recurso? → $z^* = c_B B^{-1} b$, o sea
  $\partial z^*/\partial b_i = (c_B B^{-1})_i$. **Los precios sombra son la derivada del
  óptimo respecto de cada $b_i$**, y ya están impresos en la tabla.

Todo el capítulo sale de acá.

## La única aclaración importante: "mientras la base no cambie"

$B^{-1}$ es la inversa de **esa** base, la del óptimo actual. Si el cambio es tan grande
que conviene otro vértice, la base cambia, $B^{-1}$ cambia, y todas las cuentas de arriba
dejan de valer.

Por eso cada caso de sensibilidad viene con un **rango de validez**. La pregunta nunca es
solo "¿qué pasa si...?" sino "**¿hasta dónde vale lo que acabo de decir?**".

Y hay dos cosas distintas que se pueden romper:

| | Qué significa | Qué la rompe |
|---|---|---|
| **Factibilidad** | $x_B \geq 0$: la solución existe físicamente (no hay producción negativa) | cambiar $b$ |
| **Optimalidad** | $c_j - z_j \leq 0\ \forall j$ (en Max): ninguna variable fuera de la base mejora $z$ | cambiar $c$ |

$$
\boxed{\;\text{tocar } c_j \to \text{rompe OPTIMALIDAD} \qquad
\text{tocar } b_i \to \text{rompe FACTIBILIDAD}\;}
$$

**Ese cuadrito es la mitad de la unidad.** Se ve directo en las fórmulas:
$c_j - z_j$ no contiene ninguna $b$, y $x_B = B^{-1}b$ no contiene ningún $c$.

De ahí salen las dos consecuencias que más se preguntan en el parcial:

- **Cambio un $c_j$ dentro de su rango** → el vértice óptimo **no se mueve** (mismo plan de
  producción). Solo cambia el valor de $z$, y **únicamente si la variable tocada es
  básica**: $z^{*\prime} = z^* + \Delta c_k\, x_k^*$. Si es no básica, $x_k = 0$ y $z$ ni
  se entera.
- **Cambio un $b_i$ dentro de su rango** → la **base** no cambia (siguen produciéndose los
  mismos artículos) pero los **valores sí se mueven**: $x_B' = x_B + \Delta b_i B^{-1}_{\cdot i}$,
  y $z^{*\prime} = z^* + u_i \Delta b_i$.

---

# Parte 2 — Dualidad

## De dónde sale la pregunta

Volvé al taller. El plan óptimo deja \$875 por día, y sobra arcilla. Preguntas naturales:

1. Si consigo **una hora más** de mano de obra, ¿cuánto gano? ¿Cuánto pago por ella?
2. Un kilo más de arcilla, ¿cuánto vale? (Intuición: **nada**, ya me sobra.)

Ese "cuánto vale al margen una unidad más de recurso" es el **valor implícito** o **precio
sombra** del recurso. Y la respuesta formal a esas preguntas es un segundo programa lineal.

## El truco para entenderlo: el seguro *(interpretación del apunte, PLC5 §5.6)*

Al dueño del taller le ofrecen un seguro que le paga si pierde recursos:

- $u_1$ = \$ que le pagan por cada **hora de mano de obra** perdida
- $u_2$ = \$ por cada **kg de arcilla** perdido
- $u_3$ = \$ por cada unidad de caída en la **demanda máxima**

**Qué quiere la aseguradora:** pagar lo menos posible en total. Tiene $40$ horas, $75$ kg y
$15$ de demanda a cubrir:

$$
\text{Min } w = 40u_1 + 75u_2 + 15u_3
$$

**Qué exige el alfarero:** que si le sacan los recursos para hacer una vasija, le paguen al
menos lo que la vasija le dejaba. Una vasija consume $1$ hora y $3$ kg, y deja \$20:

$$
1u_1 + 3u_2 \geq 20
$$

Un cántaro consume $2$ horas, $1{,}5$ kg y $1$ de demanda, y deja \$45:

$$
2u_1 + 1{,}5u_2 + 1u_3 \geq 45
$$

Juntando todo, **ese es el programa dual**:

$$
\begin{aligned}
\text{Min } w = 40u_1 &+ 75u_2 + 15u_3\\
u_1 + 3u_2 &\geq 20\\
2u_1 + 1{,}5u_2 + u_3 &\geq 45\\
u_1, u_2, u_3 &\geq 0
\end{aligned}
$$

No es una construcción arbitraria: es **el mismo problema real mirado desde el otro lado**.
El primal pregunta *"¿cuánto produzco de cada bien?"*; el dual pregunta *"¿cuánto vale cada
recurso?"*. Y valen lo mismo: $w^* = z^* = 875$.

## Cómo se construye el dual, mecánicamente

Con **primal de Max, todas las restricciones $\leq$, variables $\geq 0$** (forma canónica),
el dual es directo:

$$
\begin{array}{c|c}
\textbf{Primal (Max)} & \textbf{Dual (Min)}\\ \hline
\text{Max } z = cx & \text{Min } w = b^T u\\
Ax \leq b & A^T u \geq c^T\\
x \geq 0 & u \geq 0
\end{array}
$$

En criollo, la receta:

1. **Max se vuelve Min** (y $\leq$ se vuelve $\geq$).
2. **Cada restricción del primal se vuelve una variable del dual.** 3 restricciones → 3
   variables $u_1, u_2, u_3$.
3. **Cada variable del primal se vuelve una restricción del dual.** 2 variables → 2
   restricciones.
4. **Los $b_i$ pasan a ser los coeficientes del funcional dual.**
5. **Los $c_j$ pasan a ser los términos independientes de las restricciones duales.**
6. **La matriz $A$ se traspone**: la columna de $x_j$ en el primal es la fila $j$ del dual.

El dual del dual es el primal: la relación es simétrica, cualquiera de los dos puede
llamarse primal.

### Cuando el primal no está en forma canónica

| Primal (Max) | Dual (Min) |
|---|---|
| Restricción $\leq$ | Variable $u_i \geq 0$ |
| Restricción $\geq$ | Variable $u_i \leq 0$ |
| Restricción $=$ | Variable $u_i$ **libre** (sin restricción de signo) |
| Variable $x_j \geq 0$ | Restricción $\geq$ |
| Variable $x_j$ libre | Restricción $=$ |

**Alternativa equivalente:** multiplicar por $-1$ las restricciones $\geq$ para dejarlas
todas $\leq$ antes de dualizar; ahí todas las $u_i$ quedan $\geq 0$ y lo que cambia de
signo es el coeficiente en $w$. **Las dos convenciones son válidas — hay que elegir una y
sostenerla**, porque el signo de las duales depende de cuál usaste.

**Verificación obligatoria: $w^* = z^*$.** Si no da, el dual está mal planteado. Es el
chequeo más rápido que existe y caza casi todos los errores de signo.

## Teorema fundamental de la dualidad

> Si el primal tiene solución óptima finita, entonces el dual también, los valores
> óptimos de las $u_i$ **son los costos marginales del primal**, y $w^* = z^*$.

La demostración del apunte es la que ya vimos por otro lado: $z^* = c_B B^{-1} b$ es una
función lineal de $b$, y su derivada respecto de $b_i$ es $(c_B B^{-1})_i = u_i$.

$$
\boxed{\;u = c_B B^{-1}\;}
$$

Corolario práctico: **no hace falta resolver el dual.** Su solución óptima ya está en la
tabla del primal.

## Dónde se lee la solución del dual en la tabla del primal

Bajo las columnas de las **holguras**, en la fila $c_j - z_j$, cambiándole el signo:

$$
\text{Primal de MAX:}\quad u_i^* = -(c_j - z_j)\big|_{\text{holgura de la restr. } i} = z_j
$$

En la alfarería: $c_j - z_j$ vale $-20$, $0$ y $-5$ bajo $A_3, A_4, A_5$. Entonces

$$
u^* = (20,\ 0,\ 5)
$$

Verificación: $w^* = 40(20) + 75(0) + 15(5) = 800 + 75 = 875 = z^*$ ✓

Y si lo hacés por la fórmula: $u = c_B B^{-1} = (20, 0, 45) \cdot B^{-1} = (20, 0, 5)$. ✓

## Qué significa cada número

- **$u_1 = 20$ (mano de obra).** Recurso agotado ($x_3 = 0$). Una hora más de mano de obra
  hace subir la contribución en **\$20**. Es lo máximo que conviene pagar por una hora
  extra: a \$18 la hora conviene contratar, a \$22 no. Comprobación directa: con $b_1 = 41$,
  $x_B = B^{-1}b' = (11;\ 19{,}5;\ 15)$ y $z = 20(11) + 45(15) = 895 = 875 + 20$. ✓
- **$u_2 = 0$ (arcilla).** Sobra ($x_4 = 22{,}5 > 0$). Un kilo más no sirve de nada: **no
  pagaría un centavo por él**. Y si alguien me ofrece comprarme arcilla, se la vendo a
  cualquier precio positivo.
- **$u_3 = 5$ (demanda).** Está en el límite. Si consigo vender un cántaro más de tope de
  demanda (por publicidad, por ejemplo), gano \$5. Conviene invertir en publicidad hasta
  \$5 por unidad adicional de demanda.

**El precio sombra no es el precio de mercado.** Es lo que ese recurso vale *para esta
empresa, con este plan de producción*. Sale del aprovechamiento que la organización hace
del recurso, no de lo que cuesta comprarlo.

## Holguras complementarias

Es la propiedad estructural que ordena toda la tabla:

$$
\boxed{\;x_{\text{holgura } i} \cdot u_i = 0 \qquad \text{y} \qquad x_j \cdot s_j = 0\;}
$$

donde $s_j$ es la holgura de la restricción dual $j$ (= el costo reducido de $x_j$).

En palabras:

- **Si sobra recurso, su precio sombra es cero.** (arcilla: $x_4 = 22{,}5$, $u_2 = 0$)
- **Si el precio sombra es positivo, el recurso está agotado.** (mano de obra: $u_1 = 20$,
  $x_3 = 0$)
- **Si un producto se fabrica ($x_j > 0$), su restricción dual se cumple con igualdad**:
  el valor de los recursos que consume iguala exactamente su contribución.
- **Si la restricción dual se cumple con desigualdad estricta, el producto no se fabrica**:
  los recursos que consumiría valen más de lo que el producto aporta.

Comprobación en la alfarería: se fabrican vasijas y cántaros, y las dos restricciones
duales cierran con igualdad: $u_1 + 3u_2 = 20 + 0 = 20$ ✓ y
$2u_1 + 1{,}5u_2 + u_3 = 40 + 0 + 5 = 45$ ✓.

> **Sirve como control de errores:** armá la tabla de correspondencias primal↔dual y fijate
> que en cada renglón **al menos uno de los dos lados sea cero**. Un renglón con los dos
> lados no nulos es un error de cálculo seguro.

| Primal | ↔ | Dual |
|---|---|---|
| holgura/exceso de la restricción $i$ | ↔ | variable $u_i$ |
| variable de decisión $x_j$ | ↔ | holgura de la restricción dual $j$ |

## La frase económica que hay que saber decir

> Siempre que una actividad opere a nivel estrictamente positivo, el costo marginal de los
> recursos que consume debe ser **igual** al beneficio que proviene de dicha actividad. De
> lo contrario, no conviene en absoluto iniciar la actividad. *(PLC5 §5.6)*

De acá sale el criterio para decidir si conviene un producto nuevo, sin tocar el Simplex:
comparar $\sum_i a_{ij}u_i$ (lo que "cuesta" en recursos escasos) contra $c_j$ (lo que
aporta). Si el costo implícito supera la contribución, no conviene.

## Costo reducido ≠ costo marginal

La confusión más frecuente de la unidad:

| | **Costo reducido** | **Costo marginal / precio sombra** |
|---|---|---|
| Se asocia a | una **variable** (una columna de decisión) | una **restricción** (un recurso) |
| Se lee en | $c_j - z_j$ de la columna de $x_j$ | $c_j - z_j$ de la columna de la **holgura** de esa restricción |
| Qué dice | cuánto hay que **mejorar $c_j$** para que $x_j$ tenga chance de entrar | cuánto **vale al margen** una unidad más del recurso |
| Vale 0 cuando | $x_j$ es **básica** (el producto se fabrica) | la restricción es **pasiva** (sobra recurso) |

---

# Parte 3 — Los cinco casos de sensibilidad

Los cinco salen de la Parte 1. **Hipótesis del método: los coeficientes varían de a uno por
vez**, todo lo demás fijo. (Para varios a la vez, ver la regla del 100% al final.)

## Cuadro maestro

| # | Cambia… | Rompe | Qué se revisa | Si el cambio entra en el rango |
|---|---|---|---|---|
| 1 | $c_k$ **no básica** | optimalidad | solo su $c_k - z_k$ | no cambia nada, ni $x^*$ ni $z^*$ |
| 1 | $c_k$ **básica** | optimalidad | **todos** los $c_j - z_j$ | $x^*$ igual; $z^{*\prime} = z^* + \Delta c_k x_k^*$ |
| 2 | $b_k$ | factibilidad | $x_B \geq 0$ | misma base; $x^*$ se mueve; $z^{*\prime} = z^* + u_k \Delta b_k$ |
| 3 | $a_{ij}$ de una **no básica** | optimalidad | $Y_k = B^{-1}A_k'$, luego $c_k - z_k$ | sigue óptima |
| 4 | **nueva variable** | optimalidad | $Y_n = B^{-1}A_n$, luego $c_n - z_n$ | no conviene, óptimo intacto |
| 5 | **nueva restricción** | factibilidad | evaluar $x^*$ en la restricción | si la cumple, no pasa nada |

## Caso 1 — Cambia un coeficiente del funcional $c_k$

### 1.a — $x_k$ es NO básica

Como $c_B$ no cambia, ningún $z_j$ cambia. El único $c_j - z_j$ que se mueve es el de $x_k$:

$$
c_k + \Delta c_k - z_k \leq 0 \quad\Longrightarrow\quad \boxed{\Delta c_k \leq -(c_k - z_k)}
$$

$z^*$ **no cambia** en todo el rango, porque $x_k = 0$.

*Lectura:* $-(c_k - z_k)$ es **cuánto le falta a ese producto para volverse rentable**.

### 1.b — $x_k$ es BÁSICA

Ahora $c_B$ cambia, así que **todos** los $z_j = c_B Y_j$ se mueven. El que manda es la
**fila de $x_k$** en la tabla:

$$
(c_j - z_j)' = (c_j - z_j) - \Delta c_k\, y_{kj} \leq 0 \qquad \forall j \notin I_B
$$

Despejando según el signo de $y_{kj}$:

$$
\boxed{\;\max_{y_{kj} > 0} \frac{c_j - z_j}{y_{kj}} \;\leq\; \Delta c_k \;\leq\; \min_{y_{kj} < 0} \frac{c_j - z_j}{y_{kj}}\;}
$$

**Procedimiento:**
1. Recorrer la **fila** de $x_k$, anotando los $y_{kj}$ de las columnas **no básicas**.
2. Separar en $y_{kj} > 0$ y $y_{kj} < 0$ (los $y_{kj} = 0$ no restringen).
3. Calcular $\frac{c_j - z_j}{y_{kj}}$ en cada grupo.
4. **Máximo** entre los positivos = cota inferior. **Mínimo** entre los negativos = cota
   superior. Si un grupo está vacío, esa cota es infinita.

Dentro del rango, **$x^*$ no se mueve** y $z^{*\prime} = z^* + \Delta c_k x_k^*$.

**Ejemplo (alfarería, rango de $c_1$).** Fila de $A_1$, columnas no básicas $A_3$ y $A_5$:
$y_{13} = 1$, $y_{15} = -2$, con $c_j - z_j$ iguales a $-20$ y $-5$.

$$
\max\left(\tfrac{-20}{1}\right) = -20 \qquad \min\left(\tfrac{-5}{-2}\right) = 2{,}5
$$

$$
-20 \leq \Delta c_1 \leq 2{,}5 \quad\Longrightarrow\quad 0 \leq c_1 \leq 22{,}5
$$

Mientras la vasija deje entre \$0 y \$22,50, el plan sigue siendo 10 y 15.

> **Lectura gráfica:** cambiar $c_k$ hace girar la recta del funcional. El vértice óptimo no
> cambia mientras la pendiente del funcional quede **entre las pendientes de las dos
> restricciones que forman ese vértice**. Los extremos del rango son exactamente los valores
> donde el funcional se vuelve paralelo a una de las dos — que es el caso de **solución
> óptima alternativa**.

## Caso 2 — Cambia un término independiente $b_k$

Nada en $c_j - z_j$ depende de $b$: la tabla **sigue siendo óptima**. Lo que puede romperse
es que alguna básica se vuelva negativa:

$$
x_B' = x_B + \Delta b_k\, B^{-1}_{\cdot k} \geq 0
$$

Fila por fila, con $r_{ik}$ = elemento $i$ de la columna $k$ de $B^{-1}$:

$$
\boxed{\;\max_{r_{ik} > 0} \frac{-x_i^*}{r_{ik}} \;\leq\; \Delta b_k \;\leq\; \min_{r_{ik} < 0} \frac{-x_i^*}{r_{ik}}\;}
$$

Dentro del rango:

$$
x_i^{*\prime} = x_i^* + r_{ik}\,\Delta b_k \qquad\qquad z^{*\prime} = z^* + u_k\,\Delta b_k
$$

**Procedimiento:**
1. Anotar los $x_i^*$ actuales (columna $X$).
2. Tomar la **columna $k$ de $B^{-1}$** — la de la holgura de la restricción que se toca.
3. Calcular $-x_i^*/r_{ik}$ fila por fila; $r_{ik} = 0$ no restringe.
4. Máximo entre los de $r_{ik} > 0$, mínimo entre los de $r_{ik} < 0$.

**Ejemplo (alfarería, rango de $b_1$).** $x^* = (10;\ 22{,}5;\ 15)$ y la primera columna de
$B^{-1}$ es $(1;\ -3;\ 0)$:

$$
\frac{-10}{1} = -10 \qquad \frac{-22{,}5}{-3} = 7{,}5 \qquad \frac{-15}{0} = \text{no restringe}
$$

$$
-10 \leq \Delta b_1 \leq 7{,}5 \quad\Longrightarrow\quad 30 \leq b_1 \leq 47{,}5
$$

**Este rango es la letra chica del precio sombra.** $u_1 = 20$ vale mientras las horas estén
entre 30 y 47,5. Fuera de ahí, otro recurso pasa a ser el cuello de botella y el precio
sombra cambia. Por eso *"conviene pagar hasta \$20 la hora extra"* es correcto para las
primeras 7,5 horas, no para 100.

> **Lectura gráfica:** cambiar $b_k$ **desplaza paralelamente** esa restricción. El vértice
> óptimo se corre siguiendo las otras dos rectas que lo forman. El rango termina cuando el
> desplazamiento hace que ese vértice deje de ser factible.

> **Error del `resumen-primer-parcial.docx`:** la fórmula figura con `max` en los **dos**
> extremos. El extremo superior es un **mínimo**. En su ejemplo no se nota porque hay un
> solo $r_{ik}$ negativo.

## Caso 3 — Cambia un coeficiente tecnológico $a_{ij}$

Se estudia **solo para variables no básicas**. Si el coeficiente es de una básica, el cambio
afecta a $B$ misma, y por lo tanto a $B^{-1}$ y a toda la tabla: la solución puede volverse
inadmisible, no óptima o directamente no básica, y no hay atajo — se rehace.

Para $x_k$ no básica con nueva columna $A_k'$:

$$
Y_k' = B^{-1}A_k' \qquad z_k' = c_B Y_k' \qquad
\begin{cases}
c_k - z_k' \leq 0 & \text{sigue óptima, no cambia nada}\\
c_k - z_k' > 0 & x_k \text{ entra: se sigue iterando desde esta tabla}
\end{cases}
$$

Ojo con lo último: **no se rehace el problema.** Se mete la columna nueva en la tabla actual
y se itera desde ahí.

## Caso 4 — Se agrega una variable nueva

Idéntico al caso 3: es una columna que no está en la base. Con $A_n$ y $c_n$:

$$
Y_n = B^{-1}A_n \qquad z_n = c_B Y_n
$$

$$
c_n - z_n \begin{cases}
> 0 & \text{conviene: entra a la base, hay que seguir iterando}\\
= 0 & \text{no mejora, pero hay óptimo alternativo que la incluye}\\
< 0 & \text{no conviene: el óptimo actual no cambia}
\end{cases}
$$

**Atajo económico (es la misma cuenta):** $z_n = \sum_i a_{in} u_i$ es el valor implícito de
los recursos que consume una unidad del producto nuevo. Si eso supera a $c_n$, no conviene
— estarías desviando recursos escasos hacia algo que rinde menos.

> **Error del `resumen-primer-parcial.docx`:** concluye "$c_n - z_n = 0 \geq 0 \Rightarrow$
> entra en la base". Con $c_j - z_j = 0$ la variable **no mejora** el funcional: la solución
> actual sigue siendo óptima y lo que hay es un **óptimo alternativo**. El criterio de
> entrada es estrictamente $> 0$.

## Caso 5 — Se agrega una restricción nueva

Dos pasos, sin cuentas de matrices:

1. **Reemplazar el óptimo actual en la restricción nueva.**
2. Decidir:
   - **La cumple** → la restricción es **pasiva** (no corta nada donde importa). $S^*$ y
     $z^*$ **quedan igual**. No hay nada que hacer.
   - **No la cumple** → la restricción es **activa**: recorta el poliedro justo donde estaba
     el óptimo. $S^*$ **deja de ser factible** y hay que reoptimizar.

Cuando hay que reoptimizar: se agrega la fila con su holgura, se la barre para dejarla en
forma canónica respecto de las básicas actuales, y la tabla queda **óptima pero no
factible** ($c_j - z_j \leq 0$ con algún $x_B < 0$). Ese es exactamente el caso del
**Simplex dual** (Parte 5).

## Regla del 100% — cuando cambian varios a la vez

Todos los rangos de arriba valen **de a un cambio por vez**. Si se mueven dos o más
coeficientes simultáneamente, se calcula para cada uno **qué fracción de su rango
permitido consume**:

$$
r_k = \frac{|\Delta_k|}{|\text{variación máxima permitida en ese sentido}|}
$$

$$
\sum_k r_k \leq 100\% \;\Longrightarrow\; \text{la conclusión se mantiene (la base sigue óptima)}
$$

Si se pasa del 100%, la regla **no dice nada**: puede que siga valiendo o puede que no, hay
que recalcular. No es un criterio de rechazo.

Se aplica por separado a los $c_j$ (con sus rangos de optimalidad) y a los $b_i$ (con sus
rangos de factibilidad); **no se mezclan en una sola suma**.

---

# Parte 4 — Parametrización

## Qué agrega respecto de sensibilidad

Sensibilidad contesta *"¿qué pasa si $c_2$ pasa de 45 a 50?"* — un cambio puntual.

Parametrización contesta *"¿qué pasa con el óptimo cuando $c_2$ recorre **todo** el
intervalo de 0 a infinito?"*. La respuesta ya no es un número: es un **cuadro de tramos**,
donde cada tramo tiene su propia base óptima.

Se escribe el coeficiente como función de un parámetro $\lambda$, por ejemplo
$c_2(\lambda) = 45(1 + \lambda)$ o $b_2(\lambda) = 600 + \lambda$, y se barre $\lambda$.

## Procedimiento *(PLC4 §4.10)*

1. Obtener la tabla óptima para $\lambda = 0$.
2. Meter el $\lambda$ en la tabla y calcular el **intervalo de $\lambda$ que la mantiene
   óptima** — con las mismas fórmulas de la Parte 3.
3. En el extremo del intervalo, hacer **una iteración de Simplex** (entra la variable cuyo
   $c_j - z_j$ se hizo cero y está por volverse positiva) para pasar a la base siguiente.
4. Repetir 2 y 3 hasta cubrir todo el intervalo pedido.
5. Presentar el **cuadro final**: para cada tramo de $\lambda$, la base, $x^*$ y $z(\lambda)$.

## Las dos variantes

**Parametrizando $c_j$** (Ejercicio 9 de la práctica). Lo que cambia con $\lambda$ es la
fila $c_j - z_j$; la columna $X$ queda fija dentro de cada tramo. Los quiebres ocurren
cuando algún $c_j - z_j$ se anula. **En cada quiebre hay solución óptima alternativa** —
por eso el tramo de $\lambda$ es cerrado en los dos extremos y el óptimo "salta" de vértice.

**Parametrizando $b_i$** (Ejercicio 8). Lo que cambia es la columna $X = B^{-1}(b + \lambda e_i)$;
la fila $c_j - z_j$ queda fija. Los quiebres ocurren cuando alguna básica se anula y está
por hacerse negativa; ahí se cambia de base. **Como la tabla nunca deja de ser óptima, la
iteración correcta en el quiebre es de Simplex dual**, no de Simplex primal.

## Ejemplo (alfarería, $c_2 = 45(1+\lambda)$)

Metiendo $\lambda$ en la tabla, la fila $c_j - z_j$ queda $(0,\ 0,\ -20,\ 0,\ -5-45\lambda)$
y $z = 875 + 675\lambda$. La tabla sigue óptima mientras

$$
-5 - 45\lambda \leq 0 \;\Longleftrightarrow\; \lambda \geq -1/9
$$

Es decir: mientras $c_2 \geq 40$, el plan sigue siendo 10 vasijas y 15 cántaros. En
$\lambda = -1/9$ exacto hay **óptimo alternativo**; por debajo entra $A_5$, sale $A_4$, y
arranca el tramo siguiente con otro plan.

## Lectura gráfica

- Parametrizar $c_j$ = **girar** la recta del funcional de forma continua. Va tocando los
  vértices del polígono uno tras otro, y cada tramo de $\lambda$ es "el rango de pendientes
  para el que gana este vértice".
- Parametrizar $b_i$ = **desplazar** una restricción de forma continua. El vértice óptimo se
  desliza a lo largo de una arista; cuando llega a una esquina, cambia la base.

---

# Parte 5 — Simplex dual

## Para qué sirve

El Simplex normal arranca **factible pero no óptimo** y mantiene la factibilidad mientras
busca la optimalidad. El Simplex dual hace lo contrario: arranca **óptimo pero no factible**
($c_j - z_j \leq 0$ con alguna $x_B < 0$) y mantiene la optimalidad mientras busca la
factibilidad.

Es exactamente lo que necesitás cuando la sensibilidad te rompe la tabla:

- cambió un $b_i$ **fuera de rango** → alguna básica quedó negativa;
- se agregó una **restricción activa** → el óptimo dejó de ser factible.

Ventaja adicional: **no necesita variables ficticias**.

## Algoritmo *(PLC5 §5.8)*

1. Llevar todas las restricciones a $\leq$ y pasar a forma estándar, con una base inicial
   **inmejorable** ($c_j - z_j \leq 0\ \forall j$ para Max; $\geq 0$ para Min).
2. Si $x_i \geq 0$ para toda básica → **ya es la óptima**. Si no, seguir.
3. **Sale** la variable básica con el valor **más negativo**. Su fila es la fila pivote $r$.
   Empates: arbitrario.
4. **Entra** la variable $x_k$ que cumpla, mirando solo las columnas con $y_{rj} < 0$:

$$
\frac{c_k - z_k}{y_{rk}} = \min_j \left\{ \frac{c_j - z_j}{y_{rj}} \;:\; y_{rj} < 0 \right\}
$$

   Si **no hay ningún $y_{rj} < 0$** en la fila pivote → el problema es **no factible**.
5. Pivotear normalmente y volver al paso 2.

Comparación con el Simplex primal, para no confundirlos:

```
                       SIMPLEX PRIMAL              SIMPLEX DUAL
  arranca              factible, no optimo         optimo, no factible
  criterio de entrada  mejor cj-zj  (> 0)          cociente minimo sobre la fila
  criterio de salida   cociente minimo X/y         la basica mas negativa
  termina cuando       ya no hay cj-zj > 0         ya no hay xB < 0
  no acotado / infac.  no hay y > 0 en la columna  no hay y < 0 en la fila
```

---

# Parte 6 — Mapa de la Práctica 4

| Ej. | Qué es | Qué hay que dominar |
|---|---|---|
| 1 | Tabla de LINDO dada, 7 incisos de sensibilidad | Parte 1 entera + los 5 casos + regla del 100% |
| 2 | Editorial. Reconstruir la tabla final **sin iterar**, desde la base óptima conocida | $B^{-1}$ a mano, $x_B = B^{-1}b$, $Y = B^{-1}N$ |
| 3 | Gutchi (bolsos). Salida de LINDO con una restricción $\geq$ | Dualidad completa: plantear el dual, holguras complementarias, interpretar las cuatro familias de variables |
| 4 | Máquinas. Programa de **minimización** | Todo lo anterior con los signos dados vuelta; verificar la salida de sensibilidad de LINDO |
| 5 | Cuatro programas, construir el dual de cada uno | Tabla de reglas de construcción (con $=$, con $\geq$, con Min) |
| 6 | Tabla con incógnitas ($a, b, c, d, e, b_1, b_2$) | $x_B = B^{-1}b$ leído al revés + $u = c_B B^{-1}$ |
| 7 | Hallar precios sombra **sin resolver el Simplex** | Dualidad pura: resolver el dual, que tiene 2 variables → método gráfico |
| 8 | Paramétrico en $b_2$ | Parte 4, variante $b$ + Simplex dual |
| 9 | Paramétrico en $c_2$ | Parte 4, variante $c$ + interpretación gráfica |

**Traducción de la salida de LINDO**, que aparece en los ejercicios 1, 3 y 4:

| LINDO | Qué es |
|---|---|
| `SLK 2` | holgura de la **restricción 1** (LINDO cuenta el funcional como fila 1) |
| fila `ART` / fila `1)` | $z_j - c_j$, **no** $c_j - z_j$: hay que cambiarle el signo |
| `DUAL PRICES` | los $u_i$ (precios sombra), ya con el signo correcto |
| `REDUCED COST` | costo reducido de cada variable, en valor absoluto |
| `SLACK OR SURPLUS` | valor de la holgura/exceso de esa restricción |
