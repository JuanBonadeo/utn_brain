# IO — Resumen prioritario para el parcial

Fuentes usadas: `temario_confirmado_consulta.md` (consulta del profesor del 2026-09-30/10-01), `IO.md`, `banco-preguntas.md`, `machete-metodo-simplex.md`, `teoria-sensibilidad-dualidad.md` y la Unidad 7 ya volcada a la wiki.

El orden no sigue el programa: sigue la prioridad de examen. Primero va lo que el profesor marco como "tienen que saberlo" o "red flag si no"; despues lo que entra seguro; al final lo que conviene leer sin dedicarle la misma energia.

---

## 0. Mapa de estudio

### Prioridad 1 — dominar antes que nada

1. Simplex: condicion de factibilidad, condicion de optimizacion, lectura de `B^-1`.
2. Dualidad: armado del dual, teorema fundamental, holguras complementarias.
3. Sensibilidad: valores implicitos, cambios en `c_j`, cambios en `b_i`, costos reducidos.
4. Stock: formula general, modelo basico, periodo comun, restricciones con Lagrange.
5. Programacion entera: relajacion, branch and bound, por que no vale sensibilidad.

### Prioridad 2 — entra seguro

1. Transporte, transbordo y asignacion.
2. Redes: arbol de expansion minima, ruta mas corta, flujo maximo, costo minimo.
3. Conceptos basicos de PL: convexidad, SBF, degeneracion, teoremas sin demostracion.
4. Modelizacion y tipos de solucion.

### Prioridad 3 — leer, menor profundidad

1. Solucion conceptual por Cramer.
2. Periodo de tiempo fijo y clasificacion ABC.
3. Interpretacion economica del dual segun problema particular.

### No gastar tiempo

- Demostraciones de teoremas 2-5, 2-6, 2-7, 2-8.
- Demostracion del teorema fundamental de dualidad.
- Metodo de dos fases.
- Metodo de punto interior.
- Regla del 100% y cambios multiples.
- Analisis parametrico.
- Simplex dual.
- Procedimiento paso a paso de descuento por cantidad; si entra, importa el limite de `C(Q)`.

---

## 1. Simplex

### 1.1. Idea central

Simplex recorre soluciones basicas factibles. En cada iteracion hace dos preguntas:

```text
1. Optimizacion: ¿la solucion actual ya es optima? Si no, ¿quien entra?
2. Factibilidad: si esa variable entra, ¿cuanto puede crecer sin romper x >= 0?
```

Machete verbal:

```text
optimizacion mira la fila c_j - z_j
factibilidad mira la columna entrante
```

### 1.2. Condicion de factibilidad

Partimos de una base `B` y una variable no basica `x_j` que quiere entrar.

La columna de esa variable se expresa en coordenadas de la base:

```text
A_j = B Y_j
Y_j = B^-1 A_j
```

Si `Y_j = (y_1j, y_2j, ..., y_mj)^T` y hacemos entrar `x_j = theta_j`, las basicas cambian asi:

```text
x_i' = x_i - theta_j y_ij
x_j' = theta_j
```

Para seguir siendo factible:

```text
x_i' >= 0
x_i - theta_j y_ij >= 0
```

Si `y_ij > 0`, entonces:

```text
theta_j <= x_i / y_ij
```

Por eso:

```text
theta_j = min { x_i / y_ij : y_ij > 0 }
```

La variable que alcanza ese minimo sale de la base, porque queda exactamente en cero:

```text
x_r' = x_r - (x_r / y_rj) y_rj = 0
```

Reglas finas:

- Solo se divide por `y_ij > 0`.
- Si `y_ij <= 0`, esa fila no limita el crecimiento.
- `theta = 0` es valido: produce pivote degenerado.
- Si no hay ningun `y_ij > 0` y la columna mejora el funcional, la solucion es no acotada.

### 1.3. Condicion de optimizacion

El valor actual es:

```text
z_0 = sum c_i x_i
```

Si entra `x_j = theta_j`, las basicas quedan `x_i - theta_j y_ij` y aparece el aporte de la variable entrante:

```text
z = sum c_i (x_i - theta_j y_ij) + theta_j c_j
```

Distribuyendo:

```text
z = sum c_i x_i + theta_j (c_j - sum c_i y_ij)
```

Como:

```text
z_j = sum c_i y_ij
```

queda:

```text
z = z_0 + theta_j (c_j - z_j)
```

En maximizacion, como `theta_j >= 0`:

```text
c_j - z_j > 0   => mejora, conviene que entre
c_j - z_j = 0   => no mejora, pero puede haber optimo alternativo
c_j - z_j < 0   => empeora
```

Por lo tanto, en un problema de maximo:

```text
optimo <=> todos los c_j - z_j <= 0
entra   <=> el mayor c_j - z_j positivo
```

En minimo directo:

```text
optimo <=> todos los c_j - z_j >= 0
entra   <=> el mas negativo
```

### 1.4. Ficticias, holguras y penalizacion

Forma estandar:

```text
<=   + holgura                     puede ser base inicial
>=   - exceso + ficticia           entra la ficticia, no el exceso
=              ficticia            entra la ficticia
b<0  multiplicar toda la restriccion por -1 antes
```

La ficticia no representa nada real. Solo arma la identidad inicial.

Penalizacion:

```text
Max: ficticia con -M
Min: ficticia con +M
```

Razon: en maximizacion, `-M` vuelve malisimo dejarla positiva; en minimizacion, `+M` vuelve carisimo dejarla positiva.

### 1.5. Diagnosticos en tabla

| Caso | Senal |
|---|---|
| Optimo unico | Optimo y todas las no basicas tienen reducido estricto: `< 0` en Max, `> 0` en Min |
| Optimos multiples | Optimo y alguna no basica tiene `c_j - z_j = 0` |
| Degenerada | Alguna basica vale `0` |
| No acotada | Hay reducido que mejora, pero toda la columna entrante tiene `y_ij <= 0` |
| No factible | Ficticia basica positiva al terminar |

No mezclar:

```text
degenerada = una basica vale 0
multiples  = una no basica tiene reducido 0 en optimo
```

### 1.6. Donde esta `B^-1`

En la tabla final, el cuerpo de cada columna es:

```text
Y_j = B^-1 A_j
```

Si la base inicial era la de las holguras, entonces las columnas de esas holguras en la tabla final son directamente `B^-1`.

Si la base inicial uso ficticias, `B^-1` se lee debajo de las columnas que formaban la identidad inicial: holguras y ficticias, no necesariamente debajo de las basicas actuales.

Frase para acordarse:

```text
la base actual dice cual es B
la base inicial dice donde leer B^-1 en la tabla
```

---

## 2. Dualidad

### 2.1. Que es el dual

El primal decide cantidades de actividades. El dual valua recursos.

Si el primal pregunta:

```text
¿cuanto produzco?
```

el dual pregunta:

```text
¿cuanto vale cada recurso al margen?
```

### 2.2. Construccion del dual

Para un primal de maximizacion:

```text
Max z = c x
s.a. A x <= b
     x >= 0
```

el dual es:

```text
Min W = b^T u
s.a. A^T u >= c
     u >= 0
```

Reglas practicas para primal Max:

| En el primal | En el dual |
|---|---|
| Restriccion `<=` | Variable dual `u_i >= 0` |
| Restriccion `>=` | Variable dual `u_i <= 0` |
| Restriccion `=` | Variable dual libre |
| Variable `x_j >= 0` | Restriccion dual `>=` |
| Variable `x_j` libre | Restriccion dual `=` |

No hace falta convertir todas las restricciones a `<=`. Se puede armar directo respetando signos.

Chequeo obligatorio:

```text
W* = z*
```

Si no da igual, hay error de signo o de armado.

### 2.3. Teorema fundamental de la dualidad

Si el primal tiene solucion optima finita, entonces el dual tambien, y ambos tienen el mismo valor optimo:

```text
z* = W*
```

Ademas, los valores optimos de las variables duales son los costos marginales o valores implicitos de las restricciones del primal.

No piden demostracion, pero si enunciarlo bien.

### 2.4. Holguras complementarias

La propiedad:

```text
holgura primal_i * variable dual_i = 0
variable primal_j * holgura dual_j = 0
```

Lectura economica:

- Si sobra un recurso, su precio sombra vale cero.
- Si un recurso tiene precio sombra positivo, esta agotado.
- Si una actividad se realiza con nivel positivo, el valor de los recursos que consume iguala su contribucion.
- Si una restriccion dual queda con holgura positiva, esa actividad no se realiza.

Control rapido:

```text
en cada par primal-dual, al menos uno de los dos lados vale 0
```

### 2.5. Leer el dual desde la tabla

Para un primal Max con restricciones `<=`, los precios sombra se leen en la fila `c_j - z_j` bajo las holguras, cambiando el signo:

```text
u_i* = - (c_j - z_j) bajo la holgura de la restriccion i
```

Tambien:

```text
u = c_B B^-1
```

---

## 3. Sensibilidad

### 3.1. Idea clave

Sensibilidad pregunta que pasa si cambia un dato, sin resolver todo desde cero.

La tabla optima es:

```text
B^-1 aplicado a los datos originales
```

Por eso:

```text
tocar c_j  -> puede romper optimalidad
tocar b_i  -> puede romper factibilidad
```

### 3.2. Valores implicitos

Definicion correcta:

```text
valor implicito = cuanto cambia el valor optimo de la funcion objetivo ante un cambio unitario en el termino independiente de una restriccion
```

No definirlo solamente como "cuanto estoy dispuesto a pagar por una unidad mas de recurso". Eso es una consecuencia economica, no la definicion formal.

Si el recurso es escaso, el valor implicito suele ser positivo en maximizacion. Si sobra recurso, vale cero.

### 3.3. Cambio en `c_j`

Cambiar un coeficiente economico no cambia la factibilidad: las restricciones son las mismas.

#### Variable no basica

Solo cambia su reducido:

```text
c_k + Delta c_k - z_k <= 0
```

Si queda dentro del rango, no cambia ni `x*` ni `z*`, porque esa variable sigue valiendo cero.

#### Variable basica

Cambia `c_B`, por lo tanto cambian todos los reducidos. Se revisan todas las no basicas:

```text
(c_j - z_j)' = (c_j - z_j) - Delta c_k y_kj
```

En Max debe cumplirse:

```text
(c_j - z_j)' <= 0 para toda no basica
```

Dentro del rango, el plan `x*` no cambia, pero:

```text
z*' = z* + Delta c_k x_k*
```

### 3.4. Cambio en `b_i`

Cambiar un termino independiente no cambia los reducidos: la tabla sigue siendo optima. Lo que puede romperse es la factibilidad:

```text
x_B' = x_B + Delta b_i * columna i de B^-1
```

Hay que exigir:

```text
x_B' >= 0
```

Dentro del rango:

```text
z*' = z* + u_i Delta b_i
```

El valor implicito `u_i` vale solo dentro de ese rango.

### 3.5. Cambio tecnologico, variable nueva y restriccion nueva

Si cambia una columna de una variable no basica:

```text
Y_j = B^-1 A_j
z_j = c_B Y_j
c_j - z_j
```

Si `c_j - z_j <= 0` en Max, sigue sin entrar. Si `> 0`, conviene y hay que pivotear.

Nueva variable: misma cuenta; es una columna nueva.

Nueva restriccion: evaluar el optimo actual.

```text
si la cumple    -> no cambia nada
si no la cumple -> el optimo actual deja de ser factible y hay que reoptimizar
```

---

## 4. Stock

Stock es el tema con mas peso en el banco: 29 preguntas. La consulta confirmo que entra fuerte.

### 4.1. Conceptual

El stock es un desperdicio porque no agrega valor por si mismo, inmoviliza capital, ocupa espacio, requiere administracion y puede ocultar problemas de produccion.

Existe igual porque protege contra:

- aleatoriedad de la demanda;
- aleatoriedad de aprovisionamientos;
- tiempos de puesta a punto altos;
- paradas no programadas;
- falta de versatilidad de equipos o personal;
- fallas de calidad;
- ventajas de comprar o transportar por cantidad.

Objetivos de gestion:

```text
minimizar existencias
asegurar suministro
```

Estan en tension: los modelos buscan el equilibrio.

### 4.2. Formula general de costo

La consulta marco esto como base de todo stock:

```text
CT(Q) = [C(Q) Q + L + C(Q) i A(Q)] / Q = C(Q) + L/Q + C(Q) i A(Q)/Q
```

Version por unidad para modelo basico, con `C` constante:

```text
CT(Q) = C + L/Q + (C i Q)/(2D)
```

Componentes:

| Termino | Significado | Forma |
|---|---|---|
| `C` | costo unitario de compra/fabricacion | constante |
| `L/Q` | costo fijo de ordenar repartido por unidad | decrece con Q |
| `(C i Q)/(2D)` | costo de mantener stock | crece con Q |

Curva: recta horizontal + hiperbola decreciente + recta creciente. El minimo es unico.

Derivando:

```text
dCT/dQ = -L/Q^2 + C i/(2D) = 0
Q* = sqrt(2 D L / (C i))
```

Frase importante:

```text
para bajar el costo sin empeorar, hay que bajar L; no simplemente pedir menos
```

### 4.3. Punto de pedido

Sistema activado por la demanda. Se pide cuando el stock disponible llega al punto de pedido:

```text
PP = D * LT
```

Si hay incertidumbre:

```text
PP = demanda esperada durante LT + stock de seguridad
SS = z * desviacion durante LT
```

Demanda y `LT` siempre tienen que estar en la misma unidad de tiempo.

### 4.4. Consumo durante el ingreso

Aplica cuando el lote entra mientras tambien se consume. Ejemplo: produccion continua.

Con velocidad de ingreso `V` y demanda `D`:

```text
theta = Q / V
M = Q (1 - D/V)
```

El stock maximo no es `Q`, sino `M`, porque mientras entra tambien se consume.

El lote optimo:

```text
Q* = sqrt( 2 D L / (C i (1 - D/V)) )
```

Condicion necesaria:

```text
V > D
```

Si `V = D`, el lote optimo tiende a infinito; si `V < D`, el modelo no tiene sentido.

### 4.5. Periodo comun

Sistema activado por tiempo: varios articulos se piden juntos cada `T`.

Para cada articulo:

```text
Q_j = D_j T
```

Costo anual:

```text
CT(T) = C + L/T + (S/2) T
```

donde:

```text
C = sum C_j D_j
L = sum L_j
S = sum delta_j D_j
```

Minimo:

```text
T* = sqrt(2L/S)
Q_j* = D_j T*
```

Es la misma estructura que EOQ, pero la variable de decision es `T`.

### 4.6. Descuento por cantidad excedente

Si hasta `a` unidades se pagan a `C1` y el excedente a `C2 < C1`, para `Q > a`:

```text
C(Q) = [C1 a + C2 (Q-a)] / Q
     = C2 + [(C1-C2)a]/Q
```

Entonces:

```text
lim Q->infinito C(Q) = C2
```

Lectura: el precio medio se acerca a `C2` desde arriba, pero no lo alcanza para `Q` finito.

### 4.7. Restricciones con Lagrange

La mecanica se repite:

1. Calcular `Q_j*` sin restriccion (`lambda = 0`).
2. Ver si se supera el recurso disponible.
3. Si no se supera, la restriccion no es efectiva.
4. Si se supera, usar `lambda > 0` y ajustar hasta que la restriccion se cumpla con igualdad.

#### Restriccion de espacio

Restriccion:

```text
sum v_j Q_j <= E0
```

Resultado:

```text
Q_j* = sqrt( 2 D_j L_j / (C_j i + 2 lambda v_j) )
```

Interpretacion: los articulos voluminosos se penalizan mas. `lambda` es el costo marginal de no disponer de una unidad adicional de espacio.

Unidades:

```text
lambda = $ / (volumen * tiempo)
```

#### Restriccion de tiempo de preparacion

Restriccion:

```text
sum (D_j / Q_j) tau_j <= P0
```

Resultado:

```text
Q_j* = sqrt( 2 D_j (L_j + lambda tau_j) / [C_j i (1 - D_j/V_j)] )
```

Subir `lambda` agranda los lotes, porque lotes mas grandes implican menos preparaciones por periodo.

`lambda` es el costo marginal de no disponer de mas tiempo de preparacion.

#### Restriccion financiera

Interpretacion pedida:

```text
lambda = costo marginal de no disponer de mas dinero
i + lambda = tasa hasta la cual conviene aceptar dinero para invertir en stocks
```

Verificado contra el apunte (Masco-Torrent): con la restriccion `sum C_j Q_j / 2 <= I0` (inversion media) resulta `Q_j = sqrt(2 D_j L_j / (C_j (i + lambda)))`. El factor es `i + lambda`.

### 4.8. Riesgo de faltante

Stock de seguridad:

```text
SS = z * sigma_demanda_durante_LT
PP = demanda esperada durante LT + SS
```

Riesgo de faltante:

```text
RF = probabilidad de que la demanda durante LT exceda el punto de pedido
```

`RF 2%` no es lo mismo que `IPF 98%`:

- RF es probabilidad por ciclo.
- IPF es proporcion de demanda servida directamente desde stock.

En revision periodica, el periodo de incertidumbre es:

```text
T + LT
```

porque despues de revisar y pedir, hay que cubrir la demanda hasta la proxima revision mas el plazo de entrega.

---

## 5. Programacion entera y mixta

### 5.1. Tipos

- Entero puro: todas las variables son enteras.
- Entero mixto: algunas variables son enteras.
- Binario puro o mixto: variables restringidas a `0` o `1`, para decisiones si/no.

### 5.2. Relajacion

Relajar un programa entero es ignorar la condicion de integridad y resolverlo como PL.

Consecuencias:

- En maximizacion, el optimo del relajado es una cota superior del entero.
- En minimizacion, el optimo del relajado es una cota inferior del entero.
- Redondear el optimo relajado no garantiza factibilidad ni optimalidad.

Esto fue marcado como importante en la consulta.

### 5.3. Branch and Bound

Procedimiento:

1. Resolver el relajado.
2. Si la solucion es entera, terminar o actualizar mejor solucion.
3. Si hay variable fraccionaria, ramificar.
4. Si `x = 3,5`, crear ramas:

```text
x <= 3
x >= 4
```

5. Resolver cada subproblema relajado.
6. Podar un nodo si:
   - es infactible;
   - su relajado no puede mejorar la mejor solucion entera conocida;
   - su solucion ya es entera.

### 5.4. Sensibilidad en entera

No se puede usar precio sombra ni sensibilidad de LINDO para el programa entero.

Motivo:

```text
la interpretacion dual y de sensibilidad depende de convexidad y de moverse dentro de una base optima
```

En un problema entero el conjunto factible no es convexo: son puntos aislados. LINDO puede mostrar sensibilidad del relajado, pero no del entero final obtenido por ramificacion y poda.

---

## 6. Transporte, transbordo y asignacion

### 6.1. Transporte

Distribuir un producto homogeneo desde fuentes a destinos al minimo costo.

Variables:

```text
x_ij = unidades enviadas desde fuente i a destino j
```

Modelo general:

```text
Min W = sum_i sum_j c_ij x_ij
sum_j x_ij <= a_i     oferta
sum_i x_ij >= b_j     demanda
x_ij >= 0
```

Balanceado:

```text
sum ofertas = sum demandas
```

Si esta balanceado, las restricciones se escriben con igualdad.

### 6.2. Desbalanceo

| Caso | Se agrega | Interpretacion |
|---|---|---|
| Oferta > demanda | destino ficticio de costo 0 | capacidad ociosa |
| Demanda > oferta | fuente ficticia de costo 0 | demanda no satisfecha |

### 6.3. Integralidad automatica

Si ofertas y demandas son enteras, existe solucion optima entera. No hace falta declarar `x_ij` entera.

Esto conecta con entera: transporte parece entero, pero por su estructura no necesita programacion entera.

### 6.4. `m+n-1` y degeneracion

En transporte balanceado hay `m+n` ecuaciones, pero una es redundante. Por eso hay:

```text
m+n-1 restricciones independientes
```

Una solucion basica tiene a lo sumo `m+n-1` variables positivas.

Degenerada:

```text
menos de m+n-1 variables positivas
```

### 6.5. Asignacion

Caso particular de transporte:

```text
ofertas = 1
demandas = 1
```

Cada origen se asigna a un destino y cada destino recibe un origen.

Variable:

```text
x_ij = 1 si origen i se asigna a destino j
x_ij = 0 si no
```

Por integralidad automatica, puede bastar con `x_ij >= 0`; el modelo devuelve ceros y unos.

### 6.6. Transbordo

Hay nodos intermedios. La restriccion tipica de un nodo de transbordo es conservacion de flujo:

```text
lo que entra = lo que sale
```

Si el termino independiente es:

```text
0  -> nodo de paso puro
>0 -> nodo aporta flujo, actua como origen adicional
<0 -> nodo retiene flujo, actua como destino
```

Los algoritmos de transporte se pueden aplicar al transbordo si se formula balanceado.

---

## 7. Redes

Tema confirmado, pero con menor agresividad segun la consulta. Priorizar modelos y conceptos.

### 7.1. Definiciones

- Red o grafo: nodos unidos por arcos.
- Arco dirigido: permite flujo en un solo sentido.
- Trayectoria: sucesion de arcos que conectan nodos.
- Ciclo: trayectoria que empieza y termina en el mismo nodo.
- Red conexa: todo par de nodos esta conectado.
- Arbol: red conexa sin ciclos.
- Arbol de expansion: arbol que conecta todos los nodos; con `n` nodos tiene `n-1` arcos.

### 7.2. Arbol de expansion minima

Problema:

```text
conectar todos los nodos sin ciclos minimizando longitud/costo total
```

Prim:

1. Arrancar de un nodo.
2. Agregar el arco mas corto que conecte el arbol actual con un nodo no incluido.
3. Repetir hasta tener `n-1` arcos.

Kruskal:

1. Ordenar todos los arcos de menor a mayor.
2. Agregar cada arco si no forma ciclo.
3. Repetir hasta tener `n-1` arcos.

Si hay empate, puede haber multiples optimos.

### 7.3. Ruta mas corta

Problema:

```text
hallar el camino de menor costo/distancia/tiempo entre origen y destino
```

Dijkstra:

1. Etiquetar temporalmente vecinos del origen con distancia y nodo previo.
2. Fijar como permanente el temporal de menor distancia.
3. Reetiquetar vecinos si se mejora la distancia.
4. Repetir hasta fijar destino.
5. Reconstruir camino hacia atras usando nodo previo.

Modelo lineal:

```text
Min sum c_ij x_ij
conservacion de flujo por nodo
b_origen = 1
b_intermedio = 0
b_destino = -1
```

Se manda una unidad de flujo del origen al destino.

### 7.4. Flujo maximo

Red dirigida con capacidades maximas. Todo nace en una fuente y termina en un destino. En nodos intermedios:

```text
flujo que entra = flujo que sale
```

Objetivo:

```text
maximizar flujo total fuente -> destino
```

Modelo lineal:

```text
0 <= x_ij <= capacidad_ij
conservacion en nodos intermedios
maximizar flujo total
```

La consulta remarco entender que es un flujo continuo: agua, electricidad, autos por unidad de tiempo.

### 7.5. Flujo capacitado con costo minimo

Modelo mas general:

- fuentes con oferta;
- destinos con demanda;
- nodos de transbordo;
- arcos con capacidad;
- costo por unidad de flujo.

Objetivo:

```text
minimizar costo total respetando ofertas, demandas y capacidades
```

Transporte, transbordo, ruta mas corta y flujo maximo pueden verse como casos particulares.

---

## 8. Conceptos basicos de PL

### 8.1. Convexidad y puntos extremos

Conjunto convexo: si toma dos puntos del conjunto, todo el segmento que los une tambien pertenece al conjunto.

Punto extremo: punto que no puede escribirse como combinacion convexa de otros dos puntos distintos del conjunto.

La region factible de un PL es convexa porque es interseccion de semiespacios.

### 8.2. Soluciones basicas

En forma estandar:

```text
A x = b
x >= 0
```

Con `m` restricciones y `n` variables:

- Base: conjunto de `m` columnas linealmente independientes.
- Solucion basica: se fijan `n-m` variables en cero y se resuelve para las `m` basicas.
- SBF: solucion basica factible, o sea con todas las variables `>= 0`.
- Degenerada: una SBF con menos de `m` componentes estrictamente positivas; equivalentemente, alguna variable basica vale cero.

### 8.3. Teoremas que hay que saber enunciar

No entra la demostracion, si las conclusiones.

Idea practica:

```text
si un PL tiene optimo finito, hay al menos un punto extremo optimo
```

Por eso Simplex puede buscar entre SBF en vez de revisar infinitos puntos de la region factible.

---

## 9. Formato de respuesta de la catedra

Cuando pidan resolver, conviene cerrar asi:

```text
S* = (x1*; x2*; ...; xn*)^T
z* = ...
```

Luego interpretar:

- que variables de decision se producen o no;
- que holguras/excesos quedan;
- que restricciones son activas (`holgura/exceso = 0`);
- valor optimo con unidad.

Frases utiles:

```text
Es activa porque su holgura es cero.
La solucion es unica porque todos los reducidos de las no basicas son estrictos.
Hay optimos alternativos porque una no basica tiene c_j - z_j = 0 en la tabla optima.
Es degenerada porque una variable basica vale 0.
No es factible porque queda una ficticia basica positiva.
No es acotada porque mejora el funcional y no puede salir ninguna variable.
```

---

## 10. Checklist final a libro cerrado

Antes del parcial deberias poder desarrollar sin mirar:

- [ ] Condicion de factibilidad hasta `theta_j = min {x_i/y_ij}`.
- [ ] Condicion de optimizacion hasta `z = z_0 + theta_j(c_j-z_j)`.
- [ ] Donde leer `B^-1` en una tabla con holguras o ficticias.
- [ ] Armar el dual de un primal con `<=`, `>=` e `=`.
- [ ] Enunciar teorema fundamental de dualidad.
- [ ] Explicar holguras complementarias.
- [ ] Definir valor implicito correctamente.
- [ ] Hacer sensibilidad de `c_j`, `b_i`, variable nueva y restriccion nueva.
- [ ] Derivar `Q* = sqrt(2DL/(Ci))` del modelo basico de stock.
- [ ] Explicar periodo comun y obtener `T*`.
- [ ] Plantear Lagrange para espacio y tiempo de preparacion.
- [ ] Explicar relajacion y branch and bound.
- [ ] Decir por que no vale sensibilidad en programacion entera.
- [ ] Balancear transporte y explicar `m+n-1`.
- [ ] Diferenciar Prim, Kruskal, Dijkstra, flujo maximo y costo minimo.
