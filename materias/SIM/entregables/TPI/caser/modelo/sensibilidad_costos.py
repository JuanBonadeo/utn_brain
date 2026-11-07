#!/usr/bin/env python3
"""Sensibilidad del costo relevante a los parámetros de costo (2026-11-07).

La dinámica del modelo (encendidos, horas a temperatura, kg en cola) no depende de los precios ni de los
coeficientes de energía: esos parámetros solo entran en las funciones de costo del final de la corrida. Por eso la
sensibilidad a ellos es exacta recalculando sobre las mismas 120 corridas, sin volver a simular:

  luz     = (kWhPorEncendido × nEncendidos + kWhPorDiaCaliente / 24 × horasCaliente) × tarifaKWh
  gas     = kgGLPPorDiaCaliente / 24 × horasCaliente × precioGLPkg
  capital = tasaCapitalMensual × colaMediaKg × costoProductoKg × meses medidos
  desgaste = costoPorEncendido × nEncendidos            (no está en el modelo: solo para el punto de equilibrio)

Uso: sensibilidad_costos.py [corridas.csv]   (por defecto corridas_horno.csv si existe, si no el del harness)
"""
import csv
import math
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).resolve().parent
if len(sys.argv) > 1:
    CSV = Path(sys.argv[1])
else:
    CSV = AQUI / "corridas_horno.csv"
    if not CSV.exists():
        CSV = AQUI / "corridas_horno_harness.csv"

BASE = dict(kWhPorEncendido=2303, kWhPorDiaCaliente=2402, tarifaKWh=102, kgGLPPorDiaCaliente=130,
            precioGLPkg=2250, costoProductoKg=4467, tasaCapitalMensual=0.02, costoPorEncendido=0)
# t de Student bilateral, 29 g.l.
T95, T_BONF = 2.0452, 2.5466  # 95 % y 98,33 % (Bonferroni 0,05/3)

filas = list(csv.DictReader(open(CSV, encoding="utf-8"), delimiter=";"))
por = {}
for f in filas:
    por.setdefault(f["escenario"], {})[int(f["semilla"])] = f


def costo(f, p):
    h = float(f["horasMedidas"])
    caliente = float(f["fraccionCaliente"]) * h
    enc = float(f["nEncendidos"])
    kwh = p["kWhPorEncendido"] * enc + p["kWhPorDiaCaliente"] / 24 * caliente
    luz = kwh * p["tarifaKWh"]
    gas = p["kgGLPPorDiaCaliente"] / 24 * caliente * p["precioGLPkg"]
    capital = p["tasaCapitalMensual"] * float(f["colaMediaKg"]) * p["costoProductoKg"] * h / (24 * 30.4375)
    return luz + gas + capital + p["costoPorEncendido"] * enc


def dif(esc, p, fn=costo):
    d = [fn(por[esc][s], p) - fn(por["E0"][s], p) for s in sorted(por["E0"])]
    n = len(d)
    m = sum(d) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in d) / (n - 1))
    return m, T_BONF * sd / math.sqrt(n)


# Control: con los parámetros base tiene que reproducir costoTotal del CSV.
err = max(abs(costo(f, BASE) - float(f["costoTotal"])) / float(f["costoTotal"]) for f in filas)
assert err < 1e-4, f"el recálculo no reproduce costoTotal del CSV (error relativo {err:.2e})"

print(f"{CSV.name}: {len(filas)} corridas. Recálculo base = costoTotal del CSV (error relativo máx. {err:.1e}).")
print("Diferencia de costo relevante del año contra E0, en millones de $, IC 98,3 % (Bonferroni). − = ahorro.\n")

CASOS = [
    ("Base", {}),
    ("kWh por encendido = 0", dict(kWhPorEncendido=0)),
    ("kWh por encendido = 5.220 (techo teórico)", dict(kWhPorEncendido=5220)),
    ("GLP 100 kg/día caliente (solo 2025-2026)", dict(kgGLPPorDiaCaliente=100)),
    ("Tarifa 290 $/kWh (promedio con cargo fijo)", dict(tarifaKWh=290)),
    ("Capital al 1 % mensual", dict(tasaCapitalMensual=0.01)),
    ("Capital al 4 % mensual", dict(tasaCapitalMensual=0.04)),
    ("Producto a la mitad del costo (antes del horno)", dict(costoProductoKg=4467 / 2)),
    ("Desgaste 1 M$ por encendido", dict(costoPorEncendido=1e6)),
]
esc = [e for e in ("E1", "E2", "E3") if e in por]
print(f"{'caso':48s}" + "".join(f"{e:>22s}" for e in esc))
for nombre, cambio in CASOS:
    p = {**BASE, **cambio}
    celdas = []
    for e in esc:
        m, h = dif(e, p)
        celdas.append(f"{m / 1e6:+8.2f} ± {h / 1e6:5.2f}")
    print(f"{nombre:48s}" + "".join(f"{c:>22s}" for c in celdas))

# Punto de equilibrio de E3: costo por encendido no modelado (desgaste + gas de arranque) que anula el ahorro.
print()
for e in esc:
    ahorro, _ = dif(e, BASE)
    denc, _ = dif(e, BASE, lambda f, p: float(f["nEncendidos"]))
    if denc > 0 and ahorro < 0:
        print(f"{e}: {denc:+.2f} encendidos/año contra E0; el ahorro de {-ahorro / 1e6:.1f} M$ se anula con un costo no "
              f"modelado de {-ahorro / denc / 1e6:.1f} M$ por encendido.")
    else:
        print(f"{e}: {denc:+.2f} encendidos/año contra E0, diferencia de costo {ahorro / 1e6:+.1f} M$ (no hay ahorro que anular).")
