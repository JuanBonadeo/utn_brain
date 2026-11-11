#!/bin/sh
# Arma informe-overleaf.zip para subir a Overleaf (decisión D6). La fuente de verdad sigue siendo el repo:
# lo que se edite en Overleaf se baja y se vuelve a commitear acá.
# Copia al zip solo las figuras del TPI subte (materias/SIM/figs/tpi-subte-*).
set -eu
cd "$(dirname "$0")"
tmp=$(mktemp -d)
mkdir -p "$tmp/informe/figs"
cp -R tpi-subte.tex referencias.bib capitulos "$tmp/informe/"
[ -d generado ] && cp -R generado "$tmp/informe/"
for f in ../../../../figs/tpi-subte-*; do [ -e "$f" ] && cp "$f" "$tmp/informe/figs/"; done
# Los PNG de matplotlib traen canal alfa opaco: pdfLaTeX procesa una máscara por imagen y la compilación
# supera el límite de tiempo del plan gratis de Overleaf. Se quita el alfa (sin pérdida) si hay Pillow.
PY=../../../../../../.venv/bin/python; [ -x "$PY" ] || PY=python3
"$PY" - "$tmp/informe/figs" <<'PYEOF' || echo "aviso: no se pudo quitar el alfa de las figuras (falta Pillow)"
import sys, glob
from PIL import Image
for f in glob.glob(sys.argv[1] + '/*.png'):
    im = Image.open(f)
    if im.mode in ('RGBA', 'LA', 'P'):
        im.convert('RGB').save(f, optimize=True)
PYEOF
rm -f informe-overleaf.zip
(cd "$tmp/informe" && zip -qr "$OLDPWD/informe-overleaf.zip" .)
rm -rf "$tmp"
echo "listo: $(pwd)/informe-overleaf.zip — en Overleaf: New Project > Upload Project; Menu > Compiler: pdfLaTeX"
