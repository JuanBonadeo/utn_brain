# Guía para el parcial

## Regla general

**La teoría va adentro de la respuesta.** Cada concepto que usás, lo definís en una línea y lo aplicás al caso. Las áreas siempre salen del organigrama de Bancorp.

---

## PUNTO 1: ITIL

### Incidente vs. evento

- **Incidente:** interrupción no planificada o baja de calidad de un servicio. **Lo informa una persona.**
- **Evento:** cambio de estado importante de un servicio o CI. **Lo detecta la monitorización.**
- Tipos de evento: **informativo** (no requiere acción ahora), **advertencia** (actuar antes del impacto), **excepción** (se violó una norma, requiere acción).

| | Evento | Incidente |
|---|---|---|
| Cómo llega | Monitorización | Lo informa una persona |
| Quién lo maneja | [02] SOC / [04] monitoreo 24×7 | [06] Mesa de Ayuda |
| Pasos | 7 | 3 etapas |

### Cómo se gestionan los eventos (7 pasos)

1. **Detección:** ocurre el suceso.
2. **Notificación:** se avisa al equipo responsable.
3. **Filtrado:** se decide si merece atención.
4. **Clasificación:** tipo y prioridad.
5. **Correlación:** ¿hay eventos similares? ¿Hay que actuar?
6. **Respuesta:** se elige qué hacer.
7. **Revisión y cierre.**

**Qué puede pasar con un evento:** califica como incidente → **Gestión de Incidentes** · se repite fuera de lo normal → **Gestión de Problemas** · hay que modificar algo → **Control de Cambios**.
**Quién:** personal técnico de 2ª o 3ª línea, **nunca la Mesa de Ayuda**.
**Herramientas:** monitorización **activa** (revisa CI uno a uno) y **pasiva** (detecta y correlaciona alertas).

### Cómo se gestionan los incidentes (3 etapas)

1. **Registro:** verificar SLA → ¿ya hay ticket? → ID → datos (fecha, hora, descripción, sistemas) → consultar CMDB → avisar a los afectados.
2. **Clasificación:** categoría → **impacto** (procesos y cantidad de usuarios) + **urgencia** (demora aceptable / SLA) = **prioridad**.
3. **Resolución y cierre:** buscar en la **KB** → **escalado funcional** a un área especialista → **escalado jerárquico** (coordinador → CIO) → cierre: **confirmar con el usuario, cargar en KB, actualizar CMDB, cerrar**.

**Escalado:**

- **Funcional:** a un especialista de más nivel (2ª línea).
- **Jerárquico:** a alguien con más autoridad (para recursos o decisiones).
- Se escala cuando **no se resuelve en el tiempo del SLA** o la decisión excede al nivel.

### Bases y herramientas

- **ITSM:** los tickets.
- **KB:** cómo se resolvió antes.
- **CMDB:** los CI y cómo se relacionan.
- **SLA:** el acuerdo de niveles de servicio (tiempos y disponibilidad).

### Cuándo pasa a Gestión de Problemas

- **Problema:** causa de uno o más incidentes. El incidente se **resuelve**; el problema se **investiga**.
- **Reactiva:** no hay solución conocida.
- **Proactiva:** ya hay solución temporal, pero **se repite**.

### Acciones de Gestión de Problemas (5 pasos)

1. **Registro:** CI, síntomas, solución temporal, servicio, prioridad, estado activo.
2. **Clasificación y recursos:** tipo + qué áreas asignás.
3. **Análisis:** buscar la causa (no siempre es técnica) → **error conocido**.
4. **Control de errores:** proponer una **RFC** a Control de Cambios. **Problemas no implementa.**
5. **PIR y cierre:** verificar que funcionó y cerrar.

### Otras prácticas de ITIL

Incidentes · Centro de Servicios · Eventos · **Control de Cambios** (RFC, CAB/ECAB) · **Gestión de Versiones** (despliega el cambio) · **Gestión de la Configuración** (CMDB) · Activos de TI. Una línea por cada una explicando por qué entra en el caso.

### KPI (si lo piden)

Nombre + fórmula + meta + responsable. Ej.: **Resolución dentro del SLA** = incidentes resueltos a tiempo / total × 100, meta ≥ 95 %.

### Áreas de Bancorp

[01] Infraestructura y Redes · [02] Ciberseguridad · [03] Ingeniería de Software · [04] Operaciones y Core · [05] PMO · [06] Mesa de Ayuda · Gerente de TI (CIO).

---

## PUNTO 2: Talento y Seguridad

### Anuncio de puesto (5 partes, en orden AIDA)

1. **Título llamativo** (Atención)
2. **Quién es la empresa**
3. **El proyecto y los desafíos** (Interés)
4. **Puesto:** responsabilidades, lugar de trabajo, horario
5. **Requisitos excluyentes y no excluyentes** (Deseo)
6. **Qué ofrece la empresa**
7. **Cómo postularse y hasta cuándo** (Acción)

### Perfil de puesto

- **Identificación:** nombre, área, objetivo del puesto, a quién reporta, personal a cargo.
- **Tareas:** verbo + "con la finalidad de".
- **Perfil:** estudios, experiencia, idiomas, conocimientos, **capacidades y habilidades**.

### Preguntas de entrevista

- **Hipotéticas:** *"¿Qué harías si…?"*. Según el apunte sirven para **indagar conocimientos**.
- **Provocadoras:** sirven para **ver la reacción**.
- La consigna pide "hipotéticas para ver cómo reacciona". Hacelas situacionales y con presión, por ejemplo: *"¿Qué harías si un día de cobro se caen las transferencias y el gerente te pide una solución en 10 minutos?"*

### Carga física y mental

- **Física:** posturas estáticas muchas horas frente a la pantalla, fatiga visual, dolores musculares.
- **Mental:** estrés por plazos y guardias, fatiga mental, monotonía, burn-out.

### Medidas preventivas

Para cada una, **decí en qué nivel está**. Priorizá las de diseño:

1. **En el diseño:** puesto ergonómico, iluminación sin reflejos, organizar guardias y cargas de trabajo.
2. **En el origen:** instalaciones eléctricas seguras, equipos adecuados.
3. **En el medio:** barreras acústicas, separar áreas ruidosas.
4. **Sobre la persona:** pausas activas, capacitación, exámenes médicos.

**No pongas solo medidas de nivel 4** (silla y pausas): es el error que marca la cátedra.

### Leyes

**19.587** Higiene y Seguridad · **24.557** Riesgos del Trabajo (ART) · **27.555** Teletrabajo.
