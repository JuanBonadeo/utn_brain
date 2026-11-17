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

> **Billetera Virtual.**
> - Meta: ser el banco de referencia de los jóvenes y los no bancarizados.
> - Objetivo de negocio: sumar 150.000 cuentas nuevas de no clientes antes de dic-2027.
> - Objetivo de TI: onboarding biométrico con RENAPER en producción antes de jun-2027, con 99,5% de disponibilidad.
>
> **Omnicanalidad.**
> - Meta: que el cliente opere igual en cualquier canal.
> - Objetivo de negocio: bajar un 30% los reclamos por operar entre la web y la app antes de fin de 2027.
> - Objetivo de TI: Home Banking y app sobre la misma capa de APIs, con el token unificado activo para el 100% de los clientes antes de sep-2027.
>
> **Copiloto con IA.**
> - Meta: sucursales que atienden rápido y sin errores normativos.
> - Objetivo de negocio: bajar un 25% el tiempo promedio de atención en las sucursales y un 40% las consultas internas a casa central antes de dic-2027.
> - Objetivo de TI: LLM privado con el 100% de las circulares BCRA vigentes cargadas, que responda en menos de 5 segundos, funcionando en las 45 sucursales antes de oct-2027.
>
> **Portal del Empleado.**
> - Meta: que los empleados resuelvan sus trámites solos y sin papel.
> - Objetivo de negocio: que el 90% de los empleados firme el recibo de forma digital y bajar un 50% los trámites en papel de Capital Humano antes de jun-2027.
> - Objetivo de TI: portal en producción reemplazando la intranet, con firma digital e ingreso único (SSO), con 99% de disponibilidad, antes de mar-2027.
>
> **Error típico:** "implementar el token unificado" como objetivo de negocio. Es de TI y no tiene métrica ni plazo. El de negocio es el de los reclamos.

## U2 — Riesgos

**Ejemplos de severidad** (uno por proyecto):

> **Billetera: suplantación de identidad en el onboarding.**
> - SEI: 2 → 2.3 Sistemas → integración (con RENAPER), relacionado con 1.2 fraude.
> - Activos: datos biométricos, app, reputación.
> - P = 4, porque es un canal masivo y nuevo, y el fraude digital es frecuente.
> - I = 5, porque hay pérdida de plata, sanción del BCRA y daño a la **Confianza**.
> - **Severidad 20 de 25: se atiende primero.**
> - Mitigar: prueba de vida más una alerta del SOC [02] por altas sospechosas. P baja a 2 y el residual queda en 10.
>
> **Omnicanalidad: una operación que arranca en la web y termina en la app se ejecuta dos veces.**
> - SEI: 2 → 2.3 Sistemas → integración (dos canales sobre la misma lógica).
> - Activos: plata y datos del cliente, core bancario.
> - P = 3, porque la lógica compartida es nueva y los recorridos cruzados son muchos, aunque se prueban antes de salir.
> - I = 4, porque afecta la plata del cliente y genera reclamos, pero se puede revertir conciliando.
> - **Severidad 12 de 25 (media).**
> - Mitigar: [03] le da un identificador único a cada operación para que no se procese dos veces y prueba de punta a punta los recorridos web → app; [04] concilia todos los días. P baja a 1 y el residual queda en 4.
>
> **Copiloto: el asistente responde mal un procedimiento normativo y el empleado lo aplica.**
> - SEI: 2 → 2.3 Sistemas → diseño (el modelo puede inventar respuestas).
> - Activos: información (base de conocimiento), personas, reputación.
> - P = 3, porque hay cientos de consultas por día y un LLM se equivoca cada tanto.
> - I = 4, porque puede terminar en una operación mal hecha o en una multa del BCRA (por ejemplo, en prevención de lavado).
> - **Severidad 12 de 25 (media).**
> - Mitigar: cada respuesta cita la circular de la que sale; antes del lanzamiento, Cumplimiento valida un set de preguntas de prueba; en los temas de lavado de dinero, el Copiloto pide confirmar con Cumplimiento. P baja a 2 y el residual queda en 8.
>
> **Portal: un empleado ve recibos o datos de otros por un error de permisos.**
> - SEI: 2 → 2.2 Software → parámetros de seguridad (configuración de roles).
> - Activos: datos personales y sueldos de los empleados.
> - P = 2, porque los perfiles se definen una vez y se prueban, aunque son muchos.
> - I = 4, porque son datos sensibles protegidos por ley, y genera conflicto interno.
> - **Severidad 8 de 25 (media-baja).**
> - Mitigar: [02] revisa los permisos por rol y hace un pentest antes del lanzamiento; el ingreso pide doble factor. P baja a 1 y el residual queda en 4.

**Ejemplos de plan de contingencia** (3 o 4 situaciones cada uno):

> **Billetera: se cae la validación con RENAPER.**
> - Disparador: más del 30% de las validaciones con error durante 10 minutos, o una alerta del SOC.
> - (1) [03] deja el alta "pendiente": la app guarda los datos y le avisa al cliente que la termina más tarde.
> - (2) [04] consulta el estado del servicio con RENAPER o el proveedor.
> - (3) [06] atiende las llamadas con el guion de la base de conocimiento.
> - (4) Si pasan 4 horas, el CIO decide habilitar el alta presencial en las sucursales.
> - Continuidad: las cuentas que ya existen siguen operando. Recuperación: se procesan las altas pendientes y se suma un segundo proveedor de validación.
>
> **Omnicanalidad: se cae el token unificado.**
> - Disparador: falla más del 20% de las validaciones durante 5 minutos.
> - (1) [04] activa el código por SMS para montos bajos.
> - (2) Si hay sospecha de ataque, [02] bloquea los montos altos.
> - (3) [06] atiende las llamadas con el guion de la base de conocimiento.
> - (4) Si pasan 2 horas, se escala al CIO.
> - Continuidad: las sucursales siguen operando. Recuperación: se suma redundancia al servicio del token.
>
> **Copiloto: se detectan respuestas erróneas sobre un tema normativo.**
> - Disparador: tres reportes de respuestas erróneas sobre el mismo tema en un día, o una caída del servicio.
> - (1) [03] bloquea ese tema: el Copiloto responde "consultar el manual" con el link a la circular.
> - (2) [06] avisa a las 45 sucursales por el canal interno.
> - (3) Cumplimiento revisa las operaciones que se hicieron con esa respuesta.
> - (4) Si el servicio se cae completo, las sucursales vuelven a los manuales y a la consulta a casa central.
> - Continuidad: la atención sigue con los manuales. Recuperación: se corrige la base de conocimiento y el caso se suma a las pruebas.
>
> **Portal: se cae el portal en la semana de cobro (firma de recibos).**
> - Disparador: el portal no responde por más de 15 minutos durante la liquidación.
> - (1) [01] y [03] restablecen el servicio.
> - (2) Capital Humano manda los recibos por mail en PDF.
> - (3) [06] atiende las consultas con un guion.
> - (4) Se extiende el plazo para firmar.
> - Continuidad: las licencias se piden por mail al jefe. Recuperación: se cargan a mano los trámites de esos días y se suma capacidad para las fechas pico.

## U2 — ITIL

**Cada práctica en los cuatro proyectos:**

| Práctica | Billetera | Omnicanalidad | Copiloto | Portal |
|---|---|---|---|---|
| **Incidentes** | No llega una transferencia | El token no valida en la app | El Copiloto no responde en una sucursal | Un empleado no puede ver su recibo |
| **Solicitud** | Blanqueo del PIN de la app | Alta de un celular nuevo para el token | Acceso al Copiloto para un empleado nuevo | Acceso al Portal para un ingresante |
| **Eventos** | CPU del servidor de QR > 90% | La API común tarda más de 2 s | El modelo tarda más de 10 s en responder | Muchos ingresos fallidos seguidos (posible ataque) |
| **Problemas** | 40 tickets con RENAPER: certificado vencido | Operaciones duplicadas: la app reintenta sin control | Respuestas mal sobre una circular: la base tiene la versión vieja | Recibos que no se firman en iPhone: componente de firma incompatible |
| **Cambios** | Aprueba renovar el certificado | Aprueba el control de duplicados | Aprueba recargar la circular nueva | Aprueba actualizar el componente |
| **Configuración** | Instala el certificado y actualiza la CMDB | Despliega el control y lo registra | Carga la base nueva y registra la versión del modelo | Instala el componente y actualiza la CMDB |
| **Versiones** | App v2.1 | Versión de la API común y de la app | Versión del modelo y de la base | Versión del portal |

**Escalado por proyecto:**

| Proyecto | Escalado funcional (de [06] a…) | Escalado jerárquico (al CIO o coordinador, para…) |
|---|---|---|
| **Billetera** | [03], por una falla de la API de pagos QR | autorizar un cambio de emergencia en la app |
| **Omnicanalidad** | [03] por la API común, o [02] si el token parece atacado | autorizar el SMS como alternativa al token |
| **Copiloto** | [03] por las respuestas, o [01] si se caen los servidores | sumar capacidad de servidores (costo nuevo) |
| **Portal** | [03], o al proveedor de la firma digital | extender el plazo de firma con Capital Humano |

- **Quién hace qué ante un incidente en Bancorp** (si piden "roles responsables", respondé con estas áreas y puestos):

| Rol / área | Responsabilidad ante el incidente |
|---|---|
| **Técnico de Mesa de Ayuda [06]** (1ª línea) | Recibe el aviso, abre el ticket, clasifica y prioriza, busca en la base de conocimiento, intenta resolverlo y, si no puede, lo deriva. Le avisa al usuario cómo sigue |
| **Coordinador de Soporte Interno [06]** | Controla los tiempos del SLA, decide escalar y avisa a las sucursales si el problema es masivo |
| **Especialista de 2ª línea** ([03] software, [01] infraestructura, [04] core) | Diagnostica y resuelve la causa técnica. Deja documentada la solución |
| **SOC [02]** | Monitorea eventos y detecta el problema antes de que llamen. Si hay sospecha de fraude, lo investiga |
| **Coordinador del área / CIO** (eje jerárquico) | Autoriza los recursos extra o un cambio de emergencia, y comunica a la Gerencia afectada |
| **Gestión de cambios y de configuración** | Aprueban e implementan la solución definitiva y actualizan la CMDB |

## U3 — Talento

**Ejemplos de puesto** (con competencias de los dos tipos):

> **Billetera: Desarrollador Mobile Sr.**
> - Área [03], célula Mobile. Reporta al Coordinador de Desarrollo y tiene 2 juniors a cargo.
> - Tarea: "integrar la biometría con RENAPER con la finalidad de abrir cuentas 100% digitales".
> - Específicas: desarrollo Android/iOS, integración con APIs de terceros. Genéricas: trabajo en equipo, liderazgo de los juniors.
>
> **Omnicanalidad: Especialista en integración (Middleware/ESB).**
> - Área [03], arquitectura e integración. Reporta al Coordinador de Desarrollo.
> - Tarea: "unificar la lógica de Home Banking y la app en una sola capa de APIs con la finalidad de que el cliente empiece una operación en un canal y la termine en otro".
> - Específicas: diseño de APIs, ESB, autenticación con token. Genéricas: comunicación con varias células, negociación.
>
> **Copiloto: Especialista en IA generativa.**
> - Área [03]. Reporta al Coordinador de Desarrollo.
> - Tarea: "mantener actualizada la base de conocimiento con las circulares del BCRA con la finalidad de que las sucursales reciban respuestas correctas y vigentes".
> - Específicas: modelos de lenguaje, seguridad de datos, evaluación de respuestas. Genéricas: aprendizaje continuo, comunicación con Cumplimiento.
>
> **Portal: Analista de procesos.**
> - Área [05], PMO y Procesos. Reporta al Líder de PMO.
> - Tarea: "relevar los trámites de Capital Humano con la finalidad de digitalizarlos en el Portal".
> - Específicas: modelado de procesos (BPMN), firma digital, usabilidad. Genéricas: escucha, comunicación con usuarios no técnicos.

**Ejemplos de retención con Maslow:**

> **Billetera: los desarrolladores mobile se van a fintechs.**
> - Seguridad: sueldo de mercado y un bono por el lanzamiento.
> - Pertenencia: una célula de producto con identidad propia.
> - Prestigio: que presenten la app en el lanzamiento.
> - Autorrealización: liderar la 2ª etapa (inversión en FCI).
>
> **Omnicanalidad: los técnicos de [04] se queman con las guardias 24×7 de la migración.**
> - Básicas: descanso garantizado con guardias rotativas.
> - Seguridad: guardias pagas aparte.
> - Pertenencia: reconocer al equipo cuando sale cada etapa.
> - Prestigio y autorrealización: certificación ITIL pagada por el banco y plan de carrera a coordinador.
>
> **Copiloto: los especialistas en IA se van a fintechs.**
> - Seguridad: sueldo de mercado.
> - Pertenencia: una célula con identidad propia.
> - Prestigio: presentar los resultados al Directorio.
> - Autorrealización: trabajar en el Core Inteligente a 5 años.
>
> **Portal: el propio portal como herramienta de retención de todo el banco.**
> - Seguridad: recibos y licencias claros y a tiempo.
> - Pertenencia: novedades y reconocimientos entre compañeros.
> - Prestigio: evaluaciones de desempeño visibles y con devolución.
> - Autorrealización: e-learning y plan de carrera.

## U4 — Higiene y seguridad

> **Billetera: célula Mobile [03] (desarrollo).**
> - Postura: sillas ergonómicas y pausas activas.
> - Fatiga visual: buenos monitores e iluminación.
> - Estrés por la fecha de lanzamiento: planificación desde la PMO.
> - Calor o mal aire: aire acondicionado. Riesgo eléctrico: cableado certificado.
>
> **Omnicanalidad: Operaciones TI [04] (monitoreo 24×7 y sala de servidores).**
> - Turnos nocturnos (fatiga, sueño): rotación de turnos y descanso entre guardias.
> - Muchas pantallas a la vez: monitores regulables e iluminación sin reflejos.
> - Sala de servidores (ruido, frío, riesgo eléctrico, incendio): protectores auditivos, cableado certificado y matafuegos aptos para equipos eléctricos.
> - Estrés por incidentes críticos: protocolo claro y una guardia de respaldo.
>
> **Copiloto: puestos de atención de las sucursales.**
> - Postura por horas sentado atendiendo: sillas y escritorios regulables, pausas.
> - Fatiga visual: pantalla a la altura de los ojos y buena luz.
> - Estrés por atención al público: capacitación y rotación entre caja y plataforma.
> - Ruido del salón: separación de los puestos.
>
> **Portal: Mesa de Ayuda [06] (recibe las consultas del lanzamiento).**
> - Uso continuo de la voz y auriculares: auriculares de calidad, pausas e hidratación.
> - Picos de llamadas en el lanzamiento: refuerzo de personal esas semanas.
> - Técnicos que van a las sucursales (pinpads, ticketeadoras): cuidado en los traslados y en la carga de equipos.
> - Postura y fatiga visual: sillas ergonómicas y monitores regulables.

## U5 — Proyectos ("no profundicen demasiado")

**Ejemplos de alcance:**

> **Billetera.**
> - Incluye: app Android/iOS, cuenta digital, biometría, QR y transferencias.
> - No incluye: la inversión en FCI (queda para una 2ª etapa), tarjeta física, préstamos.
> - Termina cuando la app está publicada y Banca Minorista la acepta.
>
> **Omnicanalidad.**
> - Incluye: la capa de APIs común para Home Banking y la app, las operaciones que se empiezan en un canal y se terminan en otro, el token unificado y la migración de los usuarios.
> - No incluye: la Billetera (es otra app), la atención por WhatsApp, el Open Banking (proyecto a 5 años).
> - Termina cuando todos los clientes operan con el token unificado y Banca Minorista lo acepta.
>
> **Copiloto.**
> - Incluye: el LLM privado en un entorno seguro, la carga de circulares BCRA, manuales de fraude, políticas de crédito y procedimientos de la Mesa de Ayuda, el acceso desde las 45 sucursales y la capacitación.
> - No incluye: atender a clientes (es interno), ejecutar operaciones (sólo responde), consultar datos de clientes del core.
> - Termina cuando funciona en las 45 sucursales y Cumplimiento valida las respuestas.
>
> **Portal del Empleado.**
> - Incluye: el portal que reemplaza la intranet, recibos con firma digital, licencias, evaluaciones de desempeño y e-learning de normativas.
> - No incluye: la liquidación de sueldos (sigue en el sistema actual, sólo se integra), el reclutamiento externo.
> - Termina cuando se da de baja la intranet y Capital Humano lo acepta.

**Ejemplos de adquisiciones:**

| Proyecto | Qué se adquiere | Forma |
|---|---|---|
| **Billetera** | Validación biométrica, procesador de pagos QR, nube, celulares de prueba, pentest | Por uso · contrato · cloud · compra · tercerizado |
| **Omnicanalidad** | Plataforma de APIs (API gateway), solución de token, servidores, pruebas de carga | Licencia o SaaS · SaaS · cloud o leasing · tercerizado |
| **Copiloto** | Modelo de lenguaje para uso privado, servidores con GPU, capacitación a las sucursales | Licencia · cloud o leasing · tercerizado |
| **Portal** | Plataforma de portal del empleado, certificados de firma digital, contenidos de e-learning | SaaS · por uso · compra o desarrollo propio |

## U6 — Canvas (la startup **le vende al banco desde afuera**)

> **Billetera: validación de identidad para el onboarding digital.**
> - Segmento: bancos medianos de capital nacional, con más de 30 sucursales, que lanzan una cuenta digital en los próximos 12 meses (unos 8 a 10, Bancorp incluido).
> - Propuesta: abrir cuentas en minutos sin que Ciberseguridad tenga que armar su propio antifraude, y cumplir con el BCRA sin sumar personal.
> - Socios clave: RENAPER y el proveedor de nube.
> - Ingresos: abono mensual más un monto por cada validación.
> - MVP: un mes con un solo banco piloto.
>
> **Omnicanalidad: autenticación única para todos los canales de un banco.**
> - Segmento: bancos medianos con Home Banking y app separados que planean unificarlos en los próximos 18 meses.
> - Propuesta: un solo método de autenticación en todos los canales, sin desarrollarlo adentro y cumpliendo el doble factor que pide el BCRA.
> - Socios clave: el proveedor de nube y las tiendas de apps.
> - Ingresos: licencia anual más un monto por usuario activo.
> - MVP: el token en un solo canal de un banco piloto durante 2 meses.
>
> **Copiloto: asistente normativo para el personal de sucursales.**
> - Segmento: bancos regionales y cooperativas con más de 20 sucursales y sin equipo propio de IA.
> - Propuesta: que el empleado tenga la respuesta normativa vigente en segundos, sin que Cumplimiento conteste cada consulta, y que se actualice sola cuando sale una circular nueva.
> - Socios clave: el proveedor del modelo de IA y un estudio que valide las respuestas normativas.
> - Ingresos: abono mensual por sucursal.
> - MVP: sólo circulares de prevención de lavado, en 3 sucursales de un banco piloto durante un mes.
>
> **Portal: autogestión de Capital Humano para bancos.**
> - Segmento: bancos y financieras de 500 a 3.000 empleados que todavía firman los recibos en papel.
> - Propuesta: que Capital Humano deje de imprimir y juntar firmas, y que el empleado haga sus trámites desde el celular.
> - Socios clave: la certificadora de firma digital y el sistema de liquidación de sueldos del banco.
> - Ingresos: abono mensual por empleado activo.
> - MVP: sólo recibos con firma digital, en un área de un banco piloto durante 2 meses.

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
