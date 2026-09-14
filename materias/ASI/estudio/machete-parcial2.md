# ASI — Machete del 2º Parcial

> Comisión 403 · Grupo 310 · Cátedra Riva.
> Armado el 2026-09-14 desde `materias/ASI/ASI.md` (Unidades 2, 3 y 4) y el contexto de cátedra `Contexto de Bancorp (V1.0).pdf`.
> Marcado **[CG]** = conocimiento general, **no sale del material de cátedra**. Todo lo demás sí.

---

## 0. Cómo viene el examen

**Un solo parcial para todas las comisiones**; cambian las preguntas, no los temas.
**Formato: práctico, con la teoría exigida ADENTRO de la resolución.** El docente lo dijo así: *"cuando vos me justificás algo, me vas a tener que definir el concepto teórico"*.

> Traducción operativa: **no hay un punto "teoría" separado**. Si te piden un perfil de puesto, la teoría es reproducir sus bloques componentes **aplicados al caso**. Si te piden el protocolo, la teoría son las actividades de la Gestión de Incidentes de ITIL **ejecutadas sobre el incidente concreto**. Nunca listes y clasifiques aparte: **definí al pasar, mientras resolvés**.

**Tres bloques:**

| # | Bloque | Unidad | Qué hay que producir |
|---|---|---|---|
| 1 | Gestión de servicios de TI | **U2** (ITIL) | Protocolo paso a paso + **≥2 niveles de escalado** + herramientas + **≥1 KPI** |
| 2 | Dirección de talento y capital humano | **U3** | Perfil de puesto y/o aviso de reclutamiento, con sus partes aplicadas |
| 3 | Higiene y seguridad laboral | **U4** | Riesgos laborales del **área** + medidas de prevención |

**Forma del enunciado** (evidencia del 1º parcial, 08.06.26): *proyecto asignado* + bloques numerados donde **cada sub-punto nombra el marco que hay que usar**. Leé el sub-punto: si dice "según taxonomía SEI", va SEI y nada más.

**Encadenamiento probable:** el 1º parcial cerraba con *"disparadores de la materialización del riesgo"* y *"plan de contingencia"*. El 2º arranca ahí: **ese riesgo ya se materializó y es el incidente**. No te piden identificar el riesgo — **el incidente viene dado**.

---

## 1. Bancorp de bolsillo

Entidad financiera nacional. 45 sucursales + Casa Central (CABA). Cuatro negocios: minorista · comercial y corporativa · institucional · inversión.
Valores útiles para justificar impacto y urgencia: **Confianza y Solidez · Agilidad · Cercanía**.

### Organigrama — de acá salen las áreas. NO INVENTES ÁREAS.

```
                       DIRECTORIO
                           │
                    GERENCIA GENERAL ····· Auditoría y Cumplimiento (staff)
                           │
 ┌──────────┬──────────┬───┴──────┬──────────┬───────────┐
GER. TI e  GER. BANCA GER. BANCA GER. ADM.  GER. CAPITAL GER. OPS.
INNOVACIÓN MINORISTA  EMPRESAS   Y FINANZAS HUMANO       BANCARIAS
  (GTI)
```

### Departamento de TI — al tope el **Gerente de TI (CIO/CTO)**

| # | Área | Puestos |
|---|---|---|
| **01** | Infraestructura, Redes y Telecomunicaciones | Coordinador de Infraestructura Bancaria · Especialistas en **Datacenter y Conectividad de Sucursales** · Administradores de Servidores y Almacenamiento |
| **02** | Ciberseguridad y Prevención del Fraude | **CISO** · Analistas de **SOC** y monitoreo de eventos · Especialistas en seguridad de canales digitales y criptografía |
| **03** | Ingeniería de Software y Canales Digitales | Coordinador de Desarrollo · Células de canales (Home Banking, Mobile, **APIs**) · Arquitectos e integración (**Middleware / ESB**) · **DBA Core y Data Warehouse** |
| **04** | Operaciones de TI y Soporte de Aplicaciones | Coordinador de **Sistemas Core** (core bancario, clearing, sistemas centrales) · Especialistas en **monitoreo 24×7** |
| **05** | PMO y Procesos | Líder de PMO (Scrum Masters, PM) · Analistas de procesos e integración digital |
| **06** | **Mesa de Ayuda Tecnológica (Help Desk)** | Coordinador de Soporte Interno · Técnicos de soporte a sucursales (hardware bancario, pinpads, ticketeadoras) |

### La traducción que hace el 70 % del bloque 1

| Rol ITIL (U2 §7.1) | Área de Bancorp |
|---|---|
| **1ª línea** — único punto de contacto del usuario | **[06] Mesa de Ayuda** |
| **2ª línea** — escalado **funcional** (especialista) | **[01]** redes/conectividad · **[02]** seguridad · **[03]** software/API/BD · **[04]** core/clearing |
| **Eje jerárquico** — escalado **jerárquico** | Coordinador del área → **Gerente de TI (CIO)** → Gerencia General |
| Gestión de **Eventos** (el Service Desk NO la puede hacer) | **SOC**, dentro de **[02]** · monitoreo 24×7 en **[04]** |

**Los 7 proyectos del contexto** (el enunciado te asigna uno): 1) Billetera Virtual · 2) Omnicanalidad (token unificado) · 3) Copiloto IA interno · 4) Portal del Empleado (EX) · 5) Core Inteligente IA/Big Data · 6) RPA en Back-Office · 7) Open Banking / APIs.

---

## 2. TEMA 1 — Incidente: protocolo, escalado, herramientas, KPI

### 2.1 Definiciones que tenés que soltar mientras resolvés

- **Incidente (ITIL 4):** *"una interrupción no planificada de un servicio o la reducción de la calidad de un servicio"*.
- **Incidente ≠ Evento.** El incidente **se informa** (usuario, soporte). Si la interrupción **se monitoriza**, ITIL la llama **evento** y la trata la Gestión de Eventos, que **no la puede hacer el Centro de Servicios**.
- **Objetivo de la práctica:** minimizar el impacto negativo **restaurando el funcionamiento normal del servicio lo más rápido posible**.
- **La velocidad de recuperación es la máxima prioridad** → por eso se aceptan **soluciones temporales (workaround) en vez de permanentes**. La causa raíz es de **Gestión de Problemas**, no de acá.
- **Vínculo con riesgos:** la comunicación del incidente por el usuario es **el disparador que alerta la materialización de un riesgo** que debería haber sido identificado. Las soluciones temporales y permanentes **son los planes de contingencia y recuperación**. Si afecta procesos críticos, se activa el **Plan de Continuidad de Negocio**.

### 2.2 El protocolo — tres etapas, escribilas en este orden

**ETAPA 1 — REGISTRO** (seis pasos, van todos)

| Paso | Qué hacés |
|---|---|
| Admisión del trámite | La Mesa de Ayuda evalúa **si el servicio está incluido en el SLA del cliente**; si no, lo reenvía a autoridad competente |
| Comprobación de no duplicación | Varios usuarios notifican el mismo incidente: se busca ticket abierto |
| Asignación de referencia | **Identificador unívoco** del ticket |
| Registro inicial | Hora, descripción, sistemas afectados |
| Información de apoyo | Del usuario por formulario, o de la **CMDB**, que interrelaciona los **CI** (elementos de configuración): hardware, software, documentación |
| Notificación | Si puede afectar a otros usuarios, se les avisa cómo impacta en su flujo de trabajo |

**ETAPA 2 — CLASIFICACIÓN**

| Paso | Qué hacés |
|---|---|
| Categorización | Categoría según tipo de incidente o grupo responsable. Se identifican los **servicios afectados** |
| **Prioridad** | Con criterios predefinidos, porque hay múltiples incidentes concurrentes |
| → **Impacto** | **Cómo afecta a los procesos de negocio** y/o **número de usuarios afectados** |
| → **Urgencia** | **Tiempo máximo de demora que acepta el cliente** y/o el nivel acordado en el **SLA** |
| Asignación de recursos / escalado | Ver 2.3 |
| Monitorización de estado y tiempo | Estados: registrado → activo → suspendido → resuelto → cerrado. El tiempo de resolución se estima **según SLA y prioridad** |

> **Prioridad = Impacto × Urgencia.** Justificalo con el caso: "el responsable de créditos no puede operar → se frena el otorgamiento en toda la sucursal (impacto alto: proceso de negocio crítico) + el SLA del core es de X minutos en horario bancario (urgencia alta) → **prioridad crítica**".

**ETAPA 3 — ANÁLISIS, RESOLUCIÓN Y CIERRE**

1. Se examina el incidente **con la KB (base de conocimiento)** para ver si coincide con uno ya resuelto y aplicar el procedimiento asignado.
2. Si **se escapa de las posibilidades de la Mesa de Ayuda**, se redirecciona a un nivel superior para investigación por expertos asignados → **escalado funcional**.
3. Si los expertos tampoco resuelven, se siguen los **protocolos de escalado predeterminados** → **escalado jerárquico**.
4. Durante todo el ciclo se actualiza la información en las bases correspondientes.

**Al solucionarse, los cuatro pasos de cierre — no te los saltees, valen puntos:**
**(1)** se **confirma con el usuario** que la solución es satisfactoria · **(2)** se incorpora el procedimiento de resolución a la **KB** · **(3)** se actualiza la **CMDB** sobre los CI implicados · **(4)** se **cierra** el incidente.

**Y no termina ahí:** ITIL 4 exige **mejora continua** — buscar soluciones de prevención que impidan que el problema se repita.

### 2.3 Escalado — las dos clases + la derivación concreta

| Clase | Definición de cátedra | En Bancorp |
|---|---|---|
| **Escalado funcional** | *"Se requiere el apoyo de un **especialista de más alto nivel**"*. En general la **2ª línea de soporte**, que puede ser personal de Gestión de Problemas | Mesa de Ayuda **[06]** → área especialista **[01]–[04]** |
| **Escalado jerárquico** | *"Se acude a un **responsable de mayor autoridad**"* para decisiones que escapan a las atribuciones del nivel — por ejemplo **asignar más recursos** | Coordinador de área → **Gerente de TI (CIO)** → Gerencia General |

**Disparador del escalado:** el incidente **no se resuelve en el tiempo acordado en el SLA**, o la decisión **escapa a la responsabilidad** del nivel. Decilo explícito, con un umbral: *"si a los 30 min de tomado no hay diagnóstico, escala a…"*.

**Tabla de derivación según el incidente** (armala en el examen con la columna del medio del caso que te toque):

| Si el incidente es… | 2º nivel (funcional) | 3º nivel / jerárquico |
|---|---|---|
| Caída de conexión de sucursal, VPN, enlace, datacenter | **[01] Infraestructura, Redes y Telecom.** — Especialista en Conectividad de Sucursales | Coordinador de Infraestructura Bancaria → CIO |
| Home Banking / App / API que devuelve error, timeout de integración | **[03] Ingeniería de Software** — célula de canales / arquitecto de integración (Middleware-ESB) | Coordinador de Desarrollo → CIO |
| Core bancario, clearing, batch nocturno, sistema central | **[04] Ops. de TI y Soporte de Aplicaciones** — Coordinador de Sistemas Core | CIO → Gerencia de Operaciones Bancarias |
| Base de datos lenta, bloqueo, corrupción, DW | **[03]** — DBA Core y Data Warehouse | Coordinador de Desarrollo → CIO |
| Acceso indebido, fraude, malware, indisponibilidad por ataque | **[02] Ciberseguridad** — Analistas de SOC → **CISO** | CISO → CIO → Gerencia General (+ Auditoría y Cumplimiento) |
| Pinpad, ticketeadora, PC o impresora de sucursal | Resuelve **[06]** en 1ª línea; si es hardware de red, pasa a **[01]** | Coordinador de Soporte Interno |

> **Regla de oro del docente:** *"las áreas tienen que salir del organigrama de Bancorp. No inventar áreas."* Nada de "área de soporte nivel 2" genérica: escribí **[01] Infraestructura, Redes y Telecomunicaciones** y el puesto.

### 2.4 Herramientas del proceso — las pide explícitamente

| Herramienta | Para qué, dicho como lo dice la cátedra |
|---|---|
| **Base de Conocimiento (KB)** | Se consulta al analizar el incidente (¿ya pasó?, ¿con qué procedimiento se resolvió?) **y se alimenta al cerrar**, con el procedimiento de resolución nuevo |
| **CMDB** y los **CI** (elementos de configuración) | Provee la información de apoyo en el registro: interrelaciona hardware, software y documentación del servicio. **Se actualiza al cierre** sobre los CI implicados — es la **Gestión de la Configuración del Servicio** |
| **Sistema de tickets / plataforma ITSM** | Clasificación, escalado, interacción con la CMDB y la KB |
| **Gestión de Cambios / Control de Cambios** | Si la resolución implica modificar un CI, va por **RFC**; el **CAB** aprueba. Si es urgente y no se puede demorar, **cambio de emergencia** vía **ECAB** o decisión del Gestor de Cambios |
| **Gestión de Versiones** | El despliegue del parche/fix versionado, si la solución pasa por software |
| **SLA** | Fija el tiempo de resolución comprometido y dispara el escalado al vencerse |

> **Ojo con el SLA:** el apunte **usa** SLA pero **no lo define formalmente, y NO menciona OLA ni UC**. Si querés nombrar la cadena SLA → OLA → UC, sabé que **no sale del material de esta cátedra** **[CG]**.

### 2.5 KPI — con al menos uno alcanza, pero elegí el que mide lo que te piden

| KPI | Qué mide |
|---|---|
| **Tiempo de resolución de incidente** | Tiempo medio para resolver, por categoría |
| **Resolución dentro del SLA** | % de incidentes resueltos dentro del tiempo acordado |
| **Tasa de resolución de primera llamada (FCR)** | % resuelto en el Service Desk en la primera llamada |
| **Cantidad de escalados** | Escalados de incidentes **no resueltos en el tiempo acordado** |
| Cantidad de incidentes repetidos | Repetidos con método de resolución ya conocido |
| Incidentes resueltos a distancia | Sin ir al lugar del usuario |
| Cantidad de incidentes | Registrados por el Service Desk, por categoría |
| Esfuerzo de resolución | Promedio de esfuerzo de trabajo, por categoría |

**Cómo se escribe un KPI para que valga:** nombre + fórmula + **meta + frecuencia + responsable**.
*Ej.: "**Resolución dentro del SLA** = (incidentes de categoría Conectividad resueltos en ≤ 2 h / total de esa categoría) × 100. **Meta ≥ 95 % mensual.** Responsable: Coordinador de Soporte Interno **[06]**."*

### 2.6 Esqueleto de respuesta listo para copiar

> **Incidente:** *(reproducí el del enunciado)*. **Servicio afectado:** … **Usuario que reporta:** …
> **1. Registro** — Mesa de Ayuda **[06]**: verifica SLA, chequea duplicados, abre ticket INC-…, registra hora/descripción/sistemas, consulta la CMDB por los CI del servicio, notifica a los demás usuarios afectados.
> **2. Clasificación** — categoría …; **impacto** … (procesos de negocio y usuarios afectados); **urgencia** … (SLA); **prioridad** … Estado: activo. Tiempo objetivo: … según SLA.
> **3. Resolución** — consulta a la **KB**; si hay coincidencia, se aplica el procedimiento y se pasa a cierre. Si no: **escalado funcional** a **[0x] …** (puesto), que hace … Si en X min no resuelve: **escalado funcional 2** a **[0y] …** Si requiere recursos o decisión que excede al área: **escalado jerárquico** al Coordinador de … y al **Gerente de TI (CIO)**.
> **4. Cambio** — la solución modifica el CI …: se emite **RFC**, aprueba el **CAB** (o **ECAB** si es emergencia) y se despliega con **Gestión de Versiones**.
> **5. Cierre** — se confirma con el usuario, se **carga el procedimiento en la KB**, se **actualiza la CMDB**, se cierra el ticket.
> **6. Medición** — KPI: … = … Meta … Responsable …
> **7. Mejora continua** — se deriva a **Gestión de Problemas** para causa raíz y prevención de recurrencia.

### 2.7 Lo que te baja puntos

- Inventar áreas que no están en el organigrama.
- Poner "escalo a nivel 2" sin decir **a qué área y a qué puesto**, y **por qué**.
- Un solo nivel de escalado: piden **al menos dos**.
- Olvidar el **cierre** (confirmar + KB + CMDB).
- Buscar la **causa raíz** dentro de la gestión de incidentes: eso es **Gestión de Problemas**. Acá se restaura el servicio, aunque sea con workaround.
- KPI sin meta ni responsable.

---

## 3. TEMA 2 — Talento y capital humano

### 3.1 Perfil de puesto — la plantilla de cátedra

**Perfil ≠ descripción de puesto.** La descripción dice **qué se hace en el puesto**; el perfil dice **qué tiene que tener la persona** para hacerlo. Decilo en una línea antes de la ficha: ahí está la teoría.

| Bloque | Campos — **van todos, ésta es "la parte teórica"** |
|---|---|
| **Identificación** | Nombre del puesto · **Área** · **Objetivo del puesto** · **El puesto reporta a** · **Personal a cargo** |
| **Descripción de tareas** | Principales tareas y responsabilidades, redactadas **como acción + finalidad**: *"analizar los procesos operativos… **con la finalidad de** desarrollar e instalar sistemas de información"* |
| **Perfil del puesto** | **Estudios · Experiencia requerida · Idiomas · Conocimientos específicos · Capacidades y habilidades** |

**El truco de redacción:** cada tarea va en infinitivo + "**con la finalidad de**" + el para qué. Es el formato del ejemplo de cátedra (*Encargado de Sistemas*, Instituto de Bioquímica Clínica).

**Capacidades y habilidades del ejemplo de cátedra** (sacá de acá y no inventes): liderazgo · habilidad analítica · iniciativa · flexibilidad · orientación al cliente · manejo de personal · trabajo en equipo · responsabilidad · disciplina · toma de decisiones.

**Competencias:** **genéricas** (proactividad, diálogo fluido, trabajo en equipo) y **específicas** (propias del puesto).
**Fácil de definir:** estudios, conocimientos, datos objetivos (edad, educación, experiencia). **Difícil:** competencias y características personales, relaciones dentro de la organización (**el organigrama**), plan de carrera del candidato.

**Para qué se define el perfil:** para poder hacer **búsqueda, entrevista y selección**. *"El objetivo fundamental es cubrir la posición con quien más se adecue a los requerimientos del mismo."*

> **Si el puesto es de Bancorp**, sacá el "reporta a" y el "personal a cargo" **del organigrama de TI**. Ej.: *Especialista en Conectividad de Sucursales* → Área **[01]**, reporta al **Coordinador de Infraestructura Bancaria**, sin personal a cargo.

### 3.2 El Anuncio (aviso de reclutamiento) — cinco partes + AIDA

**Fórmula de cátedra: Perfil + Puesto + Fuente → Anuncio.**

**Las cinco partes componentes — la teoría exigida, aplicada:**

| # | Parte | Qué va adentro |
|---|---|---|
| 1 | **Definir la organización** | Quién es la empresa que busca |
| 2 | **Describir la posición o puesto** | Responsabilidades, **lugar de trabajo**, viajes y todo dato relevante (la ejercitación pide también **horarios**) |
| 3 | **Requisitos excluyentes y no excluyentes** | Conocimientos, competencias, experiencia — **separados en las dos categorías**, esto se olvida siempre |
| 4 | **Qué ofrece la empresa** | Desarrollo de carrera, beneficios |
| 5 | **Otras cuestiones** | A quién escribir para postularse, **plazo de recepción del CV**, si hay que indicar pretensiones económicas, foto |

**Modelo AIDA — el orden en que se redacta**, *"para que el llamado sea efectivo y los mejores perfiles se interesen en nosotros"*:

| Paso | Qué hace | Cómo se ve en el aviso |
|---|---|---|
| **A — Atención** | Llamativo, que destaque entre los demás | **Título potente** |
| **I — Interés** | Motivar a seguir leyendo describiendo **los desafíos técnicos, no solo requisitos** | Proyecto y desafíos |
| **D — Deseo** | Ser selectivos: generar deseo en quien cumple el perfil y **descartar suavemente a quien no** | Requisitos excluyentes/no excluyentes + **propuesta de valor** |
| **A — Acción** | Medios de contacto claros para postularse sin vueltas | Instrucciones de postulación |

> Las dos cosas se combinan: **AIDA da el orden, las cinco partes dan el contenido.** Escribí el aviso como aviso —con título, párrafos y bullets— y que se note dónde está cada parte.

### 3.3 Reclutamiento — por si el enunciado abre el proceso

**Definición de cátedra:** reclutamiento es *"el proceso de **atraer, seleccionar e incorporar** personal"* — el proceso completo, no solo la convocatoria.

**Fuentes de aprovisionamiento**

| Internas | Externas |
|---|---|
| Ascensos / descensos · Transferencias | **Canales digitales:** portales de empleo, redes sociales, bolsas de universidades · **Intermediarios:** agencias, asociaciones profesionales, sindicatos · **Tradicionales y directos:** ferias de empleo, referencias, **avisos** |

| | Ventajas | Desventajas |
|---|---|---|
| **INTERNO** | Más económico · Más rápido · Más seguro en resultados · Motivación · Retorno de la inversión en capacitación | Exige potencial de los empleados · Exige oportunidades de progreso · Conflictos de intereses · Mantiene el *status quo* · Problemas con políticas salariales |
| **EXTERNO** | Renueva los RRHH · Aprovecha la capacitación que trae el postulante | Más lento · Más costoso · Menos seguro · Percibido como desleal |

**Proceso completo, 20 pasos:** (1) posición a cubrir → (2) descripción del puesto → (3) perfil → (4) candidatos internos → (5) cómo buscar → (6) fuentes → (7) **anuncio** → (8) recepción de candidaturas → (9) revisión de antecedentes → (10) entrevistas, 1–2 rondas → (11) evaluaciones específicas y psicológicas → (12) formulación de candidaturas → (13) informes de finalistas → (14) presentación al **cliente interno** → (15) **selección del finalista por el cliente interno** → (16) negociación → (17) oferta por escrito → (18) comunicación a los que quedaron afuera → (19) admisión → (20) **inducción**.

> **Frase que suma:** el reclutamiento puede delegarse en Capital Humano, pero **la decisión final del ingreso (paso 15) es del gerente de sistemas**, que es el cliente interno: el costo de una mala incorporación lo paga su área.

**Decisiones de la planificación de la búsqueda:** ¿fuentes? · ¿quiénes participan de la selección? · ¿cuántas entrevistas? · ¿evaluación psicológica/física (**ART**)? · ¿cómo se presentan los finalistas al cliente interno?

**Job Posting (auto-postulación):** dar aviso de oportunidades de transferencia y promoción · indicar metodología de selección · **notificar antes de comenzar la búsqueda externa** · aclarar reglas (antigüedad, tiempo en el puesto actual) · especificar puesto y perfil.

**Consultor externo, cuándo:** confidencialidad · búsquedas complejas · se requiere visión imparcial · outsourcing para bajar costos.

### 3.4 Por si cae evaluación de desempeño

Tres actividades: **definir el puesto** (responsabilidades y criterios) → **evaluar** con algún tipo de calificación → **retroalimentación**.
**Competencia (Le Boterf):** capacidades, conocimientos, habilidades, actitudes y experiencias puestas en juego para desempeñarse en un entorno. **Conductas observables, cuantificables y evaluables.**
**Tipos:** **básicas** (educación inicial/media) · **genéricas o transversales** (educación técnica/superior, amplio campo de profesiones) · **específicas** (ejercicio profesional, propias de la ocupación).
**Formato que pide la cátedra:** competencia → **≥2 factores** por competencia → **escala de 5 niveles acumulativos** (cada nivel incluye el anterior y agrega: *"además de las consideraciones del punto 3, es organizado y distribuye las tareas con eficacia"*).

### 3.5 Lo que te baja puntos

- Listar las partes del perfil o del aviso **aparte** en vez de aplicarlas. El docente lo dijo textual.
- Un aviso sin **requisitos excluyentes vs. no excluyentes** separados.
- Un aviso sin **cómo postularse y plazo** (parte 5).
- Un perfil sin **"reporta a"** y sin **objetivo del puesto**.
- Poner solo requisitos duros: falta **capacidades y habilidades** (competencias blandas).

---

## 4. TEMA 3 — Higiene y seguridad laboral

**Lo que el docente aclaró: NO se ata a un puesto puntual, sino a un ÁREA DE TRABAJO** (ej. *el área de desarrollo del banco Bancorp*). Escribí sobre el área, no sobre una persona.

### 4.1 Definiciones de arranque

- **Riesgo laboral:** la **posibilidad de que un trabajador sufra un determinado daño derivado del trabajo**.
- **Daños derivados del trabajo:** enfermedades o accidentes laborales.
- **Salud (OMS):** *no es la mera ausencia de afecciones y enfermedades, sino el **estado de plena satisfacción física, psíquica y social***. Por eso no alcanza con hablar de accidentes.
- **Factor de riesgo / peligro:** una condición de trabajo **cuando puede originar daño**.

### 4.2 Condiciones de trabajo — los cuatro grupos (el checklist para barrer el área)

| Grupo | Qué incluye |
|---|---|
| **De seguridad** | Locales, instalaciones, equipos, almacenamiento y manipulación de cargas, inflamables, químicos |
| **Ambientales** | Agentes físicos, químicos y biológicos; calor y frío; **iluminación**; ventilación |
| **Carga de trabajo** | **Física y mental** |
| **Organización del trabajo** | **Monotonía, repetitividad, aislamiento, participación** |

**Tres tipos de riesgo:** de **accidentes** · **ambientales** (dependen de la **dosis** recibida; efectos *agudos* inmediatos vs. *crónicos* diferidos) · **psicosociales**.

**Agentes de riesgo ambiental:**

| Químicos | Físicos | Biológicos |
|---|---|---|
| Gases · Vapores · Nieblas · Polvos · Humos | **Ruido** · Vibraciones · Presiones extremas · Temperaturas extremas · Radiaciones | Insectos · Bacterias · Virus · Hongos · Mohos |

### 4.3 Los cuatro niveles de prevención primaria — ESTO ES LO QUE DECIDE LA NOTA

**Prevención primaria** = evitar el riesgo o su materialización. Es **la más eficaz y la más eficiente**, y se ordena de mayor a menor jerarquía:

| Orden | Acción | Objeto |
|---|---|---|
| **1** | **En el DISEÑO** — de instalaciones, equipos, herramientas y **puestos de trabajo** | Evitar el riesgo o minimizarlo |
| **2** | **En el ORIGEN** — evitar riesgos por defectos de fabricación, construcción o instalación | Eliminar o reducir el riesgo |
| **3** | **En el MEDIO DE TRANSMISIÓN** — interponer barreras entre el origen y la persona | Controlar el riesgo |
| **4** | **SOBRE LA PERSONA** — EPP, educación, vigilancia de la salud, reducción del tiempo de exposición | Proteger a la persona |

**Prevención secundaria:** la alteración de la salud **ya empezó** aunque no se manifieste → vigilancia de la salud, **diagnóstico precoz**, tratamiento eficaz.
**Prevención terciaria:** evitar reincidencias, recaídas, complicaciones o secuelas → tratamiento y **rehabilitación**.

> **La crítica que hace la cátedra, y cómo esquivarla:** "silla ergonómica, pausas activas y matafuegos" es **todo nivel 4 — sobre la persona, el escalón más débil**. Para cada riesgo que nombres, **proponé primero una medida de nivel 1 o 2** (diseño/origen) y recién después el EPP o la capacitación como complemento. **Decí explícitamente en qué nivel está cada medida**: ahí estás metiendo la teoría adentro de la resolución, que es lo que piden.

### 4.4 Las cinco disciplinas de la prevención

- **Seguridad en el Trabajo** — medidas en todas las fases de actividad para evitar o minimizar riesgos.
- **Higiene Industrial** — estudia dos variables, **el hombre y su ambiente de trabajo**. Ciclo: identificar agentes → medir la exposición (concentración y tiempo) → valorar contra valores de referencia → corregir → controlar periódicamente → **capacitar a los trabajadores sobre los riesgos identificados**.
- **Medicina del Trabajo** — exámenes preocupacionales y periódicos, psicotécnicos, aptitud para trabajos en altura, asistencia por accidentes, campañas.
- **Psicosociología del Trabajo** — precariedad, **estrés**, esfuerzo mental, monotonía, **acoso laboral (mobbing)**, **burn-out**.
- **Ergonomía** — **adaptación del puesto a la persona** (no al revés).

### 4.5 Catálogo listo: riesgos de un área de desarrollo / oficina bancaria

Barrido con los cuatro grupos de condiciones de trabajo. Para cada uno, la medida de nivel alto primero.

| Riesgo | Grupo / tipo | Prevención **en el diseño u origen** (nivel 1–2) | Complemento (nivel 3–4) |
|---|---|---|---|
| **Carga mental y fatiga** por exigencia cognitiva sostenida, guardias, incidentes en producción | Carga de trabajo · psicosocial | Diseñar la **distribución de la carga y las guardias**; dimensionar la dotación; definir ventanas de despliegue; acotar interrupciones | Pausas, capacitación en gestión del tiempo, vigilancia de la salud |
| **Estrés laboral** — *"desequilibrio sustancial entre la demanda y la capacidad de respuesta"* (Mc Grath) | Psicosocial | Rediseño de plazos y de la organización del trabajo; claridad de roles | Programa de salud ocupacional, asistencia psicológica |
| **Monotonía y trabajo repetitivo** (tareas encadenadas repetidas toda la jornada) | Organización del trabajo | **Rotación y enriquecimiento de tareas** desde el diseño del puesto | Pausas, variación de actividades |
| **Burn-out** — ataca especialmente cuando el trabajo **supera las ocho horas**, no se cambia de ambiente en largos períodos y está mal remunerado | Psicosocial | Control de la jornada; política de desconexión; movilidad interna | Detección precoz (**prevención secundaria**) |
| **Acoso laboral (mobbing)** — descendente, horizontal o ascendente | Psicosocial | **Protocolo de prevención y canal de denuncia** en el diseño organizativo | Capacitación a jefaturas |
| **Trastornos musculoesqueléticos** por postura estática y trabajo con pantalla | Carga física · ergonomía | **Diseño del puesto**: altura de plano de trabajo, monitor a la altura de los ojos, apoyo lumbar, espacio libre de movimiento | Silla regulable, pausas activas |
| **Fatiga visual** | Ambiental (iluminación) | **Diseño del layout**: luz natural, luminarias sin reflejo sobre pantallas, orientación de los puestos respecto de ventanas | Filtros, regulación de brillo |
| **Ruido** de oficina abierta | Ambiental (físico) | **Diseño acústico**: separar el área de desarrollo de la de atención, salas de reunión cerradas | Barreras (nivel 3), auriculares |
| **Riesgo eléctrico** — contacto directo/indirecto, quemaduras, **incendio originado por la electricidad** | Seguridad | **Instalación en origen**: tableros con disyuntor y térmica, canalización del cableado, puesta a tierra, UPS del datacenter | Señalización, capacitación, zona restringida |
| **Incendio y evacuación** | Seguridad | **Diseño**: salidas de emergencia, vías de circulación libres, detección y extinción, sectorización del datacenter | Matafuegos, señalización, **simulacros** |
| **Espacios de trabajo y zonas peligrosas** | Seguridad | Superficie y volumen adecuados, **separaciones** entre elementos, acceso solo a **trabajadores autorizados** al datacenter, **señalización** de zonas de riesgo | Control de acceso |
| **Caídas al mismo nivel** | Seguridad | Suelos **fijos, estables y no resbaladizos**, sin irregularidades; cableado canalizado, no suelto | Señalización de piso mojado |
| **Trabajo remoto / teletrabajo** | Organización | Obligaciones de la **Ley 27.555**: el empleador provee equipamiento y responde por las condiciones del puesto | Capacitación en ergonomía del hogar |

### 4.6 Sistema de gestión y legislación

**Elementos del Sistema de Gestión en Higiene y Seguridad:** administración y entrega de **EPP** · mediciones de desempeño (sistemas seguros de trabajo, **permisos de trabajo**, respeto de procedimientos) · mediciones de efectividad por auditorías, acciones correctivas e **indicadores de siniestralidad** · mediciones de agentes químicos por laboratorios acreditados · **preparación y respuesta ante emergencias**. Cierra con verificación (no conformidades, acciones correctivas y preventivas, auditorías internas y externas) y **revisión por la Dirección**.
**Certificación:** el apunte dice **OHSAS 18001** (es de 2014); la bibliografía del programa suma la familia **ISO 45000** — hoy la vigente es **ISO 45001:2018** **[CG]**.

| Norma | Qué regula |
|---|---|
| **Ley 19.587** — Higiene y Seguridad en el Trabajo (+ decreto reglamentario) | Marco general de condiciones de higiene y seguridad |
| **Ley 24.557** — Riesgos del Trabajo (1995) | Crea el sistema de **ART** y la **SRT** (Superintendencia de Riesgos del Trabajo) |
| **Ley 20.744** — Contrato de Trabajo | Relación laboral |
| **Ley 27.555** — Teletrabajo | Régimen legal del contrato de teletrabajo |

**Obligaciones de la ART** (por si pide el rol externo): brindar prestaciones preventivas y dinerarias · **evaluar periódicamente los riesgos** de las empresas afiliadas · **exámenes médicos periódicos** · **visitas para controlar el cumplimiento** · mantener un **registro de siniestralidad** por establecimiento · denunciar incumplimientos ante la SRT.
**Exámenes preocupacionales** (Res. SRT 37/10): conocer el estado de salud · detectar afecciones · determinar qué tarea puede hacer sin exponerse · **disminuir la conflictividad médico-legal**.

### 4.7 Lo que te baja puntos

- Responder por **puesto** cuando piden por **área**.
- Dar solo medidas de **nivel 4** (silla, pausas, matafuegos, EPP). Es el error que la cátedra marca explícitamente.
- Nombrar la medida sin **decir en qué nivel de prevención está**.
- Quedarse solo en riesgos de accidente y olvidar los **psicosociales** (estrés, monotonía, burn-out, acoso) y la **carga mental** — que son justamente los del área de desarrollo.
- No citar **ninguna ley**.

---

## 5. Checklist de los últimos 60 segundos

1. ¿Definí cada concepto **mientras** resolvía, o los listé aparte?
2. **Bloque 1:** ¿registro + clasificación (impacto/urgencia/prioridad) + resolución + **cierre con KB y CMDB**? ¿**Dos** escalados con **área y puesto del organigrama**? ¿Herramientas? ¿KPI **con meta y responsable**?
3. **Bloque 2:** ¿el perfil tiene **objetivo, reporta a, personal a cargo**? ¿El aviso tiene las **cinco partes**, con **excluyentes vs. no excluyentes** y **cómo postularse**? ¿Se lee con estructura **AIDA**?
4. **Bloque 3:** ¿hablé del **área**? ¿Cada riesgo tiene una medida de **nivel 1 o 2** antes del EPP? ¿Nombré el **nivel** de cada medida? ¿Metí los **psicosociales**? ¿Cité **19.587 / 24.557**?
5. ¿Todo lo que nombré como "área" **existe en el organigrama de Bancorp**?
