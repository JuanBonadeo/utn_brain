"""
TP 2.2 - Generadores de variables aleatorias con distintas distribuciones.

Uso:
    python tp2_2_simulacion.py -n 10000 --semilla 42

El programa genera valores pseudoaleatorios para distribuciones continuas y
discretas a partir de numeros uniformes U(0, 1), imprime una tabla resumen,
guarda un CSV con indicadores y produce graficas en la carpeta indicada.
"""

import argparse
import csv
import math
import random
from pathlib import Path
from typing import Callable, Dict, List, Sequence, Tuple

import matplotlib.pyplot as plt


DEFAULT_N = 10000


def parsear_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera variables aleatorias de distintas distribuciones."
    )
    parser.add_argument(
        "-n",
        "--muestras",
        type=int,
        default=DEFAULT_N,
        help="Cantidad de valores a generar por distribucion.",
    )
    parser.add_argument(
        "-s",
        "--salida",
        default="graficas_tp22",
        help="Carpeta donde se guardan las graficas.",
    )
    parser.add_argument(
        "--semilla",
        type=int,
        default=42,
        help="Semilla para reproducibilidad.",
    )
    parser.add_argument(
        "--mostrar",
        action="store_true",
        help="Muestra las graficas al terminar.",
    )
    args = parser.parse_args()

    if args.muestras <= 0:
        parser.error("La cantidad de muestras debe ser mayor que cero.")

    return args


def uniforme(n: int, a: float = 2.0, b: float = 8.0) -> List[float]:
    return [a + (b - a) * random.random() for _ in range(n)]


def exponencial(n: int, lambd: float = 1.5) -> List[float]:
    return [-math.log(1 - random.random()) / lambd for _ in range(n)]


def gamma_erlang(n: int, k: int = 3, lambd: float = 1.2) -> List[float]:
    valores = []
    for _ in range(n):
        total = 0.0
        for _ in range(k):
            total += -math.log(1 - random.random()) / lambd
        valores.append(total)
    return valores


def normal_box_muller(n: int, media: float = 10.0, desvio: float = 2.0) -> List[float]:
    valores = []
    while len(valores) < n:
        u1 = max(random.random(), 1e-12)
        u2 = random.random()
        radio = math.sqrt(-2 * math.log(u1))
        z1 = radio * math.cos(2 * math.pi * u2)
        z2 = radio * math.sin(2 * math.pi * u2)
        valores.append(media + desvio * z1)
        if len(valores) < n:
            valores.append(media + desvio * z2)
    return valores


def pascal(n: int, r: int = 4, p: float = 0.35) -> List[int]:
    valores = []
    for _ in range(n):
        exitos = 0
        fallas = 0
        while exitos < r:
            if random.random() < p:
                exitos += 1
            else:
                fallas += 1
        valores.append(fallas)
    return valores


def binomial(n: int, ensayos: int = 12, p: float = 0.4) -> List[int]:
    valores = []
    for _ in range(n):
        exitos = 0
        for _ in range(ensayos):
            if random.random() < p:
                exitos += 1
        valores.append(exitos)
    return valores


def hipergeometrica(n: int, poblacion: int = 50, exitos_poblacion: int = 18, extracciones: int = 10) -> List[int]:
    valores = []
    for _ in range(n):
        exitos_restantes = exitos_poblacion
        fracasos_restantes = poblacion - exitos_poblacion
        exitos = 0
        for _ in range(extracciones):
            total_restante = exitos_restantes + fracasos_restantes
            if random.random() < exitos_restantes / total_restante:
                exitos += 1
                exitos_restantes -= 1
            else:
                fracasos_restantes -= 1
        valores.append(exitos)
    return valores


def poisson(n: int, lambd: float = 4.0) -> List[int]:
    valores = []
    limite = math.exp(-lambd)
    for _ in range(n):
        k = 0
        producto = 1.0
        while producto > limite:
            k += 1
            producto *= random.random()
        valores.append(k - 1)
    return valores


def empirica_discreta(
    n: int,
    valores: Sequence[int] = (1, 2, 3, 4, 5),
    probabilidades: Sequence[float] = (0.10, 0.20, 0.35, 0.25, 0.10),
) -> List[int]:
    acumuladas = []
    total = 0.0
    for prob in probabilidades:
        total += prob
        acumuladas.append(total)

    muestras = []
    for _ in range(n):
        u = random.random()
        for valor, acumulada in zip(valores, acumuladas):
            if u <= acumulada:
                muestras.append(valor)
                break
    return muestras


def media(valores: Sequence[float]) -> float:
    return sum(valores) / len(valores)


def varianza_muestral(valores: Sequence[float]) -> float:
    if len(valores) < 2:
        return 0.0
    mu = media(valores)
    return sum((x - mu) ** 2 for x in valores) / (len(valores) - 1)


def normal_cdf(x: float, media_: float = 10.0, desvio: float = 2.0) -> float:
    z = (x - media_) / (desvio * math.sqrt(2))
    return 0.5 * (1 + math.erf(z))


def gamma_erlang_cdf(x: float, k: int = 3, lambd: float = 1.2) -> float:
    if x < 0:
        return 0.0
    suma = sum((lambd * x) ** i / math.factorial(i) for i in range(k))
    return 1 - math.exp(-lambd * x) * suma


def ks_continuo(valores: Sequence[float], cdf: Callable[[float], float]) -> float:
    ordenados = sorted(valores)
    n = len(ordenados)
    d_mas = max((i + 1) / n - cdf(x) for i, x in enumerate(ordenados))
    d_menos = max(cdf(x) - i / n for i, x in enumerate(ordenados))
    return max(d_mas, d_menos)


def pmf_binomial(x: int, ensayos: int = 12, p: float = 0.4) -> float:
    if x < 0 or x > ensayos:
        return 0.0
    return math.comb(ensayos, x) * (p**x) * ((1 - p) ** (ensayos - x))


def pmf_pascal(x: int, r: int = 4, p: float = 0.35) -> float:
    if x < 0:
        return 0.0
    return math.comb(r + x - 1, x) * (p**r) * ((1 - p) ** x)


def pmf_hipergeometrica(x: int, poblacion: int = 50, exitos_poblacion: int = 18, extracciones: int = 10) -> float:
    if x < 0 or x > extracciones:
        return 0.0
    if x > exitos_poblacion or extracciones - x > poblacion - exitos_poblacion:
        return 0.0
    return (
        math.comb(exitos_poblacion, x)
        * math.comb(poblacion - exitos_poblacion, extracciones - x)
        / math.comb(poblacion, extracciones)
    )


def pmf_poisson(x: int, lambd: float = 4.0) -> float:
    if x < 0:
        return 0.0
    return math.exp(-lambd) * (lambd**x) / math.factorial(x)


def pmf_empirica() -> Dict[int, float]:
    return {1: 0.10, 2: 0.20, 3: 0.35, 4: 0.25, 5: 0.10}


def chi_cuadrado_discreto(valores: Sequence[int], pmf: Callable[[int], float]) -> float:
    n = len(valores)
    minimo = min(valores)
    maximo = max(valores)
    conteos: Dict[int, int] = {}
    for valor in valores:
        conteos[valor] = conteos.get(valor, 0) + 1

    estadistico = 0.0
    for x in range(minimo, maximo + 1):
        esperado = n * pmf(x)
        if esperado >= 5:
            observado = conteos.get(x, 0)
            estadistico += ((observado - esperado) ** 2) / esperado
    return estadistico


def pdf_uniforme(x: float, a: float = 2.0, b: float = 8.0) -> float:
    return 1 / (b - a) if a <= x <= b else 0.0


def pdf_exponencial(x: float, lambd: float = 1.5) -> float:
    return lambd * math.exp(-lambd * x) if x >= 0 else 0.0


def pdf_gamma_erlang(x: float, k: int = 3, lambd: float = 1.2) -> float:
    if x < 0:
        return 0.0
    return (lambd**k) * (x ** (k - 1)) * math.exp(-lambd * x) / math.factorial(k - 1)


def pdf_normal(x: float, media_: float = 10.0, desvio: float = 2.0) -> float:
    coef = 1 / (desvio * math.sqrt(2 * math.pi))
    return coef * math.exp(-0.5 * ((x - media_) / desvio) ** 2)


def graficar_continua(
    valores: Sequence[float],
    nombre: str,
    pdf: Callable[[float], float],
    archivo: str,
    salida: Path,
) -> None:
    minimo = min(valores)
    maximo = max(valores)
    xs = [minimo + i * (maximo - minimo) / 300 for i in range(301)]
    ys = [pdf(x) for x in xs]

    plt.figure(figsize=(10, 5))
    plt.hist(valores, bins=40, density=True, alpha=0.65, color="#1f77b4", edgecolor="white", label="Simulado")
    plt.plot(xs, ys, color="#d62728", linewidth=2, label="Densidad teorica")
    plt.title(nombre)
    plt.xlabel("Valor")
    plt.ylabel("Densidad")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(salida / archivo, dpi=150)
    plt.close()


def graficar_discreta(
    valores: Sequence[int],
    nombre: str,
    pmf: Callable[[int], float],
    archivo: str,
    salida: Path,
) -> None:
    n = len(valores)
    minimo = min(valores)
    maximo = max(valores)
    xs = list(range(minimo, maximo + 1))
    conteos = {x: 0 for x in xs}
    for valor in valores:
        conteos[valor] = conteos.get(valor, 0) + 1
    observadas = [conteos.get(x, 0) / n for x in xs]
    teoricas = [pmf(x) for x in xs]

    plt.figure(figsize=(10, 5))
    plt.bar(xs, observadas, alpha=0.7, color="#2ca02c", edgecolor="#1b5e20", label="Frecuencia simulada")
    plt.plot(xs, teoricas, "o-", color="#d62728", linewidth=2, label="Probabilidad teorica")
    plt.title(nombre)
    plt.xlabel("Valor")
    plt.ylabel("Probabilidad")
    plt.grid(True, axis="y", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(salida / archivo, dpi=150)
    plt.close()


def graficar_comparacion_resumen(resultados: List[Dict[str, float]], salida: Path) -> None:
    nombres = [fila["distribucion"] for fila in resultados]
    medias_obs = [fila["media_observada"] for fila in resultados]
    medias_teo = [fila["media_teorica"] for fila in resultados]
    var_obs = [fila["varianza_observada"] for fila in resultados]
    var_teo = [fila["varianza_teorica"] for fila in resultados]
    x = list(range(len(nombres)))

    plt.figure(figsize=(12, 5))
    plt.plot(x, medias_obs, "o-", label="Media observada")
    plt.plot(x, medias_teo, "s--", label="Media teorica")
    plt.xticks(x, nombres, rotation=35, ha="right")
    plt.title("Comparacion de medias observadas y teoricas")
    plt.ylabel("Media")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(salida / "10_comparacion_medias.png", dpi=150)
    plt.close()

    plt.figure(figsize=(12, 5))
    plt.plot(x, var_obs, "o-", label="Varianza observada")
    plt.plot(x, var_teo, "s--", label="Varianza teorica")
    plt.xticks(x, nombres, rotation=35, ha="right")
    plt.title("Comparacion de varianzas observadas y teoricas")
    plt.ylabel("Varianza")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(salida / "11_comparacion_varianzas.png", dpi=150)
    plt.close()


def construir_experimentos(n: int) -> List[Dict[str, object]]:
    empirica = pmf_empirica()
    return [
        {
            "distribucion": "Uniforme",
            "tipo": "continua",
            "valores": uniforme(n),
            "media_teorica": 5.0,
            "varianza_teorica": 3.0,
            "grafica": ("01_uniforme.png", lambda v, s: graficar_continua(v, "Distribucion uniforme U(2,8)", pdf_uniforme, "01_uniforme.png", s)),
            "test": lambda v: ks_continuo(v, lambda x: 0.0 if x < 2 else 1.0 if x > 8 else (x - 2) / 6),
        },
        {
            "distribucion": "Exponencial",
            "tipo": "continua",
            "valores": exponencial(n),
            "media_teorica": 1 / 1.5,
            "varianza_teorica": 1 / (1.5**2),
            "grafica": ("02_exponencial.png", lambda v, s: graficar_continua(v, "Distribucion exponencial lambda=1.5", pdf_exponencial, "02_exponencial.png", s)),
            "test": lambda v: ks_continuo(v, lambda x: 0.0 if x < 0 else 1 - math.exp(-1.5 * x)),
        },
        {
            "distribucion": "Gamma",
            "tipo": "continua",
            "valores": gamma_erlang(n),
            "media_teorica": 3 / 1.2,
            "varianza_teorica": 3 / (1.2**2),
            "grafica": ("03_gamma.png", lambda v, s: graficar_continua(v, "Distribucion gamma/Erlang k=3, lambda=1.2", pdf_gamma_erlang, "03_gamma.png", s)),
            "test": lambda v: ks_continuo(v, gamma_erlang_cdf),
        },
        {
            "distribucion": "Normal",
            "tipo": "continua",
            "valores": normal_box_muller(n),
            "media_teorica": 10.0,
            "varianza_teorica": 4.0,
            "grafica": ("04_normal.png", lambda v, s: graficar_continua(v, "Distribucion normal N(10, 2)", pdf_normal, "04_normal.png", s)),
            "test": lambda v: ks_continuo(v, normal_cdf),
        },
        {
            "distribucion": "Pascal",
            "tipo": "discreta",
            "valores": pascal(n),
            "media_teorica": 4 * 0.65 / 0.35,
            "varianza_teorica": 4 * 0.65 / (0.35**2),
            "grafica": ("05_pascal.png", lambda v, s: graficar_discreta(v, "Distribucion de Pascal r=4, p=0.35", pmf_pascal, "05_pascal.png", s)),
            "test": lambda v: chi_cuadrado_discreto(v, pmf_pascal),
        },
        {
            "distribucion": "Binomial",
            "tipo": "discreta",
            "valores": binomial(n),
            "media_teorica": 12 * 0.4,
            "varianza_teorica": 12 * 0.4 * 0.6,
            "grafica": ("06_binomial.png", lambda v, s: graficar_discreta(v, "Distribucion binomial n=12, p=0.4", pmf_binomial, "06_binomial.png", s)),
            "test": lambda v: chi_cuadrado_discreto(v, pmf_binomial),
        },
        {
            "distribucion": "Hipergeometrica",
            "tipo": "discreta",
            "valores": hipergeometrica(n),
            "media_teorica": 10 * 18 / 50,
            "varianza_teorica": 10 * (18 / 50) * (32 / 50) * ((50 - 10) / (50 - 1)),
            "grafica": ("07_hipergeometrica.png", lambda v, s: graficar_discreta(v, "Distribucion hipergeometrica N=50, K=18, n=10", pmf_hipergeometrica, "07_hipergeometrica.png", s)),
            "test": lambda v: chi_cuadrado_discreto(v, pmf_hipergeometrica),
        },
        {
            "distribucion": "Poisson",
            "tipo": "discreta",
            "valores": poisson(n),
            "media_teorica": 4.0,
            "varianza_teorica": 4.0,
            "grafica": ("08_poisson.png", lambda v, s: graficar_discreta(v, "Distribucion de Poisson lambda=4", pmf_poisson, "08_poisson.png", s)),
            "test": lambda v: chi_cuadrado_discreto(v, pmf_poisson),
        },
        {
            "distribucion": "Empirica discreta",
            "tipo": "discreta",
            "valores": empirica_discreta(n),
            "media_teorica": sum(x * p for x, p in empirica.items()),
            "varianza_teorica": sum((x**2) * p for x, p in empirica.items()) - (sum(x * p for x, p in empirica.items()) ** 2),
            "grafica": ("09_empirica_discreta.png", lambda v, s: graficar_discreta(v, "Distribucion empirica discreta", lambda x: empirica.get(x, 0.0), "09_empirica_discreta.png", s)),
            "test": lambda v: chi_cuadrado_discreto(v, lambda x: empirica.get(x, 0.0)),
        },
    ]


def ejecutar(n: int, salida: Path) -> List[Dict[str, float]]:
    salida.mkdir(parents=True, exist_ok=True)
    experimentos = construir_experimentos(n)
    resultados = []

    for experimento in experimentos:
        valores = experimento["valores"]
        media_observada = media(valores)
        varianza_observada = varianza_muestral(valores)
        media_teorica = float(experimento["media_teorica"])
        varianza_teorica = float(experimento["varianza_teorica"])
        estadistico = float(experimento["test"](valores))

        _, graficador = experimento["grafica"]
        graficador(valores, salida)

        resultados.append(
            {
                "distribucion": str(experimento["distribucion"]),
                "tipo": str(experimento["tipo"]),
                "media_observada": media_observada,
                "media_teorica": media_teorica,
                "error_media_pct": abs(media_observada - media_teorica) / abs(media_teorica) * 100,
                "varianza_observada": varianza_observada,
                "varianza_teorica": varianza_teorica,
                "error_varianza_pct": abs(varianza_observada - varianza_teorica) / abs(varianza_teorica) * 100,
                "estadistico_ajuste": estadistico,
            }
        )

    graficar_comparacion_resumen(resultados, salida)
    return resultados


def guardar_csv(resultados: List[Dict[str, float]], salida: Path) -> None:
    ruta = salida / "resultados_tp22.csv"
    campos = [
        "distribucion",
        "tipo",
        "media_observada",
        "media_teorica",
        "error_media_pct",
        "varianza_observada",
        "varianza_teorica",
        "error_varianza_pct",
        "estadistico_ajuste",
    ]
    with ruta.open("w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resultados)


def imprimir_resumen(resultados: List[Dict[str, float]], salida: Path) -> None:
    print("Distribucion;Tipo;Media obs.;Media teor.;Error media %;Var obs.;Var teor.;Error var %;KS/Chi2")
    for fila in resultados:
        print(
            f"{fila['distribucion']};{fila['tipo']};"
            f"{fila['media_observada']:.5f};{fila['media_teorica']:.5f};"
            f"{fila['error_media_pct']:.2f};"
            f"{fila['varianza_observada']:.5f};{fila['varianza_teorica']:.5f};"
            f"{fila['error_varianza_pct']:.2f};{fila['estadistico_ajuste']:.5f}"
        )
    print(f"Graficas y CSV guardados en: {salida.resolve()}")


def main() -> None:
    args = parsear_argumentos()
    random.seed(args.semilla)
    salida = Path(args.salida)
    resultados = ejecutar(args.muestras, salida)
    guardar_csv(resultados, salida)
    imprimir_resumen(resultados, salida)

    if args.mostrar:
        plt.show()
    else:
        plt.close("all")


if __name__ == "__main__":
    main()
