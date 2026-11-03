# ASI — Machete del 2º Parcial

> Unidades 2 (ITIL), 3 (Talento) y 4 (Higiene y Seguridad) + contexto Bancorp.

---

## Bancorp — Departamento de TI

Al tope: **Gerente de TI (CIO/CTO)**. Las áreas del escalado salen de acá.

| # | Área | Puestos |
|---|---|---|
| **01** | Infraestructura, Redes y Telecomunicaciones | Coordinador de Infraestructura Bancaria · Especialistas en Datacenter y Conectividad de Sucursales · Administradores de Servidores y Almacenamiento |
| **02** | Ciberseguridad y Prevención del Fraude | CISO · Analistas de SOC · Especialistas en seguridad de canales digitales y criptografía |
| **03** | Ingeniería de Software y Canales Digitales | Coordinador de Desarrollo · Células de canales (Home Banking, Mobile, APIs) · Arquitectos e integración (Middleware/ESB) · DBA Core y Data Warehouse |
| **04** | Operaciones de TI y Soporte de Aplicaciones | Coordinador de Sistemas Core (core, clearing, sistemas centrales) · Especialistas en monitoreo 24×7 |
| **05** | PMO y Procesos | Líder de PMO · Analistas de procesos |
| **06** | Mesa de Ayuda (Help Desk) | Coordinador de Soporte Interno · Técnicos de soporte a sucursales |

Gerencias del banco: TI e Innovación · Banca Minorista · Banca Empresas · Administración y Finanzas · Capital Humano · Operaciones Bancarias. Staff: Auditoría y Cumplimiento.

| Rol ITIL | Área |
|---|---|
| 1ª línea (único punto de contacto) | **[06] Mesa de Ayuda** |
| 2ª línea (escalado funcional) | **[01]** redes · **[02]** seguridad · **[03]** software/API/BD · **[04]** core/clearing |
| Eje jerárquico | Coordinador de área → **Gerente de TI (CIO)** → Gerencia General |

---

## 1. Gestión de incidentes

**Incidente (ITIL 4):** interrupción no planificada de un servicio o reducción de su calidad.
**Incidente ≠ evento:** el incidente se **informa**; si se **monitoriza**, es un **evento** (Gestión de Eventos, que no hace el Service Desk).
**Objetivo:** restaurar el funcionamiento normal del servicio lo más rápido posible. Se aceptan **soluciones temporales**. La causa raíz es de **Gestión de Problemas**.

### Protocolo

**1. Registro** — admisión del trámite (¿está el servicio en el **SLA**?) · comprobación de no duplicación · asignación de referencia única · registro inicial (hora, descripción, sistemas afectados) · información de apoyo (usuario o **CMDB**, que interrelaciona los **CI**) · notificación a otros usuarios afectados.

**2. Clasificación** — categorización y servicios afectados · **prioridad = impacto × urgencia**, donde **impacto** = cómo afecta a los procesos de negocio y/o nº de usuarios, y **urgencia** = tiempo máximo de demora que acepta el cliente y/o el SLA · asignación de recursos / escalado · monitorización de estado (registrado → activo → suspendido → resuelto → cerrado) y tiempo de resolución según SLA y prioridad.

**3. Análisis, resolución y cierre** — se examina con la **KB** buscando un incidente ya resuelto · si excede a la Mesa de Ayuda, **escalado funcional** a expertos · si ellos tampoco resuelven, **escalado jerárquico**. Al solucionarse: **(1)** confirmar con el usuario · **(2)** incorporar el procedimiento a la **KB** · **(3)** actualizar la **CMDB** · **(4)** cerrar. Después: **mejora continua**.

### Escalado

| Clase | Definición | En Bancorp |
|---|---|---|
| **Funcional** | Apoyo de un especialista de más alto nivel (2ª línea de soporte) | **[06]** → área especialista **[01]–[04]** |
| **Jerárquico** | Responsable de mayor autoridad, para decisiones fuera de las atribuciones del nivel (ej. asignar más recursos) | Coordinador → **CIO** → Gerencia General |

**Disparador:** el incidente no se resuelve en el tiempo acordado en el SLA, o la decisión excede al nivel.

| Incidente | 2º nivel | Jerárquico |
|---|---|---|
| Caída de conexión, VPN, enlace, datacenter | **[01]** Especialista en Conectividad de Sucursales | Coordinador de Infraestructura → CIO |
| Home Banking, App, API, integración | **[03]** Célula de canales / Arquitecto de integración | Coordinador de Desarrollo → CIO |
| Core bancario, clearing, batch | **[04]** Coordinador de Sistemas Core | CIO → Ger. Operaciones Bancarias |
| Base de datos, DW | **[03]** DBA Core y Data Warehouse | Coordinador de Desarrollo → CIO |
| Acceso indebido, fraude, malware | **[02]** Analistas de SOC → CISO | CISO → CIO → Gerencia General |
| Pinpad, PC, impresora de sucursal | **[06]** en 1ª línea; si es red, **[01]** | Coordinador de Soporte Interno |

### Herramientas

**KB** (se consulta al analizar y se alimenta al cerrar) · **CMDB** y los **CI** (información de apoyo en el registro, se actualiza al cierre) · **sistema de tickets / ITSM** · **Gestión de Cambios** (**RFC** aprobado por el **CAB**; **ECAB** si es emergencia) · **Gestión de Versiones** · **SLA**.

### KPI

Tiempo de resolución · **Resolución dentro del SLA** · Tasa de resolución de primera llamada · Cantidad de escalados (incidentes no resueltos en el tiempo acordado) · Incidentes repetidos · Incidentes resueltos a distancia · Cantidad de incidentes · Esfuerzo de resolución.

Se escribe: **nombre + fórmula + meta + frecuencia + responsable**.

---

## 2. Talento y capital humano

**Reclutamiento:** proceso de **atraer, seleccionar e incorporar** personal.
**Perfil ≠ descripción de puesto:** la descripción dice qué se hace en el puesto; el perfil, qué tiene que tener la persona.

### Perfil de puesto

| Bloque | Campos |
|---|---|
| **Identificación** | Nombre del puesto · Área · **Objetivo del puesto** · **Reporta a** · **Personal a cargo** |
| **Descripción de tareas** | Tareas y responsabilidades como **acción + "con la finalidad de"** |
| **Perfil** | Estudios · Experiencia requerida · Idiomas · Conocimientos específicos · **Capacidades y habilidades** |

Competencias: **genéricas** (proactividad, trabajo en equipo, diálogo) y **específicas** (del puesto).
Habilidades del ejemplo de cátedra: liderazgo, habilidad analítica, iniciativa, flexibilidad, orientación al cliente, manejo de personal, trabajo en equipo, responsabilidad, disciplina, toma de decisiones.

### Anuncio (aviso de reclutamiento)

**Perfil + Puesto + Fuente → Anuncio.** Cinco partes:

1. **Definir la organización**
2. **Describir la posición**: responsabilidades, lugar de trabajo, horarios, viajes
3. **Requisitos excluyentes y no excluyentes**: conocimientos, competencias, experiencia
4. **Qué ofrece la empresa**: desarrollo de carrera, beneficios
5. **Otras cuestiones**: a quién escribir, **plazo de recepción del CV**, pretensiones económicas, foto

**Modelo AIDA** (orden de redacción): **Atención** (título potente) → **Interés** (desafíos técnicos, no solo requisitos) → **Deseo** (requisitos + propuesta de valor) → **Acción** (cómo postularse).

### Fuentes de reclutamiento

| Internas | Externas |
|---|---|
| Ascensos / descensos · Transferencias | Portales de empleo, redes sociales, bolsas de universidades · Agencias, asociaciones profesionales, sindicatos · Ferias, referencias, **avisos** |

| | Ventajas | Desventajas |
|---|---|---|
| **Interno** | Más económico · Más rápido · Más seguro · Motivación · Retorno de la capacitación | Exige potencial y oportunidades de progreso · Conflictos de intereses · Mantiene el status quo |
| **Externo** | Renueva los RRHH · Aprovecha capacitación del postulante | Más lento · Más costoso · Menos seguro · Percibido como desleal |

### Proceso

Posición → descripción → perfil → candidatos internos → cómo buscar → fuentes → **anuncio** → recepción de candidaturas → revisión de antecedentes → entrevistas → evaluaciones → informes de finalistas → presentación al **cliente interno** → **selección por el cliente interno** → negociación → oferta por escrito → aviso a los no seleccionados → admisión → **inducción**.

---

## 3. Higiene y seguridad laboral

Se responde sobre un **área de trabajo**, no sobre un puesto puntual.

**Riesgo laboral:** posibilidad de que un trabajador sufra un daño derivado del trabajo.
**Daños derivados del trabajo:** enfermedades o accidentes laborales.
**Salud (OMS):** no la mera ausencia de enfermedad, sino el estado de plena satisfacción **física, psíquica y social**.
**Factor de riesgo / peligro:** condición de trabajo que puede originar daño.

### Condiciones de trabajo

| Grupo | Incluye |
|---|---|
| **De seguridad** | Locales, instalaciones, equipos, manipulación de cargas, inflamables, químicos |
| **Ambientales** | Agentes físicos, químicos y biológicos; calor y frío; iluminación; ventilación |
| **Carga de trabajo** | Física y mental |
| **Organización del trabajo** | Monotonía, repetitividad, aislamiento, participación |

**Tres tipos de riesgo:** de accidentes · ambientales (según la dosis; efectos agudos o crónicos) · psicosociales.
**Agentes ambientales:** químicos (gases, vapores, nieblas, polvos, humos) · físicos (ruido, vibraciones, presiones y temperaturas extremas, radiaciones) · biológicos (insectos, bacterias, virus, hongos, mohos).

### Niveles de prevención

**Primaria** — evitar el riesgo o su materialización. Es la más eficaz y eficiente, y va **de mayor a menor jerarquía**:

| Orden | Acción | Objeto |
|---|---|---|
| **1** | **En el diseño** — instalaciones, equipos, herramientas y puestos de trabajo | Evitar o minimizar el riesgo |
| **2** | **En el origen** — defectos de fabricación, construcción o instalación | Eliminar o reducir |
| **3** | **En el medio de transmisión** — barreras entre el origen y la persona | Controlar |
| **4** | **Sobre la persona** — EPP, educación, vigilancia de la salud, menor tiempo de exposición | Proteger |

**Secundaria** — la alteración de la salud ya empezó: vigilancia, diagnóstico precoz, tratamiento.
**Terciaria** — evitar recaídas y secuelas: tratamiento y rehabilitación.

> EPP, sillas y pausas son **nivel 4**. Para cada riesgo hay que dar primero una medida de **nivel 1 o 2**.

### Cinco disciplinas

Seguridad en el Trabajo · **Higiene Industrial** (estudia el hombre y su ambiente: identificar, medir, valorar, corregir, controlar, capacitar) · Medicina del Trabajo · **Psicosociología del Trabajo** (estrés, monotonía, acoso, burn-out) · **Ergonomía** (adaptar el puesto a la persona).

### Riesgos de un área de desarrollo

| Riesgo | Prevención nivel 1–2 | Complemento nivel 3–4 |
|---|---|---|
| Carga mental y fatiga | Distribuir carga y guardias; dimensionar dotación; ventanas de despliegue | Pausas, vigilancia de la salud |
| Estrés laboral | Rediseño de plazos y organización del trabajo; claridad de roles | Programa de salud ocupacional |
| Monotonía y trabajo repetitivo | Rotación y enriquecimiento de tareas | Pausas |
| Burn-out (aparece con jornadas > 8 h) | Control de jornada; desconexión; movilidad interna | Detección precoz |
| Acoso laboral (mobbing) | Protocolo de prevención y canal de denuncia | Capacitación a jefaturas |
| Trastornos musculoesqueléticos | Diseño del puesto: altura del plano, monitor a la altura de los ojos, espacio libre | Silla regulable, pausas activas |
| Fatiga visual | Layout: luz natural, luminarias sin reflejo, orientación de puestos | Regulación de brillo |
| Ruido | Separar desarrollo de atención; salas cerradas | Barreras, auriculares |
| Riesgo eléctrico | Tableros con disyuntor y térmica, cableado canalizado, puesta a tierra, UPS | Señalización, capacitación |
| Incendio y evacuación | Salidas de emergencia, vías libres, detección y extinción, sectorización | Matafuegos, simulacros |
| Espacios y zonas peligrosas | Superficie y volumen adecuados, separaciones, acceso solo a autorizados | Señalización, control de acceso |
| Caídas al mismo nivel | Suelos fijos, estables y no resbaladizos; cableado canalizado | Señalización |
| Teletrabajo | Ley 27.555: el empleador provee equipamiento y responde por el puesto | Capacitación en ergonomía |

### Legislación

| Norma | Regula |
|---|---|
| **Ley 19.587** | Higiene y Seguridad en el Trabajo |
| **Ley 24.557** | Riesgos del Trabajo — crea las **ART** y la **SRT** |
| **Ley 20.744** | Contrato de Trabajo |
| **Ley 27.555** | Teletrabajo |

**Sistema de gestión:** entrega de EPP · permisos de trabajo · auditorías, acciones correctivas e indicadores de siniestralidad · mediciones de agentes químicos · preparación y respuesta ante emergencias · revisión por la Dirección. Certificación **OHSAS 18001** (hoy ISO 45001).
**ART:** evalúa periódicamente los riesgos, hace los exámenes médicos periódicos, visita para controlar el cumplimiento, lleva el registro de siniestralidad y denuncia incumplimientos a la SRT.
