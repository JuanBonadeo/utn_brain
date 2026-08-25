# SIM — Wiki

> Simulación · UTN-ISI · 4° año
> Cátedra: jefe **Leale**. Docentes que aparecen en exámenes viejos: Weitz, Lara, Flamini, De Federico.
> Software: **AnyLogic** (y, en años anteriores, Wolfram Mathematica).

### Bibliografía de la cátedra

Los tres apuntes **oficiales** vigentes desde que Leale es jefe de cátedra (nota de febrero 2021 en
`fuentes/apuntes-catedra/LEER-apuntes-vigentes.txt`):

| Apunte | Contenido | De dónde sale |
|---|---|---|
| **Apunte Weitz** (`Apunte Weitz con hojas rotadas y acotado.pdf`) | Cap. 1 (simulación básica), inventario, 10 pasos, cap. 13 (modelos de colas), caps. 9 y 10 en inglés (análisis de salidas y comparación de sistemas) | Fotocopias de Law & Kelton, *Simulation Modeling and Analysis*, y de un libro de modelos de colas |
| **Naylor, cap. 4** (`Tecnicas de Simulación en Computadoras - Naylor Cap. 4.pdf`) | Generación de valores de variables aleatorias: transformada inversa, rechazo, composición, y las distribuciones una por una | Naylor et al., *Técnicas de simulación en computadoras* |
| **Números pseudoaleatorios** | Generadores: cuadrados centrales, congruenciales, período, en R | Capítulo de bookdown |

Lo que está en `fuentes/apuntes-extra/` (Gordon, teoría de colas, Law & Kelton completo, números
aleatorios de Lascano) **son apoyos, no material obligatorio** — se usaban antes con Lara y otros
profesores. Aun así, `Números aleatorios.pdf` de Lascano es la mejor fuente para los tests de
Chi-cuadrado y corridas, que sí se toman.

El libro de texto principal es **Ross, *Simulación*** (2ª ed. 1997 en español; 5ª ed. 2013 en inglés,
fotocopiada en 2019). El cap. 2 de Ross es la base de la Unidad 6.

### Régimen de cursado

> De los apuntes manuscritos de clase de 2022 (`fuentes/teoria-flamini/`). **Verificá si sigue igual
> este año** — es información de hace cuatro años.

- **Regularizar**: TPs individuales con 75% aprobados + 1 o 2 parciales con 60% de aprobación (hay recuperatorio y globalizador) + entregar el TP integrador grupal (máximo 3 integrantes) a fin de año.
- **Aprobación directa**: aprobar el TP integrador, regularizar **antes** del globalizador, y asistencia.

## Índice

0. **[Mapa del parcial 1](#mapa-del-parcial-1--qué-entra-y-de-dónde-sale)** — qué entra, de dónde sale, y qué falta en el resumen
1. [Unidad 1 — Introducción a la simulación](#unidad-1--introducción-a-la-simulación)
2. [Unidad 2 — Simulación a eventos discretos (DES)](#unidad-2--simulación-a-eventos-discretos-des)
3. [Unidad 3 — Modelo de cola con un servidor](#unidad-3--modelo-de-cola-con-un-servidor)
4. [Unidad 4 — Modelo de inventarios (s, S)](#unidad-4--modelo-de-inventarios-s-s)
5. [Unidad 5 — Pasos de un estudio de simulación](#unidad-5--pasos-de-un-estudio-de-simulación)
6. [Unidad 6 — Elementos de probabilidad](#unidad-6--elementos-de-probabilidad)
7. [Unidad 7 — Generación de números y variables aleatorias](#unidad-7--generación-de-números-y-variables-aleatorias)
8. [Unidad 8 — Modelos analíticos de colas](#unidad-8--modelos-analíticos-de-colas)
9. [Unidad 9 — Análisis de los datos de salida](#unidad-9--análisis-de-los-datos-de-salida)
10. [Unidad 10 — Comparación de sistemas alternativos](#unidad-10--comparación-de-sistemas-alternativos)
11. [TPI — consigna y estado](#tpi--trabajo-práctico-integrador)

---

## Mapa del parcial 1 — qué entra y de dónde sale

> Esta sección no es teoría: es el mapa de estudio. Sale de cruzar el resumen que vas a usar
> (`fuentes/Resumen Simulación.pdf`) con los parciales y finales viejos de `fuentes/examenes/`
> y con las dos transcripciones de clase pre-examen (`fuentes/clase-preexamen/`).

### 🔴 Lo primero: el formato cambió en 2025

**Confirmá con la cátedra qué formato se toma este año.** Los parciales guardados muestran dos
formatos muy distintos:

| Años | Formato |
|---|---|
| 2019, 2021, 2022, 2023, 2024 | **10 preguntas a desarrollar** (más las de 2021 virtual, 16 y 10) |
| **2025-10-04** (el más reciente) | **Multiple choice + verdadero/falso + un ejercicio numérico** |

**Estructura del parcial 2025** (`fuentes/examenes/parciales/2025/2025-10-04.pdf`), tema 404:

- **Parte 1 — 15 preguntas multiple choice** con opciones A a E, incluyendo las clásicas *"las opciones A y B son correctas"* y *"todas las anteriores son correctas"*. Temas: geométrica, medidas de rendimiento de la cola simple, política (s,S), definición de sistema, proceso de Poisson, población finita, intensidad de tráfico, condición de estado estable de M/M/1, next-event time advance (×2), verificación vs. validación, binomial→Poisson, Poisson no homogéneo, para qué sirven los números aleatorios, segundo paso del estudio.
- **Parte 2 — 17 preguntas de verdadero/falso y de selección múltiple** más sueltas, **incluyendo preguntas sobre AnyLogic y LaTeX**: paradigmas de simulación explicados en "AnyLogic en 3 días" (basado en agentes, sistemas dinámicos, eventos discretos), qué es GIS, qué es LaTeX, si la POO es imprescindible, cuándo surgió la simulación por computadora.
- **Parte 3 — un ejercicio numérico**: calcular el **costo total promedio mensual** de un sistema de inventario con parámetros y números aleatorios dados. (Ver el ejercicio resuelto tipo en la Unidad 4.)

> ⚠️ **Las respuestas marcadas en esa copia son del alumno, no la corrección.** Varias son
> discutibles: la 2.1 ("la simulación reemplaza a la solución analítica…") está marcada V cuando la
> teoría dice lo contrario — si hay solución analítica, **usala**; y la 2.9 C marca como vigente el
> método de la parte media del cuadrado, que la propia teoría descarta. No las tomes como clave.

**Consecuencia práctica**: si el parcial de este año es multiple choice, cambia cómo conviene
estudiar — hay que cubrir **más superficie con precisión de detalle** (fórmulas exactas, condiciones
exactas, qué palabra dice cada definición) en vez de poder desarrollar tres temas en profundidad. Y
hay que mirar el material de **AnyLogic**, que en los parciales viejos no aparecía.

### Qué se toma, sin importar el formato

En los dos formatos el temario es prácticamente el mismo:

- Una o dos de **generación de números / variables aleatorias** (enunciar y demostrar transformada inversa, condiciones de $a$ y $m$ en el congruencial, aplicar transformada inversa discreta).
- Una de **inventarios** (costos, $I(t)$/$I^+(t)$/$I^-(t)$, política (s,S), rutinas) — y desde 2024, **el ejercicio numérico**.
- Una de **colas** (condiciones de M/M/1, relación λ–μ, relaciones entre medidas de rendimiento, notación de Kendall, denegación de servicio).
- Una o dos de los **10 pasos de un estudio de simulación** (te piden desarrollar dos pasos puntuales).
- Dos o tres de **probabilidad** (esperanza/varianza con demostración, una VA discreta a elección, proceso de Poisson homogéneo y no homogéneo).
- Una conceptual de **modelo vs. sistema real / analítico vs. simulación / clasificación de modelos**.
- Una o dos de **DES** (mecanismo de avance del tiempo, componentes del modelo).

### 🎯 Las tres preguntas que se repiten literalmente

Cruzando los parciales de 2022, 2023 y 2024 (formato a desarrollar), **las últimas tres preguntas son
casi idénticas año a año**:

| Nº | Pregunta | 2022 | 2023 | 2024 | Dónde está |
|---|---|:--:|:--:|:--:|---|
| **8** | *"Enuncie y describa las condiciones que hacen que la ocurrencia de ciertos eventos constituya un proceso de Poisson. ¿Qué caracteriza a un proceso de Poisson no homogéneo?"* | ✅ | ✅ | ✅ | Unidad 6, §6.10 |
| **9** | Método congruencial (multiplicativo o mixto) para generar números aleatorios; condiciones deseables para $a$ y $m$; cómo se modifica en el mixto | ✅ | ✅ | — | Unidad 7, §7.4 |
| **10** | *"Enuncie y demuestre el algoritmo de la transformada inversa para la generación de variables aleatorias continuas. Luego elija una variable aleatoria continua, y aplique dicho algoritmo para generarla."* | ✅ | ✅ | — | Unidad 7, §7.6.A |

En el parcial 2025 (multiple choice) el proceso de Poisson vuelve a aparecer **dos veces** (1.5 y 1.13).
Si vas a priorizar algo, priorizá esas tres.

Otras que se repiten mucho:

- *"Luego de la definición del sistema bajo estudio y la generación del modelo de simulación base, se deben efectuar: a) la recolección y el análisis de datos, y b) la generación del modelo preliminar"* → 2022 P5, globalizador 2023 P7, final 2021 P8, parcial 2021-10 P14. **Cuatro veces.** (Unidad 5, pasos 3 y 4 de Weitz.)
- *"Describa la notación de Kendall"* → 2022 P6, 2024 P5.
- *"Describa los costos asociados a un modelo de simulación de inventarios"* → 2021-10 P1, 2021-12 P5, globalizador 2023 P5.
- Relación entre tasas y medidas de rendimiento en colas → 2021-10 P7, 2023 P4, 2024 P4, globalizador 2023 P8, final 2021 P5. **Cinco veces**, cambiando cuál de las tres relaciones piden.

### Qué cubre bien el resumen que vas a usar

`fuentes/Resumen Simulación.pdf` (29 páginas) es un armado de tres fuentes:

| Bloque del resumen | Fuente original | Cubre |
|---|---|---|
| Capítulo 1 (1.1–1.8 + Apéndices 1A y 1B) | **Law & Kelton**, *Simulation Modeling and Analysis*, cap. 1 | Unidades 1, 2, 3, 4, 5 (los 10 pasos de Law) y la intro a colas |
| "Simulación — Darío Weitz" (1.5 y cap. 13) | **Apunte Weitz** (oficial de cátedra) | Unidad 5 (los 10 pasos de Weitz) y Unidad 8 (colas analíticas) |
| Capítulo 2 (2.1–2.9) | **Ross**, *Simulation*, cap. 2 | Unidad 6 completa |

### ⚠️ Huecos del resumen respecto de lo que se toma

Esto es lo importante: **el resumen no cubre tres bloques que aparecen en casi todos los parciales**.

| Hueco | Por qué importa | Dónde está |
|---|---|---|
| **Generación de números y variables aleatorias** (congruencial, transformada inversa, rechazo, tests) | Es la pregunta más repetida de todos los parciales guardados (2021-10 P2/P3/P8, 2021-12 P1/P8/P10, finales 2016 y 2019 con la triangular) | Unidad 7 de esta wiki. Fuentes: Naylor cap. 4 (`fuentes/apuntes-catedra/`), `fuentes/apuntes-extra/Números aleatorios.pdf`, `fuentes/apuntes-catedra/Números pseudoaleatorios.pdf` |
| **Análisis de datos de salida** (transiente/estacionario, terminal/no terminal, intervalos de confianza, precisión absoluta y relativa, nº de réplicas, media de lotes) | La clase pre-examen lo marca explícito ("Cap 9 en inglés sí", "Pag 76 sí, precisión absoluta/relativa") y sale en finales 2016, 2017 y 2019 | Unidad 9. Fuente: `fuentes/resumenes/Resumen 1.pdf` (Pagliaro), secciones 7–8 |
| **Comparación de sistemas alternativos** (t-apareado, Welch, ranking y selección, números aleatorios comunes) | La clase pre-examen dice "Cap 10 sí, pag 86 sí". Sale en parcial 2019-Weitz y final 2019 | Unidad 10. Fuente: `fuentes/resumenes/Resumen 1.pdf`, secciones 9–11 |

**Además**, hay tres detalles chicos que el resumen tampoco trae y que ya se tomaron:

- **Denegación de servicio** en cola finita (parcial 2021-10 P15). → Unidad 8.
- **Variable hipergeométrica** (parcial 2021-10 P10, "pag 32 Ross"). → Unidad 6.
- **Tests de aleatoriedad**: Chi-cuadrado, corridas, series (preguntas frecuentes #2). → Unidad 7.

### Qué NO entra (según la clase pre-examen)

- Página 67 del apunte de Weitz (numerada 62 a lápiz).
- Página 77 del apunte de Weitz.
- Sección 10.2.2 (después de la pág. 86).
- De M/M/c (13.4 de Weitz): **entendimiento general, no las fórmulas**.
- De ahí en adelante, nada.

> Ojo: esta lista es de una clase pre-examen de un año anterior. Los temas pueden cambiar.

### Preguntas frecuentes recopiladas (2020/2021, orales)

De `fuentes/clase-preexamen/Preguntas frecuentes.docx`:

1. ¿Cómo se comparan dos simulaciones? → método de muestras apareadas (t-apareado). **Unidad 10**.
2. ¿Cómo me doy cuenta de que la generación de números aleatorios no me sirve? → tests: Chi-cuadrado y prueba de corridas. **Unidad 7**.
3. Validación del modelo (uno de los 10 pasos). **Unidad 5**.
4. Problema de inventario. **Unidad 4**.
5. Modelo de cola M/M/1. **Unidad 8**.
6. Conociendo la distribución de las variables, ¿qué necesito para los tiempos de eventos aleatorios? → un generador de números aleatorios. **Unidad 7**.
7. Clasificación de modelos (estocástico/determinístico, estático/dinámico, continuo/discreto). **Unidad 1**.
8. Características de un buen generador → IID, sin patrones estadísticos, ciclo grande, reproducible, eficiente. **Unidad 7**.
9. ¿Diferencia con el manejo de inventario de Investigación Operativa? → en IO el control es **continuo** y el pedido se hace apenas se toca el punto de reorden; en Simulación el control es **periódico** (revisión al inicio de cada mes), y por eso puede haber inventario **negativo** (backlog). **Unidad 4**.

---

## Unidad 1 — Introducción a la simulación

### Conceptos clave

- **Sistema**: colección de entidades (personas, máquinas) que actúan e interactúan hacia el cumplimiento de un fin lógico. Qué es "el sistema" **depende de los objetivos del estudio** — un mismo proceso real admite varios sistemas distintos.
- **Estado del sistema**: colección de variables necesarias para describir el sistema en un momento dado, **relativas a los objetivos del estudio**.
- **Modelo**: conjunto de supuestos expresados como relaciones lógicas y matemáticas que representan el comportamiento del sistema.
- **Simulación**: uso de la computadora para **evaluar numéricamente** un modelo, ejercitándolo con las entradas en cuestión para ver cómo afectan las medidas de rendimiento de salida. Genera una "historia artificial" del sistema.

### Clasificación de sistemas

| Tipo | Definición | Ejemplo |
|---|---|---|
| **Discreto** | Las variables de estado cambian instantáneamente en puntos separados del tiempo | Un cliente llega o se va de una cola |
| **Continuo** | Las variables de estado cambian continuamente respecto al tiempo | Posición y velocidad de un avión |

> En la práctica pocos sistemas son puramente uno u otro, pero suele haber un tipo predominante.

### Formas de estudiar un sistema (el árbol de decisión)

Este árbol es pregunta de parcial recurrente (2021-10 P6 y P11). Va de arriba hacia abajo:

```
                      Sistema
                         |
        +----------------+----------------+
        |                                 |
Experimentar con             Experimentar con un
 el sistema real              modelo del sistema
                                      |
                        +-------------+-------------+
                        |                           |
                 Modelo físico            Modelo matemático
                                                    |
                                      +-------------+-------------+
                                      |                           |
                            Solución analítica              Simulación
```

- **Sistema real vs. modelo**: si se puede (y es rentable) alterar el sistema físicamente y dejarlo operar bajo las nuevas condiciones, conviene — no hay dudas sobre si lo que estudiamos es relevante. Pero **rara vez es factible**: sería demasiado caro o perjudicial para el sistema. Por eso se construye un modelo como sustituto, y ahí siempre queda la pregunta de **si el modelo refleja con precisión el sistema** para las decisiones que hay que tomar.
- **Modelo físico vs. matemático**: los físicos (maquetas, simuladores) son poco comunes en investigación operativa. Los matemáticos representan el sistema con relaciones lógicas y cuantitativas que se manipulan para ver cómo reacciona.
- **Solución analítica vs. simulación**: si el modelo es simple, se puede obtener una respuesta **exacta** con fórmulas → **si hay solución analítica disponible y computacionalmente eficiente, usala**. Si el sistema es demasiado complejo, no hay solución analítica cerrada y hay que simular.

### Clasificación de los modelos de simulación (3 ejes independientes)

Pregunta frecuente #7. Los tres ejes se combinan entre sí — un modelo puede ser dinámico, estocástico y discreto a la vez.

| Eje | A | B |
|---|---|---|
| Tiempo | **Estático**: representa el sistema en un instante, o uno donde el tiempo no juega ningún papel (ej: Monte Carlo) | **Dinámico**: representa la evolución del sistema en el tiempo |
| Aleatoriedad | **Determinístico**: sin componentes probabilísticos; la salida se determina una vez fijadas las ecuaciones y las entradas | **Estocástico**: tiene variables aleatorias de entrada; **la salida es una estimación, no un valor exacto** — esa es su principal desventaja |
| Cambio de estado | **Continuo**: describe cambios con ecuaciones diferenciales (flujo de tráfico) | **Discreto**: se enfoca en eventos puntuales (autos individuales) |

> **Ojo, punto fino que se toma**: un modelo discreto no necesariamente modela un sistema discreto, ni viceversa. La decisión entre modelo continuo y discreto **depende de los objetivos del estudio**, no del sistema.

### Cuándo se justifica simular

- Complejidad que impide una solución analítica.
- Imposibilidad, costo o riesgo de experimentar con el sistema real.
- Necesidad de control experimental (mucho mayor que en pruebas reales).
- El sistema todavía no existe (fase de diseño).
- Se quiere comprimir un horizonte temporal largo, o expandir el tiempo para estudiar detalles.

### Cuándo NO

- Hay solución analítica disponible y eficiente (ej: M/M/1).
- Existen otros enfoques de modelado válidos.
- El problema no tiene variabilidad significativa.

> Simulación y métodos analíticos son **complementarios**: la simulación puede verificar la validez de los supuestos de un modelo analítico, y un modelo analítico puede sugerir alternativas que después se investigan por simulación.

### Ventajas

- Permite representar sistemas complejos con elementos estocásticos que no se modelan bien analíticamente.
- Estimar el rendimiento del sistema bajo condiciones operativas distintas.
- Comparar diseños o políticas operativas.
- Control experimental muy superior al de pruebas reales.
- Identificación de cuellos de botella.
- Comunicación de resultados más simple (animaciones).

### Desventajas

- **Cada corrida produce una estimación, no un resultado exacto** — hacen falta varias corridas independientes.
- No es tan eficaz para **optimización** como un modelo analítico válido.
- Costosa y lenta de desarrollar.
- Riesgo de exceso de confianza en resultados de un modelo que no es válido.
- Es arte y ciencia a la vez: requiere experiencia.

### Riesgos que hacen fracasar un estudio de simulación

Agrupados como los pide Law:

- **Planificación y comunicación**: objetivos mal definidos al inicio; nivel de detalle inapropiado; no involucrar a todo el equipo desde el principio; falta de comunicación con la gerencia.
- **Conocimiento y enfoque**: tratar el estudio como si fuera solo programar; falta de personal con conocimiento de simulación y estadística; no recopilar buenos datos del sistema real.
- **Software y herramientas**: software inapropiado o con macros poco documentadas; creer que un software fácil no requiere conocimiento técnico; mal uso de la animación.
- **Datos y aleatoriedad**: no considerar correctamente las fuentes de aleatoriedad; usar distribuciones arbitrarias (normal, uniforme, triangular) como entradas sin justificar; no establecer un período de calentamiento para llegar al estado estable.
- **Análisis y resultados**: basar el análisis en **una sola corrida**; comparar diseños con una sola replicación por diseño; medidas de rendimiento incorrectas.

### Áreas de aplicación

Manufactura y logística, sistemas de salud, redes de comunicaciones, transporte, cadenas de suministro, servicios financieros, sistemas militares (armas y tácticas), políticas de pedido de inventarios, evaluación de requerimientos de hardware/software, organizaciones de servicios, ecosistemas.

### Fuentes

- `fuentes/Resumen Simulación.pdf` — Law cap. 1, secciones 1.1, 1.2, 1.8
- `fuentes/resumenes/Resumen 1.pdf` (Pagliaro) — sección 1
- `fuentes/examenes/parciales/2021/2021-10-23.pdf` — preguntas 6 y 11

---

## Unidad 2 — Simulación a eventos discretos (DES)

### Conceptos clave

- **Evento**: ocurrencia instantánea que **puede (o no)** modificar el estado del sistema. Además de cambiar el estado, un evento puede servir para **finalizar la simulación** o para **programar decisiones** en determinados momentos.
- **DES**: modelar un sistema que evoluciona en el tiempo mediante una representación en la cual las variables de estado cambian **solamente en un número contable de instantes** separados en el tiempo.
- **Reloj de simulación**: variable que registra el valor actual del **tiempo simulado**. No tiene relación con el tiempo real que tarda la computadora en correr la simulación.

### Mecanismos de avance del tiempo

| Mecanismo | Cómo funciona | Ventajas / desventajas |
|---|---|---|
| **Próximo evento** (next-event time advance) | El reloj arranca en 0. Se calculan los tiempos de los eventos futuros. El reloj **salta** al evento más próximo, se actualiza el estado y se recalculan los tiempos futuros. Sigue hasta cumplir la condición de parada. | Es el que usa la mayoría del software de simulación. **Omite los períodos de inactividad** → más eficiente. Los saltos del reloj no son de tamaño uniforme. |
| **Incremento fijo** (fixed-increment) | El reloj avanza en intervalos iguales Δt. Después de cada actualización se revisa si ocurrió algún evento en ese intervalo; si los hubo, **se considera que ocurrieron al final del intervalo**. | **No omite** los períodos de inactividad → más costoso. Introduce **error** al procesar eventos al final del intervalo. Obliga a definir reglas de desempate cuando eventos que no son simultáneos se tratan como simultáneos. Se puede achicar Δt, pero eso aumenta el número de revisiones. |

> **Cuándo se usa incremento fijo**: en sistemas donde los eventos ocurren en instantes que son múltiplos de nΔt — por ejemplo, si los datos solo están disponibles anualmente. **No conviene** para modelos donde los tiempos entre eventos varían mucho.

### Componentes de un modelo DES

Nueve componentes. Se toman de memoria:

| Componente | Qué hace |
|---|---|
| **Estado del sistema** | Conjunto de variables que describen el sistema en un tiempo dado |
| **Reloj de simulación** | Indica el valor actual del tiempo simulado |
| **Lista de eventos (LEV)** | Contiene el próximo tiempo en que ocurrirá cada tipo de evento |
| **Contadores estadísticos** | Variables que acumulan información sobre el desempeño del sistema |
| **Rutina de inicialización** | Inicializa la simulación en tiempo 0 |
| **Rutina de temporización** (timing) | Determina el próximo evento de la lista y avanza el reloj a ese instante |
| **Rutinas de eventos** | Una por cada tipo de evento; actualiza el estado del sistema cuando ese evento ocurre |
| **Rutinas de librería** | Generan observaciones aleatorias de las distribuciones definidas en el modelo |
| **Generador de reportes** | Calcula estimaciones de rendimiento y produce el reporte al finalizar |
| **Programa principal** | Invoca la rutina de temporización, transfiere el control a la rutina de evento correspondiente, revisa la finalización e invoca el generador de reportes |

### Flujo de control (el esqueleto de cualquier motor DES)

```
1. Programa Principal
   └─> invoca Rutina de Inicialización

2. Rutina de Inicialización
   ├─ reloj de simulación = 0
   ├─ inicializar estado del sistema y contadores estadísticos
   └─ inicializar lista de eventos

3. Programa Principal (repetidamente, mientras no termine)
   └─> invoca Rutina de Temporización
       ├─ determinar el próximo tipo de evento, i
       ├─ avanzar el reloj de simulación a ese instante
       └─> invoca Rutina de Evento i
           ├─ actualizar el estado del sistema
           ├─ actualizar los contadores estadísticos
           └─ generar eventos futuros y agregarlos a la lista de eventos

4. Al finalizar → Generador de Reportes
   ├─ calcular las estimaciones de interés
   └─ escribir el reporte
```

### Diagrama de desencadenamiento de eventos

> De `fuentes/practica/ejercicios-resueltos/Ejercicio 1 resuelto.pdf` (S. De Federico). Este diagrama es el
> primer punto que piden en casi todos los ejercicios prácticos y en varios finales.

Representa **qué evento provoca que suceda otro evento**, qué eventos se llaman a sí mismos, y qué
evento inicia el sistema. Para la cola simple:

```
      ┌───────────┐                      ┌───────────┐
   ┌─>│  A        │─── si S = 'D' ──────>│  P        │──┐
   └──│  (Arribo) │                      │ (Partida) │<─┘
      └───────────┘                      └───────────┘
       auto-referencia                    si n > 0, auto-referencia
```

- El **Arribo** se llama a sí mismo (cada arribo programa el siguiente) → es el evento que inicia el sistema.
- El Arribo dispara una **Partida** solo si el servidor está desocupado (`S='D'`).
- La **Partida** se llama a sí misma solo si queda gente en cola (`n>0`).

### Tipos de variables en un modelo (vocabulario de la cátedra)

Esta terminología es la que usan los ejercicios de práctica y los finales, y **no aparece en el resumen**:

| Tipo | Qué es | Ejemplo en la cola simple |
|---|---|---|
| **Variables exógenas** | Las variables **aleatorias** que entran al sistema. De ellas hay que conocer su distribución y sus medidas (E[X], Var(X)) para construir o elegir los generadores | Tiempo entre arribos, tiempo de servicio |
| **Variables endógenas** (o de respuesta, o medidas de rendimiento) | Lo que se quiere que el modelo emita como resultado | q(t) tamaño promedio de cola, u(n) utilización, d(n) demora promedio |
| **Variables de estado** | Variables internas que marcan el estado del sistema en un momento dado; participan en la generación de las endógenas | n (tamaño de cola), S (estado del servidor), Reloj, TUE (tiempo del último evento), acumuladores q, b, d |

**Estructuras de datos**:

- **LEV** (Lista de Eventos): una fila por cada evento que existe en el sistema, guardando como mínimo la hora en que va a ocurrir. Se va actualizando durante la corrida.
- **VTA** (Vector de Tiempos de Arribo): guarda los tiempos de arribo de los clientes que entraron a la cola porque el servidor estaba ocupado. Sirve para calcular la demora.

### Notación de la línea de tiempo de eventos

Esta notación se usa en toda la unidad y en la 3:

| Símbolo | Significado |
|---|---|
| $t_i$ | Tiempo de arribo del cliente $i$ (con $t_0 = 0$) |
| $A_i = t_i - t_{i-1}$ | Tiempo **entre** arribos del cliente $i-1$ y el $i$ |
| $S_i$ | Tiempo de servicio del cliente $i$ |
| $D_i$ | Demora (tiempo en cola) del cliente $i$ |
| $c_i = t_i + D_i + S_i$ | Instante en que el cliente $i$ **completa su servicio y se va** |
| $e_i$ | Instante de ocurrencia del evento $i$ (el valor que toma el reloj en ese evento) |

> Se asume que los $A_i$ y los $S_i$ son variables aleatorias **IID** con funciones de distribución acumuladas $F_A$ y $F_S$ respectivamente. IID = independientes e idénticamente distribuidas.

### Traza del método de próximo evento (cola simple)

1. **Inicio.** En $e_0 = 0$ el servidor está inactivo. Se genera $A_1$ de $F_A$ y se lo suma a 0 → primer tiempo de llegada $t_1$. El reloj avanza de $e_0$ a $e_1 = t_1$.
2. **Primera llegada.** El cliente 1 llega en $t_1$. Servidor inactivo → entra a servicio inmediatamente, $D_1 = 0$, servidor pasa a ocupado. Se genera $S_1$ de $F_S$ y se calcula $c_1 = t_1 + S_1$.
3. **Segunda llegada.** Llega en $t_2 = t_1 + A_2$. Si $t_2 < c_1$, el reloj avanza a $e_2 = t_2$. Servidor ocupado → la cola pasa de 0 a 1. **No se genera $S_2$ todavía** (se genera recién cuando entra a servicio).
4. **Tercera llegada.** $t_3 = t_2 + A_3$.
5. **Cambio de evento.** Si $c_1 < t_3$, el reloj avanza a $e_3 = c_1$. El cliente 1 termina y se va; el cliente 2 entra a servicio; se calcula su demora $D_2 = c_1 - t_2$ y su salida $c_2 = c_1 + S_2$. La cola baja en 1.
6. **Fin.** La simulación puede terminar al alcanzar un número específico de observaciones de demoras.

> **Punto conceptual que se toma**: el tiempo de servicio $S_i$ se genera **en el momento en que el cliente entra a servicio**, no cuando llega. Y el tiempo de fin de la simulación es una **variable aleatoria**, porque depende de los arribos y servicios generados.

### Fuentes

- `fuentes/Resumen Simulación.pdf` — Law cap. 1, secciones 1.3, 1.3.1, 1.3.2 y Apéndice 1A
- `fuentes/practica/ejercicios-resueltos/Ejercicio 1 resuelto.pdf` (De Federico) — vocabulario exógenas/endógenas/estado, LEV, VTA, diagrama de desencadenamiento
- `fuentes/resumenes/Resumen 1.pdf` (Pagliaro) — secciones 2 y 2.3

---

## Unidad 3 — Modelo de cola con un servidor

> Es el modelo de referencia de toda la materia. Aparece en el parcial y en todos los finales.

### Planteo del problema

- Los tiempos entre arribos $A_1, A_2, \dots$ son variables aleatorias **IID**.
- Los tiempos de servicio $S_1, S_2, \dots$ son **IID** e **independientes de los arribos**.
- Un cliente que llega y encuentra el servidor libre entra en servicio inmediatamente. Si está ocupado, se une al final de la cola **FIFO**.
- La simulación **comienza en estado vacío e inactivo** (sin clientes, servidor libre).
- El primer arribo ocurre después del primer tiempo entre arribos $A_1$ (no en t = 0).
- La simulación se ejecuta hasta que **n clientes hayan completado su demora en cola** y entren en servicio.
- El tiempo de fin $T(n)$ es una **variable aleatoria**.

### Variables de estado y eventos

| Variable de estado | Para qué sirve |
|---|---|
| Estado del servidor (ocupado/libre) | Determinar si al llegar un cliente puede ser atendido inmediatamente |
| Número de clientes en cola | Decidir si, al terminar un servicio, el servidor queda libre o atiende al siguiente |
| Tiempos de arribo de los clientes en cola | Calcular la demora = tiempo de inicio de servicio − tiempo de arribo |

| Evento | Efecto |
|---|---|
| **Llegada (arribo)** | Si el servidor estaba libre → pasa a ocupado. Si estaba ocupado → cola +1 |
| **Salida (fin de servicio, partida)** | Si no hay cola → servidor pasa a libre. Si hay cola → cola −1 (el servidor sigue ocupado, atiende al siguiente) |

> En este modelo ambos eventos cambian el estado, pero **en general un evento puede no cambiar el estado del sistema**.

### Las tres medidas de rendimiento

Esta es la distinción conceptual más importante de la unidad: **d(n) promedia sobre clientes; q(n) y u(n) promedian sobre tiempo.**

#### 1. d(n) — demora promedio en cola

Demora = tiempo entre el arribo de un cliente y el momento en que **toma servicio**. **No incluye el tiempo de servicio.**

$$\hat{d}(n) = \frac{\sum_{i=1}^{n} D_i}{n}$$

> **No se excluyen** del promedio los $D_i = 0$ (clientes que llegan y encuentran el sistema vacío). Incluirlos ayuda a reflejar el buen desempeño del sistema.

#### 2. q(n) — número promedio de clientes en cola

Promedio **ponderado por tiempo**, no por cliente. Se define con:

- $Q(t)$: número de clientes en la cola en el instante $t$ ($t \ge 0$).
- $T(n)$: tiempo total hasta que $n$ clientes completan sus demoras.
- $T_i$: tiempo total durante el cual hubo exactamente $i$ clientes en cola.
- $p_i = T_i / T(n)$: proporción de tiempo con $i$ clientes en cola.

$$\hat{q}(n) = \sum_{i=0}^{\infty} i \, p_i = \frac{\sum_{i=0}^{\infty} i \, T_i}{T(n)} = \frac{\int_0^{T(n)} Q(t)\,dt}{T(n)}$$

> La sumatoria $\sum i \, T_i$ **es el área bajo la curva $Q(t)$** desde el inicio al fin de la simulación. Eso es lo que hace que la fórmula discreta y la integral sean equivalentes.

#### 3. u(n) — utilización del servidor

Proporción de tiempo, entre 0 y $T(n)$, en que el servidor está ocupado. Su valor está entre 0 y 1.

Se define $B(t) = 1$ si el servidor está ocupado en $t$, y $0$ si está libre. Entonces:

$$\hat{u}(n) = \frac{\text{tiempo total ocupado}}{T(n)} = \frac{\int_0^{T(n)} B(t)\,dt}{T(n)}$$

> **Interpretación**: utilización cercana al 100% → colas largas y posible cuello de botella. Utilización baja → exceso de capacidad, recursos no aprovechados.

Las tres son **estimadores muestrales**: dependen de la corrida particular, por lo que dos corridas del mismo modelo dan valores distintos. De ahí la Unidad 9.

### Ejercicio resuelto tipo — cálculo de q(n) y u(n) por áreas

> Ejemplo del resumen, con $n = 6$. Este es exactamente el tipo de cálculo que puede caer.

**Datos de la trayectoria:**
- Llegadas en los tiempos: 0.4, 1.6, 2.1, 3.8, 4.0, 5.6, 5.8, 7.2
- Salidas en los tiempos: 2.4, 3.1, 3.3, 4.9, 8.6
- La simulación termina en $T(6) = 8.6$

**Cálculo de q(6)** — se acumula cuánto tiempo la cola tuvo longitud $i$:

$$T_0 = (1.6 - 0.0) + (4.0 - 3.1) + (5.6 - 4.9) = 3.2$$
$$T_1 = (2.1 - 1.6) + (3.1 - 2.4) + (4.9 - 4.0) + (5.8 - 5.6) = 2.3$$
$$T_2 = (2.4 - 2.1) + (7.2 - 5.8) = 1.7$$
$$T_3 = (8.6 - 7.2) = 1.4$$
$$T_i = 0 \quad \text{para todo } i \ge 4$$

Suma ponderada (= área bajo $Q(t)$):

$$\sum_{i=0}^{\infty} i \, T_i = (0 \cdot 3.2) + (1 \cdot 2.3) + (2 \cdot 1.7) + (3 \cdot 1.4) = 9.9$$

$$\hat{q}(6) = \frac{9.9}{8.6} = 1.15$$

**Cálculo de u(6)** — tiempo en que el servidor estuvo ocupado:

$$(3.3 - 0.4) + (8.6 - 3.8) = 2.9 + 4.8 = 7.7$$

$$\hat{u}(6) = \frac{7.7}{8.6} = 0.90$$

> El servidor estuvo ocupado el 90% del tiempo. Los huecos son (0, 0.4) antes del primer arribo y (3.3, 3.8) entre que se vacía el sistema y llega el cliente siguiente.

### Ejercicio resuelto tipo — traza paso a paso de la simulación

> Segundo ejemplo del resumen. Acá se ve el mecanismo del reloj y de los acumuladores.

**Datos generados:**
- Tiempos entre arribos: $A_1 = 0.4$, $A_2 = 1.2$, $A_3 = 0.5$, $A_4 = 1.7$, $A_5 = 0.2$, $A_6 = 1.6$, $A_7 = 0.2$, $A_8 = 1.4$, $A_9 = 1.9$, …
- Tiempos de servicio: $S_1 = 2.0$, $S_2 = 0.7$, $S_3 = 0.2$, $S_4 = 1.1$, $S_5 = 3.7$, $S_6 = 0.6$, …

**t = 0 — inicialización**
- Reloj = 0. Servidor libre (estado = 0), cola vacía. Todos los contadores en 0.
- Próxima llegada programada en $0 + A_1 = 0.4$.
- Próxima salida = **∞** (no existe todavía; se pone infinito para que la rutina de temporización elija sí o sí el arribo).
- Áreas acumuladas: $Q = 0$, $B = 0$.

**t = 0.4 — llegada del cliente 1**
- Encuentra el servidor libre → entra directo a servicio. $D_1 = 0$. Clientes con demora completada = 1, tiempo total en cola = 0.
- Servidor pasa a ocupado (estado = 1).
- Próxima llegada: $0.4 + A_2 = 1.6$. Próxima salida: $0.4 + S_1 = 2.4$.
- $B = 0 \times (0.4 - 0) = 0$ · $Q = 0 \times (0.4 - 0) = 0$

**t = 1.6 — llegada del cliente 2**
- Servidor ocupado → espera en la primera posición de la cola. Cola = 1. Se guarda su tiempo de arribo en VTA.
- Próxima llegada: $1.6 + A_3 = 2.1$. Próxima salida sigue siendo 2.4.
- $B = 0 \times 0.4 + 1 \times (1.6 - 0.4) = 1.2$ · $Q = 0 \times 1.6 = 0$

**t = 2.1 — llegada del cliente 3**
- Servidor ocupado → cola = 2. Se guarda su arribo.
- Próxima llegada: $2.1 + A_4 = 3.8$. Próxima salida sigue en 2.4.
- $B = 0 \times 0.4 + 1 \times (2.1 - 0.4) = 1.7$ · $Q = 0 \times 1.6 + 1 \times (2.1 - 1.6) = 0.5$

**t = 2.4 — salida del cliente 1**
- Hay clientes esperando → el servidor toma al cliente 2 y lo atiende inmediatamente. Cola = 1 (queda el cliente 3).
- $D_2 = 2.4 - 1.6 = 0.8$. Demoras completadas = 2, tiempo total en cola = $0 + 0.8 = 0.8$.
- Próxima salida: $2.4 + S_2 = 3.1$.
- $B = 0 \times 0.4 + 1 \times (2.4 - 0.4) = 2.0$ · $Q = 0 \times 1.6 + 1 \times 0.5 + 2 \times (2.4 - 2.1) = 1.1$

> **Patrón a memorizar**: el área se acumula **antes** de actualizar la variable de estado, usando `área += (Reloj − TUE) × valor_viejo`, y recién después se actualiza el valor y se hace `TUE = Reloj`.

### Lógica de las rutinas (versión Law)

**Evento de llegada**

```
1. Programar el siguiente evento de llegada
2. ¿El servidor está ocupado?
   SÍ:
      2.1. Cola += 1
      2.2. ¿Está la cola llena?
           SÍ  → escribir mensaje de error y detener la simulación
           NO  → guardar la hora de llegada de este cliente
   NO:
      2.1. Fijar el tiempo en cola = 0 para este cliente y recopilar estadísticas
      2.2. Incrementar en 1 el número de clientes que completaron la cola
      2.3. Poner el servidor en estado ocupado
      2.4. Programar un evento de salida para este cliente
3. Retornar
```

**Evento de salida**

```
1. ¿Está la cola vacía?
   SÍ:
      1.1. Poner el servidor en estado inactivo
      1.2. Eliminar el evento de salida de consideración (poner en ∞)
   NO:
      1.1. Cola -= 1
      1.2. Calcular el tiempo en cola del cliente que entra en servicio y recopilar estadísticas
      1.3. Incrementar en 1 el número de clientes que completaron tiempo en cola
      1.4. Programar un evento de salida para este cliente
      1.5. Mover cada cliente en cola un lugar hacia adelante
2. Retornar
```

### Pseudocódigo completo con acumuladores (versión cátedra)

> De `fuentes/practica/ejercicios-resueltos/Ejercicio 1 resuelto.pdf`. **Esta es la versión que piden
> escribir en los ejercicios y en los finales** ("hacer una rutina en la que se vea el cálculo de al
> menos una medida de rendimiento").

Acumuladores: `q` (áreas de la cola), `b` (áreas de utilización del servidor), `d` (suma de demoras),
`cli_at` (clientes atendidos), `TUE` (tiempo del último evento), `TIOS` (tiempo en que el servidor
empezó a estar ocupado).

```
PRINCIPAL
  Inicialización
  Mientras Reloj <= Fin_simulación
      Tiempos
      Si evento_seleccionado = 'A'  → ir a Arribo
      Sino                          → ir a Partida
  Fin mientras
  Reporte

TIEMPOS
  Buscar en la LEV el evento con menor tiempo de ocurrencia
  Reloj = ese tiempo

INICIALIZACIÓN
  Reloj = 0 ; q = 0 ; b = 0 ; d = 0
  cli_at = 0                       // clientes atendidos
  n = 0                            // clientes en cola
  S = 'D'                          // servidor desocupado
  Generar tiempo de arribo
  Guardar en LEV(A, tiempo de arribo)
  Guardar en LEV(P, ∞)             // para que Tiempos elija sí o sí el Arribo
  VTA = 0                          // vector de tiempos de arribo
  TUE = 0

ARRIBO
  Si S = 'O'                       // servidor ocupado
      q = q + (Reloj - TUE) * n    // acumular área de la cola ANTES de cambiar n
      n = n + 1
      Guardar Reloj en VTA
  Sino
      S = 'O'
      TIOS = Reloj                 // el servidor empieza a estar ocupado
      cli_at = cli_at + 1
      Generar tiempo de servicio
      Guardar en LEV(P, Reloj + tiempo de servicio)
  Fin Si
  Generar próximo arribo           // el Arribo se llama a sí mismo
  Guardar en LEV(A, Reloj + tiempo de próximo arribo)
  TUE = Reloj

PARTIDA
  Si n = 0
      S = 'D'
      b = b + (Reloj - TIOS)       // acumular área del servidor
      Guardar en LEV(P, ∞)
  Sino
      q = q + (Reloj - TUE) * n
      n = n - 1                    // el primero de la cola entra al servidor
      d = d + (Reloj - VTA[tiempo de ingreso de ese cliente])
      cli_at = cli_at + 1
      Generar tiempo de servicio
      Guardar en LEV(P, Reloj + tiempo de servicio)
  Fin Si
  TUE = Reloj

REPORTE
  q(T)  = q / T                    // tamaño promedio de la cola
  u(T)  = b / T                    // utilización del servidor
  d     = d / cli_at               // demora promedio
```

### Variante: dos servidores en serie (ejercicio 2)

> De `fuentes/practica/ejercicios-resueltos/Ejercicio 2 resuelto.pdf`. Modificaciones al modelo base.

Dos servidores **en serie**, con dos colas. Los clientes que van al servidor 2 son **los que salen del
servidor 1** (ejemplo: recepcionista → médico).

**Punto conceptual clave**: **NO existe una variable exógena "Arribo 2"**. Si la hubiera, sería como si
alguien entrara directamente al médico sin pasar por la recepcionista.

**Eventos**: `A1` (arribo), `P1/A2` (partida del servidor 1 **y** arribo al servidor 2 — es un evento
doble, un solo módulo), `P2` (partida del servidor 2).

Diagrama de desencadenamiento:

```
   A1 ──si S1='D'──> P1/A2 ──si S2='D'──> P2
   ↺                   ↺ (si n1>0)          ↺ (si n2>0)
```

> Notar que en el módulo `P1/A2`, la parte "Arribo servidor 2" **no genera un arribo nuevo** — por eso
> en el diagrama no hay una flecha entera apuntándose a sí misma como en el `A1`.

Todas las variables de estado se duplican: $n_1, n_2$, $S_1, S_2$, $A_{q1}, A_{q2}$, $d_1, d_2$,
$cli\_at_1, cli\_at_2$, $VTA_1, VTA_2$, $TUE_1, TUE_2$.

### La familia completa de ejercicios de práctica

> De `fuentes/practica/ejercicios-resueltos/` (Sara De Federico). Todos son variaciones sobre la cola
> simple, y **es de acá que salen los ejercicios de los finales**. Vale la pena tener claro qué cambia
> en cada uno, porque el enunciado del examen siempre es una variante nueva de esta familia.

| Ejercicio | Sistema | Qué cambia respecto de la cola simple |
|---|---|---|
| **Base 2016** | Cola simple **sin medidas de rendimiento** | Es el esqueleto mínimo para que la simulación corra. Sirve de base para construir cualquier otro |
| **1** | Cola simple completa | Agrega los acumuladores $q$, $b$, $d$ y las tres medidas de rendimiento |
| **2** | **Dos servidores en serie** | Dos colas; el evento `P1/A2` es **doble**; no hay variable exógena "arribo 2" |
| **3** | **$k$ servidores en paralelo** | Un solo arribo, **$k$ eventos de partida $P_i$** ($i = 1..k$). En el diagrama se representan con un **nodo de doble línea** (doble círculo). Todos los servidores tienen la misma distribución de servicio |
| **6** | **$k$ operarios reparando 5 máquinas** | **Población finita** (5 máquinas) → la población finita **delimita también el tamaño de la cola**. Cada cliente es individual y su arribo es exclusivo: una máquina en cola **no puede volver a romperse**. La cola **no es FIFO**: hay prioridad por tiempo de reparación (la cola se vuelve un vector ordenado de menor a mayor). La medida de rendimiento es un **costo** |
| **7.1** | **Dos secciones en serie, la segunda con $k$ servidores** | Se pide **identificar el objetivo de optimización** antes de modelar, y elegir las medidas apropiadas según qué problema se detecte (servidores ociosos vs. cola colapsada) |

**El nodo de doble círculo** (ejercicio 3) es notación de la cátedra y aparece en el final 2017: *"era
un arribo simple y partida con doble círculo, para considerar los 4 consultorios"*. Significa **$k$
instancias del mismo evento**:

```
      ┌───────────┐                      ╔═══════════╗
   ┌─>│  A        │─── si Sᵢ = 'D' ─────>║  Pᵢ       ║──┐
   └──│  (Arribo) │                      ║ i = 1..k  ║<─┘
      └───────────┘                      ╚═══════════╝
                                          si n > 0
```

**Detalle del ejercicio 6 que se puede preguntar** — en población finita, la máquina no sale
físicamente del sistema al ser reparada: queda **inutilizada para trabajar** mientras espera y se
repara, y recién cuando termina la reparación se puede determinar cuándo se volverá a descomponer.
Por eso en el diagrama la flecha va **desde el evento de reparación $R_k$ hacia el de descompostura
$D_i$**, y no al revés. La medida de rendimiento es el costo por hora:

$$\text{Costo promedio por hora} = \frac{50 \times A_{hd} + 10 \times k}{800}$$

donde $A_{hd}$ es la acumulada de horas de máquina detenida y $k$ la cantidad de operarios. Se hace
**una corrida por cada $k$** y se compara.

> **Lo que suelen pedir en el examen** (final 2017, final 2015): (a) el diagrama de desencadenamiento
> de eventos, (b) **qué información falta** en el enunciado, (c) las medidas de rendimiento
> apropiadas, (d) una rutina en pseudocódigo donde se vea el cálculo de al menos una medida, y (e) el
> análisis de resultados **específico para ese ejercicio**, no la teoría general. La consigna suele
> traer datos de contexto que **no forman parte del modelo** — hay que identificarlos y descartarlos.
>
> Y "en los ejercicios se suele pedir **un esquema del sistema real**", que es un dibujo aparte del
> diagrama de eventos.

### Fuentes

- `fuentes/Resumen Simulación.pdf` — Law cap. 1, secciones 1.4, 1.4.1, 1.4.3
- `fuentes/practica/ejercicios-resueltos/Ejercicio 1 resuelto.pdf` y `Ejercicio 2 resuelto.pdf` (De Federico)
- `fuentes/resumenes/Resumen 1.pdf` (Pagliaro) — sección 3

---

## Unidad 4 — Modelo de inventarios (s, S)

> Pregunta fija en el parcial (2021-10 P1 y P16, 2021-12 P5) y en el final oral (2020-08).

### Planteo del problema

Una empresa vende **un solo producto** y quiere decidir cuántos ítems tener en inventario durante los
próximos $n$ meses. El objetivo es **comparar políticas de pedido** distintas.

- **Tiempo entre demandas**: variables aleatorias IID con distribución **exponencial**, media 0.1 meses.
- **Tamaño de la demanda $D$**: variable aleatoria IID (independiente del momento en que ocurre la demanda), con una distribución discreta dada (típicamente D ∈ {1,2,3,4} con sus probabilidades).
- **Revisión periódica**: al **comienzo de cada mes** la empresa revisa su nivel de inventario y decide cuántos artículos pedir.

### Política de reordenamiento (s, S)

Siendo $I$ el nivel de inventario al comienzo del mes, y $Z$ la cantidad a pedir:

$$Z = \begin{cases} S - I & \text{si } I < s \\ 0 & \text{si } I \ge s \end{cases}$$

- **$s$** = punto de pedido (reorder point).
- **$S$** = tope (nivel objetivo).

**Costo de pedido**: $K + i\,Z$, donde $K$ es el **costo fijo** de pedido e $i$ es el **costo por artículo** pedido. Si $Z = 0$, no se incurre en ningún costo.

**Tiempo de entrega (lead time)**: variable aleatoria **uniforme entre 0.5 y 1 mes**.

### Backlog e inventario negativo

- Si hay suficiente inventario, la demanda se satisface de inmediato.
- Si la demanda supera el inventario disponible, el excedente queda **en espera (backlog)** y se cubre con futuras entregas. **Esto hace que el inventario pueda ser negativo.**
- Cuando llega un pedido, primero cubre el backlog y el resto (si queda) se suma al inventario.

> **Pregunta frecuente #9 — diferencia con Investigación Operativa**: en IO el control del inventario es
> **continuo** y el pedido se dispara apenas se llega al nivel mínimo. Acá el control es **periódico**
> (una revisión al inicio de cada mes), y por eso pueden generarse niveles **negativos** de inventario
> entre revisiones.

### Los tres niveles de inventario

| Símbolo | Definición | Significado |
|---|---|---|
| $I(t)$ | Nivel de inventario en el instante $t$ | Puede ser positivo, cero o **negativo** |
| $I^+(t) = \max\{I(t), 0\}$ | Artículos en **existencia física** en $t$ | Lo que realmente hay en el depósito |
| $I^-(t) = \max\{-I(t), 0\}$ | Cantidad en **backlog** en $t$ | Unidades demandadas y no entregadas por falta de stock |

Promedios sobre el período de $n$ meses:

$$\bar{I}^+ = \frac{\int_0^n I^+(t)\,dt}{n} \qquad\qquad \bar{I}^- = \frac{\int_0^n I^-(t)\,dt}{n}$$

### Los costos (esto es lo que preguntan textual)

| Costo | Fórmula | Qué incluye |
|---|---|---|
| **Costo de pedido** | $C_p = K + i\,Z$ | $K$ costo fijo, $i$ costo por artículo, $Z$ cantidad pedida |
| **Costo de almacenamiento** (holding, $h$) | $C_{pa} = \bar{I}^+ \cdot h$ | Alquiler del almacén, seguros, impuestos, mantenimiento y **costo de oportunidad del capital inmovilizado** |
| **Costo por faltante** (shortage, $\pi$ o $p$) | $C_{pr} = \bar{I}^- \cdot \pi$ | Costos administrativos y **pérdida de buena voluntad** de los clientes |

$$\text{Costo total promedio mensual} = \frac{\text{costo de pedido acumulado}}{n} + \bar{I}^+ h + \bar{I}^- \pi$$

> **Cuidado con un error que circula en los exámenes resueltos**: en el parcial 2021-12-02 la respuesta
> a la pregunta 5 invierte $h$ y $\pi$, y también confunde $i$ con $Z$. La versión correcta es la de
> arriba y la del parcial 2021-10-23: **$h$ va con $I^+$** (lo que tenés guardado) y **$\pi$ va con
> $I^-$** (lo que debés). Y en $K + iZ$, $i$ es el costo unitario y $Z$ la cantidad.

### Los cuatro tipos de evento (y por qué el orden importa)

> Detalle fino del apunte de Weitz (Law §1.5.2) que se presta para pregunta de parcial.

| Evento | Tipo |
|---|---|
| Arribo de un pedido del proveedor a la empresa | **1** |
| Demanda del producto por parte de un cliente | **2** |
| **Fin de la simulación** después de $n$ meses | **3** |
| Evaluación de inventario (y posible pedido) al comienzo del mes | **4** |

**Por qué el fin de simulación es el tipo 3 y no el 4**: en el instante $t = n$ quedan programados
**los dos** eventos —"fin de simulación" y "evaluación de inventario"— y se quiere que se ejecute
primero el fin. Como la simulación ya terminó, **no tiene sentido evaluar el inventario y
eventualmente pedir**, incurriendo en un costo de pedido por una orden que nunca va a llegar. La
rutina de temporización, ante un empate de tiempos, **le da preferencia al evento de número más
bajo** — por eso se le asigna el 3.

> **Regla general que vale la pena recordar**: un modelo de simulación debe diseñarse para procesar
> los eventos en el orden apropiado cuando hay empates de tiempo.

**Variables de estado del modelo**: el nivel de inventario $I(t)$, la **cantidad de un pedido
pendiente** de la empresa al proveedor, y el **tiempo del último evento** (necesario para computar las
áreas bajo $I^+(t)$ e $I^-(t)$).

**Diagrama de eventos** (event graph, fig. 1.55 de Law): cuatro nodos — *Order arrival*, *Demand*,
*Evaluate*, *End simulation*. **Demand** y **Evaluate** se auto-programan (arco que vuelve sobre sí
mismos). De **Evaluate** sale un arco hacia **Order arrival**. **End simulation** se programa una sola
vez al inicio.

### Los tres generadores que hace falta programar

1. **Tiempos entre demandas** → exponencial, mismo algoritmo que en la cola simple: $t = -E[X]\ln r$.
2. **Tamaño de la demanda $D$** → discreta, por transformada inversa: se divide el intervalo unitario en subintervalos **contiguos** definidos por las **probabilidades acumuladas**, y se devuelve el $D$ del subintervalo en el que cae $U$. Con los valores canónicos de Law ($D=1,2,3,4$ con $p = 1/6, 1/3, 1/3, 1/6$): $C_1 = [0,\frac{1}{6})$, $C_2 = [\frac{1}{6},\frac{1}{2})$, $C_3 = [\frac{1}{2},\frac{5}{6})$, $C_4 = [\frac{5}{6},1]$. El ancho de cada subintervalo **es** la probabilidad buscada — de ahí que el método funcione.
3. **Demora del proveedor** → uniforme en $[a,b]$: $a + U(b-a)$.

### Parámetros del caso canónico de Law

Por si te dan el ejercicio "como se vio en clase" sin datos:

| Parámetro | Valor |
|---|---|
| Media del tiempo entre demandas | 0,1 mes |
| $D$ | 1 ($p=1/6$), 2 ($p=1/3$), 3 ($p=1/3$), 4 ($p=1/6$) |
| Lead time | Uniforme en $[0{,}5;\ 1]$ mes |
| $K$ (setup cost) | \$32 |
| $i$ (incremental cost) | \$3 |
| $h$ (holding cost) | \$1 por ítem por mes |
| $\pi$ (backlog cost) | \$5 por ítem por mes |
| $I(0)$ | 60, sin pedidos pendientes |
| $n$ | 120 meses |

Y se comparan **nueve políticas** $(s,S)$:

| $s$ | 20 | 20 | 20 | 20 | 40 | 40 | 40 | 60 | 60 |
|---|---|---|---|---|---|---|---|---|---|
| $S$ | 40 | 60 | 80 | 100 | 60 | 80 | 100 | 80 | 100 |

usando el **costo total promedio por mes** (suma de los tres costos promedio) como criterio.

> **Nota de Law que se puede citar**: se ignora que sigue habiendo costos de almacenamiento cuando
> $I^+(t) = 0$. Como el objetivo es **comparar** políticas y ese costo es independiente de la política
> usada, ignorarlo no afecta la decisión de cuál es la mejor.

### Lógica de las rutinas

**Evento de llegada de pedido**
```
1. Incrementar el nivel de inventario en la cantidad previamente pedida
2. Eliminar el evento de llegada de pedido de consideración (∞)
3. Retornar
```

**Evento de demanda**
```
1. Generar el tamaño de esta demanda
2. Disminuir el nivel de inventario en ese tamaño
3. Programar el siguiente evento de demanda
4. Retornar
```

**Evento de evaluación de inventario** (el que corre al inicio de cada mes)
```
1. ¿I(t) < s?
   SÍ:
      1.1. Determinar la cantidad a pedir: Z = S - I(t)
      1.2. Incluir el costo de pedido (K + i·Z) y acumular estadísticas
      1.3. Programar el evento de llegada de pedido para esta orden
           (Reloj + lead time, uniforme entre 0.5 y 1)
2. Programar el siguiente evento de evaluación de inventario (Reloj + 1 mes)
3. Retornar
```

**Actualizar acumuladores estadísticos de tiempo promedio**
```
1. ¿Fue I(t) durante el intervalo anterior negativo, cero o positivo?
   Negativo → actualizar el área debajo de I⁻(t)
   Positivo → actualizar el área debajo de I⁺(t)
   (Cero    → no acumula en ninguno de los dos)
2. Retornar
```

**Diagrama de desencadenamiento de eventos**

```
   Control de inventario ──> Arribo de pedido
        ↺ (auto-referencia)

   Demanda
        ↺ (auto-referencia)
```

> Los dos eventos auto-referenciados (Control de inventario y Demanda) son los que sostienen el
> avance del sistema; el Arribo de pedido solo lo dispara el Control.

### Medidas de desempeño (nomenclatura de la cátedra)

Del final resuelto 2020-08-06:

| Medida | Fórmula | Qué es |
|---|---|---|
| CCP | $ACP / \text{Reloj}$ | Costo de la cantidad pedida (ACP = acumulado de cantidad pedida) |
| CUI | $AIP \cdot h$ | Costo de las unidades en inventario (AIP = acumulado inventario positivo) |
| CUP | $AIN \cdot \pi / \text{Reloj}$ | Costo de las unidades perdidas (AIN = acumulado inventario negativo) |
| **CMP** | $CCP + CUI + CUP$ | **Costo mensual promedio** — es la medida que se compara entre políticas |

### Ejercicio resuelto tipo — simulación numérica del inventario a mano

> ⚠️ **Esto apareció como ejercicio en los parciales 2024 (P2) y 2025 (punto 3).** Es el único ejercicio
> de cálculo numérico de los parciales recientes. Te dan los parámetros y **cinco números aleatorios**,
> y tenés que llegar al costo total promedio mensual.

**Consigna 2025-10-04**: determinar el costo total promedio mensual para un sistema de inventario con
la política de pedidos vista en clase, con estos datos:

| Dato | Valor |
|---|---|
| Tiempo entre demandas | Exponencial con **media 0,55** |
| Demora del proveedor (lead time) | Uniforme en $[0{,}5;\ 1]$ |
| Tamaño de la demanda | $D=3$ con $p=1/3$ · $D=4$ con $p=1/6$ · $D=5$ con $p=1/6$ · $D=6$ con $p=1/3$ |
| Costos | $K = 50$ · $i = 5$ · $h = 2{,}5$ · $\pi = 6$ |
| Política e inicio | $s = 30$ · $S = 60$ · $I_0 = 40$ |
| Números aleatorios | 0,9501 — 0,1304 — 0,9700 — 0,3546 — 0,9258 |

*(La versión 2024 es idéntica en estructura: media 0,4, lead time uniforme $[0{,}2;0{,}6]$, $D$ con
probabilidades 1/8, 1/4, 3/8, 1/4, $K=20$, $i=5$, $h=2{,}5$, $\pi=6$, $s=15$, $S=30$, $I_0=20$,
números 0,9015 — 0,1096 — 0,8901 — 0,3546 — 0,9317.)*

#### Paso 1 — armar los tres generadores por transformada inversa

**a) Tiempo entre demandas** (exponencial, media $E[X] = 0{,}55$, o sea $\alpha = 1/0{,}55$):

$$t = -E[X]\ln r = -0{,}55\,\ln r$$

**b) Tamaño de la demanda** (discreta) — se acumula la distribución:

| $D$ | $p$ | $F(D)$ acumulada | Intervalo de $r$ |
|---|---|---|---|
| 3 | 1/3 ≈ 0,3333 | 0,3333 | $0 \le r < 0{,}3333$ |
| 4 | 1/6 ≈ 0,1667 | 0,5000 | $0{,}3333 \le r < 0{,}5000$ |
| 5 | 1/6 ≈ 0,1667 | 0,6667 | $0{,}5000 \le r < 0{,}6667$ |
| 6 | 1/3 ≈ 0,3333 | 1,0000 | $0{,}6667 \le r \le 1$ |

**c) Demora del proveedor** (uniforme en $[a,b] = [0{,}5;\ 1]$):

$$L = a + (b-a)\,r = 0{,}5 + 0{,}5\,r$$

#### Paso 2 — precalcular los valores de cada número aleatorio

Conviene hacer esta tabla primero, porque no sabés de antemano para qué se va a usar cada número:

| $r$ | Como tiempo: $-0{,}55\ln r$ | Como demanda | Como lead time: $0{,}5+0{,}5r$ |
|---|---|---|---|
| 0,9501 | $-0{,}55 \times (-0{,}05119) = 0{,}0282$ | 6 | 0,9751 |
| 0,1304 | $-0{,}55 \times (-2{,}03715) = 1{,}1204$ | 3 | 0,5652 |
| 0,9700 | $-0{,}55 \times (-0{,}03046) = 0{,}0168$ | 6 | 0,9850 |
| 0,3546 | $-0{,}55 \times (-1{,}03677) = 0{,}5702$ | 4 | 0,6773 |
| 0,9258 | $-0{,}55 \times (-0{,}07710) = 0{,}0424$ | 6 | 0,9629 |

#### Paso 3 — correr los eventos

Los números se consumen **en el orden dado, a medida que la simulación los necesita**. Arranca así:

**$t = 0$ — Evaluación de inventario.** $I = 40$. ¿$I < s$? $40 \not< 30$ → **$Z = 0$, no se pide nada, costo de pedido = 0.** Se programa la próxima evaluación en $t = 1$.
Se genera el primer tiempo entre demandas con $r_1 = 0{,}9501$ → $0{,}0282$. Próxima demanda en $t = 0{,}0282$.

**$t = 0{,}0282$ — Demanda.** Tamaño con $r_2 = 0{,}1304$ → $D = 3$. $I: 40 \to 37$.
Área acumulada de $I^+$: $40 \times (0{,}0282 - 0) = 1{,}128$.
Próximo tiempo entre demandas con $r_3 = 0{,}9700$ → $0{,}0168$. Próxima demanda en $t = 0{,}0450$.

**$t = 0{,}0450$ — Demanda.** Tamaño con $r_4 = 0{,}3546$ → $D = 4$. $I: 37 \to 33$.
Área acumulada de $I^+$: $+\ 37 \times (0{,}0450 - 0{,}0282) = 0{,}622$ → total 1,750.
Próximo tiempo con $r_5 = 0{,}9258$ → $0{,}0424$. Próxima demanda en $t = 0{,}0874$.

**$t = 0{,}0874$ — Demanda.** Acá **se agotan los números aleatorios provistos**: harían falta más para
el tamaño de esta demanda y para seguir.

> ⚠️ **Confirmar con la cátedra el protocolo exacto**: con cinco números y el orden de consumo natural
> (tiempo, tamaño, tiempo, tamaño, tiempo…) la simulación no llega ni al primer mes, así que el
> enunciado tiene que estar asumiendo otra cosa — por ejemplo que los cinco números son **solo tamaños
> de demanda** con tiempos entre demandas dados por la media, o que la corrida es de un número fijo de
> demandas y no de meses. **El procedimiento de arriba es el correcto; lo que falta confirmar es cuántos
> eventos hay que simular y en qué orden se consumen los números.**

#### Paso 4 — cerrar el cálculo de costos

Una vez terminada la corrida de $n$ meses, se arma:

$$\bar{I}^+ = \frac{\text{área acumulada bajo } I^+(t)}{n} \qquad \bar{I}^- = \frac{\text{área acumulada bajo } I^-(t)}{n}$$

$$\boxed{\text{CMP} = \underbrace{\frac{\sum (K + iZ)}{n}}_{\text{costo de pedido}} \ +\ \underbrace{\bar{I}^+ \cdot h}_{\text{almacenamiento}} \ +\ \underbrace{\bar{I}^- \cdot \pi}_{\text{faltante}}}$$

**Checklist para no perder puntos en este ejercicio:**

- [ ] Acumular el área **antes** de actualizar $I$, con `área += (Reloj − TUE) × I_viejo`.
- [ ] Separar el área en $I^+$ y $I^-$ según el **signo de $I$ en el intervalo anterior**, no en el actual.
- [ ] El costo de pedido solo se cobra si $Z > 0$ (si $I \ge s$ no hay costo, **ni siquiera el fijo $K$**).
- [ ] El pedido **no llega en el momento**: llega en $t + L$ con $L$ generado uniforme.
- [ ] Cuando llega el pedido, primero **cubre el backlog** y el resto va al inventario.
- [ ] Dividir por $n$ (meses), no por la cantidad de eventos.

### Fuentes

- `fuentes/Resumen Simulación.pdf` — Law cap. 1, secciones 1.5, 1.5.1, 1.5.2
- `fuentes/examenes/parciales/2021/2021-10-23.pdf` — preguntas 1 y 16
- `fuentes/examenes/finales/Final 2020-08-06 (Resuelto).docx`
- `fuentes/teoria-flamini/Plantilla Inventario.pdf`

---

## Unidad 5 — Pasos de un estudio de simulación

> ⚠️ **Hay dos listas de 10 pasos distintas** y las dos circulan en los exámenes. La de **Law** y la de
> **Weitz**. Los parciales resueltos usan la de **Weitz** (hablan de "escenario pesimista, optimista e
> intermedio", que solo aparece ahí). El enunciado del TPI, en cambio, usa la de **Law**. Conviene
> saber las dos y, si te piden "desarrolle los pasos a) y b)", identificar por el vocabulario cuál te
> están pidiendo.

### Los 10 pasos de Law

1. **Formular el problema y planificar el estudio.** El problema lo plantea el gerente, pero puede no estar bien definido — es un proceso iterativo. Reuniones iniciales con gerente, analistas y expertos (SMEs) para definir: objetivos generales y preguntas específicas, métricas de desempeño, alcance del modelo y configuraciones a modelar, cronograma y recursos. Seleccionar el software de simulación.
2. **Recopilar datos y definir el modelo.** Ninguna persona ni documento alcanza por sí solo; puede haber información errónea (hay que identificar a los verdaderos expertos); los procedimientos pueden no estar formalizados. Obtener datos para parámetros y distribuciones. **Redactar un documento de supuestos.** Si se puede, recopilar datos del sistema actual para validar después. Elegir el nivel de detalle según objetivos, disponibilidad de datos, credibilidad, opiniones de expertos y limitaciones de recursos. **No debe haber correspondencia uno a uno entre cada elemento del modelo y cada elemento del sistema.** Empezar simple y crecer.
3. **Validar el documento de supuestos.** Revisión estructurada ante gerentes, analistas y expertos. Asegura corrección y completitud, fomenta la apropiación del modelo, y **debe hacerse antes de programar** para evitar reprocesos.
4. **Construir y verificar el programa.** Programar el modelo y **verificarlo** (debugging): asegurar que corre como se pretendía.
5. **Realizar corridas piloto.** Ejecuciones preliminares para preparar la validación.
6. **Validar el modelo programado.** Si existe un sistema real, comparar resultados del modelo con datos reales. Revisión por analistas y expertos. **Análisis de sensibilidad** para identificar los factores críticos.
7. **Diseñar experimentos.** Para cada configuración: duración de la simulación, período de calentamiento (si aplica), número de repeticiones independientes (con distintos números aleatorios).
8. **Realizar corridas de producción.** Corridas completas para el análisis formal.
9. **Analizar los datos de salida.** Desempeño absoluto de cada configuración y comparación relativa entre alternativas.
10. **Documentar, presentar y utilizar resultados.** Documentar supuestos, programa y resultados. Usar animaciones para audiencias no técnicas. Explicar el proceso de modelado y validación para ganar credibilidad. Usar los resultados en la toma de decisiones si son válidos y creíbles.

> **Verificación vs. validación** — se toma seguido:
> - **Verificación** (paso 4): ¿el programa hace lo que yo quise programar? Es debugging.
> - **Validación** (pasos 3 y 6): ¿el modelo representa el sistema real? Se hace comparando con datos reales y con el juicio de los expertos.

### Los 10 pasos de Weitz

1. **Definición del sistema bajo estudio.** Establecer objetivos y supuestos. Definir variables de decisión, sus interacciones y alcances. Desarrollar el modelo conceptual con fronteras, elementos, flujos y variables clave.
2. **Generación del modelo base.** Traducir el modelo conceptual a lenguaje de simulación. Incluir interrelaciones entre subsistemas. Definir animaciones si hacen falta. Incorporar variables aleatorias y sus distribuciones. **No demasiado detallado.**
3. **Recolección y análisis de datos.** Recopilar información estadística de las variables aleatorias. Validar calidad y formato. Si la información es insuficiente, hacer estudios estadísticos. Identificar las distribuciones de probabilidad apropiadas.
4. **Generación del modelo preliminar.** Integrar análisis de datos, supuestos e información requerida. Estimar rangos de variación o valores constantes para procesos nuevos. Sugerir distribuciones basadas en experiencia.
5. **Verificación del modelo.** Comprobar la correcta programación. Validar el funcionamiento de los parámetros. Detectar errores de programación o de alimentación de datos. Actualizar supuestos si cambiaron durante el desarrollo.
6. **Validación del modelo.** Probar el modelo con información real o condiciones actuales de operación. Validar el comportamiento con las expectativas del cliente. Justificar comportamientos contrarios a la experiencia de los especialistas. Para procesos nuevos, usar escenarios sugeridos por el cliente.
7. **Generación del modelo final.** Modelo validado y listo. **Será el modelo base para comparar escenarios** (modelo raíz).
8. **Definición de escenarios.** Acordar con el cliente los escenarios a analizar. **Se suele usar: pesimista, optimista e intermedio** para la variable de respuesta más importante. Considerar múltiples variables de respuesta. Usar las herramientas de simulación para múltiples réplicas. El analista también puede sugerir escenarios que considere importantes, para reducir las combinaciones posibles.
9. **Análisis de sensibilidad.** Comparar estadísticamente los mejores escenarios. Analizar la **intersección de los intervalos de confianza**. Si hay traslape, hacer más réplicas o aumentar el tiempo de simulación para acortar los intervalos y poder diferenciar las soluciones.
10. **Documentación y conclusiones.** Documentar el modelo completo para uso futuro: supuestos, distribuciones, alcances, limitaciones, consideraciones de programación. Agregar sugerencias sobre el uso del modelo y sobre los resultados. Presentar conclusiones. Elaborar reportes ejecutivos para la presentación final.

### Cómo se toma esto en el parcial

La forma típica es: *"Desarrolle los siguientes pasos a) y b) en la realización de un estudio de
simulación: a) la determinación de los escenarios para el análisis, b) la documentación del modelo,
sugerencias y conclusiones"* (parcial 2021-10 P5 y 2021-12 P6). Eso es **Weitz pasos 8 y 10**.

Otra variante: *"Luego de la definición del sistema bajo estudio y la generación del modelo de
simulación base, se debe efectuar: a) la recolección y el análisis de datos, y b) la generación del
modelo preliminar"* (parcial 2021-10 P14). Eso es **Weitz pasos 3 y 4**.

> Es decir: **te dan el nombre del paso y tenés que desarrollarlo**. Vale la pena memorizar el nombre
> exacto de los 10 pasos de Weitz en orden.

### Fuentes

- `fuentes/Resumen Simulación.pdf` — Law 1.7 y Weitz 1.5
- `fuentes/examenes/parciales/2021/2021-10-23.pdf` — preguntas 5 y 14
- `fuentes/examenes/parciales/2021/2021-12-02.txt` — pregunta 6
- `fuentes/examenes/finales/Final 2020-08-06 (Resuelto).docx`

---
## Unidad 6 — Elementos de probabilidad

> Ross, *Simulation*, cap. 2. En los parciales 2022, 2023 y 2024 hay **tres preguntas de esta unidad**
> (esperanza/varianza con demostración, una variable aleatoria a elección, y proceso de Poisson).

### 6.1 Espacio muestral y eventos

- **$S$**: espacio muestral, el conjunto de todos los resultados posibles del experimento.
- **$A$**: evento, subconjunto de $S$ formado por resultados posibles.
- **Unión** $A \cup B$: los resultados que están en $A$, en $B$ o en ambos.
- **Intersección** $AB$ (o $A \cap B$): los resultados que están en $A$ **y** en $B$.
- **Complemento** $A^c$: todos los resultados de $S$ que **no** están en $A$. $A^c$ ocurre ⟺ $A$ no ocurre. $S^c = \emptyset$.
- **Mutuamente excluyentes**: si $AB = \emptyset$, $A$ y $B$ no pueden ocurrir a la vez.

### 6.2 Axiomas de probabilidad

Para cada evento $A$ existe un número $P(A)$ que cumple:

| Axioma | Enunciado | Lectura |
|---|---|---|
| **1** | $0 \le P(A) \le 1$ | La probabilidad de que el resultado esté en $A$ es un número entre 0 y 1 |
| **2** | $P(S) = 1$ | Con probabilidad 1, el resultado es un elemento del espacio muestral |
| **3** | $P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i)$ para eventos mutuamente excluyentes | Para eventos mutuamente excluyentes, la probabilidad de que **al menos uno** ocurra es la suma de sus probabilidades |

**Consecuencia inmediata**: como $A$ y $A^c$ son mutuamente excluyentes y $A \cup A^c = S$:

$$1 = P(S) = P(A \cup A^c) = P(A) + P(A^c) \implies \boxed{P(A^c) = 1 - P(A)}$$

### 6.3 Probabilidad condicional e independencia

$$P(A|B) = \frac{P(AB)}{P(B)}$$

Si $P(A|B) = P(A)$, entonces $A$ y $B$ son **independientes** y se cumple $P(AB) = P(A)\,P(B)$. La relación es **simétrica**: si $A$ es independiente de $B$, $B$ es independiente de $A$.

### 6.4 Variables aleatorias

Una **variable aleatoria** es una cantidad numérica determinada por el resultado del experimento. Su **función de distribución** es:

$$F(x) = P(X \le x)$$

- **Discreta**: asume un número finito (o contable) de valores. Su **función de masa de probabilidad** es $p(x) = P(X = x)$, con $\sum_{i=1}^{\infty} p(x_i) = 1$.
- **Continua**: existe una función no negativa $f(x)$ (densidad) tal que para cualquier conjunto $C$ de reales, $P(X \in C) = \int_C f(x)\,dx$. El conjunto de valores posibles es un intervalo.

### 6.5 Esperanza

$$E[X] = \sum_i x_i\,P(X = x_i) \quad \text{(discreta)} \qquad\qquad E[X] = \int_{-\infty}^{\infty} x\,f(x)\,dx \quad \text{(continua)}$$

**Propiedad 1** — $E[aX + b] = a\,E[X] + b$ (se pide demostrar en el parcial 2022 P7 y globalizador 2023 P1):

$$E[aX+b] = \sum_x (ax + b)\,p(x) = a\sum_x x\,p(x) + b\sum_x p(x) = a\,E[X] + b\cdot 1 = a\,E[X] + b$$

> El truco de la demostración es que $\sum_x p(x) = 1$.

**Propiedad 2** — linealidad: $E[X_1 + X_2] = E[X_1] + E[X_2]$, generalizable a

$$E\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n E[X_i]$$

> Esta propiedad vale **aunque las variables no sean independientes**.

### 6.6 Varianza

Si $X$ tiene media $\mu$:

$$\mathrm{Var}(X) = E[(X - \mu)^2]$$

**Forma alternativa** (la que se usa siempre para calcular):

$$\mathrm{Var}(X) = E[(X-\mu)^2] = E[X^2 - 2\mu X + \mu^2] = E[X^2] - 2\mu E[X] + \mu^2 = E[X^2] - \mu^2 = \boxed{E[X^2] - (E[X])^2}$$

**Propiedad** — $\mathrm{Var}(aX + b) = a^2\,\mathrm{Var}(X)$ (se pide demostrar en el parcial 2024 P6):

$$\begin{aligned}
\mathrm{Var}(aX+b) &= E[(aX+b)^2] - (E[aX+b])^2 \\
&= E[a^2X^2 + 2abX + b^2] - (a\,E[X] + b)^2 \\
&= a^2E[X^2] + 2ab\,E[X] + b^2 - \left(a^2(E[X])^2 + 2ab\,E[X] + b^2\right) \\
&= a^2E[X^2] - a^2(E[X])^2 \\
&= a^2\left(E[X^2] - (E[X])^2\right) = a^2\,\mathrm{Var}(X)
\end{aligned}$$

> **Lectura**: la constante aditiva $b$ **no afecta la varianza** (desplaza la distribución sin cambiar su dispersión); la constante multiplicativa entra **al cuadrado**.

**Varianza de una suma de independientes**: si los $X_i$ son independientes, $\mathrm{Var}\left(\sum X_i\right) = \sum \mathrm{Var}(X_i)$.

### 6.7 Chebyshev y las leyes de los grandes números

#### Desigualdad de Markov

Si $X$ solo toma valores no negativos, para cualquier $a > 0$:

$$P(X \ge a) \le \frac{E[X]}{a}$$

*Demostración*: se define $Y = a$ si $X \ge a$, y $Y = 0$ si $X < a$. Entonces $E[Y] = a\,P(X \ge a) + 0\cdot P(X<a) = a\,P(X\ge a)$. Como $X \ge 0$, se tiene $X \ge Y$, luego $E[X] \ge E[Y] = a\,P(X \ge a)$, y despejando queda el resultado.

#### Desigualdad de Chebyshev

Si $X$ tiene media $\mu$ y varianza $\sigma^2$, para cualquier $k > 0$:

$$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$

*Demostración*: se aplica Markov a la variable $(X-\mu)^2/\sigma^2$, cuya esperanza es
$E\left[\frac{(X-\mu)^2}{\sigma^2}\right] = \frac{1}{\sigma^2}E[(X-\mu)^2] = \frac{1}{\sigma^2}\mathrm{Var}(X) = 1$, con $a = k^2$.

> **Lectura**: acota la probabilidad de alejarse de la media más de $k$ desvíos, **sin conocer la distribución**. Con $k=2$: a lo sumo el 25% de la masa está a más de 2 desvíos.

#### Ley Débil de los Grandes Números

Sea $X_1, X_2, \dots$ una sucesión IID con media $\mu$. Para cada $\epsilon > 0$:

$$P\left(\left|\frac{X_1 + \dots + X_n}{n} - \mu\right| > \epsilon\right) \to 0 \quad \text{cuando } n \to \infty$$

*Idea de la demostración*: se define $\bar{X}_n = \frac{X_1+\dots+X_n}{n}$. Entonces
$E[\bar{X}_n] = \frac{1}{n}(n\mu) = \mu$ y $\mathrm{Var}(\bar{X}_n) = \frac{1}{n^2}(n\sigma^2) = \frac{\sigma^2}{n}$, o sea desvío $= \sigma/\sqrt{n}$ (**el desvío muestral**). Aplicando Chebyshev con $\epsilon = k\sigma/\sqrt{n}$ queda $P(|\bar{X}_n - \mu| \ge \epsilon) \le \frac{\sigma^2}{\epsilon^2 n}$, que tiende a 0 cuando $n \to \infty$.

> **Esto es la base estadística de toda la simulación**: promediar muchas réplicas hace que el promedio muestral se acerque a la media verdadera, y el **desvío del promedio cae con $\sqrt{n}$**. Por eso duplicar la precisión exige cuadruplicar las réplicas.

#### Ley Fuerte de los Grandes Números

A largo plazo, el promedio de una sucesión IID **converge** a su media:

$$\lim_{n\to\infty} \frac{X_1 + \dots + X_n}{n} = \mu$$

### 6.8 Variables aleatorias discretas

| Distribución | Cuándo | Función de masa | $E[X]$ | $\mathrm{Var}(X)$ |
|---|---|---|---|---|
| **Bernoulli** $Be(p)$ | Un ensayo con éxito/fracaso | $P(X=1)=p$, $P(X=0)=1-p$ | $p$ | $p(1-p)$ |
| **Binomial** $Bi(n,p)$ | Nº de **éxitos** en $n$ ensayos independientes con probabilidad $p$ | $P(X=i)=\binom{n}{i}p^i(1-p)^{n-i}$ | $np$ | $np(1-p)$ |
| **Poisson** $\mathcal{P}(\lambda)$ | Nº de eventos en un intervalo; aproxima a la binomial con $n$ grande y $p$ chica | $P(X=i)=e^{-\lambda}\dfrac{\lambda^i}{i!}$ | $\lambda$ | $\lambda$ |
| **Geométrica** $G(p)$ | Nº del **primer** ensayo que resulta éxito | $P(X=n)=p(1-p)^{n-1}$ | $1/p$ | $(1-p)/p^2$ |
| **Binomial negativa** (Pascal) | Nº de ensayos necesarios para obtener $r$ éxitos | $P(X=n)=\binom{n-1}{r-1}p^r(1-p)^{n-r}$, $n \ge r$ | $r/p$ | $r(1-p)/p^2$ |
| **Hipergeométrica** | Muestra de tamaño $n$ **sin reemplazo** de una urna con $N$ claras y $M$ oscuras; $X$ = claras elegidas | $P(X=i)=\dfrac{\binom{N}{i}\binom{M}{n-i}}{\binom{N+M}{n}}$ | $np$ con $p=\frac{N}{N+M}$ | $np(1-p)\frac{N+M-n}{N+M-1}$ |

**Relaciones que se toman:**

- Una **Bernoulli** es una binomial con $n = 1$: $Be(p) = Bi(1,p)$.
- Una **binomial** es la suma de $n$ Bernoulli IID: $X = \sum_{i=1}^n X_i$, de donde salen $E[X] = np$ y $\mathrm{Var}(X) = np(1-p)$ por linealidad y por independencia.
- **Binomial → Poisson**: si $n$ es grande, $p$ es chica y $\lambda = np$, entonces $Bi(n,p) \approx \mathcal{P}(\lambda)$. La derivación usa tres límites cuando $n \to \infty$:
  $$\frac{n(n-1)\cdots(n-i+1)}{n^i} \approx 1, \qquad \left(1-\frac{\lambda}{n}\right)^n \approx e^{-\lambda}, \qquad \left(1-\frac{\lambda}{n}\right)^i \approx 1$$
  De ahí sale $E[X] = np = \lambda$ y $\mathrm{Var}(X) = np(1-p) \approx \lambda$ para $p$ chica, es decir **$E[X] = \mathrm{Var}(X) = \lambda$**, la propiedad característica de la Poisson.
- **Diferencia binomial vs. hipergeométrica**: la binomial es **con** reemplazo (o población infinita), la hipergeométrica **sin** reemplazo.

### 6.9 Variables aleatorias continuas

#### Uniforme en $(a,b)$

$$f(x) = \frac{1}{b-a} \ \text{ para } a<x<b, \quad 0 \text{ fuera} \qquad F(x) = \frac{x-a}{b-a}$$

$$E[X] = \frac{a+b}{2} \qquad \mathrm{Var}(X) = \frac{(b-a)^2}{12}$$

> *Derivación de la varianza*: $E[X^2] = \frac{1}{b-a}\int_a^b x^2 dx = \frac{b^2+ab+a^2}{3}$, y restando $\left(\frac{a+b}{2}\right)^2$ queda $\frac{(b-a)^2}{12}$.
>
> **Inversas útiles**: $a = E[X] - \sqrt{3\,V(X)}$ y $b = 2E[X] - a$.

#### Normal $N(\mu, \sigma^2)$

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\,e^{-(x-\mu)^2/2\sigma^2}, \quad -\infty<x<\infty$$

$$E[X] = \mu \qquad \mathrm{Var}(X) = \sigma^2$$

Curva **de campana, simétrica alrededor de $\mu$**. Si $X \sim N(\mu,\sigma^2)$, entonces $aX+b \sim N(a\mu+b,\ a^2\sigma^2)$.

**Estandarización**: $Z = \dfrac{X-\mu}{\sigma}$ tiene $E[Z]=0$ y $\mathrm{Var}(Z)=1$ (se prueba con las dos propiedades de arriba). Su función de distribución es

$$\phi(x) = P(Z \le x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{x} e^{-t^2/2}\,dt$$

y entonces $F(x) = P(X \le x) = \phi\!\left(\dfrac{x-\mu}{\sigma}\right)$.

> **La acumulada de la normal no existe en forma explícita** — por eso no se puede aplicar transformada inversa directamente (ver Unidad 7).

#### Exponencial $\mathrm{Exp}(\lambda)$

$$f(x) = \lambda e^{-\lambda x}, \quad 0<x<\infty \qquad F(x) = \int_0^x \lambda e^{-\lambda t}dt = 1 - e^{-\lambda x}$$

$$E[X] = \frac{1}{\lambda} \qquad \mathrm{Var}(X) = \frac{1}{\lambda^2} = (E[X])^2$$

> **Para qué se usa en un modelo de colas** (pregunta textual del parcial 2021-10 P13): en un M/M/1
> **tanto los tiempos entre arribos como los tiempos de servicio siguen una distribución exponencial**.
> El parámetro $\lambda$ es la tasa: $\lambda = 1/E[X]$ arribos por unidad de tiempo.
>
> Relación con Poisson: si los **tiempos entre eventos** son exponenciales con parámetro $\lambda$,
> entonces el **número de eventos** en un intervalo es Poisson con parámetro $\lambda t$. Son las dos
> caras del mismo proceso.

#### Gamma / Erlang

Si un proceso consiste en $k$ eventos sucesivos y el tiempo total es la suma de $k$ exponenciales independientes con el mismo $\alpha$, la suma tiene distribución **gamma** con parámetros $\alpha$ y $k$:

$$f(x) = \frac{\alpha^k x^{k-1} e^{-\alpha x}}{(k-1)!}, \quad \alpha>0,\ k>0,\ x \ge 0$$

$$E[X] = \frac{k}{\alpha} \qquad \mathrm{Var}(X) = \frac{k}{\alpha^2}$$

> **No existe forma explícita para la acumulada.** A medida que $k$ crece, la gamma tiende asintóticamente a la normal. Inversas: $\alpha = E[X]/V(X)$ y $k = (E[X])^2/V(X)$.
>
> En notación de Kendall, la $k$-Erlang se abrevia $E_k$.

#### Teorema Central del Límite

Sea $X_1, X_2, \dots$ una sucesión IID con media finita $\mu$ y varianza finita $\sigma^2$. Entonces:

$$\lim_{n\to\infty} P\left(\frac{X_1 + \dots + X_n - n\mu}{\sigma\sqrt{n}} < x\right) = \phi(x)$$

> **Por qué importa acá**: (a) justifica usar la distribución **t de Student** / normal para construir los
> intervalos de confianza sobre las medias de las réplicas (Unidad 9); (b) da un método directo para
> **generar valores normales** sumando uniformes (Unidad 7).

### 6.10 Proceso de Poisson

> ⚠️ **Esta es la pregunta 8 del parcial en 2022, 2023 y 2024 — tres años seguidos, casi textual.**
> "Enuncie y describa las condiciones que hacen que la ocurrencia de ciertos eventos constituya un
> proceso de Poisson. ¿Qué caracteriza a un proceso de Poisson no homogéneo?"

Sea $N(t)$ el número de eventos que ocurren en el intervalo $[0,t]$. Estos eventos constituyen un **proceso de Poisson con razón $\lambda > 0$** si:

| # | Condición | Nombre |
|---|---|---|
| a | $N(0) = 0$ | **Condición inicial** — comienza en el instante 0 |
| b | El número de eventos en intervalos de tiempo **disjuntos** son independientes | **Incrementos independientes** |
| c | La distribución del número de eventos en un intervalo dado depende **solo de su longitud**, no de su posición en el tiempo | **Incrementos estacionarios** |
| d | $\displaystyle\lim_{h\to 0}\frac{P(N(h)=1)}{h} = \lambda$ | En un intervalo pequeño de longitud $h$, la probabilidad de que ocurra **exactamente un** evento es aproximadamente $\lambda h$ |
| e | $\displaystyle\lim_{h\to 0}\frac{P(N(h)\ge 2)}{h} = 0$ | En un intervalo pequeño, la probabilidad de que ocurran **dos o más** eventos es aproximadamente 0 |

### Proceso de Poisson **no homogéneo**

El homogéneo asume que los eventos ocurren con la misma probabilidad en cualquier intervalo de igual longitud. Eso no siempre es realista (pensá en los arribos a un banco: no es lo mismo las 10 de la mañana que las 3 de la tarde). El **no homogéneo** permite que la tasa varíe en el tiempo: tiene una **función de intensidad $\lambda(t)$**, y cumple:

| # | Condición |
|---|---|
| a | $N(0) = 0$ (igual) |
| b | Incrementos independientes (igual) |
| c | $\displaystyle\lim_{h\to 0} \frac{P\{\text{exactamente 1 evento entre } t \text{ y } t+h\}}{h} = \lambda(t)$ |
| d | $\displaystyle\lim_{h\to 0} \frac{P\{\text{2 o más eventos entre } t \text{ y } t+h\}}{h} = 0$ |

> **La respuesta corta a "¿qué los diferencia?"** (así se toma en 2021-10 P12): el homogéneo cumple la
> **hipótesis de incremento estacionario** — la distribución del número de eventos en un intervalo
> depende solo de su longitud y no de su posición. El no homogéneo **no la cumple**: su tasa
> $\lambda(t)$ varía con el tiempo. Esa es **la única condición que se pierde**.

### Fuentes

- `fuentes/Resumen Simulación.pdf` — Ross cap. 2 completo (2.1 a 2.9)
- `fuentes/resumenes/Resumen 5.pdf` — Naylor cap. 4, distribuciones (gamma, hipergeométrica)
- `fuentes/examenes/parciales/2022/2022-09-24.jpg`, `2023/2023-09-16.jpg`, `2024/2024-10-19.jpg`

---

## Unidad 7 — Generación de números y variables aleatorias

> ⚠️ **Este es el bloque que NO está en el resumen que vas a usar, y es el que más se toma.**
> En los parciales 2022 y 2023 son las preguntas **9 y 10**; en 2021-10 son las **2, 3 y 8**; en
> 2021-12 son las **1, 8 y 10**; en el globalizador 2023 son las **3 y 4**; en 2019-Leale es toda la
> parte práctica; y en los finales 2016 y 2019 es el ejercicio de la distribución triangular.

Hay que distinguir dos cosas que se confunden:

1. **Generar números aleatorios** $u_i \sim U(0,1)$ — la materia prima.
2. **Generar variables aleatorias** con una distribución cualquiera **a partir de** esos $u_i$.

### 7.1 Números aleatorios: verdaderos vs. pseudoaleatorios

**Verdaderos**: se basan en una fuente de aleatoriedad física, teóricamente impredecible (cuántica) o prácticamente impredecible (caótica). Ejemplos: random.org (ruido atmosférico), ERNIE (ruido térmico en transistores, lotería de bonos del Reino Unido), la tabla de un millón de números de RAND Corporation (1955, ruleta electrónica).

> **Desventaja**: son costosos, lentos y **no reproducibles**.

**Pseudoaleatorios**: se generan secuencialmente con un algoritmo **determinístico**. Se definen por tres funciones:

- **Función de inicialización**: recibe la **semilla** y pone al generador en su estado inicial.
- **Función de transición**: transforma el estado del generador.
- **Función de salida**: transforma el estado para producir el número.

> Consecuencia: **una sucesión de números pseudoaleatorios está completamente determinada por la semilla**. Eso es una desventaja teórica pero una ventaja práctica enorme: permite **reproducir** una corrida y comparar escenarios bajo las mismas condiciones (ver *números aleatorios comunes*, Unidad 10).

### 7.2 Propiedades de un buen generador

Pregunta frecuente #8. Un buen generador produce sucesiones que son:

1. **Uniformemente distribuidas** en $(0,1)$.
2. **Estadísticamente independientes** (no correlacionadas).
3. **Reproducibles** — necesario para comparar dos o más alternativas bajo la misma situación de eventos generados.
4. **Sin repetición** dentro de una longitud determinada de la sucesión (**período largo**).
5. Generadas **a gran velocidad** (computacionalmente eficientes).
6. Con **mínimo requerimiento de almacenamiento**.

Dicho como en el parcial (2021-10 P3): las constantes $a$ y $m$ deben satisfacer tres criterios:

1. Para cualquier semilla inicial, la sucesión resultante **tiene la "apariencia"** de ser una sucesión de variables aleatorias independientes y uniformes en $(0,1)$.
2. Para cualquier semilla inicial, **el número de variables que se pueden generar antes de que comience la repetición es grande**.
3. Los valores **se pueden calcular de manera eficiente** en una computadora digital.

### 7.3 Método de los cuadrados centrales (middle square)

Von Neumann, 1946. Para 4 dígitos:

1. Se parte de una semilla de 4 dígitos: `seed = 9731`
2. Se la eleva al cuadrado, produciendo un número de 8 dígitos (**completando con ceros a la izquierda** si tiene menos): `9731² = 94692361`
3. Los **4 dígitos del centro** son el siguiente número de la secuencia: `seed = 6923`
4. Se calcula $U_i = Z_i / 10000$ e itera.

**Por qué no sirve**: cae rápidamente en ciclos cortos. Si aparece un cero, **se propaga para siempre**. Ejemplo con semilla 1931: `7287 → 1003 → 60 → 36 → 12 → 1 → 0 → 0 → 0 …`. Y con semilla 9731, después de ~44 iteraciones entra en el ciclo `6100 → 2100 → 4100 → 8100 → 6100 …` de período 4.

> **Conclusión que se pide**: no cumple **uniformidad** en $(0,1)$ (tiende a números cada vez más chicos y no vuelve a valores cercanos a 1) ni **independencia** (todo $U_i$ está determinado por $U_{i-1}$). No es aplicable en simulación.
>
> Nota histórica: Metropolis logró 750.000 números distintos con semillas de 38 bits en binario, pero el método sigue sin considerarse bueno.

### 7.4 Generadores congruenciales lineales (GCL)

> **Este es el que se toma.** Aparece en 2021-10 P3, 2021-12 P1, 2022 P9, 2023 P9, globalizador 2023 P3, final 2021 P1, y como ejercicio práctico en 2019-Leale.

Son métodos **determinísticos**: los procesos aritméticos determinan unívocamente cada término. Aunque no son aleatorios, las sucesiones resultantes **superan las pruebas estadísticas**, lo que permite tratarlas como si lo fueran.

#### GCL mixto ($c > 0$)

$$Z_i = (a \cdot Z_{i-1} + c) \bmod m \qquad\qquad U_i = \frac{Z_i}{m}$$

Donde:
- $a$ = **multiplicador**, entero > 0
- $c$ = **incremento**, entero > 0
- $m$ = **módulo**
- $Z_0$ = **semilla**, a partir de la cual se puede regenerar la secuencia
- Además debe ser $m > 0$, $m > a$, $m > c$, $m > Z_0$

**Forma cerrada** (permite saltar directo al $i$-ésimo):

$$Z_i = \left(a^i Z_0 + \frac{c(a^i - 1)}{a-1}\right) \bmod m$$

#### GCL multiplicativo ($c = 0$)

$$Z_i = (a \cdot Z_{i-1}) \bmod m$$

Es el caso especial con $c = 0$. Debe cumplir $m>0$, $m>a$, $m>Z_0$.

#### GCL aditivo

$$Z_{i+1} = (Z_i + Z_{i-k}) \bmod m$$

Presupone $k$ valores iniciales. Con $k=1$ genera la sucesión de Fibonacci. **Es el único método que produce períodos mayores que $m$.**

#### Período completo

El período $p$ es el mínimo $h > 0$ tal que $Z_h = Z_0$. Como $Z_i \le m$ para todo $i$, **es imposible obtener sucesiones que no se repitan** con métodos congruenciales — el máximo alcanzable es $p = m$, y en ese caso el generador es de **período completo**.

**Teorema (GCL mixto)** — un GCL mixto es de período completo si y solo si:

1. El único entero que divide a **$m$ y a $c$ simultáneamente es 1** (son primos entre sí / primos relativos).
2. Si $q$ es un número **primo** que divide a $m$, entonces $q$ divide a $a - 1$.
3. Si **4 divide a $m$**, entonces 4 divide a $a - 1$.

**Ejemplo trabajado** (ejercicio del parcial 2019-Leale, con $Z_0=7$, $a=5$, $c=3$, $m=16$):

| Criterio | Con $a=5$, $c=3$, $m=16$ | Con $a=6$, $c=4$, $m=16$ |
|---|---|---|
| $m$ y $c$ primos entre sí | ✅ Solo el 1 divide a 16 y a 3 | ❌ 2 y 4 dividen a 16 y a 4 |
| $q$ primo divide a $m$ ⟹ $q$ divide a $a-1$ | ✅ 2 divide a 16 y a 4 ($=5-1$) | ❌ 2 divide a 16 pero no a 5 ($=6-1$) |
| 4 divide a $m$ ⟹ 4 divide a $a-1$ | ✅ 4 divide a 16 y a 4 ($=5-1$) | ❌ 4 divide a 16 pero no a 5 ($=6-1$) |
| **Resultado** | **Período completo** ($p = 16$) | **No es de período completo** |

> Para el **multiplicativo** no se puede aplicar este teorema, pero sí se pueden encontrar valores de $a$, $m$ y $Z_0$ que den $p = m$.

#### Generadores recomendados en la práctica

| Tipo | Fórmula | Autor |
|---|---|---|
| Mixto | $Z_i = (5^{15}Z_{i-1} + c) \bmod 2^{35}$ | Coveyou |
| Mixto | $Z_i = (314{,}159{,}269 \cdot Z_{i-1}) \bmod 2^{31}$ | Kobayashi |
| **Multiplicativo** | $Z_i = (7^5 \cdot Z_{i-1}) \bmod (2^{31}-1)$ | El de `rand` de Matlab antes de 1995 |

> **La respuesta a "condiciones deseables para $a$ y $m$"** que se espera en el parcial: que $m$ sea un
> **número primo grande, de tamaño aproximado al de la palabra del sistema**. Para una palabra de 32
> bits: $m = 2^{31} - 1$ y $a = 7^5 = 16807$.
>
> ⚠️ En el parcial 2021-12-02 resuelto figura "$a = 7^5 = 1608$" — **es un error de tipeo**, el valor
> correcto es **16807**.

### 7.5 Tests de aleatoriedad

Pregunta frecuente #2: *"¿Cómo me doy cuenta de que la generación de números aleatorios no me sirve?"*

Se dividen en:

- **Teóricos**: trabajan con la **expresión** del generador para evaluar si los números que produciría serían uniformes e independientes.
- **Empíricos**: trabajan con los **números obtenidos** del generador para verificar esas propiedades.

| Test | Qué chequea | Cómo |
|---|---|---|
| **Chi-cuadrado** (frecuencia) | **Uniformidad** (asume independencia) | Dividir $(0,1)$ en $k$ subintervalos de igual longitud, generar $n$ números, contar cuántos $f_j$ cayeron en cada uno, calcular $\chi^2 = \frac{k}{n}\sum_{j=1}^{k}\left(f_j - \frac{n}{k}\right)^2$ y comparar con $\chi^2_{k-1,\,1-\alpha}$. Si $\chi^2$ **supera** el valor de tabla → se **rechaza** $H_0$ (los números **no** son uniformes). Se pide $n/k \ge 5$ |
| **Series** | Uniformidad, con más precisión | Generalización del chi-cuadrado a $d$ dimensiones: se arman $d$-tuplas no superpuestas y se cuenta en qué celda del hipercubo $[0,1]^d$ cae cada una. $\chi^2$ con $k^d - 1$ grados de libertad. Requiere $n/k^d \ge 5$ |
| **Corridas** (runs) | **Independencia** | Identificar las subsecuencias crecientes contiguas de longitud máxima. Contar $r_i$ = cantidad de corridas de longitud $i$ (con $i=1..5$, y $r_6$ = corridas de longitud $\ge 6$). Calcular $R = \frac{1}{n}\sum_{i=1}^{6}\sum_{j=1}^{6} a_{ij}(r_i - n b_i)(r_j - n b_j)$ con $a_{ij}$ y $b_i$ de tabla, y comparar con $\chi^2_{6,\,1-\alpha}$. Si supera → se rechaza $H_0$ (los números **no** son independientes). Se pide $n \ge 4000$ |
| **Producto rezagado** | Independencia | Con rezago $k$: $C_k = \frac{1}{N-k}\sum_{i=1}^{N-k} r_i r_{i+k}$. Si no hay correlación, los $C_k$ se distribuyen normalmente con media 0,25 y desvío $\sqrt{(13N-19k)}/(12(N-k))$ |
| **Distancia** | Uniformidad de dígitos | Para un dígito $d$, mide la longitud de las distancias entre apariciones de $d$. Para una sucesión verdaderamente aleatoria, $P(k) = (0{,}9)^k(0{,}1)$. Se compara con chi-cuadrado |
| **Máximos** | Uniformidad | $\max(r_1,\dots,r_N)$ tiene una distribución conocida por estadísticas de orden; $R^N$ debe estar uniformemente distribuida en $(0,1)$. Es una prueba de frecuencias sobre eso |
| **Poker** | Uniformidad de combinaciones | Prueba de frecuencia especial para combinaciones de 5 o más dígitos: pares, dos pares, tercias, fulles, etc. contra sus frecuencias esperadas |

> **La respuesta corta de la pregunta frecuente #2**: hay tests para evaluarlos — **Chi-cuadrado**
> (uniformidad) y **prueba de corridas** (independencia).

### 7.6 Generación de variables aleatorias: los tres métodos

Naylor identifica tres métodos para generar valores de variables aleatorias a partir de números uniformes.

#### A. Método de la transformada inversa

> ⚠️ **La pregunta 10 del parcial en 2022 y 2023, palabra por palabra**: "Enuncie y demuestre el
> algoritmo de la transformada inversa para la generación de variables aleatorias continuas. Luego elija
> una variable aleatoria continua, y aplique dicho algoritmo para generarla."

**Enunciado (proposición)**: Sea $U$ una variable aleatoria uniforme en $(0,1)$. Para cualquier función de distribución continua e invertible $F$, la variable aleatoria $X$ definida como

$$X = F^{-1}(U)$$

tiene distribución $F$. ($F^{-1}$ se define como el valor de $x$ tal que $F(x) = u$.)

**Demostración**: Sea $F_X$ la función de distribución de $X = F^{-1}(U)$. Entonces

$$\begin{aligned}
F_X(x) &= P\left(F^{-1}(U) \le x\right) \\
&= P\left(F(F^{-1}(U)) \le F(x)\right) &&\text{(aplicando } F \text{, que es creciente)}\\
&= P\left(U \le F(x)\right) &&\text{pues } F(F^{-1}(U)) = U \\
&= F(x) &&\text{pues } U \text{ es uniforme en } (0,1)
\end{aligned}$$

> El último paso es la clave: si $U \sim U(0,1)$, entonces $P(U \le a) = a$ para $a \in (0,1)$.

**Algoritmo**: para generar $X$ a partir de la distribución continua $F$ → generar un número aleatorio $U$ y hacer $X = F^{-1}(U)$.

**Aplicación 1 — uniforme en $(a,b)$**:
$$F(x) = \frac{x-a}{b-a} = r \implies \boxed{x = a + (b-a)\,r}$$

**Aplicación 2 — exponencial**:
$$F(x) = 1 - e^{-\lambda x} = r \implies e^{-\lambda x} = 1-r \implies x = -\frac{1}{\lambda}\ln(1-r)$$

Y como $r$ y $1-r$ tienen la misma distribución $U(0,1)$ (intercambiabilidad de $F(x)$ y $1-F(x)$), se usa la forma simplificada:

$$\boxed{x = -\frac{1}{\lambda}\ln r = -E[X]\ln r}$$

> Los valores de $x$ resultan siempre no negativos, como corresponde a la exponencial.

**Aplicación 3 — geométrica** (discreta, pero se hace igual): con $1 - F(x) = q^{x+1}$ y notando que el rango de $(1-F(x))/q$ es unitario, resulta $r = q^x$, de donde

$$x = \frac{\log r}{\log q}, \quad \text{redondeando siempre al entero menor}$$

#### A'. Transformada inversa **discreta**

> Pregunta textual de 2021-10 P8, 2021-12 P8, globalizador 2023 P4 y final 2021 P4.

Para una variable discreta se genera $U$ y se determina el valor de $X$ **hallando el intervalo $(F(x_{j-1}), F(x_j))$ en el que cae $U$** — equivalentemente, hallando la inversa de $F$ en $U$.

**Ejemplo trabajado** (el que se toma literal): $P(X=1)=1/6$, $P(X=2)=1/3$, $P(X=3)=1/3$, $P(X=4)=1/6$.

Se acumula: $F(1)=1/6$, $F(2)=1/6+1/3=1/2$, $F(3)=1/2+1/3=5/6$, $F(4)=1$.

```
Generar U ~ U(0,1)
Si U < 1/6   → X = 1 y terminar
Si U < 1/2   → X = 2 y terminar
Si U < 5/6   → X = 3 y terminar
En caso contrario → X = 4
```

#### B. Método de rechazo (aceptación-rechazo)

Se usa cuando $f(x)$ es **acotada** y $x$ tiene **rango finito** $a \le x \le b$ (típicamente porque no se puede invertir $F$).

**Etapas**:

1. **Normalizar el rango de $f$**: encontrar $c$ tal que $c \cdot f(x) \le 1$ para $a \le x \le b$.
2. **Definir $x$ como función lineal de $r$**: $x = a + (b-a)\,r$.
3. **Generar parejas** de números aleatorios $(r_1, r_2)$.
4. **Aceptar o rechazar**: si la pareja satisface
   $$r_2 \le c \cdot f\left[a + (b-a)\,r_1\right]$$
   se **acepta** y se usa $x = a + (b-a)\,r_1$ como el valor generado. Si no, se descarta la pareja y se generan dos números nuevos.

> **Intuición geométrica**: se tiran puntos al azar dentro del rectángulo $[a,b]\times[0,1/c]$ y se
> aceptan los que caen **debajo de la curva** $f(x)$. La proporción de aceptados en cada franja
> vertical es proporcional a $f(x)$, que es exactamente lo que se busca.

#### C. Método de composición

Se expresa $f(x)$ como una **mezcla probabilística** de funciones de densidad más simples $g_n(x)$:

$$f(x) = \sum_n g_n(x)\,p_n$$

Se elige primero cuál $g_n$ usar (con probabilidad $p_n$) y después se genera de esa $g_n$. La guía para elegir las $g_n$ es la bondad del ajuste y minimizar $\sum T_n p_n$, donde $T_n$ es el tiempo esperado de cómputo para generar de $g_n$.

### 7.7 Generación por distribución (tabla de recetas)

| Distribución | Método | Fórmula / procedimiento |
|---|---|---|
| **Uniforme** $(a,b)$ | Transformada inversa | $x = a + (b-a)r$ |
| **Exponencial** | Transformada inversa | $x = -\frac{1}{\alpha}\ln r = -E[X]\ln r$ |
| **Gamma / Erlang** $(\alpha, k)$ | Reproducir el proceso: sumar $k$ exponenciales | $x = \sum_{i=1}^{k} x_i = -\frac{1}{\alpha}\sum_{i=1}^{k}\ln r_i = -\frac{1}{\alpha}\ln\left(\prod_{i=1}^{k} r_i\right)$ |
| **Normal** $(\mu,\sigma)$ | **TCL** (no hay inversa explícita) | Sumar $K$ uniformes y estandarizar: $x = \sigma\sqrt{\frac{12}{K}}\left(\sum_{i=1}^{K} r_i - \frac{K}{2}\right) + \mu$ |
| **Geométrica** | Transformada inversa | $x = \dfrac{\log r}{\log q}$, redondeado al entero menor |
| **Binomial** $(n,p)$ | Rechazo / ensayos de Bernoulli | Fijar $x_0 = 0$. Para cada $r_i$ ($1\le i\le n$): $x_i = x_{i-1}+1$ si $r_i \le p$, si no $x_i = x_{i-1}$. El resultado es $x_n$ |
| **Hipergeométrica** | Bernoulli con $N$ y $p$ variables | Igual que la binomial pero actualizando en cada extracción: $N_i = N_{i-1}-1$ y $p_i = \dfrac{N_{i-1}p_{i-1} - S}{N_{i-1}-1}$, donde $S=1$ si el elemento $i-1$ era de la clase I y 0 si no |
| **Poisson** $(\lambda)$ | Acumular exponenciales | Determinar $x$ con $\displaystyle\sum_{i=0}^{x} t_i \le \lambda < \sum_{i=0}^{x+1} t_i$, con $t_i = -\ln r_i$. Equivalente: $\displaystyle\prod_{i=0}^{x} r_i \ge e^{-\lambda} > \prod_{i=0}^{x+1} r_i$ |

**Por qué la normal se genera con el TCL**: la acumulada de la normal **no existe en forma explícita**, así que no se puede invertir. Se usa la interpretación del TCL: si $r_1,\dots,r_K$ son uniformes en $(0,1)$, cada una tiene $\theta = E[r_i] = \frac{0+1}{2} = \frac{1}{2}$ y $\sigma = \frac{b-a}{\sqrt{12}} = \frac{1}{\sqrt{12}}$. Entonces

$$z = \frac{\sum_{i=1}^{K} r_i - K/2}{\sqrt{K/12}}$$

es aproximadamente normal estándar, y despejando $x$ de $z = (x-\mu_x)/\sigma_x$ queda la fórmula de la tabla.

**Alternativa exacta — el "procedimiento directo" (Box-Muller)**: Naylor da un segundo método que, a
diferencia del anterior, **no es una aproximación**. Con dos uniformes independientes $r_1$ y $r_2$ en
$(0,1)$ se obtienen **dos** valores normales estándar de una sola vez:

$$x_1 = \sqrt{-2\ln r_1}\ \cos(2\pi r_2) \qquad\qquad x_2 = \sqrt{-2\ln r_1}\ \operatorname{sen}(2\pi r_2)$$

> Su velocidad es comparable a la del método del límite central, y **da resultados exactos**. Si te
> piden generar normales y querés lucirte, mencioná los dos: el del TCL (aproximado, simple) y este
> (exacto).

**Distribuciones derivadas de la normal** (por si aparecen en el análisis de salidas):

| Distribución | Definición | $E[X]$ | $\mathrm{Var}(X)$ |
|---|---|---|---|
| **Ji cuadrada** $\chi^2_m$ | $\sum_{i=1}^{m} z_i^2$ con $z_i$ normales estándar; es una gamma con $k=m/2$ y $\alpha=1/2$ | $m$ | $2m$ |
| **t de Student** | $t = \dfrac{z}{\sqrt{\chi^2_m/m}}$ | 0 | $\dfrac{m}{m-2}$ |
| **F** | $F_{m,n} = \dfrac{\chi^2_m/m}{\chi^2_n/n}$ | $\dfrac{n}{n-2}$, $n>2$ | $\dfrac{2n^2(m+n-2)}{m(n-2)^2(n-4)}$, $n>4$ |

> La **t** es la que se usa para los intervalos de confianza de la Unidad 9, y la **Ji cuadrada** es la
> de los tests de aleatoriedad de la §7.5. Para $m > 30$ ambas se aproximan bien con la normal.

### Ejercicio resuelto tipo — generador para una distribución triangular

> Este ejercicio salió en el final 2016-07-05 (P1) y en el final 2019-07-02 (P4). Es el caso testigo
> de "te dan una densidad rara y tenés que armar el generador".

**Consigna (final 2019)**: $f(t) = 0$ si $t<0$ o $t>1$; $f(t) = f_0(1-t)$ si $0\le t\le 1$.
a) Encontrar $f_0$. b) Armar un generador de números aleatorios con esa función.

**a) Encontrar $f_0$** — toda densidad debe integrar 1:

$$\int_0^1 f_0(1-t)\,dt = f_0\left[t - \frac{t^2}{2}\right]_0^1 = f_0\left(1 - \frac{1}{2}\right) = \frac{f_0}{2} = 1 \implies \boxed{f_0 = 2}$$

Queda $f(t) = 2(1-t)$ en $[0,1]$, que es exactamente la densidad del final 2016.

**b) Generador por transformada inversa** — primero la acumulada:

$$F(x) = \int_0^x 2(1-t)\,dt = 2\left[t - \frac{t^2}{2}\right]_0^x = 2x - x^2$$

Se iguala a $r$ y se despeja:

$$2x - x^2 = r \implies x^2 - 2x + r = 0 \implies x = \frac{2 \pm \sqrt{4-4r}}{2} = 1 \pm \sqrt{1-r}$$

Como $x$ debe estar en $[0,1]$, se descarta la raíz con $+$:

$$\boxed{x = 1 - \sqrt{1-r}}$$

Y como $r$ y $1-r$ son ambas $U(0,1)$, se puede simplificar a $x = 1 - \sqrt{r}$.

**Verificación de coherencia**: $f(t)=2(1-t)$ es decreciente, así que debería producir más valores cerca de 0 que de 1. Con $r=0{,}5$ da $x = 1-\sqrt{0{,}5} = 0{,}293$ — efectivamente por debajo de la mediana geométrica, consistente.

> **Método alternativo** si la inversa no sale: usar el **método de rechazo**. Acá $f$ es acotada
> ($\max f = f(0) = 2$) y de rango finito $[0,1]$, así que con $c = 1/2$ queda $c\,f(x) \le 1$ y se
> aplica el procedimiento de la sección 7.6.B.

### Ejercicio resuelto tipo — pseudocódigo del generador uniforme

> Consigna del parcial 2019-Leale, ejercicio 1: dados 10 números uniformes y $f(x) = \frac{1}{b-a}$ en
> $[a,b]$, obtener (a) la acumulada, (b) la inversa, (c) un pseudocódigo con sus parámetros de entrada,
> (d) generar 10 valores.

a) **Acumulada**: $F(x) = \dfrac{x-a}{b-a}$ para $a \le x \le b$.

b) **Inversa**: de $r = \frac{x-a}{b-a}$ sale $x = a + (b-a)\,r$.

c) **Pseudocódigo**:

```
FUNCIÓN generar_uniforme(a, b, n)
    // Parámetros de entrada:
    //   a : límite inferior del intervalo
    //   b : límite superior del intervalo
    //   n : cantidad de valores a generar
    Para i = 1 hasta n
        r  = generar_aleatorio_U01()      // número uniforme en (0,1)
        x[i] = a + (b - a) * r            // transformada inversa
    Fin Para
    Retornar x
Fin FUNCIÓN
```

d) Con los números de la tabla `0.485, 0.406, 0.383, 0.457, 0.712, 0.171, 0.393, 0.678, 0.976, 0.218`
se aplica $x_i = a + (b-a)\,r_i$ con los $a$ y $b$ que dé la consigna.

### Fuentes

- `fuentes/apuntes-catedra/Tecnicas de Simulación en Computadoras - Naylor Cap. 4.pdf` — **apunte oficial de cátedra**
- `fuentes/apuntes-catedra/Números pseudoaleatorios.pdf` — **apunte oficial de cátedra** (middle square, GCL, en R)
- `fuentes/apuntes-extra/Números aleatorios.pdf` (Lascano, UTN Rosario) — GCL, período completo, tests
- `fuentes/resumenes/Resumen 5.pdf` — Naylor caps. 3 y 4 resumidos
- `fuentes/examenes/` — prácticamente todos

---
## Unidad 8 — Modelos analíticos de colas

> Weitz cap. 13. Ojo con la distinción de toda la materia: acá se resuelve la cola **analíticamente**
> (fórmulas cerradas de estado estacionario), mientras que en la Unidad 3 se la **simulaba**. La
> pregunta "¿qué relación tiene el modelo M/M/1 con el modelo analítico?" es clásica del final oral.

### 8.1 Componentes de un sistema de colas

Un sistema de colas se caracteriza por **tres componentes**:

**a) Proceso de llegada** — cómo llegan los clientes.
- Si los tiempos entre arribos $A_1, A_2,\dots$ son IID, el tiempo promedio entre llegadas es $E(A)$ y la **tasa de llegada** es
  $$\lambda = \frac{1}{E(A)}$$
- **Determinístico**: los clientes llegan en intervalos fijos y conocidos.
- **Probabilístico**: los tiempos entre llegadas son inciertos, modelados con una distribución. Usualmente **exponencial**.

**b) Mecanismo de servicio** — se define especificando: el **número de servidores** $s$; si hay **una cola por servidor o una única cola** para todos; y la **distribución** de los tiempos de servicio.
- Si los $S_i$ son IID, el tiempo promedio de servicio es $E(S)$ y la **tasa de servicio de un servidor** es
  $$\omega \text{ (o } \mu) = \frac{1}{E(S)}$$
- Servidores **idénticos** (todos a la misma velocidad — lo usual en los modelos básicos) o **no idénticos**.

**c) Disciplina de la cola** — qué cliente se atiende cuando un servidor queda libre.
- **FIFO / PEPS**: primero en entrar, primero en salir.
- **LIFO**: último en entrar, primero en salir.
- **Prioridad**: según importancia o requerimientos de servicio.

**Otras características que se preguntan:**
- **Población de clientes**: **infinita** (el número de clientes potenciales es muy grande frente a la capacidad del sistema — un supermercado) o **finita** (4 máquinas en un taller; el análisis es más complejo, y la **tasa de llegada varía con el tiempo**).
- **Cantidad de colas**: una única cola o varias.
- **Número de espacios en cola**: limitado (finito) o ilimitado (infinito).
- **Prioridad / interrupción**: si un servidor puede detener la atención de un cliente para atender a otro que acaba de llegar.

### 8.2 Las dos fases de todo sistema de colas

| Fase | Qué es |
|---|---|
| **Fase transitoria** | Período inicial en el que **se conservan los efectos de las condiciones iniciales** |
| **Estado estable** (estacionario) | Condición del sistema después de que se han eliminado las condiciones iniciales |

> ⚠️ **Todos los modelos analíticos son válidos solamente en estado estable.** Este es el puente con la
> Unidad 9: si querés comparar la simulación con la fórmula analítica, tenés que dejar pasar el
> **período de calentamiento** (warm-up) primero.

### 8.3 Notación de Kendall

> Pregunta directa en los parciales 2022 (P6) y 2024 (P5).

$$A/S/c/K/L$$

| Posición | Qué describe | Símbolos |
|---|---|---|
| **A** | Distribución de los **tiempos entre llegadas** | **D** determinístico · **M** exponencial (markoviano) · **G** o **GI** general · **$E_k$** $k$-Erlang |
| **S** | Distribución de los **tiempos de servicio** | mismos símbolos |
| **c** | Número de **estaciones/servidores en paralelo** | entero |
| **K** | Número **máximo de clientes en el sistema** en cualquier momento (capacidad) | entero |
| **L** | Número total de clientes de la **población** | entero |

> **Cuando se omite alguno de los últimos símbolos, se considera infinito.** Por eso "M/M/1" significa
> tiempos entre llegadas exponenciales, servicio exponencial, 1 servidor, capacidad infinita y
> población infinita.
>
> - **M** viene de *markoviano* (o *memoryless*): la exponencial no tiene memoria.
> - **GI** = *general independent* para los arribos; **G** = *general* para el servicio.
> - Un GI/G/s genérico es cualquier sistema con $s$ servidores en paralelo, una cola FIFO, $A_i$ IID, $S_i$ IID e independientes entre sí.

### 8.4 Medidas de rendimiento

| Símbolo | Definición |
|---|---|
| $\lambda$ | Número promedio de **llegadas** por unidad de tiempo (tasa de llegada) |
| $\mu$ | Número promedio de **clientes atendidos** por unidad de tiempo en una estación (tasa de servicio) |
| $1/\mu$ | Tiempo promedio de servicio |
| $D_i$ | Tiempo que el cliente $i$ pasó **en cola** |
| $W_i = D_i + S_i$ | Tiempo de espera **en el sistema** del cliente $i$ |
| $Q(t)$ | Número de clientes **en cola** en el tiempo $t$ |
| $L(t)$ | Número de clientes **en el sistema** en $t$ = $Q(t)$ + clientes en servicio |
| $W_q$ (o $d$) | Tiempo promedio de espera **en cola** en estado estacionario |
| $W$ (o $w$) | Tiempo promedio **en el sistema** en estado estacionario |
| $L_q$ (o $Q$) | Longitud media de la cola (número promedio de clientes **en cola**) |
| $L$ | Número medio de clientes **en el sistema** |
| $P_w$ | Probabilidad de bloqueo — probabilidad de que un cliente que llega **tenga que esperar** |
| $U$ | Utilización del servidor — fracción de tiempo, en promedio, que está ocupado |
| $P_n$ | Probabilidad de que haya $n$ clientes en el sistema (distribución de estado) |
| $P_d$ | Probabilidad de **negación de servicio** — que un cliente que llega no pueda entrar porque la cola está llena |

En el límite:

$$d = \lim_{n\to\infty}\frac{\sum_{i=1}^n D_i}{n} \qquad w = \lim_{n\to\infty}\frac{\sum_{i=1}^n W_i}{n} \qquad Q = \lim_{T\to\infty}\frac{\int_0^T Q(t)dt}{T} \qquad L = \lim_{T\to\infty}\frac{\int_0^T L(t)dt}{T}$$

### 8.5 Ecuaciones de conservación (Little)

> **Las tres relaciones que se toman una y otra vez** (parcial 2021-10 P7, 2023 P4, 2024 P4, globalizador 2023 P8, final 2021 P5). Fijate que las consignas piden la relación **con palabras y con símbolos**.

$$\boxed{L = \lambda\,W} \qquad \boxed{L_q = \lambda\,W_q} \qquad \boxed{W = W_q + \frac{1}{\mu}}$$

**Cómo se enuncian en palabras** (así lo piden en el parcial):

- $L = \lambda W$: *el número promedio de clientes **en el sistema** es igual a la **tasa de llegada** multiplicada por el **tiempo promedio en el sistema**.*
- $L_q = \lambda W_q$: *el número promedio de clientes **en cola** es igual a la **tasa de llegada** multiplicada por el **tiempo promedio de espera en cola**.*
- $W = W_q + 1/\mu$: *el tiempo promedio **en el sistema** es el tiempo promedio de espera **en cola** más el tiempo promedio de **servicio**.* ($\mu$ = tasa de servicio, $1/\mu$ = tiempo promedio de servicio por cliente.)

> Notá cuál piden: en 2023 P4 y globalizador P8 piden la relación **con la tasa de servicio** ($W = W_q + 1/\mu$); en 2024 P4 piden la relación **con la tasa de llegada** y las medidas **de cola** ($L_q = \lambda W_q$); en 2023 P4 con la tasa de llegada y las medidas **del sistema** ($L = \lambda W$). Leé bien cuál te piden.

### 8.6 Factor de utilización / intensidad de tráfico

Para cualquier GI/G/s:

$$\rho = \frac{\lambda}{s\,\omega} \qquad \text{y para un solo servidor} \qquad \rho = \frac{\lambda}{\mu}$$

donde $s\omega$ es la tasa de servicio del sistema cuando **todos** los servidores están ocupados. Mide qué tan intensamente se utilizan los recursos del sistema.

> **Cuanto más cerca de 1 esté $\rho$, más cargado está el sistema** (colas largas, cuello de botella).
> $\rho$ bajo → exceso de capacidad y recursos ociosos.

### 8.7 Modelo M/M/1

> Pregunta directa en 2021-10 P9, 2021-12 P4, final 2020-08.

**Condiciones (las cuatro que hay que enunciar):**

1. **Población de clientes infinita.**
2. Proceso de llegada en el que los clientes se presentan de acuerdo con un **proceso de Poisson** con tasa promedio $\lambda$ clientes por unidad de tiempo (equivalentemente: tiempos entre arribos exponenciales).
3. Proceso de colas con **una sola línea de espera de capacidad infinita**, con disciplina **FIFO (PEPS)**.
4. Proceso de servicio de **un solo servidor** que atiende de acuerdo con una **distribución exponencial** con un promedio de $\mu$ clientes por unidad de tiempo.

**Condición de estado estable**: $\mu > \lambda$, es decir $\rho < 1$.

> **Por qué** (pregunta 2021-12 P9): si $\lambda \ge \mu$, siempre llegarían más clientes de los que se
> puede atender, la cola crecería indefinidamente y el sistema **nunca alcanzaría un estado estable**.
>
> ⚠️ **El resumen que vas a usar dice "Población de clientes finita" para M/M/1 — es un error.** Es
> **infinita**. El error viene del propio libro de Weitz: en la pág. 723 del apunte de cátedra está
> impreso "1. Una población de clientes finita", y **alguien lo corrigió a mano** intercalando un "in"
> para que diga "infinita". La versión correcta figura en todos los parciales resueltos, en el final
> 2020-08 y en el resumen mismo dos líneas más abajo cuando describe el M/M/c.

**Fórmulas de estado estacionario:**

| Medida | Fórmula |
|---|---|
| Intensidad de tráfico / utilización | $\rho = \dfrac{\lambda}{\mu}$ ,  $U = \rho$ |
| Probabilidad de sistema vacío | $P_0 = 1 - \rho$ |
| Probabilidad de que un cliente que llega tenga que esperar | $P_w = 1 - P_0 = \rho$ |
| Probabilidad de $n$ clientes en el sistema | $P_n = \rho^n P_0 = \rho^n(1-\rho)$ |
| Número promedio en la cola | $L_q = \dfrac{\rho^2}{1-\rho}$ |
| Número promedio en el sistema | $L = \dfrac{\rho}{1-\rho} = \lambda W$ |
| Tiempo promedio de espera en cola | $W_q = \dfrac{L_q}{\lambda}$ |
| Tiempo promedio en el sistema | $W = W_q + \dfrac{1}{\mu}$ |

> **Orden de cálculo recomendado**: $\rho \to P_0 \to L_q \to W_q \to W \to L$. Y verificás con $L = \lambda W$.

**Qué se quiere predecir analíticamente** (del final 2020-08 resuelto): (1) el número promedio esperado en cola / la probabilidad de varios números de clientes en cola; (2) el tiempo esperado que pasará un cliente en las instalaciones del servicio; (3) la probabilidad de que las instalaciones estén ociosas (factor de utilización).

#### Ejercicio resuelto tipo — la estación de pesado (ejemplo canónico de Weitz)

> Ejemplo 13.1 del apunte de cátedra. Es **el** ejemplo de M/M/1 de la materia — vale la pena tenerlo
> hecho porque muestra el orden de cálculo y, sobre todo, **cómo se interpreta cada número**.

**Planteo**: la Ohio Turnpike Commission (OTC) tiene una estación de pesado de camiones. Llegan
$\lambda = 60$ camiones por hora y la báscula pesa $\mu = 66$ camiones por hora.

| Paso | Medida | Cálculo | Resultado | Interpretación |
|---|---|---|---|---|
| 0 | Intensidad de tráfico | $\rho = \lambda/\mu = 60/66$ | **0,9091** | Sistema muy cargado (cerca de 1) |
| 1 | $P_0$ | $1 - \rho = 1 - 0{,}9091$ | **0,0909** | El 9% del tiempo un camión que llega **no** espera (báscula vacía) |
| 2 | $L_q$ | $\dfrac{\rho^2}{1-\rho} = \dfrac{0{,}9091^2}{0{,}0909}$ | **9,0909** | En estado estable hay ~9 camiones esperando (sin contar el que se está pesando) |
| 3 | $W_q$ | $L_q/\lambda = 9{,}0909/60$ | **0,1515 h** | ~9 minutos de espera en la fila |
| 4 | $W$ | $W_q + 1/\mu = 0{,}1515 + 1/66$ | **0,1667 h** | ~10 minutos desde que llega hasta que sale |
| 5 | $L$ | $\lambda W = 60 \times 0{,}1667$ | **10** | 10 camiones en total en la estación (en báscula + esperando) |
| 6 | $p_w$ | $1 - P_0 = \rho$ | **0,9091** | El 91% del tiempo un camión que llega tiene que esperar |
| 7 | $P_n$ | $\rho^n P_0$ | $P_0=0{,}0909$; $P_1=0{,}0826$; $P_2=0{,}0751$; $P_3=0{,}0683$ | $P(\text{no más de 3}) = 0{,}3169$ (suma de las cuatro) |
| 8 | $U$ | $\rho$ | **0,9091** | La báscula está en uso el 91% del tiempo; ociosa el 9% |

> **La conexión con denegación de servicio** (§8.9): la rampa de salida tiene capacidad para 15
> camiones. La gerencia quiere saber con qué probabilidad la cola llega hasta la autopista, o sea que
> haya **17 o más camiones en el sistema** (1 en la báscula + 16 o más esperando). Se calcula
> $\sum_{n\ge 17} P_n = 0{,}20$: el **20% del tiempo** los camiones sobrepasan la rampa. Como no es
> aceptable, ahí se plantea el M/M/2 (agregar una segunda báscula).

### 8.8 Modelo M/M/c

> Según la clase pre-examen: **entra el entendimiento general, NO las fórmulas.**

**Condiciones:**

1. **Población de clientes infinita.**
2. Los clientes llegan según un **proceso de Poisson** con tasa promedio $\lambda$.
3. Proceso de colas con **una sola línea** con disciplina **FIFO**.
4. **$c$ servidores idénticos**, cada uno atendiendo con distribución exponencial con promedio $\mu$ clientes por unidad de tiempo.

**Condición de estado estable**: $c\,\mu > \lambda$, es decir $\dfrac{\lambda}{c\,\mu} < 1$.

> **La diferencia con M/M/1 que hay que entender**: en M/M/1 la capacidad de servicio del sistema es
> $\mu$; en M/M/c es $c\mu$ cuando todos los servidores están ocupados. Por eso la condición de estado
> estable pasa de $\lambda < \mu$ a $\lambda < c\mu$. Con una **sola cola** que alimenta a los $c$
> servidores, el sistema rinde mejor que $c$ colas M/M/1 independientes con $\lambda/c$ cada una —
> porque ningún servidor queda ocioso mientras haya alguien esperando.
>
> ⚠️ **Ojo con $\rho$ en M/M/c**: en el apunte de Weitz, $\rho = \lambda/\mu$ **sin dividir por $c$**
> (por eso en el ejemplo de OTC con $c=2$ da $\rho = 1{,}75 > 1$ y el sistema igual es estable). La
> condición se escribe entonces $\rho < c$. En el resumen y en Law, en cambio, $\rho = \lambda/(c\mu)$
> y la condición es $\rho < 1$. **Son la misma cosa escrita distinto** — fijate qué convención usa el
> enunciado antes de reemplazar en las fórmulas.

**Fórmulas** (tabla 13.2 de Weitz). Según la clase pre-examen **no hay que saberlas de memoria**, pero conviene reconocerlas:

| Medida | Fórmula |
|---|---|
| $P_0$ | $\dfrac{1}{\left(\sum_{n=0}^{c-1}\dfrac{\rho^n}{n!}\right) + \dfrac{\rho^c}{c!}\cdot\dfrac{c}{c-\rho}}$ |
| $L_q$ | $\dfrac{\rho^{c+1}}{(c-1)!\,(c-\rho)^2}\,P_0$ |
| $p_w$ | $\dfrac{\rho^c}{c!}\cdot\dfrac{c}{c-\rho}\cdot P_0$ |
| $P_n$ | $\dfrac{\rho^n}{n!}P_0$ si $n \le c$ ; $\dfrac{\rho^n}{c!\,c^{\,n-c}}P_0$ si $n > c$ |
| $U$ | $1 - \left[P_0 + \frac{c-1}{c}P_1 + \frac{c-2}{c}P_2 + \dots + \frac{1}{c}P_{c-1}\right]$ |

$W_q$, $W$ y $L$ salen igual que en M/M/1, con las relaciones de Little: $W_q = L_q/\lambda$, $W = W_q + 1/\mu$, $L = \lambda W$.

### 8.9 Denegación de servicio (cola finita)

> Pregunta textual en 2021-10 P15 y final 2021 P9. **No está en el resumen.**

**Consigna**: dada una cola finita de tamaño $n$ en un sistema de una cola y un servidor, ¿cómo se calcula la probabilidad de que un cliente no pueda entrar a la cola?

Para un sistema con **cola de tamaño finito $n-1$** y **un servidor**, la capacidad máxima del sistema es $n$, contando al cliente en servicio. Por lo tanto, la probabilidad de denegación de servicio $P_d$ es la suma de las probabilidades de que haya **más de $n$** clientes en el sistema:

$$P_d = P_{n+1} + P_{n+2} + P_{n+3} + \cdots$$

O, equivalentemente y más práctico:

$$\boxed{P_d = 1 - \left(P_0 + P_1 + P_2 + \cdots + P_n\right)}$$

Con $P_i = \rho^i P_0$ del M/M/1, queda una suma geométrica finita.

### 8.10 Análisis económico de los sistemas de colas

> Pregunta en 2023 P5 ("desarrolle brevemente algún aspecto"). La clase pre-examen lo marca dos veces
> como tema que entra.

La idea es que hay un **trade-off**: más servidores cuestan plata, pero menos servidores hacen esperar
a los clientes, y esa espera también cuesta plata. El óptimo es el $c$ que minimiza el costo total.

**Datos que se necesitan:**

- $c_s$ = costo por servidor por unidad de tiempo
- $c_w$ = costo por unidad de tiempo por cliente esperando en el sistema
- $L$ = número promedio de clientes en el sistema
- $c$ = número de servidores

**Costo total en un M/M/c:**

$$\text{Costo total} = \underbrace{c_s \cdot c}_{\text{costo de servidores}} + \underbrace{c_w \cdot L}_{\text{costo de espera}}$$

**Costo total en un M/M/c/K** (con capacidad de espera limitada) — se agrega un tercer término, porque los clientes que no pueden entrar se pierden:

$$\text{Costo total} = \underbrace{c_s \cdot c}_{\text{servidores}} + \underbrace{c_w \cdot L}_{\text{espera}} + \underbrace{c_d \cdot \lambda \cdot P_d}_{\text{negación de servicio}}$$

donde $c_d$ es el costo por negación (asociado a la **pérdida de un cliente**), $\lambda$ el número de llegadas y $P_d$ la probabilidad de negación.

> **Cómo se usa**: se calcula el costo total para $c = 1, 2, 3, \dots$ y se elige el $c$ que lo minimiza.
> A medida que $c$ crece, el primer término crece linealmente y el segundo (y el tercero) decrecen —
> la curva de costo total tiene forma de U.

#### Ejercicio resuelto tipo — American Weavers (ejemplo 13.2 de Weitz)

**Planteo**: una planta textil tiene muchas máquinas tejedoras que se atascan. Las repara **uno de
siete** operarios, con disciplina FIFO. La gerente observa que hay entre 10 y 12 máquinas paradas en
cualquier momento y quiere saber **cuántos reparadores más contratar**.

**Modelado**: los "clientes" son las máquinas que se atascan. Como hay muchas, la población se supone
**infinita**. Siete servidores independientes e idénticos, una sola fila → **M/M/7** con
$\lambda = 25$ atascos/hora y $\mu = 4$ máquinas/hora por reparador (15 min de reparación promedio).

**Resultados con distinto tamaño de personal** (tabla 13.3):

| | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|
| Utilización (%) | 89,29 | 78,13 | 69,44 | 62,50 | 56,82 |
| $L_q$ (esperando) | 5,847 | 1,494 | 0,536 | 0,209 | 0,083 |
| $L$ (en el sistema) | **12,097** | 7,744 | 6,786 | 6,459 | 6,333 |
| $p_w$ | 0,702 | 0,418 | 0,236 | 0,126 | 0,063 |
| $W_q$ (horas) | 0,234 | 0,060 | 0,022 | 0,008 | 0,003 |
| $W$ (horas) | **0,484** | 0,310 | 0,272 | 0,258 | 0,253 |

> La estimación de la gerente ("10 a 12 máquinas paradas") era buena: el modelo da $L = 12{,}10$. Y
> cada máquina está parada $W = 0{,}484$ h ≈ 29 minutos.

**Análisis de costos**: se identifican dos componentes por hora —

$$\text{Costo total} = \underbrace{c_s \cdot c}_{\substack{\text{costo por hora de cada}\\ \text{reparador} \times \text{nº de reparadores}}} + \underbrace{c_w \cdot L}_{\substack{\text{costo por hora de cada máquina}\\ \text{parada} \times \text{nº promedio de máquinas paradas}}}$$

Se evalúa para $c = 7, 8, 9, 10, 11$ y se elige el mínimo. En el ejemplo del libro el óptimo son
**9 reparadores**, con un costo total de **$1.128,63 por hora**.

> **El razonamiento a reproducir en el parcial**: pasar de 7 a 8 reparadores baja $L$ de 12,10 a 7,74
> — una mejora enorme. De 9 a 10 baja de 6,79 a 6,46 — casi nada, y encima cuesta un sueldo más. La
> curva de costo total tiene forma de U y el mínimo está donde el ahorro marginal por espera se iguala
> al costo marginal del servidor.

### Fuentes

- `fuentes/Resumen Simulación.pdf` — Apéndice 1B de Law (componentes, notación, medidas, Little) y Weitz cap. 13 (13.1, 13.2, 13.5)
- `fuentes/apuntes-catedra/Apunte Weitz con hojas rotadas y acotado.pdf` — cap. 13 completo
- `fuentes/resumenes/Resumen 1.pdf` (Pagliaro) — sección 6
- `fuentes/examenes/parciales/2021/2021-10-23.pdf` — preguntas 7, 9, 15

---

## Unidad 9 — Análisis de los datos de salida

> ⚠️ **Este bloque tampoco está en el resumen.** La clase pre-examen lo marca explícito: *"Cap 9 (en
> inglés) que es de análisis de salidas sí. Pag 76 sí. Precisión absoluta/relativa."* Sale en el
> parcial 2019-Leale (ejercicio 3 completo), en el globalizador 2023 (P10) y en los finales 2016,
> 2017 y 2019.

### 9.1 El problema de fondo

**Una corrida de simulación es UNA SOLA muestra.** Por más iteraciones internas que tenga, produce un
único valor de cada medida de rendimiento — un punto, no una distribución. Para decir algo con base
estadística hacen falta **$n$ réplicas independientes**, cada una arrancando con una **semilla
distinta**.

> Frase que aparece en la clase pre-examen: *"Para saber qué tan bien funciona un escenario se necesita
> un **intervalo de confianza**, no basta con un promedio. Solo así se garantiza que una simulación
> represente a la realidad."*

### 9.2 Estado transitorio y estado estacionario

Sean $Y_1, Y_2, \dots$ los procesos estocásticos de salida, y

$$F_i(y|I) = P(Y_i \le y \mid I)$$

donde $I$ representa las **condiciones iniciales** al tiempo 0. $F_i(y|I)$ es la **distribución de
estado transitorio** del proceso al paso $i$, para esas condiciones iniciales.

Si $F_i(y|I) \to F(y)$ cuando $i \to \infty$, **para toda $y$ y para cualquier condición inicial $I$**,
entonces $F(y)$ es la **distribución de estado estacionario** del proceso.

> **Lectura práctica**: la simulación recorre un período **transiente** en el que todavía se nota de
> dónde arrancó, hasta que llega a un estado **estable** en el que la distribución de la salida ya no
> depende ni del paso ni de las condiciones iniciales.
>
> ⚠️ **Ojo con una pregunta trampa del final 2016** (P4b): *"Todos los sistemas se estabilizan cuando
> transcurre una gran cantidad de tiempo. ¿Es correcta esa afirmación?"* → **No.** Un sistema de colas
> con $\lambda \ge \mu$ nunca alcanza estado estacionario: la cola crece sin límite. La existencia de
> estado estacionario **es una propiedad del sistema, no una garantía del paso del tiempo**.
>
> ⚠️ Y otra (final 2016 P2): *"En el estado estacionario la longitud media de la cola es constante, por
> lo que las demoras individuales también son constantes. ¿Es correcto?"* → **No.** Lo que se
> estabiliza es la **distribución** de la longitud de cola (y por lo tanto su media), no cada
> realización. Las demoras individuales $D_i$ siguen siendo variables aleatorias con dispersión; lo
> que converge es $E[D_i]$, no $D_i$.

### 9.3 Simulación terminal vs. no terminal

> Pregunta explícita del parcial 2019-Leale (ejercicio 3c): *"¿Qué diferencia hay entre un estudio de
> simulación terminal y uno no terminal? Ejemplifique para cada caso."*

| | **Terminal** | **No terminal** |
|---|---|---|
| **Definición** | Existe un **evento natural $E$** que especifica la duración de cada corrida (réplica) | **No hay** un evento natural que especifique la duración |
| **El evento $E$** | Ocurre en un tiempo más allá del cual no se obtiene información útil, o en un tiempo en que el sistema es "limpiado". Se especifica **antes** de cualquier corrida, y su tiempo de ocurrencia es una **variable aleatoria** | — |
| **Condiciones iniciales** | **Afectan** las medidas de desempeño → deben ser **representativas** de las del sistema real | Se busca eliminar su efecto con un período de calentamiento |
| **Qué se estima** | El comportamiento **durante** ese período acotado | **Parámetros de estado estacionario** |
| **Ejemplos** | Un banco que abre a las 9 y cierra a las 15 (el evento $E$ es el cierre); un call center que atiende un turno; una jornada de un consultorio; el hospital del final 2017 (guardia de 22 a 7 hs) | Una fábrica que funciona 24/7; un servidor web; un sistema de manufactura continua |

En las no terminales hay varios tipos de parámetro:

- **Parámetro de estado estacionario**: es característica de la **distribución de estado estacionario** de algún proceso de salida.
- **Parámetro de ciclo de estado estacionario**: se usa cuando el proceso **no tiene** distribución de estado estacionario porque hay ciclos (ej: la carga varía por hora del día). Se divide el eje de tiempo en **ciclos** de igual duración, se define una variable $Y_c$ en el ciclo $c$, y el parámetro es característica de $Y_c$ cuando $c\to\infty$.

### 9.4 Estimación de la media — procedimiento de tamaño fijo

Se hacen $n$ **réplicas independientes** de la simulación, obteniendo $X_1, X_2, \dots, X_n$ variables aleatorias IID. Se quiere estimar $\mu = E[X]$.

**Punto estimador** (insesgado):

$$\bar{X}(n) = \frac{\sum_{i=1}^{n} X_i}{n}$$

**Varianza muestral**:

$$S^2(n) = \frac{\sum_{i=1}^{n}\left[X_i - \bar{X}(n)\right]^2}{n-1}$$

**Intervalo de confianza del $100(1-\alpha)\%$ para $\mu$**:

$$\boxed{\bar{X}(n) \ \pm\ t_{n-1,\,1-\alpha/2}\sqrt{\frac{S^2(n)}{n}}}$$

A esto se lo llama **procedimiento de tamaño fijo**. La **semi-amplitud** (mitad del intervalo) se nota:

$$\delta(n,\alpha) = t_{n-1,\,1-\alpha/2}\sqrt{\frac{S^2(n)}{n}}$$

> **Desventaja del procedimiento de tamaño fijo**: el analista **no tiene control sobre la
> semi-amplitud**. Para $n$ fijo, la semi-amplitud depende de la varianza poblacional de los $X_j$, que
> no se conoce de antemano. Por eso vienen los procedimientos de precisión especificada.

### 9.5 Precisión absoluta y relativa

> *"Pag 76 sí. Precisión absoluta/relativa"* — clase pre-examen. Parcial 2019-Weitz: *"Procedimientos
> de precisión relativa y absoluta. **Las dos fórmulas.**"*

| | **Error absoluto** | **Error relativo** |
|---|---|---|
| Definición | $\left|\bar{X}-\mu\right| = \beta$ con probabilidad $1-\alpha$ | $\dfrac{\left|\bar{X}-\mu\right|}{|\mu|} = \gamma$ con probabilidad $1-\alpha$ |
| Cuándo usarlo | Cuando importa la magnitud del error en las unidades del problema (± 2 minutos de espera) | Cuando importa el error como porcentaje (± 5% del valor) |
| Réplicas necesarias | $n_a^*(\beta) = \min\left\{ i \ge n : t_{i-1,\,1-\alpha/2}\sqrt{\dfrac{S^2(n)}{i}} \le \beta \right\}$ | $n_r^*(\gamma) = \min\left\{ i \ge n : \dfrac{t_{i-1,\,1-\alpha/2}\sqrt{S^2(n)/i}}{\left|\bar{X}(n)\right|} \le \dfrac{\gamma}{1+\gamma} \right\}$ |

En ambos casos se **asume que el estimador de la varianza poblacional (y de la media, en el relativo)
no cambiará al aumentar el número de réplicas**, y se busca el mínimo $i$ que hace caer la
semi-amplitud por debajo del error pedido.

> **De dónde sale el $\gamma/(1+\gamma)$**: el error relativo se define contra $\mu$ (desconocido) pero
> se estima contra $\bar{X}$. La corrección $\gamma/(1+\gamma)$ compensa ese sesgo.

**Problema de usar las fórmulas directamente**: $\bar{X}(n)$ y $S^2(n)$ pueden **no ser estimadores precisos** de sus parámetros poblacionales.
- Si $n_r^*(\gamma)$ resulta **más grande** que las réplicas realmente necesarias → se producen réplicas innecesarias, desperdiciando recursos computacionales.
- Si resulta **muy chico** → el estimador de $\mu$ basado en $n_r^*(\gamma)$ réplicas puede no ser preciso.

### 9.6 Procedimiento secuencial

Por lo anterior, se usa un procedimiento **secuencial**: se agregan réplicas **de a una** y se toman solo tantas como hagan falta.

```
1. Hacer n₀ ≥ 2 réplicas de la simulación y fijar n = n₀
2. Computar X̄(n) y δ(n,α) a partir de X₁, X₂, …, Xₙ
3. Si  δ(n,α) / |X̄(n)|  ≤  γ/(1+γ)
        → usar X̄(n) como punto de estimación de μ y PARAR
   Si no
        → reemplazar n por n+1, hacer una réplica adicional y volver al paso 2
```

> **Este es el procedimiento que se pide en el globalizador 2023 P10** ("Explique el procedimiento para
> determinar cuándo detener las corridas de simulación con el objetivo de obtener un desvío estándar
> determinado") y en el parcial 2019-Leale ejercicio 3b ("dado un número fijo $n$ de repeticiones,
> desarrolle el procedimiento para calcular la cantidad extra de repeticiones de tal forma de obtener
> un error relativo máximo de $\gamma\%$").

### 9.7 Elección de condiciones iniciales

Las medidas de rendimiento de una **simulación terminal** dependen explícitamente del estado del
sistema en el tiempo 0, así que hay que **elegir con cuidado las condiciones iniciales** para que sean
representativas del sistema real.

> Ejemplo: si simulás una guardia de hospital arrancando **vacía**, vas a subestimar las demoras si en
> la realidad el turno arranca con pacientes del turno anterior.

En una simulación **no terminal**, el problema se resuelve al revés: se descarta un **período de
calentamiento (warm-up)** al principio de la corrida para eliminar el efecto de las condiciones
iniciales, y solo se estadística lo que viene después.

### 9.8 Medidas múltiples de rendimiento — desigualdad de Bonferroni

Si $I_s$ es un intervalo de confianza del $100(1-\alpha_s)\%$ para la medida $\mu_s$, con $s = 1,\dots,k$, entonces la probabilidad de que **todos** los intervalos contengan simultáneamente sus respectivas medias satisface:

$$P(\mu_s \in I_s \ \forall s = 1,\dots,k) \ \ge\ 1 - \sum_{s=1}^{k}\alpha_s$$

**El problema**: si construís 10 intervalos al 90% ($\alpha_s = 0{,}1$ para cada uno), la cota queda
$1 - 10 \times 0{,}1 = 0$ — es decir, **la garantía conjunta es cero** y no podés concluir nada.

**La solución**: si querés que los $k$ intervalos tengan **en conjunto** al menos $100(1-\alpha)\%$ de confianza, elegí los $\alpha_s$ tales que $\sum_{s=1}^{k}\alpha_s = \alpha$. Se recomienda que **$k$ no sea mayor que 10**.

> Ejemplo: para 5 medidas con 90% de confianza conjunta, cada intervalo individual debe hacerse al
> $100(1 - 0{,}10/5)\% = 98\%$.

### 9.9 Método de media de lotes (batch means)

Se usa para el análisis de simulaciones **no terminales**. La idea es sacar varias "réplicas" de **una
sola corrida larga**, en vez de hacer muchas corridas cortas (que cargarían con el período transiente
cada una).

```
1. Correr la simulación el tiempo suficiente como para remover cualquier efecto transiente
   y proveer una cantidad de datos representativos del estado estacionario.
2. Dividir la duración restante de la corrida en sub-intervalos de tiempo → "lotes" (batches).
3. Computar las medidas de rendimiento promedio para cada lote, y usar las técnicas clásicas
   (media, S², intervalo de confianza t) tratando las medias de lotes como réplicas independientes.
```

**Problema**: los lotes sucesivos poseen cierta **auto-correlación** (el estado al final de un lote es
el estado inicial del siguiente). Una manera de reducirla es **eliminar ciertos lotes** (por ejemplo,
los pares o los impares), aunque eso reduce el número de observaciones independientes → intervalos de
confianza **más débiles**.

> **El trade-off**: lotes más largos → menos auto-correlación pero menos lotes (menos grados de
> libertad). Lotes más cortos → más lotes pero más correlacionados. No hay respuesta única.

### Fuentes

- `fuentes/resumenes/Resumen 1.pdf` (Pagliaro) — secciones 7, 8 y 10. **Es la fuente principal de esta unidad.**
- `fuentes/apuntes-catedra/Apunte Weitz con hojas rotadas y acotado.pdf` — cap. 9 (en inglés)
- `fuentes/clase-preexamen/Información clase pre-examen 1.txt` y `2.txt`
- `fuentes/examenes/parciales/2019/2019 - Parcial 2 - Leale.jpg` — ejercicio 3
- `fuentes/examenes/globalizador/2023-03-16.jpg` — pregunta 10

---

## Unidad 10 — Comparación de sistemas alternativos

> El otro bloque que no está en el resumen. Clase pre-examen: *"Cap 10 (comparando sistemas
> alternativos) sí. Pag 86 sí, 10.2.2 no."* Sale en el parcial 2019-Weitz (P1), el final 2019 (P1) y
> es la **pregunta frecuente #1** ("¿cómo se comparan dos simulaciones?"). Además, **es lo que exige
> el TPI**: el test de medias entre escenarios.

### 10.1 El planteo

Para $i = 1, 2$, sean $X_{i1}, X_{i2}, \dots, X_{in_i}$ observaciones IID del sistema $i$, y sea
$\mu_i = E(X_{ij})$ el valor de interés. Se quiere construir un intervalo de confianza para

$$\xi = \mu_1 - \mu_2$$

> **La lógica de la decisión**: si el intervalo de confianza para $\xi$ **contiene al 0**, no hay
> evidencia de diferencia significativa entre los sistemas. Si está enteramente **por encima** de 0,
> el sistema 1 es mayor; si está enteramente **por debajo**, el sistema 2 es mayor.
>
> Esto es exactamente lo que pide el TPI: *"no hay diferencia significativa" es un resultado válido si
> está bien fundamentado*.

### 10.2 Intervalo de confianza t-apareado (paired-t)

> Es el **"método de muestras apareadas"** de la pregunta frecuente #1. Es el que conviene usar en el TPI.

**No requiere que $X_{1j}$ y $X_{2j}$ sean independientes** — de hecho, conviene que estén
correlacionadas positivamente (ver números aleatorios comunes, §10.5).

Requiere $n_1 = n_2 = n$. Se aparean $X_{1j}$ con $X_{2j}$ y se define:

$$Z_j = X_{1j} - X_{2j}, \quad j = 1,2,\dots,n$$

Los $Z_j$ son variables aleatorias IID con $E[Z_j] = \xi$. Entonces:

$$\bar{Z}(n) = \frac{\sum_{j=1}^{n} Z_j}{n} \qquad \widehat{\mathrm{Var}}\left[\bar{Z}(n)\right] = \frac{\sum_{j=1}^{n}\left[Z_j - \bar{Z}(n)\right]^2}{n\,(n-1)}$$

$$\boxed{\bar{Z}(n) \ \pm\ t_{n-1,\,1-\alpha/2}\sqrt{\widehat{\mathrm{Var}}\left[\bar{Z}(n)\right]}}$$

> **Por qué funciona**: al restar de a pares, cualquier fuente de variabilidad **común** a las dos
> corridas se cancela. Queda solo la diferencia que le interesa al analista, con menos varianza →
> intervalo más angosto → más chance de detectar una diferencia real.

### 10.3 Intervalo de confianza de Welch

**No aparea** las observaciones. **Requiere que $X_{1j}$ sea independiente de $X_{2j}$**, pero permite
que $n_1 \ne n_2$.

Para $i = 1,2$:

$$\bar{X}_i(n_i) = \frac{\sum_{j=1}^{n_i} X_{ij}}{n_i} \qquad S_i^2(n_i) = \frac{\sum_{j=1}^{n_i}\left[X_{ij}-\bar{X}_i(n_i)\right]^2}{n_i - 1}$$

$$\boxed{\bar{X}_1(n_1) - \bar{X}_2(n_2) \ \pm\ t_{\hat{f},\,1-\alpha/2}\sqrt{\frac{S_1^2(n_1)}{n_1} + \frac{S_2^2(n_2)}{n_2}}}$$

donde $\hat{f} = g(S_1, S_2, n_1, n_2)$ son los **grados de libertad de Welch**:

$$\hat{f} = \frac{\left(\dfrac{S_1^2}{n_1} + \dfrac{S_2^2}{n_2}\right)^2}{\dfrac{(S_1^2/n_1)^2}{n_1-1} + \dfrac{(S_2^2/n_2)^2}{n_2-1}}$$

| | **t-apareado** | **Welch** |
|---|---|---|
| Independencia entre sistemas | **No** la requiere | **Sí** la requiere |
| $n_1 = n_2$ | **Sí**, obligatorio | No, pueden diferir |
| Varianza | Menor si hay correlación positiva | Mayor |
| Grados de libertad | $n-1$ | $\hat{f}$ (fórmula de Welch) |
| Cuándo usarlo | Podés controlar las semillas → **usalo** | No podés aparear (distinto nº de réplicas, corridas de origen distinto) |

### 10.4 Más de dos sistemas — ranking y selección

> *"Analisis de resultados MAS DE DOS SISTEMAS. Formulas"* — parcial 2019-Weitz P1.

**Objetivo**: seleccionar, entre $k$ sistemas, el que tenga el $\mu_i$ **más chico** (o más grande).

Sea $X_{ij}$ la variable de interés de la réplica $j$ del sistema $i$, $\mu_i = E(X_{ij})$, y sea
$\mu_{i_\ell}$ el $\ell$-ésimo más chico, de modo que $\mu_{i_1} \le \mu_{i_2} \le \dots \le \mu_{i_k}$.

Sea $CS$ el evento **"selección correcta"**. Se quiere $P(CS) \ge P^*$, siempre que
$\mu_{i_2} - \mu_{i_1} \ge d^*$, donde:

- $P^*$ = probabilidad mínima de selección correcta, con $P^* > 1/k$
- $d^*$ = **cantidad de indiferencia** ($d^* > 0$): diferencias menores a $d^*$ nos dan igual

**Procedimiento en dos etapas:**

**Etapa 1** — hacer $n_0 \ge 2$ réplicas de cada uno de los $k$ sistemas y computar, para $i=1,\dots,k$:

$$\bar{X}_i^{(1)}(n_0) = \frac{\sum_{j=1}^{n_0} X_{ij}}{n_0} \qquad S_i^2(n_0) = \frac{\sum_{j=1}^{n_0}\left[X_{ij}-\bar{X}_i^{(1)}(n_0)\right]^2}{n_0 - 1}$$

**Etapa 2** — computar el tamaño de muestra total $N_i$ para cada sistema:

$$N_i = \max\left\{n_0 + 1,\ \left\lceil \frac{h_1^2\,S_i^2(n_0)}{(d^*)^2} \right\rceil \right\}$$

donde $h_1$ es una constante que **se obtiene por tabla** (depende de $k$, $P^*$ y $n_0$). Después se
hacen las $N_i - n_0$ réplicas adicionales de cada sistema y se selecciona el de menor media global.

> **La idea**: los sistemas con más varianza necesitan más réplicas. La fórmula asigna réplicas
> proporcionalmente a $S_i^2$.

### 10.5 Números aleatorios comunes (common random numbers)

> Parcial 2019-Weitz P2: *"Definir en no más de 10 renglones: Números Aleatorios Comunes"*.

**Idea**: si el objetivo es determinar diferencias en la respuesta de un sistema debido al cambio de
algún parámetro, es intuitivamente razonable **comparar la respuesta del sistema bajo las mismas
circunstancias**. Eso implica usar **los mismos números aleatorios** para generar los tiempos de arribo
y de partida en las corridas a comparar.

**Por qué funciona, formalmente**: si $m_1$ y $m_2$ son las respuestas de las dos configuraciones,

$$\mathrm{Var}(m_1 - m_2) = \mathrm{Var}(m_1) + \mathrm{Var}(m_2) - 2\,\mathrm{Cov}(m_1, m_2)$$

Si se usan números aleatorios comunes, habrá **correlación positiva** entre las dos respuestas, o sea
$\mathrm{Cov}(m_1,m_2) > 0$, y **la varianza de la diferencia se reduce**.

> **Consecuencia práctica**: intervalo de confianza para $\xi$ más angosto con la misma cantidad de
> réplicas → se detectan diferencias más chicas. Es una **técnica de reducción de varianza**.
>
> **Requisito**: el generador tiene que ser **reproducible** (propiedad 3 de la Unidad 7). Por eso los
> pseudoaleatorios le ganan a los verdaderos aleatorios para esto.
>
> **Cómo se combina con lo anterior**: números aleatorios comunes + intervalo **t-apareado** es la
> receta estándar. El apareamiento aprovecha la correlación que los números comunes inducen.

### 10.6 Análisis de sensibilidad con intervalos de confianza (versión Weitz)

En el paso 9 de Weitz, la comparación de escenarios se plantea así:

1. Comparar estadísticamente los mejores escenarios.
2. Analizar la **intersección de los intervalos de confianza**.
3. Si hay **traslape**, realizar más réplicas o incrementar el tiempo de simulación.
4. El objetivo es **acortar los intervalos** hasta poder diferenciar las soluciones.

> **Ojo con el matiz**: mirar si los intervalos individuales se solapan es un criterio **conservador y
> no del todo correcto** — dos intervalos pueden solaparse y aun así la diferencia ser
> significativa. Lo riguroso es construir el intervalo **de la diferencia** (§10.2 / §10.3) y ver si
> contiene al 0. Weitz plantea la versión intuitiva; para el TPI conviene hacer el test de medias
> formal, que es lo que pide el enunciado.

### Fuentes

- `fuentes/resumenes/Resumen 1.pdf` (Pagliaro) — secciones 9 y 11. **Fuente principal.**
- `fuentes/apuntes-catedra/Apunte Weitz con hojas rotadas y acotado.pdf` — cap. 10 hasta pág. 86
- `fuentes/clase-preexamen/Preguntas frecuentes.docx` — pregunta 1
- `fuentes/examenes/parciales/2019/2019 - Parcial 2 - Weitz.txt`

---
## TPI — Trabajo Práctico Integrador

> Fuente: `fuentes/TPI Simulación - Enunciado.md`. Modalidad grupal, software **AnyLogic**.

### Conceptos clave

- **Objeto**: estudio de simulación completo sobre un **caso real**, partiendo de un problema de decisión concreto. Se modela el sistema, se experimenta y se emite una **recomendación fundada en evidencia estadística**.
- **Mínimo estructural**: un escenario **base** (sistema tal como está hoy) + al menos **un escenario alternativo** (hipótesis de mejora). Comparación por **corridas múltiples + test de medias**.
- "No hay diferencia significativa" **es un resultado válido** si está bien fundamentado. No hay que forzar que la mejora dé positiva.
- El informe se estructura sobre los **10 pasos de un estudio de simulación** (los 10 deben quedar referenciados, el orden es flexible):
  1. Formulación del problema y planificación del estudio
  2. Recolección de datos y definición del modelo
  3. Validación del modelo conceptual
  4. Construcción y verificación del programa
  5. Ejecuciones piloto
  6. Validación del modelo programado
  7. Diseño de experimentos
  8. Corridas de producción
  9. Análisis de los datos de salida
  10. Documentación, presentación y uso de resultados

### Entregables (ambos al Classroom, o no se considera entregado)

**1. Informe PDF**
- Hecho en **LaTeX** (mismas pautas que las entregas parciales).
- Portada, índice, introducción, desarrollo, conclusiones y recomendaciones, bibliografía.
- Referencia explícita a los 10 pasos.
- Explicación de los escenarios (≥2).
- Test de medias entre escenarios: **fórmulas empleadas + comentario de resultados**.
- Citas de todas las fuentes externas. **Wikipedia prohibida**.
- Se sube el archivo, no un link.

**2. Video de exposición**
- Criterio de exposición en vivo: caso → escenarios y variables medidas → análisis → conclusión.
- Debe mostrar un extracto de **AnyLogic corriendo**.
- **Todos los integrantes en cámara** (OBS o grabación de Zoom).
- Slides en Google Slides como apoyo.
- **Máx. 3 minutos, pauta estricta**. **Sin editar**.
- YouTube en visibilidad "Oculto", no marcar "contenido para niños". Se entrega el link.

### Causales automáticas de recuperatorio (checklist antes de entregar)

- [ ] Menos de dos escenarios
- [ ] Una sola corrida en alguno de los escenarios
- [ ] Falta el test de medias
- [ ] Video > 3 minutos
- [ ] Informe fuera de LaTeX
- [ ] Wikipedia como referencia
- [ ] Falta alguno de los dos entregables

### Criterios de selección del tema

Un tema sirve si cumple las cuatro:
1. **Aleatoriedad relevante** — hay fenómenos estocásticos que justifican simular (si no hay varianza, no hay TP).
2. **Datos disponibles o estimables** — hay datos de entrada, o una forma *defendible* de estimarlos.
3. **Hipótesis de mejora concreta** — existe al menos una modificación evaluable como escenario alternativo.
4. **Alcance acotable** — abordable en el cuatrimestre.

Casos de años anteriores: transporte y logística, salud y emergencias, producción industrial, organización de eventos masivos.

Se evalúa: claridad del problema, rigor de modelado e implementación, calidad del análisis y las conclusiones, efectividad de la exposición, **originalidad y aplicabilidad del caso**.

### Primera actividad — elección del tema

Formulario con integrantes (nombre y legajo) + **tres temas candidatos**, cada uno con:
- **Tema**: una oración en formato libre.
- **Observaciones**: comentario breve (motivo de la elección, acceso previsto a la información).

Prioridad **por fecha de entrega del formulario** (conviene mandarlo temprano). El docente confirma viabilidad o pide reformulación; **no arrancar el modelado antes de esa confirmación**.

**Estado**: entregable armado —
- Fuente en markdown: [`TPI/formulario-eleccion-tema.md`](TPI/formulario-eleccion-tema.md)
- Documento Word: [`TPI/TPI_Simulacion_Propuesta_de_Tema.docx`](TPI/TPI_Simulacion_Propuesta_de_Tema.docx), con la carátula, estilos, header/footer y logo heredados de los informes de RD (ver `rd-informe-formato` en memoria).

Se presentan **2 temas** (el enunciado pide 3 — decisión del grupo, con el riesgo de reformulación anotado en el propio documento).

**Integrantes**: Juan Cruz Bonadeo (53533) y Matias Estevez (53528).

### Temas candidatos y datasets verificados

| # | Tema | Dataset | Estado |
|---|---|---|---|
| 1 | **Ecobici** — rebalanceo en el corredor Constitución/Retiro–Catalinas/Puerto Madero | [BA Data — Bicicletas Públicas](https://data.buenosaires.gob.ar/dataset/bicicletas-publicas) (3.559.284 viajes 2024) + capacidad de 394 estaciones vía feed GBFS del operador | ✅ Descargado y perfilado |
| 2 | **Despacho de emergencias** (San Francisco) — unidad adicional / política de despacho | [DataSF `nuek-vuh3`](https://data.sfgov.org/Public-Safety/Fire-Department-and-Emergency-Medical-Services-Dis/nuek-vuh3) (7.386.640 registros) | ✅ Muestra semanal perfilada |
| — | *Reserva*: **molinetes de subte** — dimensionamiento en hora pico | [BA Data — Subte Viajes Molinetes](https://data.buenosaires.gob.ar/dataset/subte-viajes-molinetes) (hasta 2025) | ⚠️ Cobertura verificada, columnas no. Fuera de la entrega |

Hallazgo que sostiene el Tema 1: el desbalance de Ecobici **no es anual sino intradiario y se revierte**. En días hábiles, Constitución pierde ~19,7 bicicletas netas entre 7 y 10 h (sobre 54 anclajes) y recupera ~15,1 entre 17 y 20 h; Madero Office hace el espejo, recibiendo ~14,5 netas a la mañana sobre 28 anclajes. Es el patrón commuter terminal ferroviaria → área de oficinas.

### Dudas / pendientes

- Fechas de entrega y presentación: se publican en Classroom (no están en el enunciado).
- Confirmar que la **Comisión 403** (heredada del formato de RD) aplique también a Simulación, y si hay que consignar los profesores de la cátedra en la carátula.
- Decidir si se suma un tercer tema: el enunciado pide 3 y se entregan 2.
- Enviar el formulario (prioridad por fecha de entrega).
- Confirmar si la plantilla LaTeX de las entregas parciales se reutiliza tal cual.
- Los archivos de datos (765 MB) no van al repo — mantenerlos afuera o en `.gitignore`.

### Fuentes

- `fuentes/TPI Simulación - Enunciado.md`
- Perfilado de datos propio (2026-07-29), ver anexo de `TPI/formulario-eleccion-tema.md`

---


---

## Log

- **2026-08-25**: ingesta masiva de todo el material de `archivo/`. Se copiaron a `fuentes/` los tres apuntes oficiales de cátedra (Weitz, Naylor cap. 4, Números pseudoaleatorios), la teoría de Flamini, los apuntes extra, los 13 resúmenes viejos, los 6 ejercicios resueltos de práctica, los modelos de AnyLogic y Mathematica, los 5 TPs y **todos los exámenes** (7 parciales, 6 finales, 1 globalizador). Todo convertido a markdown en `fuentes/txt/`, incluyendo la transcripción por visión de los PDFs y fotos escaneados (Weitz 79 pág., Naylor 29 pág., Flamini 24 pág., 7 exámenes en imagen). Wiki **reescrita completa**: de 3 secciones a 10 unidades más un mapa del parcial. Unidades nuevas: 4 (inventarios), 5 (10 pasos, las dos listas), 6 (probabilidad), 7 (generación de números y variables aleatorias), 8 (colas analíticas), 9 (análisis de salidas), 10 (comparación de sistemas). Hallazgos: el resumen del parcial **no cubre** generación de variables aleatorias, análisis de salidas ni comparación de sistemas; las preguntas 8/9/10 se repiten casi textuales en 2022-2023-2024; y el parcial **2025 cambió a multiple choice** con preguntas de AnyLogic y LaTeX.

- **2026-07-31**: armado el entregable en Word (`TPI/TPI_Simulacion_Propuesta_de_Tema.docx`) reutilizando carátula, estilos, header/footer y logo del informe de RD. Grupo actualizado a Bonadeo + Estevez (sale Casermeiro) y la propuesta reducida a 2 temas (Ecobici y emergencias); molinetes queda como reserva documentada.
- **2026-07-29**: redactado el formulario de elección de tema (`TPI/formulario-eleccion-tema.md`) con los 3 candidatos: Ecobici (prioritario), despacho de emergencias SF y molinetes de subte. Perfilados y verificados los datasets: Ecobici 2024 (3.559.284 viajes, 395 estaciones) + capacidad por GBFS, y DataSF `nuek-vuh3` (7,39 M registros, muestra semanal). Detectado el desbalance intradiario reversible de Ecobici, que es el fenómeno que justifica el escenario de rebalanceo. Documentadas las limitaciones a declarar (solo viajes exitosos, 9,11% de viajes <1 min, 13,47% origen=destino).
- **2026-07-29**: ingerido el enunciado del TP Integrador (`fuentes/SIM/TPI Simulación - Enunciado.md`). Se creó la sección 3 (TPI) con consigna, entregables, causales de recuperatorio, criterios de selección de tema y primera actividad. Pendiente: elegir los 3 temas candidatos.
- **2026-07-08**: ingerido el contenido de la wiki anterior de SIM (construida a partir de `Simulación_clase_2_2026.pdf`, `Simulacion_Intro_Completa.pdf`, `Resumen_de_Simulación.pdf`). Se creó el índice (Unidades 1 y 2) y se desarrollaron ambas unidades. Falta cargar el programa completo de la materia para completar el índice (Unidades 3+).
