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
- **Severidad = probabilidad × impacto**, cada uno de 1 a 5 (máximo 25). **Lo que más vale es la justificación** de cada número.
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
