"""Genera la versión blanco y negro (para imprimir) de la guía corta de defensa del TPI Caser.
Uso: python scripts/sim/defensa-bn.py materias/SIM/estudio/tpi-caser/defensa-corta.html materias/SIM/estudio/tpi-caser/defensa-corta-bn.html
Después: node scripts/html-to-pdf.js materias/SIM/estudio/tpi-caser/defensa-corta-bn.html"""
import sys,re
src,dst=sys.argv[1],sys.argv[2]
s=open(src,encoding='utf-8').read()
# portada -> encabezado simple
s=re.sub(r'<div class="cover">.*?\n</div>\n',
 '<div class="head"><div class="k">TPI Simulación 2026 · Grupo 10 · guía para la defensa (versión para imprimir)</div>'
 '<h1>¿Cuándo encender el horno?</h1>'
 '<p><b>La respuesta: −18 M$ por año.</b> Si el horno se apaga apenas se queda sin ULI, en lugar de esperarlo caliente hasta 48 h, '
 'la fábrica ahorra unos 18 millones de pesos por año (21,5 % de lo que cuesta operarlo). A cambio, el material espera poco más de un día extra.</p></div>\n',
 s,count=1,flags=re.S)
s=re.sub(r'<div class="photos">.*?\n</div>\n','',s,count=1,flags=re.S)
s=re.sub(r'<div class="tl" style="margin-top:6px">Una campaña típica</div>\n<div class="strip">.*?\n</div>\n',
 '<div class="mono" style="white-space:normal">Apagado → Acumulando ULI → Calentando 36 h → Procesando → Caliente sin carga ≤ 48 h → Enfriando 48 h → Apagado</div>\n',s,count=1,flags=re.S)
s=re.sub(r'<div class="tl">Ejemplo ilustrativo de un papelito.*?\n<div class="week">.*?</div></div>\n','',s,count=1,flags=re.S)
s=re.sub(r'<div class="part"></div>\n','',s)
s=re.sub(r' style="color:var\(--[a-z]+\)"','',s)
s=s.replace('🎟️ ','').replace('⚖️ ','').replace('🪙 ','')
s=s.replace('<title>TPI Caser · para la defensa</title>','<title>TPI Caser · defensa (B/N)</title>')
bn='''
/* ---- blanco y negro ---- */
:root{ --ink:#000; --muted:#444; --line:#999; --soft:#fff; --navy:#000; --hot:#000; --sal:#000; --ok:#000; --bad:#000; --blue:#000; --amber:#000; --violet:#000; }
@page{ size:A4; margin:12mm 13mm; }
body{ font-size:9.6pt; line-height:1.45; }
.head{ border:2px solid #000; border-radius:8px; padding:10px 14px; margin-bottom:6px; }
.head .k{ font-size:8pt; letter-spacing:.12em; text-transform:uppercase; color:#444; }
.head h1{ font-size:19pt; margin:2px 0 4px; } .head p{ margin:0; }
.sec{ margin:11px 0 6px; }
.sec .n{ background:#fff !important; color:#000; border:2px solid #000; width:26px; height:26px; font-size:11pt; }
.sec h2{ font-size:13pt; }
.box{ background:#fff !important; border:1px solid #000; }
.box h3{ color:#000 !important; }
.say{ border:1px dashed #000; border-left:4px solid #000; }
.crio{ border-left:4px double #000; }
.good,.warn{ border-width:1.5px; }
.stat{ border:1px solid #000; } .stat .v{ color:#000; font-size:15pt; }
.flow .b{ background:#fff; border:1.5px solid #000; } .flow .b .nm{ color:#000; } .flow .ar{ color:#000; }
table.t th{ color:#000; border-bottom:1.5px solid #000; } table.t td{ border-bottom:1px solid #bbb; }
table.t tr.hl td{ background:#fff; font-weight:650; border-top:1.5px solid #000; border-bottom:1.5px solid #000; }
.mono{ background:#fff; border:1px solid #000; }
.q{ border-left:3px solid #000; } .q b.p{ color:#000; }
.cap,.tl{ color:#444; }
'''
s=s.replace('</style>',bn+'</style>',1)
open(dst,'w',encoding='utf-8').write(s)
