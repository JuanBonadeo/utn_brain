# Tecnicas de Simulación en Computadoras - Naylor Cap. 4.pdf

> Transcripción de las páginas 16 a 29 del PDF (= páginas 114 a 141 del libro impreso).
> Cada página del PDF contiene un pliego doble: la página par a la izquierda y la impar a la derecha.

---

--- pág. 114 ---

**114  GENERACIÓN DE VALORES DE LAS VARIABLES**

```
1. SUBROUTINE NORMAL (EX, STDX, X)
2. SUM = 0.0
3. DO 5 I = 1, 12
4. R = RND (R)
5. SUM = SUM + R
6. X = STDX * (SUM − 6.0) + EX
7. RETURN
```

**Figura 4-16.** Subrutina FORTRAN para generar valores de variable aleatoria con distribución normal.

### El procedimiento directo [3]

Sean $r_1$ y $r_2$ dos valores de variable aleatoria independientes distribuidos de modo uniforme y definidos en el intervalo (0, 1), entonces:

$$x_1 = (-2 \log_e r_1)^{1/2} \cos 2\pi r_2 \qquad (4\text{-}81)$$

$$x_2 = (-2 \log_e r_1)^{1/2} \operatorname{sen} 2\pi r_2, \qquad (4\text{-}82)$$

serán dos valores de variable aleatoria obtenidos a partir de una distribución normal estándar. Con este método se logran resultados exactos y su velocidad de cómputo se puede comparar con la del método del límite central, sujeto a la eficiencia de ciertas subrutinas para funciones especiales [21, p. 382].

### El procedimiento rápido [19]

Se afirma que esta técnica es la más rápida, aunque se le imputa que emplea varios cientos de ubicaciones de memoria para almacenar en la computadora ciertas constantes específicas. Las desviaciones aleatorias normales se calculan a partir de la mezcla de tres densidades:

$$f(x) = 0.9578 g_1(x) + 0.0395 g_2(x) + 0.0027 g_3(x). \qquad (4\text{-}83)$$

Los fundamentos racionales en los que se basa esta mezcla establecen que del 95 al 87 por ciento del tiempo sólo se usa $g_1(x)$, lo cual proporciona inmediatamente una variable normal con una tabla de longitud mínima. Las otras dos funciones son considerablemente más complicadas; si se desean mayores detalles o información sobre las constantes que emplea este procedimiento, se encontrarán en la referencia que se cita.

También pueden emplearse otros caminos, para generar valores de variable aleatoria normales, como el *método de Von Neumann* y el *método de Hastings*, aunque ninguno de estos métodos ofrece más simplicidad, precisión o rapidez, que los vistos previamente.

---

--- pág. 115 ---

**DISTRIBUCIONES CONTINUAS DE PROBABILIDAD  115**

Las siguientes distribuciones se derivan de la distribución normal y por lo tanto, se pueden simular en forma indirecta por medio de ciertas funciones cuyos argumentos sean valores de variable aleatoria con distribución normal.

La distribución Ji cuadrada se obtiene mediante la suma de los cuadrados de los valores de variable aleatoria independientes, que obedecen a una distribución normal estándar. La variable Ji cuadrada se denota por

$$x = \chi_m{}^2 = \sum_{i=1}^{m} z_i{}^2, \qquad (4\text{-}84)$$

donde $z_i$ es una variable normal estándar y $m$ representa los *grados de libertad*. La función de densidad $\chi_m{}^2$ o $x$ es una densidad gamma (véase la ecuación 4-48), con $k = m/2$ y $\alpha = 1/2$. En consecuencia,

$$f(x) = \frac{x^{\frac{m}{2}-1} e^{-\frac{x}{2}}}{2^{\frac{m}{2}}\left(\frac{m}{2}-1\right)!}, \qquad (4\text{-}85)$$

y $EX = m$ y $VX = 2m$.

Esta distribución queda completamente descrita una vez conocidos los grados de libertad y se pueden, por lo tanto, simular muy fácilmente mediante la ecuación (4-54) si $m$ resulta par. Cuando se trate de grados de libertad impares y $m < 30$, pueden utilizarse las fórmulas (4-55) o (4-84); mientras que si $m > 30$ se podrá emplear el criterio de la aproximación normal para variables Ji cuadrada, basado en la conocida fórmula:

$$z = \sqrt{2\chi_m{}^2} - \sqrt{2m-1}. \qquad (4\text{-}86)$$

Resolviendo para el valor Ji cuadrado $\chi_m{}^2$, obtenemos:

$$x = \chi_m{}^2 = \frac{\left(z + \sqrt{2m-1}\right)^2}{2}. \qquad (4\text{-}87)$$

La distribución $t$ describe una variable aleatoria tal, que

$$t = \frac{z}{\sqrt{\chi_m{}^2/m}} \qquad (4\text{-}88)$$

con una función de densidad

$$f(t) = \frac{\Gamma\left(\frac{m+1}{2}\right)}{\Gamma\left(\frac{m}{2}\right)\left[\pi m\left(1 + \frac{t^2}{m}\right)^{m+1}\right]^{1/2}}. \qquad (4\text{-}89)$$

La distribución acumulativa correspondiente a la distribución $t$ se encuentra disponible tan sólo en forma tabular; $EX = 0$ y $VX = m/(m-2)$.

---

--- pág. 116 ---

**116  GENERACIÓN DE VALORES DE LAS VARIABLES**

Para propósitos de simulación se puede usar la fórmula (4-88) o sea, el cociente que se obtiene entre los valores de variable aleatoria con distribución normal estándar y los valores de variable aleatoria distribuidos en forma Ji cuadrada; en forma alternativa, es posible utilizar un valor de variable aleatoria distribuida en forma normal estándar, cuya variancia sea $m/(m-2)$. Para $m > 30$, bastará con que se aplique el criterio directo de la aproximación normal.

La distribución $F$ corresponde a la distribución de probabilidad de los cocientes que se obtienen entre las sumas correspondientes de los cuadrados de los valores de variable aleatoria con distribución normal. En otras palabras, se puede representar la variable $F$ bajo la siguiente notación:

$$F_{m,n} = \frac{\chi_m{}^2/m}{\chi_n{}^2/n}, \qquad (4\text{-}90)$$

donde $m$ y $n$ representan los correspondientes grados de libertad de las sumas independientes, al igual que los valores Ji cuadrados. Tanto la función de densidad como la acumulativa de las variables $F$ son lo suficientemente complicadas como para incluirlas en este libro; sin embargo, sus momentos son relativamente simples [31, p. 187], es decir,

$$EX = \frac{n}{n-2}, \qquad n > 2 \qquad (4\text{-}91)$$

$$VX = \frac{2n^2(m+n-2)}{m(n-2)^2(n-4)}, \qquad n > 4. \qquad (4\text{-}92)$$

Finalmente, conviene anotar que los valores $F$ se pueden simular mediante el uso de las ecuaciones (4-90) y (4-84) o bien, con la ecuación (4-54).

### La distribución normal multivariada

Esta distribución está definida por un vector de variables aleatorias para el que cada una de sus componentes representa una variable aleatoria normal, con una media y variancia conocidas. Cuando el conjunto de componentes de este vector normal aleatorio son independienttes entre sí, la generación de vectores aleatorios normales se seguirá en forma directa de las técnicas ya discutidas en la sección anterior. Pero si las componentes del vector aleatorio normal son dependientes, entonces, las covariancias entre las variables que representan las componentes serán distintas de cero, y será indispensable el uso de la matriz variancia-covariancia para lograr la generación de vectores aleatorios normales.

Denotaremos por $\mathbf{x}$ al vector aleatorio normal de $m$ dimensiones, con $E(\mathbf{x}) = \boldsymbol{\mu}$, donde $\boldsymbol{\mu}$ corresponde al vector media.

---

--- pág. 117 ---

**DISTRIBUCIONES CONTINUAS DE PROBABILIDAD  117**

Supondremos que $\mathbf{x}$ tiene una matriz $\mathbf{V}$ de variancia-covariancia dada por

$$\mathbf{V} = E[(\mathbf{x}-\boldsymbol{\mu})\cdot(\mathbf{x}-\boldsymbol{\mu})] = \begin{bmatrix} \sigma_{11} & \cdots & \sigma_{1m} \\ \cdots & \cdots & \cdots \\ \sigma_{m1} & \cdots & \sigma_{mm} \end{bmatrix}. \qquad (4\text{-}93)$$

En la expresión para $\mathbf{V}$, convencionalmente $\sigma_{ii}$ denota la variancia de la $i$-ésima componente, y $\sigma_{ij}$ denota la covariancia entre las componentes $i$-ésima y $j$-ésima del vector aleatorio. La teoría nos asegura que $\mathbf{V}$ es una matriz siempre simétrica para la cual existe su inversa $\mathbf{V}^{-1}$ [2].

La función de densidad de probabilidad de $\mathbf{x}$ está dada por:

$$f(\mathbf{x}) = |2\pi\mathbf{V}|^{-1/2} \exp[-1/2(\mathbf{x}-\boldsymbol{\mu})'\mathbf{V}^{-1}(\mathbf{x}-\boldsymbol{\mu})], \qquad (4\text{-}94)$$

donde $|2\pi\mathbf{V}|$ representa al determinante de la matriz $2\pi\mathbf{V}$.

La integral de la ecuación (4-94) resulta muy complicada y desconocemos si existen tablas de áreas de probabilidad para vectores aleatorios normales con más de tres componentes [12]. Esta es una de las razones por las que podemos eventualmente necesitar el proceso de simulación de vectores normales al azar. La otra razón está dada por la frecuencia con que ocurre la dependencia entre variables normales en sistemas interdependientes.

En la generación de vectores normales al azar con un vector media y una matriz de variancia-covariancia dados, se requiere el empleo de un teorema [2, p. 19] que establece: si $\mathbf{z}$ es un vector normal estándar, esto es, contiene como componentes las variables normales con media nula y variancia unitaria, entonces existe una única matriz bajo triangular $\mathbf{C}$, tal que

$$\mathbf{x} = \mathbf{C}\mathbf{z} + \boldsymbol{\mu}. \qquad (4\text{-}95)$$

En este caso $(\mathbf{x}-\boldsymbol{\mu})$ tiene una matriz de variancia-covariancia dada por:

$$\mathbf{V} = \mathbf{C}\cdot\mathbf{C}'. \qquad (4\text{-}96)$$

A fin de obtener $\mathbf{C}$ de $\mathbf{V}$ se puede utilizar el llamado *método de la raíz cuadrada*, que proporciona un conjunto de fórmulas necesarias para la computación de los elementos de $\mathbf{C}$ [26].

$$\left. \begin{aligned} c_{i1} &= \frac{\sigma_{i1}}{\sigma_{11}{}^{1/2}}, && 1 \le i \le m \\[4pt] c_{ii} &= \left(\sigma_{ii} - \sum_{k=1}^{i-1} c_{ik}{}^2\right)^{1/2} && 1 < i \le m \\[4pt] c_{ij} &= \frac{\left(\sigma_{ij} - \sum_{k=1}^{j-1} c_{ik}c_{jk}\right)}{c_{jj}} && 1 < j < i \le m. \end{aligned} \right\} \qquad (4\text{-}97)$$

---

--- pág. 118 ---

**118  GENERACIÓN DE VALORES DE LAS VARIABLES**

Puesto que $\mathbf{C}$ es bajo triangular, $c_{ij} = 0$ para toda $j > i$. Una vez obtenidos todos los elementos de $\mathbf{C}$, se pueden determinar todas las componentes de $\mathbf{x}$ mediante sumas pesadas a partir de $\mathbf{z}$:

$$x_i = \Sigma c_{ij} z_i + \mu_i. \qquad (4\text{-}98)$$

La generación de un vector aleatorio $\mathbf{x}$ con media $\mu$ y una matriz de variancia-covariancia $\mathbf{V}$, puede programarse de la siguiente manera.

1. Obtener a partir de $\mathbf{V}$ una matriz triangular $\mathbf{C}$ de acuerdo con la ecuación (4-97).

2. Generar $m$ valores de variable aleatoria independientes con distribución normal estándar, cuya media sea cero y su variancia igual a uno, según la figura 4-16, o por medio de algún otro método equivalente.

3. Multiplicar y sumar los vectores y matrices tal como lo indican las expresiones (4-95) ó (4-98); en el resultado se obtendrá un vector aleatorio a partir de la distribución multivariada definida por $\mu$, $\mathbf{V}$ y la ecuación (4-94).

Las técnicas para generar vectores tomando como base distribuciones normales multivariadas, se pueden emplear en aquellos problemas en los que se deben generar variables aleatorias normales con una correlación previamente prescrita. Aquí se demuestra cómo funciona este orden de ideas cuando se tiene un caso con dos variables aleatorias normales $x_1$ y $x_2$ que están correlacionadas y para las cuales $E(x_1) = \mu_1$, $E(x_2) = \mu_2$, $\operatorname{Var}(x_1) = \sigma_1{}^2$, $\operatorname{Var}(x_2) = \sigma_2{}^2$, $\operatorname{Cov}(x_1, x_2) = \rho\sigma_1\sigma_2$. En consecuencia,

$$\mathbf{V} = \begin{bmatrix} \sigma_1{}^2 & \rho\sigma_1\sigma_2 \\ \rho\sigma_1\sigma_2 & \sigma_2{}^2 \end{bmatrix}, \qquad (4\text{-}99)$$

$$\mathbf{C} = \begin{bmatrix} \sigma_1 & 0 \\ \rho\sigma_2 & \sigma_2\sqrt{1-\rho^2} \end{bmatrix}, \qquad (4\text{-}100)$$

y

$$\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \mathbf{C}\mathbf{z} + \mu = \begin{bmatrix} \sigma_1 z_1 \\ \sigma_2(\rho z_1 + \sqrt{1-\rho^2}\cdot z_2) \end{bmatrix} + \begin{bmatrix} \mu_1 \\ \mu_2 \end{bmatrix}. \qquad (4\text{-}101)$$

Esto significa que $x_1$ y $x_2$ se han generado como valores de variable aleatoria normales, que están correlacionadas con un coeficiente de correlación $\rho$. El ejemplo muestra cómo se pueden generar dos valores normales correlacionados partiendo de dos valores normales estándar independientes por medio del proceso de transformación descrito en la ecuación (4-95).

---

--- pág. 119 ---

**DISTRIBUCIONES CONTINUAS DE PROBABILIDAD  119**

### La distribución logarítmica normal

Si el logaritmo de una variable aleatoria tiene una distribución normal entonces la variable aleatoria tendrá una distribución continua sesgada positivamente, conocida con el nombre de distribución logarítmica normal. Frecuentemente se usa esta distribución para describir procesos aleatorios que representan el producto de varios eventos pequeños e independientes [5]. Esta propiedad de la distribución logarítmica normal es conocida como *ley de efectos proporcionales*, que establecen una base sobre la que podemos decidir la validez con la cual una distribución logarítmica normal sirva o no para describir una variable aleatoria particular.

Las aplicaciones más importantes de la distribución logarítmica normal quedan comprendidas en áreas del análisis de rendimientos y ganancias, análisis de ventas y teoría de puntos de ruptura. Esta última proporciona criterios básicos para identificar la distribución de ciertos tamaños de lotes (inclusive tamaño de empresas o receptores de petróleo, etc.), así como también la distribución del ingreso, la cual se comporta en forma logarítmica normal [1, 8]. Por ejemplo, en lugar de estratificar un conjunto de datos numéricos asociados a algún concepto como el ingreso (o las ventas), utilizando una distribución normal, podemos emplear esta misma distribución sólo que aplicada a los logaritmos de esos valores numéricos que queremos jerarquizar. En consecuencia, muy próximos al extremo superior de la escala logarítmica se encuentran pequeñas diferencias logarítmicas asociadas a las diferencias encontradas en los argumentos (los ingresos), mientras que en el extremo opuesto (de pequeños valores), las mismas diferencias en argumentos están asociadas a logaritmos cuya diferencia entre valores resulta mayor. Por consiguiente, la escala logarítmica proporciona el efecto de comprimir la distribución del ingreso en los niveles altos y ampliar la distribución en los niveles bajos. Una distribución de este tipo puede resultar con gran tendencia a cambiar, cualquier distribución sesgada positivamente en una distribución aproximadamente simétrica, lo cual constituye una de sus más valiosas características.

Se dice que $X$ tiene una distribución logarítmica normal si cuando solamente se consideran los valores positivos de $x$, el logaritmo (en base $e$) de la variable aleatoria $X$ tiene una función de densidad $f(y)$ dada como sigue:

$$f(y) = \frac{1}{\sigma_y \sqrt{2\pi}} \exp\left[\left(-\frac{1}{2}\right)\left(\frac{y-\mu_y}{\sigma_y}\right)^2\right] \quad -\infty < y < \infty, \qquad (4\text{-}102)$$

con $y = \log x$. Los parámetros $\mu$ y $\sigma_y{}^2$ que aparecen en la expresión, corresponden a la media y variancia de $y$, respectivamente.

---

--- pág. 120 ---

**120  GENERACIÓN DE VALORES DE LAS VARIABLES**

El valor esperado y la variancia de los valores de variable aleatoria, distribuidos en forma logarítmica normal $x$, están dados por las fórmulas siguientes:

$$EX = \exp\left(\mu_y + \frac{\sigma_y{}^2}{2}\right) \qquad (4\text{-}103)$$

$$VX = [\exp(2\mu_y + \sigma_y{}^2)][\exp(\sigma_y{}^2) - 1] \qquad (4\text{-}104)$$
$$= (EX)^2[\exp(\sigma_y{}^2) - 1].$$

La simulación de valores de variable aleatoria logarítmica normal con una media y variancia dadas, requiere necesariamente que $\mu_y$ y $\sigma_y{}^2$ estén expresadas en términos de $EX$ y de $VX$, lo cual se puede lograr con sólo resolver la ecuación (4-104) para $\exp(\sigma_y{}^2)$. Tenemos, que

$$\frac{VX}{(EX)^2} = \exp(\sigma_y{}^2) - 1 \qquad (4\text{-}105)$$

$$\exp(\sigma_y{}^2) = \frac{VX}{(EX)^2} + 1. \qquad (4\text{-}106)$$

Tomando ahora el logaritmo de ambos miembros de la ecuación (4-106) obtenemos

$$\sigma_y{}^2 = \log\left[\frac{VX}{(EX)^2} + 1\right]. \qquad (4\text{-}107)$$

A continuación, tomamos el logaritmo de ambos miembros de la ecuación (4-103)

$$\log(EX) = \mu_y + \frac{\sigma_y{}^2}{2} \qquad (4\text{-}108)$$

y resolvemos para $\mu_y$

$$\mu_y = \log(EX) - \frac{1}{2}\log\left[\frac{VX}{(EX)^2} + 1\right] \qquad (4\text{-}109).$$

Ahora que tanto $\mu_y$ como $\sigma_y{}^2$ han quedado expresadas en términos de la media y la variancia de $x$, el valor logarítmico normal de la variable aleatoria que se va a generar o sea el valor de variable aleatoria $z$ con distribución normal estándar, se puede definir como sigue:

$$z = \frac{\log x - \mu_y}{\sigma_y}. \qquad (4\text{-}110)$$

Resolviendo la ecuación (4-110) para $\log x$ y tomando el antilogaritmo de ambas partes de la ecuación, obtendremos

$$\log x = \mu_y + \sigma_y z \qquad (4\text{-}111)$$

$$x = \exp(\mu_y + \sigma_y z). \qquad (4\text{-}112)$$

---

--- pág. 121 ---

*[En el margen superior de esta página hay un sello de biblioteca superpuesto al encabezado, parcialmente ilegible: se alcanza a leer "BIBLIOTECA" y debajo un texto borroso ilegible.]*

**DISTRIBUCIONES DISCRETAS DE PROBABILIDAD  121**

Substituyendo el valor de $z$ de la ecuación (4-73) en la ecuación (4-112), tendremos

$$x = \exp\left[\mu_y + \sigma_y\left(\frac{K}{12}\right)^{-1/2}\left(\sum_{i=1}^{K} r_i - \frac{K}{2}\right)\right] \qquad (4\text{-}113)$$

o bien para los propósitos del programa en lenguaje FORTRAN, cuando $K = 12$,

$$\text{X} = \text{EXP (EY + STDY} * \text{(SUMR} - 6.0)). \qquad (4\text{-}114)$$

Resumiendo, para generar valores logarítmicos normales de variable aleatoria $x_1, x_2, \ldots, x_n$ con $EX$ y $VX$ dadas, debemos en primer lugar determinar $\mu_y$ y $\sigma_y$ de las ecuaciones (4-107) y (4-109), y después substituir estos valores en las ecuaciones (4-113) ó (4-114). Una vez definidos los valores de EY y de STDY el procedimiento para simular valores logarítmicos normales diferirá del procedimiento para simular valores normales en mínimos detalles, considerando tan sólo que el reemplazo de la ecuación (4-114) por la proposición 6 de la subrutina FORTRAN que aparece en la figura 4-16, bastará para lograr los resultados deseados.

## DISTRIBUCIONES DISCRETAS DE PROBABILIDAD

Se encuentra definido un número muy significativo de distribuciones de probabilidad para variables aleatorias que solamente toman valores discretos, esto es, enteros no negativos. La distribución acumulativa de probabilidad para una variable aleatoria discreta $X$ se define de manera muy similar a la de la ecuación (4-1).

$$F(x) = P(X \le x) = \sum_{X=0}^{x} f(x), \qquad (4\text{-}115)$$

donde $f(x)$ es la frecuencia o función de probabilidad de $X$, definida por valores enteros $x$ tales que:

$$f(x) = P(X = x) \qquad (4\text{-}116)$$

para $x = 0, 1, 2, \ldots$

Las distribuciones discretas de probabilidad son muy útiles cuando se las emplea como modelos estocásticos para ciertos procesos de *conteo*, ya sea sobre muestras finitas o no finitas, donde la presencia o ausencia de un atributo dicotómico está gobernada por el azar. Desde un punto de vista empírico las distribuciones discretas pueden también ocurrir como resultado de redondear medidas continuas sobre una escala discreta. Sin embargo, estrictamente hablando, las distribuciones discretas de probabilidad resultan ser los modelos más apropiados para fenómenos aleatorios cuando

---

--- pág. 122 ---

**122  GENERACIÓN DE VALORES DE LAS VARIABLES**

los valores de las variables aleatorias se pueden determinar por medio de procesos de conteo.

Las secciones siguientes contienen la descripción de técnicas para la generación de valores de variables estocásticas a partir de la mayoría de las distribuciones discretas de probabilidad más conocidas. El formato empleado en la presentación de estos métodos es semejante a la forma en que presentamos las distribuciones continuas.

### La distribución geométrica

Entre las primeras y probablemente más simples de las formulaciones matemáticas de procesos estocásticos, se encuentra la llamada *de ensayos de Bernoulli*. Estos ensayos son experimentos independientes al azar, en los que el resultado de cada ensayo queda registrado, ya sea como un éxito o un fracaso. La probabilidad de éxito se denota por $p$ $(0 \le p \le 1)$ y se supone que $p$ es constante para cualquier sucesión particular de ensayos. La probabilidad de un fracaso se denota por $q$, donde

$$q = 1 - p. \qquad (4\text{-}117)$$

Una sucesión de ensayos Bernoulli, combinada con cierto proceso de conteo, viene a constituir la base conceptual para una gran familia de distribuciones discretas de probabilidad, incluyendo la geométrica, binomial negativa, Poisson y otras distribuciones binomiales. Los valores de variable aleatoria que se generan al contar el número de fracasos en una sucesión de ensayos (o eventos) antes de que ocurra el primer éxito, son valores de variable aleatoria que se ajustan a una distribución geométrica. La distribución geométrica de probabilidad tiene un gran valor y utilidad en el área del control estadístico de calidad, así como también para las distribuciones de rezagos y movimientos en modelos econométricos.

La distribución geométrica queda descrita por la siguiente función de probabilidad:

$$f(x) = pq^x \qquad x = 0, 1, 2, \ldots. \qquad (4\text{-}118)$$

y la función de distribución acumulativa está definida por

$$F(x) = \sum_{X=0}^{x} pq^X \qquad X = 0, 1, 2, \ldots, x. \qquad (4\text{-}119)$$

Puesto que por definición se tiene $F(x) = P(X \le x)$, y como $P(X = 0) = F(0) = p$, el rango de $F(x)$ es $p \le F(x) \le 1$. Por otra parte, $P(X > x) = 1 - F(x)$, lo que implica que $P(X > 0) = q$ y además

$$1 - F(x) = q^{x+1}. \qquad (4\text{-}120)$$

---

--- pág. 123 ---

**DISTRIBUCIONES DISCRETAS DE PROBABILIDAD  123**

El valor esperado y la variancia de al variable geométrica, están dados por

$$EX = \frac{q}{p} \qquad (4\text{-}121)$$

$$VX = \frac{q}{p^2} = \frac{EX}{p}. \qquad (4\text{-}122)$$

Esta última expresión implica que la variancia difiere de la media en un factor de $1/p$. De la ecuación (4-118) resulta claro cómo la distribución geométrica siempre tendrá el perfil de una J con modo en el punto $x = 0$ [23].

La distribución geométrica tiene sólo un parámetro $p$, el cual se puede expresar como una función de la media $EX$

$$p = \frac{1}{1 + EX}. \qquad (4\text{-}123)$$

Para generar en una computadora valores de variable aleatoria con distribución geométrica se emplea la técnica de la transformación inversa y la fórmula que aparece en la ecuación (4-120) [11]. Al observar que el rango de la expresión $[1 - F(x)/q]$ es unitario, resulta que

$$r = q^x, \qquad (4\text{-}124)$$

y consecuentemente

$$x = \frac{\log r}{\log q}, \qquad (4\text{-}125)$$

donde al valor $x$ siempre se le redondea al entero que sea menor. Esto se puede lograr de manera muy simple con sólo retener los números hasta antes del punto decimal, o bien convirtiendo los números en modo de punto flotante al de punto fijo [15]. Para generar un valor de variable aleatoria con distribución geométrica haciendo uso de esta técnica, se requiere únicamente el empleo de un número aleatorio uniforme, tal como lo muestra la ecuación (4-125).

En las figuras 4-17 y 4-18 de la siguiente sección, se describe un diagrama de flujo y una subrutina en FORTRAN que sirven para el proceso de generación de valores de variable aleatoria con distribución geométrica cuando se tiene una probabilidad fija dada, para fracasos $q$ y para los éxitos $k$ igual a uno.

Se tiene un método alternativo que utiliza la técnica de rechazo para generar valores con distribución geométrica, capaces de reproducir los ensayos de Bernoulli en una computadora. Por lo común, se prefiere este último método, en relación al que se menciona en primer término, cuando

---

--- pág. 124 ---

**124  GENERACIÓN DE VALORES DE LAS VARIABLES**

se requiere una mejor precisión para grandes valores de $p$. En primer lugar, definimos una variable $x$ que se usará como contador, por lo que se la iguala a un valor nulo. A continuación generamos una sucesión de valores de variable aleatoria uniformes $r_1, r_2, \ldots, r_i, \ldots$, la cual termina cuando alcanzamos un valor de $r_i$ que resulta ser menor o igual que $p$. Para cada valor de $r_i$ en la sucesión, que sea mayor que $p$, incrementamos el valor de $x$ en uno. En otras palabras, contaremos el número de fallas o sea el número de veces que $r_i$ tiene un valor mayor que $p$. Cuando logramos el primer valor de $r_i$ menor que $p$ se termina la sucesión y el valor de $x$ corresponde al valor de la variable aleatoria con distribución geométrica. Después de reinstaurar el valor de $x$ a cero se genera una segunda sucesión que conduce a un segundo valor de $x$.

En la presentación anterior se definió a $x$ como el número de fallas que ocurren antes del primer éxito; sin embargo, se puede volver a definir a $x$ en forma tal que incluya, tanto el número de fracasos como al primer éxito. Pese a que el proceso para generar valores de variable aleatoria con distribución geométrica, es similar al procedimiento previamente explicado, las ecuaciones (4-118) y (4-121) se reformulan de la siguiente manera:

$$f(x) = pq^{x-1} \qquad x = 1, 2, \ldots \qquad (4\text{-}126)$$

$$EX = \frac{1}{p}. \qquad (4\text{-}127)$$

### La distribución binomial negativa

Cuando los procesos de ensayos de Bernoulli, tal como se han descrito en la sección anterior, se repiten hasta lograr que ocurran $k$ éxitos $(k > 1)$, la variable aleatoria que caracteriza al número de fallas tendrá una distribución binomial negativa. Por consiguiente, los valores de variables aleatorias con distribución binomial negativa coinciden esencialmente con la suma de $k$ valores de variable aleatoria con distribución geométrica; en este caso, $k$ es un número entero y la distribución recibe el nombre de distribución de Pascal. En consecuencia, la distribución geométrica constituye un caso particular de la distribución de Pascal, especificada para $k$ igual a uno.

La función de distribución de probabilidad para una distribución binomial negativa está dada por

$$f(x) = \binom{k+x-1}{x} p^k q^x \qquad x = 0, 1, 2, \ldots, \qquad (4\text{-}128)$$

donde $k$ es el número total de éxitos en una sucesión de $k + x$ ensayos, con $x$ el número de fallas que ocurren antes de obtener $k$ éxitos. El valor

---

--- pág. 125 ---

**DISTRIBUCIONES DISCRETAS DE PROBABILIDAD  125**

esperado y la variancia de $X$ se representa con:

$$EX = \frac{kq}{p} \qquad (4\text{-}129)$$

$$VX = \frac{kq}{p^2}. \qquad (4\text{-}130)$$

Se debe hacer notar que tanto la distribución geométrica como la binomial negativa se caracterizan por una sobredispersión, esto es, $VX > EX$.

Para una media y una variancia dadas, se pueden determinar los parámetros $p$ y $k$ de la siguiente manera

$$p = \frac{EX}{VX} \qquad (4\text{-}131)$$

$$k = \frac{(EX)^2}{VX - EX}. \qquad (4\text{-}132)$$

Sin embargo, puede suceder que el proceso de simulación se complique considerablemente cuando resulte que en la ecuación (4-132) el valor que se obtenga al efectuar el cómputo de $k$ no sea un entero.

Cuando $k$ es un entero, los valores de la variable aleatoria con distribución de Pascal se pueden generar con sólo considerar la suma de $k$ valores con distribución geométrica. En consecuencia:

$$x = \frac{\left(\sum_{i=1}^{k}\log r_i\right)}{\log q} = \frac{\log\left(\prod_{i=1}^{k} r_i\right)}{\log q} \qquad (4\text{-}133)$$

viene a ser un valor de variable aleatoria con distribución de Pascal, una vez que su magnitud se redondea con respecto al menor entero más próximo al valor calculado.

El contenido de las figuras 4-17 y 4-18 representa, respectivamente, al diagrama de flujo y a la subrutina FORTRAN para generar los valores que siguen la distribución de Pascal, empleando el método ya mencionado. X es una variable FORTRAN de tipo entero que corresponde a $x$. Obsérvese que, en la séptima proposición FORTRAN, automáticamente tiene lugar el proceso de redondeo de acuerdo con la aritmética entera FORTRAN.

Cuando $k$ no resulte ser un entero, deberemos confinarnos a los métodos de aproximación para generar valores de variable aleatoria con distribución binomial negativa. Uno de tales métodos implica la generación de una mezcla de valores de variable aleatoria con dos valores enteros, diferentes para $k$. Por ejemplo, si $k$ es igual a 3.60 podríamos generar una

---

--- pág. 126 ---

**126  GENERACIÓN DE VALORES DE LAS VARIABLES**

mezcla de valores de variable aleatoria con distribución de Pascal: $k$ igual a 3 en un caso y con $k$ igual a 4 en otro; aunque tomando siempre en cuenta que el valor esperado de $k$ es igual a 3.60. Otra alternativa es la que considera la generación de valores de variable aleatoria con distribución de Poisson, cuyo único parámetro se ajuste a una distribución gamma de parámetros $k$ y $\alpha$ [10]. Los valores binomiales negativos que se generan en este último criterio tendrán los parámetros $k$ y $p$, en donde

$$p = \frac{\alpha}{1+\alpha}. \qquad (4\text{-}134)$$

Los valores de variable aleatoria con distribución de Pascal también se pueden definir como el número total de ensayos, de tal suerte que ocurren $x$ fallas antes de que ocurran $k$ éxitos. En este caso, el valor de la variable aleatoria ajustado a la distribución de Pascal estará dado por $k + x$ [6]. De acuerdo con esta proposición, la media de estos valores está definida por

$$E(k+x) = \frac{kq}{p} + k = \frac{k}{p}. \qquad (4\text{-}135)$$

### La distribución binomial

Las variables aleatorias definidas por el número de eventos exitosos en una sucesión de $n$ ensayos independientes de Bernoulli, para los cuales la probabilidad de éxito es $p$ en cada ensayo, siguen una distribución binomial. Este modelo estocástico también se puede aplicar al proceso de muestreo aleatorio con reemplazo, cuando los elementos muestreados tienen sólo dos tipos de atributos (por ejemplo *si* y *no*, o respuestas como *defectuoso* o *aceptable*). El diseño de una muestra aleatoria de $n$ elementos es análoga a $n$ ensayos independientes de Bernoulli, en los que $x$ es un valor binomial que está

> [FIGURA pág. 126 — Figura 4-17]: Diagrama de flujo, empleado para generar valores de variable aleatoria con una distribución de Pascal. Se dibuja en la columna izquierda de la página, de arriba hacia abajo, con la secuencia de bloques: óvalo "PROGRAMA PRINCIPAL" → rectángulo "CALL PASCAL (K, Q, X)" → rectángulo "SUBROUTINE PASCAL (K, Q, X)" → rectángulo "INICIALIZAR TR, QR" → hexágono de ciclo "DO I = 1, K" → rectángulo "GENERAR R" → rectángulo "TR = TR * R" (desde aquí sale una línea punteada que retorna al hexágono del DO, cerrando el ciclo) → rectángulo "NX = LOG (TR)/QR" → rectángulo "X = NX" → rectángulo "RETURN" → óvalo "PROGR. PRINC.". Ilustra el algoritmo de la ecuación (4-133): acumular el producto de $k$ números aleatorios y tomar $\log(\prod r_i)/\log q$.

---

--- pág. 127 ---

**DISTRIBUCIONES DISCRETAS DE PROBABILIDAD  127**

denotando al número de elementos de una muestra de tamaño $n$ con atributos idénticos. Es ésta la analogía que sitúa la distribución binomial como uno de los modelos más importantes en las áreas del muestreo estadístico y del control de calidad.

```
1. SUBROUTINE PASCAL (K, Q, X)
2. TR = 1.0
3. QR = LOG (Q)
4. DO 6 I = 1, K
5. R = RND(R)
6. TR = TR * R
7. NX = LOG (TR)/QR
8. X = NX
9. RETURN
```

**Figura 4-18.** Subrutina FORTRAN para la generación de valores de variable aleatoria con distribución de Pascal.

La distribución binomial proporciona la probabilidad de que un evento o acontecimiento tenga lugar $x$ veces en un conjunto de $n$ ensayos, donde la probabilidad de éxito está dada por $p$. La función de probabilidad para la distribución binomial se puede expresar de la manera siguiente:

$$f(x) = \binom{n}{x} p^x q^{n-x} \qquad (4\text{-}136)$$

donde $x$ se toma como un entero definido en el intervalo finito $0, 1, 2, \ldots n$, y al que se le asocia el valor $q = (1-p)$.

El valor esperado y la variancia de la variable binomial $X$ son

$$EX = np \qquad (4\text{-}137)$$

$$VX = npq \qquad (4\text{-}138)$$

La segunda expresión implica que la variancia de las variables binomiales siempre tiene un valor menor al de la media. Aún más, nótese cómo se define en la ecuación (4-136) la distribución de $(n-x)$ con un valor esperado correspondiente a $nq$.

Cuando se conocen la media y la variancia, resulta inmediata la determinación de $p$ y de $n$, las cuales pueden calcularse como sigue:

$$p = \frac{(EX - VX)}{EX} \qquad (4\text{-}139)$$

$$n = \frac{(EX)^2}{(EX - VX)}. \qquad (4\text{-}140)$$

---

--- pág. 128 ---

**128  GENERACIÓN DE VALORES DE LAS VARIABLES**

> [FIGURA pág. 128 — Figura 4-19]: Diagrama de flujo para la generación de valores de variable aleatoria con distribución binomial. Ocupa la columna izquierda de la página, de arriba hacia abajo: óvalo "PROGRAMA PRINCIPAL" → rectángulo "CALL BINOM (N, P, X)" → rectángulo "SUBROUTINE BINOM (N, P, X)" → rectángulo "X = 0.0" → hexágono de ciclo "DO I = 1, N" → rectángulo "GENERAR R" → rombo de decisión "R − P" con dos salidas: la rama rotulada "+" (a la derecha) baja directamente al bloque "CONTINUE", y la rama rotulada "− 0" (a la izquierda) va al rectángulo "X = X + 1.0" y de ahí a "CONTINUE" → desde "CONTINUE" sale una línea punteada que retorna al hexágono del DO → rectángulo "RETURN" → óvalo "PROGR. PRINC.". Ilustra el método de rechazo basado en ensayos de Bernoulli: se cuenta un éxito cada vez que $r_i \le p$.

La distribución normal proporciona, cuando $n$ es muy grande, una buena aproximación para la distribución binomial. Puesto que con la distribución normal resulta posible manipular valores negativos, a fin de hacer un buen uso de tal distribución la probabilidad de registrar observaciones negativas deberá ser despreciablemente pequeña. En la práctica esto significa que el valor esperado deberá ser por lo menos tres veces mayor que la desviación estándar, o sea

$$np \ge 3(npq)^{1/2} \qquad (4\text{-}141)$$

lo cual implica que $n \ge 9q/p$.

Los valores de variable aleatoria con distribución binomial se pueden generar de muy diversos modos, aunque uno de los métodos más simples, que en el caso de que el valor de $n$ sea moderado resulta uno de los métodos más eficientes, es el basado en la reproducción de ensayos de Bernoulli, siguiendo el método de rechazos. Este método empieza con valores conocidos de $p$ y de $n$ y consiste en generar $n$ números aleatorios después de fijar $x_0$ igual a cero. Para cada número aleatorio $r_i$ $(1 \le i \le n)$ se efectúa una prueba y la variable $x_i$ se incrementa de acuerdo con el siguiente criterio:

$$x_i = x_{i-1} + 1 \qquad \text{si } r_i \le p \qquad (4\text{-}142)$$

$$x_i = x_{i-1} \qquad \text{si } r_i > p. \qquad (4\text{-}143)$$

Después de haberse generado $n$ números aleatorios, el valor de $x_n$ será igual al valor de la variable aleatoria con distribución binomial $x$. Este procedimiento se puede repetir tantas veces como valores binomiales se requieran.

Un segundo método para generar valores binomiales es el que se basa en las sumas aleatorias de valores de variables aleatorias con distribución

---

--- pág. 129 ---

**DISTRIBUCIONES DISCRETAS DE PROBABILIDAD  129**

```
1. SUBROUTINE BINOM (N, P, X)
2. X = 0.0
3. DO 7 I = 1, N
4. R = RND (R)
5. IF (R − P) 6, 6, 7
6. X = X + 1.0
7. CONTINUE
8. RETURN
```

**Figura 4-20.** Subrutina FORTRAN para generar valores de variable aleatoria con distribución binomial.

geométrica, con lo cual se obtiene el número de éxitos en $n$ ensayos. En el caso de que $p$ sea pequeño, este método puede ser mucho más rápido.

Las figuras 4-19 y 4-20 muestran, respectivamente, el diagrama de flujo y la subrutina FORTRAN para generar los valores binomiales, siguiendo el primero de los dos métodos presentados.

### La distribución hipergeométrica

Considérese una población que consta de $N$ elementos tales que cada uno de ellos pertenece a la clase I o a la II. Denotemos por $Np$ al número de elementos que pertenecen a la clase I y por $Nq$ al número de elementos que son miembros de la clase II, donde $p + q = 1$. Si en una población de $N$ elementos se toma una muestra aleatoria que conste de $n$ elementos $(n < N)$ *sin que tenga lugar algún reemplazo*, entonces el número de elementos $x$ de la clase I en la muestra de $n$ elementos, tendrá una distribución de probabilidad hipergeométrica [31, p. 133]. En las áreas de control de calidad y en la de control de producción, con mayor frecuencia se encuentran las aplicaciones de la distribución hipergeométrica. Por ejemplo, si el intervalo entre la llegada de órdenes sucesivas de los clientes relativas a cierto producto de la compañía, se distribuye geométricamente, entonces la demanda total en cualquier período dado de tiempo tendrá una distribución hipergeométrica [5, p. 166].

La distribución hipergeométrica está descrita por la siguiente función de probabilidad:

$$f(x) = \frac{\binom{Np}{x}\binom{Nq}{n-x}}{\binom{N}{n}} \qquad \begin{aligned} 0 &\le x \le Np \\ 0 &\le n-x \le Nq, \end{aligned} \qquad (4\text{-}144)$$

---

--- pág. 130 ---

**130  GENERACIÓN DE VALORES DE LAS VARIABLES**

> [FIGURA pág. 130 — Figura 4-21]: Diagrama de flujo para la generación de valores de variable aleatoria con distribución hipergeométrica. Ocupa toda la página, centrado, de arriba hacia abajo: óvalo "PROGRAMA PRINCIPAL" → rectángulo "CALL HYPGEO (TN, NS, P, X)" → rectángulo "SUBROUTINE HYPGEO (TN, NS, P, X)" → rectángulo "X = 0.0" → hexágono de ciclo "DO I = 1, NS" → rectángulo "GENERAR R" → rombo de decisión "R − P" con dos salidas: la rama rotulada "− 0" sale por la derecha hacia el rectángulo "S = 1.0" y de ahí al rectángulo "X = X + 1.0"; la rama rotulada "+" sale hacia abajo al rectángulo "S = 0.0". Ambas ramas confluyen en el rectángulo "P = (TN*P − S)/(TN − 1.0)" → rectángulo "TN = TN − 1.0" (desde aquí sale una línea punteada que retorna al hexágono del DO, cerrando el ciclo) → rectángulo "RETURN" → óvalo "PROGR. PRINC.". Ilustra el muestreo sin reemplazo: tras cada extracción se actualizan $p$ y $N$ según las ecuaciones (4-147) y (4-148).

---

--- pág. 131 ---

**DISTRIBUCIONES DISCRETAS DE PROBABILIDAD  131**

donde $x$, $n$ y $N$ son enteros. El valor esperado y la variancia se caracterizan como sigue:

$$EX = np \qquad (4\text{-}145)$$

$$VX = npq\left(\frac{N-n}{N-1}\right). \qquad (4\text{-}146)$$

La generación de valores hipergeométricos involucra, substancialmente, la simulación de experimentos de muestreo *sin reemplazo*. En otras palabras, bastará sencillamente con que alteremos el método de ensayos de

```
1. SUBROUTINE HYPGEO (TN, NS, P, X)
2. X = 0.0
3. DO 11 I = 1, NS
4. R = RND (R)
5. IF (R − P) 6, 6, 9
6. S = 1.0
7. X = X + 1.0
8. GO TO 10
9. S = 0.0
10. P = (TN * P − S) / (TN − 1.0)
11. TN = TN − 1.0
12. RETURN
```

**Figura 4-22.** Subrutina FORTRAN para la generación de valores de variable aleatoria con distribución hipergeométrica.

Bernoulli para generar valores binomiales, con objeto que $N$ y $p$ varíen en forma dependiente respecto al número total de elementos que previamente se han obtenido entre la población y el número de elementos de la clase I que se han extraído. A medida que se extrae un elemento de una muestra de $n$ elementos, se reduce el valor de $N = N_0$ de acuerdo con la fórmula:

$$N_i = N_{i-1} - 1 \qquad i = 1, 2, \ldots, n. \qquad (4\text{-}147)$$

De manera similar, el valor de $p = p_0$ se transforma según

$$p_i = \frac{N_{i-1}p_{i-1} - S}{N_{i-1} - 1} \qquad i = 1, 2, \ldots, n, \qquad (4\text{-}148)$$

a medida que se saca el $i$-ésimo elemento de la muestra de $n$ elementos, donde $S = 1$ cuando el elemento de muestra $(i-1)$ pertenece a la clase I y $S = 0$ cuando el elemento de muestra $(i-1)$ pertenece a la clase II. Ciertamente, los valores iniciales de $N_0$ y $P_0$ corresponden: a $N$ el tamaño

---

--- pág. 132 ---

**132  GENERACIÓN DE VALORES DE LAS VARIABLES**

inicial de la población y a $p$ la proporción de la población total que consta de elementos de la clase I.

El diagrama de flujo y la subrutina FORTRAN para generar los valores hipergeométricos se describen en las figuras 4-21 y 4-22, respectivamente. Los símbolos $TN$ y $NS$ se han empleado en este caso para denotar, respectivamente, a $N$ y $n$.

### La distribución de Poisson

Si tomamos una serie de $n$ ensayos independientes de Bernoulli, en cada uno de los cuales se tenga una probabilidad $p$ muy pequeña relativa a la ocurrencia de un cierto evento, cuando $n$ tiende al infinito, la probabilidad de $x$ ocurrencias está dada por la distribución de Poisson

$$f(x) = e^{-\lambda}\frac{\lambda^x}{x!} \qquad x = 0, 1, 2, \ldots \qquad (4\text{-}149)$$
$$\lambda > 0,$$

siempre y cuando permitamos que $p$ se aproxime a cero de manera que se satisfaga la relación $\lambda = np$ consistentemente. De nuestra discusión previa sabemos que $np$ es el valor esperado de la distribución binomial y se puede demostrar que $\lambda$ es el valor esperado para la distribución de Poisson. De hecho, tanto el valor esperado como la variancia de la distribución de Poisson coinciden en el valor $\lambda$. También se puede demostrar que si $x$ es una variable de Poisson con parámetro $\lambda$, entonces para valores muy grandes de $\lambda$ $(\lambda > 10)$, se puede utilizar la distribución normal con $EX = \lambda$ y $VX = \lambda$ para aproximar la distribución de $x$.

Los eventos que se distribuyen en forma poissoniana ocurren frecuentemente en la naturaleza; por ejemplo, el número de aeroplanos que descienden en un aeropuerto en un período de veinticuatro horas puede ser considerablemente grande. Aun así, resulta muy pequeña la probabilidad de que un avión aterrice durante un segundo determinado. Por lo tanto, podemos esperar que en un período determinado, la probabilidad de que desciendan $0, 1, 2, \ldots$ aviones, obedecerá a las leyes de la distribución de Poisson. Esta distribución es particularmente útil cuando tratamos con problemas en los que se da la ocurrencia de eventos aislados sobre un intervalo continuo de tiempo, o bien cuando resulta posible prescribir el número de veces que ocurre un evento aunque no el número de veces que no ocurre.

Para simular una distribución de Poisson con parámetro $\lambda$, nos podemos servir ventajosamente de la relación conocida entre las distribuciones exponenciales y de Poisson. Se puede justificar que si 1) el número total de eventos que ocurren durante un intervalo de tiempo dado es inde-

---

--- pág. 133 ---

**DISTRIBUCIONES DISCRETAS DE PROBABILIDAD  133**

pendiente del número de eventos que ya han ocurrido previamente al inicio del intervalo y 2) la probabilidad de que un evento ocurra en el intervalo de $t$ a $t + \Delta t$ es aproximadamente $\lambda\Delta t$ para todos los valores de $t$, *entonces*: a), la función de densidad del intervalo $t$ entre las ocurrencias de eventos consecutivos es $f(t) = \lambda e^{-\lambda t}$, y b), la probabilidad de que ocurran $x$ eventos durante el tiempo $t$ es

$$f(x) = e^{-\lambda t}\frac{(\lambda t)^x}{x!} \qquad (4\text{-}150)$$

para toda $x$ y toda $t$.

Considérese un horizonte de tiempos que se inicia en el origen 0 como punto de referencia y que se ha dividido en intervalos unitarios, como se ilustra en la figura 4-23. Supóngase también que los eventos ocurren a lo largo del mencionado horizonte y que se denotan por el símbolo $(\wedge)$. Se supondrá que el intervalo entre eventos obedece a una distribución exponencial

> [FIGURA pág. 133 — Figura 4-23]: "Eventos distribuidos en forma poissoniana, sobre una escala de tiempo." Es un eje horizontal de tiempo con el origen 0 a la izquierda y una flecha a la derecha. Sobre el eje, corchetes/llaves superiores delimitan intervalos unitarios rotulados "t = 1" (se marcan tres de estos intervalos unitarios a lo largo del horizonte). Los eventos se marcan sobre el eje con el símbolo (∧) y los tramos entre eventos consecutivos se rotulan $t_1, t_2, t_3, t_4, t_5, t_6, t_7, t_8$ de izquierda a derecha. Debajo del eje, para cada intervalo unitario se anota el conteo de eventos ocurridos en él: x = 1, x = 2, x = 3, x = 4, x = 3, x = 2, x = 1, x = 1. La figura ilustra que si los intervalos entre eventos son exponenciales con media $1/\lambda$, el número $x$ de eventos por unidad de tiempo sigue una distribución de Poisson de media $\lambda$.

cuyo valor esperado es igual a $1/\lambda$. Con estos antecedentes se implica que el número de eventos $x$ que ocurren durante un tiempo unitario seguirán una distribución de Poisson cuyo valor esperado estará dada por $\lambda$. Un método para generar valores de variable aleatoria con distribución de Poisson deberá considerar la generación de intervalos $t_2, t_3, t_3, \ldots$, distribuidos en forma exponencial con un valor esperado igual a 1. Una vez generados estos intervalos aleatorios, se acumulan hasta que su suma exceda el valor de $\lambda$.

En términos matemáticos el valor poissoniano $x$ se determina haciendo uso de las siguiente desigualdad:

$$\sum_{i=0}^{x} t_i \le \lambda < \sum_{i=0}^{x+1} t_i \qquad (x = 0, 1, 2, \ldots), \qquad (4\text{-}151)$$

donde los valores de la variable aleatoria $t_i$ se generan por medio de la fórmula

$$t_i = -\log r_i \qquad (4\text{-}152)$$

con una media unitaria. Un método más rápido para generar los valores

---

--- pág. 134 ---

**134  GENERACIÓN DE VALORES DE LAS VARIABLES**

> [FIGURA pág. 134 — Figura 4-24]: Diagrama de flujo para la generación de valores de variable aleatoria con distribución de Poisson. Ocupa la columna izquierda, de arriba hacia abajo: óvalo "PROGRAMA PRINCIPAL" → rectángulo "CALL POISSN (P, X)" → rectángulo "SUBROUTINE POISSN (P, X)" → rectángulo "INICIALIZAR X, TR" → rectángulo "B = EXP (−P)" → rectángulo "GENERAR R" → rectángulo "TR = TR*R" → rombo de decisión "TR − B" con dos salidas: la rama rotulada "0, +" sale por la derecha hacia el rectángulo "X = X + 1.0", que retorna con una línea al bloque "GENERAR R" (cerrando el ciclo); la rama rotulada "−" continúa hacia abajo → rectángulo "RETURN" → óvalo "PROGR. PRINC.". Ilustra el algoritmo de la ecuación (4-153): se multiplican números aleatorios uniformes hasta que el producto acumulado cae por debajo de $e^{-\lambda}$.

poissonianos $x$ [28, p. 37] es el que consiste en reformular la ecuación (4-151) de la manera siguiente:

$$\prod_{i=0}^{x} r_i \ge e^{-\lambda} > \prod_{i=0}^{x+1} r_i. \qquad (4\text{-}153)$$

La subrutina FORTRAN correspondiente a la ecuación (4-153) aparece en las figuras 4-24 y 4-25, donde P representa la constante FORTRAN que corresponde al parámetro $\lambda$.

---

--- pág. 135 ---

**DISTRIBUCIONES DISCRETAS DE PROBABILIDAD  135**

```
1. SUBROUTINE POISSN (P, X)
2. X = 0.0
3. B = EXP (−P)
4. TR = 1.0
5. R = RND (R)
6. TR = TR * R
7. IF (TR − B) 10, 8, 8
8. X = X + 1.0
9. GO TO 5
10. RETURN
```

**Figura 4-25.** Subrutina FORTRAN para generar valores de variable aleatoria que obedecen la distribución de Poisson.

### Distribuciones discretas empíricas

En este capítulo nos hemos concentrado en los métodos para generar ciertas distribuciones particulares de probabilidad, como la normal, la binomial y la de Poisson, para mencionar sólo algunas. Ahora trataremos un método un tanto más general que puede emplearse para simular cualquiera de las siguientes distribuciones: 1) empírica, 2) discreta y 3) continua que pueda ser aproximada mediante una distribución discreta. Sin embargo, en general nos abstendremos de utilizar este método para generar valores de variable aleatoria a partir de distribuciones de probabilidad estándares, debido a que cualquiera de los métodos descritos previamente se espera que proporcione resultados más satisfactorios, desde el punto de vista de la velocidad de computación, facilidad de programación y requisitos de almacén o memoria. En otros términos, el método que se propondrá en esta sección es uno que se utiliza siempre y cuando no se disponga de otra alternativa.

Sea $X$ una variable aleatoria discreta con $P(X = b_i) = p_i$, tal como se presenta la variable aleatoria de la siguiente tabla:

| $b_i$ | $P(x = b_i) = p_i$ |
|---|---|
| $b_1$ | 0.273 |
| $b_2$ | 0.037 |
| $b_3$ | 0.195 |
| $b_4$ | 0.009 |
| $b_5$ | 0.124 |
| $b_6$ | 0.058 |
| $b_7$ | 0.062 |
| $b_8$ | 0.151 |
| $b_9$ | 0.047 |
| $b_{10}$ | 0.044 |

---

--- pág. 136 ---

**136  GENERACIÓN DE VALORES DE LAS VARIABLES**

En consecuencia, resulta evidente que un método para generar $x$ en una computadora es aquél que genera un valor de variable aleatoria $r$ sujeto a una distribución uniforme, en el intervalo (0, 1) y un conjunto de valores $x = b_i$ siempre que se satisfaga

$$p_1 + \cdots + p_{i-1} < r \le p_1 + \cdots p_i. \qquad (4\text{-}154)$$

Pese a que se han desarrollado un buen número de técnicas de búsqueda basadas en este método, en su gran mayoría requieren programas relativamente complejos que a su vez exigen un tiempo de computación excesivo.

Uno de los procedimientos más rápidos para generar valores de variable aleatoria discretos es el desarrollado por G. Marsaglia [17], quien presupone la disponibilidad de una computadora decimal cuyos bloques o palabras de memoria pueden referirse mediante números. Esta última característica, en realidad, constituye una propiedad de la gran mayoría de las computadoras actuales. En el procedimiento de Marsaglia se mencionan los números 273 $b_1$, 37 $b_2$, 195 $b_3$, ..., 44 $b_{10}$ y los que pertenecen a cada una de estas clases respectivas, en las ubicaciones de memoria desde la 0 a la 999. Entonces, si por ejemplo $r = .d_1d_2d_3d_4$ es un número aleatorio uniforme de cuatro dígitos, generado por la computadora, el número en la localidad $d_1d_2d_3$ será el valor de $x$.

Conviene hacer notar que si bien este método es extremadamente rápido, también requiere por lo menos una memoria de 1000 palabras. Existe otro método desarrollado también por Marsaglia que en forma alternativa utiliza mucho menos capacidad de memoria, aunque incrementa ligeramente el tiempo de computación [17].

### Cadenas discretas de Markov

Una posibilidad, muy frecuente por cierto, de caracterizar los sistemas operacionales radica en la especificación del sistema en términos de una sucesión de estados distinguibles: por ejemplo, el estado en que se encuentra cierto instrumental de producción, la cola o las facilidades de almacenamiento, pueden describirse adecuadamente mediante el número de objetos estacionados en cualquier tiempo dado. En caso de que el tiempo pueda medirse mediante unidades discretas, podremos describir los cambios que ocurren en los estados del sistema, de la siguiente manera. En cualquier momento en que el sistema se encuentre en el estado $i$ al inicio de un período, se puede definir la probabilidad de que el sistema evolucione al estado $j$ cuando se inicie el principio del siguiente período. Esta probabilidad $p_{ij}$ dependerá tan sólo de los estados $i$, $j$ y para cada $i$ se tendrá que $\sum_j p_{ij} = 1$.

Las $p_{ij}$ pueden disponerse en un arreglo matricial que recibe el nombre de matriz de probabilidad de transición $P = \|p_{ij}\|$, la cual determina completamente al comportamiento del sistema. Esta clase de comportamientos

---

--- pág. 137 ---

**DISTRIBUCIONES DISCRETAS DE PROBABILIDAD  137**

recibe el nombre de proceso de Markov y la sucesión de transiciones que sirve de muestra se la conoce por el nombre de cadena de Markov.

Cabe mencionar que aunque existen métodos analíticos para evaluar la distribución de probabilidad de los procesos de Markov bajo ciertas condiciones, también se puede recurrir a la determinación bajo estimaciones de muestreo basadas en la simulación de las cadenas de Markov. Esta técnica permite hacer las estimaciones de las distribuciones de frecuencia de los vectores de probabilidad, tanto de estados transitorios como estacionarios. Una alternativa más es la de considerar la posibilidad que existe para analizar las probabilidades de transición no constante, haciendo uso de la simulación.

Uno de los métodos conocidos [11, p. 237] para generar cadenas de Markov utiliza los renglones de la matriz de transición $\|p_{ij}\|$ de modo muy similar al descrito en la sección previa. Si el último estado del sistema fue $i$, entonces el próximo estado será $j$, si

$$\sum_{k=1}^{j-1} p_{ik} < r \le \sum_{k=1}^{j} p_{ik}, \qquad (4\text{-}155)$$

donde $r$ es un número aleatorio uniforme en el intervalo (0, 1). Cada número que se genere originará una transición del estado $i$ al estado $j$ y el programa podrá incluir la facilidad de un contador de la frecuencia en que el sistema se localiza en cada uno de los estados finitos.

En las figuras 4-26 y 4-27 se describe un programa FORTRAN que sirve para generar la distribución de frecuencias de los estados por medio de la simulación de una cadena de Markov. Este programa está dimensionado hasta una matriz de transición de $10\times10$. En este caso $M$ indica la dimensión real de la matriz y $N$ representa la longitud deseada (el número de transiciones) de la cadena, e $I$ denota al estado inicial seleccionado. Las declaraciones FORMAT que sirven de formato para la lectura

> [FIGURA pág. 137 — Figura 4-26]: "Diagrama de flujo para la simulación de cadenas de Markov." Ocupa la columna derecha de la página, de arriba hacia abajo: rectángulo "DIMENSION P (10, 10), X (10)" → rectángulo "LEER M, N, I, P" → rectángulo "X (K) = 0.0; K = 1, M" → hexágono de ciclo "DO L = 1, N" → rectángulo "GENERAR R" → hexágono de ciclo interno "DO J = 1, M" → rombo de decisión "P (I, J) − R" con la rama rotulada "0, +" saliendo hacia abajo (y la otra rama retornando al ciclo interno mediante línea punteada) → rectángulo "I = J" → rectángulo "X (I) = X (I) + 1.0" (desde aquí una línea punteada retorna al hexágono del ciclo externo DO L) → rectángulo "IMPRIMIR X". Ilustra el algoritmo de la ecuación (4-155): buscar el primer $j$ cuya probabilidad acumulada del renglón $i$ supere a $r$, transicionar a ese estado y contarlo en el vector de frecuencias X.

---

--- pág. 138 ---

**138  GENERACIÓN DE VALORES DE LAS VARIABLES**

de datos, se simbolizan sin otra especificación ulterior, tan sólo por paréntesis. La matriz $P$ en el programa *no* es la matriz de probabilidad de transición sino que es una derivada de la matriz de transiciones, de modo tal que sólo contiene las probabilidades acumuladas de cada renglón. El vector $X$ deberá contener, al final de una sucesión de $N$ transiciones, la distribución de frecuencias de los estados. El programa puede genera-

```
 1. DIMENSION P(10, 10), X(10)
 2. READ ( ), M, N, I
 3. READ ( ), P
 4. DO 5 K = 1, M
 5. X(K) = 0.0
 6. DO 12 L = 1, N
 7. R = RND (R)
 8. DO 10 J = 1, M
 9. IF (P(I,J) − R) 10, 11, 11
10. CONTINUE
11. I = J
12. X(I) = X(I) + 1.0
13. PRINT ( ), X
14. END
```

**Figura 4-27.** Programa FORTRAN para la simulación de cadenas de Markov.

lizarse con sólo añadir subrutinas que alimenten información reacondicionada de entrada o que efectúe determinadas computaciones sobre el vector de frecuencias $X$.

## SERIES DE TIEMPO AUTOCORRELACIONADAS

Si en un proceso estocástico se producen variables aleatorias tales que se tenga una variable aleatoria $x_t$ para cada valor de $t$, donde $t$ representa al tiempo, entonces nos encontramos frente a una función aleatoria del tiempo llamada serie de tiempo. Cuando estas series de tiempo se relacionan específicamente con fenómenos económicos o tecnológicos, aparece una propiedad muy común en estas series, la cual establece que la covariancia de $x_{t+k}$ y $x_t$, donde $k$ es el *rezago* (i.e. el número de intervalos de tiempo entre los valores respectivos de las series de tiempo), resulta con un valor no negativo. Para el rezago $K$, definimos la función de covariancia $\phi(k)$ como sigue:

$$\phi(k) = E(x_t, x_{t+k}) \qquad (4\text{-}156)$$

y la función de autocorrelación $\rho(k)$ como

$$\rho(k) = \frac{\phi(k)}{\phi(0)}. \qquad (4\text{-}157)$$

---

--- pág. 139 ---

**SERIES DE TIEMPO AUTOCORRELACIONADAS  139**

En ambas expresiones estamos suponiendo que $E(x_t) = E(x_{t+k}) = 0$ y que tanto $\phi(k)$ como $\rho(k)$ son funciones de $k$ únicamente. Cuando es tal el caso, estas condiciones resultan válidas únicamente para series estacionarias de tiempo [31, p. 516].

No es posible, por lo común, generar series de tiempo con una función de autocorrelación arbitraria; sin embargo, se tienen dos funciones especiales que pueden usarse con una flexibilidad satisfactoria, si es que la distribución de las variables $x_t$ es normal, de media nula y con una variancia de constante idéntica [5, p. 169].

### Función lineal de autocorrelación

Sean

$$\rho(k) = 1 - \frac{k}{m} \qquad k \le m \qquad (4\text{-}158)$$

$$\rho(k) = 0 \qquad k > m$$

Estas expresiones representan una función linealmente decreciente en $k$ a la vez que un modelo para las series de tiempo autocorrelacionadas, en las que puede suponerse una autocorrelación cero para rezagos mayores que $m$. La técnica para generar una serie de tiempo con esta función de autocorrelación se basa en el proceso para generar valores de variable aleatoria que obedecen a una distribución normal, como lo describe la ecuación (4-75) y suponiendo además, que los números aleatorios uniformes se transforman en valores cuya esperanza es nula, es decir, $E(r) = 0$. Entonces, si

$$x_t = \sum_{j=1}^{N} r_j, \qquad (4\text{-}159)$$

$x_t$ tendrá media cero y variancia $N\sigma^2$ con $\sigma^2 = \operatorname{Var}(r)$. El siguiente valor se genera con

$$x_{t+1} = \sum_{j=p+1}^{N+p} r_j, \qquad (4\text{-}160)$$

en donde $(N - p)$ de los $r_j$ números aleatorios corresponden a términos comunes que aparecen en las sumas sucesivas.

La función de autocorrelación con rezago $k$ se deriva de la siguiente relación de identidad:

$$(x_t - x_{t+k})^2 = x_t{}^2 - 2x_t x_{t+k} + x^2_{t+k}. \qquad (4\text{-}161)$$

Regresando a los valores esperados y con ayuda de las ecuaciones (4-165) y (4-159) podemos escribir

$$E(x_t - x_{t+k})^2 = 2N\sigma^2 - 2\phi(k). \qquad (4\text{-}162)$$

---

--- pág. 140 ---

**140  GENERACIÓN DE VALORES DE LAS VARIABLES**

El paréntesis izquierdo contiene tan sólo $2kp$ números $r_j$ no nulos e independientes, cuya variancia es igual a $2kp\sigma^2$. Consecuentemente, si $k \le N/p$

$$kp\sigma^2 = N\sigma^2 - \phi(k) \qquad (4\text{-}163)$$

y

$$\rho(k) = \frac{\phi(k)}{N\sigma^2} = 1 - \frac{kp}{N}. \qquad (4\text{-}164)$$

Se acostumbra elegir $N$ igual a 12, con lo cual se logra obtener una variancia unitaria para los $x_t$. Sin embargo, en este caso la función de autocorrelación se define sólo para valores de a lo más $k = 12/p$ rezagos. Obsérvese que la fórmula (4-164) corresponde a la ecuación (4-158) con $m = N/p$.

Las subrutinas FORTRAN escritas para generar una serie de tiempo autocorrelacionada de valores $x$ distribuidos normalmente y con una media igual a cero y una variancia unitaria, quedan descritos en las figuras 4-28 y 4-29. El valor de $p$ en la ecuación (4-160) corresponde con la variable K del programa FORTRAN. En esta subrutina se presuponen doce valores iniciales para los valores uniformes $(RX)$ y se produce un valor $X$ de la serie de tiempo después de cada proposición CALL.

### Función exponencial de autocorrelación

El coeficiente de correlación con rezago $k$ se expresa como

$$\rho(k) = \lambda^k; \qquad 0 < \lambda < 1. \qquad (4\text{-}165)$$

Se puede demostrar la existencia de una función de autocorrelación de este tipo, en series de tiempo que se obtienen a partir de la aplicación de un ajuste exponencial suave basado en la siguiente relación recursiva:

$$x_0 = (1-\lambda)r_0$$
$$x_t = \lambda x_{t-1} + (1-\lambda)r_t, \qquad (4\text{-}166)$$

donde los números $r_t$ son variables mutuamente independientes con media nula y variancia $\sigma^2$.

Para propósitos prácticos, los valores $r_t$ se pueden generar de manera tan simple como

> [FIGURA pág. 140 — Figura 4-28]: "Diagrama de flujo para la generación de valores de variable aleatoria normales y autocorrelacionados." Ocupa la columna izquierda, de arriba hacia abajo: óvalo "PROGR. PRINC." → rectángulo "CALL AUTOCR (K, RX, X)" → rectángulo "SUBR. AUTOCR (K, RX, X)" → rectángulo "INICIALIZAR L, X" → rectángulo "DESPLAZAR RX (I), I = 1, L" → rectángulo "GENERAR RX (I), I = L + 1, 12" → rectángulo "CALCULAR X" → rectángulo "RETURN" → óvalo "PROGR. PRINC.". Ilustra el corrimiento de los doce valores uniformes almacenados: los $L = 12 - K$ últimos se reutilizan (términos comunes de la ecuación 4-160) y los $K$ restantes se generan nuevos.

---

--- pág. 141 ---

**REFERENCIAS Y BIBLIOGRAFIA  141**

se generan los números aleatorios uniformes transformados al intervalo $(-1/2, +1/2)$. En este caso, los valores de variable aleatoria $x_t$ autocorrelacionados que han sido generados, tendrán un valor esperado cero y una variancia igual a

$$\sigma^2_{x_t} = \frac{1-\lambda}{1+\lambda}\sigma^2 = \frac{1-\lambda}{12(1+\lambda)}. \qquad (4\text{-}167)$$

En la literatura sobre ajustes exponenciales suaves son bien conocidos los programas de computadora que proporcionan este tipo de autocorrelación

```
 1. SUBROUTINE AUTOCR (K, RX, X)
 2. DIMENSION RX(12)
 3. L = 12 − K
 4. X = 0.0
 5. DO 7 I = 1, L
 6. RX(I) = RX(I + K)
 7. X = X + RX(I)
 8. L = L + 1
 9. DO 11 I = L, 12
10. RX(I) = RND (R)
11. X = X + RX(I)
12. X = X − 6.0
13. RETURN
14. END
```

**Figura 4-29.** Subrutina FORTRAN para generar valores de variable autocorrelacionados.

y generalmente su estructura es muy simple, ya que en la ecuación (4-166) tan sólo se requiere un valor para representar la información pasada [5, p. 172].

## REFERENCIAS Y BIBLIOGRAFIA

1. Aitchison, J. y Brown, J. A. C. *The Lognormal Distribution*, Cambridge: Cambridge University Press, 1957.
2. Anderson, T. W. *An Introduction to Multivariate Statistical Analysis*. Nueva York: John Wiley and Sons, 1958.
3. Box, G. E. P. y Muller, M. E. "A Note on the Generation of Normal Deviates", *Annals of Mathematical Statistics*, XXIX (1958), 610-611.
4. Brockmeyer, E. H., Halstrom, L. y Jensen, A. *The Life and Works of A. K. Erlang*. Copenhague: Copenhagen Telephone Company, 1948.
