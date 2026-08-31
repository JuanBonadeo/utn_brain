# Presentación de la Etapa 3 de ASI

Genera `materias/ASI/entregables/etapa3-presentacion.pptx`: 22 láminas para exponer
el TP Integrador en 15–20 minutos, repartidas entre los cuatro integrantes del grupo.

Todo el contenido sale de `materias/ASI/entregables/etapa3.md`. Si ese documento cambia,
hay que actualizar `build.js` a mano: no lo lee, lo transcribe.

## Cómo se regenera

Las cinco figuras del Anexo II son A3 apaisado, con relaciones de 1,22 a 1,65 a 1.
En una diapositiva 16:9 (1,78) entran limitadas por la altura y dejan hasta un 35%
del ancho en blanco: se ven chicas. Por eso **no se reutilizan las láminas A3**: se
recomponen en 16:9 nativo con `figs16x9.py`, que separa el dibujo de su chrome
—título, bajada, referencias—, lo escala para llenar el lienzo y vuelve a componer
el chrome como riel lateral, agrandando además los cuerpos tipográficos. No se saca
información: se reubica. El detalle está en el encabezado de ese archivo.

```
.venv/bin/python scripts/pptx-asi-etapa3/figs16x9.py
```

Escribe cinco `.svg` de 1920×1080 en `materias/ASI/figs/presentacion/`. Se pasan a PNG
de 3840×2160 con Chrome headless:

```
cd materias/ASI/figs/presentacion
for n in fig1-red fig2a-gantt fig2b-histo fig3-plano fig4-campo; do
  printf '<!doctype html><meta charset="utf-8"><style>html,body{margin:0;padding:0;background:#fff}svg{display:block;width:3840px;height:2160px}</style>' > "$n.html"
  cat "$n.svg" >> "$n.html"
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
    --hide-scrollbars --default-background-color=FFFFFFFF \
    --screenshot="$n.png" --window-size=3840,2160 "file://$PWD/$n.html"
done
```

`render-figs.py` es el rasterizador viejo, que sacaba las láminas A3 tal cual. Se
conserva para regenerar el anexo impreso, no para el deck.

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
- Las cinco láminas de figura van **a sangre**, de borde a borde: las imágenes son
  16:9 nativas, así que `figura()` las coloca en 0,0 a 13,333 × 7,5. No llevan
  título propio en la lámina porque la figura ya lo trae en su riel.
- El reparto de la exposición entre los cuatro integrantes está en las **notas del
  orador**, no impreso en la lámina.
