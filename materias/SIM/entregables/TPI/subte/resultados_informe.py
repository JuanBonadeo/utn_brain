#!/usr/bin/env python3
"""Figuras y tablas del informe LaTeX a partir de las corridas de producción (E0, E1, E3, E13).

Lee <csv> (filas CSV_PEATONAL) y <csv sin .csv>_ventanas.csv (filas VENTANAS_PEATONAL). Si una (escenario,
semilla) aparece más de una vez, vale la última (el modelo escribe en modo append). La estadística es la de
analisis_corridas.py (t apareado, Bonferroni k = 9 para las primarias, 95 % para las secundarias) y la del
reparto entre molinetes la de validacion_corridas.py; las funciones se importan de ahí, no se duplican.

Salidas (se sobrescriben):
  informe/generado/tabla-resultados.tex, tabla-diferencias.tex, tabla-n-necesario.tex, tabla-validacion.tex,
  valores.tex y ../../../figs/tpi-subte-res-{forest,boxplot,caudal}.png (200 dpi).

Uso: python resultados_informe.py [corridas_peatonales.csv] [--salida-dir DIR]
  Con --salida-dir, todo (tablas y figuras) va a DIR/generado/ y DIR/figs/ en vez de las rutas reales.
Requiere numpy y matplotlib.
"""
import argparse, functools, math, statistics as st, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import analisis_corridas as ac  # noqa: E402
from analisis_corridas import CAMPOS, MEDIDAS, ALTERNATIVAS  # noqa: E402
from validacion_corridas import VENTANAS, cv_sbase  # noqa: E402

ESCENARIOS = ('E0',) + ALTERNATIVAS
MACRO_ESC = {'E0': r'\EO{}', 'E1': r'\EI{}', 'E3': r'\ET{}', 'E13': r'\EIT{}'}
NOMBRE_ESC = {'E0': 'EO', 'E1': 'EI', 'E3': 'ET', 'E13': 'EIT'}  # para nombres de macros (solo letras)
NOMBRE_MED = {'p90': 'PNoventa', 'prop30': 'PropTreinta', 'pico_p90': 'PicoPNoventa', 'espera_media': 'EsperaMedia',
              'pico_media': 'PicoMedia', 'Lq': 'Lq', 'qmax': 'Qmax', 'util': 'Util',
              'drenaje_final': 'DrenajeFinal', 'transito_p90': 'TransitoPNoventa', 'cv_molinetes': 'CvMolinetes'}
DECIMALES = {'p90': 1, 'prop30': 3, 'pico_p90': 1, 'espera_media': 2, 'pico_media': 2, 'Lq': 1, 'qmax': 0,
             'util': 3, 'drenaje_final': 0, 'transito_p90': 1, 'cv_molinetes': 3}
BETA = {'p90': 1.0, 'prop30': 0.01, 'pico_p90': 1.0}  # semiancho objetivo para n*, igual que analisis_corridas
COLOR = {'E0': '#2a78d6', 'E1': '#eb6834', 'E3': '#1baf7a', 'E13': '#eda100'}  # paleta categórica, orden fijo
PRIMARIAS = [(c, n) for c, n, p in MEDIDAS if p]
SECUNDARIAS = [(c, n) for c, n, p in MEDIDAS if not p]
ALFA = 0.05


@functools.lru_cache(maxsize=None)
def tinv(p, v):
    return ac.tinv(p, v)


# ---------------------------------------------------------------- lectura

def leer_corridas(ruta):
    d = {}  # semilla -> escenario -> {campo: valor}; la última fila de cada (escenario, semilla) pisa a las previas
    for linea in open(ruta, encoding='utf-8'):
        if linea.startswith('CSV_PEATONAL;'):
            r = linea.strip().split(';')
            if len(r) < 3 + len(CAMPOS):
                print(f'Aviso: fila CSV_PEATONAL corta ({len(r)} campos), se ignora: {r[1:3]}')
                continue
            d.setdefault(int(r[2]), {})[r[1]] = dict(zip(CAMPOS, map(float, r[3:3 + len(CAMPOS)])))
    return d


def leer_ventanas(ruta):
    unicas = {}
    if not ruta.exists():
        return unicas
    for l in open(ruta, encoding='utf-8'):
        if l.startswith('VENTANAS_PEATONAL;'):
            f = l.strip().split(';')
            if len(f) < 4 + 2 * len(VENTANAS):
                print(f'Aviso: fila VENTANAS_PEATONAL corta, se ignora: {f[1:3]}')
                continue
            unicas[(f[1], int(f[2]))] = {'dia': int(f[3]),
                                         'sim': [float(x) for x in f[4:4 + len(VENTANAS)]],
                                         'obs': [float(x) for x in f[14:14 + len(VENTANAS)]]}
    return unicas


# ---------------------------------------------------------------- cálculo

def comparar(d, k):
    """Diferencias apareadas alternativa - E0, como analisis_corridas.main."""
    res = {}
    for alt in ALTERNATIVAS:
        pares = sorted(s for s in d if {'E0', alt} <= set(d[s]))
        n = len(pares)
        if n < 2:
            print(f'Aviso: {alt} tiene {n} pares con E0; no alcanza para un IC, se omite.')
            continue
        distintos = [s for s in pares if d[s]['E0']['dia'] != d[s][alt]['dia']]
        if distintos:
            print(f'Aviso: {alt}: días SBASE distintos en las semillas {distintos} (se esperaba el mismo día por par).')
        tb, t95 = tinv(1 - ALFA / k / 2, n - 1), tinv(1 - ALFA / 2, n - 1)
        r = {'n': n, 'dias': len({d[s]['E0']['dia'] for s in pares}), 'tb': tb, 't95': t95, 'med': {}, 'nn': {}}
        for clave, _, prim in MEDIDAS:
            D = [d[s][alt][clave] - d[s]['E0'][clave] for s in pares]
            m, sd = st.mean(D), st.stdev(D)
            h = (tb if prim else t95) * sd / math.sqrt(n)
            e0 = st.mean(d[s]['E0'][clave] for s in pares)
            r['med'][clave] = {'m': m, 'sd': sd, 'lo': m - h, 'hi': m + h, 'e0': e0,
                               'cambio': 100 * m / e0 if e0 else None}
        for clave, beta in BETA.items():
            sd = r['med'][clave]['sd']
            r['nn'][clave] = next((i for i in range(2, 1000) if tinv(1 - ALFA / k / 2, i - 1) * sd / math.sqrt(i) <= beta),
                                  None)
        res[alt] = r
    return res


def veredicto(lo, hi):
    return 'mejora' if hi < 0 else 'empeora' if lo > 0 else 'sin evidencia'


# ---------------------------------------------------------------- LaTeX

def tex(s):
    rep = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#', '_': r'\_', '{': r'\{',
           '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}', '>': r'$>$', '<': r'$<$'}
    return ''.join(rep.get(c, c) for c in s)


def num(x, dec):
    if x is None or (isinstance(x, float) and not math.isfinite(x)):
        return '---'
    v = round(x, dec)
    if v == 0:
        v = 0.0  # evita "-0"
    return rf'\num{{{v:.{dec}f}}}'


def ic(lo, hi, dec):
    return f'[{num(lo, dec)}; {num(hi, dec)}]'


def pct(x, dec=1):
    return '---' if x is None else rf'\num{{{x:+.{dec}f}}}~\%'


def escribir(ruta, texto):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto, encoding='utf-8')


def borrar_viejo(ruta):
    # Si una salida no se puede generar, se borra la de una corrida anterior para no citar números viejos.
    if ruta.exists():
        ruta.unlink()
        print(f'  (se borró {ruta.name} de una corrida anterior)')


CABECERA = '% Generado por resultados_informe.py; no editar a mano (se sobrescribe).\n'


def tabla_resultados(d, nrep):
    filas = []
    for grupo in (PRIMARIAS, SECUNDARIAS):
        for clave, nombre in grupo:
            celdas = []
            for e in ESCENARIOS:
                xs = [d[s][e][clave] for s in d if e in d[s]]
                celdas.append(num(st.mean(xs), DECIMALES[clave]) if xs else '---')
            etiqueta = rf'\textbf{{{tex(nombre)}}}' if grupo is PRIMARIAS else tex(nombre)
            filas.append(f'{etiqueta} & ' + ' & '.join(celdas) + r' \\')
        if grupo is PRIMARIAS:
            filas.append(r'\midrule')
    reps = ', '.join(f'{MACRO_ESC[e]}: {nrep[e]}' for e in ESCENARIOS)
    return CABECERA + rf"""\begin{{table}}[H]
\centering
\caption{{Medidas de desempeño por escenario (media entre réplicas)}}
\label{{tab:resultados-escenarios}}
\small
\begin{{tabular}}{{@{{}}lrrrr@{{}}}}
\toprule
Medida & {' & '.join(MACRO_ESC[e] for e in ESCENARIOS)} \\
\midrule
{chr(10).join(filas)}
\bottomrule
\end{{tabular}}

\smallskip
\footnotesize En negrita, las tres medidas primarias. Réplicas por escenario: {reps}.
\end{{table}}
"""


def pie_comparaciones(res, k):
    ns = {(r['n'], r['dias'], round(r['tb'], 4)) for r in res.values()}
    if len(ns) == 1:
        n, dias, tb = ns.pop()
        return (rf'{n} pares por alternativa ({dias} días SBASE distintos); '
                rf'$t_{{1-0{{,}}05/(2\cdot{k}),\,{n - 1}}} = {num(tb, 3)}$.')
    return '; '.join(rf"{MACRO_ESC[a]}: {r['n']} pares, {r['dias']} días, $t = {num(r['tb'], 3)}$"
                     for a, r in res.items()) + '.'


def tabla_diferencias(res, k):
    filas = []
    for i, (alt, r) in enumerate(res.items()):
        if i:
            filas.append(r'\midrule')
        for j, (clave, nombre) in enumerate(PRIMARIAS):
            m = r['med'][clave]; dec = DECIMALES[clave] + 1
            primera = MACRO_ESC[alt] if j == 0 else ''
            filas.append(f"{primera} & {tex(nombre)} & {num(m['m'], dec)} & {ic(m['lo'], m['hi'], dec)} & "
                         f"{pct(m['cambio'])} & {veredicto(m['lo'], m['hi'])} " + r'\\')
    nivel = 100 * (1 - ALFA / k)
    return CABECERA + rf"""\begin{{table}}[H]
\centering
\caption{{Diferencias apareadas contra \EO{{}} en las medidas primarias}}
\label{{tab:diferencias}}
\small
\begin{{tabular}}{{@{{}}llrcrl@{{}}}}
\toprule
Alternativa & Medida & $\bar D$ & IC Bonferroni ({num(nivel, 2)}~\%) & Cambio & Veredicto \\
\midrule
{chr(10).join(filas)}
\bottomrule
\end{{tabular}}

\smallskip
\footnotesize $D = \text{{alternativa}} - \EO{{}}$ por semilla (números aleatorios comunes). Bonferroni con $k = {k}$
(3 primarias $\times$ 3 comparaciones), nivel $1 - 0{{,}}05/{k}$. {pie_comparaciones(res, k)}
Mejora: el IC queda entero por debajo de 0; empeora: entero por encima; sin evidencia: contiene el 0.
\end{{table}}
"""


def tabla_n(res, k):
    filas = []
    for clave, nombre in PRIMARIAS:
        b = BETA[clave]
        celdas = [str(res[a]['nn'][clave]) if a in res and res[a]['nn'][clave] else
                  ('$>$999' if a in res else '---') for a in ALTERNATIVAS]
        filas.append(f'{tex(nombre)} & {num(b, 0 if b >= 1 else 2)} & ' + ' & '.join(celdas) + r' \\')
    n = ', '.join(sorted({str(r['n']) for r in res.values()})) or '---'
    return CABECERA + rf"""\begin{{table}}[H]
\centering
\caption{{Réplicas necesarias $n^*$ para un semiancho $\beta$ del IC Bonferroni}}
\label{{tab:n-necesario}}
\small
\begin{{tabular}}{{@{{}}lrrrr@{{}}}}
\toprule
Medida & $\beta$ & {' & '.join(MACRO_ESC[a] for a in ALTERNATIVAS)} \\
\midrule
{chr(10).join(filas)}
\bottomrule
\end{{tabular}}

\smallskip
\footnotesize $n^* = \min\{{i : t_{{1-0{{,}}05/(2\cdot{k}),\,i-1}}\, s(D)/\sqrt{{i}} \le \beta\}}$, con $s(D)$ de
los {n} pares corridos (Law, §9.5). $\beta$ en segundos para los P90 y en proporción para la espera $>$ 30~s.
\end{{table}}
"""


def validacion(d, ven):
    e0 = [v for (e, _), v in sorted(ven.items()) if e == 'E0']
    if not e0:
        return None
    filas, datos = [], []
    for w, nombre in enumerate(VENTANAS):
        sim = [v['sim'][w] for v in e0]; obs = [v['obs'][w] for v in e0]
        so, ss = st.fmean(obs), st.fmean(sim)
        sesgo = 100 * (ss - so) / so if so else None
        datos.append((so, ss, sesgo, min(sim), max(sim), min(obs), max(obs)))
    to = sum(x[0] for x in datos); ts = sum(x[1] for x in datos)
    cvs = [d[s]['E0']['cv_molinetes'] for s in d if 'E0' in d[s]]
    cv_obs, n_mol, _ = cv_sbase()
    cv_mod = st.fmean(cvs) if cvs else None
    cv_sd = st.stdev(cvs) if len(cvs) > 1 else 0.0
    return {'e0': e0, 'datos': datos, 'to': to, 'ts': ts, 'sesgo_total': 100 * (ts - to) / to if to else None,
            'cv_mod': cv_mod, 'cv_sd': cv_sd, 'cv_n': len(cvs), 'cv_obs': cv_obs, 'cv_nmol': n_mol}


def tabla_validacion(v):
    filas = [f'{nombre} & {num(so, 0)} & {num(ss, 0)} & {pct(sg)} ' + r'\\'
             for nombre, (so, ss, sg, *_) in zip(VENTANAS, v['datos'])]
    filas.append(r'\midrule')
    filas.append(rf"Total franja & {num(v['to'], 0)} & {num(v['ts'], 0)} & {pct(v['sesgo_total'])} \\")
    filas.append(r'\midrule')
    filas.append(rf"\multicolumn{{2}}{{@{{}}l}}{{CV entre molinetes}} & Modelo {num(v['cv_mod'], 3)} & "
                 rf"SBASE {num(v['cv_obs'], 3)} \\")
    return CABECERA + rf"""\begin{{table}}[H]
\centering
\caption{{Validaciones por ventana de 15 minutos en \EO{{}}: observado frente a simulado}}
\label{{tab:validacion-caudal}}
\small
\begin{{tabular}}{{@{{}}lrrr@{{}}}}
\toprule
Ventana & Observado medio & Simulado medio & Sesgo \\
\midrule
{chr(10).join(filas)}
\bottomrule
\end{{tabular}}

\smallskip
\footnotesize Medias sobre {len(v['e0'])} réplicas de \EO{{}}; el observado es el perfil SBASE del día de cada
réplica. Sesgo $= (\text{{sim}} - \text{{obs}})/\text{{obs}}$. CV del modelo: media de {v['cv_n']} réplicas
(desvío {num(v['cv_sd'], 3)}); CV de SBASE entre los {v['cv_nmol']} molinetes con participación
$\ge$ \num{{0.5}}~\% del vestíbulo Principal.
\end{{table}}
"""


def valores(d, res, k, v, nrep):
    L = [CABECERA.strip(), '% Números clave para citar en el texto. Valores con \\num (coma decimal).']

    def nc(nombre, valor):
        assert nombre.isalpha(), nombre
        L.append(rf'\newcommand{{\{nombre}}}{{{valor}}}')

    # Todas las macros se definen siempre: si falta el dato, quedan como \\pendiente{} y el texto compila igual.
    falta = r'\pendiente{sin datos}'
    nc('kBonferroni', str(k))
    nc('nivelBonferroni', num(100 * (1 - ALFA / k), 2))
    r0 = next(iter(res.values()), None)
    nc('nPares', str(r0['n']) if r0 else falta)
    nc('nDias', str(r0['dias']) if r0 else falta)
    nc('tCritico', num(r0['tb'], 3) if r0 else falta)
    for e in ESCENARIOS:
        nc('nRep' + NOMBRE_ESC[e], str(nrep[e]))
        for clave, _, prim in MEDIDAS:
            xs = [d[s][e][clave] for s in d if e in d[s]]
            nc(NOMBRE_MED[clave][0].lower() + NOMBRE_MED[clave][1:] + NOMBRE_ESC[e],
               num(st.mean(xs), DECIMALES[clave]) if xs else falta)
    for alt in ALTERNATIVAS:
        r = res.get(alt); a = NOMBRE_ESC[alt]
        for clave, _ in PRIMARIAS:
            med = NOMBRE_MED[clave]; dec = DECIMALES[clave] + 1
            m = r['med'][clave] if r else None
            nc(f'dif{med}{a}', num(m['m'], dec) if m else falta)
            nc(f'icInf{med}{a}', num(m['lo'], dec) if m else falta)
            nc(f'icSup{med}{a}', num(m['hi'], dec) if m else falta)
            nc(f'cambio{med}{a}', pct(m['cambio']) if m else falta)
            nc(f'veredicto{med}{a}', veredicto(m['lo'], m['hi']) if m else falta)
            nc(f'nNec{med}{a}', (str(r['nn'][clave]) if r['nn'][clave] else '$>$999') if r else falta)
    nc('sesgoCaudalTotal', pct(v['sesgo_total']) if v else falta)
    nc('cvModeloEO', num(v['cv_mod'], 3) if v else falta)
    nc('cvSbase', num(v['cv_obs'], 3) if v else falta)
    return '\n'.join(L) + '\n'


# ---------------------------------------------------------------- figuras

def preparar_mpl():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter
    plt.rcParams.update({'font.size': 9, 'axes.spines.top': False, 'axes.spines.right': False,
                         'axes.edgecolor': '#52514e', 'axes.labelcolor': '#0b0b0b', 'xtick.color': '#52514e',
                         'ytick.color': '#52514e', 'axes.grid': True, 'grid.color': '#e4e3df', 'grid.linewidth': 0.6,
                         'axes.axisbelow': True, 'savefig.dpi': 200, 'figure.dpi': 100})
    coma = FuncFormatter(lambda x, _: f'{x:g}'.replace('.', ',').replace('-', '−'))
    return plt, coma


def fig_forest(res, k, ruta, plt, coma):
    fig, axes = plt.subplots(1, len(PRIMARIAS), figsize=(9, 2.8), sharey=True)
    alts = list(res)
    for ax, (clave, nombre) in zip(axes, PRIMARIAS):
        for i, a in enumerate(alts):
            m = res[a]['med'][clave]
            y = len(alts) - 1 - i
            ax.plot([m['lo'], m['hi']], [y, y], color=COLOR[a], lw=2, solid_capstyle='round')
            ax.plot(m['m'], y, 'o', color=COLOR[a], ms=7, mec='white', mew=1.5)
        ax.axvline(0, color='#52514e', lw=1, ls='--')
        ax.set_title(nombre, fontsize=9)
        ax.set_xlabel('Diferencia contra E0')
        ax.xaxis.set_major_formatter(coma)
        ax.grid(axis='y', visible=False)
        ax.margins(x=0.15)
    axes[0].set_yticks(range(len(alts)), list(reversed(alts)))
    axes[0].set_ylim(-0.6, len(alts) - 0.4)
    fig.suptitle(f'Diferencias apareadas (alternativa − E0) con IC Bonferroni al '
                 f'{100 * (1 - ALFA / k):.2f} %'.replace('.', ','), fontsize=10)
    fig.tight_layout()
    fig.savefig(ruta); plt.close(fig)


def fig_boxplot(d, ruta, plt, coma):
    esc = [e for e in ESCENARIOS if any(e in d[s] for s in d)]
    fig, ax = plt.subplots(figsize=(6.5, 4))
    for s in sorted(d):
        xs = [i for i, e in enumerate(esc) if e in d[s]]
        ax.plot(xs, [d[s][esc[i]]['p90'] for i in xs], color='#9a9993', lw=0.8, alpha=0.7, zorder=2)
    datos = [[d[s][e]['p90'] for s in d if e in d[s]] for e in esc]
    bp = ax.boxplot(datos, positions=range(len(esc)), widths=0.45, patch_artist=True, showfliers=False, zorder=1,
                    medianprops={'color': '#0b0b0b', 'lw': 1.5}, whiskerprops={'color': '#52514e'},
                    capprops={'color': '#52514e'}, boxprops={'edgecolor': '#52514e'})
    for caja, e in zip(bp['boxes'], esc):
        caja.set_facecolor(COLOR[e]); caja.set_alpha(0.35)
    for i, (e, xs) in enumerate(zip(esc, datos)):
        ax.plot([i] * len(xs), xs, 'o', color=COLOR[e], ms=5, mec='white', mew=1, zorder=3)
    ax.set_xticks(range(len(esc)), esc)
    ax.set_ylabel('P90 de espera (s)')
    ax.set_title('P90 de espera por escenario; cada línea gris une las réplicas de una misma semilla', fontsize=9)
    ax.yaxis.set_major_formatter(coma)
    ax.grid(axis='x', visible=False)
    fig.tight_layout(); fig.savefig(ruta); plt.close(fig)


def fig_caudal(v, ruta, plt, coma):
    x = range(len(VENTANAS))
    so, ss, _, smin, smax, omin, omax = zip(*v['datos'])
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.fill_between(x, omin, omax, color=COLOR['E0'], alpha=0.15, lw=0)
    ax.fill_between(x, smin, smax, color=COLOR['E1'], alpha=0.15, lw=0)
    ax.plot(x, so, '-o', color=COLOR['E0'], lw=2, ms=5, mec='white', label='Observado SBASE (media y mín–máx)')
    ax.plot(x, ss, '-s', color=COLOR['E1'], lw=2, ms=5, mec='white', label='Simulado E0 (media y mín–máx)')
    ax.set_xticks(list(x), VENTANAS, rotation=0, fontsize=8)
    ax.set_xlabel('Inicio de la ventana de 15 min')
    ax.set_ylabel('Validaciones por ventana')
    ax.yaxis.set_major_formatter(FuncFormatterMiles())
    ax.legend(frameon=False, fontsize=8, loc='upper left')
    ax.set_title(f"Caudal por ventana en E0 ({len(v['e0'])} réplicas)", fontsize=9)
    ax.grid(axis='x', visible=False)
    fig.tight_layout(); fig.savefig(ruta); plt.close(fig)


def FuncFormatterMiles():
    from matplotlib.ticker import FuncFormatter
    return FuncFormatter(lambda y, _: f'{y:,.0f}'.replace(',', '.'))


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('csv', nargs='?', default=str(AQUI / 'corridas_peatonales.csv'))
    ap.add_argument('--salida-dir', help='escribir en DIR/generado y DIR/figs (para pruebas)')
    a = ap.parse_args()
    ruta = Path(a.csv)
    if a.salida_dir:
        gen, figs = Path(a.salida_dir) / 'generado', Path(a.salida_dir) / 'figs'
    else:
        gen, figs = AQUI / 'informe' / 'generado', AQUI.parents[2] / 'figs'
    if not ruta.exists():
        print(f'No existe {ruta}; nada que hacer.'); return 1
    d = leer_corridas(ruta)
    ven = leer_ventanas(ruta.with_name(ruta.stem + '_ventanas.csv'))
    if not d:
        print(f'{ruta} no tiene filas CSV_PEATONAL; nada que hacer.'); return 1
    nrep = {e: sum(1 for s in d if e in d[s]) for e in ESCENARIOS}
    faltan = [e for e in ESCENARIOS if not nrep[e]]
    if faltan:
        print(f'Aviso: faltan escenarios {faltan}.')
    k = len(PRIMARIAS) * len(ALTERNATIVAS)  # familia planificada, aunque falte alguna alternativa
    res = comparar(d, k)
    v = validacion(d, ven)
    if v is None:
        print('Aviso: no hay filas VENTANAS_PEATONAL de E0; se omiten tabla-validacion y la figura de caudal.')

    escribir(gen / 'tabla-resultados.tex', tabla_resultados(d, nrep))
    hechos = ['tabla-resultados.tex']
    if res:
        escribir(gen / 'tabla-diferencias.tex', tabla_diferencias(res, k))
        escribir(gen / 'tabla-n-necesario.tex', tabla_n(res, k))
        hechos += ['tabla-diferencias.tex', 'tabla-n-necesario.tex']
    else:
        print('Aviso: ninguna alternativa tiene 2 pares o más; se omiten tabla-diferencias y tabla-n-necesario.')
        borrar_viejo(gen / 'tabla-diferencias.tex'); borrar_viejo(gen / 'tabla-n-necesario.tex')
    if v:
        escribir(gen / 'tabla-validacion.tex', tabla_validacion(v)); hechos.append('tabla-validacion.tex')
    else:
        borrar_viejo(gen / 'tabla-validacion.tex')
    escribir(gen / 'valores.tex', valores(d, res, k, v, nrep)); hechos.append('valores.tex')

    plt, coma = preparar_mpl()
    figs.mkdir(parents=True, exist_ok=True)
    if res:
        fig_forest(res, k, figs / 'tpi-subte-res-forest.png', plt, coma); hechos.append('tpi-subte-res-forest.png')
    else:
        borrar_viejo(figs / 'tpi-subte-res-forest.png')
    fig_boxplot(d, figs / 'tpi-subte-res-boxplot.png', plt, coma); hechos.append('tpi-subte-res-boxplot.png')
    if v:
        fig_caudal(v, figs / 'tpi-subte-res-caudal.png', plt, coma); hechos.append('tpi-subte-res-caudal.png')
    else:
        borrar_viejo(figs / 'tpi-subte-res-caudal.png')

    # Resumen
    print(f"Réplicas: {', '.join(f'{e}={nrep[e]}' for e in ESCENARIOS)}; k = {k}")
    for alt, r in res.items():
        print(f"{alt} - E0 ({r['n']} pares, {r['dias']} días, t = {r['tb']:.4f}):")
        for clave, nombre in PRIMARIAS:
            m = r['med'][clave]
            cambio = f"{m['cambio']:+.1f} %" if m['cambio'] is not None else '—'
            print(f"  {clave:9s} D = {m['m']:.3f} [{m['lo']:.3f}; {m['hi']:.3f}] {cambio}  "
                  f"{veredicto(m['lo'], m['hi'])}; n* = {r['nn'][clave]}")
    if v:
        print(f"Caudal E0: sesgo total {v['sesgo_total']:+.1f} %; CV modelo {v['cv_mod']:.3f} vs SBASE {v['cv_obs']:.3f}")
    print(f'Escrito en {gen} y {figs}: {", ".join(hechos)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
