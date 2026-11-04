#!/usr/bin/env python3
"""
Perfilado del dataset SBASE "Subte: Viajes Molinetes" para el TPI de Simulación.

Descarga (el portal rechaza user-agents no-navegador, de ahi el -A):

    curl -A "Mozilla/5.0" -O \
      https://cdn.buenosaires.gob.ar/datosabiertos/datasets/sbase/subte-viajes-molinetes/molinetes-2026.zip
    ditto -x -k molinetes-2026.zip ext/

Uso:
    python3 scripts/sim/sbase-perfil.py <dir-csv> [--linea LineaC] [--estacion Constitucion]
                                    [--desde 2026-03] [--hasta 2026-06]
                                    [--exportar-dias <csv>] [--exportar-molinetes <csv>]

--desde/--hasta acotan el periodo por mes (inclusive). El TPI usa marzo-junio 2026 (decision D3,
2026-09-24): enero y febrero son vacaciones y bajan la media.

--exportar-dias <csv>      una fila por dia habil depurado: fecha;dia_semana;v0700;...;v0915
                           (pax_TOTAL por ventana de 15 min, sumado sobre los molinetes del vestibulo).
--exportar-molinetes <csv> molinete;pax_franja_media_dia;participacion (franja 07:00-09:30,
                           promedio por dia habil depurado; participacion sobre el total del vestibulo).
Ambos CSV usan ';' como separador y '.' como decimal. Los molinetes con participacion < 0,5 %
quedan en el CSV pero se excluyen del CV y del cociente max/min que se imprimen.

Reproduccion del TPI (modelo SubteConstitucion, perfil de 10 ventanas):
    python3 -I scripts/sim/sbase-perfil.py <dir-csv> --desde 2026-03 --hasta 2026-06 \
      --exportar-dias materias/SIM/entregables/TPI/subte/datos/sbase_dias_ventanas.csv \
      --exportar-molinetes materias/SIM/entregables/TPI/subte/datos/sbase_molinetes.csv

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
    ap.add_argument("--exportar-dias", metavar="CSV", help="CSV fecha;dia_semana;v0700..v0915")
    ap.add_argument("--exportar-molinetes", metavar="CSV",
                    help="CSV molinete;pax_franja_media_dia;participacion")
    a = ap.parse_args()
    ym = lambda s: tuple(int(x) for x in s.split("-")) if s else None
    desde, hasta = ym(a.desde), ym(a.hasta)

    paths = sorted(glob.glob(os.path.join(a.dir, "*.csv")))
    if not paths:
        sys.exit(f"sin CSV en {a.dir}")

    dd = collections.defaultdict(lambda: collections.defaultdict(float))  # fecha -> hora -> pax
    act = collections.defaultdict(lambda: collections.defaultdict(set))   # fecha -> hora -> molinetes
    mol = collections.defaultdict(lambda: collections.defaultdict(float))  # fecha -> molinete -> pax franja

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
                mol[dt][p[4]] += pax
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

    # Carga por molinete: solo dias depurados (antes se sumaban tambien los feriados excluidos).
    nombres = sorted({m for d in buenos for m in mol[d]})
    media_mol = {m: sum(mol[d][m] for d in buenos) / len(buenos) for m in nombres}
    tot_mol = sum(media_mol.values())
    part = {m: v / tot_mol for m, v in media_mol.items()}
    print(f"\nMOLINETES en la franja pico (pax/dia habil, n={len(buenos)} dias)")
    for m, pd in sorted(media_mol.items(), key=lambda kv: -kv[1]):
        print(f"  {m.replace(a.linea + '_' + a.estacion + '_', ''):16s} {pd:>8.0f} {part[m]:>6.1%}  {'#' * int(pd / 40)}")
    reales = [m for m in nombres if part[m] >= 0.005]
    fuera = [m for m in nombres if part[m] < 0.005]
    cargas = [media_mol[m] for m in reales]
    if len(cargas) > 1:
        print(f"\n  molinetes con trafico real (participacion >= 0,5 %): {len(reales)}"
              f" | excluidos: {', '.join(fuera) or 'ninguno'}")
        print(f"  CV entre molinetes (de muestral / media) = {st.stdev(cargas) / st.mean(cargas):.3f}"
              f" | max/min = {max(cargas) / min(cargas):.2f}"
              f" ({max(reales, key=media_mol.get)} / {min(reales, key=media_mol.get)})")

    if a.exportar_dias:
        with open(a.exportar_dias, "w", encoding="utf-8", newline="") as f:
            f.write(";".join(["fecha", "dia_semana"] + ["v" + h.replace(":", "") for h in PICO]) + "\n")
            for d in buenos:
                f.write(";".join([d.isoformat(), DIAS[d.weekday()]] + [f"{dd[d][h]:.0f}" for h in PICO]) + "\n")
        print(f"\nexportado {a.exportar_dias} ({len(buenos)} dias)")
    if a.exportar_molinetes:
        with open(a.exportar_molinetes, "w", encoding="utf-8", newline="") as f:
            f.write("molinete;pax_franja_media_dia;participacion\n")
            for m, pd in sorted(media_mol.items(), key=lambda kv: -kv[1]):
                f.write(f"{m};{pd:.1f};{part[m]:.4f}\n")
        print(f"exportado {a.exportar_molinetes} ({len(nombres)} molinetes)")


if __name__ == "__main__":
    main()
