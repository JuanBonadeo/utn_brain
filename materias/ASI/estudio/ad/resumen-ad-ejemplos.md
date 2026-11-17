## Bancorp en una mirada

| Proyecto (1er año) | Qué es |
|---|---|
| **Billetera** | App para jóvenes y no bancarizados: cuenta 100% digital, biometría vía RENAPER, QR, transferencias |
| **Omnicanalidad** | Misma lógica en Home Banking y app, operación que arranca en la web y termina en el celular, **token unificado** |
| **Copiloto IA** | LLM privado entrenado con circulares BCRA y manuales, para el personal de sucursales |
| **Portal del Empleado** | Reemplaza la intranet: recibos con firma digital, licencias, evaluaciones, e-learning |

**Áreas de TI** (no inventar otras): [01] Infraestructura y Redes · [02] Ciberseguridad y Fraude (**SOC**) · [03] Ingeniería de Software · [04] Operaciones TI y Core · [05] PMO · [06] **Mesa de Ayuda**. Arriba, el **CIO**. **Valores:** Confianza y Solidez · Innovación · Inclusión · Cercanía · Integridad · Agilidad.

## U1 — Objetivos

| Proyecto | Meta | Objetivo de negocio | Objetivo de TI |
|---|---|---|---|
| **Billetera** | Ser el banco de los jóvenes y no bancarizados | 150.000 cuentas nuevas de no clientes antes de dic-2027 | Onboarding con RENAPER en producción antes de jun-2027, 99,5% de disponibilidad |
| **Omnicanalidad** | Operar igual en cualquier canal | −30% de reclamos por operar entre web y app antes de fin de 2027 | Web y app sobre la misma capa de APIs, token unificado para el 100% de los clientes antes de sep-2027 |
| **Copiloto** | Sucursales rápidas y sin errores normativos | −25% de tiempo de atención y −40% de consultas a casa central antes de dic-2027 | LLM con el 100% de las circulares vigentes, respuesta en menos de 5 s, en las 45 sucursales antes de oct-2027 |
| **Portal** | Trámites sin papel y autogestionados | 90% de recibos firmados digitalmente y −50% de trámites en papel antes de jun-2027 | Portal con firma digital y SSO reemplazando la intranet, 99% de disponibilidad, antes de mar-2027 |

**Error típico:** "implementar el token unificado" como objetivo de negocio. Es de TI y no tiene métrica ni plazo.

## U2 — Riesgos

| Proyecto | Riesgo y SEI | P × I = S (por qué) | Mitigación → residual |
|---|---|---|---|
| **Billetera** | Suplantación de identidad en el onboarding. 2.3 Sistemas → integración (con 1.2 fraude) | **4 × 5 = 20.** Canal masivo y nuevo, fraude frecuente · plata, BCRA, Confianza | Prueba de vida + alerta del SOC [02] por altas sospechosas → P 2, **residual 10** |
| **Omnicanalidad** | Una operación web → app se ejecuta dos veces. 2.3 Sistemas → integración | **3 × 4 = 12.** Lógica nueva, muchos recorridos cruzados · plata del cliente, pero se puede revertir | [03] ID único por operación y pruebas web → app; [04] concilia a diario → P 1, **residual 4** |
| **Copiloto** | Responde mal un procedimiento normativo y el empleado lo aplica. 2.3 Sistemas → diseño | **3 × 4 = 12.** Cientos de consultas, un LLM se equivoca · operación mal hecha, multa BCRA | Cita la circular fuente, Cumplimiento valida antes de lanzar, en lavado pide confirmar → P 2, **residual 8** |
| **Portal** | Un empleado ve recibos de otros por error de permisos. 2.2 Software → parámetros de seguridad | **2 × 4 = 8.** Perfiles definidos y probados, pero muchos · datos sensibles protegidos por ley | [02] revisa permisos por rol y hace pentest; doble factor → P 1, **residual 4** |

**Planes de contingencia:**

| Proyecto | Disparador | Acciones | Continuidad · recuperación |
|---|---|---|---|
| **Billetera:** cae la validación con RENAPER | >30% de errores durante 10 min o alerta del SOC | (1) [03] deja el alta pendiente y avisa al cliente (2) [04] consulta al proveedor (3) [06] atiende con guion (4) a las 4 h el CIO habilita el alta en sucursal | Las cuentas existentes siguen operando · procesar pendientes y sumar un 2º proveedor |
| **Omnicanalidad:** cae el token | >20% de validaciones fallidas durante 5 min | (1) [04] activa SMS para montos bajos (2) [02] bloquea montos altos si hay ataque (3) [06] atiende con guion (4) a las 2 h se escala al CIO | Las sucursales siguen operando · redundancia en el servicio del token |
| **Copiloto:** respuestas erróneas | 3 reportes del mismo tema en un día, o caída | (1) [03] bloquea el tema y deriva al manual (2) [06] avisa a las 45 sucursales (3) Cumplimiento revisa lo operado (4) si cae todo, se vuelve a los manuales | Se atiende con manuales · corregir la base y sumar el caso a las pruebas |
| **Portal:** cae en la semana de cobro | Sin respuesta por más de 15 min en la liquidación | (1) [01] y [03] lo restablecen (2) Capital Humano manda los recibos por mail (3) [06] atiende con guion (4) se extiende el plazo de firma | Licencias por mail al jefe · cargar a mano y sumar capacidad para los picos |

## U2 — ITIL

| Práctica | Billetera | Omnicanalidad | Copiloto | Portal |
|---|---|---|---|---|
| **Incidentes** | No llega una transferencia | El token no valida en la app | No responde en una sucursal | No puede ver su recibo |
| **Solicitud** | Blanqueo del PIN | Alta de un celular para el token | Acceso para un empleado nuevo | Acceso para un ingresante |
| **Eventos** | CPU del servidor de QR > 90% | La API común tarda > 2 s | El modelo tarda > 10 s | Muchos ingresos fallidos (posible ataque) |
| **Problemas** | 40 tickets con RENAPER: certificado vencido | Operaciones duplicadas: la app reintenta sin control | Respuestas mal: la base tiene la circular vieja | No se firma en iPhone: componente incompatible |
| **Cambios** | Aprueba renovar el certificado | Aprueba el control de duplicados | Aprueba recargar la circular | Aprueba actualizar el componente |
| **Configuración** | Instala y actualiza la CMDB | Despliega y registra | Carga la base y registra la versión | Instala y actualiza la CMDB |
| **Versiones** | App v2.1 | API común y app | Modelo y base | Portal |
| **Escalado funcional** | [03] por la API de pagos QR | [03] por la API, [02] si el token parece atacado | [03] por las respuestas, [01] si caen los servidores | [03] o el proveedor de firma digital |
| **Escalado jerárquico** | CIO: cambio de emergencia en la app | CIO: habilitar SMS en lugar del token | CIO: más servidores (costo nuevo) | Con Capital Humano: extender el plazo de firma |

**Quién hace qué ante un incidente** (si piden "roles responsables"):

| Rol / área | Responsabilidad |
|---|---|
| **Técnico de Mesa de Ayuda [06]** (1ª línea) | Recibe, abre el ticket, clasifica y prioriza, busca en la base de conocimiento, resuelve o deriva, y avisa al usuario |
| **Coordinador de Soporte Interno [06]** | Controla el SLA, decide escalar y avisa a las sucursales si es masivo |
| **Especialista de 2ª línea** ([03], [01], [04]) | Diagnostica y resuelve la causa técnica, y documenta la solución |
| **SOC [02]** | Detecta por monitoreo antes de que llamen; investiga si hay fraude |
| **Coordinador / CIO** (jerárquico) | Autoriza recursos extra o un cambio de emergencia, y comunica a la Gerencia afectada |
| **Cambios y configuración** | Aprueban e implementan la solución definitiva y actualizan la CMDB |

## U3 — Talento

| Proyecto | Puesto (área, reporta a) | Tarea ("con la finalidad de") | Competencias específicas · genéricas |
|---|---|---|---|
| **Billetera** | Desarrollador Mobile Sr. [03], al Coordinador de Desarrollo; 2 juniors a cargo | Integrar la biometría con RENAPER para abrir cuentas 100% digitales | Android/iOS, APIs de terceros · trabajo en equipo, liderazgo |
| **Omnicanalidad** | Especialista en integración (ESB) [03], al Coordinador de Desarrollo | Unificar la lógica de web y app en una capa de APIs para empezar en un canal y terminar en otro | Diseño de APIs, ESB, token · comunicación, negociación |
| **Copiloto** | Especialista en IA generativa [03], al Coordinador de Desarrollo | Mantener la base con las circulares BCRA para que las sucursales reciban respuestas vigentes | Modelos de lenguaje, seguridad de datos · aprendizaje continuo, comunicación con Cumplimiento |
| **Portal** | Analista de procesos [05], al Líder de PMO | Relevar los trámites de Capital Humano para digitalizarlos en el Portal | BPMN, firma digital, usabilidad · escucha, trato con no técnicos |

**Retención con Maslow:**

| Proyecto | Caso | Seguridad · pertenencia · prestigio · autorrealización |
|---|---|---|
| **Billetera** | Los devs mobile se van a fintechs | Sueldo de mercado y bono · célula de producto propia · presentan el lanzamiento · liderar la 2ª etapa (FCI) |
| **Omnicanalidad** | Técnicos de [04] quemados por las guardias 24×7 | Guardias rotativas y pagas aparte · reconocer al equipo en cada etapa · certificación ITIL · carrera a coordinador |
| **Copiloto** | Los especialistas en IA se van a fintechs | Sueldo de mercado · célula con identidad propia · resultados ante el Directorio · Core Inteligente a 5 años |
| **Portal** | El portal como herramienta de retención del banco | Recibos y licencias a tiempo · novedades y reconocimientos · evaluaciones con devolución · e-learning y plan de carrera |

## U4 — Higiene y seguridad

| Proyecto | Área | Riesgo → medida |
|---|---|---|
| **Billetera** | Célula Mobile [03] | Postura → sillas ergonómicas y pausas · fatiga visual → monitores y luz · estrés por el lanzamiento → planificación de la PMO · eléctrico → cableado certificado |
| **Omnicanalidad** | Operaciones TI [04], monitoreo 24×7 y sala de servidores | Turnos nocturnos → rotación y descanso · muchas pantallas → monitores regulables · ruido, frío, incendio → protectores auditivos y matafuegos para equipos eléctricos · estrés → protocolo y guardia de respaldo |
| **Copiloto** | Puestos de atención de sucursales | Postura → mobiliario regulable y pausas · fatiga visual → pantalla a la altura de los ojos · estrés por atención al público → capacitación y rotación · ruido → separar puestos |
| **Portal** | Mesa de Ayuda [06] en el lanzamiento | Voz y auriculares → buenos auriculares, pausas e hidratación · picos de llamadas → refuerzo de personal · traslados a sucursales → cuidado vial y en la carga de equipos |

## U5 — Proyectos

| Proyecto | Incluye | No incluye | Termina cuando |
|---|---|---|---|
| **Billetera** | App Android/iOS, cuenta digital, biometría, QR, transferencias | FCI (2ª etapa), tarjeta física, préstamos | La app está publicada y Banca Minorista la acepta |
| **Omnicanalidad** | Capa de APIs común, operaciones entre canales, token unificado, migración de usuarios | La Billetera, WhatsApp, Open Banking (a 5 años) | Todos operan con el token y Banca Minorista lo acepta |
| **Copiloto** | LLM privado, carga de circulares y manuales, acceso en 45 sucursales, capacitación | Atender clientes, ejecutar operaciones, datos de clientes del core | Funciona en las 45 sucursales y Cumplimiento valida las respuestas |
| **Portal** | Portal que reemplaza la intranet, recibos con firma, licencias, evaluaciones, e-learning | Liquidación de sueldos (sólo se integra), reclutamiento externo | Se da de baja la intranet y Capital Humano lo acepta |

**Adquisiciones:**

| Proyecto | Qué se adquiere | Forma |
|---|---|---|
| **Billetera** | Validación biométrica, procesador QR, nube, celulares de prueba, pentest | Por uso · contrato · cloud · compra · tercerizado |
| **Omnicanalidad** | API gateway, solución de token, servidores, pruebas de carga | Licencia o SaaS · SaaS · cloud o leasing · tercerizado |
| **Copiloto** | Modelo de lenguaje privado, servidores con GPU, capacitación | Licencia · cloud o leasing · tercerizado |
| **Portal** | Plataforma de portal, certificados de firma digital, e-learning | SaaS · por uso · compra o desarrollo propio |

## U6 — Canvas (startup que le vende al banco desde afuera)

| Proyecto | Segmento | Propuesta de valor | Socios · ingresos · MVP |
|---|---|---|---|
| **Billetera:** validación de identidad | Bancos medianos nacionales, +30 sucursales, que lanzan cuenta digital en 12 meses (8 a 10) | Abrir cuentas en minutos sin armar un antifraude propio, cumpliendo BCRA | RENAPER, nube · abono + monto por validación · 1 mes en un banco piloto |
| **Omnicanalidad:** autenticación única | Bancos medianos con web y app separados que los unifican en 18 meses | Un solo método de autenticación en todos los canales, sin desarrollarlo, con el doble factor del BCRA | Nube, tiendas de apps · licencia anual + por usuario activo · token en un canal de un banco, 2 meses |
| **Copiloto:** asistente normativo | Bancos regionales y cooperativas, +20 sucursales, sin equipo de IA | Respuesta normativa vigente en segundos, sin cargar a Cumplimiento, actualizada sola | Proveedor del modelo, estudio que valida · abono por sucursal · sólo lavado de dinero, 3 sucursales, 1 mes |
| **Portal:** autogestión de RRHH | Bancos y financieras de 500 a 3.000 empleados que firman recibos en papel | Que Capital Humano deje de imprimir y juntar firmas; trámites desde el celular | Certificadora de firma, sistema de sueldos · abono por empleado · sólo recibos, un área, 2 meses |
