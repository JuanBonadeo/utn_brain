#!/usr/bin/env python3
"""Genera la volumetría 3D del plano de Trenes Argentinos para MainPeatonal (grupo plano3D, sólo vista 3D).

Uso (desde esta carpeta, después de fondo_anylogic.py):
    python3 plano_3d.py                 # escribe plano3d_grupo.xml y figs de control en esta carpeta
    python3 plano_3d.py --insertar      # además reemplaza/inserta el grupo plano3D en ../SubteConstitucion.alp
Requiere ezdxf y shapely. Editar el .alp sólo con AnyLogic cerrado.

Qué genera (todo en px del modelo, 10 px = 1 m, Z hacia arriba; sólo Rectangle sin rotación, que es el
formato que AnyLogic ya guardó en este modelo):
- Piso del hall y del vestíbulo (Z = 0) y lecho de vías hundido (las vías del Roca van a Z = -11, 1,1 m abajo,
  así el piso del coche queda al nivel del andén y del hall, como en la estación).
- Andenes del Roca: entre los pares de vías del plano (13 vías: una suelta y seis pares), desde la cola del tren
  detenido hasta los paragolpes.
- Muros del plano (EDIFICIOS, LINE_02, MUROS-NUEVOS, MUROS1, HORM, LIMITE) como muros bajos semitransparentes
  de 2,5 m; barandas y molinetes del Roca (BARANDA, TMR) de 1 m; cordones de calle (CALLES) de 0,15 m.
  Los segmentos oblicuos o curvos se aproximan con tramos escalonados de 0,5 m.
- Escaleras (ESCALERA, ESCA) como bloques de 4 peldaños sobre su rectángulo envolvente.
- Andenes de la Línea C (LINEA_C_OSM) como losas de 1 m.
Se recortan los muros que caen donde camina la gente del modelo (pasillo, vestíbulo y circulación del hall),
para que nadie atraviese una pared en la vista 3D.
"""
import math, re, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
DXF = AQUI.parent / 'plano_constitucion_modelo.dxf'
ALP = AQUI.parent / 'SubteConstitucion.alp'
SALIDA = AQUI / 'plano3d_grupo.xml'
ID0 = 1796000000000

MUROS = {'EDIFICIOS', 'LINE_02', 'MUROS-NUEVOS', 'MUROS1', 'HORM', 'LIMITE'}
BAJOS = {'BARANDA': 10, 'TMR': 10, 'CALLES': 1.5}
ESCALERAS = {'ESCALERA', 'ESCA'}
ESPESOR = 2.5            # px (0,25 m)
ALTO_MURO = 25           # px (2,5 m)
MIN_LARGO = 3            # px: se descarta el detalle de menos de 0,3 m
PASO = 5                 # px: tramo de los escalonados oblicuos

# Vías del plano en px del modelo (georref_plano_sofse.vias_plano, Y = 360 + 10 (y - 2726,9)).
VIAS = [250, 379, 424, 553, 596, 725, 772, 902, 940, 1077, 1111, 1252, 1291]
Z_VIA = -11
Z_SUB = -46              # subsuelo: plaza de transbordo a -4,60 m (GCBA 2015), pasillo y vestíbulo (nivelVestibulo)
Z_LINEA_C = -92          # andenes de la Línea C, un entrepiso más abajo (-9,20 m) [SUP]
# Estación de la Línea C (esquema [SUP], al este del vestíbulo): dos vías entre un andén central y dos laterales.
ESTACION_C = (600, 195, 1250, 485)                      # x0, y0, x1, y1
ANDENES_C = [(195, 265), (305, 375), (415, 485)]        # lateral norte, central, lateral sur (7 m)
VIAS_C = [(265, 305), (375, 415)]
X_PARAGOLPES = -830      # fin de las vías (los RailTrack terminan en X = -820)
X_COLA = -2620           # cola del tren de 7 coches detenido (161 m) con margen
X_INICIO_VIAS = -5000
X_HALL0 = -830           # el piso del hall arranca en los paragolpes

# Colores ARGB (enteros con signo, como los guarda AnyLogic).
def argb(a, r, g, b):
    v = (a << 24) | (r << 16) | (g << 8) | b
    return v - (1 << 32) if v >= 1 << 31 else v

COLOR = {
    'piso': argb(255, 214, 210, 200), 'lecho': argb(255, 92, 84, 76), 'anden': argb(255, 196, 190, 178),
    'borde': argb(255, 232, 196, 40), 'muro': argb(150, 150, 150, 158), 'bajo': argb(200, 110, 110, 118),
    'cordon': argb(255, 160, 160, 160), 'escalera': argb(255, 168, 160, 150), 'lineaC': argb(255, 160, 180, 205),
    'vereda': argb(255, 200, 200, 196), 'subsuelo': argb(255, 226, 222, 214), 'riel': argb(255, 70, 70, 75),
}


def zonas_libres():
    """Polígonos (px) donde camina la gente del modelo: ahí no se levantan muros del plano."""
    from shapely.geometry import LineString, box
    from shapely.ops import unary_union
    pasillo = LineString([(-170, 974), (5, 974), (5, 360), (90, 360)]).buffer(31, cap_style='flat', join_style='mitre')
    vestibulo = box(75, 185, 585, 535)
    # Circulación del hall: de los andenes (X -830) a la boca B2 (X -152, Y 949-999). Los obstáculos del modelo
    # (hall*: cabeceras de andén, escaleras, vestuario y boletería) tienen muros propios; dentro se conserva el plano.
    hall = box(-835, 275, -150, 1362)          # desde los paragolpes: la gente sale de los andenes y cruza la cabecera
    return unary_union([pasillo, vestibulo, hall])


def obstaculos_modelo(alp_txt):
    """Polígonos de los muros hall* del modelo (en px absolutos), donde sí se conserva el detalle del plano."""
    from shapely.geometry import Polygon
    polys = []
    for m in re.finditer(r'<Wall>.*?</Wall>', alp_txt, re.S):
        w = m.group(0)
        nombre = re.search(r'<Name><!\[CDATA\[(.*?)\]\]>', w).group(1)
        if not nombre.startswith('hall'):
            continue
        x0, y0 = map(float, re.search(r'<X>([-\d.]+)</X><Y>([-\d.]+)</Y>', w).groups())
        pts = [(x0 + float(a), y0 + float(b)) for a, b in re.findall(r'<Point><X>([-\d.]+)</X><Y>([-\d.]+)</Y>', w)]
        if len(pts) >= 3:
            p = Polygon(pts).convex_hull
            polys.append(p)
    return polys


def segmentos(msp, capas):
    from ezdxf import path
    segs = []
    for e in msp:
        if e.dxf.layer not in capas or e.dxftype() in ('TEXT', 'MTEXT'):
            continue
        try:
            v = [(q.x * 10, -q.y * 10) for q in path.make_path(e).flattening(0.05)]
        except Exception:
            continue
        segs += [(v[i], v[i + 1], e.dxf.layer) for i in range(len(v) - 1)]
    return segs


def fusionar(segs):
    """Une tramos colineales ortogonales que se tocan o se solapan; devuelve (horizontales, verticales, oblicuos)."""
    h, v, ob = {}, {}, []
    for (a, b, capa) in segs:
        if math.dist(a, b) < 0.5:
            continue
        if abs(a[1] - b[1]) < 0.3:
            h.setdefault(round((a[1] + b[1]) / 2 / ESPESOR), []).append((min(a[0], b[0]), max(a[0], b[0])))
        elif abs(a[0] - b[0]) < 0.3:
            v.setdefault(round((a[0] + b[0]) / 2 / ESPESOR), []).append((min(a[1], b[1]), max(a[1], b[1])))
        else:
            ob.append((a, b))

    def unir(d):
        out = []
        for k, ivs in d.items():
            ivs.sort()
            s, e = ivs[0]
            for a, b in ivs[1:]:
                if a <= e + 0.6:
                    e = max(e, b)
                else:
                    out.append((k * ESPESOR, s, e)); s, e = a, b
            out.append((k * ESPESOR, s, e))
        return out
    return unir(h), unir(v), ob


GRILLA = (-1200.0, 0.0, 2500, 1700)   # x0, y0, ancho, alto (px) de la grilla de compactación
CELDA = 3.33                           # px (0,33 m)
CIERRE = 3                             # celdas del cierre morfológico
COLUMNA = 22                           # px: componentes más chicos que esto se rellenan (columnas macizas)


def cajas_de_segmentos(h, v, ob, libre, conservar, oblicuos=True):
    """Rasteriza los tramos en una grilla de 0,25 m, quita las zonas libres, rellena columnas y devuelve la
    grilla compactada en rectángulos (x, y, w, h) alineados a los ejes."""
    import numpy as np
    import shapely
    from scipy import ndimage
    gx0, gy0, gw, gh = GRILLA
    nx, ny = int(gw / CELDA), int(gh / CELDA)
    m = np.zeros((ny, nx), bool)
    def marcar(x0, y0, x1, y1):
        i0, i1 = int((y0 - gy0) // CELDA), int(-(-(y1 - gy0) // CELDA))
        j0, j1 = int((x0 - gx0) // CELDA), int(-(-(x1 - gx0) // CELDA))
        m[max(i0, 0):max(min(i1, ny), 0), max(j0, 0):max(min(j1, nx), 0)] = True
    for y, a, b in h:
        if b - a >= MIN_LARGO:
            marcar(a, y - ESPESOR / 2, b, y + ESPESOR / 2)
    for x, a, b in v:
        if b - a >= MIN_LARGO:
            marcar(x - ESPESOR / 2, a, x + ESPESOR / 2, b)
    if oblicuos:
        for a, b in ob:
            n = max(1, int(math_dist(a, b)))
            for k in range(n + 1):
                t = k / n
                x, y = a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])
                marcar(x - 1, y - 1, x + 1, y + 1)
    # Muros dibujados con doble línea: cierre morfológico para que queden macizos; se borran motas sueltas.
    m = ndimage.binary_closing(m, structure=np.ones((CIERRE, CIERRE)))
    # Columnas: componentes chicos se rellenan enteros.
    lab, n = ndimage.label(m, structure=np.ones((3, 3)))
    for sl in ndimage.find_objects(lab):
        if (sl[0].stop - sl[0].start) * CELDA <= COLUMNA and (sl[1].stop - sl[1].start) * CELDA <= COLUMNA:
            m[sl] = True
    # Zonas libres (circulación del modelo), salvo dentro de los obstáculos del modelo.
    libre = libre.difference(conservar) if conservar is not None else libre
    jj, ii = np.meshgrid(np.arange(nx), np.arange(ny))
    cx, cy = gx0 + (jj + .5) * CELDA, gy0 + (ii + .5) * CELDA
    m &= ~shapely.contains_xy(libre, cx, cy)
    return compactar(m, gx0, gy0, CELDA)


def compactar(m, gx0, gy0, celda):
    """Grilla booleana -> rectángulos: corridas por fila, extendidas hacia abajo mientras la corrida se repite."""
    import numpy as np
    ny, nx = m.shape
    abiertos, cajas = {}, []
    for i in range(ny + 1):
        fila = m[i] if i < ny else np.zeros(nx, bool)
        corridas = set()
        j = 0
        while j < nx:
            if fila[j]:
                k = j
                while k < nx and fila[k]:
                    k += 1
                corridas.add((j, k)); j = k
            else:
                j += 1
        for key in list(abiertos):
            if key not in corridas:
                i0 = abiertos.pop(key)
                cajas.append((gx0 + key[0] * celda, gy0 + i0 * celda, (key[1] - key[0]) * celda, (i - i0) * celda))
        for key in corridas:
            abiertos.setdefault(key, i)
    return cajas


def rectangulos(poly, celda=10):
    """Polígono shapely -> rectángulos alineados (grilla de `celda` px)."""
    import numpy as np
    import shapely
    x0, y0, x1, y1 = poly.bounds
    nx, ny = int(-(-(x1 - x0) // celda)), int(-(-(y1 - y0) // celda))
    jj, ii = np.meshgrid(np.arange(nx), np.arange(ny))
    m = shapely.contains_xy(poly, x0 + (jj + .5) * celda, y0 + (ii + .5) * celda)
    return compactar(m, x0, y0, celda)


def corte_subsuelo():
    """Huella del subsuelo (pasillo, escalera B2, vestíbulo y escalera B3): ahí se abre el piso de la calle y del hall
    para ver el nivel -1 en la vista 3D."""
    from shapely.geometry import box
    from shapely.ops import unary_union
    return unary_union([box(-152, 944, 35, 1004), box(-25, 330, 35, 1004), box(-25, 330, 85, 390), box(75, 185, 585, 535)])


def corte_total():
    """Corte del piso de la calle: subsuelo más la estación de la Línea C (ESTACION_C) y su escalera."""
    from shapely.geometry import box
    return corte_subsuelo().union(box(*ESTACION_C)).union(box(580, 295, 605, 425))


def math_dist(a, b):
    return math.dist(a, b)


def escaleras(msp, libre):
    """Agrupa los escalones por cercanía y devuelve el rectángulo envolvente de cada escalera (eje alineado)."""
    from shapely.geometry import LineString
    from shapely.ops import unary_union
    lineas = [LineString([a, b]) for a, b, _ in segmentos(msp, ESCALERAS) if math.dist(a, b) > 0.5]
    grupos = unary_union([l.buffer(4) for l in lineas])
    out = []
    for g in getattr(grupos, 'geoms', [grupos]):
        x0, y0, x1, y1 = g.buffer(-3.5).bounds if not g.buffer(-3.5).is_empty else g.bounds
        w, hh = x1 - x0, y1 - y0
        if w * hh < 60 or g.intersects(libre):          # descarta trazos sueltos y lo que pisa la circulación
            continue
        out.append((x0, y0, w, hh))
    return out


class Gen:
    def __init__(self):
        self.n = 0
        self.xml = []

    def rect(self, nombre, x, y, w, h, z, zh, color, linea=None):
        self.n += 1
        lc = color if linea is None else linea
        self.xml.append(f'''				<Rectangle>
					<Id>{ID0 + self.n}</Id>
					<Name><![CDATA[{nombre}{self.n}]]></Name>
					<X>{x:.1f}</X><Y>{y:.1f}</Y>
					<Label><X>10</X><Y>0</Y></Label>
					<PublicFlag>true</PublicFlag>
					<PresentationFlag>true</PresentationFlag>
					<ShowLabel>false</ShowLabel>
					<DrawMode>SHAPE_DRAW_3D</DrawMode>
					<EmbeddedIcon>false</EmbeddedIcon>
					<Z>{z:g}</Z>
					<ZHeight>{zh:g}</ZHeight>
					<LineWidth>1</LineWidth>
					<LineColor>{lc}</LineColor>
					<LineMaterial>null</LineMaterial>
					<LineStyle>SOLID</LineStyle>
					<Width>{w:.1f}</Width>
					<Height>{h:.1f}</Height>
					<Rotation>0.0</Rotation>
					<FillColor>{color}</FillColor>
					<FillMaterial>null</FillMaterial>
				</Rectangle>''')

    def grupo(self):
        cuerpo = '\n'.join(self.xml)
        return f'''				<Group>
					<Id>{ID0}</Id>
					<Name><![CDATA[plano3D]]></Name>
					<X>0</X><Y>0</Y>
					<Label><X>10</X><Y>0</Y></Label>
					<PublicFlag>true</PublicFlag>
					<PresentationFlag>true</PresentationFlag>
					<ShowLabel>false</ShowLabel>
					<DrawMode>SHAPE_DRAW_3D</DrawMode>
					<EmbeddedIcon>false</EmbeddedIcon>
					<Z>0</Z>
					<Rotation>0.0</Rotation>

			<Presentation>
{cuerpo}
			</Presentation>

				</Group>'''


def main():
    import ezdxf
    msp = ezdxf.readfile(DXF).modelspace()
    alp_txt = ALP.read_text(encoding='utf-8')
    from shapely.ops import unary_union
    libre = zonas_libres()
    obst = obstaculos_modelo(alp_txt)
    conservar = unary_union(obst) if obst else None
    g = Gen()
    resumen = {}

    # 1. Suelos. Lecho de vías hundido bajo toda la playa; andenes del Roca entre pares de vías.
    g.rect('lechoVias', X_INICIO_VIAS, 230, X_PARAGOLPES - X_INICIO_VIAS, 1150, Z_VIA - 2, 2, COLOR['lecho'])
    andenes = []
    for a, b in zip(VIAS, VIAS[1:]):
        if b - a > 60:                                  # hueco entre pares = andén (los pares están a ~4 m)
            andenes.append((a + 17, b - 17))
    andenes.append((VIAS[-1] + 17, VIAS[-1] + 75))      # andén lateral sur
    for y0, y1 in andenes:
        g.rect('andenRoca3D', X_COLA, y0, X_PARAGOLPES - X_COLA, y1 - y0, Z_VIA, -Z_VIA, COLOR['anden'])
        for yb in (y0, y1 - 5):                          # línea amarilla de borde, 0,5 m
            g.rect('bordeAnden3D', X_COLA, yb, X_PARAGOLPES - X_COLA, 5, 0, 0.2, COLOR['borde'])
    resumen['andenes'] = len(andenes)
    # Piso de calle y hall (Z 0) con el corte del subsuelo abierto; losa del subsuelo a -5 m.
    from shapely.geometry import box
    calle = unary_union([box(X_HALL0, 120, 65, 1665), box(-1150, 1385, X_HALL0, 1665), box(-1150, 120, X_HALL0, 230),
                         box(65, 100, 1250, 1660)]).difference(corte_total())
    pisos = rectangulos(calle, 10)
    for c in pisos:
        g.rect('piso3D', *c, -1, 1, COLOR['piso'] if c[0] < 65 else COLOR['vereda'])
    for c in rectangulos(corte_subsuelo(), 5):
        g.rect('pisoSubsuelo3D', *c, Z_SUB - 1, 1, COLOR['subsuelo'])
    resumen['pisos'] = len(pisos)
    # Escalera B2 (hall -> pasillo): 10 escalones de 0,9 m, de Z 0 (oeste) a -5 m (este). Es el área en pendiente
    # escaleraB2 del subsuelo, por donde la gente baja a 0,54 m/s.
    for i in range(10):
        tope = -Z_SUB * (10 - i) / 10 + Z_SUB
        g.rect('escaleraB2_3D', -152 + 9 * i, 949, 9, 50, Z_SUB - 1, tope - Z_SUB + 1, COLOR['escalera'])
    # Escalera B3 (calle Brasil -> vestíbulo): sube hacia el sur, de -5 m (Y 400) a la vereda (Y 455).
    for i in range(10):
        tope = Z_SUB - Z_SUB * (i + 1) / 10
        g.rect('escaleraB3_3D', 183, 400 + 5.5 * i, 22, 5.5, Z_SUB - 1, tope - Z_SUB + 1, COLOR['escalera'])

    # 2. Muros del plano.
    h, v, ob = fusionar(segmentos(msp, MUROS))
    cajas = cajas_de_segmentos(h, v, ob, libre, conservar)
    for c in cajas:
        g.rect('muro3D', *c, 0, ALTO_MURO, COLOR['muro'])
    resumen['muros'] = len(cajas)
    for capa, alto in BAJOS.items():
        h, v, ob = fusionar(segmentos(msp, {capa}))
        cb = cajas_de_segmentos(h, v, ob, libre, conservar, oblicuos=capa != 'CALLES')
        for c in cb:
            g.rect('bajo3D', *c, 0, alto, COLOR['cordon' if capa == 'CALLES' else 'bajo'])
        resumen[capa] = len(cb)

    # 3. Escaleras: 4 peldaños a lo largo del lado mayor.
    esc = escaleras(msp, libre)
    for x, y, w, hh in esc:
        for i in range(4):
            if w >= hh:
                g.rect('escalera3D', x + i * w / 4, y, w / 4, hh, 0, 3 * (i + 1), COLOR['escalera'])
            else:
                g.rect('escalera3D', x, y + i * hh / 4, w, hh / 4, 0, 3 * (i + 1), COLOR['escalera'])
    resumen['escaleras'] = len(esc)

    # 4. Estación de la Línea C (nivel -2, esquema [SUP]): lecho de vías, andenes de 1 m, rieles y escalera desde la
    # zona de escaleras del vestíbulo (X 520-580) hasta el andén central. Los coches van en vestibulo_3d.py.
    x0, y0, x1, y1 = ESTACION_C
    g.rect('lechoLineaC3D', x0, y0, x1 - x0, y1 - y0, Z_LINEA_C - 12, 2, COLOR['lecho'])
    for ya, yb in ANDENES_C:
        g.rect('andenLineaC3D', x0, ya, x1 - x0, yb - ya, Z_LINEA_C - 10, 10, COLOR['lineaC'])
        g.rect('bordeLineaC3D', x0, ya if ya > y0 else yb - 5, x1 - x0, 5, Z_LINEA_C, 0.2, COLOR['borde'])
        if ya > y0 and yb < y1:
            g.rect('bordeLineaC3D', x0, yb - 5, x1 - x0, 5, Z_LINEA_C, 0.2, COLOR['borde'])
    for ya, yb in VIAS_C:
        for yr in (ya + 12, yb - 14):
            g.rect('rielLineaC3D', x0, yr, x1 - x0, 1.5, Z_LINEA_C - 10, 0.6, COLOR['riel'])
    # Escalera vestíbulo -> andén central: 10 escalones de 0,8 m, de Z_SUB (X 585) a Z_LINEA_C (X 665).
    for i in range(10):
        tope = Z_SUB + (Z_LINEA_C - Z_SUB) * (i + 1) / 10
        g.rect('escaleraLineaC3D', 585 + 8 * i, 310, 8, 60, Z_LINEA_C - 10, tope - Z_LINEA_C + 10, COLOR['escalera'])
    resumen['lineaC'] = len(ANDENES_C)

    SALIDA.write_text(g.grupo() + '\n', encoding='utf-8')
    print(f'{SALIDA.name}: {g.n} figuras', resumen)
    vista_control(g)
    if '--insertar' in sys.argv:
        insertar(g.grupo())


def vista_control(g):
    """Planta coloreada por altura sobre el CAD (para revisar alineación y recortes)."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle as R
    fig, ax = plt.subplots(figsize=(18, 11), dpi=110)
    for bloque in g.xml:
        f = {k: float(re.search(fr'<{k}>([-\d.]+)</{k}>', bloque).group(1)) for k in ('X', 'Y', 'Z', 'ZHeight', 'Width', 'Height')}
        top = f['Z'] + f['ZHeight']
        ax.add_patch(R((f['X'], f['Y']), f['Width'], f['Height'], color=plt.cm.viridis((top + 13) / 40), lw=0))
    txt = ALP.read_text(encoding='utf-8')
    for m in re.finditer(r'<Wall>.*?</Wall>', txt, re.S):
        w = m.group(0)
        x0, y0 = map(float, re.search(r'<X>([-\d.]+)</X><Y>([-\d.]+)</Y>', w).groups())
        pts = [(x0 + float(a), y0 + float(b)) for a, b in re.findall(r'<Point><X>([-\d.]+)</X><Y>([-\d.]+)</Y>', w)]
        ax.plot(*zip(*pts), color='red', lw=1)
    ax.set_xlim(-1200, 1300); ax.set_ylim(1700, 0); ax.set_aspect('equal')
    fig.savefig(AQUI / 'plano3d_control.png')


def insertar(grupo):
    txt = ALP.read_text(encoding='utf-8')
    previo = re.search(r'\t\t\t\t<Group>\n\t\t\t\t\t<Id>%d</Id>.*?\n\t\t\t\t</Group>' % ID0, txt, re.S)
    if previo:
        txt = txt[:previo.start()] + grupo + txt[previo.end():]
    else:
        # Va justo después del CAD de fondo de MainPeatonal (mismo nivel de presentación).
        ancla = txt.index('<Name><![CDATA[planoConstitucion]]></Name>')
        fin = txt.index('</CADDrawing>', ancla) + len('</CADDrawing>')
        txt = txt[:fin] + '\n' + grupo + txt[fin:]
    # Vías del Roca hundidas 1,1 m (el lecho y los andenes ya cuentan con eso).
    txt = re.sub(r'(<Name><!\[CDATA\[viaRoca\d\]\]></Name>.*?<Z>)[-\d.]+(</Z>)', rf'\g<1>{Z_VIA}\g<2>', txt, flags=re.S)
    ALP.write_text(txt, encoding='utf-8')
    print('insertado en', ALP.name)


if __name__ == '__main__':
    main()
