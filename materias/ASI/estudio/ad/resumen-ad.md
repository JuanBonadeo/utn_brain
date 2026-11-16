# ASI — Resumen para la Aprobación Directa

> Sólo lo que el docente dijo que entra en la clase de repaso del 2026-11-11. Ejemplos sobre los proyectos del 1er año de Bancorp.

## El examen

- **Martes 17/11, de 17 a 19.** Está pensado para resolverse en **una hora**. Ese día se firma la asistencia.
- Son **unas 5 preguntas tipo parcial sobre BANCORP**. Puede haber algo de multiple choice.
- Respuestas **cortas y aplicadas**: no más de **una o dos hojas** en total.
- **No hay teoría pura.** La teoría se demuestra dentro de la justificación: el concepto tiene que estar explicado aunque no uses el nombre exacto.
- **No entra:** la planilla de riesgos completa, protocolos largos, calcular VAN/TIR, valor ganado ("no necesariamente") ni la clasificación de la organización ("no sé si la voy a tomar").

## Bancorp en una mirada

**Proyectos del 1er año** (de ahí salen los casos):

| Proyecto | Qué es |
|---|---|
| **Billetera Virtual** | App para jóvenes y no bancarizados: cuenta 100% digital, biometría vía RENAPER, QR, transferencias |
| **Omnicanalidad** | Misma lógica en Home Banking y app, operación que arranca en la web y termina en el celular, **token unificado** |
| **Copiloto con IA** | LLM privado entrenado con circulares BCRA y manuales, para el personal de sucursales |
| **Portal del Empleado (EX)** | Reemplaza la intranet: recibos con firma digital, licencias, evaluaciones, e-learning |

**Áreas de la Gerencia de TI** (para el escalado, **no inventar áreas**): [01] Infraestructura y Redes · [02] Ciberseguridad y Fraude (CISO, **SOC**) · [03] Ingeniería de Software (Home Banking, Mobile, APIs, bases de datos) · [04] Operaciones TI y Core Bancario · [05] PMO · [06] **Mesa de Ayuda**. Arriba de todas está el **CIO**.

**Valores** (sirven para justificar el impacto): Confianza y Solidez · Innovación Financiera · Inclusión y Accesibilidad · Cercanía · Integridad · Agilidad.

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

> **Ej. Billetera.** Meta: ser el banco de referencia de los jóvenes. Objetivo de negocio: sumar 150.000 cuentas nuevas de no clientes antes de dic-2027. Objetivo de TI: onboarding biométrico con RENAPER en producción antes de jun-2027, con 99,5% de disponibilidad.
>
> **Error típico:** "implementar el token unificado" como objetivo de negocio. Es de TI y no tiene métrica ni plazo. El de negocio sería: "bajar un 30% los reclamos por operar entre la web y la app antes de fin de 2027".

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

> **Ej. Billetera, suplantación de identidad en el onboarding.**
> - Activos: datos biométricos, app, reputación.
> - P = 4, porque es un canal masivo y nuevo, y el fraude digital es frecuente.
> - I = 5, porque hay pérdida de plata, sanción del BCRA y daño a la **Confianza**.
> - **Severidad 20 de 25: se atiende primero.**
> - Medida: prueba de vida más una alerta del SOC [02] por altas sospechosas. Con eso, P = 2 y el residual queda en 10.
>
> **Ej. contingencia por la caída del token de Omnicanalidad.**
> - Disparador: falla más del 20% de las validaciones durante 5 minutos.
> - (1) [04] activa el código por SMS para montos bajos.
> - (2) Si hay sospecha de ataque, [02] bloquea los montos altos.
> - (3) [06] atiende las llamadas con el guion de la base de conocimiento.
> - (4) Si pasan 2 horas, se escala al CIO.
> - Continuidad: las sucursales siguen operando. Recuperación: se suma redundancia al servicio del token.

## U2 — ITIL

- Las **prácticas no son roles**: la misma persona puede atender incidentes y después problemas.
- La **Mesa de Ayuda** es la 1ª línea y el **SPOC** (único punto de contacto). La 2ª línea es soporte técnico; después vienen terceros.

| Práctica | Qué hace | Bancorp |
|---|---|---|
| **Incidentes** | Alguien llama porque algo no funciona: ticket, clasificación, prioridad, resolución o derivación | Un cliente no recibe la transferencia de la billetera |
| **Solicitud de servicio** | Pedido que no cambia el sistema; lo resuelve la Mesa de Ayuda | Un empleado pide acceso al Portal |
| **Eventos** | Nadie llama: se monitorea, de forma pasiva (logs) o activa (alertas). Un evento de excepción dispara la contingencia | El SOC ve la CPU del servidor de QR por arriba del 90% |
| **Problemas** | Patrón de muchos incidentes. **Encuentra la solución, pero no la aplica** | 40 tickets iguales con RENAPER: la causa es un certificado vencido |
| **Cambios** | Evalúa, prioriza y aprueba o rechaza. **No implementa** | Se aprueba renovar el certificado |
| **Configuración** | **Implementa** y registra en la **CMDB** | Se instala el certificado y se actualiza la CMDB |
| **Versiones** | Versiona el software y también el hardware | v2.1 de la app de la billetera |

- **Escalado:**
  - **Funcional:** a quien sabe otra cosa. Por ejemplo, de [06] a [03] por una falla de una API.
  - **Jerárquico:** a quien puede **autorizar**. Por ejemplo, al CIO por licencias nuevas o un cambio de emergencia.
- **Quién hace qué ante un incidente en Bancorp** (si piden "roles responsables", respondé con estas áreas y puestos):

| Rol / área | Responsabilidad ante el incidente |
|---|---|
| **Técnico de Mesa de Ayuda [06]** (1ª línea) | Recibe el aviso, abre el ticket, clasifica y prioriza, busca en la base de conocimiento, intenta resolverlo y, si no puede, lo deriva. Le avisa al usuario cómo sigue |
| **Coordinador de Soporte Interno [06]** | Controla los tiempos del SLA, decide escalar y avisa a las sucursales si el problema es masivo |
| **Especialista de 2ª línea** ([03] software, [01] infraestructura, [04] core) | Diagnostica y resuelve la causa técnica. Deja documentada la solución |
| **SOC [02]** | Monitorea eventos y detecta el problema antes de que llamen. Si hay sospecha de fraude, lo investiga |
| **Coordinador del área / CIO** (eje jerárquico) | Autoriza los recursos extra o un cambio de emergencia, y comunica a la Gerencia afectada |
| **Gestión de cambios y de configuración** | Aprueban e implementan la solución definitiva y actualizan la CMDB |

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

> **Ej. puesto:** Desarrollador Mobile Sr.
> - Área [03], célula Mobile. Reporta al Coordinador de Desarrollo y tiene 2 juniors a cargo.
> - Tarea: "integrar la biometría con RENAPER con la finalidad de abrir cuentas 100% digitales".
>
> **Ej. retención:** los especialistas del Copiloto IA se van a fintechs.
> - Sueldo de mercado (seguridad).
> - Una célula con identidad propia (pertenencia).
> - Presentar los resultados al Directorio (prestigio).
> - Trabajar en el Core Inteligente a 5 años (autorrealización).

## U4 — Higiene y seguridad

- Se identifican las **condiciones del área** (no de un puesto suelto), sus **riesgos** y una **medida** para cada riesgo.

> **Ej. área de desarrollo [03]:**
> - Postura: sillas ergonómicas y pausas activas.
> - Fatiga visual: buenos monitores e iluminación.
> - Estrés por entregas y guardias: planificación desde la PMO y rotación de guardias.
> - Calor o mal aire: aire acondicionado.
> - Riesgo eléctrico: cableado certificado.

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

> **Ej. alcance de la Billetera.**
> - Incluye: app Android/iOS, cuenta digital, biometría, QR y transferencias.
> - No incluye: la inversión en FCI (queda para una 2ª etapa), tarjeta física, préstamos.
> - Termina cuando la app está publicada y Banca Minorista la acepta.

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

> **Ej. startup de validación de identidad para el onboarding digital.**
> - Segmento: bancos medianos de capital nacional, con más de 30 sucursales, que lanzan una cuenta digital en los próximos 12 meses (unos 8 a 10, Bancorp incluido).
> - Propuesta: abrir cuentas en minutos sin que Ciberseguridad tenga que armar su propio antifraude, y cumplir con el BCRA sin sumar personal.
> - Socios clave: RENAPER y el proveedor de nube.
> - Ingresos: abono mensual más un monto por cada validación.
> - MVP: un mes con un solo banco piloto.

<div style="page-break-before: always"></div>

## Simulacro — la AD 2025 aplicada a Bancorp

> Es el modelo de la AD del 25/02/2025 (contexto ElSuper, cajas de autoservicio), con las mismas 5 consignas pasadas a un proyecto de Bancorp. **Tiempo: 1 hora. Cada pregunta vale 2 puntos y se aprueba con 6.** Hacelo sin mirar la resolución, que está en la página siguiente.

**Contexto: BANCORP S.A. Proyecto: Generación de Billetera Virtual Propia.**

1. Defina un **objetivo de negocio** enfocado en mejorar la experiencia del cliente y un **objetivo de TI** relacionado con la implementación de la billetera, con **métricas** concretas para medir el éxito de cada uno.
2. Para el riesgo *"Fallas en la validación de identidad del onboarding que permiten abrir cuentas con datos de otra persona"*, establezca su **clasificación SEI**, calcule la **severidad con FAIR** y proponga una **estrategia de mitigación** específica.
3. A partir del **incidente** informado por el coordinador de la Mesa de Ayuda: *"Los pagos con QR de la billetera quedan en 'procesando' y no se acreditan, y los clientes llaman en cantidad"*, indique los **roles responsables** de su resolución y las **responsabilidades** clave de cada uno.
4. Defina el **rol** del puesto involucrado en el **escalado** del incidente y liste **tres competencias específicas** requeridas.
5. Para implementar la billetera, especifique las **adquisiciones** necesarias, sus **responsables** y los **criterios técnicos y funcionales** para seleccionar el equipamiento y el software.

<div style="page-break-before: always"></div>

### Resolución

**1. Objetivos**

- **De negocio:** que un cliente nuevo pueda abrir su cuenta desde el celular **en menos de 5 minutos y sin ir a una sucursal**, y que **el 80% de los usuarios califique la app con 4 estrellas o más** durante el primer año.
  - *Cómo se mide:* el tiempo promedio de alta (registrado por la app) y la calificación en las tiendas y en una encuesta dentro de la app.
- **De TI:** que la billetera esté **disponible el 99,5% del tiempo** y que **un pago con QR se acredite en menos de 3 segundos**, desde el lanzamiento previsto para junio de 2027.
  - *Cómo se mide:* el monitoreo del SOC y de Operaciones TI, con un reporte mensual.
- **Por qué está bien:** el de negocio lo entiende cualquiera (tiempo y satisfacción del cliente); el de TI es técnico. Los dos son SMART: tienen número, forma de medirse y plazo.

**2. Riesgo**

- **Clasificación SEI:** **2. Fallas de sistemas y tecnología → 2.3 Sistemas → 2.3.3 Integración**, porque la validación contra RENAPER puede fallar o ser engañada. Como alguien lo aprovecha a propósito, también se relaciona con **1.2.1 Fraude**.
- **Probabilidad (FAIR) = 4.** Hay **contacto intencional**: los estafadores buscan cuentas para mover plata. El **beneficio** es alto y el **esfuerzo** bajo, con fotos o DNI robados. La **capacidad de resistencia** es media, porque el canal es nuevo y todavía no tiene historial.
- **Impacto (FAIR) = 5.** La **pérdida primaria** es la plata robada y la investigación. La **secundaria**: reclamos de clientes, sanción del BCRA, noticias en los medios y daño a la **Confianza**, el primer valor del banco.
- **Severidad = 4 × 5 = 20 de 25 (alta).** Se atiende antes que otros riesgos.
- **Estrategia: mitigar.**
  - Ingeniería de Software [03] agrega **prueba de vida** (mover la cabeza frente a la cámara) además de la foto del DNI.
  - El SOC [02] configura una **alerta** cuando hay muchas altas desde el mismo celular o la misma IP.
  - Durante los primeros 30 días, las cuentas nuevas tienen **un límite de monto**.
  - Con eso, P baja a 2 y el **residual** queda en 2 × 5 = 10.

**3. Incidente: roles y responsabilidades**

| Rol | Qué hace |
|---|---|
| **Técnico de Mesa de Ayuda [06]** (1ª línea) | Atiende las llamadas, abre un ticket por cada una y las agrupa como un solo incidente masivo. Busca en la base de conocimiento, les dice a los clientes que su plata no se perdió y le avisa al coordinador |
| **Coordinador de Soporte [06]** | Le da **prioridad alta** (afecta a muchos clientes y a la plata), controla el SLA y escala |
| **Especialista de Ingeniería de Software [03]** (2ª línea, escalado funcional) | Revisa la API de pagos QR y la integración con el procesador de pagos. Encuentra y arregla la falla |
| **Operaciones TI [04]** | Controla que el core acredite bien y concilia los pagos que quedaron colgados |
| **SOC [02]** | Revisa en el monitoreo desde cuándo pasa y descarta un ataque |
| **CIO** (escalado jerárquico) | Si pasa más de una hora, autoriza un cambio de emergencia y avisa a la Gerencia de Banca Minorista |
| **Gestión de problemas** | Como hubo muchos incidentes iguales, busca la causa de fondo para que no se repita y la manda a **gestión de cambios**. **Configuración** la implementa y actualiza la CMDB |

Al cerrar, la solución queda escrita en la base de conocimiento. KPI: el tiempo medio de resolución.

**4. Puesto del escalado y competencias**

- **Rol:** **Especialista en integración y APIs** del área de Ingeniería de Software y Canales Digitales [03], que es la 2ª línea del escalado funcional.
  - Reporta al Coordinador de Desarrollo.
  - El objetivo del puesto es mantener funcionando la conexión de la billetera con los sistemas del banco y con los servicios externos (pagos QR, RENAPER).
  - Ante este incidente, diagnostica la causa, la corrige y documenta la solución.
- **Tres competencias específicas** (del puesto, no de la persona):
  1. Diagnóstico de fallas en APIs y servicios de pago: leer logs y seguir una transacción de punta a punta.
  2. Integración con el core bancario y el middleware (ESB).
  3. Seguridad en transacciones financieras: cifrado y normativa del BCRA.

**5. Adquisiciones**

| Qué se adquiere | Forma | Responsable |
|---|---|---|
| Servicio de validación biométrica (conexión con RENAPER) | Servicio por uso, contratado vía RFP | [03] define los requerimientos; [02] valida la seguridad |
| Servidores en la nube para la app y los pagos | Pago por uso (cloud) | Infraestructura [01] |
| Procesador de pagos QR interoperable | Contrato con un proveedor | [03] con Administración y Finanzas |
| Celulares de prueba (Android y iOS) | Compra | [03] |
| Pruebas de seguridad (pentest) | Servicio tercerizado | Ciberseguridad [02] |

- **Coordinación:** el PM de la PMO [05] coordina todo, **Administración y Finanzas** hace la compra y controla el presupuesto, y el **CIO** aprueba. Primero se hace un **RFI** para ver qué proveedores hay y después un **RFP** a por lo menos 3.
- **Criterios técnicos:** que se integre con el core y las APIs del banco, la seguridad (cifrado, normativa BCRA), que aguante muchos usuarios a la vez y la disponibilidad que garantiza el SLA (99,5% o más).
- **Criterios funcionales:** que el alta sea simple para el cliente, que el QR sea interoperable con cualquier comercio y que los reportes sirvan a Banca Minorista.
- **Del proveedor:** experiencia con otros bancos, soporte 24×7, plazo de implementación, capacitación y el **TCO** (todo lo que cuesta durante los años de uso, no sólo el precio inicial).
