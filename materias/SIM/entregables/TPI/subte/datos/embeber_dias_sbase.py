#!/usr/bin/env python3
"""Embebe en el modelo los días hábiles reales: perfil SBASE y llegadas reales del Roca (bootstrap, diaSbasePed = -2).

Lee datos/sbase_dias_ventanas.csv (una fila por día hábil depurado mar-jun 2026, vestíbulo Principal, diez
ventanas de 15 min de 07:00 a 09:15; lo genera scripts/sim/sbase-perfil.py --exportar-dias) y reemplaza el
valor inicial de las variables perfilesDiasPed (double[][]) y fechasDiasPed (String[]) de MainPeatonal.

También embebe las llegadas reales de cada tren a Plaza Constitución de ese mismo día (Trenes Argentinos,
NO-2026-104102701-APN-UCIYT-SOFSE: solicitudes/sofse-2026-10-26/trenes-a-pc-mar-jun-2026.xlsx, al minuto) en
llegadasDiasPed (segundos desde las 07:00, ordenadas) y ramalesDiasPed (código de ramal del modelo; 5 = Mar del
Plata, que no figura en el horario de cuadros). Se excluyen los días con el servicio del Roca interrumpido
(menos de MIN_TRENES trenes en la franja): el estudio es sobre un día hábil con servicio normal.
Se embebe en vez de leerse en tiempo de corrida para que el modelo funcione igual en AnyLogic Cloud.

Uso (desde esta carpeta, con AnyLogic cerrado):
    python3 embeber_dias_sbase.py [archivo.alp]
"""
import csv, re, statistics, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ALP = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else AQUI.parent / 'SubteConstitucion.alp'
CSV = AQUI / 'sbase_dias_ventanas.csv'
LLEGADAS = AQUI / 'solicitudes' / 'sofse-2026-10-26' / 'trenes-a-pc-mar-jun-2026.xlsx'
MIN_TRENES = 40      # ~80 % de la mediana (49 trenes por día hábil)
RAMALES = {'Constitución - La Plata': 0, 'Constitución - Bosques (Q)': 1, 'Constitución - Bosques (T)': 2,
           'Constitución - A. Korn': 3, 'Constitución - Ezeiza': 4, 'Constitución - Mar del Plata': 5}
VENTANAS = ['v0700', 'v0715', 'v0730', 'v0745', 'v0800', 'v0815', 'v0830', 'v0845', 'v0900', 'v0915']


def leer():
    filas = list(csv.DictReader(open(CSV, encoding='utf-8'), delimiter=';'))
    if not filas:
        sys.exit(f'{CSV.name} vacío')
    fechas = [f['fecha'] for f in filas]
    perfiles = [[float(f[v]) for v in VENTANAS] for f in filas]
    return fechas, perfiles


def leer_llegadas():
    import collections, openpyxl
    libro = openpyxl.load_workbook(LLEGADAS, read_only=True, data_only=True)
    dias = collections.defaultdict(list)
    for i, (tren, ramal, fecha, hora) in enumerate(libro.worksheets[0].iter_rows(values_only=True)):
        if i == 0 or fecha is None:
            continue
        hh, mm, ss = (int(x) for x in str(hora).split(':'))
        dias[fecha.date().isoformat()].append(((hh - 7) * 3600 + mm * 60 + ss, RAMALES[ramal]))
    return {d: sorted(v) for d, v in dias.items()}


def fijar(txt, nombre, codigo):
    i = txt.index('<Name><![CDATA[MainPeatonal]]></Name>')
    j = txt.index(f'<Name><![CDATA[{nombre}]]></Name>', i)
    pat = re.compile(r'(<InitialValue Class="CodeValue">\s*<Code><!\[CDATA\[).*?(\]\]></Code>)', re.S)
    m = pat.search(txt, j)
    assert m and m.start() < txt.index('</Variable>', j), nombre
    return txt[:m.start()] + m.group(1) + codigo + m.group(2) + txt[m.end():]


def main():
    fechas, perfiles = leer()
    llegadas = leer_llegadas()
    faltan = [f for f in fechas if f not in llegadas]
    assert not faltan, f'días SBASE sin llegadas reales: {faltan}'
    cortados = [(f, len(llegadas[f])) for f in fechas if len(llegadas[f]) < MIN_TRENES]
    elegidos = [k for k, f in enumerate(fechas) if len(llegadas[f]) >= MIN_TRENES]
    media_todos = [statistics.fmean(p[w] for p in perfiles) for w in range(10)]
    fechas = [fechas[k] for k in elegidos]
    perfiles = [perfiles[k] for k in elegidos]
    media = [statistics.fmean(p[w] for p in perfiles) for w in range(10)]
    txt = ALP.read_text(encoding='utf-8')
    perfil_medio = re.search(r'<Name><!\[CDATA\[perfilPed15min\]\]></Name>.*?<Code><!\[CDATA\[new double\[\] \{(.*?)\}', txt, re.S)
    medio = [float(x) for x in perfil_medio.group(1).split(',')]
    # Coherencia: el promedio de todos los días depurados es el perfil medio que usa diaSbasePed = -1 (±1 pax).
    assert all(abs(a - b) <= 1 for a, b in zip(media_todos, medio)), (media_todos, medio)
    num = lambda v: str(int(v)) if v == int(v) else repr(v)
    txt = fijar(txt, 'perfilesDiasPed', 'new double[][] {' + ', '.join('{' + ','.join(num(v) for v in p) + '}' for p in perfiles) + '}')
    txt = fijar(txt, 'fechasDiasPed', 'new String[] {' + ','.join(f'"{f}"' for f in fechas) + '}')
    txt = fijar(txt, 'llegadasDiasPed', 'new double[][] {' + ', '.join(
        '{' + ','.join(str(t) for t, _ in llegadas[f]) + '}' for f in fechas) + '}')
    txt = fijar(txt, 'ramalesDiasPed', 'new int[][] {' + ', '.join(
        '{' + ','.join(str(r) for _, r in llegadas[f]) + '}' for f in fechas) + '}')
    ALP.write_text(txt, encoding='utf-8')
    trenes = [len(llegadas[f]) for f in fechas]
    print(f'{len(perfiles)} días embebidos ({fechas[0]} a {fechas[-1]}); excluidos por servicio del Roca '
          f'interrumpido (< {MIN_TRENES} trenes): {cortados}')
    print(f'trenes por día {min(trenes)}-{max(trenes)} (media {statistics.fmean(trenes):.1f}); '
          f'perfil medio de los días embebidos {[round(m) for m in media]}')


if __name__ == '__main__':
    main()
