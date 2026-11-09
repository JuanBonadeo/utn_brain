# IO 2026 — Transcripción de pizarras y diapositivas de cátedra (classroom-2026)

Fuente: `materias/IO/fuentes/classroom-2026/` (curso 402, UTN FRRo). Material escaneado (pizarra digital manuscrita + diapositivas). Transcripción fiel; `[ilegible]` = no se lee; `[cortado]` = el escaneo corta la diapositiva; `[nota del transcriptor: …]` = aclaración mía, no está en el original.

Ejemplo que atraviesa casi todo el material (el "problema de alfarería" del Cap. 2):

$$\max z = 20x_1 + 45x_2 \quad \text{s.a}\quad x_1 + 2x_2 \le 40;\; 3x_1 + 1{,}5x_2 \le 75;\; x_2 \le 15;\; x_1,x_2 \ge 0$$

($x_3$: holgura mano de obra; $x_4$: holgura materia prima; $x_5$: holgura demanda). Óptimo: $x^* = (10, 15, 0, 22{,}5, 0)$, $z^* = 875$.

---

## 1. `teoria/Cap2_Conceptos_Basicos.pdf` (21 diapositivas, con texto)

"Capítulo 2 — Conceptos Básicos. Convexidad · Teoremas fundamentales · Solución conceptual. Material oficial de cátedra · UTN-FRRo." Mapa: 2.1 Convexidad · 2.2 Teoremas básicos · 2.3 Solución conceptual.

### (a) Contenido

**2.1 Convexidad**

- **Def 2.1 Recta**: dados $x^1, x^2 \in \mathbb{R}^n$, $R = \{x \in \mathbb{R}^n / x = \lambda x^1 + (1-\lambda)x^2;\ \lambda \in \mathbb{R}\}$.
- **Def 2.2 Segmento** $[x^1,x^2] = \{x / x = \lambda x^1 + (1-\lambda)x^2;\ \lambda \in [0,1]\}$. Cerrado si incluye extremos; abierto $]x^1,x^2[$ si no. "λ ∈ [0,1] recorre todo el segmento; λ ∈ ℝ recorre toda la recta."
- **Def 2.3 Hiperplano** $H = \{x \in \mathbb{R}^n / c^Tx = z;\ z \in \mathbb{R},\ c^T \ne 0\}$, i.e. $c_1x_1 + \dots + c_jx_j = z$. "El vector c es normal al hiperplano." Ejemplo en ℝ²: $x_1 + x_2 = 4$, $c=(1,1)$; $(1,1)$: 1+1=2<4 (inferior); $(3{,}5;3{,}5)$: 7>4 (superior).
- **Def 2.4 Semiespacios**: el hiperplano divide ℝⁿ en $\{c^Tx<z\}$ semiespacio inferior (abierto), $\{c^Tx=z\}$ el hiperplano (cerrado), $\{c^Tx>z\}$ semiespacio superior (abierto). Unión con el hiperplano ⇒ semiespacio cerrado (≤ z ó ≥ z).
- **Def 2.5 Polítopo**: todo conjunto de ℝⁿ expresable como intersección de un número finito de semiespacios cerrados. ℝ²: polígono; ℝ³: poliedro; ℝⁿ: polítopo (caso general). **"Cuando el polítopo está acotado se llama poliedro."** ("Polítopo acotado ⇒ poliedro").
- **Def 2.6 Combinación lineal convexa**: $x = \sum_i \lambda_i x^i$, $\lambda_i \in \mathbb{R}$ (lineal); convexa si además $\lambda_i \ge 0\ \forall i$ y $\sum_i \lambda_i = 1$. El segmento $[x^1,x^2]$ es exactamente el conjunto de combinaciones lineales convexas de $x^1$ y $x^2$.
- **Def 2.7 Conjunto convexo**: $K \subset \mathbb{R}^n$ es convexo si $\forall x^1,x^2 \in K$ ($x^1\ne x^2$) el segmento $[x^1,x^2]$ está totalmente contenido en K. Equivalente: toda c.l.c. de dos puntos del conjunto pertenece al conjunto.
- **Def 2.8 Punto extremo (vértice)**: $x\in K$ es extremo si NO puede escribirse como $x = \lambda x^1 + (1-\lambda)x^2$ con $x^1,x^2\in K$, $x^1\ne x^2$, $0\le\lambda\le 1$. Puede haber finitos o infinitos puntos extremos. "IDEA CLAVE: Todo punto interior puede expresarse como combinación convexa de dos puntos del poliedro (p. ej. de dos vértices). Los vértices, en cambio, son «irreducibles»." (Ej.: $P_{int} = \tfrac12 P_1 + \tfrac12 P_4$.)
- **Propiedades**: la intersección (finita o infinita) de convexos es convexa (la unión, en general, no); la suma de convexos es convexa; la combinación lineal de convexos es convexa. "CONSECUENCIA CLAVE: Todo polítopo es un conjunto convexo por ser la intersección de un número finito de semiespacios cerrados. Semiespacios ⇒ Polítopo ⇒ Convexo." El vacío es convexo; un unitario {p} es convexo; un convexo puede ser abierto o cerrado, acotado o no.

**2.2 Teoremas básicos**

- **Forma estándar**: $\max z = cx$, s.a. $Ax=b$, $x\ge0$. A: $m\times n$ con $m<n$; x: n componentes (incluye holguras); b: m componentes.
- **Partición base/no base**: $Ax=b \;\Rightarrow\; Bx_B + Nx_N = b$. B: base de m vectores columna de A (cuadrada invertible); $x_B$ variables básicas; N: las $n-m$ columnas restantes; $x_N$ no básicas (se anulan). $x_B = B^{-1}b$.
- **Hipótesis de rango completo**: $\text{rango}(A) = \text{rango}(A|b) = m$ ⇔ las m ecuaciones son l.i.
- **Jerarquía de soluciones**: Solución (n-upla que satisface Ax=b) ⊃ Solución factible (además x ≥ 0) ⊃ Solución básica (a lo sumo m componentes no nulas ⇒ al menos n−m nulas) ⊃ SBF (básica con todas las básicas no negativas) ⊃ SBF no degenerada (exactamente m componentes > 0) / degenerada (más de n−m nulas).
- **Teorema 2.1**: el conjunto de soluciones factibles de un PL es convexo cerrado. Idea: cada igualdad = intersección de ≤ y ≥; cada $x_j\ge0$ es semiespacio cerrado; región factible = intersección finita = polítopo ⇒ convexo cerrado. Tres casos: vacío (PL no factible), punto único (solución trivial), infinitos puntos (caso interesante).
- **Teorema 2.2 (Teorema fundamental de la PL)**, bajo rango completo: (i) si hay solución factible, hay SBF (si los p vectores activos son l.i. se completa a base; si son dependientes se reduce el número de positivas eligiendo ε y se itera); (ii) si hay solución factible óptima, hay SBF óptima (tomando $x+\theta y$ factible para $\theta\in[-\varepsilon,\varepsilon]$, si $c\cdot y\ne0$ la función mejora ⇒ contradicción; luego $c\cdot y=0$). Consecuencia: "Basta con buscar el óptimo entre las soluciones básicas factibles — no en todos los puntos factibles."
- **Teorema 2.3 (Equivalencia)**: con rango completo, x es punto extremo de K ⇔ es SBF. Álgebra: $x_1A_1 + \dots + x_jA_j = b$ con $A_1..A_j$ l.i., $x_j\ge0$, resto nulas ("puede ser degenerada si k < m").
- **Teorema 2.4**: la F.O. alcanza su óptimo en al menos un punto extremo; si lo alcanza en más de uno, también en toda combinación convexa de ellos. Esquema: $x=\sum\lambda_i x^i$ ⇒ $z = \sum\lambda_i (c\cdot x^i) = \sum \lambda_i z_i \le z_0 = \max\{z_i\}$.
- **Conclusiones**: (1) región factible convexa cerrada; (2) punto extremo = SBF; (3) si hay máximo/mínimo finito, existe un punto extremo donde se alcanza; (4) N° máximo de puntos extremos $= \binom{n}{m}$. "La solución óptima del programa lineal debe buscarse entre los puntos extremos del conjunto convexo de soluciones factibles."

**2.3 Solución conceptual**

Procedimiento: Paso 1 forma estándar (con holguras/excesos); Paso 2 elegir una base B (m columnas l.i.); Paso 3 resolver Cramer: anular las n−m no básicas y resolver $Bx_B=b$; Paso 4 verificar factibilidad: si todas las $x_B \ge 0$ ⇒ punto extremo; si no, descartar. Repetir para las $\binom{n}{m}$ combinaciones, calcular z en cada vértice factible y quedarse con el mejor.

**Ejemplo 2.1 — alfarería** (forma estándar: $x_1+2x_2+x_3=40$; $3x_1+1{,}5x_2+x_4=75$; $x_2+x_5=15$). Enumeración de las $\binom{5}{3}=10$ bases:

| Base | x₁ | x₂ | x₃ | x₄ | x₅ | Observación | z |
|---|---|---|---|---|---|---|---|
| A₁A₂A₃ | 17,5 | 15 | −7,5 | 0 | 0 | No factible | — |
| A₁A₂A₄ | 10 | 15 | 0 | 22,5 | 0 | Factible ÓPTIMA | 875 |
| A₁A₂A₅ | 20 | 10 | 0 | 0 | 5 | Factible | 850 |
| A₁A₃A₄ | — | — | — | — | — | No forman base | — |
| A₁A₃A₅ | 25 | 0 | 15 | 0 | 15 | Factible | 500 |
| A₁A₄A₅ | 40 | 0 | 0 | −45 | 15 | No factible | — |
| A₂A₃A₄ | 0 | 15 | 10 | 52,5 | 0 | Factible | 675 |
| A₂A₃A₅ | 0 | 50 | −60 | 0 | −35 | No factible | — |
| A₂A₄A₅ | 0 | 20 | 0 | 45 | −5 | No factible | — |
| A₃A₄A₅ | 0 | 0 | 40 | 75 | 15 | Factible (trivial) | 0 |

Vértices ↔ bases: Q0=(0,0) A₃A₄A₅ z=0; Q1=(25,0) A₁A₃A₅ z=500; Q2=(20,10) A₁A₂A₅ z=850; Q3=(10,15) A₁A₂A₄ z=875 ★; Q4=(0,15) A₂A₃A₄ z=675.

**2.3.1 Necesidad de un método alternativo**: con 20 variables y 10 restricciones, $\binom{20}{10} = 184.756$ puntos extremos potenciales. Crece factorialmente; muchos vértices no factibles; no hay guía para priorizar bases. Solución: Método Simplex (George B. Dantzig, 1947), "se mueve inteligentemente de vértice en vértice mejorando z". Cierre en tres ideas: región factible = polítopo convexo cerrado; vértice ⇔ SBF; óptimo en al menos un vértice → Capítulo 3: el Método Simplex.

### (b) Lo que la cátedra enfatiza

- Forma estándar de cátedra = **Max** z = cx, Ax = b, x ≥ 0, con $m<n$ y rango completo.
- Terminología propia: "polítopo" (general) vs "poliedro" = **polítopo acotado** (ojo: varios libros usan la convención inversa).
- Degenerada definida como "más de n−m nulas" (equivalente: alguna básica = 0).
- "Vértice ⇔ SBF" y "óptimo en un vértice" son las tres ideas de cierre; cota $\binom{n}{m}$ de puntos extremos.
- La tabla de 10 bases del ejemplo de alfarería (con "No forman base" para A₁A₃A₄) es material típico de pregunta.
- La enumeración se hace "por Cramer": anular no básicas y resolver $Bx_B=b$.

---

## 2. `pizarras/2026 402 factibilidad 0_260506_080552.pdf` (4 pág.) — y su gemela `..._260527_075917.pdf` (5 pág.)

Pizarra manuscrita: derivación de la condición de factibilidad (θ) y de la condición de optimización ($c_j - z_j$). Título: "FACTIBILIDAD — CAP 3."

### (a) Transcripción

**Pág. 1**

- ESTÁNDAR: $\text{MAX } z = cx$ (anotado: z esc[alar], c vec, x vec); s.a $Ax = b$ (A matriz, b vec); $x \ge 0$.
- Esquema tipo tabla: arriba $x_1, x_2, \dots, x_n$; abajo $c_1\, c_2 \dots c_n \,|\, z$.
- Esquema $Ax=b$: arriba $x_1 \dots x_n$; abajo filas $A_{11}\,A_{12}\dots A_{1n} \,|\, b_1$; $A_{21} \,|\, b_2$; …; $A_{m1}\dots A_{mn}\,|\,b_m$.
- "n variables, m restricciones, $n > m$ ⇒" A es un rectángulo ancho.
- "LIBRO CAP. 3: $A_i$ columnas de B; $A_j$ columnas de N."
- $x_N = 0$; $x_B > 0$.
- $A_{m\times n} = [\,N_{m\times(n-m)} \,|\, B_{m\times m}\,]$ (N dibujada a la izquierda en verde, B a la derecha en rojo; llave de m filas y n columnas).
- Debajo de una línea: $Ax=b$ con $x_1, x_2$ marcadas como $x_N$ y el resto hasta $x_n$ como $x_B$; matriz $[A_{11}\,A_{12}\, \dots]$ partida en N | B, …, $A_{m1}\dots A_{mn}$ | $b_1 \dots b_m$.

**Pág. 2**

- $Ax = b \Rightarrow Bx_B + Nx_N = b$, con $x_N = 0$ ⇒ **(2) $Bx_B = b$** (resaltado).
- $N = BY$. Tabla: arriba la matriz Y ($Y_{11}\dots Y_{1j}\dots Y_{1(n-m)}$; …; $Y_{m1}\dots Y_{mj}\dots Y_{m(n-m)}$), a la izquierda B ($B_{11}\dots B_{1m}$; …; $B_{m1}\dots B_{mm}$), abajo-derecha N ($N_{11}\dots N_{1j}\dots N_{1(n-m)}$; …; $N_{m1}\dots N_{mj}\dots N_{m(n-m)}$). Columna j resaltada: $Y_j$ ↔ $N_j$.
- **(1) $N_j = BY_j$** (resaltado) ⇒ $B^{-1}N_j = \underbrace{B^{-1}B}_{I}Y_j$ ⇒ $B^{-1}N_j = Y_j$.
- Sistema: (1) $BY_j = N_j$; (2) $Bx_B = b$. Operación: **(2) − (1)·$\theta_j$** ($\theta_j$ = ESCALAR):
  $$Bx_B - BY_j\theta_j = b - N_j\theta_j$$
  $$B\,(x_B - Y_j\theta_j) + N_j\theta_j = b$$
  (anotado debajo: B matriz; $x_B$ vec; $Y_j$ vec; $\theta_j$ esc; $N_j$ vec; $\theta_j$ esc; b vec).
- "θ es escalar; θ > 0." "$\theta_j$ está asociado a la columna j."
- Tabla: vector $(x_1 - Y_{1j}\theta_j,\ x_2 - Y_{2j}\theta_j,\ \dots,\ x_m - Y_{mj}\theta_j)$ sobre la matriz B ($B_{11}\dots B_{1m}$; …; $B_{m1}\dots B_{mm}$).

**Pág. 3**

$$B(x_B - Y_j\theta_j) + N_j\theta_j = b$$
$$B_1(x_1 - Y_{1j}\theta_j) + B_2(x_2 - Y_{2j}\theta_j) + \dots + B_r(x_r - Y_{rj}\theta_j) + \dots + B_m(x_m - Y_{mj}\theta_j) + N_j\theta_j = b$$
($B_1$ ← "columna $B_1$").

$$\boxed{\theta_j = \min\left\{\frac{x_i}{Y_{ij}},\; Y_{ij} > 0;\; i = 1\dots m\right\}} \quad \text{CONDICIÓN DE FACTIBILIDAD}$$

"Supongamos $\theta_j = \dfrac{x_r}{Y_{rj}}$" ⇒
$$B_1\left(x_1 - Y_{1j}\tfrac{x_r}{Y_{rj}}\right) + B_2\left(x_2 - Y_{2j}\tfrac{x_r}{Y_{rj}}\right) + \dots + \underbrace{B_r\left(x_r - Y_{rj}\tfrac{x_r}{Y_{rj}}\right)}_{=0} + \dots + B_m\left(x_m - Y_{mj}\tfrac{x_r}{Y_{rj}}\right) + N_j\frac{x_r}{Y_{rj}} = b$$
(anotado sobre el término r: "$= x_r - Y_{rj}\theta_j$").

Problema Original: Max z = cx; s.a Ax = b; b ≥ 0; x ≥ 0.

- $z = cx$; $z = c_Nx_N + c_Bx_B$ con $x_N = 0$ ⇒ $z = c_Bx_B$.
- Tabla: $x_1, x_2$ → $x_N$ (n−m); resto hasta $x_n$ → $x_B$ (m componentes); fila de costos $c_1\, c_2 \dots c_n$ partida en $c_N$ | $c_B$; z.
- $z = c_Bx_B$; $z = \sum_i c_ix_i$.
- $\theta_j \to\; z' = \sum_i c_i(x_i - Y_{ij}\theta_j) + c_j\theta_j$ (flechas: "ver condición de factibilidad" → $\sum_i B_i(x_i - Y_{ij}\theta_j) + N_j\theta_j = b$; sobre $c_j$: "DE LA NO BASE")
  $$= \sum_i\left[c_ix_i - c_iY_{ij}\theta_j\right] + c_j\theta_j = \sum_i c_ix_i - \theta_j\sum_i c_iY_{ij} + c_j\theta_j$$

**Pág. 4**

$$= \sum_i c_ix_i + \theta_j\Big(c_j - \underbrace{\textstyle\sum_i c_iY_{ij}}_{z_j}\Big) = \sum_i c_ix_i + \theta_j(c_j - z_j)$$

- $c_j - z_j > 0$ → "nuevo z es mejor" ⇒ "sigo iterando".
- $c_j - z_j \le 0$ → "nuevo z no es mejor" ⇒ "NO PUEDO SEGUIR MEJORANDO" ⇒ "ESTAMOS EN EL ÓPTIMO".

**Diferencias de la versión 2026-05-27 (5 pág.)**: contenido idéntico página a página; sólo agrega en pág. 3 una flecha de "$\theta_j = x_r/Y_{rj}$" hacia el $\theta_j$ que multiplica a $N_j$ (marcando que $x_j' = \theta_j = x_r/Y_{rj}$). La pág. 5 está en blanco.

### (b) Lo que la cátedra enfatiza

- Notación propia: **$Y = B^{-1}N$**, columna $Y_j = B^{-1}N_j$ (de $N = BY$); elementos $Y_{ij}$ (i fila básica, j columna no básica). Índice **i = base, j = no base** ("Libro cap. 3: $A_i$ columnas de B, $A_j$ columnas de N").
- **θ_j** es un escalar > 0 "asociado a la columna j"; se obtiene de "(2) − (1)·θ_j" sobre $Bx_B=b$ y $BY_j=N_j$.
- **Condición de factibilidad** escrita literalmente: $\theta_j = \min\{x_i/Y_{ij},\ Y_{ij}>0;\ i=1..m\}$; la fila r que alcanza el mínimo es la que se anula (sale).
- **$z_j = \sum_i c_iY_{ij}$** y $z' = z + \theta_j(c_j - z_j)$. **Criterio en Max: $c_j - z_j > 0$ ⇒ sigo iterando; todos $c_j - z_j \le 0$ ⇒ óptimo.** (Usa $c_j - z_j$, no $z_j - c_j$.)
- Dibuja A como $[N\,|\,B]$ (no básicas primero) y escribe $x_B > 0$ (estricto) en vez de ≥ 0; el problema original lleva explícito $b \ge 0$.
- [nota del transcriptor: en la expansión con $B_1..B_m$ numera las básicas $x_1..x_m$, aunque en el esquema anterior $x_1, x_2$ eran las no básicas; es sólo indexado genérico.]

---

## 3. `pizarras/Pasos del simplex 402_260527_082014.pdf` (9 pág.) — y `..._250612_094602.pdf` (8 pág., versión 2025)

Diapositivas "Pasos del algoritmo simplex" (texto impreso) + resolución manuscrita del ejemplo de alfarería. Transcribo la versión 2026 (más completa en anotaciones) y abajo las diferencias.

### (a) Transcripción (versión 2026-05-27)

**Pág. 1**: portada "Pasos del algoritmo simplex".

**Paso 1. Expresar el problema en forma estándar** — impreso: "Max z = cx; s.a Ax = b. Encontrar B, N, $c_B$, $c_N$, $x_B$, $x_N$, z" (tachados a medida que se encuentran). Manuscrito (en la esquina, el original: Max z = 20x₁ + 45x₂; s.a x₁ + 2x₂ ≤ 40; 3x₁ + 1,5x₂ ≤ 75; x₂ ≤ 15):

$$\text{MAX } z = \underbrace{20x_1 + 45x_2}_{c_N} + \underbrace{0x_3 + 0x_4 + 0x_5}_{c_B}$$
$$\text{s.a}\begin{cases} 1x_1 + 2x_2 + 1x_3 + 0x_4 + 0x_5 = 40\\ 3x_1 + 1{,}5x_2 + 0x_3 + 1x_4 + 0x_5 = 75\\ 0x_1 + 1x_2 + 0x_3 + 0x_4 + 1x_5 = 15\end{cases}\qquad b = \begin{bmatrix}b_1\\b_2\\b_3\end{bmatrix}$$

Columnas de $x_1, x_2$ → N ($j = 1$, $j = 2$); columnas de $x_3, x_4, x_5$ → B ($i = 3$, $i = 4$, $i = 5$).

$$B = \begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix},\quad N = \begin{bmatrix}1&2\\3&1{,}5\\0&1\end{bmatrix},\quad c_B = [0\ 0\ 0],\quad c_N = [20\ \ 45],\quad x_N = [0\ \ 0]$$
$$Bx_B = b \;\Rightarrow\; x_B = B^{-1}b = \begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}\begin{bmatrix}40\\75\\15\end{bmatrix} = \begin{bmatrix}40\\75\\15\end{bmatrix} = x_B,\qquad z = c_Bx_B = 0$$

**Paso 2. Calcular la matriz completa Y** — impreso: "$Y = B^{-1}N$". Manuscrito: "(N = BY) → de la cond. de factibilidad". Tabla: arriba N (columnas 1 y 2: (1, 3, 0) y (2; 1,5; 1)); a la izquierda $B^{-1}$ con filas rotuladas 3, 4, 5 (identidad); resultado Y:

| fila (básica) | $Y_1$ (j=1) | $Y_2$ (j=2) |
|---|---|---|
| 3 | $y_{31} = 1$ | $y_{32} = 2$ |
| 4 | $y_{41} = 3$ | $y_{42} = 1{,}5$ |
| 5 | $y_{51} = 0$ | $y_{52} = 1$ |

("subíndices" → columnas $Y_1$, $Y_2$.)

**Paso 3. Calcular $z_j$** — impreso: $z_j = \sum_i c_iy_{ij}\ \forall j \in N$; "$z_j = c_BY$ (i: base, j: no base)". Manuscrito: "ver cond. de optimización".
$$c_BY = [0\ 0\ 0]\begin{bmatrix}1&2\\3&1{,}5\\0&1\end{bmatrix} = [0\ \ 0] = [z_1\ \ z_2]$$

**Paso 4. Evaluar $(c_j - z_j)$. Aplicar condición de Optimización** — impreso:
"Para todos los j de la No base. Aplicar Condición de optimización:
- Todas $(c_j - z_j) \le 0$ ⇒ Óptimo [STOP]
- Alguna $(c_j - z_j) > 0$ ⇒ Elegir el mejor valor para j; Columna $N_j$ "entra" a la Base; [Sigo iterando]"

(los signos ≤ y > están corregidos a mano sobre el impreso). Manuscrito: $z' = z + \theta(c_j - z_j)$ con "(+)" sobre θ.
$c_j$ → NO BASE → [20 45]; $z_j$ → [0 0];
$c_1 - z_1 = 20 - 0 = 20$; $c_2 - z_2 = 45 - 0 = 45$ (resaltado) → "MEJOR VALOR → j = 2 ($N_2$)", "columna j = 2 de la NO BASE", $N_2 = (2;\ 1{,}5;\ 1)$ "ENTRA" A LA BASE.

**Paso 5. Calcular $\theta_j$ (condición de Factibilidad)** — impreso:
$$\theta_j = \min_i\left\{\frac{x_i}{y_{ij}};\ y_{ij} > 0;\ i \in B\right\}$$
"Supongamos que $x_r$ cumple la condición: $\theta_j = x_r/y_{rj}$ ⇒ la columna $B_r$ "sale" de la Base."
Manuscrito: $j = 2 \to \theta_2$:
$$\frac{x_i}{Y_{i2}}:\quad \frac{x_3}{Y_{32}} = \frac{40}{2} = 20;\quad \frac{x_4}{Y_{42}} = \frac{75}{1{,}5} = 50;\quad \frac{x_5}{Y_{52}} = \frac{15}{1} = 15\ \text{(resaltado)}$$
$i = 5 \to B_5$ "SALE" DE LA BASE, $B_5 = (0, 0, 1)$.

**Paso 6. Nueva solución → x′** — impreso:
"- El vector x tiene componentes $x_i$
- Uno de los $x_i$ es tal que $x_i = x_r$ (define a $\theta_j$)
- Uno de los $x_j$ de la No base dejó de ser 0 (el j de la condición de Optimización)
Entonces:"
$$x_i' = x_i - \theta_jy_{ij} = x_i - \frac{x_r}{y_{rj}}y_{ij}\quad \forall x_i \ne x_r$$
$$x_r' = x_r - \frac{x_r}{y_{rj}}y_{rj} = 0 \qquad (x_i = x_r)$$
$$x_j' = \theta_j = \frac{x_r}{y_{rj}}$$

**Pág. 8 (manuscrita)**:

| | X actual | | X nuevo |
|---|---|---|---|
| N | $x_1 = 0$ | N | $x_1' = 0$ |
| N | $x_2 = 0$ | B (ENTRÓ) | $x_2' = \theta_2 = x_5/Y_{52} = 15/1 = 15$ |
| B | $x_3 = 40$ | B | $x_3' = x_3 - Y_{32}\cdot\theta_2 = 40 - 2\cdot15 = 10$ |
| B | $x_4 = 75$ | B | $x_4' = x_4 - Y_{42}\cdot\theta_2 = 75 - 1{,}5\cdot15 = 52{,}5$ |
| B | $x_5 = 15$ | N (SALIÓ) | $x_5' = x_5 - Y_{52}\cdot\theta_2 = 15 - 1\cdot15 = 0$ |

$x' = [0\ \ 15\ \ 10\ \ 52{,}5\ \ 0]$ (N B B B N). "LO ORDENAMOS COMO $[x_3\ x_4\ x_2]$ — VA EN EL LUGAR DE LA QUE SALIÓ."
$x_B' = [10\ \ 52{,}5\ \ 15]$; $c_B' = [c_3\ c_4\ c_2] = [0\ \ 0\ \ 45]$;
$$z' = c_B'x_B' = [0\ 0\ 45]\cdot[10;\ 52{,}5;\ 15] = 0\cdot10 + 0\cdot52{,}5 + 45\cdot15 = 675$$
Pág. 9: en blanco.

**Diferencias de la versión 2025-06-12 (8 pág.)**: mismas diapositivas impresas; anotaciones algo distintas: escribe además $C = [20\ 45\ 0\ 0\ 0]$, "N: NO BASE j = 1, 2" y "B: BASE i = 3, 4, 5", y $z = cx = c_Bx_B + c_N\underbrace{x_N}_{=0} \Rightarrow z = c_Bx_B = 0$; calcula Y explícitamente como producto $B^{-1}N = I\cdot N$; en el paso 3 anota "(todos)" y "$Y_i$ → filas 3,4,5 / columnas 1,2; $z_j$; j = 1,2"; en el paso 4 escribe "$c_j \in N \to c_N = [20\ 45]$" y "j = 2 ⇒ $N_2$ "entra" a la base"; en el paso 5 "j = 2 ⇒ $\theta_2 = x_5/Y_{52} = 15$", "i = r = 5 ⇒ $B_5$ "sale" de la base". La hoja final presenta $z' = c_B'x_B'$ como mini-tabla ($c_B'$ = 0 0 45 abajo, $x_B'$ = 10; 52,5; 15 a la derecha) = 675. No hay diferencias de procedimiento.

### (b) Lo que la cátedra enfatiza

- Algoritmo en **6 pasos** con nombres fijos: (1) forma estándar y encontrar B, N, $c_B$, $c_N$, $x_B$, $x_N$, z; (2) "matriz completa Y" = $B^{-1}N$; (3) $z_j = c_BY$; (4) evaluar $(c_j - z_j)$ = "condición de Optimización"; (5) $\theta_j$ = "condición de Factibilidad"; (6) nueva solución x′.
- Columna que **"entra"**: la $N_j$ con el **mejor (mayor) $c_j - z_j > 0$** (en Max). Columna que **"sale"**: $B_r$ con el mínimo cociente $x_i/y_{ij}$ con $y_{ij} > 0$.
- Las comillas en "entra"/"sale" son de la cátedra. La nueva básica "va en el lugar de la que salió" (se respeta el orden de filas al armar $c_B'$, $x_B'$).
- Fórmulas de actualización explícitas: $x_i' = x_i - \theta_jy_{ij}$, $x_r' = 0$, $x_j' = \theta_j$; luego $z' = c_B'x_B'$.
- Vínculo con la pizarra de factibilidad: "(N = BY) → de la cond. de factibilidad"; $z' = z + \theta(c_j - z_j)$ con θ > 0.
- Resultado de la 1ª iteración del ejemplo: base $\{x_3, x_4, x_2\}$, $x_B' = (10;\ 52{,}5;\ 15)$, $z' = 675$ (coincide con el vértice Q4 / base A₂A₃A₄ del Cap. 2).

---

## 4. `pizarras/Coef sustitución 402_260901_142610.pdf` (8 pág.; 5 con contenido, 6–8 en blanco)

Diapositivas "Capítulo 3" con tablas simplex impresas + anotaciones: base inversa, coeficientes de sustitución y costos reducidos, variables ficticias y penalización (Gran M).

### (a) Transcripción

**Pág. 1**: portada "Capítulo 3".

**Pág. 2 — "Base inversa"**. Formato de tabla de la cátedra: columnas $c_i$ | $A_i$ | $A_1 \dots A_5$ (con $c_j$ arriba) | $x_i$ | $x_i/y_{ij}$ ($y_{ij}>0$); filas finales $z_j$ y $c_j - z_j$; recuadro z = ….

Tabla 3-1

| $c_i$ | $A_i$ | $A_1$ (20) | $A_2$ (45) | $A_3$ (0) | $A_4$ (0) | $A_5$ (0) | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|
| 0 | $A_3$ | 1 | 2 | 1 | 0 | 0 | 40 | 20 |
| 0 | $A_4$ | 3 | 3/2 | 0 | 1 | 0 | 75 | 50 |
| 0 | $A_5$ | 0 | **1** | 0 | 0 | 1 | 15 | **15** |
| $z_j$ | | 0 | 0 | 0 | 0 | 0 | z = 0 | |
| $c_j - z_j$ | | 20 | **45** | 0 | 0 | 0 | | |

Tabla 3-2

| $c_i$ | $A_i$ | $A_1$ (20) | $A_2$ (45) | $A_3$ (0) | $A_4$ (0) | $A_5$ (0) | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|
| 0 | $A_3$ | **1** | 0 | 1 | 0 | −2 | 10 | **10** |
| 0 | $A_4$ | 3 | 0 | 0 | 1 | −3/2 | 105/2 | 35/2 |
| 45 | $A_2$ | 0 | 1 | 0 | 0 | 1 | 15 | |
| $z_j$ | | 0 | 45 | 0 | 0 | 45 | z = 675 | |
| $c_j - z_j$ | | **20** | 0 | 0 | 0 | −45 | | |

Tabla 3-3 (óptima)

| $c_i$ | $A_i$ | $A_1$ (20) | $A_2$ (45) | $A_3$ (0) | $A_4$ (0) | $A_5$ (0) | $x_i$ |
|---|---|---|---|---|---|---|---|
| 20 | $A_1$ | 1 | 0 | 1 | 0 | −2 | 10 |
| 0 | $A_4$ | 0 | 0 | −3 | 1 | 9/2 | 45/2 |
| 45 | $A_2$ | 0 | 1 | 0 | 0 | 1 | 15 |
| $z_j$ | | 20 | 45 | 20 | 0 | 5 | z = 875 |
| $c_j - z_j$ | | 0 | 0 | −20 | 0 | −5 | |

Recuadros a la izquierda (resaltado de colores = qué columnas se leen):
- Base de la Tabla 3-2, columnas originales de $A_3, A_4, A_2$: $\begin{bmatrix}1&0&2\\0&1&1{,}5\\0&0&1\end{bmatrix}$ → "Inversa": $\begin{bmatrix}1&0&-2\\0&1&-1{,}5\\0&0&1\end{bmatrix}$ = columnas $A_3, A_4, A_5$ de la Tabla 3-2 (resaltadas en verde).
- Base de la Tabla 3-3, columnas originales de $A_1, A_4, A_2$: $\begin{bmatrix}1&0&2\\3&1&1{,}5\\0&0&1\end{bmatrix}$ → "Inversa": $\begin{bmatrix}1&0&-2\\-3&1&4{,}5\\0&0&1\end{bmatrix}$ = columnas $A_3, A_4, A_5$ de la Tabla 3-3 (resaltadas en violeta).

**Pág. 3 — "Coeficientes de sustitución y costos reducidos"** (se repiten Tablas 3-1 y 3-2). Manuscrito:
$$Ax = b;\quad Bx_B + Nx_N = b\quad (x_{B,N} \ge 0)$$
$$Bx_B = b - Nx_N \;\Rightarrow\; x_B = B^{-1}(b - Nx_N) \;\Rightarrow\; x_B = B^{-1}b - \underbrace{B^{-1}N}_{=Y\ \text{(ver factibilidad)}}x_N$$
$$x_B = B^{-1}b - Yx_N \;\Rightarrow\; x_B = B^{-1}b - \sum_j Y_jx_j$$
$$\frac{\partial x_B}{\partial x_j} = 0 - \sum_j Y_j \quad [\text{así escrito}]$$
$$\frac{\partial x_1}{\partial x_j} = -Y_{1j};\quad \frac{\partial x_2}{\partial x_j} = -Y_{2j}\quad \longrightarrow \text{"coef de sustitución"}$$
A la derecha:
$$z' = z + \theta_j(c_j - z_j) \;\to\; \text{"ver factibilidad"};\qquad z' = z + x_j(c_j - z_j) \;\to\; \text{"ver paso a paso del simplex"}\ (x_j' = \theta_j)$$

**Pág. 4 (arriba, continuación)**:
$$\frac{\partial z'}{\partial x_j} = 0 + c_j - z_j = \underbrace{c_j - z_j}_{\text{COSTO REDUCIDO}}$$

**Pág. 4 — "Variables ficticias y penalización"**. Problema (resuelto gráficamente en la diapositiva):
$$\max z = 30x_1 + 40x_2\quad\text{s.a}\quad x_1 + x_2 \le 7;\quad x_1 - 2x_2 \ge 4;\quad x_1 = 5;\quad x_1, x_2 \ge 0$$
Gráfico: rectas $x_1 + x_2 = 7$ (roja), $x_1 - 2x_2 = 4$ (verde), $x_1 = 5$ (amarilla); vector gradiente $c_1 = 30$, $c_2 = 40$; recta de nivel $z = 30x_1 + 40x_2 = 170$ [aprox., parcialmente legible]; "ÓPTIMO" en (5; 1/2). "Solución Óptima: $x_1^* = 5$, $x_2^* = 1/2$, $z^* = 170$."

ESTÁNDAR:
$$\max z = 30x_1 + 40x_2 + 0x_3 + 0x_4\quad \text{s.a}\quad \begin{cases}x_1 + x_2 + 1x_3 + 0x_4 = 7\\ x_1 - 2x_2 + 0x_3 - 1x_4 = 4\\ x_1 + 0x_2 + 0x_3 + 0x_4 = 5\end{cases}\quad x_j \ge 0,\ j = 1..4$$
(resaltada la columna de $x_3$: sólo la 1ª fila tiene vector unitario.)

Con ficticias:
$$\max z = 30x_1 + 40x_2 + 0x_3 + 0x_4 - Mx_5 - Mx_6\quad \text{s.a}\quad \begin{cases}x_1 + x_2 + 1x_3 + 0x_4 + 0x_5 + 0x_6 = 7\\ x_1 - 2x_2 + 0x_3 - 1x_4 + 1x_5 + 0x_6 = 4\\ x_1 + 0x_2 + 0x_3 + 0x_4 + 0x_5 + 1x_6 = 5\end{cases}\quad x_j \ge 0,\ j = 1..6$$
Anotado: M "MUY GRANDES"; "MAX −, MIN +"; $x_5, x_6$ "VAR. FICTICIAS".

**Pág. 5 — tablas con penalización**

Tabla inicial

| $c_i$ | $A_i$ | $A_1$ (30) | $A_2$ (40) | $A_3$ (0) | $A_4$ (0) | $A_5$ (−M) | $A_6$ (−M) | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|---|
| 0 | $A_3$ | 1 | 1 | 1 | 0 | 0 | 0 | 7 | 7 |
| −M | $A_5$ | **1** | −2 | 0 | −1 | 1 | 0 | 4 | **4** |
| −M | $A_6$ | 1 | 0 | 0 | 0 | 0 | 1 | 5 | 5 |
| $z_j$ | | −2M | 2M | 0 | M | −M | −M | z = −9M | |
| $c_j - z_j$ | | **30+2M** | 40−2M | 0 | −M | 0 | 0 | | |

2ª tabla

| $c_i$ | $A_i$ | $A_1$ (30) | $A_2$ (40) | $A_3$ (0) | $A_4$ (0) | $A_5$ (−M) | $A_6$ (−M) | $x_i$ | $x_i/y_{ij}$ |
|---|---|---|---|---|---|---|---|---|---|
| 0 | $A_3$ | 0 | 3 | 1 | 1 | −1 | 0 | 3 | 1 |
| 30 | $A_1$ | 1 | −2 | 0 | −1 | 1 | 0 | 4 | |
| −M | $A_6$ | 0 | **2** | 0 | 1 | −1 | 1 | 1 | **1/2** |
| $z_j$ | | 30 | −60−2M | 0 | −30−M | 30+M | −M | z = 120−M | |
| $c_j - z_j$ | | 0 | **100+2M** | 0 | 30+M | −30−2M | 0 | | |

3ª tabla (óptima)

| $c_i$ | $A_i$ | $A_1$ (30) | $A_2$ (40) | $A_3$ (0) | $A_4$ (0) | $A_5$ (−M) | $A_6$ (−M) | $x_i$ |
|---|---|---|---|---|---|---|---|---|
| 0 | $A_3$ | 0 | 0 | 1 | −1/2 | 1/2 | −3/2 | 3/2 |
| 30 | $A_1$ | 1 | 0 | 0 | 0 | 0 | 1 | 5 |
| 40 | $A_2$ | 0 | 1 | 0 | 1/2 | −1/2 | 1/2 | 1/2 |
| $z_j$ | | 30 | 40 | 0 | 20 | −20 | 50 | z = 170 |
| $c_j - z_j$ | | 0 | 0 | 0 | −20 | 20−M | −50−M | |

(Resaltados en la tabla inicial: columnas $A_3$, $A_5$, $A_6$ = la identidad inicial.)

### (b) Lo que la cátedra enfatiza

- **Base inversa**: $B^{-1}$ de cualquier tabla se lee en las columnas que en la tabla inicial formaban la identidad (acá $A_3, A_4, A_5$, holguras). Lo muestra invirtiendo la matriz de columnas originales de la base y comparando.
- **"Coeficiente de sustitución"** = $-Y_{ij} = \partial x_i/\partial x_j$: cuánto cambia la básica $x_i$ por unidad de la no básica $x_j$ que entra. Se deriva de $x_B = B^{-1}b - Yx_N$.
- **"Costo reducido"** = $c_j - z_j = \partial z'/\partial x_j$, de $z' = z + x_j(c_j - z_j)$.
- Formato de tabla de la cátedra: $c_i$ | $A_i$ | columnas $A_j$ | $x_i$ | $x_i/y_{ij}$ ($y_{ij}>0$), con filas $z_j$ y $c_j - z_j$ abajo (no fila 0 arriba; no $z_j - c_j$).
- Artificiales se llaman **"variables ficticias"**; se resuelve por **penalización (Gran M)**, no por dos fases: **"MAX −, MIN +"** (coeficiente −M en Max, +M en Min). M "muy grande".
- En Max, entra la columna con mayor $c_j - z_j$ comparando expresiones en M (30+2M > 40−2M; 100+2M > 30+M).
- En la tabla óptima las ficticias quedan con $c_j - z_j$ negativos con −M (20−M, −50−M).

---

## 5. `teoria/IO 2025 - Dualidad_260806_220511.pdf` (8 pág., anotada) — y `IO 2025 - Dualidad.pdf` (7 pág., limpia)

Diapositivas impresas de Dualidad. La versión 260806 es la misma presentación con anotaciones manuscritas (y una pág. 8 en blanco con el título "DUALIDAD"). Transcribo la anotada.

### (a) Transcripción

**Pág. 1**: "Investigación Operativa — Dualidad".

**Pág. 2 — Teorema Fundamental de la Dualidad**. "Dado un programa lineal en su forma canónica y su correspondiente programa dual asociado,"

| Problema original (PRIMAL) | Problema dual |
|---|---|
| $\max z = cx$ | $\min w = b^Tu$ |
| s.a $Ax \le b$ | s.a $A^Tu \ge c^T$ |
| $x \ge 0$ | $u \ge 0$ |

Manuscrito (ejemplo): Max z = 20x₁ + 45x₂; s.a x₁ + 2x₂ ≤ 40; 3x₁ + 1,5x₂ ≤ 75; x₂ ≤ 15; $x_i \ge 0$ ⟶ Min w = 40u₁ + 75u₂ + 15u₃; s.a u₁ + 3u₂ ≥ 20; 2u₁ + 1,5u₂ + u₃ ≥ 45; $u_j \ge 0$. (Colores: c ↔ cᵀ, b ↔ b, A ↔ Aᵀ; Max ↔ Min.)

"El teorema enuncia que: Si el programa primal tiene solución óptima finita, **los valores de u que minimizan el dual son los costos marginales del programa original**. Además, el valor óptimo de la función objetivo del dual coincide con el valor óptimo de la función objetivo del original ($w^* = z^*$)."

Manuscrito: $u^{*T} = c_BB^{-1} = z_j$; $w^* = z^*$.

**Pág. 3 — En la tabla** (tabla óptima del primal, = Tabla 3-3):

| $c_i$ | $A_i$ | $A_1$ (20) | $A_2$ (45) | $A_3$ (0) | $A_4$ (0) | $A_5$ (0) | $x_i$ |
|---|---|---|---|---|---|---|---|
| 20 | $A_1$ | 1 | 0 | 1 | 0 | −2 | 10 |
| 0 | $A_4$ | 0 | 0 | −3 | 1 | 9/2 | 45/2 |
| 45 | $A_2$ | 0 | 1 | 0 | 0 | 1 | 15 |
| $z_j$ | | 20 | 45 | 20 | 0 | 5 | z = 875 |
| $c_j - z_j$ | | 0 | 0 | −20 | 0 | −5 | |

Recuadros: rojo = columna $c_B$ (20, 0, 45); azul = bloque $A_3..A_5$ de las filas (= $B^{*-1}$); amarillo = $z_j$ de $A_3..A_5$ (20, 0, 5).
"Costo marginal o Valor implícito: $\;c_B\,B^{*-1} = z_j$."

**Pág. 4 — Relación de x con u**

Primal: Max z = 20x₁ + 45x₂; s.a x₁ + 2x₂ ≤ 40; 3x₁ + 1,5x₂ ≤ 75; x₂ ≤ 15; x₁, x₂ ≥ 0.
Dual: Min w = 40u₁ + 75u₂ + 15u₃; s.a u₁ + 3u₂ ≥ 20 (manuscrito: $u_4$); 2u₁ + 1,5u₂ + u₃ ≥ 45 (manuscrito: $u_5$); u₁, u₂, u₃ ≥ 0.

| Tipo | Vector x | Coef x | Vector u | Coef u | Tipo |
|---|---|---|---|---|---|
| Concreta | $x_1$ | 20 | $u_4$ | 0 | Exceso |
| Concreta | $x_2$ | 45 | $u_5$ | 0 | Exceso |
| Holgura | $x_3$ | 0 | $u_1$ | 40 | Concreta |
| Holgura | $x_4$ | 0 | $u_2$ | 75 | Concreta |
| Holgura | $x_5$ | 0 | $u_3$ | 15 | Concreta |

**Pág. 5 — Valores del Primal en el Dual y viceversa**

Tabla óptima primal (igual a la de pág. 3), resaltados: base $A_1, A_4, A_2$; $x_i$ = 10 y 15; $z_j$ de $A_3..A_5$ = 20, 0, 5; $c_j - z_j$ de $A_1, A_2$ = 0, 0; z = 875.
"$x^* = (10, 15, 0, 22.5, 0)$. Base A1, A4, A2."
"$u^* = (20, 0, 5, 0, 0)$. Base A1, A3."

Tabla óptima dual (Min w = 40u₁ + 75u₂ + 15u₃):

| $c_i$ | $A_i$ | $A_1$ (40) | $A_2$ (75) | $A_3$ (15) | $A_4$ (0) | $A_5$ (0) | $x_i$ |
|---|---|---|---|---|---|---|---|
| 40 | $A_1$ | 1 | 3 | 0 | −1 | 0 | 20 |
| 15 | $A_3$ | 0 | −9/2 | 1 | 2 | −1 | 5 |
| $z_j$ | | 40 | 105/2 | 15 | −10 | −15 | w = 875 |
| $c_j - z_j$ | | 0 | 22,5 | 0 | 10 | 15 | |

Mini-tabla de correspondencia: $x_1 \leftrightarrow u_4$, $x_2 \leftrightarrow u_5$, $x_3 \leftrightarrow u_1$, $x_4 \leftrightarrow u_2$, $x_5 \leftrightarrow u_3$.

**Pág. 6 — Para los valores no base**. Impreso: "Reemplazamos costo marginal por **costo reducido −(c_j − z_j)**". Manuscrito:
- Forma canónica: $A^Tu^* \ge c^T$
- Forma estándar: $A^Tu^* - s^* = c^T$
- Transponer: $u^{*T}A - s^{*T} = c$ (las tres "Equivalentes")
- $u^{*T}A - c = s^{*T}$, partiendo cada término en B | N:
  - $u^{*T}B - c_B = s_B^{*T}$ ⟶ (TFD $u^{*T} = c_BB^{-1}$) ⟶ $c_B\underbrace{B^{-1}B}_{I} - c_B = 0$
  - $u^{*T}N - c_N = s_N^{*T}$ (resaltado) ⟶ $c_B\underbrace{B^{-1}N}_{Y} - c_N = \underbrace{c_BY}_{z_j} - c_N = z_j - c_j = -(c_j - z_j)$ (anotado "BY = N")
  - [cortado: debajo hay una línea más que el escaneo no muestra]

**Pág. 7 — Resumen** (las dos tablas óptimas + cuadro):

| | | Primal | Dual | Dual | Primal |
|---|---|---|---|---|---|
| $x_1$ | $u_4$ | $x_1 = 10$ | $-z_4 = 10$ | $u_1 = 20$ | $z_3 = 20$ |
| $x_2$ | $u_5$ | $x_2 = 15$ | $-z_5 = 15$ | $u_2 = 0$ | $z_4 = 0$ |
| $x_3$ | $u_1$ | $x_3 = 0$ | $c_1 - z_1 = 0$ | $u_3 = 5$ | $z_5 = 5$ |
| $x_4$ | $u_2$ | $x_4 = 22.5$ | $c_2 - z_2 = 22.5$ | $u_4 = 0$ | $-(c_1 - z_1) = 0$ |
| $x_5$ | $u_3$ | $x_5 = 0$ | $c_3 - z_3 = 0$ | $u_5 = 0$ | $-(c_2 - z_2) = 0$ |

(Columna "Dual" de la izquierda: valores leídos de la tabla del dual; columna "Primal" de la derecha: valores leídos de la tabla del primal. En la versión limpia, las dos últimas celdas dicen "$c_1 - z_1 = 0$" y "$c_2 - z_2 = 0$"; en la anotada se les agregó a mano el signo: "$-(c_1 - z_1)$", "$-(c_2 - z_2)$".)

**Diferencias de la versión limpia `IO 2025 - Dualidad.pdf` (7 pág.)**: mismas diapositivas sin anotaciones manuscritas: falta el ejemplo dual escrito a mano en la pág. 2, falta $u^{*T} = c_BB^{-1} = z_j$, faltan las etiquetas $u_4$/$u_5$ en las restricciones duales, la pág. 6 sólo tiene el título y la frase sobre el costo reducido (sin derivación), y el resumen tiene los signos sin corregir. No tiene la pág. 8 en blanco.

### (b) Lo que la cátedra enfatiza

- **Cómo arma el dual**: desde la **forma canónica** (Max, ≤, x ≥ 0) ⟶ Min $w = b^Tu$, $A^Tu \ge c^T$, $u \ge 0$. Variables duales $u$ (no $y$); las de exceso del dual se numeran a continuación ($u_4$, $u_5$).
- **Teorema Fundamental de la Dualidad (TFD)**: "los valores de u que minimizan el dual son los costos marginales del programa original" y $w^* = z^*$; en fórmula **$u^{*T} = c_BB^{-1} = z_j$**.
- **"Costo marginal o Valor implícito"** = $c_B B^{*-1} = z_j$ leído en la fila $z_j$ bajo las columnas de holgura ($B^{*-1}$ = base óptima inversa, con asterisco).
- **Correspondencia de variables**: concretas del primal ↔ excesos del dual ($x_1 \leftrightarrow u_4$, $x_2 \leftrightarrow u_5$); holguras del primal ↔ concretas del dual ($x_3 \leftrightarrow u_1$, …).
- Para variables no básicas: "reemplazamos costo marginal por **costo reducido −(c_j − z_j)**"; derivación $s_N^{*T} = z_j - c_j = -(c_j - z_j)$.
- Lectura cruzada en el resumen: valores primales = $-z_j$ de los excesos del dual y $c_j - z_j$ de las concretas del dual; valores duales = $z_j$ de las holguras del primal y $-(c_j - z_j)$ de las concretas del primal.
- [nota del transcriptor: la tabla óptima del dual (Min) muestra todos los $c_j - z_j \ge 0$ (0; 22,5; 0; 10; 15), es decir el criterio de óptimo en Min con la convención $c_j - z_j$ es "todos ≥ 0". No lo dice en palabras; se infiere de la tabla. Tampoco muestra las columnas de ficticias del dual.]

---

## 6. `pizarras/Transporte, transbordo y asignación_260820_193558.pdf` (15 pág.; 13 con contenido)

Diapositivas impresas (fuente citada en una de ellas: "Modelos Especiales de Programación Lineal — Norma Torrent") con algunas marcas manuscritas. Planteo como PL; no hay métodos de resolución (esquina noroeste, Vogel, MODI) en este archivo.

### (a) Transcripción

**Pág. 1**: "Transporte, transbordo y asignación — Investigación Operativa".

**Págs. 2–4 — "Empecemos con un ejemplo"**. "Tres fábricas envían su producto a cinco distribuidores. Las disponibilidades, los requerimientos y los costos unitarios de transporte se dan en la siguiente tabla. ¿Qué cantidad del producto debe enviarse desde cada fábrica a cada distribuidor de modo de minimizar el costo total de transporte?"

| Fábricas | D1 | D2 | D3 | D4 | D5 | Disponibilidades |
|---|---|---|---|---|---|---|
| 1 | 20 | 19 | 14 | 21 | 16 | 40 |
| 2 | 15 | 20 | 13 | 19 | 16 | 60 |
| 3 | 18 | 15 | 18 | 20 | 21 | 70 |
| Requerimientos | 30 | 20 | 30 | 40 | 50 | |

Manuscrito: Σ requerimientos = 170 ↔ Σ disponibilidades = 170.

Modelo: $\min w = 20x_{11} + 19x_{12} + 14x_{13} + \dots + 21x_{35}$, s.a
$x_{11}+x_{12}+x_{13}+x_{14}+x_{15} = 40$; $x_{21}+\dots+x_{25} = 60$; $x_{31}+\dots+x_{35} = 70$;
$x_{11}+x_{21}+x_{31} = 30$; $x_{12}+x_{22}+x_{32} = 20$; $x_{13}+x_{23}+x_{33} = 30$; $x_{14}+x_{24}+x_{34} = 40$; $x_{15}+x_{25}+x_{35} = 50$;
$x_{ij} \ge 0$ (i = 1,2,3; j = 1,…,5). "$x_{ij}$ cantidad enviada desde la fábrica i al distribuidor j."
Solución: $x_{15}^* = 40$, $x_{21}^* = 20$, $x_{23}^* = 30$, $x_{25}^* = 10$, $x_{31}^* = 10$, $x_{32}^* = 20$, $x_{34}^* = 40$; $w^* = 2.770$.

**Pág. 5 — Formulación general del modelo de transporte**. $F_1..F_m$: m fuentes con capacidades $a_1..a_m$; $D_1..D_n$: n destinos con demandas $b_1..b_n$; $x_{ij}$: cantidad que sale de la fuente i y llega al destino j; $c_{ij}$: costo unitario de la ruta ij.
$$\min w = \sum_{i=1}^m\sum_{j=1}^n c_{ij}x_{ij}\quad\text{s.a}\quad \sum_{j=1}^n x_{ij} \le a_i\ (i=1..m)\ \text{[oferta]};\quad \sum_{i=1}^m x_{ij} \ge b_j\ (j=1..n)\ \text{[demanda]};\quad x_{ij}\ge 0\ \text{[signo]}$$
(Grafo bipartito $F_i \to D_j$.)

**Pág. 6 — Problema balanceado**. "El modelo tiene dos tipos generales de restricciones: la cantidad enviada desde una fuente no puede exceder su capacidad (oferta); la cantidad enviada a un destino no puede ser inferior a su requerimiento (demanda). Si un problema se ajusta a las restricciones descritas pero su función objetivo es de maximización, sigue siendo un problema de transporte. Si $\sum_i a_i = \sum_j b_j$, la oferta total es igual a la demanda total, y el problema se denomina problema de transporte balanceado." Esquema: "Lo disponible = Lo requerido ⇒ Oferta = Demanda ⇒ Mercado Perfecto" → "Modelo Balanceado".

**Pág. 7 — Oferta > demanda (destino ficticio)**. "Supongamos que para el problema del ejemplo, la oferta de la fábrica 2 fuese igual a 80 unidades." Manuscrito: 60 → 80; Σ oferta = 190, Σ demanda = 170.
$\min w = 20x_{11} + \dots + 21x_{35} + 0x_{16} + 0x_{26} + 0x_{36}$; s.a $x_{11}+\dots+x_{15}+x_{16} = 40$; $x_{21}+\dots+x_{26} = 80$; $x_{31}+\dots+x_{36} = 70$; restricciones de destinos 1–5 iguales (marcadas ✓); $x_{16}+x_{26}+x_{36} = 20$ ← "Destino 6"; $x_{ij}\ge0$ (i=1,2,3; j=1..6).
Solución: $x_{15}^*=40$, $x_{21}^*=30$, $x_{23}^*=30$, $x_{24}^*=10$, $x_{25}^*=10$, $x_{32}^*=20$, $x_{34}^*=30$ y $x_{36}^*=20$ (recuadrado); $w^* = 2.730$.

**Pág. 8 — Demanda > oferta (fábrica ficticia)**. "Supongamos ahora que en el ejemplo original los requerimientos del distribuidor 5 asciendan a 60 unidades. El modelo balanceado (resultante de incorporar la fábrica ficticia 4)…" Manuscrito: 50 → 60; Σ demanda = 180, Σ oferta = 170.
$\min w = 20x_{11} + \dots + 21x_{35} + 0x_{41} + \dots + 0x_{45}$; s.a filas 1–3 iguales; $x_{41}+x_{42}+x_{43}+x_{44}+x_{45} = 10$ (señalada); columnas $x_{1j}+x_{2j}+x_{3j}+x_{4j} = b_j$ con $b_5 = 60$; $x_{ij}\ge0$ (i=1..4; j=1..5).
Solución: $x_{15}^*=40$, $x_{21}^*=10$, $x_{23}^*=30$, $x_{25}^*=20$, $x_{31}^*=20$, $x_{32}^*=20$, $x_{34}^*=30$ y $x_{44}^*=10$ (recuadrado); $w^* = 2.760$.

**Págs. 9–10 — El problema de Transbordo**. "Un problema de transporte permite sólo envíos directamente desde los puntos de origen a los puntos de demanda. En muchas situaciones, sin embargo, existe la posibilidad de hacer envíos a través de puntos intermedios (puntos de transbordo). En tales casos estamos frente a problemas de transbordo."
Red: orígenes 1 (1.000 u) y 2 (1.200 u); transbordo 3 y 4; destinos 5 (800 u), 6 (900 u), 7 (500 u). Arcos (costo): 1→3 (3), 1→4 (4), 2→3 (2), 2→4 (5), 3→4 (7), 3→5 (8), 3→6 (6), 4→6 (4), 4→7 (9), 5→6 (5), 6→7 (3).
$$\min w = 3x_{13} + 4x_{14} + 2x_{23} + 5x_{24} + 7x_{34} + 8x_{35} + 6x_{36} + 4x_{46} + 9x_{47} + 5x_{56} + 3x_{67}$$
s.a
- restricciones de los puntos de origen: $x_{13} + x_{14} = 1.000$; $x_{23} + x_{24} = 1.200$
- restricciones de los puntos de transbordo: $-x_{13} - x_{23} + x_{34} + x_{35} + x_{36} = 0$; $-x_{14} - x_{24} - x_{34} + x_{46} + x_{47} = 0$
- restricciones de los puntos de destino: $x_{35} - x_{56} = 800$; $x_{36} + x_{46} + x_{56} - x_{67} = 900$; $x_{47} + x_{67} = 500$
- $x_{ij} \ge 0$ (i = 1,…,6; j = 3,…,7)

Manuscrito: "$x_{13} + x_{23} = x_{35} + x_{36} + x_{34}$ ⇒ $x_{13} + x_{23} - x_{35} - x_{36} - x_{34} = 0$" (lo que entra = lo que sale); "$x_{13} + x_{14} = 1000$"; "$x_{23} + x_{24} = 1200$". Arcos usados marcados en verde en el grafo.
Solución: $x_{14}^* = 1.000$, $x_{23}^* = 1.200$, $x_{35}^* = 800$, $x_{36}^* = 400$, $x_{46}^* = 1.000$ y $x_{67}^* = 500$; $w^* = 20.700$.

**Págs. 11–13 — El problema de Asignación**. "Los problemas de asignación presentan una estructura similar a los de transporte con la diferencia de que la oferta en cada origen es de **valor uno** (subrayado), como lo es la demanda en cada destino. Tal es el caso de asignar trabajos a máquinas, representantes de ventas a zonas geográficas, investigadores a proyectos, etc. La restricción que existe en este tipo de problemas es que a cada oferta se le asigna una sola demanda y a cada demanda se le asigna una sola oferta. Dado que, por cada pareja asignada existe un "costo" asociado, […] el objetivo es elegir asignaciones que minimicen el costo total."
Ejemplo: relevo de natación 200 m; Lucía sólo nada libre; Julia, Ana y Paula a mariposa, espalda, pecho. Tiempos (s):

| | Mariposa | Espalda | Pecho |
|---|---|---|---|
| Julia | 33 | 35 | 37 |
| Ana | 33 | 37 | 37 |
| Paula | 32 | 36 | 39 |

$\min w = 33x_{11} + 35x_{12} + \dots + 36x_{32} + 39x_{33}$; s.a $\sum_j x_{ij} = 1$ (i = 1,2,3); $\sum_i x_{ij} = 1$ (j = 1,2,3); $x_{ij} \ge 0$.
Solución: $x_{12}^* = 1$ (Julia–espalda), $x_{23}^* = 1$ (Ana–pecho), $x_{31}^* = 1$ (Paula–mariposa); $w^* = 104$.

**Pág. 14**: portada "Programación Entera y Mixta" (sin contenido). **Pág. 15**: en blanco.

### (b) Lo que la cátedra enfatiza

- Variable $x_{ij}$ = cantidad de i a j; F.O. de minimización se llama **w** (no z).
- Formulación general con **oferta ≤ $a_i$** y **demanda ≥ $b_j$**; en los ejemplos balanceados se escriben con =.
- "Balanceado" = Σ oferta = Σ demanda = "Mercado Perfecto". Desbalance: se agrega **destino ficticio** (si sobra oferta) o **fábrica ficticia** (si falta oferta), con costo 0, y su oferta/demanda = la diferencia.
- Maximizar no cambia que sea transporte ("sigue siendo un problema de transporte").
- Transbordo: restricción de nodo intermedio = **lo que entra = lo que sale** ($= 0$); destinos con red neta (entradas − salidas = demanda). Clasifica restricciones en "de origen / de transbordo / de destino".
- Asignación = transporte con ofertas y demandas = 1 ("valor uno" subrayado).
- Valores óptimos de referencia: 2.770 (original), 2.730 (oferta 80), 2.760 (demanda 60), 20.700 (transbordo), 104 (asignación).
