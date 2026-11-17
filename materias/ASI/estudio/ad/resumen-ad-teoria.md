## U1 — Estrategia y objetivos

- **Gobierno de TI:** TI es parte inseparable de la dirección, no un área de soporte. Tiene que estar alineada con los objetivos y los valores de la empresa (ISO 38500; COBIT es un framework, no una norma).
- **Misión, visión y valores.** La misión dice para qué existe la empresa, la visión cómo se ve en un tiempo dado, y los valores con qué principios trabaja.
- **Meta vs. objetivo** ★ ("en el parcial lo llevamos siempre"):
  - La **meta** es el horizonte y apunta a la visión.
  - Los **objetivos** son pequeñas metas **medibles y con plazo**. Se controlan al final y también **durante** el avance; si hay desvío, se ajusta o se cancela.
- **SMART:** específico, medible, alcanzable, realista, en tiempo. Primero se piensa el objetivo desde el negocio y después se afina con SMART.
- **Objetivo de negocio vs. de TI** ★:
  - El de **negocio** lo entiende alguien que no sabe de tecnología: plata, tiempo, costos, clientes.
  - El de **TI** es el técnico: sistemas, disponibilidad, infraestructura.
- **Qué hace que se cumplan:** que los involucrados participen en definirlos, la política organizacional y sobre todo la **cultura**: "la cultura se come la estrategia".

## U2 — Riesgos

- **Riesgo:** algo no esperado y negativo que puede pasar. El riesgo positivo es una oportunidad y no se trata.
- **Activos que pueden estar involucrados:** información, software, hardware, instalaciones, servicios y personas.
- **Clasificación SEI** (de dónde viene el riesgo). Se escribe clase → subclase → subcategoría:

| Clase | Subclases y algunas subcategorías |
|---|---|
| **1. Acciones de las personas** | 1.1 Involuntarias (equivocación, error, omisión) · 1.2 Deliberadas (**fraude**, sabotaje, **robo**, vandalismo) · 1.3 Inacción (habilidad, conocimiento, guía, disponibilidad) |
| **2. Fallas de sistemas y tecnología** | 2.1 Hardware (capacidad, rendimiento, mantenimiento, obsolescencia) · 2.2 Software (configuración, control de cambios, parámetros de seguridad, **testing**) · 2.3 Sistemas (diseño, especificaciones, **integración**, complejidad) |
| **3. Fallas de procesos internos** | 3.1 Diseño y ejecución (flujo, documentación, roles, alertas, escalado, SLA) · 3.2 Control de procesos (monitorización) · 3.3 Procesos de soporte (dotación de personal, proveedores) |
| **4. Eventos externos** | 4.1 Desastres · 4.2 Cuestiones legales (regulaciones) · 4.3 Cuestiones del negocio (fallas del suministro) · 4.4 Dependencias con servicios (servicios públicos) |

  La clase tiene que ser **coherente con la causa**: si la causa es un error del software, va en 2; si es alguien que lo aprovecha a propósito, va en 1.2.

- **FAIR** sirve para **justificar** la probabilidad y el impacto, no para clasificar:
  - **Probabilidad = frecuencia de eventos de pérdida.** Depende de qué tan seguido la amenaza entra en **contacto** con el activo (aleatorio, periódico o intencional), de si conviene **actuar** (beneficio, esfuerzo, riesgo de que lo detecten) y de la **vulnerabilidad**: la capacidad de la amenaza contra la **capacidad de resistencia** (los controles).
  - **Impacto = magnitud de la pérdida.** La pérdida **primaria** es la directa sobre el activo (productividad, costo de reemplazo, sensibilidad: reputación, legal). La **secundaria** viene de la reacción de otros (clientes, BCRA, medios).
- **Severidad = probabilidad × impacto**, cada uno de 1 a 5 (máximo 25). **Lo que más vale es la justificación** de cada número.
- **Estrategias de tratamiento:** evitar, transferir (por ejemplo, un seguro), **mitigar** o aceptar. Una **mitigación específica** dice qué control se aplica, quién lo aplica y qué baja (la P o el I).
- **Inherente vs. residual:**
  - El **inherente** es el riesgo con lo que hay hoy, antes de las medidas nuevas.
  - El **residual** es el que queda después de aplicarlas. Nunca llega a cero.
- **Priorizar:** se ordena de mayor a menor severidad. Por Pareto, el 80% de la severidad está en el primer 20% de los riesgos. Se revisa periódicamente.
- **Tipos de control:**
  - **Preventivo:** se aplica antes, para reducir el riesgo.
  - **Detectivo:** detecta que pasó y dispara el **plan de contingencia**.
  - **Correctivo:** identifica qué pasó y lo arregla.
- **Planes, en este orden:**
  1. **Contingencia:** actuar al detectarlo y limitar el daño.
  2. **Continuidad:** que la empresa siga funcionando mientras tanto, aunque sea a mano.
  3. **Recuperación:** volver a funcionar, y **mejor que antes**, no igual.

  Todos se planifican antes de que pase.
- **Lo que pueden pedir:** un plan de contingencia de **3 o 4 situaciones**, una medida de mitigación, o clasificar un riesgo y calcular su severidad.

## U2 — ITIL

- Las **prácticas no son roles**: la misma persona puede atender incidentes y después problemas.
- La **Mesa de Ayuda** es la 1ª línea y el **SPOC** (único punto de contacto). La 2ª línea es soporte técnico; después vienen terceros.

| Práctica | Qué hace |
|---|---|
| **Incidentes** | Alguien llama porque algo no funciona: ticket, clasificación, prioridad, resolución o derivación |
| **Solicitud de servicio** | Pedido que no cambia el sistema; lo resuelve la Mesa de Ayuda |
| **Eventos** | Nadie llama: se monitorea, de forma pasiva (logs) o activa (alertas). Un evento de excepción dispara la contingencia |
| **Problemas** | Patrón de muchos incidentes. **Encuentra la solución, pero no la aplica** |
| **Cambios** | Evalúa, prioriza y aprueba o rechaza. **No implementa** |
| **Configuración** | **Implementa** y registra en la **CMDB** |
| **Versiones** | Versiona el software y también el hardware |

- **Escalado:**
  - **Funcional:** a quien sabe otra cosa. Por ejemplo, de [06] a [03] por una falla de una API.
  - **Jerárquico:** a quien puede **autorizar**. Por ejemplo, al CIO por licencias nuevas o un cambio de emergencia.

**Quién hace qué ante un incidente** (si piden "roles responsables"):

| Rol / área | Responsabilidad |
|---|---|
| **Técnico de Mesa de Ayuda [06]** (1ª línea) | Recibe, abre el ticket, clasifica y prioriza, busca en la base de conocimiento, resuelve o deriva, y avisa al usuario |
| **Coordinador de Soporte Interno [06]** | Controla el SLA, decide escalar y avisa a las sucursales si es masivo |
| **Especialista de 2ª línea** ([03], [01], [04]) | Diagnostica y resuelve la causa técnica, y documenta la solución |
| **SOC [02]** | Detecta por monitoreo antes de que llamen; investiga si hay fraude |
| **Coordinador / CIO** (jerárquico) | Autoriza recursos extra o un cambio de emergencia, y comunica a la Gerencia afectada |
| **Cambios y configuración** | Aprueban e implementan la solución definitiva y actualizan la CMDB |

- **Siempre hay que nombrar:** el **sistema de tickets**, la **base de conocimiento** (cómo se resolvió algo), la **CMDB** (la ficha de cada ítem) y el **SLA** (para validar si el usuario tiene derecho a lo que pide). Sumá algún **KPI**, como el tiempo medio de resolución.

## U3 — Talento

- **Procesos:** organizar y diseñar los puestos → reclutamiento → **retención** → desarrollo → evaluación.
- **Definir un puesto** ★:
  - **Identificación:** nombre, área, objetivo del puesto, a quién reporta y personal a cargo.
  - **Tareas:** se escriben como acción + "con la finalidad de".
  - **Perfil:** estudios, experiencia, idiomas, conocimientos y capacidades.
  - El puesto es qué se hace; el perfil es qué tiene que tener la persona para hacerlo.
- **Competencias** ★:
  - **Genéricas** son de la persona: comunicación, trabajo en equipo, liderazgo, resolución de problemas.
  - **Específicas** son del puesto: seguridad por diseño, costos cloud, arquitectura.
- **Tipos de evaluación:** técnicas, psicológicas, **por competencias** (con factores y escala) y assessment. La **360°** suma la opinión del jefe, los pares y los usuarios.
- **Retención con Maslow** ★ ("el centro de todo esto"): básicas → seguridad (cobrar todos los meses) → pertenencia ("ponerse la camiseta") → prestigio → autorrealización.
- **Reclutamiento:**
  - **Interno:** es más barato, ya conocés a la persona y se siente que hay crecimiento. En contra: celos, y deja un sector sin gente.
  - **Externo:** trae gente nueva, con riesgo de equivocarse.
  - Se hace con un equipo propio o con una **consultora**, que está especializada y ahorra tiempo.
  - El aviso se redacta con **AIDA**: atención, interés, deseo, acción.

## U4 — Higiene y seguridad

- Se identifican las **condiciones del área** (no de un puesto suelto), sus **riesgos** y una **medida** para cada riesgo.

## U5 — Proyectos ("no profundicen demasiado")

- Un **proyecto** tiene inicio y fin, un presupuesto de plata y de tiempo, y objetivos propios. Operar el producto después ya no es el proyecto.
- **Qué considerar para defenderlo ante la Dirección:**
  - el beneficio (más ingresos o menos costos);
  - el **alcance**, el tiempo y el costo;
  - la comparación contra otros proyectos.
- **Qué controlar y con qué:** el avance contra el plan, el costo contra el presupuesto, el alcance (que no se sume nada sin aprobar) y la calidad. Las herramientas son el Gantt, la red, el valor ganado y el acta.
- **Especificación del alcance:** qué incluye, **qué no incluye** y cuándo termina el proyecto (quién lo acepta).
- **Indicadores** (saber identificarlos y compararlos, no calcularlos):
  - **VAN:** la plata que deja el proyecto a valor de hoy. Conviene si es **mayor a 0**; entre dos, se prefiere el de mayor VAN.
  - **TIR:** la rentabilidad propia del proyecto. Conviene si es **mayor que la tasa de corte**.
  - **ROI:** la ganancia por cada peso invertido. **No considera el valor del dinero en el tiempo.**

- **Adquisiciones** (salió en la AD 2025):
  - **Qué se adquiere:** surge de la solución elegida. Se arma una tabla con el activo o servicio, la cantidad, las características mínimas, la forma de adquisición y por qué.
  - **Formas de adquisición:** comprar, alquilar, **leasing** (alquiler con opción de compra), SaaS o pago por uso, o tercerizar (outsourcing).
  - **RFI → RFP:** el **RFI** pide **información** para conocer qué hay en el mercado, y va primero. El **RFP** pide la **propuesta** formal con precio, plazo, equipo y SLA, y se hace cuando los requerimientos ya están claros. Se piden al menos 3 cotizaciones.
  - **Responsables:** el **PM** del proyecto (PMO [05]) coordina. El **área técnica** define los requerimientos. **Administración y Finanzas** ve el presupuesto y la compra. **Ciberseguridad [02]** valida la seguridad. El **CIO** aprueba.
  - **Criterios técnicos:** que cubra los requerimientos, la **integración** con los sistemas actuales (core, APIs), la seguridad, la escalabilidad y el rendimiento.
  - **Criterios funcionales:** que sea fácil de usar para el cliente o el empleado y que haga lo que el negocio necesita.
  - **Del proveedor:** experiencia en bancos y referencias, soporte y SLA, plazo de implementación, capacitación, y el **TCO**: el costo total durante toda la vida útil, no sólo el precio.

## U6 — Canvas (la startup **le vende al banco desde afuera**)

- **Canvas ≠ plan de negocios:** el Canvas es el modelo de negocio en una hoja.
- **Segmentos** ★: tienen que estar **acotados a lo que podés atender**. "Bancos" es el mercado, no un segmento.
- **Propuesta de valor** ★: es **lo que le resuelve a ese segmento**, no la función del producto. Va asociada a cada segmento.
- **Relación con los clientes:** **get, keep y grow son estrategias.** Poner sólo "redes sociales" está mal.
  - **Get:** conseguir clientes nuevos (CAC = gasto ÷ clientes nuevos).
  - **Keep:** retenerlos.
  - **Grow:** venderles más.
- **Canales:** cómo llegás al cliente. **Acá sí** van las redes sociales o el App Store.
- **Actividades y recursos clave:** son **todo** lo que hace funcionar la empresa: vender, cobrar, marketing, soporte, oficina. Poner sólo "desarrollo" está mal.
- **Socios clave:** de quién **depende** tu modelo, aunque no lo sepa.
- **Costos:** fijos y variables, incluidos los gastos propios del emprendedor.
- **Fuente de ingresos ≠ inversión:** la fuente es cómo cobrás; la inversión financia los recursos clave.
- **MVP:** el producto más completo posible en poco tiempo, que **el cliente usa de verdad** (no es un prototipo). Se mide y se pivotea hasta llegar al product-market fit.
- **Desarrollo de clientes:** validar el problema hablando con clientes reales antes de construir todo.
