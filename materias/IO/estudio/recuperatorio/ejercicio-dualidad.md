# Ejercicio de dualidad

## Parte A — El dual de las dos plantas

Es el mismo problema del ejercicio completo: una empresa usa dos plantas para cumplir los pedidos de los productos P y Q al menor costo. Costos en miles de pesos.

$x_1$: horas de funcionamiento de la planta A por semana. $x_2$: horas de funcionamiento de la planta B por semana.

$$\text{Min } w = 3x_1 + 2x_2 \quad \text{s.a.} \quad
\begin{cases}
① \;\; 2x_1 + x_2 \geq 12 & \text{(toneladas de P exigidas)}\\
② \;\; x_1 + x_2 \geq 8 & \text{(toneladas de Q exigidas)}\\
③ \;\; x_2 \leq 6 & \text{(horas máximas de la planta B)}\\
x_1, x_2 \geq 0
\end{cases}$$

La tabla óptima del primal ($x_3$, $x_4$ excesos de ① y ②; $x_5$ holgura de ③; $x_6$, $x_7$ ficticias de ① y ②):

| $c_i$ | Base | $A_1$ (3) | $A_2$ (2) | $A_3$ (0) | $A_4$ (0) | $A_5$ (0) | $A_6$ ($M$) | $A_7$ ($M$) | $X$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | $A_1$ | 1 | 0 | −1 | 1 | 0 | 1 | −1 | **4** |
| 2 | $A_2$ | 0 | 1 | 1 | −2 | 0 | −1 | 2 | **4** |
| 0 | $A_5$ | 0 | 0 | −1 | 2 | 1 | 1 | −2 | **2** |
| | $z_j$ | 3 | 2 | −1 | −1 | 0 | 1 | 1 | **20** |
| | $c_j - z_j$ | 0 | 0 | 1 | 1 | 0 | $M-1$ | $M-1$ | |

**a) Armar el dual.** Escribí el dual completo, con una variable $u_i$ por cada restricción del primal. Indicá el signo de cada $u_i$ y justificalo con la tabla de signos (resumen, §6.1). Cuidado: el primal es **Min**.

**b) Interpretación económica.** ¿Qué representa cada $u_i$? ¿Qué dice, en palabras, cada restricción del dual? Pista: pensá en alguien que quiere "comprarle" a la empresa las toneladas de P y Q que necesita.

**c) La solución del dual sin resolverlo.** Leé $u^*$ en la tabla óptima del primal. Indicá en qué columnas y en qué fila. Calculá el valor óptimo del dual y comprobá el teorema fundamental.

**d) Factibilidad dual.** Reemplazá $u^*$ en cada restricción del dual. ¿Cuáles se cumplen justo y cuáles con holgura? ¿Por qué?

**e) Holguras complementarias.** Armá los cinco pares primal–dual (variable de decisión ↔ holgura o exceso dual; holgura o exceso primal ↔ variable dual), con el valor de cada lado. Verificá que en cada par al menos uno vale cero.

**f) El dual por método gráfico.** Usando holguras complementarias, deducí cuánto vale $u_3$ **sin mirar la tabla**. Con eso el dual queda con dos variables: resolvelo por método gráfico y verificá que llegues al mismo $u^*$.

## Parte B — Armar un dual con todos los casos de signo

$$\text{Max } z = 5x_1 + 4x_2 - 3x_3 \quad \text{s.a.} \quad
\begin{cases}
① \;\; x_1 + x_2 + x_3 \leq 10\\
② \;\; 2x_1 - x_2 \geq 4\\
③ \;\; x_1 + 3x_3 = 6\\
x_1 \geq 0,\; x_2 \geq 0,\; x_3 \text{ libre}
\end{cases}$$

**g)** Escribí el dual. Para cada variable dual, indicá su signo y de qué regla sale. Para cada restricción dual, indicá su tipo ($\leq$, $\geq$ o $=$) y de qué variable primal sale.

## Parte C — Teoría

**h)** Contestá en una o dos líneas cada una:

1. Si el primal tiene óptimo finito, ¿qué se puede decir del dual?
2. Si el primal tiene solución **no acotada**, ¿qué pasa con el dual?
3. En la tabla óptima de un primal hay una no básica con $c_j - z_j = 0$. ¿Qué tipo de solución tiene el dual?
4. Un recurso tiene precio sombra positivo. ¿Qué podés afirmar de su holgura en el primal? ¿Qué teorema lo justifica?
