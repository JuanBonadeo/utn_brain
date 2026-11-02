#!/usr/bin/env python3
"""Copia a ../3d/ las figuras 3D de la vista de MainPeatonal: cuatro personas (Pasajero) y el coche del Roca (CocheRoca).

Son recursos de la instalación de AnyLogic (ejemplo "Subway Entrance Hall" y biblioteca de la interfaz): no se
suben al repositorio público, así que cada máquina las copia de su propia instalación. Uso:
    python3 copiar_figuras_3d.py            (macOS o Windows; busca en las ubicaciones habituales)
    python3 copiar_figuras_3d.py <carpeta>  (si AnyLogic está instalado en otro lugar)
"""
import shutil, sys
from pathlib import Path

# Personas (agente Pasajero) y coche de pasajeros con su textura (agente CocheRoca, ejemplo "Railway Station").
FIGURAS = ['ped_1_m.glb', 'office_1_m.glb', 'ped_sport_2_f.glb', 'ped_3_f.glb', 'passengercar.dae', 'passengercar.jpg',
           # Equipamiento del vestíbulo y coches de la Línea C (vestibulo_3d.py), de la galería 3D del IDE.
           'turnstile_open.dae', 'cash_desk.dae', 'ticket_vending_machine_1.dae', 'subway_car.dae']
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
