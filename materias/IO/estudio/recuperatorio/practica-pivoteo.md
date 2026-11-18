# Práctica de pivoteo del simplex

> Cuatro ejercicios para practicar **sólo el paso que cuesta**: armar la tabla nueva. En cada uno ya te dicen quién entra, quién sale y cuál es el pivote. Armá la tabla nueva (filas, $z_j$ y $c_j - z_j$) y decí si es óptima. Las soluciones están en la última página: no las mires antes.

## Las dos formas de pivotear

**Por filas.**

1. La fila del pivote se divide por el pivote: $F_r' = F_r / y_{rk}$. Pasa a ser la fila de la variable que entra, con su $c_i$.
2. A cada otra fila se le resta su número en la columna que entra, multiplicado por la fila nueva: $F_i' = F_i - y_{ik}\,F_r'$.

**Por el rectángulo** (siempre sobre la tabla **vieja**):

$$\text{nuevo} = \text{viejo} - \frac{a \cdot b}{\text{pivote}}$$

donde $a$ es el número de **su fila** en la columna del pivote y $b$ el número de **su columna** en la fila del pivote.

**Atajos:** si la fila del pivote tiene 0 en una columna, esa columna no cambia en las otras filas. Si una fila tiene 0 en la columna que entra, esa fila queda igual. La columna que entra queda con 1 en la fila del pivote y 0 en las demás.

**Controles al terminar:** las columnas de las básicas forman la identidad; la columna $X$ es toda $\geq 0$; las básicas tienen $c_j - z_j = 0$.

## Ejercicio 1 — pivote 1 (la alfarería, primera iteración)

$\text{Max } z = 20x_1 + 45x_2$. Entra $A_2$, sale $A_5$, pivote = 1 (fila $A_5$).

| $c_i$ | Base | $A_1$ (20) | $A_2$ (45) | $A_3$ (0) | $A_4$ (0) | $A_5$ (0) | $X$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | $A_3$ | 1 | 2 | 1 | 0 | 0 | 40 |
| 0 | $A_4$ | 3 | 1,5 | 0 | 1 | 0 | 75 |
| 0 | $A_5$ | 0 | **1** | 0 | 0 | 1 | 15 |

## Ejercicio 2 — pivote 1/2 (el taller, última iteración)

$\text{Max } z = 40x_1 + 30x_2$, con ficticia $x_6$ ($-M$). Entra $A_2$, sale $A_3$, pivote = 1/2 (fila $A_3$).

| $c_i$ | Base | $A_1$ (40) | $A_2$ (30) | $A_3$ (0) | $A_4$ (0) | $A_5$ (0) | $A_6$ ($-M$) | $X$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | $A_3$ | 0 | **1/2** | 1 | −1/2 | 0 | 0 | 10 |
| 0 | $A_5$ | 0 | 1/2 | 0 | 1/2 | 1 | −1 | 20 |
| 40 | $A_1$ | 1 | 1/2 | 0 | 1/2 | 0 | 0 | 30 |

## Ejercicio 3 — pivote 3/5 (la fábrica de alimentos, de la variante 1)

$\text{Max } Z = 40x_1 + 85x_2 + 80x_3$, con ficticia $x_7$ ($-M$). Entra $A_2$, sale $A_1$, pivote = 3/5 (fila $A_1$). Es la que te costó: hacela de nuevo sin mirar.

| $c_i$ | Base | $A_1$ (40) | $A_2$ (85) | $A_3$ (80) | $A_4$ (0) | $A_5$ (0) | $A_6$ (0) | $A_7$ ($-M$) | $X$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 40 | $A_1$ | 1 | **3/5** | 0 | 2/5 | −4/5 | 0 | 0 | 1840 |
| 80 | $A_3$ | 0 | 1/5 | 1 | −1/5 | 12/5 | 0 | 0 | 2480 |
| 0 | $A_6$ | 0 | 1/5 | 0 | −1/5 | 12/5 | 1 | −1 | 2230 |

## Ejercicio 4 — pivote 2, en un Min con M (las dos plantas, primera iteración)

$\text{Min } w = 3x_1 + 2x_2$, con ficticias $x_6$ y $x_7$ ($+M$). Entra $A_1$, sale $A_6$, pivote = 2 (fila $A_6$). Ojo: los $z_j$ quedan con $M$, y en Min la tabla es óptima cuando todos los $c_j - z_j \geq 0$.

| $c_i$ | Base | $A_1$ (3) | $A_2$ (2) | $A_3$ (0) | $A_4$ (0) | $A_5$ (0) | $A_6$ ($M$) | $A_7$ ($M$) | $X$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $M$ | $A_6$ | **2** | 1 | −1 | 0 | 0 | 1 | 0 | 12 |
| $M$ | $A_7$ | 1 | 1 | 0 | −1 | 0 | 0 | 1 | 8 |
| 0 | $A_5$ | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 6 |

<div style="page-break-before: always"></div>

## Soluciones

**Ejercicio 1.** Fila del pivote ÷ 1 (queda igual, ahora es $A_2$ con $c_i = 45$). $A_3 - 2 \cdot A_2'$; $A_4 - 1{,}5 \cdot A_2'$.

| $c_i$ | Base | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $X$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | $A_3$ | 1 | 0 | 1 | 0 | −2 | 10 |
| 0 | $A_4$ | 3 | 0 | 0 | 1 | −1,5 | 52,5 |
| 45 | $A_2$ | 0 | 1 | 0 | 0 | 1 | 15 |
| | $z_j$ | 0 | 45 | 0 | 0 | 45 | 675 |
| | $c_j - z_j$ | 20 | 0 | 0 | 0 | −45 | |

No es óptima: $c_1 - z_1 = 20 > 0$, entra $A_1$ (θ: 10/1 = 10, 52,5/3 = 17,5 → sale $A_3$).

**Ejercicio 2.** Fila del pivote ÷ 1/2 (× 2), ahora $A_2$ con $c_i = 30$. $A_5 - \tfrac12 A_2'$; $A_1 - \tfrac12 A_2'$.

| $c_i$ | Base | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $X$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 30 | $A_2$ | 0 | 1 | 2 | −1 | 0 | 0 | 20 |
| 0 | $A_5$ | 0 | 0 | −1 | 1 | 1 | −1 | 10 |
| 40 | $A_1$ | 1 | 0 | −1 | 1 | 0 | 0 | 20 |
| | $z_j$ | 40 | 30 | 20 | 10 | 0 | 0 | 1400 |
| | $c_j - z_j$ | 0 | 0 | −20 | −10 | 0 | $-M$ | |

Es óptima: todos los $c_j - z_j \leq 0$.

**Ejercicio 3.** Fila del pivote × 5/3, ahora $A_2$ con $c_i = 85$. $A_3 - \tfrac15 A_2'$; $A_6 - \tfrac15 A_2'$.

| $c_i$ | Base | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $X$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 85 | $A_2$ | 5/3 | 1 | 0 | 2/3 | −4/3 | 0 | 0 | 3066,67 |
| 80 | $A_3$ | −1/3 | 0 | 1 | −1/3 | 8/3 | 0 | 0 | 1866,67 |
| 0 | $A_6$ | −1/3 | 0 | 0 | −1/3 | 8/3 | 1 | −1 | 1616,67 |
| | $z_j$ | 115 | 85 | 80 | 30 | 100 | 0 | 0 | 410.000 |
| | $c_j - z_j$ | −75 | 0 | 0 | −30 | −100 | 0 | $-M$ | |

Es óptima. Por el rectángulo, por ejemplo $A_3$/$A_5$: $12/5 - (1/5 \cdot (-4/5))/(3/5) = 12/5 + 4/15 = 8/3$.

**Ejercicio 4.** Fila del pivote ÷ 2, ahora $A_1$ con $c_i = 3$. $A_7 - 1 \cdot A_1'$; $A_5$ queda igual (tiene 0 en $A_1$).

| $c_i$ | Base | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $X$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | $A_1$ | 1 | 1/2 | −1/2 | 0 | 0 | 1/2 | 0 | 6 |
| $M$ | $A_7$ | 0 | 1/2 | 1/2 | −1 | 0 | −1/2 | 1 | 2 |
| 0 | $A_5$ | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 6 |
| | $z_j$ | 3 | $3/2 + M/2$ | $-3/2 + M/2$ | $-M$ | 0 | $3/2 - M/2$ | $M$ | $18 + 2M$ |
| | $c_j - z_j$ | 0 | $1/2 - M/2$ | $3/2 - M/2$ | $M$ | 0 | $3M/2 - 3/2$ | 0 | |

No es óptima (en Min hay negativos). $A_2$ y $A_3$ empatan en $-M/2$: decide el número suelto, $1/2 < 3/2$, así que entra $A_2$ (θ: 6/(1/2) = 12, 2/(1/2) = 4, 6/1 = 6 → sale $A_7$).
