# Investigación Operativa — Parcial de práctica (variante del 3/10)

> **Variante del parcial del 3/10**: mismo formato, mismos temas y misma dificultad, con otros números. Tiempo sugerido: 2 horas. Sólo la hoja de fórmulas. Elegí **una sola** opción por pregunta ("el valor más cercano"). Los números se verificaron por cálculo exacto.

## Ejercicio 1 — Método gráfico

$$\text{Min } W = 30x_1 + 50x_2 \quad \text{s.a.} \quad
\begin{cases}
① \;\; x_1 + 2x_2 \geq 40\\
② \;\; x_1 + x_2 \leq 50\\
③ \;\; x_1 - x_2 \leq 20\\
x_1, x_2 \geq 0
\end{cases}$$

Resolvé gráficamente y contestá:

**1)** ¿Cuáles son las coordenadas de la solución óptima del problema?

- a) Infinitas: todo el segmento entre $(0;\ 20)$ y $(26{,}67;\ 6{,}67)$.
- b) Única, en $(0;\ 20)$.
- c) Única, en $(26{,}67;\ 6{,}67)$.
- d) Única, en $(35;\ 15)$.
- e) Única, en $(40;\ 0)$.

**2)** ¿El punto $x_1 = 30$, $x_2 = 10$ es una solución factible?

- a) No, viola la restricción ③.
- b) No, viola la restricción ①.
- c) Sí, cumple las tres restricciones y la no negatividad.
- d) No, viola la restricción ②.
- e) Sí, y además es la solución óptima.

**3)** ¿Qué restricciones funcionales están activas en el óptimo?

- a) Sólo ①.
- b) ① y ③.
- c) ② y ③.
- d) ① y ②.
- e) Ninguna.

**4)** ¿Cuál es el valor de la variable de exceso de la primera restricción en el punto $(35;\ 15)$?

- a) 0
- b) 15
- c) −25
- d) 25
- e) 65

**5)** ¿Cuál es el costo óptimo, en pesos?

- a) 1.133,33
- b) 1.800
- c) 1.000
- d) 2.500
- e) 1.200

## Ejercicio 2 — La fábrica de alimentos: simplex, sensibilidad y dual

Una fábrica de alimentos produce galletitas ($x_1$), budines ($x_2$) y alfajores ($x_3$), medidos en cajas. El objetivo es maximizar la ganancia en pesos.

$$\text{Max } Z = 40x_1 + 85x_2 + 80x_3 \quad \text{s.a.} \quad
\begin{cases}
① \;\; 3x_1 + 2x_2 + x_3 \leq 8000 & \text{(kg de harina)}\\
② \;\; 0{,}25x_1 + 0{,}25x_2 + 0{,}5x_3 \leq 1700 & \text{(horas de horno)}\\
③ \;\; x_3 \geq 250 & \text{(contrato mínimo de alfajores)}\\
x_j \geq 0
\end{cases}$$

En forma estándar con Gran M: $x_4$ y $x_5$ son las holguras de ① y ②, $x_6$ el exceso de ③ y $x_7$ su ficticia. A continuación se muestra una tabla simplex de su resolución:

| $C_B$ | Base | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $X_i$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 40 | $A_1$ | 1 | 3/5 | 0 | 2/5 | −4/5 | 0 | 0 | 1840 |
| 80 | $A_3$ | 0 | 1/5 | 1 | −1/5 | 12/5 | 0 | 0 | 2480 |
| 0 | $A_6$ | 0 | 1/5 | 0 | −1/5 | 12/5 | 1 | −1 | 2230 |

Resolvé analíticamente y contestá:

**1)** Según la tabla presentada, ¿qué debe suceder según el simplex?

- a) Detenerse: la tabla es óptima porque no hay variables ficticias en la base.
- b) Ingresar $x_2$ a la base y sacar $x_3$.
- c) Ingresar $x_2$ a la base y sacar $x_6$.
- d) Ingresar $x_4$ a la base y sacar $x_1$.
- e) Ingresar $x_2$ a la base y sacar $x_1$.

**2)** ¿Cuál es el precio sombra de la restricción de horas de horno en el óptimo?

- a) 160
- b) 100
- c) 0
- d) 30
- e) 200

**3)** ¿En qué rango puede variar el $c_3$ de los alfajores para que la base óptima no cambie?

- a) $[0;\ 170]$
- b) $[80;\ 170]$
- c) $[42{,}5;\ 170]$
- d) $[70;\ 90]$
- e) $[117{,}5;\ 160]$

**4)** ¿Cuál es la función objetivo del dual asociado, asumiendo todas las variables duales $y_j \geq 0$?

- a) Minimizar $W = 8000y_1 + 1700y_2 - 250y_3$
- b) Minimizar $W = 40y_1 + 85y_2 + 80y_3$
- c) Maximizar $W = 8000y_1 + 1700y_2 - 250y_3$
- d) Minimizar $W = 8000y_1 + 1700y_2 + 250y_3$
- e) Maximizar $W = 8000y_1 + 1700y_2 + 250y_3$

**5)** ¿Qué variables de holgura o exceso resultan no básicas en el óptimo?

- a) Sólo $x_4$.
- b) Sólo $x_5$.
- c) $x_4$, $x_5$ y $x_6$.
- d) $x_4$ y $x_5$.
- e) Sólo $x_6$.

**6)** ¿Qué significa económicamente el precio sombra de la primera restricción?

- a) Cuesta 30 pesos almacenar cada kg de harina.
- b) Sobran 30 kg de harina en el inventario.
- c) Si disponemos de 1 kg más de harina, la ganancia aumenta en 30 pesos.
- d) Si aumentamos el precio de los budines, la ganancia aumentará en 30 pesos.
- e) Si disponemos de 1 kg más de harina, la ganancia disminuye en 30 pesos.

**7)** Al plantear la tabla simplex inicial, ¿qué variable ingresa y cuál sale de la base?

- a) Ingresa $x_3$, sale $x_4$.
- b) Ingresa $x_3$, sale $x_7$.
- c) Ingresa $x_3$, sale $x_5$.
- d) Ingresa $x_2$, sale $x_7$.
- e) Ingresa $x_1$, sale $x_7$.

**8)** En el óptimo, ¿cuál es el costo reducido de las galletitas y cómo se interpreta?

- a) 0: significa que ya se están produciendo y son rentables.
- b) 75: significa que conviene producirlas para aumentar la ganancia.
- c) −40: significa que no hay capacidad suficiente para producirlas.
- d) −75: significa que hay que bajar su precio en 75 para producirlas.
- e) −75: producir una caja de galletitas disminuiría la ganancia en 75 pesos.

## Ejercicio 3 — Stock con restricción financiera

Una distribuidora de insumos médicos gestiona el stock de dos productos críticos: guantes (A) y barbijos (B).

| | Demanda anual | Costo fijo del pedido | Costo unitario de compra |
|---|---|---|---|
| Guantes (A) | $D_A$ = 9.000 u | $L_A$ = \$ 200 | $C_A$ = \$ 40 |
| Barbijos (B) | $D_B$ = 5.000 u | $L_B$ = \$ 300 | $C_B$ = \$ 120 |

La tasa de mantenimiento es $i$ = 25 % anual. El capital máximo para invertir en el stock es $I_0$ = **\$ 22.000**.

**1)** ¿Qué valor de $\lambda$ es el más cercano al óptimo para cumplir con el presupuesto?

- a) $\lambda \approx 0{,}41$
- b) $\lambda \approx 0{,}10$
- c) $\lambda \approx 0{,}98$
- d) $\lambda \approx 0{,}25$
- e) $\lambda \approx 0{,}12$

**2)** ¿Cuál es el tamaño de lote óptimo para los guantes (A) si se ignora la restricción?

- a) 600 unidades
- b) 849 unidades
- c) 424 unidades
- d) 316 unidades
- e) 426 unidades

**3)** ¿Cuál es el valor más cercano a la inversión promedio si se consideran ambos lotes óptimos?

- a) \$ 11.913, por lo tanto SÍ cumple la restricción.
- b) \$ 30.974, por lo tanto SÍ cumple la restricción.
- c) \$ 22.000, por lo tanto coincide con la restricción.
- d) \$ 61.947, por lo tanto NO cumple la restricción.
- e) \$ 30.974, por lo tanto NO cumple la restricción.

**4)** Bajo la restricción financiera, ¿cuál es el tamaño de lote óptimo aproximado para los barbijos (B)?

- a) 316 unidades
- b) 225 unidades
- c) 160 unidades
- d) 426 unidades
- e) 292 unidades

**5)** ¿Le convendría a la distribuidora tomar un crédito al 15 % anual para expandir su presupuesto?

- a) No, porque $\lambda$ indica que incorporar más capital perjudica la ganancia (es negativo).
- b) No, porque la tasa bancaria es un costo adicional y el modelo ya penaliza el inventario con un 25 %.
- c) Sí, porque el costo marginal del capital invertido ($\lambda$) es mayor que la tasa bancaria.
- d) Sí, resulta conveniente porque el límite de capital actual es bajo.
- e) No, porque la tasa bancaria supera a $i + \lambda$.

## Hoja de respuestas

| Ej. 1 | 1 | 2 | 3 | 4 | 5 | | | |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Letra | | | | | | | | |

| Ej. 2 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Letra | | | | | | | | |

| Ej. 3 | 1 | 2 | 3 | 4 | 5 | | | |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Letra | | | | | | | | |
