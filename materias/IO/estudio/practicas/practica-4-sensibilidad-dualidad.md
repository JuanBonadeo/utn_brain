# IO — Práctica 4: Análisis de sensibilidad, dualidad y parametrización

Guía de la Práctica 4 (`PL4UTN.pdf`). Contrastada con la resolución oficial de la cátedra
(`PL4UTNresol.pdf`, Farbman) y verificada por cálculo exacto con fracciones (inversa de la
base, enumeración de bases, rangos de sensibilidad).

**Estado:** Ejercicio 1 resuelto. Ejercicios 2 a 9 pendientes.

---

# Parte 1 — El herramental. Todo sale de $B^{-1}$

La práctica 4 no pide volver a iterar el Simplex. Pide **leer la tabla óptima** y contestar
qué pasa si cambia un dato. Todo se apoya en una sola matriz: la inversa de la base óptima.

## Dónde está $B^{-1}$ en la tabla

$B^{-1}$ **ya está impresa** en la tabla final: son las columnas de las variables que
formaban la identidad en la tabla inicial (las holguras, en el orden de las restricciones).

```
  tabla inicial            tabla final
  columna de x4 = e1  -->  columna de x4 = primera columna de B^-1
  columna de x5 = e2  -->  columna de x5 = segunda  columna de B^-1
  columna de x6 = e3  -->  columna de x6 = tercera  columna de B^-1
```

Ojo con las restricciones $\geq$ o $=$: ahí la columna que estaba en la identidad es la
**ficticia**, no la de exceso. La columna de exceso vale $-B^{-1}e_i$, o sea $B^{-1}$
cambiada de signo.

> **Nomenclatura de LINDO.** LINDO numera las filas contando la función objetivo como
> fila 1. Entonces `SLK 2` es la holgura de la **restricción 1**, `SLK 3` la de la
> restricción 2, etc. La fila `ART` (o `1)`) no es $c_j - z_j$ sino **$z_j - c_j$**: en un
> Max óptimo aparece toda $\geq 0$. Para pasar al criterio de la cátedra hay que cambiarle
> el signo.

## Las cinco fórmulas

$$
x_B = B^{-1}b \qquad
Y_j = B^{-1}A_j \qquad
z_j = c_B Y_j \qquad
u = c_B B^{-1} \qquad
z^* = c_B x_B
$$

$u = c_B B^{-1}$ es el **vector de valores implícitos** (precios sombra, costos marginales,
solución del dual). Aparece en la fila $z_j - c_j$ debajo de las columnas de las holguras.

## Qué se pregunta y con qué se contesta

| Cambia… | Variable afectada | Condición que hay que revisar | Fórmula |
|---|---|---|---|
| $c_j$ de una **no básica** | solo esa columna | $c_j + \Delta c_j - z_j \leq 0$ | $\Delta c_j \leq -(c_j - z_j)$ |
| $c_j$ de una **básica** (fila $r$) | **todos** los $c_j - z_j$ | $(c_j - z_j) - \Delta c_r\, y_{rj} \leq 0\ \forall j \notin I_B$ | $\max\limits_{y_{rj}>0}\frac{c_j-z_j}{y_{rj}} \leq \Delta c_r \leq \min\limits_{y_{rj}<0}\frac{c_j-z_j}{y_{rj}}$ |
| $b_i$ | $x_B$ (la **factibilidad**) | $x_B + \Delta b_i\, B^{-1}_{\cdot i} \geq 0$ | $\max\limits_{r_{ki}>0}\frac{-x^*_k}{r_{ki}} \leq \Delta b_i \leq \min\limits_{r_{ki}<0}\frac{-x^*_k}{r_{ki}}$ |
| $A_j$ de una **no básica** | esa columna | recalcular $Y_j = B^{-1}A_j$, $z_j = c_B Y_j$ | óptima si $c_j - z_j \leq 0$ |
| **nueva variable** | una columna nueva | ídem anterior | conviene si $c_{n} - z_{n} > 0$ |
| **nueva restricción** | factibilidad | evaluar el $x^*$ actual en la restricción | si la cumple, no pasa nada |

Dos asimetrías que hay que tener clarísimas, porque es donde se pierde el punto:

- **Cambiar $c_j$ nunca rompe la factibilidad**, rompe la *optimalidad*. Si el $\Delta c$
  cae dentro del rango, $x^*$ **no se mueve** y $z^*$ cambia solo si la variable tocada es
  básica ($z^{*\prime} = z^* + \Delta c_r\, x^*_r$).
- **Cambiar $b_i$ nunca rompe la optimalidad**, rompe la *factibilidad*. Si el $\Delta b$
  cae dentro del rango, la **base** no cambia pero $x^*$ **sí se mueve**, y
  $z^{*\prime} = z^* + u_i\, \Delta b_i$.

## Regla del 100%

Sirve cuando cambian **varios coeficientes a la vez**. Los rangos de la tabla de arriba
valen de a un cambio por vez; si se mueven dos o más, se calcula para cada uno la
**fracción del rango permitido que se consume**:

$$
r_k = \frac{|\Delta_k|}{|\text{máxima variación permitida en ese sentido}|}
$$

Si $\sum r_k \leq 100\%$, la conclusión se mantiene (base óptima intacta). Si se pasa del
100%, la regla **no dice nada**: hay que recalcular, no es que necesariamente cambie.

---

# Parte 2 — Ejercicio 1

## Enunciado

$$
\text{Max } z = 2x_1 - x_2 + x_3
$$

$$
\begin{aligned}
3x_1 + x_2 + x_3 &\leq 60 \\
x_1 - x_2 + 2x_3 &\leq 10 \\
x_1 + x_2 - x_3 &\leq 20 \\
x_j &\geq 0
\end{aligned}
$$

$x_j$ = cantidades a fabricar de tres artículos; $c_j$ sus contribuciones marginales;
$b_i$ las unidades disponibles de tres recursos.

Tabla óptima de LINDO (traducida: `SLK 2` $\to x_4$, `SLK 3` $\to x_5$, `SLK 4` $\to x_6$,
y la fila `ART` con el signo dado vuelta para tener $c_j - z_j$):

```
  cB   base    A1    A2     A3     A4     A5     A6      X
  ---------------------------------------------------------
   0    A4      0     0      1      1     -1     -2     10
   2    A1      1     0    1/2      0    1/2    1/2     15
  -1    A2      0     1   -3/2      0   -1/2    1/2      5
  ---------------------------------------------------------
      cj-zj     0     0   -3/2      0   -3/2   -1/2   z=25
```

La base óptima es $I_B = \{A_4, A_1, A_2\}$ y su inversa se lee en las columnas
$A_4, A_5, A_6$:

$$
B^{-1} = \begin{pmatrix} 1 & -1 & -2 \\ 0 & 1/2 & 1/2 \\ 0 & -1/2 & 1/2 \end{pmatrix}
\qquad
x_B = B^{-1}b = \begin{pmatrix} 1 & -1 & -2 \\ 0 & 1/2 & 1/2 \\ 0 & -1/2 & 1/2 \end{pmatrix}
\begin{pmatrix} 60 \\ 10 \\ 20 \end{pmatrix} = \begin{pmatrix} 10 \\ 15 \\ 5 \end{pmatrix}
$$

$$
S^* = \begin{pmatrix} 15 \\ 5 \\ 0 \\ 10 \\ 0 \\ 0 \end{pmatrix}
\qquad z^* = 2(15) - 1(5) + 1(0) = 25
$$

---

## a) Costo marginal de cada recurso

$$
u = c_B B^{-1} = (0,\ 2,\ -1)
\begin{pmatrix} 1 & -1 & -2 \\ 0 & 1/2 & 1/2 \\ 0 & -1/2 & 1/2 \end{pmatrix}
= (0,\ 3/2,\ 1/2)
$$

Que es exactamente lo que ya estaba en la fila $z_j - c_j$ bajo $A_4, A_5, A_6$.

| Recurso | $u_i$ | Holgura | Lectura |
|---|---|---|---|
| 1 ($b_1 = 60$) | $0$ | $x_4 = 10 > 0$ | **Sobra**. Restricción pasiva, no limita. Una unidad más no agrega nada: no se pagaría por ella. |
| 2 ($b_2 = 10$) | $1{,}5$ | $x_5 = 0$ | **Saturado**. Cada unidad extra del recurso 2 aumenta $z$ en \$1,50. Es el precio máximo que conviene pagar por una unidad adicional. |
| 3 ($b_3 = 20$) | $0{,}5$ | $x_6 = 0$ | **Saturado**. Cada unidad extra aumenta $z$ en \$0,50. |

Nota: es la relación de holgura complementaria — recurso con sobrante $\Rightarrow$ precio
sombra nulo; precio sombra positivo $\Rightarrow$ recurso agotado. Y el valor vale **solo
dentro del rango de $b_i$** calculado en (d): no se puede extrapolar linealmente para
siempre.

---

## b) $c_3$ se incrementa en una unidad

$x_3$ es **no básica**. Al cambiar el $c_j$ de una no básica se afecta un solo
$c_j - z_j$; los demás quedan igual porque $c_B$ no cambió.

$$
c_3 + \Delta c_3 - z_3 \leq 0 \;\Rightarrow\; \Delta c_3 \leq -(c_3 - z_3) = -(-3/2) = 3/2
$$

Es decir $c_3 \leq 1 + 1{,}5 = 2{,}5$.

Como $\Delta c_3 = 1 \leq 1{,}5$, **no cambia nada**: $x^*$ y $z^*$ se mantienen. El nuevo
$c_3 - z_3 = 2 - 5/2 = -1/2 \leq 0$, sigue siendo no rentable producir el artículo 3.

Interpretación: al artículo 3 le falta \$1,50 de contribución para que valga la pena
fabricarlo. Un aumento de \$1 no alcanza.

---

## c) Rango de variación de $c_2$

$x_2$ es **básica** (tercera fila de la base). Acá sí se corren **todos** los $c_j - z_j$,
porque $c_B$ cambia y por lo tanto cambia todo $z_j = c_B Y_j$. La fila de $x_2$ es la que
manda:

$$
(c_j - z_j)' = (c_j - z_j) - \Delta c_2\, y_{2j} \leq 0 \quad \forall j \notin I_B
$$

| $j$ no básica | $c_j - z_j$ | $y_{2j}$ (fila de $x_2$) | Condición |
|---|---|---|---|
| $A_3$ | $-3/2$ | $-3/2$ | $y < 0 \Rightarrow \Delta c_2 \leq \frac{-3/2}{-3/2} = 1$ |
| $A_5$ | $-3/2$ | $-1/2$ | $y < 0 \Rightarrow \Delta c_2 \leq \frac{-3/2}{-1/2} = 3$ |
| $A_6$ | $-1/2$ | $1/2$ | $y > 0 \Rightarrow \Delta c_2 \geq \frac{-1/2}{1/2} = -1$ |

$$
\max_{y_{2j}>0} \frac{c_j - z_j}{y_{2j}} \leq \Delta c_2 \leq \min_{y_{2j}<0} \frac{c_j - z_j}{y_{2j}}
\;\Rightarrow\; -1 \leq \Delta c_2 \leq 1
$$

Como $c_2 = -1$: **$-2 \leq c_2 \leq 0$**.

Dentro de ese rango $x^*$ **no se mueve** (misma base, mismo vértice). Lo que sí cambia es
el funcional, porque $x_2 = 5 \neq 0$:

$$
z^{*\prime} = z^*_{\text{actual}} + \Delta c_2\, x_2^* = 25 + 5\,\Delta c_2
\quad\Rightarrow\quad 20 \leq z^{*\prime} \leq 30
$$

Fuera del rango, la base deja de ser óptima y hay que seguir iterando desde esa tabla.

---

## d) $b_3$ disminuye en 5 unidades

Cambiar un $b_i$ no toca la optimalidad ($c_j - z_j$ no depende de $b$), toca la
**factibilidad**. Se pide que el nuevo $x_B$ siga siendo $\geq 0$:

$$
x_B' = x_B + \Delta b_3 \cdot B^{-1}_{\cdot 3}
= \begin{pmatrix} 10 \\ 15 \\ 5 \end{pmatrix} + \Delta b_3 \begin{pmatrix} -2 \\ 1/2 \\ 1/2 \end{pmatrix} \geq 0
$$

| Fila | Condición | Resultado |
|---|---|---|
| $x_4$ | $10 - 2\Delta b_3 \geq 0$ | $\Delta b_3 \leq 5$ |
| $x_1$ | $15 + \tfrac12 \Delta b_3 \geq 0$ | $\Delta b_3 \geq -30$ |
| $x_2$ | $5 + \tfrac12 \Delta b_3 \geq 0$ | $\Delta b_3 \geq -10$ |

$$
-10 \leq \Delta b_3 \leq 5 \quad\Longleftrightarrow\quad 10 \leq b_3 \leq 25
$$

$\Delta b_3 = -5$ **está dentro del rango**, así que la base no cambia. Solo se recalculan
los valores:

$$
x_1^* = 15 - 5\cdot\tfrac12 = 12{,}5 \qquad
x_2^* = 5 - 5\cdot\tfrac12 = 2{,}5 \qquad
x_4^* = 10 - 5\cdot(-2) = 20
$$

$$
z^{*\prime} = z^* + u_3\,\Delta b_3 = 25 + 0{,}5(-5) = 22{,}5
$$

Verificación directa: $2(12{,}5) - 1(2{,}5) = 22{,}5$. ✓

Se pierden 2,5 unidades monetarias — exactamente $5$ unidades de recurso $\times$ \$0,50 de
costo marginal. Notar que el recurso 1, que sobraba, ahora sobra **más** (de 10 a 20):
menos recurso 3 $\Rightarrow$ menos producción $\Rightarrow$ menos consumo del recurso 1.

---

## e) Los coeficientes tecnológicos de $A_3$ cambian a $(1/2,\ 1,\ 1)^T$

$x_3$ es **no básica**, así que su columna no participa de $B$: cambiarla no altera
$B^{-1}$ ni la factibilidad. Solo hay que recalcular su $Y_3$ y su $c_3 - z_3$.

$$
Y_3 = B^{-1}A_3 =
\begin{pmatrix} 1 & -1 & -2 \\ 0 & 1/2 & 1/2 \\ 0 & -1/2 & 1/2 \end{pmatrix}
\begin{pmatrix} 1/2 \\ 1 \\ 1 \end{pmatrix}
= \begin{pmatrix} -5/2 \\ 1 \\ 0 \end{pmatrix}
$$

$$
z_3 = c_B Y_3 = 0(-5/2) + 2(1) + (-1)(0) = 2
\qquad c_3 - z_3 = 1 - 2 = -1 \leq 0
$$

**La solución actual sigue siendo óptima**: $x^*$ y $z^*$ no cambian. El artículo 3 pasó a
ser menos malo (antes le faltaba \$1,50, ahora \$1), pero sigue sin convenir.

> Si hubiera dado $c_3 - z_3 > 0$, no se rehace el problema: se toma esta tabla, se mete
> $A_3$ con su nuevo $Y_3$ y se itera el Simplex desde ahí.

---

## f) Introducir un nuevo artículo: $c_{n} = 1{,}5$, $A_{n} = (1,\ 2,\ 1)^T$

Mismo procedimiento que (e): es una columna nueva, no básica.

$$
Y_{n} = B^{-1}A_{n} =
\begin{pmatrix} 1 & -1 & -2 \\ 0 & 1/2 & 1/2 \\ 0 & -1/2 & 1/2 \end{pmatrix}
\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}
= \begin{pmatrix} -3 \\ 3/2 \\ -1/2 \end{pmatrix}
$$

$$
z_{n} = 0(-3) + 2(3/2) + (-1)(-1/2) = 3{,}5
\qquad c_{n} - z_{n} = 1{,}5 - 3{,}5 = -2 \leq 0
$$

**No lo pondría en producción.** La solución actual sigue siendo óptima.

**Vía dual (más rápida y es la interpretación económica que piden).** El costo implícito de
los recursos que consume una unidad del artículo nuevo es:

$$
\sum_i a_{i,n}\, u_i = 1(0) + 2(1{,}5) + 1(0{,}5) = 3{,}5
$$

Fabricar una unidad del artículo nuevo obliga a resignar \$3,50 de la producción actual
(desvía recursos escasos), y solo aporta \$1,50. Pérdida neta de \$2 por unidad. Esto es
literalmente la condición dual $\sum_i a_{ij}u_i \geq c_j$: mientras el dual se cumpla con
holgura, esa actividad no entra en la base.

---

## g) Se agrega la restricción $5x_1 - x_2 + 4x_3 \leq 20$

El test es directo: **evaluar el óptimo actual en la nueva restricción**.

$$
5(15) - 1(5) + 4(0) = 75 - 5 = 70 \;>\; 20
$$

**No la cumple.** La restricción es **activa** (limitante): recorta el poliedro justo donde
estaba el óptimo, así que $S^*$ **deja de ser factible** y sí se afecta la solución.

Cómo se sigue: se agrega la restricción a la tabla con su holgura, se expresa la fila en
términos de las no básicas (barriendo las columnas de $x_1$ y $x_2$ para que la fila quede
en forma canónica) y se reoptimiza con **Simplex dual** — la tabla queda óptima
($c_j - z_j \leq 0$) pero no factible ($x_B$ con un negativo), que es exactamente el caso
del Simplex dual.

> Si el óptimo hubiera cumplido la restricción, sería **pasiva** o redundante: no cambia
> nada, $S^*$ y $z^*$ siguen igual.

---

## h) Regla del 100% sobre los $c_j$

*(No está en el enunciado impreso; sí en la resolución de la cátedra.)*

Primero hace falta el rango de $c_1$, que es básica (segunda fila de la base). Su fila es
$y_{1j} = (1/2,\ 1/2,\ 1/2)$ para $A_3, A_5, A_6$ — **todos positivos**, así que solo hay
cota inferior:

$$
\Delta c_1 \geq \max\left(\frac{-3/2}{1/2},\ \frac{-3/2}{1/2},\ \frac{-1/2}{1/2}\right) = -1
\qquad\Rightarrow\qquad \Delta c_1 \geq -1,\ \text{sin cota superior}
$$

Tiene sentido: $x_1$ ya es rentable, hacerla más rentable nunca la saca de la base.

De (b): $\Delta c_3 \leq 1{,}5$.

**Caso: $c_1$ baja 0,2 y $c_3$ sube 0,3.**

$$
r_1 = \frac{0{,}2}{|-1|} = 0{,}2 = 20\% \qquad
r_3 = \frac{0{,}3}{1{,}5} = 0{,}2 = 20\% \qquad
r_1 + r_3 = 40\% \leq 100\%
$$

$\Rightarrow$ **$x^*$ no cambia.** El funcional sí, porque $x_1$ es básica (a $x_3 = 0$ el
cambio de $c_3$ no la toca):

$$
z^{*\prime} = (2 - 0{,}2)(15) + (-1)(5) = 27 - 5 = 22
$$

---

## i) Regla del 100% sobre los $b_i$

Rangos individuales, con las columnas de $B^{-1}$:

| $b_i$ | $B^{-1}_{\cdot i}$ | Rango |
|---|---|---|
| $b_1$ | $(1,\ 0,\ 0)^T$ | $10 + \Delta b_1 \geq 0 \Rightarrow \Delta b_1 \geq -10$, sin cota superior |
| $b_2$ | $(-1,\ 1/2,\ -1/2)^T$ | $-30 \leq \Delta b_2 \leq 10$ |
| $b_3$ | $(-2,\ 1/2,\ 1/2)^T$ | $-10 \leq \Delta b_3 \leq 5$ *(de (d))* |

$b_1$ no tiene cota superior porque el recurso 1 ya sobra: agregarle más solo engorda la
holgura.

**Caso: $b_1$ aumenta 20 y $b_2$ aumenta 5.**

$$
r_1 = \frac{20}{\infty} = 0 \qquad r_2 = \frac{5}{10} = 0{,}5 = 50\% \qquad \sum r = 50\% \leq 100\%
$$

$\Rightarrow$ **la base óptima no cambia**, y por lo tanto los valores implícitos se
mantienen:

$$
z^{*\prime} = z^* + u_1(20) + u_2(5) = 25 + 0 + 1{,}5(5) = 32{,}5
$$

---

## Qué se lleva de este ejercicio

1. **Identificar si la variable tocada es básica o no básica** antes de elegir la fórmula.
   Es el error más común: aplicar el rango de básica a una no básica.
2. **$c_j$ toca optimalidad, $b_i$ toca factibilidad.** De ahí sale todo lo demás.
3. Los precios sombra **ya están en la tabla**, bajo las columnas de las holguras. No hay
   que resolver el dual aparte para tenerlos.
4. Para **variable nueva / columna cambiada**, siempre el mismo cálculo:
   $Y_j = B^{-1}A_j \to z_j = c_B Y_j \to$ signo de $c_j - z_j$. La versión económica
   ($\sum a_{ij}u_i$ vs. $c_j$) es la misma cuenta y sale más rápido.
5. Para **restricción nueva**, evaluar el óptimo actual y listo: cumple (pasiva, nada
   cambia) o no cumple (activa, hay que reoptimizar con Simplex dual).
