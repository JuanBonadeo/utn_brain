COMUNICACIONES
Fórmulas y pasos para resolver ejercicios de finales

IMPORTANTE: este es un documento NO oficial, no pertenece a la documentación de
la cátedra. Puede contener errores u omisiones. Está confeccionado para que sirva
para rendir, no para entender los temas. Para entender el origen de los temas es
necesario buscar información en internet o perder tiempo interpretando los apuntes
de la cátedra, que están bastante mal redactados en su mayoría o son poco claros.

Unidades
Tiempo
| ∞ Milisegundo = 𝑚𝑆𝑒𝑔 |     | = 10−3 segundos  |
| -------------------- | --- | ---------------- |
10−6 segundos
| ∞ Microsegundo = 𝜇𝑆𝑒𝑔 |     | =                |
| --------------------- | --- | ---------------- |
| ∞ Nanosegundo = 𝑛𝑆𝑒𝑔  |     | = 10−9 segundos  |
10−12 segundos
| ∞ Picosegundo = 𝜌𝑆𝑒𝑔 |     | =   |
| -------------------- | --- | --- |

Frecuencia (ciclos por segundo)
| ∞ Hercio =         | 𝐻𝑧 = 1 ciclo/segundo  |                     |
| ------------------ | --------------------- | ------------------- |
| ∞ Kilohercio = 𝐾𝐻𝑧 | =                     | 103 ciclos/segundo  |
106 ciclos/segundo
| ∞ Megahercio = 𝑀𝐻𝑧 |     | =                    |
| ------------------ | --- | -------------------- |
| ∞ Gigahercio = 𝐺𝐻𝑧 | =   | 109 ciclos/segundo   |
| ∞ Terahercio = 𝑇𝐻𝑧 | =   | 1012 ciclos/segundo  |

Tips de logaritmos
(Para facilitar el cálculo en la calculadora)
ln𝑁
| ∞ log 𝑁 | =   |     |
| ------- | --- | --- |
2
ln2
| ∞ log 𝑁 ≅ | 3,32 𝑥 log | 𝑁   |
| --------- | ---------- | --- |
| 2         |            | 10  |

Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

Teoría de la Información
Ejercicios del tipo: “Se tiene un mensaje compuesto por X pulsos. El primero de arranque, otros X
de 4 niveles y uno de parada…”
∞ Cantidad de mensajes ≠ que pueden transmitirse en tiempo T:
𝑡
|     | 𝑀(𝑇) | = µ𝑛 = µ𝜏  |     |
| --- | ---- | ---------- | --- |
∞ Cantidad de información:
|     | 𝐼 = log | 𝑀(𝑇) [𝑏𝑖𝑡𝑠]  |     |
| --- | ------- | ------------ | --- |
2
∞ Tasa de Información:
|     | 𝐼       | 𝑏𝑖𝑡𝑠     |     |
| --- | ------- | -------- | --- |
|     | 𝑅 =   [ | ]        |     |
|     | 𝑇       | 𝑠𝑒𝑔𝑢𝑛𝑑𝑜𝑠 |     |
∞ Tasa de Dígitos:
|     | 𝑁 𝑑í𝑔𝑖𝑡𝑜𝑠  | 𝑏𝑖𝑛𝑖𝑡𝑠   |     |
| --- | ---------- | -------- | --- |
| 𝑟 = |   [        | ] 𝑜 [    | ]   |
|     | 𝑇 𝑠𝑒𝑔𝑢𝑛𝑑𝑜𝑠 | 𝑠𝑒𝑔𝑢𝑛𝑑𝑜𝑠 |     |
∞ Velocidad de señalización:
|     | 1          | 1              |     |
| --- | ---------- | -------------- | --- |
| 𝑠 = |   [        | ] 𝑜 [𝑏𝑎𝑢𝑑𝑖𝑜𝑠]  |     |
|     | 𝜏 𝑠𝑒𝑔𝑢𝑛𝑑𝑜𝑠 |                |     |
𝑚í𝑛𝑖𝑚𝑜
Referencias:
𝑛: cantidad de dígitos de información sin los de arranque ni parada.
𝑡: tiempo de los dígitos de información sin los de arranque ni parada.
𝜏: tiempo de cada dígito.
𝑁: cantidad total de dígitos, incluyendo los de arranque y parada.
𝑇: tiempo total, incluyendo el tiempo de los dígitos de arranque y parada.

-----------------------------------------------------------------
Ejercicios del tipo: “Se tiene un canal binario / ternario en el que las probabilidades de los símbolos
son… Calcular Información Mutua / Entropía”
∞ Probabilidad de Salida:
𝑛
|     | 𝑃(𝑏 ) = ∑𝑃(𝑎 | )×𝑃(𝑏 | /𝑎 )  |
| --- | ------------ | ----- | ----- |
|     | 𝑗            | 𝑖     | 𝑗 𝑖   |
𝑖=1

∞ Probabilidad a Posteriori (o “Hacia atrás”):
|     |            | 𝑃(𝑎 )×𝑃(𝑏 | /𝑎 ) |
| --- | ---------- | --------- | ---- |
|     |            | 𝑖         | 𝑗 𝑖  |
|     | 𝑃(𝑎 /𝑏 ) = |           |      |
|     | 𝑖 𝑗        | 𝑃(𝑏 )     |      |
𝑗
Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

∞ Entropía de Salida:
𝑛
1
|     | 𝐻(𝐵) | = ∑𝑃(𝑏 | )×log  |     |     |
| --- | ---- | ------ | ------ | --- | --- |
|     |      |        | 𝑗 2𝑃(𝑏 | )   |     |
𝑗
𝑗=1

∞ Entropía del Canal:
𝑛
1
| 𝐻(𝐵/𝐴) | = ∑𝑃(𝑎 | )×𝑃(𝑏 | /𝑎 )×log |        |     |
| ------ | ------ | ----- | -------- | ------ | --- |
|        |        | 𝑖     | 𝑗 𝑖      | 2      |     |
|        |        |       |          | 𝑃(𝑏 /𝑎 | )   |
𝑗 𝑖
𝑖=1
𝑗=1

∞ Información Mutua:
𝐻(𝐵)−𝐻(𝐵/𝐴)
|     | 𝐼(𝐴,𝐵) | =   |     |     |     |
| --- | ------ | --- | --- | --- | --- |

Códigos compactos
∞ Fórmula para saber si necesito incorporar símbolos falsos:
|     |     | ω = r+α(r−1)  |     |     |     |
| --- | --- | ------------- | --- | --- | --- |
Si α no da entero, hay que agregar símbolos falsos de a uno, hasta que dé entero.
∞ Longitud media del código:
𝑛
|     |     | 𝐿 = ∑𝑃(𝑠 | )×𝐿   |     |     |
| --- | --- | -------- | ----- | --- | --- |
𝑖 𝑖
𝑖=1

∞ Entropía de la fuente:
𝑛
1
|     | 𝐻(𝑠) | = ∑𝑃(𝑠 | )×log  |     |     |
| --- | ---- | ------ | ------ | --- | --- |
|     |      |        | 𝑖 2𝑃(𝑠 |     |     |
)
𝑖
𝑖=1

∞ Entropía en unidades r-arias:
𝐻(𝑠)
|     |     | 𝐻 (𝑠) = |     |     |     |
| --- | --- | ------- | --- | --- | --- |
𝑟
|     |     |     | log 𝑟 |     |     |
| --- | --- | --- | ----- | --- | --- |
2

∞ Eficiencia:
𝐻 (𝑠)
𝑟
|     | 𝐸𝑓𝑖𝑐𝑖𝑒𝑛𝑐𝑖𝑎 |     | =   |     |     |
| --- | ---------- | --- | --- | --- | --- |
𝐿

Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

∞ Redundancia:
𝐿−𝐻 (𝑠)
𝑟
𝑅𝑒𝑑𝑢𝑛𝑑𝑎𝑛𝑐𝑖𝑎 = 1−𝐸𝑓𝑖𝑐𝑖𝑒𝑛𝑐𝑖𝑎 =
𝐿
Referencias:
ω: cantidad de símbolos de la fuente.
𝑟: cantidad de dígitos del alfabeto código.
Códigos Lineales
Ejercicios del tipo: “Dada la siguiente Matriz de Control de Paridad (H) hallar la Matriz Generadora
(G), el Código de Grupo y analizar el comportamiento frente a errores (síndromes).”
Pasos sobre un ejemplo (Final 5 - Ejercicio 3):
1) La matriz de paridad H tiene “n-m” filas por “n” columnas. La generadora tiene m filas por n
columnas. Y el Código de Grupo tiene 2𝑚 palabras.
2) Hago el producto matricial entre 𝐻𝑇 y el vector 𝑋 (vector de n columnas y una fila). El resultado
𝑛
lo tengo que igualar a un vector nulo de “n-m” columnas.
Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

3) A partir de eso, armo “n-m” ecuaciones igualadas a 0. Por ejemplo 𝑥 +𝑥 +𝑥 =0. Después
1 2 3
despejo para dejar “m” incógnitas.
4) A partir de esas ecuaciones, armo una tabla en la que le doy valores arbitrarios al “n-m” incógnitas
y así calculo las x que despejé en el paso anterior.
5) De la tabla del paso anterior, tomo m vectores linealmente independiente y con eso armo G.
6) Con G ya puedo armar el Código de Grupo (V). Elijo “m” escalares, le doy valores arbitrarios y
hago combinación lineal con G para obtenerlo (𝑣 =𝑘 𝑣 +𝑘 𝑣 …). La forma es la siguiente:
𝑖 1 1 2 2
Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

7) Lo último que queda es ver qué errores detectan y/o corrigen los diferentes síndromes. Pruebo
primero con 001:
Si hubiese encontrado más de un renglón con menor cantidad de 0’s solo se detecta error, pero no
se corrige. El error que detecta y/o corrige el síndrome es en el lugar donde las X tienen un 1.
Hamming
1) Si el ejercicio dice que se quieren enviar X mensajes, lo que hago es calcular la cantidad de dígitos
de información de la siguiente manera:
2𝑚 ≥ 𝑋
Esto siempre da m=4 en los finales. Evidentemente buscan que sea así para no complicarla.
2) Después calculo la cantidad de dígitos de control de la siguiente manera (esto siempre da que n=3
en los finales):
2𝑛 ≥ 𝑛+𝑚+1
3) Armo el diagrama de Venn ubicando en cada zona un Dígito de Control (𝐶 ,𝐶 ,𝐶 ) y los dígitos de
1 2 3
información en las intersecciones. La forma en la que están organizados en el gráfico es la más
conveniente según lo que se verá más adelante.
4) Del punto anterior sacó las ecuaciones correspondientes:
Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

5) Armo una “tira” de 7 posiciones dándole un número de ubicación a los dígitos de control según lo que
puse en el paso 3. Por ejemplo, 𝐶 =20 =1, por lo tanto, va en la posición 1 de la tira. 𝐶 =21 =2, va
1 2
en la posición 2 y 𝐶 =22 =4, va en la posición 4. En el resto de las posiciones completo con los dígitos
3
de información teniendo en cuenta la siguiente regla:
Si 𝐼 está en la intersección de 𝐶 y 𝐶 , tengo que ponerlo en la 3º posición por ser la suma de 𝐶 +𝐶 .
1 1 2 1 2
Otro ejemplo es que 𝐼 tiene que ir en la posición 7 por ser la suma de 𝐶 +𝐶 +𝐶 .
4 1 2 3
6) Este paso puedo hacerlo o no. Pero es útil tenerlo calculado todo para el paso siguiente. Lo que hago es
darles valores arbitrarios a los dígitos de información y, con las ecuaciones del paso 4, calcular cada uno
de los dígitos de control. En nuestro ejemplo, para 9 mensajes, es suficiente calcular los primeros 9
renglones.
Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

7) Ahora tengo que elegir un renglón para decir: “Quiero enviar tal palabra, pero se recibió tal otra”. Hago
la diferencia entre el dígito de control recibido y el que debería tener según la tabla del punto anterior.
El resultado binario lo paso a decimal teniendo en cuenta a que “C” corresponde cada posición y ese es
el número de posición, según la “tira” del punto 5, donde está el error.
Comunicaciones Digitales
TDM
Sabemos que el ejercicio es de TDM porque, en general, el ejercicio nos da el “n” (que
es la cantidad de bits con que se codifica) o directamente dice que es una codificación
binaria. También podemos darnos cuenta que es TDM porque se habla de señal
analógica por un canal digital.
∞ Ancho de Banda:
𝐵 = 𝑁×𝑛×2𝑓
𝑤 𝑚𝑎𝑥
∞ Ancho de Banda (fórmula alternativa):
1
𝐵 =
𝑤 𝜏
∞ Duración de la muestra:
𝑇 = 𝑛×𝜏
𝑚
Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

∞ Tiempo de muestreo:
| 𝑇 = | 𝑇 ×𝑁  |     |
| --- | ----- | --- |
𝑠 𝑚
∞ Frecuencia de muestreo:
1
𝑓 =
𝑠 𝑇
𝑠
Referencias:
𝑁: cantidad de señales que se transmiten.
𝑛: cantidad de bits con los que se codifica.
𝜏: ancho del pulso.

Qué graficar:

FDM
Sabemos que el ejercicio es de FDM porque el ejercicio puede decir que se desean
transmitir N señales analógicas en simultáneo o porque directamente habla de canal
analógico o porque no nos dan los bits con que se codifica.
∞ Ancho de Banda:
| 𝐵 = 𝑁×2𝑓 |                   |     |
| -------- | ----------------- | --- |
| 𝑤        | max (𝑑𝑒𝑙 𝑚𝑒𝑛𝑠𝑎𝑗𝑒) |     |
∞ Ancho de Banda (fórmula alternativa):
| 𝐵 = 𝑓       | −𝑓        |     |
| ----------- | --------- | --- |
| 𝑤 𝑚𝑎𝑥 𝑐𝑜𝑟𝑡𝑒 | 𝑚𝑖𝑛 𝑐𝑜𝑟𝑡𝑒 |     |
∞ Ancho del mensaje:
| 𝑤 = 𝑓 | −𝑓   |     |
| ----- | ---- | --- |
𝑚𝑎𝑥 𝑚𝑖𝑛
∞ Tiempo de muestreo:
| 𝑇 = | 𝑇 ×𝑁  |     |
| --- | ----- | --- |
𝑠 𝑚
Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.

∞ Equivalencia para calcular Bw:
𝑤 = 𝑓
𝑚𝑎𝑥
Referencias:
𝑁: cantidad de señales que se transmiten.
Qué graficar:
Documento realizado por Joel Arnold en febrero del 2020
Este documento no es oficial.