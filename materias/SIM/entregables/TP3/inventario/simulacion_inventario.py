"""
Simulacion por eventos discretos de un sistema de inventario con politica (s, S)
de revision periodica (modelo clasico de Law & Kelton).

Funcionamiento de la politica (s, S):
  - Se monitorea la POSICION de inventario (stock fisico + pedidos en transito).
  - En cada instante de revision, si la posicion esta en <= s, se ordena lo
    necesario para llegar a S.
  - La demanda llega de forma aleatoria y consume stock (puede ir a negativo =
    "backorders", pedidos pendientes de clientes).
  - El objetivo del estudio es encontrar la politica (s, S) de minimo costo total.

Costos:
  - Orden       : costo fijo K por pedido + costo c por unidad pedida.
  - Mantenimiento (holding): h por unidad y por unidad de tiempo que hay stock > 0.
  - Faltante (shortage)    : p por unidad y por unidad de tiempo en backorder (stock < 0).

Ejecutar:
    python simulacion_inventario.py --s 20 --S 60 --tiempo 1200
"""

from __future__ import annotations

import argparse
import heapq
import random
from dataclasses import dataclass, field


# Distribucion del TAMANO de cada demanda (cuantas unidades pide cada cliente).
# Discreta: (valor, probabilidad). Por defecto 1..4 unidades.
DEMANDA_TAMANOS = [1, 2, 3, 4]
DEMANDA_PROBS   = [1/6, 1/3, 1/3, 1/6]   # media = 2.5 unidades por demanda


@dataclass
class ResultadoInventario:
    costo_orden:  float    # costo total de ordenar (acumulado)
    costo_holding: float   # costo total de mantenimiento
    costo_faltante: float  # costo total de faltante
    costo_total:  float
    # Promedios por unidad de tiempo (mas comparables entre corridas):
    costo_orden_prom:    float
    costo_holding_prom:  float
    costo_faltante_prom: float
    costo_total_prom:    float
    nivel_promedio: float
    n_ordenes: int
    # Series temporales para graficar la evolucion:
    tiempos: list[float] = field(default_factory=list)
    serie_costo_total: list[float] = field(default_factory=list)
    serie_nivel: list[float] = field(default_factory=list)


def simular_inventario(
    s: int,
    S: int,
    tiempo_max: float,
    tasa_demanda: float = 10.0,   # demandas por unidad de tiempo
    costo_fijo: float = 32.0,     # K: costo fijo por orden
    costo_unidad: float = 3.0,    # c: costo por unidad ordenada
    costo_holding: float = 1.0,   # h: por unidad y por tiempo
    costo_faltante: float = 5.0,  # p: por unidad y por tiempo en backorder
    lead_min: float = 0.5,        # lead time minimo (uniforme)
    lead_max: float = 1.0,        # lead time maximo (uniforme)
    intervalo_revision: float = 1.0,
    nivel_inicial: int = 60,
    semilla: int | None = None,
    n_muestras_serie: int = 500,
) -> ResultadoInventario:
    """Corre una simulacion del inventario (s, S) hasta tiempo_max."""
    rng = random.Random(semilla)

    # --- Estado ---
    nivel = nivel_inicial         # nivel de inventario (puede ser negativo)
    posicion = nivel_inicial      # posicion = nivel + lo que esta en camino
    reloj = 0.0

    # --- Acumuladores ---
    c_orden = 0.0
    area_holding = 0.0    # integral de max(nivel, 0) dt
    area_faltante = 0.0   # integral de max(-nivel, 0) dt
    area_nivel = 0.0      # integral de nivel dt (para nivel promedio)
    n_ordenes = 0

    # --- Agenda de eventos: (instante, tipo, cantidad) ---
    eventos: list[tuple[float, str, int]] = []

    def proxima_demanda() -> float:
        return rng.expovariate(tasa_demanda)

    def tamano_demanda() -> int:
        return rng.choices(DEMANDA_TAMANOS, weights=DEMANDA_PROBS)[0]

    def revisar_y_ordenar():
        """Politica (s, S): si la posicion <= s en una revision, ordena hasta S."""
        nonlocal posicion, c_orden, n_ordenes
        if posicion <= s:
            cantidad = S - posicion
            c_orden += costo_fijo + costo_unidad * cantidad
            n_ordenes += 1
            posicion += cantidad
            lead = rng.uniform(lead_min, lead_max)
            heapq.heappush(eventos, (reloj + lead, 'llegada', cantidad))

    # Primer evento de demanda y primera revision.
    heapq.heappush(eventos, (proxima_demanda(), 'demanda', 0))
    heapq.heappush(eventos, (0.0, 'revision', 0))

    proximo_muestreo = tiempo_max / n_muestras_serie
    tiempos: list[float] = []
    serie_costo_total: list[float] = []
    serie_nivel: list[float] = []

    # ---------------- Bucle principal ----------------
    while eventos:
        instante, tipo, cantidad = heapq.heappop(eventos)
        if instante > tiempo_max:
            break

        # 1) Avanzar el reloj acumulando holding/faltante con el estado PREVIO.
        dt = instante - reloj
        if nivel > 0:
            area_holding += nivel * dt
        else:
            area_faltante += (-nivel) * dt
        area_nivel += nivel * dt
        reloj = instante

        # Muestreo de series temporales.
        while reloj >= proximo_muestreo and len(tiempos) < n_muestras_serie:
            holding_acum = costo_holding * area_holding
            faltante_acum = costo_faltante * area_faltante
            tiempos.append(reloj)
            serie_costo_total.append(c_orden + holding_acum + faltante_acum)
            serie_nivel.append(nivel)
            proximo_muestreo += tiempo_max / n_muestras_serie

        # 2) Procesar el evento.
        if tipo == 'demanda':
            d = tamano_demanda()
            nivel -= d          # la demanda consume stock (puede ir a negativo)
            posicion -= d
            heapq.heappush(eventos, (reloj + proxima_demanda(), 'demanda', 0))
        elif tipo == 'revision':
            revisar_y_ordenar()
            heapq.heappush(eventos, (reloj + intervalo_revision, 'revision', 0))
        else:  # 'llegada' de un pedido
            nivel += cantidad   # llega la mercaderia pedida

    # ---------------- Costos finales ----------------
    T = reloj if reloj > 0 else 1.0
    c_holding = costo_holding * area_holding
    c_faltante = costo_faltante * area_faltante
    c_total = c_orden + c_holding + c_faltante

    return ResultadoInventario(
        costo_orden=c_orden,
        costo_holding=c_holding,
        costo_faltante=c_faltante,
        costo_total=c_total,
        costo_orden_prom=c_orden / T,
        costo_holding_prom=c_holding / T,
        costo_faltante_prom=c_faltante / T,
        costo_total_prom=c_total / T,
        nivel_promedio=area_nivel / T,
        n_ordenes=n_ordenes,
        tiempos=tiempos,
        serie_costo_total=serie_costo_total,
        serie_nivel=serie_nivel,
    )


def main() -> None:
    p = argparse.ArgumentParser(description='Simulacion de inventario (s, S).')
    p.add_argument('--s', type=int, default=20, help='Punto de reorden s.')
    p.add_argument('--S', dest='S', type=int, default=60, help='Nivel objetivo S.')
    p.add_argument('--tiempo', type=float, default=1200.0, help='Tiempo de simulacion.')
    p.add_argument('--demanda', type=float, default=10.0, help='Tasa de demanda.')
    p.add_argument('--revision', type=float, default=1.0,
                   help='Intervalo entre revisiones de inventario.')
    p.add_argument('--semilla', type=int, default=None)
    args = p.parse_args()

    if args.s >= args.S:
        p.error('s debe ser menor que S')

    r = simular_inventario(args.s, args.S, args.tiempo,
                           tasa_demanda=args.demanda,
                           intervalo_revision=args.revision,
                           semilla=args.semilla)

    print(f'--- Inventario (s={args.s}, S={args.S}) ---')
    print(f'Tiempo simulado: {args.tiempo}   Ordenes emitidas: {r.n_ordenes}')
    print(f'Nivel promedio de inventario: {r.nivel_promedio:.2f}')
    print()
    print(f'{"":22}{"Total":>12}{"Por tiempo":>14}')
    print(f'{"Costo de orden":22}{r.costo_orden:>12.1f}{r.costo_orden_prom:>14.3f}')
    print(f'{"Costo de holding":22}{r.costo_holding:>12.1f}{r.costo_holding_prom:>14.3f}')
    print(f'{"Costo de faltante":22}{r.costo_faltante:>12.1f}{r.costo_faltante_prom:>14.3f}')
    print(f'{"-"*48}')
    print(f'{"COSTO TOTAL":22}{r.costo_total:>12.1f}{r.costo_total_prom:>14.3f}')


if __name__ == '__main__':
    main()
