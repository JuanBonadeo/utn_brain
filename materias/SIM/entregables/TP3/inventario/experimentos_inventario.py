"""
Experimentos sobre el modelo de inventario periodico (s, S).

Que hace:
  - Barre una grilla de politicas (s, S) y evalua cada una con varias corridas.
  - Encuentra la politica de MINIMO costo total (la "politica optima").
  - Desglosa los tres costos (orden / holding / faltante) para ver el trade-off.
  - Genera graficos: mapa de calor del costo, desglose de costos, trayectoria
    del inventario y convergencia del costo en el tiempo.

Minimo 10 corridas por cada combinacion (s, S).

Ejecutar:
    python experimentos_inventario.py
    python experimentos_inventario.py --corridas 15 --tiempo 1500
"""

from __future__ import annotations

import argparse
import math
import statistics
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from simulacion_inventario import simular_inventario

# --- Grilla de politicas a evaluar (faciles de cambiar para mostrar en clase) ---
VALORES_s = [10, 20, 30, 40, 50]          # punto de reorden
VALORES_S = [40, 50, 60, 70, 80, 90]      # nivel objetivo

GRAFICAS_DIR = Path(__file__).resolve().parents[1] / 'graficas'
GRAFICAS_DIR.mkdir(exist_ok=True)


def media_ic(datos, conf_z=1.96):
    media = statistics.fmean(datos)
    if len(datos) < 2:
        return media, 0.0
    return media, conf_z * statistics.stdev(datos) / math.sqrt(len(datos))


def evaluar_politica(s, S, tiempo, corridas, intervalo_revision=1.0):
    """Evalua una politica (s, S) con varias corridas; devuelve medias de costos."""
    totales, ordenes, holdings, faltantes = [], [], [], []
    ultima = None
    for i in range(corridas):
        r = simular_inventario(
            s, S, tiempo,
            intervalo_revision=intervalo_revision,
            semilla=2000 + i,
        )
        totales.append(r.costo_total_prom)
        ordenes.append(r.costo_orden_prom)
        holdings.append(r.costo_holding_prom)
        faltantes.append(r.costo_faltante_prom)
        ultima = r
    return {
        'total': media_ic(totales),
        'orden': media_ic(ordenes),
        'holding': media_ic(holdings),
        'faltante': media_ic(faltantes),
        'ultima': ultima,
    }


def experimento_grilla(tiempo, corridas, intervalo_revision):
    """Evalua toda la grilla (s, S) y reporta la politica optima."""
    print('\n' + '=' * 70)
    print('EXPERIMENTO: busqueda de la politica (s, S) optima')
    print(f'(costo total promedio por unidad de tiempo, {corridas} corridas c/u)')
    print('=' * 70)

    # Encabezado de la tabla.
    print(f'{"s\\S":>5}', end='')
    for S in VALORES_S:
        print(f'{S:>9}', end='')
    print()

    resultados = {}   # (s, S) -> dict
    mejor = None
    for s in VALORES_s:
        print(f'{s:>5}', end='')
        for S in VALORES_S:
            if S <= s:
                print(f'{"-":>9}', end='')
                continue
            res = evaluar_politica(s, S, tiempo, corridas, intervalo_revision)
            resultados[(s, S)] = res
            total = res['total'][0]
            print(f'{total:>9.1f}', end='')
            if mejor is None or total < mejor[2]:
                mejor = (s, S, total)
        print()

    print('-' * 70)
    s_opt, S_opt, costo_opt = mejor
    print(f'>> Politica OPTIMA: s={s_opt}, S={S_opt}  ->  costo total = {costo_opt:.2f}/tiempo')
    res_opt = resultados[(s_opt, S_opt)]
    print(f'   Desglose:  orden={res_opt["orden"][0]:.2f}   '
          f'holding={res_opt["holding"][0]:.2f}   faltante={res_opt["faltante"][0]:.2f}')
    return resultados, mejor


# ------------------------------------------------------------------ #
#  Graficos                                                           #
# ------------------------------------------------------------------ #
def grafico_mapa_calor(resultados):
    """Mapa de calor del costo total sobre la grilla (s, S)."""
    import numpy as np
    M = np.full((len(VALORES_s), len(VALORES_S)), np.nan)
    for i, s in enumerate(VALORES_s):
        for j, S in enumerate(VALORES_S):
            if (s, S) in resultados:
                M[i, j] = resultados[(s, S)]['total'][0]

    fig, ax = plt.subplots(figsize=(8, 5))
    im = ax.imshow(M, cmap='viridis_r', aspect='auto', origin='lower')
    ax.set_xticks(range(len(VALORES_S)), [str(S) for S in VALORES_S])
    ax.set_yticks(range(len(VALORES_s)), [str(s) for s in VALORES_s])
    ax.set_xlabel('S (nivel objetivo)')
    ax.set_ylabel('s (punto de reorden)')
    ax.set_title('Costo total por politica (s, S)\nmas claro/amarillo = mejor (menor costo)')
    fig.colorbar(im, ax=ax, label='Costo total / tiempo')
    # Marcar el optimo.
    mejor = min((v['total'][0], k) for k, v in resultados.items())[1]
    j = VALORES_S.index(mejor[1]); i = VALORES_s.index(mejor[0])
    ax.plot(j, i, 'r*', ms=18, label=f'optimo ({mejor[0]},{mejor[1]})')
    ax.legend()
    fig.tight_layout()
    ruta = GRAFICAS_DIR / 'inv_01_mapa_calor.png'
    fig.savefig(ruta, dpi=110); plt.close(fig)
    print(f'  [grafico] {ruta.name}')


def grafico_desglose(resultados, S_fijo):
    """Desglose de los 3 costos vs s, para un S fijo (muestra el trade-off)."""
    ss = [s for s in VALORES_s if (s, S_fijo) in resultados]
    orden    = [resultados[(s, S_fijo)]['orden'][0] for s in ss]
    holding  = [resultados[(s, S_fijo)]['holding'][0] for s in ss]
    faltante = [resultados[(s, S_fijo)]['faltante'][0] for s in ss]
    total    = [resultados[(s, S_fijo)]['total'][0] for s in ss]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(ss, orden, 'o-', label='Orden')
    ax.plot(ss, holding, 's-', label='Holding (mantenimiento)')
    ax.plot(ss, faltante, '^-', label='Faltante')
    ax.plot(ss, total, 'D-', color='black', lw=2, label='TOTAL')
    ax.set_xlabel('s (punto de reorden)')
    ax.set_ylabel('Costo por unidad de tiempo')
    ax.set_title(f'Desglose de costos vs s  (S={S_fijo} fijo)\nel total es un compromiso entre los tres')
    ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout()
    ruta = GRAFICAS_DIR / 'inv_02_desglose_costos.png'
    fig.savefig(ruta, dpi=110); plt.close(fig)
    print(f'  [grafico] {ruta.name}')


def grafico_trayectoria(mejor, intervalo_revision):
    """Trayectoria del nivel de inventario en el tiempo (diente de sierra)."""
    s_opt, S_opt, _ = mejor
    r = simular_inventario(
        s_opt, S_opt, 100.0,
        intervalo_revision=intervalo_revision,
        semilla=7,
    )
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.plot(r.tiempos, r.serie_nivel, lw=1, color='#4C72B0')
    ax.axhline(s_opt, color='orange', ls='--', lw=1, label=f's={s_opt} (reorden)')
    ax.axhline(S_opt, color='green', ls='--', lw=1, label=f'S={S_opt} (objetivo)')
    ax.axhline(0, color='red', ls=':', lw=1, label='faltante (stock<0)')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Nivel de inventario')
    ax.set_title(f'Trayectoria del inventario con la politica optima (s={s_opt}, S={S_opt})')
    ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout()
    ruta = GRAFICAS_DIR / 'inv_03_trayectoria.png'
    fig.savefig(ruta, dpi=110); plt.close(fig)
    print(f'  [grafico] {ruta.name}')


def grafico_convergencia(mejor, intervalo_revision):
    """Costo total acumulado por tiempo, convergiendo a su valor estable."""
    s_opt, S_opt, _ = mejor
    fig, ax = plt.subplots(figsize=(8, 5))
    for sem in range(5):
        r = simular_inventario(
            s_opt, S_opt, 2000.0,
            intervalo_revision=intervalo_revision,
            semilla=500 + sem,
        )
        # costo por unidad de tiempo acumulado
        por_tiempo = [c / t if t > 0 else 0 for c, t in zip(r.serie_costo_total, r.tiempos)]
        ax.plot(r.tiempos, por_tiempo, lw=1, alpha=0.8, label=f'corrida {sem+1}')
    ax.set_xlabel('Tiempo de simulacion')
    ax.set_ylabel('Costo total acumulado / tiempo')
    ax.set_title(f'Convergencia del costo total (politica optima s={s_opt}, S={S_opt})')
    ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout()
    ruta = GRAFICAS_DIR / 'inv_04_convergencia.png'
    fig.savefig(ruta, dpi=110); plt.close(fig)
    print(f'  [grafico] {ruta.name}')


def main():
    p = argparse.ArgumentParser(description='Experimentos de inventario (s, S).')
    p.add_argument('--corridas', type=int, default=10, help='Corridas por politica (>=10).')
    p.add_argument('--tiempo', type=float, default=1200.0, help='Tiempo simulado por corrida.')
    p.add_argument('--revision', type=float, default=1.0,
                   help='Intervalo entre revisiones de inventario.')
    args = p.parse_args()

    print(f'Buscando politica optima en grilla s={VALORES_s} x S={VALORES_S}')
    resultados, mejor = experimento_grilla(args.tiempo, args.corridas, args.revision)

    grafico_mapa_calor(resultados)
    grafico_desglose(resultados, S_fijo=mejor[1])
    grafico_trayectoria(mejor, args.revision)
    grafico_convergencia(mejor, args.revision)

    print(f'\nListo. Graficos guardados en: {GRAFICAS_DIR}')


if __name__ == '__main__':
    main()
