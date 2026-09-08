# ASI — Machete expo Etapa 3 · Gonza (Casermeiro)

**Mi bloque: láminas 7 a 10 + la 22.**

- Arranco en **2:20** (cuando Bonadeo cierra la 6) y tengo que cerrar en **4:07** → **1:39 netos** para las cuatro.
- Vuelvo al final para la **22**: 50 s. Reloj final del grupo: 9:49.
- **Me entrega Bonadeo con:** *"Con el ciclo de vida definido, así se organiza el trabajo."*
- **Le paso a Lezcano con:** *"Esas medidas se materializan en dos planos."*
- Ninguna tabla se lee en voz alta. La 9 es lámina de consulta: enuncio qué significa y sigo.

---

## L7 — Las once fases · 22 s

- **11 fases**, cada una con un entregable verificable. Señalo tres.
- **Fase 2 — mide las líneas base.** Es lo vital: hoy los indicadores de los objetivos son **supuestos declarados**, porque las etapas anteriores no relevaron indicadores. Sin medirlas no hay contra qué evaluar si el proyecto funcionó.
- **Fase 3 — proceso formal de compras.** Sin RFI y RFP no hay plataforma: es **SaaS**, no lo desarrollamos, lo contratamos y lo configuramos.
- **Fase 11 — da de alta el sistema en la CMDB.** Cierra el circuito con la Etapa 2.

> **Si voy corto:** una sola frase → *"once fases, cada una con entregable verificable; la 11 cierra el circuito con la CMDB de la Etapa 2"*.

---

## L8 — EDT · 27 s

- **11 paquetes de primer nivel** y **50 paquetes de trabajo**. ← *el 11 me lo estaba comiendo*
- Cada paquete lleva: predecesora, duración, perfil y entregable.
- **Criterio de descomposición:** se para cuando el paquete tiene **un responsable único** y **un entregable verificable**. Por debajo de eso no se baja.
- Los **solapamientos están puestos a propósito**: varias actividades comparten perfil en la misma ventana. Es el insumo del análisis de sobreasignación que muestra Lezcano en la 15.

---

## L9 — Recursos humanos · 25 s

- **9 perfiles · 11 personas · 4.240 horas-persona** (= 530 días-persona, ventana d0–d192).
- Ningún perfil figura acá sin ser responsable de al menos un paquete de la EDT: la carga sale de sumar esas duraciones.
- Ninguno alcanza dedicación completa → todos conservan sus tareas de línea.
- **Por qué 11 personas sobre 9 perfiles:** son los dos refuerzos del aplanamiento — **2 en integraciones y 2 en pruebas**.
- **Remate:** *"no es volumen, es aplanamiento, y evita 23 días de atraso."*

> ⚠️ **NO decir 187 acá.** El 187/215/192 es la lámina 15, de Lezcano. Mi único número es **23**. (Detalle abajo, en Apuntes.)

---

## L10 — Higiene y seguridad · 25 s

- Analizamos los sectores del proceso crítico, **incluido el campo**, que es donde están los riesgos graves: caída de altura, riesgo eléctrico, espacio confinado.
- Ordenamos las medidas por las **cuatro acciones de la prevención primaria**: **diseño → origen → medio → persona**.
- Asumimos que el **EPP es el escalón más débil**: es la acción 4, sobre la persona, y depende de una conducta diaria.
- Y hay un caso donde **el propio sistema es la medida preventiva de diseño**: la app **bloquea el despacho de la OT** si el técnico tiene la habilitación vencida. La habilitación vigente pasa a ser condición de despacho, y el control deja de depender de la memoria.

> ⚠️ Si preguntan *"¿cuántos niveles de prevención hay?"* → **tres** (primaria, secundaria, terciaria). La que tiene cuatro escalones es la **primaria**. Por eso digo *"las cuatro acciones de la prevención primaria"*, no *"los cuatro niveles"*.

---

## L22 — Factibilidad legal y conclusión · 50 s · **NO SE RECORTA**

**Legal.** Alojar datos personales en una plataforma contratada como servicio los saca del perímetro de la organización:

- El **proveedor pasa a ser encargado del tratamiento**.
- Si los servidores están fuera del país, se configura **transferencia internacional de datos**.
- El **deber de seguridad sigue siendo nuestro**. No se delega con el contrato.

**Conclusión, en tres partes:**

- **Técnicamente factible**, con un supuesto crítico declarado: que el SGOT, el CRM y el NMS expongan interfaces de programación para poder integrarlos.
- **Económicamente viable pero de margen estrecho**: a tres años todavía no se repaga.
- **Legalmente factible bajo condición contractual**: sin las cláusulas del punto 8, el proyecto **agravaría el R05 en lugar de contenerlo**.

**Remate:**

- Por eso la decisión de **despliegue masivo no se toma con la aprobación del Acta**, sino en el **paquete 8.4**: una vez medidas las líneas base, verificadas las interfaces y cerrados los precios.
- *"Muchas gracias."*

---

# Apuntes — lo que tengo que tener claro por si preguntan

## El 187, en criollo

Pensalo como una cocina.

| Escenario | Qué supone | Días |
|---|---|---|
| **187** | Cocineros infinitos: cada tarea arranca apenas la dependencia lo permite, siempre hay alguien libre. Es el CPM puro, **recursos ilimitados**. 30 actividades críticas. | 187 |
| **215** | Aplanado con **una persona por perfil**. El único especialista de integraciones no se puede clonar, así que sus cuatro integraciones se ponen en fila india. +28 días. | 215 |
| **192** | Aplanado **con refuerzo**: 2 en integraciones y 2 en pruebas. Lo que estaba en fila vuelve a correr en paralelo. **Es el adoptado** (~9,1 meses). | 192 |

- **Los 23 días son 215 − 192**: lo que compran las dos personas de refuerzo. El fundamento de contratarlas es económico.
- **Mi error a evitar:** pegar *"una persona por perfil"* con *"recursos ilimitados"*. Son los dos escenarios opuestos.
- Y los conflictos de sobreasignación **caen sobre actividades críticas**, así que no se resuelven corriendo tareas dentro de la holgura: hay que agregar gente o estirar el proyecto.

## RFI vs. RFP (por la fase 3)

- **RFI** — *Request for Information*. Explora **el mercado**. Se emite temprano, antes de fijar especificaciones: qué plataformas existen, qué integran de forma nativa, qué licenciamiento manejan, dónde alojan los datos. **No vinculante.** Producto: mapa del mercado + lista corta. Paquete **3.1**, 5 días.
- **RFP** — *Request for Proposal*. Compara **la oferta**. Se emite tarde, solo a la lista corta y con requerimientos ya aprobados: propuesta técnica y económica, cronograma, equipo, SLA, migración, cláusulas de datos. **Vinculante** para el oferente; su aceptación deriva en contrato. Paquete **3.3**, 7 días.
- **La frase:** *el RFI reduce la incertidumbre sobre el mercado, el RFP reduce la incertidumbre sobre la oferta.*
- **Por qué no se saltea el RFI:** escribir el pliego sobre supuestos deja el pliego desierto (exijo algo que ninguna plataforma regional ofrece) o me pierdo capacidades disponibles.
- **Por qué no un RFQ** (*Request for Quotation*): lo que se contrata no es un bien de especificación cerrada comparable solo por precio — hay licenciamiento, configuración, 4 integraciones, migración y soporte. El RFQ sí serviría para los dispositivos rugerizados.
- La fase 3 completa: 3.1 RFI (5 d) → 3.2 lista corta (5 d) → 3.3 RFP (7 d) → 3.4 evaluación (8 d) → 3.5 contrato (6 d) = **31 días críticos consecutivos**. Es el tramo más largo y menos comprimible del proyecto.

## CMDB (por la fase 11)

- *Configuration Management Database*. Repositorio centralizado de los **elementos de configuración (CI)**: **hardware, software, documentación y personas** de la infraestructura del cliente y de los servicios que se le prestan.
- La mantiene la práctica ITIL de **Gestión de la Configuración del Servicio**.
- Lo que la distingue de un inventario común son las **relaciones entre CI**: habilitan el **análisis de impacto** (cómo un cambio en un CI afecta a otros CI y a los servicios). Un inventario dice qué tengo; la CMDB dice de qué depende.
- **Por qué cierra el circuito con la Etapa 2:** el inventario de activos ya lo relevamos y valoramos ahí. Dar de alta el sistema nuevo en la CMDB lo incorpora a ese mismo inventario vivo.

## Preguntas probables de mi bloque

- **"¿Por qué 11 personas si son 9 perfiles?"** → los dos refuerzos del aplanamiento: segundo especialista de integraciones y segundo responsable de pruebas.
- **"¿Por qué dos personas en integraciones y en pruebas?"** → con una por perfil el proyecto pasa de 192 a 215 días. Los conflictos caen sobre actividades críticas, así que no se resuelven corriendo tareas dentro de la holgura.
- **"¿Por qué el costo de RRHH es de 3.456 horas y no 4.240?"** → porque el **consultor de plataforma aporta 784 horas y lo provee el proveedor**, no la organización. No se computa como RRHH propio: se imputa dentro del servicio de implantación contratado. **3.456 + 784 = 4.240**, sin duplicar importes.
- **"¿Por qué SaaS y no desarrollo propio?"** → reduce plazo y riesgo técnico, a cambio de costo recurrente y de sacar los datos del perímetro, que es lo que se compensa por contrato.
- **"¿Qué pasa si el SGOT no tiene API?"** → plan alternativo en tres vías: base de datos intermedia, intercambio por lotes o automatización de interfaz. Las tres se cotizan en el RFP y las tres cuestan más horas del especialista de integraciones.
- **"¿Por qué el EPP es el eslabón más débil?"** → porque es prevención sobre la persona (acción 4) y depende de una conducta diaria. Por eso el layout muestra prevención **en el diseño** (acción 1) y el sistema bloquea el despacho: eso no depende de que alguien se acuerde.

---

*Derivado de `../entregables/etapa3-guion.md` (guion completo de las 22 láminas) y de `../entregables/etapa3.md` (entregable). Si cambia un número, cambia allá primero.*
