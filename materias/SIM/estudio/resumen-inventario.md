# Simulación de un sistema de inventario

> **SIM · UTN-ISI · para el parcial 1**
>
> Inventario es el tema con **más presencia del parcial**: aparece en los nueve exámenes del
> archivo, sin excepción. Este apunte junta el resumen propio (Law §1.5), el original de Law
> transcripto del apunte de cátedra —que trae detalles que el resumen recorta—, la plantilla en
> blanco de la cátedra y los dos ejercicios numéricos que ya se tomaron.

---

## 0. Qué se toma de inventario

| Qué preguntan | Dónde cayó |
|---|---|
| **Los costos** del modelo (los tres, con fórmula) | 2021-10 P1, 2021-12 P5, Globalizador P5, 2022 P4 — **4 veces** |
| **Los tres niveles** $I(t)$, $I^+(t)$, $I^-(t)$ | 2021-10 P16, 2023 P2b, Final 2021-11 P10 — **3 veces** |
| **Ejercicio numérico**: calcular el costo total promedio mensual | 2024 P2, 2025 ej. 3 — **2 veces, y son los dos últimos parciales** |
| **La política (s, S)** | 2022 P4, 2023 P2a, 2025 (1.3) |
| **Planteo del sistema** (demanda, política, demora del proveedor) | 2023 P2a |
| **Las rutinas / eventos** | Final 2020-08 (oral) |
| **Diferencia con Investigación Operativa** | Preguntas frecuentes #9 |

> **Lo más importante para este parcial**: los **dos últimos parciales (2024 y 2025) pidieron el
> ejercicio numérico**, no la teoría. Si la tendencia sigue, el ejercicio de inventario es lo que
> más conviene practicar. Está resuelto paso a paso en §7.

---

## 1. El sistema, en concreto

Una empresa vende **un solo producto** y tiene que decidir cuántas unidades tener en inventario
durante los próximos $n$ meses. El objetivo del estudio **no es** encontrar el stock óptimo: es
**comparar políticas de pedido distintas** y ver cuál sale más barata.

Cuatro cosas definen el sistema:

| Elemento | Cómo se modela | Valores de Law |
|---|---|---|
| **Tiempo entre demandas** | Variables IID con distribución **exponencial** | media 0,1 mes |
| **Tamaño de la demanda $D$** | Variable IID **discreta**, independiente de cuándo ocurre la demanda | 1, 2, 3 o 4 unidades con probabilidades $\tfrac16, \tfrac13, \tfrac13, \tfrac16$ |
| **Demora del proveedor** (*lead time* / retardo de envío) | Variable **uniforme** | entre 0,5 y 1 mes |
| **Revisión del inventario** | **Periódica**: al comienzo de cada mes | cada 1 mes |

> **El detalle que hace todo lo demás**: la revisión es **periódica**, no continua. La empresa mira
> el inventario **una vez por mes** y recién ahí decide si pide. Entre dos revisiones el inventario
> puede caer todo lo que sea, incluso **por debajo de cero**. De ahí sale el backlog, y de ahí sale
> el costo por faltante.

---

## 2. La política (s, S)

Siendo $I$ el nivel de inventario **al comienzo del mes** (en el momento de la revisión), la
cantidad $Z$ a pedir es:

$$Z = \begin{cases} S - I & \text{si } I < s \\[2pt] 0 & \text{si } I \ge s \end{cases}$$

| Símbolo | Nombre | Qué es |
|---|---|---|
| $s$ | **Punto de pedido** (*reorder point*) | El umbral: si el inventario cayó por debajo, se pide |
| $S$ | **Tope** (nivel objetivo) | Hasta dónde se rellena cuando se pide |

En castellano: *"si al revisar tengo menos de $s$, pido lo necesario para llegar a $S$; si tengo
$s$ o más, no pido nada"*. Se la llama **política estacionaria** porque $s$ y $S$ no cambian mes a
mes.

**Comparar políticas** = probar distintos pares $(s, S)$ y ver cuál da menor costo total promedio
mensual. Law compara nueve:

| $s$ | 20 | 20 | 20 | 20 | 40 | 40 | 40 | 60 | 60 |
|---|---|---|---|---|---|---|---|---|---|
| $S$ | 40 | 60 | 80 | 100 | 60 | 80 | 100 | 80 | 100 |

---

## 3. Los tres niveles de inventario

Pedido textual en 2021-10 P16, 2023 P2b y Final 2021-11 P10. La consigna de 2023 agrega:
*"ilustre con un ejemplo gráfico cómo se pueden ir modificando a lo largo del tiempo"*.

| Símbolo | Definición | Qué significa |
|---|---|---|
| $I(t)$ | Nivel de inventario en el instante $t$ | Puede ser **positivo, cero o negativo** |
| $I^+(t) = \max\{I(t),\,0\}$ | Unidades **físicamente en existencia** | Lo que realmente hay en el depósito. Nunca negativo |
| $I^-(t) = \max\{-I(t),\,0\}$ | Unidades en **backlog** | Lo demandado y no entregado por falta de stock. Nunca negativo |

**Las tres relaciones que conviene tener claras:**

- En todo momento, **una de las dos vale cero**: si $I(t) > 0$ entonces $I^-(t) = 0$, y si $I(t) < 0$ entonces $I^+(t) = 0$.
- $I(t) = I^+(t) - I^-(t)$
- $I(t)$ **baja en escalones** en los instantes en que ocurren las demandas, y **sube de golpe** cuando llega un pedido.

### 3.1 Cómo funciona el backlog

- Si la demanda **no supera** el inventario disponible, se satisface de inmediato.
- Si la demanda **supera** el inventario, el excedente queda **en espera (backlog)** y se cubre con entregas futuras. El nuevo nivel es *(nivel viejo − tamaño de la demanda)*, que da **negativo**.
- Cuando **llega un pedido**, primero se usa para **eliminar todo el backlog** que se pueda; el resto (si queda) se suma al inventario.

### 3.2 Ejemplo gráfico

> Con $s = 30$, $S = 60$, $I(0) = 60$, sobre 3 meses. Es la figura 1.54 de Law, con números.

| $t$ | Evento | $I(t)$ | $I^+(t)$ | $I^-(t)$ |
|---|---|---|---|---|
| 0 | Evaluación: $I = 60 \ge s$ → no pide | 60 | 60 | 0 |
| 0,3 | Demanda de 20 | 40 | 40 | 0 |
| 0,7 | Demanda de 15 | 25 | 25 | 0 |
| **1,0** | **Evaluación: $I = 25 < s$ → pide $Z = 60-25 = 35$** | 25 | 25 | 0 |
| 1,2 | Demanda de 30 → **no alcanza**, quedan 5 en backlog | **−5** | 0 | **5** |
| 1,6 | **Llega el pedido de 35**: cubre los 5 de backlog, entran 30 | 30 | 30 | 0 |
| 2,0 | Evaluación: $I = 30 \ge s$ → no pide | 30 | 30 | 0 |
| 2,4 | Demanda de 25 | 5 | 5 | 0 |
| 3,0 | Fin de la simulación | 5 | 5 | 0 |

```
   I(t)
    60 ┤━━━━━━━┓
       │       ┃
    40 ┤       ┗━━━━━━━━┓
    30 ┤· · · · · · · · ┃· · · · · · · · ┏━━━━━━━━━━━━━━━┓ · · · · ·  s = 30
    25 ┤                ┗━━━━━━━━┓       ┃               ┃
       │                         ┃       ┃               ┃
     5 ┤                         ┃       ┃               ┗━━━━━━━━━
     0 ┼─────────────────────────╂───────╂───────────────────────────→ t
       0     0,3     0,7    1,0  ┃  1,2  ┃  1,6    2,0   2,4      3,0
    -5 ┤                         ┗━━━━━━━┛
       │                          backlog
              ↑pide Z=35                ↑llega el pedido
```

---

## 4. Los costos

**Es lo más preguntado del tema** (cuatro apariciones). Hay que saber los tres, con su fórmula y
qué incluye cada uno.

| Costo | Fórmula | Qué incluye |
|---|---|---|
| **De pedido** | $K + i\,Z$ | $K$ = **costo fijo de preparación** (*setup cost*), $i$ = **costo incremental por unidad**, $Z$ = cantidad pedida. **Si $Z=0$ no se incurre en ningún costo** |
| **De almacenamiento** (*holding*, $h$) | $h \cdot \bar{I}^+$ | Alquiler del depósito, seguros, impuestos, mantenimiento, y el **costo de oportunidad del capital inmovilizado** |
| **Por faltante** (*shortage*, $\pi$) | $\pi \cdot \bar{I}^-$ | Costos administrativos extra por llevar el registro del backlog, y la **pérdida de buena voluntad** de los clientes |

Los promedios temporales sobre los $n$ meses:

$$\bar{I}^+ = \frac{\displaystyle\int_0^n I^+(t)\,dt}{n} \qquad\qquad \bar{I}^- = \frac{\displaystyle\int_0^n I^-(t)\,dt}{n}$$

$$\boxed{\text{Costo total promedio mensual} = \frac{\text{costo de pedido acumulado}}{n} + h\,\bar{I}^+ + \pi\,\bar{I}^-}$$

> **Cómo se calculan las integrales en la práctica**: son **áreas de rectángulos**. Entre dos
> eventos consecutivos el nivel de inventario es constante, así que el área es *(nivel) × (tiempo
> transcurrido)*. Se acumula igual que las áreas de $Q(t)$ y $B(t)$ en el modelo de colas: cada vez
> que $I(t)$ va a cambiar, primero se acumula el área del tramo que termina.

⚠️ **Dos errores que están en los exámenes resueltos del archivo, no los copies:**

1. El parcial **2021-12 P5** invierte $h$ y $\pi$: dice *"costo por ítems almacenados $I^+\cdot\pi$"* y *"costo por ítems adeudados $I^-\cdot h$"*. **Es al revés.** La regla mnemotécnica: **$h$ de *holding*, va con lo que tenés guardado ($I^+$)**; **$\pi$ va con lo que debés ($I^-$)**.
2. El mismo parcial dice *"$K + Z\cdot i$, donde $Z$ es el costo por unidad pedida e $i$ es la cantidad"*. **Están cambiados**: $i$ es el **costo** unitario, $Z$ es la **cantidad**.

> **Detalle fino de Law**: en la formulación se ignora que algunos costos de almacenamiento se
> siguen pagando aunque $I^+(t) = 0$ (el depósito se alquila igual). Se ignora **a propósito**,
> porque ese costo es independiente de la política usada y el objetivo es *comparar* políticas —
> no afecta cuál resulta mejor.

---

## 5. Los eventos y las rutinas

### 5.1 Los cuatro eventos

El resumen propio menciona tres, pero **el original de Law y la plantilla de la cátedra usan
cuatro**:

| Nº | Evento | Qué lo dispara |
|---|---|---|
| **1** | **Arribo de un pedido** del proveedor | Lo programa la evaluación de inventario, con el lead time |
| **2** | **Demanda** de un cliente | Se autoprograma: cada demanda programa la siguiente |
| **3** | **Fin de la simulación** (a los $n$ meses) | Se programa al inicio |
| **4** | **Evaluación de inventario** al comienzo del mes | Se autoprograma: cada evaluación programa la del mes siguiente |

> **Por qué el fin de simulación es el evento 3 y no el 4** — este detalle es de Law y es el tipo de
> cosa que se pregunta en un oral: en el instante $t = n$ están programados **los dos** eventos, el
> fin de simulación y la evaluación de inventario. Se quiere que **el fin se ejecute primero**,
> porque no tiene sentido evaluar el inventario y hacer un pedido que nunca va a llegar (y cargar su
> costo). Como la rutina de temporización, ante un empate de tiempos, **da prioridad al evento de
> número más bajo**, numerarlo 3 garantiza el orden correcto.

### 5.2 Variables de estado

Según Law son exactamente tres:

- $I(t)$, el **nivel de inventario**.
- La **cantidad del pedido pendiente** de la empresa al proveedor.
- El **tiempo del último evento** — hace falta para poder calcular las áreas bajo $I^+(t)$ e $I^-(t)$.

### 5.3 La plantilla de la cátedra

`fuentes/teoria-flamini/Plantilla Inventario.pdf` es un esquema en blanco para completar a mano.
Su estructura dice exactamente qué esperan que sepas:

```
┌─────────────────────────┬────────────────────────────────────────┐
│    ESTADO DEL SISTEMA   │                EVENTOS                 │
│                         │                                        │
│    I(t)          I+     │   ┌───────┐   ┌───────────────────┐    │
│                         │   │ reloj │   │ arribo de pedido  │    │
│    I-     último pedido │   │       │   ├───────────────────┤    │
│                         │   │       │   │ arribo de cliente │    │
│    s             S      │   └───────┘   ├───────────────────┤    │
│                         │               │ fin de simulación │    │
│                         │               ├───────────────────┤    │
│                         │               │ evaluación inv.   │    │
│                         │               └───────────────────┘    │
│                         ├────────────────────────────────────────┤
│                         │        CONTADORES ESTADÍSTICOS         │
│                         │                                        │
│                         │  Costo     Costo ped.                  │
│                         │  pedidos   acumulado    A(I+)    A(I-) │
└─────────────────────────┴────────────────────────────────────────┘
```

`A(I+)` y `A(I-)` son los **acumuladores de área** bajo $I^+(t)$ e $I^-(t)$.

### 5.4 Las rutinas

**Evento de evaluación de inventario** (el que corre al inicio de cada mes)
```
1. ¿I(t) < s?
   SÍ:
      1.1. Determinar la cantidad a pedir:  Z = S - I(t)
      1.2. Acumular el costo del pedido:    K + i·Z
      1.3. Generar el lead time (uniforme) y programar el
           ARRIBO DE PEDIDO en  Reloj + lead time
2. Programar la próxima evaluación en  Reloj + 1 mes
3. Retornar
```

**Evento de demanda**
```
1. Generar el tamaño de esta demanda
2. Disminuir el nivel de inventario en ese tamaño   I = I - D
3. Generar el próximo tiempo entre demandas (exponencial) y
   programar la próxima DEMANDA
4. Retornar
```

**Evento de arribo de pedido**
```
1. Incrementar el nivel de inventario en la cantidad previamente pedida
   (primero cubre el backlog, el resto entra al inventario)
2. Eliminar el evento de arribo de consideración (ponerlo en ∞)
3. Retornar
```

**Actualizar acumuladores de área** (se llama antes de cada cambio de estado)
```
1. ¿I(t) durante el intervalo anterior fue negativo, cero o positivo?
   Negativo → A(I-) = A(I-) + (-I) · (Reloj - TUE)
   Positivo → A(I+) = A(I+) + ( I) · (Reloj - TUE)
   Cero     → no acumula en ninguno
2. TUE = Reloj
3. Retornar
```

### 5.5 Diagrama de desencadenamiento de eventos

```
   ┌────────────────────────────┐
   ▼                            │
   Evaluación de inventario ────┘ ─────────>  Arribo de pedido
   (se reprograma cada mes)

   ┌───────────┐
   ▼           │
   Demanda ────┘
   (cada demanda programa la siguiente)
```

Los dos eventos **autorreferenciados** son los que sostienen el avance del sistema. El arribo de
pedido **no se autoprograma**: solo lo dispara la evaluación, y únicamente cuando hay que pedir.

---

## 6. Medidas de desempeño

Nomenclatura del final resuelto 2020-08, que es la que usa la cátedra:

| Medida | Fórmula | Qué es |
|---|---|---|
| **CCP** | $ACP / n$ | Costo de la cantidad pedida (ACP = acumulado de los $K + iZ$) |
| **CUI** | $h \cdot \bar{I}^+$ | Costo de las unidades en inventario |
| **CUP** | $\pi \cdot \bar{I}^-$ | Costo de las unidades perdidas (en backlog) |
| **CMP** | $CCP + CUI + CUP$ | **Costo mensual promedio** — es lo que se compara entre políticas |

---

## 7. El ejercicio numérico

Cayó en **2024 P2** y en **2025 ejercicio 3**, con la misma consigna: *"Determine el costo total
promedio mensual para un sistema de inventario con la política de pedidos vista en clase, y con
estos datos…"*, seguida de los parámetros y **cinco números aleatorios**.

### 7.1 Los tres generadores que hacen falta

Cada variable aleatoria del modelo necesita su generador. **Los tres salen por transformada
inversa** (Unidad 7 de la wiki):

**a) Tiempo entre demandas — exponencial de media $\mu$**

$$x = -\mu \ln(r)$$

**b) Tamaño de la demanda — discreta, por transformada inversa discreta**

Se arma la acumulada y se ve en qué tramo cae $r$. Para la distribución de 2025
($3$ w.p. $\tfrac13$, $4$ w.p. $\tfrac16$, $5$ w.p. $\tfrac16$, $6$ w.p. $\tfrac13$):

| Si $r$ cae en… | $D =$ |
|---|---|
| $[0;\ 0{,}3333)$ | 3 |
| $[0{,}3333;\ 0{,}5)$ | 4 |
| $[0{,}5;\ 0{,}6667)$ | 5 |
| $[0{,}6667;\ 1)$ | 6 |

**c) Demora del proveedor — uniforme en $(a,b)$**

$$x = a + (b-a)\,r$$

### 7.2 Los cinco números de 2025, evaluados

Datos: media 0,55 · lead time uniforme $[0{,}5;1]$ · $K=50$, $i=5$, $h=2{,}5$, $\pi=6$ ·
$s=30$, $S=60$, $I_0=40$.

Conviene armar esta tabla **antes** de empezar la traza, porque no sabés de antemano cuál número
va a hacer falta para qué:

| $r$ | Como tiempo entre demandas<br>$-0{,}55\ln r$ | Como tamaño de demanda | Como lead time<br>$0{,}5 + 0{,}5r$ |
|---|---|---|---|
| 0,9501 | 0,0282 | 6 | 0,9751 |
| 0,1304 | 1,1204 | 3 | 0,5652 |
| 0,9700 | 0,0168 | 6 | 0,9850 |
| 0,3546 | 0,5702 | 4 | 0,6773 |
| 0,9258 | 0,0424 | 6 | 0,9629 |

⚠️ **Advertencia honesta sobre este ejercicio.** Consumiendo los cinco números en el orden natural
—uno para el tiempo hasta la primera demanda, uno para su tamaño, uno para el tiempo hasta la
segunda, uno para su tamaño, uno para la tercera— la simulación llega a $t = 0{,}087$ meses: **no
alcanza siquiera la primera evaluación de inventario del mes 1**, nunca se hace un pedido, y el
"costo total promedio mensual" no da nada interpretable.

Probé también la convención $x = -\mu\ln(1-r)$: ahí los tiempos se estiran, pero el inventario
arranca en 40 y solo baja hasta 33 con las dos demandas que alcanzan a generarse, así que **nunca
cruza $s = 30$ y tampoco se pide nada**.

**Conclusión**: al enunciado, tal como está transcripto, le falta información — o más números
aleatorios, o un horizonte de simulación explícito, o una convención de consumo de los números que
se dio en clase. **Preguntalo antes del parcial.** Lo que sí es examinable y transferible es el
método, que va completo en §7.3.

### 7.3 Ejercicio resuelto de punta a punta

> Como el enunciado real está incompleto, va resuelto el ejemplo de §3.2, que tiene los mismos
> parámetros de costo de 2025 y sí cierra. **Este es el procedimiento que hay que reproducir.**

**Datos**: $s=30$, $S=60$, $I(0)=60$, $n=3$ meses, $K=50$, $i=5$, $h=2{,}5$, $\pi=6$.

**Paso 1 — La traza** (la tabla de §3.2). El único pedido se hace en $t=1{,}0$: como $I=25 < s=30$,
se pide $Z = S - I = 60 - 25 = 35$.

**Paso 2 — Costo de pedido acumulado**

$$ACP = K + i\,Z = 50 + 5 \times 35 = 225$$
$$CCP = \frac{225}{3} = 75$$

**Paso 3 — Área bajo $I^+(t)$.** Cada tramo aporta *(nivel) × (duración)*:

| Tramo | Duración | $I^+$ | Área |
|---|---|---|---|
| $[0;\ 0{,}3)$ | 0,3 | 60 | 18,0 |
| $[0{,}3;\ 0{,}7)$ | 0,4 | 40 | 16,0 |
| $[0{,}7;\ 1{,}2)$ | 0,5 | 25 | 12,5 |
| $[1{,}2;\ 1{,}6)$ | 0,4 | 0 | 0,0 |
| $[1{,}6;\ 2{,}4)$ | 0,8 | 30 | 24,0 |
| $[2{,}4;\ 3{,}0)$ | 0,6 | 5 | 3,0 |
| | | **Total** | **73,5** |

$$\bar{I}^+ = \frac{73{,}5}{3} = 24{,}5 \qquad\Rightarrow\qquad CUI = h\,\bar{I}^+ = 2{,}5 \times 24{,}5 = 61{,}25$$

**Paso 4 — Área bajo $I^-(t)$.** Solo hay backlog en el tramo $[1{,}2;\ 1{,}6)$, con 5 unidades:

$$\int_0^3 I^-(t)\,dt = 5 \times 0{,}4 = 2{,}0$$
$$\bar{I}^- = \frac{2{,}0}{3} = 0{,}6667 \qquad\Rightarrow\qquad CUP = \pi\,\bar{I}^- = 6 \times 0{,}6667 = 4{,}00$$

**Paso 5 — Costo total promedio mensual**

$$CMP = CCP + CUI + CUP = 75 + 61{,}25 + 4{,}00 = \boxed{140{,}25 \text{ por mes}}$$

> **El error más común en este ejercicio**: dividir el costo de pedido por algo que no sea $n$, o
> calcular las áreas con el nivel **nuevo** en vez del **viejo**. El área de un tramo se calcula
> con el nivel que hubo **durante** ese tramo, o sea el anterior al evento que lo cierra.

---

## 8. La diferencia con Investigación Operativa

Pregunta frecuente #9 del archivo, y es una pregunta conceptual linda porque conecta dos materias.

| | **Investigación Operativa** | **Simulación** |
|---|---|---|
| Control del inventario | **Continuo**: se vigila permanentemente | **Periódico**: se revisa al inicio de cada mes |
| Cuándo se pide | **Apenas** se toca el nivel mínimo | Recién en la **próxima revisión** |
| ¿Puede haber inventario negativo? | **No**: el pedido se dispara antes | **Sí**: entre dos revisiones la demanda puede superar el stock |
| Consecuencia | No hay backlog | Aparecen $I^-(t)$ y el **costo por faltante** |

> En una línea: *"en IO los pedidos se hacen inmediatamente cuando se llega al nivel mínimo, el
> control es constante; en el manejo de inventario de simulación el control es periódico, por lo
> que se pueden generar niveles negativos de inventario."*

---

## 9. Errores y trampas

| # | Trampa | Lo correcto |
|---|---|---|
| 1 | Cambiar $h$ y $\pi$ | **$h$ de *holding*** va con $I^+$ (lo guardado); $\pi$ va con $I^-$ (lo adeudado) |
| 2 | Cambiar $i$ y $Z$ en $K + iZ$ | $i$ es el **costo** por unidad, $Z$ la **cantidad** pedida |
| 3 | Creer que $I^+$ e $I^-$ pueden ser negativos | Son máximos contra 0: **nunca** son negativos. El que puede ser negativo es $I(t)$ |
| 4 | Pedir $Z = S$ | Se pide $Z = S - I$: lo que **falta** para llegar al tope, no el tope |
| 5 | Cobrar costo de pedido cuando $Z = 0$ | Si no se pide, **no hay costo**, ni siquiera el fijo $K$ |
| 6 | Calcular el área con el nivel nuevo | Se usa el nivel que hubo **durante** el tramo, o sea el viejo |
| 7 | Olvidar que el pedido primero cubre el backlog | Al llegar, **primero** cancela $I^-$; el sobrante recién ahí suma a $I^+$ |
| 8 | Poner el fin de simulación como evento 4 | Va como **evento 3**, para que se ejecute antes que la evaluación en $t=n$ |

---

## 10. Checklist de repaso

- [ ] Describo el **planteo**: demanda exponencial, tamaño discreto, lead time uniforme, revisión periódica.
- [ ] Escribo la **política (s, S)** con la llave de los dos casos y explico qué es $s$ y qué es $S$.
- [ ] Defino $I(t)$, $I^+(t)$ e $I^-(t)$ y **dibujo** un ejemplo de cómo evolucionan, con un episodio de backlog.
- [ ] Enuncio los **tres costos** con su fórmula y digo qué incluye cada uno.
- [ ] Escribo las integrales de $\bar{I}^+$ y $\bar{I}^-$ y sé que en la práctica son **áreas de rectángulos**.
- [ ] Enumero los **cuatro eventos** y explico por qué el fin de simulación es el nº 3.
- [ ] Escribo la **rutina de evaluación de inventario** en pseudocódigo.
- [ ] Armo los **tres generadores** (exponencial, discreta por transformada inversa, uniforme).
- [ ] Resuelvo el **ejercicio numérico** completo hasta el costo total promedio mensual.
- [ ] Explico la **diferencia con IO** (control continuo vs. periódico → backlog).

---

## Fuentes

- `fuentes/Resumen Simulación.pdf` — Law cap. 1, §1.5, §1.5.1 y §1.5.2
- `fuentes/apuntes-catedra/Apunte Weitz con hojas rotadas y acotado.pdf` — el original de Law §1.5 (págs. 74–79 del libro), transcripto en `fuentes/txt/apuntes-catedra__Weitz__p21-30.md`
- `fuentes/teoria-flamini/Plantilla Inventario.pdf` — plantilla en blanco de la cátedra
- `fuentes/resumenes/Resumen 1.pdf` (Pagliaro) — sección 4
- `fuentes/examenes/` — parciales 2021-10 (P1, P16), 2021-12 (P5), 2022 (P4), 2023 (P2), 2024 (P2), 2025 (1.3 y ej. 3); globalizador 2023 (P5); finales 2020-08 (resuelto) y 2021-11 (P10)
- `fuentes/clase-preexamen/Preguntas frecuentes.docx` — preguntas #4 y #9
