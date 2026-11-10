# Presentación de la Etapa 4 de ASI (Cuadra)

Genera `materias/ASI/entregables/etapa4/etapa4-presentacion.pptx`: 13 láminas para la
defensa, unos 9 minutos entre cuatro expositores. Mismo criterio que la de la Etapa 3
(`scripts/asi/pptx-etapa3/`): Calibri, `LAYOUT_WIDE`, azul `15406B` de los entregables
del grupo, más un ámbar `E8A33D` de acento. El motivo visual es la "manzana" (cuadrado
redondeado) con el número de punto del entregable, y la grilla de manzanas con un pin
en la portada y el cierre.

```
node scripts/asi/pptx-etapa4/build.js
```

- El texto de las láminas **transcribe** `etapa4.md`: si cambia el documento, se
  actualiza `build.js` a mano.
- Las **notas del orador** se leen de `etapa4-guion.md` (una por `### Lámina N`), así
  que al editar el guion alcanza con regenerar el deck.
- El guion se mide con `.venv/bin/python scripts/guion-timing.py materias/ASI/entregables/etapa4/etapa4-guion.md`
  y se pasa a PDF con `node scripts/md-to-pdf.js materias/ASI/entregables/etapa4/etapa4-guion.md`.
- Validar con `validate.py` del skill de pptx (Python del venv) y mirar el render de
  LibreOffice antes de dar por buena una versión.
- Los rótulos de los gráficos nativos (separador de miles y decimal) los formatea
  PowerPoint según el idioma de la máquina: en castellano salen `10.240` y `54,2%`.
