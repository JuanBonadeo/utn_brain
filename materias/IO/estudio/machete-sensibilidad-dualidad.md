# Machete — Sensibilidad y dualidad (Práctica 4)

Una carilla. Fundamentos en [[teoria-sensibilidad-dualidad]]; ejercicios resueltos en
[[practica-4-sensibilidad-dualidad]]. **Parametrización: fuera de alcance** (decisión del
2026-09-30).

## La idea: la tabla óptima *es* $B^{-1}$

```text
x_B = B⁻¹·b      Y_j = B⁻¹·A_j      z_j = c_B·Y_j      u = c_B·B⁻¹      z* = c_B·x_B
```

- $B^{-1}$ **ya está impresa**: son las columnas que formaban la identidad en la tabla
  inicial → las **holguras**, en el orden de las restricciones.
- Restricción $\geq$: la columna de la identidad era la **ficticia**. La de exceso vale
  $-B^{-1}e_i$ (cambiada de signo). No borres la ficticia si vas a hacer sensibilidad.
- **LINDO:** `SLK k+1` es la holgura de la **restricción k** (la fila 1 es el funcional).
  La fila `ART` es $z_j - c_j$, **no** $c_j - z_j$: cambiale el signo.

## Las tres preguntas de cada inciso

```text
1. ¿QUÉ DATO CAMBIA?     c  → puede romper OPTIMALIDAD  → miro la FILA cj−zj
                         b  → puede romper FACTIBILIDAD → miro la COLUMNA X
                         (cj−zj no contiene ningún b;  x_B = B⁻¹b no contiene ningún c)
2. ¿BÁSICA O NO BÁSICA?  define si se mueve una sola columna o toda la fila cj−zj
3. ¿CAE EN EL RANGO?     sí → misma base, se recalcula sin iterar
                         no → se itera desde esta tabla (Simplex o Simplex dual)
```

## Cuadro maestro (primal de Max, un cambio por vez)

| Cambia | Qué uso | Condición | Si cae en el rango |
|---|---|---|---|
| $c_k$, $x_k$ **no básica** | solo su $c_k - z_k$ | $\Delta c_k \leq -(c_k - z_k)$ | $x^*$ y $z^*$ **iguales** |
| $c_k$, $x_k$ **básica** | la **fila** de $x_k$: $y_{kj}$ de las no básicas | $\max\limits_{y_{kj}>0}\frac{c_j-z_j}{y_{kj}} \leq \Delta c_k \leq \min\limits_{y_{kj}<0}\frac{c_j-z_j}{y_{kj}}$ | $x^*$ igual; $z' = z^* + \Delta c_k\, x_k^*$ |
| $b_k$ | la **columna $k$ de $B^{-1}$** = holgura de la restr. $k$ | $\max\limits_{r_{ik}>0}\frac{-x_i}{r_{ik}} \leq \Delta b_k \leq \min\limits_{r_{ik}<0}\frac{-x_i}{r_{ik}}$ | base igual; $x_i' = x_i + r_{ik}\Delta b_k$; $z' = z^* + u_k \Delta b_k$ |
| $A_k$, $x_k$ **no básica** | $Y_k' = B^{-1}A_k'$, $z_k' = c_B Y_k'$ | $c_k - z_k' \leq 0$ | sigue óptima, nada cambia |
| $A_k$, $x_k$ **básica** | cambia $B$ misma | — | no hay atajo: se rehace |
| **variable nueva** | $Y_n = B^{-1}A_n$, $z_n = c_B Y_n = u \cdot A_n$ | $>0$ conviene · $=0$ óptimo alternativo · $<0$ no conviene | si no conviene, óptimo intacto |
| **restricción nueva** | reemplazar $x^*$ en ella | la cumple → **pasiva** | nada cambia. Si no la cumple → Simplex dual |

**Cómo cerrar un rango** (vale para $b$ siempre, y para $c$ en Max):

```text
denominador > 0  → da una cota INFERIOR  → de todas, quedate con la MAYOR
denominador < 0  → da una cota SUPERIOR  → de todas, quedate con la MENOR
denominador = 0  → no restringe          (grupo vacío → esa cota es ±∞)
al final: rango del coeficiente = valor actual + rango del Δ
```

**Primal de Min:** la optimalidad es $c_j - z_j \geq 0$. No memorices otra fórmula:
planteá la desigualdad y despejá. Para $c_k$ no básica queda $\Delta c_k \geq -(c_k-z_k)$;
para $c_k$ básica se **invierten** los grupos (el máximo sale de $y_{kj}<0$, el mínimo de
$y_{kj}>0$). El rango de $b_k$ no cambia: la factibilidad es $x_B \geq 0$ en los dos.

## Regla del 100% (varios cambios a la vez)

```text
rₖ = |Δₖ| / |variación máxima permitida EN ESE SENTIDO|
Σ rₖ ≤ 100%  → la base sigue óptima
Σ rₖ > 100%  → la regla NO DICE NADA: hay que recalcular (no es criterio de rechazo)
los cⱼ y los bᵢ se suman POR SEPARADO, nunca en la misma cuenta
```

## Precios sombra (= solución del dual)

$u = c_B B^{-1}$. En la tabla, fila $c_j - z_j$, bajo la columna de cada restricción:

```text
columna de HOLGURA (restricción ≤)  →  uᵢ = −(cj − zj)
columna de EXCESO  (restricción ≥)  →  uᵢ = +(cj − zj)
(vale en Max y en Min: la columna de exceso es la de holgura cambiada de signo)
```

- $u_i$ = cuánto cambia $z^*$ por **una unidad más** de $b_i$. Es lo máximo que conviene
  pagar por esa unidad. **Vale solo dentro del rango de $b_i$**, y no es el precio de mercado.
- **Holguras complementarias:** $\text{holgura}_i \cdot u_i = 0$ y $x_j \cdot s_j = 0$.
  Si sobra recurso, $u_i = 0$; si $u_i \neq 0$, el recurso está agotado. Si $x_j > 0$, su
  restricción dual cierra con igualdad. Un renglón con los dos lados $\neq 0$ es error.
- **LINDO:** `DUAL PRICES` = cuánto *mejora* el funcional. En Max coincide con $u_i$;
  en **Min viene con el signo opuesto**. `REDUCED COST` = costo reducido en valor absoluto.

| | Costo reducido | Costo marginal / precio sombra |
|---|---|---|
| Es de | una **variable** $x_j$ | una **restricción** (recurso) |
| Se lee en | $c_j - z_j$ de la columna de $x_j$ | $c_j - z_j$ de la columna de la **holgura** |
| Dice | cuánto le falta a $c_j$ para que $x_j$ entre | cuánto vale una unidad más del recurso |
| Vale 0 si | $x_j$ es **básica** | la restricción es **pasiva** (sobra) |

## Construcción del dual

```text
Max ↔ Min  ·  restricción i → variable uᵢ  ·  variable xⱼ → restricción j
bᵢ → coeficiente de uᵢ en el funcional  ·  cⱼ → lado derecho de la restricción j (CON SU SIGNO)
la columna de xⱼ en el primal es la fila j del dual (se traspone A)
```

| Primal **Max** | Dual (Min) | | Primal **Min** | Dual (Max) |
|---|---|---|---|---|
| restr. $\leq$ | $u_i \geq 0$ | | restr. $\geq$ | $y_i \geq 0$ |
| restr. $\geq$ | $u_i \leq 0$ | | restr. $\leq$ | $y_i \leq 0$ |
| restr. $=$ | $u_i$ **libre** | | restr. $=$ | $y_i$ **libre** |
| $x_j \geq 0$ | restr. $\geq$ | | $x_j \geq 0$ | restr. $\leq$ |
| $x_j$ libre | restr. $=$ | | $x_j$ libre | restr. $=$ |

- **Regla mnemotécnica:** la restricción "natural" (la de la forma canónica: $\leq$ en Max,
  $\geq$ en Min) da variable $\geq 0$; la "rara" da $\leq 0$; la igualdad da **libre**.
- **Alternativa:** llevar antes el primal a forma canónica ($\geq$ por $-1$; $=$ partida en
  dos). Todas las duales quedan $\geq 0$ y el dual final es el mismo. **Elegí un camino y
  sostenelo.**
- **Siempre escribí el signo de TODAS las variables duales.** Si no decís nada, se asume
  $\geq 0$: omitir "libre" cambia el problema.
- No hace falta forma estándar para dualizar: nada de holguras ni de $b_i \geq 0$.
- **Control:** $W^* = z^*$. Si el primal es **no factible**, el dual es no acotado o no
  factible (5a); si el primal es **no acotado**, el dual es no factible (5d). Ahí el control
  no aplica.

## Simplex dual (cuando el cambio sale del rango)

```text
arranca ÓPTIMO pero NO FACTIBLE  (cj−zj ok, alguna x_B < 0)
SALE    la básica más negativa → fila pivote r
ENTRA   min { (cj−zj)/y_rj : y_rj < 0 }   ·  sin ningún y_rj < 0 → problema NO FACTIBLE
se usa  bᵢ fuera de rango  ·  restricción nueva que el óptimo no cumple
```

## Errores típicos (los que salieron practicando)

1. **Mezclar convenciones** en el dual: funcional con el $b_i$ multiplicado por $-1$ y
   restricciones sin multiplicar (5a).
2. Poner el sentido de las restricciones duales al azar: con $x_j \geq 0$, dual de Max →
   **todas $\geq$**, dual de Min → **todas $\leq$** (5a, 5c).
3. Dejar Min cuando el primal es Min: **el dual de un Min es Max** (5c).
4. Omitir "$u_i$ libre" en una igualdad (5d).
5. Para $\Delta b_k$ usar la columna de la **variable** $x_k$ en vez de la de la **holgura**
   de la restricción $k$. En el Ej. 1, $b_3$ va con $A_6$ (`SLK 4`), no con $A_3$ (1d).
6. En $c_k - z_k'$ usar un $c$ que no es: si cambia la columna $A_k$, el $c_k$ **sigue siendo
   el original** (1e).
7. Leer $c_j - z_j = 0$ como "entra": no mejora, es **óptimo alternativo**.
8. Extrapolar el precio sombra fuera del rango de $b_i$.

## Mapa de la práctica

| Ej. | Qué es | Herramienta |
|---|---|---|
| 1 | Tabla de LINDO, 9 incisos | cuadro maestro completo + regla del 100% |
| 2 | Reconstruir la tabla final sin iterar | $B^{-1}$ a mano, $x_B = B^{-1}b$, $Y = B^{-1}N$ |
| 3 | Salida de LINDO con una restricción $\geq$ | dual completo, holguras complementarias, **columna de exceso con signo cambiado** |
| 4 | Minimización con LINDO | todo con signos de Min; `DUAL PRICES` con signo opuesto |
| 5 | Construir cuatro duales | tabla de construcción (con $=$, con $\geq$, con Min) |
| 6 | Tabla con incógnitas | $x_B = B^{-1}b$ leído al revés, $u = c_B B^{-1}$ |
| 7 | Precios sombra sin Simplex | resolver el dual (2 variables) por método gráfico |
| 8–9 | Parametrización | **fuera de alcance** |
