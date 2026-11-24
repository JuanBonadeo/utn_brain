#!/usr/bin/env python3
"""
cd-figs-final.py — Figuras del resumen para el final de Comunicación de Datos.

Genera en materias/CD/figs/ los PNG cd-*.png que usa el resumen del final.
Todos los datos salen de la wiki (materias/CD/CD.md) y del banco de ejercicios
de finales (materias/CD/estudio/final/). Sin azar: correrlo dos veces da lo mismo.

Uso (desde la raíz del repo):
    .venv/bin/python scripts/cd/cd-figs-final.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle
from matplotlib.ticker import FuncFormatter

OUT = Path(__file__).resolve().parents[2] / "materias" / "CD" / "figs"
OUT.mkdir(parents=True, exist_ok=True)

# ── estilo (mismo que scripts/sim/sim-figs-parcial1.py) ──────────────────
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
    "font.family": "Arial",
    "font.size": 10,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": INK,
    "axes.titlecolor": INK,
    "axes.titlesize": 10.5,
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
    """Número con coma decimal."""
    return f"{x:.{d}f}".replace(".", ",")


COMA_FMT = FuncFormatter(lambda v, _: f"{v:g}".replace(".", ","))


def save(fig, name):
    for a in fig.axes:
        if not a.axison:
            a.set_aspect("equal", adjustable="box")
    fig.savefig(OUT / name, facecolor="white")
    plt.close(fig)
    print("  ✓", name)


def canvas(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
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


def diamond(ax, x, y, w, h, text, fc="white", ec=INK, size=9.5):
    ax.add_patch(Polygon([[x, y + h / 2], [x + w / 2, y], [x, y - h / 2], [x - w / 2, y]],
                         fc=fc, ec=ec, lw=1.2))
    ax.text(x, y, text, ha="center", va="center", fontsize=size, linespacing=1.25)


def brace(ax, x0, x1, y, depth, color=INK, lw=1.3, down=True):
    """Llave horizontal entre x0 y x1; la punta mira hacia abajo (down) o arriba."""
    half = (x1 - x0) / 2
    b = 30.0
    xh = np.linspace(0, half, 200)
    yh = 1 / (1 + np.exp(-b * xh)) + 1 / (1 + np.exp(-b * (xh - half))) - 0.5
    xs = np.concatenate([x0 + xh, x0 + half + xh[1:]])
    ys = np.concatenate([yh, yh[-2::-1]])
    sgn = -1 if down else 1
    ax.plot(xs, y + sgn * depth * ys, color=color, lw=lw, solid_capstyle="round")


def dim(ax, x0, x1, y, text, color=INK, size=9.5, above=True, lw=1.1):
    """Cota horizontal con flechas en ambos extremos."""
    arrow(ax, (x0, y), (x1, y), style="<|-|>", color=color, lw=lw, ms=9, shrinkA=0, shrinkB=0)
    ax.text((x0 + x1) / 2, y + (0.07 if above else -0.07), text, ha="center",
            va="bottom" if above else "top", fontsize=size, color=color)


# ═════════════════════════════════════════════════════════════════════════
# 1. Sistema de comunicación (cadena de bloques)
# ═════════════════════════════════════════════════════════════════════════
def fig_sistema():
    fig, ax = canvas(8.6, 3.9)
    xs = [0.85, 2.5, 4.15, 5.8]
    yt, yb = 2.95, 0.95
    w, h = 1.45, 0.7
    top = [("Fuente", "Información", GRAY_L, MUTED),
           ("Codificador\nde fuente", "Codificación", GREEN_L, GREEN),
           ("Codificador\nde canal", "Errores", ORANGE_L, ORANGE),
           ("Modulador", "Modulación", BLUE_L, BLUE)]
    bot = [("Destino", "Información", GRAY_L, MUTED),
           ("Decodificador\nde fuente", "Codificación", GREEN_L, GREEN),
           ("Decodificador\nde canal", "Errores", ORANGE_L, ORANGE),
           ("Demodulador", "Modulación", BLUE_L, BLUE)]
    for x, (t, u, fc, ec) in zip(xs, top):
        box(ax, x, yt, w, h, t, fc=fc, ec=ec, size=9.3)
        ax.text(x, yt + h / 2 + 0.12, u, ha="center", va="bottom", fontsize=9, color=MUTED,
                style="italic")
    for x, (t, u, fc, ec) in zip(xs, bot):
        box(ax, x, yb, w, h, t, fc=fc, ec=ec, size=9.3)
        ax.text(x, yb - h / 2 - 0.12, u, ha="center", va="top", fontsize=9, color=MUTED,
                style="italic")
    for i in range(3):
        arrow(ax, (xs[i] + w / 2, yt), (xs[i + 1] - w / 2, yt), color=INK)
        arrow(ax, (xs[i + 1] - w / 2, yb), (xs[i] + w / 2, yb), color=INK)
    # canal
    cx, cy = 7.2, 1.95
    box(ax, cx, cy, 1.1, 0.75, "Canal", fc=PURPLE_L, ec=PURPLE, weight="bold", size=10)
    ax.text(cx - 0.65, cy, "Medios", ha="right", va="center", fontsize=9, color=MUTED,
            style="italic")
    arrow(ax, (xs[3] + w / 2, yt), (cx, cy + 0.38), color=INK, rad=-0.35)
    arrow(ax, (cx, cy - 0.38), (xs[3] + w / 2, yb), color=INK, rad=-0.35)
    # ruido
    ax.text(8.55, 2.95, "Ruido", ha="center", va="center", fontsize=10, color=RED, weight="bold")
    arrow(ax, (8.5, 2.75), (cx + 0.57, cy + 0.15), color=RED, lw=1.6)
    ax.text(8.55, 1.6, "actúa sobre\n$P(b_j/a_i)$", ha="center", va="top", fontsize=9,
            color=RED)
    ax.text(0.85, 1.95, "$a_i$ entra al canal  ·  $b_j$ sale del canal", ha="left",
            fontsize=9, color=MUTED)
    ax.set_xlim(0.0, 9.0)
    ax.set_ylim(0.2, 3.85)
    save(fig, "cd-sistema-comunicacion.png")


# ═════════════════════════════════════════════════════════════════════════
# 2. Canal binario simétrico (final típico: P(a1) = 0,65, P(b1/a1) = 0,75)
# ═════════════════════════════════════════════════════════════════════════
def fig_canal_binario():
    fig, ax = canvas(7.8, 3.6)
    xa, xb = 1.6, 4.6
    y1, y2 = 2.85, 0.75
    r = 0.32
    for y, t, p in [(y1, "$a_1$", "0,65"), (y2, "$a_2$", "0,35")]:
        ax.add_patch(Circle((xa, y), r, fc=BLUE_L, ec=BLUE, lw=1.5))
        ax.text(xa, y, t, ha="center", va="center", fontsize=12)
        ax.text(xa - r - 0.12, y, f"$P(a)$ = {p}".replace("$P(a)$", "P(" + t + ")"),
                ha="right", va="center", fontsize=9.5)
    for y, t, p in [(y1, "$b_1$", "0,575"), (y2, "$b_2$", "0,425")]:
        ax.add_patch(Circle((xb, y), r, fc=GREEN_L, ec=GREEN, lw=1.5))
        ax.text(xb, y, t, ha="center", va="center", fontsize=12)
        ax.text(xb + r + 0.12, y, "P(" + t + f") = {p}", ha="left", va="center", fontsize=9.5,
                color=MUTED)
    # flechas
    arrow(ax, (xa + r, y1), (xb - r, y1), color=INK, lw=1.8)
    arrow(ax, (xa + r, y2), (xb - r, y2), color=INK, lw=1.8)
    arrow(ax, (xa + r * 0.8, y1 - r * 0.6), (xb - r * 0.8, y2 + r * 0.6), color=RED, lw=1.4)
    arrow(ax, (xa + r * 0.8, y2 + r * 0.6), (xb - r * 0.8, y1 - r * 0.6), color=RED, lw=1.4)
    xm = (xa + xb) / 2
    ax.text(xm, y1 + 0.12, "$P(b_1/a_1)$ = 0,75", ha="center", va="bottom", fontsize=9.5)
    ax.text(xm, y2 - 0.12, "$P(b_2/a_2)$ = 0,75", ha="center", va="top", fontsize=9.5)
    ax.text(xa - 0.05, y1 - 0.62, "$P(b_2/a_1)$ = 0,25", ha="center", va="center",
            fontsize=9.5, color=RED)
    ax.text(xa - 0.05, y2 + 0.62, "$P(b_1/a_2)$ = 0,25", ha="center", va="center",
            fontsize=9.5, color=RED)
    ax.text(xa, 3.45, "Entrada A", ha="center", fontsize=9.5, weight="bold", color=BLUE)
    ax.text(xb, 3.45, "Salida B", ha="center", fontsize=9.5, weight="bold", color=GREEN)
    # resultados del ejercicio (wiki U1, ej. 1)
    box(ax, 7.0, 1.8, 1.55, 1.75,
        "p = 0,25 (error)\n\nH(A) = 0,934\nH(B) = 0,984\nH(B/A) = 0,811\nI(A,B) = 0,172\n[bit/símb]",
        fc=GRAY_L, size=9, ha="left")
    ax.set_xlim(0.0, 7.85)
    ax.set_ylim(0.2, 3.7)
    save(fig, "cd-canal-binario.png")


# ═════════════════════════════════════════════════════════════════════════
# 3. Entropías del sistema (Venn)
# ═════════════════════════════════════════════════════════════════════════
def fig_entropias():
    fig, ax = canvas(8.0, 3.8)
    ca, cb, cy, r = 1.75, 3.35, 2.0, 1.4
    ax.add_patch(Circle((ca, cy), r, fc=BLUE, alpha=0.13, ec="none"))
    ax.add_patch(Circle((cb, cy), r, fc=GREEN, alpha=0.13, ec="none"))
    ax.add_patch(Circle((ca, cy), r, fc="none", ec=BLUE, lw=1.6))
    ax.add_patch(Circle((cb, cy), r, fc="none", ec=GREEN, lw=1.6))
    ax.text(ca - 0.55, cy, "$H(A/B)$", ha="center", va="center", fontsize=10.5)
    ax.text(ca - 0.55, cy - 0.38, "equivocación", ha="center", va="center", fontsize=9,
            color=MUTED)
    ax.text((ca + cb) / 2, cy, "$I(A,B)$", ha="center", va="center", fontsize=10.5,
            weight="bold")
    ax.text((ca + cb) / 2, cy - 0.38, "mutua", ha="center", va="center", fontsize=9,
            color=MUTED)
    ax.text(cb + 0.55, cy, "$H(B/A)$", ha="center", va="center", fontsize=10.5)
    ax.text(cb + 0.55, cy - 0.38, "ruido", ha="center", va="center", fontsize=9, color=MUTED)
    ax.text(ca - 0.95, cy + 1.25, "$H(A)$", ha="center", fontsize=11, color=BLUE, weight="bold")
    ax.text(cb + 0.95, cy + 1.25, "$H(B)$", ha="center", fontsize=11, color=GREEN,
            weight="bold")
    brace(ax, ca - r, cb + r, cy - r - 0.08, 0.22, color=INK)
    ax.text((ca + cb) / 2, cy - r - 0.42, "$H(A,B)$  (todo el sistema)", ha="center",
            va="top", fontsize=10)
    x0 = 5.55
    ax.text(x0, 3.0, "$I(A,B) = H(A) - H(A/B)$", fontsize=10.5)
    ax.text(x0, 2.45, "$\\qquad\\ \\ = H(B) - H(B/A)$", fontsize=10.5)
    ax.text(x0, 1.9, "$\\qquad\\ \\ = H(A) + H(B) - H(A,B)$", fontsize=10.5)
    ax.text(x0, 1.15, "Canal transparente: $H(A/B) = H(B/A) = 0$\n"
                      "y los dos círculos coinciden.", fontsize=9, color=MUTED, va="top")
    ax.set_xlim(0.15, 8.9)
    ax.set_ylim(0.0, 3.7)
    save(fig, "cd-entropias.png")


# ═════════════════════════════════════════════════════════════════════════
# 4. Transmisión multinivel
# ═════════════════════════════════════════════════════════════════════════
def fig_multinivel():
    fig, ax = plt.subplots(figsize=(7.8, 3.6))
    tau = 1.0
    info = [1.5, -2.5, 3.0, 0.5, -1.0, 2.0]
    vals = [4.0] + info + [-4.0]
    for k, v in enumerate(vals):
        col = ORANGE if k in (0, len(vals) - 1) else BLUE
        fc = ORANGE_L if k in (0, len(vals) - 1) else BLUE_L
        ax.add_patch(Rectangle((k * tau, min(0, v)), tau, abs(v), fc=fc, ec=col, lw=1.4))
    for lv in np.arange(-3.5, 3.6, 0.5):
        ax.axhline(lv, color=GRID, lw=0.7, zorder=0)
    ax.axhline(0, color=MUTED, lw=1.0)
    n = len(info)
    Ttot = (n + 2) * tau
    ax.set_xlim(-0.3, Ttot + 0.4)
    ax.set_ylim(-7.2, 6.2)
    ax.set_yticks([-4, 0, 4])
    ax.set_yticklabels(["−4 V", "0", "+4 V"])
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.text(Ttot + 0.25, 0.25, "t", fontsize=10, color=MUTED)
    ax.text(0.5, 4.35, "arranque\n(fijo)", ha="center", va="bottom", fontsize=9, color=ORANGE)
    ax.text(Ttot - 0.5, -4.35, "stop\n(fijo)", ha="center", va="top", fontsize=9, color=ORANGE)
    ax.text(1 + n / 2, 4.35, "n pulsos de información, cada uno en uno de μ niveles",
            ha="center", va="bottom", fontsize=9, color=BLUE)
    # cotas
    dim(ax, 3 * tau, 4 * tau, 3.4, "τ", color=INK, size=10.5)
    ax.plot([3, 3], [3.0, 3.6], color=MUTED, lw=0.8)
    ax.plot([4, 4], [0.5, 3.6], color=MUTED, lw=0.8, ls=":")
    dim(ax, 1 * tau, (n + 1) * tau, -4.8, "t = n·τ  (sólo información)", color=BLUE, size=9.5,
        above=False)
    dim(ax, 0, Ttot, -6.75, "T = N·τ,  N = n + 2  (cuenta arranque y stop)", color=INK,
        size=9.5, above=True)
    for x in (0, Ttot):
        ax.plot([x, x], [-6.9, -4.0 if x else 0], color=MUTED, lw=0.8, ls=":")
    ax.text(Ttot + 0.4, 2.6, "$M(T) = \\mu^{\\,n}$\n$I = n\\,\\lg\\mu$\n$R = I/T$",
            ha="left", va="center", fontsize=10, linespacing=1.7)
    save(fig, "cd-multinivel.png")


# ═════════════════════════════════════════════════════════════════════════
# 5. Jerarquía de códigos
# ═════════════════════════════════════════════════════════════════════════
def fig_jerarquia():
    fig, ax = canvas(8.0, 5.0)
    rings = [
        ("Códigos bloque", "singular: 0, 11, 0, 01", GRAY_L, MUTED),
        ("No singulares", "1, 11, 00, 10   (1100 = $S_2S_3$ o $S_1S_1S_3$)", ORANGE_L, ORANGE),
        ("Unívocos", "0, 01, 011, 0111   (coma al inicio: hay que esperar)", PURPLE_L, PURPLE),
        ("Instantáneos", "1, 01, 001, 0001   (ninguna es prefijo de otra)", BLUE_L, BLUE),
        ("Compactos", "", GREEN_L, GREEN),
    ]
    for k, (name, ex, fc, ec) in enumerate(rings):
        left, right = 0.1 + 0.22 * k, 7.9 - 0.22 * k
        top, bottom = 4.9 - 0.68 * k, 0.1 + 0.16 * k
        ax.add_patch(FancyBboxPatch((left, bottom), right - left, top - bottom,
                                    boxstyle="round,pad=0,rounding_size=0.18",
                                    fc=fc, ec=ec, lw=1.5))
        ax.text(left + 0.15, top - 0.32, name, ha="left", va="center", fontsize=10,
                weight="bold", color=ec)
        if ex:
            ax.text(right - 0.15, top - 0.32, ex, ha="right", va="center", fontsize=9.2,
                    color=INK)
    ax.text(4.0, 1.55, "L mínima entre todos los instantáneos (misma fuente y mismo alfabeto)",
            ha="center", va="center", fontsize=9.2)
    ax.text(4.0, 1.05, "0, 10, 110, 111  con  P = 1/2, 1/4, 1/8, 1/8   →   L = H = 1,75",
            ha="center", va="center", fontsize=9.2)
    ax.set_xlim(0, 8.0)
    ax.set_ylim(0, 5.0)
    save(fig, "cd-jerarquia-codigos.png")


# ═════════════════════════════════════════════════════════════════════════
# 6. Huffman (ejemplo de la cátedra: 0,4 / 0,3 / 0,1 / 0,1 / 0,06 / 0,04)
# ═════════════════════════════════════════════════════════════════════════
def fig_huffman():
    fig, ax = canvas(8.2, 4.9)
    Y = [4.4, 3.45, 2.5, 1.55, 0.6]
    nodes = {  # id: (x, y, prob, kind, extra)
        "root": (2.55, Y[0], "1", "int", None),
        "n06": (1.55, Y[1], "0,6", "int", 4),
        "S1": (3.55, Y[1], "0,4", "leaf", ("$S_1$", "1")),
        "S2": (0.75, Y[2], "0,3", "leaf", ("$S_2$", "00")),
        "n03": (2.35, Y[2], "0,3", "int", 3),
        "n02": (1.55, Y[3], "0,2", "int", 2),
        "n01": (3.15, Y[3], "0,1", "int", 1),
        "S3": (1.1, Y[4], "0,1", "leaf", ("$S_3$", "0100")),
        "S4": (2.0, Y[4], "0,1", "leaf", ("$S_4$", "0101")),
        "S5": (2.7, Y[4], "0,06", "leaf", ("$S_5$", "0110")),
        "S6": (3.6, Y[4], "0,04", "leaf", ("$S_6$", "0111")),
    }
    edges = [("root", "n06", "0"), ("root", "S1", "1"), ("n06", "S2", "0"),
             ("n06", "n03", "1"), ("n03", "n02", "0"), ("n03", "n01", "1"),
             ("n02", "S3", "0"), ("n02", "S4", "1"), ("n01", "S5", "0"), ("n01", "S6", "1")]
    rn = 0.25
    for a, b, bit in edges:
        xa, ya = nodes[a][:2]
        xb, yb = nodes[b][:2]
        ax.plot([xa, xb], [ya - rn, yb + rn], color=MUTED, lw=1.3, zorder=1)
        xm, ym = (xa + xb) / 2, (ya + yb) / 2
        off = -0.13 if bit == "0" else 0.13
        ax.text(xm + off, ym + 0.05, bit, ha="center", va="center", fontsize=10,
                weight="bold", color=RED if bit == "1" else BLUE)
    for k, (x, y, p, kind, extra) in nodes.items():
        if kind == "int":
            ax.add_patch(Circle((x, y), rn, fc="white", ec=INK, lw=1.3, zorder=2))
            ax.text(x, y, p, ha="center", va="center", fontsize=9.5, zorder=3)
            if extra:
                ax.text(x + rn + 0.08, y + 0.18, f"fusión {extra}", ha="left", va="center",
                        fontsize=9, color=ORANGE)
        else:
            name, code = extra
            box(ax, x, y, 0.62, 0.5, "", fc=GREEN_L, ec=GREEN)
            ax.text(x, y + 0.09, name, ha="center", va="center", fontsize=9.5)
            ax.text(x, y - 0.12, p, ha="center", va="center", fontsize=9, color=MUTED)
            ax.text(x, y - 0.38, code, ha="center", va="top", fontsize=9.5, weight="bold",
                    color=INK, family="monospace")
    ax.text(0.2, 4.4, "raíz", ha="left", va="center", fontsize=9, color=MUTED)
    # tabla
    tx = [4.75, 5.5, 6.45, 7.5]
    hdr = ["$S_i$", "$P_i$", "palabra", "$l_i$"]
    rows = [("$S_1$", "0,4", "1", "1"), ("$S_2$", "0,3", "00", "2"),
            ("$S_3$", "0,1", "0100", "4"), ("$S_4$", "0,1", "0101", "4"),
            ("$S_5$", "0,06", "0110", "4"), ("$S_6$", "0,04", "0111", "4")]
    y0 = 4.35
    for x, h in zip(tx, hdr):
        ax.text(x, y0, h, ha="center", va="center", fontsize=10, weight="bold")
    ax.plot([4.4, 7.85], [y0 - 0.22, y0 - 0.22], color=MUTED, lw=1)
    for i, row in enumerate(rows):
        y = y0 - 0.5 - 0.42 * i
        if i % 2 == 0:
            ax.add_patch(Rectangle((4.4, y - 0.21), 3.45, 0.42, fc=GRAY_L, ec="none", zorder=0))
        for j, (x, v) in enumerate(zip(tx, row)):
            ax.text(x, y, v, ha="center", va="center", fontsize=10,
                    family="monospace" if j == 2 else None,
                    weight="bold" if j == 2 else "normal")
    yl = y0 - 0.5 - 0.42 * 6 + 0.05
    ax.plot([4.4, 7.85], [yl + 0.15, yl + 0.15], color=MUTED, lw=1)
    ax.text(6.12, yl - 0.2, "L = 2,2 binit/símb\nH = 2,1435 bit/símb\nη = H/L = 0,974",
            ha="center", va="top", fontsize=9.8, linespacing=1.45)
    ax.set_xlim(0.1, 8.0)
    ax.set_ylim(0.0, 4.8)
    save(fig, "cd-huffman.png")


# ═════════════════════════════════════════════════════════════════════════
# 7. Árbol de Kraft (código instantáneo 0, 10, 110)
# ═════════════════════════════════════════════════════════════════════════
def fig_kraft():
    fig, ax = canvas(8.2, 4.2)
    dx = 1.25
    leaf_y = {format(i, "03b"): 3.85 - 0.5 * i for i in range(8)}

    def ypos(p):
        ys = [y for k, y in leaf_y.items() if k.startswith(p)]
        return sum(ys) / len(ys)

    words = {"0", "10", "110"}
    free = {"111"}

    def status(p):
        if p in words:
            return "word"
        if p in free:
            return "free"
        if any(p.startswith(w) and p != w for w in words):
            return "pruned"
        return "node"

    allp = [""] + [format(i, f"0{d}b") for d in (1, 2, 3) for i in range(2 ** d)]
    pos = {p: (0.4 + dx * len(p), ypos(p)) for p in allp}
    for p in allp:
        if not p:
            continue
        par = p[:-1]
        st = status(p)
        x0, y0 = pos[par]
        x1, y1 = pos[p]
        pr = st == "pruned"
        ax.plot([x0 + 0.12, x1 - 0.12], [y0, y1], color=GRID if pr else MUTED,
                lw=1.0 if pr else 1.3, ls="--" if pr else "-", zorder=1)
        if not pr:
            ax.text((x0 + x1) / 2 - 0.05, (y0 + y1) / 2 + (0.1 if p[-1] == "0" else -0.1),
                    p[-1], ha="center", va="center", fontsize=9.5, weight="bold",
                    color=BLUE if p[-1] == "0" else RED)
    for p in allp:
        x, y = pos[p]
        st = status(p) if p else "node"
        if st == "word":
            box(ax, x + 0.18, y, 0.62, 0.36, p, fc=GREEN_L, ec=GREEN, size=10, weight="bold")
        elif st == "free":
            box(ax, x + 0.18, y, 0.62, 0.36, p, fc="white", ec=MUTED, size=10, color=MUTED)
            ax.patches[-1].set_linestyle("--")
        elif st == "pruned":
            ax.add_patch(Circle((x, y), 0.06, fc="white", ec=GRID, lw=1.0))
        else:
            ax.add_patch(Circle((x, y), 0.08, fc=INK, ec=INK))
    for p, l in [("0", 1), ("10", 2), ("110", 3)]:
        x, y = pos[p]
        ax.text(x + 0.56, y, f"$2^{{-{l}}}$", ha="left", va="center", fontsize=10, color=GREEN)
    ax.text(pos["111"][0] + 0.56, pos["111"][1], "libre", ha="left", va="center",
            fontsize=9, color=MUTED)
    ax.text(pos["0"][0] + 0.2, 3.95, "subárbol podado:\nnada puede empezar con 0",
            ha="left", va="bottom", fontsize=9, color=MUTED, style="italic")
    # suma
    x0 = 5.35
    ax.text(x0, 3.5, "$\\sum_i 2^{-l_i} = 2^{-1} + 2^{-2} + 2^{-3}$", fontsize=10.5)
    ax.text(x0, 2.95, "$= 1/2 + 1/4 + 1/8 = 7/8 \\leq 1$", fontsize=10.5, color=GREEN)
    ax.text(x0, 2.35, "Cada palabra de longitud $l$ tapa\n$2^{3-l}$ hojas: 4 + 2 + 1 = 7 de 8.\n"
                      "La hoja libre (111) es el 1/8 que sobra.",
            fontsize=9.3, va="top", linespacing=1.4)
    ax.text(x0, 0.95, "Longitudes 1, 2, 2, 3 → 9/8 > 1:\nno existe código instantáneo\n"
                      "(ni unívoco, por McMillan).",
            fontsize=9.3, va="top", color=RED, linespacing=1.4)
    ax.set_xlim(0.2, 8.1)
    ax.set_ylim(0.1, 4.6)
    save(fig, "cd-kraft-arbol.png")


# ═════════════════════════════════════════════════════════════════════════
# 8. Hamming (7,4) con diagrama de Venn — convención de la cátedra
#    C1 = I0+I1+I2, C2 = I1+I2+I3, C3 = I0+I2+I3; TX 1000 110, RX 1010 110
# ═════════════════════════════════════════════════════════════════════════
def fig_hamming():
    fig, ax = canvas(8.4, 4.6)
    R = 1.3
    cI, cII, cIII = (2.0, 2.95), (3.4, 2.95), (2.7, 1.75)
    for c, ec, fc, lab, lp in [
        (cI, RED, RED_L, "Zona I  ($C_1$)", (0.75, 4.45)),
        (cII, RED, RED_L, "Zona II  ($C_2$)", (4.65, 4.45)),
        (cIII, GREEN, GREEN_L, "Zona III  ($C_3$)", (2.7, 0.18)),
    ]:
        ax.add_patch(Circle(c, R, fc=fc, alpha=0.35, ec="none"))
        ax.add_patch(Circle(c, R, fc="none", ec=ec, lw=1.8))
        ax.text(*lp, lab, ha="center", va="center", fontsize=10, color=ec, weight="bold")
    regions = [  # (x, y, nombre, valor recibido, error)
        (1.4, 3.35, "C_1", "0", False),
        (4.0, 3.35, "C_2", "1", False),
        (2.7, 0.95, "C_3", "1", False),
        (2.7, 3.5, "I_1", "1", True),
        (2.05, 2.15, "I_0", "0", False),
        (3.35, 2.15, "I_3", "1", False),
        (2.7, 2.6, "I_2", "0", False),
    ]
    for x, y, nm, v, err in regions:
        col = RED if err else INK
        ax.text(x, y + 0.13, f"${nm}$", ha="center", va="center", fontsize=10, color=col)
        ax.text(x, y - 0.15, v, ha="center", va="center", fontsize=11, weight="bold",
                color=col)
    # texto
    x0 = 5.35
    lines = [
        ("Bit de control = paridad par de su zona:", INK, 9.5, "normal"),
        ("$C_1 = I_0 \\oplus I_1 \\oplus I_2$", INK, 10, "normal"),
        ("$C_2 = I_1 \\oplus I_2 \\oplus I_3$", INK, 10, "normal"),
        ("$C_3 = I_0 \\oplus I_2 \\oplus I_3$", INK, 10, "normal"),
        ("", INK, 6, "normal"),
        ("TX  $I_3I_2I_1I_0\\,C_3C_2C_1$ = 1000 110", INK, 9.5, "normal"),
        ("RX  1010 110  (se invirtió $I_1$)", RED, 9.5, "normal"),
        ("", INK, 6, "normal"),
        ("Recalculados con 1010: $C_3C_2C_1$ = 101", INK, 9.5, "normal"),
        ("Recibidos: 110 → fallan $C_1$ y $C_2$", INK, 9.5, "normal"),
        ("El único bit común sólo a I y II es $I_1$", RED, 9.5, "bold"),
        ("→ se invierte: información = 1000", INK, 9.5, "normal"),
    ]
    y = 4.35
    for t, c, s, w in lines:
        if t:
            ax.text(x0, y, t, ha="left", va="center", fontsize=s, color=c, weight=w)
        y -= 0.36 if t else 0.12
    ax.set_xlim(0.3, 8.5)
    ax.set_ylim(0.0, 4.65)
    save(fig, "cd-hamming-venn.png")


# ═════════════════════════════════════════════════════════════════════════
# 9. Decodificación por síndrome
# ═════════════════════════════════════════════════════════════════════════
def fig_sindrome():
    fig, ax = canvas(7.6, 8.0)
    xc = 2.9
    box(ax, xc, 6.4, 2.6, 0.55, "Palabra recibida  $v'$", fc="white", ec=INK, r=0.25)
    box(ax, xc, 5.45, 2.6, 0.6, "Síndrome  $S = v' \\cdot H^T$", fc=BLUE_L, ec=BLUE)
    diamond(ax, xc, 4.25, 2.0, 1.05, "¿$S = 0$?")
    box(ax, 6.05, 4.25, 2.6, 0.85, "Pertenece a V:\ncorrecta (o error\nno detectable)",
        fc=GREEN_L, ec=GREEN, size=9.3)
    box(ax, xc, 2.95, 3.4, 0.75,
        "Familia de S: todos los $e$\ncon $e \\cdot H^T = S$  ($2^m$ vectores)",
        fc=GRAY_L, size=9.3)
    box(ax, xc, 1.9, 3.4, 0.6, "Líder = vector de menor peso", fc=ORANGE_L, ec=ORANGE)
    diamond(ax, xc, 0.75, 2.2, 1.05, "¿Líder\núnico?", size=9.3)
    box(ax, 6.05, 0.75, 2.6, 0.75, "Corregir:\n$v = v' \\oplus e$", fc=GREEN_L, ec=GREEN,
        size=9.5)
    box(ax, xc, -0.6, 3.0, 0.6, "Sólo detecta: pedir retransmisión", fc=RED_L, ec=RED,
        size=9.3)
    arrow(ax, (xc, 6.12), (xc, 5.75), color=INK)
    arrow(ax, (xc, 5.15), (xc, 4.78), color=INK)
    arrow(ax, (xc + 1.0, 4.25), (6.05 - 1.3, 4.25), color=INK)
    ax.text(xc + 1.12, 4.38, "Sí", fontsize=9.5, weight="bold")
    arrow(ax, (xc, 3.72), (xc, 3.33), color=INK)
    ax.text(xc + 0.12, 3.5, "No", fontsize=9.5, weight="bold", va="center")
    arrow(ax, (xc, 2.57), (xc, 2.2), color=INK)
    arrow(ax, (xc, 1.6), (xc, 1.28), color=INK)
    arrow(ax, (xc + 1.1, 0.75), (6.05 - 1.3, 0.75), color=INK)
    ax.text(xc + 1.22, 0.88, "Sí", fontsize=9.5, weight="bold")
    arrow(ax, (xc, 0.22), (xc, -0.3), color=INK)
    ax.text(xc + 0.12, -0.04, "No", fontsize=9.5, weight="bold", va="center")
    ax.text(xc, -1.15,
            "El mismo síndrome lo producen también errores dobles, triples…:\n"
            "se corrige el más probable (el de menor peso).",
            ha="center", va="top", fontsize=9.2, color=MUTED, style="italic")
    ax.set_xlim(1.0, 7.5)
    ax.set_ylim(-1.8, 6.8)
    save(fig, "cd-sindrome.png")


# ═════════════════════════════════════════════════════════════════════════
# 10. ASK / FSK / PSK
# ═════════════════════════════════════════════════════════════════════════
def fig_modulaciones():
    bits = [1, 0, 1, 1, 0]
    nb = len(bits)
    t = np.linspace(0, nb, 4000)
    b = np.array([bits[min(int(x), nb - 1)] for x in t])
    fc = 3.0
    ask = b * np.sin(2 * np.pi * fc * t)
    # FSK con fase continua: f1 = 4 (para 1), f0 = 2 (para 0)
    f = np.where(b == 1, 4.0, 2.0)
    phase = 2 * np.pi * np.cumsum(f) * (t[1] - t[0])
    fsk = np.sin(phase)
    psk = np.sin(2 * np.pi * fc * t + np.where(b == 1, 0, np.pi))
    fig, axs = plt.subplots(4, 1, figsize=(7.6, 5.4), sharex=True,
                            gridspec_kw={"height_ratios": [0.8, 1, 1, 1], "hspace": 0.25})
    data = [(b, "datos", INK), (ask, "ASK", BLUE), (fsk, "FSK", GREEN), (psk, "PSK", PURPLE)]
    notes = ["", "1 = hay portadora · 0 = no hay",
             "1 = $f_1$ (alta) · 0 = $f_0$ (baja)", "0 = fase invertida (180°)"]
    for ax, (y, name, col), note in zip(axs, data, notes):
        ax.plot(t, y, color=col, lw=1.4)
        for k in range(nb + 1):
            ax.axvline(k, color=GRID, lw=0.9, ls="--", zorder=0)
        ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.set_ylabel(name, rotation=0, ha="right", va="center", fontsize=10.5, weight="bold",
                      color=col, labelpad=10)
        ax.set_ylim(-1.35, 1.35) if name != "datos" else ax.set_ylim(-0.25, 1.55)
        if note:
            ax.text(nb + 0.08, 0, note, ha="left", va="center", fontsize=9, color=MUTED)
    for k, bit in enumerate(bits):
        axs[0].text(k + 0.5, 1.22, str(bit), ha="center", va="center", fontsize=12,
                    weight="bold")
    axs[-1].set_xticks([])
    axs[-1].set_xlim(0, nb)
    axs[-1].annotate("", xy=(nb, -1.6), xytext=(0, -1.6), xycoords="data",
                     arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.0),
                     annotation_clip=False)
    axs[-1].text(nb, -1.85, "t", ha="right", va="top", fontsize=10, color=MUTED)
    save(fig, "cd-modulaciones.png")


# ═════════════════════════════════════════════════════════════════════════
# 11. Constelaciones BPSK / QPSK / QAM-16
# ═════════════════════════════════════════════════════════════════════════
def fig_constelacion():
    fig, axs = plt.subplots(1, 3, figsize=(8.0, 3.4))
    s2 = 1 / np.sqrt(2)
    sets = [
        ("BPSK", [(-1, 0), (1, 0)], ["0", "1"], 2, BLUE),
        ("QPSK", [(s2, s2), (-s2, s2), (-s2, -s2), (s2, -s2)], ["00", "01", "11", "10"], 4,
         GREEN),
        ("QAM-16", [(i, q) for q in (3, 1, -1, -3) for i in (-3, -1, 1, 3)], None, 16, PURPLE),
    ]
    for ax, (name, pts, labs, mu, col) in zip(axs, sets):
        lim = 1.6 if mu < 16 else 4.6
        ax.axhline(0, color=GRID, lw=1, zorder=0)
        ax.axvline(0, color=GRID, lw=1, zorder=0)
        if mu < 16:
            th = np.linspace(0, 2 * np.pi, 200)
            ax.plot(np.cos(th), np.sin(th), color=GRID, lw=1, ls="--", zorder=0)
        xs, ys = zip(*pts)
        ax.scatter(xs, ys, s=55 if mu < 16 else 38, color=col, zorder=3)
        if labs:
            for (x, y), l in zip(pts, labs):
                ax.text(x * 1.0 + (0.0 if mu == 2 else 0.12 * np.sign(x)),
                        y + (0.22 if mu == 2 else 0.2 * np.sign(y)), l, ha="center",
                        va="center", fontsize=9.5, family="monospace")
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(False)
        bits = int(np.log2(mu))
        ax.set_title(name, color=col)
        ax.text(0.5, -0.1, f"μ = {mu}  →  {bits} bit{'s' if bits > 1 else ''}/símbolo",
                transform=ax.transAxes, ha="center", va="top", fontsize=10)
    fig.text(0.5, 0.06, "Mismos baudios $s$ → más bits/s:   $R = s\\cdot\\log_2\\mu$   "
             "(más niveles exigen mejor S/N: los puntos quedan más juntos)",
             ha="center", va="top", fontsize=9.8, color=INK)
    save(fig, "cd-constelacion.png")


# ═════════════════════════════════════════════════════════════════════════
# 12. PCM: señal, muestreo, cuantificación + codificación
# ═════════════════════════════════════════════════════════════════════════
def fig_pcm():
    def x(t):
        return 2.3 * np.sin(2 * np.pi * 0.9 * t + 0.3) + 1.1 * np.sin(2 * np.pi * 2.1 * t + 1.0)

    t = np.linspace(0, 1, 800)
    ns = 10
    ts = (np.arange(ns) + 0.5) / ns
    xs = x(ts)
    levels = np.arange(-3.5, 3.6, 1.0)  # 8 niveles
    q = np.clip(np.round(xs - 0.5) + 0.5, -3.5, 3.5)
    codes = [format(int(v + 3.5), "03b") for v in q]
    fig, axs = plt.subplots(3, 1, figsize=(7.6, 7.2), sharex=True,
                            gridspec_kw={"hspace": 0.35})
    for ax in axs:
        ax.axhline(0, color=MUTED, lw=0.8)
        ax.set_ylim(-4.3, 4.3)
        ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.set_xlim(0, 1.0)
    a1, a2, a3 = axs
    a1.plot(t, x(t), color=BLUE, lw=1.8)
    a1.set_title("1) Mensaje analógico $x(t)$", loc="left")
    a2.plot(t, x(t), color=BLUE, lw=1.0, alpha=0.35)
    a2.vlines(ts, 0, xs, color=ORANGE, lw=2.2)
    a2.scatter(ts, xs, color=ORANGE, s=18, zorder=3)
    a2.set_title("2) Muestreo (PAM):  $T_s = 1/f_s$,  $f_s \\geq 2f_{max}$", loc="left")
    a2.annotate("", xy=(ts[1], -3.6), xytext=(ts[0], -3.6),
                arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=1, mutation_scale=9,
                                shrinkA=0, shrinkB=0))
    a2.text((ts[0] + ts[1]) / 2, -3.45, "$T_s$", ha="center", va="bottom", fontsize=10)
    for lv in levels:
        a3.axhline(lv, color=GRID, lw=0.9, zorder=0)
        a3.text(1.01, lv, format(int(lv + 3.5), "03b"), ha="left", va="center", fontsize=9,
                color=MUTED, family="monospace", transform=a3.get_yaxis_transform())
    for lv in np.arange(-4, 4.1, 1.0):
        a3.axhline(lv, color=GRID, lw=0.5, ls=":", zorder=0)
    a3.plot(t, x(t), color=BLUE, lw=1.0, alpha=0.3)
    a3.scatter(ts, xs, color=ORANGE, s=14, zorder=3, alpha=0.6)
    a3.vlines(ts, 0, q, color=GREEN, lw=2.4)
    a3.scatter(ts, q, color=GREEN, s=30, zorder=4, marker="s")
    a3.set_title("3) Cuantificación a 8 niveles + codificación con 3 bits por muestra",
                 loc="left")
    for tt, c in zip(ts, codes):
        a3.text(tt, -4.75, c, ha="center", va="top", fontsize=9.5, family="monospace",
                weight="bold", color=GREEN)
    a3.text(1.01, 4.25, "código", ha="left", va="center", fontsize=9, color=MUTED,
            transform=a3.get_yaxis_transform())
    a3.set_xticks([])
    a3.spines["bottom"].set_visible(False)
    for ax in (a1, a2):
        ax.spines["bottom"].set_visible(False)
    a3.text(0.0, -6.0, "señal PCM:  " + " ".join(codes), ha="left", va="top", fontsize=9.3,
            family="monospace", color=INK)
    save(fig, "cd-pcm.png")


# ═════════════════════════════════════════════════════════════════════════
# 13. Trama TDM (final 2025: 25 + 2 muestras, 7 dígitos, fmax = 3500 Hz)
# ═════════════════════════════════════════════════════════════════════════
def fig_trama_tdm():
    fig, ax = canvas(8.4, 4.6)
    y0, hh = 3.2, 0.6
    slots = ["1", "2", "3", "…", "25", "ctl", "ctl"]
    sw = 0.92
    x = 0.4
    xs = []
    for s in slots:
        if s == "…":
            ax.text(x + sw / 2, y0 + hh / 2, "…", ha="center", va="center", fontsize=12)
        else:
            ctl = s == "ctl"
            ax.add_patch(Rectangle((x, y0), sw, hh, fc=ORANGE_L if ctl else BLUE_L,
                                   ec=ORANGE if ctl else BLUE, lw=1.3))
            ax.text(x + sw / 2, y0 + hh / 2, s if not ctl else "control", ha="center",
                    va="center", fontsize=9.5 if not ctl else 9, color=INK)
        xs.append(x)
        x += sw
    xend = x
    # comienzo de la trama siguiente
    for k, s in enumerate(["1", "2"]):
        ax.add_patch(Rectangle((xend + k * sw, y0), sw, hh, fc="white", ec=GRID, lw=1.1))
        ax.text(xend + k * sw + sw / 2, y0 + hh / 2, s, ha="center", va="center", fontsize=9.5,
                color=MUTED)
    ax.text(xend + 2 * sw + 0.1, y0 + hh / 2, "trama siguiente", ha="left", va="center",
            fontsize=9, color=MUTED, style="italic")
    dim(ax, 0.4, xend, y0 + hh + 0.12, "$T_s = 1/f_s$  (una trama: N = 25 + 2 = 27 muestras)",
        size=9.5)
    dim(ax, xs[1], xs[1] + sw, y0 - 0.12, "$T_M = T_s/N$", size=9.5, above=False)
    # zoom de la ranura 2
    zx0, zy, bw = 1.0, 1.35, 0.78
    bits = "1011001"
    for k, b in enumerate(bits):
        ax.add_patch(Rectangle((zx0 + k * bw, zy), bw, 0.55, fc=BLUE_L if b == "1" else "white",
                               ec=BLUE, lw=1.2))
        ax.text(zx0 + k * bw + bw / 2, zy + 0.275, b, ha="center", va="center", fontsize=10.5,
                family="monospace", weight="bold")
    zx1 = zx0 + 7 * bw
    ax.plot([xs[1], zx0], [y0 - 0.55, zy + 0.55], color=MUTED, lw=0.9, ls=":")
    ax.plot([xs[1] + sw, zx1], [y0 - 0.55, zy + 0.55], color=MUTED, lw=0.9, ls=":")
    dim(ax, zx0, zx0 + bw, zy - 0.1, "τ", size=10.5, above=False)
    dim(ax, zx0 + bw, zx1, zy - 0.1, "muestra: n = 7 dígitos,  $\\tau = T_M/n$", size=9.5,
        above=False)
    ax.text(zx1 + 0.25, zy + 0.27, "$f_s = 2\\cdot 3500 = 7000$ Hz\n$T_s = 142{,}86\\ \\mu s$\n"
            "$T_M = 5{,}29\\ \\mu s$\n$\\tau = 0{,}756\\ \\mu s$",
            ha="left", va="center", fontsize=9.5, linespacing=1.5)
    box(ax, 4.2, 0.25, 7.6, 0.5,
        "$B_w = 1/\\tau = N\\cdot n\\cdot 2f_{max} = 27\\cdot 7\\cdot 2\\cdot 3500"
        " = 1{,}323\\ \\mathrm{MHz}$", fc=GREEN_L, ec=GREEN, size=10.5)
    ax.set_xlim(0.3, 8.6)
    ax.set_ylim(-0.1, 4.45)
    save(fig, "cd-trama-tdm.png")


# ═════════════════════════════════════════════════════════════════════════
# 14. Espectro de un tren de pulsos de duración τ
# ═════════════════════════════════════════════════════════════════════════
def fig_espectro():
    fig, ax = plt.subplots(figsize=(7.6, 3.4))
    tau = 1.0
    f = np.linspace(0, 3.3, 1200)
    env = np.abs(np.sinc(f * tau))
    ax.fill_between(f, 0, env, where=f <= 1 / tau, color=BLUE_L, zorder=0)
    ax.plot(f, env, color=BLUE, lw=1.2, ls="--", zorder=2)
    T0 = 4 * tau
    fk = np.arange(0, 3.3, 1 / T0)
    ax.vlines(fk, 0, np.abs(np.sinc(fk * tau)), color=INK, lw=1.8, zorder=3)
    ax.axvline(1 / (2 * tau), color=ORANGE, lw=1.4, ls=":", zorder=1)
    ax.set_xlim(0, 3.3)
    ax.set_ylim(0, 1.18)
    ax.set_xticks([0, 0.5, 1, 2, 3])
    ax.set_xticklabels(["0", "$\\frac{1}{2\\tau}$", "$\\frac{1}{\\tau}$",
                        "$\\frac{2}{\\tau}$", "$\\frac{3}{\\tau}$"], fontsize=12)
    ax.set_yticks([])
    ax.set_xlabel("f", loc="right")
    ax.set_ylabel("|espectro|")
    ax.annotate("$B_w = 1/\\tau$ (cátedra):\nprimer cruce por cero;\nlóbulo principal = casi toda\nla energía",
                xy=(1.0, 0.02), xytext=(1.25, 0.72), fontsize=9.5, color=BLUE,
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1))
    ax.text(0.53, 1.1, "$1/(2\\tau) = s/2$: mínimo de Nyquist\n(criterio alternativo, apunte 1)",
            ha="left", va="top", fontsize=9.3, color=ORANGE)
    ax.text(2.25, 0.45, "líneas separadas $1/T_0$\n($T_0$ = período del tren)\nenvolvente |sinc(fτ)|",
            ha="left", va="top", fontsize=9.3, color=INK)
    save(fig, "cd-espectro-pulso.png")


# ═════════════════════════════════════════════════════════════════════════
# 15. FDM vs TDM + espectro ADSL
# ═════════════════════════════════════════════════════════════════════════
def fig_fdm_tdm_adsl():
    fig = plt.figure(figsize=(7.8, 5.6))
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 0.95], hspace=0.55, wspace=0.3)
    cols = [(BLUE_L, BLUE), (GREEN_L, GREEN), (ORANGE_L, ORANGE), (PURPLE_L, PURPLE)]
    a1 = fig.add_subplot(gs[0, 0])
    for k, (fc, ec) in enumerate(cols):
        a1.add_patch(Rectangle((0.05, k + 0.12), 3.9, 0.76, fc=fc, ec=ec, lw=1.2))
        a1.text(2.0, k + 0.5, f"señal {k + 1}", ha="center", va="center", fontsize=9.5)
    a1.set_xlim(0, 4)
    a1.set_ylim(0, 4)
    a1.set_title("(a) FDM: cada uno su banda, todos a la vez", loc="left", fontsize=9.8)
    a2 = fig.add_subplot(gs[0, 1])
    for k in range(8):
        fc, ec = cols[k % 4]
        a2.add_patch(Rectangle((k * 0.5 + 0.03, 0.05), 0.44, 3.9, fc=fc, ec=ec, lw=1.2))
        a2.text(k * 0.5 + 0.25, 2.0, f"{k % 4 + 1}", ha="center", va="center", fontsize=9.5)
    a2.set_xlim(0, 4)
    a2.set_ylim(0, 4)
    a2.set_title("TDM: cada uno toda la banda, por turnos", loc="left", fontsize=9.8)
    for ax in (a1, a2):
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel("tiempo →", loc="right", fontsize=9.5)
        ax.set_ylabel("frecuencia →", loc="top", fontsize=9.5)
    # ADSL con escala quebrada
    a3 = fig.add_subplot(gs[1, :])
    fk = [0, 4, 25.875, 138, 1104]
    xp = [0, 1.3, 2.0, 4.0, 8.0]

    def m(v):
        return np.interp(v, fk, xp)

    bands = [(0, 4, "Voz\n(PSTN)", GREEN_L, GREEN), (25.875, 138, "Subida (upstream)\n112,125 kHz", ORANGE_L,
                                                      ORANGE),
             (138, 1104, "Bajada (downstream)\n966 kHz", BLUE_L, BLUE)]
    a3.add_patch(Rectangle((m(4), 0), m(25.875) - m(4), 0.35, fc=GRAY_L, ec=MUTED, lw=0.8,
                           hatch="///"))
    a3.text((m(4) + m(25.875)) / 2, 0.5, "guarda", ha="center", va="bottom", fontsize=9,
            color=MUTED)
    for lo, hi, lab, fc, ec in bands:
        h = 1.0 if lo else 0.8
        a3.add_patch(Rectangle((m(lo), 0), m(hi) - m(lo), h, fc=fc, ec=ec, lw=1.3))
        a3.text((m(lo) + m(hi)) / 2, h / 2, lab, ha="center", va="center", fontsize=9.5)
    a3.set_xlim(0, 8.15)
    a3.set_ylim(0, 1.3)
    a3.set_xticks(xp)
    a3.set_xticklabels(["0", "4", "25,875", "138", "1104"], fontsize=9.5)
    a3.set_xlabel("f [kHz]  (escala no lineal: tramos estirados para que se vea la voz)",
                  fontsize=9.5)
    a3.set_yticks([])
    a3.spines["left"].set_visible(False)
    for xb in (1.3, 2.0, 4.0):
        a3.text(xb, 0, "//", ha="center", va="center", fontsize=10, color=MUTED,
                transform=a3.transData, clip_on=False,
                bbox=dict(fc="white", ec="none", pad=0.5))
    a3.set_title("(b) ADSL: FDM sobre el par de cobre del abonado (asimétrico)", loc="left",
                 fontsize=9.8)
    save(fig, "cd-fdm-tdm-adsl.png")


# ═════════════════════════════════════════════════════════════════════════
# 16. Elección del medio de acceso (ejemplos de la cátedra + banco de teoría)
# ═════════════════════════════════════════════════════════════════════════
def fig_medio_acceso():
    fig, ax = canvas(8.6, 6.4)
    MED = {
        "fibra": (BLUE_L, BLUE), "par": (GREEN_L, GREEN),
        "re": (ORANGE_L, ORANGE), "sat": (PURPLE_L, PURPLE),
    }
    xr, xz, xc, xl = 0.55, 1.9, 3.95, 6.85
    ys = [5.75, 5.05, 4.3, 3.6, 2.9, 2.15, 1.45, 0.75]
    leaves = [
        ("Alta", "Fibra óptica\n(en anillo si segurización)", "fibra", "ej. 2"),
        ("Baja", "Par telefónico + HDSL", "par", "ej. 1"),
        ("Alta", "Fibra óptica en anillo", "fibra", "ej. 6"),
        ("Baja / media,\ncon espacio p/ mástil", "Radioenlace\n(+ satélite si segurización)",
         "re", "ej. 4, 5"),
        ("Baja, sin espacio\no transitoria", "Satélite", "sat", "ej. 3"),
        ("Media, definitiva,\nen crecimiento", "Fibra + backup\npor radioenlace", "fibra",
         "ej. 7"),
        ("Baja, transitoria", "Satélite", "sat", "ej. 3"),
        ("Baja", "Satélite", "sat", "ej. 8"),
    ]
    zones = [("Urbana", [0, 1]), ("Suburbana", [2, 3, 4]), ("Rural", [5, 6]),
             ("Montañosa /\nselva", [7])]
    box(ax, xr, 3.25, 0.85, 0.55, "Zona", fc="white", ec=INK, weight="bold", r=0.2)
    for name, idx in zones:
        yz = np.mean([ys[i] for i in idx])
        box(ax, xz, yz, 1.3, 0.55, name, fc=GRAY_L, ec=MUTED, size=9.5, weight="bold")
        arrow(ax, (xr + 0.43, 3.25), (xz - 0.65, yz), color=MUTED, lw=1.1, ms=9)
        for i in idx:
            cond, med, kind, ej = leaves[i]
            box(ax, xc, ys[i], 2.0, 0.6, cond, fc="white", ec=MUTED, size=9)
            arrow(ax, (xz + 0.65, yz), (xc - 1.0, ys[i]), color=MUTED, lw=1.1, ms=9)
            fc, ec = MED[kind]
            box(ax, xl, ys[i], 2.5, 0.6, med, fc=fc, ec=ec, size=9.3, weight="bold")
            arrow(ax, (xc + 1.0, ys[i]), (xl - 1.25, ys[i]), color=MUTED, lw=1.1, ms=9)
            ax.text(xl + 1.32, ys[i], ej, ha="left", va="center", fontsize=9, color=MUTED)
    ax.text(xz, 6.35, "ubicación", ha="center", fontsize=9, color=MUTED, style="italic")
    ax.text(xc, 6.35, "velocidad (BW) y otros datos", ha="center", fontsize=9, color=MUTED,
            style="italic")
    ax.text(xl, 6.35, "medio de acceso", ha="center", fontsize=9, color=MUTED, style="italic")
    ax.text(0.15, 0.05,
            "BW: bajo 4–8 M · medio 10–50 M · alto > 100 M.   Cablemódem (coaxil): sólo "
            "residencial, nunca para una empresa.\nSi la consigna no lo dice, escribir el "
            "supuesto (espacio físico, segurización, permanencia).",
            ha="left", va="top", fontsize=9, color=INK, linespacing=1.4)
    ax.set_xlim(0.05, 8.6)
    ax.set_ylim(-0.55, 6.55)
    save(fig, "cd-medio-acceso.png")


# ═════════════════════════════════════════════════════════════════════════
# 17. M/M/1: esquema + L, Lq vs ρ (final 2025: ρ = 2/3, L = 2, Lq = 1,33)
# ═════════════════════════════════════════════════════════════════════════
def fig_mm1():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.2, 3.4),
                                 gridspec_kw={"width_ratios": [1, 1.25], "wspace": 0.25})
    a1.axis("off")
    a1.set_xlim(0, 4.2)
    a1.set_ylim(0, 3)
    a1.text(0.3, 1.68, "λ", ha="center", fontsize=14, color=ORANGE)
    a1.text(0.3, 2.12, "llegadas\nPoisson", ha="center", va="bottom", fontsize=9, color=MUTED)
    arrow(a1, (0.05, 1.5), (0.75, 1.5), color=INK, lw=1.6)
    a1.add_patch(Rectangle((0.8, 1.15), 1.5, 0.7, fc="white", ec=INK, lw=1.3))
    for xq in (1.1, 1.55, 2.0):
        a1.add_patch(Circle((xq, 1.5), 0.17, fc=ORANGE_L, ec=ORANGE, lw=1.2))
    a1.text(1.55, 2.05, "cola: $L_q$, $W_q$", ha="center", fontsize=9.5)
    arrow(a1, (2.35, 1.5), (2.75, 1.5), color=INK, lw=1.6)
    a1.add_patch(Circle((3.2, 1.5), 0.42, fc=BLUE_L, ec=BLUE, lw=1.6))
    a1.text(3.2, 1.5, "μ", ha="center", va="center", fontsize=14, color=BLUE)
    a1.text(3.2, 2.1, "servidor", ha="center", fontsize=9.5)
    arrow(a1, (3.65, 1.5), (4.2, 1.5), color=INK, lw=1.6)
    a1.text(2.2, 0.5, "sistema: $L$, $W$ (cola + servicio)", ha="center", fontsize=9.5)
    a1.plot([0.75, 3.7], [0.85, 0.85], color=MUTED, lw=0.9)
    a1.plot([0.75, 0.75], [0.8, 0.9], color=MUTED, lw=0.9)
    a1.plot([3.7, 3.7], [0.8, 0.9], color=MUTED, lw=0.9)
    a1.text(2.2, 2.65, "$\\rho = \\lambda/\\mu = \\lambda\\,E[s]$", ha="center", fontsize=10)

    r = np.linspace(0, 0.95, 400)
    a2.plot(r, r / (1 - r), color=BLUE, lw=2, label="$L = \\rho/(1-\\rho)$")
    a2.plot(r, r ** 2 / (1 - r), color=ORANGE, lw=2, label="$L_q = \\rho^2/(1-\\rho)$")
    p = 2 / 3
    a2.scatter([p, p], [2, 4 / 3], color=[BLUE, ORANGE], zorder=4, s=30)
    a2.axvline(p, color=GRID, lw=1, ls="--", zorder=0)
    a2.annotate("final 2025: ρ = 2/3\nL = 2,  $L_q$ = 1,33", xy=(p, 2), xytext=(0.2, 8.5),
                fontsize=9.5, arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.9))
    a2.set_xlim(0, 1.15)
    a2.set_ylim(0, 20)
    a2.axvline(1, color=RED, lw=1.2, ls="--")
    a2.axvspan(1, 1.15, color=RED_L, zorder=0)
    a2.text(1.075, 10, "ρ ≥ 1:\nse\nsatura", ha="center", va="center", fontsize=9,
            color=RED)
    a2.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    a2.yaxis.set_major_formatter(COMA_FMT)
    a2.set_xlabel("ρ (factor de utilización)")
    a2.set_ylabel("usuarios promedio")
    a2.xaxis.set_major_formatter(COMA_FMT)
    a2.grid(color=GRID, lw=0.7)
    a2.legend(frameon=False, fontsize=9.5, loc="upper left", bbox_to_anchor=(0.0, 1.0))
    save(fig, "cd-mm1.png")


if __name__ == "__main__":
    print("Figuras →", OUT)
    fig_sistema()
    fig_canal_binario()
    fig_entropias()
    fig_multinivel()
    fig_jerarquia()
    fig_huffman()
    fig_kraft()
    fig_hamming()
    fig_sindrome()
    fig_modulaciones()
    fig_constelacion()
    fig_pcm()
    fig_trama_tdm()
    fig_espectro()
    fig_fdm_tdm_adsl()
    fig_medio_acceso()
    fig_mm1()
