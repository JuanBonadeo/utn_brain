#!/usr/bin/env python3
"""Actualiza parámetros de CaserHorno.alp con las respuestas del encargado (2026-10-07). IDE cerrado.

Uso: .venv/Scripts/python.exe -I .../actualizar_parametros_0710.py [archivo.alp]   (por defecto CaserHorno.alp)

- umbralULI 75 -> 79: promedio de la cola al encender de las campañas largas, sin las ULI "sin apuro"
  (espera > 30 días) ni los días sueltos de 1-2 ULI (error de planilla). Coincide con el 70-80 relevado.
- horasEnVacio sigue en 48: primero dijo "se apaga enseguida", pero repreguntado aclaró que si sabe que entra
  más se mantiene prendido; el registro muestra huecos de hasta 2 días dentro de campañas. E3 = apagar enseguida (0 h).
- soloUrgentesEnPrioridad true -> false: los encendidos cortos reales tratan toda la cola (~27 ULI); la regla
  de "solo urgentes" salía de los registros erróneos de 1-2 ULI.
- pPrioridad 0,0095 -> 0,0054: 10 encendidos cortos reales / 1.857 ULI llegadas con el horno apagado.
- kWhPorEncendido 1384 -> 2303 y kWhPorDiaCaliente 2445 -> 2402: regresión rehecha sin los días erróneos
  (R2 0,90; horno_regresion3.py).
- Escenarios: E3 pasa a ser "apagar enseguida" (0 h), la alternativa a la práctica actual.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

ALP = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "CaserHorno.alp"
s = ALP.read_text(encoding="utf-8")

NUEVOS = {
    "umbralULI": ("75", "79", "ULI en cola que disparan el encendido. 79 = promedio de la cola al encender de las campañas largas 2024-2026, sin ULI retenidas por falta de demanda ni registros erróneos (encargado: 70-80)."),
    "horasEnVacio": ("48", "48", "Horas que el horno sigue caliente con la cola vacía. 48: el encargado lo mantiene prendido si sabe que entra más (07/10/2026); el registro tiene huecos de hasta 2 días dentro de campañas. E3 prueba apagar enseguida (0 h)."),
    "soloUrgentesEnPrioridad": ("true", "false", "Si es true, un encendido por prioridad trata solo las urgentes. False (base): los encendidos cortos reales tratan toda la cola."),
    "pPrioridad": ("0.0095", "0.0054", "Probabilidad de que una ULI sea urgente y adelante el encendido: 10 encendidos cortos reales / 1.857 ULI llegadas con el horno apagado (2024-2026, sin registros erróneos)."),
    "kWhPorEncendido": ("1384", "2303", "kWh fijos por encendido (regresión sin registros erróneos: 2.303 ± 1.386; sensibilidad 0-5.220)."),
    "kWhPorDiaCaliente": ("2445", "2402", "kWh por día con el horno a temperatura (regresión sin registros erróneos: 2.402 ± 160, ≈100 kW)."),
}
for nombre, (viejo, nuevo, desc) in NUEVOS.items():
    pat = (rf'(<Variable Class="Parameter"><Id>\d+</Id><Name>{nombre}</Name>.*?<DefaultValue Class="CodeValue"><Code>){re.escape(viejo)}'
           rf'(</Code></DefaultValue>.*?<Description>)[^<]*(</Description>)')
    s, n = re.subn(pat, rf"\g<1>{nuevo}\g<2>{escape(desc)}\g<3>", s, count=1, flags=re.S)
    assert n == 1, nombre

# Escenarios del experimento CorridasE0E3
for viejo, nuevo in (("index / 30 == 1 ? 45 : 75", "index / 30 == 1 ? 45 : 79"),
                     ("index / 30 == 3 ? 96 : 48", "index / 30 == 3 ? 0 : 48")):
    assert s.count(escape(viejo)) == 1, viejo
    s = s.replace(escape(viejo), escape(nuevo))

ET.fromstring(s.encode("utf-8"))
ALP.write_text(s, encoding="utf-8", newline="\n")
print("Parámetros actualizados en", ALP)
