# Etapa 4 — Emprendedorismo

> **Fuente de verdad de este entregable.** El `.docx` y el `.pdf` se generan desde acá con
> `npm run docx -- materias/ASI/entregables/etapa4.md materias/ASI/entregables/etapa4.docx`
> y después `scripts/preview-docx.sh`. No editar los generados a mano.
>
> **Anexo I — Business Model Canvas.** Lámina A3 apaisada en archivo independiente:
> `etapa4-canvas.html` → `etapa4-canvas.pdf`.
>
> **Estado al 2026-10-20.** Las tres actividades de la consigna están desarrolladas y no queda
> nada pendiente de definición. Idea elegida por el grupo: plataforma de reclamos urbanos con
> ruteo a municipio y prestadoras, app de cuadrilla y datos abiertos (candidata A).
>
> **Encuadre que no hay que perder.** Rosario **ya tiene** 147 + SUA + CIOR + Munibot. La
> startup no compite con eso: Rosario es el modelo de referencia y un posible cliente de
> integración. El mercado objetivo son los municipios medianos del Gran Rosario y de la provincia.
>
> **Todos los números son supuestos de la fase de búsqueda** (Lean Startup, C2): precios,
> proyección y costos están marcados como hipótesis a validar con el MVP. No hay datos medidos.
>
> **Definido el 2026-10-20** (eran los dos ⚠ de la versión 1):
> - Cinco roles, cada uno dueño de una hipótesis del MVP (tabla del 2.6). Los roles **no tienen
>   nombres asignados**: si el grupo los quiere, se agregan como columna en esa tabla.
> - Pacto de socios con *vesting* a cuatro años con un mínimo de uno (riesgos del punto 1).
> - 20% de la SAS al inversor por USD 70.000 (valuación posterior USD 350.000), en dos tramos de
>   USD 35.000; el segundo se libera cuando el municipio piloto firma la suscripción (H4).
>
> **El resumen del punto 3 tiene que entrar en una página con Lexend**, que es más ancha que
> la fuente que sustituye LibreOffice o Word si no la tienen instalada. Para medir sin Lexend,
> renderizar una copia con Verdana (tan ancha o más): si entra con Verdana, entra con Lexend.
>
> **No correr `scripts/fix-cols-md.py` sobre este archivo.** Los anchos de columna están puestos
> a mano. El script reparte por volumen de texto sin contar negritas ni el ancho de la fuente, y
> con Lexend corta palabras ("Económic-o", "Participació-n") y parte montos en dos renglones.
>
> Contenido tomado de la wiki: Unidad 6 y sección TP Integrador.

---

## UNIVERSIDAD TECNOLÓGICA NACIONAL

### CÁTEDRA

Administración de Sistemas de Información — 4º Año Ingeniería en Sistemas de Información

### TRABAJO PRÁCTICO INTEGRADOR 2026 — ETAPA 4

**Emprendedorismo**

*Cuadra: plataforma de reclamos urbanos con ruteo entre organizaciones, app de cuadrilla y datos abiertos*

**Comisión Nº:** 403

**Grupo Nº:** 310

### INTEGRANTES

*Legajo, Apellido y Nombres, Email*

- 53535, Bonadeo Juan Cruz, juancruzbonadeo04@gmail.com
- 52674, Casermeiro Gonzalo, gonzacasermeiro@gmail.com
- 53543, De la Rosa Valentín Yael, mferreyra079@gmail.com
- 53215, Lezcano Diego, diegolezcano209@gmail.com
- 52688, Lurati Ignacio, ignaciolurati2@gmail.com

### VERSIÓN DEL DOCUMENTO

<!-- cols: 8,13,13,66 -->

| Mod | Fecha | Autor | Descripción |
|---|---|---|---|
| 1 | 14/10/2026 | Grupo N310 | Primera versión: idea de startup, Business Model Canvas con fuentes de ingreso y resumen para el inversor |
| 2 | 20/10/2026 | Grupo N310 | Equipo fundador con un rol y una hipótesis del MVP por cofundador; pacto de socios con consolidación gradual de acciones; participación ofrecida al inversor, en dos tramos atados al piloto; resumen para el inversor ajustado a una página |

### ÍNDICE

1. Idea de startup
2. Business Model Canvas y fuentes de ingreso
3. Resumen del negocio para un socio inversionista

Anexo I — Business Model Canvas (lámina, archivo independiente)

---

## 1. IDEA DE STARTUP

### El problema

Un vecino ve un bache, una luminaria apagada, un contenedor desbordado o un cable caído después de una tormenta. Para que se resuelva, primero tiene que saber **de quién es el problema**: la calle y la luminaria son del municipio, el poste y el medidor de la distribuidora eléctrica, la pérdida de agua de la prestadora de agua, y el cable colgado de alguna de las empresas de telecomunicaciones o cableoperadoras. Si se equivoca de destinatario, el reclamo se pierde o se deriva a mano. Si acierta, igual no sabe cuándo se va a resolver, y la única forma de enterarse es volver a reclamar.

Del otro lado, quien resuelve tampoco la tiene fácil. El mismo bache entra veinte veces por canales distintos —teléfono, redes sociales, mensajería, mostrador—, nadie sabe cuántos reclamos son en realidad uno solo y la cuadrilla sale con una dirección escrita a mano y sin foto. Además, el cierre no deja evidencia: no hay forma de saber si el problema efectivamente se resolvió ni cuánto se tardó.

**Rosario resolvió buena parte de esto para su propio ámbito.** Tiene la línea 147, el Munibot, formularios web y el Sistema Único de Atención (SUA), todo dentro del Centro Integrado de Operaciones (CIOR). En la Etapa 1 lo tomamos como uno de los fundamentos para evaluar la ciudad como "en transición" hacia ciudad inteligente. Ese diagnóstico también marcaba lo que falta: **una estrategia unificada y financiamiento para escalar.** Ese modelo no está disponible para los municipios medianos del Gran Rosario y de la provincia, que no pueden desarrollar ni operar un sistema así por su cuenta. Y ni siquiera en Rosario el reclamo llega integrado a las prestadoras que tienen infraestructura en la vía pública.

### La idea

**Cuadra** es una plataforma en la nube que lleva el reclamo urbano desde el vecino hasta la cuadrilla que lo resuelve, sea del municipio o de una prestadora, y publica cuánto se tarda en resolverlo.

<!-- cols: 24,76 -->

| Módulo | Qué hace |
|---|---|
| **App del vecino** | Aplicación web que no requiere instalación, accesible también desde un código QR en el mobiliario urbano. El vecino saca una foto, la ubicación se toma por GPS y elige una categoría. Recibe un número de seguimiento y una notificación en cada cambio de estado, y al cierre ve la foto del trabajo terminado y puede calificarlo |
| **Motor de ruteo** | Clasifica el reclamo por categoría y por imagen, y lo asigna al responsable según el tipo de problema y la zona: área municipal o prestadora. Agrupa los reclamos repetidos sobre el mismo problema en una sola orden de trabajo con varios seguidores |
| **App de cuadrilla** | Orden de trabajo en el celular, con funcionamiento sin conexión, priorización, foto del antes y del después y cierre georreferenciado. Es el mismo tipo de solución que planificamos en la Etapa 3 para las instalaciones de fibra óptica de Personal: trazabilidad, priorización y evidencia de cierre |
| **Tablero público y datos abiertos** | Tiempos de resolución por barrio, por categoría y por organización responsable, con un conjunto de datos descargable en formatos abiertos. Los datos del vecino nunca se publican: se publican agregados y anonimizados |
| **Conector** | Interfaz de integración con los sistemas que ya existen —el SUA de un municipio grande, el sistema comercial de una prestadora— para sumarse a lo que hay en vez de reemplazarlo |

### Ejes de la consigna que cubre

<!-- cols: 34,66 -->

| Eje | Cómo lo cubre |
|---|---|
| Empleo de TICs | Toda la solución: aplicaciones móviles, plataforma en la nube, clasificación por imagen, integración entre organizaciones |
| Transparencia entre gobiernos y ciudadanos | El vecino ve en qué estado está su reclamo y quién lo tiene, y el tablero público muestra los tiempos reales de cada responsable |
| Datos compartidos (open data) | Conjunto de datos abierto de reclamos y tiempos de resolución, anonimizado y descargable |
| Planificación urbana eficiente | El historial georreferenciado muestra dónde se repiten los problemas y orienta el mantenimiento preventivo y las obras |
| Preocupación por el entorno social | El tablero hace visible la desigualdad entre barrios en los tiempos de respuesta |
| Sostenibilidad ambiental y residuos | Contenedores desbordados y basurales entran como categoría con ruteo propio. Además, agrupar reclamos y priorizar evita viajes innecesarios de cuadrillas |

### Por qué es una idea disruptiva y no una app más

La disrupción, como vimos en la Unidad 6, no está en la tecnología sino en **cambiar el comportamiento del mercado**. Hoy el reclamo urbano es un trámite que cada organización atiende por separado y sin rendir cuentas. Cuadra lo convierte en un **servicio con tiempos públicos y medibles** que cruza organizaciones. Para el vecino deja de importar de quién es el problema, y para el municipio la demora deja de ser invisible.

### Tipo de mercado y clientes

**Tipo de mercado: resegmentado.** El modelo de atención ciudadana integrada ya existe en las ciudades grandes; Cuadra lo adapta, como servicio por suscripción, a un segmento que hoy no puede acceder a él. Los clientes son posiblemente conocidos y la necesidad es de adaptación: es el riesgo de redefinición que describe la cátedra, y lo enfrentamos con un MVP.

<!-- cols: 28,72 -->

| Tamaño del mercado | Estimación *(a validar en la fase de descubrimiento)* |
|---|---|
| Mercado total disponible | Los gobiernos locales de la provincia de Santa Fe que reciben reclamos sobre el espacio público, y las prestadoras de servicios con infraestructura en la vía pública |
| Mercado atendido disponible | Municipios con cuadrillas propias y volumen de reclamos suficiente para que la trazabilidad tenga valor, más las prestadoras que operan en ellos. Su tamaño se releva hablando con secretarías de gobierno y de servicios públicos |
| Mercado objetivo | Años 1 y 2: municipios del Gran Rosario (Funes, Roldán, Granadero Baigorria, Villa Gobernador Gálvez, Pérez, Capitán Bermúdez, San Lorenzo). Año 3: otras ciudades medianas de la provincia. Meta: 3, 8 y 14 municipios al cierre de cada año |

**Early adopters:** un municipio mediano del Gran Rosario con agenda de modernización y una prestadora con cuadrillas propias en la zona. **Actores críticos:** las cuadrillas municipales y de las prestadoras, que no compran el sistema pero de cuyo uso real depende que el tablero refleje la realidad.

### MVP y aprendizaje validado

El MVP es del tipo **Mago de Oz**: un **piloto de 90 días** en un municipio del Gran Rosario. El vecino usa la aplicación real, pero el ruteo lo hace a mano el equipo, que clasifica cada reclamo y lo deriva al área o a la prestadora por los canales que ya usan. El tablero público se publica desde el primer mes. Así se valida si hay demanda antes de construir el motor de ruteo y los conectores.

<!-- cols: 8,56,36 -->

| Nº | Hipótesis | Criterio de validación al día 90 |
|---|---|---|
| H1 | Los vecinos usan un canal nuevo si les muestra el seguimiento | Al menos el 15% de los reclamos del municipio entra por la aplicación |
| H2 | Buena parte de los reclamos son repetidos | Al menos el 25% de los reclamos se agrupa con otro sobre el mismo problema |
| H3 | La trazabilidad acorta los tiempos | El tiempo medio de resolución baja un 30% respecto de la línea base medida en el primer mes |
| H4 | El municipio paga por el servicio | El municipio piloto firma la suscripción al terminar el piloto |
| H5 | Las prestadoras aceptan recibir reclamos ruteados | Al menos una prestadora prueba la app de cuadrilla en la zona del piloto |

Si H4 falla pero H5 se confirma, el pivot natural es invertir los segmentos: que la prestadora sea el cliente principal y el municipio entre gratis como canal de los reclamos.

### Triple impacto

<!-- cols: 18,82 -->

| Pilar | Impacto |
|---|---|
| Económico | Ingresos recurrentes por suscripción y licencias. Al municipio le baja el costo por reclamo atendido y a la prestadora el de las salidas en falso de sus cuadrillas |
| Social | Rendición de cuentas: el vecino de un barrio periférico ve el mismo tablero que el del centro, y la desigualdad en los tiempos de respuesta se vuelve visible y discutible |
| Ambiental | Menos kilómetros recorridos por las cuadrillas, al agrupar reclamos y priorizar por zona; detección temprana de basurales, pérdidas de agua y luminarias encendidas de día |

### Riesgos considerados

Tomamos las causas de fracaso que la cátedra agrupa en la Unidad 6 y respondemos a las que más nos afectan.

<!-- cols: 30,70 -->

| Riesgo | Respuesta |
|---|---|
| Ciclo de venta largo del sector público y cambio de gestión cada cuatro años | Pilotos cortos con resultado medible; precios accesibles para un municipio mediano; cartera de varios municipios; el ingreso por prestadoras, que son privadas o mixtas, diversifica el riesgo político |
| Inflación y costos en dólares (la infraestructura en la nube se paga en dólares) | Precio fijado en dólares y cobrado en pesos al tipo de cambio oficial, con ajuste trimestral; infraestructura con costo por uso |
| Competir con un gigante o con el sistema propio de una ciudad grande | No competimos con el 147 de Rosario: nos integramos. El conector suma a Rosario como cliente de integración y de tablero, no de reemplazo |
| Solución a un problema inexistente | El MVP valida H1 a H5 antes de construir el motor completo, y la segunda mitad de la inversión se libera recién cuando el municipio piloto firma la suscripción (H4) |
| Conflictos entre cofundadores | Pacto de socios en la constitución de la SAS: un rol y una hipótesis del MVP por cofundador (punto 2.6), dedicación y salida. Las acciones de cada cofundador se consolidan de forma gradual en cuatro años, con un mínimo de uno (*vesting*): quien se va antes del primer año no conserva acciones, y quien se va a los dos años conserva la mitad |

### Marco legal

- **Ley 27.349 (Ley de Emprendedores)**: constitución como Sociedad por Acciones Simplificada (SAS).
- **Ley 25.326 (Protección de Datos Personales)**: los datos del vecino (contacto, ubicación exacta del domicilio) se tratan con consentimiento y nunca se publican; el conjunto de datos abierto se publica agregado y anonimizado.
- **Ley 27.275 (Acceso a la Información Pública)**: el tablero público ayuda al municipio a cumplir con la publicación proactiva de información.
- **Ley 27.506 (Economía del Conocimiento)**: la empresa desarrolla software, por lo que puede encuadrarse en el régimen de promoción.

### Trazabilidad con las etapas anteriores del TPI

<!-- cols: 14,86 -->

| Etapa | Qué toma Cuadra |
|---|---|
| Etapa 1 | El diagnóstico de Rosario como ciudad en transición, y su déficit de estrategia unificada y de financiamiento para escalar; el CIOR y la atención ciudadana como modelo de referencia |
| Etapa 2 | La lógica de priorización y escalamiento de incidentes de ITIL, aplicada al reclamo urbano: cada reclamo tiene prioridad, responsable y tiempo comprometido |
| Etapa 3 | La plataforma de órdenes de trabajo con app de campo para Personal: Cuadra generaliza esa solución a cualquier cuadrilla que trabaje en la vía pública. Personal, con su red de fibra y sus cuadrillas en el Gran Rosario, es el primer socio prestador que buscamos |

---

## 2. BUSINESS MODEL CANVAS Y FUENTES DE INGRESO

El Canvas completo, en la disposición de la plantilla de la cátedra, va como **Anexo I** en lámina independiente. A continuación se desarrolla cada bloque, en el orden que propone la cátedra: cliente, valor, operación y números.

### 2.1 Segmentos de clientes

**Plataforma múltiple:** Cuadra solo funciona si están los vecinos que reclaman, los municipios que resuelven y las prestadoras que reciben su parte. En cada segmento se separan los roles de quien paga, quien usa y quien decide.

<!-- cols: 24,19,19,38 -->

| Segmento | Paga | Usa | Decide / influye |
|---|---|---|---|
| **Municipios medianos** (cliente principal) | Municipio | Agentes de atención y cuadrillas municipales | Decide: secretaría de gobierno o de modernización. Influyen: Concejo Deliberante y vecinales |
| **Prestadoras de servicios en la vía pública** (distribuidora eléctrica, agua, gas, telecomunicaciones y cable) | Prestadora | Sus cuadrillas y su área de atención | Decide: gerencia de operaciones. Influye: el organismo regulador del servicio |
| **Vecinos** | No pagan | Reportan y siguen su reclamo | Recomiendan: vecinales y redes barriales. Pueden sabotear si el sistema no responde |
| **Planificadores y analistas** (consultoras, universidades, áreas de obras públicas) | Pagan por informes a medida | Usan el conjunto de datos abierto y los informes | Decide: el área que contrata el estudio |

**Arquetipo del cliente que decide:** *Laura, 42 años, secretaria de gobierno de un municipio del Gran Rosario.* Recibe los reclamos por teléfono, redes y mensajería, y tiene que derivar a la distribuidora eléctrica los que no son del municipio. No puede responder cuánto tarda su gestión en arreglar una luminaria. Influyen en ella el intendente, que necesita mostrar gestión, y el Concejo, que le pide informes.

### 2.2 Propuesta de valor

La propuesta de valor no es "una app de reclamos". Es lo que cada segmento gana:

<!-- cols: 24,76 -->

| Segmento | Propuesta de valor |
|---|---|
| Municipio | **Saber y mostrar cuánto tarda en resolver cada reclamo**, sin desarrollar ni operar un sistema propio. Elimina las derivaciones manuales a las prestadoras y los reclamos repetidos. Tipo de valor: reducción de costos, desempeño y accesibilidad, porque lleva a un municipio mediano lo que hoy solo tiene una ciudad grande |
| Prestadora | **Recibir solo los reclamos que son suyos**, con foto y ubicación exacta, y cerrarlos con evidencia. Menos salidas en falso de las cuadrillas. Tipo de valor: reducción de costos y de riesgo regulatorio, porque el cierre documentado sirve ante el ente regulador |
| Vecino | **Reclamar una sola vez, en un solo lugar, y ver quién lo tiene y cuándo se resuelve.** Tipo de valor: conveniencia y usabilidad |
| Planificadores | Datos georreferenciados y confiables de problemas urbanos, con historia. Tipo de valor: novedad, porque hoy esos datos no existen consolidados |

### 2.3 Canales

<!-- cols: 18,41,41 -->

| Fase | Municipios y prestadoras | Vecinos |
|---|---|---|
| Información | Venta directa del equipo; presentaciones en el Polo Tecnológico Rosario, el Clúster TIC Santa Fe y encuentros de municipios; casos publicados del piloto | Comunicación del propio municipio; QR en luminarias, contenedores y paradas; vecinales |
| Evaluación | Piloto de 90 días con tablero de resultados | Uso inmediato sin instalar nada |
| Compra | Contratación directa o convenio con el municipio; contrato comercial con la prestadora | No aplica: es gratuito |
| Entrega | Plataforma en la nube; implementación y capacitación en el lugar | Aplicación web y tiendas de aplicaciones |
| Posventa | Referente de cuenta, reunión trimestral de resultados, mesa de ayuda | Notificación de cierre y calificación del trabajo |

Todos los canales son **propios**. La excepción es el acceso a las prestadoras, que en parte llega **por medio de socios**: el municipio cliente es el que invita a las prestadoras que operan en su territorio.

### 2.4 Relación con clientes

<!-- cols: 16,84 -->

| Etapa | Cómo |
|---|---|
| Obtener | Municipios: asistencia personal dedicada, con un piloto como puerta de entrada. Vecinos: autoservicio, captados por la comunicación del municipio y el QR en la calle |
| Mantener | Municipios y prestadoras: referente de cuenta, informe trimestral de resultados y **cocreación** en una mesa de usuarios que prioriza nuevas funciones. Vecinos: servicio automatizado con notificaciones, y **comunidad** a través de las vecinales |
| Incrementar | Venta cruzada: invitar a las prestadoras del territorio, módulo de informes, conector con sistemas existentes. Venta de una versión mejor: pasar de tramo cuando el municipio suma áreas o cuadrillas. Referidos: cada municipio cliente es el caso de éxito que abre el siguiente |

### 2.5 Fuentes de ingreso

Cada segmento que paga tiene su fuente de ingreso. **No usamos publicidad**: en un servicio público, un aviso al lado de un reclamo dañaría la confianza que es justamente el valor de la plataforma. El precio no sale del costo más un margen. Sale del valor percibido y de lo que cada segmento ahorra, y se diferencia por tamaño del cliente.

<!-- cols: 20,26,32,22 -->

| Fuente | Cómo se cobra | Precio *(supuesto a validar)* | Segmento |
|---|---|---|---|
| **Suscripción municipal** | Suscripción mensual por tramo de habitantes | Hasta 30.000 hab.: USD 600 · de 30.001 a 100.000: USD 1.200 · de 100.001 a 250.000: USD 2.200 · más grandes: integración a medida | Municipios |
| **Implementación** | Pago único al alta (carga de zonas y categorías, capacitación) | USD 2.500 | Municipios |
| **Licencia por cuadrilla** | Licencia mensual por cuadrilla activa en la app (mínimo 10) | USD 35 por cuadrilla | Prestadoras |
| **Datos e informes** | Informes a medida y acceso a la interfaz de datos de alto volumen. El tablero y el conjunto de datos abierto son gratuitos | USD 1.500 por informe · USD 400 por mes de acceso a la interfaz | Planificadores, prestadoras y municipios |

Los precios se fijan en dólares porque el principal costo, la infraestructura en la nube, se paga en dólares. Se cobran en pesos al tipo de cambio oficial, con ajuste trimestral.

**Proyección de ingresos.** Ingreso mensual recurrente al cierre de cada año:

<!-- cols: 34,22,22,22 -->

| Concepto | Año 1 | Año 2 | Año 3 |
|---|---|---|---|
| Municipios (cantidad y tramos) | 3 (2 de hasta 30.000, 1 de hasta 100.000) | 8 (4 · 3 · 1) | 14 (6 · 6 · 2) |
| Suscripción municipal | USD 2.400 | USD 8.200 | USD 15.200 |
| Prestadoras y cuadrillas | 1 · 30 cuadrillas | 2 · 120 cuadrillas | 4 · 280 cuadrillas |
| Licencias por cuadrilla | USD 1.050 | USD 4.200 | USD 9.800 |
| Acceso a la interfaz de datos | — | USD 400 | USD 800 |
| **Ingreso mensual recurrente** | **USD 3.450** | **USD 12.800** | **USD 25.800** |

**Cuánto aporta cada fuente** a los ingresos del año 3, a ritmo anual:

<!-- cols: 40,30,30 -->

| Fuente | Ingreso anual | Participación |
|---|---|---|
| Suscripción municipal (USD 15.200 × 12) | USD 182.400 | 54,2% |
| Licencias por cuadrilla (USD 9.800 × 12) | USD 117.600 | 34,9% |
| Datos e informes (8 informes + 2 accesos a la interfaz) | USD 21.600 | 6,4% |
| Implementación (6 municipios nuevos) | USD 15.000 | 4,5% |
| **Total** | **USD 336.600** | **100%** |

### 2.6 Recursos clave

<!-- cols: 20,80 -->

| Tipo | Recurso |
|---|---|
| Intelectuales | La plataforma de software (aplicaciones, motor de ruteo, conector); **la base de datos georreferenciada de reclamos y tiempos**, que crece con cada municipio y es la barrera de entrada; la marca y los casos de éxito |
| Humanos | Los cinco cofundadores, estudiantes avanzados de Ingeniería en Sistemas, con un frente y una hipótesis del MVP cada uno (tabla siguiente); a partir del año 2, un desarrollador, que se suma a tecnología, y una persona de implementación y soporte, que se suma a operaciones |
| Financieros | Ronda inicial de USD 70.000 por el 20% de la SAS, que valúa la empresa en USD 350.000 después de la inversión. Entra en dos tramos de USD 35.000: el segundo se libera cuando el municipio piloto firma la suscripción (H4). Se complementa con aportes no reembolsables de los programas de emprendedores (ver punto 3) |
| Físicos | Mínimos: notebooks y celulares de prueba. No hay hardware en la calle: el sensor es el celular del vecino y el de la cuadrilla |

**Equipo fundador.** Cada cofundador lleva un frente del negocio y responde por una de las hipótesis del MVP (punto 1), de modo que cada resultado del piloto tiene un responsable.

<!-- cols: 22,56,22 -->

| Rol | Responsabilidades | Hipótesis que lidera |
|---|---|---|
| Dirección y municipios | Venta institucional a los municipios, negociación del piloto y relación con el inversor y con los programas de emprendedores | H4 — el municipio paga |
| Prestadoras y alianzas | Venta a las prestadoras y licencias por cuadrilla; relación con Personal y con los socios del ecosistema. Sostiene el pivot previsto si H4 falla | H5 — las prestadoras aceptan los reclamos ruteados |
| Tecnología | Plataforma, app de cuadrilla y medición de tiempos, conectores, seguridad y protección de los datos personales. El motor de ruteo se construye recién cuando el piloto valida la demanda | H3 — la trazabilidad acorta los tiempos |
| Producto y datos | App del vecino, tablero público, conjunto de datos abiertos e informes | H1 — los vecinos usan el canal nuevo |
| Operaciones e implementación | Ruteo manual de los reclamos durante el piloto, alta de cada municipio nuevo, capacitación de las cuadrillas y mesa de ayuda | H2 — buena parte de los reclamos son repetidos |

### 2.7 Actividades clave

Categoría principal: **plataforma / red**. El negocio consiste en mantener la plataforma y la red de organizaciones que se conectan a través de ella.

- Operar y mantener la plataforma: disponibilidad, seguridad y protección de los datos personales.
- Desarrollar el producto: motor de ruteo, clasificación por imagen, conectores.
- Implementar y capacitar en cada municipio nuevo: zonas, categorías, áreas responsables y cuadrillas.
- Vender al sector público y a las prestadoras.
- Sumar prestadoras en cada territorio: es lo que hace crecer el valor de la red.
- Publicar los datos abiertos y elaborar los informes.

### 2.8 Socios clave

Cada socio aporta un recurso o hace una actividad que nosotros no hacemos.

<!-- cols: 30,44,26 -->

| Socio | Qué aporta | Motivación |
|---|---|---|
| Municipio piloto del Gran Rosario | El territorio y los reclamos reales para validar el MVP; el primer caso de éxito. Es un socio **evangelista** | Reducir riesgo e incertidumbre |
| Personal (Telecom Argentina) | Primera prestadora con cuadrillas propias en la zona y conectividad móvil para la app de campo. Es el puente con la Etapa 3 | Adquirir recursos |
| Proveedor de infraestructura en la nube | Cómputo, almacenamiento de fotos y servicios de mapas, con costo por uso | Optimización y economía de escala |
| Polo Tecnológico Rosario y BCR Innova | Aceleración, mentoría y contacto con inversores | Adquirir recursos |
| UTN FRRo | Talento para el equipo y validación técnica | Adquirir recursos |
| Vecinales | Difusión barrial y retroalimentación de los vecinos | Reducir riesgo: adopción |
| Programas de emprendedores de Rosario y de la provincia | Capacitación y aportes no reembolsables | Adquirir recursos financieros |

### 2.9 Estructura de costos

**Enfoque en costo**, con máxima automatización: el ruteo, las notificaciones y la publicación de datos son automáticos, y la infraestructura se contrata por uso. El único gasto con economía de escala fuerte es el desarrollo, que se reparte entre todos los clientes.

<!-- cols: 60,40 -->

| Costos fijos mensuales (año 1) | Monto *(supuesto)* |
|---|---|
| Retiro de los cinco cofundadores (5 × USD 800) | USD 4.000 |
| Infraestructura base en la nube (entornos, copias de seguridad, monitoreo) | USD 350 |
| Herramientas y licencias de desarrollo y diseño | USD 150 |
| Contador, sociedad y seguros | USD 250 |
| Actividad comercial: viajes a municipios, eventos, difusión | USD 450 |
| Puestos en un espacio de coworking | USD 300 |
| **Total de costos fijos** | **USD 5.500** |

<!-- cols: 60,40 -->

| Costos variables | Monto *(supuesto)* |
|---|---|
| Por municipio: nube incremental, notificaciones y mesa de ayuda | USD 180 por mes |
| Por cuadrilla: almacenamiento de fotos y notificaciones | USD 4 por mes |

**Punto de equilibrio.** Como hace la cátedra en su ejemplo, el retiro de los socios va dentro de los costos fijos. Para un municipio de hasta 100.000 habitantes:

Q = CF / (P − CVu) = 5.500 / (1.200 − 180) = 5.500 / 1.020 ≈ 5,4 → **6 municipios**

Con la mezcla de clientes proyectada, el margen de contribución al cierre del año 1 es de USD 2.790 por mes. Son USD 1.860 de los tres municipios y USD 930 de las 30 cuadrillas, la mitad de los costos fijos. **El equilibrio se alcanza durante el año 2.** Al cierre de ese año, el margen de contribución (USD 10.880 por mes) cubre los costos fijos aun después de sumar al equipo el desarrollador y la persona de soporte, unos USD 8.000 por mes en total. La brecha del primer año y medio es la que cubre la inversión que se pide en el punto 3.

<!-- pagebreak -->

## 3. RESUMEN DEL NEGOCIO PARA UN SOCIO INVERSIONISTA

### Cuadra — del reclamo a la cuadrilla, a la vista de todos

**El problema.** En las ciudades medianas, un bache, una luminaria apagada o un cable caído se reclaman por teléfono, redes o mensajería, a menudo a quien no corresponde. El mismo problema entra veinte veces y nadie sabe cuándo se resuelve. Rosario lo resolvió para su ámbito con el 147, pero los municipios del Gran Rosario no pueden costearlo, y ni en Rosario el reclamo llega a las prestadoras que trabajan en la calle.

**La solución.** Una plataforma en la nube: el vecino reclama con una foto y sigue su reclamo, un motor de ruteo lo envía al área municipal o a la prestadora que corresponde y agrupa los repetidos, la cuadrilla recibe la orden en el celular y cierra con foto, y un tablero público muestra cuánto tarda cada responsable, con datos abiertos.

**Por qué es interesante.** Llevamos como servicio el modelo de una ciudad grande a los municipios que no pueden construirlo, y nos integramos con el que ya existe. El diferencial es **cruzar organizaciones**: municipio y prestadoras en una misma red, que gana valor con cada cliente y acumula datos difíciles de copiar. Responde a la agenda de ciudad inteligente: transparencia, datos abiertos y planificación urbana.

**Clientes e ingresos.** Pagan los municipios, con una suscripción por tramo de habitantes (USD 600 a 2.200 por mes) y USD 2.500 de implementación, y las prestadoras, con una licencia de USD 35 por cuadrilla por mes; se suman informes de datos a medida. El vecino lo usa gratis y no hay publicidad. Vendemos de forma directa, con un piloto de 90 días como puerta de entrada, y el municipio invita a las prestadoras de su territorio. Con 14 municipios y 280 cuadrillas, el año 3 cierra en **USD 336.600**: 54% suscripciones, 35% licencias, 11% datos e implementación.

**Cómo se lleva a cabo.** Operamos con software, datos y personas, sin hardware en la calle: USD 5.500 de costos fijos por mes con el retiro de los socios, y equilibrio con unos seis municipios durante el año 2. Empezamos con un MVP de 90 días en un municipio piloto, con ruteo manual, para validar cinco hipótesis antes de automatizar, con el Polo Tecnológico Rosario, BCR Innova, la UTN FRRo y una prestadora local.

**El equipo.** Cinco cofundadores, estudiantes avanzados de Ingeniería en Sistemas de la UTN FRRo, que ya planificaron una plataforma de órdenes de trabajo con app de campo para una empresa de telecomunicaciones. Cada uno lleva un frente y una hipótesis del piloto: dirección y municipios, prestadoras y alianzas, tecnología, producto y datos, y operaciones. El pacto de socios consolida sus acciones en cuatro años.

**Qué pedimos.** **USD 70.000** para 18 meses: 60% producto y equipo, 25% piloto y venta, 15% reserva. A cambio, el **20% de la SAS** en dos desembolsos de USD 35.000 por el 10% cada uno: el primero financia el piloto y el segundo se libera cuando el municipio firma la suscripción, al mes 6. Si el piloto falla, el inversor arriesgó la mitad. Se suman aportes no reembolsables de programas públicos.
