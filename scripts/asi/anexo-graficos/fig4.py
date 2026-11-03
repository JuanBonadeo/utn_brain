# -*- coding: utf-8 -*-
"""Figura 4 - Croquis tipo de trabajo en campo.

Escena de tendido aereo en via publica, en planta y en vista lateral auxiliar,
con los dos esquemas complementarios que pide el punto 6: camara subterranea y
domicilio del cliente.
"""

AZUL, CELESTE, ROJO, AMBAR, VERDE = "#15406B", "#DCE9F7", "#B23A2E", "#C8901F", "#2E7D5B"
GRIS, ASFALTO, VEREDA, NARANJA = "#8798A8", "#DFE3E7", "#F0EDE6", "#E8622A"

O = []
def add(s): O.append(s)
def r(v): return round(v, 1)
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def txt(x, y, s, cls="ann", anchor=None, rot=None):
    a = ' text-anchor="%s"' % anchor if anchor else ''
    if rot is not None:
        add('<text class="%s" transform="translate(%s,%s) rotate(%s)"%s>%s</text>' % (cls, r(x), r(y), rot, a, esc(s)))
    else:
        add('<text class="%s" x="%s" y="%s"%s>%s</text>' % (cls, r(x), r(y), a, esc(s)))

def bloque(x, y, lineas, cls="micro", dy=13):
    for i, s in enumerate(lineas):
        if s:
            txt(x, y + i * dy, s, cls)

def marco(x, y, w, h, titulo, sub=""):
    add('<rect x="%s" y="%s" width="%s" height="%s" rx="4" fill="#FFFFFF" stroke="#C9D6E4" stroke-width="1.4"/>' % (x, y, w, h))
    add('<rect x="%s" y="%s" width="%s" height="26" rx="4" fill="%s"/>' % (x, y, w, CELESTE))
    add('<text class="marcotit" x="%s" y="%s">%s</text>' % (x + 12, y + 18, esc(titulo)))
    if sub:
        add('<text class="marcosub" x="%s" y="%s">%s</text>' % (x + w - 12, y + 18, esc(sub)))

def caja(x, y, w, h, titulo, lineas, color=AMBAR, fondo="#FFF3D6"):
    add('<rect x="%s" y="%s" width="%s" height="%s" rx="4" fill="%s" stroke="%s" stroke-width="1.2"/>' % (x, y, w, h, fondo, color))
    txt(x + 12, y + 19, titulo, "locn")
    bloque(x + 12, y + 35, lineas)

def cono(x, y, s=1.0):
    add('<g transform="translate(%s,%s) scale(%s)"><polygon points="0,-11 6,4 -6,4" fill="%s" stroke="#A5411A" stroke-width="0.8"/>'
        '<rect x="-4.6" y="-4" width="9.2" height="3.2" fill="#FFFFFF"/><rect x="-7.5" y="4" width="15" height="2.6" fill="#A5411A"/></g>' % (r(x), r(y), s, NARANJA))

def valla_h(x, y, w):
    add('<g transform="translate(%s,%s)"><rect x="0" y="-5" width="%s" height="10" fill="#FFFFFF" stroke="#A5411A" stroke-width="0.9"/>' % (r(x), r(y), r(w)))
    for i in range(int(w // 10)):
        add('<polygon points="%s,-5 %s,-5 %s,5 %s,5" fill="%s" opacity="0.9"/>' % (r(i * 10), r(i * 10 + 5), r(i * 10 + 10), r(i * 10 + 5), NARANJA))
    add('</g>')

def valla_v(x, y, h):
    add('<g transform="translate(%s,%s) rotate(90)"><rect x="0" y="-5" width="%s" height="10" fill="#FFFFFF" stroke="#A5411A" stroke-width="0.9"/>' % (r(x), r(y), r(h)))
    for i in range(int(h // 10)):
        add('<polygon points="%s,-5 %s,-5 %s,5 %s,5" fill="%s" opacity="0.9"/>' % (r(i * 10), r(i * 10 + 5), r(i * 10 + 10), r(i * 10 + 5), NARANJA))
    add('</g>')

def persona(x, y, color=AZUL, arnes=False, esc_=1.0):
    add('<g transform="translate(%s,%s) scale(%s)">' % (r(x), r(y), esc_))
    add('<circle cx="0" cy="-13" r="5.4" fill="%s"/>' % color)
    add('<path d="M 0 -7.5 L 0 4 M -7 -3 L 7 -3 M 0 4 L -5.5 14 M 0 4 L 5.5 14" stroke="%s" stroke-width="2.4" fill="none" stroke-linecap="round"/>' % color)
    if arnes:
        add('<circle cx="0" cy="-1" r="6.6" fill="none" stroke="%s" stroke-width="1.8"/>' % AMBAR)
    add('</g>')

def baliza(x, y):
    add('<g transform="translate(%s,%s)"><circle r="5" fill="#FFC400" stroke="#B58900" stroke-width="0.9"/>'
        '<path d="M -10 -7 L -5 -3 M 10 -7 L 5 -3 M 0 -12 L 0 -7" stroke="#B58900" stroke-width="1.2"/></g>' % (r(x), r(y)))

def vehiculo(x, y, w=140, h=58):
    add('<g transform="translate(%s,%s)">' % (r(x), r(y)))
    add('<rect x="0" y="0" width="%s" height="%s" rx="6" fill="#F4F7FA" stroke="%s" stroke-width="1.6"/>' % (w, h, AZUL))
    add('<rect x="%s" y="6" width="%s" height="%s" rx="3" fill="%s" stroke="%s" stroke-width="1"/>' % (r(w * 0.40), r(w * 0.55), h - 12, CELESTE, AZUL))
    add('<rect x="6" y="8" width="%s" height="%s" rx="3" fill="#FFFFFF" stroke="%s" stroke-width="1"/>' % (r(w * 0.28), h - 16, AZUL))
    add('</g>')
    baliza(x + 14, y - 4)
    baliza(x + w - 14, y - 4)

def cota_h(x1, x2, y, etiqueta, dy=-6):
    add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="0.9" marker-start="url(#cot)" marker-end="url(#cot)"/>' % (r(x1), r(y), r(x2), r(y), AMBAR))
    txt((x1 + x2) / 2, y + dy, etiqueta, "cota", "middle")

def cota_v(x, y1, y2, etiqueta, dx=-7):
    add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="0.9" marker-start="url(#cot)" marker-end="url(#cot)"/>' % (r(x), r(y1), r(x), r(y2), AMBAR))
    txt(x + dx, (y1 + y2) / 2, etiqueta, "cota", "middle", -90)


def svg():
    del O[:]
    add('<text class="figtit" x="60" y="46">Figura 4 &#8212; Croquis tipo de trabajo en campo</text>')
    add('<text class="figsub" x="60" y="70">Escena de tendido aereo en via publica, en planta y en vista lateral auxiliar, con los esquemas complementarios de camara subterranea y de domicilio del cliente. '
        'Las distancias son minimos de diseno supuestos, a validar con el Servicio de Higiene y Seguridad y con la normativa del distribuidor electrico.</text>')

    # ==================================================== A) PLANTA
    marco(60, 96, 990, 604, "A  ·  PLANTA DE LA ESCENA DE TENDIDO AEREO", "sentido del transito de izquierda a derecha")
    VN0, VN1, CZ1, VS1 = 176, 236, 424, 484
    add('<rect x="76" y="%s" width="958" height="%s" fill="%s" stroke="%s" stroke-width="0.8"/>' % (VN0, VN1 - VN0, VEREDA, GRIS))
    add('<rect x="76" y="%s" width="958" height="%s" fill="%s" stroke="%s" stroke-width="0.8"/>' % (VN1, CZ1 - VN1, ASFALTO, GRIS))
    add('<rect x="76" y="%s" width="958" height="%s" fill="%s" stroke="%s" stroke-width="0.8"/>' % (CZ1, VS1 - CZ1, VEREDA, GRIS))
    txt(84, VN1 - 8, "VEREDA", "locs")
    txt(84, VS1 - 8, "VEREDA", "locs")
    for x in range(88, 1030, 42):
        add('<rect x="%s" y="328" width="24" height="3" fill="#FFFFFF"/>' % x)
    for x in (200, 480, 820, 1000):
        add('<line x1="%s" y1="382" x2="%s" y2="382" stroke="#5B7FA6" stroke-width="2.8" marker-end="url(#veh)"/>' % (x - 30, x + 22))
    txt(96, 372, "SENTIDO DEL TRANSITO", "viacap")

    # perimetro vallado: zona de trabajo + proyeccion de caida de objetos
    VX0, VX1, VY0, VY1 = 596, 828, 152, 344
    add('<rect x="%s" y="%s" width="%s" height="%s" fill="#FDF3EE" stroke="%s" stroke-width="1.3" stroke-dasharray="7 4"/>'
        % (VX0, VY0, VX1 - VX0, VY1 - VY0, NARANJA))
    valla_h(VX0, VY0, VX1 - VX0)
    valla_h(VX0, VY1, VX1 - VX0)
    valla_v(VX0, VY0, VY1 - VY0)
    valla_v(VX1, VY0, VY1 - VY0)
    txt(VX0, VY0 - 22, "PERIMETRO VALLADO", "locn")
    txt(VX0, VY0 - 10, "encierra la zona de trabajo y la proyeccion de caida de objetos", "micro")
    PX, PY = 712, 214
    add('<circle cx="%s" cy="%s" r="46" fill="none" stroke="%s" stroke-width="0.9" stroke-dasharray="3 3"/>' % (PX, PY, NARANJA))
    cota_h(PX, PX + 46, PY, "3,00 m", 15)
    add('<circle cx="%s" cy="%s" r="13" fill="#B98B4E" stroke="#7A5A2E" stroke-width="1.6"/>' % (PX, PY))
    txt(PX, PY + 3.4, "P", "sim", "middle")
    txt(PX + 20, PY - 22, "poste", "micro")
    persona(PX - 4, PY + 46, ROJO, arnes=True)
    txt(PX - 4, PY + 74, "operario en altura", "micro", "middle")
    txt(PX - 4, PY + 85, "arnes con doble cabo", "micro", "middle")
    persona(770, 288, AZUL)
    txt(770, 312, "segundo operario", "micro", "middle")
    txt(770, 323, "a nivel de piso: vigia", "micro", "middle")
    txt(VX0 + 8, VY1 - 10, "proyeccion de caida de objetos", "micro")

    # vehiculo aguas arriba + conos de transicion
    vehiculo(404, 250)
    txt(474, 350, "VEHICULO TECNICO con balizas, ubicado aguas arriba", "micro", "middle")
    txt(474, 361, "del punto de trabajo, actuando como barrera fisica", "micro", "middle")
    txt(474, 285, "VEHICULO", "micro", "middle")
    for i in range(7):
        cono(556 + i * 12, 300 - i * 8, 0.8)
    txt(560, 242, "conos de transicion", "micro", "end")
    for i in range(9):
        cono(VX0 + 12 + i * 26, VY1 + 14, 0.8)

    # desvio peatonal senalizado
    add('<path d="M 132 200 L 300 200 L 300 452 L 940 452 L 940 200 L 1010 200" fill="none" stroke="%s" stroke-width="2.6" stroke-dasharray="9 5" marker-end="url(#evac)"/>' % VERDE)
    for cx_ in (288, 928):
        for i in range(5):
            add('<rect x="%s" y="%s" width="7" height="%s" fill="#FFFFFF" opacity="0.9"/>' % (cx_ - 2 + i * 11, VN1 + 2, CZ1 - VN1 - 4))
    txt(132, 192, "DESVIO PEATONAL SENALIZADO", "locn")
    txt(320, 468, "el peaton cruza a la vereda opuesta aguas arriba del vallado y regresa aguas abajo, por sendas senalizadas", "micro")

    caja(76, 512, 470, 116, "CONDICION DE INICIO DE LA TAREA",
         ["Distancia minima de aproximacion a la linea energizada verificada antes de subir.",
          "Escalera dielectrica, nunca metalica. Suspension de la tarea con viento o tormenta.",
          "Lista de verificacion de seguridad completada en la aplicacion de campo: sin ella",
          "la orden no puede iniciarse.",
          "Habilitacion vigente para trabajo en altura y riesgo electrico (tratamiento de R04)."])
    caja(564, 512, 470, 116, "EQUIPO DE PROTECCION PERSONAL",
         ["Casco con barbijo. Arnes con doble cabo sobre anclaje certificado.",
          "Guantes y calzado dielectricos. Chaleco reflectivo.",
          "",
          "Se consigna como complemento y nunca como respuesta principal al riesgo:",
          "la prevencion sobre la persona es el escalon mas debil de la jerarquia."],
         AZUL, "#F6FAFD")
    txt(76, 652, "Riesgos tratados: trabajo en altura, riesgo electrico por proximidad a linea energizada, circulacion vehicular y caida de herramientas sobre terceros.", "notap")
    txt(76, 670, "Niveles de prevencion: 1 diseno y 3 medio de transmision, con complemento de nivel 4 sobre la persona.", "notap")
    txt(76, 688, "El vallado y la posicion del vehiculo son prevencion en el medio; el bloqueo de la orden en la aplicacion de campo es prevencion en el diseno del flujo de trabajo.", "notap")

    # ==================================================== B) VISTA LATERAL
    marco(1074, 96, 616, 604, "B  ·  VISTA LATERAL AUXILIAR", "corte transversal de la misma escena")
    SUELO, TOPE = 588, 176
    add('<rect x="1090" y="%s" width="584" height="70" fill="%s" stroke="%s" stroke-width="0.8"/>' % (SUELO, VEREDA, GRIS))
    add('<rect x="1090" y="%s" width="300" height="70" fill="%s" stroke="%s" stroke-width="0.8"/>' % (SUELO, ASFALTO, GRIS))
    txt(1240, SUELO + 58, "CALZADA", "locs", "middle")
    txt(1540, SUELO + 58, "VEREDA", "locs", "middle")
    PSX = 1452
    add('<rect x="%s" y="%s" width="16" height="%s" fill="#B98B4E" stroke="#7A5A2E" stroke-width="1.4"/>' % (PSX - 8, TOPE, SUELO - TOPE))
    add('<line x1="1096" y1="%s" x2="1668" y2="%s" stroke="#2B2B2B" stroke-width="2.6"/>' % (TOPE + 12, TOPE + 12))
    add('<line x1="1096" y1="%s" x2="1668" y2="%s" stroke="#2B2B2B" stroke-width="2.6"/>' % (TOPE + 26, TOPE + 26))
    add('<rect x="%s" y="%s" width="40" height="10" fill="#D8D8D8" stroke="#666" stroke-width="0.8"/>' % (PSX - 20, TOPE + 2))
    txt(1096, TOPE - 8, "LINEA DE ENERGIA ENERGIZADA  ·  nivel superior", "locn")
    add('<path d="M 1096 356 Q 1274 372 1452 356 Q 1560 350 1668 358" fill="none" stroke="%s" stroke-width="2.2"/>' % VERDE)
    txt(1096, 344, "TENDIDO DE FIBRA OPTICA  ·  nivel inferior", "locn")
    cota_v(1150, TOPE + 26, 356, "1,50 m entre servicios")
    add('<rect x="%s" y="%s" width="150" height="52" fill="#FDECE9" stroke="%s" stroke-width="1.1" stroke-dasharray="5 3"/>' % (PSX - 172, TOPE + 26, ROJO))
    txt(PSX - 97, TOPE + 47, "ZONA DE APROXIMACION", "microrojo", "middle")
    txt(PSX - 97, TOPE + 58, "PROHIBIDA", "microrojo", "middle")
    cota_v(PSX - 186, TOPE + 26, TOPE + 78, "1,00 m")
    bloque(1096, 424, ["Distancia minima de aproximacion a la linea energizada:",
                       "condicion de inicio de la tarea. Valor supuesto, a validar",
                       "con la normativa del distribuidor electrico."])
    # escalera dielectrica
    EX0, EY0, EX1, EY1 = 1352, SUELO, 1436, 344
    for off in (0, 17):
        add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="2.2"/>' % (EX0 + off, EY0, EX1 + off, EY1, AMBAR))
    for i in range(8):
        t = i / 8.0 + 0.08
        add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.5"/>'
            % (r(EX0 + (EX1 - EX0) * t), r(EY0 + (EY1 - EY0) * t), r(EX0 + 17 + (EX1 - EX0) * t), r(EY0 + (EY1 - EY0) * t), AMBAR))
    bloque(1096, 486, ["escalera dielectrica, apoyo 1:4, atada en su extremo superior"])
    persona(1444, 358, ROJO, arnes=True)
    add('<path d="M 1444 350 Q 1420 334 1448 318" fill="none" stroke="%s" stroke-width="1.6" stroke-dasharray="3 2"/>' % AMBAR)
    bloque(1478, 316, ["doble cabo sobre", "anclaje certificado"])
    persona(1330, SUELO - 16, AZUL)
    txt(1330, SUELO + 22, "vigia a nivel de piso", "micro", "middle")
    vehiculo(1116, SUELO - 62, 116, 52)
    txt(1174, SUELO - 30, "VEHICULO", "micro", "middle")
    cono(1266, SUELO - 8, 0.9)
    cono(1292, SUELO - 8, 0.9)
    cota_v(1666, TOPE, SUELO, "altura del poste 8,00 m", 10)

    # ==================================================== C) CAMARA SUBTERRANEA
    marco(60, 724, 810, 416, "C  ·  ESQUEMA COMPLEMENTARIO: CAMARA SUBTERRANEA", "espacio confinado  ·  planta")
    add('<rect x="78" y="768" width="774" height="298" fill="%s" stroke="%s" stroke-width="0.8"/>' % (VEREDA, GRIS))
    BX0, BY0, BX1, BY1 = 250, 878, 400, 998
    add('<rect x="%s" y="%s" width="%s" height="%s" fill="#3F4A55" stroke="#20262C" stroke-width="1.6"/>' % (BX0, BY0, BX1 - BX0, BY1 - BY0))
    add('<text class="sim" x="%s" y="%s" text-anchor="middle" fill="#F2F5F8">BOCA DE CAMARA</text>' % (r((BX0 + BX1) / 2), r(BY1 - 10)))
    valla_h(BX0 - 26, BY0 - 24, 202)
    valla_h(BX0 - 26, BY1 + 24, 202)
    valla_v(BX0 - 30, BY0 - 20, 158)
    valla_v(BX1 + 30, BY0 - 20, 158)
    for x, y in ((BX0 - 30, BY0 - 24), (BX1 + 30, BY0 - 24), (BX0 - 30, BY1 + 24), (BX1 + 30, BY1 + 24)):
        cono(x, y, 0.8)
    txt(BX0 - 30, BY0 - 40, "BOCA VALLADA EN SUS CUATRO LADOS", "locn")
    TCX, TCY = (BX0 + BX1) / 2, BY0 - 12
    add('<g stroke="%s" stroke-width="2.4" fill="none"><path d="M %s %s L %s %s M %s %s L %s %s M %s %s L %s %s"/></g>'
        % (AMBAR, TCX, TCY, TCX - 46, BY1 - 14, TCX, TCY, TCX + 46, BY1 - 14, TCX, TCY, TCX, BY1 - 2))
    add('<circle cx="%s" cy="%s" r="6" fill="%s"/>' % (TCX, TCY, AMBAR))
    txt(BX1 + 46, BY0 + 6, "TRIPODE DE RESCATE", "micro")
    txt(BX1 + 46, BY0 + 18, "con linea de vida", "micro")
    add('<rect x="108" y="906" width="58" height="46" rx="4" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>' % AZUL)
    add('<circle cx="137" cy="929" r="15" fill="none" stroke="%s" stroke-width="1.4"/>' % AZUL)
    add('<path d="M 137 916 A 13 13 0 0 1 148 936 M 137 942 A 13 13 0 0 1 126 922" fill="none" stroke="%s" stroke-width="1.6"/>' % AZUL)
    add('<path d="M 166 929 L 244 929" stroke="#7FA3C6" stroke-width="6" stroke-dasharray="7 4" opacity="0.75"/>')
    txt(137, 896, "VENTILACION FORZADA", "micro", "middle")
    txt(205, 948, "conducto", "micro", "middle")
    persona(500, 934, AZUL)
    txt(500, 962, "VIGIA PERMANENTE", "micro", "middle")
    txt(500, 973, "EN EL EXTERIOR", "micro", "middle")
    txt(500, 984, "trabajo de a dos", "micro", "middle")
    caja(568, 800, 274, 216, "CONDICIONES DE INGRESO",
         ["Permiso de trabajo escrito previo.",
          "Medicion de atmosfera antes del ingreso",
          "y durante toda la tarea.",
          "Ventilacion forzada en marcha.",
          "Arnes con linea de vida sobre el tripode",
          "de rescate. Prohibido ingresar sin vigia.",
          "",
          "Riesgos: atmosfera deficiente o explosiva,",
          "anegamiento y caida a distinto nivel.",
          "",
          "Niveles de prevencion: 1 diseno, 2 origen."])
    txt(78, 1100, "El vallado en los cuatro lados y la ventilacion forzada son prevencion en el diseno y en el origen; el vigia y el permiso, control de la tarea.", "notap")

    # ==================================================== D) DOMICILIO DEL CLIENTE
    marco(896, 724, 794, 416, "D  ·  ESQUEMA COMPLEMENTARIO: DOMICILIO DEL CLIENTE", "planta tipo")
    HX0, HY0, HX1, HY1 = 916, 782, 1306, 1074
    add('<rect x="%s" y="%s" width="%s" height="%s" fill="#FFFFFF" stroke="%s" stroke-width="1.8"/>' % (HX0, HY0, HX1 - HX0, HY1 - HY0, AZUL))
    add('<line x1="1116" y1="%s" x2="1116" y2="982" stroke="%s" stroke-width="1.4"/>' % (HY0, AZUL))
    add('<line x1="%s" y1="982" x2="%s" y2="982" stroke="%s" stroke-width="1.4"/>' % (HX0, HX1, AZUL))
    txt(HX0 + 10, HY0 + 18, "LIVING", "locs")
    txt(1126, HY0 + 18, "PASILLO", "locs")
    txt(HX0 + 10, 1002, "ACCESO", "locs")
    add('<rect x="%s" y="%s" width="34" height="22" rx="3" fill="%s" stroke="%s" stroke-width="1.2"/>' % (1000, 830, CELESTE, AZUL))
    add('<text class="sim" x="1017" y="845" text-anchor="middle">ONT</text>')
    txt(1017, 870, "equipo del cliente", "micro", "middle")
    add('<rect x="1250" y="820" width="42" height="56" fill="#FDECE9" stroke="%s" stroke-width="1.6"/>' % ROJO)
    add('<text class="sim" x="1271" y="844" text-anchor="middle" fill="%s">&#9889;</text>' % ROJO)
    add('<text class="sim" x="1271" y="860" text-anchor="middle" fill="%s">TAB.</text>' % ROJO)
    txt(1292, 810, "TABLERO DOMICILIARIO", "microrojo", "end")
    add('<rect x="1150" y="900" width="142" height="70" fill="#E9F3EC" stroke="%s" stroke-width="1.2" stroke-dasharray="6 3"/>' % VERDE)
    txt(1221, 930, "ZONA DESPEJADA", "micro", "middle")
    txt(1221, 943, "DE TRABAJO", "micro", "middle")
    txt(1221, 956, "1,50 x 1,50 m", "micro", "middle")
    for off in (0, 18):
        add('<line x1="%s" y1="904" x2="%s" y2="966" stroke="%s" stroke-width="2"/>' % (1122 + off, 1122 + off, AMBAR))
    for i in range(5):
        add('<line x1="1122" y1="%s" x2="1140" y2="%s" stroke="%s" stroke-width="1.4"/>' % (910 + i * 14, 910 + i * 14, AMBAR))
    txt(1131, 894, "escalera", "micro", "middle")
    bloque(HX0 + 10, 1024, [
        "Verificacion y corte de energia en el tablero domiciliario antes de intervenir.",
        "Escalera propia certificada, nunca la que provee el cliente.",
        "Trabajo en la zona despejada, con los ocupantes fuera del area."], "micro", 14)
    caja(1330, 782, 344, 292, "CONTROLES DE LA ORDEN",
         ["Lista de verificacion de seguridad obligatoria en la",
          "aplicacion de campo. Bloquea el inicio de la orden si",
          "no se completa: prevencion en el diseno del flujo.",
          "",
          "Protocolo de trabajo solitario con aviso de llegada",
          "y de cierre.",
          "",
          "Habilitacion vigente para trabajo en altura y riesgo",
          "electrico como condicion de despacho: es el",
          "tratamiento comprometido del riesgo R04.",
          "",
          "Riesgos: riesgo electrico en el tablero domiciliario,",
          "caida desde escalera, animales sueltos y conflicto",
          "con el cliente.",
          "",
          "Niveles de prevencion: 1 diseno y 4 persona."],
         AZUL, "#F6FAFD")
    txt(916, 1100, "Es el unico sector donde el sistema del proyecto actua directamente como medida preventiva: el control deja de depender de la memoria del tecnico.", "notap")
    return "\n".join(O)
