# Clase 2 Brozo

# Validacion y Verificacion

Resumen Mateo pag 37

Son 2 áreas de CMMI

Validación, asgura el producto satiface expectativas del cliente.

- Debe hacer lo que el cliente requiere

Verificacion, asegura que el producto se construya adecuadamente.

- Software debería ajustarse a su especificación.

## Grado de Confianza

Depende de

- Funcion del Software
- Expectativas del usuario
- Entorno de marketing

## Estática y Dinámica

Estatica → Revisiones

- Documentos (codigo, user story)
- Puedo detectar donde estaría el error. Se encuentran varios a la vez. Ventajas
- Mas lentas. Desventaja

Pueden ser:

Informales, no hay procesodefinido, no existen roles, no son planeadas

Formales, objetivos definidos, proceso documentado, roles definidos, reporte del resultado, recolección de datos para el control del proceso.

Dinamica → Pruebas

- Tengo un producto. Caja negra → Entrada, veo salida. Se crean casos de prueba: par ordenado: (Valor Entrada, Salida Esperada) → Si no se cumple detecto un error. Desventaja, no sé donde está.
- Son más rapidas. Ventaja.

Clasificación de las pruebas, son una banda y va a x3 el chancho.

Según: quien prueba, que se prueba, como se diesñan, 

![image.png](Clase%202%20Brozo/image.png)

## Casos de Prueba - TriMaster Tarea

Casos de Prueba  ( Valor Entrada → Resultado Esperado )

(10, 10, 10) → Equilatero

(8, 8, 6) → Isósceles

(1, 2, 6) → Escaleno

( 10, 1, 2) → “No es un Triangulo. La suma de dos lados tiene que ser mayor al tercero”

(0, 0, 0) → “Ingrese numero mayores a 0”

(-10, 6, -7) → “Ingrese numero mayores a 0”

(12345678, 98765432, 12345678) → “Ingrese numeros entre (0, 10000)”

(peke, arbol, tata) → “Ingrese unicamente numeros”

## Principios de Prueba

1. Una parte necesaria de un caso de prueba es una definición de la salida prevista o resultado.
2. Un desarrollador debe evitar tratar de poner a prueba su propio programa.
3. El personal de prueba no debería depender del área de desarrollo.
4. Inspecciones los resultados de la prueba.
5. Los casos de prueba deben ser escitos tanto para las condiciones de entrada esperadas como las no.
6. Examinar un programa para comprobar que no hace lo que se supone
7. Evitar casos de prueba desechables, sin documentar. **Pruebas de regresión** → Guardar casos de prueba y reejecutarlos al fixear errores, para chequear no romper cosas nuevas.
8. No se debe planear el esfuerzo de pruebas, con la suposición tácita de que no se encontrarán errores.
9. La probabilidad de encontrar errores adicionales en una sección de un programa es proporcional al número de errores ya encontrados en esa misma sección.
10. Las pruebas constituyen una tarea altamente creativa y son un desafio intelectual.

Una vez tengo los casos de prueba que detectaron error, se mandan a fixear.

Despues de fixear → Se vuelven a probar los mismos casos de prueba: **Pruebas de Regresion**

### Por qué el que desarrolla no debe ser quien prueba

- Desarrollo es un proceso creativo, probar es un proceso destructivo.
- Tunnel vision, el que desarrolla tiene muy clara la visión sobre su propio desarrollo y lo entiende de raiz.
- Error en planteamiento/entendimiento de algun requerimiento. Probar con el cliente → Pruebas estáticas con cliente.

### Donde fixear errores

- En los módulos donde mas haya, porque seguro sea más fácil que se encuentren, falle ese módulo.

# Técnicas de prueba

Para solucionar el tener que probar **exhaustivamente** todos los casos.

## Particionamiento de equivalencias

- Definir particiones, y crear grupos.
    - Particiones validas (debe permitir) y Particiones invalidas (debe rechazar)
    - Por cada partición se define un representante, se evalua el caso de prueba sobre el representante para saber si esa particion es válida o no.
    - Tabla
    - Creamos particiones en base al ratamiento que les va a dar el sistema a ese grupo de elementos, asigno un representante y pruebo.
    

## Particionamiento por valores límites

- Tener más de un caso de prueba por partición (sobre todo en las validas) para evaluar en los exremos, donde suele haber más problemas → De esta forma se mejora el Particionamiento por Equivalencia
- Suelen ser de mayor calidad.
- Para los casos numericos hay criterios para probar los extremos de las particiones. + - 1 de los límites.
- Para los casos alfanuméricos es distinto, si es una letra puede ser 1 cualquiera, si permite 3 valores especificos, habria que hacer 3 casos de prueba. Si fuera una cadena de caracteres fisica iría de ese tamaño, si fuera de hasta x cantidad de caracteres iria un caso de prueba por cada cantidad.

### Tarea recargo a pagar por retraso en la cuota de la escuela

Particiones válidas

1. Numeros enteros positivos entre 1 y 10
    1. Casos de prueba ( Valor entrada, Salida esperada )
        1. ( 1 , 0 )
        2. ( 21 , 4 )
2. Numeros enteros positivos entre 11 y 21
    1. Casos de Prueba 
        1. ( 11 , 2 )
3. Numeros enteros positivos entre 21 y 31
    1. Casos de prueba ( Valor entrada, Salida esperada )
        1. ( 21 , 4 )

Particiones Invalidas

1. Numeros negativos
2. Letras
3. Caracteres especiales
4. Numeros decimales
5. Numeros Enteros mayores a 31
6. Vacio

| ATRIBUTO | DOMINIO | VALIDAS | INVALIDAS |
| --- | --- | --- | --- |
| Día del mes | entero positivo entre 1 y 31 | PV1) 1 ≤ X ≤ 10 | PI1) letras |
|  |  | PV2) 11 ≤ X ≤ 20 | PI2) X ≤ 0 |
|  |  | PV3) 21 ≤ X ≤ 31 | PI3) X ≥ 31 |
|  |  |  | PI4) vacio |
|  |  |  | PI5) imagen |
|  |  |  | PI6) caracter especial |
|  |  |  | PI7) cadena de caracteres |

| Casos de prueba | Particion | Entrada | Salida |
| --- | --- | --- | --- |
| 1 | PV1 | 1 | 0 |
| 2 | PV2 | 12 | 2 |
| 3 | PV3 | 30 | 4 |
| 4 | PI1 | a | error? |
| 5 | PI2 | -1 | error? |
| 6 | PI3 | 32 | error? |
| 7 | PI4 |  | error? |
| 8 | PI5 | foto | error? |
| 9 | PI6 | * | error? |
| 10 | PI7 | pepe | error? |

![image.png](Clase%202%20Brozo/image%201.png)

| ATRIBUTO | DOMINIO | VALIDAS | INVALIDAS |
| --- | --- | --- | --- |
| Codigo del banco | entero positivo entre 1 y 999 o en blanco | PV1) 1 ≤ X ≤ 999
PV2) [ ] | PI1) letras
PI2) X ≤ 0 
PI3) X ≥ 999
PI4) vacio |
| Codigo de Sucursal | entero entre 1 y 9999 | PV1) 1 ≤ X ≤ 9999 | PI1) letras
PI2) X ≤ 0 
PI3) X ≥ 9999
PI4) vacio |
| Numero de Cuenta | nro de 5 digitos  | PV1) 12345 | PI1) 123456 |
| Clave personal | valor alfanumerico de 5 posiciones | PV1) string de 5 de largo alfanumerico | PI1) clave.length() > 5
PI2) clave.length() < 5 |
| Orden | 3 particiones: [vacio, talonario, movimientos] |  |  |
|  |  |  |  |

[6ab723ce-74df-4443-8597-452bb28f48b8_Tarea_recargo_a_pagar_por_retraso_en_la_cuota_de_la_escuela.pdf](Clase%202%20Brozo/6ab723ce-74df-4443-8597-452bb28f48b8_Tarea_recargo_a_pagar_por_retraso_en_la_cuota_de_la_escuela.pdf)