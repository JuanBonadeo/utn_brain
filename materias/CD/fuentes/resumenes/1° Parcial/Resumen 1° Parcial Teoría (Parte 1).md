Comunicaciones 1er parcial teoría
Información, codificación y canales
Fuentes:
  - Ergódicas: probabilidad independiente del tiempo.
  - Memoria nula.
1
| Cantidad de información (𝑰 |     |     | ) de un suceso 𝑨: lg |     |     |     |     | = [Bit]  |     |     |
| -------------------------- | --- | --- | -------------------- | --- | --- | --- | --- | -------- | --- | --- |
|                            |     |     | (𝑨)                  |     |     |     | 2   |          |     |     |
𝑃 (𝐴)
|                          |     |     |          |      |     | 1   | 𝑏𝑖𝑡     |     |     |     |
| ------------------------ | --- | --- | -------- | ---- | --- | --- | ------- | --- | --- | --- |
| Entropía de la fuente (𝑯 |     |     | ): ∑ 𝑃(𝑎 | ).lg |     | =   | [       |  ]  |     |     |
|                          |     | (𝑨) | 𝑖        | 𝑖    | 2   |     |         |     |     |     |
|                          |     |     |          |      | 𝑃(𝑎 | )   | 𝑠𝑖𝑚𝑏𝑜𝑙𝑜 |     |     |     |
𝑖
Es la esperanza matemática de la información por símbolo de la fuente. Tiene su máximo
valor para un determinado número de símbolos fuente cuando son equiprobables.
Modelo de canal multivariado:

|     |     |     |     |     |     |     |     |     | 𝑎 : Símbolos de entrada del  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- |
𝑖
canal.
𝑏 : Símbolos de salida del
𝑖
canal.

|     |     |     |     | 𝑃(𝑏 | ⁄𝑎  | )   | 𝑃(𝑏 ⁄𝑎 | )   | 𝑃(𝑏 ⁄𝑎 | )   |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------ | --- |
|     |     |     |     |     | 1   | 1   | 2      | 1   | 3      | 1   |
Probabilidades condicionales: 𝑃 = [𝑃(𝑏 ⁄𝑎 ) 𝑃(𝑏 ⁄𝑎 ) 𝑃(𝑏 ⁄𝑎 )]
|     |     |     |     |     | 1   | 2   | 2      | 2   | 3      | 2   |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------ | --- |
|     |     |     |     | 𝑃(𝑏 | ⁄𝑎  | )   | 𝑃(𝑏 ⁄𝑎 | )   | 𝑃(𝑏 ⁄𝑎 | )   |
|     |     |     |     |     | 1   | 3   | 2      | 3   | 3      | 3   |
Cada fila de la matriz corresponde a una entrada del canal y cada columna a una salida.
Canal transparente:  no introduce error, su matriz de probabilidades condicionales es
diagonal.
Modelo bivariado: canal binario simétrico.
|   - 𝑃(𝑏 | ⁄𝑎 ) =    | 𝑃(𝑏 ⁄𝑎 | )   |     |     |     |     |     |     |     |
| ------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|         | 1 2       | 2      | 1   |     |     |     |     |     |     |     |
|   - 𝑃(𝑏 | ) = ∑ 𝑃(𝑎 | ).𝑃(𝑏  | ⁄𝑎  | )   |     |     |     |     |     |     |
|         | 𝑗 𝑖       | 𝑖      | 𝑗   | 𝑖   |     |     |     |     |     |     |
1
|   - Entropía entrada: 𝐻(𝐴) |     |     | =   | ∑ 𝑃(𝑎 | ).lg |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ----- | ---- | --- | --- | --- | --- | --- |
|                            |     |     |     | 𝑖     | 𝑖    | 2   |     |     |     |     |
|                            |     |     |     |       |      | 𝑃(𝑎 | )   |     |     |     |
𝑖
1
|   - Entropía salida: 𝐻(𝐵) |     |     | = ∑ | 𝑃(𝑏 | ).lg |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
|                           |     |     |     | 𝑗   | 𝑗    | 2   |     |     |     |     |
|                           |     |     |     |     |      | 𝑃(𝑏 | 𝑗 ) |     |     |     |
1
|   - Entropía del canal: 𝐻(𝐵⁄𝐴 ) |     |     |     | =   | ∑ 𝑃(𝑎 | ).𝑃(𝑏 |     | /𝑎 ).lg |       | -    |
| ------------------------------- | --- | --- | --- | --- | ----- | ----- | --- | ------- | ----- | ---- |
|                                 |     |     |     |     | 𝑖,𝑗   | 𝑖     | 𝑗   | 𝑖       | 2 𝑃(𝑏 | ⁄𝑎 ) |
𝑗 𝑖
|                                   |     |     |     |     |        | 𝑃(𝑎 | 𝑖 ).𝑃(𝑏 𝑗 | ⁄𝑎 𝑖 ) |     |     |
| --------------------------------- | --- | --- | --- | --- | ------ | --- | --------- | ------ | --- | --- |
|   - Probabilidad hacia atrás: 𝑃(𝑎 |     |     |     |     | ⁄𝑏 ) = |     |           |        |     |     |
𝑖 𝑗
𝑃(𝑏 )
𝑗

Información mutua: cantidad de información promedio que pasa de la entrada a la salida a
través del canal.
|                                   |     | 𝐼(𝐴,𝐵) |     | = 𝐼(𝐵,𝐴) | = 𝐻(𝐵) | − 𝐻(𝐵⁄𝐴)  | = 𝐻(𝐴) | − 𝐻(𝐴⁄𝐵)  |
| --------------------------------- | --- | ------ | --- | -------- | ------ | --------- | ------ | --------- |
| Si el canal es transparente: 𝐻(𝐵) |     |        |     |          | = 𝐻(𝐴) | = 𝐼(𝐴,𝐵)  |        |           |
Conceptos fundamentales (mensajes equiprobables)
Siendo:
𝑛: cantidad de dígitos de información
𝑁: cantidad de dígitos del mensaje
𝑇: duración del mensaje
𝜏: duración del pulso
𝜇: cantidad de niveles
|     |                             |     |     |     | 𝐼(𝑀) 𝑏𝑖𝑡 |     |     |     |
| --- | --------------------------- | --- | --- | --- | -------- | --- | --- | --- |
|     | - Tasa de información (𝑅):  |     |     |     | = [      | ]   |     |     |
|     |                             |     |     |     | 𝑇 𝑠𝑒𝑔    |     |     |     |
1
|     | - Velocidad de señalización (𝑠):  |     |     |     |     |     |     |     |
| --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
𝜏
𝑚𝑖𝑛
|     |                                       |     | 𝑁      | 𝑏𝑖𝑛𝑖𝑡 |           |        |     |     |
| --- | ------------------------------------- | --- | ------ | ----- | --------- | ------ | --- | --- |
|     | - Tasa de dígitos:                    |     |        | = [   | ]         |        |     |     |
|     |                                       |     | 𝑇      | 𝑠𝑒𝑔   |           |        |     |     |
|     | - Cantidad de mensajes posibles: 𝑀(𝑇) |     |        |       |           | 𝜇𝑛     |     |     |
|     |                                       |     |        |       |           | =      |     |     |
|     |                                       | 1   |        |       |           | 𝑛lg 𝜇  |     |     |
|     | - 𝑷(𝑴)                                | =   | ⇒ 𝑰(𝑴) | =     | 𝑛lg 𝜇 ⇒ 𝑹 | = 2    |     |     |
2
|     |     | 𝜇𝑛  |     |     |     | 𝑇   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Codificación
Código bloque: asigna a cada símbolo del código fuente 𝑆 una secuencia fija de símbolos
del alfabeto código 𝑍. Estas secuencias fijas (𝑍 ) reciben el nombre de palabras código.
𝑗
| 𝑆          𝑍 | (𝑧   | ;𝑧 ;𝑧 | ;…;𝑧 | )   |     |     |     |     |
| ------------ | ---- | ----- | ---- | --- | --- | --- | --- | --- |
| 1            | 1 11 | 12    | 13   | 1𝑟  |     |     |     |     |
| 𝑆          𝑍 | (𝑧   | ;𝑧 ;𝑧 | ;…;𝑧 | )   |     |     |     |     |
| 2            | 2 21 | 22    | 23   | 2𝑟  |     |     |     |     |
…
| 𝑆          𝑍 | (𝑧 ;𝑧 | ;𝑧    | ;…;𝑧 | )   |     |     |     |     |
| ------------ | ----- | ----- | ---- | --- | --- | --- | --- | --- |
| 𝑗            | 1 𝑗1  | 𝑗2 𝑗3 |      | 𝑗𝑟  |     |     |     |     |
Código no singular: código bloque cuyas palabras son todas distintas.
Código unívocamente decodificable (unívoco): código no singular tal que a cualquier
secuencia de palabras código le corresponde una única secuencia de símbolos de la fuente.
Un código bloque se dice unívocamente decodificado sí y solo sí su extensión de orden n es
no singular para cualquier valor finito de n.
- Ecuación de McMillan: dado que los códigos instantáneos son una subclase de los
unívocos, la condición suficiente para que exista al menos un código unívoco es que las
| longitudes 𝑙 |  verifiquen la expresión:   |     |     |     |     |     |     |     |
| ------------ | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
𝑖
𝑞
|     |     |     |     |     | ∑𝑟−𝑙 | ≤ 1  |     |     |
| --- | --- | --- | --- | --- | ---- | ---- | --- | --- |
𝑖
𝑖=1
si satisfacen la expresión pueden construirse con ellas un código unívoco.

Código instantáneo: código unívoco en el cual ninguna palabra es prefijo de otra.
- Inecuación de Kraft: Si los enteros 𝑙 ; 𝑙 ; ..........; 𝑙  satisfacen la inecuación:
1 2 𝑞
𝑞
∑𝑟−𝑙 𝑖 ≤ 1
𝑖=1
Entonces esta es condición suficiente y necesaria para que exista al menos un código
instantáneo de r símbolos en su alfabeto y cuyas q palabras códigos tienen las longitudes 𝑙 ;
1
| 𝑙 ; ..........; 𝑙 |  respectivamente.  |     |     |
| ----------------- | ------------------ | --- | --- |
| 2                 | 𝑞                  |     |     |
Código compacto: código instantáneo de menor longitud promedio entre todos los códigos
instantáneos que se pueden aplicar a esa fuente con ese código.
| 𝐿 ≥ 𝐻 (𝑆),     | 𝐻 = | ∑ 𝑃.lg 1/𝑃  |     |
| -------------- | --- | ----------- | --- |
| 𝑟              | 𝑟   | 𝑖 𝑖 𝑟       | 𝑖   |
|                |     | 𝐻 (𝑆)       |     |
| Rendimiento: 𝜂 | =   | 𝑟           |     |

𝐿
| Redundancia: ℜ       |     | = 1 − 𝜂  |     |
| -------------------- | --- | -------- | --- |
| Longitud promedio: ∑ |     | 𝑃 .𝑙     |     |
|                      |     | 𝑖 𝑖 𝑖    |     |
Método Hoffman: para obtener un código compacto 𝑟-ario:
1. Ordenar los símbolos fuente según sus probabilidades en orden decreciente.
2. Agrupar los 𝑟 símbolos de menor probabilidad en un nuevo símbolo que tendrá la suma
de las probabilidades.
3. Reordenar los símbolos de la fuente extendida en orden decreciente indicando con una
flecha de donde proviene el resultado de la suma de probabilidades.
4. Se repiten los pasos 2 y 3 hasta llegar a una fuente de 𝑟 símbolos.
5. Se codifica esta fuente en forma compacta con los 𝑟 símbolos código.
6. Se vuelve hacia atrás teniendo en cuenta la codificación que se le dio a c/u de los 𝑟
símbolos de la fuente extendida.
7. Se observa que los 𝑟 símbolos de menor probabilidad tienen la misma codificación, con lo
cual se deberá agregar a la derecha un dígito con los 𝑟 símbolos.
8. Repetir pasos 6 y 7 hasta llegar a la fuente original.
Nota: tener en cuenta que si el código es binario siempre se va a llegar a una fuente
externa de 2 símbolos. Si el código es ternario puede que no se llegue a 3 símbolos, en este
caso a la fuente original habrá que agregarle un símbolo fantasma de 𝑃(𝑆) = 0.
Si el código es cuaternario, puede ocurrir que la última fuente externa no sea de 4
símbolos, con lo cual deberá agregarse 1 o 2 símbolos fantasma según corresponda.
|     |     |     |     |
| --- | --- | --- | --- |

Detección de errores
Distancia de un código: cantidad de dígitos que cambian entre dos palabras del código.
Distancia mínima: menor cantidad de dígitos entre dos palabras del mismo código.
Si se pretende detectar un error simple en la palabra código que se recibe se deberá
aumentar la Distancia Mínima del Código
Bit de paridad: agregar un dígito a la derecha que representa la paridad par o impar de
“unos” de la palabra código.
| 𝐵𝑃  | = 𝐼 ⊕ 𝐼 | ⊕ 𝐼 ⊕ …⊕ | 𝐼 ,        𝐵𝑃 | =     | 𝐵𝑃 + 1  |
| --- | ------- | -------- | ------------- | ----- | ------- |
| 𝑃𝐴𝑅 | 0 1     | 2        | 𝑛             | 𝐼𝑀𝑃𝐴𝑅 | 𝑃𝐴𝑅     |
⊕: suma sin acarreo.
Paridad por filas y columnas: arma un bloque de palabras y se agrega una columna y una
fila de paridad par. Se transmite el bloque y al recibirlo se verifican la paridad de cada fila y
columna y se comparan.
El dígito con error se encontrará en la intersección de la fila y columna donde los bit de
paridad recibidos y generador en el receptor no coinciden.
El inconveniente de este método es que se debe armar bloques de palabras códigos, no
corrige por palabra.
Paridad por zonas – código Hamming: cada dígito de control será la paridad par del
conjunto de dígitos de información incluidos en su zona:
|     |     |     | 𝐶1  | = 𝐼 ⊕ 𝐼 | ⊕ 𝐼   |
| --- | --- | --- | --- | ------- | ----- |
|     |     |     |     | 0 1     | 2     |
|     |     |     | 𝐶2  | = 𝐼 ⊕ 𝐼 | ⊕ 𝐼   |
|     |     |     |     | 1 2     | 3     |
|     |     |     | 𝐶3  | = 𝐼 ⊕ 𝐼 | ⊕ 𝐼   |
|     |     |     |     | 0 2     | 3     |
En el receptor genero nuevamente los dígitos de control y los
comparo con los dígitos de control recibidos.
Los dígitos de control se descartan una vez realizada el
control y la corrección.
El inconveniente del código Hamming es la de tener dos campos, uno para la información y
otro de control.