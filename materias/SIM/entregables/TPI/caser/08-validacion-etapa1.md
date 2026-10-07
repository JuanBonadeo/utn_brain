# TPI Caser — validación de la Etapa 1 (primera pasada, 2026-10-07)

> E0 (30 réplicas de `CorridasE0E3`, AnyLogic) contra el registro del **mismo período** que las entradas: ULI
> lavadas del 15/08/2025 al 14/08/2026, campañas que empiezan en ese lapso (15) y facturas del medidor
> exclusivo del horno (sep/2025-abr/2026). Script: `modelo/validar_etapa1.py`, que lee `datos-locales/` y
> solo imprime agregados. Criterios de `05-` §4.1.

## Resultado

| Métrica | Registro | Modelo | Error | Tolerancia | Welch 95 % contiene 0 | Veredicto |
|---|---:|---:|---:|---:|---|---|
| Toneladas tratadas por mes | 21,7 | 21,1 | −2,9 % | 10 % | (un valor) | **OK** |
| Duración de campaña (días) | 7,47 | 7,28 | −2,5 % | 10 % | sí | **OK** |
| ULI por campaña | 84,1 | 101 | +19,9 % | 10 % | sí (n = 15, muy disperso) | fuera de tolerancia |
| Campañas por mes | 1,28 | 1,50 | +17,7 % | 10 % | (un valor) | fuera |
| Espera antes del horno, media (días) | 8,95 | 7,25 | −18,9 % | 15 % | no | fuera |
| kWh del horno por mes | 38.000 | 31.800 | −16,3 % | 15 % | sí | fuera, por poco |
| Espera p90 (días) | 23 | 15,1 | −34 % | — | — | informativa |
| Cola al encender (ULI) | 73,7 | 65 | −12 % | — | sí | informativa |
| Fracción de encendidos chicos | 0,53 | 0,36 | — | — | — | calibrada: no valida |

**Lectura.** El modelo mueve la cantidad correcta de material (t/mes) con campañas de la duración correcta,
pero **enciende demasiado seguido** y por eso la espera le da corta. No es un problema de una métrica suelta:
las tres que fallan son consistentes entre sí (más campañas → menos espera → más kWh por kg).

## Causa más probable: el umbral real es más alto que 75

- Las campañas largas del registro arrancan con una cola **mediana de 98-99 ULI** (2024-2026: 98,5; rango
  intercuartil 73-123). El conteo del registro incluye las ULI lavadas durante las 36 h de calentamiento
  (unas 10), así que el umbral efectivo rondaría las **85-90 ULI**, no 75.
- El 70-80 fue lo que dijo el encargado; el registro dice algo más alto y más variable. No se cambia el
  umbral para que coincida (calibrar no es validar): **se le pregunta al encargado** y, si confirma que
  esperan más, el umbral pasa a ser el relevado nuevo y se vuelve a validar.

## Otras diferencias a revisar

- **Cola larga de la espera.** El registro tiene un 4,6 % de ULI que esperan más de 30 días (máximo 118).
  El modelo no genera esas esperas: o son ULI retenidas por otros motivos (calidad, falta de material para
  completar la orden, prioridad baja), o errores de fecha. Pregunta al encargado.
- **Encendidos chicos.** En la ventana son 8 de 15 (53 %), contra el 44 % de 2024-2026 con el que se estimó
  `pPrioridad`. Cinco de esos ocho trataron 1 o 2 ULI. Si son errores de carga en la planilla, `pPrioridad`
  baja y cambia la cantidad de campañas.
- **kWh.** Las facturas cubren sep/2025-abr/2026, meses de más actividad que may-ago/2026, mientras que el
  modelo promedia los 12 meses. Parte del −16 % viene de ahí; se puede comparar kWh por tonelada en vez de
  kWh por mes cuando cierre lo anterior.

## Próximo paso

Con las respuestas del encargado: fijar el umbral relevado, corregir `pPrioridad` si los encendidos de
1-2 ULI no son reales, volver a correr `CorridasE0E3` y repetir esta validación. Hasta entonces, los
resultados del test de medias (07- §5) muestran la dirección de los efectos, pero no su tamaño.
