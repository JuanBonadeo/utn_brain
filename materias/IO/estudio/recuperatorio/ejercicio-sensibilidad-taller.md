# Ejercicio de sensibilidad — el taller de muebles

Un taller fabrica **escritorios** y **estantes**. Cada escritorio deja una ganancia de \$ 40 y cada estante, \$ 30.

- **Armado:** un escritorio lleva 1 hora y un estante, 1 hora. Hay **40 horas** por semana.
- **Lijado:** un escritorio lleva 2 horas y un estante, 1 hora. Hay **60 horas** por semana.
- **Contrato:** el taller tiene que entregar **al menos 10 escritorios** por semana.

## El modelo

$x_1$: cantidad de escritorios a fabricar por semana. $x_2$: cantidad de estantes a fabricar por semana.

$$\text{Max } z = 40x_1 + 30x_2 \quad \text{s.a.} \quad
\begin{cases}
① \;\; x_1 + x_2 \leq 40 & \text{(horas de armado)}\\
② \;\; 2x_1 + x_2 \leq 60 & \text{(horas de lijado)}\\
③ \;\; x_1 \geq 10 & \text{(contrato mínimo)}\\
x_1, x_2 \geq 0
\end{cases}$$

En forma estándar con Gran M: $x_3$ es la holgura de ①, $x_4$ la holgura de ②, $x_5$ el exceso de ③ y $x_6$ la ficticia de ③.

$$\text{Max } z = 40x_1 + 30x_2 + 0x_3 + 0x_4 + 0x_5 - Mx_6$$

## La tabla óptima

| $c_i$ | Base | $A_1$ (40) | $A_2$ (30) | $A_3$ (0) | $A_4$ (0) | $A_5$ (0) | $A_6$ ($-M$) | $X$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 30 | $A_2$ | 0 | 1 | 2 | −1 | 0 | 0 | **20** |
| 0 | $A_5$ | 0 | 0 | −1 | 1 | 1 | −1 | **10** |
| 40 | $A_1$ | 1 | 0 | −1 | 1 | 0 | 0 | **20** |
| | $z_j$ | 40 | 30 | 20 | 10 | 0 | 0 | **1400** |
| | $c_j - z_j$ | 0 | 0 | −20 | −10 | 0 | $-M$ | |

Entre paréntesis, al lado de cada columna, va su $c_j$. Solución óptima: $S^* = (20;\ 20;\ 0;\ 0;\ 10)$, $z^* = 1400$.

## Consignas

### Coeficientes del funcional

**a)** Hallá el **rango de $c_2$** (ganancia del estante) en el que el plan óptimo no cambia. Interpretalo en una frase.

**b)** Si el estante pasa a dejar **\$ 45**, ¿sigue siendo óptimo el plan? Si no, ¿qué variable entraría a la base y qué significaría eso en el taller?

### Valores implícitos

**c)** Indicá el **valor implícito** de cada una de las tres restricciones, dónde lo leés en la tabla e interpretá cada uno. Explicá por qué el del contrato da lo que da.

### Términos independientes

**d)** Hallá el **rango de $b_1$** (horas de armado) en el que la base sigue siendo óptima. ¿Qué te dice sobre el valor implícito de la c)?

**e)** Un proveedor ofrece **5 horas extra de lijado a \$ 8 cada una**. ¿Conviene aceptarlas?

- Justificá con el valor implícito.
- Verificá que 65 horas estén dentro del rango de $b_2$.
- Calculá el nuevo plan $(x_1, x_2)$ y la nueva ganancia.

**f)** Hallá el **rango de $b_3$** (el contrato). ¿Hasta cuántos escritorios podría exigir el cliente sin que cambie la base?

### Bonus

**g)** El taller evalúa fabricar **mesas de luz**: cada una usa 1 hora de armado y 1 de lijado, y deja \$ 25. ¿Conviene? Usá los valores implícitos (resumen, §5.4).

## Dónde se lee cada cosa

| Qué | Dónde |
|---|---|
| Rango de un $c_k$ de una básica | **Fila** de $x_k$, en las columnas no básicas (sin la ficticia) |
| Rango de un $b_k$ | **Columna** de $B^{-1}$: la que en la tabla inicial tenía el 1 en la fila $k$ ($A_3$, $A_4$ o $A_6$) |
| Valor implícito $u_k$ | Fila $z_j$, en esa misma columna |
