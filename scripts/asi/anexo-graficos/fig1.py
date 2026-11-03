# -*- coding: utf-8 -*-
"""Figura 1 - Diagrama de Red (actividad en el nodo), en dos bandas."""
from data import ACT
D = {a[0]: a for a in ACT}

# (banda, columna dentro de la banda, fila)  -- columnas = nivel topologico
POS = {
 "1.1":(0,0,1), "1.2":(0,1,1), "1.3":(0,2,1), "2.1":(0,3,1),
 "2.4":(0,4,0), "2.2":(0,4,1), "2.3":(0,4,2), "2.5":(0,4,3),
 "2.6":(0,5,1), "3.1":(0,6,1), "7.1":(0,6,3), "3.2":(0,7,1),
 "3.3":(0,8,1), "3.4":(0,9,1), "3.5":(0,10,1),
 "4.5":(0,11,0), "4.1":(0,11,1), "5.5":(0,11,2), "4.4":(0,11,3),
 "4.2":(0,12,0), "5.1":(0,12,1), "5.6":(0,12,2), "6.2":(0,12,3),
 "4.3":(0,13,0), "5.2":(0,13,1), "4.7":(0,13,2), "7.5":(0,13,3),
 "4.6":(0,14,0), "5.3":(0,14,1),
 "7.2":(1,0,0), "5.4":(1,0,1), "6.1":(1,0,2),
 "9.1":(1,1,0), "7.3":(1,1,1), "7.4":(1,2,1), "7.6":(1,3,1),
 "8.1":(1,4,1), "8.2":(1,5,1), "8.3":(1,6,1), "8.4":(1,7,1),
 "9.2":(1,8,1), "9.3":(1,9,0), "10.1":(1,9,1),
 "9.4":(1,10,0), "10.2":(1,10,1), "10.3":(1,11,1),
 "11.2":(1,12,0), "11.1":(1,12,1), "11.3":(1,13,1), "11.4":(1,14,1),
}

NW, NH = 88, 58
COL, ROWP = 108, 92
BX = 66                      # margen izquierdo de las bandas
BY = [126, 604]              # y del tope de la fila 0 de cada banda

def nx(k): return BX + POS[k][1] * COL
def ny(k): return BY[POS[k][0]] + POS[k][2] * ROWP
def cx(k): return nx(k) + NW / 2
def cy(k): return ny(k) + NH / 2

CRIT = {k for k in D if D[k][7] == 0}
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def nodo(k):
    _, _, dur, es, ef, ls, lf, ht, _, _ = D[k]
    x, y = nx(k), ny(k)
    c = k in CRIT
    fill, stroke = ("#FDECE9", "#B23A2E") if c else ("#F2F7FC", "#15406B")
    band = "#B23A2E" if c else "#DCE9F7"
    tcol = "#FFFFFF" if c else "#15406B"
    w3 = NW / 3
    o = [f'<g class="nodo">',
         f'<rect x="{x}" y="{y}" width="{NW}" height="{NH}" rx="3" fill="{fill}" stroke="{stroke}" stroke-width="{1.6 if c else 1}"/>',
         f'<rect x="{x}" y="{y+17}" width="{NW}" height="24" fill="{band}"/>',
         f'<line x1="{x}" y1="{y+17}" x2="{x+NW}" y2="{y+17}" stroke="{stroke}" stroke-width="0.7"/>',
         f'<line x1="{x}" y1="{y+41}" x2="{x+NW}" y2="{y+41}" stroke="{stroke}" stroke-width="0.7"/>']
    for i in (1, 2):
        o.append(f'<line x1="{x+w3*i}" y1="{y}" x2="{x+w3*i}" y2="{y+17}" stroke="{stroke}" stroke-width="0.5"/>')
        o.append(f'<line x1="{x+w3*i}" y1="{y+41}" x2="{x+w3*i}" y2="{y+NH}" stroke="{stroke}" stroke-width="0.5"/>')
    for i, v in enumerate((es, dur, ef)):
        o.append(f'<text class="num" x="{x+w3*(i+0.5)}" y="{y+12.4}">{v}</text>')
    for i, v in enumerate((ls, ht, lf)):
        o.append(f'<text class="num" x="{x+w3*(i+0.5)}" y="{y+53.4}">{v}</text>')
    o.append(f'<text class="idn" x="{x+NW/2}" y="{y+33.6}" fill="{tcol}">{k}</text>')
    o.append('</g>')
    return "".join(o)

def flecha(pts, crit):
    col = "#B23A2E" if crit else "#5B7FA6"
    w = 1.5 if crit else 1.0
    d = " ".join(f"{round(x,1)},{round(y,1)}" for x, y in pts)
    m = "url(#ahC)" if crit else "url(#ah)"
    return f'<polyline points="{d}" fill="none" stroke="{col}" stroke-width="{w}" marker-end="{m}"/>'

# ---- ruteo -------------------------------------------------------------
ocupada = {(POS[k][0], POS[k][1], POS[k][2]) for k in POS}
# rutas por carril, resueltas a mano (unicos 4 tramos bloqueados por nodos intermedios)
CARRIL = {("4.5", "4.6"): -1, ("7.1", "7.5"): +1, ("7.2", "7.6"): -1, ("9.4", "11.3"): -1}

def ruta(u, v):
    """Polilinea ortogonal de u a v dentro de una misma banda."""
    x1, y1 = nx(u) + NW, cy(u)
    x2, y2 = nx(v), cy(v)
    key = (u, v)
    if key in CARRIL:
        s = CARRIL[key]
        fila = POS[u][2]
        ly = (BY[POS[u][0]] + fila * ROWP - 14) if s < 0 else (BY[POS[u][0]] + fila * ROWP + NH + 14)
        return [(x1, y1), (x1 + 10, y1), (x1 + 10, ly), (x2 - 14, ly), (x2 - 14, y2), (x2, y2)]
    if abs(y1 - y2) < 0.5:
        return [(x1, y1), (x2, y2)]
    return [(x1, y1), (x2 - 14, y1), (x2 - 14, y2), (x2, y2)]

# ---- etiquetas de cruce entre bandas -----------------------------------
SALE, ENTRA = {}, {}
for a in ACT:
    for p in a[1]:
        if POS[p][0] != POS[a[0]][0]:
            SALE.setdefault(p, []).append(a[0])
            ENTRA.setdefault(a[0], []).append(p)

def etiqueta(k, texto, arriba):
    x = nx(k) + (NW if not arriba else 0)
    y = ny(k) + (NH + 11 if not arriba else -5)
    w = 11 + 5.4 * len(texto)
    tx = x - w if not arriba else x
    return (f'<g><rect x="{round(tx,1)}" y="{round(y-9,1)}" width="{round(w,1)}" height="12.5" rx="6.2" '
            f'fill="#FFF3D6" stroke="#C8901F" stroke-width="0.7"/>'
            f'<text class="cruce" x="{round(tx+w/2,1)}" y="{round(y,1)}">{esc(texto)}</text></g>')

def svg():
    o = []
    o.append('<text class="figtit" x="66" y="46">Figura 1 &#8212; Diagrama de Red del proyecto (actividad en el nodo)</text>')
    o.append('<text class="figsub" x="66" y="70">Metodo del camino critico sobre la EDT del punto 4.3. Fechas tempranas y tardias en dias habiles contados desde el dia 0 '
             '(aprobacion del Acta de Proyecto). Disponibilidad de recursos ilimitada. Duracion: 187 dias habiles; 30 actividades criticas.</text>')
    for b, (t, sub) in enumerate([("BANDA A", "actividades 1.1 a 5.3 &#183; dias 0 a 97"),
                                  ("BANDA B", "actividades 5.4 a 11.4 &#183; dias 92 a 187")]):
        y = BY[b] - 30
        o.append(f'<text class="bandtit" x="66" y="{y}">{t}</text>')
        o.append(f'<text class="bandsub" x="{66+64}" y="{y}">{sub}</text>')
        o.append(f'<line x1="66" y1="{y+8}" x2="1690" y2="{y+8}" stroke="#C9D6E4" stroke-width="0.8"/>')
    for a in ACT:
        for p in a[1]:
            if POS[p][0] == POS[a[0]][0]:
                o.append(flecha(ruta(p, a[0]), p in CRIT and a[0] in CRIT))
    for k in SALE:
        o.append(etiqueta(k, "\u25b6 " + " \u00b7 ".join(SALE[k]), False))
    for k in ENTRA:
        o.append(etiqueta(k, " \u00b7 ".join(ENTRA[k]) + " \u25c0", True))
    for k in POS:
        o.append(nodo(k))
    return "\n".join(o)

# ---- referencia (simbologia del nodo) ----------------------------------
def leyenda():
    X, Y = 66, 900
    o = [f'<line x1="66" y1="{Y-16}" x2="1690" y2="{Y-16}" stroke="#C9D6E4" stroke-width="0.8"/>',
         f'<text class="legtit" x="{X}" y="{Y+4}">REFERENCIAS</text>']
    # nodo modelo, al doble de escala
    x, y, w, h = X + 130, Y - 6, 176, 116
    w3 = w / 3
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#F2F7FC" stroke="#15406B"/>')
    o.append(f'<rect x="{x}" y="{y+34}" width="{w}" height="48" fill="#DCE9F7"/>')
    for yy in (y+34, y+82):
        o.append(f'<line x1="{x}" y1="{yy}" x2="{x+w}" y2="{yy}" stroke="#15406B" stroke-width="0.7"/>')
    for i in (1, 2):
        o.append(f'<line x1="{x+w3*i}" y1="{y}" x2="{x+w3*i}" y2="{y+34}" stroke="#15406B" stroke-width="0.5"/>')
        o.append(f'<line x1="{x+w3*i}" y1="{y+82}" x2="{x+w3*i}" y2="{y+h}" stroke="#15406B" stroke-width="0.5"/>')
    for i, t in enumerate(("ES", "D", "EF")):
        o.append(f'<text class="legcell" x="{x+w3*(i+0.5)}" y="{y+23}">{t}</text>')
    for i, t in enumerate(("LS", "HT", "LF")):
        o.append(f'<text class="legcell" x="{x+w3*(i+0.5)}" y="{y+105}">{t}</text>')
    o.append(f'<text class="legid" x="{x+w/2}" y="{y+64}">ID</text>')
    txt = [("ES", "inicio temprano"), ("D", "duracion en dias habiles"), ("EF", "fin temprano"),
           ("LS", "inicio tardio"), ("HT", "holgura total"), ("LF", "fin tardio")]
    for i, (a, b) in enumerate(txt):
        o.append(f'<text class="legtxt" x="{x+w+24}" y="{y+16+i*19}"><tspan class="legb">{a}</tspan>  {b}</text>')
    # muestras de color
    mx = x + w + 250
    o.append(f'<rect x="{mx}" y="{y+4}" width="34" height="16" rx="2" fill="#FDECE9" stroke="#B23A2E" stroke-width="1.6"/>')
    o.append(f'<text class="legtxt" x="{mx+44}" y="{y+16}">Actividad critica (HT = 0). Son 30 y su encadenamiento define los 187 dias.</text>')
    o.append(f'<rect x="{mx}" y="{y+30}" width="34" height="16" rx="2" fill="#F2F7FC" stroke="#15406B"/>')
    o.append(f'<text class="legtxt" x="{mx+44}" y="{y+42}">Actividad con holgura (HT &gt; 0). Son 20.</text>')
    o.append(f'<line x1="{mx}" y1="{y+64}" x2="{mx+34}" y2="{y+64}" stroke="#B23A2E" stroke-width="1.5" marker-end="url(#ahC)"/>')
    o.append(f'<text class="legtxt" x="{mx+44}" y="{y+68}">Precedencia fin a comienzo entre actividades criticas. No consume tiempo.</text>')
    o.append(f'<line x1="{mx}" y1="{y+88}" x2="{mx+34}" y2="{y+88}" stroke="#5B7FA6" stroke-width="1" marker-end="url(#ah)"/>')
    o.append(f'<text class="legtxt" x="{mx+44}" y="{y+92}">Precedencia fin a comienzo con holgura.</text>')
    o.append(f'<g><rect x="{mx}" y="{y+106}" width="52" height="12.5" rx="6.2" fill="#FFF3D6" stroke="#C8901F" stroke-width="0.7"/>'
             f'<text class="cruce" x="{mx+26}" y="{y+115}">\u25b6 5.4</text></g>')
    o.append(f'<text class="legtxt" x="{mx+64}" y="{y+115}">Relacion que cruza de una banda a la otra: \u25b6 sale hacia, \u25c0 viene de.</text>')
    o.append(f'<text class="legnota" x="{X}" y="{Y+132}">Las denominaciones completas de cada paquete estan en la tabla de la EDT del punto 4.3 del documento.</text>')
    return "\n".join(o)
