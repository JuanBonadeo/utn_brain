# Apunte Weitz con hojas rotadas y acotado.pdf — páginas 41 a 60 del PDF

> Nota de transcripción: cada página del PDF es un escaneo de una **doble página** del libro
> (Rardin/Weitz — capítulo 13 "Modelos de colas"). Se indica en cada encabezado qué páginas
> impresas del libro contiene, y el número manuscrito que aparece abajo a la derecha del escaneo
> (numeración propia del apunte fotocopiado: **manuscrito = página PDF − 2**).

---

--- pág. 41 ---
*(escaneo de la portadilla del capítulo + página impresa 711; manuscrito abajo a la derecha: **39**)*

## Página izquierda — portadilla del capítulo

CAPÍTULO

# 13

# MODELOS DE COLAS

*(El texto de apertura está impreso en blanco sobre una fotografía muy oscura y contrastada; se
transcribe lo legible, con reconstrucción entre corchetes de las partes tapadas por el borde de la
fotocopia.)*

**N**ational Public TV está llevando a cabo un teletón con el fin de recabar fondos. El apoyo
corporativo casi se ha ago[tado], y la red necesita abrir una fuente más amplia d[e apoyo] de los
espectadores privados. La red tiene compromi[sos de vo]luntarios para encargarse de las líneas
telefónicas [durante el] esfuerzo de cinco días, que es el tiempo que dura el ev[ento, pero] la
administración aún debe decidir qué sistema telef[ónico es la] mejor alternativa. ¿Cuántas líneas
de teléfono debe[rá alquilar la] red? La administración no desea gastar el dinero qu[e necesita]
desesperadamente en la programación de un número i[nnecesario] de líneas telefónicas. Sin embargo,
la red no puede da[rse el lujo] de que las personas que llaman para ofrecer dinero en[cuentren] que
la línea está ocupada o se les ponga a esperar tan[to tiempo] que cuelguen.

*Este capítulo le proporciona las herramientas que usted necesita para analizar la situación de
National Public TV, que pertenece a una categoría de problemas conocidos como modelos de colas.*

> [FIGURA pág. 710 (portadilla)]: fotografía a página completa, muy oscura y saturada por la
> fotocopia. Se distingue apenas una escena con siluetas humanas y un trazo punteado horizontal en
> la parte superior. No es un gráfico técnico: es la imagen decorativa de apertura del capítulo.

## Página derecha — pág. 711 del libro

MODELOS DE COLAS — 711

> *Nota al margen:* **Sistema de colas.** Sistema en el que los productos (o los clientes) llegan a
> una estación, esperan en una fila (o cola), obtienen algún tipo de servicio y luego salen del
> sistema.

Muchas industrias de productos y de servicios tienen un sistema de colas, en el que los "productos"
(o clientes) llegan a una "estación", esperan en una "fila" (o cola), obtienen algún tipo de
"servicio" y luego salen del sistema. Considere los siguientes ejemplos:

- Los clientes llegan a un banco, esperan en una fila para obtener un servicio de uno de los
  cajeros, y después salen del banco.
- Las partes de un proceso de producción llegan a una estación de trabajo particular desde
  diferentes estaciones, esperan en un compartimiento para ser procesadas por una máquina, y luego
  son enviadas a otra estación de trabajo.
- Después de hacer sus compras, los clientes eligen una fila en las cajas, esperan a que el cajero
  les cobre y luego salen de la tienda.
- Las llamadas telefónicas llegan a un centro de reservaciones de una aerolínea, esperan al agente
  de ventas disponible, son atendidas por ese agente y dejan el sistema cuando el cliente cuelga.

Los problemas administrativos relacionados con tales sistemas de colas se clasifican en dos grupos
básicos:

1. *Problemas de análisis.* Usted podría estar interesado en saber si un sistema *dado* está
   funcionando satisfactoriamente. Necesita responder una o más de las siguientes preguntas:

   a. ¿Cuál es el tiempo promedio que un cliente tiene que esperar en la fila antes de ser
      atendido?
   b. ¿Qué fracción del tiempo ocupan los servidores en atender a un cliente o en procesar un
      producto?
   c. ¿Cuáles son el número promedio y el máximo de clientes que esperan en la fila?

   Basándose en estas preguntas, los gerentes tomarán decisiones como emplear a uno o a más gente;
   agregar una estación de trabajo adicional para mejorar el nivel de servicio; o si es necesario o
   no aumentar el tamaño del área de espera.

2. *Problemas de diseño.* Usted desea diseñar las características de un sistema que logre un
   objetivo general. Esto puede implicar el planteamiento de preguntas como las siguientes:

   a. ¿Cuántas personas o estaciones deben emplearse para proporcionar un servicio aceptable?
   b. ¿Deberán los clientes esperar en una sola fila (como se hace en muchos bancos) o en
      diferentes filas (como en el caso de los supermercados)?
   c. ¿Deberá haber una estación de trabajo separada que maneje las cuestiones "especiales" (como
      el caso del acceso a primera clase en el mostrador de una aerolínea)?
   d. ¿Qué tanto espacio se necesita para que los clientes o los productos puedan esperar? Por
      ejemplo, en un sistema de reservaciones por teléfono, ¿qué tan grande debe ser la capacidad
      de retención? Esto es, ¿cuántas llamadas telefónicas se deben mantener en espera antes de que
      la siguiente obtenga la señal de ocupado?

Estas decisiones de diseño se toman mediante la evaluación de los méritos de las diferentes
alternativas, respondiendo a las preguntas de análisis del grupo 1 y luego seleccionando la
alternativa que cumpla con los objetivos administrativos.

---

--- pág. 42 ---
*(páginas impresas 712 y 713; manuscrito: **40**)*

## Página izquierda — pág. 712 del libro

712 — CAPÍTULO 13 MODELOS DE COLAS

> *Notas al margen (columna izquierda, de arriba abajo):*
>
> **Población de clientes.** Conjunto de todos los clientes posibles de un sistema de colas.
>
> **Proceso de llegada.** La forma en que los clientes de la población llegan a solicitar un
> servicio.
>
> **Proceso de colas.** La forma en que los clientes esperan a que se les dé un servicio.
>
> **Disciplina de colas.** La forma en que los clientes son elegidos para proporcionarles un
> servicio.
>
> **Proceso de servicio.** Forma y rapidez con que son atendidos los clientes.
>
> **Proceso de salida.** Forma en que los productos o los clientes abandonan un sistema de colas.
>
> **Sistema de colas de un paso.** Sistema en el cual los productos o los clientes abandonan el
> sistema después de ser atendidos en un solo centro o estación de trabajo.
>
> **Red de colas.** Sistema en el que un producto puede proceder de una estación de trabajo y pasar
> a otra antes de abandonar el sistema.

En el presente capítulo se proporcionan las técnicas para analizar un sistema de colas dado. Sin
embargo, las técnicas matemáticas específicas dependen de la *clase* de sistema al cual pertenece su
problema de colas. Estas clases, basadas en las características de los diferentes componentes del
sistema, se presentan en la sección 13.1. En la sección 13.2, se describen varias medidas utilizadas
para evaluar el desempeño de tales sistemas.

### ■ 13.1 CARACTERÍSTICAS DE UN SISTEMA DE COLAS

Para analizar un sistema de colas, es mejor primero identificar las características importantes que
aparecen en la siguiente sección de características clave, y que se ilustran en la figura 13.1.

> ### CARACTERÍSTICAS CLAVE
>
> Las siguientes características se aplican a los sistemas de colas:
>
> ✓ Una **población de clientes**, que es el conjunto de todos los clientes posibles.
>
> ✓ Un **proceso de llegada**, que es la forma en que llegan los clientes de esa población.
>
> ✓ Un **proceso de colas**, que está conformado por (a) la manera en que los clientes esperan para
>   ser atendidos y (b) la **disciplina de colas**, que es la forma en que son elegidos para
>   proporcionarles el servicio.
>
> ✓ Un **proceso de servicio**, que es la forma y la rapidez con la que es atendido el cliente.
>
> ✓ **Procesos de salida**, que son de los siguientes dos tipos:
>
>   a. Los elementos abandonan completamente el sistema después de ser atendidos, lo que tiene como
>      resultado un *sistema de colas de un paso*. Por ejemplo, como se muestra en la figura
>      13.2(a), los clientes de un banco esperan en una sola fila, son atendidos por uno de los tres
>      cajeros y, después de que son atendidos, abandonan el sistema.
>   b. Los productos, ya que son procesados en una estación de trabajo, son trasladados a alguna
>      otra para someterlos a otro tipo de proceso, lo que tiene como resultado una *red de colas*.
>      Por ejemplo, los productos que se muestran en la figura 13.2(b) primero son procesados en la
>      estación de trabajo A y después enviados a la estación B o C. Los productos terminados en
>      ambas estaciones, B y C, luego son procesados en la estación D, antes de abandonar el
>      sistema.
>
> Se necesitan diferentes análisis matemáticos para cada uno de estos dos tipos de procesos de
> salida. En el presente capítulo solamente se considerarán sistema de un paso.

El análisis de un sistema de colas de un paso depende de las características precisas de los
primeros cuatro componentes, que se analizarán con detalle a continuación.

## Página derecha — pág. 713 del libro

13.1 CARACTERÍSTICAS DE UN SISTEMA DE COLAS — 713

> [FIGURA pág. 713 — Figura 13.1 "Componentes de un sistema de colas"]: diagrama de bloques. A la
> izquierda, un círculo grande sombreado rotulado **Población de clientes**. De él sale una flecha
> rotulada **Proceso de llegada** que entra a un rectángulo grande rotulado **Sistema**. Dentro del
> rectángulo, a la izquierda, una hilera horizontal de cuatro círculos pequeños rotulada **Clientes
> que esperan**, con la llave **Proceso de colas** debajo. A la derecha, una columna vertical de
> cuadrados rotulada **Servidores** (tres cuadrados visibles y puntos suspensivos verticales
> indicando más). De los servidores sale hacia abajo/derecha una flecha rotulada **Proceso de
> servicio**, que representa la salida del sistema. Ilustra los cinco componentes: población,
> proceso de llegada, proceso de colas, servidores/proceso de servicio y proceso de salida.

Figura 13.1 Componentes de un sistema de colas.

> [FIGURA pág. 713 — Figura 13.2 "Proceso de salida de un sistema de colas"]: dos esquemas.
>
> **(a) Sistema de colas de un paso:** flecha de entrada rotulada **Llegada** hacia una fila
> horizontal de tres círculos rotulada **Clientes que esperan**; desde la fila salen tres flechas
> hacia tres cuadrados numerados **1, 2, 3**, rotulados en conjunto **Cajeros**; de los tres
> cuadrados sale una única flecha rotulada **Salida**. Ilustra el caso del banco: una sola fila,
> tres cajeros, y el cliente abandona el sistema después de ser atendido.
>
> **(b) Red de colas:** flecha rotulada **Llegada** hacia un nodo **A**; de A salen dos ramas, una
> hacia arriba al nodo **B** y otra hacia abajo al nodo **C**; ambas convergen en el nodo **D**; de
> D sale una flecha rotulada **Salida**. Los nodos forman un rombo (A a la izquierda, B arriba, C
> abajo, D a la derecha). Ilustra que un producto procesado en una estación pasa a otra antes de
> abandonar el sistema.

Figura 13.2 Proceso de salida de un sistema de colas.

---

--- pág. 43 ---
*(páginas impresas 714 y 715; manuscrito: **41**)*

## Página izquierda — pág. 714 del libro

714 — CAPÍTULO 13 MODELOS DE COLAS

### 13.1.1 La población de clientes

Al tomar en cuenta la base de clientes, la principal preocupación es el *tamaño* de la población.
Para problemas como los de un banco o de un supermercado, en donde el número de clientes potenciales
es bastante grande (cientos o miles), el tamaño de la población se considera, para fines prácticos,
como si fuera *infinita*.

Al contrario, considere una fábrica que tiene cuatro máquinas, que a menudo se descomponen y
requieren servicio de reparación en un taller especializado. En este caso, las máquinas están en
lugar de los clientes y el taller es el centro de servicio. El tamaño de la población de clientes,
en este caso, es de solamente cuatro. El análisis de poblaciones *finitas* (es decir, de tamaño
limitado) es más complicado que el análisis en donde la base de población se considera infinita.

### 13.1.2 El proceso de llegada

> *Nota al margen:* **Tiempo entre llegadas.** Intervalo de tiempo que existe entre dos llegadas
> sucesivas de clientes a un sistema de colas.

El proceso de llegada es la forma en que los clientes llegan a solicitar un servicio. La
característica más importante del proceso de llegada es el **tiempo entre llegadas**, que es la
cantidad de tiempo entre dos llegadas sucesivas. Este lapso es importante porque mientras menor sea
el intervalo de tiempo, con más frecuencia llegan los clientes, lo cual aumenta la demanda de
servidores disponibles.

> ### CARACTERÍSTICAS CLAVE
>
> Existen dos clases básicas de tiempos entre llegadas:
>
> ✓ *Determinístico*, en el cual clientes sucesivos llegan en un mismo intervalo de tiempo, fijo y
>   conocido. Un ejemplo clásico es el caso de una línea de ensamblaje, en donde los artículos
>   llegan a una estación a intervalos invariables de tiempo (conocidos como *ciclos de tiempo*).
>
> ✓ *Probabilístico*, en el cual el tiempo entre llegadas sucesivas es incierto y variable. Los
>   tiempos entre llegadas probabilísticos se describen mediante una distribución de probabilidad.

En el caso probabilístico, la determinación de la distribución real, a menudo, resulta difícil. Sin
embargo, una distribución, la *distribución exponencial*, ha probado ser confiable en muchos
problemas prácticos. La función de densidad para una distribución exponencial depende de un
parámetro, digamos λ (la letra griega lambda), y está dada por:

$$f(t) = (1/\lambda)e^{-\lambda T}$$

en donde λ (lambda) es el número promedio de llegadas por unidad de tiempo.

Con una cantidad, *T*, de tiempo, usted puede hacer uso de la función de densidad para calcular la
probabilidad de que el siguiente cliente llegue dentro de las siguientes *T* unidades a partir de la
llegada anterior, de la manera siguiente:

$$P(\text{tiempo entre llegadas} \le T) = 1 - e^{-\lambda T}$$

## Página derecha — pág. 715 del libro

13.1 CARACTERÍSTICAS DE UN SISTEMA DE COLAS — 715

Por ejemplo, si los clientes llegan al banco con una rapidez promedio de $\lambda = 20$ por hora y
si un cliente acaba de llegar, entonces la probabilidad de que el siguiente llegue dentro de los
siguientes diez minutos (es decir $T = 1/6$ de hora) es:

$$
\begin{aligned}
P(\text{tiempo entre llegadas} \le 1/6\ \text{hora}) &= 1 - e^{-(20)(1/6)} \\
&= 1 - e^{-3.333} \\
&= 1 - 0.036 \\
&= 0.964
\end{aligned}
$$

Otro planteamiento igualmente válido para describir el proceso de llegadas consiste en utilizar la
distribución de probabilidad del *número de llegadas*. Por ejemplo, usted podría estar interesado en
la probabilidad de que dos clientes lleguen dentro de los diez minutos siguientes. Cuando la
distribución de tiempos entre llegadas es una función exponencial con parámetro λ, la distribución
de probabilidad para el número de llegadas se conoce como **distribución de Poisson** y está dada
por:

$$P(\text{tiempo entre llegadas } T = k) = \frac{e^{-\lambda * T}(\lambda * T)^{k}}{k!}$$

> *Nota al margen:* **Distribución de Poisson.** Distribución que describe la probabilidad de que se
> presenten un número dado de llegadas en un intervalo dado de tiempo, cuando el tiempo entre
> llegadas sigue una distribución exponencial.

en la que $k! = k(k-1)\ldots(2)(1)$.

Por ejemplo, cuando $\lambda = 20$ clientes por hora y $T = 1/6$ de hora, la probabilidad de que
lleguen $k = 2$ clientes en los siguientes diez minutos es:

$$
\begin{aligned}
P(\text{tiempo de llegadas en 10 minutos} = 2) &= \frac{e^{-(20)(1/6)}(20/6)^{2}}{2!} \\
&= \frac{0.036 * 11.111}{2} \\
&= 0.20
\end{aligned}
$$

En este caso, el proceso de llegadas se conoce como **proceso de Poisson**, pero en general, un
proceso de llegadas puede obedecer a cualquier otra distribución.

> *Nota al margen:* **Proceso de Poisson.** Proceso aleatorio en que el tiempo entre llegadas
> sucesivas sigue una distribución exponencial.

### 13.1.3 El proceso de colas

Parte del proceso de colas tiene que ver con la forma en que los clientes esperan para ser
atendidos. Los clientes pueden esperar en *una sola fila*, como en un banco; observe la figura
13.3(a), éste es un sistema de colas de una sola línea. Al contrario, los clientes pueden elegir una
de varias filas en la que deben esperar a ser atendidos, como en las cajas cobradoras de un
supermercado; observe la figura 13.3(b), éste es un sistema de colas de líneas múltiples.

> *Nota al margen:* **Sistema de colas de una sola línea.** Sistema de colas en el cual los clientes
> esperan en una sola línea para tener acceso al siguiente prestador de servicio disponible.

Otra característica del proceso de colas es el número de espacios de espera en cada fila, es decir,
el número de clientes que pueden esperar en cada línea. En algunos casos, como en un banco, ese
número es bastante grande y no significa ningún problema práctico, pues para cuestiones de análisis
la cantidad de espacio de espera se considera *infinita*. En contraste, un sistema telefónico puede
mantener solamente un número *finito* (es decir limitado) de llamadas, después del cual las llamadas
subsecuentes no tienen acceso al sistema. Las condiciones de espacio de espera infinito y finito
requieren análisis matemáticos diferentes.

> *Nota al margen:* **Sistema de colas de líneas múltiples.** Sistema de colas en el cual los
> clientes que llegan pueden elegir una de varias líneas en la cual esperar a ser atendidos.

---

--- pág. 44 ---
*(páginas impresas 716 y 717; manuscrito: **42**)*

## Página izquierda — pág. 716 del libro

716 — CAPÍTULO 13 MODELOS DE COLAS

> ### CARACTERÍSTICAS CLAVE
>
> Otra característica del proceso de colas es la **disciplina de colas**, es decir, la forma en que
> los clientes que esperan son seleccionados para ser atendidos. A continuación presentamos algunas
> de las formas más comunes.
>
> ✓ **Primero en entrar, primero en salir (PEPS).** Los clientes son atendidos en el orden en que
>   van llegando a la fila. Los clientes de un banco y de un supermercado, por ejemplo, son
>   atendidos de esta manera.
>
> ✓ **Último en entrar, primero en salir (VEPS).** El cliente que ha llegado más recientemente es
>   el primero en ser atendido. Un ejemplo de esta disciplina se da en su proceso de producción, en
>   el que los productos llegan a una estación de trabajo y son apilados uno encima del otro. El
>   trabajador elige, para su procesamiento, el producto que está en la cima de la pila, que fue el
>   último que llegó para ser procesado o para brindarle un servicio.
>
> ✓ **Selección de prioridad.** A cada cliente que llega se le da una prioridad y se le elige según
>   ésta para brindarle el servicio. Un ejemplo de esta disciplina son los pacientes que llegan a la
>   sala de urgencias de un hospital. Mientras más severo sea el caso, mayor será la prioridad del
>   "cliente".

> *Notas al margen (columna izquierda):*
>
> **Primero en entrar, primero en salir (PEPS).** Disciplina de colas en la que los clientes son
> atendidos en el orden en que van llegando.
>
> **Primero en entrar, último en salir (VEPS).** Disciplina de colas en la que el cliente que ha
> llegado más recientemente es el primero en ser atendido.
>
> **Selección de prioridad.** Proceso de llegadas en el que a cada cliente se le da una prioridad y
> de acuerdo a ésta se selecciona para el servicio.
>
> **Sistema de colas de canal múltiple.** Sistema en el cual los clientes que llegan pueden pasar a
> una de varias estaciones de trabajo posibles.
>
> **Sistema de colas de canal sencillo.** Sistema en el cual los clientes que llegan pasan por una
> estación de trabajo.

En el presente capítulo, sólo se analizará la selección PEPS, que es la disciplina de colas más
comúnmente utilizada.

### 13.1.4 El proceso de servicio

El proceso de servicio define cómo son atendidos los clientes. En algunos casos, puede existir más
de una estación en el sistema en la cual se proporciona el servicio requerido. Los bancos y los
supermercados, de nuevo, son buenos ejemplos de lo anterior. Cada ventanilla y cada caja registradora
son estaciones que proporcionan el mismo servicio. A tales estructuras se les conoce como **sistemas
de colas de canal múltiple**. En dichos sistemas, los servidores pueden ser *idénticos*, en el
sentido de que proporcionan la misma tasa de servicio, o pueden ser *no idénticos*. Por ejemplo, si
todos los cajeros de un banco tienen la misma experiencia, pueden considerarse como idénticos. En
este capítulo, se tomarán en cuenta solamente servidores idénticos.

Al contrario de un sistema de canal múltiple, considere un proceso de producción con una estación
de trabajo que proporciona el servicio requerido. Todos los productos deben pasar por esa estación
de trabajo; en este caso se trata de un **sistema de colas de canal sencillo**. Es importante hacer
notar que incluso en un sistema de canal sencillo pueden existir muchos servidores que, *juntos*,
llevan a cabo la tarea necesaria. Por ejemplo, un negocio de lavado a mano de automóviles, tiene una
sola estación, puede tener dos empleados que trabajan en un auto de manera simultánea.

Otra característica del proceso de servicio es el número de clientes atendidos al mismo tiempo en
una estación. En los bancos y en los supermercados (sistema de canal múltiple), y en el negocio de
lavado de automóviles (sistema de canal sencillo), solamente un cliente es atendido a la vez. Por el
contrario, los pasajeros que esperan en una parada de autobús son atendidos en grupo, según la
capacidad del autobús que llega. En el presente capítulo solamente se verá el servicio de uno a la
vez.

## Página derecha — pág. 717 del libro

13.1 CARACTERÍSTICAS DE UN SISTEMA DE COLAS — 717

> [FIGURA pág. 717 — Figura 13.3 "Sistemas de colas de (a) una sola fila y (b) múltiples filas"]:
> dos esquemas apilados verticalmente.
>
> **(a)** Una hilera horizontal de cuatro círculos rotulada **Clientes que esperan**; de ella salen
> flechas hacia arriba y hacia abajo a una columna de cuadrados con un icono de servidor, rotulada
> **Servidores** (se ven tres, con puntos suspensivos verticales entre el segundo y el tercero).
> Ilustra el sistema de **una sola fila** con varios servidores.
>
> **(b)** Varias filas horizontales independientes de círculos, agrupadas por una llave a la
> izquierda rotulada **Clientes que esperan**; cada fila desemboca directamente en su propio
> cuadrado-servidor, en una columna a la derecha rotulada **Servidores** (con puntos suspensivos
> verticales indicando más filas). Ilustra el sistema de **múltiples filas**, una por servidor.

Figura 13.3 Sistemas de colas de (a) una sola fila y (b) múltiples filas.

Otra característica más de un proceso de servicio es si se permite o no la prioridad, esto es,
¿puede un servidor detener el proceso con el cliente que está atendiendo para dar lugar a un cliente
que acaba de llegar? Por ejemplo, en una sala de urgencias, la prioridad se presenta cuando un
médico, que está atendiendo un caso que no es crítico, es llamado a atender un caso más crítico. En
este capítulo, los modelos a analizar no permiten la prioridad.

> *Nota al margen:* **Prioridad.** Proceso de servicio en el cual un servidor puede interrumpir el
> servicio que está proporcionando para dar lugar a un nuevo cliente.

Cualquiera que sea el proceso de servicio, es necesario tener una idea de cuánto tiempo se requiere
para llevar a cabo el servicio. Esta cantidad es importante debido a que cuanto más dure el
servicio, más tendrán que esperar los clientes que llegan. Como en el caso del proceso de llegada,
este tiempo puede ser *determinístico* o *probabilístico*. Con un tiempo de servicio determinístico,
cada cliente requiere precisamente la misma cantidad conocida de tiempo para ser atendido. Con un
tiempo de servicio probabilístico, cada cliente requiere una cantidad distinta e incierta de tiempo
de servicio.

---

--- pág. 45 ---
*(páginas impresas 718 y 719; manuscrito: **43**)*

## Página izquierda — pág. 718 del libro

718 — CAPÍTULO 13 MODELOS DE COLAS

Los tiempos de servicio probabilísticos se describen matemáticamente mediante una distribución de
probabilidad. En la práctica resulta difícil determinar cuál es la distribución real. Sin embargo,
una distribución que ha resultado confiable en muchas aplicaciones, como cuando se trata el caso de
bancos y supermercados, es la *distribución exponencial*. En este caso, su función de densidad
depende de un parámetro, digamos μ (la letra griega my), y está dada por:

$$s(t) = (1/\mu)e^{-\mu T}$$

en la que:

$$\mu = \text{número promedio de clientes atendidos por unidad de tiempo, de modo que}$$
$$1/\mu = \text{tiempo promedio invertido en atender a un cliente.}$$

En general, el tiempo de servicio puede seguir cualquier distribución, pero, antes de que pueda
analizar el sistema, usted necesita identificar dicha distribución.

### 13.1.5 Clasificaciones de los modelos de colas

Como se mencionó al inicio del presente capítulo, para aplicar las técnicas matemáticas apropiadas,
usted debe identificar las características de un sistema de colas, basado en la población de
clientes y en los procesos de llegada, de colas y de servicio. El método de clasificación presentado
aquí pertenece a un sistema de colas en el que el tamaño de la población de clientes es infinita,
los clientes que llegan esperan en una sola fila y el espacio de espera en cada línea es
efectivamente infinito.

> ### CARACTERÍSTICAS CLAVE
>
> En este método, los símbolos describen las características del sistema.
>
> ✓ El *proceso de llegada*. Este símbolo describe la distribución de tiempo entre llegadas, que es
>   uno de los siguientes:
>
>   a. **D** para denotar que el tiempo entre llegadas es determinístico.
>   b. **M** para denotar que los tiempos entre llegadas son probabilísticos y siguen una
>      distribución exponencial.
>   c. **G** para denotar que los tiempos entre llegadas son probabilísticos y siguen una
>      distribución general diferente a la exponencial.
>
> ✓ El *proceso de servicio*. Este símbolo describe la distribución de tiempos de servicio, que es
>   una de las siguientes:
>
>   a. **D** para describir un tiempo de servicio determinístico.
>   b. **M** para denotar que los tiempos de servicio son probabilísticos y siguen una distribución
>      exponencial.
>   c. **G** para denotar que los tiempos de servicio son probabilísticos y siguen una distribución
>      general diferente a la exponencial.
>
> ✓ El *proceso de colas*. Este número, *c*, representa cuántas estaciones o canales paralelos
>   existen en el sistema. (Recuerde que se supone que los servidores son idénticos en su rapidez de
>   servicio.)

## Página derecha — pág. 719 del libro

13.2 MEDIDAS DE RENDIMIENTO PARA EVALUAR UN SISTEMA DE COLAS — 719

Considere un sistema etiquetado como *M/M/3*. La primera *M* indica que el tiempo entre llegadas es
probabilístico y sigue una distribución exponencial. La segunda *M* denota que el tiempo de servicio
es probabilístico y sigue, también, una distribución exponencial. El *3* significa que el sistema
tiene tres estaciones paralelas, cada una dando un servicio con la misma rapidez.

> ### CARACTERÍSTICAS CLAVE
>
> Cuando el espacio de espera y/o el tamaño de la población de clientes es finito, los dos
> siguientes símbolos adicionales se incluyen para indicar estas limitaciones:
>
> ✓ Un número **K** que represente el número máximo de clientes que pueden estar en el sistema en
>   cualquier momento (es decir, en servicio o en espera en la fila). Este número es igual al número
>   de estaciones paralelas más el número total de clientes que pueden esperar para ser atendidos.
>
> ✓ Un número **L** que represente el número total de clientes de la población.

Cuando se omite cualquiera de los símbolos, se supone que el valor correspondiente es infinito. Por
ejemplo, *M/M/3/10* indica que el sistema tiene espacio para un número infinito de clientes, el
número *K* no se ha puesto, y que solamente 10 posibles clientes existen.

En la presente sección, usted ha aprendido que las características básicas de un sistema de colas
incluyen el número de clientes disponibles y los procesos de llegada, de colas y de servicio. Estas
características se utilizan para clasificar un sistema de modo que se puedan aplicar los análisis
matemáticos adecuados para evaluar el desempeño del sistema, sobre la base de las medidas
presentadas en la sección 13.2.

### ■ 13.2 MEDIDAS DE RENDIMIENTO PARA EVALUAR UN SISTEMA DE COLAS

El objetivo último de la teoría de colas consiste en responder cuestiones administrativas
pertenecientes al diseño y a la operación de un sistema de colas. El gerente de un banco puede
querer decidir si programa tres o cuatro cajeros durante la hora del almuerzo. En una estructura de
producción, el administrador puede desear evaluar el impacto de la compra de una nueva máquina que
puede procesar los productos con mayor rapidez.

Cualquier sistema de colas pasa por dos fases básicas. Por ejemplo, considere la cantidad de tiempo
que los clientes tienen que esperar en un banco durante el curso de un día, como se muestra en la
figura 13.4. Cuando el banco abre a la mañana, no hay nadie en el sistema, de modo que el primer
cliente es atendido de manera inmediata. Conforme van llegando más clientes, lentamente se va
formando la cola y la cantidad de tiempo que tienen que esperar empieza a aumentar. A medida que
avanza el día, el sistema llega a una condición en la que el efecto de la falta inicial de clientes
ha sido eliminado y el tiempo de espera de cada cliente ha alcanzado un nivel bastante estable. Como
se indica en la figura 13.4, la fase inicial, que conserva los efectos de las condiciones iniciales,
se conoce como **fase transitoria**. Después de que los efectos de las condiciones iniciales son
eliminados, el sistema entra en una condición de **estado estable**. A pesar de que las preguntas
pertenecientes a ambas fases son importantes, esta sección trata *solamente* sobre el comportamiento
del estado estable.

> *Notas al margen (columna derecha):*
>
> **Fase transitoria.** El periodo inicial de un sistema de colas en que se observan los efectos de
> las condiciones iniciales.
>
> **Estado estable.** Condición del sistema después de que se han eliminado las condiciones
> iniciales.

---

--- pág. 46 ---
*(páginas impresas 720 y 721; manuscrito: **44**)*

## Página izquierda — pág. 720 del libro

720 — CAPÍTULO 13 MODELOS DE COLAS

> [FIGURA pág. 720 — Figura 13.4 "Las fases de estado transitorio y estado estable"]: gráfico de
> línea. Eje vertical rotulado **Tiempo de espera**; eje horizontal rotulado **Número de clientes
> (en orden de llegada)**. La curva parte del origen, crece rápidamente al principio con
> oscilaciones, y luego se aplana oscilando alrededor de un nivel horizontal aproximadamente
> constante. Debajo del eje horizontal, dos tramos marcados con flechas: a la izquierda, **Fase de
> transición**; a la derecha (el tramo largo y plano), **Fase de estado estable**. Ilustra cómo el
> efecto de las condiciones iniciales desaparece y el tiempo de espera se estabiliza.

Figura 13.4 Las fases de estado transitorio y estado estable.

> *Notas al margen (columna izquierda, de arriba abajo):*
>
> **Medida de rendimiento.** Valor numérico que se utiliza para evaluar los méritos de un sistema de
> colas en estado estable.
>
> **Tiempo promedio de espera ($W_q$).** Tiempo promedio que un cliente que llega tiene que esperar
> en la cola antes de ser atendido.
>
> **Tiempo promedio en el sistema ($W$).** Tiempo promedio que un cliente invierte desde su llegada
> hasta su salida de un sistema de colas.
>
> **Longitud media de la cola ($L_q$).** Número promedio de clientes que se encuentran esperando en
> la fila para ser atendidos.
>
> **Número medio en el sistema ($L$).** Número promedio de clientes que se encuentran en el sistema
> a cualquier tiempo dado.
>
> **Probabilidad de bloqueo ($p_w$).** Probabilidad de que un cliente que llega tenga que esperar
> para ser atendido.
>
> **Utilización ($U$).** Fracción de tiempo, en promedio, que un servidor está ocupado.

### 13.2.1 Algunas medidas de rendimiento comunes

Existen muchas medidas de rendimiento diferentes que se utilizan para evaluar un sistema de colas en
estado estable, algunas de las cuales se describen en la presente sección. Para diseñar y poner en
operación un sistema de colas, por lo general, los administradores se preocupan por el nivel de
servicio que recibe un cliente, así como el uso apropiado de las instalaciones de servicio de la
empresa. Algunas de las medidas que se utilizan para evaluar el rendimiento surgen de hacerse las
siguientes preguntas:

1. Preguntas relacionadas con el tiempo, centradas en el cliente, como:

   a. ¿Cuál es el tiempo promedio que un cliente recién llegado tiene que esperar en la fila antes
      de ser atendido? La medida de rendimiento asociada es el **tiempo promedio de espera**,
      representado con $W_q$.
   b. ¿Cuál es el tiempo promedio que un cliente invierte en el sistema entero, incluyendo el
      tiempo de espera y servicio? La medida de rendimiento asociada es el **tiempo promedio en el
      sistema**, denotado con $W$.

2. Preguntas cuantitativas pertinentes al número de clientes, como:

   a. En promedio, ¿cuántos clientes están esperando en la cola para ser atendidos? La medida de
      rendimiento asociada es la **longitud media de la cola**, representada con $L_q$.
   b. ¿Cuál es el número promedio de clientes en el sistema? La medida de rendimiento asociada es
      el **número medio en el sistema**, representado con $L$.

3. Preguntas probabilísticas que implican tanto a los clientes como a los servidores, por ejemplo:

   a. ¿Cuál es la probabilidad de que un cliente que llega tenga que esperar a ser atendido? La
      medida de rendimiento asociada es la **probabilidad de bloqueo**, representada con $p_w$.
   b. En cualquier tiempo particular, ¿cuál es la probabilidad de que un servidor esté ocupado? La
      medida de rendimiento asociada es la **utilización**, denotada con $U$. Esta medida indica
      también la fracción de tiempo que un servidor está ocupado.

## Página derecha — pág. 721 del libro

13.2 MEDIDAS DE RENDIMIENTO PARA EVALUAR UN SISTEMA DE COLAS — 721

   c. ¿Cuál es la probabilidad de que existan *n* clientes en el sistema? La medida de rendimiento
      asociada se obtiene calculando la probabilidad $P_0$ de que no haya clientes en el sistema, la
      probabilidad $P_1$ de que haya un cliente en el sistema, y así sucesivamente. *Esto tiene como
      resultado la distribución de probabilidad de estado*, representada por $P_n$, $n = 0, 1,
      \ldots$
   d. Si el espacio de espera es finito, ¿cuál es la probabilidad de que la cola esté llena y que un
      cliente que llegue no sea atendido? La medida de rendimiento asociada es la **probabilidad de
      negación de servicio**, representada por $p_d$.

4. Preguntas relacionadas con los costos, como:

   a. ¿Cuál es el costo promedio por unidad de tiempo para operar el sistema?
   b. ¿Cuántas estaciones de trabajo se necesitan para lograr la mayor efectividad de costos?

> *Notas al margen (columna derecha):*
>
> **Distribución de probabilidad de estado.** Probabilidad de que se encuentren *n* clientes en el
> sistema de colas cuando está en estado estable.
>
> **Probabilidad de negación de servicio ($p_d$).** Probabilidad de que un cliente que llega no
> pueda entrar al sistema debido a que la cola está llena.

El cálculo específico de estas medidas de rendimiento depende de la clase de sistema de colas, como
se vio en la sección 13.1. Algunas de estas medidas relacionadas entre sí. Conocer el valor de una
medida le permite encontrar el valor de una medida relacionada. Tales relaciones generales se
describen primeramente en la sección 13.2.2, antes de que se presenten los métodos utilizados para
calcular estas medidas de rendimiento para un sistema de colas dado.

### 13.2.2 Relaciones entre medidas de rendimiento

El cálculo de muchas medidas de rendimiento depende de los procesos de llegada y de servicio del
sistema de colas específico. Recuerde, de la sección 13.1, que en el caso probabilístico, estos
procesos son descritos matemáticamente mediante distribuciones de probabilidad. Incluso sin conocer
la distribución específica, las relaciones entre algunas de las medidas de rendimiento pueden
obtenerse para ciertos sistemas de colas, únicamente mediante el uso de los siguientes parámetros de
los procesos de llegada y de servicio:

$$\lambda = \text{número promedio de llegadas por unidad de tiempo}$$
$$\mu = \text{número promedio de clientes atendidos por unidad de tiempo en una estación}$$

Suponga una población de clientes infinita y una cantidad ilimitada de espacio de espera en la fila.
El tiempo total que un cliente invierte en el sistema es la cantidad de tiempo invertido en esperar
en la fila más el tiempo durante el cual es atendido:

$$
\left\{\begin{array}{c}\text{Tiempo promedio}\\ \text{en el sistema}\end{array}\right\}
=
\left\{\begin{array}{c}\text{tiempo promedio}\\ \text{de espera}\end{array}\right\}
+
\left\{\begin{array}{c}\text{tiempo promedio}\\ \text{de servicio}\end{array}\right\}
$$

El tiempo promedio en el sistema y el tiempo promedio de espera están representados por las
cantidades $W$ y $W_q$, respectivamente. El tiempo promedio de servicio puede expresarse en términos
del parámetro μ. Por ejemplo, si a se atienden cuatro clientes por hora, entonces, en promedio, cada
cliente requiere 1/4 de hora para ser atendido. En general, el tiempo promedio de servicio es
$1/\mu$, lo cual nos conduce a la siguiente relación:

$$W = W_q + \frac{1}{\mu} \qquad (1)$$

---

--- pág. 47 ---
*(páginas impresas 722 y 723; manuscrito: **45**)*

## Página izquierda — pág. 722 del libro

722 — CAPÍTULO 13 MODELOS DE COLAS

Considere ahora la relación entre el número promedio de clientes en el sistema *y* el tiempo
promedio que cada cliente pasa en el sistema. Imagine que un cliente acaba de llegar y se espera que
permanezca en el sistema un promedio de 1/2 hora. Durante esta media hora, otros clientes siguen
llegando a una tasa, λ, digamos doce por hora. Cuando el cliente en cuestión abandona el sistema,
después de media hora, deja tras de sí un promedio de $(1/2) * 12 = 6$ clientes nuevos. Es decir, en
promedio, existen seis clientes en el sistema a cualquier tiempo dado. En términos de λ y de las
medidas de rendimiento, entonces:

$$
\left\{\begin{array}{c}\text{Tiempo promedio}\\ \text{de clientes}\\ \text{en el sistema}\end{array}\right\}
=
\left\{\begin{array}{c}\text{número promedio}\\ \text{de llegadas por}\\ \text{unidad de tiempo}\end{array}\right\}
*
\left\{\begin{array}{c}\text{tiempo promedio}\\ \text{en el sistema}\end{array}\right\}
$$

de modo que:

$$L = \lambda * W \qquad (2)$$

Utilizando una lógica parecida se obtiene la siguiente relación entre el número promedio de clientes
que esperan en la cola y el tiempo promedio de espera en la fila:

$$
\left\{\begin{array}{c}\text{Número promedio}\\ \text{de clientes}\\ \text{en el sistema}\end{array}\right\}
=
\left\{\begin{array}{c}\text{número promedio}\\ \text{de llegadas por}\\ \text{unidad de tiempo}\end{array}\right\}
*
\left\{\begin{array}{c}\text{tiempo promedio}\\ \text{en la cola}\end{array}\right\}
$$

de manera que:

$$L_q = \lambda * W_q \qquad (3)$$

Suponiendo que usted conoce los valores de λ y μ y para las medidas $W$, $W_q$, $L$ y $L_q$, se
pueden encontrar a partir de las ecuaciones (1) a (3), ya que el valor de cualquiera de ellos se
puede encontrar si el valor de cualquiera de ellos está determinado. Por ejemplo, suponga que λ es
12 y μ es 4 y que usted ha determinado que $L_q$, el número promedio de clientes que esperan en la
cola, es 3:

$$
\begin{aligned}
W_q &= \frac{L_q}{\lambda} \qquad \text{[De (3)]}\\
&= \frac{3}{12}\\
&= \frac{1}{4}
\end{aligned}
$$

$$
\begin{aligned}
W &= W_q + \frac{1}{\mu} \qquad \text{[De (1)]}\\
&= \frac{1}{4} + \frac{1}{4}\\
&= \frac{1}{2}
\end{aligned}
$$

## Página derecha — pág. 723 del libro

13.3 ANÁLISIS DE UN SISTEMA DE COLAS DE UN SOLO CANAL DE UNA SOLA LÍNEA CON LLEGADA EXPONENCIAL Y PROCESOS DE SERVICIO — 723

$$
\begin{aligned}
L &= \lambda * W \qquad \text{[De (2)]}\\
&= 12 * \frac{1}{2}\\
&= 6
\end{aligned}
$$

> ### CARACTERÍSTICAS CLAVE
>
> En resumen, conociendo λ y μ, se cumple la siguiente relación:
>
> $$W = W_q + \frac{1}{\mu}$$
> $$L = \lambda * W$$
> $$L_q = \lambda * W_q$$

En la presente sección, usted ha aprendido las medidas de rendimiento utilizadas para evaluar un
sistema de colas y las diferentes relaciones entre ellas. Encontrar valores para tales medidas
depende de la clase específica de modelo de colas que usted tenga. En las secciones 13.3 a 13.6 se
muestra cómo encontrar estas medidas cuando se obtienen con un paquete de computación.

### ■ 13.3 ANÁLISIS DE UN SISTEMA DE COLAS DE UN SOLO CANAL DE UNA SOLA LÍNEA CON LLEGADA EXPONENCIAL Y PROCESOS DE SERVICIO (M/M/1)

En la presente sección usted verá cómo calcular las diferentes medidas de rendimiento descritas en
la sección 13.2.2 y cómo interpretar el resultado de computación asociado al análisis de un sistema
de colas *M/M/1* que consiste en lo siguiente:

1. Una población de clientes finita. *[anotación manuscrita: se agrega "in" arriba de "finita",
   corrigiendo a **infinita**]*
2. Un proceso de llegada en el que los clientes se presentan de acuerdo con un proceso de Poisson
   con una tasa promedio de λ clientes por unidad de tiempo.
3. Un proceso de colas que consiste en una sola línea de espera de capacidad infinita, con una
   disciplina de colas de primero en entrar primero en salir.
4. Un proceso de servicio que consiste en un solo servidor que atiende a los clientes de acuerdo con
   una distribución exponencial con un promedio de μ clientes por unidad de tiempo.

Para que este sistema alcance una condición de estado estable, *la tasa de servicio promedio, μ,
debe ser mayor que la tasa de llegadas promedio*, λ. Si éste no fuera el caso, la cola del sistema
continuaría creciendo debido a que, en promedio, llegarían más clientes que los que pueden ser
atendidos por unidad de tiempo. Considere el problema de Ohio Turnpike Commission.

---

--- pág. 48 ---
*(páginas impresas 724 y 725; manuscrito: **46**)*

## Página izquierda — pág. 724 del libro

724 — CAPÍTULO 13 MODELOS DE COLAS

> [FIGURA pág. 724 — Figura 13.5 "Sistema de colas para la estación de pesado en la autopista de
> Ohio"]: dibujo esquemático en perspectiva. Arriba, dos líneas de trazos horizontales representan
> los carriles de la autopista. Una rampa punteada se desprende de la autopista hacia abajo/derecha
> y conduce a una construcción rotulada **Estación de pesado**, dentro de la cual hay un rectángulo
> rotulado **Báscula** con un camión encima. Sobre la rampa se ven camiones en fila esperando. La
> figura ilustra un sistema de un solo canal (una báscula) con una única fila de espera formada en
> la rampa.

Figura 13.5 Sistema de colas para la estación de pesado en la autopista de Ohio.

**EJEMPLO 13.1 EL PROBLEMA DE COLAS DE LA OHIO TURNPIKE COMMISSION** La Comisión de la Autopista de
Ohio (Ohio Turnpike Commission, OTC) tiene un número de estaciones para el pesado de camiones a lo
largo de la autopista de cuota de Ohio, para verificar que el peso de los vehículos cumple con las
regulaciones federales. Una de tales estaciones se ilustra en la figura 13.5. La administración de
OTC está considerando mejorar la calidad del servicio en sus estaciones de pesado y ha seleccionado
una de las instalaciones como modelo a estudiar, antes de instrumentar los cambios. La
administración desea analizar y entender el desempeño del sistema actual durante las horas pico,
cuando llega a la báscula el mayor número de camiones, suponiendo que si el sistema puede
desempeñarse bien durante este periodo, el servicio en cualquier otro momento será aún mejor. ■

> *Nota al margen:* **Formación de cola EX13_1A.DAT** *(icono de disquete)*

El gerente de operaciones siente que el sistema actual de la figura 13.5 cumple con las cuatro
condiciones presentadas anteriormente. Su siguiente paso es estimar las tasas promedio de llegada y
de servicio en dicha estación. De los datos disponibles, suponga que la gerencia determina que los
valores son:

$$\lambda = \text{número promedio de camiones que llegan por hora} = 60$$
$$\mu = \text{número promedio de camiones que pueden ser pesados por hora} = 66$$

El valor de μ = 66 es mayor que el de λ = 60, de modo que es posible hacer el análisis de estado
estable de este sistema.

### 13.3.1 Cálculo de las medidas de rendimiento

En términos de los parámetros μ y λ, los investigadores han derivado fórmulas para calcular las
diferentes medidas de rendimiento descritas en la sección 13.2 para cualquier sistema de colas
*M/M/1*. Estas fórmulas a menudo se expresan en términos de la **intensidad de tráfico**, ρ (la
letra griega ro), que es el cociente de λ sobre μ. Para el problema de OTC, esta intensidad de
tráfico es:

$$
\begin{aligned}
\rho &= \frac{\lambda}{\mu}\\
&= \frac{60}{66}\\
&= 0.9091
\end{aligned}
$$

> *Nota al margen:* **Intensidad de tráfico (ρ).** Cociente de la tasa de llegadas, λ, entre la tasa
> de servicio, μ.

## Página derecha — pág. 725 del libro

13.3 ANÁLISIS DE UN SISTEMA DE COLAS DE UN SOLO CANAL DE UNA SOLA LÍNEA CON LLEGADA EXPONENCIAL Y PROCESOS DE SERVICIO — 725

Mientras más cerca esté ρ de 1, más cargado estará el sistema, lo cual tiene como resultado colas
más largas y tiempos de espera más grandes.

En términos de ρ, λ y μ, las medidas de rendimiento, para el problema de OTC, se calculan de la
manera siguiente:

1. **Probabilidad de que no haya clientes en el sistema ($P_0$):**

$$
\begin{aligned}
P_0 &= 1 - \rho\\
&= 1 - 0.9091\\
&= 0.0909
\end{aligned}
$$

Este valor indica que aproximadamente 9% del tiempo un camión que llega no tiene que esperar a que
se le proporcione el servicio porque la estación de pesado está vacía. Dicho de otra manera,
aproximadamente 91% del tiempo un camión que llega tiene que esperar.

2. **Número promedio en la fila ($L_q$):**

$$
\begin{aligned}
L_q &= \frac{\rho^{2}}{1-\rho}\\
&= \frac{(0.9091)^{2}}{1-0.9091}\\
&= 9.0909
\end{aligned}
$$

En otras palabras, en el estado estable, en promedio, la estación de pesado puede esperar tener
aproximadamente nueve camiones esperando para obtener el servicio (sin incluir al que se está
pesando).

Cuando ya ha determinado un valor para $L_q$, usted puede calcular los valores de $W_q$, $W$ y $L$,
utilizando las relaciones derivadas en la sección 13.2, de la manera siguiente:

3. **Tiempo promedio de espera en la cola ($W_q$):**

$$
\begin{aligned}
W_q &= \frac{L_q}{\lambda}\\
&= \frac{9.0909}{60}\\
&= 0.1515
\end{aligned}
$$

Este valor indica que, en promedio, un camión tiene que esperar 0.1515 horas, aproximadamente 9
minutos, en la fila antes de que empiece el proceso de pesado.

4. **Tiempo promedio de espera en el sistema ($W$):**

$$
\begin{aligned}
W &= W_q + \frac{1}{\mu}\\
&= 0.1515 + \frac{1}{66}\\
&= 0.1667
\end{aligned}
$$

---

--- pág. 49 ---
*(páginas impresas 726 y 727; manuscrito: **47**)*

## Página izquierda — pág. 726 del libro

726 — CAPÍTULO 13 MODELOS DE COLAS

Este valor indica que, en promedio, un camión invierte 0.1667 horas, 10 minutos, desde que llega
hasta que sale.

5. **Número promedio en el sistema ($L$):**

$$
\begin{aligned}
L &= \lambda * W\\
&= 60 * 0.1667\\
&= 10
\end{aligned}
$$

Este valor indica que, en promedio, existe un total de 10 camiones en la estación de pesado, ya sea
en la báscula o esperando a ser atendidos.

6. **Probabilidad de que un cliente que llega tenga que esperar ($p_w$):**

$$
\begin{aligned}
p_w &= 1 - P_0 = \rho\\
&= 0.9091
\end{aligned}
$$

Este valor, como se estableció en el paso 1, indica que aproximadamente 91% del tiempo un camión que
llega tiene que esperar.

7. **Probabilidad de que haya *n* clientes en el sistema ($P_n$):**

$$P_n = \rho^{n} * P_0$$

Al utilizar esta fórmula, se obtienen las siguientes probabilidades:

| *n* | $P_n$ |
|---|---|
| 0 | 0.0909 |
| 1 | 0.0826 |
| 2 | 0.0751 |
| 3 | 0.0683 |

Esta tabla proporciona la distribución de probabilidad para el número de camiones que se encuentran
en el sistema. Los números que aparecen en la tabla se pueden utilizar para responder una pregunta
como: ¿cuál es la probabilidad de que no haya más de tres camiones en el sistema? En este caso, la
respuesta de 0.3169 se obtiene mediante la suma de las primeras cuatro probabilidades de la tabla,
para *n* = 0, 1, 2 y 3.

8. **Utilización ($U$):**

$$
\begin{aligned}
U &= \rho\\
&= 0.9091
\end{aligned}
$$

Este valor indica que aproximadamente 91% del tiempo las instalaciones de pesado están en uso (un
camión está siendo pesado). De manera equivalente,

## Página derecha — pág. 727 del libro

13.3 ANÁLISIS DE UN SISTEMA DE COLAS DE UN SOLO CANAL DE UNA SOLA LÍNEA CON LLEGADA EXPONENCIAL Y PROCESOS DE SERVICIO — 727

aproximadamente 9% del tiempo la estación está sin funcionar, sin que haya camiones que se estén
pesando.

Las fórmulas generales para calcular estas diferentes medidas de rendimiento para un sistema de
colas *M/M/1* con una población de clientes infinita y una capacidad ilimitada de área de espera se
resumen en la tabla 13.1, en términos de los parámetros λ, μ y ρ. Ahora que usted ya conoce las
fórmulas para las diferentes medidas de rendimiento, puede dejar que la computadora lleve a cabo los
cálculos y volver su atención a las cuestiones administrativas, como se describen en la sección
13.3.2.

### 13.3.2 Interpretación de las medidas de rendimiento

Al evaluar el sistema actual, la gerencia de OTC encuentra que muchas medidas de rendimiento están
dentro de los intervalos aceptables. Por ejemplo, un tiempo de espera de $W = 10$ minutos para que
un chofer pueda pasar por el proceso de pesado es algo razonable. Se tiene también que un promedio
de $L_q = 9$ camiones esperando para ser pesados es tolerable, pues la rampa de salida de la
carretera tiene una capacidad de 15 camiones, pero la gerencia está preocupada pues hay ocasiones en
que la cola llega hasta la autopista.

**TABLA 13.1 Fórmulas para calcular las medidas de rendimiento de un sistema de colas M/M/1**

| MEDIDA DE RENDIMIENTO | FÓRMULA GENERAL |
|---|---|
| Número promedio en la fila | $L_q = \dfrac{\rho^{2}}{1-\rho}$ |
| Tiempo promedio de espera en la cola | $W_q = L_q/\lambda$ |
| Tiempo promedio de espera en el sistema | $W = W_q + \dfrac{1}{\mu}$ |
| Número promedio en el sistema | $L = \lambda * W$ |
| Probabilidad de que no haya clientes en el sistema | $P_0 = 1-\rho$ |
| Probabilidad de que un cliente que llega tenga que esperar | $p_w = 1 - P_0 = \rho$ |
| Probabilidad de que haya *n* clientes en el sistema | $P_n = \rho^{n}\,P_0$ |
| Utilización | $U = \rho$ |

Para calcular la probabilidad de que esto suceda, usted debe calcular la probabilidad de que el
número de camiones en el sistema sea de 17 o más (uno siendo atendido y 16 o más esperando en la
rampa). Este número se obtiene sumando las probabilidades $P_n$ de que *n* camiones se encuentren en
el sistema, para *n* = 17, 18, ... Esto tiene como resultado un valor de 0.20, es decir,
aproximadamente 20% del tiempo los camiones sobrepasarán la rampa completa y llegarán hasta la
autopista. Como éste no es un nivel aceptable de desempeño, la gerencia desea mejorar la eficiencia
global del sistema, no solamente por la razón anterior, sino también porque se prevé un aumento en
el tráfico de camiones sobre la autopista en el futuro cercano. Un informe reciente indica que OTC
debería planear una tasa de llegada pico de aproximadamente 70 camiones por hora, en vez del actual
valor de 60.

---

--- pág. 50 ---
*(páginas impresas 728 y 729; manuscrito: **48**)*

## Página izquierda — pág. 728 del libro

728 — CAPÍTULO 13 MODELOS DE COLAS

> *Nota al margen:* **Formación de cola EX13_1B.DAT** *(icono de disquete)*

Para atender estas cuestiones, la gerencia de OTC ha propuesto contratar un trabajador adicional, lo
cual tendría como resultado un aumento en la eficiencia de aproximadamente 10%. Es decir, con esta
persona extra, aproximadamente 73 camiones por hora pueden ser pesados en lugar de los originales
66. Como gerente de operaciones, se le ha pedido a usted que evalúe el impacto de la propuesta.

Este análisis puede llevarse a cabo utilizando las fórmulas de la sección 13.3.1. Solamente cambian
la tasa de servicio y de llegada. Los resultados que se obtienen al utilizar la sección de colas del
programa STORM para calcular las diferentes medidas de rendimiento para el nuevo sistema, en el cual
la tasa de servicio y de llegada de μ se dan en la figura 13.6.

Las primeras tres líneas del informe de la figura 13.6 muestran los datos de entrada.
Específicamente, este sistema tiene un servidor, con una tasa de llegada de 70 camiones por hora, y
una tasa de servicio de 73 camiones por hora.

La parte restante de dicho informe enumera los valores de las diferentes medidas de rendimiento. La
gerencia está particularmente preocupada tanto por el tiempo promedio que un conductor de camión
invierte en el sistema, como por el número esperado de camiones que esperan en la rampa. De los
resultados que se presentan en la figura 13.6, usted puede informar que, en promedio, un conductor
de camión pasa 0.3333 horas (20 minutos) desde el inicio hasta el final del proceso. También que el
número promedio de camiones que esperan en la rampa es de aproximadamente 22.

Estas medidas de rendimiento son confirmadas por el resultado obtenido con SQB, presentado en la
figura 13.7. La primera línea del informe muestra las tasas de llegada y de servicio. El tiempo
promedio que un conductor de camión pasa en el sistema (*W*) es de 0.332712 horas, que es
ligeramente distinto que el presentado en la figura 13.6, debido al error de redondeo. Se tiene
también del resultado obtenido con SQB, figura 13.7, que el número promedio de camiones que esperan
en la rampa ($L_q$) es de 22.3308, ligeramente distinto del valor de 22.3744 reportado en la figura
13.6, debido al error de redondeo.

Basándose en estos resultados, la gerencia de OTC encuentra que tal nivel de rendimiento es
inaceptable, no sólo porque los conductores se quejarán del hecho de tener que tardar 20 minutos en
el sistema, sino también porque la longitud de cola esperada

```
     The Problem of the Ohio Turnpike Commission
                    OTC : M / M / C
             Q U E U E   S T A T I S T I C S

  Number of identical servers . . . . . . . . .        1
  Mean arrival rate . . . . . . . . . . . . . .  70.0000
  Mean service rate per server  . . . . . . . .  73.0000

  Mean server utilization (%) . . . . . . . . .  95.8904
  Expected number of customers in queue . . . .  22.3744
  Expected number of customers in system  . . .  23.3333
  Probability that a customer must wait . . . .   0.9589
  Expected time in the queue  . . . . . . . . .   0.3196
  Expected time in the system . . . . . . . . .   0.3333
```

Figura 13.6 Resultado obtenido con STORM para el problema de colas *M/M/1* de OTC, con λ = 70 y μ = 73.

## Página derecha — pág. 729 del libro

13.4 ANÁLISIS DE UN SISTEMA DE COLAS DE CANAL MÚLTIPLE DE UNA SOLA LÍNEA CON LLEGADA EXPONENCIAL Y PROCESOS DE SERVICIO — 729

```
        Final Solution for the Problem of the OTC
                          M/M/1
 With lambda = 70 customers per hour   and f = 73 customers per hour
          Overall system effective arrival rate =  69.9994 per hour
          Overall system effective service rate =  69.9994 per hour
     Overall system effective utilization factor = 0.958904
  Average number of customers in the system (L) =  23.2897
  Average number of customers in the queue (Lq) =  22.3308
      Average time a customer in the system (W) = 0.332712 hour
       Average time a customer in the queue (Wq) = 0.319014 hour
  The probability that all servers are idle (Po) = 0.041105
  The probability an arriving customer waits(Pw) = 0.958895
             Probability of n Customers in the System
       P(0)  = 0.04110    P(1)  = 0.03942
```

Figura 13.7 Resultado obtenido con QSB para el problema de colas *M/M/1* de OTC con λ = 70 y μ = 73.

de 22 camiones excede con mucho la capacidad disponible de 15, lo cual podría tener como
consecuencia un posible accidente de tráfico en la autopista.

Para obtener niveles de rendimiento aceptables, se ha propuesto otra alternativa, a saber, la
construcción de una segunda báscula del otro lado de la estación de pesado. Utilizando el personal
actual para que opere ambas básculas, las estimaciones de la gerencia tendrán como resultado una
capacidad de peso de aproximadamente 40 camiones por hora en cada báscula.

De nuevo, se le ha pedido que evalúe la presente propuesta. En esta ocasión, sin embargo, usted *no
puede* utilizar los resultados obtenidos en la sección 13.3.1. Esto es así debido a que ahora el
sistema propuesto tiene *dos* servidores, y el análisis de la sección 13.3.1 se aplica a un sistema
con sólo un servidor. El análisis apropiado se presenta en la sección 13.4.

### ■ 13.4 ANÁLISIS DE UN SISTEMA DE COLAS DE CANAL MÚLTIPLE DE UNA SOLA LÍNEA CON LLEGADA EXPONENCIAL Y PROCESOS DE SERVICIO (M/M/c)

En la presente sección, usted verá cómo calcular las diferentes medidas de rendimiento descritas en
la sección 13.2 y cómo interpretar los resultados asociados obtenidos con computadora para analizar
un sistema de colas *M/M/c* consistente en lo siguiente:

1. Una población de clientes infinita.
2. Un proceso de llegada en el que los clientes se presentan de acuerdo a un proceso de Poisson con
   una tasa promedio de λ clientes por unidad de tiempo.
3. Un proceso de colas que consiste en una sola fila de espera de capacidad infinita, con una
   disciplina de colas de primero en entrar, primero en salir.
4. Un proceso de servicio que consiste en *c* servidores idénticos, cada uno de los cuales atiende a
   los clientes de acuerdo con una distribución exponencial, con una cantidad promedio, μ, de
   clientes por unidad de tiempo.

---

--- pág. 51 ---
*(páginas impresas 730 y 731; manuscrito: **49**)*

## Página izquierda — pág. 730 del libro

730 — CAPÍTULO 13 MODELOS DE COLAS

> [FIGURA pág. 730 — Figura 13.8 "Sistema de colas con dos básculas, para el problema de OTC"]:
> dibujo esquemático. Arriba, líneas de trazos representando la autopista. Una rampa punteada se
> abre en dos ramales que conducen a dos construcciones: la de arriba rotulada **Báscula 1** y la de
> abajo rotulada **Báscula 2**, ambas dentro del recinto rotulado **Estación de pesado**. Sobre la
> rampa, antes de la bifurcación, se ven camiones en fila con la etiqueta **Camiones esperando**.
> Ilustra un sistema *M/M/2*: una sola fila de espera que alimenta dos servidores paralelos.

Figura 13.8 Sistema de colas con dos básculas, para el problema de OTC.

Este sistema es distinto al sistema *M/M/1* de la sección 13.3 únicamente en el paso 4, que nos
permite tener *c* servidores en lugar de sólo uno. Para que un sistema *M/M/c* alcance una condición
de estado estable, *la tasa total promedio de servicio, c \* μ, debe ser estrictamente mayor que la
tasa promedio de llegadas, λ*. Si éste no fuera el caso, la cola del sistema continuaría creciendo
debido a que, en promedio y por unidad de tiempo, llegarían más clientes que los que pueden ser
atendidos.

Recuerde la última propuesta de OTC de construir una segunda báscula en la estación de pesado, según
se describió en la sección 13.3.2 y se ilustró en la figura 13.8. Esta propuesta tiene como
resultado un sistema con dos servidores, dos básculas, y la siguiente estimación de llegada,
utilizando el personal actual:

$$c = 2 \text{ servidores}$$
$$\lambda = 70 \text{ camiones por hora}$$
$$\mu = 40 \text{ camiones por hora en cada báscula}$$

> *Nota al margen:* **Formación de colas OTC_MM2.DAT** *(icono de disquete)*

El valor de $c * \mu = 2 * 40 = 80$, es mayor que el de λ = 70, de modo que se puede llevar a cabo
un análisis de estado estable para este sistema.

### 13.4.1 Cálculo de las medidas de rendimiento

Los investigadores han derivado fórmulas para calcular las diferentes medidas de rendimiento de un
sistema de colas *M/M/c*, en términos de los parámetros μ y λ. Estas fórmulas, de nueva cuenta, se
expresan en términos de ρ, que es el cociente de λ sobre μ. Para el problema de OTC:

$$
\begin{aligned}
\rho &= \frac{\lambda}{\mu}\\
&= \frac{70}{40}\\
&= 1.75
\end{aligned}
$$

## Página derecha — pág. 731 del libro

13.4 ANÁLISIS DE UN SISTEMA DE COLAS DE CANAL MÚLTIPLE DE UNA SOLA LÍNEA CON LLEGADA EXPONENCIAL Y PROCESOS DE SERVICIO — 731

En términos de ρ, λ y μ, las medidas de rendimiento para el problema de OTC se calculan de la manera
siguiente:

1. **Probabilidad de que ningún cliente esté en el sistema ($P_0$):**

$$P_0 = \frac{1}{\left(\displaystyle\sum_{n=0}^{c-1}\frac{\rho^{n}}{n!}\right) + \left(\frac{\rho^{c}}{c!}\right) * \left(\frac{c}{c-\rho}\right)}$$

donde

$$\sum_{n=0}^{c-1}\frac{\rho^{n}}{n!} = \frac{\rho^{0}}{0!} + \frac{\rho^{1}}{1!} + \ldots + \frac{\rho^{c-1}}{(c-1)!}$$

y $k! = k(k-1)\ldots 1$ (y $0! = 1$). Para el problema de OTC en el cual ρ = 1.75 y *c* = 2:

$$
\begin{aligned}
\sum_{n=0}^{c-1}\frac{\rho^{n}}{n!} &= \frac{(1.75)^{0}}{0!} + \frac{(1.75)^{1}}{1!}\\
&= 1 + 1.75\\
&= 2.75
\end{aligned}
$$

$$
\begin{aligned}
\frac{\rho^{c}}{n!} * \frac{c}{c-\rho} &= \frac{(1.75)^{2}}{2!} * \frac{2}{2-1.75}\\
&= 1.53125 * 8\\
&= 12.25
\end{aligned}
$$

$$
\begin{aligned}
P_0 &= \frac{1}{2.75 + 12.25}\\
&= \frac{1}{15}\\
&= 0.06667
\end{aligned}
$$

Este valor de $P_0$ indica que aproximadamente 7% del tiempo, la estación de pesado está vacía.

2. **Número promedio en la fila ($L_q$):**

$$
\begin{aligned}
L_q &= \frac{\rho^{c+1}}{(c-1)!} * \frac{1}{(c-\rho)^{2}} * P_0\\
&= \frac{(1.75)^{3}}{1!} * \frac{1}{(2-1.75)^{2}} * 0.06667\\
&= 5.359375 * 16 * 0.06667\\
&= 5.7167
\end{aligned}
$$

Dicho con palabras, en promedio, la estación de pesado puede esperar tener aproximadamente seis
camiones esperando a ser atendidos (sin incluir al que ya está en la báscula).

---

--- pág. 52 ---
*(páginas impresas 732 y 733; manuscrito: **50**)*

## Página izquierda — pág. 732 del libro

732 — CAPÍTULO 13 MODELOS DE COLAS

Ahora que ya se ha determinado un valor para $L_q$, los valores de $W_q$, $W$ y $L$ pueden
calcularse utilizando la relación derivada en la sección 13.2:

3. **Tiempo promedio de espera en la cola ($W_q$):**

$$
\begin{aligned}
W_q &= \frac{L_q}{\lambda}\\
&= \frac{5.7167}{70}\\
&= 0.081667
\end{aligned}
$$

Este valor indica que en promedio, un camión tiene que esperar 0.0817 horas, aproximadamente 5
minutos, en la fila antes de iniciar el proceso de pesado.

4. **Tiempo promedio de espera en el sistema ($W$):**

$$
\begin{aligned}
W &= W_q + \frac{1}{\mu}\\
&= 0.081667 + \frac{1}{40}\\
&= 0.081667 + 0.025\\
&= 0.10667
\end{aligned}
$$

Este valor indica que en promedio, un camión tiene que esperar 0.10667 horas, aproximadamente 7
minutos, desde que llega hasta que sale de la estación.

5. **Número promedio en el sistema ($L$):**

$$
\begin{aligned}
L &= \lambda * W\\
&= 70 * 0.10667\\
&= 7.4667
\end{aligned}
$$

Este valor indica que, en promedio, se tienen entre siete y ocho camiones esperando en la estación,
ya sea en la báscula o en espera de ser atendidos.

6. **Probabilidad de que un cliente que llega tenga que esperar ($p_w$):**

$$
\begin{aligned}
p_w &= \frac{1}{c!} * \rho^{c} * \frac{c}{c-\rho} * P_0\\
&= \frac{1}{2!} * (1.75)^{2} * \frac{2}{2-1.75} * 0.06667\\
&= 0.5 * 3.0625 * 8 * 0.06667\\
&= 0.81667
\end{aligned}
$$

Este valor indica que aproximadamente 82% de las veces un camión que llega tiene que esperar o, de
manera equivalente, aproximadamente 18% de las veces un camión que llega es pesado sin que tenga que
esperar.

## Página derecha — pág. 733 del libro

13.4 ANÁLISIS DE UN SISTEMA DE COLAS DE CANAL MÚLTIPLE DE UNA SOLA LÍNEA CON LLEGADA EXPONENCIAL Y PROCESOS DE SERVICIO — 733

7. **Probabilidad de que haya *n* clientes en el sistema ($P_n$):**

Si $n \le c$:

$$P_n = \frac{\rho^{n}}{n!} * P_0$$

Al utilizar esta fórmula se obtienen las siguientes probabilidades:

| *n* | $P_n$ |
|---|---|
| 0 | 0.06667 |
| 1 | 0.11667 |
| 2 | 0.10210 |

Si $n > c$:

$$P_n = \frac{\rho^{n}}{(c!)c^{\,n-c}} * P_0$$

Al utilizar esta fórmula, se obtienen las siguientes probabilidades:

| *n* | $P_n$ |
|---|---|
| 3 | 0.08932 |
| 4 | 0.07816 |
| ⋮ | ⋮ |

Estas tablas proporcionan la distribución de probabilidad para el número de camiones que hay en el
sistema. Las cantidades que aparecen en tales tablas se pueden utilizar para responder preguntas
como: ¿cuál es la probabilidad de que al menos una báscula no esté funcionando? Esta probabilidad es
la misma que la probabilidad de que haya menos de dos camiones en el sistema. Sumando las dos
primeras probabilidades de la tabla para *n* = 0 y 1, se obtiene la respuesta: 0.18334.

8. **Utilización ($U$):**

$$
\begin{aligned}
U &= 1 - \left[P_0 + \left(\frac{c-1}{c}\right)P_1 + \left(\frac{c-2}{c}\right)P_2 + \ldots + \left(\frac{1}{c}\right)P_{c-1}\right]\\
&= 1 - \left[P_0 + \left(\frac{1}{2}\right)P_1\right]\\
&= 1 - [0.06667 + (0.5 * 0.11667)]\\
&= 1 - 0.125\\
&= 0.875
\end{aligned}
$$

Este valor indica que cada báscula está ocupada 87% del tiempo.

---

--- pág. 53 ---
*(páginas impresas 734 y 735; manuscrito: **51**)*

## Página izquierda — pág. 734 del libro

734 — CAPÍTULO 13 MODELOS DE COLAS

En la tabla 13.2 se resumen las fórmulas para un sistema de colas *M/M/c* con una población infinita
de clientes y un área de espera de capacidad ilimitada, en términos de los parámetros λ, μ y ρ.
Observe que cuando *c* = 1, estas fórmulas tienen como resultado los mismos valores de las medidas
de rendimiento del sistema *M/M/1*, derivadas en la sección 13.3. Usted puede ahora dejar que la
computadora efectúe estos cálculos y dirigir su atención a cuestiones gerenciales.

**TABLA 13.2 Fórmulas para calcular las medidas de rendimiento de un sistema de colas M/M/c**

| MEDIDA DE RENDIMIENTO | FÓRMULA GENERAL |
|---|---|
| Probabilidad de que no haya clientes en el sistema | $P_0 = \dfrac{1}{\left(\sum\limits_{n=0}^{c-1}\frac{\rho^{n}}{n!}\right)+\left(\frac{\rho^{c}}{c!}\right)*\left(\frac{c}{c-\rho}\right)}$ |
| Número promedio en la fila | $L_q = \dfrac{\rho^{c+1}}{(c-1)!}*\dfrac{1}{(c-\rho)^{2}}*P_0$ |
| Tiempo promedio de espera en la cola | $W_q = \dfrac{L_q}{\lambda}$ |
| Tiempo promedio de espera en el sistema | $W = W_q + \dfrac{1}{\mu}$ |
| Número promedio en el sistema | $L = \lambda * W$ |
| Probabilidad de que un cliente que llega tenga que esperar | $p_w = \dfrac{1}{c!}*\rho^{c}*\dfrac{c}{c-\rho}*P_0$ |
| Probabilidad de que haya *n* clientes en el sistema ($n \le c$) | $P_n = \dfrac{\rho^{n}}{n!}*P_0$ |
| Probabilidad de que haya *n* clientes en el sistema ($n > c$) | $P_n = \dfrac{\rho^{n}}{(c!)c^{\,n-c}}*P_0$ |
| Utilización | $U = 1 - \left[P_0+\left(\frac{c-1}{c}\right)P_1+\left(\frac{c-2}{c}\right)P_2+\ldots+\left(\frac{1}{c}\right)P_{c-1}\right]$ |

### 13.4.2 Interpretación de las medidas de rendimiento

> *Nota al margen:* **Formación de cola OTC_MM2.DAT** *(icono de disquete)*

Los resultados de la evaluación de las fórmulas de la tabla 13.2 con el paquete de cómputo STORM,
para el sistema de colas propuesto para OTC, se muestran en la figura 13.9. Las primeras tres líneas
del informe de la figura corresponden a los datos de entrada. Este sistema tiene una tasa de llegada
de 70 camiones por hora y dos servidores, con una tasa promedio de servicio de 40 camiones por hora
en cada servidor.

El informe de la figura 13.9 también enumera las diferentes medidas de rendimiento. Usted puede
informar a la gerencia sobre el tiempo promedio que un

## Página derecha — pág. 735 del libro

13.4 ANÁLISIS DE UN SISTEMA DE COLAS DE CANAL MÚLTIPLE DE UNA SOLA LÍNEA CON LLEGADA EXPONENCIAL Y PROCESOS DE SERVICIO — 735

conductor de camión tiene que invertir en el sistema y el número esperado de camiones que esperan en
la rampa. En la última línea del informe de la figura 13.9, usted puede observar que, en promedio,
un conductor espera 0.1067 horas (aproximadamente 7 minutos) desde que entra hasta que sale.
También, que el número promedio de camiones que esperan en la rampa es de aproximadamente 5.7167.

La gerencia de OTC encuentra aceptable este nivel de rendimiento. Sin embargo, la gerencia de nuevo
se pregunta si la fila de camiones excederá la capacidad de la rampa cuando haya dos camiones en la
báscula y más de 15 esperando en la rampa. ¿Cuál es la probabilidad de que más de 17 camiones estén
en el sistema en cualquier momento?

Se puede utilizar el informe de STORM, figura 13.10, para responder a esta pregunta.
Específicamente, la probabilidad de que se presente este caso se obtiene sumando las probabilidades
de la figura correspondientes a cada valor de *n* = 18, 19, ... La probabilidad resulta ser 9.6%. Si
tal valor no es aceptable, deben sugerirse modelos alternativos. Por ejemplo, la contratación de una
persona más para aumentar la tasa de servicio, o el aumento de la capacidad del área de espera
teniendo dos filas en lugar de una sola, podrían ser sugerencias apropiadas.

Las medidas de rendimiento para este problema son confirmadas por el resultado obtenido con el
paquete de computación QSB, mostrado en la figura 13.11. La primera línea de tal informe muestra la
tasa de llegada de 70 camiones por hora y la tasa de servicio de 40 camiones por hora en cada
báscula. La cantidad promedio de tiempo que un conductor tiene que invertir en el sistema (*W*) es
de 0.106667, la misma reportada en la figura 13.9. El número promedio de camiones que esperan en la
rampa para ser pesados ($L_q$) es de 5.716664, que también es el mismo que se muestra en la figura
13.9.

Usted ha visto cómo calcular e interpretar las medidas de rendimiento para un sistema de colas
*M/M/c*, tanto a mano como con una computadora. Cuando solamente hay uno o dos sistemas
alternativos para analizar, a menudo, se puede hacer una elección aceptable basándose en las medidas
de rendimiento. Sin embargo, cuando se tienen disponibles muchas alternativas, a veces debe
incurrirse en costos de información adicionales para seleccionar la mejor alternativa, según se
describe en la sección 13.5.

```
     The Problem of the Ohio Turnpike Commission
                    OTC : M / M / C
             Q U E U E   S T A T I S T I C S

  Number of identical servers . . . . . . . . .        2
  Mean arrival rate . . . . . . . . . . . . . .  70.0000
  Mean service rate per server  . . . . . . . .  40.0000

  Mean server utilization (%) . . . . . . . . .  87.5000
  Expected number of customers in queue . . . .   5.7167
  Expected number of customers in system  . . .   7.4867
  Probability that a customer must wait . . . .   0.8167
  Expected time in the queue  . . . . . . . . .   0.0817
  Expected time in the system . . . . . . . . .   0.1067
```

Figura 13.9 Medidas de rendimiento obtenidas con STORM para el problema de dos servidores de OTC.

---

--- pág. 54 ---
*(páginas impresas 736 y 737; manuscrito: **52**)*

## Página izquierda — pág. 736 del libro

736 — CAPÍTULO 13 MODELOS DE COLAS

```
        The Problem of the Ohio Turnpike Commission
                       OTC : M / M / C
        PROBABILITY DISTRIBUTION OF NUMBER IN SYSTEM
 Number  Prob  0   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9   1
               +----+----+----+----+----+----+----+----+----+----+
      0  0.0667|***+                                             |
      1  0.1167|******---                                        |
      2  0.1021|*****+--------                                   |
      3  0.0893|****+-------------                               |
      4  0.0782|****----------------                             |
      5  0.0684|***+-------------------                          |
      6  0.0598|***------------------------                      |
      7  0.0524|***-----------------------------                 |
      8  0.0458|**+--------------------------------              |
      9  0.0401|**+-----------------------------------           |
     10  0.0351|**-------------------------------------          |
     11  0.0307|**----------------------------------------       |
     12  0.0269|*+-----------------------------------------      |
     13  0.0235|*+-------------------------------------------    |
     14  0.0206|*+--------------------------------------------   |
     15  0.0180|*-----------------------------------------------  |
     16  0.0157|*------------------------------------------------ |
     17  0.0138|*------------------------------------------------ |
     18  0.0121|*------------------------------------------------ |
     19  0.0105|*------------------------------------------------ |
     20  0.0092|+------------------------------------------------ |
     21  0.0081|+------------------------------------------------ |
     22  0.0071|+------------------------------------------------ |
     23  0.0062|+------------------------------------------------ |
     24  0.0054|+------------------------------------------------ |
   OVER  0.0375|**----------------------------------------------- |
               +----+----+----+----+----+----+----+----+----+----+
```

*(Nota: el largo exacto de las barras de asteriscos y guiones es una representación gráfica
horizontal de cada probabilidad; los valores numéricos de la columna Prob son los transcritos
arriba.)*

Figura 13.10 Probabilidad obtenida con STORM de que haya *n* camiones en el sistema de [OTC].

```
        Final Solution for the Problem of the OTC
                          M/M/2
 With lambda = 70 customers per hour   and f = 40 customers per hour
          Overall system effective arrival rate =  70.0000 per hour
          Overall system effective service rate =  70.0000 per hour
     Overall system effective utilization factor = 0.875001
  Average number of customers in the system (L) = 7.466666
  Average number of customers in the queue (Lq) = 5.716664
      Average time a customer in the system (W) = 0.106667 hour
       Average time a customer in the queue (Wq) = 0.081667 hour
  The probability that all servers are idle (Po)= 0.066667
  The probability an arriving customer waits(Pw)= 0.816667
             Probability of n Customers in the System
  P(0)   = 0.06667     P(1)   = 0.11667
```

Figura 13.11 Medidas de rendimiento obtenidas con QSB para el problema de dos servidores de OTC.

## Página derecha — pág. 737 del libro

13.5 ANÁLISIS ECONÓMICO DE LOS SISTEMAS DE COLAS — 737

### ■ 13.5 ANÁLISIS ECONÓMICO DE LOS SISTEMAS DE COLAS

En la sección 13.4, usted vio la ventaja de tener más de un servidor, a saber, la reducción del
tiempo de espera y del número de clientes que esperan a ser atendidos. Claramente, mientras más
servidores se tengan, mejor será el servicio a los clientes. Sin embargo, cada servidor implica
costos de operación. ¿De qué manera evalúa usted este equilibrio entre nivel de servicio y costo?

En el ejemplo de la Ohio Turnpike Commission de la sección 13.4, la decisión de poner en operación
dos básculas, es decir, tener dos servidores, está basada exclusivamente en el logro de un nivel
aceptable de servicio, lo que en este caso significa asegurar tiempos de espera y colas de tamaño
razonables. En algunos problemas, es posible utilizar información sobre costos para llevar a cabo un
análisis económico del equilibrio entre el número de servidores y el nivel de servicio al cliente.
Considere el problema de American Weavers, Inc.

**EJEMPLO 13.2 PROBLEMA DE COLAS DE AMERICAN WEAVERS, INC.** American Weavers, Inc., tiene una
planta de manufactura de tela en Georgia. La planta tiene un gran número de máquinas tejedoras que
con frecuencia se atascan. Estas máquinas son reparadas basándose en el procedimiento de la primera
en entrar, la primera en ser revisada, por uno de los siete miembros del personal de reparación.
Durante varios recorridos, la gerente de producción ha observado que, en promedio, aproximadamente
de 10 a 12 máquinas están fuera de operación en cualquier momento debido a que están atascadas. Ella
sabe que contratar personal de reparaciones adicional bajaría el número de máquinas sin funcionar,
lo cual traería como consecuencia un aumento en la producción, pero no sabe a cuántas personas más
debería contratar. Como asesor administrativo, se le ha mandado llamar a usted para que ayude a
determinar dicho número. ■

> *Nota al margen:* **Formación de cola EX13_2A.DAT** *(icono de disquete)*

### 13.5.1 Modelo y análisis del sistema de colas actual

El primer paso que debe dar consiste en analizar las condiciones de operación actuales. Debe
reconocer que las máquinas tejedoras conforman un modelo de colas. Los clientes están constituidos
por las máquinas que se atascan de vez en cuando. Existe un gran número de tales máquinas, de modo
que podría suponer, razonablemente, que la población de clientes es infinita. Se tienen siete
servidores independientes e idénticos que reparan las máquinas basándose en una estrategia de
primera en entrar, primera en darle servicio. Usted puede pensar en estas máquinas formando una sola
fila en espera de pasar con el siguiente servidor que esté disponible.

Para modelar esta operación, el siguiente paso consiste en reunir y analizar los datos
correspondientes a los procesos de llegada y de servicio. Suponga que se tiene que:

1. La aparición de máquinas atascadas puede ser aproximada por un proceso de llegada de Poisson con
   una tasa promedio de 25 por hora.
2. Cada máquina atascada requiere una cantidad aleatoria de tiempo para su reparación, que puede ser
   aproximada por una distribución exponencial con un tiempo promedio de servicio de 15 minutos, lo
   cual, para cada servidor, significa una tasa promedio de cuatro máquinas por hora.

Con estas observaciones, el sistema actual puede modelarse como un sistema de colas *M/M/7*, con λ =
25, μ = 4 y una población y un área de espera infinitas.

---

--- pág. 55 ---
*(páginas impresas 738 y 739; manuscrito: **53**)*

## Página izquierda — pág. 738 del libro

738 — CAPÍTULO 13 MODELOS DE COLAS

```
                 M/M/7 : M / M / C
             Q U E U E   S T A T I S T I C S

  Number of identical servers . . . . . . . . .        7
  Mean arrival rate . . . . . . . . . . . . . .  25.0000
  Mean service rate per server  . . . . . . . .   4.0000

  Mean server utilization (%) . . . . . . . . .  89.2857
  Expected number of customers in queue . . . .   5.8473
  Expected number of customers in system  . . .  12.0973
  Probability that a customer must wait . . . .   0.7017
  Expected time in the queue  . . . . . . . . .   0.2339
  Expected time in the system . . . . . . . . .   0.4839
```

Figura 13.12 Medidas de rendimiento obtenidas con STORM para el problema de American Weavers, Inc.,
con siete reparadores.

Los resultados obtenidos con el paquete STORM con respecto a las medidas de rendimiento se presentan
en la figura 13.12. Como puede ver, el gerente de producción había estimado con bastante precisión
el hecho de que entre 10 y 12 máquinas están atascadas, en promedio, en cualquier momento. De hecho,
ese número en el informe es de 12.09. La última línea del reporte indica que las máquinas atascadas
están fuera de operación durante un tiempo promedio de 0.4839 horas, aproximadamente 29 minutos.

Como asesor, se le ha pedido a usted que recomiende el número de reparadores adicionales que se
necesitarían contratar. Usted conoce las medidas de rendimiento de un total de siete trabajadores.
¿De qué manera cambian las medidas de rendimiento si se aumenta el personal de reparación? Las
medidas de rendimiento asociadas para un número entre 7 y 11 reparadores se muestran en la tabla
13.3.

A medida que aumenta el tamaño del personal de 7 a 11, el número promedio de máquinas fuera de
operación disminuye 12 a 6.333. Similarmente, la cantidad promedio de tiempo que una máquina está
fuera de operación disminuye de 0.4839 horas (aproximadamente 29 minutos) a 0.2533 horas
(aproximadamente 15 minutos). Ahora necesita información sobre los costos para determinar cuántos
reparadores adicionales, si se requieren, deben contratarse.

**TABLA 13.3 Medidas de rendimiento para el problema de American Weavers, Inc., con diferentes
tamaños de personal de reparación**

*(Encabezado de columnas agrupado bajo el rótulo **NÚMERO DE REPARADORES**.)*

| | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|
| Utilización (%) | 89.2857 | 78.1250 | 69.4444 | 62.5000 | 56.8182 |
| Número esperado en la cola | 5.8473 | 1.4936 | 0.5363 | 0.2094 | 0.0830 |
| Número esperado en el sistema | 12.0973 | 7.7436 | 6.7863 | 6.4594 | 6.3330 |
| Probabilidad de que un cliente tenga que esperar | 0.7017 | 0.4182 | 0.2360 | 0.1257 | 0.0630 |
| Tiempo esperado en la cola | 0.2339 | 0.0597 | 0.0215 | 0.0084 | 0.0033 |
| Tiempo esperado en el sistema | 0.4839 | 0.3097 | 0.2715 | 0.2584 | 0.2533 |

## Página derecha — pág. 739 del libro

13.5 ANÁLISIS ECONÓMICO DE LOS SISTEMAS DE COLAS — 739

> *(Sobre el margen superior de esta página hay un sello de biblioteca, parcialmente legible:
> "BIBLIOTECA ... ROSARIO".)*

### 13.5.2 Análisis de costos del sistema de colas

Al analizar los méritos de contratar personal de reparación adicional en American Weavers, Inc.,
usted debería identificar dos componentes importantes:

1. Un costo por hora basado en el tamaño del personal,

$$
\left\{\begin{array}{c}\text{Costo total de}\\ \text{personal por hora}\end{array}\right\}
=
\left\{\begin{array}{c}\text{costo por hora para}\\ \text{cada reparador}\end{array}\right\}
*
\left\{\begin{array}{c}\text{número de}\\ \text{reparadores}\end{array}\right\}
$$

2. Un costo por hora basado en el número de máquinas fuera de operación:

$$
\left\{\begin{array}{c}\text{Costo total}\\ \text{por la}\\ \text{espera}\end{array}\right\}
=
\left\{\begin{array}{c}\text{costo por hora para}\\ \text{cada máquina fuera}\\ \text{de operación}\end{array}\right\}
*
\left\{\begin{array}{c}\text{número promedio}\\ \text{de máquinas fuera}\\ \text{de operación}\end{array}\right\}
$$

Para seguir adelante, necesita ahora conocer el costo por hora de cada miembro del personal de
reparación (denotado con $c_s$) y el costo por hora de una máquina fuera de operación (denotado por
$c_w$), que es el costo de una hora de producción perdida. Suponga que el departamento de
contabilidad le informa que cada reparador le cuesta a la compañía $50 por hora, incluyendo
impuestos, prestaciones, etc. El costo de una hora de producción perdida deberá incluir costos
explícitos, como la cantidad de ganancias no obtenidas, y costos implícitos, como la pérdida de
voluntad por parte del cliente si no se cumple con la fecha límite de entrega. Estos costos
implícitos son difíciles de estimar. Sin embargo, suponga que el departamento de contabilidad estima
que la compañía pierde $100 por cada hora que una máquina esté fuera de operación. Ahora ya puede
calcular un costo total para cada uno de los tamaños de personal. Para un personal de siete
reparadores, el número esperado de máquinas en el sistema es 12.0973 (véase la tabla 13.3), de modo
que:

$$
\begin{aligned}
\text{Costo total} &= (\text{costo del personal}) + (\text{costo de la espera})\\
&= \left\{\left(\begin{array}{c}\text{costo por hora}\\ \text{por persona}\end{array}\right) * \left(\begin{array}{c}\text{número de}\\ \text{reparadores}\end{array}\right)\right\} +\\
&\quad\ \left\{\left(\begin{array}{c}\text{costo por hora por}\\ \text{cada máquina fuera}\\ \text{de operación}\end{array}\right) * \left(\begin{array}{c}\text{número esperado}\\ \text{de máquinas fuera}\\ \text{de operación}\end{array}\right)\right\}\\
&= (50 * 7) + (100 * 12.0973)\\
&= \$1559.73 \text{ por hora}
\end{aligned}
$$

Realizando cálculos parecidos para cada uno de los tamaños de personal restantes se tiene como
resultado los costos por hora de cada alternativa que presentamos en la tabla 13.4.

De los resultados, usted puede ver que la alternativa que tiene el menor costo por hora, $1128.63,
es tener un total de nueve reparadores. En consecuencia, su recomendación a la gerencia de
producción de American Weavers, Inc., es contratar a dos reparadores adicionales. Estos dos nuevos
empleados tendrán un costo de $100 por hora, pero este costo adicional está más que justificado por
los ahorros que se tendrán con menos máquinas fuera de operación. La recomendación reducirá el costo
por hora de $1559.73 a $1128.63, un ahorro de aproximadamente $430 por hora, mayor que la cantidad
que cubre sus honorarios.

---

--- pág. 56 ---
*(páginas impresas 740 y 741; manuscrito: **54**)*

## Página izquierda — pág. 740 del libro

740 — CAPÍTULO 13 MODELOS DE COLAS

**TABLA 13.4 Costo por hora para diferentes tamaños de personal de reparación de American Weavers,
Inc.**

| TAMAÑO DE PERSONAL | NÚMERO ESPERADO EN EL SISTEMA | COSTO POR HORA ($) | | | |
|---|---|---|---|---|---|
| 7 | 12.0973 | (50 * 7) | + | (100 * 12.0973) | = 1559.73 |
| 8 | 7.7436 | (50 * 8) | + | (100 * 7.7436) | = 1174.36 |
| 9 | 6.7863 | (50 * 9) | + | (100 * 6.7863) | = 1128.63 |
| 10 | 6.4594 | (50 * 10) | + | (100 * 6.4594) | = 1145.94 |
| 11 | 6.3330 | (50 * 11) | + | (100 * 6.3330) | = 1183.30 |

> ### CARACTERÍSTICAS CLAVE
>
> En resumen, para evaluar un sistema de colas en el que usted controla el número de servidores o su
> tasa de servicio, se necesitan las siguientes estimaciones de costo y medidas de rendimiento:
>
> ✓ El costo por servidor por unidad de tiempo ($c_s$).
> ✓ El costo por unidad de tiempo por cliente esperando en el sistema ($c_w$).
> ✓ El número promedio de clientes en el sistema ($L$).
>
> Para cada alternativa que implique *c* servidores, calcule el siguiente costo total por unidad de
> tiempo:
>
> Costo total por unidad de tiempo con *c* servidores
>
> $$= (\text{costo de los servidores}) + (\text{costo de la espera})$$
>
> $$= \left\{\left(\begin{array}{c}\text{costo por servidor}\\ \text{por unidad de tiempo}\end{array}\right)*\left(\begin{array}{c}\text{número de}\\ \text{servidores}\end{array}\right)\right\} + \left\{\left(\begin{array}{c}\text{costo por cliente}\\ \text{por unidad de}\\ \text{tiempo}\end{array}\right)*\left(\begin{array}{c}\text{número esperado}\\ \text{de clientes en el}\\ \text{sistema}\end{array}\right)\right\}$$
>
> $$= (c_s * c) + (c_w * L)$$
>
> Por último, seleccione la alternativa que ofrezca el costo total mínimo por unidad de tiempo.

### ■ 13.6 ANÁLISIS DE OTROS MODELOS DE COLAS USANDO LA COMPUTADORA

En la sección 13.1 usted aprendió que existen diferentes modelos de colas basados en las
características del sistema. Usted sabe que la población de posibles clientes puede

## Página derecha — pág. 741 del libro

13.6 ANÁLISIS DE OTROS MODELOS DE COLAS USANDO LA COMPUTADORA — 741

ser finita o infinita, el área de espera puede ser limitada o ilimitada en su capacidad, y el
proceso de servicio puede seguir o no una distribución exponencial.

Los modelos *M/M/c* y los ejemplos presentados en las secciones 13.2 a 13.5, todos suponen una
población infinita de clientes, un área de espera ilimitada, una distribución de Poisson en las
llegadas y una distribución exponencial en el servicio. Sobre la base de estas suposiciones, usted
efectúa los cálculos de las medidas de rendimiento utilizando las fórmulas de la sección 13.4. ¿Qué
sucede cuando una o varias de tales suposiciones no cumplen con el sistema de colas que se está
investigando? En algunos casos, sigue siendo posible calcular las medidas de rendimiento. Sin
embargo, las fórmulas se vuelven bastante complejas y se necesita un paquete de cómputo para llevar
a cabo los cálculos de una variedad de modelos de colas que se encuentran comúnmente y en los cuales
los clientes que llegan esperan en una sola línea.

### 13.6.1 Un sistema M/M/c con una población de clientes finita (M/M/c/K)

En los modelos de colas que usted ha visto hasta este punto, se ha supuesto que existe una población
infinita de clientes. A pesar de que en la realidad esto nunca es verdadero, para muchas
situaciones prácticas la suposición es bastante razonable. Por ejemplo, cuando la población real es
muy grande, como en el caso de clientes que llegan a un supermercado o a un banco, tal suposición es
bastante justificable. En algunos modelos, sin embargo, la suposición de una población infinita no
es apropiada. Por ejemplo:

1. Personal de mantenimiento proporciona servicio de reparación en un laboratorio de computación
   conformado por 50 microcomputadoras. En este caso, las 50 computadoras son clientes y los
   miembros del personal de reparaciones son los servidores.
2. Una compañía da mantenimiento a los elevadores de 30 edificios de oficinas. Aquí, los 30
   edificios son clientes y el personal de reparaciones de la compañía son los servidores.
3. Una flotilla de automóviles de una compañía se encuentran disponibles para 20 directivos. En este
   caso, los 20 directivos son los clientes y los automóviles de la flotilla son los servidores.

En cada uno de los ejemplos anteriores, la población de clientes es bastante limitada en tamaño.
Obtener medidas de rendimiento utilizando la suposición de una población de clientes infinita puede
producir resultados no válidos. Recuerde el problema enfrentado por el gerente de producción de
American Weavers, Inc., en el que las máquinas tejedoras se atascan de tiempo en tiempo y requieren
servicio. Al realizar el análisis, a usted, como asesor, se le hizo creer que había un número
suficiente de máquinas tejedoras, clientes, de modo que la suposición de una población infinita era
válida. Los resultados que obtuvo en la sección 13.5, sobre la base de esta suposición, llevaron a
la recomendación de contratar dos reparadores adicionales que se suman a los siete reparadores
actuales.

Al analizar con más detalle la situación con el gerente de producción, sin embargo, usted se ha
enterado de que solamente tienen 100 máquinas tejedoras. Antes de escribir su informe final, usted
necesita ver si la consideración de la población de clientes como finita tiene un impacto
significativo en su recomendación.

En general, la suposición de una población finita afecta el proceso de llegada. Con una población
infinita, la tasa de llegadas permanece igual, sin importar cuántos clientes hayan llegado. Éste *no*
es el caso con una población finita. Supongamos que usted estima que los clientes de una población
infinita llegan a una tienda de abarrotes con

---

--- pág. 57 ---
*(páginas impresas 742 y 743; manuscrito: **55**)*

## Página izquierda — pág. 742 del libro

742 — [CAPÍTULO 13 MODELOS] DE COLAS

> *Nota: en este párrafo varias palabras impresas fueron re-entintadas a mano sobre el texto
> original desvanecido; el texto resultante es el que se transcribe.*

una tasa de, digamos, 20 por hora. Incluso si ya hay 60 clientes en algún [lugar], resulta razonable
suponer que los clientes nuevos continuarán llegando a un ritmo de 20 por hora, porque hay un número
infinito de clientes que aún no están en la tienda. Sin embargo, suponga que la tienda tiene una
base de 100 clientes y 60 ya están dentro. Ya no resulta razonable suponer que los 40 clientes
restantes llegarán con una tasa de 20 por hora, pues existen muy pocos de ellos que aún no llegan.

> ### CARACTERÍSTICAS CLAVE
>
> En general, con un número finito de clientes, la tasa de llegadas disminuye conforme aumenta el
> número de clientes en el sistema, porque existen menos clientes restantes que aún no llegan.

Los procesos de llegada para una población finita no se pueden describir de manera matemática
mediante una tasa de llegada *fija*, debido a que la tasa cambia según el número de clientes que se
encuentren en el sistema. Cuantos más clientes haya en el sistema, menor será la tasa de llegada de
clientes. Considere los extremos. Si el sistema no tiene clientes, la tasa de llegada estará en
nivel más alto. Si todos los clientes están en el sistema en un momento dado, la tasa de llegada
bajará a cero. ¿De qué modo, entonces, se puede especificar la tasa de llegadas?

El proceso de llegada se describe considerando la *tasa de llegada de cada cliente individual*. Esto
es, usted debe identificar con qué frecuencia llega un cliente en particular. En el problema de
American Weavers, con 100 máquinas, usted debe determinar la tasa a la cual cada máquina requiere
reparación. Suponga que la frecuencia es de una vez cada cuatro horas. Esta frecuencia se convierte
en una tasa por hora:

$$\lambda = 1/4 = 0.25 \text{ atascadas por hora por máquina}$$

```
             M/M/7/K : M / M / C / K / K
             Q U E U E   S T A T I S T I C S

  Number of identical servers . . . . . . . . .        7
  Mean arrival rate per customer  . . . . . . .   0.2500
  Mean service rate per customer  . . . . . . .   4.0000
  Size of the source population . . . . . . . .      100

  Mean server utilization (%) . . . . . . . . .  82.5102
  Expected number of customers in queue . . . .   1.8128
  Expected number of customers in system  . . .   7.5885
  Probability that a customer must wait . . . .   0.5254
  Expected time in the queue  . . . . . . . . .   0.0785
  Expected time in the system . . . . . . . . .   0.3285
```

Figura 13.13 Medidas de rendimiento obtenidas con STORM para el problema de American Weavers, Inc.,
con una población finita.

## Página derecha — pág. 743 del libro

13.6 ANÁLISIS DE OTROS MODELOS DE COLAS USANDO LA COMPUTADORA — 743

Recuerde que, actualmente, existe un personal de siete reparadores, cada uno capaz de reparar una
máquina en un tiempo promedio de 15 minutos. La tasa de servicio por servidor es μ = 4 máquinas por
hora. Recuerde también que el costo por hora de cada reparador es de $50, y que el costo por hora de
producción perdida cuando una máquina se atora es de $100. Al introducir estos datos en el paquete
de software STORM, junto con el hecho de que el tamaño de la población es de 100, produce los
valores para las medidas de rendimiento mostrados en la figura 13.13.

> *Nota al margen:* **Formación de cola EX13_2B.DAT** *(icono de disquete)*

Compare las medidas de rendimiento de la figura 13.13 con las de la figura 13.12 presentada en la
sección 13.5, correspondiente a una población infinita. Usted puede ver que hay algunas diferencias.
Por ejemplo, con una población infinita, el número esperado de máquinas fuera de operación es de
12.0973; con una población finita de 100, la misma estadística es de 7.5885. ¿Qué es lo que causa
esta significativa diferencia? Con una población infinita, la tasa de llegada se fija en 25 máquinas
por hora, independientemente de cuántas máquinas estén en reparación en cualquier momento. Pero
considere una población finita de 100 máquinas. Si las 100 máquinas tejedoras están trabajando, la
tasa de descomposturas también es de 25 por hora (0.25 atascadas por máquina * 100 máquinas). Pero,
¿qué sucede cuando, digamos, diez máquinas se atascan? Solamente hay 90 máquinas operando, de modo
que la tasa baja a 22.5 (0.25 atascadas por máquina * 90 máquinas) tejedoras atascadas por hora. El
número menor de llegadas tiene como resultado un menor número de máquinas atascadas que requieren
servicio.

El análisis económico de STORM para este ejemplo, se muestra en la figura 13.14. Los costos por cada
servidor y por espera son los mismos aquí que antes. La última línea de dicho informe proporciona el
costo total de $1108.85 por hora para el sistema actual con siete reparadores. STORM lleva a cabo un
análisis económico parecido con diferentes cantidades de reparadores e informa el tamaño del
personal con menor costo por hora en la última columna, etiquetada con "Optimal system" (Sistema
óptimo). Del informe de la figura 13.14, como puede ver, el tamaño óptimo de reparadores es de
solamente ocho, con una población finita de 100 máquinas. Este tamaño de personal es menor que el
número óptimo de nueve que se obtiene cuando se supone una población infinita, debido a que menos
máquinas tejedoras están atascadas. Por consiguiente, usted deberá modificar su recomendación y
sugerir que solamente se contrate un reparador adicional.

```
             M/M/7/K : M / M / C / K / K
            COST ANALYSIS PER UNIT TIME

                        |  Current System |  Optimal System *
  Number of servers     |        7        |         8
  Cost per server       |    50.0000      |     50.0000
  Cost of service       |         350.0000|          400.0000
  Mean number in system |     7.5885      |      6.5145
  Waiting cost/customer |   100.0000      |    100.0000
  Cost of waiting       |         758.8500|          651.4500
                                ---------           ---------
  TOTAL COST                    1108.8500           1051.4500
            * Optimization is over number of servers
```

Figura 13.14 Análisis económico hecho con STORM para el problema de American Weavers, Inc., con una
población finita.

---

--- pág. 58 ---
*(páginas impresas 744 y 745; manuscrito: **56**)*

## Página izquierda — pág. 744 del libro

744 — CAPÍTULO 13 MODELOS DE COLAS

### 13.6.2 Un sistema M/M/c con capacidad de espera limitada (M/M/c/K)

¿Es válida la suposición de un área de espera ilimitada para los clientes? Los modelos de colas
vistos hasta aquí, han utilizado esta suposición. De hecho, en muchas situaciones prácticas, esta
suposición es razonable. En un banco, por ejemplo, el área de espera es limitada, pero los clientes
que esperan nunca necesitan más de tal espacio. Incluso cuando la fila se hace muy grande, el
espacio de espera puede extenderse hasta los pasillos o la calle. Así pues, para todos los
propósitos prácticos, el área de espera puede suponerse ilimitada. En algunos modelos, sin embargo,
esta suposición no resulta apropiada.

1. Un sistema de reservaciones por teléfono puede mantener un número limitado de llamadas. Aquí, las
   llamadas que llegan son los clientes y los recepcionistas son los servidores.
2. En una planta de producción, las partes que llegan de una etapa previa de producción a una
   máquina en donde se les hará cierto proceso esperan en una banda transportadora con una capacidad
   limitada. Si las partes que esperan alcanzan la capacidad de la banda, la producción en la etapa
   anterior deberá detenerse. En este caso, las partes que llegan de la etapa anterior son los
   clientes y la máquina es el servidor.
3. Un estacionamiento, una vez lleno a toda su capacidad, debe rechazar a los automóviles que
   llegan. En este caso, los autos que llegan son los clientes, cada cajón de estacionamiento es un
   servidor y no hay espacio de espera.

En cada uno de estos ejemplos, no hay área de espera o la capacidad de ésta es limitada. Cuando se
llena el área de espera, los clientes que llegan son rechazados y podrían, o no, regresar. En tales
casos, las medidas de rendimiento obtenidas utilizando la suposición de un área de espera limitada
pueden no ser válidas. Al modificar las fórmulas para calcular las medidas de rendimiento para tomar
en cuenta el espacio limitado de espera, se pueden obtener resultados válidos.

> ### CARACTERÍSTICAS CLAVE
>
> Estos sistemas dan lugar a cuestiones adicionales:
>
> ✓ ¿Cuál es la probabilidad de que un cliente que llegue sea rechazado y se le niegue el servicio
>   porque el área de espera está llena? A esta medida de rendimiento se le conoce como la
>   **probabilidad de negación de servicio**, denotada con $p_d$.
>
> ✓ Cuando se efectúa un análisis económico, debe tomarse en consideración un tercer componente, un
>   costo asociado con la pérdida de un cliente, junto con el costo por servidor y el costo por
>   esperar.

Considere el problema enfrentado por National Public TV (NPTV).

**EJEMPLO 13.3 EL PROBLEMA DE CAPACIDAD DE ESPERA LIMITADA DE NATIONAL PUBLIC TV** El gerente de la
estación local de NPTV, una red de televisión no lucra-

## Página derecha — pág. 745 del libro

13.6 ANÁLISIS DE OTROS MODELOS DE COLAS USANDO LA COMPUTADORA — 745

tiva, está planeando un maratón telefónico (teletón) especial de cinco días para la obtención de
fondos, y está tratando de determinar el tipo de sistema telefónico que debe alquilar para recibir
las promesas de donaciones. La compañía telefónica local proporciona sistemas de 15 o de 20 líneas.
Con cada sistema, se tiene disponible una opción de espera de 0, 5 o 10 llamadas, costos diarios
totales dados a continuación:

| SISTEMA | NÚMERO DE TELÉFONOS | LLAMADAS ESPERADAS | COSTO TOTAL ($/DÍA) |
|---|---|---|---|
| 1 | 15 | 0 | 150 |
| 2 | 20 | 0 | 220 |
| 3 | 15 | 5 | 180 |
| 4 | 20 | 5 | 264 |
| 5 | 15 | 10 | 225 |
| 6 | 20 | 10 | 330 |

Como gerente de la estación, usted desea determinar el sistema más económico que podría utilizar. ■

Al igual que con cualquier sistema de colas, su primera tarea consiste en identificar los procesos
de llegada y de servicio apropiados. En este caso, un proceso de llegada de Poisson y una tasa de
servicio exponencial han resultado ser, históricamente, razonables para sistemas telefónicos.
Suponga que su investigación revela los siguientes datos:

1. Tasa de llegadas = λ = 150 llamadas por hora.
2. Tasa de servicio por línea telefónica = μ = 12 llamadas por hora.

Para analizar el rendimiento de uno de estos seis sistemas diferentes, usted debe introducir estos
datos en un paquete de computación capaz de proporcionar medidas para modelos *M/M/c* con capacidad
de espera limitada. Los resultados obtenidos con el paquete STORM para el primer sistema, con 15
líneas y sin mantenimiento de llamadas, se muestran en la figura 13.15. Excepto por la última línea
del informe, todas las medidas de rendimiento son interpretadas del mismo modo que en cualquier
modelo

> *Nota al margen:* **Formación de cola EX13_3.DAT** *(icono de disquete)*

```
            M/M/15/0 : M / M / C / K
             Q U E U E   S T A T I S T I C S

  Number of identical servers . . . . . . . . .       15
  Mean arrival rate . . . . . . . . . . . . . . 150.0000
  Mean service rate per server  . . . . . . . .  12.0000
  Waiting room capacity . . . . . . . . . . . .        0

  Mean server utilization (%) . . . . . . . . .  74.9592
  Expected number of customers in queue . . . .   0.0000
  Expected number of customers in system  . . .  11.2439
  Probability that a customer must wait . . . .   0.1005
  Probability of service denial . . . . . . . .   0.1005
```

Figura 13.15 Medidas de rendimiento obtenidas con STORM para el problema *M/M/15/0* de National
Public TV.

---

--- pág. 59 ---
*(páginas impresas 746 y 747; manuscrito: **57**)*

## Página izquierda — pág. 746 del libro

746 — CAPÍTULO 13 MODELOS DE COLAS

*M/M/c*. Observe la medida de rendimiento de la probabilidad de negación de servicio ($p_d$), una
nueva e importante estadística, en la última línea del informe. El valor de 0.1005 indica que con
este sistema existe 10% de probabilidad de que un observador que llame obtenga señal de ocupado
porque las 15 líneas están ocupadas. Este cliente puede llamar o no de nuevo. En el último caso, se
pierden entradas.

Para realizar un análisis económico de tales sistemas, usted necesita saber el costo de los
servidores y el costo de la espera. También necesita estimar el costo de perder un cliente cuando el
espacio de espera está lleno. Para el problema de NPTV, estos tres componentes del costo se estiman
de la manera siguiente:

1. **Costo por servidor:** Cada servidor corresponde a una línea telefónica. El costo total para
   NPTV puede convertirse en un costo por línea telefónica por hora. Suponga que el teletón se lleva
   a cabo durante ocho horas diarias. El costo asociado para el primer sistema es:

$$
\begin{aligned}
c_s &= (\$150/\text{día})/(8\ \text{horas}/\text{día})/(15\ \text{líneas telefónicas})\\
&= 1.25
\end{aligned}
$$

   Por consiguiente, con este sistema de 15 servidores (líneas telefónicas), este costo por hora es:

$$
\begin{aligned}
\text{Costo total de los servidores} &= (\text{costo por servidor}) * (\text{número de servidores})\\
&= c_s * c\\
&= 1.25 * 15\\
&= \$18.75 \text{ por hora}
\end{aligned}
$$

2. **Costo de espera:** En este caso, no existe un costo directo correspondiente a un contribuyente
   que pierde tiempo en la línea para prometer una donación, de modo que:

$$c_w = 0$$

   Así pues, el costo por hora de los clientes en el sistema es:

$$
\begin{aligned}
\left\{\begin{array}{c}\text{costo total de}\\ \text{la espera}\end{array}\right\} &= \left\{\begin{array}{c}\text{costo de la}\\ \text{espera}\end{array}\right\} * \left\{\begin{array}{c}\text{número de clientes}\\ \text{en el sistema}\end{array}\right\}\\
&= c_w * L\\
&= 0 * 11.2439\\
&= \$0 \text{ por hora}
\end{aligned}
$$

3. **Costo por pérdida de un cliente:** Aquí es necesario estimar cuánto dinero se pierde cuando una
   persona llama y obtiene una señal de ocupado y no puede hacer una contribución. La gerencia de
   NPTV sabe, por experiencias pasadas, que la donación promedio por llamada es de $50. Sin embargo,
   esta cantidad no siempre se pierde cuando un contribuyente no puede hacer la llamada, pues el 80%
   de ellos intentará llamar de nuevo. El costo por la pérdida de un cliente en este caso es,
   entonces:

$$
\begin{aligned}
c_d &= (\text{por llamada}) * (\text{probabilidad de perder la llamada})\\
&= 50 * 0.20\\
&= \$10.00 \text{ por negación}
\end{aligned}
$$

## Página derecha — pág. 747 del libro

13.6 ANÁLISIS DE OTROS MODELOS DE COLAS USANDO LA COMPUTADORA — 747

Esta cifra representa un costo de negación de servicio *por cada cliente*. Para calcular el costo
por hora, es necesario saber a *cuántos clientes* se les niega el servicio por hora. Recuerde que la
tasa de llegadas es λ = 150 llamadas por hora y que la probabilidad de que a un cliente se le niegue
el servicio es $p_d = 0.1005$ (véase la figura 13.15). En promedio, entonces, 150 * 0.1005 = 15.075
clientes no obtienen servicio cada hora. Así pues, el costo por hora de pérdida de negación es:

$$
\begin{aligned}
\left\{\begin{array}{c}\text{Costo total}\\ \text{por negación}\end{array}\right\} &= \left\{\begin{array}{c}\text{costo por}\\ \text{negación}\end{array}\right\} * \left\{\begin{array}{c}\text{número de}\\ \text{llegadas}\end{array}\right\} * \left\{\begin{array}{c}\text{probabilidad}\\ \text{de negación}\\ \text{de servicio}\end{array}\right\}\\
&= c_d * \lambda * p_d\\
&= 10 * 150 * 0.1005\\
&= \$150.75 \text{ por hora}
\end{aligned}
$$

Estos tres componentes de costo se suman para obtener el costo total por hora para el primer sistema
con 15 líneas y sin capacidad de espera:

$$
\begin{aligned}
\text{Costo total} &= (\text{costo de los servidores}) + (\text{costo de la espera}) +\\
&\quad\ (\text{costo de la negación del servicio})\\
&= (c_s * c) + (c_w * L) + (c_d * \lambda * p_d)\\
&= (1.25 * 15) + (0 * 11.2439) + (10.00 * 150 * 0.1005)\\
&= 18.75 + 0 + 150.75\\
&= \$169.50 \text{ por hora}
\end{aligned}
$$

Un análisis parecido se puede efectuar, ahora, para los restantes cinco sistemas telefónicos. Los
resultados se resumen en la tabla 13.5. Observe el costo total por hora de cada sistema en la línea
final de dicha tabla. Los costos indican que resulta más económico tener un sistema con 20 líneas y
capacidad de espera de hasta cinco llamadas, con un costo total por hora de $34.90 (sistema 4).

**TABLA 13.5 Análisis económico de los sistemas de seis teléfonos para el problema de NPTV**

*(Encabezado de columnas agrupado bajo el rótulo **SISTEMA**.)*

| | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Número de filas | 15 | 20 | 15 | 20 | 15 | 20 |
| Capacidad de espera | 0 | 0 | 5 | 5 | 10 | 10 |
| $c_s$ | 1.25 | 1.375 | 1.50 | 1.65 | 1.875 | 2.0625 |
| $c_w$ | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| $c_d$ | 10.00 | 10.00 | 10.00 | 10.00 | 10.00 | 10.00 |
| $L$ | 11.235 | 12.331 | 12.722 | 12.527 | 13.565 | 12.555 |
| $p_d$ | 0.1005 | 0.0135 | 0.0311 | 0.0013 | 0.0114 | 0.0001 |
| Costo total ($/hr) | 169.50 | 47.78 | 69.08 | 34.90 | 45.26 | 41.43 |

---

--- pág. 60 ---
*(páginas impresas 748 y 749; manuscrito: **58**)*

## Página izquierda — pág. 748 del libro

748 — CAPÍTULO 13 MODELOS DE COLAS

### 13.6.3 Un sistema de colas con una distribución de tiempo de servicio general (M/G/c)

En todos los sistemas de colas analizados hasta este punto, el tiempo de servicio se supone que
sigue una distribución exponencial con una tasa de servicio media conocida de μ. En algunos modelos,
sin embargo, esta suposición puede no ser válida. Un ejemplo extremo es cuando el tiempo de servicio
es determinístico, esto es, cuando cada cliente requiere la misma cantidad conocida de tiempo de
servicio (como en el caso de una línea de ensamblaje con un ciclo de tiempo fijo). Incluso cuando el
tiempo de servicio es probabilístico, usted puede no conocer su distribución o ésta puede no ser
exponencial. En tales casos, se puede utilizar un análisis de colas apropiado mediante la
identificación del proceso de servicio como "general" (G).

> ### CARACTERÍSTICAS CLAVE
>
> Para obtener medidas de rendimiento en cuanto a tales sistemas, además de la tasa de llegada
> promedio de λ, usted debe estimar:
>
> ✓ La cantidad promedio de tiempo por servicio.
> ✓ La desviación estándar del tiempo de servicio, que proporciona una medida de su variabilidad.
>   (Observe que una desviación estándar de cero corresponde a un tiempo de servicio determinístico.)

Considere el problema de la división Los Álamos de la Oficina de Control de Vehículos de Motor de
Texas.

**EJEMPLO 13.4 EL PROBLEMA DE COLAS DE LA OFICINA DE CONTROL DE VEHÍCULOS DE MOTOR DE TEXAS** La
división de Los Álamos actualmente tiene tres servidores públicos que procesan el registro de
automóviles. Recientemente, han recibido quejas de los clientes que tienen que esperar demasiado
durante la hora del almuerzo, de 11:30 a 13:30 horas. Para minimizar el problema, usted, como
administrador de la oficina, está tratando de determinar cuántos empleados adicionales debe
contratar para este periodo de dos horas, de modo que el tiempo de espera sea menor a los 10
minutos. ■

> *Nota al margen:* **Formación de cola EX13_4.DAT** *(icono de disquete)*

La llegada de clientes podría suponerse, razonablemente, que sigue un proceso de Poisson. Basándose
en datos históricos, usted estima que la tasa promedio de llegadas es λ = 46 personas por hora. A
pesar de que no tiene certeza sobre la distribución del tiempo de servicio, un estudio del tiempo ha
revelado que cada servidor necesita un promedio de cinco minutos (0.08333 horas) para atender a un
cliente, con una desviación estándar de dos minutos (0.0333 horas).

Estos datos indican que cada servidor puede procesar un promedio de μ = 12 clientes por hora. Así
pues, para manejar la estimación pico de 46 clientes por hora, es decir, asegurar que la tasa total
de servicio, $c * \mu$, excede a la tasa total de llegadas, λ, es necesario tener al menos cuatro
ventanillas en servicio. Al introducir estos datos en el paquete de software STORM, utilizando un
modelo *M/G/4* (para indicar que la distribución de tiempo de servicio no es exponencial) produce
las medidas de rendimiento dadas en la figura 13.16. Usted puede ver que existe un promedio de 12
clientes en la cola y que cada uno de ellos tiene que esperar un promedio de 0.2636 horas (apro-

## Página derecha — pág. 749 del libro

13.6 ANÁLISIS DE OTROS MODELOS DE COLAS USANDO LA COMPUTADORA — 749

```
                 M/G/4 : M / G / C
             Q U E U E   S T A T I S T I C S

  Number of identical servers . . . . . . . . .        4
  Mean arrival rate . . . . . . . . . . . . . .  46.0000
  Mean service rate per server  . . . . . . . .  12.0000
  Standard deviation of service time  . . . . .   0.0333

  Mean server utilization (%) . . . . . . . . .  95.8330
  Expected number of customers in queue . . . .  12.1272
  Expected number of customers in system  . . .  15.9605
  Probability that a customer must wait . . . .   0.9092
  Expected time in the queue  . . . . . . . . .   0.2636
  Expected time in the system . . . . . . . . .   0.3470
```

Figura 13.16 Medidas de rendimiento obtenidas con STORM para el problema *M/G/4* de Texas BMV.

ximadamente 16 minutos) antes de ser atendidos. En total, cada cliente tiene que invertir 0.3470
horas (aproximadamente 21 minutos) en la oficina.

Este nivel de servicio no es aceptable porque el tiempo promedio de espera de 16 minutos excede al
objetivo de 10 minutos. Por consiguiente, es necesario tener al menos cinco ventanillas en
funcionamiento. Al cambiar el número de servidores de 4 a 5 y resolver el nuevo modelo *M/G/5*, se
obtienen los resultados mostrados en la figura 13.17. Usted puede ver que con cinco ventanillas
abiertas, el tiempo promedio de espera en la cola disminuye a 0.0204 horas, un poco más de un
minuto. Esto está completamente dentro del propósito de los diez minutos, de modo que usted decide
aumentar el número de servidores públicos de 3 a 5, durante el tiempo del almuerzo.

En la presente sección, usted ha visto cómo la computadora obtiene medidas de rendimiento para
algunos de los sistemas de colas que se presentan más comúnmente

```
                 M/G/5 : M / G / C
             Q U E U E   S T A T I S T I C S

  Number of identical servers . . . . . . . . .        5
  Mean arrival rate . . . . . . . . . . . . . .  46.0000
  Mean service rate per server  . . . . . . . .  12.0000
  Standard deviation of service time  . . . . .   0.0333

  Mean server utilization (%) . . . . . . . . .  76.6664
  Expected number of customers in queue . . . .   0.9369
  Expected number of customers in system  . . .   4.7702
  Probability that a customer must wait . . . .   0.4916
  Expected time in the queue  . . . . . . . . .   0.0204
  Expected time in the system . . . . . . . . .   0.1037
```

Figura 13.17 Medidas de rendimiento obtenidas con STORM para el problema *M/G/5* de Texas BMV.

---

*(Fin de la transcripción de las páginas 41 a 60 del PDF.)*
