# Investigación Operativa — Simulacro del recuperatorio

> **Simulacro completo, con práctica y teoría.** Mismo estilo que el parcial, pero con preguntas distintas: región no acotada, tabla óptima dada, rangos de $b$, producto nuevo, dual y stock con demanda aleatoria. Tiempo sugerido: 2 h 30 min (práctica 1 h 45 min, teoría 45 min). Sólo la hoja de fórmulas. Elegí **una sola** opción por pregunta ("el valor más cercano"). Los números se verificaron por cálculo exacto.

# Parte A — Práctica

## Ejercicio 1 — Método gráfico

$$\text{Min } W = 4x_1 + 3x_2 \quad \text{s.a.} \quad
\begin{cases}
① \;\; x_1 + x_2 \geq 8\\
② \;\; 2x_1 + x_2 \geq 10\\
③ \;\; x_1 \leq 6\\
x_1, x_2 \geq 0
\end{cases}$$

**1)** ¿Cómo es la región factible y qué tipo de solución tiene el problema?

- a) La región es acotada y la solución óptima es única.
- b) La región no es acotada, pero la solución óptima es única y finita.
- c) La región no es acotada y la solución es no acotada.
- d) La región no es acotada y hay óptimos alternativos.
- e) La región es vacía: el problema no es factible.

**2)** ¿Cuáles son las coordenadas de la solución óptima?

- a) $(0;\ 10)$
- b) $(6;\ 2)$
- c) $(5;\ 0)$
- d) $(2;\ 6)$
- e) $(0;\ 8)$

**3)** ¿Cuál es el costo óptimo $W^*$?

- a) 26
- b) 30
- c) 24
- d) 20
- e) 32

**4)** ¿Cuál es el valor de la variable de exceso de la restricción ② en el punto $(6;\ 2)$?

- a) −4
- b) 0
- c) 4
- d) 14
- e) 10

**5)** Si con las mismas restricciones el objetivo fuera $\text{Max } Z = 4x_1 + 3x_2$, ¿qué pasaría?

- a) El óptimo estaría en $(6;\ 2)$.
- b) El óptimo estaría en $(0;\ 10)$.
- c) Habría óptimos alternativos sobre la restricción ③.
- d) El problema no sería factible.
- e) La solución sería no acotada.

## Ejercicio 2 — La fábrica de muebles: tabla óptima, sensibilidad y dual

Una fábrica produce mesas ($x_1$), sillas ($x_2$) y estantes ($x_3$), y quiere maximizar la ganancia en pesos.

$$\text{Max } Z = 80x_1 + 30x_2 + 60x_3 \quad \text{s.a.} \quad
\begin{cases}
① \;\; 2x_1 + 4x_2 + x_3 \leq 660 & \text{(horas de corte)}\\
② \;\; 2x_1 + 2x_2 + 3x_3 \leq 1080 & \text{(horas de pintura)}\\
③ \;\; x_3 \geq 170 & \text{(contrato mínimo de estantes)}\\
x_j \geq 0
\end{cases}$$

$x_4$ y $x_5$ son las holguras de ① y ②, $x_6$ el exceso de ③ y $x_7$ su ficticia. Ésta es la **tabla óptima**:

| $C_B$ | Base | $A_1$ (80) | $A_2$ (30) | $A_3$ (60) | $A_4$ (0) | $A_5$ (0) | $A_6$ (0) | $A_7$ ($-M$) | $X_i$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 80 | $A_1$ | 1 | 5/2 | 0 | 3/4 | −1/4 | 0 | 0 | 225 |
| 60 | $A_3$ | 0 | −1 | 1 | −1/2 | 1/2 | 0 | 0 | 210 |
| 0 | $A_6$ | 0 | −1 | 0 | −1/2 | 1/2 | 1 | −1 | 40 |
| | $z_j$ | 80 | 140 | 60 | 30 | 10 | 0 | 0 | |
| | $c_j - z_j$ | 0 | −110 | 0 | −30 | −10 | 0 | $-M$ | |

**1)** ¿Cuáles son la solución óptima y el valor de $Z^*$?

- a) $S^* = (225;\ 0;\ 210;\ 0;\ 0;\ 40)$, $Z^* = 30.600$
- b) $S^* = (225;\ 0;\ 210;\ 0;\ 0;\ 40)$, $Z^* = 31.000$
- c) $S^* = (0;\ 225;\ 210;\ 0;\ 0;\ 40)$, $Z^* = 30.600$
- d) $S^* = (225;\ 0;\ 170;\ 0;\ 0;\ 0)$, $Z^* = 28.200$
- e) $S^* = (225;\ 0;\ 210;\ 30;\ 10;\ 40)$, $Z^* = 30.600$

**2)** ¿Qué tipo de solución es?

- a) Con óptimos alternativos, porque $x_6$ es básica.
- b) Degenerada, porque una holgura vale 0.
- c) Única, porque todas las no básicas tienen $c_j - z_j < 0$.
- d) Con óptimos alternativos, porque $c_6 - z_6 = 0$.
- e) No factible, porque la columna de la ficticia no es nula.

**3)** ¿En qué rango puede variar la disponibilidad de horas de corte ($b_1$) sin que cambie la base óptima?

- a) $360 \leq b_1 \leq 1080$
- b) $580 \leq b_1 \leq 740$
- c) $-300 \leq b_1 \leq 80$
- d) $660 \leq b_1 \leq 740$
- e) $360 \leq b_1 \leq 740$

**4)** Si se consiguen 40 horas más de pintura ($b_2 = 1120$), ¿cómo queda el plan?

- a) $x_1 = 225$, $x_3 = 210$, $Z^* = 31.000$
- b) $x_1 = 215$, $x_3 = 230$, $Z^* = 31.000$
- c) $x_1 = 235$, $x_3 = 190$, $Z^* = 30.200$
- d) Cambia la base óptima: hay que volver a iterar.
- e) $x_1 = 215$, $x_3 = 230$, $Z^* = 30.600$

**5)** Se evalúa fabricar bancos: cada uno usa 1 hora de corte y 2 de pintura, y deja \$ 45. ¿Conviene?

- a) Sí, porque deja una ganancia positiva.
- b) Sí, porque su $c - z = +5$.
- c) Es indiferente: su $c - z = 0$.
- d) No: los recursos que usa valen \$ 50 en el plan actual, más que los \$ 45 que deja.
- e) No, porque no quedan horas libres de corte.

**6)** ¿Hasta cuánto puede aumentar la ganancia de las sillas ($c_2$) sin que convenga fabricarlas?

- a) $c_2 \leq 140$
- b) $c_2 \leq 110$
- c) $30 \leq c_2 \leq 140$
- d) $c_2 \geq 140$
- e) $c_2 \leq -80$

**7)** ¿En qué rango puede variar la ganancia de las mesas ($c_1$) sin que cambie el plan óptimo?

- a) $[36;\ 120]$
- b) $[80;\ 120]$
- c) $[40;\ 120]$
- d) $[-40;\ 40]$
- e) $[0;\ 120]$

**8)** En el dual, ¿cuánto valen $u_2$ y el exceso de la restricción dual asociada a las sillas ($x_2$)?

- a) $u_2 = 30$ y exceso dual $= 110$
- b) $u_2 = 10$ y exceso dual $= 110$
- c) $u_2 = 10$ y exceso dual $= 0$
- d) $u_2 = 0$ y exceso dual $= 110$
- e) $u_2 = 10$ y exceso dual $= -110$

## Ejercicio 3 — Stock con demanda aleatoria

Una ferretería vende en promedio **40 unidades por día** de un artículo, con un desvío estándar diario de **6 unidades** (demanda normal, días independientes). Trabaja **300 días al año**. El proveedor tarda **9 días** en entregar. Cada unidad cuesta **\$ 25**, cada pedido **\$ 150** y la tasa de mantenimiento es **20 % anual**. Las existencias se controlan permanentemente y se acepta un **riesgo de faltante del 5 %**.

**1)** ¿Cuál es el lote óptimo de compra?

- a) 600 unidades
- b) 1.200 unidades
- c) 1.697 unidades
- d) 849 unidades
- e) 49 unidades

**2)** ¿Cuál es el desvío estándar de la demanda durante el plazo de entrega?

- a) 54 unidades
- b) 18 unidades
- c) 6 unidades
- d) 108 unidades
- e) 2 unidades

**3)** ¿Cuál es el stock de seguridad?

- a) 30 unidades
- b) 29 unidades
- c) 89 unidades
- d) 18 unidades
- e) 50 unidades

**4)** ¿Cuál es el punto de pedido?

- a) 360 unidades
- b) 30 unidades
- c) 389 unidades
- d) 420 unidades
- e) 390 unidades

**5)** ¿Cuál es el costo anual de mantener el stock de seguridad?

- a) \$ 750
- b) \$ 30
- c) \$ 150
- d) \$ 148
- e) \$ 7,50

**6)** Si el proveedor pasara a tardar 36 días (cuatro veces más), ¿qué pasaría con el stock de seguridad?

- a) Se cuadruplicaría.
- b) Se duplicaría.
- c) No cambiaría.
- d) Se reduciría a la mitad.
- e) Se multiplicaría por 16.

# Parte B — Teoría

**1)** Un problema de Min con restricciones $\geq$ tiene región factible no acotada. Entonces:

- a) La solución es necesariamente no acotada.
- b) No tiene solución óptima.
- c) Puede tener un óptimo finito: la solución sólo es no acotada si el objetivo mejora indefinidamente hacia donde se abre la región.
- d) Tiene necesariamente óptimos alternativos.
- e) La región tiene que ser vacía.

**2)** Una solución básica factible de un PL con $m$ restricciones es degenerada cuando:

- a) alguna variable básica vale cero, es decir, tiene menos de $m$ componentes positivas.
- b) alguna variable no básica tiene $c_j - z_j = 0$ en la tabla óptima.
- c) tiene menos de $n - m$ componentes positivas.
- d) alguna variable básica tiene $c_j - z_j = 0$.
- e) todas sus variables básicas son positivas.

**3)** Si la función objetivo de un PL alcanza el óptimo en dos puntos extremos distintos, entonces también lo alcanza en:

- a) cualquier combinación lineal de ellos.
- b) ningún otro punto.
- c) cualquier punto interior de la región factible.
- d) toda combinación lineal convexa de ellos, es decir, en todo el segmento que los une.
- e) sólo en el punto medio del segmento.

**4)** Se llega a la condición de óptimo y en la base quedó una variable ficticia con valor 4. Entonces:

- a) La solución es óptima y degenerada.
- b) El problema no es factible: la región factible es vacía.
- c) Hay óptimos alternativos.
- d) La solución es óptima, porque la ficticia no aporta al funcional.
- e) Hay que tomar M más grande y volver a resolver.

**5)** En la tabla de un Max, la solución es no acotada cuando:

- a) existe un $c_j - z_j > 0$ y todos los $y_{ij}$ de esa columna son $\leq 0$.
- b) existe un $c_j - z_j > 0$ y todos los $y_{ij}$ de esa columna son $< 0$.
- c) todos los $c_j - z_j$ son $\leq 0$.
- d) una no básica tiene $c_j - z_j = 0$.
- e) alguna básica vale cero.

**6)** ¿Dónde se lee $B^{-1}$ en la tabla óptima?

- a) Debajo de las columnas de las variables básicas de la tabla óptima.
- b) En la columna de los valores $X$.
- c) Debajo de las columnas que formaban la identidad en la tabla inicial (holguras y ficticias).
- d) En la fila $c_j - z_j$.
- e) En la fila $z_j$ de las variables de decisión.

**7)** En la tabla **óptima** de un Max, una variable **no básica** tiene $c_j - z_j = 0$. Entonces:

- a) La solución es degenerada.
- b) Hay soluciones óptimas alternativas.
- c) La solución es no acotada.
- d) Hay que seguir iterando.
- e) El problema no es factible.

**8)** Cambia un término independiente $b_k$, y el cambio queda dentro de su rango. Entonces:

- a) No cambia nada: ni la base, ni los valores, ni $z^*$.
- b) Cambia la base óptima.
- c) Cambian los $c_j - z_j$ de las no básicas.
- d) La base sigue siendo la misma, pero cambian los valores de las básicas, y $z^*$ cambia en $u_k \cdot \Delta b_k$.
- e) Cambian los valores, pero $z^*$ no cambia.

**9)** En un problema de **mínimo**, ¿qué signo tiene el valor implícito de una restricción $\leq$?

- a) $u \leq 0$: aflojarla (subir su $b$) nunca hace subir el costo.
- b) $u \geq 0$, igual que en un Max.
- c) Es siempre nulo.
- d) Es libre.
- e) $u \geq 0$, porque toda restricción es un recurso.

**10)** En un Max, la restricción de horas tiene precio sombra $u = 15$ \$/h. ¿Cuál es correcta?

- a) Por cada hora que sobra, la ganancia baja \$ 15.
- b) Conviene comprar horas extra mientras cuesten más de \$ 15.
- c) El valor vale para cualquier cantidad de horas adicionales.
- d) La restricción no es activa.
- e) Conviene comprar horas extra si cuestan menos de \$ 15, mientras $b$ siga dentro de su rango.

**11)** Si el primal tiene solución no acotada, el dual:

- a) también tiene solución no acotada.
- b) tiene óptimos alternativos.
- c) no tiene soluciones factibles.
- d) tiene una solución degenerada.
- e) tiene óptimo finito con el mismo valor.

**12)** Al construir el dual, una restricción de **igualdad** del primal da:

- a) una restricción de igualdad en el dual.
- b) una variable dual libre (sin restricción de signo).
- c) una variable dual $\geq 0$.
- d) una variable dual $\leq 0$.
- e) nada: se descarta.

**13)** Un transporte balanceado tiene 4 orígenes y 5 destinos. Una solución básica tiene, como máximo:

- a) 20 variables positivas.
- b) 9 variables positivas.
- c) 12 variables positivas.
- d) 8 variables positivas.
- e) 5 variables positivas.

**14)** En un transporte, la demanda total supera a la oferta total. ¿Cómo se balancea?

- a) Con un origen ficticio de costo 0; lo que envía es demanda que queda sin cubrir.
- b) Con un destino ficticio de costo 0; lo que recibe es capacidad ociosa.
- c) Con un origen ficticio de costo M.
- d) No hace falta balancearlo.
- e) Se reducen las demandas en la misma proporción.

**15)** En un problema entero de **máximo**, el óptimo del PL relajado es:

- a) siempre igual al óptimo entero.
- b) una cota inferior del óptimo entero.
- c) una cota superior del óptimo entero.
- d) siempre un punto entero.
- e) el óptimo entero redondeado.

**16)** Un árbol de expansión de una red conexa con 8 nodos tiene:

- a) 8 arcos y ningún ciclo.
- b) 7 arcos y ningún ciclo.
- c) 7 arcos y un ciclo.
- d) 9 arcos.
- e) la cantidad de arcos que minimiza la distancia desde el origen.

**17)** En el modelo con consumo durante el ingreso (velocidad de ingreso $V$, demanda $D$):

- a) debe ser $V < D$ y el lote es menor que el del modelo básico.
- b) debe ser $V = D$ para que el modelo tenga sentido.
- c) el pico de stock es $Q$.
- d) el lote es menor que el del básico porque el stock se mantiene más tiempo.
- e) debe ser $D < V$ y el lote es mayor que el del modelo básico.

**18)** ¿Un riesgo de faltante del 3 % es lo mismo que un IPF del 97 %?

- a) Sí, son dos formas de decir lo mismo.
- b) Sí, porque RF + IPF siempre suman 100 %.
- c) No: el RF es la fracción de la demanda entregada desde el stock.
- d) No: el RF es la probabilidad de faltante por ciclo y el IPF es la fracción de la demanda entregada directamente desde el stock.
- e) No: el IPF siempre es menor que 1 − RF.

**19)** En el sistema de revisión periódica, el stock de seguridad se calcula sobre:

- a) $T + LT$, porque lo que se pide hoy tiene que cubrir hasta que llegue el pedido de la próxima revisión.
- b) $LT$, igual que en punto de pedido.
- c) $T$, el período entre revisiones.
- d) $T \cdot LT$.
- e) $T - LT$.

**20)** En los modelos multiartículo con Lagrange, al aumentar $\lambda$:

- a) los lotes siempre se achican.
- b) los lotes siempre se agrandan.
- c) con restricción de espacio los lotes se achican, y con restricción de tiempo de preparación se agrandan.
- d) con restricción de espacio los lotes se agrandan, y con preparación se achican.
- e) los lotes no cambian; sólo cambia el costo.

# Hoja de respuestas

| Ej. 1 | 1 | 2 | 3 | 4 | 5 | | | |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Letra | | | | | | | | |

| Ej. 2 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Letra | | | | | | | | |

| Ej. 3 | 1 | 2 | 3 | 4 | 5 | 6 | | |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Letra | | | | | | | | |

| Teoría | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Letra | | | | | | | | | | |

| Teoría | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Letra | | | | | | | | | | |
