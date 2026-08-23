#!/bin/bash
# docx -> pdf -> png por página, para poder mirar cómo queda el render.
# Uso: scripts/preview-docx.sh <archivo.docx> [directorio-salida]
set -e
IN="$1"
OUT="${2:-/tmp/preview}"
SOFFICE="/Applications/LibreOffice.app/Contents/MacOS/soffice"
[ -x "$SOFFICE" ] || { echo "Falta LibreOffice en $SOFFICE"; exit 1; }
mkdir -p "$OUT"
"$SOFFICE" --headless --convert-to pdf --outdir "$OUT" "$IN" >/dev/null 2>&1
PDF="$OUT/$(basename "${IN%.*}").pdf"
[ -f "$PDF" ] || { echo "No se generó el PDF"; exit 1; }
"$(dirname "$0")/../.venv/bin/python" - "$PDF" "$OUT" <<'PY'
import sys, pymupdf
pdf, out = sys.argv[1], sys.argv[2]
d = pymupdf.open(pdf)
print(f"{d.page_count} páginas")
for i, page in enumerate(d, 1):
    page.get_pixmap(dpi=110).save(f"{out}/p{i:02d}.png")
    print(f"  {out}/p{i:02d}.png")
PY
