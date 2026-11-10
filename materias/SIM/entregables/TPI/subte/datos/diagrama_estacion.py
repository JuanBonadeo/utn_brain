#!/usr/bin/env python3
"""Diagrama de la estación Constitución tal como la representa el modelo: corte por el recorrido del pasajero del Roca
y planta esquemática por niveles. Escribe materias/SIM/figs/tpi-subte-estacion-niveles.png. Requiere matplotlib.

Medidas: las del modelo (02-modelo-anylogic.md, secciones del vestíbulo coherente, del subsuelo y "Accesos reales al
subsuelo", con su corrección del 2026-11-09). El pasajero del Roca baja del hall por una de las dos escaleras mecánicas
del bloque central (norte: X -385 a -280, Y 740-768; sur: Y 916-944; 10,5 m × 2,8 m, 4,6 m de desnivel, tope al oeste)
según su andén (Y < 840: norte), cruza la plaza de transbordo (X -280 a -152, Y 660-1010) y sigue por el pasillo del
Roca (desde X -152, Y 949-999) hasta el vestíbulo. Profundidades: -4,60 m (plaza, pasillo y vestíbulo, GCBA 2015) y -9,20 m (andenes de la Línea C, supuesto [SUP]); el resto sale del plano de Trenes Argentinos
georreferenciado con OpenStreetMap.
"""
import math
from pathlib import Path

AQUI = Path(__file__).resolve().parent
FIG = AQUI.parents[3] / 'figs' / 'tpi-subte-estacion-niveles.png'
C0, C1, C2 = '#e9e4d8', '#cfdcec', '#b9c9a8'       # nivel 0 (calle/hall), -1 (vestíbulo), -2 (andenes C)
ROCA, LINEAC, FLUJO = '#7a6a58', '#1f5fbf', '#d9531e'

# Hall: distancia en línea recta desde la cabecera de cada andén (X = -545) hasta el tope de su escalera mecánica
# (X = -385; Y = 754 la norte, Y = 930 la sur). Bajan por la norte los andenes con Y < 840 (Pasajero.accesoNortePed).
ANDENES_Y = [314, 489, 661, 837, 1009, 1181, 1326]
ESC_NORTE_Y, ESC_SUR_Y = 754, 930
ESC_Y = [ESC_NORTE_Y if y < 840 else ESC_SUR_Y for y in ANDENES_Y]
HALL = [math.dist((-545, y), (-385, ye)) / 10 for y, ye in zip(ANDENES_Y, ESC_Y)]
# Plaza de transbordo: del pie de cada escalera (X = -280) a la boca del pasillo (X = -152, Y = 974).
PLAZA = [math.dist((-280, ye), (-152, 974)) / 10 for ye in (ESC_NORTE_Y, ESC_SUR_Y)]
N1, N2 = -4.6, -9.2                                  # profundidades del subsuelo y de los andenes de la C (m)


def corte(ax):
    import matplotlib.patches as mp
    # Tramos a lo largo del recorrido (m): andén, hall, escalera mecánica (10,5 m), plaza, pasillo (84 m), vestíbulo.
    x_hall = 31
    x_esc = x_hall + 34
    x_pla = x_esc + 10.5
    x_pas = x_pla + 20
    x_ves = x_pas + 84
    x_fin = x_ves + 50
    gris = '#d8d2c4'
    ax.add_patch(mp.Rectangle((-5, -1.2), x_esc + 5, 1.2, color=gris))                              # losa del hall
    ax.add_patch(mp.Rectangle((x_esc + 6, -1.2), x_fin - x_esc - 1, 1.2, color=gris))               # terreno calle
    ax.add_patch(mp.Rectangle((x_esc + 6, N1 - 1.2), x_fin - x_esc - 1, 1.2, color=gris))           # losa subsuelo
    ax.add_patch(mp.Rectangle((x_ves + 30, N2 - 1.2), 22, 1.2, color=gris))                         # andén C
    # Niveles (fondos).
    ax.add_patch(mp.Rectangle((-5, 0), x_esc + 5, 4, color=C0, alpha=.8))
    ax.add_patch(mp.Rectangle((x_esc, N1), x_fin - x_esc, 3.4, color=C1, alpha=.9))
    ax.add_patch(mp.Rectangle((x_ves + 30, N2), 22, 3.4, color=C2, alpha=.9))
    ax.plot([x_pla, x_pla], [N1, N1 + 3.4], color='#7f95b3', lw=.6, ls=':')
    ax.plot([x_pas, x_pas], [N1, N1 + 3.4], color='#7f95b3', lw=.6, ls=':')
    # Tren del Roca en el andén (vías hundidas 1,1 m).
    ax.add_patch(mp.Rectangle((-5, -1.1), 34, 4.0, color=ROCA, alpha=.85))
    ax.text(12, 1.0, 'tren del Roca', color='white', ha='center', va='center', fontsize=9)
    # Escalera mecánica (norte o sur, iguales): 10,5 m de largo, 4,6 m de desnivel; tope en el hall, pie en la plaza.
    n = 14
    for i in range(n):
        ax.add_patch(mp.Rectangle((x_esc + 10.5 * i / n, N1 + 4.6 * (n - i - 1) / n), 10.5 / n, 4.6 / n + .02,
                                  color='#a89f92'))
    ax.plot([x_esc, x_pla], [0, N1], color='#6b645a', lw=1)
    # Escaleras del vestíbulo a los andenes de la C y escalera B3 a la calle Brasil.
    for i in range(10):
        ax.add_patch(mp.Rectangle((x_ves + 22 + .8 * i, N1 - .46 * (i + 1)), .8, .46 * (i + 1) - .02, color='#a89f92'))
    for i in range(10):
        ax.add_patch(mp.Rectangle((x_ves + 2 + .8 * i, N1), .8, .46 * (i + 1), color='#a89f92'))
    ax.add_patch(mp.Rectangle((x_ves + 30, N2), 22, .6, color=LINEAC))
    # Molinetes.
    for k in range(4):
        ax.add_patch(mp.Rectangle((x_ves + 18 + .5 * k, N1), .25, 1.0, color='#444'))
    # Flujo del pasajero.
    yf1, yf2 = N1 + .9, N2 + .9
    pts = [(2, .9), (x_hall, .9), (x_esc, .9), (x_pla, yf1), (x_ves + 20, yf1), (x_ves + 26, yf1), (x_ves + 36, yf2)]
    ax.plot(*zip(*pts), color=FLUJO, lw=2.2, ls='--')
    ax.annotate('', xy=pts[-1], xytext=(x_ves + 33, yf2 + 1.2), arrowprops=dict(arrowstyle='-|>', color=FLUJO, lw=2))
    # Cotas y rótulos.
    def cota(x0, x1, y, txt):
        ax.annotate('', xy=(x0, y), xytext=(x1, y), arrowprops=dict(arrowstyle='<->', color='#333', lw=.8))
        ax.text((x0 + x1) / 2, y + .35, txt, ha='center', fontsize=8.5)
    cota(0, x_hall, 5.0, 'andén (se camina)\ndesde 21 puertas')
    cota(x_hall, x_esc, 5.0, f'hall del Roca (se camina)\n{min(HALL):.0f} a {max(HALL):.0f} m según el andén')
    cota(x_esc, x_pla, 2.0, 'escalera mecánica\n10,5 m')
    cota(x_pla, x_pas, -0.6, f'plaza de\ntransbordo\n{min(PLAZA):.0f} a {max(PLAZA):.0f} m')
    cota(x_pas, x_ves, -0.6, 'pasillo del Roca (se camina), 84 m × 5 m')
    cota(x_ves + 12, x_ves + 50, -0.6, 'vestíbulo Línea C, 50 m')
    ax.text(x_esc - 1, -2.6, 'norte o sur según el andén:\n4,6 m de desnivel a 0,685 m/s\n→ 15,3 s', fontsize=8.5,
            ha='right', va='center')
    ax.annotate('B3 desde la calle Brasil', xy=(x_ves + 6, -1.9), xytext=(x_ves + 6, 2.2), fontsize=8.5, ha='center',
                arrowprops=dict(arrowstyle='-', color='#777', lw=.7))
    ax.text(x_ves + 19, N1 + 1.25, 'molinetes', fontsize=8, ha='center')
    ax.text(x_ves + 41, N2 - 2.6, 'andenes Línea C', fontsize=8.5, ha='center', color=LINEAC)
    for y, t in ((0, 'nivel 0 · calle y hall'), (N1, 'nivel −1 · −4,60 m (GCBA)'), (N2, 'nivel −2 · −9,20 m [SUP]')):
        ax.axhline(y, color='#999', lw=.5, ls=':')
        ax.text(x_fin + 7, y + .2, t, fontsize=8.5, color='#555')
    ax.set_xlim(-8, x_fin + 40); ax.set_ylim(N2 - 3.4, 8.6); ax.set_aspect(2.2); ax.axis('off')
    ax.set_title('Corte por el recorrido del pasajero del Roca (escala vertical exagerada ×2,2; tramos horizontales '
                 'del hall y la plaza, esquemáticos)', fontsize=11, loc='left')


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
    # Escaleras mecánicas norte y sur (bloque central: tope al oeste, en el hall; pie al este, en la plaza).
    R(-385, 740, -280, 768, color='#a89f92', ec='#6b645a', lw=.6); R(-385, 916, -280, 944, color='#a89f92', ec='#6b645a', lw=.6)
    # Subsuelo (nivel -1): plaza de transbordo (debajo del bloque central), pasillo y vestíbulo.
    R(-280, 660, -152, 1010, color=C1, ec='#7f95b3', lw=.8, ls='--', alpha=.95)
    for x0, y0, x1, y1 in ((-152, 949, 30, 999), (-20, 335, 30, 999), (-20, 335, 80, 385)):
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
    # Puertas del tren (21 por tren, del lado del andén) y caminata por el andén y el hall hasta el tope de su
    # escalera mecánica (norte si el andén está al norte del centro del bloque, Y < 840; si no, sur).
    for yb in (354, 528, 700, 877, 1052, 1227, 1316):
        ye = ESC_NORTE_Y if yb < 840 else ESC_SUR_Y
        xs = [(-830 - 230 * (k // 3) - 230 * (2 * (k % 3) + 1) / 6) / 10 for k in range(21)]
        ax.plot(xs, [-yb / 10] * 21, 'o', ms=1.6, color=FLUJO)
        ax.plot([-150, -83, -54.5, -38.5], [-yb / 10, -yb / 10, -yb / 10, -ye / 10], color=FLUJO, lw=.8, alpha=.6)
    for ye in (ESC_NORTE_Y, ESC_SUR_Y):                                                     # escalera y plaza
        ax.plot([-38.5, -28, -15.2], [-ye / 10, -ye / 10, -97.4], color=FLUJO, lw=2, ls='--')
    ax.plot([-15.2, 0.5, 0.5, 30], [-97.4, -97.4, -36, -36], color=FLUJO, lw=2, ls='--')
    ax.annotate('', xy=(56.8, -36), xytext=(32, -36), arrowprops=dict(arrowstyle='-|>', color=FLUJO, lw=2))
    t = dict(fontsize=8.5, ha='center')
    ax.text(-115, -150, 'andenes del Roca: se baja por las\n21 puertas del tren (puntos) y se camina', **t)
    ax.text(-49, -144, 'hall del Roca', **t)
    fondo = dict(fc='white', ec='none', alpha=.85, pad=1.2)
    ax.text(-33.25, -72.2, 'escalera norte', fontsize=8, ha='center', bbox=fondo)
    ax.text(-33.25, -97.6, 'escalera sur', fontsize=8, ha='center', bbox=fondo)
    ax.text(-8.6, -74, 'plaza de transbordo (nivel −1)', fontsize=8, ha='center', va='center', rotation=90)
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
               mp.Patch(color=C1, label='nivel −1: plaza, pasillo y vestíbulo (−4,60 m)'),
               mp.Patch(color=LINEAC, alpha=.6, label='nivel −2: andenes de la Línea C (−9,20 m)'),
               mp.Patch(color='#a89f92', label='escaleras (mecánicas norte y sur del hall, B3)'),
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
