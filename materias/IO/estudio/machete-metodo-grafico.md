# Machete — Método gráfico

Una carilla. La teoría completa está en [[resumen-hasta-simplex]].

## El procedimiento

```
1. VARIABLES      con unidad Y periodo.  "x1: piezas A por semana"
2. FUNCION OBJ    Max z = c1 x1 + c2 x2.  Solo los cj. Nunca los recursos.
3. RESTRICCIONES  una por RECURSO = una por COLUMNA de la tabla
                     recurso disponible  ->  <=
                     minimo exigido      ->  >=
4. FORMA ESTANDAR  <= suma holgura   |   >= resta exceso
5. CORTES          x1 = b/a1   y   x2 = b/a2      (sacar decimales antes)
6. GRAFICO         semiplano: probar (0;0). Si cumple, es el lado del origen.
7. VECTOR NORMAL   n = (c1 ; c2).  Max: empujo en ese sentido. Min: al reves.
8. OPTIMO          sistema 2x2 de las dos restricciones que se cruzan ahi
9. HOLGURAS        holgura = bi - lado izq        exceso = lado izq - bi
10. RESPUESTA      S* vector columna + interpretacion en castellano
```

## Los cuatro tipos de solución

```
UNICA          la recta de isobeneficio toca UN vertice
ALTERNATIVAS   queda PARALELA a una restriccion activa -> toca todo un lado
NO ACOTADA     se puede empujar para siempre
INCOMPATIBLE   no hay RF: las restricciones se contradicen
```

> Región factible no acotada **≠** solución no acotada. Lo marca el profesor a mano en la resolución del parcial.

## Clasificación de restricciones

```
holgura = 0   ->  ACTIVA      (pasa por el optimo)
holgura > 0   ->  PASIVA
                    |- NECESARIA:   forma parte del borde de la RF
                    |- REDUNDANTE:  si la saco, la RF no cambia
                          |- geometrica: la recta NO toca la RF
                          |- analitica:  la toca en un vertice que ya
                                         definen otras dos restricciones
```

Activa/pasiva habla del **punto óptimo**. Necesaria/redundante habla de **toda la RF**.
Una restricción puede ser pasiva y aun así imprescindible.

## Formato de respuesta de la cátedra

```
         40
         40                Se producen 40 piezas A y 40 piezas B por semana.
S*  =     0                Se agotan las horas de estampado y de soldado.
          0                Sobra una capacidad de 80 hs semanales en pintado.
         80                El beneficio maximo semanal es de 200 u.m.

z* = 200
```

Vocabulario: **recta de isobeneficio**, **RF**, **variables ficticias**, **se cumple con holgura**.
Justificaciones de una oración: *afirmación + porque/ya que/por lo tanto + el hecho numérico*.

## Las cuatro trampas

| Trampa | Antídoto |
|---|---|
| Leer la tabla por **fila** | Cada restricción es un recurso = una **columna** |
| Recursos en hs, insumos en min | Chequeo dimensional antes de escribir |
| Tope de **un** producto modelado como total | ¿A qué sustantivo se refiere el tope? |
| Dividir por decimales | ×10 y simplificar **antes** de dividir |

## Los dos controles que salvan

**Antes de dibujar.** Cortes en columna: ¿están todos en la misma escala? Si uno da 2,5 y el
resto 300, se rompió algo.

**Al encontrar el óptimo.** Un vértice tiene **al menos 2 restricciones activas** (contando
ejes). Si te sobra de todo, no estás en un vértice: todavía podés mejorar.

**Al terminar.** Holgura negativa = punto no factible = error en el sistema. No sigas.

## Casos particulares

```
restriccion con solo x1     ->  recta VERTICAL, no tiene segmentaria
restriccion con solo x2     ->  recta HORIZONTAL
optimo sobre un eje         ->  un producto NO se fabrica: decilo explicito
soluciones alternativas     ->  2 vectores S* + parametrica P = a·P1 + (1-a)·P2
                                los extremos son BASICOS, los del medio NO
```
