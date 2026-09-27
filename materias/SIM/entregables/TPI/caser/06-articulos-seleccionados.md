# Artículos representativos del Tema 1 — propuesta

> Universo de partida: los 310 artículos de `datos-locales/_perfil/candidatos_articulos2.csv` (catálogo
> CASER con precio en la Lista CASER, sin códigos KIT). Criterio: mezcla de familias, de volumen, de fill
> rate, y mayoría que pase por el horno con al menos un caso que no.

## Hallazgo previo a la selección

Los códigos de venta de mayor volumen son mayormente variantes de **estuche** (empaque chico), y el
seguimiento de producción (`Seguimiento TR ulis`) está anotado contra el código **granel** de fábrica —
mismo producto físico, dos códigos distintos. Sin corregirlo, solo 14 de 310 artículos parecían pasar por
el horno; corrigiendo (cada código de venta enlazado a su código de fábrica por prefijo), son **205 de 310**.
Implicancia para el modelo: la demanda de un artículo representativo debe sumar sus ventas por granel y por
estuche cuando corresponda — son la misma producción, dos canales de venta.

## Propuesta (15 artículos, pendiente de confirmación con la empresa)

| Código | Familia | Volumen/año | Pasa horno | Fill rate | Nota |
|---|---|---|---|---|---|
| C8114232 | CASER-Drill | 813 | Sí | 18% | pérdida grande — caso de estudio central |
| C1003551 | CASER-Wall | alto (+ estuche C10035515) | Sí | 87% | alto volumen, buen fill rate |
| C1003532 | CASER-Wall | alto (+ estuche) | Sí | — | alto volumen |
| C1113516 | CASER-Fix | 349 (+ estuche) | Sí | 82% | |
| C4104213 | CASER-Drill | medio (+ estuche) | Sí | — | |
| C7003510 | CASER-Drill | 190 | Sí | 32% | pérdida media |
| C7404813 | CASER-Rosc | 93 | Sí | 95% | fill rate alto, contraste |
| C1114520 | CASER-Fix | 90 | Sí | 78% | |
| C1115040 | CASER-Fix | 123 (+ estuche) | Sí | **1,6%** | pérdida casi total — caso extremo |
| C1004275 | CASER-Wall | medio (+ estuche) | Sí | — | |
| C2003525 | CASER-Wall | 84 | Sí | 40% | |
| C8203913 | CASER-Drill | 63 | Sí | 65% | |
| C8506350 | CASER-Max | bajo | Sí | — | familia distinta, artículo especial |
| C3914050 | CASER-Maq | bajo | Sí | — | familia distinta, artículo especial |
| C3224030 | CASER-Plast | bajo | **No** | — | caso bypass del horno (rosca para plásticos) |

Cubre las 7 familias del catálogo, mezcla alto/bajo volumen y fill rate alto/bajo/extremo, y tiene el único
caso relevante de "no pasa por horno" entre los artículos con datos.

## Pendiente

- Confirmar con la empresa si alguno de estos 15 no es representativo en la práctica (por ejemplo, si algún
  código está discontinuado pese a tener ventas históricas).
- De estos 15, verificar cuáles llevan revenido (ninguno de los 310 del universo general lo lleva según
  `Termico 2026`/Revenido, pero conviene confirmarlo específicamente para estos).
- Confirmar si alguno es de las excepciones que sí se mantienen con stock (regla general: todo contra
  pedido).
