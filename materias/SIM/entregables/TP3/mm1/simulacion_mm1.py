"""
Simulacion por eventos discretos de un sistema de colas M/M/1 (y M/M/1/K).

Analogia: un unico "worker" que atiende requests de a uno.
  - Llegadas  ~ Exponencial(lambda)  -> requests que entran al servicio.
  - Servicio  ~ Exponencial(mu)       -> tiempo que tarda el worker en uno.
  - 1 servidor.
  - Cola opcionalmente FINITA de tamano K (el "tamano del pool / queue").
    Si la cola esta llena, el request se RECHAZA (analogo a un HTTP 503).

Ejecutar:
    python simulacion_mm1.py --lambda 0.75 --mu 1.0 --tiempo 10000
    python simulacion_mm1.py --lambda 0.9 --mu 1.0 --cola 5
"""

from __future__ import annotations

import argparse
import heapq
from dataclasses import dataclass, field


@dataclass
class ResultadoMM1:
    """Medidas de rendimiento de UNA corrida de la simulacion."""
    L:  float   # promedio de clientes en el sistema (en cola + en servicio)
    Lq: float   # promedio de clientes en cola
    W:  float   # tiempo promedio en el sistema  (espera + servicio)
    Wq: float   # tiempo promedio en cola
    rho: float  # utilizacion del servidor (fraccion de tiempo ocupado)
    prob_n: dict[int, float]      # P(n clientes en el sistema)
    prob_denegacion: float        # fraccion de arribos rechazados (cola llena)
    arribos: int
    atendidos: int
    rechazados: int
    # Series temporales (para graficar la evolucion vs tiempo de simulacion):
    tiempos: list[float] = field(default_factory=list)
    serie_L:  list[float] = field(default_factory=list)
    serie_Lq: list[float] = field(default_factory=list)


def simular_mm1(
    lam: float,
    mu: float,
    tiempo_max: float,
    cola_max: int | None = None,
    semilla: int | None = None,
    n_muestras_serie: int = 500,
) -> ResultadoMM1:
    """
    Corre una simulacion M/M/1 hasta 'tiempo_max' unidades de tiempo simulado.

    cola_max = None  -> cola infinita (M/M/1 clasico).
    cola_max = K     -> cola finita de tamano K (M/M/1/K). Los arribos que
                        llegan con la cola llena se rechazan.
    """
    import random
    rng = random.Random(semilla)

    # --- Estado del sistema ---
    n = 0                    # cantidad de clientes en el sistema AHORA
    reloj = 0.0              # tiempo simulado actual
    servidor_ocupado = False

    # --- Acumuladores (ponderados por tiempo) ---
    # Integral de n(t) dt -> dividido por el tiempo total da el promedio L.
    area_n  = 0.0            # area bajo la curva n(t)   -> para L
    area_nq = 0.0           # area bajo la curva nq(t)  -> para Lq
    area_ocupado = 0.0      # tiempo total con el servidor ocupado -> para rho
    tiempo_en_estado: dict[int, float] = {}   # tiempo total con exactamente n clientes

    # --- Contadores ---
    arribos = atendidos = rechazados = 0
    suma_tiempo_sistema = 0.0   # suma de (salida - llegada) -> para W
    suma_tiempo_cola    = 0.0   # suma de espera en cola      -> para Wq

    # Cola de clientes esperando: guardamos el instante de llegada de cada uno.
    from collections import deque
    cola: deque[float] = deque()

    # --- Agenda de eventos futuros (min-heap por tiempo) ---
    # Cada evento es (instante, tipo, dato). tipo: 'arribo' | 'salida'.
    eventos: list[tuple[float, str]] = []

    def exp(tasa: float) -> float:
        """Muestra un tiempo de una Exponencial de la tasa dada."""
        return rng.expovariate(tasa)

    # Agendamos el primer arribo.
    heapq.heappush(eventos, (reloj + exp(lam), 'arribo'))

    proximo_muestreo = tiempo_max / n_muestras_serie
    tiempos: list[float] = []
    serie_L: list[float] = []
    serie_Lq: list[float] = []

    # ---------------- Bucle principal de eventos ----------------
    while eventos:
        instante, tipo = heapq.heappop(eventos)
        if instante > tiempo_max:
            break

        # 1) Avanzar el reloj y acumular las areas con el estado PREVIO.
        dt = instante - reloj
        area_n  += n * dt
        nq = n - (1 if servidor_ocupado else 0)   # en cola = en sistema - en servicio
        area_nq += nq * dt
        if servidor_ocupado:
            area_ocupado += dt
        tiempo_en_estado[n] = tiempo_en_estado.get(n, 0.0) + dt
        reloj = instante

        # Muestreo de las series temporales (para los graficos vs tiempo).
        while reloj >= proximo_muestreo and len(tiempos) < n_muestras_serie:
            tiempos.append(reloj)
            serie_L.append(area_n / reloj if reloj > 0 else 0.0)
            serie_Lq.append(area_nq / reloj if reloj > 0 else 0.0)
            proximo_muestreo += tiempo_max / n_muestras_serie

        # 2) Procesar el evento.
        if tipo == 'arribo':
            arribos += 1
            # Agendar el PROXIMO arribo (el flujo de llegadas no se detiene).
            heapq.heappush(eventos, (reloj + exp(lam), 'arribo'))

            if not servidor_ocupado:
                # Servidor libre -> lo atiende ya, sin pasar por la cola.
                servidor_ocupado = True
                n += 1
                suma_tiempo_cola += 0.0   # espero 0 en cola
                heapq.heappush(eventos, (reloj + exp(mu), 'salida'))
                # guardamos su llegada para calcular W al salir
                cola.append(reloj)        # reutilizamos 'cola' como registro de llegada
            else:
                # Servidor ocupado -> intenta entrar a la cola.
                capacidad_cola = nq  # clientes ya esperando
                if cola_max is not None and capacidad_cola >= cola_max:
                    # Cola llena -> RECHAZO (HTTP 503).
                    rechazados += 1
                else:
                    n += 1
                    cola.append(reloj)    # registra instante de llegada

        else:  # tipo == 'salida'
            atendidos += 1
            llegada = cola.popleft()      # FIFO: sale el que llego primero
            suma_tiempo_sistema += reloj - llegada
            n -= 1
            if n > 0:
                # Hay alguien esperando -> empieza su servicio.
                # El proximo en la cola ya tiene su llegada registrada al frente.
                heapq.heappush(eventos, (reloj + exp(mu), 'salida'))
                # su espera en cola = ahora - su llegada
                suma_tiempo_cola += reloj - cola[0]
            else:
                servidor_ocupado = False

    # ---------------- Calculo de las medidas finales ----------------
    T = reloj if reloj > 0 else 1.0
    L  = area_n  / T
    Lq = area_nq / T
    rho = area_ocupado / T
    W  = suma_tiempo_sistema / atendidos if atendidos else 0.0
    Wq = suma_tiempo_cola    / atendidos if atendidos else 0.0
    prob_n = {k: v / T for k, v in sorted(tiempo_en_estado.items())}
    prob_denegacion = rechazados / arribos if arribos else 0.0

    return ResultadoMM1(
        L=L, Lq=Lq, W=W, Wq=Wq, rho=rho,
        prob_n=prob_n, prob_denegacion=prob_denegacion,
        arribos=arribos, atendidos=atendidos, rechazados=rechazados,
        tiempos=tiempos, serie_L=serie_L, serie_Lq=serie_Lq,
    )


def main() -> None:
    p = argparse.ArgumentParser(description='Simulacion M/M/1 por eventos discretos.')
    p.add_argument('--lambda', dest='lam', type=float, default=0.75,
                   help='Tasa de arribos (requests/seg).')
    p.add_argument('--mu', type=float, default=1.0,
                   help='Tasa de servicio (requests/seg que despacha el worker).')
    p.add_argument('--tiempo', type=float, default=10000.0,
                   help='Tiempo de simulacion (unidades de tiempo).')
    p.add_argument('--cola', type=int, default=None,
                   help='Tamano maximo de cola K (vacio = cola infinita).')
    p.add_argument('--semilla', type=int, default=None,
                   help='Semilla del generador aleatorio (reproducibilidad).')
    args = p.parse_args()

    r = simular_mm1(args.lam, args.mu, args.tiempo, args.cola, args.semilla)

    print(f'--- Simulacion M/M/1{"/" + str(args.cola) if args.cola is not None else ""} ---')
    print(f'lambda={args.lam}  mu={args.mu}  rho(teorico)={args.lam/args.mu:.3f}')
    print(f'Tiempo simulado: {args.tiempo}   Arribos: {r.arribos}   Atendidos: {r.atendidos}   Rechazados: {r.rechazados}')
    print()
    print(f'L  (clientes en sistema): {r.L:.4f}')
    print(f'Lq (clientes en cola):    {r.Lq:.4f}')
    print(f'W  (tiempo en sistema):   {r.W:.4f}')
    print(f'Wq (tiempo en cola):      {r.Wq:.4f}')
    print(f'rho (utilizacion):        {r.rho:.4f}')
    print(f'P(denegacion):            {r.prob_denegacion:.4f}')


if __name__ == '__main__':
    main()
