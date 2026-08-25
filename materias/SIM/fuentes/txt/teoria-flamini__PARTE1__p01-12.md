# TeoriaSimulacion_Flamini_PARTE1_2022.pdf

_Transcripción de páginas 1 a 12 (apunte manuscrito de clase)._

---

--- pág. 1 ---

| | Simulacion (Teoria) | Hoja 1 |
|---|---|---|
| | Consultas: Martes 20:00 hs — 5to piso | |

**14/03**

Libro: "Simulacion"
Autor: S. Ross          } 2da. Edicion 1997
                          5ta Ed 2013 en Ingles  → 2019 en fotocop

Apunte (Fotocopias de dif. libros) prof Weitz, Darío → "Simulation modeling and Analysis"

Autores: A. Law y D. Kelton (2da Ed 1991) ← 8va Ed.

Regularizar → T.P. (individuales) 75% Aprob
- 1 o 2 parciales 60% aprob (recup y glob)
- entregar un TP integrador (fin de año) grupal (max 3)

Aprob Directa → aprobar el TP integrador
- regularizar ANTES del globalizador
- asistencia

— o — . — . — o — . — . — o —

"Simular" → replicar la realidad utilizando herramientas (o técnicas) computacionales.

CAP 1 - libro                    Simulacion es una <u>TÉCNICA</u> no una teoria.

                                 MUCHA EXPERIENCIA

**21/03**

Law - Kelton : <u>Cap 1</u> : Modelado Basico por simulacion

§ 1.1. Naturaleza de la Simulación.

---

--- pág. 2 ---

_[nota al margen superior]_: instalacion    proceso

Sistema → lo que estudiamos.
- para estudiarlo científicamente, hay que hacer suposiciones lo más realistas posibles (como hipótesis) y eso da origen a un MODELO del sistema.

Si el sist es simple podemos decir que el MODELO es un MODELO MATEMÁTICO, y al resolverlo obtenemos información exacta sobre el sistema, a esto se le llama SOLUCIÓN ANALÍTICA

A los modelos complejos (NO simples), se los estudia por simulacion.

En una simulación a traves de computadoras hacemos una evaluación numérica del modelo, y en vez de darme una solución exacta, de devuelve estimaciones de las características deseadas.

A que se puede aplicar la simulacion?
- diseño y anal de sist de fab.
- evaluacion de requisitos de hardware y software
- " de armas militares
- diseño de sist de comunicaciones.

* * * *

§ 1.2: Sistemas, modelos y simulacion.

_[flecha desde "Sistemas"]_ → conexion de entidades que actuan e interactuan entre sí para lograr un fin lógico.

Estado de un sistema → coleccion de variables necesarias para describirlo en un momento dado, en relacion con los objetivos en estudio.

Ej: hora llegada de los clientes llegan, cantidad cajeros, cantidad clientes

---

--- pág. 3 ---

| | Simulacion (Teoria) | Hoja 2 |
|---|---|---|

Clasificacion Sistemas : DISCRETOS VS CONTINUOS

V.E: variables de estado

| DISCRETOS | CONTINUOS |
|---|---|
| aquel para el cual las V.E. cambian en puntos separables de tiempo. | aquel para el cual las V.E cambian continuamente con respecto al tiempo (y avión volando) |

En la practica, pocos sistemas son completamente discretos o completamente continuos

Maneras de estudiar un sistema:
- Experimentando con el sistema real.
- Experimentando con un modelo del sistema; de ser así, hay dos alternativas:
  * modelo físico
  * modelo matemático:
    - solucion analítica.
    - simulacion.

Si es posible y rentable alterar fisicamente el sistema, sería lo más real.

Modelo → representan un sistema.

Modelo por simulacion → estaticos / dinamicos VS  y  determinísticos VS Estocásticos
                                                    Continuos VS DISCRETOS

estático → representacion de un sist. en un momento determinado, o bien un sist en el que el tiempo no interviene. Ej: modelos de montecarlo.

determinísticos → no contiene ningun componente probabilístico o aleatorio.
  ° deterministas.

---

--- pág. 4 ---

Estocástico → producen resultados que son en sí mismos aleatorios;

Los modelos que vamos a ver en la materia son:
- DINAMICOS
- ESTOCASTICOS
- DISCRETOS.

§ 1.3 Simulacion de Modelos a eventos discretos.

Se refiere al modelado de un sist _[amerita que evolucione]_ a lo largo del tiempo donde las VE cambian en <u>puntos separados en el tiempo</u>.

                          <u>aquellos en los que ocurre un evento</u>

(en terminos matematicos diremos que el sistema puede cambiar solo en numeros contables en el tiempo)

Estos puntos en el tiempo son aquellos en los que ocurre un evento donde un EVENTO = suceso instantaneo que cambia el estado del sistema.

Si bien la simulacion discreta de eventos discretos puede hacerse "a mano" debe hacerse en computadoras

Ejemplo: estimar la demora esperada en la cola de la barbería/peluquería

variable aleatoria → esperanza
                   → varianza
_[nota: estan relacionados]_

Variables de estado:
- Estado del servidor (inactivo u ocupado)
- Numero de Clientes en la cola
- hora de llegada de c/cliente

Un evento seria algo que modifique alguna de las 3 variables

demora en la cola = hora en que comienza a recibir servicio - hora llegada.

Hay 2 tipos de eventos para este sistema:
- la llegada del cliente  y → porq aumenta n° clientes y/o estado serv.
- la finalizacion del servicio → " disminuye " y/o " "

(Leer ultimo parrafo)

---

--- pág. 5 ---

| | Simulacion (Teoría) | Hoja 3 |
|---|---|---|

§ 1.3.1. Mecanismo de Avance en el tiempo

\* reloj de simulacion: su unidad de tiempo no se establece explícitamente

2 enfoques para avanzar el reloj de simulacion:
1) avance al proximo evento
2) avance a incremento fijo

usaremos el 1).

Ejemplo 1.2
- $t_i$ = tiempo _[hora]_ de llegada del i-esimo cliente $(t_0 = 0)$
- $A_i = t_i - t_{i-1}$ = tiempo transcurrido entre las llegadas de los clientes $i$ e $i-1$ (arribos consecutivos)
- $S_i$ = demora en el servidor con el cliente $i$
- $D_i$ = demora en la cola del cliente $i$
- $c_i = t_i + D_i + S_i$ = hora de salida del cliente $i$ ($i$-esimo cliente)
- $e_i$ = iésimo evento.

Figura 1.2

> [FIGURA pág. 5]: Línea de tiempo horizontal (eje "tiempo"). Sobre el eje, marcados de izquierda a derecha, los instantes $t_0=0$, $t_1$, $t_2$, $c_1$, $t_3$, $c_2$, seguidos de puntos suspensivos. Por encima de la línea se rotulan los eventos $e_1$ (sobre $t_1$) y luego, agrupados, $e_2$, $e_3$, $e_4$, $e_5$, ... sobre los instantes posteriores. Debajo del origen, $e_0$ con la aclaración "momento en el que abre el lugar". Por debajo del eje, arcos que miden los tiempos entre arribos: $A_1$ entre $t_0$ y $t_1$, $A_2$ entre $t_1$ y $t_2$, $A_3$ entre $t_2$ y $t_3$, $A_4$ a continuación. Más abajo, arcos que miden los tiempos de servicio: $S_1$ (que arranca en $t_1$ y termina en $c_1$), $S_2$ (hasta $c_2$) y $S_3$. Ilustra la correspondencia entre arribos ($t_i$), salidas ($c_i$), tiempos entre arribos ($A_i$) y tiempos de servicio ($S_i$) sobre el eje temporal de la simulación.

---

--- pág. 6 ---

§ 1.3.2 Componentes y Organización de un modelo de simulación a eventos discretos.

1) modelo de un Sist de espera  § 1.4
2)   "   de un sist de inventario § 1.5

- **Estado del sistema**: Coleccion de variables de estado necesarias para describir el sistema en un momento determinado
- **Reloj de Simulacion**: variable que da el valor actual de la hora de la simulacion.
- **Lista de eventos**: lista que contiene la proxima vez que ocurrira un evento.
- **Contadores Estadisticos**: variables utilizadas para almacenar informacion estadistica para el desempeño del sistema.
- **Rutina de inicializacion**: un subprograma para inicializar el modelo de simulacion en el momento cero
- **Rutina de avance en el tiempo**: subprograma que determina el siguiente evento de la Lista de eventos y avanza el reloj de simulacion a la hora que ocurre el evento.
- **Rutina de eventos**: subprograma que actualiza el estado del sistema cuando ocurre un tipo particular de evento. (hay una rutina por c/tipo de evento).
- **Biblioteca de rutinas**: grupo de subprogramas usados para generar observaciones
- **Generador de informes**: subprograma que calcula las estimaciones a partir de los contadores estadisticos.
- **Programa Principal**: subprog que invoca a la rutina de avance en el tiempo para determinar el prox evento

---

--- pág. 7 ---

| | Simulacion (Teoria) | Hoja 4 |
|---|---|---|

Figura 1.3

> [FIGURA pág. 7]: Diagrama de flujo de la organización de un modelo de simulación a eventos discretos.
>
> - Nodo de arranque ovalado: **Inicio**, que baja al bloque **Prog Principal**.
> - **Programa Principal** (caja con tres pasos numerados): "0 - Invoca la rutina de inicializacion", "1 - Invoca la rutina de avance en el tiempo", "2 - Invoca la rutina del eventos i".
> - Flecha (0) desde el paso 0 hacia la izquierda, al bloque **Rutina de Inicializacion**: "1 - Pone en 0 el reloj de simulacion.", "2 - Inicializa el estado del sist y los contadores estadisticos", "3 - Inicializa la lista de eventos". Vuelve al Programa Principal.
> - Flecha (1) desde el paso 1 hacia la derecha, al bloque **Rutina de avance en el tiempo**: "1 - Se determina el sig tipo de evento i", "2 - Se avanza el reloj de simulacion". Devuelve el tipo de evento $i$ al Programa Principal.
> - Flecha (2) desde el paso 2 hacia abajo, al bloque **Rutina evento i**: "1 - Actualizar el estado del sistema", "2 - Actualiza los contadores estadisticos", "3 - Genera los eventos futuros y los agrega a la lista de eventos".
> - A la derecha de ese bloque, con flechas de ida y vuelta, el bloque **Biblioteca de rutinas**: "Genera variables aleatorias".
> - Debajo, rombo de decisión: "¿Fin simulacion?". La salida **NO** vuelve (por la derecha) a la Rutina de avance en el tiempo / Programa Principal; la salida afirmativa baja al bloque **Generador de informes**: "1 - Calcula estimaciones de interes", "2 - Escribe el informe".
> - Nodo ovalado final: **Fin**.

---

--- pág. 8 ---

**4/04**

§ 1.4. Simulación de un Sistema formado por una Cola con un solo servidor

(por ej el de la pelu con un solo peluquero)

§ 1.4.1 Planteo del Problema

> [FIGURA pág. 8]: Esquema/leyenda del sistema de cola con un servidor. Se dibujan y rotulan los símbolos: **Servidor** = un cuadrado; **cliente en Servicio** = un círculo; **clientes en cola** = tres círculos apilados verticalmente; **cliente que está arribando** = un círculo con una flecha que apunta hacia el sistema (entrando); **cliente que se retira** = un círculo con una flecha que apunta hacia afuera (saliendo).

Supuestos o hipotesis:
- Los tiempos entre ambos $A_1$, $A_2$, ... son variables aleatorias independientes y distribuidas de manera identica. (VAII)  $(A_i = t_i - t_{i-1})$
- Un cliente que llega y encuentra al servidor desocupado/inactivo, entra y empieza a ser atendido en ese momento. ($S_1$, $S_2$, ... son VAII)
  $t = 0$ → servidor INACTIVO $t_1 > 0$.
- Cuando llega un cliente y el servidor esta ocupado, comienza la cola, y son atendidos (los clientes) es FIFO (PEPS)
- Cuando el n-esimo cliente completo la cola o cuando haya pasado un tiempo $T$ _[prefijado de antemano]_, se finaliza la simulacion.

medidas de Desempeño o Rendimiento del sistema $(d(n), q(n)$ y $u(n)$ son V.A)

_[nota: V.A (2 parametros) → esperanza, varianza]_

3 medidas

→ demora promedio esperada en la cola de los n clientes que completaron su espera. $(d(n))$

$$\hat{d}(n) = \frac{\sum_{i=1}^{n} D_i}{n}$$

($D$ = tiempo en la cola)

→ numero promedio de clientes en cola en promedio _[en el momento "t"]_

$$\hat{q}(n) = \sum_{i=0}^{\infty} i \, p_i$$

_[nota sobre el $\infty$: mayor valor de $i$ en la simulacion, no es realmente $\infty$]_

---

--- pág. 9 ---

| | Simulacion (Teoría) | Hoja 5 |
|---|---|---|

$0 \le t \le T(n)$        $Q(t)$ = n° de clientes en cola en el momento $t$

$p_i$ = proporcion de tiempo total en que hay $i$ clientes en cola $(i = 0, 1, 2, ...)$

> [FIGURA pág. 9]: Gráfico escalonado de $Q(t)$ (eje vertical, marcado con los valores 1 y 2) contra $t$ (eje horizontal, con marcas en $t_1$, $t_2$, $t_3$, $c_1$). La curva es una función escalonada: vale 0 hasta $t_2$, salta a 1, sube a 2 y vuelve a bajar, con los extremos de cada tramo dibujados con círculo abierto a la derecha y punto lleno a la izquierda (continuidad por derecha). Anotación al costado: "grafica seccionalmente constante". Ilustra que $Q(t)$ es constante a tramos entre eventos.

$T_i$ = tiempo en que hay $i$ clientes en cola _[con $i = 1$]_

$$T_0 + T_1 + T_2 + \dots = T(n)$$

$$\hat{p}_i = \frac{T_i}{T(n)}$$

$$q(n) = \sum_{i=0}^{\infty} i \cdot \hat{p}_i = \frac{\left(\sum_{i=0}^{\infty} i \cdot T_i\right)}{T(n)}$$

_[llaves: la primera expresión es (1.1) pag 15; la segunda es (1.2) pag 16]_
_[nota: "sale de la sumatoria por ser una cte"]_

Ejemplo pag 16

| i | t_i | c_i |
|---|---|---|
| 0 | 0 | |
| 1 | 0,4 | 2,4 |
| 2 | 1,6 | 3,1 |
| 3 | 2,1 | 3,3 |
| 4 | 3,8 | 4,9 |
| 5 | 4,0 | 7,6 |
| 6 | 5,6 | |
| 7 | 5,8 | |
| 9 | 7,2 | |

_[$i$ = n° de clientes]_    Fin de la sim. $n = 6$

En este ejemplo $T(n) = T(6) = 8,6$

---

--- pág. 10 ---

> [FIGURA pág. 10]: Gráfico completo de $Q(t)$ para el ejemplo. Eje vertical $Q(t)$ con marcas en 1, 2, 3, 4, 5; eje horizontal $t$ con marcas y rótulos: $t=0$; 0,4 ($t_1$); 1; 1,6 ($t_2$); 2; 2,1 ($t_3$); 2,4 ($c_1$); 3; 3,1 ($c_2$); 3,3 ($c_3$); 3,8 ($t_4$); 4 ($t_5$); 4,9 ($c_4$); 5. La función escalonada vale 0 hasta 1,6; sube a 1 entre 1,6 y 2,1; sube a 2 entre 2,1 y 2,4 (tramo sombreado más oscuro); baja a 1 entre 2,4 y 3,1; vale 0 entre 3,1 y 4; vuelve a valer 1 entre 4 y 4,9; y 0 después de 4,9. Las áreas bajo los escalones aparecen rayadas (son las que se integran para calcular $\hat q(n)$).

$t_i$ y $c_i$ son EVENTOS enumerados en orden cronologico

$$T_0 = (t_2 - 0) + (t_5 - c_2) + (5 - c_4) = (1,6-0) + (4-3,1) + (5-4,9) =$$

$$T_1 = (t_3 - t_2) + (c_2 - c_1) + (c_4 - t_5) = (2,1-1,6) + (3,1-2,4) + (4,9-4) =$$

$$T_2 = (c_1 - t_3) = 2,4 - 2,1 =$$

$$\vdots$$

$$\therefore \; q(n) = \frac{0 \cdot T_0 + 1 \cdot T_1 + 2 \cdot T_2 + 3 \cdot T_3 \dots}{8,6}$$

_[nota: $i \cdot T_i$ → son areas de rectangulos.]_

$$\hat{q}(n) = \frac{\int_0^{T(n)} Q(t) \cdot dt}{T(n)} \qquad (1.4)$$

→ $u(n)$ = proporcion de tiempo que el servidor está ocupado

$$B(t) = \begin{cases} 1 & \text{si el servidor esta ocupado en el tiempo } t \\ 0 & \text{si el servidor esta "vacio" en el tiempo } t \end{cases}$$

---

--- pág. 11 ---

| | Simulacion (Teoría) | Hoja 6 |
|---|---|---|

> [FIGURA pág. 11]: Gráfico de $B(t)$ ("con el mismo ejemplo"). Eje vertical $B(t)$ con la marca 1; eje horizontal $t$ con marcas en $t_1$, ... , $c_3$, $t_4$, ... La función vale 1 (área rayada por debajo) desde $t_1$ hasta $c_3$, cae a 0 entre $c_3$ y $t_4$, y vuelve a valer 1 a partir de $t_4$. Los saltos se dibujan con círculo abierto/punto lleno. Ilustra la proporción de tiempo en que el servidor está ocupado.

$$\hat{u}(n) = \frac{(c_3 - t_1) + (T(n) - t_4)}{T(n)} = \frac{(3,3 - 0,4) + (8,6 - 3,8)}{8,6}$$

$$\hat{u}(n) = \frac{\int_0^{T(n)} B(t)\,dt}{T(n)} \qquad \text{(terminar de leer)}$$

§ 1.4.2 Explicacion Intuitiva (pag 19)
(prueba de escritorio)

<u>Proceso Estocastico de Poisson</u>

→ establece hipotesis cuando un proceso aleatorio cumple ciertas condiciones

Los $t$ de llegada y de salida de los clientes cumplen estas condiciones

$$A_i = t_i - t_{i-1} \; \longrightarrow \; \text{V.A. exponencial} \; \longrightarrow \; \text{Dist de exp}$$

_[llave bajo $A_i$: tiempos entre arribos.]_

---

--- pág. 12 ---

$S_i$
↓
tiempos de servicio

| i | A | S |
|---|---|---|
| 0 | | |
| 1 | $t_1 - 0,4$ | $2,4 - 0,4$ |
| 2 | $1,6 - 0,4$ | $3,1 - 2,4$ |
| ⋮ | ⋮ | ⋮ |

Seccion 1.4.2  lista numeros: $A_i$, $S_i$

| i | A_i | S_i |
|---|---|---|
| 0 | | |
| 1 | 0,4 | 2,0 |
| 2 | 1,2 | 0,7 |
| 3 | 0,5 | 0,2 |
| 4 | 1,7 | 1,1 |
| 5 | 0,2 | 3,7 |
| 6 | 1,6 | 0,6 |
| 7 | 0,2 | ⋮ |
| 8 | 1,4 | |
| 9 | 2,0 | |

_[anotación al margen: "pag 20"]_

Representacion de la computadora   _[en orden cronologico]_

> [FIGURA pág. 12]: Esquema de cómo la computadora representa el modelo. Tres bloques en fila:
> - **Estado del sist**: cuatro casilleros; los primeros dos rotulados $B(t)$ y $Q(t)$, luego una pila de casilleros rotulada $t_i$, y un casillero suelto. Las flechas debajo indican: $B(t)$ → "estado del servidor"; $Q(t)$ → "estado de la cola"; $t_i$ → "tiempos de arribo"; el último → "tiempo del ultimo evento".
> - **Reloj Simulacion**: un casillero único.
> - **Lista de eventos** ("en orden cronologico"): dos casilleros rotulados A (arribos) y P (partidas).
> - Debajo, **Contadores estadisticos**: cuatro casilleros, con flechas que los identifican como "demora total", "cantidad de clientes / tiempo en cola", "Area debajo de $B(t)$" y "Area debajo de $Q(t)$".
>
> Ilustra las estructuras de datos del programa de simulación a eventos discretos del sistema de cola con un servidor.
