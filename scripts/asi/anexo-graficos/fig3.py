# -*- coding: utf-8 -*-
"""Figura 3 - Plano de la base operativa, en planta.

Sigue elemento por elemento la Especificacion de los planos del punto 6 del
entregable. Escala grafica 1 m = 8 px. Cotas declaradas como minimos de diseno
supuestos, a validar con el Servicio de Higiene y Seguridad.
"""

M = 8.0                      # pixeles por metro
def m(v): return v * M
def r(v): return round(v, 1)
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

AZUL, CELESTE, ROJO, AMBAR, VERDE = "#15406B", "#DCE9F7", "#B23A2E", "#C8901F", "#2E7D5B"
GRIS, ASFALTO = "#8798A8", "#E2E6EA"

O = []
def add(s): O.append(s)

def txt(x, y, s, cls="ann", anchor=None, rot=None):
    a = ' text-anchor="%s"' % anchor if anchor else ''
    if rot is not None:
        add('<text class="%s" transform="translate(%s,%s) rotate(%s)"%s>%s</text>' % (cls, r(x), r(y), rot, a, esc(s)))
    else:
        add('<text class="%s" x="%s" y="%s"%s>%s</text>' % (cls, r(x), r(y), a, esc(s)))

def bloque(x, y, lineas, cls="micro", dy=12):
    for i, s in enumerate(lineas):
        if s:
            txt(x, y + i * dy, s, cls)

def local(x, y, w, h, titulo, sub="", fill="#FFFFFF", stroke=AZUL):
    add('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" stroke-width="1.6"/>' % (r(x), r(y), r(w), r(h), fill, stroke))
    txt(x + 9, y + 17, titulo, "locn")
    if sub:
        txt(x + 9, y + 30, sub, "locs")

def cota_h(x1, x2, y, etiqueta, dy=-5):
    add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="0.8" marker-start="url(#cot)" marker-end="url(#cot)"/>' % (r(x1), r(y), r(x2), r(y), AMBAR))
    if etiqueta:
        txt((x1 + x2) / 2, y + dy, etiqueta, "cota", "middle")

def cota_v(x, y1, y2, etiqueta, dx=-6):
    add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="0.8" marker-start="url(#cot)" marker-end="url(#cot)"/>' % (r(x), r(y1), r(x), r(y2), AMBAR))
    if etiqueta:
        txt(x + dx, (y1 + y2) / 2, etiqueta, "cota", "middle", -90)

def matafuego(x, y, clase):
    add('<g><circle cx="%s" cy="%s" r="8.4" fill="%s" stroke="#7A241B" stroke-width="1"/>'
        '<text class="sim" x="%s" y="%s" text-anchor="middle" fill="#FFFFFF">%s</text></g>' % (r(x), r(y), ROJO, r(x), r(y + 3.4), clase))

def luzem(x, y):
    add('<g><rect x="%s" y="%s" width="14" height="9" rx="1.5" fill="#FFF3D6" stroke="%s" stroke-width="1"/>'
        '<text class="sim2" x="%s" y="%s" text-anchor="middle" fill="%s">E</text></g>' % (r(x - 7), r(y - 4.5), AMBAR, r(x), r(y + 3), AMBAR))

def senal(x, y, glifo, color=AMBAR):
    add('<g><polygon points="%s,%s %s,%s %s,%s" fill="#FFF3D6" stroke="%s" stroke-width="1.2"/>'
        '<text class="sim2" x="%s" y="%s" text-anchor="middle" fill="%s">%s</text></g>'
        % (r(x), r(y - 10), r(x + 9.5), r(y + 6), r(x - 9.5), r(y + 6), color, r(x), r(y + 4), color, glifo))

def salida_h(x, y, ancho, sentido):
    add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="3.4"/>' % (r(x), r(y), r(x + ancho), r(y), VERDE))
    add('<path d="M %s %s A %s %s 0 0 %d %s %s" fill="none" stroke="%s" stroke-width="0.9" stroke-dasharray="3 2"/>'
        % (r(x + ancho), r(y), r(ancho), r(ancho), 1 if sentido > 0 else 0, r(x + ancho), r(y + sentido * ancho), VERDE))

def salida_v(x, y, ancho, sentido):
    add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="3.4"/>' % (r(x), r(y), r(x), r(y + ancho), VERDE))
    add('<path d="M %s %s A %s %s 0 0 %d %s %s" fill="none" stroke="%s" stroke-width="0.9" stroke-dasharray="3 2"/>'
        % (r(x), r(y + ancho), r(ancho), r(ancho), 0 if sentido > 0 else 1, r(x + sentido * ancho), r(y + ancho), VERDE))

def flecha_veh(x, y, dx_, dy_):
    add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#5B7FA6" stroke-width="2.6" marker-end="url(#veh)"/>' % (r(x), r(y), r(x + dx_), r(y + dy_)))

def flecha_evac(d):
    add('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-dasharray="9 5" marker-end="url(#evac)"/>' % (d, VERDE))


PX0, PY0, PX1, PY1 = 60, 132, 1340, 1020      # perimetro del predio
LW = 58                                        # ancho de calzada interna
LN0, LN1 = 158, 158 + LW                       # carril norte
LS0, LS1 = PY1 - 26 - LW, PY1 - 26             # carril sur
LE0, LE1 = 1256, 1256 + LW                     # carril este
SENDA_Y, SP = 560, 14                          # eje y ancho de la senda peatonal


def svg():
    del O[:]
    add('<text class="figtit" x="60" y="46">Figura 3 &#8212; Plano de la base operativa</text>')
    add('<text class="figsub" x="60" y="70">Planta. Sectores del proceso critico de instalacion de fibra optica, con circulaciones, cotas, senalizacion, proteccion contra incendio y evacuacion. '
        'Las cotas son minimos de diseno supuestos, a validar con el Servicio de Higiene y Seguridad de la organizacion; la distribucion es una base operativa tipo.</text>')

    add('<rect x="%s" y="%s" width="%s" height="%s" fill="#F7F9F6" stroke="#5C6B57" stroke-width="2.4"/>' % (PX0, PY0, PX1 - PX0, PY1 - PY0))

    # ---------------- circulacion vehicular de sentido unico -----------------
    for (x, y, w, h) in ((PX0, LN0, PX1 - PX0, LW), (LE0, LN0, LW, LS1 - LN0), (PX0, LS0, PX1 - PX0, LW),
                         (200, 216, 120, 20), (150, 900, 720, 36)):
        add('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" stroke-width="0.8"/>' % (r(x), r(y), r(w), r(h), ASFALTO, GRIS))
    for x in range(170, 1200, 156):
        flecha_veh(x, LS0 + LW / 2, 56, 0)
    for y in range(890, 250, -150):
        flecha_veh(LE0 + LW / 2, y, 0, -56)
    for x in range(1180, 140, -156):
        flecha_veh(x, LN0 + LW / 2, -56, 0)
    flecha_veh(260, 218, 0, 14)
    txt(700, 1012, "CIRCULACION VEHICULAR DE SENTIDO UNICO  ·  velocidad maxima 10 km/h  ·  prohibido retroceder sin senalero  ·  espejo en el punto ciego de la playa", "viacap", "middle")
    cota_v(1200, LS0, LS1, "7,25 m")

    # accesos
    add('<rect x="%s" y="%s" width="14" height="%s" fill="#FFFFFF" stroke="%s" stroke-width="1.6"/>' % (PX0 - 7, LS0, LW, AMBAR))
    add('<rect x="%s" y="%s" width="14" height="%s" fill="#FFFFFF" stroke="%s" stroke-width="1.6"/>' % (PX0 - 7, LN0, LW, AMBAR))
    add('<rect x="%s" y="%s" width="14" height="26" fill="#FFFFFF" stroke="%s" stroke-width="1.6"/>' % (PX0 - 7, SENDA_Y - 13, VERDE))
    txt(PX0 + 24, LN0 - 8, "SALIDA VEHICULAR", "acc")
    txt(PX0 + 24, 916, "ACCESO VEHICULAR CONTROLADO  ·  barrera y garita de control", "acc")
    txt(PX0 + 22, SENDA_Y - 22, "ACCESO PEATONAL DIFERENCIADO", "acc")
    txt(206, 232, "acceso al estacionamiento", "micro")

    # ---------------- senda peatonal ----------------------------------------
    for (x, y, w, h) in ((PX0 + 7, SENDA_Y - SP / 2, 1173, SP),
                         (520, SENDA_Y + SP / 2, SP, 790 - SENDA_Y - SP / 2),
                         (910, 236, SP, SENDA_Y - SP / 2 - 236)):
        add('<rect x="%s" y="%s" width="%s" height="%s" fill="#E9F3EC" stroke="%s" stroke-width="1.2"/>' % (r(x), r(y), r(w), r(h), VERDE))
    txt(296, SENDA_Y - 14, "SENDA PEATONAL DEMARCADA  ·  trazo continuo, sin cruces con la circulacion vehicular", "sendacap")
    cota_v(1216, SENDA_Y - SP / 2, SENDA_Y + SP / 2, "1,75 m")

    # ---------------- estacionamiento ---------------------------------------
    local(96, 236, 340, 200, "ESTACIONAMIENTO DE VEHICULOS TECNICOS", "12 posiciones  ·  retroceso solo con senalero", "#FBFCFD")
    for i in range(5):
        add('<line x1="%s" y1="260" x2="%s" y2="436" stroke="%s" stroke-width="0.7" stroke-dasharray="4 3"/>' % (r(153 + 56.5 * i), r(153 + 56.5 * i), GRIS))
    add('<line x1="96" y1="348" x2="436" y2="348" stroke="%s" stroke-width="0.7" stroke-dasharray="4 3"/>' % GRIS)

    # ---------------- deposito y panol --------------------------------------
    local(470, 236, 430, 300, "DEPOSITO Y PANOL DE MATERIALES", "estanterias ancladas  ·  carga maxima senalizada  ·  material pesado en el nivel inferior")
    for j, y in enumerate((278, 324, 370)):
        for yy in (y, y + 22):
            add('<rect x="486" y="%s" width="248" height="14" fill="%s" stroke="%s" stroke-width="0.9"/>' % (yy, CELESTE, AZUL))
        if j == 0:
            txt(490, y + 10, "estanteria anclada  ·  carga max. 800 kg por modulo", "micro")
    cota_h(486, 486 + m(4), 424, "4,00 m")
    txt(486 + m(4) + 8, 428, "pasillo de circulacion de autoelevador", "micro")
    add('<rect x="752" y="278" width="134" height="86" fill="#F1EFE6" stroke="%s" stroke-width="1"/>' % GRIS)
    txt(758, 292, "ZONA DE BOBINAS", "locs")
    for cx_, cy_ in ((786, 322), (826, 322), (866, 322), (786, 350), (826, 350)):
        add('<circle cx="%s" cy="%s" r="11" fill="#FFFFFF" stroke="%s" stroke-width="1"/>' % (cx_, cy_, GRIS))
    add('<rect x="752" y="378" width="134" height="46" fill="#FFF3D6" stroke="%s" stroke-width="1"/>' % AMBAR)
    txt(758, 394, "MESA DE ARMADO DE KITS", "locs")
    txt(758, 408, "separada de la circulacion", "micro")
    txt(758, 420, "de vehiculos y de peatones", "micro")
    add('<rect x="486" y="446" width="182" height="70" fill="#F6F8FB" stroke="%s" stroke-width="1"/>' % AZUL)
    txt(490, 462, "PANOL DE HERRAMIENTAS", "locs")
    bloque(490, 476, ["entrega con registro nominal", "carros y medios mecanicos", "de elevacion disponibles"])
    senal(704, 462, "⚠")
    txt(704, 482, "carga max.", "micro", "middle")
    add('<g><rect x="772" y="450" width="18" height="18" rx="2" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>'
        '<path d="M 781 454 L 781 464 M 776 459 L 786 459" stroke="%s" stroke-width="2"/></g>' % (ROJO, ROJO))
    txt(781, 482, "botiquin", "micro", "middle")
    matafuego(866, 460, "ABC")
    luzem(884, 252)
    salida_h(818, 536, 34, 1)
    txt(836, 548, "salida de emergencia", "micro", "middle")

    # ---------------- sala tecnica ------------------------------------------
    local(936, 236, 300, 190, "SALA TECNICA / NODO DE DISTRIBUCION", "acceso restringido con control de identidad", "#FDF6F5", ROJO)
    for i in range(3):
        add('<rect x="%s" y="298" width="26" height="88" fill="#FFFFFF" stroke="%s" stroke-width="1.1"/>' % (r(1156 - i * 34), AZUL))
    txt(1122, 294, "tableros", "micro", "middle")
    add('<line x1="1078" y1="298" x2="1078" y2="386" stroke="%s" stroke-width="0.9" stroke-dasharray="4 3"/>' % AMBAR)
    cota_h(1078, 1078 + m(1), 342, "")
    txt(1024, 336, "1,00 m libres", "cota")
    txt(1018, 348, "frente a tableros", "cota")
    senal(966, 300, "⚡", ROJO)
    txt(966, 318, "riesgo", "micro", "middle")
    txt(966, 328, "electrico", "micro", "middle")
    senal(966, 356, "⛔", ROJO)
    txt(966, 374, "acceso", "micro", "middle")
    txt(966, 384, "restringido", "micro", "middle")
    matafuego(1214, 410, "C")
    luzem(1214, 252)
    txt(944, 414, "herramientas y calzado dielectricos  ·  bloqueo y etiquetado de energia", "micro")

    # ---------------- oficina del NOC ---------------------------------------
    local(936, 456, 300, 264, "OFICINA DEL NOC", "sala de 24 horas  ·  turnos rotativos con descanso planificado", "#F6FAFD")
    add('<line x1="1236" y1="470" x2="1236" y2="706" stroke="#4FA3D1" stroke-width="5"/>')
    txt(1250, 588, "ventanas (muro este)", "micro", "middle", -90)
    for i in range(4):
        yy = 500 + i * 40
        add('<rect x="1130" y="%s" width="80" height="24" fill="#FFFFFF" stroke="%s" stroke-width="1"/>' % (yy, AZUL))
        add('<rect x="1210" y="%s" width="8" height="24" fill="%s" stroke="%s" stroke-width="0.8"/>' % (yy, CELESTE, AZUL))
    cota_v(1116, 524, 540, "")
    txt(1110, 536, "1,60 m entre puestos", "cota", "end")
    bloque(944, 636, ["Puestos perpendiculares a las ventanas: iluminacion",
                      "sin reflejo sobre la pantalla. Monitores y sillas",
                      "regulables. Distancia ojo-pantalla de 0,60 m minimo.",
                      "Cableado en canaleta perimetral."])
    add('<rect x="940" y="698" width="292" height="8" fill="none" stroke="%s" stroke-width="1" stroke-dasharray="5 3"/>' % AMBAR)
    txt(1000, 694, "canaleta perimetral", "micro")
    matafuego(1214, 476, "C")
    luzem(950, 690)

    # ---------------- aula --------------------------------------------------
    local(96, 596, 340, 176, "AULA DE CAPACITACION", "pausas programadas  ·  practicas de altura solo con supervision", "#FBFCFD")
    for f in range(3):
        for c in range(4):
            add('<rect x="%s" y="%s" width="58" height="16" fill="#FFFFFF" stroke="%s" stroke-width="0.8"/>' % (114 + c * 78, 648 + f * 32, AZUL))
    senal(400, 620, "24")
    txt(400, 640, "aforo", "micro", "middle")
    matafuego(420, 700, "ABC")
    luzem(420, 748)
    salida_h(130, 772, 34, 1)
    txt(147, 784, "salida de emergencia", "micro", "middle")

    # ---------------- sanitarios --------------------------------------------
    local(470, 596, 230, 176, "SANITARIOS Y VESTUARIOS", "duchas de emergencia y lavaojos", "#F7F7FA")
    add('<line x1="585" y1="626" x2="585" y2="772" stroke="%s" stroke-width="1"/>' % GRIS)
    txt(478, 648, "vestuario", "micro")
    txt(592, 648, "sanitarios", "micro")

    # ---------------- mesa de despacho --------------------------------------
    local(704, 596, 196, 176, "MESA DE DESPACHO", "y supervision  ·  limite de pantallas por operador", "#F6FAFD")
    for i in range(3):
        add('<rect x="716" y="%s" width="70" height="20" fill="#FFFFFF" stroke="%s" stroke-width="1"/>' % (646 + i * 30, AZUL))
        add('<rect x="786" y="%s" width="10" height="20" fill="%s" stroke="%s" stroke-width="0.8"/>' % (646 + i * 30, CELESTE, AZUL))
    bloque(716, 748, ["auriculares con limitador de nivel sonoro", "rotacion de tareas dentro del turno"])
    matafuego(882, 616, "C")
    luzem(882, 748)

    # ---------------- playa de carga ----------------------------------------
    local(96, 790, 804, 110, "PLAYA DE CARGA Y DARSENAS", "cinco darsenas  ·  chaleco reflectivo obligatorio  ·  prohibido el retroceso sin senalero", "#F4F6F4")
    for i in range(5):
        x = 150 + i * 150
        add('<rect x="%s" y="830" width="120" height="70" fill="#FFFFFF" stroke="%s" stroke-width="1" stroke-dasharray="5 3"/>' % (x, GRIS))
        txt(x + 60, 868, "darsena %d" % (i + 1), "micro", "middle")
    matafuego(872, 852, "ABC")
    add('<circle cx="118" cy="866" r="9" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>' % AMBAR)
    txt(118, 870, "◑", "sim", "middle")
    txt(118, 890, "espejo", "micro", "middle")

    # ---------------- punto de encuentro y evacuacion ------------------------
    add('<rect x="110" y="446" width="330" height="82" rx="6" fill="#E9F3EC" stroke="%s" stroke-width="1.8" stroke-dasharray="7 4"/>' % VERDE)
    txt(122, 468, "PUNTO DE ENCUENTRO", "locn")
    bloque(122, 484, ["fuera del edificio, sobre superficie despejada y sin interferir",
                      "la circulacion vehicular  ·  aforo previsto 60 personas",
                      "senalizado y visible desde todos los sectores"])
    for x in (1150, 950, 760, 610):
        flecha_evac("M %d %d L %d %d" % (x, SENDA_Y, x - 46, SENDA_Y))
    flecha_evac("M 470 %d L 300 %d L 300 %d" % (SENDA_Y, SENDA_Y, SENDA_Y - 14))
    flecha_evac("M 266 596 L 266 %d" % (SENDA_Y + 16))
    flecha_evac("M 527 790 L 527 %d" % (SENDA_Y + 16))
    flecha_evac("M 836 552 L 836 %d" % (SENDA_Y + 12))
    flecha_evac("M 917 260 L 917 %d" % (SENDA_Y - 16))

    # ---------------- acceso de ambulancia ----------------------------------
    add('<path d="M 67 966 L 690 966 L 690 908" fill="none" stroke="#1F6FB2" stroke-width="2.6" stroke-dasharray="2 4" marker-end="url(#amb)"/>')
    txt(240, 980, "recorrido de acceso de ambulancia hasta el ingreso principal", "micro")

    # ---------------- norte y escala ----------------------------------------
    add('<g transform="translate(1392,206)"><circle r="24" fill="#FFFFFF" stroke="%s" stroke-width="1.2"/>'
        '<polygon points="0,-18 6.5,5 0,0.5 -6.5,5" fill="%s"/><text class="norte" y="18" text-anchor="middle">N</text></g>' % (AZUL, AZUL))
    add('<g transform="translate(1352,320)">')
    for i in range(4):
        add('<rect x="%s" y="-7" width="%s" height="8" fill="%s" stroke="%s" stroke-width="0.6"/>'
            % (r(i * m(2.5)), r(m(2.5)), "#FFFFFF" if i % 2 else AZUL, AZUL))
    add('<text class="micro" x="0" y="14">0</text>')
    add('<text class="micro" x="%s" y="14" text-anchor="middle">5</text>' % r(m(5)))
    add('<text class="micro" x="%s" y="14" text-anchor="end">10 m</text>' % r(m(10)))
    add('<text class="micro" x="0" y="-13">escala grafica</text>')
    add('</g>')
    bloque(1352, 372, ["Escala 1:125", "Norte indicado", "Cotas en metros"])
    return "\n".join(O)


def referencias():
    """Bloque de simbologia de las figuras 3 y 4."""
    del O[:]
    it = [("matafuego", "Matafuego identificado por clase: ABC en deposito, playa de carga y aula; C o agente limpio en sala tecnica y NOC."),
          ("luz", "Luz de emergencia."),
          ("salida", "Salida de emergencia con su sentido de apertura, hacia el sentido de evacuacion."),
          ("evac", "Recorrido de evacuacion senalizado desde cada sector hasta el punto de encuentro."),
          ("senal", "Senalizacion: velocidad maxima, riesgo electrico, acceso restringido, carga maxima de estanteria y aforo del aula."),
          ("senda", "Senda peatonal demarcada, en trazo continuo."),
          ("veh", "Circulacion vehicular de sentido unico, en trazo distinto y con flechas."),
          ("cota", "Cota de diseno. Minimo supuesto, a validar con el Servicio de Higiene y Seguridad."),
          ("amb", "Recorrido de acceso de ambulancia hasta el ingreso principal."),
          ("boti", "Botiquin de primeros auxilios.")]
    add('<line x1="60" y1="0" x2="1400" y2="0" stroke="#C9D6E4" stroke-width="0.8"/>')
    add('<text class="legtit" x="60" y="26">REFERENCIAS Y SIMBOLOGIA</text>')
    for i, (k, d) in enumerate(it):
        col = 60 + (i // 5) * 690
        y = 52 + (i % 5) * 22
        if k == "matafuego":
            add('<circle cx="%s" cy="%s" r="8.4" fill="%s" stroke="#7A241B" stroke-width="1"/><text class="sim" x="%s" y="%s" text-anchor="middle" fill="#FFFFFF">ABC</text>' % (col + 11, y - 4, ROJO, col + 11, y - 0.6))
        elif k == "luz":
            add('<rect x="%s" y="%s" width="14" height="9" rx="1.5" fill="#FFF3D6" stroke="%s" stroke-width="1"/><text class="sim2" x="%s" y="%s" text-anchor="middle" fill="%s">E</text>' % (col + 4, y - 8.5, AMBAR, col + 11, y - 1, AMBAR))
        elif k == "salida":
            add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="3.4"/><path d="M %s %s A 14 14 0 0 1 %s %s" fill="none" stroke="%s" stroke-width="0.9" stroke-dasharray="3 2"/>' % (col, y - 8, col + 22, y - 8, VERDE, col + 22, y - 8, col + 22, y + 6, VERDE))
        elif k == "evac":
            add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="2.4" stroke-dasharray="9 5" marker-end="url(#evac)"/>' % (col, y - 4, col + 22, y - 4, VERDE))
        elif k == "senal":
            add('<polygon points="%s,%s %s,%s %s,%s" fill="#FFF3D6" stroke="%s" stroke-width="1.2"/>' % (col + 11, y - 14, col + 20.5, y + 2, col + 1.5, y + 2, AMBAR))
        elif k == "senda":
            add('<rect x="%s" y="%s" width="24" height="10" fill="#E9F3EC" stroke="%s" stroke-width="1.2"/>' % (col, y - 9, VERDE))
        elif k == "veh":
            add('<rect x="%s" y="%s" width="26" height="12" fill="%s" stroke="%s" stroke-width="0.8"/><line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#5B7FA6" stroke-width="2.2" marker-end="url(#veh)"/>' % (col, y - 11, ASFALTO, GRIS, col + 3, y - 5, col + 19, y - 5))
        elif k == "cota":
            add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="0.8" marker-start="url(#cot)" marker-end="url(#cot)"/>' % (col, y - 4, col + 24, y - 4, AMBAR))
        elif k == "amb":
            add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#1F6FB2" stroke-width="2.6" stroke-dasharray="2 4" marker-end="url(#amb)"/>' % (col, y - 4, col + 22, y - 4))
        elif k == "boti":
            add('<rect x="%s" y="%s" width="16" height="16" rx="2" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/><path d="M %s %s L %s %s M %s %s L %s %s" stroke="%s" stroke-width="2"/>' % (col + 3, y - 13, ROJO, col + 11, y - 10, col + 11, y - 2, col + 7, y - 6, col + 15, y - 6, ROJO))
        add('<text class="legtxt" x="%s" y="%s">%s</text>' % (col + 36, y, esc(d)))
    return "\n".join(O)
