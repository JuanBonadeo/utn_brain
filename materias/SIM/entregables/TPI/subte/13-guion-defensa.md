---
title: "Guion de la defensa (3 min) - TPI Subte Constitución"
subject: "Simulación"
status: "Diapositivas: TPI_Subte_Defensa.pptx (scripts/sim/subte-defensa-pptx.js). Faltan los corchetes, que salen de la producción"
---

# Defensa: máximo 3 minutos, con el modelo en funcionamiento

Objetivo: **2 min 50 s**. El bloque de AnyLogic tiene 50 s reservados. Las notas de cada diapositiva de
`TPI_Subte_Defensa.pptx` son estas secciones. Medir con
`.venv/bin/python scripts/guion-timing.py materias/SIM/entregables/TPI/subte/13-guion-defensa.md`.

## 0:00 · Juan · Diapositiva 1: el problema

Analizamos el ingreso a la Línea C en Constitución, de 7 a 9:30 de un día hábil: la estación más cargada del subte. La pregunta es si conviene habilitar más molinetes, validar más rápido o las dos cosas.

## 0:17 · Matías · Diapositiva 2: por qué simular

Con promedios no hay problema: a las 8:15 cada molinete está ocupado un tercio del tiempo y una fórmula de colas da casi cero espera. Pero el Roca trae 47 trenes y la gente llega en oleadas. La cola es transitoria, y eso se simula.

## 0:37 · Juan · Diapositiva 3: el modelo

Cada réplica es un día hábil real: las validaciones de SBASE y la llegada real de cada tren. Cada pasajero baja del tren, camina el andén y el hall, baja por las escaleras mecánicas, elige un molinete y valida.

## 0:55 · Matías · Diapositiva 4: escenarios y medidas

Comparamos la situación actual, E0, con 20 molinetes, contra 22 molinetes, validación sin contacto, y las dos juntas. Medimos el percentil 90 de la espera, porque el promedio esconde la oleada.

## 1:12 · Juan · Diapositiva 5: el modelo en funcionamiento (50 s)

> Cambiar a AnyLogic: `PeatonalFranjaVisualE0` lanzado ~90 s antes, a 30x, ya cerca del pico. Mostrar en este
> orden y hablar sobre la animación. Si algo falla, volver a la diapositiva: tiene la captura de respaldo.

Este es el modelo en AnyLogic. Arriba, en tres bloques, las variables, las medidas y la lógica; abajo, la simulación. Acá llega un tren del Roca: la gente baja por las puertas, cruza el hall y baja por las dos escaleras mecánicas. En el subsuelo camina el pasillo hasta los molinetes, donde se forma la oleada. El panel muestra en vivo la hora, la cola y el percentil 90, y el mapa de calor marca en rojo dónde se acumula la gente.

## 2:02 · Matías · Diapositiva 6: resultados

Corrimos [N] días por escenario, con los mismos días y los mismos pasajeros en los cuatro. Con intervalos apareados y Bonferroni, el percentil 90 pasó de [E0] segundos a [E1] con 22 molinetes, [E3] validando más rápido y [E13] con las dos. [FRASE SOBRE LOS INTERVALOS].

## 2:30 · Juan · Diapositiva 7: conclusión y alcance

[CONCLUSIÓN]. Vale dentro de los supuestos: no medimos la espera real, la proporción que viene del Roca es un supuesto y el subsuelo no tiene plano oficial. Gracias.

## Reloj: antes de empezar

- AnyLogic abierto, `PeatonalFranjaVisualE0` lanzado ~90 s antes de arrancar, a 30x, con la vista del bloque 4.
- Presentación en la diapositiva 1; alternar con Cmd+Tab (o Alt+Tab) en la diapositiva 5.
- Si la máquina no sostiene 30x con el 3D, mostrar solo la vista 2D.
