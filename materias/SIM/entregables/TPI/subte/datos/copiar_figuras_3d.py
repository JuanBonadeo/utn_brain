#!/usr/bin/env python3
"""Copia a ../3d/ las cuatro figuras humanas 3D que usa el agente Pasajero (vista 3D de MainPeatonal).

Son recursos de la instalación de AnyLogic (ejemplo "Subway Entrance Hall" y biblioteca de la interfaz): no se
suben al repositorio público, así que cada máquina las copia de su propia instalación. Uso:
    python3 copiar_figuras_3d.py            (macOS o Windows; busca en las ubicaciones habituales)
    python3 copiar_figuras_3d.py <carpeta>  (si AnyLogic está instalado en otro lugar)
"""
import shutil, sys
from pathlib import Path

FIGURAS = ['ped_1_m.glb', 'office_1_m.glb', 'ped_sport_2_f.glb', 'ped_3_f.glb']
DESTINO = Path(__file__).resolve().parent.parent / '3d'
RAICES = [Path(a) for a in sys.argv[1:]] or [
    Path('/Users/Shared/AnyLogic 8 PLE'), Path('/Applications/AnyLogic 8 PLE.app'),
    Path('C:/Program Files/AnyLogic 8.9 Personal Learning Edition'), Path('C:/Users/Public/AnyLogic 8 PLE'),
    Path.home() / 'AnyLogic 8 PLE']

DESTINO.mkdir(exist_ok=True)
for nombre in FIGURAS:
    origen = next((p for r in RAICES if r.exists() for p in r.rglob(nombre)), None)
    if origen is None:
        sys.exit(f'No encontré {nombre}: pasá la carpeta de instalación de AnyLogic como argumento.')
    shutil.copy2(origen, DESTINO / nombre)
    print(f'{nombre}  <-  {origen}')
