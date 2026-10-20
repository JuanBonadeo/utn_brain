"""
TP 1.1 - Simulacion de una ruleta europea.

Version de Python utilizada: 3.12.

Uso:
    python simulacion_ruleta.py -c 30 -n 1000 -e 17

Parametros principales:
    -c / --corridas: cantidad de corridas independientes.
    -n / --tiradas: cantidad de tiradas por corrida.
    -e / --elegido: numero elegido para analizar aciertos, entre 0 y 36.

El programa genera 9 graficas en la carpeta indicada por --salida.
"""

import argparse
import math
import random
from pathlib import Path
from typing import List, Optional

import matplotlib.pyplot as plt


NUMEROS_RULETA = 37
MIN_NUMERO = 0
MAX_NUMERO = 36
PROBABILIDAD_ESPERADA = 1 / NUMEROS_RULETA
MEDIA_ESPERADA = (MIN_NUMERO + MAX_NUMERO) / 2
VARIANZA_ESPERADA = ((NUMEROS_RULETA**2) - 1) / 12


def parsear_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Simula una ruleta europea y genera graficas estadisticas."
    )
    parser.add_argument(
        "-c",
        "--corridas",
        type=int,
        required=True,
        help="Cantidad de corridas independientes del experimento.",
    )
    parser.add_argument(
        "-n",
        "--tiradas",
        type=int,
        required=True,
        help="Cantidad de tiradas por corrida.",
    )
    parser.add_argument(
        "-e",
        "--elegido",
        type=int,
        required=True,
        help="Numero elegido para estudiar aciertos (0 a 36).",
    )
    parser.add_argument(
        "-s",
        "--salida",
        default="graficas",
        help="Carpeta donde se guardan las graficas generadas.",
    )
    parser.add_argument(
        "--semilla",
        type=int,
        default=None,
        help="Semilla opcional para repetir exactamente la simulacion.",
    )
    parser.add_argument(
        "--mostrar",
        action="store_true",
        help="Muestra las graficas al finalizar, ademas de guardarlas.",
    )
    args = parser.parse_args()

    if args.corridas <= 0:
        parser.error("La cantidad de corridas debe ser mayor que cero.")
    if args.tiradas <= 0:
        parser.error("La cantidad de tiradas debe ser mayor que cero.")
    if not MIN_NUMERO <= args.elegido <= MAX_NUMERO:
        parser.error("El numero elegido debe estar entre 0 y 36.")

    return args


def simular_corridas(corridas: int, tiradas: int) -> List[List[int]]:
    resultados = []

    for _ in range(corridas):
        corrida = []
        for _ in range(tiradas):
            corrida.append(random.randint(MIN_NUMERO, MAX_NUMERO))
        resultados.append(corrida)

    return resultados


def frecuencia_absoluta_acumulada(corrida: List[int], elegido: int) -> List[int]:
    frecuencias = []
    aciertos = 0

    for numero in corrida:
        if numero == elegido:
            aciertos += 1
        frecuencias.append(aciertos)

    return frecuencias


def frecuencia_relativa_acumulada(corrida: List[int], elegido: int) -> List[float]:
    frecuencias = []
    aciertos = 0

    for indice, numero in enumerate(corrida, start=1):
        if numero == elegido:
            aciertos += 1
        frecuencias.append(aciertos / indice)

    return frecuencias


def media_acumulada(corrida: List[int]) -> List[float]:
    medias = []
    suma = 0

    for indice, numero in enumerate(corrida, start=1):
        suma += numero
        medias.append(suma / indice)

    return medias


def varianza_acumulada(corrida: List[int]) -> List[float]:
    varianzas = []
    suma = 0
    suma_cuadrados = 0

    for indice, numero in enumerate(corrida, start=1):
        suma += numero
        suma_cuadrados += numero**2
        media = suma / indice
        varianza = (suma_cuadrados / indice) - media**2
        varianzas.append(varianza)

    return varianzas


def desvio_estandar(valores: List[float]) -> float:
    if len(valores) < 2:
        return 0.0

    media = sum(valores) / len(valores)
    suma_cuadrados = 0.0

    for valor in valores:
        suma_cuadrados += (valor - media) ** 2

    return math.sqrt(suma_cuadrados / (len(valores) - 1))


def guardar_figura(nombre: str, salida: Path) -> None:
    ruta = salida / nombre
    plt.tight_layout()
    plt.savefig(ruta, dpi=150)


def graficar_linea(
    x: List[int],
    y: List[float],
    titulo: str,
    etiqueta_y: str,
    nombre_archivo: str,
    salida: Path,
    esperado: Optional[float] = None,
    etiqueta_esperado: str = "Valor esperado",
) -> None:
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, color="#1f77b4", linewidth=1.5)

    if esperado is not None:
        plt.axhline(
            esperado,
            color="#d62728",
            linestyle="--",
            linewidth=1.2,
            label=f"{etiqueta_esperado}: {esperado:.4f}",
        )
        plt.legend()

    plt.title(titulo)
    plt.xlabel("Numero de tirada")
    plt.ylabel(etiqueta_y)
    plt.grid(True, alpha=0.3)
    guardar_figura(nombre_archivo, salida)


def graficar_corridas_simultaneas(
    x: List[int],
    series: List[List[float]],
    titulo: str,
    etiqueta_y: str,
    nombre_archivo: str,
    salida: Path,
    esperado: Optional[float] = None,
) -> None:
    plt.figure(figsize=(10, 5))

    for indice, serie in enumerate(series, start=1):
        plt.plot(x, serie, linewidth=0.9, alpha=0.55, label=f"Corrida {indice}")

    if esperado is not None:
        plt.axhline(
            esperado,
            color="#111111",
            linestyle="--",
            linewidth=1.3,
            label=f"Esperado: {esperado:.4f}",
        )

    if len(series) <= 10:
        plt.legend(fontsize=8)
    elif esperado is not None:
        plt.legend(fontsize=8)

    plt.title(titulo)
    plt.xlabel("Numero de tirada")
    plt.ylabel(etiqueta_y)
    plt.grid(True, alpha=0.3)
    guardar_figura(nombre_archivo, salida)


def graficar_distribucion_final(
    corridas: List[List[int]], nombre_archivo: str, salida: Path
) -> None:
    conteos = [0 for _ in range(NUMEROS_RULETA)]
    total = 0

    for corrida in corridas:
        for numero in corrida:
            conteos[numero] += 1
            total += 1

    frecuencias_relativas = []
    for conteo in conteos:
        frecuencias_relativas.append(conteo / total)

    numeros = list(range(MIN_NUMERO, MAX_NUMERO + 1))

    plt.figure(figsize=(12, 5))
    plt.bar(numeros, frecuencias_relativas, color="#2ca02c", edgecolor="#1b5e20")
    plt.axhline(
        PROBABILIDAD_ESPERADA,
        color="#d62728",
        linestyle="--",
        linewidth=1.2,
        label=f"Probabilidad esperada: {PROBABILIDAD_ESPERADA:.4f}",
    )
    plt.title("Distribucion empirica final de todos los numeros")
    plt.xlabel("Numero de la ruleta")
    plt.ylabel("Frecuencia relativa")
    plt.xticks(numeros)
    plt.grid(True, axis="y", alpha=0.3)
    plt.legend()
    guardar_figura(nombre_archivo, salida)


def graficar_histograma_medias(
    corridas: List[List[int]], nombre_archivo: str, salida: Path
) -> None:
    medias_finales = []

    for corrida in corridas:
        medias_finales.append(sum(corrida) / len(corrida))

    plt.figure(figsize=(10, 5))
    plt.hist(
        medias_finales,
        bins="auto",
        color="#9467bd",
        edgecolor="#4a235a",
        alpha=0.85,
    )
    plt.axvline(
        MEDIA_ESPERADA,
        color="#d62728",
        linestyle="--",
        linewidth=1.2,
        label=f"Media esperada: {MEDIA_ESPERADA:.2f}",
    )
    plt.title("Distribucion de medias finales por corrida")
    plt.xlabel("Media final de la corrida")
    plt.ylabel("Cantidad de corridas")
    plt.grid(True, axis="y", alpha=0.3)
    plt.legend()
    guardar_figura(nombre_archivo, salida)


def generar_graficas(corridas: List[List[int]], elegido: int, salida: Path) -> None:
    tiradas = len(corridas[0])
    x = list(range(1, tiradas + 1))
    primera_corrida = corridas[0]

    fa = frecuencia_absoluta_acumulada(primera_corrida, elegido)
    fr = frecuencia_relativa_acumulada(primera_corrida, elegido)
    medias = media_acumulada(primera_corrida)
    varianzas = varianza_acumulada(primera_corrida)

    graficar_linea(
        x,
        fa,
        f"Frecuencia absoluta acumulada del numero {elegido}",
        "Frecuencia absoluta",
        "01_frecuencia_absoluta_acumulada.png",
        salida,
    )
    graficar_linea(
        x,
        fr,
        f"Frecuencia relativa acumulada del numero {elegido}",
        "Frecuencia relativa",
        "02_frecuencia_relativa_acumulada.png",
        salida,
        PROBABILIDAD_ESPERADA,
        "Probabilidad teorica",
    )
    graficar_linea(
        x,
        medias,
        "Media acumulada de los resultados",
        "Media acumulada",
        "03_media_acumulada.png",
        salida,
        MEDIA_ESPERADA,
    )
    graficar_linea(
        x,
        varianzas,
        "Varianza acumulada de los resultados",
        "Varianza acumulada",
        "04_varianza_acumulada.png",
        salida,
        VARIANZA_ESPERADA,
    )

    frecuencias_relativas = []
    medias_por_corrida = []
    varianzas_por_corrida = []

    for corrida in corridas:
        frecuencias_relativas.append(frecuencia_relativa_acumulada(corrida, elegido))
        medias_por_corrida.append(media_acumulada(corrida))
        varianzas_por_corrida.append(varianza_acumulada(corrida))

    graficar_corridas_simultaneas(
        x,
        frecuencias_relativas,
        f"Frecuencia relativa acumulada del numero {elegido} en varias corridas",
        "Frecuencia relativa",
        "05_frecuencia_relativa_varias_corridas.png",
        salida,
        PROBABILIDAD_ESPERADA,
    )
    graficar_corridas_simultaneas(
        x,
        medias_por_corrida,
        "Media acumulada en varias corridas",
        "Media acumulada",
        "06_media_varias_corridas.png",
        salida,
        MEDIA_ESPERADA,
    )
    graficar_corridas_simultaneas(
        x,
        varianzas_por_corrida,
        "Varianza acumulada en varias corridas",
        "Varianza acumulada",
        "07_varianza_varias_corridas.png",
        salida,
        VARIANZA_ESPERADA,
    )
    graficar_distribucion_final(
        corridas,
        "08_distribucion_final_numeros.png",
        salida,
    )


def imprimir_resumen(corridas: List[List[int]], elegido: int, salida: Path) -> None:
    tiradas = len(corridas[0])
    total_tiradas = len(corridas) * tiradas
    aciertos = 0
    medias_finales = []
    varianzas_finales = []

    for corrida in corridas:
        for numero in corrida:
            if numero == elegido:
                aciertos += 1
        medias_finales.append(sum(corrida) / tiradas)
        varianzas_finales.append(varianza_acumulada(corrida)[-1])

    frecuencia_relativa = aciertos / total_tiradas
    media_de_medias = sum(medias_finales) / len(medias_finales)
    media_de_varianzas = sum(varianzas_finales) / len(varianzas_finales)
    error_estandar_media = desvio_estandar(medias_finales) / math.sqrt(len(medias_finales))

    print("Simulacion finalizada")
    print(f"Corridas: {len(corridas)}")
    print(f"Tiradas por corrida: {tiradas}")
    print(f"Numero elegido: {elegido}")
    print(f"Total de tiradas: {total_tiradas}")
    print(f"Aciertos del numero elegido: {aciertos}")
    print(f"Frecuencia relativa observada: {frecuencia_relativa:.6f}")
    print(f"Probabilidad teorica: {PROBABILIDAD_ESPERADA:.6f}")
    print(f"Media observada promedio: {media_de_medias:.6f}")
    print(f"Media teorica: {MEDIA_ESPERADA:.6f}")
    print(f"Varianza observada promedio: {media_de_varianzas:.6f}")
    print(f"Varianza teorica: {VARIANZA_ESPERADA:.6f}")
    print(f"Error estandar de las medias finales: {error_estandar_media:.6f}")
    print(f"Graficas guardadas en: {salida.resolve()}")


def main() -> None:
    args = parsear_argumentos()

    if args.semilla is not None:
        random.seed(args.semilla)

    salida = Path(args.salida)
    salida.mkdir(parents=True, exist_ok=True)

    corridas = simular_corridas(args.corridas, args.tiradas)
    generar_graficas(corridas, args.elegido, salida)
    graficar_histograma_medias(corridas, "09_histograma_medias_finales.png", salida)
    imprimir_resumen(corridas, args.elegido, salida)

    if args.mostrar:
        plt.show()
    else:
        plt.close("all")


if __name__ == "__main__":
    main()
