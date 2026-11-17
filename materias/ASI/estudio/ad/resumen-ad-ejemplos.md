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
| **Billetera** | Que los jóvenes manejen su plata con el banco desde su primera cuenta | Que el 30% de los usuarios active la inversión automática de saldos en el FCI en el primer año | Inversión automática integrada con el FCI propio, con el 100% de las suscripciones del día procesadas antes de las 18 h, antes de dic-2027 |
| **Omnicanalidad** | Operar igual en cualquier canal | Pasar a web y app el 40% de los plazos fijos y pagos que hoy se hacen en sucursal, antes de dic-2027 | Web y app sobre la misma capa de APIs, token unificado para el 100% de los clientes antes de sep-2027 |
| **Copiloto** | Sucursales rápidas y sin errores normativos | −25% de tiempo de atención y −40% de consultas a casa central antes de dic-2027 | LLM con el 100% de las circulares vigentes, respuesta en menos de 5 s, en las 45 sucursales antes de oct-2027 |
| **Portal** | Trámites sin papel y autogestionados | 90% de recibos firmados digitalmente y −50% de trámites en papel antes de jun-2027 | Portal con firma digital y SSO reemplazando la intranet, 99% de disponibilidad, antes de mar-2027 |

**Error típico:** "que el Copiloto mejore la atención en las sucursales". No es SMART: no dice cuánto ni para cuándo. Bien planteado es el −25% de tiempo de atención de la tabla.

## U2 — Riesgos

| Proyecto | Riesgo y SEI | P × I = S (por qué) | Mitigación → residual |
|---|---|---|---|
| **Billetera** | Robo de cuentas por phishing o duplicación de la línea del celular. 1.2 Deliberadas → robo | **4 × 4 = 16.** Los jóvenes son blanco frecuente por redes y la app es nueva · plata del cliente, reclamos, Confianza | [02] alerta por cambio de celular y bloqueo de transferencias por 24 h después del cambio; avisos de seguridad en la app → P 2, **residual 8** |
| **Omnicanalidad** | Una operación web → app se ejecuta dos veces. 2.3 Sistemas → integración | **3 × 4 = 12.** Lógica nueva, muchos recorridos cruzados · plata del cliente, pero se puede revertir | [03] ID único por operación y pruebas web → app; [04] concilia a diario → P 1, **residual 4** |
| **Copiloto** | Responde mal un procedimiento normativo y el empleado lo aplica. 2.3 Sistemas → diseño | **3 × 4 = 12.** Cientos de consultas, un LLM se equivoca · operación mal hecha, multa BCRA | Cita la circular fuente, Cumplimiento valida antes de lanzar, en lavado pide confirmar → P 2, **residual 8** |
| **Portal** | Un empleado ve recibos de otros por error de permisos. 2.2 Software → parámetros de seguridad | **2 × 4 = 8.** Perfiles definidos y probados, pero muchos · datos sensibles protegidos por ley | [02] revisa permisos por rol y hace pentest; doble factor → P 1, **residual 4** |

**Planes de contingencia:**

| Proyecto | Disparador | Acciones | Continuidad · recuperación |
|---|---|---|---|
| **Billetera:** no se acreditan los rescates del FCI | Rescates sin acreditar a las 10 h, o diferencias en la conciliación con el FCI | (1) [04] suspende la inversión automática del día y el saldo queda líquido (2) [03] muestra un aviso en la app (3) [06] atiende con guion (4) si pasa un día hábil, el CIO y Banca Minorista acreditan a mano | La billetera sigue operando con el saldo líquido · reprocesar los rescates y automatizar la conciliación |
| **Omnicanalidad:** se cae la API común (caen web y app a la vez) | >5% de errores durante 5 min en el monitoreo de [04] | (1) [04] pasa al servidor de respaldo (2) [03] deja los canales sólo en consulta: se ven saldos, no se transfiere (3) [06] avisa en web y app y atiende con guion (4) a las 2 h se escala al CIO | Cajeros y sucursales atienden lo urgente · análisis de causa y respaldo siempre activo |
| **Copiloto:** respuestas erróneas | 3 reportes del mismo tema en un día, o caída | (1) [03] bloquea el tema y deriva al manual (2) [06] avisa a las 45 sucursales (3) Cumplimiento revisa lo operado (4) si cae todo, se vuelve a los manuales | Se atiende con manuales · corregir la base y sumar el caso a las pruebas |
| **Portal:** cae en la semana de cobro | Sin respuesta por más de 15 min en la liquidación | (1) [01] y [03] lo restablecen (2) Capital Humano manda los recibos por mail (3) [06] atiende con guion (4) se extiende el plazo de firma | Licencias por mail al jefe · cargar a mano y sumar capacidad para los picos |

## U2 — ITIL

| Práctica | Billetera | Omnicanalidad | Copiloto | Portal |
|---|---|---|---|---|
| **Incidentes** | Una recarga de celular se cobró y no se acreditó | El token no valida en la app | No responde en una sucursal | No puede ver su recibo |
| **Solicitud** | Blanqueo del PIN | Alta de un celular para el token | Acceso para un empleado nuevo | Recuperar la contraseña del portal |
| **Eventos** | Las suscripciones al FCI del día no terminaron a las 18 h | La API común tarda > 2 s | El modelo tarda > 10 s | Muchos ingresos fallidos (posible ataque) |
| **Problemas** | Muchas recargas sin acreditar: el proveedor corta por tiempo de espera | Operaciones duplicadas: la app reintenta sin control | Respuestas mal: la base tiene la circular vieja | No se firma en iPhone: componente incompatible |
| **Cambios** | Aprueba ampliar el tiempo de espera y sumar reintentos | Aprueba el control de duplicados | Aprueba recargar la circular | Aprueba actualizar el componente |
| **Configuración** | Aplica el parámetro y lo registra en la CMDB | Despliega y registra | Carga la base y registra la versión | Instala y actualiza la CMDB |
| **Versiones** | App 3.0 con inversión en FCI | API común y app | Modelo y base | Portal |
| **Escalado funcional** | [03] por la integración con el proveedor de recargas | [03] por la API, [02] si el token parece atacado | [03] por las respuestas, [01] si caen los servidores | [03] o el proveedor de firma digital |
| **Escalado jerárquico** | CIO: contratar un 2º proveedor de recargas | CIO: frenar la migración de usuarios hasta resolverlo | CIO: más servidores (costo nuevo) | Con Capital Humano: extender el plazo de firma |

## U3 — Talento

| Proyecto | Puesto (área, reporta a) | Tarea ("con la finalidad de") | Competencias específicas · genéricas |
|---|---|---|---|
| **Billetera** | Scrum Master de la célula Billetera [05], al Líder de PMO | Coordinar los sprints de la célula para lanzar la inversión en FCI en la fecha comprometida | Scrum, gestión del backlog, métricas ágiles · facilitación, resolución de conflictos |
| **Omnicanalidad** | Diseñador UX de canales [03], al Coordinador de Desarrollo | Unificar la experiencia de web y app para que el cliente encuentre cada operación en el mismo lugar en los dos canales | Diseño UX/UI, pruebas de usabilidad, accesibilidad · empatía, comunicación |
| **Copiloto** | Especialista en IA generativa [03], al Coordinador de Desarrollo | Mantener la base con las circulares BCRA para que las sucursales reciban respuestas vigentes | Modelos de lenguaje, seguridad de datos · aprendizaje continuo, comunicación con Cumplimiento |
| **Portal** | Analista de procesos [05], al Líder de PMO | Relevar los trámites de Capital Humano para digitalizarlos en el Portal | BPMN, firma digital, usabilidad · escucha, trato con no técnicos |

**Retención con Maslow:**

| Proyecto | Caso | Seguridad · pertenencia · prestigio · autorrealización |
|---|---|---|
| **Billetera** | Perfiles jóvenes en su primer empleo rotan mucho | Contrato efectivo y obra social · mentoría con un senior · mostrar su trabajo en las demos · plan de formación y carrera a semi senior |
| **Omnicanalidad** | Técnicos de [04] quemados por las guardias 24×7 | Guardias rotativas y pagas aparte · reconocer al equipo en cada etapa · certificación ITIL · carrera a coordinador |
| **Copiloto** | Empleados de sucursal con antigüedad sienten que el Copiloto los reemplaza | Aclarar que no hay despidos, es una herramienta · referentes de sucursal que lo prueban primero · reconocer a quienes reportan correcciones · más tiempo para asesorar clientes |
| **Portal** | El portal como herramienta de retención del banco | Recibos y licencias a tiempo · novedades y reconocimientos · evaluaciones con devolución · e-learning y plan de carrera |

## U4 — Higiene y seguridad

| Proyecto | Área | Riesgo → medida |
|---|---|---|
| **Billetera** | Célula Billetera en home office | Puesto en casa sin ergonomía → silla y monitor provistos por el banco · jornada sin límite → derecho a la desconexión (ley de teletrabajo) · aislamiento → un día presencial por semana · instalación eléctrica de la casa → verificarla |
| **Omnicanalidad** | Operaciones TI [04], monitoreo 24×7 y sala de servidores | Turnos nocturnos → rotación y descanso · muchas pantallas → monitores regulables · ruido, frío, incendio → protectores auditivos y matafuegos para equipos eléctricos · estrés → protocolo y guardia de respaldo |
| **Copiloto** | Puestos de atención de sucursales | Postura → mobiliario regulable y pausas · fatiga visual → pantalla a la altura de los ojos · estrés por atención al público → capacitación y rotación · ruido → separar puestos |
| **Portal** | Mesa de Ayuda [06] en el lanzamiento | Voz y auriculares → buenos auriculares, pausas e hidratación · picos de llamadas → refuerzo de personal · traslados a sucursales → cuidado vial y en la carga de equipos |

## U5 — Proyectos

| Proyecto | Incluye | No incluye | Termina cuando |
|---|---|---|---|
| **Billetera** (2ª etapa) | Inversión automática de saldos en el FCI propio, rescate inmediato, recargas de celular y transporte | FCI de terceros, préstamos, tarjeta | 100 usuarios piloto invierten y rescatan sin errores durante un mes y Banca Minorista lo acepta |
| **Omnicanalidad** | Capa de APIs común, operaciones entre canales, token unificado, migración de usuarios | La Billetera, WhatsApp, Open Banking (a 5 años) | Todos operan con el token y Banca Minorista lo acepta |
| **Copiloto** | LLM privado, carga de circulares y manuales, acceso en 45 sucursales, capacitación | Atender clientes, ejecutar operaciones, datos de clientes del core | Funciona en las 45 sucursales y Cumplimiento valida las respuestas |
| **Portal** | Portal que reemplaza la intranet, recibos con firma, licencias, evaluaciones, e-learning | Liquidación de sueldos (sólo se integra), reclutamiento externo | Se da de baja la intranet y Capital Humano lo acepta |

**Adquisiciones:**

| Proyecto | Qué se adquiere | Forma |
|---|---|---|
| **Billetera** | Proveedor de recargas, monitoreo de fallas de la app, pruebas de usabilidad con jóvenes, asesoría normativa para el FCI | Comisión por recarga · SaaS · tercerizado · tercerizado |
| **Omnicanalidad** | API gateway, solución de token, servidores, pruebas de carga | Licencia o SaaS · SaaS · cloud o leasing · tercerizado |
| **Copiloto** | Modelo de lenguaje privado, servidores con GPU, capacitación | Licencia · cloud o leasing · tercerizado |
| **Portal** | Plataforma de portal, certificados de firma digital, e-learning | SaaS · por uso · compra o desarrollo propio |

## U6 — Canvas (startup que le vende al banco desde afuera)

| Proyecto | Segmento | Propuesta de valor | Socios · ingresos · MVP |
|---|---|---|---|
| **Billetera:** educación financiera con desafíos dentro de la billetera | Bancos con billetera para jóvenes de 16 a 25 años lanzada hace menos de 2 años (5 a 8) | Que los usuarios jóvenes pasen de sólo gastar a ahorrar e invertir, sin que el banco arme los contenidos | Creadores de contenido financiero · abono por usuario activo del módulo · 3 desafíos en un banco piloto, 1 mes |
| **Omnicanalidad:** autenticación única | Bancos medianos con web y app separados que los unifican en 18 meses | Un solo método de autenticación en todos los canales, sin desarrollarlo, con el doble factor del BCRA | Nube, tiendas de apps · licencia anual + por usuario activo · token en un canal de un banco, 2 meses |
| **Copiloto:** asistente normativo | Bancos regionales y cooperativas, +20 sucursales, sin equipo de IA | Respuesta normativa vigente en segundos, sin cargar a Cumplimiento, actualizada sola | Proveedor del modelo, estudio que valida · abono por sucursal · sólo lavado de dinero, 3 sucursales, 1 mes |
| **Portal:** autogestión de RRHH | Bancos y financieras de 500 a 3.000 empleados que firman recibos en papel | Que Capital Humano deje de imprimir y juntar firmas; trámites desde el celular | Certificadora de firma, sistema de sueldos · abono por empleado · sólo recibos, un área, 2 meses |
