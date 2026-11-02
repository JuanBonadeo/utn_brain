#!/usr/bin/env python3
"""Diagrama de la estación Constitución tal como la representa el modelo: corte por el recorrido del pasajero del Roca
y planta esquemática por niveles. Escribe materias/SIM/figs/tpi-subte-estacion-niveles.png. Requiere matplotlib.

Medidas: las del modelo (02-modelo-anylogic.md, secciones del vestíbulo coherente y del subsuelo). Profundidades:
-4,60 m (pasillo y vestíbulo, plaza de transbordo, GCBA 2015) y -9,20 m (andenes de la Línea C, supuesto [SUP]); el resto sale del plano de Trenes Argentinos
georreferenciado con OpenStreetMap.
"""
import math
from pathlib import Path

AQUI = Path(__file__).resolve().parent
FIG = AQUI.parents[3] / 'figs' / 'tpi-subte-estacion-niveles.png'
C0, C1, C2 = '#e9e4d8', '#cfdcec', '#b9c9a8'       # nivel 0 (calle/hall), -1 (vestíbulo), -2 (andenes C)
ROCA, LINEAC, FLUJO = '#7a6a58', '#1f5fbf', '#d9531e'

# Hall: distancia en línea recta desde la cabecera de cada andén (X = -545) hasta la boca B2 (X = -152, Y = 974).
ANDENES_Y = [314, 489, 661, 837, 1009, 1181, 1326]
HALL = [math.dist((-545, y), (-152, 974)) / 10 for y in ANDENES_Y]


def corte(ax):
    import matplotlib.patches as mp
    # Tramos a lo largo del recorrido (m): andén, hall, escalera B2, pasillo, vestíbulo.
    x_anden, x_hall, x_esc, x_pas, x_ves = 0, 31, 31 + 55, 31 + 55 + 9, 31 + 55 + 9 + 75
    x_fin = x_ves + 50
    ax.add_patch(mp.Rectangle((-5, -1.2), x_fin + 10, 1.2, color='#d8d2c4'))                      # terreno calle
    ax.add_patch(mp.Rectangle((x_esc + 9, -6.2), x_fin - x_esc - 4, 1.2, color='#d8d2c4'))        # losa subsuelo
    ax.add_patch(mp.Rectangle((x_ves + 30, -11.2), 22, 1.2, color='#d8d2c4'))                      # andén C
    # Niveles (fondos).
    ax.add_patch(mp.Rectangle((-5, 0), x_esc + 5, 4, color=C0, alpha=.8))
    ax.add_patch(mp.Rectangle((x_esc + 9, -5), x_fin - x_esc - 9, 3.5, color=C1, alpha=.9))
    ax.add_patch(mp.Rectangle((x_ves + 30, -10), 22, 3.5, color=C2, alpha=.9))
    # Tren del Roca en el andén (vías hundidas 1,1 m).
    ax.add_patch(mp.Rectangle((-5, -1.1), 34, 4.0, color=ROCA, alpha=.85))
    ax.text(12, 1.0, 'tren del Roca', color='white', ha='center', va='center', fontsize=9)
    # Escalera B2: 9 m de largo, 5 m de desnivel.
    n = 12
    for i in range(n):
        ax.add_patch(mp.Rectangle((x_esc + 9 * i / n, -5 + 5 * (n - i - 1) / n), 9 / n, 5 / n + .02, color='#a89f92'))
    ax.plot([x_esc, x_esc + 9], [0, -5], color='#6b645a', lw=1)
    # Escaleras del vestíbulo a los andenes de la C y escalera B3 a la calle Brasil.
    for i in range(10):
        ax.add_patch(mp.Rectangle((x_ves + 30 - 8 + .8 * i, -5 - .5 * (i + 1)), .8, .5 * (i + 1) - .02 + 0, color='#a89f92'))
    for i in range(10):
        ax.add_patch(mp.Rectangle((x_ves + 2 + .8 * i, -5), .8, .5 * (i + 1), color='#a89f92'))
    ax.add_patch(mp.Rectangle((x_ves + 30, -10), 22, .6, color=LINEAC))
    # Molinetes.
    for k in range(4):
        ax.add_patch(mp.Rectangle((x_ves + 18 + .5 * k, -5), .25, 1.0, color='#444'))
    # Flujo del pasajero.
    pts = [(2, .9), (x_hall, .9), (x_esc, .9), (x_esc + 9, -4.1), (x_ves + 20, -4.1), (x_ves + 26, -4.1), (x_ves + 36, -9.1)]
    ax.plot(*zip(*pts), color=FLUJO, lw=2.2, ls='--')
    ax.annotate('', xy=pts[-1], xytext=(x_ves + 33, -7.9), arrowprops=dict(arrowstyle='-|>', color=FLUJO, lw=2))
    # Cotas y rótulos.
    def cota(x0, x1, y, txt):
        ax.annotate('', xy=(x0, y), xytext=(x1, y), arrowprops=dict(arrowstyle='<->', color='#333', lw=.8))
        ax.text((x0 + x1) / 2, y + .35, txt, ha='center', fontsize=8.5)
    cota(0, x_hall, 5.0, 'andén (se camina)\ndesde 21 puertas')
    cota(x_hall, x_esc, 5.0, f'hall del Roca (se camina)\n{min(HALL):.0f} a {max(HALL):.0f} m según el andén')
    cota(x_esc, x_esc + 9, 2.6, 'B2\n9 m')
    cota(x_esc + 9, x_ves, -0.6, 'pasillo (se camina), 75 m × 5 m')
    cota(x_ves + 12, x_ves + 50, -0.6, 'vestíbulo Línea C, 50 m')
    ax.text(x_esc + 11, -3.75, 'escalera B2 en pendiente: 0,59 m/s → 15,3 s', fontsize=8.5, va='bottom')
    ax.annotate('B3 desde la calle Brasil', xy=(x_ves + 6, -2.2), xytext=(x_ves + 6, 2.2), fontsize=8.5, ha='center',
                arrowprops=dict(arrowstyle='-', color='#777', lw=.7))
    ax.text(x_ves + 19, -3.5, 'molinetes', fontsize=8, ha='center')
    ax.text(x_ves + 41, -12.6, 'andenes Línea C', fontsize=8.5, ha='center', color=LINEAC)
    for y, t in ((0, 'nivel 0 · calle y hall'), (-5, 'nivel −1 · −4,60 m (GCBA)'), (-10, 'nivel −2 · −9,20 m [SUP]')):
        ax.axhline(y, color='#999', lw=.5, ls=':')
        ax.text(x_fin + 7, y + .2, t, fontsize=8.5, color='#555')
    ax.set_xlim(-8, x_fin + 40); ax.set_ylim(-13.4, 7.2); ax.set_aspect(2.2); ax.axis('off')
    ax.set_title('Corte por el recorrido del pasajero del Roca (escala vertical exagerada ×2,2)', fontsize=11, loc='left')


def planta(ax):
    import matplotlib.patches as mp
    R = lambda x0, y0, x1, y1, **k: ax.add_patch(mp.Rectangle((x0 / 10, -y1 / 10), (x1 - x0) / 10, (y1 - y0) / 10, **k))
    # Vías y andenes del Roca (nivel 0).
    for y in (250, 379, 424, 553, 596, 725, 772, 902, 940, 1077, 1111, 1252, 1291):
        ax.plot([-150, -83], [-y / 10, -y / 10], color=ROCA, lw=1.2)
    for y0, y1 in ((267, 362), (441, 536), (613, 708), (789, 885), (957, 1060), (1128, 1235), (1308, 1366)):
        R(-1500, y0, -830, y1, color=C0, ec='#a99f8c', lw=.6)
    R(-830, 230, -150, 1400, color=C0, ec='#a99f8c', lw=.8)                                   # hall
    # Obstáculos del hall del modelo (envolventes de las siluetas hall* tomadas del plano).
    R(-385, 675, -204, 1012, color='#d6cdb9'); R(-305, 368, -186, 629, color='#d6cdb9'); R(-376, 1055, -205, 1310, color='#d6cdb9')
    for y0 in (370, 542, 714, 886, 1057, 1229):                                             # cabeceras (hallCabecera*)
        R(-727, y0, -553, y0 + 84, color='#d6cdb9')
    # Subsuelo (nivel -1): escalera B2, pasillo y vestíbulo.
    R(-152, 949, -62, 999, color='#a89f92')
    for x0, y0, x1, y1 in ((-62, 949, 30, 999), (-20, 335, 30, 999), (-20, 335, 80, 385)):
        R(x0, y0, x1, y1, color=C1, ec='#7f95b3', lw=.6)
    R(80, 190, 580, 530, color=C1, ec='#7f95b3', lw=.8)
    R(181, 395, 207, 455, color='#a89f92')
    for k in range(28):
        ax.plot([30.0, 31.6], [-(22 + k) - .5, -(22 + k) - .5], color='#444', lw=.6)
    R(300, 190, 316, 530, color='#555', alpha=.25)
    # Andenes de la Línea C (nivel -2), debajo, al este del vestíbulo.
    for y in (315, 330, 348):
        ax.plot([52, 122], [-y / 10, -y / 10], color=LINEAC, lw=3, alpha=.6)
    # Flujo.
    # Puertas del tren (21 por tren, del lado del andén) y caminata por el andén y el hall hasta la B2.
    for yb in (354, 528, 700, 877, 1052, 1227, 1316):
        xs = [(-830 - 230 * (k // 3) - 230 * (2 * (k % 3) + 1) / 6) / 10 for k in range(21)]
        ax.plot(xs, [-yb / 10] * 21, 'o', ms=1.6, color=FLUJO)
        ax.plot([-150, -83, -54.5, -15.2], [-yb / 10, -yb / 10, -yb / 10, -97.4], color=FLUJO, lw=.8, alpha=.6)
    ax.plot([-15.2, 0.5, 0.5, 30], [-97.4, -97.4, -36, -36], color=FLUJO, lw=2, ls='--')
    ax.annotate('', xy=(56.8, -36), xytext=(32, -36), arrowprops=dict(arrowstyle='-|>', color=FLUJO, lw=2))
    t = dict(fontsize=8.5, ha='center')
    ax.text(-115, -150, 'andenes del Roca: se baja por las\n21 puertas del tren (puntos) y se camina', **t)
    ax.text(-49, -144, 'hall del Roca', **t)
    ax.text(-10.7, -103.5, 'escalera B2', **t)
    ax.text(10, -70, 'pasillo\n(nivel −1)', fontsize=8.5, ha='left')
    ax.text(33, -56, 'vestíbulo Línea C (nivel −1)', **t)
    ax.text(19.4, -47.5, 'B3', **t)
    ax.text(30.8, -18, 'molinetes', **t)
    ax.text(87, -38.5, 'andenes Línea C (nivel −2)', fontsize=8.5, ha='center', color=LINEAC)
    ax.text(-145, -18, 'calle Lima', fontsize=8.5, color='#777'); ax.text(13.5, -125, 'calle Brasil', fontsize=8.5, color='#777', rotation=90)
    ax.annotate('N', xy=(124, -20), xytext=(110, -20), fontsize=9, va='center',
                arrowprops=dict(arrowstyle='-|>', color='#333'))
    ax.set_xlim(-152, 128); ax.set_ylim(-160, -15); ax.set_aspect('equal'); ax.axis('off')
    ax.set_title('Planta esquemática (m, coordenadas del modelo; norte a la derecha como en el plano)', fontsize=11, loc='left')
    leyenda = [mp.Patch(color=C0, label='nivel 0: calle, andenes y hall del Roca'),
               mp.Patch(color=C1, label='nivel −1: pasillo y vestíbulo (−4,60 m)'),
               mp.Patch(color=LINEAC, alpha=.6, label='nivel −2: andenes de la Línea C (−9,20 m)'),
               mp.Patch(color='#a89f92', label='escaleras'),
               plt_line(FLUJO, 'recorrido del pasajero del Roca')]
    ax.legend(handles=leyenda, loc='lower right', fontsize=8.5, frameon=True)


def plt_line(color, label):
    from matplotlib.lines import Line2D
    return Line2D([], [], color=color, lw=2, ls='--', label=label)


def main():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, (a, b) = plt.subplots(2, 1, figsize=(13, 11.5), dpi=170, gridspec_kw=dict(height_ratios=[0.62, 1.45]))
    corte(a)
    planta(b)
    fig.suptitle('Estación Constitución en el modelo: del tren del Roca al andén de la Línea C', fontsize=13, x=.02, ha='left')
    fig.tight_layout()
    FIG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG)
    print('figura:', FIG)


if __name__ == '__main__':
    main()
