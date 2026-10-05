#!/usr/bin/env python3
"""Distancia del andén del Roca a la boca de la Línea C en Plaza Constitución, desde OpenStreetMap.

Uso: python3 medir_acceso_osm.py            (consulta Overpass y guarda osm_constitucion.json)
     python3 medir_acceso_osm.py --offline  (reusa osm_constitucion.json)

Método (2026-10-05):
- Cabecera de cada vía del Roca = nodo railway=buffer_stop del lado del hall (fila de paragolpes a
  lat -34.62884; 14 vías).
- Bocas de la Línea C dentro o junto al hall = nodos railway=subway_entrance al sur de lat -34.6280.
- D = recorrido en L (|dx| + |dy|) desde cada paragolpes hasta la boca más cercana; se informa
  mínimo, mediana y máximo entre vías. Es la distancia de los primeros pasajeros (coche delantero).
- La demora del modelo usa la mediana de D y la fórmula de la §5 del plan:
  D/v + h/v_escalera, con h = 5 m [SUP: un nivel, el vestíbulo Principal está bajo el hall].
Fuente: © colaboradores de OpenStreetMap (ODbL), API Overpass.
"""
import json, math, statistics as st, subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ARCH = AQUI / 'osm_constitucion.json'
Q = ('[out:json][timeout:60];(nwr(around:450,-34.6276,-58.3810)["railway"~"platform|subway_entrance|station|buffer_stop"];'
     'nwr(around:450,-34.6276,-58.3810)["public_transport"~"platform|station"];);out tags center;')


def xy(lat, lon, lat0=-34.6285, lon0=-58.3805):
    return ((lon - lon0) * 111320 * math.cos(math.radians(lat0)), (lat - lat0) * 110574)


def main():
    if '--offline' not in sys.argv:
        subprocess.run(['curl', '-s', '-m', '90', '-A', 'UTN-TPI-simulacion/1.0 (academico)', '-H', 'Accept: application/json',
                        '--data-urlencode', f'data={Q}', 'https://overpass-api.de/api/interpreter', '-o', str(ARCH)], check=True)
    d = json.load(open(ARCH))
    buf = [e for e in d['elements'] if e.get('tags', {}).get('railway') == 'buffer_stop' and abs(e['lat'] + 34.62884) < 0.00005]
    hall = [e for e in d['elements'] if e.get('tags', {}).get('railway') == 'subway_entrance' and e['lat'] < -34.6280]
    D = []
    for b in buf:
        bx, by = xy(b['lat'], b['lon'])
        D.append(min(abs(bx - xy(e['lat'], e['lon'])[0]) + abs(by - xy(e['lat'], e['lon'])[1]) for e in hall))
    med, h = st.median(D), 5.0
    print(f'{len(buf)} cabeceras, {len(hall)} bocas del hall; D en L: min {min(D):.0f} m, mediana {med:.0f} m, max {max(D):.0f} m')
    for nombre, v, ve in (('optimista', 1.25, 0.30), ('intermedio', 0.95, 0.30), ('pesimista', 0.63, 0.20)):
        print(f'  demora {nombre}: {med:.0f}/{v} + {h:.0f}/{ve} = {med / v + h / ve:.0f} s')


if __name__ == '__main__':
    main()
