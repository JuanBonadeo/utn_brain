#!/usr/bin/env python3
"""Validación del modelo con lo que SBASE sí mide (2026-11-04).

1. Caudal por ventana de 15 min: validaciones simuladas contra las observadas del mismo día SBASE (archivo
   <salida>_ventanas.csv, filas VENTANAS_PEATONAL). Como el día es la entrada del modelo, no es una validación
   independiente: muestra si el modelo retrasa o recorta el flujo (cola que se arrastra de una ventana a otra).
2. Reparto entre molinetes: CV de las validaciones entre los molinetes habilitados en E0, contra el CV observado
   entre los 21 molinetes del vestíbulo Principal (datos/sbase_molinetes.csv). Ésta sí es independiente: el
   reparto no es una entrada, sale de la regla de elección de cola (elegirColaPed).

Uso: python3 validacion_corridas.py [corridas_peatonales.csv]
"""
import csv, math, statistics as st, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
VENTANAS = ['07:00', '07:15', '07:30', '07:45', '08:00', '08:15', '08:30', '08:45', '09:00', '09:15']


def cv_sbase():
    filas = list(csv.DictReader(open(AQUI / 'datos' / 'sbase_molinetes.csv', encoding='utf-8'), delimiter=';'))
    x = [float(f['pax_franja_media_dia']) for f in filas]
    m = st.fmean(x)
    return math.sqrt(sum((v - m) ** 2 for v in x) / len(x)) / m, len(x), max(x) / min(x)


def main(archivo='corridas_peatonales.csv'):
    ruta = Path(archivo)
    ventanas = ruta.with_name(ruta.stem + '_ventanas.csv')
    filas = [l.strip().split(';') for l in open(ventanas, encoding='utf-8') if l.startswith('VENTANAS_PEATONAL;')]
    e0 = [f for f in filas if f[1] == 'E0']
    print(f'## Caudal por ventana (E0, {len(e0)} réplicas; sim - obs del mismo día)')
    print('| Ventana | obs medio | sim medio | sesgo medio | sesgo % | |sim - obs| máx |\n|---|---:|---:|---:|---:|---:|')
    for w, nombre in enumerate(VENTANAS):
        sim = [float(f[4 + w]) for f in e0]
        obs = [float(f[14 + w]) for f in e0]
        dif = [a - b for a, b in zip(sim, obs)]
        print(f'| {nombre} | {st.fmean(obs):.0f} | {st.fmean(sim):.0f} | {st.fmean(dif):+.1f} | '
              f'{100 * st.fmean(dif) / st.fmean(obs):+.1f} % | {max(abs(x) for x in dif):.0f} |')
    cv_obs, n_obs, maxmin = cv_sbase()
    cvs = [float(l.strip().split(';')[20]) for l in open(ruta, encoding='utf-8')
           if l.startswith('CSV_PEATONAL;E0;')]
    print(f'\n## Reparto entre molinetes\nSBASE: CV = {cv_obs:.3f} entre {n_obs} molinetes (máx/mín = {maxmin:.1f})')
    if cvs:
        m = st.fmean(cvs); s = st.stdev(cvs) if len(cvs) > 1 else 0
        print(f'Modelo E0: CV = {m:.3f} (desvío entre réplicas {s:.3f}, {len(cvs)} réplicas)')
        print('Lectura: si el CV del modelo es mucho menor, la regla de elección reparte más parejo que la gente '
              'real (que prefiere los molinetes cercanos a su boca de entrada).')


if __name__ == '__main__':
    main(*sys.argv[1:2])
