# Investigación Operativa — Parcial del 3/10/2026 (Tema 1)

> **Para practicar en condiciones de examen.** Tiempo sugerido: 2 horas. Sólo la hoja de fórmulas. El enunciado es la transcripción que hizo un compañero; los Ej. 1 y 2 quedaron sin las opciones del original, así que se contestan con el valor. Las opciones del Ej. 3 están **reconstruidas** con los números del enunciado. La resolución está en `parcial-2026-resuelto.pdf`: no la mires hasta terminar.

## Ejercicio 1 — Método gráfico

$$\text{Min } Z = 150x_1 + 500x_2 \quad \text{s.a.} \quad
\begin{cases}
① \;\; 3x_1 + 10x_2 \geq 300\\
② \;\; x_1 + 2x_2 \leq 120\\
③ \;\; -x_1 + x_2 \leq 30\\
x_1, x_2 \geq 0
\end{cases}$$

Resolvé gráficamente y contestá:

1. ¿Cuáles son las coordenadas de la solución óptima del problema?
2. ¿El punto $x_1 = 50$, $x_2 = 30$ es una solución factible?
3. ¿Qué restricciones funcionales están activas en el óptimo?
4. ¿Cuál es el valor de la variable de holgura de la segunda restricción en el punto $(100;\ 0)$?
5. ¿Cuál es el costo óptimo, en pesos?

## Ejercicio 2 — La refinería: simplex, sensibilidad y dual

Una refinería de petróleo produce nafta ($x_1$), diésel ($x_2$) y fueloil ($x_3$), medidos en toneladas. El objetivo es maximizar la ganancia en dólares.

$$\text{Max } Z = 50x_1 + 80x_2 + 30x_3 \quad \text{s.a.} \quad
\begin{cases}
① \;\; 2x_1 + 3x_2 + 1{,}5x_3 \leq 5000 & \text{(materia prima: petróleo crudo)}\\
② \;\; 0{,}5x_1 + 0{,}8x_2 + 0{,}2x_3 \leq 1200 & \text{(capacidad de destilación)}\\
③ \;\; x_2 \geq 500 & \text{(contrato mínimo de diésel)}\\
x_j \geq 0
\end{cases}$$

En forma estándar con Gran M: $x_4$ y $x_5$ son las holguras de ① y ②, $x_6$ el exceso de ③ y $x_7$ su ficticia. A continuación se muestra una tabla simplex de su resolución:

| $C_B$ | Base | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $X_i$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | $A_4$ | 1/8 | 0 | 3/4 | 1 | −15/4 | 0 | 0 | 500 |
| 0 | $A_6$ | 5/8 | 0 | 1/4 | 0 | 5/4 | 1 | −1 | 1000 |
| 80 | $A_2$ | 5/8 | 1 | 1/4 | 0 | 5/4 | 0 | 0 | 1500 |

Resolvé analíticamente y contestá:

1. Según la tabla presentada, ¿qué debe suceder según el simplex? ¿Se detiene o sigue? Si sigue, ¿qué variable entra y cuál sale?
2. ¿Cuál es el precio sombra de la restricción de capacidad de destilación en el óptimo?
3. ¿En qué rango puede variar el $c_2$ del diésel para que la base óptima no cambie?
4. ¿Cuál es la función objetivo del dual asociado, suponiendo todas las variables duales $y_j \geq 0$?
5. ¿Qué variables de holgura o exceso resultan no básicas en el óptimo?
6. ¿Qué significa económicamente el precio sombra de la primera restricción?
7. Al plantear la tabla simplex inicial, ¿qué variable ingresa y cuál sale de la base?
8. En el óptimo, ¿cuál es el costo reducido de la nafta y cómo se interpreta?

## Ejercicio 3 — Stock con restricción financiera

Una ferretería mayorista gestiona el stock de dos insumos críticos: tornillos (A) y tuercas (B).

| | Demanda anual | Costo fijo del pedido | Costo unitario de compra |
|---|---|---|---|
| Tornillos (A) | $D_A$ = 12.000 u | $L_A$ = \$ 150 | $C_A$ = \$ 50 |
| Tuercas (B) | $D_B$ = 8.000 u | $L_B$ = \$ 200 | $C_B$ = \$ 80 |

La tasa de mantenimiento es $i$ = 20 % anual. El capital máximo para invertir en el stock es $I_0$ = **\$ 23.000** (en la foto del original el 3 podría ser un 8; usá 23.000).

Elegí **una sola opción** en cada pregunta.

**1)** ¿Qué valor de $\lambda$ es el más cercano al óptimo para cumplir con el presupuesto?

- a) $\lambda \approx 0{,}43$
- b) $\lambda \approx 0{,}09$
- c) $\lambda \approx 0{,}21$
- d) $\lambda \approx 1{,}04$
- e) $\lambda \approx 0{,}10$

**2)** ¿Cuál es el tamaño de lote óptimo para los tornillos (A) si se ignora la restricción?

- a) 424 unidades
- b) 600 unidades
- c) 849 unidades
- d) 447 unidades
- e) 420 unidades

**3)** ¿Cuál es el valor más cercano a la inversión promedio si se consideran ambos lotes óptimos?

- a) \$ 12.650, por lo tanto SÍ cumple la restricción.
- b) \$ 32.889, por lo tanto SÍ cumple la restricción.
- c) \$ 23.000, por lo tanto coincide con la restricción.
- d) \$ 32.889, por lo tanto NO cumple la restricción.
- e) \$ 65.777, por lo tanto NO cumple la restricción.

**4)** Bajo la restricción financiera, ¿cuál es el tamaño de lote óptimo aproximado para las tuercas (B)?

- a) 447 unidades
- b) 219 unidades
- c) 313 unidades
- d) 420 unidades
- e) 407 unidades

**5)** ¿Le convendría a la ferretería tomar un crédito al 12 % anual para expandir su presupuesto?

- a) No, porque $\lambda$ indica que incorporar más capital perjudica la ganancia (es negativo).
- b) Sí, porque el costo marginal del capital invertido ($\lambda$) es mayor que la tasa bancaria.
- c) No, porque la tasa bancaria es un costo adicional y el modelo ya penaliza el inventario con un 20 %.
- d) Sí, resulta conveniente porque el límite de capital actual es bajo.
- e) No, porque la tasa bancaria supera a $i + \lambda$.

## Hoja de respuestas

| Ej. 1 | Respuesta |
|---|---|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |

| Ej. 2 | Respuesta |
|---|---|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |
| 8 | |

| Ej. 3 | 1 | 2 | 3 | 4 | 5 |
|---|:---:|:---:|:---:|:---:|:---:|
| Letra | | | | | |
