# -*- coding: utf-8 -*-
"""Variantes 16:9 de las cinco laminas del Anexo II, para proyectar.

Las laminas originales son A3 apaisado, con relaciones de 1,22 a 1,65 a 1. En una
diapositiva 16:9 (1,78) entran limitadas por la altura y dejan margenes laterales
de hasta el 35% del ancho: se ven chicas. Aca cada figura se recompone sobre un
lienzo de 1920x1080 nativo.

**No se saca informacion.** Lo que cambia es la disposicion:

  - El dibujo se separa de su chrome (titulo, bajada, referencias) y se escala
    para ocupar todo el lienzo disponible.
  - El chrome se recompone como columna lateral derecha o franja inferior, y se
    vuelve a tipografiar al cuerpo que corresponde a una proyeccion, no a una
    lamina A3 que se lee a un palmo. Las referencias en tira horizontal se pasan
    a lista vertical, con las mismas leyendas y las mismas muestras de color.
  - En el Gantt y el histograma, que son parametricos, se ajusta ademas el eje de
    tiempo (PPD) para que el dibujo nazca con la relacion de la caja que le toca,
    en lugar de estirarse dentro de ella. Ambos comparten PPD, porque el
    documento afirma que estan a la misma escala.
  - Los cuerpos tipograficos del dibujo se multiplican por un factor por figura
    (`escalar_css`), que es lo que de verdad mueve la legibilidad proyectada.

Los datos salen intactos de fig1..fig4: este modulo no dibuja nada propio salvo
los textos del chrome, que son los mismos de la lamina A3.
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "anexo-graficos"))

import fig1, fig2, fig3, fig4          # noqa: E402
import build as anexo                  # noqa: E402
from acentos import acentuar           # noqa: E402

W, H = 1920, 1080
AZUL, CELESTE, MUTED, ROJO, ORO = "#15406B", "#DCE9F7", "#4C6480", "#B23A2E", "#C8901F"

# ------------------------------------------------------------------ utilidades


def _lineas(svg):
    return [l for l in svg.split("\n") if l.strip()]


def parte(svg, marca_inicio=None, marca_fin=None, quitar=()):
    """Lineas del svg entre dos marcas, salteando las que contengan `quitar`."""
    ls = _lineas(svg)
    i = next((n for n, l in enumerate(ls) if marca_inicio in l), 0) if marca_inicio else 0
    j = next((n for n, l in enumerate(ls) if marca_fin in l), len(ls)) if marca_fin else len(ls)
    return [l for l in ls[i:j] if not any(q in l for q in quitar)]


def grupo(lineas, tx, ty, s):
    return ('<g transform="translate(%.2f,%.2f) scale(%.5f)">%s</g>'
            % (tx, ty, s, "".join(lineas)))


def encaje(bw, bh, cw, ch):
    return min(cw / float(bw), ch / float(bh))


def escalar_css(k):
    """La CSS del anexo con todos los cuerpos multiplicados por k."""
    css = re.sub(r"font-size:\s*([\d.]+)px",
                 lambda m: "font-size:%.2fpx" % (float(m.group(1)) * k),
                 anexo.CSS)
    css = css.split("/* ---- tipografia de las laminas ---- */")[-1]
    return ("<style>text{font-family:'Lexend','Segoe UI',Arial,Helvetica,sans-serif;fill:#15406B}"
            + css + "</style>")


def txt(x, y, s, size, color=AZUL, bold=False, anchor=None):
    a = ' text-anchor="%s"' % anchor if anchor else ""
    return ('<text x="%.1f" y="%.1f" font-size="%.1f" fill="%s" font-weight="%d"%s>%s</text>'
            % (x, y, size, color, 700 if bold else 400, a, s))


def parrafo(x, y, cuerpo, size, ancho_car, color=MUTED, interlinea=1.44, bold=False):
    """Corta el parrafo a mano: SVG no tiene motor de texto."""
    out, linea, yy = [], "", y
    for p in cuerpo.split():
        prueba = (linea + " " + p).strip()
        if len(prueba) > ancho_car and linea:
            out.append(txt(x, yy, linea, size, color, bold))
            yy += size * interlinea
            linea = p
        else:
            linea = prueba
    if linea:
        out.append(txt(x, yy, linea, size, color, bold))
        yy += size * interlinea
    return "".join(out), yy


# --------------------------------------------------------- muestras del riel

def m_rect(x, y, fill, stroke=None, dash=None, w=42, h=13):
    s = ' stroke="%s" stroke-width="1.1"' % stroke if stroke else ""
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="2" fill="%s"%s%s/>'
            % (x, y - h + 2, w, h, fill, s, d))


def m_linea(x, y, color, dash="6 4", w=42):
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"'
            ' stroke-dasharray="%s"/>' % (x, y - 4, x + w, y - 4, color, dash))


def riel(x, y, ancho_car, items, size=15.5, sangria=56):
    """Lista vertical de referencias: muestra a la izquierda, leyenda al lado."""
    o, yy = [], y
    for muestra, leyenda in items:
        if muestra:
            o.append(muestra(x, yy))
            p, yy = parrafo(x + sangria, yy, leyenda, size, ancho_car, "#2A3B4D")
        else:
            p, yy = parrafo(x, yy, leyenda, size, ancho_car + 6, MUTED)
        o.append(p)
        yy += 13
    return "".join(o), yy


def cabecera_riel(x, titulo, sub, bajada, ancho_car, y=60, sub_car=22):
    o = [txt(x, y, titulo, 29, AZUL, True)]
    p, yy = parrafo(x, y + 34, sub, 25, sub_car, AZUL, 1.22, True)
    o.append(p)
    p, yy = parrafo(x, yy + 12, bajada, 16, ancho_car, MUTED)
    o.append(p)
    return "".join(o), yy + 20


def lamina(css, cuerpo):
    return acentuar(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">'
        '<rect width="%d" height="%d" fill="#FFFFFF"/>%s%s%s</svg>'
        % (W, H, W, H, W, H, css, anexo.DEFS, cuerpo))


# =========================================================== Figura 1 · Red

def fig1_16x9():
    fig1.COL, fig1.ROWP, fig1.BY = 118, 96, [132, 566]
    dib = parte(fig1.svg(), quitar=('class="figtit"', 'class="figsub"'))
    # el rotulo de banda es mas ancho con la tipografia agrandada: corro su subtitulo
    dib = [re.sub(r'(class="bandsub" x=")(\d+)', lambda m: m.group(1) + str(int(m.group(2)) + 74), l)
           if 'class="bandsub"' in l else l for l in dib]
    leg = _lineas(fig1.leyenda())

    bx0, by0 = 66, 104
    bw = (66 + 14 * fig1.COL + fig1.NW) - bx0
    bh = (fig1.BY[1] + 2 * fig1.ROWP + fig1.NH) - by0

    TOP, LEGH = 158, 172
    s = encaje(bw, bh, W - 76, H - TOP - LEGH - 26)
    sl = encaje(1624, 148, W - 96, LEGH)

    o = [txt(46, 50, "Figura 1 — Diagrama de Red del proyecto (actividad en el nodo)", 33, AZUL, True)]
    p, _ = parrafo(46, 82, "Metodo del camino critico sobre la EDT del punto 4.3. Fechas tempranas y tardias "
                           "en dias habiles contados desde el dia 0, la aprobacion del Acta de Proyecto. "
                           "Disponibilidad de recursos ilimitada. Duracion 187 dias habiles; 30 actividades criticas.",
                   16.5, 195)
    o += [p,
          grupo(dib, (W - bw * s) / 2 - bx0 * s, TOP - by0 * s, s),
          grupo(leg, 48 - 66 * sl, H - LEGH - 2 - 884 * sl, sl)]
    return lamina(escalar_css(1.16), "".join(o))


# ============================================== Figuras 2.a y 2.b · tiempos
# Comparten PPD y XT: el documento afirma que estan a la misma escala.

PPD16, XT16 = 4.92, 502


def fig2a_16x9():
    fig2.PPD, fig2.XT, fig2.RH, fig2.Y0 = PPD16, XT16, 17.6, 158
    svg = fig2.svg_gantt()
    dib = parte(svg, marca_fin='class="legtit"',
                quitar=('class="figtit"', 'class="figsub"', 'class="hito"'))[:-1]

    ybot = fig2.Y0 + 50 * fig2.RH
    # Los hitos venian rotados 90 grados colgando del eje: en 16:9 esa columna de
    # texto no entra a lo alto. Se reponen horizontales, escalonados en dos filas.
    for d, t, fila, anchor in ((58, "Contrato firmado", 0, None),
                               (122, "Inicio del piloto", 0, None),
                               (192, "Cierre del proyecto", 0, "end"),
                               (169, "Ola 3 en produccion", 1, "middle")):
        a = ' text-anchor="%s"' % anchor if anchor else ""
        dib.append('<text class="hito" x="%.1f" y="%.1f"%s>%s (d%d)</text>'
                   % (fig2.dx(d) + (0 if anchor else 4), ybot + 26 + fila * 25, a, t, d))

    bx0, by0 = 66, 116
    bw = (fig2.XT + 192 * fig2.PPD) - bx0
    bh = (ybot + 58) - by0

    RAIL = 356
    s = encaje(bw, bh, W - RAIL - 74, H - 46)
    x = W - RAIL + 4

    o = [grupo(dib, 42 - bx0 * s, (H - bh * s) / 2 - by0 * s, s)]
    cab, y = cabecera_riel(x, "Figura 2.a", "Diagrama de Gantt",
                           "Cronograma aplanado adoptado, con refuerzo de un integrador y un tester "
                           "(estrategia b del punto 10). Duracion 192 dias habiles, aproximadamente 9,1 meses "
                           "de 21 dias habiles, contados desde la aprobacion del Acta de Proyecto (dia 0).", 42)
    o.append(cab)
    o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#C9D6E4" stroke-width="1"/>'
             % (x, y - 6, W - 44, y - 6))
    o.append(txt(x, y + 22, "REFERENCIAS", 14, MUTED, True))
    ref, y = riel(x, y + 52, 40, [
        (lambda a, b: m_rect(a, b, "#C0392B", "#8E2A20"),
         "Actividad del camino critico: 30 actividades con holgura total nula."),
        (lambda a, b: m_rect(a, b, "#3D77B0", "#25547F"),
         "Actividad no critica: 20 actividades."),
        (lambda a, b: m_rect(a, b, "none", "#7FA3C6", "4 3"),
         "Holgura remanente: holgura total del CPM menos el corrimiento aplicado en el aplanamiento."),
        (lambda a, b: m_linea(a, b, ORO, "6 4"),
         "Hito de control. La escala superior marca los meses de 21 dias habiles."),
        (None, "La etiqueta al pie de cada barra indica duracion y, cuando existe, holgura: 8d · h9."),
    ])
    o.append(ref)
    fases, y = parrafo(x, y + 6, "FASES  " + "   ".join("%s %s" % f for f in fig2.FASES), 13.5, 52)
    o.append(fases)
    nota, _ = parrafo(x, y + 14, "El histograma de recursos por perfil se presenta en la figura 2.b, "
                                 "sobre el mismo eje de tiempo y a la misma escala.", 13.5, 52)
    o.append(nota)
    return lamina(escalar_css(1.34), "".join(o))


def fig2b_16x9():
    fig2.PPD, fig2.XT = PPD16, XT16
    svg = fig2.svg_histo()
    dib = parte(svg, marca_fin='class="legtit"', quitar=('class="figtit"', 'class="figsub"'))[:-1]

    bx0, by0 = 66, 138
    bw = (fig2.XT + 192 * fig2.PPD) - bx0
    bh = 150 + 9 * (92 + 16) - by0

    RAIL = 356
    s = encaje(bw, bh, W - RAIL - 74, H - 46)
    x = W - RAIL + 4

    o = [grupo(dib, 42 - bx0 * s, (H - bh * s) / 2 - by0 * s, s)]
    cab, y = cabecera_riel(x, "Figura 2.b", "Histograma de recursos",
                           "Personas requeridas de cada perfil en cada dia habil del cronograma aplanado. "
                           "Mismo eje de tiempo y misma escala que la figura 2.a.", 42)
    o.append(cab)
    o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#C9D6E4" stroke-width="1"/>'
             % (x, y - 6, W - 44, y - 6))
    o.append(txt(x, y + 22, "REFERENCIAS", 14, MUTED, True))
    ref, y = riel(x, y + 52, 40, [
        (lambda a, b: m_rect(a, b, "#3D77B0"), "Una persona del perfil requerida ese dia habil."),
        (lambda a, b: m_rect(a, b, "#7FA3C6"),
         "Dos personas requeridas: son las ventanas que motivaron el refuerzo de EI y QA."),
        (lambda a, b: m_linea(a, b, ORO, "5 3"), "Dotacion asignada. No se supera en ningun dia."),
    ])
    o.append(ref)
    nota, _ = parrafo(x, y + 8, "Esfuerzo total: 530 dias-persona, equivalentes a 4.240 horas-persona sobre "
                                "jornada de ocho horas, con once personas distribuidas en nueve perfiles. "
                                "Los valores coinciden con la tabla de carga por perfil del punto 10.", 13.5, 52)
    o.append(nota)
    return lamina(escalar_css(1.34), "".join(o))


# ========================================================= Figura 3 · Plano

REFS3 = [
    ("matafuego", "Matafuego identificado por clase: ABC en deposito, playa de carga y aula; C o agente limpio en sala tecnica y NOC."),
    ("luz", "Luz de emergencia."),
    ("salida", "Salida de emergencia con su sentido de apertura, hacia el sentido de evacuacion."),
    ("evac", "Recorrido de evacuacion senalizado desde cada sector hasta el punto de encuentro."),
    ("senal", "Senalizacion: velocidad maxima, riesgo electrico, acceso restringido, carga maxima de estanteria y aforo del aula."),
    ("senda", "Senda peatonal demarcada, en trazo continuo."),
    ("veh", "Circulacion vehicular de sentido unico, en trazo distinto y con flechas."),
    ("cota", "Cota de diseno. Minimo supuesto, a validar con el Servicio de Higiene y Seguridad."),
    ("amb", "Recorrido de acceso de ambulancia hasta el ingreso principal."),
    ("boti", "Botiquin de primeros auxilios."),
]


def simbolo3(k):
    """Las mismas muestras de la simbologia de la lamina A3, a escala del riel."""
    def f(x, y):
        if k == "matafuego":
            return ('<circle cx="%.1f" cy="%.1f" r="11" fill="%s" stroke="#7A241B" stroke-width="1.2"/>'
                    '<text x="%.1f" y="%.1f" font-size="9" font-weight="700" fill="#FFFFFF" text-anchor="middle">ABC</text>'
                    % (x + 14, y - 5, ROJO, x + 14, y - 1.6))
        if k == "luz":
            return ('<rect x="%.1f" y="%.1f" width="19" height="12" rx="2" fill="#FFF3D6" stroke="%s" stroke-width="1.2"/>'
                    '<text x="%.1f" y="%.1f" font-size="9.5" font-weight="700" fill="%s" text-anchor="middle">E</text>'
                    % (x + 5, y - 15, ORO, x + 14.5, y - 5.6, ORO))
        if k == "salida":
            return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#2E7D5B" stroke-width="4"/>'
                    '<path d="M %.1f %.1f A 18 18 0 0 1 %.1f %.1f" fill="none" stroke="#2E7D5B" stroke-width="1.2" stroke-dasharray="4 3"/>'
                    % (x, y - 10, x + 29, y - 10, x + 29, y - 10, x + 29, y + 8))
        if k == "evac":
            return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#2E7D5B" stroke-width="3"'
                    ' stroke-dasharray="10 6" marker-end="url(#evac)"/>' % (x, y - 5, x + 30, y - 5))
        if k == "senal":
            return ('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="#FFF3D6" stroke="%s" stroke-width="1.4"/>'
                    % (x + 14, y - 18, x + 26, y + 2, x + 2, y + 2, ORO))
        if k == "senda":
            return ('<rect x="%.1f" y="%.1f" width="32" height="13" fill="#E9F3EC" stroke="#2E7D5B" stroke-width="1.4"/>'
                    % (x, y - 12))
        if k == "veh":
            return ('<rect x="%.1f" y="%.1f" width="34" height="15" fill="#E2E6EA" stroke="#8798A8" stroke-width="1"/>'
                    '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#5B7FA6" stroke-width="2.6" marker-end="url(#veh)"/>'
                    % (x, y - 14, x + 4, y - 6.5, x + 25, y - 6.5))
        if k == "cota":
            return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1"'
                    ' marker-start="url(#cot)" marker-end="url(#cot)"/>' % (x, y - 5, x + 32, y - 5, ORO))
        if k == "amb":
            return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#1F6FB2" stroke-width="3"'
                    ' stroke-dasharray="2 5" marker-end="url(#amb)"/>' % (x, y - 5, x + 30, y - 5))
        return ('<rect x="%.1f" y="%.1f" width="20" height="20" rx="2.5" fill="#FFFFFF" stroke="%s" stroke-width="1.6"/>'
                '<path d="M %.1f %.1f L %.1f %.1f M %.1f %.1f L %.1f %.1f" stroke="%s" stroke-width="2.4"/>'
                % (x + 4, y - 17, ROJO, x + 14, y - 13.5, x + 14, y - 3.5, x + 9, y - 8.5, x + 19, y - 8.5, ROJO))
    return f


def fig3_16x9():
    dib = parte(fig3.svg(), quitar=('class="figtit"', 'class="figsub"'))

    bx0, by0, bw, bh = 0, 100, 1400, 918
    RAIL = 424
    s = encaje(bw, bh, W - RAIL - 66, H - 44)
    x = W - RAIL + 4

    o = [grupo(dib, 30 - bx0 * s, (H - bh * s) / 2 - by0 * s, s)]
    cab, y = cabecera_riel(x, "Figura 3", "Plano de la base operativa",
                           "Planta, escala 1:125, norte indicado, cotas en metros. Sectores del proceso critico "
                           "de instalacion de fibra optica, con circulaciones, senalizacion, proteccion contra "
                           "incendio y evacuacion.", 50)
    o.append(cab)
    o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#C9D6E4" stroke-width="1"/>'
             % (x, y - 8, W - 42, y - 8))
    o.append(txt(x, y + 18, "REFERENCIAS Y SIMBOLOGIA", 14, MUTED, True))
    ref, y = riel(x, y + 46, 46, [(simbolo3(k), d) for k, d in REFS3], size=14.5, sangria=46)
    o.append(ref)
    nota, _ = parrafo(x, y + 2, "Las cotas son minimos de diseno supuestos, a validar con el Servicio de Higiene "
                                "y Seguridad de la organizacion; la distribucion es una base operativa tipo.",
                      13, 58)
    o.append(nota)
    return lamina(escalar_css(1.06), "".join(o))


# ========================================================= Figura 4 · Campo

def fig4_16x9():
    dib = parte(fig4.svg(), quitar=('class="figtit"', 'class="figsub"'))

    bx0, by0, bw, bh = 52, 92, 1642, 1020
    RAIL = 322
    s = encaje(bw, bh, W - RAIL - 62, H - 40)
    x = W - RAIL + 4

    o = [grupo(dib, 28 - bx0 * s, (H - bh * s) / 2 - by0 * s, s)]
    cab, y = cabecera_riel(x, "Figura 4", "Croquis de trabajo en campo",
                           "Escena de tendido aereo en via publica, en planta y en vista lateral auxiliar, "
                           "con los esquemas complementarios de camara subterranea y de domicilio del cliente.",
                           38, sub_car=19)
    o.append(cab)
    o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#C9D6E4" stroke-width="1"/>'
             % (x, y - 6, W - 44, y - 6))
    bloques = [
        ("A · Planta", "Escena de tendido aereo: vehiculo aguas arriba como barrera fisica, perímetro vallado "
                       "sobre la proyeccion de caida de objetos y desvío peatonal."),
        ("B · Vista lateral", "Corte de la misma escena, con la zona de aproximacion prohibida a la linea energizada."),
        ("C · Cámara subterránea", "Espacio confinado: boca vallada en sus cuatro lados, vigia permanente en el "
                                   "exterior, ventilacion forzada y tripode de rescate."),
        ("D · Domicilio del cliente", "Único sector donde el sistema del proyecto actua como medida preventiva: "
                                      "la lista de verificacion bloquea el inicio de la orden."),
    ]
    yy = y + 26
    for t, d in bloques:
        o.append(txt(x, yy, t, 15.5, AZUL, True))
        p, yy = parrafo(x, yy + 21, d, 13.5, 44)
        o.append(p)
        yy += 14
    nota, _ = parrafo(x, yy + 2, "Las distancias son minimos de diseno supuestos, a validar con el Servicio de "
                                 "Higiene y Seguridad y con la normativa del distribuidor electrico.", 13, 46)
    o.append(nota)
    return lamina(escalar_css(1.16), "".join(o))


FIGURAS = [("fig1-red", fig1_16x9), ("fig2a-gantt", fig2a_16x9), ("fig2b-histo", fig2b_16x9),
           ("fig3-plano", fig3_16x9), ("fig4-campo", fig4_16x9)]


def main(destino):
    os.makedirs(destino, exist_ok=True)
    for nombre, fn in FIGURAS:
        ruta = os.path.join(destino, nombre + ".svg")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(fn())
        print(ruta)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1
         else os.path.join(RAIZ, "materias", "ASI", "figs", "presentacion"))
