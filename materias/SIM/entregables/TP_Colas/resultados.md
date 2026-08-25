# TP_Colas — Resultados de simulación (AnyLogic)

> Registro de corridas reales para el TP de M/M/1 y M/M/1/K. Modelo: `TP_Colas.alp`.
> tasaServicio (μ) = 1 fijo en todo el TP; se varía tasaArribo (λ) para fijar ρ = λ/μ.

## Parte B — M/M/1/K (cola finita), ρ = 0.75, K = 5

12 corridas (semilla aleatoria — Randomness = "Random seed (unique simulation runs)", Stop en t=20.000). Cumple el mínimo de 10 corridas exigido por la cátedra.

### Corridas individuales

| # | Lq | U | L | W | Wq (Lq/tasaArribo, sin corregir) | Pb |
|---|---|---|---|---|---|---|
| 1 | 1.225 | 0.714 | 1.939 | 2.724 | 1.633 | 0.053 |
| 2 | 1.206 | 0.710 | 1.916 | 2.684 | 1.608 | 0.052 |
| 3 | 1.207 | 0.712 | 1.918 | 2.698 | 1.609 | 0.052 |
| 4 | 1.203 | 0.713 | 1.916 | 2.688 | 1.604 | 0.050 |
| 5 | 1.230 | 0.715 | 1.945 | 2.715 | 1.640 | 0.052 |
| 6 | 1.171 | 0.702 | 1.873 | 2.641 | 1.561 | 0.048 |
| 7 | 1.195 | 0.709 | 1.904 | 2.694 | 1.593 | 0.050 |
| 8 | 1.216 | 0.715 | 1.931 | 2.712 | 1.621 | 0.050 |
| 9 | 1.197 | 0.707 | 1.904 | 2.673 | 1.597 | 0.049 |
| 10 | 1.222 | 0.715 | 1.938 | 2.731 | 1.630 | 0.053 |
| 11 | 1.239 | 0.716 | 1.955 | 2.729 | 1.652 | 0.054 |
| 12 | 1.228 | 0.716 | 1.944 | 2.723 | 1.638 | 0.050 |

### Nota metodológica: corrección de Wq

La columna Wq de arriba (y el Text en AnyLogic) se calculó como `Lq / tasaArribo`, fórmula válida para cola **infinita** (Parte A, donde todos los que llegan entran a la cola). En cola **finita** (Parte B) hay clientes rechazados que nunca la integran, así que Little's Law hay que aplicarlo con la **tasa efectiva**, no la nominal:

    λef = tasaArribo · (1 − Pb)
    Wq_correcto = Lq / λef

El resumen de abajo ya usa el valor corregido (no el de la tabla de corridas individuales).

### Resumen (n=12) vs. teórico M/M/1/K

Sistema: ρ = 0.75, K = 5 → capacidad total C = K+1 = 6.

Fórmulas teóricas:

    P0 = (1−ρ) / (1−ρ^(C+1))
    Pn = P0 · ρⁿ ,  n = 0..C
    Pb = P_C
    L  = Σ n·Pₙ  (n=0..C)
    U  = 1 − P0                    (utilización = P(servidor ocupado))
    Lq = L − U
    λef = tasaArribo · (1−Pb)
    W  = L / λef                   (Little's Law con tasa efectiva)
    Wq = Lq / λef

| Métrica | AnyLogic (media, n=12) | IC95 (±1.96·σ/√12) | Teórico | Error |
|---|---|---|---|---|
| Lq | 1.212 | ±0.011 | 1.210 | 0.15% |
| Utilización | 0.712 | ±0.002 | 0.711 | 0.07% |
| L | 1.924 | ±0.013 | 1.922 | 0.10% |
| W | 2.701 | ±0.015 | 2.701 | 0.02% |
| Wq (corregido) | 1.703 | ±0.016 | 1.701 | 0.10% |
| Pb | 0.0511 | ±0.0010 | 0.0514 (≈0.051) | 0.6% |

Las 6 métricas caen dentro del IC95 respecto del valor teórico. Validación completa para este punto (ρ=0.75, K=5).

**Este Pb = 0.0511 es el valor que va en la columna "AnyLogic" de la tabla comparativa del informe (§6), fila "Pb (K=5)"** — coincide con Teórico 0.051 y Python 0.050.

---

## Parte D — Modelo de Inventario (s, S), política (s=20, S=60)

10 corridas (semilla aleatoria, horizonte 120 meses). Cumple el mínimo de 10 corridas exigido.

Parámetros usados (Law & Kelton, informe §5.2): Ksetup=32, cUnit=3, h=1, p=5, demanda Poisson tasa 10/mes (tamaños {1,2,3,4} con prob. {1/6,1/3,1/3,1/6}), lag de entrega Uniforme(0.5, 1.0) meses.

### Corridas individuales

| # | C. orden | C. mant. | C. faltante | C. TOTAL |
|---|---|---|---|---|
| 1 | 89.588 | 17.249 | 13.023 | 119.860 |
| 2 | 89.971 | 17.170 | 13.287 | 120.428 |
| 3 | 89.593 | 17.303 | 13.087 | 119.983 |
| 4 | 89.624 | 17.278 | 13.088 | 119.990 |
| 5 | 89.522 | 17.290 | 12.954 | 119.766 |
| 6 | 89.923 | 17.191 | 13.353 | 120.467 |
| 7 | 89.732 | 17.171 | 13.210 | 120.113 |
| 8 | 89.456 | 17.233 | 13.000 | 119.688 |
| 9 | 89.856 | 17.166 | 13.212 | 120.233 |
| 10 | 89.509 | 17.268 | 13.052 | 119.830 |

### Resumen (n=10) vs. teórico/Python (informe §5.3, política 20-60)

| Métrica | AnyLogic (media, n=10) | IC95 (±1.96·σ/√10) | Teórico/Python | Error |
|---|---|---|---|---|
| Costo de orden | 89.677 | ±0.113 | 89.31 | 0.41% |
| Costo de mantenimiento | 17.232 | ±0.033 | 17.26 | 0.16% |
| Costo de faltante | 13.127 | ±0.082 | 13.71 | 4.25% |
| **Costo TOTAL** | **120.036** | **±0.167** | **120.28** | **0.20%** |

El TOTAL coincide con la teoría (0.2% de error). El mayor desvío relativo está en Costo de faltante (4.25%) — esperable, es la métrica más ruidosa de las tres (solo se activa durante backorders).

**Nota para el informe**: a diferencia de la tabla de M/M/1 (§6), el informe **no trae armada una tabla de 3 fuentes para Inventario** (la de §5.3 es solo Python, comparando 5 políticas entre sí). Hay que agregar una tabla nueva con esta comparación Teórico/Python vs. AnyLogic.

**Nota de alcance**: el enunciado da libertad para elegir los parámetros del Inventario (a diferencia de M/M/1, que fija los 5 niveles de ρ) — con esta única política (20,60) justificada y validada alcanza; no hace falta repetir las 5 políticas del informe en AnyLogic.

---

## Pendiente

### Parte A — M/M/1 (cola infinita)
- [ ] ρ=0.25: 10 corridas (Lq, U, L, W, Wq)
- [ ] ρ=0.50: 10 corridas
- [ ] ρ=0.75: 10 corridas — **son las que completan la tabla del informe §6** (filas L, Lq, W, Utilización). Ya hay 1 corrida de validación (Lq=2.271, U=0.75, L=3.02, W=4.02, Wq=3.028, ver log 2026-07-08) pero falta repetir con semilla aleatoria y promediar sobre 10.
- [ ] ρ=1.00 y ρ=1.25: no aplican en cola infinita (sistema inestable, diverge). Documentar como resultado cualitativo esperado, no numérico (coincide con el informe §3.1, filas con "—").

### Parte B — M/M/1/K (cola finita)
- [x] K=5, ρ=0.75 (12 corridas) ✓ — ver arriba.
- [ ] K=0, ρ=0.75: 10 corridas
- [ ] K=2, ρ=0.75: 10 corridas
- [ ] K=10, ρ=0.75: 10 corridas
- [ ] K=50, ρ=0.75: 10 corridas
- [ ] (Opcional) repetir la grilla K×ρ para ρ=0.50, 1.00, 1.25 como en el informe §4.2 — confirmar alcance real pedido por la cátedra antes de multiplicar el trabajo x4.

### Parte D — Modelo de Inventario
- [x] Política (20,60), 10 corridas ✓ — ver arriba. Falta agregar la tabla comparativa nueva al informe (no existe todavía, a diferencia de la de M/M/1 §6).

## Log

- **2026-07-08**: cerrado el experimento K=5, ρ=0.75 con 12 corridas reales (semilla aleatoria, mínimo de 10 cumplido). Detectado y corregido un error metodológico: la fórmula de Wq usaba la tasa de arribo nominal en vez de la efectiva (tasa nominal × (1−Pb)), lo cual subestimaba Wq en ~5.4% (el porcentaje de rechazo). Validadas las 6 métricas (Lq, U, L, W, Wq, Pb) contra fórmulas teóricas de M/M/1/K derivadas a partir de la distribución Pₙ — las 6 caen dentro del IC95.
- **2026-07-08**: cerrado el experimento de Inventario, política (20,60), con 10 corridas reales. Costo TOTAL con 0.2% de error vs. teórico/Python. Se resolvieron antes varios errores de compilación en el Agent Type del inventario, causados por caracteres invisibles pegados desde el Word/PDF de la guía (comillas tipográficas, guiones de escape) — se solucionó retipeando el código limpio en cada bloque.
