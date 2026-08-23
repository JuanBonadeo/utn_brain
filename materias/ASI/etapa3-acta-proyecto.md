# Acta de Proyecto — Etapa 3 del TP Integrador

> **Fuente de verdad de este entregable.** El `.docx` se genera desde acá con
> `npm run docx -- materias/ASI/etapa3-acta-proyecto.md materias/ASI/etapa3-acta-proyecto.docx`.
> Si hay que corregir algo, se corrige en este archivo
> y se regenera — no se edita el `.docx` a mano.
>
> Estructura tomada del **Anexo I de cátedra**
> (`fuentes/ASI/Campus/ASI-Unidad5_Adm_Recursos_en_ProyectosIT/ASI-5-T1-Proyectos_AnexoI_ActaProyecto.doc`),
> con las instrucciones campo por campo del apunte T2. Ver Unidad 5 §6 de la wiki.
>
> **Estado al 2026-08-23: borrador actualizado.** El docente validó el punto 3 el
> 23/08 e indicó **SaaS FSM configurable** como modo de construcción. `Producto` y
> `Entregables` ya se reescribieron sobre esa base y la autoridad de compra pasó de
> infraestructura a licenciamiento y servicios. `Justificación`, `Objetivos` y
> `Límite` no cambiaron. Falta definir los nombres propios y el monto de autoridad.
>
> **Sin nombres propios, por decisión del grupo (2026-08-19).** Patrocinador y
> designados se identifican por **rol y área**, no por persona. El nombre del
> patrocinador aparece una sola vez, en el bloque de firma al final, que va en
> blanco para que lo complete quien autorice. El ejemplo de cátedra (ESABAL S.A.)
> sí usa nombres inventados; acá se optó por lo contrario.

---

## ACTA DEL PROYECTO

**Implementación de la Plataforma de Gestión de Órdenes de Trabajo de Campo (OT-Campo) para el proceso de instalación de internet con fibra óptica**

---

### DE

**Gerencia de Operaciones** — Personal (Telecom Argentina)

*Patrocinador del proyecto. Es el área titular del proceso crítico afectado y de
los objetivos de negocio que el proyecto compromete.*

### PARA

Integrantes de las áreas de la organización que deben tomar conocimiento del proyecto:

- Gerencia de Operaciones — Supervisión de Instalaciones
- Gerencia de Tecnología y Sistemas — Desarrollo, Infraestructura y Seguridad de la Información
- Centro de Operaciones de Red (NOC)
- Gerencia Comercial — Atención al Cliente
- Logística y Almacenes
- Compras y Abastecimiento
- Recursos Humanos
- Servicio de Higiene y Seguridad Laboral

Y el equipo del proyecto, inicialmente conformado por las personas indicadas en
el apartado DESIGNACIÓN.

### DESIGNACIÓN

El patrocinador designa los siguientes roles para la ejecución del proyecto:

<!-- cols: 44,56 -->

| Rol designado | Área de procedencia |
|---|---|
| Director de Proyecto | Gerencia de Tecnología y Sistemas |
| Arquitecto de Software / Líder Técnico | Gerencia de Tecnología y Sistemas — Desarrollo |
| Analista Funcional | Gerencia de Tecnología y Sistemas — Desarrollo |
| Responsable de Seguridad de la Información | Gerencia de Tecnología y Sistemas — Seguridad de la Información |
| Referente de Operaciones | Gerencia de Operaciones — Supervisión de Instalaciones |

El resto del equipo —desarrollo, experiencia de usuario, datos, pruebas,
infraestructura y capacitación— es conformado por el Director de Proyecto según
los perfiles y competencias descriptos en el punto 5 de esta etapa.

### DESCRIPCIÓN DE SU RESPONSABILIDAD

**Director de Proyecto.** Dirigir el proyecto y **conformar el equipo que lo
llevará adelante**: desarrollo, diseño de experiencia de usuario, datos, pruebas,
infraestructura y capacitación. Los perfiles y competencias de ese equipo se
detallan en el punto 5 de esta etapa. Es responsable de la planificación, del
cumplimiento del cronograma, del presupuesto aprobado, de la gestión de riesgos y
de las comunicaciones con el patrocinador y las áreas involucradas. Responde por
la entrega de los entregables comprometidos en este Acta.

**Arquitecto de Software / Líder Técnico.** Definir la arquitectura de la
plataforma y de las integraciones con SGOT, CRM, la base de datos de clientes y
órdenes de trabajo, y el sistema de gestión de red (NMS). Conducir técnicamente al
equipo de desarrollo que designe el Director de Proyecto y responder por la
calidad técnica de los entregables.

**Analista Funcional.** Relevar y validar los requerimientos con Supervisión de
Instalaciones, técnicos de campo, NOC y Logística. Responsable de la **medición
de las líneas base** de los indicadores comprometidos en los objetivos, y de la
definición de las reglas de priorización y del motor de asignación.

**Responsable de Seguridad de la Información.** Definir e implementar los
controles de acceso, autenticación y auditoría de la plataforma, incluida la
baja automática de credenciales integrada con Recursos Humanos. Verificar el
cumplimiento de la Ley 25.326 de Protección de Datos Personales sobre los datos
de clientes que la aplicación de campo trata.

**Referente de Operaciones.** Ser el nexo entre el equipo del proyecto y la
operación. Facilitar el acceso a la información del proceso, a los técnicos y a
las zonas de trabajo; coordinar el piloto y validar funcionalmente los
entregables antes de su aceptación.

### DESCRIPCIÓN DE SU AUTORIDAD

**Director de Proyecto.** Tiene autoridad para asignar trabajo dentro del equipo
del proyecto, coordinar con las áreas involucradas y con proveedores, y validar
entregables intermedios. Puede aprobar cambios que **no afecten** el alcance, el
costo total ni la fecha de finalización comprometidos en este Acta; todo cambio
que afecte alguno de esos tres factores debe elevarse al patrocinador para su
aprobación. Tiene autoridad para acceder a las instalaciones de la organización
en horario de funcionamiento y, cuando el proyecto lo requiera, fuera de él,
coordinando previamente con el Referente de Operaciones.

**Arquitecto de Software / Líder Técnico.** Tiene autoridad para definir la
arquitectura técnica y aprobar o rechazar diseños de integración. Las decisiones
que impliquen modificar los sistemas existentes (SGOT, CRM, NMS) requieren
acuerdo previo del área propietaria de cada sistema.

**Analista Funcional.** Tiene autoridad para convocar a usuarios clave de
Operaciones, NOC y Logística a instancias de relevamiento y validación, dentro
de la disponibilidad acordada con cada área.

**Responsable de Seguridad de la Información.** Tiene autoridad para **bloquear
la puesta en producción** de cualquier componente que no cumpla las políticas de
seguridad de la organización o la normativa de protección de datos personales.
Esta decisión solo puede ser revertida por la Gerencia de Tecnología y Sistemas.

**Referente de Operaciones.** Tiene autoridad para autorizar el ingreso del
equipo del proyecto a las zonas operativas y para definir, junto con Supervisión
de Instalaciones, la zona y el momento del piloto.

⚠ *Autoridad de compra: el Director de Proyecto puede aprobar adquisiciones
hasta el monto fijado por la política de compras vigente de la organización;
para excederlo debe solicitar autorización a la Gerencia de Administración y
Finanzas.* **(Completar con el monto real si el grupo lo define. Este es el
campo donde el ejemplo de cátedra es más concreto — conviene no dejarlo genérico.)**

---

## ALCANCE DEL PROYECTO

### Justificación

El proceso de instalación de internet con fibra óptica, relevado y modelado en
la Etapa 1 de este trabajo, presenta tres debilidades que fueron identificadas y
documentadas en las etapas anteriores y que hoy no tienen tratamiento:

1. **Falta de trazabilidad de la orden de trabajo.** El estado real de la
   instalación no está disponible en tiempo real para las áreas que lo
   necesitan, lo que genera reclamos duplicados y consultas manuales entre
   Operaciones, NOC y el área Comercial.

2. **Ausencia de criterio de priorización en la cola de órdenes de trabajo.**
   Identificado en la Etapa 2 como riesgo **R07**, valorado en severidad 12 y
   **sin plan de tratamiento**.

3. **Falta de control de competencias técnicas al asignar una orden.**
   Identificado en la Etapa 2 como riesgo **R04** — técnico sin capacitación en
   el nuevo modelo de ONT —, valorado en severidad 12 y **también sin plan de
   tratamiento**.

Este proyecto constituye el tratamiento de los riesgos R04 y R07, cubriendo un
hueco de la etapa anterior, y contribuye adicionalmente a la mitigación de R06
(ausencia de flujo de escalamiento en el CRM) al eliminar aguas arriba la causa
de los reclamos duplicados, y de R05 (credenciales de contratistas sin baja),
dado que la aplicación de campo es el control ya comprometido en la Etapa 2 para
que los técnicos contratistas operen sin acceso a los sistemas de backend.

Asimismo, el proyecto da cumplimiento al **objetivo de TI ya definido por la
organización en la Etapa 1** — *implementar una aplicación de gestión para
técnicos de campo que permita aumentar la productividad operativa en un 5%* — y
a la meta de TI *Asignación Optimizada de Técnicos*, ambos alineados con el
objetivo de negocio de *aumentar el rendimiento de los técnicos en un 5%,
medido como instalaciones sobre horas de trabajo*.

### Producto

**Plataforma de gestión de órdenes de trabajo con aplicación móvil de campo**:
solución de mercado de *Field Service Management*, contratada como servicio,
configurada e integrada con los sistemas existentes y en producción, que gestiona
el ciclo completo de la orden de trabajo de instalación de fibra óptica, desde el
despacho hasta el cierre con conformidad del cliente.

Comprende seis componentes:

1. Módulo de despacho y priorización, con cola única alimentada por CRM, SGOT y
   excepciones del NMS, cronómetro de SLA y escalamiento.
2. Motor de asignación por competencia certificada, zona o nodo, carga del día,
   ventana horaria y stock del vehículo.
3. Aplicación móvil de campo *offline-first* del proveedor, configurada con
   agenda, ficha de orden de trabajo, checklist por modelo de ONT, registro de
   mediciones ópticas, evidencia fotográfica, geolocalización, consumo de
   materiales, tipificación obligatoria del motivo cuando la visita no se
   completa y conformidad del cliente con firma digital.
4. Integraciones con SGOT, CRM, base de datos de clientes y órdenes de trabajo,
   NMS y sistema de stock.
5. Capa de seguridad: inicio de sesión único con doble factor, mínimo
   privilegio, baja automática de credenciales integrada con Recursos Humanos y
   registro de auditoría.
6. Tablero de indicadores para Supervisión y Gerencia de Operaciones.

Los componentes 1, 2, 3 y 6 se obtienen configurando la plataforma contratada;
los componentes 4 y 5 —integraciones y capa de seguridad— se construyen sobre
la infraestructura de la organización.

### Entregables

Primera aproximación de la Estructura de Desglose de Trabajo, con los
entregables principales por fase:

<!-- cols: 30,70 -->

| Fase | Entregable principal |
|---|---|
| 1. Inicio | Acta de Proyecto aprobada |
| 2. Relevamiento y análisis | Documento de requerimientos validado y **medición de las líneas base** de los indicadores |
| 3. Selección de proveedor | RFI, lista corta, RFP evaluado y contrato firmado |
| 4. Diseño y configuración | Plataforma configurada: flujos, roles, matriz de competencias, reglas de priorización, SLA y tableros |
| 5. Integración y seguridad | Integraciones operativas y controles de seguridad implementados |
| 6. Migración de datos | Matriz de competencias y datos maestros cargados |
| 7. Pruebas | Informe de pruebas funcionales, de integración y de seguridad |
| 8. Piloto | Informe de piloto en zona acotada, con ajustes aplicados |
| 9. Capacitación | Técnicos, supervisores y despachantes capacitados |
| 10. Despliegue por olas | Plataforma en producción en todas las zonas |
| 11. Estabilización y cierre | Documentación, transferencia operativa, alta del elemento de configuración en la CMDB y cierre formal |

### Objetivos

<!-- cols: 5,22,27,16,13,17 -->

| # | Objetivo | Indicador | Línea base | Meta | Plazo |
|---|---|---|---|---|---|
| O1 | Aumentar la productividad del técnico de campo | Instalaciones finalizadas conformes ÷ horas-técnico disponibles | 0,50 inst./hora-técnico *(supuesto)* | 0,525 (+5%) | 6 meses desde la puesta en producción |
| O2 | Reducir la latencia de registro del cierre de la orden de trabajo | % de órdenes cerradas en el sistema dentro de los 15 minutos de terminada la visita, y tiempo medio entre asignación y cierre | 20% · 26 h *(supuesto)* | ≥90% · ≤8 h | Mes 4, sostenido 3 meses |
| O3 | Reducir las visitas fallidas por causa evitable | Órdenes reprogramadas por "técnico sin competencia" o "kit incompleto" ÷ órdenes despachadas | 12% *(supuesto)* | ≤6% | 6 meses desde la puesta en producción |
| O4 | Asegurar el cumplimiento de la priorización de la cola | % de órdenes despachadas según el orden del motor de priorización, y % de cumplimiento del SLA de primera respuesta | No medible en la situación actual — esa imposibilidad **es** la definición del riesgo R07 | ≥95% · ≥90% | Mes 3 desde la puesta en producción |

> **Sobre las líneas base.** Los valores indicados como *supuesto* son
> estimaciones: las Etapas 1 y 2 de este trabajo no relevaron indicadores de
> operación. Su medición formal constituye un entregable propio de la fase 2
> (Relevamiento y análisis), y las metas se recalibrarán sobre los valores
> reales medidos.

### Límite

El proyecto **no incluye**:

- El rediseño del flujo de escalamiento del CRM (riesgo R06), que cuenta con
  plan de tratamiento propio en la Etapa 2.
- El reemplazo o la migración del CRM, del SGOT o de la base de datos de
  clientes y órdenes de trabajo.
- Obra civil, tendido troncal, ampliación de nodos (riesgo R11) y mantenimiento
  preventivo del cable (riesgo R08).
- El reemplazo del firewall (riesgo R03), la redundancia del balanceador de
  carga (riesgo R09) y la correlación de eventos del NMS (riesgo R10).
- Los procesos de venta, facturación y recupero de clientes.
- Otros procesos de campo distintos de la instalación: reparaciones, mudanzas y
  desinstalaciones.
- La adquisición de vehículos y fusionadoras de fibra óptica.
- Las actividades 1 y 2 del proceso modelado en la Etapa 1 —recepción de la
  solicitud y verificación de cobertura—, que continúan gestionándose en el CRM.

---

### Firma Autorizante

Nombre: _______________________________________________

Título: _______________________________________________
