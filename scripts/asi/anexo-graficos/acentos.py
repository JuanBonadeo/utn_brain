# -*- coding: utf-8 -*-
"""Restituye la acentuacion castellana en el texto del anexo.

Las laminas se escriben sin acentos en el codigo fuente por comodidad; este
paso los repone sobre los nodos de texto del HTML final, palabra por palabra y
respetando mayusculas. Nunca toca atributos ni la hoja de estilos.
"""
import re

PARES = [
    ("acompana", "acompaña"), ("Acompanar", "Acompañar"), ("actua", "actúa"),
    ("Administracion", "Administración"), ("aereo", "aéreo"), ("AEREO", "AÉREO"),
    ("analisis", "análisis"), ("aplicacion", "aplicación"), ("aprobacion", "aprobación"),
    ("APROXIMACION", "APROXIMACIÓN"), ("aproximacion", "aproximación"), ("aqui", "aquí"),
    ("area", "área"), ("Arnes", "Arnés"), ("arnes", "arnés"), ("asignacion", "asignación"),
    ("atmosfera", "atmósfera"), ("automatica", "automática"),
    ("botiquin", "botiquín"), ("Botiquin", "Botiquín"),
    ("caida", "caída"), ("calculo", "cálculo"), ("camara", "cámara"), ("CAMARA", "CÁMARA"),
    ("Capacitacion", "Capacitación"), ("capacitacion", "capacitación"), ("CAPACITACION", "CAPACITACIÓN"),
    ("CIRCULACION", "CIRCULACIÓN"), ("Circulacion", "Circulación"), ("circulacion", "circulación"),
    ("Comision", "Comisión"), ("CONDICION", "CONDICIÓN"), ("condicion", "condición"),
    ("configuracion", "configuración"), ("critica", "crítica"), ("criticas", "críticas"),
    ("critico", "crítico"), ("Critico", "Crítico"),
    ("darsena", "dársena"), ("darsenas", "dársenas"), ("DARSENAS", "DÁRSENAS"),
    ("debil", "débil"), ("decision", "decisión"), ("dedicacion", "dedicación"),
    ("DEPOSITO", "DEPÓSITO"), ("deposito", "depósito"), ("dia", "día"), ("dias", "días"),
    ("dielectrica", "dieléctrica"), ("dielectricos", "dieléctricos"),
    ("Disenar", "Diseñar"), ("Diseno", "Diseño"), ("diseno", "diseño"),
    ("DISTRIBUCION", "DISTRIBUCIÓN"), ("distribucion", "distribución"),
    ("Documentacion", "Documentación"), ("Dotacion", "Dotación"), ("dotacion", "dotación"),
    ("duracion", "duración"), ("Duracion", "Duración"), ("DESVIO", "DESVÍO"),
    ("economicas", "económicas"), ("electrico", "eléctrico"), ("elevacion", "elevación"),
    ("ENERGIA", "ENERGÍA"), ("energia", "energía"), ("escalon", "escalón"),
    ("Especificacion", "Especificación"), ("estabilizacion", "estabilización"),
    ("Estabilizacion", "Estabilización"), ("estan", "están"),
    ("estanteria", "estantería"), ("estanterias", "estanterías"),
    ("evacuacion", "evacuación"), ("fisica", "física"),
    ("gestion", "gestión"), ("grafica", "gráfica"),
    ("habil", "hábil"), ("habiles", "hábiles"), ("Habilitacion", "Habilitación"),
    ("iluminacion", "iluminación"), ("imagenes", "imágenes"), ("indice", "índice"),
    ("Informacion", "Información"), ("instalacion", "instalación"),
    ("integracion", "integración"), ("Integracion", "Integración"), ("integramente", "íntegramente"),
    ("jerarquia", "jerarquía"),
    ("Lamina", "Lámina"), ("lamina", "lámina"), ("laminas", "láminas"),
    ("limite", "límite"), ("linea", "línea"), ("LINEA", "LÍNEA"), ("lineas", "líneas"),
    ("max", "máx"), ("maxima", "máxima"), ("mecanicos", "mecánicos"), ("Medicion", "Medición"),
    ("metalica", "metálica"), ("Metodo", "Método"), ("Migracion", "Migración"),
    ("minima", "mínima"), ("minimo", "mínimo"), ("Minimo", "Mínimo"), ("minimos", "mínimos"),
    ("modulo", "módulo"), ("movil", "móvil"),
    ("ningun", "ningún"), ("notacion", "notación"),
    ("operacion", "operación"), ("optica", "óptica"), ("OPTICA", "ÓPTICA"),
    ("ordenes", "órdenes"), ("organizacion", "organización"),
    ("padron", "padrón"), ("PANOL", "PAÑOL"), ("panol", "pañol"), ("peaton", "peatón"),
    ("PERIMETRO", "PERÍMETRO"), ("Planificacion", "Planificación"), ("posicion", "posición"),
    ("practicas", "prácticas"), ("Practico", "Práctico"), ("prevencion", "prevención"),
    ("produccion", "producción"), ("Programacion", "Programación"),
    ("proteccion", "protección"), ("PROTECCION", "PROTECCIÓN"), ("proyeccion", "proyección"),
    ("publica", "pública"),
    ("Relacion", "Relación"), ("relevo", "relevó"), ("reunion", "reunión"),
    ("rotacion", "rotación"),
    ("segun", "según"), ("Seleccion", "Selección"), ("senalero", "señalero"),
    ("senalizacion", "señalización"), ("Senalizacion", "Señalización"),
    ("senalizada", "señalizada"), ("senalizadas", "señalizadas"),
    ("SENALIZADO", "SEÑALIZADO"), ("senalizado", "señalizado"),
    ("SIMBOLOGIA", "SIMBOLOGÍA"), ("simbologia", "simbología"),
    ("SUBTERRANEA", "SUBTERRÁNEA"), ("subterranea", "subterránea"),
    ("supervision", "supervisión"), ("Suspension", "Suspensión"),
    ("tardias", "tardías"), ("tardio", "tardío"),
    ("TECNICA", "TÉCNICA"), ("tecnica", "técnica"), ("tecnicas", "técnicas"),
    ("tecnico", "técnico"), ("TECNICO", "TÉCNICO"), ("TECNICOS", "TÉCNICOS"),
    ("tecnicos", "técnicos"), ("Tecnologica", "Tecnológica"),
    ("transicion", "transición"), ("TRANSITO", "TRÁNSITO"), ("transito", "tránsito"),
    ("transmision", "transmisión"), ("TRIPODE", "TRÍPODE"), ("tripode", "trípode"),
    ("unico", "único"), ("UNICO", "ÚNICO"),
    ("vehiculo", "vehículo"), ("VEHICULO", "VEHÍCULO"),
    ("VEHICULOS", "VEHÍCULOS"), ("vehiculos", "vehículos"),
    ("VENTILACION", "VENTILACIÓN"), ("ventilacion", "ventilación"), ("Ventilacion", "Ventilación"),
    ("Verificacion", "Verificación"), ("verificacion", "verificación"),
    ("via", "vía"), ("vigia", "vigía"), ("VIGIA", "VIGÍA"),
]
# las mas largas primero, para que "criticas" no se resuelva como "critica"+"s"
PARES.sort(key=lambda p: -len(p[0]))
RX = re.compile(r"\b(%s)\b" % "|".join(re.escape(a) for a, _ in PARES))
MAPA = dict(PARES)


def _nodo(mm):
    return ">" + RX.sub(lambda w: MAPA[w.group(0)], mm.group(1)) + "<"


def acentuar(html):
    """Aplica la acentuacion a los nodos de texto, salteando <style>."""
    ini = html.find("<style>")
    fin = html.find("</style>") + len("</style>")
    cabeza, estilo, cuerpo = html[:ini], html[ini:fin], html[fin:]
    return cabeza + estilo + re.sub(r">([^<>]+)<", _nodo, cuerpo)
