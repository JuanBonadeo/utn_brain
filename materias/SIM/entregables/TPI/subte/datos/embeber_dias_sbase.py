#!/usr/bin/env python3
"""Embebe en el modelo los perfiles por día de SBASE (bootstrap de días reales, diaSbasePed = -2).

Lee datos/sbase_dias_ventanas.csv (una fila por día hábil depurado mar-jun 2026, vestíbulo Principal, diez
ventanas de 15 min de 07:00 a 09:15; lo genera scripts/sim/sbase-perfil.py --exportar-dias) y reemplaza el
valor inicial de las variables perfilesDiasPed (double[][]) y fechasDiasPed (String[]) de MainPeatonal.
Se embebe en vez de leerse en tiempo de corrida para que el modelo funcione igual en AnyLogic Cloud.

Uso (desde esta carpeta, con AnyLogic cerrado):
    python3 embeber_dias_sbase.py [archivo.alp]
"""
import csv, re, statistics, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ALP = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else AQUI.parent / 'SubteConstitucion.alp'
CSV = AQUI / 'sbase_dias_ventanas.csv'
VENTANAS = ['v0700', 'v0715', 'v0730', 'v0745', 'v0800', 'v0815', 'v0830', 'v0845', 'v0900', 'v0915']


def leer():
    filas = list(csv.DictReader(open(CSV, encoding='utf-8'), delimiter=';'))
    if not filas:
        sys.exit(f'{CSV.name} vacío')
    fechas = [f['fecha'] for f in filas]
    perfiles = [[float(f[v]) for v in VENTANAS] for f in filas]
    return fechas, perfiles


def fijar(txt, nombre, codigo):
    i = txt.index('<Name><![CDATA[MainPeatonal]]></Name>')
    j = txt.index(f'<Name><![CDATA[{nombre}]]></Name>', i)
    pat = re.compile(r'(<InitialValue Class="CodeValue">\s*<Code><!\[CDATA\[).*?(\]\]></Code>)', re.S)
    m = pat.search(txt, j)
    assert m and m.start() < txt.index('</Variable>', j), nombre
    return txt[:m.start()] + m.group(1) + codigo + m.group(2) + txt[m.end():]


def main():
    fechas, perfiles = leer()
    media = [statistics.fmean(p[w] for p in perfiles) for w in range(10)]
    txt = ALP.read_text(encoding='utf-8')
    perfil_medio = re.search(r'<Name><!\[CDATA\[perfilPed15min\]\]></Name>.*?<Code><!\[CDATA\[new double\[\] \{(.*?)\}', txt, re.S)
    medio = [float(x) for x in perfil_medio.group(1).split(',')]
    # Coherencia: el promedio de los días embebidos es el perfil medio que usa diaSbasePed = -1 (±1 pax por redondeo).
    assert all(abs(a - b) <= 1 for a, b in zip(media, medio)), (media, medio)
    num = lambda v: str(int(v)) if v == int(v) else repr(v)
    txt = fijar(txt, 'perfilesDiasPed', 'new double[][] {' + ', '.join('{' + ','.join(num(v) for v in p) + '}' for p in perfiles) + '}')
    txt = fijar(txt, 'fechasDiasPed', 'new String[] {' + ','.join(f'"{f}"' for f in fechas) + '}')
    ALP.write_text(txt, encoding='utf-8')
    print(f'{len(perfiles)} días embebidos ({fechas[0]} a {fechas[-1]}); media por ventana {[round(m) for m in media]}')


if __name__ == '__main__':
    main()
