---
title: "Guion de exposición - TPI Subte Constitución"
subject: "Simulación"
status: "Borrador condicionado a resultados calibrados"
---

# Guion de exposición - máximo 3 minutos

Presentación editable asociada: [`TPI_Subte_Presentacion.pptx`](TPI_Subte_Presentacion.pptx). Sus seis
diapositivas siguen la secuencia de este guion y mantienen marcadores visibles donde faltan resultados.

## Condiciones de grabación

- Duración objetivo: **2 min 45 s**. Deja 15 s de margen respecto del límite estricto.
- Toma única, sin edición.
- Juan Cruz Bonadeo y Matías Estevez aparecen en cámara.
- Compartir Google Slides y alternar una sola vez a AnyLogic para mostrar el modelo en ejecución.
- Reemplazar los campos `[RESULTADO]` únicamente con las 30 réplicas calibradas de E0 y E1.
- No mostrar como evidencia cuantitativa los valores de `PeatonalDemo` ni corridas con `modoDemo`.

## Secuencia cronometrada

| Tiempo | Orador | Apoyo visual | Texto guía |
|---|---|---|---|
| 0:00-0:20 | Juan | Diapositiva 1: problema | Nuestro trabajo analiza el acceso desde el ferrocarril Roca a la Línea C en Constitución durante 07:00-09:30. El problema no es solamente el volumen promedio: los trenes generan oleadas que pueden formar colas aunque la capacidad media parezca suficiente. |
| 0:20-0:42 | Matías | Diapositiva 2: evidencia | Usamos los viajes por molinete de SBASE de enero a junio de 2026. Constitución contiene las 14 ventanas de 15 minutos más cargadas de la red. En el pico de las 08:30 observamos 2.066 pasajeros y una variabilidad diaria relevante. |
| 0:42-1:02 | Juan | Diapositiva 3: modelo conceptual | Modelamos un sistema terminal: llegan tandas, los pasajeros eligen una cola, validan el viaje en un molinete y salen hacia la Línea C. La réplica termina después de las 09:30 cuando se drena la cohorte, para no censurar esperas. |
| 1:02-1:25 | Matías | Diapositiva 4: escenarios | E0 representa la operación base con 20 posiciones habilitadas y E1 habilita las 28 instaladas. Ambos escenarios usan las mismas entradas y semillas. E2 y E3 quedan como extensiones: desvío a Plaza y validación contactless. |
| 1:25-1:48 | Juan | AnyLogic en ejecución | Implementamos el flujo con la Pedestrian Library: PedSource, PedService, salida física y PedSink. Medimos espera media, percentil 90, proporción sobre 30 segundos, cola, disipación, throughput y utilización por molinete. Esta geometría sigue siendo provisoria hasta recibir el plano oficial. |
| 1:48-2:18 | Matías | Diapositiva 5: resultados | Ejecutamos 30 pares con números aleatorios comunes. En el indicador principal, el P90 pasó de `[E0]` a `[E1]` segundos. La diferencia media E1 menos E0 fue `[DIF]`, con intervalo de confianza `[IC_INF; IC_SUP]`. El throughput con drenaje `[SE MANTUVO / CAMBIÓ]` y la proporción sobre 30 segundos `[RESULTADO]`. |
| 2:18-2:42 | Juan | Diapositiva 6: conclusión | `[CONCLUSIÓN ESTADÍSTICA]`. Esta recomendación vale para los supuestos y datos calibrados del vestíbulo Principal. La espera real y la geometría todavía requieren validación con información de SBASE, Emova o una observación de campo. |
| 2:42-2:45 | Ambos | Diapositiva final | Gracias. |

## Regla para completar la conclusión

- Si el intervalo del P90 queda completamente por debajo de cero, el throughput no empeora y las medidas
  de cola son consistentes: `Recomendamos E1 para el escenario estudiado porque reduce el P90 con evidencia
  estadística y sin degradar el throughput.`
- Si el intervalo contiene cero: `Con las réplicas realizadas no encontramos evidencia suficiente para
  afirmar que E1 mejora el P90. No forzamos una recomendación y proponemos ampliar las réplicas o revisar
  los supuestos críticos.`
- Si E1 reduce espera pero degrada throughput u otra restricción principal: describir el compromiso y no
  presentar E1 como mejora global.

## Material que debe estar listo antes de grabar

- Captura limpia de `PeatonalE0` y `PeatonalE1` ejecutándose con parámetros calibrados.
- Tabla breve tomada de `04-resultados-corridas.xlsx`, sin columnas auxiliares.
- Intervalo de confianza del P90 y control de throughput con drenaje.
- Una diapositiva final con alcance, limitaciones y recomendación.
- Cronómetro visible para quien coordine la toma.
- Configuración de YouTube: visibilidad `Oculto` y contenido no creado para niños.

## Ensayo

Hacer al menos dos ensayos completos sin cortar. Si supera 2 min 50 s, recortar palabras antes de grabar;
no acelerar la lectura ni omitir la conclusión. Durante el tramo de AnyLogic debe verse movimiento real y
el nombre del escenario, pero los resultados se leen desde la planilla de corridas.
