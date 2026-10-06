# Presentación de SGD: Serverless

Genera `materias/SGD/entregables/serverless/presentacion-serverless.pptx`: 14 láminas
para 15 minutos y 4 expositores. El contenido sale del informe
(`informe-investigacion.md`) y está transcripto en `build.js`. Las notas del orador
se leen de `guion-presentacion.md`: cada bloque `## Lámina N` es la nota de la lámina N.

```
node scripts/pptx-sgd-serverless/build.js
node scripts/build-docx.js materias/SGD/entregables/serverless/guion-presentacion.md \
     materias/SGD/entregables/serverless/guion-presentacion.docx --title
.venv/bin/python scripts/guion-timing.py materias/SGD/entregables/serverless/guion-presentacion.md
```

Si se edita el guion, hay que regenerar el pptx para que se actualicen las notas, y
también el docx.
