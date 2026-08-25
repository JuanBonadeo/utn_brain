Prácticas de LABORATORIO
1
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

PROGRAMA PRÁCTICO
SESIÓN 0.- CONCEPTOS BÁSICOS DE ESTADÍSTICA
1.- Conceptos y Terminología
2.- Aplicaciones Prácticas de Modelos Estadísticos
3.- Distribuciones Discretas
4.- Distribuciones Continuas
SESIÓN 1.- INTRODUCCIÓN AL SW DE SIMULACIÓN ARENA
1.- Descripción Arena
2.- Primer Ejemplo
3.- Estudio de Módulos
4.- EJERCICIO - Proceso de Solicitud de una Hipoteca
SESIÓN 2.- CONSTRUCCIÓN DE MODELOS CON ARENA STANDARD
1.- Mejoras en la Visualización de la Simulación del Modelo
2.- Modificaciones en el Proceso de Solicitudes de una Hipoteca
3.- Modelos Jerárquicos: submodelos
4.- EJERCICIO - Proceso de Solicitud de Préstamo para Automóviles
SESIÓN 3.- MODELOS ESTADÍSTICOS EN SIMULACIÓN
1.- Herramienta Input Analyzer
2.- Datos a Analizar
3.- Datos y Ventanas
4.- Generación de Datos
5.- Ajuste de los Datos a una Distribución
6.- Modificación de Parámetros
7.- Ejercicios
SESIONES 4 y 5.- SIMULACIÓN de SISTEMAS de COLAS
1.- Introducción
2.- Teoría de Colas y Arena
3.- Ejercicios
SESIÓN 6.- ANÁLISIS DE DATOS DE ENTRADA
1.- Introducción
2.- Ejercicios
3.- Apéndice: Distribuciones
2
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

3
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 0.- Conceptos Básicos de Estadística
SESIÓN 0.- CONCEPTOS BÁSICOS DE ESTADÍSTICA
Objetivo: Introducir y repasar los conceptos básicos de estadística utilizados en las sesiones
prácticas de la asignatura Modelado y Simulación II. Los modelos probabilísticos utilizados
en el modelado y simulación de sistemas de eventos discretos requieren el conocimiento de
los términos y conceptos elementales de la estadística básica.
Índice:
1.- Conceptos y Terminología
Variable Aleatoria Discreta, Variable Aleatoria Continua, Función de
Distribución Acumulativa, Valor Esperado, Moda.
2.- Aplicaciones Prácticas de Modelos Estadísticos
Sistemas de Colas, Sistemas Inventario, Mantenimiento y Fiabilidad, Datos
Limitados o Incompletos, Otras Distribuciones.
3.- Distribuciones Discretas
Bernoulli, Binomial, Geométrica y Poisson.
4.- Distribuciones Continuas
Uniforme, Exponencial, Gamma, Erlang, Normal, Weibull y Triangular
1.- CONCEPTOS Y TERMINOLOGÍA
1.1.- Variable Aleatoria Discreta.-
• El número de posibles valores de la variable es finito o infinito pero contable.
• Para cada posible valor xi de la variable X se tiene que p(xi) = p(X = xi) es la
probabilidad de que la variable X tome el valor xi.
• Se cumplen las siguientes condiciones:
a) p(xi) ≥ 0 Para todo xi
∞
b) ∑p(xi)=1
i=1
• Distribución de Probabilidad o Función Masa de Probabilidad (pmf) de X es el
conjunto de pares (xi,p(xi)) con i=1, 2 ...
• Ejemplo Lanzamiento del dado trucado
1.2.- Variable Aleatoria Continua.-
1
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 0.- Conceptos Básicos de Estadística

•  El espacio de valores de la variable X (Rx) es un intervalo o un conjunto
de intervalos.

•  La probabilidad de que el valor de X se encuentre en un intervalo [a,b] viene
dada por la expresión:
b
|     |     |     | P(a ≤ x ≤b)= | ∫ f(x)dx |
| --- | --- | --- | ------------ | -------- |
|     |     |     |              | a        |
f(x) se llama función densidad de probabilidad (pdf) de la variable X

•  pdf satisface las siguientes condiciones:

a)  f(x) ≥ 0 Para todo x

|     |     | ∫ f(x)dx | =1  |     |
| --- | --- | -------- | --- | --- |
b)
|     |     | Rx  |     |     |
| --- | --- | --- | --- | --- |
x∉ Rx
c)  f(x) = 0 Si

|     | •  Ejemplo  Funcionamiento de una bombilla  |     |     |     |
| --- | ------------------------------------------- | --- | --- | --- |

1.3.- Función de Distribución Acumulativa.-

•  La función de distribución acumulativa (cdf), denotada por F(x), mide la
probabilidad de que la variable X tenga un valor menor o igual que x; es decir F(x)
= P (X ≤ x).

|     |                       |     | F(x) = ∑ | p(xi) |
| --- | --------------------- | --- | -------- | ----- |
|     | •  Si X  es discreta  |     |          |       |
xi≤x

x
Si X es continua
|     |     |     | F(x)= ∫ f(t)dt |     |
| --- | --- | --- | -------------- | --- |

−∞

|     | •  Propiedades de F(x):  |     |     |     |
| --- | ------------------------ | --- | --- | --- |

a)      F es una función no decreciente. Si a < b entonces F(a) ≤ F(b)
|     |   b)  limF(x)                        | =1      |     |     |
| --- | ------------------------------------ | ------- | --- | --- |
|     | x→∞                                  |         |     |     |
|     |   c)  lim                            | F(x) =0 |     |     |
|     | x→−∞                                 |         |     |     |
|     | •  Ejemplos Dado Trucado – Bombilla  |         |     |     |

1.4.- Valor Esperado.-

•  E(x) se denomina media y se define del siguiente modo:

∞
|     | Si X es continua    | E(X)= ∫xf(x)dx |     |     |
| --- | ------------------- | -------------- | --- | --- |
|     |                     | −∞             |     |     |
|     | Si X es discreta    | E(X)= ∑xip(xi) |     |     |
|     |                     | todoi          |     |     |
•  La media es una medida de la tendencia central de la variable aleatoria
  2
Xabier Basogain / Miguel Ángel Olabe             Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 0.- Conceptos Básicos de Estadística
1.5.- Varianza.-
• V(X) ó σ2 se denomina varianza y se define como:
V(X) = E [(X - E(X))2] equivalentemente V(X) = E(X2) - [E(X)]2
• La varianza de X mide la variación de los valores de x respecto de la media
• La desviación estándar σ se define como la raíz cuadrada de la varianza de X
1.6.- Moda.-
• Se define de la siguiente forma:
Variable Discreta: La moda es el valor de la variable que aparece más frecuentemente.
Variable Continua: La moda es el valor máximo de pdf
• La Moda puede no ser única.
• Si el valor de la moda ocurre en dos valores la distribución es bimodal
2.- APLICACIONES PRÁCTICAS DE MODELOS ESTADÍSTICOS
2.1.- Sistemas de Colas.-
• La distribución del tiempo entre llegadas y la distribución del número de llegadas por
periodo de tiempo son importantes a la hora de simular los sistemas de colas.
• El tiempo de servicio puede ser constante o probabilístico.
• Distribuciones utilizadas:
Exponencial. Si los tiempos de servicio son completamente aleatorios.
Normal. Si los tiempos de servicio son constantes pero existe una variabilidad que
produce fluctuaciones positivas y negativas.
Normal Truncada. Si existen valores de la variable que deben ser mayores o
menores que un cierto valor y el resto siguen una distribución normal.
Gamma y Weibull. Se utilizan para modelar Tiempos de Servicio.
3
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 0.- Conceptos Básicos de Estadística
2.2.- Sistemas Inventario.-
• Existen tres variables aleatorias:
a) Número de items solicitados en cada pedido o en cada periodo de
tiempo
b) Tiempo entre pedidos
c) Tiempo entre realizar un pedido y recibir dicho pedido
• La variable número de items o tamaño del pedido suele ser representada por
las siguientes distribuciones:
Geométrica. Se caracteriza por tener la moda centrada en la unidad
Binomial Negativa. Se caracteriza por tener una cola larga
Poisson. Está tabulada y se conoce con profundidad. Tiene una cola
más corta que la binomial negativa
2.3.- Mantenimientos y Fiabilidad.-
• El tiempo de fallo puede ser modelado por varias funciones:
Distribución Exponencial. Si solamente ocurren fallos aleatorios
Distribución Gamma. Surge del modelado por redundancia.
Distribución Weibull. Cuando hay muchos componentes en un sistema
y el fallo se debe al defecto más serio del conjunto de defectos
Distribución Normal. Cuando los fallos se deben al desgaste normal
Distribución Logonormal. Se utiliza para describir el tiempo de fallo de
algún tipo de componentes
2.4.- Datos Limitados o Incompletos.-
• No se dispone del suficiente número de datos
• Las funciones que se utilizan son:
Distribución uniforme. Se utiliza cuando se sabe que el tiempo entre llagadas o
de servicio es aleatorio pero no se dispone de más información
Distribución Triangular. Se puede utilizar cuando se hacen suposiciones sobre
el máximo, el mínimo y la moda
Distribución Beta. Proporciona una gran variedad de formas en su distribución
4
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 0.- Conceptos Básicos de Estadística
3.- DISTRIBUCIONES DISCRETAS
3.1.- Distribución de Bernoulli
Es una distribución de probabilidad con dos puntos de probabilidad discreta
definida como:
p(0) = q
p(1) = p siendo p+q = 1 con p,q >0
Sea un experimento consistente en n ensayos y cada uno de ellos puede tener
éxito o fracaso (1 ó 0). Sea por ejemplo xj=1 éxito y xj=0 fracaso.
Se tiene:
p(x1, x2 ... xn) = p1(x1). p2(x2) ... pn(xn)
⎧ p xj = 1 j = 1, 2 ... n
⎪
p j ( x j ) = p ( x j ) = ⎨ 1 − p = q xj = 0 j = 1, 2 ... n
⎪
⎩ 0 otros
3.2.- Distribución Binomial
La variable X indica el número de éxitos en n ensayos de Bernoulli y tiene una
distribución binomial dada por:
⎧⎛n⎞
⎪⎜ ⎜ ⎟ ⎟pxq n − x x = 0, 1, 2 ... n
p(x)=⎨⎝x⎠
⎪
⎩ 0 resto
La media y la varianza son:
E (x) = np V(x) = npq
3.3.- Distribución Geométrica (Relacionada con la secuencia de ensayos de Bernoulli)
La variable X indica el número de ensayos para obtener el primer éxito. La
distribución de esta variable es:
⎧qx−1p
x = 1, 2 ...
p(x) = ⎨
⎩ 0 otros
El evento {X = x} ocurre cuando hay x-1 fallos seguidos de un éxito
Cada uno de los fallos tiene asignada una probabilidad de q=1-p y cada uno de
los éxitos tiene probabilidad p. Así:
p(FFF....FS) = qx-1.p
La Media y la Varianza vienen dados por:
E(x) =
1
V(x ) =
q 5
Xabier Basogain / Miguel Ángel Olapbe Modelado
p
2y Simulación de Sistemas de Eventos Discretos

Sesión 0.- Conceptos Básicos de Estadística
3.4.- Distribución de Poisson
Se utiliza para modelar tiempos entre eventos aleatorios ocurridos en un
intervalo de tiempo fijo.
La función masa de probabilidad (pmf) está dada por:
x = 0, 1 ...
⎧e−ααx
⎪ otros con α > 0
p(x)=⎨ x!
⎪
⎩0
Una propiedad importante de la distribución de Poisson es E(x) = V(x) = α
La función de distribución acumulativa es:
x e−ααi
F(x)=∑
i!
i=0
Esta función está tabulada
Ejemplo: Servicio de Fontanería
4.- DISTRIBUCIONES CONTINUAS
4.1.- Distribución Uniforme
Se utiliza cuando todos los valores en un rango finito se pueden considerar
iguales
La variable aleatoria X está uniformemente distribuida en el intervalo (a,b) si
pdf está dada por:
a ≤ x <b
⎧ 1
⎪
f(x)= ⎨b−a
⎪ ⎩0 otros
cdf está dada por:
⎧0 x < a
⎪
⎪ x − a a ≤ x < b
F (x) = ⎨
b − a
⎪
⎪1 x ≥ b
⎩
Se tiene que p(x1 < x < x2) = F(x2)-F(x1x)2=− x 1 es proporcional a la
b−a
longitud del intervalo para todo x1 y x2 que satisfaga a ≤ x1 < x2 ≤ b
La media y la Varianza son:
a+b (b−a)2
E(X)= V(X)=
2 12
6
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 0.- Conceptos Básicos de Estadística

4.2.- Distribución Exponencial

Se utiliza para modelar tiempos entre llegadas y también tiempos entre servicios

Una variable aleatoria X se dice que tiene distribución exponencial con parámetro   λ
> 0 si su pdf está dada por:

|     | ⎧λe−λx |     |     | ⎧1−e−λx |     |
| --- | ------ | --- | --- | ------- | --- |
    f(x) =     x ≥ 0       ⇒                               x ≥ 0  F(x) =
|     | ⎨   |     |     | ⎨   |     |
| --- | --- | --- | --- | --- | --- |
     ⎩0   resto                                       0             resto
⎩
|     |     |     |     |       |     |
| --- | --- | --- | --- | ----- | --- |
|     |     |     |     |       |     |
1
1
|   La media y la Varianza son: E(x)= |     |     | V(x) | =   |     |
| ----------------------------------- | --- | --- | ---- | --- | --- |
λ2
|     |     |     | λ   |     |     |
| --- | --- | --- | --- | --- | --- |

4.3.- Distribución Gamma

Se utiliza para representar el tiempo requerido para finalizar una tarea
Una variable aleatoria X tiene una distribución Gamma con parámetros β y θ si
pdf es:
βθ
|     |               | ⎧    |     | x > 0  |     |
| --- | ------------- | ---- | --- | ------ | --- |
⎪ (βθx)β−1e−βθx
|     |   f(x) | = ⎨Γ(β) |     |          |     |
| --- | ------ | ------- | --- | -------- | --- |
|     |        | ⎪       |     | otros    |     |
0
⎩

donde β es un parámetro de forma y θ es un parámetro de escala y
además:
|     |   ∞                  |     |                |               |     |
| --- | -------------------- | --- | -------------- | ------------- | --- |
|     |  Γ(β) =  ∫xβ−1e −xdx |     |                | Γ(β) = (β−1)! |     |
|     |                      |     | para β entero  |               |     |

0
|     |                                      |     |     | 1     | 1   |
| --- | ------------------------------------ | --- | --- | ----- | --- |
|     |   La Media y la Varianza son:  E(x)= |     |     | V(x)= |     |
|     |                                      |     |     | θ     | βθ2 |

Cuando β es entero, la distribución Gamma está relacionada con la
Exponencial

Para β = 1 se obtiene una distribución Exponencial

4.4.- Distribución Erlang

La expresión pdf de Gamma, para  β = K, con K entero se denomina
distribución de Erlang de orden K

|     | La Media y la Varianza son:  |     | 1      | 1     |     |
| --- | ---------------------------- | --- | ------ | ----- | --- |
|     |                              |     | E(x) = | V(x)= |     |
|     |                              |     | θ      | Kθ2   |     |

Se verifica que:
  7
Xabier Basogain / Miguel Ángel Olabe             Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 0.- Conceptos Básicos de Estadística

|        |                  |        |     |     |         |     |     |     |     |
| ------ | ---------------- | ------ | --- | --- | ------- | --- | --- | --- | --- |
|        | ⎧ k−1e−kθx(Kθx)i |        |     |     |         |     |     |     |     |
|        | ⎪1−  ∑           |        |     |     |  x > 0  |     |     |     |     |
| F(x )= | ⎨                |  i!    |     |     |         |     |     |     |     |
i=0
⎪
|     |   ⎩0   |     |     |     | x ≤ 0  |     |     |     |     |
| --- | ------ | --- | --- | --- | ------ | --- | --- | --- | --- |

4.5.- Distribución Normal

Una variable aleatoria X con media μ (- ∝ < μ < ∝ ) y varianza σ2 tiene
una distribución normal si pdf es:

|     |     |     |       |     | ⎡     | 2⎤     |     |     |              |
| --- | --- | --- | ----- | --- | ----- | ------ | --- | --- | ------------ |
|     |     |     |       |     | 1     | 1⎛x−μ⎞ |     |     |              |
|     |     |     | f(x)= |     | exp⎢− | ⎜ ⎟ ⎥  |     | -   | ∝ < x < ∝    |
|     |     |     |       |     |       | 2⎝ σ   |     |     |              |
|     |     |     |       | σ   | 2Π ⎢⎣ | ⎠ ⎥⎦   |     |     |              |

Se utiliza la notación N(μ, σ)

La cdf de la Distribución Normal es:
|     |       |       |       |     |          |     |     |     |     |
| --- | ----- | ----- | ----- | --- | -------- | --- | --- | --- | --- |
|     |       |       | x     | 1   | ⎡ 1⎛t−μ⎞ | 2⎤  |     |     |     |
|     | F(x)= | p(X ≤ | x)= ∫ |     | exp⎢−    | ⎥dt |     |     |     |
|     |       |       |       |     | ⎜        | ⎟   |     |     |     |
|     |       |       | σ     | 2Π  | 2⎝       | σ ⎠ |     |     |     |
|     |       |       | −∞    |     | ⎢⎣       | ⎥⎦  |     |     |     |

La función acumulativa cdf está tabulada y es:
|     |     |     |      |     | z   | t2     |     |     |     |
| --- | --- | --- | ---- | --- | --- | ------ | --- | --- | --- |
|     |     |     |      |     | 1   | −      |     |     |     |
|     |     |     | φ(z) | =   | ∫   | e 2 dt |     |     |     |
2Π
−∞

4.6.- Distribución Weibull

Se utiliza en modelos de fiabilidad para representar tiempos de vida de
dispositivos. Un sistema formado por muchas partes independientes y el
sistema falla cuando hay un fallo.
Una variable aleatoria tiene una distribución Weibull si pdf es

|     |     |     | ⎧β ⎛x−ν⎞ | β−  | 1 ⎡      | β⎤    |        |     |     |
| --- | --- | --- | -------- | --- | -------- | ----- | ------ | --- | --- |
|     |     |     |          |     |   ⎛ x−ν⎞ |       | x ≥ ν  |     |     |
|     |     |     | ⎪ ⎜      | ⎟   | exp⎢−⎜   | ⎟ ⎥   |        |     |     |
|     |     | f(  | x)=⎨α ⎝  | α   | ⎝ α      |       |        |     |     |
|     |     |     |          | ⎠   |   ⎢⎣     | ⎠ ⎥⎦  |        |     |     |
⎪
|     |     |     | ⎩0   |     |     |     | otros  |     |     |
| --- | --- | --- | ---- | --- | --- | --- | ------ | --- | --- |
|     |     |     |      |     |     |     |        |     |     |

Los tres parámetros de una distribución Weibull son ν (-∝ < ν < ∝) que
es el parámetro de localización; α (α > 0) que es el parámetro de escala y
β (β>0) que es el parámetro de forma. Para ν = 0 se tiene que la pdf es:

|     |          |           | ⎧β ⎛ x ⎞  β−1 | ⎡    | ⎛ x ⎞ β ⎤  |        |     |     |     |
| --- | -------- | --------- | ------------- | ---- | ---------- | ------ | --- | --- | --- |
|     |          |  ⎪        | ⎜ ⎟           | exp⎢ | −  ⎜ ⎟ ⎥   | x ≥ 0  |     |     |     |
|     |     f(x) | =  ⎨α⎝α⎠  |               | ⎢⎣   | ⎝α⎠ ⎥⎦     |        |     |     |     |
⎪
|     |     |     | ⎩0  |     |     | otros  |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |

|     |     |     |     |     |     |     |     |     | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Xabier Basogain / Miguel Ángel Olabe             Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 0.- Conceptos Básicos de Estadística

|     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4.7.- Distribución Triangular

Se utiliza cuando no se conoce la forma exacta de la distribución pero se
estima el mínimo, el máximo y la moda
Una variable aleatoria X tiene distribución Triangular  si pdf es:

|     |     |     |     | ⎧   | 2(x−a) |     |                |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | -------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |        |     |     a ≤ x ≤ b  |     |     |     |     |     |
⎪(b−a)(c−a)
|     |     |     |     | ⎪   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2(c −x)
|     |     |     |     |  ⎪  |     |     |     b < x ≤ c  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
f(x) = ⎨
(c−b)(c−a)
|     |     |     |     | ⎪   |     |     |            |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
|     |     |     |     |  ⎪0 |     |     |     otros  |     |     |     |     |     |
⎪

⎩
|     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

La cdf de una distribución Triangular es:

 ⎧0
|     |     |     |     |     |     |     |     | x ≤ a  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
⎪
(x − a)2
|     |     |     |      |  ⎪  |      |     |     |            |     |     |     |     |
| --- | --- | --- | ---- | --- | ---- | --- | --- | ---------- | --- | --- | --- | --- |
|     |     |     |      | ⎪(b | a)(c | a)  |     |            |     |     |     |     |
|     |     |     |      | ⎪   | −    | −   |     | a < x ≤ b  |     |     |     |     |
|     |     |     | F(x) | = ⎨ |      |     |     |            |     |     |     |     |
|     |     |     |      |     | (c   | x)2 |     |            |     |     |     |     |
|     |     |     |      | ⎪   | −    |     |     |            |     |     |     |     |
1−
|     |     |     |     | ⎪   | (c − b)(c | − a) |     |            |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | ---- | --- | ---------- | --- | --- | --- | --- |
|     |     |     |     |     |           |      |     | b < x ≤ c  |     |     |     |     |
⎪
|     |     |     |     |  ⎪⎩1 |     |     |     | x > c  |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | ------ | --- | --- | --- | --- |

TABLA - RESUMEN
|            |     |              |     |     |       |     |     |       |     |       |     |     |
| ---------- | --- | ------------ | --- | --- | ----- | --- | --- | ----- | --- | ----- | --- | --- |
| Distribuci |     | f(x) ó p(x)  |     |     | F(x)  |     |     | E(x)  |     | V(x)  |     |     |
ón
|     |     |     |     |     |       |         |     |         |     |            |     |     |
| --- | --- | --- | --- | --- | ----- | ------- | --- | ------- | --- | ---------- | --- | --- |
|     |     |     |     |     |  F(x) | = ∑ p(x | )   | E(X)=∑x | p(x | )          |     |     |
|     |     |     |     |     |       |         |     |         | i   | i V(X) =   |     |     |
|     |     |     |     |     |       |         | i   |         | ∀i  |            |     |     |
|     |     |     |     |     |       | x≤x     |     |         |     | E(X2)      |     | -   |
i
|     |     |     |     |     |     | x   |     |     |     | [E(X)]2  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
∞
|     |     |     |     |     | F(x)= | ∫ f(t)dt |     |       |          |     |     |     |
| --- | --- | --- | --- | --- | ----- | -------- | --- | ----- | -------- | --- | --- | --- |
|     |     |     |     |     |       |          |     | E(X)= | ∫xf(x)dx |     |     |     |
−∞
|          |     |      |      |     |     | −∞  |     |           |     |           |     |     |
| -------- | --- | ---- | ---- | --- | --- | --- | --- | --------- | --- | --------- | --- | --- |
| Poisson  |     |      |      |     |     |     |     |           |     |           |     |     |
|          |     |   ⎧e | −α x |     |     |     |     | E(x) = α  |     | V(x) = α  |     |     |
α
|     |     |  p(x)=⎪⎪ |   x=0,1,2 |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
⎨ x!
⎪ 0          resto
|     |     |   ⎪⎩ |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |     |     | 9   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Xabier Basogain / Miguel Ángel Olabe             Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 0.- Conceptos Básicos de Estadística

| E x ponenc |         |             |                 |     |       | ⎧1 −e−λx |     |       | 1   |      |     |
| ---------- | ------- | ----------- | --------------- | --- | ----- | -------- | --- | ----- | --- | ---- | --- |
|            |         | ⎧λ − λ      | x               |     |       |          |     |       |     |      |     |
|            |         | ⎪ e         |     x ≥ 0       |     | F(x)= | ⎨        |     | E(x)= |     |      | 1   |
| ia l       |   f(x)= | ⎨           |                 |     |       |          |     |       |     | V(x) | =   |
|            |         | ⎪⎩ 0        |         r es to |     |       | ⎩ 0      |     |       | λ   |      |     |
λ 2

| Erlang-k  |            |                 |     |        |       |                |     |      |     |      |     |
| --------- | ---------- | --------------- | --- | ------ | ----- | -------------- | --- | ---- | --- | ---- | --- |
|           |            | ⎧ βθ            |     |        | ⎧     | k−1e−kθx(Kθx)i |     |      |     |      |     |
|           |            | ⎪ (βθx)β−1e−βθx |     |        | ⎪ 1−∑ |                |     |      |     |      | 1   |
|           | f(x)=⎨Γ(β) |                 |     | F(x)=⎨ |       |                | i!  |      |     |      |     |
|           |            |                 |     |        |       | i=0            |     |      | 1   | V(x) | =   |
|           |            | ⎪               | 0   |        | ⎪     |                |     | E(x) | =   |      |     |
|           |            | ⎩               |     |        | ⎩0    |                |     |      |     |      | Kθ2 |
θ

| Weibull  |     | ⎧β⎛x⎞β−1 | ⎡ ⎛x⎞β⎤ |     |     |     |     |     |     |     |     |
| -------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
⎧0
|     |        | ⎪ ⎜ ⎟ | exp⎢−⎜ | ⎟ ⎥   | ⎪        |         |      |     |     |     |     |
| --- | ------ | ----- | ------ | ----- | -------- | ------- | ---- | --- | --- | --- | --- |
|     |  f(x)= | ⎨α⎝α⎠ | ⎢⎣ ⎝α⎠ | ⎥⎦    |          |         | β⎤   |     |     |     |     |
|     |        | ⎪     |        | F(x)= | ⎨        | ⎡ ⎛x−ν⎞ |      |     |     |     |     |
|     |        | ⎩0    |        |       | 1−exp⎢−⎜ |         | ⎟ ⎥  |     |     |     |     |
|     |        |       |        |       | ⎪        |         | α    |     |     |     |     |
|     |        |       |        |       | ⎩        | ⎢⎣ ⎝    | ⎠ ⎥⎦ |     |     |     |     |

|     |     |     |     |     |     |     |     |     |     |     | 10  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Xabier Basogain / Miguel Ángel Olabe             Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 1.- Introducción al Software de Simulación Arena Standard
SESIÓN 1.- INTRODUCCIÓN AL SW DE SIMULACIÓN ARENA
Objetivo: Familiarizarse con el software de simulación ARENA que permite modelar,
simular, visualizar y analizar Sistemas de Eventos Discretos (SED).
Índice:
1.- Descripción Arena
2.- Primer Ejemplo
3.- Estudio de Módulos
4.- EJERCICIO - Proceso de Solicitud de una Hipoteca
1.- DESCRIPCIÓN del Software ARENA
El software de simulación ARENA es una herramienta que permite construir el modelo
del sistema o proceso a estudiar de manera gráfica mediante la utilización de una serie
de módulos. Una vez realizado el 'organigrama' del sistema, se introducen los datos de
dichos módulos y se ejecuta la simulación.
La ventana principal del software ARENA presenta tres regiones o ventanas
correspondientes a:
- Barra de Proyectos
- Organigrama o Modelo
- Datos
Ventana de Modelo
Barra de Proyectos
Ventana de Datos
11
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 1.- Introducción al Software de Simulación Arena Standard
La Barra de Proyectos (ventana vertical a la izquierda) presenta los diferentes paneles
de módulos que se pueden utilizar; en este curso se utilizarán los correspondientes al
Panel de Basic Process (en la Barra de Proyectos de la figura se ilustran los módulos
correspondientes al panel Basic Process). Los paneles Advanced Process y Advanced
Transfer suministran otros módulos orientados a la construcción de modelos de cierto
grado de complejidad.
Existen dos tipos de módulos en el Panel Basic Process:
- módulos de organigrama (iconos de color amarillo)
- módulos de datos (iconos rectangulares azul y blanco)
Los primeros se utilizan para construir el modelo, y para ello se arrastran de la Barra de
Proyectos a la ventana de Modelo, y se conectan de acuerdo al sistema que se desea
construir.
Los módulos de datos no se ubican en la ventana de Modelo, sino que se editan
mediante un mecanismo similar a las hojas de cálculo y se visualizan en la ventana
inferior a la ventana del Modelo, llamada Ventana de Datos. Estos módulos sirven para
definir las características de los diferentes módulos del proceso como son las colas y
recursos.
2.- PRIMER EJEMPLO
Comencemos por realizar un primer modelo sencillo siguiendo las fases siguientes:
a) construir un modelo
b) editar los módulos que constituyen el modelo
c) ejecutar la simulación y observar los informes de los resultados
- construcción de un modelo
Esta fase primera consiste en realizar el organigrama del modelo a partir de la
combinación de los diferentes módulos de organigrama. Todos ellos se deben ubicar en
la ventana de Modelo.
El primer ejemplo que se va a construir y simular está constituido por tres módulos
básicos como se indica en la figura:
Create Process Dispose
0 0
0
12
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 1.- Introducción al Software de Simulación Arena Standard
El módulo Create representa las llegadas de entidades a un proceso.
El módulo Process representa una actividad que supondrá la utilización de un recurso
durante un tiempo.
El módulo Dispose representa las salidas de las entidades del sistema
La forma de construir este organigrama es seleccionando cada uno de los módulos de la
Barra de Proyectos y arrastrándolos a la ventana de Modelo. La conexión entre ellos se
realiza a medida que añadimos un nuevo módulo al modelo.
- edición de los módulos
a) Módulos de Organigrama
Aun cuando el modelo correspondiente al organigrama construido podría ser simulado,
se debe editar cada uno de los módulos para asignarles valores adecuados al problema y
que serán en general diferentes a los que ARENA asigna por defecto a cada uno.
Además conviene nombrar los diferentes módulos con nombres relacionados con el
problema; en nuestro primer ejemplo se va a denominar el módulo Create como
'Entrada de Pedidos', el módulo Process como 'Papeleo' y al módulo Dispose como
'Envío de Pedidos'.
Para ello se hace doble-click en cada módulo del modelo y se abre una ventana de
edición de dicho módulo.
En nuestro primer ejemplo editar los módulos de la siguiente manera:
Create: cambiar en las opciones Name y Entity Type los valores 'Entrada de Pedidos' y
'Pedido' respectivamente (no teclear las comillas)
Process: cambiar en las opciones Name y Action los valores 'Papeleo' y
'SeizeDelayRelease' respectivamente. A continuación hacer simple-click en el boton
Add y poner 'Oficinista' en el campo Resource Name. Realizar dos veces click en OK
para cerrar las ventanas del menú.
Dispose: cambiar en la opción Name el valor 'Envio de Pedido'.
El organigrama editado presenta el siguiente aspecto:
Entrada de
Papeleo Envio de Pedido
Pedidos
0 0
0
13
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 1.- Introducción al Software de Simulación Arena Standard
b) Módulos de Datos
Además de editar los módulos de organigrama se debe editar los módulos de datos; en
nuestro ejemplo se seleccionará el módulo Resource en la Barra de Proyecto
correspondiente al recurso que se ha definido como 'Oficinista' y se editarán los valores
15, 15 y 2.5 para las casillas de los costes Busy/Hour, Idle/Hour y Per Use
respectivamente.
- ejecución de la simulación
Ya ha finalizado la fase de construcción del modelo y se puede realizar la simulación
del mismo. Antes conviene ajustar los parámetros de la simulación a los valores
adecuados al sistema que se va a estudiar.
Para ello se elige la opción del menú principal de ARENA, Run, Setup y se selecciona
la página Project Parameters. En esta ventana se cambia Project Title por uno
relacionado con nuestro primer ejemplo, p.e. Proceso de Entrada de Pedidos. También
se cambiará en la página Replications Parameters los valores de Replication Length y
Hours/Day por 40(horas) y 8 respectivamente.
La ejecución de la simulación será tan sencilla como seleccionar la opción Run, Go o
más sencillo pulsando el icono de Play de la barra de herramientas estándar.
A partir de este momento el diseñador observará en la ventana del Modelo los Pedidos
(entidades) moviéndose paso a paso por el sistema, y la animación tanto del proceso que
se está realizando como de los trabajos realizados como se ilustra en la figura.
Una vez finalizada la simulación, ARENA pregunta al diseñador si desea ver los
resultados obtenidos de la simulación. Los resultados obtenidos se organizan en una
serie de informes correspondientes al Proyecto en general, entidades, recursos, procesos,
colas, etc. como se ilustra en la figura:
14
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 1.- Introducción al Software de Simulación Arena Standard
Cada informe se muestra en una ventana independiente y una vez leídos los informes,
estas ventanas pueden ser minimizadas o cerradas utilizando los iconos estándar de
opciones de ventanas de windows:
Después de cerrar las ventanas de los informes y para volver al modo normal de diseño
y simulación del modelo, se debe salir del modo de ejecución (Run Mode) eligiendo la
opción Run/End o simplemente pulsando el icono de fin de simulación:
15
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 1.- Introducción al Software de Simulación Arena Standard
3.- ESTUDIO DE MÓDULOS
- TERMINOLOGÍA
Conviene describir una serie de términos que aparecen en el mundo de la simulación de
eventos discretos y relacionados con la simulación, ya que su conocimiento resulta útil a
la hora de comprender y analizar modelos de sistemas.
Entidad.- objeto de interés perteneciente al sistema; es el objeto sobre lo que actúa el
proceso(por ejemplo máquinas, mensajes, documentos, clientes, piezas, etc.)
Las entidades serán producidas y generalmente demandarán un servicio que será
realizado por un servidor que se describirá en términos de recurso.
Arena utiliza un lenguaje orientado a entidades. Las entidades representan personas,
objetos o cosas, bien sean reales o imaginarias, cuyo movimiento en el sistema provoca
cambios de estado del sistema.
Atributo.- propiedad de una entidad. En un sistema pueden existir muchos tipos de
entidades y cada una tendrá unas características propias llamadas Atributos.
Los atributos representan valores definidos por el usuario y asociados a cada una de las
entidades(p.e. tipo de cliente, tamaño del producto, instante en que un trabajo entra en el
sistema, etc.)
Todas las entidades tienen el mismo conjunto de atributos, pero con distintos valores.
Arena asigna un conjunto de atributos determinados (Entity.Type, Entity.Picture,
Entity.CreateTime, Entity.Station, Entity.Sequence, Entiy.JobStep)
Actividad.- representa un periodo de tiempo de duración específica.
Recurso.- elemento utilizado para modelar un área donde hay una limitación o
restricción; dichas restricciones pueden ser causadas por un número limitado de
personas para realizar una acción, espacio de almacenamiento restringido, capacidad de
los equipos, etc.
Se llama capacidad de un recurso al número de unidades de recurso idénticas
disponibles para dar un servicio.
Las entidades capturan (seize) recursos para tomar control de una o más unidades del
mismo, y una vez finalizado el servicio las entidades liberan (release) los recursos
utilizados.
Colas.- Área donde permanece una entidad mientras espera que un recurso está
disponible o mientras espera a formar un grupo(batch) con otras entidades.
Variables.- las variables representan un conjunto de valores globales que se pueden
modificar o utilizar sus valores como control en cualquier parte del modelo. Arena tiene
dos tipos de variables, las variables definidas por el Usuario y las variables definidas
por el Sistema
16
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 1.- Introducción al Software de Simulación Arena Standard
Las primeras son definidas por quien construye el modelo, y pueden cambiarse durante
la ejecución de la simulación(p.e. tasa de llegada, inventario actual, número de
pacientes, etc.)
Las variables del Sistema son características predefinidas de los componentes del
modelo que recogen el estado de los componentes(p.e. número de entidades esperando
en una cola; se denota con NQ(nombre de la cola), valor de un contador NC(nombre
del contador)).
MÓDULOS DE ORGANIGRAMA
A continuación se va a describir con cierto detalle los diferentes módulos accesibles en
el Basic Process panel. Los 8 módulos son los correspondientes a las siguientes formas:
- Create - Dispose
- Process - Decide
- Batch - Separate
- Assign -Record
CREATE.-
Este módulo se ha diseñado como punto de entrada de las entidades en el modelo de
simulación. Las entidades se crean en base a un tiempo entre llegadas o utilizando una
planificación determinada. Las entidades abandonan el módulo Create para empezar su
procesamiento a lo largo del sistema. El Tipo de entidad se especifica en este módulo.
La edición de este módulo (doble-click) presenta la siguiente ventana:
Create
0
El nombre es el único identificador del módulo y se visualiza dentro de la forma gráfica
del módulo; en el campo Entity Type se escribe el nombre del tipo de la entidad que se
va a generar.
El campo Type acepta los valores: Random(se utiliza una distribución exponencial y la
media la define el usuario), Schedule(se utiliza una distribución exponencial y la media
está determinada por un módulo Schedule), Constant (el usuario especifica el valor
constante) y Expression(se utilizará cualquier expresión que se presentará en el menú
que se desdobla en la opción Expression)
17
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 1.- Introducción al Software de Simulación Arena Standard
El campo Entities per Arrival indica el número de entidades que entrarán en el sistema
en cada uno de los instantes en que se produce una llegada(por defecto es 1)
DISPOSE.-
Este módulo tiene como función constituir el punto final de las entidades en el modelo
de simulación. Las estadísticas pueden ser registradas antes de que la entidad abandone
el sistema. La ventana de la edición de este módulo es la siguiente:
Dispose
0
PROCESS.-
Este módulo se ha diseñado como el principal método de procesamiento de las
entidades en la simulación. Dispone de las opciones 'capturar' y 'liberar' cualquier
recurso.
Además existe la opción de utilizar un 'submodelo' que permite al usuario definir de
forma jerárquica la lógica que desee con el número de módulos de organigrama que se
precise para el proyecto de simulación.
La ventana de edición de este módulo es la siguiente:
Process
0
18
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 1.- Introducción al Software de Simulación Arena Standard
El campo nombre tiene las misma funciones que las descritas en el módulo Create.
El Type permite describir el método de especificar la lógica que existe en el interior del
módulo. Procesamiento Standard significa que toda la lógica será almacenada dentro del
módulo Process y que será definida por una particular Action, mientras que Submodel
indica que la lógica será definida jerárquicamente en un submodelo.
Los posibles tipos de procesamiento dentro del módulo son los siguientes (campo
Action)
- Delay: se producirá un retraso pero no se utilizará ningún recurso o limitación.
- Seize Delay: uno o varios recursos se utilizarán en el módulo Process y también se
producirá un retraso, y la liberación del recurso se producirá más tarde.
- Seize Delay Release: se utilizará un recurso seguido de un retraso y entonces se
liberará el recurso utilizado.
- Delay Release: indica que un recurso que ha sido previamente utilizado será liberado
una vez transcurra un determinado retraso.
En los casos necesarios se debe indicar la lista de recursos que son utilizados en dicho
módulo y la cantidad de los mismos que serán capturados y liberados.
El campo Delay Type indica el tipo de distribución o método de especificar los
parámetros del retraso; las opciones Constant y Expression requieren un único valor,
mientras que Normal, Uniform y Triangular requieren varios parámetros.
DECIDE.-
Este módulo permite realizar procesos de decisión en el sistema de simulación; esto
incluye opciones de toma de decisiones basadas en una o más condiciones(p.e. si el tipo
de entidad es Tarjeta Oro) o basado en una o varias probabilidades(p.e. 75% verdadero;
25% falso). Las condiciones se pueden basar en los valores de los atributos, valores de
las variables, tipo de entidad o en una expresión(NQ(Cola del proceso Papeleo)).
La ventana de edición de este módulo es la siguiente:
0 Tr ue
Decide
0
False
19
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 1.- Introducción al Software de Simulación Arena Standard
BATCH.-
Este módulo constituye un mecanismo para el agrupamiento de entidades en el modelo
de simulación. Las agrupaciones pueden ser permanentes o temporales. Estas últimas
requerirán que se utilice un módulo Separate para separar las entidades agrupadas.
Los agrupamientos pueden realizarse basados en un número específico de entidades o
basados en un atributo determinado.
Las entidades que llegan a un módulo Batch se sitúan en una cola hasta que se acumulen
el número requerido de entidades. Una vez acumulados se creará una entidad
representativa de dicho agrupamiento.
La ventana de edición de este módulo es la siguiente:
Batch
0
SEPARATE.-
Este módulo se utiliza para copiar una entidad entrante en múltiples entidades o para
separar un entidad previamente agrupada mediante el módulo batch. En este segundo
caso, la entidad temporal representativa desaparece y se recuperan las entidades
originales que constituían el agrupamiento.
La ventana de edición es la siguiente, para el caso de realizar tres copias del original:
0
Separate
Original
0 Duplicate
20
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 1.- Introducción al Software de Simulación Arena Standard
ASSIGN.-
Este módulo se utiliza para asignar a las entidades que entren al módulo nuevos valores
a variables, atributos de entidades, tipos de entidades, dibujos de entidades y otras
variables del sistema. Se pueden realizar múltiples asignaciones en un único módulo
Assign.
Assign
RECORD.-
Este módulo se utiliza para recoger las estadísticas de la simulación del modelo. Los
tipos de estadísticas disponibles incluyen tiempo de salida del módulo, estadísticas de
las entidades(tiempo, coste, etc.), observaciones generales y estadísticas de intervalos de
tiempo.
Record
NOTA:
La información completa de todos los módulos descritos está disponible en el botón
Para cada uno de ellos existe información ordenada en los campos indicados en la figura
siguiente:
21
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 1.- Introducción al Software de Simulación Arena Standard
4.- EJERCICIO - Proceso de Solicitud de una Hipoteca
En el siguiente ejercicio que se propone se pretende que el alumno realice una primera
experiencia en la utilización del software ARENA para modelar, simular, visualizar y
analizar los resultados de un sencillo sistema a estudiar.
En una sucursal bancaria se desea estudiar y analizar el funcionamiento de un servicio
determinado relativo a las solicitudes de Préstamos Hipotecarios. En concreto se
pretende conocer las repuestas a las siguientes preguntas:
1) ¿Cuál es tiempo promedio para evaluar una Solicitud de una hipoteca?
2) ¿Cuál es el coste promedio de la revisión de una Solicitud de una hipoteca?
3) ¿Cuál es el máximo tiempo que duró la revisión de una Solicitud?
4) ¿Cuál es el máximo número de solicitudes que han estado esperando a ser revisadas?
5) ¿Qué proporción de tiempo ha estado ocupado el oficinista que realiza las
revisiones?
Para ello, el alumno debe construir un modelo del Proceso 'Revisión de una Solicitud de
Hipoteca' y obtener dichos resultados mediante la simulación con ARENA.
La información que se dispone del proceso a estudiar es la siguiente:
a) las Solicitudes (entidades) de una hipoteca se producen o llegan a la sucursal bancaria
de una manera aleatoria siguiendo una distribución exponencial de media 2 horas entre
llegadas de solicitudes.
b) el proceso de revisión y evaluación de una solicitud lo realiza un Oficinista (un
recurso o un servidor). Cada solicitud (entidad) que llega al Oficinista (proceso)
requiere dicho recurso durante un tiempo aleatorio que sigue una distribución triangular,
en la que el tiempo mínimo es una hora, el tiempo más probable es de 1.75 horas y
tiempo máximo es de 3 horas.
Cuando una entidad llega al proceso, ésta esperará su turno para capturar el recurso.
Una vez llegado su turno la entidad capturará (seize) el recurso, tendrá un tiempo de
retraso correspondiente al tiempo de servicio del Oficinista, y liberará (release) el
recurso para que éste pueda realizar otro servicio.
c) Una vez la solicitud ha sido revisada y evaluada, queda por decidir si se acepta o no
se acepta dicha solicitud. El criterio de aceptación de una solicitud se basará en un
simple criterio probabilístico, en concreto se aceptará el 88% de las solicitudes. NOTA:
se utilizarán dos módulos Dispose, una para las solicitudes aceptadas y el otro para las
solicitudes no aceptadas.
d) Los costes correspondientes al Oficinista se fijan en $12 por hora de trabajo,
independientemente de si ha estado ocupado o desocupado.
e) El estudio de simulación se desea realizar sobre el funcionamiento de la sucursal
bancaria durante 20 días y 24 horas al día, es decir sobre un total de 480 horas.
22
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 1.- Introducción al Software de Simulación Arena Standard
- CONSTRUCCIÓN DEL ORGANIGRAMA
Realizar en la ventana del Modelo el siguiente organigrama correspondiente al
problema de estudio:
Revisión de una Solicitud de Hipoteca
0
Inicio de Solicitud Concesion de
de Hipoteca Revision Hipoteca? True Solicitud Aceptada
0 0
0
0 False
Solicitud
Rechazada
0
- EDICIÓN DE LOS MÓDULOS
Una vez realizado el organigrama con los módulos necesarios se debe editar cada uno
de ellos para asignarles los parámetros correspondientes al problema de estudio.
Editar los siguientes módulos:
Módulos de organigrama.-
- Create: asignarle el nombre 'Inicio de Solicitud de Hipoteca', definir el tipo de entidad
como 'Solicitud' y elegir el adecuado tiempo entre llegadas (no poner tilde a las letras
acentuadas).
- Process: asignarle el nombre 'Revisión', elegir la Action adecuada y definir un Recurso
que tenga el nombre Oficinista. El tiempo de retraso del proceso es tipo triangular.
- Decide: asignarle el nombre 'Concesión de Hipoteca' y Percent True adecuado al
problema.
- Dispose: asignarles los nombres 'Solicitud Aceptada' y 'Solicitud Rechazada'.
Módulos de datos.-
- Resource: introducir los costes por hora ($12) en la hoja de cálculo correspondiente al
recurso 'Oficinista'.
- SIMULACIÓN
Antes de ejecutar la simulación conviene ajustar los parámetros de simulación al
problema de estudio.
23
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 1.- Introducción al Software de Simulación Arena Standard
Editar en primer lugar, el título del proyecto como 'Análisis de la Revisión de Solicitud
de Hipoteca' en el tabulador Poject Title de la carpeta Project Parameters del menú
Run,Setup. Además, se debe seleccionar en las cajas check de Statistic Colletion las
correspondientes a Entities, Qeues, Resources, Processes y Costing.
En el mismo menú Run,Setup, en la carpeta Replication Parameters seleccionar 20 en el
campo Replication Length y elegir días en Time Units.
Salvar el modelo realizado mediante la opción File/Save (o el pulsando el botón Save
de barra de herramientas estándar).
NOTA: Utilizar un subdirectorio específico para este y el resto de modelos que se
desarrollarán a lo largo del curso.
Simular el modelo.
NOTA: se puede variar y ajustar la velocidad de la animación de la simulación del
modelo; para ello durante la simulación basta mantener pulsada la tecla '<' o la tecla '>'
unos instantes para decrementar o aumentar la velocidad de la animación
respectivamente.
Si se desea realizar la simulación sin animación se debe elegir la opción Run/Fast-
Forward y simplemente pulsar su correspondiente icono Fast-Forward
en la barra de herramientas estándar.
- INFORMES de los RESULTADOS DE SIMULACIÓN
Ver y analizar los datos presentados en los diferentes informes que ha generado
ARENA al simular el modelo del Proceso de Solicitud de una Hipoteca.
Responder a las 5 preguntas realizadas al comienzo de este apartado 4 EJERCICIO, a
partir de los resultados de dichos informes.
Pregunta 1.- Informe Entity (Total Time Average)
Pregunta 2.- Informe Entity (Total Cost Average)
Pregunta 3.- Informe Process (Total Time Maximun)
Pregunta 4.- Informe Queue (Number Waiting Maximun)
Pregunta 5.- Informe Resource (Utilization Average)
24
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 2.- Construcción de Modelos con Arena Standard
SESIÓN 2.- CONSTRUCCIÓN DE MODELOS CON ARENA
STANDARD
Objetivo: Diseñar, construir y simular sistemas SED con mayor versatilidad mediante
herramientas adecuadas que provee el software de Simulación.
Índice:
1.- Mejoras en la Visualización de la Simulación del Modelo
2.- Modificaciones en el Proceso de Solicitudes de una Hipoteca
3.- Modelos Jerárquicos: submodelos
4.- EJERCICIO - Proceso de Solicitud de Préstamo para Automóviles
1.- MEJORAS EN LA VISUALIZACIÓN DE LA SIMULACIÓN DEL MODELO
La animación gráfica en la simulación del modelo que se quiere diseñar y simular vista
hasta ahora se limita a representar gráficamente sobre el modelo el movimiento de las
entidades a lo largo del organigrama. Sin embargo, Arena tiene la posibilidad de
incrementar la animación y así mejorar el estudio del comportamiento del sistema
modelado.
Además otra ventaja de las mejoras en la visualización animada del sistema es el interés
que puede generar en otros miembros de la empresa u organización, como los
directivos, gestores o administradores, por conocer las posibilidades que ofrece esta
nueva herramienta de modelado de sistemas de eventos discretos.
Para comprobar las ventajas que supone la mejora de la animación gráfica se añadirá
dos componentes de animación al Modelo de Solicitudes de Hipoteca estudiado en la
sesión anterior:
a) Oficinista , ocupado y desocupado
b) Representación dinámica del número de solicitudes en trámite
Incorporando estos dos nuevos componentes de animación al modelo, éste presentará el
aspecto que se indica en la siguiente figura:
Revisión de una Solicitud de Hipoteca
0
Inicio de Solicitud Concesion de
de Hipoteca Revision Hipoteca? True Solicitud Aceptada
0 0
0
0 False
Solicitud
Rechazada
0
Solicitudes en Trámite
Oficinista 10
se
d
c loi i
u
t
S
0
Tiempo de Simulación (días) 20
25
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 2.- Construcción de Modelos con Arena Standard
Nota: para este tipo de mejoras se utilizará los iconos correspondientes a la barra de
herramientas de Animación.
a) Animación del Recurso 'Oficinista'
La actividad que realiza el recurso Oficinista consiste en revisar y evaluar cada una de
las solicitudes que le llegan; si no llega ninguna solicitud el Oficinista está desocupado
y se utilizará un dibujo de una persona sentada en su puesto de trabajo (chaqueta de
color verde). Cuando llega una solicitud, ésta capturará el recurso y el recurso pasará a
estar ocupado representado por un dibujo de una persona trabajando sobre la mesa
(chaqueta de color rojo).
Los pasos que hay que realizar para establecer este tipo de animación son los siguientes:
1.- Clic el botón de Recurso de la barra de herramientas de animación.
2.- Se abre la ventana de Resource Picture Placement. Seleccionar 'Oficinista' en el
campo Identifier.
3.- Si Current Library no es c:\...\workers.plb , abrir la librería de dibujos adecuada
mediante el botón Open (seleccionar workers.plb).
4.- Para cambiar el icono de Oficinista Desocupado:
a) clic el botón de Idle de la parte izquierda (el campo State se actualizará a Idle)
b) Seleccionar el dibujo de una persona sentada con chaqueta verde.
c) click el botón de transferencia entre tablas
5.- Para cambiar el icono de Oficinista Ocupado:
a) repetir los mismos pasos que en el caso anterior, particularizando para el
estado Busy (dibujo de persona trabajando con chaqueta roja).
6.- Clic el botón Ok para cerrar la ventana de diálogo.
7.- El cursor se transformará en una cruz; moverlo al lugar del modelo donde se desee
que aparezca la animación del Oficinista.
8.- Si se desea redimensionar el icono del Oficinista, basta con seleccionarlo y alargar o
reducir el dibujo.
b) Representación Dinámica del Número de Solicitudes en Trámite
En algunos procesos resulta de gran interés visualizar de forma dinámica la evolución
de una serie de variables como puede ser el número de entidades en una cola, nivel de
ocupación de un recurso, etc. Este tipo de información ilustra la carga de trabajo del
sistema que puede variar bruscamente debido a la naturaleza aleatoria del proceso
simulado.
26
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 2.- Construcción de Modelos con Arena Standard
Los pasos que hay que realizar para establecer este tipo de animación son los siguientes:
1.- Clic el botón de Plot de la barra de herramientas de animación.
2.- Se abre la ventana de Plot. En caso presente se va a representar una única expresión,
la correspondiente a work-in-process (WIP) del proceso 'Revisión' de nuestro
modelo. Para ello se debe pulsar el botón Add.
3.- En la nueva ventana de dialogo de Plot Expression, pulsar el botón de editar
expresiones para abrir el editor de expresiones.
4.- Se desea representar a lo largo del tiempo el número de entidades (solicitudes) en el
proceso 'Revisión'. Seleccionar en el campo Process Name el nombre del
proceso (Revisión) y en el campo de Information elegir WIP (la última opción
que aparece en la lista que se despliega en este campo).
5.- Editar los valores Máximum y History Points con los valores 10 y 5000
respectivamente (en la sesión anterior se obtuvo que el número máximo de
entidades en cola era 9). Pulsar el botón OK para cerrar la ventana de dialogo de
Plot Expression (fijarse que Arena pone la fórmula Revision.WIP).
6.- Para completar la definición del Plot, cambiar Time Range al valor de 480. El eje
horizontal del plot representará 480 horas de simulación. Pulsar OK para cerrar
la ventana de diálogo de Plot.
7.- El cursor cambia a la forma de una cruz; dibujar el Plot en la ventana del modelo
mediante realizando clic en dos extremos en el lugar que se desee.
c) simulación del modelo con las mejoras de animación
Una vez editados los dos nuevos componentes de animación pasemos a simularlo;
previamente conviene salvar el modelo; también puede resultar interesante añadir algún
texto que documente con cierto detalle los dos nuevos componentes de animación.
Editar en el pie del icono del Oficinista, el texto Oficinista, y junto a los ejes del Plot, el
texto Tiempo de Simulación (días) para el eje de abcisas, el texto Solicitudes para el eje
de ordenadas y el texto Solicitudes en Trámite para un título superior del plot. Para la
edición de texto utilizar el icono Text de la barra estandar de dibujo .
Realizar la simulación del modelo y comprobar el efecto de la animación. El nuevo
modelo presenta una animación más interesante y medible. Los resultados numéricos
que se obtendrán serán los mismos que los obtenidos en la sesión anterior ya que no se
ha realizado ningún cambio en los parámetros del modelo.
27
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 2.- Construcción de Modelos con Arena Standard
Sin embargo, se observará a medida que avanza la simulación cómo el dibujo que
representa al Oficinista cambia entre los estados Desocupado y Ocupado según lleguen
solicitudes al proceso Revisión.
La representación dinámica del número de solicitudes en trámite muestra una serie de
picos importantes debido a la combinación del tiempo variable entre llegadas de
solicitudes (módulo Create) y el tiempo de proceso de las solicitudes (módulo Process).
2.- MODIFICACIONES EN EL PROCESO DE SOLICITUDES DE UNA
HIPOTECA
En este apartado se va a considerar dos modificaciones del Proceso de Solicitudes de
una Hipoteca estudiado en la anterior sesión con el propósito de mostrar diferentes
posibilidades del software Arena.
a) Primera Modificación: Añadir un proceso de Escáner
Para mejorar e informatizar el proceso de Solicitud de Hipoteca se ha decidido añadir
delante del proceso Revisión, un proceso llamado Escáner que lo realizará una
Secretaria.
El proceso Escáner tiene una duración mínima de 15 minutos, máxima de 45 minutos, y
una duración normal de 25 minutos.
Asignar un dibujo a la Secretaria y una tarifa de $6.75 hora.
Revisión de una Solicitud de Hipoteca Modificación 1
Inic d io e d H e i p S ot o e l c ic a itud Escaner Revision Concesion de Hipoteca?
0
Tr ue Solicitud Aceptada
0 0
0 0
0 False
Solicitud
Rechazada
0
Secretaria
Oficinista
Simular el nuevo sistema y contestar a las preguntas:
a1) ¿Qué proporción de tiempo estará ocupada la Secretaria, y el Oficinista?
a2) ¿Cuál es el coste promedio de cada Solicitud?
28
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 2.- Construcción de Modelos con Arena Standard
a3) ¿Cuál es el número máximo de solicitudes en espera en la cola del
Oficinista?
b) Segunda Modificación: Devolución de algunas Solicitudes después del proceso
Escáner
Una vez se ha completado la tarea de Escáner, el 8% de las solicitudes son devueltas por
estar incompletas. Este hecho significa que muchas de las solicitudes serán detectadas
en el proceso de Escáner y por consiguiente el porcentaje de solicitudes aceptadas
después del proceso Revisión se incrementa del 88% al 94%, y el tiempo de proceso de
Revisión se reduce un 10%.
Simular el nuevo sistema y contestar a las preguntas:
b1) ¿Qué proporción de tiempo estará ocupada la Secretaria, y el Oficinista?
b2) ¿Cuál es el coste promedio de cada Solicitud?
b3) ¿Cuál es el número máximo de solicitudes en espera en la cola del
Oficinista?
b4) ¿Cuál es el tiempo promedio para revisar una Solicitud?
Nota:
La reducción del 10% del tiempo de proceso Revisión se puede realizar mediante la
definición de una variable llamada 'Factor de Reducción' inicializada al valor 0.9 y
utilizada en los campos correspondientes a la distribución triangular del tiempo de
servicio del proceso Revisión como se indica en la figura siguiente:
Para la definición de la variable 'Factor de Reducción' se utiliza el módulo de datos
Variable de la Barra de Proyectos y se edita como se muestra en la figura
29
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 2.- Construcción de Modelos con Arena Standard
3.- MODELOS JERÁRQUICOS: SUBMODELOS
Arena ofrece la posibilidad de diseñar/construir el modelo de un sistema de una forma
jerarquizada, en vistas jerarquizadas llamadas Submodelos.
Submodelo.-
Los submodelos disponen de un espacio de trabajo completo para definir el
organigrama de flujo de las entidades, incluyendo los recursos de animación gráfica, de
la misma forma que cualquier modelo no jerarquizado.
Los submodelos pueden contener cualquier objeto que se pueda colocar en la ventana de
modelo (lógica, gráficos estadísticos, animación, etc.)
La utilización de los submodelos en el modelo del sistema ofrece las siguientes
ventajas:
a) aumento del espacio de trabajo para construir el modelo.
b) facilita una mejor organización del modelo (cada submodelo es representado en su
propia vista, es decir, en la ventana de modelo) permitiendo la división visual de un
organigrama complejo de un modelo en ventanas más fáciles de manipular y
comprender el modelo.
Los submodelos pueden conectarse a otros módulos, a otros submodelos, o simplemente
pueden estar solos en el modelo. Además existen una serie de comandos que permiten
realizar una serie de operaciones sobre los submodelos:
- Properties.- permite cambiar las características del submodelo, por ejemplo el número
de puntos de entrada y salida.
30
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 2.- Construcción de Modelos con Arena Standard
- Open.- abrir el submodelo para visualizar la vista del submodelo e introducir la lógica,
animación y gráficos.
- Aggregate.- sirve para agrupar en un submodelo la lógica, animación y gráficos que
exista ya en la ventana del modelo.
- Unaggregate.- saca los objetos de una vista de submodelo y los ubica en el siguiente
nivel superior del modelo.
Definición de submodelos.-
El modelo jerárquico de un sistema se puede realizar de dos maneras:
- Submodelo Process
- Objeto Submodelo
El primero de ellos se crea definiendo el campo Type de un módulo Process con la
opción Submodel, como se indica en la figura:
Esta capacidad del módulo Process es referida como jerarquización de procesos y
permite agregar varios módulos de organigrama de flujo en vistas de submodelo
diferentes, cada una de ellas asociadas al módulo Process correspondiente.
El segundo tipo de submodelo se obtiene mediante la selección de la opción de menú
Objetc/Submodel/Add Submodel o haciendo clic en el botón de Submodelo de la barra
31
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 2.- Construcción de Modelos con Arena Standard
de herramienta estándar . Este tipo de submodelo es simplemente una colección de
módulos que han sido agregados para navegación y facilidad de uso.
La principal diferencia entre los dos métodos son las estadísticas generadas. Cuando un
módulo que se define como tipo Submodelo y se construye una lógica en la vista de
submodelo, cualquier estadística, coste e información temporal que se recoge cuando
una entidad está dentro del submodelo será reflejada directamente en las estadísticas,
costes e información temporal de ese Proceso (independientemente del número de
niveles de jerarquía que se hayan definido).
Sin embargo, las estadísticas recogidas a partir de la lógica definida en el Objeto
Submodelo no son agregadas para ese submodelo en particular.
Navegación en el Modelo.-
Existen varias formas de acceder a las vistas de los submodelos. Un método es del Panel
Navigate de la Barra de Proyectos (hacer clic en el icono Navigate para que se visualice
el Panel Navigate).
Cuando se utiliza el Panel Navigate, Arena permite el acceso directo a cada una de las
vistas de los submodelos, simplemente haciendo clic en la lista de los nombres de los
submodelos. Esto significa que en el caso de varios submodelos anidados, se puede
acceder directamente a un submodelo que esté a varios niveles del nivel superior de la
jerarquía.
Otro método de acceso es realizar doble clic en el objeto submodelo presente en la
ventana de modelo; en este método el acceso a submodelos anidados requiere realizar
doble clic en los sucesivos objetos de los submodelos anidados.
El tercer método consiste en realizar clic-derecho (en el botón de la derecha del ratón)
sobre el objeto submodelo presente en la ventana de modelo y seleccionar del menú la
opción Open Submodel.
Vista de un Submodelo.-
Dentro del objeto submodelo está la vista de submodelo que contiene la lógica u
organigrama de flujo del submodelo. En la vista del submodelo hay puntos de entrada y
puntos de salida que están conectados a la lógica del submodelo. Estos puntos permiten
el paso de las entidades del nivel superior del modelo al submodelo, continua el
procesamiento de las entidades de acuerdo a la lógica del submodelo y se vuelve al
nivel superior para seguir su procesamiento, como se ilustra en la figura.
Create 1 Submodel 1 Dispose 1
0 0
Create 2 Process 3 Dispose 2
0 0
0
Dispose 3
32
0
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 2.- Construcción de Modelos con Arena Standard
El número de puntos de entrada y salida pueden elegirse mediante la opción Properties
del menú que aparece al realizar clic-derecho sobre el objeto submodelo.
Los puntos de entrada en la vista del submodelo se representa mediante una flecha que
apunta a la dirección que seguirá el flujo de la lógica. El punto de salida se representa
por un cuadrado. Desde este punto la entidad regresará a la vista del siguiente nivel para
continuar con el procesado. En la figura se muestra la vista de un submodelo particular,
con dos puntos de entrada y tres de salida.
Process 1
0
0
Separate 1
Orginial
0 Dupcilate
Process 2
0
4.- EJERCICIO - PROCESO DE SOLICITUD DE PRÉSTAMOS PARA
AUTOMÓVILES
Se desea realizar el estudio de un proceso correspondiente a la solicitud de préstamos
para la adquisición de automóviles que ofrece una entidad bancaria.
En este modelo, las solicitudes de préstamos para adquirir un automóvil llegan al centro
de procesamiento aproximadamente cada 5 minutos.
La revisión de la solicitud la realiza uno de los cinco agentes de préstamos que
comprueban si la solicitud está completa. Esta revisión suele durar 15 minutos, pero
puede durar como mínimo 12 minutos y como máximo 18 minutos. Los agentes
detectan que el 8% de las solicitudes están incompletas y las devuelven al solicitante.
Las solicitudes que están completas se envían a una máquina de procesamiento
automático donde las solicitudes son procesadas. Esta operación puede durar de 0.5
horas a 1.5 horas, pero habitualmente requiere 1 hora. Se supone que la máquina de
procesamiento automático puede procesar tantas solicitudes como sea necesario.
Una vez procesadas las solicitudes, un agente comprobará los resultados del
procesamiento y escribirá un documento de aceptación o rechazo. Esta tarea suele tener
una duración de 7 minutos, aunque nunca más de 10 minutos y ni menos de 5 minutos.
Una vez escrito dicho documento, el proceso de la solicitud del préstamo se ha
completado y se envía dicho documento a los solicitantes.
1) Realizar la simulación para un día considerando la jornada de 8 horas.
33
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 2.- Construcción de Modelos con Arena Standard
- Indicar los valores más relevantes de los resultados de la simulación (nº de solicitudes,
utilización de los recursos, nº medio de solicitudes en las diferentes colas, etc.)
4.1.- Submodelo en el Proceso de Solicitud de Préstamos para Automóviles
La Dirección de la entidad bancaria quiere un análisis más detallado del funcionamiento
del departamento de autorización de préstamos. Para ello, se sustituirá el proceso que
modelaba la máquina de 'procesamiento automático' por un proceso que sea definido
como Submodelo en el campo Type.
La actividad de autorización de préstamos realiza dos operaciones por separado:
- Evaluación de Legitimidad de la solicitud
- Comprobación de Crédito
a) Evaluación de Legitimidad de la solicitud.-
Una vez que el agente de préstamos hace la revisión inicial de la solicitud y está
completa, 1 de los 5 agentes de evaluación comprueba la legitimidad de la solicitud. El
95% de las solicitudes son legítimas. Cualquier solicitud que no sea legítima se salta la
Comprobación de Crédito, y continuará con un agente de préstamos disponible en el
proceso de generación de documento de aceptación o rechazo.
La operación de evaluación requiere entre 20 y 30 minutos.
b) Comprobación del Crédito.-
Las solicitudes legítimas serán estudiadas por uno de los 12 agentes de crédito que
realizan la revisión del crédito a partir de un informe sobre el crédito del solicitante.
Esta operación suele requerir aproximadamente una hora, con un mínimo de 55 minutos
y un máximo de 90 minutos.
Una vez finalizada la revisión, cada solicitud continuará con un agente de préstamos
disponible en el proceso de generación de documento de aceptación o rechazo.
2) Realizar la simulación para un día considerando la jornada de 8 horas.
- Indicar los valores más relevantes de los resultados de la simulación (nº de solicitudes,
utilización de los recursos, nº medio de solicitudes en las diferentes colas, etc.)
34
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 3.- Modelos Estadísticos en Simulación
SESIÓN 3.- MODELOS ESTADÍSTICOS EN SIMULACIÓN
Objetivo: Familiarizarse con las funciones de distribución de procesos aleatorios más
utilizados en la Simulación de SED.
Indice:
1.- Herramienta Input Analyzer
2.- Datos a Analizar
3.- Datos y Ventanas
4.- Generación de Datos
5.- Ajuste de los Datos a una Distribución
6.- Modificación de Parámetros
7.- Ejercicios
A la hora de modelar fenómenos reales son pocas las veces en las que el diseñador
puede predecir de una manera determinista las acciones que se van producir sobre las
entidades que están dentro de un sistema objeto de estudio.
El diseñador generalmente modela los sistemas desde un punto de vista probabilístico
más que desde un punto determinista ya que son muchas las causas que pueden producir
variaciones sobre el comportamiento global del sistema. Sin embargo, a pesar de la
aleatoriedad de las causas y la imposibilidad de predecirlas, existen modelos
estadísticos o funciones de distribución que permiten describir la aleatoriedad de las
causas que influyen en el comportamiento del sistema.
El conocimiento de los diferentes modelos estadísticos (distribuciones discretas y
continuas) permite al diseñador realizar un modelo más preciso del sistema. Así por
ejemplo, el tiempo de servicio de un servidor en un sistema de colas puede ser descrito
por las siguientes distribuciones:
- Exponencial: si los tiempos de servicio son completamente aleatorios.
- Normal: si los tiempos de servicio son constantes pero existe una variabilidad que
produce fluctuaciones negativas y positivas.
- Normal Truncada: si existen valores de la variable que deben ser mayores o menores
que un umbral y el resto sigue una distribución normal.
- Weibull y Gamma: ambas presentan aspectos similares y están relacionadas con la
distribución exponencial. Las diferencias estriban en la localización de la moda
de las funciones de distribución y en las formas de las colas para los extremos.
35
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 3.- Modelos Estadísticos en Simulación
1.- Herramienta INPUT ANALYZER
El Input Analyzer es un componente estándar del entorno de simulación de Arena. Es
una herramienta potente y versátil que se puede utilizar para las siguientes actividades:
a) determinar la calidad de ajuste de una función distribución de probabilidad a un
conjunto de datos de entrada.
b) comparar diferentes funciones de distribución de probabilidad
c) representar gráficamente los efectos de la variación de los parámetros para una
misma distribución.
d) generar datos aleatorios siguiendo una determinada función de distribución de
probabilidad.
En esta sesión se va a utilizar el Input Analyzer para representar y comparar diferentes
funciones de distribución de probabilidad.
Ejecución del Input Analyzer: la forma de ejecutar este componente de Arena se realiza
a través de cualquiera de estas dos opciones:
a) seleccionar Input Analyzer en Inicio/Programas/Arena
b) seleccionar Input Analyzer en el Menú Tools de Arena.
Figura 1.- Menú Principal del Input Analyzer
NOTA: en la sesión 6 se utilizará el Input Analyzer para analizar ficheros de datos
correspondientes al tiempo entre llegadas de entidades a un sistema de colas, tiempo de
servicio de un servidor o proceso, etc., con el propósito de evaluar con criterios
estadísticos (test de hipótesis Chi-cuadrado) la calidad del ajuste de dichos datos a una
determinada función de distribución de probabilidad.
2.- DATOS A ANALIZAR
Los datos que el Input Analyzer va a representar y analizar deben estar almacenados en
un fichero de texto ASCII con formato libre (los datos individuales deben estar
separados por 'espacios en blanco, tabuladores, etc.'). Para ello se puede utilizar
36
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 3.- Modelos Estadísticos en Simulación
cualquier editor de textos (word, bloc de notas, notepad, etc.). Generalmente estos datos
se corresponden con observaciones reales del sistema que se quiere analizar.
Supóngase que la siguiente lista de valores numéricos se corresponde con los tiempos
de servicio (medido en horas) de un agente de préstamos de una entidad bancaria que
revisa las solicitudes de préstamos de automóviles.
Figura 2.- Fichero de datos editado con el Bloc de Notas
Editar un fichero ASCII con datos numéricos positivos y salvarlo con el nombre
datos.dat
Si no se dispone de datos reales puede generarse datos sintéticos que sigan una función
de distribución de probabilidad mediante la opción del menú File, Data File, Generate
New ( se verá en el apartado 4).
3.- DATOS Y VENTANAS
El modo de funcionamiento del Input Analyzer se basa en Ventanas, asignando a cada
conjunto de datos que se desea analizar una ventana. Se pueden abrir tantas ventanas
como conjunto de datos se desee analizar.
Para analizar las características de los datos contenidos en un fichero se debe asignar
una Nueva Ventana a dicho fichero y después utilizar los comandos propios del Input
Analyzer.
Primer paso: abrir una nueva ventana en el Input Analyzer. Utilizar la opción File, New,
y se abre una ventana vacía como se indica en la figura.
37
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 3.- Modelos Estadísticos en Simulación
Figura 3.- Nueva Ventana en el Input Analyzer
Segundo Paso: una vez abierta una ventana vacía, se debe asignar un fichero de datos
desde dos posibles opciones:
a) File, Data File, Use Existing (para el caso de utilizar un fichero ASCII de datos
reales, previamente editado).
b) File, Data File, Generate New ( para el caso de generación artificial de datos).
En la ventana se representará, en la parte superior un Histograma de los datos y en la
parte inferior con el título Data Summary se adjunta información relevante del conjunto
de datos como el número de muestras, número de intervalos, rango del histograma, la
media y desviación de las muestras, los valores máximo y mínimo (ver figura).
Elegir la opción a) y utilizar el fichero ASCII (datos.dat) que se desea representar y
analizar. Indicar los valores que se presentan en el Data Summary.
Figura 4.- Histograma e Información del conjunto de datos
38
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 3.- Modelos Estadísticos en Simulación
4.- GENERACIÓN DE DATOS
La opción del menú File, Data File, Generate New permite al usuario generar un fichero
de muestras aleatorias que sigan una determinada función de distribución de
probabilidad.
Al seleccionar esta opción aparece un cuadro de dialogo que presenta los siguientes
submenús (ver figura):
1) una lista de funciones de distribución sobre las que se generará las muestras
2) los parámetros de la distribución seleccionada
3) el número de muestras a generar
4) el nombre del fichero sobre el que se escribirán dichas muestras. (ARENA
utiliza por defecto la extensión dst)
Figura 5.- Menú Generación de Datos
5.- AJUSTE DE LOS DATOS A UNA DISTRIBUCIÓN
Después de que los datos de un fichero han sido cargados y representados mediante un
histograma en la Ventana, el siguiente paso es Ajustar los datos a una función de
distribución de probabilidad.
Para ello, seleccionar la opción Fit del menú. Se despliega un menú con todas las
posibles distribuciones. Se selecciona la función de distribución deseada y el Input
Analyzer determinará los parámetros de la distribución que se ajuste a los datos. Dichos
parámetros e información adicional se presentan en la parte inferior de la ventana con el
título Distribution Summary
39
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 3.- Modelos Estadísticos en Simulación
Además, el Input Analyzer representará mediante una línea continua la función de
densidad de probabilidad calculada sobre el histograma, como se representa en la figura.
Figura 6.- Ajuste de los datos a una Función de Distribución
6.- MODIFICACIÓN DE PARÁMETROS
En el menú Options, Parameters, existen dos comandos: Histogram y Distribution que
permiten realizar cambios en los parámetros propios de cada una de los tipos de
representación realizados por Input Analyzer.
7.- EJERCICIOS
NOTA: Para la documentación de la práctica utilizar la opción Copy/Paste de las
ventanas obtenidas en los diferentes ejercicios.
1.- Representar el histograma y la función de distribución de los datos almacenados en
los ficheros siguientes:
expo_1.dat
expo_2.dat
40
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 3.- Modelos Estadísticos en Simulación
expo_3.dat
Comparar dichas representaciones e indicar las principales conclusiones.
2.- Representar el histograma y la función de distribución de los datos almacenados en
los ficheros siguientes:
weibull_1.dat
weibull_2.dat
weibull_3.dat
Comparar dichas representaciones e indicar las principales conclusiones.
3.- Generar datos numéricos aleatorias que sigan la función de distribución Poisson con
diferentes medias, α = 1, 2 y 4
Representar sus correspondientes histogramas y función de distribución.
4.- Cambio de Parámetros: sobre un conjunto de datos concreto (p.e. distribución
exponencial expo_1.dat o weibull_1.dat) comprobar el efecto al cambiar valor numérico
de los parámetros de las correspondientes funciones de distribución ( media, alfa, beta y
offest).
Para ello, utilizar previamente el ajuste Fit y después el menú Options, Parameters,
Distribution.
También modificar el histograma de los datos mediante Options, Parameters, Histogram
5.- Comprobar las formas que presentan las diferentes funciones de distribución : Beta ,
Lognormal, Empirical Continuous, Normal, k-Erlang, Poisson, Exponential, Gamma,
Triangular, Uniform, Weibull , para diferentes valores de sus parámetros.
41
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesiones 4 y 5.- Simulación de Sistemas de Colas
SESIONES 4 y 5.- SIMULACIÓN de SISTEMAS de COLAS
Objetivo: Estas sesiones tienen como propósito modelar, simular y evaluar diferentes
sistemas de eventos discretos desde el punto de vista de teoría sistemas de colas. El
objetivo principal de estas sesiones se desdobla en las siguientes áreas de interés:
a) familiarizar al diseñador en el estudio cuantitativo de las medidas de
comportamiento de los modelos de sistemas de colas.
b) mostrar la simulación como una herramienta válida y alternativa a los
métodos analíticos clásicos de teoría de colas.
Índice:
1.- Introducción
2.- Teoría de Colas y Arena
3.- Ejercicios
1.- INTRODUCCIÓN
Los modelos de los sistemas de colas representan y caracterizan aquellos sistemas que
utilizan una serie de recursos finitos para realizar un determinado tipo de servicio que
demandan los clientes.
En un simple modelo de colas, los clientes llegan con cierta cadencia y se juntan en una
cola o línea de espera para ser atendidos o servidos, y una vez servidos abandonan el
sistema.
Población
de Servidor
Clientes Salida
Llegada
Cola de Clientes
A la hora de tratar de mejorar un sistema de colas, el diseñador se encuentra con el
compromiso entre la utilización del servidor y la satisfacción del cliente medida en
términos de longitud de cola y tiempo de retraso.
42
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesiones 4 y 5.- Simulación de Sistemas de Colas
Se utiliza teoría de colas y/o simulación para predecir dichos parámetros en función de
los parámetros de entrada entre los que se encuentran el ratio de llegadas de clientes,
peticiones de servicio de los clientes, ratio al que el servidor trabaja, número y
organización de servidores, entre otros. Algunos de estos parámetros de entrada son en
cierto grado controlables por el gestor del sistema y en consecuencia existe cierta
relación indirecta entre el comportamiento del sistema y los parámetros de entrada.
Las medidas típicas del comportamiento del sistema (utilización del servidor, longitud
de la línea de espera y el tiempo de retraso) pueden ser calculadas matemáticamente
para sistemas relativamente sencillos. Existe una relación de fórmulas matemáticas que
expresan el valor de dichas medidas de comportamiento para una serie de sistemas de
colas (M/G/1, M/M/1, M/E /1, M/D/1, M/M/c, etc.)
K
¿Por qué el interés de obtener la solución de esta serie de sistemas de colas utilizando
simulación, si existe la solución matemática de los mismos? El interés se basa en
presentar la simulación como una herramienta válida para la solución de sistemas de
eventos discretos y de esta manera utilizar este método de solución para otros sistemas
cuyos modelos matemáticos son muy complejos, o no admiten las suposiciones
necesarias para obtener una solución matemática cerrada.
2.- TEORÍA DE COLAS Y ARENA
Antes de implementar el modelo de sistema de colas y simularlo mediante el software
Arena, conviene matizar algunos aspectos particulares del mismo en relación con los
parámetros característicos de la teoría de colas.
Siguiendo la notación de colas propuesta por Kendall, A/B/c/N/K , existen dos
parámetros que caracterizan de forma unívoca la llegada de los clientes y el tiempo de
servicio:
Llegada: λ ratio de número de llegadas de clientes por unidad de tiempo (hora, minuto)
Servicio: μ ratio de número de salidas (clientes atendidos) por unidad de tiempo
Llegadas
Salidas
μ
λ
Las medidas de comportamiento de sistemas de colas en simulaciones de larga duración
son las siguientes:
L.- media temporal del número de clientes en el sistema
L .- media temporal del número de clientes en la cola
Q
43
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesiones 4 y 5.- Simulación de Sistemas de Colas
W.- tiempo medio por cliente en el sistema
W .- tiempo medio por cliente en la cola
Q
Existen otras medidas de comportamiento que se pueden analizar en un sistema de
colas, como son:
- el número de clientes que tengan un retraso mayor que t unidades de tiempo.
o
- número de clientes que han regresado a la Población por limitaciones de la capacidad
del sistema.
- tiempo en el que ha habido más de k clientes esperando en la cola.
o
Todos estos aspectos propios de la teoría de colas se pueden identificar y materializar en
el software Arena realizando las siguientes observaciones:
a) En primer lugar hay que señalar que los bloques Create y Process del diagrama de
flujo de un sistema modelado mediante Arena son los bloques que incluyen la
expresiones necesarias para construir los modelos de sistemas de colas.
Las expresiones correspondientes a las funciones de distribución utilizadas para
representar los tiempos entre llegadas y tiempos de servicio requieren uno o dos
parámetros relacionados directamente con los valores de λ y μ respectivamente. La
figura muestra el caso particular de un sistema M/M/1 .
0
0
Create Process
EXPO(1/ λ) EXPO(1/ μ)
En ambos módulos, la función distribución exponencial, el parámetro Mean
(EXPO(Mean)) hace referencia a la media expresada en tiempo entre llegadas y tiempo
por cliente, es decir el inverso del ratio λ y μ respectivamente.
b) Las medidas de comportamiento del sistema de colas simulado en Arena se
encuentran en diferentes partes de los distintos informes (reports) que genera Arena. En
la siguiente tabla se resumen algunas secciones de los informes que recogen las medidas
de comportamiento.
MEDIDA REPORT ARENA
COMPORTAMIENTO
L Entity.WIP (work in process)
L Queues.Number Waiting
Q
W Process.Total Time
W Queues.Waiting Time
Q
ρ Resource.Utilization
(utilización recurso)
44
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesiones 4 y 5.- Simulación de Sistemas de Colas
Los valores que se obtienen de la simulación son estimaciones y por consiguiente deben
ser analizadas desde un punto de vista estadístico (no se debe esperar una solución
exactamente igual a la obtenida por las fórmulas de la solución matemática que ofrece la
teoría de colas). En realidad la notación que se debe utilizar para las medidas de
comportamiento del sistema obtenidas a través de la simulación es la siguiente: ^L,
^L , ^W, ^W , ^ρ (el símbolo ^ representa 'estimador').
Q Q
Nota: también se pueden ver los valores del comportamiento del sistema modelado
junto con otros valores internos del sistema en un fichero de extensión *.out y nombre
del modelo que genera ARENA al finalizar la simulación.
3.- EJERCICIOS: COMPORTAMIENTO en ESTADO ESTABLE DE
MODELOS MARKOVIANOS DE SISTEMAS DE COLAS
El conjunto de ejercicios propuestos tienen como objetivo determinar mediante
estimaciones basadas en simulación los parámetros más significativos del
comportamiento de una serie de sistemas de colas.
Para cada uno de los sistemas se debe obtener una tabla de dichas estimaciones para
diez valores de intensidad de tráfico ρ= λ/ μ ( μ = 10 clientes/hora y λ = 1, 2, 3, 4, 5, 6,
7, 8, y 9 clientes/hora). A dicha tabla se le añadirá una columna con los valores de la
solución matemática. Evaluar la calidad del método de simulación comparando las
estimaciones y las soluciones matemáticas.
Realizar la representación gráfica de dicha tabla con la ayuda de cualquier herramienta
que realice gráficas de una serie de datos( Excel, Matlab,..)
La duración de la simulación debe ser lo suficientemente larga para que el número de
eventos producidos garantice que las estimaciones obtenidas tienen cierto grado de
validación estadística. El número de eventos a generar en cada simulación debe ser
como mínimo 10000 eventos.
Nota: se puede utilizar Run/Setup/Terminating Condition (Process.NumberOut >=
10000)
3.1.- Modelo de Cola: Único servidor, Capacidad de cola Ilimitada M/G/1
a) modelo M/M/1
b) modelo M/E /1 (k=3, distribuciones exponenciales ratio kμ)
k
c) modelo M/D/1 (Constant)
d) modelo M/G/1 (Lognormal de media = μ, desviación estándar = 0.1, 0.05 )
Indicar las principales conclusiones que se infieren de los resultados obtenidos.
Nota: si no existiera la función de distribución ERLA(media,k), ¿cómo podría
implementarse un sistema correspondiente al apartado c) ?
45
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesiones 4 y 5.- Simulación de Sistemas de Colas
3.2.- Modelo de Cola: Único servidor, Capacidad de cola Limitada M/M/1/N
a) modelo M/M/1/3. Comparar los resultados con los obtenidos con el modelo
M/M/1 (indicar el número de clientes que regresan a la Población por
encontrarse la capacidad del sistema llena)
b) modelo M/M/1/50. Evaluar este modelo para los valores de a (λ/μ) = 0.5 y
0.9. ¿es similar a M/M/1?
3.3.- Modelo de Cola: Multiservidor M/M/c
a) modelo M/M/c para c= 1, 2 y 25
Nota: comprobar el caso c=1 con M/M/1
NOTA:
- Condición de tamaño de cola finita de un proceso.-
ejemplo particular (tamaño=3, nombre del proceso = Proceso) :
nq(Proceso.queue).lt.2
- En el tema 8, 'Análisis de Datos', se describirá con detalle los pasos necesarios para
validar estadísticamente los 'estimadores' obtenidos en los ejercicios anteriores. Un
aspecto que mejora la exactitud de las estimaciones será utilizar el promedio de los
estimadores obtenidos en realizaciones independientes de los modelos de colas (Run
Setup, Number of Replications).
46
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 6.- Análisis de Datos de Entrada
SESIÓN 6.- ANÁLISIS DE DATOS DE ENTRADA
Objetivo: Identificar y parametrizar las funciones de distribución de probabilidad de
los conjuntos de datos representativos de las variables aleatorias de entrada en los
modelos de simulación de eventos discretos. Para ello se elaborarán los diferentes
estadísticos y estimadores de las funciones de distribución de probabilidad ayudados de
herramientas software que faciliten su cálculo (Excel, calculadora programable), y
también se utilizarán los recursos que ofrecen los programas software de modelado de
entrada como el Input Analyzer de Arena.
Índice:
1.- Introducción
2.- Ejercicios
3.- Apéndice: Distribuciones
1.- INTRODUCCIÓN
En un modelo de simulación, los datos de entrada suponen un elemento determinante a
la hora de obtener resultados precisos y próximos al sistema real objeto del estudio de
simulación. En este sentido, la tarea de determinar la distribución de probabilidad
apropiada de los datos de entrada es una de las más importantes en el proceso de
modelado y simulación de un sistema de eventos discretos.
¿Cuáles son los datos de entrada en un modelo de simulación de un sistema de colas
G/G/1? Hasta ahora, en los modelos teóricos simulados con la ayuda de Arena se ha
considerado como dato de partida el tipo de distribución tanto de los tiempos entre
llegadas de los eventos (clientes), como del tiempo de servicio de los recursos limitados
(servidores).
Sin embargo, en el estudio del comportamiento de un sistema real mediante modelado y
simulación, es imprescindible garantizar de forma estadística, las características
aleatorias de los datos de entrada correspondientes a las distribuciones G, G, utilizadas
en el modelo G/G/1.
El desarrollo de un modelo válido de los datos de entrada requiere los siguientes cuatro
pasos básicos:
1) Recogida de datos del sistema real.
2) Identificación de la familia de distribución probabilística que representa el conjunto
de datos de entrada, a partir de la distribución de frecuencia o histograma de los datos
de entrada.
3) Estimar los parámetros que determinen una distribución específica de la familia de
distribuciones identificada.
47
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 6.-  Análisis de Datos de Entrada
4) Test de validación de la distribución y los parámetros seleccionados.

2.- EJERCICIOS

1.- Representar el histograma de los siguientes datos generados según una distribución
Gamma (utilizar el Input Analyzer de Arena).

| 1.691  | 1.437  | 8.221  | 5.976  |
| ------ | ------ | ------ | ------ |
| 1.116  | 4.435  | 2.345  | 1.782  |
| 3.810  | 4.589  | 5.313  | 10.90  |
| 2.649  | 2.432  | 1.581  | 2.432  |
| 1.843  | 2.466  | 2.833  | 2.361  |

Determinar los estimadores de máxima verosimilitud β^ y θ^ (utilizar Excel)

NOTA: Almacenar los datos en un fichero ASCII con el nombre Gamma_1.dat

2.- Representar el histograma de los siguientes datos generados según una distribución
Weibull con v = 0 (utilizar el Input Analyzer de Arena).

|  7.936  | 5.224  | 3.937  | 6.513  |
| ------- | ------ | ------ | ------ |
| 4.599   | 7.563  | 7.172  | 5.132  |
| 5.259   | 2.759  | 4.278  | 2.696  |
| 6.212   | 2.407  | 1.857  | 5.002  |
| 4.612   | 2.003  | 6.908  | 3.326  |

Determinar los estimadores de máxima verosimilitud   α ^ y β^ (utilizar Excel)

NOTA: Almacenar los datos en un fichero ASCII con el nombre Weibull_1.dat

3.-  Una empresa especializada en riesgos laborales ha decidido estudiar la siniestralidad
laboral de una factoría del sector minero. El número de siniestros laborales en los
últimos cien meses se detalla en la siguiente tabla:

|     | Siniestros por Mes | Frecuencia |     |
| --- | ------------------ | ---------- | --- |
|     | 0                  |            | 35  |
|     | 1                  |            | 40  |
|     | 2                  |            | 13  |
|     | 3                  |            | 6   |
|     | 4                  |            | 4   |
|     | 5                  |            | 1   |
|     | 6                  |            | 1   |

Utilizar el Test Chi-cuadrado para evaluar la hipótesis de que los datos siguen una
α
distribución de Poisson. Utilizar un nivel de significancia de   = 0.05

NOTA: Almacenar los datos en un fichero ASCII con el nombre Poisson_1.dat
  48
Xabier Basogain / Miguel Ángel Olabe             Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 6.-  Análisis de Datos de Entrada
4.-  El tiempo requerido para calcular y registrar el número de horas trabajadas durante
una semana para cada uno de los 50 empleados de una empresa se muestra en la
siguiente tabla:

| Empleado  | Tiempo     | Empleado | Tiempo     |
| --------- | ---------- | -------- | ---------- |
|           | (minutos)  |          | (minutos)  |
| 1         | 1.88       | 26       | 0.04       |
| 2         | 0.54       | 27       | 1.49       |
| 3         | 1.90       | 28       | 0.66       |
| 4         | 0.15       | 29       | 2.03       |
| 5         | 0.02       | 30       | 1.00       |
| 6         | 2.81       | 31       | 0.39       |
| 7         | 1.50       | 32       | 0.34       |
| 8         | 0.53       | 33       | 0.01       |
| 9         | 2.62       | 34       | 0.10       |
| 10        | 2.67       | 35       | 1.10       |
| 11        | 3.53       | 36       | 0.24       |
| 12        | 0.53       | 37       | 0.26       |
| 13        | 1.80       | 38       | 0.45       |
| 14        | 0.79       | 39       | 0.17       |
| 15        | 0.21       | 40       | 4.29       |
| 16        | 0.80       | 41       | 0.80       |
| 17        | 0.26       | 42       | 5.50       |
| 18        | 0.63       | 43       | 4.91       |
| 19        | 0.36       | 44       | 0.35       |
| 20        | 2.03       | 45       | 0.36       |
| 21        | 1.42       | 46       | 0.90       |
| 22        | 1.28       | 47       | 1.03       |
| 23        | 0.82       | 48       | 1.73       |
| 24        | 2.16       | 49       | 0.38       |
| 25        | 0.05       | 50       | 0.48       |

Utilizar el Test Chi-cuadrado para evaluar la hipótesis de que los tiempos de servicio
α
siguen una distribución exponencial. Utilizar un nivel de significancia de  = 0.05 y
número de clases de intervalos k = 6.

NOTA: Almacenar los datos en un fichero ASCII con el nombre Exponential_1.dat

5.-  Utilizar las opciones Fit, y Options/Parameters/Histogram del Input Analyzer para
ratificar y obtener más información sobre los cuatro conjuntos de datos Gamma_1.dat,
Weibull_1.dat, Poisson_1.dat y Exponential_1.dat.

Analizar los resultados del Test Chi-cuadrado para diferente número de intervalos, y
comprobar si todos los test indican las mismas conclusiones.

¿Es relevante el papel que desempeña el valor 'p-value'? Comprobarlo para el ajuste de
cada uno de los ficheros *.dat a otra distribución diferente a la considerada en su
correspondiente hipótesis nula.
  49
Xabier Basogain / Miguel Ángel Olabe             Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 6.- Análisis de Datos de Entrada
Distribución de Poisson.-
⎧e −α α x ⎫
⎪ x = 0, 1, .. α> 0⎪
p(x) = ⎨ !x ⎬
⎪ ⎪
⎩0 resto ⎭
E(x)=α
V(x) = α
Distribución Uniforme.-
⎧ 1 ⎫
⎪ a < x < b⎪
f (x) = ⎨b-a ⎬
⎪ ⎪
0 resto
⎩ ⎭
a +b
E(x) =
2
(b−a)2
V(x) =
12
Distribución Exponencial.-
⎧λ e -λx x ≥ 0⎫
f (x) = ⎨ ⎬
0 resto
⎩ ⎭
1
E(x) =
λ
1
V(x) =
2
λ
Distribución Gamma.-
50
Xabier Basogain / Miguel Ángel Olabe Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 6.-  Análisis de Datos de Entrada
|     | ⎧ βθ (βθx)β−1e−βθx         x>0⎪ |     |     | ⎫   |     |     |
| --- | ------------------------------- | --- | --- | --- | --- | --- |
⎪
| f(x) = ⎨Γ(x) |     |     |     | ⎬   |     |     |
| ------------ | --- | --- | --- | --- | --- | --- |
|              | ⎪   |     |     | ⎪   |     |     |
⎩0              resto
⎭
    β parámetro de Forma (Input Analyzer Arena β es el parámetro de Escala)
    θ parámetro de Escala (Input Analyze Arena θ es el parámetro de Forma)
     Nota: Γ(β)=(β-1)!  si β es entero
1
E(x)=
θ
1
V(x)=

βθ2
Distribución Weibull.-

|           | ⎧     |     | x−v β           | ⎫   |     |     |
| --------- | ----- | --- | --------------- | --- | --- | --- |
|           | β x−v |     | −( )            |     |     |     |
|           | ⎪     | β−1 |                 | v⎪  |     |     |
|           | (     | )   |  e α          x | ≥   |     |     |
| f(x) = ⎨α |       |     |                 | ⎬   |     |     |
α
|     | ⎪                     |     |     | ⎪   |     |     |
| --- | --------------------- | --- | --- | --- | --- | --- |
|     | ⎩0              resto |     |     | ⎭   |     |     |
    β parámetro de Forma(β>0)  (Input Analyzer Arena Escala)
    α parámetro de Escala (α>0)  (Input Analyzer Arena Forma)
|     v parámetro de localización ( -∞< |     |     |     | v<∞)      |     |     |
| ------------------------------------- | --- | --- | --- | --------- | --- | --- |
E(x)=
V(x)=

Distribución Triangular.-

2(x−a)
|     |     | ⎧   |     |            | ⎫       |     |
| --- | --- | --- | --- | ---------- | ------- | --- |
|     |     |     |     |          a | ≤ x ≤ b |     |
|     |     | ⎪   |     |            | ⎪       |     |
(b−a)(c−a)
|     |           | ⎪   |         |            | ⎪        |     |
| --- | --------- | --- | ------- | ---------- | -------- | --- |
|     |           | ⎪   | 2(c− x) |            | ⎪        |     |
|     | f (x) = ⎨ |     |         |          b | ≤ x ≤ c⎬ |     |
(c−b)(c−a)
|     |     | ⎪                     |     |     | ⎪   |     |
| --- | --- | --------------------- | --- | --- | --- | --- |
|     |     | ⎪0              resto |     |     | ⎪   |     |
|     |     | ⎪                     |     |     | ⎪   |     |
|     |     | ⎩                     |     |     | ⎭   |     |

a+b+c
|     | E(x) | =   |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- |
3
a+b+c
|     | V(x) | =   |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- |
3
  51
Xabier Basogain / Miguel Ángel Olabe             Modelado y Simulación de Sistemas de Eventos Discretos

Sesión 6.-  Análisis de Datos de Entrada
ESTIMADORES de Máxima Verosimilitud

Distribución Gamma : Parámetros β y θ

1 n
|     |     | M = lnX | − ∑lnX |     |     |
| --- | --- | ------- | ------ | --- | --- |
|     |     |         | n      | i   |     |
1
ver Tablas 1/M    β
|     |     | θ=1/ X |     |     |     |
| --- | --- | ------ | --- | --- | --- |

Distribución Weibull : Parámetros β y Alfa(σ) de Máxima Verosimilitud

n
∑X2
−nX2
|       | n      |                    |       | i   |     |
| ----- | ------ | ------------------ | ----- | --- | --- |
|       | 1 ∑Xβˆ | )1/βˆ              |       |     |     |
| αˆ =( |        |                 S2 | = i=1 |     |     |
i
|     | n   |     |     | n−1 |     |
| --- | --- | --- | --- | --- | --- |
i=1
n
n∑XβlnX
i i
n n
| f(β) | = +∑lnX | −   | i=1 |     |     |
| ---- | ------- | --- | --- | --- | --- |
|      | β       | i   | n   |     |     |
|      | i=1     |     | ∑Xβ |     |     |
i

i=1
|     |     | n        |            | n   |     |
| --- | --- | -------- | ---------- | --- | --- |
|     |     | n∑Xβ(lnX | )2 n(∑Xβln |     | )2  |
X
|        | −n  | i   | i   | i      | i   |
| ------ | --- | --- | --- | ------ | --- |
| f '(β) | = − | i=1 | +   | i=1    |     |
|        | β2  | n   |     | n      |     |
|        |     | ∑Xβ |     | (∑Xβ)2 |     |
|        |     | i   |     | i      |     |
|        |     | i=1 |     | i=1    |     |
ˆ
|      | f(β | )     |     |     |     |
| ---- | --- | ----- | --- | --- | --- |
| ˆ    | ˆ   | j−1   |     |     |     |
| β =β | −   |       |     |     |     |
| j    | j−1 | ˆ     |     |     |     |
|      | f   | '(β ) |     |     |     |
j−1

  52
Xabier Basogain / Miguel Ángel Olabe             Modelado y Simulación de Sistemas de Eventos Discretos