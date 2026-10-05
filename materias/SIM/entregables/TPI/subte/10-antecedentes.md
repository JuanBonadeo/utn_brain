---
title: "Antecedentes y literatura - TPI Subte Constitución"
subject: "Simulación"
status: "Cinco papers de acceso abierto leídos el 2026-10-05; base del capítulo de antecedentes y de la justificación de supuestos"
---

# Antecedentes y literatura

El docente pidió buscar fuentes que nutran el modelo. Se bajaron y leyeron los cinco estudios de acceso abierto
más pertinentes. Los originales están en `materias/SIM/fuentes/papers-tpi-subte/` y su texto convertido en
`fuentes/txt/papers-tpi-subte/`. Cada dato lleva la sección o tabla de origen para poder citarlo.

## 1. Qué aporta cada estudio

| Estudio | Caso | Aporte para nuestro modelo |
|---|---|---|
| Seriani et al. (2025) | Estación Francia, Metro de Valparaíso, Chile. Salida en la hora pico, con observación y microsimulación (LEGION) | Tiempo de paso medido: **2 s** de media (Tabla 2). **Sesgo por cercanía**: el molinete más cercano al recorrido es el más usado (10 a 21 % entre seis molinetes); uno agregado lejos se usa el 0,4 %. **Valida** comparando el % de uso por molinete, simulado contra observado (±4 %) |
| Wang et al. (2024) | Estación Ciqunan, Pekín. 813 pasos por molinete medidos con video, AnyLogic 8.7 | Tiempo de molinete medido: **2,91 a 3,49 s** de media (Tabla 5), desde que el pasajero se detiene hasta que cruza. Depende del medio de pago (NFC más rápido que QR), del equipaje y del género. La elección combina cercanía y fila más corta (cualitativo) |
| Tian et al. (2026) | Estación de trasbordo que recibe pasajeros de un ferrocarril (análoga a Roca → Línea C), AnyLogic | Molinete U(3; 5) s y velocidades de U(0,6; 1,0) a U(0,8; 1,2) m/s, según la norma china GB/T 38707-2020. El **88,2 %** usa el grupo de molinetes más cercano a la salida del tren. Métricas: cola media por grupo, densidad con nivel de servicio de Fruin y tiempo de viaje. 10 réplicas con IC del 95 % |
| Li et al. (2024) | Andén del metro de Suzhou. Calibración del modelo de fuerza social con video (YOLOv5), AnyLogic 8.7 | Rango de velocidad deseada de la literatura: **1,1 a 1,5 m/s**, el mismo que usamos. Valor calibrado: **1,37 m/s** (Tabla 7). La calibración bajó el error de densidad a menos del 10 % en la mitad de los casos |
| Zhen et al. (2024) | Columbus Circle, Nueva York (Winter Simulation Conference 2024), AnyLogic con datos abiertos de molinetes | Antecedente de AnyLogic con datos de molinetes, como nuestro uso de SBASE. Procedimiento de limpieza: promedio de día hábil, sin feriados ni contadores rotos. Es débil: arribos Poisson sin oleadas y sin validación informada. Sirve como contraste |

## 2. Contraste con los supuestos del modelo

| Supuesto | Nuestro valor | Literatura | Lectura |
|---|---|---|---|
| Tiempo de validación | Triangular (1,8; 2,4; 3,5) s, media 2,57 s (TCQSM) | 2 s (Valparaíso); 2,9 a 3,5 s (Pekín); U(3; 5) s (norma china) | El intermedio cae dentro del rango observado. El contexto pesimista, (2,2; 3,0; 4,5) con media 3,23 s, cubre el caso de Pekín. Los valores dependen del medio de pago: SUBE es una tarjeta sin contacto, como NFC |
| Velocidad de caminata | U(1,1; 1,5) m/s | 1,1 a 1,5 m/s, calibrado en 1,37 (Suzhou); 1,5 a 1,57 de media (Valparaíso); 0,6 a 1,2 con equipaje (norma china) | Se sostiene con Li et al. (2024). La norma china es más lenta porque incluye equipaje, que en Constitución en el pico de la mañana es raro: se declara |
| Diámetro del peatón | 0,5 m | Ninguno de los cinco lo informa | Hay que citar otra fuente (Fruin; el valor por defecto de AnyLogic) o declararlo |
| Elección de molinete | Desvío lateral más asignados × servicio | Sesgo fuerte por cercanía (Seriani; Tian, 88,2 %); cercanía y cola (Wang) | Confirma que el término de desvío es necesario. Advierte que **dónde** quedan los 2 molinetes extra de E1 pesa tanto como **cuántos** son |
| Oleadas del tren | 47 trenes, descarga de 145 s, demora de 106 s | Zhen (2024) usa Poisson, sin oleadas | Nuestro modelo captura algo que ese antecedente no: es un aporte |

## 3. Ideas para incorporar

1. **Validación por uso de molinete** (Seriani et al., 2025). Comparar la distribución simulada del uso
   entre molinetes con la observada en SBASE. Como el plano es hipotético, la correspondencia uno a uno no es
   posible: se compara la **forma** de la distribución (rango y desbalance entre el más y el menos usado; en
   SBASE el factor es de ~11).
2. **Métricas adicionales** (Tian et al., 2026): cola media por grupo de molinetes y densidad en la zona de
   espera, con nivel de servicio de Fruin.
3. **Sensibilidad del servicio hacia 3 s.** Wang (2024) y Tian (2026) miden más de 2,9 s. El contexto
   pesimista ya lo cubre: hay que decirlo en el informe.
4. **Trabajo futuro:** validación con QR o EMV (Wang, 2024, muestra que el QR es más lento) y molinetes
   bidireccionales.

## 4. Referencias (APA 7)

- Li, T., Xu, B., Lu, W., Chen, Z., Zhang, S., & Xia, F. (2024). The parameter calibration of social force
  model for pedestrian flow simulation based on YOLOv5. *Sensors, 24*(15), 5011.
  https://doi.org/10.3390/s24155011
- Seriani, S., Aprigliano, V., Peña, A., Garrido, A., Arredondo, B., Minatogawa, V., Falavigna, C., &
  Fujiyama, T. (2025). Crowd management at turnstiles in metro stations: A pilot study based on observation
  and microsimulation. *Systems, 13*(2), 95. https://doi.org/10.3390/systems13020095
- Tian, Y., Jin, G., Lu, S., Ma, W., Li, N., Cao, G., & Wang, W. (2026). Simulation-based optimization
  analysis of passenger flow organization in metro interchange stations using AnyLogic. *Scientific Reports,
  16*, 12517. https://doi.org/10.1038/s41598-026-41719-5
- Wang, Y., Yuan, R., Tong, X., Bai, Z., & Hou, Y. (2024). Towards simulation optimization of subway station
  considering refined passenger behaviors. *PLOS ONE, 19*(6), e0304081.
  https://doi.org/10.1371/journal.pone.0304081
- Zhen, D., Liu, Z., Chen, Y., & Cui, Q. (2024). Enhancing passenger flow at subway transfer stations through
  simulation modeling. En H. Lam et al. (Eds.), *Proceedings of the 2024 Winter Simulation Conference*
  (pp. 1398-1409). IEEE. [DOI a completar desde IEEE Xplore]

**Para citar sin haberlos leído completos** (no son de acceso abierto; se mencionan por su resumen):
- Helbing, D., & Molnár, P. (1995). Social force model for pedestrian dynamics. *Physical Review E, 51*(5),
  4282-4286. Es la base del movimiento en la Pedestrian Library.
- Yanagisawa, D., et al. (2013). Walking-distance introduced queueing model for pedestrian queueing system:
  Theoretical analysis and experimental verification. *Transportation Research Part C*. Incorpora la
  caminata a la teoría de colas, lo mismo que hace nuestra regla de elección.
