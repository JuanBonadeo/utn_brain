# Investigación Operativa — Resumen para el Recuperatorio

> **IO · UTN-ISI · recuperatorio del parcial único · jueves 19/11/2026, 16:00 h, en la mesa de Investigación Operativa**
>
> Si no se aprueba, queda el globalizador del jueves 25/02/2027 (aviso de Guillermo Leale en el Classroom, 14/10).
>
> El resumen sigue el orden en que conviene estudiar. Cada tema trae su dibujo y, cuando corresponde, cómo vino en el parcial del 3/10. Las trampas están marcadas con **Ojo**. El parcial del 3/10 está resuelto entero, repartido en tres lugares: el ejercicio 1 en §2.6, el 2 en §7 y el 3 en §8.8.
>
> Para el desarrollo largo de cada tema: la wiki (`IO.md`), `estudio/parcial/banco-preguntas.md` (las 89 preguntas de teoría) y las hojas de fórmulas de `estudio/parcial/`.

## 0. Qué entra y cómo se toma

### 0.1 El alcance

En 2026 hay **un solo parcial** y entra **todo el programa**. El recuperatorio cubre lo mismo. Ninguna fuente oficial recortó el alcance, así que la prioridad sale de dos datos: lo que tomó el parcial del 3/10 y lo que repiten los exámenes de años anteriores.

| Tema | Peso para el recuperatorio | Dónde está |
|---|---|---|
| Método gráfico, modelización y formas del modelo | **Alto**: fue el ejercicio 1 del parcial | §1, §2 y §3 |
| Simplex, sensibilidad y dualidad sobre una tabla | **Muy alto**: fue el ejercicio 2 del parcial y es lo más tomado en la historia | §4 a §7 |
| Gestión de stocks | **Alto**: fue el ejercicio 3 del parcial; además, un tercio de las preguntas de teoría | §8 |
| Transporte, transbordo y asignación | Bajo: no salió en 2026 | §9 |
| Programación entera y mixta | Bajo: no salió en 2026 | §10 |
| Modelos de redes | Bajo: casi nunca hubo práctica, sí alguna pregunta de teoría | §11 |
| CPM/PERT, programación no lineal, parametrización | **No se dieron** en 2026 | — |

### 0.2 Cómo fue el parcial del 3/10

![Mapa del parcial 2026: tres ejercicios y qué preguntaba cada uno](../../figs/r-mapa.png)
*Figura 1. Los tres ejercicios del parcial del 3/10 (Tema 1) y en qué sección se estudia cada uno.*

Las preguntas pedían **"el valor más cercano"**, así que todo indica que fue de opción múltiple. El formato importa por dos razones:

- No hay puntaje por el procedimiento. Un error de signo en un precio sombra da otra opción, y esa opción también va a estar en la lista.
- Cada respuesta es un número puntual: un vértice, una holgura, un precio sombra, el extremo de un rango, un $\lambda$, un lote. Hay que saber llegar a cada uno **por el camino más corto**.

### 0.3 Qué tomaron los exámenes de años anteriores

Se revisaron 25 parciales y 21 finales de `archivo/Examenes/` (2010–2026). Cantidad de exámenes en los que aparece cada tema como ejercicio práctico, sobre 46:

| Tema | Exámenes |
|---|---|
| Sensibilidad sobre una tabla óptima (manual o salida de LINDO) | **29** |
| Plantear el dual y dar su solución | **16** |
| Stock con demanda aleatoria (punto de pedido, stock de seguridad) | **14** |
| Método gráfico | 10 |
| Completar o iterar una tabla simplex | 9 |
| Período común · revisión periódica · modelización entera | 7 cada uno |
| Lagrange (restricción financiera, de espacio o de tiempo) | 6 |
| Consumo durante el ingreso | 5 |
| Descuentos | 4 |
| Transporte y asignación | 2 |

Dos patrones se repiten:

- **Casi siempre hay una restricción $\geq$ o $=$** en el ejercicio de sensibilidad (2017, 2021, 2022, 2025 y 2026). Es donde más se resta: el signo del precio sombra y el signo de la variable dual.
- **"¿Conviene tomar un crédito para ampliar el presupuesto?"** con Lagrange salió en 2019, dos veces en 2021 y en 2026.

### 0.4 Siete reglas para responder "el valor más cercano"

1. **Primero el diagnóstico, después la cuenta.** ¿La tabla es óptima? ¿Es Max o Min? ¿Hay una restricción $\geq$? Casi todos los errores vienen de saltear esta pregunta.
2. **Verificá con $z^* = W^*$.** Si el valor del dual no da igual al del primal, hay un error de signo.
3. **Un precio sombra vale dentro de su rango.** "Si se agregan 1000 unidades de recurso" puede caer fuera del rango, y entonces no alcanza con multiplicar.
4. **Cuidado con las unidades.** El precio sombra está en \$ por unidad **de recurso**, el costo reducido en \$ por unidad **de producto** y $\lambda$ en tasa (1/tiempo).
5. **En stock, las cantidades y las tasas deben estar en la misma unidad de tiempo.** Las cantidades se multiplican (por día a por año); las tasas se dividen.
6. **Si dos opciones están muy cerca**, rehacé la cuenta con fracciones o con más decimales. En un ejercicio de 2018 (§14.4), el tanteo dio $\lambda = 0{,}18$ y el valor exacto es 0,170.
7. **Si sale una opción "trampa" conocida**, como el óptimo de una tabla que no es óptima o el rango de $b$ calculado con la columna equivocada de $B^{-1}$, desconfiá y revisá.

### 0.5 Un plan para los diez días

| Día | Qué |
|---|---|
| Lun 9 y mar 10 | §1 a §4: modelizar, método gráfico, simplex. Rehacer el ejercicio 1 del parcial sin mirar |
| Mié 11 | §5: sensibilidad. Rangos de $c_j$ y de $b_i$ hasta hacerlos de memoria |
| Jue 12 | §6 y §7: dualidad y el ejercicio 2 del parcial, completo y sin mirar |
| Vie 13 | §8.1 a §8.6: stock determinístico |
| Sáb 14 | §8.7 a §8.10: Lagrange, aleatorio, sistemas. Rehacer el ejercicio 3 del parcial |
| Dom 15 | §14: Steelco, restaurante, Vialmetal |
| Lun 16 | §9 a §12: transporte, entera, redes y la teoría que se repite |
| Mar 17 | Simulacro cronometrado: el parcial 2026 y el ejercicio de gráfico del 2025 |
| Mié 18 | §13: las trampas. Repaso de fórmulas |

## 1. Modelización y formas del modelo

*Fuentes: apunte PLC1 (Torrent), Práctica 2 y la resolución de Vaccaro del parcial 2025.*

### 1.1 Cómo se modeliza

Un programa lineal tiene una **función objetivo** que se maximiza o minimiza y un conjunto de **restricciones**, todas lineales. Los pasos son cuatro:

1. **Definir las variables con precisión**: qué miden, en qué unidad y en qué período. "$x_1$: toneladas de nafta producidas por día" está bien; "$x_1$: nafta" está mal.
2. Escribir la **función objetivo**: se maximiza si son ganancias o contribuciones, se minimiza si son costos.
3. Escribir `s.a.` y todas las restricciones, numeradas $1), 2), 3)\dots$
4. No olvidar la **no negatividad**: $x_j \geq 0$. La cátedra la numera como una restricción más.

Los parámetros tienen nombre propio y conviene usarlo al interpretar:

| Símbolo | Nombre | Qué representa |
|---|---|---|
| $c_j$ | coeficiente económico | cuánto aporta al objetivo cada unidad de $x_j$ |
| $b_i$ | término independiente | cantidad disponible de un recurso, o cantidad exigida de un requerimiento |
| $a_{ij}$ | coeficiente tecnológico | cuánto del recurso $i$ consume cada unidad de $x_j$ |

### 1.2 Forma canónica y forma estándar

- **Forma canónica**: Max con todas las restricciones $\leq$, o Min con todas $\geq$, y variables $\geq 0$. Es la que se usa para armar el dual.
- **Forma estándar**: todas las restricciones son **ecuaciones**, con $b_i \geq 0$ y variables $\geq 0$. Es la que necesita el simplex.

| Situación | Qué se hace |
|---|---|
| Restricción $\leq$ | Se **suma** una variable de **holgura** |
| Restricción $\geq$ | Se **resta** una variable de **exceso** (y, para el simplex, se suma una **ficticia**) |
| Restricción $=$ | Para el simplex, se suma una **ficticia** |
| $b_i < 0$ | Se multiplica toda la restricción por $-1$ **antes** de lo demás |
| Variable libre $x_k$ | $x_k = x_k' - x_k''$, con las dos $\geq 0$ |
| Min $W$ | Equivale a Max $Z = -W$: cambia el signo del valor, no las variables |

Las holguras y los excesos entran en la función objetivo con coeficiente **cero**. Las ficticias entran con $-M$ en Max y con $+M$ en Min (§4.4).

**Qué significan:**

- **Holgura**: cantidad de recurso que **sobra** en la solución.
- **Exceso**: cuánto **supera** el lado izquierdo al mínimo exigido.
- **Ficticia**: no significa nada; sólo sirve para armar la base inicial. En el óptimo tiene que valer cero.

> **Ojo:** la cátedra dice "variables **ficticias**", no "artificiales", y "recta de **isobeneficio**" (o isocosto), no "recta de nivel".

## 2. Método gráfico

*Fuentes: PLC1, Práctica 1, parciales 2025 y 2026.*

### 2.1 El procedimiento

Sirve con dos variables:

1. Graficar cada restricción como recta. Las intersecciones con los ejes salen de poner $x_1 = 0$ y después $x_2 = 0$.
2. Elegir el semiplano de cada una probando un punto, típicamente el $(0; 0)$: si cumple, el semiplano es el que lo contiene.
3. La **región factible (RF)** es la intersección de todos los semiplanos dentro del primer cuadrante.
4. Trazar la recta de isobeneficio $c_1x_1 + c_2x_2 = z$. Su vector normal $(c_1; c_2)$ apunta hacia donde crece $z$.
5. Desplazarla hasta el último punto de la RF: en el sentido de la normal si es Max, en el sentido opuesto si es Min.
6. Calcular el vértice resolviendo el sistema de las dos rectas que se cortan ahí.

La alternativa es el **método de los vértices**: calcular todos los vértices de la RF, evaluar $z$ en cada uno y quedarse con el mejor. Funciona porque, si hay óptimo, está en al menos un vértice (§3). En un examen de opción múltiple suele ser lo más rápido.

### 2.2 Tipos de solución

![Seis paneles: óptimo único, alternativos, no acotada, RF no acotada con óptimo finito, no factible y clasificación de restricciones](../../figs/r-tipos-solucion.png)
*Figura 2. Los casos posibles del método gráfico y la clasificación de restricciones.*

| Caso | Cómo se reconoce en el gráfico | Frase de la cátedra |
|---|---|---|
| **Única** | La isobeneficio toca la RF en un solo vértice | — |
| **Alternativas** | La isobeneficio es **paralela a una restricción activa** | "El óptimo se da en un segmento, no en un solo punto." |
| **No acotada** | La RF está abierta en la dirección en que mejora $z$ | "La solución es no acotada." |
| **No factible** | Los semiplanos no se cortan: $\text{RF} = \emptyset$ | "La región factible es nula." |

Con óptimos alternativos, cada vértice del segmento es una solución básica y todo punto intermedio también es óptimo:

$$P = \alpha\,P_1 + (1-\alpha)\,P_2, \qquad 0 \leq \alpha \leq 1$$

> **Ojo:** **región factible no acotada no es lo mismo que solución no acotada.** Un Min sobre una RF abierta hacia arriba puede tener un óptimo finito (panel d). El profesor lo escribió en la resolución del parcial 2025: "No confundir región factible no acotada con solución no acotada".

**Para detectar alternativas sin dibujar:** compará pendientes. Si $c_1/c_2$ es igual a $a_{i1}/a_{i2}$ de alguna restricción que pasa por el óptimo, hay alternativas. En el parcial 2026, $150/500 = 3/10$, que es justo la pendiente de la restricción ①.

### 2.3 Clasificación de restricciones

- **Activa** (u obligatoria): pasa por el óptimo. Su holgura o exceso vale **cero**.
- **Pasiva** (o no obligatoria): su holgura o exceso es **positivo**. Puede ser de dos tipos:
  - **necesaria**: si se la saca, la RF cambia;
  - **redundante**: si se la saca, la RF no cambia. Es *geométricamente redundante* si ni toca la RF, y *analíticamente redundante* si toca un vértice y es combinación lineal de las que pasan por él.

### 2.4 Las preguntas puntuales y cómo se contestan

| Pregunta | Cómo se responde |
|---|---|
| ¿Un punto es factible? | Reemplazarlo en **todas** las restricciones, incluida la no negatividad. Si falla una, no es factible |
| ¿Cuánto vale la holgura de la restricción $i$ en un punto? | Holgura $= b_i - a_i x$ en una $\leq$; exceso $= a_i x - b_i$ en una $\geq$ |
| ¿Qué restricciones son activas en el óptimo? | Las que dan holgura o exceso **cero** en el punto óptimo |
| ¿Cuál es el valor óptimo? | $z^*$ con la unidad y el período: "el costo mínimo diario es de \$ 320" |
| ¿Cuántas soluciones tiene? | Una, infinitas (alternativas), ninguna (no factible) o no acotada |

> **Ojo:** "estar sobre la recta $i$" es lo mismo que "su holgura o exceso vale 0". Por eso cruzar dos rectas para encontrar un vértice equivale a anular dos variables y resolver el resto. Es el puente con el simplex (§3).

### 2.5 Cómo se escribe la respuesta

La cátedra escribe la solución como **vector columna con todas las variables**, incluidas holguras y excesos, y el valor del funcional aparte:

```
         40
          0
S*  =     0          W* = 320
         50
          0
```

Después interpreta línea por línea: qué se produce, qué **no** se produce (se dice explícitamente), cuánto sobra de cada recurso con su unidad y el valor óptimo con unidad y período. Con alternativas va un vector por vértice: $S^*_A$, $S^*_D$.

### 2.6 Así vino en el parcial: ejercicio 1

$$\text{Min } W = 150x_1 + 500x_2 \quad \text{s.a.} \quad
\begin{cases}
① \;\; 3x_1 + 10x_2 \geq 300\\
② \;\; x_1 + 2x_2 \leq 120\\
③ \;\; -x_1 + x_2 \leq 30\\
x_1, x_2 \geq 0
\end{cases}$$

![Región factible del ejercicio 1 con el segmento óptimo entre A y D](../../figs/r-parcial-ej1.png)
*Figura 3. La RF es el cuadrilátero ABCD. La isocosto es paralela a ①, así que todo el segmento AD es óptimo.*

Los vértices de la RF y el valor de $W$ en cada uno:

| Vértice | Rectas que se cortan | $W$ |
|---|---|---|
| A $(0; 30)$ | ① ∩ ③ ∩ eje $x_2$ | **15.000** |
| B $(20; 50)$ | ② ∩ ③ | 28.000 |
| C $(120; 0)$ | ② ∩ eje $x_1$ | 18.000 |
| D $(100; 0)$ | ① ∩ eje $x_1$ | **15.000** |

**1) Coordenadas de la solución óptima.** Hay **óptimos alternativos**: todo el segmento entre A $(0; 30)$ y D $(100; 0)$. Se ve sin dibujar porque $W = 50 \cdot (3x_1 + 10x_2)$: la función objetivo es proporcional a la restricción ①. Si la opción pide un solo punto, tanto A como D son correctos.

**2) ¿$(50; 30)$ es factible?** Sí. ① da $150 + 300 = 450 \geq 300$; ② da $50 + 60 = 110 \leq 120$; ③ da $-20 \leq 30$.

**3) Restricciones activas en el óptimo.** **①** en todo el segmento. En el vértice A también ③ ($-0 + 30 = 30$). ② no es activa en ningún punto del segmento.

**4) Holgura de ② en $(100; 0)$.** $120 - (100 + 0) = 20$.

**5) Costo óptimo.** $W^* =$ **\$ 15.000**.

> **Ojo:** el que no ve el paralelismo elige A o D y cree que la solución es única. Ante una opción que dice "infinitas soluciones", revisá siempre las pendientes.

## 3. Conceptos básicos: convexidad, soluciones básicas y teoremas

*Fuentes: PLC2 y las diapositivas "Cap. 2 – Conceptos básicos" del Classroom.*

### 3.1 Las definiciones

- **Conjunto convexo**: el segmento que une dos puntos cualesquiera del conjunto queda entero adentro.
- **Punto extremo** (vértice): no se puede escribir como combinación lineal convexa de otros dos puntos del conjunto.
- **Combinación lineal convexa**: $x = \sum \lambda_i x_i$, con $\lambda_i \geq 0$ y $\sum \lambda_i = 1$.
- **Polítopo**: intersección de un número finito de semiespacios cerrados. Acotado, se llama poliedro. La RF de un PL es un polítopo, y por eso es **convexa**.
- **Solución básica**: con $m$ restricciones y $n$ variables en forma estándar, se anulan $n - m$ variables (las **no básicas**) y se resuelve para las $m$ **básicas**: $x_B = B^{-1}b$.
- **Solución básica factible (SBF)**: todas sus básicas son $\geq 0$.
- **SBF degenerada**: alguna variable **básica** vale cero (tiene menos de $m$ componentes positivas).

### 3.2 Los teoremas

1. El conjunto de soluciones factibles es **convexo y cerrado**.
2. **Teorema fundamental de la PL**: si hay una solución factible, hay una SBF; si hay una solución óptima, hay una **SBF óptima**.
3. **Teorema de equivalencia**: $x$ es punto extremo **si y sólo si** es una SBF. Une la geometría (vértices) con el álgebra (bases).
4. El óptimo se alcanza en **al menos un punto extremo**. Si se alcanza en más de uno, también en toda combinación convexa de ellos.

Consecuencia: **aunque la RF tenga infinitos puntos, alcanza con mirar un número finito**, los vértices. Como mucho hay

$$\binom{n}{m} = \frac{n!}{m!\,(n-m)!}$$

La **solución conceptual** recorre todas esas bases. Su problema es la escala: con 20 variables y 10 restricciones son 184.756 sistemas. Por eso existe el simplex, que va de vértice en vértice sin recorrerlos todos.

> **Ojo:** la cátedra no pide demostrar los teoremas, sí enunciarlos y explicar qué consecuencia tienen.

## 4. Método simplex

*Fuentes: PLC3, pizarras de clase "Factibilidad", "Pasos del simplex" y "Coeficientes de sustitución" (Classroom 2026).*

### 4.1 La notación de la cátedra

| Símbolo | Qué es | Cómo se calcula |
|---|---|---|
| $B$ | la base: las $m$ columnas de las variables básicas | — |
| $Y_j$ | columna de $A_j$ escrita en la base actual | $Y_j = B^{-1}A_j$ (en la tabla, la columna $j$) |
| $z_j$ | lo que se pierde en el funcional al hacer entrar una unidad de $x_j$ | $z_j = c_B\,Y_j = \sum_i c_i\,y_{ij}$ |
| $c_j - z_j$ | **costo reducido**: cuánto cambia $z$ por unidad de $x_j$ que entra | fila de abajo de la tabla |
| $\theta_j$ | cuánto puede crecer $x_j$ sin que ninguna básica se vuelva negativa | $\min\{x_i/y_{ij} : y_{ij} > 0\}$ |
| $-y_{ij}$ | **coeficiente de sustitución**: cuánto cambia la básica $x_i$ por unidad de $x_j$ | $\partial x_i/\partial x_j = -y_{ij}$ |

La tabla de la cátedra tiene columnas $c_i$ | $A_i$ (base) | $A_1 \dots A_n$ | $x_i$ | $x_i/y_{ij}$, y abajo las filas $z_j$ y $c_j - z_j$. Se trabaja con **$c_j - z_j$**, no con $z_j - c_j$.

### 4.2 Las dos condiciones

**Condición de factibilidad: quién sale.** Si entra $x_j$ con valor $\theta_j$, cada básica pasa a valer $x_i' = x_i - \theta_j\,y_{ij}$. Para que ninguna quede negativa,

$$\theta_j = \min_i \left\{ \frac{x_i}{y_{ij}} \;:\; y_{ij} > 0 \right\}$$

Sale la básica que da el mínimo, porque queda exactamente en cero. **Sólo se divide por $y_{ij} > 0$.**

**Condición de optimización: quién entra.** Con esa nueva solución, el funcional queda

$$z' = z + \theta_j\,(c_j - z_j)$$

Como $\theta_j \geq 0$, en **Max** conviene que entre una $x_j$ con $c_j - z_j > 0$. La tabla es óptima cuando **todos los $c_j - z_j \leq 0$**. En **Min** todo se da vuelta: entra el más negativo y es óptima cuando todos son $\geq 0$.

| | Max | Min |
|---|---|---|
| Entra | el mayor $c_j - z_j > 0$ | el menor $c_j - z_j < 0$ |
| Óptimo cuando | todos los $c_j - z_j \leq 0$ | todos los $c_j - z_j \geq 0$ |
| Ficticia en el funcional | $-M$ | $+M$ |

### 4.3 El algoritmo

![Diagrama de flujo del simplex: forma estándar, base inicial, cálculo de cj − zj, entrada, salida, pivoteo y diagnóstico](../../figs/r-simplex-flujo.png)
*Figura 4. El simplex como diagrama de flujo, con los dos puntos donde termina: óptimo o no acotada.*

El pivoteo, con la tabla: la fila del pivote se divide por el pivote, y en las demás filas se resta un múltiplo de la fila nueva para que la columna entrante quede con ceros. Con fórmulas: $x_j' = \theta_j$, $x_r' = 0$ y $x_i' = x_i - \theta_j\,y_{ij}$ para las demás básicas.

**Desempates** (apunte, §3.2): si empatan dos entradas, entra la de menor subíndice; si empatan dos salidas, sale la de mayor subíndice. Un empate en la salida anuncia una **solución degenerada**.

### 4.4 Variables ficticias y Gran M

Las restricciones $\geq$ y $=$ no traen una columna de la identidad, así que se agrega una **ficticia** para completar la base inicial. Para que el simplex la expulse, se la castiga en el funcional: **"MAX −, MIN +"**, es decir $-M\,x_f$ en Max y $+M\,x_f$ en Min, con $M$ muy grande. En las cuentas manda el término en $M$: $30 + 2M$ le gana a $40 - 2M$.

- Una ficticia que sale de la base no vuelve a entrar.
- **Efecto espejo**: en una $\geq$, la columna del exceso es siempre la de su ficticia multiplicada por $-1$, y lo mismo pasa con sus $z_j$. Sirve para controlar la tabla.
- En 2026 la cátedra usó sólo Gran M. El método de las dos fases (minimizar la suma de las ficticias y después reciclar la tabla) está en el apunte, pero no apareció en clase.

### 4.5 Diagnóstico en la tabla óptima

| Caso | Señal en la tabla | Frase de la cátedra |
|---|---|---|
| **Única** | Todos los $c_j - z_j$ de las **no básicas** son estrictamente negativos (Max) | "La solución es única ya que todos los $c_j - z_j$ son nulos para las básicas y negativos para las no básicas." |
| **Alternativas** | Una **no básica** tiene $c_j - z_j = 0$ en el óptimo | "El óptimo se da en un segmento." Haciéndola entrar sale otra SBF con el mismo $z$ |
| **Degenerada** | Una **básica** vale 0 | — |
| **No acotada** | Un $c_j - z_j$ mejora y su columna no tiene ningún $y_{ij} > 0$ | "No puede salir ninguna variable, por lo tanto el problema tiene solución no acotada." |
| **No factible** | En el óptimo queda una **ficticia básica con valor > 0** | "Hay variables ficticias en la base, por lo tanto el problema es no factible ($\text{RF} = \emptyset$)." |

> **Ojo:** degenerada y alternativas son cosas distintas. **Degenerada**: una **básica** vale 0. **Alternativas**: una **no básica** tiene $c_j - z_j = 0$. Pueden darse juntas.

> **Ojo:** un $c_j - z_j = 0$ en una no básica sólo indica alternativas **si la tabla ya es óptima**. En la tabla del parcial 2026, $c_1 - z_1 = 0$, pero la tabla no era óptima: no decía nada.

### 4.6 Dónde se lee cada cosa

- **$x_B$**: la columna $x_i$. Las variables que no están en la base valen cero.
- **$z$**: abajo de la columna $x_i$, $z = c_B\,x_B$.
- **$B^{-1}$**: debajo de las columnas que en la **tabla inicial formaban la identidad**, es decir las holguras y, si hubo, las ficticias. No debajo de las básicas actuales.
- **Control rápido**: bajo cada columna básica, $z_j = c_j$ y $c_j - z_j = 0$.

> **Ojo:** si vas a hacer sensibilidad o dualidad, **no borres la columna de la ficticia** aunque haya salido de la base. Es la columna de $B^{-1}$ que corresponde a esa restricción.

### 4.7 "¿Se detiene o sigue?" en treinta segundos

Es la primera pregunta del ejercicio 2 del parcial:

1. Calcular la fila $z_j = c_B Y_j$ (la tabla del parcial **no la traía**).
2. Mirar los $c_j - z_j$ de las no básicas. En Max, si alguno es $> 0$, **sigue** y entra el mayor.
3. En la columna que entra, dividir $x_i / y_{ij}$ sólo donde $y_{ij} > 0$. Sale la fila del menor cociente.

## 5. Análisis de sensibilidad

*Fuentes: PLC4, Práctica 4 y `estudio/parcial/teoria-sensibilidad-dualidad.md` (los fundamentos con el ejemplo de la alfarería).*

### 5.1 La idea

Sensibilidad (o postoptimización) estudia cómo cambia el óptimo cuando cambia **un** dato, **sin volver a resolver**. Funciona porque toda la tabla óptima es $B^{-1}$ aplicada a los datos originales:

- **Si cambia un $c_j$**, cambian los $c_j - z_j$ y las restricciones siguen iguales. Lo que puede romperse es la **optimalidad**.
- **Si cambia un $b_i$**, cambia $x_B = B^{-1}b$ y los $c_j - z_j$ siguen iguales. Lo que puede romperse es la **factibilidad**.

**Hipótesis**: cambia un solo coeficiente por vez y los demás quedan como en la formulación original.

### 5.2 Cambio en un coeficiente económico $c_k$

**Si $x_k$ es no básica**, sólo cambia su propio $c_k - z_k$. Para que siga sin entrar:

$$\text{Max: } \Delta c_k \leq -(c_k - z_k) \qquad\qquad \text{Min: } \Delta c_k \geq -(c_k - z_k)$$

Dentro del rango no cambian ni el punto óptimo ni $z^*$, porque $x_k$ vale cero.

**Si $x_k$ es básica**, cambian **todos** los $c_j - z_j$ de las no básicas: el nuevo valor es $(c_j - z_j) - \Delta c_k\,y_{kj}$. En Max:

$$\max_{y_{kj} > 0} \frac{c_j - z_j}{y_{kj}} \;\leq\; \Delta c_k \;\leq\; \min_{y_{kj} < 0} \frac{c_j - z_j}{y_{kj}}$$

En Min se invierten los grupos: el máximo se toma sobre los $y_{kj} < 0$ y el mínimo sobre los $y_{kj} > 0$.

**Paso a paso** (Max):

1. Ir a la **fila** de $x_k$ en la tabla óptima.
2. Tomar los $y_{kj}$ de las columnas **no básicas**, sin contar las ficticias.
3. Dividir cada $c_j - z_j$ por su $y_{kj}$ y separar los cocientes según el signo de $y_{kj}$.
4. Cota inferior: el **mayor** de los cocientes con $y_{kj} > 0$. Cota superior: el **menor** de los cocientes con $y_{kj} < 0$. Si un grupo está vacío, esa cota es infinita.

Dentro del rango, el punto óptimo **no cambia** y $z^{*\prime} = z^* + \Delta c_k \cdot x_k^*$.

### 5.3 Cambio en un término independiente $b_k$

Geométricamente, la restricción $k$ se desplaza en paralelo. Las básicas pasan a valer $x_i^* + r_{ik}\,\Delta b_k$, donde $r_{ik}$ es la columna $k$ de $B^{-1}$. Para que sigan siendo $\geq 0$:

$$\max_{r_{ik} > 0} \frac{-x_i^*}{r_{ik}} \;\leq\; \Delta b_k \;\leq\; \min_{r_{ik} < 0} \frac{-x_i^*}{r_{ik}}$$

La fórmula es la misma para Max y para Min. Dentro del rango la base sigue siendo óptima, los **valores** de las básicas cambian y

$$z^{*\prime} = z^* + u_k\,\Delta b_k$$

donde $u_k$ es el valor implícito de la restricción $k$ (§5.5).

**¿Qué columna de $B^{-1}$ uso?** La de la variable que en la tabla inicial tenía el 1 en la fila $k$: la **holgura** si la restricción es $\leq$, la **ficticia** si es $\geq$ o $=$. Si borraste la ficticia, en una $\geq$ sirve la columna del exceso **cambiada de signo**.

### 5.4 Cambio tecnológico, variable nueva y restricción nueva

- **Cambia $a_{ij}$ de una no básica**, o **aparece una variable nueva**: se calcula su columna en la base óptima, $Y_k = B^{-1}A_k$, después $z_k = c_B\,Y_k$ (o directamente $z_k = u \cdot A_k$) y se mira $c_k - z_k$. En Max: si es $\leq 0$, el óptimo no cambia; si es $> 0$, la variable entra y hay que iterar. Si da exactamente 0, aparece un óptimo alternativo que la incluye.
- **Restricción nueva**: se reemplaza el óptimo actual en ella. Si la cumple, no cambia nada. Si no la cumple, hay que agregarla e iterar (con el simplex dual).
- **Cambia $a_{ij}$ de una básica**: puede alterar toda la tabla. La cátedra no lo toma.

> **Ojo:** "¿conviene fabricar un producto nuevo?" se responde en una línea con el dual: $z_k = \sum_i u_i\,a_{ik}$ es lo que valen los recursos que consume. Si su contribución $c_k$ supera ese valor, conviene.

### 5.5 Valor implícito, precio sombra y costo reducido

**Valor implícito** (o precio dual): cuánto cambia el valor óptimo $z^*$ si el término independiente de una restricción aumenta en una unidad, con los demás fijos y **sin que cambie la base óptima**. Según la restricción, toma otro nombre:

- Si la restricción es un **recurso disponible** ($\leq$ en Max), se llama **precio sombra**, costo marginal o costo de oportunidad. Es **lo máximo que conviene pagar por una unidad más** del recurso.
- Si la restricción es un **requerimiento** ($\geq$), se llama **valor marginal**: cuánto empeora (o mejora) el óptimo por cada unidad más que se exige.

La cátedra lo lee así: **costo marginal $= c_B\,B^{-1} = z_j$** en las columnas de la base inicial. Para una holgura, como $c_j = 0$, eso es $-(c_j - z_j)$.

| | Costo reducido | Precio sombra |
|---|---|---|
| Se asocia a | una **variable** (un producto) | una **restricción** (un recurso) |
| Se lee en | $c_j - z_j$ de la columna de $x_j$ | $z_j$ de la columna de la holgura (o la ficticia) |
| Qué dice | cuánto hay que **mejorar** $c_j$ para que $x_j$ entre a la base | cuánto vale, al margen, una unidad más del recurso |
| Vale 0 cuando | $x_j$ es básica (se produce) | la restricción es **pasiva** (sobra recurso) |
| Unidad | \$ por unidad de producto | \$ por unidad de recurso |

**El signo del valor implícito** depende del tipo de problema y de restricción:

| Problema | $\leq$ | $\geq$ | $=$ |
|---|---|---|---|
| Max | $u_i \geq 0$ | $u_i \leq 0$ | cualquier signo |
| Min | $u_i \leq 0$ | $u_i \geq 0$ | cualquier signo |

Es lógico: en un Max, aumentar un recurso nunca empeora el óptimo, pero exigir más de un mínimo sí puede empeorarlo.

![Rangos de c1, c2, c3, b1, b2 y b3 del ejercicio 2 del parcial sobre rectas numéricas](../../figs/r-rangos-sensibilidad.png)
*Figura 5. Los rangos del ejercicio 2 del parcial (§7). Dentro de cada barra, la base óptima no cambia.*

## 6. Dualidad

*Fuentes: PLC5, diapositivas "IO 2025 – Dualidad" del Classroom y Práctica 4.*

### 6.1 Cómo se arma el dual

A todo programa lineal (el **primal**) le corresponde otro (el **dual**). En forma canónica:

$$\text{Primal: } \text{Max } z = c\,x \;\; \text{s.a. } A\,x \leq b,\; x \geq 0
\qquad\qquad
\text{Dual: } \text{Min } w = b^T u \;\; \text{s.a. } A^T u \geq c^T,\; u \geq 0$$

Las reglas mecánicas:

- Max pasa a Min, y al revés.
- Cada **restricción** del primal da una **variable** del dual, y cada **variable** del primal da una **restricción** del dual.
- Los $b_i$ pasan a ser los coeficientes del funcional dual, y los $c_j$, los términos independientes.
- La matriz se **transpone**: la fila $i$ del primal es la columna $i$ del dual.

Los signos, cuando el primal no está en forma canónica (primal Max):

| Primal (Max) | Dual (Min) |
|---|---|
| Restricción $i$ con $\leq$ | $u_i \geq 0$ |
| Restricción $i$ con $\geq$ | $u_i \leq 0$ |
| Restricción $i$ con $=$ | $u_i$ libre |
| $x_j \geq 0$ | Restricción $j$ con $\geq$ |
| $x_j$ libre | Restricción $j$ con $=$ |

Para un primal Min se lee la misma tabla de derecha a izquierda: restricción $\geq$ da $u_i \geq 0$, restricción $\leq$ da $u_i \leq 0$, y cada $x_j \geq 0$ da una restricción $\leq$ en el dual (Max).

> **Ojo:** hay otra forma de hacerlo: multiplicar las $\geq$ por $-1$ para dejar todo en forma canónica. Así todas las $u_i$ quedan $\geq 0$, pero el $b_i$ de esa restricción entra al funcional con signo cambiado. Las dos formas son correctas. Elegí una y no las mezcles, porque el signo de $u_i$ depende de cuál uses.

### 6.2 El teorema fundamental

**Si el primal tiene solución óptima finita, los valores de $u$ que minimizan el dual son los costos marginales del primal, y $w^* = z^*$.** En fórmula, $u^{*T} = c_B\,B^{-1}$.

Las relaciones entre los dos problemas:

| Si uno tiene… | el otro tiene… |
|---|---|
| óptimo finito | óptimo finito, con el mismo valor |
| solución no acotada | ninguna solución factible |
| soluciones múltiples | solución degenerada |
| solución degenerada | soluciones múltiples |
| ninguna solución factible | ninguna solución factible, o una solución no acotada |

### 6.3 Holguras complementarias

Las variables del primal y del dual se aparean:

| Primal | ↔ | Dual |
|---|---|---|
| variable de decisión $x_j$ | ↔ | exceso de la restricción dual $j$ (es el costo reducido de $x_j$, cambiado de signo) |
| holgura o exceso de la restricción $i$ | ↔ | variable dual $u_i$ (el precio sombra) |

**En el óptimo, en cada par al menos uno vale cero.** Leído en criollo:

- Si sobra un recurso, su precio sombra es **cero**.
- Si un recurso tiene precio sombra positivo, está **agotado**.
- Si un producto se fabrica ($x_j > 0$), lo que valen los recursos que consume es **exactamente** su contribución.
- Si los recursos que consume un producto valen más que lo que aporta, ese producto **no se fabrica**.

![Pares primal–dual del ejercicio 2 del parcial: en cada par uno de los dos vale cero](../../figs/r-pares-primal-dual.png)
*Figura 6. Los seis pares del ejercicio 2 del parcial. Ningún par tiene los dos lados distintos de cero.*

### 6.4 El dual sin resolverlo: lectura en la tabla óptima del primal

| Valor del dual | Dónde se lee (primal Max) |
|---|---|
| $u_i$ de una restricción $\leq$ | $z_j$ de su holgura, que es igual a $-(c_j - z_j)$ |
| $u_i$ de una restricción $\geq$ o $=$ | $z_j$ de su ficticia, que es igual a $-z_j$ de su exceso |
| exceso dual $j$ (de una $x_j$) | $-(c_j - z_j)$ de la columna de $x_j$ |
| $w^*$ | $= z^*$ |

### 6.5 La interpretación económica

El primal pregunta **cuánto producir**. El dual pregunta **cuánto vale cada recurso**. El dual busca el valor total mínimo de los recursos disponibles, con la condición de que los recursos que consume cada producto valgan por lo menos lo que ese producto aporta. Que $w^* = z^*$ quiere decir que **la ganancia máxima coincide con el valor mínimo de los recursos**: nada se crea ni se pierde.

El apunte lo explica como un **seguro**: el dual es la prima mínima que habría que cobrar por "alquilar" todos los recursos de modo que al dueño le dé igual producir o alquilar.

## 7. Ejercicio integrador: la refinería del parcial

*El ejercicio 2 del parcial del 3/10/2026, resuelto entero y verificado por cálculo exacto.*

### 7.1 El enunciado y el modelo

Una refinería produce nafta ($x_1$), diésel ($x_2$) y fueloil ($x_3$), medidos en toneladas, y quiere maximizar la ganancia en USD.

$$\text{Max } Z = 50x_1 + 80x_2 + 30x_3 \quad \text{s.a.}\quad
\begin{cases}
① \;\; 2x_1 + 3x_2 + 1{,}5x_3 \leq 5000 & \text{(materia prima: petróleo crudo)}\\
② \;\; 0{,}5x_1 + 0{,}8x_2 + 0{,}2x_3 \leq 1200 & \text{(capacidad de destilación)}\\
③ \;\; x_2 \geq 500 & \text{(contrato mínimo de diésel)}\\
x_j \geq 0
\end{cases}$$

En forma estándar, con Gran M: $x_4$ es la holgura de ①, $x_5$ la holgura de ②, $x_6$ el exceso de ③ y $x_7$ la ficticia de ③.

$$\text{Max } Z = 50x_1 + 80x_2 + 30x_3 + 0x_4 + 0x_5 + 0x_6 - Mx_7$$

### 7.2 La tabla dada y la óptima

![Tabla intermedia del parcial con la entrada y la salida marcadas, y tabla óptima anotada](../../figs/r-parcial-ej2-tablas.png)
*Figura 7. a) La tabla del parcial no es óptima: entra $A_3$ y sale $A_4$. b) Dónde se lee cada respuesta en la tabla óptima.*

### 7.3 Las ocho preguntas

**1) ¿Se detiene o sigue? ¿Quién entra y quién sale?** **Sigue.** Con $c_B = (0; 0; 80)$, los $z_j$ son $(50; 80; 20; 0; 100; 0; 0)$, y $c_3 - z_3 = 30 - 20 = +10 > 0$. **Entra $A_3$** (fueloil). Los cocientes son $500/(3/4) = 666{,}7$, $1000/(1/4) = 4000$ y $1500/(1/4) = 6000$: **sale $A_4$**, la holgura de la materia prima.

**2) Precio sombra de la capacidad de destilación en el óptimo.** $u_2 =$ **50 USD por unidad de capacidad**. Se lee como $-(c_5 - z_5) = 50$.

**3) Rango de $c_2$ (diésel) para que la base no cambie.** La fila de $A_2$ tiene $y_{21} = 7/12$, $y_{24} = -1/3$, $y_{25} = 5/2$ en las no básicas, con $c_j - z_j$ iguales a $-5/3$, $-40/3$ y $-50$:

$$\max\left\{\frac{-5/3}{7/12};\ \frac{-50}{5/2}\right\} = \max\{-2{,}86;\ -20\} = -2{,}86 \;\leq\; \Delta c_2 \;\leq\; \frac{-40/3}{-1/3} = 40$$

$$\boxed{77{,}14 \leq c_2 \leq 120}$$

**4) Función dual.** Armada directamente (la ③ es $\geq$ en un Max, así que $u_3 \leq 0$):

$$\text{Min } W = 5000u_1 + 1200u_2 + 500u_3 \quad \text{s.a.}\quad
\begin{cases}
2u_1 + 0{,}5u_2 \geq 50\\
3u_1 + 0{,}8u_2 + u_3 \geq 80\\
1{,}5u_1 + 0{,}2u_2 \geq 30\\
u_1, u_2 \geq 0;\;\; u_3 \leq 0
\end{cases}$$

La solución es $u^* = (40/3;\ 50;\ 0)$ y $W^* = 5000 \cdot 40/3 + 1200 \cdot 50 = 126.666{,}67 = Z^*$ ✓.

> **Ojo:** la consigna decía "$y_j \geq 0$". Si te piden todas las duales $\geq 0$, hay que escribir la ③ como $-x_2 \leq -500$: el término del funcional pasa a ser $-500u_3$, con $u_3 \geq 0$. El valor óptimo es el mismo.

**5) Holguras que no son básicas en el óptimo.** **$x_4$ y $x_5$**: valen cero, así que la materia prima y la capacidad de destilación se usan completas. El exceso $x_6 = 833{,}33$ es básico: se producen 833,33 t de diésel por encima del mínimo del contrato.

**6) Significado económico del precio sombra de la primera restricción.** $u_1 = 40/3 \approx 13{,}33$: **cada tonelada adicional de petróleo crudo aumenta la ganancia en 13,33 USD**, mientras $b_1$ se mantenga entre 4.500 y 7.500. Es lo máximo que conviene pagar por una tonelada más.

**7) En la tabla inicial, ¿qué variables entran a la base y cuál sale en la primera iteración?** La base inicial es $\{x_4, x_5, x_7\}$: las dos holguras y la **ficticia** de la ③, no el exceso. En la primera iteración, $c_2 - z_2 = 80 + M$ es el mayor, así que **entra $x_2$**. Los cocientes son $5000/3 = 1666{,}7$, $1200/0{,}8 = 1500$ y $500/1 = 500$: **sale la ficticia $x_7$**.

**8) Costo reducido de la nafta en el óptimo.** $c_1 - z_1 = -5/3 \approx -1{,}67$ **USD/t**. Producir una tonelada de nafta bajaría la ganancia en 1,67 USD. Para que convenga producirla, su ganancia tendría que subir más de 1,67, es decir **$c_1 > 51{,}67$**.

### 7.4 La solución completa y los rangos de $b$

$$S^* = (0;\ 1333{,}33;\ 666{,}67;\ 0;\ 0;\ 833{,}33)^T \qquad Z^* = 126.666{,}67 \text{ USD}$$

Se producen 1.333,33 t de diésel y 666,67 t de fueloil, y no se produce nafta. Se usan completos el crudo y la capacidad de destilación. El diésel supera el mínimo del contrato en 833,33 t. La solución es **única**: todos los $c_j - z_j$ de las no básicas son negativos.

Las columnas de $B^{-1}$ son las de $A_4$, $A_5$ y $A_7$, y $x_B = (666{,}67;\ 833{,}33;\ 1333{,}33)$:

| Restricción | Columna de $B^{-1}$ | Rango de $\Delta b$ | Rango de $b$ |
|---|---|---|---|
| ① crudo | $(4/3;\ -1/3;\ -1/3)$ | $-500 \leq \Delta b_1 \leq 2500$ | $4.500 \leq b_1 \leq 7.500$ |
| ② destilación | $(-5;\ 5/2;\ 5/2)$ | $-333{,}33 \leq \Delta b_2 \leq 133{,}33$ | $866{,}67 \leq b_2 \leq 1.333{,}33$ |
| ③ diésel mínimo | $(0;\ -1;\ 0)$ | $\Delta b_3 \leq 833{,}33$ | $b_3 \leq 1.333{,}33$ |

Rango de $c_3$ (fueloil): $20 \leq c_3 \leq 40$. Todos los rangos se verificaron re-resolviendo el problema con el dato apenas adentro y apenas afuera de cada extremo.

## 8. Gestión de stocks

*Fuentes: apunte de Mascó y Torrent (`STOCK16Transp.pdf`), Práctica 7 y su resolución en Excel (`RESOLSTOCK.xlsx`, Classroom), y finales y parciales viejos.*

### 8.1 Por qué existe el stock

Para la cátedra el stock es un **desperdicio**: no agrega valor, inmoviliza capital, genera costos y **oculta problemas** de producción. El ideal sería no tenerlo, pero en la práctica es un **desperdicio inevitable**.

**Causas que lo generan**: aleatoriedad de la demanda y de los aprovisionamientos, tiempos de preparación de máquinas altos, paradas no programadas, equipos o personal poco versátiles y fallas de calidad.

**Objetivos de la gestión de existencias**: reducir los niveles al mínimo y asegurar el suministro en el momento adecuado. Los dos tiran para lados opuestos, y los modelos buscan el equilibrio.

**Cómo se reducen las existencias**: primero se eliminan las causas con mejora continua y después se achican los lotes y los plazos. Achicar los lotes sin atacar las causas sólo traslada el problema.

**La tasa de mantenimiento $i$** suma los costos anuales que dependen del stock: capital inmovilizado (costo de oportunidad), espacio, personal, riesgos (deterioro, obsolescencia, robo, seguros), administración e impuestos. Típicamente va del 15 % al 40 % anual del valor invertido.

### 8.2 La fórmula general del costo

Para un lote de $Q$ unidades, el costo **por unidad** en el momento de usarla es

$$CT(Q) = C(Q) + \frac{L}{Q} + \frac{C(Q)\, i\, A(Q)}{Q}$$

| Letra | Qué es | Unidad |
|---|---|---|
| $D$ | demanda | unidades/tiempo |
| $C$ | costo unitario de compra o fabricación | \$/unidad |
| $L$ | costo fijo de lanzar una orden; no depende de $Q$ | \$/orden |
| $i$ | tasa de mantenimiento | 1/tiempo |
| $A(Q)$ | área bajo la curva de existencias en un ciclo | unidades·tiempo |
| $LT$ | plazo de provisión (*lead time*) | tiempo |

> **Ojo:** $C$ es el precio, un dato. $CT$ es el costo real por unidad (precio, más pedir, más mantener), un resultado. Siempre $CT > C$. El costo del período es $CT \cdot D$. Para comparar alternativas se compara $CT$, nunca el precio solo.

### 8.3 Modelo básico

**Supuestos**: $C$ constante, demanda continua y uniforme, el lote entra de golpe, $LT$ constante y conocido, sin faltantes.

![Diente de sierra del modelo básico con Q, T*, punto de pedido y plazo de provisión](../../figs/r-stock-basico.png)
*Figura 8. Cada ciclo dura $T = Q/D$ y el stock promedio es $Q/2$. El pedido se emite cuando el stock toca PP.*

Como el stock baja en línea recta de $Q$ a 0 en $T = Q/D$, el área es $A(Q) = Q^2/(2D)$, y

$$CT(Q) = C + \frac{L}{Q} + \frac{C\,i\,Q}{2D}$$

Derivando e igualando a cero se obtiene el lote óptimo:

$$\boxed{Q^* = \sqrt{\frac{2\,D\,L}{C\,i}}} \qquad T^* = \frac{Q^*}{D} \qquad n^* = \frac{D}{Q^*} \qquad PP = D \cdot LT$$

![Curvas de costo de pedir, de mantener y su suma, con el mínimo en Q* = 600](../../figs/r-stock-costo.png)
*Figura 9. El mínimo está donde se cruzan el costo de pedir y el de mantener. Datos del artículo A del parcial.*

- **Control**: en $Q^*$, el costo de pedir es igual al de mantener, $L/Q^* = C\,i\,Q^*/(2D)$.
- La curva es **plana cerca del mínimo**: redondear $Q^*$ a un **período práctico** cómodo (cada mes, cada 20 días) casi no cambia el costo.
- **¿Cómo se baja el costo?** Bajando $L$, por ejemplo con SMED en las preparaciones. Pedir lotes más chicos sin bajar $L$ **sube** el costo.
- Si se compra por cajas de $k$ unidades, se evalúa $CT$ en los múltiplos de $k$ más cercanos a $Q^*$ y se elige el menor.

### 8.4 Consumo durante el ingreso

Sirve cuando el lote **se fabrica** a una velocidad $V$ mientras se sigue consumiendo a ritmo $D$.

![Stock que sube con pendiente V − D durante θ y baja con pendiente −D; el pico es M < Q](../../figs/r-stock-ingreso.png)
*Figura 10. Mientras entra el lote, también se consume: el pico es $M$, no $Q$.*

$$\theta = \frac{Q}{V} \qquad M = Q\left(1 - \frac{D}{V}\right) \qquad \boxed{Q^* = \sqrt{\frac{2\,D\,L}{C\,i\,(1 - D/V)}}}$$

- Hace falta **$V > D$**. Si $V$ se acerca a $D$, el denominador tiende a cero y $Q^* \to \infty$: habría que producir sin parar. Con $V < D$ el modelo no tiene sentido, porque la producción no alcanza a cubrir el consumo.
- Como el stock promedio es menor, mantener sale más barato, y por eso **el lote óptimo es más grande** que en el modelo básico.
- El $LT$ del punto de pedido incluye sólo la organización y la puesta a punto, no el tiempo de fabricar el lote.

### 8.5 Descuentos por cantidad

![Escalón: dos curvas de CT con salto en a; excedente: precio medio que baja hacia C2](../../figs/r-stock-descuentos.png)
*Figura 11. Izquierda: con escalón, el candidato suele ser el borde $a$. Derecha: con excedente, el precio medio se acerca a $C_2$ sin alcanzarlo. Datos ilustrativos.*

**Escalón**: si $Q \geq a$, **todo el lote** se paga a $C_2 < C_1$.

1. Calcular $Q_2^* = \sqrt{2DL/(C_2\,i)}$. Si $Q_2^* \geq a$, ése es el óptimo.
2. Si no, comparar $CT_1(Q_1^*)$ con $CT_2(a)$ y quedarse con el menor.

El mínimo siempre está en un punto de derivada nula ($Q^*$ de algún tramo) o en un salto ($a$).

**Excedente**: las primeras $a$ unidades se pagan a $C_1$ y sólo **lo que excede** a $a$ se paga a $C_2$. El precio medio es

$$C(Q) = \frac{C_1\,a + C_2\,(Q - a)}{Q} = C_2 + \frac{(C_1 - C_2)\,a}{Q} \qquad \lim_{Q \to \infty} C(Q) = C_2$$

Es continuo en $a$, porque $C(a) = C_1$, y baja hacia $C_2$ **sin alcanzarlo nunca**. El término $k = (C_1 - C_2)\,a$ funciona como un costo fijo más:

$$Q^* = \sqrt{\frac{2D\,(L + k)}{C_2\,i}} \quad (\text{vale si da mayor que } a)$$

**Excedente con mínimo de compra y $L = 0$**: en el tramo a precio $C_1$ queda $CT_1(Q) = C_1 + C_1\,i\,Q/(2D)$, una **recta** creciente. Su mínimo está en la compra mínima. En el tramo con descuento, $k$ hace el papel de $L$ y sigue habiendo un mínimo interior. Se comparan los dos.

### 8.6 Período común y clasificación ABC

Varios artículos de una familia se piden **juntos cada $T$**, así que $Q_j = D_j\,T$. Sumando el costo anual de todos:

$$CT(T) = \sum_j C_jD_j + \frac{L}{T} + \frac{S}{2}\,T \qquad S = \sum_j \delta_j\,D_j \qquad \boxed{T^* = \sqrt{\frac{2L}{S}}} \qquad Q_j^* = D_j\,T^*$$

- $L$ es el costo de **toda** la orden conjunta.
- $\delta_j = C_j\,i$ si se compra, y $C_j\,i\,(1 - D_j/V_j)$ si se fabrica.
- El gráfico de $CT(T)$ es igual al del modelo básico, con $T$ en lugar de $Q$: una recta horizontal, una hipérbola que baja y una recta que sube.

**Clasificación ABC**, según el costo anual $C_jD_j$ ordenado de mayor a menor y acumulado:

- **A**: hasta el 75 % del costo total.
- **B**: del 75 % al 95 %.
- **C**: del 95 % al 100 %.

Los **C** se gestionan con revisión periódica, porque no se justifica un registro permanente.

### 8.7 Restricciones: multiplicadores de Lagrange

Varios artículos comparten un recurso limitado. Los tres modelos se resuelven igual:

1. Calcular cada $Q_j^*$ **sin restricción**, con $\lambda = 0$.
2. Ver cuánto recurso consumen. Si alcanza, la restricción no es efectiva y se terminó.
3. Si no alcanza, el óptimo usa **todo** el recurso. Se prueban valores de $\lambda > 0$ hasta que la restricción se cumpla **con igualdad**.

| Recurso | Restricción | Lote | Unidad de $\lambda$ |
|---|---|---|---|
| Capital | $\sum_j C_j Q_j / 2 \leq I_0$ (inversión **media**) | $\sqrt{\dfrac{2D_jL_j}{C_j\,(i + \lambda)}}$ | 1/tiempo (una tasa) |
| Espacio | $\sum_j v_j Q_j \leq E_0$ (cada artículo ocupa su máximo) | $\sqrt{\dfrac{2D_jL_j}{C_j\,i + 2\lambda v_j}}$ | \$/(volumen·tiempo) |
| Preparación | $\sum_j (D_j/Q_j)\,\tau_j \leq P_0$ | $\sqrt{\dfrac{2D_j\,(L_j + \lambda\tau_j)}{C_j\,i\,(1 - D_j/V_j)}}$ | \$/hora |

**Cómo se interpreta $\lambda$:**

- **Espacio**: el costo marginal de no disponer de una unidad más de espacio. Penaliza más a los artículos voluminosos, que se achican más.
- **Preparación**: el costo marginal de no disponer de una hora más de preparación. Acá subir $\lambda$ **agranda** los lotes: lotes más grandes son menos preparaciones por año.
- **Capital**: el incremento del costo anual por cada peso que se ahorraría si hubiera más capital. Actúa como si la tasa de mantenimiento subiera de $i$ a $i + \lambda$.

**¿Conviene tomar un crédito?** El apunte separa $i = i_1 + i_2$, donde $i_1$ es el costo del capital inmovilizado e $i_2$ el resto de los costos de mantener. Según el apunte, **$i_1 + \lambda$ es la tasa de interés por debajo de la cual conviene aceptar dinero para invertir en stock**.

> **Ojo:** muchos resúmenes simplifican y comparan la tasa del crédito directamente con $\lambda$. Si el enunciado no separa $i_1$, escribí el criterio del apunte y aclará el supuesto. En el parcial 2026, con $I_0 = 23.000$, los dos criterios dan la misma respuesta.

Un atajo útil para el capital: todos los lotes se achican en la misma proporción, así que

$$I(\lambda) = I(0)\,\sqrt{\frac{i}{i + \lambda}} \quad\Longrightarrow\quad \lambda = i\left[\left(\frac{I(0)}{I_0}\right)^2 - 1\right]$$

Así $\lambda$ sale de una sola cuenta, sin tantear.

### 8.8 Así vino en el parcial: ejercicio 3

Una ferretería mayorista gestiona tornillos (A) y tuercas (B), con $i = 20\,\%$ anual y un capital máximo para invertir en stock $I_0$:

| | $D$ (u/año) | $L$ (\$/orden) | $C$ (\$/u) |
|---|---|---|---|
| A (tornillos) | 12.000 | 150 | 50 |
| B (tuercas) | 8.000 | 200 | 80 |

![Inversión media en función de λ con I0 = 23.000 y 28.000, y lotes de A y B en función de λ](../../figs/r-stock-lagrange.png)
*Figura 12. Se sube $\lambda$ hasta que la inversión media iguala a $I_0$. Los dos lotes bajan juntos.*

> **Ojo:** en la foto del enunciado, $I_0$ se lee como **\$ 23.000**, pero el 3 podría ser un 8. Abajo están las dos versiones.

**2) Lote óptimo de A sin la restricción.**

$$Q_A^* = \sqrt{\frac{2 \cdot 12.000 \cdot 150}{50 \cdot 0{,}20}} = \sqrt{360.000} = \textbf{600}$$

Para B: $Q_B^* = \sqrt{2 \cdot 8.000 \cdot 200/(80 \cdot 0{,}20)} = 447{,}2$.

**3) Inversión promedio con los dos lotes óptimos.**

$$I = \frac{50 \cdot 600}{2} + \frac{80 \cdot 447{,}2}{2} = 15.000 + 17.889 = \textbf{32.889}$$

Supera a $I_0$, así que la restricción es **efectiva**.

**1) Valor de $\lambda$.** Con el atajo de §8.7:

| | $I_0 = 23.000$ | $I_0 = 28.000$ |
|---|---|---|
| $\lambda = 0{,}20\,[(32.889/I_0)^2 - 1]$ | **$\approx 0{,}209$** | $\approx 0{,}076$ |
| $Q_A$ con la restricción | 420 | 511 |
| **4)** $Q_B$ con la restricción | **$\approx 313$** | $\approx 381$ |

**5) ¿Conviene un crédito al 12 % anual?** **Sí.** Según el apunte, la tasa límite es $i_1 + \lambda$, que es por lo menos $\lambda$ y, si todo el 20 % es costo del capital, llega a $0{,}20 + 0{,}209 \approx 41\,\%$. Con la comparación simplificada también conviene, porque $\lambda = 20{,}9\,\% > 12\,\%$.

> **Ojo:** si $I_0$ fuera 28.000, $\lambda = 7{,}6\,\%$. Con la comparación simplificada **no** convendría, y con la del apunte ($20\,\% + 7{,}6\,\% = 27{,}6\,\%$), sí. Es otra razón para escribir el criterio completo y aclarar el supuesto.

### 8.9 Demanda aleatoria: stock de seguridad y riesgo de faltante

Si la demanda o el plazo varían, se mantiene un **stock de seguridad (SS)** que absorbe esa variabilidad. El lote se sigue calculando con el modelo básico y la demanda media: lo aleatorio sólo cambia el **punto de pedido**.

![Stock con demanda variable, el SS como piso; normal de la demanda durante el LT con la cola de riesgo de faltante](../../figs/r-stock-aleatorio.png)
*Figura 13. El SS cubre los picos de demanda durante el LT. El RF es la probabilidad de la cola derecha.*

**Riesgo de faltante (RF)**: probabilidad de que la demanda durante el $LT$ supere el punto de pedido. Es una probabilidad **por ciclo** de reposición.

$$PP = \bar d \cdot LT + SS \qquad SS = z \cdot S_d\,\sqrt{LT} \qquad \text{costo anual del SS} = SS \cdot C \cdot i$$

| RF | 1 % | 2 % | 3 % | 5 % | 10 % |
|---|---|---|---|---|---|
| $z$ | 2,33 | 2,05 | 1,88 | 1,645 | 1,28 |

- El desvío se multiplica por **la raíz del tiempo**: si $S_d$ es diario y $LT$ son 9 días, $S_{LT} = 3\,S_d$.
- El SS se redondea **hacia arriba**.
- Se pide cuando **existencias + pendientes de entrega** $\leq PP$.
- La tabla del RF es la de la normal estándar porque la demanda acumulada en el $LT$ es normal: por la propiedad reproductiva si la demanda diaria es normal, o por el teorema central del límite si no lo es.

> **Ojo:** RF 2 % **no** es lo mismo que IPF 98 %. El RF es una probabilidad por ciclo. El IPF es la fracción de la demanda que se entrega directamente desde el stock. Pueden ser muy distintos.

> **Ojo:** "nivel de servicio del 95 %" quiere decir RF = 5 %, o sea $z = 1{,}645$. Dejalo escrito.

### 8.10 Punto de pedido o revisión periódica

![Punto de pedido con Q fijo e intervalos variables; revisión periódica con T fijo y cantidades variables](../../figs/r-stock-sistemas.png)
*Figura 14. Es la pregunta de teoría más repetida en los exámenes, y suele pedir los dos gráficos.*

En **revisión periódica** se revisa cada $T$ y se pide lo que falta para cubrir hasta la llegada del próximo pedido. Por eso el período de incertidumbre es $T + LT$:

$$SS = z\,S_d\,\sqrt{T + LT} \qquad Q = \bar d\,(T + LT) + SS - q_r - q_{pe}$$

donde $q_r$ son las existencias al revisar y $q_{pe}$ los pedidos que todavía no llegaron.

| | Punto de pedido | Revisión periódica |
|---|---|---|
| Lo activa | la **demanda** (el stock llega a PP) | el **tiempo** (cada $T$) |
| Cantidad | fija, $Q^*$ | variable |
| Momento | variable | fijo |
| Registro | se actualiza en cada movimiento | sólo al revisar |
| El SS cubre | $LT$ | $T + LT$: más stock promedio |
| Para qué artículos | A y B, críticos, caros | C, baratos; varios de un mismo proveedor |

### 8.11 Cómo reconocer el modelo y no errarle a las unidades

| Si el enunciado dice… | El modelo es |
|---|---|
| compra, entrega de una sola vez, precio fijo | básico |
| se fabrica, "capacidad de producción" $V$ | consumo durante el ingreso |
| precio menor para **todo** el lote desde $a$ | descuento con escalón |
| precio menor sólo para lo que **excede** $a$ | descuento por excedente |
| varios artículos en una orden conjunta | período común |
| varios artículos y espacio, horas o capital limitado | Lagrange |
| desvío, tabla de frecuencias, RF, "control permanente" | punto de pedido aleatorio |
| "se revisa cada $T$", con existencias y pendientes | revisión periódica |

- Lo más seguro es pasar $D$ a la unidad de tiempo de $i$ y dejar $i$ como viene.
- "Costo anual de mantener \$ $x$ por unidad" **ya es** $C \cdot i$: va directo al denominador.
- Año hábil del apunte: 276 días. Un mes: 30,42 días. Si el enunciado no dice, aclarar qué se usa.
- En la Práctica 7, los ejercicios que no dan $i$ salen con **24 % anual** (2 % mensual). Si falta, declarar el supuesto.

## 9. Transporte, transbordo y asignación

*Fuentes: apunte "Modelos especiales de PL", pizarras de clase del 20/8 y Práctica 5.*

### 9.1 El problema de transporte

Distribuir un producto homogéneo desde $m$ **fuentes**, con oferta $a_i$, hacia $n$ **destinos**, con demanda $b_j$, al menor costo. La variable $x_{ij}$ es lo que se manda de $i$ a $j$, y $c_{ij}$ el costo unitario de esa ruta.

$$\text{Min } W = \sum_i \sum_j c_{ij}\,x_{ij} \quad \text{s.a.} \quad \sum_j x_{ij} \leq a_i \;\;(\text{oferta}) \qquad \sum_i x_{ij} \geq b_j \;\;(\text{demanda}) \qquad x_{ij} \geq 0$$

Si el funcional es de máximo (contribuciones en lugar de costos), sigue siendo un problema de transporte.

![Transporte desbalanceado con destino ficticio; red de transbordo del apunte con la solución óptima](../../figs/r-transporte.png)
*Figura 15. Izquierda: el destino ficticio absorbe la oferta que sobra. Derecha: en el transbordo, lo que entra a cada depósito es igual a lo que sale.*

### 9.2 Balanceo

El modelo está **balanceado** si $\sum a_i = \sum b_j$, y entonces todas las restricciones se escriben con $=$.

| Situación | Se agrega | Qué significa en el óptimo |
|---|---|---|
| Oferta > demanda | destino ficticio, con costo 0 | capacidad ociosa de cada fuente |
| Demanda > oferta | fuente ficticia, con costo 0 | demanda que queda sin cubrir |

### 9.3 Tres propiedades que se preguntan

- **Soluciones enteras automáticas**: si todas las ofertas y demandas son enteras, existe un óptimo entero, por la estructura de la matriz (sólo ceros y unos). No hace falta programación entera.
- **$m + n - 1$**: en un modelo balanceado una de las $m + n$ ecuaciones es redundante. Toda solución básica tiene $m + n - 1$ básicas, o sea **a lo sumo $m + n - 1$ variables positivas**.
- **Degenerada**: tiene menos de $m + n - 1$ variables positivas.

### 9.4 Asignación y transbordo

**Asignación**: es un transporte con todas las ofertas y demandas iguales a 1. Cada origen va a un solo destino y cada destino recibe un solo origen. Alcanza con pedir $x_{ij} \geq 0$: por la integralidad, salen ceros y unos. Si está desbalanceada, se pone $\leq 1$ del lado que sobra y $= 1$ del lado escaso.

**Transbordo**: hay nodos intermedios que reciben y reenvían. Cada uno tiene una restricción de **conservación de flujo**: lo que entra es igual a lo que sale.

- Si el término independiente es 0, es un nodo de paso.
- Si es positivo, el nodo además aporta mercadería: es también un origen.
- Si es negativo, se queda con parte: es también un destino.

Los algoritmos de transporte sirven para el transbordo si se lo formula balanceado.

> **Ojo:** los algoritmos manuales (esquina noroeste, Vogel, MODI, húngaro) **no se toman**. Lo dice el apunte de Torrent. La cátedra **plantea el modelo y lo resuelve con LINDO**.

## 10. Programación entera y mixta

*Fuentes: PLC9 y Práctica 6.*

### 10.1 Tipos y relajado

- **Entero puro**: todas las variables enteras. **Mixto**: algunas. **Binario**: las enteras valen 0 o 1 y representan decisiones de sí o no.
- El conjunto factible de un entero puro es **discreto y no convexo**. Por eso el simplex directo no sirve.
- **Programa relajado**: el mismo modelo sin la condición de enteros. Su óptimo es una **cota**: superior en Max, inferior en Min.
- Redondear el relajado puede dar una solución **no factible** o lejos del óptimo. Sólo es aceptable cuando los valores son grandes.

### 10.2 Métodos

- **De corte**: parten del relajado y agregan restricciones que eliminan zonas sin puntos enteros. Son el fraccionario (para enteros puros) y el mixto.
- **De búsqueda**: enumeran los puntos enteros de forma implícita. El más usado es **ramificación y poda** (*branch and bound*), que es el que usa LINDO.

![Región factible con los puntos enteros, el relajado y el óptimo entero; árbol de ramificación y poda](../../figs/r-entera-bb.png)
*Figura 16. Ejemplo del apunte: el relajado da 63, el óptimo entero es 55.*

**Ramificación y poda**:

1. Resolver el relajado. Si sale entero, se terminó.
2. Elegir una variable fraccionaria $x_k = v$ y abrir dos ramas: $x_k \leq \lfloor v \rfloor$ y $x_k \geq \lfloor v \rfloor + 1$. La franja del medio no tiene enteros.
3. Resolver cada rama como relajado.
4. **Podar** una rama si es no factible, si ya es entera (si mejora la cota, pasa a ser la nueva cota) o si su $z$ no puede superar la cota.
5. Seguir hasta que no queden ramas abiertas.

### 10.3 Modelizar con binarias

| Situación | Restricción |
|---|---|
| Costo fijo si se produce algo | $x_i \leq M\,y_i$, y el costo fijo multiplicado por $y_i$ en el funcional |
| Capacidad que existe sólo si se construye | $\sum_j x_{ij} \leq \text{cap}_i\,y_i$ |
| A lo sumo $k$ de $n$ | $\sum y_i \leq k$ |
| Excluyentes | $y_A + y_B \leq 1$ |
| B sólo si A | $y_B \leq y_A$ |
| Un tope que depende de una decisión | $\sum x \leq 6000\,y_A + 8000\,(1 - y_A)$ |

> **Ojo:** en un programa entero **no valen** los precios duales ni los rangos que imprime LINDO. Son los del relajado con los cortes de la ramificación. La sensibilidad supone que la base óptima no cambia, y en un entero eso no se cumple.

## 11. Modelos de redes

*Fuentes: apunte `REDESUTN_2016.pdf` y resumen de alumnos 2026. Los ejemplos del gráfico son propios.*

### 11.1 Definiciones

- **Red**: nodos unidos por arcos, con un flujo asociado. Un **arco dirigido** permite flujo en un solo sentido.
- **Trayectoria**: sucesión de arcos que une dos nodos. **Ciclo**: trayectoria que vuelve al nodo de partida.
- **Red conexa**: todo par de nodos está unido por alguna trayectoria.
- **Árbol**: nodos conectados sin ciclos. **Árbol de expansión**: árbol que conecta todos los nodos. Con $n$ nodos tiene $n - 1$ arcos.

### 11.2 Los cuatro problemas

![Misma red con el árbol de expansión mínima, la ruta más corta con etiquetas de Dijkstra y el flujo máximo](../../figs/r-redes.png)
*Figura 17. Ejemplo propio: árbol mínimo de longitud 14, ruta más corta O-A-C-T de longitud 12 y flujo máximo 12.*

| Problema | Qué busca | Cómo se resuelve |
|---|---|---|
| **Árbol de expansión mínima** | Conectar todos los nodos sin ciclos, con longitud total mínima (redes eléctricas, de agua, de cable) | Partir de un nodo y agregar siempre el arco más corto que conecta un nodo nuevo, hasta tener $n - 1$ arcos |
| **Ruta más corta** | El camino de menor distancia, costo o tiempo entre dos nodos | **Dijkstra**: etiquetas [distancia, nodo previo]; se fija la menor temporal y se reetiqueta. La ruta se reconstruye hacia atrás |
| **Flujo máximo** | El máximo flujo de la fuente al destino sin superar la capacidad de ningún arco | **Trayectoria en aumento** sobre la red residual, hasta que no quede ninguna con capacidad positiva |
| **Flujo con costo mínimo** | Mandar la oferta a la demanda al menor costo, respetando capacidades | Se plantea el PL y se resuelve con LINDO. Los otros tres, y el transporte, son casos particulares de éste |

**Los modelos lineales:**

- **Ruta más corta**: una variable por arco y una restricción de conservación por nodo, $\sum_j x_{ij} - \sum_j x_{ji} = b_i$, con $b = 1$ en el origen, $-1$ en el destino y $0$ en los demás. Se minimiza $\sum c_{ij}\,x_{ij}$.
- **Flujo máximo**: $0 \leq x_{ij} \leq c_{ij}$, conservación en los nodos intermedios y un arco ficticio $x_O$ que entra a la fuente. Se maximiza $x_O$.

> **Ojo:** el algoritmo del árbol mínimo que describe la cátedra (arrancar de un nodo y agregar el arco más corto hacia un nodo nuevo) se llama **Prim**, aunque en el material aparece como "Kruskal". Kruskal ordena todos los arcos y agrega el más corto que no forme ciclo. Los dos dan el mismo árbol. Si preguntan, describí el procedimiento con el nombre que usa la cátedra y aclaralo.

## 12. La teoría que más se repite

Estas son las preguntas que aparecen en más exámenes, con la idea central de la respuesta y dónde está desarrollada.

| Pregunta | La idea central | Dónde |
|---|---|---|
| Diferencias entre punto de pedido y revisión periódica (con gráficos) | Demanda o tiempo; $Q$ fijo o variable; SS cubre $LT$ o $T + LT$ | §8.10 |
| Límite de $C(Q)$ en el descuento por excedente | $C_2 + k/Q \to C_2$, sin alcanzarlo | §8.5 |
| Mínimo con Lagrange (espacio o preparación) y unidad de $\lambda$ | Lagrangiano, derivar, el $Q^*$ base con un parámetro corregido | §8.7 |
| $\lambda$ en la restricción financiera | Costo marginal de no tener más capital; $i_1 + \lambda$ es la tasa límite | §8.7 |
| Costo total del período común en función de $T$ | Recta + hipérbola + recta; $T^* = \sqrt{2L/S}$ | §8.6 |
| Relación entre $V$ y $D$ en el consumo durante el ingreso | $V > D$; si $V \to D$, $Q^* \to \infty$ | §8.4 |
| Componentes del costo unitario y su mínimo (con gráfico) | $C + L/Q + C\,i\,Q/(2D)$; el mínimo donde pedir = mantener | §8.3 |
| Cómo se calcula la tasa de mantenimiento | Suma de los costos anuales que dependen del stock | §8.1 |
| Teorema fundamental de la dualidad | $u^* = c_BB^{-1}$ son los costos marginales y $w^* = z^*$ | §6.2 |
| Valor implícito: precio sombra o valor marginal, y su signo | Recurso o requerimiento; el signo según Max/Min y $\leq$/$\geq$ | §5.5 |
| Costos reducidos | Cuánto mejorar $c_j$ para que $x_j$ entre | §5.5 |
| Coeficientes de sustitución | $-y_{ij}$: cuánto cambia la básica $x_i$ por unidad de $x_j$ | §4.1 |
| Condición de factibilidad y de optimización (desarrollo) | $\theta_j = \min x_i/y_{ij}$; $z' = z + \theta_j(c_j - z_j)$ | §4.2 |
| Ficticia con valor positivo en el óptimo | El problema es no factible | §4.5 |
| Cómo se detecta la solución no acotada (simplex y gráfico) | Un $c_j - z_j$ que mejora sin ningún $y_{ij} > 0$; RF abierta hacia donde mejora $z$ | §2.2 y §4.5 |
| Holguras complementarias, con un ejemplo | En cada par, uno vale cero | §6.3 |

## 13. Las treinta trampas, una por línea

1. **Región factible no acotada no es solución no acotada.** Un Min sobre una RF abierta puede tener óptimo finito.
2. Si la isobeneficio es paralela a una restricción activa, hay **alternativas**: compará las pendientes.
3. Para saber si un punto es factible, se prueban **todas** las restricciones, incluida $x \geq 0$.
4. La holgura de una $\leq$ es $b - ax$; el exceso de una $\geq$ es $ax - b$.
5. **Degenerada**: una básica vale 0. **Alternativas**: una no básica tiene $c_j - z_j = 0$ en el óptimo.
6. $c_j - z_j = 0$ en una no básica sólo dice algo si la tabla ya es óptima.
7. En Max se busca el mayor $c_j - z_j > 0$; en Min, el más negativo.
8. En la condición de factibilidad se divide **sólo por $y_{ij} > 0$**.
9. Si la columna que entra no tiene ningún $y_{ij} > 0$, la solución es **no acotada**.
10. En la base inicial entra la **ficticia**, no el exceso.
11. Ficticias: **$-M$ en Max, $+M$ en Min**.
12. Ficticia básica con valor positivo en el óptimo: **no factible**. Con valor cero: degenerada.
13. $B^{-1}$ está debajo de las columnas de la **base inicial**, no de las básicas actuales.
14. Bajo cada columna básica, $c_j - z_j = 0$. Si no da cero, la tabla está mal.
15. Si la tabla no trae la fila $z_j$, calculala antes de decidir: $z_j = c_B\,Y_j$.
16. Cambiar un $c_j$ puede romper la optimalidad; cambiar un $b_i$, la factibilidad.
17. Dentro del rango de $c_k$, **el punto óptimo no cambia**: cambia sólo $z^*$, en $\Delta c_k\,x_k^*$.
18. Dentro del rango de $b_k$, **cambian los valores** de las básicas y $z^*$ cambia en $u_k\,\Delta b_k$.
19. El rango de $b_k$ se calcula con la **columna $k$ de $B^{-1}$**, no con la fila.
20. Para una $\geq$, la columna de $B^{-1}$ es la de la ficticia, o la del exceso con el signo cambiado.
21. En un Max, el valor implícito de una $\geq$ es **$\leq 0$**, y la variable dual también.
22. Una restricción $=$ da una variable dual **libre**.
23. Siempre: $W^* = Z^*$. Si no da, hay un error de signo.
24. Si sobra un recurso, su precio sombra es cero; si tiene precio sombra positivo, está agotado.
25. **Precio sombra**: \$ por unidad de recurso. **Costo reducido**: \$ por unidad de producto.
26. En stock, $C$ es el precio y $CT$ el costo real por unidad. Se comparan los $CT$.
27. En el escalón, el candidato con descuento suele ser **el borde $a$**, no $Q_2^*$.
28. El desvío de la demanda se multiplica por **$\sqrt{LT}$** (o $\sqrt{T + LT}$), no por $LT$.
29. "Nivel de servicio del 95 %" es **RF = 5 %**: $z = 1{,}645$. RF 2 % no es IPF 98 %.
30. Con Lagrange, la restricción efectiva se cumple **con igualdad**. Para el crédito, la tasa límite es $i_1 + \lambda$.

## 14. Para practicar

Ejercicios de exámenes reales del `archivo/`, con el mismo formato que el parcial 2026. Todos los resultados se verificaron por cálculo.

### 14.1 Gráfico con preguntas de selección (parcial del 26/07/2025)

$$\text{Min } W = 4x_1 + 6x_2 \quad \text{s.a.} \quad
\begin{cases}
f) \;\; 3x_1 + 4x_2 \leq 24\\
i) \;\; 6x_1 + 9x_2 \geq 36\\
g) \;\; 2x_1 \geq 4\\
h) \;\; 3x_1 + 7x_2 \geq 21\\
x_j \geq 0
\end{cases}$$

Preguntas: ¿cuántas soluciones óptimas tiene? ¿$A = (0; 6)$ es factible? ¿La restricción f se cumple con holgura? ¿La RF es acotada? ¿h es activa?

**Resultados.** La función objetivo es paralela a i), porque $4/6 = 6/9$: hay **óptimos alternativos** en el segmento entre $L = (2; 8/3)$ y $K = (21/5; 6/5)$, con $W^* = 24$. A **no** es factible: no cumple $2x_1 \geq 4$. f se cumple **con holgura** (en L y en K da menos de 24). La RF es acotada. h es **activa** en K.

### 14.2 Tabla óptima, dual y sensibilidad con una restricción $=$ (parcial del 26/07/2025)

Un restaurante vende tres menús: vegetariano ($x_1$), clásico ($x_2$) y proteico ($x_3$), que ganan \$ 4, \$ 2 y \$ 6.

$$\text{Max } Z = 4x_1 + 2x_2 + 6x_3 \quad \text{s.a.} \quad
\begin{cases}
2x_1 + x_2 + x_3 = 10 & \text{(vegetales: deben usarse todos)}\\
x_2 + 2x_3 \leq 20 & \text{(carne)}
\end{cases}$$

**Resultados.** $x_3 = 10$ y el resto cero, $Z^* = 60$. Es **degenerada**: la holgura de la carne es básica y vale 0. El dual es $\text{Min } W = 10u_1 + 20u_2$, con $u_1$ **libre** por la igualdad; su solución es $u = (6;\ 0)$ y $W^* = 60$. Los costos reducidos: un menú vegetariano restaría \$ 8 y uno clásico \$ 4. El proteico puede bajar hasta $c_3 = 2$ sin que cambie la solución. Con 10 vegetales más ($b_1 = 20$) se sale del rango: la nueva solución es $x_1 = 5$, $x_3 = 10$, con $Z = 80$.

### 14.3 Salida de LINDO con una restricción $\geq$ (Steelco, parcial del 27/09/2022)

Tres tipos de acero, que ganan 8, 5 y 2 u.m. por lámina:

```
MAX 8X1 + 5X2 + 2X3
2) 3X1 + 2X2 + X3 <= 200      carbón (t)
3)  X1       + X3 <=  65      hierro (t)
4)  X1 +  X2 + X3 <= 100      horas
5)        X2      >=  10      mínimo de láminas tipo 2

OBJECTIVE FUNCTION VALUE   530
X1  60   (reduced cost 0)          ROW 2)  slack 0    dual price  2.667
X2  10   (reduced cost 0)          ROW 3)  slack 5    dual price  0
X3   0   (reduced cost 0.667)      ROW 4)  slack 30   dual price  0
                                   ROW 5)  slack 0    dual price -0.333
```

| Pregunta | Resultado |
|---|---|
| Interpretación | 60 láminas tipo 1 y 10 tipo 2; el carbón se agota (vale 2,67 por t); sobran 5 t de hierro y 30 h |
| Si el mínimo del tipo 2 pasa a 12 | Está dentro del rango: $Z = 530 - 2 \cdot 1/3 = 529{,}33$ |
| Si se pierden 30 t de carbón | Dentro del rango: $x_1 = 50$, $Z = 530 - 30 \cdot 8/3 = 450$ |
| Ganancia mínima del tipo 3 para producirlo | $c_3 > 2 + 0{,}667 = 2{,}667$ |
| Hasta dónde puede bajar la ganancia del tipo 1 | Hasta $c_1 = 7{,}5$ |
| Con 35 horas menos | Fuera del rango (sólo sobran 30): cambia la base; $x_1 = 55$, $Z = 490$ |
| Dual | $\text{Min } 200u_1 + 65u_2 + 100u_3 + 10u_4$, con $u_4 \leq 0$; $u = (8/3;\ 0;\ 0;\ -1/3)$, $W = 530$ |

### 14.4 Lagrange con capital (Vialmetal, parcial del 30/10/2018)

Tres señales con $i = 25\,\%$ anual y una inversión media que no puede pasar de 7.000 u.m.:

| | A | B | C |
|---|---|---|---|
| $D$ (u/año) | 2.000 | 600 | 1.500 |
| $L$ (u.m./orden) | 60 | 90 | 80 |
| $C$ (u.m./u) | 18 | 70 | 75 |

**Resultados.** Sin restricción, $Q = (230{,}9;\ 78{,}6;\ 113{,}1)$ e $I = 9.070{,}65 > 7.000$. El $\lambda$ exacto es **0,170**, con $Q = (178{,}2;\ 60{,}6;\ 87{,}3)$. La resolución del archivo se quedó con 0,18 por tanteo: en un "valor más cercano", esa diferencia cambia la respuesta.

### 14.5 "¿Conviene un préstamo?" (parcial del 04/11/2021)

Tres artículos con $i = 25\,\%$ anual y un presupuesto (inversión media) de 1.500 u.m.:

| | A | B | C |
|---|---|---|---|
| $D$ (u/año) | 1.000 | 700 | 500 |
| $L$ (u.m./orden) | 120 | 100 | 80 |
| $C$ (u.m./u) | 3 | 2,5 | 2 |

**Resultados.** Sin restricción, $I = 1.840{,}1 > 1.500$. Entonces $\lambda \approx 0{,}126$ y $Q = (461{,}1;\ 385{,}8;\ 326{,}1)$. Según el apunte, conviene un préstamo con una tasa menor que $i_1 + \lambda$. Con la comparación simplificada, conviene si la tasa es menor que 12,6 % anual (§8.7).

### 14.6 Descuento y compra por cajas (parcial 3 de 2024)

Un artículo cuesta USD 25 por unidad, con 10 % de descuento desde 150 unidades. Se usan 20 unidades por día, el pedido cuesta USD 50, $i = 24\,\%$ anual y el plazo es de 6 días.

**Resultados**, con un año de 365 días ($D = 7.300$): con el descuento, $Q^* = \sqrt{2 \cdot 7300 \cdot 50/(22{,}5 \cdot 0{,}24)} = 367{,}7 \geq 150$, así que es válido y **conviene**. $PP = 20 \cdot 6 = 120$ unidades. Si se compra por cajas de 150, dos y tres cajas casi empatan: hay que justificar comparando $CT(300)$ con $CT(450)$.

## Fuentes

- **Classroom IO 402 2026** (`fuentes/classroom-2026/`, bajado el 9/11): pizarras de clase (factibilidad, pasos del simplex, coeficientes de sustitución, transporte), diapositivas de conceptos básicos y de dualidad, prácticas 1, 2 y 4 de 2026, resolución de la Práctica 7 en Excel y el libro *Programación Lineal* de Torrent. La transcripción de las pizarras se usó para la notación de §4 a §6.
- **Apuntes de cátedra** (`fuentes/Material de cursado (2023)/Teoría/`): PLC1 a PLC5, PLC8, PLC9, *Modelos especiales de PL*, `REDESUTN_2016.pdf` y `STOCK16Transp.pdf` (Mascó y Torrent).
- **Parcial del 3/10/2026** (`fuentes/parciales/2026-10-03/`) y **parcial del 26/07/2025** con la resolución de Vaccaro (`fuentes/parciales/2025-07-26/`).
- **Exámenes de años anteriores** (`archivo/Examenes/`): 25 parciales y 21 finales, para las frecuencias de §0.3, la teoría de §12 y los ejercicios de §14.
- **Resumen de alumnos 2026** (`fuentes/resumen-alumnos-2026.pdf`, del Drive de la facu) y los materiales de estudio del parcial (`estudio/parcial/`).
- Todos los números del parcial 2026 y de §14 se verificaron por cálculo exacto (enumeración de bases y re-resolución con el dato perturbado).
- Las figuras se generan con `scripts/io/io-figs-recuperatorio.py`.
