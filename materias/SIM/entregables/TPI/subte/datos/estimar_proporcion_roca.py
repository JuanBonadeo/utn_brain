#!/usr/bin/env python3
"""Intento de estimar la proporcion de pasajeros del vestibulo Principal (Constitucion, Linea C)
que llegan con los trenes del Roca, a partir de los molinetes SBASE y del horario del Roca.

Entradas (en esta misma carpeta):
  - sbase_dias_ventanas.csv: una fila por dia habil depurado mar-jun 2026, pax por ventana de 15 min
    07:00..09:15 (la genera scripts/sim/sbase-perfil.py --exportar-dias).
  - arribos_roca_constitucion_habiles.csv: columna segundos_desde_07 = llegada de cada tren a
    Pza. Constitucion, en segundos desde las 07:00 (la genera extraer_arribos_roca.py).

Modelo (efectos fijos de dia):
    pax[d,w] = a_d + b * T_w + e[d,w]
  T_w = trenes cuya llegada + rezago de caminata cae en la ventana w (variante "dispersa": cada tren
  reparte su gente uniforme entre llegada+r1 y llegada+r2, y T_w es la fraccion que cae en w).
  a_d = flujo de fondo no-Roca por ventana (constante dentro del dia), b = pax del Principal por tren.
  Proporcion Roca implicita = b * sum_w T_w / sum_w pax_medio_w.

Advertencia de identificacion: el horario del Roca es el mismo todos los dias habiles, asi que T_w solo
varia entre las 10 ventanas. Con efectos fijos de dia, b sale exclusivamente de la covariacion entre la
forma del perfil medio y T_w: 10 puntos, sin variacion exogena. Cualquier forma del pico que no venga
del Roca (colectivos, otras lineas, horarios de entrada) se confunde con b. Ademas el horario es el
vigente desde el 03/08/2026 y los molinetes son de mar-jun 2026.

IC 95 % por dos vias:
  (1) bootstrap de dias (B remuestreos): solo mide el ruido dia a dia; NO captura el error de
      especificacion, porque el diseño (T_w) es identico en cada dia remuestreado.
  (2) regresion de los 10 puntos del perfil medio (t con 10-1-k gl): el residuo incluye la parte de la
      forma del pico que T_w no explica; es la medida honesta de la incertidumbre de b.
Criterio de aceptacion (fijado antes de estimar): IC 95 % de la proporcion con ancho <= 0,20 y
contenido en [0, 1], en ambas vias, y estable frente al rezago de caminata.

Uso: python3 -I estimar_proporcion_roca.py [--boot 2000] [--semilla 2026]
Solo stdlib.
"""
import argparse, csv, random, statistics as st
from pathlib import Path

AQUI = Path(__file__).resolve().parent
VENTANA = 900  # s
NW = 10        # 07:00..09:15
# t de Student 0,975 por grados de libertad (para la via de los 10 puntos)
T975 = {5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262}


def leer():
    with open(AQUI / "sbase_dias_ventanas.csv", encoding="utf-8") as f:
        r = list(csv.DictReader(f, delimiter=";"))
    cols = [c for c in r[0] if c.startswith("v")]
    assert len(cols) == NW, cols
    pax = [[float(x[c]) for c in cols] for x in r]
    with open(AQUI / "arribos_roca_constitucion_habiles.csv", encoding="utf-8") as f:
        lleg = [int(x["segundos_desde_07"]) for x in csv.DictReader(f, delimiter=";")]
    return pax, lleg


def trenes_por_ventana(lleg, r1, r2=None):
    """r2=None: rezago puntual r1. Si no, reparto uniforme en [lleg+r1, lleg+r2]."""
    T = [0.0] * NW
    for t in lleg:
        if r2 is None:
            w = (t + r1) // VENTANA
            if 0 <= w < NW:
                T[w] += 1
        else:
            a, b = t + r1, t + r2
            for w in range(NW):
                lo, hi = w * VENTANA, (w + 1) * VENTANA
                T[w] += max(0.0, min(b, hi) - max(a, lo)) / (b - a)
    return T


def mco(X, y):
    """Minimos cuadrados por ecuaciones normales (k chico). Devuelve beta y (X'X)^-1."""
    k = len(X[0])
    A = [[sum(r[i] * r[j] for r in X) for j in range(k)] + [1.0 if i == j else 0.0 for j in range(k)]
         for i in range(k)]
    for i in range(k):  # Gauss-Jordan
        p = max(range(i, k), key=lambda q: abs(A[q][i]))
        A[i], A[p] = A[p], A[i]
        piv = A[i][i]
        A[i] = [v / piv for v in A[i]]
        for q in range(k):
            if q != i:
                f = A[q][i]
                A[q] = [vq - f * vi for vq, vi in zip(A[q], A[i])]
    inv = [row[k:] for row in A]
    Xy = [sum(r[i] * yy for r, yy in zip(X, y)) for i in range(k)]
    beta = [sum(inv[i][j] * Xy[j] for j in range(k)) for i in range(k)]
    return beta, inv


def ajustar(pax, T, tendencia=0):
    """Efectos fijos de dia == regresion del perfil medio centrado sobre regresores centrados.
    tendencia=1/2 agrega w y w^2 como control de la forma del pico. Devuelve dict."""
    D = len(pax)
    media = [st.mean(p[w] for p in pax) for w in range(NW)]
    regs = [T] + [[float(w ** g) for w in range(NW)] for g in range(1, tendencia + 1)]
    cen = lambda v: [x - st.mean(v) for x in v]
    X = [list(r) for r in zip(*[cen(v) for v in regs])]
    y = cen(media)
    beta, inv = mco(X, y)
    b = beta[0]
    prop = b * sum(T) / sum(media)
    # R^2 "within" (sobre los datos dia-ventana desviados de la media del dia) y R^2 del perfil medio
    yhat = [sum(bi * xi for bi, xi in zip(beta, row)) for row in X]
    sse_w = sum((p[w] - st.mean(p) - yhat[w]) ** 2 for p in pax for w in range(NW))
    sst_w = sum((p[w] - st.mean(p)) ** 2 for p in pax for w in range(NW))
    sse_m = sum((yy - yh) ** 2 for yy, yh in zip(y, yhat))
    sst_m = sum(yy ** 2 for yy in y)
    # R^2 total con efectos fijos (dummies de dia + regresores)
    gm = st.mean(x for p in pax for x in p)
    sst_tot = sum((x - gm) ** 2 for p in pax for x in p)
    k = len(beta)
    gl = NW - 1 - k
    se_b = (sse_m / gl * inv[0][0]) ** 0.5 if gl > 0 else float("nan")
    tq = T975.get(gl, 2.0)
    esc = sum(T) / sum(media)
    return dict(b=b, prop=prop, r2_within=1 - sse_w / sst_w, r2_perfil=1 - sse_m / sst_m,
                r2_total=1 - sse_w / sst_tot, ic_reg=((b - tq * se_b) * esc, (b + tq * se_b) * esc),
                se_b=se_b, gl=gl, D=D)


def bootstrap(pax, T, tendencia, B, rng):
    D = len(pax)
    props = sorted(ajustar([pax[rng.randrange(D)] for _ in range(D)], T, tendencia)["prop"] for _ in range(B))
    return props[int(0.025 * B)], props[int(0.975 * B) - 1]


def acepta(ic):
    lo, hi = ic
    return hi - lo <= 0.20 and lo >= 0 and hi <= 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--boot", type=int, default=2000)
    ap.add_argument("--semilla", type=int, default=2026)
    a = ap.parse_args()
    pax, lleg = leer()
    print(f"dias habiles depurados: {len(pax)} | trenes del Roca en el archivo: {len(lleg)}")
    print("perfil medio (pax/15 min):", [round(st.mean(p[w] for p in pax)) for w in range(NW)])

    variantes = [  # (etiqueta, r1, r2, tendencia)
        ("PRINCIPAL: llegada+10 s", 10, None, 0),
        ("llegada+60 s", 60, None, 0),
        ("llegada+120 s", 120, None, 0),
        ("llegada+180 s", 180, None, 0),
        ("llegada+300 s", 300, None, 0),
        ("disperso 60-360 s", 60, 360, 0),
        ("llegada+10 s + tendencia cuadratica", 10, None, 2),
    ]
    filas = []
    for i, (et, r1, r2, tend) in enumerate(variantes):
        T = trenes_por_ventana(lleg, r1, r2)
        r = ajustar(pax, T, tend)
        rng = random.Random(a.semilla + i)
        icb = bootstrap(pax, T, tend, a.boot, rng)
        filas.append((et, T, r, icb))

    for et, T, r, icb in filas:
        ok = acepta(icb) and acepta(r["ic_reg"])
        print(f"\n[{et}]")
        print("  T_w =", [round(t, 2) for t in T], f"(sum {sum(T):.1f})")
        print(f"  b = {r['b']:.1f} pax/tren | proporcion Roca = {r['prop']:.3f}")
        print(f"  IC95 bootstrap dias  = [{icb[0]:.3f}, {icb[1]:.3f}] (ancho {icb[1]-icb[0]:.3f})")
        print(f"  IC95 regresion 10 pt = [{r['ic_reg'][0]:.3f}, {r['ic_reg'][1]:.3f}]"
              f" (ancho {r['ic_reg'][1]-r['ic_reg'][0]:.3f}, gl={r['gl']})")
        print(f"  R2 within = {r['r2_within']:.3f} | R2 perfil medio = {r['r2_perfil']:.3f}"
              f" | R2 total con EF de dia = {r['r2_total']:.3f}")
        print(f"  criterio (ancho <= 0,20 y dentro de [0,1], ambas vias): {'CUMPLE' if ok else 'NO CUMPLE'}")

    props = [r["prop"] for _, _, r, _ in filas[:6]]
    print(f"\nsensibilidad al rezago (variantes sin tendencia): proporcion entre {min(props):.3f} y {max(props):.3f}")
    principal_ok = acepta(filas[0][3]) and acepta(filas[0][2]["ic_reg"])
    estable = max(props) - min(props) <= 0.10
    print("VEREDICTO:", "ACEPTADA" if principal_ok and estable else
          "NO DEFENDIBLE: el horario del Roca no identifica la proporcion (ver advertencia en el docstring)")


if __name__ == "__main__":
    main()
