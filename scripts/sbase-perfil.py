#!/usr/bin/env python3
"""
Perfilado del dataset SBASE "Subte: Viajes Molinetes" para el TPI de Simulación.

Descarga (el portal rechaza user-agents no-navegador, de ahi el -A):

    curl -A "Mozilla/5.0" -O \
      https://cdn.buenosaires.gob.ar/datosabiertos/datasets/sbase/subte-viajes-molinetes/molinetes-2026.zip
    ditto -x -k molinetes-2026.zip ext/

Uso:
    python3 scripts/sbase-perfil.py <dir-csv> [--linea LineaC] [--estacion Constitucion]
                                    [--desde 2026-03] [--hasta 2026-06]

--desde/--hasta acotan el periodo por mes (inclusive). El TPI usa marzo-junio 2026 (decision D3,
2026-09-24): enero y febrero son vacaciones y bajan la media.

Ojo con dos cosas del dataset, las dos ya contempladas acá:
  - Cada fila viene envuelta en comillas y separada por ';'.
  - El campo de hora cambia de formato segun el mes: 03/2026 y 04/2026 usan 'HH:MM'
    y el resto 'HH:MM:SS'. Agregar sin normalizar parte cada hora en dos.
"""
import argparse, collections, datetime, glob, os, statistics as st, sys

PICO = [f"{h:02d}:{m:02d}" for h in (7, 8, 9) for m in (0, 15, 30, 45)][:10]  # 07:00..09:15
DIAS = ["lun", "mar", "mie", "jue", "vie", "sab", "dom"]


def hm(s):
    """Normaliza 'HH:MM:SS' y 'H:MM' a 'HH:MM'."""
    p = s.split(":")
    return f"{int(p[0]):02d}:{p[1]}"


def filas(path):
    with open(path, encoding="utf-8-sig") as f:
        for i, raw in enumerate(f):
            raw = raw.strip()
            if not raw:
                continue
            if raw.startswith('"') and raw.endswith('"'):
                raw = raw[1:-1]
            p = raw.split(";")
            if i == 0 or len(p) < 10 or p[0] == "FECHA":
                continue
            yield p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    ap.add_argument("--linea", default="LineaC")
    ap.add_argument("--estacion", default="Constitucion")
    ap.add_argument("--vestibulo", default="Principal", choices=["Principal", "Plaza", "ambos"])
    ap.add_argument("--desde", help="primer mes incluido, AAAA-MM")
    ap.add_argument("--hasta", help="ultimo mes incluido, AAAA-MM")
    a = ap.parse_args()
    ym = lambda s: tuple(int(x) for x in s.split("-")) if s else None
    desde, hasta = ym(a.desde), ym(a.hasta)

    paths = sorted(glob.glob(os.path.join(a.dir, "*.csv")))
    if not paths:
        sys.exit(f"sin CSV en {a.dir}")

    dd = collections.defaultdict(lambda: collections.defaultdict(float))  # fecha -> hora -> pax
    act = collections.defaultdict(lambda: collections.defaultdict(set))   # fecha -> hora -> molinetes
    mol = collections.defaultdict(float)

    for path in paths:
        for p in filas(path):
            if p[3] != a.linea or p[5] != a.estacion:
                continue
            es_plaza = "_Plaza_" in p[4]
            if a.vestibulo == "Principal" and es_plaza:
                continue
            if a.vestibulo == "Plaza" and not es_plaza:
                continue
            try:
                pax = int(p[9])
            except ValueError:
                continue
            d, m, y = (int(x) for x in p[0].split("/"))
            dt = datetime.date(y, m, d)
            if dt.weekday() >= 5:
                continue
            if (desde and (y, m) < desde) or (hasta and (y, m) > hasta):
                continue
            h = hm(p[1])
            dd[dt][h] += pax
            if h in PICO:
                mol[p[4]] += pax
                if pax > 0:
                    act[dt][h].add(p[4])

    # Depuracion: los dias habiles con menos del 50% de la mediana diaria son feriados.
    tot = {d: sum(v.values()) for d, v in dd.items()}
    med = st.median(tot.values())
    malos = sorted(d for d, v in tot.items() if v < 0.5 * med)
    buenos = sorted(set(dd) - set(malos))

    print(f"{a.linea} / {a.estacion} / vestibulo {a.vestibulo} / periodo {a.desde or 'inicio'} a {a.hasta or 'fin'}")
    print(f"primer dia {min(dd)} | ultimo dia {max(dd)}")
    print(f"dias habiles con dato: {len(dd)} | excluidos por feriado: {len(malos)} | utiles: {len(buenos)}")
    for d in malos:
        print(f"   excluido {d} ({DIAS[d.weekday()]}) pax={tot[d]:,.0f}")

    print(f"\nFRANJA 07:00-09:30 (n={len(buenos)} dias)")
    print(f"  {'ventana':9s} {'media':>7s} {'de':>6s} {'CV':>5s} {'min':>6s} {'max':>6s} {'molin':>6s} {'pax/mol/min':>11s}")
    total = 0.0
    for h in PICO:
        v = [dd[d][h] for d in buenos]
        na = st.mean(len(act[d][h]) for d in buenos)
        total += st.mean(v)
        print(f"  {h:9s} {st.mean(v):>7.0f} {st.stdev(v):>6.0f} "
              f"{st.stdev(v)/st.mean(v):>5.2f} {min(v):>6.0f} {max(v):>6.0f} "
              f"{na:>6.1f} {st.mean(v)/na/15:>11.2f}")
    print(f"\n  TOTAL franja = {total:,.0f} pax/dia habil")

    print(f"\nMOLINETES en la franja pico (pax/dia habil)")
    for m, v in sorted(mol.items(), key=lambda kv: -kv[1]):
        pd = v / len(buenos)
        print(f"  {m.replace(a.linea + '_' + a.estacion + '_', ''):16s} {pd:>8.0f}  {'#' * int(pd / 40)}")


if __name__ == "__main__":
    main()
