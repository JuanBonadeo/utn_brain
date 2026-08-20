# Tarea — Casos de prueba por valores límite (aplicación bancaria)

> **Fuente de verdad de este entregable.** El `.docx` y el `.pdf` se generan
> desde acá con `npm run docx -- materias/ICS/tarea-casos-prueba-valores-limite.md materias/ICS/tarea-casos-prueba-valores-limite.docx`
> y después `scripts/preview-docx.sh`. No editar los generados a mano.
>
> **Consigna (Clase 2 — Brozo, punto 3).** Aplicación bancaria por Internet.
> Entradas del procedimiento que gestiona las operaciones: código del banco,
> código de sucursal, número de cuenta, clave personal y orden. Hay que derivar
> las clases de equivalencia y construir los casos de prueba con la técnica de
> **particionamiento por valores límite**.
>
> **Observación sobre la tabla de clase.** La tabla que quedó en el Notion pone
> para el código del banco `PV1) 1 ≤ X ≤ 999`, lo que ignora la regla "el primer
> dígito tiene que ser mayor que 1", y `PI3) X ≥ 999`, que deja 999 como
> inválido cuando en realidad es el límite superior válido. Acá está corregido:
> el rango válido es 200 ≤ X ≤ 999.

---

## CASOS DE PRUEBA POR VALORES LÍMITE

**Aplicación bancaria por Internet — datos de entrada de la operación**

<!-- cols: 24,76 -->

| | |
|---|---|
| Cátedra | Ingeniería y Calidad de Software — 4º Año Ingeniería en Sistemas de Información |
| Técnica | Particionamiento de equivalencias + análisis de valores límite |
| Alumno | Bonadeo, Juan Cruz (53535) |

---

### 1. ENUNCIADO

Considérese una aplicación bancaria donde el usuario puede conectarse al banco por Internet y realizar una serie de operaciones bancarias. Una vez accedido al banco con las consiguientes medidas de seguridad (clave de acceso y demás), la información de entrada del procedimiento que gestiona las operaciones concretas a realizar por el usuario requiere la siguiente entrada:

- **Código del banco.** En blanco o número de tres dígitos. En este último caso, el primero de los dígitos tiene que ser mayor que 1.
- **Código de sucursal.** Un número de cuatro dígitos. El primero de ellos mayor de 0.
- **Número de cuenta.** Número de cinco dígitos.
- **Clave personal.** Valor alfanumérico de cinco posiciones.
- **Orden.** Se introduce según la orden que se desee realizar. Puede estar en blanco o ser una de las dos cadenas siguientes: "Talonario" o "Movimientos". En el primer caso el usuario recibirá un talonario de cheques, en el segundo recibirá los movimientos del mes en curso. Si este código está en blanco, el usuario recibirá los dos documentos.

### 2. CRITERIO APLICADO

El particionamiento de equivalencias solo garantiza un caso por clase, tomando un representante cualquiera. El análisis de valores límite refina esa elección: la experiencia muestra que los errores se concentran en los bordes de cada partición, no en el medio. El criterio usado en toda la tarea es:

- Para una partición válida numérica de rango `[a, b]`, se prueban `a`, `a+1`, `b-1` y `b`.
- Para cada borde se prueba además el primer valor que queda afuera: `a-1` y `b+1`, que caen en particiones inválidas y sirven para verificar que el rechazo ocurre exactamente donde debe.
- Para los campos definidos por longitud (número de cuenta, clave personal), el límite es la cantidad de caracteres: se prueban las longitudes `n-1`, `n` y `n+1`.
- Para los campos alfanuméricos con un conjunto cerrado de valores (orden), no hay orden numérico ni longitud que recorrer: se prueba un caso por cada valor admitido, y como "límites" se usan las variantes mínimamente distintas de esos valores (mayúsculas/minúsculas, un carácter de más o de menos, espacios sobrantes).

Cada caso de prueba varía **un solo atributo**. Los demás campos se completan siempre con la combinación válida de referencia: banco `250`, sucursal `1234`, cuenta `12345`, clave `A1b2C`, orden `Talonario`.

### 3. CLASES DE EQUIVALENCIA

<!-- cols: 16,24,26,34 -->

| ATRIBUTO | DOMINIO | VÁLIDAS | INVÁLIDAS |
|---|---|---|---|
| Código del banco | En blanco, o entero de 3 dígitos con el primer dígito mayor que 1 (200 ≤ X ≤ 999) | PV1) en blanco · PV2) 200 ≤ X ≤ 999 | PI1) 3 dígitos con primer dígito ≤ 1 (000 ≤ X ≤ 199) · PI2) menos de 3 dígitos · PI3) más de 3 dígitos (X > 999) · PI4) negativos · PI5) contiene letras · PI6) contiene caracteres especiales · PI7) decimales |
| Código de sucursal | Entero de 4 dígitos con el primer dígito mayor que 0 (1000 ≤ X ≤ 9999) | PV1) 1000 ≤ X ≤ 9999 | PI1) 4 dígitos con primer dígito 0 (0000 ≤ X ≤ 0999) · PI2) menos de 4 dígitos · PI3) más de 4 dígitos (X > 9999) · PI4) en blanco · PI5) negativos · PI6) contiene letras · PI7) contiene caracteres especiales o decimales |
| Número de cuenta | Cadena de exactamente 5 dígitos (00000 ≤ X ≤ 99999) | PV1) longitud = 5 y todos los caracteres son dígitos | PI1) longitud = 4 · PI2) longitud = 6 · PI3) en blanco (longitud 0) · PI4) longitud 5 con algún carácter no numérico · PI5) negativos o decimales |
| Clave personal | Cadena alfanumérica de exactamente 5 posiciones | PV1) longitud = 5 y todos los caracteres son alfanuméricos | PI1) longitud = 4 · PI2) longitud = 6 · PI3) en blanco (longitud 0) · PI4) longitud 5 con algún carácter no alfanumérico (símbolo, espacio, acento) |
| Orden | En blanco, "Talonario" o "Movimientos" | PV1) "Talonario" · PV2) "Movimientos" · PV3) en blanco | PI1) cualquier otra cadena · PI2) valor válido con diferencia de mayúsculas/minúsculas · PI3) valor válido con caracteres de más o de menos · PI4) valor válido con espacios sobrantes |

### 4. CASOS DE PRUEBA

#### 4.1 Código del banco

Rango válido `[200, 999]` más la partición "en blanco". Los límites relevantes son 200 y 999, con sus vecinos inmediatos 199 y 1000, que ya caen fuera.

<!-- cols: 9,12,26,17,36 -->

| Caso | Partición | Criterio de límite | Entrada | Salida esperada |
|---|---|---|---|---|
| 1 | PV1 | Único valor de la partición | (en blanco) | Operación aceptada, se procesa la orden |
| 2 | PV2 | Límite inferior (a) | 200 | Operación aceptada, se procesa la orden |
| 3 | PV2 | Límite inferior + 1 (a+1) | 201 | Operación aceptada, se procesa la orden |
| 4 | PV2 | Límite superior − 1 (b−1) | 998 | Operación aceptada, se procesa la orden |
| 5 | PV2 | Límite superior (b) | 999 | Operación aceptada, se procesa la orden |
| 6 | PI1 | Límite inferior − 1 (a−1) | 199 | "El código del banco debe ser de 3 dígitos y el primero mayor que 1" |
| 7 | PI1 | Extremo inferior de la partición inválida | 000 | "El código del banco debe ser de 3 dígitos y el primero mayor que 1" |
| 8 | PI2 | Longitud máxima con menos de 3 dígitos | 99 | "El código del banco debe ser de 3 dígitos y el primero mayor que 1" |
| 9 | PI3 | Límite superior + 1 (b+1) | 1000 | "El código del banco debe ser de 3 dígitos y el primero mayor que 1" |
| 10 | PI4 | Simétrico negativo del límite inferior | −200 | "El código del banco debe ser de 3 dígitos y el primero mayor que 1" |
| 11 | PI5 | Un solo carácter no numérico | A25 | "Ingrese únicamente números" |
| 12 | PI6 | Un solo carácter especial | 2#5 | "Ingrese únicamente números" |
| 13 | PI7 | Valor válido con parte decimal mínima | 250,5 | "Ingrese un número entero" |

#### 4.2 Código de sucursal

Rango válido `[1000, 9999]`. El campo es obligatorio: a diferencia del código del banco, el enunciado no admite dejarlo vacío.

<!-- cols: 9,12,26,17,36 -->

| Caso | Partición | Criterio de límite | Entrada | Salida esperada |
|---|---|---|---|---|
| 14 | PV1 | Límite inferior (a) | 1000 | Operación aceptada, se procesa la orden |
| 15 | PV1 | Límite inferior + 1 (a+1) | 1001 | Operación aceptada, se procesa la orden |
| 16 | PV1 | Límite superior − 1 (b−1) | 9998 | Operación aceptada, se procesa la orden |
| 17 | PV1 | Límite superior (b) | 9999 | Operación aceptada, se procesa la orden |
| 18 | PI1 | Límite inferior − 1 (a−1), primer dígito 0 | 0999 | "El código de sucursal debe ser de 4 dígitos y el primero mayor que 0" |
| 19 | PI1 | Extremo inferior de la partición inválida | 0000 | "El código de sucursal debe ser de 4 dígitos y el primero mayor que 0" |
| 20 | PI2 | Longitud máxima con menos de 4 dígitos | 999 | "El código de sucursal debe ser de 4 dígitos y el primero mayor que 0" |
| 21 | PI3 | Límite superior + 1 (b+1) | 10000 | "El código de sucursal debe ser de 4 dígitos y el primero mayor que 0" |
| 22 | PI4 | Ausencia total de dato | (en blanco) | "El código de sucursal es obligatorio" |
| 23 | PI5 | Simétrico negativo del límite inferior | −1000 | "El código de sucursal debe ser de 4 dígitos y el primero mayor que 0" |
| 24 | PI6 | Un solo carácter no numérico | 1B34 | "Ingrese únicamente números" |
| 25 | PI7 | Un solo carácter especial | 12#4 | "Ingrese únicamente números" |

#### 4.3 Número de cuenta

Acá el límite no es un rango de valores sino la longitud: exactamente 5 dígitos. Se prueban las longitudes 4, 5 y 6, y dentro de la partición válida los valores extremos que puede tomar una cadena de 5 dígitos.

<!-- cols: 9,12,26,17,36 -->

| Caso | Partición | Criterio de límite | Entrada | Salida esperada |
|---|---|---|---|---|
| 26 | PV1 | Longitud correcta, valor mínimo | 00000 | Operación aceptada, se procesa la orden |
| 27 | PV1 | Valor mínimo + 1 | 00001 | Operación aceptada, se procesa la orden |
| 28 | PV1 | Valor máximo − 1 | 99998 | Operación aceptada, se procesa la orden |
| 29 | PV1 | Longitud correcta, valor máximo | 99999 | Operación aceptada, se procesa la orden |
| 30 | PI1 | Longitud − 1 (un dígito de menos) | 1234 | "El número de cuenta debe tener 5 dígitos" |
| 31 | PI2 | Longitud + 1 (un dígito de más) | 123456 | "El número de cuenta debe tener 5 dígitos" |
| 32 | PI3 | Longitud 0 | (en blanco) | "El número de cuenta es obligatorio" |
| 33 | PI4 | Longitud correcta, un carácter no numérico | 1234A | "Ingrese únicamente números" |
| 34 | PI5 | Longitud correcta, un carácter especial | 1234# | "Ingrese únicamente números" |
| 35 | PI5 | Signo negativo ocupando una posición | −1234 | "Ingrese únicamente números" |

#### 4.4 Clave personal

Dos límites conviven en este campo: la longitud (exactamente 5) y el conjunto de caracteres admitidos (alfanuméricos). Se recorren ambos.

<!-- cols: 9,12,26,17,36 -->

| Caso | Partición | Criterio de límite | Entrada | Salida esperada |
|---|---|---|---|---|
| 36 | PV1 | Longitud correcta, mezcla de letras y dígitos | A1b2C | Operación aceptada, se procesa la orden |
| 37 | PV1 | Extremo del dominio: solo dígitos | 00000 | Operación aceptada, se procesa la orden |
| 38 | PV1 | Extremo del dominio: solo letras minúsculas | aaaaa | Operación aceptada, se procesa la orden |
| 39 | PV1 | Extremo del dominio: solo letras mayúsculas | ZZZZZ | Operación aceptada, se procesa la orden |
| 40 | PI1 | Longitud − 1 (un carácter de menos) | A1b2 | "La clave personal debe tener 5 posiciones alfanuméricas" |
| 41 | PI2 | Longitud + 1 (un carácter de más) | A1b2C3 | "La clave personal debe tener 5 posiciones alfanuméricas" |
| 42 | PI3 | Longitud 0 | (en blanco) | "La clave personal es obligatoria" |
| 43 | PI4 | Longitud correcta, un carácter especial | A1b2# | "La clave personal admite solo letras y números" |
| 44 | PI4 | Longitud correcta, un espacio intermedio | A1 2C | "La clave personal admite solo letras y números" |
| 45 | PI4 | Longitud correcta, una letra acentuada | A1b2é | "La clave personal admite solo letras y números" |

#### 4.5 Orden

Campo alfanumérico con tres valores admitidos y ningún orden numérico que recorrer. Se hace un caso por cada valor válido, y los "límites" son las variantes mínimamente distintas de esos valores: son las que más errores destapan, porque suelen surgir de comparaciones de cadenas mal hechas.

<!-- cols: 9,12,26,17,36 -->

| Caso | Partición | Criterio de límite | Entrada | Salida esperada |
|---|---|---|---|---|
| 46 | PV1 | Valor admitido, escrito exacto | Talonario | Se entrega el talonario de cheques |
| 47 | PV2 | Valor admitido, escrito exacto | Movimientos | Se entregan los movimientos del mes en curso |
| 48 | PV3 | Ausencia de valor: comportamiento por defecto | (en blanco) | Se entregan los dos documentos: talonario y movimientos |
| 49 | PI2 | Valor válido en minúsculas | talonario | "Orden no reconocida. Valores admitidos: Talonario, Movimientos o en blanco" |
| 50 | PI3 | Valor válido con un carácter de más | Talonarios | "Orden no reconocida. Valores admitidos: Talonario, Movimientos o en blanco" |
| 51 | PI3 | Valor válido con un carácter de menos | Movimiento | "Orden no reconocida. Valores admitidos: Talonario, Movimientos o en blanco" |
| 52 | PI4 | Valor válido con un espacio al final | Talonario_ | "Orden no reconocida. Valores admitidos: Talonario, Movimientos o en blanco" |
| 53 | PI1 | Cadena ajena al conjunto admitido | Transferencia | "Orden no reconocida. Valores admitidos: Talonario, Movimientos o en blanco" |

En el caso 52 el guion bajo representa un espacio en blanco al final de la cadena. Si la aplicación recorta los espacios antes de comparar, la salida esperada pasa a ser la del caso 46; el caso sirve justamente para dejar documentado cuál de los dos comportamientos implementa el programa.

### 5. CASO COMBINADO EN LOS LÍMITES

Los casos anteriores varían un atributo por vez. Conviene agregar dos casos que combinen los extremos de todos los campos a la vez: los errores de desbordamiento y de concatenación de campos aparecen cuando todas las entradas están simultáneamente en su valor mínimo o máximo.

<!-- cols: 9,21,12,12,12,12,22 -->

| Caso | Criterio | Banco | Sucursal | Cuenta | Clave | Salida esperada |
|---|---|---|---|---|---|---|
| 54 | Todos los campos en su límite inferior, orden en blanco | 200 | 1000 | 00000 | 00000 | Operación aceptada, se entregan los dos documentos |
| 55 | Todos los campos en su límite superior, orden "Movimientos" | 999 | 9999 | 99999 | ZZZZZ | Operación aceptada, se entregan los movimientos del mes |

### 6. RESUMEN

<!-- cols: 34,16,16,17,17 -->

| Atributo | Válidos | Inválidos | Total | Casos |
|---|---|---|---|---|
| Código del banco | 5 | 8 | 13 | 1 a 13 |
| Código de sucursal | 4 | 8 | 12 | 14 a 25 |
| Número de cuenta | 4 | 6 | 10 | 26 a 35 |
| Clave personal | 4 | 6 | 10 | 36 a 45 |
| Orden | 3 | 5 | 8 | 46 a 53 |
| Combinados | 2 | 0 | 2 | 54 y 55 |
| **Total** | **22** | **33** | **55** | |

Todos estos casos quedan documentados y se conservan: al corregir cualquier error detectado se vuelven a ejecutar completos como **pruebas de regresión**, para verificar que la corrección no rompió nada que antes funcionaba.
