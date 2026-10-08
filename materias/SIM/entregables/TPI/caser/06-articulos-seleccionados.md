# Artículos representativos del Tema 1 — propuesta (v2, 2026-10-07)

> Reemplaza la propuesta del 2026-09-27, que tenía errores en las columnas "pasa horno" y "revenido" (ver
> "Qué se corrigió"). Fuente de verdad para esas dos columnas: `Seguimiento TR ulis` (12.527 ULI, 2023-2026),
> a nivel de código base de fábrica. Tablas completas en `datos-locales/_perfil/candidatos_v3.csv`.

## Hallazgos que condicionan la selección

**1. Estuche vs. granel.** Los códigos de venta de mayor volumen son variantes de estuche y la producción se
registra contra el código granel de fábrica (mismo producto, dos códigos). Se enlazan por prefijo del código.
La demanda de un artículo representativo suma sus ventas por granel y por estuche. Los volúmenes mezclan
unidades de facturación (estuches y millares), así que los porcentajes de volumen son indicativos.

**2. El revenido es por artículo y casi binario.** De 193 artículos base: 74 pasan por el horno sin revenido,
24 por horno y revenido (77-100 % de sus ULI), 8 no pasan por el horno y 87 no tienen datos suficientes
(menos de 15 ULI en el seguimiento). **Los 24 con revenido son todos de CASER-Drill.**

**3. Los artículos con revenido son los peor servidos.** Fill rate ponderado de los artículos de horno solo:
**66 %** (74 artículos). Con revenido: **33 %** (24 artículos). Es co-ocurrencia dentro de una familia: como
todos los de revenido son Drill, no se puede separar el efecto del revenido del efecto de la familia.
Implicancia para el alcance: sacar el revenido de la cola simulada es razonable (el estudio cambia la regla
del horno de cementación, no la del de revenido), pero **los artículos con revenido no deben excluirse de la
selección** — son el 22 % del volumen y donde está el problema de servicio. Para ellos el revenido entra
como una demora aleatoria con la distribución empírica (ver `03-pedido-de-datos.md`), no como constante.

**4. Casi todo el volumen pasa por el horno.** Ponderado por volumen: 63 % horno solo, 22 % horno + revenido,
15 % sin datos suficientes, ~0 % sin horno. Los 8 artículos sin horno son CASER-Max y CASER-Maq de volumen
mínimo. CASER-Plast **sí** pasa por el horno (C3224020: 100 % de sus 28 ULI): la suposición anterior de que
las roscas para plásticos no se tratan era incorrecta.

**5. Hexagonales tipo 1: se fabrican como C6x0 y se venden como C6x1 (empresa, 07/10/2026).** Los C610.../C630...
se venden con la arandela vulcanizada colocada como C611.../C631...: mismo producto físico, mismos procesos. La
v3 dejaba esos 30 códigos de venta (259 de presupuestado) sin código de fábrica. Corregido en
`datos-locales/_perfil/seleccion_v4.py`. El C6106351 pasa de 47 a 127 de presupuestado, pero su fill rate sigue
en 21 %: sigue siendo de los peor servidos. Los fill rate por perfil no cambian (66 % horno solo, 33 % con revenido).
**Pendiente de confirmar**: los C110... ("DOR") y C130... ("AZUL") siguen sin enlazar (512 de presupuestado; el
C13035165 solo tiene 297). Parecen el mismo tornillo que el C100... con otro color de zincado.

**6. Demanda en millares y por código de fabricación (v5, 07/10/2026).** Hasta la v4 se sumaba "presupuestado" de
códigos de granel (millares) con códigos de estuche (unidades de estuche) sin convertir. Ahora cada línea se pasa a
millares con "Unidades por Envase" de la Lista CASER (un C13035165, estuche x500, = 0,5 millar del C1303516), y
cada código de venta se lleva a su código de fabricación: arandela (C6x1 → C6x0) y color de zincado (C110/C130 →
C100, confirmado por la empresa; C121/C131 → C111 por analogía, **a confirmar**). Script:
`datos-locales/_perfil/seleccion_v5.py`. El 100 % de los millares queda con código de fabricación en el seguimiento.

| Perfil | Artículos | Millares | % | Fill rate |
|---|---:|---:|---:|---:|
| Horno solo | 77 | 2.354 | 52 % | 69 % |
| Horno + revenido | 26 | 1.292 | 28 % | 27 % |
| Sin horno | 8 | 7 | 0 % | 70 % |
| Pocos datos (< 15 ULI) | 112 | 914 | 20 % | 46 % |
| **Total** | 223 | 4.567 | | 53 % |

Con esta medida los 15 de abajo cubren el 45 % de los millares, con fill rate 45 % (sesgo hacia los mal servidos,
por el peso del C8114232). Faltan dos de los más vendidos: **C1003516** (4.º, 211 millares, 77 %; absorbe al
C13035165 azul) y **C1003538** (7.º, 128 millares, 66 %). El C6106351 baja a 12 % medido en millares. Propuesta
pendiente de decidir con el grupo: sumar C1003516 y C1003538 y sacar C9157050 y C3914050 (menos de 1 millar por año).

## Propuesta (15 artículos, pendiente de confirmación con la empresa)

| Código base | Familia | Volumen presup. | Fill rate | ULI en seguimiento | Horno | Revenido |
|---|---|---:|---:|---:|---:|---:|
| C1003551 | CASER-Wall | 542 | 87 % | 1.092 | 98 % | 0 % |
| C1003532 | CASER-Wall | 492 | 78 % | 415 | 99 % | 0 % |
| C3104213 | CASER-Wall | 162 | 25 % | 371 | 98 % | 0 % |
| C1004275 | CASER-Wall | 156 | 87 % | 294 | 94 % | 0 % |
| C2003525 | CASER-Wall | 84 | 40 % | 399 | 98 % | 0 % |
| C1113516 | CASER-Fix | 349 | 82 % | 136 | 100 % | 0 % |
| C1115040 | CASER-Fix | 123 | **2 %** | 57 | 98 % | 0 % |
| C1114050 | CASER-Fix | 65 | 97 % | 223 | 100 % | 0 % |
| C8114232 | CASER-Drill | 823 | **18 %** | 16 | 100 % | 88 % |
| C4104213 | CASER-Drill | 248 | 47 % | 221 | 99 % | 93 % |
| C4104219 | CASER-Drill | 118 | 46 % | 62 | 100 % | 92 % |
| C6106351 | CASER-Drill | 127 | 21 % | 420 | 99 % | 77 % |
| C7006008 | CASER-Max | 5 | 100 % | 21 | **0 %** | — |
| C9157050 | CASER-Max | 2 | 0 % | 118 | **0 %** | — |
| C3914050 | CASER-Maq | 3 | 0 % | 48 | **0 %** | — |

Cubre 42 % del volumen presupuestado del universo con precio (3.299 de 7.935, con la corrección de la arandela),
con fill rate ponderado de 53 % contra 55 % del universo: la muestra no está sesgada hacia casos fáciles ni difíciles. Incluye los tres
perfiles (horno solo, horno + revenido, sin horno) y cinco de las siete familias.

**Quedan afuera**: CASER-Rosc (el mejor candidato, C7404813, tiene 6 ULI en el seguimiento) y CASER-Plast
(1 unidad vendida en el año): sin datos suficientes para caracterizarlos. Los tres artículos sin horno tienen
volumen de venta casi nulo; sirven para ejercitar el camino que saltea el horno, no para medir servicio.

## Qué se corrigió respecto de la propuesta del 27/09

- La columna "pasa horno" se había armado con una heurística sobre códigos de venta: C3914050 figuraba como
  "sí" y no pasa por el horno (0 de 48 ULI); C8506350 pasa en 2 de 11; C3224030 no tiene ULI en el seguimiento.
  Se reemplazaron por artículos con datos del seguimiento.
- Se afirmaba que ninguno de los 310 artículos llevaba revenido, midiendo solo la hoja 2026 de `Termico 2026`.
  Con el seguimiento completo, 4 de los 15 anteriores lo llevaban, y 24 artículos base en total.
- Se afirmaba que CASER-Plast no pasa por el horno; sí pasa.

## Pendiente

- Confirmar con la empresa si alguno de estos 15 está discontinuado o no es representativo en la práctica.
- Confirmar si alguno es de las excepciones que sí se mantienen con stock (regla general: todo contra pedido).
- Decidir si se sustituye alguno de los tres sin horno por un artículo de CASER-Rosc o CASER-Plast con más
  datos, si la empresa los considera importantes.
