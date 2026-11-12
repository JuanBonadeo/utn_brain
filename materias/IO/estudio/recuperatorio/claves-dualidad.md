# Claves de dualidad

Cuatro cosas, con el ejemplo del ejercicio de dualidad 2: qué se convierte en qué, dónde se lee el dual en la tabla óptima del primal, holguras complementarias y la interpretación económica.

**El ejemplo.** Una fábrica produce los artículos A, B y C con horas de máquina y de mano de obra.

$$\text{Primal: Max } z = 6x_1 + 5x_2 + 4x_3 \quad
\begin{cases}
① \;\; 2x_1 + x_2 + x_3 \leq 100 & \text{(horas de máquina)}\\
② \;\; x_1 + x_2 + 2x_3 \leq 80 & \text{(horas de mano de obra)}\\
x_1, x_2, x_3 \geq 0
\end{cases}$$

$$\text{Dual: Min } w = 100u_1 + 80u_2 \quad
\begin{cases}
(x_1) \;\; 2u_1 + u_2 \geq 6\\
(x_2) \;\; u_1 + u_2 \geq 5\\
(x_3) \;\; u_1 + 2u_2 \geq 4\\
u_1, u_2 \geq 0
\end{cases}$$

## 1. Qué se convierte en qué

Al pasar al dual, **las restricciones se convierten en variables y las variables en restricciones**. Por eso las variables auxiliares **cambian de tipo**:

- en el primal (Max con $\leq$), cada restricción tiene una **holgura**: lo que sobra del recurso;
- en el dual (Min con $\geq$), cada restricción tiene un **exceso**: cuánto se pasa.

Las holguras del primal **no** se convierten en los excesos del dual. Las parejas son **cruzadas**:

| Primal | se empareja con | Dual |
|---|:---:|---|
| restricción ① (con su holgura $x_4$) | ↔ | variable $u_1$ |
| restricción ② (con su holgura $x_5$) | ↔ | variable $u_2$ |
| variable $x_1$ | ↔ | restricción $(x_1)$ (con su exceso $e_1$) |
| variable $x_2$ | ↔ | restricción $(x_2)$ (con su exceso $e_2$) |
| variable $x_3$ | ↔ | restricción $(x_3)$ (con su exceso $e_3$) |

En una línea: **holgura del primal ↔ variable del dual**, y **variable del primal ↔ exceso del dual**.

Cuántos hay de cada cosa:

| | Primal | Dual |
|---|---|---|
| variables de decisión | 3 ($x_1, x_2, x_3$) | 2 ($u_1, u_2$) |
| restricciones | 2 | 3 |
| auxiliares | 2 holguras ($x_4, x_5$) | 3 excesos ($e_1, e_2, e_3$) |
| total | **5** | **5** |

Los dos tienen la misma cantidad total de variables, y por eso se pueden aparear de a pares.

## 2. Dónde se lee el dual en la tabla óptima del primal

La tabla óptima del primal:

| $c_i$ | Base | $A_1$ (6) | $A_2$ (5) | $A_3$ (4) | $A_4$ (0) | $A_5$ (0) | $X$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 6 | $A_1$ | 1 | 0 | −1 | 1 | −1 | **20** |
| 5 | $A_2$ | 0 | 1 | 3 | −1 | 2 | **60** |
| | $z_j$ | 6 | 5 | 9 | 1 | 4 | **420** |
| | $c_j - z_j$ | 0 | 0 | −5 | −1 | −4 | |

**La regla general: $u_i$ es el $z_j$ de la columna que en la tabla inicial tenía el +1 en la fila $i$.** Esa columna es la holgura si la restricción es $\leq$, y la ficticia si es $\geq$ o $=$.

| Restricción | Tipo | Columna | $u_i = z_j$ |
|---|---|---|---|
| ① máquina | $\leq$ | holgura $A_4$ | $u_1 = z_4 = 1$ |
| ② mano de obra | $\leq$ | holgura $A_5$ | $u_2 = z_5 = 4$ |

¿Por qué $z_j$? Porque $u = c_B B^{-1}$, y debajo de esas columnas está $B^{-1}$. El $z_j$ es $c_B$ por esa columna.

**El atajo para Max con todas $\leq$: la fila $c_j - z_j$ cambiada de signo es la solución completa del dual.**

| | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
|---|:---:|:---:|:---:|:---:|:---:|
| $c_j - z_j$ | 0 | 0 | −5 | −1 | −4 |
| $-(c_j - z_j)$ | 0 | 0 | 5 | 1 | 4 |
| es en el dual… | $e_1$ | $e_2$ | $e_3$ | $u_1$ | $u_2$ |

- Bajo las **variables de decisión** quedan los **excesos del dual**: $e_1 = 0$, $e_2 = 0$, $e_3 = 5$.
- Bajo las **holguras** quedan las **variables del dual**: $u_1 = 1$, $u_2 = 4$. En una holgura $c_j = 0$, así que $-(c_j - z_j) = z_j$. Es la regla general.
- Valor del dual: $w^* = 100 \cdot 1 + 80 \cdot 4 = 420 = z^*$.

**Los otros casos:**

| Si la restricción $i$ es… | $u_i$ se lee en… |
|---|---|
| $\leq$ (tiene holgura) | $z_j$ de la holgura |
| $\geq$ (tiene exceso y ficticia) | $z_j$ de la **ficticia**, o $z_j$ del **exceso cambiado de signo** |
| $=$ (sólo ficticia) | $z_j$ de la ficticia |

| Si el primal es… | el exceso o holgura del dual de $x_j$ es… |
|---|---|
| Max | $-(c_j - z_j)$ de la columna de $x_j$ |
| Min | $c_j - z_j$ de la columna de $x_j$ (sin cambiar el signo) |

## 3. Holguras complementarias

**En el óptimo, en cada pareja primal–dual al menos uno de los dos vale cero** (pueden ser los dos).

| Pareja | Primal | Dual | ¿Uno es 0? |
|---|---|---|:---:|
| $x_1$ ↔ $e_1$ | $x_1 = 20$ (se fabrica A) | $e_1 = 0$ | ✓ |
| $x_2$ ↔ $e_2$ | $x_2 = 60$ (se fabrica B) | $e_2 = 0$ | ✓ |
| $x_3$ ↔ $e_3$ | $x_3 = 0$ (no se fabrica C) | $e_3 = 5$ | ✓ |
| $x_4$ ↔ $u_1$ | $x_4 = 0$ (máquina agotada) | $u_1 = 1$ | ✓ |
| $x_5$ ↔ $u_2$ | $x_5 = 0$ (mano de obra agotada) | $u_2 = 4$ | ✓ |

**Las cuatro frases:**

1. Si un recurso **sobra** (holgura $> 0$), su precio sombra es **0**.
2. Si un recurso tiene precio sombra **$> 0$**, está **agotado** (holgura $= 0$).
3. Si un producto **se fabrica** ($x_j > 0$), los recursos que usa valen **exactamente** lo que deja (exceso dual $= 0$).
4. Si los recursos que usa un producto valen **más** de lo que deja (exceso dual $> 0$), **no se fabrica** ($x_j = 0$).

**Del dual al primal** (resolver el dual por método gráfico y recuperar el primal):

1. Reemplazá $u^*$ en cada restricción dual. La que **se pasa** tiene exceso $> 0$, así que su $x_j = 0$. Acá: $(x_3)$ da $1 + 2 \cdot 4 = 9 > 4$, con exceso 5, así que $x_3 = 0$.
2. Cada $u_i > 0$ hace que la restricción $i$ del primal se cumpla **justo**. Acá $u_1 = 1$ y $u_2 = 4$, así que ① y ② son igualdades.
3. Resolvé el sistema que queda: $2x_1 + x_2 = 100$ y $x_1 + x_2 = 80$. Restando, $x_1 = 20$ y $x_2 = 60$.
4. Controlá: $z^* = 6 \cdot 20 + 5 \cdot 60 = 420 = w^*$.

**Del primal al dual** (conocés $x^*$ y querés $u^*$):

1. Cada holgura del primal $> 0$ hace que su $u_i = 0$.
2. Cada $x_j > 0$ hace que su restricción dual se cumpla **justo**.
3. Resolvé el sistema.

## 4. Interpretación económica

**Primal Max con recursos ($\leq$): el dual es alguien que alquila los recursos.**

- $u_i$ = precio por unidad del recurso $i$ que pagaría quien lo alquila. Acá, \$ 1 000 por hora de máquina y \$ 4 000 por hora de mano de obra.
- Restricción dual $j$: **lo que valen los recursos que usa el producto $j$, a esos precios, es por lo menos lo que deja**. Si no, a la fábrica le conviene fabricarlo antes que alquilar. Para C: $1 \cdot 1 + 2 \cdot 4 = 9 \geq 4$.
- Funcional dual: quien alquila quiere pagar **lo mínimo** por todos los recursos, $100u_1 + 80u_2$.
- $w^* = z^*$: en el óptimo paga exactamente lo que ganaría la fábrica produciendo, \$ 420 000. A la fábrica le da igual producir o alquilar.

**Primal Min con requerimientos ($\geq$): el dual es un proveedor que vende el producto.**

- $u_i$ = precio por unidad del requerimiento $i$ que puede cobrar el proveedor.
- Restricción dual $j$: **lo que produce la actividad $j$, valuado a esos precios, no supera lo que cuesta**. Si no, la empresa produce sola.
- Funcional dual: el proveedor quiere **cobrar lo máximo** por todo lo requerido.
- $w^* = z^*$: en el óptimo cobra exactamente lo que le cuesta a la empresa producir.

**Plantilla para escribir la respuesta:**

> $u_i$ representa el valor (precio sombra) de una unidad de [recurso $i$]. La restricción dual de $x_j$ exige que los recursos que consume una unidad de [producto $j$], valuados a esos precios, valgan por lo menos [o como mucho, si el primal es Min] su [ganancia / costo] $c_j$. El dual [minimiza / maximiza] el valor total de los recursos, y en el óptimo coincide con el del primal.
