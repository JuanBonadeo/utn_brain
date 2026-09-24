#!/usr/bin/env python3
"""Extrae los arribos a Plaza Constitución (días hábiles) de los horarios oficiales del Roca.

Fuente: PDFs "nweb_frec_horario_*" de Trenes Argentinos (vigentes desde el 03/08/2026), guardados sin
modificar en datos/roca/. Requiere `pdftotext` (poppler).

Criterios:
- solo la sección "Lunes a viernes";
- trenes con número par (convención de la línea: los pares circulan hacia Pza. Constitución);
- el arribo es el último horario de la fila del tren (columna Pza. Constitución);
- se descartan filas con menos de 6 horarios (lanzaderas Bosques-Gutiérrez que no llegan a Constitución);
- un mismo tren publicado en dos PDFs se cuenta una vez y debe tener el mismo arribo.

Salida: datos/arribos_roca_constitucion_habiles.csv (tren;ramal;llegada;segundos_desde_07).

Uso: python3 extraer_arribos_roca.py [--desde 06:30] [--hasta 09:30]
"""
import argparse, csv, re, subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAMALES = {
    'la_plata': 'La Plata',
    'ezeiza': 'Ezeiza / Cañuelas',
    'glew': 'Glew / A. Korn',
    'bosques': 'Bosques / Gutiérrez',
}
HORA = re.compile(r'\b([0-2]\d):([0-5]\d)\b')
TREN = re.compile(r'(?<![\d:])(\d{4})(?![\d:])')


def ramal_de(nombre):
    for clave, etiqueta in RAMALES.items():
        if clave in nombre:
            return etiqueta
    raise ValueError(nombre)


def texto_habiles(pdf):
    txt = subprocess.run(['pdftotext', '-layout', str(pdf), '-'], check=True, capture_output=True, text=True).stdout
    lineas = txt.splitlines()
    ini = next(i for i, l in enumerate(lineas) if 'Lunes a viernes' in l)
    fin = next(i for i, l in enumerate(lineas) if i > ini and re.search(r'S[áa]bados', l))
    return lineas[ini:fin]


def trenes(lineas):
    """Asigna horarios a trenes respetando tablas lado a lado y filas partidas en varias líneas."""
    filas = {}
    bloques = []  # (columna de inicio, tren actual)
    for linea in lineas:
        marcas = [(m.start(), m.group(1)) for m in TREN.finditer(linea)]
        horas = [(m.start(), int(m.group(1)) * 60 + int(m.group(2))) for m in HORA.finditer(linea)]
        if marcas:
            bloques = sorted(marcas)
            for c, t in marcas:
                filas.setdefault(t, [])
        for c, minutos in horas:
            dueño = None
            for inicio, t in bloques:
                if inicio <= c:
                    dueño = t
            if dueño is not None:
                filas[dueño].append(minutos)
    return filas


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--desde', default='06:30', help='incluye trenes previos cuyo pasaje llega al vestíbulo después de las 07:00')
    ap.add_argument('--hasta', default='09:30')
    args = ap.parse_args(argv)
    h0 = int(args.desde[:2]) * 60 + int(args.desde[3:])
    h1 = int(args.hasta[:2]) * 60 + int(args.hasta[3:])
    arribos = {}
    # El PDF de Bosques repite trenes de La Plata en tablas laterales: se procesa al final para que cada
    # tren conserve el ramal de su propio horario.
    pdfs = sorted((AQUI / 'roca').glob('nweb_frec_horario_*.pdf'), key=lambda p: ('bosques' in p.name, p.name))
    for pdf in pdfs:
        for tren, horas in trenes(texto_habiles(pdf)).items():
            if int(tren) % 2 or len(horas) < 6:
                continue
            # Trenes que cruzan la medianoche: se suma un día a los horarios posteriores.
            horas = [h + 1440 * any(x - y > 600 for x, y in zip(horas[:i], horas[1:i + 1])) for i, h in enumerate(horas)]
            if any(b < a for a, b in zip(horas, horas[1:])):
                raise SystemExit(f'{pdf.name}: horarios no crecientes en el tren {tren}: {horas}')
            llegada = horas[-1]
            if tren in arribos and arribos[tren][1] != llegada:
                raise SystemExit(f'tren {tren}: arribo distinto entre PDFs ({arribos[tren][1]} vs {llegada})')
            ramal = ramal_de(pdf.name)
            if ramal == 'La Plata' and tren.startswith('2'):
                ramal = 'Bosques (vía Quilmes)'
            elif ramal.startswith('Bosques') and tren.startswith('1'):
                ramal = 'Bosques (vía Temperley)'
            arribos.setdefault(tren, (ramal, llegada))
    elegidos = sorted((ll, tren, ramal) for tren, (ramal, ll) in arribos.items() if h0 <= ll < h1)
    salida = AQUI / 'arribos_roca_constitucion_habiles.csv'
    with salida.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(['tren', 'ramal', 'llegada', 'segundos_desde_07'])
        for ll, tren, ramal in elegidos:
            w.writerow([tren, ramal, f'{ll // 60:02d}:{ll % 60:02d}', (ll - 7 * 60) * 60])
    print(f'{len(elegidos)} arribos entre {args.desde} y {args.hasta} -> {salida.name}')
    for ramal in sorted(set(r for _, _, r in elegidos)):
        print(f'  {ramal}: {sum(1 for *_, r in elegidos if r == ramal)}')


if __name__ == '__main__':
    main()
