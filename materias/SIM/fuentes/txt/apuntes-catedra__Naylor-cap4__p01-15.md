# Tecnicas de Simulación en Computadoras - Naylor Cap. 4.pdf

> Transcripción de las páginas 1 a 15 del PDF. Cada página escaneada contiene dos páginas del libro (par izquierda/derecha). Los marcadores `--- pág. N ---` refieren a la página del PDF; entre paréntesis se indica la numeración original del libro.

---

--- pág. 1 (portada manuscrita + inicio del Capítulo 4, libro p. 87) ---

> [ANOTACIÓN MANUSCRITA pág. 1, mitad izquierda]: Título escrito a mano en mayúsculas: "TÉCNICAS DE SIMULACIÓN EN COMPUTADORAS". Debajo, también manuscrito: "Autor: Naylor, Thomas".

CAPITULO 4

*Generación de valores de*
*las variables estocásticas*
*empleadas en simulación*

INTRODUCCION

Cuando se establecen las bases racionales subyacentes al empleo de los métodos existentes para generar valores de variables estocásticas en una computadora digital, se parte de dos problemas un tanto divergentes. Estos dos problemas de tipo distinto se pueden clasificar convenientemente como determinísticos, es decir, no probabilísticos o bien, como estocásticos. Recientemente se ha popularizado el término Monte Carlo como sinónimo para el concepto *simulación de procesos estocásticos*. Sin embargo, conviene anotar que en el pasado, éste término se aplicó tan sólo al emplear los métodos de simulación estocástica para la resolución de problemas estrictamente determinísticos.

En un principio, los métodos de simulación estocástica fueron aplicados por los matemáticos y los científicos relacionados con las áreas de la Física, para resolver ciertos problemas determinísticos que se podían expresar mediante ecuaciones matemáticas para las cuales sus soluciones no resultaban fáciles de obtener, utilizando los criterios convencionales de los métodos numéricos o analíticos. Cabe considerar el hecho de que para cierto número de problemas matemáticos de importancia reconocida, existe la posibilidad de que, una vez encontrado un proceso estocástico cuya distribución de probabilidad o cuyos parámetros satisfagan las propiedades matemáticas que se requieran, queden resueltas las ecuaciones que caracterizan a estos problemas. Aún más, desde un punto de vista computístico pudiera resultar más eficiente construir tal tipo de procesos a la vez que generar su estadística, empleando la computadora en lugar de seguir los métodos convencionales. Entre los problemas matemáticos determinísticos para los que se ha encontrado que la simulación estocástica resulta útil en la obtención de

---

--- pág. 2 (apéndice y bibliografía del capítulo 3; libro, páginas del APENDICE A) ---

> [NOTA]: el encabezado superior izquierdo está borroneado; se alcanza a leer "…APENDICE A". Esta página pertenece al final del capítulo anterior (capítulo 3) y aparece intercalada en el PDF antes del cuerpo del capítulo 4.

donde $e_i$ es una constante y $\Pi$ denota el producto $p_1^{e_1} \times p_2^{e_2} \times p_3^{e_3} \dots$ La prueba de esto se debe a Euclides [2, p. 21].

*Teorema 5.* Si $(a, m) = 1$, entonces $a^{\varphi(m)} \equiv 1 \pmod m$, de lo cual se sigue que:

(1) El mayor orden posible de $a$ es $h = \varphi(m)$ cuando $a$ es una raíz primitiva de $m$.

(2) Para $n < m$ tales que $(m, n) = 1$, $na^h \equiv n \pmod m$, donde $h = \varphi(m)$. La prueba de esto se atribuye a Euler [21, p. 273] y se obtiene de los teoremas 2 y 3.

*Teorema 6.* Para todas las potencias de un número primo $p > 2$ existen las raíces primitivas, i.e. existe un número tal que $(a, p^e) \equiv 1$ y $a^{\varphi(p^e)} \equiv 1 \pmod{p^e}$ donde $h = \varphi(p^e)$. (Véase [21, p. 285].)

*Teorema 7.* Si $m = \Pi p_i^{e_i}$, entonces $\varphi(m) = \Pi(p_i - 1)p_i^{e_i - 1}$. La demostración se debe a Euler [21, p. 113].

*Teorema 8.* Si $m = p^e$ y $p$ es un primo impar, entonces $h = \lambda(m) = (p - 1)p^{e-1} = \varphi(m)$ para valores de $a$ que son raíces primitivas de $m$. Corolario: Si $p = 2$, i.e., $h = \lambda(m) = 2^{e-2}$ para $e > 2$, entonces $\lambda(m) \neq \varphi(m)$. La prueba se debe a Euler [21, pp. 289-290].

*Teorema 9.* Si $m = \Pi p_i^{e_i}$ para $i = 1, 2, \dots, s$; entonces:

(1) $\lambda(m) = \text{m.c.m}\,[\lambda(p_1^{e_1}), \lambda(p_2^{e_2}), \dots, \lambda(p_s^{e_s})]$.

(2) Existen valores de $a$ cuyo orden es igual a (esto es, pertenecen conjuntamente a) cada $\lambda(p_i^{e_i})$. La demostración está en [21, p. 293] y se sigue del teorema chino del residuo debido a Sun-Tse [21, p. 246].

Colorario: Si $p_1 = 2$, entonces $\lambda(m) = \text{m.c.m}\,[\lambda(2^{e_1}), \varphi(p_2^{e_2}), \varphi(p_3^{e_3}), \dots]$.

*Teorema 10.* El menor entero positivo $a$ tal que $(a^h - 1)/(a - 1) \equiv 0 \pmod m$ es $h = m$, si (1) $a \equiv 1 \pmod p$ si $p$ es un factor primo de $m$ (2) $a \equiv 1 \pmod 4$ si 4 es un factor de $m$. La prueba se debe a Hull y Dobell [16, pp. 233-235].

### REFERENCIAS Y BIBLIOGRAFIA

1. Allard, J. L., Dobell, A. R. y Hull, T. E. "Mixed Congruential Random Number Generators for Decimal Machines", *Journal of the Association for Computing Machinery*, X, No. 2 (1963), 131-141.
2. Birkhoff, G., y MacLane, S. *A Survey of Modern Algebra*. Nueva York: The Macmillan Company, 1953.
3. Coveyou, R. R. "Serial Correlation in the Generation of Pseudo-Random Numbers", *Journal of the Association for Computing Machinery*, VII (1960), 72-74.
4. Duparc, H[…] Lekkerkerker, C. G. y Peremans, W. "Reduced Sequences of Integers an[d …]-Random Numbers", *Mathematische Centrum Report ZW* 1953-002, […] (1953).
5. Fisher, R. […], F. *Statistical Tables for Biological Agricultural and Medical Research*. […]ondres: Oliver and Boyd, 1953.
6. Forsythe, G. E. "Generation and Testing of Random Digits at the National Bureau of Standards, Los Angeles," en *Monte Carlo Method*. National Bureau of Standards Applied Mathematics Series No. 12. Washington, D. C., 1951.
7. Freund, J. E. *Mathematical Statistics*. Englewood Cliffs: Prentice-Hall, 1962.
8. Golenko, D. K., y Smiriagin, V. A. "A Source of Random Numbers Which Are Equidistributed in [0, 1]", *Publications Math. Inst. Hungarian Acad. Sci.* 5, Series A. Fasc. 3, en ruso, con resumen en inglés (1960), 241-253.
9. Good I. J. "The Serial Test for Sampling Numbers and Other Tests of Randomness" *Proc. Camb. Phil. Soc.*, XLIX (1953), 276-284.
10. Good, I. J. "On the Serial Test for Random Sequences", *Annals of Mathematical Statistics* XXVIII (1957), 262-264.
11. Green, B. F., *Digital Computers in Research*. Nueva York: McGraw-Hill Book Co., 1963.
12. Green, B. F., Smith J., y Klem L. "Empirical Tests of an Additive Random Number Generator", *Journal of the Association for Computing Machinery*, VI, No. 4 (1959), 527-537.
13. Greenberger, M. "An a Priori Determination of Serial Correlation in Computer Generated Random Numbers", *Mathematics of Computations*, XV (1961), 383-389.
14. Greenberger, M., "Method in Randomness", *Communications of the ACM*, VIII, No. 3 (1965), 177-179.
15. Hull, T. E., y Dobell, A. R. "Mixed Congruential Random Number Generators for Binary Machines", *Journal of the Association for Computing Machinery*, XI, No. 1 (1964), 31-40.
16. Hull, T. E., y Dobell, A. R. "Random Number Generators", *SIAM Review*, IV, No. 3 (julio, 1962), 230-254.
17. International Business Machines Corporation, "Random Number Generation and Testing", *Reference Manual* (C20-8011), Nueva York, 1959.
18. Lehmer, D. H. "Mathematical Methods in Large-Scale Computing Units", *Annals Computer Laboratory Harvard University*, XXVI (1951), 141-146.
19. MacLaren, M. D., y Marsaglia, G. "Uniform Random Number Generators", *Journal of the Association for Computing Machinery*, XII, No. 1 (1965), 83-89.
20. National Bureau of Standards. *Monte Carlo Method*. Applied Mathematics Series No. 12. Washington, D. C., 1951.
21. Ore, O. *Number Theory and Its History*. Nueva York: McGraw-Hill Book Co., 1948.
22. RAND Corporation. *A Million Random Digits with 100,000 Normal Deviates*. Glencoe, Ill.: The Free Press, 1955.
23. Rotenberg, A. "A New Pseudo-Random Number Generator", *Journal of the Association for Computing Machinery*, VII (1960), 75-77.
24. Stockmal, F. "Calculations with Pseudo-Random Numbers", *Journal of the Association for Computing Machinery*, XI, No. 1 (enero, 1964), 41-52.
25. Taussky, O., y Todd, J. "Generation and Testing of Pseudo-Random Numbers" en *Symposium on Monte Carlo Methods*, ed. Herbert A. Meyer. Nueva York: John Wiley and Sons, Inc., 1956.
26. Tocher, K. D. "The Application of Automatic Computers to Sampling Experiments", *Journal of the Royal Statistical Society*, B16 (1954), 39-61.
27. Uspensky, James V., y Heaslet, M. A. *Elementary Number Theory*. Nueva York: McGraw-Hill Book Co., 1939.
28. Wold, H. "Random Normal Deviates", *Tracts for Computers*, No. XXV. Londres: Cambridge University Press, 1955.

---

--- pág. 3 (libro pp. 88-89) ---

**88  GENERACIÓN DE VALORES DE LAS VARIABLES**

o alguna de sus variantes respectivas, proporcionan la base general para simular la mayoría de las distribuciones consideradas en este capítulo.

### El método de la transformación inversa

Si deseamos generar los valores $x_i$ de las variables aleatorias a partir de cierta estadística de población cuya función de densidad esté dada por $f(x)$, debemos en primer lugar obtener la función de distribución acumulativa $F(x)$. (Véase la figura 4-1.) Puesto que $F(x)$ se define sobre el rango de 0 a 1, podemos generar números aleatorios distribuidos uniformemente y además hacer $F(x) = r$. Resulta claro, entonces, cómo queda $x$ determinada

> [FIGURA 4-1, pág. 3]: Gráfica cartesiana rotulada arriba a la izquierda "$F(x) = r$". Eje vertical con marcas en 1.0 y en un valor intermedio $r_0$; eje horizontal $x$ con la marca $x_0$. La curva es una función de distribución acumulativa con forma de S: arranca en el origen, crece monótonamente y se aplana asintóticamente en 1.0. Líneas punteadas horizontales desde $r_0$ hasta la curva y verticales desde la curva hasta $x_0$, mostrando la correspondencia unívoca $r_0 \leftrightarrow x_0$.

**Figura 4-1. Una función de distribución acumulativa.**

unívocamente por $r = F(x)$. Sigue, por lo tanto, que para cualquier valor particular de $r$, que generemos, por ejemplo $r_0$, siempre es posible encontrar el valor de $x$; en este caso $x_0$, que corresponde a $r_0$ debido a la función inversa de $F$, si es conocida. Esto es,

$$x_0 = F^{-1}(r_0) \tag{4-2}$$

donde $F^{-1}(x)$ es la transformación inversa (o mapeo) de $r$ sobre el intervalo unitario en el dominio de $x$. Si generamos números aleatorios uniformes correspondientes a una $F(x)$ dada, podemos resumir, matemáticamente, este método como sigue:

$$r = F(x) = \int_{-\infty}^{x} f(t)\,dt \tag{4-3}$$

entonces

$$P\{X \le x\} = F(x) = P[r \le F(x)] = P[F^{-1}(r) \le x], \tag{4-4}$$

y consecuentemente $F^{-1}(r)$ es una variable que tiene a $f(x)$ como función de densidad de probabilidad. Este criterio equivale a resolver la ecuación (4-3) en $x$, en términos de $r$; el procedimiento se ilustra con los siguientes ejemplos:

**INTRODUCCIÓN  89**

**Ejemplo 1.** Genérense los valores $x$ de variables aleatorias con una función de densidad $f(x) = 2x$, $0 \le x \le 1$. De la ecuación (4-3) resulta que

$$r = F(x) = \int_{0}^{x} 2t\,dt \qquad 0 \le x \le 1 \tag{4-5}$$

$$= x^2.$$

Tomando ahora la transformación inversa $F^{-1}(r)$, esto es, resolviendo la ecuación (4-5) para $x$, obtendremos

$$x = F^{-1}(r) = \sqrt{r}, \qquad 0 \le r \le 1. \tag{4-6}$$

Por lo tanto, los valores de $x$ con una función de densidad $f(x) = 2x$ se pueden generar al determinar la raíz cuadrada de los números aleatorios $r$.

> [FIGURA 4-2, pág. 3]: Dos gráficas lado a lado para el ejemplo 2.
> Izquierda — función de densidad $f(x)$: eje vertical con marcas 0.25, 0.50, 0.75, 1.0; eje horizontal $x$ con marcas 1 y 2. Es una función escalonada: vale 0.25 (constante) en el intervalo $0 \le x \le 1$ y salta a 0.75 (constante) en el intervalo $1 \le x \le 2$; cero fuera.
> Derecha — función de distribución acumulativa $F(x)$: mismo eje vertical (0.25, 0.50, 0.75, 1.0) y horizontal (1, 2). Es poligonal: recta de pendiente suave desde (0,0) hasta (1, 0.25) y luego recta de pendiente mayor desde (1, 0.25) hasta (2, 1.0). Líneas punteadas marcan los valores 0.25 en $x=1$ y 1.0 en $x=2$.

**Figura 4-2. La función de densidad y la función de distribución acumulativa, para el ejemplo 2.**

**Ejemplo 2.** Genérense los valores $x$ de variables aleatorias con una función de densidad

$$f(x) = \frac{1}{4} \qquad 0 \le x \le 1 \tag{4-7}$$

$$= \frac{3}{4} \qquad 1 \le x \le 2$$

(La función de densidad y la función de distribución acumulativa se ilustran gráficamente en la figura 4-2.) A partir de la ecuación (4-3) sigue que

$$r = F(x) = \int_{0}^{x} \frac{1}{4}\,dt \qquad 0 \le x < 1 \tag{4-8}$$

$$= \frac{x}{4}$$

---

--- pág. 4 (libro pp. 90-91) ---

**90  GENERACIÓN DE VALORES DE LAS VARIABLES**

$$r = F(x) = \frac{1}{4} + \int_{1}^{x} \frac{3}{4}\,dt \qquad 1 \le x \le 2 \tag{4-9}$$

$$= \frac{3}{4}x - \frac{1}{2}.$$

Si tomamos la transformación inversa $F^{-1}(r)$ y resolvemos en $x$ las ecuaciones (4-8) y (4-9), obtenemos

$$x = 4r \qquad 0 \le r < \frac{1}{4} \tag{4-10}$$

$$x = \frac{4}{3}r + \frac{2}{3} \qquad \frac{1}{4} \le r \le 1. \tag{4-11}$$

Para generar un valor de $x$ deberemos, en primer lugar, generar [un] valor de $r$; cuando $r$ sea menor que 1/4, el valor de $x$ estará determinado por la ecuación (4-10). Si $r$ es mayor o igual a 1/4, entonces $x$ estará determinada por la ecuación (4-11). Para el caso de los intervalos múltiples sobre la escala caracterizada por $r$, podemos fácilmente generalizar este procedimiento a fin de generar los valores de las variables aleatorias que correspondan a una determinada distribución empírica.

Desafortunadamente, para muchas de las distribuciones de probabilidad, resulta imposible o extremadamente difícil expresar a $x$ en términos de la transformación inversa $F^{-1}(r)$. Cuando es éste el caso, el único recurso de que disponemos consiste en obtener una aproximación numérica para la transformación inversa $F^{-1}(r)$, o bien recurrir a alguno de los siguientes dos métodos.

### El método de rechazo

Si $f(x)$ es una función acotada y $x$ tiene además un rango finito, como $a \le x \le b$, entonces se puede utilizar la técnica de rechazos [29] para generar los valores de variables aleatorias. La aplicación de esta técnica requiere que se proceda de acuerdo con las siguientes etapas:

1. Normalizar el rango de $f$ mediante un factor de escala $c$ tal que

$$c \cdot f(x) \le 1 \qquad a \le x \le b: \tag{4-12}$$

2. Definir a $x$ como una función lineal de $r$, o sea

$$x = a + (b - a)r. \tag{4-13}$$

3. Generar parejas de números aleatorios $(r_1\ r_2)$.

4. Siempre que se encuentre una pareja de números aleatorios [que] satisfagan la relación

$$r_2 \le c \cdot f[a + (b - a)r_1]. \tag{4-14}$$

**INTRODUCCIÓN  91**

dicho par será aceptado y se utilizará a $x = a + (b - a)r_1$ como el valor generado de la variable aleatoria.

La teoría sobre la que se apoya este método se basa en el hecho ya conocido relativo a la probabilidad de que $r$ sea menor o igual a $c \cdot f(x)$ es

$$P[r \le c \cdot f(x)] = c \cdot f(x). \tag{4-15}$$

En consecuencia, si $x$ se elige al azar dentro del rango $(a, b)$ de acuerdo con la ecuación (4-13) y en el caso de que $r > c \cdot f(x)$ se rechaza, la función de densidad de probabilidad de los valores de $x$ aceptados deberá ser igual a $f(x)$. Tocher [28, p. 25] ha demostrado que la esperanza matemática del número de intentos que se realizan, antes de encontrar una pareja exitosa, es igual a $1/c$. Esto implica que para ciertas funciones de densidad de probabilidad este método puede resultar sumamente ineficaz. En muchas de las técnicas generatrices que se describen en este capítulo se empleará este método, para lo cual se incluyen dos ejemplos a fin de aclarar ideas sobre él.

> [FIGURA 4-3, pág. 4]: Dos gráficas lado a lado que ilustran el escalamiento.
> Izquierda, rotulada "Antes de escalar": ejes $f(x)$ (vertical, con marcas en 1 y 2) y $x$ (horizontal, con marca en 1). Recta que sale del origen y llega al punto (1, 2), es decir $f(x) = 2x$ sobre $0 \le x \le 1$. Líneas punteadas marcan el punto (1, 2).
> Derecha, rotulada "Después de escalar": ejes $g(r)$ (vertical, marca en 1) y $x$ (horizontal, marca en 1). Recta desde el origen hasta el punto (1, 1), es decir $g(r) = r$ sobre el intervalo unitario. Líneas punteadas marcan el punto (1, 1).

**Figura 4-3. Un ejemplo de escalamiento.**

**Ejemplo 1.** Utilice el método de rechazo para generar los valores $x$ de las variables aleatorias, con una función de densidad $f(x) = 2x$ para las que $0 \le x \le 1$.

Puesto que $x$ ha sido definida sobre el intervalo unitario, se tendrá que $x = r$; pero $f(r) = 2r$ está definida en el intervalo $0 \le f(r) \le 2$. En consecuencia, si se escala haciendo $g(r) = 1/2f(r)$, se transformará a $f(r)$ al intervalo unitario, en cuyo caso $g(r) = r$. La figura 4-3 muestra la función de densidad $f(x) = 2x$, antes del proceso de escalamiento y después de él.

Para el ejemplo 1 el método de rechazo consta de cuatro pasos:

1. Generar $r_1$ y calcular $g(r_1)$.

---

--- pág. 5 (libro pp. 92-93) ---

**92  GENERACIÓN DE VALORES DE LAS VARIABLES**

> [NOTA]: en el original el número de página aparece cortado por el margen y sólo se lee "2".

2. Generar $r_2$ y compararlo con $g(r_1)$.

3. Si $r_2 \le g(r_1)$, se acepta a $r_1$ tomándolo como una $x$ de $f(x)$; si $r_2 \le g(r_1)$, se rechaza a $r_1$ y se vuelve a empezar por el paso 1.

4. Este proceso se repite hasta haber generado $n$ valores de $x$. El método de rechazo se puede utilizar también, al igual que la técnica Monte Carlo, para evaluar integrales definidas.

**Ejemplo 2.** Use el método de rechazo para computar el área correspondiente al primer cuadrante de un círculo unitario cuyos ejes coordenados son $r_1$ y $r_2$, respectivamente (figura 4-4). Este problema de integración numérica servirá para ilustrar el empleo del método Monte Carlo en la solución de un problema completamente determinístico. Cualquier pareja de números aleatorios $(r_2, r_3)$ definidos en el intervalo unitario, corresponde a un punto contenido en el cuadrado unitario de la figura 4-4; obsérvese que los puntos que satisfacen la ecuación $r_2^2 + r_3^2 = 1$ se encuentran en la circunferencia. Sea $g(r_2) = \sqrt{1 - r_2^2}$; si para los números aleatorios generados $(r_2^{\,0}, r_3^{\,0})$ se tiene que $g(r_2^{\,0}) \ge r_3^{\,0}$, entonces $(r_2^{\,0}, r_3^{\,0})$ será un punto aleatorio bajo la curva. Pero si $g(r_2^{\,0}) < r_3^{\,0}$, entonces $(r_2^{\,0}, r_3^{\,0})$ será un punto que se encuentre sobre la curva. Al aceptar y contar el primer tipo de ocurrencias aleatorias y luego dividir esta cuenta entre el número total de parejas generadas, obtenemos un cociente que corresponde a la proporción del área del cuadrado unitario que se encuentra bajo la curva.

Este cociente se aproximará al valor de $\pi/4$, a medida que se incremente el número de pares de variables aleatorias aceptados. Esta misma técnica se puede aplicar a la solución de integrales múltiples de funciones con más de una variable independiente.

> [FIGURA 4-4, pág. 5]: Cuadrado unitario con eje horizontal $r_1$ (marca en 1) y eje vertical $r_2$ (marca en 1). Dentro del cuadrado se traza el arco del primer cuadrante de la circunferencia unitaria, que va del punto (0, 1) al punto (1, 0). Líneas punteadas indican un punto genérico $(r_1, r_2)$ ubicado bajo el arco. La razón entre puntos aceptados (bajo el arco) y puntos totales generados estima el área $\pi/4$.

**Figura 4-4. Integración numérica.**

### El método de composición

Otro método para generar valores de variables estocásticas utilizando computadoras es el llamado método de composición o método de mezclas [7, 13, 18, 19, 28]. En este método se expresa a $f(x)$ como una mezcla probabilística de las funciones de densidad $g_n(x)$ seleccionadas adecuadamente. En términos matemáticos tenemos

$$f(x) = \Sigma g_n(x)\,p_n. \tag{4-16}$$

La guía para la selección de las $g_n(x)$ está dada sobre las consideraciones relativas a la bondad del ajuste y al objetivo de minimizar $\Sigma T_n p_n$, donde

**INTRODUCCIÓN  93**

$T_n$ es el tiempo esperado de computación para generar valores de variables aleatorias a partir de $g_n(x)$.

En las partes subsecuentes de este capítulo, se proveerá al lector de un conjunto de (relativamente simples) técnicas específicas para simular valores de variables aleatorias, considerando algunas de las distribuciones de probabilidad mejor conocidas. En el caso de algunas distribuciones, se considerará más de un método alternativo. Intentamos desplazarnos desde las distribuciones de probabilidad específicas hasta los modelos estocásticos en general, con el fin de ampliar nuestro estudio sobre las técnicas de simulación. Para una revisión de los elementos de la teoría de probabilidades, remitiremos al lector a los textos siguientes [1, 8, 10, 23, 31].

En principio, se cubrirán separadamente las distribuciones de probabilidad continua y discreta. Primeramente se tratarán seis de las distribuciones continuas más comunes: la uniforme, exponencial, gamma, normal, normal multivariada y normal logarítmica. Para cada una de ellas se proporcionará la siguiente información: (1) una breve descripción relativa a la naturaleza y uso de la distribución; (2) las fórmulas para la función de densidad, la función de distribución acumulativa (si es que existe en forma explícita), el valor de la esperanza matemática y la varianza de la distribución; (3) los parámetros de la distribución, expresados en términos de los momentos de la distribución; (4) una explicación o en su defecto una derivación, de las técnicas más simples para generar los valores de las variables aleatorias de acuerdo con la distribución; (5) un diagrama de flujo y un programa en FORTRAN para generar los valores de las variables aleatorias mediante una computadora digital; (6) algunas técnicas alternativas para generar los mismos valores; (7) una lista útil de los valores de las variables aleatorias relacionadas o derivables de los valores encontrados en (el caso de que existan). Se respetará un formato semejante en el tratamiento de las cinco distribuciones discretas de probabilidad: la geométrica, de Pascal, la binomial, hipergeométrica y de Poisson. Se dedicarán secciones especiales para las distribuciones empíricas, los procesos de Markov y los valores de las variables aleatorias autocorrelacionados.

Aunque este capítulo está orientado a la utilización de las computadoras digitales en la simulación de distribuciones de probabilidad, la computadora no constituye, en forma alguna, un requisito previo para emplear las técnicas que se encuentran en este capítulo. Para mayor seguridad, en cualesquiera de los métodos que aquí se tratan, se pueden utilizar las técnicas de computación manual. Empero, si el número de las distribuciones de probabilidad que se van a simular es muy grande, y la cantidad de datos por simular es considerable, será imperioso el empleo de la computadora.

En este libro se seleccionó el sistema de programación FORTRAN debido a que es un lenguaje de computadora ampliamente utilizado, que se

---

--- pág. 6 (libro pp. 94-95) ---

**94  GENERACIÓN DE VALORES DE LAS VARIABLES**

asemeja mucho al lenguaje de las matemáticas y fue diseñado en principio para los procesos de computación tanto científicos como ingenieriles. Una de las ventajas principales de FORTRAN es la de proporcionar al analista un medio eficiente para escribir sus programas de computadora. Además, no requiere para su uso un período muy largo de instrucción, así como tampoco algún conocimiento detallado de la propia computadora. Aún más, los compiladores FORTRAN se encuentran en la actualidad disponibles para casi todas las computadoras en uso, ya sea en la industria, en las dependencias del Gobierno y en las universidades. En este libro se encuentra un lenguaje FORTRAN que no necesariamente está diseñado para una computadora en particular y con muy pocas modificaciones se puede adaptar al de cualquier máquina que tenga un compilador FORTRAN. Debido a esto, las proposiciones FORTRAN que aparecen en este libro se han mantenido, deliberadamente, con una estructura muy simple y sin que se incluya el empleo de los medios de entrada y salida. El lector que no esté familiarizado con el FORTRAN podrá consultar el respectivo manual, publicado por algunos fabricantes de computadoras, o alguno de los siguientes textos sobre FORTRAN [15, 22].

En este capítulo las proposiciones FORTRAN se presentarán como subrutinas (SUBROUTINE) y supone que existe un programa principal de simulación llamado MAIN, el cual llama a las apropiadas subrutinas mediante la proposición CALL. Cada subrutina, genera y envía al programa principal un solo valor de la variable aleatoria, a partir de una distribución de probabilidad para la cual fue programada. El programa principal deberá contener las instrucciones que permitan leer los valores de los parámetros que se requieran, el número de valores de las variables aleatorias que se deban generar y los criterios acerca de cómo manipular los resultados estadísticos.

A fin de evitar complicaciones notacionales al escribir subrutinas FORTRAN que contengan otras subrutinas, se establecerá que los números pseudoaleatorios están generados por una función propia del compilador y disponible en un programa de biblioteca previamente programado. Esta función se denota por RND y se supone programada en lenguaje de máquina de acuerdo con el criterio de alguno de los métodos propuestos en el capítulo 3. Otras funciones de biblioteca de las que se puede disponer también en forma de subrutinas, son la función logarítmica (de base $e$), denotada por LOG y la función exponencial (en base $e$) representada por EXP.

Ahora podemos enfocar nuestra atención a la tarea de desarrollar los métodos previamente mencionados, relativos a la generación de los valores de variables aleatorias a partir de las distribuciones de probabilidad.

**DISTRIBUCIONES CONTINUAS DE PROBABILIDAD  95**

## DISTRIBUCIONES CONTINUAS DE PROBABILIDAD

### La distribución uniforme

Quizá la función de densidad de probabilidad más simple es aquella que se caracteriza por ser constante, en el intervalo $(a, b)$ y cero fuera de él. Esta función de densidad define la distribución conocida como uniforme o rectangular. La distribución uniforme surge cuando se estudian las características de los errores por redondeo al registrar un conjunto de medidas sujetas a cierto nivel de precisión. Por ejemplo, si se registran medidas de peso con una aproximación determinada en gramos, puede suponerse que la diferencia en gramos entre el peso real y el peso registrado corresponde a un cierto número entre $-0.5$ y $+0.5$, y que el error se encuentra distribuido uniformemente en este intervalo. El valor más sobresaliente que puede tener la distribución uniforme respecto a las técnicas de simulación radica en su simplicidad y en el hecho de que esta distribución se puede emplear para simular variables aleatorias a partir de casi cualquier tipo de distribución de probabilidad.

Matemáticamente, la función de densidad uniforme se define como sigue:

$$f(x) = \begin{cases} \dfrac{1}{b-a} & a < x < b \\[2mm] 0 & \text{fuera del intervalo } (a, b)\end{cases} \tag{4-17}$$

En esta expresión, $X$ es una variable aleatoria definida en el intervalo $(a, b)$. La gráfica de la distribución uniforme queda ilustrada en la figura 4-5.

La función de la distribución acumulativa $F(x)$, para una variable aleatoria $X$ uniformemente distribuida, se puede representar por

$$F(x) = \int_{a}^{x} \frac{1}{b-a}\,dt = \frac{x-a}{b-a} \qquad 0 \le F(x) \le 1. \tag{4-18}$$

El valor esperado y la varianza de una variable aleatoria uniformemente distribuida están dados por las siguientes expresiones\*

$$EX = \int_{a}^{b} \frac{1}{b-a}\,x\,dx = \frac{b+a}{2} \tag{4-19}$$

$$VX = \int_{a}^{b} \frac{(x-EX)^2}{b-a}\,dx = \frac{(b-a)^2}{12}. \tag{4-20}$$

Al efectuar aplicaciones de esta función, los parámetros de la función

---

\* A fin de evitar confusiones con las variables FORTRAN que llevan subíndice, utilizamos los símbolos $EX$ y $VX$ para indicar, respectivamente, la media (o valor esperado) y a la varianza de $X$, en lugar de $E(X)$ y $V(X)$.

---

--- pág. 7 (libro pp. 96-97) ---

**96  GENERACIÓN DE VALORES DE LAS VARIABLES**

de densidad uniforme (4-17) esto es, los valores numéricos de $a$ y de $b$, no necesariamente deben ser conocidos en forma directa. En casos típicos, aunque esto no sucede en todas las distribuciones uniformes, solamente conocemos la media y la varianza de la estadística que se va a generar. En estos casos, los valores de los parámetros se deben derivar al resolver el sistema que consta de las ecuaciones (4-19) y (4-20), para $a$ y para $b$, pues se supone que $EX$ y $VX$ son conocidos. Este procedimiento, semejante

> [FIGURA 4-5, pág. 7]: Gráfica de la función de densidad uniforme. Eje vertical $f(x)$ con una marca en $\dfrac{1}{b-a}$; eje horizontal $x$ con marcas en $a$ y $b$. La curva es un rectángulo: la función vale $1/(b-a)$ constante entre $a$ y $b$ (trazo horizontal punteado hasta el eje vertical y verticales punteadas en $a$ y $b$), y cero fuera de ese intervalo.

**Figura 4-5.**

a una técnica de estimación conocida en la literatura estadística como método de momentos, proporciona las siguientes expresiones:

$$a = EX - \sqrt{3VX} \tag{4-21}$$

$$b = 2EX - a. \tag{4-22}$$

Para simular una distribución uniforme sobre cierto intervalo conocido $(a, b)$ deberemos, en primer lugar, obtener la transformación inversa para la ecuación (4-18), de acuerdo con la ecuación (4-2).

$$x = a + (b - a)r \qquad 0 \le r \le 1. \tag{4-23}$$

En seguida generamos un conjunto de números aleatorios correspondientes al rango de las probabilidades acumulativas, es decir, los valores de variables aleatorias uniformes definidas sobre el rango 0 a 1. Cada número aleatorio $r$ determina, de manera única, un valor de la variable aleatoria $x$ uniformemente distribuida.

Para aclarar estas afirmaciones es probable que lo mejor sea presentar una explicación gráfica. La figura 4-6 nos ilustra cómo cada valor generado de $r$ está asociado con uno y sólo un valor de $x$. Por ejemplo, el valor específico de la función de distribución acumulativa en $r_0$ determina el valor de $x$ en $x_0$. Obviamente, este procedimiento se puede repetir tantas veces como se desee y en cada repetición se generará un nuevo valor de $x$. En este capítulo se observará cómo la generación de valores de variables aleatorias se puede seguir, mediante el uso de probabilidades acumulativas, de muchas otras distribuciones. Aún más, esta técnica sirve de base para

> [FIGURA 4-7, pág. 7]: Diagrama de flujo vertical, de arriba hacia abajo, con estos bloques encadenados por flechas:
> (óvalo) PROGRAMA PRINCIPAL → (rectángulo) CALL UNIFRM (A, B, X) → (rectángulo) SUBROUTINE UNIFRM (A, B, X) → (rectángulo) GENERAR R → (rectángulo) X = A + (B − A) * R → (rectángulo) RETURN → (óvalo) PROGRAMA PRINCIPAL.

**Figura 4-7. Diagrama de flujo de la generación de valores de variables aleatorias uniformes.**

**DISTRIBUCIONES CONTINUAS DE PROBABILIDAD  97**

> [FIGURA 4-6, pág. 7]: Gráfica de la función de distribución acumulativa de la uniforme. Eje vertical $F(x)$, con marcas en 1 y en un valor intermedio $r_0$; eje horizontal $x$ con marcas en $a$, $x_0$ y $b$. La curva vale 0 a la izquierda de $a$, crece como recta de pendiente constante $1/(b-a)$ entre $a$ y $b$, y vale 1 (horizontal) a la derecha de $b$. Líneas punteadas: horizontal desde $r_0$ hasta la recta y vertical desde ese punto hasta $x_0$, mostrando la correspondencia $r_0 \to x_0$.

**Figura 4-6**

desarrollar los métodos más generales de los procesos de Monte Carlo, como se discutirá durante el desarrollo de este capítulo.

La figura 4-7 contiene un diagrama de flujo, asociado a la lógica que debe emplearse al simular una distribución uniforme para un intervalo dado $(a, b)$, para cuando se pretenda programar su estructura en una computadora. El diagrama de flujo se ha formulado de tal modo que resulta compatible con la subrutina FORTRAN, de la figura 4-8.

La primera declaración de nuestro diagrama FORTRAN para generar los valores de variables aleatorias, es una declaración CALL, que comprende el nombre de la subrutina y las variables de ésta. Los nombres de la subrutina usualmente se limitan a seis caracteres; por consiguiente, a esta subrutina en particular se le ha dado el nombre de UNIFRM. Los símbolos $A$, $B$ y $X$ que aparecen entre paréntesis representan a los parámetros $a$ y $b$, así como al valor de la variable aleatoria $x$, respectivamente. El valor $x$ se genera por medio de la subrutina y se regresa al programa principal mediante el efecto de la misma. Debe hacerse notar que la proposición CALL constituye una parte del programa principal, razón por lo que no se ha incluido en las instrucciones FORTRAN que aparecen en la figura 4-8.

La primera proposición en esta subrutina (figura 4-8) es de inicialización, la cual identifica, a su vez, la subrutina particular que es llamada por el programa principal. Cada una de las subrutinas que se describen en este capítulo

---

--- pág. 8 (libro pp. 98-99) ---

**98  GENERACIÓN DE VALORES DE LAS VARIABLES**

empezarán con una proposición similar de inicialización o de identificación.

La segunda proposición en la subrutina (figura 4-8) es una función de biblioteca cuyo efecto es el de fijar a la variable $R$ igual a un número pseudoaleatorio generado por la función RND; cada vez que se llama a la

```
1. SUBROUTINE UNIFRM (A, B, X)
2. R = RND (R)
3. X = A + (B - A) * R
4. RETURN
```

**Figura 4-8. Subrutina FORTRAN para la generación de valores de variables aleatorias uniformes.**

subrutina se genera un nuevo valor para $R$. La variable $R$ es el símbolo FORTRAN que representa a $r$ en la ecuación (4-23).

La tercera proposición en nuestra subrutina FORTRAN transforma a R del intervalo $(0, 1)$ al intervalo $(a, b)$ mediante una expresión aritmética FORTRAN basada en la ecuación (4-23).

La cuarta proposición FORTRAN de la figura 4-8 regresa al programa principal el valor generado de $X$ y el propio control del programa.

En lo que resta del presente capítulo se desarrollarán otras rutinas similares a la anterior.

### La distribución exponencial

Durante nuestra experiencia diaria, observamos cómo transcurren los intervalos de tiempo definidos entre las ocurrencias de los eventos aleatorios distintos, y sobre la base de un plan de tiempos completamente independientes, recibimos información sobre numerosos eventos que ocurren en nuestro alrededor. Bastaría con citar los nacimientos, defunciones, accidentes, o conflictos mundiales, para mencionar sólo algunos. Si es muy pequeña la probabilidad de que ocurra un evento en un intervalo corto, si la ocurrencia de tal evento es, estadísticamente independiente respecto a la ocurrencia de otros eventos, entonces el intervalo de tiempo entre ocurrencias de eventos de este tipo estará distribuido en forma exponencial. El hecho de que en el mundo real un proceso estocástico proporcione o no efectivamente valores de variables aleatorias de tipo exponencial, constituye una cuestión empírica cuya confirmación depende del grado en que se satisfagan las suposiciones que sirven de base a la distribución exponencial. Específicamente, para los valores de variables aleatorias de tipo exponencial se deben satisfacer las siguientes suposiciones:

1. La probabilidad de que ocurra un evento en el intervalo $[t, (t + \Delta t)]$ es $\alpha \Delta t$.

**DISTRIBUCIONES CONTINUAS DE PROBABILIDAD  99**

2. $\alpha$ es una constante que no depende de $t$ o de algún otro factor.

3. La probabilidad de que durante un intervalo $[t, (t + \Delta t)]$ ocurra más de un evento, tiende a 0 a medida que $\Delta t \to 0$, y su orden de magnitud deberá ser menor que el de $\alpha \Delta t$.

Curiosamente, se ha encontrado que el comportamiento de un considerable número de procesos dependientes del tiempo satisfacen las anteriores suposiciones un tanto fuertes. Por ejemplo, el intervalo entre los accidentes en una fábrica, la llegada de pedidos a una compañía, el registro de pacientes en un hospital, el aterrizaje de aviones en un aeropuerto, etc., satisfacen una distribución exponencial.

> [FIGURA 4-9, pág. 8]: Dos gráficas lado a lado de la distribución exponencial.
> Izquierda — función de densidad $f(x)$: eje vertical con marca en 1, eje horizontal $x$. Curva decreciente que arranca en el valor 1 sobre el eje vertical y decae monótonamente hacia cero (forma de "J" invertida, decaimiento exponencial).
> Derecha — función de distribución acumulativa $F(x)$: eje vertical con marca en 1 (línea horizontal punteada de referencia en 1), eje horizontal $x$. Curva creciente que arranca en el origen y se acerca asintóticamente a 1.

**Figura 4-9**

Se dice que una variable aleatoria $X$ tiene una distribución exponencial, si se puede definir a su función de densidad como:

$$f(x) = \alpha e^{-\alpha x} \tag{4-24}$$

con $\alpha > 0$ y $x \ge 0$.

La función de distribución acumulativa de $X$ está dada por:

$$F(x) = \int_{0}^{x} \alpha e^{-\alpha t}\,dt = 1 - e^{-\alpha x}, \tag{4-25}$$

y la media junto con la varianza de $X$ se pueden expresar como

$$EX = \int_{0}^{\infty} x\alpha e^{-\alpha x}\,dx = \frac{1}{\alpha} \tag{4-26}$$

$$VX = \int_{0}^{\infty} \left(x - \frac{1}{\alpha}\right)^2 \alpha e^{-\alpha x}\,dx = \frac{1}{\alpha^2} = (EX)^2 \tag{4-27}$$

En figura 4-9 aparece la gráfica de la distribución exponencial.

Obsérvese que, como la distribución exponencial solamente tiene un parámetro $\alpha$, es posible expresarlo como:

$$\alpha = \frac{1}{EX} \tag{4-28}$$

Existen muchas maneras para lograr la generación de valores de variables

---

--- pág. 9 (libro pp. 100-101) ---

**100  GENERACIÓN DE VALORES DE LAS VARIABLES**

aleatorias exponenciales. Puesto que $F(x)$ existe explícitamente, la técnica de la transformación inversa nos permite desarrollar métodos directos para dicha generación. Debido a la simetría que existe entre la distribución uniforme sigue que la intercambiabilidad de $F(x)$ y $1 - F(x)$. Por lo tanto,

$$r = e^{-\alpha x} \tag{4-29}$$

y consecuentemente

$$x = -\left(\frac{1}{\alpha}\right)\log r = -EX \log r. \tag{4-30}$$

Por consiguiente, para cada valor del número pseudoaleatorio $r$ se determina un único valor para $x$. Los valores de $x$ toman tan sólo magnitudes no negativas, debido a que $\log r \le 0$ para $0 \le r \le 1$, y además se ajustan a la función de densidad exponencial (4-24) con un valor esperado $EX$. Conviene hacerle notar al lector, que pese a que esta técnica parece en principio muy simple, es preciso recordar que en una computadora digital el cálculo del logaritmo natural involucra una expansión en serie de potencias (o una técnica equivalente de aproximación) para cada valor de variable aleatoria uniforme que se deba generar.

La figura (4-10) contiene un diagrama de flujo para generar valores de variables aleatorias exponenciales, mientras que la figura 4-11 contiene la subrutina FORTRAN correspondiente. El nombre que se da a esta subrutina es EXPENT.

La técnica de la transformación inversa es el único método para generar valores de variables aleatorias exponenciales con procedimientos internos. En este libro se esbozarán dos métodos adicionales: el motivado por su importancia histórica, y el debido a su rapidez potencial.

Un ejemplo ingenioso de utilización de la técnica de rechazo lo constituye el método de Von Neumann [29] para generar valores de variables aleatorias exponenciales; resulta una de esas penosas realidades de la vida, que el empleo de la transformación logarítmica, que para el mismo propósito, sea más conveniente, de-

> [FIGURA 4-10, pág. 9]: Diagrama de flujo vertical con los bloques encadenados de arriba a abajo:
> (óvalo) PROGRAMA PRINCIPAL → (rectángulo) CALL EXPENT (EX, X) → (rectángulo) SUBROUTINE EXPENT (EX, X) → (rectángulo) GENERAR R → (rectángulo) X = − EX * LOG (R) → (rectángulo) RETURN → (óvalo) PROGRAMA PRINCIPAL.

**Figura 4-10. Diagrama de flujo para la generación de valores de variable aleatoria con distribución exponencial.**

**DISTRIBUCIONES CONTINUAS DE PROBABILIDAD  101**

```
1. SUBROUTINE EXPENT (EX, X)
2. R = RND (R)
3. X = -EX * LOG (R)
4. RETURN
```

**Figura 4-11. Subrutina FORTRAN para la generación de valores de variable aleatoria exponencial.**

bido a una ligera diferencia en rapidez. Debido a que este método se menciona muy a menudo en la literatura, aquí ofrecemos una breve descripción de su estructura.

Al generar los números aleatorios uniformes $r_1, r_{11}, r_{12}, \dots, r_{1j}, r_2, r_{21} \dots$ y tomar la sucesión de sumas:

$$1 - r_1 + \sum_{i=1}^{j} r_{1i},$$

$$1 - r_2 + \sum_{i=1}^{j} r_{2i},$$

$$\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot$$

$$1 - r_t + \sum_{i=1}^{j} r_{ti}.$$

cada una de estas series, se acorta o termina, para aquel valor de $j$ para el cual $1 - r_t + \sum_{i=1}^{j} t_{ti} \ge 1$ por primera vez. La sucesión se termina tan pronto como el primer valor de $t$ implique un valor impar para $j$. La cantidad

$$x = (t - 1) + r_t \tag{4-31}$$

constituye un valor de variable aleatoria exponencial para el cual $EX = 1$. En [7, p. 262] y [5, p. 166], se presentan, respectivamente, una prueba del método y un diagrama de flujo para su programación.

El segundo método que se delinea aquí, debido a G. Marsaglia [18], también sirve para generar valores de variable aleatoria con distribución exponencial con media y varianza unitarias, sin requerir los beneficios de la transformación logarítmica. Si el programa correspondiente se escribe en un lenguaje similar al de la subrutina para calcular logaritmos, este método resulta más rápido que el de la técnica de transformación inversa. Además, este procedimiento constituye un ejemplo excelente del método de composición.

El valor de la variable aleatoria $x$ distribuida exponencialmente, está dado por

$$x = m + \min_{i} (r_1, r_2, \dots, r_i, \dots, r_n) \tag{4-32}$$

---

--- pág. 10 (libro pp. 102-103) ---

**102  GENERACIÓN DE VALORES DE LAS VARIABLES**

donde las $r_i$ son números pseudoaleatorios uniformemente distribuidos; los valores de $m$ y $n$ para una $x$ particular están determinados por las siguientes distribuciones acumulativas discretas de probabilidad:

$$P(M \le m) = \sum_{k=0}^{m} \frac{1}{ce^{k+1}} \qquad \text{para } m = 0, 1, 2, \dots \tag{4-33}$$

$$P(N \le n) = \sum_{k=1}^{n} \frac{c}{k!} \qquad \text{para } n = 1, 2, 3, \dots \tag{4-34}$$

donde $c = 1/(e - 1)$. Los valores (de variables aleatorias) de $m$ y $n$ se computan mediante la generación de dos números aleatorios, cuyos valores correspondientes se calculan haciendo uso de la transformación inversa en las ecuaciones (4-33) y (4-34). A fin de obtener un valor de variable aleatoria exponencial la probabilidad de que sólo se generen tres números aleatorios es de 0.58; para no más de cinco, la probabilidad es de 0.9[…]. Cuando se desee generar valores de variables aleatorias con $EX \neq 1$, bastará con multiplicar el valor de $x$, determinado por la ecuación (4-32), por el valor de $EX$.

La distribución exponencial se basa en el supuesto de que se tiene un parámetro constante $\alpha$. En otras palabras, se supone que todos los eventos han sido generados por un solo proceso aleatorio. En el mundo real frecuentemente se viola esta suposición, sobre todo, cuando tratamos con eventos indistinguibles que son producto de procesos aleatorios diferentes pero entremezclados. Resulta en muchas ocasiones posible, y hasta frecuente, que al tomar una muestra ésta provenga de dos o más distribuciones exponenciales, cada una de las cuales tenga un valor diferente de $\alpha$. En este caso tenemos una mayoría de problemas sobre fenómenos de espera (colas); por ejemplo, las llegadas pueden ocurrir en razones iguales a $\alpha_i$ con probabilidades $p_i$, en las que $\alpha_i$ representa el parámetro de la $i$-ésima población ($i = 1, 2, \dots, s$), tal que $\alpha_i \neq \alpha_j$ y $\sum_{i=1}^{s} p_i = 1$. Esta mezcla de valores exponenciales se dice que obedece a una distribución hiperexponencial ($s = 2$) o a una exponencial generalizada ($s > 2$). Para generar la mezcla dada de $s$ valores de variables aleatorias exponenciales, sencillamente se intercala un interruptor de probabilidad antes de la instrucción CALL en la figura 4-10, con la cual se puede decidir cuál de los $s$ valores de $1/\alpha_i$, previamente almacenados, debe ser el que se aplique en la transformación inversa. El problema real radica en el hecho de que raramente conocemos cuál es el tipo de mezcla que se tiene o debe generar. Sin embargo, algunas veces se pueden considerar ciertas hipótesis simplificadoras. Dos casos de este tipo se describen a continuación:

1. Las llegadas se originan solamente en dos poblaciones y tienen probabilidades $p$ y $(1 - p)$ con parámetros $p2\alpha$ y $(1 - p)2\alpha$, respectiva-

**DISTRIBUCIONES CONTINUAS DE PROBABILIDAD  103**

mente. Este proceso genera valores de variable aleatoria hiperexponenciales [20] con media igual a $1/\alpha$ y con una función de densidad:

$$f(x) = 2p^2\alpha \exp(-2p\alpha x) + 2(1-p)^2\alpha \exp[2(1-p)\alpha x] \tag{4-35}$$

La varianza de $x$ es

$$VX = \frac{1}{\alpha^2}\left[\frac{1}{2p(1-p)} - 1\right], \tag{4-36}$$

la cual indica que los valores hiperexponenciales siempre tienen una varianza mayor de $1/\alpha^2$, a menos que $p = 1/2$. En caso de conocer el valor de la sobredispersión $VX/(EX)^2$, para cierto valor dado de $EX = 1/\alpha$ entonces se puede determinar a $p$ como sigue:

$$p = \frac{1}{2} - \frac{1}{2}\left[1 - \frac{2}{VX/(EX)^2 + 1}\right]^{1/2} \tag{4-37}$$

a usarse en el programa como se indicó previamente.

2. Las llegadas se originan en un número infinito de poblaciones diferentes, con un número $\alpha$ también diferente para cada una. Debido a que $\alpha$ es siempre positiva y no está restringida a valores enteros, podemos suponer que la probabilidad de cualquier valor de $\alpha$ se ajusta a una distribución gamma. En los casos en que componemos valores de variables aleatorias, distribuidos exponencialmente y que se ajustan a una distribución gamma, diremos que se forma una *distribución exponencial generalizada* (o bien una distribución Pearson del tipo XI) [16]. La función de densidad correspondiente es:

$$f(x) = ka^k(a + x)^{-(k+1)}, \tag{4-38}$$

y su función de distribución acumulativa está dada por:

$$F(x) = 1 - \left(\frac{a}{a+x}\right)^k, \tag{4-39}$$

donde $k$ y $a$ son los parámetros de la variable aleatoria repartida de acuerdo con la distribución gamma. Haciendo $r = 1 - F(x)$ y aplicando la transformación inversa de la expresión dada en (4-39), se sigue que:

$$x = a\left[\left(\frac{1}{r}\right)^{1/k} - 1\right] \tag{4-40}$$

es una variable aleatoria con una función de densidad igual a la que se expresa en la ecuación (4-38). Para generar valores de variable aleatoria que se ajusten a una distribución exponencial con media $EX$ y varianza

---

--- pág. 11 (libro pp. 104-105) ---

**104  GENERACIÓN DE VALORES DE LAS VARIABLES**

$VX$, tales que $VX > (EX)^2$, se pueden utilizar las siguientes fórmulas:

$$k = \frac{2VX}{[VX - (EX)^2]} \tag{4-41}$$

$$a = (k - 1)EX, \tag{4-42}$$

las cuales resultan válidas solamente para valores de $k > 2$.

La generalización de la distribución exponencial resulta una tarea demasiado simple cuando se consideran variables positivas $x \ge a$ con $a$ estrictamente positiva. En este caso, la substitución de $(x - a)$ por $x$ conduce de inmediato a la así llamada distribución exponencial no central o de doble parámetro, la cual se puede simular sin dificultad alguna por cualesquiera de los métodos que se han tratado previamente.

Una más de las extensiones de la distribución exponencial es la conocida por el nombre de distribución Weibull [30], con una función de densidad y una distribución acumulativa que se pueden expresar como sigue:

$$f(x) = \frac{c}{b}\left(\frac{x-a}{b}\right)^{c-1}\exp\left[-\left(\frac{x-a}{b}\right)^{c}\right] \tag{4-43}$$

$$F(x) = 1 - \exp\left[-\left(\frac{x-a}{b}\right)^{c}\right] \tag{4-44}$$

para $x \ge a$, $a \ge 0$, $b > 0$ y $c > 0$.

En esta descripción el parámetro de ubicación $a$ se supone con un valor idénticamente nulo, lo cual deja a $b$ y a $c$, como parámetros de escala y de forma, respectivamente. Como únicos datos de caracterización, el papel que desempeña la constante $1/b$ es análogo al de $\alpha$ en la distribución exponencial. Si $c = 1$, la expresión (4-43) resulta idéntica a la dada en la ecuación (4-24), pero si $c > 1$, entonces la distribución adopta la forma de una campana. En cualquier otro caso esta distribución mantendrá la forma de una "J", al igual que la distribución exponencial. Se ha encontrado que esta distribución resulta de gran utilidad cuando se realiza el tratamiento de problemas relacionados con la vida media, resistencia a la ruptura y los datos relacionados con los fenómenos de confiabilidad, para los que su comportamiento ha sido descrito satisfactoriamente.

El valor esperado de la ecuación (4-43) está dado por

$$EX = b\Gamma\left(\frac{1}{c} + 1\right), \tag{4-45}$$

y su varianza

$$VX = b^2\Gamma\left(\frac{2}{c} + 1\right) - (EX)^2. \tag{4-46}$$

**DISTRIBUCIONES CONTINUAS DE PROBABILIDAD  105**

La transformación inversa de la ecuación (4-44), utilizando $r = 1 - F(x)$, conduce al proceso de generación de valores de variable aleatoria con distribución Weibull, mediante la siguiente expresión:

$$x = b(-\log r)^{1/c}. \tag{4-47}$$

### La distribución gamma

Si un determinado proceso consiste de $k$ eventos sucesivos y si el total del tiempo transcurrido para dicho proceso se puede considerar igual a la suma de $k$ valores independientes de la variable aleatoria con distribución exponencial, cada uno de los cuales tiene un parámetro definido $\alpha$, la distribución de esta suma coincidirá con una distribución gamma con parámetros $\alpha$ y $k$. La suma de los $k$ (donde $k$ es un entero positivo) valores de variable aleatoria con distribución exponencial con un mismo parámetro $\alpha$, también recibe el nombre de distribución de Erlang [4]. Desde un punto de vista matemático la distribución de Erlang no es otra cosa que la convolución de $k$ distribuciones exponenciales, o sea la distribución de la suma de $k$ variables exponenciales. Aun más, si $k$ se adecúa a la distribución binomial negativa o a la distribución geométrica [6], entonces la suma de $k$ valores de variable aleatoria, con la misma $\alpha$, adoptará la forma de una distribución gamma. La forma más general de una distribución gamma se obtiene al considerar a $k$ con valores positivos pero sin que estén restringidos a ser enteros. Casi siempre resulta posible ajustar alguna de las formas de la distribución gamma a un buen número de distribuciones de datos estadísticos sesgados en forma positiva.

La función gamma está descrita mediante la siguiente función de densidad:

$$f(x) = \frac{\alpha^k x^{(k-1)} e^{-\alpha x}}{(k-1)!} \tag{4-48}$$

donde $\alpha > 0$, $k > 0$ y $x$ se considera no negativo. Pese a que no existe una forma explícita para describir la función acumulativa de la distribución gamma, Pearson [31] ha logrado presentar, en forma tabular, los valores de la llamada función gamma incompleta. Respecto a la media y la varianza de esta distribución, sus correspondientes expresiones están formuladas como sigue:

$$EX = \frac{k}{\alpha} \tag{4-49}$$

$$VX = \frac{k}{\alpha^2}. \tag{4-50}$$

Si $k = 1$, entonces la distribución gamma resulta ser idéntica a la distribución exponencial; mientras que si $k$ es un entero positivo, la distri-

---

--- pág. 12 (libro pp. 106-107) ---

**106  GENERACIÓN DE VALORES DE LAS VARIABLES**

bución gamma coincide con la distribución de Erlang. Conviene también anotar que, a medida que $k$ se incrementa, la distribución gamma tiende, en forma asintótica, a una distribución normal.

Para generar valores de variable aleatoria con distribución gamma y con un valor esperado y varianza dados, se pueden emplear las siguientes fórmulas a fin de determinar los parámetros de $f(x)$ en la ecuación (4-48):

$$\alpha = \frac{EX}{VX} \tag{4-51}$$

$$k = \frac{(EX)^2}{VX}. \tag{4-52}$$

Debido a que para una distribución gamma no se puede formular explícitamente una función de distribución acumulativa, debemos considerar un método alternativo para generar valores de variable aleatoria con distribución gamma. En relación a tales valores que satisfacen la distribución Erlang, éstos se pueden generar con sólo reproducir el proceso aleatorio sobre el cual se basa la distribución de Erlang. Para lograr este resultado se debe tomar la suma de los $k$ valores de variable aleatoria con distribución exponencial $x_1, x_2, \dots, x_k$, cuyo valor esperado es el mismo e igual a $1/\alpha$. En consecuencia, el valor de la variable aleatoria (Erlang) $x$ se puede expresar como

$$x = \sum_{i=1}^{k} x_i = -\frac{1}{\alpha}\sum_{i=1}^{k}\log r_i. \tag{4-53}$$

En las figuras 4-12 y 4-13 aparece un diagrama de flujo y una subrutina en FORTRAN que sirve para generar una distribución Erlang (gamma), en la que $k$ toma valores enteros. El lector debe notar que la ecuación (4-53) no se utiliza en la codificación del programa FORTRAN; en lugar de ésta, se utiliza una forma computacional equivalente y más rápida, que la substituye. Esta expresión corresponde a la siguiente fórmula:

$$x = -\frac{1}{\alpha}\left(\log \prod_{i=1}^{k} r_i\right), \tag{4-54}$$

> [FIGURA 4-12, pág. 12]: Diagrama de flujo vertical con los bloques encadenados de arriba a abajo:
> (óvalo) PROGRAMA PRINCIPAL → (rectángulo) CALL GAMMA (K, A, X) → (rectángulo) SUBROUTINE GAMMA (K, A, X) → (rectángulo) TR = 1.0 → (rectángulo) DO I = 1, K → (rectángulo) GENERAR R → (rectángulo) TR = TR * R, con una flecha punteada de retorno que sube desde este bloque hasta el bloque DO, cerrando el ciclo → (rectángulo) X = −LOG (TR)/A → (rectángulo) RETURN → (óvalo) PROGRAMA PRINCIPAL.

**Figura 4-12. Diagrama de flujo para generar valores de variable aleatoria con distribución gamma.**

**DISTRIBUCIONES CONTINUAS DE PROBABILIDAD  107**

obsérvese también que en la subrutina se utilizan $A$ y $K$ para denotar a $\alpha$ y $k$, respectivamente.

El problema de generar valores de variable aleatoria con distribución gamma cuando el parámetro $k$ no es un entero, queda aún en la actividad como un problema por resolverse, ya que en este caso todavía se formula un método estocástico satisfactorio, sin el cual no puede justificarse algún proceso de simulación correspondiente. Empero, delinearemos uno de los intentos producidos para resolver esta dificultad. Si $k$ es un número racional, entonces se lo puede expresar mediante la suma de un entero más una fracción, de modo tal que $k = k_1 + q$, con $0 < q < 1$; más aún, si $k_2 = k_1 + 1$, entonces se tiene que $k_2 - k_1 = 1 - q$. Nótese que aquí sólo consideraremos el caso en que $k > 1$. Puesto que el valor esperado, la va-

```
1. SUBROUTINE GAMMA (K, A, X)
2. TR = 1.0
3. DO 5 I = 1, K
4. R = RND (R)
5. TR = TR * R
6. X = - LOG (TR)/A
7. RETURN
```

**Figura 4-13. Subrutina FORTRAN para la generación de valores de variable aleatoria con distribución gamma.**

riancia y el tercer momento central de $k$ [23], la distribución gamma de parámetro $k$ se puede aproximar con sólo considerar una mezcla adecuada de valores de variable aleatoria con distribución gamma, para la cual se eligen valores de $k_2$ con probabilidad $q$ y valores de $k_1$ con probabilidad $1 - q$. Si los valores de $k$ son suficientemente grandes, entonces la aproximación lograda con este criterio proporcionará resultados más satisfactorios. Si utilizamos esta técnica en el programa FORTRAN mencionado debemos insertar un interruptor de probabilidad que defina unívocamente los valores de $k$, antes de la proposición DO (en la figura 4-13).

Relacionadas con las variables gamma existe un buen número de distribuciones de probabilidad, de las cuales las más importantes que se pueden mencionar son: la distribución Ji cuadrada y la Beta.

La distribución Ji cuadrada no es otra cosa que una distribución gamma, para la cual $\alpha = 1/2$. Consecuentemente, las variables con distribución Ji cuadrada tienen una media igual a $EX = 2k$, que recibe el nombre de grados de libertad, y una varianza $VX = 4k$. En el caso de ser $EX$ un número par, entonces $k$ es un entero y, en consecuencia, se podrá aplicar la técnica de generación correspondiente a la ecuación (4-54). Si por el

---

--- pág. 13 (libro pp. 108-109) ---

**108  GENERACIÓN DE VALORES DE LAS VARIABLES**

contrario, $EX$ resulta un número impar, entonces $k = EX/2 - 1/2$, y por lo tanto:

$$x = -\frac{1}{\alpha}\log\left(\prod_{i=1}^{k} r_i\right) + z^2, \tag{4-55}$$

donde $z^2$ es el cuadrado de un valor de variable aleatoria con distribución normal, la cual tiene una media nula y una varianza unitaria. La generación de valores de variable aleatoria normales se describirá en la sección siguiente.

La distribución Beta corresponde a los cocientes que se producen con dos variables gamma $x_1$ y $(x_1 + x_2)$, donde $x_1$ y $x_2$ son dos variables independientes a las que corresponde un mismo valor de los parámetros $\alpha$, $k_1$ y $k_2$, respectivamente, de modo que $k = (k_1 + k_2)$ resulte el parámetro de $(x_1 + x_2)$. La variable Beta está dada por

$$x = \frac{x_1}{x_1 + x_2} \qquad 0 < x < 1. \tag{4-56}$$

Por lo tanto, para generar un valor de variable aleatoria $x$ con distribución Beta, se debe obtener el cociente de dos valores de variable aleatoria con distribución gamma, uno con parámetro $k$ y el otro con parámetro $k$.

La función de densidad de la distribución Beta es

$$f(x) = \frac{\Gamma(a+b)x^{a-1}(1-x)^{b-1}}{\Gamma(a)\,\Gamma(b)} \tag{4-57}$$

con un valor esperado y una varianza iguales a

$$EX = a/(a+b) \tag{4-58}$$

$$VX = \frac{(EX)(b)}{(a+b+1)(a+b)}, \tag{4-59}$$

donde $a$ y $b$ corresponden a los parámetros $k_1$ y $k_2$ de los valores de variables aleatorias con distribución gamma, que cumplen la ecuación (4-56). Esta distribución Beta tiene una amplia aplicación, principalmente en los programas referentes al empleo de las técnicas de camino crítico, como por ejemplo PERT [9]. Con estos mismos principios se puede obtener una versión generalizada de la distribución Beta, llamada distribución de Dirichlet, para la cual basta considerar el modelo más de dos cocientes no constantes. Este caso suele surgir al simular vectores fijos o renglones de matrices estocásticas cuyas entradas están asociadas a situaciones de probabilidad variable, así como también, cuando se modelan composiciones aleatorias de ciertas unidades físicas que se encuentran subdivididas en partes o componentes distribuidas al azar.

**DISTRIBUCIONES CONTINUAS DE PROBABILIDAD  109**

### La distribución normal

La más conocida y más ampliamente utilizada distribución de probabilidad es sin duda la distribución normal y su popularidad se debe cuando menos a dos razones que presentan sus propiedades generales. "Pruebas matemáticas nos señalan, que *bajo ciertas condiciones de calidad*, resulta justificado que esperemos una distribución normal mientras que la experiencia estadística muestre que, de hecho, muy a menudo las distribuciones se aproximan a la normal" [8, p. 232].

La distribución normal basa su utilidad en el teorema del límite central. Este teorema postula que, la distribución de probabilidad de la suma de $N$ valores de variable aleatoria $x_i$ independientes pero idénticamente distribuidos, con medias respectivas $\mu_i$ y varianzas $\sigma_i^2$ se aproxima asintóticamente a una distribución normal, a medida que $N$ se hace muy grande, y que dicha distribución tiene como media y varianza respectivamente, a

$$\mu = \sum_{i=1}^{N} \mu_i \tag{4-60}$$

$$\sigma^2 = \sum_{i=1}^{N} \sigma_i^2. \tag{4-61}$$

En consecuencia, el teorema del límite central permite el empleo de distribuciones normales para representar medidas globales operadas sobre los efectos de causas (errores) aditivas distribuidas en forma independiente, sin importar la distribución de probabilidad a que obedezcan las mediciones de causas individuales [25, p. 262]. El carácter que se atribuye a esta forma de interpretación del teorema del límite central resulta de particular importancia, ya que de esta manera se provee una justificación matemática para manipular la evidencia empírica, que tan frecuentemente aparece en los datos distribuidos en forma aproximadamente normal, obtenidos en una gran mayoría de problemas de investigación.

Otro rasgo valiosamente práctico de la distribución normal, es su utilidad para aproximar distribuciones de Poisson y binomiales para mencionar sólo dos entre muchas. A partir de la distribución normal, se pueden derivar otras muchas de las distribuciones existentes que juegan un papel muy importante en la estadística moderna, por ejemplo la $t$, la Ji cuadrada, y la distribución $F$, las cuales se originan a partir de consideraciones hechas sobre la distribución de probabilidad de la suma de los cuadrados de un número específico de valores de variables aleatoria con una distribución estándar.

Si la variable aleatoria $X$ tiene una función de densidad $f(x)$ dada como

$$f(x) = \frac{1}{\sigma_x\sqrt{2\pi}}\,e^{-1/2\left(\frac{x-\mu_x}{\sigma_x}\right)^2}, \qquad -\infty < x < \infty, \tag{4-62}$$

---

--- pág. 14 (libro pp. 110-111) ---

**110  GENERACIÓN DE VALORES DE LAS VARIABLES**

con $\sigma_x$ positiva, entonces se dice que $X$ tiene una distribución normal o Gaussiana, con parámetros $\mu_x$ y $\sigma_x$. En la figura 4-14 se muestra la ya conocida gráfica con su forma de campana, de la función de densidad normal.

Si los parámetros de la distribución normal tienen los valores $\mu_x = 0$ y $\sigma_x = 1$, la función de distribución recibirá el nombre de *distribución normal estándar*, con función de densidad

$$f(z) = \frac{1}{\sqrt{2\pi}}\,e^{-\frac{1}{2}z^2} \qquad -\infty < z < \infty. \tag{4-63}$$

Cualquiera distribución normal se puede convertir a la forma estándar, mediante la siguiente substitución:

$$z = \frac{x - \mu_x}{\sigma_x}. \tag{4-64}$$

La función de distribución acumulativa $F(x)$ o $F(z)$ no existe en forma explícita; sin embargo, esta última se encuentra totalmente tabulada

> [FIGURA 4-14, pág. 14]: Curva de densidad normal con forma de campana simétrica. Eje vertical rotulado $f(x)$; eje horizontal con una única marca, $\mu_x$, ubicada bajo el pico de la campana, y una línea vertical desde el eje hasta el máximo de la curva. Las colas se extienden simétricamente a ambos lados acercándose asintóticamente al eje horizontal.

**Figura 4-14. Una distribución normal.**

en cualquier libro sobre estadística. El valor esperado y la varianza de la distribución normal no estándar están dados por:

$$EX = \mu_x \tag{4-65}$$

$$VX = \sigma_x^2. \tag{4-66}$$

Existen varios métodos para generar en una computadora, valores de variable aleatoria distribuidos en forma normal. Debido a su popularidad sólo discutiremos y demostraremos en detalle el procedimiento llamado del límite central. También se incluirán breves descripciones de otros procedimientos.

A fin de simular una distribución normal con media $\mu_x$ y varianza $\sigma_x^2$ dadas, se debe proponer la siguiente interpretación matemática del teorema del límite central. Si $r_1, r_2, \dots, r_N$ representan variables aleatorias indepen-

**DISTRIBUCIONES CONTINUAS DE PROBABILIDAD  111**

dientes, cada una de las cuales posee la misma distribución de probabilidad caracterizada por $E(r_i) = \theta$ y $\text{Var}(r_i) = \sigma^2$, entonces

$$\lim_{N\to\infty} P\left[a < \frac{\sum_{i=1}^{N} r_i - N\theta}{\sqrt{N}\,\sigma} < b\right] = \frac{1}{\sqrt{2\pi}}\int_{a}^{b} e^{-\frac{1}{2}z^2}\,dz, \tag{4-67}$$

donde

$$E\left(\sum_{i=1}^{N} r_i\right) = N\theta, \tag{4-68}$$

$$\text{Var}\left(\sum_{i=1}^{N} r_i\right) = N\sigma^2, \tag{4-69}$$

$$z = \frac{\sum_{i=1}^{N} r_i - N\theta}{\sigma\sqrt{N}} \tag{4-70}$$

Tanto de la definición de la distribución normal estándar como de la ecuación (4-64), se sigue que $z$ es un valor de variable aleatoria con distribución normal estándar.

El procedimiento para simular valores normales utilizando computadoras requiere el uso de la suma de $K$ valores de variable aleatoria distribuidos uniformemente; esto es, la suma de $r_1, r_2, \dots, r_K$, con cada $r_i$ definida en el intervalo $0 < r_i < 1$. Aplicando la convención notacional de la forma matemática del teorema del límite central, así como nuestros conocimientos previos de la distribución uniforme, encontramos que

$$\theta = \frac{a+b}{2} = \frac{0+1}{2} = \frac{1}{2}, \tag{4-71}$$

$$\sigma = \frac{b-a}{\sqrt{12}} = \frac{1}{\sqrt{12}}, \tag{4-72}$$

$$z = \frac{\sum_{i=1}^{K} r_i - K/2}{\sqrt{K/12}}. \tag{4-73}$$

Pero, por definición, $z$ es un valor de variable aleatoria con distribución normal estándar que se puede escribir en la forma sugerida por la ecuación (4-64), donde $x$ es un valor de variable aleatoria distribuido en forma normal que se va a simular, con media $\mu_x$ y varianza $\sigma_x^2$. Igualando las

---

--- pág. 15 (libro pp. 112-113) ---

**112  GENERACIÓN DE VALORES DE LAS VARIABLES**

ecuaciones (4-73) y (4-64) obtendremos:

$$\frac{x - \mu_x}{\sigma_x} = \frac{\sum_{i=1}^{K} r_i - K/2}{\sqrt{K/12}}, \tag{4-74}$$

y resolviendo para $x$, se tiene que

$$x = \sigma_x\left(\frac{12}{K}\right)^{1/2}\left(\sum_{i=1}^{K} r_i - \frac{K}{2}\right) + \mu_x. \tag{4-75}$$

Por lo tanto, mediante la ecuación (4-75) podemos proporcionar una formulación muy simple para generar valores de variable aleatoria normalmente distribuidos, cuya media sea igual a $\mu_x$ y varianza $\sigma_x^2$. Para generar un solo valor de $x$ (un valor de variable aleatoria con distribución normal) bastará con sumar $K$ números aleatorios definidos en el intervalo de 0 a 1. Substituyendo el valor de esta suma en la ecuación (4-75), así como también los valores de $\mu_x$ y $\sigma_x$ para la distribución deseada, encontramos que se ha determinado un valor particular de $x$. Ciertamente, este procedimiento se puede repetir tantas veces como valores de variable aleatoria normalmente distribuidos se requieran.

El valor de $K$ que debe aplicarse a las fórmulas usualmente se determina al establecer las condiciones de balance entre la eficiencia de cómputo y la precisión. Al considerar la convergencia asintótica implicada por el procedimiento del límite central, es deseable que $K$ corresponda a un número muy grande. Considerando el tiempo que comprende la generación de $K$ valores uniformes por cada valor de variable aleatoria normal, sería preferible que $K$ estuviera asociada a un número muy chico. En la práctica de simulación se recomienda una $K = 10$, como el menor valor deseable. Sin embargo, con $K = 12$ se logra cierta ventaja computacional, ya que en la ecuación (4-75) se puede evitar una multiplicación constante. No obstante, este valor de $K$ trunca la distribución a los límites $\pm 6$, y además, se ha encontrado que no es confiable para valores de $x$ mayores que tres de las desviaciones estándar, aunque pese a lo anterior, la experiencia muestra que este criterio conduce a programas de razonable rapidez [21, p. 381]. Con el fin de obtener mayor precisión se deben considerar valores mayores para $K$ (del orden de $K = 24$), de acuerdo con la llamada técnica de aproximación de Teichroew [27], aunque en estos casos la eficiencia del procedimiento del límite central resulta significativamente menor a la de otros criterios.

> [FIGURA 4-15, pág. 15]: Diagrama de flujo vertical con los bloques encadenados de arriba a abajo:
> (óvalo) PROGRAMA PRINCIPAL → (rectángulo) CALL NORMAL (EX, STDX, X) → (rectángulo) SUBROUTINE NORMAL (EX, STDX, X) → (rectángulo) SUM = 0.0 → (rectángulo) DO I = 1, 12 → (rectángulo) GENERAR R → (rectángulo) SUM = SUM + R, con flecha punteada de retorno que sube hasta el bloque DO cerrando el ciclo de 12 iteraciones → (rectángulo) X = STDX * (SUM − 6.0) + EX → (rectángulo) RETURN → (óvalo) PROGRAMA PRINCIPAL.

**Figura 4-15. Diagrama de flujo para la generación de valores de variable aleatoria con distribución normal.**

**DISTRIBUCIONES CONTINUAS DE PROBABILIDAD  113**

La aproximación de Teichroew mejora la precisión de las probabilidades de los eventos extremos, obtenidas con el procedimiento del límite central. Con $K = 12$ deberemos calcular el valor de

$$y = \frac{\left(\sum_{i=1}^{12} r_i - 6\right)}{4}, \tag{4-76}$$

y el siguiente polinomio servirá para obtener el valor de la variable aleatoria $z$ distribuida normalmente:

$$z = a_1 y + a_3 y^3 + a_5 y^5 + a_7 y^7 + a_9 y^9, \tag{4-77}$$

donde

$$a_1 = 3.949846138$$
$$a_3 = 0.252408784$$
$$a_5 = 0.076542912$$
$$a_7 = 0.008355968$$
$$a_9 = 0.029899776$$

Pese a que el método de aproximación de Teichroew se puede programar fácilmente en FORTRAN, nuestro diagrama de flujo (figura 4-15) y subrutina FORTRAN (figura 4-16) para generar valores de variable aleatoria con distribución normal, con un valor dado tanto para el valor esperado como para la varianza, sigue el criterio del límite central. En la subrutina se utiliza la siguiente notación

$$EX = \mu_x \tag{4-78}$$

$$STDX = \sigma_x \tag{4-79}$$

$$SUM = \Sigma R. \tag{4-80}$$

Ahora incluiremos un breve resumen de otros dos procedimientos para generar valores de variables aleatorias distribuidas normalmente.

---

> **Fin de la transcripción (páginas 1 a 15 del PDF).** La figura 4-16 (subrutina FORTRAN NORMAL) se menciona en la p. 113 pero aparece recién en la página siguiente del libro, fuera del rango transcripto.
