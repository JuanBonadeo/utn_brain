# Podcast SIM 3 de 8 — El modelo de inventario (s, S)

Fuente para un episodio de podcast de estudio. Materia: Simulación (UTN, Ingeniería en
Sistemas, 4.º año). Sirve para el primer parcial, el sábado 7 de noviembre de 2026: integrado
teórico-práctico y probablemente multiple choice. Las respuestas del banco son la clave revisada
por nosotros, no la corrección oficial de la cátedra.

## Indicaciones para el episodio

La política (s, S) con revisión periódica, por qué aparece el backlog, los tres costos y con qué nivel va cada uno, los cuatro eventos y su prioridad, y qué concluye Law al comparar las 9 políticas. Contar el procedimiento del ejercicio numérico, no leer los números. Cerrar con la diferencia con Investigación Operativa.

## Contenido principal

### 5. Modelo de inventario (s, S)

*Fuentes: Law §1.5 completo (Weitz, hojas 23 a 28 del PDF) y diapositivas "Simulación – Inventarios". Es el tema del ejercicio numérico.*

#### 5.1 El planteo

Una empresa vende **un solo producto** y quiere decidir cuántas unidades tener en stock durante los próximos $n$ meses.

- Las demandas llegan con **tiempos entre demandas exponenciales**. En Law la media es 0,1 mes.
- El **tamaño de cada demanda** $D$ es una variable discreta. En Law vale 1, 2, 3 o 4, con probabilidades 1/6, 1/3, 1/3 y 1/6, y se genera con la **distribución empírica** (§9.2).
- El inventario se **revisa al principio de cada mes**. Es una **revisión periódica**.
- El pedido no llega enseguida: tarda una **demora** $L$, que en Law es uniforme entre 0,5 y 1 mes.

**La política (s, S):** al revisar, se mira el nivel $I$ y se aplica

$$Z = \begin{cases} S - I & \text{si } I < s \\ 0 & \text{si } I \ge s \end{cases}$$

Es decir: si el inventario está por debajo de $s$, se pide **lo que falta para llegar a $S$**. Si no, no se pide nada.

> **Ojo:** la política **no** asegura que el inventario quede entre $s$ y $S$. Entre dos revisiones puede caer muy por debajo de $s$, e incluso **volverse negativo**. Tampoco se piden "$s$ unidades" ni "$S$ unidades": se pide $Z = S - I$.

#### 5.2 El nivel de inventario y el backlog

Cuando una demanda supera el stock, **no se pierde**: queda **pendiente** (*backlog*) y el inventario se vuelve negativo. Cuando llega el pedido, **primero cubre el backlog** y el resto va al depósito. Por eso se usan tres niveles:

- $I(t)$ es el nivel neto, que puede ser negativo.
- $I^+(t) = \max\{I(t), 0\}$ es lo que hay **en depósito**.
- $I^-(t) = \max\{-I(t), 0\}$ es lo que **se debe**.

**Diferencia con Investigación Operativa.** En IO el control es **continuo**: se pide apenas el stock toca el punto de reorden. Acá el control es **periódico**: solo se mira al inicio de cada mes. Por eso puede aparecer backlog.

#### 5.3 Los costos

| Costo | Cuánto vale | Se paga |
|---|---|---|
| **Pedido** | $K + iZ$: $K$ es el costo fijo de preparación (*setup*) e $i$ el costo **unitario** | solo si $Z > 0$. Si no se pide, no se paga ni siquiera $K$ |
| **Mantenimiento** (*holding*) | $h$ por unidad y por mes, aplicado a $\bar I^+ = \frac{1}{n}\int_0^n I^+(t)\,dt$ | por lo que hay **en depósito** |
| **Faltante** (*shortage*) | $\pi$ por unidad y por mes, aplicado a $\bar I^- = \frac{1}{n}\int_0^n I^-(t)\,dt$ | por lo que **se debe** |

$$\boxed{\ \text{costo total promedio mensual} = \frac{\sum (K + iZ)}{n} + h\,\bar I^+ + \pi\,\bar I^-\ }$$

En las diapositivas el profe lo escribe como $C = iZ + k + pI^- + hI^+$.

> **Ojo:** $h$ va con $I^+$ y $\pi$ va con $I^-$. En $K + iZ$, $i$ es el costo por unidad y $Z$ la cantidad pedida. Un parcial resuelto de 2021 los tiene invertidos.

#### 5.4 Los cuatro eventos

| Prioridad | Evento | Qué hace |
|---|---|---|
| 1 | **Llegada de pedido** | suma $Z$ al inventario (si había backlog, lo cubre primero). No programa nada |
| 2 | **Demanda** | genera el tamaño $D$ y lo resta (puede quedar negativo). Programa la próxima demanda |
| 3 | **Fin de simulación** | en $t = n$ calcula los costos y reporta |
| 4 | **Evaluación** | si $I < s$, pide $Z = S - I$, paga $K + iZ$ y programa la llegada en $t + L$. Siempre programa la próxima evaluación en $t + 1$ |

Además hay una rutina que **no es evento**: la que actualiza las áreas bajo $I^+$ e $I^-$. Se llama antes de cada evento y mira el signo de $I$ **en el intervalo anterior**:

- si fue negativo, suma al área de $I^-$;
- si fue positivo, suma al área de $I^+$;
- si fue cero, no suma nada.

#### 5.5 La salida y la discusión de Law (§1.5.6)

Law simuló **9 políticas durante 120 meses**, con $I(0) = 60$, $K = 32$, $i = 3$, $h = 1$ y $\pi = 5$. Esta tabla está en las diapositivas del profe:

De ese informe Law saca cinco conclusiones. Se pueden tomar como verdadero/falso:

1. **Con $s = 20$ fijo, al subir $S$ de 40 a 100:**
   - **sube el mantenimiento** (de 9,25 a 36,00): se guarda más;
   - **baja el faltante** (de 18,10 a 7,95);
   - **baja el costo de pedido** (de 99,26 a 81,37): se piden lotes más grandes, menos veces, y se paga menos veces el fijo $K$.
2. **Con $S = 100$ fijo, al subir $s$ de 20 a 60:**
   - **baja el faltante** (de 7,95 a 0,24);
   - **sube el mantenimiento** (de 36,00 a 53,91): un $s$ más alto deja caer menos el inventario.
3. **La dirección** en que se mueve cada componente se podía prever sin simular, pero **la magnitud no**. Y como los componentes van en sentidos opuestos, **sin simular no se sabe ni para dónde va el total**.
4. **(20, 60) parece la mejor**, con **122,74 por mes**. Pero cada número es la estimación de **una sola corrida** (una muestra de tamaño 1) y tiene mucha varianza. Con otros números aleatorios, **el orden de las políticas podría cambiar**.
5. **Conclusión**: si la duración de la corrida está fijada por el problema (acá, 10 años), **una sola corrida por política no alcanza**. Cuántas hacen falta lo resuelve el cap. 9, que este año no entra.

Un dato más que puede caer: aun usando el mismo generador de números aleatorios, los resultados **cambiaron un poco entre lenguajes, compiladores y computadoras** (Law, apéndice 1C).

#### 5.6 El ejercicio numérico

**Consigna tipo** (2024 y 2025): "Determine el costo total promedio mensual para un sistema de inventario con la política vista en clase", con los datos y cinco números aleatorios.

1. **Armá los tres generadores** por transformada inversa (§9.2):
   - tiempo entre demandas: $-\text{media}\cdot\ln r$;
   - tamaño de la demanda: tramos de la acumulada;
   - demora: $a + (b-a)\,r$.
2. **Hacé una tabla de cada número $r$ en sus tres usos.** Todavía no sabés para qué se va a usar cada uno.
3. **Corré los eventos en orden.** En cada uno, acumulá las áreas con el **nivel anterior** y después actualizá.
4. **Cerrá con la fórmula** del recuadro de §5.3, dividiendo por la cantidad de **meses** y no por la cantidad de eventos.

> **Ojo:** en el enunciado de 2025, con los cinco números en orden, la corrida no llega a terminar el primer mes. `banco-preguntas.md` (Parte 3) lo resuelve con los dos supuestos posibles. Si te pasa algo así, **escribí el supuesto** que usás.

## Ampliación

### La diferencia con Investigación Operativa

Pregunta frecuente #9 del archivo, y es una pregunta conceptual linda porque conecta dos materias.

| | **Investigación Operativa** | **Simulación** |
|---|---|---|
| Control del inventario | **Continuo**: se vigila permanentemente | **Periódico**: se revisa al inicio de cada mes |
| Cuándo se pide | **Apenas** se toca el nivel mínimo | Recién en la **próxima revisión** |
| ¿Puede haber inventario negativo? | **No**: el pedido se dispara antes | **Sí**: entre dos revisiones la demanda puede superar el stock |
| Consecuencia | No hay backlog | Aparecen $I^-(t)$ y el **costo por faltante** |

> En una línea: *"en IO los pedidos se hacen inmediatamente cuando se llega al nivel mínimo, el
> control es constante; en el manejo de inventario de simulación el control es periódico, por lo
> que se pueden generar niveles negativos de inventario."*

### Errores y trampas

| # | Trampa | Lo correcto |
|---|---|---|
| 1 | Cambiar $h$ y $\pi$ | **$h$ de *holding*** va con $I^+$ (lo guardado); $\pi$ va con $I^-$ (lo adeudado) |
| 2 | Cambiar $i$ y $Z$ en $K + iZ$ | $i$ es el **costo** por unidad, $Z$ la **cantidad** pedida |
| 3 | Creer que $I^+$ e $I^-$ pueden ser negativos | Son máximos contra 0: **nunca** son negativos. El que puede ser negativo es $I(t)$ |
| 4 | Pedir $Z = S$ | Se pide $Z = S - I$: lo que **falta** para llegar al tope, no el tope |
| 5 | Cobrar costo de pedido cuando $Z = 0$ | Si no se pide, **no hay costo**, ni siquiera el fijo $K$ |
| 6 | Calcular el área con el nivel nuevo | Se usa el nivel que hubo **durante** el tramo, o sea el viejo |
| 7 | Olvidar que el pedido primero cubre el backlog | Al llegar, **primero** cancela $I^-$; el sobrante recién ahí suma a $I^+$ |
| 8 | Poner el fin de simulación como evento 4 | Va como **evento 3**, para que se ejecute antes que la evaluación en $t=n$ |

### La fórmula que tenés que escribir sí o sí

$$\text{CTPM} = \underbrace{\frac{\sum (K + iZ)}{n}}_{\text{pedido}} + \underbrace{h\,\frac{\int_0^n I^+(t)\,dt}{n}}_{\text{mantenimiento}} + \underbrace{\pi\,\frac{\int_0^n I^-(t)\,dt}{n}}_{\text{faltante}}$$

**Trampas**:

- El área de cada tramo se calcula con el nivel **anterior** al evento.
- Si $I\ge s$ no se paga ni siquiera $K$.
- El pedido llega en $t+L$.
- Cuando llega, primero cubre el backlog.
- Se divide por **meses**, no por eventos.
- $h$ va con $I^+$ y $\pi$ va con $I^-$.

### En el TP 3: Inventario (s, S) con revisión periódica

Se usan los parámetros de Law & Kelton:

- **Demanda:** Poisson de tasa 10 por unidad de tiempo, con tamaño {1, 2, 3, 4} y probabilidades {1/6, 1/3, 1/3, 1/6} (media 2,5).
- **Costos:** orden 32 fijo + 3 por unidad; mantenimiento h = 1 y faltante p = 5, ambos por unidad y por unidad de tiempo.
- **Lag de entrega:** Uniforme(0,5; 1).
- **Faltantes:** quedan como backorder (inventario negativo).
- **Grilla:** s ∈ {10…50} × S ∈ {40…90}, con 10 réplicas por política.

Los costos se calculan por unidad de tiempo: orden = Σ(K + c·Q)/T, mantenimiento = h·∫max(I, 0)/T y faltante = p·∫max(−I, 0)/T.

**Resultado:** la política óptima es **(s = 30, S = 60)**, con un costo total de ≈ 119,4. No hay fórmula cerrada para el óptimo, así que acá la comparación es Python contra AnyLogic.

| Costo con (30, 60) | Python | AnyLogic |
|---|---|---|
| Orden | 92,8 | 93,0 |
| Mantenimiento | 20,9 | 20,9 |
| Faltante | 5,7 | 5,4 |
| **Total** | **119,4** | **119,3** |

**Qué mostrar:** el mapa de calor, que muestra dónde está el óptimo, y el desglose, que explica por qué está ahí. Subir s baja el faltante pero sube el mantenimiento y la orden.

## Preguntas de parcial y de práctica sobre este tema

**1.3** (parcial 2025) **¿Qué representa la política (s, S)?**
A) ordenar fijo s al llegar a S · B) si $I<s$ pedir hasta S; si $I\ge s$ no pedir · C) pedir s cada S períodos · D) asegura que el inventario siempre está entre s y S · E) B y D

✅ **B.** D es falsa. Entre dos revisiones el inventario puede caer muy por debajo de $s$, y como hay backlog puede quedar **negativo**. La política no garantiza ningún rango. Tampoco es que se pidan $S$ unidades: se pide $Z = S - I$.
*Unidad 4, "Política de reordenamiento (s, S)".*

**P19** (práctica, no oficial) En el modelo de inventario, la **evaluación de inventario** ocurre: A) cada vez que hay una demanda · B) al principio de cada mes (revisión periódica) · C) cuando $I<s$, en el instante en que pasa · D) cuando llega un pedido · E) A y C

→ Respuesta: **B**. Control **periódico**. Por eso hay backlog. La C es el control continuo de IO.

**P20** (práctica, no oficial) En el modelo de inventario, si en $t=n$ coinciden fin de simulación y evaluación: A) se evalúa primero · B) se ejecuta primero el fin de simulación, para no hacer un pedido que no se va a contabilizar · C) da igual · D) se descartan los dos · E) A y C

→ Respuesta: **B**. Law ordena los eventos así: el fin es el tipo 3 y la evaluación el tipo 4.

**P28** (práctica, no oficial) V o F: en el modelo de inventario de Law, al aumentar $S$ con $s$ fijo, el costo de pedido promedio **baja**.

→ Respuesta: **V**. Lotes más grandes, menos pedidos y el fijo $K$ se paga menos veces (de 99,26 a 81,37).

**P29** (práctica, no oficial) En la salida de Law, la política (20, 60) tuvo el menor costo (122,74). La conclusión correcta es: A) es la política óptima · B) es la mejor solo si se repite la corrida con la misma semilla · C) es una estimación de una sola corrida y otra corrida podría cambiar el orden · D) las 9 políticas cuestan lo mismo · E) A y B

→ Respuesta: **C**. Es la conclusión de Law en §1.5.6.

**P30** (práctica, no oficial) Sin simular, en el modelo de inventario se puede prever: A) la magnitud de cada componente de costo · B) la dirección en que se mueve cada componente, pero no su magnitud · C) cuál es la política óptima · D) nada · E) A y C

→ Respuesta: **B**. Sin simular se prevé la dirección, pero no la magnitud. Y el total tampoco.
