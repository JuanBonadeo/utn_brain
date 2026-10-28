# DEFENSA DEL TPI — JUNTAS DE MOTOR

**Investigación Operativa · Comisión 402 · Grupo 1**

Resumen de las tres etapas y posibles preguntas con su respuesta. Los importes del modelo de producción están en miles de pesos y los de stock en pesos.

## Etapa 1 · Qué hicimos

**El problema.** Una autopartista fabrica tres juntas de corcho para motores. Hay que decidir cuántos lotes fabricar por semana para maximizar el beneficio. Un lote son 100 juntas.

**Variables.** X₁ = lotes de tapa de cilindros, X₂ = lotes de cárter, X₃ = lotes de múltiple.

**Modelo.** Max Z = 50 X₁ + 30 X₂ + 40 X₃

| Restricción | Ecuación | Tipo |
| --- | --- | --- |
| R1 · Corcho (m²) | 3X₁ + 2X₂ + X₃ ≤ 600 | Oferta |
| R2 · Horas de troqueladora | 4X₁ + 3X₂ + 2X₃ ≤ 480 | Oferta |
| R3 · Mínimo contractual (lotes totales) | X₁ + X₂ + X₃ ≥ 150 | Demanda |
| R4 · Capacidad de despacho | X₁ + X₂ + 2X₃ ≤ 200 | Capacidad |

**Resolución.** Usamos Simplex con Big M. A4, A5 y A6 son las holguras de R1, R2 y R4. A7 es el exceso de R3 y A8 su artificial, con costo −M. Hicieron falta tres iteraciones:

| Iteración | Entra | Sale | Qué pasa |
| --- | --- | --- | --- |
| I0 → I1 | A1 (tapa) | A5 (horas) | Tapa es la que más aporta. Las horas alcanzan para 120 lotes. |
| I1 → I2 | A3 (múltiple) | A6 (despacho) | Faltan 30 lotes para el mínimo. Múltiple es la que da más lotes por hora. |
| I2 → I3 | A2 (cárter) | A8 (artificial) | Faltan 3,3 lotes y solo el cárter puede completarlos. |

**Solución óptima.** X* = (80; 20; 50) lotes y Z* = 6600, o sea **$6.600.000 por semana**. Sobran 270 m² de corcho. Las horas, el despacho y el mínimo contractual quedan justos (activos).

**Conclusión.** Los cuellos de botella son las horas de troqueladora y el despacho. El corcho no limita la producción.

**Escenario alternativo (faltó en la entrega).** Si se rompe una troqueladora y quedan 440 horas, el plan pasa a (40; 60; 50) y el beneficio a $5.800.000, $800.000 menos. Conviene tercerizar horas si cada una cuesta menos de $20.000.

## Etapa 1 · Preguntas

**1) ¿Qué escenario alternativo analizarían?**

El de la troqueladora: las horas bajan de 480 a 440. Como 440 está dentro del rango de la base (400 a 500), no hace falta rehacer el Simplex. Se usa la columna de A5 de la tabla final:

- X₁ = 80 + Δ = 40
- X₂ = 20 − Δ = 60
- X₃ = 50
- Sobrante de corcho = 270 − Δ = 310
- Z = 6600 + 20 · (−40) = 5800

Se pasa producción de tapa a cárter. Otro escenario posible: si la terminal sube el mínimo a 160 lotes, Z baja a 6000. Conviene aceptarlo solo si la terminal paga al menos $60.000 por cada lote extra.

**2) ¿Cómo llevaron el modelo a forma estándar?**

A las restricciones de tipo ≤ (R1, R2 y R4) les sumamos una holgura: X₄, X₅ y X₆. A R3, que es de tipo ≥, le restamos un exceso (X₇) y le sumamos una artificial (X₈), que en la función objetivo lleva −M.

- X₄: m² de corcho que sobran.
- X₅: horas de troqueladora sin usar.
- X₆: capacidad de despacho sin usar.
- X₇: lotes por encima del mínimo del contrato.
- X₈: no tiene significado en el problema, sirve solo para arrancar.

**3) ¿Por qué hace falta la variable artificial? (clave)**

El Simplex necesita arrancar con una variable básica en cada fila, con coeficiente +1 y valor ≥ 0. En R1, R2 y R4 eso lo da la holgura. En R3 el exceso tiene coeficiente −1: si fuera básica valdría −150, y eso no se puede. Por eso se agrega la artificial X₈, que al arrancar vale 150.

Como X₈ no existe en la realidad, se la penaliza con −M para que el método la saque de la base. En la resolución se ve: la artificial valía 30 en I1 y 3,3 en I2, que eran los lotes que faltaban para cumplir el contrato. Salió en I3, cuando entró el cárter.

**4) ¿Por qué la artificial lleva −M y no +M? ¿Qué pasa si no sale de la base?**

Lleva −M porque maximizamos, y así la artificial empeora mucho la Z. En un problema de mínimo sería +M.

Si al final la artificial sigue en la base con valor positivo, el problema no tiene solución factible. Si queda en la base pero con valor 0, la solución es factible y degenerada. En nuestro caso salió de la base, así que la solución es factible.

**5) ¿Hay otra forma de resolverlo además de Big M?**

Sí, el método de las dos fases. En la fase 1 se minimiza la suma de las artificiales para encontrar una base factible. En la fase 2 se sacan las artificiales y se optimiza la Z original. Llega al mismo resultado sin trabajar con M.

**6) ¿Cómo saben que la tabla final es óptima? ¿La solución es única?**

Es óptima porque todos los Cj − Zj son ≤ 0 (es un máximo) y la artificial salió de la base, así que la solución es factible. Es única porque ninguna variable no básica tiene Cj − Zj = 0.

**8) ¿Por qué queda activo un mínimo si estamos maximizando?**

Porque el mínimo obliga a fabricar cárter, que es el producto que menos rinde por hora de troqueladora:

- Cárter: 30/3 = 10 por hora.
- Tapa: 50/4 = 12,5 por hora.
- Múltiple: 40/2 = 20 por hora.

Si el mínimo bajara, el modelo dejaría de fabricar cárter y ganaría más. Por eso su precio sombra es negativo: cada lote más de contrato cuesta $60.000.

**9) En la Etapa 1 dicen que el despacho vale $90.000 y en la Etapa 2, $30.000. ¿Cuál es el correcto?**

$30.000. La fila Zj de la tabla final tiene un error de cuenta en A6: 50·1 + 30·(−2) + 40·1 = 30, no 90. Se comprueba con el dual: 480·20 + 200·30 − 150·60 = 6600 = Z*. Con 90 daría 18.600.

**10) ¿Por qué el Cj − Zj de A7 es −60 y no −M−60?**

Porque A7 es la variable de exceso y su costo es 0, así que 0 − 60 = −60. La M va en la artificial A8: su Cj − Zj es −M + 60. En el documento estas dos casillas estaban mal.

**11) El texto dice "mínimo de juntas de tapa de cilindros", pero la restricción suma los tres productos.**

Es un error de redacción. El contrato es por 150 lotes totales, como está en la Etapa 2.

**12) ¿Por qué X₃ cuenta doble en el despacho?**

⚠️ Acordar la respuesta con el grupo, porque no está justificado en el documento. Una respuesta posible: la junta de múltiple ocupa el doble de volumen de embalaje por lote.

## Etapa 2 · Qué hicimos

**Modelo dual.** Min W = 600u₁ + 480u₂ + 150u₃ + 200u₄

| Restricción dual | Viene de |
| --- | --- |
| 3u₁ + 4u₂ + u₃ + u₄ ≥ 50 | X₁ |
| 2u₁ + 3u₂ + u₃ + u₄ ≥ 30 | X₂ |
| u₁ + 2u₂ + u₃ + 2u₄ ≥ 40 | X₃ |

u₁, u₂, u₄ ≥ 0 y u₃ ≤ 0, porque R3 es de tipo ≥. Solución: u* = (0; 20; −60; 30) y W* = 6600 = Z*.

En la presentación el orden era distinto: U₃ era el despacho y U₄ el mínimo.

**Precios sombra.**

| Recurso | Precio sombra | Rango donde vale |
| --- | --- | --- |
| Corcho | $0 (sobra) | 330 m² en adelante |
| Horas de troqueladora | $20.000 por hora | 400 a 500 h |
| Mínimo contractual | −$60.000 por lote | 146,7 a 170 lotes |
| Despacho | $30.000 por unidad | 150 a 210 |

**Cambio en la ganancia del cárter (C₂).** El rango es −∞ < ΔC₂ ≤ 10, así que −∞ < C₂ ≤ 40. Con C₂ = 35 el plan no cambia y Z sube a 6700. Con C₂ = 42 hay que reoptimizar: el plan pasa a (0; 140; 30) y Z = 7080.

**Cambio en las horas (b₂).** El rango es −80 ≤ Δ ≤ 20, así que 400 ≤ b₂ ≤ 500. Con 500 horas el plan pasa a (100; 0; 50) y Z = 7000.

**Producto nuevo: junta de bomba de agua.** Su costo de oportunidad es 0·2 + 20·3 + 30·2 − 60·1 = 60. Como deja 45, su costo reducido es 45 − 60 = −15: no conviene.

**Programación entera (mochila).** Cuatro pedidos especiales para usar los 270 m² de corcho que sobran, con variables Y₁ a Y₄ que valen 0 o 1. Se resolvió con Branch and Bound:

- La relajación da 349, que es la cota superior.
- La rama Y₃ = 0 da la solución entera 345, con los pedidos 1, 2 y 4.
- Las ramas de Y₃ = 1 dan cotas de 332 y 344, menores que 345, así que se podan.

Óptimo: aceptar los pedidos 1, 2 y 4, por **$345.000 más por semana**.

**Conclusión (faltó en el documento).** Las horas y el despacho valen la pena de ampliar solo si cuestan menos que su precio sombra. El corcho sobrante se aprovecha con los pedidos especiales. La bomba de agua no conviene salvo que deje más de $60.000 por lote.

## Etapa 2 · Preguntas

**1) Escriban el dual. ¿Por qué u₃ es ≤ 0?**

El primal es de máximo, así que el dual es de mínimo. Las reglas:

- Cada restricción del primal da una variable dual. Las de tipo ≤ dan una variable ≥ 0 y la de tipo ≥ da u₃ ≤ 0.
- Cada variable del primal da una restricción dual de tipo ≥.
- Los términos independientes del primal (600, 480, 150, 200) pasan a la función objetivo, y las ganancias (50, 30, 40) a los términos independientes del dual.

Otra forma: multiplicar R3 por −1 para que quede de tipo ≤ (−X₁ − X₂ − X₃ ≤ −150). Así la variable dual queda ≥ 0 y en W aparece −150u₃'.

**2) ¿Qué son los costos marginales? (el profe marcó que faltaron)**

Es lo que "cuestan" en recursos escasos los productos que fabricamos. Si un producto se fabrica, el valor de lo que consume (a precio sombra) tiene que ser igual a lo que aporta:

- Tapa: 20·4 − 60·1 + 30·1 = 50 = C₁
- Cárter: 20·3 − 60·1 + 30·1 = 30 = C₂
- Múltiple: 20·2 − 60·1 + 30·2 = 40 = C₃

Por eso los tres tienen costo reducido 0 y las holguras duales son 0.

**3) ¿Qué significa que la hora de troqueladora valga $20.000?**

Es lo máximo que conviene pagar por una hora extra, por encima de lo que ya cuesta. Vale de a un cambio por vez y entre 400 y 500 horas.

**4) Escriban bien el rango de C₂.**

Primero se despeja la variación y después se suma el valor original, sin mezclarlos:

- Variación: −∞ < ΔC₂ ≤ 10
- Coeficiente: −∞ < C₂ ≤ 40

El error del documento fue mezclar Δ y C₂ en el mismo intervalo.

**5) ¿Por qué C₂ no tiene cota inferior?**

Porque sin cárter no se puede cumplir el contrato. Con X₂ = 0, las restricciones R3 y R4 obligan a X₃ ≤ 50, y R3 y R2 obligan a X₃ ≥ 60: es imposible. El cárter se fabrica aunque deje poca ganancia.

**6) Hagan el rango de b₂ paso a paso.**

Con b₂ = 480 + Δ, todas las variables básicas tienen que seguir siendo ≥ 0:

- X₁ = 80 + Δ ≥ 0, entonces Δ ≥ −80
- X₂ = 20 − Δ ≥ 0, entonces −Δ ≥ −20, y al multiplicar por −1 **se da vuelta**: Δ ≤ 20
- Sobrante de corcho = 270 − Δ ≥ 0, entonces Δ ≤ 270

De las cotas superiores se queda la menor (20) y de las inferiores la mayor (−80). Resultado: 400 ≤ b₂ ≤ 500. El error del documento fue no dar vuelta la desigualdad.

**7) ¿Con qué ganancia convendría la bomba de agua?**

Con más de $60.000 por lote, que es su costo de oportunidad. Si pasa eso, entra a la base y hay que reoptimizar.

**8) ¿Por qué la relajación es una cota superior? ¿Cuándo se poda una rama?**

La relajación permite más soluciones que el problema entero, así que su óptimo no puede ser peor. Una rama se poda cuando su cota es menor o igual que la mejor solución entera encontrada (345).

**9) ¿Los pedidos especiales no usan horas ni despacho, que están agotados?**

Es un supuesto del submodelo: se atienden con capacidad aparte. Si usaran horas o despacho, habría que agregarlos al modelo original como variables binarias.

## Etapa 3 · Qué hicimos

**Insumo elegido.** El corcho. La demanda sale del plan óptimo: 330 m² por semana × 52 = **17.160 m² por año**. Sumamos el sellador porque comparte el depósito con el corcho.

**1. Descuento por cantidad.** El metro cuadrado cuesta $2.500, o $2.350 si se piden 2.000 m² o más. Cada pedido cuesta $45.000 y mantener stock cuesta el 28 % anual del precio.

- Con el precio con descuento, Q* = 1.532 m². No llega a 2.000, así que hay que comparar dos opciones.
- Precio normal: Q* = 1.485 m², con un costo anual de $43.939.716.
- Pedir justo 2.000 m² con descuento cuesta $41.370.100 por año.
- Por costo conviene el descuento: ahorra unos $2.570.000 por año.

**2. Restricción de espacio.** El depósito tiene 60 m³ y el corcho ocupa 0,05 m³ por m². Con los lotes sin restricción se necesitan 80,4 m³, así que no entran. Se resolvió con Lagrange. Para cada insumo queda Q = √(2·D·L / (C·i + 2·λ·v)), donde v es el espacio que ocupa cada unidad.

- Con λ = $5.820 por m³ el depósito queda justo lleno.
- Lotes: 1.098 m² de corcho y 255 L de sellador.
- El lote de 2.000 m² ocupa 100 m³. Para aprovechar el descuento hay que ampliar el depósito a unos 106 m³.

**3. Demanda aleatoria.** La demanda diaria es de 47 m² con un desvío de 8, y el proveedor tarda 10 días en entregar. Con un 5 % de riesgo de faltante (z = 1,645):

- Stock de seguridad: SS = 1,645 · 8 · √10 = **42 m²**
- Punto de pedido: PP = 470 + 42 = **512 m²**

**Política final.** Cuando el stock baja a 512 m², pedir 1.098 m² de corcho. Son unos 15,6 pedidos por año, uno cada 23 días.

## Etapa 3 · Preguntas

**1) ¿Cuál es la inconsistencia del modelo aleatorio? (lo que marcó el profe)**

El stock de seguridad no entra en el depósito. El lote de 1.098 m² se calculó para llenar justo los 60 m³. Pero cuando llega un pedido, en el depósito hay lote más stock de seguridad: 0,05 · (1.098 + 42) + 0,02 · 255 = 62,1 m³, más que los 60 disponibles.

La corrección es reservar el lugar del stock de seguridad y volver a calcular con Lagrange con 60 − 2,1 = 57,9 m³:

| | Antes | Corregido |
| --- | --- | --- |
| Lote de corcho | 1.098 m² | 1.059 m² |
| Lote de sellador | 255 L | 249 L |
| λ | $5.820 | $6.775 |
| Espacio total con SS | 62,1 m³ | 60 m³ |
| Punto de pedido | 512 m² | 512 m² |

Cuesta solo $13.000 más por año y la política entra en el depósito.

**2) ¿Y si se aceptan los pedidos especiales de la Etapa 2?**

El consumo de corcho sube a 600 m² por semana, justo el máximo que entrega el proveedor. El corcho deja de sobrar y pasa a ser un recurso limitante. Igual el depósito sigue limitando el lote (unos 1.100 m²), así que la conclusión no cambia.

**3) ¿Por qué se compara con exactamente 2.000 m² y no con un lote mayor?**

Porque con el precio con descuento el mínimo de costo está en 1.532 m². Por encima de 2.000 el costo sube a medida que el lote se aleja de ese mínimo, así que el mejor lote con descuento es el propio umbral.

**4) ¿Por qué en el descuento se suma el costo de compra y en Lagrange no?**

En el descuento el precio depende del tamaño del lote, así que D·C cambia la decisión. En Lagrange el precio es fijo y D·C es una constante que no mueve el lote óptimo.

**5) ¿Qué significa λ? ¿Por qué el tope para ampliar ($56.750 por m³) es mayor que λ?**

λ es cuánto bajaría el costo anual con 1 m³ más de depósito. El tope es mayor porque ampliar 46 m³, además de dar espacio, habilita el salto de precio del descuento, y λ no captura ese salto.

**6) ¿Por qué no hay stock de seguridad en los modelos determinísticos?**

Porque la demanda y el plazo de entrega se conocen con certeza: el pedido llega justo cuando se termina el stock.

**7) ¿Por qué el modelo aleatorio usa el lote del modelo con restricción?**

Porque la aleatoriedad cambia cuándo pedir (el punto de pedido), no cuánto. Y el lote restringido es el único que entra en el depósito.

**8) Si el plan de la Etapa 1 es fijo, ¿por qué la demanda es aleatoria?**

Los 330 m² por semana son el promedio planificado. Lo que varía semana a semana es el mix real de pedidos. El desvío de 8 m² es un supuesto: si fuera mayor, el stock de seguridad crecería en la misma proporción.
