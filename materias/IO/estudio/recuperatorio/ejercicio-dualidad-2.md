# Ejercicio de dualidad 2 — resolver por el dual

Una fábrica produce tres artículos: **A**, **B** y **C**. Por unidad, dejan una ganancia de \$ 6, \$ 5 y \$ 4 (en miles), respectivamente.

- **Máquina:** cada unidad de A usa 2 horas, cada una de B usa 1 hora y cada una de C usa 1 hora. Hay **100 horas** de máquina por semana.
- **Mano de obra:** cada unidad de A usa 1 hora, cada una de B usa 1 hora y cada una de C usa 2 horas. Hay **80 horas** de mano de obra por semana.

$x_1$, $x_2$, $x_3$: unidades de A, B y C a fabricar por semana.

$$\text{Max } z = 6x_1 + 5x_2 + 4x_3 \quad \text{s.a.} \quad
\begin{cases}
① \;\; 2x_1 + x_2 + x_3 \leq 100 & \text{(horas de máquina)}\\
② \;\; x_1 + x_2 + 2x_3 \leq 80 & \text{(horas de mano de obra)}\\
x_1, x_2, x_3 \geq 0
\end{cases}$$

El primal tiene **tres variables**, así que no se puede resolver por método gráfico. Su dual tiene **dos**. En este ejercicio no se usa el simplex: se resuelve el dual gráficamente y se recupera el primal con holguras complementarias.

## Consignas

**a) Armar el dual.** Escribí el dual completo. Indicá qué restricción del primal genera cada $u_i$, qué variable del primal genera cada restricción dual, y el signo de cada $u_i$.

**b) Interpretación económica.** ¿Qué representan $u_1$ y $u_2$? ¿Qué dice, en palabras, cada restricción del dual? Pensá en alguien que quiere alquilarle a la fábrica las horas de máquina y de mano de obra.

**c) Resolver el dual por método gráfico.**

1. Dibujá las tres restricciones del dual en el plano $(u_1; u_2)$, por forma segmentaria.
2. Marcá la región factible. Cuidado con el sentido de las desigualdades.
3. Hallá los vértices, resolviendo los sistemas de 2×2 que hagan falta. Descartá los cruces que no cumplan las tres restricciones.
4. Evaluá $w$ en cada vértice e indicá el óptimo $u^*$ y $w^*$.

**d) Recuperar el primal con holguras complementarias.**

1. Con $u^*$, calculá la holgura (o exceso) de cada restricción dual. ¿Cuál no se cumple justo? ¿Qué te dice eso de la variable primal correspondiente?
2. Con los $u_i^*$ distintos de cero, ¿qué restricciones del primal se cumplen justo?
3. Armá el sistema que queda y resolvelo: obtené $x_1^*$, $x_2^*$, $x_3^*$ y las holguras $x_4^*$, $x_5^*$.
4. Escribí $S^*$ del primal y verificá que $z^* = w^*$.

**e) El artículo que no se fabrica.**

1. ¿Cuál de los tres artículos no se fabrica?
2. Explicá por qué, comparando lo que deja con lo que valen los recursos que consume.
3. ¿Cuál es su costo reducido?
4. ¿A partir de qué ganancia por unidad convendría fabricarlo? ¿Qué pasaría con la solución si deja **exactamente** ese valor?

**f) Precios sombra.**

1. ¿Cuánto vale una hora más de máquina y cuánto una hora más de mano de obra?
2. Si un proveedor ofrece horas extra de mano de obra a \$ 3 (miles) cada una, ¿conviene comprarlas? Suponé que la cantidad está dentro del rango.
3. ¿Y horas extra de máquina a \$ 3?

**g) Teoría.** Si al resolver el dual por método gráfico la recta de isocosto hubiera sido paralela a uno de los lados del óptimo, con infinitas soluciones duales, ¿qué podrías decir de la solución del primal?
