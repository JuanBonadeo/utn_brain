#!/Users/juanbonadeo/Desktop/UTN/.venv/bin/python
"""
Wrapper de markitdown para convertir fuentes no-markdown (PDF, PPTX, DOCX,
imágenes, audio, etc.) a texto markdown.

Requiere markitdown, instalado en el virtualenv del proyecto (.venv).
El python del sistema (3.9) no sirve: markitdown necesita Python >= 3.10.
Si hay que recrear el entorno:
    /opt/homebrew/bin/python3.12 -m venv .venv
    ./.venv/bin/python -m pip install 'markitdown[all]'

Uso:
    from ingest import ingest
    texto = ingest("materias/TPA/fuentes/apunte-unidad1.pdf")

Desde la terminal (usar el python del venv):
    .venv/bin/python scripts/ingest.py materias/TPA/fuentes/apunte-unidad1.pdf
    .venv/bin/python scripts/ingest.py materias/TPA/fuentes/apunte.pdf salida.md
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
    # En Windows stdout redirigido usa cp1252 y revienta con símbolos
    # matemáticos (≤, α, Σ, →) muy comunes en los apuntes.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

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
