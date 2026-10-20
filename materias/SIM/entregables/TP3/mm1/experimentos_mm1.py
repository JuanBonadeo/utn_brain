"""
Experimentos sobre el modelo M/M/1: corre los barridos que pide la consigna,
con multiples corridas por experimento, compara contra la teoria y genera
los graficos.

Barridos:
  - Tasa de arribo = 25, 50, 75, 100, 125% de la tasa de servicio (rho).
  - Tamanos de cola finita = 0, 2, 5, 10, 50 (probabilidad de denegacion).
  - Minimo 10 corridas por experimento (promedio + intervalo de confianza).

Ejecutar:
    python experimentos_mm1.py
    python experimentos_mm1.py --corridas 20 --tiempo 20000
"""

from __future__ import annotations

import argparse
import math
import statistics
from pathlib import Path

import matplotlib
matplotlib.use('Agg')   # backend sin ventana: solo guarda PNGs
import matplotlib.pyplot as plt

from simulacion_mm1 import simular_mm1
from teorico_mm1 import mm1_infinita, mm1_finita, prob_n_infinita

# --- Parametros del estudio (faciles de cambiar para mostrar en clase) ---
MU = 1.0                                  # tasa de servicio de referencia
CARGAS = [0.25, 0.50, 0.75, 1.00, 1.25]   # rho = lambda/mu a barrer
COLAS  = [0, 2, 5, 10, 50]                # tamanos de cola finita a barrer

GRAFICAS_DIR = Path(__file__).resolve().parents[1] / 'graficas'
GRAFICAS_DIR.mkdir(exist_ok=True)


def intervalo_confianza(datos: list[float], conf: float = 0.95) -> tuple[float, float]:
    """Devuelve (media, semiancho del IC) usando aproximacion normal (z=1.96)."""
    media = statistics.fmean(datos)
    if len(datos) < 2:
        return media, 0.0
    desvio = statistics.stdev(datos)
    z = 1.96  # 95%
    semiancho = z * desvio / math.sqrt(len(datos))
    return media, semiancho


def correr_experimento(lam, mu, tiempo, corridas, cola_max=None):
    """Corre 'corridas' simulaciones y agrega las medidas (media + IC)."""
    medidas = {k: [] for k in ('L', 'Lq', 'W', 'Wq', 'rho', 'P_deneg')}
    ultima = None
    for i in range(corridas):
        r = simular_mm1(lam, mu, tiempo, cola_max=cola_max, semilla=1000 + i)
        medidas['L'].append(r.L)
        medidas['Lq'].append(r.Lq)
        medidas['W'].append(r.W)
        medidas['Wq'].append(r.Wq)
        medidas['rho'].append(r.rho)
        medidas['P_deneg'].append(r.prob_denegacion)
        ultima = r
    resumen = {k: intervalo_confianza(v) for k, v in medidas.items()}
    return resumen, ultima


# ------------------------------------------------------------------ #
#  EXPERIMENTO 1: barrido de carga (rho) con cola infinita            #
# ------------------------------------------------------------------ #
def experimento_cargas(tiempo, corridas):
    print('\n' + '=' * 78)
    print('EXPERIMENTO 1: barrido de carga rho (cola infinita) — Teorico vs Python')
    print('=' * 78)
    print(f'{"rho":>5} | {"L sim":>16} {"L teo":>8} | {"W sim":>16} {"W teo":>8} | {"rho sim":>8}')
    print('-' * 78)

    filas = []
    for rho in CARGAS:
        lam = rho * MU
        resumen, ultima = correr_experimento(lam, MU, tiempo, corridas)
        teo = mm1_infinita(lam, MU)
        L_sim, L_ic = resumen['L']
        W_sim, W_ic = resumen['W']
        rho_sim, _ = resumen['rho']
        L_teo = f'{teo.L:8.3f}' if teo.estable else '    inf '
        W_teo = f'{teo.W:8.3f}' if teo.estable else '    inf '
        print(f'{rho:>5.2f} | {L_sim:8.3f} +-{L_ic:5.3f} {L_teo} | '
              f'{W_sim:8.3f} +-{W_ic:5.3f} {W_teo} | {rho_sim:8.3f}')
        filas.append((rho, resumen, teo, ultima))
    return filas


def grafico_teorico_vs_sim(filas):
    """Barras: L de la simulacion (con IC) vs L teorico, por cada rho."""
    estables = [f for f in filas if f[2].estable]
    rhos = [f[0] for f in estables]
    L_sim = [f[1]['L'][0] for f in estables]
    L_ic  = [f[1]['L'][1] for f in estables]
    L_teo = [f[2].L for f in estables]

    x = range(len(rhos))
    ancho = 0.38
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar([i - ancho/2 for i in x], L_sim, ancho, yerr=L_ic, capsize=4,
           label='Simulacion (Python)', color='#4C72B0')
    ax.bar([i + ancho/2 for i in x], L_teo, ancho,
           label='Teorico', color='#DD8452')
    ax.set_xticks(list(x))
    ax.set_xticklabels([f'{r:.2f}' for r in rhos])
    ax.set_xlabel('Utilizacion rho = lambda/mu')
    ax.set_ylabel('L (clientes promedio en el sistema)')
    ax.set_title('M/M/1: L teorico vs simulado (10+ corridas, IC 95%)')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    fig.tight_layout()
    ruta = GRAFICAS_DIR / 'mm1_01_teorico_vs_sim.png'
    fig.savefig(ruta, dpi=110)
    plt.close(fig)
    print(f'  [grafico] {ruta.name}')


def grafico_convergencia(filas):
    """Evolucion de L a lo largo del tiempo de simulacion (convergencia)."""
    fig, ax = plt.subplots(figsize=(8, 5))
    for rho, resumen, teo, ultima in filas:
        if ultima.tiempos:
            ax.plot(ultima.tiempos, ultima.serie_L, label=f'rho={rho:.2f}', lw=1.2)
        if teo.estable:
            ax.axhline(teo.L, color='gray', ls='--', lw=0.6)
    ax.set_xlabel('Tiempo de simulacion')
    ax.set_ylabel('L (promedio acumulado)')
    ax.set_title('M/M/1: convergencia de L vs tiempo de simulacion')
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    ruta = GRAFICAS_DIR / 'mm1_02_convergencia.png'
    fig.savefig(ruta, dpi=110)
    plt.close(fig)
    print(f'  [grafico] {ruta.name}')


def grafico_prob_n(filas):
    """Distribucion P(n): probabilidad de encontrar n clientes en el sistema."""
    fig, ax = plt.subplots(figsize=(8, 5))
    for rho, resumen, teo, ultima in filas:
        if not teo.estable:
            continue
        ns = sorted(k for k in ultima.prob_n if k <= 12)
        p_sim = [ultima.prob_n[n] for n in ns]
        p_teo = [prob_n_infinita(rho * MU, MU, n) for n in ns]
        linea, = ax.plot(ns, p_sim, 'o-', ms=4, lw=1, label=f'rho={rho:.2f} (sim)')
        ax.plot(ns, p_teo, 'x--', color=linea.get_color(), lw=0.8, alpha=0.7)
    ax.set_xlabel('n (clientes en el sistema)')
    ax.set_ylabel('P(N = n)')
    ax.set_title('M/M/1: distribucion P(n)  — solido=sim, punteado=teorico')
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    ruta = GRAFICAS_DIR / 'mm1_03_prob_n.png'
    fig.savefig(ruta, dpi=110)
    plt.close(fig)
    print(f'  [grafico] {ruta.name}')


# ------------------------------------------------------------------ #
#  EXPERIMENTO 2: probabilidad de denegacion vs tamano de cola        #
# ------------------------------------------------------------------ #
def experimento_denegacion(tiempo, corridas):
    print('\n' + '=' * 78)
    print('EXPERIMENTO 2: probabilidad de denegacion vs tamano de cola K')
    print('=' * 78)
    print(f'{"rho":>5} {"K":>4} | {"P(deneg) sim":>14} {"P(deneg) teo":>14}')
    print('-' * 78)

    # Para denegacion tienen sentido las cargas altas (saturacion).
    cargas_deneg = [0.75, 1.00, 1.25]
    datos = {}   # rho -> (lista K, lista P_sim, lista P_teo)
    for rho in cargas_deneg:
        lam = rho * MU
        Ks, P_sim_l, P_teo_l = [], [], []
        for K in COLAS:
            resumen, _ = correr_experimento(lam, MU, tiempo, corridas, cola_max=K)
            P_sim, P_ic = resumen['P_deneg']
            P_teo = mm1_finita(lam, MU, K)['P_bloqueo']
            print(f'{rho:>5.2f} {K:>4} | {P_sim:>9.4f} +-{P_ic:4.3f} {P_teo:>14.4f}')
            Ks.append(K); P_sim_l.append(P_sim); P_teo_l.append(P_teo)
        datos[rho] = (Ks, P_sim_l, P_teo_l)
    return datos


def grafico_denegacion(datos):
    fig, ax = plt.subplots(figsize=(8, 5))
    for rho, (Ks, P_sim, P_teo) in datos.items():
        linea, = ax.plot(Ks, P_sim, 'o-', label=f'rho={rho:.2f} (sim)')
        ax.plot(Ks, P_teo, 'x--', color=linea.get_color(), alpha=0.7)
    ax.set_xlabel('Tamano de cola K (capacidad del pool)')
    ax.set_ylabel('P(denegacion de servicio)')
    ax.set_title('M/M/1/K: probabilidad de rechazo vs tamano de cola\n(solido=sim, punteado=teorico)')
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    ruta = GRAFICAS_DIR / 'mm1_04_denegacion.png'
    fig.savefig(ruta, dpi=110)
    plt.close(fig)
    print(f'  [grafico] {ruta.name}')


def main():
    p = argparse.ArgumentParser(description='Experimentos M/M/1.')
    p.add_argument('--corridas', type=int, default=10, help='Corridas por experimento (>=10).')
    p.add_argument('--tiempo', type=float, default=20000.0, help='Tiempo simulado por corrida.')
    args = p.parse_args()

    print(f'Configuracion: mu={MU}, {args.corridas} corridas/experimento, '
          f'tiempo={args.tiempo} por corrida')

    filas = experimento_cargas(args.tiempo, args.corridas)
    grafico_teorico_vs_sim(filas)
    grafico_convergencia(filas)
    grafico_prob_n(filas)

    datos = experimento_denegacion(args.tiempo, args.corridas)
    grafico_denegacion(datos)

    print(f'\nListo. Graficos guardados en: {GRAFICAS_DIR}')


if __name__ == '__main__':
    main()
