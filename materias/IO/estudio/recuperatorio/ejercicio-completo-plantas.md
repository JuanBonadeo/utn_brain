# Ejercicio completo — las dos plantas

Una empresa fabrica dos productos químicos, **P** y **Q**, en dos plantas, **A** y **B**. Cada semana decide cuántas horas hace funcionar cada planta.

- Una hora de la **planta A** cuesta \$ 3 000 y produce **2 toneladas de P** y **1 tonelada de Q**.
- Una hora de la **planta B** cuesta \$ 2 000 y produce **1 tonelada de P** y **1 tonelada de Q**.
- Los clientes exigen por semana **al menos 12 toneladas de P** y **al menos 8 toneladas de Q**.
- Por un plan de mantenimiento, la **planta B** puede funcionar **como máximo 6 horas** por semana.

La empresa quiere cumplir los pedidos al **menor costo** posible. Trabajá los costos en miles de pesos.

## Parte 1 — Modelo y simplex

**a)** Definí las variables de decisión con el formato de la cátedra: qué representan, en qué unidad y en qué período. Planteá el modelo: funcional, restricciones con el nombre de cada una y no negatividad.

**b)** Escribí la forma estándar con Gran M. Para cada variable que agregues, decí qué es (holgura, exceso o ficticia), de qué restricción y qué significa en el problema. Usá la numeración de la cátedra.

**c)** Resolvé por el método simplex hasta la tabla óptima. En cada tabla indicá quién entra, los cocientes θ, quién sale y el pivote. Podés trabajarlo como Min o convertirlo a Max, pero aclaralo.

**d)** Escribí $S^*$ y $w^*$. ¿La solución es única? Justificá con la tabla.

**e)** Interpretá la solución:

1. ¿Cuántas horas funciona cada planta?
2. ¿Qué pedidos se cumplen justo y cuáles con exceso, y por cuánto?
3. ¿Sobra capacidad en la planta B?
4. ¿Qué restricciones son activas?

## La tabla óptima

Para hacer la Parte 2 sin el simplex. Está en **forma Min**, con $x_3$ y $x_4$ los excesos de ① y ②, $x_5$ la holgura de ③ y $x_6$, $x_7$ las ficticias de ① y ②.

| $c_i$ | Base | $A_1$ (3) | $A_2$ (2) | $A_3$ (0) | $A_4$ (0) | $A_5$ (0) | $A_6$ ($M$) | $A_7$ ($M$) | $X$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | $A_1$ | 1 | 0 | −1 | 1 | 0 | 1 | −1 | **4** |
| 2 | $A_2$ | 0 | 1 | 1 | −2 | 0 | −1 | 2 | **4** |
| 0 | $A_5$ | 0 | 0 | −1 | 2 | 1 | 1 | −2 | **2** |
| | $z_j$ | 3 | 2 | −1 | −1 | 0 | 1 | 1 | **20** |
| | $c_j - z_j$ | 0 | 0 | 1 | 1 | 0 | $M-1$ | $M-1$ | |

Si la resolviste como Max ($z = -w$), tu tabla tiene el mismo cuerpo y la misma columna $X$, y los $c_j$, $z_j$ y $c_j - z_j$ con el signo cambiado.

## Parte 2 — Sensibilidad

Contestá todo a partir de la tabla óptima, **sin volver a resolver**. Cuidado: el problema es de **mínimo**.

**f)** Hallá el **rango del costo por hora de la planta A** ($c_1$) y el de la **planta B** ($c_2$) en los que el plan óptimo no cambia. Interpretá cada uno en una frase.

**g)** Si la hora de la planta A pasa a costar \$ 5 000, ¿sigue siendo óptimo el plan? Si no, ¿qué variable entraría a la base?

**h)** Indicá el **valor implícito** de cada restricción y dónde lo leés. Interpretá cada uno. ¿El signo es el que corresponde a un Min con restricciones $\geq$ y $\leq$? Justificá con la tabla de signos del resumen (§5.5).

**i)** Hallá el **rango de $b_1$** (toneladas de P exigidas). Si el cliente pasa a pedir **14 toneladas de P**, calculá el nuevo plan y el nuevo costo con $x_i' = x_i + r_{ik}\,\Delta b_k$ y $w^{*\prime} = w^* + u_k\,\Delta b_k$. Verificá el plan reemplazando en las restricciones originales.

**j)** Hallá el **rango de $b_3$** (horas de la planta B). Si el mantenimiento se reprograma y la planta B puede funcionar 10 horas, ¿baja el costo? ¿Por qué?

**k)** Se evalúa alquilar una **planta C**: cada hora produce 1 tonelada de P y 1 de Q, y cuesta \$ 2 500. ¿Conviene usarla? Usá los valores implícitos. ¿A partir de qué costo por hora convendría?

## Para tener a mano

| Qué | Dónde se lee | En Min |
|---|---|---|
| ¿Es óptima? | fila $c_j - z_j$ | todos $\geq 0$ |
| Quién entra | fila $c_j - z_j$ | el más negativo |
| Quién sale | $\theta = X / y_{ik}$ con $y_{ik} > 0$ | el menor (igual que en Max) |
| Rango de $c_k$ | **fila** de $x_k$, columnas no básicas | pedir $c_j - z_j$ nuevo $\geq 0$ |
| Rango de $b_k$ | **columna** de $B^{-1}$ (la que tenía el 1 en la fila $k$ al inicio) | igual que en Max |
| Valor implícito | fila $z_j$, en esa misma columna | — |
| Variable nueva | $z_k = \sum u_i\,a_{ik}$ | entra si $c_k - z_k < 0$ |
