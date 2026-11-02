#!/usr/bin/env python3
"""Georreferencia el plano DWG de Trenes Argentinos con OpenStreetMap y mide el acceso del Roca a la Línea C.

Uso (desde esta carpeta):
    dwg2dxf -y -o /tmp/plano.dxf solicitudes/sofse-2026-10-26/CONSTITUCION_NUEVO_FINAL.dwg   # libredwg
    python3 georref_plano_sofse.py /tmp/plano.dxf            # reusa osm_hall.json
    python3 georref_plano_sofse.py /tmp/plano.dxf --online   # vuelve a consultar Overpass

Requiere ezdxf y matplotlib (no son de la biblioteca estándar). Escribe la figura
materias/SIM/figs/tpi-subte-plano-acceso.png e imprime el ajuste y las distancias.

Método (2026-11-02):
1. Control: los 13 paragolpes del plano (extremos de vía de la capa VIAS en x = -2116,31; centro de cada
   par de rieles) contra los nodos railway=buffer_stop de OSM de la misma fila. El patrón de separaciones
   (una vía suelta y seis pares, ~13 m entre pares y ~4 m dentro del par) identifica la correspondencia.
2. Ajuste de similitud (escala, rotación y traslación, sin reflejo) por mínimos cuadrados.
3. Se transforman al plano las bocas, escaleras, pasillos subterráneos y andenes de la Línea C de OSM.
4. Recorrido = paragolpes -> boca del hall (en L y en línea recta) + escalera y pasillo hasta el vestíbulo
   (polilínea de OSM), y la demora con la fórmula de 07-plan-tpi.md §5: D/v + h/v_esc, h = 5 m [SUP].
Fuentes: plano de Trenes Argentinos (nota NO-2026-104102701-APN-UCIYT#SOFSE) y © colaboradores de
OpenStreetMap (ODbL). Los pasillos subterráneos son datos voluntarios de OSM, no del plano oficial.
"""
import json, math, statistics as st, subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
OSM = AQUI / 'osm_hall.json'
FIG = AQUI.parents[3] / 'figs' / 'tpi-subte-plano-acceso.png'
Q = ('[out:json][timeout:60];('
     'nwr(around:450,-34.6282,-58.3808)["railway"~"buffer_stop|subway_entrance|platform|station"];'
     'nwr(around:160,-34.6282,-58.3808)["highway"~"steps|footway|corridor|elevator"];'
     ');out tags geom;')
LAT0, LON0, R = -34.6285, -58.3805, 6371008.8
X_PARAGOLPES = -2116.31
# Correspondencia vía del plano (de oeste a este) -> paragolpes de OSM (paso 1).
OSM_PARAGOLPES = [3443461332, 3443461331, 3443461330, 3443461329, 3443461328, 3443461327, 3443461326,
                  3443461325, 3443461324, 3443461323, 3443461322, 3443461321, 3443461320]
BOCA_HALL = 1978947865                 # railway=subway_entrance, level 0, dentro del hall
ESCALERA_HALL, PASILLO_HALL = 187138350, 187138351
CAPAS_FONDO_FUERA = {'BASURA', 'COTAS', 'TIT_COTAS', 'TIT_NUM', 'ASHADE', 'TEXT-03', 'TEXT-02', 'VENDIDO',
                     'EXPTEVENTA', 'PERMUTA', 'CEDIDO', 'HABILITA', 'IINTUSION', 'VIVIENDA', 'TITULO'}


def en(lat, lon):
    return complex(math.radians(lon - LON0) * R * math.cos(math.radians(LAT0)), math.radians(lat - LAT0) * R)


def vias_plano(msp):
    ys = sorted({round(p.y, 2) for e in msp.query('LINE[layer=="VIAS"]') for p in (e.dxf.start, e.dxf.end)
                 if abs(p.x - X_PARAGOLPES) < 0.05 and 2700 < p.y < 2850})
    assert len(ys) == 26, f'se esperaban 26 extremos de riel, hay {len(ys)}'
    return [(ys[i] + ys[i + 1]) / 2 for i in range(0, 26, 2)]


def main():
    import ezdxf
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from ezdxf.addons.drawing import RenderContext, Frontend
    from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
    from ezdxf.addons.drawing.config import Configuration, BackgroundPolicy, ColorPolicy

    if '--online' in sys.argv:
        subprocess.run(['curl', '-s', '--max-time', '120', '-A', 'UTN-SIM-TPI/1.0', '--data-urlencode', f'data={Q}',
                        'https://overpass-api.de/api/interpreter', '-o', str(OSM)], check=True)
    osm = {e['id']: e for e in json.load(open(OSM))['elements']}
    doc = ezdxf.readfile(next(a for a in sys.argv[1:] if not a.startswith('--')))
    msp = doc.modelspace()

    centros = vias_plano(msp)
    za = [complex(X_PARAGOLPES, y) for y in centros]
    zb = [en(osm[i]['lat'], osm[i]['lon']) for i in OSM_PARAGOLPES]
    ma, mb = sum(za) / len(za), sum(zb) / len(zb)
    k = sum((b - mb) * (a - ma).conjugate() for a, b in zip(za, zb)) / sum(abs(a - ma) ** 2 for a in za)
    t = mb - k * ma
    res = [abs(k * a + t - b) for a, b in zip(za, zb)]
    print(f'ajuste: escala {abs(k):.4f}, rotación {math.degrees(math.atan2(k.imag, k.real)):.2f}°, '
          f'residuo máx {max(res):.2f} m, rms {math.sqrt(sum(r * r for r in res) / len(res)):.2f} m (n = {len(res)})')

    def plano(lat, lon):
        w = (en(lat, lon) - t) / k
        return w.real, w.imag

    def geom(e):
        return [plano(e['lat'], e['lon'])] if e['type'] == 'node' else [plano(p['lat'], p['lon']) for p in e['geometry']]

    boca = geom(osm[BOCA_HALL])[0]
    acceso = geom(osm[ESCALERA_HALL]) + geom(osm[PASILLO_HALL])[1:]
    largo_acceso = sum(math.dist(acceso[i], acceso[i + 1]) for i in range(len(acceso) - 1))
    en_l = [abs(X_PARAGOLPES - boca[0]) + abs(y - boca[1]) for y in centros]
    recta = [math.dist((X_PARAGOLPES, y), boca) for y in centros]
    print(f'paragolpes -> boca del hall: en L mediana {st.median(en_l):.1f} m ({min(en_l):.1f}-{max(en_l):.1f}); '
          f'recta mediana {st.median(recta):.1f} m ({min(recta):.1f}-{max(recta):.1f})')
    print(f'escalera + pasillo subterráneo hasta el vestíbulo (OSM): {largo_acceso:.1f} m')
    for nombre, d in (('en L', st.median(en_l) + largo_acceso), ('recta', st.median(recta) + largo_acceso)):
        print(f'D total ({nombre}) = {d:.0f} m -> demora optimista {d / 1.25 + 5 / 0.30:.0f} s, '
              f'intermedia {d / 0.95 + 5 / 0.30:.0f} s, pesimista {d / 0.63 + 5 / 0.20:.0f} s')

    # Figura: plano de fondo en gris y superposición de OSM.
    x0, x1, y0, y1 = -2335, -2095, 2700, 2840
    fig = plt.figure(figsize=(12, 12 * (y1 - y0) / (x1 - x0)), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    cfg = Configuration(background_policy=BackgroundPolicy.WHITE, color_policy=ColorPolicy.CUSTOM,
                        custom_fg_color='#9a9a9a', lineweight_scaling=0.25)
    Frontend(RenderContext(doc), MatplotlibBackend(ax), config=cfg).draw_layout(
        msp, finalize=False,
        filter_func=lambda e: e.dxf.layer not in CAPAS_FONDO_FUERA and e.dxftype() not in ('TEXT', 'MTEXT', 'DIMENSION'))
    for e in osm.values():
        tg = e.get('tags', {})
        if 'geometry' not in e and e['type'] != 'node':
            continue
        g = geom(e)
        xs, ys = zip(*g)
        if tg.get('railway') == 'platform' and tg.get('layer') == '-2':
            ax.plot(xs, ys, color='#1f5fbf', lw=5, alpha=.8, solid_capstyle='butt')
        elif tg.get('tunnel') == 'yes' or tg.get('layer') == '-1':
            ax.plot(xs, ys, color='#d9531e', lw=2.6, ls=(0, (4, 2)))
        elif tg.get('highway') == 'steps':
            ax.plot(xs, ys, color='#d9531e', lw=3.5)
        elif tg.get('railway') == 'subway_entrance':
            ax.plot(*g[0], 'o', ms=8, color='#d9531e', mec='white', mew=1.2, zorder=5)
    ax.plot([X_PARAGOLPES] * len(centros), centros, 's', ms=4, color='black')
    yv = centros[6]
    ax.plot([X_PARAGOLPES, boca[0]], [yv, boca[1]], color='black', lw=1.4, ls=':')
    rot = dict(fontsize=10, ha='center')
    ax.annotate('Andenes de la Línea C (nivel −2)', (-2278, 2716.5), color='#1f5fbf', **rot)
    ax.annotate('Pasillo subterráneo (OSM)', (-2207, 2760), color='#d9531e', rotation=90, **rot)
    ax.annotate('Boca en el hall', (boca[0] - 2, boca[1] + 5), color='#d9531e', fontsize=10, ha='right')
    ax.annotate('Hall del Roca', (-2150, 2812), fontsize=11, color='#555555', ha='center')
    ax.annotate('Calle Lima', (-2250, 2703), fontsize=10, color='#555555', ha='center')
    ax.annotate('Paragolpes del Roca', (X_PARAGOLPES - 2, 2835), fontsize=10, ha='right')
    ax.annotate('Calle Brasil', (-2221, 2805), rotation=90, fontsize=10, color='#555555', ha='center')
    ax.annotate('N  ←', (-2330, 2833), fontsize=10)
    ax.set_xlim(x0, x1); ax.set_ylim(y0, y1); ax.set_aspect('equal'); ax.axis('off')
    FIG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG)
    print('figura:', FIG)


if __name__ == '__main__':
    main()
