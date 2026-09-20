# ICS — Banco de preguntas de parciales de regularización

Armado a partir de los **9 parciales de regularización** guardados en
`fuentes/parciales-regularizacion/` (2012, 2013, 2015, 2016, 2020, 2021, 2022, 2024, 2025).
Organizado **por tema**, no por año, porque las preguntas se repiten entre años.

## Cómo leer las respuestas

| Marca | Significado |
|---|---|
| ✅ | **Confirmada.** El formulario corregido (o la marca del profesor en los de papel) da esa opción como correcta. |
| ⚠️ | **Deducida.** El alumno la erró y el export **no revela** cuál era la buena. La razoné yo; la justificación está abajo de cada una. |

---

## Formato del examen

| Año | Formato | Puntaje | Se aprueba con |
|---|---|---|---|
| 2012–2016 | Papel. Multiple choice con opciones combinadas (A y C, B y D, "Todas", "Ninguna") + preguntas a desarrollar + un ejercicio de testing | — | — |
| 2020 | Google Forms, MC | 10 | — |
| 2021 | Google Forms, MC | 10 (preguntas de 1 y 2 pts) | **6** |
| 2022 | Google Forms, MC + matrices | — | — |
| 2024 | Google Forms, MC + matrices | 13 | **8** |
| 2025 | Google Forms, MC + matrices | 12 | **8** |

Hoy es todo **multiple choice y matrices**, sin desarrollo. Hay opción **"Ninguna de las
opciones"** y es una opción real, no relleno. Varias preguntas son de **selección múltiple**
(más de una correcta): si marcás de más, se pierde el punto.

---

## Lo que más se repite (empezá por acá)

| Pregunta | Años | Respuesta |
|---|---|---|
| Componentes **requeridos** de un área de proceso | 2012, 2020, 2021, 2024 | Metas específicas + metas genéricas |
| Área cuyo propósito es **comprender fortalezas y debilidades** de los procesos | 2015, 2016, 2020, 2022 | **OPF** |
| Matriz **activo / producto de trabajo / ambos** | 2022, 2024, 2025 | ver tabla abajo |
| **Termómetro** — particiones válidas | 2020, 2022 | un representante por partición |
| **Tablas de decisión** — contar condiciones / acciones / columnas / casos | 2022, 2024 | ver abajo |
| Momento en que se definen los **controles** del proyecto | 2020, 2021 | **Planificación** |
| "Cualquier desvío debe ser resuelto" | 2020, 2021 | **Falso** |
| Área que mantiene el **repositorio de medidas** ligado a los procesos estándar | 2022, 2024 | **OPD** |
| Principios de la Ingeniería de Software | 2012, 2013, 2015 | calidad + probar |

---

# 1. CMMI — estructura del modelo

### 1.1 Son componentes requeridos de un Área de Proceso CMMi ✅

*(2012 · 2020 · 2021 · 2024 — selección múltiple)*

Opciones típicas: Herramientas · Metas específicas · Metas genéricas · Sub-prácticas genéricas ·
Prácticas genéricas.

**Respuesta: Metas específicas (SG) + Metas genéricas (GG).**

Requeridos = **sólo las metas**. Las prácticas (SP/GP) son **esperadas**. Todo lo demás
—subprácticas, productos de trabajo típicos, herramientas, ampliaciones, ejemplos— es
**informativo**.

### 1.2 "CMMI considera como elemento obligatorio las prácticas específicas en las áreas de proceso" ⚠️

*(2025 — el alumno puso "Sí" y lo erró)*

**Respuesta: No.**

Misma idea que la anterior, dada vuelta. Las prácticas específicas son componentes
**esperados**, no requeridos: la organización puede implementar prácticas alternativas siempre
que satisfaga la meta. Lo obligatorio son las **metas**.

### 1.3 Determinar el nivel de madurez de una software factory ⚠️

*(2025 — el alumno puso "Nivel 2" y lo erró)*

> Lleva varios años en el mercado, cumple con las áreas de proceso de nivel 3 y con las áreas de
> nivel 2, **excepto el área de proceso de MA**, que también corresponde al nivel 2.

**Respuesta: Nivel 1.**

Los niveles son **acumulativos y todo-o-nada**: si falta **una sola** área de proceso de nivel 2,
no se alcanza el nivel 2, y sin nivel 2 no hay nivel 3 por más que se cumplan sus áreas. Queda
en **nivel 1**, que es el nivel por defecto (no exige nada).

Esta deducción está **confirmada por la pregunta 1.4**, que es el mismo razonamiento y sí tiene
clave oficial.

### 1.4 ¿En cuáles niveles de madurez NO nos encontramos? ✅

*(2025 — selección múltiple)*

> Cierto gerente afirmó que una vez que alcanza nivel 3 ya no es necesario cumplir con la meta
> *Establecer estimaciones*. De hecho: "nosotros dejamos de hacerlo".

**Respuesta: Nivel 2, Nivel 3, Nivel 4 y Nivel 5** (o sea: la organización **está en nivel 1**).

*Establecer estimaciones* es una meta de **PP, nivel 2**. Si dejó de cumplirla, se cae de nivel 2
y de todo lo que está por encima. Sólo queda nivel 1.

> **La regla que unifica 1.3 y 1.4:** alcanzar un nivel superior **no te exime** de las áreas de
> los niveles anteriores. Una organización nivel 5 sigue haciendo PP y PMC todos los días.

---

# 2. CMMI — discriminar entre áreas de proceso

### 2.1 Área cuyo propósito se basa en la comprensión de las fortalezas y debilidades actuales de los procesos de la organización ✅

*(2015 · 2016 · 2020 · 2022 — la pregunta más repetida de toda la serie)*

Opciones: OPD · OT · **OPF** · PP

**Respuesta: OPF (Enfoque de Procesos de la Organización).**

OPF **diagnostica y planifica la mejora**: evalúa dónde está parada la organización. OPD
**define y guarda** los activos (procesos estándar, modelos de ciclo de vida, repositorio).

### 2.2 Área que evalúa los procesos de la organización contra los de otras organizaciones ✅

*(2021)*

Opciones: VER · VAL · OT · **OPF** · OPD · PP

**Respuesta: OPF.** Es la misma idea que 2.1: el diagnóstico —incluido el benchmarking contra
otras organizaciones— vive en OPF.

### 2.3 Área que mantiene el repositorio de medidas de producto y proceso relacionadas con el conjunto de procesos estándar de la organización ✅

*(2022 · 2024)*

Opciones: MA · **OPD** · PMC · PP · OPF · OPP · Ninguna

**Respuesta: OPD (Definición de Procesos de la Organización).**

> ⚠️ **La trampa es MA.** MA (Medición y Análisis) es **nivel 2** y mide **el proyecto**. El
> **repositorio de medidas de la organización**, atado al conjunto de procesos estándar, es un
> **activo organizacional** → OPD, nivel 3. Si dice "de la organización" o "procesos estándar",
> es OPD.

### 2.4 Cuando se almacenan las métricas de un proyecto en el repositorio de mediciones de la software factory, ¿qué área(s) intervienen? ✅

*(2021)*

Opciones: OT · PP · OPF · **OPD**

**Respuesta: OPD.** Mismo criterio que 2.3: el repositorio es de la organización.

### 2.5 Son prácticas específicas del área OPF ✅

*(2012 — respuesta marcada: B y D)*

- A) Establecer el repositorio de medición de la organización
- **B) Establecer planes de acción de procesos** ✅
- C) Especificar el proceso de negocio principal
- **D) Incorporar las experiencias relativas al proceso en los activos de proceso de la organización** ✅

A es de **OPD**. C no es de ninguna (es del negocio del cliente, no del proceso).

### 2.6 Son prácticas específicas del área OPD ✅

*(2013 — respuesta marcada: A y B)*

- **A) Establecer el repositorio de medición de la organización** ✅
- **B) Establecer las descripciones de los modelos de ciclo de vida** ✅
- C) Especificar el proceso de negocio principal
- D) Incorporar las experiencias relativas al proceso en los activos de proceso de la organización

D es de **OPF** (ver 2.5). Ojo con el par 2.5 / 2.6: **son la misma lista de opciones con la
pregunta invertida**. Tomaron las dos en años distintos.

### 2.7 Área cuyo propósito es que las personas puedan realizar sus roles de manera eficaz y eficiente ✅

*(2013)*

Opciones: OPD · OPF · **OT** · RD

**Respuesta: OT (Formación Organizativa).**

### 2.8 Área cuyo propósito es "proporcionar una comprensión del progreso del proyecto para tomar acciones correctivas cuando el rendimiento se desvía significativamente del plan" ✅

*(2012)*

**Respuesta: PMC (Monitorización y Control del Proyecto).** Es la definición textual de PMC.

### 2.9 Área donde se trata la captura de necesidades, expectativas y restricciones del cliente ✅

*(2015)*

Opciones: PP · **RD** · OPD · OPF

**Respuesta: RD (Desarrollo de Requerimientos).** La **elicitación** es de RD. Ojo de no
confundir con **REQM**, que **gestiona** requerimientos ya capturados (cambios, trazabilidad).

### 2.10 La identificación de inconsistencias entre los requerimientos, los planes y los productos de trabajo es propósito de ✅

*(2013)*

Opciones: RD · **REQM** · PP · OPD

**Respuesta: REQM (Gestión de Requerimientos), SP 1.5.**

### 2.11 Áreas de proceso que corresponden a nivel de madurez 3

*(2016 — el alumno puso B y lo erró; la clave no se ve)* ⚠️

Opciones: VAL · PMC · VER · PP · OPF

**Respuesta: VAL, VER y OPF** (las tres son nivel 3). PMC y PP son **nivel 2**.

### 2.12 Son metas específicas del área PMC ✅

*(2016 — respuesta marcada: B y C)*

- A) Obtener el compromiso con el plan → es de **PP**
- **B) Monitorizar el proyecto frente al plan** ✅ (SG1)
- **C) Gestionar las acciones correctivas hasta su cierre** ✅ (SG2)
- D) Monitorizar los criterios y las guías de adaptación → no es de PMC

---

# 3. Activo vs. producto de trabajo

Es una **matriz** con 4-5 ítems, un punto cada uno. Apareció en 2022, 2024 y 2025.

### 3.1 Tabla consolidada de los tres años

| Ítem | Respuesta | Año |
|---|---|---|
| Plantilla de Casos de Uso | **Activo** | 2022 ✅ |
| Plantilla de Manual de Instalación | **Activo** | 2024 ✅ |
| Plantilla para presentación de Reunión de Lanzamiento de Proyecto | **Activo** | 2025 ✅ |
| Guía para confeccionar Manual de Usuario | **Activo** | 2025 ✅ |
| Directrices para conformar el Equipo del Proyecto | **Activo** | 2024 ✅ |
| Manual de usuario del **compilador Java** | **Activo** | 2022 ✅ |
| Descripción de (flujo del) Proceso de Negocio **del Cliente** | **Producto de Trabajo** | 2024 ✅ · 2025 ✅ |
| Manual de Instalación **del sistema desarrollado para el cliente** | **Producto de Trabajo** | 2024 ✅ |
| Manual de Usuario **del sistema desarrollado para el cliente** | **Producto de Trabajo** | 2025 ✅ |
| Regla de Negocio | **Producto de Trabajo** | 2022 ✅ · 2024 ✅ |

### 3.2 El criterio

- **Activo** = algo que la organización tiene **para usar en sus proyectos**. Señales:
  *plantilla, guía, directriz, modelo, estándar*. También las **herramientas que la organización
  adquiere** (por eso el manual del compilador Java es activo: es documentación de una
  herramienta, no un producto del proyecto).
- **Producto de trabajo** = el resultado concreto de una tarea **de un proyecto**. Señales:
  *"del cliente"*, *"del sistema desarrollado"*, un artefacto puntual (regla de negocio,
  descripción del proceso de negocio del cliente, minuta, código).

> **El par que confunde:** *Plantilla de Manual de Instalación* = **activo** ·
> *Manual de Instalación del sistema desarrollado para el cliente* = **producto de trabajo**.
> El molde es de la organización; lo moldeado es del proyecto.

> **Observación, no regla:** en los **10 ítems confirmados** de los tres años, **"Ambos" nunca
> fue la respuesta correcta**. En 2022 el alumno marcó "Ambos" en dos ítems y perdió los dos
> puntos. Pensalo dos veces antes de marcar "Ambos".

---

# 4. Testing — particiones de equivalencia y valores límite

### 4.1 Termómetro con refrigeración (2022) ⚠️

> Mide grados centígrados **enteros**, cada 1 minuto. Si la temperatura **sube por encima de 25**
> se activa la refrigeración. Si **cae por debajo de 20** se apaga. Capacidad de medición: **0 a
> 53** grados.
> ¿Cuáles valores son la mejor elección para cubrir **todas las particiones válidas**?

Opciones: 19,33 · 0,20,25,53 · **3,23,33** · 13,23 · 17,18,19 · 20,25

**Respuesta: 3, 23, 33.** *(El alumno puso 0,20,25,53 y lo erró.)*

Las particiones válidas son **tres**, y hay que dar **un representante de cada una**:

| Partición | Rango | Comportamiento | Representante |
|---|---|---|---|
| PV1 | 0 – 19 | Se apaga la refrigeración | **3** |
| PV2 | 20 – 25 | No pasa nada (zona muerta) | **23** |
| PV3 | 26 – 53 | Se activa la refrigeración | **33** |

> La zona muerta 20–25 **existe y es una partición**: "por encima de 25" es > 25, y "por debajo
> de 20" es < 20, así que entre 20 y 25 inclusive el sistema no hace nada. Olvidarse de la zona
> muerta es el error clásico. `0,20,25,53` son **valores límite**, no representantes de
> partición: la consigna pide cubrir las particiones, no los bordes.

### 4.2 Termómetro con calefacción (2020) ⚠️

> Si la temperatura **cae por debajo de 18** se activa la calefacción. Si **pasa los 23** se apaga.

Opciones: **15,19,25** · 17,18,19 · 18,20,22 · 16,26,32

**Respuesta: 15, 19, 25.** *(El alumno puso 18,20,22 y lo erró.)*

| Partición | Rango | Representante |
|---|---|---|
| PV1 | ≤ 17 | **15** |
| PV2 | 18 – 23 | **19** |
| PV3 | ≥ 24 | **25** |

`18,20,22` caen **los tres en la misma partición** (la zona muerta) → no cubre nada.
`17,18,19` idem, dos particiones a lo sumo.

### 4.3 Adicional por antigüedad ✅

*(2024)*

> La antigüedad se mide en categorías: **≤ 2 años**, **> 2 y < 5**, **≥ 5 y < 10**, **10 o más**.
> Se sabe además que la edad de jubilación es 65 años y el período de prueba inicial es de hasta
> 6 meses.
> ¿Cuántos casos de prueba son necesarios si **sólo** se necesitan las **particiones de
> equivalencia válidas** para probar el cálculo del adicional?

Opciones: 0 · 1 · 2 · 3 · **4** · 5

**Respuesta: 4.**

Una partición válida por categoría, y son cuatro categorías → 4 casos.

> **Las dos trampas.** (a) La jubilación a los 65 y el período de prueba de 6 meses son **ruido**:
> no intervienen en el cálculo del adicional. (b) La opción *"0 (las pruebas exhaustivas son
> imposibles)"* es verdadera como frase y falsa como respuesta — justamente **por eso** se
> particiona.

### 4.4 Correspondencia técnica ↔ acción ✅

*(2025)*

> 1. Diseñar casos con valores válidos e inválidos en el campo "número de legajo" (8 dígitos).
> 2. Verificar las reglas de promoción (aprobado con 4 o más) representando **todas las
>    combinaciones** de notas y estados en una **matriz**.
> 3. Ejecutar casos que simulen la **secuencia de estados** de un alumno:
>    Inscripto → Cursando → Aprobado/Desaprobado.

**Respuesta: (1) Valores límite, (2) Tablas de decisión, (3) Transición de estados.**

Las palabras que disparan cada técnica:

| Señal en el enunciado | Técnica |
|---|---|
| Un campo con rango, longitud o formato; "válidos e inválidos"; extremos | **Valores límite** (o partición de equivalencia) |
| "Todas las combinaciones", matriz, reglas de negocio que se cruzan | **Tablas de decisión** |
| Secuencia, flechas entre estados, "pasa de X a Y" | **Transición de estados** |
| Flujo básico + flujos alternativos, escenarios punta a punta | **Casos de uso** |
| Tengo el código, cobertura de sentencias/decisiones | **Caja blanca** |
| Volver a probar lo que ya andaba, después de un fix | **Regresión** |

### 4.5 Ejercicio de testing a desarrollar (2016)

> Una función de auditoría recibe: **código de operación** numérico(3) entre 200 y 900 ·
> **tipo de operación** lista [Alta; Baja; Modificación; Consulta] · **fecha de operación** ·
> **usuario operación** texto(20).
> Se pide: (a) las particiones de equivalencia, (b) los casos de prueba con particiones puras,
> (c) los casos de prueba **usando valores límite**.
> Formato: `ID Caso + Atributo + ID Clase Equivalencia + Valor Entrada + Resultado Esperado`
> (resultado esperado: "OK" o "Error").

Hoy no se toma en este formato, pero **es el mismo contenido** que las preguntas de conteo de
hoy, y es idéntico al ejercicio del recargo de cuota de la clase 2 (ver
[ICS.md → U5 → ejercicio 19](../ICS.md)).

---

# 5. Testing — tablas de decisión

Preguntan **contar**: condiciones, acciones, columnas después de simplificar, casos válidos.

### 5.1 Gimnasio ✅ *(2024 — parcial con 13/13, clave confiable)*

> Categorías de socio: **Coulson** (inicial), **IronMan** (10 % de descuento), **Hulk** (15 %).
> Además, si al comprar tiene la **cuota al día**, recibe un **5 % adicional**. Los descuentos son
> acumulables. El sistema calcula el porcentaje de descuento a aplicar.

| Se pregunta | Respuesta |
|---|:---:|
| Cantidad de **acciones** a colocar | **4** |
| Cantidad de **columnas** que quedan después de reducir/simplificar la tabla | **6** |
| Cantidad de **casos de prueba válidos** (sin condiciones incompatibles) | **6** |

- **4 acciones**: aplicar 0 %, aplicar 10 %, aplicar 15 %, aplicar el 5 % adicional.
- **6 columnas**: 3 categorías × 2 estados de cuota = 6 combinaciones posibles. La categoría
  **no es binaria**: es una condición de 3 valores mutuamente excluyentes, y ahí está la gracia
  del ejercicio.
- **6 casos válidos**: ninguna de las 6 combinaciones es imposible.

### 5.2 Aerolínea ⚠️ *(2022 — el alumno erró 3 de los 4 conteos)*

> El sistema solicita usuario y contraseña, **valida** si son correctos y de ser así muestra el
> **historial de vuelo**. Caso contrario **rechaza** el ingreso (el rechazo se produce si el
> usuario no existe **o** si existe y la contraseña no coincide). Adicionalmente, si el usuario
> tiene **puntos suficientes** ofrece viajes de recompensa.

| Se pregunta | Respuesta | Estado |
|---|:---:|:---:|
| Cantidad de **condiciones** | **3** | ✅ |
| Cantidad de **acciones** | **3** | ⚠️ |
| Cantidad de **casos de prueba** | **4** | ⚠️ |
| Casos de prueba con **todas las condiciones verdaderas** | **1** | ⚠️ |

- **3 condiciones**: ¿el usuario existe? · ¿la contraseña coincide? · ¿tiene puntos suficientes?
- **3 acciones**: mostrar historial de vuelo · rechazar el ingreso · ofrecer viajes de recompensa.
- **4 casos**: las 2³ = 8 combinaciones se reducen porque hay **condiciones incompatibles** —
  si el usuario no existe, la contraseña y los puntos son irrelevantes:

  | # | Usuario existe | Contraseña OK | Puntos suficientes | Acción |
  |---|---|---|---|---|
  | 1 | No | — | — | Rechazar |
  | 2 | Sí | No | — | Rechazar |
  | 3 | Sí | Sí | No | Mostrar historial |
  | 4 | Sí | Sí | Sí | Mostrar historial + ofrecer recompensa |

- **1 caso con todas verdaderas**: el caso 4.

> El conteo de acciones, casos y "todas verdaderas" es **mi deducción**: el formulario no revela
> la clave de las que el alumno erró. El **3 de condiciones sí está confirmado**, y la lógica de
> reducción es la misma que la del gimnasio (5.1), que sí tiene clave oficial. Igual conviene
> verificarlo con el profe.

---

# 6. Verificación y Validación

### 6.1 Diferencia entre VER y VAL ✅

*(2025)*

**Respuesta: "VER asegura que el producto cumple con lo especificado; VAL asegura que el
producto satisface la necesidad del usuario."**

Distractores que aparecieron: *"VAL es opcional y VER obligatorio"* · *"VER es opcional y VAL
obligatorio"* · *"VER mide la satisfacción del usuario; VAL el cumplimiento de las
especificaciones"* (invertida) · *"VER y VAL son equivalentes, ambos miden defectos"*. Ninguna
de las dos áreas es opcional.

### 6.2 Correspondencia de tres acciones ✅

*(2025)*

> 1. Implementar **revisiones** de documentos de requisitos y diseño.
> 2. Ejecutar **pruebas de sistema** para verificar cumplimiento de **especificaciones**.
> 3. Organizar **pilotos con usuarios finales** para confirmar que el producto satisface **sus
>    necesidades**.

**Respuesta: (1) VER, (2) VER, (3) VAL.**

> La trampa es la 2: "pruebas de sistema" suena a producto terminado y tienta con VAL, pero se
> contrastan contra **la especificación** → **VER**. Lo que define VAL es **quién juzga**: si
> juzga el usuario contra su necesidad, es VAL.

### 6.3 Proyecto bancario ✅

*(2025)*

> 1) Se realizan **inspecciones de requisitos y revisiones de diseño**.
> 2) Luego se ejecutan **pruebas de aceptación con clientes reales**.

**Respuesta: la primera es VER y la segunda es VAL.**

Inspección y revisión = técnicas **estáticas** → VER. Aceptación **con clientes reales** → VAL.

### 6.4 QA ejecuta pruebas para comprobar que cada requisito funcional fue implementado ✅

*(2025)*

> El objetivo es asegurar que **"lo construido" cumpla con "lo especificado"**.

Opciones: OT · VAL · OPD · **VER** · Ninguna

**Respuesta: VER.**

> Que lo haga "el equipo de QA" **no lo convierte en PPQA**. PPQA evalúa **procesos y productos
> contra estándares y procedimientos de la organización**; acá se contrasta el producto contra
> **su especificación** → VER.

### 6.5 ¿En cuáles momentos puede realizarse una Revisión? ✅

*(2016 — respuesta marcada: E, Todas las anteriores)*

- A) En la primera entrevista con el cliente (antes de haber escrito la primera minuta)
- B) En la etapa de Análisis
- C) Al estar cerca de terminar la etapa de Programación
- D) En la etapa de Diseño

**Respuesta: Todas.** Las revisiones son la **primera forma de prueba aplicable** y se pueden
hacer en **cualquier momento** del ciclo, a diferencia de las pruebas dinámicas, que necesitan
el sistema andando.

### 6.6 Objetivo de la prueba de regresión *(pregunta a desarrollar, 2016)*

Volver a ejecutar casos de prueba ya existentes después de un cambio o corrección, para
verificar que **lo que antes funcionaba sigue funcionando**. No busca validar el fix (eso es la
prueba de **confirmación**), sino detectar que el arreglo **no rompió otra cosa**.

---

# 7. Gestión de proyectos

### 7.1 ¿En qué momento del ciclo de vida definiría los controles (puntos de control y monitoreo)? ✅

*(2020 · 2021)*

Opciones: Inicio · **Planificación** · Fin · Ejecución

**Respuesta: Planificación.**

Los puntos de control y los hitos se definen **al planificar**, en la EDT. En ejecución se
**usan**, no se definen.

### 7.2 "Cualquier desvío encontrado dentro del control y monitoreo de un proyecto debe ser resuelto" ✅

*(2020 · 2021)*

**Respuesta: Falso.**

Sólo se actúa sobre las **desviaciones significativas** — las que, sin resolver, **impiden al
proyecto cumplir sus objetivos**. Lo mismo vale para riesgos: se tratan según **umbrales
definidos**, no ante cualquier variación.

### 7.3 La planificación de un proyecto incluye ✅

*(2012 · 2015 — respuesta marcada: A, B y D)*

- **A) La estimación de las tareas** ✅
- **B) Determinación de los recursos** ✅
- C) Pago a los recursos → no es PP
- **D) Identificación de riesgos** ✅
- E) Especificación detallada de la arquitectura del software a construir → es **TS**, no PP

### 7.4 Actividades/procesos que forman parte de la gestión de proyectos ✅

*(2012 — respuesta marcada: E, Todas las anteriores)*

Definir las actividades · Estimar la duración de las actividades · Elaborar presupuestos de
proyecto · Definir equipo del proyecto → **todas**.

### 7.5 "Definir el Equipo del Proyecto" incluye ✅

*(2012 — respuesta marcada: A y C)*

- **A) Determinar roles del proyecto** ✅
- B) Estimar el esfuerzo previsto para cada rol → **no**
- **C) Determinar las responsabilidades para cada rol** ✅
- D) Controlar el cronograma para cada rol → **no**

### 7.6 Procesos relacionados con el **tiempo** en la gestión de proyectos ✅

*(2013 — respuesta marcada: B, C y D)*

- A) Definir las actividades → grupo **Alcance**
- **B) Establecer la secuencia de actividades** ✅
- **C) Estimar duración de actividades** ✅
- **D) Controlar el cronograma** ✅

> El distractor perfecto es "Definir las actividades": suena a cronograma pero pertenece a
> **Alcance**. Al grupo **Tiempo** le corresponden secuencia, duración, desarrollar el cronograma
> y controlarlo.

### 7.7 Procesos relacionados con la **coordinación** ✅

*(2015)*

- **A) Desarrollar el plan del proyecto** ✅
- B) Establecer la secuencia de actividades → Tiempo
- C) Estimar duración de actividades → Tiempo
- **D) Supervisar el trabajo del proyecto** ✅

### 7.8 Afirmaciones verdadero / falso ✅

*(2022)*

| Afirmación | |
|---|---|
| La planificación de un proyecto es un área de proceso que se cumple desde el **nivel 2** de maduración del CMMI | **V** |
| Un proyecto **puede no tener fin** | **F** — por definición tiene inicio y fin definidos |
| Los proyectos de software son **sólo de desarrollo** | **F** — hay de desarrollo, mantenimiento y despliegue (DES / MANT / DESPL) |
| Decir "tengo un plan de proyecto" es decir "tengo un diagrama de Gantt" | **F** — el Gantt es **una vista** del cronograma; el plan incluye alcance, estimaciones, recursos, riesgos, calidad, comunicación |

### 7.9 Determinar el esfuerzo de la fase de análisis en horas-persona ✅

*(2022 — 2 puntos)*

> Dos módulos independientes X y B. Duración y esfuerzo en **días**, el esfuerzo interpretable
> como **días-persona**. Un día-persona = **8 horas**. Ciclo de vida cascada.
>
> | Tarea | Duración | Esfuerzo |
> |---|---|---|
> | Analizar X | 3 días | **3 días** |
> | Diseñar X | 5 días | 5 días |
> | Codificar X | 4 días | 4 días |
> | Probar X | 5 días | 5 días |
> | Analizar B | 2 días | **3 días** |
> | Diseñar B | 4 días | 5 días |
> | Codificar B | 3 días | 6 días |
> | Probar B | 3 días | 5 días |

Opciones: 24 · **48** · 3 · 6 · 29 · 136

**Respuesta: 48 horas-persona.**

`Analizar X (3) + Analizar B (3) = 6 días-persona × 8 h = 48 h`

> **La trampa está en la columna que mirás.** *Analizar B* dura **2 días** pero consume **3
> días-persona** (dos personas parte del tiempo). Si sumás **duración** te da 5 días → 40 h, que
> ni siquiera está entre las opciones. El esfuerzo **se suma**; la duración **no**, porque las
> tareas de módulos independientes corren en paralelo. La opción **24** es la trampa de sumar un
> solo módulo; **136** es sumar todo el proyecto.

### 7.10 EDT — tareas predecesoras ✅

*(2024)*

> El producto final está compuesto por **3 módulos independientes: X, Y, Z**. Tareas de la EDT:
> Analizar / Diseñar / Codificar / Probar, para cada módulo.
> Nota: sólo **predecesoras directas**.

| Pregunta | Respuesta |
|---|---|
| Predecesora(s) directa(s) de **Codificar X** | **Diseñar X** |
| Tarea(s) que **dan inicio al proyecto** | **Analizar X, Analizar Y y Analizar Z** |

> Dos cosas. (a) *Directa* significa la inmediatamente anterior: Analizar X precede a Diseñar X
> que precede a Codificar X, pero **Analizar X no es predecesora directa** de Codificar X.
> (b) Los módulos son **independientes**, así que los tres análisis arrancan **en paralelo**: son
> **tres** tareas de inicio, no una.

---

# 8. Ingeniería de Software — conceptos generales

### 8.1 Entre los principios de la Ingeniería de Software están ✅

*(2012 · 2013 · 2015 — las tres veces la misma respuesta, cambiando las letras)*

- A) Las personas y el tiempo son intercambiables → **falso**, es justo lo contrario
- **B) Haz de la calidad la razón de trabajar** ✅
- C) Primero hazlo rápido, luego hazlo correcto → falso
- **D) Probar, probar y probar** ✅

*(En 2012 la respuesta fue sólo D porque B no figuraba entre las opciones.)*

### 8.2 Etapa que consiste en comprobar que el software realiza correctamente las tareas indicadas en la especificación ✅

*(2013)*

Opciones: Análisis de requerimientos · Planificación · Diseño · **Prueba** · Mantenimiento

**Respuesta: Prueba.**

### 8.3 Objetivo primario de la Ingeniería de Software

*(2015 — sin clave confirmada)* ⚠️

- A) Definir las actividades
- B) Entender el problema
- **C) Construir un producto de alta calidad de una manera oportuna** ⚠️
- D) Hacer software rentable de una manera oportuna

El alumno marcó C. Es coherente con la definición IEEE (enfoque sistemático, disciplinado y
cuantificable), pero **el examen no tiene marca de corrección**, así que tomalo con pinzas.

### 8.4 Tipos de mantenimiento

Aparece en 2013 (evolutivo), 2015 (a desarrollar) y 2016 (adaptativo).

| Tipo | Objetivo |
|---|---|
| **Correctivo** | Corregir errores detectados |
| **Evolutivo / perfectivo** | Incorporaciones, modificaciones y eliminaciones necesarias para **cubrir la expansión o cambio en las necesidades del usuario** |
| **Adaptativo** | Modificaciones que afectan a los **entornos** donde opera el sistema (hardware, software de base, gestores de BD, comunicaciones) |
| **Preventivo** | Mejorar la calidad interna / mantenibilidad, sin cambio funcional visible |

> En 2016 preguntaron cuál **"elimina requerimientos que quedan fuera del alcance de las
> necesidades del usuario"** y el alumno respondió "B y F" y lo erró. Por la definición de arriba
> eso es **evolutivo** (las *eliminaciones* para cubrir el cambio de necesidades forman parte del
> evolutivo/perfectivo). ⚠️ Sin clave confirmada.

### 8.5 Mejores prácticas en la gestión de requisitos ✅

*(2012 — respuesta marcada: A y D)*

- **A) Usar herramientas para la gestión de requisitos** ✅
- B) Mantener copias impresas de los casos de uso → no
- C) Asegurar la evolución de los requisitos
- **D) Priorizar los requisitos** ✅

### 8.6 Prácticas recomendadas para el desarrollo de requisitos

*(2013 ✅ — el alumno la erró y el profesor marcó **H**)*

En 2013 las opciones eran: A) Verificar requisitos · B) Priorizar requisitos ·
C) Comunicación abierta · D) Validar requisitos · E) Involucrar a toda la gente implicada.
**H) A, D y E** → **Verificar + Validar + Involucrar a toda la gente implicada.**

En 2015 la misma pregunta con otras opciones (A) Establecer líneas base · B) Involucrar a toda
la gente implicada · C) Mantener un glosario · D) Validar · E) Verificar) — el alumno también
puso H, pero ahí ese "H" es **A, D y E** = líneas base + validar + verificar. ⚠️ Sin marca de
corrección en 2015.

### 8.7 La línea base de los requisitos ✅

*(2012 — respuesta marcada: E, Todas las anteriores)*

- A) Contiene los requisitos aprobados
- B) Permite detectar los cambios de alcance
- C) Puede servir como base para el desarrollo

### 8.8 Componentes que constituyen el software *(a desarrollar, 2012)*

**Programas + datos + documentos.**

---

# 9. Preguntas a desarrollar de los parciales viejos

Ya no se toman en este formato, pero marcan qué considera la cátedra el núcleo de la materia.

| Pregunta | Año |
|---|---|
| Enumere tres actividades involucradas en la monitorización de un proyecto | 2012 |
| Explique las diferencias entre los niveles de madurez **2 y 3** del CMMI | 2012 |
| Por qué es importante mantener la **trazabilidad** entre requisitos | 2012 · 2013 |
| Defina cuáles son los componentes que constituyen el software | 2012 |
| Una vez evaluados los procesos de la organización, ¿cuáles deberían ser los próximos pasos? | 2013 |
| ¿Es correcto afirmar que una organización que implementa CMMI genera **siempre** productos en tiempo y forma? | 2013 |
| Enumere tres actividades de la planificación que **no** sean del grupo Tiempo | 2013 |
| Diferencias entre "Gestionar la ejecución del proyecto" y "Supervisar el trabajo del proyecto" | 2015 |
| Explique qué es el mantenimiento evolutivo | 2015 |
| Defina qué es un proyecto | 2015 · 2016 |
| Elementos que conforman la **Representación de un Proceso según SPEM** | 2015 |
| Explique el objetivo de la prueba de regresión | 2016 |
| ¿Qué es un **desvío significativo** dentro de PMC? | 2016 |
| ¿Cuáles son las **dimensiones críticas** sobre las que las organizaciones se centran para mejorar su actividad? | 2016 |

> Dos de estas tienen respuesta corta y conviene tenerla lista:
> **desvío significativo** = el que, sin resolver, impide al proyecto cumplir sus objetivos ·
> **dimensiones críticas** = personas · métodos y procedimientos · herramientas y equipamiento.

---

# 10. Checklist de la semana

1. **Activo vs. producto de trabajo** — 4 o 5 puntos regalados si tenés el criterio del punto 3.2.
2. **Componentes requeridos = sólo las metas** — apareció 4 años seguidos.
3. **OPF diagnostica / OPD define y guarda** — entre las dos se llevan 6 preguntas de la serie.
4. **Niveles acumulativos y todo-o-nada** — si falta un área de nivel 2, estás en nivel 1.
5. **Particiones: contar la zona muerta** — es el error que se repite en los dos termómetros.
6. **Tablas de decisión: condiciones no binarias** — la categoría de 3 valores da 6 columnas, no 4.
7. **Esfuerzo ≠ duración** — sumá la columna esfuerzo.
8. **VER vs VAL: mirá contra qué se contrasta**, no quién lo hace ni en qué fase.
9. **"Ninguna de las opciones" existe y a veces es la correcta.**
10. **Desvío: sólo los significativos.**
