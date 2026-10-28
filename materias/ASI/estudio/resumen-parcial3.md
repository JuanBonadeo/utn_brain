# ASI — Resumen para el 3º Parcial (U5 Proyectos + U6 Emprendedorismo)

> **Contexto del examen.** Proyectos: **Bancorp** y sus **proyectos del 1er año**. Emprendedorismo: **tema bancario, pero desde afuera**: somos una startup que le vende al banco (o a otros) un producto o servicio. *No somos el banco.*
>
> **Fuentes.** [consulta] = clase de consulta del 2026-10-28 (`fuentes/Parcial3/`) · [wiki] = `ASI.md`, Unidades 5 y 6 · [cátedra] = ejercicio Pinaires de valor ganado · [guía] = guías de U5/U6 que pasaste · [general] = conocimiento mío, no está en tu material.

---

## 0. Qué se toma: prioridades

| Prioridad | Tema | Qué te van a pedir (probable) |
|---|---|---|
| ★★★ | **Valor ganado** | Tabla con BAC, PV, EV, AC → **SV y CV** (estas fórmulas sí van de memoria) + interpretar: ¿atrasado/adelantado? ¿eficiente/ineficiente? |
| ★★★ | **Canvas parcial** | Detallar **algunos bloques** para una idea dada, en hoja. Lo central: **segmento ↔ propuesta de valor** |
| ★★ | **Leer Gantt y red** | No se dibujan ("no hay tiempo"), pero hay que **justificar**: camino crítico, holguras, qué pasa si se atrasa X |
| ★★ | **Rentabilidad** | Qué mide y para qué sirve TR, TPR, VA/VF, VAN, TIR, ROI (posible multiple choice). Ventajas y desventajas |
| ★ | Lean Startup | Ciclo, MVP, pivot, desarrollo de clientes, ajuste producto-mercado |
| ★ | Adquisiciones | TCO, compra/alquiler/leasing, quién asume el riesgo, RFI vs. RFP |
| ★ | Acta y objetivos | Para el proyecto de Bancorp asignado (la guía la pone primera; la consulta **no la nombró**) |

---

## 1. Los proyectos de Bancorp del 1er año [wiki]

Tenelos a mano: el enunciado asigna uno, y de ahí salen las tareas del Gantt.

| # | Proyecto | En una línea |
|---|---|---|
| 1 | **Billetera Virtual Propia** | App para no bancarizados y jóvenes: cuenta 100% digital, onboarding biométrico (RENAPER), QR interoperable, transferencias, FCI para saldos |
| 2 | **Omnicanalidad** | Home Banking web + App con la misma lógica de negocio; operación empezada en web y terminada en el celular; **token unificado** |
| 3 | **Copiloto con IA generativa** | LLM privado entrenado con circulares del BCRA, manuales de fraude, políticas de crédito y procedimientos de la Mesa de Ayuda, para el personal de sucursal |
| 4 | **Employee Experience** | Portal del empleado: recibos con firma digital, licencias, evaluaciones y e-learning normativo |

Áreas de TI que podés nombrar (no inventes): **[01]** Infraestructura y Redes · **[02]** Ciberseguridad y Fraude (CISO, SOC) · **[03]** Ingeniería de Software · **[04]** Ops. TI y Core · **[05]** PMO · **[06]** Mesa de Ayuda. Gerencias: Banca Minorista, Banca Empresas, Adm. y Finanzas, Capital Humano, Operaciones Bancarias, TI e Innovación, Cumplimiento y Riesgos.

---

## 2. Red de tareas y Gantt: leerlos y justificar

### 2.1 El nodo

```
┌──────┬──────────┬──────┐
│  IT  │ Duración │  FT  │   ← lo más temprano
├──────┴──────────┴──────┤
│         Tarea          │
├──────┬──────┬────┬─────┤
│ ITa  │  HT  │ HL │ FTa │   ← lo más tarde + holguras
└──────┴──────┴────┴─────┘
```

### 2.2 Convención de días: usá la del profe [consulta]

- La primera tarea arranca el **día 1**.
- **FT = IT + duración − 1.** Ejemplo: empieza el lunes (1) y dura 2, termina el martes (2).
- La sucesora arranca **al día siguiente**. Con varias predecesoras, el día siguiente a la que **termina más tarde** (máximo).
- La pasada hacia atrás usa la misma lógica: FTa = (menor ITa de las sucesoras) − 1.

> ⚠️ **Contradicción entre fuentes.** La guía de U5 y el caso de cátedra de la wiki usan días desde **0** con FT = IT + duración. El profe dijo que la herramienta arranca en 0, "pero es lo mismo". Las holguras y el camino crítico salen iguales. Elegí una convención y no la mezcles; si el enunciado trae la red hecha, **respetá la que traiga**.

### 2.3 Holguras

| | Qué es | Cálculo (días desde 1) |
|---|---|---|
| **HT** (total) | Cuánto se puede demorar la tarea **sin mover el fin del proyecto** | ITa − IT |
| **HL** (libre) | Cuánto se puede demorar **sin mover el IT de ninguna sucesora** | (menor IT de las sucesoras) − FT − 1 |

- Siempre **HL ≤ HT**. El profe: "me interesa más la holgura de la izquierda", es decir, la **total**.
- **Camino crítico** = tareas con **HT = 0**. Si una se atrasa, se atrasa el proyecto. **Puede haber más de uno.**
- La duración del proyecto **no es la suma de las duraciones**: las ramas paralelas se solapan.

### 2.4 Para qué sirven las holguras: nivelación de recursos

- **Problema:** si todo arranca en su IT, hay días con pico de gente (4,25 personas en el ejemplo del profe) y días casi vacíos. Contratar para dos días es caro.
- **Solución:** se corren las tareas **no críticas** dentro de su holgura hasta que la carga queda pareja (2,5 personas por día en su ejemplo).
- **Consecuencia:** la tarea que consume toda su holgura **pasa a ser crítica**, y pueden aparecer **nuevos caminos críticos**. El proyecto dura lo mismo, pero sube el riesgo de atraso.

### 2.5 Ejemplo Bancorp — Proyecto 2: Omnicanalidad

| Tarea | Descripción | Pred. | Dur. | Ppto. (USD) |
|---|---|---|---|---|
| A | Relevamiento de Home Banking y App ([03] + Banca Minorista) | — | 3 | 600 |
| B | Diseño de la arquitectura de API única ([03] arquitectos) | A | 4 | 800 |
| C | RFI/RFP del proveedor de token unificado ([02] + Compras) | A | 5 | 500 |
| D | Desarrollo del backend unificado ([03]) | B | 6 | 1.500 |
| E | Integración del token unificado ([02] + [03]) | B, C | 4 | 900 |
| F | Pruebas integrales y de seguridad ([02] SOC) | D, E | 3 | 700 |
| G | Capacitación de la Mesa de Ayuda y de sucursales ([06]) | E | 2 | 400 |
| H | Puesta en producción ([04]) | F, G | 2 | 600 |

**Resolución** (días desde 1):

```
Tarea  Dur  IT  FT  ITa  FTa  HT  HL
A       3    1   3   1    3    0   0   ← crítica
B       4    4   7   4    7    0   0   ← crítica
C       5    4   8   5    9    1   0
D       6    8  13   8   13    0   0   ← crítica
E       4    9  12  10   13    1   0
F       3   14  16  14   16    0   0   ← crítica
G       2   13  14  15   16    2   2
H       2   17  18  17   18    0   0   ← crítica

Duración: 18 días     Camino crítico: A → B → D → F → H
```

Cómo se justifica cada número:

- **E** arranca el 9 porque espera a B (termina el 7) y a C (termina el 8): manda **la que termina más tarde**.
- **C** tiene HT = 1 pero **HL = 0**: si se atrasa 1 día no atrasa el proyecto, pero sí atrasa a E. Esa holgura la **comparten** C y E. Si C la consume, E queda crítica.
- **G** tiene HT = HL = 2: es la única holgura "gratis", porque moverla no afecta a nadie. Es la primera candidata para nivelar. Si se corre a los días 15–16, queda **crítica**.

**Gantt** (█ crítica · ▒ no crítica · ┃ corte al final del día 10):

```
Tarea   1  2  3  4  5  6  7  8  9 10 ┃ 11 12 13 14 15 16 17 18
A*      █  █  █  ·  ·  ·  ·  ·  ·  · ┃  ·  ·  ·  ·  ·  ·  ·  ·
B*      ·  ·  ·  █  █  █  █  ·  ·  · ┃  ·  ·  ·  ·  ·  ·  ·  ·
C       ·  ·  ·  ▒  ▒  ▒  ▒  ▒  ·  · ┃  ·  ·  ·  ·  ·  ·  ·  ·
D*      ·  ·  ·  ·  ·  ·  ·  █  █  █ ┃  █  █  █  ·  ·  ·  ·  ·
E       ·  ·  ·  ·  ·  ·  ·  ·  ▒  ▒ ┃  ▒  ▒  ·  ·  ·  ·  ·  ·
F*      ·  ·  ·  ·  ·  ·  ·  ·  ·  · ┃  ·  ·  ·  █  █  █  ·  ·
G       ·  ·  ·  ·  ·  ·  ·  ·  ·  · ┃  ·  ·  ▒  ▒  ·  ·  ·  ·
H*      ·  ·  ·  ·  ·  ·  ·  ·  ·  · ┃  ·  ·  ·  ·  ·  ·  █  █
```

**Leer el Gantt al corte.** Lo que queda **a la izquierda** de la línea debería estar terminado. Lo que la línea **corta** está en curso según el plan. Lo que queda **a la derecha** todavía no debería haber empezado.

---

## 3. Valor Ganado ★★★

### 3.1 Qué es

Es una técnica de **seguimiento**. Responde dos preguntas: si el proyecto va **atrasado o adelantado** (tiempo) y si **gasta de más o de menos** (costo). Pasa todo a plata "para unificar" y poder comparar.

| Sigla | Qué es | De dónde sale |
|---|---|---|
| **BAC** | Presupuesto total | Suma del presupuesto de todas las tareas |
| **PV** | Lo que **según el plan** tendría que estar hecho al corte, en $ | Del **Gantt** |
| **EV** | Lo que **realmente** está hecho, valuado a precio de **presupuesto** | De la columna **estado real** |
| **AC** | "La plata que realmente gasté, lo que saqué de la billetera" | Lo da el enunciado |

### 3.2 Fórmulas (SV y CV de memoria) [consulta]

| Indicador | Fórmula | > 0 | < 0 |
|---|---|---|---|
| **SV** (variación de tiempo) | **EV − PV** | adelantado | **atrasado** |
| **CV** (variación de costo) | **EV − AC** | eficiente (gasta menos) | **ineficiente** (gasta de más) |
| SPI | EV / PV | > 1 adelantado | < 1 atrasado |
| CPI | EV / AC | > 1 eficiente | < 1 ineficiente |
| EAC | BAC / CPI | costo final estimado si se sigue gastando igual | |
| VAC | BAC − EAC | | < 0: se va a pasar del presupuesto |

**Truco:** las dos fórmulas arrancan con **EV**. Lo que hice se compara contra lo que **planeé** (PV, tiempo) y contra lo que **gasté** (AC, costo).

> SV < 0 **no** significa gastar menos: "es que estoy haciendo menos". Mide **tiempo**, expresado en plata.

### 3.3 Criterio para tareas en curso

Se define **al comienzo del proyecto** y queda fijo, para comparar "naranja con naranja":

| Criterio | Tarea en curso vale |
|---|---|
| 0% | nada, como si no hubiera empezado |
| 100% | todo, como si estuviera terminada |
| 20/80 | 20% o 80% según haya avanzado poco o mucho |
| **50/50** | **la mitad: el que se usa normalmente** |

Terminada = 100% · en curso = 50% · no iniciada = 0.

### 3.4 La planilla [cátedra]

Es el formato de la resolución de Pinaires. Armala así en la hoja:

```
Tarea │ Presup. │ Según planificado │ $ plan │ Estado real │ $ real
──────┼─────────┼───────────────────┼────────┼─────────────┼───────
  A   │   ...   │ Finalizada        │ 100%   │ ...         │ ...
  ...
──────┴─────────┴───────────────────┴────────┴─────────────┴───────
 BAC = Σ presup.             PV = Σ $ plan           EV = Σ $ real
 AC = (dato)    SV = EV − PV  →  ...      CV = EV − AC  →  ...
```

Pasos:

1. Sumar los presupuestos: **BAC**.
2. En el Gantt, trazar el **corte** (al **final** del día indicado) y leer qué estado **debería** tener cada tarea: completa "Según planificado" y "$ plan". La suma es el **PV**.
3. Con la tabla de ejecución del enunciado, completar "Estado real" y "$ real". La suma es el **EV**.
4. Anotar el **AC** y calcular SV y CV.
5. **Interpretar con una frase.** Si no interpretás, perdés puntos.

### 3.5 Ejemplo resuelto — Omnicanalidad, corte al final del día 10, AC = USD 2.900

Estado real informado: A y B finalizadas; C en curso; D en curso; E, F, G y H no iniciadas.

```
Tarea  Presup.  Según plan    $ plan   Estado real   $ real
  A      600    Finalizada      600    Finalizada      600
  B      800    Finalizada      800    Finalizada      800
  C      500    Finalizada      500    En curso        250
  D    1.500    En curso        750    En curso        750
  E      900    En curso        450    No iniciada       0
  F      700    No iniciada       0    No iniciada       0
  G      400    No iniciada       0    No iniciada       0
  H      600    No iniciada       0    No iniciada       0
─────────────────────────────────────────────────────────
BAC = 6.000          PV = 3.100           EV = 2.400
```

```
SV  = EV − PV = 2.400 − 3.100 = −700   → ATRASADO
CV  = EV − AC = 2.400 − 2.900 = −500   → INEFICIENTE (gasta de más)
SPI = 2.400 / 3.100 ≈ 0,77    CPI = 2.400 / 2.900 ≈ 0,83
EAC = 6.000 / 0,83 ≈ 7.250    VAC = 6.000 − 7.250 = −1.250
```

**Interpretación (así se escribe):** "El proyecto está **atrasado** (SV = −700: se hizo USD 700 menos de lo planificado) y es **ineficiente** (CV = −500: lo hecho costó USD 500 más de lo presupuestado). Si mantiene esta eficiencia, terminará costando unos USD 7.250, 1.250 por encima del presupuesto."

**Justificación con la red (lo que suma puntos):**

- C debía terminar el día 8 y sigue en curso. Tenía HT = 1 y ya la consumió.
- Por eso **E no pudo arrancar** (depende de B **y** de C). E tenía HT = 1: si arranca después del día 10 **atrasa todo el proyecto**. E y C pasaron a ser críticas: hay **dos caminos críticos**.
- Acción: reasignar gente a C/E (por ejemplo, sacar recursos de G, que tiene holgura 2) o negociar con el proveedor del token.

### 3.6 Ejercicio de la cátedra (Pinaires, corte día 20, AC = U$2.500) [cátedra]

Resultado oficial: **BAC = 8.100 · PV = 2.400 · EV = 2.300 · CV = −200 · SV = −100** → levemente atrasado e ineficiente.

Detalle útil: la tarea C estaba planificada como finalizada y **no se inició**, mientras que I y K estaban planificadas como no iniciadas y **estaban en curso**. **Hay tareas adelantadas dentro de un proyecto atrasado.** El SV es el neto.

### 3.7 Complicaciones típicas para comentar [guía]

- **Tarea crítica atrasada:** atrasa el proyecto entero.
- **Dependencia violada:** una tarea en curso cuya predecesora no terminó.
- Una tarea que debía haber empezado y no empezó: consume holgura y se vuelve crítica.
- **Distorsión del 50/50:** una tarea recién empezada infla el avance.
- **AC alto con EV bajo:** se gasta más de lo que se avanza.
- **Dependencias externas** (proveedor, aprobación del CAB, auditoría).

---

## 4. Rentabilidad: ¿conviene el proyecto o el emprendimiento? ★★

### 4.1 Para qué

Como gerente de sistemas, tenés que **defender tu proyecto ante la dirección** frente a otros que compiten por la misma plata. Para eso, los beneficios se **monetizan**:

**Beneficios = ingresos nuevos + costos evitados** (multas evitadas, fraudes evitados, horas de soporte liberadas, menos reprocesos). "Mejora la gestión" no es un beneficio evaluable.

### 4.2 Indicadores: qué mide cada uno

| Indicador | Qué mide | Regla | Considera el valor del dinero en el tiempo | Ventaja | Desventaja |
|---|---|---|---|---|---|
| **TR** (Tiempo de Recupero) | **Cuándo** se recupera la inversión (beneficios acumulados = inversión) | menor, mejor | **No** | Fácil de calcular y entender | Ignora lo que pasa **después** del recupero; ignora que la plata rinde (un plazo fijo podría rendir más) |
| **TPR** (Tasa Promedio de Retorno) | Beneficio promedio anual / inversión, en **%** | mayor, mejor | **No** | Fácil; **considera la vida útil** | Ignora cuándo llegan los flujos |
| **VF** (Valor Futuro) | Cuánto valdrá **mañana** la plata de hoy (capitalizar) | — | Sí | — | — |
| **VA** (Valor Actual) | Cuánto vale **hoy** la plata futura (descontar) | — | Sí | Permite comparar en un mismo momento | — |
| **VAN** | VA de los beneficios − VA de la inversión, en **$** | **VAN > 0 → conviene** | **Sí** | Usa la vida útil y el valor del dinero | Depende de elegir bien la **tasa de descuento** |
| **TIR** | La **tasa** que hace VAN = 0: el rendimiento propio del proyecto | **TIR > tasa exigida → conviene**; mayor, mejor | **Sí** | Es una tasa, así que se compara fácil entre proyectos. "Importantísima para defender un proyecto" | (general) Con flujos raros puede dar varias tasas |
| **ROI** | Cuánto se gana por cada $ invertido: (beneficio − inversión) / inversión | mayor, mejor | No (en su forma simple) | Muy intuitivo | No dice **cuándo** |
| **EVA** [guía] | Ganancia después de pagar el costo de **todo** el capital | EVA > 0 → se creó valor | Sí | | |

- **"La plata trabaja."** Un millón hoy vale más que un millón dentro de cuatro años. Al 10% anual, $1 dentro de 4 años vale **$0,68 hoy**.
- **Tasa de descuento = costo de capital + % de riesgo.** No confundirla con la inflación.
- **Los más importantes para el profe:** ROI, VA/VAN y TIR, "que son los que sirven para comparar proyectos", con sus ventajas y desventajas.
- **Pregunta en una línea:** TR → ¿**cuándo**? · TPR/ROI → ¿**cuánto rinde**? · VAN → ¿**cuánto valor crea hoy**? · TIR → ¿**a qué tasa** rinde?
- **Imperativo legal** (por ejemplo, una norma del BCRA): no se decide si se hace, se hace al **menor costo**. El beneficio son las sanciones evitadas.

### 4.3 Ejemplo — Proyecto 3 de Bancorp (Copiloto IA)

Inversión USD 100.000. Beneficio de USD 40.000 por año (horas de plataforma liberadas + menos consultas a la Mesa de Ayuda [06] + menos errores operativos). Vida útil de 4 años. Tasa exigida del 15%.

```
TR  = 100.000 / 40.000          = 2,5 años
TPR = (160.000 / 4) / 100.000   = 40% anual
ROI = (160.000 − 100.000)/100.000 = 60%  (en los 4 años)
VAN = 40.000 × 2,855 − 100.000  ≈ +14.200   → conviene (VAN > 0)
TIR ≈ 21,9%  > 15%                          → conviene
```

(2,855 = factor de valor actual de 4 cuotas al 15%. **No te van a pedir la cuenta**: lo que importa es leer el resultado.)

**Por qué el TR solo no alcanza:** otro proyecto con el mismo TR de 2,5 años pero 8 años de vida útil empata en TR y le gana en VAN y en TIR.

### 4.4 Rentabilidad del emprendimiento: punto de equilibrio [wiki U6]

**Q = CF / (P − CVu)**, redondeando hacia arriba. **El retiro de los socios va en los costos fijos.** Ejemplo de la cátedra: remeras, 1.360.000 / (30.000 − 14.800) = **90 remeras por mes**.

**CAC** (costo de adquisición de clientes) = lo invertido en captación / clientes que **pagan**. Ejemplo del profe: 10.000 mails a USD 1 → 10 compradores → **USD 100 por cliente**; con una campaña de USD 100 en un club con los mismos 10 clientes → **USD 10**.

**Vender más ≠ ganar más:** con margen del 30%, bajar el precio un 15% obliga a **duplicar** las ventas para ganar lo mismo.

---

## 5. Canvas (Business Model Canvas) ★★★

### 5.1 Plantilla en español

```
┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│              │ Actividades  │              │ Relación con │              │
│ Socios       │ clave (8)    │ Propuesta    │ clientes (4) │ Segmentos    │
│ clave (7)    ├──────────────┤ de valor (1) ├──────────────┤ de clientes  │
│              │ Recursos     │              │ Canales (3)  │ (2)          │
│              │ clave (6)    │              │              │              │
├──────────────┴──────────────┴──────┬───────┴──────────────┴──────────────┤
│ Estructura de costos (9)           │ Fuentes de ingresos (5)             │
└────────────────────────────────────┴─────────────────────────────────────┘
```

**Orden para llenarlo:** Segmentos → Propuesta de valor **por segmento** → Canales, Relación e Ingresos (cada ítem con su S1, S2…) → Recursos, Actividades y Socios → Costos (**fijos y variables por separado**).

**Regla de consistencia:** todo lo que se promete a la derecha tiene que estar sostenido a la izquierda. Si prometés soporte 24×7, tiene que haber una actividad (soporte), un recurso (técnicos) y un costo (sueldos).

### 5.2 Lo más importante: segmento ↔ propuesta de valor [consulta]

> "Nos va a interesar que hagan esa relación entre propuesta de valor y segmento de clientes."

**Segmentos específicos.** Tienen que poder "verse". Si son genéricos, "va a ser tirar el tiro al aire".

| Mal | Bien |
|---|---|
| Bancos | Bancos privados de capital nacional con 30 a 80 sucursales que tienen un proyecto de IA en su plan estratégico |
| Jóvenes | Estudiantes de 18 a 24 años del interior que viven en Rosario, sin cuenta bancaria propia y que cobran por transferencia trabajos informales de menos de $400.000 por mes |
| Comercios | Comercios de barrio de Rosario con facturación menor a $5 M por mes que hoy cobran en efectivo y con QR de una billetera ajena |

Variables para recortar: **geográficas, demográficas, socioeconómicas (ingreso), de comportamiento (qué hacen hoy y con qué) y de necesidad.** Nombrá a los **early adopters**. Separá **usuario / decisor / pagador** (en B2B: usa el cajero, decide el Gerente de Operaciones, paga Finanzas). Un **actor crítico** no paga, pero sin él el modelo no funciona.

**La propuesta de valor es el beneficio, no el producto.**
- Mal: "Chatbot con IA". Bien: "Atender una consulta normativa en 30 segundos en vez de 15 minutos".
- **Plantilla:** (S1) [beneficio concreto], **porque** [el dolor específico de ese segmento].
- **La misma solución vale distinto para cada segmento.** En DeepAgro (cámaras con IA que solo fumigan la maleza): al **productor** le da **plata** (70% menos herbicida); a la **provincia**, **ambiente**; a la **empresa pulverizadora**, **trabajo** (la eligen más). Hay que ir "al dolor que tiene cada uno".
- Si la propuesta sirve igual para cualquier segmento, **está mal**.

### 5.3 Ejemplo completo — startup "Norma" (copiloto normativo para entidades financieras)

> Somos **de afuera**: una startup rosarina que le vende al banco un asistente con IA para el personal de sucursal. Bancorp lo tiene como proyecto propio (Proyecto 3); nosotros le ofrecemos **comprarlo hecho** en lugar de desarrollarlo.

**Segmentos de clientes**
- **(S1)** Bancos privados de capital nacional con 30 a 80 sucursales (como Bancorp), cuyo personal de plataforma y cajas consulta varias veces por día circulares del BCRA y manuales internos y hoy deriva las dudas a la Mesa de Ayuda o a Cumplimiento. *Usa:* el personal de sucursal · *decide:* el Gerente de Operaciones Bancarias, con aval del CISO · *paga:* Administración y Finanzas. *Early adopters:* bancos que ya tienen un proyecto de IA aprobado en su plan.
- **(S2)** Cajas de crédito, cooperativas y mutuales con servicio de ayuda económica de Santa Fe y Córdoba, de 5 a 20 sucursales, sin área propia de normativa (una persona de Cumplimiento o un estudio externo).
- **(S3)** Oficiales de Cumplimiento y PLA/FT de esas entidades: necesitan demostrarle al auditor que el personal opera según la norma vigente.

**Propuesta de valor (una por segmento)**
- **(S1)** Bajar la atención de una consulta normativa de ~15 minutos a menos de 1, sin que el dato del cliente salga del banco, **porque** con 45 sucursales cada consulta que va a la Mesa de Ayuda frena la fila y un error operativo puede terminar en una sanción del BCRA.
- **(S2)** Tener "un área de normativa" por una fracción del sueldo de un especialista, con las circulares nuevas ya cargadas, **porque** no pueden pagar un equipo propio y se enteran tarde de los cambios.
- **(S3)** Trazabilidad de qué se consultó, qué se respondió y con qué norma vigente, **porque** en una auditoría tienen que demostrar que el personal estaba capacitado.

**Canales**
- (S1) Venta directa B2B con demo y prueba piloto en 3 sucursales; presencia en eventos del sector bancario; entrega instalada en la nube privada del banco; posventa con soporte dedicado.
- (S2) Federaciones de cooperativas (canal de socios) y webinars; alta online con onboarding guiado.
- (S3) Se llega a través de S1 y S2: reportes que se envían por mail y tablero web.

**Relación con clientes (Get / Keep / Grow)**
- **Get:** (S1) piloto gratis de 60 días con métricas de tiempo ahorrado · (S2) demo en la federación y primer mes gratis.
- **Keep:** (S1) Customer Success asignado y actualización normativa semanal incluida · (S2) soporte por chat y boletín de cambios normativos.
- **Grow:** (S1) up-sell al módulo de auditoría (S3) y extensión a Banca Empresas · (S2) referidos entre cooperativas de la federación.

**Fuentes de ingreso**
- (S1) **Suscripción** mensual por sucursal + **implementación** (carga de los manuales propios del banco).
- (S2) **Suscripción** por plan cerrado según cantidad de usuarios, con base normativa compartida (sin manuales propios, más barato).
- (S3) Módulo de auditoría con **tarifa adicional** dentro de la suscripción.

**Recursos clave**
- **Humanos:** desarrolladores, especialista en normativa bancaria, comercial B2B.
- **Intelectuales:** base normativa curada y actualizada, la plataforma, la marca.
- **Físicos/tecnológicos:** infraestructura cloud contratada.
- **Financieros:** capital de los fundadores y un ANR.

**Actividades clave:** desarrollo y mantenimiento de la plataforma · **curaduría normativa semanal** · integración con los sistemas del banco · ventas B2B · soporte.

**Socios clave** (de quién **depende** el modelo; no son los dueños)
- **Proveedor del modelo de lenguaje** (proveedor estratégico): si sube el costo de los tokens o cambia sus condiciones, cambian los costos y el precio. *Mitigación:* arquitectura que permita cambiar a un modelo abierto alojado por nosotros.
- **Proveedor cloud con datacenter en la región** (proveedor estratégico): el banco exige que los datos no salgan del país.
- **Federaciones de cooperativas** (alianza estratégica): son el canal hacia S2.
- **Estudio jurídico especializado en BCRA** (proveedor estratégico): valida la base normativa.

**Estructura de costos**
- **Fijos:** sueldos (incluido el retiro de los socios), plan base de cloud, estudio jurídico, contador, publicidad base.
- **Variables:** tokens del modelo de IA por consulta, cloud que escala con los usuarios, comisiones de venta, impuestos sobre la facturación.

**¿Es rentable?** (números supuestos) CF = USD 9.000 por mes; precio de USD 150 por sucursal por mes; CV de USD 30 por sucursal (tokens + cloud).
Q = 9.000 / (150 − 30) = **75 sucursales**, es decir, alrededor de **dos bancos como Bancorp**. El modelo cierra con pocos clientes S1; S2 aporta volumen.

**Chequeo de consistencia:** prometo norma vigente (S1, S2) → actividad: curaduría semanal → recurso: especialista y estudio jurídico → costo: sueldo y honorarios. ✔

### 5.4 Otra idea, para practicar solo segmento ↔ propuesta: onboarding biométrico como servicio

Startup que valida identidad (DNI + selfie contra RENAPER) por API.

| Segmento | Propuesta de valor (beneficio + porqué) | Ingreso |
|---|---|---|
| (S1) Bancos medianos que lanzan billetera o cuenta digital (como Bancorp, Proyecto 1) | Abrir cuentas en 3 minutos sin sucursal, **porque** cada abandono en el alta es un cliente que se va a una fintech | Tarifa por validación |
| (S2) Fintechs y proveedores de servicios de pago de menos de 50 empleados | Cumplir el "conozca a su cliente" del BCRA sin armar un equipo de fraude, **porque** no tienen escala para hacerlo propio | Suscripción con tope de validaciones |
| (S3) Área de Prevención del Fraude de bancos ([02] en Bancorp) | Menos fraude por suplantación de identidad, **porque** cada fraude es una pérdida y un reclamo | Módulo antifraude premium |

Socio clave: **RENAPER**. Si cambia su API o sus tarifas, el modelo se cae. *Mitigación:* validación alternativa con lectura del chip del DNI.

### 5.5 Recordatorios por bloque

- **Canales ≠ Relación.** Los canales son **cómo llega** el producto y **cómo se entera** el cliente (información → evaluación → compra → entrega → posventa). La relación es **marketing**: cómo conseguís, mantenés y hacés crecer clientes (el **doble embudo Get/Keep/Grow**). "Conviene más cuidar los clientes que conseguir nuevos": cada cliente perdido es el CAC que pagaste más sus compras futuras.
- **Socios clave:** son aquellos de los que **depende** el modelo, "aunque ni sepan que lo son" (Vercel, la API de Mercado Pago, NVIDIA para DeepAgro, el proveedor de IA por el costo de los tokens). Cuando cambia un socio clave, cambian las actividades, los recursos, los costos y el precio. Nombrá el **tipo**: proveedor estratégico, alianza, coopetición o joint venture. **Los fundadores van en recursos financieros**, no acá.
- **Ingresos:** venta, tarifa por uso, suscripción, alquiler, licencia, intermediación, publicidad. **Uno por segmento.** El precio parte del **valor percibido**, no del costo.
- **Costos:** el mismo costo no puede estar en las dos columnas. Si crece con los clientes, es **variable**.

---

## 6. Lean Startup ★

- **Qué es:** una forma de emprender **validando el modelo con clientes reales antes de invertir fuerte**. El Canvas está lleno de **hipótesis** que hay que probar. Idea central: no construir algo que nadie quiere; **fallar rápido y barato**.
- **Ciclo:** crear (construir) → **validar/medir** → aprender → cambiar. Si hay que cambiar algo sustancial, aparece el **pivot**, y se vuelve a validar con un MVP nuevo.
- **MVP:** la versión del producto que se **lanza al mercado** para validar ideas con el máximo aprendizaje y el mínimo esfuerzo. Es **funcional**; el prototipo no. El profe lo plantea como "lo más que puedo hacer en menos tiempo". Tipos: **landing page** (medir interés antes de construir) y **Mago de Oz** (parece automático pero por detrás se hace a mano, como Zappos).
- **Iterar vs. pivotar:** iterar es un ajuste menor; pivotar es un cambio sustancial (de segmento, de propuesta o de modelo de ingreso) **sin abandonar la visión**. Ejemplo del profe: el robot cortacésped para canchas de golf tenía un mercado chico, así que se suma la **venta** de cortadoras eléctricas importadas a los countries de Funes y se mantiene el **alquiler** a las canchas. Mismo objetivo, otro modelo según el segmento.
- **Desarrollo de clientes:** descubrimiento → validación → creación de demanda → desarrollo de la empresa. Si pagan y el mercado alcanza, se crece; si el mercado es chico, se crece lento; **si no pagan, se buscan otros clientes**.
- **Ajuste producto-mercado:** "lo que yo ofrezco, que la gente me lo saque de las manos". A veces el que compra no es el que uno pensaba (la herramienta agro que no compra el productor, sino el agrónomo asesor o la empresa que monitorea desde Rosario).
- **Startup vs. empresa:** la startup **busca** un modelo repetible y escalable; la empresa ya lo **ejecuta**.
- **En el ejemplo Norma:** MVP Mago de Oz en 3 sucursales de un banco, con analistas que responden "detrás" del chat. Se mide si las consultas a la Mesa de Ayuda bajan y si el banco paga después del piloto. Si no paga, **pivot**: venderle a Cumplimiento (S3) como herramienta de auditoría.

---

## 7. Adquisiciones ★ ("tampoco es lo más crítico")

- **Se planifican en el tiempo:** se compra cuando se necesita, no todo al principio.
- **Qué se adquiere:** bienes, pero también servicios (mano de obra, consultores, proveedores externos).
- **Cómo:** hacer internamente, subcontratar o tercerizar (**outsourcing**). Para bienes: **comprar, alquilar o leasing**. El leasing es un alquiler con **opción de compra al final** por un importe preestablecido: "no es un alquiler ni una compra".
- **Selección del proveedor:** **licitación** ("sobre cerrado", con proceso definido de antemano) · **RFP** · **compra común** (comparar presupuestos, para cosas baratas y poco riesgosas).
- **RFI vs. RFP:** el **RFI** pide **información** para conocer el mercado, va **primero** y sirve para armar la lista corta. La **RFP** pide la **propuesta**, con precio, plazos y solución, para un requerimiento definido. (La RFQ pide solo cotización.) No te van a pedir armar una RFP, pero sí **qué es**.
- **TCO** (costo total de propiedad): **no es solo el precio**. Suma el costo **inicial** (compra, instalación, licencias), el de **operación** (energía, personal, soporte) y el de **mantenimiento** (preventivo, correctivo, actualizaciones) durante toda la vida útil. "Probablemente te preguntemos qué costos tiene que tener en cuenta."
- **Contratos: quién asume el riesgo**

| Contrato | Riesgo | Cuándo |
|---|---|---|
| Precio fijo | **Proveedor** | Alcance bien definido |
| Costo reembolsable (costo + ganancia) | **Cliente** | Alcance incierto |
| Tiempo y materiales (por hora) | Compartido | Servicios, consultoría |
| Con incentivos | Compartido | Premio por mejorar plazo, costo o calidad |

Regla: **cuanto más fijo el precio, más riesgo para el proveedor.** Los contratos también fijan la finalización anticipada y la resolución de conflictos.

---

## 8. Acta de constitución y objetivos ★ (por si cae con el proyecto asignado)

**Acta:** documento que **autoriza formalmente** el proyecto y le da al **director** autoridad sobre los recursos. La firma el **patrocinador**, en la **iniciación**. Es de alto nivel: **no es el plan**.

Contenido: nombre · justificación · **objetivos medibles** · requisitos de alto nivel · alcance (qué entra y qué no) · supuestos y restricciones · riesgos de alto nivel · hitos · presupuesto global · interesados · **director con su nivel de autoridad** · patrocinador · criterios de aprobación y cierre. Lo que más se corrige: objetivos **medibles** y la **autoridad del director**.

**Objetivos:** [verbo] + [qué] + [cuánto] + [para cuándo], con su **criterio de verificación**. Si falta el criterio, perdés la mitad del punto.

- *De negocio (Omnicanalidad):* aumentar un 25% las operaciones iniciadas en un canal y terminadas en otro dentro de los 6 meses posteriores a la salida. Criterio: logs de operaciones multicanal contra la línea base del trimestre previo.
- *De TI:* unificar en una sola API la lógica de Home Banking y App, con 99,9% de disponibilidad mensual, antes del cierre del proyecto. Criterio: monitoreo 24×7 de [04] y pruebas de aceptación.

**Ciclo de vida:** cascada (requisitos estables, por ejemplo por normativa) · iterativo/incremental (cada módulo suma funcionalidad) · espiral (alto riesgo) · ágil (requisitos cambiantes). **Justificalo con una característica del proyecto**, no con la definición.

---

## 9. Autoevaluación rápida (tipo multiple choice)

1. SV = −300 y CV = +200. → **Atrasado, pero eficiente** (hace menos de lo planeado y lo que hace le cuesta menos).
2. ¿Qué indicador no considera el valor del dinero en el tiempo? → **TR y TPR**.
3. VAN = 0. → El proyecto rinde **exactamente** la tasa exigida; la TIR es igual a esa tasa.
4. ¿La TIR conviene mayor o menor? → **Mayor**, y tiene que superar la tasa de descuento.
5. Una tarea con HT = 3 y HL = 0. → Puede atrasarse 3 días sin atrasar el proyecto, pero **cualquier** atraso corre a su sucesora.
6. Se consume toda la holgura de una tarea para nivelar. → Queda crítica y puede aparecer un **segundo camino crítico**.
7. ¿Contrato de precio fijo? → El riesgo lo asume el **proveedor**.
8. ¿RFI o RFP para conocer qué soluciones hay en el mercado? → **RFI**.
9. ¿El socio que puso la plata es socio clave? → **No**: va en **recursos financieros**.
10. "App de turnos" como propuesta de valor. → **Mal**: es el producto. Escribí el beneficio para un segmento concreto.
11. Pivotar es abandonar la idea. → **Falso**: es cambiar una parte del modelo sin abandonar la visión.
12. PV se calcula con el estado real. → **Falso**: el PV sale del **plan** (Gantt) y el EV del **estado real**.
