#!/usr/bin/env python3
"""
sim-figs-parcial1.py — Figuras del resumen del parcial 1 de Simulación.

Genera en materias/SIM/figs/ los PNG p1-*.png que usa
materias/SIM/estudio/resumen-parcial1.md. Todo sale de datos fijos (Law,
Weitz, el parcial 2025) o de semillas fijas: correrlo dos veces da lo mismo.

Uso (desde la raíz del repo):
    .venv/bin/python scripts/sim/sim-figs-parcial1.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle

OUT = Path(__file__).resolve().parents[2] / "materias" / "SIM" / "figs"
OUT.mkdir(parents=True, exist_ok=True)

# ── estilo ────────────────────────────────────────────────────────────────
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
    """Número con coma decimal."""
    return f"{x:.{d}f}".replace(".", ",")


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


# ═════════════════════════════════════════════════════════════════════════
# 1. Formas de estudiar un sistema
# ═════════════════════════════════════════════════════════════════════════
def fig_arbol():
    fig, ax = canvas(10, 5.2)
    nodes = {
        "sis": (5.0, 4.7, "Sistema"),
        "real": (2.4, 3.55, "Experimentar con\nel sistema real"),
        "mod": (7.6, 3.55, "Experimentar con\nun modelo"),
        "fis": (5.6, 2.35, "Modelo físico"),
        "mat": (9.0, 2.35, "Modelo matemático"),
        "ana": (7.3, 1.05, "Solución analítica"),
        "simu": (9.6 - 0.1, 1.05, "SIMULACIÓN"),
    }
    path = {"sis", "mod", "mat", "simu"}
    edges = [("sis", "real"), ("sis", "mod"), ("mod", "fis"), ("mod", "mat"),
             ("mat", "ana"), ("mat", "simu")]
    for a, b in edges:
        xa, ya, _ = nodes[a]
        xb, yb, _ = nodes[b]
        on = a in path and b in path
        arrow(ax, (xa, ya - 0.33), (xb, yb + 0.33), color=BLUE if on else MUTED,
              lw=2.2 if on else 1.2)
    for k, (x, y, t) in nodes.items():
        on = k in path
        w = 1.75 if k != "simu" else 1.5
        box(ax, x, y, w, 0.62, t, fc=BLUE_L if on else GRAY_L,
            ec=BLUE if on else MUTED, weight="bold" if on else "normal",
            color=BLUE if k == "simu" else INK)
    notes = [
        (2.4, 2.85, "Ideal, pero rara vez factible:\ncaro, riesgoso o el sistema\ntodavía no existe", MUTED),
        (5.6, 1.72, "Maquetas, simuladores de vuelo.\nPoco usados en IO", MUTED),
        (5.75, 0.3, "Fórmulas cerradas: resultado EXACTO.\nSi existe y es eficiente, se usa (ej. M/M/1)", GREEN),
        (9.45, 0.3, "Evalúa el modelo numéricamente:\nda ESTIMACIONES (cada corrida\nes una muestra)", BLUE),
    ]
    for x, y, t, c in notes:
        ax.text(x, y, t, ha="center", va="center", fontsize=8.6, color=c,
                style="italic", linespacing=1.3)
    ax.set_xlim(0.8, 10.6)
    ax.set_ylim(-0.25, 5.1)
    save(fig, "p1-arbol-estudio.png")


# ═════════════════════════════════════════════════════════════════════════
# 2. Motor de un simulador DES (flujo de control)
# ═════════════════════════════════════════════════════════════════════════
def fig_motor_des():
    fig, ax = canvas(10, 6.2)
    box(ax, 1.4, 5.6, 1.3, 0.5, "Inicio", fc="white", ec=INK, r=0.25, weight="bold")
    box(ax, 1.9, 4.25, 3.1, 1.25,
        "Rutina de inicialización\n1. reloj = 0\n2. estado y contadores en 0\n3. carga la lista de eventos",
        fc=GRAY_L, size=8.8)
    box(ax, 5.0, 4.25, 2.3, 1.25,
        "PROGRAMA\nPRINCIPAL\n0. inicializa\n1. llama a temporización\n2. llama a la rutina del evento",
        fc=BLUE_L, ec=BLUE, size=8.6, weight="normal")
    box(ax, 8.35, 5.15, 2.9, 1.0,
        "Rutina de temporización\n1. elige el PRÓXIMO evento\n2. SALTA el reloj a ese instante",
        fc=PURPLE_L, ec=PURPLE, size=8.8)
    box(ax, 8.35, 3.3, 2.9, 1.3,
        "Rutina del evento i\n1. actualiza el estado\n2. actualiza contadores\n3. programa eventos futuros",
        fc=ORANGE_L, ec=ORANGE, size=8.8)
    box(ax, 8.35, 1.55, 2.9, 0.85,
        "Rutinas de librería\ngeneran las variables aleatorias",
        fc=GREEN_L, ec=GREEN, size=8.8)
    # rombo
    dx, dy = 5.0, 2.15
    ax.add_patch(plt.Polygon([[dx, dy + 0.55], [dx + 1.05, dy], [dx, dy - 0.55], [dx - 1.05, dy]],
                             fc="white", ec=INK, lw=1.2))
    ax.text(dx, dy, "¿Terminó la\nsimulación?", ha="center", va="center", fontsize=8.8)
    box(ax, 1.9, 2.15, 3.0, 0.95,
        "Generador de reportes\n1. calcula las estimaciones\n2. escribe el reporte",
        fc=GRAY_L, size=8.8)
    box(ax, 1.9, 0.75, 1.3, 0.5, "Fin", fc="white", ec=INK, r=0.25, weight="bold")

    arrow(ax, (1.4, 5.35), (1.6, 4.9))
    arrow(ax, (3.45, 4.25), (3.85, 4.25), style="<|-|>")
    arrow(ax, (6.15, 4.6), (6.9, 4.95), style="<|-|>", color=PURPLE)
    arrow(ax, (6.15, 3.95), (6.9, 3.45), style="<|-|>", color=ORANGE)
    arrow(ax, (8.35, 2.65), (8.35, 1.98), style="<|-|>", color=GREEN)
    arrow(ax, (5.0, 3.62), (5.0, 2.72))
    arrow(ax, (3.95, 2.15), (3.42, 2.15))
    arrow(ax, (1.9, 1.67), (1.9, 1.0))
    ax.text(3.7, 2.35, "Sí", fontsize=9, color=INK, weight="bold")
    # bucle No
    arrow(ax, (6.05, 2.15), (6.6, 2.15), style="-")
    arrow(ax, (6.6, 2.15), (6.6, 5.45), style="-", shrinkB=0)
    arrow(ax, (6.6, 5.45), (6.9, 5.45), style="-|>", shrinkA=0)
    ax.text(6.25, 2.3, "No", fontsize=9, weight="bold")
    ax.text(6.55, 0.62,
            "El reloj NO avanza de a pasos fijos: salta de evento en evento.\n"
            "Entre dos eventos no pasa nada, así que no hace falta simular ese tiempo.",
            ha="center", fontsize=8.8, color=MUTED, style="italic")
    ax.set_xlim(0.2, 10)
    ax.set_ylim(0.1, 6.0)
    save(fig, "p1-motor-des.png")


# ═════════════════════════════════════════════════════════════════════════
# 3. Cola simple: esquema + diagrama de desencadenamiento de eventos
# ═════════════════════════════════════════════════════════════════════════
def fig_cola_esquema():
    fig, ax = canvas(11, 4.4)
    # llegadas
    ax.text(0.9, 3.35, "Llegadas", ha="center", weight="bold")
    ax.text(0.9, 2.95, "tiempo entre arribos\n$A_i$ (exógena)", ha="center",
            fontsize=8.5, color=MUTED)
    for k, x in enumerate([0.45, 0.9, 1.35]):
        ax.add_patch(Circle((x, 2.3), 0.15, fc=GRAY_L, ec=MUTED))
    arrow(ax, (1.65, 2.3), (2.25, 2.3), lw=1.8)
    # cola
    ax.add_patch(Rectangle((2.3, 1.95), 2.3, 0.7, fc="white", ec=INK, lw=1.3))
    for x in [2.6, 3.1, 3.6]:
        ax.add_patch(Circle((x, 2.3), 0.18, fc=ORANGE_L, ec=ORANGE, lw=1.2))
    ax.text(3.45, 3.0, "Cola (FIFO)", ha="center", weight="bold")
    ax.text(3.45, 1.55, "esperan acá: su DEMORA\nes el tiempo en cola", ha="center",
            fontsize=8.5, color=ORANGE)
    arrow(ax, (4.65, 2.3), (5.2, 2.3), lw=1.8)
    # servidor
    ax.add_patch(Circle((5.75, 2.3), 0.52, fc=BLUE_L, ec=BLUE, lw=1.6))
    ax.add_patch(Circle((5.75, 2.3), 0.18, fc=BLUE, ec=BLUE))
    ax.text(5.75, 3.15, "Servidor", ha="center", weight="bold")
    ax.text(5.75, 1.35, "tiempo de servicio\n$S_i$ (exógena)", ha="center",
            fontsize=8.5, color=BLUE)
    arrow(ax, (6.3, 2.3), (6.9, 2.3), lw=1.8)
    ax.text(6.6, 2.62, "Salida", ha="center", weight="bold")
    # estado
    box(ax, 3.55, 0.45, 6.6, 0.55,
        "ESTADO:  servidor libre/ocupado (0/1)  ·  nº en cola  ·  tiempos de arribo de los que esperan",
        fc=GRAY_L, size=8.5)

    # desencadenamiento
    ax.text(9.4, 4.15, "Qué evento programa a cuál", ha="center", weight="bold", size=10)
    a = (8.3, 2.45)
    d = (10.45, 2.45)
    ax.add_patch(Circle(a, 0.5, fc=ORANGE_L, ec=ORANGE, lw=1.6))
    ax.add_patch(Circle(d, 0.5, fc=BLUE_L, ec=BLUE, lw=1.6))
    ax.text(*a, "ARRIBO", ha="center", va="center", weight="bold", size=8.6)
    ax.text(*d, "PARTIDA", ha="center", va="center", weight="bold", size=8.6)
    arrow(ax, (8.0, 2.9), (8.6, 2.9), rad=-1.6, color=ORANGE, lw=1.5)
    ax.text(8.3, 3.75, "siempre programa\nel próximo arribo", ha="center", fontsize=8, color=ORANGE)
    arrow(ax, (8.8, 2.45), (9.95, 2.45), color=INK, lw=1.5)
    ax.text(9.38, 2.05, "si el servidor\nestaba libre", ha="center", fontsize=8)
    arrow(ax, (10.15, 2.0), (10.75, 2.0), rad=1.6, color=BLUE, lw=1.5)
    ax.text(10.45, 1.05, "si queda gente\nen cola, programa\nla siguiente partida", ha="center",
            fontsize=8, color=BLUE)
    ax.set_xlim(0.1, 11.25)
    ax.set_ylim(0.05, 4.4)
    save(fig, "p1-cola-esquema.png")


# ═════════════════════════════════════════════════════════════════════════
# 4. Traza de Law: Gantt de clientes + Q(t) + B(t)
# ═════════════════════════════════════════════════════════════════════════
def fig_cola_traza():
    T = 8.6
    clientes = [  # (arribo, inicio servicio, fin servicio)
        (0.4, 0.4, 2.4), (1.6, 2.4, 3.1), (2.1, 3.1, 3.3), (3.8, 3.8, 4.9),
        (4.0, 4.9, 8.6), (5.6, 8.6, 9.2), (5.8, None, None), (7.2, None, None),
    ]
    q_steps = [(0, 0), (1.6, 1), (2.1, 2), (2.4, 1), (3.1, 0), (4.0, 1), (4.9, 0),
               (5.6, 1), (5.8, 2), (7.2, 3), (T, 3)]
    b_steps = [(0, 0), (0.4, 1), (3.3, 0), (3.8, 1), (T, 1)]

    fig, axs = plt.subplots(3, 1, figsize=(10, 7.4), sharex=True,
                            gridspec_kw={"height_ratios": [2.3, 1.25, 0.9], "hspace": 0.32})
    ax = axs[0]
    for i, (a, s, e) in enumerate(clientes, start=1):
        y = 9 - i
        s_draw = s if s is not None else T
        if s_draw > a:
            ax.add_patch(Rectangle((a, y - 0.3), min(s_draw, T) - a, 0.6, fc=ORANGE_L, ec=ORANGE, lw=1))
        if s is not None and s < T:
            ax.add_patch(Rectangle((s, y - 0.3), min(e, T) - s, 0.6, fc=BLUE_L, ec=BLUE, lw=1))
        ax.plot([a], [y], marker="v", color=INK, ms=6)
        if i <= 6:
            dly = (s if s is not None else T) - a
            ax.text(-0.15, y, f"cliente {i}", ha="right", va="center", fontsize=8.6)
            ax.text(a + max(dly, 0) / 2 if dly > 0.25 else a + 0.08, y + 0.42,
                    f"$D_{i}$ = {coma(dly, 1)}", fontsize=8, color=ORANGE,
                    ha="center" if dly > 0.25 else "left")
        else:
            ax.text(-0.15, y, f"cliente {i}", ha="right", va="center", fontsize=8.6, color=MUTED)
    ax.axvline(T, color=RED, ls="--", lw=1.2)
    ax.text(T - 0.05, 8.75, "fin: se completó la 6ª demora\n$T(6) = 8{,}6$", ha="right",
            fontsize=8.5, color=RED, va="top")
    ax.set_ylim(0.3, 8.9)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_title("Cada cliente: espera en cola (naranja) y servicio (azul). El triángulo marca el arribo.", loc="left", fontsize=10)
    ax.text(0.0, 0.55,
            r"$\hat d(6) = \frac{0 + 0{,}8 + 1{,}0 + 0 + 0{,}9 + 3{,}0}{6} = \frac{5{,}7}{6} = 0{,}95$"
            "   (promedio sobre CLIENTES)",
            fontsize=9.5, color=ORANGE)

    def step(axq, steps, color, fill, label, area, val, ymax):
        xs, ys = zip(*steps)
        axq.step(xs, ys, where="post", color=color, lw=1.8)
        axq.fill_between(xs, ys, step="post", color=fill, alpha=0.9)
        axq.set_ylim(0, ymax)
        axq.set_ylabel(label, rotation=0, ha="right", va="center", fontsize=10)
        axq.grid(axis="y", color=GRID)
        axq.text(0.1, ymax * 0.82, f"área = {area}   →   {val}", fontsize=9.5, color=color)

    step(axs[1], q_steps, ORANGE, ORANGE_L, "$Q(t)$\nen cola", "9,9",
         r"$\hat q(6) = 9{,}9 / 8{,}6 = 1{,}15$  (promedio sobre TIEMPO)", 3.9)
    axs[1].set_yticks([0, 1, 2, 3])
    step(axs[2], b_steps, BLUE, BLUE_L, "$B(t)$\nocupado", "7,7",
         r"$\hat u(6) = 7{,}7 / 8{,}6 = 0{,}90$", 1.45)
    axs[2].set_yticks([0, 1])
    axs[2].set_xlabel("tiempo simulado (minutos)")
    axs[2].set_xlim(0, 9.3)
    axs[2].set_xticks([0, 0.4, 1.6, 2.1, 2.4, 3.1, 3.3, 3.8, 4.0, 4.9, 5.6, 5.8, 7.2, 8.6])
    axs[2].set_xticklabels([coma(v, 1) for v in axs[2].get_xticks()], fontsize=7.5, rotation=55)
    for a_ in axs[1:]:
        a_.axvline(T, color=RED, ls="--", lw=1.2)
    save(fig, "p1-cola-traza.png")


# ═════════════════════════════════════════════════════════════════════════
# 5. Inventario: nivel I(t), I+, I-, pedido y demora
# ═════════════════════════════════════════════════════════════════════════
def fig_inventario_nivel():
    s, S = 30, 60
    steps = [(0, 60), (0.3, 40), (0.7, 25), (1.2, -5), (1.6, 30), (2.4, 5), (3.0, 5)]
    xs = np.array([p[0] for p in steps])
    ys = np.array([p[1] for p in steps])
    fig, ax = plt.subplots(figsize=(10, 5.0))
    ax.fill_between(xs, np.maximum(ys, 0), step="post", color=GREEN_L, label="$I^+(t)$: en depósito → costo $h$")
    ax.fill_between(xs, np.minimum(ys, 0), step="post", color=RED_L, label="$I^-(t)$: backlog → costo $\\pi$")
    ax.step(xs, ys, where="post", color=INK, lw=2, label="$I(t)$")
    ax.axhline(S, color=BLUE, ls="--", lw=1.1)
    ax.axhline(s, color=ORANGE, ls="--", lw=1.1)
    ax.axhline(0, color=MUTED, lw=0.8)
    ax.text(3.08, S + 1.8, "S = 60", color=BLUE, fontsize=9.5)
    ax.text(3.08, s + 1.8, "s = 30", color=ORANGE, fontsize=9.5)
    for m in [0, 1, 2]:
        ax.plot([m], [-10.8], marker="^", color=PURPLE, ms=9)
    ax.text(2.07, -10.8, "▲ = evaluación del inventario (inicio de cada mes)".replace("▲ = ", ""),
            color=PURPLE, fontsize=8.6, va="center")
    # pedido
    ax.annotate("mes 1: $I = 25 < s$\n→ pide $Z = S - I = 35$\ncosto $K + iZ$",
                xy=(1.0, 25), xytext=(0.55, 47), fontsize=8.8, color=INK,
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1))
    ax.annotate("", xy=(1.6, 8), xytext=(1.0, 8),
                arrowprops=dict(arrowstyle="<|-|>", color=PURPLE, lw=1.3))
    ax.text(1.42, 10.5, "demora L", ha="center", color=PURPLE, fontsize=8.6)
    ax.annotate("llega el pedido: primero\ncubre los 5 del backlog,\nentran 30", xy=(1.6, 30),
                xytext=(1.75, 46), fontsize=8.8,
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1))
    ax.annotate("la demanda de 30\nno alcanza: $I = -5$", xy=(1.3, -5), xytext=(0.35, -9.5),
                fontsize=8.8, color=RED, arrowprops=dict(arrowstyle="-|>", color=RED, lw=1))
    for x, d in [(0.3, 20), (0.7, 15), (1.2, 30), (2.4, 25)]:
        ax.text(x + 0.02, 62 if x < 1 else (35 if x == 2.4 else 22), f"−{d}", fontsize=8,
                color=MUTED)
    ax.set_xlim(-0.05, 3.35)
    ax.set_ylim(-13, 68)
    ax.set_xticks([0, 0.3, 0.7, 1, 1.2, 1.6, 2, 2.4, 3])
    ax.set_xticklabels([coma(v, 1) for v in [0, 0.3, 0.7, 1, 1.2, 1.6, 2, 2.4, 3]])
    ax.set_xlabel("tiempo (meses)")
    ax.set_ylabel("unidades")
    ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.72), fontsize=8.6, frameon=True, facecolor="white", edgecolor=GRID)
    ax.grid(axis="y", color=GRID)
    save(fig, "p1-inventario-nivel.png")


# ═════════════════════════════════════════════════════════════════════════
# 6. Inventario: los 4 eventos, prioridad y desencadenamiento
# ═════════════════════════════════════════════════════════════════════════
def fig_inventario_eventos():
    fig, ax = canvas(11, 4.6)
    evs = [
        (1.5, "1", "LLEGADA\nDE PEDIDO", GREEN, GREEN_L,
         "suma Z al inventario\n(primero cubre el backlog)\nno programa nada"),
        (4.2, "2", "DEMANDA", RED, RED_L,
         "genera el tamaño D\nresta D (puede quedar < 0)\nprograma la próxima demanda"),
        (6.9, "3", "FIN DE\nSIMULACIÓN", MUTED, GRAY_L,
         "en t = n meses\ncalcula los costos\npromedio y reporta"),
        (9.6, "4", "EVALUACIÓN", PURPLE, PURPLE_L,
         "¿I < s? → pide Z = S − I,\npaga K + iZ y programa\nla llegada en t + L.\nSiempre programa la\npróxima en t + 1"),
    ]
    for x, n, t, c, cl, desc in evs:
        ax.add_patch(Circle((x, 3.1), 0.68, fc=cl, ec=c, lw=1.8))
        ax.text(x, 3.1, t, ha="center", va="center", weight="bold", fontsize=8.6, color=INK)
        ax.add_patch(Circle((x - 0.6, 3.68), 0.2, fc=c, ec=c))
        ax.text(x - 0.6, 3.68, n, ha="center", va="center", color="white", weight="bold", fontsize=9)
        ax.text(x, 1.25, desc, ha="center", va="center", fontsize=8.4, linespacing=1.35)
    # desencadenamientos
    arrow(ax, (9.0, 3.65), (2.1, 3.65), rad=0.22, color=PURPLE, lw=1.4, ls="--")
    ax.text(5.55, 4.68, "si pidió: programa la llegada del pedido en t + L", ha="center",
            fontsize=8.3, color=PURPLE)
    arrow(ax, (3.75, 2.62), (4.65, 2.62), rad=1.5, color=RED, lw=1.3)
    arrow(ax, (10.2, 3.45), (10.2, 2.75), rad=-1.5, color=PURPLE, lw=1.3)
    ax.text(5.5, 0.25,
            "Los números en los círculos son la PRIORIDAD cuando dos eventos caen en el mismo instante. "
            "En t = n coinciden fin (3) y evaluación (4):\n"
            "va primero el fin, para no hacer un pedido que no llegaría a contabilizarse.",
            ha="center", fontsize=8.4, color=MUTED, style="italic")
    ax.set_xlim(0.4, 11.0)
    ax.set_ylim(-0.1, 5.0)
    save(fig, "p1-inventario-eventos.png")


# ═════════════════════════════════════════════════════════════════════════
# 7. Inventario: salida de Law (9 políticas) — costos apilados
# ═════════════════════════════════════════════════════════════════════════
def fig_inventario_tradeoff():
    data = [
        ("(20,40)", 126.61, 99.26, 9.25, 18.10), ("(20,60)", 122.74, 90.52, 17.39, 14.83),
        ("(20,80)", 123.86, 87.36, 26.24, 10.26), ("(20,100)", 125.32, 81.37, 36.00, 7.95),
        ("(40,60)", 126.37, 98.43, 25.99, 1.95), ("(40,80)", 125.46, 88.40, 35.92, 1.14),
        ("(40,100)", 132.34, 84.62, 46.42, 1.30), ("(60,80)", 150.02, 105.69, 44.02, 0.31),
        ("(60,100)", 143.20, 89.05, 53.91, 0.24),
    ]
    labels = [d[0] for d in data]
    tot = np.array([d[1] for d in data])
    ped = np.array([d[2] for d in data])
    man = np.array([d[3] for d in data])
    fal = np.array([d[4] for d in data])
    x = np.arange(len(data))
    fig, ax = plt.subplots(figsize=(10, 4.9))
    ax.bar(x, ped, color="#93c5fd", label="pedido (K + iZ)")
    ax.bar(x, man, bottom=ped, color="#86efac", label="mantenimiento (h)")
    ax.bar(x, fal, bottom=ped + man, color="#fca5a5", label="faltante (π)")
    for i, t in enumerate(tot):
        best = i == 1
        ax.text(i, t + 2, coma(t), ha="center", fontsize=8.8, weight="bold" if best else "normal",
                color=BLUE if best else INK)
    ax.annotate("menor costo: (20, 60)\npero es UNA sola corrida:\ncon otros números aleatorios\nel orden podría cambiar",
                xy=(1.3, 127), xytext=(4.35, 163), fontsize=8.8, color=BLUE,
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1))
    for xx in [3.5, 6.5]:
        ax.axvline(xx, color=GRID, lw=1)
    ax.text(1.5, -24, "s = 20: al subir S, sube mantenimiento\ny bajan faltante y pedido", ha="center", fontsize=8.4, color=MUTED)
    ax.text(5.0, -24, "s = 40", ha="center", fontsize=8.4, color=MUTED)
    ax.text(7.5, -24, "s = 60: casi nunca falta,\npero se guarda de más", ha="center", fontsize=8.4, color=MUTED)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_xlabel("política (s, S)", labelpad=34)
    ax.set_ylabel("costo promedio por mes ($)")
    ax.set_ylim(0, 190)
    ax.legend(loc="upper left", fontsize=8.6, frameon=False, ncol=1)
    ax.grid(axis="y", color=GRID)
    ax.set_axisbelow(True)
    save(fig, "p1-inventario-politicas.png")


# ═════════════════════════════════════════════════════════════════════════
# 8. Proceso de Poisson homogéneo y no homogéneo
# ═════════════════════════════════════════════════════════════════════════
def fig_poisson():
    rng = np.random.default_rng(7)
    lam, Tm = 1.2, 12
    t, ev = 0.0, []
    while True:
        t += rng.exponential(1 / lam)
        if t > Tm:
            break
        ev.append(t)
    ev = np.array(ev)

    def lam_t(x):
        return 0.4 + 2.6 * np.exp(-((x - 6.5) ** 2) / 4.0)

    lmax = 3.0
    t, ev2 = 0.0, []
    while True:  # thinning (Lewis-Shedler)
        t += rng.exponential(1 / lmax)
        if t > Tm:
            break
        if rng.random() <= lam_t(t) / lmax:
            ev2.append(t)
    ev2 = np.array(ev2)

    fig, axs = plt.subplots(3, 1, figsize=(10, 6.6), sharex=True,
                            gridspec_kw={"height_ratios": [0.9, 1.5, 1.6], "hspace": 0.45})
    ax = axs[0]
    ax.axhline(0, color=MUTED, lw=1)
    ax.plot(ev, np.zeros_like(ev), "|", ms=18, mew=2, color=BLUE)
    for k in range(4):
        a = 0 if k == 0 else ev[k - 1]
        b = ev[k]
        ax.annotate("", xy=(b, 0.45), xytext=(a, 0.45),
                    arrowprops=dict(arrowstyle="<|-|>", color=ORANGE, lw=1))
        ax.text((a + b) / 2, 0.62, f"$X_{k + 1}$", ha="center", fontsize=9, color=ORANGE)
    ax.text(ev[4] + 0.2, 0.5, "tiempos entre eventos: exponenciales i.i.d. de media 1/λ  (NO Poisson)",
            fontsize=8.8, color=ORANGE, va="center")
    ax.set_ylim(-0.6, 1.0)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_title(f"Homogéneo, λ = {coma(lam, 1)}: los eventos llegan de a uno, a ritmo parejo", loc="left")

    ax = axs[1]
    xs = np.concatenate([[0], ev, [Tm]])
    ys = np.concatenate([[0], np.arange(1, len(ev) + 1), [len(ev)]])
    ax.step(xs, ys, where="post", color=BLUE, lw=1.8, label="N(t): eventos hasta t")
    ax.plot([0, Tm], [0, lam * Tm], ls="--", color=MUTED, lw=1, label="E[N(t)] = λt")
    ax.legend(loc="upper left", fontsize=8.6, frameon=False)
    ax.text(Tm * 0.62, 2.0, "N(t) ~ Poisson(λt)   ·   N(0) = 0\nincrementos independientes y ESTACIONARIOS",
            fontsize=8.8, color=INK)
    ax.grid(axis="y", color=GRID)
    ax.set_ylabel("N(t)")

    ax = axs[2]
    xx = np.linspace(0, Tm, 400)
    ax.fill_between(xx, lam_t(xx), color=PURPLE_L)
    ax.plot(xx, lam_t(xx), color=PURPLE, lw=1.8, label="λ(t): intensidad que cambia con el tiempo")
    ax.plot(ev2, np.full_like(ev2, -0.25), "|", ms=14, mew=1.8, color=PURPLE)
    ax.set_ylim(-0.55, 3.4)
    ax.set_title("No homogéneo: más eventos donde λ(t) es alta (ej. la hora pico de un banco)", loc="left")
    ax.text(0.2, 2.55,
            "se pierde SOLO la estacionariedad;\nlos incrementos siguen siendo independientes\n"
            "N(t+s) − N(t) ~ Poisson( m(t+s) − m(t) ),  m(t) = ∫ λ",
            fontsize=8.8, color=PURPLE)
    ax.set_xlabel("tiempo")
    ax.set_ylabel("λ(t)")
    ax.grid(axis="y", color=GRID)
    save(fig, "p1-poisson.png")


# ═════════════════════════════════════════════════════════════════════════
# 9. M/M/1: explosión de Lq cuando ρ → 1 y distribución de Pn
# ═════════════════════════════════════════════════════════════════════════
def fig_mm1():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 3.9), gridspec_kw={"width_ratios": [1.45, 1]})
    r = np.linspace(0.0, 0.965, 300)
    a1.plot(r, r / (1 - r), color=BLUE, lw=2, label="L = ρ/(1−ρ)  (en el sistema)")
    a1.plot(r, r ** 2 / (1 - r), color=ORANGE, lw=2, label="Lq = ρ²/(1−ρ)  (en cola)")
    a1.axvspan(1.0, 1.15, color=RED_L)
    a1.axvline(1.0, color=RED, lw=1.2, ls="--")
    a1.text(1.075, 16, "ρ ≥ 1\nsin estado\nestable", ha="center", fontsize=8.6, color=RED)
    for rr in [0.5, 0.75, 0.9]:
        a1.plot([rr], [rr / (1 - rr)], "o", color=BLUE, ms=4)
        a1.text(rr - 0.02, rr / (1 - rr) + 1.0, f"ρ={coma(rr, 2)}: L={coma(rr / (1 - rr), 1)}",
                fontsize=8, ha="right", color=BLUE)
    a1.set_xlim(0, 1.15)
    a1.set_ylim(0, 25)
    a1.set_xlabel("ρ = λ/μ  (intensidad de tráfico = utilización)")
    a1.set_ylabel("clientes promedio")
    a1.legend(loc="upper left", fontsize=8.6, frameon=False)
    a1.grid(color=GRID)
    a1.set_title("Cuanto más cerca de 1, la cola explota", loc="left")

    rho = 0.75
    n = np.arange(0, 13)
    p = (1 - rho) * rho ** n
    a2.bar(n, p, color=[GREEN if k == 0 else "#93c5fd" for k in n])
    a2.text(1.0, 0.215, r"$P_0 = 1-\rho = 0{,}25$" "\n(sistema vacío)", fontsize=8.5, color=GREEN)
    a2.set_title(r"$P_n = (1-\rho)\,\rho^n$ con $\rho = 0{,}75$", loc="left")
    a2.set_xticks(range(0, 13, 2))
    a2.set_xlabel("n clientes en el sistema")
    a2.set_ylabel("probabilidad")
    a2.grid(axis="y", color=GRID)
    a2.set_axisbelow(True)
    save(fig, "p1-mm1.png")


# ═════════════════════════════════════════════════════════════════════════
# 10. Transformada inversa: continua (exponencial) y discreta (demanda 2025)
# ═════════════════════════════════════════════════════════════════════════
def fig_inversa():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.0))
    m = 0.55
    x = np.linspace(0, 2.6, 300)
    a1.plot(x, 1 - np.exp(-x / m), color=BLUE, lw=2)
    u = 0.75
    xu = -m * np.log(1 - u)
    a1.annotate("", xy=(xu, u), xytext=(0, u), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.5))
    a1.annotate("", xy=(xu, 0), xytext=(xu, u), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.5))
    a1.text(0.04, u + 0.04, "1) sorteo u ~ U(0,1)", color=ORANGE, fontsize=8.8)
    a1.text(xu + 0.06, 0.12, "2) $x = F^{-1}(u)$\n   = −0,55·ln(1−u)\n   = " + coma(xu), color=ORANGE, fontsize=8.8)
    a1.set_title("Continua: exponencial de media 0,55", loc="left")
    a1.set_xlabel("x (tiempo entre demandas)")
    a1.set_ylabel("F(x) = P(X ≤ x)")
    a1.set_ylim(0, 1.05)
    a1.grid(color=GRID)

    vals = [3, 4, 5, 6]
    probs = [1 / 3, 1 / 6, 1 / 6, 1 / 3]
    cum = np.cumsum(probs)
    cols = ["#bfdbfe", "#bbf7d0", "#fde68a", "#fecaca"]
    lo = 0
    for v, c, col in zip(vals, cum, cols):
        a2.add_patch(Rectangle((0, lo), 0.95, c - lo, fc=col, ec="white"))
        a2.text(0.475, (lo + c) / 2, f"[{coma(lo, 3)} ; {coma(c, 3)})", ha="center", va="center", fontsize=8.3)
        a2.annotate("", xy=(1.55, (lo + c) / 2), xytext=(1.0, (lo + c) / 2),
                    arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1))
        a2.text(1.62, (lo + c) / 2, f"D = {v}", va="center", fontsize=10, weight="bold")
        lo = c
    r = 0.3546
    a2.plot([0, 0.95], [r, r], color=RED, lw=2)
    a2.text(2.25, r, "r = 0,3546 cae en el\n2º tramo → D = 4\n(números del parcial 2025)", fontsize=8.6,
            color=RED, va="center")
    a2.set_xlim(0, 3.6)
    a2.set_ylim(0, 1)
    a2.set_xticks([])
    a2.set_ylabel("r ~ U(0,1)")
    a2.spines["bottom"].set_visible(False)
    a2.set_title("Discreta: se parte [0,1) según la acumulada", loc="left")
    save(fig, "p1-transformada-inversa.png")


# ═════════════════════════════════════════════════════════════════════════
# 11. TCL: suma de uniformes → normal
# ═════════════════════════════════════════════════════════════════════════
def fig_tcl():
    rng = np.random.default_rng(3)
    fig, axs = plt.subplots(1, 3, figsize=(10, 2.9), sharey=False)
    for ax, n in zip(axs, [1, 2, 12]):
        sm = rng.random((60000, n)).sum(axis=1)
        z = (sm - n / 2) / np.sqrt(n / 12)
        ax.hist(z, bins=60, density=True, color="#93c5fd", ec="white", lw=0.3)
        xx = np.linspace(-4, 4, 200)
        ax.plot(xx, np.exp(-xx ** 2 / 2) / np.sqrt(2 * np.pi), color=RED, lw=1.6)
        ax.set_title(f"suma de {n} uniforme{'s' if n > 1 else ''}", loc="left", fontsize=10)
        ax.set_xlim(-4, 4)
        ax.set_yticks([])
        ax.spines["left"].set_visible(False)
    axs[2].text(1.3, 0.33, "ya es casi\nnormal", color=RED, fontsize=8.8)
    fig.suptitle("TCL: la suma (o el promedio) de muchas VA i.i.d. se aproxima a una normal, "
                 "SEA CUAL SEA su distribución", fontsize=10, x=0.02, ha="left", y=1.04)
    save(fig, "p1-tcl.png")


# ═════════════════════════════════════════════════════════════════════════
# 12. Los 10 pasos de Weitz + verificación vs validación
# ═════════════════════════════════════════════════════════════════════════
def fig_pasos():
    fig, ax = canvas(11, 5.6)
    pasos = ["Definición del\nsistema", "Modelo de\nsimulación BASE", "Recolección y\nanálisis de datos",
             "Modelo\npreliminar", "VERIFICACIÓN", "VALIDACIÓN", "Modelo\nfinal",
             "Determinación\nde escenarios", "Análisis de\nsensibilidad", "Documentación y\nconclusiones"]
    pos = [(1.0 + 2.1 * i, 4.55) for i in range(5)] + [(1.0 + 2.1 * (4 - i), 2.75) for i in range(5)]
    for i, ((x, y), t) in enumerate(zip(pos, pasos), start=1):
        hi = i in (5, 6)
        c, cl = (ORANGE, ORANGE_L) if i == 5 else ((GREEN, GREEN_L) if i == 6 else (BLUE, BLUE_L))
        box(ax, x, y, 1.8, 0.85, t, fc=cl, ec=c, size=8.6, weight="bold" if hi else "normal")
        ax.add_patch(Circle((x - 0.82, y + 0.38), 0.17, fc=c, ec=c))
        ax.text(x - 0.82, y + 0.38, str(i), ha="center", va="center", color="white", fontsize=8, weight="bold")
    for i in range(4):
        arrow(ax, (pos[i][0] + 0.92, 4.55), (pos[i + 1][0] - 0.92, 4.55))
        arrow(ax, (pos[5 + i][0] - 0.92, 2.75), (pos[6 + i][0] + 0.92, 2.75))
    arrow(ax, (pos[4][0], 4.1), (pos[5][0], 3.2))
    # retornos
    arrow(ax, (pos[4][0] - 0.3, 4.98), (pos[3][0] + 0.3, 4.98), rad=0.5, color=ORANGE, ls="--", lw=1.2)
    arrow(ax, (pos[5][0] + 0.95, 2.6), (pos[3][0] + 0.6, 4.1), rad=0.35, color=GREEN, ls="--", lw=1.2)
    ax.text(pos[3][0] + 1.05, 5.55, "si falla, se corrige", fontsize=8, color=ORANGE, ha="center")
    ax.text(10.75, 3.6, "si no representa\nla realidad,\nse vuelve atrás", fontsize=8, color=GREEN, ha="right")
    ax.text(pos[1][0], 3.72, "los datos todavía\nno importan", fontsize=7.8, color=MUTED, ha="center", style="italic")
    ax.text(pos[7][0], 2.0, "optimista, pesimista\ne intermedio", fontsize=7.8, color=MUTED, ha="center", style="italic")
    ax.text(pos[8][0], 2.0, "¿diferencia estadísticamente\nsignificativa? (IC)", fontsize=7.8, color=MUTED, ha="center", style="italic")
    ax.text(pos[6][0], 2.0, "modelo raíz para\ncomparar escenarios", fontsize=7.8, color=MUTED, ha="center", style="italic")

    # V&V
    y = 0.75
    box(ax, 1.4, y, 2.0, 0.75, "Sistema real", fc=GRAY_L, weight="bold")
    box(ax, 5.3, y, 2.4, 0.75, "Modelo conceptual\n(supuestos)", fc=GRAY_L, weight="bold")
    box(ax, 9.3, y, 2.2, 0.75, "Programa\n(modelo en la compu)", fc=GRAY_L, weight="bold")
    arrow(ax, (2.45, y), (4.05, y), style="<|-|>", color=GREEN, lw=2)
    arrow(ax, (6.55, y), (8.15, y), style="<|-|>", color=ORANGE, lw=2)
    ax.text(3.25, y + 0.5, "VALIDACIÓN", ha="center", color=GREEN, weight="bold", fontsize=9)
    ax.text(3.25, y - 0.62, "¿el modelo representa\nla realidad?", ha="center", color=GREEN, fontsize=8.2)
    ax.text(7.35, y + 0.5, "VERIFICACIÓN", ha="center", color=ORANGE, weight="bold", fontsize=9)
    ax.text(7.35, y - 0.62, "¿el programa hace lo\nque quise programar?", ha="center", color=ORANGE, fontsize=8.2)
    ax.set_xlim(-0.05, 10.9)
    ax.set_ylim(-0.25, 5.75)
    save(fig, "p1-pasos-weitz.png")


# ═════════════════════════════════════════════════════════════════════════
# 13. Notación de Kendall
# ═════════════════════════════════════════════════════════════════════════
def fig_kendall():
    fig, ax = canvas(10, 2.6)
    parts = [("M", "llegadas\n(tiempo entre arribos)", BLUE), ("M", "servicio\n(tiempo de atención)", ORANGE),
             ("c", "nº de servidores\nen paralelo", GREEN), ("K", "capacidad máxima\ndel SISTEMA", PURPLE),
             ("N", "tamaño de la\npoblación", RED)]
    xs = [1.0, 3.0, 5.0, 7.0, 9.0]
    for i, (x, (sym, txt, c)) in enumerate(zip(xs, parts)):
        ax.text(x, 1.9, sym, ha="center", va="center", fontsize=26, weight="bold", color=c)
        ax.text(x, 0.85, txt, ha="center", va="center", fontsize=8.8)
        if i < 4:
            ax.text(x + 1.0, 1.9, "/", ha="center", va="center", fontsize=24, color=MUTED)
    ax.text(5.0, 0.12, "M = exponencial (markoviana) · D = determinística · G = general.   "
            "Si se omiten K y N, son infinitos:  M/M/1 = M/M/1/∞/∞",
            ha="center", fontsize=8.8, color=MUTED, style="italic")
    save(fig, "p1-kendall.png")


# ═════════════════════════════════════════════════════════════════════════
# 14. AnyLogic: tres paradigmas según el nivel de abstracción
# ═════════════════════════════════════════════════════════════════════════
def fig_anylogic_paradigmas():
    fig, ax = canvas(11, 5.4)
    # eje
    arrow(ax, (0.55, 0.5), (0.55, 4.9), color=INK, lw=1.6)
    ax.text(0.35, 4.85, "ALTA abstracción\nagregados, estratégico", ha="left", va="bottom", fontsize=8.4, weight="bold")
    ax.text(0.35, 0.35, "BAJA abstracción\ndetalle físico", ha="left", va="top", fontsize=8.4, weight="bold")
    ax.text(0.25, 2.7, "media", rotation=90, va="center", fontsize=8.4, color=MUTED)
    # SD
    ax.add_patch(FancyBboxPatch((1.2, 3.5), 2.9, 1.35, boxstyle="round,pad=0,rounding_size=0.1",
                                fc=GREEN_L, ec=GREEN, lw=1.5))
    ax.text(2.65, 4.62, "Dinámica de sistemas (SD)", ha="center", weight="bold", fontsize=9.5, color=GREEN)
    ax.add_patch(Rectangle((1.45, 3.75), 0.6, 0.45, fc="white", ec=GREEN))
    ax.text(1.75, 3.97, "stock", ha="center", va="center", fontsize=7.5)
    arrow(ax, (2.05, 3.97), (2.75, 3.97), color=GREEN, lw=2.2)
    ax.text(2.4, 4.12, "flujo", ha="center", fontsize=7.2, color=GREEN)
    ax.add_patch(Rectangle((2.75, 3.75), 0.6, 0.45, fc="white", ec=GREEN))
    ax.text(3.05, 3.97, "stock", ha="center", va="center", fontsize=7.5)
    ax.text(2.4, 3.6, "con lazos de realimentación", ha="center", fontsize=7.2, color=GREEN)
    # DES
    ax.add_patch(FancyBboxPatch((1.2, 0.6), 2.9, 2.55, boxstyle="round,pad=0,rounding_size=0.1",
                                fc=BLUE_L, ec=BLUE, lw=1.5))
    ax.text(2.65, 2.9, "Eventos discretos (DES)", ha="center", weight="bold", fontsize=9.5, color=BLUE)
    for i, t in enumerate(["Source", "Queue", "Delay", "Sink"]):
        y = 2.5 - i * 0.42
        box(ax, 2.65, y, 1.1, 0.3, t, fc="white", ec=BLUE, size=7.6, r=0.05)
        if i < 3:
            arrow(ax, (2.65, y - 0.15), (2.65, y - 0.3), color=BLUE, lw=1, ms=8)
    ax.text(2.65, 0.8, "procesos: entidades que\ncompiten por recursos", ha="center", fontsize=7.6, color=BLUE)
    # ABM
    ax.add_patch(FancyBboxPatch((4.4, 0.6), 2.4, 4.25, boxstyle="round,pad=0,rounding_size=0.1",
                                fc=ORANGE_L, ec=ORANGE, lw=1.5))
    ax.text(5.6, 4.62, "Basado en agentes (ABM)", ha="center", weight="bold", fontsize=9.5, color=ORANGE)
    rng = np.random.default_rng(1)
    pts = rng.random((14, 2)) * [1.9, 2.3] + [4.65, 1.8]
    for k, (px, py) in enumerate(pts):
        ax.add_patch(Circle((px, py), 0.09, fc=ORANGE if k % 3 else "white", ec=ORANGE))
    for k in range(0, 12, 3):
        ax.plot(pts[k:k + 2, 0], pts[k:k + 2, 1], color=ORANGE, lw=0.6, alpha=0.6)
    ax.text(5.6, 1.0, "individuos con reglas propias\n(statecharts); el comportamiento\nglobal EMERGE",
            ha="center", fontsize=7.6, color=ORANGE)
    # textos laterales
    notas = [
        (4.25, "SD · desde los años 50 (Forrester, MIT)\nPoblaciones, mercados, epidemias. Los ítems\nson indistinguibles: solo cantidades.\nEn el libro: modelo SEIR (epidemia)."),
        (2.75, "ABM · cualquier nivel de abstracción\nAgentes: personas, vehículos, empresas, ideas.\nEn el libro: modelo de mercado (publicidad\ny boca en boca)."),
        (1.25, "DES · abstracción media y media-baja\nGPSS (Geoffrey Gordon, IBM, 1961) fue el primero.\nSalidas típicas: utilización, esperas, colas,\nthroughput, cuellos de botella. En el libro: Job Shop."),
    ]
    for y, t in notas:
        ax.text(7.05, y, t, fontsize=8.1, va="center", linespacing=1.35)
    ax.text(7.05, 0.2, "Peatones (Airport), Road Traffic, Rail, Fluid y Material Handling\n"
            "son BIBLIOTECAS, no paradigmas. GIS es un espacio (mapa multicapa).",
            fontsize=8.1, color=RED, va="center")
    ax.set_xlim(0, 11)
    ax.set_ylim(-0.15, 5.4)
    save(fig, "p1-anylogic-paradigmas.png")


# ═════════════════════════════════════════════════════════════════════════
# 15. AnyLogic: M/M/1 con la Process Modeling Library
# ═════════════════════════════════════════════════════════════════════════
def fig_anylogic_mm1():
    fig, ax = canvas(11, 3.4)
    blocks = [("Source", "genera llegadas\nexponential(λ)", GREEN),
              ("TimeMeasure\nStart", "marca la\nentrada", MUTED),
              ("Queue", "la cola\n(FIFO)", ORANGE),
              ("Seize", "TOMA un\nservidor", BLUE),
              ("Delay", "servicio\nexponential(μ)", BLUE),
              ("Release", "LIBERA el\nservidor", BLUE),
              ("TimeMeasure\nEnd", "tiempo en\nel sistema", MUTED),
              ("Sink", "salida", RED)]
    xs = np.linspace(0.75, 10.25, len(blocks))
    for i, (x, (t, d, c)) in enumerate(zip(xs, blocks)):
        box(ax, x, 2.25, 1.08, 0.7, t, fc="white", ec=c, size=8.3, weight="bold", lw=1.6)
        ax.text(x, 1.45, d, ha="center", va="center", fontsize=7.8, color=c if c != MUTED else INK)
        if i < len(blocks) - 1:
            arrow(ax, (x + 0.55, 2.25), (xs[i + 1] - 0.55, 2.25), ms=9)
    box(ax, (xs[3] + xs[5]) / 2, 3.2, 2.7, 0.45, "ResourcePool (capacidad = c)", fc=BLUE_L, ec=BLUE, size=8.0)
    arrow(ax, ((xs[3] + xs[5]) / 2 - 0.5, 2.98), (xs[3], 2.62), color=BLUE, ls="--", lw=1)
    arrow(ax, ((xs[3] + xs[5]) / 2 + 0.5, 2.98), (xs[5], 2.62), color=BLUE, ls="--", lw=1)
    ax.text(5.5, 0.45, "Seize + Delay + Release con un ResourcePool equivalen a un bloque Service. "
            "Las fórmulas de M/M/1 se usan para comparar con lo simulado.",
            ha="center", fontsize=8.3, color=MUTED, style="italic")
    ax.set_xlim(0.05, 10.95)
    ax.set_ylim(0.2, 3.55)
    save(fig, "p1-anylogic-mm1.png")


if __name__ == "__main__":
    print("Figuras →", OUT)
    fig_arbol()
    fig_motor_des()
    fig_cola_esquema()
    fig_cola_traza()
    fig_inventario_nivel()
    fig_inventario_eventos()
    fig_inventario_tradeoff()
    fig_poisson()
    fig_mm1()
    fig_inversa()
    fig_tcl()
    fig_pasos()
    fig_kendall()
    fig_anylogic_paradigmas()
    fig_anylogic_mm1()
