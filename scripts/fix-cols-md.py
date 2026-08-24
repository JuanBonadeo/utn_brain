# -*- coding: utf-8 -*-
"""Audita y recalcula los anchos de columna de las tablas de un .md.

Dos fuerzas distintas gobiernan el ancho de una columna:

  - el VOLUMEN de texto, que determina cuanto conviene darle para que no se
    parta en demasiadas lineas. Se mide con un percentil alto del largo de
    celda, no con el maximo, para que un solo outlier no distorsione.
  - el ANCHO MINIMO PRACTICABLE, que sale de lo mas largo que la columna no
    puede partir: la palabra mas larga, y ademas la celda mas larga cuando la
    columna es corta en terminos absolutos.

El reparto va por volumen, pero respetando ese piso por columna. Sin el, las
columnas de identificadores quedan impracticables: "4.6, 4.7, 7.1" se apila en
tres renglones porque el reparto por volumen la ve como una columna de tres
caracteres.
"""
import io, re, sys, math

CHARS_ANCHO = 95     # caracteres que entran a lo ancho del area util, a 9 pt
MARGEN_PCT = 2.6     # margenes internos de celda, en % del ancho util
P = 0.85

def tope(n):
    """Ancho maximo de una columna segun cuantas tenga la tabla. Una tabla de
    tres columnas puede darle 60% a la de prosa sin que se vea mal; una de seis
    no, porque deja a las otras cinco en nada."""
    return {2: 75, 3: 60, 4: 50, 5: 44}.get(n, 38)


def celdas(linea):
    s = linea.strip()
    if s.startswith('|'): s = s[1:]
    if s.endswith('|'): s = s[:-1]
    return [c.strip() for c in s.split('|')]


def limpio(t):
    return re.sub(r'\*\*|\*|`', '', t)


def metricas(col, MAX_PCT):
    """(volumen, piso_pct) de una columna. col[0] es el encabezado."""
    cuerpo = [limpio(c) for c in col[1:]] or ['']
    largos = sorted(len(c) for c in cuerpo)
    idx = min(len(largos) - 1, int(math.ceil(P * len(largos)) - 1))
    volumen = max(largos[idx], len(limpio(col[0])) * 0.55, 3)

    # palabra mas larga que no se puede partir, encabezado incluido
    tok = 1
    for c in [limpio(x) for x in col]:
        for w in c.split():
            tok = max(tok, len(w))
    # Piso de la columna. Ademas de la palabra impartible, una columna de
    # contenido corto deberia entrar entera en su renglon: sin esto,
    # "4.6, 4.7, 7.1" se apila en tres lineas aunque sobre lugar en la tabla.
    # Se toma el MAXIMO de la columna y no un percentil, porque las celdas
    # largas suelen ser minoria (solo 3 de 50 actividades tienen tres
    # predecesoras) y un percentil no las ve. Se acota a 13 caracteres para que
    # una columna de prosa no reclame un piso enorme: ahi manda el volumen.
    ancho_util = max(tok, min(max(largos), 13))
    piso = min(MAX_PCT, ancho_util * 100.0 / CHARS_ANCHO + MARGEN_PCT)
    return volumen, piso


def reparte(cols):
    MAX_PCT = tope(len(cols))
    m = [metricas(c, MAX_PCT) for c in cols]
    vol = [x[0] for x in m]
    piso = [x[1] for x in m]
    # Si los pisos no entran en el 100%, se los escala en bloque: es preferible
    # apretar todas las columnas por igual antes que dejar el reparto sin solucion.
    sp = sum(piso)
    if sp > 95:
        piso = [x * 95.0 / sp for x in piso]
    tot = sum(vol)
    pct = [100.0 * v / tot for v in vol]

    for _ in range(80):
        pct = [max(piso[i], min(MAX_PCT, pct[i])) for i in range(len(pct))]
        exceso = sum(pct) - 100.0
        if abs(exceso) < 0.05:
            break
        # el ajuste se toma de las columnas que tienen aire sobre su piso
        libres = [i for i in range(len(pct)) if pct[i] > piso[i] + 0.5]
        if not libres:
            break
        base = sum(pct[i] - piso[i] for i in libres)
        if base <= 0: break
        for i in libres:
            pct[i] -= exceso * ((pct[i] - piso[i]) / base)

    MIN_ENT = 4
    ent = [max(MIN_ENT, int(round(v))) for v in pct]
    # Ajuste final del redondeo. Se reparte de a un punto por vez sobre las
    # columnas con mas aire sobre su piso, en vez de descargarlo todo en una:
    # volcar el resto entero en una sola columna es lo que llegaba a dejarla
    # en negativo cuando los pisos no cerraban.
    guarda = 0
    while sum(ent) != 100 and guarda < 500:
        guarda += 1
        if sum(ent) > 100:
            cand = [k for k in range(len(ent)) if ent[k] > MIN_ENT]
            if not cand: break
            ent[max(cand, key=lambda k: ent[k] - piso[k])] -= 1
        else:
            ent[min(range(len(ent)), key=lambda k: ent[k] - piso[k])] += 1
    assert sum(ent) == 100 and min(ent) >= MIN_ENT, ent
    return ent


def main(path, escribir=False):
    L = io.open(path, encoding='utf-8').read().split('\n')
    out = list(L)
    i = 0; cambios = 0; total = 0
    while i < len(L):
        if L[i].startswith('|') and i + 1 < len(L) and re.match(r'^\|[\s:|-]+\|$', L[i + 1]):
            ini = i; filas = []
            while i < len(L) and L[i].startswith('|'):
                if not re.match(r'^\|[\s:|-]+\|$', L[i]):
                    filas.append(celdas(L[i]))
                i += 1
            total += 1
            n = len(filas[0])
            filas = [f for f in filas if len(f) == n]
            nuevo = reparte(list(zip(*filas)))
            j = ini - 1; dj = None; viejo = None
            while j >= 0 and j > ini - 9:
                mm = re.match(r'^<!-- cols:\s*([-\d,\s]+?)\s*-->$', L[j].strip())
                if mm:
                    dj = j; viejo = [int(x) for x in mm.group(1).split(',') if x.strip()]
                    break
                j -= 1
            dif = max(abs(a - b) for a, b in zip(viejo, nuevo)) if (viejo and len(viejo) == len(nuevo)) else 99
            if dif >= 5:
                print('L%-5d %s' % (ini + 1, ' | '.join(filas[0])[:56]))
                print('        %s  ->  %s' % (viejo, nuevo))
                if dj is not None:
                    out[dj] = '<!-- cols: %s -->' % ','.join(map(str, nuevo))
                else:
                    out[ini] = '<!-- cols: ' + ','.join(map(str, nuevo)) + ' -->' + chr(10) + chr(10) + out[ini]
                cambios += 1
            i -= 0
            continue
        i += 1
    print('\n%d tablas, %d ajustadas' % (total, cambios))
    if escribir:
        io.open(path, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
        print('archivo reescrito')


if __name__ == '__main__':
    main(sys.argv[1], '--write' in sys.argv)
