# Podcast SIM 1 de 8 — Qué es simular y cómo se encara un estudio

Fuente para un episodio de podcast de estudio. Materia: Simulación (UTN, Ingeniería en
Sistemas, 4.º año). Sirve para el primer parcial, el sábado 7 de noviembre de 2026: integrado
teórico-práctico y probablemente multiple choice. Las respuestas del banco son la clave revisada
por nosotros, no la corrección oficial de la cátedra.

## Indicaciones para el episodio

Las definiciones exactas de sistema, modelo y simulación (el parcial las pregunta "según el texto"), cuándo conviene simular y cuándo no, los elementos de la simulación según la cátedra y los 10 pasos de Weitz frente a los de Law. Insistir en la diferencia entre verificación y validación.

## Contenido principal

### 1. Qué es simular

*Fuentes: Law cap. 1 (Weitz), diapositivas de la clase 1 y AnyLogic in 3 Days.*

#### 1.1 Las cuatro definiciones base

**Sistema.** Es una colección de **entidades** (personas, máquinas) que **actúan e interactúan** hacia el logro de algún **fin lógico**. El sistema no viene dado por la realidad: **lo define el objetivo del estudio**. Un mismo supermercado puede ser "la línea de cajas" o "la cadena de abastecimiento", según la pregunta que queramos responder.

**Estado del sistema.** Es el conjunto de variables necesarias para describir el sistema en un instante, **en relación con los objetivos** del estudio. Por ejemplo: cuántos clientes hay en la cola y si el cajero está libre.

**Modelo.** Es un conjunto de **supuestos**, expresados como relaciones matemáticas, lógicas y simbólicas, que representan el comportamiento del sistema. Siempre es una **abstracción**: incluye lo que creemos importante y deja afuera el resto. Por eso **siempre es menos complejo que el sistema real**.

**Simulación.** Es la imitación de la operación de un sistema real **a lo largo del tiempo**. Genera una **historia artificial** del sistema y la observa para **inferir** sus características. Técnicamente, usa la computadora para **evaluar numéricamente** un modelo y **estimar** las medidas que nos interesan.

> **Ojo:** las cuatro se confunden a propósito en el multiple choice. "Un conjunto de ecuaciones que describen un proceso" es un **modelo**. "Un programa que imita al sistema" es una **simulación**. La única que es **sistema** es "colección de entidades que interactúan hacia un fin lógico".

#### 1.2 Formas de estudiar un sistema

El árbol responde tres preguntas, una por bifurcación:

1. **¿Sistema real o modelo?** Experimentar con el sistema real sería ideal, pero rara vez se puede: cuesta mucho, es riesgoso o el sistema todavía no existe. Por eso se construye un modelo.
2. **¿Modelo físico o matemático?** Los físicos (maquetas, simuladores de vuelo) se usan poco en investigación operativa. Los matemáticos representan el sistema con relaciones lógicas y cuantitativas.
3. **¿Solución analítica o simulación?** Si el modelo es simple, se resuelve con fórmulas y el resultado es **exacto**. Si es demasiado complejo, se simula, y el resultado es una **estimación**.

> **Ojo:** "la solución analítica es exacta" es **verdadero**. "La simulación reemplaza a la solución analítica" es **falso**: si existe una solución analítica eficiente, **se usa esa**. Las dos son **complementarias**. La simulación puede verificar los supuestos de un modelo analítico, y un modelo analítico puede sugerir alternativas que después se simulan.

#### 1.3 Clasificación de los modelos de simulación

Hay tres ejes independientes. Un modelo puede ser, por ejemplo, dinámico, estocástico y discreto a la vez:

| Eje | Una punta | La otra punta |
|---|---|---|
| **Tiempo** | **Estático**: un instante, o el tiempo no importa (Montecarlo) | **Dinámico**: el sistema evoluciona en el tiempo |
| **Azar** | **Determinístico**: sin variables aleatorias; fijadas las entradas, la salida queda determinada | **Estocástico**: con variables aleatorias; **la salida es una estimación** y cambia entre corridas |
| **Cambio de estado** | **Continuo**: las variables cambian continuamente (fluidos, la posición de un avión) | **Discreto**: las variables cambian en instantes puntuales (colas) |

Los modelos de la materia (la cola y el inventario) son **dinámicos, estocásticos y discretos**.

> **Ojo:** un modelo discreto **no** tiene por qué representar un sistema discreto. Se elige uno u otro según los **objetivos** del estudio.

#### 1.4 Cuándo conviene simular y cuándo no

| Conviene simular | No hace falta simular |
|---|---|
| La complejidad impide una solución analítica | Hay solución analítica disponible (por ejemplo M/M/1) |
| No se puede experimentar con el sistema real (costo, riesgo) | Otros enfoques de modelado alcanzan |
| Se necesita control experimental | El problema no tiene variabilidad significativa |
| El sistema todavía no existe (etapa de diseño) | |

**Ventajas**:

- Probar diseños, reglas y flujos nuevos sin comprometer recursos reales.
- Estimar el rendimiento bajo condiciones nuevas.
- Encontrar cuellos de botella.
- Responder preguntas del tipo "¿qué pasaría si…?" sin riesgo.
- Comunicar los resultados con animaciones.

AnyLogic in 3 Days agrega dos más: el modelo **refleja naturalmente la estructura del sistema**, y una vez elegido el nivel de abstracción **suele ser más fácil de construir que un modelo analítico**.

**Desventajas**:

1. **Cada corrida da solo una estimación, no un resultado exacto.** Por eso hacen falta varias corridas.
2. Desarrollar el modelo cuesta caro y lleva tiempo.
3. Se puede usar sin el rigor necesario y terminar confiando en un modelo que no es válido.
4. Requiere experiencia: es tanto un arte como una ciencia.

Además, para **optimizar** es mejor un buen modelo analítico.

**Riesgos que hacen fracasar un estudio** (Law):

- objetivos mal definidos;
- un nivel de detalle inadecuado;
- tratar el estudio como "solo programar";
- no recolectar buenos datos;
- usar distribuciones arbitrarias;
- no definir un período de calentamiento;
- **sacar conclusiones de una sola corrida**.

**Para simular hace falta información de la realidad, o al menos estimaciones.** En cambio, **no hace falta**:

- que el modelo esté "totalmente testeado";
- usar computadora para todo modelo (hay modelos físicos);
- la programación orientada a objetos.

### 2. Los elementos de la simulación

*Fuentes: el cap. 1 en castellano del apunte de Weitz y las diapositivas "Pasos de la simulación". Las definiciones van con la redacción del profe.*

| Elemento | Definición de la cátedra | Ejemplo en un banco |
|---|---|---|
| **Sistema** | Conjunto de elementos. **Define el alcance** | el banco |
| **Estado del sistema** | Condición del sistema en un momento determinado | 3 en cola, cajero ocupado |
| **Evento** | Cambio en el estado actual del sistema | llega un cliente |
| **Entidad** | Elemento **responsable de que cambie el estado** del sistema | el cliente |
| **Localizaciones** | Lugares donde las entidades pueden detenerse (son **estáticas**) | la fila, la sala de espera |
| **Recursos** | Dispositivos para llevar a cabo un evento (son **dinámicos**) | el cajero |
| **Atributo** | Característica de una entidad | el tipo de trámite del cliente |
| **Variables** | Condiciones cuyos valores se modifican | el tiempo entre llegadas |
| **Reloj de la simulación** | Registra el tiempo **simulado**, que no tiene relación con el tiempo de CPU | |

Las diapositivas de la clase 1 dan tres ejemplos:

| | Entidades | Recursos | Variable | Medida de rendimiento |
|---|---|---|---|---|
| Banco | clientes | cajeros | tiempo entre llegadas | tiempo de espera |
| Fábrica | productos | máquinas | tiempos de proceso | productividad |
| Red de computadoras | paquetes | routers | llegada de paquetes | latencia, *throughput* |

**Los tres tipos de variables**, en el vocabulario de la práctica:

| Tipo | Qué son | En la cola simple |
|---|---|---|
| **Exógenas** | Variables aleatorias que **entran** al modelo; hay que conocer su distribución | tiempo entre arribos, tiempo de servicio |
| **De estado** | Describen el sistema en cada instante | servidor libre u ocupado, nº en cola |
| **Endógenas** (de respuesta) | Las **medidas de rendimiento** que **salen** del modelo | $d(n)$, $q(n)$, $u(n)$ |

> **Ojo:** el profe define el evento como "**cambio** en el estado". Law es más preciso: un evento es una ocurrencia instantánea que **puede** cambiar el estado, y a veces solo sirve para **terminar** la simulación o para **programar decisiones**. Si la opción dice que "**siempre** cambia el estado", desconfiá.

### 6. Los pasos de un estudio de simulación

*Fuentes: el cap. 1 en castellano del apunte de Weitz y las diapositivas "Pasos de la simulación".*

Lo que el profe agrega en las diapositivas:

1. **Definición del sistema bajo estudio.**
   - Qué entra y qué queda afuera (el alcance).
   - Cuál es el problema concreto.
   - Los supuestos y las interacciones entre los elementos.
2. **Generación del modelo de simulación base.**
   - Relaciones, gráficos e indicadores de salida.
   - **Los datos todavía no importan en esta etapa.**
3. **Recolección y análisis de datos.**
   - Cómo se comportan las variables y qué distribuciones siguen.
4. **Generación del modelo preliminar.**
   - Integra los pasos anteriores.
   - Debe representar lo mejor posible el estado habitual del sistema.
5. **Verificación.**
   - ¿El programa funciona?
   - ¿Los parámetros son correctos?
   - ¿Se completa una corrida sin problemas?
6. **Validación.**
   - A entradas similares, ¿da salidas similares a la realidad?
   - Se hace junto con el cliente.
7. **Generación del modelo final.**
   - Es el escenario **raíz** contra el que se comparan los demás.
8. **Determinación de los escenarios.**
   - Ideas nuevas, cambios sugeridos.
   - Versiones **optimista, pesimista e intermedia**.
9. **Análisis de sensibilidad.**
   - ¿Hay **diferencia estadísticamente significativa** entre escenarios? Se responde con intervalos de confianza.
10. **Documentación, sugerencias y conclusiones.**
    - "Documentar todo, todo, todo."

**Law tiene otra lista de 10 pasos**:

1. Formular el problema.
2. **Recopilar datos y definir el modelo.**
3. **Validar el documento de supuestos.**
4. Programar y **verificar**.
5. Corridas piloto.
6. **Validar el modelo programado.**
7. Diseñar experimentos.
8. Corridas de producción.
9. Analizar las salidas.
10. Documentar.

> **Ojo:** si preguntan "el segundo paso", las opciones usan el vocabulario de Weitz, así que la respuesta es **"generación del modelo de simulación base"**. "Recolección de datos" es el paso 3 de Weitz (y parte del paso 2 de Law).
>
> **Verificar** es comprobar que el programa hace lo que quise programar: es *debugging*. **Validar** es comprobar que el modelo representa la realidad. En Weitz se verifica (5) antes de validar (6). En Law, en cambio, hay una validación **antes** de programar (el documento de supuestos, paso 3).

## Preguntas de parcial y de práctica sobre este tema

**1.4** (parcial 2025) **"Según el texto", ¿cuál es la definición de sistema?**
A) conjunto de ecuaciones · B) colección de entidades que actúan e interactúan hacia el logro de algún fin lógico · C) modelo computacional que imita · D) algoritmo de nº aleatorios · E) todas

✅ **B**, la definición textual de Law (Schmidt y Taylor). A describe un **modelo matemático** y C una **simulación**. "Todas" es la trampa de no distinguir **sistema / modelo / simulación**.
*Unidad 1, "Conceptos clave".*

**1.10** (parcial 2025) **Principal diferencia entre verificación y validación**
A) la verificación comprueba que el modelo funcione correctamente; la validación lo compara con la realidad · B) la verificación se hace antes que la validación · C) la verificación usa datos reales · D) la verificación es opcional · E) A y B

◐ **A.** A es la diferencia conceptual: **verificar** es preguntar si el programa hace lo que quise programar, o sea debugging. **Validar** es preguntar si el modelo representa al sistema real.
Sobre B: en los 10 pasos de **Weitz**, la verificación (paso 5) va antes que la validación (paso 6). En **Law** hay una validación antes de programar, la del documento de supuestos (paso 3), y otra después (paso 6). Si la cátedra piensa con la lista de Weitz, que es la que usa en la 1.15, puede tomar B como verdadera y la clave sería **E**.
**Criterio:** si el enunciado pregunta por la *diferencia*, marcá A. Si alguna vez pregunta "¿cuál de estas afirmaciones es verdadera?", B también lo es según Weitz.
*Unidad 5.*

**1.15** (parcial 2025) **¿Cuál es el segundo paso de un estudio de simulación?**
✅ **B**, generación del modelo de simulación base. Es la lista de **Weitz**: 1 definición del sistema → **2 modelo base** → 3 recolección y análisis de datos → 4 modelo preliminar → 5 verificación → 6 validación → 7 modelo final → 8 escenarios → 9 sensibilidad → 10 documentación.
**Ojo:** en **Law** el paso 2 es "recopilar datos y definir el modelo". Por eso existe la opción A como trampa. Como las opciones usan el vocabulario de Weitz, la respuesta es B.
*Unidad 5.*

**2.1** (parcial 2025) **La simulación reemplaza a la solución analítica para resolver problemas complejos con solución.** → ✅ **F**
Si hay solución analítica, **se usa**. Simulación y métodos analíticos son **complementarios**: la simulación se justifica cuando no hay solución cerrada. El alumno marcó V: error.

**2.2** (parcial 2025) **Para simular hace falta información del funcionamiento de la realidad o estimaciones.** → ✅ **V**
Sin datos o estimaciones no hay distribuciones de entrada. Es el paso 3 de Weitz.

**2.3** (parcial 2025) **Un modelo es un recorte de la realidad y solo puede usarse si está totalmente testeado.** → ✅ **F**
La primera mitad es cierta. La trampa es el "totalmente": ningún modelo está totalmente probado, y se usa una vez **validado** para el objetivo del estudio.

**2.4** (parcial 2025) **Para construir modelos siempre hacen falta herramientas informáticas.** → ✅ **F**
Hay modelos **físicos**, como maquetas, y modelos **matemáticos** que se resuelven analíticamente a mano.

**2.5** (parcial 2025) **La simulación por computadora surgió en los últimos 30 años.** → ✅ **F**
Viene de los años 40, con el método de Montecarlo en el Proyecto Manhattan (von Neumann y Ulam). Von Neumann propuso el método de los cuadrados centrales en 1946. *(Conocimiento general: no está en la wiki.)*

**2.7** (parcial 2025) **La solución analítica es exacta.** → ✅ **V**
Law: si el modelo es simple, se puede obtener una solución analítica **exacta**. La simulación da **estimaciones**.

**E13** (pregunta inventada por alumnos de 2025) **Montecarlo** se asocia principalmente con: A) procesos determinísticos · B) procesos estocásticos complejos · C) GIS · D) POO

→ Respuesta: ⚠️ Los alumnos ponían **A**, y está mal según su propio texto: *"el término Monte Carlo se asocia con la simulación de procesos estocásticos, aunque **originalmente** también se aplicaba a problemas determinísticos"*. **Clave: B**

**P17** (práctica, no oficial) V o F: un modelo estocástico produce una estimación de las características del sistema, no un valor exacto.

→ Respuesta: **V**. Es la principal desventaja del modelo estocástico.

**P26** (práctica, no oficial) Según las diapositivas de la cátedra, la **entidad** es: A) el lugar donde se detienen los clientes · B) el elemento responsable de que cambie el estado del sistema · C) el dispositivo que lleva a cabo un evento · D) una característica de un recurso · E) A y C

→ Respuesta: **B**. Definición de la cátedra. A son las localizaciones y C los recursos.

**P27** (práctica, no oficial) Las **localizaciones** y los **recursos** se diferencian en que: A) las localizaciones son estáticas (lugares donde las entidades se detienen) y los recursos dinámicos (llevan a cabo eventos) · B) son sinónimos · C) los recursos son estáticos · D) las localizaciones son atributos de la entidad · E) B y D

→ Respuesta: **A**.

**P32** (práctica, no oficial) V o F: en el paso 2 de Weitz (generación del modelo base), los datos todavía no son importantes.

→ Respuesta: **V**. Así está en las diapositivas del profe.
