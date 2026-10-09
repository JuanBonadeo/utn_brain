#!/usr/bin/env python3
"""Agrega el costo en pesos a CaserHorno.alp (2026-10-09, IDE cerrado).

Costo relevante de una regla de encendido (05- §3.4), en $ sobre el horizonte medido (365 días):
  luz     = kWhTotal × tarifaKWh                      (tarifa MARGINAL: el cargo fijo de potencia es hundido)
  gas     = kgGLPPorDiaCaliente / 24 × horas a temperatura × precioGLPkg
  capital = tasaCapitalMensual × kg promedio en cola × costoProductoKg × meses medidos
Valores (todos con impuestos, como las facturas):
- tarifaKWh 290 -> 102 $/kWh: pendiente de importe ~ kWh en las facturas del medidor del horno 03/2025-04/2026
  (fijo ~6,8 M$/mes + tendencia, R² 0,95). Los 290 eran el promedio con el cargo fijo adentro.
- kgGLPPorDiaCaliente 130: regresión trimestral facturas + estadística de compras 01/2024-08/2026 (R² 0,92).
- precioGLPkg 2250: 2.004 $/kg sin IVA (09/2026) + 12,25 % (IVA 10,5 % y percepción 1,75 %).
- costoProductoKg 4467: precio de lista × 0,335 por kg, ponderado por las ULI de los últimos 12 meses. Es el costo
  del producto terminado: sobrestima el valor del producto antes del horno (cota superior del costo de capital).
- tasaCapitalMensual 0,02: empresa.
Agrega columnas al final del CSV (glpKg, costoLuz, costoGLP, costoCapital, costoTotal) sin cambiar las existentes.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

ALP = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "CaserHorno.alp"
s = ALP.read_text(encoding="utf-8")
if "<Name>costoProductoKg</Name>" in s:
    sys.exit("Los costos ya están agregados.")
_id = [1830000000000]


def nid():
    _id[0] += 1
    return str(_id[0])


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:100], s.count(a))
    s = s.replace(a, b)


LABEL = "<Label><X>10</X><Y>0</Y></Label>"
FLAGS_OFF = "<PublicFlag>false</PublicFlag><PresentationFlag>false</PresentationFlag><ShowLabel>true</ShowLabel>"

# tarifa marginal
rep("<DefaultValue Class=\"CodeValue\"><Code>290</Code></DefaultValue>", "<DefaultValue Class=\"CodeValue\"><Code>102</Code></DefaultValue>")
s, n = re.subn(r"(<Name>tarifaKWh</Name>.*?<Description>)[^<]*(</Description>)",
               r"\g<1>" + escape("$/kWh marginal con impuestos: pendiente importe ~ kWh de las facturas del horno 03/2025-04/2026 (R² 0,95). El cargo fijo de potencia (~6,8 M$/mes) es hundido para esta decisión.") + r"\g<2>",
               s, count=1, flags=re.S)
assert n == 1

NUEVOS = [
    ("kgGLPPorDiaCaliente", "130", "kg de GLP (propano) por día de horno a temperatura: facturas YPF Gas + estadística de compras 01/2024-08/2026, regresión trimestral (± 12, R² 0,92). Sensibilidad 100."),
    ("precioGLPkg", "2250", "$/kg de GLP con impuestos: 2.004 sin IVA (09/2026) + IVA 10,5 % + percepción 1,75 %."),
    ("costoProductoKg", "4467", "$ por kg de producto: precio de lista × 0,335 por kg, ponderado por las ULI de los últimos 12 meses. Costo del producto terminado: cota superior del valor antes del horno."),
    ("tasaCapitalMensual", "0.02", "Costo del capital inmovilizado, por mes (empresa, 2026-10-07)."),
]
pids = {}
xml_params = ""
for k, (n_, v, d) in enumerate(NUEVOS):
    pids[n_] = nid()
    xml_params += (f'<Variable Class="Parameter"><Id>{pids[n_]}</Id><Name>{n_}</Name><X>1100</X><Y>{900 + 22 * k}</Y>{LABEL}{FLAGS_OFF}'
                   f'<Properties SaveInSnapshot="true" ModificatorType="STATIC"><Type>double</Type><UnitType>NONE</UnitType><SdArray>false</SdArray>'
                   f'<DefaultValue Class="CodeValue"><Code>{v}</Code></DefaultValue><ParameterEditor><Id>{nid()}</Id><EditorContolType>TEXT_BOX</EditorContolType>'
                   f'<MinSliderValue>0</MinSliderValue><MaxSliderValue>100</MaxSliderValue><DelimeterType>NO_DELIMETER</DelimeterType></ParameterEditor>'
                   f'</Properties><Description>{escape(d)}</Description></Variable>')
i = s.index('<Variable Class="PlainVariable">')  # los parámetros van antes de las variables (en Main, el primero)
s = s[:i] + xml_params + s[i:]

# experimentos: los parámetros nuevos sin valor (toman el default)
for n_ in pids:
    rep("</Parameters>\n<PresentationProperties>", f"<Parameter><ParameterName>{n_}</ParameterName></Parameter></Parameters>\n<PresentationProperties>", 2)
    rep("</FreeformParamValue><RangeVariationParamValue>", f"</FreeformParamValue><FreeformParamValue><Id>{pids[n_]}</Id></FreeformParamValue><RangeVariationParamValue>")
    rep("</RangeVariationParamValue>\n<ModelTimeProperties>", f"</RangeVariationParamValue><RangeVariationParamValue><Id>{pids[n_]}</Id><Type>FIXED</Type></RangeVariationParamValue>\n<ModelTimeProperties>")

FUNCS = [
    ("glpKg", "return kgGLPPorDiaCaliente / 24 * horasCaliente;"),
    ("costoLuz", "return kWhTotal() * tarifaKWh;"),
    ("costoGLP", "return glpKg() * precioGLPkg;"),
    ("costoCapital", "return tasaCapitalMensual * areaColaKg / (24 * 30.4375) * costoProductoKg;"),
    ("costoTotal", "return costoLuz() + costoGLP() + costoCapital();"),
]
fx = ""
for k, (n_, body) in enumerate(FUNCS):
    fx += (f'<Function AccessType="public" StaticFunction="false"><ReturnModificator>RETURNS_VALUE</ReturnModificator><ReturnType>double</ReturnType>'
           f'<Id>{nid()}</Id><Name>{n_}</Name><X>1700</X><Y>{1200 + 22 * k}</Y><PublicFlag>true</PublicFlag><PresentationFlag>false</PresentationFlag>'
           f'<ShowLabel>true</ShowLabel>{LABEL}<Body>{escape(body)}</Body></Function>')
rep("</Functions>", fx + "</Functions>")

# CSV: columnas nuevas al final
rep('+ "utilizacion;fraccionCaliente;kWhTotal;kWhPorKg;costoEnergiaPorKg";',
    '+ "utilizacion;fraccionCaliente;kWhTotal;kWhPorKg;costoEnergiaPorKg;glpKg;costoLuz;costoGLP;costoCapital;costoTotal";')
rep("horasOcupado / h, horasCaliente / h, kWhTotal(), kWhTotal() / kgTratados, kWhTotal() / kgTratados * tarifaKWh };",
    "horasOcupado / h, horasCaliente / h, kWhTotal(), kWhTotal() / kgTratados, kWhTotal() / kgTratados * tarifaKWh,\n"
    "    glpKg(), costoLuz(), costoGLP(), costoCapital(), costoTotal() };")
# resumen en consola
rep(escape('kWh/kg %.3f",'), escape('kWh/kg %.3f, costo total %.1f M$ (luz %.1f, gas %.1f, capital %.1f)",'))
rep("media(esperas) / 24, cuantil(esperas, 0.9) / 24, kWhTotal() / kgTratados));",
    "media(esperas) / 24, cuantil(esperas, 0.9) / 24, kWhTotal() / kgTratados,\n    costoTotal() / 1e6, costoLuz() / 1e6, costoGLP() / 1e6, costoCapital() / 1e6));")

ET.fromstring(s.encode("utf-8"))
ALP.write_text(s, encoding="utf-8", newline="\n")
print("Costos agregados a", ALP.name)
