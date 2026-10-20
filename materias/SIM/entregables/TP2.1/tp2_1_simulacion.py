import math
import os
import random
from dataclasses import dataclass

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    plt = None

try:
    from PIL import Image, ImageDraw
except ModuleNotFoundError:
    Image = None
    ImageDraw = None


N = 10000
SEED = 5731
OUT_DIR = "graficas_tp21"


def gcl(n, seed=SEED, a=1103515245, c=12345, m=2**31):
    """Generador congruencial lineal normalizado en [0, 1)."""
    x = seed
    values = []
    for _ in range(n):
        x = (a * x + c) % m
        values.append(x / m)
    return values


def cuadrados_medios(n, seed=5731, digits=4):
    """Metodo de los cuadrados medios normalizado en [0, 1)."""
    x = seed
    values = []
    modulus = 10**digits
    for _ in range(n):
        square = str(x * x).zfill(2 * digits)
        start = (len(square) - digits) // 2
        x = int(square[start:start + digits])
        values.append(x / modulus)
    return values


def python_random(n, seed=SEED):
    rng = random.Random(seed)
    return [rng.random() for _ in range(n)]


def mean(values):
    return sum(values) / len(values)


def sample_variance(values):
    mu = mean(values)
    return sum((x - mu) ** 2 for x in values) / (len(values) - 1)


@dataclass
class TestResult:
    value: float
    limit: str
    passed: bool


def test_media(values):
    n = len(values)
    z = abs(mean(values) - 0.5) / math.sqrt((1 / 12) / n)
    return TestResult(z, "< 1.96", z < 1.96)


def test_varianza(values):
    n = len(values)
    statistic = (n - 1) * sample_variance(values) / (1 / 12)
    z = abs(statistic - (n - 1)) / math.sqrt(2 * (n - 1))
    return TestResult(z, "< 1.96", z < 1.96)


def test_chi_cuadrado(values, bins=10):
    n = len(values)
    expected = n / bins
    counts = [0] * bins
    for value in values:
        index = min(int(value * bins), bins - 1)
        counts[index] += 1
    statistic = sum((observed - expected) ** 2 / expected for observed in counts)
    return TestResult(statistic, "< 16.919", statistic < 16.919)


def test_kolmogorov_smirnov(values):
    n = len(values)
    ordered = sorted(values)
    d_plus = max((i + 1) / n - x for i, x in enumerate(ordered))
    d_minus = max(x - i / n for i, x in enumerate(ordered))
    d = max(d_plus, d_minus)
    critical = 1.36 / math.sqrt(n)
    return TestResult(d, f"< {critical:.5f}", d < critical)


def test_corridas(values):
    bits = [x >= 0.5 for x in values]
    n1 = sum(bits)
    n2 = len(bits) - n1
    runs = 1 + sum(bits[i] != bits[i - 1] for i in range(1, len(bits)))
    expected = (2 * n1 * n2) / (n1 + n2) + 1
    variance = (
        2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)
        / (((n1 + n2) ** 2) * (n1 + n2 - 1))
    )
    z = abs(runs - expected) / math.sqrt(variance)
    return TestResult(z, "< 1.96", z < 1.96)


def test_autocorrelacion(values, lag=1):
    n = len(values)
    mu = mean(values)
    numerator = sum((values[i] - mu) * (values[i + lag] - mu) for i in range(n - lag))
    denominator = sum((x - mu) ** 2 for x in values)
    rho = numerator / denominator
    z = abs(rho) * math.sqrt(n)
    return TestResult(z, "< 1.96", z < 1.96)


TESTS = {
    "Media": test_media,
    "Varianza": test_varianza,
    "Chi-cuadrado": test_chi_cuadrado,
    "Kolmogorov-Smirnov": test_kolmogorov_smirnov,
    "Corridas": test_corridas,
    "Autocorrelacion": test_autocorrelacion,
}


GENERATORS = {
    "GCL": gcl,
    "Cuadrados medios": cuadrados_medios,
    "Python random": python_random,
}


def evaluate():
    rows = []
    series = {}
    for name, generator in GENERATORS.items():
        values = generator(N)
        series[name] = values
        for test_name, test in TESTS.items():
            result = test(values)
            rows.append((name, test_name, result.value, result.limit, result.passed))
    return series, rows


def save_plots(series):
    if plt is None:
        save_plots_pillow(series)
        return

    os.makedirs(OUT_DIR, exist_ok=True)

    plt.figure(figsize=(10, 5))
    for name, values in series.items():
        plt.hist(values, bins=30, alpha=0.45, label=name)
    plt.title("Histograma comparativo de generadores")
    plt.xlabel("Valor generado")
    plt.ylabel("Frecuencia")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "histograma_generadores.png"), dpi=150)
    plt.close()

    plt.figure(figsize=(10, 5))
    for name, values in series.items():
        plt.plot(values[:200], marker=".", linestyle="-", linewidth=0.8, label=name)
    plt.title("Primeros 200 valores generados")
    plt.xlabel("Indice")
    plt.ylabel("Valor")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "primeros_valores.png"), dpi=150)
    plt.close()

    plt.figure(figsize=(10, 5))
    for name, values in series.items():
        plt.scatter(values[:-1:5], values[1::5], s=4, alpha=0.4, label=name)
    plt.title("Diagrama de dispersion $u_i$ vs. $u_{i+1}$")
    plt.xlabel("$u_i$")
    plt.ylabel("$u_{i+1}$")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "dispersion_pares.png"), dpi=150)
    plt.close()


def save_plots_pillow(series):
    if Image is None:
        print("Aviso: no esta instalado matplotlib ni Pillow; no se generaron graficas.")
        return

    os.makedirs(OUT_DIR, exist_ok=True)
    colors = {
        "GCL": (39, 119, 180),
        "Cuadrados medios": (214, 39, 40),
        "Python random": (44, 160, 44),
    }

    save_histogram_pillow(series, colors)
    save_first_values_pillow(series, colors)
    save_scatter_pillow(series, colors)


def base_canvas(title, width=1100, height=650):
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    draw.text((40, 20), title, fill="black")
    draw.rectangle((70, 70, width - 40, height - 80), outline="black")
    return image, draw


def draw_legend(draw, colors, x=760, y=25):
    for i, (name, color) in enumerate(colors.items()):
        yy = y + i * 20
        draw.rectangle((x, yy, x + 14, yy + 14), fill=color)
        draw.text((x + 20, yy - 2), name, fill="black")


def save_histogram_pillow(series, colors):
    image, draw = base_canvas("Histograma comparativo de generadores")
    width, height = image.size
    left, top, right, bottom = 70, 70, width - 40, height - 80
    bins = 30
    bar_group = (right - left) / bins

    counts_by_name = {}
    max_count = 1
    for name, values in series.items():
        counts = [0] * bins
        for value in values:
            counts[min(int(value * bins), bins - 1)] += 1
        counts_by_name[name] = counts
        max_count = max(max_count, max(counts))

    names = list(series.keys())
    for b in range(bins):
        for j, name in enumerate(names):
            count = counts_by_name[name][b]
            bar_width = bar_group / len(names)
            x0 = left + b * bar_group + j * bar_width
            x1 = x0 + bar_width * 0.85
            y1 = bottom
            y0 = bottom - (count / max_count) * (bottom - top)
            draw.rectangle((x0, y0, x1, y1), fill=colors[name])

    draw_legend(draw, colors)
    image.save(os.path.join(OUT_DIR, "histograma_generadores.png"))


def save_first_values_pillow(series, colors):
    image, draw = base_canvas("Primeros 200 valores generados")
    width, height = image.size
    left, top, right, bottom = 70, 70, width - 40, height - 80

    for name, values in series.items():
        points = []
        for i, value in enumerate(values[:200]):
            x = left + i * (right - left) / 199
            y = bottom - value * (bottom - top)
            points.append((x, y))
        draw.line(points, fill=colors[name], width=2)

    draw_legend(draw, colors)
    image.save(os.path.join(OUT_DIR, "primeros_valores.png"))


def save_scatter_pillow(series, colors):
    image, draw = base_canvas("Dispersion entre valores consecutivos")
    width, height = image.size
    left, top, right, bottom = 70, 70, width - 40, height - 80

    for name, values in series.items():
        color = colors[name]
        for i in range(0, len(values) - 1, 10):
            x = left + values[i] * (right - left)
            y = bottom - values[i + 1] * (bottom - top)
            draw.ellipse((x - 1, y - 1, x + 1, y + 1), fill=color)

    draw_legend(draw, colors)
    image.save(os.path.join(OUT_DIR, "dispersion_pares.png"))


def print_table(rows):
    print("Generador;Test;Estadistico;Criterio;Resultado")
    for generator, test_name, value, limit, passed in rows:
        status = "OK" if passed else "RECHAZA"
        print(f"{generator};{test_name};{value:.5f};{limit};{status}")


if __name__ == "__main__":
    generated, results = evaluate()
    save_plots(generated)
    print_table(results)
