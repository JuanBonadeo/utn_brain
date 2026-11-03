# Machete — Método Simplex

Una carilla. El desarrollo completo y los ejercicios están en [[practica-3-simplex]].

## Las dos condiciones del Simplex

El método hace dos preguntas distintas en cada iteración y en este orden:

```text
1. CONDICION DE OPTIMALIDAD   ¿la solucion actual ya es optima? Si no, ¿que ENTRA?
2. CONDICION DE FACTIBILIDAD  ¿cuanto puede crecer la que entra sin romper x >= 0?
                              La respuesta determina que variable SALE.
```

**Condición de optimalidad — fila $C_j-Z_j$.**

```text
MAX   todos Cj-Zj <= 0 -> OPTIMO     | si no: entra el MAYOR POSITIVO
MIN   todos Cj-Zj >= 0 -> OPTIMO     | si no: entra el MENOR NEGATIVO
```

**Condición de factibilidad — columna entrante.** Mantiene no negativas las variables
básicas mientras aumenta la variable que entra:

```text
theta_i = xi/yij     SOLO para yij > 0

sale la fila con el MENOR theta >= 0
```

- $y_{ij}=0$ o $y_{ij}<0$: esa fila **no limita** el crecimiento; no se divide.
- $\theta=0$ es válido: produce una solución degenerada.
- Si ningún $y_{ij}>0$, ninguna variable puede salir: la solución es **no acotada** en la
  dirección de mejora (o **no factible** si todavía queda una ficticia positiva).

> Machete verbal: **optimalidad mira la fila y elige quién entra; factibilidad mira esa
> columna y elige quién sale**.

## El procedimiento por tablas

```text
1. ESTANDARIZAR   Ax = b, x >= 0 y b >= 0. Numeracion corrida de variables.
2. BASE INICIAL   buscar columnas de I: holguras + ficticias. Nunca excesos (-1).
3. ARMAR TABLA    Cj arriba; variable basica y su Ci a la izquierda; xi a la derecha.
4. CALCULAR Zj    zj = SUMA_i ci*yij. En la ultima columna: z = SUMA_i ci*xi.
5. REDUCIDOS      calcular Cj-Zj para TODAS las columnas.
6. ¿OPTIMO?       MAX: todos Cj-Zj <= 0  |  MIN: todos Cj-Zj >= 0.
7. ENTRA          MAX: mayor positivo     |  MIN: menor negativo.
8. SALE           theta = xi/yij SOLO si yij > 0. Sale el menor theta >= 0.
                  Si no hay yij > 0: no acotada (salvo ficticia positiva: no factible).
9. PIVOTEAR       fila pivote / pivote; resto: Fi - (coef. de entrada)*fila pivote.
10. REPETIR       recalcular Zj y Cj-Zj. Al terminar: S*, z*/W* y diagnostico.
```

## La tabla se lee así

```text
BASICAS       aparecen en la columna Base; sus columnas forman I; valor = xi.
NO BASICAS    no aparecen en Base; valen 0 en la solucion actual.
Cj            coeficientes FIJOS de todas las variables en el funcional.
Ci            Cj de la variable basica de esa fila. Se COPIA: no es Cj-Zj.
```

Tres controles instantáneos:

```text
columna de cada basica = vector de la identidad
Zj de cada basica = su Cj
Cj-Zj de cada basica = 0
```

> Una básica puede valer 0: eso es **degeneración**. Un $C_j-Z_j=0$ no prueba que una
> variable sea básica: una **no básica** con reducido 0 anuncia óptimos alternativos.

## Forma estándar y base artificial

```text
<=   + holgura (+1)                         entra en la base inicial
>=   - exceso  (-1) + ficticia (+1)         entra la ficticia, NO el exceso
 =                    ficticia (+1)         entra la ficticia
b<0  multiplicar TODA la restriccion por -1 antes de lo anterior
```

Cada variable nueva aparece en **todas** las filas (con 0 donde no interviene) y en el
funcional. Holguras y excesos llevan $c_j=0$.

```text
PENALIZACION     MAX: ficticia con -M     |     MIN: ficticia con +M
                 M > 0 y enorme: al comparar, manda primero el termino en M.

DOS FASES        Fase I: Min f = suma de ficticias (o Max zeta = -f).
                 f* = 0: factible -> borrar ficticias, reponer Cj y hacer Fase II.
                 f* > 0: no factible -> RF vacia.
```

Ficticia básica con valor **positivo** al terminar = problema no factible. Ficticia básica
con valor **0** = factible pero degenerado; se intenta sacarla antes de la Fase II.

## Mapa de decisión final

```text
¿Se cumple optimalidad?
|
|-- NO -> elegir columna entrante
|         |-- algun yij > 0 -> menor xi/yij -> pivotear
|         `-- todos yij <= 0
|                |-- ficticias nulas     -> NO ACOTADA
|                `-- ficticia positiva   -> NO FACTIBLE
|
`-- SI -> ¿ficticia basica positiva?
          |-- SI -> NO FACTIBLE
          `-- NO -> mirar SOLO las no basicas:
                    |-- alguna Cj-Zj = 0 -> OPTIMOS MULTIPLES
                    `-- signo estricto   -> OPTIMO UNICO

Ademas: alguna BASICA con xi = 0 -> DEGENERADA (puede ser unica o multiple).
```

## Los cinco diagnósticos

| Diagnóstico | Señal en la tabla |
|---|---|
| **Única** | óptimo; no básicas con $C_j-Z_j<0$ en Max ($>0$ en Min) |
| **Múltiples** | óptimo; alguna **no básica** con $C_j-Z_j=0$ |
| **Degenerada** | alguna **básica** tiene $x_i=0$; suele venir de empate en salida |
| **No acotada** | hay reducido que mejora, pero toda su columna tiene $y_{ij}\leq0$ |
| **No factible** | ficticia básica positiva; o Fase I termina con $f^*>0$ |

> **No factible**: no existe ningún punto que cumpla las restricciones. **No acotada**:
> sí hay puntos factibles, pero el funcional mejora sin límite. RF no acotada tampoco
> implica por sí sola solución no acotada.

## Desempates y casos especiales

```text
empate en ENTRADA   -> entra el menor subindice
empate en SALIDA    -> sale el mayor subindice; la proxima SBF sera degenerada
theta = 0           -> pivote degenerado: cambia la base pero no el punto ni z
```

Si una ficticia sale, no vuelve. Para resolver solamente se puede borrar su columna; si
después habrá sensibilidad/dualidad, se conserva porque ayuda a leer $B^{-1}$.

## Formato de respuesta de la cátedra

```text
S* = (x1*; x2*; ...; xn*)^T       z* = ...       (o W* = ...)

"Como todos los Cj-Zj <= 0, se cumple la condicion de optimalidad" (Max).
"La solucion es unica porque los reducidos de las no basicas son < 0".
"Es degenerada porque la variable basica xk vale 0".
```

Interpretar en castellano: cuánto se produce, qué holguras/excesos quedan, qué restricciones
son activas ($h/e=0$) o pasivas ($h/e>0$), y qué significa el valor óptimo.

## Las trampas que más cuestan puntos

| Trampa | Antídoto |
|---|---|
| Poner el viejo $C_j-Z_j$ como nuevo $C_i$ | $C_i$ se copia del funcional según la nueva base |
| Dividir por 0 o por negativos en $x_i/y_{ij}$ | solo denominadores **estrictamente positivos** |
| Confundir básica con positiva | la base la marca la identidad; una básica puede valer 0 |
| Declarar múltiples por un cero cualquiera | el cero debe ser de una **no básica** y en óptimo |
| Declarar no factible porque queda una ficticia | solo si queda con valor **positivo** |
| Mezclar mínimo y máximo | Min directo: ficticia $+M$, óptimo $C_j-Z_j\geq0$ |
| No recalcular después del pivote | nueva base -> nuevos $C_i$, $Z_j$, reducidos y $z$ |

## Control final

```text
[ ] columnas basicas = I y sus reducidos = 0
[ ] variables no basicas = 0; basicas leidas de xi
[ ] S* satisface TODAS las ecuaciones y x >= 0
[ ] z*/W* coincide con reemplazar S* en el funcional original
[ ] ficticias nulas; diagnostico justificado con un numero de la tabla
```
