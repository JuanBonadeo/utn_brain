#!/usr/bin/env python3
"""Gráficos de resultados del informe del TPI Caser (2026-11-07).

Uso: graficos_informe.py [corridas.csv]   (por defecto corridas_horno.csv si existe, si no el del harness)
Escribe en materias/SIM/figs/:
  tpi-caser-costos.png        costo relevante del año por escenario, apilado en luz, gas y capital
  tpi-caser-compromiso.png    costo del año contra espera media, con IC 95 % de cada media
"""
import csv
import math
import statistics as st
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

AQUI = Path(__file__).resolve().parent
FIGS = AQUI.parents[3] / "figs"
if len(sys.argv) > 1:
    CSV = Path(sys.argv[1])
else:
    CSV = AQUI / "corridas_horno.csv"
    if not CSV.exists():
        CSV = AQUI / "corridas_horno_harness.csv"

ESC = ["E0", "E1", "E2", "E3"]
NOMBRE = {"E0": "E0 base", "E1": "E1 umbral 45", "E2": "E2 espera máx. 15 d", "E3": "E3 apagar enseguida"}
# Paleta categórica de referencia (validada: luz, gas, capital).
AZUL, NARANJA, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
TINTA, TINTA2, GRILLA, FONDO = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
T29 = 2.0452

filas = list(csv.DictReader(open(CSV, encoding="utf-8"), delimiter=";"))


def valores(e, col, k=1.0):
    return [float(f[col]) * k for f in filas if f["escenario"] == e]


def media_ic(v):
    return st.mean(v), T29 * st.stdev(v) / math.sqrt(len(v))


plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": TINTA2,
                     "axes.labelcolor": TINTA, "xtick.color": TINTA2, "ytick.color": TINTA2,
                     "figure.facecolor": FONDO, "axes.facecolor": FONDO, "savefig.facecolor": FONDO})


def ejes_limpios(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.set_axisbelow(True)


# 1. Costos apilados (barras horizontales, M$ por año).
fig, ax = plt.subplots(figsize=(7.2, 3.0), dpi=200)
partes = [("Luz", "costoLuz", AZUL), ("Gas (GLP)", "costoGLP", NARANJA), ("Capital inmovilizado", "costoCapital", AQUA)]
ys = list(range(len(ESC)))[::-1]
for y, e in zip(ys, ESC):
    x0 = 0.0
    for nombre, col, color in partes:
        w = st.mean(valores(e, col, 1e-6))
        ax.barh(y, w, left=x0, height=0.56, color=color, edgecolor=FONDO, linewidth=2,
                label=nombre if e == "E0" else None)
        if w > 4.5:
            ax.text(x0 + w / 2, y, f"{w:.1f}", ha="center", va="center", color="white", fontsize=8.5, fontweight="bold")
        x0 += w
    ax.text(x0 + 1.2, y, f"{x0:.1f} M$", va="center", color=TINTA, fontsize=9.5, fontweight="bold")
ax.set_yticks(ys, [NOMBRE[e] for e in ESC])
ax.set_xlabel("Costo relevante del año (millones de $, media de 30 réplicas)")
ax.set_xlim(0, 100)
ax.xaxis.grid(True, color=GRILLA, linewidth=0.8)
ejes_limpios(ax)
ax.legend(loc="upper center", bbox_to_anchor=(0.45, 1.18), ncol=3, frameon=False, fontsize=9)
fig.tight_layout()
fig.savefig(FIGS / "tpi-caser-costos.png")
plt.close(fig)

# 2. Compromiso costo contra espera.
fig, ax = plt.subplots(figsize=(6.4, 3.8), dpi=200)
desplaz = {"E0": (10, -16), "E1": (8, 6), "E2": (8, 10), "E3": (-14, 10)}
for e in ESC:
    mx, hx = media_ic(valores(e, "esperaMediaDias"))
    my, hy = media_ic(valores(e, "costoTotal", 1e-6))
    color = TINTA2 if e == "E0" else AZUL
    ax.errorbar(mx, my, xerr=hx, yerr=hy, fmt="o", ms=8, color=color, ecolor=color, elinewidth=1.5, capsize=3,
                markeredgecolor=FONDO, markeredgewidth=2)
    dx, dy = desplaz[e]
    ax.annotate(NOMBRE[e], (mx, my), textcoords="offset points", xytext=(dx, dy),
                ha="right" if dx < 0 else "left", color=TINTA, fontsize=9)
ax.set_xlabel("Espera media de una ULI antes del horno (días)")
ax.set_ylabel("Costo relevante del año (M$)")
ax.grid(True, color=GRILLA, linewidth=0.8)
ax.set_xlim(2.5, 9)
ejes_limpios(ax)
ax.text(0.99, 0.02, "Barras: IC 95 % de la media (30 réplicas)", transform=ax.transAxes, ha="right", va="bottom",
        color=TINTA2, fontsize=8)
fig.tight_layout()
fig.savefig(FIGS / "tpi-caser-compromiso.png")
plt.close(fig)
print(f"{CSV.name} -> {FIGS / 'tpi-caser-costos.png'}, {FIGS / 'tpi-caser-compromiso.png'}")
