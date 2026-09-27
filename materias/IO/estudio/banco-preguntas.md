# IO — Banco de preguntas de teoría

**Para el parcial del 2026-10-03.** Origen: `fuentes/preguntas-frecuentes.pdf` (20 pág.),
material de circulación entre alumnos bajado el 2026-09-27. **89 preguntas** agrupadas en
diez temas.

> **Advertencia de confiabilidad.** Este banco **no es material oficial de cátedra** y sus
> respuestas no están verificadas. En el material de IO que ya auditamos aparecieron seis
> errores, tres de ellos **en la resolución oficial** de la Práctica 3. En este PDF ya
> detectamos cinco: están en la **Parte 2**. Regla: donde este banco y el apunte
> (`fuentes/Material de cursado (2023)/Teoría/PLC*.pdf`) no coincidan, **gana el apunte**.

## Cómo usar esto

1. **Parte 1** es el checklist para autoevaluarte a libro cerrado. Cada pregunta tiene un
   código (`SPX-04`) y una marca de estado.
2. Las marcadas **✔** ya están respondidas y verificadas en [[IO]] (Unidades 1 a 5). La
   **Parte 7** te dice a qué unidad ir para cada una.
3. Las marcadas **⚠** son las de las unidades todavía vacías. Su respuesta está en las
   **Partes 3 a 6** de este archivo, transcripta y limpiada del PDF, pero **todavía sin
   cruzar contra el apunte**.
4. **Parte 2** son los errores del material. Leela antes de estudiar, no después.

## Reparto de las 89 preguntas

| Tema | Código | Preg. | Estado |
|---|---|---:|---|
| Método gráfico | `GRA` | 1 | ✔ Unidad 1 |
| Formas de presentación | `FOR` | 2 | ✔ Unidad 1 |
| Conceptos básicos | `CBA` | 6 | ✔ Unidad 2 |
| Método Simplex | `SPX` | 17 | ✔ Unidad 3 |
| Análisis de sensibilidad | `SEN` | 7 | ✔ Unidad 4 |
| Dualidad | `DUA` | 4 | ✔ Unidad 5 |
| **Subtotal ya cubierto** | | **37** | **42 %** |
| Transporte, trasbordo y asignación | `TTA` | 11 | ⚠ Unidad 7 vacía |
| Programación entera y mixta | `ENT` | 4 | ⚠ Unidad 8 vacía |
| Modelos de redes | `RED` | 8 | ⚠ Unidad 9 vacía |
| Gestión de stock | `STK` | 29 | ⚠ Unidad 11 vacía |
| **Subtotal por estudiar** | | **52** | **58 %** |

**Stock sola es un tercio del total** (29 de 89) y es el último tema que se dio en clase.
**Redes no se dio en clase**, aunque presuntamente entra. **CPM/PERT no se dio y no aparece
en este banco**: presuntamente fuera de alcance.

---

# Parte 1 — Checklist de las 89 preguntas

## Método gráfico

- [ ] `GRA-01` ✔ Explicar los tipos de soluciones de un PL.

## Formas de presentación del modelo

- [ ] `FOR-01` ✔ ¿Para qué se usa la forma estándar en la PL? Características.
- [ ] `FOR-02` ✔ ¿Qué son las restricciones activas y cómo identificarlas? Describa los tipos de restricciones redundantes.

## Conceptos básicos

- [ ] `CBA-01` ✔ Enuncie los tres teoremas fundamentales de la programación lineal.
- [ ] `CBA-02` ✔ Definición de conjunto convexo y punto extremo.
- [ ] `CBA-03` ✔ Si alguna variable básica toma el valor cero, ¿ante qué tipo de solución nos encontramos? **(ojo: ver E-2)**
- [ ] `CBA-04` ✔ ¿Cuál es la máxima cantidad de puntos extremos que puede tener un conjunto convexo? ¿Y el conjunto de soluciones factibles de un PL?
- [ ] `CBA-05` ✔ ¿Qué inconveniente presenta la solución conceptual del problema de PL?
- [ ] `CBA-06` ✔ ¿Por qué, aun habiendo infinitos puntos en la región factible, basta considerar un número finito de ellos?

## Método Simplex

- [ ] `SPX-01` ✔ ¿Qué son las variables ficticias y para qué sirven? Explicar el método de penalización.
- [ ] `SPX-02` ✔ ¿Cuándo un problema es degenerado? Si cae en degeneración, ¿la solución será siempre degenerada? **(ojo: ver E-1)**
- [ ] `SPX-03` ✔ Desarrollo analítico del método Simplex. **(el PDF dice "hecho en hoja")**
- [ ] `SPX-04` ✔ Demostración de la condición de factibilidad. **(ídem; la desarrolla `SPX-11`)**
- [ ] `SPX-05` ✔ Demostrar la condición de optimización a partir del desarrollo analítico. **(ídem; la desarrolla `SPX-12`)**
- [ ] `SPX-06` ✔ ¿Qué es un coeficiente de sustitución y qué representa?
- [ ] `SPX-07` ✔ Si se estaba en condición de óptimo y para algún $c_j-z_j$ la diferencia es nula, ¿qué solución se obtenía?
- [ ] `SPX-08` ✔ ¿Qué es el efecto espejo? ¿Cuándo se produce y para qué sirve?
- [ ] `SPX-09` ✔ ¿Qué pasa si una variable ficticia integra la solución óptima?
- [ ] `SPX-10` ✔ ¿Qué son los costos reducidos? ¿Qué información dan para una variable no básica?
- [ ] `SPX-11` ✔ ¿En qué consiste la condición de factibilidad? Desarrolle analíticamente.
- [ ] `SPX-12` ✔ ¿En qué consiste la condición de optimización? Desarrolle analíticamente.
- [ ] `SPX-13` ✔ La solución es degenerada y debe ingresar $A_j$ con al menos un $y_{ij}>0$: justifique por qué podrá tenerse o no incremento en $z$.
- [ ] `SPX-14` ✔ Si en la tabla de óptimo hay una básica que asume el valor uno, ¿qué tipo de solución tiene el problema? **(ojo: ver E-3)**
- [ ] `SPX-15` ✔ En minimización, ¿qué pasa si en lugar del $c_j-z_j$ más negativo hacemos entrar otro negativo de mayor valor?
- [ ] `SPX-16` ✔ ¿Cómo se detecta que un PL tiene solución no acotada, en Simplex y en el método gráfico?
- [ ] `SPX-17` ✔ ¿Dónde encontrar $B^{-1}$ en la tabla de la solución óptima?

## Análisis de sensibilidad

- [ ] `SEN-01` ✔ Si se desea añadir una nueva restricción al problema ya óptimo, ¿cómo procedería?
- [ ] `SEN-02` ✔ *(multiple choice)* Si una variable de exceso vale cero en el óptimo: a) el recurso se usa a pleno; b) la dual es nula; c) se puede mejorar subiendo el lado derecho; d) ninguna. → **a)**
- [ ] `SEN-03` ✔ ¿De qué depende el signo de los valores implícitos?
- [ ] `SEN-04` ✔ Desarrolle analíticamente la sensibilidad ante un cambio en el término independiente.
- [ ] `SEN-05` ✔ ¿Para qué se usan los valores implícitos? Defina valor implícito; ¿cuándo se comporta como precio sombra y cuándo como valor marginal?
- [ ] `SEN-06` ✔ Desarrolle el cambio en un coeficiente económico una vez obtenido el óptimo.
- [ ] `SEN-07` ✔ Desarrollar el agregado de una nueva variable.

## Dualidad

- [ ] `DUA-01` ✔ Enuncie el teorema dual de la PL.
- [ ] `DUA-02` ✔ Si un PL tiene solución alternativa o no acotada, ¿qué ocurre con el otro problema? Justifique.
- [ ] `DUA-03` ✔ Describa el concepto de holguras complementarias y dé un ejemplo.
- [ ] `DUA-04` ✔ Al construir el dual, ¿qué consideraciones aplican si el primal tiene restricciones de igualdad?

## Transporte, trasbordo y asignación

- [ ] `TTA-01` ⚠ Defina el problema de transporte y el problema de trasbordo.
- [ ] `TTA-02` ⚠ Describir el problema de asignación.
- [ ] `TTA-03` ⚠ ¿Qué particularidad tienen los problemas de transporte, trasbordo y asignación?
- [ ] `TTA-04` ⚠ Si las capacidades y demandas son enteras, ¿la solución también será entera?
- [ ] `TTA-05` ⚠ ¿Qué sucede si la oferta total excede a la demanda total?
- [ ] `TTA-06` ⚠ ¿Qué sucede si la demanda total excede a la oferta total?
- [ ] `TTA-07` ⚠ ¿Cuándo una solución de transporte es degenerada?
- [ ] `TTA-08` ⚠ ¿Pueden aplicarse los algoritmos de transporte a los problemas de trasbordo?
- [ ] `TTA-09` ⚠ ¿Qué significa que un modelo de transporte esté balanceado? En fórmulas, con ejemplo.
- [ ] `TTA-10` ⚠ ¿Por qué una solución básica de un modelo balanceado tiene a lo sumo $m+n-1$ variables positivas?
- [ ] `TTA-11` ⚠ En un trasbordo, ¿qué representan las ecuaciones con término independiente $=0$? ¿Y si ese término fuera distinto de cero?

## Programación entera y mixta

- [ ] `ENT-01` ⚠ Tipos de modelos de PL con enteros.
- [ ] `ENT-02` ⚠ ¿Qué métodos para resolver problemas enteros y mixtos existen?
- [ ] `ENT-03` ⚠ Describir el criterio que usa el algoritmo de ramificación y poda.
- [ ] `ENT-04` ⚠ Programa lineal relajado: ¿qué es y para qué se usa?
- [ ] `ENT-05` ⚠ *(no está entre las 89; sale del resumen y es trampa clásica)* ¿Por qué no es válido usar el análisis de sensibilidad que reporta LINDO en un programa entero?

## Modelos de redes

- [ ] `RED-01` ⚠ ¿Dónde se utilizan los modelos de redes?
- [ ] `RED-02` ⚠ Definir red, ciclo, árbol y árbol de expansión mínima.
- [ ] `RED-03` ⚠ ¿Cuál es el problema en el árbol de expansión mínima, en el de ruta más corta y en el de flujo máximo?
- [ ] `RED-04` ⚠ Describa el algoritmo del árbol de expansión mínima y dé ejemplos de uso. **(ojo: ver E-4)**
- [ ] `RED-05` ⚠ Describa el problema de la ruta más corta y el algoritmo que lo resuelve.
- [ ] `RED-06` ⚠ Desarrollar el problema de flujo máximo.
- [ ] `RED-07` ⚠ ¿Cómo se resuelve el problema del flujo máximo?
- [ ] `RED-08` ⚠ Características del problema de flujo capacitado con costo mínimo.

## Gestión de stock

- [ ] `STK-01` ⚠ ¿Cómo calculan las empresas sus tasas de mantenimiento de stock? Enuncie los costos generales con ejemplos.
- [ ] `STK-02` ⚠ ¿Por qué el stock se considera un desperdicio? Si lo es, ¿por qué existe igual?
- [ ] `STK-03` ⚠ Problemas que causan stock y herramientas para solventarlos.
- [ ] `STK-04` ⚠ Diferencia entre modelo de punto de pedido y período común.
- [ ] `STK-05` ⚠ ¿Cómo se compone la curva de costo directo total mínimo? Graficar.
- [ ] `STK-06` ⚠ Desarrolle el modelo con consumo durante el ingreso.
- [ ] `STK-07` ⚠ ¿Un RF 2 % es lo mismo que un IPF 98 %? Justifique.
- [ ] `STK-08` ⚠ En un modelo con restricción de espacio, ¿en qué unidades se expresa $\lambda$?
- [ ] `STK-09` ⚠ Enuncie la clasificación ABC. ¿Qué gestión se usa para los artículos de bajo costo?
- [ ] `STK-10` ⚠ ¿Cuáles son los principales objetivos de la gestión de existencias?
- [ ] `STK-11` ⚠ Principales causas generadoras de stock.
- [ ] `STK-12` ⚠ ¿Qué beneficios tiene hacer una inversión en stocks?
- [ ] `STK-13` ⚠ ¿Cómo se logra la reducción de existencias?
- [ ] `STK-14` ⚠ Componentes de la función de costo unitario en el momento de la utilización. ¿Cómo se determina el costo mínimo? Con gráfico.
- [ ] `STK-15` ⚠ ¿Cómo puedo reducir los costos $CT(Q)$?
- [ ] `STK-16` ⚠ En consumo durante el ingreso, ¿cómo debe ser la relación entre velocidad de ingreso y demanda? Justifique con fórmulas.
- [ ] `STK-17` ⚠ Descuento por cantidad excedente con valor mínimo de compra y $L$ nulo: ¿qué cambia?
- [ ] `STK-18` ⚠ Interpretación económica de $\lambda$ en el modelo de restricción financiera. ¿Y de $i+\lambda$?
- [ ] `STK-19` ⚠ Interpretación económica de $\lambda$ en el modelo de restricción de almacenamiento.
- [ ] `STK-20` ⚠ Interpretación económica de $\lambda$ en el modelo de restricción de tiempo de preparación.
- [ ] `STK-21` ⚠ ¿Qué es el stock de seguridad (SS)?
- [ ] `STK-22` ⚠ ¿Qué es el riesgo de faltante (RF)?
- [ ] `STK-23` ⚠ ¿Por qué la tabla de RF es la misma que la de la normal estándar?
- [ ] `STK-24` ⚠ ¿Por qué en revisión periódica la demanda se estudia durante $T+LT$?
- [ ] `STK-25` ⚠ Diferencias entre punto de pedido con RF especificado y revisión periódica con RF especificado.
- [ ] `STK-26` ⚠ Grafique el costo total del modelo de período común para un conjunto de artículos y explique cada parte.
- [ ] `STK-27` ⚠ En descuento por cantidad excedente, demuestre el límite de $C(Q)$ cuando $Q\to\infty$.
- [ ] `STK-28` ⚠ Halle el mínimo del modelo con restricción de tiempo de preparación, por multiplicadores de Lagrange.
- [ ] `STK-29` ⚠ Halle el mínimo del modelo con restricción de espacio de almacenamiento, por multiplicadores de Lagrange.

---

# Parte 2 — Errores y trampas detectados en el material

Cinco cosas mal o imprecisas en `preguntas-frecuentes.pdf`. Estudiar la versión corregida,
no la del PDF.

### E-1 — `SPX-02`: la definición de degeneración está dada vuelta

**El PDF dice:** *"un PL es degenerado cuando al aplicar la condición de factibilidad existen
dos o más vectores columna $A_j$ no básicos que poseen el mismo valor $\theta_j$"*.

**Está mal:** confunde columnas con filas. El empate que produce degeneración se da en la
**prueba del cociente mínimo**, entre **filas** — es decir, entre dos o más variables
**básicas** que alcanzan el mismo $\theta$ mínimo, lo que define cuál **sale** de la base. Al
salir una, la otra queda básica con valor cero: eso es la SBF degenerada.

**Lo correcto:** una SBF es **degenerada** cuando alguna variable **básica** vale cero. En la
tabla se detecta porque el mínimo de $\theta = \min_i \{x_i/y_{ij} : y_{ij}>0\}$ se alcanza en
**dos o más filas**.

> Ya está bien escrito en la Unidad 3 de [[IO]]: *"Degenerada = una variable **básica** vale 0.
> Alternativas = una **no básica** tiene $c_j-z_j=0$. Son cosas distintas y pueden darse
> juntas."*

La segunda mitad de la pregunta sí está bien: caer en degeneración **no** condena a que la
solución final sea degenerada. Se puede salir del estado degenerado en una iteración
posterior, o llegar al óptimo con todas las básicas positivas.

### E-2 — `CBA-03`: dice $n-m$ donde va $m$

**El PDF dice:** *"si una variable básica toma el valor cero, la solución posee menos de
$n-m$ componentes estrictamente positivas"*.

**Está mal**, y el propio PDF se contradice en `DUA-02`, donde escribe correctamente *"menos
de $m$ componentes estrictamente positivas"*. Una base tiene $m$ variables básicas, una por
restricción. Degenerada = **menos de $m$** componentes estrictamente positivas.

### E-3 — `SPX-14`: la justificación no se sostiene

La pregunta da que **una** básica vale 1, y el PDF concluye "no degenerada" argumentando *"si
**todas** las básicas tienen valores positivos, la solución es no degenerada"*. Es un salto
lógico: saber que **una** vale 1 no dice nada de las otras.

**Respuesta defendible:** que esa variable valga 1 (≠ 0) implica únicamente que **esa** no
causa degeneración. Para afirmar que la solución es no degenerada hacen falta **las $m$**
básicas estrictamente positivas. Con el dato de una sola variable **no se puede concluir**,
salvo que el enunciado agregue que las demás son positivas.

### E-4 — `RED-04`: el algoritmo descripto es Prim, no Kruskal

**El PDF lo llama Kruskal** y describe: *"arrancar de un nodo cualquiera; en cada paso agregar
el arco más corto que conecte el árbol actual con algún nodo todavía no incluido"*.

Ese es **Prim**: mantiene **un solo árbol conexo** que crece desde un nodo inicial.
**Kruskal** ordena **todos** los arcos de menor a mayor y va agregando el más corto que no
forme ciclo, sin importar la conexidad — durante la ejecución hay **varios fragmentos
sueltos** que recién al final se unen.

Los dos dan un árbol de expansión mínima válido y el resultado numérico coincide, pero si el
parcial pide "describa Kruskal", lo del PDF no es eso. **Pendiente: verificar qué nombre usa
la cátedra en `fuentes/Material de cursado (2023)/Teoría/REDESUTN_2016.pdf`.**

### E-5 — `SPX-03`, `SPX-04`, `SPX-05`: sin respuesta en el PDF

Las tres dicen literalmente *"Hecho en hoja"*: el autor las resolvió a mano y no las
transcribió. No son un hueco real:

- `SPX-04` (condición de factibilidad) está desarrollada en `SPX-11`.
- `SPX-05` (condición de optimización) está desarrollada en `SPX-12`.
- `SPX-03` (desarrollo analítico completo) está en la **Unidad 3** de [[IO]] y en
  [[machete-metodo-simplex]].

---

# Parte 3 — Transporte, trasbordo y asignación (11)

> Transcripto y limpiado de `fuentes/preguntas-frecuentes.pdf`. **Sin cruzar todavía** contra
> `Teoría/Modelos especiales de PL.pdf` ni `PLC7.pdf`.

### `TTA-01` — Defina el problema de transporte y el de trasbordo

**Transporte:** se interesa, literalmente o de manera figurada, en la distribución de un
producto **homogéneo** desde un grupo de centros de suministro (**fuentes**) hacia un grupo de
centros receptores (**destinos**), de manera tal que se **minimicen los costos de
distribución**.

**Trasbordo:** distribución de un producto de distintos orígenes a distintos destinos, pero
con la posibilidad de pasar por un **centro intermedio de trasbordo**. Es una extensión del
problema de transporte con el agregado de puntos intermedios que reciben mercadería y la
envían a destino.

### `TTA-02` — Describir el problema de asignación

Consiste en relacionar un conjunto de ofertas a un conjunto de demandas con relación **uno a
uno**; a cada pareja se le asigna un costo asociado (por ejemplo, el costo en tiempo de una
máquina particular para hacer determinado trabajo). El objetivo es **minimizar el costo
total**. Los casos especiales son iguales a los del transporte y se balancean de la misma
manera.

### `TTA-03` — Qué particularidad tienen los tres

Presentan una **estructura muy particular en la matriz $A$**: la mayor parte de los
coeficientes son **cero**, y el resto son **$1$ o $-1$**.

### `TTA-04` — Si capacidades y demandas son enteras, ¿la solución también?

**Sí.** En muchas aplicaciones se requiere que las variables sean enteras, lo que obligaría a
usar algoritmos de programación entera — mucho más lentos que Simplex. Pero **dada la
estructura especial de $A$** (valores $0$, $1$ o $-1$), si todos los $a_i$ (capacidades) y
$b_j$ (requerimientos) son enteros y el problema tiene solución factible, **siempre tendrá una
solución óptima con valores enteros**. Por eso **es innecesario agregar la restricción de
integridad**.

> Esta es la propiedad que hace que transporte **no** sea un problema de programación entera
> aunque la respuesta tenga que ser entera. Vale la pena tenerla lista: conecta la Unidad 7
> con la Unidad 8.

### `TTA-05` — ¿Y si la oferta total excede la demanda total?

Se **balancea** creando un **destino ficticio** con demanda igual al excedente de oferta. Los
envíos hacia él no son reales, así que se les asigna **costo cero**. En el óptimo, los envíos
al destino ficticio indican la **capacidad ociosa de la oferta**.

### `TTA-06` — ¿Y si la demanda total excede la oferta total?

El problema **no tiene solución factible** tal cual está planteado. Si igual interesa abastecer
toda la demanda posible al mínimo costo, se reajusta agregando un **origen ficticio** con
oferta igual al excedente de demanda y costo cero hacia cualquier destino. En el óptimo, la
oferta asignada desde el origen ficticio se interpreta como **demanda no satisfecha**.

### `TTA-07` — ¿Cuándo una solución de transporte es degenerada?

Cualquier solución básica de un modelo **balanceado** con $m$ orígenes y $n$ destinos tiene a
lo sumo $m+n-1$ variables positivas. Si hay **menos de $m+n-1$** variables positivas, la
solución es **degenerada**.

### `TTA-08` — ¿Se aplican los algoritmos de transporte al trasbordo?

**Sí.** Requieren formular un **modelo balanceado**, incorporando fuentes o destinos ficticios
según haga falta.

### `TTA-09` — ¿Qué significa que el modelo esté balanceado?

Con $m$ fuentes de oferta $a_i$, $n$ destinos de demanda $b_j$ y $x_{ij}$ las unidades enviadas
de $i$ a $j$, hay dos tipos de restricciones:

$$\sum_j x_{ij} \leq a_i \quad \text{(no enviar más que la capacidad)}$$
$$\sum_i x_{ij} \geq b_j \quad \text{(no enviar menos que el requerimiento)}$$

El modelo está **balanceado** cuando $\sum_i a_i = \sum_j b_j$. En ese caso **ambos tipos de
restricción se cumplen con igualdad**.

**Ejemplo.** Fuentes $F_1$ (capacidad 30) y $F_2$ (capacidad 20); destinos $D_1$ (demanda 25) y
$D_2$ (demanda 25). Oferta total $=50$, demanda total $=50$: coinciden, el modelo está
balanceado y no hace falta agregar nada ficticio.

### `TTA-10` — ¿Por qué a lo sumo $m+n-1$ variables positivas?

En un modelo balanceado con $m$ orígenes y $n$ destinos hay $m+n$ restricciones, **pero una es
redundante**, porque la suma de las ofertas es igual a la suma de las demandas (conociendo
$m+n-1$ ecuaciones, la restante queda determinada). Entonces hay solo **$m+n-1$ restricciones
linealmente independientes**. Como en una solución básica el número máximo de variables
positivas es igual al número de restricciones independientes, toda SBF tiene **a lo sumo
$m+n-1$** variables positivas.

### `TTA-11` — En un trasbordo, ¿qué representan las ecuaciones con término independiente $=0$?

Representan los **nodos de trasbordo**: la suma de los flujos que llegan es igual a la suma de
los que salen, o sea el nodo **solo funciona como paso intermedio**, no acumula ni genera.

**Ejemplo.** Un origen $O$ (oferta 50) envía a un destino $D$ (demanda 50) a través de un nodo
intermedio $K$. La restricción de $K$ es

$$-x_{OK} + x_{KD} = 0$$

**Si el término independiente no fuera cero:**

- **Positivo** (ej. $-x_{OK}+x_{KD}=10$): $K$ actúa como un **origen adicional** que aporta 10
  unidades propias de flujo, además de lo que recibe.
- **Negativo** (ej. $=-10$): $K$ actúa como un **destino** que retiene 10 unidades para consumo
  propio y entrega solo el excedente.

---

# Parte 4 — Programación entera y mixta (5)

> Transcripto y limpiado de `fuentes/preguntas-frecuentes.pdf`. **Sin cruzar todavía** contra
> `PLC8.pdf`.

### `ENT-01` — Tipos de modelos de PL con enteros

- **Enteros puros:** todas las variables son enteras.
- **Enteros mixtos:** algunas variables son enteras.
- **Binarios puros o mixtos:** las variables enteras están restringidas a $0$ o $1$, útiles
  para representar **decisiones dicotómicas** (sí/no).

### `ENT-02` — ¿Qué métodos existen?

Dos categorías:

**Métodos de corte.** Arrancan del óptimo del **programa lineal relajado** y añaden
restricciones secundarias (**cortes**) que recortan del espacio de soluciones las partes que no
contienen puntos enteros, hasta que el punto extremo solución satisface la condición de entero.
Se dividen en:
- **algoritmo fraccionario** — para programas enteros puros;
- **algoritmo mixto** — para modelos mixtos.

**Métodos de búsqueda.** Nacen de la idea de enumerar todos los puntos enteros posibles, pero
desarrollan tests que **inspeccionan solo una parte** de ellos teniendo en cuenta los
restantes. El más importante es **ramificación y poda** (*branch and bound*).

### `ENT-03` — Criterio de ramificación y poda

1. Resolver el **problema relajado** (ignorando la condición de integridad).
2. **Ramificar** por cualquiera de las variables con valor fraccionario: se elige una y el
   espacio de soluciones queda dividido en dos. Si $x_1^* = 3{,}5$, se crean dos ramas con las
   restricciones $x_1 \leq 3$ y $x_1 \geq 4$ — los valores intermedios se descartan porque no
   contienen enteros.
3. Cada subproblema se resuelve como PL relajado, con la **misma función objetivo**.
4. **Podar** (dejar de ramificar) un nodo en tres casos:
   - el subproblema es **infactible**;
   - su relajación es **peor o igual** que la mejor solución entera ya encontrada — no puede
     mejorarla, y esa solución entera hace de **cota**;
   - su solución **ya es entera**: se poda y, si mejora a la mejor conocida, pasa a ser la
     nueva cota.

Así se evita explorar todo el árbol.

### `ENT-04` — Programa lineal relajado

Cuando en un programa entero se **ignora la condición de integridad** de las variables, se dice
que el espacio de soluciones factibles se ha **relajado**. El PL que resulta se llama
**programa lineal relajado**. La mayoría de los algoritmos de programación entera se basan en
resolver una **sucesión de programas lineales relajados**.

Dos consecuencias que conviene poder decir:
- El óptimo del relajado es siempre **al menos tan bueno** como el del entero (es una **cota**:
  superior en maximización, inferior en minimización), porque el relajado admite todo lo que
  admite el entero y más.
- **Redondear** el óptimo del relajado no garantiza ni optimalidad ni factibilidad.

### `ENT-05` — ¿Por qué no vale la sensibilidad de LINDO en un programa entero?

No está entre las 89 preguntas del PDF, pero sí en el resumen del compañero, y es una trampa
clásica.

Al resolver un programa **entero** con LINDO (`GIN` para variables enteras, `INT` para
binarias), el software también usa ramificación y poda internamente. **No es válido usar los
precios sombra ni el análisis de sensibilidad que reporta:** esos valores corresponden al
**modelo lineal relajado**, no al modelo entero, al que el algoritmo le fue agregando las
restricciones propias de las ramas. La interpretación económica de los valores duales —"cuánto
mejora $z$ por una unidad más de recurso"— se apoya en que la base óptima no cambia, y en un
programa entero eso no aplica.

---

# Parte 5 — Modelos de redes (8)

> Transcripto y limpiado de `fuentes/preguntas-frecuentes.pdf`. **Sin cruzar todavía** contra
> `REDESUTN_2016.pdf`. Tema **no dado en clase** al 2026-09-27.

### `RED-01` — ¿Dónde se utilizan?

Redes de transporte, logística, redes eléctricas o de comunicación, seguimiento de proyectos,
administración de recursos y planificación financiera.

### `RED-02` — Definiciones

- **Red o grafo:** conjunto de **nodos** enlazados con **arcos**, con un flujo asociado
  (productos, fluidos, tráfico). Un **arco dirigido** permite flujo positivo en un solo sentido.
- **Red dirigida / no dirigida:** todos sus arcos son dirigidos / no dirigidos.
- **Trayectoria:** sucesión de arcos distintos que conectan dos nodos.
- **Ciclo:** trayectoria que empieza y termina en el mismo nodo.
- **Red conexa:** todo par de nodos está conectado por alguna ruta.
- **Árbol:** nodos conectados **sin ciclos**.
- **Árbol de expansión:** árbol que conecta **todos** los nodos de la red. Con $n$ nodos tiene
  exactamente $n-1$ arcos.
- **Árbol de expansión mínima:** el árbol de expansión de **longitud total mínima**.

### `RED-03` — Los tres problemas

- **Árbol de expansión mínima:** conectar todos los nodos sin formar ciclo, **minimizando la
  longitud total**.
- **Ruta más corta:** encontrar el camino de **menor distancia/costo/tiempo** entre un nodo
  origen y un nodo destino.
- **Flujo máximo:** en una red dirigida donde cada arco tiene capacidad máxima, **maximizar el
  flujo** que circula de la fuente al destino sin exceder esas capacidades.

### `RED-04` — Algoritmo del árbol de expansión mínima

> **Atención (ver E-4):** el PDF llama "Kruskal" a un procedimiento que en realidad es
> **Prim**. Acá van los dos, bien nombrados. Confirmar cuál usa la cátedra.

**Prim** — mantiene **un solo árbol conexo** que crece:
1. Arrancar de un nodo cualquiera.
2. Agregar el **arco más corto** que conecte el árbol actual con algún nodo **todavía no
   incluido**.
3. Repetir hasta tener $n-1$ arcos.

**Kruskal** — trabaja sobre **arcos ordenados**, sin exigir conexidad intermedia:
1. Ordenar **todos** los arcos de la red de menor a mayor longitud.
2. Recorrerlos en ese orden y agregar cada uno **si no forma ciclo** con los ya agregados.
3. Repetir hasta tener $n-1$ arcos. Durante la ejecución hay **varios fragmentos sueltos** que
   recién al final se unen en un único árbol.

En ambos: si hay **empate** en el arco más corto se elige cualquiera, y el empate indica que
hay **múltiples óptimos** (distintos árboles con la misma longitud total mínima).

**Usos:** redes eléctricas, de agua o gas, y de comunicaciones — conectar todos los puntos con
el menor costo total de tendido o cableado.

### `RED-05` — Ruta más corta y su algoritmo

Se usa en logística y transporte, típicamente para minimizar tiempos o costos de traslado.

**Algoritmo de Dijkstra** (rutas más cortas del origen a todos los demás nodos):
1. Etiquetar **temporalmente** todos los nodos alcanzables directo desde el origen, con
   `[distancia, nodo previo]`.
2. Fijar como **permanente** el nodo con **menor distancia** entre los etiquetados
   temporalmente.
3. **Reetiquetar** los vecinos del último nodo fijado, si la nueva distancia es menor que la que
   ya tenían.
4. Repetir 2–3 hasta que todos los nodos sean permanentes.

La ruta se **reconstruye hacia atrás** desde el destino, siguiendo el "nodo previo" de cada
etiqueta permanente hasta volver al origen.

**Modelo lineal:** una variable $x_{ij}$ por arco y una restricción de **conservación de flujo**
por nodo:

$$\text{Min } w = \sum_i \sum_j c_{ij}x_{ij} \quad \text{s.a.} \quad \sum_j x_{ij} - \sum_j x_{ji} = b_i$$

con $b_i = 1$ en el origen, $0$ en los intermedios y $-1$ en el destino. Se manda **una unidad**
de flujo del origen al destino, y el camino que elige es el más corto.

### `RED-06` — El problema de flujo máximo

Red **dirigida** en la que cada arco tiene una **capacidad máxima** de flujo. Todo el flujo se
origina en un nodo **fuente** y termina en un nodo **destino**; en cada nodo de **trasbordo**
el flujo que entra iguala al que sale; y no se puede exceder la capacidad de ningún arco. El
objetivo es **maximizar el flujo total** de la fuente al destino.

### `RED-07` — ¿Cómo se resuelve?

**Algoritmo de la trayectoria en aumento**, sobre la **red residual** (las capacidades que
quedan tras asignar flujo):
1. Buscar una trayectoria dirigida de la fuente al destino con **capacidad residual positiva**
   en todos sus arcos. Si no existe, **ya se llegó al óptimo**.
2. Sea $C$ la **menor capacidad residual** de esa trayectoria. **Restar $C$** a cada arco en el
   sentido del flujo y **sumar $C$** en el sentido inverso. Volver al paso 1.

**Modelo lineal:** $0 \leq x_{ij} \leq c_{ij}$ en cada arco, conservación de flujo en cada nodo
de trasbordo, y un **arco ficticio** de flujo $x_O$ que entra al nodo origen; la función
objetivo es maximizar $x_O$.

> **Lo que dice el resumen sobre el alcance:** *"el algoritmo especializado no es objeto de
> examen; alcanza con plantear el modelo lineal y resolverlo con LINDO"*. Priorizar entonces
> **plantear el modelo** por sobre ejecutar el algoritmo a mano.

### `RED-08` — Flujo capacitado con costo mínimo

Red **dirigida y conexa** con al menos un nodo **fuente** (suministro) y al menos uno
**destino** (demanda); el resto son nodos de **trasbordo**. Cada arco tiene **capacidad
máxima** y un **costo por unidad de flujo**. El objetivo es **minimizar el costo total** del
flujo, respetando la disponibilidad y la demanda de los nodos y la capacidad de cada arco.

Es el modelo **más general** de esta familia: transporte, trasbordo, ruta más corta y flujo
máximo son todos casos particulares suyos.

---

# Parte 6 — Gestión de stock (29)

> Transcripto y limpiado de `fuentes/preguntas-frecuentes.pdf`. **Sin cruzar todavía** contra
> `PLC9.pdf`, `STOCK16Transp.pdf` ni `PGSTOCK.pdf`. Último tema dado en clase; **29 de las 89
> preguntas** salen de acá.

## Ruta de estudio recomendada

Las 29 no están en orden pedagógico en el PDF. Este es el orden en que conviene estudiarlas:

| Bloque | Preguntas | Qué es |
|---|---|---|
| 1. Conceptual | `02` `03` `10` `11` `12` `13` `01` `09` | Por qué existe el stock, sus causas y costos, ABC |
| 2. Modelo básico (EOQ) | `05` `14` `15` | La curva de costo, su mínimo, cómo bajarlo |
| 3. Consumo durante el ingreso | `06` `16` | Producción y consumo simultáneos |
| 4. Descuentos | `27` `17` | Precio que depende de $Q$ |
| 5. Período común | `04` `26` | Varios artículos comprados juntos |
| 6. Restricciones (Lagrange) | `28` `29` `08` `18` `19` `20` | Espacio, dinero, tiempo de preparación |
| 7. Caso aleatorio | `21` `22` `23` `07` `24` `25` | Stock de seguridad, riesgo de faltante |

**El bloque 6 es el que más rinde por hora**: son tres modelos con **la misma estructura**
(mismo $Q^*$ del modelo base con un parámetro corregido) y cuatro preguntas que solo piden la
interpretación de $\lambda$.

---

## Bloque 1 — Conceptual

### `STK-02` — ¿Por qué el stock es un desperdicio? Si lo es, ¿por qué existe?

**Desperdicio** es todo aquello que no resulte absolutamente esencial para agregar valor al
producto. El stock lo es porque: las existencias **no agregan valor** por sí mismas,
**ocultan los problemas de producción**, **inmovilizan capital** y su mantenimiento **genera
costos**.

Entonces el stock ideal sería **nulo**, pero como en la mayoría de los casos eso no es posible,
se considera un **desperdicio inevitable**.

### `STK-11` — Principales causas generadoras de stock

1. Aleatoriedad en la **demanda**.
2. Aleatoriedad en los **aprovisionamientos**.
3. Elevado **tiempo de puesta a punto** de máquinas o equipos.
4. **Paradas no programadas** (roturas) de máquinas o equipos.
5. Equipamiento **poco versátil** o insuficiente.
6. Falta de **versatilidad del personal**.
7. **Fallas de calidad**.

### `STK-03` — Problemas que causan stock y herramientas para solventarlos

| Problema | Solución |
|---|---|
| Aleatoriedad en la demanda | Involucrar activamente a los clientes (relaciones *win-win*). Contar con un sistema de **pronósticos de demanda** |
| Aleatoriedad en los aprovisionamientos | Participación activa de los proveedores (relaciones *win-win*) |
| Elevado tiempo de puesta a punto de máquinas | Aplicar **SMED** (*Single Minute Exchange of Die*) |
| Paradas no programadas (roturas) | Ejecutar un programa de **Mantenimiento Productivo Total** |
| Falta de versatilidad del personal | **Capacitación** y entrenamiento |

### `STK-10` — Objetivos de la gestión de existencias

1. **Reducir al mínimo posible** los niveles de existencia.
2. **Asegurar el suministro** de productos en el momento adecuado.

Son objetivos en tensión: eso es exactamente lo que resuelven los modelos.

### `STK-12` — Beneficios de invertir en stocks

- Producir bienes **a cierta distancia** del consumidor.
- **Anticipar cambios en la demanda** (demandas estacionales que pueden superar la capacidad de
  producción).
- **Balancear operaciones sucesivas** con distintas tasas de producción.
- Reducir **costos unitarios** mediante compras por cantidad.
- Reducir **costos unitarios de transporte** por cantidad.
- Realizar **compras especulativas** ante alzas de precios.

### `STK-13` — ¿Cómo se logra la reducción de existencias?

Mediante la **disminución del tamaño de los lotes** y el **acortamiento de los plazos de
provisión**. Pero previo a eso se requiere un proceso de **mejora continua** que elimine
progresivamente las principales **causas generadoras** (las de `STK-11`).

> El orden importa y es lo que se pregunta: **primero** se atacan las causas, **después** se
> bajan los lotes. Bajar los lotes sin haber eliminado las causas solo traslada el problema.
> Ver también `STK-15`.

### `STK-01` — ¿Cómo se calculan las tasas de mantenimiento de stock?

A partir de estos **costos generales de mantenimiento de existencias**:

- **Capital inmovilizado** — lo que se pierde por haber invertido en stock. *Ej.:* comprar
  unidades para almacenar hace perder la posibilidad de invertir esos fondos en otro lado.
- **Espacios de almacenamiento** — *ej.:* el alquiler mensual de los depósitos.
- **Personal** — movimiento, limpieza, etc., dependientes de la cantidad almacenada. *Ej.:* el
  sueldo de los empleados de mantenimiento de existencias.
- **Riesgos** — deterioro, roturas y seguros.
- **Administración** — auditorías, recuentos físicos, búsqueda de diferencias.
- **Impuestos** — impuesto a los activos.

Para obtener la tasa de mantenimiento se **suman todos estos costos anuales** y se dividen por
la **cantidad total de existencias** $Q$.

### `STK-09` — Clasificación ABC

Clasifica los artículos en tres grupos según el **costo anual de las cantidades demandadas**:

- **A:** artículos de **alto** costo — hasta el **75 %** del costo total.
- **B:** costo **intermedio** — entre el **75 %** y el **95 %**.
- **C:** **bajo** costo — entre el **95 %** y el **100 %**.

**Pasos:**
1. Calcular el costo total anual de cada artículo.
2. Ordenar los artículos en forma **decreciente** según ese costo.
3. Calcular el porcentaje sobre el total y el **porcentaje acumulado**.
4. Clasificar.

Para los artículos de **bajo costo (C)** se usa **revisión periódica**, en vez de sistemas de
punto de pedido — no vale la pena el costo administrativo de un registro continuo.

---

## Bloque 2 — Modelo básico (EOQ / Wilson)

### `STK-14` — Componentes del costo unitario en el momento de la utilización y su mínimo

$$CT(Q) = C(Q)\cdot Q + L + C(Q)\cdot i \cdot A(Q)$$

- $C(Q)\cdot Q$ — **costo de compra o fabricación** del lote de extensión $Q$. $C$ es el costo
  unitario en $\$/\text{unidad}$ y **puede ser función de $Q$** (el precio varía según la
  cantidad: ver bloque 4).
- $L$ — **costo fijo de la orden** de compra, en $\$$. **No depende de $Q$**: se incurre cada
  vez que se coloca un pedido.
- $C(Q)\cdot i \cdot A(Q)$ — **costo de mantenimiento** de existencias. $i$ es la **tasa de
  mantenimiento**, en $1/\text{tiempo}$, y $A(Q)$ es la existencia media acumulada en el tiempo.

**Determinación del mínimo.** Bajo los supuestos del modelo básico, $A(Q) = Q^2/(2D)$ — porque
la existencia media es $Q/2$ y el ciclo dura $T=Q/D$, así que $A(Q)=(Q/2)(Q/D)$. Dividiendo
todo por $Q$ para pasar a costo **por unidad**:

$$CT(Q) = C + \frac{L}{Q} + \frac{C\cdot i\cdot Q}{2D}$$

Tiene un **único punto extremo**, mínimo relativo y absoluto a la vez. Derivando e igualando a
cero:

$$\frac{dCT(Q)}{dQ} = -\frac{L}{Q^2} + \frac{C\cdot i}{2D} = 0 \quad \Longrightarrow \quad \boxed{Q^* = \sqrt{\frac{2D\cdot L}{C\cdot i}}}$$

### `STK-05` — ¿Cómo se compone la curva de costo directo total mínimo? Graficar

$CT(Q)$ es la **suma de tres curvas**:

- $C(Q)$ — costo unitario de compra o fabricación. En el modelo básico es **constante**: recta
  horizontal.
- $L/Q$ — costo fijo de la orden repartido por unidad. **Decrece** al crecer $Q$ (menos pedidos
  por año): hipérbola.
- $\dfrac{C\cdot i\cdot A(Q)}{Q} = \dfrac{C\cdot i\cdot Q}{2D}$ — costo de mantenimiento por
  unidad. **Crece** con $Q$ (lotes más grandes, más existencia inmovilizada): recta creciente.

Como una decrece y la otra crece, la suma tiene un **único mínimo**, que se alcanza justo donde
**el costo de ordenar y el costo de mantener se cruzan** (se igualan). Ese punto es
$Q^* = \sqrt{2DL/(C i)}$.

```
  $/unidad
     │╲                                    ╱  CT(Q) = suma
     │ ╲                                ╱
     │  ╲                            ╱
     │   ╲___                     ╱
     │       ‾‾─╲_            _╱‾            ← mínimo donde se cruzan
     │           ‾╲_______╱‾
     │        L/Q  ╲   ╱   C·i·Q/(2D)
     │              ╲╱
     │──────────────┼──────────────────────  C  (constante)
     └──────────────┼──────────────────────→ Q
                   Q*
```

### `STK-15` — ¿Cómo puedo reducir los costos $CT(Q)$?

Mirando la fórmula, **lo único que se puede modificar es $L$**: $C$, $i$ y $D$ vienen dados. Si
se está fabricando, se baja $L$ cambiando las máquinas, arreglando una falla, aplicando SMED,
etc.

> La frase que hay que saber decir: **"la clave para reducir los stocks sin incrementar el costo
> medio está en disminuir el costo fijo de ordenar ($L$), no en simplemente pedir lotes más
> chicos"**. Si se baja $Q$ por debajo de $Q^*$ sin tocar $L$, el costo total **sube**. Es la
> misma idea que `STK-13`: primero la causa, después el lote.

---

## Bloque 3 — Consumo durante el ingreso

### `STK-06` — Desarrolle el modelo con consumo durante el ingreso

Se aplica cuando el lote **no ingresa de golpe** al almacenamiento, sino **durante cierto
período** — típico cuando la producción y el consumo de un artículo suceden **simultáneamente**.

Si el lote $Q$ ingresa en forma continua y uniforme durante un intervalo $\theta$, y $V$ es la
**velocidad de ingreso** $[\text{unidades}/\text{tiempo}]$:

$$\theta = \frac{Q}{V}$$

Durante $\theta$ también hay **salidas** a velocidad $D$, así que el stock máximo alcanzado
**no es $Q$**, sino

$$M = Q\left(1-\frac{D}{V}\right)$$

Con $T = Q/D$:

$$A(Q) = \frac{T\cdot M}{2} = \frac{(1-D/V)}{2D}\,Q^2$$

$$CT(Q) = C + \frac{L}{Q} + \frac{C\cdot i\cdot (1-D/V)}{2D}\,Q$$

Derivando e igualando a cero:

$$\boxed{Q^* = \sqrt{\frac{2D\cdot L}{C\cdot i\,(1-D/V)}}}$$

Es el $Q^*$ del modelo básico con la tasa de mantenimiento **corregida por el factor
$(1-D/V)$**, que es menor que 1: el stock promedio es menor, mantener sale más barato, y por eso
**el lote óptimo es más grande** que en el modelo básico.

**Punto de pedido.** Vale $PP = D\cdot LT$, pero acá el $LT$ se compone **solo de los tiempos de
organización y puesta a punto** para iniciar la corrida de producción — **no incluye** el tiempo
de fabricación del lote en sí, porque el consumo se va abasteciendo de lo que se produce.

### `STK-16` — ¿Cómo debe ser la relación entre $V$ y $D$?

**$D < V$**: la demanda debe ser **menor** que la velocidad de ingreso. Se ve en la fórmula: si
$V \to D$, entonces $(1-D/V) \to 0$, el denominador tiende a cero y $Q^* \to \infty$. Habría que
provocar ingresos de **forma continua**, resultando un **lote infinito** — es decir, producir
sin parar solo para no quedarse sin stock. Con $V < D$ el modelo no tiene sentido: la producción
no llega a cubrir el consumo.

---

## Bloque 4 — Descuentos

### `STK-27` — Descuento por cantidad excedente: límite de $C(Q)$ cuando $Q\to\infty$

Se compran $Q > a$ unidades: las primeras $a$ se pagan a $C_1$ y las $Q-a$ restantes a
$C_2 < C_1$. El **precio medio por unidad** es

$$C(Q) = \frac{C_1 a + C_2(Q-a)}{Q} = C_2 + \frac{(C_1-C_2)a}{Q} = C_2 + \frac{k}{Q}, \qquad k = (C_1-C_2)a$$

Como $k$ es una **constante**, al crecer $Q$ el término $k/Q$ tiende a cero:

$$\lim_{Q\to\infty} C(Q) = \lim_{Q\to\infty}\left(C_2 + \frac{k}{Q}\right) = C_2$$

**Lectura.** El precio medio baja a medida que se compra más, **acercándose a $C_2$ por encima
sin alcanzarlo nunca** (siempre $C(Q) > C_2$ para $Q$ finito). A diferencia del modelo de **un
escalón** —donde el precio **salta** a $C_2$ para todo el lote—, acá el descuento se aplica
**solo al excedente** y $C(Q)$ es **continua** en $Q=a$:

$$C(a) = C_2 + \frac{(C_1-C_2)a}{a} = C_2 + (C_1-C_2) = C_1 \;\checkmark$$

### `STK-17` — Descuento por cantidad excedente con valor mínimo de compra y $L$ nulo

**Lo que dice el PDF, literal:** *"Si $L=0$, la gráfica de la ley de precios tiene un mínimo
(que no es cero) y la función económica pasa a ser lineal."*

> ⚠ **Respuesta a verificar.** Es la más floja de las 29 y no la reconstruí. Sustituyendo
> $C(Q)=C_2+k/Q$ con $L=0$ en el costo unitario queda
> $CT(Q) = \left(C_2 + \frac{k\,i}{2D}\right) + \frac{k}{Q} + \frac{C_2\, i\, Q}{2D}$,
> que **sigue teniendo** un término en $1/Q$ y uno lineal — o sea sigue habiendo un mínimo
> interior en $Q^*=\sqrt{2Dk/(C_2 i)}$, con $k$ jugando el papel de $L$. Eso **no es** una
> función lineal, así que o el PDF se refiere a otra cosa por "función económica", o está mal.
> **Contrastar con `PLC9.pdf` / `STOCK16Transp.pdf` antes de contestar esto en el parcial.**

---

## Bloque 5 — Período común

### `STK-04` — Diferencia entre punto de pedido y período común

**Punto de pedido.** Se hace un pedido de tamaño $Q^*$ **cada vez que el stock disponible**
(existencias más pendientes de entrega) **alcanza el valor $PP$**. Son sistemas **activados por
la demanda**: requieren actualizar los registros cada vez que se retira o agrega un artículo,
para verificar si se llegó al punto de pedido.

**Período común (tiempo fijo).** Se aplican **en conjunto a varios artículos** de una familia, y
el pedido se coloca **al término de un intervalo de tiempo predeterminado**. Son sistemas
**activados por el tiempo**: basta actualizar las existencias **en el momento de la revisión**,
sin registro continuo.

### `STK-26` — Costo total del modelo de período común: gráfico y desarrollo

Todos los artículos se compran juntos cada $T$, así que $Q_j = D_j\cdot T$. El costo del
artículo $A_j$ en el momento de su utilización es

$$CT(Q_j) = C_j + \frac{L_j}{Q_j} + \frac{\delta_j}{2D_j}Q_j, \qquad
\delta_j = \begin{cases} C_j\,i & \text{(modelo básico)}\\[2pt] C_j\,i\,(1-D_j/V_j) & \text{(consumo durante el ingreso)}\end{cases}$$

Reemplazando $Q_j = D_j T$, multiplicando cada uno por $D_j$ (para pasar a **costo anual**) y
sumando sobre los $n$ artículos:

$$CT(T) = C + \frac{L}{T} + \frac{S}{2}T, \qquad C=\sum_j C_j D_j,\quad L=\sum_j L_j,\quad S=\sum_j \delta_j D_j$$

**Significado de cada parte:**
- $C=\sum C_j D_j$ — costo anual de compra o fabricación de todos los artículos. **No depende de
  $T$**: recta horizontal.
- $L/T$ — costo anual de ordenar. $L$ es el gasto fijo **total del trámite conjunto** (no hace
  falta conocer cada $L_j$). **Decrece** con $T$ (hipérbola): a mayor período, menos órdenes por
  año.
- $\frac{S}{2}T$ — costo anual de mantenimiento. **Crece linealmente** con $T$: lotes más
  grandes, más stock inmovilizado.

La curva $CT(T)$ es la suma de las tres y tiene un **único mínimo**, donde se cruzan el costo de
ordenar y el de mantener:

$$-\frac{L}{T^2} + \frac{S}{2} = 0 \quad \Longrightarrow \quad \boxed{T^* = \sqrt{\frac{2L}{S}}}, \qquad Q_j^* = D_j\cdot T^*$$

> Es **la misma estructura** que el modelo básico, con $T$ en lugar de $Q$. Si tenés
> internalizado el EOQ, esto es gratis.

---

## Bloque 6 — Restricciones (multiplicadores de Lagrange)

Los tres modelos tienen **la misma mecánica**: se plantea el lagrangiano, se deriva respecto de
cada $Q_j$, y el resultado es **el $Q_j^*$ del modelo sin restricción con un parámetro
corregido**. Y el **procedimiento de resolución es idéntico** en los tres:

1. Calcular los $Q_j^*$ **sin restricción** ($\lambda=0$) y ver el recurso que consumen.
2. Si **no** superan el disponible, la restricción **no es efectiva** y no hay nada más que hacer.
3. Si lo superan, **dar valores a $\lambda>0$** crecientes hasta que la restricción se cumpla con
   igualdad.

### `STK-29` — Modelo con restricción de espacio de almacenamiento

Hay $n$ artículos (modelo básico), cada uno con volumen unitario $v_j$. Se supone que cada
artículo ocupa un espacio igual a su **existencia máxima $Q_j$**, y el espacio total no puede
superar $E_0$:

$$\text{Min } CT = \sum_{j=1}^{n}\left(C_j D_j + \frac{L_j D_j}{Q_j} + \frac{C_j i}{2}Q_j\right) \quad \text{s.a.} \quad \sum_{j=1}^{n} v_j Q_j - E_0 = 0$$

**Lagrangiano:**

$$F(Q_j,\lambda) = CT + \lambda\left(\sum_j v_j Q_j - E_0\right)$$

**Condición de mínimo** (derivando respecto de cada $Q_j$ e igualando a cero):

$$-\frac{L_j D_j}{Q_j^2} + \frac{C_j i}{2} + \lambda v_j = 0 \quad \Longrightarrow \quad \boxed{Q_j^* = \sqrt{\frac{2 D_j L_j}{C_j i + 2\lambda v_j}}}$$

Es el $Q_j^*$ del modelo básico con la **tasa de mantenimiento aumentada** en un término
proporcional al volumen: $C_j i \to C_j i + 2\lambda v_j$. Los artículos **voluminosos se
penalizan más** y sus lotes se achican más. Derivando respecto de $\lambda$ se recupera la
restricción $\sum_j v_j Q_j = E_0$.

### `STK-28` — Modelo con restricción de tiempo de preparación de máquinas

Hay $n$ artículos, cada uno con tiempo de preparación $\tau_j$ **por lote**, y el tiempo total
anual de preparación no puede superar $P_0$. Cada artículo se fabrica (modelo con consumo durante
el ingreso, velocidad $V_j$):

$$\text{Min } CT = \sum_{j=1}^{n}\left(C_j D_j + \frac{L_j D_j}{Q_j} + \frac{C_j i(1-D_j/V_j)}{2}Q_j\right) \quad \text{s.a.} \quad \sum_{j=1}^{n}\frac{D_j}{Q_j}\tau_j - P_0 = 0$$

El tiempo anual de preparación de cada ítem es la **cantidad de lotes por año** ($D_j/Q_j$) por
$\tau_j$.

**Lagrangiano:**

$$F(Q_j,\lambda) = CT + \lambda\left(\sum_j \frac{D_j \tau_j}{Q_j} - P_0\right)$$

**Condición de mínimo:**

$$-\frac{L_j D_j}{Q_j^2} + \frac{C_j i(1-D_j/V_j)}{2} - \frac{\lambda D_j \tau_j}{Q_j^2} = 0 \quad \Longrightarrow \quad \boxed{Q_j^* = \sqrt{\frac{2 D_j (L_j + \lambda\tau_j)}{C_j i\,(1-D_j/V_j)}}}$$

Es el $Q_j^*$ del modelo sin restricción con el **costo de orden $L_j$ reemplazado por
$L_j + \lambda\tau_j$**. Derivando respecto de $\lambda$ se recupera
$\sum_j (D_j/Q_j)\tau_j = P_0$.

> **Ojo al sentido**, que es al revés del de espacio: acá subir $\lambda$ **agranda** los lotes
> (porque engorda el numerador), y lotes más grandes significan **menos corridas por año**, o
> sea **menos tiempo total de preparación**. Que es justamente lo que la restricción pide.

### `STK-08` — Unidades de $\lambda$ en el modelo con restricción de espacio

$$\lambda = \frac{\$}{[\text{volumen}\times\text{tiempo}]} \qquad \text{(ej.: \$/m}^3\!\times\text{mes)}$$

Se verifica con la fórmula de `STK-29`: $\lambda v_j$ tiene que sumar con $C_j i$, que está en
$\$/(\text{unidad}\cdot\text{tiempo})$; y $v_j$ está en $\text{volumen}/\text{unidad}$. Entonces
$\lambda$ queda en $\$/(\text{volumen}\cdot\text{tiempo})$. ✓

### `STK-19` — Interpretación económica de $\lambda$ (restricción de almacenamiento)

Es el **costo de no disponer de una unidad de espacio de almacenamiento**, es decir el **costo
marginal de no disponer de más espacio**.

### `STK-20` — Interpretación económica de $\lambda$ (restricción de tiempo de preparación)

Es el **costo marginal de no disponer de tiempo adicional para la preparación de máquinas**. Se
expresa en $\$/\text{unidad de tiempo}$ — se verifica porque $L_j + \lambda\tau_j$ tiene que
quedar en $\$$, y $\tau_j$ está en unidades de tiempo.

### `STK-18` — Interpretación económica de $\lambda$ y de $i+\lambda$ (restricción financiera)

**$\lambda$** es el **incremento del costo anual por cada peso que podría economizarse si
dispusiéramos de más capital a interés $i$**. Dicho de otro modo: el **costo marginal de no
disponer de más dinero**.

**$i+\lambda$** da el valor de **un interés por debajo del cual conviene aceptar dinero para
invertir en stocks** — es la tasa que se está dispuesto a pagar. La comparación correcta **no es
contra $i$ solo, sino contra $i+\lambda$**: si la tasa que ofrecen es menor a $i+\lambda$,
conviene tomar el dinero y meterlo en stock.

> ⚠ **Detalle a verificar.** Por analogía con `STK-29` (donde la restricción se plantea sobre la
> existencia **máxima** y el resultado es $C_j i + 2\lambda v_j$), si la restricción financiera se
> plantea sobre el **capital máximo** $\sum C_j Q_j \le F_0$, el factor corregido sería
> $i + 2\lambda$, no $i+\lambda$. La forma $i+\lambda$ sale de plantearla sobre la **inversión
> media** $\sum C_j Q_j/2 \le F_0$. La **interpretación** de arriba es la que piden y no cambia;
> el factor exacto depende de cómo escribe la restricción el apunte. **Confirmar en `PLC9.pdf`.**

---

## Bloque 7 — Caso aleatorio

Cuando no se justifica suponer demanda constante y conocida (ni plazos de provisión constantes),
hay que mantener un **stock de seguridad** que proteja contra el agotamiento.

$$PP = \mu_{D_{LT}} + z\cdot\sigma_{D_{LT}} \approx \bar{D}\cdot LT + z\cdot S_{D_{LT}}, \qquad SS = z\cdot S_{D_{LT}}$$

### `STK-21` — ¿Qué es el stock de seguridad (SS)?

Un stock que actúa como **protección ante la posibilidad de agotamiento** de las existencias.
Tiene por objeto **absorber la variabilidad** de la demanda y del plazo de provisión ($LT$).

### `STK-22` — ¿Qué es el riesgo de faltante (RF)?

Un **criterio para determinar cuánta protección** se garantiza contra el agotamiento. Es la
**probabilidad de que la demanda durante el plazo de provisión exceda el punto de pedido**.

### `STK-23` — ¿Por qué la tabla de RF es la misma que la de la normal estándar?

Porque la probabilidad del riesgo de faltante está dada por la **distribución normal**:

- Si la demanda sigue una distribución normal, por la **propiedad reproductiva de la normal** la
  demanda acumulada durante el período $LT$ (el período relevante para el cálculo del RF)
  **también será normal**.
- Y si la demanda **no** fuera normal, la demanda acumulada durante el $LT$ se **aproxima** a una
  normal por el **Teorema Central del Límite**.

En ambos casos se termina trabajando con una normal, así que la tabla de RF **es** la tabla de la
normal estándar.

### `STK-07` — ¿Un RF 2 % es lo mismo que un IPF 98 %?

**No, son dos parámetros totalmente distintos.**

- **RF (riesgo de faltante):** **probabilidad** de que la demanda durante el $LT$ exceda el $PP$.
  Se mide **por ciclo de reposición**.
- **IPF (proporción de entrega directa por ítem):** **cociente** entre la cantidad entregada
  directamente al cliente desde el stock y la cantidad total demandada. Se mide **sobre
  cantidades**, no sobre ciclos.

Uno es una probabilidad de que ocurra un evento; el otro, una fracción de demanda servida.
Pueden convivir valores muy distintos: un faltante puede ocurrir en el 2 % de los ciclos y, si
cuando ocurre es grande, dejar el IPF bastante por debajo del 98 %.

### `STK-24` — ¿Por qué en revisión periódica la demanda se estudia durante $T+LT$?

Porque **ese es el intervalo total en el que el sistema depende exclusivamente del inventario
disponible, sin recibir reposiciones**: se revisa, se pide, y hasta que llega el pedido pasan
$LT$; pero además, entre revisión y revisión pasan $T$ sin que se pueda corregir nada.

Los parámetros de demanda (media y desviación estándar) se calculan **en ese plazo** para estimar
tanto el consumo esperado como la **incertidumbre total** hasta la llegada del nuevo pedido, y
así asegurar el nivel de servicio deseado.

> Contraste con punto de pedido, donde el período relevante es solo $LT$: ahí el sistema **puede
> reaccionar en cualquier momento** en que el stock cruce el $PP$, así que el único tramo a ciegas
> es el plazo de provisión.

### `STK-25` — Punto de pedido con RF especificado vs. revisión periódica con RF especificado

**Punto de pedido:** se pide un lote de tamaño $Q^*$ cada vez que el stock disponible alcanza el
valor $PP$. Son sistemas **activados por la demanda**, por lo que **requieren actualizar los
registros** siempre que se retiren o agreguen artículos, para verificar si se alcanzó el $PP$.

**Revisión periódica:** basta **actualizar las existencias al momento de la revisión** — son
sistemas **activados por el tiempo**.

La consecuencia de fondo, que es lo que conviene agregar: por lo anterior, el período de
incertidumbre es $LT$ en punto de pedido y $T+LT$ en revisión periódica (ver `STK-24`), así que
**para un mismo RF la revisión periódica exige más stock de seguridad**.

---

# Parte 7 — Las 37 de Unidades 1 a 5: dónde está cada respuesta

Estas no hace falta estudiarlas de este archivo: están desarrolladas y **verificadas contra las
resoluciones oficiales** en la wiki. Acá va el puntero.

| Código | Ir a |
|---|---|
| `GRA-01` tipos de solución | [[IO]] Unidad 1 → *Tipos de solución*, y las frases hechas de *Formato de respuesta de la cátedra* |
| `FOR-01` forma estándar | [[IO]] Unidad 1 → *Formas de presentación* |
| `FOR-02` restricciones activas y redundantes | [[IO]] Unidad 1 → *Clasificación de restricciones*; redundancia analítica también en Unidad 3 |
| `CBA-01` tres teoremas | [[IO]] Unidad 2 → *Teoremas* |
| `CBA-02` convexidad y punto extremo | [[IO]] Unidad 2 → *Convexidad* |
| `CBA-03` básica en cero | [[IO]] Unidad 3 → *Diagnóstico de la tabla* (**y E-2 de este archivo**) |
| `CBA-04` máximo de puntos extremos | [[IO]] Unidad 2; el $\binom{n}{m}$ está en [[practica-3-simplex]] ej. 3 |
| `CBA-05` solución conceptual | [[IO]] Unidad 2 → *Solución conceptual* |
| `CBA-06` por qué bastan los vértices | [[IO]] Unidad 2 → *Teoremas* + *El puente entre el gráfico y el álgebra* |
| `SPX-01` ficticias y penalización | [[IO]] Unidad 3 → *Variables ficticias*, *Penalización*; [[machete-metodo-simplex]] |
| `SPX-02` degeneración | [[IO]] Unidad 3 → *Diagnóstico* (**leer E-1 primero**) |
| `SPX-03` `SPX-04` `SPX-05` desarrollos analíticos | [[IO]] Unidad 3 → *Condición de optimalidad* y *de factibilidad* (el PDF no las responde: E-5) |
| `SPX-06` coeficientes de sustitución | [[IO]] Unidad 3; y [[teoria-sensibilidad-dualidad]] Parte 1 |
| `SPX-07` $c_j-z_j=0$ en no básica | [[IO]] Unidad 3 → *Diagnóstico*, caso *óptimos alternativos* |
| `SPX-08` efecto espejo | [[IO]] Unidad 3 → *Efecto espejo* |
| `SPX-09` ficticia en la solución óptima | [[IO]] Unidad 3 → *Dos fases* y el caso de la ficticia básica nula |
| `SPX-10` costos reducidos | [[IO]] Unidad 4; y [[teoria-sensibilidad-dualidad]] → *Costo reducido ≠ costo marginal* |
| `SPX-11` condición de factibilidad | [[IO]] Unidad 3; [[machete-metodo-simplex]] |
| `SPX-12` condición de optimización | [[IO]] Unidad 3; [[machete-metodo-simplex]] |
| `SPX-13` degeneración e incremento de $z$ | [[IO]] Unidad 3 → *Ciclado* y *reglas de desempate* |
| `SPX-14` básica igual a uno | [[IO]] Unidad 3 (**y E-3 de este archivo**) |
| `SPX-15` entrar el $c_j-z_j$ no más negativo | [[IO]] Unidad 3 → *Criterios de entrada* |
| `SPX-16` no acotada en tabla y gráfico | [[IO]] Unidad 3 → *Diagnóstico*; [[practica-3-simplex]] ej. 2.d |
| `SPX-17` dónde está $B^{-1}$ | [[IO]] Unidad 3 (cierre) y Unidad 4; [[teoria-sensibilidad-dualidad]] → *Dónde está $B^{-1}$, sin calcularla* |
| `SEN-01` agregar una restricción | [[teoria-sensibilidad-dualidad]] → *Caso 5*; [[practica-4-sensibilidad-dualidad]] inciso g |
| `SEN-02` exceso en cero *(multiple choice)* | [[teoria-sensibilidad-dualidad]] → *Holguras complementarias* |
| `SEN-03` signo de los valores implícitos | [[teoria-sensibilidad-dualidad]] → *Qué significa cada número* |
| `SEN-04` cambio en $b_k$ | [[teoria-sensibilidad-dualidad]] → *Caso 2*; [[practica-4-sensibilidad-dualidad]] inciso d |
| `SEN-05` valor implícito, precio sombra, valor marginal | [[teoria-sensibilidad-dualidad]] → *Costo reducido ≠ costo marginal* y *La frase económica que hay que saber decir* |
| `SEN-06` cambio en $c_k$ | [[teoria-sensibilidad-dualidad]] → *Caso 1*; [[practica-4-sensibilidad-dualidad]] incisos b y c |
| `SEN-07` agregar una variable | [[teoria-sensibilidad-dualidad]] → *Caso 4*; [[practica-4-sensibilidad-dualidad]] inciso f |
| `DUA-01` teorema dual | [[teoria-sensibilidad-dualidad]] → *Teorema fundamental de la dualidad* |
| `DUA-02` alternativa / no acotada en el dual | [[IO]] Unidad 5; [[teoria-sensibilidad-dualidad]] Parte 2 |
| `DUA-03` holguras complementarias | [[teoria-sensibilidad-dualidad]] → *Holguras complementarias* |
| `DUA-04` igualdades en el primal | [[teoria-sensibilidad-dualidad]] → *Cómo se construye el dual, mecánicamente* |

---

## Pendientes de este banco

- [ ] Cruzar las Partes 3 a 6 contra el apunte de cátedra (`PLC7`, `PLC8`, `PLC9`,
      `Modelos especiales de PL.pdf`, `REDESUTN_2016.pdf`, `STOCK16Transp.pdf`) y volcar el
      resultado a las Unidades 7, 8, 9 y 11 de [[IO]].
- [ ] Resolver `STK-17`, que quedó marcada como dudosa.
- [ ] Confirmar el factor $i+\lambda$ vs. $i+2\lambda$ de `STK-18`.
- [ ] Confirmar si la cátedra llama Prim o Kruskal al algoritmo de `RED-04` (E-4).
- [ ] Confirmar con la cátedra si entran **CPM/PERT** y **programación no lineal**: no figuran
      en ninguno de los dos materiales nuevos y no se dieron en clase.
