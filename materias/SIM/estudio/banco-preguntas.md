# Banco de preguntas — Parcial 1 (multiple choice)

> **SIM · UTN-ISI · parcial del sábado 7/11/2026**
>
> El **parcial 2025-10-04** (tema 404) es el único multiple choice que hay guardado, así que este banco sale de ahí. Lo reviso pregunta por pregunta con **la clave corregida**: la copia que circula tiene marcadas las respuestas de un alumno, y **en 14 de las 32 preguntas no coinciden con la teoría** (más una discutible). Al final hay preguntas de práctica que escribí yo con el mismo estilo, para cubrir lo que entra este año (Ross cap. 2) y en 2025 no se tomó.

## Cómo usar este banco

- **Fuente oficial**: `fuentes/examenes/parciales/2025/2025-10-04.pdf`, revisado contra las fotos del original. La transcripción completa con todas las opciones está en `banco-examenes.md`.
- **Clave**: la puse yo con la teoría de la wiki, el apunte de Weitz y el resumen de Law y Ross. **No es la corrección de la cátedra**, porque esa no la tenemos.
- **Seguridad** de cada respuesta:
  - ● **firme**: sale textual de la bibliografía.
  - ◐ **discutible**: hay dos lecturas razonables. Explico cuál elegir y por qué.
- Las marcadas por el alumno van como *"alumno: X"*. ❌ quiere decir que esa respuesta está mal.
- **Validación externa**: el resumen de alumnos 2025 (`fuentes/resumenes/Resumen Simulación 2025 (con preguntas de parcial).docx`) trae varias de estas mismas preguntas con sus respuestas: 2.1, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.10, 2.12, 2.14, 2.16 y 2.17. **Coinciden todas con esta clave**, incluidas las que el alumno de la foto erró: 2.1, 2.6, 2.9, 2.10, 2.12 y 2.17. Para la 2.11 también ponen A, C y D, con un "ni idea, ponele".

## Clave rápida

| Nº | Tema | Clave | Alumno | Seg. |
|---|---|---|---|---|
| 1.1 | Geométrica | **D** (A y B) | D ✅ | ● |
| 1.2 | Medidas de la cola simple | **B** | E ❌ | ● |
| 1.3 | Política (s, S) | **B** | E ❌ | ● |
| 1.4 | Definición de sistema | **B** | E ❌ | ● |
| 1.5 | Proceso de Poisson homogéneo | **D** (todas) | D ✅ | ● |
| 1.6 | Población finita | **C** | A ❌ | ● |
| 1.7 | Intensidad de tráfico | **B** | B ✅ | ● |
| 1.8 | Estado estable M/M/1 | **B** | B ✅ | ● |
| 1.9 | Ventaja del next-event | **B** | E ❌ | ● |
| 1.10 | Verificación vs. validación | **A** (E defendible) | E | ◐ |
| 1.11 | Next-event: inactividad | **B** | B ✅ | ● |
| 1.12 | Binomial → Poisson | **A** | E ❌ | ● |
| 1.13 | Poisson no homogéneo | **A** (D defendible) | A ✅ | ◐ |
| 1.14 | Para qué sirven los nº aleatorios | **E** (todas) | E ✅ | ● |
| 1.15 | Segundo paso del estudio | **B** | B ✅ | ● |
| 2.1 | Simulación reemplaza a lo analítico | **F** | V ❌ | ● |
| 2.2 | Hace falta información de la realidad | **V** | V ✅ | ● |
| 2.3 | Modelo solo usable si está totalmente testeado | **F** | F ✅ | ● |
| 2.4 | Siempre hacen falta herramientas informáticas | **F** | F ✅ | ● |
| 2.5 | La simulación surgió en los últimos 30 años | **F** | F ✅ | ● |
| 2.6 | La POO no es imprescindible | **V** | F ❌ | ● |
| 2.7 | La solución analítica es exacta | **V** | V ✅ | ● |
| 2.8 | LaTeX | **V** | V ✅ | ● |
| 2.9 | Pseudoaleatorios | **A, D** | A, B, C ❌ | ● |
| 2.10 | Verdaderos aleatorios | **B** | A, B ❌ | ● |
| 2.11 | Cola simple e inventario de los TP | **A, C, D** | A ❌ (incompleta) | ◐ |
| 2.12 | Eventos de la cola simple | **A, B** | A, B, E ❌ | ● |
| 2.13 | Medidas de la cola simple | **A, D** | A, B, D ❌ | ◐ |
| 2.14 | λ > μ ⇒ no se puede simular | **F** | F ✅ | ● |
| 2.15 | λ < μ ⇒ no hay solución analítica | **F** | F ✅ | ● |
| 2.16 | Paradigmas de *AnyLogic en 3 días* | **A, B, C** | A, B, C ✅ | ● |
| 2.17 | GIS es monocapa | **F** | V ❌ | ● |
| 3 | Costo total promedio mensual (inventario) | ver Parte 3 | — | ◐ |

**De qué temas salen las 32**: colas 8, Law cap. 1 (sistema, modelo, DES, pasos, analítico vs. simulación) 11, probabilidad y proceso de Poisson 4, números aleatorios 3, inventario 1 y "cultura de cátedra" (AnyLogic, GIS, LaTeX, POO, historia) 5. El ejercicio 3 es de inventario.

## Parte 1 — Opción múltiple (15)

**1.1 ¿Qué propiedad caracteriza a una variable aleatoria geométrica?**
A) número de ensayos hasta el primer éxito · B) $E=1/p$, $\mathrm{Var}=(1-p)/p^2$ · C) es suma de Bernoulli independientes · D) A y B · E) todas

✅ **D.** A y B son la definición de Ross y sus momentos. C es falsa: la **suma de Bernoulli independientes es la binomial**, no la geométrica.
*Unidad 6, §2.8 de Ross.*

**1.2 En la cola de un servidor, ¿cuáles son las tres medidas de rendimiento principales que se estiman?**
A) tiempo promedio de servicio, nº promedio en el sistema, utilización · B) retraso promedio en cola, nº promedio en cola, proporción de tiempo que el servidor está ocupado · C) llegada/salida/longitud · D) solo retraso y utilización · E) A y B

✅ **B**, sin dudas. Son las tres de Law: $d(n)$ demora promedio en cola, $q(n)$ número promedio en cola y $u(n)$ utilización. **A es la trampa**: mezcla el tiempo de servicio, que es un dato de entrada, y el número en el **sistema**, cuando Law mide en la **cola**.
*Unidad 3, "Las tres medidas de rendimiento".*

**1.3 ¿Qué representa la política (s, S)?**
A) ordenar fijo s al llegar a S · B) si $I<s$ pedir hasta S; si $I\ge s$ no pedir · C) pedir s cada S períodos · D) asegura que el inventario siempre está entre s y S · E) B y D

✅ **B.** D es falsa. Entre dos revisiones el inventario puede caer muy por debajo de $s$, y como hay backlog puede quedar **negativo**. La política no garantiza ningún rango. Tampoco es que se pidan $S$ unidades: se pide $Z = S - I$.
*Unidad 4, "Política de reordenamiento (s, S)".*

**1.4 "Según el texto", ¿cuál es la definición de sistema?**
A) conjunto de ecuaciones · B) colección de entidades que actúan e interactúan hacia el logro de algún fin lógico · C) modelo computacional que imita · D) algoritmo de nº aleatorios · E) todas

✅ **B**, la definición textual de Law (Schmidt y Taylor). A describe un **modelo matemático** y C una **simulación**. "Todas" es la trampa de no distinguir **sistema / modelo / simulación**.
*Unidad 1, "Conceptos clave".*

**1.5 Proceso de Poisson homogéneo de tasa λ: ¿qué condición lo define?**
A) $N(0)=0$ e incrementos independientes · B) la distribución del nº de eventos depende solo de la longitud del intervalo · C) $\lim_{h\to0} P\{N(h)=1\}/h=\lambda$ · D) todas · E) A y C

✅ **D.** A, B y C son tres de las cinco condiciones de Ross. Falta $\lim P\{N(h)\ge 2\}/h = 0$, que no está entre las opciones. **B es la que distingue al homogéneo**, porque son los incrementos estacionarios.
*Unidad 6, §6.10 · `resumen-probabilidad.md` §5.2.*

**1.6 Con población de clientes finita, la tasa de llegada…**
A) varía con el tiempo · B) aumenta con el nº de clientes en el sistema · C) disminuye conforme aumenta el nº de clientes en el sistema · D) es constante · E) A y C

✅ **C**, textual del recuadro "Características clave" de Weitz (cap. 13): *"con un número finito de clientes, la tasa de llegadas disminuye conforme aumenta el número de clientes en el sistema"*. La tasa depende del **estado**, de cuántos clientes ya entraron, y no del reloj. Por eso A no es la característica.
*Unidad 8 · `resumen-colas.md` §2.1.*

**1.7 ¿Qué es la intensidad de tráfico ρ?**
✅ **B**: $\rho=\lambda/\mu$. D es falsa porque la probabilidad de sistema vacío es $P_0 = 1-\rho$, no $\rho$. Con $c$ servidores, $\rho = \lambda/(c\mu)$.
*`resumen-colas.md` §4.*

**1.8 Condición de estado estable en M/M/1**
✅ **B**: $\mu>\lambda$, o sea $\rho<1$. Si $\lambda \ge \mu$ la cola crece sin límite y no hay estado estable.

**1.9 Principal ventaja del next-event time advance**
A) más precisión · B) salta los períodos de inactividad y ahorra cómputo · C) más fácil de programar · D) resultados más estables · E) B y C

✅ **B.** Law no dice en ningún lado que sea "más fácil de programar". Lo que dice es que lo usa casi todo el software comercial, que no es lo mismo. Con "principal ventaja" la respuesta es una sola.
*Unidad 2, "Mecanismos de avance del tiempo".*

**1.10 Principal diferencia entre verificación y validación**
A) la verificación comprueba que el modelo funcione correctamente; la validación lo compara con la realidad · B) la verificación se hace antes que la validación · C) la verificación usa datos reales · D) la verificación es opcional · E) A y B

◐ **A.** A es la diferencia conceptual: **verificar** es preguntar si el programa hace lo que quise programar, o sea debugging. **Validar** es preguntar si el modelo representa al sistema real.
Sobre B: en los 10 pasos de **Weitz**, la verificación (paso 5) va antes que la validación (paso 6). En **Law** hay una validación antes de programar, la del documento de supuestos (paso 3), y otra después (paso 6). Si la cátedra piensa con la lista de Weitz, que es la que usa en la 1.15, puede tomar B como verdadera y la clave sería **E**.
**Criterio:** si el enunciado pregunta por la *diferencia*, marcá A. Si alguna vez pregunta "¿cuál de estas afirmaciones es verdadera?", B también lo es según Weitz.
*Unidad 5.*

**1.11 En el next-event, ¿qué pasa con los períodos de inactividad?**
✅ **B**: se saltan y el reloj va directo al próximo evento. A describe el **incremento fijo**.

**1.12 Relación binomial–Poisson con n grande y p chico**
A) la binomial se aproxima a una Poisson con $\lambda=np$ · B) misma varianza · C) la Poisson es siempre aproximación exacta · D) solo cuando $n>100$ y $p<0{,}1$ · E) A y D

✅ **A.** D es falsa por el **"solo"**: Ross habla de "n grande, p chico", sin umbral. Esos umbrales son reglas prácticas y cambian según el libro. B también es falsa: $np(1-p)\neq np$, aunque se acercan cuando $p\to0$. C es falsa por el "siempre exacta".
*Unidad 6.*

**1.13 ¿Qué distingue al Poisson no homogéneo del homogéneo?**
A) la tasa λ varía en función del tiempo · B) los intervalos entre eventos no son exponenciales · C) no se mantienen los incrementos independientes · D) A y B · E) todas

◐ **A.** Es la definición de Ross: la intensidad $\lambda(t)$ depende de $t$.
C es **falsa**: el no homogéneo **mantiene** los incrementos independientes, y lo que pierde es la estacionariedad.
B es técnicamente **cierta**: con $\lambda(t)$ variable, los tiempos entre eventos dejan de ser exponenciales i.i.d. Pero Ross no lo dice en el cap. 2 y el profe no lo dio. Marcá **A**. Si en una variante aparece "A y B" junto a "todas", **"todas" es seguro falsa por C**.
*Unidad 6, §6.10 · `resumen-probabilidad.md` §5.3.*

**1.14 ¿Propósito principal de los números aleatorios?**
✅ **E**, todas. Generan variables con distribuciones arbitrarias, porque toda VA sale de una $U(0,1)$ transformada. Simulan las ocurrencias del modelo probabilístico. Y son la base de cualquier estudio de simulación estocástica.
*Unidad 7.*

**1.15 ¿Cuál es el segundo paso de un estudio de simulación?**
✅ **B**, generación del modelo de simulación base. Es la lista de **Weitz**: 1 definición del sistema → **2 modelo base** → 3 recolección y análisis de datos → 4 modelo preliminar → 5 verificación → 6 validación → 7 modelo final → 8 escenarios → 9 sensibilidad → 10 documentación.
**Ojo:** en **Law** el paso 2 es "recopilar datos y definir el modelo". Por eso existe la opción A como trampa. Como las opciones usan el vocabulario de Weitz, la respuesta es B.
*Unidad 5.*

## Parte 2 — Verdadero/falso y selección múltiple (17)

**2.1 La simulación reemplaza a la solución analítica para resolver problemas complejos con solución.** → ✅ **F**
Si hay solución analítica, **se usa**. Simulación y métodos analíticos son **complementarios**: la simulación se justifica cuando no hay solución cerrada. El alumno marcó V: error.

**2.2 Para simular hace falta información del funcionamiento de la realidad o estimaciones.** → ✅ **V**
Sin datos o estimaciones no hay distribuciones de entrada. Es el paso 3 de Weitz.

**2.3 Un modelo es un recorte de la realidad y solo puede usarse si está totalmente testeado.** → ✅ **F**
La primera mitad es cierta. La trampa es el "totalmente": ningún modelo está totalmente probado, y se usa una vez **validado** para el objetivo del estudio.

**2.4 Para construir modelos siempre hacen falta herramientas informáticas.** → ✅ **F**
Hay modelos **físicos**, como maquetas, y modelos **matemáticos** que se resuelven analíticamente a mano.

**2.5 La simulación por computadora surgió en los últimos 30 años.** → ✅ **F**
Viene de los años 40, con el método de Montecarlo en el Proyecto Manhattan (von Neumann y Ulam). Von Neumann propuso el método de los cuadrados centrales en 1946. *(Conocimiento general: no está en la wiki.)*

**2.6 La programación orientada a objetos no es imprescindible para simular.** → ✅ **V**
Se simula en FORTRAN, en C, en una planilla o a mano, como la cola simple de Law. La POO **ayuda** a modelar entidades y agentes, pero no es imprescindible. El alumno marcó F: **error**. Cuidado con la doble negación del enunciado.

**2.7 La solución analítica es exacta.** → ✅ **V**
Law: si el modelo es simple, se puede obtener una solución analítica **exacta**. La simulación da **estimaciones**.

**2.8 LaTeX es un sistema de composición de textos de alta calidad tipográfica, muy usado en artículos científicos con matemática.** → ✅ **V**

**2.9 Sobre los números pseudoaleatorios… (puede haber más de una correcta)**
- A) se generan secuencialmente con un algoritmo determinístico → ✅ **V**
- B) "ciclo completo" es cuando repite siempre el mismo número tras generar muchos distintos → ❌ **F**. El **período completo** es $p=m$: el generador recorre **todos** los valores posibles antes de repetir. Lo que describe la opción es una **degeneración**, como el cero que se propaga en el método de los cuadrados centrales.
- C) el método de la parte media del cuadrado sigue vigente → ❌ **F**. Cae en ciclos cortos y en cero, y no cumple uniformidad ni independencia. Es histórico.
- D) se pueden generar con cualquier computadora a altas velocidades → ✅ **V**. Velocidad y poco almacenamiento son propiedades de un buen generador.

**Clave: A y D.** El alumno marcó A, B y C: dos de más y una de menos.
*Unidad 7, §7.1 a §7.4.*

**2.10 Verdaderos números aleatorios.**
- A) en simulaciones de alto rendimiento es preferible usar verdaderos aleatorios y no pseudoaleatorios → ❌ **F**. Los verdaderos son **lentos, caros y no reproducibles**. Para simular se prefieren los pseudoaleatorios: rápidos y **reproducibles** con la misma semilla, que es lo que permite comparar escenarios.
- B) se basan en una fuente física de aleatoriedad, cuántica o caótica → ✅ **V**, textual de la Unidad 7.

**Clave: B.**

**2.11 Los modelos de cola simple e inventario de los TP de clase…**
- A) son modelos simples que pueden simularse y además tienen solución analítica → ✅
- B) solo pueden simularse si se tiene la solución analítica → ❌
- C) la solución analítica puede compararse con las respuestas de la simulación → ✅. Es lo que hicieron en el TP 3: M/M/1 simulado contra teórico.
- D) las respuestas de las simulaciones suelen ser parecidas a la solución analítica → ✅

◐ **Clave: A, C y D.** El alumno marcó solo A. En selección múltiple, **marcar de menos también resta**. La única duda es si la cátedra considera "analítico" al inventario (s, S); para la cola M/M/1 no hay discusión.

**2.12 En DES, los eventos de la cola simple son…**
A) arribo · B) partida · C) inicio · D) finalización · E) poner el servidor ocupado/desocupado

✅ **A y B.** E **no es un evento**: es un cambio de **estado** que producen el arribo y la partida.
C) La inicialización es una rutina, no un evento.
D) Solo existiría si la corrida terminara a tiempo fijo, con un evento "fin de simulación" como tercer tipo. En el modelo de Law la cola simple corta por $n$ demoras y tiene dos tipos de evento.
*Unidad 3, "Variables de estado y eventos".*

**2.13 Las medidas de rendimiento más importantes de la cola simple son…**
A) tiempo de espera "en el servidor" · B) tiempo de arribo · C) veces que el cliente pasó por el servidor · D) utilización del servidor

◐ **A y D.** A está mal redactada, pero apunta a la **demora en cola** $d(n)$. D es $u(n)$. B es un **dato de entrada**, no una medida, y C no tiene sentido en una cola simple. La tercera medida de Law, el **número promedio en cola** $q(n)$, no está entre las opciones.

**2.14 Si la tasa de arribos es mayor que la de servicio, no se puede simular.** → ✅ **F**
Se puede simular igual: la cola crece sin límite y no se alcanza el estado estable. Lo que no existe es la **solución analítica** de estado estable.

**2.15 Si la tasa de arribos es menor que la de servicio, no hay solución analítica.** → ✅ **F**
Es justamente al revés: con $\rho<1$ valen las fórmulas de M/M/1.

**2.16 Paradigmas explicados en *AnyLogic en 3 días*.** → ✅ **A, B y C**
Basado en agentes, dinámica de sistemas y eventos discretos son **los tres paradigmas** de AnyLogic. Peatones, caminos (Road Traffic) y GIS son **bibliotecas o espacios**, no paradigmas. En otra versión de la pregunta aparece también "Sistemas en tiempo real", que es otro distractor. La fuente es la pág. 13 de *AnyLogic in 3 days*: *"There are three methods: System Dynamics, Discrete Event Modeling and Agent-Based Modeling"*.

**2.17 GIS es un sistema geográfico monocapa para analizar cuestiones de una zona particular.** → ✅ **F**
Un Sistema de Información Geográfica es justamente **multicapa**: superpone capas de datos georreferenciados, como calles, población y redes. El alumno marcó V: error. *(Conocimiento general.)*

## Parte 2 bis — Otras preguntas reales de parcial (7)

El resumen de alumnos 2025 trae estas preguntas en su lista de "Preguntas Parciales" y **no están en la foto del tema 404**. Probablemente salen de otro tema o de otra fecha. La respuesta que daban los alumnos va entre paréntesis.

**2b.1 ¿Cuáles son algunas características de los generadores aleatorios verdaderos?**
A) solo generan conjuntos finitos · B) en general son menos prácticos que otros generadores · C) el tiempo de generación importa más que la calidad · D) están basados en algoritmos procesados en computadoras
✅ **B** (ellos: B). Son caros, lentos y no reproducibles. D describe a los **pseudo**aleatorios.

**2b.2 V/F: la frecuencia relativa se calcula como la *suma* de la frecuencia absoluta de algún valor entre el total de valores de la población o muestra.** → ✅ **F** (ellos: F)
La definición es el **cociente** $f_r = f_i/N$. El enunciado cambia "cociente" por "suma". Es una trampa de una sola palabra: leé cada palabra.

**2b.3 ¿Cuáles son los *tipos* de pruebas de aleatoriedad?**
A) empíricas · B) póker · C) bondad de ajuste · D) tests de Cooper · E) subidas y bajadas · F) teóricas · G) prueba de espera
✅ **A y F** (ellos: A y F). Law §7.4 dice que hay **dos tipos**:
- **Empíricas**: se aplican sobre los $U_i$ generados (chi-cuadrado, series, corridas, Kolmogórov-Smirnov).
- **Teóricas**: se aplican sobre los **parámetros** del generador, sin generar ningún número.
Póker, corridas o espera son **pruebas**, no tipos.

**2b.4 V/F: la media o promedio es una medida de tendencia central; la media aritmética es el promedio estándar.** → ✅ **V**

**2b.5 V/F: hacer tests sobre los valores de un generador pseudoaleatorio es obligatorio antes de usarlo en simulación.** → ✅ **V** (ellos: V)
Los generadores básicos caen en patrones o ciclos. Por eso existen los tests, y la pregunta frecuente #2 apunta a lo mismo.

**2b.6 V/F: se espera que los números pseudoaleatorios tengan un "comportamiento" similar al de los aleatorios verdaderos.** → ✅ **V**
Es el objetivo: que imiten las propiedades estadísticas de una muestra i.i.d. $U(0,1)$.

**2b.7 V/F: la frecuencia absoluta de un evento es el número de veces que se repite durante un experimento o muestra.** → ✅ **V**

> **Lección**: entran **preguntas de estadística básica** (media, frecuencia absoluta y relativa) que no están en ninguna unidad. Repasá esas definiciones exactas (§9 del resumen).

## Parte 2 ter — Preguntas inventadas por los alumnos de 2025, corregidas

Están en el mismo resumen bajo "Preguntas Extra (inventadas por nosotros)". **No son oficiales**, pero muestran qué consideraban probable. Van con la clave revisada. **Dos de sus respuestas estaban mal y las corregí.**

| # | Pregunta | Clave |
|---|---|---|
| E1 | El **Mersenne Twister** se destaca porque: A) período extremadamente largo · B) lo diseñó von Neumann en 1946 · C) es más lento que los GCL · D) está implementado en Python, R y Excel | **A y D**. Es de 1997, de Matsumoto y Nishimura |
| E2 | Característica deseable de un generador: A) período corto · B) patrones claros para depurar · C) alta velocidad · D) no reproducible | **C** |
| E3 | ¿Qué problema tenía **RANDU**? A) ceros perpetuos · B) las ternas caían en pocos planos · C) período infinito pero lento · D) no reproducible | **B**. A es el defecto de la parte media del cuadrado |
| E4 | El **método de rechazo** se usa cuando: A) la inversa de la FDA no tiene forma cerrada · B) la densidad es uniforme · C) se quiere reducir el cómputo · D) todas | **A** |
| E5 | El **método de composición**: A) usa trigonometría · B) combina distribuciones simples para formar una más compleja · C) es la transformada inversa · D) solo para exponenciales | **B** |
| E6 | La **exponencial**: A) modela tiempos entre eventos independientes · B) no tiene memoria · C) es la única continua sin memoria · D) solo para tiempos de servicio realistas | **A, B y C**. D es falsa: para servicio se usa **por conveniencia matemática**, no por realismo |
| E7 | ¿Cuáles son **discretas**? Normal · Binomial · Poisson · Hipergeométrica | **Binomial, Poisson e hipergeométrica** |
| E8 | La **normal** se genera con: A) transformada inversa · B) Box-Muller · C) TCL (sumar uniformes) · D) rechazo | ⚠️ Los alumnos ponían **B y C**. **También D es válida**: Ross genera la normal por rechazo con una exponencial. La A **no**, porque $\Phi$ no tiene inversa cerrada. Si es de opción única, B |
| E9 | Estabilidad M/M/1: A) λ>μ · B) λ<μ · C) λ=μ · D) siempre | **B** |
| E10 | En AnyLogic, **Source**: A) genera llegadas · B) es la cola · C) libera recursos · D) mide el tiempo en el sistema | **A** |
| E11 | Para medir el **tiempo en el sistema** en AnyLogic se usan: A) TimeMeasureStart y TimeMeasureEnd · B) ResourcePool · C) Delay con histogramas · D) Sink | **A** |
| E12 | **Seize** en AnyLogic: A) genera llegadas · B) registra esperas · C) captura un recurso (servidor) · D) libera al servidor | **C**. D es **Release** |
| E13 | **Montecarlo** se asocia principalmente con: A) procesos determinísticos · B) procesos estocásticos complejos · C) GIS · D) POO | ⚠️ Los alumnos ponían **A**, y está mal según su propio texto: *"el término Monte Carlo se asocia con la simulación de procesos estocásticos, aunque **originalmente** también se aplicaba a problemas determinísticos"*. **Clave: B** |
| E14 | Ventaja de los pseudoaleatorios frente a los verdaderos: A) más realistas · B) reproducibles y eficientes · C) no requieren semilla · D) nunca muestran patrones | **B** |
| E15 | Los **procesos de Markov** en simulación se representan con: A) tablas de frecuencias · B) matrices de transición de estados · C) uniformes · D) GIS | **B** |
| E16 | Un buen generador es: A) lento y preciso · B) rápido, reproducible y con buen comportamiento estadístico · C) basado en fenómenos físicos · D) de período corto | **B** |
| E17 | Característica de los **verdaderamente** aleatorios: A) algoritmos determinísticos · B) reproducibles con semilla · C) basados en fenómenos físicos como los cuánticos · D) ciclos cortos | **C** |
| E18 | ¿Qué condición **NO** es necesaria para el período completo de un GCL mixto? A) $m$ y $c$ primos relativos · B) $a-1$ divisible por todos los primos que dividen a $m$ · C) si 4 divide a $m$, 4 divide a $a-1$ · D) el multiplicador debe ser primo | **D**. Ojo: el resumen redacta mal la B, al revés. Lo correcto es "**todo primo que divide a $m$ divide a $a-1$**" |
| E19 | La **transformada inversa** se usa cuando: A) la inversa de la FDA es fácil de obtener · B) no hay inversa cerrada · C) se mezclan distribuciones · D) se aceptan o rechazan candidatos | **A**. B lleva a rechazo, C es composición y D es rechazo |

## Parte 3 — El ejercicio de inventario

**Consigna 2025**: costo total promedio mensual con la política (s, S) vista en clase.

| Dato | Valor |
|---|---|
| Tiempo entre demandas | exponencial, media 0,55 |
| Demora del proveedor | uniforme $[0{,}5;\ 1]$ |
| Tamaño de demanda | 3 (1/3) · 4 (1/6) · 5 (1/6) · 6 (1/3) |
| Costos | $K=50$, $i=5$, $h=2{,}5$, $\pi=6$ |
| Política e inicio | $s=30$, $S=60$, $I_0=40$ |
| Números aleatorios | 0,9501 · 0,1304 · 0,9700 · 0,3546 · 0,9258 |

### Paso 1 — Generadores (transformada inversa)

- Tiempo entre demandas: $t = -0{,}55\ln r$.
- Demanda: acumulada $0{,}3333 \mid 0{,}5 \mid 0{,}6667 \mid 1$. Entonces $r<0{,}3333\Rightarrow3$; $r<0{,}5\Rightarrow4$; $r<0{,}6667\Rightarrow5$; si no, $6$.
- Demora: $L = 0{,}5 + 0{,}5\,r$.

### Paso 2 — Tabla de los cinco números

Conviene armarla primero, antes de saber para qué se va a usar cada número:

| $r$ | tiempo $-0{,}55\ln r$ | demanda | demora $0{,}5+0{,}5r$ |
|---|---|---|---|
| 0,9501 | 0,0282 | 6 | 0,9750 |
| 0,1304 | 1,1204 | 3 | 0,5652 |
| 0,9700 | 0,0168 | 6 | 0,9850 |
| 0,3546 | 0,5702 | 4 | 0,6773 |
| 0,9258 | 0,0424 | 6 | 0,9629 |

### Paso 3 — Traza, consumiendo los números en orden

| $t$ | Evento | Nº usado | Qué pasa | $I$ | Área $I^+$ del tramo |
|---|---|---|---|---|---|
| 0 | evaluación | — | $40 \ge 30$, no se pide; próxima evaluación en $t=1$ | 40 | — |
| 0 | (init) | $r_1$ | primera demanda en $0{,}0282$ | 40 | — |
| 0,0282 | demanda | $r_2 \to 3$; $r_3 \to 0{,}0168$ | $40\to37$; próxima demanda en 0,0450 | 37 | $40\times0{,}0282=1{,}128$ |
| 0,0450 | demanda | $r_4 \to 4$; $r_5 \to 0{,}0424$ | $37\to33$; próxima demanda en 0,0874 | 33 | $37\times0{,}0168=0{,}622$ |
| 0,0874 | demanda | **no quedan números** | — | — | $33\times0{,}0424=1{,}399$ |

◐ **El enunciado no cierra.** Con cinco números en el orden natural la corrida llega a $t=0{,}087$ meses, nunca baja de $s$ y nunca se pide. Hay dos maneras razonables de terminarlo. **Escribí el supuesto en la hoja**:

- **Supuesto 1, reusar los números en ciclo, $n=1$ mes.** En $t=0{,}0874$ se usa $r_1$ de nuevo: demanda $6$, $I: 33\to27$. Después $r_2$: próxima demanda en $1{,}2078$. En $t=1$ coinciden el fin de simulación y la evaluación, y el fin va primero, igual que en Law. No se pide nada.
  Área total $I^+ = 1{,}128+0{,}622+1{,}399+27\times(1-0{,}0874) = 27{,}789$.
  **CTPM** $= 0 + 2{,}5 \times 27{,}789/1 + 6\times 0 \approx$ **69,47 por mes**.
- **Supuesto 2, cortar cuando se acaban los números.** Se promedia sobre el tiempo simulado, $T=0{,}0874$: $\bar I^+ = 3{,}149/0{,}0874 = 36{,}03$. **CTPM** $= 2{,}5\times36{,}03 \approx$ **90,07 por mes**.

> Lo que se evalúa es el **procedimiento**, y ese sí está claro. Un ejemplo completo que cierra, con pedido, backlog y los tres costos, está en `resumen-inventario.md` §7.3. **Si alguien del curso sabe cómo lo corrigieron en 2025, ese dato vale oro.**

### La fórmula que tenés que escribir sí o sí

$$\text{CTPM} = \underbrace{\frac{\sum (K + iZ)}{n}}_{\text{pedido}} + \underbrace{h\,\frac{\int_0^n I^+(t)\,dt}{n}}_{\text{mantenimiento}} + \underbrace{\pi\,\frac{\int_0^n I^-(t)\,dt}{n}}_{\text{faltante}}$$

**Trampas**:

- El área de cada tramo se calcula con el nivel **anterior** al evento.
- Si $I\ge s$ no se paga ni siquiera $K$.
- El pedido llega en $t+L$.
- Cuando llega, primero cubre el backlog.
- Se divide por **meses**, no por eventos.
- $h$ va con $I^+$ y $\pi$ va con $I^-$.

## Cómo pregunta la cátedra (patrones del 2025)

1. **"Según el texto"** = Law cap. 1 o Ross cap. 2 **textual**. La opción correcta repite la definición del libro palabra por palabra.
2. **Las opciones "A y B" o "todas" son la trampa más usada.** En la parte 1 fue correcta en 3 de 15 (1.1, 1.5 y 1.14). En las otras 12 la respuesta era una sola. Antes de marcar "A y B", **probá que B sea verdadera por sí sola**.
3. **Palabras absolutas = casi siempre falsa**: "siempre", "solo", "totalmente", "exacta" (salvo la solución analítica), "asegura". Lo vimos en 1.3 D, 1.12 C y D, 2.3 y 2.4.
4. **Confunde lo que sale de un modelo con lo que entra**: tiempo de servicio o de arribo como "medida de rendimiento" (1.2 A, 2.13 B), o un cambio de estado como "evento" (2.12 E).
5. **Confunde sistema / modelo / simulación** (1.4) y **verificación / validación** (1.10).
6. **Doble negación** en V/F: "la POO **no** es imprescindible" (2.6). Leela despacio.
7. **Cultura de cátedra**: AnyLogic (paradigmas, GIS), LaTeX e historia de la simulación. Son 5 de 32, regaladas si las leíste.
8. **En la selección múltiple marcar de menos también resta** (2.11).

## Preguntas de práctica — alcance 2026 *(no oficiales)*

> P1 a P25 cubren Ross cap. 2, colas e inventario. P26 a P40 cubren lo que se sumó con el material del Classroom: los elementos de la simulación, la salida del inventario, M/G/c y AnyLogic.

> Estas no son de la cátedra: las escribí yo con el estilo del 2025, para cubrir lo que **este año entra** (Ross cap. 2 §2.1 a §2.9 más Weitz) y en 2025 no se tomó. Las respuestas están al final.

**P1)** La desigualdad de Markov establece que, si $X \ge 0$ y $a>0$:
A) $P\{X\ge a\}\le E[X]/a$ · B) $P\{X\ge a\}\ge E[X]/a$ · C) $P\{|X-\mu|\ge a\}\le \sigma^2/a^2$ · D) solo vale si $X$ es normal · E) A y C

**P2)** La desigualdad de Chebyshev $P\{|X-\mu|\ge k\sigma\}\le 1/k^2$ se demuestra:
A) aplicando Markov a $(X-\mu)^2/\sigma^2$ con $a=k^2$ · B) con el teorema central del límite · C) aplicando la ley fuerte · D) solo para VA discretas · E) A y C

**P3)** En la ley débil de los grandes números, lo que tiende a infinito es:
A) el tiempo de simulación · B) la cantidad $n$ de variables i.i.d. promediadas · C) la varianza · D) la media · E) A y B

**P4)** Para probar la ley débil se usa que $\mathrm{Var}(\bar X)=\sigma^2/n$. Esto requiere:
A) que las $X_i$ sean normales · B) que las $X_i$ sean independientes · C) que $n>30$ · D) nada · E) A y C

**P5)** $\mathrm{Var}(aX+b)$ es igual a:
A) $a\,\mathrm{Var}(X)+b$ · B) $a^2\,\mathrm{Var}(X)$ · C) $a^2\,\mathrm{Var}(X)+b^2$ · D) $a\,\mathrm{Var}(X)$ · E) B y C

**P6)** $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y$:
A) siempre · B) solo si $\mathrm{Cov}(X,Y)=0$, por ejemplo si son independientes · C) nunca · D) solo si tienen la misma distribución · E) A y D

**P7)** La binomial $(n,p)$ puede verse como:
A) suma de $n$ Bernoulli$(p)$ independientes · B) nº de ensayos hasta el primer éxito · C) límite de la Poisson · D) una continua · E) A y B

**P8)** ¿Por qué AnyLogic calcula la binomial y la Poisson con fórmulas de recurrencia?
A) porque la fórmula directa (factoriales y potencias) es cara de calcular · B) porque la directa es inexacta por definición · C) porque la recurrencia es la definición · D) no las usa · E) B y C

**P9)** La variable exponencial de tasa λ cumple:
A) $E=1/\lambda$ · B) no tiene memoria: $P\{X>s+t\mid X>s\}=P\{X>t\}$ · C) es el tiempo entre eventos de un proceso de Poisson de tasa λ · D) A y B · E) todas

**P10)** En un proceso de Poisson de tasa λ, $N(t)$ tiene distribución:
A) exponencial de media $1/\lambda$ · B) Poisson de media $\lambda t$ · C) binomial · D) uniforme en $(0,t)$ · E) A y B

**P11)** En un proceso de Poisson no homogéneo con intensidad $\lambda(t)$, el número de eventos en $(s, s+t]$ es:
A) Poisson con media $\lambda t$ · B) Poisson con media $m(s+t)-m(s)$, con $m(t)=\int_0^t\lambda(y)\,dy$ · C) exponencial · D) no tiene distribución conocida · E) A y B

**P12)** El teorema central del límite dice que, para $n$ grande, la suma o el promedio de $n$ VA i.i.d.:
A) tiende a la distribución de las $X_i$ · B) es aproximadamente normal, cualquiera sea la distribución de las $X_i$ · C) es exactamente normal · D) solo vale si las $X_i$ son normales · E) C y D

**P13)** Si $Z$ es normal estándar, $X=\mu+\sigma Z$ es:
A) normal de media $\mu$ y varianza $\sigma$ · B) normal de media $\mu$ y varianza $\sigma^2$ · C) estándar · D) uniforme · E) A y C

**P14)** Una VA uniforme en $(a,b)$ tiene media y varianza:
A) $(a+b)/2$ y $(b-a)^2/12$ · B) $(b-a)/2$ y $(b-a)/12$ · C) $(a+b)/2$ y $(b-a)/12$ · D) $0$ y $1$ · E) A y D

**P15)** V o F: los tiempos entre arribos de un proceso de Poisson siguen una distribución de Poisson.

**P16)** V o F: en un proceso de Poisson los incrementos son independientes **y** estacionarios; en el no homogéneo deja de cumplirse la estacionariedad.

**P17)** V o F: un modelo estocástico produce una estimación de las características del sistema, no un valor exacto.

**P18)** V o F: el método de incremento fijo de tiempo omite los períodos de inactividad.

**P19)** En el modelo de inventario, la **evaluación de inventario** ocurre:
A) cada vez que hay una demanda · B) al principio de cada mes (revisión periódica) · C) cuando $I<s$, en el instante en que pasa · D) cuando llega un pedido · E) A y C

**P20)** En el modelo de inventario, si en $t=n$ coinciden fin de simulación y evaluación:
A) se evalúa primero · B) se ejecuta primero el fin de simulación, para no hacer un pedido que no se va a contabilizar · C) da igual · D) se descartan los dos · E) A y C

**P21)** Ley de Little:
A) $L=\lambda W$ · B) $L_q=\lambda W_q$ · C) $W=W_q+1/\mu$ · D) A y B · E) todas

**P22)** En el M/M/1, la probabilidad de que haya $n$ clientes en el sistema es:
A) $(1-\rho)\rho^n$ · B) $\rho^n$ · C) $e^{-\rho}\rho^n/n!$ · D) $1-\rho$ · E) A y D

**P23)** Notación de Kendall A/B/c/K/N: ¿qué indica la segunda letra?
A) distribución de los tiempos entre llegadas · B) distribución de los tiempos de servicio · C) nº de servidores · D) capacidad del sistema · E) población

**P24)** ¿Qué es la **semilla** de un generador pseudoaleatorio?
A) el valor inicial que determina toda la sucesión · B) el módulo $m$ · C) el período · D) un número verdaderamente aleatorio obligatorio · E) A y D

**P25)** Un GCL mixto $Z_i=(aZ_{i-1}+c) \bmod m$ tiene período completo si:
A) $m$ y $c$ son primos relativos · B) todo primo que divide a $m$ divide a $a-1$ · C) si 4 divide a $m$, 4 divide a $a-1$ · D) solo si $c=0$ · E) A, B y C a la vez

**P26)** Según las diapositivas de la cátedra, la **entidad** es:
A) el lugar donde se detienen los clientes · B) el elemento responsable de que cambie el estado del sistema · C) el dispositivo que lleva a cabo un evento · D) una característica de un recurso · E) A y C

**P27)** Las **localizaciones** y los **recursos** se diferencian en que:
A) las localizaciones son estáticas (lugares donde las entidades se detienen) y los recursos dinámicos (llevan a cabo eventos) · B) son sinónimos · C) los recursos son estáticos · D) las localizaciones son atributos de la entidad · E) B y D

**P28)** V o F: en el modelo de inventario de Law, al aumentar $S$ con $s$ fijo, el costo de pedido promedio **baja**.

**P29)** En la salida de Law, la política (20, 60) tuvo el menor costo (122,74). La conclusión correcta es:
A) es la política óptima · B) es la mejor solo si se repite la corrida con la misma semilla · C) es una estimación de una sola corrida y otra corrida podría cambiar el orden · D) las 9 políticas cuestan lo mismo · E) A y B

**P30)** Sin simular, en el modelo de inventario se puede prever:
A) la magnitud de cada componente de costo · B) la dirección en que se mueve cada componente, pero no su magnitud · C) cuál es la política óptima · D) nada · E) A y C

**P31)** Para analizar una cola **M/G/c** hace falta, además de $\lambda$:
A) solo la media del servicio · B) la media y el desvío estándar del tiempo de servicio · C) que el servicio sea exponencial · D) que la población sea finita · E) C y D

**P32)** V o F: en el paso 2 de Weitz (generación del modelo base), los datos todavía no son importantes.

**P33)** Según *AnyLogic in 3 Days*, la **dinámica de sistemas**:
A) trabaja con agregados (stocks y flujos) y una abstracción alta · B) modela cada individuo · C) se usa para el detalle físico · D) fue creada por Gordon en 1961 · E) B y C

**P34)** En DES, el primer software fue:
A) AnyLogic · B) GPSS, de Geoffrey Gordon (IBM, 1961) · C) Arena · D) Excel · E) Mathematica

**P35)** V o F: en un modelo basado en agentes, los agentes tienen que ser personas.

**P36)** En la Process Modeling Library, el bloque que **libera** un recurso es:
A) Seize · B) Delay · C) Release · D) Sink · E) Source

**P37)** En AnyLogic, el tiempo de servicio de una M/M/1 se modela con:
A) un Source con exponential(λ) · B) un Delay con exponential(μ) entre un Seize y un Release · C) un Sink · D) un ResourcePool sin bloques · E) A y C

**P38)** En la traza de Law de la cola simple ($n=6$), la corrida termina:
A) cuando sale el sexto cliente · B) cuando el sexto cliente **empieza** su servicio, porque ahí se completa la sexta demora · C) a tiempo fijo · D) cuando se vacía la cola · E) A y D

**P39)** En un sistema de colas con capacidad limitada, el costo total incluye:
A) solo servidores · B) servidores + espera + negación de servicio · C) solo espera · D) servidores + inventario · E) A y C

**P40)** V o F: la simulación a eventos discretos es estocástica porque los tiempos de servicio y de llegada suelen ser aleatorios, y por eso hace falta correrla un tiempo suficiente o varias réplicas para obtener resultados con sentido.

## Respuestas

| P | Clave | Por qué |
|---|---|---|
| 1 | **A** | Markov. C es Chebyshev con $a=k\sigma$, no Markov. |
| 2 | **A** | Markov sobre $(X-\mu)^2/\sigma^2$, que tiene esperanza 1, con $a=k^2$. Después se saca raíz. |
| 3 | **B** | Lo que crece es $n$, no el tiempo. Lo remarcó el profe. |
| 4 | **B** | Independencia, para que se anulen las covarianzas. |
| 5 | **B** | La constante $b$ no aporta varianza. |
| 6 | **B** | En general $+2\,\mathrm{Cov}(X,Y)$. |
| 7 | **A** | B es la geométrica. Y la Poisson es límite de la binomial, no al revés. |
| 8 | **A** | Es lo que dijo el profe: la recurrencia es más barata. |
| 9 | **E** | Las tres son ciertas. |
| 10 | **B** | Exponencial es el **tiempo entre** eventos. Poisson es la **cantidad**. |
| 11 | **B** | $m(t)$ es la función de valor medio. |
| 12 | **B** | "Aproximadamente", para cualquier distribución con varianza finita. |
| 13 | **B** | La varianza es $\sigma^2$, no $\sigma$. |
| 14 | **A** | |
| 15 | **F** | Son **exponenciales**. Este error ya apareció en el parcial 2021-12. |
| 16 | **V** | |
| 17 | **V** | Es la principal desventaja del modelo estocástico. |
| 18 | **F** | Esa ventaja es del **próximo evento**. |
| 19 | **B** | Control **periódico**. Por eso hay backlog. La C es el control continuo de IO. |
| 20 | **B** | Law ordena los eventos así: el fin es el tipo 3 y la evaluación el tipo 4. |
| 21 | **E** | Son las tres relaciones universales. |
| 22 | **A** | Geométrica en $n$. D es $P_0$. |
| 23 | **B** | A/**B**/c: llegadas / **servicio** / servidores. |
| 24 | **A** | |
| 25 | **E** | Teorema de Hull–Dobell: tienen que cumplirse las tres. |
| 26 | **B** | Definición de la cátedra. A son las localizaciones y C los recursos. |
| 27 | **A** | |
| 28 | **V** | Lotes más grandes, menos pedidos y el fijo $K$ se paga menos veces (de 99,26 a 81,37). |
| 29 | **C** | Es la conclusión de Law en §1.5.6. |
| 30 | **B** | Sin simular se prevé la dirección, pero no la magnitud. Y el total tampoco. |
| 31 | **B** | Un desvío de 0 equivale a un servicio determinístico. |
| 32 | **V** | Así está en las diapositivas del profe. |
| 33 | **A** | Forrester, años 50. D describe a GPSS y al DES. |
| 34 | **B** | |
| 35 | **F** | Pueden ser vehículos, máquinas, ideas o empresas. |
| 36 | **C** | |
| 37 | **B** | |
| 38 | **B** | $T(6)=8{,}6$. |
| 39 | **B** | Weitz 13.5. |
| 40 | **V** | Texto de *AnyLogic in 3 Days* sobre DES. |

## Fuentes

- `fuentes/examenes/parciales/2025/2025-10-04.pdf`, revisado contra las fotos del original el 2026-11-02.
- Wiki `SIM.md`: Unidades 1 a 8 y el Mapa del parcial 1.
- `estudio/parcial1-alcance-2026.md` (clase del 14/10), `resumen-colas.md`, `resumen-inventario.md`, `resumen-probabilidad.md`.
- Weitz cap. 13 (recuadro de población finita): `fuentes/txt/apuntes-catedra__Weitz__p41-60.md`.
