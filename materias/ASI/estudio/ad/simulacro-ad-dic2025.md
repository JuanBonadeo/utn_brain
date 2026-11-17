## Simulacro AD — formato de la AD de diciembre 2025

> Mismas 5 consignas que la AD del 16/12/2025 (contexto Agromar ERP), pasadas a un proyecto de Bancorp. **Tiempo: 1 hora.** Resolvé sin mirar: la resolución está en la página siguiente.

**Contexto: BANCORP S.A. Proyecto: Modernización e Integración de Canales Electrónicos (Omnicanalidad).**

1. Para el proyecto defina **3 objetivos de negocio** y **3 objetivos de TI** especificando **métricas**.
2. Riesgo: *"La instalación de una actualización de la plataforma de canales en el módulo de transferencias registra importes inválidos en las transferencias iniciadas en Home Banking y confirmadas en la app, desencadenando reclamos de los clientes"*. **Calcular severidad**, indicar **disparadores** y definir un **plan de contingencia**.
3. Indique los **cargos necesarios para mitigar** el riesgo anterior y redacte un **anuncio** indicando conocimientos, competencias, experiencia requerida y también **"qué ofrece la empresa"**.
4. A partir del incidente informado al **responsable de atención al cliente**: *"Se recibe el reclamo de un cliente por débitos en su cuenta que no corresponden a las operaciones que realizó"*, indique los **puestos / áreas del organigrama** involucrados y **qué pasos se siguen en caso de que se escale**.
5. **Adquisiciones, responsables y criterios** para la plataforma omnicanal.

<div style="page-break-before: always"></div>

## Resolución

### 1. Objetivos

| | Objetivo | Métrica (cómo se mide) |
|---|---|---|
| **N1** | Pasar a Home Banking y app el 40% de los plazos fijos y pagos de servicios que hoy se hacen en sucursal, antes de dic-2027 | % de operaciones por canal, reporte mensual de Banca Minorista |
| **N2** | Que el 85% de los clientes digitales califique la experiencia con 4 o más sobre 5, a 12 meses del lanzamiento | Encuesta dentro de web y app |
| **N3** | Bajar un 25% el costo por transacción durante 2028, por operaciones que dejan la sucursal | Costo por transacción, informe de Administración y Finanzas |
| **T1** | Que web y app tomen el 100% de las operaciones de la misma capa de APIs antes de sep-2027 | % de operaciones servidas por la API común (monitoreo de [04]) |
| **T2** | Disponibilidad mensual de 99,8% y respuesta en menos de 2 segundos en el 95% de las operaciones | Monitoreo 24×7 de Operaciones TI [04], reporte mensual |
| **T3** | Token unificado activo para el 100% de los clientes digitales, sin incidentes de seguridad críticos en el primer año | % de clientes migrados ([03]) e incidentes registrados por el SOC [02] |

Los de **negocio** los entiende cualquiera: operaciones, satisfacción y costo. Los de **TI** son técnicos: arquitectura, disponibilidad y seguridad. Cada objetivo de TI sostiene a uno de negocio: T1 a N1, T2 a N2 y T3 a la Confianza. Todos tienen número y plazo (SMART).

### 2. Riesgo

- **Clasificación SEI:** 2. Fallas de sistemas y tecnología → 2.2 Software → **control de cambios / testing**. Una versión salió a producción sin probar bien los recorridos entre canales.
- **Activos:** información (importes y saldos), software (plataforma de canales), el servicio de transferencias y la reputación.
- **Probabilidad = 3 (media).** El contacto es **periódico**: hay una actualización en cada sprint. La lógica compartida entre canales es nueva y los recorridos web → app son muchos. Hay ambiente de prueba y gestión de cambios, así que la capacidad de resistencia es media, no baja.
- **Impacto = 5 (muy alto).** La **pérdida primaria** es la plata transferida mal, el costo de detectar y revertir, y el servicio frenado. La **secundaria** son los reclamos masivos, la exposición ante el BCRA por protección del usuario financiero, los medios y el daño a **Confianza y Solidez** e **Integridad**.
- **Severidad = 3 × 5 = 15 de 25 (alta).** Va entre los primeros de la lista (Pareto) y se trata con mitigación.

**Disparadores** (cómo nos damos cuenta de que se materializó):

1. La **conciliación automática** de [04] encuentra diferencias entre el importe confirmado en la app y el debitado en el core.
2. Llegan **más de 5 reclamos del mismo tipo en una hora** a la Mesa de Ayuda o a las sucursales después de un despliegue.
3. El **SOC [02]** ve un patrón anómalo de importes en las transferencias.
4. Errores de validación de importes en los logs de la plataforma en las 2 horas posteriores a un despliegue.

**Plan de contingencia:**

| # | Situación | Qué se hace | Responsable |
|---|---|---|---|
| 1 | Contener | Se suspenden las transferencias entre canales; cada canal sigue operando por separado. Se vuelve a la versión anterior (**rollback**) como cambio de emergencia | [04] suspende; [03] hace el rollback; lo aprueba el CIO (comité de emergencia) |
| 2 | Corregir lo afectado | Se identifican las transferencias con importes inválidos desde el despliegue y se revierten o ajustan los débitos | [04] con Clearing (Gerencia de Operaciones Bancarias) |
| 3 | Atender a los clientes | Guion en la Mesa de Ayuda y en plataforma: "su dinero está resguardado y se reintegra en 24 h". Cada reclamo se vincula al incidente mayor | [06] y el Personal de Plataforma de las sucursales |
| 4 | Comunicar | Se informa a Gerencia General y a Cumplimiento, que evalúa si hay que informar al BCRA. Banca Minorista avisa a los clientes afectados | CIO, Cumplimiento Normativo, Banca Minorista |

**Continuidad:** las transferencias dentro de un mismo canal y las sucursales siguen funcionando. **Recuperación:** se corrige la versión, se suman pruebas automáticas de los recorridos entre canales y el despliegue pasa a ser gradual (primero el 5% de los clientes).

### 3. Cargos para mitigar el riesgo y anuncio

| Cargo | Área | Qué aporta a la mitigación |
|---|---|---|
| **Analista QA Sr. (automatización de pruebas)** | [03] célula de Canales Digitales | Pruebas de regresión automáticas de los recorridos web → app antes de cada versión (baja la P) |
| **Analista de Gestión de Cambios y Versiones** | [04] Operaciones TI | Controla que ningún cambio pase a producción sin pruebas aprobadas y que exista un plan de rollback |
| **Especialista en monitoreo y conciliación** | [04] Operaciones TI (monitoreo 24×7) | Conciliación automática después de cada despliegue: detecta antes y limita el daño (baja el I) |

**Anuncio** (redactado con AIDA):

> **¿Querés que cada transferencia de nuestros clientes llegue exacta? Bancorp busca Analista QA Senior — Automatización de Pruebas** *(Atención)*
>
> **Quiénes somos.** Bancorp S.A. es un banco de capitales 100% nacionales, con 45 sucursales en todo el país y en plena transformación digital de sus canales.
>
> **El desafío** *(Interés)*. Te vas a sumar a la célula de Canales Digitales del área de Ingeniería de Software para:
> - diseñar y automatizar las pruebas de Home Banking y de la app antes de cada versión;
> - validar las operaciones que empiezan en un canal y terminan en otro;
> - participar en la aprobación de los cambios.
>
> Trabajás en Casa Central (CABA), en un esquema híbrido de 3 días presenciales, de lunes a viernes de 9 a 18, con guardias rotativas en los despliegues nocturnos.
>
> **Qué buscamos** *(Deseo)*.
> - **Conocimientos excluyentes:** automatización de pruebas web y mobile, pruebas de APIs, SQL.
> - **Conocimientos no excluyentes:** certificación ISTQB, integración continua, normativa del BCRA.
> - **Experiencia:** 3 años o más en QA, al menos 1 en sistemas financieros o de pagos.
> - **Formación:** Ingeniería o Licenciatura en Sistemas o carrera afín (avanzada o recibido).
> - **Competencias:** atención al detalle, pensamiento analítico, comunicación clara con los desarrolladores, trabajo en equipo y orientación al cliente.
>
> **Qué te ofrecemos.**
> - Relación de dependencia con obra social de primer nivel y bono anual por desempeño.
> - Condiciones preferenciales en los productos del banco.
> - Certificación ISTQB y capacitación pagas.
> - Plan de carrera hacia Líder de QA.
> - Trabajo híbrido.
>
> **Cómo postularte** *(Acción)*. Cargá tu CV con tu pretensión salarial en la sección "Trabajá con nosotros" del sitio de Bancorp, hasta el 15/12.

### 4. Incidente: áreas involucradas y escalado

**Puestos y áreas que intervienen:**

| Puesto / área (organigrama) | Qué hace |
|---|---|
| **Personal de Plataforma** de la sucursal (Banca Minorista), que es el responsable de atención al cliente | Toma el reclamo con los datos: cuenta, débitos desconocidos, fechas e importes. Lo registra y le da al cliente un número de seguimiento |
| **Líder de Operaciones de Sucursal / Gerente de Sucursal** | Supervisa, y si hay varios reclamos iguales lo informa como masivo |
| **Técnico de Mesa de Ayuda [06]** (1ª línea) | Registra el incidente, controla que no esté duplicado, lo vincula a los CI de la CMDB (app, API de transferencias, core) y busca en la base de conocimiento |
| **Coordinador de Soporte Interno [06]** | Controla el SLA y decide escalar |
| **SOC [02] / CISO** | Primero descarta o confirma **fraude**: un débito no reconocido puede ser una cuenta robada. Si hay sospecha, bloquea la cuenta en forma preventiva |
| **[03] célula de canales** o **[04] Coordinador de Sistemas Core** | 2ª línea: [03] si los débitos vienen de operaciones digitales, [04] si vienen del core o de un proceso batch |
| **Gerencia de Operaciones Bancarias (Clearing)** | Revierte o reintegra los débitos |
| **Cumplimiento Normativo y Riesgos** | Controla los plazos de respuesta al usuario financiero y si hay que informar al BCRA |
| **CIO → Gerencia General** | Escalado jerárquico |

**Pasos cuando se escala:**

1. **Registro y clasificación.** Plataforma carga el reclamo y la Mesa de Ayuda [06] lo registra. La prioridad sale de impacto × urgencia: es plata de un cliente, con posibilidad de que sea masivo y con plazos regulatorios, así que es **alta**.
2. **Primera línea.** [06] busca en la base de conocimiento. Si no lo resuelve en el tiempo del SLA, escala.
3. **Escalado funcional.**
   - Si hay sospecha de fraude, va al **SOC [02]**.
   - Si es un error de sistema: a **[03]** si el débito salió de web o app, a **[04]** si salió del core o del clearing.
   - El especialista diagnostica y propone la solución.
4. **Escalado jerárquico**, si no se resuelve en el SLA o la decisión excede al nivel técnico:
   - **Coordinador del área → CIO**: autoriza un cambio de emergencia o recursos extra.
   - **Gerencia General y Operaciones Bancarias**: autorizan el reintegro si es masivo.
   - **Cumplimiento**: decide si hay que informar al BCRA.
5. **Resolución y cierre.**
   - Clearing reintegra el importe.
   - Plataforma confirma con el cliente.
   - Se carga la solución en la base de conocimiento, se actualiza la CMDB y se cierra el ticket.
   - Si hubo varios casos iguales, se abre un registro en **Gestión de Problemas** para buscar la causa de fondo.
6. **KPI:** tiempo de resolución dentro del SLA y cantidad de incidentes escalados.

### 5. Adquisiciones, responsables y criterios

| Qué se adquiere | Características mínimas | Forma | Por qué |
|---|---|---|---|
| Plataforma de APIs (API gateway / middleware) | Que se integre con el core y el ESB actuales y soporte los picos de transacciones | Licencia o SaaS | Es la capa común de los dos canales |
| Solución de autenticación (token unificado) | Doble factor según BCRA, con kit para web y mobile | SaaS | Un solo token para todos los canales |
| Servidores para producción, prueba y respaldo | Alta disponibilidad en dos sitios | Cloud por uso o leasing | Disponibilidad de 99,8% (T2) |
| Herramientas de pruebas automáticas y de monitoreo | Que se integren al proceso de despliegue | Licencia o SaaS | Mitigan el riesgo del punto 2 |
| Pentest y pruebas de carga | Antes de cada salida a producción | Tercerizado | Seguridad y rendimiento verificados por terceros |

**Responsables:**
- El **PM de la PMO [05]** coordina la adquisición.
- Los **arquitectos de [03]** y la **Infraestructura [01]** definen los requerimientos técnicos.
- **Banca Minorista** define los requerimientos funcionales y acepta.
- El **CISO [02]** valida la seguridad.
- **Administración y Finanzas** maneja el presupuesto, la compra y los contratos.
- **Cumplimiento** revisa la normativa de tercerización.
- El **CIO** aprueba.

**Proceso:** primero un **RFI** para conocer qué proveedores hay. Después un **RFP** a por lo menos 3 proveedores, que se evalúan con una matriz ponderada.

**Criterios:**
- **Técnicos (40%):** integración con el core y el ESB, seguridad y cifrado, escalabilidad en los picos, disponibilidad garantizada por SLA.
- **Funcionales (30%):** misma experiencia en web y app, operaciones que se empiezan en un canal y se terminan en otro, facilidad de uso y accesibilidad (valor Inclusión), reportes para Banca Minorista.
- **Del proveedor (30%):** experiencia en bancos y referencias, soporte 24×7, plazo de implementación, capacitación y **TCO** durante toda la vida útil, no sólo el precio inicial.
