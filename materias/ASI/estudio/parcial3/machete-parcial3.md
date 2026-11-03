# ASI — Machete 3º Parcial (U5 Proyectos + U6 Emprendedorismo)

> **Proyectos:** sobre los proyectos del 1er año de **Bancorp** (Billetera Virtual · Omnicanalidad · Copiloto IA · Employee Experience). **Emprendedorismo:** tema bancario, pero **desde afuera**: somos una startup que le vende algo al banco.

---

## U5 · 1. Valor Ganado ★★★

| Sigla | Qué es | De dónde sale |
|---|---|---|
| **BAC** | Presupuesto total | Σ presupuesto de las tareas |
| **PV** | Lo que **debería** estar hecho al corte, en $ | **Gantt (plan)** |
| **EV** | Lo que **está** hecho, a precio de presupuesto | **Estado real** |
| **AC** | Lo que se gastó ("lo que saqué de la billetera") | Dato |

**De memoria:**
- **SV = EV − PV** → tiempo. Si es < 0, **atrasado**.
- **CV = EV − AC** → costo. Si es < 0, **ineficiente** (gasta de más).

Extras: SPI = EV/PV · CPI = EV/AC · EAC = BAC/CPI.

**Criterio 50/50** (se fija al inicio del proyecto): terminada = 100% · en curso = 50% · no iniciada = 0.

**Ejemplo — Omnicanalidad, corte al final del día 10, AC = 2.900**

```
Tarea  Presup.  Plan         $plan   Real          $real
A        600    Finalizada     600   Finalizada      600
B        800    Finalizada     800   Finalizada      800
C        500    Finalizada     500   En curso        250
D      1.500    En curso       750   En curso        750
E        900    En curso       450   No iniciada       0
F,G,H  1.700    No iniciada      0   No iniciada       0
BAC = 6.000     PV = 3.100           EV = 2.400
SV = 2.400 − 3.100 = −700 → ATRASADO
CV = 2.400 − 2.900 = −500 → INEFICIENTE
```

**Siempre cerrar con una frase:** "Está atrasado (se hizo $700 menos de lo planeado) e ineficiente (lo hecho costó $500 más de lo presupuestado). C se atrasó y E no pudo arrancar: aparece un 2º camino crítico."

Errores típicos: sacar el PV del estado real o el EV del plan · equivocarse de día de corte · no interpretar.

---

## U5 · 2. Red y Gantt (leer y justificar, no dibujar) ★★

```
┌─────┬──────┬─────┐
│ IT  │ Dur  │ FT  │   temprano
├─────┴──────┴─────┤
│      Tarea       │
├─────┬────┬────┬──┴──┐
│ ITa │ HT │ HL │ FTa │   tardío
└─────┴────┴────┴─────┘
```

- **Convención del profe:** se arranca el **día 1** y **FT = IT + dur − 1**. La sucesora arranca al día siguiente de la predecesora que termina **más tarde**. La cátedra cuenta desde 0; el resultado es el mismo, pero **no mezcles las dos**.
- **HT = ITa − IT:** cuánto se puede atrasar la tarea **sin atrasar el proyecto**. Es la que importa.
- **HL:** cuánto se puede atrasar **sin atrasar a la sucesora**. Siempre HL ≤ HT.
- **Camino crítico** = tareas con **HT = 0**. Puede haber más de uno.
- La duración del proyecto es el **mayor FT**. Si hay una sola tarea final, su FT = FTa y es crítica.
- **Nivelación:** se corren las tareas no críticas dentro de su **holgura total** para emparejar la gente por día (de un pico de 4,25 personas a 2,5 parejas). El trabajo total es el mismo, pero baja el pico → **menos costo**. A cambio se **gasta el colchón**: aparecen **nuevos caminos críticos** y sube el riesgo. La duración no cambia.

**Ejemplo — Omnicanalidad:** 18 días · crítico **A→B→D→F→H** · C (HT 1, HL 0): si se atrasa, atrasa a E · G (HT 2, HL 2): es holgura "gratis", la primera que se corre para nivelar.

---

## U5 · 3. Rentabilidad: qué mide cada indicador ★★

**Beneficios = ingresos nuevos + costos evitados**, siempre **monetizados**.

**Ejemplo — Portal del Empleado:** inversión 100.000 · beneficio de 50.000 por año · 3 años · tasa del 10%.

| | Pregunta que responde | Resultado | Regla | ¿Considera el valor del dinero? |
|---|---|---|---|---|
| **TR** | ¿Cuándo recupero? | **2 años** | menor = mejor | NO (y no ve nada después del recupero) |
| **TPR** | ¿Qué % vuelve por año? | 50.000 / 100.000 = **50%** | mayor = mejor | NO (pero sí usa la vida útil) |
| **ROI** | ¿Cuánto gano por cada $1? | (150 − 100) / 100 = **50%** | mayor = mejor | NO |
| **VAN** | ¿Cuánto gano en $ de hoy? | 124.343 − 100.000 = **+24.343** | **> 0 conviene** | SÍ |
| **TIR** | ¿A qué tasa rinde? | **≈ 23,4%** | **> tasa exigida** conviene | SÍ |

- **VF:** cuánto valdrá mañana la plata de hoy (100.000 al 10% → 110.000 en 1 año).
- **VA:** cuánto vale hoy la plata futura (50.000 en el año 3 → 37.566 hoy). "La plata trabaja."
- **VAN** = VA de los beneficios − inversión. **TIR** = la tasa que hace VAN = 0. La TIR es la clave para **comparar proyectos** porque es un %.
- Tasa de descuento = costo de capital + % de riesgo. **No es la inflación.**
- **Punto de equilibrio** (para el emprendimiento): **Q = CF / (P − CVu)**. El retiro de los socios va en los costos fijos.

### Ejercicio tipo, explicado paso a paso

**Los datos te los da el enunciado.** No se inventan.

| Dato | Qué es |
|---|---|
| **Inversión** | Lo que cuesta hacer el proyecto, se paga hoy |
| **Beneficio por año** | Lo que el banco gana o deja de gastar cada año (costos evitados + ingresos) |
| **Vida útil** | Cuántos años da beneficios |
| **Tasa (ej. 10%)** | Lo **mínimo** que el banco le exige a su plata: lo que ganaría en otro lado (por ejemplo, un plazo fijo) más un extra por riesgo. **El proyecto tiene que ganarle a esa tasa.** |

> **Enunciado.** Bancorp evalúa el **Portal del Empleado**. La inversión es de **$100.000**, los beneficios de **$50.000 anuales** durante **3 años** y la tasa exigida del **10%**.
> a) TR y ROI. b) VAN: ¿conviene? c) La TIR es 23,4%: interprétela. d) ¿Por qué no alcanza con el TR?

**a) TR:** sumo beneficios hasta llegar a lo invertido.

```
Año 1: 50.000 → acumulado  50.000
Año 2: 50.000 → acumulado 100.000  ← iguala la inversión → TR = 2 años
```

**ROI** = (beneficio total − inversión) / inversión = (150.000 − 100.000) / 100.000 = **50%**.
→ "Recupera en 2 años. Por cada $100 invertidos gana $50 netos."

**b) VAN:** paso cada beneficio a **pesos de hoy** (divido por 1,10 una vez por cada año de espera) y resto la inversión.

```
Año 1: 50.000 / 1,10  = 45.455
Año 2: 50.000 / 1,21  = 41.322     (1,10 × 1,10)
Año 3: 50.000 / 1,331 = 37.566     (1,10 × 1,10 × 1,10)
                        ───────
        Total hoy     = 124.343
VAN = 124.343 − 100.000 = +24.343
```

¿Por qué divido? Porque $45.455 puestos hoy al 10% se convierten en $50.000 en un año. **Cobrar $50.000 dentro de un año equivale a tener $45.455 hoy.**
→ "VAN > 0, **conviene**: recupera la inversión, rinde el 10% exigido y genera $24.343 extra en pesos de hoy."

**c) TIR** (te la dan, no se calcula): "Es la tasa a la que rinde el proyecto, 23,4% anual. Supera el 10% exigido → **conviene**."

**d)** "El TR solo dice **cuándo** recupero. No mira lo que pasa después del recupero ni el valor del dinero en el tiempo. El VAN y la TIR sí."

**Cierre (siempre):** "El proyecto **conviene**: VAN positivo (+$24.343) y TIR (23,4%) mayor que la tasa exigida (10%). Recupera en 2 años con un ROI del 50%."

**Si la pregunta es solo teórica:** "Se monetizan los beneficios (ingresos + costos evitados), se comparan contra la inversión y se calcula el VAN a la tasa exigida: si da > 0, conviene. Si la TIR supera esa tasa, conviene."

**¿Proyecto o emprendimiento?** En un **proyecto**, como el anterior, deciden el VAN y la TIR. En un **emprendimiento** todavía no hay datos ciertos para un VAN creíble, así que se usan el **punto de equilibrio** (¿cuántos clientes necesito y es alcanzable?), el **CAC** y la **validación con un MVP** de que el cliente paga.

---

## U6 · 4. Segmentos ↔ Propuesta de valor ★★★

- **Segmento** = quién + dónde + tamaño o ingreso + qué hace hoy + qué le duele. Tiene que poder "verse".
- **Propuesta** = (S1) **[beneficio concreto], porque [dolor de ese segmento]**. Es el beneficio, **no el producto**.
- **La misma solución vale distinto para cada segmento.** Si la propuesta sirve igual para todos, está mal.
- Separar **usa / decide / paga**. El **actor crítico** no paga pero es imprescindible.

**ValidaYa** — alta de clientes con DNI + selfie *(Billetera Virtual)*

| Segmento | Propuesta de valor |
|---|---|
| (S1) Bancos privados medianos (30 a 80 sucursales) que lanzan una billetera digital | Abrir una cuenta en 3 minutos desde el celular, **porque** cada abandono del alta es un cliente que se va a una fintech |
| (S2) Fintechs de Rosario y Córdoba de menos de 50 empleados | Cumplir el "conozca a su cliente" del BCRA sin equipo propio, **porque** no tienen escala para hacerlo |
| (S3) Jóvenes de 18 a 25 años sin cuenta (actor crítico, no paga) | Tener cuenta sin ir a una sucursal, **porque** trabajan en horario bancario |

**UnToken** — token de seguridad único para web y app *(Omnicanalidad)*

| Segmento | Propuesta de valor |
|---|---|
| (S1) Bancos medianos con Home Banking y App separados | Menos reclamos a la Mesa de Ayuda por tokens bloqueados, **porque** cada cambio de celular termina en un llamado |
| (S2) Áreas de Ciberseguridad y Fraude (el [02] de Bancorp) | Menos fraude por robo de credenciales, **porque** cada canal con su propio token es una puerta más que defender |

**Norma** — asistente de normativa con IA *(Copiloto IA)*

| Segmento | Propuesta de valor |
|---|---|
| (S1) Bancos con más de 30 sucursales cuyo personal de cajas consulta circulares del BCRA a diario | Responder una duda normativa en menos de 1 minuto en lugar de 15, **porque** cada derivación a la Mesa de Ayuda frena la fila |
| (S2) Cajas de crédito y mutuales de Santa Fe de 5 a 20 sucursales sin área de normativa | "Un área de normativa" por una fracción de un sueldo, **porque** se enteran tarde de las circulares nuevas |

**Recibo+** — recibos con firma digital y licencias online *(Employee Experience)*

| Segmento | Propuesta de valor |
|---|---|
| (S1) Capital Humano de bancos con más de 1.000 empleados en sucursales del interior (**paga**) | Dejar de imprimir y archivar miles de recibos firmados por mes, **porque** viajan en sobre desde 45 sucursales y se pierden |
| (S2) Empleados de sucursal (**usa**, no paga) | Pedir una licencia desde el celular en 1 minuto, **porque** hoy es un formulario en papel que firma el gerente |

**Mal → bien:**
- "Bancos" → "Bancos privados con 30 a 80 sucursales que lanzan una billetera".
- "App con biometría" (es el producto) → "Abrir cuenta en 3 minutos".
- "Mejorar la experiencia del cliente" (vago) → "Bajar los reclamos por token bloqueado".

---

## U6 · 5. Resto del Canvas (una línea por bloque)

**Orden para llenarlo:** Segmentos → Propuesta → Canales / Relación / Ingresos (cada ítem con su S1, S2) → Recursos / Actividades / Socios → Costos.

- **Canales:** **cómo llega** el producto y **cómo se entera** el cliente. Ej.: venta directa B2B con demo a los bancos (S1); federación de cooperativas (S2).
- **Relación (Get / Keep / Grow):** es **marketing**. Get = piloto gratis de 60 días · Keep = soporte y actualizaciones · Grow = vender un módulo extra (up-sell) o referidos. **CAC** = gasto en captación / clientes que pagan.
- **Ingresos (uno por segmento):** suscripción, tarifa por uso, licencia, venta, alquiler, intermediación, publicidad. Ej.: ValidaYa cobra por validación (S1) y suscripción con tope (S2). El precio parte del **valor percibido**, no del costo.
- **Recursos:** físicos, intelectuales, humanos y financieros. **El capital de los fundadores va acá.**
- **Actividades:** desarrollo de la plataforma, ventas y soporte.
- **Socios clave:** aquellos de los que **depende** el modelo, no los dueños. Ej.: **RENAPER** para ValidaYa, el proveedor de IA para Norma. Si cambian, cambian los costos y el precio. Nombrá cómo se mitiga el riesgo.
- **Costos:** **fijos** (sueldos, retiro de los socios, plan base de cloud) / **variables** (tokens de IA, validaciones, comisiones). El mismo costo no va en las dos columnas.
- **Consistencia:** si prometés soporte 24×7, tiene que haber una actividad, un recurso y un costo que lo sostengan.

---

## U6 · 6. Lean Startup

- Validar con clientes **antes** de invertir fuerte. El ciclo es **crear → medir → aprender → cambiar**. Fallar rápido y barato.
- **MVP:** versión **funcional** que sale al mercado para validar (el prototipo no es funcional). Tipos: landing page y **Mago de Oz** (por detrás se hace a mano). Ej.: Norma con analistas que responden detrás del chat en 3 sucursales.
- **Iterar** = ajuste menor · **Pivotar** = cambio sustancial (de segmento o de modelo) **sin abandonar la visión**. Ej.: el robot de golf, que se vende a los countries y se alquila a las canchas.
- **Ajuste producto-mercado:** "que la gente me lo saque de las manos".
- **Startup** = busca un modelo repetible y escalable · **empresa** = ya lo ejecuta.

---

## U5 · 7. Adquisiciones (lo justo)

- **TCO** = costo inicial + operación + mantenimiento durante toda la vida útil, no solo el precio.
- **Bienes:** comprar · alquilar · **leasing** (alquiler con opción de compra al final).
- **RFI** = pedir **información** para conocer el mercado, va primero · **RFP** = pedir la **propuesta** con precio y plazos.
- Selección del proveedor: licitación (sobre cerrado) · RFP · compra común.
- **Riesgo del contrato:** precio fijo → lo asume el **proveedor** · costo reembolsable → lo asume el **cliente** · tiempo y materiales o con incentivos → compartido.

## U5 · 8. Acta y objetivos (por si cae)

- **Acta:** autoriza el proyecto y da autoridad al director. La **firma el patrocinador**, en la iniciación. Es de alto nivel, **no es el plan**. Lo que más se corrige: objetivos **medibles** y la **autoridad del director**.
- **Objetivo** = verbo + qué + cuánto + para cuándo + **criterio de verificación**.
- Ej. (Omnicanalidad): "Aumentar un 25% las operaciones iniciadas en un canal y terminadas en otro, a 6 meses de la salida. Criterio: logs multicanal contra el trimestre previo."
