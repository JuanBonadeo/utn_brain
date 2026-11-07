#!/usr/bin/env python3
"""Corridas piloto del TPI Caser: calentamiento (Welch) y número de réplicas. Resumen en 09-pilotos.md.

Uso, desde la raíz del repo (Windows; tarda ~25 s):
    .venv/Scripts/python.exe -I materias/SIM/entregables/TPI/caser/modelo/pilotos.py [--reps-welch 10]

Reusa el motor mínimo de verificar_modelo.py (las MISMAS funciones del .alp, que coincidieron campo por campo
con AnyLogic) y le agrega una clase CaserPilotos que lo maneja:

1. Welch: E0..E3, réplicas 1..R (R = 10 por defecto, y 100 como control), SIN calentamiento (calentamientoModeloDias = 0),
   horizonte 1.095 días. Un evento extra cada 720 h (30 días) llama a acumular() y anota los acumuladores; la
   diferencia entre dos fotos da el valor del mes (kg promedio en cola, horas a temperatura, costo relevante,
   espera media de las ULI despachadas). Antes de usarlas se controla que:
   a. las fotos coinciden con el "truco del horizonte" (correr con horizonteDias = 30 k desde la misma semilla
      y leer los acumuladores al final), y
   b. agregar las fotos no cambia la corrida (misma fila de resultado que sin fotos).
   Media móvil de Welch con w = 3 y w = 6 y dos cortes: el de la media móvil (elegir_corte) y el de una prueba t
   sobre la serie cruda (corte_por_prueba), que no arrastra la ventana. Se elige el segundo, con 100 réplicas.
2. Contraste del corte: E0, 30 réplicas, un año medido con calentamiento 0, 90, 180 y 365 días.
3. Réplicas: con corridas_horno_harness.csv (lo escribe verificar_modelo.py), para D = Ei − E0 de las medidas
   primarias, semiamplitud h (Bonferroni, α = 0,05/3), h/|D̄| y n* = n·(h / h_objetivo)² para ±10 %.
Salidas: materias/SIM/figs/tpi-caser-welch.png y la tabla en consola.
"""
import csv
import math
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))  # con -I el directorio del script no está en sys.path
import verificar_modelo as vm  # noqa: E402
from analizar_corridas import DERIVADAS, PRIMARIAS, SECUNDARIAS, t_cuantil  # noqa: E402

REPS_WELCH = int(sys.argv[sys.argv.index("--reps-welch") + 1]) if "--reps-welch" in sys.argv else 10
REPS_WELCH_LARGO = 100   # Law: si con n réplicas la curva es muy ruidosa, se repite con más
HORIZONTE_DIAS, MESES, H_MES = 1095, 36, 720.0
CSV_H = AQUI / "corridas_horno_harness.csv"
FIG = AQUI.parents[3] / "figs" / "tpi-caser-welch.png"   # materias/SIM/figs
CAMPOS = ["areaCola", "areaColaKg", "horasCaliente", "nEnc", "nEncP", "nEsperas", "sumEsperas", "nTratadas",
          "kgTratados", "nLlegadas", "costoTotal"]

PILOTOS = r"""import java.util.*;
public class CaserPilotos {
static CaserLogicCheck nuevo(int esc, long sem, double cal, double hor) {
  CaserLogicCheck m = new CaserLogicCheck(); int index = esc * 30;
  %ESCENARIO%
  m.semilla = sem; m.calentamientoModeloDias = cal; m.horizonteDias = hor; m.startup(); return m; }
static String foto(CaserLogicCheck m) {
  double s = 0; for (double e : m.esperas) s += e;
  return String.format(Locale.US, "%.10g;%.10g;%.10g;%d;%d;%d;%.10g;%d;%.10g;%d;%.10g", m.areaCola, m.areaColaKg,
    m.horasCaliente, m.nEncendidos, m.nEncendidosPrioridad, m.esperas.size(), s, m.nTratadas, m.kgTratados, m.nLlegadas, m.costoTotal()); }
public static void main(String[] a) {
  String modo = a[0]; int esc = Integer.parseInt(a[1]); int reps = Integer.parseInt(a[2]);
  if (modo.equals("serie")) {          // fotos cada 720 h, sin calentamiento
    int meses = Integer.parseInt(a[3]); double hor = Double.parseDouble(a[4]);
    for (int s = 1; s <= reps; s++) {
      final CaserLogicCheck m = nuevo(esc, s, 0, hor); final int sem = s;
      for (int k = 1; k <= meses; k++) { final int kk = k;
        m.agendar(k * 720.0, () -> { m.acumular(); System.out.println("FOTO;" + sem + ";" + kk + ";" + foto(m)); }); }
      m.correr(1e12); if (!m.finalizado) throw new AssertionError("no termino");
      System.out.println("FIN;" + s + ";" + m.filaResultado());
    }
  } else if (modo.equals("truco")) {   // horizonte = 30 k dias, acumuladores al final
    for (int s = 1; s <= reps; s++) for (int i = 3; i < a.length; i++) { int k = Integer.parseInt(a[i]);
      CaserLogicCheck m = nuevo(esc, s, 0, 30.0 * k); m.correr(1e12);
      System.out.println("TRUCO;" + s + ";" + k + ";" + foto(m)); }
  } else if (modo.equals("fila")) {    // corrida comun con calentamiento y horizonte dados
    double cal = Double.parseDouble(a[3]), hor = Double.parseDouble(a[4]);
    for (int s = 1; s <= reps; s++) { CaserLogicCheck m = nuevo(esc, s, cal, hor); m.correr(1e12);
      System.out.println("FILA;" + s + ";" + m.filaResultado()); }
  }
}
}"""


def preparar():
    vm.jdk()
    x = vm.extraer(vm.AQUI / "CaserHorno.alp")
    tmp = tempfile.TemporaryDirectory(prefix="caser-pilotos-")
    d = Path(tmp.name)
    vm.compilar_harness(x, d)
    # El escenario se arma con las mismas expresiones del experimento CorridasE0E3 (index / 30 = escenario).
    esc = " ".join(f"m.{k} = {v};" for k, v in x.cor.items() if v and k not in ("archivoSalida", "semilla"))
    (d / "CaserPilotos.java").write_text(PILOTOS.replace("%ESCENARIO%", esc), encoding="utf-8")
    r = subprocess.run([str(vm.JAVAC), "-encoding", "UTF-8", "-nowarn", "-cp", str(d), "-d", str(d), str(d / "CaserPilotos.java")],
                       capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr)
        sys.exit("FALLA: CaserPilotos no compila")
    return tmp, d


def java(d, *args):
    r = subprocess.run([str(vm.JAVA), "-Xss8m", "-cp", str(d), "CaserPilotos", *map(str, args)], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr)
        sys.exit("FALLA: CaserPilotos " + " ".join(map(str, args)))
    return [ln.split(";") for ln in r.stdout.splitlines()]


def fotos(lineas, tag):
    return {(int(f[1]), int(f[2])): dict(zip(CAMPOS, map(float, f[3:]))) for f in lineas if f[0] == tag}


def mensual(fot, reps):
    """Valor de cada mes por réplica: diferencias entre fotos consecutivas."""
    series = {k: [[None] * MESES for _ in range(reps)] for k in ("kgCola", "horasCal", "costo", "espera")}
    for s in range(1, reps + 1):
        prev = dict.fromkeys(CAMPOS, 0.0)
        for k in range(1, MESES + 1):
            f = fot[(s, k)]
            dlt = {c: f[c] - prev[c] for c in CAMPOS}
            series["kgCola"][s - 1][k - 1] = dlt["areaColaKg"] / H_MES
            series["horasCal"][s - 1][k - 1] = dlt["horasCaliente"]
            series["costo"][s - 1][k - 1] = dlt["costoTotal"] / 1e6
            series["espera"][s - 1][k - 1] = dlt["sumEsperas"] / 24 / dlt["nEsperas"] if dlt["nEsperas"] else float("nan")
            prev = f
    return series


def welch(y, w):
    """Media móvil de Law (cap. 9): ventanas centradas de 2w+1; las primeras w, simétricas más cortas."""
    m = len(y)
    return [statistics.fmean(y[0:2 * i + 1]) if i < w else statistics.fmean(y[i - w:i + w + 1]) for i in range(m - w)]


def elegir_corte(yw, ref, banda):
    """Primer mes l tal que la media móvil queda dentro de ref ± banda desde l+1 en adelante."""
    l = len(yw)
    while l > 0 and abs(yw[l - 1] - ref) <= banda:
        l -= 1
    return l


def banda_de(yw):
    """Ruido propio de la media móvil en la zona estable (meses 13 a m−w): ±2 desvíos, con un piso de ±2 % de la
    referencia. Así el corte no lo decide el ruido de un mes suelto (con 10 réplicas el CV mensual es ~13 %)."""
    ref = statistics.fmean(yw[12:])
    return ref, max(2 * statistics.stdev(yw[12:]), 0.02 * abs(ref))


def corte_por_prueba(ser, alfa=0.05 / 12):
    """Último mes de los primeros 12 cuya media entre réplicas difiere de la referencia (media de los meses 13-36
    de cada réplica): prueba t apareada por réplica, Bonferroni sobre los 12 meses. Es el transitorio sin el
    corrimiento que mete la ventana de la media móvil (Ȳ_i(w) incluye los meses i−w..i+w)."""
    reps = len(ser)
    refs = [statistics.fmean(r[12:]) for r in ser]
    t = t_cuantil(alfa, reps - 1)
    l = 0
    for j in range(12):
        z = [r[j] - ref for r, ref in zip(ser, refs)]
        if abs(statistics.fmean(z)) > t * statistics.stdev(z) / math.sqrt(reps):
            l = j + 1
    return l


CLAVES = ("kgCola", "horasCal", "costo")
NOMBRES = {"kgCola": "kg en cola", "horasCal": "h a temperatura", "costo": "costo (M$)", "espera": "espera (d)"}


def grafico(curvas, l_elegido, l_welch):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "axes.spines.top": False, "axes.spines.right": False,
                         "axes.edgecolor": "#52514e", "axes.labelcolor": "#0b0b0b", "xtick.color": "#52514e", "ytick.color": "#52514e"})
    paneles = [("kgCola", "kg promedio en cola"), ("horasCal", "horas a temperatura en el mes"), ("costo", "costo relevante del mes (M$)")]
    reps = list(curvas)
    fig, axs = plt.subplots(len(paneles), len(reps), figsize=(7.4, 8.6), sharex=True, sharey="row")
    meses = list(range(1, MESES + 1))
    for col, R in enumerate(reps):
        prom, ws = curvas[R]
        for fila, (clave, titulo) in enumerate(paneles):
            ax = axs[fila][col]
            ax.plot(meses, prom[clave], color="#9a9994", lw=1, marker="o", ms=2.5, label="media entre réplicas (cruda)")
            for (w, color) in ((3, "#2a78d6"), (6, "#eb6834")):
                yw = ws[clave][w]
                ax.plot(meses[:len(yw)], yw, color=color, lw=2, label=f"media móvil w = {w}")
            ax.axvline(3, color="#0b0b0b", lw=1, ls="--", label="90 días (calentamiento del modelo)")
            ax.axvline(l_welch, color="#6250d6", lw=1.2, ls=":", label=f"se aplana la media móvil w = 3 ({REPS_WELCH_LARGO} rép.): mes {l_welch}")
            ax.axvline(l_elegido, color="#1baf7a", lw=1.8, label=f"corte elegido l = {l_elegido} mes (transitorio)")
            ax.set_title(f"{titulo} — {R} réplicas", loc="left", fontsize=9, color="#0b0b0b")
            ax.grid(axis="y", color="#e4e3df", lw=0.6)
            ax.set_xticks(range(0, MESES + 1, 6))
        axs[-1][col].set_xlabel("mes (30 días) desde t = 0")
    h, lab = axs[0][0].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", ncol=2, fontsize=8, frameon=False)
    fig.suptitle("Welch — E0 sin calentamiento (arranca con cola vacía y horno apagado), 36 meses", x=0.02, ha="left", fontsize=10.5)
    fig.tight_layout(rect=(0, 0.075, 1, 1))
    FIG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG, dpi=200)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    tmp, d = preparar()

    # ---------------- 1. Welch
    print(f"## 1. Welch: sin calentamiento, {MESES} meses de 30 días (horizonte {HORIZONTE_DIAS} d)")
    res = {}
    for R in (REPS_WELCH, REPS_WELCH_LARGO):
        for esc in range(4):
            lin = java(d, "serie", esc, R, MESES, HORIZONTE_DIAS)
            res[(R, esc)] = (fotos(lin, "FOTO"), {int(f[1]): ";".join(f[2:]) for f in lin if f[0] == "FIN"})

    # a. fotos = truco del horizonte (E0, réplicas 1..3, varios meses)
    ks = [1, 2, 3, 6, 12, 24, 36]
    tru = fotos(java(d, "truco", 0, 3, *ks), "TRUCO")
    f0 = res[(REPS_WELCH, 0)][0]
    peor = max(abs(tru[sk][c] - f0[sk][c]) / max(1.0, abs(f0[sk][c])) for sk in tru for c in CAMPOS)
    assert peor < 1e-9, f"las fotos no coinciden con el truco del horizonte: {peor}"
    print(f"   OK fotos = truco del horizonte (horizonteDias = 30 k) en {len(tru)} casos: diferencia relativa máx. {peor:.1e}")
    # b. las fotos no cambian la corrida
    for esc in range(4):
        sin = {int(f[1]): ";".join(f[2:]) for f in java(d, "fila", esc, REPS_WELCH, 0, HORIZONTE_DIAS)}
        assert sin == res[(REPS_WELCH, esc)][1], f"E{esc}: las fotos cambian el resultado"
    print("   OK las fotos no cambian ninguna corrida (fila de resultado idéntica con y sin fotos, E0-E3)")

    cortes, curvas, pruebas = {}, {}, {}
    for (R, esc), (fot, _) in res.items():
        ser = mensual(fot, R)
        prom = {c: [statistics.fmean(v for v in col if not math.isnan(v)) for col in zip(*ser[c])] for c in ser}
        ws = {c: {w: welch(prom[c], w) for w in (3, 6)} for c in prom}
        if esc == 0:
            curvas[R] = (prom, ws)
            refs = {c: statistics.fmean(prom[c][12:]) for c in prom}
            print(f"\n   E0, {R} réplicas: media de cada mes y % de la media de los meses 13-36")
            print("   mes | " + " | ".join(f"{NOMBRES[c]:>22s}" for c in prom))
            for i in range(12):
                print(f"   {i + 1:3d} | " + " | ".join(f"{prom[c][i]:14.2f} ({100 * prom[c][i] / refs[c]:4.0f} %)" for c in prom))
            print("   13-36 | " + " | ".join(f"{refs[c]:14.2f} (100 %)" for c in prom))
        for c in CLAVES:
            pruebas[(R, esc, c)] = corte_por_prueba(ser[c])
            for w in (3, 6):
                ref, banda = banda_de(ws[c][w])
                cortes[(R, esc, c, w)] = elegir_corte(ws[c][w], ref, banda)
    print("\n   Corte l (meses): media móvil dentro de ref ± máx(2 desvíos de la media móvil en meses 13-36; 2 %)")
    print("   réplicas esc | " + " | ".join(f"{NOMBRES[c] + ' w=' + str(w):>18s}" for c in CLAVES for w in (3, 6)))
    for (R, esc) in res:
        print(f"   {R:8d} E{esc}  | " + " | ".join(f"{cortes[(R, esc, c, w)]:18d}" for c in CLAVES for w in (3, 6)))
    print("\n   Último mes que difiere de la referencia (prueba t por réplica, Bonferroni α = 0,05/12 sobre los meses 1-12)")
    print("   réplicas esc | " + " | ".join(f"{NOMBRES[c]:>16s}" for c in CLAVES))
    for (R, esc) in res:
        print(f"   {R:8d} E{esc}  | " + " | ".join(f"{pruebas[(R, esc, c)]:16d}" for c in CLAVES))
    l_welch = max(cortes[(REPS_WELCH_LARGO, e, c, 3)] for e in range(4) for c in CLAVES)
    l_elegido = max(pruebas[(REPS_WELCH_LARGO, e, c)] for e in range(4) for c in CLAVES)
    grafico({R: curvas[R] for R in (REPS_WELCH, REPS_WELCH_LARGO)}, l_elegido, l_welch)
    print(f"\n   Welch w = 3 con {REPS_WELCH_LARGO} réplicas (máx. E0-E3): la media móvil se aplana desde l = {l_welch} (cota conservadora: la ventana arrastra el mes 1)")
    print(f"   Transitorio por prueba sobre la serie cruda ({REPS_WELCH_LARGO} réplicas, máx. E0-E3): l = {l_elegido} mes(es) -> corte elegido")
    print(f"   Gráfico: {FIG}")

    # ---------------- 2. contraste: un año medido con calentamiento 0, 90 y 180 días
    print("\n## 2. E0, 30 réplicas, 365 días medidos con distintos calentamientos")
    cols = {"costoTotal": 37, "colaMediaKg": 25, "esperaMediaDias": 21, "fraccionCaliente": 29}
    base = {}
    for cal in (0, 90, 180, 365):
        filas = [f for f in java(d, "fila", 0, 30, cal, 365)]
        base[cal] = {c: [float(f[2 + i]) for f in filas] for c, i in cols.items()}
    for c in cols:
        txt = []
        for cal in (0, 90, 180, 365):
            z = [a - b for a, b in zip(base[cal][c], base[365][c])]
            h = t_cuantil(0.05, 29) * statistics.stdev(z) / math.sqrt(30) if cal != 365 else 0
            txt.append(f"cal {cal:3d}: {statistics.fmean(base[cal][c]):12.4g}" + (f" (D vs 365 = {statistics.fmean(z):+.4g} ± {h:.3g})" if cal != 365 else ""))
        print(f"   {c:17s} " + " | ".join(txt))

    # ---------------- 3. número de réplicas
    print(f"\n## 3. Réplicas: {CSV_H.name}, D = Ei − E0, objetivo h ≤ 0,10·|D̄|")
    filas = list(csv.DictReader(open(CSV_H, encoding="utf-8"), delimiter=";"))
    por = {(f["escenario"], int(f["semilla"])): f for f in filas}
    sem = sorted(s for e, s in por if e == "E0")
    n = len(sem)
    for grupo, alfa, nivel in ((PRIMARIAS, 0.05 / len(PRIMARIAS), "primarias, Bonferroni α = 0,05/3"),
                               ([m for m in SECUNDARIAS if m[0] in ("costoEnergia", "costoCapital")], 0.05, "secundarias, α = 0,05")):
        print(f"   -- {nivel}")
        for e in ("E1", "E2", "E3"):
            for c, nom in grupo:
                val = DERIVADAS.get(c, lambda f, c=c: float(f[c]))
                z = [val(por[(e, s)]) - val(por[("E0", s)]) for s in sem]
                dm, sd = statistics.fmean(z), statistics.stdev(z)
                h = t_cuantil(alfa, n - 1) * sd / math.sqrt(n)
                rel = h / abs(dm)
                nstar = math.ceil(n * (rel / 0.10) ** 2)
                # versión iterativa (Law, ec. 9.40): menor n con t_{n-1,1-α/2}·s/√n ≤ 0,10·|D̄|
                ni = 2
                while t_cuantil(alfa, ni - 1) * sd / math.sqrt(ni) > 0.10 * abs(dm) and ni < 100000:
                    ni += 1
                print(f"   {e} {nom:34s} D̄ = {dm:12.5g}  s = {sd:10.4g}  h = {h:10.4g}  h/|D̄| = {rel:6.3f}  n* = {nstar:5d}"
                      f"  n_iter = {ni:5d}  {'alcanza' if nstar <= n else 'NO alcanza'}")
    tmp.cleanup()


if __name__ == "__main__":
    main()
