# Podcast SIM 8 de 8 — AnyLogic, cultura de cátedra y las trampas del multiple choice

Fuente para un episodio de podcast de estudio. Materia: Simulación (UTN, Ingeniería en
Sistemas, 4.º año). Sirve para el primer parcial, el sábado 7 de noviembre de 2026: integrado
teórico-práctico y probablemente multiple choice. Las respuestas del banco son la clave revisada
por nosotros, no la corrección oficial de la cátedra.

## Indicaciones para el episodio

Los tres paradigmas de AnyLogic y los bloques de la Process Modeling Library, las preguntas de cultura de cátedra (GIS, LaTeX, historia, POO) y, sobre todo, cómo pregunta la cátedra: las trampas típicas del multiple choice. Formato de repaso final, tipo quiz: plantear la pregunta, dar un momento y explicar la respuesta.

## Contenido principal

#### Cómo se toma: lo que muestra el parcial 2025

El parcial 2025 tuvo tres partes:

- 15 preguntas de opción múltiple, con opciones de la A a la E.
- 17 de verdadero/falso o de selección múltiple.
- Un ejercicio numérico de inventario.

Como el parcial es teórico-práctico, también puede caer una **traza a mano de la cola simple**. La plantilla está en las diapositivas de clase (§4.5).

**Siete reglas para el multiple choice**, sacadas de los errores del 2025:

1. **"A y B son correctas" casi nunca es la respuesta.** En 2025 fue correcta en 3 de 15 preguntas. Antes de marcarla, comprobá que **B sea verdadera sola**.
2. **Las palabras absolutas** (*siempre, solo, totalmente, asegura, nunca*) suelen hacer falsa la frase.
3. **"Según el texto"** quiere decir que la opción correcta es la **definición textual** del libro.
4. **Un dato de entrada no es una medida de rendimiento**, y **un cambio de estado no es un evento**.
5. **En selección múltiple, marcar de menos también resta.** Evaluá cada opción por separado.
6. **Leé cada palabra.** En 2025 una pregunta cambiaba "cociente" por "suma" y con eso la frase pasaba a ser falsa.
7. **Cuidado con la doble negación.** "La POO **no** es imprescindible" es **verdadero**.

### 10. AnyLogic y lo que hay alrededor

*Fuentes: AnyLogic in Three Days, The Art of Process-Centric Modeling, los tutoriales entregados y las consignas de los TP.*

#### 10.1 Los tres paradigmas

AnyLogic es **multimétodo**: permite combinar los tres paradigmas en un mismo modelo. El libro aclara que **cada método sirve para un rango de niveles de abstracción**.

| Paradigma | Cómo ve al sistema | Elementos | Modelo del libro |
|---|---|---|---|
| **Dinámica de sistemas** (Forrester, MIT, años 50) | como **agregados**: los ítems no se distinguen, solo importan las cantidades. Se usa para modelos estratégicos de largo plazo | **stocks** (acumulaciones: la memoria del sistema), **flujos** (tasas de cambio), lazos de **realimentación** | **SEIR**: una epidemia con susceptibles, expuestos, infectados y recuperados |
| **Eventos discretos** (GPSS, de Geoffrey Gordon en IBM, 1961) | como un **proceso**: entidades que pasan por operaciones y **compiten por recursos limitados**, así que casi siempre hay colas | diagrama de flujo de bloques: Source, Queue, Delay, Seize/Release, Sink | **Job Shop**: un taller con recepción, almacenamiento, máquinas y camiones |
| **Basado en agentes** | como **individuos** con comportamiento propio (a menudo con *statecharts*). El **comportamiento global emerge** de las interacciones | agentes, statecharts, entorno | **Mercado**: cómo se adopta un producto por publicidad y boca en boca |

El libro tiene un cuarto capítulo, **Peatones** (modelo *Airport*), pero **no es un paradigma**: es una biblioteca. Tampoco son paradigmas Road Traffic, Rail, Fluid, Material Handling ni GIS.

En la práctica entregamos tres modelos del libro (**SEIR, Job Shop y Airport**) y tres tutoriales de la ayuda:

- Supply Chain GIS;
- Subway Entrance Hall (peatones);
- Intersection (tránsito).

Detalles del libro que pueden caer:

- **Los agentes no tienen por qué ser personas**: pueden ser vehículos, máquinas, proyectos, ideas o empresas.
- Las salidas típicas de un modelo de eventos discretos son:
  - utilización de recursos;
  - tiempo en el sistema;
  - esperas;
  - largo de las colas;
  - *throughput*;
  - cuellos de botella.
- **El primer software de eventos discretos fue GPSS (1961), de Geoffrey Gordon.** Es el mismo Gordon de la bibliografía.

#### 10.2 M/M/1 en AnyLogic (Process-Centric Modeling)

| Bloque | Qué hace |
|---|---|
| **Source** | genera las llegadas, con `exponential(λ)`: es un proceso de Poisson |
| **Queue** | la cola |
| **Seize** | **toma** un recurso (el servidor) |
| **Delay** | el tiempo de servicio, con `exponential(μ)` |
| **Release** | **libera** el recurso |
| **ResourcePool** | el conjunto de servidores; define la capacidad $c$ |
| **Sink** | la salida del sistema |
| **TimeMeasureStart / End** | miden el tiempo en el sistema (o en la cola) |

Los promedios de clientes en el sistema y en la cola se llevan con objetos *Statistics*. El libro presenta las fórmulas de M/M/1 **para compararlas con lo simulado**.

Del cap. 2 del libro también conviene saber dos cosas:

- La diferencia entre simulaciones **terminales** (horizonte finito) y **no terminales** (estado estable, con un **período de calentamiento** que se descarta).
- Que la **ley de Little** vale también para estimar medidas a partir de la simulación.

#### 10.3 Cultura de cátedra

Son preguntas que en 2025 fueron 5 de 32:

- **GIS** (Sistema de Información Geográfica) es **multicapa**: superpone capas de datos sobre un mapa. "Monocapa" es **falso**. En AnyLogic es un espacio donde se ubican agentes sobre mapas reales.
- **LaTeX** es un sistema de composición de textos de alta calidad tipográfica, muy usado en artículos científicos con matemática. Los informes de los TP se hicieron en LaTeX, con la plantilla de Cornell en Overleaf.
- **La POO no es imprescindible para simular.** Ayuda a modelar entidades y agentes, pero se simula también en FORTRAN, en C o en una planilla. Law aclara que la mayoría de los paquetes de simulación no son realmente orientados a objetos.
- **Historia.** La simulación por computadora existe desde los **años 40** (Montecarlo y el Proyecto Manhattan). **No** "surgió en los últimos 30 años". GPSS es de 1961 y la dinámica de sistemas de los años 50.
- **Montecarlo** se asocia con la simulación de procesos **estocásticos**, aunque en su origen también se usó para problemas determinísticos. Un modelo de Montecarlo es **estático**.
- **Los TP de clase** (cola e inventario) son modelos simples que **se pueden simular y además tienen solución analítica**. Lo simulado se **compara** con lo analítico y da **parecido**. Para simular no hace falta conocer la solución analítica.

**Estadística básica** (del TP 1.1, la ruleta), que se tomó en 2025:

- **Media aritmética**: medida de tendencia central; es "el promedio".
- **Frecuencia absoluta** $f_i$: cuántas veces aparece un valor o evento en la muestra.
- **Frecuencia relativa**: el **cociente** $f_i / N$. Si el enunciado dice "suma", es **falso**.
- En la ruleta, la frecuencia relativa de un número **converge** a $1/37$ a medida que crecen las tiradas. Es la ley de los grandes números vista en la práctica.

### 11. Las 25 trampas, una por línea

1. **Sistema**, **modelo** y **simulación** son cosas distintas.
2. La solución analítica es **exacta**. La simulación **no la reemplaza**: la complementa.
3. Para simular hacen falta datos o estimaciones. No hacen falta POO ni computadora para todo modelo.
4. Un modelo **no** tiene que estar "totalmente testeado" para usarse.
5. La ventaja del *next-event* es **saltear la inactividad**.
6. Los eventos de la cola son **arribo y partida**. "Servidor ocupado" es un estado.
7. Las medidas de Law son demora **en cola**, número **en cola** y **utilización**.
8. La demora **no incluye** el tiempo de servicio.
9. La política (s, S) **no** garantiza que $I$ quede entre $s$ y $S$, porque puede ser negativo.
10. $h$ va con $I^+$ y $\pi$ con $I^-$. Si no se pide, **no se paga $K$**.
11. Al subir $S$ sube el mantenimiento y bajan el faltante y el pedido. Una sola corrida **no alcanza** para elegir la política.
12. **Paso 2 de Weitz**: modelo de simulación **base**. Recolección de datos es el paso 3.
13. Verificar es comprobar el **programa**. Validar es comparar con la **realidad**.
14. Con **población finita**, la tasa de llegadas **baja** cuando sube el número de clientes en el sistema.
15. $\rho = \lambda/\mu$. **Estable si $\mu > \lambda$.** $P_0 = 1 - \rho$.
16. En Kendall la segunda letra es el **servicio**, y K es la capacidad del **sistema**.
17. La **suma de Bernoulli** es binomial. La **geométrica** cuenta el número del intento del primer éxito: $E = 1/p$.
18. De binomial a Poisson con $\lambda = np$, **sin umbrales fijos**.
19. $\mathrm{Var}(aX + b) = a^2\,\mathrm{Var}(X)$. $\mathrm{Var}(\bar X) = \sigma^2/n$ **necesita independencia**.
20. En la ley de los grandes números lo que crece es **$n$**, no el tiempo.
21. **Los tiempos entre arribos son exponenciales.** La cantidad de arribos es Poisson.
22. **Poisson no homogéneo**: $\lambda(t)$ varía; los incrementos siguen **independientes** pero dejan de ser **estacionarios**.
23. **Período completo** quiere decir $p = m$. Los cuadrados centrales **no están vigentes**. Los pseudoaleatorios se prefieren por velocidad y reproducibilidad.
24. Hay **dos tipos** de prueba de aleatoriedad: empíricas y teóricas. Chi-cuadrado o póker son pruebas, no tipos.
25. Los paradigmas de AnyLogic son **tres**: agentes, dinámica de sistemas y eventos discretos. Peatones y GIS no lo son. GIS es **multicapa**.

## Ampliación

### Cómo pregunta la cátedra (patrones del 2025)

1. **"Según el texto"** = Law cap. 1 o Ross cap. 2 **textual**. La opción correcta repite la definición del libro palabra por palabra.
2. **Las opciones "A y B" o "todas" son la trampa más usada.** En la parte 1 fue correcta en 3 de 15 (1.1, 1.5 y 1.14). En las otras 12 la respuesta era una sola. Antes de marcar "A y B", **probá que B sea verdadera por sí sola**.
3. **Palabras absolutas = casi siempre falsa**: "siempre", "solo", "totalmente", "exacta" (salvo la solución analítica), "asegura". Lo vimos en 1.3 D, 1.12 C y D, 2.3 y 2.4.
4. **Confunde lo que sale de un modelo con lo que entra**: tiempo de servicio o de arribo como "medida de rendimiento" (1.2 A, 2.13 B), o un cambio de estado como "evento" (2.12 E).
5. **Confunde sistema / modelo / simulación** (1.4) y **verificación / validación** (1.10).
6. **Doble negación** en V/F: "la POO **no** es imprescindible" (2.6). Leela despacio.
7. **Cultura de cátedra**: AnyLogic (paradigmas, GIS), LaTeX e historia de la simulación. Son 5 de 32, regaladas si las leíste.
8. **En la selección múltiple marcar de menos también resta** (2.11).

## Preguntas de parcial y de práctica sobre este tema

**2.6** (parcial 2025) **La programación orientada a objetos no es imprescindible para simular.** → ✅ **V**
Se simula en FORTRAN, en C, en una planilla o a mano, como la cola simple de Law. La POO **ayuda** a modelar entidades y agentes, pero no es imprescindible. El alumno marcó F: **error**. Cuidado con la doble negación del enunciado.

**2.8** (parcial 2025) **LaTeX es un sistema de composición de textos de alta calidad tipográfica, muy usado en artículos científicos con matemática.** → ✅ **V**

**2.16** (parcial 2025) **Paradigmas explicados en *AnyLogic en 3 días*.** → ✅ **A, B y C**
Basado en agentes, dinámica de sistemas y eventos discretos son **los tres paradigmas** de AnyLogic. Peatones, caminos (Road Traffic) y GIS son **bibliotecas o espacios**, no paradigmas. En otra versión de la pregunta aparece también "Sistemas en tiempo real", que es otro distractor. La fuente es la pág. 13 de *AnyLogic in 3 days*: *"There are three methods: System Dynamics, Discrete Event Modeling and Agent-Based Modeling"*.

**2.17** (parcial 2025) **GIS es un sistema geográfico monocapa para analizar cuestiones de una zona particular.** → ✅ **F**
Un Sistema de Información Geográfica es justamente **multicapa**: superpone capas de datos georreferenciados, como calles, población y redes. El alumno marcó V: error. *(Conocimiento general.)*

**E10** (pregunta inventada por alumnos de 2025) En AnyLogic, **Source**: A) genera llegadas · B) es la cola · C) libera recursos · D) mide el tiempo en el sistema

→ Respuesta: **A**

**E11** (pregunta inventada por alumnos de 2025) Para medir el **tiempo en el sistema** en AnyLogic se usan: A) TimeMeasureStart y TimeMeasureEnd · B) ResourcePool · C) Delay con histogramas · D) Sink

→ Respuesta: **A**

**E12** (pregunta inventada por alumnos de 2025) **Seize** en AnyLogic: A) genera llegadas · B) registra esperas · C) captura un recurso (servidor) · D) libera al servidor

→ Respuesta: **C**. D es **Release**

**P33** (práctica, no oficial) Según *AnyLogic in 3 Days*, la **dinámica de sistemas**: A) trabaja con agregados (stocks y flujos) y una abstracción alta · B) modela cada individuo · C) se usa para el detalle físico · D) fue creada por Gordon en 1961 · E) B y C

→ Respuesta: **A**. Forrester, años 50. D describe a GPSS y al DES.

**P34** (práctica, no oficial) En DES, el primer software fue: A) AnyLogic · B) GPSS, de Geoffrey Gordon (IBM, 1961) · C) Arena · D) Excel · E) Mathematica

→ Respuesta: **B**.

**P35** (práctica, no oficial) V o F: en un modelo basado en agentes, los agentes tienen que ser personas.

→ Respuesta: **F**. Pueden ser vehículos, máquinas, ideas o empresas.

**P36** (práctica, no oficial) En la Process Modeling Library, el bloque que **libera** un recurso es: A) Seize · B) Delay · C) Release · D) Sink · E) Source

→ Respuesta: **C**.

**P37** (práctica, no oficial) En AnyLogic, el tiempo de servicio de una M/M/1 se modela con: A) un Source con exponential(λ) · B) un Delay con exponential(μ) entre un Seize y un Release · C) un Sink · D) un ResourcePool sin bloques · E) A y C

→ Respuesta: **B**.
