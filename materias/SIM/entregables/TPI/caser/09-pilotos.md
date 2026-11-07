# TPI Caser — corridas piloto: calentamiento y número de réplicas

Corridas del 2026-11-07 con el motor mínimo de `modelo/verificar_modelo.py` (las mismas funciones del `.alp`,
que coincidieron campo por campo con AnyLogic en las 120 corridas de `CorridasE0E3`). Script:
`modelo/pilotos.py`. Gráfico: `materias/SIM/figs/tpi-caser-welch.png`.

**Decisiones:** el transitorio dura **un mes** (la primera campaña), así que los **90 días** de calentamiento
del modelo **alcanzan** y no hace falta cambiarlos. **30 réplicas alcanzan para decidir** (los nueve intervalos
de las primarias excluyen el 0 con Bonferroni), **pero no para ±10 % de precisión relativa**: eso pide entre 48
y 456 réplicas según la medida. La única excepción es el costo de E3, que ya está en 9,9 %.

## 1. Calentamiento (Welch)

### Método

- Escenarios E0 a E3 (los de `CorridasE0E3`), réplicas con semillas 1..10 (lo pedido) y 1..100 (control),
  `calentamientoModeloDias = 0`, horizonte 1.095 días (3 años). El arranque es t = 0, lunes 00:00, con la cola
  vacía y el horno apagado.
- Serie mensual: períodos de 30 días (36 meses). El motor no guarda series, así que un evento extra cada 720 h
  llama a `acumular()` y anota los acumuladores (`areaColaKg`, `horasCaliente`, `nEncendidos`, `esperas`,
  `costoTotal()`…). El valor de cada mes es la diferencia entre dos anotaciones consecutivas:
  - kg promedio en cola = Δ`areaColaKg` / 720;
  - horas a temperatura = Δ`horasCaliente`;
  - costo relevante del mes = Δ`costoTotal()` (luz marginal + gas + capital parado);
  - espera media de las ULI despachadas en el mes (solo informativa: es muy ruidosa).
- **Controles de las anotaciones**, los dos exactos:
  1. coinciden con el "truco del horizonte" (correr con `horizonteDias` = 30 k desde la misma semilla y leer los
     acumuladores al final), en 21 casos (semillas 1-3, k = 1, 2, 3, 6, 12, 24, 36): diferencia relativa 0;
  2. no cambian la corrida: la fila de resultado de 1.095 días es idéntica con y sin anotaciones, E0-E3.
- Media entre réplicas Ȳ_j, media móvil de Welch Ȳ_i(w) con w = 3 y w = 6 (Law, cap. 9: ventana centrada
  de 2w + 1 meses; los primeros w con ventanas simétricas más cortas).
- Dos criterios de corte, con la referencia = media de los meses 13 a 36:
  - **Welch**: primer mes desde el cual la media móvil queda dentro de la referencia ± máx(2 desvíos de la
    propia media móvil en los meses 13-36; 2 %);
  - **prueba sobre la serie cruda**: último de los meses 1-12 cuya media difiere de la referencia, con una
    prueba t apareada por réplica (mes j contra la media de los meses 13-36 de esa réplica), Bonferroni
    α = 0,05/12.

### Resultados (E0, 100 réplicas)

| Mes | kg en cola | % ref. | h a temperatura | % ref. | Costo (M$) | % ref. |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 4.377 | 97 % | 195,2 | **72 %** | 4,99 | **74 %** |
| 2 | 4.770 | 106 % | 257,1 | 95 % | 6,44 | 96 % |
| 3 | 4.547 | 101 % | 269,0 | 99 % | 6,67 | 99 % |
| 4 | 4.666 | 104 % | 249,9 | 92 % | 6,22 | 93 % |
| 5 | 4.319 | 96 % | 292,9 | 108 % | 7,19 | 107 % |
| 6 | 4.719 | 105 % | 264,2 | 97 % | 6,60 | 98 % |
| 13-36 (ref.) | 4.495 | 100 % | 271,3 | 100 % | 6,72 | 100 % |

Con 10 réplicas la serie es demasiado ruidosa para ver nada: el CV de un mes promedio es ~13 % en kg en cola y
horas a temperatura, del mismo orden que el transitorio. El criterio de Welch da cortes de 1 a 32 meses según
la medida y el escenario (puro ruido), y la prueba sobre la serie cruda no detecta ningún mes distinto. Law lo
contempla: si la curva no se estabiliza con n réplicas, se repite con más. Con 100 réplicas:

| Corte (meses), 100 réplicas | kg en cola | h a temperatura | Costo |
|---|---:|---:|---:|
| Welch w = 3 (E0 / E1 / E2 / E3) | 0 / 0 / 0 / 1 | 4 / 4 / 5 / 4 | 4 / 4 / 5 / 4 |
| Welch w = 6 (E0 / E1 / E2 / E3) | 1 / 0 / 1 / 2 | 7 / 7 / 7 / 7 | 7 / 6 / 7 / 7 |
| Prueba sobre la serie cruda (E0-E3) | 0 | 1 | 1 |

Con un control de 300 réplicas (fuera del script) quedan igual: mes 1 en 77-79 % de la referencia y del mes 2
en adelante entre 97 % y 103 %.

**Lectura.** Lo único que se aparta es el **mes 1**, en horas a temperatura y en costo. Arrancando vacío, la
primera campaña recién se enciende a los ~16 días (79 ULI a 4,8 por día) y llega a temperatura 36 h después, y
el mes 1 tiene un cuarto menos de horas calientes. Los kg en cola no muestran transitorio: la acumulación hasta
el umbral desde cero es la misma fase que en cualquier ciclo. Los cortes de Welch de 4-5 meses (w = 3) y
7 meses (w = 6) son el **arrastre de la ventana**, no un transitorio más largo: Ȳ_i(w) promedia los meses
i − w..i + w, así que la media móvil queda contaminada por el mes 1 hasta i = w + 1 (w = 3 → mes 4; w = 6 →
mes 7). Es exactamente lo que se ve. La serie cruda con 100 y 300 réplicas confirma que el mes 2 ya es
estacionario.

**Corte elegido: l = 1 mes (30 días).**

### Estado inicial y regeneración

- En `workConserving` el vacío de 48 h solo vence con la cola vacía (`colaAlApagarMedia` = 0 en las 120
  corridas). Cada fin de campaña es entonces un punto **casi regenerativo**: cola vacía, horno caliente sin
  carga y 48 h de enfriamiento determinista por delante. El estado del horno y de la cola se renueva. Lo que no
  se renueva es la fase del calendario: el día y la hora de la semana, la semana real sorteada en el bootstrap
  y las llegadas que quedan del día. Por eso no es regenerativo en sentido estricto.
- El estado inicial (cola vacía, horno apagado, lunes 00:00) es casi un estado típico. Equivale a un fin de
  enfriamiento sin las ~10 ULI que llegan durante esas 48 h. Por eso el sesgo inicial dura un solo ciclo (un
  ciclo dura ~28 días: 1,08 campañas por mes en E0).
- Las llegadas son semanas completas sorteadas con reposición, sin estacionalidad, así que no hay un ciclo anual
  que exija calentar un año.

### Contraste directo: ¿cambia el año medido con distintos calentamientos?

E0, 30 réplicas (semillas 1-30), 365 días medidos después de 0, 90, 180 o 365 días de calentamiento. D =
media con ese calentamiento − media con 365 días, apareado por semilla, IC 95 %.

| Medida | Sin calentamiento | 90 días (modelo) | 180 días | 365 días |
|---|---:|---:|---:|---:|
| Costo relevante del año (M$) | 80,14 (D = −2,40 ± 3,95) | 83,67 (D = +1,12 ± 4,06) | 85,02 (D = +2,47 ± 2,65) | 82,54 |
| kg promedio en cola | 4.505 (+44 ± 288) | 4.437 (−25 ± 242) | 4.510 (+49 ± 177) | 4.461 |
| Espera media (días) | 6,81 (+0,19 ± 0,49) | 6,52 (−0,10 ± 0,48) | 6,46 (−0,16 ± 0,33) | 6,62 |
| Fracción del tiempo a temperatura | 0,368 (−0,013 ± 0,020) | 0,387 (+0,006 ± 0,021) | 0,393 (+0,012 ± 0,013) | 0,381 |

Ninguna diferencia es significativa. Sin calentamiento, el costo del año sale ~2-3 % más bajo. Es lo esperable
por el mes 1, que tiene 26 % menos de costo (≈ −1,7 M$ sobre 80 M$). Con 90 días ese sesgo desaparece y el
resultado es indistinguible del de 180 o 365 días.

**Conclusión: 90 días alcanzan** (tres veces el transitorio). Se mantiene `calentamientoModeloDias = 90`. Subirlo
a 120-210 días para cubrir también el corte de la media móvil no cambiaría los resultados y alargaría cada
corrida.

## 2. Número de réplicas

Fuente: `modelo/corridas_horno_harness.csv` (30 réplicas apareadas por semilla, mismas filas que AnyLogic). Para
D = Ei − E0: h = t(29; 1 − α/2) · s_D / √30, con α = 0,05/3 (Bonferroni, primarias de `analizar_corridas.py`).
Objetivo: h ≤ 0,10 · |D̄|.
- n* = n · (h / h_objetivo)² = 30 · (h/|D̄| / 0,10)²;
- n iterativo = menor n con t(n − 1; 1 − α/2) · s_D / √n ≤ 0,10 · |D̄| (Law, ec. 9.40). Da algo menos porque
  t baja con n.

| Diferencia | Medida | D̄ | s_D | h | h/\|D̄\| | n* | n iterativo | ¿30 alcanza? |
|---|---|---:|---:|---:|---:|---:|---:|---|
| E1 − E0 | costo relevante (M$/año) | +4,83 | 3,61 | 1,68 | 34,7 % | 362 | 325 | no |
| E1 − E0 | espera media (días) | −2,57 | 0,77 | 0,36 | 13,9 % | 58 | 55 | no |
| E1 − E0 | kg promedio en cola | −1.736 | 470 | 218 | 12,6 % | 48 | 46 | no |
| E2 − E0 | costo relevante (M$/año) | +2,87 | 1,77 | 0,82 | 28,5 % | 245 | 221 | no |
| E2 − E0 | espera media (días) | −0,96 | 0,81 | 0,37 | 38,9 % | **456** | 408 | no |
| E2 − E0 | kg promedio en cola | −621 | 453 | 210 | 33,9 % | 345 | 309 | no |
| E3 − E0 | costo relevante (M$/año) | −18,00 | 3,86 | 1,79 | 9,9 % | 30 | 30 | **sí** |
| E3 − E0 | espera media (días) | +1,11 | 0,74 | 0,34 | 30,8 % | 285 | 256 | no |
| E3 − E0 | kg promedio en cola | +764 | 477 | 221 | 29,0 % | 252 | 227 | no |

Como secundarias al 95 % (informativas): energía E1/E2/E3 → n* 142 / 145 / 19; capital parado → 31 / 223 / 164.

**Decisión.**
- Para la **pregunta del estudio** (qué alternativa cambia qué y en qué sentido), 30 alcanzan: todos los
  intervalos de las primarias excluyen el 0 con Bonferroni, el más ajustado con h/|D̄| = 0,39.
- Para **±10 % de precisión relativa** en las nueve diferencias primarias hacen falta **~460 réplicas por
  escenario** (n* máx. 456; 408 con la fórmula iterativa). Lo que manda es E2 (umbral + espera máxima), cuyo
  efecto sobre la espera es chico (−0,96 días) frente al ruido.
- Intermedio: con ±20 % alcanza n* / 4 ≈ **115 réplicas**.
- Cada corrida genera ~1.800 ULI, lejos del límite de 50.000 agentes de la PLE. El costo es solo de tiempo en el
  IDE. Si se suben las réplicas, cambian `NumberOfRuns` y las expresiones `index / 30` / `index % 30` de
  `CorridasE0E3`, y el verificador (sección G y el `assert` de 120 corridas) y `analizar_corridas.py` tienen que
  acompañar.

## 3. Cómo reproducirlo

Desde la raíz del repo (Windows, ~25 s; requiere matplotlib en el venv):

```sh
.venv/Scripts/python.exe -I materias/SIM/entregables/TPI/caser/modelo/verificar_modelo.py   # regenera corridas_horno_harness.csv
.venv/Scripts/python.exe -I materias/SIM/entregables/TPI/caser/modelo/pilotos.py            # Welch, contraste, réplicas y gráfico
```

`pilotos.py` importa `extraer()` y `compilar_harness()` del verificador, compila el mismo `CaserLogicCheck` y le
suma una clase `CaserPilotos`. Esa clase arma cada escenario con las expresiones de `CorridasE0E3` y tiene tres
modos: `serie` (anotaciones mensuales), `truco` (horizonte 30 k) y `fila` (corrida común). No toca el `.alp`.
`--reps-welch N` cambia las 10 réplicas base de Welch; el control de 100 está fijo en `REPS_WELCH_LARGO`.
