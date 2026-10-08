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
C100; C121/C131 → C111; ambas confirmadas por la empresa). Script:
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
C13035165 azul) y **C1003538** (7.º, 128 millares, 66 %). El C6106351 baja a 12 % medido en millares. **Decidido
(07/10/2026)**: entran C1003516 y C1003538, salen C9157050 y C3914050 (menos de 1 millar por año).

## Selección (15 artículos, v5 — 07/10/2026)

Demanda en millares por código de fabricación (presupuestado, 12 meses). "Puesto" = ranking por millares entre
los 223 códigos de fabricación del universo con precio.

| Código fabricación | Familia | Millares | Fill rate | Puesto | ULI en seguimiento | Perfil |
|---|---|---:|---:|---:|---:|---|
| C8114232 | CASER-Drill | 818,0 | 18 % | 1 | 16 | horno + revenido |
| C1003551 | CASER-Wall | 279,5 | 85 % | 2 | 1.092 | horno |
| C1003532 | CASER-Wall | 257,0 | 76 % | 3 | 415 | horno |
| C1003516 | CASER-Wall | 211,0 | 77 % | 4 | 104 | horno |
| C1113516 | CASER-Fix | 181,5 | 83 % | 6 | 136 | horno |
| C1003538 | CASER-Wall | 128,0 | 66 % | 7 | 353 | horno |
| C4104213 | CASER-Drill | 124,0 | 47 % | 8 | 221 | horno + revenido |
| C3104213 | CASER-Wall | 81,0 | 25 % | 11 | 371 | horno |
| C6106351 | CASER-Drill | 74,5 | 12 % | 13 | 420 | horno + revenido |
| C1115040 | CASER-Fix | 61,5 | 2 % | 16 | 57 | horno |
| C4104219 | CASER-Drill | 59,0 | 46 % | 19 | 62 | horno + revenido |
| C2003525 | CASER-Wall | 42,0 | 40 % | 24 | 399 | horno |
| C1004275 | CASER-Wall | 32,8 | 85 % | 30 | 294 | horno |
| C1114050 | CASER-Fix | 32,5 | 97 % | 31 | 223 | horno |
| C7006008 | CASER-Max | 5,0 | 100 % | 103 | 21 | sin horno |

Cubre el **52 %** de los millares del universo (2.387 de 4.567), con fill rate ponderado de 49 % contra 53 % del
universo. Incluye los tres perfiles y cuatro familias (Wall, Fix, Drill, Max). El C8114232 tiene pocas ULI (16) pero
grandes: ~60 millares cada una, 960 desde 2023, coherente con que se entregue solo el 18 % de lo presupuestado.

**Quedan afuera**: CASER-Rosc (el mejor candidato, C7404813, tiene 6 ULI en el seguimiento) y CASER-Plast
(1 unidad vendida en el año): sin datos suficientes para caracterizarlos. También CASER-Maq: sus artículos sin
horno venden menos de 1 millar por año. El C7006008 queda solo para ejercitar el camino que saltea el horno, no
para medir servicio.

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
