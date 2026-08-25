# 2019 - Parcial 2 - Leale.jpg

> Ruta original: `materias/SIM/fuentes/examenes/parciales/2019/2019 - Parcial 2 - Leale.jpg`
> La foto contiene las **dos hojas del examen** puestas una al lado de la otra: a la izquierda la "Página 1 de 2" y a la derecha la "Página 2 de 2". Se transcriben como pág. 1 y pág. 2 respectivamente.

--- pág. 1 ---

# Examen Parcial
## ISI - UTN - FRRo
### Simulación
### Recuperatorio 2019

| Apellido y Nombre | Mail | Legajo | Comisión |
|---|---|---|---|
|  |  |  |  |

**Ejercicio 1:** Dados los siguientes números supuestamente generados con distribución uniforme y la siguiente definición de la función de densidad de probabilidad uniforme:

| N° | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| # | 0.485 | 0.406 | 0.383 | 0.457 | 0.712 | 0.171 | 0.393 | 0.678 | 0.976 | 0.218 |

$$f(x) \begin{cases} \dfrac{1}{b-a} & a \leq x \leq b \\ 0 & \text{en otro caso} \end{cases}$$

**Se solicita:**

a) Obtener la función de densidad acumulada.

b) Obtener la función inversa.

c) Generar un pseudocódigo con sus correspondientes parámetros de entrada para generar con dicha distribución.

d) Generar 10 valores empleando los números provistos en la tabla.

---

**Ejercicio 2:** Suponiendo que usamos que empleamos un "Generador Congruencial Lineal Mixto" con los siguientes parámetros:

$Z_0 = 7$, $a = 5$, $c = 3$, $m = 16$.

**Se solicita:**

- Indicar si es o no de período completo. Justifique.

——————— FIN DE LA PRÁCTICA ———————

Simulación &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Página 1 de 2

--- pág. 2 ---

**Ejercicio 3:** (TEORÍA EN HOJA APARTE) Responda a las siguientes preguntas:

a) Desarrolle el intervalo de confianza para $E(Z_j) = \zeta$. Explique claramente para qué sirve en el contexto del análisis de salidas de simulación.

b) Dado un número fijo $n$ de repeticiones de una simulación, desarrolle el procedimiento para calcular la cantidad extra de repeticiones de tal forma de obtener un error relativo máximo de $\gamma\,\%$.

c) Qué diferencia hay entre un estudio de simulación terminal y uno no terminal? Ejemplifique para cada caso.

——————— FIN DEL EXAMEN ———————

Simulación &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Página 2 de 2

---

# 2022-09-24.jpg

> Ruta original: `materias/SIM/fuentes/examenes/parciales/2022/2022-09-24.jpg`

--- pág. 1 ---

### Simulación (ISI) - Parcial - 24/9/2022

APELLIDO Y NOMBRES: [tachado con corrector blanco — ilegible/anonimizado]

### Tema 1

1. Explique la diferencia entre los siguientes tipos de modelos por simulación:
   - Deterministas vs. estocásticos.
   - Continuos vs. discretos.

2. Desarrolle el diagrama de Control de Flujo para el mecanismo de avance en el tiempo al próximo evento, en una simulación de modelos a eventos discretos.

3. En la simulación del sistema formado por una cola con un solo servidor, defina y desarrolle las tres medidas de rendimiento vistas en clase.

4. En la simulación de un sistema de inventario, describa cada uno de los siguientes conceptos:
   - Política de pedidos.
   - Tamaño de la demanda.
   - Costo por pedido.

5. Luego de la definición del sistema bajo estudio y la generación del modelo de simulación base, se deben efectuar: a) la recolección y el análisis de datos, y b) la generación del modelo preliminar. Desarrolle los pasos a) y b) de un estudio de simulación.

6. Describa la notación de Kendall para clasificar los distintos modelos de colas.

7. ¿Cómo se define la esperanza de una variable aleatoria, tanto en el caso discreto como continuo? Demuestre, en el caso de una variable aleatoria discreta $X$, que: $E[aX + b] = aE[X] + b$ (si $a$ y $b$ son constantes).

8. Enuncie y describa las condiciones que hacen que la ocurrencia de ciertos "eventos" constituya un Proceso de Poisson.

   ¿Qué caracteriza a un proceso de Poisson no homogéneo?

9. Dada la fórmula de generación de números aleatorios $x_n = a x_{n-1}$ módulo $m$ (método congruencial multiplicativo), explique cuáles son las condiciones deseables para $a$ y $m$.

   ¿Cómo se modifica la fórmula anterior en el método congruencial mixto?

10. Enuncie y demuestre el algoritmo de la transformada inversa para la generación de variables aleatorias continuas. Luego elija una variable aleatoria continua, y aplique dicho algoritmo para generarla.

---

# 2023-09-16.jpg

> Ruta original: `materias/SIM/fuentes/examenes/parciales/2023/2023-09-16.jpg`

--- pág. 1 ---

### Simulación (ISI) - Parcial - 16/9/2023

[Línea de Apellido y Nombre tachada con corrector blanco — ilegible/anonimizada]

### Tema 1

1. Simulación de modelos a eventos discretos:

   a) Desarrolle e ilustre con un ejemplo en la línea de tiempo, el enfoque de avance en el tiempo al próximo evento para el sistema de una cola con un solo servidor.

   b) Describa las siguientes componentes: contadores estadísticos, rutina de eventos, biblioteca de rutinas y generador de informes.

2. Simulación de un sistema de inventario:

   a) Desarrolle el planteo del sistema, incluyendo: el tamaño de la demanda, la política de pedidos y la demora del proveedor.

   b) Defina los tres tipos de niveles de inventario al momento $t$: $I(t)$, $I^{+}(t)$ e $I^{-}(t)$; e ilustre con un ejemplo gráfico, cómo se pueden ir modificando a lo largo del tiempo.

3. De los diez pasos de la simulación vistos en clase, desarrolle brevemente los tres primeros.

4. En un modelo de colas (analítico), establezca la relación matemática entre la tasa de llegada (o número promedio de clientes que llegan por unidad de tiempo), y estas dos medidas de rendimiento: el número promedio de clientes en el sistema, y el tiempo promedio de cada cliente en el sistema. Exprese dicha relación simbólicamente (señalando el significado de cada símbolo que utilice).

5. Desarrolle brevemente algún aspecto del análisis económico de los sistemas de colas.

6. Defina los siguientes conceptos para variables aleatorias continuas: función de probabilidad acumulativa, esperanza y variancia. Enuncie y pruebe alguna propiedad que involucre al menos uno de dichos conceptos.

7. Defina y desarrolle alguna de las variables aleatorias discretas vistas en clase, incluyendo: el significado de sus parámetros, su función de masa de probabilidad, su esperanza y su variancia.

8. Enuncie y describa las condiciones que hacen que la ocurrencia de ciertos "eventos" constituya un *proceso de Poisson*.

   ¿Qué caracteriza a un proceso de Poisson *no homogéneo*?

9. Desarrolle el método congruencial multiplicativo para la generación de números aleatorios con distribución uniforme en el intervalo $(0;1)$.

   ¿Cómo se modifica la fórmula de dicho método en el método congruencial mixto?

10. Enuncie y demuestre el algoritmo de la transformada inversa para la generación de variables aleatorias continuas. Luego elija una variable aleatoria continua, y aplique dicho algoritmo para generarla.

> [NOTA pág. 1]: En el margen derecho de la foto asoma parcialmente otra hoja (cuadriculada, con escritura manuscrita). Solo se ven fragmentos de trazos sueltos, sin ninguna palabra completa: **ilegible**, no transcribible.

---

# 2024-10-19.jpg

> Ruta original: `materias/SIM/fuentes/examenes/parciales/2024/2024-10-19.jpg`
> [NOTA DE TRANSCRIPCIÓN]: El encabezado de la hoja está cortado por el borde superior de la foto — solo se ve el final de una línea (presumiblemente "Simulación (ISI) - Parcial - 19/10/2024", ilegible en la imagen). La fecha del título proviene del nombre del archivo. La foto llega hasta la consigna 8; **no se ven consignas 9 y 10** (probablemente en otra hoja no fotografiada).

--- pág. 1 ---

[encabezado cortado / ilegible]

### Tema 1

1. Explique brevemente la diferencia entre las siguientes maneras de estudiar un sistema.
   - Modelo físico vs. Modelo matemático.
   - Solución analítica frente a Simulación.

2. Determine el costo total promedio mensual para un sistema de inventario con estos datos:

   Tiempo entre demandas: variable aleatoria exponencial con media 0,4.

   Demora del proveedor: variable aleatoria uniforme en el intervalo $[0{,}2;\,0{,}6]$.

   Tamaño de la demanda:

$$D = \begin{cases} 3 & \text{con probabilidad } 1/8 \\ 4 & \text{con probabilidad } 1/4 \\ 5 & \text{con probabilidad } 3/8 \\ 6 & \text{con probabilidad } 1/4 \end{cases}$$

   Parámetros para los costos: $K = 20$; $i = 5$; $h = 2{,}5$; $\pi = 6$.

   Restantes parámetros: $s = 15$; $S = 30$; $I_0 = 20$.

   Números aleatorios: 0.9015 - 0.1096 - 0.8901 - 0.3546 - 0.9317.

3. De los diez pasos de la simulación vistos en clase, desarrolle brevemente los siguientes: 6. Validación del modelo. 7. Generación del modelo final. 8. Determinación de los escenarios para el análisis.

4. En un modelo de colas (analítico), establezca la relación matemática entre la tasa de llegada (o número promedio de clientes que llegan por unidad de tiempo), y estas dos medidas de rendimiento: el número promedio de clientes en cola, y el tiempo promedio de cada cliente en la cola. Exprese dicha relación simbólicamente (señalando el significado de cada símbolo que utilice).

5. Describa la notación de Kendall para clasificar los distintos modelos de colas.

6. ¿Cómo se define la varianza de una variable aleatoria? Enuncie y demuestre a qué es equivalente la expresión $\mathrm{Var}(aX + b)$, siendo $a$ y $b$ constantes.

7. Defina y desarrolle las variables aleatorias binomiales.

8. Enuncie y describa las condiciones que hacen que la ocurrencia de ciertos "eventos" constituya un *proceso de Poisson*.

   ¿Qué caracteriza a un proceso de Poisson *no homogéneo*?

[fin de lo visible en la foto]

---

# 2023-03-16.jpg (Globalizador)

> Ruta original: `materias/SIM/fuentes/examenes/globalizador/2023-03-16.jpg`

--- pág. 1 ---

### Simulación (ISI) - Globalizador - 16/3/2023

APELLIDO Y NOMBRE: ______________________________ &nbsp;&nbsp; LEGAJO: __________

1. ¿Cómo se define la esperanza de una variable aleatoria? Desarrolle a qué es igual la esperanza de una variable aleatoria multiplicada por una constante y sumada con un término independiente.

2. Enuncie la fórmula y explique bajo qué condiciones hablamos de una variable aleatoria binomial.

3. Dada la fórmula de generación de números aleatorios $x_n = a x_n - 1$ módulo $m$, explique cuáles son las condiciones deseables para $a$ y $m$.

   > [NOTA DE TRANSCRIPCIÓN]: la fórmula está impresa literalmente así en el original ($x_n = ax_n - 1$); se entiende que refiere a $x_n = a\,x_{n-1} \bmod m$.

4. Desarrolle el Método de la Transformada Inversa para la generación de variables aleatorias discretas.

5. Describa los costos asociados a un modelo de simulación de inventarios.

6. ¿Cuál es la diferencia entre un modelo determinístico y uno estocástico?

7. Luego de la definición del sistema bajo estudio y la generación del modelo de simulación base, se deben efectuar: a) la recolección y el análisis de datos, y b) la generación del modelo preliminar. Desarrolle los pasos a) y b) de un estudio de simulación.

8. En un modelo de colas, establezca la relación matemática entre la tasa de servicio (o número promedio de clientes atendidos por unidad de tiempo), y estas dos medidas de rendimiento: Tiempo promedio de espera en la cola - Tiempo promedio en el sistema. Exprese dicha relación simbólicamente (señalando el significado de cada símbolo que utilice).

9. Desarrolle las condiciones que caracterizan un modelo $M/M/c$.

10. Explique el procedimiento para determinar cuándo detener las corridas de simulación con el objetivo de obtener un desvío estandar determinado (pre-definido).

---

# Final 2017-05.jpg

> Ruta original: `materias/SIM/fuentes/examenes/finales/Final 2017-05.jpg`
> [NOTA DE TRANSCRIPCIÓN]: el nombre del archivo dice "2017-05", pero el encabezado impreso en la hoja dice **"Examen Final, agosto 2015"**. Se transcribe el encabezado tal como figura en la imagen.

--- pág. 1 ---

### Simulación
### Examen Final, agosto 2015

Alumnos: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Calificación:

———————————————————————————————————

En una empresa hay dos secciones de operación: A y B. Ciertos artículos arriban al sistema con distribución de Poisson para los tiempos entre arribos con frecuencia lambda. Los lotes de mercadería forman una línea de espera con disciplina Fifo. El servidor de A consiste en cargar la mercadería y transportarla hasta la sección B, en el cual se descarga y se la lleva a un deposito con una frecuencia de servicio mhu. Una vez completada la descarga, el sistema de transporte retorna al puesto A para recibir la nueva carga. La demora de ir de B hacia A posee distribución forme. Existe un único transporte.

Se desea:

1) Desarrollar el diagrama de desencadenamiento de eventos.
2) Falta alguna información y cual es.
3) Desarrolle un algoritmo para el tratamiento de la línea de espera en A
4) En el régimen estacionario se desea saber cómo influye el tiempo de retorno en el tiempo medio en el sistema. Que análisis de resultados hará.

> [NOTA DE TRANSCRIPCIÓN]: "distribución forme" figura así en el original (probable errata por "distribución uniforme"). "mhu" figura así en el original (por $\mu$). No hay resolución manuscrita en la imagen.

---

# Final 2021-11-29.jpeg

> Ruta original: `materias/SIM/fuentes/examenes/finales/Final 2021-11-29.jpeg`
> Captura de pantalla de un examen en plataforma tipo Moodle. Cada pregunta muestra su estado ("Finalizado" / "Sin contestar") y "Puntúa como 1,00", más un enlace "Marcar pregunta". Se transcriben esos metadatos entre corchetes.

--- pág. 1 ---

**Pregunta 1** [Finalizado — Puntúa como 1,00 — Marcar pregunta]

Dada la fórmula de generación de números aleatorios $x_n = a x_{n-1}$ modulo $m$, explique cuáles son las condiciones deseables para $a$ y $m$

**Pregunta 2** [Finalizado — Puntúa como 1,00 — Marcar pregunta]

Cuál es la diferencia entre un modelo del sistema y un experimento con el sistema real?

**Pregunta 3** [Sin contestar — Puntúa como 1,00 — Marcar pregunta]

Explique la diferencia entre un proceso de Poisson homogéneo y uno no homogéneo

**Pregunta 4** [Sin contestar — Puntúa como 1,00 — Marcar pregunta]

Explique y aplique el Método de la Transformada Inversa para generar el valor de una variable aleatoria discreta X con la siguiente función de masa de probabilidad: $P(X=1) = 1/6$, $P(X=2) = 1/3$, $P(X=3) = 1/3$, $P(X=4) = 1/6$ (observe que $1/6 + 1/3 + 1/3 + 1/6 = 1$)

**Pregunta 5** [Finalizado — Puntúa como 1,00 — Marcar pregunta]

En un modelo de colas, establezca la relación matemática entre la tasa de servicio (o número promedio de clientes atendidos por unidad de tiempo), y estas dos medidas de rendimiento: Tiempo promedio de espera en la cola - Tiempo promedio en el sistema. Exprese dicha relación simbólicamente (señalando el significado de cada símbolo que utilice)

**Pregunta 6** [Finalizado — Puntúa como 1,00 — Marcar pregunta]

Explique la fórmula y el concepto de variable aleatoria exponencial. Para qué usamos esta fórmula en un modelo de colas?

**Pregunta 7** [Sin contestar — Puntúa como 1,00 — Marcar pregunta]

Enuncie y demuestre el Algoritmo de la Transformada Inversa para la generación de variables aleatorias continuas y aplíquelo para generar una variable aleatoria con distribución uniforme.

**Pregunta 8** [Finalizado — Puntúa como 1,00 — Marcar pregunta]

Luego de la definición del sistema bajo estudio y la generación del modelo de simulación base, se deben efectuar: a) la recolección y el análisis de datos, y b) la generación del modelo preliminar. Desarrolle los pasos a) y b) de un estudio de simulación

**Pregunta 9** [Sin contestar — Puntúa como 1,00 — Marcar pregunta]

Dada una cola finita de tamaño n en un sistema de una cola y un servidor. Cómo se calcula la probabilidad de que un cliente no pueda entrar a la cola? (Denegación de servicio)

**Pregunta 10** [Finalizado — Puntúa como 1,00 — Marcar pregunta]

En el modelo de simulación de inventarios desarrollado en clase, describa el significado, las fórmulas que los involucran, y cómo varían en el tiempo los tres niveles de inventario: $I(t)$, $I^{\wedge}(t)$, $I^{\wedge}\{-\}(t)$ {}

> [NOTA DE TRANSCRIPCIÓN]: la pregunta 10 aparece en pantalla con el LaTeX sin renderizar, literalmente como `I(t), I^(t), I^{-}(t) {}`. Se refiere a $I(t)$, $I^{+}(t)$ e $I^{-}(t)$.
