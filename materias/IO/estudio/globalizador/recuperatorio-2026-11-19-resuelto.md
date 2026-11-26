# Recuperatorio de IO del 19/11/2026 — resuelto

> Enunciados originales en `fuentes/parciales/2026-11-19/` (teoría y práctica). Acá están la
> respuesta correcta de cada pregunta, su justificación, lo que marqué en el examen y el
> diagnóstico para el globalizador de febrero.
>
> **Resultado:** práctica 3/12 · teoría 7/20.
>
> **Para practicarlo:** `../recuperatorio/simulacro-teoria.html` tiene el banco «Recuperatorio
> 19/11» (las 20 de teoría tal cual), dos tandas nuevas escritas con este formato y, en la pestaña
> Práctica, los tres ejercicios con corrección.

## Cómo es el formato real

No se parece a los bancos viejos del simulacro. Tres rasgos que hay que entrenar:

1. **El enunciado es una situación**, no una frase a completar. Primero hay que traducirla al
   concepto ("cada cambio de tamaño lleva horas" → tiempo de puesta a punto).
2. **Cada opción es una afirmación más un «porque».** Suelen venir de a pares con la misma
   conclusión y distinta justificación ("No cambia, porque…" × 2, "Aumenta, porque…" × 2). Una
   conclusión correcta con una razón falsa es una opción incorrecta.
3. **Los distractores usan hechos verdaderos fuera de lugar.** En la pregunta 2 de teoría, "se
   actualizan los registros más seguido" es cierto del sistema de punto de pedido, pero no es lo
   que cubre un riesgo de faltante menor.

Método: decidir primero la conclusión (descarta un par entero) y después leer el «porque» de las
dos que quedan buscando cuál es falso.

## Práctica

### Ejercicio 1 — Método gráfico

Restricciones leídas del gráfico:

| | Recta | Pasa por |
|---|---|---|
| R1 | $3X_1 + 2X_2 \le 24$ | (0, 12) y (8, 0) |
| R2 | $X_1 + 3X_2 \le 15$ | (0, 5) y (15, 0) |
| R3 | $2X_1 + X_2 \ge 4$ | (0, 4) y (2, 0) |
| R4 | $X_1 \le 8$ | vertical |

Vértices de la región y valor de $Z = 5X_1 + 4X_2$:

| Vértice | Z |
|---|---|
| (2, 0) | 10 |
| (8, 0) | 40 |
| **(6, 3)** | **42** |
| (0, 5) | 20 |
| (0, 4) | 16 |

| N° | Correcta | Marqué | Justificación |
|---|---|---|---|
| 1 | **c** | c ✓ | El mayor Z está en (6, 3), intersección de R1 y R2: $Z = 42$. |
| 2 | **e** | b ✗ | R3 es de ≥, así que tiene excedente: $2\cdot 6 + 3 - 4 = 11$. No figura entre las opciones. $-11$ es el mismo número con el signo al revés: una variable de excedente nunca es negativa en un punto factible. |
| 3 | **b** | d ✗ | El óptimo no cambia mientras la pendiente de Z quede entre las de R2 y R1: $\tfrac13 \le \tfrac{c_1}{4} \le \tfrac32$, o sea $c_1 \in [4/3,\ 6]$. Con $c_1 < 4/3$ el óptimo se va a (0, 5); el límite inferior no es 0. |

### Ejercicio 2 — Simplex, sensibilidad y dual

Forma estándar: $X_4$ holgura del lúpulo, $X_5$ excedente del contrato, $X_7$ su ficticia,
$X_6$ holgura del envasado.

**Tabla dada** (base $X_2, X_1, X_6$): $X_1 = 70$, $X_2 = 55$, $Z = 4300$. Fila $c_j - z_j$:

| | $X_1$ | $X_2$ | $X_3$ | $X_4$ | $X_5$ | $X_6$ | $X_7$ |
|---|---|---|---|---|---|---|---|
| $z_j$ | 30 | 40 | 80 | 20 | $-10$ | 0 | 10 |
| $c_j - z_j$ | 0 | 0 | $-65$ | $-20$ | $+10$ | 0 | $-M-10$ |

Entra $X_5$ (único positivo). Cocientes: $55/(1/2) = 110$ y $70/1 = 70$ → sale $X_6$.

**Tabla óptima** (base $X_2, X_1, X_5$):

| $C_B$ | Base | $X_1$ | $X_2$ | $X_3$ | $X_4$ | $X_5$ | $X_6$ | $X_i$ |
|---|---|---|---|---|---|---|---|---|
| 40 | $X_2$ | 0 | 1 | 3/2 | 1/2 | 0 | $-1/2$ | 20 |
| 30 | $X_1$ | 1 | 0 | 1 | 0 | 0 | 1 | 140 |
| 0 | $X_5$ | 0 | 0 | 1 | 0 | 1 | 1 | 70 |
| | $c_j - z_j$ | 0 | 0 | $-75$ | $-20$ | 0 | $-10$ | $Z = 5000$ |

Precios sombra: $y_1 = 20$ (lúpulo), $y_2 = 0$ (contrato), $y_3 = 10$ (envasado).

| N° | Correcta | Marqué | Justificación |
|---|---|---|---|
| 4 | **c** | d ✗ | La ficticia $X_7$ no está en la base, así que es factible para el problema original. No es óptima porque $c_5 - z_5 = +10$. No es degenerada: ninguna básica vale cero (55, 70, 70). |
| 5 | **d** | d ✓ | Entra $X_5$, sale $X_6$: la Rubia supera el mínimo ($X_5 = 70$) y se agota el envasado ($X_6 = 0$). |
| 6 | **b** | b ✓ | $X_2$ es básica. Con $c_2$ genérico, los $c_j - z_j$ quedan $X_3: -15 - \tfrac32 c_2$, $X_4: -\tfrac12 c_2$, $X_6: \tfrac12 c_2 - 30$. Todos ≤ 0 si $0 \le c_2 \le 60$. Con 25 se mantiene la solución y $Z = 30\cdot140 + 25\cdot20 = 4700$. |
| 7 | **d** | b ✗ | Trigo usa 3 kg de lúpulo y 1 hl de envasado: $z_j = 3\cdot20 + 1\cdot10 = 70$. $c_j - z_j = 80 - 70 = +10 > 0$: conviene. El $-10$ sale de calcular $z_j - c_j$. |
| 8 | **d** | e ✗ | $X_1 = 140 > 70$: el contrato no está activo, su excedente $X_5$ es básico y por holguras complementarias $y_2 = 0$. Las otras dos restricciones están activas con dual positivo. |

### Ejercicio 3 — Stock con descuento por cantidad excedente

Datos: $D = 10000$ u/año, $i = 0{,}25$, $C_1 = 12$ hasta $a = 1000$, $C_2 = 10$ el excedente,
costo de pedido $L = 0$ ("portal electrónico y sin cargo de envío").

Es descuento **sobre el excedente**, no sobre todo el lote. El precio medio es
$C(Q) = C_2 + \dfrac{(C_1 - C_2)\,a}{Q} = 10 + \dfrac{2000}{Q}$: las primeras 1000 unidades
funcionan como un costo fijo de \$2000 por pedido.

$$CT(Q) = \begin{cases} 120000 + 1{,}5\,Q & Q \le 1000 \\[4pt] 100000 + \dfrac{2\cdot10^{7}}{Q} + 1{,}25\,Q + 250 & Q > 1000 \end{cases}$$

En $Q = 1000$ las dos ramas valen 121500: la curva es **continua**.

$$Q^* = \sqrt{\frac{2\cdot10^{7}}{1{,}25}} = 4000 \qquad CT(4000) = 100000 + 5000 + 5000 + 250 = 110250$$

| N° | Correcta | Marqué | Justificación |
|---|---|---|---|
| 9 | **a** | d ✗ | Recta creciente hasta 1000 (sin costo de pedido, sólo crece el de mantener) y después, sin salto, una curva con mínimo. El gráfico d) tiene un salto en 1000: ése es el de descuento sobre todo el lote. |
| 10 | **a** | b ✗ | $Q^* = 4000$. 3651 sale de usar $C_1 = 12$ en el costo de mantener; 2828 de equivocar el 2. |
| 11 | **a** | e ✗ | $CT(1000) - CT(4000) = 121500 - 110250 = 11250$. |
| 12 | **b** | d ✗ | $10000/4000 = 2{,}5$ pedidos por año → $365/2{,}5 = 146$ días. |

## Teoría

| N° | Tema | Correcta | Marqué | Justificación |
|---|---|---|---|---|
| 1 | Stock | **d** | c ✗ | Detener, cambiar piezas, ajustar y probar en cada cambio de producto es tiempo de puesta a punto. No es una parada no programada (está prevista) ni una falla de calidad. |
| 2 | Stock | **b** | a ✗ | En punto de pedido con riesgo de faltante, el lote se calcula como en el determinístico. El menor riesgo sube $z$, el stock de seguridad y el punto de pedido. |
| 3 | Stock | **c** | c ✓ | $V$ es la velocidad de ingreso mientras dura el ingreso. Lo que crecen las existencias es $V - D$. |
| 4 | Dualidad | **b** | c ✗ | $c_j$ es el término independiente de la restricción $j$ del dual. La función económica del dual usa los $b_i$, que no cambiaron. |
| 5 | Sensibilidad | **a** | d ✗ | Dentro del intervalo la base sigue factible, y como los $c_j - z_j$ no dependen de $b$, sigue óptima. Sí cambian los valores de las básicas y Z. |
| 6 | Asignación | **d** | d ✓ | Con ofertas y demandas iguales a 1, toda solución básica es entera: $x_{ij}$ vale 1 o 0 sin exigirlo. |
| 7 | Entera | **a** | a ✓ | El conjunto de soluciones del entero es discreto y no convexo: en sentido estricto sólo el relajado es lineal. |
| 8 | Redes | **a** | d ✗ | Conectar todos los nodos con la menor longitud total es árbol de expansión mínima. La d) es flujo de costo mínimo, la b) ruta más corta y la c) flujo máximo. |
| 9 | Simplex | **c** | a ✗ | M penaliza las **ficticias**, no los excesos. La ficticia que sale no vuelve a entrar ($c_j - z_j$ siempre negativo) y su columna se puede quitar. |
| 10 | Stock | **d** | c ✗ | Aleatorio: leyes de probabilidad conocidas, inferidas del estudio estadístico. Incierto: no se pueden predecir con la experiencia pasada. |
| 11 | Redes | **a** | b ✗ | El arco ficticio permite escribir conservación de flujo (entra = sale) también en O y en F, como en los nodos intermedios. |
| 12 | Transporte | **b** ⚠ | d ✗ | Es de transporte todo problema que se ajusta al modelo, sea de costos o de ganancias. Respuesta apoyada en Hillier, no cotejada con el apunte de la cátedra. |
| 13 | Stock | **c** | c ✓ | Plazo de provisión constante y conocido. La b) lo confunde con el ingreso instantáneo del lote. |
| 14 | Stock | **a** | a ✓ | Con descuento por excedente CT es continua en $a$ y la pendiente de $CT_2$ en $a$ es menor que la de $CT_1$: el quiebre nunca es un mínimo. |
| 15 | Entera | **d** | b ✗ | Búsqueda: revisar explícitamente una parte de los puntos enteros y el resto implícitamente. La b) describe los métodos de corte. |
| 16 | Dualidad | **b** | c ✗ | El dual siempre se puede plantear. Si el primal es no acotado, el dual no tiene soluciones factibles. |
| 17 | Formas | **c** | a ✗ | La estándar exige $b_i \ge 0$: se multiplica por $-1$ (queda ≤) y se suma una holgura. La canónica de mínimo ya pide ≥: se deja. |
| 18 | Stock | **d** ⚠ | b ✗ | El modelo reserva a cada artículo el espacio de su existencia máxima, lo que equivale a suponer que el lugar que libera no lo usa otro. La wiki sólo registra "ocupa su existencia máxima". |
| 19 | Simplex | **b** | b ✓ | La fila del vector que sale se divide por el pivote; si vale 1, queda igual. |
| 20 | Conceptos básicos | **c** | c ✓ | Una combinación con alguna incógnita negativa es una solución básica no factible, no un punto extremo. |

⚠ = respuesta que depende de la formulación exacta de la cátedra y no está cotejada con el apunte.
Si en las dos la correcta fuera la que marqué, la teoría quedaría en 9/20.

## Diagnóstico

**Práctica.** De 9 errores, 6 son recuperables con poco:

- Tres son de signo o de un límite (2, 3, 7): el excedente no es negativo, el rango de $c_1$ tiene
  dos pendientes y el costo reducido es $c_j - z_j$, no al revés.
- Tres son arrastre de un solo error de modelo (10, 11, 12): tratar el descuento por excedente
  como descuento sobre todo el lote.
- Los otros tres son de lectura de tabla (4, 8) y de reconocer la curva (9).

**Teoría.** Los errores se agrupan en cuatro bloques:

| Bloque | Preguntas | Qué falló |
|---|---|---|
| Dualidad y sensibilidad | 4, 5, 16 | Qué dato del primal va a qué lugar del dual; qué garantiza un rango de $b_i$; primal no acotado → dual sin factibles. |
| Mecánica del simplex | 9, 17 | Exceso vs. ficticia en la M grande; la estándar exige $b_i \ge 0$. |
| Redes y entera | 8, 11, 15 | Reconocer cada problema de redes por su objetivo; para qué sirve el arco ficticio; búsqueda vs. cortes. |
| Stock conceptual | 1, 2, 10 (y 18) | Causas generadoras, qué mueve el riesgo de faltante, aleatorio vs. incierto. |

**Temas que no estaban en los bancos viejos:** el arco ficticio del flujo máximo (11), aleatorio
vs. incierto (10) y la linealidad "en sentido estricto" del programa entero (7).
