# Tarea — Casos de prueba por valores límite (aplicación bancaria)

> Fuente de verdad del entregable. Se genera con
> `npm run docx -- materias/ICS/tarea-casos-prueba-valores-limite.md materias/ICS/tarea-casos-prueba-valores-limite.docx`.
> No editar el .docx ni el .pdf a mano.

---

## CASOS DE PRUEBA POR VALORES LÍMITE

### CLASES DE EQUIVALENCIA

<!-- cols: 16,24,26,34 -->

| ATRIBUTO | DOMINIO | VÁLIDAS | INVÁLIDAS |
|---|---|---|---|
| Código del banco | En blanco, o entero de 3 dígitos con el primer dígito mayor que 1 (200 ≤ X ≤ 999) | PV1) en blanco · PV2) 200 ≤ X ≤ 999 | PI1) 3 dígitos con primer dígito ≤ 1 (000 ≤ X ≤ 199) · PI2) menos de 3 dígitos · PI3) más de 3 dígitos (X > 999) · PI4) negativos · PI5) contiene letras · PI6) contiene caracteres especiales · PI7) decimales |
| Código de sucursal | Entero de 4 dígitos con el primer dígito mayor que 0 (1000 ≤ X ≤ 9999) | PV1) 1000 ≤ X ≤ 9999 | PI1) 4 dígitos con primer dígito 0 (0000 ≤ X ≤ 0999) · PI2) menos de 4 dígitos · PI3) más de 4 dígitos (X > 9999) · PI4) en blanco · PI5) negativos · PI6) contiene letras · PI7) contiene caracteres especiales o decimales |
| Número de cuenta | Cadena de exactamente 5 dígitos (00000 ≤ X ≤ 99999) | PV1) longitud = 5 y todos los caracteres son dígitos | PI1) longitud = 4 · PI2) longitud = 6 · PI3) en blanco (longitud 0) · PI4) longitud 5 con algún carácter no numérico · PI5) negativos o decimales |
| Clave personal | Cadena alfanumérica de exactamente 5 posiciones | PV1) longitud = 5 y todos los caracteres son alfanuméricos | PI1) longitud = 4 · PI2) longitud = 6 · PI3) en blanco (longitud 0) · PI4) longitud 5 con algún carácter no alfanumérico (símbolo, espacio, acento) |
| Orden | En blanco, "Talonario" o "Movimientos" | PV1) "Talonario" · PV2) "Movimientos" · PV3) en blanco | PI1) cualquier otra cadena · PI2) valor válido con diferencia de mayúsculas/minúsculas · PI3) valor válido con caracteres de más o de menos · PI4) valor válido con espacios sobrantes |

### CÓDIGO DEL BANCO

<!-- cols: 10,14,20,56 -->

| Caso | Partición | Entrada | Salida esperada |
|---|---|---|---|
| 1 | PV1 | (en blanco) | Operación aceptada, se procesa la orden |
| 2 | PV2 | 200 | Operación aceptada, se procesa la orden |
| 3 | PV2 | 201 | Operación aceptada, se procesa la orden |
| 4 | PV2 | 998 | Operación aceptada, se procesa la orden |
| 5 | PV2 | 999 | Operación aceptada, se procesa la orden |
| 6 | PI1 | 199 | "El código del banco debe ser de 3 dígitos y el primero mayor que 1" |
| 7 | PI1 | 000 | "El código del banco debe ser de 3 dígitos y el primero mayor que 1" |
| 8 | PI2 | 99 | "El código del banco debe ser de 3 dígitos y el primero mayor que 1" |
| 9 | PI3 | 1000 | "El código del banco debe ser de 3 dígitos y el primero mayor que 1" |
| 10 | PI4 | −200 | "El código del banco debe ser de 3 dígitos y el primero mayor que 1" |
| 11 | PI5 | A25 | "Ingrese únicamente números" |
| 12 | PI6 | 2#5 | "Ingrese únicamente números" |
| 13 | PI7 | 250,5 | "Ingrese un número entero" |

### CÓDIGO DE SUCURSAL

<!-- cols: 10,14,20,56 -->

| Caso | Partición | Entrada | Salida esperada |
|---|---|---|---|
| 14 | PV1 | 1000 | Operación aceptada, se procesa la orden |
| 15 | PV1 | 1001 | Operación aceptada, se procesa la orden |
| 16 | PV1 | 9998 | Operación aceptada, se procesa la orden |
| 17 | PV1 | 9999 | Operación aceptada, se procesa la orden |
| 18 | PI1 | 0999 | "El código de sucursal debe ser de 4 dígitos y el primero mayor que 0" |
| 19 | PI1 | 0000 | "El código de sucursal debe ser de 4 dígitos y el primero mayor que 0" |
| 20 | PI2 | 999 | "El código de sucursal debe ser de 4 dígitos y el primero mayor que 0" |
| 21 | PI3 | 10000 | "El código de sucursal debe ser de 4 dígitos y el primero mayor que 0" |
| 22 | PI4 | (en blanco) | "El código de sucursal es obligatorio" |
| 23 | PI5 | −1000 | "El código de sucursal debe ser de 4 dígitos y el primero mayor que 0" |
| 24 | PI6 | 1B34 | "Ingrese únicamente números" |
| 25 | PI7 | 12#4 | "Ingrese únicamente números" |

### NÚMERO DE CUENTA

<!-- cols: 10,14,20,56 -->

| Caso | Partición | Entrada | Salida esperada |
|---|---|---|---|
| 26 | PV1 | 00000 | Operación aceptada, se procesa la orden |
| 27 | PV1 | 00001 | Operación aceptada, se procesa la orden |
| 28 | PV1 | 99998 | Operación aceptada, se procesa la orden |
| 29 | PV1 | 99999 | Operación aceptada, se procesa la orden |
| 30 | PI1 | 1234 | "El número de cuenta debe tener 5 dígitos" |
| 31 | PI2 | 123456 | "El número de cuenta debe tener 5 dígitos" |
| 32 | PI3 | (en blanco) | "El número de cuenta es obligatorio" |
| 33 | PI4 | 1234A | "Ingrese únicamente números" |
| 34 | PI4 | 1234# | "Ingrese únicamente números" |
| 35 | PI5 | −1234 | "Ingrese únicamente números" |

### CLAVE PERSONAL

<!-- cols: 10,14,20,56 -->

| Caso | Partición | Entrada | Salida esperada |
|---|---|---|---|
| 36 | PV1 | A1b2C | Operación aceptada, se procesa la orden |
| 37 | PV1 | 00000 | Operación aceptada, se procesa la orden |
| 38 | PV1 | aaaaa | Operación aceptada, se procesa la orden |
| 39 | PV1 | ZZZZZ | Operación aceptada, se procesa la orden |
| 40 | PI1 | A1b2 | "La clave personal debe tener 5 posiciones alfanuméricas" |
| 41 | PI2 | A1b2C3 | "La clave personal debe tener 5 posiciones alfanuméricas" |
| 42 | PI3 | (en blanco) | "La clave personal es obligatoria" |
| 43 | PI4 | A1b2# | "La clave personal admite solo letras y números" |
| 44 | PI4 | A1 2C | "La clave personal admite solo letras y números" |
| 45 | PI4 | A1b2é | "La clave personal admite solo letras y números" |

### ORDEN

<!-- cols: 10,14,20,56 -->

| Caso | Partición | Entrada | Salida esperada |
|---|---|---|---|
| 46 | PV1 | Talonario | Se entrega el talonario de cheques |
| 47 | PV2 | Movimientos | Se entregan los movimientos del mes en curso |
| 48 | PV3 | (en blanco) | Se entregan los dos documentos: talonario y movimientos |
| 49 | PI2 | talonario | "Orden no reconocida. Valores admitidos: Talonario, Movimientos o en blanco" |
| 50 | PI3 | Talonarios | "Orden no reconocida. Valores admitidos: Talonario, Movimientos o en blanco" |
| 51 | PI3 | Movimiento | "Orden no reconocida. Valores admitidos: Talonario, Movimientos o en blanco" |
| 52 | PI4 | "Talonario " | "Orden no reconocida. Valores admitidos: Talonario, Movimientos o en blanco" |
| 53 | PI1 | Transferencia | "Orden no reconocida. Valores admitidos: Talonario, Movimientos o en blanco" |
