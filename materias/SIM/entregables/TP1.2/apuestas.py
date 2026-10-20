"""
TP 1.2 - Estudio economico-matematico de apuestas en la ruleta europea.

Uso:
    python apuestas.py -c 30 -n 1000 -s m -a f --capital 100
    python apuestas.py -c 30 -n 1000 -s w -a i

Parametros:
    -c / --corridas     : cantidad de corridas independientes
    -n / --tiradas      : cantidad de tiradas por corrida
    -s / --estrategia   : m (Martingala), d (D'Alembert), f (Fibonacci), w (Winograd)
    -a / --capital-tipo : i (infinito), f (finito)
    --capital           : capital inicial en modo finito (default: 100)
    --apuesta-min       : apuesta minima (default: 1)
    --semilla           : semilla opcional para reproducibilidad
    --salida            : carpeta de salida de graficas (default: graficas_apuestas)
    --mostrar           : muestra las graficas al finalizar
"""

from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path
from typing import List, Tuple

try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
except ModuleNotFoundError:
    print("Falta instalar Matplotlib. Ejecuta: pip install matplotlib", file=sys.stderr)
    raise SystemExit(1)

from simulacion_ruleta import guardar_figura, MIN_NUMERO, MAX_NUMERO


# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

NUMEROS_WINOGRAD = set(range(22, 37))          # 15 numeros cubiertos
COSTO_WINOGRAD   = len(NUMEROS_WINOGRAD)       # 15 unidades por tirada
GANANCIA_WINOGRAD = 35 - (COSTO_WINOGRAD - 1)  # 35 - 14 = +21 neto si gana

FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

NOMBRES = {
    'm': 'Martingala',
    'd': "D'Alembert",
    'f': 'Fibonacci',
    'w': 'Winograd',
}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parsear_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Simula estrategias de apuesta en una ruleta europea."
    )
    parser.add_argument('-c', '--corridas', type=int, required=True,
                        help='Cantidad de corridas independientes.')
    parser.add_argument('-n', '--tiradas', type=int, required=True,
                        help='Cantidad de tiradas por corrida.')
    parser.add_argument('-s', '--estrategia', choices=['m', 'd', 'f', 'w'], required=True,
                        help='Estrategia: m=Martingala, d=D\'Alembert, f=Fibonacci, w=Winograd.')
    parser.add_argument('-a', '--capital-tipo', choices=['i', 'f'], required=True,
                        help='Tipo de capital: i=infinito, f=finito.')
    parser.add_argument('--capital', type=float, default=100,
                        help='Capital inicial para modo finito (default: 100).')
    parser.add_argument('--apuesta-min', type=float, default=1,
                        help='Apuesta minima (default: 1).')
    parser.add_argument('--salida', default='graficas_apuestas',
                        help='Carpeta donde se guardan las graficas.')
    parser.add_argument('--semilla', type=int, default=None,
                        help='Semilla para reproducir la simulacion.')
    parser.add_argument('--mostrar', action='store_true',
                        help='Muestra las graficas al finalizar.')

    args = parser.parse_args()

    if args.corridas <= 0:
        parser.error('La cantidad de corridas debe ser mayor que cero.')
    if args.tiradas <= 0:
        parser.error('La cantidad de tiradas debe ser mayor que cero.')
    if args.capital <= 0:
        parser.error('El capital inicial debe ser mayor que cero.')
    if args.apuesta_min <= 0:
        parser.error('La apuesta minima debe ser mayor que cero.')

    return args


# ---------------------------------------------------------------------------
# Fibonacci
# ---------------------------------------------------------------------------

def _fib(idx: int) -> float:
    while idx >= len(FIBONACCI):
        FIBONACCI.append(FIBONACCI[-1] + FIBONACCI[-2])
    return float(FIBONACCI[idx])


# ---------------------------------------------------------------------------
# Simulacion
# ---------------------------------------------------------------------------

def simular_corrida(
    n_tiradas: int,
    estrategia: str,
    capital_inicial: float,
    apuesta_min: float,
    infinito: bool,
) -> Tuple[List[float], List[float], bool]:
    """
    Simula una corrida completa.

    Retorna:
        flujo_caja       : capital despues de cada tirada (incluye el inicial)
        ganancias        : ganancia/perdida en cada tirada
        quiebra          : True si el jugador se quedo sin capital
    """
    capital   = capital_inicial
    apuesta   = apuesta_min
    fib_idx   = 0
    flujo     = [capital]
    ganancias: List[float] = []
    quiebra   = False

    for _ in range(n_tiradas):
        resultado = random.randint(MIN_NUMERO, MAX_NUMERO)

        # ---- Winograd: apuesta 1 ficha a cada numero del 22 al 36 ----------
        if estrategia == 'w':
            if not infinito and capital < COSTO_WINOGRAD:
                quiebra = True
                break
            apuesta_real = COSTO_WINOGRAD if infinito else min(COSTO_WINOGRAD, capital)
            escala = apuesta_real / COSTO_WINOGRAD
            if resultado in NUMEROS_WINOGRAD:
                ganancia = GANANCIA_WINOGRAD * escala
            else:
                ganancia = -apuesta_real

        # ---- Estrategias de chance simple (apuesta a 1-18) ------------------
        else:
            if not infinito and capital < apuesta:
                quiebra = True
                break
            apuesta_real = apuesta if infinito else min(apuesta, capital)
            gano = 1 <= resultado <= 18
            ganancia = apuesta_real if gano else -apuesta_real

            if estrategia == 'm':
                apuesta = apuesta_min if gano else apuesta * 2

            elif estrategia == 'd':
                apuesta = max(apuesta_min, apuesta - 1) if gano else apuesta + 1

            elif estrategia == 'f':
                fib_idx = max(0, fib_idx - 2) if gano else fib_idx + 1
                apuesta = _fib(fib_idx)

        capital += ganancia
        flujo.append(capital)
        ganancias.append(ganancia)

    return flujo, ganancias, quiebra


def simular_todas_corridas(
    n_corridas: int,
    n_tiradas: int,
    estrategia: str,
    capital_inicial: float,
    apuesta_min: float,
    infinito: bool,
) -> Tuple[List[List[float]], List[List[float]], int]:
    flujos:   List[List[float]] = []
    ganancias_list: List[List[float]] = []
    quiebras = 0

    for _ in range(n_corridas):
        flujo, ganancias, quiebra = simular_corrida(
            n_tiradas, estrategia, capital_inicial, apuesta_min, infinito
        )
        flujos.append(flujo)
        ganancias_list.append(ganancias)
        if quiebra:
            quiebras += 1

    return flujos, ganancias_list, quiebras


# ---------------------------------------------------------------------------
# Graficas
# ---------------------------------------------------------------------------

def graficar_barras(
    ganancias: List[float],
    nombre_estrategia: str,
    nombre_archivo: str,
    salida: Path,
) -> None:
    x = list(range(1, len(ganancias) + 1))
    colores = ['#2ca02c' if g > 0 else '#d62728' for g in ganancias]

    plt.figure(figsize=(12, 4))
    plt.bar(x, ganancias, color=colores, width=1.0)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.title(f'Ganancia/perdida por tirada — {nombre_estrategia}')
    plt.xlabel('Numero de tirada')
    plt.ylabel('Ganancia (unidades)')
    ganancia_patch = mpatches.Patch(color='#2ca02c', label='Ganancia')
    perdida_patch  = mpatches.Patch(color='#d62728', label='Perdida')
    plt.legend(handles=[ganancia_patch, perdida_patch])
    plt.grid(True, axis='y', alpha=0.3)
    guardar_figura(nombre_archivo, salida)
    plt.close()


def graficar_flujo_caja(
    flujo: List[float],
    referencia: float,
    nombre_estrategia: str,
    nombre_archivo: str,
    salida: Path,
    infinito: bool,
) -> None:
    x = list(range(len(flujo)))
    etiqueta_ref = 'Punto de equilibrio' if infinito else f'Capital inicial: {referencia:.0f}'

    plt.figure(figsize=(10, 5))
    plt.plot(x, flujo, color='#1f77b4', linewidth=1.5, label='Capital')
    plt.axhline(referencia, color='#d62728', linestyle='--',
                linewidth=1.2, label=etiqueta_ref)
    plt.title(f'Flujo de caja — {nombre_estrategia}')
    plt.xlabel('Numero de tirada')
    plt.ylabel('Capital (unidades)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    guardar_figura(nombre_archivo, salida)
    plt.close()


def graficar_flujos_multiples(
    flujos: List[List[float]],
    referencia: float,
    nombre_estrategia: str,
    nombre_archivo: str,
    salida: Path,
    quiebras: int,
    infinito: bool,
) -> None:
    etiqueta_ref = 'Punto de equilibrio' if infinito else f'Capital inicial: {referencia:.0f}'
    titulo_quiebras = f' ({quiebras} quiebras)' if (quiebras and not infinito) else ''

    plt.figure(figsize=(10, 5))
    for indice, flujo in enumerate(flujos, start=1):
        plt.plot(range(len(flujo)), flujo, linewidth=0.8, alpha=0.5)

    plt.axhline(referencia, color='black', linestyle='--', linewidth=1.3,
                label=etiqueta_ref)
    plt.title(f'Flujo de caja — {nombre_estrategia} — {len(flujos)} corridas{titulo_quiebras}')
    plt.xlabel('Numero de tirada')
    plt.ylabel('Capital (unidades)')
    plt.legend(fontsize=8)
    plt.grid(True, alpha=0.3)
    guardar_figura(nombre_archivo, salida)
    plt.close()


# ---------------------------------------------------------------------------
# Resumen por consola
# ---------------------------------------------------------------------------

def imprimir_resumen(
    estrategia: str,
    infinito: bool,
    capital_inicial: float,
    flujos: List[List[float]],
    quiebras: int,
    salida: Path,
) -> None:
    nombre = NOMBRES[estrategia]
    capitales_finales = [f[-1] for f in flujos]
    media_final   = sum(capitales_finales) / len(capitales_finales)
    ganancia_media = media_final - capital_inicial

    print(f'\nEstrategia : {nombre}')
    print(f'Capital    : {"infinito" if infinito else f"finito (inicial: {capital_inicial:.0f})"}')
    print(f'Corridas   : {len(flujos)}')
    print(f'Capital final promedio   : {media_final:.2f}')
    print(f'Ganancia/perdida promedio: {ganancia_media:+.2f}')
    if not infinito:
        pct = 100 * quiebras / len(flujos)
        print(f'Quiebras   : {quiebras} de {len(flujos)} corridas ({pct:.1f}%)')
    print(f'Graficas guardadas en: {salida.resolve()}')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    args = parsear_argumentos()

    if args.semilla is not None:
        random.seed(args.semilla)

    infinito        = args.capital_tipo == 'i'
    estrategia      = args.estrategia
    nombre          = NOMBRES[estrategia]
    capital_inicial = args.capital if not infinito else 0.0
    apuesta_min     = args.apuesta_min
    salida          = Path(args.salida)
    salida.mkdir(parents=True, exist_ok=True)

    flujos, ganancias_list, quiebras = simular_todas_corridas(
        args.corridas, args.tiradas, estrategia,
        capital_inicial, apuesta_min, infinito,
    )

    prefijo = f'{estrategia}_{args.capital_tipo}'

    graficar_barras(
        ganancias_list[0], nombre,
        f'{prefijo}_01_barras_ganancias.png', salida,
    )
    graficar_flujo_caja(
        flujos[0], capital_inicial, nombre,
        f'{prefijo}_02_flujo_caja.png', salida, infinito,
    )
    graficar_flujos_multiples(
        flujos, capital_inicial, nombre,
        f'{prefijo}_03_flujos_multiples.png', salida, quiebras, infinito,
    )

    imprimir_resumen(estrategia, infinito, capital_inicial, flujos, quiebras, salida)

    if args.mostrar:
        plt.show()
    else:
        plt.close('all')


if __name__ == '__main__':
    main()
