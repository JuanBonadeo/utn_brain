# Soporte a la Gestión de Datos con P. Visual — Wiki

## Índice
_(vacío — se completa cuando se ingiera el programa de la materia)_

## Desarrollo
_(sin unidades cargadas todavía)_

## Entregables
- **Presentación: Serverless** → `entregables/serverless/informe-investigacion.md`
  Informe de investigación con fuentes (CNCF, AWS, Berkeley, Datadog, OWASP,
  Cloudflare). Base para armar el deck de la exposición a la clase.
- **Deck: Serverless** → `entregables/serverless/presentacion-serverless.pptx`
  14 láminas, 15 min, 4 expositores. Guion con notas por lámina y preguntas
  probables en `guion-presentacion.md` (+ `.docx`). Generador en
  `scripts/sgd/pptx-serverless/`.
- **Informe: Serverless** → `entregables/serverless/informe-serverless.md` (+ `.pdf`)
  Versión para entregar del informe de investigación: 12 págs., carátula,
  sin las notas internas. Profes: Torres y Castagnino.
- **Cuestionario: Serverless** → `entregables/serverless/cuestionario.md`
  10 preguntas (8 opción múltiple, 2 V/F) para la clase, con clave. El Google
  Form se genera con `cuestionario-form.gs` (Apps Script).
- **Proyecto: Spine-Guard** → `entregables/Spine-Guard/` (submódulo git,
  repo propio en github.com/JuanBonadeo/Spine-Guard). Monitor de postura con
  webcam (OpenCV + MediaPipe).
- **TPI: UTNHub** (Grupo 7) → `entregables/utnhub/informe-utnhub.md` (+ `.pdf`)
  Documentación final del TPI: se imprime por duplicado y se deja en el 5° piso.
  Asistente para alumnos de la FRRO: chatbot agéntico (LangGraph + Gemini + RAG
  en pgvector), ingesta de novedades con IA en AWS Lambda, núcleo académico
  (correlatividades, promedio, horarios, calendario .ics). Repo:
  github.com/augustobrizio/UTNHub (clon local en `D:/Utn/4° Año/Soporte/TPI-Soporte`),
  app en utnhub.up.railway.app. PDF: `node scripts/sgd/utnhub-informe/build.js`;
  capturas en `figs/utnhub-*.jpg`.

## Log
- Archivo creado.
- 2026-09-08: investigación sobre serverless para la presentación de la materia.
  Se creó `entregables/serverless/informe-investigacion.md` (16 secciones +
  glosario). No se tocaron unidades: la materia todavía no tiene programa
  ingerido.
- 2026-10-06: deck de la presentación de serverless (14 láminas en 4 bloques,
  uno por expositor) y guion hablado de ~12:45 con notas del orador y anexo de
  preguntas probables.
- 2026-10-09: cuestionario de 10 preguntas sobre la presentación de serverless
  + script de Apps Script que arma el Google Form en modo cuestionario.
- 2026-10-09: informe de serverless para entregar (pdf con carátula), armado
  desde el informe de investigación y alineado con el deck (punto de cruce 34 %).
- 2026-11-03: se documenta el submódulo Spine-Guard en Entregables; se borran
  las opciones A/B/C descartadas del deck de serverless y sus generadores.
- 2026-11-03: el generador del deck pasó a `scripts/sgd/pptx-serverless/`.
- 2026-11-16: informe final del TPI UTNHub (24 págs., con el estilo del informe de
  referencia: Aptos, títulos en azul, carátula de la UTN), armado desde el repo y la
  app en producción, con diagramas de arquitectura, dominio, agente y pipeline.
