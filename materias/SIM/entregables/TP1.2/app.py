"""
Frontend web para la simulacion de la ruleta europea.
Ejecutar: python app.py
Luego abrir: http://localhost:5000
"""

from __future__ import annotations

import base64
import sys
import subprocess
from pathlib import Path

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

SCRIPT_DIR   = Path(__file__).parent
GRAFICAS_DIR = SCRIPT_DIR / 'graficas_apuestas'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/simular', methods=['POST'])
def simular():
    data = request.get_json()

    corridas     = int(data.get('corridas',    30))
    tiradas      = int(data.get('tiradas',     1000))
    estrategia   = data.get('estrategia',      'm')
    capital_tipo = data.get('capitalTipo',     'f')
    capital      = float(data.get('capital',   100))
    apuesta_min  = float(data.get('apuestaMin', 1))

    cmd = [
        sys.executable, str(SCRIPT_DIR / 'apuestas.py'),
        '-c', str(corridas),
        '-n', str(tiradas),
        '-s', estrategia,
        '-a', capital_tipo,
        '--capital',     str(capital),
        '--apuesta-min', str(apuesta_min),
        '--salida',      str(GRAFICAS_DIR),
    ]

    resultado = subprocess.run(
        cmd, capture_output=True, text=True, cwd=str(SCRIPT_DIR)
    )

    imagenes = {}
    prefijo = f'{estrategia}_{capital_tipo}'
    sufijos = [
        '01_barras_ganancias',
        '02_flujo_caja',
        '03_flujos_multiples',
    ]
    for i, sufijo in enumerate(sufijos):
        ruta = GRAFICAS_DIR / f'{prefijo}_{sufijo}.png'
        if ruta.exists():
            with open(ruta, 'rb') as f:
                imagenes[str(i)] = base64.b64encode(f.read()).decode('utf-8')

    return jsonify({
        'output':   resultado.stdout,
        'error':    resultado.stderr,
        'imagenes': imagenes,
        'ok':       resultado.returncode == 0,
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
