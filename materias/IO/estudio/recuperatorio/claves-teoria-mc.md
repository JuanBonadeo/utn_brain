# Claves de teoría para el multiple choice

> Armado a partir de las 95 preguntas del banco del simulacro (Gráfico, Conceptos básicos, Simplex, Sensibilidad, Dualidad, Transporte, Entera, Redes y Stock). Cada punto es una afirmación **correcta** tal como conviene recordarla, y al lado, **la trampa** con la que la presentan las opciones gemelas. Si sabés estas claves, reconocés la correcta aunque cambien la redacción.

**Cómo leer las opciones.** Casi siempre vienen de a pares casi idénticos: (a, b) y (c, d). Una de cada par cambia una sola palabra: "activa/cualquiera", "convexa/lineal", "≤/<", "mayor/menor", "necesariamente". Primero descartá el par que habla de otra cosa; después buscá la palabra que cambia. Si las dos de un par parecen correctas, mirá la e) "Ninguna de las anteriores".

## 1. Método gráfico y formas del modelo

- **Óptimos alternativos**: la función objetivo es paralela a una restricción **activa** en el óptimo, y el óptimo vale en **todo el segmento** entre los dos vértices. *Trampa: "paralela a alguna restricción" (puede ser una pasiva) o "perpendicular".*
- **RF no acotada ≠ solución no acotada.** Un Min con ≥ suele tener RF abierta y óptimo finito. La solución es no acotada sólo si la función mejora indefinidamente hacia donde se abre la región. *Trampa: "necesariamente no acotada".*
- **Restricción redundante**: geométrica, no toca la región. Analítica, toca un vértice y es combinación lineal de las que pasan por él. Si se la quita, la región **no cambia**. *Trampa: "si se la elimina, la región se agranda" (eso es una necesaria).*
- **Activa** (obligatoria) en el óptimo: se cumple con igualdad, holgura o exceso = 0. No asegura u ≠ 0. Lo seguro es al revés: **u ≠ 0 → activa**.
- **Forma estándar**: Max o Min, todas ecuaciones, todos los $b_i \geq 0$, todas las variables $\geq 0$. *Trampa: "debe ser de máximo", "todas ≤" (eso es la canónica de un Max), "b de cualquier signo".*
- **Para qué la forma estándar**: el simplex necesita ecuaciones y una base inicial $B = I$ que dé una SBF ($x_B = b \geq 0$).

## 2. Conceptos básicos

- **Teorema de equivalencia**: $x$ es punto extremo **si y sólo si** es una SBF. *Trampa: mezclarlo con "óptimo" o dejar sólo una implicación.*
- **El óptimo** se alcanza en al menos un punto extremo; si en más de uno, en toda **combinación lineal convexa** de ellos (coeficientes entre 0 y 1 que suman 1). *Trampa: "combinación lineal" a secas, o "exactamente un punto".*
- **Puntos extremos**: un convexo cualquiera puede tener infinitos (un círculo). Un PL tiene **a lo sumo** $C(n, m)$. *Trampa: "exactamente C(n, m)" o "n·m".*
- **Degenerada**: alguna básica vale 0, o sea, **menos de m** componentes positivas. *Trampa: "menos de n − m" (error de un material de circulación) o confundirla con "no básica con cⱼ − zⱼ = 0" (eso son alternativas).*
- **Conjuntos convexos**: el vacío, un punto, un semiespacio y un hiperplano lo son. La **intersección** de convexos es convexa (por eso la RF lo es); la **unión**, no.
- **Solución conceptual** (probar todas las bases): $C(n, m)$ crece **combinatoriamente** y es intratable. En PL no hay óptimos locales que no sean globales.
- **Por qué alcanza con finitos puntos**: el óptimo está en un extremo, cada extremo es una SBF, y las SBF son **a lo sumo** $C(n, m)$. La región no tiene por qué ser acotada.

## 3. Simplex

- **Ficticias**: se agregan en las restricciones **≥ y =** para tener $B = I$. No tienen significado y deben valer 0 si hay solución. *Trampa: "en ≤ y =", o confundirlas con el exceso.*
- **Gran M: MAX −M, MIN +M**, para que el simplex saque la ficticia.
- **Ficticia básica con valor 0 en el óptimo → óptimo degenerado. Con valor > 0 → no factible.** *Trampa: "no factible porque hay una ficticia en la base" (sólo si vale > 0); "M no fue suficientemente grande".*
- **Degeneración transitoria**: puede desaparecer. La final es degenerada sólo si en el óptimo queda una básica en 0. Se **origina** con un **empate en θ** (no en la entrada).
- **Coeficiente de sustitución**: $\partial x_i / \partial x_j = -y_{ij}$. Si $y_{ij} > 0$, la básica baja cuando entra $x_j$.
- **cⱼ − zⱼ = 0 en una no básica → alternativas, sólo si la tabla es óptima.** Toda básica tiene cⱼ − zⱼ = 0, así que eso no dice nada.
- **Efecto espejo**: columna del exceso = −(columna de su ficticia), y lo mismo sus $z_j$. Pasa en las ≥.
- **Salida**: $\theta = \min\{x_i / y_{ij} : y_{ij} > 0\}$. *Trampa: "$y_{ij} \neq 0$" o "máximo".*
- **Mejora**: $z' = z_0 + \theta_j\,(c_j - z_j)$. En Max es óptima con todos cⱼ − zⱼ ≤ 0 (en Min, ≥ 0).
- **No acotada (Max)**: existe cⱼ − zⱼ > 0 y **todos** los $y_{ij}$ de esa columna **≤ 0** (ceros incluidos). *Trampa: "< 0".*
- **Degenerada y entra con cⱼ − zⱼ > 0**: z puede **no cambiar** (θ = 0) y el método puede ciclar. Nunca empeora.
- **Una básica vale 1**: con ese dato solo no se puede decir que sea no degenerada (hace falta que todas sean > 0). Si el enunciado agrega que todas son positivas, la respuesta es "no degenerada".
- **Entrar con otro negativo (Min)**: igual se llega al óptimo. El más negativo da la mayor mejora **por unidad**, no la mayor mejora total ($\theta \cdot (c_j - z_j)$).
- **B⁻¹**: debajo de las columnas que **al inicio eran la identidad**. Si se borró una ficticia, sirve el exceso con el signo cambiado. *Trampa: "debajo de las básicas actuales" (ahí hay la identidad).*
- **Costo reducido en la óptima de un Max**: cuánto tendría que **aumentar** $c_j$ para que $x_j$ pueda entrar.
- **zⱼ** = lo que deja de aportar la reducción de las básicas al entrar una unidad de $x_j$ (costo de oportunidad).
- **Desempates (apunte)**: entrada, el de **menor** subíndice; salida, el de **mayor** subíndice.

## 4. Sensibilidad

- **Exceso = 0 en el óptimo**: la restricción es activa, se usa a pleno. No implica que su dual sea nulo. *Trampa: "se mejora aumentando su b" (subir el b de una ≥ la ajusta y nunca mejora).*
- **Signo del valor implícito**: Max ≤ → u ≥ 0 · Max ≥ → u ≤ 0 · Min ≤ → u ≤ 0 · Min ≥ → u ≥ 0 · = → libre. **Regla: aflojar nunca empeora, ajustar nunca mejora.**
- **Δb dentro del rango**: misma base, pero **cambian los valores** de las básicas ($x_B = x^* + r_k\,\Delta b_k$) y $z$ cambia en $u_k\,\Delta b_k$. *Trampa: "no cambian los valores" o "cambian los cⱼ − zⱼ".*
- **Δc de una NO básica (Max)**: sólo cambia su propio cⱼ − zⱼ. Sigue óptima mientras $\Delta c_k \leq -(c_k - z_k)$, y $z^*$ no cambia porque $x_k = 0$. *Trampa: el signo dado vuelta.*
- **Δc de una BÁSICA dentro del rango**: el **punto no cambia**, pero $z^*$ sí: $z^{*\prime} = z^* + \Delta c_k\, x_k^*$.
- **Cambiar c rompe la optimalidad (cⱼ − zⱼ); cambiar b rompe la factibilidad (x_B ≥ 0).** *Trampa: cruzados.*
- **Restricción nueva**: si la solución actual la cumple, no cambia nada. Si no, se agrega y se reoptimiza.
- **Actividad nueva (Max)**: conviene si $c_N - c_B B^{-1} A_N > 0$, o sea, si $c_N > \sum u_i\,a_{iN}$.
- **u = 20 \$/h**: z sube \$20 por hora adicional **mientras b esté en su rango**; conviene comprar si la hora cuesta **menos** de \$20.
- **Implicación segura**: valor implícito ≠ 0 → restricción activa. La recíproca falla.
- **Precio sombra**: lo máximo que conviene pagar por una unidad más del recurso. **Valor marginal**: lo que se deja de ganar por no disponerla. Es el mismo número con dos lecturas.

## 5. Dualidad

- **Primal con alternativas ↔ dual degenerado** (y al revés). **Primal no acotado → dual no factible.**
- **Primal no factible → dual no factible O no acotado.** No es "necesariamente" ninguno de los dos: la respuesta es "Ninguna de las anteriores".
- **Restricción = → variable dual libre. Variable libre → restricción dual =.**
- **Primal Max con una ≥ (sin multiplicar por −1) → u ≤ 0.** Si se la multiplica por −1, u ≥ 0 y su b entra con signo menos en el funcional dual.
- **Teorema fundamental**: si el primal tiene óptimo finito, el dual también, con $w^* = z^*$ y $u^* = c_B B^{-1}$. *Trampa: "$B^{-1}b$" (son las básicas del primal) o "costos reducidos".*
- **Holguras complementarias**: en cada par, al menos uno vale 0. Si sobra un recurso, su u = 0. Si un producto se fabrica, su restricción dual se cumple con igualdad. Que uno sea 0 **no** obliga al otro a ser positivo (pueden ser 0 los dos: degeneración).
- **Exceso de la restricción dual j** (primal Max): $-(c_j - z_j)$ de la columna de $x_j$. Los $z_j$ de las holguras dan los $u_i$.

## 6. Transporte, transbordo y asignación

- **Oferta > demanda** → destino ficticio, costo 0: lo que recibe es **capacidad ociosa**. **Demanda > oferta** → origen ficticio, costo 0: lo que manda es **demanda no satisfecha** (sin él, no hay solución factible).
- **m + n − 1**: una de las m + n restricciones es redundante; toda SBF tiene **a lo sumo m + n − 1 positivas**. *Trampa: confundir con las no básicas, que son m·n − (m + n − 1).*
- **Degenerada**: **menos** de m + n − 1 positivas.
- **Integralidad**: con ofertas y demandas enteras **existe** un óptimo entero, por la matriz de 0, 1 y −1. No hace falta programación entera. *Trampa: "todo óptimo es entero" (con alternativas puede haber fraccionarios) o que dependa de los costos.*
- **Transbordo** con (salidas − entradas) = b: b = 0, nodo de paso; b > 0, aporta flujo (origen); b < 0, retiene (destino). Si está escrito entradas − salidas, los signos se invierten.
- **Asignación**: transporte con ofertas y demandas = 1; alcanza con $x_{ij} \geq 0$ porque salen ceros y unos.
- **Estructura**: la mayoría de los coeficientes de A son 0 y el resto 1 o −1. Puede ser de máximo y tener = o ≥.
- **Transbordo con algoritmos de transporte**: sí, formulado como transporte balanceado. La cátedra lo resuelve con LINDO.

## 7. Programación entera

- **Relajado**: cota **superior** del óptimo entero en un Max, **inferior** en un Min.
- **Poda (Max)**: si el nodo es infactible, si ya es entero, o si su relajado da z **≤** la mejor entera encontrada.
- **Corte**: agregan restricciones que eliminan zonas sin enteros (fraccionario o mixto). **Búsqueda**: enumeran implícitamente; el principal es **ramificación y poda**.
- **Tipos**: puro (todas enteras), mixto (algunas), binario (0 o 1). Algunas enteras binarias y otras continuas: **binario mixto**.
- **LINDO en un entero**: los precios duales y rangos **no valen**: son del último relajado.
- **Redondear el relajado** no alcanza: puede quedar no factible o lejos del óptimo. *Trampa: "siempre no factible".*

## 8. Redes

- **Árbol de expansión**: conecta todos los nodos **sin ciclos**, con **n − 1 arcos**.
- **Prim**: arranca de un nodo y agrega el arco más corto que conecte el árbol con un nodo nuevo. **Kruskal**: ordena todos los arcos y agrega el más corto que no forme ciclo. Los dos dan el árbol mínimo. (Algunos materiales llaman Kruskal a Prim.)
- **Dijkstra**: se hace **permanente la etiqueta temporal de menor distancia** y se reetiquetan sus vecinos. Etiquetas [distancia, previo].
- **Ruta más corta como PL** (salidas − entradas = b): b = **1 en el origen, −1 en el destino, 0** en los intermedios.
- **Flujo máximo**: en cada trayectoria se manda la **menor** capacidad residual; se resta en el sentido del flujo y se **suma en el inverso**.
- **Flujo con costo mínimo**: el modelo general; transporte, ruta más corta y flujo máximo son casos particulares.

## 9. Stock

- **Tasa i**: capital inmovilizado, espacio, personal, riesgos, administración e impuestos (lo que depende del stock). L va aparte.
- **En Q\***: costo de ordenar = costo de mantener.
- **Reducir stock sin subir el costo**: **bajar L** (SMED). Subir i o achicar Q a la fuerza encarece.
- **Consumo durante el ingreso**: debe ser **D < V**; el lote es **mayor** que el básico; si V → D, Q\* → ∞. El LT del PP incluye sólo **organización y puesta a punto**, no la fabricación.
- **Excedente**: $C(Q) = C_2 + (C_1 - C_2)\,a/Q$; tiende a $C_2$ **sin alcanzarlo** y es **continuo** en a. Con L = 0 y mínimo de compra: el tramo sin descuento es una recta creciente (mínimo en la compra mínima) y el tramo con descuento tiene mínimo interior, porque k actúa como L.
- **Crédito (capital)**: conviene si la tasa **< i + λ** (el apunte: i₁ + λ). λ es el costo marginal de no tener más capital.
- **Unidad de λ**: capital, 1/tiempo (una tasa); espacio, \$/(volumen·tiempo); preparación, \$/hora.
- **Al subir λ**: con espacio los lotes se **achican**; con preparación se **agrandan** (menos preparaciones).
- **Qué mide cada restricción**: espacio, la existencia **máxima** $v_j Q_j$; capital, la inversión **media** $C_j Q_j / 2$.
- **Primer paso con Lagrange**: Q\* sin restricción (λ = 0) y ver si entra. Si entra, la restricción no es efectiva.
- **RF ≠ IPF**: el RF es la probabilidad de faltante **por ciclo**; el IPF, la fracción de demanda entregada desde el stock. Con RF = 2 %, el IPF suele ser mayor que 98 %.
- **Por qué la normal**: si la demanda es normal, la del LT también (**propiedad reproductiva**); si no, se aproxima (**teorema central del límite**).
- **Desvío en el LT**: $\sigma_d \sqrt{LT}$ (varianzas que se suman). Con σ = 10 y LT = 9: **30**, no 90.
- **Revisión periódica**: el período de riesgo es **T + LT**; $SS = z\,\sigma\,\sqrt{T + LT}$.
- **PP contra RP**: PP lo activa la **demanda**, Q fijo, registro permanente. RP lo activa el **tiempo**, cantidad variable, se mira sólo al revisar, y lleva **más** SS.
- **ABC**: por costo anual C·D acumulado. A hasta 75 %, B hasta 95 %, C el resto; los **C** van con revisión periódica.
- **Período común**: $T^* = \sqrt{2L/S}$, con L de toda la orden conjunta y $S = \sum \delta_j D_j$; $Q_j = D_j T^*$.
- **Stock como desperdicio**: no agrega valor, oculta problemas e inmoviliza capital; existe porque casi nunca se puede eliminar: **desperdicio inevitable**.
- **Reducir existencias**: achicar lotes y plazos, **previa mejora continua** que ataque las causas.
- **Objetivos de la gestión**: reducir los niveles al mínimo **y** asegurar el suministro en el momento adecuado.
