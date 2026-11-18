# Investigación Operativa — Parcial de práctica (variante 2)

> **Segunda variante del parcial del 3/10**: mismo formato, mismos temas y misma dificultad, con otros números. Tiempo sugerido: 2 horas. Sólo la hoja de fórmulas. Elegí **una sola** opción por pregunta ("el valor más cercano"). Los números se verificaron por cálculo exacto.

## Ejercicio 1 — Método gráfico

$$\text{Max } Z = 20x_1 + 30x_2 \quad \text{s.a.} \quad
\begin{cases}
① \;\; 2x_1 + 3x_2 \leq 120\\
② \;\; x_1 \leq 40\\
③ \;\; x_2 \geq 10\\
x_1, x_2 \geq 0
\end{cases}$$

Resolvé gráficamente y contestá:

**1)** ¿Cuáles son las coordenadas de la solución óptima del problema?

- a) Única, en $(40;\ 13{,}33)$.
- b) Única, en $(0;\ 40)$.
- c) Única, en $(40;\ 10)$.
- d) Infinitas: todo el segmento entre $(0;\ 40)$ y $(40;\ 13{,}33)$.
- e) Infinitas: todo el segmento entre $(0;\ 10)$ y $(40;\ 10)$.

**2)** ¿El punto $x_1 = 30$, $x_2 = 25$ es una solución factible?

- a) Sí, cumple las tres restricciones y la no negatividad.
- b) No, viola la restricción ①.
- c) No, viola la restricción ②.
- d) No, viola la restricción ③.
- e) Sí, y además es la solución óptima.

**3)** ¿Qué restricciones funcionales están activas en el óptimo?

- a) ① (en todo el segmento óptimo).
- b) Sólo ②.
- c) ② y ③.
- d) Ninguna.
- e) Sólo ③.

**4)** ¿Cuál es el valor de la variable de holgura de la primera restricción en el punto $(40;\ 10)$?

- a) 110
- b) −10
- c) 0
- d) 120
- e) 10

**5)** ¿Cuál es la ganancia óptima, en pesos?

- a) 1.100
- b) 1.200
- c) 300
- d) 1.300
- e) 800

## Ejercicio 2 — La metalúrgica: simplex, sensibilidad y dual

Una metalúrgica produce perfiles ($x_1$), chapas ($x_2$) y caños ($x_3$), medidos en toneladas. El objetivo es maximizar la ganancia en dólares.

$$\text{Max } Z = 30x_1 + 50x_2 + 40x_3 \quad \text{s.a.} \quad
\begin{cases}
① \;\; 3x_1 + 2x_2 + 2{,}5x_3 \leq 6000 & \text{(toneladas de acero)}\\
② \;\; 0{,}4x_1 + 0{,}8x_2 + 0{,}5x_3 \leq 1700 & \text{(horas de laminado)}\\
③ \;\; x_2 \geq 500 & \text{(contrato mínimo de chapas)}\\
x_j \geq 0
\end{cases}$$

En forma estándar con Gran M: $x_4$ y $x_5$ son las holguras de ① y ②, $x_6$ el exceso de ③ y $x_7$ su ficticia. A continuación se muestra una tabla simplex de su resolución:

| $C_B$ | Base | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $X_i$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 50 | $A_2$ | 0 | 1 | 0 | 0 | 0 | −1 | 1 | 500 |
| 40 | $A_3$ | 6/5 | 0 | 1 | 2/5 | 0 | 4/5 | −4/5 | 2000 |
| 0 | $A_5$ | −1/5 | 0 | 0 | −1/5 | 1 | 2/5 | −2/5 | 300 |

Resolvé analíticamente y contestá:

**1)** Según la tabla presentada, ¿qué debe suceder según el simplex?

- a) Detenerse: la tabla es óptima porque no hay variables ficticias en la base.
- b) Ingresar $x_6$ a la base y sacar $x_2$.
- c) Ingresar $x_6$ a la base y sacar $x_5$.
- d) Ingresar $x_6$ a la base y sacar $x_3$.
- e) Ingresar $x_1$ a la base y sacar $x_5$.

**2)** ¿Cuál es el precio sombra de la restricción de horas de laminado en el óptimo?

- a) 0
- b) 7
- c) 50
- d) 90
- e) 45

**3)** ¿En qué rango puede variar el $c_2$ de las chapas para que la base óptima no cambie?

- a) $[0;\ 64]$
- b) $[32;\ 64]$
- c) $[50;\ 64]$
- d) $[40;\ 60]$
- e) $[68;\ 100]$

**4)** ¿Cuál es la función objetivo del dual asociado, asumiendo todas las variables duales $y_j \geq 0$?

- a) Minimizar $W = 30y_1 + 50y_2 + 40y_3$
- b) Maximizar $W = 6000y_1 + 1700y_2 - 500y_3$
- c) Minimizar $W = 6000y_1 + 1700y_2 + 500y_3$
- d) Minimizar $W = 6000y_1 + 1700y_2 - 500y_3$
- e) Maximizar $W = 6000y_1 + 1700y_2 + 500y_3$

**5)** ¿Qué variables de holgura o exceso resultan no básicas en el óptimo?

- a) $x_4$ y $x_5$.
- b) Sólo $x_4$.
- c) Sólo $x_5$.
- d) $x_4$, $x_5$ y $x_6$.
- e) Sólo $x_6$.

**6)** ¿Qué significa económicamente el precio sombra de la primera restricción?

- a) Cuesta 7 dólares almacenar cada tonelada de acero.
- b) Sobran 7 toneladas de acero en el inventario.
- c) Si disponemos de 1 tonelada más de acero, la ganancia disminuye en 7 dólares.
- d) Si aumentamos el precio de las chapas, la ganancia aumentará en 7 dólares.
- e) Si disponemos de 1 tonelada más de acero, la ganancia aumenta en 7 dólares.

**7)** Al plantear la tabla simplex inicial, ¿qué variable ingresa y cuál sale de la base?

- a) Ingresa $x_2$, sale $x_4$.
- b) Ingresa $x_2$, sale $x_5$.
- c) Ingresa $x_2$, sale $x_7$.
- d) Ingresa $x_1$, sale $x_7$.
- e) Ingresa $x_3$, sale $x_7$.

**8)** En el óptimo, ¿cuál es el costo reducido de los perfiles y cómo se interpreta?

- a) 0: significa que ya se están produciendo y son rentables.
- b) −9: producir una tonelada de perfiles disminuiría la ganancia en 9 dólares.
- c) 9: significa que conviene producirlos para aumentar la ganancia.
- d) −9: significa que hay que bajar su precio en 9 para producirlos.
- e) −30: significa que no hay capacidad suficiente para producirlos.

## Ejercicio 3 — Stock con restricción financiera

Una librería mayorista gestiona el stock de dos productos: cuadernos (A) y resmas (B).

| | Demanda anual | Costo fijo del pedido | Costo unitario de compra |
|---|---|---|---|
| Cuadernos (A) | $D_A$ = 8.000 u | $L_A$ = \$ 150 | $C_A$ = \$ 30 |
| Resmas (B) | $D_B$ = 3.000 u | $L_B$ = \$ 250 | $C_B$ = \$ 60 |

La tasa de mantenimiento es $i$ = 20 % anual. El capital máximo para invertir en el stock es $I_0$ = **\$ 18.000**.

**1)** ¿Qué valor de $\lambda$ es el más cercano al óptimo para cumplir con el presupuesto?

- a) $\lambda \approx 0{,}12$
- b) $\lambda \approx 0{,}05$
- c) $\lambda \approx 0{,}25$
- d) $\lambda \approx 0{,}02$
- e) $\lambda \approx 0{,}10$

**2)** ¿Cuál es el tamaño de lote óptimo para los cuadernos (A) si se ignora la restricción?

- a) 894 unidades
- b) 447 unidades
- c) 632 unidades
- d) 354 unidades
- e) 567 unidades

**3)** ¿Cuál es el valor más cercano a la inversión promedio si se consideran ambos lotes óptimos?

- a) \$ 20.093, por lo tanto SÍ cumple la restricción.
- b) \$ 7.728, por lo tanto SÍ cumple la restricción.
- c) \$ 18.000, por lo tanto coincide con la restricción.
- d) \$ 20.093, por lo tanto NO cumple la restricción.
- e) \$ 40.187, por lo tanto NO cumple la restricción.

**4)** Bajo la restricción financiera, ¿cuál es el tamaño de lote óptimo aproximado para las resmas (B)?

- a) 354 unidades
- b) 284 unidades
- c) 567 unidades
- d) 412 unidades
- e) 317 unidades

**5)** ¿Le convendría a la librería tomar un crédito al 28 % anual para expandir su presupuesto?

- a) Sí, porque el costo marginal del capital invertido ($\lambda$) es mayor que la tasa bancaria.
- b) Sí, resulta conveniente porque el límite de capital actual es bajo.
- c) No, porque $\lambda$ indica que incorporar más capital perjudica la ganancia (es negativo).
- d) No, porque la tasa bancaria es un costo adicional y el modelo ya penaliza el inventario con un 20 %.
- e) No, porque la tasa bancaria supera a $i + \lambda$: el capital extra cuesta más de lo que ahorra.

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
