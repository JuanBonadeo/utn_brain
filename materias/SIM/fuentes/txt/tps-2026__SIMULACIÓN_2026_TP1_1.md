TP 1.1 - SIMULACIÓN DE UNA RULETA

Juan I. Torres
Universidad Tecnológica Nacional - FRRO
Zeballos 1341, S2000, Argentina
orkuan@gmail.com

30 de abril, 2026

ABSTRACT

El siguiente documento tiene por objetivo detallar el trabajo de investigación que debe realizarse
como introducción a la materia simulación. El mismo consiste en desarrollar un modelo simple de
ruleta cuyo funcionamiento será veriﬁcado mediante distintos tests rudimentarios.

Keywords Simulación · Trabajo práctico · Ruleta

1

Introducción

La ruleta1 es un juego de azar típico de los casinos, cuyo nombre viene del término francés roulette, que signiﬁca
"ruedita" o "rueda pequeña". Su uso como elemento de juego de azar, aún en conﬁguraciones distintas de la actual, no
está documentado hasta bien entrada la Edad Media. Es de suponer que su referencia más antigua es la llamada Rueda
de la Fortuna, de la que hay noticias a lo largo de toda la historia, prácticamente en todos los campos del saber humano.

La “magia” del movimiento de las ruedas tuvo que impactar a todas las generaciones. La aparente quietud del centro, el
aumento de velocidad conforme nos alejamos de él, la posibilidad de que se detenga en un punto al azar; todo esto tuvo
que inﬂuir en el desarrollo de distintos juegos que tienen la rueda como base.

Las ruedas, y por extensión las ruletas, siempre han tenido conexión con el mundo mágico y esotérico. Así, una de ellas
forma parte del tarot, más precisamente de los que se conocen como arcanos mayores.

Según los indicios, la creación de una ruleta y sus normas de juego, muy similares a las que conocemos hoy en día,
se debe a Blaise Pascal, matemático francés, quien ideó una ruleta con treinta y seis números (sin el cero), en la que
se halla un extremado equilibrio en la posición en que está colocado cada número. La elección de 36 números da
un alcance aún más vinculado a la magia (la suma de los primeros 36 números da el número mágico por excelencia:
seiscientos sesenta y seis).

Esta ruleta podía usarse como entretenimiento en círculos de amistades. Sin embargo, a nivel de empresa que pone los
medios y el personal para el entretenimiento de sus clientes, no era rentable, ya que estadísticamente todo lo que se
apostaba se repartía en premios (probabilidad de 1/36 de acertar el número y ganar 36 veces lo apostado).

En 1842, los hermanos Blanc modiﬁcaron la ruleta añadiéndole un nuevo número, el 0, y la introdujeron inicialmente
en el Casino de Montecarlo. Esta es la ruleta que se conoce hoy en día, con una probabilidad de acertar de 1/37 y ganar
36 veces lo apostado, consiguiendo un margen para la casa del 2,7% (1/37).

Más adelante, en algunas ruletas (sobre todo las que se usan en países anglosajones) se añadió un nuevo número (el
doble cero), con lo cual el beneﬁcio para el casino resultó ser doble (2/38 o 5,26%).

1WIKIPEDIA - https://es.wikipedia.org/wiki/Ruleta

2 Descripción del trabajo de investigación

El trabajo de investigación consiste en construir un programa en lenguaje Python 3.x que simule el funcionamiento del
plato de una ruleta. Para esto se debe tener en cuenta los siguientes temas:

• Generación de valores aleatorios enteros.
• Uso de listas para el almacenamiento de datos.
• Uso de la estructura de control FOR para iterar las listas.
• Empleo de funciones estadísticas.
• Gráﬁcos de los resultados mediante el paquete Matplotlib.
• Ingreso por consola de parámetros para la simulación (cantidad de tiradas, corridas y número elegido, ejemplo

python programa.py -c XXX -n YYY -e ZZ).

2.1 Exposición de los resultados y análisis de los mismos

Los resultados se deben graﬁcar y luego concluir su comportamiento simulado y esperado. A modo de ejemplo se dejan
los siguientes bocetos de gráﬁcas, siendo estas las que, como mínimo deben estar en el estudio:

Figura 1: Conjunto de gráﬁcas mínimas solicitadas.

Luego de ﬁnalizar lo anterior, se deben de realizar varias corridas del experimento (determinar y justiﬁcar la cantidad)
y generar nuevas gráﬁcas donde se muestren en forma simultáneamente sus resultados. En total son como mínimo 8
gráﬁcas en todo el trabajo. Se debe justiﬁcar cada aspecto práctico vinculando con los aspectos teóricos derivados de la
probabilidad y estadística (teorema central de límite, estadísticos, etc.).

2

2.2 Presentación del trabajo y entrega

Este y los siguientes trabajos se presentan obligatoriamente en formato LATEX. Una manera cómoda de trabajar es
mediante un IDE el cual puede ser online o local. La ventaja de trabajar online es la posibilidad de que el resto del
grupo aporte y corrija directa y simultáneamente.

Una de las plataformas online más conocidas es Overleaf. Por el otro lado, en forma local tenemos, para los que
trabajan con Linux distribución Ubuntu el muy conocido Texmaker. En Windows debe instalarse primero el compilador
MiKteX, y posteriormente puede instalarse Texmaker o TexStudio. VSCode también tiene utilidades para escribir en ,
pero se deja que los grupos elijan sus herramientas, siempre y cuando respeten el formato proporcionado.

El contenido mínimo a entregar es:

• Código completo en Python 3.x.
• Informe en formato con las secciones mínimas:

título, Resumen (Abstract), Introducción, Métodos (o
Materiales y Métodos), Resultados, Discusión, Conclusiones. Referencias. Que contenga gráﬁcas, fórmulas
empleadas, conclusiones bien redactadas y referencias reales (hay un apartado para esto), conceptos teóricos
empleados (conceptos de probabilidad, fórmula de varianza, fórmula de frecuencia relativa, teorema central del
límite, etc) y cualquier otra información que quieran agregar. Se sugiere buscar e investigar como se escriben
los "artículos cientíﬁcos" de fuentes conﬁables para no omitir o agregar secciones incorrectas

La fecha de entrega ﬁgura en el Google Classroom.

3 Recursos online obligatorios

Usaremos el template LATEXde la Cornell University por su sencillez. Es muy probable que deban hacer modiﬁcaciones,
presten atención a sus archivos adicionales para realizar cambios:

https://es.overleaf.com/latex/templates/style-and-template-for-preprints-arxiv-bio-arxiv/
pkzcrhzcdxmc

4 Recursos online sugeridos

Algunas páginas que han servido a alumnos de años anteriores en Python (se pueden recomendar otros):

https://python-para-impacientes.blogspot.com/2014/08/graficos-en-ipython.html

https://relopezbriega.github.io/blog/2015/06/27/probabilidad-y-estadistica-con-python/

3

