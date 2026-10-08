#!/usr/bin/env python3
"""Validación de la Etapa 1 (05- §4.1): escenario base E0 contra el registro real del MISMO período que las
entradas (ULI lavadas del 15/08/2025 al 14/08/2026).

Uso, desde la raíz del repo:
    .venv/Scripts/python.exe -I materias/SIM/entregables/TPI/caser/modelo/validar_etapa1.py [corridas_horno.csv]

Lee el registro desde datos-locales/ (gitignorado; solo existe en las máquinas con los datos) y las 30 réplicas
de E0 del CSV del experimento CorridasE0E3. Imprime una tabla con agregados (no hay filas individuales).

Criterios (05- §4.1): error relativo de la media contra la tolerancia de cada métrica, e intervalo de Welch al
95 % para la diferencia entre las observaciones reales (campañas, ULI o meses) y las 30 réplicas del modelo.
pPrioridad se estimó contando encendidos chicos: la proporción de encendidos por prioridad se informa pero
NO cuenta como validación (calibrar no es validar).
"""
import csv
import math
import statistics
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings("ignore")
sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from analizar_corridas import t_cuantil  # noqa: E402

DATOS = AQUI.parent / "datos-locales"
CSV_M = Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI / "corridas_horno.csv"
INI, FIN = pd.Timestamp("2025-08-15"), pd.Timestamp("2026-08-14")
KWH_BASE_MES = 2750  # término constante de la regresión (horno_regresion3.py): el medidor lo registra aunque no haya campaña
ESPERA_RETENIDA = 30  # días: más que esto es producto "sin apuro" retenido a propósito (encargado, 07/10/2026)

# ---------------- registro real ----------------
tr = pd.read_excel(DATOS / "Simulación" / "Seguimiento TR ulis.xlsx", sheet_name="Tablero TR ULIS", header=1, engine="openpyxl")
for c in ["Inicio Prensa", "Lavado", "Cementado"]:
    tr[c] = pd.to_datetime(tr[c], errors="coerce")
tr["kg"] = pd.to_numeric(tr["Cant. x U.L.I."], errors="coerce") * pd.to_numeric(tr["P. Pieza"], errors="coerce")
tr = tr[(tr["Inicio Prensa"] >= "2023-01-01") & (tr["Inicio Prensa"] <= "2026-09-30")]
ok = tr["Cementado"].notna() & (tr["Cementado"] - tr["Lavado"]).dt.days.between(-1, 400)
cem = tr[ok].copy()
ULT = cem["Cementado"][cem["Cementado"] <= "2026-12-31"].max()
# Días sueltos de 1-2 ULI = error de planilla (encargado, 07/10/2026): se excluyen esas ULI.
cem["dia"] = cem["Cementado"].dt.normalize()
_d = pd.Series(sorted(cem["dia"].unique()))
_c = (_d.diff().dt.days.fillna(99) > 3).cumsum()
for _, _g in _d.groupby(_c):
    if cem["dia"].between(_g.min(), _g.max()).sum() <= 2:
        cem = cem[~cem["dia"].between(_g.min(), _g.max())]

# Campañas: fechas de cementado separadas por más de 3 días (mismo criterio que campanas_cola.py)
dd = pd.Series(sorted(cem["Cementado"].dt.normalize().unique()))
dd = dd[dd >= "2024-01-01"].reset_index(drop=True)
cid = (dd.diff().dt.days.fillna(99) > 3).cumsum()
camps = []
for _, g in dd.groupby(cid):
    a, b = g.min(), g.max()
    en = cem[(cem["Cementado"] >= a) & (cem["Cementado"] <= b)]
    cola = ((cem["Lavado"] <= a - pd.Timedelta(days=1)) & (cem["Cementado"] >= a)).sum()
    camps.append({"ini": a, "fin": b, "dias": (b - a).days + 1, "uli": len(en), "cola": int(cola)})
camps = pd.DataFrame(camps)
# Ventana: campañas que empiezan dentro del período. La última termina en el corte de datos (07/08/2026).
cv = camps[(camps["ini"] >= INI) & (camps["ini"] <= min(FIN, ULT))]
meses_ventana = ((min(FIN, ULT) - INI).days + 1) / 30.4375

lav = cem[cem["Lavado"].between(INI, FIN) & (cem["Cementado"] <= ULT)]
espera_todas = (lav["Cementado"].dt.normalize() - lav["Lavado"].dt.normalize()).dt.days.clip(lower=0)
espera = espera_todas[espera_todas <= ESPERA_RETENIDA]  # el modelo no representa el producto retenido sin demanda
kg_mes = cem[cem["Cementado"].between(INI, ULT)]["kg"].sum() / meses_ventana / 1000
fac = pd.read_csv(DATOS / "_perfil" / "facturas_energia.csv")
fac = fac[(fac["tipo"] == "Horno") & (pd.to_datetime(fac["periodo_hasta"]) > INI) & (pd.to_datetime(fac["periodo_hasta"]) <= "2026-04-30")]
kwh_mes = fac["kwh_activa"].astype(float)

# ---------------- modelo (E0, 30 réplicas) ----------------
filas = [f for f in csv.DictReader(open(CSV_M, encoding="utf-8"), delimiter=";") if f["escenario"] == "E0"]
assert len(filas) == 30, f"se esperan 30 réplicas de E0, hay {len(filas)}"
M = {k: np.array([float(f[k]) for f in filas]) for k in filas[0] if k not in ("escenario", "modoFinCampana")}
horas = M["horasMedidas"]
mod = {
    "campanasPorMes": M["campanasPorMes"],
    "uli": M["uliPorCampanaMedia"],
    "dias": M["diasPorCampanaMedia"],
    "cola": M["colaAlEncenderMedia"],
    "esperaMedia": M["esperaMediaDias"],
    "esperaP90": M["esperaP90Dias"],
    "tMes": M["kgTratados"] / (horas / 24 / 30.4375) / 1000,
    "kwhMes": M["kWhTotal"] / (horas / 24 / 30.4375) + KWH_BASE_MES,
    "fracPrioridad": M["nEncendidosPrioridad"] / M["nEncendidos"],
}
reales = {
    "campanasPorMes": (np.array([len(cv) / meses_ventana]), None),
    "uli": (cv["uli"].to_numpy(float), "campañas"),
    "dias": (cv["dias"].to_numpy(float), "campañas"),
    "cola": (cv["cola"].to_numpy(float), "campañas"),
    "esperaMedia": (espera.to_numpy(float), "ULI"),
    "esperaP90": (np.array([float(np.quantile(espera, 0.9, method="inverted_cdf"))]), None),
    "tMes": (np.array([kg_mes]), None),
    "kwhMes": (kwh_mes.to_numpy(float), "meses"),
    "fracPrioridad": (np.array([(cv["dias"] < 7).mean()]), None),
}
NOMBRES = [
    ("campanasPorMes", "Campañas por mes", 0.10),
    ("uli", "ULI por campaña", 0.10),
    ("dias", "Duración de campaña (días)", 0.10),
    ("cola", "Cola al encender (ULI)", None),
    ("esperaMedia", "Espera media, sin retenidas (días)", 0.15),
    ("esperaP90", "Espera p90, sin retenidas (días)", None),
    ("tMes", "Toneladas tratadas por mes", 0.10),
    ("kwhMes", "kWh del horno por mes", 0.15),
    ("fracPrioridad", "Fracción de encendidos cortos (< 7 días)", None),
]


def welch(x, y):
    """IC 95 % de mean(y) - mean(x), Welch-Satterthwaite."""
    vx, vy = np.var(x, ddof=1) / len(x), np.var(y, ddof=1) / len(y)
    gl = (vx + vy) ** 2 / (vx ** 2 / (len(x) - 1) + vy ** 2 / (len(y) - 1))
    h = t_cuantil(0.05, gl) * math.sqrt(vx + vy)
    d = y.mean() - x.mean()
    return d - h, d + h


print(f"Validación E0 contra el registro, {INI.date()} a {min(FIN, ULT).date()} ({meses_ventana:.1f} meses; "
      f"{len(cv)} campañas, {len(espera)} ULI; kWh: {len(kwh_mes)} facturas sep/2025-abr/2026)\n")
print(f"{'métrica':42s} {'registro':>9s} {'n':>5s} {'modelo':>9s} {'error':>8s} {'tol':>6s}  {'Welch 95 % (modelo − real)':28s} veredicto")
for k, nombre, tol in NOMBRES:
    x, unidad = reales[k]
    y = mod[k]
    err = (y.mean() - x.mean()) / x.mean()
    if unidad and len(x) > 1:
        lo, hi = welch(x, y)
        w = f"[{lo:9.3g}; {hi:9.3g}]"
        cubre = lo <= 0 <= hi
    else:
        w, cubre = "(un solo valor real)", None
    if k == "fracPrioridad":
        ver = "calibrada, no valida"
    elif tol is None:
        ver = "informativa"
    else:
        dentro = abs(err) <= tol
        ver = ("OK" if dentro else "FUERA") + ("" if cubre is None else (" · Welch contiene 0" if cubre else " · Welch no contiene 0"))
    n = f"{len(x)}" if unidad else "-"
    print(f"{nombre:42s} {x.mean():9.3g} {n:>5s} {y.mean():9.3g} {100*err:+7.1f}% {'' if tol is None else f'{100*tol:.0f}%':>6s}  {w:28s} {ver}")

print("\nCampañas del registro en la ventana (inicio, días, ULI, cola al encender):")
for _, r in cv.iterrows():
    print(f"  {r['ini'].date()}  {r['dias']:3d} d  {r['uli']:4d} ULI  cola {r['cola']:3d}")
print(f"\nModelo, distribución de la espera entre réplicas: media {mod['esperaMedia'].mean():.2f} "
      f"(rango {mod['esperaMedia'].min():.2f}-{mod['esperaMedia'].max():.2f}); p90 {mod['esperaP90'].mean():.1f}")
print(f"Registro, espera de todas las ULI: media {espera_todas.mean():.2f}, p90 {np.quantile(espera_todas, .9):.0f}, "
      f"máx {espera_todas.max():.0f}; retenidas (> {ESPERA_RETENIDA} días, sin demanda): {100*(espera_todas > ESPERA_RETENIDA).mean():.1f} %")
