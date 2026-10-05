#!/usr/bin/env python3
"""Baja / actualiza `materias/[CÓDIGO]/archivo/` desde el Drive público de la facu.

El Drive (https://drive.google.com/drive/folders/1ZgKML44drc8Wq3pcbHsc-ozPINv6xSHQ)
tiene una carpeta por materia con `Examenes/`, `Material de Cursado/`, `Resumenes/`
y `LEER.pdf`. El contenido de esa carpeta se vuelca tal cual en
`materias/[CÓDIGO]/archivo/` (ver MATERIAS abajo).

Reglas (las mismas del CLAUDE.md para `archivo/`):
  - Sólo AGREGA lo que falta. Nunca sobrescribe ni borra nada local, aunque en el
    Drive haya cambiado o desaparecido (eso se informa con --comparar).
  - No necesita login: el Drive es público. Sólo usa la biblioteca estándar, así
    que corre igual en macOS y en Windows (`python3` o `py`).

Uso:
  python3 scripts/drive-archivo.py                  # actualiza todas las materias
  python3 scripts/drive-archivo.py ICS RD           # sólo esas
  python3 scripts/drive-archivo.py --dry-run        # muestra qué bajaría, no baja
  python3 scripts/drive-archivo.py ICS --comparar   # además lista lo local que ya no está en el Drive

Al final imprime los archivos nuevos por materia: ese es el material candidato a
copiar a `fuentes/` e ingerir.
"""
import argparse
import html
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

RAIZ_DRIVE = "1ZgKML44drc8Wq3pcbHsc-ozPINv6xSHQ"  # carpeta "UTN" del Drive

# código -> (id de la carpeta de la materia en el Drive, ruta legible)
MATERIAS = {
    "ASI": ("1B2f0wTl1kiPOjN-b4exhyz3JDzuZZw9C", "4º AÑO/Administración de Sistemas de Información"),
    "ICS": ("1VJJ04eHB8hRrZriCKJ-Ha1EodwLhi2f3", "4º AÑO/Ingeniería y Calidad de Software"),
    "IO":  ("1qY_d4w0BAVVBiVDc68kslUSCluP7EkWn", "4º AÑO/Investigación Operativa"),
    "LEG": ("1kA9pJ6aVZwHTcaW2dhJQveGcnQVtAy0k", "4º AÑO/Legislación"),
    "RD":  ("1e5MZUFocfXBkwDw7E33NTQjwXQBNPBay", "4º AÑO/Redes de Datos"),
    "SIM": ("1F9-Ml_ppaLDSGrxLoO1kmz39XGxtEl-9", "4º AÑO/Simulación"),
    "TPA": ("1NhoZw0orcdC-8Aw1c9lGfrQBa5zqxSdP", "4º AÑO/Tecnologías para la Automatización"),
    "IYS": ("1V-QfFznBzNwUVzWgURqLYvRBMOq_Mxz4", "2° AÑO/Ingeniería y Sociedad"),
    "IPP": ("1ofC3BJb8651rZIN6nvlS6nesNMhdQR3l", "Electivas/Introducción a la Práctica Profesional (IPP)"),
    "SGD": ("1rGbGb7_Vspbf98t-ggGYeP08QGIGxF9n", "Electivas/Soporte a la Gestión de Datos con Programación Visual"),
}

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "Mozilla/5.0 (drive-archivo.py)"}

# Documentos nativos de Google: no tienen binario, se exportan a formato Office.
EXPORT = {
    "document": ("https://docs.google.com/document/d/{id}/export?format=docx", ".docx"),
    "spreadsheets": ("https://docs.google.com/spreadsheets/d/{id}/export?format=xlsx", ".xlsx"),
    "presentation": ("https://docs.google.com/presentation/d/{id}/export/pptx", ".pptx"),
}
DESCARGA = "https://drive.usercontent.google.com/download?id={id}&export=download&confirm=t"

ENTRADA = re.compile(
    r'<a href="([^"]+)"[^>]*>.*?<div class="flip-entry-title">(.*?)</div>', re.S)


def pedir(url, intentos=4):
    for i in range(intentos):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120)
        except (urllib.error.URLError, TimeoutError) as e:
            if i == intentos - 1:
                raise
            time.sleep(2 ** i)


def nombre_seguro(n):
    n = unicodedata.normalize("NFC", n).replace("/", "-").strip()
    if os.name == "nt":
        n = re.sub(r'[<>:"\\|?*]', "-", n).rstrip(". ")
    return n


def listar(carpeta_id):
    """Entradas directas de una carpeta pública: [(tipo, nombre, id, url_descarga)]."""
    s = pedir(f"https://drive.google.com/embeddedfolderview?id={carpeta_id}").read().decode("utf-8")
    out = []
    for href, titulo in ENTRADA.findall(s):
        nombre = nombre_seguro(html.unescape(titulo))
        m = re.search(r"/folders/([\w-]+)", href)
        if m:
            out.append(("D", nombre, m.group(1), None))
            continue
        m = re.search(r"docs\.google\.com/(document|spreadsheets|presentation)/d/([\w-]+)", href)
        if m:
            plantilla, ext = EXPORT[m.group(1)]
            if not nombre.lower().endswith(ext):
                nombre += ext
            out.append(("F", nombre, m.group(2), plantilla.format(id=m.group(2))))
            continue
        m = re.search(r"/d/([\w-]+)", href)
        if m:
            out.append(("F", nombre, m.group(1), DESCARGA.format(id=m.group(1))))
    return out


def arbol(carpeta_id, rel=""):
    """Todos los archivos bajo la carpeta: [(ruta_relativa, url)]."""
    archivos = []
    for tipo, nombre, fid, url in listar(carpeta_id):
        ruta = os.path.join(rel, nombre)
        if tipo == "D":
            archivos += arbol(fid, ruta)
        else:
            archivos.append((ruta, url))
    return archivos


def bajar(url, destino):
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    tmp = destino + ".parcial"
    with pedir(url) as r:
        if "text/html" in (r.headers.get("Content-Type") or ""):
            pagina = r.read(4096).decode("utf-8", "replace")
            if "download file" in pagina:  # "Can't download file"
                raise RuntimeError("el Drive no permite bajar este archivo (bloqueado por el "
                                   "dueño o por Google); si hace falta, abrilo a mano")
            raise RuntimeError("el Drive devolvió una página HTML en vez del archivo "
                               "(sin permiso o cuota de descarga agotada: reintentá más tarde)")
        with open(tmp, "wb") as f:
            while True:
                bloque = r.read(1 << 20)
                if not bloque:
                    break
                f.write(bloque)
    os.replace(tmp, destino)


def locales(base):
    out = set()
    for raiz, _, archivos in os.walk(base):
        for a in archivos:
            if a == ".DS_Store" or a.endswith(".parcial"):
                continue
            rel = os.path.relpath(os.path.join(raiz, a), base)
            out.add(unicodedata.normalize("NFC", rel))
    return out


def procesar(codigo, dry_run, comparar):
    carpeta, ruta_drive = MATERIAS[codigo]
    base = os.path.join(REPO, "materias", codigo, "archivo")
    print(f"\n== {codigo}  ({ruta_drive})")
    remotos = arbol(carpeta)
    ya = locales(base)
    faltan = [(r, u) for r, u in remotos if unicodedata.normalize("NFC", r) not in ya]
    print(f"  Drive: {len(remotos)} archivos · local: {len(ya)} · nuevos: {len(faltan)}")

    errores = []
    if faltan and not dry_run:
        def tarea(item):
            rel, url = item
            try:
                bajar(url, os.path.join(base, rel))
                return rel, None
            except Exception as e:  # se informa y se sigue con el resto
                return rel, str(e)
        with ThreadPoolExecutor(max_workers=4) as pool:
            for rel, err in pool.map(tarea, faltan):
                if err:
                    errores.append((rel, err))
    for rel, _ in faltan:
        marca = "x" if any(rel == e[0] for e in errores) else ("?" if dry_run else "+")
        print(f"  {marca} {rel}")
    for rel, err in errores:
        print(f"  ERROR {rel}: {err}", file=sys.stderr)

    if comparar:
        en_drive = {unicodedata.normalize("NFC", r) for r, _ in remotos}
        sobran = sorted(ya - en_drive)
        if sobran:
            print(f"  Locales que ya no están en el Drive ({len(sobran)}, no se tocan):")
            for rel in sobran:
                print(f"    - {rel}")
    return len(faltan) - len(errores), len(errores)


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("codigos", nargs="*", help="códigos de materia (default: todas)")
    p.add_argument("--dry-run", action="store_true", help="sólo mostrar qué se bajaría")
    p.add_argument("--comparar", action="store_true",
                   help="listar también lo local que ya no está en el Drive")
    a = p.parse_args()
    codigos = [c.upper() for c in a.codigos] or list(MATERIAS)
    malos = [c for c in codigos if c not in MATERIAS]
    if malos:
        p.error(f"códigos desconocidos: {', '.join(malos)} (válidos: {', '.join(MATERIAS)})")
    total = fallas = 0
    for c in codigos:
        n, e = procesar(c, a.dry_run, a.comparar)
        total += n
        fallas += e
    verbo = "a bajar" if a.dry_run else "bajados"
    print(f"\nListo: {total} archivos {verbo}" + (f", {fallas} con error" if fallas else "") + ".")
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    main()
