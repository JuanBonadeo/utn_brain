# TPA — Wiki

> Tecnologías para la Automatización · UTN-ISI · 4° año
> Migrado desde el Proyecto de Claude (archivos subidos + conversaciones históricas).

## Índice

1. Introducción a los Sistemas de Control
2. Diagramas de Bloques y Función de Transferencia
3. Modelo Matemático — Transformada de Laplace
4. Sistemas de Primer Orden
5. Sistemas de Segundo Orden
6. Error en Estado Estable
7. Controladores (P, PI, PD, PID)
8. Estabilidad (incluye Lugar Geométrico de Raíces — LGR)
9. Robótica (bonus — presente en el material de cátedra aunque no figura en el temario de 8 unidades)

---

## Unidad 1 — Introducción a los Sistemas de Control

### Conceptos clave

- **Sistema de control**: controla una o más variables de salida por medio de una o más variables de entrada. Actúa sobre una **planta** (objeto físico tangible) o **proceso** (operación intangible, química/económica/biológica).
- **Perturbación**: señal aleatoria/arbitraria que afecta adversamente la salida.
- **Respuesta transitoria** vs **respuesta en estado estacionario**: la salida no cambia instantáneamente (transitorio); luego se aproxima a la respuesta comandada (estacionario). La diferencia final es el **error en estado estacionario**.
- **Lazo abierto**: no mide ni corrige la salida; no compensa perturbaciones. Más simple y barato.
- **Lazo cerrado (realimentado)**: mide la salida (transductor de salida/sensor), la compara con la entrada en un punto suma, y genera una **señal de actuación** (= error, si los transductores tienen ganancia unitaria). Compensa perturbaciones; más preciso pero más complejo/caro.
- **Servo vs Regulador**:
  - **Servo**: la entrada (referencia) cambia permanentemente; se asume que no hay perturbación. La salida debe *seguir* la referencia. Ej.: brazo robótico, avión.
  - **Regulador**: la entrada es fija; la única "entrada" relevante es la perturbación. El objetivo es *rechazar* la perturbación. Ej.: regulador de temperatura/humedad.
- **Feedback negativo vs positivo**: se trabaja con feedback negativo (la variable medida se resta).
- **Entradas de prueba estándar**: escalón (comando constante, respuesta transitoria y estacionaria bien visibles), rampa (señal creciente linealmente, da info del error en estado estacionario), parábola (ídem, error en estado estacionario), senoidal (para identificación de sistemas).
- **Objetivos del análisis y diseño**: respuesta transitoria adecuada, error en estado estacionario aceptable, estabilidad.
- **Proceso de diseño** (6 pasos): requerimientos → diagrama funcional → diagrama esquemático → modelo matemático (función de transferencia, vía Laplace) → reducción del diagrama de bloques → análisis y diseño.

### Desarrollo

La materia arranca separando **lazo abierto** de **lazo cerrado** según si el sistema puede o no corregir perturbaciones comparando la salida real con la deseada. Sobre esa base se monta la distinción **servo/regulador**, que no es sobre la topología del lazo sino sobre *qué está cambiando*: en servo cambia la referencia (se sigue), en regulador cambia la perturbación (se rechaza) mientras la referencia permanece fija.

Esta distinción es clave porque determina cómo se arma el diagrama de bloques (dónde entra la perturbación) y qué error en estado estable importa evaluar (ver Unidad 6).

**Cómo justificar servo vs regulador en un enunciado** (patrón práctico): buscar palabras clave. Si el enunciado dice que una variable "debe **seguir**" un comando cambiante → servo. Si dice que algo "debe **mantenerse constante**" ante variaciones de carga/perturbaciones → regulador.

### Ejercicios resueltos tipo

**Clasificación servo vs regulador — reactor químico.** Enunciado: la concentración de un reactor debe mantenerse constante pese a variaciones de carga. Se identificó como **regulador** (referencia fija, hay perturbaciones) porque el enunciado usa la palabra "constante" frente a variaciones. La perturbación se dibuja entrando *dentro* del lazo, entre el controlador y la planta:

```
        Perturbación D(s)
              ↓
R(s) →⊗→ Gc →⊗→ Gp → C(s)
      ↑              |
      └──────H=1─────┘
```
con $G_p = \dfrac{1}{s(2s+1)}$, $H=1$ (no especificado, se asume unitaria).

### Dudas / pendientes

_(sin datos adicionales sin cerrar en el historial para esta unidad)_

### Fuentes

- `TDC_ResumenTeoría_Opción1.pdf` (Capítulos: Introducción, Cap. 9 "El Sistema de Control")
- Conversación: *Clasificación de ejercicio servo versus regulador*

---

## Unidad 2 — Diagramas de Bloques y Función de Transferencia

### Conceptos clave

- **Función de transferencia**: $G(s) = \dfrac{Y(s)}{X(s)} = \dfrac{\mathcal{L}\{\text{salida}\}}{\mathcal{L}\{\text{entrada}\}}$, asumiendo condiciones iniciales cero. También: $G(s) = \mathcal{L}\{g(t)\}$ (transformada de la respuesta al impulso).
- Es una **propiedad del sistema**, independiente de la magnitud/naturaleza de la entrada. No da información de la estructura física interna (sistemas físicamente distintos pueden compartir función de transferencia).
- Limitada a sistemas **LTI** (lineales e invariantes en el tiempo) **SISO** (una entrada, una salida). Se puede obtener experimentalmente (identificación de sistemas).
- **Principio de superposición**: si $X(s) = a_1X_1(s) + a_2X_2(s)$ entonces $Y(s) = a_1Y_1(s) + a_2Y_2(s)$.
- **Álgebra de bloques / reducción**: regla general para un tramo entre dos puntos X e Y del diagrama:
$$\frac{X}{Y} = \frac{\pi_f}{1+\pi_i}$$
donde $\pi_f$ = producto de todas las funciones de transferencia entre X e Y, y $\pi_i$ = producto de todas las funciones de transferencia que están dentro del lazo.
- **Función de transferencia de lazo cerrado — problema servo**: con $C = G\varepsilon$, $B=HC$, $\varepsilon = R-B$:
$$\frac{C}{R} = \frac{G}{1+GH}$$
- **Problema regulador** (perturbación $U$ entrando entre controlador y planta, con $G = G_cG_1$):
$$C = R\cdot\frac{G_1G_2}{1+GH} + U\cdot\frac{G_2}{1+GH}$$
(mismo denominador para ambas componentes). Con solo perturbación ($R=0$):
$$\frac{C}{U} = \frac{G_2}{1+GH}$$
- **Función de transferencia de lazo abierto**: $GH = G_1G_2H(s) = G$ (notación usada en estabilidad).

### Desarrollo

El diagrama de bloques es el paso intermedio entre el modelo físico y la función de transferencia algebraica. La reducción de bloques se apoya en identificar, para cualquier par de nodos, qué camino "directo" (feedforward, $\pi_f$) los conecta y qué lazo cerrado ($\pi_i$) rodea ese camino — de ahí la regla $\pi_f/(1+\pi_i)$, que es una generalización de la fórmula estándar $G/(1+GH)$.

La diferencia entre **servo** y **regulador** (Unidad 1) se traduce acá en *dónde* se dibuja la entrada de la perturbación en el diagrama: en el problema regulador, la perturbación entra en un punto suma **entre el controlador y la planta**, no en el punto suma de entrada. Por eso la función de transferencia de lazo cerrado tiene dos componentes (una para R, otra para U) que comparten el mismo denominador $1+GH$ — el denominador (la "función característica") depende solo de la topología del lazo, no de por dónde entra la señal.

### Ejercicios resueltos tipo

Ver diagrama de bloques del reactor químico en Unidad 1 (regulador, perturbación entre $G_c$ y $G_p$).

### Dudas / pendientes

_(sin datos en el historial — no se registraron dudas puntuales de reducción de bloques)_

### Fuentes

- `TDC_ResumenTeoría_Opción1.pdf` (Cap. 3 "Formas de representación del modelo matemático", Cap. 12 "Función de transferencia a lazo cerrado")
- `Diagrama_de_bloques_250612_103153.pdf`
- Conversación: *Clasificación de ejercicio servo versus regulador*

---

## Unidad 3 — Modelo Matemático — Transformada de Laplace

### Conceptos clave

- Modelo matemático base: ecuación diferencial ordinaria lineal e invariante en el tiempo (LTI).
- Definición: $f(s) = \int_0^\infty f(t)e^{-st}\,dt = \mathcal{L}\{f(t)\}$.
- La transformada de Laplace es **lineal**: $\mathcal{L}\{af_1(t)+bf_2(t)\} = a\mathcal{L}\{f_1(t)\}+b\mathcal{L}\{f_2(t)\}$.
- No da información de $f(t)$ para $t<0$.
- **Transformadas elementales**:
  - Escalón: $\mathcal{L}\{Au(t)\} = A/s$
  - Exponencial: $\mathcal{L}\{Au(t)e^{-at}\} = A/(a+s)$
  - Rampa: $\mathcal{L}\{Atu(t)\} = A/s^2$
- **Teorema del Valor Final (T.V.F.)**: $\lim_{t\to\infty} f(t) = \lim_{s\to0} sf(s)$, válido si $sf(s)$ no diverge para ningún $s$ con $\text{Re}(s)\ge 0$.
- **Teorema del Valor Inicial**: $\lim_{t\to0} f(t) = \lim_{s\to\infty} sf(s)$.
- **Traslación de una transformada**: $\mathcal{L}\{e^{-at}f(t)\} = f(s+a)$.
- **Traslación de una función** (retardo): $\mathcal{L}\{f(t-t_0)\} = e^{-st_0}f(s)$, para $f(t)=0\;\forall t<0$.

### Desarrollo

Laplace es la herramienta que convierte ecuaciones diferenciales en ecuaciones algebraicas, permitiendo definir la función de transferencia (Unidad 2). El **teorema del valor final** es la herramienta central para calcular el error en estado estable (Unidad 6): en vez de resolver $y(t)$ completo y evaluar el límite, se opera directamente sobre $sY(s)$ cuando $s\to0$ — siempre que el sistema sea estable (condición implícita del teorema).

### Ejercicios resueltos tipo

_(sin datos en el historial — no se resolvieron ejercicios puramente de transformada en las conversaciones registradas; el uso del T.V.F. aparece aplicado indirectamente en Unidad 6)_

### Dudas / pendientes

_(sin datos en el historial)_

### Fuentes

- `TDC_ResumenTeoría_Opción1.pdf` (Cap. 2 "Transformada de Laplace", Cap. 4 "Otras propiedades de las transformadas")

---

## Unidad 4 — Sistemas de Primer Orden

### Conceptos clave

- **Variables de desviación**: $Y = y-y_s$, $X = x-x_s$ (valor en el tiempo $t$ menos valor en estado estacionario).
- **Función de transferencia**: a partir de $X-Y=\tau\dfrac{dy}{dt}$:
$$G(s) = \frac{Y(s)}{X(s)} = \frac{1}{\tau s+1}$$
donde $\tau$ (constante de tiempo, unidad de tiempo) es el único parámetro variable.
- **Respuesta al escalón** ($X(t)=Au(t)$): $Y(t) = A(1-e^{-t/\tau})$ para $t\ge0$.
  - Medidas: tiempo de subida $t_r = 2.2\tau$ (10%→90%); tiempo de asentamiento $t_s = 4\tau$ (banda ±2%).
  - A $t=\tau$, la respuesta vale el **63%** del valor final.
- **Respuesta al impulso** ($X(t)=A\delta(t)$): $Y(t) = \dfrac{A}{\tau}e^{-t/\tau}$. Sube inmediatamente a $A/\tau$ y decae. Medida: $t_s=4\tau$.
- **Respuesta senoidal** (en estado estacionario): $Y(t)|_{ss} = \dfrac{A}{\sqrt{\tau^2\omega^2+1}}\sin(\omega t+\phi)$, con $\phi=\arctan(-\omega\tau)$ (entre 0° y −90°). La **relación de amplitud** $AR = 1/\sqrt{\tau^2\omega^2+1}$ siempre es menor a 1 (señal atenuada); nunca hay adelanto de fase en primer orden.
- Un sistema de primer orden **nunca oscila ni sobrepasa** el valor final (una sola raíz real) → no tiene overshoot, decay ratio ni período de oscilación.

### Desarrollo

El primer orden es el bloque más simple y sirve de base para entender los efectos del control P sobre una planta (Unidad 7): al cerrar el lazo con control proporcional sobre una planta de primer orden, el sistema en lazo cerrado sigue siendo de primer orden pero con una constante de tiempo *efectiva* $\tau_1 = \tau/(1+K_cA)$ menor que la de la planta sola — es decir, **el lazo cerrado siempre responde más rápido** que la planta a lazo abierto, y cuanto mayor $K_c$, más chico $\tau_1$ y más rápido el sistema. A cambio, aparece un **offset** (error en estado estacionario) que nunca desaparece del todo con control P puro, aunque se reduce al aumentar $K_c$.

**Truco gráfico para reconocer primer orden vs segundo orden** (de una curva de respuesta al escalón): mirar el arranque en $t=0$.
- **Primer orden**: arranca con **pendiente máxima** en el origen, cóncava hacia abajo todo el tiempo, sin punto de inflexión ("rampa que se cansa"). Nunca se pasa del valor final.
- Si se pasa del valor final y oscila → ya es segundo orden subamortiguado (ver Unidad 5).
- Si no se pasa pero arranca **plano** y tiene forma de "S" (punto de inflexión) → segundo orden sobreamortiguado, no primer orden.

Razón física: en primer orden la salida puede cambiar de inmediato (un solo almacenamiento de energía); en segundo orden hay "inercia" (dos almacenamientos), por eso el arranque es plano.

### Ejercicios resueltos tipo

**Control proporcional sobre planta de primer orden — problema servo.** Con $\tau_i=0$, $G_c=K_c$, $G_1=\dfrac{1}{\tau s+1}$:
$$\frac{T'}{T'_R} = \frac{A_1}{\tau_1 s+1},\quad A_1=\frac{K_cA}{1+K_cA},\quad \tau_1=\frac{\tau}{1+K_cA}$$
Conclusiones: $\tau_1<\tau$ siempre (lazo más rápido que la planta); $A_1\neq$ valor de entrada siempre → aparece **offset** $= T'_R(\infty)-T'(\infty)$; a mayor $K_c$, menor offset (pero nunca cero).

**Problema regulador** (misma planta, perturbación como entrada): $\dfrac{T'}{T'_i} = \dfrac{A_2}{\tau_1 s+1}$, con $A_2=\dfrac{1}{1+K_cA}$, $\tau_1=\dfrac{\tau}{1+K_cA}$ — misma dinámica de primer orden, mismo $\tau_1$.

### Dudas / pendientes

_(sin datos en el historial)_

### Fuentes

- `TDC_ResumenTeoría_Opción1.pdf` (Cap. 5 "Respuestas de sistemas de primer orden", Cap. 13 "Respuesta transiente de un sistema de control sencillo")
- `Sistemas_de_primer_orden_250613_105654.pdf`
- Conversación: *Hoja de fórmulas esenciales*

---

## Unidad 5 — Sistemas de Segundo Orden

### Conceptos clave

- **Función de transferencia**: a partir de $\tau^2\dfrac{d^2Y}{dt^2}+2\xi\tau\dfrac{dY}{dt}+Y=X$:
$$G(s) = \frac{Y(s)}{X(s)} = \frac{1}{\tau^2s^2+2\xi\tau s+1}$$
$\tau$ = constante de tiempo (min); $\xi$ = coeficiente de amortiguamiento (adimensional); ambos $>0$ para sistemas físicos reales.
- **Raíces**: $s_{1,2} = -\dfrac{\xi}{\tau}\pm\dfrac{\sqrt{\xi^2-1}}{\tau}$. Tres casos según $\xi$:

| Caso | $\xi$ | Raíces | Tipo |
|---|---|---|---|
| I | $<1$ | Complejas | Subamortiguado |
| II | $=1$ | Reales e iguales | Críticamente amortiguado |
| III | $>1$ | Reales y distintas | Sobreamortiguado |

- **Medidas de desempeño** (solo existen si el sistema **oscila**, es decir, subamortiguado):
  - **Overshoot**: $OS = \exp\!\left(\dfrac{-\pi\xi}{\sqrt{1-\xi^2}}\right)$ — depende solo de $\xi$; menor $\xi$ → mayor overshoot.
  - **Decay ratio**: $RC = (OS)^2$.
  - **Rise time** $t_r$: tiempo en llegar por primera vez al valor final; crece con $\xi$. **Sin fórmula cerrada en los apuntes** — se mide gráficamente.
  - **Response time / tiempo de asentamiento**: tiempo hasta entrar y permanecer en banda ±5% del valor final.
  - **Period of oscillation**: frecuencia angular amortiguada, $\omega_d = \dfrac{\sqrt{1-\xi^2}}{\tau}$ (rad). *Ojo*: en el apunte esta expresión aparece etiquetada como "frecuencia (radianes)" — en rigor es $\omega_d$, no el período. El período real es $T=2\pi/\omega_d$.
  - **Natural period of oscillation**: $\omega_n = 1/\tau$ (caso $\xi=0$).
  - Críticamente amortiguado y sobreamortiguado **no tienen** overshoot, decay ratio, ni período (no oscilan). Sí tienen rise time (10%→90%) y response time.
- **Retardo de transporte** (transportation lag / dead time): $y(t)=x(t-\tau)$ ⟹ $\dfrac{Y(s)}{X(s)} = e^{-\tau s}$ ($\tau$ acá es un retardo puro, no la constante de tiempo).
- **Retardo de fase en 2do orden**: $\phi = -\arctan\!\left(\dfrac{2\xi\omega\tau}{1-(\omega\tau)^2}\right)$, varía entre 0° y −180°.

### Desarrollo

La idea central de esta unidad es que **$\xi$ gobierna la forma** de la respuesta (si oscila y cuánto) mientras que **$\tau$ gobierna la velocidad/período** — son parámetros independientes. Esto conecta directamente con el análisis por lugar de raíces (LGR, Unidad 8): la posición angular del polo complejo en el plano $s$ codifica $\xi$ (el ángulo respecto al eje real negativo), y la distancia al origen codifica $\omega_n=1/\tau$.

No confundir la **relación de amplitud** (respuesta en frecuencia, cuánto se atenúa una entrada senoidal) con el **overshoot** (respuesta al escalón, cuánto se pasa del valor final): son medidas de contextos distintos.

### Ejercicios resueltos tipo

_(no se resolvió un ejercicio numérico completo de segundo orden en el historial registrado; el contenido trabajado fue conceptual/gráfico — ver "reconocimiento gráfico" más abajo)_

**Reconocimiento gráfico 1er vs 2do orden**: ver Unidad 4 (mismo criterio, aplicado también acá desde el lado del 2do orden: si oscila → subamortiguado; si no oscila pero tiene forma de S → sobreamortiguado).

### Dudas / pendientes

- El apunte original tiene una **imprecisión de notación**: llama "frecuencia" a $\omega_d=\sqrt{1-\xi^2}/\tau$, cuando en realidad es la frecuencia angular amortiguada, no el período. Quedó marcado como corrección a tener en cuenta.
- No hay en los apuntes fórmula cerrada para el rise time de segundo orden subamortiguado — se obtiene gráficamente. No inventar una fórmula en el parcial.

### Fuentes

- `TDC_ResumenTeoría_Opción1.pdf` (Cap. 8 "Respuestas de sistemas de segundo orden y retardo de transporte")
- `Sistemas_de_segundo_orden_250703_215320.pdf`
- Conversación: *Hoja de fórmulas esenciales*

---

## Unidad 6 — Error en Estado Estable

### Conceptos clave

- **Tipo de sistema** ($q$) = número de integradores (polos en $s=0$) en la **función de transferencia de lazo abierto** (FTLA).
- **Tabla de error en estado estable** según tipo y entrada (aplica solo si el sistema es estable):

| Tipo | $E_{ss}$ escalón | $E_{ss}$ rampa | $E_{ss}$ parábola |
|---|---|---|---|
| 0 | finito ($1/(1+K_p)$) | $\infty$ | $\infty$ |
| 1 | **0** | finito ($1/K_v$) | $\infty$ |
| 2 | **0** | **0** | finito ($1/K_a$) |

- **Coeficientes de error**: $K_p$ (posición), $K_v$ (velocidad), $K_a$ (aceleración) — se calculan evaluando la FTLA en $s\to0$ según corresponda (constantes estáticas de error clásicas).
- **Cómo leer el tipo desde una gráfica**:
  - Respuesta a escalón que llega **exacta**, sin offset → tipo 1 o superior.
  - Respuesta a rampa **paralela** a la entrada pero separada por una distancia **constante** → tipo 1 (esa separación es $1/K_v$). Si la separación **crece sin parar** → tipo 0.
- Cada integrador que se agrega (subir el tipo) **mata el error** de la entrada de un orden inferior, pero acerca el sistema a la **inestabilidad** (ver Unidad 8).
- El **teorema del valor final** (Unidad 3) es la herramienta de cálculo directo: $E_{ss} = \lim_{s\to0} sE(s)$, con $E(s)$ la transformada de la señal de error.

### Desarrollo

Esta unidad es la bisagra entre el análisis matemático (Laplace, tipo de sistema) y el diseño de controladores (Unidad 7): **el tipo del sistema manda sobre el error en estado estable**, y cada acción de control sube o no sube ese tipo:
- **P**: no agrega integradores → no cambia el tipo.
- **I (dentro de un PI)**: agrega un polo en el origen → **sube el tipo en 1**, eliminando el error de la entrada correspondiente al tipo anterior.
- **D**: no agrega integradores ni cambia el tipo — solo actúa en el transitorio (en $s=0$ el término derivativo vale cero).

### Ejercicios resueltos tipo

**TermoNivel S.A. (regulador) — cálculo de tipo desde la FTLA.** Planta y sensor: $G_p(s)=\dfrac{1}{(3s+1)(s+1)}$, $H(s)=\dfrac{3}{(s+1)}$ (⚠️ $H\neq1$, tiene ganancia 3 en continua, afecta los valores finales). FTLA con controlador $G_c$:
$$G_cG_pH = G_c\cdot\frac{3}{(3s+1)(s+1)^2}$$
Con $G_c=K$ (proporcional): 3 polos (uno en $s=-1/3$, doble en $s=-1$), **sin** polos en el origen → **sistema tipo 0**.

**Reactor químico (servo/regulador) — tipo natural de la planta.** Con $G_p=\dfrac{1}{s(2s+1)}$, la planta ya trae un polo en el origen → el sistema **ya es tipo 1** antes de agregar ningún controlador. Con control P puro, $G=K_p\cdot\dfrac{1}{s(2s+1)}$ sigue tipo 1 → ante **escalón**, $E_{ss}=0$; ante **rampa**, $E_{ss}=1/K_v$ (finito). Agregando la acción integral de un PI se sube a tipo 2 → $E_{ss}=0$ también para rampa. Si la entrada fuera escalón, el integrador extra no aporta nada nuevo (ya daba cero con tipo 1).

**Parcial de práctica RoboPos S.A. (servo, planteado — sin resolver en el chat, quedó como ejercicio para el usuario).** $G_p(s)=\dfrac{2}{(s+1)(s+2)}$, $H=1$. Compara tres diseños de controlador (P, PI, PD) pidiendo tipo de sistema, coeficientes de error, $E_{ss}$ ante escalón y rampa, y luego una variante con $G_p=\dfrac{2}{s(s+1)(s+2)}$ (integrador natural agregado).

### Dudas / pendientes

_(sin dudas registradas explícitamente; el ejercicio RoboPos quedó pendiente de resolución por el usuario, sin corrección registrada en el historial)_

### Fuentes

- `TDC_ResumenTeoría_Opción1.pdf` (referencias dispersas en Cap. 9, 12, 13, 14)
- `Error_en_estado_estable_y_Estabilidad_251117_202210.pdf`
- Conversaciones: *Comparativa de reguladores P, PI y PD ante entrada escalón*, *Clasificación de ejercicio servo versus regulador*, *Hoja de fórmulas esenciales*

---

## Unidad 7 — Controladores (P, PI, PD, PID)

### Conceptos clave

- **Proporcional (P)**: $p = K_c\varepsilon + p_s \;\Rightarrow\; \dfrac{P(s)}{\varepsilon(s)} = K_c$. Señal de control proporcional al error. No agrega polos ni ceros a la FTLA.
- **Proporcional-Integral (PI)**: $p = K_c\varepsilon + \dfrac{K_c}{\tau_i}\displaystyle\int_0^t\varepsilon\,dt + p_s \;\Rightarrow\; \dfrac{P(s)}{\varepsilon(s)} = K_c\left(1+\dfrac{1}{\tau_i s}\right)$. Requiere $K_c$ (ganancia) y $\tau_i$ (tiempo integral, minutos). **Objetivo: eliminar el error en estado estacionario** (sube el tipo del sistema en 1, agrega un polo en el origen y un cero).
- **Proporcional-Derivativo (PD)**: $p = K_c\varepsilon + K_c\tau_D\dfrac{d\varepsilon}{dt}+p_s \;\Rightarrow\; \dfrac{P(s)}{\varepsilon(s)} = K_c(1+\tau_D s)$. Se anticipa al error, "matándolo" antes de que crezca (agrega un cero).
- **PID**: $\dfrac{P(s)}{\varepsilon(s)} = K_c\left(1+\tau_D s+\dfrac{1}{\tau_i s}\right)$ (agrega un polo en el origen y dos ceros).
- **Qué agrega cada controlador a la FTLA**:

| Controlador | Aporta |
|---|---|
| P | nada (solo escala la ganancia) |
| PD | un cero |
| PI | un cero + un polo en el origen |
| PID | dos ceros + un polo en el origen |

- **Efecto de cada acción**:
  - **P**: reduce el offset pero no lo elimina. A mayor $K_c$, menor offset y sistema más rápido, pero **menor amortiguamiento** (relación inversa entre $K_c$ y $\xi$: subir $K_c$ → baja $\xi$ → más oscilación/overshoot). Intuición: un controlador más "agresivo" se pasa más del valor final.
  - **I**: elimina el offset (sube el tipo), pero acerca el sistema a la inestabilidad (el polo en el origen "empuja" el lugar de raíces).
  - **D**: no toca el offset (en $s=0$ vale cero) — solo mejora el transitorio, **aumenta el amortiguamiento ξ**, reduciendo el overshoot. El cero que agrega el PD "tira" las ramas del LGR hacia la izquierda → amortigua y mejora la estabilidad relativa.
- **Banda proporcional** ($PB$): $PB = \dfrac{100}{K_c}\,\%$. *(No figura textual en los apuntes del proyecto — es conocimiento estándar de control clásico; conviene confirmar con la cátedra la notación exacta usada.)* Relación inversa con $K_c$: $K_c$ grande → banda angosta → muy sensible al error (con un error chico ya se satura la salida, p. ej. una válvula al 100%). $K_c$ chico → banda ancha → poco sensible, necesita errores grandes para actuar.
- **Comparación visual P vs PI vs PID ante escalón** (patrón típico de gráfico de parcial): P llega rápido pero se queda con offset visible por debajo de la referencia; PI llega exacto a la referencia (mata el offset) pero oscila más antes de estabilizarse; PID llega exacto y oscila **menos** que el PI (por el aporte derivativo al amortiguamiento).

### Desarrollo

El eje conceptual de la unidad es que cada acción de control tiene un rol distinto y complementario:
- **P** determina qué tan agresivo es el ataque al error (velocidad vs. amortiguamiento — trade-off).
- **I** determina si el error en estado estable se elimina o no (vía el tipo del sistema, Unidad 6).
- **D** determina qué tan suave es la aproximación al valor final (amortiguamiento, sin tocar el error final).

Estos efectos se leen directamente en el LGR (Unidad 8): P solo reescala la ganancia sobre las mismas ramas; I agrega un polo en el origen que empuja el lugar de raíces hacia la derecha (menos estable, pero corrige el error); D agrega un cero que "atrae" las ramas hacia la izquierda (más estable, menos overshoot).

### Ejercicios resueltos tipo

**TermoNivel S.A. — identificación de controlador desde el LGR / tipo de sistema.** (Continuación del ejercicio de Unidad 6.) Con $G_cG_pH = \dfrac{3G_c}{(3s+1)(s+1)^2}$:
- Reglas usadas para identificar cada diseño: contar polos y ceros que agrega $G_c$ (P → nada; PD → 1 cero; PI → 1 polo en el origen + 1 cero; PID → 1 polo en el origen + 2 ceros).
- Con $G_c=K$ (P): sistema **tipo 0**, mantiene 3 polos reales.
- El machete de conclusiones que se armó al cierre del ejercicio: *"el tipo del sistema manda sobre el error en estado estable, y cada controlador sube o no sube ese tipo"*; P reduce offset sin matarlo; D no toca el offset (solo amortigua); I lo elimina porque sube el tipo.

**Parcial RoboPos S.A. (servo, práctica, sin resolver)**: compara diseño A ($K_c$, P), B ($K_c(1+\frac{1}{2s})$, PI) y C ($K_c(1+\frac{s}{3})$, PD) sobre $G_p=\dfrac{2}{(s+1)(s+2)}$, pidiendo identificar tipo de controlador, polos/ceros agregados, tipo de sistema resultante, rango de $K_c$ estable, y comparación de $E_{ss}$ ante escalón y rampa para los tres diseños.

### Dudas / pendientes

- La fórmula de banda proporcional ($PB=100/K_c$) **no aparece textual** en `TDC_ResumenTeoría_Opción1.pdf` — está en el programa pero no desarrollada numéricamente ahí. Confirmar con la cátedra si usan exactamente esa expresión.
- El ejercicio RoboPos S.A. quedó **sin resolver/corregir** en el historial (se le dio al usuario para practicar, con el solucionario reservado).

### Fuentes

- `TDC_ResumenTeoría_Opción1.pdf` (Cap. 10 "Controladores y elementos de control final")
- `Controladores_251118_230242.pdf`
- Conversaciones: *Comparativa de reguladores P, PI y PD ante entrada escalón*, *Clasificación de ejercicio servo versus regulador*, *Hoja de fórmulas esenciales*

---

## Unidad 8 — Estabilidad (incluye LGR)

### Conceptos clave

- **Definición BIBO**: sistema estable ⟺ respuesta acotada para toda entrada acotada. Respuesta no acotada ante entrada acotada ⟹ inestable.
- **Definición alternativa (Bolton, vía impulso)**: ante entrada impulso, si la salida → 0 cuando $t\to\infty$: estable. Si → $\infty$: inestable. Si tiende a un valor finito no nulo: **crítica o marginalmente estable**.
- **Función característica**: $1+G(s)=0$, donde $G(s)=GH$ es la **función de transferencia de lazo abierto**. Es la **misma** para problema servo y regulador — depende solo de la topología del lazo, no de dónde entra la señal (ver Unidad 2).
- **Criterio de estabilidad por ubicación de raíces**: el sistema es inestable si alguna raíz de la ecuación característica está **sobre o a la derecha** del eje imaginario.

| Ubicación de la raíz | Estado |
|---|---|
| Semiplano izquierdo | Estable |
| Sobre el eje imaginario | Marginal/críticamente estable (⚠️ la cátedra lo **cuenta como inestable**) |
| Semiplano derecho | Inestable |

- **Respuesta libre vs forzada**: Respuesta Total = Respuesta Libre (independiente de la entrada) + Respuesta Forzada. Para que el sistema sea útil, la respuesta libre debe decaer a cero (o oscilar sin crecer) — si crece sin límite, el sistema es inestable y puede autodestruirse si no hay topes de diseño.
- **Análisis de estabilidad con la ganancia**: se estudia cómo se mueven las raíces de la ecuación característica al variar $K$. Herramienta algebraica: **Routh-Hurwitz** (se arma la tabla y se busca el $K$ que anula una fila → da la frecuencia de cruce por el eje imaginario). Herramienta gráfica: **Lugar Geométrico de Raíces (LGR / root locus)**.

### LGR — Lugar Geométrico de Raíces

> **✅ Confirmado con la cátedra (2026-07-02): se pide SOLO análisis cualitativo del LGR, NO trazado formal.** No se exige el método completo de Evans (asíntotas, ángulos de salida, puntos de ruptura): lo que se evalúa es razonar qué le hace cada controlador a los polos/ceros del lazo y qué implica para velocidad y estabilidad. Las reglas formales de Evans que siguen quedan en la wiki **solo como referencia (conocimiento general Ogata/Nise/Dorf), no son evaluables**.

- **Qué es**: el camino que recorren los polos de lazo cerrado al variar $K_o$ de 0 a ∞, definido por la ecuación característica $1+K_oG(s)=0 \Leftrightarrow K_oG(s)=-1$.
- **Condición de ángulo** (define la *forma* del LGR): $\angle G(s) = 180°$ (+ múltiplos de 360°). Un punto $s$ pertenece al LGR sii la suma de ángulos desde los polos y ceros de $G(s)$ hasta ese punto da 180°.
- **Condición de módulo** (define el *valor de K* en cada punto del LGR): $K_o = 1/|G(s)|$ = (producto de distancias del punto a cada polo) / (producto de distancias del punto a cada cero).
- **Reglas cualitativas de movimiento usadas en la cátedra** (con $n$ ceros y $m$ polos en la FTLA, variando ganancia $0\to\infty$):
  - $m-n$ ramas se van a infinito.
  - $n$ ramas terminan en los ceros (los ceros son puntos fijos).
  - Un polo que se mueve **hacia la izquierda** → el sistema responde **más rápido** (no necesariamente "mejor", solo más rápido).
  - Un polo que se mueve **hacia la derecha** → se acerca al eje imaginario y eventualmente lo cruza → se vuelve inestable.
- **Reglas formales de Evans** [referencia / conocimiento general — **NO evaluable**, la cátedra pide solo análisis cualitativo]:
  1. Ramas y simetría: tantas ramas como polos ($n$); simétrico respecto al eje real.
  2. Cada rama arranca en un polo ($K=0$) y termina en un cero o en infinito ($K\to\infty$).
  3. Tramos del eje real: pertenecen al LGR si a su derecha hay un número **impar** de polos+ceros reales.
  4. Asíntotas: ángulos $\theta=(2k+1)\cdot180°/(n-m)$, saliendo del centroide $\sigma = [\sum\text{polos}-\sum\text{ceros}]/(n-m)$.
  5. Puntos de ruptura (breakaway/break-in): donde $dK_o/ds=0$; ahí dos ramas reales se separan hacia el plano complejo.
  6. Cruce con el eje $j\omega$: el $K$ crítico marginal; se calcula con Routh-Hurwitz.
  7. Ángulos de salida/llegada en polos/ceros complejos (aplican la condición de 180° en la vecindad del punto).
- **Polo dominante**: el más cercano al eje imaginario (más a la derecha dentro del semiplano izquierdo) domina la respuesta transitoria, incluso con varios polos en juego.
- **Relación $\xi$ ↔ posición del polo**: la posición **angular** del polo complejo respecto al eje real negativo codifica el coeficiente de amortiguamiento $\xi$; la distancia al origen codifica $\omega_n=1/\tau$. Por eso subir $K_c$ en un P (que mueve los polos siguiendo el LGR) tiende a reducir $\xi$ (ver Unidad 7).
- **Checklist de lectura de un LGR en un parcial**:
  1. ¿Alguna rama sobre o a la derecha del eje $j\omega$? → inestable para ese $K$.
  2. ¿Dónde está el polo dominante? → da velocidad y oscilación.
  3. ¿La rama tiene parte imaginaria? → sí: subamortiguado (hay overshoot); no: sobre/críticamente amortiguado.
  4. ¿En qué $K$ cruza el eje imaginario? → ahí está el límite de estabilidad ($K$ crítico).

### Desarrollo

La estabilidad es "el primer objetivo" al seleccionar un controlador (cita del apunte): sin estabilidad, no importa cuán bueno sea el error en estado estable o la respuesta transitoria. El criterio de raíces (semiplano izquierdo = estable) es la base teórica; el LGR es la herramienta visual para aplicar ese criterio cuando el parámetro libre es la ganancia $K$, conectando directamente con el efecto de cada controlador (Unidad 7): el polo/cero que agrega cada acción de control desplaza las ramas del LGR, y eso es exactamente lo que determina si el sistema se vuelve más o menos estable al subir la ganancia.

### Ejercicios resueltos tipo

Ver Unidad 6 y 7: TermoNivel S.A. (cálculo de tipo desde FTLA con $H\neq1$) usa el mismo denominador $1+G_cG_pH$ como función característica de base para el análisis de estabilidad, aunque el ejercicio en el historial se detuvo en la identificación del tipo, no llegó a resolver el rango de $K$ estable con Routh-Hurwitz de forma completa en el registro disponible.

### Dudas / pendientes

- ✅ **Resuelto (2026-07-02):** la cátedra pide **solo análisis cualitativo** del LGR, no trazado formal (reglas de Evans completas). Las reglas de Evans quedan en la wiki únicamente como referencia, no son evaluables.
- Verificar el rango de $K_c$ estable del ejercicio RoboPos S.A. (parte del parcial de práctica, pendiente de resolución).

### Fuentes

- `TDC_ResumenTeoría_Opción1.pdf` (Cap. 14 "Estabilidad")
- `Error_en_estado_estable_y_Estabilidad_251117_202210.pdf`
- Conversaciones: *Claves para interpretar gráficas logarítmicas* (LGR), *Hoja de fórmulas esenciales*, *Comparativa de reguladores P, PI y PD ante entrada escalón*

---

## Unidad 9 — Robótica (bonus)

> No forma parte del temario de 8 unidades declarado para TPA, pero hay material de cátedra dedicado (`7__Robótica.pdf`, `7_1__Robótica.pdf`) que se incluye para no perder contenido. Confirmar si entra en la evaluación de esta materia o pertenece a otro módulo/cursada.

### Conceptos clave

- **Automatización**: técnicas para optimizar recursos humanos y materiales usando avances de mecánica, informática y robótica. Objetivos: productividad, calidad/uniformidad, seguridad, reducción de tiempos e inventarios.
- **Robot**: estructura mecánica con cierto grado de autonomía, bajo control de un computador, con sistema sensorial para percibir su entorno. Tipos: manipuladores robóticos y robots móviles.
- **Leyes de la robótica (Asimov, 1944)**: no dañar a un humano (ni por inacción); obedecer órdenes humanas salvo que contradigan la 1ª ley; autoprotegerse salvo que contradiga las dos anteriores.
- **Definiciones mecánicas**: eslabones unidos por articulaciones; **grado de libertad** = movimiento independiente de cada articulación respecto a la anterior; **espacio de trabajo** = volumen alcanzable por el robot.
- **Atributos de un robot**: movilidad, versatilidad (reprogramable), percepción (sensores), autonomía.
- **Cinemática del robot**: estudio de posición/orientación en función de las coordenadas articulares.
  - **Cinemática directa**: de los ángulos de las articulaciones → posición/orientación del efector final.
  - **Cinemática indirecta (inversa)**: de la posición deseada → ángulos necesarios de las articulaciones.
- **Método de Denavit-Hartenberg (D-H, 1955)**: método matricial sistemático para asignar sistemas de coordenadas a cada eslabón de una cadena articulada.
  - Parámetros D-H: $a_i$ (distancia entre ejes $z_{i-1}$/$z_i$ a lo largo de $x_i$), $\alpha_i$ (ángulo entre $z_{i-1}$/$z_i$ alrededor de $x_i$), $d_i$ (distancia entre $x_{i-1}$/$x_i$ a lo largo de $z_{i-1}$), $\theta_i$ (ángulo entre $x_{i-1}$/$x_i$ alrededor de $z_{i-1}$).
  - Pasos: numerar eslabones (0 a n) y articulaciones (1 a n, distinguiendo revolución/rotación vs. prismática/traslación) → asignar sistema de coordenadas por eslabón (3 casos según si $z_i$ intercepta, es paralelo, o se une por perpendicular común a $z_{i-1}$) → obtener parámetros D-H → matriz de transformación homogénea $H_i^{i-1}$ por par de sistemas → matriz resultante $H_n^0 = H_1^0 H_2^1\cdots H_n^{n-1}$ → ecuaciones de cinemática directa desde el vector de traslación de esa matriz.
  - Efector final tipo pinza: eje $Z_n$ (letra $a$) en dirección de aproximación al objeto; eje $Y_n$ (letra $s$) en dirección de apertura/cierre de los dedos; eje $X_n$ (letra $n$) normal a ambos.
- **Composición de matrices de transformación**:
  - **Premultiplicación**: cuando las transformaciones se hacen sobre el eje **original** (del sistema $S_0$).
  - **Posmultiplicación**: cuando las transformaciones se hacen sobre el eje **actual** (voy de $S_0$ a $S_1$, de $S_1$ a $S_2$, etc.).

### Desarrollo

El bloque de robótica es autocontenido respecto al resto de TPA (no depende de Laplace/controladores) y se centra en la **cinemática**: cómo describir matemáticamente la geometría de un manipulador. D-H es el método estándar para no tener que inventar a mano un sistema de coordenadas por cada robot — sistematiza la asignación de ejes y permite construir la cadena de matrices de transformación homogénea que lleva de la base (sistema 0) al efector final (sistema n).

### Ejercicios resueltos tipo

**Ejemplo D-H — robot de 2 eslabones planar** (Práctica Ej. 27, parcialmente visible en los apuntes): identificación de ejes, casos de intersección/paralelismo entre $z_i$ y $z_{i-1}$, tabla de parámetros D-H y armado de matrices homogéneas $H_1^0$, $H_2^1$.

**Ejemplo D-H — robot de 3 grados de libertad** (con $d_1$, $d_2^*$, $d_3^*$ como variables prismáticas y $\theta_1^*$ angular): tabla de parámetros:

| $i$ | $a_i$ | $\alpha_i$ | $d_i$ | $\theta_i$ |
|---|---|---|---|---|
| 1 | 0 | 0 | $d_1$ | $\theta_1^*$ |
| 2 | 0 | −90° | $d_2^*$ | −90° |
| 3 | 0 | 0 | $d_3^*$ | 0 |

con las matrices homogéneas correspondientes armadas paso a paso.

**Ejemplos de composición de matrices**: giro −90° sobre eje $OX$ + traslación $(5,5,10)$ + giro 90° sobre eje $OZ$ (premultiplicación); traslación $(-3,10,10)$ + giro −90° sobre $O'U$ + giro 90° sobre $O'V$ (posmultiplicación).

### Dudas / pendientes

_(sin dudas registradas en el historial de conversaciones — este bloque no se trabajó en chat, solo está presente en los PDFs subidos)_

### Fuentes

- `7__Robótica.pdf`
- `7_1__Robótica.pdf`

---

## Log

- 2026-04-21: creación del system prompt del proyecto y estructura de 8 unidades en Notion (conversación *Sistema de estudio personalizado para TPA*).
- 2026-06-08: ejercicio resuelto de clasificación servo/regulador (reactor químico), explicación de banda proporcional y comparación de gráficos P/PI/PID (conversación *Clasificación de ejercicio servo versus regulador*).
- 2026-06-10: desarrollo extenso de LGR — interpretación, reglas de Evans, relación ξ↔posición del polo (conversación *Claves para interpretar gráficas logarítmicas*).
- 2026-06-12: hoja de fórmulas de los 8 bloques del programa, hoja de medidas de desempeño, comparación gráfica P vs PD, relación Kc↔ξ (conversación *Hoja de fórmulas esenciales*).
- 2026-06-30: ejercicio resuelto TermoNivel S.A. (regulador, identificación de controlador desde LGR/tipo de sistema) + parcial de práctica servo RoboPos S.A. planteado sin resolver (conversación *Comparativa de reguladores P, PI y PD ante entrada escalón*).
- 2026-07-02: migración de todo el conocimiento del proyecto a esta wiki e instalación como `materias/TPA.md` (reemplazo del stub inicial).
- 2026-07-02: confirmado que la cátedra pide **solo análisis cualitativo del LGR** (no trazado formal de Evans) → Unidad 8 actualizada, duda cerrada.
