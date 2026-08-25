# TeoriaSimulacion_Flamini_PARTE1_2022.pdf

_Transcripción de páginas 13 a 24 (apunte manuscrito de clase)._

---

--- pág. 13 ---

| | Simulacion (Teoria) | Hoja 7 |
|---|---|---|

**19/04**

**§ 1.4.2 "Prueba de Escritorio"**

$A_i$ y $S_i$ &nbsp;&nbsp; $i = 0, 1, 2, \dots, n$

V.A. con distrib. de probabilidad conocida ⊛ si los tiempos de llegada y partida ($t_i$ y $C_i$) cumplen con las condiciones de un proceso estocástico de Poisson.

⊛ &nbsp;&nbsp; $A_i \sim Exp(\alpha)$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ($A_i = t_i - t_{i-1}$)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $S_i \sim Exp(\beta)$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ($S_i = C_i - t_i - D_i$)

> [FIGURA pág. 13]: Reproducción de la fig. 1.4 del libro (indicada al margen como "Pag 14 fig 1.4"): representación de la computadora de un sistema de cola de un solo servidor. Un rectángulo grande dividido en tres bloques por líneas punteadas verticales/horizontales:
> - **Bloque izquierdo "Estado del Sistema"**: a la izquierda, dos cajitas cuadradas (clientes ya atendidos / en el sistema) y una pila vertical rayada que representa la cola; sobre la pila la anotación *"N° de Clientes en cola Q(t)"* (flecha roja hacia la cola). Debajo, con flecha, *"Estado del servidor B(t)"*. Otra flecha señala *"Tiempos de arribos de quienes están en cola"* apuntando a las cajitas de la fila inferior.
> - **Bloque central "Reloj de simulación"**: una cajita vacía. Debajo, flecha hacia *"Tiempo del último evento"*.
> - **Bloque derecho "Lista de Eventos futuros"**: dos cajitas apiladas; flechas hacia la derecha indican *"tiempos de arribo $t_i$ (de tipo arribo)"* y *"tiempos de salida $C_i$ (de tipo salida)"*.
> - **Franja inferior "contadores Estadísticos"**: cuatro cajitas en fila; flechas de colores las etiquetan, de izquierda a derecha, como: *"N° de clientes que completaron su demora en cola"*, *"Demora total D ⊛"*, *"Área bajo Q(t) ⊛"* y *"Área Bajo B(t) ⊛"*.
> - Al margen izquierdo: *"Pag 14 / fig 1.4"*.
> La figura ilustra los tres componentes de la representación interna de la simulación por eventos discretos (estado del sistema, reloj, lista de eventos) más los contadores estadísticos que alimentan las medidas de rendimiento.

⊛ &nbsp; $\hat{d}(n) = \sum_{i=1}^{n} D_i$

⊛ &nbsp; $\hat{q}(n) = \dfrac{\int_{0}^{T(n)} Q(t)\,dt}{T(n)}$

⊛ &nbsp; $\hat{\mu}(n) = \dfrac{\int_{0}^{T(n)} B(t)\,dt}{T(n)}$

---

--- pág. 14 ---

momento 0 → vacío e inactivo &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <u>inicializar lista de eventos</u>

$t_1 > 0$ &nbsp;&nbsp;&nbsp;&nbsp; $t = 0$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↳ calcula el primer evento

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; arribo del primer cliente

<u>mirar pag 20</u>

> [FIGURA pág. 14 — gráfico superior]: Gráfico escalonado de $B(t)$ (estado del servidor: ocupado = 1 / desocupado = 0) contra $t(s)$. Eje horizontal marcado en: **0,4 — 1 — 1,6 — 2 — 2,1 — 2,4 — 3 — 3,1 — 3,9 — 4 — 5 — 6 — 7 — 8**. La función vale 0 en $[0;\,0{,}4)$, salta a **1** en $t = 0{,}4$ y se mantiene en 1 (trazo naranja horizontal con puntos marcados en 0,4 · 1,6 · 2,1 · 2,4 · 3,1) hasta $t = 3{,}1$, donde vuelve a 0. El área bajo la curva está rayada y subdividida por segmentos verticales en 1,6 · 2,1 · 2,4. Llaves debajo del eje miden los tramos: **1,2** (de 0,4 a 1,6), **0,5** (de 1,6 a 2,1) y **0,3** (de 2,1 a 2,4). Ilustra el cálculo de $\int_0^{T(n)} B(t)\,dt$ = área bajo $B(t)$ para la utilización del servidor.

> [FIGURA pág. 14 — gráfico inferior]: Gráfico escalonado de $Q(t)$ (número de clientes en cola) contra $t(s)$. Eje vertical con marcas en **1** y **2**. Eje horizontal marcado en: **0,4 — 1 — 1,6 — 2 — 2,1 — 2,4 — 3 — 3,1 — 3,9 — 4 — 5 — 6 — 7 — 8**. $Q(t) = 0$ desde 0 hasta 1,6; salta a **1** en $t = 1{,}6$; salta a **2** en $t = 2{,}1$; baja a **1** en $t = 2{,}4$ y se mantiene en 1 hasta $t = 3{,}1$, donde vuelve a 0. Las áreas están rayadas. Llaves debajo del eje miden los tramos: **0,5** (1,6 → 2,1), **0,3** y **0,2** (tramo 2,1 → 2,4) y **0,7** (2,4 → 3,1). Ilustra el cálculo de $\int_0^{T(n)} Q(t)\,dt$ = área bajo $Q(t)$ para el número promedio en cola.

$D_1 = 0$

$D_2 = 2{,}4 - 1{,}6 = 0{,}8$

**2/05**

**§ 1.3 Organización y Lógica del Programa** (pag 15)

1) Tanto $A_i$ y $S_i$ son V.A.I.I. y tienen distribución exp

&nbsp;&nbsp;&nbsp;&nbsp; $A_i \sim Exp(\alpha)$

&nbsp;&nbsp;&nbsp;&nbsp; $S_i \sim Exp(\beta)$

---

--- pág. 15 ---

| | Simulacion (Teoria) | Hoja 8 |
|---|---|---|

2) La computadora genera n° aleatorios con <u>distribución uniforme</u> en el intervalo $(0,1)$

&nbsp;&nbsp;&nbsp;&nbsp; $0(\ ,\ 0{,}000\ ,\ \dots\ ,\ )1$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ← _cualquier valor tiene igual chance de ser generado por el programa._

(en realidad son números <u>pseudo aleatorios</u> por ser generados por un programa).

$U \sim U(0,1) \;\rightarrow\; -\alpha \ln U \sim Exp(\alpha)$

(pag 16)

**Rutina de Arribos** (pág 16)

> [FIGURA pág. 15 — diagrama de flujo izquierdo, "Evento Arribo"]:
> - Óvalo de inicio: **Evento Arribo**
> - → Caja: **"Se determina el próximo arribo"**
> - → Rombo de decisión: **"¿servidor ocupado?"** — salida **Sí** a la izquierda, **No** a la derecha.
> - Rama **Sí** → Caja: **"Sumamos 1 al n° de clientes en cola"** → Caja: **"Guardamos el tiempo de llegada del cliente"** → óvalo **FIN**.
> - Rama **No** → Caja: **"$D_i = 0$ y calculamos estadísticos"** → Caja: **"Aumentamos en 1 el n° de clientes que completaron su demora en cola"** → Caja: **"$B_i = 1$"** → Caja: **"Determinamos el tiempo de partida de ese cliente"** → óvalo **FIN**.

> [FIGURA pág. 15 — diagrama de flujo derecho, "Evento Partida"]:
> - Óvalo de inicio: **Evento Partida**
> - → Rombo de decisión: **"¿cola vacía?"** — salida **Sí** a la izquierda, **No** a la derecha.
> - Rama **Sí** → Caja: **"Poner el servidor en 'desocupado' $B_i = 0$"** → Caja: **"Eliminamos el evento partida de la lista de eventos"** → óvalo **FIN**.
> - Rama **No** → Caja: **"Calcular la demora del cliente que entra en servicio ($S_i$) y actualizar los contadores estadísticos"** → Caja: **"Restar 1 al n° de clientes en cola"** → Caja: **"Sumar 1 al n° de clientes que completaron su demora en cola"** → Caja: **"Determinar el tiempo de partida de ese cliente"** → Caja: **"Mover cada cliente de la cola un lugar hacia arriba"** → óvalo **FIN**.

---

--- pág. 16 ---

Se puede calcular todo conociendo $\alpha$, $\beta$, $n$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↳ Dist Exponencial

| | $U$ |
|---|---|
| 1 | 0,5121 |
| 2 | 0,8116 |
| 3 | 0,6717 |
| 4 | 0,1901 |
| 5 | 0,5148 |
| 6 | 0,6467 |
| 7 | 0,8954 |
| 8 | 0,3824 |
| 9 | 0,0279 |
| 10 | 0,8365 |

$\alpha = 0{,}7$

$\beta = 0{,}66$

$A_1 = t_1 - t_0 = t_1 - 0 = t_1$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⎫

$A_1 = -0{,}7 \times \ln(0{,}5121)$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⎬ &nbsp; $A = 0{,}4684$

> [FIGURA pág. 16 — esquema 1]: Reproducción del cuadro "estado del sistema / reloj de simulación / lista de eventos futuros". En el bloque izquierdo (estado del sistema) cajitas con los valores **0**, **1**, **0**; en el bloque central (reloj de simulación) una cajita con **0,4684**; en el bloque derecho (lista de eventos futuros) una cajita con dos filas: **A → 0,4684** y **P → ∞**. Debajo, la franja de contadores estadísticos con cuatro cajitas: **0**, **0**, **0**, **0**. Muestra el estado tras generar el primer arribo.

$A_2 = -0{,}7 \times \ln(0{,}8116) = 0{,}1461 = t_2 - t_1 = 0$; &nbsp; $t_2 = 0{,}4684 \rightarrow \underline{t_2 = 0{,}6145}$

> [FIGURA pág. 16 — esquema 2]: Segundo cuadro igual al anterior; en la lista de eventos futuros aparece **A → 0,6145** ($t_2$) y **P → 0,7310** ($C_1$).

$S_1 = -0{,}66 \ln(0{,}6717)$

&nbsp;&nbsp;&nbsp;&nbsp; $= 0{,}2626$

$S_1 + t_1 = C_1 = 0{,}7310$

---

--- pág. 17 ---

| | Simulacion (teoria) | Hoja 9 |
|---|---|---|

**9/05**

**§ 1.5. Simulación de un sistema de inventario** (pag 21)

Empresa que comercializa un solo tipo de artículo

Fin de la simulación: una vez transcurridos $n$ períodos

"Control de inventario" se hace al inicio (o al final) del período

> [FIGURA pág. 17]: Recta temporal horizontal con marcas en **0, 1, 2, …, n** y flecha hacia la derecha rotulada $t$. Una flecha desde abajo a la izquierda indica *"se hace al final de cada período (mes)"* y otra sobre $n$ indica *"Fin simulación"*.

Tiempos entre demandas (V.A.I.I.) $\sim Exp(\lambda) \rightarrow \lambda = 0{,}1$ meses (3 días) &nbsp;&nbsp; ← _tiempo promedio entre demandas_

$D$ = tamaño de la demanda (distribución empírica):

$$D = \begin{cases} 1 & \text{con prob } 1/6 \\ 2 & \text{con "} \;\; 1/3 \\ 3 & \text{con "} \;\; 1/3 \\ 4 & \text{con "} \;\; 1/6 \end{cases} \qquad \text{(ej. libro)}$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\overline{\phantom{xxx} 1 \phantom{xxx}}$

$P(D \neq 0) = P\big((D=1) \cup (D=2) \cup (D=3) \cup (D=4)\big) = P(D=1) \cup P(D=2) \cup P(D=3) \cup P(D=4)$

$= \dfrac{1}{6} + \dfrac{1}{3} + \dfrac{1}{3} + \dfrac{1}{6} = 1 \; \checkmark$

~~Costo por pedido~~ $= C_p = k + i\,Z$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓ &nbsp;&nbsp; ↓ &nbsp;&nbsp; ↓

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Costo fijo &nbsp;&nbsp; Costo por unidad &nbsp;&nbsp; n° de artículos comprados al proveedor

$s$ = nivel mínimo de mercadería en stock

$S$ = nivel máximo &nbsp; " &nbsp;&nbsp; " &nbsp;&nbsp; " &nbsp;&nbsp; " &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $(s, S)$

---

--- pág. 18 ---

**Política de Pedidos**

$$Z = \begin{cases} S - I & \text{si } I < s \\ 0 & \text{si } I \geq s \end{cases}$$

$I$ = nivel real de inventario al momento de hacer un pedido &nbsp;&nbsp; ← _final de c/período (mes)_

(Si $Z = 0$ entonces $C_p = 0$) &nbsp;&nbsp; ← _porque no hago pedido._

Demora por parte del proveedor en entregar un pedido tiene distribución uniforme en $[0{,}5\,;\,1]$

→ $C_T = C_p + C_M + C_F$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $C_M = h \cdot \overline{I}^{\,+}$

↑ _Medida del rendimiento_ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $C_F = \pi \cdot \overline{I}^{\,-}$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↳ La finalidad es minimizar el costo total, eventualmente haciendo variar el par $(s, S)$

| $s$ | 20 | ⋯ | 60 |
|---|---|---|---|
| $S$ | 40 | ⋯ | 100 |

(ver ejemplo)

> [FIGURA pág. 18]: Gráfico de $I(t)$ (nivel de inventario) contra $t$. Eje vertical con marcas en $S$ (arriba), $I(0)$ (algo más abajo) y $s$ (línea de trazos horizontal); eje horizontal con marcas en 0, 1, 2, …, n. La curva es escalonada: parte de $I(0)$ y va bajando en escalones (cada escalón = una demanda) con puntos llenos/huecos que marcan la discontinuidad; en algunos puntos, al caer por debajo de $s$, salta hacia arriba hasta $S$ (flecha vertical rotulada **$S - I$**), representando la llegada de un pedido. En la parte central el nivel cruza el eje y queda **negativo** (faltante/backlog), tramo trazado en rojo por debajo de 0; luego un nuevo pedido lo devuelve a valores positivos. Se distinguen con colores el área por encima de 0 ($I^+$) y por debajo de 0 ($I^-$). Al margen derecho: *"leer hasta pag 78"*.

$I(t)^{+} = \max\{I(t),\, 0\}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $I^{+} \geq 0$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\overline{I}^{\,+} = \dfrac{\int_{0}^{n} I^{+}(t)\,dt}{n}$

$I(t)^{-} = \max\{-I(t),\, 0\}$ &nbsp;&nbsp;&nbsp;&nbsp; $I^{-} \geq 0$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\overline{I}^{\,-} = \dfrac{\int_{0}^{n} I^{-}(t)\,dt}{n}$

---

--- pág. 19 ---

| | Simulacion (Teoria) | Hoja 10 |
|---|---|---|

**16/05**

V.V.A.A. &nbsp; Tiempos entre demandas $= T_i \sim Exp(\lambda)$ &nbsp;&nbsp;&nbsp;&nbsp; $\lambda = 0{,}45 \; \dfrac{mes}{cliente}$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Tamaño de la demanda $= D \sim$ Empírica

~~Arribos~~ &nbsp; Demora en la entrega $\sim U[0{,}5\,;\,1]$ &nbsp;&nbsp;&nbsp;&nbsp; ⊛ $D = \begin{cases} 1 & \text{con prob } 1/6 \\ 2 & \text{"} \;\; 1/3 \\ 3 & \text{"} \;\; 1/3 \\ 4 & \text{"} \;\; 1/6 \end{cases}$

Otros supuestos: $(s, S) = (15, 30)$. &nbsp; $I(0) = 20$ artíc.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "Final simulación" → $n = 120$ mes

**Representación de la computadora**

> [FIGURA pág. 19]: Cuadro grande dividido en bloques (misma estructura que la fig. 1.4 pero para el modelo de inventario):
> - **"Estado del Sist"** (bloque izquierdo): cuatro cajitas. Primera: valor **20**, con correcciones sucesivas tachadas **19** y **17**, rotulada $I(t)$. Segunda: **20** (también corregido a 19 y 17), rotulada $I^{+}(t)$. Tercera: **0**, rotulada $I^{-}(t)$. Cuarta: **0**, rotulada *"último pedido pendiente de entrega"*. Debajo, dos cajitas fijas: **15** rotulada $s$ y **30** rotulada $S$.
> - **"Reloj de Sim."** (bloque central superior): una cajita con **0,0349** tachado y reemplazado por **0,0852**.
> - **Lista de eventos** (bloque derecho): cuatro filas rotuladas a la izquierda y con sus valores a la derecha: *"Arribo de un pedido"* → **∞**; *"Arribo de un cliente"* → **0,0349** (tachado) → **0,0852**; *"Fin de la Sim"* → **120**; *"evaluación de inventario"* → **1**. Una flecha desde arriba señala la primera fila con la aclaración *"pendiente de entrega por parte del mayorista"*.
> - **"Contadores Estadísticos"** (franja inferior): cuatro cajitas con **0**, **0**, **0** (corregido a **0,6978**) y **0**; flechas hacia abajo las rotulan como *"costo por pedido"* ($C_p = k + i\,Z$), *"costo acum por pedido"*, *"área bajo $I^{+}(t)$"* y *"área bajo $I^{-}(t)$"*.

> [FIGURA pág. 19 — gráfico inferior izquierdo]: Gráfico de $I(t)$ contra $t$, con los ejes rotulados $I(t)$, $I^{+}$ (violeta) e $I^{-}$ (naranja). Sobre el eje vertical están marcados $S = 30$, $I(0) = 20$, **19**, **17** y $s = 15$ (línea de trazos). Trazo escalonado violeta: desde $I(0) = 20$ hasta $t_1$, luego baja a 19 hasta $t_2$, etc. Las áreas rectangulares bajo cada escalón se rotulan $A_1$ (violeta) y $A_2$ (verde). Marcas $t_1$ y $t_2$ sobre el eje horizontal.

$A_1 = 0{,}0349 \times 20 = 0{,}6978$

$A_2 = 0{,}0503 \times 19 = 0{,}9557$

> [FIGURA pág. 19 — recta de la distribución empírica de $D$]: Segmento $[0,1]$ dividido en cuatro tramos con llaves debajo rotuladas **1/6**, **1/3**, **1/3**, **1/6**. Sobre la recta, flechas indican dónde caen los números aleatorios: **0,1146** → *"compra 1 artículo"*; **0,3557** → *"compra 2 artículos"* ⊛.

| $U \sim (0,1)$ |
|---|
| 0,9254 |
| 0,1146 |
| 0,2942 |
| 0,3557 |
| 0,9372 |

$T_i = t_i - t_{i-1}$

$T_1 = -\lambda \ln U$

&nbsp;&nbsp;&nbsp;&nbsp; $= -0{,}45 \ln(0{,}9254)$

&nbsp;&nbsp;&nbsp;&nbsp; $= 0{,}0349$

$T_1 = t_1 - \underbrace{t_0}_{= 0}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $T_3 = 0{,}0292$

&nbsp;&nbsp;&nbsp;&nbsp; $= t_1$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $t_3 = 0{,}1144$

$T_2 = 0{,}0503$

$t_2 = 0{,}0852$

---

--- pág. 20 ---

**23/05** (segunda ~~hoja~~ / anotación al margen parcialmente ilegible)

> [FIGURA pág. 20]: Continuación del cuadro de la representación de la computadora, con los valores actualizados y sucesivamente tachados:
> - **Estado del sistema**: cajita $I$ con la sucesión de valores **17 → 14 → 10 → 7 → 27**; cajita $I^{+}$ con la misma sucesión **17 → 14 → 10 → 7 → 27**; cajitas $I^{-}$ (vacía / 0); cajitas fijas **15** ($s$) y **30** ($S$).
> - **"Reloj sim"**: cajita con la sucesión de valores tachados **0,1144 → 0,4738 → 0,5731 → 1,1347 → 1,8197**.
> - **Lista de eventos futuros**: *"Arribo pedido"* → **∞** (tachado) → **1,8197** (y **∞** anotado arriba); *"Arribo cliente"* → **0,1144** (tachado) → **0,4738** (tachado) → **0,5731** (tachado) → **1,1347** (tachado) → **1,9263**; *"fin de la sim"* → **120**; *"eval de inv"* → **1** (tachado) → **2**.
> - **Contadores estadísticos**: cajita $C_p$ → **0**; cajita $C_{p\,ac}$ → **0** (y **92**); cajita *"área bajo $I^{+}$"* → **0** → **1,6539** → **2,1503** → **7,1819** → **8,2742** → **12,5432** → **13,8899**; cajita *"área bajo $I^{-}$"* → **0**.

$\sim U(0,1)$

| $U$ |
|---|
| 0,9254 |
| 0,1146 |
| 0,2942 |
| 0,3557 |
| 0,9372 |
| 0,5207 |
| 0,4499 |
| 0,5244 |
| 0,802 |
| 0,2482 |
| 0,2871 |
| 0,6394 |
| 0,5379 _(parcialmente ilegible, escrito encima de otro número)_ |
| 0,1722 |
| 0,3333 |
| 0,7122 |
| 0,0333 |
| 0,5408 |

> [FIGURA pág. 20 — gráfico central]: Gráfico de $I(t)$ contra $t$ con línea horizontal violeta en $S = 30$ y línea de trazos en $s = 15$; sobre el eje vertical marcas en **19**, **17**, **14**, ... El trazo escalonado violeta va descendiendo con cada demanda; el área bajo la curva está rayada en rojo. Sobre el eje horizontal se marcan $t_1, t_2, t_3, t_4, t_5, t_6$ y el punto **1,8197**; un círculo azul marca el instante **①** rotulado *"(inventario)"* (evaluación de inventario). Llaves miden los tramos entre los $t_i$. Otra llave rotula los tramos **0,1347** y **0,687** cerca del final.

$T = -\lambda \ln U$

$T = -0{,}45 \ln(0{,}4499)$

&nbsp;&nbsp; $= 0{,}3594$

$t = 0{,}1144 + 0{,}3594 = 0{,}4738$

$T = -0{,}45 \ln(0{,}802)$

$T = 0{,}0993$

$t = 0{,}4738 + 0{,}0993 = 0{,}5731$

$T = -0{,}45 \cdot \ln(0{,}2871) = 0{,}5616$

$t = 0{,}5616 + 0{,}5731 = 1{,}1347$

$t_1 = 0{,}0349$ &nbsp;&nbsp;&nbsp; $t_2 = 0{,}0852$ &nbsp;&nbsp;&nbsp; $t_3 = 0{,}1144$ &nbsp;&nbsp;&nbsp; $t_4 = 0{,}4738$ &nbsp;&nbsp;&nbsp; $t_5 = 0{,}5731$ &nbsp;&nbsp;&nbsp; $t_6 = 1{,}1347$

$0{,}0292 \cdot 17 + 1{,}6539 = 2{,}1503$

$0{,}3594 \cdot 14 + 2{,}1503 = 7{,}1819$

$0{,}0993 \cdot 11 = 1{,}0923 + 7{,}1819 = 8{,}2742$

$0{,}4269 \cdot 10 = 4{,}269$

$4{,}269 + 8{,}2742 = 12{,}5432$

$0{,}1347 \cdot 10 = 1{,}347$

$+ \; 12{,}5432$

$\overline{\;13{,}8899\;}$

$$Z = \begin{cases} S - I & \text{si } I < s \\ 0 & \text{si } I \geq s \end{cases}$$

↳ este caso: $10 < 15$, hacemos pedido de $30 - 10 = 20$

Arribo pedidos $\sim U(0{,}5\,;\,1)$

---

--- pág. 21 ---

| | Simulacion (Teoria) | Hoja 11 |
|---|---|---|

Arribo pedido $\sim U(0{,}5\,;\,1)$

> [FIGURA pág. 21]: Gráfico de la densidad uniforme. Eje vertical con marcas en **1 = b** y **0,5 = a**; se dibuja el rectángulo/región de la distribución y, en diagonal, la recta de la función de distribución acumulada. Sobre el eje horizontal, marcas en **0**, **U** (con línea de trazos vertical) y **1**. Ilustra la transformación inversa para generar una $U(a,b)$.

$t = 1 + 0{,}8197 = 1{,}8197$

_(al margen: cuando va a arrancar el próx arribo)_

$$\boxed{\;Y = a + (b - a)\,U\;}$$

&nbsp;&nbsp;&nbsp; $= 0{,}5 + (0{,}5)(0{,}6394)$

&nbsp;&nbsp;&nbsp; $= 0{,}8197$

$T = -0{,}45 \cdot \ln(0{,}1722)$

$T = 0{,}7916$

$t = 0{,}7916 + 1{,}1347 = 1{,}9263$

$T = 0{,}685 \cdot 7 = 4{,}795$

$t = 4{,}795 + 13{,}8899 = 18{,}6849$

$C_p = k + i \cdot \underset{= 20}{Z} \;=\; 92$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓ &nbsp;&nbsp;&nbsp; ↓

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \$32 &nbsp;&nbsp; \$3

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↳ Datos dados

En el momento 2 &nbsp; $I \geq s$ &nbsp; ∴ no se hace pedido, ni se calcula arribo de pedido, pero se pone 3 en Eval inventario

$C_T = C_p + C_M + C_F$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↘

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $h\,\overline{I}^{\,+}$ &nbsp;&nbsp;&nbsp;&nbsp; $\pi\,\overline{I}^{\,-}$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \$5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \$1

_(el resto de la página está en blanco)_

---

--- pág. 22 ---

_(el encabezado de la hoja está en blanco; se trasluce la escritura del reverso)_

**1/07**

**Modelos de Colas** (pag 39 libro, después de los paros)

No vamos a ver la deducción de las formulas

CAP 13 — pag 39-61 — Modelos Analíticos de Colas

pag 62-68 — Deducción de las fórmulas (solo usaremos la fórmula)

Leer pag 39 completa

**§ 13.1 Características de un sist. de colas** &nbsp;&nbsp; _(al margen: 29 definiciones)_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↳ mirar los modelos para largos de colas (gráficos) (pag 40 y 42)

Población de Clientes: conjunto de todos los clientes posibles de un sist. de colas
&nbsp;&nbsp;&nbsp;&nbsp; **§ 13.1.1**

⎧ Proceso de llegada &nbsp; **§ 13.1.2**

⎪ Proceso de colas &nbsp; (~~Filas~~) **13.1.3**

⎨ Disciplina de cola (FIFO) **13.1.4**

⎪ Proceso de servicio **13.1.4**

⎩ Proceso de salida **13.1.5**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓

_Al margen derecho:_ Sistemas de cola de un paso: &nbsp;&nbsp; Ver definiciones en margen pag 40 &nbsp;&nbsp; Redes de colas

distribución de Poisson

&nbsp;&nbsp;&nbsp;&nbsp; $\lambda$ = tasa de arribos $= \dfrac{\text{n° de clientes}}{\text{unidad de tiempo}}$ &nbsp;&nbsp;&nbsp;&nbsp; Ej. $\lambda = \dfrac{4 \text{ clientes}}{\text{hora}}$

&nbsp;&nbsp;&nbsp;&nbsp; $\dfrac{1}{\lambda} = \dfrac{1}{4} = \dfrac{h}{c} = \dfrac{15 \text{ min}}{\text{cliente}} \;\rightarrow\;$ tiempos entre arribo promedio

&nbsp;&nbsp;&nbsp;&nbsp; $\mu$ = tasa de servicio

&nbsp;&nbsp;&nbsp;&nbsp; $\dfrac{1}{\mu} = \dots$ &nbsp; (se procede igual que tasa de arribos)

---

--- pág. 23 ---

| | Simulacion (Teoria) | Hoja 12 |
|---|---|---|

pag 43

**§ 13.1.5 Clasificación de los modelos de colas**

Notación de Kendall

$1 / 2 / 3 / 4 / 5 / 6$

$M / M / 1 / \_ / \_ / \_$ &nbsp;&nbsp; ← _por defecto_

_Flechas desde los últimos tres campos:_

- **Área de espera** — cuando ~~o~~ se pone es "infinita" (sin tope). Si no, se pone el área limitada.
- **Disciplina de cola** — si es FIFO no se pone nada.
- **Población o cantidad de clientes**, si se pone algo es porq hay un límite de cantidad, si no es "infinita".

> [ESQUEMA pág. 23 — Proceso de Llegada]: Árbol con dos ramas desde **"Proceso de Llegada"**: rama izquierda **"Aleatoria"**, rama derecha **"Determinístico D"**. De "Aleatoria" bajan a su vez dos ramas: **"Exponenc. M"** y **"otra dist. G"**.

**§ 13.2 Medidas de Rendimiento**

| notación del apunte de simulación | notación de colas |
|---|---|
| $\overline{d(n)}$ (demora promedio en cola) | $W_q$ &nbsp;&nbsp;&nbsp; $W$ |
| $q(n)$ = cant pers en cola | $L_q$ (long de la cola) &nbsp;&nbsp;&nbsp; $L$ |
| $\mu(n)$ | $U$ &nbsp;&nbsp;&nbsp; $P_W$ |

$W = W_q + \dfrac{1}{\mu}$ &nbsp;&nbsp; (1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $L_q = \lambda \cdot W_q$ &nbsp;&nbsp; (3)

$L = \lambda \cdot W$ &nbsp;&nbsp; (2)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Dato → siempre 2: $\lambda$, $\mu$

---

--- pág. 24 ---

**§ 13.3 Formulas para M/M/1**

**§ 13.4** &nbsp; " &nbsp;&nbsp; " &nbsp;&nbsp; **M/M/C**

pag 720 → gráfico → num de clientes y el tiempo de espera

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↳ dinámica de la cola ya alcanza un valor estable

Inicio = etapa transitoria = cola en formación

Estado Estable/Permanente → **ACÁ VALEN LAS FÓRMULAS**

"CONDICIÓN DE ESTADO ESTABLE" → $\dfrac{1}{\mu} < \dfrac{1}{\lambda}$

$\overset{rho}{\rho} = \dfrac{\lambda}{\mu} < 1$

pag 727 o 47

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Número de clientes en cola &nbsp; $L_q = \dfrac{\rho^{2}}{1 - \rho}$

Ver las formulas &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $P_n = \rho^{n} \cdot P_0$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $W = W_q + \dfrac{1}{\mu}$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $P_0 = 1 - \rho$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $P_W = 1 - P_0 = \rho$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $W_q = L_q \,/\, \lambda$

**§ 13.4 &nbsp; M/M/C**

&nbsp;&nbsp;&nbsp;&nbsp; Servidores idénticos

&nbsp;&nbsp;&nbsp;&nbsp; "cond de estado estable" &nbsp;&nbsp; $\dfrac{\lambda}{\mu \cdot C} < 1$

&nbsp;&nbsp;&nbsp;&nbsp; TABLA 13.2 pag 734 &nbsp;&nbsp;&nbsp;&nbsp; $L_q = \dfrac{\rho^{c+1}}{(c-1)!} \cdot \dfrac{1}{(c - \rho)^{2}} \cdot P_0$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _(no saber esto pero sí la tabla 13.1, aunque sí hay q saber cómo usarla si me la dan escrita.)_

&nbsp;&nbsp;&nbsp;&nbsp; leer hasta ~~pag~~ 736
