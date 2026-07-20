#!/usr/bin/env python3
"""
Wrapper de markitdown para convertir fuentes no-markdown (PDF, PPTX, DOCX,
imágenes, audio, etc.) a texto markdown.

Uso:
    from ingest import ingest
    texto = ingest("fuentes/TPA/apunte-unidad1.pdf")

Desde la terminal:
    python scripts/ingest.py fuentes/TPA/apunte-unidad1.pdf
    python scripts/ingest.py fuentes/TPA/apunte.pdf salida.md
"""

import sys
from pathlib import Path

from markitdown import MarkItDown


def ingest(path: str) -> str:
    """Convierte el archivo en `path` a markdown y devuelve el texto."""
    ruta = Path(path)
    if not ruta.exists():
        raise FileNotFoundError(f"No existe el archivo: {ruta}")
    resultado = MarkItDown().convert(str(ruta))
    return resultado.text_content


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python scripts/ingest.py <archivo> [salida.md]", file=sys.stderr)
        raise SystemExit(1)

    texto = ingest(sys.argv[1])

    if len(sys.argv) >= 3:
        Path(sys.argv[2]).write_text(texto, encoding="utf-8")
        print(f"Escrito: {sys.argv[2]}")
    else:
        print(texto)


if __name__ == "__main__":
    main()
