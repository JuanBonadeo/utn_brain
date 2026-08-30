# -*- coding: utf-8 -*-
"""Renderiza cada figura del anexo como HTML standalone, para pasar a PNG con Chrome."""
import os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "anexo-graficos"))
import fig1, fig2, fig3, fig4, build
from acentos import acentuar

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, "materias", "ASI", "figs", "presentacion")
os.makedirs(OUT, exist_ok=True)

TPL = """<!doctype html><html><head><meta charset="utf-8">
<style>
%s
html,body{margin:0;padding:0;background:#FFFFFF;width:%dpx;height:%dpx;}
svg{width:%dpx;height:%dpx;display:block;}
</style></head><body>
<svg viewBox="0 0 %d %d" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">%s%s</svg>
</body></html>"""

FIGS = [
    ("fig1-red",    fig1.svg() + fig1.leyenda(),                              1750, 1064),
    ("fig2a-gantt", fig2.svg_gantt(),                                          1750, 1270),
    ("fig2b-histo", fig2.svg_histo(),                                          1750, 1220),
    ("fig3-plano",  fig3.svg() + '<g transform="translate(0,1040)">' + fig3.referencias() + '</g>', 1460, 1200),
    ("fig4-campo",  fig4.svg(),                                                1750, 1180),
]

ESCALA = 1.6
for nombre, cuerpo, w, h in FIGS:
    pw, ph = int(w * ESCALA), int(h * ESCALA)
    html = TPL % (build.CSS, pw, ph, pw, ph, w, h, build.DEFS, cuerpo)
    html = acentuar(html)
    ruta = os.path.join(OUT, nombre + ".html")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)
    print("%s %dx%d" % (ruta, pw, ph))
