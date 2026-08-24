# IO — Práctica 2: Modelización

Guía completa de la Práctica 2 (`PL2UTN.pdf`): cómo modelizar, más los ejercicios
resueltos. Contrastado con la resolución oficial de la cátedra (`PL2UTNresol.pdf`) y
con la sección **1.4 del apunte** (PLC1), que es el catálogo de patrones.

> **Práctica 2 termina en el planteo.** No se resuelve. La resolución oficial de la
> cátedra, para los cinco ejercicios, llega hasta `xj >= 0` y corta: no hay una sola
> tabla ni un valor óptimo en todo el PDF. Lo que se corrige es: variables bien
> definidas, FO correcta, y restricciones completas con el signo correcto.

---

# Parte 1 — Cómo modelizar

## El procedimiento

Siempre el mismo, cuatro preguntas en este orden:

```
1. ¿QUE DECIDO?                     ->  variables de decision
2. ¿QUE QUIERO?                     ->  funcion objetivo
3. ¿QUE ME LIMITA?                  ->  restricciones
4. ¿QUE NO PUEDE SER NEGATIVO?      ->  no negatividad y variables extra
```

La trampa es empezar por la 3. Sin variables claras, las restricciones salen mal escritas.

## Cuántos índices lleva la variable

Decí la decisión en voz alta y contá cuántas cosas tenés que especificar:

```
"producir 40 piezas A"                 -> UNA especificacion  -> un indice:  x1, x2
"vender 5.000 L de nafta a la est. B"  -> DOS                 -> doble:      x_ij
"enviar 300 dosis de la cia. 2 a la
 ciudad 1 para ancianos"               -> TRES                -> triple:     x_ijk
```

**Cada especificación es un índice.**

Pero ojo con el criterio para *no* agregar de más:

> **Un índice se agrega solo si algún coeficiente o alguna restricción distingue
> según ese índice.** Si el costo no cambia con `k`, el índice `k` duplica variables
> y no aporta nada.

## El formato de la cátedra

Literal de las resoluciones oficiales:

```
x : cantidad de empleados que inician su secuencia de 5 dias el dia j;
 j    j = 1 (lun. a vier.), 2 (mar. a sab.), 3 (mier. a dom.), 4 (jue. a lun.),
      5 (vier. a mar.), 6 (sab. a mier.), 7 (dom. a jue.)

x  : cantidad invertida en la opcion i en el instante j;
 ij   i = A, B, C, D;  j = 0 (inicio año 1), 1 (inicio año 2), ...

x   : cantidad de vacunas enviadas por la cia. i, a la ciudad j, destinadas
 ijk  a la poblacion k;  i = 1, 2;  j = 1, 2, 3;  k = A (ancianos), O (otros)
```

Molde: **sustantivo con unidad + preposición + a qué se refiere cada índice**, y
después la **enumeración completa** de qué vale cada índice. Un índice sin enumerar
es media definición.

## Catálogo de patrones (sección 1.4 del apunte)

| Patrón | El tell del enunciado | Ejemplo apunte |
|---|---|---|
| Mezcla / dieta | "cada kg contiene tanto de tal nutriente" | 1-2, 1-3 |
| Planificación de producción | "cada producto consume tanto de cada recurso" | 1-4 |
| Precios según cantidad | descuentos, escalas de precio | 1-5 |
| **Cobertura cíclica (RRHH)** | "turnos", "días/horas consecutivas", mínimo por período | **1-6** |
| Cartera de inversiones | porcentajes, "riesgo promedio", "al menos el X%" | 1-7 |
| **Multiperíodo** | "al cabo de N años", "reinvertir", horizonte temporal | **1-8** |
| **Transporte** | orígenes con oferta, destinos con demanda | **1-9** |
| Corte de material | "minimizar desperdicio", patrones de corte | 1-10 |
| **Asignación con pérdida** | "el costo de lo no hecho es la ganancia no percibida" | **1-11** |

## Las cinco técnicas

### a) Cobertura cíclica — la variable NO es lo que parece

El error natural: `x_j = cantidad que TRABAJA en el período j`. **Está mal**: con esa
definición no podés imponer que cada persona trabaje N períodos consecutivos.

La correcta: `x_j = cantidad que INGRESA al inicio del período j`.

Así la consecutividad **queda incorporada en la definición de la variable** y no hay
que escribirla como restricción. Y además la FO cuenta a cada persona una sola vez
(con la otra definición, sumar daría el doble).

Una restricción **por período**: para el período `j`, sumás todas las variables cuya
secuencia lo cubre. Nunca se agrupan períodos ni se suman requerimientos.

**Es cíclico:** el día (o la semana) se cierra sobre sí mismo. Siempre hay una
restricción donde el índice se da vuelta. Renumerar la mueve de lugar, no la elimina.
Conviene declarar la convención una vez:

```
   x     +  x   >=  requerimiento           j = 1, ..., n
    j-1      j                   j

   con la convencion  x  = x     (el periodo anterior al primero es el ultimo)
                       0     n
```

### b) Proporciones y promedios — hay que linealizar

Una restricción de porcentaje **nunca queda con la división puesta**. Multiplicás por
el denominador y pasás todo a la izquierda; el término independiente suele quedar en 0.

```
"el riesgo promedio no debe superar el 5%"

   0,02x1+0,05x2+0,03x3+0,04x4+0,08x5
   ----------------------------------  <=  0,05
        x1+x2+x3+x4+x5

   ->  0,03x1 + 0,02x3 + 0,01x4 - 0,03x5  >=  0

"al menos el 20% en prestamos comerciales"

   x4 >= 0,2(x1+x2+x3+x4+x5)
   ->  -0,2x1 - 0,2x2 - 0,2x3 + 0,8x4 - 0,2x5  >=  0

"el monto combinado de personales y privados no puede superar el de publicos"

   x2 + x5 <= x1     ->     x1 - x2 - x5  >=  0
```

### c) Multiperíodo — restricciones de balance

Dos ideas:

**1. Una variable extra para lo que no se invierte:** `y_j` = cantidad no invertida en
el instante `j`. Sin ella el modelo obliga a invertir todo siempre.

**2. Una restricción de balance por instante:**

```
lo que TENGO disponible en j  =  lo que INVIERTO en j  +  lo que DEJO parado
```

"Lo que tengo" = lo que **vence** en ese instante (con capital + retorno) **más** lo
que quedó sin invertir del instante anterior.

```
inicio año 1:   xA0 + xB0 + y0  =  30.000
inicio año 2:   y0  =  xA1 + xB1 + xC1 + y1
inicio año 3:   1,3 xA0 + y1  =  xA2 + xB2 + y2
inicio año 4:   1,5 xB0 + 1,3 xA1 + y2  =  xA3 + y3
inicio año 5:   1,5 xB1 + 1,3 xA2 + y3  =  xD4
```

Los coeficientes son **capital + retorno**: si A devuelve $0,30 por peso, el
coeficiente es **1,3**, no 0,3. La FO suma solo lo que **madura al final** del horizonte.

### d) Transporte — doble índice

```
x  : cantidad enviada desde el origen i al destino j

Min w = SUM_i SUM_j  c_ij x_ij
SA
   una restriccion por ORIGEN   ->  lo que sale de i
   una restriccion por DESTINO  ->  lo que llega a j
```

El signo de cada una lo decide el balance oferta/demanda. Si la demanda supera a la
oferta, la oferta se agota (`=`) y la demanda va acotada por arriba (`<=`).

### e) La variable de "lo que no se hizo"

Cuando el enunciado dice *"el costo de un pasajero perdido es la ganancia no percibida"*
o *"el capital no invertido va a depósitos"*, esa opción **necesita su propia variable**:

```
s : cantidad de pasajeros NO transportados en el itinerario i
 i
```

y entra en la FO con su **costo de oportunidad**. Sin ella el modelo no puede elegir
"no hacer algo", que es justo la decisión que el problema plantea.

## Errores típicos

```
1. Definir la variable por el PERIODO en vez de por el INGRESO (cobertura ciclica)
2. Agrupar periodos y sumar requerimientos en una sola restriccion
3. Dejar una restriccion de porcentaje con la division puesta
4. Olvidar la variable de "lo no invertido" / "lo no hecho"
5. Poner solo el retorno (0,3) en vez de capital + retorno (1,3) en multiperiodo
6. No enumerar los indices en la definicion de variables
7. Olvidar el TECHO cuando el enunciado da una demanda: la demanda suele funcionar
   en las dos direcciones (piso si hay compromiso, techo porque nadie compra de mas)
```

## Cómo se entrega

Cuando hay que **precalcular coeficientes** (descuentos, contribuciones marginales), va
un bloque aparte **antes** del modelo. Tres bloques:

```
1) definicion de variables
2) calculo de coeficientes      (solo si hace falta)
3) formulacion del modelo
```

Y la cátedra usa `Max z` para maximización y **`Min w`** para minimización, para poder
escribir `w = -z` y, en dualidad, `W* = z*`.

---

# Parte 2 — Ejercicios resueltos

## Ejercicio 1 — Nafta y gasoil

Distribuidora que vende nafta ($30/L) y gasoil ($10/L) a tres estaciones. Capacidad:
22.000 L de nafta y 11.000 de gasoil. B y C tienen 5% y 8% de descuento. A las tres se
les debe vender al menos el 80% de lo que solicitan. Costos fijos de envío: $200, $300, $500.

| Estación | Costo fijo | Demanda nafta | Demanda gasoil |
|---|---|---|---|
| A | $200 | 10.000 | 5.000 |
| B | $300 | 8.000 | 4.500 |
| C | $500 | 7.000 | 3.000 |

```
1) VARIABLES

   x  : cantidad de litros del producto i vendidos a la estacion j
    ij     i = 1 (nafta), 2 (gasoil)
           j = A, B, C

2) CALCULO DE LOS PRECIOS EFECTIVOS

   Estacion A:  nafta 30                gasoil 10
   Estacion B:  nafta 30 x 0,95 = 28,50    gasoil 10 x 0,95 = 9,50
   Estacion C:  nafta 30 x 0,92 = 27,60    gasoil 10 x 0,92 = 9,20

3) MODELO

   Max z = 30 x1A + 28,50 x1B + 27,60 x1C
              + 10 x2A + 9,50 x2B + 9,20 x2C  - 1.000

   SA
   1)   x1A + x1B + x1C  <=  22.000            (capacidad nafta)
   2)   x2A + x2B + x2C  <=  11.000            (capacidad gasoil)

   3)   x1A >=  8.000      6)   x2A >= 4.000   (80% de lo solicitado)
   4)   x1B >=  6.400      7)   x2B >= 3.600
   5)   x1C >=  5.600      8)   x2C >= 2.400

   9)   x1A <= 10.000     12)   x2A <= 5.000   (no se vende mas de lo pedido)
  10)   x1B <=  8.000     13)   x2B <= 4.500
  11)   x1C <=  7.000     14)   x2C <= 3.000

  15)   x   >= 0
         ij

   Los costos fijos de envio suman $1.000 y se incurren siempre, ya que la
   restriccion de demanda minima obliga a abastecer a las tres estaciones.
   Al ser una constante, no altera la solucion optima, solo el valor de z.
```

**Lo que enseña:**

1. **Doble índice** con enumeración.
2. **Coeficientes precalculados** en bloque aparte (los descuentos).
3. **Una constante en la FO no mueve el óptimo**, solo su valor. Se puede incluir o omitir, pero hay que **justificarlo**.
4. **El costo fijo normalmente no es lineal.** "Si envío pago $200, si no envío pago $0" necesitaría una binaria `y_j` con `x1j + x2j <= M·y_j` (Unidad 8). Acá se puede tratar como constante **solo porque** el 80% obliga a abastecer a las tres.
5. **Cotas por los dos lados** sobre la misma variable. Sin el techo (restricciones 9 a 14), el modelo mandaría toda la nafta a la estación A, que es la de mayor precio, ignorando que A solo quiere 10.000 L.

> Validación (no se entrega): `z* = 742.240`, con las dos capacidades agotadas.
> Todo el excedente va a la estación A, la única sin descuento; B y C reciben
> exactamente su 80%. El descuento por fidelidad se paga en volumen.

## Ejercicio 2 — Mozos de cafetería (cobertura cíclica)

Cafetería abierta 24 hs. Seis franjas de 4 hs con mínimos de 4, 8, 10, 7, 12 y 4 mozos.
Cada mozo trabaja **8 hs consecutivas** = **2 franjas**.

```
1) VARIABLES

   x : cantidad de mozos que INGRESAN al inicio del turno j;
    j   j = 1 (2-6), 2 (6-10), 3 (10-14), 4 (14-18), 5 (18-22), 6 (22-02)

2) MODELO

   Min w = x1 + x2 + x3 + x4 + x5 + x6

   SA
   1)   x1                     + x6  >=   4      (2-6)
   2)   x1 + x2                      >=   8      (6-10)
   3)        x2 + x3                 >=  10      (10-14)
   4)             x3 + x4            >=   7      (14-18)
   5)                  x4 + x5       >=  12      (18-22)
   6)                       x5 + x6  >=   4      (22-02)

   7)   x  >= 0
         j
```

Coincide con la resolución oficial letra por letra.

**Lo que enseña:**

1. **La variable es el ingreso, no la presencia.** Con "mozos que trabajan en la franja j" no podés imponer las 8 hs consecutivas, y además la FO contaría a cada mozo dos veces.
2. **Una restricción por franja, nunca agrupadas.** Si sumás dos requerimientos en una sola (`x1+x2 >= 12`), el modelo acepta soluciones donde una franja queda **vacía**. Contraejemplo: `x = (12,0,17,0,0,16)` cumple las agrupadas, pero deja la franja 18-22 —la más cargada— **sin nadie**.
3. **Los coeficientes son 1**, no costos: el enunciado pide el mínimo *número*. Si diera sueldos por turno (como el Ejemplo 1-6 del apunte, donde el domingo se paga más), los `cj` serían distintos.
4. **La circularidad es del problema, no de la numeración.** Elijas el origen que elijas, siempre hay una restricción donde el índice se da vuelta.
5. **Cota inferior gratis:** sumando las seis restricciones, cada variable aparece exactamente dos veces, así que `2·(suma xj) >= 45` → `suma xj >= 22,5`. Sirve de control.

> Validación (no se entrega): `w* = 26`, con `x = (0, 8, 2, 5, 7, 4)`. Cinco
> restricciones activas y la de 22-02 con holgura 7: sobran 7 mozos de noche, pero
> no es evitable — son los que entraron a las 18 para cubrir el pico de 12 y se
> quedan 8 horas sí o sí. **La sobredotación nocturna es consecuencia forzada del
> pico de la tarde.**

## Ejercicio 3 — Vacunas contra la gripe (transporte)

Dos compañías con 1.100 y 900 (miles de) dosis. Tres ciudades con ancianos (325, 260, 195)
y otros (750, 800, 650). Hay que cubrir **al menos** a los ancianos, y el resto se vacuna
"mientras duren los suministros".

| Costos ($/dosis) | Ciudad 1 | Ciudad 2 | Ciudad 3 |
|---|---|---|---|
| Compañía 1 | 3 | 3 | 6 |
| Compañía 2 | 1 | 4 | 7 |

**La cuenta que define el modelo:**

```
STOCK      1.100 + 900              = 2.000
ANCIANOS   325 + 260 + 195          =   780
OTROS      750 + 800 + 650          = 2.200
NECESIDAD TOTAL                     = 2.980     ->  falta para 980
```

```
1) VARIABLES

   x  : cantidad de vacunas (en miles de dosis) enviadas por la compania i
    ij   a la ciudad j;     i = 1, 2;   j = 1, 2, 3

2) MODELO

   Min w = 3 x11 + 3 x12 + 6 x13 + 1 x21 + 4 x22 + 7 x23

   SA
   1)   x11 + x12 + x13                =  1.100     (stock cia. 1)
   2)                x21 + x22 + x23   =    900     (stock cia. 2)

   3)   x11 + x21  >=   325                         (ancianos ciudad 1)
   4)   x12 + x22  >=   260                         (ancianos ciudad 2)
   5)   x13 + x23  >=   195                         (ancianos ciudad 3)

   6)   x11 + x21  <= 1.075                         (habitantes ciudad 1)
   7)   x12 + x22  <= 1.060                         (habitantes ciudad 2)
   8)   x13 + x23  <=   845                         (habitantes ciudad 3)

   9)   x   >= 0
         ij
```

**Los tres signos, que es donde se juega el ejercicio:**

- **Stock con `=`**, porque el enunciado dice *"se los vacunará mientras duren los suministros"*: se reparte todo, no queda nada en depósito.
- **Ancianos con `>=`**, es el piso: *"al menos"*.
- **Otros con `<=`**, es el **techo**: no se le puede mandar a una ciudad más dosis que habitantes tiene. El techo de cada ciudad es `ancianos + otros`.

> **El error frecuente es ignorar la demanda de "otros".** Sin los techos, el modelo
> puede mandarle a la Ciudad 1 las 1.100 dosis de la Compañía 1, cuando la ciudad tiene
> 1.075 habitantes: 25 mil dosis para gente que no existe. Y si además el stock fuera
> `<=`, el óptimo enviaría solo 780 dosis y dejaría 1.220 guardadas en plena epidemia.

**Las dos formulaciones.** La resolución oficial da también una con **triple índice**
(`x_ijk`, con `k = A (ancianos), O (otros)`), de 12 variables, donde las restricciones
de ciudad se parten en `x11A + x21A = 325` y `x11O + x21O <= 750`.

Las dos son correctas, pero **conviene la de 6 variables**: el costo `c_ij` **no depende
de k** — mandar una dosis a la Ciudad 1 cuesta $3 vaya a un anciano o a otro habitante.
El índice `k` duplica las variables y no aporta nada a la FO. Haría falta solo si el
costo variara por población, o si hubiera una restricción que mezclara poblaciones
entre ciudades.

> Validación (no se entrega): `w* = 4.785`, con `x21 = 900` (toda la Compañía 2 por la
> ruta de $1), `x13 = 195` y `x11 + x12 = 905` repartidos libremente — **hay soluciones
> alternativas**, porque las dos rutas cuestan lo mismo ($3).
>
> Lectura para defensa: **la Ciudad 3 recibe solo sus ancianos y nadie más**, por ser la
> más cara de alcanzar. El criterio de costo mínimo **no reparte con equidad**; si se
> quisiera eso harían falta otras restricciones u otra función objetivo.

---

# Parte 3 — Pendientes

- **Ejercicio 4 — Inversión a 3 años.** Patrón multiperíodo (Ejemplo 1-8 del apunte). Atención a que la alternativa B *"sólo puede reinvertirse al cabo de 2 años"*. Tiene resolución oficial.
- **Ejercicio 5 — Aviones e itinerarios.** Asignación con variable de pérdida (Ejemplo 1-11). Tiene resolución oficial.
- Los dos ejercicios exclusivos de la versión nueva de la guía (`PL2 y modelizacion.pdf`): **plantas / artículos del hogar** y **frutos secos**. Sin resolución oficial, y sus tablas se perdieron en la conversión del PDF — hay que leerlas del original.
