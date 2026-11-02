# Podcast SIM 2 de 8 — El motor de eventos discretos y la cola de un servidor

Fuente para un episodio de podcast de estudio. Materia: Simulación (UTN, Ingeniería en
Sistemas, 4.º año). Sirve para el primer parcial, el sábado 7 de noviembre de 2026: integrado
teórico-práctico y probablemente multiple choice. Las respuestas del banco son la clave revisada
por nosotros, no la corrección oficial de la cátedra.

## Indicaciones para el episodio

Cómo avanza el reloj (incremento fijo contra próximo evento), las piezas del motor de un simulador DES y el modelo de cola simple de Law: los dos eventos, las variables de estado y las tres medidas d(n), q(n) y u(n). Explicar la traza con palabras, sin dictar la tabla número por número.

## Contenido principal

### 3. Simulación a eventos discretos (DES)

*Fuentes: Law §1.3 (Weitz) y diapositivas de la clase 2.*

En una DES las variables de estado cambian **solo en un número contable de instantes**, y en cada uno de esos instantes ocurre un evento. Entre dos eventos no pasa nada: el estado se mantiene constante. Por eso **el reloj no necesita avanzar de a poco**: puede **saltar** de un evento al siguiente.

#### 3.1 Dos formas de avanzar el reloj

| | **Próximo evento** (*next-event*) | **Incremento fijo** (*fixed-increment*) |
|---|---|---|
| Cómo avanza | **Salta** al instante del evento más próximo | Avanza de a $\Delta t$ y en cada paso revisa qué pasó |
| Períodos de inactividad | **Los salta**. Es la ventaja principal: ahorra cómputo | Los recorre igual |
| Error | Ninguno por discretizar | Los eventos se procesan **al final** del intervalo, lo que introduce error y obliga a desempatar |
| Uso | Casi todo el software comercial | Datos que existen solo por período (por ejemplo, anuales) |

> **Ojo:** la ventaja del *next-event* **no** es ser "más fácil de programar" ni "más preciso en los cálculos". Es **saltear la inactividad**.

#### 3.2 El motor de cualquier simulador DES

Los componentes que se toman de memoria:

- **Estado del sistema.**
- **Reloj.**
- **Lista de eventos**: el próximo instante de cada tipo de evento.
- **Contadores estadísticos.**
- **Rutina de inicialización**: arranca todo en $t = 0$.
- **Rutina de temporización**: elige el próximo evento y salta el reloj.
- **Rutinas de evento**: una por tipo de evento.
- **Rutinas de librería**: generan las variables aleatorias.
- **Generador de reportes.**
- **Programa principal**: coordina el ciclo y revisa si hay que terminar.

### 4. Modelo de cola con un servidor

*Fuentes: Law §1.4 (Weitz), diapositivas "Cola simple e inventarios" y "Simulación de eventos discretos: traza paso a paso".*

#### 4.1 El modelo

Los clientes llegan con tiempos entre arribos $A_1, A_2, \dots$ i.i.d. Si el servidor está libre los atiende enseguida; si no, hacen cola FIFO. Cada servicio dura $S_1, S_2, \dots$ i.i.d. La simulación **termina cuando $n$ clientes completaron su demora** en cola.

- **Variables de estado**:
  - el estado del servidor (libre u ocupado);
  - el número de clientes en cola;
  - el tiempo de arribo de cada cliente que espera, que hace falta para calcular su demora.
- **Eventos: solo dos**, el **arribo** y la **partida** (fin de servicio).
  - "Poner el servidor ocupado" **no es un evento**: es un **cambio de estado** que producen esos dos eventos.
  - "Inicio" tampoco es un evento: es la rutina de inicialización.

**Qué programa cada evento:**

- **Arribo**:
  - siempre programa el próximo arribo;
  - si el servidor estaba libre, además programa la partida de ese cliente.
- **Partida**:
  - si queda gente en cola, programa la partida del siguiente;
  - si no, deja el servidor libre.

#### 4.2 Las tres medidas de rendimiento

| Medida | Qué mide | Fórmula | Promedia sobre |
|---|---|---|---|
| **$d(n)$** | demora promedio **en cola** | $\hat d(n) = \dfrac{\sum_{i=1}^{n} D_i}{n}$ | **clientes** |
| **$q(n)$** | número promedio de clientes **en cola** | $\hat q(n) = \dfrac{\int_0^{T(n)} Q(t)\,dt}{T(n)}$ | **tiempo** |
| **$u(n)$** | utilización del servidor | $\hat u(n) = \dfrac{\int_0^{T(n)} B(t)\,dt}{T(n)}$ | **tiempo** |

Las tres son medidas **muestrales**: una corrida es una muestra de tamaño $n$.

- **La demora es el tiempo en cola y no incluye el servicio.** Los $D_i = 0$ también se promedian.
- $q(n)$ es el **área bajo $Q(t)$** dividida por el tiempo total.
- $u(n)$ es la **proporción del tiempo** en que el servidor estuvo ocupado ($B(t) = 1$).

> **Ojo:** las tres medidas de Law son demora **en cola**, número **en cola** y utilización. "Tiempo promedio de servicio" es un **dato de entrada**, y "número en el **sistema**" es otra medida. Las dos son trampas del 2025.

#### 4.3 La traza de Law, dibujada

Datos de la traza: $A = 0{,}4;\ 1{,}2;\ 0{,}5;\ 1{,}7;\ 0{,}2;\ 1{,}6;\ 0{,}2;\ 1{,}4$ y $S = 2{,}0;\ 0{,}7;\ 0{,}2;\ 1{,}1;\ 3{,}7;\ 0{,}6$, con $n = 6$.

Cómo leer la figura:

- **$d(6)$ se lee arriba**: es el promedio de los seis tramos naranjas, $5{,}7/6 = 0{,}95$.
- **$q(6)$ se lee en el medio**: es el área naranja (9,9) dividida por la duración de la corrida (8,6), y da 1,15.
- **$u(6)$ se lee abajo**: el servidor estuvo ocupado 7,7 de los 8,6 minutos, o sea 0,90. Los únicos huecos son antes del primer arribo y entre 3,3 y 3,8.

La corrida termina en $T(6) = 8{,}6$, cuando el cliente 6 **empieza** su servicio: en ese momento se completa la sexta demora. **No** termina cuando sale el sexto cliente.

#### 4.4 La salida de la simulación

Law simuló 1000 clientes con media entre arribos de 1 minuto y media de servicio de 0,5 minutos. Obtuvo:

- demora promedio en cola: 0,430 min;
- número promedio en cola: 0,418;
- utilización: 0,460;
- duración de la corrida: 1027,9 min.

Son **estimaciones de una sola corrida**: con otros números aleatorios saldrían otros valores.

#### 4.5 La plantilla para la traza a mano

Las diapositivas de clase usan una plantilla con cinco bloques. Si toman una traza, es este formato:

| Bloque | Qué se anota |
|---|---|
| **Estado del sistema** | estado del servidor (1/0), cantidad en cola, tiempos de arribo de los que esperan |
| **Reloj** | el instante actual |
| **Lista de eventos** | próximo arribo (A) y próxima partida (D). Con el servidor libre, D vale $\infty$ |
| **Contadores estadísticos** | cantidad de demoras completadas, demora total, área bajo $Q(t)$, área bajo $B(t)$ |
| **Números generados** | las listas de $A_i$ y $S_i$ que se van consumiendo |

En cada evento se hacen siempre los mismos cuatro pasos:

1. Se **acumulan las áreas con el valor viejo**: `área += (reloj − tiempo del último evento) × valor anterior`.
2. Se actualiza el estado.
3. Se programan los eventos futuros.
4. Se salta al próximo evento.

## Ampliación

### Las tres medidas de la cola **simulada**

> Esto es de la Unidad 3 (simulación), pero cae seguido en las mismas preguntas que colas, así que
> va acá para tenerlo junto. Preguntado en 2022 P3, 2025 (1.2 y 2.13) y 2019-Weitz.

Sobre una corrida que termina cuando $n$ clientes completaron su demora, con $T(n)$ el tiempo total:

| Medida | Fórmula | Tipo de promedio |
|---|---|---|
| $\hat{d}(n)$ — **demora promedio** | $\dfrac{\sum_{i=1}^{n} D_i}{n}$ | **Sobre clientes** |
| $\hat{q}(n)$ — **nº promedio en cola** | $\dfrac{\int_0^{T(n)} Q(t)\,dt}{T(n)} = \dfrac{\sum_i i\,T_i}{T(n)}$ | **Sobre tiempo** |
| $\hat{u}(n)$ — **utilización** | $\dfrac{\int_0^{T(n)} B(t)\,dt}{T(n)}$ | **Sobre tiempo** |

**La distinción conceptual central**: $d(n)$ promedia **sobre clientes** (divide por $n$); $q(n)$ y
$u(n)$ promedian **sobre tiempo** (dividen por $T(n)$). Es la trampa clásica.

Detalles que se preguntan:
- La **demora no incluye el tiempo de servicio** — es solo lo que espera en la fila.
- **No se excluyen** los $D_i = 0$ (clientes que llegan y encuentran el sistema vacío); incluirlos refleja el buen desempeño del sistema.
- $B(t) = 1$ si el servidor está ocupado en $t$, 0 si está libre.
- $\sum_i i\,T_i$ **es el área bajo la curva $Q(t)$** — por eso la versión discreta y la integral son equivalentes.

## Preguntas de parcial y de práctica sobre este tema

**1.2** (parcial 2025) **En la cola de un servidor, ¿cuáles son las tres medidas de rendimiento principales que se estiman?**
A) tiempo promedio de servicio, nº promedio en el sistema, utilización · B) retraso promedio en cola, nº promedio en cola, proporción de tiempo que el servidor está ocupado · C) llegada/salida/longitud · D) solo retraso y utilización · E) A y B

✅ **B**, sin dudas. Son las tres de Law: $d(n)$ demora promedio en cola, $q(n)$ número promedio en cola y $u(n)$ utilización. **A es la trampa**: mezcla el tiempo de servicio, que es un dato de entrada, y el número en el **sistema**, cuando Law mide en la **cola**.
*Unidad 3, "Las tres medidas de rendimiento".*

**1.9** (parcial 2025) **Principal ventaja del next-event time advance**
A) más precisión · B) salta los períodos de inactividad y ahorra cómputo · C) más fácil de programar · D) resultados más estables · E) B y C

✅ **B.** Law no dice en ningún lado que sea "más fácil de programar". Lo que dice es que lo usa casi todo el software comercial, que no es lo mismo. Con "principal ventaja" la respuesta es una sola.
*Unidad 2, "Mecanismos de avance del tiempo".*

**1.11** (parcial 2025) **En el next-event, ¿qué pasa con los períodos de inactividad?**
✅ **B**: se saltan y el reloj va directo al próximo evento. A describe el **incremento fijo**.

**2.11** (parcial 2025) **Los modelos de cola simple e inventario de los TP de clase…**
- A) son modelos simples que pueden simularse y además tienen solución analítica → ✅
- B) solo pueden simularse si se tiene la solución analítica → ❌
- C) la solución analítica puede compararse con las respuestas de la simulación → ✅. Es lo que hicieron en el TP 3: M/M/1 simulado contra teórico.
- D) las respuestas de las simulaciones suelen ser parecidas a la solución analítica → ✅

◐ **Clave: A, C y D.** El alumno marcó solo A. En selección múltiple, **marcar de menos también resta**. La única duda es si la cátedra considera "analítico" al inventario (s, S); para la cola M/M/1 no hay discusión.

**2.12** (parcial 2025) **En DES, los eventos de la cola simple son…**
A) arribo · B) partida · C) inicio · D) finalización · E) poner el servidor ocupado/desocupado

✅ **A y B.** E **no es un evento**: es un cambio de **estado** que producen el arribo y la partida.
C) La inicialización es una rutina, no un evento.
D) Solo existiría si la corrida terminara a tiempo fijo, con un evento "fin de simulación" como tercer tipo. En el modelo de Law la cola simple corta por $n$ demoras y tiene dos tipos de evento.
*Unidad 3, "Variables de estado y eventos".*

**2.13** (parcial 2025) **Las medidas de rendimiento más importantes de la cola simple son…**
A) tiempo de espera "en el servidor" · B) tiempo de arribo · C) veces que el cliente pasó por el servidor · D) utilización del servidor

◐ **A y D.** A está mal redactada, pero apunta a la **demora en cola** $d(n)$. D es $u(n)$. B es un **dato de entrada**, no una medida, y C no tiene sentido en una cola simple. La tercera medida de Law, el **número promedio en cola** $q(n)$, no está entre las opciones.

**P18** (práctica, no oficial) V o F: el método de incremento fijo de tiempo omite los períodos de inactividad.

→ Respuesta: **F**. Esa ventaja es del **próximo evento**.

**P38** (práctica, no oficial) En la traza de Law de la cola simple ($n=6$), la corrida termina: A) cuando sale el sexto cliente · B) cuando el sexto cliente **empieza** su servicio, porque ahí se completa la sexta demora · C) a tiempo fijo · D) cuando se vacía la cola · E) A y D

→ Respuesta: **B**. $T(6)=8{,}6$.

**P40** (práctica, no oficial) V o F: la simulación a eventos discretos es estocástica porque los tiempos de servicio y de llegada suelen ser aleatorios, y por eso hace falta correrla un tiempo suficiente o varias réplicas para obtener resultados con sentido.

→ Respuesta: **V**. Texto de *AnyLogic in 3 Days* sobre DES.
