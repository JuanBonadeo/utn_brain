#!/usr/bin/env python3
"""Test de medias apareado entre escenarios a partir del CSV que escribe el experimento CorridasE0E3.

Uso, desde la raíz del repo:
    .venv/Scripts/python.exe -I materias/SIM/entregables/TPI/caser/modelo/analizar_corridas.py [corridas_horno.csv]
    ... analizar_corridas.py corridas_horno.csv --comparar corridas_horno_harness.csv
La segunda forma controla que AnyLogic haya producido exactamente las mismas filas que el motor mínimo del
verificador (mismas funciones y mismos generadores: deben coincidir campo por campo).

Para cada alternativa Ek contra E0 y cada medida, sobre las réplicas con la misma semilla (números aleatorios
comunes): D_j = X_Ek,j - X_E0,j (signo opuesto al Z de 05- §5.4: positivo = la alternativa aumenta la medida); IC = Z̄ ± t_{n-1, 1-α/2} · s_Z / √n (05- §5.4, Law cap. 10).
Primarias con Bonferroni (α = 0,05 / 3 cada una), secundarias al 95 % individual.
Rechaza el archivo si hay semillas sin par, escenarios con distinta cantidad de réplicas o filas repetidas.
"""
import csv
import math
import statistics
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).resolve().parent
_args = [a for a in sys.argv[1:] if a != "--comparar"]
ARCH = Path(_args[0]) if _args else AQUI / "corridas_horno.csv"
COMPARAR = Path(_args[1]) if "--comparar" in sys.argv and len(_args) > 1 else None

# Primarias de la Etapa 1 (sin demanda ni nivel de servicio, que entran en la Etapa 2):
# energía por kg y producto inmovilizado antes del horno (kg promedio en cola), más la espera media.
PRIMARIAS = [("kWhPorKg", "kWh por kg tratado"), ("colaMediaKg", "kg promedio en cola (WIP pre-horno)"),
             ("esperaMediaDias", "espera media en cola (días)")]
SECUNDARIAS = [("esperaP90Dias", "espera p90 (días)"), ("campanasPorMes", "campañas por mes"),
               ("nEncendidosPrioridad", "encendidos por prioridad"), ("uliPorCampanaMedia", "ULI por campaña"),
               ("fraccionCaliente", "fracción del tiempo a temperatura"), ("costoEnergiaPorKg", "$ de energía por kg")]


def betainc(a, b, x):
    """Beta incompleta regularizada (fracción continua de Lentz)."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    front = math.exp(math.log(x) * a + math.log1p(-x) * b - (math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)))
    if x > (a + 1) / (a + b + 2):
        return 1.0 - betainc(b, a, 1 - x)
    f, c, d = 1.0, 1.0, 0.0
    for i in range(400):
        m = i // 2
        if i == 0:
            num = 1.0
        elif i % 2 == 0:
            num = m * (b - m) * x / ((a + 2 * m - 1) * (a + 2 * m))
        else:
            num = -((a + m) * (a + b + m) * x) / ((a + 2 * m) * (a + 2 * m + 1))
        d = 1.0 + num * d
        d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
        c = 1.0 + num / (c if abs(c) > 1e-300 else 1e-300)
        f *= c * d
        if abs(1.0 - c * d) < 1e-15:
            break
    return front * (f - 1.0) / a


def t_cuantil(p_dos_colas, gl):
    """t tal que P(|T| > t) = p_dos_colas, por bisección."""
    lo, hi = 0.0, 1000.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if betainc(gl / 2, 0.5, gl / (gl + mid * mid)) > p_dos_colas:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


assert abs(t_cuantil(0.05, 29) - 2.0452296) < 1e-6 and abs(t_cuantil(0.05 / 3, 29) - 2.5409081) < 1e-6


def leer(path):
    filas = list(csv.DictReader(open(path, encoding="utf-8"), delimiter=";"))
    if not filas:
        sys.exit(f"{path} no tiene filas")
    por = {}
    for f in filas:
        clave = (f["escenario"], int(f["semilla"]))
        if clave in por:
            if por[clave] != f:
                sys.exit(f"{clave} aparece dos veces con valores distintos: renombrar el CSV viejo antes de relanzar")
            continue
        por[clave] = f
    esc = sorted({e for e, _ in por})
    if "E0" not in esc:
        sys.exit("falta el escenario base E0")
    semillas = {e: sorted(s for x, s in por if x == e) for e in esc}
    for e in esc:
        if semillas[e] != semillas["E0"]:
            sys.exit(f"{e} no tiene las mismas semillas que E0: {semillas[e]} vs {semillas['E0']}")
    return por, esc, semillas["E0"]


def intervalo(z, alfa):
    n = len(z)
    m = statistics.fmean(z)
    s = statistics.stdev(z) if n > 1 else float("nan")
    h = t_cuantil(alfa, n - 1) * s / math.sqrt(n)
    return m, s, m - h, m + h


def comparar(a, b):
    pa, ea, sa = leer(a)
    pb, eb, sb = leer(b)
    if (ea, sa) != (eb, sb):
        sys.exit(f"distintos escenarios o semillas: {ea} {sa[:3]}... vs {eb} {sb[:3]}...")
    dif = 0
    for clave in sorted(pa):
        for col, va in pa[clave].items():
            vb = pb[clave][col]
            try:
                igual = math.isclose(float(va), float(vb), rel_tol=1e-5, abs_tol=1e-9) or (math.isnan(float(va)) and math.isnan(float(vb)))
            except ValueError:
                igual = va == vb
            if not igual:
                dif += 1
                if dif <= 10:
                    print(f"DIFERENCIA {clave} {col}: {va} vs {vb}")
    if dif:
        sys.exit(f"{dif} campos distintos entre {a.name} y {b.name}")
    print(f"OK: {a.name} y {b.name} coinciden en las {len(pa)} corridas, campo por campo")


def main():
    if COMPARAR:
        comparar(ARCH, COMPARAR)
        return
    por, esc, sem = leer(ARCH)
    n = len(sem)
    print(f"{ARCH.name}: escenarios {', '.join(esc)}; {n} réplicas apareadas por semilla ({sem[0]}..{sem[-1]})")
    for e in esc[1:]:
        print(f"\n## {e} contra E0  (D = {e} − E0)")
        print(f"{'medida':38s} {'E0':>10s} {e:>10s} {'D medio':>10s} {'s(D)':>9s}   IC                        nivel   ¿≠0?")
        for grupo, alfa, etiqueta in ((PRIMARIAS, 0.05 / len(PRIMARIAS), "98,3 %"), (SECUNDARIAS, 0.05, "95 %")):
            for col, nombre in grupo:
                x0 = [float(por[("E0", s)][col]) for s in sem]
                xk = [float(por[(e, s)][col]) for s in sem]
                z = [b - a for a, b in zip(x0, xk)]
                m, sd, lo, hi = intervalo(z, alfa)
                sig = "sí" if (lo > 0 or hi < 0) else "no"
                print(f"{nombre:38s} {statistics.fmean(x0):10.4g} {statistics.fmean(xk):10.4g} {m:10.4g} {sd:9.3g}   "
                      f"[{lo:10.4g}; {hi:10.4g}]  {etiqueta:>6s}   {sig}")


if __name__ == "__main__":
    main()
