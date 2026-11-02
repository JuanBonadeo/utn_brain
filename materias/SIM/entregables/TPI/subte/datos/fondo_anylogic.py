#!/usr/bin/env python3
"""Genera el CAD de fondo de MainPeatonal: plano de Trenes Argentinos + capas de OSM, en coordenadas del modelo.

Uso (desde esta carpeta, con el DXF que produce dwg2dxf; ver georref_plano_sofse.py):
    python3 fondo_anylogic.py /tmp/plano.dxf
Escribe ../plano_constitucion_modelo.dxf (DXF R2000, en metros) junto a SubteConstitucion.alp, para cargarlo en
AnyLogic como CAD Drawing (Presentation > CAD Drawing) en MainPeatonal.

Transformación (rotación de 180°, sin reflejo, más traslación), elegida para que el pasillo subterráneo de OSM
termine en la boca oeste del vestíbulo hipotético y llegue a ella moviéndose hacia +X, como entra el Roca:
    u = -(x - X0) + 8,   v = -(y - Y0) - 36        (u, v en metros; y del CAD hacia arriba)
equivale en el modelo (10 px = 1 m, Y hacia abajo) a  X = 10 u,  Y = -10 v.  Con el origen del CAD en (0, 0) del
modelo, la cruz REFERENCIA cae en la boca oeste del vestíbulo (X = 80, Y = 360). El norte queda a la derecha.
Capas: plano oficial (las del DWG útiles), LINEA_C_OSM, PASILLO_OSM, BOCAS_OSM, ROTULOS, REFERENCIA y MARCO.
El marco fija el recuadro del dibujo: en el .alp el CADDrawing va en X = -1150, Y = 0, Width = 2400, Height = 1660.
"""
import json, math, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SALIDA = AQUI.parent / 'plano_constitucion_modelo.dxf'
X0, Y0 = -2206.0, 2726.9
PX0, PX1, PY0, PY1 = -2335.0, -2085.0, 2690.0, 2855.0          # recorte del DWG (m)
CAPAS = {'EDIFICIOS', 'ESCALERA', 'VIAS', 'CALLES', 'BARANDA', 'CARPINTERIA', 'LIMITE', 'MUROS-NUEVOS', 'MUROS1',
         'HORM', 'ESCA', 'A-CARP', 'LOCALES', '01', '02', '03', '015', 'TMR', 'PROYEC', 'LINE_02', 'ADIF'}
# Marco del CAD en metros (u0, u1, v0, v1): en el modelo, X = -1150, Y = 0, ancho 2400, alto 1660 px.
MARCO = (-115.0, 125.0, -166.0, 0.0)
TIPOS = {'LINE', 'ARC', 'CIRCLE', 'LWPOLYLINE', 'POLYLINE', 'SPLINE', 'ELLIPSE', 'SOLID'}


def uv(x, y):
    return -(x - X0) + 8, -(y - Y0) - 36


def main():
    import ezdxf
    from ezdxf import bbox
    from ezdxf.math import Matrix44
    from ezdxf.addons import Importer
    sys.path.insert(0, str(AQUI))
    from georref_plano_sofse import en, vias_plano, OSM_PARAGOLPES, OSM, X_PARAGOLPES

    src = ezdxf.readfile(sys.argv[1])
    msp = src.modelspace()
    elegidas = []
    for e in msp:
        if e.dxftype() not in TIPOS or e.dxf.layer not in CAPAS:
            continue
        b = bbox.extents([e])
        if b.has_data and PX0 <= b.extmin.x and b.extmax.x <= PX1 and PY0 <= b.extmin.y and b.extmax.y <= PY1:
            elegidas.append(e)

    dst = ezdxf.new('R2000', setup=True)
    dst.units = ezdxf.units.M
    imp = Importer(src, dst)
    imp.import_entities(elegidas, dst.modelspace())
    imp.finalize()
    m = Matrix44.chain(Matrix44.translate(-X0, -Y0, 0), Matrix44.z_rotate(math.pi), Matrix44.translate(8, -36, 0))
    for e in dst.modelspace():
        e.transform(m)
        e.dxf.color = 8          # gris: el plano es fondo
    for nombre, color in (('LINEA_C_OSM', 5), ('PASILLO_OSM', 30), ('BOCAS_OSM', 30), ('ROTULOS', 8), ('REFERENCIA', 1)):
        if nombre not in dst.layers:
            dst.layers.add(nombre, color=color)
    out = dst.modelspace()

    # Capas de OSM, con el mismo ajuste plano <-> OSM que georref_plano_sofse.py.
    osm = {e['id']: e for e in json.load(open(OSM))['elements']}
    za = [complex(X_PARAGOLPES, y) for y in vias_plano(msp)]
    zb = [en(osm[i]['lat'], osm[i]['lon']) for i in OSM_PARAGOLPES]
    ma, mb = sum(za) / len(za), sum(zb) / len(zb)
    k = sum((b - mb) * (a - ma).conjugate() for a, b in zip(za, zb)) / sum(abs(a - ma) ** 2 for a in za)
    t = mb - k * ma

    def p(lat, lon):
        w = (en(lat, lon) - t) / k
        return uv(w.real, w.imag)

    for e in osm.values():
        tg = e.get('tags', {})
        if e['type'] == 'node' and tg.get('railway') == 'subway_entrance':
            out.add_circle(p(e['lat'], e['lon']), 0.8, dxfattribs={'layer': 'BOCAS_OSM'})
        if 'geometry' not in e:
            continue
        pts = [p(q['lat'], q['lon']) for q in e['geometry']]
        if tg.get('railway') == 'platform' and tg.get('layer') == '-2':
            out.add_lwpolyline(pts, dxfattribs={'layer': 'LINEA_C_OSM', 'const_width': 1.2})
        elif tg.get('tunnel') == 'yes' or tg.get('layer') == '-1' or tg.get('highway') == 'steps':
            out.add_lwpolyline(pts, dxfattribs={'layer': 'PASILLO_OSM'})

    def rot(texto, x, y, h=1.6, ang=0):
        out.add_text(texto, height=h, rotation=ang, dxfattribs={'layer': 'ROTULOS'}).set_placement(uv(x, y))
    rot('HALL DEL ROCA - plano de Trenes Argentinos', -2135, 2800, 2.2)
    rot('Paragolpes', -2112, 2845)
    rot('Andenes Linea C (nivel -2, OpenStreetMap)', -2235, 2718)
    rot('Calle Brasil', -2214, 2760, 1.6, 90)
    rot('Calle Lima', -2150, 2696)
    rot('Pasillo subterraneo (OSM)', -2200, 2765, 1.4, 90)
    rot('N ->', -2100, 2697, 2.0)
    # Cruz de control: tiene que caer en la boca oeste del vestíbulo (X = 80, Y = 360 del modelo).
    cx, cy = 8, -36
    out.add_line((cx - 1.5, cy), (cx + 1.5, cy), dxfattribs={'layer': 'REFERENCIA'})
    out.add_line((cx, cy - 1.5), (cx, cy + 1.5), dxfattribs={'layer': 'REFERENCIA'})
    rot('REF (80, 360)', X0 - 1.0, Y0 + 1.0, 1.0)
    # Marco fijo: AnyLogic ajusta el CAD a su recuadro, así que el recuadro tiene que ser conocido y exacto.
    if 'MARCO' not in dst.layers:
        dst.layers.add('MARCO', color=9)
    out.add_lwpolyline([(MARCO[0], MARCO[2]), (MARCO[1], MARCO[2]), (MARCO[1], MARCO[3]), (MARCO[0], MARCO[3])],
                       close=True, dxfattribs={'layer': 'MARCO'})
    dst.saveas(SALIDA)
    ext = bbox.extents(out)
    print(f'{SALIDA}: {len(elegidas)} entidades del plano; extensión u {ext.extmin.x:.1f}..{ext.extmax.x:.1f} m, '
          f'v {ext.extmin.y:.1f}..{ext.extmax.y:.1f} m -> modelo X {10*ext.extmin.x:.0f}..{10*ext.extmax.x:.0f}, '
          f'Y {-10*ext.extmax.y:.0f}..{-10*ext.extmin.y:.0f} px')


if __name__ == '__main__':
    main()
