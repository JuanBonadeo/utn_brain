#!/bin/sh
# Arma informe-overleaf.zip para subir a Overleaf (decisión D6). La fuente de verdad sigue siendo el repo:
# lo que se edite en Overleaf se baja y se vuelve a commitear acá.
# Copia al zip solo las figuras del TPI subte (materias/SIM/figs/tpi-subte-*).
set -eu
cd "$(dirname "$0")"
tmp=$(mktemp -d)
mkdir -p "$tmp/informe/figs"
cp -R tpi-subte.tex referencias.bib capitulos "$tmp/informe/"
for f in ../../../../figs/tpi-subte-*; do [ -e "$f" ] && cp "$f" "$tmp/informe/figs/"; done
rm -f informe-overleaf.zip
(cd "$tmp/informe" && zip -qr "$OLDPWD/informe-overleaf.zip" .)
rm -rf "$tmp"
echo "listo: $(pwd)/informe-overleaf.zip — en Overleaf: New Project > Upload Project; Menu > Compiler: pdfLaTeX"
