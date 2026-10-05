#!/usr/bin/env python3
"""Análisis de las corridas de producción E0 (20 molinetes) contra E1 (22): diferencias apareadas,
IC t de Student (Bonferroni k = 3 para las primarias D4) y n necesario (Law §9.5).

Uso: python3 analisis_corridas.py [corridas_peatonales.csv]
Sin dependencias externas: el cuantil t se obtiene por integración numérica (Simpson) y bisección.
"""
import math, statistics as st, sys

CAMPOS = ['generados', 'desviados', 'proc_corte', 'proc_drenaje', 'espera_media', 'p90', 'prop30', 'Lq',
          'qmax', 'drenaje_final', 'util', 'disp_util', 'pico_n', 'pico_media', 'pico_p90']
MEDIDAS = [('p90', 'P90 de espera (s)', True), ('prop30', 'Proporción con espera > 30 s', True),
           ('pico_p90', 'P90 cohorte pico (s)', True), ('espera_media', 'Espera media (s)', False),
           ('pico_media', 'Espera media cohorte pico (s)', False), ('Lq', 'Lq (personas)', False),
           ('qmax', 'Cola máxima', False), ('util', 'Utilización media', False),
           ('drenaje_final', 'Tiempo de drenaje final (s)', False)]


def tcdf(x, v, N=20000):
    c = math.gamma((v + 1) / 2) / (math.sqrt(v * math.pi) * math.gamma(v / 2))
    h = x / N
    s = sum((1 if i in (0, N) else 4 if i % 2 else 2) * c * (1 + (i * h) ** 2 / v) ** (-(v + 1) / 2) for i in range(N + 1))
    return 0.5 + s * h / 3


def tinv(p, v):
    lo, hi = 0.0, 20.0
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if tcdf(mid, v) < p else (lo, mid)
    return (lo + hi) / 2


def main(archivo='corridas_peatonales.csv', alfa=0.05):
    d = {}
    for linea in open(archivo, encoding='utf-8'):
        if linea.startswith('CSV_PEATONAL;'):
            r = linea.strip().split(';')
            d.setdefault(int(r[2]), {})[r[1]] = dict(zip(CAMPOS, map(float, r[3:])))
    pares = sorted(s for s in d if {'E0', 'E1'} <= set(d[s]))
    n, k = len(pares), sum(1 for *_, p in MEDIDAS if p)
    tb, t95 = tinv(1 - alfa / k / 2, n - 1), tinv(1 - alfa / 2, n - 1)
    print(f'{n} pares; t({alfa}/{k}, {n-1}) = {tb:.4f} (primarias, Bonferroni); t({alfa}, {n-1}) = {t95:.4f}')
    print(f"| Medida | E0 | E1 | D = E1 - E0 | s(D) | IC | Cambio |\n|---|---:|---:|---:|---:|---|---:|")
    for clave, nombre, prim in MEDIDAS:
        D = [d[s]['E1'][clave] - d[s]['E0'][clave] for s in pares]
        m, sd = st.mean(D), st.stdev(D)
        h = (tb if prim else t95) * sd / math.sqrt(n)
        e0 = st.mean(d[s]['E0'][clave] for s in pares)
        e1 = st.mean(d[s]['E1'][clave] for s in pares)
        nivel = f'{100 * (1 - alfa / k):.2f} %' if prim else '95 %'
        print(f"| {'**' + nombre + '**' if prim else nombre} | {e0:.3f} | {e1:.3f} | {m:.3f} | {sd:.3f} | "
              f"[{m - h:.3f}; {m + h:.3f}] ({nivel}) | {100 * m / e0:+.1f} % |")
    for clave, beta in (('p90', 1.0), ('prop30', 0.01), ('pico_p90', 1.0)):
        sd = st.stdev(d[s]['E1'][clave] - d[s]['E0'][clave] for s in pares)
        nn = next(i for i in range(2, 1000) if tinv(1 - alfa / k / 2, i - 1) * sd / math.sqrt(i) <= beta)
        print(f'n* para {clave} con semiancho {beta}: {nn}')


if __name__ == '__main__':
    main(*sys.argv[1:2])
