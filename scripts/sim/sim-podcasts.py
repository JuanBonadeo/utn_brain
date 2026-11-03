#!/usr/bin/env python3
"""Arma las fuentes .md para generar los podcasts de SIM en NotebookLM.

Cada episodio junta: su parte de resumen-parcial1.md, ampliación de los
resúmenes por tema y del repaso de TPs, y las preguntas del banco que le tocan
(con la respuesta). Saca las figuras, que en audio no sirven.

Uso: python3 scripts/sim/sim-podcasts.py   (regenera materias/SIM/estudio/podcasts/)
"""
import re
from pathlib import Path

EST = Path(__file__).resolve().parents[2] / "materias/SIM/estudio"
OUT = EST / "podcasts"


def lines(name):
    return (EST / name).read_text(encoding="utf-8").splitlines()


RES = lines("resumen-parcial1.md")
BANCO = lines("banco-preguntas.md")


def section(src, title, *, sub_only=False):
    """Devuelve la sección cuyo encabezado empieza con `title` (hasta el próximo
    encabezado de nivel igual o mayor). Con sub_only, sin el encabezado."""
    doc = lines(src) if isinstance(src, str) else src
    for i, l in enumerate(doc):
        m = re.match(r"^(#+)\s+(.*)", l)
        if m and m.group(2).startswith(title):
            lvl = len(m.group(1))
            out = [] if sub_only else [l]
            for l2 in doc[i + 1:]:
                m2 = re.match(r"^(#+)\s", l2)
                if m2 and len(m2.group(1)) <= lvl:
                    break
                out.append(l2)
            return clean(out)
    raise SystemExit(f"no encontré la sección '{title}' en {src if isinstance(src, str) else 'resumen'}")


def clean(block):
    """Saca figuras (imagen + epígrafe), separadores y espacios de más."""
    out, skip_caption = [], False
    for l in block:
        if l.startswith("!["):
            skip_caption = True
            continue
        if skip_caption and l.startswith("*Figura"):
            skip_caption = False
            continue
        skip_caption = False
        if l.strip() == "---":
            continue
        out.append(l)
    txt = "\n".join(out)
    txt = re.sub(r"\n{3,}", "\n\n", txt).strip("\n")
    return txt


def demote(txt, n=1):
    return re.sub(r"^(#+)", lambda m: m.group(1) + "#" * n, txt, flags=re.M)


def relevel(txt, top=3):
    """Lleva el primer encabezado del bloque al nivel `top` y le saca la numeración
    del documento de origen (en la ampliación confundiría con la del resumen)."""
    first = len(re.match(r"^(#+)", txt).group(1))
    def f(m):
        lvl = len(m.group(1)) - first + top
        return "#" * lvl + " " + re.sub(r"^\d+(\.\d+)*\.?\s+", "", m.group(2))
    return re.sub(r"^(#+)\s+(.*)", f, txt, flags=re.M)


# ---------- banco ----------
def bank_blocks():
    """Preguntas 1.x, 2.x y 2b.x con su explicación, por id."""
    blocks, cur, buf = {}, None, []
    for l in BANCO:
        m = re.match(r"^\*\*(\d\.\d+|2b\.\d+) ", l)
        if m or l.startswith("## ") or l.startswith("> **Lección"):
            if cur:
                blocks[cur] = "\n".join(buf).strip()
            cur, buf = (m.group(1), [l]) if m else (None, [])
        elif cur:
            buf.append(l)
    return blocks


def bank_e():
    rows = {}
    for l in BANCO:
        m = re.match(r"^\| E(\d+) \| (.*) \| (.*) \|$", l)
        if m:
            rows[int(m.group(1))] = (m.group(2), m.group(3))
    return rows


def bank_p():
    qs, ans, cur = {}, {}, None
    in_ans = False
    for l in BANCO:
        if l.startswith("## Respuestas"):
            in_ans = True
        if in_ans:
            m = re.match(r"^\| (\d+) \| (.*?) \|(.*)\|$", l)
            if m:
                ans[int(m.group(1))] = (m.group(2), m.group(3).strip())
            continue
        m = re.match(r"^\*\*P(\d+)\)\*\* ?(.*)", l)
        if m:
            cur = int(m.group(1))
            qs[cur] = [m.group(2)]
        elif cur and l.strip() and not l.startswith("#"):
            qs[cur].append(l)
        elif cur and not l.strip():
            cur = None
    return {k: (" ".join(v), ans[k]) for k, v in qs.items()}


BB, BE, BP = bank_blocks(), bank_e(), bank_p()


def preguntas(ids):
    out = []
    for i in ids:
        if i.startswith("E"):
            q, a = BE[int(i[1:])]
            out.append(f"**{i}** (pregunta inventada por alumnos de 2025) {q}\n\n→ Respuesta: {a}")
        elif i.startswith("P"):
            q, (clave, pq) = BP[int(i[1:])]
            out.append(f"**{i}** (práctica, no oficial) {q}\n\n→ Respuesta: {clave}. {pq}".rstrip())
        else:
            tag = "parcial 2025" if not i.startswith("2b") else "parcial real, otra fecha"
            out.append(BB[i].replace(f"**{i} ", f"**{i}** ({tag}) **", 1))
    return "\n\n".join(out)


def rng(prefix, a, b):
    return [f"{prefix}{k}" for k in range(a, b + 1)]


def tp(title):
    """Subsección del TP 3, con el encabezado aclarando que es de la práctica."""
    txt = section("repaso-tps.md", title)
    return re.sub(r"^(#+)\s+[\d.]+\s+", r"\1 En el TP 3: ", txt, count=1)


# ---------- episodios ----------
EPIS = [
    dict(
        n=1, slug="que-es-simular",
        titulo="Qué es simular y cómo se encara un estudio",
        foco="Las definiciones exactas de sistema, modelo y simulación (el parcial las pregunta "
             "\"según el texto\"), cuándo conviene simular y cuándo no, los elementos de la "
             "simulación según la cátedra y los 10 pasos de Weitz frente a los de Law. Insistir "
             "en la diferencia entre verificación y validación.",
        contenido=[section(RES, "1. Qué es simular"), section(RES, "2. Los elementos"),
                   section(RES, "6. Los pasos")],
        ampliacion=[],
        preguntas=["1.4", "1.10", "1.15", "2.1", "2.2", "2.3", "2.4", "2.5", "2.7", "E13",
                   "P17", "P26", "P27", "P32"],
    ),
    dict(
        n=2, slug="eventos-discretos-cola-simple",
        titulo="El motor de eventos discretos y la cola de un servidor",
        foco="Cómo avanza el reloj (incremento fijo contra próximo evento), las piezas del motor "
             "de un simulador DES y el modelo de cola simple de Law: los dos eventos, las "
             "variables de estado y las tres medidas d(n), q(n) y u(n). Explicar la traza con "
             "palabras, sin dictar la tabla número por número.",
        contenido=[section(RES, "3. Simulación a eventos"), section(RES, "4. Modelo de cola")],
        ampliacion=[section("resumen-colas.md", "10. Las tres medidas")],
        preguntas=["1.2", "1.9", "1.11", "2.11", "2.12", "2.13", "P18", "P38", "P40"],
    ),
    dict(
        n=3, slug="inventario",
        titulo="El modelo de inventario (s, S)",
        foco="La política (s, S) con revisión periódica, por qué aparece el backlog, los tres "
             "costos y con qué nivel va cada uno, los cuatro eventos y su prioridad, y qué "
             "concluye Law al comparar las 9 políticas. Contar el procedimiento del ejercicio "
             "numérico, no leer los números. Cerrar con la diferencia con Investigación Operativa.",
        contenido=[section(RES, "5. Modelo de inventario")],
        ampliacion=[section("resumen-inventario.md", "8. La diferencia con"),
                    section("resumen-inventario.md", "9. Errores y trampas"),
                    section(BANCO, "La fórmula que tenés"),
                    tp("5.3 Inventario")],
        preguntas=["1.3", "P19", "P20", "P28", "P29", "P30"],
    ),
    dict(
        n=4, slug="colas-1",
        titulo="Teoría de colas I: Kendall, Little y M/M/1",
        foco="Las partes de un sistema de colas, la notación de Kendall, las medidas de "
             "rendimiento y las tres relaciones universales (ley de Little). El M/M/1: supuestos, "
             "por qué hace falta que ρ sea menor que 1 y qué pasa si no. Dar la intuición de las "
             "fórmulas en vez de enumerarlas.",
        contenido=[section(RES, "7. Modelos analíticos", sub_only=False).split("### 7.5")[0].rstrip()],
        ampliacion=[section("resumen-colas.md", "1. Las dos miradas"),
                    section("resumen-colas.md", "5. Las tres relaciones"),
                    section("resumen-colas.md", "Ejemplo resuelto completo"),
                    section("resumen-colas.md", "11. Errores y trampas"),
                    tp("5.1 M/M/1")],
        preguntas=["1.7", "1.8", "2.14", "2.15", "E9", "P21", "P22", "P23"],
    ),
    dict(
        n=5, slug="colas-2",
        titulo="Teoría de colas II: varios servidores, colas finitas y costos",
        foco="M/M/c con una sola cola, población finita (la tasa de llegadas baja con el estado), "
             "capacidad limitada y probabilidad de negación de servicio, M/G/c (media y desvío "
             "del servicio) y el análisis económico: cuándo conviene agregar un servidor. Usar "
             "los ejemplos resueltos como historia.",
        contenido=[section(RES, "7.5 Otros modelos")],
        ampliacion=[section("resumen-colas.md", "2.1 La población"),
                    section("resumen-colas.md", "7. Modelo M/M/c"),
                    section("resumen-colas.md", "8. Colas finitas"),
                    section("resumen-colas.md", "9. Análisis económico"),
                    tp("5.2 M/M/1/K")],
        preguntas=["1.6", "P31", "P39"],
    ),
    dict(
        n=6, slug="probabilidad",
        titulo="Probabilidad para simular (Ross cap. 2)",
        foco="Esperanza y varianza, las desigualdades de Markov y Chebyshev, la ley de los "
             "grandes números (lo que crece es n), el teorema central del límite, cuándo se usa "
             "cada distribución discreta y continua, y el proceso de Poisson homogéneo y no "
             "homogéneo. Remarcar: Poisson cuenta eventos, la exponencial mide el tiempo entre "
             "ellos.",
        contenido=[section(RES, "8. Elementos de probabilidad")],
        ampliacion=[section("resumen-probabilidad.md", "1. El vocabulario"),
                    section("resumen-probabilidad.md", "2. Axiomas"),
                    section("resumen-probabilidad.md", "4.1 El árbol").replace("familia", "familia de las distribuciones", 1),
                    section("resumen-probabilidad.md", "5. El proceso de Poisson"),
                    section("repaso-tps.md", "1. TP 1.1")],
        preguntas=["1.1", "1.5", "1.12", "1.13", "2b.2", "2b.4", "2b.7", "E6", "E7", "E15"]
                  + rng("P", 1, 16),
    ),
    dict(
        n=7, slug="numeros-aleatorios",
        titulo="Números aleatorios y generación de variables",
        foco="Verdaderos contra pseudoaleatorios, qué pide un buen generador, el congruencial "
             "lineal y el teorema de período completo, por qué fallan los cuadrados medios y "
             "RANDU, el Mersenne Twister, los dos tipos de pruebas (empíricas y teóricas) y los "
             "métodos para generar variables: transformada inversa, rechazo y composición.",
        contenido=[section(RES, "9. Números aleatorios")],
        ampliacion=[section("repaso-tps.md", "3. TP 2.1"), section("repaso-tps.md", "4. TP 2.2")],
        preguntas=["1.14", "2.9", "2.10", "2b.1", "2b.3", "2b.5", "2b.6"]
                  + ["E1", "E2", "E3", "E4", "E5", "E8", "E14", "E16", "E17", "E18", "E19",
                     "P24", "P25"],
    ),
    dict(
        n=8, slug="anylogic-y-trampas",
        titulo="AnyLogic, cultura de cátedra y las trampas del multiple choice",
        foco="Los tres paradigmas de AnyLogic y los bloques de la Process Modeling Library, las "
             "preguntas de cultura de cátedra (GIS, LaTeX, historia, POO) y, sobre todo, cómo "
             "pregunta la cátedra: las trampas típicas del multiple choice. Formato de repaso "
             "final, tipo quiz: plantear la pregunta, dar un momento y explicar la respuesta.",
        contenido=[section(RES, "Cómo se toma: lo que muestra"), section(RES, "10. AnyLogic"),
                   section(RES, "11. Las 25 trampas")],
        ampliacion=[section(BANCO, "Cómo pregunta la cátedra")],
        preguntas=["2.6", "2.8", "2.16", "2.17", "E10", "E11", "E12"] + rng("P", 33, 37),
    ),
]

CABECERA = """\
Fuente para un episodio de podcast de estudio. Materia: Simulación (UTN, Ingeniería en
Sistemas, 4.º año). Sirve para el primer parcial, el sábado 7 de noviembre de 2026: integrado
teórico-práctico y probablemente multiple choice. Las respuestas del banco son la clave revisada
por nosotros, no la corrección oficial de la cátedra."""


def build(e):
    partes = [f"# Podcast SIM {e['n']} de {len(EPIS)} — {e['titulo']}", CABECERA,
              "## Indicaciones para el episodio", e["foco"],
              "## Contenido principal"] + [demote(c) for c in e["contenido"]]
    if e["ampliacion"]:
        partes += ["## Ampliación"] + [relevel(c) for c in e["ampliacion"]]
    partes += ["## Preguntas de parcial y de práctica sobre este tema", preguntas(e["preguntas"])]
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
