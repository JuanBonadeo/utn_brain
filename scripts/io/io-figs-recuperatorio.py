#!/usr/bin/env python3
"""
io-figs-recuperatorio.py — Figuras del resumen del recuperatorio de IO.

Genera en materias/IO/figs/ los PNG r-*.png que usa
materias/IO/estudio/recuperatorio/resumen-recuperatorio.md. Todo sale de datos
fijos (el parcial 2026-10-03, ejemplos del apunte o ejemplos propios marcados
como tales): correrlo dos veces da lo mismo.

Uso (desde la raíz del repo):
    .venv/bin/python scripts/io/io-figs-recuperatorio.py
"""
import heapq
import math
from collections import deque
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

OUT = Path(__file__).resolve().parents[2] / "materias" / "IO" / "figs"
OUT.mkdir(parents=True, exist_ok=True)

# ── estilo (el mismo que el resumen de SIM) ───────────────────────────────
INK = "#1f2937"
MUTED = "#6b7280"
GRID = "#e5e7eb"
BLUE = "#2563eb"
BLUE_L = "#dbeafe"
GREEN = "#16a34a"
GREEN_L = "#dcfce7"
RED = "#dc2626"
RED_L = "#fee2e2"
ORANGE = "#ea580c"
ORANGE_L = "#ffedd5"
PURPLE = "#7c3aed"
PURPLE_L = "#ede9fe"
GRAY_L = "#f3f4f6"

plt.rcParams.update({
    "font.family": ["Arial", "DejaVu Sans"],
    "font.size": 10,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": INK,
    "axes.titlecolor": INK,
    "axes.titlesize": 11,
    "axes.titleweight": "bold",
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "text.color": INK,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.12,
    "axes.formatter.use_locale": False,
})


def coma(x, d=2):
    """Número con coma decimal y punto de miles."""
    s = f"{x:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def save(fig, name):
    fig.savefig(OUT / name, facecolor="white")
    plt.close(fig)
    print("  ✓", name)


def canvas(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, text, fc=GRAY_L, ec=MUTED, color=INK, size=9.5,
        weight="normal", r=0.08, lw=1.2, ha="center"):
    p = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                       boxstyle=f"round,pad=0,rounding_size={r}",
                       fc=fc, ec=ec, lw=lw)
    ax.add_patch(p)
    tx = x if ha == "center" else x - w / 2 + 0.12
    ax.text(tx, y, text, ha=ha, va="center", fontsize=size, color=color,
            weight=weight, linespacing=1.35)
    return p


def arrow(ax, p1, p2, color=MUTED, lw=1.4, style="-|>", rad=0.0, ls="-",
          ms=12, shrinkA=2, shrinkB=2):
    a = FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=ms,
                        color=color, lw=lw, ls=ls,
                        connectionstyle=f"arc3,rad={rad}",
                        shrinkA=shrinkA, shrinkB=shrinkB)
    ax.add_patch(a)
    return a


# ── geometría de PL: región factible por recorte de semiplanos ────────────
def clip(poly, a, b, c):
    """Recorta el polígono con el semiplano a·x + b·y <= c (Sutherland–Hodgman)."""
    out = []
    n = len(poly)
    for k in range(n):
        p, q = poly[k], poly[(k + 1) % n]
        fp = a * p[0] + b * p[1] - c
        fq = a * q[0] + b * q[1] - c
        if fp <= 1e-9:
            out.append(p)
        if (fp < -1e-9 and fq > 1e-9) or (fp > 1e-9 and fq < -1e-9):
            t = fp / (fp - fq)
            out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
    return out


def region(cons, xmax, ymax):
    """cons: lista de (a, b, signo, c) con signo '<=' o '>='."""
    poly = [(0, 0), (xmax, 0), (xmax, ymax), (0, ymax)]
    for a, b, s, c in cons:
        if s == ">=":
            a, b, c = -a, -b, -c
        poly = clip(poly, a, b, c)
        if not poly:
            break
    return poly


def recta(ax, a, b, c, xmax, ymax, color=MUTED, lw=1.3, ls="-", label=None,
          lpos=None, lsize=8.5):
    """Dibuja a·x + b·y = c dentro de la caja [0,xmax]x[0,ymax]."""
    if abs(b) < 1e-12:
        xs = np.array([c / a, c / a])
        ys = np.array([0, ymax])
    else:
        xs = np.linspace(0, xmax, 200)
        ys = (c - a * xs) / b
        ok = (ys >= -0.02 * ymax) & (ys <= ymax * 1.02)
        xs, ys = xs[ok], ys[ok]
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, zorder=3)
    if label and lpos:
        ax.text(*lpos, label, color=color, fontsize=lsize, ha="center",
                va="center", weight="bold", zorder=6,
                bbox=dict(fc="white", ec="none", pad=0.6, alpha=0.85))


def ejes(ax, xmax, ymax, xl="$x_1$", yl="$x_2$"):
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, ymax)
    ax.set_xlabel(xl)
    ax.set_ylabel(yl, rotation=0, labelpad=10)
    ax.grid(color=GRID, lw=0.6, zorder=0)


# ═════════════════════════════════════════════════════════════════════════
# 0. Mapa del recuperatorio
# ═════════════════════════════════════════════════════════════════════════
def fig_mapa():
    fig, ax = canvas(11, 5.6)
    ax.text(5.5, 5.3, "Parcial 2026 (Tema 1): tres ejercicios con preguntas de valor puntual",
            ha="center", fontsize=11.5, weight="bold")
    cols = [
        (1.95, "Ejercicio 1\nMétodo gráfico", BLUE, BLUE_L,
         ["coordenadas del óptimo", "¿un punto es factible?", "restricciones activas",
          "holgura en un punto dado", "valor óptimo con unidad"], "§2"),
        (5.5, "Ejercicio 2\nModelo + tabla simplex", PURPLE, PURPLE_L,
         ["¿se detiene o sigue? entra/sale", "tabla inicial: quién entra/sale",
          "precio sombra y su significado", "rango de un $c_j$", "función dual",
          "costo reducido e interpretación"], "§4 a §7 (resuelto en §7)"),
        (9.05, "Ejercicio 3\nStock", GREEN, GREEN_L,
         ["lote óptimo sin restricción", "inversión promedio",
          "λ de la restricción de capital", "lote con la restricción",
          "¿conviene un crédito al 12 %?"], "§8 (resuelto en §8.8)"),
    ]
    for x, title, c, cl, items, ref in cols:
        box(ax, x, 4.45, 3.2, 0.82, title, fc=cl, ec=c, color=c, weight="bold", size=10.5)
        y = 3.75
        for it in items:
            ax.text(x - 1.48, y, "•  " + it, fontsize=9.2, va="center")
            y -= 0.42
        ax.text(x, 1.05, "→ " + ref, ha="center", fontsize=9.5, color=c, weight="bold")
    box(ax, 5.5, 0.38, 10.4, 0.55,
        "Puede caer además: transporte, asignación y transbordo (§9) · entera y mixta (§10) · redes (§11) · teoría (§12)",
        fc=GRAY_L, ec=MUTED, size=9.4)
    save(fig, "r-mapa.png")


# ═════════════════════════════════════════════════════════════════════════
# 1. Tipos de solución y de restricción (método gráfico)
# ═════════════════════════════════════════════════════════════════════════
def fig_tipos():
    fig, axs = plt.subplots(2, 3, figsize=(11.5, 7.4))
    X = Y = 9

    def base(ax, title, color=INK):
        ejes(ax, X, Y)
        ax.set_title(title, color=color, fontsize=10.5)
        ax.set_aspect("equal")

    # (a) única
    ax = axs[0, 0]
    base(ax, "Óptimo único", GREEN)
    cons = [(1, 1, "<=", 7), (1, 0, "<=", 5), (0, 1, "<=", 6)]
    ax.add_patch(Polygon(region(cons, X, Y), fc=BLUE_L, ec="none", zorder=1))
    for a, b, s, c in cons:
        recta(ax, a, b, c, X, Y)
    recta(ax, 3, 2, 19, X, Y, color=ORANGE, ls="--", lw=1.6)
    ax.plot(5, 2, "o", color=GREEN, ms=8, zorder=7)
    ax.annotate("único vértice\nóptimo (5; 2)", (5, 2), (6.2, 4.3), fontsize=8.5,
                color=GREEN, arrowprops=dict(arrowstyle="-|>", color=GREEN))
    ax.text(0.4, 8.3, "Max z = 3x₁ + 2x₂", fontsize=8.5, color=MUTED)

    # (b) múltiples
    ax = axs[0, 1]
    base(ax, "Óptimos alternativos", PURPLE)
    cons = [(1, 1, "<=", 7), (1, 0, "<=", 5), (0, 1, "<=", 6)]
    ax.add_patch(Polygon(region(cons, X, Y), fc=BLUE_L, ec="none", zorder=1))
    for a, b, s, c in cons:
        recta(ax, a, b, c, X, Y)
    ax.plot([1, 5], [6, 2], color=PURPLE, lw=4.5, zorder=5, solid_capstyle="round")
    ax.plot([1, 5], [6, 2], "o", color=PURPLE, ms=8, zorder=7)
    ax.text(3.6, 4.8, "todo el segmento\nes óptimo", color=PURPLE, fontsize=8.5,
            ha="left", weight="bold")
    ax.text(0.4, 8.3, "Max z = 2x₁ + 2x₂  ∥  x₁ + x₂ ≤ 7", fontsize=8.5, color=MUTED)

    # (c) no acotada
    ax = axs[0, 2]
    base(ax, "Solución no acotada", RED)
    cons = [(-1, 1, "<=", 2), (1, -1, "<=", 2)]
    ax.add_patch(Polygon(region(cons, X, Y), fc=BLUE_L, ec="none", zorder=1))
    for a, b, s, c in cons:
        recta(ax, a, b, c, X, Y)
    arrow(ax, (3.5, 3.5), (7.4, 7.4), color=RED, lw=2.4, ms=16)
    ax.text(5.9, 4.6, "z → ∞", color=RED, fontsize=11, weight="bold")
    ax.text(0.4, 8.3, "Max z = x₁ + x₂", fontsize=8.5, color=MUTED)

    # (d) RF no acotada con óptimo finito
    ax = axs[1, 0]
    base(ax, "RF no acotada, óptimo finito", GREEN)
    cons = [(1, 2, ">=", 6), (2, 1, ">=", 6)]
    ax.add_patch(Polygon(region(cons, X, Y), fc=BLUE_L, ec="none", zorder=1))
    for a, b, s, c in cons:
        recta(ax, a, b, c, X, Y)
    recta(ax, 1, 1, 4, X, Y, color=ORANGE, ls="--", lw=1.6)
    ax.plot(2, 2, "o", color=GREEN, ms=8, zorder=7)
    ax.annotate("mínimo (2; 2)", (2, 2), (3.6, 1.0), fontsize=8.5, color=GREEN,
                arrowprops=dict(arrowstyle="-|>", color=GREEN))
    ax.text(0.4, 8.3, "Min w = x₁ + x₂", fontsize=8.5, color=MUTED)
    ax.text(5.2, 6.8, "la RF sigue\nabierta, pero\nW no baja más", fontsize=8.3,
            color=MUTED, ha="center")

    # (e) no factible
    ax = axs[1, 1]
    base(ax, "No factible: RF = ∅", RED)
    ax.add_patch(Polygon(region([(1, 1, "<=", 3)], X, Y), fc=ORANGE_L, ec="none", zorder=1))
    ax.add_patch(Polygon(region([(1, 1, ">=", 6)], X, Y), fc=PURPLE_L, ec="none", zorder=1))
    recta(ax, 1, 1, 3, X, Y, color=ORANGE, label="x₁+x₂ ≤ 3", lpos=(1.2, 0.8))
    recta(ax, 1, 1, 6, X, Y, color=PURPLE, label="x₁+x₂ ≥ 6", lpos=(6.4, 3.6))
    ax.text(4.6, 7.5, "los semiplanos no\nse cortan", fontsize=8.5, color=RED, ha="center")

    # (f) clasificación de restricciones
    ax = axs[1, 2]
    base(ax, "Activa · pasiva · redundante", INK)
    cons = [(1, 1, "<=", 6), (1, 0, "<=", 4), (0, 1, "<=", 5), (1, 2, "<=", 14)]
    ax.add_patch(Polygon(region(cons, X, Y), fc=BLUE_L, ec="none", zorder=1))
    recta(ax, 1, 1, 6, X, Y, color=GREEN, lw=1.8, label="① activa", lpos=(2.3, 3.0))
    recta(ax, 1, 0, 4, X, Y, color=GREEN, lw=1.8, label="② activa", lpos=(4.0, 6.6))
    recta(ax, 0, 1, 5, X, Y, color=BLUE, lw=1.8, label="③ pasiva necesaria", lpos=(6.3, 5.4))
    recta(ax, 1, 2, 14, X, Y, color=MUTED, ls="--", label="④ redundante", lpos=(6.6, 3.9))
    ax.plot(4, 2, "o", color=GREEN, ms=8, zorder=7)
    ax.text(0.3, 8.3, "Max z = 2x₁ + x₂\nóptimo (4; 2)", fontsize=8.5, color=MUTED, va="center")
    fig.tight_layout(h_pad=2.0)
    save(fig, "r-tipos-solucion.png")


# ═════════════════════════════════════════════════════════════════════════
# 2. Parcial 2026, ejercicio 1 (gráfico)
# ═════════════════════════════════════════════════════════════════════════
def fig_parcial_ej1():
    fig, ax = plt.subplots(figsize=(9.2, 5.6))
    X, Y = 136, 68
    ejes(ax, X, Y)
    cons = [(3, 10, ">=", 300), (1, 2, "<=", 120), (-1, 1, "<=", 30)]
    ax.add_patch(Polygon(region(cons, X, Y), fc=BLUE_L, ec="none", zorder=1))
    recta(ax, 3, 10, 300, X, Y, color=INK, lw=1.5, label="① 3x₁ + 10x₂ ≥ 300", lpos=(76, 12.5))
    recta(ax, 1, 2, 120, X, Y, color=INK, lw=1.5, label="② x₁ + 2x₂ ≤ 120", lpos=(88, 22))
    recta(ax, -1, 1, 30, X, Y, color=INK, lw=1.5, label="③ −x₁ + x₂ ≤ 30", lpos=(31, 61))
    recta(ax, 150, 500, 28000, X, Y, color=ORANGE, ls="--", lw=1.4)
    ax.text(108, 25.3, "W = 28.000", color=ORANGE, fontsize=8.5, rotation=-11)
    ax.plot([0, 100], [30, 0], color=PURPLE, lw=5, zorder=4, solid_capstyle="round", alpha=0.9)
    ax.text(38, 10, "W = 15.000 en todo el segmento\n(la isocosto es paralela a ①)",
            color=PURPLE, fontsize=9, weight="bold", rotation=-15, ha="center", va="center")
    pts = {"A (0; 30)": (0, 30), "B (20; 50)": (20, 50), "C (120; 0)": (120, 0),
           "D (100; 0)": (100, 0)}
    offs = {"A (0; 30)": (2, -5), "B (20; 50)": (3, -4.5), "C (120; 0)": (1.5, 2.5),
            "D (100; 0)": (1.5, 2.5)}
    for k, (x, y) in pts.items():
        ax.plot(x, y, "o", color=INK, ms=6, zorder=7)
        ax.text(x + offs[k][0], y + offs[k][1], k, fontsize=8.8, weight="bold")
    ax.plot(50, 30, "s", color=GREEN, ms=8, zorder=7)
    ax.annotate("P (50; 30) factible:\n①450 ≥ 300 · ②110 ≤ 120 · ③−20 ≤ 30", (50, 30),
                (62, 45), fontsize=8.5, color=GREEN,
                arrowprops=dict(arrowstyle="-|>", color=GREEN))
    ax.annotate("en D la holgura de ②\nvale 120 − 100 = 20", (99.5, 0.8), (112, 16),
                fontsize=8.5, color=BLUE, ha="center",
                arrowprops=dict(arrowstyle="-|>", color=BLUE))
    arrow(ax, (70, 40), (64, 20), color=ORANGE, lw=1.6)
    ax.text(71, 36, "W baja", color=ORANGE, fontsize=8.5)
    ax.set_title("Min W = 150x₁ + 500x₂ — región factible y óptimos alternativos")
    save(fig, "r-parcial-ej1.png")


# ═════════════════════════════════════════════════════════════════════════
# 3. Algoritmo simplex (diagrama de flujo)
# ═════════════════════════════════════════════════════════════════════════
def fig_simplex_flujo():
    fig, ax = canvas(11, 7.4)
    W = 3.5
    box(ax, 2.4, 6.9, W, 0.62, "1. Forma estándar\n(holguras, excesos, ficticias)", fc=GRAY_L)
    box(ax, 2.4, 5.85, W, 0.62, "2. Base inicial = identidad\n(holguras y ficticias)", fc=GRAY_L)
    box(ax, 2.4, 4.8, W, 0.62, "3. Calcular  $z_j = c_B\\,Y_j$  y  $c_j - z_j$", fc=GRAY_L)
    box(ax, 2.4, 3.6, W, 0.8, "¿Todos los $c_j - z_j \\leq 0$?\n(Max; en Min: ≥ 0)",
        fc=PURPLE_L, ec=PURPLE, color=PURPLE, weight="bold")
    box(ax, 2.4, 2.25, W, 0.62, "4. ENTRA el mayor $c_j - z_j > 0$\n(condición de optimización)",
        fc=BLUE_L, ec=BLUE)
    box(ax, 2.4, 1.1, W, 0.8, "¿La columna entrante tiene\nalgún $y_{ij} > 0$?",
        fc=PURPLE_L, ec=PURPLE, color=PURPLE, weight="bold")
    box(ax, 7.4, 1.1, 3.7, 0.62, "5. SALE el de menor  $\\theta = x_i / y_{ij}$\n(condición de factibilidad)",
        fc=BLUE_L, ec=BLUE)
    box(ax, 7.4, 2.25, 3.7, 0.62, "6. Pivotear: fila pivote ÷ pivote;\nel resto, a cero en esa columna",
        fc=GRAY_L)
    box(ax, 7.4, 3.6, 3.7, 0.62, "ÓPTIMO → diagnosticar\n(única / alternativa / degenerada / no factible)",
        fc=GREEN_L, ec=GREEN, color=GREEN, weight="bold")
    box(ax, 2.4, 0.08 + 0.05, 2.6, 0.42, "NO ACOTADA: z → ∞", fc=RED_L, ec=RED, color=RED,
        weight="bold", size=9)
    for y1, y2 in [(6.59, 6.16), (5.54, 5.11), (4.49, 4.0), (3.2, 2.56), (1.94, 1.5)]:
        arrow(ax, (2.4, y1), (2.4, y2))
    arrow(ax, (4.15, 3.6), (5.55, 3.6), color=GREEN, lw=1.8)
    ax.text(4.85, 3.75, "sí", color=GREEN, fontsize=9.5, weight="bold")
    ax.text(2.55, 2.93, "no", color=MUTED, fontsize=9.5, weight="bold")
    arrow(ax, (4.15, 1.1), (5.55, 1.1), color=BLUE, lw=1.6)
    ax.text(4.85, 1.25, "sí", color=BLUE, fontsize=9.5, weight="bold")
    arrow(ax, (2.4, 0.7), (2.4, 0.36), color=RED, lw=1.6)
    ax.text(2.55, 0.5, "no", color=RED, fontsize=9.5, weight="bold")
    arrow(ax, (7.4, 1.41), (7.4, 1.94))
    ax.plot([9.25, 9.85, 9.85, 5.0], [2.25, 2.25, 4.8, 4.8], color=MUTED, lw=1.4)
    arrow(ax, (5.0, 4.8), (4.15, 4.8))
    ax.text(7.4, 4.92, "nueva tabla: volver al paso 3", ha="center", fontsize=8.8, color=MUTED)
    ax.text(5.6, 6.6, "Ficticias en la función objetivo:\n   Max → $-M\\,x_f$     Min → $+M\\,x_f$\n"
            "Si al óptimo queda una ficticia\nbásica con valor > 0 → RF = ∅",
            fontsize=9.2, color=INK, va="center",
            bbox=dict(fc=ORANGE_L, ec=ORANGE, boxstyle="round,pad=0.5"))
    save(fig, "r-simplex-flujo.png")


# ═════════════════════════════════════════════════════════════════════════
# 4. Parcial 2026, ejercicio 2: tabla dada y tabla óptima, anotadas
# ═════════════════════════════════════════════════════════════════════════
def tabla(ax, x0, y0, rows, header, cw, rh, colors=None, bold_rows=()):
    """Dibuja una tabla. rows: lista de listas de str. colors: {(r, c): color}."""
    colors = colors or {}
    for j, h in enumerate(header):
        x = x0 + sum(cw[:j])
        ax.add_patch(Rectangle((x, y0), cw[j], rh, fc="#e5e7eb", ec="white", lw=1.5))
        ax.text(x + cw[j] / 2, y0 + rh / 2, h, ha="center", va="center",
                fontsize=9.3, weight="bold")
    for i, row in enumerate(rows):
        y = y0 - (i + 1) * rh
        for j, v in enumerate(row):
            x = x0 + sum(cw[:j])
            fc = colors.get((i, j), "white" if i % 2 == 0 else "#fafafa")
            ax.add_patch(Rectangle((x, y), cw[j], rh, fc=fc, ec=GRID, lw=0.8))
            ax.text(x + cw[j] / 2, y + rh / 2, v, ha="center", va="center",
                    fontsize=9.3, weight="bold" if i in bold_rows else "normal")


def fig_parcial_ej2():
    fig, ax = canvas(12.6, 10.6)
    cw = [0.75, 0.85] + [0.92] * 7 + [1.15, 1.2]
    rh = 0.42
    header = ["$c_B$", "Base", "$A_1$\n50", "$A_2$\n80", "$A_3$\n30", "$A_4$\n0",
              "$A_5$\n0", "$A_6$\n0", "$A_7$\n−M", "$x_B$", "θ"]
    # ── tabla dada ──
    ax.text(0.2, 10.3, "a)  Tabla que da el parcial (base A4, A6, A2): NO es óptima",
            fontsize=11, weight="bold", color=PURPLE)
    rows = [
        ["0", "A4", "1/8", "0", "3/4", "1", "−15/4", "0", "0", "500", "666,7"],
        ["0", "A6", "5/8", "0", "1/4", "0", "5/4", "1", "−1", "1000", "4000"],
        ["80", "A2", "5/8", "1", "1/4", "0", "5/4", "0", "0", "1500", "6000"],
        ["", "$z_j$", "50", "80", "20", "0", "100", "0", "0", "Z = 120.000", ""],
        ["", "$c_j-z_j$", "0", "0", "+10", "0", "−100", "0", "−M", "", ""],
    ]
    col = {}
    for i in range(5):
        col[(i, 4)] = BLUE_L
    for j in range(11):
        col[(0, j)] = ORANGE_L
    col[(0, 4)] = "#fbbf24"
    col[(4, 4)] = BLUE_L
    tabla(ax, 0.3, 9.45, rows, header, cw, rh, col, bold_rows=(4,))
    ax.text(0.3, 6.85, "Entra $A_3$: es el único $c_j - z_j > 0$ (Max).    "
            "Sale $A_4$: menor θ = 500 ÷ 3/4 = 666,7.    Pivote = 3/4.",
            fontsize=9.6, color=INK)
    ax.text(0.3, 6.45, "Ojo: $c_1 - z_1 = 0$ con $A_1$ no básica, pero todavía no es el óptimo, "
            "así que eso no dice nada sobre alternativas.", fontsize=9.2, color=MUTED)
    # ── tabla óptima ──
    ax.text(0.2, 5.75, "b)  Tabla óptima (base A3, A6, A2): dónde se lee cada respuesta",
            fontsize=11, weight="bold", color=GREEN)
    header2 = header[:-1]
    cw2 = cw[:-1]
    rows2 = [
        ["30", "A3", "1/6", "0", "1", "4/3", "−5", "0", "0", "666,67"],
        ["0", "A6", "7/12", "0", "0", "−1/3", "5/2", "1", "−1", "833,33"],
        ["80", "A2", "7/12", "1", "0", "−1/3", "5/2", "0", "0", "1333,33"],
        ["", "$z_j$", "51,67", "80", "30", "40/3", "50", "0", "0", "Z* = 126.666,67"],
        ["", "$c_j-z_j$", "−5/3", "0", "0", "−40/3", "−50", "0", "−M", ""],
    ]
    col2 = {}
    for i in range(3):
        for j in (5, 6, 8):
            col2[(i, j)] = BLUE_L
        col2[(i, 9)] = GREEN_L
    col2[(4, 5)] = ORANGE_L
    col2[(4, 6)] = ORANGE_L
    col2[(4, 2)] = PURPLE_L
    tabla(ax, 0.3, 4.95, rows2, header2, cw2, rh, col2, bold_rows=(4,))
    # anotaciones
    yb = 4.95 - 5 * rh - 0.85
    notes = [
        (BLUE, BLUE_L, "$B^{-1}$: columnas de la base inicial (A4, A5, A7)"),
        (GREEN, GREEN_L, "$x_B = B^{-1}b$: valores de las básicas"),
        (ORANGE, ORANGE_L, "−($c_j - z_j$) de las holguras = precios sombra: $u_1 = 40/3$, $u_2 = 50$"),
        (PURPLE, PURPLE_L, "$c_1 - z_1 = -5/3$: costo reducido de la nafta"),
    ]
    for k, (c, cl, t) in enumerate(notes):
        y = yb - k * 0.48
        ax.add_patch(Rectangle((0.35, y - 0.15), 0.35, 0.3, fc=cl, ec=c, lw=1.2))
        ax.text(0.85, y, t, fontsize=9.6, va="center", color=INK)
    ax.text(0.35, yb - 4 * 0.48 - 0.1,
            "S* = (0; 1333,33; 666,67; 0; 0; 833,33)ᵀ  ·  Z* = 126.666,67 USD.  "
            "Única: todos los $c_j - z_j$ de las no básicas son < 0.",
            fontsize=9.6, weight="bold")
    save(fig, "r-parcial-ej2-tablas.png")


# ═════════════════════════════════════════════════════════════════════════
# 5. Rangos de sensibilidad del ejercicio 2
# ═════════════════════════════════════════════════════════════════════════
def fig_rangos():
    fig, axs = plt.subplots(6, 1, figsize=(7.6, 6.4))
    data = [
        ("$c_1$ (nafta, no básica)", None, 50 + 5 / 3, 50, 30, 60, PURPLE,
         "c₁ ≤ 51,67\n(si gana más, la nafta entra)"),
        ("$c_2$ (diésel, básica)", 80 - 20 / 7, 120, 80, 60, 130, BLUE,
         "77,14 ≤ c₂ ≤ 120"),
        ("$c_3$ (fueloil, básica)", 20, 40, 30, 10, 50, BLUE, "20 ≤ c₃ ≤ 40"),
        ("$b_1$ (materia prima)", 4500, 7500, 5000, 4000, 8000, GREEN,
         "4.500 ≤ b₁ ≤ 7.500\n(cada t vale u₁ = 13,33)"),
        ("$b_2$ (destilación)", 866.67, 1333.33, 1200, 700, 1500, GREEN,
         "866,67 ≤ b₂ ≤ 1.333,33\n(cada unidad vale u₂ = 50)"),
        ("$b_3$ (mínimo de diésel)", None, 1333.33, 500, 0, 1500, GREEN,
         "b₃ ≤ 1.333,33\n(sobran 833,33 t: u₃ = 0)"),
    ]
    for ax, (name, lo, hi, cur, xmin, xmax, c, txt) in zip(axs, data):
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(-1, 1)
        ax.axhline(0, color=GRID, lw=2)
        a = lo if lo is not None else xmin
        ax.plot([a, hi], [0, 0], color=c, lw=7, solid_capstyle="butt", alpha=0.85)
        if lo is not None:
            ax.plot(lo, 0, "|", color=c, ms=18, mew=2)
            ax.text(lo, -0.95, coma(lo, 2).rstrip("0").rstrip(","), ha="center", fontsize=9.5, color=c)
        else:
            ax.text(xmin, -0.95, "−∞", ha="left", fontsize=9.5, color=c)
        ax.plot(hi, 0, "|", color=c, ms=18, mew=2)
        ax.text(hi, -0.95, coma(hi, 2).rstrip("0").rstrip(","), ha="center", fontsize=9.5, color=c)
        ax.plot(cur, 0, "o", color=INK, ms=7, zorder=5)
        ax.text(cur, 0.5, f"actual {coma(cur, 0)}", ha="center", fontsize=9.3)
        ax.set_yticks([])
        ax.set_xticks([])
        for s in ("left", "bottom"):
            ax.spines[s].set_visible(False)
        ax.text(xmin - (xmax - xmin) * 0.02, 0, name, ha="right", va="center",
                fontsize=10, weight="bold")
        ax.text(xmax + (xmax - xmin) * 0.03, 0, txt, ha="left", va="center",
                fontsize=9.5, color=MUTED, wrap=False)
    fig.suptitle("Rangos en los que la base óptima no cambia (parcial 2026, ejercicio 2)",
                 fontsize=11, weight="bold", x=0.5, y=0.995)
    fig.subplots_adjust(left=0.27, right=0.68, hspace=0.45)
    save(fig, "r-rangos-sensibilidad.png")


# ═════════════════════════════════════════════════════════════════════════
# 6. Pares primal–dual (holguras complementarias)
# ═════════════════════════════════════════════════════════════════════════
def fig_pares():
    fig, ax = canvas(11, 5.8)
    ax.text(2.6, 5.45, "PRIMAL (Max Z)", ha="center", fontsize=11, weight="bold", color=BLUE)
    ax.text(8.4, 5.45, "DUAL (Min W)", ha="center", fontsize=11, weight="bold", color=ORANGE)
    pares = [
        ("x₁ nafta = 0", "holgura dual 1 = 5/3  (costo reducido)", False),
        ("x₂ diésel = 1333,33", "holgura dual 2 = 0", True),
        ("x₃ fueloil = 666,67", "holgura dual 3 = 0", True),
        ("x₄ holgura ① = 0", "u₁ = 40/3 ≈ 13,33", False),
        ("x₅ holgura ② = 0", "u₂ = 50", False),
        ("x₆ exceso ③ = 833,33", "u₃ = 0", True),
    ]
    for k, (p, d, pnz) in enumerate(pares):
        y = 4.75 - k * 0.78
        box(ax, 2.6, y, 3.6, 0.55, p, fc=BLUE_L if pnz else GRAY_L,
            ec=BLUE if pnz else MUTED, weight="bold" if pnz else "normal")
        box(ax, 8.4, y, 3.9, 0.55, d, fc=GRAY_L if pnz else ORANGE_L,
            ec=MUTED if pnz else ORANGE, weight="normal" if pnz else "bold")
        arrow(ax, (4.45, y), (6.4, y), style="<|-|>", color=GREEN, lw=1.4)
        ax.text(5.42, y + 0.12, "producto = 0", ha="center", fontsize=8.2, color=GREEN)
    ax.text(5.5, 0.12, "En cada par, al menos uno vale cero. Si sobra recurso (x₆ > 0), su precio "
            "sombra es 0; si se produce (x₂, x₃ > 0), su restricción dual se cumple con igualdad.",
            ha="center", fontsize=9.2, color=INK)
    save(fig, "r-pares-primal-dual.png")


# ═════════════════════════════════════════════════════════════════════════
# 7. Stock: modelo básico (diente de sierra)
# ═════════════════════════════════════════════════════════════════════════
def fig_stock_basico():
    fig, ax = plt.subplots(figsize=(9.5, 4.2))
    Q, T, LT = 100, 4.0, 1.4
    PP = Q * LT / T
    t = []
    q = []
    for k in range(3):
        t += [k * T, (k + 1) * T]
        q += [Q, 0]
    ax.plot(t, q, color=BLUE, lw=2.2)
    for k in range(1, 3):
        ax.plot([k * T, k * T], [0, Q], color=BLUE, lw=2.2)
    ax.plot([0, 3 * T], [PP, PP], color=ORANGE, ls="--", lw=1.4)
    ax.text(3 * T + 0.15, PP, "PP = D·LT", color=ORANGE, va="center", fontsize=9.5, weight="bold")
    for k in range(3):
        te = (k + 1) * T - LT
        ax.plot(te, PP, "o", color=ORANGE, ms=6, zorder=5)
    te = 2 * T - LT
    ax.annotate("", (te, -12), (2 * T, -12), arrowprops=dict(arrowstyle="<|-|>", color=PURPLE))
    ax.text(te + LT / 2, -21, "LT", color=PURPLE, ha="center", fontsize=9.5, weight="bold")
    ax.annotate("se emite el pedido\n(el stock tocó PP)", (te, PP), (5.3, 14), fontsize=8.6,
                color=ORANGE, ha="center", arrowprops=dict(arrowstyle="-|>", color=ORANGE))
    ax.annotate("", (0, 112), (T, 112), arrowprops=dict(arrowstyle="<|-|>", color=INK))
    ax.text(T / 2, 116, "T* = Q*/D", ha="center", fontsize=9.5)
    ax.annotate("", (-0.35, 0), (-0.35, Q), arrowprops=dict(arrowstyle="<|-|>", color=INK))
    ax.text(-0.5, Q / 2, "Q", ha="right", va="center", fontsize=10, weight="bold")
    ax.plot([0, 3 * T], [Q / 2, Q / 2], color=GREEN, ls=":", lw=1.4)
    ax.text(3 * T + 0.15, Q / 2, "stock medio = Q/2", color=GREEN, va="center", fontsize=9.5)
    ax.text(T * 0.55, 62, "pendiente −D", color=BLUE, fontsize=9, rotation=-34)
    ax.set_xlim(-1.0, 3 * T + 2.6)
    ax.set_ylim(-26, 125)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("tiempo")
    ax.set_ylabel("q(t)", rotation=0, labelpad=14)
    ax.set_title("Modelo básico: el lote entra de golpe y se consume a ritmo constante D")
    save(fig, "r-stock-basico.png")


# ═════════════════════════════════════════════════════════════════════════
# 8. Stock: curva de costo (con los datos del artículo A del parcial)
# ═════════════════════════════════════════════════════════════════════════
def fig_stock_costo():
    C, L, i, D = 50, 150, 0.20, 12000
    Q = np.linspace(150, 1500, 400)
    ped = L / Q
    man = C * i * Q / (2 * D)
    fig, ax = plt.subplots(figsize=(9.0, 4.6))
    ax.plot(Q, ped, color=ORANGE, lw=2, label="pedir: L/Q  (baja con Q)")
    ax.plot(Q, man, color=PURPLE, lw=2, label="mantener: C·i·Q/(2D)  (sube con Q)")
    ax.plot(Q, ped + man, color=BLUE, lw=2.8, label="CT(Q) − C  (la suma)")
    qs = math.sqrt(2 * D * L / (C * i))
    ax.axvline(qs, color=GREEN, ls="--", lw=1.3)
    ax.plot(qs, L / qs + C * i * qs / (2 * D), "o", color=GREEN, ms=8, zorder=5)
    ax.text(qs + 20, 0.95, f"Q* = √(2DL/(C·i)) = {qs:.0f}\nlas dos curvas se cruzan:\n"
            "pedir = mantener = 0,25 $/u", color=GREEN, fontsize=9.2, va="top")
    ax.set_xlabel("Q (unidades por pedido)")
    ax.set_ylabel("$ por unidad")
    ax.set_ylim(0, 1.05)
    ax.grid(color=GRID, lw=0.6)
    ax.legend(frameon=False, loc="upper right", fontsize=9)
    ax.set_title("Costo por unidad: CT(Q) = C + L/Q + C·i·Q/(2D)   (artículo A del parcial: C = 50, L = 150, i = 20 %, D = 12.000)",
                 fontsize=10)
    ax.text(1000, 0.3, "C = 50 $/u es constante: sólo sube toda la curva,\nno mueve el mínimo. CT(Q*) = 50,50 $/u",
            fontsize=8.8, color=MUTED)
    save(fig, "r-stock-costo.png")


# ═════════════════════════════════════════════════════════════════════════
# 9. Stock: consumo durante el ingreso
# ═════════════════════════════════════════════════════════════════════════
def fig_stock_ingreso():
    fig, ax = plt.subplots(figsize=(9.5, 4.2))
    V, D, Q = 3.0, 1.0, 9.0
    th = Q / V
    T = Q / D
    M = Q * (1 - D / V)
    for k in range(2):
        t0 = k * T
        ax.plot([t0, t0 + th, t0 + T], [0, M, 0], color=BLUE, lw=2.4)
    ax.plot([0, th], [0, Q], color=MUTED, ls=":", lw=1.3)
    ax.text(th - 0.1, Q + 0.2, "si no se consumiera,\nllegaría a Q", fontsize=8.5,
            color=MUTED, ha="right")
    ax.plot([0, T + th], [M, M], color=ORANGE, ls="--", lw=1.2)
    ax.text(th + 0.25, M + 0.35, "M = Q(1 − D/V)", ha="left", va="bottom", color=ORANGE,
            fontsize=9.5, weight="bold")
    ax.annotate("", (0, -0.8), (th, -0.8), arrowprops=dict(arrowstyle="<|-|>", color=PURPLE))
    ax.text(th / 2, -1.5, "θ = Q/V", ha="center", color=PURPLE, fontsize=9.5, weight="bold")
    ax.annotate("", (0, -2.4), (T, -2.4), arrowprops=dict(arrowstyle="<|-|>", color=INK))
    ax.text(T / 2, -3.1, "T = Q/D", ha="center", fontsize=9.5)
    ax.text(th * 0.72, M * 0.22, "sube con\npendiente V − D", color=BLUE, fontsize=9, ha="left")
    ax.text(th + (T - th) * 0.55, M * 0.6, "baja con pendiente −D", color=BLUE, fontsize=9)
    ax.set_xlim(-2.6, 2 * T + 0.5)
    ax.set_ylim(-3.6, Q + 1.6)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("tiempo")
    ax.set_ylabel("q(t)", rotation=0, labelpad=14)
    ax.set_title("Consumo durante el ingreso: el pico es M < Q, por eso conviene un lote más grande")
    save(fig, "r-stock-ingreso.png")


# ═════════════════════════════════════════════════════════════════════════
# 10. Stock: descuentos (escalón y excedente)
# ═════════════════════════════════════════════════════════════════════════
def fig_stock_descuentos():
    D, L, i, a = 1000, 50, 0.24, 400
    C1, C2 = 10.0, 9.5
    Q = np.linspace(50, 1200, 500)
    fig, axs = plt.subplots(1, 2, figsize=(11.6, 4.3))
    ax = axs[0]
    m1 = Q < a
    ct1 = C1 + L / Q + C1 * i * Q / (2 * D)
    ct2 = C2 + L / Q + C2 * i * Q / (2 * D)
    ax.plot(Q[m1], ct1[m1], color=ORANGE, lw=2.3, label="CT₁ (precio C₁, Q < a)")
    ax.plot(Q[~m1], ct2[~m1], color=BLUE, lw=2.3, label="CT₂ (precio C₂, Q ≥ a)")
    ax.plot(Q[~m1], ct1[~m1], color=ORANGE, lw=1, ls=":")
    ax.plot(Q[m1], ct2[m1], color=BLUE, lw=1, ls=":")
    q1 = math.sqrt(2 * D * L / (C1 * i))
    q2 = math.sqrt(2 * D * L / (C2 * i))
    ax.plot(q1, C1 + L / q1 + C1 * i * q1 / (2 * D), "o", color=ORANGE, ms=7)
    ax.text(q1, 10.58, f"Q₁* = {q1:.0f}\nCT₁ = {coma(C1 + L / q1 + C1 * i * q1 / (2 * D), 2)}", color=ORANGE, ha="center", fontsize=8.8)
    ax.plot(q2, C2 + L / q2 + C2 * i * q2 / (2 * D), "x", color=MUTED, ms=8, mew=2)
    ax.text(q2, 9.8, f"Q₂* = {q2:.0f} < a:\nno se puede", color=MUTED, ha="center", fontsize=8.3)
    ca = C2 + L / a + C2 * i * a / (2 * D)
    ax.plot(a, ca, "o", color=BLUE, ms=8, zorder=6)
    ax.annotate(f"candidato a = {a}\nCT₂(a) = {coma(ca, 2)}: conviene", (a, ca), (620, 9.78), fontsize=8.8,
                color=BLUE, arrowprops=dict(arrowstyle="-|>", color=BLUE))
    ax.axvline(a, color=GRID, lw=1)
    ax.set_title("Escalón: el precio menor vale para TODO el lote")
    ax.set_xlabel("Q")
    ax.set_ylabel("CT(Q) [$/u]")
    ax.set_ylim(9.6, 11.0)
    ax.grid(color=GRID, lw=0.6)
    ax.legend(frameon=False, fontsize=8.6, loc="upper right")
    ax.text(60, 9.64, "se comparan los CT de los candidatos, no los precios", fontsize=8.4, color=MUTED)

    ax = axs[1]
    Qe = np.linspace(1, 3000, 600)
    cq = np.where(Qe <= a, C1, C2 + (C1 - C2) * a / Qe)
    ax.plot(Qe, cq, color=BLUE, lw=2.4)
    ax.axhline(C2, color=GREEN, ls="--", lw=1.2)
    ax.text(2950, C2 + 0.015, "C₂: el límite, que nunca se alcanza", color=GREEN, ha="right",
            fontsize=8.8)
    ax.axvline(a, color=GRID, lw=1)
    ax.text(a - 40, 9.94, "a", fontsize=10, weight="bold", ha="right")
    ax.text(1100, 9.78, "C(Q) = C₂ + (C₁ − C₂)·a / Q", fontsize=9.5, color=BLUE)
    ax.set_title("Excedente: sólo lo que pasa de a se paga a C₂")
    ax.set_xlabel("Q")
    ax.set_ylabel("precio medio C(Q) [$/u]")
    ax.set_ylim(9.4, 10.1)
    ax.grid(color=GRID, lw=0.6)
    fig.tight_layout(w_pad=2.5)
    save(fig, "r-stock-descuentos.png")


# ═════════════════════════════════════════════════════════════════════════
# 11. Stock: Lagrange con restricción de capital (parcial, ejercicio 3)
# ═════════════════════════════════════════════════════════════════════════
def fig_stock_lagrange():
    DA, DB, LA, LB, CA, CB, i = 12000, 8000, 150, 200, 50, 80, 0.20
    qa = lambda l: np.sqrt(2 * DA * LA / (CA * (i + l)))
    qb = lambda l: np.sqrt(2 * DB * LB / (CB * (i + l)))
    inv = lambda l: CA * qa(l) / 2 + CB * qb(l) / 2
    lam = np.linspace(0, 0.4, 400)
    fig, axs = plt.subplots(1, 2, figsize=(11.6, 4.4))
    ax = axs[0]
    ax.plot(lam, inv(lam), color=BLUE, lw=2.4)
    ax.plot(0, inv(0), "o", color=INK, ms=7)
    ax.text(0.008, inv(0) + 300, f"λ = 0: I = {coma(inv(0), 0)} (lotes sin restricción)",
            fontsize=8.8)
    for I0, c in ((23000, GREEN), (28000, ORANGE)):
        lo, hi = 0.0, 2.0
        for _ in range(80):
            mid = (lo + hi) / 2
            lo, hi = (mid, hi) if inv(mid) > I0 else (lo, mid)
        ax.axhline(I0, color=c, ls="--", lw=1.2)
        ax.plot(lo, I0, "o", color=c, ms=8, zorder=6)
        ax.text(lo + 0.008, I0 + 350, f"I₀ = {coma(I0, 0)} → λ ≈ {coma(lo, 3)}", color=c,
                fontsize=9, weight="bold")
    ax.set_xlabel("λ")
    ax.set_ylabel(r"inversión media $I = \sum C_j Q_j / 2$")
    ax.set_title("Se sube λ hasta que I = I₀")
    ax.grid(color=GRID, lw=0.6)
    ax.set_ylim(19000, 34500)
    ax = axs[1]
    ax.plot(lam, qa(lam), color=PURPLE, lw=2.2, label=r"$Q_A$ (tornillos)")
    ax.plot(lam, qb(lam), color=BLUE, lw=2.2, label=r"$Q_B$ (tuercas)")
    for l, c in ((0.2089, GREEN), (0.0759, ORANGE)):
        ax.axvline(l, color=c, ls="--", lw=1.1)
        ax.plot(l, qa(l), "o", color=c, ms=6)
        ax.plot(l, qb(l), "o", color=c, ms=6)
    ax.text(0.212, qb(0.2089) - 32, f"$Q_B$ ≈ {qb(0.2089):.0f}", color=GREEN, fontsize=8.8)
    ax.text(0.212, qa(0.2089) + 10, f"$Q_A$ ≈ {qa(0.2089):.0f}", color=GREEN, fontsize=8.8)
    ax.text(0.079, qb(0.0759) + 12, f"$Q_B$ ≈ {qb(0.0759):.0f}", color=ORANGE, fontsize=8.8)
    ax.text(0.079, qa(0.0759) + 12, f"$Q_A$ ≈ {qa(0.0759):.0f}", color=ORANGE, fontsize=8.8)
    ax.set_xlabel("λ")
    ax.set_ylabel("lote")
    ax.set_title(r"$Q_j = \sqrt{2D_jL_j\,/\,(C_j(i + \lambda))}$: todos se achican juntos")
    ax.grid(color=GRID, lw=0.6)
    ax.legend(frameon=False, fontsize=9)
    fig.tight_layout(w_pad=2.5)
    save(fig, "r-stock-lagrange.png")


# ═════════════════════════════════════════════════════════════════════════
# 12. Stock: demanda aleatoria (SS, PP, RF)
# ═════════════════════════════════════════════════════════════════════════
def fig_stock_ss():
    fig, axs = plt.subplots(1, 2, figsize=(11.6, 4.3), gridspec_kw={"width_ratios": [1.5, 1]})
    ax = axs[0]
    SS, Q = 25, 100
    rng = np.random.default_rng(7)
    PP = 60
    t, q = [0.0], [SS + Q]
    level, time = SS + Q, 0.0
    pend = None
    for _ in range(330):
        time += 0.03
        level -= rng.uniform(0.0, 1.8)
        if pend is None and level <= PP:
            pend = time + 1.2
            ax.plot(time, level, "o", color=ORANGE, ms=5, zorder=5)
        if pend is not None and time >= pend:
            t.append(time)
            q.append(level)
            level += Q
            pend = None
        t.append(time)
        q.append(level)
    ax.plot(t, q, color=BLUE, lw=1.6)
    ax.plot([0, t[-1]], [SS, SS], color=RED, ls="--", lw=1.3)
    ax.fill_between([0, t[-1]], 0, SS, color=RED_L, alpha=0.6)
    ax.text(t[-1] + 0.15, SS, r"$SS = z\,\sigma_{LT}$", color=RED, fontsize=10, va="center")
    ax.plot([0, t[-1]], [PP, PP], color=ORANGE, ls="--", lw=1.3)
    ax.text(t[-1] + 0.15, PP, r"$PP = \bar d\cdot LT + SS$", color=ORANGE, fontsize=10, va="center")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("tiempo")
    ax.set_ylabel("q(t)", rotation=0, labelpad=14)
    ax.set_xlim(0, t[-1] + 3.4)
    ax.set_ylim(0, SS + Q + 15)
    ax.set_title("La demanda varía: el SS absorbe los picos durante el LT")
    ax = axs[1]
    x = np.linspace(-3.5, 3.5, 400)
    f = np.exp(-x ** 2 / 2) / math.sqrt(2 * math.pi)
    ax.plot(x, f, color=INK, lw=2)
    z = 1.645
    m = x >= z
    ax.fill_between(x[m], f[m], color=RED, alpha=0.45)
    ax.axvline(0, color=MUTED, ls=":")
    ax.axvline(z, color=ORANGE, lw=1.6)
    ax.text(-0.1, 0.415, r"$\mu = \bar d\cdot LT$", ha="right", fontsize=9.5)
    ax.set_ylim(0, 0.47)
    ax.text(z + 0.08, 0.3, "PP", color=ORANGE, fontsize=10, weight="bold")
    ax.annotate("RF = P(demanda en LT > PP)\n(5 % → z = 1,645)", (2.1, 0.02), (2.05, 0.2),
                fontsize=8.8, color=RED, arrowprops=dict(arrowstyle="-|>", color=RED))
    ax.annotate("", (0, 0.36), (z, 0.36), arrowprops=dict(arrowstyle="<|-|>", color=GREEN))
    ax.text(z / 2, 0.375, "SS = z·σ", ha="center", color=GREEN, fontsize=9, weight="bold")
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_xlabel("demanda durante el LT")
    ax.set_title("Riesgo de faltante = cola de la normal")
    fig.tight_layout(w_pad=2.5)
    save(fig, "r-stock-aleatorio.png")


# ═════════════════════════════════════════════════════════════════════════
# 13. Stock: punto de pedido vs revisión periódica
# ═════════════════════════════════════════════════════════════════════════
def fig_stock_sistemas():
    fig, axs = plt.subplots(1, 2, figsize=(11.6, 3.9), sharey=True)
    rng = np.random.default_rng(3)
    rates = rng.uniform(0.6, 1.6, 400)
    # punto de pedido: Q fijo
    ax = axs[0]
    Q, PP, LT = 60, 30, 8
    lvl, t, ts, qs, pend = 80.0, 0, [0], [80.0], None
    orders = []
    for k in range(120):
        t += 1
        lvl -= rates[k]
        if pend is None and lvl <= PP:
            pend = t + LT
            orders.append(t)
        if pend is not None and t >= pend:
            ts.append(t)
            qs.append(lvl)
            lvl += Q
            pend = None
        ts.append(t)
        qs.append(lvl)
    ax.plot(ts, qs, color=BLUE, lw=1.8)
    ax.plot([0, 120], [PP, PP], color=ORANGE, ls="--", lw=1.2)
    ax.text(122, PP, "PP", color=ORANGE, va="center", weight="bold")
    ax.set_xlim(-2, 130)
    for o in orders:
        ax.axvline(o, color=ORANGE, lw=0.8, alpha=0.6)
    ax.set_title("Punto de pedido: cantidad fija Q*, momento variable")
    ax.text(3, 5, "lo activa la DEMANDA · registro permanente · SS cubre LT",
            fontsize=8.8, color=MUTED)
    # revisión periódica: T fijo
    ax = axs[1]
    T, LT, S = 30, 8, 85
    lvl, ts, qs, pend = 80.0, [0], [80.0], None
    for k in range(120):
        t = k + 1
        lvl -= rates[k + 150]
        if t % T == 0:
            pend = (t + LT, S - lvl)
            ax.axvline(t, color=PURPLE, lw=0.9, alpha=0.7)
        if pend is not None and t >= pend[0]:
            ts.append(t)
            qs.append(lvl)
            lvl += pend[1]
            pend = None
        ts.append(t)
        qs.append(lvl)
    ax.plot(ts, qs, color=BLUE, lw=1.8)
    ax.set_title("Revisión periódica: momento fijo cada T, cantidad variable")
    ax.text(3, 5, "lo activa el TIEMPO · se cuenta al revisar · SS cubre T + LT",
            fontsize=8.8, color=MUTED)
    for a in axs:
        a.set_xticks([])
        a.set_yticks([])
        a.set_xlabel("tiempo")
    axs[0].set_ylabel("q(t)", rotation=0, labelpad=14)
    fig.tight_layout(w_pad=2.0)
    save(fig, "r-stock-sistemas.png")


# ═════════════════════════════════════════════════════════════════════════
# 14. Transporte y transbordo
# ═════════════════════════════════════════════════════════════════════════
def nodo(ax, x, y, t, fc, ec, r=0.38, size=9.5, color=INK, ls="-"):
    c = plt.Circle((x, y), r, fc=fc, ec=ec, lw=1.6, ls=ls, zorder=4)
    ax.add_patch(c)
    ax.text(x, y, t, ha="center", va="center", fontsize=size, weight="bold", color=color, zorder=5)


def fig_transporte():
    fig, axs = plt.subplots(1, 2, figsize=(12, 5.0))
    ax = axs[0]
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 5.4)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Transporte desbalanceado (oferta 900 > demanda 800)")
    fu = [("A", 300), ("B", 400), ("C", 200)]
    de = [("1", 500, False), ("2", 300, False), ("F", 100, True)]
    for k, (n, a) in enumerate(fu):
        y = 4.3 - k * 1.5
        nodo(ax, 1.2, y, n, BLUE_L, BLUE)
        ax.text(0.55, y, f"a = {a}", ha="right", va="center", fontsize=9)
        for m, (d, b, fict) in enumerate(de):
            yd = 4.3 - m * 1.5
            ax.plot([1.58, 4.42], [y, yd], color=MUTED if not fict else ORANGE,
                    ls="-" if not fict else "--", lw=1.0, zorder=2)
    for m, (d, b, fict) in enumerate(de):
        y = 4.3 - m * 1.5
        nodo(ax, 4.8, y, d, ORANGE_L if fict else GREEN_L, ORANGE if fict else GREEN,
             ls="--" if fict else "-")
        ax.text(5.35, y, f"b = {b}", va="center", fontsize=9)
    ax.text(3.0, 0.15, "Destino ficticio F con costo 0: lo que \"recibe\" es\ncapacidad ociosa de cada cantera",
            ha="center", fontsize=8.8, color=ORANGE)
    ax = axs[1]
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 5.4)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Transbordo (ejemplo del apunte, W* = 1210)")
    pos = {1: (0.8, 3.9), 2: (0.8, 1.6), 3: (3.4, 3.9), 4: (3.4, 1.6), 5: (6.0, 4.4),
           6: (6.0, 2.75), 7: (6.0, 1.1)}
    arcs = {(1, 3): 10, (1, 4): 5, (2, 3): 8, (2, 4): 7, (3, 4): 4, (4, 3): 4, (3, 5): 3,
            (3, 6): 7, (3, 7): 1, (4, 5): 2, (4, 6): 1, (4, 7): 6}
    used = {(1, 4), (2, 3), (2, 4), (3, 7), (4, 5), (4, 6)}
    for (a, b), c in arcs.items():
        rad = 0.25 if (a, b) in ((3, 4), (4, 3)) else 0.0
        arrow(ax, pos[a], pos[b], color=GREEN if (a, b) in used else "#c7cbd1",
              lw=2.2 if (a, b) in used else 1.0, rad=rad, shrinkA=13, shrinkB=13)
    for n, (x, y) in pos.items():
        if n <= 2:
            nodo(ax, x, y, str(n), BLUE_L, BLUE)
        elif n <= 4:
            nodo(ax, x, y, str(n), PURPLE_L, PURPLE)
        else:
            nodo(ax, x, y, str(n), GREEN_L, GREEN)
    ax.text(0.8, 4.55, "oferta 50", ha="center", fontsize=8.6)
    ax.text(0.8, 0.95, "oferta 100", ha="center", fontsize=8.6)
    ax.text(3.4, 4.55, "depósito", ha="center", fontsize=8.6, color=PURPLE)
    ax.text(3.4, 0.95, "depósito", ha="center", fontsize=8.6, color=PURPLE)
    for n, d in ((5, 20), (6, 40), (7, 90)):
        ax.text(6.45, pos[n][1], f"dem. {d}", va="center", fontsize=8.6)
    ax.text(3.4, 0.15, "Depósito 3:  x₁₃ + x₂₃ + x₄₃ − x₃₄ − x₃₅ − x₃₆ − x₃₇ = 0\n(lo que entra = lo que sale)",
            ha="center", fontsize=8.8, color=PURPLE)
    fig.tight_layout(w_pad=2)
    save(fig, "r-transporte.png")


# ═════════════════════════════════════════════════════════════════════════
# 15. Programación entera: ramificación y poda (ejemplo del apunte)
# ═════════════════════════════════════════════════════════════════════════
def fig_bb():
    fig, axs = plt.subplots(1, 2, figsize=(12, 5.2), gridspec_kw={"width_ratios": [1, 1.25]})
    ax = axs[0]
    X, Y = 7, 5
    ejes(ax, X, Y)
    cons = [(-1, 3, "<=", 6), (7, 1, "<=", 35)]
    ax.add_patch(Polygon(region(cons, X, Y), fc=BLUE_L, ec="none", zorder=1))
    recta(ax, -1, 3, 6, X, Y, color=INK, label="−x₁ + 3x₂ ≤ 6", lpos=(1.6, 3.2))
    recta(ax, 7, 1, 35, X, Y, color=INK, label="7x₁ + x₂ ≤ 35", lpos=(5.75, 1.9))
    for x in range(X + 1):
        for y in range(Y + 1):
            if -x + 3 * y <= 6 and 7 * x + y <= 35:
                ax.plot(x, y, "o", color=MUTED, ms=4, zorder=5)
    ax.axvspan(4, 5, color=RED_L, alpha=0.7, zorder=1)
    ax.text(4.5, 4.6, "franja\neliminada", ha="center", fontsize=8.3, color=RED)
    ax.plot(4.5, 3.5, "*", color=ORANGE, ms=15, zorder=7)
    ax.text(3.0, 4.2, "relajado (4,5; 3,5)\nz = 63", color=ORANGE, fontsize=8.8)
    ax.plot(4, 3, "o", color=GREEN, ms=10, zorder=7)
    ax.text(2.5, 2.4, "entero (4; 3)\nz* = 55", color=GREEN, fontsize=8.8, weight="bold")
    ax.set_title("Max z = 7x₁ + 9x₂, x enteras")
    ax.set_aspect("equal")
    ax = axs[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.2)
    ax.axis("off")
    ax.set_title("Árbol de ramificación y poda")
    N = {
        "P0": (5, 5.4, "P0  relajado\nx = (4,5; 3,5)  z = 63", BLUE_L, BLUE),
        "A": (2.6, 3.6, "A: x₁ ≤ 4\nx = (4; 3,33)  z = 58", BLUE_L, BLUE),
        "B": (7.6, 3.6, "B: x₁ ≥ 5\nx = (5; 0)  z = 35\nentera → cota 35", GREEN_L, GREEN),
        "C": (1.55, 1.5, "C: x₂ ≤ 3\nx = (4; 3)  z = 55\nentera → cota 55", GREEN_L, GREEN),
        "D": (4.55, 1.5, "D: x₂ ≥ 4\nno factible\n→ se poda", RED_L, RED),
    }
    for a, b in (("P0", "A"), ("P0", "B"), ("A", "C"), ("A", "D")):
        arrow(ax, (N[a][0], N[a][1] - 0.45), (N[b][0], N[b][1] + 0.5))
    for k, (x, y, t, fc, ec) in N.items():
        box(ax, x, y, 2.75, 0.95 if k in ("P0", "A") else 1.15, t, fc=fc, ec=ec, size=8.8)
    ax.text(6.55, 1.5, "Se poda un nodo si:\n• es no factible\n• ya es entero\n• su z no supera la cota",
            fontsize=9, va="center",
            bbox=dict(fc=GRAY_L, ec=MUTED, boxstyle="round,pad=0.45"))
    ax.text(5, 0.15, "Óptimo entero: x = (4; 3), z* = 55. El relajado (63) es cota superior en Max.",
            ha="center", fontsize=9.2, weight="bold")
    fig.tight_layout(w_pad=2)
    save(fig, "r-entera-bb.png")


# ═════════════════════════════════════════════════════════════════════════
# 16. Redes (ejemplo propio): árbol mínimo, ruta más corta, flujo máximo
# ═════════════════════════════════════════════════════════════════════════
POS = {"O": (0.5, 2.0), "A": (2.2, 3.4), "B": (2.2, 0.6), "C": (4.2, 3.4),
       "D": (4.2, 0.6), "T": (5.9, 2.0)}
EDGES = {("O", "A"): 4, ("O", "B"): 3, ("A", "B"): 2, ("A", "C"): 5, ("B", "D"): 6,
         ("C", "D"): 1, ("A", "D"): 7, ("C", "T"): 3, ("D", "T"): 4}


def prim(nodes, edges):
    adj = {n: [] for n in nodes}
    for (a, b), w in edges.items():
        adj[a].append((w, a, b))
        adj[b].append((w, b, a))
    seen = {"O"}
    pq = list(adj["O"])
    heapq.heapify(pq)
    tree = []
    while pq and len(seen) < len(nodes):
        w, a, b = heapq.heappop(pq)
        if b in seen:
            continue
        seen.add(b)
        tree.append((a, b, w))
        for e in adj[b]:
            heapq.heappush(pq, e)
    return tree


def dijkstra(nodes, edges, s):
    adj = {n: [] for n in nodes}
    for (a, b), w in edges.items():
        adj[a].append((b, w))
        adj[b].append((a, w))
    dist = {n: math.inf for n in nodes}
    prev = {}
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev


CAP = {("O", "A"): 7, ("O", "B"): 6, ("A", "B"): 2, ("A", "C"): 5, ("B", "D"): 6,
       ("C", "D"): 2, ("A", "D"): 3, ("C", "T"): 4, ("D", "T"): 8}


def maxflow(cap, s, t):
    res = {}
    for (a, b), c in cap.items():
        res[(a, b)] = res.get((a, b), 0) + c
        res.setdefault((b, a), 0)
    total = 0
    while True:
        par = {s: None}
        dq = deque([s])
        while dq and t not in par:
            u = dq.popleft()
            for (a, b), c in res.items():
                if a == u and c > 0 and b not in par:
                    par[b] = a
                    dq.append(b)
        if t not in par:
            break
        path = []
        v = t
        while par[v] is not None:
            path.append((par[v], v))
            v = par[v]
        f = min(res[e] for e in path)
        for a, b in path:
            res[(a, b)] -= f
            res[(b, a)] += f
        total += f
    flow = {e: c - res[e] for e, c in cap.items()}
    return total, flow


def fig_redes():
    fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.6))
    nodes = list(POS)
    tree = prim(nodes, EDGES)
    tset = {frozenset((a, b)) for a, b, _ in tree}
    dist, prev = dijkstra(nodes, EDGES, "O")
    path = set()
    v = "T"
    while v != "O":
        path.add(frozenset((prev[v], v)))
        v = prev[v]
    total, flow = maxflow(CAP, "O", "T")

    def dibujar(ax, title, sel, color, etiqueta, dirigido=False, extra=None):
        ax.set_xlim(0, 6.4)
        ax.set_ylim(-0.25, 4.1)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title, fontsize=10.5)
        for (a, b) in EDGES:
            on = sel(a, b)
            (x1, y1), (x2, y2) = POS[a], POS[b]
            if dirigido:
                arrow(ax, POS[a], POS[b], color=color if on else "#c7cbd1",
                      lw=2.4 if on else 1.0, shrinkA=12, shrinkB=12)
            else:
                ax.plot([x1, x2], [y1, y2], color=color if on else "#c7cbd1",
                        lw=3 if on else 1.2, zorder=2)
            ax.text((x1 + x2) / 2, (y1 + y2) / 2, etiqueta(a, b), fontsize=8.6,
                    ha="center", va="center", zorder=6,
                    bbox=dict(fc="white", ec="none", pad=0.4))
        for n, (x, y) in POS.items():
            nodo(ax, x, y, n, GRAY_L, INK, r=0.3, size=9.5)
        if extra:
            extra(ax)

    dibujar(axs[0], f"Árbol de expansión mínima: {sum(w for *_, w in tree)}",
            lambda a, b: frozenset((a, b)) in tset, GREEN, lambda a, b: str(EDGES[(a, b)]))
    axs[0].text(3.2, -0.15, "5 arcos para 6 nodos (n − 1), sin ciclos", ha="center",
                fontsize=8.6, color=GREEN)

    def labels(ax):
        for n, (x, y) in POS.items():
            if n == "O":
                continue
            ax.text(x, y + 0.45, f"[{dist[n]}, {prev[n]}]", ha="center", fontsize=8.4,
                    color=BLUE, weight="bold")
    dibujar(axs[1], f"Ruta más corta O → T: {dist['T']}",
            lambda a, b: frozenset((a, b)) in path, BLUE, lambda a, b: str(EDGES[(a, b)]),
            extra=labels)
    axs[1].text(3.2, -0.15, "etiqueta permanente [distancia, nodo previo]", ha="center",
                fontsize=8.6, color=BLUE)
    dibujar(axs[2], f"Flujo máximo O → T: {total}",
            lambda a, b: flow[(a, b)] > 0, ORANGE,
            lambda a, b: f"{flow[(a, b)]}/{CAP[(a, b)]}", dirigido=True)
    axs[2].text(3.2, -0.15, "flujo/capacidad en cada arco", ha="center", fontsize=8.6,
                color=ORANGE)
    fig.tight_layout(w_pad=1.5)
    save(fig, "r-redes.png")
    return tree, dist, prev, total, flow


if __name__ == "__main__":
    print("Figuras del recuperatorio de IO →", OUT)
    fig_mapa()
    fig_tipos()
    fig_parcial_ej1()
    fig_simplex_flujo()
    fig_parcial_ej2()
    fig_rangos()
    fig_pares()
    fig_stock_basico()
    fig_stock_costo()
    fig_stock_ingreso()
    fig_stock_descuentos()
    fig_stock_lagrange()
    fig_stock_ss()
    fig_stock_sistemas()
    fig_transporte()
    fig_bb()
    tree, dist, prev, total, flow = fig_redes()
    print("  redes:", tree, dist, prev, total, flow)
