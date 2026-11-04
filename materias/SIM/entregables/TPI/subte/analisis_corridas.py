#!/usr/bin/env python3
"""Análisis de las corridas de producción: E1 (22 molinetes), E3 (20, validación rápida) y E13 (22, validación
rápida) contra E0 (20 molinetes, validación intermedia). Diferencias apareadas por semilla y día SBASE, IC t de
Student con Bonferroni k = 3 primarias x 3 comparaciones = 9 (Unidad 9 §9.8, Unidad 10 §10.2 y §10.4) y n
necesario (Law §9.5).

Uso: python3 analisis_corridas.py [corridas_peatonales.csv]
Sin dependencias externas: el cuantil t se obtiene por integración numérica (Simpson) y bisección.
"""
import math, statistics as st, sys

CAMPOS = ['generados', 'desviados', 'proc_corte', 'proc_drenaje', 'espera_media', 'p90', 'prop30', 'Lq',
          'qmax', 'drenaje_final', 'util', 'disp_util', 'pico_n', 'pico_media', 'pico_p90', 'dia',
          'transito_p90', 'cv_molinetes']
ALTERNATIVAS = ('E1', 'E3', 'E13')
MEDIDAS = [('p90', 'P90 de espera (s)', True), ('prop30', 'Proporción con espera > 30 s', True),
           ('pico_p90', 'P90 cohorte pico (s)', True), ('espera_media', 'Espera media (s)', False),
           ('pico_media', 'Espera media cohorte pico (s)', False), ('Lq', 'Lq (personas)', False),
           ('qmax', 'Cola máxima', False), ('util', 'Utilización media', False),
           ('drenaje_final', 'Tiempo de drenaje final (s)', False),
           ('transito_p90', 'P90 de tránsito del Roca a la cola (s)', False),
           ('cv_molinetes', 'CV de validaciones entre molinetes', False)]


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
    alternativas = [a for a in ALTERNATIVAS if any({'E0', a} <= set(v) for v in d.values())]
    k = sum(1 for *_, p in MEDIDAS if p) * len(alternativas)
    for alt in alternativas:
        pares = sorted(s for s in d if {'E0', alt} <= set(d[s]))
        n = len(pares)
        if n < 2:
            print(f'{alt}: {n} pares, no alcanza para un IC')
            continue
        assert all(d[s]['E0']['dia'] == d[s][alt]['dia'] for s in pares), f'{alt}: días distintos en un par'
        tb, t95 = tinv(1 - alfa / k / 2, n - 1), tinv(1 - alfa / 2, n - 1)
        dias = len({d[s]['E0']['dia'] for s in pares})
        print(f'\n## {alt} contra E0: {n} pares ({dias} días SBASE distintos); t({alfa}/{k}, {n-1}) = {tb:.4f} '
              f'(primarias, Bonferroni); t({alfa}, {n-1}) = {t95:.4f}')
        print(f"| Medida | E0 | {alt} | D = {alt} - E0 | s(D) | IC | Cambio |\n|---|---:|---:|---:|---:|---|---:|")
        for clave, nombre, prim in MEDIDAS:
            D = [d[s][alt][clave] - d[s]['E0'][clave] for s in pares]
            m, sd = st.mean(D), st.stdev(D)
            h = (tb if prim else t95) * sd / math.sqrt(n)
            e0 = st.mean(d[s]['E0'][clave] for s in pares)
            e1 = st.mean(d[s][alt][clave] for s in pares)
            nivel = f'{100 * (1 - alfa / k):.2f} %' if prim else '95 %'
            cambio = f'{100 * m / e0:+.1f} %' if e0 else '—'
            print(f"| {'**' + nombre + '**' if prim else nombre} | {e0:.3f} | {e1:.3f} | {m:.3f} | {sd:.3f} | "
                  f"[{m - h:.3f}; {m + h:.3f}] ({nivel}) | {cambio} |")
        # Números aleatorios comunes (Unidad 10 §10.5): covarianza entre E0 y la alternativa en el P90.
        x0 = [d[s]['E0']['p90'] for s in pares]; x1 = [d[s][alt]['p90'] for s in pares]
        if n > 2 and st.stdev(x0) > 0 and st.stdev(x1) > 0:
            cov = sum((a - st.mean(x0)) * (b - st.mean(x1)) for a, b in zip(x0, x1)) / (n - 1)
            print(f'Cov(P90 E0, P90 {alt}) = {cov:.3f}; Var(D) = {st.variance([b - a for a, b in zip(x0, x1)]):.3f} '
                  f'frente a Var(E0) + Var({alt}) = {st.variance(x0) + st.variance(x1):.3f}')
        for clave, beta in (('p90', 1.0), ('prop30', 0.01), ('pico_p90', 1.0)):
            sd = st.stdev(d[s][alt][clave] - d[s]['E0'][clave] for s in pares)
            nn = next(i for i in range(2, 1000) if tinv(1 - alfa / k / 2, i - 1) * sd / math.sqrt(i) <= beta)
            print(f'n* para {clave} con semiancho {beta}: {nn}')


if __name__ == '__main__':
    main(*sys.argv[1:2])
