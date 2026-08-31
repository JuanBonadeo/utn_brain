# -*- coding: utf-8 -*-
"""Mide cuanto dura hablado un guion de exposicion.

Cuenta solo el texto que se dice: saltea titulos, citas, tablas y listas. El
ritmo por defecto son 145 palabras por minuto, que es una lectura academica
clara en castellano; se puede cambiar con el segundo argumento.

    .venv/bin/python scripts/guion-timing.py materias/ASI/entregables/etapa3-guion.md
"""
import re
import sys

RUTA = sys.argv[1]
WPM = float(sys.argv[2]) if len(sys.argv) > 2 else 145.0
OMITIR = ("Reloj", "Preguntas")


def hablado(bloque):
    return " ".join(l for l in bloque.split("\n")[1:]
                    if l.strip() and not l.startswith(("#", ">", "|", "-", "*")))


total = 0.0
print("%-44s %9s %8s" % ("BLOQUE", "PALABRAS", "DURACION"))
print("-" * 63)
for b in re.split(r"^## ", open(RUTA, encoding="utf-8").read(), flags=re.M)[1:]:
    nombre = b.split("\n")[0].strip()
    if nombre.startswith(OMITIR):
        continue
    n = len(hablado(b).split())
    seg = n / WPM * 60
    total += seg
    print("%-44s %9d %5d:%02d" % (nombre[:44], n, seg // 60, seg % 60))
print("-" * 63)
print("%-44s %9s %5d:%02d" % ("TOTAL", "", total // 60, total % 60))
