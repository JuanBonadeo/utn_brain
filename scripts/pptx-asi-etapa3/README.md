# Presentación de la Etapa 3 de ASI

Genera `materias/ASI/entregables/etapa3-presentacion.pptx`: 22 láminas para exponer
el TP Integrador en 15–20 minutos, repartidas entre los cuatro integrantes del grupo.

Todo el contenido sale de `materias/ASI/entregables/etapa3.md`. Si ese documento cambia,
hay que actualizar `build.js` a mano: no lo lee, lo transcribe.

## Cómo se regenera

Las cinco figuras del Anexo II se rasterizan primero desde los mismos scripts que
producen el anexo A3, así lámina y figura no se pueden desincronizar:

```
.venv/bin/python scripts/pptx-asi-etapa3/render-figs.py
```

Escribe cinco `.html` en `materias/ASI/figs/presentacion/`. Se pasan a PNG con Chrome
headless (los tamaños salen del propio script, escala 1,6×):

```
for f in fig1-red:2800,1702 fig2a-gantt:2800,2032 fig2b-histo:2800,1952 \
         fig3-plano:2336,1920 fig4-campo:2800,1888; do
  n="${f%%:*}"; s="${f##*:}"
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
    --hide-scrollbars --default-background-color=FFFFFFFF \
    --screenshot="materias/ASI/figs/presentacion/$n.png" --window-size="$s" \
    "file://$PWD/materias/ASI/figs/presentacion/$n.html"
done
```

Y después el deck:

```
node scripts/pptx-asi-etapa3/build.js
```

Acepta dos argumentos opcionales: ruta de salida del `.pptx` y carpeta de figuras.

## Verificación

`pptxgenjs` emite XML de gráficos que PowerPoint rechaza y el resto de las herramientas
acepta, así que **la validación no es opcional**. Necesita Python 3.10 o superior —
el `python3` del sistema es 3.9 y falla con `SyntaxError`; usar el venv del proyecto:

```
.venv/bin/python <skill-pptx>/scripts/office/validate.py materias/ASI/entregables/etapa3-presentacion.pptx
```

**Mirar el render, no el código.** Se convierte a PDF con LibreOffice y se rasteriza:

```
soffice --headless --convert-to pdf etapa3-presentacion.pptx
pdftoppm -jpeg -r 110 etapa3-presentacion.pdf slide
```

En la primera pasada se habían colado tres colisiones de texto —el sello "ADOPTADA"
encima del título de su tarjeta, la barra del costo total fuera de su tarjeta y el
total de beneficios desbordando la suya— y aire muerto de 1 a 2 pulgadas al pie de
casi todas las láminas. Nada de eso se ve leyendo el `.js`.

## Convenciones

- Lienzo `LAYOUT_WIDE`, 13,333 × 7,5 pulgadas. El contenido arranca en y = 1,66 cuando
  la lámina tiene bajada, en 1,32 cuando no, y **cierra alrededor de y = 7,0**.
- Márgenes laterales de 0,62.
- Paleta del entregable y del anexo gráfico: azul `15406B`, celeste `DCE9F7`,
  rojo `B23A2E` para camino crítico y advertencias, `5B7FA6` y `4C6480` de apoyo.
- Tipografía **Calibri**. No se usa Lexend —la fuente del `.docx`— porque no está
  instalada y el render de control la sustituye con métricas distintas, lo que
  invalida la revisión de desbordes.
- Motivo visual: insignia circular con el número de punto del entregable, en todas
  las láminas de contenido. Sin barras ni filetes decorativos.
- Las cinco láminas de figura van a sangre, sin título propio: la figura ya lo trae.
- El reparto de la exposición entre los cuatro integrantes está en las **notas del
  orador**, no impreso en la lámina.
