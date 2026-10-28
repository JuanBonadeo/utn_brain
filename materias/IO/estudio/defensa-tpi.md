# Defensa del TPI — Juntas de motor (Grupo 1, com. 402)

Guía para el coloquio final. Está armada **desde las devoluciones del profe**: cada punto que
marcó es una pregunta casi segura. Todos los números se recalcularon de forma exacta
(enumeración de bases, Big M paso a paso y Lagrange por bisección), sin copiarlos de los
documentos.

> Importes del modelo de producción en **miles de pesos**. Importes de stock en **pesos**.

---

## 0. Ficha de memoria

$$\max Z = 50X_1 + 30X_2 + 40X_3$$

| Restricción | Ecuación | En el óptimo | Precio sombra |
|---|---|---|---|
| R1 corcho (oferta) | $3X_1+2X_2+X_3 \le 600$ | 330 → **sobran 270 m²** | $u_1 = 0$ |
| R2 horas troqueladora (oferta) | $4X_1+3X_2+2X_3 \le 480$ | 480 → activa | $u_2 = 20$ |
| R3 mínimo contractual (demanda) | $X_1+X_2+X_3 \ge 150$ | 150 → activa | $u_3 = -60$ |
| R4 despacho (capacidad) | $X_1+X_2+2X_3 \le 200$ | 200 → activa | $u_4 = 30$ |

- Óptimo: $X^* = (80;\ 20;\ 50)$ lotes, $Z^* = 6600$ → **\$6.600.000 por semana**.
- Base óptima: $A_4$ (holgura del corcho), $A_1$, $A_2$, $A_3$.
- Control: $W^* = 480\cdot20 + 200\cdot30 - 150\cdot60 = 9600+6000-9000 = 6600 = Z^*$.

> Ojo con la numeración: en la **tabla Simplex** A6 es la holgura del **despacho** (R4) y A7
> el exceso del **mínimo** (R3). En el **dual** de la Etapa 2 se ordenó distinto:
> $U_3$ = despacho, $U_4$ = mínimo. Si te preguntan, aclaralo de entrada.

---

## 1. Etapa 1 — lo que van a preguntar

### 1.1 El escenario alternativo que faltó (pregunta casi segura)

El profe lo marcó como incumplido y dijo que lo dejaba "para que piensen en ese punto". Hay
que llevarlo resuelto. Los tres caen **dentro del rango de la base óptima**, así que se
resuelven sin rehacer el Simplex: $X_B' = X_B + \Delta b\cdot(\text{columna de } B^{-1})$ y
$Z' = Z^* + u_i\,\Delta b$. Los tres se verificaron resolviendo el modelo de nuevo.

| Escenario | Cambio | Nuevo plan $(X_1;X_2;X_3)$ | $Z'$ | Decisión |
|---|---|---|---|---|
| **A. Se rompe una troqueladora** | $b_2$: 480 → 440 h | (40; 60; 50) | 5800 (−800) | Se pasa producción de tapa a cárter. Conviene tercerizar o pagar horas extra si cada hora cuesta **menos de \$20.000** (hasta 40 h, para volver a 480). |
| **B. La terminal sube el mínimo** | $b_3$: 150 → 160 lotes | (40; 80; 40) | 6000 (−600) | Aceptarlo solo si la terminal compensa **al menos \$60.000 por lote** adicional (\$600.000 por semana). |
| **C. Flete tercerizado** | $b_4$: 200 → 210 | (90; 0; 60) | 6900 (+300) | Conviene si cada unidad de despacho extra cuesta **menos de \$30.000**. Ojo: 210 es el tope del rango. |

Para defender el **A** con la mecánica (columna de $A_5$ en la tabla final):
$X_1 = 80 + \Delta$, $X_2 = 20 - \Delta$, $X_3 = 50$, $X_4 = 270 - \Delta$, con $\Delta = -40$:
$X_1 = 40$, $X_2 = 60$, $X_4 = 310$. Sobra más corcho porque se fabrica menos tapa.

### 1.2 La tabla final tiene errores en la fila $Z_j$ (enterate antes que el profe)

El cuerpo de la tabla (los $y_{ij}$ y los $X_i$) está **bien**. Las filas $Z_j$ y $C_j - Z_j$
tienen tres errores:

| Columna | En el documento | Correcto | Cuenta |
|---|---|---|---|
| A6 (holgura despacho) | $Z_j = 90$, $C_j-Z_j = -90$ | $Z_j = 30$, $C_j-Z_j = \mathbf{-30}$ | $50(1)+30(-2)+40(1) = 30$ |
| A7 (exceso mínimo) | $C_j-Z_j = -M-60$ | $\mathbf{-60}$ | $C_7 = 0$, $Z_7 = 60$ → $0-60$ |
| A8 (artificial) | $C_j-Z_j = 0$ | $\mathbf{-M+60}$ | $C_8=-M$, $Z_8 = -60$ → $-M+60$ |

Por qué importa: la Etapa 2 usa $u_{\text{despacho}} = 30$, que es lo correcto, pero la tabla de
la Etapa 1 dice 90. Si el profe pregunta por la diferencia: **"Fue un error de cuenta en la fila
$Z_j$ de A6; el valor correcto es 30 y se verifica con $W^* = Z^*$: con 90 el dual daría 18.600,
no 6.600."** Con el mismo argumento cae la interpretación de la Etapa 1 ("\$90.000 por unidad
de despacho"): es \$30.000.

Regla para A7 y A8: la variable de exceso tiene costo 0, así que su $C_j - Z_j$ **no lleva M**. La
M aparece en la artificial: su $C_j - Z_j$ es la del exceso con signo cambiado, más $-M$.

### 1.3 Las iteraciones (te pueden pedir que expliques cada una)

Criterio: entra la de mayor $C_j - Z_j$ positivo; sale la de menor cociente $X_i / y_{ik}$.

| Iteración | Base | Solución | $Z$ | Entra / sale | Lectura |
|---|---|---|---|---|---|
| I0 | A4, A5, A8, A6 | holguras + artificial = 150 | $-150M$ | entra **A1** ($50+M$), sale **A5** (cociente 120) | Arranca con la artificial: el mínimo todavía no se cumple. Tapa es la que más aporta y la limita la troqueladora (480/4 = 120). |
| I1 | A4, A1, A8, A6 | $X_1 = 120$, artificial = 30 | $6000-30M$ | entra **A3** ($15+M/2$), sale **A6** (cociente 53,3) | Con todas las horas en tapa solo hay 120 lotes: faltan 30 para el mínimo. Entra múltiple, que da más lotes por hora. |
| I2 | A4, A1, A8, A3 | $X_1 = 93,3$; $X_3 = 53,3$; artificial = 3,3 | $6800-3,3M$ | entra **A2** ($M/6-10$), sale **A8** (cociente 20) | Horas y despacho agotados y todavía faltan 3,3 lotes. Solo cárter puede completar el mínimo. |
| I3 | A4, A1, A2, A3 | (80; 20; 50), sobran 270 m² | **6600** | — óptimo | Todos los $C_j-Z_j \le 0$ y la artificial salió de la base: solución factible y óptima, única (ninguna no básica con $C_j-Z_j = 0$). |

Detalle fino: en I2 el $C_j - Z_j$ de cárter es **negativo en pesos** (−10) pero lleva $+M/6$:
cárter entra solo porque hace falta para cumplir el contrato, no porque convenga.

### 1.4 Otras preguntas de modelado

- **¿Por qué una restricción de mínimo queda activa en un problema de máximo?** Porque el mínimo
  obliga a fabricar **cárter**, el que menos rinde por hora de troquelado (30/3 = 10 por hora,
  contra 12,5 de tapa y 20 de múltiple). Si el mínimo bajara a 140, el óptimo deja de fabricar
  cárter: (93,3; 0; 53,3) con $Z = 6800$. Por eso el precio sombra es **negativo**: cada lote
  más de contrato cuesta \$60.000.
- **El texto dice "mínimo de Juntas de Tapa de Cilindros" pero la restricción suma las tres.**
  Es un error de redacción del documento: el contrato es por **150 lotes totales** (así está en
  la Etapa 2). Admitirlo directo.
- **¿Por qué $X_3$ pesa 2 en el despacho?** ⚠️ **Acordar la respuesta con el grupo antes de la
  defensa.** No está justificado en los documentos. Una justificación razonable es que la junta
  de múltiple ocupa el doble de volumen de embalaje por lote.
- **"Las restricciones deben ser de oferta y demanda."** R1 y R2 son oferta (recursos propios),
  R3 es demanda (contrato) y R4 es capacidad de salida. El modelo fue aprobado por formulario
  antes de seguir.

---

## 2. Etapa 2 — lo que van a preguntar

### 2.1 El dual (en el documento estaba mal; en el video bien)

Pedirán escribirlo en el pizarrón. Dos formas equivalentes:

**Forma directa** (el signo de cada variable dual sale del tipo de restricción del primal):

$$\min W = 600u_1 + 480u_2 + 150u_3 + 200u_4$$

$$\begin{aligned}
3u_1 + 4u_2 + u_3 + u_4 &\ge 50 \quad (X_1)\\
2u_1 + 3u_2 + u_3 + u_4 &\ge 30 \quad (X_2)\\
u_1 + 2u_2 + u_3 + 2u_4 &\ge 40 \quad (X_3)\\
u_1, u_2, u_4 \ge 0, &\quad u_3 \le 0
\end{aligned}$$

**Forma simétrica:** se pasa R3 a $\le$ multiplicando por −1 ($-X_1-X_2-X_3 \le -150$). Queda
$u_3' \ge 0$ y en la función objetivo aparece $-150u_3'$, con $u_3' = -u_3 = 60$.

Reglas para justificar cada cosa:
- Primal max → dual min. Los $b_i$ del primal pasan a ser los coeficientes de $W$, y los $c_j$
  los términos independientes del dual.
- Una restricción dual por cada **variable** primal, de tipo $\ge$ porque $X_j \ge 0$.
- Las **columnas** del primal pasan a ser las **filas** del dual.
- $u_i \ge 0$ para las $\le$ de un max; $u_i \le 0$ para la $\ge$.

Solución: $u^* = (0;\ 20;\ -60;\ 30)$ en el orden R1, R2, R3, R4. Se lee en la fila
$C_j - Z_j$ de la tabla final, columnas A4, A5, A7 y A6, con el signo cambiado.

**Holguras complementarias** (sirven de control):
- $X_1, X_2, X_3 > 0$ → las tres restricciones duales se cumplen **con igualdad**.
- Sobra corcho ($X_4 = 270 > 0$) → $u_1 = 0$.
- $u_2, u_3, u_4 \ne 0$ → R2, R3 y R4 están activas.

### 2.2 "Faltó considerar los costos marginales"

En el apunte, *costo marginal* es sinónimo de precio sombra. Como los precios sombra estaban
bien, lo más probable es que el profe se refiera a la **otra mitad del dual**: las holguras de
las restricciones duales, es decir, el costo de oportunidad de cada producto. Hay que saber
decirlo así:

> "Siempre que una actividad opere a nivel positivo, el costo marginal de los recursos que
> consume es igual al beneficio que aporta." *(PLC5 §5.6)*

| Producto | Recursos valorizados a precio sombra | $c_j$ | Holgura dual |
|---|---|---|---|
| Tapa | $0\cdot3 + 20\cdot4 - 60\cdot1 + 30\cdot1 = 50$ | 50 | 0 |
| Cárter | $0\cdot2 + 20\cdot3 - 60\cdot1 + 30\cdot1 = 30$ | 30 | 0 |
| Múltiple | $0\cdot1 + 20\cdot2 - 60\cdot1 + 30\cdot2 = 40$ | 40 | 0 |

Los tres se fabrican, así que cada uno "paga" exactamente lo que consume en recursos escasos:
ninguno sobra ni falta, y por eso los tres tienen costo reducido 0.

Dos matices que conviene decir:
- El precio sombra es lo **máximo que conviene pagar por encima del costo actual**, porque
  $c_j$ ya es beneficio neto. Una hora de troqueladora conviene si su sobrecosto es menor a
  \$20.000.
- Solo vale **de a un cambio por vez** y **dentro del rango** (tabla de 2.4).

### 2.3 Rango de $C_2$: la notación que mezclaron

Con $C_2 = 30 + \Delta$, la fila de $A_2$ en la tabla final da:
$-20 + \Delta \le 0$, $-60 + 6\Delta \le 0$, $-30 + 2\Delta \le 0$ → $\Delta \le 10$.

Escrito bien, **separando las dos variables**:

$$-\infty < \Delta C_2 \le 10 \quad\Longrightarrow\quad -\infty < C_2 \le 40$$

El error del documento fue escribir algo como "$\Delta C_2 \le 40$" o mezclar $\Delta$ y $C_2$ en
el mismo intervalo. $\Delta$ es la **variación** y $C_2$ el **coeficiente**: se despeja primero
$\Delta$ y recién después se suma 30.

Pregunta trampa: **¿por qué no hay cota inferior?** Porque todos los $y_{2j}$ de las no básicas
son negativos (−1, −6, −2), así que bajar $C_2$ nunca vuelve positivo un $C_j - Z_j$. La
explicación económica: **sin cárter no se puede cumplir el contrato**. Con $X_2 = 0$, R3 y R4
obligan a $X_3 \le 50$ y R3 y R2 a $X_3 \ge 60$: no hay solución. Cárter se fabrica aunque pierda
plata.

Rangos de todos los $c_j$ (por si te piden otro):

| Coef. | Rango de $\Delta$ | Rango del coeficiente |
|---|---|---|
| $C_1 = 50$ | $-15 \le \Delta \le +\infty$ | $35 \le C_1 < \infty$ |
| $C_2 = 30$ | $-\infty < \Delta \le 10$ | $-\infty < C_2 \le 40$ |
| $C_3 = 40$ | $-30 \le \Delta \le +\infty$ | $10 \le C_3 < \infty$ |

Fuera del rango, con $C_2 = 42$: el nuevo óptimo es (0; 140; 30) y $Z = 7080$, verificado.

### 2.4 Rango de $b_2$: el error en las inecuaciones

Con $b_2 = 480 + \Delta$, la columna de $A_5$ en la tabla final es $(-1;\ 1;\ -1;\ 0)$ en el
orden A4, A1, A2, A3:

$$\begin{aligned}
X_4 &= 270 - \Delta \ge 0 &\Rightarrow&\ \Delta \le 270\\
X_1 &= 80 + \Delta \ge 0 &\Rightarrow&\ \Delta \ge -80\\
X_2 &= 20 - \Delta \ge 0 &\Rightarrow&\ -\Delta \ge -20 \Rightarrow \boxed{\Delta \le 20}\ \text{(se da vuelta la desigualdad)}\\
X_3 &= 50 \ge 0 &&\ \text{siempre}
\end{aligned}$$

Intersección: $-80 \le \Delta \le 20$ → $400 \le b_2 \le 500$.

El error típico, y casi seguro el del documento, es multiplicar o dividir por −1 sin dar vuelta
la desigualdad: $20 - \Delta \ge 0$ queda mal como $\Delta \ge 20$. Para la intersección: entre
cotas superiores manda la **menor** (20 < 270), y entre inferiores la **mayor**.

Rangos de todos los $b_i$:

| Recurso | $u_i$ | Rango de $b_i$ |
|---|---|---|
| Corcho | 0 | $330 \le b_1 < \infty$ |
| Horas | 20 | $400 \le b_2 \le 500$ |
| Mínimo contractual | −60 | $146,7 \le b_3 \le 170$ |
| Despacho | 30 | $150 \le b_4 \le 210$ |

Dato lindo: el piso de 146,7 del mínimo contractual es exactamente la solución de la iteración
I2 (93,3 + 53,3).

### 2.5 Producto nuevo (bomba de agua)

Costo de oportunidad: $0\cdot2 + 20\cdot3 + 30\cdot2 - 60\cdot1 = 60$. Costo reducido:
$45 - 60 = -15$ → no conviene. Pregunta probable: **¿a qué precio conviene?** Con un beneficio
de **más de \$60.000 por lote** entra a la base, y hay que reoptimizar para saber cuánto
fabricar.

### 2.6 PEM (mochila sobre el corcho sobrante)

El profe lo elogió. Preguntas probables:
- **¿Por qué la relajación es cota superior?** Porque la relajación tiene más soluciones
  posibles que el problema entero, así que su óptimo no puede ser peor.
- **¿Cuándo se poda?** Cuando la cota de la rama es ≤ la mejor solución entera ya encontrada
  (345). Las dos ramas de $Y_3 = 1$ dan 332 y 344.
- **¿Los pedidos no consumen horas ni despacho, que están agotados?** Es el supuesto del
  submodelo: se atienden con capacidad aparte (por ejemplo, retiro por el cliente o un turno
  extra). Si las consumieran, habría que meterlos en el modelo original como variables binarias
  (opción B).

### 2.7 Conclusión de la Etapa 2 (faltó en el documento; tenerla para decir)

> Las horas de troqueladora (\$20.000/h, válido entre 400 y 500 h) y el despacho (\$30.000 por
> unidad, entre 150 y 210) son los cuellos de botella: ampliar conviene solo si el sobrecosto es
> menor que el precio sombra. El corcho no limita (precio sombra 0, sobran 270 m²), y ese
> sobrante se aprovecha con los pedidos 1, 2 y 4 (+\$345.000 por semana). El contrato mínimo
> cuesta \$60.000 por lote porque obliga a fabricar cárter. El plan aguanta cualquier baja de la
> ganancia del cárter y una suba hasta \$40.000. La bomba de agua no conviene salvo que deje más
> de \$60.000 por lote.

---

## 3. Etapa 3 — la "inconsistencia inherente" del stock aleatorio

### 3.1 La lectura más probable: el stock de seguridad no entra en el depósito

El lote restringido (1.098 m² de corcho + 255 L de sellador) se calculó para llenar **exactamente**
los 60 m³. Después, el modelo aleatorio le suma 42 m² de stock de seguridad. Cuando llega un
pedido, el stock máximo de corcho es **Q + SS**, no Q:

$$0,05\cdot(1098 + 42) + 0,02\cdot255 = 57,0 + 5,1 = \mathbf{62,1\ m^3} > 60\ m^3$$

Cada modelo está bien por separado, pero juntos la política no entra en el depósito. Eso es lo
que el profe llamó resultado no integral.

**La corrección:** reservar el espacio del colchón y volver a resolver Lagrange con lo que queda:

$$0,05\,Q_1 + 0,02\,Q_2 \le 60 - 0,05\cdot41,6 = 57,92\ m^3$$

| | Original | **Integrado** |
|---|---|---|
| λ | \$5.813/m³ | **\$6.775/m³** |
| Lote corcho | 1.098 m² | **1.059 m²** |
| Lote sellador | 255 L | **249 L** |
| Espacio con SS | 62,1 m³ ✗ | **60,0 m³** ✓ |
| Pedidos de corcho por año | 15,6 (cada 23 días) | 16,2 (cada 22,5 días) |
| Costo anual conjunto | \$46.306.000 | \$46.319.000 (**+\$13.000**) |
| Punto de pedido | 512 m² | 512 m² (no cambia: depende de la demanda en el plazo de entrega) |

Conclusión para decir: *"Integrando el stock de seguridad con la restricción de espacio, el lote
baja a 1.059 m² y se pide cuando quedan 512 m². Cuesta solo \$13.000 más por año y la política
entra en el depósito."* Con el mismo razonamiento, la ampliación para habilitar el descuento
pasa de ≈106 a **≈108 m³** (2.000 + 42 m² de corcho + 309 L de sellador).

### 3.2 Otras lecturas posibles (tener respuesta igual)

- **Los pedidos especiales de la Etapa 2.** Si se aceptan, el corcho pasa de 330 a **600 m² por
  semana**: exactamente el tope del proveedor. R1 queda activa y el corcho **deja de ser
  gratis** (su precio sombra ya no sería 0). La demanda anual sube a 31.200 m² y la del plazo de
  entrega a ≈855 m². El depósito sigue mandando: corcho ≈1.117 m² sin SS y ≈1.078 m² con SS. La
  conclusión de fondo no cambia.
- **Demanda aleatoria contra un plan de producción fijo.** La Etapa 1 fija 330 m² por semana, y
  el modelo aleatorio dice que el consumo varía. Respuesta: el plan es el **valor medio**
  planificado y lo que varía semana a semana es el mix real de pedidos. El desvío de 8 m² por día
  es un supuesto, y el SS crece en proporción a él.

### 3.3 Fórmulas de stock que pueden pedir de memoria

- Lote óptimo: $Q^* = \sqrt{\dfrac{2DL}{C\,i}}$ → corcho 1.485 m², sellador 309 L.
- Costo total con descuento: $CT = DC + \dfrac{D}{Q}L + \dfrac{Q}{2}C\,i$. La compra $DC$
  entra porque el precio depende de Q. En Lagrange, con precio fijo, es constante y no afecta el
  lote.
- Lote con restricción: $Q_j = \sqrt{\dfrac{2D_jL_j}{C_j\,i + 2\lambda v_j}}$. λ es lo que bajaría
  el costo anual con 1 m³ más de depósito.
- Aleatorio: $SS = z\,\sigma_d\sqrt{LT} = 1,645\cdot8\sqrt{10} = 41,6$ m²; $PP = \bar d\,LT + SS = 470,1 + 41,6 = 512$ m².
- Mantener el SS cuesta $41,6\cdot2500\cdot0,28 \approx$ \$29.000 por año: es el precio del 95 %
  de ciclos sin faltante.

---

## 4. Errores propios para admitir sin que te los saquen

1. Tabla final de la Etapa 1: filas $Z_j$ de A6, A7 y A8 (ver 1.2).
2. Interpretación de la Etapa 1: "despacho \$90.000" → es **\$30.000**.
3. Texto de R3: dice "tapa de cilindros", pero el contrato es por **lotes totales**.
4. Etapa 2: portada y pie de página con "Etapa 1" y fecha de junio. Faltó la sección de
   conclusiones.
5. Etapa 3: el stock de seguridad no estaba integrado con el depósito (ver 3.1).

La actitud que suma: **reconocer el error, dar el valor correcto y mostrar cómo se verifica**.
El criterio de evaluación 4 es "Evolución: correcciones entre etapas".

## 5. Checklist para la noche anterior

- [ ] Repetir sin mirar la ficha del punto 0.
- [ ] Decir el escenario alternativo A en 30 segundos, con números.
- [ ] Escribir el dual en las dos formas.
- [ ] Hacer el rango de $b_2$ dando vuelta la desigualdad.
- [ ] Decir la frase de costo marginal y la tabla de los tres productos.
- [ ] Explicar por qué no hay cota inferior para $C_2$ y por qué el mínimo tiene precio negativo.
- [ ] Explicar Q + SS > depósito y la corrección a 1.059 m².
- [ ] Acordar con el grupo la justificación del 2 en $2X_3$ del despacho.
