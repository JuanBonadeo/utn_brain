#!/usr/bin/env python3
"""Equipa en 3D el vestíbulo (grupo vestibulo3D de nivelVestibulo) con objetos de la galería de AnyLogic.

Uso (desde esta carpeta, con AnyLogic cerrado):
    python3 copiar_figuras_3d.py           # copia los .dae a ../3d/ (no se suben al repo)
    python3 vestibulo_3d.py                # reemplaza/inserta el grupo y registra los recursos en el .alp

Objetos (sólo vista 3D; no cambian la simulación, que sigue usando los muros y el ServiceWithLine):
- molinetes (turnstile_open) en cada divisor de los 28 pasos: AutoScale y rotación 270°, como en el ejemplo oficial
  "Border Checkpoint";
- boletería y cabina de control (cash_desk), máquinas de carga (ticket_vending_machine_1);
- coches de la Línea C (subway_car) detenidos en las dos vías de la estación esquemática de plano_3d.py.
Los colores de cada objeto (ColorTable) se leen del propio .dae, igual que los guarda el IDE.
"""
import re, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ALP = AQUI.parent / 'SubteConstitucion.alp'
D3 = AQUI.parent / '3d'
ID0 = 1798000000000
Z_SUB, Z_RIEL_C = -46, -102                 # coherente con plano_3d.py (Z_SUB y Z_LINEA_C - 10)
OBJETOS = ['turnstile_open.dae', 'cash_desk.dae', 'ticket_vending_machine_1.dae', 'subway_car.dae']


def colores(dae):
    t = (D3 / dae).read_text(errors='ignore')
    efe = {}
    for m in re.finditer(r'<effect id="([^"]+)".*?</effect>', t, re.S):
        c = re.search(r'<diffuse>\s*<color[^>]*>([^<]+)</color>', m.group(0))
        if c:
            r, g, b = [float(x) for x in c.group(1).split()][:3]
            v = (255 << 24) | (round(r * 255) << 16) | (round(g * 255) << 8) | round(b * 255)
            efe[m.group(1)] = v - (1 << 32)
    return [(m.group(2) or m.group(1), efe.get(m.group(3), -8355712)) for m in
            re.finditer(r'<material id="([^"]+)"(?: name="([^"]+)")?>\s*<instance_effect url="#([^"]+)"', t)]


class Gen:
    def __init__(self):
        self.n, self.xml = 0, []

    def fig(self, nombre, dae, x, y, z=0, rot=0.0):
        self.n += 1
        tabla = '\n'.join(f'''						<ColorMapping>
							<Name><![CDATA[{m}]]></Name>
							<OriginalColor>{c}</OriginalColor>
						</ColorMapping>''' for m, c in colores(dae))
        self.xml.append(f'''				<Figure3D>
					<Id>{ID0 + self.n}</Id>
					<Name><![CDATA[{nombre}{self.n}]]></Name>
					<X>{x:g}</X><Y>{y:g}</Y>
					<Label><X>0</X><Y>-10</Y></Label>
					<PublicFlag>true</PublicFlag>
					<PresentationFlag>true</PresentationFlag>
					<ShowLabel>false</ShowLabel>
					<DrawMode>SHAPE_DRAW_3D</DrawMode>
					<X>{x:g}</X><Y>{y:g}</Y><Z>{z:g}</Z>
					<Label><X>0</X><Y>-10</Y></Label>
					<ResourceReference>
						<PackageName><![CDATA[subteconstitucion]]></PackageName>
						<ClassName><![CDATA[3d/{dae}]]></ClassName>
					</ResourceReference>
					<ColorTable>
{tabla}
					</ColorTable>
					<AutoScale>true</AutoScale>
					<Scale>1.0</Scale>
					<Rotation>{rot:.1f}</Rotation>
					<AxisOrder>XYZ_AXIS_ORDER</AxisOrder>
					<SelectedAnimationPose></SelectedAnimationPose>
					<ApplyShading>true</ApplyShading>
					<InternalLighting>OFF</InternalLighting>
					<IgnoreSceneLights>false</IgnoreSceneLights>
</Figure3D>''')

    def grupo(self):
        return f'''				<Group>
					<Id>{ID0}</Id>
					<Name><![CDATA[vestibulo3D]]></Name>
					<X>0</X><Y>0</Y>
					<Label><X>10</X><Y>0</Y></Label>
					<PublicFlag>true</PublicFlag>
					<PresentationFlag>true</PresentationFlag>
					<ShowLabel>false</ShowLabel>
					<DrawMode>SHAPE_DRAW_3D</DrawMode>
					<EmbeddedIcon>false</EmbeddedIcon>
					<Z>0</Z>
					<Rotation>0.0</Rotation>

			<Presentation>
{chr(10).join(self.xml)}
			</Presentation>

				</Group>'''


def main():
    faltan = [o for o in OBJETOS if not (D3 / o).exists()]
    if faltan:
        sys.exit(f'Faltan {faltan} en {D3}: corré antes python3 copiar_figuras_3d.py')
    txt = ALP.read_text(encoding='utf-8')
    g = Gen()
    # Molinetes: uno por divisor (los divisores separan los 28 pasos; X 300-316 es la línea de molinetes).
    for y in sorted(int(float(v)) for v in re.findall(
            r'<Name><!\[CDATA\[divisorMolinete\d+\]\]></Name>\s*<X>[-\d.]+</X><Y>([-\d.]+)</Y>', txt)):
        g.fig('molinete3D', 'turnstile_open.dae', 300, y, 0, 270)
    # Boletería (pared boleteria, X 95-200, Y 165-225): tres puestos mirando al vestíbulo.
    for x in (115, 145, 175):
        g.fig('boleteria3D', 'cash_desk.dae', x, 215, 0, 0)
    g.fig('cabina3D', 'cash_desk.dae', 304, 370, 0, 90)                 # cabina de control entre los molinetes
    # Máquinas de carga SUBE (pared maquinasCargaSur, X 65-150, Y 493-543), contra la pared inferior.
    for x in (92, 112, 132):
        g.fig('maquinaCarga3D', 'ticket_vending_machine_1.dae', x, 520, 0, 180)
    # Coches de la Línea C en la estación esquemática (nivel -2): Z relativo al subsuelo.
    for yc in (285, 395):
        for x in (640, 820, 1000):
            g.fig('cocheLineaC3D', 'subway_car.dae', x, yc - 13, Z_RIEL_C - Z_SUB, 0)
    grupo = g.grupo()

    previo = re.search(r'\t\t\t\t<Group>\n\t\t\t\t\t<Id>%d</Id>.*?\n\t\t\t\t</Group>' % ID0, txt, re.S)
    if previo:
        txt = txt[:previo.start()] + grupo + txt[previo.end():]
    else:
        i = txt.index('<Name><![CDATA[nivelVestibulo]]></Name>')
        j = txt.index('\n\t\t\t</Presentation>\n\n\t\t\t\t</Level>', i)
        txt = txt[:j] + '\n' + grupo + txt[j:]
    # Recursos del modelo (la carpeta 3d/ la llena copiar_figuras_3d.py).
    rid = ID0 + 900
    for o in OBJETOS:
        if f'<Path><![CDATA[3d/{o}]]></Path>' not in txt:
            rid += 1
            txt = txt.replace('\n\t</ModelResources>', f'''
		<Resource>
			<Id>{rid}</Id>
			<Path><![CDATA[3d/{o}]]></Path>
			<ReferencedFromUserCode>false</ReferencedFromUserCode>
			<Location>FILE_SYSTEM</Location>
		</Resource>
	</ModelResources>''', 1)
    ALP.write_text(txt, encoding='utf-8')
    print(f'vestibulo3D: {g.n} objetos insertados en {ALP.name}')


if __name__ == '__main__':
    main()
