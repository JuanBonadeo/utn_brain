# IO — Práctica 3: Método Simplex

Guía completa de la Práctica 3 (`PL3UTN.pdf`): cómo se ejecuta el Simplex —tablas y
matricial—, el tratamiento de variables ficticias, y los seis ejercicios resueltos.
Contrastado con la resolución oficial de la cátedra (`PL3UTNresol.pdf` y
`PL3UTNresol (1).pdf`) y con el **capítulo 3 del apunte** (PLC3, secciones 3.2 a 3.6).

> **Los resultados de esta guía están verificados por enumeración exacta.** Se enumeraron
> con fracciones exactas las $\binom{n}{m}$ bases de cada programa y se comparó el óptimo
> con el de la resolución oficial. Coinciden en los seis casos. **Salvo en el 2.a, donde
> la resolución oficial tiene dos errores** — están señalados en la Parte 5.

---

# Parte 1 — Cómo se ejecuta el Simplex

## Paso 0: forma estándar. Sin esto no hay tabla.

El Simplex arranca de $\text{Max } z = cx$ s.a. $Ax = b$, $x \geq 0$, con **$b \geq 0$**.
Todo lo demás hay que convertirlo antes de dibujar nada.

```
QUE HAY EN LA RESTRICCION      QUE SE AGREGA              SIRVE DE BASE INICIAL?

  a x  <=  b   (b >= 0)        + 1 holgura   (+1)         SI   -> columna de I
  a x  >=  b   (b >= 0)        - 1 exceso    (-1)         NO   -> queda -1, no sirve
                               + 1 ficticia  (+1)         SI
  a x   =  b   (b >= 0)        + 1 ficticia  (+1)         SI

  b < 0                        multiplicar la fila por -1 PRIMERO
                               (y se da vuelta el sentido de la desigualdad)
```

Reglas que no se negocian:

- **Cada variable nueva aparece en TODAS las restricciones**, con coeficiente 0 donde no
  corresponde. Si no, la matriz no tiene $m$ columnas por fila.
- **Cada variable nueva aparece en la función objetivo**, con $c_j = 0$ para holguras y
  excesos, y con $\pm M$ para las ficticias (penalización) o $1$ (dos fases).
- La **numeración es corrida**: si el problema tiene $x_1, x_2$, la primera holgura es
  $x_3$, y así. No se usan $s_1$, $e_1$, $a_1$.
- En **mínimo** la cátedra escribe las dos formas al lado: `Mín w = …` y su equivalente
  `Máx z = – …`, y al final reporta `W* = –z*`.

## Cuál es la base inicial

**La base inicial es siempre la identidad**, formada por las holguras y las ficticias. Los
excesos **nunca** forman parte de la base inicial: entran con $-1$, no con $+1$.

$$B = I \quad\Longrightarrow\quad B^{-1} = I \quad\Longrightarrow\quad x_B = b$$

De ahí sale la primera tabla sin hacer una sola cuenta.

## El algoritmo de tablas

```
1. FORMA ESTANDAR. Base inicial = holguras + ficticias.
2. ARMAR LA TABLA. Fila cj arriba, columna ci a la izquierda (los cj de las basicas).
3. CALCULAR zj = SUMA_i ci * yij   (producto escalar: columna ci por columna Aj)
4. CALCULAR cj - zj  para toda columna.
5. ¿OPTIMO?
      MAX: optimo si TODOS los (cj - zj) <= 0
      MIN: optimo si TODOS los (cj - zj) >= 0
   Si es optimo -> ir a DIAGNOSTICO.
6. ENTRA: la columna con el (cj - zj) mas favorable.
      MAX: el mayor positivo.   MIN: el menor negativo.
      Empate -> el de MENOR subindice.
7. SALE: theta = min { xi / yij : yij > 0 }.  La fila que da el minimo sale.
      Solo se miran los yij ESTRICTAMENTE POSITIVOS.
      Si NINGUN yij > 0 -> SOLUCION NO ACOTADA. Fin.
      Empate -> sale el de MAYOR subindice (y la proxima tabla sera degenerada).
8. PIVOTEAR sobre yrj: fila r dividida por yrj, y al resto se le resta
   la fila pivote multiplicada por su propio coeficiente en la columna j.
9. Volver a 3.
```

### Cómo se lee la tabla (los tres chequeos de 5 segundos)

| Chequeo | Qué tiene que dar | Para qué sirve |
|---|---|---|
| $z_j$ bajo una columna **básica** | su propio $c_j$ | detecta error aritmético al instante |
| $c_j - z_j$ de las **básicas** | siempre $0$ | idem |
| columnas de la **base inicial** | son $B^{-1}$ | se necesita en sensibilidad y dualidad |

> **No borres la columna de una ficticia aunque salga de la base** si después vas a hacer
> sensibilidad o dualidad: es la única forma de leer esa columna de $B^{-1}$. (Para
> resolver nomás, sí se pueden tirar: una ficticia que sale nunca vuelve a entrar.)

## El algoritmo matricial

Es lo mismo, sin tabla. La cátedra lo pide explícitamente en el Ejercicio 1 —
**seis pasos**, y así los numera la resolución oficial:

```
1. Se busca una solucion basica inicial.
      B, N, xB = B^-1 b, xN = 0, z = cB xB
2. Se calculan los yij.
      B^-1  y luego  Y = B^-1 N
3. Se determinan los zj.
      (z1, ..., zk) = cB Y
4. Se calculan las diferencias cj - zj.
      El mas favorable ENTRA.
5. Se determina el vector que sale.
      theta_j = min { xi / yij : yij > 0 }
6. Se calcula la nueva solucion, el z asociado, y se vuelve al punto 2.
      x'i = xi - theta_j * yij ;  x'r = 0 ;  x'j = theta_j
```

**La diferencia práctica con la tabla:** el matricial recalcula $B^{-1}$ desde cero en cada
iteración; la tabla lo arrastra pivoteando. Dan lo mismo. En el parcial el matricial se pide
para una o dos iteraciones (es carísimo a mano), la tabla para resolver entero.

## Variables ficticias: cuándo y por qué

Con restricciones $\geq$ o $=$ **no hay solución básica factible inmediata**: no aparece la
identidad. Se agregan variables **ficticias** (la cátedra dice *ficticias*, no
*artificiales*) para completar $B = I$. Eso es la **técnica de la base artificial**.

> Las ficticias **no tienen significado físico**. Si el problema original tiene solución,
> en el óptimo tienen que valer **cero**. Si alguna queda en base con valor **positivo**,
> el problema original es **no factible**.

Hay dos formas de forzar que se vayan: **penalización** y **dos fases**.

### Método de penalización (M grande)

Se resuelve el modelo aumentado de una sola pasada, castigando cada ficticia en el
funcional con un coeficiente $M$ positivo y enorme:

```
MAXIMIZAR ->  el coeficiente de la ficticia es  -M
MINIMIZAR ->  el coeficiente de la ficticia es  +M
```

En ambos casos $M > 0$ y, conceptualmente, **mucho mayor que el mayor valor absoluto de los
coeficientes económicos reales** del modelo. Toda la aritmética de la tabla queda en función
de $M$: los $z_j$ y $c_j - z_j$ son binomios del tipo $-6M + 24$, y para comparar se razona
"$M$ es enorme, manda el término en $M$".

**Los cuatro finales posibles:**

| Al alcanzar la condición de optimización… | Conclusión |
|---|---|
| ninguna ficticia en base | óptimo del problema original |
| alguna ficticia en base con **valor nulo** | óptimo del original, y es **degenerado** |
| alguna ficticia en base con **valor estrictamente positivo** | el original es **no factible** |
| se concluye no acotada, con todas las ficticias nulas | el original es **no acotado** |
| se concluye no acotada, con alguna ficticia $\neq 0$ | el original es **no factible** |

### Método de las dos fases

El problema del M grande es computacional: con $M$ enorme los $c_j$ reales quedan
insignificantes frente a los $z_j$, y con errores de redondeo la solución se vuelve
insensible a los coeficientes económicos originales. Las dos fases lo evitan.

```
FASE I    Se reemplaza el funcional original por la SUMA DE LAS FICTICIAS,
          y SIEMPRE se minimiza:      Min f = x_f1 + x_f2 + ...
          (equivalente: Max zeta = -x_f1 - x_f2 - ...)
          Los cj de TODAS las variables reales pasan a valer 0.

          f* = 0  ->  las ficticias son nulas. Hay solucion factible. Sigue Fase II.
          f* > 0  ->  NO HAY SOLUCION FACTIBLE. Se termina aca.

FASE II   Se toma la tabla optima de la Fase I y se la recicla:
            - se ELIMINAN las columnas de las ficticias
            - se REEMPLAZAN los cj por los del funcional ORIGINAL
            - se RECALCULAN zj, cj - zj y z
          Y se sigue el Simplex normal desde ahi.
```

**El caso raro que puede tomarse:** Fase I termina con $f^* = 0$ pero **una ficticia sigue
en base, con valor cero**. Entonces:

- Si existe una no básica **no ficticia** $x_j$ con $y_{fj} \neq 0$, se pivotea sobre
  $y_{fj}$ para sacar la ficticia (acá $y_{fj}$ **puede ser negativo**: como $x_f = 0$, la
  razón $x_f/y_{fj}$ da 0 igual). Queda una SBF inicial **degenerada** y se sigue normal.
- Si **todos** los $y_{fj}$ de las no básicas no ficticias son nulos, esa restricción es
  **analíticamente redundante**: se borran su fila y su columna, y se sigue con la Fase II.

### Efecto espejo

En una restricción $\geq$ con $b \geq 0$, la columna del **exceso** es la columna de la
**ficticia** multiplicada por $-1$, y lo mismo pasa con sus $z_j$. Se mantiene en todas las
iteraciones.

```
    A4 (exceso)  =  - A6 (ficticia)      z4 = - z6
```

Sirve para dos cosas: **chequear** que la tabla está bien, y **ahorrar columnas** (se pueden
no escribir las de las ficticias, porque la información está en las de exceso cambiada de
signo).

## Diagnóstico: qué tipo de solución salió

Esto es lo que se corrige. La tabla final se lee así:

```
UNICA
   Todos los (cj - zj) son NULOS para las basicas y ESTRICTAMENTE NEGATIVOS (max)
   para las no basicas. Ninguna ficticia en base.
   -> "La solucion es unica ya que todos los (cj - zj) son nulos para las variables
       basicas y negativos para las variables no basicas."

ALTERNATIVAS / MULTIPLES
   Optimo alcanzado y hay una columna NO BASICA con (cj - zj) = 0.
   Se hace entrar esa columna: sale otra SBF optima con el MISMO z.
   -> "El optimo se da en un segmento, no en un solo punto."
   La familia completa es la combinacion convexa:
       x* = lambda * S*_1 + (1 - lambda) * S*_2 ,  0 <= lambda <= 1

DEGENERADA
   Optimo alcanzado y alguna variable BASICA vale CERO.
   Sintoma previo: empate en el criterio de salida en alguna iteracion.
   No cambia el valor optimo; cambia como se lo escribe.

NO ACOTADA
   Hay un (cj - zj) que mejora, pero TODOS los yij de esa columna son <= 0.
   Ninguna variable puede salir.
   -> "No puede salir ninguna variable, por lo tanto, el problema tiene solucion
       no acotada."   z = infinito

NO FACTIBLE
   Optimo alcanzado (penalizacion) con una FICTICIA EN BASE Y VALOR > 0.
   O Fase I termina con f* distinto de 0.
   -> "Estoy en el optimo y hay variables ficticias en la base, por lo tanto, el
       problema es no factible, es decir, la region factible es nula (RF = vacio)."
```

> El profesor escribió en la resolución del parcial: *"No confundir región factible no
> acotada con solución no acotada."* La región del ejercicio 2.d es no acotada **y** la
> solución también; pero se puede tener región no acotada con óptimo finito.

## Reglas de desempate (convención del apunte, sección 3.2)

| Empate en… | Regla | Consecuencia |
|---|---|---|
| **entrada** (dos $c_j - z_j$ iguales y máximos) | entra el de **menor** subíndice | ninguna, es solo convención |
| **salida** (dos $\theta_j$ iguales y mínimos) | sale el de **mayor** subíndice | **la próxima solución será degenerada** |

Con degeneración puede pasar que $\theta_j = 0$: entra una variable pero $z$ **no cambia**.
Si eso se repite, el programa puede **ciclar**. El apunte aclara que el ciclado no se observa
en la práctica —los ejemplos cíclicos se construyen a propósito.

## Errores típicos

1. **Olvidarse de que $b$ tiene que ser $\geq 0$** antes de agregar nada. Si hay un $b_i < 0$
   se multiplica la fila por $-1$ primero, y se da vuelta la desigualdad.
2. **Poner la ficticia en una restricción $\leq$.** No hace falta: la holgura ya da la columna
   de la identidad.
3. **Meter el exceso en la base inicial.** Entra con $-1$; no es columna de $I$.
4. **Calcular $\theta$ con $y_{ij} \leq 0$.** Solo se miran los estrictamente positivos. Un
   $y_{ij}$ negativo significa que esa básica *crece* cuando entra $x_j$: no limita nada.
5. **Invertir el criterio de óptimo en mínimo.** En `Min` el óptimo es $c_j - z_j \geq 0$.
   Si convertís a `Max z = –w`, el criterio vuelve a ser $\leq 0$, pero acordate de reportar
   $W^* = -z^*$.
6. **Declarar "no acotada" viendo un solo $y_{ij} \leq 0$.** Tienen que ser **todos** los de
   la columna.
7. **Declarar "no factible" porque quedó una ficticia en base.** Solo si su valor es
   **estrictamente positivo**. Con valor cero, es degenerada, no infactible.
8. **Confundir degeneración con óptimos alternativos.** Degenerada = una **básica** vale 0.
   Alternativos = una **no básica** tiene $c_j - z_j = 0$. Son cosas distintas y pueden darse
   juntas.

---

# Parte 2 — Ejercicios resueltos

## Ejercicio 1 — Simplex matricial y por tablas

$$\text{Max } z = 2x_1 + 3x_2 \quad \text{s.a.} \quad
\begin{cases}
4x_1 + 4x_2 \leq 320\\
2x_1 + 4x_2 \leq 240\\
8x_1 + 4x_2 \leq 560\\
x_j \geq 0
\end{cases}$$

> Es **el mismo problema del Ejercicio 1 de la Práctica 1**, resuelto allá por método
> gráfico. El punto del ejercicio es que el Simplex tiene que dar el mismo vértice.

### Forma estándar

$$\text{Max } z = 2x_1 + 3x_2 + 0x_3 + 0x_4 + 0x_5$$

$$\begin{aligned}
4x_1 + 4x_2 + 1x_3 \phantom{{}+ 1x_4 + 1x_5} &= 320\\
2x_1 + 4x_2 \phantom{{}+ 1x_3} + 1x_4 \phantom{{}+ 1x_5} &= 240\\
8x_1 + 4x_2 \phantom{{}+ 1x_3 + 1x_4} + 1x_5 &= 560\\
x_j &\geq 0
\end{aligned}$$

### a) Algoritmo matricial

**Iteración 1 — paso 1: solución básica inicial.**

$$B = (A_3, A_4, A_5) = \begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}, \qquad
N = (A_1, A_2) = \begin{pmatrix}4&4\\2&4\\8&4\end{pmatrix}$$

$$x_B = (x_3, x_4, x_5)^T = (320; 240; 560)^T, \qquad x_N = (x_1, x_2)^T = (0; 0)^T$$

$$z = c_B\,x_B = (0;0;0)\,(320;240;560)^T = 0$$

**Paso 2: los $y_{ij}$.** Como $B = I$, resulta $B^{-1} = I$ y

$$Y = B^{-1}N = \begin{pmatrix}4&4\\2&4\\8&4\end{pmatrix}$$

**Paso 3: los $z_j$.**

$$(z_1, z_2) = c_B\,Y = (0;0;0)\begin{pmatrix}4&4\\2&4\\8&4\end{pmatrix} = (0;0)$$

**Paso 4: las diferencias.**

$$c_1 - z_1 = 2 - 0 = 2, \qquad c_2 - z_2 = 3 - 0 = 3 \;\Longrightarrow\; \textbf{entra } A_2$$

**Paso 5: el que sale.**

$$\theta_2 = \min\left\{\frac{320}{4};\ \frac{240}{4};\ \frac{560}{4}\right\} = \min\{80; 60; 140\} = 60 \;\Longrightarrow\; \textbf{sale } A_4$$

**Paso 6: nueva solución.**

$$\begin{aligned}
x_1' &= 0 & x_2' &= \theta_2 = 60 & x_3' &= 320 - 60\cdot 4 = 80\\
x_4' &= 240 - 60\cdot 4 = 0 & x_5' &= 560 - 60\cdot 4 = 320 & z &= 3\cdot 60 = 180
\end{aligned}$$

**Iteración 2.** Ahora $B = (A_3, A_2, A_5)$, $N = (A_1, A_4)$, $c_B = (0; 3; 0)$.

$$B = \begin{pmatrix}1&4&0\\0&4&0\\0&4&1\end{pmatrix} \Longrightarrow
B^{-1} = \begin{pmatrix}1&-1&0\\0&\tfrac14&0\\0&-1&1\end{pmatrix}, \qquad
Y = B^{-1}N = \begin{pmatrix}2&-1\\ \tfrac12&\tfrac14\\ 6&-1\end{pmatrix}$$

$$(z_1, z_4) = (0;3;0)\,Y = \left(\tfrac32;\ \tfrac34\right)$$

$$c_1 - z_1 = 2 - \tfrac32 = \tfrac12 > 0 \;\Longrightarrow\; \textbf{entra } A_1,
\qquad c_4 - z_4 = 0 - \tfrac34 = -\tfrac34$$

$$\theta_1 = \min\left\{\frac{80}{2};\ \frac{60}{1/2};\ \frac{320}{6}\right\}
= \min\left\{40;\ 120;\ \tfrac{160}{3}\right\} = 40 \;\Longrightarrow\; \textbf{sale } A_3$$

$$x_1' = 40, \quad x_2' = 60 - 40\cdot\tfrac12 = 40, \quad x_5' = 320 - 40\cdot 6 = 80,
\quad z = 2\cdot 40 + 3\cdot 40 = 200$$

**Iteración 3.** $B = (A_1, A_2, A_5)$, $N = (A_3, A_4)$, $c_B = (2; 3; 0)$.

$$Y = B^{-1}N = \begin{pmatrix}\tfrac12 & -\tfrac12\\[2pt] -\tfrac14 & \tfrac12\\[2pt] -3 & 2\end{pmatrix}
\qquad (z_3, z_4) = (2;3;0)\,Y = \left(\tfrac14;\ \tfrac12\right)$$

$$c_3 - z_3 = -\tfrac14 \leq 0, \qquad c_4 - z_4 = -\tfrac12 \leq 0
\;\Longrightarrow\; \textbf{ÓPTIMO}$$

### b) Algoritmo de tablas

**Tabla 1.** Base inicial $(A_3, A_4, A_5)$.

| $c_i$ | $A_i \backslash A_j$ | $A_1$ (2) | $A_2$ (3) | $A_3$ (0) | $A_4$ (0) | $A_5$ (0) | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|
| 0 | $A_3$ | 4 | 4 | 1 | 0 | 0 | 320 | 80 |
| 0 | $A_4$ | 2 | **4** | 0 | 1 | 0 | 240 | **60** ← sale |
| 0 | $A_5$ | 8 | 4 | 0 | 0 | 1 | 560 | 140 |
| | $z_j$ | 0 | 0 | 0 | 0 | 0 | $z = 0$ | |
| | $c_j - z_j$ | 2 | **3** ↑ entra | 0 | 0 | 0 | | |

**Tabla 2.** Entra $A_2$, sale $A_4$. Pivote $= 4$.

| $c_i$ | $A_i \backslash A_j$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|
| 0 | $A_3$ | **2** | 0 | 1 | −1 | 0 | 80 | **40** ← sale |
| 3 | $A_2$ | 1/2 | 1 | 0 | 1/4 | 0 | 60 | 120 |
| 0 | $A_5$ | 6 | 0 | 0 | −1 | 1 | 320 | 160/3 |
| | $z_j$ | 3/2 | 3 | 0 | 3/4 | 0 | $z = 180$ | |
| | $c_j - z_j$ | **1/2** ↑ entra | 0 | 0 | −3/4 | 0 | | |

**Tabla 3.** Entra $A_1$, sale $A_3$. Pivote $= 2$.

| $c_i$ | $A_i \backslash A_j$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $x_i$ |
|---|---|---|---|---|---|---|---|
| 2 | $A_1$ | 1 | 0 | 1/2 | −1/2 | 0 | 40 |
| 3 | $A_2$ | 0 | 1 | −1/4 | 1/2 | 0 | 40 |
| 0 | $A_5$ | 0 | 0 | −3 | 2 | 1 | 80 |
| | $z_j$ | 2 | 3 | 1/4 | 1/2 | 0 | $z^* = 200$ |
| | $c_j - z_j$ | 0 | 0 | −1/4 | −1/2 | 0 | |

Todos los $c_j - z_j \leq 0$ → **óptimo**.

### Respuesta

```
         40
         40
S*  =     0
          0
         80

z* = 200
```

- $x_1$: unidades del producto 1 — se producen **40**
- $x_2$: unidades del producto 2 — se producen **40**
- $x_3$, $x_4$: holguras de las restricciones 1 y 2 — **nulas**: ambas son **activas**
- $x_5$: holgura de la restricción 3 — **sobran 80 unidades** del recurso 3
- El beneficio máximo es **200**

La solución es **única**, ya que todos los $c_j - z_j$ son nulos para las variables básicas
y estrictamente negativos para las no básicas.

> **Chequeo con la Práctica 1:** el método gráfico daba $x^* = (40; 40)$, $z^* = 200$.
> Coincide. Además $B^{-1}$ se lee en las columnas $A_3, A_4, A_5$ de la tabla final:
> $B^{-1} = \begin{pmatrix} 1/2 & -1/2 & 0\\ -1/4 & 1/2 & 0\\ -3 & 2 & 1\end{pmatrix}$.

---

## Ejercicio 2.a — Solución degenerada

$$\text{Max } z = 3x_1 + 9x_2 \quad \text{s.a.} \quad
\begin{cases} x_1 + 4x_2 \leq 8\\ x_1 + 2x_2 \leq 4\\ x_j \geq 0 \end{cases}$$

Dos restricciones $\leq$: **no hacen falta ficticias**. Base inicial $(A_3, A_4)$.

$$\text{Max } z = 3x_1 + 9x_2 + 0x_3 + 0x_4 \quad \text{s.a.} \quad
\begin{cases} 1x_1 + 4x_2 + 1x_3 + 0x_4 = 8\\ 1x_1 + 2x_2 + 0x_3 + 1x_4 = 4\\ x_j \geq 0 \end{cases}$$

**Tabla 1.**

| $c_i$ | $A_i$ | $A_1$ (3) | $A_2$ (9) | $A_3$ (0) | $A_4$ (0) | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|
| 0 | $A_3$ | 1 | **4** | 1 | 0 | 8 | **2** |
| 0 | $A_4$ | 1 | 2 | 0 | 1 | 4 | **2** |
| | $z_j$ | 0 | 0 | 0 | 0 | $z = 0$ | |
| | $c_j - z_j$ | 3 | **9** ↑ | 0 | 0 | | |

**Empate en la salida** ($2 = 2$). La convención del apunte manda sacar el de **mayor
subíndice**, $A_4$; la resolución oficial saca $A_3$. Da lo mismo en el resultado — pero
**el empate ya anuncia que la próxima solución es degenerada**.

**Tabla 2** (siguiendo a la cátedra: sale $A_3$, pivote $= 4$).

| $c_i$ | $A_i$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|
| 9 | $A_2$ | 1/4 | 1 | 1/4 | 0 | 2 | 8 |
| 0 | $A_4$ | **1/2** | 0 | −1/2 | 1 | **0** | **0** ← sale |
| | $z_j$ | 9/4 | 9 | 9/4 | 0 | $z = 18$ | |
| | $c_j - z_j$ | **3/4** ↑ entra | 0 | −9/4 | 0 | | |

$x_4 = 0$ **siendo básica** → la solución ya es **degenerada**. Entra $A_1$ con
$\theta_1 = 0$: es un pivoteo degenerado, $z$ **no va a cambiar**.

**Tabla 3.** Entra $A_1$, sale $A_4$. Pivote $= 1/2$.

| $c_i$ | $A_i$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $x_i$ |
|---|---|---|---|---|---|---|
| 9 | $A_2$ | 0 | 1 | 1/2 | −1/2 | 2 |
| 3 | $A_1$ | 1 | 0 | −1 | 2 | **0** |
| | $z_j$ | 3 | 9 | 3/2 | 3/2 | $z^* = 18$ |
| | $c_j - z_j$ | 0 | 0 | −3/2 | −3/2 | |

Óptimo. $x_1 = 0$ **siendo básica** → sigue degenerada.

### Respuesta

```
          0
S*  =     2
          0
          0

z* = 18
```

- Se producen **2 unidades** del producto 2, **ninguna** del 1
- Las **dos** restricciones son **activas**: sus holguras son nulas
- El beneficio máximo es **18**

La solución es **degenerada**: una variable básica ($x_1$ en la tabla final) tiene valor
cero. Geométricamente, el vértice $(0; 2)$ tiene **tres** rectas concurrentes en $\mathbb{R}^2$
—las dos restricciones y el eje $x_1 = 0$— cuando alcanzarían dos.

> **La resolución oficial de la cátedra tiene el vector dado vuelta** (escribe
> $x_1^* = 2;\ x_2^* = 0$). Está mal: con $x_1 = 2$, $x_2 = 0$ sería $z = 6$, no 18. Ver
> Parte 5.

> **Degenerada no es lo mismo que múltiple.** Acá el óptimo es un **único punto** $(0;2)$
> alcanzable desde **tres bases distintas** — eso es degeneración. Verificado por
> enumeración: de las $\binom{4}{2} = 6$ combinaciones, 5 son SBF, pero corresponden a
> solo **3 vértices distintos**.

---

## Ejercicio 2.b — Penalización y dos fases sobre el mismo problema

$$\text{Mín } W = 5x_1 + 6x_2 - 7x_3 \quad \text{s.a.} \quad
\begin{cases}
x_1 + 5x_2 - 3x_3 \geq 15\\
5x_1 - 6x_2 + 10x_3 \leq 20\\
x_1 + x_2 + x_3 = 5\\
x_j \geq 0
\end{cases}$$

Una $\geq$, una $\leq$ y una $=$: hace falta **exceso** en la 1ª, **holgura** en la 2ª, y
**dos ficticias** (en la 1ª y en la 3ª).

$$\text{Mín } W = 5x_1 + 6x_2 - 7x_3 \qquad\text{ó}\qquad \text{Máx } z = -5x_1 - 6x_2 + 7x_3$$

$$\begin{aligned}
1x_1 + 5x_2 - 3x_3 - 1x_4 + 0x_5 + 1x_6 + 0x_7 &= 15\\
5x_1 - 6x_2 + 10x_3 + 0x_4 + 1x_5 + 0x_6 + 0x_7 &= 20\\
1x_1 + 1x_2 + 1x_3 + 0x_4 + 0x_5 + 0x_6 + 1x_7 &= 5\\
x_j &\geq 0
\end{aligned}$$

con $x_4$ exceso, $x_5$ holgura, $x_6$ y $x_7$ ficticias.

### b.1) Por penalización

$$\text{Máx } z = -5x_1 - 6x_2 + 7x_3 + 0x_4 + 0x_5 - Mx_6 - Mx_7$$

**Tabla 1.** Base $(A_6, A_5, A_7)$, $c_B = (-M; 0; -M)$.

| $c_i$ | $A_i$ | $A_1$ (−5) | $A_2$ (−6) | $A_3$ (7) | $A_4$ (0) | $A_5$ (0) | $A_6$ (−M) | $A_7$ (−M) | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|---|---|
| −M | $A_6$ | 1 | **5** | −3 | −1 | 0 | 1 | 0 | 15 | **3** ← sale |
| 0 | $A_5$ | 5 | −6 | 10 | 0 | 1 | 0 | 0 | 20 | — |
| −M | $A_7$ | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 5 | 5 |
| | $z_j$ | −2M | −6M | 2M | M | 0 | −M | −M | $z = -20M$ | |
| | $c_j - z_j$ | −5+2M | **−6+6M** ↑ | 7−2M | −M | 0 | 0 | 0 | | |

Con $M$ enorme, el mayor $c_j - z_j$ es $-6 + 6M$ → entra $A_2$.

**Tabla 2.** Base $(A_2, A_5, A_7)$.

| $c_i$ | $A_i$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|---|---|
| −6 | $A_2$ | 1/5 | 1 | −3/5 | −1/5 | 0 | 1/5 | 0 | 3 | — |
| 0 | $A_5$ | 31/5 | 0 | 32/5 | −6/5 | 1 | 6/5 | 0 | 38 | 95/16 |
| −M | $A_7$ | 4/5 | 0 | **8/5** | 1/5 | 0 | −1/5 | 1 | 2 | **5/4** ← sale |
| | $z_j$ | $-\tfrac65-\tfrac45M$ | −6 | $\tfrac{18}5-\tfrac85M$ | $\tfrac65-\tfrac M5$ | 0 | $-\tfrac65+\tfrac M5$ | −M | $z = -18-2M$ | |
| | $c_j - z_j$ | $-\tfrac{19}5+\tfrac45M$ | 0 | $\tfrac{17}5+\tfrac85M$ ↑ | $-\tfrac65+\tfrac M5$ | 0 | $\tfrac65-\tfrac{6M}5$ | 0 | | |

**Tabla 3.** Entra $A_3$, sale $A_7$. Salieron las dos ficticias.

| $c_i$ | $A_i$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $x_i$ |
|---|---|---|---|---|---|---|---|---|---|
| −6 | $A_2$ | 1/2 | 1 | 0 | −1/8 | 0 | 1/8 | 3/8 | 15/4 |
| 0 | $A_5$ | 3 | 0 | 0 | −2 | 1 | 2 | −4 | 30 |
| 7 | $A_3$ | 1/2 | 0 | 1 | 1/8 | 0 | −1/8 | 5/8 | 5/4 |
| | $z_j$ | 1/2 | −6 | 7 | 13/8 | 0 | −13/8 | 17/8 | $z^* = -55/4$ |
| | $c_j - z_j$ | −11/2 | 0 | 0 | −13/8 | 0 | $-M+\tfrac{13}8$ | $-M-\tfrac{17}8$ | $W^* = 55/4$ |

Todos los $c_j - z_j \leq 0$ y **ninguna ficticia en base** → óptimo del problema original.

### b.2) Por dos fases

**FASE I.** Programa auxiliar: $\text{Mín } \Phi = x_6 + x_7$, ó $\text{Máx } \zeta = -x_6 - x_7$.
Los $c_j$ de $x_1$ a $x_5$ pasan a valer 0.

| $c_i$ | $A_i$ | $A_1$ (0) | $A_2$ (0) | $A_3$ (0) | $A_4$ (0) | $A_5$ (0) | $A_6$ (−1) | $A_7$ (−1) | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|---|---|
| −1 | $A_6$ | 1 | **5** | −3 | −1 | 0 | 1 | 0 | 15 | **3** ← sale |
| 0 | $A_5$ | 5 | −6 | 10 | 0 | 1 | 0 | 0 | 20 | — |
| −1 | $A_7$ | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 5 | 5 |
| | $z_j$ | −2 | −6 | 2 | 1 | 0 | −1 | −1 | $\zeta = -20$ | |
| | $c_j - z_j$ | 2 | **6** ↑ | −2 | −1 | 0 | 0 | 0 | | |

| $c_i$ | $A_i$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | $A_2$ | 1/5 | 1 | −3/5 | −1/5 | 0 | 1/5 | 0 | 3 | — |
| 0 | $A_5$ | 31/5 | 0 | 32/5 | −6/5 | 1 | 6/5 | 0 | 38 | 95/16 |
| −1 | $A_7$ | 4/5 | 0 | **8/5** | 1/5 | 0 | −1/5 | 1 | 2 | **5/4** ← sale |
| | $z_j$ | −4/5 | 0 | −8/5 | −1/5 | 0 | 1/5 | −1 | $\zeta = -2$ | |
| | $c_j - z_j$ | 4/5 | 0 | **8/5** ↑ | 1/5 | 0 | −6/5 | 0 | | |

| $c_i$ | $A_i$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $x_i$ |
|---|---|---|---|---|---|---|---|---|---|
| 0 | $A_2$ | 1/2 | 1 | 0 | −1/8 | 0 | 1/8 | 3/8 | 15/4 |
| 0 | $A_5$ | 3 | 0 | 0 | −2 | 1 | 2 | −4 | 30 |
| 0 | $A_3$ | 1/2 | 0 | 1 | 1/8 | 0 | −1/8 | 5/8 | 5/4 |
| | $z_j$ | 0 | 0 | 0 | 0 | 0 | 0 | 0 | $\zeta^* = 0$ |
| | $c_j - z_j$ | 0 | 0 | 0 | 0 | 0 | −1 | −1 | |

$\zeta^* = 0$ y ninguna ficticia en base → **hay solución factible**. Sigue la Fase II.

> **Atajo del apunte:** no hacía falta la última tabla. Apenas se ve que la ficticia
> abandona la base, ya se puede asegurar que la próxima tabla es la de óptimo de la Fase I.

**FASE II.** Se borran las columnas $A_6$ y $A_7$, se reponen los $c_j$ originales
($-5, -6, 7, 0, 0$) y se recalculan $z_j$ y $c_j - z_j$.

| $c_i$ | $A_i$ | $A_1$ (−5) | $A_2$ (−6) | $A_3$ (7) | $A_4$ (0) | $A_5$ (0) | $x_i$ |
|---|---|---|---|---|---|---|---|
| −6 | $A_2$ | 1/2 | 1 | 0 | −1/8 | 0 | 15/4 |
| 0 | $A_5$ | 3 | 0 | 0 | −2 | 1 | 30 |
| 7 | $A_3$ | 1/2 | 0 | 1 | 1/8 | 0 | 5/4 |
| | $z_j$ | 1/2 | −6 | 7 | 13/8 | 0 | $z^* = -55/4$ |
| | $c_j - z_j$ | −11/2 | 0 | 0 | −13/8 | 0 | $W^* = 55/4$ |

**Misma tabla óptima que por penalización.** Ese es el punto del ejercicio: los dos métodos
llegan al mismo lado.

### Respuesta

```
           0
        15/4
S*  =    5/4
           0
          30

W* = 55/4 = 13,75
```

- No se usa nada de $x_1$; $x_2 = 3{,}75$ y $x_3 = 1{,}25$
- $x_4 = 0$: la restricción 1 ($\geq 15$) es **activa**, se cumple con igualdad
- $x_5 = 30$: la restricción 2 se cumple **con holgura** de 30 unidades
- El costo mínimo es **13,75**

La solución es **única**: todos los $c_j - z_j$ son nulos para las básicas y estrictamente
negativos para las no básicas.

**Chequeo aritmético:** $0 + 5(15/4) - 3(5/4) = 75/4 - 15/4 = 15$ ✓ (activa) ·
$0 - 6(15/4) + 10(5/4) = -10 \leq 20$ ✓ (holgura $= 30$) · $0 + 15/4 + 5/4 = 5$ ✓ ·
$W = 6(15/4) - 7(5/4) = 90/4 - 35/4 = 55/4$ ✓

---

## Ejercicio 2.c — No factible

$$\text{Máx } z = 3x_1 + 2x_2 \quad \text{s.a.} \quad
\begin{cases} 2x_1 + x_2 \leq 2\\ 3x_1 + 4x_2 \geq 12\\ x_j \geq 0 \end{cases}$$

Forma estándar con $x_3$ holgura, $x_4$ exceso y $x_5$ ficticia:

$$\begin{aligned}
2x_1 + 1x_2 + 1x_3 + 0x_4 + 0x_5 &= 2\\
3x_1 + 4x_2 + 0x_3 - 1x_4 + 1x_5 &= 12\\
x_j &\geq 0
\end{aligned}$$

**FASE I.** $\text{Máx } \zeta = -x_5$.

| $c_i$ | $A_i$ | $A_1$ (0) | $A_2$ (0) | $A_3$ (0) | $A_4$ (0) | $A_5$ (−1) | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|
| 0 | $A_3$ | 2 | **1** | 1 | 0 | 0 | 2 | **2** ← sale |
| −1 | $A_5$ | 3 | 4 | 0 | −1 | 1 | 12 | 3 |
| | $z_j$ | −3 | −4 | 0 | 1 | −1 | $\zeta = -12$ | |
| | $c_j - z_j$ | 3 | **4** ↑ | 0 | −1 | 0 | | |

| $c_i$ | $A_i$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $x_i$ |
|---|---|---|---|---|---|---|---|
| 0 | $A_2$ | 2 | 1 | 1 | 0 | 0 | 2 |
| −1 | $A_5$ | −5 | 0 | −4 | −1 | 1 | **4** |
| | $z_j$ | 5 | 0 | 4 | 1 | −1 | $\zeta = -4$ |
| | $c_j - z_j$ | −5 | 0 | −4 | −1 | 0 | |

Todos los $c_j - z_j \leq 0$ → **óptimo de la Fase I alcanzado**, pero con
$\zeta^* = -4 \neq 0$ y la ficticia $x_5 = 4 \neq 0$ **en base**.

### Respuesta

$$\text{RF} = \emptyset$$

Estoy en el óptimo y hay una variable ficticia en la base con valor positivo, por lo tanto,
el problema es **no factible**, es decir, la región factible es nula ($\text{RF} = \emptyset$).

**Por qué, sin tablas:** de $2x_1 + x_2 \leq 2$ con $x_j \geq 0$ se sigue $x_1 \leq 1$ y
$x_2 \leq 2$, y entonces $3x_1 + 4x_2 \leq 3 + 8 = 11 < 12$. Las dos restricciones son
incompatibles. La enumeración exacta confirma: de las $\binom{4}{2} = 6$ bases posibles,
**ninguna** da una solución factible.

---

## Ejercicio 2.d — No acotada

$$\text{Máx } z = 8x_1 + 30x_2 \quad \text{s.a.} \quad
\begin{cases}
10x_1 + 12x_2 \geq 60\\
3x_1 - 4x_2 \leq 12\\
-3x_1 + 2x_2 \leq 30\\
x_j \geq 0
\end{cases}$$

$$\begin{aligned}
10x_1 + 12x_2 - 1x_3 + 0x_4 + 0x_5 + 1x_6 &= 60\\
3x_1 - 4x_2 + 0x_3 + 1x_4 + 0x_5 + 0x_6 &= 12\\
-3x_1 + 2x_2 + 0x_3 + 0x_4 + 1x_5 + 0x_6 &= 30\\
x_j &\geq 0
\end{aligned}$$

con $x_3$ exceso, $x_4$ y $x_5$ holguras, $x_6$ ficticia. Por **penalización**:
$\text{Máx } z = 8x_1 + 30x_2 + 0x_3 + 0x_4 + 0x_5 - Mx_6$.

**Tabla 1.**

| $c_i$ | $A_i$ | $A_1$ (8) | $A_2$ (30) | $A_3$ (0) | $A_4$ (0) | $A_5$ (0) | $A_6$ (−M) | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|---|
| −M | $A_6$ | 10 | **12** | −1 | 0 | 0 | 1 | 60 | **5** ← sale |
| 0 | $A_4$ | 3 | −4 | 0 | 1 | 0 | 0 | 12 | — |
| 0 | $A_5$ | −3 | 2 | 0 | 0 | 1 | 0 | 30 | 15 |
| | $z_j$ | −10M | −12M | M | 0 | 0 | −M | $z = -60M$ | |
| | $c_j - z_j$ | 8+10M | **30+12M** ↑ | −M | 0 | 0 | 0 | | |

**Tabla 2.** Entra $A_2$, sale $A_6$ (la ficticia se va — no vuelve, se puede borrar la columna).

| $c_i$ | $A_i$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|
| 30 | $A_2$ | 5/6 | 1 | −1/12 | 0 | 0 | 5 | — |
| 0 | $A_4$ | 19/3 | 0 | −1/3 | 1 | 0 | 32 | — |
| 0 | $A_5$ | −14/3 | 0 | **1/6** | 0 | 1 | 20 | **120** ← sale |
| | $z_j$ | 25 | 30 | −5/2 | 0 | 0 | $z = 150$ | |
| | $c_j - z_j$ | −17 | 0 | **5/2** ↑ | 0 | 0 | | |

**Tabla 3.** Entra $A_3$, sale $A_5$.

| $c_i$ | $A_i$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|
| 30 | $A_2$ | **−3/2** | 1 | 0 | 0 | 1/2 | 15 | — |
| 0 | $A_4$ | **−3** | 0 | 0 | 1 | 2 | 72 | — |
| 0 | $A_3$ | **−28** | 0 | 1 | 0 | 6 | 120 | — |
| | $z_j$ | −45 | 30 | 0 | 0 | 15 | $z = 450$ | |
| | $c_j - z_j$ | **53** ↑ entra | 0 | 0 | 0 | −15 | | |

$c_1 - z_1 = 53 > 0$: conviene que entre $A_1$. Pero **toda su columna es negativa**
($-3/2$, $-3$, $-28$): no hay ningún $y_{i1} > 0$, no se puede calcular $\theta_1$.

### Respuesta

$$z = \infty$$

No puede salir ninguna variable, por lo tanto, el problema tiene **solución no acotada**.

**Verificación directa.** Desde el punto factible $(x_1; x_2) = (0; 15)$, la dirección
$d = (4; 3)$ es de recesión:

$$3(4) - 4(3) = 0 \leq 0 \quad\checkmark \qquad -3(4) + 2(3) = -6 \leq 0 \quad\checkmark
\qquad 10(4) + 12(3) = 76 > 0 \quad\checkmark$$

y sobre esa dirección $c \cdot d = 8(4) + 30(3) = 122 > 0$. Entonces
$z(0 + 4t;\ 15 + 3t) = 450 + 122t \to \infty$. Confirmado.

> **No confundir región factible no acotada con solución no acotada.** Acá pasan las dos
> cosas, pero son independientes: una región no acotada puede tener óptimo finito si el
> funcional "apunta" hacia adentro.

---

## Ejercicio 2.e — Óptimos alternativos

$$\text{Mín } W = 24x_1 + 36x_2 + 24x_3 + 36x_4 \quad \text{s.a.} \quad
\begin{cases} 6x_1 + 4x_2 = 100\\ 2x_3 + 3x_4 = 24\\ x_j \geq 0 \end{cases}$$

Dos igualdades: **dos ficticias**, ninguna holgura. Por penalización, en **mínimo** el
coeficiente es $+M$:

$$\text{Mín } W = 24x_1 + 36x_2 + 24x_3 + 36x_4 + Mx_5 + Mx_6$$

$$\begin{aligned}
6x_1 + 4x_2 + 0x_3 + 0x_4 + 1x_5 + 0x_6 &= 100\\
0x_1 + 0x_2 + 2x_3 + 3x_4 + 0x_5 + 1x_6 &= 24\\
x_j &\geq 0
\end{aligned}$$

> **Ojo con el criterio de óptimo:** el problema se resuelve como **mínimo**, así que el
> óptimo es cuando **todos** los $c_j - z_j \geq 0$, y entra el **más negativo**.

**Tabla 1.**

| $c_i$ | $A_i$ | $A_1$ (24) | $A_2$ (36) | $A_3$ (24) | $A_4$ (36) | $A_5$ (M) | $A_6$ (M) | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|---|
| M | $A_5$ | **6** | 4 | 0 | 0 | 1 | 0 | 100 | **100/6** ← sale |
| M | $A_6$ | 0 | 0 | 2 | 3 | 0 | 1 | 24 | — |
| | $z_j$ | 6M | 4M | 2M | 3M | M | M | $W = 124M$ | |
| | $c_j - z_j$ | **24−6M** ↑ | 36−4M | 24−2M | 36−3M | 0 | 0 | | |

**Tabla 2.** Entra $A_1$, sale $A_5$.

| $c_i$ | $A_i$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|---|
| 24 | $A_1$ | 1 | 4/6 | 0 | 0 | 1/6 | 0 | 100/6 | — |
| M | $A_6$ | 0 | 0 | 2 | **3** | 0 | 1 | 24 | **8** ← sale |
| | $z_j$ | 24 | 16 | 2M | 3M | 4 | M | $W = 400+24M$ | |
| | $c_j - z_j$ | 0 | 20 | 24−2M | **36−3M** ↑ | −4+M | 0 | | |

**Tabla 3.** Entra $A_4$, sale $A_6$.

| $c_i$ | $A_i$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $x_i$ |
|---|---|---|---|---|---|---|---|---|
| 24 | $A_1$ | 1 | 4/6 | 0 | 0 | 1/6 | 0 | 100/6 |
| 36 | $A_4$ | 0 | 0 | 2/3 | 1 | 0 | 1/3 | 8 |
| | $z_j$ | 24 | 16 | 24 | 36 | 4 | 12 | $W^* = 688$ |
| | $c_j - z_j$ | 0 | 20 | **0** | 0 | −4+M | −12+M | |

Todos los $c_j - z_j \geq 0$ (con $M$ grande, $-4+M > 0$ y $-12+M > 0$) → **óptimo**.
Ninguna ficticia en base.

Pero **$c_3 - z_3 = 0$ siendo $x_3$ NO básica** → hay **solución alternativa**. Se la obtiene
haciendo entrar $A_3$ ($\theta = 8/(2/3) = 12$, sale $A_4$):

| $c_i$ | $A_i$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $x_i$ |
|---|---|---|---|---|---|---|---|---|
| 24 | $A_1$ | 1 | 4/6 | 0 | 0 | 1/6 | 0 | 100/6 |
| 24 | $A_3$ | 0 | 0 | 1 | 3/2 | 0 | 1/2 | 12 |
| | $z_j$ | 24 | 16 | 24 | 36 | 4 | 12 | $W^* = 688$ |
| | $c_j - z_j$ | 0 | 20 | 0 | **0** | −4+M | −12+M | |

Mismo $W^*$. Ahora $c_4 - z_4 = 0$ con $x_4$ no básica: es el espejo del anterior.

### Respuesta

```
        100/6                    100/6
            0                        0
S*  =       0            S*  =      12
  1         8              2          0

W* = 688                 W* = 688
```

- Se compran **$100/6 \approx 16{,}67$** unidades de 1, **y** o bien 8 de 4, o bien 12 de 3
- Nunca conviene el ingrediente 2 ($c_2 - z_2 = 20 > 0$, encarecería)
- El costo mínimo es **688** en cualquiera de los dos casos

**El óptimo se da en un segmento, no en un solo punto.** La familia completa de óptimos es
la combinación convexa de las dos SBF óptimas:

$$S^* = \lambda\,(100/6;\ 0;\ 0;\ 8)^T + (1-\lambda)\,(100/6;\ 0;\ 12;\ 0)^T,
\qquad 0 \leq \lambda \leq 1$$

**Por qué pasa, mirando el modelo:** las dos restricciones están **desacopladas** (una en
$x_1,x_2$ y otra en $x_3,x_4$). En la segunda, el costo por unidad de recurso es
$24/2 = 12$ vía $x_3$ y $36/3 = 12$ vía $x_4$ — **exactamente el mismo**. Por eso da igual
cuál usar. En la primera, $24/6 = 4 < 36/4 = 9$: ahí $x_1$ gana claro y no hay empate.

---

# Parte 3 — Ejercicio 3: número máximo de soluciones básicas

Una solución básica se obtiene eligiendo $m$ columnas de las $n$ de la matriz $A$ en **forma
estándar** y anulando las $n - m$ restantes. El máximo posible de combinaciones es

$$C_{n,m} = \binom{n}{m} = \frac{n!}{(n-m)!\,m!}$$

Es un **máximo**, no un conteo: algunas combinaciones no son base ($\det = 0$) y otras dan
soluciones **no factibles** (alguna componente negativa).

Contando $n$ sobre la forma estándar (holguras y excesos incluidos, **ficticias no** — son
un artificio del método, no del programa):

| | Variables reales | Restricciones $m$ | Extras (h/e) | $n$ | $\binom{n}{m}$ | SBF reales | Vértices distintos |
|---|---|---|---|---|---|---|---|
| **Ej. 1** | 2 | 3 (3 $\leq$) | 3 holg. | 5 | **10** | 5 | 5 |
| **Ej. 2.a** | 2 | 2 (2 $\leq$) | 2 holg. | 4 | **6** | 5 | **3** ← degenerada |
| **Ej. 2.b** | 3 | 3 ($\geq$, $\leq$, $=$) | 1 exc. + 1 holg. | 5 | **10** | 3 | 3 |
| **Ej. 2.c** | 2 | 2 ($\leq$, $\geq$) | 1 holg. + 1 exc. | 4 | **6** | **0** | 0 ← RF $= \emptyset$ |
| **Ej. 2.d** | 2 | 3 ($\geq$, $\leq$, $\leq$) | 1 exc. + 2 holg. | 5 | **10** | 3 | 3 |
| **Ej. 2.e** | 4 | 2 (2 $=$) | ninguna | 4 | **6** | 4 | 4 |

> Las columnas *SBF reales* y *Vértices distintos* no las pide el ejercicio: son la
> verificación por enumeración exacta. Sirven para leer dos cosas de un vistazo:
> **2.a** tiene más bases factibles (5) que vértices (3) → **degeneración**; **2.c** tiene
> cero → **no factible**.

**Si se cuentan también las ficticias** (interpretación alternativa, sobre el modelo
aumentado que efectivamente se tabula):

| | $n$ con ficticias | $m$ | $\binom{n}{m}$ |
|---|---|---|---|
| Ej. 1 | 5 (ninguna ficticia) | 3 | 10 |
| Ej. 2.a | 4 (ninguna) | 2 | 6 |
| Ej. 2.b | 7 (2 fict.) | 3 | 35 |
| Ej. 2.c | 5 (1 fict.) | 2 | 10 |
| Ej. 2.d | 6 (1 fict.) | 3 | 20 |
| Ej. 2.e | 6 (2 fict.) | 2 | 15 |

La respuesta que corresponde dar es la **primera tabla**: la pregunta es sobre "el programa
lineal", y las ficticias no pertenecen al programa lineal.

**El punto del ejercicio** es el mismo que el del cierre de la Unidad 2: comparar
$\binom{n}{m}$ contra la cantidad de iteraciones que efectivamente hizo el Simplex. En el
Ejercicio 1 hay 10 bases posibles y el Simplex llegó al óptimo en **2 iteraciones**, tocando
3 de los 5 vértices. Esa es la razón de ser del método.

---

# Parte 4 — Ejercicio 4: LINDO / Solver

Pide resolver los mismos programas por software. No hay resolución oficial de esta parte
más allá de la mención `d) Solución en el infinito (lindo)` en el PDF de la cátedra — que
confirma el diagnóstico del 2.d.

Lo que hay que saber leer del output:

| Diagnóstico | LINDO dice | Solver de Excel dice |
|---|---|---|
| óptimo único | `LP OPTIMUM FOUND AT STEP n` | *Solver encontró una solución* |
| no acotada | `UNBOUNDED SOLUTION` | *Los valores de la celda objetivo no convergen* |
| no factible | `NO FEASIBLE SOLUTION` | *Solver no encontró una solución factible* |
| alternativas | óptimo con un `REDUCED COST = 0` en una variable **no básica** | ídem, en el informe de sensibilidad |

Material de apoyo en `fuentes/`: `Material de cursado (2023)/Práctica/PROBLEMAS RESUELTOS CON LINDO.pdf`.

---

# Parte 5 — Errores de la resolución oficial

Los tres detectados están en `PL3UTNresol.pdf`. Ninguno cambia el método; sí cambian el
número que uno copia si no chequea.

1. **Ejercicio 2.a, cuadro final (pág. 2).** Escribe $x_1^* = 2;\ x_2^* = 0;\ z^* = 18$.
   Está **dado vuelta**. La propia tabla final de la resolución tiene $A_2$ básica con
   valor 2 y $A_1$ básica con valor 0, o sea $x_1 = 0$, $x_2 = 2$. Y con $x_1 = 2$,
   $x_2 = 0$ daría $z = 3(2) = 6 \neq 18$. **Correcto: $x_1^* = 0$, $x_2^* = 2$, $z^* = 18$.**
   Verificado por enumeración exacta.

2. **Ejercicio 2.a, segunda tabla (pág. 2).** La fila $c_j - z_j$ tiene los **signos
   invertidos**: escribe $-3/4$ bajo $A_1$ y $9/4$ bajo $A_3$; con $c_B = (9; 0)$ corresponde
   $c_1 - z_1 = 3 - 9/4 = +3/4$ y $c_3 - z_3 = 0 - 9/4 = -9/4$. Escribieron $z_j - c_j$.
   El pivoteo que hacen a continuación (entra $A_1$) es el correcto **con los signos bien**;
   con los signos como los escribieron sería injustificable en un problema de máximo.

3. **Ejercicio 1, segunda tabla (pág. 1).** $c_4 - z_4$ figura como $3/4$; corresponde
   $-3/4$. El PDF de 27 páginas (`PL3UTNresol (1).pdf`) lo tiene bien.

---

# Pendientes

- **Ejercicio 4 sin hacer.** No hay corridas de LINDO ni de Solver. Si el parcial las pide,
  hay que generarlas.
- La regla de desempate en la salida (**mayor subíndice**) no la respeta la resolución
  oficial en el 2.a. No cambia el resultado, pero conviene saber que la cátedra a veces la
  saltea.
- El apunte (PLC3, 3.6) trae dos casos que la Práctica 3 **no** ejercita y que sí pueden
  aparecer: **redundancia analítica** (Fase I termina con $f^* = 0$ y una ficticia básica
  con valor nulo cuyos $y_{fj}$ son todos cero → se borra fila y columna) y **ciclado**.

---

# Los seis finales del Simplex, en una tabla

| Qué ves en la tabla | Tipo | Frase de cátedra |
|---|---|---|
| $c_j - z_j$ nulos en básicas, negativos (máx) en no básicas | **única** | "La solución es única ya que todos los $(c_j - z_j)$ son nulos para las variables básicas y negativos para las no básicas." |
| óptimo + una **no básica** con $c_j - z_j = 0$ | **alternativas** | "El óptimo se da en un segmento, no en un solo punto." |
| óptimo + una **básica** con valor 0 | **degenerada** | (empate previo en el criterio de salida) |
| $c_j - z_j$ mejora pero **todos** los $y_{ij} \leq 0$ | **no acotada** | "No puede salir ninguna variable, por lo tanto, el problema tiene solución no acotada." |
| óptimo + **ficticia en base con valor > 0** | **no factible** | "Estoy en el óptimo y hay variables ficticias en la base, por lo tanto, el problema es no factible, es decir, la región factible es nula (RF = ∅)." |
| Fase I termina con $f^* \neq 0$ | **no factible** | ídem |
