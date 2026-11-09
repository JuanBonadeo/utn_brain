# IO — Mapa de parciales y finales (UTN FRRo) para el recuperatorio del 19/11/2026

Fuente: `materias/IO/archivo/Examenes/` (solo lectura). Se revisaron 25 parciales (2010–2026) y 21 finales (2012–2023).
Los finales 2012–2019 son en su mayoría **relatos de alumnos** (.txt/.pdf de foro), no el enunciado: sirven para contar temas, no para copiar datos.
Archivos de práctica que **no** son exámenes y se excluyeron del conteo: `PRACT_STOCK_hasta8.pdf`, `Practica4_…SENSIBILIDAD_DUALIDAD_2022.pdf`, `Practica5_…Transporte…_2022.pdf`, `SUP_Y_FORM_IO_3erPARCIAL.pdf`, `StockPráctica.pdf`, `StockResolución.pdf`.

Duplicados detectados (no se contaron dos veces):
- `Parciales/2010/2010-04-30.docx` = `Parciales/2015/2015-00-00.pdf` (mismo examen).
- `Parciales/2024/IMG-1.jpg` = `Parciales/2022/Recuperatorio 2 y 3/IMG_20221201_110552.jpg` (recup. parcial 3 2022, reutilizado o mal archivado).
- `Parciales/2022/3° Parcial/IMG_2022111*.jpg` = las dos fotos con nombre (md5 idéntico). 2° parcial 2022 tema 1 (2) y (3) son la misma hoja.
- `Parciales/Sin fecha/Ejercicio de parcial (Dualidad…) 1.jpg` = laboratorio LINDO de 2020-09-22 / final 2021-06-28.
- `Parciales/2020/2020-00-00.pdf` es una **resolución manuscrita** del ejercicio “fabricante de tejidos” (recup. P2 2021-11-29), no un examen.
- `Parciales/Parcial_IO_02102019.pdf` e `IO Parcial.pdf` son resoluciones manuscritas (LINDO “carga de avión” y modelización binaria de galpones/barrios).

---

## 1. Tabla de exámenes

Formato: **D** = desarrollo; **MC** = opción múltiple / “valor más cercano”; **VF** = verdadero-falso; **D+MC** = mixto.

### Parciales

| Archivo | Fecha | Ejercicios (temas) | Formato |
|---|---|---|---|
| `2010/2010-04-30.docx` (= `2015/2015-00-00.pdf`) | 2010 / 2015 | 1) 1ª tabla simplex con −M: plantear el PL, ¿es óptima?, nº máx. de soluciones · 2) “Compañía Peter” 4 prod.: tableau LINDO, interpretar solución y columna de X1 (coef. de sustitución) · 3) gráfico: región factible, Max y Min de x1+x2, detectar alternativas | D |
| `2015/2015-10-20 … Teoría Tema 2.txt` | 20/10/2015 (P2) | Teoría: valores implícitos, teorema dual, PL relajado, ficticia en el óptimo, problema de transporte | D |
| `2016/2016-06-14.jpg` | 14/06/2016 (P1) | 1) modelización (celulares, 2 segmentos) + forma estándar + gráfico + tipo de solución · 2) tabla simplex intermedia: básicas, completar, ¿óptima?, iterar, interpretar coef. y_ij · Teoría: no acotada (simplex y gráfico), condición de factibilidad, penalización, punto extremo | D |
| `2016/2016-10-04 - A1.jpg` | 04/10/2016 (P2) | 1) dual “sin simplex” (holguras complementarias) · 2) tableau LINDO (celulares) – sensibilidad | D |
| `2017/2017-04-17a.jpg` | 18/04/2017 | CPM: red y camino crítico · Teoría PERT/CPM | D |
| `2017/2017-10-03.jpg` | 03/10/2017 (P2) | 1) modelización entera (binarias, a lo sumo 3 de 4, no 1 y 4 juntos, capacidad condicional) · 2) tableau LINDO puertas: Δb (horas 85), Δc2, forzar x1, plantear dual y su solución | D |
| `2018/2018-06-14.pdf` | 14/06/2018 (P1) | 1) modelización (dentista) + gráfico + tipo de solución · 2) tabla óptima a completar + intervalo de c2 · Teoría: solución conceptual, efecto espejo, factibilidad, no acotada, nº máx. de puntos extremos | D |
| `2018/2018-10-30.pdf` (con solución) | 30/10/2018 (P3) | T1: Lagrange **restricción financiera** 3 artículos; SS → plazo de aprovisionamiento · T2: SS → LT; consumo durante el ingreso vs compra (costo unitario) · Teoría: PP, descuento excedente, PP vs RP | D |
| `2018/2018-11-01.txt` (relato) | 01/11/2018 | 1) modelización transporte con costos fijos (entera) · 2) stock básico: Q*, T*, CT, cambia i · Teoría: asignación, PL relajado, causas de stock, m+n−1 | D |
| `2019/2019-06-11 - 1° Parcial.pdf` (con solución) | 11/06/2019 (P1) | 1) modelización + forma estándar + gráfico + tipo de solución (T1 incompatible, T2 alternativas) · 2) tabla con −M a completar e iterar | D |
| `Parcial_IO_02102019.pdf` (resolución) | 02/10/2019 (P2) | Interpretación de salida LINDO (carga de avión): holguras, valores duales | D |
| `2020/2020-00-00 - 1° Parcial.pdf` (Moodle) | 2020 (P3) | P3: consumo durante el ingreso (harina): lote, PP, período · P6: PP con RF 3 % (Q, SS, costo SS) | D |
| `2020/2020-09-22 - 2° Parcial.pdf` (Moodle) | 22/09/2020 (P2) | P4: asignación (Cami/Fede) – modelizar · P5: LINDO laboratorio: ampliar 150 m², precio de P3, dual y su solución | D |
| `2020/2020-11-03 - 2° Parcial.pdf` (Moodle) | 03/11/2020 (P3/recup) | Proveedor A vs B con RF 5 % · fabricación de TV (consumo durante el ingreso): lote, CT, período | D |
| `2021/2021-02-00 - 3° Parcial.pdf` | 02/2021 (P3) | Revisión periódica (calzado, RF 3 %, Q y costo SS) · consumo durante el ingreso (lámparas) · proveedor A vs B (RF 5 %) | D |
| `2021/2021-11-04 - 3° Parcial (Com 404).pdf` | 04/11/2021 (P3) | Teoría RP (T+LT), teoría excedente con mínimo y L=0, clasificación ABC · SS → RF y costo SS · **Lagrange presupuesto 1500: ¿conviene préstamo? ¿a qué interés?** | D |
| `2021/2021-11-11 - 3° Parcial (Com 403).pdf` | 11/11/2021 (P3) | Teoría: costos de mantenimiento, λ en restricción de espacio, tabla RF = normal, costo unitario en la utilización · **Lagrange 2 artículos (40.000 u.m.) + préstamo** · PP con RF 3 % | D |
| `2021/2021-11-29 - 2° Parcial (Com 404).pdf` | 29/11/2021 (recup. P2) | VF Kruskal / árbol de expansión; MC red conexa; MC precio dual · tableau LINDO “tejidos” (con ≥): forzar x1=300, máquina a 11 u.m./h, rango c1, Δb3, dual · modelización mezcla con binarias (Acermet) · teoría transbordo, análisis paramétrico | D+MC+VF |
| `2022/1° Parcial/2022-06-23 - 1° Parcial.pdf` | 23/06/2022 (P1) | 1) Min con ≤,≥,=: forma canónica, cómo resolver, métodos, 1ª tabla · 2) tabla incompleta (Max): completar, ¿óptima?, iterar, vector óptimo, básicas/no básicas, B⁻¹, graficar el modelo original · Teoría: ficticia ≠0 en el óptimo, no acotada, teoremas fundamentales, PERT | D |
| `2022/2° Parcial/…27-09-22….jpg` | 27/09/2022 (P2) | 1) modelización entera (2 productos × 3 plantas, costos fijos, lógicas) · 2) **Steelco** LINDO (con x2 ≥ 10): interpretar, Δb≥, Δb carbón / horas, rango c1, c3 para producir, nuevo acero tipo 4, dual · Teoría: transporte balanceado, ruta más corta, B&B, valor implícito | D |
| `2022/3° Parcial/2022-11-10 - *.jpg` | 10/11/2022 (P3) | 1) revisión periódica (aire acondicionado, RF 3 %) · 2) período común 2 artículos + lote práctico · Teoría: stock desperdicio, Lagrange tiempo de preparación, escalón (gráficos), consumo durante el ingreso | D |
| `2022/Recuperatorio 2 y 3/*.jpg` | 01/12/2022 | Rec. P3: revisión periódica; descuento 20 % > 2000 → período óptimo · Teoría (período común gráfico, excedente C(Q)→∞, PP vs RP ×2, Lagrange t. preparación) · Rec. P2: modelización entera (Motores SA); LINDO CD/DVD/Blu-ray (≥15): rango c1, Δb≥, c2 para producir, −85 h, dual · Teoría: transporte balanceado, B&B, cambio en c, holguras complementarias, árbol de expansión mínima | D |
| `2024/3° Parcial - Tema 1/2.jpg` + `Teoría Tema 1/2.jpg` | 2024 (P3) | 1) período común 3 artículos + gráfico de existencias · 2) **descuento 10 % ≥150**: ley de precios, ¿conviene?, cajas de 150, gráfico, T*, PP · 3) inferir μ y σ desde PP y SS; lote óptimo y costo mensual del SS · Teoría: Lagrange espacio, v vs d, CT período común, costo unitario, excedente C(Q)→∞ | D |
| `2025/2025-07-26 - 1º Parcial/*` (+ resolución Vaccaro) | 26/07/2025 (P1) | 1) **gráfico Min con preguntas de selección** (región, óptimo, punto factible, restricción activa / con holgura) · 2) pizzería: Big-M, tipo de solución, ficticia en la base, no acotada · 3) **tabla óptima con incógnitas A…K** (restaurante, con =): dual, costo reducido, rango de c3, Δb1 · Teoría: 10 preguntas | D + selección |
| `2026/2026-10-03 - Parcial (Tema 1).pdf` | 03/10/2026 (parcial único) | 1) gráfico Min 3 restricciones · 2) refinería Max con ≥, tabla intermedia: entra/sale, precio sombra, rango c_j, dual, holguras, costo reducido · 3) Lagrange financiera 2 artículos + crédito al 12 % | **MC (“valor más cercano”)** |

### Finales

| Archivo | Fecha | Práctica | Teoría (resumen) | Formato |
|---|---|---|---|---|
| `2012/2012-11-28.pdf` | 28/11/2012 | consumo durante el ingreso vs compra | gráfico PP con RF, PERT, árbol de expansión | D |
| `2013/2013-02-13*.pdf` | 13/02/2013 | LINDO (Δb, dual) · período común 4 artículos + RP con RF 3 % | PERT, costos reducidos, PP vs RP, sensib. de c, tasa i, ruta más corta | D |
| `2013/2013-08-05.pdf` | 05/08/2013 | LINDO: Δb3, Δc1, Δc2, Δb4 (≥) · PERT | dual, nueva restricción, Brooks, degenerada, ABC | D |
| `2013/2013-08-26.pdf` | 26/08/2013 | tabla: ¿óptima?, ¿única?, a_ij y b_i faltantes, dual, Δb, valor implícito, recurso escaso · CPM | 2 fases, holguras complementarias, PP vs RP, Brooks | D |
| `2013/2013-12-02.txt` | 02/12/2013 | LINDO: costo reducido, 80 unidades extra · PP con IPF 98 % | ficticia > 0, nueva variable, curva de costo mínimo, IPF vs RF, Dijkstra | D |
| `2014/2014-05-19.txt` | 19/05/2014 | escalón (lote, costo, cambio del límite) · LINDO | nueva variable, ruta más corta, costo total mínimo, tasa i, ficticias | D |
| `2014/2014-07-28.pdf` | 28/07/2014 | LINDO (recurso ocioso, costo reducido) · dual vía gráfico + holguras complementarias · excedente + PP | PERT, factibilidad, coef. sustitución, λ espacio, forma cuadrática | D |
| `2014/2014-08-25.txt` | 25/08/2014 | LINDO · RF (Q, SS, costo SS) + IPF 95 % → PP | signo valor implícito (≥ en Min), dual, λ financiera, costo directo, red/árbol | D |
| `2015/2015-00-00.pdf` | 2015 | LINDO · RF e IPF | dual, solución básica, ABC, camino crítico; deducir consumo durante ingreso | D |
| `2015/2015-03-09.txt` | 09/03/2015 | LINDO completo (precio sombra, Δb) · independiente vs conjunta | primal-dual, signo valor implícito, costos de proyecto, PP vs RP, red | D |
| `2015/2015-08-03.txt` | 03/08/2015 | modelización + gráfico · sensib. c y b · período común + RP | y_ij básicas 0/1, causas de stock, incompatibilidad, m+n−1 | D |
| `2016/2016-11-21.txt` | 21/11/2016 | modelización + gráfico · dual · período común | punto extremo, escalón, precio sombra/valor implícito, redes | D |
| `2017/2017-08-28.txt` | 28/08/2017 | Lagrange financiera · simplex | forma estándar, costos reducidos, Beta, objetivos de stock, tasa i | D |
| `2017/2017-11-27.txt` | 27/11/2017 | tabla desde la base (B⁻¹), óptimo, rango c2, Δb3, nueva variable · RF → LT | nueva variable, ruta más corta, ficticias/2 fases, costo mínimo, λ financiera, tasa i | D |
| `2018/2018-05-28.txt` | 28/05/2018 | LINDO (Δc, nueva variable) · independiente vs conjunta | coef. sustitución, PERT, consumo durante ingreso, teoremas, λ espacio | D |
| `2018/2018-08-27.txt` | 27/08/2018 | sensibilidad · RP con RF (Q, SS, costo SS) | primal-dual, solución conceptual, nivelación, PP vs RP, restricción financiera | D |
| `2019/2019-02-13.txt` | 13/02/2019 | LINDO completo (alternativas, holguras, Δb fuera de rango, dual) · **Lagrange financiera 3 artículos + interpretar λ** | entrar otro cj−zj, tipos de solución, B⁻¹ con ≥, tasa i, excedente | D |
| `2019/2019-04-29.txt` | 29/04/2019 | LINDO (sin cuentas) · PP con RF (z de tabla), costo anual | costo reducido, coef. sustitución, tipos de solución, consumo durante ingreso, PERT | D |
| `2020/2020-11-16 - Enunciado y Resolución.pdf` | 16/11/2020 | modelización binaria · tableau LINDO (contribución de P1, 80 h extra: a qué proceso, sobreprecio, efecto; dual) · RP con RF 1 % | — | D |
| `2021/2021-06-28.docx` | 28/06/2021 | LINDO laboratorio (precio P2, ampliar 150 m² a 70 u.m., dual) · modelización binaria (plantas) · PP con RF 2 % | — | D |
| `2023/2023-04-27/*.jpg` | 27/04/2023 | PP con RF (alimento gatos) · PL + dual con salida LINDO (solución dual, holgura, comprar proteína a 300) | coef. sustitución, condición de optimización, PP vs RP, CT período común | D (teoría eliminatoria) |

---

## 2. Frecuencia por tema

Conteo = cantidad de exámenes distintos (46: 25 parciales + 21 finales) en los que aparece el tema como **práctica**. La teoría va aparte.

```
Sensibilidad (LINDO o tabla)           ██████████████████████████████  29
Dualidad (plantear dual + solución)    ████████████████                16
Stock aleatorio PP (RF/IPF, SS, c.SS)  ██████████████                  14
Gráfico                                ██████████                      10
Simplex / lectura y completar tabla    █████████                        9
Modelización PL continua               ███████                          7
Entera / binaria (modelización)        ███████                          7
Período común / gestión conjunta       ███████                          7
Revisión periódica (RF)                ███████                          7
Lagrange / restricciones (financ.)     ██████                           6
Consumo durante el ingreso             █████                            5
Descuentos (escalón / excedente)       ████                             4
CPM / PERT                             ███                              3
Transporte / asignación (práctica)     ██                               2
Stock básico (EOQ puro)                ██                               2
Redes (solo teoría / VF)               ▏                                0
```

Lectura por bloque:
- **PL (gráfico + simplex + sensibilidad + dual)** es el 100 % del primer parcial y ~50 % de cada final. La pregunta estrella es la lectura de una tabla óptima (LINDO “THE TABLEAU” o tabla manual): precio sombra / valor implícito, rango de c_j, Δb_i con cambio o no de base, costo reducido de una no básica, “¿conviene comprar el recurso a X?”, “¿conviene un producto nuevo?” (columna nueva con u·A_j), dual y su solución.
- Casi siempre hay **una restricción ≥ o =** en el PL (2017, 2021-11-29, 2022 Steelco, 2022 recup, 2025 restaurante, 2026 refinería): el valor implícito sale negativo en la ≥ (en Max) y el dual tiene u ≤ 0 o libre. Es el punto donde más se resta.
- **Stock**: lo más repetido es el aleatorio con RF (PP o revisión periódica), luego período común, Lagrange y consumo durante el ingreso. Descuentos aparece menos en práctica pero mucho en teoría.
- **Lagrange con “¿conviene un préstamo/crédito a i %?”** aparece en 2021 (Com 403 y 404), 2019 final y 2026: la respuesta es comparar λ (en la unidad de i) con la tasa del crédito. Variante de 2018 y 2024: λ por tanteo, “valor más cercano”.
- Transporte, entera, redes, CPM/PERT: aparecen en parciales viejos (P2 de 2016–2022) y en finales anteriores a 2020. **No están en el parcial único 2026**, así que para el recuperatorio son prioridad baja (a lo sumo una pregunta de teoría).
- Formato: hasta 2024 es casi todo **desarrollo**. 2021 (Moodle) mezcla VF/MC; 2025 introduce preguntas de **selección** sobre el gráfico; 2026 es **MC “valor más cercano”**. Para el recuperatorio conviene practicar cálculo exacto y rápido de: vértice óptimo, holgura en un punto, valor implícito, rango de c_j y Δb_i, λ, Q con restricción, inversión promedio.

---

## 3. Preguntas de teoría que se repiten

(Textual o casi. Entre paréntesis, en qué exámenes aparece.)

**Stock**
1. “¿Cuáles son las principales diferencias entre los sistemas de punto de pedido y los de revisión periódica?” / “Enuncie las principales diferencias… Realice un gráfico de cantidad en stock vs. tiempo para cada modelo” (F 2013-02-13, F 2013-08-26, F 2015-03-09, F 2018-08-27, P3 2018-10-30, Rec 2022-12-01 ×2, F 2023-04-27, 2024 IMG-1). **La más repetida de todas.**
2. “En el modelo de descuento por cantidad excedente, suponiendo un costo C1 si se compra una cantidad menor a A; y un costo de C1 para las primeras A unidades más un costo de C2 > C1 para la cantidad excedente. Demuestre el límite de la función de costo C(Q) cuando Q tiende a infinito.” (Rec 2022-12-01, P3 2024 T1 y T2). Variante: “Describa el modelo de descuento por cantidad excedente, en el caso particular se haya indicado un valor mínimo de compra y nos dicen que el valor de la gestión de orden de compra puede considerarse nulo. Explicar qué es lo que cambia en la expresión y en su modelo.” (P3 2018-10-30, P3 2021-11-04); “Desarrollo del modelo de descuento por cantidad excedente” (F 2019-02-13).
3. “Desarrolle el método para hallar el mínimo de la función objetivo correspondiente al modelo con restricción de espacio de almacenamiento / de tiempo de preparación de máquinas. Utilice el método de los multiplicadores de Lagrange para este fin.” (P3 2022-11-10, Rec 2022-12-01, P3 2024 T1/T2). Relacionadas: “En un modelo de stock con restricción de espacio, ¿en qué unidades se expresa λ? Explique la fórmula de restricción y el significado de λ… obtenga Qj óptimo” (F 2014-07-28, F 2018-05-28, P3 2021-11-11); “Interpretación de λ en un modelo con restricción financiera” (F 2014-08-25, F 2017-11-27, F 2018-08-27, F 2019-02-13).
4. “Grafique (en forma aproximada) la función de Costo total en el momento de la utilización en función del ‘tiempo’, correspondiente al modelo de período común para un conjunto de artículos. Explique el significado de cada una de sus partes. Desarrolle.” (Rec 2022-12-01, F 2023-04-27, P3 2024 T1/T2).
5. “En el modelo de consumo durante el ingreso, ¿cómo debe ser la relación entre la velocidad de ingreso al stock y la demanda? ¿Por qué? Justifique utilizando las fórmulas correspondientes.” (P3 2022-11-10, P3 2024 T1/T2); “Desarrolle el modelo con consumo durante el ingreso” (F 2015, F 2018-05-28, F 2019-04-29).
6. “¿Cuáles son los componentes de la función de costo unitario en el momento de la utilización? A partir de estos componentes, ¿cómo se determina el costo mínimo? Desarrolle el concepto y explíquelo con el gráfico correspondiente.” (P3 2021-11-11, P3 2024 T1/T2).
7. “¿Cómo calculan las empresas su tasa de mantenimiento de stock?” / “Enuncie tres tipos de costos de mantenimiento con un ejemplo” (F 2013-02-13, F 2014-05-19, F 2017-08-28, F 2017-11-27, F 2019-02-13, P3 2021-11-11).
8. “¿Por qué el stock es un desperdicio? ¿Y si es un desperdicio, por qué existe de todos modos?” / causas generadoras de stock (P 2018-11-01, F 2015-08-03, P3 2022-11-10).
9. Escalón: “Realice los gráficos del costo unitario en el momento de la utilización en función de la cantidad a comprar, correspondientes a las distintas situaciones que pueden presentarse” (P3 2022-11-10, F 2016-11-21).
10. RF vs IPF: “¿Un RF 2 % es lo mismo que un IPF 98 %?” / “Definir IPF y RF” (F 2013-12-02); “¿Por qué la tabla de RF es la de la normal estándar?” (P3 2021-11-11); “¿Por qué en revisión periódica la demanda se estudia durante T + LT?” (P3 2021-11-04).
11. Clasificación ABC y qué gestión para los C (F 2013-08-05, F 2015, P3 2021-11-04 práctico).

**Programación lineal**
12. “Enuncie el teorema fundamental de la dualidad / el teorema dual” (F 2013-08-05, F 2014-08-25, F 2015, P2 2015-10-20, P1 2025 Q9).
13. Relación entre primal y dual / “¿Qué tipo de solución posee el dual de un primal con soluciones múltiples?” (F 2015-03-09, F 2018-08-27, Sin fecha teoría c).
14. “Defina valor implícito. Indique su consecuencia en cuanto al precio de los recursos. Explique cuándo se comporta como precio sombra y cuándo como valor marginal” (P2 2022-09-27); “¿De qué depende el signo del valor implícito?” / “¿Qué signo tiene el valor implícito de una ≥ en un Min?” (F 2014-08-25, F 2015-03-09); “¿Para qué se utilizan los valores implícitos?” (Sin fecha, F 2016-11-21, P2 2015-10-20). MC 2021-11-29: el precio dual requiere “que los restantes términos independientes queden fijos” y “que el cambio mantenga la base óptima”.
15. “¿Qué son / qué información brindan los costos reducidos (de las no básicas)?” (F 2013-02-13, F 2017-08-28, F 2019-04-29, P1 2025 Q6, Sin fecha doc).
16. “¿A qué se denominan coeficientes de sustitución? ¿Qué información brindan?” (F 2014-07-28, F 2018-05-28, F 2019-04-29, F 2023-04-27).
17. “Desarrolle / demuestre la condición de factibilidad (y de optimización) del simplex” (F 2014-07-28, P1 2016-06-14, P1 2018-06-14, Sin fecha doc, F 2023-04-27, P1 2025 Q4).
18. “¿Qué indica que una variable ficticia integre la base del óptimo a valor distinto de cero?” (F 2013-12-02, P2 2015-10-20, P1 2022-06-23; práctico en P1 2025); variables ficticias, penalización, 2 fases (F 2013-08-26, F 2014-05-19, P1 2016-06-14, F 2017-11-27).
19. “¿Cómo se detecta que un PL tiene solución no acotada? Tanto con simplex como con el gráfico” (P1 2016-06-14, P1 2018-06-14, P1 2022-06-23; práctico en P1 2025).
20. “Enuncie los teoremas fundamentales de la PL” (F 2018-05-28, P1 2022-06-23); punto extremo / nº máximo de puntos extremos (P1 2016-06-14, F 2016-11-21, P1 2018-06-14, Sin fecha doc).
21. Agregado de una nueva variable / restricción (F 2013-08-05, F 2013-12-02, F 2014-05-19, F 2017-11-27).
22. “Describa el concepto de holguras complementarias. Provea un ejemplo” (F 2013-08-26, Rec 2022-12-01).
23. Sensibilidad: “Desarrolle analíticamente el análisis de sensibilidad de un término independiente” (Sin fecha; P1 2025 Q10: “condición general para que la base siga siendo factible ante Δb”); “Desarrolle el cambio en un coeficiente económico” (F 2013-02-13, Rec 2022-12-01).
24. Transporte/entera (solo P2 viejos): “¿Qué significa que un modelo de transporte esté balanceado? Descríbalo con fórmulas” (P2 2022-09-27, Rec 2022-12-01); m+n−1 (F 2015-08-03, P 2018-11-01); “Describa el criterio de ramificación y poda… cómo realiza la poda” (P2 2022-09-27, Rec 2022-12-01); PL relajado (P2 2015-10-20, P 2018-11-01, Sin fecha).

---

## 4. Ejercicios para practicar (formato parecido al parcial 2026)

> Las respuestas marcadas **[archivo]** salen de la resolución que está en el archivo. Las marcadas **[calculado]** las calculé yo y conviene verificarlas.

### 4.1 Gráfico con preguntas de selección — Parcial 1, 26/07/2025, Tema 1, Ej. 1

Archivo: `Parciales/2025/2025-07-26 - 1º Parcial/2025-07-26 - Parcial - Parte 1.jpg` (resolución: `…Parcial y Resolución de Vaccaro.pdf`).

```
Min w = 4x1 + 6x2
s.a.  3x1 + 4x2 ≤ 24   (f)    A(0,6)  – B(8,0)
      6x1 + 9x2 ≥ 36   (i)    H(0,4)  – G(6,0)
      2x1       ≥ 4    (g)    recta vertical x1 = 2
      3x1 + 7x2 ≥ 21   (h)    E(0,3)  – F(7,0)
      xj ≥ 0                  K = i ∩ h
```

a) Indique la región factible y encuentre la solución óptima completa con el método gráfico (rectas de isobeneficio).
b) Seleccione ninguna, una o varias opciones y justifique:
- i) El problema: no tiene solución / tiene una solución óptima / tiene más de una solución óptima / tiene solución en el infinito.
- ii) El punto A: es solución factible no óptima / no es solución factible / es la (o una) solución óptima.
- iii) La restricción f: se cumple con exceso / se cumple sin holgura.
- iv) La región factible es: acotada o cerrada / no acotada o abierta.
- v) La restricción h: es activa / no es activa.
- vi) ¿Cuáles de estos puntos son posibles soluciones?: H, B, K, E.

**Resultados [archivo]:** la recta objetivo es paralela a (i) (4/6 = 6/9) → **óptimos alternativos** en el segmento LK, con L = (2, 8/3) y K = (21/5, 6/5); **w\* = 24**.
Vector completo (x1, x2, s_f, e_i, e_g, e_h): L = (2, 8/3, 22/3, 0, 0, 11/3); K = (21/5, 6/5, 33/5, 0, 22/5, 0).
i) más de una solución óptima · ii) A no es factible (no cumple 2x1 ≥ 4) · iii) f se cumple **con holgura** (en L y K da menos de 24), así que ninguna de las dos opciones · iv) cerrada (y acotada) · v) h es activa (holgura 0 en K) · vi) B y K son factibles; H y E no.
Tema 2 (variante): 2x1 ≥ 5 → L = (5/2, 7/3), w\* = 24.

### 4.2 Tabla óptima con incógnitas, dual y sensibilidad — Parcial 1, 26/07/2025, Ej. 3 (ambos temas)

Archivo: `…/2025-07-26 - Parcial - Parte 2.jpg` (resolución de Vaccaro).

Un restaurante ofrece tres menús: vegetariano (x1), clásico (x2) y proteico (x3). Ganancia por menú: 4, 2 y 6 $. Vegetales: 2, 1, 1 por menú (disponible 10, **deben usarse todos**). Carne: 0, 1, 2 (disponible 20).

```
Max z = 4x1 + 2x2 + 6x3
s.a. 2x1 + x2 +  x3       = 10    (x5 ficticia, −M)
            x2 + 2x3 + x4 = 20    (x4 holgura)
     xj ≥ 0

Tabla de óptimo a completar:
          c        4    2    6    0    −M
 CB   base        x1   x2   x3   x4   x5     Xi
 L    x3           A    E    1    0    1      I
 M    x4           B    F    0    1   −2      J
      zj           C    G    0    0    6
      cj−zj        D    H             −M−6    K
```

a) Completar la tabla. b) Dual y su solución completa, interpretando algún costo reducido. c) Si pudiera vender por separado algún ingrediente, ¿lo haría? d) ¿Cuánto puede disminuir la contribución del menú proteico sin que cambie la solución? e) Si se elimina la carne del menú clásico, su ganancia sube 2 unidades: ¿conviene? (con el dual). f) Con 10 unidades más de vegetales por día, ¿cambia la solución óptima?

**Resultados [archivo]:** L = 6, M = 0; B⁻¹ = [[1, 0], [−2, 1]]; A = 2, B = −4, E = 1, F = −1, I = 10, J = 0; C = 12, D = −8, G = 6, H = −4, K = 60.
Óptimo: x3 = 10, el resto 0, **z\* = 60** (degenerada: x4 = 0 en la base).
Dual: Min w = 10u1 + 20u2; 2u1 ≥ 4; u1 + u2 ≥ 2; u1 + 2u2 ≥ 6; u1 libre, u2 ≥ 0 → **u1 = 6, u2 = 0**, excedentes (8, 4, 0), w\* = 60. Costo reducido: producir un vegetariano resta $8, un clásico $4.
c) No: no le sobra ni vegetal ni carne. d) −4 ≤ Δc3 < ∞ (c3 ≥ 2). f) Rango −10 ≤ Δb1 ≤ 0: +10 sale del rango, cambia la base; la nueva solución es x1 = 5, x3 = 10, z = 80.
e) **[calculado]** Columna nueva (1, 0) con c = 4: z_j = u·A = 6 > 4 → costo reducido −2 → no conviene.

### 4.3 Salida LINDO con restricción ≥ — Steelco, 2° Parcial 27/09/2022 (T1 y T2)

Archivo: `Parciales/2022/2° Parcial/PRACTICA parcial 27-09-22 tema 1 (2).jpg` y `tema 2 (2).jpeg`.

Tres tipos de acero, ganancia por lámina 8, 5 y 2 u.m. Carbón: 200 t (3, 2, 1 t por lámina). Hierro: 65 t (los tipos 1 y 3 usan 1 t cada uno). Mano de obra: 100 h (1 h por lámina). Hay que producir al menos 10 láminas del tipo 2.

```
MAX 8X1 + 5X2 + 2X3
2) 3X1 + 2X2 + X3 <= 200   (carbón)
3)  X1       + X3 <=  65   (hierro)
4)  X1 +  X2 + X3 <= 100   (horas)
5)        X2      >=  10   (mínimo tipo 2)

OBJECTIVE FUNCTION VALUE 530
VARIABLE  VALUE  REDUCED COST        ROW  SLACK  DUAL PRICE
X1        60     0                   2)   0       2.666667
X2        10     0                   3)   5       0
X3         0     0.666667            4)  30       0
                                     5)   0      -0.333333
THE TABLEAU
ROW (BASIS)  X1   X2   X3     SLK2    SLK3  SLK4   SLK5
1  ART       0    0    0.667  2.667   0     0     ∓0.333   530
2  X1        1    0    0.333  0.333   0     0     -0.667    60
3  SLK3      0    0    0.667 -0.333   1     0     +0.667     5
4  X2        0    1    0      0       0     0     +1.000    10
5  SLK4      0    0    0.667 -0.333   0     1     -0.333    30
```

Tema 1: a) Interprete la solución completa. b) Si el mínimo de producción del tipo 2 sube a 12, ¿qué pasa? c) Se descartan 30 t de carbón: ¿cómo cambia la solución? d) ¿Qué ganancia debería tener el acero tipo 3 para que convenga producirlo? e) Dual y su solución.
Tema 2: b) ¿Hasta qué valor puede bajar la ganancia del tipo 1 sin que cambie la solución? c) Hay 35 h menos de trabajo: analice. d) Acero tipo 4: ganancia 1, usa 0,5 t de carbón, 1,2 t de hierro y 1,5 h. ¿Conviene?

**Resultados [calculado]:**
a) 60 láminas del tipo 1 y 10 del tipo 2; z = 530. Carbón agotado (valor implícito 8/3). Sobran 5 t de hierro y 30 h. Cada lámina extra exigida del tipo 2 resta 1/3.
b) Rango de b5: [2,5 ; 100]. Con 12: x1 = 58,67, x2 = 12, s3 = 6,33, s4 = 29,33, **z = 529,33** (−2/3).
c) Rango de b2: [20 ; 215] (Δ entre −180 y +15). Con 170: x1 = 50, x2 = 10, s3 = 15, s4 = 40, **z = 450** (−30·8/3).
d) c3 > 2 + 0,667 = **2,667**.
e) Min 200u1 + 65u2 + 100u3 + 10u4; 3u1 + u2 + u3 ≥ 8; 2u1 + u3 + u4 ≥ 5; u1 + u2 + u3 ≥ 2; u1, u2, u3 ≥ 0; **u4 ≤ 0**. Solución: u = (8/3, 0, 0, −1/3), w = 530.
T2 b) c1 ∈ [7,5 ; ∞): puede bajar hasta 7,5 (lo limita la columna de SLK5: 0,333/0,667 = 0,5).
T2 c) Se pueden perder hasta 30 h sin cambio; con −35 la holgura daría −5 y cambia la base. Resolviendo de nuevo: x1 = 55, x2 = 10, z = 490.
T2 d) z4 = u·A4 = (8/3)(0,5) = 1,33 > 1 → costo reducido −0,33 → no conviene.

### 4.4 Lagrange con restricción financiera, 3 artículos — Parcial 3, 30/10/2018, Tema 1, Ej. 1

Archivo: `Parciales/2018/2018-10-30.pdf` (con solución).

Almacenes Vialmetal tiene tres tipos de señales. Se busca que el valor de las señales en stock **nunca exceda 7.000 u.m.** Tasa de mantenimiento: 25 % anual. ¿Qué tamaño tendrán los lotes?

```
                 A      B      C
D (u/año)      2000    600   1500
L (u.m./OC)      60     90     80
C (u.m./u)       18     70     75
i = 0,25 /año   Inversión = Σ Cj·Qj/2 ≤ 7000
```

**Resultados [archivo]:** sin restricción, Q = (230,94; 78,56; 113,14) e I = 9070,65 > 7000. Probando valores de λ, con λ = 0,18 da Q = (176,09; 59,90; 86,27) e I = 6916,3.
Fórmula usada: Qj = √(2·Dj·Lj / (Cj·(i + λ))).
**[calculado]** El λ exacto que hace I = 7000 es **0,170 /año**, con Q = (178,2; 60,6; 87,3). En formato “valor más cercano” hay que distinguir 0,17 de 0,18. Además, como todos los Q escalan igual, vale I(λ) = I₀·√(i/(i+λ)).

### 4.5 Lagrange + “¿conviene un préstamo?” — Parcial 3 Com 404, 04/11/2021, Pregunta 5

Archivo: `Parciales/2021/2021-11-04 - 3° Parcial (Com 404).pdf`.

El presupuesto para la gestión de tres artículos es de 1.500 u.m. La tasa de mantenimiento es 0,25 /año. ¿Conviene conseguir un préstamo para aumentar el tamaño de los lotes? En caso afirmativo, ¿a qué interés?

```
                     A      B      C
Demanda anual (u)  1000    700    500
Costo orden (u.m.)  120    100     80
Precio (u.m./u)       3    2,5      2
```

**Resultados [calculado]** (no hay resolución en el archivo):
- Sin restricción: Q = (565,7; 473,3; 400,0). Inversión promedio Σ CQ/2 = 1840,1 > 1500, así que la restricción está activa.
- Si el presupuesto es la inversión promedio: **λ ≈ 0,126 /año**, con Q = (461,1; 385,8; 326,1). Conviene el préstamo si su interés es menor que ~12,6 % anual (lo que se ahorra por cada peso extra invertido).
- Si se toma como inversión máxima Σ CQ ≤ 1500: λ ≈ 1,25 /año y Q = (230,6; 192,9; 163,0).
- La cátedra usó la inversión promedio en 2018, aunque el enunciado decía “nunca exceda”.
- Ejercicio gemelo: Com 403, 11/11/2021, Pregunta 2 (viruta/pegamento). D = 500 kg/mes de cada uno, C = 100 y 250 u.m., L = 200 y 300 u.m., 40.000 u.m. disponibles. La respuesta del alumno fue “conviene si el interés no supera el 2 % mensual”, sin verificar porque el enunciado del archivo no trae la tasa i.

### 4.6 Descuento por cantidad + lote en cajas — Parcial 3 2024, Tema 1/2, Ej. 2

Archivo: `Parciales/2024/3° Parcial - Tema 1.jpg`.

Un artículo se vende a U$S 25 por unidad, con 10 % de descuento para lotes de 150 unidades o más. La compañía usa 20 unidades por día. Costo de preparación del pedido: U$S 50. Tasa de mantenimiento: 24 % anual. Tiempo de espera: 6 días.
a) Grafique la ley de precios. b) ¿Debe aprovechar el descuento? Represente la función económica. c) El artículo se vende en cajas de 150 unidades: ¿cuántas cajas conviene comprar y por qué? d) Grafique la función de existencias con lote óptimo, período entre órdenes, punto de pedido y plazo de provisión.

**Resultados [calculado]** (el enunciado no fija los días del año; con 365, D = 7300 u/año):
- Con C = 22,5: Q\* = √(2·7300·50/(22,5·0,24)) = **367,7 ≥ 150** → es válido y conviene el descuento. CT = 166.235 contra 185.397 en el mejor punto sin descuento (Q = 149 a 25).
- Cajas: con 2 cajas (300 u) el costo variable es 1216,7 + 810 = 2026,7; con 3 cajas (450 u), 811,1 + 1215 = 2026,1. Es prácticamente un empate: con 365 días ganan por poco 3 cajas; con 360 días, 2 cajas (2010 contra 2015); con 250 días, 2 cajas claramente (Q\* = 304). Hay que justificar con CT(300) vs CT(450).
- d) PP = d·LT = 20·6 = **120 u**. T\* = Q/d: 15 días con 300 u o 22,5 días con 450 u.
- Ejercicio 3 del mismo parcial **[calculado]**, para practicar inferir μ y σ. T1: RF 1 % (z = 2,33), LT = 3 semanas = 15 días hábiles, SS = 32, PP = 228 → σ = 32/(2,33·√15) ≈ 3,55 u/día y μ = (228 − 32)/15 ≈ 13,07 u/día. Costo mensual del SS = 32·55·0,24/12 = 35,2 u.m./mes.

### Otros ejercicios con datos completos en el archivo (para más práctica)

- Tableau LINDO “fabricante de tejidos” con x2 ≥ 800 (Rec. P2 2021-11-29). Resolución manuscrita en `Parciales/2020/2020-00-00.pdf`: con x1 = 300, z\* = 33.000 (x2 = 1200); no paga 11 u.m./h porque el valor implícito de la máquina es 10; Δb3 no cambia nada.
- LINDO “laboratorio” 4 productos, con rangos completos (P2 2020-09-22 y final 2021-06-28): z = 740, valores implícitos 0,68 y 1,6, rango de b1 [400; 1066,67].
- PL + dual con salida LINDO “alimentos para gatos” (final 2023-04-27). Ojo: el LINDO usa c = 100 y 95, el enunciado dice 1000 y 950 $/kg.
- Tabla con −M a completar (P1 2019-06-11, con solución: incompatible) y tabla intermedia a completar e iterar (P1 2016-06-14; P1 2022-06-23).
