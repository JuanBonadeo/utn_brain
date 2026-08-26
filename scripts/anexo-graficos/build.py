# -*- coding: utf-8 -*-
"""Arma el anexo grafico de la Etapa 3 en un unico HTML listo para imprimir a PDF."""
import io, os, sys
import fig1, fig2, fig3, fig4
from acentos import acentuar

SALIDA = sys.argv[1] if len(sys.argv) > 1 else "etapa3-anexo-graficos.html"

DEFS = """
<defs>
  <marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 9 5 L 0 9 z" fill="#5B7FA6"/></marker>
  <marker id="ahC" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 9 5 L 0 9 z" fill="#B23A2E"/></marker>
  <marker id="cot" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto">
    <path d="M 5 0 L 5 10" stroke="#C8901F" stroke-width="1.6"/></marker>
  <marker id="veh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse">
    <path d="M 0 1 L 9 5 L 0 9 z" fill="#5B7FA6"/></marker>
  <marker id="evac" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
    <path d="M 0 1 L 9 5 L 0 9 z" fill="#2E7D5B"/></marker>
  <marker id="amb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
    <path d="M 0 1 L 9 5 L 0 9 z" fill="#1F6FB2"/></marker>
</defs>
"""

CSS = """
@page { size: A3 landscape; margin: 9mm; }
* { box-sizing: border-box; }
html, body { margin:0; padding:0; background:#FFFFFF; }
body { font-family:'Lexend','Segoe UI',Arial,Helvetica,sans-serif; color:#15406B; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.hoja { width:100%; height:279mm; display:flex; flex-direction:column; page-break-after:always; break-after:page; overflow:hidden; }
.hoja:last-child { page-break-after:auto; break-after:auto; }
.lamina { flex:1 1 auto; min-height:0; display:flex; }
.lamina svg { width:100%; height:100%; display:block; }
.rotulo { flex:0 0 auto; border-top:1.2px solid #15406B; margin-top:3mm; padding-top:2mm;
          display:flex; justify-content:space-between; align-items:flex-end; font-size:8.2px; color:#4C6480; }
.rotulo b { color:#15406B; font-weight:600; }
.rotulo .der { text-align:right; }

/* ---- tipografia de las laminas ---- */
text { font-family:'Lexend','Segoe UI',Arial,Helvetica,sans-serif; }
text:not([fill]) { fill:#15406B; }
.figtit { font-size:21px; font-weight:700; }
.figsub { font-size:10.4px; fill:#4C6480; }
.bandtit { font-size:11.5px; font-weight:700; letter-spacing:0.09em; }
.bandsub { font-size:10px; fill:#4C6480; }
.num  { font-size:9.4px; text-anchor:middle; }
.idn  { font-size:11.6px; font-weight:700; text-anchor:middle; }
.cruce{ font-size:8.4px; font-weight:600; fill:#8A6413; text-anchor:middle; }
.legtit { font-size:9.6px; font-weight:700; letter-spacing:0.13em; fill:#4C6480; }
.legcell{ font-size:11px; font-weight:600; text-anchor:middle; }
.legid  { font-size:16px; font-weight:700; text-anchor:middle; }
.legtxt { font-size:9.6px; fill:#33506E; }
.legb   { font-weight:700; fill:#15406B; }
.legnota{ font-size:9.2px; fill:#6B7F96; font-style:italic; }
.ejed { font-size:8.6px; fill:#4C6480; text-anchor:middle; }
.ejem { font-size:8.8px; font-weight:600; fill:#8A6413; text-anchor:middle; }
.fasenum { font-size:9.6px; font-weight:700; fill:#15406B; text-anchor:middle; }
.fasenom { font-size:8.4px; font-weight:600; letter-spacing:0.07em; fill:#4C6480; text-anchor:middle; }
.gid  { font-size:9.4px; }
.gnom { font-size:9.2px; fill:#33506E; }
.gdur { font-size:8px; fill:#6B7F96; }
.hito { font-size:8.4px; font-weight:600; fill:#8A6413; }
.hpsigla { font-size:13px; font-weight:700; }
.hpnom { font-size:10px; fill:#33506E; }
.hpdat { font-size:9px; fill:#6B7F96; text-anchor:end; }
.hpesc { font-size:8px; fill:#8798A8; text-anchor:end; }
.locn { font-size:9.4px; font-weight:700; letter-spacing:0.04em; }
.locs { font-size:8.4px; fill:#4C6480; }
.ann  { font-size:9px; }
.micro { font-size:7.6px; fill:#4C6480; }
.microrojo { font-size:7.8px; font-weight:600; fill:#B23A2E; }
.notap { font-size:8.6px; fill:#4C6480; }
.cota { font-size:8.2px; font-weight:600; fill:#8A6413; }
.sim  { font-size:8.4px; font-weight:700; }
.sim2 { font-size:8px; font-weight:700; }
.acc  { font-size:9px; font-weight:700; fill:#8A6413; }
.viacap { font-size:8.6px; font-weight:600; letter-spacing:0.05em; fill:#4C6480; }
.sendacap { font-size:8.4px; font-weight:600; fill:#2E7D5B; }
.norte { font-size:12px; font-weight:700; }
.marcotit { font-size:11px; font-weight:700; letter-spacing:0.05em; }
.marcosub { font-size:8.6px; fill:#4C6480; text-anchor:end; }

/* ---- portada ---- */
.portada { flex:1 1 auto; min-height:0; padding:12mm 16mm 0 16mm; }
.portada h1 { font-size:30px; margin:0 0 4px 0; font-weight:700; letter-spacing:-0.01em; }
.portada h2 { font-size:15px; margin:0 0 22px 0; font-weight:500; color:#4C6480; }
.portada .meta { font-size:11px; color:#4C6480; margin-bottom:20px; line-height:1.65; }
.portada table { border-collapse:collapse; width:100%; font-size:11px; margin-bottom:20px; }
.portada th { background:#DCE9F7; color:#15406B; text-align:left; font-weight:600; padding:7px 10px; border:0.8px solid #C9D6E4; }
.portada td { padding:7px 10px; border:0.8px solid #E2E9F1; vertical-align:top; color:#33506E; }
.portada td.h { font-weight:600; color:#15406B; white-space:nowrap; }
.nota { font-size:10.2px; color:#4C6480; line-height:1.6; border-left:3px solid #DCE9F7; padding-left:12px; margin-bottom:14px; }
.nota b { color:#15406B; }
"""

ROTULO = """<div class="rotulo">
  <div><b>ASI &#183; Trabajo Practico Integrador 2026 &#183; Etapa 3</b> &#183; Anexo II &#8212; Documentacion grafica<br>
  UTN FRRo &#183; Comision 403 &#183; Grupo 310 &#183; Personal (Telecom Argentina) &#183; instalacion de internet con fibra optica</div>
  <div class="der"><b>%s</b><br>Hoja %d de %d &#183; escala segun lamina &#183; entrega 28/08/2026</div>
</div>"""


def hoja(svg_body, ancho, alto, titulo, n, total):
    return ('<section class="hoja"><div class="lamina">'
            '<svg viewBox="0 0 %d %d" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">%s%s</svg>'
            '</div>%s</section>' % (ancho, alto, DEFS, svg_body, ROTULO % (titulo, n, total)))


def portada(total):
    filas = [
        ("Figura 1", "Diagrama de Red del proyecto, en notacion de actividad en el nodo. Las 51 actividades de la EDT con predecesoras, duracion, fechas tempranas y tardias y holgura total; camino critico destacado.", "Punto 10 &#183; Diagrama de Red"),
        ("Figura 2.a", "Diagrama de Gantt del cronograma aplanado adoptado, con barras por actividad, camino critico destacado, holguras en trazo discontinuo e hitos de control.", "Punto 10 &#183; Diagrama de Gantt"),
        ("Figura 2.b", "Histograma de recursos por perfil sobre el mismo eje de tiempo, con la dotacion asignada a cada perfil.", "Punto 10 &#183; Histograma de recursos"),
        ("Figura 3", "Plano de la base operativa, en planta: deposito y panol, playa de carga, mesa de despacho, oficina del NOC, sala tecnica, aula, circulaciones, senalizacion y evacuacion.", "Punto 6 &#183; Plano 1"),
        ("Figura 4", "Croquis tipo de trabajo en campo: tendido aereo en via publica en planta y vista lateral, con los esquemas de camara subterranea y de domicilio del cliente.", "Punto 6 &#183; Plano 2"),
    ]
    tr = "".join('<tr><td class="h">%s</td><td>%s</td><td>%s</td></tr>' % f for f in filas)
    return ('<section class="hoja"><div class="portada">'
            '<h1>Anexo II &#8212; Documentacion grafica</h1>'
            '<h2>Trabajo Practico Integrador 2026 &#183; Etapa 3 &#183; Planificacion de un Proyecto de TI</h2>'
            '<div class="meta"><b>Universidad Tecnologica Nacional &#183; Facultad Regional Rosario</b><br>'
            'Administracion de Sistemas de Informacion &#183; Comision 403 &#183; Grupo 310<br>'
            'Empresa analizada: Personal (Telecom Argentina) &#183; Proceso critico: instalacion de internet con fibra optica<br>'
            'Proyecto: implementar una plataforma de gestion de ordenes de trabajo con aplicacion movil de campo &#183; Entrega: 28/08/2026</div>'
            '<table><tr><th style="width:9%%">Lamina</th><th>Contenido</th><th style="width:24%%">Punto del documento</th></tr>%s</table>'
            '<div class="nota"><b>Por que&#769; este anexo existe.</b> El documento principal de la Etapa 3 se genera con un conversor que no admite imagenes. '
            'Las cuatro laminas que ese documento compromete como adjuntos se presentan aqui, en archivo independiente, y se leen junto con el.</div>'
            '<div class="nota"><b>Sobre las figuras 1, 2.a y 2.b.</b> Reproducen integramente los datos de las tablas del punto 10: predecesoras, duraciones, '
            'fechas tempranas y tardias, holguras, corrimientos del aplanamiento y carga por perfil. El calculo se reproduce sobre la EDT del punto 4.3 y arroja los mismos '
            'valores publicados: 187 dias habiles a fechas tempranas, 30 actividades criticas, 192 dias habiles de duracion aplanada adoptada y 4.240 horas-persona de esfuerzo. '
            'Todas las fechas son dias habiles relativos al dia 0, que es la aprobacion del Acta de Proyecto.</div>'
            '<div class="nota"><b>Sobre las figuras 3 y 4.</b> Siguen elemento por elemento la <i>Especificacion de los planos</i> del punto 6. Se confeccionan en planta, con '
            'escala uniforme y norte indicado, y comparten una misma simbologia, cuyo detalle acompana la figura 3. Las cotas se expresan como <b>minimos de diseno supuestos, '
            'a validar con el Servicio de Higiene y Seguridad de la organizacion</b>, dado que este trabajo no relevo medidas reales de las instalaciones. La distribucion de '
            'sectores es igualmente un supuesto de trabajo: representa la base operativa tipo del proceso critico, no un relevamiento del predio.</div>'
            '</div>%s</section>' % (tr, ROTULO % ("Portada e indice de laminas", 1, total)))


def main():
    total = 6
    partes = [portada(total),
              hoja(fig1.svg() + fig1.leyenda(), 1750, 1064, "Figura 1 &#183; Diagrama de Red", 2, total),
              hoja(fig2.svg_gantt(), 1750, 1270, "Figura 2.a &#183; Diagrama de Gantt", 3, total),
              hoja(fig2.svg_histo(), 1750, 1220, "Figura 2.b &#183; Histograma de recursos", 4, total),
              hoja(fig3.svg() + '<g transform="translate(0,1040)">' + fig3.referencias() + '</g>', 1460, 1200,
                   "Figura 3 &#183; Plano de la base operativa", 5, total),
              hoja(fig4.svg(), 1750, 1180, "Figura 4 &#183; Croquis de trabajo en campo", 6, total)]
    html = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
            '<title>Anexo II - Documentacion grafica - ASI Etapa 3</title>'
            '<link rel="preconnect" href="https://fonts.googleapis.com">'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            '<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700&display=swap" rel="stylesheet">'
            '<style>%s</style></head><body>%s</body></html>' % (CSS, "".join(partes)))
    with io.open(SALIDA, "w", encoding="utf-8") as f:
        f.write(acentuar(html))
    print("escrito %s  (%d KB)" % (SALIDA, os.path.getsize(SALIDA) // 1024))


if __name__ == "__main__":
    main()
