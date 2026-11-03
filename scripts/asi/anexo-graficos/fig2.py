# -*- coding: utf-8 -*-
"""Figura 2.a - Gantt del cronograma aplanado.  Figura 2.b - Histograma de recursos."""
from data import ACT, FASES
from sched import D, START, FIN, HOLG_REM as HOLG, CRIT, FINPROY, PERFILES, PERFIL_NOMBRE, carga

X0, XT = 66, 432          # margen izquierdo y comienzo del eje de tiempo
PPD = 6.55                # pixeles por dia habil
Y0, RH = 152, 17.6        # tope de la primera barra y alto de fila

NAC = {a[0]: a[9] for a in ACT}
FILAS = [a[0] for a in ACT]
ROW = {k: i for i, k in enumerate(FILAS)}

def dx(d): return XT + d * PPD
def ry(k): return Y0 + ROW[k] * RH
def fase_de(k): return k.split(".")[0]
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def r(v): return round(v, 1)

# dotacion adoptada por perfil (refuerzo en EI y QA, punto 10)
DOT = {p: (2 if p in ("EI", "QA") else 1) for p in PERFILES}
DEDIC = {"AF": 58, "CP": 78, "RO": 49, "EI": 22, "JP": 27,
         "ES": 41, "QA": 18, "CA": 42, "UX": 28}

MDASH = "&#8212;"
MIDDOT = "&#183;"
NDASH = "–"


def eje(y_base, y_tope, con_meses=True):
    """Retícula vertical de dias habiles entre y_tope y y_base."""
    o = []
    for d in range(0, FINPROY + 1, 5):
        maj = (d % 21 == 0)
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"/>'
                 % (r(dx(d)), r(y_tope), r(dx(d)), r(y_base),
                    "#C9D6E4" if maj else "#EDF2F7", 0.8 if maj else 0.5))
    for d in range(0, FINPROY + 1, 21):
        o.append('<text class="ejed" x="%s" y="%s">d%d</text>' % (r(dx(d)), r(y_tope - 7), d))
        if con_meses and d > 0:
            o.append('<text class="ejem" x="%s" y="%s">mes %d</text>'
                     % (r(dx(d) - 10.5 * PPD), r(y_tope - 20), d // 21))
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#15406B" stroke-width="1"/>'
             % (r(dx(0)), r(y_tope), r(dx(FINPROY)), r(y_tope)))
    return "".join(o)


def svg_gantt():
    o = ['<text class="figtit" x="66" y="46">Figura 2.a ' + MDASH +
         ' Diagrama de Gantt del cronograma aplanado adoptado</text>',
         '<text class="figsub" x="66" y="70">Programacion con refuerzo de un integrador y un tester '
         '(estrategia b del punto 10). Duracion adoptada: 192 dias habiles, aproximadamente 9,1 meses '
         'de 21 dias habiles, contados desde la aprobacion del Acta de Proyecto (dia 0).</text>']
    ybot = Y0 + len(FILAS) * RH
    o.append(eje(ybot, Y0 - 4))

    # franjas por fase
    for f, nom in FASES:
        ks = [k for k in FILAS if fase_de(k) == f]
        y1, y2 = ry(ks[0]) - 2, ry(ks[-1]) + RH - 2
        o.append('<rect x="%s" y="%s" width="15" height="%s" fill="#DCE9F7" stroke="#FFFFFF" stroke-width="0.8"/>'
                 % (X0, r(y1), r(y2 - y1)))
        o.append('<text class="fasenum" x="%s" y="%s">%s</text>' % (X0 + 7.5, r((y1 + y2) / 2 + 3.2), f))
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#C9D6E4" stroke-width="0.8"/>'
                 % (X0, r(y1), r(dx(FINPROY)), r(y1)))

    # filas de actividad
    for k in FILAS:
        y = ry(k)
        crit = k in CRIT
        if ROW[k] % 2 == 1:
            o.append('<rect x="%s" y="%s" width="%s" height="%s" fill="#F7FAFD"/>'
                     % (X0 + 38, r(y - 2), r(dx(FINPROY) - X0 - 38), RH))
        o.append('<text class="gid" x="%s" y="%s" font-weight="%d">%s</text>'
                 % (X0 + 42, r(y + 9.6), 700 if crit else 400, k))
        o.append('<text class="gnom" x="%s" y="%s">%s</text>' % (X0 + 76, r(y + 9.6), esc(NAC[k])))
        x1 = dx(START[k])
        w = max(D[k][2] * PPD, 2.5)
        fill, stro = ("#C0392B", "#8E2A20") if crit else ("#3D77B0", "#25547F")
        o.append('<rect x="%s" y="%s" width="%s" height="10" rx="1.6" fill="%s" stroke="%s" stroke-width="0.5"/>'
                 % (r(x1), r(y + 1.8), r(w), fill, stro))
        if HOLG[k] > 0:
            o.append('<rect x="%s" y="%s" width="%s" height="10" rx="1.6" fill="none" '
                     'stroke="#7FA3C6" stroke-width="0.9" stroke-dasharray="3 2.2"/>'
                     % (r(x1 + w), r(y + 1.8), r(HOLG[k] * PPD)))
        etq = "%dd" % D[k][2] + ((" " + MIDDOT + " h%d" % HOLG[k]) if HOLG[k] > 0 else "")
        xe = x1 + w + (HOLG[k] * PPD if HOLG[k] > 0 else 0) + 5
        o.append('<text class="gdur" x="%s" y="%s">%s</text>' % (r(xe), r(y + 10), etq))

    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#15406B" stroke-width="1"/>'
             % (X0, r(ybot - 2), r(dx(FINPROY)), r(ybot - 2)))

    # hitos de control
    for d, t in ((58, "Contrato firmado"), (122, "Inicio del piloto"),
                 (169, "Ola 3 en produccion"), (192, "Cierre del proyecto")):
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#C8901F" stroke-width="0.9" stroke-dasharray="5 3"/>'
                 % (r(dx(d)), Y0 - 4, r(dx(d)), r(ybot + 4)))
        o.append('<text class="hito" transform="translate(%s,%s) rotate(90)">%s (d%d)</text>'
                 % (r(dx(d) + 3.5), r(ybot + 8), esc(t), d))

    # referencias
    ly = ybot + 132
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#C9D6E4" stroke-width="0.8"/>'
             % (X0, r(ly - 20), r(dx(FINPROY)), r(ly - 20)))
    o.append('<text class="legtit" x="%s" y="%s">REFERENCIAS</text>' % (X0, ly))
    o.append('<rect x="%s" y="%s" width="46" height="10" rx="1.6" fill="#C0392B" stroke="#8E2A20" stroke-width="0.5"/>' % (X0 + 120, ly - 9))
    o.append('<text class="legtxt" x="%s" y="%s">Actividad del camino critico: 30 actividades con holgura total nula.</text>' % (X0 + 176, ly))
    o.append('<rect x="%s" y="%s" width="46" height="10" rx="1.6" fill="#3D77B0" stroke="#25547F" stroke-width="0.5"/>' % (X0 + 620, ly - 9))
    o.append('<text class="legtxt" x="%s" y="%s">Actividad no critica: 20 actividades.</text>' % (X0 + 676, ly))
    o.append('<rect x="%s" y="%s" width="46" height="10" rx="1.6" fill="none" stroke="#7FA3C6" stroke-width="0.9" stroke-dasharray="3 2.2"/>' % (X0 + 960, ly - 9))
    o.append('<text class="legtxt" x="%s" y="%s">Holgura remanente: holgura total del CPM menos el corrimiento aplicado en el aplanamiento.</text>' % (X0 + 1016, ly))
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#C8901F" stroke-width="0.9" stroke-dasharray="5 3"/>'
             % (X0 + 120, ly + 13, X0 + 166, ly + 13))
    o.append('<text class="legtxt" x="%s" y="%s">Hito de control. La escala superior marca los meses de 21 dias habiles.</text>' % (X0 + 176, ly + 17))
    o.append(('<text class="legtxt" x="%s" y="%s">La etiqueta al pie de cada barra indica duracion y, cuando existe, holgura: '
              '<tspan class="legb">8d ' + MIDDOT + ' h9</tspan>.</text>') % (X0 + 620, ly + 17))
    clave = "  ".join("%s %s" % (f, nom) for f, nom in FASES)
    o.append('<text class="legtxt" x="%s" y="%s"><tspan class="legb">FASES</tspan>   %s</text>' % (X0, ly + 40, esc(clave)))
    o.append('<text class="legnota" x="%s" y="%s">El histograma de recursos por perfil se presenta en la hoja siguiente, figura 2.b, '
             'sobre el mismo eje de tiempo y a la misma escala.</text>' % (X0, ly + 62))
    return "\n".join(o)


def svg_histo():
    o = ['<text class="figtit" x="66" y="46">Figura 2.b ' + MDASH + ' Histograma de recursos por perfil</text>',
         '<text class="figsub" x="66" y="70">Personas requeridas de cada perfil en cada dia habil del cronograma aplanado. '
         'Mismo eje de tiempo y misma escala que la figura 2.a. La linea de puntos marca la dotacion asignada al perfil: '
         'una persona, salvo en integraciones y pruebas, reforzados con una segunda persona de dedicacion parcial.</text>']
    CH, GAP, top = 92, 16, 150
    for i, p in enumerate(PERFILES):
        y = top + i * (CH + GAP)
        base = y + CH
        alto = CH - 46
        v = carga(p)
        def ey(n, base=base, alto=alto): return base - (n / 2.0) * alto
        o.append(eje(base, y + 46, con_meses=(i == 0)))
        o.append('<text class="hpsigla" x="%s" y="%s">%s</text>' % (X0, r(y + 14), p))
        o.append('<text class="hpnom" x="%s" y="%s">%s</text>' % (X0 + 36, r(y + 14), esc(PERFIL_NOMBRE[p])))
        ini = min(d for d in range(FINPROY) if v[d])
        fin = max(d for d in range(FINPROY) if v[d]) + 1
        o.append('<text class="hpdat" x="%s" y="%s">%d persona%s %s %d dias-persona %s %d h %s ventana d%d%sd%d %s ded. media %d%%</text>'
                 % (r(dx(FINPROY)), r(y + 14), DOT[p], "s" if DOT[p] > 1 else "", MIDDOT,
                    sum(v), MIDDOT, sum(v) * 8, MIDDOT, ini, NDASH, fin, MIDDOT, DEDIC[p]))
        for n in (1, 2):
            o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#EDF2F7" stroke-width="0.6"/>'
                     % (r(dx(0)), r(ey(n)), r(dx(FINPROY)), r(ey(n))))
            o.append('<text class="hpesc" x="%s" y="%s">%d</text>' % (r(dx(0) - 6), r(ey(n) + 3.2), n))
        d = 0
        while d < FINPROY:
            e = d
            while e < FINPROY and v[e] == v[d]:
                e += 1
            if v[d]:
                col = "#C0392B" if v[d] > DOT[p] else ("#3D77B0" if v[d] == 1 else "#7FA3C6")
                o.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="#FFFFFF" stroke-width="0.3"/>'
                         % (r(dx(d)), r(ey(v[d])), r((e - d) * PPD), r(base - ey(v[d])), col))
            d = e
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#C8901F" stroke-width="1" stroke-dasharray="4 3"/>'
                 % (r(dx(0)), r(ey(DOT[p])), r(dx(FINPROY)), r(ey(DOT[p]))))
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#15406B" stroke-width="0.9"/>'
                 % (r(dx(0)), r(base), r(dx(FINPROY)), r(base)))

    ly = top + 9 * (CH + GAP) + 40
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#C9D6E4" stroke-width="0.8"/>'
             % (X0, r(ly - 20), r(dx(FINPROY)), r(ly - 20)))
    o.append('<text class="legtit" x="%s" y="%s">REFERENCIAS</text>' % (X0, ly))
    o.append('<rect x="%s" y="%s" width="30" height="11" fill="#3D77B0"/>' % (X0 + 120, ly - 10))
    o.append('<text class="legtxt" x="%s" y="%s">Una persona del perfil requerida ese dia habil.</text>' % (X0 + 160, ly))
    o.append('<rect x="%s" y="%s" width="30" height="11" fill="#7FA3C6"/>' % (X0 + 490, ly - 10))
    o.append('<text class="legtxt" x="%s" y="%s">Dos personas requeridas: son las ventanas que motivaron el refuerzo de EI y QA.</text>' % (X0 + 530, ly))
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#C8901F" stroke-width="1" stroke-dasharray="4 3"/>'
             % (X0 + 1020, ly - 5, X0 + 1050, ly - 5))
    o.append('<text class="legtxt" x="%s" y="%s">Dotacion asignada. No se supera en ningun dia.</text>' % (X0 + 1060, ly))
    o.append('<text class="legnota" x="%s" y="%s">Esfuerzo total: 530 dias-persona, equivalentes a 4.240 horas-persona sobre jornada de ocho horas, '
             'con once personas distribuidas en nueve perfiles. Los valores coinciden con la tabla de carga por perfil del punto 10 del documento.</text>'
             % (X0, ly + 26))
    return "\n".join(o)
