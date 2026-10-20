"""
Formulas analiticas (teoricas) para colas M/M/1 y M/M/1/K.

Esta es la "fuente de datos teorica" contra la que se compara la simulacion.
Todas las formulas son de regimen estacionario (steady-state), es decir,
el comportamiento promedio del sistema una vez que se estabiliza.

Notacion:
    lam (lambda) = tasa de arribos
    mu           = tasa de servicio
    rho = lam/mu = utilizacion (fraccion de tiempo que el servidor esta ocupado)
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TeoricoMM1:
    rho: float
    L:  float
    Lq: float
    W:  float
    Wq: float
    estable: bool


def mm1_infinita(lam: float, mu: float) -> TeoricoMM1:
    """
    M/M/1 con cola infinita.

    rho = lam / mu

    Si rho >= 1 el sistema es INESTABLE: la cola crece sin limite y no
    existe un promedio estacionario (las formulas dan infinito). Esto modela
    un servidor que recibe mas trabajo del que puede procesar.

    Formulas (validas solo si rho < 1):
        L  = rho / (1 - rho)            clientes en el sistema
        Lq = rho^2 / (1 - rho)          clientes en cola
        W  = 1 / (mu - lam)             tiempo en el sistema
        Wq = rho / (mu - lam)           tiempo en cola
    """
    rho = lam / mu
    if rho >= 1.0:
        # Inestable: no hay estado estacionario.
        return TeoricoMM1(rho=rho, L=float('inf'), Lq=float('inf'),
                          W=float('inf'), Wq=float('inf'), estable=False)
    L  = rho / (1 - rho)
    Lq = rho**2 / (1 - rho)
    W  = 1 / (mu - lam)
    Wq = rho / (mu - lam)
    return TeoricoMM1(rho=rho, L=L, Lq=Lq, W=W, Wq=Wq, estable=True)


def prob_n_infinita(lam: float, mu: float, n: int) -> float:
    """
    P(N = n): probabilidad de encontrar exactamente n clientes en el sistema.
        P(n) = (1 - rho) * rho^n
    Es una distribucion geometrica: cuanto mas grande n, menos probable.
    """
    rho = lam / mu
    if rho >= 1.0:
        return float('nan')
    return (1 - rho) * rho**n


def mm1_finita(lam: float, mu: float, K: int) -> dict:
    """
    M/M/1/K: cola finita. El sistema admite a lo sumo (K + 1) clientes
    (K esperando en cola + 1 en servicio). Si llega un cliente con el sistema
    lleno, se RECHAZA (probabilidad de denegacion).

    A diferencia del caso infinito, aca SIEMPRE hay estado estacionario,
    incluso con rho >= 1, porque la cola no puede crecer infinito.

    Sea rho = lam/mu y m = K + 1 (capacidad total del sistema):
        P0 = (1 - rho) / (1 - rho^(m+1))       si rho != 1
        Pn = P0 * rho^n
        P(denegacion) = P_m  (probabilidad de sistema lleno = formula PASTA)

    Devuelve un dict con L, Lq, W, Wq, P_bloqueo y P0.
    """
    rho = lam / mu
    m = K + 1  # capacidad total: K en cola + 1 en servicio

    if abs(rho - 1.0) < 1e-12:
        # Caso especial rho = 1: las probabilidades son uniformes.
        P0 = 1.0 / (m + 1)
        probs = [P0] * (m + 1)
    else:
        P0 = (1 - rho) / (1 - rho**(m + 1))
        probs = [P0 * rho**n for n in range(m + 1)]

    P_bloqueo = probs[m]                  # sistema lleno -> se rechaza
    lam_efectiva = lam * (1 - P_bloqueo)  # arribos que SI entran

    L = sum(n * probs[n] for n in range(m + 1))
    # Lq = clientes esperando = L - (clientes en servicio)
    Lq = L - (1 - probs[0])
    W  = L / lam_efectiva if lam_efectiva > 0 else 0.0
    Wq = Lq / lam_efectiva if lam_efectiva > 0 else 0.0

    return {
        'rho': rho, 'K': K, 'L': L, 'Lq': Lq, 'W': W, 'Wq': Wq,
        'P_bloqueo': P_bloqueo, 'P0': P0, 'lam_efectiva': lam_efectiva,
    }


if __name__ == '__main__':
    # Demo rapida: imprime la teoria para varios niveles de carga.
    mu = 1.0
    print(f'{"rho":>6} {"L":>10} {"Lq":>10} {"W":>10} {"Wq":>10}')
    for rho in (0.25, 0.50, 0.75, 0.90):
        t = mm1_infinita(rho * mu, mu)
        print(f'{rho:>6.2f} {t.L:>10.4f} {t.Lq:>10.4f} {t.W:>10.4f} {t.Wq:>10.4f}')

    print('\nCola finita K=5, rho=0.9 (probabilidad de denegacion):')
    f = mm1_finita(0.9, 1.0, 5)
    print(f'  P(denegacion) = {f["P_bloqueo"]:.4f}   L = {f["L"]:.4f}   W = {f["W"]:.4f}')
