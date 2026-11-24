#!/usr/bin/env python3
"""Genera el audio de un listening de Inglés II a partir de una transcripción.

Usa las voces en inglés de macOS (`say`) y arma un único .m4a con varias voces.

Formato del .txt (una intervención por línea):
    # comentario                 -> se ignora
    Daniel: texto a leer         -> lo lee la voz "Daniel" (Samantha, Karen, Moira…)
    [PAUSA 30]                   -> 30 segundos de silencio

Uso:
    python3 scripts/ing2/tts-listening.py materias/ING2/estudio/final-libre/audio/sim1-part1.txt
    (deja sim1-part1.m4a al lado del .txt)

Sólo biblioteca estándar + `say` y `afconvert` (vienen con macOS).
"""
import os
import re
import subprocess
import sys
import tempfile
import wave

RATE = 22050
VELOCIDAD = "170"  # palabras por minuto: un poco más lento que el default (~185)
PAUSA_ENTRE_LINEAS = 0.7  # segundos


def silencio(segundos):
    return b"\x00\x00" * int(RATE * segundos)


def sintetizar(voz, texto, tmpdir, n):
    salida = os.path.join(tmpdir, f"{n:03d}.wav")
    subprocess.run(
        ["say", "-v", voz, "-r", VELOCIDAD, f"--data-format=LEI16@{RATE}", "-o", salida, texto],
        check=True,
    )
    with wave.open(salida, "rb") as w:
        assert w.getnchannels() == 1 and w.getsampwidth() == 2 and w.getframerate() == RATE
        return w.readframes(w.getnframes())


def main():
    if len(sys.argv) != 2:
        sys.exit("uso: tts-listening.py <transcripcion.txt>")
    origen = sys.argv[1]
    base = os.path.splitext(origen)[0]
    frames = []
    with tempfile.TemporaryDirectory() as tmp:
        for n, linea in enumerate(open(origen, encoding="utf-8")):
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            m = re.fullmatch(r"\[PAUSA (\d+(?:\.\d+)?)\]", linea)
            if m:
                frames.append(silencio(float(m.group(1))))
                continue
            voz, _, texto = linea.partition(":")
            if not texto:
                sys.exit(f"línea sin 'Voz: texto': {linea!r}")
            frames.append(sintetizar(voz.strip(), texto.strip(), tmp, n))
            frames.append(silencio(PAUSA_ENTRE_LINEAS))
        wav = os.path.join(tmp, "todo.wav")
        with wave.open(wav, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(RATE)
            w.writeframes(b"".join(frames))
        subprocess.run(["afconvert", "-f", "m4af", "-d", "aac", "-b", "64000", wav, base + ".m4a"], check=True)
    print(f"Escrito: {base}.m4a")


if __name__ == "__main__":
    main()
