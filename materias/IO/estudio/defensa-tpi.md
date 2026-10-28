# DEFENSA DEL TPI — JUNTAS DE MOTOR

**Investigación Operativa · Comisión 402 · Grupo 1**

Resumen de las tres etapas explicado con palabras simples, y posibles preguntas con su respuesta. Los importes del modelo de producción están en miles de pesos y los de stock en pesos.

## Etapa 1 · Qué hicimos

**El problema.** Una autopartista fabrica tres tipos de juntas de corcho para motores. Tenemos que decidir **cuántos lotes de cada una fabricar por semana para ganar lo máximo posible**. Un lote son 100 juntas.

**Las variables** son las decisiones:

- X₁ = lotes de juntas de tapa de cilindros (gana 50 por lote)
- X₂ = lotes de juntas de cárter (gana 30 por lote)
- X₃ = lotes de juntas de múltiple (gana 40 por lote)

**El modelo.** Queremos Max Z = 50 X₁ + 30 X₂ + 40 X₃, respetando cuatro límites:

| Restricción | Ecuación | Qué dice |
| --- | --- | --- |
| R1 · Corcho | 3X₁ + 2X₂ + X₃ ≤ 600 | No hay más de 600 m² de corcho por semana |
| R2 · Horas | 4X₁ + 3X₂ + 2X₃ ≤ 480 | La troqueladora tiene 480 horas por semana |
| R3 · Contrato | X₁ + X₂ + X₃ ≥ 150 | Hay que entregar al menos 150 lotes en total |
| R4 · Despacho | X₁ + X₂ + 2X₃ ≤ 200 | Se pueden despachar hasta 200 unidades |

Los números de la derecha (600, 480, 150 y 200) son los **bᵢ**. Tres son cosas que tenemos (recursos, ≤) y uno es algo que nos exigen (el contrato, ≥).

**Paso 1: forma estándar.** El Simplex trabaja con igualdades, así que a cada restricción le agregamos una variable que "rellena" la diferencia:

- A R1, R2 y R4 les sumamos una **holgura** (X₄, X₅, X₆). La holgura es lo que sobra del recurso.
- A R3 le restamos un **exceso** (X₇), que son los lotes por encima del mínimo.
- A R3 también le sumamos una **artificial** (X₈), que en la función objetivo lleva −M.

**¿Por qué la artificial?** El Simplex arranca sin fabricar nada. En las ≤ eso funciona: la holgura vale todo el recurso. Pero sin fabricar nada no cumplimos el contrato de 150 lotes, y el exceso valdría −150, que no se puede. Entonces agregamos una variable "trucha" que hace de cuenta que cumple el contrato. Como no existe en la realidad, la castigamos con −M (una pérdida enorme) para que el método la eche.

**Paso 2: las iteraciones.** En cada paso entra la variable que más mejora la ganancia (mayor Cj − Zj positivo) y sale la que primero llega a 0 (menor cociente Xi / Yij).

| Paso | Entra | Sale | Qué pasa en el problema |
| --- | --- | --- | --- |
| I0 → I1 | Tapa (A1) | Holgura de horas (A5) | Tapa es la que más gana. Con 480 horas alcanza para 120 lotes. La trucha todavía vale 30: faltan 30 lotes para el contrato. |
| I1 → I2 | Múltiple (A3) | Holgura de despacho (A6) | Entra múltiple, que da más lotes por hora. Ya se agotaron horas y despacho, y la trucha vale 3,3: todavía faltan 3,3 lotes. |
| I2 → I3 | Cárter (A2) | Artificial (A8) | Solo el cárter puede completar los lotes que faltan. Entra porque lo exige el contrato, no porque convenga: en pesos su Cj − Zj era −10. |

**Paso 3: la tabla final.**

| Base | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | Xi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A4 | 0 | 0 | 0 | 1 | −1 | 0 | −1 | 1 | 270 |
| A1 | 1 | 0 | 0 | 0 | 1 | 1 | 4 | −4 | 80 |
| A2 | 0 | 1 | 0 | 0 | −1 | −2 | −6 | 6 | 20 |
| A3 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | −1 | 50 |
| **Zj** | 50 | 30 | 40 | 0 | 20 | 30 | 60 | −60 | **Z = 6600** |
| **Cj − Zj** | 0 | 0 | 0 | 0 | −20 | −30 | −60 | −M+60 | |

Es **óptima** porque ningún Cj − Zj es positivo: no hay forma de mejorar. Es **factible** porque la trucha salió de la base.

**La solución.** Fabricar 80 lotes de tapa, 20 de cárter y 50 de múltiple. Se ganan **$6.600.000 por semana**. Sobran 270 m² de corcho. Las horas, el despacho y el contrato quedan justos.

**Conclusión.** Lo que frena a la fábrica son las horas de troqueladora y el despacho. El corcho sobra.

**Escenario alternativo (faltó en la entrega).** Si se rompe una troqueladora y quedan 440 horas, se pierden 40 horas × 20 mil = 800 mil. El plan pasa a 40 de tapa, 60 de cárter y 50 de múltiple, y la ganancia a $5.800.000. Conviene tercerizar horas si cada una cuesta menos de $20.000.

## Etapa 1 · Preguntas

**1) ¿Qué escenario alternativo analizarían?**

Imaginar "¿qué pasa si…?" y ver cómo cambia el plan. Si se rompe una máquina y hay 440 horas en vez de 480, tenemos 40 horas menos y cada una vale 20 mil: perdemos 800 mil, y la Z baja a 5800. Como 440 está dentro del rango de 400 a 500 horas, no hace falta rehacer el Simplex. Con menos horas se fabrica menos tapa, que gasta 4 horas por lote, y más cárter: el plan queda en 40, 60 y 50. Otro ejemplo: si la terminal pide 160 lotes en vez de 150, perdemos 60 mil por cada lote extra. Conviene aceptarlo solo si nos pagan al menos eso.

**2) ¿Cómo llevaron el modelo a forma estándar?**

El Simplex solo trabaja con igualdades. A cada ≤ le sumamos una holgura, que es lo que sobra del recurso: si de 600 m² usamos 330, la holgura vale 270. A la ≥ le restamos un exceso y le sumamos una artificial con −M.

**3) ¿Por qué hace falta la variable artificial? (clave)**

El Simplex necesita un punto de partida, y arranca sin fabricar nada. En las ≤ eso es válido. En la del contrato no: sin fabricar nada no se cumplen los 150 lotes, y el exceso valdría −150, que no se puede. Entonces inventamos una variable "trucha" que hace de cuenta que cumple el contrato. Como es trucha, la castigamos con −M para que el método la eche. En las tablas se ve: valía 30 en I1 y 3,3 en I2, que eran los lotes que faltaban. Salió en I3, cuando entró el cárter.

**4) ¿Por qué la artificial lleva −M y no +M? ¿Qué pasa si no sale?**

Como buscamos ganar lo máximo, a la trucha le ponemos una pérdida enorme y el método la quiere sacar sí o sí. En un problema de mínimo sería al revés: +M. Si aun así no se puede sacar (queda en la base con valor positivo), no hay forma real de cumplir todas las restricciones a la vez: el problema no tiene solución. Si queda en la base pero con valor 0, la solución es válida y se llama degenerada.

**5) ¿Hay otra forma de resolverlo además de Big M?**

Sí, el método de las dos fases. Primero solo te ocupás de echar a las truchas, y después recién buscás la mejor ganancia. Llega al mismo resultado.

**6) ¿Cómo saben que la tabla final es óptima? ¿La solución es única?**

En la fila Cj − Zj ningún número es positivo. Eso quiere decir que meter cualquier variable que hoy vale 0 bajaría la ganancia. Es única porque ninguna variable fuera de la base tiene un 0 en esa fila. Si lo hubiera, existiría otro plan que gana lo mismo.

**7) ¿Por qué el contrato queda justo si queremos ganar lo máximo?**

El cárter es el que menos rinde: 10 por hora, contra 12,5 de la tapa y 20 del múltiple. Si pudiéramos elegir, no lo fabricaríamos. Pero el contrato obliga a hacer 150 lotes en total, y con las horas y el despacho que hay solo se llega metiendo algo de cárter. **El contrato nos obliga a fabricar algo que no conviene.** Por eso cada lote más de contrato cuesta 60 mil, y su precio sombra es negativo.

**8) En la Etapa 1 el despacho vale $90.000 y en la Etapa 2, $30.000. ¿Cuál es el correcto?**

$30.000. Fue un error de cuenta en la fila Zj de A6: 50·1 + 30·(−2) + 40·1 = 30, no 90. Para comprobarlo, se multiplica cada recurso por su precio y se suma: 480·20 + 200·30 − 150·60 = 6600, que es la ganancia. Con 90 no da.

**9) ¿Por qué el Cj − Zj de A7 es −60 y no −M−60?**

La M solo va pegada a la trucha (A8), y por eso su casilla es −M + 60. A7 es el exceso, una variable normal que cuesta 0, así que su número no lleva M: es 0 − 60 = −60. En el documento esas dos casillas estaban mal.

**10) El texto dice "mínimo de juntas de tapa de cilindros", pero la restricción suma los tres productos.**

Es un error de redacción. El contrato es por 150 lotes en total, de cualquier tipo.

**11) ¿Por qué X₃ cuenta doble en el despacho?**

⚠️ Acordar la respuesta con el grupo, porque el documento no lo justifica. Una respuesta posible: cada lote de múltiple ocupa el doble de lugar al despachar.

## Etapa 2 · Qué hicimos

**La idea del dual.** El primal pregunta **cuánto fabricar** para ganar lo máximo. El dual mira lo mismo desde los recursos y pregunta **cuánto vale cada recurso**. Sus variables (u₁, u₂, u₃, u₄) son los **precios sombra**: cuánto ganaríamos con una unidad más de cada recurso.

**Cómo se arma el dual, paso a paso:**

1. Una variable dual por cada restricción del primal: u₁ corcho, u₂ horas, u₃ contrato, u₄ despacho.
2. El primal es de máximo, así que el dual es de mínimo. Los bᵢ pasan a la función objetivo: Min W = 600u₁ + 480u₂ + 150u₃ + 200u₄.
3. Una restricción dual por cada producto. Se lee la matriz del primal por columnas y la ganancia va a la derecha:

| Restricción dual | Producto | Qué dice |
| --- | --- | --- |
| 3u₁ + 4u₂ + u₃ + u₄ ≥ 50 | Tapa | Los recursos que gasta un lote de tapa valen al menos 50 |
| 2u₁ + 3u₂ + u₃ + u₄ ≥ 30 | Cárter | Los recursos que gasta un lote de cárter valen al menos 30 |
| u₁ + 2u₂ + u₃ + 2u₄ ≥ 40 | Múltiple | Los recursos que gasta un lote de múltiple valen al menos 40 |

4. Los signos: u₁, u₂, u₄ ≥ 0 y u₃ ≤ 0. Las ≤ son recursos que tenemos: conseguir más nunca perjudica, así que su precio es ≥ 0. La ≥ es una obligación: que nos exijan más solo puede perjudicar, así que su precio es ≤ 0.

**La solución del dual se lee en la tabla final del primal**, en la fila Cj − Zj de las holguras, con el signo cambiado: u* = (0; 20; −60; 30). Comprobación: 480·20 + 200·30 − 150·60 = 6600 = Z*. El primal y el dual siempre dan lo mismo.

En la presentación el orden era distinto: U₃ era el despacho y U₄ el contrato. Aclararlo si se escribe en el pizarrón.

**Qué significa cada precio sombra:**

| Recurso | Precio sombra | En criollo | Vale entre |
| --- | --- | --- | --- |
| Corcho | $0 | Sobra, así que más corcho no sirve | 330 m² en adelante |
| Horas | $20.000 | Una hora más nos hace ganar 20 mil | 400 y 500 h |
| Contrato | −$60.000 | Un lote más de contrato nos hace perder 60 mil | 146,7 y 170 lotes |
| Despacho | $30.000 | Una unidad más de despacho nos hace ganar 30 mil | 150 y 210 |

**Cambio en la ganancia del cárter.** ¿Hasta dónde puede cambiar sin que cambie el plan? Puede subir hasta 10 (o sea, ganar hasta 40) y puede bajar todo lo que quiera. Si gana 35, el plan sigue igual y la Z sube a 6700. Si gana 42, conviene otro plan: 0 de tapa, 140 de cárter y 30 de múltiple, con Z = 7080.

**Cambio en las horas.** Entre 400 y 500 horas se fabrican los mismos tres productos, aunque en distintas cantidades. Con 500 horas: 100 de tapa, 0 de cárter y 50 de múltiple, con Z = 7000.

**Producto nuevo: junta de bomba de agua.** Un lote gasta recursos que valen 0·2 + 20·3 + 30·2 − 60·1 = 60 mil, y solo gana 45 mil. Perderíamos 15 mil por lote respecto a usar esos recursos en lo que ya fabricamos: no conviene.

**Programación entera (mochila).** Con los 270 m² de corcho que sobran podemos aceptar pedidos especiales. Cada pedido se acepta entero o no se acepta (variables de 0 o 1). Lo resolvimos con Branch and Bound:

- Primero hicimos de cuenta que se podían aceptar pedazos de pedido. Eso da 349: un techo.
- Separamos en dos casos según el pedido 3. Sin el pedido 3, aceptando el 1, el 2 y el 4, se usan los 270 m² y se gana 345.
- Con el pedido 3, los techos dan 332 y 344. Son menores que 345, así que por ahí no se puede mejorar y se descartan.

Resultado: aceptar los pedidos 1, 2 y 4, que dan **$345.000 más por semana**.

**Conclusión (faltó en el documento).** Ampliar horas o despacho conviene solo si cuesta menos que su precio sombra. El corcho que sobra se aprovecha con los pedidos especiales. La bomba de agua no conviene salvo que gane más de $60.000 por lote.

## Etapa 2 · Preguntas

**1) Escriban el dual. ¿Por qué u₃ es ≤ 0?**

Se arma con los cuatro pasos de arriba. u₃ es ≤ 0 porque el contrato es una obligación: que nos exijan más solo nos puede perjudicar. Si te piden la forma simétrica, se multiplica R3 por −1 para que quede ≤ (−X₁ − X₂ − X₃ ≤ −150). Así la variable queda ≥ 0 y en W aparece −150.

**2) ¿Qué son los costos marginales? (el profe marcó que faltaron)**

Si fabricamos un producto, lo que gana tiene que ser exactamente igual a lo que valen los recursos que gasta. Si ganara menos, no convendría fabricarlo; si ganara más, convendría fabricar todavía más. Con la tapa: gasta 4 horas (4·20 = 80), 1 de despacho (30) y cuenta 1 para el contrato (−60). En total 80 + 30 − 60 = 50, justo lo que gana. Lo mismo da 30 para el cárter y 40 para el múltiple.

**3) ¿Qué significa que una hora valga $20.000?**

Es lo máximo que conviene pagar por una hora extra, además de lo que ya cuesta. Si alguien nos alquila una hora a 15 mil, la tomamos y ganamos 5 mil. Si nos la cobra 25 mil, no conviene. Vale solo hasta 500 horas; más allá el valor cambia.

**4) Escriban bien el rango de la ganancia del cárter.**

Son dos cosas distintas y van por separado. Δ es cuánto cambia la ganancia: −∞ < ΔC₂ ≤ 10. C₂ es la ganancia: −∞ < C₂ ≤ 40. El error del documento fue mezclarlas en la misma línea.

**5) ¿Por qué la ganancia del cárter no tiene piso?**

Aunque el cárter dejara de ganar plata, igual habría que fabricarlo, porque sin cárter es imposible cumplir el contrato con las horas y el despacho que hay. Entonces bajar su ganancia nunca cambia el plan, solo baja la Z.

**6) Hagan el rango de las horas paso a paso.**

Si cambian las horas, cambian las cantidades, y ninguna puede quedar negativa:

- Tapa: 80 + Δ ≥ 0, entonces Δ ≥ −80
- Cárter: 20 − Δ ≥ 0, entonces −Δ ≥ −20, y al multiplicar por −1 **se da vuelta el signo**: Δ ≤ 20
- Corcho que sobra: 270 − Δ ≥ 0, entonces Δ ≤ 270

Nos quedamos con lo más exigente: −80 ≤ Δ ≤ 20, o sea, entre 400 y 500 horas. El error del documento fue no dar vuelta el signo.

**7) ¿Con qué ganancia convendría la bomba de agua?**

Los recursos que gasta un lote valen 60 mil. Conviene recién si gana más de 60 mil. En ese caso habría que volver a resolver para saber cuánto fabricar.

**8) ¿Qué es la relajación y cuándo se poda una rama?**

La relajación es hacer de cuenta que se pueden aceptar pedazos de un pedido. Como es más libre que la realidad, nunca da menos que la mejor solución real: es un techo. Podar es dejar de explorar una rama: si su techo es 344 y ya tenemos una solución real de 345, por ese lado nunca vamos a mejorar.

**9) ¿Los pedidos especiales no usan horas ni despacho, que están agotados?**

Es un supuesto: se hacen con otra capacidad, por ejemplo un turno extra. Si usaran las horas que ya están agotadas, habría que meterlos en el modelo grande.

## Etapa 3 · Qué hicimos

**Qué insumo y por qué.** Elegimos el corcho porque lo usan las tres juntas. Por semana usamos 330 m², así que al año son 330 × 52 = **17.160 m²**. Sumamos el sellador porque comparte el depósito con el corcho. Cada modelo responde una pregunta distinta.

**1. Descuento por cantidad: ¿cuánto conviene pedir?** El m² cuesta $2.500, pero si pedimos 2.000 m² o más baja a $2.350. Cada pedido cuesta $45.000 y guardar el corcho cuesta el 28 % anual de su precio. La tensión es esta: pedir mucho de una vez ahorra pedidos y da descuento, pero hay que pagar por guardarlo.

- Con el precio con descuento, el lote ideal sería 1.532 m². No llega a 2.000, así que el descuento no sale solo: hay que comparar.
- Sin descuento, el lote ideal es 1.485 m² y cuesta $43.939.716 por año.
- Pidiendo 2.000 m² con descuento cuesta $41.370.100 por año.
- Por plata conviene el descuento: ahorra unos $2.570.000 por año.

**2. Restricción de espacio: ¿entra en el depósito?** El depósito tiene 60 m³ y cada m² de corcho ocupa 0,05 m³. Con los lotes ideales necesitaríamos 80,4 m³: no entran. Lo resolvimos con Lagrange. Se agrega λ, que funciona como un "alquiler" por usar espacio: cuanto más grande es, más chicos quedan los lotes. Fuimos subiendo λ hasta que el depósito quedó justo lleno:

- λ = $5.820 por m³
- Lotes: 1.098 m² de corcho y 255 L de sellador

El lote de 2.000 m² del descuento ocupa 100 m³, así que hoy no entra. Para aprovecharlo habría que ampliar el depósito a unos 106 m³.

**3. Demanda aleatoria: ¿cuándo hay que pedir?** El consumo no es siempre igual: en promedio es 47 m² por día, con un desvío de 8. El proveedor tarda 10 días en entregar. Si pidiéramos justo cuando queda lo que se consume en promedio en esos 10 días, la mitad de las veces nos quedaríamos sin corcho. Entonces guardamos un colchón:

- Stock de seguridad: 1,645 · 8 · √10 = **42 m²**, para un 5 % de riesgo de faltante.
- Punto de pedido: 470 + 42 = **512 m²**.

**Política final.** Cuando quedan 512 m² de corcho, pedir 1.098 m². Son unos 15,6 pedidos por año, uno cada 23 días.

## Etapa 3 · Preguntas

**1) ¿Cuál es la inconsistencia del modelo aleatorio? (lo que marcó el profe)**

Ejemplo: tenés un placard que entra justo con 1.098 m² de corcho. Después decís "por las dudas guardo 42 m² extra de reserva". Cuando llega un pedido nuevo, en el depósito está el pedido más la reserva, y no entra: 62,1 m³ en un depósito de 60. Cada modelo estaba bien solo, pero juntos no cierran.

La solución es reservar primero el lugar para los 42 m² y calcular el lote con el espacio que queda (57,9 m³):

| | Antes | Corregido |
| --- | --- | --- |
| Lote de corcho | 1.098 m² | 1.059 m² |
| Lote de sellador | 255 L | 249 L |
| Espacio con la reserva | 62,1 m³ | 60 m³ |
| Punto de pedido | 512 m² | 512 m² |

Cuesta solo $13.000 más por año y ahora sí entra.

**2) ¿Y si se aceptan los pedidos especiales de la Etapa 2?**

Usaríamos todo el corcho que da el proveedor (600 m² por semana), así que el corcho dejaría de sobrar. Igual el que manda sigue siendo el depósito: el lote no puede pasar de unos 1.100 m².

**3) ¿Por qué pedir exactamente 2.000 m² y no más?**

Con descuento, el lote ideal sería 1.532. Cuanto más nos alejamos de ese número, más caro sale. Si estamos obligados a pedir 2.000 o más para tener el descuento, lo mejor es pedir 2.000 justo, lo más cerca posible del ideal.

**4) ¿Por qué el costo de compra entra en el descuento y en Lagrange no?**

En el descuento el precio cambia según cuánto pidamos, así que importa. En Lagrange el precio es siempre el mismo: pidamos como pidamos, al año compramos la misma cantidad al mismo precio. Es un número fijo que no cambia la decisión.

**5) ¿Qué es λ? ¿Por qué el tope para ampliar ($56.750 por m³) es mayor?**

λ es cuánto nos ahorraríamos por año si el depósito tuviera 1 m³ más: es el precio sombra del espacio. El tope para ampliar es mayor porque ampliar mucho no solo da espacio: también deja comprar con descuento, y eso es un ahorro extra que λ no ve.

**6) ¿Por qué no hay stock de seguridad en los modelos determinísticos?**

Porque sabemos exactamente cuánto vamos a consumir y cuándo llega el pedido. No hay sorpresas, así que no hace falta reserva.

**7) ¿Por qué el modelo aleatorio usa el lote del modelo con restricción?**

La incertidumbre cambia **cuándo** pedir: pedimos antes, cuando quedan 512 m², para tener colchón. **Cuánto** pedir no cambia, y el único lote que entra en el depósito es el restringido.

**8) Si el plan de la Etapa 1 es fijo, ¿por qué la demanda es aleatoria?**

Los 330 m² por semana son un promedio. En la realidad una semana nos piden más tapas y otra más cárter, y el consumo de corcho varía alrededor de ese promedio. El desvío de 8 es un supuesto: si fuera mayor, la reserva crecería en la misma proporción.
