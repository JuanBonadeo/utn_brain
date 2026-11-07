#!/usr/bin/env python3
"""Genera TPI_Caser_Resultados_Corridas.xlsx (planilla de la entrega final) desde un CSV de corridas.

Uso, desde la raíz del repo:
    .venv/Scripts/python.exe -I materias/SIM/entregables/TPI/caser/modelo/construir_planilla.py [corridas.csv] [--verificar]

Sin argumento usa `corridas_horno.csv` (el que escribe el experimento CorridasE0E3 de AnyLogic) si existe y tiene
todas las columnas que hacen falta; si no, `corridas_horno_harness.csv` (motor mínimo del verificador).
`--verificar` recalcula la planilla con la librería `formulas` (no hace falta Excel ni LibreOffice) y compara cada
celda de los tests y de los costos contra `analizar_corridas.py` sobre el mismo CSV.

Las medidas, los nombres, los grupos (primarias con Bonferroni / secundarias al 95 %) y el test apareado salen de
`analizar_corridas.py` (se importa): la planilla y el análisis no se pueden desincronizar. Todo lo que se calcula
en la planilla (resumen, diferencias, IC, costos) son fórmulas vivas sobre la hoja Corridas.
"""
from __future__ import annotations

import csv
import math
import statistics
import sys
from datetime import date, datetime
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
_argv = sys.argv
sys.argv = sys.argv[:1]  # analizar_corridas lee sys.argv al importarse
import analizar_corridas as ac  # noqa: E402

sys.argv = _argv

SALIDA = AQUI.parent / "TPI_Caser_Resultados_Corridas.xlsx"
ALFA = 0.05

# Medidas del test, en el orden y con los nombres de analizar_corridas.py.
TEST = [(c, n, "Primaria") for c, n in ac.PRIMARIAS] + [(c, n, "Secundaria") for c, n in ac.SECUNDARIAS]
K_PRIMARIAS = len(ac.PRIMARIAS)
# Resumen por escenario: las del test más las dos partes de la energía.
RESUMEN = []
for c, n, _ in TEST:
    RESUMEN.append((c, n))
    if c == "costoEnergia":
        RESUMEN += [("costoLuz", "luz: kWh × tarifa marginal ($)"), ("costoGLP", "gas: GLP × precio ($)")]

ETIQUETA_ESC = {"E0": "base", "E1": "umbral bajo", "E2": "umbral + espera máxima", "E3": "apagar enseguida"}

# Columnas del CSV: encabezado legible (con unidad) y formato numérico.
COLUMNAS = {
    "escenario": ("Escenario", None),
    "semilla": ("Semilla", "0"),
    "umbralULI": ("Umbral de encendido (ULI)", "0"),
    "esperaMaxDias": ("Espera máxima permitida (días; ∞ = sin límite)", "0"),
    "horasEnVacio": ("Horas caliente en vacío antes de apagar (h)", "0"),
    "modoFinCampana": ("Fin de campaña (modo)", None),
    "pPrioridad": ("P(ULI urgente)", "0.0000"),
    "factorDemanda": ("Factor de demanda", "0.00"),
    "minPorULI": ("Ciclo por ULI (min)", "0.00"),
    "horasMedidas": ("Horizonte medido (h)", "#,##0"),
    "nLlegadas": ("ULI llegadas", "#,##0"),
    "nTratadas": ("ULI tratadas", "#,##0"),
    "kgTratados": ("kg tratados", "#,##0"),
    "nEncendidos": ("Encendidos", "0"),
    "nEncendidosPrioridad": ("Encendidos por prioridad", "0"),
    "campanasPorMes": ("Campañas por mes", "0.000"),
    "uliPorCampanaMedia": ("ULI por campaña (media)", "#,##0.0"),
    "uliPorCampanaMediana": ("ULI por campaña (mediana)", "#,##0.0"),
    "diasPorCampanaMedia": ("Duración de campaña (días, media)", "0.00"),
    "colaAlEncenderMedia": ("Cola al encender (ULI, media)", "0.0"),
    "colaAlApagarMedia": ("Cola al apagar (ULI, media)", "0.0"),
    "esperaMediaDias": ("Espera media en cola (días)", "0.00"),
    "esperaP90Dias": ("Espera p90 (días)", "0.00"),
    "esperaMaximaDias": ("Espera máxima observada (días)", "0.00"),
    "colaMediaULI": ("Cola media (ULI)", "0.00"),
    "colaMediaKg": ("kg promedio en cola", "#,##0"),
    "sistemaMedioULI": ("ULI medias en el sistema", "0.00"),
    "sistemaMedioHoras": ("Tiempo medio en el sistema (h)", "0.00"),
    "utilizacion": ("Utilización (fracción)", "0.0000"),
    "fraccionCaliente": ("Fracción del tiempo a temperatura", "0.0000"),
    "kWhTotal": ("Energía eléctrica (kWh)", "#,##0"),
    "kWhPorKg": ("kWh por kg tratado", "0.000"),
    "costoEnergiaPorKg": ("Energía por kg ($/kg)", "#,##0.00"),
    "glpKg": ("GLP del año (kg)", "#,##0"),
    "costoLuz": ("Luz ($)", "#,##0"),
    "costoGLP": ("Gas ($)", "#,##0"),
    "costoCapital": ("Capital parado al 2 % mensual ($)", "#,##0"),
    "costoTotal": ("Costo relevante del año ($)", "#,##0"),
}
# Columna calculada que se agrega al final de Corridas (fórmula viva), con la misma definición que ac.DERIVADAS.
DERIVADA = ("costoEnergia", "Energía: luz + gas ($)", "#,##0", ("costoLuz", "costoGLP"))
FMT_MEDIDA = {c: COLUMNAS[c][1] for c in COLUMNAS} | {DERIVADA[0]: DERIVADA[2]}
REQUERIDAS = {"escenario", "semilla", "umbralULI", "esperaMaxDias", "horasEnVacio", *DERIVADA[3]} | \
             {c for c, _ in RESUMEN if c != DERIVADA[0]}
assert ac.DERIVADAS.keys() == {DERIVADA[0]}

# ---------------------------------------------------------------- estilo
AZUL_OSCURO, AZUL_CLARO, GRIS_CLARO = "FF17365D", "FFD9EAF7", "FFF2F2F2"
VERDE_F, VERDE_T, GRIS_F, GRIS_T = "FFC6EFCE", "FF006100", "FFE7E6E6", "FF595959"
FUENTE = "Arial"
F_NORMAL = Font(name=FUENTE, size=10)
F_NEGRITA = Font(name=FUENTE, size=10, bold=True)
F_TITULO = Font(name=FUENTE, size=14, bold=True, color=AZUL_OSCURO)
F_SUB = Font(name=FUENTE, size=11, bold=True, color=AZUL_OSCURO)
F_NOTA = Font(name=FUENTE, size=9, italic=True, color=GRIS_T)
F_ENC = Font(name=FUENTE, size=10, bold=True, color="FFFFFFFF")
RELLENO_ENC = PatternFill("solid", fgColor=AZUL_OSCURO)
RELLENO_ENC2 = PatternFill("solid", fgColor=AZUL_CLARO)
RELLENO_PARAM = PatternFill("solid", fgColor="FFFFF2CC")
BORDE = Border(bottom=Side(style="thin", color="FFBFBFBF"))


def encabezado(ws, fila, col, texto, claro=False):
    c = ws.cell(fila, col, texto)
    c.font = F_NEGRITA if claro else F_ENC
    c.fill = RELLENO_ENC2 if claro else RELLENO_ENC
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    return c


def celda(ws, fila, col, valor, fmt=None, negrita=False, alinear=None):
    c = ws.cell(fila, col, valor)
    c.font = F_NEGRITA if negrita else F_NORMAL
    if fmt:
        c.number_format = fmt
    if alinear:
        c.alignment = Alignment(horizontal="left" if alinear == "wrap" else alinear, vertical="center", wrap_text=alinear == "wrap")
    c.border = BORDE
    return c


def si_no(ws, rango):
    ws.conditional_formatting.add(rango, CellIsRule(operator="equal", formula=['"sí"'],
                                                    fill=PatternFill("solid", bgColor=VERDE_F),
                                                    font=Font(color=VERDE_T, bold=True)))
    ws.conditional_formatting.add(rango, CellIsRule(operator="equal", formula=['"no"'],
                                                    fill=PatternFill("solid", bgColor=GRIS_F),
                                                    font=Font(color=GRIS_T)))


def anchos(ws, valores):
    for j, a in enumerate(valores, 1):
        ws.column_dimensions[get_column_letter(j)].width = a


def ref(hoja, col, fila, abs_=True):
    d = "$" if abs_ else ""
    return f"'{hoja}'!{d}{col}{d}{fila}"


# ---------------------------------------------------------------- datos
def elegir_csv(args):
    if args:
        p = Path(args[0])
        faltan = REQUERIDAS - set(next(csv.reader(open(p, encoding="utf-8"), delimiter=";")))
        if faltan:
            sys.exit(f"{p.name} no tiene las columnas {sorted(faltan)}")
        return p
    for p in (AQUI / "corridas_horno.csv", AQUI / "corridas_horno_harness.csv"):
        if p.exists():
            faltan = REQUERIDAS - set(next(csv.reader(open(p, encoding="utf-8"), delimiter=";")))
            if not faltan:
                return p
            print(f"AVISO: {p.name} existe pero no tiene {sorted(faltan)} (es de un modelo viejo): se ignora")
    sys.exit("no hay un CSV de corridas utilizable")


def a_valor(col, texto):
    if col in ("escenario", "modoFinCampana"):
        return texto
    try:
        v = float(texto)
    except ValueError:
        return texto
    if math.isinf(v):
        return "∞"
    if math.isnan(v):
        return None
    return int(v) if col == "semilla" else v


# ---------------------------------------------------------------- hojas
def hoja_corridas(wb, por, esc, sem, columnas):
    ws = wb.create_sheet("Corridas")
    letra = {}
    for j, col in enumerate(columnas, 1):
        encabezado(ws, 1, j, COLUMNAS.get(col, (col, None))[0])
        letra[col] = get_column_letter(j)
    jd = len(columnas) + 1
    encabezado(ws, 1, jd, DERIVADA[1])
    letra[DERIVADA[0]] = get_column_letter(jd)
    ws.row_dimensions[1].height = 54
    fila_de = {}
    fila = 2
    for e in esc:
        for s in sem:
            fila_de[(e, s)] = fila
            f = por[(e, s)]
            for j, col in enumerate(columnas, 1):
                c = ws.cell(fila, j, a_valor(col, f[col]))
                c.font = F_NORMAL
                fmt = COLUMNAS.get(col, (None, None))[1]
                if fmt:
                    c.number_format = fmt
            a, b = (letra[x] for x in DERIVADA[3])
            c = ws.cell(fila, jd, f"={a}{fila}+{b}{fila}")
            c.font, c.number_format = F_NORMAL, DERIVADA[2]
            fila += 1
    ultima = fila - 1
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = f"A1:{get_column_letter(jd)}{ultima}"
    for j in range(1, jd + 1):
        ws.column_dimensions[get_column_letter(j)].width = 11 if j > 2 else 10
    ws.column_dimensions[letra["modoFinCampana"]].width = 15 if "modoFinCampana" in letra else 11
    return letra, fila_de


def bloque(letra, fila_de, e, sem, col):
    """Rango de la hoja Corridas con la medida `col` de las n réplicas del escenario e (filas contiguas)."""
    a, b = fila_de[(e, sem[0])], fila_de[(e, sem[-1])]
    assert b - a + 1 == len(sem)
    return f"Corridas!${letra[col]}${a}:${letra[col]}${b}"


def hoja_resumen(wb, letra, fila_de, esc, sem):
    ws = wb.create_sheet("Resumen por escenario")
    ws.cell(1, 1, "Resumen por escenario").font = F_TITULO
    ws.cell(2, 1, f"Media, desvío estándar muestral, mínimo y máximo de las n = {len(sem)} réplicas de cada escenario "
                  "(fórmulas sobre la hoja Corridas).").font = F_NOTA
    encabezado(ws, 4, 1, "Medida")
    ws.merge_cells(start_row=4, start_column=1, end_row=5, end_column=1)
    stats = (("Media", "AVERAGE"), ("Desvío", "STDEV"), ("Mínimo", "MIN"), ("Máximo", "MAX"))
    for i, e in enumerate(esc):
        c0 = 2 + 4 * i
        encabezado(ws, 4, c0, f"{e} — {ETIQUETA_ESC.get(e, '')}")
        ws.merge_cells(start_row=4, start_column=c0, end_row=4, end_column=c0 + 3)
        for k, (nom, _) in enumerate(stats):
            encabezado(ws, 5, c0 + k, nom, claro=True)
    for r, (col, nombre) in enumerate(RESUMEN, 6):
        celda(ws, r, 1, nombre, negrita=True)
        for i, e in enumerate(esc):
            for k, (_, fn) in enumerate(stats):
                celda(ws, r, 2 + 4 * i + k, f"={fn}({bloque(letra, fila_de, e, sem, col)})", FMT_MEDIDA[col])
    ws.freeze_panes = "B6"
    anchos(ws, [36] + [13] * 4 * len(esc))
    return {col: 6 + r for r, (col, _) in enumerate(RESUMEN)}


def hoja_test(wb, letra, fila_de, e, sem, celdas_param):
    nombre = f"Test {e}-E0"
    ws = wb.create_sheet(nombre)
    n = len(sem)
    ws.cell(1, 1, f"Test de medias apareado: {e} ({ETIQUETA_ESC.get(e, '')}) contra E0 (base)").font = F_TITULO
    ws.cell(2, 1, f"D_j = X({e}, semilla j) − X(E0, semilla j), números aleatorios comunes. D > 0: la alternativa "
                  "aumenta la medida (en costos, D < 0 es ahorro). IC = D̄ ± t·s_D/√n con t = T.INV.2T(α; n−1).").font = F_NOTA
    ws.cell(3, 1, "Primarias con Bonferroni (α = α_global / k); secundarias con α = α_global individual. "
                  "α_global y k se editan en la hoja Léame.").font = F_NOTA
    cols = ["Medida", "Grupo", "α", "Nivel", "n", "Media E0", f"Media {e}", "D̄", "s_D", "t crítico",
            "Semiamplitud t·s_D/√n", "IC inferior", "IC superior", "¿≠ 0?"]
    F0 = 5
    for j, t in enumerate(cols, 1):
        encabezado(ws, F0, j, t)
    ws.row_dimensions[F0].height = 30
    FD = F0 + len(TEST) + 3  # encabezado de la tabla de diferencias
    d1, dn = FD + 1, FD + n
    ws.cell(FD - 1, 1, "Diferencias por semilla (D_j)").font = F_SUB
    encabezado(ws, FD, 1, "Semilla")
    a_ref, k_ref = celdas_param
    filas = {}
    for i, (col, nom, grupo) in enumerate(TEST):
        r = F0 + 1 + i
        filas[col] = r
        cd = get_column_letter(2 + i)  # columna de diferencias de esta medida
        rd = f"${cd}${d1}:${cd}${dn}"
        fmt = FMT_MEDIDA[col]
        celda(ws, r, 1, nom, negrita=True)
        celda(ws, r, 2, grupo, alinear="center")
        celda(ws, r, 3, f'=IF(B{r}="Primaria",{a_ref}/{k_ref},{a_ref})', "0.0000")
        celda(ws, r, 4, f"=1-C{r}", "0.0%")
        celda(ws, r, 5, f"=COUNT({rd})", "0")
        celda(ws, r, 6, f"=AVERAGE({bloque(letra, fila_de, 'E0', sem, col)})", fmt)
        celda(ws, r, 7, f"=AVERAGE({bloque(letra, fila_de, e, sem, col)})", fmt)
        celda(ws, r, 8, f"=AVERAGE({rd})", fmt, negrita=True)
        celda(ws, r, 9, f"=STDEV({rd})", fmt)
        celda(ws, r, 10, f"=_xlfn.T.INV.2T(C{r},E{r}-1)", "0.0000")
        celda(ws, r, 11, f"=J{r}*I{r}/SQRT(E{r})", fmt)
        celda(ws, r, 12, f"=H{r}-K{r}", fmt)
        celda(ws, r, 13, f"=H{r}+K{r}", fmt)
        celda(ws, r, 14, f'=IF(OR(L{r}>0,M{r}<0),"sí","no")', alinear="center")
        # tabla de diferencias
        encabezado(ws, FD, 2 + i, nom)
        for j, s in enumerate(sem):
            rr = d1 + j
            fk, f0 = fila_de[(e, s)], fila_de[("E0", s)]
            celda(ws, rr, 2 + i, f"=Corridas!{letra[col]}{fk}-Corridas!{letra[col]}{f0}", fmt)
    for j, s in enumerate(sem):
        celda(ws, d1 + j, 1, s, "0", alinear="center")
    ws.row_dimensions[FD].height = 54
    si_no(ws, f"N{F0 + 1}:N{F0 + len(TEST)}")
    ws.freeze_panes = f"B{F0 + 1}"
    anchos(ws, [36, 11, 9, 8, 6, 14, 14, 14, 13, 9, 14, 14, 14, 8])
    return nombre, filas


def hoja_costos(wb, letra, fila_de, esc, sem, tests):
    ws = wb.create_sheet("Costos")
    ws.cell(1, 1, "Costo relevante del año por escenario (millones de $)").font = F_TITULO
    ws.cell(2, 1, "Media de las réplicas. Luz a tarifa marginal (el cargo fijo de potencia es hundido), gas = GLP × "
                  "precio, capital = 2 % mensual sobre el kg promedio en cola × costo del producto.").font = F_NOTA
    ws.cell(3, 1, "Ahorro = total E0 − total Ek (positivo = la alternativa cuesta menos). El IC del ahorro es el del "
                  "test apareado del costo relevante (hoja Test Ek-E0), con signo cambiado.").font = F_NOTA
    cols = ["Escenario", "Luz (M$)", "Gas (M$)", "Energía: luz + gas (M$)", "Capital parado (M$)",
            "Costo relevante total (M$)", "Ahorro vs E0 (M$)", "Ahorro vs E0 (%)", "IC del ahorro: inferior (M$)",
            "IC del ahorro: superior (M$)", "Nivel del IC", "¿Ahorro ≠ 0?"]
    F0 = 5
    for j, t in enumerate(cols, 1):
        encabezado(ws, F0, j, t)
    ws.row_dimensions[F0].height = 44
    fmt = "#,##0.00"
    r0 = F0 + 1
    for i, e in enumerate(esc):
        r = r0 + i
        celda(ws, r, 1, f"{e} — {ETIQUETA_ESC.get(e, '')}", negrita=True)
        for j, col in enumerate(("costoLuz", "costoGLP", "costoEnergia", "costoCapital", "costoTotal"), 2):
            celda(ws, r, j, f"=AVERAGE({bloque(letra, fila_de, e, sem, col)})/10^6", fmt)
        if e == "E0":
            for j in range(7, 13):
                celda(ws, r, j, "—", alinear="center")
            continue
        hoja, filas = tests[e]
        rt = filas["costoTotal"]
        celda(ws, r, 7, f"=$F${r0}-F{r}", fmt, negrita=True)
        celda(ws, r, 8, f"=G{r}/$F${r0}", "0.0%", negrita=True)
        celda(ws, r, 9, f"=-{ref(hoja, 'M', rt)}/10^6", fmt)
        celda(ws, r, 10, f"=-{ref(hoja, 'L', rt)}/10^6", fmt)
        celda(ws, r, 11, f"={ref(hoja, 'D', rt)}", "0.0%")
        celda(ws, r, 12, f"={ref(hoja, 'N', rt)}", alinear="center")
    si_no(ws, f"L{r0}:L{r0 + len(esc) - 1}")
    anchos(ws, [26, 11, 11, 13, 13, 14, 13, 11, 14, 14, 9, 10])
    return r0


def hoja_leame(ws, arch, por, esc, sem, columnas, nombres_test):
    n = len(sem)
    ws.title = "Léame"
    ws.cell(1, 1, "TPI Simulación — Horno de cementado (Caser): resultados de las corridas").font = F_TITULO
    r = 3
    mod = datetime.fromtimestamp(arch.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
    filas_csv = sum(1 for _ in open(arch, encoding="utf-8")) - 1
    for k, v in (("Archivo de corridas", arch.name), ("Fecha del archivo", mod),
                 ("Filas del CSV", filas_csv), ("Generada el", date.today().isoformat()),
                 ("Generada con", "modelo/construir_planilla.py (regenerar con el CSV nuevo, no editar a mano)")):
        celda(ws, r, 1, k, negrita=True)
        celda(ws, r, 2, v, alinear="left")
        r += 1

    r += 1
    ws.cell(r, 1, "Hojas").font = F_SUB
    r += 1
    hojas = [("Corridas", f"Las {len(esc) * n} corridas crudas (una fila por escenario y semilla), tal como las escribió "
                          "el modelo, con encabezados legibles. La última columna (energía = luz + gas) es una fórmula."),
             ("Resumen por escenario", "Media, desvío, mínimo y máximo de cada medida para cada escenario."),
             *[(h, f"Test de medias apareado {h[5:7]} − E0: las {n} diferencias por semilla de cada medida, D̄, s_D, "
                   "t crítico, semiamplitud, IC y si la diferencia es significativa.") for h in nombres_test],
             ("Costos", "Luz, gas, capital y total por escenario en millones de $, y ahorro de cada alternativa "
                        "contra E0 en $ y en %, con su IC.")]
    for h, d in hojas:
        celda(ws, r, 1, h, negrita=True)
        celda(ws, r, 2, d, alinear="wrap")
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
        ws.row_dimensions[r].height = 28
        r += 1

    r += 1
    ws.cell(r, 1, "Escenarios").font = F_SUB
    r += 1
    params = ["umbralULI", "esperaMaxDias", "horasEnVacio"]
    for j, t in enumerate(["Escenario", "Descripción"] + [COLUMNAS[p][0] for p in params], 1):
        encabezado(ws, r, j, t)
    ws.row_dimensions[r].height = 44
    r += 1
    for e in esc:
        f = por[(e, sem[0])]
        celda(ws, r, 1, e, negrita=True, alinear="center")
        celda(ws, r, 2, ETIQUETA_ESC.get(e, ""))
        for j, p in enumerate(params, 3):
            celda(ws, r, j, a_valor(p, f[p]), COLUMNAS[p][1], alinear="center")
        r += 1
    comunes = [c for c in ("modoFinCampana", "pPrioridad", "factorDemanda", "minPorULI", "horasMedidas")
               if c in columnas and len({por[k][c] for k in por}) == 1]
    if comunes:
        f = por[(esc[0], sem[0])]
        txt = "; ".join(f"{COLUMNAS[c][0]} = " + f"{a_valor(c, f[c]):g}".replace(".", ",") if isinstance(a_valor(c, f[c]), float)
                        else f"{COLUMNAS[c][0]} = {f[c]}" for c in comunes)
        ws.cell(r, 1, f"Iguales en todas las corridas: {txt}.").font = F_NOTA
        r += 1

    r += 1
    ws.cell(r, 1, "Diseño del experimento y test").font = F_SUB
    r += 1
    celda(ws, r, 1, "Réplicas por escenario (n)", negrita=True)
    celda(ws, r, 2, n, "0", alinear="left")
    celda(ws, r, 3, f"semillas {sem[0]}..{sem[-1]}, apareadas: la misma semilla da las mismas ULI en todos los "
                    "escenarios (números aleatorios comunes)")
    r += 1
    celda(ws, r, 1, "α global (familiar)", negrita=True)
    c = celda(ws, r, 2, ALFA, "0.00", alinear="left")
    c.fill = RELLENO_PARAM
    a_ref = f"'Léame'!$B${r}"
    celda(ws, r, 3, "editable: los tests se recalculan")
    r += 1
    celda(ws, r, 1, "k = medidas primarias (Bonferroni)", negrita=True)
    c = celda(ws, r, 2, K_PRIMARIAS, "0", alinear="left")
    c.fill = RELLENO_PARAM
    k_ref = f"'Léame'!$B${r}"
    r += 1
    celda(ws, r, 1, "Primarias: α = α_global / k", negrita=True)
    celda(ws, r, 2, f"={a_ref}/{k_ref}", "0.0000", alinear="left")
    celda(ws, r, 3, f"=\"nivel de confianza \"&ROUND(100*(1-B{r}),1)&\" %\"&\" cada una: \"&\""
                    f"{', '.join(nm for _, nm in ac.PRIMARIAS)}\"")
    r += 1
    celda(ws, r, 1, "Secundarias: α = α_global", negrita=True)
    celda(ws, r, 2, f"={a_ref}", "0.0000", alinear="left")
    celda(ws, r, 3, f"=\"nivel de confianza \"&ROUND(100*(1-B{r}),1)&\" %\"&\" individual: \"&\""
                    f"{', '.join(nm for _, nm in ac.SECUNDARIAS)}\"")
    r += 2

    ws.cell(r, 1, "Test de medias apareado (Law, cap. 10)").font = F_SUB
    r += 1
    for k, v in (("Diferencia por semilla", "D_j = X(Ek, j) − X(E0, j),  j = 1..n"),
                 ("Media de las diferencias", "D̄ = (1/n) · Σ D_j"),
                 ("Desvío de las diferencias", "s_D = √[ Σ (D_j − D̄)² / (n − 1) ]"),
                 ("Estadístico", "t = D̄ / (s_D / √n), con n − 1 grados de libertad"),
                 ("t crítico", "t_{n−1; 1−α/2} = T.INV.2T(α; n − 1)  (INV.T.2C en Excel en castellano)"),
                 ("Intervalo de confianza", "IC = D̄ ± t_{n−1; 1−α/2} · s_D / √n"),
                 ("Decisión", "\"sí\" (diferencia significativa) si el IC no contiene al 0; \"no\" si lo contiene"),
                 ("Signo", "D > 0: la alternativa aumenta la medida. En costos, espera y cola, D < 0 es mejora")):
        celda(ws, r, 1, k, negrita=True)
        celda(ws, r, 2, v)
        r += 1
    r += 1
    ws.cell(r, 1, "Las celdas calculadas son fórmulas: Excel y LibreOffice las calculan al abrir el archivo. "
                  "Mismas medidas y fórmulas que modelo/analizar_corridas.py.").font = F_NOTA
    anchos(ws, [34, 18, 16, 16, 16, 16, 16])
    return a_ref, k_ref


# ---------------------------------------------------------------- verificación
def verificar(path_xlsx, por, esc, sem, tests, r0_costos):
    try:
        import formulas
    except ImportError:
        sys.exit("--verificar necesita la librería formulas: .venv/Scripts/python.exe -m pip install formulas")
    sol = formulas.ExcelModel().loads(str(path_xlsx)).finish().calculate()
    val = {}
    for k, v in sol.items():
        if "!" in k:
            hoja, c = k.rsplit("!", 1)
            val[(hoja.split("]", 1)[1].strip("'").upper(), c.upper())] = v.value[0, 0] if hasattr(v, "value") else v

    def get(hoja, c):
        return val[(hoja.upper(), c)]

    peor, malas = 0.0, 0
    for e in esc[1:]:
        hoja, filas = tests[e]
        for col, nom, grupo in TEST:
            alfa = ALFA / K_PRIMARIAS if grupo == "Primaria" else ALFA
            f = ac.DERIVADAS.get(col, lambda x, c=col: float(x[c]))
            x0 = [f(por[("E0", s)]) for s in sem]
            xk = [f(por[(e, s)]) for s in sem]
            m, sd, lo, hi = ac.intervalo([b - a for a, b in zip(x0, xk)], alfa)
            sig = "sí" if (lo > 0 or hi < 0) else "no"
            r = filas[col]
            esperado = {"F": statistics.fmean(x0), "G": statistics.fmean(xk), "H": m, "I": sd,
                        "J": ac.t_cuantil(alfa, len(sem) - 1), "L": lo, "M": hi}
            for c, x in esperado.items():
                y = float(get(hoja, f"{c}{r}"))
                err = abs(y - x) / max(abs(x), 1e-12)
                peor = max(peor, err)
                if err > 1e-9:
                    malas += 1
                    print(f"DIFERENCIA {hoja} {c}{r} ({nom}): planilla {y!r} vs analizar_corridas {x!r}")
            if get(hoja, f"N{r}") != sig:
                malas += 1
                print(f"DIFERENCIA {hoja} N{r} ({nom}): {get(hoja, f'N{r}')} vs {sig}")
    for i, e in enumerate(esc):
        tot = statistics.fmean(float(por[(e, s)]["costoTotal"]) for s in sem) / 1e6
        y = float(get("Costos", f"F{r0_costos + i}"))
        if abs(y - tot) > 1e-9 * abs(tot):
            malas += 1
            print(f"DIFERENCIA Costos F{r0_costos + i}: {y} vs {tot}")
    if malas:
        sys.exit(f"{malas} celdas no coinciden con analizar_corridas.py")
    print(f"VERIFICADO: {len(esc) - 1} tests × {len(TEST)} medidas (medias, D̄, s_D, t, IC, ¿≠0?) y costos coinciden "
          f"con analizar_corridas.py (error relativo máximo {peor:.1e})")


# ---------------------------------------------------------------- main
def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    arch = elegir_csv(args)
    por, esc, sem = ac.leer(arch)
    columnas = list(next(iter(por.values())).keys())
    print(f"{arch.name}: escenarios {', '.join(esc)}; n = {len(sem)} por escenario")

    wb = Workbook()
    leame = wb.active
    letra, fila_de = hoja_corridas(wb, por, esc, sem, columnas)
    hoja_resumen(wb, letra, fila_de, esc, sem)
    a_ref, k_ref = hoja_leame(leame, arch, por, esc, sem, columnas, [f"Test {e}-E0" for e in esc[1:]])
    tests = {e: hoja_test(wb, letra, fila_de, e, sem, (a_ref, k_ref)) for e in esc[1:]}
    r0 = hoja_costos(wb, letra, fila_de, esc, sem, tests)
    for ws in wb.worksheets:
        ws.sheet_view.zoomScale = 100
    wb.save(SALIDA)
    print(f"escrita {SALIDA}")
    if "--verificar" in sys.argv:
        verificar(SALIDA, por, esc, sem, tests, r0)


if __name__ == "__main__":
    main()
