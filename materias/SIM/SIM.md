# SIM — Wiki

> Simulación · UTN-ISI · 4° año
> Migrado desde el Proyecto de Claude (PDFs subidos: `Simulación_clase_2_2026.pdf`, `Simulacion_Intro_Completa.pdf`, `Resumen_de_Simulación.pdf`).

## Índice

1. Introducción a la Simulación
2. Simulación a Eventos Discretos (DES)

> Unidades 3 en adelante: pendientes de que suba el programa completo de la materia o más material de clase.

---

## Unidad 1 — Introducción a la Simulación

### Conceptos clave

- **Simulación**: imitación de la operación de un proceso o sistema del mundo real a través del tiempo. Implica generar una "historia artificial" del sistema y observarla para inferir las características operacionales del sistema real.
- **Sistema**: colección de entidades que interactúan entre sí y cumplen un fin o propósito. Es una representación lógica — un mismo proceso puede dar lugar a varios sistemas distintos (ej: un supermercado puede modelarse como sistema de colas, de inventario, de logística, etc.).
- **Estado del sistema**: conjunto de variables necesarias para describir el sistema en un momento dado, en relación a los objetivos del estudio.
- **Modelo de simulación**: conjunto de supuestos expresados como relaciones matemáticas, lógicas y simbólicas, usado para responder preguntas "¿qué pasaría si?" y evaluar cambios antes de implementarlos en el sistema real.

**Categorías de sistemas** (clasificaciones que se combinan entre sí, no son excluyentes):

| Par | Definición A | Definición B |
|---|---|---|
| Continuo vs. Discreto | Variables de estado cambian continuamente (ej: flujo de fluidos) | Variables cambian en puntos específicos del tiempo (ej: colas) |
| Estático vs. Dinámico | Sistema evaluado en un punto del tiempo (ej: Monte Carlo) | Evolución del sistema a lo largo del tiempo |
| Determinístico vs. Estocástico | Sin componentes aleatorios, resultados predecibles | Incluye variables aleatorias, resultados varían entre corridas |

**Tipos de estudio de un sistema** (jerarquía de decisiones):
- Sistema real vs. Modelo del sistema
- Modelo físico vs. Modelo matemático
- Solución analítica vs. Simulación

**Cuándo es necesaria la simulación:**
- Complejidad que impide soluciones analíticas
- Imposibilidad de experimentar con el sistema real
- Costo y tiempo de experimentación directa
- Necesidad de control experimental
- Sistema aún no existe (fase de diseño)

**Cuándo NO es necesaria:**
- Hay solución analítica disponible (ej: modelo M/M/1)
- Existen otros enfoques de modelado válidos
- El problema no tiene variabilidad significativa

> Simulación y métodos analíticos pueden ser complementarios entre sí, no mutuamente excluyentes.

**Ventajas**: flexibilidad de diseño, estimación de rendimiento bajo condiciones nuevas, identificación de cuellos de botella, exploración segura de escenarios, comprensión profunda del sistema, comunicación de resultados más simple que con soluciones analíticas.

**Desventajas**: costo de desarrollo (tiempo y recursos), resultados estocásticos (cada corrida da solo una estimación, no un resultado exacto), riesgo de uso sin el rigor necesario, requiere experiencia (es arte y ciencia a la vez).

**Áreas de aplicación**: manufactura y logística, sistemas de salud, redes de comunicaciones, sistemas de transporte, cadenas de suministro, servicios financieros, sistemas militares, ecosistemas y medio ambiente.

### Desarrollo

La materia parte de una idea simple: en el mundo real hay procesos con partes interrelacionadas que persiguen un objetivo (sistemas), y para entender cómo funcionan hay que representarlos en un modelo. La simulación es una de varias formas de estudiar un sistema — la alternativa a experimentar directamente sobre el sistema real (que suele ser costoso, lento o directamente imposible, por ejemplo "¿conviene agregar una nueva pista en el aeropuerto?").

El árbol de decisión conceptual es: sistema real → ¿experimentar con el sistema real o con un modelo? → si es con un modelo, ¿físico o matemático? → si es matemático, ¿tiene solución analítica o hay que simularlo?

Un modelo de simulación se clasifica según tres ejes independientes (continuo/discreto, estático/dinámico, determinístico/estocástico). La materia se enfoca en el **discreto** dentro del eje continuo/discreto — es decir, en la Simulación a Eventos Discretos (DES), que se desarrolla en la Unidad 2.

La simulación se justifica cuando el sistema es demasiado complejo para una solución analítica cerrada, o cuando experimentar con el sistema real es inviable por costo, riesgo o porque el sistema todavía no existe. Pero no reemplaza a los métodos analíticos cuando estos están disponibles (ej: colas simples tipo M/M/1) — son herramientas complementarias.

### Ejercicios resueltos tipo

(sin datos en el historial)

### Dudas / pendientes

(sin datos en el historial)

### Fuentes

- `Simulacion_Intro_Completa.pdf`
- `Resumen_de_Simulación.pdf` (sección "Definición de Sistema" y "Categorías de sistemas")

---

## Unidad 2 — Simulación a Eventos Discretos (DES)

### Conceptos clave

- **Evento**: ocurrencia instantánea que puede cambiar el estado del sistema.
- **DES (Discrete Event Simulation)**: las variables de estado cambian instantáneamente en momentos separados del tiempo, cada uno de esos momentos es un evento. El "reloj" de simulación está definido por los eventos, no por el tiempo continuo — solo importan los instantes en que ocurre algo. El avance del tiempo se da evento a evento (no por incremento fijo).

**Modelo de referencia: una cola, un servidor**

- **Eventos**: arribo de un cliente / servicio completo (partida) de un cliente.
- **Variables de estado**: estado del servidor (libre/ocupado), cantidad de clientes en cola, tiempo de arribo de cada cliente.
- **Efecto de cada evento**:
  - *Arribo*: si el servidor estaba libre → pasa a ocupado; si estaba ocupado → incrementa en 1 la cola.
  - *Partida (servicio completo)*: si no hay nadie en cola → servidor pasa a libre; si hay cola → decrementa en 1 la cola (el servidor sigue ocupado, atiende al siguiente).
- **Reloj de simulación**: puede avanzar por "próximo evento" (lo que usa DES) o por "incremento fijo" (otro enfoque, no el de DES).

**Rutina de eventos (estructura general de un motor de DES):**

1. **Initialization routine**: reloj de simulación = 0; inicializar estado del sistema; inicializar lista de eventos.
2. **Main program** (se repite mientras la simulación no termine):
   1. Invocar timing routine
   2. Invocar event routine correspondiente al evento i
3. **Timing routine**: determinar cuál es el próximo evento; avanzar el reloj de simulación a ese instante.
4. **Event routine i**: actualizar el estado del sistema; actualizar contadores estadísticos; generar eventos futuros (usando rutinas de generación de variables aleatorias).
5. **Report generator** (al terminar la simulación): calcular estimadores; escribir el reporte.

**Notación de la línea de tiempo de eventos:**
- `eᵢ`: evento i-ésimo
- `tᵢ`: instante de tiempo en que ocurre un evento
- `Aᵢ`: tiempo entre llegadas (arribos)
- `Sᵢ`: tiempos de servicio
- `Dᵢ`: demora del cliente i (tiempo en cola, sin contar el tiempo de servicio)
- `cᵢ`: notación asociada a eventos de partida/completado en la línea de tiempo (aparece en el diagrama de ejemplo junto a los eventos de servicio completo)

### Medidas resumen (criterio de parada: n clientes fijos)

Todas son **medidas muestrales**: corresponden a una única corrida (realización) de la simulación, no a un valor poblacional exacto.

1. **d(n) — Demora promedio de clientes en cola**
   - Demora = tiempo entre el arribo de un cliente y el momento en que toma servicio (**no** incluye el tiempo de servicio en sí).
   - Dadas las demoras individuales D₁, D₂, ..., Dₙ de los n clientes:

     d̂(n) = (D₁ + D₂ + ... + Dₙ) / n

2. **q(n) — Cantidad promedio de clientes en cola**
   - Se define a partir de una función Q(t) (o T(t) según el archivo) que mide la cantidad de clientes en cola en el instante t.
   - Sea T(n) el tiempo en que se completa el servicio del n-ésimo cliente, y pᵢ la proporción del tiempo total en que hay exactamente i clientes en cola (pᵢ = Tᵢ / T(n), donde Tᵢ es el tiempo total de la corrida con i clientes en cola).
   - q(n) es el promedio ponderado por tiempo de la cantidad de clientes en cola:

     q̂(n) = Σ pᵢ · i  (equivalente a integrar/ponderar Q(t) sobre el tiempo total T(n))

3. **u(n) — Utilización promedio del servidor**
   - Se define a partir de una función B(t) = 1 si el servidor está ocupado en t, 0 si está libre.
   - Representa la proporción del tiempo total en que el servidor está ocupado = probabilidad de encontrarlo ocupado.
   - û(n) = (tiempo total ocupado) / T(n)

### Desarrollo

La Unidad 2 formaliza el enfoque DES usando como caso de estudio recurrente el modelo de **una cola con un servidor**. La idea central que atraviesa toda la unidad es que en DES el tiempo "salta" de evento en evento — no hay pasos de tiempo fijos, solo importan los instantes t₁, t₂, t₃... donde ocurre un arribo o una partida.

El modelo tiene dos tipos de evento (arribo y partida) que modifican dos variables de estado (estado del servidor: libre/ocupado, y longitud de la cola). La lógica de actualización de estado es simétrica: un arribo mueve al cliente directamente al servidor si está libre, o a la cola si está ocupado; una partida libera al servidor si no hay cola, o lo deja ocupado atendiendo al siguiente cliente de la cola (decrementándola en 1).

Sobre este modelo se construyen tres medidas resumen, cada una respondiendo una pregunta distinta:
- d(n) responde "¿cuánto espera en promedio un cliente antes de ser atendido?" — es un promedio simple sobre los n clientes.
- q(n) responde "¿cuántos clientes en promedio hay en la cola en un instante cualquiera?" — es un promedio ponderado por el tiempo que la cola pasa en cada valor posible (0, 1, 2, ... clientes), no un promedio simple sobre clientes. Esta es la distinción conceptual más importante de la unidad: d(n) promedia sobre *clientes*, q(n) y u(n) promedian sobre *tiempo*.
- u(n) responde "¿qué fracción del tiempo estuvo el servidor ocupado?" — mismo tipo de promedio ponderado por tiempo que q(n), pero aplicado a una variable binaria (ocupado/libre) en lugar de a la longitud de cola.

Las tres son estimadores muestrales: dependen de la corrida particular de la simulación (la "realización"), por lo que dos corridas del mismo modelo pueden dar valores distintos de d(n), q(n) y u(n). Este punto de "profundizar más adelante" queda anunciado en la clase 2 pero sin desarrollo adicional en el material disponible — probablemente se trabaje en unidades siguientes con conceptos de estadística de la simulación (varianza de estimadores, número de corridas, etc.).

La rutina de eventos (initialization → main program → timing routine → event routine → report generator) es el esqueleto genérico de cualquier motor de simulación a eventos discretos, independientemente del sistema modelado. Vale la pena memorizar el flujo porque es la base conceptual para programar un simulador (en Python o AnyLogic más adelante en la materia).

### Ejercicios resueltos tipo

(sin datos en el historial — el material disponible es teórico/conceptual, no incluye ejercicios numéricos resueltos)

### Dudas / pendientes

- La notación `cᵢ` en el diagrama de línea de tiempo de eventos (`Simulacion_Intro_Completa.pdf`) no está explícitamente definida en el texto — se infiere que corresponde a instantes de eventos de partida/completado, pero convendría confirmarlo con la cátedra o con el archivo original si tenés el diagrama completo.
- No hay todavía ejemplos numéricos completos (tabla de simulación paso a paso con arribos, servicios y cálculo de d(n), q(n), u(n) sobre datos concretos) en los archivos disponibles.

### Fuentes

- `Simulación_clase_2_2026.pdf`
- `Simulacion_Intro_Completa.pdf` (sección "Simulación a eventos discretos" en adelante)
- `Resumen_de_Simulación.pdf` (páginas 2 y 3)

---

## Log

- **2026-07-08**: ingerido el contenido de la wiki anterior de SIM (construida a partir de `Simulación_clase_2_2026.pdf`, `Simulacion_Intro_Completa.pdf`, `Resumen_de_Simulación.pdf`). Se creó el índice (Unidades 1 y 2) y se desarrollaron ambas unidades. Falta cargar el programa completo de la materia para completar el índice (Unidades 3+).
