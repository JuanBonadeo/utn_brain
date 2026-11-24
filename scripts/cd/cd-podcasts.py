#!/usr/bin/env python3
"""Arma las fuentes .md para generar los podcasts de CD en NotebookLM.

Cada episodio junta su parte de estudio/final/resumen-final.md y las preguntas
reales de teoría de los finales que le tocan (de banco-preguntas-teoria.md, con
la respuesta modelo). Saca las figuras, que en audio no sirven.

Uso: python3 scripts/cd/cd-podcasts.py   (regenera materias/CD/estudio/final/podcasts/)
"""
import re
from pathlib import Path

EST = Path(__file__).resolve().parents[2] / "materias/CD/estudio/final"
OUT = EST / "podcasts"


def lines(name):
    return (EST / name).read_text(encoding="utf-8").splitlines()


RES = lines("resumen-final.md")
TEO = lines("banco-preguntas-teoria.md")
EJ = lines("banco-ejercicios.md")


def clean(block):
    """Saca figuras (imagen + epígrafe), separadores y espacios de más."""
    out, skip_caption = [], False
    for l in block:
        if l.startswith("!["):
            skip_caption = True
            continue
        if skip_caption and (l.startswith("*Figura") or not l.strip()):
            if l.strip():
                skip_caption = False
            continue
        skip_caption = False
        if l.strip() == "---":
            continue
        out.append(l)
    txt = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", txt).strip("\n")


def section(doc, title):
    """Sección cuyo encabezado empieza con `title`, hasta el próximo encabezado
    de nivel igual o mayor."""
    for i, l in enumerate(doc):
        m = re.match(r"^(#+)\s+(.*)", l)
        if m and m.group(2).startswith(title):
            lvl = len(m.group(1))
            out = [l]
            for l2 in doc[i + 1:]:
                m2 = re.match(r"^(#+)\s", l2)
                if m2 and len(m2.group(1)) <= lvl:
                    break
                out.append(l2)
            return clean(out)
    raise SystemExit(f"no encontré la sección '{title}'")


def relevel(txt, top):
    """Lleva el primer encabezado del bloque al nivel `top`."""
    first = len(re.match(r"^(#+)", txt).group(1))
    return re.sub(r"^(#+)", lambda m: "#" * (len(m.group(1)) - first + top), txt, flags=re.M)


EPIS = [
    dict(
        n=1, slug="mapa-y-teoria-de-la-informacion",
        titulo="El mapa del sistema y la teoría de la información",
        foco="Primero el recorrido completo de un mensaje, de la fuente al destino, para ubicar "
             "cada tema de la materia. Después información, entropía, el canal binario simétrico, "
             "las entropías del sistema y la información mutua: qué mide cada una y cómo se "
             "relacionan. Contá el procedimiento del ejercicio del canal binario, no leas los números.",
        res=["0. Qué entra", "1. El mapa", "2. Teoría de la información"],
        teo=["1. Teoría de la información", "2. Errores de canal"],
    ),
    dict(
        n=2, slug="transmision-multinivel",
        titulo="Transmisión multinivel: M(T), información y velocidades",
        foco="La idea de mandar más de dos niveles por pulso, la receta del problema que sale en "
             "casi todos los finales (pulsos de arranque y stop, M(T), I, R) y la diferencia entre "
             "R, r y s. Explicá por qué subir los niveles aumenta la velocidad sin tocar los baudios.",
        res=["2.6 Las velocidades", "3. Transmisión multinivel"],
        teo=[],
        ej=["1. Transmisión multinivel"],
    ),
    dict(
        n=3, slug="codificacion-de-fuente",
        titulo="Codificación de fuente: Kraft, longitud media y Huffman",
        foco="La jerarquía de códigos (no singular, unívoco, instantáneo, compacto) con ejemplos, "
             "la inecuación de Kraft, la cota inferior de la longitud media y el método de Huffman. "
             "Es la pregunta de teoría que salió en todos los finales: armá la respuesta modelo "
             "en voz alta.",
        res=["4. Codificación de fuente"],
        teo=["3. Codificación de fuente"],
    ),
    dict(
        n=4, slug="deteccion-y-correccion-de-errores",
        titulo="Detección y corrección de errores: Hamming y códigos lineales",
        foco="Distancia y redundancia, Hamming por zonas, las matrices G y H, el síndrome y la "
             "familia de errores de cada síndrome. Explicá por qué el mismo síndrome lo producen "
             "también errores de orden mayor y por qué igual se corrige el más probable.",
        res=["5. Detección y corrección"],
        teo=["4. Detección y corrección"],
    ),
    dict(
        n=5, slug="modulacion",
        titulo="Modulación: AM y mensajes digitales por una red analógica",
        foco="Qué es modular, AM y sus bandas laterales, y sobre todo ASK, FSK, PSK y QAM: cómo se "
             "ve cada una, cómo se aumenta la velocidad y dónde se usa (el módem, ADSL). Es la "
             "primera pregunta de teoría del final 2025.",
        res=["6. Modulación"],
        teo=["5. Comunicaciones digitales"],
    ),
    dict(
        n=6, slug="pcm-tdm-fdm",
        titulo="Muestreo, PCM y multiplexado: TDM, FDM y ADSL",
        foco="Nyquist, las etapas de PCM, la trama TDM y su ancho de banda (el problema que sale "
             "en casi todos los finales), FDM y el reparto de frecuencias de ADSL. Aclará que hay "
             "dos criterios para el ancho de banda (1/τ y s/2) y por qué conviene declarar cuál se usa.",
        res=["7. Muestreo, PCM"],
        teo=["6. Muestreo", "7. Multiplexación"],
    ),
    dict(
        n=7, slug="medios-de-acceso",
        titulo="Medios de transmisión y cómo elegir el medio de acceso",
        foco="Par telefónico, coaxil, fibra, radioenlace y satélite: ventajas y desventajas. "
             "Después el razonamiento para elegir el medio según la zona, la velocidad, la "
             "permanencia y la segurización, con los casos que toma la cátedra. Cerrá con lo "
             "que casi no se toma (OSI, CDM, WDM) en dos minutos.",
        res=["8. Medios de transmisión", "10. Por las dudas"],
        teo=["8. Medios de transmisión"],
    ),
    dict(
        n=8, slug="colas-y-repaso-del-final",
        titulo="Teoría de colas y repaso del final",
        foco="Kendall, Little y el M/M/1 con el ejercicio de la sala de emergencias del final 2025 "
             "contado como historia, el punto de saturación del modelo cerrado y asignación de "
             "capacidad en breve. Terminá con las reglas para el examen en formato quiz: "
             "planteá la situación, esperá un momento y explicá qué conviene hacer.",
        res=["9. Teoría de colas", "0.3 Reglas para el examen"],
        teo=["9. Teoría de colas"],
    ),
]

CABECERA = """\
Fuente para un episodio de podcast de estudio. Materia: Comunicación de Datos (UTN Facultad
Regional Rosario, Ingeniería en Sistemas, 3.er año). Sirve para rendir el final: tres problemas
de práctica y tres preguntas de teoría para desarrollar. Las respuestas de las preguntas son
respuestas modelo armadas por nosotros a partir de los apuntes de la cátedra, no la corrección
oficial."""


def build(e):
    partes = [f"# Podcast CD {e['n']} de {len(EPIS)} — {e['titulo']}", CABECERA,
              "## Indicaciones para el episodio", e["foco"], "## Contenido principal"]
    partes += [relevel(section(RES, t), 3) for t in e["res"]]
    if e["teo"]:
        partes += ["## Preguntas reales de teoría de los finales, con su respuesta"]
        partes += [relevel(section(TEO, t), 3) for t in e["teo"]]
    if e.get("ej"):
        partes += ["## Ejercicios de finales sobre este tema (contar el procedimiento, no dictar números)"]
        partes += [relevel(section(EJ, t), 3) for t in e["ej"]]
    txt = "\n\n".join(partes) + "\n"
    return re.sub(r"\n{3,}", "\n\n", txt)


def main():
    OUT.mkdir(exist_ok=True)
    for e in EPIS:
        p = OUT / f"{e['n']:02d}-{e['slug']}.md"
        p.write_text(build(e), encoding="utf-8")
        print(f"{p.name}: {len(p.read_text(encoding='utf-8').split())} palabras")


if __name__ == "__main__":
    main()
