# (Gordon) Libro - páginas 320 a 332.pdf

> Transcripción de 7 hojas escaneadas (fotos de dobles páginas del libro de Gordon,
> *Simulación de sistemas*, cap. 15 "Verificación de los resultados de simulación").
> Se numeran con la paginación original del libro: págs. 320 a 332.
> Correspondencia hoja escaneada → páginas del libro:
> hoja 1 → 320-321, hoja 2 → 322-323, hoja 3 → 324-325, hoja 4 → 326-327,
> hoja 5 → 328-329, hoja 6 → 330-331, hoja 7 → 332.

--- pág. 320 ---

**320    Simulación de sistemas**

entonces de la integral de la distribución **t** de Student. La desviación entre estas dos distribuciones disminuye conforme aumenta $n$, y para $n$ suficientemente grande ($\geqslant 30$), se puede utilizar la distribución normal.

Expresando en términos del valor estimado de la variancia de la población, el intervalo de confianza para $\mu$ es

$$\bar{x} \pm \frac{s}{\sqrt{n}} u_{\alpha/2}$$

en que $u_{\alpha/2}$ se basa en una distribución **t** de Student cuando $n$ es pequeña, y en la distribución normal cuando $n$ es grande.

## 15-3  Estadísticas de corridas de simulación

El método de determinar un intervalo de confianza descrito en la sección anterior se basa en dos suposiciones. Supone que la distribución de la cual se obtienen las observaciones es estacionaria, y supone que las observaciones son independientes. Desafortunadamente, muchas estadísticas de interés en una simulación no satisfacen estas condiciones. Para ilustrar los problemas que se plantean al medir estadísticas de corridas de simulación, se estudiará un ejemplo específico.

Considere un sistema de un solo dependiente en que las llamadas ocurren con una disciplina de distribución de Poisson y el tiempo de servicio tiene una distribución exponencial. La disciplina de colas es de primero entrado, primero salido, sin prioridades. Suponga que el objetivo del estudio es medir el tiempo medio de espera, definido como el tiempo que esperan las entidades a recibir servicio y excluyendo al propio tiempo de servicio. El problema se puede resolver analíticamente. En la ec. (7-8) se dio la solución y en la figura 7-6 se graficó la probabilidad del tiempo de espera.

El enfoque más simple en una corrida de simulación es estimar el tiempo medio de espera acumulando el tiempo de espera en $n$ entidades sucesivas y dividiendo entre $n$. A esta medida se le llama la media de la muestra y se denota mediante $x(n)$ para enfatizar el que su valor depende de la cantidad de observaciones que se toman. Si $x_i$ ($i = 1, 2, \ldots, n$) son los tiempos individuales de espera (incluyendo el valor 0 para las entidades que no tienen que esperar), entonces

$$\bar{x}(n) = \frac{1}{n} \sum_{i=1}^{n} x_i \qquad (15\text{-}2)$$

--- pág. 321 ---

> [El número de página no es legible en el escaneo; se deduce por secuencia.]

Los tiempos de espera medidos de esta manera no son independientes. Siempre que se forma una cola, el tiempo de espera de cada entidad en la cola claramente depende de los tiempos de espera de sus predecesores. Se dice de cualquier serie de datos que tenga esta propiedad de que un valor afecte a otros, que está *autorrelacionada*. El grado en que los datos están autocorrelacionados se puede medir en formas que se describirán brevemente en una sección posterior. En el problema específico en estudio, la autocorrelación aumenta rápidamente conforme aumenta la utilización de la facilidad de servicio.

Bajo condiciones más generales que se puede esperar normalmente que valgan en una corrida de simulación, se puede mostrar que la media de la muestra de datos autocorrelacionados se aproxima a una distribución normal conforme aumenta el tamaño de la muestra⁴. La fórmula usual para estimar el valor medio de la distribución, la ec. (15-2), continúa siendo una estimada satisfactoria para la media de los datos autocorrelacionados. Sin embargo, la variancia de los datos autocorrelacionados no está relacionada con la variancia de la población mediante la expresión simple $\sigma^2/n$, como ocurre para los datos independientes. Es necesario agregar un término para tomar en cuenta la autocorrelación. El término es positivo en los casos que normalmente ocurren en un experimento de simulación, de manera que si se ignora, se subestima la variancia y se calcula un intervalo de confianza excesivamente optimista.

Otro problema que debe afrontarse es que las distribuciones pueden no ser estacionarias. En especial, se inicia una corrida de simulación con el sistema en algún estado inicial, con frecuencia el estado de ocio, en que no se está dando servicio y no hay entidades en espera. Las primeras llegadas tienen entonces una probabilidad más que normal de obtener rápidamente el servicio, de manera que estará sesgada una media de muestra que incluya las primeras llegadas. El efecto del sesgo disminuye al extender la longitud de la corrida de simulación y aumentar el tamaño de la muestra. Para un tamaño dado de muestra que parta de una condición inicial dada, la distribución de la media de la muestra es estacionaria; pero si pudieran compararse las distribuciones para tamaños distintos de muestras, las distribuciones serían ligeramente diferentes. Las soluciones analíticas descritas antes corresponden a valores de estado estable a los que convergen las distribuciones al aumentar el tamaño de la muestra.

Para ilustrar estos problemas, la figura 15-1 muestra los resultados de medir el tiempo de espera medio de la muestra para el sistema de un solo dependiente. Se muestran resultados de tres corridas, cada uno para el caso en que la utilización del sistema es de 0.5 Para cada co-

--- pág. 322 ---

> [FIGURA pág. 322 — FIGURA 15-1. Variabilidad de los resultados de simulación.]
> Gráfico de líneas con ejes lineales.
> Eje Y (rotulado como fracción vertical): "TIEMPO MEDIO DE ESPERA / TIEMPO MEDIO DE SERVICIO", escala de 0 a 0.7 con divisiones marcadas en 0.1, 0.2, 0.3, 0.4, 0.5, 0.6 y 0.7.
> Eje X: "NUM. DE OBSERVACIONES", de 0 a 200, marcas en 0, 50, 100, 150 y 200.
> Se grafican tres curvas (tres corridas independientes del mismo sistema con ρ = 0.5), todas partiendo del origen (0,0) porque el sistema arranca en estado de ocio.
> - Curva A: sube muy rápido, alcanza ≈0.59 en n≈25, baja a ≈0.52 en n≈40, salta a un máximo de ≈0.64 en n≈55, cae a ≈0.48, vuelve a subir a ≈0.59 en n≈75, luego desciende irregularmente (≈0.50 en n≈95, ≈0.47 en n≈120, mínimo ≈0.44 en n≈130), sube a ≈0.54-0.55 entre n≈150 y 165, baja a ≈0.52 en n≈175 y termina subiendo hasta ≈0.67 en n≈190 y ≈0.64 en n=200.
> - Curva B: sube algo más lento, ≈0.52 en n≈30, ≈0.48 en n≈50, ≈0.45 en n≈75-100, ≈0.44 en n≈100, desciende suavemente a ≈0.41 en n≈150-170, y termina en ≈0.40 en n=200.
> - Curva C: sube muy lentamente, ≈0.11 en n≈30, máximo local ≈0.23 en n≈40, cae a un mínimo de ≈0.12 en n≈80, sube a ≈0.20 en n≈110, se mantiene entre 0.18 y 0.20 hasta n≈155, y luego sube abruptamente hasta ≈0.42 en n≈180, terminando en ≈0.37 en n=200.
> El valor verdadero teórico de la relación es 0.5. La figura ilustra (a) la enorme variabilidad de la media de la muestra entre corridas que solo difieren en los números aleatorios usados y (b) el sesgo inicial provocado por arrancar el sistema desde el estado de ocio.

**FIGURA 15-1.** Variabilidad de los resultados de simulación.

rrida se inició el sistema en el estado de ocio; las corridas sólo difieren porque se utilizaron distintos números aleatorios. Las observaciones se realizaron al dar servicio a cada décima entidad. Se muestra la relación del tiempo medio de espera al tiempo de servicio; en este caso debería de ser de 0.5. De inmediato es aparente la variabilidad de la media de la muestra y también se aprecia el sesgo inicial provocado por arrancar el sistema desde el estado de ocio. La media de la muestra finalmente se establece en un valor estable debido a que es una estadística cumulativa. Por ejemplo, la figura 15-2 muestra los resultados para el mismo experimento realizado para 10,000 entidades con muestras cada 500.

--- pág. 323 ---

> [FIGURA pág. 323 — FIGURA 15-2. Estabilización del tiempo medio de espera acumulado.]
> Gráfico de una sola curva, ejes lineales.
> Eje Y (rotulado como fracción vertical, **tal como está impreso**): "TIEMPO MEDIO DE SERVICIO / NUM. DE OBSERVACIONES", con marcas en 0.4, 0.5 y 0.6.
> Eje X (**tal como está impreso**): "TIEMPO MEDIO DE ESPERA", de 0 a 10,000 con marcas en 2,000, 4,000, 6,000, 8,000 y 10,000.
> [Nota del transcriptor: los rótulos de los ejes de esta figura están evidentemente intercambiados/erróneos en esta edición; por el texto deberían ser Y = tiempo medio de espera / tiempo medio de servicio, X = núm. de observaciones.]
> La curva arranca en ≈0.48 (para n≈500), sube a un pico de ≈0.66 cerca de 1,000, cae a ≈0.54 en ≈1,500, sube a un segundo pico de ≈0.59 cerca de 2,000, y a partir de ahí desciende suave y monótonamente con pequeñas oscilaciones: ≈0.55 en 2,500-3,500, ≈0.54 en 4,000-5,000, ≈0.52 en 6,000-6,500, ≈0.53 en 7,000-8,500, y termina en ≈0.52 en 10,000.
> Ilustra que la media acumulada de la muestra se estabiliza cerca del valor verdadero (0.5) aunque siguen viéndose fluctuaciones apreciables incluso después de muchas entidades medidas.

**FIGURA 15-2.** Estabilización del tiempo medio de espera acumulado.

Sin embargo, incluso aquí pueden verse fluctuaciones significativas después de haber medido muchas entidades. Desde luego, el hecho de que la media de la muestra acumulada tienda a un valor estable no significa que el tiempo de espera tienda a un valor estable. Los tiempos individuales de espera siguen mostrando su variabilidad inherente sin importar cuántos se midan, pero con la acumulación de las observaciones, las variantes de la media de la muestra se balancean.

## 15-4  Repetición de corridas

La figura 15-1 sugiere una manera de obtener una medida de la variancia de la media de la muestra. Al repetir el experimento con distintos números aleatorios para el mismo tamaño $n$ de la muestra se obtiene un conjunto de determinaciones independientes de la media $x(n)$ de la muestra. Aunque la distribución de la media de la muestra depende del grado de autocorrelación, se puede utilizar adecuadamente estas determinaciones independientes de la media de la muestra para estimar la variancia de la distribución. Suponga que el experimento se repite $p$ veces con series de números aleatorios independientes. Sea $x_{ij}$ la $i$-ésima observación en la $j$-ésima corrida, y sea el valor de la

--- pág. 324 ---

**324    Simulación de sistemas**

media de la muestra para la $j$-ésima corrida igual a $\bar{x}_j(n)$. Entonces, la estimada del tiempo medio de espera y su variancia son:

$$m(n) = \frac{1}{p} \sum_{j=1}^{p} \bar{x}_j(n) = \frac{1}{np} \sum_{j=1}^{p} \sum_{i=1}^{n} x_{ij} \qquad (15\text{-}3)$$

$$s^2(n) = \frac{1}{p-1} \sum_{j=1}^{p} \left[ \bar{x}_j(n) - m(n) \right]^2 \qquad (15\text{-}4)$$

Se pueden utilizar las dos estimaciones para establecer un intervalo de confianza.

La figura 15-3 muestra el resultado de aplicar el procedimiento al sistema de un solo dependiente. Los resultados se muestran para utilizaciones de 0.2, 0.3, 0.4, 0.5 y 0.6. En cada caso se ha repetido el experimento desde un estado inicial de ocio, utilizando distintos números aleatorios en cada repetición. Los resultados muestran el tiempo medio de espera estimado calculado de la ec. (15-3) como una función del tamaño de la muestra $n$. Las mediciones se realizaron en incrementos de $n = 5$ para $\rho = 0.2$, $0.3$, y $0.4$ y $n = 10$ para $\rho = 0.5$ y $0.6$. Cada caso es para 100 representaciones ($p = 100$). También se muestran los intervalos de 90% de confianza calculados para el valor más alto de $n$ que se utiliza en cada caso, y los valores *verdaderos* conocidos de los tiempos verdaderos efectivamente caen dentro de los intervalos de confianza.

La media en que se basa el intervalo de confianza depende de $1/np$. En ausencia del sesgo inicial, se puede esperar que el mismo aumento proporcional en $n$ o $p$ tenga efectos equivalentes en el tamaño del intervalo de confianza. También se puede esperar que cuesten aproximadamente la misma cantidad de tiempo de computador para su ejecución. Sin embargo, para aumentar la probabilidad de reducir el sesgo inicial hasta el punto en que pueda considerarse despreciable, es preferible extender las corridas manteniendo el número de repeticiones a un nivel en que el tamaño de la muestra es suficientemente grande para justificar la aproximación a una distribución normal. Para una cantidad dada de computación, se puede maximizar el tamaño de la corrida reduciendo a un mínimo el efecto del sesgo inicial. En las referencias⁵ ʸ ⁶ se estudian más ampliamente los criterios para esas decisiones.

## 15-5  Eliminación del sesgo inicial

Los resultados de la figura 15-5 muestran claramente los efectos del sesgo inicial. El que los valores verdaderos caigan dentro de los

--- pág. 325 ---

*Verificación de los resultados de simulación*    **325**

> [FIGURA pág. 325 — FIGURA 15-3. Tiempo medio de espera acumulado para el sistema, partiendo del estado de ocio.]
> Gráfico de líneas con eje Y logarítmico.
> Eje Y (rotulado como fracción vertical): "TIEMPO MEDIO DE ESPERA / TIEMPO MEDIO DE SERVICIO", escala logarítmica de 0.01 a 1.0, con rótulos en 0.01, 0.05, 0.1, 0.5 y 1.0.
> Eje X: "$n$, NUM. DE OBSERVACIONES", lineal de 0 a 150, con marcas en 50, 100 y 150.
> Texto dentro del cuadro del gráfico: "NUM. DE REPETICIONES, $p = 100$".
> Leyenda a la derecha: "INTERVALO DE CONFIANZA DE ULTIMO VALOR" (indicado con dos líneas de trazos, una arriba y otra abajo del valor) y "VALOR VERDADERO" (indicado con una flecha horizontal ←).
> Cinco curvas, rotuladas de arriba hacia abajo con flechas: $\rho = 0.6$, $\rho = 0.5$, $\rho = 0.4$, $\rho = 0.3$ y $\rho = 0.2$.
> Todas las curvas arrancan desde valores muy bajos (el sistema parte del estado de ocio), suben abruptamente en las primeras observaciones y luego se aplanan:
> - $\rho = 0.6$: sube desde ≈0.4 hasta ≈0.75 en n≈20, sigue creciendo lentamente a ≈0.85 en n≈50 y ≈0.9 en n≈100-150 (no llega aún al valor verdadero ≈0.95, marcado con flecha en el borde derecho).
> - $\rho = 0.5$: sube hasta ≈0.5 en n≈40-50, luego crece muy lentamente hasta ≈0.53 en n≈150; valor verdadero ≈0.55.
> - $\rho = 0.4$: sube hasta un máximo ≈0.31 en n≈30, baja ligeramente y se mantiene en ≈0.27-0.28 desde n≈50 hasta n≈100; valor verdadero apenas por encima del último valor.
> - $\rho = 0.3$: se estabiliza en ≈0.14-0.15 desde n≈20, con pequeñas oscilaciones hasta n≈100.
> - $\rho = 0.2$: se estabiliza en ≈0.05 (leve pico inicial ≈0.055 en n≈15, luego ≈0.048 y ligera subida final a ≈0.052 en n≈95).
> Cada curva termina con su intervalo de confianza del 90% en trazos y la flecha del valor verdadero, que en todos los casos cae dentro del intervalo.

**FIGURA 15-3.** Tiempo medio de espera acumulado para el sistema, partiendo del estado de ocio.

intervalos estimados de confianza sugiere que las corridas fueron suficientemente largas para que el sesgo inicial fuera despreciable. Sin embargo, por lo general no se dispone de los resultados teóricos que se utilizaron para establecer este hecho. Se pueden seguir dos enfoques generales para reducir el efecto del sesgo inicial. Se puede iniciar cada sistema en una condición inicial más representativa o se puede ignorar la primera parte de cada corrida de simulación.

--- pág. 326 ---

**326    Simulación de sistemas**

En algunos sistemas de simulación, especialmente de sistemas existentes, se puede disponer de información sobre las condiciones esperadas, lo que permite elegir mejores condiciones iniciales que el estado de ocio. Sin embargo, debe de utilizarse un rango de valores para las condiciones iniciales a partir del cual se escoja un estado inicial distinto para cada repetición. Utilizar la misma condición inicial para cada corrida puede reducir el sesgo eliminando una condición no usual de arranque, pero deja cierto grado de correlación entre las corridas. Desafortunadamente, este enfoque requiere conocer mucho acerca del comportamiento del sistema antes de iniciar la simulación. Sin embargo, hay casos en que se puede utilizar este enfoque. Adicionalmente, es posible utilizar el enfoque para verificar la exactitud de una simulación mediante reiteración. Después de obtener los resultados por uno u otro método, se pueden utilizar las condiciones predichas por los resultados para indicar condiciones iniciales razonables. Si los resultados originales son verdaderamente independientes del sesgo inicial, la repetición de algunas de las corridas con las nuevas condiciones iniciales no debe de producir diferencia significativa.

El enfoque más común para eliminar el sesgo inicial es eliminar una sección inicial de la corrida. La corrida se inicia a partir de un estado de ocio y se detiene después de determinado periodo. Entonces se dejan como están las entidades que existen en el sistema en ese momento. Luego se reinicia la corrida recabando estadísticas desde el punto de reinicio. Como cuestión práctica, es usual programar la simulación de manera que se recaben las estadísticas desde el principio, y sencillamente borrar las recabadas hasta el punto del reinicio. No es posible dar reglas simples para decidir de qué largo debe de ser el intervalo eliminado. Se aconseja utilizar algunas corridas piloto a partir del estado de ocio para juzgar el tiempo durante el que se mantiene el sesgo inicial, lo que puede hacerse graficando las estadísticas medidas contra la longitud de corrida como se hizo en la figura 15-2. Sin embargo, es sumamente deseable que la investigación piloto se realice repitiendo las corridas como se hizo en la figura 15-3. Un examen de las tres corridas individuales de la figura 15-1 mostrará lo difícil que es juzgar de una sola corrida cuando el valor medido se haya aproximado a su valor estable. A costa de un poco más de cálculo, se puede examinar la presencia de sesgo inicial estudiando el comportamiento de la desviación estándar. En ausencia de sesgo inicial, se puede esperar que la desviación estándar sea inversamente proporcional a $n^{1/2}$. Al examinar la manera en que cambia la desviación estándar con la longitud de la muestra, es posible ver si se satisface esta relación. Por ejemplo, la figura 15-4 muestra la desviación estándar que se obtuvo

--- pág. 327 ---

*Verificación de los resultados de simulación*    **327**

al mismo tiempo que los resultados de la figura 15-3. Se grafica el logaritmo de la desviación estándar, deducido de la ec. (15-4), contra el logaritmo $n$. El resultado debe de aproximar una línea recta inclinada hacia abajo con la relación de 1 en 2 (para ejes con escalas iguales). Se puede ver que las curvas aumentan inicialmente pero que al final disminuyen como se espera.

A partir de los resultados de la figura 15-4, se puede juzgar que los márgenes para un periodo inicial serán como sigue:

| Utilización | Punto de corte |
|---|---|
| 0.3 | 14 |
| 0.4 | 30 |
| 0.5 | 60 |
| 0.6 | 120 |
| 0.2 | 7 |

Probablemente los valores elegidos sean conservadores debido a que son estadísticas acumuladas. Usando los valores anteriores para un periodo inicial de corte, las figuras 15-5 y 15-6 muestran los resultados de repetir los experimentos de las figuras 15-3 y 15-4.

## 15-6  Medias de lotes

Otro enfoque al problema de estimar la precisión de los resultados de simulación no solo se apoya en la repetición sino que utiliza una sola corrida larga, preferentemente quitando el sesgo inicial. La corrida se divide en una cantidad de segmentos para separar las mediciones en lotes de igual tamaño. Se toma la media de cada lote y se considera a las medias de los lotes individuales como observaciones interdependientes. El valor estimado de la variable que se está midiendo es la media de las medias de los lotes, lo que naturalmente es justo igual a la media de todas las mediciones. Sin embargo, la suposición de que las medias de los lotes son independientes, junto con la aplicación del teorema del límite central, permite considerar a las observaciones de las medias de los lotes como distritos normalmente. Entonces se puede aplicar la fórmula usual para estimar la variancia de la media y calcular un intervalo de confianza.

No se puede aplicar el método a una estadística acumulada, tal como el tiempo medio de espera acumulado que se estudió en la sección anterior, debido a que la distribución de la media de la muestra depende de la longitud de la corrida y no se puede considerar a las medias de lotes sucesivos como observaciones de la misma población. Típicamente, se podría utilizar el método en la medición de una lon-

--- pág. 328 ---

> [FIGURA pág. 328 — FIGURA 15-4. Variación de la desviación estándar con el tamaño de la muestra, partiendo del estado de ocio.]
> Gráfico log-log.
> Eje Y: "DESVIACION ESTANDAR DEL TIEMPO DE ESPERA DE LA MUESTRA", escala logarítmica de 0.01 a 1.0, con rótulos en 0.01, 0.05, 0.1, 0.5 y 1.0.
> Eje X: "$n$, NUM. DE OBSERVACIONES", escala logarítmica de 10 a 200, con rótulos en 10, 20, 50, 100 y 200.
> Texto dentro del cuadro del gráfico: "TIEMPO MEDIO DE SERVICIO = 1" y "NUM. DE REPETICIONES, $p = 100$".
> Cinco curvas rotuladas $\rho = 0.6$, $\rho = 0.5$, $\rho = 0.4$, $\rho = 0.3$ y $\rho = 0.2$ (de arriba hacia abajo).
> - $\rho = 0.6$: parte en ≈0.55 en n=10, **sube** hasta un máximo de ≈0.72 entre n≈22 y n≈35, luego baja a ≈0.50 en n≈65, ≈0.51 en n≈80, y llega a ≈0.38 en n≈150.
> - $\rho = 0.5$: parte en ≈0.36 en n=10, se mantiene plana hasta n≈20, sube a un máximo ≈0.44 en n≈32, baja a ≈0.33 en n≈50, ≈0.30 en n≈65, y termina en ≈0.24 en n≈130-150.
> - $\rho = 0.4$: parte en ≈0.26 en n=10, plana hasta n≈17, sube a ≈0.34 en n≈27-32, baja monótonamente a ≈0.25 en n≈50, ≈0.19 en n≈70, y termina en ≈0.15 en n≈100.
> - $\rho = 0.3$: **decrece monótonamente** desde ≈0.20 en n=10 hasta ≈0.10 en n≈50, ≈0.075 en n≈70 y ≈0.056 en n≈100.
> - $\rho = 0.2$: decrece monótonamente desde ≈0.09 en n=10 hasta ≈0.055 en n≈22, ≈0.045 en n≈32, ≈0.035 en n≈50, ≈0.026 en n≈70 y ≈0.023 en n≈100.
> Ilustra que, con sesgo inicial presente, las curvas de utilización alta primero aumentan y solo después decrecen; en ausencia de sesgo deberían ser rectas descendentes de pendiente 1 en 2 (es decir, $s \propto n^{-1/2}$).

**FIGURA 15-4.** Variación de la desviación estándar con el tamaño de la muestra, partiendo del estado de ocio.

--- pág. 329 ---

> [FIGURA pág. 329 — FIGURA 15-5. Tiempo medio de espera acumulado para el sistema, quitando el periodo inicial.]
> Mismo formato que la figura 15-3.
> Eje Y (fracción vertical): "TIEMPO MEDIO DE ESPERA / TIEMPO MEDIO DE SERVICIO", escala logarítmica de 0.01 a 1.0, rótulos en 0.01, 0.05, 0.1, 0.5 y 1.0.
> Eje X: "$n$, NUM. DE OBSERVACIONES", lineal de 0 a 150, marcas en 50, 100 y 150.
> Texto dentro del cuadro: "NUM. DE REPETICIONES, $p = 100$".
> Leyenda a la derecha: "INTERVALO DE CONFIANZA DEL ULTIMO VALOR" (líneas de trazos) y "VALOR VERDADERO" (flecha ←).
> Cinco curvas rotuladas $\rho = 0.6$ (sólo 40 repeticiones), $\rho = 0.5$, $\rho = 0.4$, $\rho = 0.3$ y $\rho = 0.2$.
> A diferencia de la figura 15-3, ahora todas las curvas arrancan ya cerca de su valor final (no hay rampa inicial), y son prácticamente planas:
> - $\rho = 0.6$: parte en ≈0.82, sube a un máximo de ≈0.97 en n≈50 y luego baja suavemente a ≈0.90 en n≈95; el intervalo de confianza es visiblemente más ancho porque solo hay 40 repeticiones.
> - $\rho = 0.5$: parte en ≈0.55, cae de inmediato a ≈0.51 y se mantiene plana en ≈0.50-0.51 hasta n≈95.
> - $\rho = 0.4$: oscila entre ≈0.29 y ≈0.31 en todo el rango.
> - $\rho = 0.3$: parte en ≈0.11 (n≈5), sube a ≈0.16 en n≈25 y luego se mantiene en ≈0.14-0.15.
> - $\rho = 0.2$: se mantiene en ≈0.052-0.058 en todo el rango, terminando en ≈0.050.
> En los cinco casos la flecha del valor verdadero cae dentro del intervalo de confianza del último valor.

**FIGURA 15-5.** Tiempo medio de espera acumulado para el sistema, quitando el periodo inicial.

--- pág. 330 ---

**330    Simulación de sistemas**

> [FIGURA pág. 330 — FIGURA 15-6. Variación de la desviación estándar con el tamaño de la muestra, quitando el periodo inicial.]
> Mismo formato log-log que la figura 15-4.
> Eje Y: "DESVIACION ESTANDAR DEL TIEMPO MEDIO DE ESPERA DE LA MUESTRA", escala logarítmica de 0.01 a 1.0, rótulos en 0.01, 0.05, 0.1, 0.5 y 1.0.
> Eje X: "$n$, NUM. DE OBSERVACIONES", escala logarítmica de 10 a 200, rótulos en 10, 20, 50, 100 y 200.
> Texto dentro del cuadro: "TIEMPO MEDIO DE SERVICIO = 1" y "NUM. DE REPETICIONES, $p = 100$".
> Cinco curvas rotuladas $\rho = 0.6$ (sólo 40 repeticiones), $\rho = 0.5$, $\rho = 0.4$, $\rho = 0.3$ y $\rho = 0.2$.
> A diferencia de la figura 15-4, ahora **todas** las curvas decrecen desde el principio, aproximándose a rectas descendentes (pendiente ≈ 1 en 2):
> - $\rho = 0.6$: desde ≈0.95 en n=10 hasta ≈0.40 en n≈100, con un escalón local (baja a ≈0.47 en n≈40, sube a ≈0.55 en n≈50, vuelve a bajar).
> - $\rho = 0.5$: desde ≈0.57 en n=10 hasta ≈0.24 en n≈100.
> - $\rho = 0.4$: desde ≈0.45 en n=10 hasta ≈0.17 en n≈100.
> - $\rho = 0.3$: desde ≈0.20 en n=10, ≈0.10 en n≈40, pequeño repunte a ≈0.09 en n≈60, hasta ≈0.065 en n≈100.
> - $\rho = 0.2$: desde ≈0.062 en n=10, meseta en ≈0.05 entre n≈15 y n≈27, luego baja hasta ≈0.021 en n≈100.

**FIGURA 15-6.** Variación de la desviación estándar con el tamaño de la muestra, quitando el periodo inicial.

--- pág. 331 ---

> [NOTA AL MARGEN pág. 331: anotación manuscrita a lápiz en el margen superior, apenas legible. Se distingue algo como "N = 5 = P" en la línea superior y, debajo, "n = tamaño del lote". Hay además unos trazos verticales encima, tipo diagrama de barras/segmentos.]

*Verificación de los resultados de simulación*    **331**

gitud de cola en que el experimento se realiza muestreando la longitud de la cola a intervalos uniformes, de manera que cada observación es una medida individual de la misma variable aleatoria.

Una corrida completa consiste en $N$ observaciones que se descomponen en $p$ lotes de tamaño $n$, de manera que $N = np$. (Se supone que $n$ es exactamente divisible entre $p$.) En efecto, el experimento equivale a repetir un experimento de longitud $n$ un total de $p$ veces, en que el estado final de una corrida es el estado inicial de la siguiente. Se prefiere esta manera de repetir una corrida a iniciar cada corrida a partir de un estado de ocio inicial, ya que el estado al final de un lote es un estado inicial más razonable que el de ocio. Sin embargo, la conexión entre los lotes introduce correlación. A veces se puede separar los lotes en intervalos en que se descartan las mediciones para eliminar la correlación. Es claro que esto desperdicia información útil. Conway⁷ demuestra que la variancia que deba de esperarse utilizando todos los datos y aceptando la correlación entre los lotes es menor que la que se obtiene de la cantidad reducida de datos obtenida separando los lotes. En consecuencia, parece preferible trabajar con lotes próximos.

El método de la media del lote tiene la ventaja del método de la repetición sin la necesidad de eliminar el sesgo inicial en cada repetición. Sin embargo, es necesario suponer que las medias de los lotes individuales son independientes. Se puede justificar la suposición si es suficiente la longitud del lote. El efecto de la autocorrelación es que el valor de una parte de los datos afecta el valor de los siguientes. El efecto disminuye al aumentar la separación entre los datos y se puede ignorar razonablemente más allá de determinado tamaño de intervalo. Si el tamaño del lote es mayor que este intervalo, se puede considerar a las medias de los lotes como independientes. Es cuestión de juicio elegir un tamaño adecuado de lote. Se podría especular en forma razonable que el intervalo en el cual se mide el lote debe de ser al menos tan grande como el intervalo que se excluye del inicio de una corrida para quitar el sesgo inicial. Si se ha determinado ese valor, también se puede usar como tamaño de lote. Sin embargo, el único procedimiento útil es utilizar una corrida de prueba en la cual probar un tamaño de lote y determinar la presencia de correlación en los resultados⁷. Otro enfoque es repetir los cálculos con diferentes tamaños de lotes y probar si hay consistencia en los resultados⁸. Haciendo que los tamaño de los lotes sean múltiples entre sí, es posible realizar la operación en una sola corrida.

Al estudiar el método de la repetición, se señaló que hay un equilibrio entre el número de repeticiones y la longitud de la corrida. Con

--- pág. 332 ---

**332    Simulación de sistemas**

el método de los lotes hay un equilibrio semejante entre el tamaño del lote y el número de ellos. Ya que el número de los lotes corresponde a la cantidad de muestras de una distribución normal supuesta, de nuevo es aconsejable mantener este número en un límite razonable para satisfacer y maximizar el tamaño del lote, para reducir la correlación entre lotes.

Un aspecto práctico importante del método de los lotes es que no comprenda la presencia simultánea de todos los datos para realizar los cálculos. Es posible calcular las medias de los lotes según se desarrolla la corrida de simulación. Solo se requiere espacio de computador para acumular la suma de las medias de los lotes y la suma de sus cuadrados, junto con una acumulación de los números que forman la media del lote actual. Si se recaban tamaños de lotes múltiples, se necesita un conjunto de tres de esos números por cada tamaño de lote.

## 15-7  Análisis de series de tiempo

> [La página se corta acá: solo se ve el título de la sección 15-7, sin texto.]

---

# Plantilla Inventario.pdf

--- pág. 1 ---

> Página sin texto corrido. Contiene **dos copias idénticas** de la misma plantilla en blanco
> (un recuadro arriba y otro abajo de la hoja), para completar a mano.

> [FIGURA pág. 1 — Plantilla en blanco del modelo de inventario, esquema tipo "estado / eventos / contadores".]
> Cada copia es un rectángulo grande dividido por una línea vertical punteada en dos mitades:
>
> **Mitad izquierda — "Estado del Sistema"**: seis cuadros vacíos dispuestos en tres filas de dos, rotulados debajo de cada cuadro:
> - fila 1: `I(t)` y `I+`
> - fila 2: `I-` y `Ultimo pedido`
> - fila 3: `s` y `S`
>
> **Mitad derecha, sector superior — "Eventos"**: a la izquierda un cuadro grande vacío (reloj / tiempo de simulación); a la derecha una columna de cuatro celdas vacías apiladas (la lista de eventos), rotuladas a su derecha de arriba hacia abajo:
> - `arribo de pedidos`
> - `arribo de cliente`
> - `fin de simulacion`
> - `evaluación inventario`
>
> **Mitad derecha, sector inferior** (separado por una línea horizontal punteada) — **"Contadores estadísticos"**: cuatro cuadros vacíos en fila, rotulados debajo:
> - `Costo pedidos`
> - `Costo pedidos acumulado`
> - `A(I+)`
> - `A(I-)`

---

# 2025-10-04.pdf — Examen Parcial de Simulación

> El PDF tiene 2 páginas; cada una es la foto de **dos hojas del examen** puestas lado a lado.
> El texto fluye de la hoja izquierda a la hoja derecha. Las respuestas están marcadas a
> mano con un círculo sobre la letra de la opción elegida; se indican abajo con **(marcada)**.
> El nombre del alumno está tachado con marcador verde en la carátula.

--- pág. 1 del PDF — hoja izquierda ---

**[404] Examen Parcial de Simulación. Apellido y Nombre:** ██████████ *(tachado con marcador verde)*

---

**1.1  Preg.** ¿Qué propiedad caracteriza a una variable aleatoria geométrica?
- A Representa el número de ensayos necesarios para obtener el primer éxito
- B Su media es $1/p$ y su varianza es $(1-p)/p^2$
- C Es la suma de variables aleatorias de Bernoulli independientes
- **D Las opciones A y B son correctas** *(marcada)*
- E Todas las opciones anteriores son correctas

**1.2  Preg.** En el sistema de colas de un solo servidor, ¿cuáles son las tres medidas de rendimiento principales que se estiman?
- A Tiempo promedio de servicio, número promedio de clientes en el sistema, utilización del servidor
- B Retraso promedio en cola, número promedio de clientes en cola, proporción de tiempo que el servidor está ocupado
- C Tiempo promedio de llegada, tiempo promedio de salida, longitud promedio de la cola
- D Solo el retraso promedio en cola y la utilización del servidor
- **E Las opciones A y B son correctas** *(marcada)*

**1.3  Preg.** En el sistema de inventario, ¿qué representa la política (s, S)?
- A Una política donde se ordena una cantidad fija s cuando el inventario llega a S
- B Una política donde se ordena hasta S si el inventario I es menor que s, y no se ordena nada si $I \geq s$
- C Una política donde se ordena s unidades cada S períodos
- D Una política que asegura que el inventario siempre está entre s y S unidades
- **E Las opciones B y D son correctas** *(marcada)*

**1.4  Preg.** Según el texto, ¿cuál es la definición de un sistema en el contexto de simulación?
- A Un conjunto de ecuaciones matemáticas que describen un proceso
- B Una colección de entidades que actúan e interactúan juntas hacia el logro de algún fin lógico
- C Un modelo computacional que imita el comportamiento de un proceso real
- D Un algoritmo que genera números aleatorios para simular eventos
- **E Todas las opciones anteriores son correctas** *(marcada)*

**1.5  Preg.** En un proceso de Poisson homogéneo con tasa $\lambda$, ¿cuál de las siguientes condiciones define correctamente el proceso?
- A $N(0) = 0$ y los números de eventos en intervalos disjuntos son independientes
- B La distribución del número de eventos depende solo de la longitud del intervalo
- C $\lim P\{N(h) = 1\}/h = \lambda$ cuando $h \to 0$
- **D Todas las opciones anteriores son correctas** *(marcada)*
- E Solo las opciones A y C son correctas

**1.6  Preg.** En los modelos de colas con población de clientes finita, la tasa de llegada...
- **A ...varía con el tiempo** *(marcada)*
- B ...aumenta conforme aumenta el número de clientes en el sistema.
- C ...disminuye conforme aumenta el número de clientes en el sistema
- D ...es constante
- E Las opciones A y C son correctas

**1.7  Preg.** ¿Qué representa la intensidad de tráfico ($\rho$) en un sistema de colas?
- A El número promedio de clientes en el sistema
- **B El cociente de la tasa de llegadas ($\lambda$) entre la tasa de servicio ($\mu$)** *(marcada)*
- C El tiempo promedio de espera en la cola
- D La probabilidad de que el sistema esté vacío
- E Las opciones B y D son correctas

**1.8  Preg.** ¿Qué condición debe cumplirse para que un sistema M/M/1 alcance el estado estable?
*(el número "1.8" queda cortado en el borde izquierdo de la foto; se deduce por secuencia)*
- A La tasa de llegadas debe ser mayor que la tasa de servicio

*(la pregunta 1.8 continúa en la hoja derecha)*

--- pág. 1 del PDF — hoja derecha ---

*(continuación de 1.8)*
- **B La tasa de servicio ($\mu$) debe ser mayor que la tasa de llegadas ($\lambda$)** *(marcada)*
- C El número de servidores debe ser mayor que 1
- D La capacidad del sistema debe ser finita
- E Las opciones A y C son correctas

**1.9  Preg.** ¿Cuál es la principal ventaja de usar el enfoque "next-event time advance" en simulación?
- A Proporciona mayor precisión en los cálculos
- B Permite saltar períodos de inactividad, ahorrando tiempo de computación
- C Es más fácil de programar que otros enfoques
- D Genera resultados más estables
- **E Las opciones B y C son correctas** *(marcada)*

**1.10  Preg.** ¿Cuál es la principal diferencia entre la verificación y la validación del modelo en un estudio de simulación?
- A La verificación comprueba que el modelo funcione correctamente, mientras que la validación compara el modelo con la realidad
- B La verificación se realiza antes de la validación
- C La verificación utiliza información de entrada real, mientras que la validación utiliza datos simulados
- D La verificación es opcional, mientras que la validación es obligatoria
- **E Las opciones A y B son correctas** *(marcada)*

**1.11  Preg.** En el mecanismo de avance de tiempo "next-event time advance", ¿qué sucede con los períodos de inactividad?
- A Se procesan paso a paso con incrementos fijos de tiempo
- **B Se saltan completamente, avanzando directamente al siguiente evento** *(marcada)*
- C Se simulan con mayor detalle para obtener mayor precisión
- D Se registran pero no se procesan
- E Las opciones A y C son correctas

**1.12  Preg.** ¿Cuál es la relación entre las variables aleatorias binomial y Poisson cuando n es grande y p es p[equeño]? *(el final de la línea queda cortado en el borde derecho de la foto)*
- A La distribución binomial se aproxima a la distribución Poisson con parámetro $\lambda = np$
- B Ambas distribuciones tienen la misma varianza
- C La distribución Poisson es siempre una aproximación exacta de la binomial
- D Solo cuando $n > 100$ y $p < 0.1$
- **E Las opciones A y D son correctas** *(marcada)*

**1.13  Preg.** En un proceso de Poisson no homogéneo, ¿qué característica lo diferencia del proceso hom[ogéneo]? *(cortado en el borde derecho)*
- **A La tasa $\lambda$ varía en función del tiempo** *(marcada)*
- B Los intervalos entre eventos no son exponenciales
- C La propiedad de incrementos independientes no se mantiene
- D Las opciones A y B son correctas
- E Todas las opciones anteriores son correctas

**1.14  Preg.** En el contexto de simulación, ¿cuál es el propósito principal de los "números aleatorio[s]"? *(cortado en el borde derecho)*
- A Generar valores de variables aleatorias con distribuciones arbitrarias
- B Simular posibles ocurrencias del modelo probabilístico
- C Proporcionar la base para estudios de simulación
- D Las opciones A y B son correctas
- **E Todas las opciones anteriores son correctas** *(marcada)*

**1.15  Preg.** ¿Cuál es el segundo paso en un estudio de simulación?
- A Recolección y análisis de datos
- **B Generación del modelo de simulación base** *(marcada)*
- C Validación del modelo
- D Determinación de escenarios
- E Las opciones A y B son correctas

--- pág. 2 del PDF — hoja izquierda ---

**2.1  Preg.** La simulación reemplaza a la solución analítica como método de resolución de problemas complejos con solución.
- **V Verdadero** *(marcada)*
- F Falso

**2.2  Preg.** Para poder simular es necesario contar con información de funcionamiento de la realidad o estimaciones del mismo.
- **V Verdadero** *(marcada)*
- F Falso

**2.3  Preg.** Un modelo es un recorte de características observables de la realidad y solo puede ser usado si está totalmente testeado.
- V Verdadero
- **F Falso** *(marcada)*

**2.4  Preg.** Para la construcción de modelos es necesario herramientas informáticas siempre.
- V Verdadero
- **F Falso** *(marcada)*

**2.5  Preg.** La simulación por computadora surgió en los últimos 30 años.
- V Verdadero
- **F Falso** *(marcada)*

**2.6  Preg.** La programación orientada a objetos no es imprescindible para realizar simulaciones.
- V Verdadero
- **F Falso** *(marcada)*

**2.7  Preg.** La solución analítica es exacta.
- **V Verdadero** *(marcada)*
- F Falso

**2.8  Preg.** LaTeX es un sistema de composición de textos, orientado a la creación de documentos escritos que presenten una alta calidad tipográfica. Por sus características y posibilidades, es usado de forma especialmente intensa en la generación de artículos y libros científicos que incluyen, entre otros elementos, expresiones matemáticas.
- **V Verdadero** *(marcada)*
- F Falso

**2.9  Preg.** Sobre los números pseudoaleatorios...
- **A Se generan de manera secuencial con un algoritmo determinístico.** *(marcada)*
- **B Se denomina de ciclo completo cuando el conjunto de números pseudoaleatorios generados repite siempre el mismo número, luego de generar un gran conjunto de números distintos.** *(marcada)*
- **C El método de la parte media del cuadrado es un método vigente para la generación de números pseudoaleatorios.** *(marcada)*
- D Los números pseudoaleatorios pueden generarse con cualquier computadora a altas velocidades.

**2.10  Preg.** Verdaderos números aleatorios.
- **A Es preferible en simulaciones de alto rendimiento usar un conjunto de números aleatorios y no pseudoaleatorios.** *(marcada)*
- **B En general los números aleatorios se basan en alguna fuente de aleatoriedad física que puede ser teóricamente impredecible (cuántica) o prácticamente impredecible (caótica).** *(marcada)*

**2.11  Preg.** Los modelos de la cola simple y de inventario empleados durante los TPI de clase...
*(el número queda cortado en el borde izquierdo de la foto; se deduce por secuencia)*
- **A Son modelos simples que pueden ser simulados y que también se cuenta con la solución analítica de los mismos.** *(marcada)*
- B Solo pueden ser simulados si se tiene la solución analítica.
- C La solución analítica puede ser comparada con las respuestas obtenidas de las simulaciones.
- D Las respuestas obtenidas mediante simulaciones son generalmente similares al de la solución analítica.

**2.12  Preg.** Los eventos a tratar en el modelo de cola simple, en el paradigma de simulación basado en eventos discretos, son...
*(el número queda cortado en el borde izquierdo de la foto; se deduce por secuencia)*
- **A Arribo.** *(marcada)*

*(la pregunta 2.12 continúa en la hoja derecha)*

--- pág. 2 del PDF — hoja derecha ---

*(continuación de 2.12)*
- **B Partida.** *(marcada)*
- C Inicio.
- D Finalización.
- **E Poner el servidor ocupado/desocupado.** *(marcada)*

**2.13  Preg.** Las medidas de rendimiento más importantes a calcular en el problema de cola simple son...
- **A Tiempo de espera en el servidor.** *(marcada)*
- **B Tiempo de arribo.** *(marcada)*
- C Cantidad de veces que el cliente paso por el servidor.
- **D Utilización del servidor.** *(marcada)*

**2.14  Preg.** Si la tasa de arribos es mayor que la tasa de servicio no es posible realizar la simulación.
- V Verdadero
- **F Falso** *(marcada)*

**2.15  Preg.** Si la tasa de arribos es menor que la tasa de servicio no es posible obtener una solución analítica.
- V Verdadero
- **F Falso** *(marcada)*

**2.16  Preg.** ¿Cuáles paradigmas de simulación son los explicados en AnyLogic en 3 días?
- **A Basado en agentes.** *(marcada)*
- **B Sistemas dinámicos.** *(marcada)*
- **C Eventos discretos.** *(marcada)*
- D Peatones.
- E Caminos.
- F GIS.

**2.17  Preg.** GIS es un sistema geográfico monocapa para analizar cuestiones concretas de una zona particular.
- **V Verdadero** *(marcada)*
- F Falso

---

**3.**  Determine el costo total promedio mensual para un sistema de inventario con la política de pedidos vista en clase, y con estos datos:

Tiempo entre demandas: variable aleatoria exponencial con media 0,55.

Demora del proveedor: variable aleatoria uniforme en el intervalo $[0,5;\ 1]$.

Tamaño de la demanda:

$$D = \begin{cases} 3 & \text{con probabilidad } 1/3 \\ 4 & \text{con probabilidad } 1/6 \\ 5 & \text{con probabilidad } 1/6 \\ 6 & \text{con probabilidad } 1/3 \end{cases}$$

Parámetros para los costos: $K = 50$; $i = 5$; $h = 2,5$; $\pi = 6$.

Restantes parámetros: $s = 30$; $S = 60$; $I0 = 40$.

Números aleatorios: $0.9501 - 0.1304 - 0.9700 - 0.3546 - 0.9258$.
