---
title: "Guía de defensa - TPI Subte Constitución"
subject: "Simulación"
status: "Para la defensa del 10-11/11/2026; los números se completan con la producción de 10 días × 4 escenarios"
---

# Guía de defensa

Todo sale de los archivos de esta carpeta: [02-modelo-anylogic.md](02-modelo-anylogic.md), el informe
(`informe/`) y los scripts. Lo marcado *[general]* es conocimiento general, no verificado contra los
materiales de la materia.

## El argumento en una frase

> En la hora pico, los trenes del Roca descargan en oleadas y la cola de los molinetes de la Línea C es
> **transitoria**. Comparamos, con el mismo día real y los mismos pasajeros, la situación actual (E0, 20
> molinetes) contra tres alternativas: habilitar los 22 (E1), validar más rápido (E3) y las dos juntas (E13).
> Medimos el P90 de la espera y no el promedio, porque el promedio esconde la oleada.

## Recorrido sugerido (10-12 min)

| Min | Qué mostrar | Dónde |
|---|---|---|
| 0-1 | Problema y pregunta: oleadas del Roca → cola transitoria en el vestíbulo Principal | Informe §1-2 |
| 1-3 | **Bloque 1, Variables:** escenario (molinetes, validación), día real sorteado, trenes reales, generadores, supuestos [SUP] | Modelo, fila de arriba a la izquierda |
| 3-4 | **Bloque 2, Medidas:** las 3 primarias (P90, % > 30 s, P90 de la cohorte pico) y por qué no la media; panel en vivo | Modelo, arriba al centro |
| 4-5 | **Bloque 3, Lógica:** flujo del pasajero (PedSource → bajada por las escaleras → PedService → salida) y trenes | Modelo, arriba a la derecha |
| 5-7 | **Bloque 4:** correr `PeatonalFranjaVisualE0`: llega un tren, la gente baja por las 21 puertas, camina el hall, baja por las escaleras mecánicas, se forma la oleada en los molinetes; **mapa de calor** | Modelo, abajo |
| 7-10 | Resultados: tabla por escenario, forest plot (IC de Bonferroni), n* | Informe §10 |
| 10-12 | Conclusión, recomendación y limitaciones | Informe §11 |

Si la franja visual es lenta, avanzar la velocidad después del primer tren; tener capturas del mapa de calor
de E0 y E1 como respaldo.

## La teoría que hay que poder explicar

| Concepto | Qué decir | Dónde está en el modelo |
|---|---|---|
| Sistema **terminal** | Arranca vacío a las 07:00 y termina cuando sale el último que entró antes de las 09:30. No hay estado estable ni calentamiento | Corte a t = 9000 y drenaje |
| **Réplicas independientes** | Cada réplica = un día hábil real con su semilla → un valor por medida. El IC se arma con esos valores, nunca con las esperas de una misma mañana (están correlacionadas) | `diaSbasePed = -2`, semilla `20260923 + index/4` |
| **Números aleatorios comunes** | Mismo día, mismos trenes, mismos pasajeros y mismos sorteos en los 4 escenarios. Var(D) = Var(Xa) + Var(X0) − 2 Cov: la covarianza positiva achica el IC | Un generador por fuente: calle, servicio, velocidad, trenes |
| **t apareado** | Z_j = X_a,j − X_E0,j; IC t con n − 1 grados de libertad sobre las diferencias | `analisis_corridas.py`, planilla |
| **Bonferroni** | 3 primarias × 3 comparaciones = 9 intervalos; α_s = 0,05/9 para que la confianza conjunta sea ≥ 95 % | k = 9 en la planilla y en Python |
| **n necesario** | Piloto n0 = 10, n* = mínimo i con t·s/√i ≤ β (β = 1 s en percentiles, 0,01 en la proporción). Si n* > 10, se agregan días | Tabla de n* |
| **Verificación vs validación** | Verificar: el programa hace lo que dice el modelo (verificador automático, traza manual de 5 pasajeros). Validar: el modelo se parece a la realidad (caudal por ventana, reparto entre molinetes) | Informe §5 y §7 |

## Preguntas probables

- **¿Por qué P90 y no la media?** Porque la congestión es transitoria: la media de toda la franja diluye las
  oleadas. El P90 dice cuánto espera el pasajero que llega con la oleada.
- **¿Validaron la espera?** No. No hay datos de cola en Constitución; los molinetes registran a quien pasó.
  Validamos lo que el dato permite: caudal por ventana del mismo día y reparto entre molinetes (CV). Por eso la
  conclusión es comparativa: los escenarios comparten los supuestos.
- **¿De dónde sale el 80 % del Roca?** Es un supuesto. Intentamos estimarlo con regresión de validaciones contra
  trenes por ventana y no es identificable (IC [0,00; 0,28], cambia con el rezago). La matriz origen-destino del
  Roca lo hace verosímil.
- **¿Por qué 10 réplicas y no 30?** Cada corrida tarda ~170 s; 120 corridas eran 5,5 h. Usamos el procedimiento
  secuencial: piloto de n0 = 10, calculamos n* y agregamos días solo si hace falta.
- **¿El reparto entre molinetes es realista?** Es más parejo que el real (CV ~0,3 contra 0,56). Si los molinetes
  extra de E1 quedaran mal ubicados en la realidad, el modelo sobreestimaría su efecto. Está declarado.
- **¿Las escaleras son las reales?** Sí, las mecánicas del bloque central, según el plano de Trenes Argentinos.
  La plaza de transbordo y el interior del vestíbulo son supuestos: SBASE no envió el plano.
- **¿Por qué no todos los que bajan del tren van al vestíbulo?** Solo se modela a quien valida en el vestíbulo
  Principal (80 % de sus validaciones). El resto sale a la calle u otros accesos y no se simula.
- **¿Los peatones caminan todos igual?** No: velocidad uniforme entre 1,1 y 1,5 m/s, con generador propio.
- **¿E3 está medido?** No: es el extremo rápido del rango técnico (TCQSM). Se lee como "qué pasaría si".

## Resultados (completar con la producción)

| | E0 | E1 | E3 | E13 |
|---|---:|---:|---:|---:|
| P90 de espera (s) | | | | |
| Proporción > 30 s | | | | |
| P90 cohorte pico (s) | | | | |

Diferencias contra E0 con IC de Bonferroni: ver `informe/generado/tabla-diferencias.tex` y
`figs/tpi-subte-res-forest.png`.

## Antes de entrar

1. `python3 verificar_modelo.py`: los 5 OK.
2. Abrir el modelo y responder **No** al autosave; dejar `MainPeatonal` en la vista de los 4 bloques.
3. Tener a mano el informe compilado, la planilla (`Resumen`) y las capturas del mapa de calor.
