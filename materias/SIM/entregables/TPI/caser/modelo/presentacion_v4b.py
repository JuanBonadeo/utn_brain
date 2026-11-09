#!/usr/bin/env python3
"""Ajustes a la presentación v4 (2026-11-08, IDE cerrado), a partir de las capturas de la primera corrida.

- Números con coma decimal (Locale es-AR) en todos los textos de la presentación.
- Energía por kg: "–" hasta que haya 5 t tratadas (con pocos kilos el cociente no significa nada).
- Bloques de la PML más separados: los contadores de entrada y salida se pisaban.
- La línea de abajo del selector repetía el encabezado: ahora muestra el resultado del estudio.
Solo presentación: el CSV de CorridasE0E3 no cambia (lo controla el verificador).
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

ALP = Path(__file__).resolve().parent / "CaserHorno.alp"
s = ALP.read_text(encoding="utf-8")
if "presentacion v4b" in s:
    sys.exit("Los ajustes v4b ya están aplicados.")
LOC = 'new java.util.Locale("es", "AR"), '


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:120], s.count(a))
    s = s.replace(a, b)


# Presentación de Main: coma decimal en todos los String.format de los textos.
i0 = s.index("<Name>Main</Name>")
lvl = s.index("<Presentation>", s.index("<Level>", s.index("<Presentation>", i0)))
fin = s.index("</Presentation>", lvl)
bloque = s[lvl:fin]
bloque = bloque.replace('String.format("', "String.format(" + LOC + '"')
s = s[:lvl] + bloque + s[fin:]

# Energía por kg
viejo = ('String.format(' + LOC + '"%.2f kWh/kg", (kWhPorEncendido * visEncendidos + kWhPorDiaCaliente / 24 * visHorasCaliente()) '
         '/ Math.max(1, visKg))')
rep(escape(viejo), escape('visKg < 5000 ? "–" : ' + viejo.replace("Math.max(1, visKg)", "visKg")))

# (La posición de los bloques de la PML la fija presentacion_v4.py, en escalera.)

ET.fromstring(s.encode("utf-8"))
ALP.write_text(s, encoding="utf-8", newline="\n")
print("Ajustes v4b aplicados a", ALP.name)
