# ASI — Fórmulas de memoria y práctica de multiple choice (3º parcial)

> **Formato confirmado por el docente (2026-10-29):** **12 multiple choice** de elección única, 0,5 pts cada una (6 pts), algunas aplicadas al contexto · **2 de desarrollo**, 2 pts cada una (4 pts), muy probablemente **valor ganado** y **modelo de negocios**. **No hace falta llevar el contexto.**
>
> **De memoria:** fórmulas de **valor ganado** y de **TCO** · **qué representa** ROI, TIR y el resto de los indicadores de costos · **ciclos de vida**, solo cuáles son y qué son, por encima.
>
> Fuentes: DIAP T4 Costos (láminas 8–50) y T5 Adquisiciones (láminas 28–32), apunte T1 Proyectos (págs. 6 y 12–16). El ejercicio de valor ganado desarrollado y el Canvas están en `machete-parcial3.md`.

---

## 1. Valor ganado ★★★ (desarrollo y multiple choice)

**Las cuatro bases**

| Sigla | Qué es | De dónde sale |
|---|---|---|
| **BAC** | Presupuesto total del proyecto | Σ presupuesto de las tareas |
| **PV** | Lo que **debería** estar hecho al corte, valuado en $ (BCWS) | Del **plan** (Gantt) |
| **EV** | Lo que **está** hecho, valuado a precio de **presupuesto** (BCWP) | Del **estado real** |
| **AC** | Lo que **realmente se gastó** (ACWP) | Lo da el enunciado |

**Las fórmulas** (todo arranca en **EV**)

| Indicador | Fórmula | Qué representa | Cómo se lee |
|---|---|---|---|
| **SV** (variación de tiempo) | **EV − PV** | Cuánto trabajo hice de más o de menos respecto del plan, en $ | < 0 **atrasado** · > 0 adelantado |
| **CV** (variación de costo) | **EV − AC** | Cuánto gasté de menos o de más por lo que hice | < 0 **ineficiente** · > 0 eficiente |
| SV % | SV / PV × 100 (o SV / EV × 100) | El desvío de tiempo en % | sobre lo presupuestado (PV) o sobre lo ya completado (EV) |
| CV % | CV / EV × 100 | El desvío de costo en % | |
| **SPI** | **EV / PV** | Cuánto trabajo genera cada $1 planificado | < 1 atrasado · > 1 adelantado |
| **CPI** | **EV / AC** | Cuánto trabajo genera cada $1 gastado ("grado de eficiencia") | < 1 ineficiente · > 1 eficiente |
| **ETC** | **BAC − EV** | Cuánto me **falta** hacer, a precio de presupuesto | |
| **EAC₁** | **AC + (BAC − EV)** | Costo final si lo que falta se hace **según presupuesto** (el desvío fue puntual) | |
| EAC₂ | AC + (BAC − EV) / CPI | Costo final si lo que falta se hace **al mismo rendimiento** | da lo mismo que EAC₃ |
| **EAC₃** | **BAC / CPI** | Costo final si se sigue gastando **igual que hasta ahora** | |
| **VAC** | **BAC − EAC** | Cuánto me voy a pasar (o ahorrar) al terminar | < 0 me paso del presupuesto |
| TPI | CPI × SPI | Índice total del proyecto (tiempo y costo juntos) | < 1 mal en conjunto |
| % terminado | EV / BAC × 100 | Qué parte del proyecto está hecha | |
| % gastado | AC / BAC × 100 | Qué parte del presupuesto se consumió | si % gastado > % terminado → ineficiente |

**Reglas rápidas de la cátedra:** PV > EV → atrasado · PV < EV → adelantado · AC > EV → ineficiente · AC < EV → eficiente.

**Criterios para tareas en curso** (se fijan **al inicio** del proyecto): **0%** (no la tengo en cuenta) · **100%** (la considero completa) · **20/80** (según si hay poco o mucho) · **50/50** (la considero a la mitad, el habitual).

**Ejemplo completo — Omnicanalidad al día 10** (BAC 6.000 · PV 3.100 · EV 2.400 · AC 2.900):

```
SV  = 2.400 − 3.100 = −700        → atrasado
CV  = 2.400 − 2.900 = −500        → ineficiente
SV% = −700 / 3.100  = −22,6 %     CV% = −500 / 2.400 = −20,8 %
SPI = 2.400 / 3.100 = 0,77        → por cada $1 planificado se hicieron $0,77
CPI = 2.400 / 2.900 = 0,83        → por cada $1 gastado se hicieron $0,83 de trabajo
ETC = 6.000 − 2.400 = 3.600
EAC₁ = 2.900 + 3.600 = 6.500      → VAC = −500   (si el desvío fue puntual)
EAC₃ = 6.000 / 0,83  = 7.250      → VAC = −1.250 (si sigue así)
TPI = 0,83 × 0,77    = 0,64
% terminado = 2.400 / 6.000 = 40 %    % gastado = 2.900 / 6.000 = 48 %
```

Lectura: gastó el 48% del presupuesto para hacer el 40% del proyecto; está atrasado e ineficiente.

**Trampas:** SV < 0 **no** es "gastar menos", es hacer menos de lo planeado · el PV sale del plan y el EV del estado real, nunca al revés · el AC no se calcula, lo da el enunciado.

---

## 2. TCO — Costo Total de Propiedad ★★★ (de memoria)

**Qué representa:** el costo de **poseer y operar** una solución **durante toda su vida útil**, no solo su precio de compra. La cátedra lo presenta como un método sencillo para la adquisición de soluciones, que incluye el aspecto **financiero, administrativo y operativo**. Se usa para **comparar propuestas** (en la evaluación de proveedores, junto con la capacidad financiera).

```
TCO = CIS + CA + CO + CSU

CIS (Costo Inicial de la Solución) = Ch + Cs + Cins + Ccon
      Ch   = hardware requerido
      Cs   = software requerido
      Cins = servicios iniciales de instalación
      Ccon = servicios iniciales de configuración

CA  (Costo de Administración) =
      costo anual de un ingeniero (interno o externo) × nº de ingenieros de planta
      × nº de años en funcionamiento × % de tiempo dedicado a la solución

CO  (Costo de Operación) =
      nº de incidentes promedio por año × nº de años en funcionamiento
      × costo por hora de servicio × tiempo aproximado para reparar la falla

CSU (Costo de Soporte a Usuarios) =
      nº de incidentes promedio por año × nº de años en funcionamiento
      × costo por hora de soporte × tiempo aproximado para dar el soporte
```

**Cómo no confundirlas:** **CA** es la única que va por **ingenieros y % de dedicación**. **CO y CSU** van las dos por **incidentes**: CO es **reparar la falla** (costo/hora de **servicio**) y CSU es **atender al usuario** (costo/hora de **soporte**). Todas menos el CIS se multiplican por los **años de vida**.

**Ejemplo inventado, a 3 años:**

```
CIS = 20.000 + 15.000 + 3.000 + 2.000      = 40.000
CA  = 30.000 × 1 ingeniero × 3 años × 20 % = 18.000
CO  = 10 incid. × 3 años × $50/h × 4 h     =  6.000
CSU = 10 incid. × 3 años × $30/h × 2 h     =  1.800
TCO                                        = 65.800
```

El hardware y el software (35.000) son apenas el 53% del TCO: por eso no se compara solo por precio.

**Variables del TCO del caso integral de cátedra** (para listar en desarrollo): licencias o suscripciones · implementación y parametrización · integraciones y migración · infraestructura o cloud · capacitación · soporte y mantenimiento · actualizaciones y renovaciones · administración interna · escalabilidad · **costos de salida o cambio de proveedor**.

---

## 3. Indicadores económicos: qué representa cada uno ★★

| Indicador | Fórmula | Qué representa | Conviene si | ¿Valor del dinero en el tiempo? | Ventaja / desventaja clave |
|---|---|---|---|---|---|
| **TR** — Tiempo de Recuperación | años hasta que Beneficios = Inversión | **Cuándo** recupero la inversión | menor | NO | Fácil · no ve los beneficios posteriores al recupero ni el rendimiento |
| **TPR** — Tasa Promedio de Retorno | BPA / Inversión, con BPA = Beneficio total / Vida útil | Qué **% de la inversión vuelve por año**, en promedio | mayor | NO | **Sí considera la vida útil** · no ve cuándo llegan los flujos |
| **ROI** — Retorno de la Inversión | **Beneficio neto / Inversión** | **Cuánto beneficio me da cada $ que invierto** | mayor | NO | Simple y comparable · ignora cuándo llega la plata |
| **VF** — Valor Futuro | C × (1 + i)ⁿ | Cuánto valdrá mañana la plata de hoy (**capitalizar**) | | | |
| **VA** — Valor Actual | C / (1 + i)ⁿ | Cuánto vale hoy la plata futura (**descontar**) | | | Al 10%, $1 dentro de 4 años vale $0,68 hoy |
| **VAN** — Valor Actual Neto | Σ VA de los beneficios − Inversión | **Valor neto** que se espera ganar, en $ de hoy | **VAN > 0** | SÍ | Considera tiempo y vida útil · depende de **elegir bien la tasa** |
| **TIR** — Tasa Interna de Retorno | la tasa que hace **VAN = 0** | La **tasa de rendimiento** del proyecto | **TIR > tasa de la empresa** | SÍ | Da un **%** (sirve para comparar proyectos) y no necesita tasa de descuento · supone reinvertir a la misma TIR y es difícil de calcular a mano |
| **EVA** — Valor Agregado Económico | Beneficio neto − Inversión × Costo de capital | Lo que el proyecto **aporta** después de pagar el costo del capital | EVA > 0 | | |
| **Punto de equilibrio** (emprendimiento) | Q = CF / (P − CVu) | Cuántas unidades o clientes necesito para no perder | Q alcanzable | | |

- **Beneficios = Ingresos + Costos evitados**, siempre monetizados.
- **Tasa de descuento** = costo de capital + % de riesgo. **No es la inflación.**
- **VAN y TIR van juntos:** si a la tasa de la empresa el VAN es > 0, la TIR es mayor que esa tasa. Si el VAN es < 0, la TIR es menor.
- **TR, TPR y ROI no consideran el valor del dinero en el tiempo; VAN y TIR sí.**

---

## 4. Ciclos de vida (multiple choice, por encima)

**Ciclo de vida de un proyecto** = las **fases que conectan el inicio con el fin**. No existe uno ideal. Define qué trabajo técnico se hace en cada fase, cuándo se generan los entregables y cómo se validan, quién participa y cómo se controla y aprueba cada fase. **No confundir ciclo de vida con metodología de desarrollo.**

| Ciclo | En una línea | Cuándo |
|---|---|---|
| **Cascada** (Royce, 1970) | Etapas en secuencia con revisión al final de cada una; admite retroalimentación. El más sencillo, rígido, base de los demás | Requerimientos **completos y estables desde el inicio**. Contra: un error tardío es caro y el resultado se ve recién al final |
| **Iterativo** | Varias cascadas seguidas: cada iteración entrega una versión **mejorada** del producto y el cliente la evalúa | Reducir el riesgo de malentender los requerimientos. Ej.: migrar una aplicación de a poco |
| **Por prototipos** | Iterativo donde las versiones son **prototipos** antes del producto final | Innovación o tecnología nueva o poco probada |
| **Incremental** | Construye **por módulos**: una cascada por cada funcionalidad nueva | El cliente necesita **entregas rápidas aunque sean parciales**. Si hay un error grave, se descarta solo el último incremento |
| **Espiral** (Boehm, 1988) | Ciclos repetitivos con foco en el **riesgo**: planificación → **análisis de riesgos** → implementación (prototipo) → evaluación del cliente | Mucha incertidumbre en los requerimientos |

**Iterativo vs. incremental (la trampa):** el iterativo **mejora** el mismo producto en cada vuelta; el incremental le **agrega** un módulo nuevo en cada vuelta.

La clasificación de las sugerencias de cátedra para el TP: **predictivo** (cascada) · **iterativo o incremental** · **ágil** (alta incertidumbre, prioridades que cambian) · **híbrido** (parte previsible, parte que necesita iterar).

---

## 5. Modelo de negocios (desarrollo) — recordatorio

Desarrollado con ejemplos en `machete-parcial3.md` §4 y §5. Lo esencial:

- **Orden:** Segmentos → Propuesta → Canales / Relación / Ingresos → Recursos / Actividades / Socios → Costos.
- **Propuesta de valor ↔ segmento** es lo que más pesa: segmentos **específicos** (quién, dónde, tamaño, qué le duele) y una propuesta **por segmento**, redactada como beneficio, no como producto.
- **Socios clave** = aquellos de los que **depende** el modelo (proveedor de IA, API de pagos, cloud), no los dueños.
- **Canales** = cómo llega y cómo se entera · **Relación** = marketing, Get / Keep / Grow, CAC.
- **Costos:** fijos y variables, sin repetir el mismo costo en las dos columnas.

---

## 6. Práctica: 14 preguntas de multiple choice

Elegí una sola. Respuestas al final.

**1.** Al día de corte, CV = −500 y SV = +200. El proyecto está:
a) atrasado y eficiente · b) adelantado e ineficiente · c) adelantado y eficiente · d) atrasado e ineficiente

**2.** El TCO de una solución es:
a) el precio de compra del hardware y el software · b) la inversión inicial menos los beneficios · c) el costo inicial más los de administración, operación y soporte a usuarios durante su vida útil · d) el costo anual de las licencias

**3.** ¿Qué representa la TIR?
a) la tasa que usa la empresa para descontar sus flujos · b) la tasa de descuento que hace que el VAN sea cero · c) la inflación esperada · d) el % de beneficio sobre la inversión sin considerar el tiempo

**4.** Un ROI del 40% significa que:
a) se recupera la inversión en 0,4 años · b) por cada $1 invertido se obtienen $0,40 de beneficio neto · c) el VAN es el 40% de la inversión · d) el proyecto rinde un 40% por encima de la inflación

**5.** ¿Cuál de estos indicadores **no** considera el valor del dinero en el tiempo pero **sí** la vida útil?
a) TR · b) VAN · c) TPR · d) TIR

**6.** Bancorp evalúa la Billetera Virtual con una tasa del 12% y obtiene un VAN de −12.000. Entonces:
a) la TIR es mayor al 12% · b) la TIR es menor al 12% · c) la TIR es igual al 12% · d) no se puede saber nada de la TIR

**7.** "Costo anual de un ingeniero × nº de ingenieros de planta × años en funcionamiento × % de tiempo dedicado" corresponde a:
a) CO · b) CSU · c) CIS · d) CA

**8.** BAC = 10.000, PV = 4.000, EV = 3.000, AC = 3.500. El % terminado es:
a) 30% · b) 35% · c) 40% · d) 75%

**9.** Con el mismo dato de la 8, el SPI es:
a) 1,33: adelantado · b) 0,75: atrasado · c) 0,86: ineficiente · d) 0,75: ineficiente

**10.** Con criterio 50/50, una tarea en curso con presupuesto de 800 suma al EV:
a) 0 · b) 160 · c) 400 · d) 800

**11.** El ciclo de vida que incorpora explícitamente el análisis de riesgos en cada vuelta es:
a) cascada · b) incremental · c) espiral · d) iterativo

**12.** Un banco necesita salir rápido con un módulo de transferencias y después sumar pagos e inversiones, cada uno con su propio ciclo completo. El ciclo de vida que corresponde es:
a) cascada · b) incremental · c) espiral · d) por prototipos

**13.** La tasa de descuento que se usa para calcular el VAN:
a) es la inflación anual · b) es la TIR del proyecto · c) es el costo de capital más un % de riesgo · d) es siempre el 10%

**14.** En el Canvas, los socios clave son:
a) los socios de la SRL · b) los clientes que más pagan · c) aquellos de los que depende el modelo de negocio · d) los inversores que aportan capital

---

**Respuestas**

1. **b** — SV > 0 es adelantado; CV < 0 es ineficiente.
2. **c** — TCO = CIS + CA + CO + CSU a lo largo de la vida útil. La a) es solo parte del CIS.
3. **b** — La a) es la tasa contra la que se **compara** la TIR.
4. **b** — ROI = Beneficio neto / Inversión.
5. **c** — El TR no considera la vida útil; VAN y TIR sí consideran el valor del dinero.
6. **b** — Si el VAN da negativo al 12%, la tasa que lo hace cero es menor.
7. **d** — Es la única que va por ingenieros y % de dedicación.
8. **a** — EV / BAC = 3.000 / 10.000. El 35% es el % gastado (AC / BAC).
9. **b** — SPI = EV / PV = 3.000 / 4.000. El SPI mide tiempo, no eficiencia de costo.
10. **c** — En curso cuenta la mitad.
11. **c** — Espiral (Boehm).
12. **b** — Incremental: un módulo nuevo por vuelta, cada uno con su cascada.
13. **c** — No es la inflación (lo aclara el apunte) ni la TIR.
14. **c** — Los socios de la SRL no son socios clave del Canvas.
