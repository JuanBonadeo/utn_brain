#!/usr/bin/env python3
"""Genera el audio de un listening de Inglés II a partir de una transcripción.

Usa las voces en inglés de macOS (`say`) y arma un único .m4a con varias voces.

Formato del .txt (una intervención por línea):
    # comentario                 -> se ignora
    Daniel: texto a leer         -> lo lee la voz "Daniel" (Samantha, Karen, Moira, Tessa, Rishi…)
    [PAUSA 30]                   -> 30 segundos de silencio
    [VELOCIDAD 195]              -> palabras por minuto desde esa línea en adelante (default 170)
    [RUIDO 0.03]                 -> ruido de fondo (murmullo de aula) en todo el audio;
                                    0.02 = suave, 0.04 = molesto, 0.06 = difícil
    [HUECO 0.25]                 -> silencio entre intervenciones (default 0.7 s)

Uso:
    python3 scripts/ing2/tts-listening.py materias/ING2/estudio/final-libre/simulacro-1/audio/sim1-part1.txt
    (deja sim1-part1.m4a al lado del .txt)

Sólo biblioteca estándar + `say` y `afconvert` (vienen con macOS).
"""
import array
import os
import random
import re
import subprocess
import sys
import tempfile
import wave

RATE = 22050


def silencio(segundos):
    return array.array("h", bytes(2 * int(RATE * segundos)))


def sintetizar(voz, texto, velocidad, tmpdir, n):
    salida = os.path.join(tmpdir, f"{n:03d}.wav")
    subprocess.run(
        ["say", "-v", voz, "-r", str(velocidad), f"--data-format=LEI16@{RATE}", "-o", salida, texto],
        check=True,
    )
    with wave.open(salida, "rb") as w:
        assert w.getnchannels() == 1 and w.getsampwidth() == 2 and w.getframerate() == RATE
        muestras = array.array("h")
        muestras.frombytes(w.readframes(w.getnframes()))
        return muestras


def mezclar_ruido(muestras, nivel, semilla=7):
    """Ruido marrón (grave, tipo murmullo de aula) con leve ondulación de volumen."""
    rnd = random.Random(semilla)
    amp = nivel * 32767
    b = 0.0
    out = array.array("h", muestras)
    for i in range(len(out)):
        b = 0.985 * b + rnd.uniform(-1, 1) * 0.15
        ondula = 0.75 + 0.25 * ((i // (RATE // 2)) % 7) / 6  # sube y baja cada medio segundo
        v = out[i] + int(b * amp * 4 * ondula)
        out[i] = max(-32768, min(32767, v))
    return out


def main():
    if len(sys.argv) != 2:
        sys.exit("uso: tts-listening.py <transcripcion.txt>")
    origen = sys.argv[1]
    base = os.path.splitext(origen)[0]
    velocidad, ruido, hueco = 170, 0.0, 0.7
    pista = array.array("h")
    with tempfile.TemporaryDirectory() as tmp:
        for n, linea in enumerate(open(origen, encoding="utf-8")):
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            m = re.fullmatch(r"\[(PAUSA|VELOCIDAD|RUIDO|HUECO) (\d+(?:\.\d+)?)\]", linea)
            if m:
                clave, valor = m.group(1), float(m.group(2))
                if clave == "PAUSA":
                    pista.extend(silencio(valor))
                elif clave == "VELOCIDAD":
                    velocidad = int(valor)
                elif clave == "RUIDO":
                    ruido = valor
                else:
                    hueco = valor
                continue
            voz, _, texto = linea.partition(":")
            if not texto:
                sys.exit(f"línea sin 'Voz: texto': {linea!r}")
            pista.extend(sintetizar(voz.strip(), texto.strip(), velocidad, tmp, n))
            pista.extend(silencio(hueco))
        if ruido:
            pista = mezclar_ruido(pista, ruido)
        wav = os.path.join(tmp, "todo.wav")
        with wave.open(wav, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(RATE)
            w.writeframes(pista.tobytes())
        subprocess.run(["afconvert", "-f", "m4af", "-d", "aac", "-b", "64000", wav, base + ".m4a"], check=True)
    print(f"Escrito: {base}.m4a")


if __name__ == "__main__":
    main()
