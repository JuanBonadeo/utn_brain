---
title: "Guion de exposición - TPI Subte Constitución"
subject: "Simulación"
status: "Actualizado al modelo del 2026-11-09; faltan los campos entre corchetes, que salen de la producción"
---

# Guion del video - máximo 3 minutos

## Reloj: condiciones de grabación

- Duración objetivo: **2 min 40 s**. Deja 20 s de margen respecto del límite estricto.
- Toma única, sin edición. Juan Cruz Bonadeo y Matías Estevez aparecen en cámara.
- Diapositivas en Google Slides y un solo cambio a AnyLogic, en el bloque 5.
- Los campos entre corchetes se completan solo con `corridas_peatonales.csv` (`analisis_corridas.py` y `04-resultados-corridas.xlsx`). Nunca con el piloto del 04/11 ni con las corridas descartadas.
- `[N]` es la cantidad de días que queda después de calcular n*. Mínimo 10.
- Medir el texto con `scripts/guion-timing.py` después de completar los corchetes.

## 0:00 · Juan · Diapositiva 1: el problema

> Foto o plano de Constitución y la pregunta del estudio.

Analizamos el ingreso a la Línea C en Constitución, entre las 7 y las 9:30 de un día hábil. Es la estación más cargada del subte: tiene las 14 ventanas de 15 minutos con más pasajeros de toda la red. La pregunta es concreta: ¿conviene habilitar más molinetes, validar más rápido, o las dos cosas?

## 0:23 · Matías · Diapositiva 2: por qué simular

> Gráfico de ingresos por ventana con los arribos de trenes marcados.

Con promedios, el problema no existe: a las 8:15 entran 2.214 personas en 15 minutos y cada molinete está ocupado un 32 % del tiempo. Un modelo M/M/c dice que no hay cola. Pero la cola se ve todos los días, porque la gente llega en oleadas: en la franja el Roca tiene 47 trenes. Por eso simulamos.

## 0:47 · Juan · Diapositiva 3: el modelo

> Diagrama del recorrido: tren, andén, hall, escalera, pasillo, cola, molinete.

Usamos los datos de molinetes de SBASE y los arribos reales del Roca. Cada réplica es un día hábil real, sorteado entre 75. Cada pasajero baja del tren, camina hasta el vestíbulo, elige una cola y valida. Es un sistema terminal: la réplica sigue hasta que sale el último que entró antes de las 9:30.

## 1:09 · Matías · Diapositiva 4: escenarios y medidas

> Tabla de 4 escenarios (molinetes y validación) y las 3 medidas primarias.

Comparamos cuatro escenarios: E0, la situación actual, con 20 molinetes; E1, con los 22 del vestíbulo; E3, con 20 y validación sin contacto más rápida; y E13, las dos medidas juntas. Medimos el percentil 90 de la espera, la proporción que espera más de 30 segundos y el percentil 90 en el pico.

## 1:31 · Juan · AnyLogic en ejecución

> `PeatonalFranjaVisualE0` a 30x, ya en el pico (ver "Material"). Vista 2D del bloque 4 y salto a la ventana 3D.

Este es el modelo en AnyLogic, con la Pedestrian Library. Arriba están las variables, las medidas y la lógica; abajo, la simulación. Acá llega un tren del Roca y la oleada camina hacia los molinetes. El panel muestra en vivo la espera y la cola, y el mapa de calor marca dónde se concentra la gente.

## 1:54 · Matías · Diapositiva 5: resultados

> Tabla de diferencias contra E0 con intervalos de Bonferroni, sin columnas auxiliares.

Corrimos [N] días por escenario con números aleatorios comunes: los cuatro reciben el mismo día y los mismos trenes. Comparamos contra E0 con intervalos t apareados y Bonferroni, con 95 % de confianza conjunta. El percentil 90 pasó de [E0] segundos a [E1] con E1, [E3] con E3 y [E13] con E13. [FRASE SOBRE LOS INTERVALOS].

## 2:19 · Juan · Diapositiva 6: conclusión y alcance

> Recomendación arriba, limitaciones abajo.

[CONCLUSIÓN ESTADÍSTICA]. Vale para estos supuestos: el vestíbulo no tiene plano oficial, la proporción de pasajeros que viene del Roca es un supuesto, la validación sale de la literatura y no medimos la espera real. Gracias.

## Reloj: regla para completar la conclusión

Fijada antes de correr (informe, paso 7):

- Intervalo de una primaria entero por debajo de cero: esa alternativa mejora esa medida con evidencia estadística. Se dice el intervalo, no solo la media.
- Intervalo que contiene al cero: `con [N] días no hay evidencia de diferencia`. Si además el semiancho es ≤ 1 s (percentiles) o ≤ 0,01 (proporción), la diferencia es despreciable en la práctica.
- Las primarias no coinciden: describir el compromiso, sin declarar una mejora global.
- Entre las alternativas que mejoran, recomendar la de menor P90 solo si el intervalo frente a las otras también lo sostiene.

## Reloj: material antes de grabar

- Las seis diapositivas en Google Slides con los resultados cargados.
- AnyLogic abierto con `PeatonalFranjaVisualE0`, las 10 figuras en `3d/` y la velocidad en 30x.
- Lanzar la simulación **unos 90 s antes de grabar**: las 08:30 llegan a los 180 s a 30x y el bloque 5 arranca en 1:31. Medir en el ensayo si la máquina sostiene 30x con el 3D.
- Cronómetro visible para quien coordina la toma.
- YouTube: visibilidad `Oculto` y contenido no creado para niños.
- Probar el enlace desde una sesión sin permisos y entregarlo en el Classroom.

## Reloj: ensayo

- Hacer al menos dos ensayos completos sin cortar.
- Si supera 2 min 50 s, recortar palabras: no acelerar la lectura ni omitir la conclusión.
- En AnyLogic debe verse movimiento real y el escenario. Los números se leen de la planilla, no de la animación.
