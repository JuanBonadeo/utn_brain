# Administración de Sistemas de Información — Wiki

> Materia: **ASI** — 4º año, Ingeniería en Sistemas de Información, UTN FRRo.
> Cátedra: Esp. Lic. Fabiana María Riva. Plan 2023 (Ord. 1877).
> Comisión **403** — Grupo **310**.

## Índice

> Numeración **oficial de cátedra**, según el Programa Analítico (Plan 2023, versión 2022_11_27).
> La asignatura es **anual**, 6 hs cátedra semanales, 144 hs reloj.

1. Unidad 1 — Gobierno de TIC y Planeamiento Estratégico
2. Unidad 2 — Administración de Recursos en áreas de Sistemas de Información
3. Unidad 3 — Dirección de Talento y Capital Humano
4. Unidad 4 — Higiene y Seguridad Laboral
5. Unidad 5 — Administración de Recursos en Proyectos de Sistemas y Tecnologías de Información
6. Unidad 6 — Emprendedorismo
7. TP Integrador — Personal (Telecom) / Proceso de instalación de fibra óptica

## Desarrollo

### Unidad 1 — Gobierno de TIC y Planeamiento Estratégico

#### Conceptos clave

- **Gobierno de TI ≠ Gestión de TI.** Gobierno = EDM (Evaluar, Dirigir, Monitorizar), nivel estratégico, parte del gobierno corporativo. Gestión = APO, BAI, DSS, MEA, nivel táctico/operativo.
- **Tres niveles de la organización** y sus tres problemas: Institucional (problema organizacional, producto/mercado), Intermedio (problema administrativo, estructurar actividades), Operacional (problema de adecuación tecnológica).
- **Eficiencia** = medios, hacer correctamente las cosas. **Eficacia** = fines, hacer las cosas correctas.
- **Meta ≠ Objetivo.** La meta es la dirección; el objetivo es la meta hecha medible, con indicador, valor y plazo. Existen en dos planos: negocio y TI, y se encadenan en cascada (meta de negocio → objetivo de negocio → meta de TI → objetivo de TI).
- **Proceso crítico vs. clave vs. estratégico**, y su horizonte de impacto: crítico → corto plazo, clave → mediano, estratégico → largo.
- **Proceso**: entradas → actividades → salidas. Se modela en **BPMN**.
- **Ciudad inteligente**: marco usado por la cátedra para el TPI (dimensiones tipo Smart City Wheel de Boyd Cohen).

#### Desarrollo


---


##### Unidad 1 — Gobierno de TI y Planeamiento Estratégico

> Fuentes: Apunte "Planeamiento Estratégico (V1.1)" y PPT "Planeamiento Estratégico (V2.1)", Esp. Lic. Fabiana María Riva, UTN FRRo, ASI, Plan 2023 (Ord. 1877).
> Aviso sobre el material: varias láminas del PPT contienen **solo imágenes** (tablas de COBIT que no se extrajeron al convertir el PDF). Están señaladas abajo como *[figura no extraída]*. La lista de 40 objetivos COBIT, las metas empresariales, las metas de TI, el mapeo entre ambas, la tabla de tamaño de organización, el modelo de abastecimiento, la estrategia de adopción de TI, los riesgos/problemas relacionados con TI y el ejemplo de BSC **no están en el texto disponible**: son figuras. No se inventan acá.

---

###### 1. Encuadre de la unidad

**Contenidos mínimos s/Ordenanza 1877:** Plan Estratégico; Gobierno y gestión de Tecnología de la Información y la Comunicación.

**Objetivo s/Ordenanza:** aplicar técnicas y metodologías en la elaboración del plan estratégico en la selección y dirección de talento y capital humano, procesos y sistemas software, sistemas de computación y comunicación en áreas y proyectos de SI, considerando los riesgos y optimizando los recursos tecnológicos.

**Resultado de aprendizaje (Unidades 1 y 2):** diseñar un plan estratégico de TIC alineado a las metas y objetivos organizacionales.

**Capacidades asociadas:**

| # | Capacidad |
|---|---|
| 1 | Analizar sistémicamente una organización para reconocer sus **procesos críticos** y los recursos de SI, software y comunicación que los sustentan |
| 2 | Identificar **metas organizacionales** y **alinear objetivos de TI** a las mismas |
| 3 | Identificar los **riesgos** a los que están sometidos los activos de información en distintos contextos |
| 4 | Especificar **indicadores** de rendimiento y de riesgos |
| 5 | Asociar posibles soluciones de gestión de servicios de TI a partir de la situación analizada y de las debilidades/amenazas identificadas, optimizando los recursos existentes |
| 6 | Plantear **mecanismos de control** en el contexto identificado |

**Competencias específicas:** CE1.1 (especificar, proyectar y desarrollar SI), CE5.1 (dirigir y controlar implementación, operación y mantenimiento de SI, comunicación de datos, software, seguridad y calidad, para alcanzar los objetivos fijados por la organización).
**Competencias genéricas:** tecnológicas CG1–CG5; sociales, políticas y actitudinales CG6–CG10.

---

###### 2. Gobierno de TI vs. Gestión de TI

**Gobierno de TI** (IT Governance / Gobierno Corporativo de TI): conjunto de **procesos, estructuras organizativas y políticas** que garantizan que las TIC de una organización se utilicen de manera efectiva para lograr sus objetivos. **Es parte del Gobierno Corporativo.**

| Eje | Gobierno de TI | Gestión de TI |
|---|---|---|
| Foco | Dirección estratégica, políticas y procedimientos | Implementación y ejecución de lo que definió el Gobierno |
| Nivel | Estratégico / institucional | Táctico y operativo, día a día |
| Decisiones típicas | Inversión en tecnología, gestión del riesgo, cumplimiento normativo | Infraestructura, administración de sistemas, seguridad de la información, soporte técnico |
| Función | Supervisar y dirigir los recursos de TI para uso eficiente y eficaz | Gestión eficiente de recursos tecnológicos: garantizar seguridad (confidencialidad, disponibilidad, integridad) y rendimiento |
| Alineamiento | Asegurar que TI esté alineada con las necesidades de los **stakeholders** | Cumplir políticas y procedimientos establecidos |

Regla mnemotécnica del material: **Gobierno = EDM (Evaluar, Dirigir, Monitorizar). Gestión = APO, BAI, DSS, MEA.**

---

###### 3. La organización y sus procesos

**Organización:** forma de cooperación entre personas basada en relaciones de trabajo para producir bienes y servicios. Está constituida por **recursos humanos, materiales y financieros** que le permiten funcionar como un **sistema** y lograr sus objetivos dentro de la comunidad donde está ubicada.

**Ciclo continuo de operación** (esquema del apunte y del PPT): sobre un flujo de **Entradas / Insumos → Salidas / Resultados** se ejecutan cuatro actividades en ciclo:

```
        Planeamiento  →  Organización
             ↑                ↓
  Entradas/Insumos      Salidas/Resultados
             ↑                ↓
         Control     ←     Ejecución
```

Las cuatro funciones (planeamiento, organización, ejecución, control) **no son unidades separadas**: son elementos interdependientes que interactúan y ejercen influencias recíprocas.

**3.1 Niveles de la organización y los tres problemas**

| Problema | Definición | Nivel responsable | Qué produce ese nivel |
|---|---|---|---|
| **1. Organizacional** | Elección del dominio **producto / mercado** | **Institucional** | Objetivos, políticas y planes estratégicos |
| **2. Administrativo** | Estructuración de las **actividades internas**; converge en la racionalización y estabilización de las actividades | **Intermedio** | Normas y procedimientos, planes tácticos, presupuestos y programas |
| **3. De adecuación tecnológica** | Ejecución de operaciones y generación de productos/servicios; elección de la **tecnología apropiada**. Incluye crear un sistema que transforme en operaciones la solución dada al problema organizacional | **Operacional** (a partir de las decisiones de Institucional e Intermedio) | Normas y reglamentos, planes operacionales, procedimientos de control |

**Tabla nivel / objetivos / políticas / planes** (transcripción de la lámina):

| NIVEL | OBJETIVOS | POLÍTICAS | PLANES | OTROS |
|---|---|---|---|---|
| **INSTITUCIONAL** | Empresariales | Generales | Estratégicos | — |
| **INTERMEDIO** | — | Normas y procedimientos | Tácticos | Presupuesto y programa |
| **OPERACIONAL** | — | Normas y reglamentos | Operacionales | Procedimientos de control |

Entre los tres niveles hay **retroalimentación**, que es lo que habilita el ciclo de mejora.

> Disparador del PPT (para pensar los tres niveles en acción): qué tuvo que hacer una empresa de desarrollo de software en las primeras semanas de COVID-19.

**3.2 Horizonte temporal del planeamiento**

El material no da una tabla explícita de años, pero encadena horizonte con nivel y con tipo de plan:

| Nivel | Tipo de plan | Horizonte |
|---|---|---|
| Institucional | Estratégico | **Largo plazo** (la formulación de estrategias produce efectos "en un determinado horizonte temporal a largo plazo") |
| Intermedio | Táctico | Mediano plazo (inferencia por posición en la cascada; el apunte no lo enuncia) |
| Operacional | Operacional | Corto plazo / día a día (inferencia) |

Complemento del material sobre plazos, vía impacto de fallas de procesos: **estratégicos → largo plazo; clave → mediano plazo; críticos → corto plazo.**

**3.3 Eficiencia y eficacia**

**Eficiencia:** se orienta a la **mejor manera de hacer o ejecutar las tareas** (métodos) para que los recursos (personas, infraestructura, materias primas) se apliquen de la forma más racional posible. Se preocupa por los **medios**.
**Eficacia:** se preocupa por los **fines**: para qué se ejecutan las tareas, qué resultados traen, qué objetivos se consiguen.

| EFICIENCIA | EFICACIA |
|---|---|
| Énfasis en los **medios** | Énfasis en los **resultados** |
| Hacer **correctamente** las cosas | Hacer las **cosas correctas** |
| Resolver problemas | Alcanzar objetivos |
| Salvaguardar los recursos | — |
| Cumplir tareas y obligaciones | Obtener resultados |
| Entrenar a los subordinados | Proporcionar eficacia a los subordinados |
| Mantener las máquinas | Máquinas disponibles |

*(La fila "salvaguardar los recursos" viene sin par en la columna eficacia en el original.)*

**Relación eficiencia–eficacia (lámina 8 del PPT):** la **eficacia** recorre el eje Objetivos → Decisiones → Políticas → Planes (estratégicos, tácticos, operacionales); la **eficiencia** recorre el eje Planes → Normas y procedimientos → Acción → Resultados. Es decir: la eficacia domina la definición del qué (arriba de la cascada) y la eficiencia domina la ejecución del cómo (abajo). *(La lámina vino desarmada en la conversión; la lectura del encadenamiento es inferencia.)*

---

###### 4. Procesos de negocio

**Definición (la de la cátedra):** *proceso* es **cualquier fenómeno que presente cambio continuo en el tiempo, o cualquier operación que tenga cierta continuidad o secuencia**. En general, **una secuencia de actividades**.

Propiedades que remarca el apunte:
- Los acontecimientos y las relaciones entre ellos son **dinámicos**, en evolución y cambio constante.
- No es una situación inmóvil, estancada ni estática: es **móvil, continua y sin comienzo ni fin**, en una secuencia fija de eventos o actividades.
- Los elementos del proceso **interactúan**: cada uno afecta a los demás.

**Estructura entrada → transformación → salida:** el esquema de la organización lo presenta como **Entradas / Insumos** que, atravesando las actividades de planeamiento, organización, ejecución y control, producen **Salidas / Resultados**. El material **no desarrolla** una plantilla formal de proceso (proveedor, entradas, actividades, salidas, cliente, dueño, indicadores) — si el TP la exige, sale de otra fuente, no de este apunte.

**Encuadre normativo:** uno de los **principios de la Gestión de Calidad** es el **enfoque basado en procesos**; permite planificar los procesos y sus interacciones para mejorar el desempeño global y sostener iniciativas de desarrollo sostenible. Las **Normas ISO** son ejemplo de adopción de este enfoque.

**4.1 Clasificación de procesos (taxonomía completa de la cátedra)**

| Tipo | Definición | Impacto de una falla | Notas |
|---|---|---|---|
| **Estratégicos** | Destinados a **definir y controlar los objetivos** de la organización, sus políticas y estrategias. Generan o contienen los procesos necesarios para sostener a la organización a lo largo del tiempo | **Largo plazo** | **No pueden delegarse** |
| **De gestión** | **Miden la calidad** de las actividades e **identifican los puntos a ajustar** para mejorar los resultados. Coordinan los procesos operativos y de soporte | — | No aportan valor directo al cliente, pero son esenciales para aumentar la calidad de las rutinas empresariales |
| **Operativos** | **Generan valor** para la organización; contribuyen **de manera directa** con el producto o servicio para el cliente | — | Se subdividen en clave y críticos (ver abajo) |
| ↳ **Clave** | **Fundamentales para el modelo de negocio** | **Mediano plazo** | — |
| ↳ **Críticos** | **No pueden dejar de llevarse a cabo bajo ninguna circunstancia**; una falla genera una **disrupción importante** | **Corto plazo** | Deben estar **siempre bajo control**, deben **evaluarse sus riesgos** y **determinarse el impacto de su interrupción** |
| **De soporte** | Procesos de **apoyo a los operativos**: brindan los recursos necesarios para que la operación sea eficiente y eficaz | — | — |

> Aclaración del apunte: "hay mucha bibliografía disímil referida a la clasificación de los procesos" — esta es **la clasificación que fija la cátedra**, y es la que hay que usar. Ojo con la distinción **clave ≠ crítico**: clave es lo fundamental para el modelo de negocio (mediano plazo); crítico es lo que no puede interrumpirse jamás (corto plazo). La capacidad 1 del resultado de aprendizaje pide identificar **procesos críticos**.

**4.2 BPMN**

**No aparece en este material.** Ni el apunte ni el PPT de la Unidad 1 mencionan BPMN, notación de modelado, eventos, compuertas (gateways), pools, lanes, flujos de secuencia/mensaje ni artefactos. Los procesos se tratan conceptualmente (definición, clasificación, criticidad), no gráficamente. Si BPMN es requisito del TP Integrador, viene de otro archivo de cursado o de la consigna del TP: **pendiente de ingestar**.

---

###### 5. Buenas prácticas y normas de Gobierno y Gestión de TI

**5.1 ISO/IEC 38500 — Gobierno Corporativo de las TI**

Norma publicada en **2008**. Aplicable a **cualquier tipo y tamaño de empresa**. Da orientación general amplia sobre el **papel de la alta dirección** en el Gobierno Corporativo de TI. **No es certificable.**

**Propósito:** "fomentar el uso efectivo, eficiente y aceptable de las TI" en todas las organizaciones, para asegurar a los involucrados que pueden tener confianza en el Gobierno de TI de la organización, y proporcionar guías a los directivos para el uso adecuado de las TI.

**Objetivo principal del Gobierno de TI derivado de la norma:** asegurar que **la inversión en tecnología produzca valor** para la organización y contribuya a su **éxito a largo plazo**.

**Los seis principios (completos):**

| Principio | Contenido |
|---|---|
| **Estrategia** | Obtener la alineación de TI a las necesidades del negocio. TI, como área de apoyo, debe ser identificada como **facilitador estratégico** para el cumplimiento de los objetivos organizacionales |
| **Adquisición** | Las adquisiciones de TI se hacen por **razones válidas**, con análisis apropiado y continuo, decisiones claras y transparentes, y equilibrio adecuado entre **beneficios, oportunidades, costos y riesgos** |
| **Conformidad** | TI cumple **todas las legislaciones y normas aplicables**; políticas y prácticas claramente definidas, implementadas y exigidas |
| **Responsabilidad** | Establecer responsabilidades **claramente entendidas** para el área de TI |
| **Rendimiento** | Las TI están **dimensionadas** para dar soporte a la organización, con servicios de la calidad adecuada para las necesidades **actuales y futuras** |
| **Factor humano** | Políticas, prácticas y decisiones de TI demuestran **respeto al factor humano**, incluyendo necesidades actuales y emergentes de todo el personal involucrado |

**Modelo de tres actividades** (se relacionan con los principios):

| Actividad | Qué implica |
|---|---|
| **Evaluar** | El **uso actual y futuro** de las TI: revisar la situación actual y futura, si la dirección estratégica de TI está alineada con los objetivos de negocio, si se cumplen las responsabilidades establecidas y si se logran los resultados deseados |
| **Dirigir** | La **toma de decisiones estratégicas** de TI por parte de la dirección: definir objetivos, prioridades, asignar recursos, establecer políticas y procedimientos |
| **Monitorear** | Supervisar **continuamente** el desempeño de TI y el cumplimiento de las políticas y procesos establecidos por el Gobierno de TI |

**5.2 COBIT 2019 — Control Objectives for Information and Related Technology**

**Marco de trabajo (framework)** para el **gobierno y la gestión** de las TI empresariales, **dirigido a toda la empresa**. Promovido por **ISACA** (Information Systems Audit and Control Association) desde su **primera versión en 1996**; versión vigente **COBIT 2019**.

**Evolución del enfoque:** en las primeras versiones ISACA apuntaba a la **auditoría** de TI; hoy el alcance se amplió a **auditoría, control y gestión**. COBIT 2019 plantea una **clara diferenciación entre Sistema de Gobierno y Sistema de Gestión**.

**Los seis principios del Sistema de Gobierno (completos):**

| # | Principio | Contenido |
|---|---|---|
| **1** | **Creación de valor para los stakeholders** | Proporcionar valor a través de las TI, asegurando que los recursos de tecnología se usen para alcanzar los objetivos del negocio y satisfacer a los stakeholders. El valor **no es solo económico**: incluye intangibles como la percepción del stakeholder |
| **2** | **Enfoque holístico (integral) del Sistema de Gobierno** | El gobierno de TI se construye a partir de **componentes de distinto tipo que funcionan juntos de manera integrada** para lograr sus metas; implica estructuras y procesos para guiar y controlar cómo la organización usa sus recursos de TI |
| **3** | **Sistema de Gobierno dinámico** | Cada vez que cambian uno o más **factores de diseño** (p. ej., un cambio de estrategia o de tecnología), debe considerarse el **impacto** de esos cambios en el sistema de Gobierno |
| **4** | **Separación de responsabilidades** | Clara separación de responsabilidades entre **Gobierno** y **Gestión** de TI: evita conflictos de interés, asegura transparencia y rendición de cuentas |
| **5** | **Adaptarse a las necesidades de la organización** | El sistema de gobierno debe **personalizarse** según las necesidades de la empresa, usando **factores de diseño** como parámetros para personalizar y priorizar componentes |
| **6** | **Sistema de gobierno íntegro / para toda la empresa** | Cubrir la empresa **de principio a fin**, no solo la función de TI, sino **todo el procesamiento de tecnología e información** que la empresa pone en funcionamiento, independientemente de dónde se realice |

**Ecuación de valor (clave para el TP):**

```
VALOR = UTILIDAD + GARANTÍA – RIESGOS
```

Del lado positivo: **utilidad** y **garantía**. Del lado negativo: **riesgos, costos ocultos, calidad inferior**.

**Stakeholders según COBIT:**

| Internos | Externos |
|---|---|
| Dirección ejecutiva | Entidades reguladoras |
| Gerentes del negocio | Socios de negocio |
| Gerentes de TI | Proveedores de TI |

> **Las necesidades de las partes interesadas son el punto de partida para la definición de los Objetivos del Gobierno de TI.** Este es el arranque de toda la cascada.

**Estructura de objetivos y dominios: 40 objetivos en 5 dominios.**

| Sistema | Dominio | Sigla | Cantidad de objetivos | Qué hace |
|---|---|---|---|---|
| **Gobierno** | Evaluar, Dirigir y Monitorizar | **EDM** | **5** | El organismo de gobierno **evalúa** las opciones estratégicas, **direcciona** a la alta gerencia respecto de las opciones elegidas y **monitoriza** la consecución de la estrategia |
| **Gestión** | Alinear, Planificar y Organizar | **APO** | 35 (repartidos entre los cuatro dominios de gestión) | Planificar |
| **Gestión** | Construir, Adquirir e Implementar | **BAI** | ↑ | Construir |
| **Gestión** | Entregar, Dar servicio y soporte | **DSS** | ↑ | Operar |
| **Gestión** | Monitorizar, Evaluar y Valorar | **MEA** | ↑ | Monitorizar |

Cada objetivo (de gobierno o de gestión) se relaciona **siempre** a un **proceso** y a un **grupo de componentes** específicos. Se establecen **métricas** para medir la efectividad de las prácticas y el **nivel de capacidad** requerido para las actividades de los procesos.

*[figura no extraída: lámina "Los 40 Objetivos" — el listado completo de los 40 objetivos COBIT es una imagen y no está disponible en el texto convertido.]*

**Esquema Gobierno/Gestión (lámina 26 y apunte):**

```
        Necesidades del Negocio
                  ↓
   ┌──────── GOBIERNO ─────────┐
   │  Evaluar → Dirigir → Monitorizar (EDM)  │
   └───────────┬───────────────┘
               ↓        ↑ retroalimentación
   ┌──────── GESTIÓN ──────────┐
   │ Planificar → Construir → Operar → Monitorizar │
   │   (APO)       (BAI)       (DSS)      (MEA)    │
   └───────────────────────────┘
```

**Los siete componentes del Sistema de Gobierno (principio 2, enfoque holístico):**

| Componente | Definición |
|---|---|
| **Procesos** | Prácticas y actividades organizadas para lograr determinados objetivos y producir resultados que contribuyan a la consecución de la totalidad de los objetivos relacionados con las TI |
| **Estructuras organizativas** | Las **entidades clave de toma de decisiones** en una empresa |
| **Políticas y procedimientos** | Convierten el **comportamiento deseado** en orientación práctica para la gestión del día a día |
| **Flujo de información** | Toda la información producida y utilizada por la empresa que debe compartirse para el funcionamiento eficaz del sistema de gobierno |
| **Cultura, ética y comportamiento** | De los individuos y de la empresa, como **factor de éxito** de las actividades de gobierno y gestión |
| **Personas, habilidades y competencias** | Necesarias para tomar buenas decisiones, ejecutar acciones correctivas y completar satisfactoriamente todas las actividades |
| **Servicios, infraestructura y aplicaciones** | Dan soporte al sistema de Gobierno de TI |

**Ciclo de la información en COBIT:** los **procesos generan y procesan datos**; estos se transforman en **información** y en **conocimiento**, que **crea valor** a la organización. El apunte remarca que es fundamental **automatizar e implementar los metadatos** en la gestión documental y de contenidos, desde una visión holística que integre el ciclo de vida del dato, de la información y del conocimiento en el ciclo de vida del desarrollo de aplicaciones basadas en **procesos como servicio**.

```
datos → información → conocimiento → VALOR
```

> **ITIL no aparece** en este material. Las normas y marcos efectivamente citados son: **ISO/IEC 38500** (gobierno corporativo de TI), **COBIT 2019** (marco de gobierno y gestión, base del PETI y del análisis organizacional), **normas ISO de calidad** (mencionadas como ejemplo del enfoque basado en procesos) y **Balanced Scorecard** de Kaplan y Norton (para estructurar objetivos empresariales). El apunte también apela a "seguridad de la información" con la tríada **confidencialidad, disponibilidad, integridad** sin citar ISO 27001 explícitamente.

---

###### 6. Diseño del Sistema de Gobierno de TI

**6.1 Responsabilidades**

El diseño del Sistema de Gobierno de TI es **responsabilidad del nivel institucional** de la organización, porque —tal como lo definen ISO 38500 y COBIT— **el Gobierno de TI es parte componente del Gobierno Corporativo**.

Acá se hace presente la **separación de responsabilidades**: el Sistema de Gobierno de TI se encarga de **evaluar, dirigir y monitorizar (EDM)**.

**Los 5 objetivos del dominio EDM ("Asegurar…"):**

| # | Objetivo EDM |
|---|---|
| 1 | Asegurar el **establecimiento y mantenimiento del Marco de Gobierno** |
| 2 | Asegurar la **Obtención de Beneficios** |
| 3 | Asegurar la **Optimización del Riesgo** |
| 4 | Asegurar la **Optimización de los Recursos** |
| 5 | Asegurar el **compromiso de las partes interesadas** |

Independientemente del tamaño de la organización y del rol dado a las TI, **los procesos de gobierno del dominio EDM son parte del Gobierno Corporativo** (no se tercerizan).
En cambio, la organización **sí puede decidir** si los dominios del Sistema de **Gestión** de TI serán estructuras organizativas internas o **tercerizadas**. En caso de tercerizar, **los procesos de monitorización dependerán de la información provista por terceros** (consecuencia que el apunte marca explícitamente).

**6.2 Estrategia organizacional**

**Definición:** la estrategia organizacional es el **proceso mediante el cual las organizaciones evalúan su situación, su nivel de competitividad, su visión, misión y valores, hacia el logro de sus objetivos**.

Racional: al acelerarse los cambios en el ambiente se origina una presión creciente que exige (a) **capacidad de anticiparse** a esos cambios y aprovechar de inmediato las nuevas oportunidades, y (b) **flexibilidad** para contrarrestar amenazas y presiones ambientales.

**Arquetipos de estrategia según COBIT (tabla completa):**

| Arquetipo de la estrategia | La organización se centra en: |
|---|---|
| **Crecimiento / Adquisición** | Crecimiento (ingresos) |
| **Innovación / Diferenciación** | Ofrecer productos y servicios diferentes y/o innovadores |
| **Liderazgo en costos** | Minimizar costos a corto plazo |
| **Servicio al cliente / Estabilidad** | Proporcionar servicio estable y orientado al cliente |

**6.3 Misión, visión y valores**

| Elemento | Definición (textual del apunte) | Forma | Permanencia |
|---|---|---|---|
| **Misión** | Formulación del **propósito para el cual existe** la organización | Generalmente **una sola frase** | Carácter bastante duradero; puede mejorarse o modificarse cuando el "concepto" de la organización lo requiere |
| **Visión** (o "visión de futuro") | Formulación de la **situación futura deseable** para la organización | Una o varias frases, redactadas de manera **atractiva y motivadora** | Carácter duradero, pero suele **actualizarse regularmente** o redefinirse cuando cambian las circunstancias estratégicas |
| **Valores** (corporativos, empresariales u organizacionales) | Las **creencias (el credo)** acerca de las conductas consideradas **correctas y valiosas** por la organización | Lista de creencias | **Mayor permanencia de los tres.** No son declaración circunstancial ni de conveniencia: son creencias básicas, esenciales, con valor intrínseco |

**Para qué sirven en el análisis (lo que dice el material, no relleno):**
- La **visión**, al ser una situación futura deseable, es **una especie de gran objetivo a lograr**: por eso es **la inspiración y el marco para definir objetivos y metas más específicas**. Es el nexo entre "quiénes somos" y la cascada de objetivos.
- Para transmitir la visión, la organización redacta una **declaración de la misión** que contiene una **breve y clara descripción de los valores en los que cree y de los objetivos**.
- La **misión** define el **primer nivel jerárquico de objetivo** (ver 6.4).
- El **primer principio para definir objetivos** es que estén **alineados con visión, misión y valores** — o sea, misión/visión/valores son el **criterio de validación** de todo objetivo que se proponga en el TP.

**Ejemplos del PPT** (útiles para calibrar redacción):

| Tipo | Organización | Enunciado |
|---|---|---|
| Visión | IKEA | Crear un mejor día a día para la mayoría de las personas |
| Visión | Microsoft | Una computadora en cada escritorio y en cada hogar |
| Visión | Google | Organizar la información del mundo y hacer que sea útil y accesible para todos |
| Visión | LinkedIn | Conectar a profesionales de todo el mundo para ayudarles a ser más productivos y a alcanzar todas sus metas laborales |
| Visión | Caterpillar | Un mundo en el cual las necesidades básicas de las personas se satisfacen de manera ambientalmente sostenible |
| Visión | Harvard | Educar a los ciudadanos y líderes para nuestra sociedad |
| Misión | McDonald's | Ser el lugar y la forma de comer preferidos de nuestros clientes |
| Misión | Sony | Llenar el mundo con emoción a través del poder de la creatividad y la tecnología |
| Misión | Amazon | Ser la empresa más centrada en el consumidor del mundo, donde los consumidores puedan encontrar cualquier cosa que quieran comprar en línea |
| Misión | Avon | Ser la compañía que mejor entienda y satisfaga las necesidades de productos, servicio y autoestima de la mujer en todo el mundo |
| Misión | Toyota | Ofrecer la mejor experiencia de compra y de servicio superando las expectativas de los clientes |

**Valores — ejemplos:**

| Coca-Cola | Sony |
|---|---|
| **Integridad:** ser auténticos | **Sueños y curiosidad:** sé pionero del futuro con sueños y curiosidad |
| **Calidad:** lo que hacemos, lo hacemos bien | **Diversidad:** crear lo mejor aprovechando la diversidad y los distintos puntos de vista |
| **Responsabilidad:** que suceda depende de uno mismo | **Integridad y sinceridad:** ganarse la confianza de la marca a través de conducta ética y responsable |
| **Liderazgo:** el coraje de forjar un futuro mejor | **Sostenibilidad:** cumplir con las responsabilidades de las partes interesadas mediante prácticas comerciales disciplinadas |
| **Colaboración:** potenciar el talento colectivo | |
| **Pasión:** comprometidos con el corazón y con la razón | |

**Ejemplo completo resuelto por la cátedra — Empresa de Desarrollo de Software** (sirve de molde directo para el TP):
- **Misión:** dotar a las PYMES y profesionales de herramientas para mejorar e impulsar su gestión empresarial. Ofrecer productos que destaquen por su facilidad de uso, potencia y capacidad de adaptación a múltiples actividades y entornos operativos.
- **Visión:** ser líder de desarrollo de la región, certificada en calidad.
- **Valores:** eficacia (rapidez y dinamismo, adaptación al entorno), escucha (necesidades del cliente, comunicación bidireccional), innovación (mejoras y actualización constante de conocimientos), servicio (soluciones que aumenten la satisfacción del cliente), trabajo en equipo (clima de confianza y respeto mutuo), rigor (calidad y ética profesional), transparencia (información continua, veraz y accesible).

> Actividad del PPT: definir misión, visión y valores para (a) una universidad, (b) una empresa de desarrollo de software, (c) una ONG ambientalista.

**6.4 Objetivos estratégicos: META vs. OBJETIVO**

**Definición base:** *"Un **objetivo** constituye la **expresión de un propósito a obtener**."*

Los objetivos estratégicos son **una de las categorías fundamentales de la actividad de dirección**, porque **condicionan las actuaciones** de la organización y en especial de sus dirigentes. Pregunta clave que los dispara, una vez conocida la razón de ser: **¿qué es imprescindible para cumplir con su objeto social?**

**Jerarquía de objetivos (dos niveles explícitos en el apunte):**

| Nivel | Qué es | Alcance |
|---|---|---|
| **1º nivel** | La **misión** de la organización | La expresión **más general** de su razón de ser en cuanto a su papel económico y social |
| **2º nivel** | Los **objetivos generales** | Expresan los **propósitos o metas a escala global y a largo plazo**, en función de la situación del entorno y sobre todo de su **evolución futura (visión)**, en especial de las oportunidades y amenazas, y de la situación interna de la organización |

**META vs. OBJETIVO — cómo lo usa la cátedra.** El material **no da una definición contrastiva formal** de meta versus objetivo (dato importante para no inventar en el parcial). Lo que sí hace es **usarlos de manera consistente** en la actividad SMART y en el mapeo COBIT:

| | **META** | **OBJETIVO** |
|---|---|---|
| Qué expresa | El **propósito general / la dirección** a alcanzar | La **expresión concreta de un propósito a obtener** |
| Grado de precisión | Amplia, cualitativa, sin métrica ni plazo | Específica, medible, con responsable y fecha |
| Ejemplo de la cátedra | "Mejorar la presencia de marca de la empresa en las redes sociales" | "Publicar todos los días hábiles en Instagram durante el primer semestre del año fiscal 2025, asegurando que cada publicación combine hashtags propios y populares del sector, para generar 1000 seguidores nuevos en Instagram para el 30 de junio" |
| Relación | La meta **contiene** al objetivo | El objetivo **operacionaliza** la meta aplicando SMART |
| En COBIT | Metas empresariales / metas de TI (catálogo genérico del framework) | Objetivos específicos que la organización deriva de cada meta |

**Consigna literal de la actividad del PPT que fija el criterio:** *"Definir un **objetivo**, siguiendo la metodología SMART, que cumpla con la siguiente **META**: mejorar la presencia de marca de la empresa en las redes sociales."*
→ **Meta = enunciado amplio de entrada. Objetivo = salida SMART.** Esa es la operación que hay que saber hacer.

**Definiciones de apoyo:**

| Concepto | Definición |
|---|---|
| **Factores clave de éxito** | Qué necesidad espera satisfacer la organización, el público al que se dirige, qué valora y qué no valora. Varían según la industria. Los más comunes: **innovación, calidad del producto, gestión eficiente, satisfacción del cliente, adaptabilidad al mercado** |
| **Áreas de resultados clave** | Los **departamentos o grupos** de la organización primordialmente **responsables** de que ésta pueda lograr un factor clave de éxito determinado. Dependen del factor clave que se busque. Incluyen las funciones cruciales para el logro de los objetivos y **establecen dónde se asignan los recursos y esfuerzos** que tendrán mayor impacto sobre los resultados |

> Metáfora del PPT (Alicia y el Gato de Cheshire): *"—¿Qué camino he de tomar? —Depende mucho del punto adonde quieras ir. —Me da casi igual adónde. —Entonces no importa qué camino sigas."* Sin objetivo definido, cualquier estrategia de TI es indistinguible de cualquier otra.

**6.5 Criterios de definición de objetivos**

**Principios fundamentales que rigen la previsión y el planeamiento de los objetivos (los 5 de la cátedra, completos):**

| Principio | Contenido |
|---|---|
| **Alineados** | Con la **visión, misión y valores** |
| **Enfocados** | En los **factores clave de éxito** |
| **Precisos** | **Específicos**, definidos en forma clara para ser entendidos por **todos los implicados** |
| **Factibles** | **Decisivos, retadores y realizables**: que todos los esfuerzos se orienten hacia ellos, pero posibles de alcanzar. Los objetivos que constituyen un **desafío de moderada dificultad** conducen a **mayor rendimiento** que los percibidos como demasiado difíciles |
| **Verificables** | **Medibles** para poder ser evaluados. Cuando no puedan cuantificarse, deben **definirse los criterios** para evaluar su logro. Debe establecerse además un **límite de tiempo** en que se pueda obtener la medida de su logro |

**Metodología SMART** (la que usa la cátedra operativamente en la actividad; el PPT la presenta con las cinco preguntas):

| Letra | Criterio | Pregunta guía |
|---|---|---|
| **S** | **Específico** | ¿Tu objetivo define **exactamente** lo que querés hacer? |
| **M** | **Medible** | ¿Ya estableciste **cómo medirás** tu objetivo una vez que se complete el proyecto? |
| **A** | **Alcanzable** | ¿Tu objetivo es algo que **podés lograr**, considerando las posibilidades de tu proyecto? |
| **R** | **Realista** | ¿Puede el equipo del proyecto alcanzarlo de manera razonable **con los recursos** de que dispone? |
| **T** | **De duración limitada** (time-bound) | ¿**Cuándo** lo vas a lograr? Aclarar la **fecha prevista** en el objetivo |

**Construcción incremental del ejemplo resuelto** (así se toma en la actividad — cada paso agrega una letra):

| Paso | Enunciado resultante |
|---|---|
| Meta | Mejorar la presencia de marca de la empresa en las redes sociales |
| **+ S** | Mejorar la marca de nuestra empresa **en Instagram** con **hashtags propios** de la empresa |
| **+ M** | Desarrollar hashtags propios para generar **1000 seguidores nuevos** en Instagram |
| **+ A** | Desarrollar y usar hashtags propios, **junto con hashtags populares del sector**, para generar 1000 seguidores nuevos en Instagram |
| **+ R** | **Publicar una vez al día** en Instagram y asegurarse de que cada publicación tenga una combinación de hashtags propios y populares del sector, para generar 1000 seguidores nuevos |
| **+ T** | Publicar **todos los días hábiles** en Instagram **durante el primer semestre del año fiscal 2025**, asegurándose de que cada publicación combine hashtags propios y populares del sector, para generar 1000 seguidores nuevos en Instagram **para el 30 de junio** |

Nótese la correspondencia con los 5 principios del apunte: **Precisos ≈ S**, **Verificables ≈ M + T**, **Factibles ≈ A + R**, **Alineados** y **Enfocados** son los dos criterios adicionales que SMART **no** cubre y que la cátedra sí exige. (inferencia sobre la correspondencia; el material presenta ambas listas sin mapearlas)

**6.6 Factores que influyen en el cumplimiento de los objetivos**

| Factor | Contenido |
|---|---|
| **Participación de los involucrados** | Es **uno de los factores más importantes y determinante de la efectividad**. La participación de la mayor cantidad de involucrados en la **definición** redunda en **mayor compromiso**. Los objetivos desafiantes y realistas se asocian a mayor rendimiento **siempre y cuando sean decididos, o al menos aceptados, por quienes han de cumplirlos**. El establecimiento de objetivos **en grupo aumenta su aceptación** |
| **Cultura organizacional** | *"…la forma en que nosotros hacemos las cosas aquí…"*. Refiere a cómo se relacionan las personas dentro de la organización, cómo se toman e implementan las decisiones, la actitud de los empleados frente a su trabajo, clientes, proveedores, superiores y colegas. Depende de los estándares y valores de las personas: **no puede ser modificada, pero puede ser influenciada**. Influenciarla requiere **liderazgo en forma de políticas claras y consistentes de recursos humanos**. **Si la cultura otorga un valor bajo a la innovación, serán difíciles los cambios de TI en la organización** |
| **Política organizacional** | Es la **combinación de todas las decisiones y medidas tomadas para definir y realizar los objetivos**. En ellas la organización debe **priorizar objetivos y decidir cómo serán alcanzados**. Las prioridades **pueden cambiar con el tiempo** según las circunstancias. **Cuanto más claras sean las políticas, menor será la necesidad de explicitar cómo el personal realiza sus tareas**: en lugar de procedimientos detallados, el personal usa las políticas como guía → la organización se torna **más flexible** y responde más rápido a circunstancias cambiantes |

> Consecuencia directa para el TP: la cultura organizacional es un **factor de riesgo** para cualquier propuesta de implementación de solución de TI. Si la organización analizada valora poco la innovación, hay que preverlo en la gestión del cambio (punto 6 del PETI).

**6.7 Balanced Scorecard (BSC / Cuadro de Mando Integral)**

**Qué es:** metodología para **alinear la estrategia de las organizaciones con los indicadores de gestión**, creada en **1992 por Kaplan y Norton**. Ayuda en la **medición y monitoreo**, permitiendo que los tomadores de decisiones determinen el comportamiento de los puntos esenciales de la cadena de producción.

**Función:** permite **traducir una estrategia en objetivos relacionados**, mediante la medición de **indicadores agrupados en cuatro perspectivas**:

| # | Perspectiva |
|---|---|
| 1 | **Financiera** |
| 2 | **Cliente** |
| 3 | **Procesos internos** |
| 4 | **Crecimiento** (aprendizaje y crecimiento) |

**Vínculo con COBIT:** *"Los **Objetivos Empresariales** (u Organizacionales) apoyan a las **Estrategias Organizacionales** y se **estructuran en torno a las dimensiones del Balanced Scorecard**."* Es decir: **las metas empresariales del catálogo COBIT están clasificadas por perspectiva BSC.**

*[figura no extraída: lámina "BSC — Ejemplo" es una imagen.]*

**6.8 Alineamiento Negocio–TI: la cascada de metas**

Esta es la columna vertebral de la unidad. Reconstruida a partir de las piezas que da el material:

```
Necesidades de las partes interesadas (stakeholders)   ← punto de partida (COBIT, principio 1)
                 ↓
Misión / Visión / Valores                              ← 1er nivel de objetivo = misión
                 ↓
Estrategia organizacional  (arquetipo COBIT)
                 ↓
METAS EMPRESARIALES  (estructuradas por perspectivas BSC)
                 ↓
OBJETIVOS ESTRATÉGICOS DE NEGOCIO  (específicos, SMART)
                 ↓
METAS DE TI  (COBIT define, para cada dimensión de meta empresarial, las metas de TI que deben cumplirse)
                 ↓
OBJETIVOS ESPECÍFICOS DE TI
                 ↓
OBJETIVOS / PROCESOS COBIT (EDM, APO, BAI, DSS, MEA) + componentes + métricas
```

**Regla textual del apunte:** *"Cada objetivo planteado por la organización deberá ser **mapeado** con objetivos específicos de TI. COBIT plantea **para cada dimensión de meta empresarial las metas de TI que tendrán que cumplirse**, de las cuales se podrán identificar objetivos de TI específicos."*

**Diferencia exacta entre objetivo DE NEGOCIO y objetivo DE TI (tabla del PPT, lámina 44):**

| | **Objetivos DE NEGOCIO** | **Objetivos DE TECNOLOGÍA DE LA INFORMACIÓN (TI)** |
|---|---|---|
| **Función** | **Guían a la organización hacia el logro de sus metas a largo plazo** | **Están vinculados a la infraestructura tecnológica y a la gestión eficiente de la información** |
| **Aspectos típicos** | Crecimiento de los ingresos, expansión del mercado, mejora de la eficiencia operativa, maximización de la rentabilidad | Seguridad de la información, actualización de sistemas, optimización de procesos, implementación de nuevas tecnologías, soporte efectivo a las operaciones comerciales |
| **Ejemplo 1** | **Incrementar la cuota de mercado:** lograr un aumento del **15%** en la cuota de mercado en el segmento X durante el próximo año fiscal, mediante estrategias de penetración y expansión | **Mejorar la seguridad de la información:** implementar un sistema de seguridad que reduzca las vulnerabilidades y garantice la protección de datos confidenciales, reduciendo el riesgo de brechas de seguridad en un **30%** |
| **Ejemplo 2** | **Mejorar la experiencia del cliente:** aumentar la satisfacción del cliente en un **20%** mediante programas de retroalimentación, capacitación del personal y mejoras en los procesos de atención | **Actualizar la infraestructura tecnológica:** migrar a una nueva plataforma de servidor y actualizar el software empresarial para mejorar la eficiencia y la capacidad de respuesta del sistema en un **25%** |
| **Ejemplo 3** | **Optimizar la cadena de suministro:** reducir los costos operativos en un **10%** mediante tecnologías avanzadas de seguimiento y gestión en toda la cadena | **Optimizar procesos de negocio:** automatizar procesos clave como gestión de pedidos y facturación, para reducir tiempos de ciclo y mejorar la eficiencia operativa en un **15%** |

**Lectura del encadenamiento (lo que hay que poder defender):**
- El objetivo de negocio dice **qué resultado quiere el negocio** (cuota, satisfacción, costo). El objetivo de TI dice **qué capacidad tecnológica se construye** para habilitarlo (seguridad, plataforma, automatización).
- Cada objetivo de TI debe poder **rastrearse hacia arriba** hasta al menos un objetivo de negocio; si no, es inversión en tecnología sin creación de valor — exactamente lo que ISO 38500 (principio Estrategia) y COBIT (principio 1) prohíben.
- Ambos niveles se redactan **con la misma exigencia SMART** (nótense los porcentajes y plazos en los seis ejemplos de arriba).

*[figuras no extraídas: la tabla COBIT de **metas empresariales** y la de **mapeo metas empresariales → metas de TI** son imágenes en ambos archivos. Para el TP hay que conseguirlas del PDF original o del framework COBIT 2019.]*

---

###### 7. Planeamiento estratégico

**Definición operativa (PPT):** **determinar la posición futura de la empresa** frente a:

| # | Dimensión |
|---|---|
| 1 | Sus **productos y mercados** |
| 2 | Su **rentabilidad** |
| 3 | Su **tamaño** |
| 4 | Su **grado de innovación** |
| 5 | Sus **relaciones** con sus ejecutivos, empleados e instituciones externas |

**Encuadre (apunte):** una vez establecidos los lineamientos básicos de la estrategia empresarial, la organización debe **tomar decisiones estratégicas**; esto le permite **equilibrar la posición estratégica que adoptará en el futuro**. Se usan las **tres actividades básicas que configuran el análisis FODA**.

**7.1 Las tres actividades básicas**

| # | Actividad | Contenido |
|---|---|---|
| **1** | **Análisis organizacional** | Análisis de **condiciones actuales y futuras** de la organización, **recursos disponibles y necesarios**, potencialidades, **fortalezas y debilidades**, estructura organizacional, capacidad y competencia → produce **F** y **D** |
| **2** | **Análisis ambiental** | Análisis de las **condiciones y variables ambientales**, sus perspectivas actuales y futuras, las **coacciones, contingencias, desafíos y oportunidades** percibidos en el contexto ambiental → produce **O** y **A** |
| **3** | **Formulación de estrategias** | **Toma de decisiones globales y amplias** que producirán efectos en el futuro de la organización, en un determinado **horizonte temporal a largo plazo** |

> El apunte las enumera en el orden ambiental → organizacional → formulación; el PPT en el orden organizacional → ambiental → formulación. **No hay contradicción de contenido, solo de orden de presentación.**

**Esquema del proceso completo (reconstruido del diagrama de ambos archivos):**

```
ANÁLISIS AMBIENTAL
Verificación de factores ambientales:
  Mercados · Competencia · Tecnología · Economía · Gobierno · Legislación
        ↓ (aspectos considerados por la cúpula de la administración)
  Oportunidades y Amenazas GENERALES
        ↓
  Oportunidades y Amenazas ESPECÍFICAS de la empresa
        ↓
  Formulación de alternativas de estrategia → Evaluación de alternativas → DECISIONES ESTRATÉGICAS
        ↑
ANÁLISIS ORGANIZACIONAL
  Análisis de fortalezas y debilidades operacionales y de recursos disponibles
        ↓
  Definición de las posibilidades y de los recursos necesarios
```

**7.2 Análisis organizacional**

**Cuatro factores a establecer inicialmente** (COBIT plantea las posibilidades para cada uno):

| # | Factor a determinar |
|---|---|
| 1 | **Tamaño de la organización** |
| 2 | **Rol que tienen las tecnologías de la información** |
| 3 | **Modelo de abastecimiento** |
| 4 | **Estrategia de adopción de la tecnología** |

*[figuras no extraídas: las cuatro tablas COBIT con las opciones concretas de tamaño, rol de TI, modelo de abastecimiento y estrategia de adopción son imágenes en el PPT (láminas 55–58) y en el apunte (pág. 15). **No se puede transcribir la taxonomía porque no está en el texto convertido.** Es material necesario para el TP.]*

> El PPT ilustra el caso "TI considerada como **Soporte**" con la serie *The IT Crowd*.

**Fortalezas y debilidades (o vulnerabilidades, como se las llama en contexto de TI):** se analizan usando el concepto de creación de valor de COBIT — **valor = utilidad + garantía – riesgos** — y para eso es de utilidad la determinación del **inventario de activos**.

**Categorías de activos (taxonomía completa del apunte; el listado no es exhaustivo porque varía con los avances tecnológicos):**

| Categoría | Definición | Ejemplos |
|---|---|---|
| **Activos de información** | En el contexto de seguridad de la información son los **activos críticos**, a partir de los cuales se identifican las demás categorías | Documentación del sistema, manuales de usuario, material de formación, procedimientos operativos o de soporte, planes de continuidad, documentación específica generada por los procesos, documentación histórica archivada, claves de acceso a aplicaciones o instalaciones |
| **Activos de soporte a los activos de información** (*"contenedores"*) | Los medios que contienen a los activos de información | **Soporte físico:** papel, carpetas, biblioratos. **Soporte electrónico:** bases de datos, documentos digitalizados, correos electrónicos, archivos en la nube; y los medios de almacenamiento en sí: discos internos y externos, dispositivos USB, CD, DVD |
| **Software** | — | Software de base (sistemas operativos, gestores de bases de datos), herramientas de desarrollo, ofimática, software de aplicación |
| **Hardware** | — | Equipos de procesamiento (servidores, procesadores, monitores, portátiles), equipos de comunicaciones (módems, routers, centrales digitales, equipos de telecomunicaciones) |
| **Equipamiento** | Otro hardware auxiliar y soporte físico del ambiente | UPS, impresoras, scanners, equipos de climatización, mobiliario |
| **Instalaciones** | Donde se desarrollan los procesos y se alojan los activos anteriores | Oficinas, galpones |
| **Servicios** | Servicios prestados por la organización a partir de sus procesos, **o** servicios de los que **depende un proceso** para su prestación (**interesan estos últimos**, en relación con los activos de información identificados) | Internos: mantenimiento de una intranet por el depto. de sistemas, limpieza. Externos contratados: correo postal, seguridad privada, hosting, internet. Públicos: energía eléctrica. Provisión de insumos: papel para impresoras, tóner, combustible |
| **Personas** | Empleados y terceros que **explotan u operan** todos los elementos anteriores | Interesan sus **competencias** |
| **Otros activos** | — | Imagen de la organización, objetivos, credibilidad. **Muchas metodologías no los consideran en la identificación, sino como factores para medir el impacto de las amenazas sobre el resto de los activos** |

*[figuras no extraídas: las listas COBIT de **riesgos relacionados con TI** y de **problemas relacionados con TI** son imágenes (apunte pág. 17, PPT láminas 60–61). No están disponibles en texto.]*

**7.3 Análisis ambiental**

Objetivo: establecer las **oportunidades y amenazas** que genera el **ambiente externo**. Se puede recurrir al inventario de activos ya identificado y además analizar (**taxonomía completa — es un PESTEL**):

| Dimensión | Qué analizar |
|---|---|
| **Política** | Políticas gubernamentales locales, estatales y federales; normas comerciales; reglamentos fiscales |
| **Economía** | Tasas de desempleo, tasas de crecimiento económico, tipos de cambio, inflación, tipos de interés |
| **Aspectos sociales** | Tendencias demográficas, patrones de compra de los consumidores, distribución de la riqueza, actitudes y opiniones, reconocimiento de marcas |
| **Cuestiones tecnológicas** | Nuevos descubrimientos y productos tecnológicos, áreas de investigación y desarrollo, incentivos para la tecnología |
| **Normativas y legislación** | Normativas de salud y seguridad, leyes de empleo, normativas de productos, aranceles |
| **Medio ambiente** | Condiciones climáticas y meteorológicas, normas de consumo energético, políticas medioambientales |

*(El material no lo nombra "PESTEL", pero las seis dimensiones coinciden exactamente con ese marco — inferencia.)*

Factores ambientales que enumera el diagrama: **mercados, competencia, tecnología, economía, gobierno, legislación**, considerados por la **cúpula de la administración**.

**7.4 Formulación de estrategias (matriz FODA cruzada)**

| Estrategia | Combinación | Lógica |
|---|---|---|
| **FO** | Fortalezas + Oportunidades | Usar fortalezas para capitalizar oportunidades |
| **DO** | Debilidades + Oportunidades | — |
| **FA** | Fortalezas + Amenazas | — |
| **DA** | Debilidades + Amenazas | — |

**Regla de combinación (textual):** las combinaciones pueden darse **entre una fortaleza y una oportunidad**, **entre una fortaleza y varias oportunidades**, o **entre varias fortalezas y una oportunidad**. La misma lógica aplica a DO, FA y DA. *(El apunte solo explicita las definiciones de la lógica FO; para DO/FA/DA dice "con la misma lógica".)*

> Actividades del PPT: FODA de una fábrica de alfajores artesanales de la costa argentina. La solución de ejemplo lista, entre otros: **fortalezas** — buen trato al cliente, personal adecuado, buen producto, aceptación de los consumidores, sólida organización empresarial, efectividad del servicio; **debilidades** — cantidad limitada de personal, empresa joven con poca experiencia en el mercado, poca publicidad, empresas de complementos cercanos; **oportunidades** — producto de alto consumo, venta de productos complementarios, pocas empresas del rubro, crecimiento del mercado; **amenazas** — mayor crecimiento de marketing en el mercado, aumento del costo de la materia prima, aparición de empresas del rubro. *(La lámina vino con los cuatro cuadrantes desarmados en la conversión; la asignación de cada ítem a su cuadrante es reconstrucción — inferencia.)*

---

###### 8. PETI — Plan Estratégico de Tecnologías de la Información

**Estructura del PETI usando el marco de trabajo de COBIT (10 puntos, completa):**

| # | Sección | Contenido |
|---|---|---|
| **1** | **Introducción y contexto** | 1.1 Descripción de la organización, su misión, visión y objetivos estratégicos. 1.2 Breve explicación sobre la importancia del Gobierno y Gestión de TI en el logro de los objetivos organizacionales |
| **2** | **Análisis del entorno de TI** | 2.1 Evaluación del entorno tecnológico **interno y externo**. 2.2 Análisis de **tendencias y cambios** en la industria de TI que podrían afectar a la organización. 2.3 Identificación de **riesgos y oportunidades** asociadas con la TI |
| **3** | **Objetivos estratégicos de TI** | 3.1 Definición de objetivos estratégicos específicos de TI **que apoyen los objetivos generales de la organización**. 3.2 **Priorización** en función de su **impacto y urgencia** |
| **4** | **Alcance y enfoque del plan** | 4.1 Descripción de los **procesos que serán priorizados**. 4.2 Identificación de las **áreas de gobierno y gestión de TI** que se abordarán |
| **5** | **Estrategias y acciones para la implementación de procesos** | 5.1 Desarrollo de estrategias y acciones específicas para implementar los procesos seleccionados. 5.2 **Asignación de recursos y responsabilidades** |
| **6** | **Gestión del cambio y capacitación** | 6.1 Planificación de actividades de gestión del cambio para asegurar una **adopción efectiva**. 6.2 Desarrollo de **programas de capacitación** para el personal |
| **7** | **Métricas y KPIs** | 7.1 Definición de métricas y KPIs para medir el **desempeño de los procesos de TI** y la **efectividad del sistema de gobierno**. 7.2 Establecimiento de **metas y objetivos de desempeño** para cada métrica y KPI |
| **8** | **Gestión de riesgos** | 8.1 Evaluación de los riesgos asociados con la implementación de los procesos y del plan. 8.2 Desarrollo de **estrategias de mitigación** y **planes de contingencia** |
| **9** | **Cronograma y seguimiento** | 9.1 Cronograma detallado para la implementación de las acciones y actividades. 9.2 Proceso de **seguimiento y revisión** para monitorear el progreso y realizar ajustes |
| **10** | **Plan de comunicación** | 10.1 Plan para informar a los **stakeholders** sobre el plan estratégico y sus progresos. 10.2 Identificación de **canales de comunicación** y **mensajes clave** |

**Nota de la cátedra:** muchos de estos puntos **se completan con la documentación obtenida en el análisis realizado para el Sistema de Gobierno de TI**; el resto de la información requerida se completa **con los temas de la Unidad 2**.

---

###### 9. Ciudad inteligente / Smart City

**No aparece en este material.** Ni el apunte ni el PPT de la Unidad 1 mencionan ciudad inteligente, smart city, ni dimensiones o modelos de madurez asociados. Si el TP Integrador lo requiere, **falta ingestar la fuente correspondiente** (probablemente una consigna de TP o material de otra unidad).

---

###### 10. Dudas / pendientes

1. **Figuras no convertidas** — hay que recuperarlas del PDF original: los 40 objetivos COBIT; el catálogo de **metas empresariales** COBIT; el catálogo de **metas de TI** y el **mapeo** entre ambas; las cuatro tablas de análisis organizacional (tamaño, rol de TI, modelo de abastecimiento, estrategia de adopción); riesgos y problemas relacionados con TI; el ejemplo de BSC; la lámina de componentes del sistema de gobierno.
2. **BPMN** — no está en la Unidad 1. Verificar si viene por consigna del TP o por otra unidad.
3. **Smart city** — ídem punto 2.
4. **ITIL** — no citado en este material, pese a ser el marco típico de gestión de servicios. Verificar si entra en Unidad 2 (gestión de servicios de TI).
5. **META vs. OBJETIVO** — la cátedra los usa contrastivamente en la actividad SMART pero **no define la diferencia por escrito**. Confirmar en clase si la definición formal es exigible en parcial.
6. **Horizontes temporales en años** por nivel de planeamiento — no están cuantificados en el material.
7. **Plantilla formal de proceso** (proveedor/entradas/actividades/salidas/cliente/indicadores) — no está en el apunte; solo el esquema entradas→salidas. Verificar si el TP la exige.


---


##### Ejemplo de cátedra — Proceso de Exámenes UTN (Etapa 1)

Documento de referencia: `Material de Cursado / Unidad 1 / 3 - Ejemplo (ProcesoExamenesUTN) / 1 - Contexto - UTN_ProcesoExamenes.pdf`. Autoría: Esp. Lic. Fabiana María Riva. Encabezado fijo en todas las páginas: `Cátedra: ADMINISTRACIÓN DE SISTEMAS DE INFORMACIÓN` / `Contexto: UTN-FRRo - Proceso de Exámenes Finales`. Extensión total: ~5 páginas de texto + organigrama + diagrama BPMN en Anexo II.

###### Estructura del documento (orden exacto de apartados)

| # | Apartado | Contenido | Extensión aprox. |
|---|---|---|---|
| 1 | BREVE DESCRIPCIÓN DEL CONTEXTO | Qué es la organización, para qué fue creada, qué la distingue del resto | 1 párrafo + 2 bullets |
| 2 | ESTRATEGIA DE LA UTN → VISIÓN | Transcripción textual del Estatuto | 1 párrafo |
| 3 | ESTRATEGIA DE LA UTN → MISIÓN | Transcripción textual del Estatuto | 1 párrafo |
| 4 | ESTRATEGIA DE LA UTN → OBJETIVOS | Objetivos agrupados por dimensión (7 dimensiones) | 1-2 bullets por dimensión |
| 5 | ESTRATEGIA DE LA UTN → VALORES | Valores + "principios básicos ser:" | 1 + 4 bullets |
| 6 | **CONSIGNA 1** | Relacionar arquetipos de estrategia y metas COBIT con la estrategia de la UTN | — |
| 7 | CONTEXTO ESPECÍFICO: UTN Facultad Regional Rosario | Baja del nivel institución al nivel unidad de análisis | (imagen/mapa) |
| 8 | COMPONENTES DEL SISTEMA DE GOBIERNO | — | (imagen) |
| 9 | **CONSIGNA 2** | Definir cuestionario a un referente de dirección | — |
| 10 | CADENA DE VALOR Y PROCESOS | Actividades sustantivas + clasificación de procesos en 4 capas + justificación del recorte | ~1 página, cuadro |
| 11 | ESTRUCTURA ORGANIZATIVA | Organigrama de los departamentos que participan del proceso | (imagen, 1 página) |
| 12 | POLÍTICAS Y PROCEDIMIENTOS | Marco normativo en 3 niveles (Nación / Consejo Superior / Facultad) | ~1 página |
| 13 | PROCESO DE EXÁMENES FINALES | Breve descripción: entradas → actividades → salidas | ~1 página |
| 14 | Reglas del Negocio | 7 reglas numeradas | ~1/2 página |
| 15 | (referencia) Diagrama BPMN | Remitido al Anexo II, hecho en Bizagi | — |
| 16 | **CONSIGNA 3** | Análisis Organizacional y Ambiental + formular estrategias | — |

Patrón de fondo: **de lo general a lo particular**. Institución (UTN nacional) → estrategia declarada → unidad concreta (FRRo) → cadena de valor → recorte a un proceso → estructura que lo ejecuta → normativa que lo rige → el proceso en sí → sus reglas.

###### Cómo redacta la descripción de la organización

Fórmula usada: **finalidad fundacional + rasgo diferencial en bullets**.

> "La Universidad Tecnológica Nacional (UTN) fue creada para generar, preservar y transmitir el conocimiento cultural universal y técnico en el campo de la tecnología, siendo la única universidad nacional del país con la ingeniería en el foco central de su estructura académica."

Y a continuación, características distintivas explícitas y cortas:
- "Es la única universidad del país que tiene a la ingeniería como prioridad en su oferta académica."
- "Posee carácter federal, por incluir a todas las regiones de Argentina."

Cierra el apartado **anclando la estrategia a la norma**: "Los art. 1º y 2º del Estatuto Superior de la Universidad, establecen los principios constitutivos, la visión, la misión y los objetivos de la Institución." Es decir: no inventa la estrategia, la cita de la fuente formal.

###### Cómo redacta visión / misión / valores

- **VISIÓN**: párrafo único, largo, aspiracional, sin métricas. Habla de qué clase de institución quiere ser y con qué se compromete. Transcripción literal del Estatuto.
- **MISIÓN**: párrafo único, más corto, con verbos de acción sobre el objeto del negocio. Empieza con la fórmula "Es MISIÓN de la Universidad Tecnológica Nacional: crear, preservar y transmitir los productos de los campos científicos, tecnológico y cultural…". Patrón: **verbos + objeto + destinatario + alcance**.
- **VALORES**: dos bloques. Primero los valores propiamente dichos (libertad, dignidad del hombre, identidad del pueblo argentino, integración armónica de sectores sociales), después una lista de "principios básicos ser:" redactada con **adjetivos institucionales**:

| Principio básico | Redacción textual (abreviada) |
|---|---|
| 1 | "Autónoma, de gestión pública, gratuita, pluralista y laica y con ingreso irrestricto." |
| 2 | "Promotora y garante de calidad académica sustentada en los principios de: libertad académica, la igualdad de oportunidades y posibilidades, jerarquización docente y la convivencia pluralista de teorías y líneas de investigación." |
| 3 | "Solidaria, comprometida y en relación permanente con la comunidad a través de la generación de políticas de articulación con instituciones públicas y otras organizaciones." |
| 4 | "Responsable social de promover el desarrollo nacional a través de un compromiso hacia una mejor calidad de vida de sus habitantes." |

###### Cómo baja metas a objetivos

El documento **no usa el rótulo "metas de negocio" ni "metas de TI"** — ese vocabulario aparece recién en la CONSIGNA 1, que pide relacionar los arquetipos de estrategia y las metas de COBIT con lo que la UTN ya declaró. El patrón implícito es:

1. La organización declara **visión + misión** (nivel aspiracional, no medible).
2. De ahí derivan **OBJETIVOS agrupados por dimensión** — la estructura del ejemplo es una taxonomía de 7 dimensiones que actúa como el equivalente a las perspectivas de un balanced scorecard.
3. El alumno debe **mapear** esos objetivos contra la cascada de metas COBIT (metas corporativas → metas de alineamiento → metas de TI). Ese mapeo es la Consigna 1, no está resuelto en este archivo.

Taxonomía completa de dimensiones de objetivos usada por la cátedra:

| Dimensión | Cantidad de objetivos |
|---|---|
| En relación con lo académico | 2 |
| En relación con lo científico y tecnológico | 1 |
| En relación con lo regional y local | 1 |
| En relación con lo nacional | 2 (uno de ellos absorbe "lo Internacional") |
| En relación con lo social | 1 |
| En relación con lo humanístico cultural | 1 |

Nota: la dimensión "En relación con lo Internacional" viene **anidada dentro del bullet nacional** en el PDF extraído ("• En relación con lo Internacional: Incrementar su presencia…"). Es un defecto de maquetación del original, no una decisión de diseño (inferencia). Al imitar el patrón conviene listarla como dimensión propia.

Ejemplos textuales representativos — **este es el patrón a imitar**:

*Objetivo académico (formativo):*
> "Preparar profesionales idóneos en el ámbito de la tecnología capaces de actuar con eficiencia, responsabilidad, creatividad, sentido crítico y sensibilidad social, para satisfacer las necesidades del medio socio productivo, y para generar y emprender alternativas innovadoras que promuevan sustentablemente el desarrollo económico nacional y regional, en un marco de justicia y solidaridad social."

*Objetivo científico-tecnológico:*
> "Desarrollar la investigación, acordando las máximas facilidades para su realización, definiendo y priorizando modos de acción que sirvan a sus intereses y que promuevan el bienestar de la sociedad y el desarrollo productivo del país."

*Objetivo nacional / productivo:*
> "Fomentar el desarrollo autónomo y sustentable de la industria argentina, y la consolidación del sector de las PyMEs como fuente sustancial de empleo y de aporte al mercado interno y a la exportación."

*Objetivo social (nótese que cierra con una consecuencia operativa concreta):*
> "Extender sus acciones y sus servicios a la comunidad con el fin de contribuir a su pleno desarrollo y a su transformación hacia una forma de sociedad más solidaria que brinde mejor calidad de vida a sus integrantes. Es por ello que, la Universidad Tecnológica nacional consagra el derecho al ingreso irrestricto y a la gratuidad de la enseñanza en sus carreras de grado."

Estructura gramatical común a todos: **verbo en infinitivo + objeto + "para / con el fin de" + finalidad de impacto**. Un solo objetivo por bullet, extensión 2-4 líneas, sin indicadores numéricos.

###### Cadena de valor y clasificación de procesos

Declara primero las **actividades sustantivas**: docencia (Formación de Grado, Pregrado y Posgrado), Investigación, Extensión y Vinculación Tecnológica. Luego toma **una** cadena (Docencia → Formación de Grado) y la descompone en 4 capas:

| Capa | Contenido en el ejemplo |
|---|---|
| Procesos Estratégicos | Consejo Superior (Estatuto Universitario, Planes de Carrera, Reglamentos de Estudio); Consejo Directivo (Resoluciones Regional, Calendario Académico) |
| Procesos de Gestión | Consejos Departamentales (Resoluciones Depto, Planificaciones de Cátedra) |
| Procesos Operativos | Ingreso (Inscripción a Carreras, Seminario Universitario); Docencia (Inscripción a Cursado, Cursado Anual, **Exámenes**); Egreso (Gestión del Título) |
| Procesos de Apoyo | Alumnado, Ingreso, Bedelía, Legajos y Actas, SAU, Tutorías, Biblioteca, RRHH, Audiovisuales, Redes, Sist. de Datos |

El cuadro original venía en tablas mal convertidas por markitdown (celdas vacías, texto de las etiquetas verticales "Entrada/Salida" partido en fragmentos como `tn`, `a se`, `rg`); la tabla de arriba es la reconstrucción del sentido, no la maquetación literal.

**Justificación explícita del recorte** — patrón a imitar cuando el TP pida elegir un proceso:
> "Para simplificar el análisis acotaremos el mismo al proceso de Exámenes que constituye uno de los procesos operativos que puede considerarse clave ya que del mismo depende luego la gestión del título para el estudiante que ha finalizado el cursado y la aprobación de todas las asignaturas de la carrera."

Es decir: el recorte se justifica por **criticidad + dependencia aguas abajo**, no por comodidad.

###### Cómo redacta normas y regulaciones (apartado POLÍTICAS Y PROCEDIMIENTOS)

Estructura en tres niveles descendentes de autoridad:

| Nivel | Fuente normativa | Instrumentos citados en el ejemplo |
|---|---|---|
| Nación | Leyes emanadas de la Nación | LES – Ley de Educación Superior Nº 24.521 (de ella derivan resoluciones como las Actividades reservadas al título de Ingeniero en Sistemas de Información); Leyes y normas de Administración Pública; **específica de TI**: Políticas de Seguridad de la Información para Organismos de la Administración Pública Nacional (ONTI) |
| Consejo Superior UTN | Ordenanzas y resoluciones | Estatuto Universitario; Ordenanzas de creación y diseño curricular de las carreras de Ingeniería (aprobadas por el Ministerio de Educación); Régimen de Organización de Cátedras |
| Facultad Regional | Desarrollo de procesos propios | "Cada Facultad dependiente de la UTN desarrolla sus procesos conforme a las reglamentaciones anteriores." |

Además incorpora el **control externo**: la LES exige acreditación periódica de las carreras por CONEAU, porque preparan para profesiones cuyo ejercicio "puede poner en riesgo de modo directo la salud, la seguridad, los derechos, los bienes o la formación de los habitantes". CONEAU audita según estándares por carrera.

Y **aterriza la normativa al proceso concreto**: los Planes de Carrera establecen el Régimen de Correlativas; el Reglamento de Estudios define las modalidades de aprobación — **Directa** (durante el cursado) o **No Directa** (en el Examen Final). Ese último dato es el que conecta la norma con el proceso elegido.

Patrón a imitar: no listar normas sueltas. Cada norma citada debe terminar explicando **qué restringe o habilita en el proceso bajo análisis**. Nótese que incluye deliberadamente al menos una norma de TI (ONTI) — la consigna del TP pide referirse a cuestiones de TI.

###### Cómo describe el proceso: entradas / actividades / salidas

Encabeza situando el proceso en la cadena de valor: "El proceso que se describe a continuación forma parte de la cadena de valor Docencia de la UTN-FRRo."

**Entradas** — cada una con (a) el documento, (b) el órgano que lo emite entre paréntesis con su sigla, (c) qué aporta al proceso:

| # | Entrada | Emisor | Qué define |
|---|---|---|---|
| a | Ordenanza Plan de Carrera | Consejo Superior en Rectorado (CS) | Las correlatividades |
| b | Reglamento de Estudio | CS | Requisitos para rendir una asignatura |
| c | Ordenanza Calendario Académico | Consejo Directivo en la FRRo (CD) | (fechas de turnos) |
| d | Planificaciones de Cátedra | Consejo Departamental de Carrera (CDep) | Lineamientos de los exámenes; aprobada por el CDep específico |

Aclara además su procedencia: "Son entradas al proceso y pertenecientes a procesos de gestión y de apoyo" — es decir, **cada entrada se rastrea a la capa de proceso de la que viene**.

**Salidas** — con destinatario obligatorio, formuladas como "se requiere para…":

| # | Salida | Proceso destino |
|---|---|---|
| a | Lista de asistencia de docentes | Procesos de RRHH |
| b | Registro de Actas de exámenes | Emisión de certificados analíticos y Trámite de Título |

**Actividades** — 15 pasos numerados, en orden cronológico estricto. Cada paso arranca con el **actor** (o el actor va inmediatamente después del disparador temporal) y usa **verbo en presente**. Los sistemas y documentos van nombrados con precisión:

| # | Actor | Actividad (síntesis) |
|---|---|---|
| 1 | Secretarios de Departamentos Académicos (SDA) | Antes de cada turno, confeccionan la Nómina de ternas de las mesas del turno |
| 2 | SDA | Envían mail a Directores de Cátedra (DCA) para corroborar fechas e integrantes |
| 3 | SDA | Nómina corroborada → se envía a Legajos y Actas |
| 4 | Legajos y Actas | Habilita la Inscripción a Mesas en **SYSACAD (escritorio)** |
| 5 | Alumnos | Hasta 24 hs del día hábil anterior, completan Formulario de inscripción vía **SYSACAD (web)** |
| 6 | Docentes de la mesa | Corroboran cantidad de inscriptos vía SYSACAD (web) |
| 7 | Legajos y Actas | Cada día de exámenes imprime las Actas y las entrega a Bedelía |
| 8 | Bedelía | Confecciona lista de asistencia de docentes y planilla de entrega de actas |
| 9 | DCA / presidentes de terna | Retiran actas en Bedelía y firman planilla de entrega y lista de asistencia |
| 10 | Mesa examinadora | Se desarrollan las mesas, se completan las actas y se devuelven a Bedelía. Si no se completa → **cuarto intermedio**: el presidente lo anota en el Acta con la fecha; el Acta queda en Bedelía hasta completarse. Opcionalmente se completa la Libreta del Alumno |
| 11 | Mesa / Departamento | Exámenes físicos se entregan en sobre al Departamento; se firma planilla de entrega de exámenes físicos |
| 12 | Bedelía | Entrega Lista de asistencia de docentes a RRHH |
| 13 | Bedelía → Legajos y Actas | Entrega actas completas; se registran las Notas del Acta en SYSACAD |
| 14 | Legajos y Actas | Digitaliza el acta; arma la bolsa de envío con originales; entrega a Mesa de Entradas, que la envía a Rectorado |
| 15 | Rectorado | Recibe la bolsa y archiva las Actas por regional y carrera |

Observaciones de estilo sobre las actividades:
- Nombra **roles y áreas**, nunca personas, y define la sigla la primera vez que aparece (SDA, DCA, CS, CD, CDep).
- Los **artefactos** están nominados y se sigue su trazabilidad físicamente de mano en mano (Nómina → Acta impresa → Acta completa → Acta digitalizada → bolsa → archivo en Rectorado).
- El **sistema** (SYSACAD) se distingue por canal: escritorio vs. web. Esto es lo que después habilita el análisis de TI.
- Los **caminos alternativos** (cuarto intermedio) se describen dentro del paso, no como pasos aparte; el detalle fino va a Reglas del Negocio.
- El proceso termina cuando el artefacto llega a su archivo definitivo, no cuando termina el examen.

**Diagrama BPMN**: no se dibuja en el cuerpo del texto, se remite al Anexo II y se declara la herramienta usada — Bizagi, descargable gratis desde bizagi.com/es.

###### Reglas del Negocio (patrón)

7 reglas numeradas. No son pasos: son **restricciones, excepciones y criterios de decisión** que el diagrama no puede expresar.

| # | Regla (síntesis) | Tipo |
|---|---|---|
| 1 | Terna = docentes de teoría, un Presidente (generalmente el docente de teoría de la comisión) y dos vocales | Composición / estructura |
| 2 | Exámenes físicos (incluidos los rendidos en computadora) van en sobre cerrado rotulado, para auditoría de CONEAU o revisión pedida por el alumno según reglamento. Los digitales los guarda la cátedra con el mismo criterio | Resguardo / cumplimiento |
| 3 | Alumno inscripto que no figura en el Acta no puede rendir. Con formulario correcto, Legajos y Actas reimprime el acta y **destruye la incorrecta** | Excepción / control de integridad |
| 4 | Alumno que figura en acta y no se presenta → se indica "AUSENTE" en el lugar de la nota | Codificación de dato |
| 5 | Docente firmante ausente → firma otro docente de teoría o el Director del Departamento. Si la ausencia no es justificada, RRHH pasa a descuento el día | Suplencia + consecuencia administrativa |
| 6 | El examen se desarrolla según la planificación de cátedra. Si es oral, se completa planilla de exámenes orales que va en el sobre | Variante de ejecución |
| 7 | Los exámenes evaluados en forma digital por el campus residen en el servidor de Rectorado | Ubicación del dato / TI |

Patrón a imitar: cada regla cubre un caso que **rompe el camino feliz** y dice quién lo resuelve y con qué consecuencia. Varias tienen componente de TI o de auditoría — no son adorno, alimentan el análisis posterior.

###### Consignas incluidas en el ejemplo (lo que el TP replica)

| Consigna | Ubicación | Enunciado textual |
|---|---|---|
| 1 | Tras VALORES | "Relacione los arquetipos de estrategias y las metas que plantea COBIT con la Estrategia de la UTN" |
| 2 | Tras COMPONENTES DEL SISTEMA DE GOBIERNO | "Defina un cuestionario a realizar a algún referente de las áreas de dirección de la facultad para establecer: tamaño de la organización, rol que tienen las tecnologías de la información en la organización, modelo de abastecimiento y la estrategia de adopción de la tecnología." |
| 3 | Cierre del documento | "A partir de su conocimiento referido al proceso detallado anteriormente y a las consideraciones en relación al contexto realice un Análisis Organizacional y Ambiental. Considere referirse a cuestiones vinculadas con las TI. Formule estrategias." |

Las tres consignas marcan que el contexto **no es el entregable final**: es el insumo sobre el que se aplica COBIT (arquetipos + cascada de metas), el cuestionario de diseño factors (tamaño, rol de TI, modelo de abastecimiento, estrategia de adopción tecnológica) y el análisis organizacional/ambiental con formulación de estrategias.

###### Criterios de corrección implícitos (deducidos del ejemplo)

Todo lo de esta subsección es inferencia a partir de la forma del documento, no está enunciado como rúbrica.

1. **Extensión esperada del contexto**: ~5 páginas de texto para un solo proceso. No es un resumen de media carilla ni un informe de 30.
2. **Trazabilidad a fuentes formales**: visión, misión, objetivos y valores se **transcriben del estatuto u ordenanza**, no se redactan de cero. Se cita el artículo o el órgano emisor.
3. **Recorte justificado**: elegir un proceso operativo y explicar por qué es clave, con criterio de criticidad y dependencias aguas abajo.
4. **Trazabilidad entrada→emisor y salida→destinatario**: ninguna entrada queda sin órgano emisor; ninguna salida queda sin proceso que la consuma. Es el criterio más visible de completitud.
5. **Actores por rol, con siglas definidas**: nada de nombres propios; la sigla se introduce la primera vez y se reutiliza.
6. **Granularidad de las actividades**: entre 10 y 20 pasos. El ejemplo usa 15. Un paso = una acción de un actor sobre un artefacto.
7. **Separación actividades / reglas de negocio**: el flujo va numerado y lineal; las excepciones y restricciones van en un bloque aparte. Mezclarlas es error de forma.
8. **Presencia obligatoria de TI**: sistemas nombrados y diferenciados por canal (SYSACAD escritorio vs. web), normativa de TI citada (ONTI), ubicación física de los datos (servidor de Rectorado). Las consignas 2 y 3 piden explícitamente "cuestiones vinculadas con las TI".
9. **Uso de tablas y cuadros**: la clasificación de procesos va en cuadro de 4 capas; el organigrama va como imagen; entradas y salidas van en listas rotuladas a)/b)/c); las actividades y reglas van numeradas. El texto corrido se reserva para descripción de contexto y normativa.
10. **Anexos**: el diagrama BPMN va en anexo separado, no en el cuerpo, y se declara la herramienta (Bizagi).
11. **Cierre del proceso en el archivo definitivo**: el proceso no termina en la actividad "core" sino cuando el artefacto llega a su destino final. Cortar antes deja salidas huérfanas.

###### Advertencias sobre esta conversión

- El cuadro de clasificación de procesos (Estratégicos / Gestión / Operativos / Apoyo) y las etiquetas verticales "Entrada" / "Salida" vinieron **rotos** de markitdown: tablas con celdas vacías y texto fragmentado (`tn`, `a se`, `rg`, `E n`, `I`). Se reconstruyó el sentido; la maquetación exacta hay que verla en el PDF original.
- El **organigrama** (apartado ESTRUCTURA ORGANIZATIVA), el mapa de CONTEXTO ESPECÍFICO FRRo y el cuadro de COMPONENTES DEL SISTEMA DE GOBIERNO son **imágenes** y no se extrajeron. Ese contenido no está disponible en esta conversión.
- El **diagrama BPMN** está en el Anexo II, que es otro archivo — no forma parte de este documento.

#### Ejercicios resueltos tipo

- **Ejemplo de cátedra:** Proceso de Exámenes UTN-FRRo (transcripto arriba). Es la plantilla de referencia para la Etapa 1 del TPI.
- **Resolución propia:** Etapa 1 del TP Integrador — Personal / Instalación de fibra óptica. Ver sección **TP Integrador** de esta wiki.

#### Dudas / pendientes

- Varias láminas del PPT de Planeamiento Estratégico son **imágenes** y no se extrajeron al convertir el PDF: la lista de los 40 objetivos COBIT, las tablas de metas empresariales y metas de TI, el mapeo entre ambas, la tabla de tamaño de organización, el modelo de abastecimiento, la estrategia de adopción de TI, los riesgos relacionados con TI y el ejemplo de Balanced Scorecard. **Falta conseguir esas tablas** (pedirlas en clase o sacarlas del PDF original a mano) — son las que se usan para justificar el alineamiento negocio-TI.
- No está confirmado qué versión de COBIT usa la cátedra (2019 vs. 5) para la cascada de metas.

#### Fuentes

- `fuentes/ASI/Material de Cursado/Unidad 1/1 - Apunte - Planeamiento Estratégico (V1.1).pdf`
- `fuentes/ASI/Material de Cursado/Unidad 1/2 - PPT - Planeamiento Estratégico (V2.1).pdf`
- `fuentes/ASI/Material de Cursado/Unidad 1/3 - Ejemplo (ProcesoExamenesUTN)/1 - Contexto - UTN_ProcesoExamenes.pdf`
- `fuentes/ASI/Material de Cursado/Unidad 1/3 - Ejemplo (ProcesoExamenesUTN)/2 - BPMN - ProcesoExamenes.pdf` — **el PDF no tiene capa de texto, la conversión salió vacía. Sin leer.**

---

### Unidad 2 — Administración de Recursos en áreas de Sistemas de Información

#### Conceptos clave

- **Riesgo** = evento incierto que, de ocurrir, degrada una dimensión (C, I, D) de un activo. Se valora por **Probabilidad × Impacto = Severidad**.
- **Inventario de activos**: tipo, contenedor, relaciones, **propietario** (decide sobre el activo) vs. **custodio** (lo opera). Valoración C/I/D en escala 1–3; **criticidad = C + I + D**.
- **FAIR**: taxonomía para *justificar* la probabilidad (frecuencia de contacto con la amenaza + capacidad de resistencia) y el impacto (pérdida primaria + pérdida secundaria).
- **Taxonomía SEI**: clasificación jerárquica del origen del riesgo (acciones de personas / fallas de sistemas y tecnología / fallas de procesos internos / eventos externos).
- **Tratamiento**: Evitar, Transferir, Mitigar, Aceptar. Cada uno con ventaja y desventaja. Resultado → **riesgo residual** recalculado.
- **Contingencia ≠ Recuperación ≠ Continuidad.** Contingencia = qué se hace cuando ocurre. Recuperación = cómo se vuelve al estado normal. Continuidad = cómo sigue operando el negocio mientras tanto.
- **ISO 27002:2022**: 93 controles en 4 temas (5 Organizacionales, 6 Personas, 7 Físicos, 8 Tecnológicos). Se seleccionan en el **SOA** (Declaración de Aplicabilidad).
- **ITIL**: Evento → Incidente → Problema → Cambio, sobre una **CMDB** de Elementos de Configuración (CI).

#### Desarrollo


---


##### Fuente

Apunte "Áreas de TI (V1.0)" — UTN FRRo, ISI, ASI, Unidad 2 "Administración de Recursos en Áreas de Sistemas de Información". Autora: Esp. Lic. Fabiana María Riva. 52 páginas + 2 anexos. Todo lo que sigue sale de ese archivo salvo lo marcado como "(inferencia)".

###### Mapa del documento (para ubicar cada tema)

| Págs. | Sección | Estado en esta wiki |
|---|---|---|
| 1 | Introducción: encuadre EDM / objetivos de Gobierno | Parte A (acá) |
| 2–3 | Buenas prácticas en seguridad de la información (CID, ciberseguridad vs. seguridad de la información) | Parte B (riesgos) |
| 4–6 | COBIT 2019 (obj. Gestionar el Riesgo), ISO 31000:2018, MAGERIT v3, serie ISO 27000 | Marcos: acá; aplicación a riesgo: Parte B |
| 7–20 | **El proceso de Gestión de Riesgos** completo | **Parte B — no se desarrolla acá** |
| 21–27 | Gestión de Servicios en TI: ITSM, servicio, calidad, valor, activos, relación con el cliente, procesos, ITIL (historia, v3, 4) | Parte A (acá) |
| 28 | Tabla de las 34 prácticas de ITIL 4 | Parte A (acá) |
| 29–46 | Prácticas desarrolladas: incidentes, solicitudes, Centro de Servicios, eventos, problemas, control de cambios, configuración/activos, versiones | Parte A (acá) |
| 47–49 | Anexo I: proceso COBIT 2019 "Gestionar Riesgos" en detalle | Parte B |
| 50–52 | Anexo II: etapas de un ciberataque + IDS/IPS/SOC | Parte B |

**Dónde está la gestión de riesgos y con qué enfoque:** páginas 7 a 20 del apunte (más el Anexo I, págs. 47–49). El enfoque es: proceso iterativo estructurado según las prácticas de COBIT 2019 (Recopilar datos → Analizar el riesgo → Mantener perfil → Articular → Definir portafolio → Responder), alineado a ISO 31000:2018, con el **método de identificación de activos de MAGERIT v3**, taxonomías de amenazas MAGERIT / comunidades de amenazas FAIR / taxonomía SEI de riesgos operacionales de ciberseguridad / RBS del PMI, **evaluación cualitativa** con escalas de impacto (0–5) y probabilidad (0–5), Severidad = Probabilidad × Impacto, priorización por Pareto 80-20, riesgo inherente vs. residual, estrategias de tratamiento (evitar/transferir/mitigar/aceptar y explotar/compartir/mejorar/aceptar), controles preventivos/detectivos/correctivos, y planes de contingencia, recuperación y continuidad de negocio (RPO/RTO/WRT, NIST 800-34, ISO 22301/BS 25999). Todo eso se desarrolla en la Parte B.

---

##### 1. Encuadre: Gobierno de TI vs. Gestión de TI

El apunte no dedica una sección propia al tema; lo retoma de la Unidad 1 en la Introducción (pág. 1) y en la introducción a Gestión de Servicios (pág. 21). Lo que dice, textual en sustancia:

- **COBIT 2019 separa los objetivos de Gobierno de los de Gestión de TI.** Para cada objetivo el marco establece **Procesos**, que incluyen **prácticas** requeridas y **actividades** a realizar.
- El **Sistema de Gobierno de TI** se encarga de **Evaluar, Dirigir y Monitorizar (EDM)**, en función de cinco objetivos:

| Objetivos del dominio EDM (Gobierno) |
|---|
| Asegurar el establecimiento y mantenimiento del Marco de Gobierno |
| Asegurar la Obtención de Beneficios |
| Asegurar la Optimización del Riesgo |
| Asegurar la Optimización de los Recursos |
| Asegurar el compromiso de las partes interesadas |

- La **Gestión** opera en dominios; el apunte nombra explícitamente **APO (Alinear, Planificar y Organizar)**, donde vive el objetivo **"Gestionar el Riesgo"**.
- El Gobierno de TI requiere información sobre la evolución del **PETI** en términos de **indicadores** que permitan analizar el cumplimiento de objetivos.
- La Unidad 2 se concentra en dos objetivos de Gobierno: **Optimización del Riesgo** (→ seguridad de la información y gestión de riesgos) y **Optimización de los Recursos** (→ **procesos de Gestión de TI** para la administración eficiente y eficaz de los recursos, es decir ITSM/ITIL). En ambos el foco es **mantener la continuidad de los procesos críticos y claves de la organización**.
- La separación Gobierno/Gestión es consecuencia del desarrollo de las TIC y su impacto en los procesos de negocio, y **debe tender a flexibilizar la estructura de las áreas de TI sin desatender los procesos de soporte** requeridos por la organización.

###### Cambio de paradigma (pág. 21)

| Modelo tradicional | Paradigma orientado al negocio |
|---|---|
| Foco en la tecnología | Foco en los procesos |
| Actitud **reactiva** ante la ocurrencia de problemas | Actitud **proactiva** |
| Procesos informales | Procesos implementados a partir de buenas prácticas |
| Orientación al producto | Orientación al servicio / al negocio |

---

##### 2. Marcos, normas y modelos que menciona el apunte

###### 2.1 Para Gestión de Servicios de TI (ITSM)

| Marco / Norma | Qué es, según el apunte |
|---|---|
| **ITIL** (Information Technology Infrastructure Library) | Marco de buenas prácticas de gestión de servicios. **El seleccionado por la cátedra** para comprender las prácticas esenciales. |
| **eSCM** (enabled Service Capability Model) | Mencionado como marco alternativo de ITSM. Sin desarrollo. |
| **COBIT 2019** | Mencionado como marco de ITSM también, "con los dominios de objetivos mencionados en la Unidad 1". |
| **ISO 20000** | Nombrada como **la norma certificable** dentro de la disciplina ITSM. El apunte **no la desarrolla**: es la única mención. |

###### 2.2 Para calidad y madurez del proveedor (págs. 22–23)

| Referencia | Qué aporta |
|---|---|
| **ISO 8402** | Definición de calidad: "Conjunto de propiedades y características de un producto o servicio que le confieren su aptitud para satisfacer necesidades explícitas o implícitas". |
| **Ciclo PDCA de Deming** | Planificar–Hacer–Revisar–Actuar (plan-do-check-act). Base para organizar las actividades de calidad. |
| **ISO 9001** | Certificación que algunas organizaciones exigen a sus proveedores. Prueba que el proveedor tiene un sistema de calidad evaluado por auditor independiente. **No garantiza en términos absolutos** la calidad del servicio, pero indica que el proveedor toma en serio el aseguramiento de calidad. |
| **CMMi** (Capability Maturity Model Integrated, SEI – Carnegie Mellon) | Madurez organizacional del proveedor de servicios de TI. Según el nivel de madurez obtenido se pueden esperar distintos niveles de servicio. |

###### 2.3 Para seguridad y riesgo (se listan acá; se desarrollan en la Parte B)

| Documento | Rol |
|---|---|
| **COBIT 2019** | Objetivo "Gestionar el Riesgo" en el dominio APO. Proceso detallado en Anexo I. |
| **ISO 31000:2018 — Gestión del riesgo. Directrices** | Principios y guías genéricas. **COBIT 2019 está alineado a ISO 31000:2018.** |
| **MAGERIT v3** | Metodología Automatizada de Análisis y Gestión de Riesgos de los SI de las Administraciones Públicas de España. Método formal en tres libros; el Libro I establece el proceso de Gestión de Riesgos basado en ISO 31000 y el método de análisis **basado en la identificación de activos**. Libro II = Catálogo de elementos (amenazas). |
| **Serie ISO 27000** | **ISO 27001:2022 es la única certificable**; las demás son guías de buenas prácticas. |
| **ISO 27001:2022** | Aplicable a todo tipo y tamaño de organización. Propone el marco para el **SGSI** (Sistema de Gestión de la Seguridad de la Información): políticas, objetivos y alcance; análisis, valorización y tratamiento de riesgos sobre los activos; controles y su monitorización; mejora. |
| **ISO 27002:2022** | "Seguridad de la información, ciberseguridad y protección de la privacidad – Controles de seguridad de la información". Actualiza la versión 2013; reordena en **4 temas que agrupan 93 controles**. |
| **ISO 27005:2022** | Directrices para la gestión de riesgos de seguridad de la información. |
| **NIST 800-34** | Metodología para planes de contingencia y recuperación. |
| **ISO 22301 / BS 25999** | Gestión de la Continuidad del Negocio (BCM). |
| **FAIR** (Factor Analysis Information Risk) | Taxonomía de comunidades de amenazas y de factores de frecuencia/magnitud de pérdida. |
| **Taxonomy of Operational Cyber Security Risks (SEI)** | 4 clases de riesgos operacionales de TI. |
| **RBS del PMI** | Estructura de desglose de riesgos en proyectos. |

**Nota importante del apunte:** *"Las normas ISO 27000 no establecen metodologías específicas, por lo que pueden ser complementadas con otros marcos de trabajo"*.

###### 2.4 Atributos de los 93 controles de ISO 27002:2022 (transcripción completa, pág. 5)

Los 4 temas que agrupan los controles se presentaban en una figura que **no sobrevivió a la conversión del PDF** (no hay texto legible de la figura). Los atributos sí están completos:

| Atributo | Valores posibles |
|---|---|
| **Tipo de Control** | Preventivo, Detectivo, Correctivo |
| **Propiedades de Seguridad de la Información** | Confidencialidad, Integridad, Disponibilidad |
| **Conceptos de Ciberseguridad** (5 funciones NIST) | Identificar, Proteger, Detectar, Responder, Recuperar |
| **Capacidades operacionales** | Clasifican controles desde una perspectiva práctica: permiten **asignar responsabilidades** y establecer **lineamientos de implementación** |
| **Dominios de seguridad** | Gobernanza y ecosistema, Protección, Defensa, Resiliencia (conjunto de bienes y recursos sujetos a una política de seguridad común) |

---

##### 3. Conceptos base de ITSM (Gestión de Servicios de TI)

###### 3.1 Servicio

> **Servicio = conjunto de recursos provisto a los clientes para apoyarlo en la operación de una o más áreas de negocio.** Un servicio es percibido como algo **único y completo**.

- La provisión de servicios de TI refiere a **la administración completa de la infraestructura de TI**: hardware, software, herramientas y relaciones con los clientes.
- Un servicio es el **resultado de la interacción de un Cliente con la organización de TI proveedora**; por lo tanto la calidad depende, hasta cierto punto, **de la forma en que proveedor y cliente interactúan**.
- A diferencia de la manufactura, **cliente y proveedor pueden realizar cambios mientras el servicio se está desarrollando**.
- La percepción del cliente es esencial. Las tres preguntas con que el cliente evalúa la calidad:
  1. ¿Se alineó el servicio con mis expectativas?
  2. ¿Podré esperar un servicio similar la próxima vez?
  3. ¿El costo de este servicio es razonable?
- **Que el servicio cumpla las expectativas depende más de cómo se hayan acordado los niveles de servicio que de cómo el proveedor lo haya realizado.** Se requiere diálogo continuo proveedor–cliente.

###### 3.2 Calidad del servicio

- Calidad = **cuánto satisfizo el servicio las expectativas del cliente**. Para proveerla el proveedor debe evaluar continuamente cómo es percibido el servicio y cuáles serán las expectativas futuras. *Un cliente puede considerar normal lo que otro considera un requerimiento especial.*
- El **costo razonable** se considera la satisfacción de una **necesidad implícita**. Acordado el "qué", el paso siguiente es acordar el "cuánto costará"; el proveedor debe conocer sus costos y los valores de mercado de servicios comparables.
- **Proveer una calidad constante es uno de los aspectos más importantes y más difíciles de la industria de los servicios** (un proveedor que a veces excede expectativas y otras decepciona genera insatisfacción).

###### 3.3 Valor del servicio: utilidad y garantía

> Los servicios deben definirse como **un medio de aportar valor al cliente sin que éste deba asumir los riesgos y costos específicos de su prestación**.

**Ecuación del valor:**

| Lado positivo | Lado negativo |
|---|---|
| **Utilidad**: el servicio cumple los requisitos del cliente, aumenta el rendimiento y resulta en un beneficio, disminuyendo costos o contribuyendo a aumentar ingresos | Pérdida de control de todo el proceso |
| **Garantía**: el servicio estará disponible cuando se lo necesite, correctamente dimensionado para cumplir sus objetivos, será seguro y dispondrá de mecanismos de respaldo que permitirán su continuidad | Costos ocultos |
| | Inferior calidad |
| | "Caer cautivo" en manos de un proveedor de servicios |

- El valor **no depende exclusivamente del valor económico**; incluye intangibles, entre ellos la percepción del cliente.
- **El valor para el cliente está en el resultado del servicio y el impacto que éste tiene en su negocio, no en el servicio en sí mismo.**
- Utilidad y garantía son frecuentemente interdependientes: al concebir un servicio nuevo hay que **buscar el equilibrio entre ambas** minimizando lo que el cliente perciba negativamente o como riesgo.

###### 3.4 Activos del servicio

| Activo | Definición | Ejemplos que da el apunte |
|---|---|---|
| **Recursos** | La "materia prima" necesaria para la prestación del servicio | Capital, infraestructuras, aplicaciones, información |
| **Capacidades** | Habilidades desarrolladas a lo largo del tiempo para **transformar los recursos en valor** | Gestión, organización, procesos, conocimiento |
| **Personal** (base de ambos) | Es en sí mismo un recurso que aporta capacidades | Profesionalidad, creatividad, capacidad de liderazgo |

Regla clave: **las capacidades solas no crean valor sin recursos adecuados, y los recursos no se aprovechan sin las capacidades correspondientes.** La organización de TI debe equilibrar ambos.

###### 3.5 Cliente vs. Usuario (definición explícita, pág. 24)

| Rol | Definición del apunte |
|---|---|
| **Usuario** | "La persona frente a una PC", el **empleado que utiliza los servicios de TI por sus actividades rutinarias** |
| **Cliente** | La persona **autorizada a realizar un acuerdo con la organización de TI** referente a la provisión de servicios, y **responsable de asegurar que se entreguen los niveles de servicio por los que se está pagando** |

- El **primer contacto** que tiene un usuario con la organización de TI frente a un incidente es la **Mesa de Ayuda o Centro de Servicios**.
- **La mesa de ayuda provee el servicio al usuario según el nivel de servicio pactado con el cliente, y ese nivel puede no ser el nivel de servicio requerido por el usuario.** (Este es el punto de fricción típico del rol.)
- La calidad de los servicios depende también de las relaciones entre empleados de TI y clientes; el reto es que existan **buenas y efectivas relaciones en todos los niveles**, aunque sean distintas en cada nivel.

###### 3.6 Gestión de servicios basada en procesos

- **Proceso = secuencia lógica de actividades relacionadas para obtener un objetivo determinado.**
- Hay que analizar las **características y estándares de calidad de cada salida** de un proceso, porque son entradas de otro, de modo que la **cadena de procesos** resulte efectiva y eficiente.
- Cada proceso se puede estudiar por separado para analizar su performance **estableciendo indicadores**.
- **ITSM** (IT Service Management): marco focalizado en el proceso y en el servicio, inicialmente llamado "Gestión de TI", enfocado en **alinear los servicios de TI con las necesidades de las empresas**, con énfasis en los beneficios que percibe el cliente final. Propone cambiar el paradigma de gestión de TI por **una colección de componentes enfocados en servicios**, usando marcos con buenas prácticas.

---

##### 4. ITIL

###### 4.1 Origen e historia

| Hito | Contenido |
|---|---|
| Fines de 1980 | La calidad de los servicios de TI provistos al gobierno británico lleva a la **CCTA** (Central Computer and Telecommunications Agency) a desarrollar una propuesta para el uso eficiente y efectivo (en términos financieros) de los recursos de TI. **Resultado: ITIL.** |
| Origen | Biblioteca de **más de 40 volúmenes** con las mejores prácticas de TI. |
| 1º de abril de 2001 | La CCTA se fusiona con la **OGC** (Office of Government Commerce), actual "dueño" de ITIL. |
| Mayo de 2007 | **ITIL V3**: 5 libros principales, **26 procesos**. |
| Febrero de 2022 | **ITIL 4**: enfoque ágil, 4 dimensiones, SVS, **34 prácticas**. |

###### 4.2 Naturaleza del marco

- Provee descripción detallada de prácticas importantes de TI, con **listas de chequeo, tareas, procedimientos y responsabilidades** adaptables a cualquier organización. Están definidas como **procesos**.
- **ITIL no dicta cómo debe estructurarse la organización**: define las **relaciones entre las actividades** en los procesos relevantes para cualquier organización. Esto es central para la pregunta "¿cómo organizo el área de TI?" — ITIL no responde por organigrama sino por procesos y roles.
- Permite compartir experiencias entre organizaciones estableciendo un **lenguaje común**.
- Es el **estándar "de facto"** para describir los procesos fundamentales de ITSM (en parte porque muchos marcos comerciales se basan en él).
- El término pasó de **"mejores prácticas"** a **"buenas prácticas"**.
- De disposición pública desde sus primeras publicaciones; utilizable por **grandes, pequeñas y medianas empresas**.

###### 4.3 ITIL V3 — ciclo de vida del servicio (5 libros / 26 procesos)

| # | Libro (ciclo de vida) |
|---|---|
| 1 | **Estrategia de Servicio** (Service Strategy) |
| 2 | **Diseño del Servicio** (Service Design) |
| 3 | **Transición del Servicio** (Service Transition) |
| 4 | **Operación del Servicio** (Service Operation) |
| 5 | **Mejora Continua del Servicio** (Continual Service Improvement) |

Objetivo principal de V3: **centrarse en el ciclo de vida del servicio y alinear las TI con el negocio.**

###### 4.4 ITIL 4 — las 4 dimensiones del Sistema de Valor del Servicio (SVS)

ITIL 4 cambia a un **enfoque ágil**, con un modelo de cuatro dimensiones que muestran las perspectivas relevantes para el **Sistema de Valor del Servicio (SVS)**:

| Dimensión | Alcance |
|---|---|
| **Organizaciones y Personas** | Aspectos organizacionales y recursos humanos de la empresa |
| **Información y Tecnología** | Todos los elementos técnicos que forman parte de la oferta de servicios |
| **Socios y Proveedores** | Relaciones con otras empresas involucradas en la **co-creación de valor** |
| **Flujos de Valor y Procesos** | Actividades y métricas necesarias para lograr de manera consistente los resultados esperados |

###### 4.5 Procesos → Prácticas

- ITIL 4 usa "procesos" para gestionar los servicios de TI pero **los denomina "prácticas"**.
- Las prácticas **comparten el mismo valor e importancia que los procesos de ITIL v3**, pero tienen una **visión holística de las formas de trabajo**, incorporando cultura, tecnología, información y gestión de datos.
- **Práctica = conjunto de recursos organizacionales para realizar un trabajo o lograr un objetivo.**
- El SVS incluye **34 prácticas** en **3 categorías**:

| Categoría | Cant. | Origen |
|---|---|---|
| Prácticas generales de gestión | **14** | Vienen del mundo empresarial y de la gestión propia del negocio |
| Prácticas de gestión de servicios de TI | **17** | Desarrolladas para la gestión de servicios de TI (ITSM) |
| Prácticas de gestión técnica | **3** | Tomadas de dominios netamente tecnológicos |

> El cuadro de correspondencia entre procesos de ITIL v3 y prácticas de ITIL 4 que anuncia el apunte (pág. 27) era una figura y **no sobrevivió a la conversión del PDF**: no hay contenido legible de ese cuadro.

###### 4.6 Las 34 prácticas de ITIL 4 (tabla completa, pág. 28)

| # | Gestión General (14) | Gestión de Servicio (17) | Gestión Técnica (3) |
|---|---|---|---|
| 1 | Gestión de estrategia | Análisis de negocio | Gestión de la implementación |
| 2 | Gestión de portfolio | Gestión del catálogo de servicios | Gestión de infraestructura y plataformas |
| 3 | Gestión de arquitectura | Diseño de servicios | Desarrollo y gestión de software |
| 4 | Gestión financiera de servicios | Gestión del nivel de servicio | — |
| 5 | Gestión de personal y talento | Gestión de la disponibilidad | — |
| 6 | Mejora continua | Gestión de capacidad y rendimiento | — |
| 7 | Medición e informes | Gestión de la continuidad del servicio | — |
| 8 | Gestión de riesgos | Gestión y monitorización de eventos | — |
| 9 | Gestión de la seguridad y de la información | Asistencia al cliente | — |
| 10 | Gestión del conocimiento | Gestión de incidentes | — |
| 11 | Gestión del cambio organizacional | Gestión de solicitudes de servicio | — |
| 12 | Gestión de proyectos | Gestión de problemas | — |
| 13 | Gestión de las relaciones | Gestión de versiones | — |
| 14 | Gestión de suministros | Control de cambios | — |
| 15 | — | Validación y pruebas del servicio | — |
| 16 | — | Gestión de la configuración del servicio | — |
| 17 | — | Gestión de activos de TI | — |

**Criterio de selección de la cátedra:** el apunte desarrolla solo *"las prácticas más relevantes en relación a la Gestión de Riesgos trabajada anteriormente y a la optimización para la administración de los recursos"*. Son 8: Gestión de Incidentes, Gestión de Solicitudes de Servicio, Centro de Servicios de TI (transversal), Gestión y Monitorización de Eventos, Gestión de Problemas, Control de Cambios, Gestión de la Configuración del Servicio + Gestión de Activos de TI, y Gestión de Versiones.

---

##### 5. Prácticas desarrolladas

###### 5.1 Gestión de Incidentes

> **Incidente (ITIL 4): "una interrupción no planificada de un servicio o la reducción de la calidad de un servicio".**

- **No existe monitorización de los incidentes**: son **informados** por diversas fuentes (usuarios, soporte técnico, etc.). Cuando las interrupciones o la reducción de calidad **son monitorizadas**, ITIL las llama **eventos** y las trata la Gestión de Eventos. Esta es la distinción operativa clave incidente/evento.
- **Objetivo:** minimizar el impacto negativo de los incidentes **restaurando el funcionamiento normal del servicio lo más rápidamente posible**.
- **La velocidad de recuperación es la máxima prioridad.** Por eso pueden abordarse **soluciones temporales en lugar de permanentes** para optimizar el tiempo de respuesta.
- **Vínculo con riesgos:** la comunicación del incidente por el usuario es **el disparador que alerta la materialización de un riesgo que debería haber sido identificado**. Las soluciones temporales y permanentes **son los planes de contingencia y recuperación** que se activan. Si el incidente afecta procesos críticos, probablemente se active el **Plan de Continuidad de Negocio**.

**Actividades:**

**1. Registro**
| Paso | Contenido |
|---|---|
| Admisión del trámite | El Centro de Servicios evalúa en primera instancia si el servicio requerido **está incluido en el SLA del cliente**; si no, lo reenvía a una autoridad competente |
| Comprobación de no duplicación | Es moneda corriente que varios usuarios notifiquen el mismo incidente |
| Asignación de referencia | Identificador unívoco, para procesos internos y comunicación con el cliente |
| Registro inicial | Hora, descripción, sistemas afectados, etc. |
| Información de apoyo | Solicitada al cliente por formulario específico u obtenida de la **CMDB**, que interrelaciona los **CI** (elementos de configuración) o activos de TI del servicio: hardware, software, documentación, etc. |
| Notificación del incidente | Si puede afectar a otros usuarios, se los notifica para que sepan cómo impacta en su flujo habitual de trabajo |

**2. Clasificación**
| Paso | Contenido |
|---|---|
| Categorización | Categoría (subdivisible en niveles) según tipo de incidente o grupo de trabajo responsable. Se identifican los **servicios afectados** |
| Nivel de prioridad | Con criterios predefinidos, porque suele haber múltiples incidentes concurrentes |
| → **Impacto** | Importancia según **cómo afecta a los procesos de negocio** y/o **número de usuarios afectados** |
| → **Urgencia** | **Tiempo máximo de demora que acepte el cliente** y/o el nivel de servicio acordado en el **SLA** |
| Asignación de recursos / **Escalado** | Ver tabla de escalado abajo |
| Monitorización de estado y tiempo de respuesta | Estados p. ej.: registrado, activo, suspendido, resuelto, cerrado. El tiempo de resolución se estima **en base al SLA correspondiente y a la prioridad** |

**3. Análisis, Resolución y Cierre**
1. Se examina el incidente con ayuda de la **KB** (base de conocimiento) para ver si se identifica con un incidente ya resuelto y aplicar el procedimiento asignado.
2. Si se escapa de las posibilidades del Centro de Servicios, se redirecciona a un nivel superior para investigación por expertos asignados.
3. Si los expertos tampoco lo resuelven, se siguen los **protocolos de escalado predeterminados**.
4. Durante todo el ciclo de vida se actualiza la información en las bases de datos correspondientes.

Al solucionarse: **(1)** se confirma con los usuarios la solución satisfactoria, **(2)** se incorpora el proceso de resolución a la **KB**, **(3)** se actualiza la **CMDB** sobre los CI implicados, **(4)** se cierra el incidente.

**La gestión de incidentes no acaba con el cierre**: uno de los enfoques de ITIL 4 es la **mejora continua**, buscando reiterativamente soluciones de prevención que impidan que surjan problemas o incidentes que afecten la calidad del servicio.

**KPIs de Gestión de Incidentes (tabla completa):**

| KPI | Descripción |
|---|---|
| Cantidad de incidentes repetidos | Cantidad de incidentes repetidos (con métodos para su resolución ya conocidos) |
| Incidentes resueltos a distancia | Cantidad de incidentes resueltos a distancia por el Service Desk (p. ej. sin acudir al lugar del usuario) |
| Cantidad de escalados | Cantidad de escalados de incidentes no resueltos en el tiempo acordado |
| Cantidad de incidentes | Cantidad de incidentes registrados por el Service Desk, agrupados por categorías |
| Tiempo de resolución de incidente | Tiempo medio para resolver un incidente, agrupados por categorías |
| Tasa de Resolución de Primera Llamada | Porcentaje de incidentes resueltos en el Service Desk durante la primera llamada, agrupados por categorías |
| Resolución dentro del SLA | Porcentaje de incidentes resueltos durante el tiempo acordado en el SLA, agrupados por categorías |
| Esfuerzo de resolución de incidente | Promedio de esfuerzo de trabajo para resolver incidentes, agrupados por categorías |

###### 5.2 Gestión de Solicitudes de Servicio

- **Qué es:** la práctica encargada de **atender las solicitudes de los usuarios**, proporcionándoles información y **acceso rápido a los servicios estándar** de la organización TI.
- **Una solicitud puede englobar:**
  - Solicitudes de información o consejo
  - Solicitudes de **cambios estándar**
  - Solicitudes de **acceso a servicios de TI**
- **Beneficios que enumera el apunte:** mejora la productividad del departamento comercial, la calidad de los servicios comerciales y los propios productos; **reduce la burocracia** del proceso de solicitud de acceso a servicios nuevos o existentes, reduciendo costos; **incrementa el nivel de control** sobre los servicios al **centralizar la concesión de acceso**; reduce costos al **centralizar la negociación con proveedores** respecto al acceso a servicios; y reduce el costo del soporte.

**Actividades:**

| # | Actividad | Contenido |
|---|---|---|
| 1 | **Selección de solicitudes** | Los usuarios emiten sus peticiones, mediante herramientas destinadas a tal fin, conforme a **tipologías predefinidas** |
| 2 | **Aprobación financiera** | La mayoría de las solicitudes tiene implicancias financieras: se considera su costo y se decide si tramitarla o no |
| 3 | **Tramitación** | La solicitud es cursada por la persona o personas adecuadas según cada caso |
| 4 | **Cierre** | Tras notificar al Centro de Servicios y comprobar desde allí que el usuario quedó conforme, se cierra |

**KPIs de Gestión de Solicitudes de Servicio (tabla completa):**

| KPI | Descripción |
|---|---|
| Solicitudes de Servicio procesadas | Cantidad total de solicitudes de servicio |
| Estado de Solicitudes de Servicio | Desglose de solicitudes en cada etapa: registrada, aprobada, cerrada, etc. |
| Solicitudes Pendientes | Tamaño de la lista de solicitudes de servicio pendientes |
| Tiempo de atención de solicitudes | Promedio de tiempo de atención de las solicitudes de servicio por tipo |
| Solicitudes finalizadas con éxito | Cantidad y porcentaje de solicitudes completadas de acuerdo a los tiempos acordados |
| Costo promedio | Costo promedio de solicitudes de servicio por tipo de solicitud |
| Nivel de Satisfacción del cliente | Nivel de satisfacción del cliente con el tratamiento de la solicitud, medido por **encuestas de satisfacción** |

###### 5.3 Centro de Servicios de TI (Mesa de Ayuda / Service Desk)

> Para la Gestión de Incidentes **y** la Gestión de Solicitudes, los usuarios finales son derivados a un **único punto de contacto (o primera línea de soporte)**: el **Centro de Servicios de TI**.

**Canales de acceso que debe brindar (lista completa, pág. 33):**

| Canal | Detalle |
|---|---|
| Llamadas telefónicas | Pueden incluir respuesta de voz interactiva (**IVR**), conferencias telefónicas, reconocimiento de voz y otros |
| Portales de servicios y aplicaciones móviles | Respaldados por **catálogos de solicitudes y servicios** y bases de conocimientos |
| Chat | Chat en vivo y **chatbots** |
| Correo electrónico | Para registro y actualización, y para encuestas de seguimiento y confirmaciones |
| Centros de servicio sin cita (presencial) | Cada vez más frecuentes en algunos sectores, p. ej. educación superior, donde hay **altos picos de actividad que exigen presencia física** |
| Mensajes de texto y redes sociales | Útiles para notificaciones en incidentes importantes y para contactar grupos específicos de partes interesadas; también permiten a usuarios solicitar asistencia |
| Foros de discusión y redes sociales públicas y corporativas | Para contactar al proveedor de servicios y para **soporte entre pares** |

**Modalidades de organización:** en algunos casos el centro de servicios es un equipo que trabaja en un **solo lugar (centralizado)**; en otros, una **mesa de servicio virtual** permite a los agentes trabajar desde múltiples ubicaciones dispersas geográficamente, con soluciones basadas en la nube.

**Tecnologías de apoyo requeridas (lista completa, pág. 33):**

| Tecnología | Detalle / ejemplos que da el apunte |
|---|---|
| Sistemas de telefonía inteligente | Integración telefonía-computadora, IVR, distribución automática de llamadas |
| **Software de Gestión de Servicios de TI (ITSM)** | Suite completa: gestión de incidentes, solicitudes, etc. Permiten registrar, priorizar y gestionar todos los tickets. **ServiceNow, BMC Remedy, Jira Service Desk** |
| Herramientas de Automatización de Procesos | Integradas a la plataforma de conocimiento, para tareas repetitivas y flujos de trabajo. **Microsoft Power Automate, Zapier** |
| Software de Gestión del Conocimiento | Bases de conocimiento (**KB**) integradas en el ITSM o independientes: **Confluence, SharePoint**. Documentación detallada, guías de solución de problemas, artículos de ayuda |
| Herramientas de Colaboración y Comunicación | **Microsoft Teams, Slack**, o chat en tiempo real integrado al ITSM. Comunicación entre miembros del Service Desk, otros grupos de soporte y usuarios finales |
| Portal de Autoservicio para Usuarios Finales | Registrar incidentes y solicitudes, seguir el progreso de sus tickets, acceder a documentación y buscar soluciones a problemas comunes de manera autónoma |
| **CMDB** (Base de Datos de Configuraciones) | Repositorio centralizado de los elementos de configuración: **hardware, software, documentación y personas** que forman parte de la infraestructura del cliente y de los servicios prestados. Incidentes y Solicitudes pueden asociar estos elementos al registro |

**Niveles de soporte y escalado (págs. 30 y 34):**

| Concepto | Definición |
|---|---|
| **Primera línea de soporte** | El **Centro de Servicios de TI**: único punto de contacto del usuario final |
| **Escalado** | Recurrir a un especialista o a un superior porque el Centro de Servicios no puede resolver en primera instancia o la decisión escapa a su responsabilidad |
| **Escalado funcional** | Se requiere el apoyo de un **especialista de más alto nivel** para resolver el problema. *"En general denominado **segunda línea de soporte**, que puede ser personal abocado a la Gestión de Problemas"* |
| **Escalado jerárquico** | Se acude a un **responsable de mayor autoridad** para tomar decisiones que escapan a las atribuciones de ese nivel; por ejemplo, **asignar más recursos** para la resolución de un incidente específico |
| **Segunda / tercera línea** | Las actividades de **Gestión y Monitorización de Eventos** *"no pueden ser realizadas por el Centro de Servicios de TI"*: están asignadas a **personal técnico con competencias específicas que conforma una segunda o tercera línea de soporte** |

Ojo con la distinción de ejes: **funcional = competencia técnica** (horizontal, hacia el especialista); **jerárquico = autoridad para decidir/asignar recursos** (vertical, hacia el jefe). Son independientes: un mismo incidente puede escalar por los dos.

###### 5.4 Gestión y Monitorización de Eventos

- **Propósito:** observar sistemáticamente los servicios y componentes del servicio, y **registrar e informar cambios de estado seleccionados identificados como eventos**. Identifica y prioriza infraestructura, servicios, procesos comerciales y eventos de seguridad de la información, y **establece la respuesta adecuada**, incluida la respuesta a condiciones que podrían conducir a posibles fallas o incidentes.
- **Evento = cualquier cambio de estado que tenga importancia para la gestión de un servicio u otro CI.** Se reconocen a través de **notificaciones** creadas por un servicio de TI, un CI o una herramienta de monitoreo.

**Clasificación de eventos (tabla completa, con su vínculo a riesgos):**

| Tipo | Definición | Vínculo con Gestión de Riesgos (lo dice el apunte) |
|---|---|---|
| **Informativos** | No requieren acción en el momento en que se identifican, pero el análisis posterior de los datos puede revelar información beneficiosa | Insumo para la **Gestión de Problemas** |
| **De advertencia** | Permiten tomar medidas **antes** de que la empresa experimente un impacto negativo | Es un **disparador para Estrategias de Tratamiento** en la Gestión de Riesgos |
| **Excepciones** | Indican que se identificó una **infracción a una norma establecida**. Requieren acción | Son los **disparadores de Planes de Contingencia** en la Gestión de Riesgos |

**Interacción con otras prácticas:** algunos eventos calificarán como **incidente** → se inicia la Gestión de Incidentes. Eventos **repetidos** con desempeño fuera de los niveles deseados pueden ser evidencia de un **problema potencial** → Gestión de Problemas. Para algunos eventos la respuesta correcta es **iniciar un cambio** → Control de Cambios.

**Automatización e intervención humana:** aunque una vez implementada la práctica está **altamente automatizada, la intervención humana sigue siendo necesaria y de hecho esencial** — para definir estrategias de monitoreo, umbrales específicos y criterios de evaluación, incorporando perspectivas de infraestructura, aplicaciones, propietarios de servicios, gestión del nivel de servicio y prácticas relacionadas con la garantía. **Los roles y responsabilidades deben estar claramente definidos**, y cada persona o grupo debe tener acceso fácil y oportuno a la información necesaria para desempeñar su rol.

**Tipos de herramientas de monitorización:**

| Tipo | Cómo opera |
|---|---|
| **Monitorización activa** | Se comprueban los **CI uno a uno** para verificar estado y disponibilidad. Si detecta excepciones, genera una **alerta** y la envía al equipo o mecanismo de control asignado |
| **Monitorización pasiva** | **Detectan y correlacionan alertas operacionales**, que quedan registradas asociadas al mismo CI (p. ej. logs de acceso) |

También deben usarse **herramientas automatizadas para la correlación de eventos** (herramientas de supervisión o sistemas de flujo de trabajo ITSM). Advertencia del apunte: *"puede haber un gran volumen de datos generados por esta práctica, pero sin políticas y estrategias claras sobre cómo limitar, filtrar y usar estos datos, no tendrán ningún valor"*.

**Actividades (7 pasos):**

| # | Actividad | Contenido |
|---|---|---|
| 1 | Detección del disparador del evento | El proceso se inicia cuando ocurre el suceso |
| 2 | Notificación del evento | Al equipo responsable de su resolución o gestión |
| 3 | Detección y filtrado del evento | La notificación llega a un agente o herramienta de gestión que lee e interpreta el suceso para determinar si merece mayor atención |
| 4 | Clasificación del evento | Se asigna categoría y nivel de prioridad |
| 5 | Correlación | Se analiza si existen eventos similares y la importancia del evento en sí mismo; se decide si hay que tomar medidas |
| 6 | Selección de la respuesta | Se ponen en marcha los mecanismos de respuesta; se eligen las soluciones a adoptar |
| 7 | Revisión de acciones y cierre | Se revisan las excepciones o eventos importantes para determinar si se trataron correctamente; se cierra el proceso |

**KPIs de Gestión y Monitorización de Eventos (tabla completa):**

| KPI | Descripción |
|---|---|
| Eventos clasificados | Número de eventos por categorías y por impacto; número y porcentaje de cada tipo de evento, por plataforma o aplicación |
| Intervención en eventos | Número y porcentaje de eventos que requirieron intervención humana, y cómo fue esa intervención |
| Escalado para resolución | Número y porcentaje de eventos que desembocaron en el registro de un nuevo incidente o solicitud de cambio |
| Eventos reiterados | Número y porcentaje de eventos ocasionados por problemas ya existentes o errores conocidos |
| Eventos duplicados | Número y porcentaje de eventos repetidos o duplicados. Relevante para **optimizar la función de Correlación** |
| Eventos por problemas de capacidad | Número y porcentaje de eventos relacionados con problemas de rendimiento |
| Eventos por problemas de disponibilidad | Número y porcentaje de eventos que indican futuros problemas de disponibilidad |
| Ratio de Incidentes por Eventos | Número y ratio de eventos por comparación al número de incidentes |

###### 5.5 Gestión de Problemas

> **Problema (ITIL 4): "una causa, o causa potencial, de uno o más incidentes".**

**Incidente vs. Problema (la distinción que más se pregunta):**

| Incidente | Problema |
|---|---|
| Elemento **reparable (break-fix)** que causa un impacto negativo en las personas | **Causa** incidentes o eventos |
| Debe **resolverse** para restaurar el funcionamiento normal del trabajo | Debe **analizarse e investigarse** para identificar soluciones temporales o definitivas que reduzcan el **número y el impacto de futuros incidentes o eventos** |

**Modalidades:**

| Modalidad | Definición |
|---|---|
| **Reactiva** | Notificado el incidente o evento que **no tiene solución temporal o definitiva conocida**, lo analiza para descubrir su causa y proponer soluciones |
| **Proactiva** | Basándose en los incidentes registrados o **monitorizando la calidad de la infraestructura TI** y analizando su configuración, con el objetivo de **prevenir** incidentes o eventos con las mismas características antes de que ocurran. Cuando un tipo de incidente se vuelve **recurrente** o tiene fuerte impacto en la infraestructura, es función de esta práctica determinar sus causas y encontrar soluciones definitivas |

**Límite explícito:** *"la Gestión de Problemas **no realiza la implementación de cambios**; para esto existe una práctica específica: el Control de Cambios, con la que debe interactuar"*.

**Actividades:**

**1. Identificación y Registro.** Todas las áreas de la infraestructura TI deben colaborar informando cualquier síntoma que pueda ser señal de deterioro del servicio. El problema se registra completando el registro del incidente (gestión proactiva) o con registro inicial tras analizar incidentes recurrentes. El registro debe contener, entre otra información:
- CI implicados
- Causas del problema
- Síntomas asociados
- Soluciones temporales
- Servicios involucrados
- Niveles de urgencia, prioridad e impacto
- **Estado: activo, error conocido, cerrado**

**2. Clasificación y Asignación de recursos.** Características generales (hardware o software), áreas funcionales afectadas, detalles de los CI involucrados. **La prioridad puede cambiar durante el ciclo de vida del problema** (por ejemplo, si aparece una solución temporal que reduce considerablemente su impacto). Los recursos asignados deben ser suficientes para tratar eficazmente los problemas asociados y minimizar su impacto en la infraestructura.

**3. Análisis y diagnóstico.** Determinar las causas y **proporcionar soluciones temporales a la Gestión de Incidentes** para minimizar el impacto hasta que se implementen los cambios definitivos.
- **No siempre el origen es un error de hardware o software.** Puede estar causado por: **errores de procedimiento, documentación incorrecta, falta de coordinación entre diferentes áreas**. También puede ser un *bug* conocido de alguna aplicación.
- Conviene contacto directo con el entorno de desarrollo (aplicaciones internas) o investigar en Internet errores conocidos aplicables.
- **Determinadas las causas, el problema se convierte en Error Conocido y se remite al Control de Errores.**

**4. Control de Errores.** Registra los errores conocidos y propone soluciones mediante **Solicitudes de Cambio (RFC)** enviadas al Control de Cambios. Efectuado el cambio, realiza la **PIR** (revisión post-implementación) en estrecha colaboración con el Control de Cambios.
- *Análisis y Solución:* investigar diferentes soluciones evaluando el posible **impacto en la infraestructura TI, los costos asociados y sus consecuencias sobre los SLA**. Si el impacto del problema puede tener consecuencias graves en la calidad del servicio, puede emitirse una **RFC de emergencia**.

**5. Revisión Post Implementación y Cierre.** Antes de cerrar el problema se analiza el resultado de la implementación de la RFC mediante la **PIR**. Si los resultados son los deseados y se pueden cerrar todos los incidentes relacionados, se considera concluido el proceso y se emiten los informes.

**Qué debe lograr una buena gestión de problemas:**
- Disminución del número de incidentes y resolución más rápida de los mismos.
- Mayor eficacia en la resolución de problemas.
- Gestión proactiva que identifique problemas potenciales antes de que se manifiesten o provoquen seria degradación de la calidad del servicio.

**KPIs de Gestión de Problemas (tabla completa):**

| KPI | Descripción |
|---|---|
| Cantidad de problemas | Cantidad de problemas registrados, agrupados por categorías |
| Tiempo de resolución de problemas | Tiempo medio para resolver problemas, agrupados por categorías |
| Cantidad de incidentes por problema | Cantidad media de incidentes vinculados al mismo problema **antes** de identificar el problema |
| Cantidad de incidentes por problema conocido | Cantidad media de incidentes vinculados al mismo problema **después** de identificar el problema |
| Tiempo hasta la identificación del problema | Tiempo medio transcurrido entre la primera aparición de un incidente y la identificación de la raíz del problema |
| Esfuerzo de resolución de problemas | Tiempo medio de esfuerzo de trabajo para resolver problemas, agrupados por categorías |

###### 5.6 Control de Cambios

> *"Lo único inmutable es el cambio."* El cambio suele ser fuente de problemas y no debe hacerse sin evaluar bien sus consecuencias, **pero puede resultar mucho más peligroso el estancamiento en servicios y tecnologías desactualizados.**

- **Objetivo principal:** **evaluación y planificación** del proceso de cambio para asegurar que, si se lleva a cabo, se haga de la forma más eficiente, siguiendo los procedimientos establecidos y asegurando en todo momento la **calidad y continuidad del servicio TI**.
- **El Control de Cambios debe asegurar que los cambios:**
  - están **justificados**
  - se llevan a cabo **sin perjuicio de la calidad del servicio TI**
  - están convenientemente **registrados, clasificados y documentados**
  - han sido cuidadosamente **testeados en un entorno de prueba**
  - se ven reflejados en la **CMDB**
  - **pueden deshacerse** mediante planes de "retirada del cambio" (**back-outs**) en caso de incorrecto funcionamiento tras la implementación

**Roles y órganos (conceptos básicos):**

| Rol / órgano | Definición |
|---|---|
| **Gestor de Cambios** | Responsable del proceso del cambio. En grandes organizaciones puede disponer de un **equipo de asesores específicos** para cada una de las diferentes áreas |
| **CAB** (Consejo Asesor de Cambios) | **Órgano interno, presidido por el Gestor de Cambios**, formado principalmente por representantes de las principales áreas de la gestión de servicios TI. Puede incorporar **consultores externos, representantes de grupos de usuarios y representantes de los principales proveedores de software y hardware** |
| **ECAB** | Comité de emergencia; puede formarse en casos de necesidad |

**Actividades:**

**1. Registro.** Orígenes posibles de una RFC (lista completa):

| Origen | Detalle |
|---|---|
| **Gestión de Problemas** | Propone soluciones a errores conocidos; en la mayoría de los casos acarrea un cambio en la infraestructura TI |
| **Gestión de Solicitudes de Servicio** | Puede requerir cambios de infraestructura. Hay que coordinar con las Gestiones de **Capacidad, Disponibilidad y Niveles de Servicio** para asegurar que cumplan expectativas y **no deterioren la calidad de los otros servicios prestados** |
| **Estrategia empresarial** | La dirección puede decidir una redirección estratégica que afecte, p. ej., a los niveles de servicio ofrecidos; suele requerir cambios de hardware, software y/o procedimientos |
| **Actualizaciones de software de terceros** | Los proveedores dejan de soportar versiones anteriores o introducen nuevas versiones con grandes mejoras |
| **Imperativo legal** | Un cambio de legislación puede exigir cambios en la infraestructura TI |
| **Otros** | Cualquier empleado, cliente o proveedor puede sugerir mejoras que requieran cambios |

Contenido mínimo del **registro inicial de una RFC**: fecha de recepción; identificador único; identificador del error conocido asociado (si corresponde); descripción del cambio propuesto (motivación, propósito, CI involucrados); estimación de recursos necesarios para la implementación; tiempo estimado; estado inicial "registrado".

El registro se **actualiza durante todo el proceso** e incluye al menos: cambios de estado ("aceptado", "rechazado", "implementado", etc.) y sus fechas; evaluación realizada por la Gestión del Cambio; prioridad y categoría (según impacto y urgencia); **especificación de los planes de back-out**; recursos asignados; fecha de implementación; descripción del **plan de implementación, que deberá seguir la Gestión de Versiones**; cronograma; **PIR** (revisión post-implementación); evaluación final y fecha de cierre.

**2. Aceptación o rechazo.** Una RFC puede rechazarse si el cambio no está justificado, o pedirse su modificación si algunos aspectos son mejorables o necesitan mayor definición; en esos casos se devuelve al departamento o persona que la generó. **La aceptación no implica la posterior aprobación por el CAB**: es solo indicación de que se justifica su implementación.

**3. Clasificación.** Establecer **prioridad y categoría** según urgencia e impacto. La prioridad determina la importancia relativa de esta RFC respecto de otras pendientes y es **el dato relevante para establecer el calendario de cambios**.

**4. Aprobación y Planificación.** Evaluación minuciosa: **un cambio menor puede derivar en una reacción en cadena con resultados catastróficos**. Es imprescindible disponer de **planes de back-out** que permitan recuperar la última configuración estable antes del cambio.

**5. Implementación del cambio.** En ITIL 4 el Control de Cambios **se adapta para ser más ágil**, permitiendo cambios más rápidos y frecuentes manteniendo control y mitigación de riesgos. Promueve **entrega continua y despliegue continuo**, lo que implica **automatización de los procesos de construcción, prueba y despliegue**, en estrecha relación con la **Gestión de Versiones** y la **Gestión de la Configuración**. *"Los clientes y proveedores no deben percibir el cambio como algo inesperado"*: es función tanto del Control de Cambios como del **Centro de Servicios de TI** mantener informados a los usuarios, hacerlos partícipes escuchando sugerencias, comunicar las ventajas, aclarar dudas y dar soporte — **la percepción de mejora debe ser compartida por usuarios y clientes**.

**6. Evaluación del cambio.** Antes del cierre hay que verificar que fue positivo para el servicio. **El Control de Cambios emite el dictamen final, pero es la evaluación del servicio la que le proporciona los informes.** Si el proceso y los resultados fueron satisfactorios se cierra la RFC y toda la información se incluye en la **PIR** asociada.

**Cambios de Emergencia.** Cualquier interrupción del servicio de alto impacto —por número de usuarios afectados o por involucrar sistemas/servicios críticos— debe encontrar respuesta inmediata. Los procedimientos deben estar previstos, con protocolos que impliquen **reuniones urgentes del CAB y/o ECAB**, o decisiones del **Gestor del Cambio** si es imposible demorar la resolución o el hecho sucede en períodos de inactividad. **Al cierre del cambio de emergencia se debe disponer de la misma información que tras un cambio normal**; si no, se provocarían cambios futuros incompatibles, configuraciones registradas incorrectas, etc., fuente de nuevos incidentes y problemas.

**KPIs de Control de Cambios (tabla completa):**

| KPI | Descripción |
|---|---|
| Cantidad de cambios solicitados | Cantidad de RFC evaluadas por el CAB |
| Cantidad de reuniones de CAB | Cantidad de reuniones de CAB con información estadística asociada: número de asistentes, duración, número de cambios aprobados por reunión, etc. |
| Tasa de aceptación de cambios | Cantidad de RFC aceptadas vs. rechazadas |
| Número de cambios clasificados | Número de cambios realizados clasificados por impacto y prioridad, y filtrados temporalmente |
| Tiempo para autorización para cambios | Tiempo medio desde la solicitud de una RFC al Control de Cambios hasta la autorización |
| Tiempo medio del cambio | Tiempo medio desde la autorización de una RFC hasta su cierre, según impacto y prioridad |
| Porcentaje de cambios exitosos | Porcentaje de cambios exitosos en primera instancia, segunda instancia, etc. |
| Cantidad de Back-outs | Número de back-outs con una detallada explicación de los mismos |
| Porcentaje de cambios cerrados sin incidentes ulteriores | Cantidad de cambios que **no** requirieron la ejecución de planes de back-out |
| Incidentes asociados a cambios realizados | Cantidad de incidentes detectados asociados a cambios realizados, después de su cierre |
| Cantidad de cambios urgentes | Cantidad de cambios urgentes evaluados por el **ECAB** (Consejo Consultor para Cambios de Emergencia) |
| Evaluaciones post-implementación | Cantidad de **PIR** realizadas posteriores a la implementación de un cambio |

###### 5.7 Gestión de la Configuración del Servicio y Gestión de Activos de TI

**Cambio v3 → 4:** en **ITIL V3 estas gestiones estaban unidas**. La separación en **ITIL 4** permite **mayor claridad y enfoque** en las actividades y objetivos específicos de cada práctica, facilitando una gestión más efectiva de la infraestructura de TI y los recursos asociados. Pueden superponerse en algunas áreas, pero cada una tiene su propio conjunto de actividades y responsabilidades.

| Práctica | Se centra en | Objetivo principal |
|---|---|---|
| **Gestión de la Configuración del Servicio** | Mantenimiento de la **CMDB** y gestión de los **CI** | Proporcionar una **visión precisa y actualizada** de la infraestructura de TI y los servicios asociados, incluyendo **la relación entre los distintos CI y su estado en un momento dado** |
| **Gestión de Activos de TI** | Gestión de los activos de TI **a lo largo de todo su ciclo de vida**, desde la adquisición hasta la disposición | **Maximizar el valor** de los activos de TI y **optimizar su rendimiento, costo y riesgo asociado** |

**Actividades de la Gestión de la Configuración del Servicio (7):**

| # | Actividad | Contenido |
|---|---|---|
| 1 | Identificación de CI | Identificar y definir los CI de la infraestructura y los servicios asociados: hardware, software, documentación, **personas, procesos** y cualquier otro componente necesario para entregar y soportar los servicios de TI |
| 2 | Registro y Clasificación de CI | Registrar formalmente cada CI en la **CMDB** y clasificarlos según **tipo, función y relación con otros CI**. Mantiene inventario completo y organizado |
| 3 | Control de la Configuración | Establecer controles y procedimientos para gestionar cambios en la configuración de los CI a lo largo de su ciclo de vida: **autorizar, registrar, evaluar y aprobar** cambios de configuración y gestionar su implementación controlada y coordinada |
| 4 | Auditoría y Verificación de CI | Auditorías regulares y verificaciones de **precisión e integridad** de la información en la CMDB, para garantizar que refleje el estado actual y se mantenga actualizada |
| 5 | Gestión de Relaciones y Dependencias | Identificar y gestionar relaciones y dependencias entre CI: comprender cómo un cambio en un CI puede afectar a otros y a los servicios, y **minimizar los impactos negativos** |
| 6 | Reportes y Análisis de Configuración | Informes y análisis periódicos: métricas de rendimiento, tendencias de cambio, **cumplimiento de políticas y requisitos regulatorios**, y otros datos relevantes |
| 7 | Gestión de Versiones y Baselines | Gestionar versiones y **baselines** de configuración para mantener registro histórico de cambios y **facilitar la reversión a estados anteriores**; garantiza integridad y consistencia y mitiga riesgos asociados a los cambios |

**Actividades de la Gestión de Activos de TI (6):**

| # | Actividad | Contenido |
|---|---|---|
| 1 | Planificación Estratégica de Activos | Estrategia de gestión de activos **alineada a los objetivos del negocio**: políticas, objetivos y procedimientos, y **definición de roles y responsabilidades** dentro de la organización |
| 2 | Adquisición y Aprovisionamiento | Identificar necesidades y adquirir de manera eficiente y efectiva: **evaluar proveedores, negociar contratos, realizar compras** y gestionar el aprovisionamiento desde la solicitud inicial hasta la entrega y aceptación |
| 3 | Seguimiento y Control de Activos | Seguimiento detallado a lo largo del ciclo de vida: registros actualizados, **inventarios regulares**, verificación de ubicación y estado, y cumplimiento de **acuerdos de licencia y contratos** |
| 4 | Gestión de Licencias de Software | Gestión proactiva para garantizar el **cumplimiento legal** y optimizar costos: registros precisos, control de uso, gestión de renovaciones, actualización de políticas |
| 5 | Optimización de Costos | Consolidación de activos, negociación de contratos favorables, **eliminación de activos obsoletos o subutilizados**, prácticas de gestión más eficientes. Maximizar el ROI |
| 6 | Disposición de Activos al Final de su Vida Útil | Eliminación **segura y responsable**, cumplimiento de requisitos legales y regulatorios, y **minimización del impacto ambiental negativo** |

**KPIs (tabla completa; el apunte los presenta unificados para ambas prácticas):**

| KPI | Descripción |
|---|---|
| Frecuencia de verificación | Frecuencia de verificaciones **físicas** del contenido de la CMDB |
| Duración de verificación | Duración promedio de verificaciones físicas del contenido de la CMDB |
| Esfuerzo para verificaciones | Promedio de esfuerzo de trabajo para verificaciones físicas del contenido de la CMDB |
| Cobertura CMS *(el PDF convertido dice "Cubiertas CMS"; se lee como cobertura — (inferencia))* | Porcentaje de elementos de configuración cuyos datos están incluidos en la CMDB |
| Actualización automática | Porcentaje de CI cuyos datos en la CMDB se actualizan automáticamente |
| Cantidad de desvíos | Número de ocasiones en que las auditorías de configuración detectaron incorrecciones en el contenido de la CMDB |
| CI involucrados en incidentes | Cantidad de CI que han estado involucrados en incidentes |
| Configuraciones no autorizadas | Cantidad de configuraciones detectadas en controles y auditorías que **no fueron autorizadas o no cuentan con licencias** |
| Costos asociados | Costos asociados a las actividades de Gestión de la Configuración y Activos de Servicio |

###### 5.8 Gestión de Versiones

- **Qué es:** la encargada del **control de calidad de todo el software y hardware instalado en el entorno de producción**.
- **Colabora** estrechamente con el **Control de Cambios** y las Gestiones de **Configuración del Servicio** y de **Activos de TI** para asegurar que toda la información relativa a las nuevas versiones se integre adecuadamente en la **CMDB**, de forma que ésta ofrezca una imagen real de la configuración de la infraestructura.
- Mantiene actualizadas la **DML** y los **DS**.

**Conceptos básicos:**

| Concepto | Definición |
|---|---|
| **Versión** | Un **nuevo grupo de CIs o un grupo de CIs modificados que han sido validados para su instalación en el entorno de producción**. Sus especificaciones funcionales y técnicas están determinadas en la **RFC** correspondiente |
| **DML** — Biblioteca de Medios Definitivos | Debe contener copia de **todo el software instalado** en el entorno TI: no solo sistemas operativos y aplicaciones, sino también **controladores de dispositivos y documentación asociada**. Debe contener el **histórico completo de versiones** de un mismo software, para proporcionar la versión necesaria si hay que implementar planes de **back-out**. Debe almacenarse en un **entorno seguro** y conviene realizar **back-ups periódicos** |
| **DS** — Almacén de Recambios Definitivos | Contiene **piezas de repuesto** para los CIs en el entorno de producción (y documentación para la rápida reparación de problemas de hardware) |

**Clasificación de versiones según su impacto en la infraestructura TI + nomenclatura:**

| Tipo | Definición | Numeración |
|---|---|---|
| **Versiones mayores** | Representan **importantes despliegues de software y hardware** e introducen modificaciones importantes en la funcionalidad, características técnicas, etc. | 1.0, 2.0, etc. |
| **Versiones menores** | Suelen implicar la **corrección de varios errores conocidos puntuales**; a menudo implementan, de manera correctamente documentada, **soluciones de emergencia** | 1.1, 1.2, 1.3, etc. |
| **Versiones de emergencia** | Modificaciones que **reparan de forma rápida un error conocido** | 1.1.1, 1.1.2, etc. |

El apunte llama a este esquema **"el sistema universalmente aceptado"** para identificar unívocamente las versiones.

**KPIs de Gestión de Versiones (tabla completa):**

| KPI | Descripción |
|---|---|
| Cantidad de versiones | Cantidad de versiones desplegadas en el área de producción de TI, agrupadas en mayores, menores o de emergencia |
| Cantidad de back-outs | Cantidad de versiones que fueron revertidas y **razones** |
| Cantidad de incidentes | Cantidad de incidentes asociados a nuevas versiones |
| Cumplimiento de plazos | Cumplimiento de los plazos previstos para cada despliegue |
| Duración de Versiones Mayores | Duración media de versiones mayores, desde su autorización hasta su finalización |
| Proporción de versiones con despliegue automático | Proporción de nuevas versiones distribuidas automáticamente |
| Utilización de recursos | Asignación de recursos para el despliegue de versiones |
| Disponibilidad del Servicio | Disponibilidad del servicio **durante y tras** el proceso de lanzamiento de la nueva versión |

---

##### 6. Servicios de TI: catálogo, SLA, OLA, UC — qué dice y qué NO dice el apunte

Este punto hay que tenerlo claro porque es un hueco del material, no un olvido de la wiki.

**Lo que el apunte SÍ dice sobre SLA:**

| Contexto | Qué afirma |
|---|---|
| Registro de incidentes | El Centro de Servicios evalúa en primera instancia **si el servicio requerido se incluye en el SLA del cliente**; si no, lo reenvía a una autoridad competente |
| Urgencia | La urgencia depende del tiempo máximo de demora que acepte el cliente **y/o el nivel de servicio acordado en el SLA** |
| Monitorización | El tiempo de resolución del incidente se estima **en base al SLA correspondiente y la prioridad** |
| KPI | "Resolución dentro del SLA": porcentaje de incidentes resueltos dentro del tiempo acordado en el SLA |
| Control de errores | Al evaluar soluciones a errores conocidos hay que considerar **sus consecuencias sobre los SLA** |
| Definición de cliente | El cliente es quien está **autorizado a acordar** con la organización de TI y es responsable de que se entreguen los niveles de servicio que se pagan |
| Rol del acuerdo | *"Que el servicio complete las expectativas del cliente depende de **cómo se hayan acordado los niveles de servicio** más que de cómo el proveedor lo haya realizado"* |
| Taxonomía SEI de riesgos | El ítem **3.1.7 "Acuerdo de Nivel de Servicio"** figura como fuente de riesgo dentro de "Fallas de Procesos Internos → Diseño de Procesos y Ejecución" |

**Lo que el apunte SÍ dice sobre catálogo de servicios:**
- **"Gestión del catálogo de servicios"** figura como una de las 17 prácticas de gestión de servicio de ITIL 4 (solo el nombre, sin desarrollo).
- Los **portales de servicios y aplicaciones móviles** del Centro de Servicios están *"respaldados por **catálogos de solicitudes y servicios** y bases de conocimientos"*.

**Lo que el apunte NO dice — hueco a cubrir con otra fuente:**
- **No define SLA** (Service Level Agreement) formalmente: lo usa siempre como concepto ya conocido.
- **No menciona OLA** (Operational Level Agreement) ni **UC / Underpinning Contract** en ningún lugar del documento. La cadena SLA → OLA → UC **no está en este apunte**.
- **No define ni estructura el catálogo de servicios** (ni distingue catálogo de negocio vs. catálogo técnico).
- **No desarrolla la práctica "Gestión del nivel de servicio"**, aunque la nombra en la tabla de las 34 prácticas y la menciona al pasar dos veces (coordinación con Control de Cambios; perspectivas a incorporar en la definición de umbrales de monitoreo).

*(Inferencia, para el TP Integrador):* si el TP pide definir catálogo de servicios y SLA/OLA/UC, hay que traerlo de la bibliografía complementaria o de ITIL 4 directamente, y dejar constancia de que no sale de este apunte.

---

##### 7. Estructura y funciones del área de TI: qué aporta el apunte

**Advertencia:** pese al nombre del archivo ("AreasTI"), **el apunte no presenta un organigrama del área de TI ni una lista de áreas típicas** (tipo desarrollo / operaciones / infraestructura / soporte / seguridad / datos). Lo que aporta es una estructura **por procesos, líneas de soporte y roles**, coherente con la premisa de que *"ITIL no dicta cómo la organización debe ser estructurada, sino que define las relaciones entre las actividades en los procesos"*.

###### 7.1 Estructura por líneas de soporte (lo más cercano a un organigrama que da el material)

| Línea | Quién / qué | Responsabilidad |
|---|---|---|
| **1ª línea** | **Centro de Servicios de TI / Mesa de Ayuda** | Único punto de contacto del usuario final para **incidentes y solicitudes**; registro, clasificación, priorización, resolución con KB, comunicación al usuario, cierre; también informa a los usuarios sobre los cambios futuros |
| **2ª línea** | Especialistas (**escalado funcional**); *"puede ser personal abocado a la Gestión de Problemas"* | Resolución de lo que la 1ª línea no puede; investigación de causas |
| **2ª / 3ª línea** | **Personal técnico con competencias específicas** | **Gestión y Monitorización de Eventos** — explícitamente **no puede ser realizada por el Centro de Servicios** |
| **Eje jerárquico** (transversal) | Responsables con mayor autoridad (**escalado jerárquico**) | Decisiones que escapan a las atribuciones del nivel, p. ej. **asignar más recursos** |

###### 7.2 Roles y órganos que el apunte sí define

| Rol / órgano | Práctica | Responsabilidad |
|---|---|---|
| **Gestor de Cambios** | Control de Cambios | Responsable del proceso de cambio; preside el CAB; en grandes organizaciones dispone de asesores por área; puede decidir cambios de emergencia si es imposible demorar |
| **CAB** (Consejo Asesor de Cambios) | Control de Cambios | Órgano interno con representantes de las principales áreas de la gestión de servicios TI; puede incluir consultores externos, grupos de usuarios y proveedores de SW/HW. **Aprueba** los cambios |
| **ECAB** | Control de Cambios | Comité de emergencia para cambios urgentes |
| **Cliente** | Transversal | Autorizado a acordar con TI; responsable de asegurar que se entreguen los niveles de servicio pagados |
| **Usuario** | Transversal | Empleado que usa los servicios de TI en sus actividades rutinarias |
| **Propietario / Dueño del Activo** | Gestión de Riesgos (pág. 9) | Individuo con **responsabilidad principal de la viabilidad y capacidad de supervivencia del activo** |
| **Custodio del Activo** | Gestión de Riesgos (pág. 9) | Cualquier persona con **responsabilidad de proteger un activo de información** mientras se almacena, transporta o procesa. Vinculado al activo de soporte y a su contenedor |
| **SOC** (Centro de Operaciones de Seguridad) | Anexo II | Estructura que las organizaciones implementan (o tercerizan) para **monitorear y responder a posibles incidentes** de ciberseguridad |
| Personal de **infraestructura, aplicaciones, propietarios de servicios, gestión del nivel de servicio** | Gestión de Eventos | Perspectivas a incorporar en la definición de estrategias de monitoreo, umbrales y criterios de evaluación |

###### 7.3 Funciones del área de TI que se desprenden del material

De las prácticas desarrolladas, las funciones concretas que el apunte adjudica al área (inferencia de agrupamiento; los contenidos son textuales):

1. **Soporte al usuario**: Centro de Servicios, gestión de incidentes, gestión de solicitudes.
2. **Vigilancia técnica**: monitorización y gestión de eventos, con herramientas activas y pasivas y correlación automatizada.
3. **Análisis de causa raíz**: gestión de problemas reactiva y proactiva, control de errores.
4. **Gobierno del cambio**: control de cambios, CAB/ECAB, planes de back-out, PIR.
5. **Control del inventario técnico**: gestión de la configuración del servicio (CMDB, CI, baselines, auditorías).
6. **Administración económica de los activos**: gestión de activos de TI (adquisición, licencias, optimización de costos, disposición final).
7. **Control de calidad de producción**: gestión de versiones, DML, DS.
8. **Gestión de riesgos y continuidad**: ver Parte B.

---

##### 8. Puente ITSM ↔ Gestión de Riesgos (para no duplicar con la Parte B)

El apunte teje explícitamente estos vínculos; conviene tenerlos a mano porque es el eje conceptual de la unidad:

| Elemento ITSM | Rol en la Gestión de Riesgos (textual del apunte) |
|---|---|
| **Incidente comunicado por el usuario** | Disparador que **alerta la materialización de un riesgo** que debería haber sido identificado |
| **Solución temporal / solución permanente** | Son los **planes de contingencia y recuperación** que deben activarse |
| **Incidente que afecta procesos críticos** | Probablemente deba activarse el **Plan de Continuidad de Negocio** |
| **Evento de advertencia** | Disparador para **Estrategias de Tratamiento** |
| **Evento de excepción** | Disparador de **Planes de Contingencia** |
| **Evento informativo** | Insumo posterior para la Gestión de Problemas |
| **Estrategias de tratamiento** | Se implementan como **controles ISO 27002:2022** de tipo **Preventivo**, ligados a todas las propiedades de seguridad de la información y al concepto de ciberseguridad **Proteger**; las **capacidades operacionales** permiten asignar responsabilidades y lineamientos de implementación |
| **Controles preventivos / detectivos / correctivos** | Preventivos → estrategias de tratamiento; detectivos → planes de contingencia y continuidad; correctivos → planes de recuperación |
| **Gestión de riesgos** (ITIL 4) | Es una de las 14 prácticas de **gestión general** del SVS |
| **Gestión de la continuidad del servicio** (ITIL 4) | Es una de las 17 prácticas de **gestión de servicio** |

---

##### 9. Dudas / pendientes de esta parte

- **Figuras perdidas en la conversión del PDF.** No hay texto recuperable de: (a) la figura de los 4 temas de ISO 27002:2022 (pág. 5), (b) el cuadro de correspondencia procesos ITIL v3 ↔ prácticas ITIL 4 (pág. 27), (c) el diagrama del proceso de ISO 31000:2018 (pág. 4). Los diagramas de riesgos (matriz de severidad, taxonomía FAIR, RBS del PMI, cadena de planes con RPO/RTO/WRT) también vinieron degradados — eso lo tiene que resolver la Parte B.
- **ITIL 4 fechado en "febrero de 2022"** por el apunte. La versión ITIL 4 fue publicada originalmente en 2019 *(conocimiento general, no está en el material)*. Puede ser un error del apunte o referirse a una actualización específica. Si aparece en un parcial, responder con la fecha del apunte.
- **"Cubiertas CMS"** en la tabla de KPIs de configuración: probable error de conversión de "Cobertura CMS" o "Cobertura CMDB". El texto de la descripción sí es claro.
- **No hay desarrollo de ISO 20000**, pese a ser la norma certificable de ITSM. Solo se la nombra.
- **No hay SLA/OLA/UC ni catálogo de servicios desarrollados** (ver punto 6). Hueco a cubrir para el TP Integrador.
- **No hay organigrama ni áreas típicas de TI** (ver punto 7). Si el TP pide estructurar un área de TI, hay que armarla desde las líneas de soporte + prácticas ITIL, o traer otra fuente.
- **La práctica "Asistencia al cliente"** figura en la tabla de las 34 prácticas pero no se desarrolla; es la que en ITIL 4 corresponde al Service Desk *(inferencia)*, y el apunte trata el Centro de Servicios como sección propia sin nombrar esa correspondencia.


---


##### PARTE B — Gestión de Riesgos (Unidad 2)

> Fuente única de esta parte: *Apunte "Administración de Recursos en Áreas de Sistemas de Información" — Unidad 2*, Esp. Lic. Fabiana María Riva (UTN FRRo), págs. 1–20 y Anexos I y II. Todo lo que no esté marcado como "(inferencia)" sale textualmente del apunte.

---

###### B.0 Encuadre: por qué la Gestión de Riesgos está en esta Unidad

El Sistema de Gobierno de TI de COBIT 2019 evalúa, dirige y monitoriza (**EDM**) sobre cinco objetivos:

1. Asegurar el establecimiento y mantenimiento del Marco de Gobierno
2. Asegurar la Obtención de Beneficios
3. **Asegurar la Optimización del Riesgo**
4. **Asegurar la Optimización de los Recursos**
5. Asegurar el compromiso de las partes interesadas

La Unidad 2 desarrolla los objetivos 3 y 4. El objetivo 3 (Optimización del Riesgo) es esta Parte B: amplía el concepto de riesgo de TI de la Unidad 1 entrando en Seguridad de la Información. El objetivo 4 (Optimización de Recursos) es la Gestión de Servicios de TI / ITIL 4 (Parte C). El foco transversal en ambos: **mantener la continuidad de los procesos críticos y claves de la organización**.

La Gestión de Riesgos es **parte integrante del PETI**, no un anexo. El Gobierno de TI requiere información de la evolución del PETI en términos de indicadores; entre ellos, indicadores de riesgo.

---

###### B.1 Seguridad de la Información: definición y dimensiones

**Seguridad de la información** = *el proceso de planear, organizar, coordinar, dirigir y controlar las actividades relacionadas a asegurar la seguridad de la información de una organización en todas sus dimensiones: integridad, confidencialidad y disponibilidad.*

| Dimensión | Definición del apunte | Núcleo operativo |
|---|---|---|
| **Integridad** | Que la información solo pueda ser modificada por entidades autorizadas, minimizando corrupción por fallas físicas o lógicas, de hardware o software, malware, o alteraciones de usuarios internos o intrusos, con o sin intención de daño | Mantener la **exactitud y completitud** de la información y de sus métodos de proceso |
| **Confidencialidad** | Característica de almacenamiento y transmisión que posibilita que la información sea conocida y manipulada solo por personas autorizadas. Aplica a datos personales y datos sensibles (bases de datos de empresas, relación con empleados y clientes, datos médicos, ámbito jurídico) | Garantizar la **privacidad** de la información y de su tratamiento, previniendo divulgación no autorizada **almacenada o en tránsito** |
| **Disponibilidad** | Garantizar que los recursos (información, sistemas, almacenamiento) sean **accesibles y utilizables** por los usuarios o procesos autorizados **cuando estos lo requieran** | — |

**No repudio**: principio en que se apoya la confidencialidad. Es *la capacidad de demostrar o probar la participación de las partes (origen y destino, emisor y receptor, remitente y destinatario), mediante su identificación, en una comunicación o en la realización de una determinada acción*. Requiere mecanismos de **identificación, autenticación y trazabilidad**.

**Seguridad de la Información ≠ Ciberseguridad (Seguridad Informática)**

| | **Ciberseguridad / Seguridad Informática** | **Seguridad de la Información** |
|---|---|---|
| Alcance | Protección de los **sistemas informáticos**: información en medios magnéticos + aplicaciones (software) + equipos que la soportan (hardware) + personas que la usan (usuarios) | Amplía la visión técnica: **todas** las personas, procesos, funciones y activos de **toda** la organización |
| Enfoque | Aspecto **técnico**. Análisis de riesgos basado en activos de los sistemas informáticos, sus vulnerabilidades y las amenazas a las que se exponen | Riesgos **organizacionales, operacionales y físicos** |
| Medidas | Implementa **salvaguardas** para mantener los riesgos en un nivel aceptable | Hincapié en el **factor humano**: las medidas requieren modificar comportamientos y actitudes, que suelen chocar con la resistencia al cambio |
| Prerrequisito | — | Políticas de seguridad de la información, que guían el proceso de Gestión de Riesgos |

**Riesgos típicos de cada ámbito** (reconstruido de una figura mal convertida; el original venía con las letras separadas):

| Riesgos del ámbito **Seguridad de la Información** | Riesgos del ámbito **Ciberseguridad** |
|---|---|
| Falta de políticas de tratamiento de la información | Ataques utilizando tecnologías, malware |
| Errores, actos deliberados del personal | Falta de políticas de resguardo |
| No realización de la gestión correcta de cambios | Desconocimiento de posibles riesgos |
| Controles insuficientes | |

---

###### B.2 Documentos de referencia

Interesan en dos frentes: **(1)** metodologías del proceso en sí, identificación de riesgos y su tratamiento; **(2)** mecanismos para actuar ante la materialización de un riesgo (contingencia, recuperación y continuidad de las operaciones).

| Documento | Qué aporta |
|---|---|
| **COBIT 2019** | Objetivo de **Gestión** *Gestionar el Riesgo*, dominio **APO** (Alinear, Planificar y Organizar). Define el proceso con 6 prácticas (ver B.3) |
| **ISO 31000:2018 — Gestión del Riesgo. Directrices** | Principios y guías **genéricas** de gestión de riesgos. COBIT 2019 está alineado a esta norma. *(El diagrama del proceso ISO 31000 es una figura que no sobrevivió la conversión del PDF)* |
| **MAGERIT v.3** (Metodología Automatizada de Análisis y Gestión de Riesgos de los Sistemas de Información de las Administraciones Públicas de España) | Método formal para investigar riesgos de los SI y recomendar medidas. 3 libros. **Libro I**: proceso de Gestión de Riesgos basado en ISO 31000 + método de análisis de riesgos **basado en identificación de activos**. **Libro II**: catálogo de elementos (amenazas) |
| **ISO 27001:2022** (única **certificable** de la serie) | Aplicable a todo tipo y tamaño de organización. Marco para el **SGSI**: coordina definición de políticas, objetivos y alcance de la seguridad; análisis, valorización y tratamiento de riesgos sobre los activos; controles y su monitorización; y mejoras |
| **ISO 27002:2022** — "Seguridad de la información, ciberseguridad y protección de la privacidad – Controles de seguridad de la información" | Actualiza la versión 2013. **93 controles** agrupados en 4 temas, con atributos (ver abajo) |
| **ISO 27005:2022** | Recomendaciones y directrices generales para **establecer el proceso de Gestión de Riesgos** |
| **NIST 800-34** | Planes de contingencia y recuperación (ver B.11) |
| **ISO 22301 / BS 25999** | Gestión de la Continuidad del Negocio – BCM (ver B.11) |
| **FAIR** (Factor Analysis Information Risk) | Comunidades de amenazas + taxonomía para estimar probabilidad e impacto |
| **PMI** | Estructura de desglose de riesgos (RBS) en proyectos; concepto dual riesgo = amenaza + oportunidad; reservas |
| **SEI** | *Taxonomy of Operational Cyber Security Risks*; *Software Development Risk Taxonomy* |

> Las normas ISO 27000 **no establecen metodologías específicas**, por lo que se complementan con otros marcos.

**Atributos de los 93 controles de ISO 27002:2022**

| Atributo | Valores posibles |
|---|---|
| **Tipo de Control** | Preventivo, Detectivo, Correctivo |
| **Propiedades de Seguridad de la Información** | Confidencialidad, Integridad, Disponibilidad |
| **Conceptos de Ciberseguridad** (5 funciones del marco NIST) | Identificar, Proteger, Detectar, Responder, Recuperar |
| **Capacidades operacionales** | Clasifican los controles desde una perspectiva práctica que permite **asignar responsabilidades y establecer lineamientos de implementación** |
| **Dominios de seguridad** | Gobernanza y ecosistema, Protección, Defensa, Resiliencia (conjunto de bienes y recursos sujetos a una política de seguridad común) |

> **Faltante del material**: el apunte dice "Los cuatro temas diferenciados por la norma se muestran en la siguiente figura" — esa figura **no se convirtió**. Los nombres de los 4 temas no están en el texto extraído. *(inferencia, conocimiento general fuera del apunte: ISO 27002:2022 agrupa en Organizativos, de Personas, Físicos y Tecnológicos — verificar contra el PDF original antes de usarlo en el TP.)*

---

###### B.3 Definiciones núcleo

| Concepto | Definición según el apunte |
|---|---|
| **Gestión de Riesgos** | *Proceso **iterativo** basado en el conocimiento, evaluación y manejo de los riesgos, con el propósito de mejorar la toma de decisiones organizacionales; aplicable a cualquier situación donde un resultado no deseado o inesperado pueda ser significativo o donde se identifiquen oportunidades* |
| **Riesgo** (ISO 31000) | *El **efecto de la incertidumbre sobre el logro de los objetivos**, donde efecto es un desvío respecto a lo esperado (ya sea positivo o negativo)* |
| **Riesgo — concepto dual** (COBIT 2019 y PMI) | Resultados positivos = **Oportunidades**; resultados negativos = **Amenazas**. Objetivo de la Gestión de Riesgos del Proyecto: *aumentar la probabilidad y el impacto de los eventos positivos, y disminuir la probabilidad y el impacto de los eventos adversos* |
| **Activo** | *Los **recursos necesarios** para que una organización o proceso de ésta **funcione correctamente y alcance sus objetivos*** |
| **Impacto** | *Las **consecuencias** de un evento o incidente (efecto de amenazas/oportunidades explotando las vulnerabilidades/fortalezas de los activos)* |
| **Probabilidad** | *La **incertidumbre** de que ese evento o incidente se produzca o no, ya que el riesgo es algo que todavía no ha ocurrido* |
| **Severidad / Exposición / Estado del riesgo** | `SEVERIDAD = PROBABILIDAD × IMPACTO` |
| **Riesgo inherente** (comúnmente mencionado solo como "riesgo") | *El riesgo que se presenta **sin aplicar ninguna medida** sobre las amenazas (u oportunidades), vulnerabilidades, impacto o probabilidad; es decir, sin aplicar ninguna estrategia para disminuir (o aumentar) su severidad* |
| **Riesgo residual** (o remanente) | La severidad **recalculada después de aplicar las estrategias de tratamiento**, ya que probabilidad e impacto pueden haber variado. Es *el riesgo que estaremos dispuestos a aceptar* / *el nivel de riesgo que la organización está dispuesta a aceptar y para el que deberán plantearse los planes de contingencia, recuperación y continuidad de negocio* |
| **Salvaguardas** | Medidas de seguridad que se implementan para *mantener los riesgos en un nivel aceptable* |

> **Regla explícita del apunte sobre riesgo residual**: *"La **especificación del riesgo no ha variado**, solo el valor de su severidad."* No se reescribe el riesgo; se recalcula su número.

> **Carácter continuo**: *"El análisis de riesgos no es algo estático que se realiza por única vez. Debe ser una actividad continua ya que tanto los activos, como sus vulnerabilidades y las amenazas van cambiando con el tiempo."*

**Amenaza y vulnerabilidad — advertencia**

El apunte **no da una definición literal** de *amenaza* ni de *vulnerabilidad*; las usa operativamente. De su texto se desprende:

- **Amenaza**: aquello que, al materializarse, produce consecuencias sobre un activo explotando sus vulnerabilidades. Puede provenir de un atacante *"que puede contar con recursos o no para materializar el ataque"*. Se clasifica por **origen** (MAGERIT) o por **comunidad de amenaza** (FAIR).
- **Vulnerabilidad**: la condición del activo que la amenaza **aprovecha**. En FAIR es una variable derivada: **Vulnerabilidad = f(Capacidad de las Amenazas, Capacidad de Resistencia [controles])**.
- La figura "Conceptos asociados a la Gestión de Riesgos" — que era la que graficaba estas relaciones — **no se convirtió del PDF**. Es un faltante a cubrir con el PDF original.

---

###### B.4 El proceso de Gestión de Riesgos — COBIT 2019, objetivo *Gestionar el Riesgo* (APO)

Seis prácticas. El apunte desarrolla en el cuerpo solo las tres marcadas con ★; el resto está en el Anexo I.

| # | Práctica | Definición COBIT |
|---|---|---|
| 1 ★ | **Recopilar datos** | Integrar la gestión del riesgo empresarial relacionado con la TI con la gestión del riesgo empresarial global, y equilibrar los costos y beneficios de la gestión del riesgo empresarial relacionado con las TI |
| 2 ★ | **Analizar el riesgo** | Desarrollar una visión fundamentada del riesgo de TI vigente, que soporte las decisiones de riesgo |
| 3 | **Mantener un perfil de riesgo** | Mantener un inventario de los riesgos conocidos y los atributos de riesgo, incluidos la frecuencia esperada, impacto potencial y respuestas. Documentar los recursos, capacidades y actividades de control actuales relacionados con elementos de riesgo |
| 4 | **Articular el riesgo** | Comunicar de manera oportuna información sobre el estado actual de las exposiciones y oportunidades relacionadas con TI a todas las partes interesadas requeridas para obtener una respuesta apropiada |
| 5 | **Definir un portafolio con acciones de gestión de riesgos** | Gestionar las oportunidades para reducir el riesgo a un nivel aceptable como un portafolio |
| 6 ★ | **Responder al riesgo** | Responder de manera oportuna a eventos de riesgo materializados con medidas eficaces para limitar la magnitud de las pérdidas |

**Orden operativo que sigue el apunte (secuencia de trabajo para el TP)**

```
1. Recopilar datos
   1.1 Identificación de Activos (método MAGERIT v3)
   1.2 Identificación de Amenazas y Vulnerabilidades
   1.3 Taxonomías para identificación de riesgos
2. Analizar el riesgo
   2.1 Valoración: Severidad = Probabilidad × Impacto  →  RIESGO INHERENTE
   2.2 Priorización (ordenar por severidad decreciente + Pareto 80-20)
3. Responder a los riesgos
   3.1 Definir controles (preventivos / detectivos / correctivos)
   3.2 Estrategias de tratamiento  →  recalcular severidad  →  RIESGO RESIDUAL
   3.3 Reservas (gerenciales / de contingencia)
   3.4 Planes de contingencia, recuperación y continuidad de negocio (sobre el residual)
[iterar]
```

**Entregables identificables (inferencia, a partir de los artefactos que el apunte nombra)**

| Etapa | Entregable |
|---|---|
| Recopilar datos | **Inventario de activos** (con propietario, contenedor, custodio, origen, acceso, dependencias) |
| Recopilar datos | Catálogo de amenazas y vulnerabilidades por activo |
| Recopilar datos | Taxonomía de riesgos adoptada (SEI / PMI-RBS / MAGERIT / FAIR) |
| Analizar el riesgo | **Tabla de riesgos inherentes** (Id, Especificación, Categoría, Probabilidad, Impacto, Severidad, ΣSeveridad) ordenada decreciente + corte de Pareto |
| Responder | Tabla de tratamiento: estrategia + controles + severidad recalculada = **riesgo residual** |
| Responder | Planes de contingencia, recuperación y continuidad de negocio |
| Responder | Presupuesto de reservas (gerenciales y de contingencia) |
| Continuo | **Perfil de riesgo agregado** + conjunto de **indicadores de riesgo** (Anexo I, práctica 3) |

**Detalle completo del Anexo I — actividades por práctica**

**Recopilar datos**
1. Establecer y mantener un método para la recogida, clasificación y análisis de datos relacionados con el riesgo de TI.
2. Registrar datos relevantes y significativos relacionados con los riesgos de TI en el entorno operativo interno y externo de la empresa.
3. **Adoptar o definir una taxonomía de riesgo** para las definiciones consistentes de escenarios de riesgo y categorías de impacto y probabilidad.
4. Registrar datos de **eventos, incidentes o problemas** de riesgo que han causado o podrían causar impacto en el negocio conforme a las categorías de impacto definidas en la taxonomía de riesgo.
5. Estudiar y analizar los datos históricos de riesgo de TI y de pérdidas experimentadas a partir de datos y tendencias externos disponibles, homólogos de la industria a través de logs de eventos de la industria, bases de datos y acuerdos de la industria para la publicación común de eventos.
6. Para clases de eventos similares, organizar los datos recopilados y **resaltar los factores causantes**.
7. Determinar las condiciones específicas que existieron o estuvieron ausentes cuando tuvieron lugar los eventos de riesgo y cómo afectaron a la frecuencia del evento y la magnitud de la pérdida.
8. Realizar un análisis periódico de eventos y factores de riesgo para identificar riesgos nuevos o emergentes.

**Analizar el riesgo**
1. Definir el alcance adecuado de los esfuerzos en análisis de riesgos, considerando todos los factores de riesgo y/o la **criticidad de los activos** para el negocio.
2. Crear y actualizar regularmente los **escenarios de riesgo de TI**; las exposiciones a pérdidas relacionadas con TI; y los escenarios de riesgo reputacional, incluidos escenarios compuestos de tipos de amenazas y **eventos en cascada y/o coincidentes**. Desarrollar previsiones para actividades de control específicas y capacidades de detección.
3. **Estimar la frecuencia (o probabilidad) y la magnitud de la pérdida o ganancia** asociada con escenarios de riesgo de TI. Evaluar controles operativos conocidos.
4. **Comparar el riesgo actual con el apetito al riesgo y la tolerancia de riesgo aceptable.** Identificar el riesgo inaceptable o elevado.
5. Proponer respuestas al riesgo para riesgos que excedan el apetito al riesgo y los niveles de tolerancia.
6. Especificar los requisitos de alto nivel para los proyectos o programas que implementarán las respuestas seleccionadas. Identificar requisitos y expectativas para los **controles clave**.
7. Validar el análisis de riesgo y los resultados del **análisis de impacto del negocio (BIA)** antes de usarlos en la toma de decisiones. Comprobar que los sesgos de las estimaciones se calibraron y analizaron adecuadamente.
8. **Analizar el costo/beneficio** de las opciones de respuesta: evitar, reducir/mitigar, transferir/compartir, aceptar y explotar/aprovechar. Confirmar la respuesta óptima.

**Mantener un perfil de riesgo**
1. Inventariar los procesos de negocio y documentar su dependencia con los procesos de gestión de servicios de TI y los recursos de infraestructura. Identificar personal de apoyo, aplicaciones, infraestructura, instalaciones, registros manuales críticos, contratistas, proveedores y terceros.
2. Determinar y acordar qué servicios y recursos de infraestructura de TI son **esenciales** para sostener los procesos de negocio. Analizar dependencias e identificar **eslabones débiles**.
3. Agregar los escenarios de riesgo actuales por categoría, línea de negocio y área funcional.
4. Capturar regularmente la información del perfil de riesgo y consolidarla en un **perfil de riesgo agregado**.
5. Capturar información del estado del plan de acción de riesgos.
6. Definir un conjunto de **indicadores de riesgo** que permitan identificación y monitorización rápida del riesgo actual y sus tendencias.

**Articular el riesgo**
1. Informar los resultados del análisis a las partes interesadas en términos y formatos útiles para decisiones empresariales, incluyendo probabilidades y rangos de pérdidas o ganancias con **niveles de confianza**.
2. Proporcionar a los decisores la comprensión de los **escenarios más probables y peores**, exposiciones a pérdidas, y consideraciones reputacionales, legales y regulatorias.
3. Informar el perfil de riesgo actual: eficacia del proceso de gestión de riesgos, eficacia del control, brechas, inconsistencias, redundancias, estado de remediación e impactos en el perfil.
4. Periódicamente, en áreas con riesgos y capacidades similares, identificar oportunidades que permitirían **aceptar un riesgo mayor** a cambio de mayor crecimiento y retorno.
5. Revisar resultados de evaluaciones objetivas de terceros y revisiones de auditoría interna y de aseguramiento de la calidad; incluirlos en el perfil de riesgo.

**Definir un portafolio con acciones de gestión de riesgos**
1. Mantener un **inventario de las actividades de control** implantadas para mitigar el riesgo. Clasificarlas y asignarlas a escenarios de riesgo de TI específicos y agregados.
2. Determinar si cada entidad organizativa monitoriza el riesgo y acepta la responsabilidad de actuar dentro de los niveles de tolerancia individuales y del portafolio.
3. Definir un conjunto **equilibrado** de propuestas de proyectos para reducir el riesgo y/o habilitar oportunidades estratégicas, considerando costos, beneficios, efecto en el perfil de riesgo y regulaciones.

**Responder al riesgo**
1. **Preparar, mantener y probar planes** que documenten los pasos a dar cuando un evento de riesgo pudiera causar un incidente significativo de desarrollo u operativo con impacto grave. Los planes deben incluir **vías de escalamiento**.
2. Aplicar el plan de respuesta adecuado para minimizar el impacto cuando ocurren incidentes de riesgo.
3. Clasificar los incidentes y comparar las exposiciones a pérdidas con los **umbrales de tolerancia**. Comunicar impactos de negocio a los decisores.
4. Examinar eventos adversos/pérdidas y oportunidades pasadas no consideradas y **determinar las causas raíz**.
5. Comunicar causa raíz, requisitos adicionales de respuesta y mejoras del proceso a los decisores, asegurando que se incluyan en los procesos de gobierno del riesgo.

> **Apetito al riesgo** y **tolerancia al riesgo** aparecen únicamente en el Anexo I (como referencia contra la cual se compara el riesgo actual). El apunte **no los define** en el cuerpo.

---

###### B.5 Recopilar datos — Identificación e inventario de activos (método MAGERIT v3)

> *"Se deberán determinar los **riesgos inherentes** y documentar sus características, para lo cual utilizaremos el método basado en la identificación de activos propuesto por Magerit V3."*

**Por qué inventariar**: *permite la identificación de activos y componentes críticos y es esencial para conocer qué debe protegerse.* La **tipificación** de los activos es a la vez información documental de interés y criterio para (a) la posterior identificación de amenazas potenciales y vulnerabilidades, y (b) establecer **controles apropiados a la naturaleza del activo**.

**Cuadro de dependencias entre activos**

Reconstrucción de la figura (venía con las letras espaciadas). La flecha "Dependencia" corre de arriba hacia abajo: los niveles superiores **dependen** de los inferiores.

| Nivel | Elementos |
|---|---|
| 1 (superior) | Misión, Objetivos, Credibilidad, Imagen |
| 2 | Procesos, Bienes y Servicios Producidos |
| 3 | **Activos de Información** |
| 4 | **Activos de Soporte**: Hardware, Software |
| 5 (base) | Equipamiento, Instalaciones, Servicios, Personas |

**Procedimiento de identificación de activos (5 pasos)**

| Paso | Actividad |
|---|---|
| 1 | **Identificación del Contexto** |
| 2 | **Identificación de Activos de Información.** Descripción. Propietario |
| 3 | **Identificación de Contenedores** (o activos de soporte) **y Custodios** |
| 4 | **Identificación de Dependencias entre Activos** |
| 5 | **Identificación de otros Tipos de Activos** (surgen de Activos de Soporte y Dependencias) |

Partiendo del análisis del contexto —para el cual *se debe contar con empleados expertos para la especificación de objetivos de la organización, procesos de negocio y actividades*— se identifican los activos de información que se **procesan, consumen o producen** en el transcurso de esas actividades.

**Regla del esfuerzo adecuado**: se puede recurrir a documentación existente; si no la hay, el esfuerzo debe ser proporcional al objetivo — *"ni una identificación de actividades de bajo nivel (excesivamente detallada) ni de muy alto nivel"*. La misma regla aplica a la identificación de amenazas y vulnerabilidades.

**Campos del inventario de activos**

| Campo | Definición del apunte |
|---|---|
| **Identificador del Activo de Información** | Sirve para registrar el activo y hacer referencias |
| **Nombre** | El nombre del activo como se conoce para la organización |
| **Descripción** | Características del activo. Puede indicarse si es un documento legal o requerido por el propio proceso |
| **Propietario o Dueño del Activo** | *Aquellos individuos que tienen la **responsabilidad principal de la viabilidad y la capacidad de supervivencia** del activo* |
| **Contenedores o Soportes del Activo de Información** | *Concepto que ayuda a **diferenciar el activo de información propiamente dicho de la forma en que se almacena, procesa y distribuye*** |
| **Custodio del Activo** | *Cualquier persona en la organización que tenga la responsabilidad de **proteger** un activo de información **a medida que se almacena, transporta o procesa**. Está vinculado al **activo de soporte y a su contenedor*** |
| **Origen** | Ayuda a identificar **quién tiene la potestad de generar** el Activo de Información. Se deberá identificar si se requiere la identificación de la entidad de origen |
| **Acceso** | Subclasificación según el acceso posible (ver escala abajo) |
| **Dependencias** | *Denominación de todos los activos a partir de los cuales la **materialización de una amenaza tenga como consecuencia efectos en la seguridad del activo de información identificado***. A partir de las dependencias se realizan los inventarios de activos correspondientes, clasificados según convenga a la organización |

**Propietario vs. Custodio — la distinción exacta**

| | **Propietario / Dueño** | **Custodio** |
|---|---|---|
| Objeto sobre el que recae | El **activo de información** | El **activo de soporte y su contenedor** |
| Responsabilidad | Viabilidad y **supervivencia** del activo (responsabilidad principal) | **Protegerlo** mientras se almacena, transporta o procesa |
| Horizonte | Permanente sobre el activo lógico | Ligado al medio concreto por el que el activo pasa |

Un mismo activo de información tiene **un** propietario y puede tener **varios** custodios, uno por cada contenedor por el que circula (inferencia, derivada de que el custodio "está vinculado al activo de soporte y a su contenedor" y de que un activo puede tener varios contenedores).

**Escala de clasificación por Acceso (completa)**

| Nivel | Definición |
|---|---|
| **Público** | Sin requisitos de confidencialidad. Cualquier persona de la organización **o terceros** puede tener acceso |
| **Compartido** | Activos compartidos entre grupos o personas **no pertenecientes** a la organización |
| **Reservado** | Restringido el acceso a los **empleados** de la organización |
| **Confidencial** | Acceso restringido a una **lista específica de personas**. Conviene identificar si la información contiene **datos personales o sensibles** |

**Valoración C/I/D y criticidad**

**Dimensiones de valoración** = *las características o atributos que hacen valioso un activo*. Una dimensión es *una faceta o aspecto de un activo que se podrá utilizar para valorar las consecuencias o impacto de la materialización de una amenaza*.

> *"La valoración que recibe un activo en una cierta dimensión es la **medida del perjuicio para la organización** (sobre sus objetivos, productividad, etc.) si el activo se ve dañado en dicha dimensión."*

*"Las dimensiones de valoración que permiten establecer el **nivel de criticidad** de un activo son:"*

| Dimensión | Criterio de valoración alta |
|---|---|
| **Confidencialidad** | Asociada a la información y derivada del **marco regulador externo** o de **criterios internos**. Alta valoración cuando **su revelación causaría graves daños** a la organización |
| **Disponibilidad** | En función del **número de personas afectadas** por la falta de disponibilidad o por un funcionamiento irregular |
| **Integridad** | Cuando **su alteración, voluntaria o intencionada, causaría graves daños** a la organización |

**Cómo se enlaza con el impacto**: *"para establecer qué valor de la escala corresponde al **impacto** podemos referirnos al **valor que el activo tiene para la organización** o a la **magnitud de la pérdida** que sufriría la misma si fuese afectado dicho activo."*

> **El apunte NO da una fórmula de criticidad.** No define si criticidad = máximo(C, I, D), promedio, suma o matriz. Solo dice que esas tres dimensiones "permiten establecer el nivel de criticidad".
> **(inferencia)** Para el TP, el criterio consistente con el resto del apunte es: valorar cada activo en C, I y D con la misma escala 0–5 usada para impacto, y tomar **criticidad = máx(C, I, D)** — porque el impacto se define como el perjuicio de que el activo *se vea dañado en dicha dimensión*, y basta con que una dimensión se rompa para que el perjuicio se materialice. Dejar explícito el criterio elegido en el informe.

---

###### B.6 Identificación de amenazas y vulnerabilidades

Habiendo identificado los activos, se identifican las **amenazas** que pueden actuar sobre ellos. *"La identificación de amenazas permite además el análisis de las **vulnerabilidades que pueden ser aprovechadas** por dichas amenazas."* El atacante puede contar con recursos o no para materializar el ataque.

**Punto de partida para identificar y clasificar**: examinar (a) la **naturaleza de la organización** (p. ej. la industria en la que está) y (b) las **condiciones que rodean al activo** (su valor, el personal que accede a su uso, su contenedor, las instalaciones donde se encuentra).

Las taxonomías usadas: **Amenazas (MAGERIT)** y **Comunidades de amenazas (FAIR)**. Ambas *"intentan establecer subconjuntos de la población total de amenazas que comparten características claves y proponen metodologías para la identificación y clasificación de las mismas."*

**MAGERIT — clasificación de amenazas por origen**

| Clase | Origen |
|---|---|
| **Desastres naturales** | De origen accidental |
| **De origen industrial** | Del entorno: accidentales, o de origen humano accidentales o deliberados |
| **Errores y fallos no intencionados** | De origen humano |
| **Ataques intencionados** | — |

Para cada amenaza, MAGERIT distingue **qué activos** pueden ser objeto de ella y **a qué dimensión** afecta (confidencialidad, integridad, disponibilidad). Además establece una **correlación** que separa: amenazas que pueden provenir de errores **o** de ataques deliberados / amenazas que **solo** pueden provenir de errores / amenazas que **solo** pueden provenir de ataques deliberados. *(Catálogo completo: MAGERIT Libro II — Catálogo de elementos. No está en este apunte.)*

**FAIR — Comunidades de amenazas**

| Tipo | Comunidades |
|---|---|
| **Internas** | Empleados; contratistas y vendedores; socios |
| **Externas** | Ciberdelincuentes (hackers profesionales); espías de la competencia; hackers no profesionales |

**Características de estas comunidades** (sirven para establecer luego la **probabilidad** de que las amenazas se materialicen):

| Característica | Contenido |
|---|---|
| **Motivación** | Ideología del atacante, ganancia financiera, venganza |
| **Intento primario** | Solo conseguir acceso; dañar; destruir |
| **Patrocinio** | Posibilidad de que exista beneficio (patrocinado o no) para el atacante |
| **Características preferidas del objetivo general** | Entidades o personas que representan una ideología en particular |
| **Objetivos preferidos** | Personas; infraestructura (edificios, comunicaciones, energía, etc.) |
| **Características preferidas del objetivo específico** | Alto perfil, alta visibilidad |
| **Capacidades del atacante** | Varían según el **vector de ataque** o ruta que sigue el atacante para materializar la amenaza |
| **Tolerancia al riesgo** | Consecuencias negativas que el agente de amenaza es capaz de tolerar |

---

###### B.7 Taxonomías para la identificación de riesgos

**Para qué sirven**: *listas de clasificación de riesgos que permiten que el equipo encargado de identificar riesgos pueda pensar con mayor amplitud sobre los mismos, porque ya dispone de una lista de áreas o activos susceptibles de esconder riesgos procedentes de diferentes situaciones.*

Usos adicionales:
- Se usa una **lista de chequeo** basada en una taxonomía con preguntas orientadas a grupos de riesgos, ya que *trabajar con listas muy extensas puede resultar complejo*.
- **Unificar la terminología** que el equipo utiliza para supervisar y notificar el estado de los riesgos a lo largo de un proyecto o en los momentos de control.

Taxonomías de fuentes de riesgo en **proyectos de desarrollo de software**: **Barry Boehm**, **Caper Jones**, y la del **SEI** — *Software Development Risk Taxonomy*. También existen taxonomías para **proyectos de adquisiciones de software**. *(Los documentos específicos están en la carpeta de apuntes complementarios, no en este archivo.)*

**PMI — Estructura de desglose de riesgos (RBS) de proyectos**

> **Faltante**: el apunte dice "El PMI propone la siguiente estructura de desglose de riesgos que pueden darse en Proyectos:" y a continuación va una **figura que no se convirtió**. El contenido de la RBS del PMI **no está disponible** en el texto extraído. Hay que sacarlo del PDF original.

**SEI — *Taxonomy of Operational Cyber Security Risks* (transcripción completa)**

Clasificación para riesgos de la **operación** de tecnologías de información. Organiza la fuente de estos riesgos en **cuatro clases**:

1. **Acciones (o inacción) de las personas**: realizadas tanto deliberada como accidentalmente.
2. **Fallas de los sistemas y tecnología**: fallas del hardware, software y sistemas de información.
3. **Fallas de los procesos internos**: problemas en los procesos internos del negocio que impactan en la habilidad para implementar, gestionar y sostener la seguridad.
4. **Eventos externos**: cuestiones fuera del control de la organización.

| **1. Acciones de las Personas** | **2. Fallas de los sistemas y tecnologías** | **3. Fallas de Procesos Internos** | **4. Eventos externos** |
|---|---|---|---|
| **1.1 Involuntarias**<br>1.1.1 Equivocación (acción incorrecta)<br>1.1.2 Error (por desconocimiento)<br>1.1.3 Omisión (por apresuramiento) | **2.1 Hardware**<br>2.1.1 Capacidad<br>2.1.2 Rendimiento<br>2.1.3 Mantenimiento<br>2.1.4 Obsolescencia | **3.1 Diseño de Procesos y Ejecución**<br>3.1.1 Flujo de Procesos<br>3.1.2 Documentación de Procesos<br>3.1.3 Roles y responsabilidades<br>3.1.4 Notificaciones y alertas<br>3.1.5 Flujo de Información<br>3.1.6 Escalado de problemas<br>3.1.7 Acuerdo de Nivel de Servicio<br>3.1.8 Actividad fuera de control | **4.1 Desastres**<br>4.1.1 Climatológicos<br>4.1.2 Incendios<br>4.1.3 Inundaciones<br>4.1.4 Terremotos<br>4.1.5 Disturbios<br>4.1.6 Pandemias |
| **1.2 Deliberadas**<br>1.2.1 Fraude<br>1.2.2 Sabotaje<br>1.2.3 Robo<br>1.2.4 Vandalismo | **2.2 Software**<br>2.2.1 Compatibilidad<br>2.2.2 Administración de Configuraciones<br>2.2.3 Control de Cambios<br>2.2.4 Parámetros de Seguridad<br>2.2.5 Prácticas de Codificación<br>2.2.6 Testing | **3.2 Control de Procesos**<br>3.2.1 Monitorización del estado<br>3.2.2 Métricas<br>3.2.3 Revisiones Periódicas<br>3.2.4 Propietario o prácticas de gobierno del proceso | **4.2 Cuestiones Legales**<br>4.2.1 Regulaciones<br>4.2.2 Legislación<br>4.2.3 Litigios |
| **1.3 Inacción**<br>1.3.1 Habilidad<br>1.3.2 Conocimiento<br>1.3.3 Guía<br>1.3.4 Disponibilidad | **2.3 Sistemas**<br>2.3.1 Diseño<br>2.3.2 Especificaciones<br>2.3.3 Integración<br>2.3.4 Complejidad | **3.3 Procesos de Soporte**<br>3.3.1 Dotación del Personal<br>3.3.2 Recursos económicos<br>3.3.3 Entrenamiento y desarrollo<br>3.3.4 Otros recursos necesarios de soporte a los procesos | **4.3 Cuestiones del Negocio**<br>4.3.1 Fallas del Suministro<br>4.3.2 Condiciones del Mercado<br>4.3.3 Condiciones Económicas<br><br>**4.4 Dependencias con Servicios**<br>4.4.1 Servicios Públicos / No Públicos<br>4.4.2 Servicios de Emergencia<br>4.4.3 Combustible<br>4.4.4 Transporte |

*(Descripción ampliada: Documento Anexo 3 — Descripción de la Taxonomía SEI, no incluido en este archivo.)*

---

###### B.8 Analizar el riesgo — Valoración

**Cualitativo vs. cuantitativo**

| | **Evaluación Cualitativa** | **Evaluación Cuantitativa** |
|---|---|---|
| Definición del apunte | *La severidad de los riesgos se calcula utilizando **escalas** de probabilidad e impacto* | *La severidad de un riesgo se calcula **numéricamente*** |
| Para qué se usa | **Priorizar** los riesgos más severos para analizar las posibles acciones posteriores | Comparar si el **costo de las acciones de tratamiento no excede a los beneficios** |
| Uso en la materia | **Es la que se usa** — *"A los efectos de nuestro estudio utilizaremos la evaluación cualitativa"* | Complementaria, posterior |

> **Erratum del apunte**: el texto dice literalmente *"Si bien luego será necesaria una evaluación **cualitativa** para comparar si el costo de las acciones que determinemos para el tratamiento de los riesgos no excede a los beneficios."* Ahí debe decir **cuantitativa** — es un error tipográfico evidente, ya que la frase anterior acaba de asignar la priorización a la cualitativa y el análisis costo/beneficio es numérico. Confirmado también por el Anexo I, práctica *Analizar el riesgo*, act. 8 ("Analizar el costo/beneficio de las posibles opciones de respuesta").

**Fórmula única del apunte**

```
SEVERIDAD DEL RIESGO = PROBABILIDAD × IMPACTO
```

Sinónimos que usa el apunte para el resultado: **severidad**, **estado del riesgo**, **exposición**.

**Escala de IMPACTO (completa, 0–5)**

| Valor | Nivel |
|---|---|
| 0 | Insignificante |
| 1 | Menor |
| 2 | Bajo |
| 3 | Significativo |
| 4 | Mayor |
| 5 | Severo |

**Escala de PROBABILIDAD (completa, 0–5, con umbrales)**

| Valor | Nivel | Umbral |
|---|---|---|
| 0 | Imposible | — |
| 1 | Raro | < 3 % |
| 2 | Poco Probable | < 10 % |
| 3 | Moderado | < 30 % |
| 4 | Probable | < 60 % |
| 5 | Casi seguro | > 60 % |

> Las escalas se aplican igual para amenazas (caso negativo) y para oportunidades (caso positivo).
> **Faltante**: *"se puede establecer una matriz para medir la severidad del riesgo"* — la **matriz de calor P×I no se convirtió** (era imagen). **(inferencia)** Con estas escalas, la matriz es de 6×6 y la severidad va de **0 a 25**; los cortes de color (verde/amarillo/rojo) no están definidos en el texto extraído. No inventar cortes: o se sacan del PDF original, o se declaran explícitamente como criterio propio en el TP.

**Taxonomía FAIR — para estimar probabilidad e impacto**

*"La Taxonomía FAIR puede ayudar a evaluar la **probabilidad (frecuencia de eventos de pérdida)** y el **impacto (magnitud de la pérdida)** de un riesgo."*

Reconstrucción del árbol (la figura llegó severamente destruida por markitdown — letras espaciadas y columnas entremezcladas; esta es una reconstrucción de la estructura, **verificar contra el PDF original**):

```
RIESGO
├── FRECUENCIA DE EVENTO DE PÉRDIDA        (→ probabilidad)
│   ├── Frecuencia de Amenazas
│   │   ├── Contacto: Aleatorio | Periódico | Intencional
│   │   └── Acción: Beneficio | Nivel de Esfuerzo | Riesgo de Detección
│   └── Vulnerabilidad
│       ├── Capacidad de las Amenazas: Habilidades | Recursos
│       └── Capacidad de Resistencia (Controles)
└── MAGNITUD DE PÉRDIDA                    (→ impacto)
    ├── Factores primarios de pérdida
    │   ├── Sobre el Activo: Productividad | Costo | Sensibilidad
    │   │      └── Sensibilidad → Reputación | Ventaja Competitiva |
    │   │                          Legal/Regulatoria | General
    │   │      Volumen
    │   └── Según la Amenaza: Competencia | Internas/Externas |
    │          Acción → Acceso | Uso Indebido | Divulgación |
    │                   Modificación | Denegación de Acceso
    └── Factores secundarios de pérdida
        ├── Sobre la organización: Momento | Debido cuidado | Detección |
        │      Respuesta → Contención | Remediación | Recuperación
        └── Factores externos: Detección | Legal/Regulatorio |
               Competidores | Medios de comunicación |
               Otros grupos de interés
```

*(Descripción completa: Documento Anexo 4 — Taxonomía FAIR, no incluido en este archivo.)*

**Resultado de esta etapa**: la valorización realizada da el **riesgo inherente**.

---

###### B.9 Priorización para el tratamiento de los riesgos

**Tabla de riesgos inherentes (formato del apunte)**

| Id | Especificación del Riesgo | Categoría | Valor Escala de Probabilidad | Valor Escala de Impacto | Severidad |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | **Σ Severidad** |

- La columna **Categoría** se llena con la taxonomía adoptada (SEI, PMI-RBS, MAGERIT, etc.).
- **Severidad** = Probabilidad × Impacto.
- La última fila acumula **Σ Severidad** (severidad total).

**Ordenamiento y regla de Pareto 80-20**

1. Ordenar la lista en **forma decreciente por Severidad**.
2. *"Dependiendo del análisis, es probable que puedan identificarse una gran cantidad de riesgos y, por lo tanto, la Gestión de Riesgos puede convertirse en un proyecto en sí mismo."* Por eso se adapta **Pareto 80-20**:

> *"La experiencia dice que la suma de la severidad de los riesgos que pertenecen al **80 por ciento de la severidad total** nos permitirá establecer el **20 por ciento de los riesgos** a los que deberá dar prioridad para su tratamiento."*

**Procedimiento operativo (inferencia, derivada de la formulación anterior)**: calcular Σ Severidad; recorrer la lista ordenada de mayor a menor acumulando severidad; **el corte está donde la severidad acumulada alcanza el 80 % de Σ Severidad**. Los riesgos por encima del corte son los que se tratan con prioridad.

**Del inherente al residual**

*"Una vez establecidas las estrategias de tratamiento será necesario **volver a calcular su severidad**, ya que tanto su probabilidad como su impacto podrán haber variado. Este valor será el **riesgo residual**, que será el riesgo que estaremos dispuestos a aceptar."*

**Importante (textual del apunte)**: *"La **especificación del riesgo no ha variado**, solo el valor de su severidad."*

```
Riesgo inherente  = P_inicial  × I_inicial      (sin ninguna medida aplicada)
        ↓  aplicar estrategia de tratamiento + controles
Riesgo residual   = P_tratada  × I_tratada      (lo que se acepta y se cubre con planes)
```

---

###### B.10 Responder a los riesgos

**Tipos de control y qué instrumento se define para cada uno**

Esta tabla es el corazón de la articulación control → instrumento. Es lo que más se pregunta.

| Tipo de control | Qué hace (textual) | Instrumento que se define |
|---|---|---|
| **Preventivo** | *Reducen la probabilidad o impacto del riesgo o eliminan sus causas* | **Estrategias de tratamiento**, en función de las características del riesgo |
| **Detectivo** | *Detectan el riesgo una vez ocurrido, reducen el impacto del riesgo* | **Planes de contingencia y de continuidad de negocio**, en función de las estrategias de tratamiento definidas |
| **Correctivo** | *Identifican y corrigen las causas del riesgo ocurrido* | **Planes de recuperación**, también en relación a las estrategias de tratamiento |

**Encuadre ISO 27002:2022 de los controles de tratamiento**

Los controles a establecer para las **estrategias de tratamiento** serán:
- **Tipo**: Preventivo
- **Propiedades de seguridad de la información**: todas (C, I, D)
- **Concepto de ciberseguridad**: **Proteger**
- **Capacidades operacionales**: son las que *permitirán asignar las responsabilidades y establecer los lineamientos de implementación de las acciones requeridas para el control*

**Estrategias de tratamiento — riesgos NEGATIVOS (amenazas)**

| Estrategia | Definición del apunte | Cuándo aplica *(inferencia — el apunte no da criterios de selección explícitos, solo las definiciones)* |
|---|---|---|
| **Evitar** | *No se acepta de esa forma* | Severidad muy alta e inaceptable, y existe una alternativa que elimina la exposición: cambiar el diseño, no adoptar la tecnología, no hacer la actividad. Elimina el riesgo, no lo reduce |
| **Transferir** | *A un tercero el riesgo y la gestión del mismo (**subcontratar, asegurar**)* | Impacto alto y probabilidad baja/media, y hay un tercero mejor posicionado para absorberlo (seguro) o gestionarlo (outsourcing). No reduce la probabilidad; acota la pérdida propia |
| **Mitigar** | *Se hará lo posible para **minimizar su ocurrencia (probabilidad) y consecuencias (impacto)*** | Caso general de los riesgos priorizados por Pareto donde evitar es inviable y transferir no cubre. Es donde entran los controles preventivos concretos |
| **Aceptar** | *Se aceptan las consecuencias de la posible ocurrencia del riesgo* | Severidad baja, o el costo del control excede el beneficio. Deja un residual que igualmente requiere planes de contingencia/recuperación/continuidad |

**Estrategias de tratamiento — riesgos POSITIVOS (oportunidades)**

| Estrategia | Definición del apunte | Simétrica de |
|---|---|---|
| **Explotar** | *Se hará lo posible para asegurarse que la oportunidad sea una realidad* | Evitar |
| **Compartir** | *Transferir a un tercero **mejor capacitado para capturar** la oportunidad* | Transferir |
| **Mejorar** | *Se hará lo posible por **maximizar** su ocurrencia (probabilidad) y consecuencias (impacto)* | Mitigar |
| **Aceptar** | *Estoy dispuesto a aceptar las consecuencias de su posible ocurrencia* | Aceptar |

> El Anexo I (Analizar el riesgo, act. 8) nombra las opciones con otra nomenclatura, equivalente: **evitar, reducir/mitigar, transferir/compartir, aceptar, explotar/aprovechar**.

**Balance costo/beneficio**

*"Deberemos balancear el **costo de implementación de los controles y acciones de tratamiento** de los riesgos contra los **beneficios derivados** en función del nivel de riesgo."*
> La figura que graficaba esa curva **no se convirtió**.

**Reservas**

*"Los imprevistos y todas las cuestiones relacionadas a la respuesta a riesgos deben gestionarse a través de **reservas**."*

| Reserva | Qué atiende |
|---|---|
| **Gerenciales** | Los **imprevistos** |
| **De Contingencia** | Todas las cuestiones relacionadas a la **planificación de la respuesta a riesgos** |

**Descomposición del precio de un contrato de proyecto** (aplicable, dice el apunte, *"a cualquier proceso o actividad de la organización"*). Reconstrucción del cuadro:

```
Precio total del contrato
├── Presupuesto total del Proyecto
│   ├── Presupuesto de realización del proyecto      → COSTO SEGURO
│   │   ├── Costo del Proyecto
│   │   └── Costo de respuesta a riesgos
│   └── Presupuesto de Reservas                      → COSTO PROBABLE
│       ├── Reservas Gerenciales
│       └── Reservas de Contingencias
└── Honorarios o Ganancias
```

> El cuadro original vino como texto plano en dos columnas sin bordes; la **anidación de arriba es una reconstrucción (inferencia)**. Lo que sí es textual: los ocho conceptos, los pares "Costo del Proyecto / Reservas Gerenciales" y "Costo de respuesta a riesgos / Reservas de Contingencias", y la línea final "Costo seguro | Costo probable".

---

###### B.11 Planes de contingencia, recuperación y continuidad de negocio

**Sobre qué actúan**: *"Identificados los riesgos y realizado su tratamiento quedará actuar sobre el **riesgo residual o remanente**. Este es el nivel de riesgo que la organización está dispuesta a aceptar y para el que deberán plantearse los planes de contingencia, recuperación y continuidad de negocio."*

**Los tres planes — definición y diferencia**

| Plan | Definición textual | Momento | Pregunta que responde |
|---|---|---|---|
| **Plan de Contingencia** | *Especifica los **procedimientos que se ejecutarán ante la eventual ocurrencia de un riesgo*** | Inmediatamente al materializarse el riesgo | ¿Qué hago **ahora** que pasó? |
| **Plan de Recuperación** | *Sigue **inmediatamente** al plan de contingencia; permitirá **restablecer rápidamente los servicios** de la organización* | Después de la contingencia | ¿Cómo **vuelvo** al estado normal? |
| **Plan de Continuidad de Negocio** | *En el tiempo que media entre que sucede la contingencia y se recuperan los servicios se deberán mantener operativos los **procesos críticos**. Especificará **cómo se realizarán las actividades críticas del negocio para las cuales puede no contarse con los activos normalmente utilizados**ated en las mismas* | **En paralelo**, durante todo el intervalo contingencia → recuperación | ¿Cómo **sigo funcionando** mientras tanto? |

Encadenamiento:

```
        materialización
              │
   ───────────┼──────────────────────────────────────────►  tiempo
              │
        [CONTINGENCIA] ──► [RECUPERACIÓN] ──► servicios restablecidos
              └──────── [CONTINUIDAD DE NEGOCIO] ────────┘
                     (procesos críticos operativos
                      sin los activos habituales)
```

**Qué deben prever los planes (contingencia y recuperación)**

1. **Actividades de monitoreo** de la materialización de un riesgo en función de las **alarmas o indicadores** establecidos en la identificación del riesgo.
2. **Definición de las acciones** a poner en práctica una vez materializado el riesgo.
3. **Formación del equipo** involucrado en la ejecución de los planes de contingencia y recuperación.
4. **Entrenamiento mediante simulacros o pruebas.**

**Secuencia de acciones desde la detección**

A partir de la detección de la materialización del riesgo, los planes deben indicar la forma de:

1. **Evaluar los daños**
2. **Priorizar** las actividades del plan de acción
3. **Ejecutar** las actividades
4. **Evaluar los resultados**
5. **Restablecer las operaciones**

**Métricas de recuperación: RPO, RTO, WRT**

Escenario del gráfico del apunte:
1. Se tiene un **backup del sistema completo** realizado en un punto.
2. **Ocurre un desastre.**
3. **Recuperación**: no es completa, *"ya que habremos perdido todo lo ocurrido entre el punto 1 y 2 (RPO)"*.

| Sigla | Nombre | Definición textual |
|---|---|---|
| **RPO** | Recovery Point Objective | *Determina el objetivo de **posible pérdida máxima de datos** introducidos desde el último backup hasta la caída del sistema* |
| **RTO** | Recovery Time Objective | *Determina el **tiempo en que se puede recuperar el sistema*** |
| **WRT** | Work Recovery Time | *El **tiempo máximo necesario para verificar el sistema, la integridad de los datos**, entre otros. Por ejemplo: chequear información faltante, chequear bases de datos, logs, levantar servicios, etc.* |

```
   ← RPO →│                 │← RTO ──►│← WRT ─►│
 [backup] │  ...datos       │         │        │
──────────┼─────────────────┼─────────┼────────┼──►
       (1) backup      (2) desastre  sistema  sistema
                                    recuperado verificado
```
*(El gráfico original es una figura; el esquema de arriba es reconstrucción — inferencia — a partir de las tres definiciones textuales y del orden en que el apunte las presenta.)*

**Buenas prácticas de referencia para estos planes**

| Documento | Alcance |
|---|---|
| **NIST 800-34** — Planes de contingencia y recuperación | *Proporciona una metodología para **medir el desarrollo** de planes de contingencia, considerados **únicos para cada sistema**, brindando medidas preventivas, estrategias de recuperación y consideraciones técnicas apropiadas para la confidencialidad, integridad y disponibilidad de la información del sistema, requisitos y el **nivel de impacto** del sistema* |
| **ISO 22301** y **BS 25999** — Gestión de la Continuidad del Negocio (BCM) | *Se enfocan en considerar la **disponibilidad como dimensión crítica** de la seguridad de la información, por lo que el análisis de riesgos se realiza en función de considerar el **impacto en el negocio** de incidentes o eventos que provoquen una **interrupción o degradación de las operaciones*** |

---

###### B.12 SOA / Declaración de Aplicabilidad — NO ESTÁ EN ESTE APUNTE

**El apunte no menciona la Declaración de Aplicabilidad (SoA / Statement of Applicability) en ningún punto.** Búsqueda exhaustiva sobre el archivo completo: no aparecen "SOA", "SoA", "aplicabilidad" ni "declaración de aplicabilidad".

Lo más cercano que sí trae el apunte:
- **ISO 27001:2022** propone el marco del **SGSI**, que coordina *"la definición de políticas, objetivos y **alcance** de la seguridad de la información en la organización, el análisis, valorización y tratamiento de los riesgos sobre los activos involucrados, **los controles a realizar y su monitorización** para luego realizar las mejoras correspondientes"*. Ese "los controles a realizar" es el lugar del SGSI donde el SoA vive, pero el apunte no lo nombra.
- **ISO 27002:2022** con sus **93 controles** y sus atributos es el catálogo contra el cual se elabora un SoA.
- **COBIT 2019 / Anexo I, práctica "Definir un portafolio con acciones de gestión de riesgos", act. 1**: *"Mantener un **inventario de las actividades de control** que se han implantado para mitigar el riesgo... Clasificar las actividades de control y asignarlas a escenarios de riesgos de TI específicos y agregados."* Funcionalmente es lo mismo que un SoA, con otro nombre.

**Pendiente**: si el TP Integrador pide un SoA, la definición hay que traerla de otra fuente (ISO 27001 cláusula 6.1.3 d) o de otro apunte de la cátedra. No inventarla desde este material.

---

###### B.13 Enlaces explícitos entre Gestión de Riesgos y Gestión de Servicios (ITIL 4)

> El apunte trata incidentes, eventos, problemas, cambios y configuración/CMDB **en la sección de Gestión de Servicios de TI**, no en la de Gestión de Riesgos. Su desarrollo completo (actividades y KPIs de cada práctica) corresponde a la Parte C. Acá se consolida **solo lo que el propio apunte declara como puente con la Gestión de Riesgos**, más las definiciones mínimas, porque es exactamente lo que cierra el ciclo del riesgo residual.

**Definiciones ITIL 4**

| Concepto | Definición textual ITIL 4 |
|---|---|
| **Incidente** | *Una **interrupción no planificada** de un servicio o la **reducción de la calidad** de un servicio* |
| **Evento** | *Cualquier **cambio de estado** que tenga importancia para la gestión de un servicio u otro elemento de configuración (CI)* |
| **Problema** | *Una **causa o causa potencial, de uno o más incidentes*** |
| **CMDB** (Base de Datos de Configuraciones) | *Repositorio centralizado de los **elementos de configuración**: hardware, software, documentación y **personas** que forman parte de la infraestructura del cliente y de los servicios que se prestan* |

**Incidente vs. Evento** (criterio de separación del apunte): *"No existe una monitorización de los incidentes, sino que son **informados** por diversas fuentes tales como usuarios, soporte técnico. Cuando las interrupciones de servicio o la reducción de su calidad son **monitorizadas**, ITIL las denomina **eventos**."*

**Incidente vs. Problema**: *"Los **incidentes** son elementos reparables (break-fix) que causan un impacto negativo en las personas y, como tales, deben resolverse para restaurar el funcionamiento normal del trabajo. Los **problemas** causan incidentes o eventos; deben analizarse e investigarse para que se puedan identificar soluciones temporales o definitivas que reduzcan el número y el impacto de futuros incidentes o eventos."*

**Puentes declarados con la Gestión de Riesgos (textuales)**

| Elemento ITSM | Rol en la Gestión de Riesgos (según el apunte) |
|---|---|
| **Comunicación del incidente por el usuario** | *Es el **disparador que da la alerta de la materialización de un riesgo** que debería haber sido identificado* |
| **Soluciones temporales y permanentes de la Gestión de Incidentes** | *Son los **planes de contingencia y recuperación** que deben ser activados* |
| **Incidente que afecta procesos críticos** | *Probablemente se deba **activar el Plan de Continuidad de Negocio*** |
| **Evento Informativo** | No requiere acción en el momento; su análisis posterior *puede revelar información beneficiosa a la **Gestión de Problemas*** |
| **Evento De advertencia** | *Permite tomar medidas antes de que la empresa experimente un impacto negativo; **es un disparador para Estrategias de Tratamiento en la Gestión de Riesgos*** |
| **Evento Excepción** | *Indica que se ha identificado una **infracción a una norma establecida**. Requiere acción: son los **disparadores de Planes de Contingencia** en la Gestión de Riesgos* |
| **CMDB** | Provee, en el registro del incidente, la **información de apoyo** sobre los CI (activos de TI) involucrados; es el inventario vivo que sostiene la trazabilidad activo → incidente → riesgo |
| **Control de Cambios** | Su ausencia figura como riesgo propio de Seguridad de la Información ("no realización de la gestión correcta de cambios"); en la taxonomía SEI aparece como **2.2.3 Control de Cambios** dentro de fallas de software |

**Clasificación de eventos (completa)**

| Tipo | Definición | Acción | Disparador de |
|---|---|---|---|
| **Informativos** | No requieren acción en el momento en que se identifican | Registrar y analizar después | Insumo para Gestión de Problemas |
| **De advertencia** | Permiten tomar medidas antes de que la empresa experimente un impacto negativo | Actuar preventivamente | **Estrategias de Tratamiento** (Gestión de Riesgos) |
| **Excepciones** | Indican que se identificó una infracción a una norma establecida | Requieren acción | **Planes de Contingencia** (Gestión de Riesgos) |

Ruteo de eventos hacia otras prácticas: *"algunos eventos calificarán como incidente → **Gestión de Incidentes**. Los eventos repetidos que muestran un desempeño fuera de los niveles deseados pueden ser evidencia de un **problema potencial** → **Gestión de Problemas**. Para algunos eventos, la respuesta correcta es **iniciar un cambio** → **Control de Cambios**."*

**Priorización de incidentes: Impacto + Urgencia**

Ojo con la diferencia respecto de la Gestión de Riesgos, que usa **Impacto × Probabilidad**. En Gestión de Incidentes el par es distinto:

| Parámetro | Definición del apunte |
|---|---|
| **Impacto** | *Determina la importancia del incidente dependiendo de cómo éste afecta a los **procesos de negocio** y/o del **número de usuarios afectados*** |
| **Urgencia** | *Depende del **tiempo máximo de demora que acepte el cliente** para la resolución del incidente y/o el nivel de servicio acordado en el **SLA*** |

**Escalado** (aplica a incidentes y a problemas):
- **Funcional**: se requiere el apoyo de un **especialista de más alto nivel** (segunda línea de soporte, que puede ser personal de Gestión de Problemas).
- **Jerárquico**: se acude a un **responsable de mayor autoridad** para decisiones que exceden las atribuciones del nivel (p. ej., asignar más recursos).

**Cadena Problema → Cambio → Configuración**

```
Incidentes recurrentes / eventos
        ↓ (Gestión de Problemas: reactiva o proactiva)
   Análisis y diagnóstico → causa determinada → ERROR CONOCIDO
        ↓ (Control de Errores)
   RFC (Solicitud de Cambio)  →  CONTROL DE CAMBIOS (CAB / ECAB)
        ↓  con plan de "back-out" obligatorio
   Implementación (Gestión de Versiones)
        ↓
   Actualización de la CMDB (Gestión de la Configuración del Servicio)
        ↓
   PIR (Revisión Post Implementación)  →  cierre del problema
```

- **Gestión de Problemas reactiva**: notificado el incidente/evento que no tiene solución temporal o definitiva conocida, lo analiza para descubrir su causa y proponer soluciones.
- **Gestión de Problemas proactiva**: basándose en incidentes registrados o monitorizando la calidad de la infraestructura TI y analizando su configuración, **previene** incidentes o eventos con las mismas características antes de que ocurran.
- **La Gestión de Problemas NO implementa cambios**: para eso existe el **Control de Cambios**, con el que debe interactuar.
- **Gestión de la Configuración del Servicio** (mantiene la CMDB y los CI: visión precisa y actualizada de la infraestructura y sus relaciones) vs. **Gestión de Activos de TI** (gestiona los activos **a lo largo de su ciclo de vida completo**, desde la adquisición hasta la disposición, maximizando valor y optimizando rendimiento, **costo y riesgo asociado**). En ITIL v3 estaban unidas; ITIL 4 las separa.

---

###### B.14 Anexo II — Etapas de un ciberataque (insumo para identificar amenazas y vulnerabilidades)

> Advertencia del propio apunte: *"el uso de estas herramientas puede ser ilegal y está sujeto a restricciones legales y éticas. Siempre es recomendable utilizar estas herramientas de manera ética y legal, con el permiso explícito del propietario del sistema o red objetivo."*

| Fase | Qué hace el atacante | Herramientas |
|---|---|---|
| **1. Reconocimiento** | Obtención de información sobre una potencial víctima (persona u organización). Se **selecciona el objetivo** identificando sistemas, redes o datos vulnerables | Escaneo de red: **Nmap, Masscan, Zmap**<br>Recopilación de información: **theHarvester, Maltego, Shodan**<br>Reconocimiento activo: **Recon-ng, Metasploit**<br>Ingeniería social: **SET (Social Engineering Toolkit), Gophish**<br>Escaneo de vulnerabilidades: **Nessus, OpenVAS, Qualys** |
| **2. Exploración** | Usa la info de la fase 1 para sondear el blanco: direcciones IP, nombres de host, datos de autenticación, sistemas operativos, servicios en ejecución | *(mismas herramientas que fase 1)* |
| **3. Consolidación** | Se materializa el ataque por **explotación de vulnerabilidades y defectos** (*flaw exploitation*). Puede comprender **elevación de privilegios**, **movimiento lateral** (propagación por la red para comprometer otros sistemas) y **exfiltración de datos** (recolección y transmisión), o usar credenciales robadas para comprometer más sistemas.<br>Técnicas: **Buffer Overflow, DoS, DDoS, Password filtering, Session hijacking** | Explotación: **Metasploit, ExploitDB, SQLMap**<br>Exfiltración: **Cobalt Strike, Mimikatz, Empire**<br>Escalada de privilegios: **PowerSploit, Sudo-Killer, BeRoot** |
| **4. Mantener el acceso** | Implanta herramientas para volver a acceder en el futuro desde cualquier lugar con Internet. Garantiza **persistencia** y manipula o elimina rastros | Backdoors: **Netcat (nc), Meterpreter, Cobalt Strike**<br>Rootkits: **RootkitHunter, chkrootkit, Windows Rootkit Arsenal**<br>Troyanos y RATs: **DarkComet, NanoCore**<br>Persistencia: **Scheduled Tasks, Registry, Service Installation** |
| **5. Borrar huellas** | Borra las huellas de la intrusión para evitar detección: **archivos de registro, archivos de configuración** y otras pistas | — |

**Mitigación**: las organizaciones implementan **SOC** (centros de operaciones de seguridad) o contratan personal que realice monitoreo y responda a incidentes.

| Herramienta | Definición del apunte |
|---|---|
| **IDS** (Sistema de Detección de Intrusiones) | *Un dispositivo de monitoreo **pasivo** que detecta amenazas potenciales y **genera alertas*** |
| **IPS** (Sistema de Prevención de Intrusiones) | *No sólo se encarga de la búsqueda de actividad maliciosa, sino también de **intentar detenerla**. Dispositivos **proactivos** que monitorizan el tráfico de forma continua y todas las actividades del entorno TI. Controla el acceso en la red. Toma decisiones de control de acceso **basándose en los contenidos del tráfico**, en lugar de puertos o direcciones IP. Representa una importante mejora respecto a las tradicionales tecnologías de cortafuegos* |

> Conexión con la Parte B: las **5 fases** son un vector para redactar la *especificación del riesgo* y para estimar la **probabilidad** en la taxonomía FAIR (rama "Capacidad de las Amenazas": habilidades y recursos del atacante). Las herramientas de mitigación (IDS/IPS/SOC) son **controles detectivos**; los backups y las políticas de resguardo, **correctivos/preventivos**. *(inferencia)*

---

###### B.15 Faltantes del material y problemas de conversión (verificar contra el PDF original)

1. **Figura "Conceptos asociados a la Gestión de Riesgos"** (pág. 7): perdida. Es la que relaciona amenaza / vulnerabilidad / activo / impacto / probabilidad / riesgo. Es el diagrama conceptual central de la unidad.
2. **Figura del proceso ISO 31000:2018** (pág. 4): perdida.
3. **Los 4 temas de ISO 27002:2022** (pág. 5): la figura no se convirtió; los nombres no están en el texto.
4. **Estructura de desglose de riesgos (RBS) del PMI** (pág. 11): la figura no se convirtió; el contenido no está en ningún lado del texto.
5. **Matriz de severidad P × I** (pág. 14): la figura no se convirtió. No hay cortes de nivel (bajo/medio/alto/crítico) definidos en el texto.
6. **Gráfico de balance costo de controles vs. beneficios** (pág. 17): perdido.
7. **Gráfico RPO/RTO/WRT** (pág. 20): perdido; solo quedan las tres definiciones y la secuencia numerada.
8. **Taxonomía FAIR** (pág. 15): llegó destruida (letras espaciadas, columnas mezcladas). La reconstrucción de B.8 es probable pero **no verificada**.
9. **Cuadro de dependencias entre activos** y **procedimiento de 5 pasos** (págs. 8): llegaron destruidos; reconstruidos en B.5.
10. **Cuadro de reservas / precio del contrato** (pág. 18): llegó como texto plano; la anidación de B.10 es reconstrucción.
11. **Erratum del apunte** (pág. 13): dice "evaluación cualitativa" donde debe decir "cuantitativa" en la frase sobre comparar costo de acciones contra beneficios.
12. **No están en este apunte** (hay que buscarlos en otras fuentes de la cátedra): SOA / Declaración de Aplicabilidad; catálogo de amenazas de MAGERIT Libro II; descripción ampliada de la Taxonomía SEI (Anexo 3); descripción de la Taxonomía FAIR (Anexo 4); taxonomías de Boehm, Caper Jones y SEI *Software Development Risk Taxonomy*; definiciones de **apetito** y **tolerancia** al riesgo (solo se mencionan en el Anexo I, sin definir); fórmula de cálculo de **criticidad** a partir de C/I/D.


---


##### Definición formal de riesgo (cátedra)

La cátedra no da una definición propia: encadena tres definiciones de estándar más una cita conceptual.

| Fuente | Definición textual del material |
|---|---|
| ISO 9001 | Riesgo **es la probabilidad de que ocurra un evento que pueda afectar los objetivos de la organización**. Un riesgo puede ser negativo (AMENAZA) o positivo (OPORTUNIDAD). |
| ISO 31000 / COBIT 2019 | Riesgo **es el efecto de la incertidumbre sobre el logro de los objetivos**, donde *efecto* es un desvío respecto a lo esperado. |
| PMI (contexto de proyectos) | Los objetivos de la Gestión de los Riesgos del Proyecto son **aumentar la probabilidad e impacto de eventos positivos (oportunidades) y disminuir la probabilidad e impacto de eventos adversos (amenazas)** para el proyecto. |
| Robert Charette (cita) | "Un riesgo NO es un PROBLEMA… El PROBLEMA es un RIESGO que ha acontecido". |

El eje común que la cátedra remarca es el **concepto dual**: el riesgo no es solo pérdida, también es oportunidad. Esto se refleja después en las estrategias de tratamiento (dos columnas: negativos / positivos).

###### Cómo se redacta una especificación de riesgo

Del documento "Definición de Riesgo". Una definición de riesgo **debe** contener los cinco elementos:

| # | Elemento |
|---|---|
| 1 | La situación que ocurre |
| 2 | Un verbo en tiempo presente |
| 3 | Un activo (o varios) |
| 4 | La consecuencia de ese riesgo |
| 5 | El proceso crítico afectado |

Ejemplos que da la cátedra (contexto: fábrica de galletitas):

| Situación | Activo | Consecuencia / proceso |
|---|---|---|
| Falla sensor | Máquina empaquetado | Falla calidad producción galletitas |
| Corte luz | Servidor ERP | Suspender facturación |
| Falta insumos | Proceso fabricación | Reducción ventas |
| Bloqueo sindical | Logística | Reducción de ventas |
| Hackeo | BD | Cae la reputación de la organización |

La secuencia de trabajo que pide la cátedra sobre cada riesgo definido es: (1) definir varios riesgos, (2) clasificar cada uno según SEI, (3) calcular Severidad = Probabilidad × Impacto, (4) definir estrategias para Evitar / Transferir / Mitigar, (5) controles que se aplican, (6) riesgo residual — cómo cambia en base a las acciones tomadas, (7) disparadores y planes.

Nota de consistencia: la tabla de ejemplo mezcla en una sola columna "Consecuencia/proceso", cuando la regla de los 5 elementos los pide separados. Los ejemplos de la tabla, además, no incluyen el verbo en presente — son notas taquigráficas, no especificaciones completas. **(inferencia)**

---

##### Taxonomía SEI — Taxonomy of Operational Cyber Security Risks

Se usa en la etapa **1 – Recopilar Datos** del proceso de gestión de riesgos (COBIT 2019), para **clasificar** el riesgo una vez identificado. Cuatro clases de primer nivel, subclases y subcategorías. Transcripción completa de la lámina (el PDF viene en tablas rotas; se reconstruyó la jerarquía por numeración).

###### 1. Acciones de las Personas

| Código | Subclase | Código | Subcategoría |
|---|---|---|---|
| 1.1 | Involuntarias | 1.1.1 | Equivocación (acción incorrecta) |
| | | 1.1.2 | Error (por desconocimiento) |
| | | 1.1.3 | Omisión (por apresuramiento) |
| 1.2 | Deliberadas | 1.2.1 | Fraude |
| | | 1.2.2 | Sabotaje |
| | | 1.2.3 | Robo |
| | | 1.2.4 | Vandalismo |
| 1.3 | Inacción | 1.3.1 | Habilidad |
| | | 1.3.2 | Conocimiento |
| | | 1.3.3 | Guía |
| | | 1.3.4 | Disponibilidad |

###### 2. Fallas de Sistemas y Tecnología

| Código | Subclase | Código | Subcategoría |
|---|---|---|---|
| 2.1 | Hardware | 2.1.1 | Capacidad |
| | | 2.1.2 | Rendimiento |
| | | 2.1.3 | Mantenimiento |
| | | 2.1.4 | Obsolescencia |
| 2.2 | Software | 2.2.1 | Compatibilidad |
| | | 2.2.2 | Configuración |
| | | 2.2.3 | Control de Cambios |
| | | 2.2.4 | Parámetros de Seguridad |
| | | 2.2.5 | Prácticas de Codificación |
| | | 2.2.6 | Testing |
| 2.3 | Sistemas | 2.3.1 | Diseño |
| | | 2.3.2 | Especificaciones |
| | | 2.3.3 | Integración |
| | | 2.3.4 | Complejidad |

###### 3. Fallas de Procesos Internos

| Código | Subclase | Código | Subcategoría |
|---|---|---|---|
| 3.1 | Diseño de Procesos y Ejecución | 3.1.1 | Flujo de Procesos |
| | | 3.1.2 | Documentación de Procesos |
| | | 3.1.3 | Roles y responsabilidades |
| | | 3.1.4 | Notificaciones y alertas |
| | | 3.1.5 | Flujo de Información |
| | | 3.1.6 | Escalado de problemas |
| | | 3.1.7 | Acuerdo de Nivel de Servicio |
| | | 3.1.8 | Tarea fuera de control |
| 3.2 | Control de Procesos | 3.2.1 | Monitorización del estado |
| | | 3.2.2 | Métricas |
| | | 3.2.3 | Revisiones Periódicas |
| | | 3.2.4 | Dueño del Proceso |
| 3.3 | Procesos de Soporte | 3.3.1 | Dotación del Personal |
| | | 3.3.2 | Recursos |
| | | 3.3.3 | Entrenamiento y desarrollo |
| | | 3.3.4 | Adquisición |

###### 4. Eventos Externos

| Código | Subclase | Código | Subcategoría |
|---|---|---|---|
| 4.1 | Desastres | 4.1.1 | Climatológicos |
| | | 4.1.2 | Incendios |
| | | 4.1.3 | Inundaciones |
| | | 4.1.4 | Terremotos |
| | | 4.1.5 | Disturbios |
| | | 4.1.6 | Pandemias |
| 4.2 | Cuestiones Legales | 4.2.1 | Regulaciones |
| | | 4.2.2 | Legislación |
| | | 4.2.3 | Litigios |
| 4.3 | Cuestiones del Negocio | 4.3.1 | Fallas del Suministro |
| | | 4.3.2 | Condiciones del Mercado |
| | | 4.3.3 | Condiciones Económicas |
| 4.4 | Dependencias con Servicios | 4.4.1 | Servicios Públicos |
| | | 4.4.2 | Servicios de Emergencia |
| | | 4.4.3 | Combustible |
| | | 4.4.4 | Transporte |

Totales: 4 clases, 13 subclases, 45 subcategorías.

La lámina remite a "**Anexo 3: Descripción de la Taxonomía SEI**" para la descripción de cada subcategoría. **Ese anexo no está entre los archivos leídos** — la taxonomía acá está completa en estructura y numeración, pero sin las definiciones de cada ítem.

###### Taxonomía complementaria de amenazas (MAGERIT)

En la misma etapa de recopilación de datos, para identificar **amenazas y vulnerabilidades** (no para clasificar el riesgo), el PPT usa MAGERIT:

| Categoría | Detalle en el material |
|---|---|
| Desastres naturales | — |
| De origen industrial | Del entorno: accidentales. Humanos: accidentales o deliberados |
| Fallos humanos no intencionados | — |
| Ataques intencionales | — |

---

##### Taxonomía FAIR — Factor Analysis of Information Risk

FAIR es lo que la cátedra usa para **justificar el valor de Probabilidad y de Impacto**, no para clasificar el riesgo. La rama izquierda (Frecuencia de Eventos de Pérdida) sostiene la **Probabilidad**; la rama derecha (Magnitud de Pérdida) sostiene el **Impacto**. **(inferencia explícita del uso, coherente con el título de la lámina "FAIR — Valoración del Impacto y Probabilidad del Riesgo")**

###### Árbol completo

```
RIESGO
├── Frecuencia de Eventos de Pérdida   → sostiene PROBABILIDAD
│   ├── Frecuencia de Amenazas
│   │   ├── Contacto
│   │   │   ├── Aleatorio
│   │   │   ├── Periódico (Regular)
│   │   │   └── Intencional
│   │   └── Acción
│   │       ├── Beneficio
│   │       ├── Nivel de Esfuerzo
│   │       └── Riesgo de Detección
│   └── Vulnerabilidades
│       ├── Capacidad de las Amenazas
│       │   ├── Habilidades
│       │   └── Recursos
│       └── Capacidad de Resistencia (Controles)
└── Magnitud de Pérdida                → sostiene IMPACTO
    ├── Factores primarios de pérdida
    │   ├── Sobre el Activo
    │   │   ├── Productividad
    │   │   ├── Costo (de reemplazo)
    │   │   ├── Sensibilidad
    │   │   │   ├── Reputación
    │   │   │   ├── Ventaja Competitiva
    │   │   │   ├── Legal / Regulatoria
    │   │   │   └── General
    │   │   └── Volumen
    │   └── Según la Amenaza
    │       ├── Competencia
    │       ├── Internas / Externas
    │       └── Acción
    │           ├── Acceso
    │           ├── Uso Indebido
    │           ├── Divulgación
    │           ├── Modificación
    │           └── Denegación de Acceso
    └── Factores secundarios de pérdida
        ├── Sobre la organización
        │   ├── Momento
        │   ├── Debido cuidado
        │   ├── Detección
        │   └── Respuesta
        │       ├── Contención
        │       ├── Remediación
        │       └── Recuperación
        └── Factores externos
            ├── Detección
            ├── Legal / Regulatorio
            ├── Competidores
            ├── Medios de comunicación
            └── Otros grupos de interés
```

Discrepancia entre fuentes: el PPT rotula el segundo tipo de contacto como **"Periódico"** y el Anexo II como **"Regular"**. Es el mismo factor.

###### Rama: Frecuencia de Eventos de Pérdida (Probabilidad)

Definición (Anexo II): **frecuencia probable, dentro de un rango de tiempo, en que un agente de amenaza podrá causar daño sobre un activo**. Definición del PPT: **número de veces que es probable que ocurra un evento de pérdida dentro de un período de tiempo definido**. Se descompone en dos factores: frecuencia de amenazas y vulnerabilidades.

**Frecuencia de Amenazas** — frecuencia probable, dentro de un rango de tiempo, en que un evento de amenaza podrá actuar sobre un activo (la cantidad probable de veces que una amenaza actúe, de forma exitosa o no, sobre el recurso).

| Factor | Subfactor | Definición del material |
|---|---|---|
| **Contacto** (Frecuencia de Contacto) | — | Frecuencia probable, dentro de un rango de tiempo, en que el agente de amenaza entrará en contacto con el activo. El contacto puede ser **físico o lógico**. Cada cuánto un activo entra en contacto con una amenaza. |
| | Aleatorio | El agente entra en contacto accidentalmente con el activo en el curso de una actividad no controlada. |
| | Periódico / Regular | El agente de amenaza entra en contacto con el activo durante el curso de una actividad regular. |
| | Intencional | El agente de amenaza busca entrar en contacto con el activo con objetivos específicos. |
| **Acción** (Probabilidad de Acción) | — | Una vez producido el contacto, es posible que se produzca o no una acción contra el activo. Para algunos agentes la acción siempre ocurre (ej.: un tornado que entra en contacto con una casa). **La acción solo se cuestiona con agentes humanos, otros animales y agentes artificialmente inteligentes como programas maliciosos.** |
| | Beneficio | Valor del activo desde el punto de vista del agente de amenaza. |
| | Nivel de esfuerzo | Expectativa del agente de amenaza sobre cuánto esfuerzo se necesitará para comprometer el activo. |
| | Riesgo de detección | Probabilidad de consecuencias negativas para el agente de amenaza: probabilidad de ser atrapado y sufrir consecuencias inaceptables. |

**Vulnerabilidades** — probabilidad de que un activo **no sea capaz de resistir** las acciones de un agente de amenaza (PPT: "probabilidad de que una amenaza se materialice en una pérdida de información").

Tres principios que fija el Anexo II:
- La vulnerabilidad **siempre es relativa al tipo de fuerza involucrada**. La resistencia a la tracción de una cuerda solo importa si la fuerza es un peso aplicado a lo largo de la cuerda; no aplica contra fuego o erosión química. Igual, un antivirus no protege contra un empleado que busca perpetrar un fraude.
- Hay que evaluar la vulnerabilidad **en el contexto de tipos específicos de amenaza y tipos de control**.
- La vulnerabilidad frente a **cada** evento no puede exceder el 100%, pero el **riesgo agregado** crece con la cantidad de escenarios de amenaza distintos (ejemplo del material: caminar de noche por una zona peligrosa expone a ser atropellado, asaltado o víctima de un tiroteo — cada uno es un evento de amenaza potencial diferente).

| Factor | Subfactor | Definición del material |
|---|---|---|
| **Capacidad de las Amenazas** | — | Nivel probable de **fuerza** que un agente de amenaza puede aplicar contra un activo. No todos los agentes tienen las mismas habilidades ni recursos; según la comunidad de amenaza analizada, la probabilidad de encontrar un agente altamente capaz puede ser remota. Un agente puede ser muy hábil en un tipo de fuerza e incompetente en otro (ej.: un ingeniero de redes es competente en ataques tecnológicos pero puede ser incapaz de ejecutar un fraude contable complejo). Ejemplo del PPT: hay tipos de malware o ransomware más destructivos que otros. |
| | Habilidades | Enumerado en el árbol del PPT. Sin definición propia en el material. |
| | Recursos | Enumerado en el árbol del PPT. Sin definición propia en el material. |
| **Capacidad de Resistencia (CR)** — Controles | — | **La fortaleza de un control en comparación con una medida de referencia.** Se representa con un porcentaje. Ejemplo del material: una contraseña de ocho caracteres con mayúsculas, minúsculas, números y caracteres especiales resistirá los intentos de craqueo de cierto porcentaje de la población de agentes de amenaza. |

**Cálculo de la vulnerabilidad (método explícito de FAIR según el Anexo II):**

> La vulnerabilidad se determina **comparando CR con la capacidad de la comunidad de amenaza específica bajo estudio**. Si la capacidad de resistencia de una contraseña se estima en **80%** y la comunidad de amenaza tiene capacidades mejores que el promedio, digamos en el rango del **90%**, **la diferencia representa la vulnerabilidad**.

Es decir: Vulnerabilidad ≈ Capacidad de Amenaza − Capacidad de Resistencia (10 puntos en el ejemplo). El material da el ejemplo numérico pero **no formaliza la fórmula ni define qué hacer cuando CR > capacidad de amenaza**.

###### Rama: Magnitud de Pérdida (Impacto)

Definición del PPT: **las pérdidas sufridas a raíz del evento, resultado del impacto exitoso del agente de amenaza en el activo**.

FAIR establece **cuatro componentes principales** para evaluar la magnitud de pérdida, agrupados en dos niveles:

| Nivel | Componentes |
|---|---|
| Factores **primarios** de pérdida | Activos, Amenazas |
| Factores **secundarios** de pérdida | La organización, El ambiente externo |

**Pérdida primaria vs. pérdida secundaria** (definiciones del PPT, lámina 46):

| Tipo | Definición | Ejemplo del material |
|---|---|---|
| **Pérdida Primaria** | La que ocurre **directamente** como resultado de la acción de la amenaza sobre el activo. | En un ataque de denegación de servicio sobre la web de la empresa, la pérdida es la caída de la web y el perjudicado es la empresa. |
| **Pérdida Secundaria** | La pérdida sufrida por **el interesado principal debido a la reacción negativa de los interesados secundarios** ante el evento de pérdida. | Si es la web de una empresa que da un servicio de CRM, los afectados serán los clientes del CRM. |

**Factores primarios — sobre el ACTIVO**

Las dimensiones de criticidad (integridad, confidencialidad, disponibilidad) ya permiten establecer el nivel de criticidad; **FAIR agrega estos elementos para mejorar la valuación**:

| Factor | Subfactor | Definición del material |
|---|---|---|
| Productividad | — | Impacto del activo en la productividad de la organización. Ej.: el impacto que una base de datos dañada tendría en la capacidad de la organización para generar ingresos. |
| Costo de reemplazo | — | Costos asociados con el reemplazo de un activo robado o destruido. Ej.: reemplazar una notebook robada, reconstruir un edificio incendiado. |
| Sensibilidad | — | Impacto resultante de la **divulgación o uso indebido de información confidencial**. En algunos casos representa un valor económico, en otros confiabilidad. |
| | Reputación | La información divulgada proporciona **evidencia de incompetencia, actuación criminal o poco ética**. Refiere al daño de reputación resultante de **la naturaleza de la información divulgada**, a diferencia del daño de reputación que puede resultar cuando ocurre un evento de pérdida. |
| | Ventaja competitiva | La información proporciona una ventaja competitiva (estrategias clave, secretos, etc.). |
| | Legal / Regulatoria | La organización está **obligada por ley** a proteger la información. |
| | General | Información sensible que no cae en ninguna categoría anterior, pero que daría como resultado alguna forma de pérdida si se revela. |
| Volumen | — | Más activos en riesgo equivalen a mayor magnitud de pérdida. Ej.: un registro de cliente sensible versus miles. |

**Factores primarios — según la AMENAZA**

Amenaza: **cualquier cosa (objeto, sustancia, ser humano, plaga, etc.) capaz de actuar contra un activo de manera que pueda resultar en daño**. La consideración clave es que **las amenazas aplican fuerza contra un activo**, lo que puede causar un evento de pérdida. Prácticamente cualquiera y cualquier cosa puede ser un agente de amenaza en las circunstancias adecuadas: el operador bien intencionado pero inepto que destruye un trabajo por lotes diario, un contador realizando una auditoría, un hacker que ejecuta un exploit, el agua en una inundación, el viento en un tornado, un roedor que mastica un cable de datos.

| Factor | Subfactor | Definición del material |
|---|---|---|
| Competencia | — | Capacidades que tiene el atacante de **utilizar la información una vez conseguida**. Ej.: un hacker puede hacerse del código de un programa pero [no] tener las competencias necesarias para utilizarlo. *(El original dice "puede tener las competencias" — falta un "no"; error de tipeo del apunte, el sentido es el negativo).* |
| Internas / Externas | — | Identificación de las **comunidades de amenaza**. Herramienta para entender a quién y a qué nos enfrentamos. Internas: empleados, contratistas, socios. Externas: ciberdelincuentes (hackers profesionales), espías de la competencia, hackers no profesionales. |
| Acción | Acceso | Simplemente acceso no autorizado. |
| | Uso indebido | Uso no autorizado de activos (robo de identidad, montar un servicio de distribución de pornografía en un servidor comprometido, etc.). |
| | Divulgación | El agente de amenaza revela ilícitamente información sensible. |
| | Modificación | Cambios no autorizados en un activo. |
| | Denegación de acceso | Incluye destrucción, robo de un activo que no es de datos, etc. |

**Factores secundarios — sobre la ORGANIZACIÓN**

El riesgo existe dentro del contexto de una organización: **es la organización la que pierde recursos o la capacidad de operar**. Sus características también pueden atraer la atención de ciertas comunidades de amenaza, aumentando la frecuencia de eventos.

| Factor | Subfactor | Definición del material |
|---|---|---|
| Momento | — | El momento en que tiene lugar un evento puede tener un impacto tremendo en la pérdida. Ej.: un evento en medio de una gran campaña publicitaria genera pérdida significativamente mayor que el mismo evento en otro momento. |
| Debido cuidado | — | Juega un papel importante en el **grado de responsabilidad** que enfrenta la organización. Si no se tomaron las medidas preventivas del caso (en función de la amenaza y del valor del activo), el daño puede ser mucho más severo. Los estándares de la industria o "buenas prácticas" teóricas se toman como pautas de debido cuidado, pero generalmente **no consideran el entorno de amenaza ni la magnitud de la pérdida**; en consecuencia pueden ser insuficientes (no verdaderamente representativas del debido cuidado) o excesivamente conservadoras (prohibitivamente caras dado el riesgo inherente). |
| Detección | — | **No se puede responder a algo que no se ha detectado**: la respuesta se basa en la detección. Ocurren incidentes que no aparecen en el radar, pero si resultan en pérdida material casi siempre se detectan con el tiempo. Ej.: información robada que da ventaja a un competidor casi seguramente será reconocida. Aunque la detección no sea oportuna, una vez detectado el robo la organización aún puede responder y reducir pérdidas (ej.: acción legal). |
| Respuesta | — | Eficiencia con que la organización responde a un evento. Tiene tres componentes cuya inexistencia puede impactar significativamente la magnitud de pérdida. Las capacidades de respuesta no se limitan a restablecer servicios: también aplican a la divulgación de información (una organización que sufre divulgación pública de datos de clientes puede perder cartera y probablemente deba compensar al cliente afectado). |
| | Contención | Capacidad de limitar la **amplitud y la profundidad** de un evento. Ej.: contener la propagación de un gusano. |
| | Remediación | Capacidad de **eliminar el agente amenazante**. Ej.: erradicar el gusano. |
| | Recuperación | Capacidad de **devolver las cosas a la normalidad**. |

**Factores secundarios — FACTORES EXTERNOS**

El entorno en el que opera la organización juega un papel importante en el riesgo. **Los factores externos afectan la magnitud de pérdida cuando el evento es detectado por una entidad externa.**

| Factor | Definición del material |
|---|---|
| Detección | La detección externa puede ocurrir por: gravedad del evento, acciones intencionales del agente de amenaza, divulgación por parte de alguien interno familiarizado con el evento, divulgación intencional de la organización (por sentido del deber o por requerimiento legal), o por accidente. **Los restantes factores externos están basados en el factor de detección.** |
| Legal / Regulatorio | Se compone principalmente de tres partes: **regulaciones** (locales, provinciales, federales e internacionales), **derecho contractual** y **jurisprudencia específica**. |
| Competidores | Las pérdidas asociadas al panorama competitivo tienen que ver con la capacidad de la competencia de **aprovechar la situación**. Si un evento hace que las partes interesadas consideren abandonar la organización, la capacidad del competidor de aprovechar esa debilidad afectará la cantidad de pérdidas. |
| Medios de comunicación | La reacción de los medios afecta fuertemente cómo ven el evento las partes interesadas, abogados, reguladores y competidores. Si los medios difaman a la organización y la mantienen en los titulares por un período prolongado, el resultado puede ser devastador. Si en cambio la pintan como víctima bienintencionada que ejerció el debido cuidado, el daño legal y reputacional puede minimizarse. **Por esto las organizaciones deben tener procesos efectivos de comunicación de crisis.** |
| Otros grupos de interés | Otros grupos que pueden haber detectado el evento o que se consideren implicados en el riesgo (ej.: organizaciones no gubernamentales). |

###### Comunidades de Amenaza (FAIR) — características

Lámina 29 del PPT, muy degradada en la conversión. Reconstrucción de los pares característica–definición:

| Característica | Definición / valores del material |
|---|---|
| Motivación | Ideología, dinero ($), venganza. |
| Tolerancia al riesgo del agente de amenaza | Consecuencias negativas que el agente de amenaza es capaz de tolerar. |
| Intento | Solo conseguir acceso / dañar. |
| Capacidades del atacante | Según el **vector primario de ataque** o la ruta que sigue el atacante. |
| Patrocinio | Que exista beneficio para el atacante. |
| Características preferidas | Personas, infraestructura. |
| Objetivos generales | Entidades o personas que representan una ideología en particular. |
| Objetivo específico preferido | Alto perfil, alta visibilidad. |

Las comunidades se dividen en **INTERNAS** y **EXTERNAS**. La correspondencia exacta característica↔columna en la lámina original no es recuperable del texto extraído: el mapeo de arriba es la reconstrucción más razonable **(inferencia)**.

---

##### Escalas de valoración y fórmula de severidad

###### Definiciones base

| Componente | Definición del material |
|---|---|
| **IMPACTO** | Consecuencias de un incidente o evento (efecto de amenazas / oportunidades explotando las vulnerabilidades / fortalezas de los activos). |
| **PROBABILIDAD** | Incertidumbre de que el incidente o evento se produzca o no. |

###### Fórmula

**SEVERIDAD = PROBABILIDAD × IMPACTO**

El material la llama indistintamente "estado del riesgo, exposición o severidad".

###### Formas de evaluación

| Forma | Cómo se calcula |
|---|---|
| **Cualitativa** | Se calcula utilizando escalas de probabilidad e impacto. Se visualiza con la **Matriz de Riesgo**, que "permite visualizar, cuantificar, transferir o mitigar los riesgos y tomar decisiones". |
| **Cuantitativa** | Se calcula numéricamente. |

###### Escala de PROBABILIDAD

| Valor | Nivel | Descripción del material |
|---|---|---|
| 1 | RARO | La probabilidad de que ocurra es casi nula. |
| 2 | POCO PROBABLE | Probabilidad baja, aunque puede presentarse. |
| 3 | MODERADO | El riesgo puede materializarse en cualquier momento. |
| 4 | PROBABLE | La materialización del riesgo es alta, suele presentarse. |
| 5 | CASI SEGURO | Muy alta probabilidad de ocurrencia. |

###### Escala de IMPACTO — "nivel de afectación que causaría en la empresa"

| Valor | Nivel | Descripción del material |
|---|---|---|
| 1 | INSIGNIFICANTE | No es problema para la organización. |
| 2 | MENOR | La materialización del riesgo genera impacto mínimo. |
| 3 | SIGNIFICATIVO | Puede causar pérdida momentánea. |
| 4 | MAYOR | Genera retrasos importantes que afectan cumplimiento de objetivos. |
| 5 | SEVERO | Puede detener la operación de la empresa y hasta cierre. |

###### Inconsistencia a tener en cuenta entre láminas

El PPT define las escalas dos veces y **no coinciden en el punto de arranque**:

| Lámina | Probabilidad | Impacto |
|---|---|---|
| 40 ("La SEVERIDAD puede evaluarse de dos formas") | **0-Imposible, 1-Raro a 5-Casi seguro (>60%)** | **0-Insignificante a 5-Severo** |
| 42 (escalas detalladas) | 1-Raro a 5-Casi seguro | 1-Insignificante a 5-Severo |

La lámina 40 agrega un nivel **0 = Imposible** en probabilidad, y ancla **"Casi seguro" a >60%** — único dato numérico de la escala en todo el material. También coloca "Insignificante" en 0 en lugar de 1. La lámina 42, que es la que desarrolla las escalas, usa 1-5 en ambas. **Para el TP conviene usar 1-5 (lámina 42), que es la escala desarrollada, y mencionar el 0-Imposible como caso degenerado.** (inferencia)

La **matriz de riesgo** aparece como imagen en la lámina 41: **no hay valores, colores ni umbrales de corte transcriptos en el material** — no se puede reconstruir qué combinación probabilidad×impacto cae en cada zona.

###### Valoración del IMPACTO en la evaluación cuantitativa

Para definir el valor del impacto se puede recurrir a:
- El **valor que el activo tiene para la organización**.
- La **magnitud de la pérdida** que sufriría la organización si el activo fuese afectado.

Dimensiones de valoración:

| Dimensión | Criterio del material |
|---|---|
| Confidencialidad | Asociada a la información y derivada del marco regulador externo o de criterios internos. **Alta valoración cuando su revelación causara graves daños a la organización.** |
| Disponibilidad | En función del **número de personas afectadas** por falta de disponibilidad o por un funcionamiento irregular. |
| Integridad | En función del **daño de su alteración**, voluntaria o intencionada. |

---

##### Priorización, riesgo inherente y riesgo residual

###### Riesgo inherente

La valorización del riesgo permite establecer el **riesgo inherente** (comúnmente mencionado solo como "riesgo"): el riesgo que se presenta **sin aplicar ninguna medida** sobre las amenazas (u oportunidades), vulnerabilidades, impacto o probabilidad, es decir sin aplicar ninguna estrategia para disminuir (o aumentar) su severidad.

###### Priorización con Pareto 80-20

| Paso | Acción |
|---|---|
| 1 | Listar los riesgos inherentes y aplicar **PARETO 80-20** (el 80% de la severidad está cubierta por el 20% de los riesgos). |
| 2 | Ordenar la lista en forma **decreciente por severidad**. |
| 3 | Seleccionar los riesgos cuya **suma de severidad sea el 80% de la Σ Severidad**. |

Estructura de la planilla de priorización que da la cátedra:

| Id | Especificación Riesgo | Categoría | Valor Probabilidad | Escala de Probabilidad | Valor Impacto | Escala de Impacto | Severidad |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | **Σ Severidad** | |

"Categoría" es la clasificación **SEI**. "Escala" es el nombre del nivel (RARO, MODERADO, etc.) que corresponde al valor numérico. (inferencia)

###### Riesgo residual

Comprende los peligros que persisten **una vez implementados todos los controles y medidas de prevención** existentes respecto de los riesgos inherentes. Nunca podrá reducirse a cero, pero se puede trabajar sobre las medidas que reduzcan su impacto.

> Mientras que el riesgo inherente es el existente al no aplicar ningún tipo de acción para alterar su probabilidad o impacto, el **riesgo residual es el que persiste después de implementados los controles o medidas de mitigación**.

Ejemplo del material: después de implementar cinturones de seguridad y airbags en un automóvil, aún existe riesgo residual de accidente, pero la gravedad y la probabilidad se redujeron significativamente.

**Punto clave para el TP:** *"La especificación del riesgo no ha variado. Sólo su severidad."* Una vez establecidas las estrategias de tratamiento hay que **volver a calcular la severidad** — ese nuevo valor es el riesgo residual, que es el riesgo que la organización está dispuesta a aceptar.

###### Secuencia completa del método

```
IDENTIFICAR ACTIVOS
IDENTIFICAR AMENAZAS Y VULNERABILIDADES        ┐
ESPECIFICAR EL RIESGO y CLASIFICARLO (SEI)     ├── Riesgo INHERENTE
VALORIZAR LA SEVERIDAD DEL RIESGO (FAIR)       ┘
PRIORIZAR LOS RIESGOS PARA SU TRATAMIENTO (Pareto)
APLICAR ESTRATEGIAS DE TRATAMIENTO             ┐
VALORIZAR LA SEVERIDAD DEL RIESGO              ┴── Riesgo RESIDUAL
```

---

##### Qué NO está en el material (no completado de memoria)

- **Las seis "formas de pérdida" (forms of loss) del FAIR canónico** — productividad, respuesta, reemplazo, multas y sentencias, ventaja competitiva, reputación — **no figuran como tales en ninguno de los cuatro archivos**. Lo que la cátedra usa en su lugar es el corte **factores primarios / factores secundarios** con las cuatro áreas (Activo, Amenaza, Organización, Ambiente externo), transcripto completo arriba. Los nombres "Productividad", "Ventaja Competitiva", "Reputación" y "Legal/Regulatoria" sí aparecen, pero como **factores del activo**, no como las seis categorías de pérdida.
- **Anexo 3: Descripción de la Taxonomía SEI** — la lámina lo referencia; no está entre los archivos leídos. Sin él, cada subcategoría SEI queda sin definición.
- **Valores y umbrales de la Matriz de Riesgo** (lámina 41): la matriz es una imagen, no hay texto extraíble.
- **Controles y atributos ISO 27002** (láminas 14, 15 y 56): son imágenes; el material remite a la planilla `ASI-2-Anexo6_ISO 27002 Controles.xlsx`, no incluida.
- **Fórmula cerrada de vulnerabilidad en FAIR**: solo hay el ejemplo numérico 80% vs 90%, sin formalización.
- **Etapas de un ciberataque**: la lámina 9 remite a "ANEXO II: ETAPAS DE UN CIBERATAQUE"; el Anexo II leído es el de FAIR, no el de etapas de ciberataque. Son documentos distintos con la misma numeración de anexo en el PPT.
- **Planilla de Riesgo** (`ASI-2-T1-AdminRecursosAreaTI-Riesgos_Anexo5_PlanillaRiesgo.docx`) y **contexto PINAIRES** (tinyurl ASI-CTX-Pinaires): referenciados como insumo de las actividades del TP, no incluidos.


---


##### Gestión de Servicios de TI (ITIL) — PPT de cátedra

###### Encuadre: de dónde viene ITSM

Evolución de modelos relacionados con TI (lámina de introducción):

| Modelo | Actitud | Foco |
|---|---|---|
| Tradicional | REACTIVA ante la ocurrencia de problemas | La tecnología |
| Orientado al Negocio | PROACTIVA | Los procesos |

Marcos de trabajo que menciona el PPT para el modelo orientado al negocio: **ITIL** (Information Technology Infrastructure Library), **eSCM** (enabled Service Capability Model), **COBIT 2019**.

**ITSM (IT Service Management)**: "disciplina basada en procesos, enfocada en alinear los servicios de TI proporcionados con las necesidades de las Organizaciones, poniendo énfasis en los beneficios que puede percibir el Cliente final".

La lámina "Relación con otras prácticas" ubica a ITSM/ITIL en una dinámica de organización de TI tensionada por: demandas de clientes (constantemente cambiantes y crecientes), tecnología (cambiante y cada vez más compleja), profesionalización de la dirección de proyectos (PMI), normas y marcos de trabajo (CMMi, ISO, COBIT), estrategia de TI (IT Governance) y cultura organizacional / estrategia del cambio organizacional (Corporate Governance). *(La lámina vino mal convertida del PPT — es un diagrama de bloques; se reconstruyó el sentido a partir de los fragmentos de texto.)*

###### Conceptos previos de servicio

**Servicio**: "Conjunto de recursos provisto a los clientes para apoyarlo en la operación de una o más áreas de negocio. Es percibido como algo único y completo."

Particularidades en TI:
- Es el resultado de la interacción de un Cliente con la organización de TI proveedora.
- A diferencia de la manufactura, cliente y proveedor pueden realizar cambios *mientras* el servicio se está desarrollando.
- Refiere a la administración completa de la infraestructura de TI (hardware, software, herramientas) y relaciones con los clientes.
- Que el servicio complete las expectativas del cliente depende de **cómo se acordaron los niveles de servicio**, más que de cómo el proveedor lo haya realizado.

**Calidad** (ISO 8402, complemento de ISO 9000): "Conjunto de propiedades y características de un producto o servicio que le confieren su aptitud para satisfacer necesidades explícitas o implícitas". La calidad de un servicio refiere a cuánto satisfizo el servicio las expectativas del cliente, medido según el SLA y a un costo razonable acordado.

**Valor**: está en el resultado del servicio y el impacto que éste tiene en el negocio del cliente, **no en el servicio en sí mismo**. El servicio debe aportar valor sin que el cliente asuma los riesgos y costos específicos de su prestación.

| Utilidad | Garantía | Riesgos |
|---|---|---|
| Cumple con requisitos | Capacidad | Pérdida de control del proceso |
| Mejora rendimiento | Seguridad | Costos ocultos |
| Disminuye costos | Continuidad | Baja calidad |
| Contribuye a aumentar ingresos | Disponibilidad | "Caer cautivos" |

*(El PPT deja como ejercicio: contratar una desarrolladora para hacer un ERP e identificar Utilidad, Garantía y Riesgo.)*

**Activos del servicio**: dos componentes — **recursos** ("materia prima" necesaria para la prestación del servicio) y **capacidades** (habilidades para transformar recursos en valor; recurso que aporta profesionalidad, creatividad y capacidad de liderazgo). *(El PPT no rotula explícitamente los términos "recursos" y "capacidades" en el texto convertido, pero es la dupla estándar de ITIL y las dos definiciones que sí aparecen se corresponden con ella — inferencia.)*

**Administración de la relación con el cliente** — los tres tipos de acuerdo:

| Sigla | Nombre | Entre quiénes |
|---|---|---|
| SLA | Service Level Agreement (Acuerdo de Nivel de Servicio) | Organización de TI ↔ Cliente |
| OLA | Operational Level Agreement (Acuerdo de Nivel Operacional) | Interno: Mesa de Ayuda ↔ segunda línea de soporte |
| UC | Underpinning Contract (Contrato de Soporte) | Organización de TI ↔ proveedor tercerizado |

###### ITIL 4: estructura general

**ITIL**: marco de trabajo que presenta las mejores prácticas para gestionar servicios de TI y mejorar el soporte de TI y los niveles de servicio. Objetivo principal: garantizar que los servicios de TI se alineen con los objetivos empresariales, incluso cuando estos cambien.

**ITIL 4** — objetivo: centrarse en el ciclo de vida del servicio y alinear las TI con el negocio. Enfoque: ágil. Introduce el modelo de cuatro dimensiones del Sistema de Valor del Servicio (SVS).

**Las 4 dimensiones del SVS:**

| Dimensión | Qué abarca |
|---|---|
| Organizaciones y Personas | Aspectos organizacionales y de RRHH de una empresa |
| Información y Tecnología | Elementos técnicos que forman parte de la oferta de servicios |
| Socios y Proveedores | Relaciones de la empresa con otras involucradas en la co-creación de valor |
| Flujos de Valor y Procesos | Actividades y métricas necesarias para lograr de manera consistente los resultados esperados |

**Cadena de Valor del Servicio**: modelo operativo que describe 6 actividades clave necesarias para responder a la demanda y facilitar la creación de valor a través de la creación y gestión de productos y servicios.

1. Planificación
2. Demanda / Contacto
3. Diseño y transición
4. Obtención / Construcción
5. Entrega y apoyo
6. Mejora

**Prácticas**: ITIL 4 utiliza "procesos" para gestionar los servicios de TI, denominándolos **"prácticas"**. Cuenta con **34 prácticas** agrupadas en 3 categorías:

| Categoría | Cantidad | Origen |
|---|---|---|
| Prácticas generales de gestión | 14 | Las que vienen del mundo empresarial y de la gestión propia del negocio |
| Prácticas de gestión de servicios de TI | 17 | Las desarrolladas para la Gestión de Servicios de TI (ITSM) |
| Prácticas de gestión técnica | 3 | Las que vienen de los dominios netamente tecnológicos |

**Listado completo de las 34 prácticas (tal como las lista el PPT):**

| Gestión General (14) | Gestión de Servicios de TI (17) | Gestión Técnica (3) |
|---|---|---|
| Gestión de estrategia | Análisis de negocio | Gestión de la implementación |
| Gestión de portfolio | Gestión del catálogo de servicios | Gestión de infraestructura y plataformas |
| Gestión de arquitectura | Diseño de servicios | Desarrollo y gestión de software |
| Gestión financiera de servicios | Gestión del nivel de servicio | |
| Gestión de personal y talento | Gestión de la disponibilidad | |
| Mejora continua | Gestión de capacidad y rendimiento | |
| Medición e informes | Gestión de continuidad del servicio | |
| Gestión de riesgos | Gestión y monitorización de eventos | |
| Gestión de la seguridad y de la información | Asistencia al cliente | |
| Gestión del conocimiento | Gestión de incidentes | |
| Gestión del cambio organizacional | Gestión de solicitudes de servicio | |
| Gestión de proyectos | Gestión de problemas | |
| Gestión de las relaciones | Gestión de versiones | |
| Gestión de suministros | Control de cambios | |
| | Validación y pruebas del servicio | |
| | Gestión de configuración del servicio | |
| | Gestión de activos de TI | |

**Prácticas que el PPT desarrolla en profundidad** ("las más relevantes en relación a la Gestión de Riesgos y a la Optimización de la Administración de los Recursos" — las llama **procesos de soporte de TI**):

- Gestión de incidentes
- Gestión y monitorización de eventos
- Gestión de solicitudes de servicio
- Gestión de problemas
- Gestión de versiones
- Control de cambios
- Gestión de la configuración del servicio
- Gestión de activos de TI

###### Centro de Servicios (Service Desk)

**Definición**: Centro de Servicios (**SPOC**, Single Point Of Contact) es el único punto de contacto para los usuarios de Gestión de Incidentes y Gestión de Solicitudes.

Distinción de figuras:

| Figura | Alcance |
|---|---|
| Service Desk (Centro de Servicios) | El punto único de contacto integral |
| Call Center (Centro de asistencia) | Gestionar un alto volumen de llamadas y redirigir a los usuarios |
| Help Desk (Mesa de ayuda) | Soporte técnico, gestión de incidencias |

**Canales de acceso** que brinda: telefónico; portales de servicios y aplicaciones móviles; chat; correo electrónico; centros de servicios sin cita; mensajes de texto y de redes sociales; foros de discusión y redes sociales públicas y corporativas.

**Herramientas de apoyo requeridas:**

| Herramienta | Para qué |
|---|---|
| Sistemas de Tickets (plataformas ITSM) | Clasificación, escalado, interacción con la CMDB y la KB |
| De colaboración | Slack, MS Teams, chat integrado a plataformas ITSM |
| CMDB (Base de Datos de Configuraciones) | Elementos de configuración de hardware, software, documentación y personas de la infraestructura del cliente, y los servicios que se le prestan |
| KB (Base de Datos de Conocimiento) | Protocolos de interacción con el cliente (guiones, checklists), formación sobre productos y servicios |

**Estructuras físicas posibles**: Centralizada, Distribuida, Virtual. *(El PPT dedica una lámina a cada una, pero son diagramas sin texto convertible — el .md no trae la descripción de ninguna de las tres.)*

###### Escalamiento (tipos)

Ocurre cuando el Centro de Servicios no es capaz de resolver un incidente en primera instancia y debe recurrir a alguien más.

| Tipo | Cuándo se aplica | A quién se recurre |
|---|---|---|
| **Funcional** | Cuando se requiere apoyo de un especialista de más alto nivel para resolver el problema | Segunda línea de soporte, que puede ser personal abocado a la Gestión de Problemas |
| **Jerárquico** | Cuando hay que tomar decisiones que se escapan de las atribuciones asignadas a ese nivel (ej.: asignar más recursos para la resolución de un incidente específico) | Un responsable de mayor autoridad |

Regla mnemotécnica: funcional = falta **conocimiento técnico** (se mueve horizontal/hacia especialistas); jerárquico = falta **autoridad o recursos** (se mueve vertical/hacia arriba). *(Inferencia — el PPT no lo formula así.)*

###### Gestión y Monitorización de Eventos

**Evento** (definición literal del PPT): "Cuando las interrupciones de servicio o la reducción de su calidad son monitorizadas". *(La definición del PPT está mal redactada respecto del estándar ITIL: un evento es cualquier cambio de estado significativo detectado por monitoreo, no necesariamente una interrupción. La lámina de objetivos, que habla de "registrar e informar cambios de estado seleccionados identificados como eventos", es coherente con la definición estándar. Contradicción interna del material — observación.)*

**Objetivos:**
- Observar sistemáticamente los servicios y sus componentes.
- Registrar e informar cambios de estado seleccionados identificados como eventos.
- Identificar y priorizar la infraestructura, los servicios, los procesos comerciales y los eventos de seguridad de la información.
- Establecer la respuesta adecuada a esos eventos.

**Clasificación de eventos (los tres niveles):**

| Nivel | Definición del PPT | Adónde deriva |
|---|---|---|
| **Informativos** | No requieren acción en el momento en que se identifican | Se usan para **Gestión de Problemas** |
| **De advertencia** | Permiten tomar medidas **antes** de experimentar impacto negativo | Disparan **Estrategias de Tratamiento en Gestión de Riesgos** |
| **Excepciones** | Indican que se ha identificado una **infracción a una norma establecida** | Disparan **Planes de Contingencia en Gestión de Riesgos** |

El nivel de advertencia es, en la práctica, el disparo de un **umbral** definido sobre una métrica del CI antes de que se viole la norma; la excepción es el cruce de la norma misma. *(Inferencia — el PPT usa la palabra "norma establecida" pero no habla explícitamente de "umbrales" ni define cómo se fijan.)*

**Tipos de herramientas de monitorización:**

| Tipo | Cómo opera |
|---|---|
| **ACTIVA** | Comprueba los CI uno a uno para verificar su estado y disponibilidad. Si detecta excepciones, genera una alerta y la envía al equipo o mecanismo de control asignado |
| **PASIVA** | Detectan y **correlacionan** alertas operacionales generadas por los propios CI. Ejemplo: archivos de logs |

La **correlación** aparece en dos lugares del PPT: (a) como función propia de la monitorización pasiva (correlacionar alertas generadas por los CI), y (b) en la etapa de clasificación de la actividad, donde "se analiza si existen eventos similares"; el KPI "Eventos duplicados" existe justamente "para optimizar la función de correlación".

**Actividades (flujo):**

`Disparador del Evento → Detección y Filtrado → Registro → Clasificación → Respuesta → Cierre`

Apoyado en: SLA, TICKETS, KB, CMDB.

| Etapa | Contenido |
|---|---|
| Detección y filtrado | Llega notificación a agente o herramienta que interpreta el suceso para determinar si hay que atenderlo |
| Clasificación | Asigna una categoría y un nivel de prioridad. Se analiza si existen eventos similares |
| Selección de respuesta | Se ponen en marcha mecanismos para dar respuesta al evento. Se eligen soluciones a adoptar |

**Interacción con otras prácticas** — los eventos pueden:
- Registrar un Incidente → **Gestión de Incidentes**
- Evidenciar un problema (si son reiterados) → **Gestión de Problemas**
- Requerir un Cambio → **Control de Cambios**

**KPIs de Gestión de Eventos:**

| KPI | Descripción |
|---|---|
| Eventos clasificados | Número de eventos, por categorías y por impacto. Número y porcentaje de cada tipo de evento, por plataforma o aplicación |
| Intervención en eventos | Número y porcentaje de eventos que requirieron intervención humana, y cómo fue esa intervención |
| Escalado para resolución | Número y porcentaje de eventos que desembocaron en el registro de un nuevo incidente o RFC |
| Eventos reiterados | Número y porcentaje de eventos ocasionados por problemas ya existentes o errores conocidos |
| Eventos duplicados | Número y porcentaje de eventos repetidos o duplicados. Relevante para optimizar la función de correlación |
| Eventos por problemas de capacidad | Número y porcentaje de eventos relacionados con problemas de rendimiento |
| Eventos por problemas de disponibilidad | Número y porcentaje de eventos que indican futuros problemas de disponibilidad |
| Ratio de Incidentes por Eventos | Número y ratio de eventos por comparación al número de incidentes |

###### Gestión de Incidentes

**Incidente**: "una interrupción no planificada de un servicio o la reducción de la calidad de un servicio". Pueden afectar a una actividad, a un proceso, a un usuario o incluso a la totalidad de la organización, y son informados por usuarios, soporte técnico, entre otros.

**Objetivos:**
- Minimizar el impacto negativo de los incidentes.
- Recuperar rápidamente el funcionamiento normal del servicio.
- Activar soluciones temporales o permanentes.

**Relación con la Gestión de Riesgos** (eje transversal de la unidad):
- La comunicación del incidente es el **disparador que alerta de la materialización del riesgo**.
- Las soluciones temporales o permanentes son los **Planes de Contingencia y Recuperación**.
- Activa los **Planes de Continuidad de Negocio** relacionados al incidente.

**Ciclo de vida (actividades):**

`Notificación del Incidente → Registro → Clasificación → Análisis y Resolución → Cierre`

Apoyado en: SLA, TICKETS, KB (Base de Conocimiento), CMDB (Base de Datos de Configuraciones).

| Etapa | Pasos que detalla el PPT |
|---|---|
| **Registro** | 1. Admitir/tramitar incidente. 2. Comprobar que ese incidente aún no fue registrado. 3. Asignar referencia (id). 4. Registrar info básica para procesamiento. 5. Información de apoyo. 6. Notificar incidente a otros usuarios |
| **Clasificación** | 1. Asignar categoría. 2. Establecer nivel de **prioridad (impacto y urgencia)**. 3. Asignar recursos: si no lo puedo resolver, un especialista o superior. 4. Asignar tiempo de respuesta esperado |
| **Análisis y Resolución** | 1. Examinar incidente contra la KB para ver si hay uno similar ya resuelto y aplicar ese procedimiento. 2. Si no sabe cómo resolver, envía a investigar por expertos |
| **Cierre** | 1. Confirmar solución con usuarios. 2. Incorporar el proceso de resolución a la KB. 3. Actualizar CMDB sobre el incidente. 4. Cerrar incidente |

**Priorización: impacto y urgencia.** El PPT establece que la prioridad se determina a partir de **impacto** y **urgencia** en la etapa de clasificación, y que en esa misma etapa se asigna el **tiempo de respuesta esperado** (que sale del SLA — el SLA figura como insumo del flujo). El material **no incluye la matriz numérica** impacto × urgencia. Matriz canónica de referencia, no presente en el PPT:

| | Urgencia Alta | Urgencia Media | Urgencia Baja |
|---|---|---|---|
| **Impacto Alto** | 1 – Crítica | 2 – Alta | 3 – Media |
| **Impacto Medio** | 2 – Alta | 3 – Media | 4 – Baja |
| **Impacto Bajo** | 3 – Media | 4 – Baja | 5 – Planificable |

*(Inferencia / conocimiento general de ITIL — no está en el archivo. Impacto = magnitud del daño al negocio, cuántos usuarios/servicios afecta; urgencia = qué tan rápido el negocio necesita la resolución. Si se usa en el TP, aclarar que es una matriz estándar y no del material de cátedra.)*

**Escalamiento**: ver la sección de Centro de Servicios más arriba (funcional y jerárquico). El KPI "Cantidad de escalados" mide los escalados de incidentes **no resueltos en el tiempo acordado**, es decir, el disparo del escalamiento está atado al SLA.

**KPIs de Gestión de Incidentes:**

| KPI | Descripción |
|---|---|
| Cantidad de incidentes repetidos | Cantidad de incidentes repetidos (con métodos ya conocidos para resolución) |
| Incidentes resueltos a distancia | Cantidad de incidentes resueltos a distancia por el Service Desk (p. ej. sin acudir al lugar del usuario) |
| Cantidad de escalados | Cantidad de escalados de incidentes no resueltos en el tiempo acordado |
| Cantidad de incidentes | Cantidad de incidentes registrados por el Service Desk, agrupados por categoría |
| Tiempo de resolución de incidente | Tiempo medio para resolver un incidente, agrupados por categorías |
| Tasa de Resolución de Primera Llamada | Porcentaje de incidentes resueltos en el Service Desk durante la primera llamada, agrupados por categorías |
| Resolución dentro del SLA | Porcentaje de incidentes resueltos durante el tiempo acordado en el SLA, agrupados por categorías |
| Esfuerzo de resolución de incidente | Promedio de esfuerzo de trabajo para resolver incidentes, agrupados por categorías |

###### Gestión de Solicitudes de Servicio

**Definición**: "Es la encargada de atender las solicitudes de los usuarios proporcionándoles información y acceso rápido a los servicios estándar de la organización TI."

**Tipos de solicitudes**: de información o consejo; de **cambios estándar**; de acceso a los servicios.

**Objetivos**: proporcionar al departamento comercial acceso rápido a servicios estándar; reducción de costos.

**Ejemplos que da el PPT:**

| Tipo | Ejemplo |
|---|---|
| Solicitudes de acceso | A sistemas, aplicaciones o recursos específicos: gestión de cuentas de usuario, restablecimiento de contraseñas, cambios de permisos |
| Requerimientos de hardware | Periféricos o equipos: laptops, impresoras, dispositivos móviles |
| Pedidos de instalación de software | Nuevas aplicaciones en los aparatos de un usuario |
| Peticiones de información | Orientación sobre servicios, procesos o procedimientos. Incluye documentación |
| Demandas de pequeños cambios de configuración | Ajustes en la configuración del sistema del dispositivo del usuario final |
| Exigencia de reportes | Generación o entrega de informes, o análisis de datos |
| Solicitudes de formación | Capacitaciones, talleres o tutoriales sobre uso de aplicaciones o herramientas |

**Actividades (flujo):**

`Solicitud → Aprobación Financiera → Tramitación → Cierre`

| Etapa | Contenido |
|---|---|
| Selección de solicitudes | Los usuarios emiten sus peticiones, que se clasifican en función de criterios predefinidos |
| Aprobación financiera | Dado que la mayoría de las solicitudes tienen implicaciones financieras, se considera su costo y se decide si tramitar la solicitud o no |
| Tramitación | La solicitud se asigna a las personas adecuadas según cada caso para su resolución |
| Cierre | Tras notificar al Centro de Servicios y comprobar que el usuario quedó conforme con la gestión, se procede a cerrarla |

**KPIs de Gestión de Solicitudes de Servicio:**

| KPI | Descripción |
|---|---|
| Solicitudes de Servicio procesadas | Cantidad total de solicitudes de servicio |
| Estado de Solicitudes de Servicio | Desglose en cada etapa: registrada, aprobada, cerrada, etc. |
| Solicitudes Pendientes | Tamaño de la lista de solicitudes de servicio pendientes |
| Tiempo de atención de solicitudes | Promedio de tiempo de atención por tipo |
| Solicitudes finalizadas con éxito | Cantidad y porcentaje de solicitudes completadas de acuerdo a los tiempos acordados |
| Costo promedio | Costo promedio por tipo de solicitud |
| Nivel de Satisfacción del cliente | Satisfacción con el tratamiento de la solicitud, medida por encuestas |

###### Gestión de Problemas

**Problema**: "una causa o causa potencial de incidentes o eventos".

**Incidentes vs. Problemas** (distinción literal del PPT):
- Los **INCIDENTES** son elementos reparables (**break-fix**) que causan un impacto negativo en las personas y, como tales, deben resolverse para restaurar el funcionamiento normal del trabajo.
- Los **PROBLEMAS** causan incidentes o eventos. Deben analizarse e investigarse para que se puedan identificar soluciones temporales o definitivas que reduzcan el número y el impacto de futuros incidentes o eventos.

**Objetivos:**
- Investigar las causas subyacentes a toda alteración.
- Determinar posibles soluciones a las mismas.
- Proponer las Solicitudes de cambio (**RFC**) a Control de Cambios.
- Realizar las Revisiones post Implementación (**PIR**).

**Los dos modos de operar:**

| Modo | Definición del PPT |
|---|---|
| **Reactiva** | Luego de notificado el incidente, lo analiza para descubrir la causa y proponer soluciones |
| **Proactiva** | Monitoriza la calidad de la infraestructura TI y analiza su configuración para prevenir incidentes similares, **antes de que ocurran** |

**Actividades (flujo):**

`Identificación → Registro → Clasificación → Análisis y Diagnóstico → Control de Errores → Cierre`

Apoyado en: CMDB, SLA, KB, y con interfaz hacia **Control de Cambios**.

| Etapa | Contenido |
|---|---|
| **Identificación y Registro** | Se identifican problemas **reales y potenciales**. Se registra con info sobre los CI implicados, causas, síntomas, soluciones temporales, servicios involucrados, niveles de urgencia, prioridad e impacto, estado |
| **Análisis y Solución** | Se investigan soluciones, evaluando su impacto en la infraestructura TI, los costos y sus consecuencias sobre los SLA. Si el impacto del problema puede tener consecuencias graves en la calidad de servicio, emite una **RFC de emergencia** para Control de Cambios |
| **Control de Errores** | Registra errores y propone soluciones mediante Solicitudes de cambio (RFC), enviadas a Control de Cambios |
| **Cierre / PIR** | Una vez efectuado el cambio, efectúa la **PIR** (Post Implementation Review) de los mismos |

**Error conocido y workaround (solución temporal).** El PPT usa ambos conceptos pero no los define formalmente:
- **Solución temporal / workaround**: figura como campo del registro del problema ("soluciones temporales") y en Gestión de Incidentes como "activar soluciones temporales o permanentes". Es la solución que restaura el servicio sin eliminar la causa raíz. *(La caracterización "sin eliminar la causa raíz" es inferencia; el PPT solo la nombra.)*
- **Error conocido**: aparece nombrado en la etapa de Control de Errores, en el KPI "Cantidad de incidentes por problema conocido", en las razones para hacer cambios ("solución de errores conocidos") y en el origen de las RFC ("Gestión de Problemas: propone soluciones a errores conocidos"). Es un problema con causa raíz identificada y, en general, con un workaround documentado. *(La definición explícita es inferencia — el PPT no la enuncia.)*
- **RCA (Root Cause Analysis)**: el PPT **no usa la sigla ni describe ninguna técnica de análisis de causa raíz** (ni Ishikawa, ni 5 porqués, ni Pareto). Lo más cercano es el objetivo "investigar las causas subyacentes a toda alteración" y el KPI "Tiempo hasta la identificación del problema", definido como el tiempo entre la primera aparición de un incidente y **la identificación de la raíz del problema**. Si el TP exige RCA, hay que traerlo de otra fuente.

**KPIs de Gestión de Problemas:**

| KPI | Descripción |
|---|---|
| Cantidad de problemas | Cantidad de problemas registrados, agrupados por categorías |
| Tiempo de resolución de problemas | Tiempo medio para resolver problemas, agrupados por categorías |
| Cantidad de incidentes por problema | Cantidad media de incidentes vinculados al mismo problema **antes** de identificar el problema |
| Cantidad de incidentes por problema conocido | Cantidad media de incidentes vinculados al mismo problema **después** de identificar el problema |
| Tiempo hasta la identificación del problema | Tiempo medio entre la primera aparición de un incidente y la identificación de la raíz del problema |
| Esfuerzo de resolución de problemas | Tiempo medio de esfuerzo de trabajo para resolver problemas, agrupados por categorías |

###### Control de Cambios

Encuadre del PPT: "Lo único inmutable es el cambio". El cambio suele ser fuente de problemas y no debe hacerse sin evaluar bien sus consecuencias, pero puede resultar mucho más peligroso el estancamiento en servicios y tecnologías desactualizados.

**Objetivo**: "Evaluación y planificación del proceso de cambio para asegurar que se realice en forma eficiente, asegurando en todo momento la calidad y continuidad del servicio TI."

**Principales razones para realizar cambios en la infraestructura TI:**
- Solución de errores conocidos.
- Desarrollo de nuevos servicios.
- Mejora de los servicios existentes.
- Imperativo legal.

**Origen de las RFC (Request for Change):**

| Origen | Qué dispara |
|---|---|
| Gestión de Problemas | Propone soluciones a errores conocidos |
| Gestión de Solicitudes de Servicios | Requiere cambios de la infraestructura TI |
| Estrategia empresarial | La dirección decide una redirección estratégica |
| Actualizaciones de software de terceros | Los proveedores dejan de soportar versiones anteriores |
| Imperativo legal | Cambio de legislación |

**Participantes de la práctica:**

| Rol | Definición |
|---|---|
| **Gestor de Cambios** | Responsable del proceso del cambio |
| **CAB** (Consejo Asesor de Cambios / Change Advisory Board) | Órgano interno formado por representantes de áreas de la gestión de servicios TI |
| **ECAB** (Comité de emergencia / Emergency CAB) | Se forma en casos de necesidad |

**Actividades (flujo):**

`RFC → Aceptación o Rechazo → Clasificación → Aprobación y Planificación → Implementación del Cambio → Evaluación del Cambio → Cierre`

Apoyado en: KB, CMDB, y con interfaz hacia **Gestión de la Configuración**, **Gestión de Versiones** y **Gestión de Problemas**.

| Etapa | Contenido |
|---|---|
| Aceptación o rechazo | La RFC puede ser rechazada si el cambio no está justificado |
| Clasificación | Establecer prioridad y categoría dependiendo de **urgencia e impacto** |
| Evaluación del cambio | Antes de cerrar el cambio, verificar que ha sido positivo para el servicio |

**Tipos de cambio (estándar / normal / emergencia).** El PPT **no presenta la taxonomía de tres tipos de forma explícita en una sola lámina**, pero los tres aparecen dispersos:
- **Estándar**: nombrado en Gestión de Solicitudes de Servicio, como uno de los tipos de solicitud ("de cambios estándar") — o sea, el cambio pre-aprobado y de bajo riesgo se canaliza por Solicitudes de Servicio, no por el flujo completo de RFC.
- **Normal**: es el flujo completo descripto arriba (RFC → CAB → aprobación → implementación → PIR). El PPT no lo llama "normal".
- **Emergencia**: nombrado en Gestión de Problemas ("emite una RFC de emergencia para Control de Cambios") y en el KPI "Cantidad de cambios urgentes: cantidad de cambios urgentes evaluados por el ECAB".

Cuadro de reconstrucción (**inferencia**, armado con las piezas del PPT más el estándar ITIL — marcar como tal si se usa en el TP):

| Tipo | Aprobación | Flujo | Evidencia en el PPT |
|---|---|---|---|
| **Estándar** | Pre-aprobado, no requiere CAB | Vía Gestión de Solicitudes de Servicio | "Tipos de solicitudes: de cambios estándar" |
| **Normal** | Requiere evaluación y aprobación del CAB | RFC completo con planificación y PIR | Flujo de actividades y KPIs de CAB |
| **Emergencia** | ECAB | RFC de emergencia, acelerado | "RFC de emergencia", "Comité de emergencia (ECAB)", KPI "Cantidad de cambios urgentes" |

**Rollback / back-out**: el PPT lo define en la nota al pie de la lámina de métricas — "**back-out: roll-back o plan de retirada, es un plan que siempre debería existir al realizar cualquier despliegue**". Se mide con los KPIs "Cantidad de Back-outs" y "Porcentaje de cambios cerrados sin incidencias ulteriores" (cambios que no requirieron ejecutar el plan de back-out).

**PIR (Post Implementation Review)**: revisión posterior a la implementación de un cambio. En el PPT la ejecuta la **Gestión de Problemas** ("Una vez efectuado el cambio, efectúa la PIR de los mismos") y se mide con el KPI "Evaluaciones post-implementación". Se corresponde con la etapa "Evaluación del Cambio" del flujo de Control de Cambios: verificar que el cambio ha sido positivo para el servicio antes de cerrarlo.

**KPIs de Control de Cambios:**

| KPI | Descripción |
|---|---|
| Cantidad de cambios solicitados | Cantidad de cambios (RFC) evaluados por el CAB |
| Cantidad de reuniones de CAB | Cantidad de reuniones con información estadística asociada: nº de asistentes, duración, nº de cambios aprobados por reunión, etc. |
| Tasa de aceptación de cambios | Cantidad de RFC aceptadas vs. rechazadas |
| Número de cambios clasificados | Nº de cambios realizados clasificados por impacto y prioridad, filtrados temporalmente |
| Tiempo para autorización para cambios | Tiempo medio desde la solicitud de una RFC a Gestión de Cambios hasta la autorización del cambio |
| Tiempo medio del cambio | Tiempo medio desde la autorización de una RFC hasta su cierre, dependiendo del impacto y la prioridad |
| Porcentaje de cambios exitosos | Porcentaje de cambios exitosos en primera instancia, segunda, etc. |
| Cantidad de Back-outs | Número de back-outs con una detallada explicación de los mismos |
| Porcentaje de cambios cerrados sin incidencias ulteriores | Cantidad de cambios que no han requerido ejecución de planes de back-out |
| Incidencias asociadas a cambios realizados | Cantidad de incidencias detectadas asociadas a cambios realizados después de su cierre |
| Cantidad de cambios urgentes | Cantidad de cambios urgentes evaluados por el ECAB |
| Evaluaciones post-implementación | Cantidad de PIR realizadas posteriores a la implementación de un cambio |

###### Gestión de la Configuración del Servicio y Gestión de Activos de TI

Encuadre: "Es esencial conocer en detalle la infraestructura TI de nuestras organizaciones para obtener el mayor provecho de la misma."

**Objetivos, separados por práctica:**

| Práctica | Objetivos |
|---|---|
| **Gestión de la Configuración del Servicio** | Mantenimiento de la Base de Datos de Gestión de la Configuración (**CMDB**). Gestión de los elementos de configuración (**CI**) |
| **Gestión de Activos de TI** | Gestiona activos de TI **a lo largo de su ciclo de vida completo, desde la adquisición hasta la disposición**. Objetivo: maximizar el valor de los activos de TI y optimizar su rendimiento, costo y riesgo asociado |

Diferencia operativa: Configuración se ocupa de **cómo se relacionan** los componentes para prestar el servicio; Activos se ocupa del **valor económico y el ciclo de vida** de esos componentes. *(Inferencia a partir de los dos bloques de objetivos — el PPT los presenta juntos sin contrastarlos explícitamente.)*

**CI (Configuration Item)**: elementos de la infraestructura de TI y servicios asociados. El PPT enumera qué cuenta como CI: **hardware, software, documentación, personas, procesos y demás componentes para entregar y soportar los servicios de TI**. La lámina del Centro de Servicios agrega la misma enumeración para la CMDB: "elementos de configuración de hardware, software, documentación y personas de la infraestructura del cliente y los servicios que se le prestan".

**Atributos de un CI**: el PPT **no da una lista de atributos**. Lo que sí indica es que los CI se clasifican "según **tipo, función y relación con otros CI**", y que el registro asociado a un problema guarda "info sobre los CI implicados". Cualquier lista de atributos más completa (ID único, versión, propietario, estado, ubicación, licencia, fecha de adquisición) hay que traerla de otra fuente. *(Observación — no está en el archivo.)*

**Actividades (flujo):**

`Identificación de CI → Registro y Clasificación → Control de la Configuración → Auditoría y Verificación → Gestión de Relaciones y Dependencias → Reportes y Análisis de Configuración → Gestión de Versiones y Baselines` — todas girando alrededor de la **CMDB**.

| Actividad | Contenido |
|---|---|
| **Identificación de CI** | Identificar los CI de la infraestructura de TI y servicios asociados (hardware, software, documentación, personas, procesos y demás componentes para entregar y soportar los servicios de TI) |
| **Registro y Clasificación de CI** | Registrar cada CI en la CMDB y clasificarlos según tipo, función y relación con otros CI, para mantener inventario de todos los componentes de la infraestructura de TI y los servicios asociados |
| **Control de la Configuración** | Establecer controles y procedimientos para gestionar cambios en la configuración de los CI (autorizar, registrar, evaluar y aprobar cambios de configuración, así como gestionar la implementación de cambios de forma controlada) |
| **Auditoría y Verificación de CI** | Realizar auditorías regulares de precisión e integridad de la información de configuración en la CMDB, para tener siempre actualizado el estado de la infraestructura de TI y servicios asociados |
| **Gestión de Relaciones y Dependencias** | Gestionar relaciones y dependencias entre CI, para comprender **cómo un cambio en un CI afecta a otros CI y a servicios de TI**, y tomar medidas para minimizar impactos negativos |
| **Reportes y Análisis de Configuración** | Generar informes y análisis sobre la configuración de la infraestructura de TI y servicios asociados (métricas de rendimiento, tendencias de cambio, cumplimiento de políticas y requisitos regulatorios, etc.) |
| **Gestión de Versiones y Baselines** | Mantener un registro histórico de cambios y facilitar la **reversión a estados anteriores** si es necesario, para garantizar integridad y consistencia de la configuración |

Las **relaciones entre CI** son, junto con el inventario, lo que distingue una CMDB de un simple inventario de activos: permiten el análisis de impacto ("cómo un cambio en un CI afecta a otros CI y a servicios de TI"). El PPT no enumera tipos de relación (contiene / depende de / se conecta a / es instancia de). *(Observación — la taxonomía de relaciones no está en el archivo.)*

**KPIs de Gestión de la Configuración y Activos:**

| KPI | Descripción |
|---|---|
| Frecuencia de verificación | Frecuencia de verificaciones físicas |
| Duración de verificación | Duración promedio de verificaciones físicas |
| Esfuerzo para verificaciones | Promedio de esfuerzo de trabajo para verificaciones |
| Cubiertas CMS | Porcentaje de elementos de configuración cuyos datos están incluidos en la CMDB |
| Actualización automática | Porcentaje de elementos de configuración cuyos datos en la CMDB se actualizan automáticamente |
| Cantidad de desvíos | Número de ocasiones en que las auditorías de configuración detectaron incorrecciones en el contenido de la CMDB |
| CIs involucrados en incidentes | Cantidad de CI que han estado involucrados en incidentes |
| Configuraciones no autorizadas | Cantidad de configuraciones detectadas en controles y auditorías que no fueron autorizadas o no cuentan con licencias |
| Costos asociados | Costos asociados a las actividades de Gestión de la Configuración y Activos de Servicio |

###### Gestión de Versiones

**Definición**: "Es la encargada del control de calidad de todo el software y hardware instalado en el entorno de producción."

Funciones:
- Establecer una política de implementación de nuevas versiones de hardware y software.
- Implementar las nuevas versiones en el entorno de producción.
- Garantizar que el proceso de cambio cumpla con las RFC.
- Asegurar el contenido de la CMDB.
- Archivar copias en la **DML**.
- Mantener actualizado el **DS**.

**Versión**: "nuevo grupo de CI modificados que han sido validados para su instalación en el entorno de producción". Las especificaciones funcionales y técnicas de una versión están determinadas en la **RFC correspondiente**.

**Clasificación de versiones según su impacto en la infraestructura TI:**

| Tipo | Definición | Codificación |
|---|---|---|
| **Versiones mayores** | Introducen modificaciones importantes en la funcionalidad, características técnicas, etc. | 1.0, 2.0, etc. |
| **Versiones menores** | Corrección de varios errores conocidos | 1.1, 1.2, 1.3, etc. |
| **Versiones de emergencia** | Reparan de forma rápida un error conocido | 1.1.1, 1.1.2, etc. |

**Repositorios:**

| Sigla | Nombre | Contenido |
|---|---|---|
| **DML** | Biblioteca de Medios Definitivos | Copia de todo el histórico completo del software instalado en el entorno TI: sistemas operativos, aplicaciones, controladores de dispositivos, documentación asociada |
| **DS** | Almacén de Recambios Definitivos | Piezas de repuesto para los CI en el entorno de producción |

**KPIs de Gestión de Versiones:**

| KPI | Descripción |
|---|---|
| Cantidad de versiones | Cantidad de versiones desplegadas en el área de producción de TI, agrupadas en mayores, menores o de emergencia |
| Cantidad de back-outs | Cantidad de versiones que fueron revertidas y razones |
| Cantidad de incidencias | Cantidad de incidencias asociadas a nuevas versiones |
| Cumplimiento de plazos | Cumplimiento de los plazos previstos para cada despliegue |
| Duración de Versiones Mayores | Duración media de versiones mayores, desde su autorización hasta su finalización |
| Proporción de versiones con despliegue automático | Proporción de nuevas versiones distribuidas automáticamente |
| Utilización de recursos | Asignación de recursos para el despliegue de versiones |
| Disponibilidad del Servicio | Disponibilidad del servicio durante y tras el proceso de lanzamiento de la nueva versión |

###### Tabla comparativa: evento vs. incidente vs. problema vs. cambio

| Criterio | **Evento** | **Incidente** | **Problema** | **Cambio** |
|---|---|---|---|---|
| **Definición (PPT)** | Cuando las interrupciones de servicio o la reducción de su calidad son monitorizadas; cambio de estado seleccionado, registrado e informado | Interrupción no planificada de un servicio o reducción de la calidad de un servicio | Una causa o causa potencial de incidentes o eventos | Modificación de la infraestructura TI tramitada vía RFC (el PPT define el proceso, no la palabra "cambio") |
| **Origen / disparador** | Monitorización activa o pasiva de los CI | Reporte de usuario, soporte técnico, o un evento | Uno o varios incidentes/eventos (reactiva), o análisis de la infraestructura (proactiva) | RFC desde Problemas, Solicitudes de Servicio, estrategia empresarial, actualizaciones de terceros, imperativo legal |
| **Naturaleza** | Puede ser inocuo (informativo), preventivo (advertencia) o violación de norma (excepción) | Break-fix: elemento reparable con impacto negativo en las personas | Causa subyacente, real o potencial | Acción planificada y controlada sobre la infraestructura |
| **Objetivo de la práctica** | Observar, registrar, priorizar y establecer la respuesta adecuada | Minimizar impacto y **restaurar rápido** el servicio normal | **Investigar la causa** y determinar soluciones que reduzcan futuros incidentes | Ejecutar el cambio de forma eficiente asegurando calidad y continuidad del servicio |
| **Horizonte temporal** | Continuo / tiempo real | Corto plazo, urgente | Mediano plazo, investigativo | Planificado (salvo emergencia) |
| **Salida típica** | Registro; incidente; evidencia de problema; requerimiento de cambio | Servicio restaurado (solución temporal o permanente) + entrada en la KB + CMDB actualizada | Error conocido + workaround + **RFC** | Servicio modificado + CMDB actualizada + **PIR** |
| **Órgano / rol** | Herramientas de monitorización y agentes | Centro de Servicios (SPOC), 1ª y 2ª línea | Especialistas / 2ª línea abocada a Gestión de Problemas | Gestor de Cambios + CAB (o ECAB en emergencias) |
| **Interfaz principal** | → Incidentes, Problemas, Control de Cambios | → Problemas (si se repite), KB, CMDB | → Control de Cambios (vía RFC), ejecuta la PIR | → Configuración, Versiones, Problemas |

Cadena típica de encadenamiento según el PPT: **evento reiterado → evidencia un problema → el problema se analiza y emite una RFC → Control de Cambios implementa → Gestión de Problemas hace la PIR → se actualiza la CMDB**. Un incidente se resuelve por su cuenta (break-fix) sin necesariamente cerrar el problema de fondo.

###### Observaciones sobre el material

- La conversión del PPT rompe las láminas con diagramas de flujo: las etapas y sus descripciones vienen intercaladas en columnas desordenadas. Se reconstruyó el orden de cada flujo a partir de las barras de proceso que sí quedaron legibles (las filas tipo `| Registro | Clasificación | ... | Cierre |`).
- Las tres láminas de **estructura física del Centro de Servicios** (centralizada, distribuida, virtual) son solo imágenes: no hay texto que describa ninguna de las tres.
- La lámina de **Activos del Servicio** perdió los rótulos "recursos" y "capacidades"; quedaron solo las definiciones.
- Falta en el material: matriz numérica impacto/urgencia, técnicas de RCA, lista de atributos de un CI, taxonomía de relaciones entre CI, y la lámina que unificaría los tres tipos de cambio (estándar/normal/emergencia). Todo eso está marcado como inferencia arriba.


---


##### Planillas y controles ISO 27002 (formato de entrega)

Sección de referencia operativa: define **cómo se entrega** el TP Integrador (formato exacto de cada planilla) y provee el catálogo completo de controles ISO 27002:2022 del que hay que elegir. Fuentes: `Estructura de la Tabla de Activos.pdf`, `Planillas de Riesgo.docx`, `ISO 27002 (2022) Controles.xlsx` y su versión imprimible.

###### A. Tabla de inventario de activos

**A.1. Estructura exacta de la planilla de entrega** (`Planillas de Riesgo.docx`, hoja "INVENTARIO DE ACTIVOS"). Once columnas, en este orden:

| # | Columna | Qué va |
|---|---|---|
| 1 | **ID** | Identificador único del activo. En la plantilla viene pre-numerado 1..9 (correlativo simple). |
| 2 | **Activo** | Nombre del activo. |
| 3 | **Tipo** | Tipo/categoría del activo. La planilla no define la tipología permitida. |
| 4 | **Contenedor** | Contenedor o soporte: dónde se almacena, procesa y distribuye el activo. Sirve para separar el activo de información de su soporte. |
| 5 | **Relacionados** | Activos relacionados = las dependencias (activos cuya materialización de una amenaza impacta la seguridad de este activo). |
| 6 | **Propietario** | Responsable de la viabilidad y supervivencia del activo. |
| 7 | **Custodio** | Quien tiene el activo bajo guarda operativa. |
| 8 | **C** | Valor de criticidad en la dimensión Confidencialidad. |
| 9 | **I** | Valor de criticidad en la dimensión Integridad. |
| 10 | **D** | Valor de criticidad en la dimensión Disponibilidad. |
| 11 | **Crit.** | Criticidad resultante del activo. |

Escala para C, I y D: **1–5 o 1–3** (definida en las REFERENCIAS del docx, apartado "Activos involucrados en el riesgo y dimensiones para la valoración de su criticidad"). Hay que elegir una y usarla consistentemente. El material **no define cómo se agrega C, I y D en `Crit.`** — no da fórmula ni criterio (máximo, promedio, suma). Hay que fijar el criterio y declararlo en el TP (inferencia).

**A.2. Atributos de identificación de activos según la teoría** (`Estructura de la Tabla de Activos.pdf`, etapa "1 - Recopilar Datos" del proceso de Gestión de Riesgos). Este es el listado conceptual completo de atributos del inventario:

| Atributo | Definición textual del material |
|---|---|
| **Identificador** | (sin definición ampliada) |
| **Nombre + Descripción** | (sin definición ampliada) |
| **Propietario** | "El que tiene la responsabilidad de viabilidad y supervivencia del activo" |
| **Contenedores o Soportes del Activo de Información** | "Para diferenciar el activo de la forma en que se almacena, procesa y distribuye" |
| **Custodio** | "Responsable de la viabilidad y la capacidad de supervivencia del activo" |
| **Origen** | "Identifica quién es el que tiene la potestad de generar el Activo" |
| **Acceso al activo** | Clasificación en 4 niveles (tabla siguiente) |
| **Dependencias** | "Activos a partir de los cuales la materialización de una amenaza tenga como consecuencia efectos en la seguridad del activo" |

**A.3. Escala de Acceso al activo** (completa, 4 niveles):

| Nivel | Alcance |
|---|---|
| **Público** | Sin restricción. |
| **Compartido** | Grupos o personas no pertenecientes a la organización. |
| **Reservado** | Sólo empleados de la organización. |
| **Confidencial** | Lista específica de personas. |

**A.4. Discrepancias entre la teoría y la planilla de entrega** (relevante para no perder puntos):

- El PDF da definiciones **idénticas** para *Propietario* y *Custodio* ("responsabilidad de viabilidad y supervivencia del activo"). Es un error de la filmina: no permite distinguirlos. La lectura estándar es Propietario = responsable de la decisión y del riesgo; Custodio = responsable de la guarda y operación diaria (inferencia).
- Los atributos **Origen** y **Acceso al activo** están en la teoría pero **no tienen columna** en la planilla de entrega. Si se quieren registrar, hay que agregar columnas o documentarlos aparte.
- Inversamente, la planilla exige **Tipo**, **C/I/D** y **Crit.**, que no figuran en la lista de atributos del PDF.
- El PDF no aparece degradado por la conversión; el contenido está completo salvo el pie de filmina ("mar.-26 UTN Rosario – Administración de Sist. de Información / 25"), que es ruido.

###### B. Planilla 1 — IDENTIFICACIÓN DE RIESGOS

Campos exactos, en orden:

| Campo | Contenido exigido |
|---|---|
| **ID** | Identificador del riesgo. |
| **Identificador** | Dos subcampos: **Legajo** y **Apellido y Nombres** — quién identificó el riesgo. |
| **Especificación** | El evento particular que, una vez materializado, afecta al activo. Debe redactarse con una de las formas canónicas (ver B.1). |
| **Clasificación** | Según la taxonomía o lista de chequeo elegida (ver B.2). |
| **Descripción ampliada del Contexto del Riesgo** | Cuestiones que mejoren la descripción del riesgo en función del contexto evaluado. |
| **VALORACIÓN DEL RIESGO → ACTIVOS involucrados y dimensión de valor de su criticidad** | Qué activos entran y con qué criticidad en C, I y D. Escala 1-5 o 1-3. |
| **Descripción de Factores analizados para evaluar IMPACTO** | Descripción de los factores que influyen en el cálculo, **usando FAIR**. |
| **Descripción de Factores analizados para evaluar PROBABILIDAD** | Ídem, con FAIR. |
| **IMPACTO =** | Valor numérico, escala **1–5**. |
| **PROBABILIDAD =** | Valor numérico, escala **1–5**. |
| **SEVERIDAD =** | Valor resultante. |

El material **no da la fórmula de SEVERIDAD**: sólo deja el campo. La convención habitual es Severidad = Impacto × Probabilidad, con rango 1–25 sobre escalas 1–5 (inferencia; hay que declarar el criterio usado).

**B.1. Formas canónicas de redacción de la Especificación** (transcripción completa de las REFERENCIAS del docx). Los términos entre `<>` son los que hay que instanciar:

*Relacionados con Activos de información, soportes de información, hardware o software:*
- `<Activo>` presenta `<Degradación en la dimensión [Integridad – Disponibilidad – Confidencialidad]>` causada por `<Amenaza>`
- `<Acción de amenaza>` con `<Motivo>` sobre un `<Activo>` por parte de `<Agente de Amenaza>` genera `<Degradación en la dimensión [Integridad – Disponibilidad – Confidencialidad]>`
- `<Activo>` no cuenta con `<Característica>`

*Relacionados con Activos de Procesos:*
- `<Proceso>` no se ejecuta
- `<Proceso>` demora más tiempo de lo esperado
- `<Proceso>` cuesta más de lo esperado
- `<Proceso>` no cuenta con `<Rol>`
- `<Proceso>` no cuenta con `<Actividad>`

*Relacionados con Recursos Humanos:*
- `<Rol>` no está definido
- `<Rol>` no cuenta con `<Competencia>`

**B.2. Formato del campo Clasificación según la taxonomía elegida:**

| Taxonomía / Lista de chequeo | Formato de la clasificación |
|---|---|
| Estructura de desglose del Riesgo del **PMI** (RBS) | `Categoría / Sub-categoría` |
| Taxonomía de riesgos operacionales del **SEI** | `Clase de la Fuente / Subclase / Elemento` |

###### C. Planilla 2 — TRATAMIENTO DE RIESGOS

| Campo | Contenido exigido |
|---|---|
| **ID** | Mismo ID del riesgo identificado. |
| **Identificador** | **Legajo** y **Apellido y Nombres**. |
| **Especificación** | Se repite la especificación del riesgo (el riesgo no cambia de especificación entre planillas). |
| **ESTRATEGIAS → EVITAR** | Características de la estrategia, ventajas y desventajas. **Numeradas**, para poder referenciar los controles necesarios. |
| **ESTRATEGIAS → TRANSFERIR** | Ídem. |
| **ESTRATEGIAS → MITIGAR** | Ídem. |
| **CONTROLES** | Controles de la **ISO 27002:2022** requeridos para garantizar cada estrategia de tratamiento. |
| **RIESGO RESIDUAL** | No se re-especifica el riesgo: se referencia a las estrategias anteriores y se describe su **efecto sobre la probabilidad o el impacto** del riesgo inherente calculado en la planilla de Identificación. |

Punto fino: la planilla lista **sólo tres estrategias — Evitar, Transferir, Mitigar**. **No incluye "Aceptar"**. Si un riesgo se acepta, el material no provee un casillero para eso; lo consistente es reflejarlo vía el riesgo residual (inferencia).

Punto fino 2: las estrategias deben ir **numeradas** porque los controles se enganchan a un número de estrategia. No es decorativo; es la trazabilidad estrategia → control.

###### D. Planilla 3 — PLANES DE CONTINGENCIA, RECUPERACIÓN Y CONTINUIDAD DE NEGOCIO

| Campo | Contenido exigido |
|---|---|
| **ID** | Mismo ID del riesgo. |
| **Identificador** | **Legajo** y **Apellido y Nombres**. |
| **Especificación** | Se repite la especificación del riesgo. |
| **Disparadores** | Señales de advertencia o alarmas que permitan detectar la **proximidad** del riesgo o su **materialización**. |
| **Contingencia** | Acciones específicas del plan de contingencia. |
| **Recuperación** | Acciones específicas del plan de recuperación. |
| **Continuidad de Negocio** | Acciones específicas del plan de continuidad. |
| **Controles de Garantía de los Planes** | Controles de la **ISO 27002:2022** requeridos para garantizar los tres planes. |

Los tres planes se especifican por separado, cada uno con sus acciones concretas — el material dice explícitamente "acciones específicas para **cada uno** de los planes". No se resuelve con un párrafo único.

###### E. Controles ISO 27002:2022 — catálogo completo (93 controles, 4 temas)

Estructura de la norma en la versión 2022: 4 temas (cláusulas 5 a 8) que reemplazan los 14 dominios de la versión 2013. Distribución: **5 Organizacionales (37) + 6 Personas (8) + 7 Físicos (14) + 8 Tecnológicos (34) = 93**.

**Leyenda de columnas** (atributos de la ISO 27002:2022, transcritos del xlsx de la cátedra):

- **Tipo**: `P` Preventivo · `C` Correctivo · `D` Detectivo (un control puede tener más de uno).
- **Prop.** (propiedad de seguridad de la información): `C` Confidencialidad · `I` Integridad · `D` Disponibilidad.
- **Ciber.** (concepto de ciberseguridad, marco NIST): `Id` Identificar · `Pr` Proteger · `De` Detectar · `Rc` Recuperar · `Rs` Responder.
- **Capacidad operacional**: agrupamiento funcional del control.
- **Dominio de seguridad**: `G&E` Gobernanza y Ecosistema · `Prot` Protección · `Def` Defensa · `Res` Resiliencia · `PI` Protección de información.

Nota de numeración: la cátedra usa formato de dos dígitos (`5.01`, `5.02`…). La norma oficial numera `5.1`, `5.2`… Es la misma numeración.

**E.1. Tema 5 — Controles Organizacionales (37)**

| N° | Nombre del control | Tipo | Prop. | Ciber. | Capacidad operacional | Dominio |
|---|---|---|---|---|---|---|
| 5.01 | Políticas para la seguridad de la información | P | C I D | Id | Gobernanza | G&E, Res |
| 5.02 | Roles y responsabilidades en seguridad de la información | P | C I D | Id | Gobernanza | G&E, Res, Prot |
| 5.03 | Segregación de funciones | P | C I D | Pr | Gobernanza | G&E |
| 5.04 | Responsabilidades de gestión | P | C I D | Id | Gobernanza | G&E |
| 5.05 | Contacto con autoridades | P, C | C I D | Pr, Rc, Rs | Gobernanza | Res, Def |
| 5.06 | Contacto con grupos de interés especial | P, C | C I D | Pr, Rc, Rs | Gobernanza | Def |
| 5.07 | Inteligencia de amenazas | P, D | C I D | Id, De | Gestión de amenazas y vulnerabilidades | Res, Def |
| 5.08 | Seguridad de la información en la gestión de proyectos | P | C I D | Id, Pr | Gobernanza | G&E, Prot |
| 5.09 | Inventario de información y otros activos asociados | P | C I D | Id | Gestión de activos | G&E, Prot |
| 5.10 | Uso aceptable de la información y otros activos asociados | P | C I D | Pr | Gestión de activos | G&E |
| 5.11 | Devolución de activos | P | C I D | Pr | Gestión de activos | Prot |
| 5.12 | Clasificación de la información | P | C I D | Id | Protección de la información | Prot, Def |
| 5.13 | Etiquetado de la información | P | C I D | Pr | Protección de la información | Def |
| 5.14 | Transferencia de la información | P | C I D | Pr | Gestión de activos | Prot, PI |
| 5.15 | Control de acceso | P | C I D | Pr | Gestión de identidades y accesos | Prot |
| 5.16 | Gestión de identidad | P | C I D | Pr | Gestión de identidades y accesos | Prot |
| 5.17 | Información de autenticación | P | C I D | Pr | Gestión de identidades y accesos | Prot |
| 5.18 | Derechos de acceso | P | C I D | Pr | Gestión de identidades y accesos | Prot |
| 5.19 | Seguridad de la información en las relaciones con proveedores | P | C I D | Id | Seguridad de las relaciones con proveedores | G&E, Prot |
| 5.20 | Directrices de seguridad de la información en los acuerdos con proveedores | P | C I D | Id | Seguridad de las relaciones con proveedores | G&E, Prot |
| 5.21 | Gestión de la seguridad de la información en la cadena de suministro de TIC | P | C I D | Id, Pr | Seguridad de las relaciones con proveedores | G&E, Prot |
| 5.22 | Seguimiento, revisión y gestión de cambios de servicios de proveedores | P | C I D | Id | Seguridad de las relaciones con proveedores | G&E, Prot, Def |
| 5.23 | Seguridad de la información para el uso de servicios en la nube | P | C I D | Pr | Seguridad de las relaciones con proveedores | G&E, Prot |
| 5.24 | Planificación y preparación de la gestión de incidentes de seguridad de la información | C | C I D | Rc, Rs | Gestión de eventos en seguridad de la información | Def |
| 5.25 | Evaluación y decisión sobre los eventos de seguridad de información | D | C I D | De, Rs | Gestión de eventos en seguridad de la información | Def |
| 5.26 | Respuesta a incidentes de seguridad de la información | C | C I D | Rc, Rs | Gestión de eventos en seguridad de la información | Def |
| 5.27 | Aprendizaje de los incidentes de seguridad de la información | P | C I D | Id, Pr | Gestión de eventos en seguridad de la información | Def |
| 5.28 | Recopilación de evidencias | C, D | C I D | De, Rs | Gestión de eventos en seguridad de la información | Def |
| 5.29 | Seguridad de la información durante interrupciones | P | C I D | Pr | Continuidad | Res, Prot |
| 5.30 | Preparación de las TIC para la continuidad del negocio | C | D | Pr, Rs | Continuidad | Res |
| 5.31 | Identificación de requerimientos legales, estatutarios, regulatorios y contractuales | P | C I D | Id | Legal y cumplimiento | G&E, Prot |
| 5.32 | Derechos de Propiedad Intelectual | P | C I D | Id | Legal y cumplimiento | G&E |
| 5.33 | Protección de registros | P | C I D | Id, Pr | Legal y cumplimiento; Gestión de activos; Protección de información | Def |
| 5.34 | Privacidad y protección de PII | P | C I D | Id, Pr | Legal y cumplimiento; Protección de la información | Prot |
| 5.35 | Revisión independiente de la seguridad de la información | P, C | C I D | Id | Garantía de la seguridad de la información | G&E |
| 5.36 | Cumplimiento con políticas y estándares de seguridad de la información | P | C I D | Pr | Legal y cumplimiento | G&E |
| 5.37 | Procedimientos operativos documentados | P | C I D | Pr | Continuidad; Gestión de activos | G&E, Prot, Def |

**E.2. Tema 6 — Controles de Personas (8)**

| N° | Nombre del control | Tipo | Prop. | Ciber. | Capacidad operacional | Dominio |
|---|---|---|---|---|---|---|
| 6.01 | Investigación de antecedentes | P | C I D | Pr | Seguridad de recursos humanos | G&E |
| 6.02 | Términos y condiciones del empleo | P | C I D | Pr | Seguridad de recursos humanos | G&E |
| 6.03 | Concientización, educación y entrenamiento en seguridad de la información | P | C I D | Pr, Rs | Seguridad de recursos humanos | G&E |
| 6.04 | Proceso disciplinario | P, C | C I D | Pr | Seguridad de recursos humanos | G&E |
| 6.05 | Responsabilidades después de la finalización o cambio de empleo | P | C I D | Pr | Seguridad de recursos humanos; Gestión de activos | G&E |
| 6.06 | Acuerdos de confidencialidad o no revelación | P | C | Pr | Seguridad de RRHH; Protección de la información; Seguridad de las relaciones con proveedores | G&E |
| 6.07 | Teletrabajo | P | C I D | Pr | Gestión de activos; Seguridad del sistema y de la red; Seguridad física | G&E, Prot |
| 6.08 | Reporte de eventos de seguridad de la información | D | C I D | De | Gestión de eventos en seguridad de la información | Def |

**E.3. Tema 7 — Controles Físicos (14)**

| N° | Nombre del control | Tipo | Prop. | Ciber. | Capacidad operacional | Dominio |
|---|---|---|---|---|---|---|
| 7.01 | Perímetro de seguridad física | P | C I D | Pr | Seguridad física | Prot |
| 7.02 | Controles de entrada física | P | C I D | Pr | Seguridad física | Prot |
| 7.03 | Seguridad de oficinas, despachos y recursos | P | C I D | Pr | Seguridad física; Gestión de activos | Prot |
| 7.04 | Supervisión de la seguridad física | D | C I D | De | Seguridad física | Prot, Def |
| 7.05 | Protección contra las amenazas físicas y ambientales | P | C I D | Pr | Seguridad física | Prot |
| 7.06 | Trabajar en áreas seguras | P | C I D | Pr | Seguridad física | Prot |
| 7.07 | Escritorio limpio y pantalla limpia | P | C | Pr | Seguridad física | Prot |
| 7.08 | Ubicación y protección del equipamiento | P | C I D | Pr | Seguridad física; Gestión de activos | Prot |
| 7.09 | Seguridad de los activos fuera de las instalaciones | P | C I D | Pr | Seguridad física; Gestión de activos | Prot |
| 7.10 | Medios de almacenamiento | P | C I D | Pr | Seguridad física; Gestión de activos | Prot |
| 7.11 | Utilidades de apoyo | P, D | D | Pr, De | Seguridad física | Prot |
| 7.12 | Seguridad del cableado | P | C D | Pr | Seguridad física | Prot |
| 7.13 | Mantención del equipamiento | P | C I D | Pr | Seguridad física; Gestión de activos | Res, Prot |
| 7.14 | Eliminación segura o reutilización de equipos | P | C | Pr | Seguridad física; Gestión de activos | Prot |

**E.4. Tema 8 — Controles Tecnológicos (34)**

| N° | Nombre del control | Tipo | Prop. | Ciber. | Capacidad operacional | Dominio |
|---|---|---|---|---|---|---|
| 8.01 | Dispositivos de punto final del usuario | P | C I D | Pr | Gestión de activos; Protección de la información | Prot |
| 8.02 | Derechos de acceso privilegiado | P | C I D | Pr | Gestión de identidades y accesos | Prot |
| 8.03 | Restricción del acceso a la información | P | C I D | Pr | Gestión de identidades y accesos | Prot |
| 8.04 | Acceso al código fuente | P | C I D | Pr | Gestión de identidades y accesos | Prot |
| 8.05 | Autenticación segura | P | C I D | Pr | Gestión de identidades y accesos | Prot |
| 8.06 | Gestión de la capacidad | P, D | D | Id, Pr, De | Continuidad | G&E, Prot |
| 8.07 | Protección contra malware | P, C, D | C I D | Pr, De | Seguridad del sistema y de la red | Prot, Def |
| 8.08 | Gestión de vulnerabilidades técnicas | P | C I D | Pr | Gestión de amenazas y vulnerabilidades | G&E, Prot, Def |
| 8.09 | Gestión de la configuración | P | I D | Pr | Configuración segura | Prot |
| 8.10 | Eliminación de la información | P | C | Pr | Protección de la información | Prot |
| 8.11 | Enmascaramiento de datos | P | C | Pr | Protección de la información | Prot |
| 8.12 | Prevención de la fuga de datos | P, D | C | Pr, De | Protección de la información | Prot, Def |
| 8.13 | Copias de seguridad de la información | C | I D | Rc | Continuidad | Prot |
| 8.14 | Redundancia de las instalaciones de procesamiento de información | P | D | Pr | Continuidad; Gestión de activos | Res, Prot |
| 8.15 | Gestión de eventos (Log) | D | C I D | De | Gestión de eventos en seguridad de la información | Prot, Def |
| 8.16 | Actividades de seguimiento | C, D | C I D | De, Rs | Gestión de eventos en seguridad de la información | Def |
| 8.17 | Sincronización del reloj | D | I | Pr, De | Gestión de eventos en seguridad de la información | Prot, Def |
| 8.18 | Uso de programas de utilidad privilegiados | P | C I D | Pr | Seguridad del sistema y de la red; Configuración segura | Prot |
| 8.19 | Instalación de software en sistemas operacionales | P | C I D | Pr | Configuración segura | Prot |
| 8.20 | Controles de red | P, D | C I D | Pr, De | Seguridad del sistema y de la red | Prot |
| 8.21 | Seguridad de los servicios de red | P | C I D | Pr | Seguridad del sistema y de la red | Prot |
| 8.22 | Segregación en redes | P | C I D | Pr | Seguridad del sistema y de la red | Prot |
| 8.23 | Filtrado Web | P | C I D | Pr | Seguridad del sistema y de la red | Prot |
| 8.24 | Uso de Criptografía | P | C I D | Pr | Configuración segura | Prot |
| 8.25 | Ciclo de vida de desarrollo seguro | P | C I D | Pr | Seguridad del sistema y de la red; Seguridad de las aplicaciones | Prot |
| 8.26 | Requisitos de seguridad en aplicaciones | P | C I D | Pr | Seguridad del sistema y de la red; Seguridad de las aplicaciones | Prot, Def |
| 8.27 | Arquitectura de sistema seguro y principios de ingeniería | P | C I D | Pr | Seguridad del sistema y de la red; Seguridad de las aplicaciones | Prot |
| 8.28 | Codificación Segura | P | C I D | Pr | Seguridad del sistema y de la red; Seguridad de las aplicaciones | Prot |
| 8.29 | Pruebas de seguridad en el desarrollo y aceptación | P | C I D | De | Seguridad del sistema y de la red; Seguridad de las aplicaciones; Seguridad de información | Prot |
| 8.30 | Desarrollo subcontratado | P, D | C I D | Id, Pr, De | Seguridad del sistema y de la red; Seguridad de las aplicaciones; Seguridad de las relaciones con proveedores | G&E, Prot |
| 8.31 | Separación de los entornos de desarrollo, prueba y producción | P | C I D | Pr | Seguridad del sistema y de la red; Seguridad de las aplicaciones | Prot |
| 8.32 | Gestión del cambio | P | C I D | Pr | Seguridad del sistema y de la red; Seguridad de las aplicaciones | Prot |
| 8.33 | Información de prueba | P | C I | Pr | Protección de la información | Prot |
| 8.34 | Protección de sistemas de información durante pruebas de auditoría | P | I D | Pr | Seguridad del sistema y de la red; Protección de la información | G&E, Prot |

**E.5. Notas sobre la fuente**

- Los nombres de control se tomaron del `.xlsx`, que está completo y estructurado. El PDF imprimible trae el mismo listado pero con el texto desarmado por la conversión (números de control partidos en dos líneas, filas de tabla mezcladas con texto suelto): sirve de verificación cruzada, no como fuente primaria. Ambos coinciden en los 93 nombres.
- Los atributos "Tipo de control", "Propiedad de seguridad", "Concepto de ciberseguridad", "Capacidad operacional" y "Dominio de seguridad" vienen del `.xlsx` en formato de columnas-bandera (una columna por valor posible, con celdas vacías). Acá están condensados a un solo campo por atributo — el contenido es el mismo, sin pérdida.
- El `.xlsx` trae una hoja adicional ("Hoja17") con la leyenda de hashtags de la norma (`#Preventive/#Preventivo`, `#Confidentiality/#Confidencialidad`, etc.). Está mal convertida: los valores quedaron desalineados respecto de sus etiquetas y algunas traducciones son directamente erróneas (p. ej. `#Legal_and_compliance #Asset_management #Information_protection` traducido como "Gestión_de_activos_legales_y_de_cumplimiento"). **No usar esa hoja**; los hashtags oficiales son simplemente los valores de atributo listados en la leyenda de E, con prefijo `#`.


---


##### Ejemplo de cátedra — Gestión de Riesgos del Proceso de Exámenes UTN (Etapa 2)

Modelo resuelto por la cátedra sobre el Proceso de Exámenes Normales de UTN-FRRo. Fija el nivel de detalle esperado en el TP Integrador. Consta de dos piezas: la planilla `ASI-2-InventarioActivos_ProcesoExamenes.xlsx` (inventario + hoja de riesgos inherentes) y el documento `ASI_2_GestiónDeRiesgos-ProcesoExamenes.docx` (metodología + fichas de Identificación, Tratamiento y Planes). El propio material aclara dos cosas: el Proceso de Gestión de Riesgos de UTN no está documentado o no es accesible, por lo que **se usa el proceso y la documentación propuestos por la cátedra**; y **el ejemplo está deliberadamente incompleto** para completarse en clase.

###### Marco de partida (qué se asume dado antes de empezar)

La UTN tiene tres documentos de seguridad: Políticas de Seguridad de la Información, Plan de Desarrollo e Implementación, y Procedimientos de Implementación. El Comité de Seguridad de la Información hace cumplir las políticas en las Regionales. Alcance de las políticas: todos los procesos de gestión, operativos y de soporte de las funciones fundamentales definidas en el Estatuto Universitario (Docencia, Investigación, Extensión y Vinculación).

Del documento *Procedimientos de Implementación* se toman cuatro normas metodológicas:

| Norma | Contenido |
|---|---|
| Responsabilidades | Roles que participan en los procedimientos del SGSI |
| Identificación de riesgos | Basada en Inventario de Activos críticos, **revisable cada seis meses** |
| Clasificación | Dimensiones confidencialidad, integridad y disponibilidad, con **criterios cualitativos** |
| Declaración de Aplicabilidad | Dominios, Objetivos de Control y Controles según normas de la Administración Pública (**ONTI**) |

Patrón a copiar: **antes de valorar nada, se declara de dónde sale la escala y qué se modificó respecto del documento original.** El ejemplo hace dos declaraciones explícitas de este tipo:
- El documento UTN clasifica sólo Información: "Se ha modificado para que cubra todos los activos vinculados a la gestión de la seguridad".
- El documento habla de criticidad pero no dice cómo calcularla: la cátedra define la fórmula (ver abajo) y lo dice.

###### Cómo está armado el inventario de activos

Siete hojas / categorías. El documento enumera seis (Información, Software, Hardware, Equipamiento, Instalaciones, Servicios); la planilla agrega **Procesos** al inicio y **Activos de Soporte** (contenedores), y no lista una hoja separada de Equipamiento distinta a la del documento — la planilla efectivamente tiene: Procesos, ActivosInformación, Software, Hardware, Activos de Soporte, Equipamiento, Instalaciones, Servicios, RiesgosInherentes.

Conteo de activos cargados en el ejemplo:

| Hoja | Cant. | IDs (prefijo) | Observación |
|---|---|---|---|
| Procesos | 5 | `PO_EXA`, `PG_PLC`, `PG_CAL`, `PO_CAN`, `PO_REXA` | Sólo `PO_EXA` (Exámenes) está valorado; los otros 4 están en el inventario sólo como contexto/dependencia, con celdas vacías |
| ActivosInformación | 12 | `I_EXA001`–`I_EXA007`, `I_TI001`, `I_CAL001`, `I_CAN001`, `I_PG001`, `I_PC002` | Prefijo por proceso de origen: EXA=exámenes, TI=tecnología, CAL=calendario, CAN=cursado anual, PG/PC=plan de carrera |
| Software | 2 | `SW_REDES001` (SYSACAD y MS SQL Server) | **ID duplicado en el ejemplo — error de la planilla** |
| Hardware | 4 | `HW_REDES001..003`, `HW_LYA001` | Sin valorar C/I/D (criticidad 0) |
| Activos de Soporte | 2 | `SI_REDES001` (Base de Datos SYSACAD), `SI_EXA001` (Cajas con sobres de Exámenes) | |
| Equipamiento | 1 | `EQ_DEP_001` (Mobiliario para resguardo de documentación crítica) | |
| Instalaciones | 3 | `INS_001`, `INS_002` (×2, **ID duplicado**) | Sin valorar |
| Servicios | 2 | `SER_001` (Internet), `SER_002` (Energía Eléctrica - EPE) | Sin valorar |

**Total ≈ 31 filas de activo**, de las cuales sólo ~14 están efectivamente valoradas. El patrón es: se inventaría todo lo que toca el proceso, pero **se valora sólo lo que es candidato a riesgo**.

Columnas del inventario (varían levemente por hoja):

`ID | Activo | Descripción | Dueño | Activos de Soporte (Contenedores) | Custodios | Acceso | Origen | Confidencialidad | Integridad | Disponibilidad | Criticidad | (*) | Dependencias con otros activos (inmediatas)`

- La hoja **Procesos** agrega **Autenticidad** y **Trazabilidad** como dimensiones adicionales (`PO_EXA`: C=0, I=5, D=5, Aut=5, Traz=5, Criticidad=5). Ojo: acá la criticidad **no** es la suma — es 5, no 20. La escala del proceso parece ser otra que la de los activos (inferencia: la fila de proceso usa una valoración distinta, o quedó mal cargada).
- Un mismo activo de información puede tener **varias filas de contenedor**: `I_EXA004` (Acta de Examen) se despliega en Formulario individual en Papel, Carpeta, Base de Datos del SYSACAD (\*), Bolsa para traslado a Rectorado (\*). Cada contenedor tiene su propio Custodio y su propio nivel de Acceso.
- El marcador `(*)` en la columna de contenedores significa **"este contenedor debe analizarse como Activo de Soporte en su propia hoja"**. Es el mecanismo de encadenado entre hojas.
- La columna `Dependencias con otros activos (inmediatas)` se escribe tipada: `Información: ... Software: ... Hardware: ... Instalaciones: ... Servicios: ... Procesos: ...`. Ej. de `I_EXA004`/BD SYSACAD: `Información: Credenciales de Acceso  Software: SYSACAD`.
- La columna `Origen` indica quién genera el activo (Alumno, Personal Administrativo LyA, CD, Jefe de Cátedra…), o de qué proceso viene (`Procesos: Compras y Patrimonio por la asignación del activo al Área de Redes`).

###### Escalas de valoración C / I / D (transcripción completa)

Confidencialidad:

| Valor | Criterio |
|---|---|
| 0 | Acceso Público |
| 1 | Acceso Reservado para uso interno |
| 2 | Acceso Reservado Confidencial |
| 3 | Acceso Reservado Secreto/Privado/Sensible (enmarcado en cuestiones estratégicas o legales) |

Integridad:

| Valor | Criterio |
|---|---|
| 0 | Activo cuya modificación no autorizada puede repararse fácilmente, o no afecta la operatoria de la Universidad |
| 1 | Activo cuya modificación no autorizada puede repararse, aunque podría ocasionar pérdidas leves para la Universidad, el Sector Público Nacional o terceros |
| 2 | Activo cuya modificación no autorizada es de difícil reparación y podría ocasionar pérdidas significativas para la Universidad, el Sector Público Nacional o terceros |
| 3 | Activo cuya modificación no autorizada podría no repararse y podría ocasionar pérdidas graves a la Universidad, al Sector Público Nacional o a terceros |

Disponibilidad:

| Valor | Criterio |
|---|---|
| 0 | Activo cuya inaccesibilidad no afecta la operatoria del organismo |
| 1 | Activo cuya inaccesibilidad en un plazo no menor a una semana podría ocasionar pérdidas significativas para el organismo |
| 2 | Activo cuya inaccesibilidad permanente en un plazo no menor a un día podría ocasionar pérdidas significativas al organismo |
| 3 | Activo cuya inaccesibilidad permanente durante un plazo no menor a una hora podría ocasionar pérdidas significativas al organismo |

Nota sobre la numeración: el documento presenta las tres escalas como listas numeradas 1–4, pero la planilla usa valores **0–3** (hay activos con C=0, y la criticidad máxima observada es 9 = 3+3+3). Se transcribe acá 0–3, que es lo consistente con los datos. (inferencia: el renumerado 1–4 del .docx es artefacto de la lista de Word)

**Criticidad = C + I + D.** El documento lo dice explícitamente: el criterio de cálculo no está en el documento UTN, así que la cátedra adopta la suma "debido a los valores establecidos (que no contemplan un rango amplio)".

**Regla de corte para pasar a identificación de riesgos:** se analizan los activos cuya **criticidad ≥ 6** *o* que hayan sido **valuados con 3 en alguna dimensión**. Los activos que pasan el corte están marcados con `(*)` en la columna sin nombre a la derecha de Criticidad.

Activos que superan el corte en el ejemplo:

| ID | Activo | C | I | D | Criticidad |
|---|---|---|---|---|---|
| `I_EXA003` | Formulario de Inscripción a Exámenes | 2 | 1 | 3 | 6 |
| `I_EXA004` | Acta de Examen | 2 | 3 | 3 | 8 |
| `I_EXA006` | Planilla entrega de Actas | 1 | 2 | 3 | 6 |
| `I_EXA007` | Exámenes Físicos | 2 | 3 | 2 | 7 |
| `I_TI001` | Credenciales de Acceso al SYSACAD | 3 | 3 | 3 | 9 |
| `I_PC002` | Registro de Correlatividades Plan de Carrera | 1 | 3 | 2 | 6 |
| `SW_REDES001` | SYSACAD | 2 | 3 | 3 | 8 |
| `SW_REDES001` | Microsoft SQL Server | 3 | 3 | 3 | 9 |
| `SI_REDES001` | Base de Datos SYSACAD | 3 | 3 | 3 | 9 |
| `SI_EXA001` | Cajas con sobres de Exámenes Depto. Carrera | 1 | 3 | 2 | 6 |
| `EQ_DEP_001` | Mobiliario para resguardo de Documentación crítica | 2 | 3 | 3 | 8 |

###### Comunidades de amenaza y vulnerabilidades (paso previo a redactar riesgos)

Antes de escribir un solo riesgo, el ejemplo caracteriza las **comunidades de amenaza**:

| Tipo | Comunidades |
|---|---|
| Internas | Personal que participa del Proceso (Docentes, No Docentes/Administrativos) con acceso físico o por red; Personal que accede físicamente a las áreas con documentación del proceso (maestranza, mantenimiento, técnico) |
| Externas | Alumnos; Proveedores o visitantes ocasionales que acceden a esas áreas; Hackers |

Características de esas comunidades (esto alimenta después los factores FAIR):

| Característica | Contenido en el ejemplo |
|---|---|
| Motivación | Ganancias económicas (patrocinio); Visibilidad del atacante (ataques a servidores para publicarlos en redes sociales). **Se descartan explícitamente las ideológicas**, por el tipo de organización y proceso |
| Intento primario | Conseguir acceso, dañar o destruir |
| Patrocinio | Connivencia de un alumno con alguna de las personas participantes del proceso |
| Capacidades | Varían según el vector de ataque (físico o por red). Los alumnos de Ing. en Sistemas tienen capacidad para atacar por red |
| Tolerancia al riesgo | Alumnos: expulsión de la Universidad. Personal interno: sumario administrativo. Otros: en caso de robo interviene la justicia federal |

Vulnerabilidades transversales identificadas: falta de controles en el acceso físico; falta de controles en el acceso lógico; falta de documentación en los procesos; confianza en el personal de la institución (participe o no del proceso); estado de los activos de hardware e instalaciones; dependencia del desarrollo del software SYSACAD.

Patrón: **descartar explícitamente lo que no aplica y justificar por qué** (el caso de la motivación ideológica). Es tan valorable como listar lo que sí aplica.

###### Cómo se descompone una amenaza (hoja RiesgosInherentes)

Cada fila de riesgo inherente descompone la amenaza en cuatro columnas antes de redactar la frase:

| Columna | Valores usados en el ejemplo |
|---|---|
| **Acceso** (vector) | `Por Red` / `Físico` |
| **Actor / Otras Amenazas** | Personal con acceso al registro de Actas; Custodio de las Actas de Exámenes; Keyloggers; Hacker; Desastres Naturales: inundación causada por tormentas |
| **Motivo** | `Deliberado` / `Accidental` |
| **Resultado** | Efecto + **dimensión degradada explícita**. Ej.: "Modificar el registro de nota final del examen. Actúa sobre la integridad de la activo" |

Y luego: `Vulnerabilidades que explota | Observaciones para el cálculo de la probabilidad | Observaciones para el cálculo del Impacto | Probabilidad | Impacto | Severidad | ID. Riesgo | Especificación del Riesgo | Clasificación (Clase / Subclase / Elemento)`.

###### Estructura de la frase de "Especificación" del riesgo

La fórmula que se repite en los 6 riesgos:

**[Acción sobre el activo] + [del activo concreto, con su contenedor] + [por parte de / a causa de: agente] + [causa o vulnerabilidad explotada / condición habilitante]**

Es una frase única, sin viñetas, en sustantivo de acción (Modificación, Pérdida, Captura, Obtención, Destrucción), no en verbo conjugado. Transcripciones textuales:

> **Riesgo 1** — "Modificación deliberada del registro de la Nota de un Alumno en la base de datos del SYSACAD por parte de Personal con acceso a la opción de registro de Actas de Exámenes en connivencia con el alumno."

> **Riesgo 3** — "Pérdida accidental del Acta de Exámenes (en papel) por deficiencias en la organización atribuible al custodio de la misma en el momento de la pérdida."

> **Riesgo 6** — "Destrucción de las cajas con sobres de Exámenes Físicos existentes en el Departamento de Carrera a causa de inundaciones provocadas por tormentas."

Los otros tres, para completar el patrón:
- **2**: "Modificación accidental del registro de la Nota de un Alumno en la Base de Datos del SYSACAD por parte de Personal con acceso a la opción de registro de Actas de Exámenes"
- **4**: "Captura de usuarios y contraseñas de acceso al SYSACAD a partir de la instalación de keyloggers en las computadoras que se utilizan para el acceso"
- **5**: "Obtención de acceso a los activos de software a partir del escaneo de puertos por deficiencias en los parámetros de seguridad"

Observaciones sobre la redacción:
- El adverbio **deliberada / accidental** va incrustado en la frase: los riesgos 1 y 2 son el mismo activo y la misma acción y se diferencian sólo por el motivo. **Un par deliberado/accidental sobre el mismo activo es dos riesgos distintos, no uno.**
- La causa se introduce con conectores fijos: `por parte de` (agente humano), `a partir de` (mecanismo técnico), `a causa de` (evento externo), `por deficiencias en` (vulnerabilidad).
- Se nombra el **contenedor**, no sólo el activo lógico: "en la base de datos del SYSACAD", "(en papel)", "existentes en el Departamento de Carrera".
- Nunca se menciona el control ausente como si fuera el riesgo. El riesgo es el evento, no la falta de control.

###### Clasificación SEI (taxonomía de riesgos operacionales)

El documento declara: *"Los riesgos están clasificados según la Taxonomía de riesgos operacionales del SEI."* Se clasifica en tres niveles: **Clase / Subclase / Elemento**. Clasificaciones usadas en el ejemplo:

| ID | Clase | Subclase | Elemento |
|---|---|---|---|
| 1 | Acciones de las Personas | Deliberadas | Fraude |
| 2 | Acciones de las Personas | Involuntarias | Equivocación |
| 3 | Fallas de los Procesos Internos | Procesos de Control | Roles y Responsabilidades |
| 4 | Fallas de los Sistemas y Tecnologías | Software | Prácticas de Codificación |
| 5 | Fallas de los Sistemas y Tecnologías | Software | Parámetros de Seguridad |
| 6 | Eventos Externos | Desastres Naturales | Inundaciones |

Patrón: la clasificación **debe ser coherente con la columna Motivo y con el Actor**. Deliberado + persona interna → Acciones de las Personas / Deliberadas. Accidental + persona → Involuntarias / Equivocación. Cuando la causa raíz es organizativa (no la torpeza de un individuo puntual) se sube a Fallas de Procesos Internos / Roles y Responsabilidades — ver riesgo 3, donde el actor es "Custodio" pero la vulnerabilidad es "falta de organización de la cátedra / de Bedelía". Vulnerabilidad de software → Fallas de Sistemas y Tecnologías. Naturaleza → Eventos Externos.

###### Valoración: escala y factores FAIR

**Escala de 0 a 5 para impacto y probabilidad.** El ejemplo justifica la elección: se podría haber usado la criticidad del activo como impacto, pero *"se ha utilizado la taxonomía de factores propuesta por FAIR que mejora el análisis del impacto y la probabilidad"*.

**Severidad = Probabilidad × Impacto.** Verificable en la planilla (5 × 2 = 10) y en las fichas (4 × 1 = 4; 3 × 4 = 12).

Advertencia: **los valores de la planilla y los de las fichas del documento no coinciden.** Riesgo 1: planilla P=5, I=2, Sev=10; ficha P=4, I=1, Sev=4. Riesgo 6: planilla sin valores; ficha P=3, I=4, Sev=12. En un mismo riesgo (el 1) también cambia el texto del impacto: la planilla dice "Productividad: El impacto es sobre el Proceso de Emisión de Títulos" y la ficha dice "Productividad: No existe impacto directo sobre la productividad". Es incoherencia del material, no una regla — coherente con la nota "el ejemplo no está completo".

Después de valorar: *"se deben priorizar los riesgos (ordenar por severidad en forma decreciente)"* y sobre ese orden se seleccionan los riesgos a tratar.

Factores FAIR usados para **probabilidad** (siempre estos cuatro, en este orden):

| Factor | Qué se argumenta | Ejemplo textual (riesgo 1) |
|---|---|---|
| **Contacto** | Frecuencia/tipo de contacto del agente con el activo | "El acceso al sistema es periódico" (otros: "Intencional", "Aleatorio") |
| **Acción** | Se abre en tres subfactores fijos: **Beneficio**, **Nivel de Esfuerzo**, **Riesgo de Detección** | "Beneficio: Patrocinio por parte de un alumno. Nivel de Esfuerzo: Bajo o Inexistente. Riesgo de Detección: Bajo. Solo existen sanciones administrativas previstas en caso de ser probado el fraude" |
| **Capacidad de la amenaza** | Si el agente tiene recursos y habilidades | "Tiene recursos y habilidades suficientes para materializar la amenaza" |
| **Capacidad de Resistencia** | Controles existentes, trazabilidad, momento de detección | "No existen auditorías posteriores al registro de Actas de Exámenes. El momento de detección más avanzado es el proceso de Trámite de Título. No existe trazabilidad en los procesos de registro de datos del SYSACAD" |

Factores FAIR usados para **impacto**, agrupados en tres bloques:

| Bloque | Factores | Ejemplo textual |
|---|---|---|
| **Sobre el activo** | Productividad; Costo; Sensibilidad (con sub-etiquetas **Legal** y **Reputación**); Volumen | "Costo: El costo no tiene una evaluación directa" / "Legal: Se deberán establecer los procedimientos Legales para evaluar la sanción y emisión o no del Título" / "Volumen: La modificación de gran cantidad de registros de Actas de Exámenes puede ser catastrófica" |
| **Según la amenaza** | Origen del agente (interno / externo / fuera de control); Acción (qué dimensión degrada) | "El agente de amenaza es interno" / "Acción: actúa sobre la integridad del Activo por efectos de su modificación" |
| **Sobre la Organización** | Detección; Respuesta | "Detección: puede no detectarse con la sola existencia de un control al momento de la solicitud del título" / "Respuesta: incluirá la recuperación del registro a su valor establecido y la remediación incluirá las acciones administrativas y legales previstas en caso de fraude" |

Reglas de escritura de los factores que se deducen del ejemplo:
- Cada factor se responde con una **afirmación sobre el caso concreto**, no con un adjetivo suelto. Cuando se pone un adjetivo (Bajo, Medio, Ninguno) se lo acompaña de la razón: "Riesgo de Detección: Bajo. **Solo existen sanciones administrativas previstas en caso de ser probado el fraude**".
- Si un factor no aplica, se lo dice: "Beneficio: No Existe", "Costo: El costo no tiene una evaluación directa", "El costo no tiene una evaluación directa. El activo no puede recuperarse".
- Los factores no aplicables se omiten sin problema: en el riesgo 2 (accidental) no aparece Sensibilidad/Legal; en el riesgo 6 sí aparece Reputación (que no está en el 1).
- **La Capacidad de Resistencia es el factor bisagra**: es donde se declara qué controles faltan, y es lo que después las estrategias de mitigación atacan una por una.

###### Ficha de IDENTIFICACIÓN DE RIESGOS (estructura)

| Fila | Contenido |
|---|---|
| **Id. N** | Número del riesgo (mismo ID que en la planilla) |
| **Identificador** | Legajo + Apellido y Nombres del alumno que lo elaboró |
| **Especificación** | La frase única del riesgo (idéntica a la de la planilla) |
| **Clasificación** | Clase / Subclase / Elemento del SEI |
| **Descripción ampliada del Contexto del Riesgo** | Párrafo narrativo: quién, con qué permiso, motivado por qué, y qué competencias tiene |
| **Valoración del Riesgo** | Activos Involucrados + **Dimensión del valor para su criticidad** + factores de probabilidad + factores de impacto + PROBABILIDAD / IMPACTO / VALOR DE LA SEVERIDAD |

Nótese: la **Descripción ampliada** no repite la Especificación, la contextualiza. Ejemplo del riesgo 6: *"Los sobres entregados por el Jefe de Cátedra o presidente de mesa examinadora son entregados al Departamento de Carrera y el personal que lo recibe lo guarda en cajas habilitadas para tal fin. Las cajas son dejadas en lugares cercanos a ventanas que permiten el acceso de agua ante una tormenta de mediana severidad."* — agrega la condición física concreta que hace verosímil el riesgo.

También: **Activos Involucrados puede ser más de uno**, y se declara una sola **Dimensión** como eje de la criticidad ("Actas de Exámenes – Registro en el SYSACAD / Dimensión: Integridad"; "Exámenes Finales – Cajas de resguardo / Dimensión: Integridad").

###### Ficha de TRATAMIENTO: EVITAR / TRANSFERIR / MITIGAR

Las tres estrategias se responden **siempre**, aunque la respuesta sea negativa. Esto es clave: no se saltea "Evitar" porque no aplique; se escribe por qué no aplica.

**EVITAR** — una línea, y se argumenta que la actividad es indispensable para el negocio:
> R1: "No se puede evitar la realización de la actividad de registro de Exámenes"
> R6: "No se puede evitar la realización de la actividad de resguardo de los Exámenes Físicos"

**TRANSFERIR** — se evalúa seguro o tercerización:
> R1: "No se pueden subcontratar seguros o transferir a un tercero la realización de esta actividad"
> R6: "Se puede transferir la actividad de resguardo de los Exámenes Físicos a partir de las siguientes estrategias: Subcontratar una empresa que realice el almacenamiento y la gestión de activos de información"

**MITIGAR** — lista numerada de estrategias, **cada una con VENTAJA y, si corresponde, DESVENTAJA**, y la ventaja dice **sobre qué variable actúa (probabilidad, impacto o ambas) y por qué mecanismo**. Las 4 del riesgo 1:

| # | Estrategia | Ventaja | Desventaja |
|---|---|---|---|
| 1 | Especificación formal de la actividad de digitalización de Actas de Exámenes | Actúa sobre el impacto de pérdida de integridad del Activo | — |
| 2 | Auditorías esporádicas de consistencia entre Actas de Exámenes físicas (o digitalizadas) y los registros del SYSACAD | Anticipa el momento de detección (disminuye la probabilidad al aumentar la resistencia a la amenaza); actúa sobre el impacto de detección en el proceso de Trámite de Título | — |
| 3 | Implementación de Trazabilidad en el registro de Actas de Exámenes en el SYSACAD | Permite identificar el usuario que realizó la modificación, habilitando las sanciones previstas (disminuye la probabilidad al aumentar el riesgo de detección) | Puede ser costoso ya que depende de terceros |
| 4 | Procedimientos de monitorización periódicos sobre la trazabilidad (ITIL – Gestión de Eventos – **Monitorización pasiva**) que alerten ante accesos al registro de actas fuera de los momentos previstos | Ídem 3, aumentando aún más el riesgo de detección | Debe especificarse muy bien: podría generar numerosos falso-positivos |

Riesgo 6, mitigación única: *"Adecuar espacios separados con las condiciones adecuadas de temperatura y humedad, así como imposibilitados de acceso de agua u otras condiciones que posibiliten la materialización de otras amenazas de origen humanas, naturales o industriales."* VENTAJAS: disminuye la probabilidad y el impacto. DESVENTAJAS: se deberá establecer la viabilidad y el costo.

Patrones a copiar:
- Las estrategias se **encadenan**: la 4 depende de la 3 ("A partir de la implementación de la Trazabilidad se podrán establecer…").
- Cada mitigación ataca un factor FAIR nombrado antes. La 2 y la 3 atacan directamente lo que se declaró en Capacidad de Resistencia ("no existen auditorías", "no existe trazabilidad").
- Se citan marcos externos cuando aportan (ITIL, Gestión de Eventos, Monitorización pasiva).
- La desventaja no es decorativa: costo, dependencia de terceros, falsos positivos, viabilidad.

###### CONTROLES

Se listan como **nombre de control + Evidencias objetivas**. Es una dupla fija.

| Riesgo | Control | Evidencias objetivas |
|---|---|---|
| 1 | Copias de Seguridad (de las Actas de Exámenes digitalizadas) | Actas de exámenes digitalizadas; Existencia de Copias de Seguridad según las normas establecidas; Registros de realización de copias de seguridad; Informe de auditoría de Digitalización de Actas de Exámenes |
| 1 | Gestión de Eventos | Logs de usuarios; Registros de trazabilidad |
| 6 | Seguridad de la información en las relaciones con proveedores | SLA con proveedor de servicio; Informes de Auditoría |
| 6 | Protección contra las amenazas físicas y ambientales | Revisiones periódicas del estado de las instalaciones |

Los nombres de control son los de la norma (dominios/controles ISO 27001-27002 según Declaración de Aplicabilidad ONTI). Notar que cada control corresponde a una estrategia: el control de proveedores garantiza la *transferencia*, el de amenazas físicas garantiza la *mitigación*.

###### Riesgo Residual

No se recalcula un número: **se argumenta cualitativamente qué queda de probabilidad y qué queda de impacto después de aplicar las estrategias, y se concluye si alcanza o hay que seguir tratando.**

Riesgo 1 (textual): *"El impacto en la integridad del activo se reduce a las acciones necesarias para establecer el plan de recuperación de la integridad del activo modificando la nota a su valor real en función del acta digitalizada en el momento de la auditoría. La probabilidad de que esta amenaza se materialice a raíz de haber aumentado considerablemente el riesgo de detección es muy baja o inexistente. La severidad calculada del riesgo residual no justifica la realización de otras estrategias para su tratamiento."*

Estructura de esa argumentación: (a) qué pasa con el **impacto** y a qué queda reducido; (b) qué pasa con la **probabilidad** y por qué mecanismo bajó; (c) **veredicto**: si la severidad residual justifica o no más tratamiento.

Riesgo 6 (textual): *"En la estrategia de transferencia el riesgo residual es cero porque se ha transferido el mismo a la gestión de contratos con terceros. En la estrategia de mitigación se ha bajado considerablemente la probabilidad sin embargo se deberá establecer la viabilidad y el costo."*

Patrón adicional: **si hay varias estrategias alternativas, se calcula el residual de cada una por separado.** Transferencia → residual cero (queda en el contrato). Mitigación → baja probabilidad pero queda pendiente la viabilidad económica.

###### Planes de Contingencia, Recuperación y Continuidad

Definiciones que da el propio material:

| Plan | Definición textual |
|---|---|
| **Contingencia** | "acciones a realizar ante la detección de materialización del riesgo" |
| **Recuperación** | "acciones a realizar para recuperar los activos para la normal operación (si es posible). Acciones de remediación previstas" |
| **Continuidad de negocio** | "acciones a realizar mientras se están ejecutando los planes de contingencia y recuperación" |

Se especifican **a partir de los riesgos y de los controles**, no de la nada.

**Disparadores.** Son eventos observables que indican posible materialización. Se derivan de las estrategias de mitigación ya definidas — el ejemplo hace la referencia cruzada explícita:

Riesgo 1: (1) Inconsistencias en el control de Notas de Exámenes en el proceso de Emisión de Título; (2) Inconsistencias en las auditorías de registros de Actas de Exámenes **especificadas en la estrategia de tratamiento del riesgo 2**; (3) Identificación de actividad inusual de los usuarios en el registro de Actas de Exámenes **a partir del procedimiento establecido en la estrategia de tratamiento de riesgo 4**.

Riesgo 6: (1) Alertas meteorológicas; (2) Notificación de debilidades referidas al resguardo de cajas con sobres de Exámenes Físicos. — Acá los disparadores son **preventivos** (anteriores al daño), no sólo detectivos.

**Contingencia.** Acciones inmediatas, y **ramificadas según cuál disparador se activó**:
> R1: "En caso de que la detección se haya originado por los disparadores 1 o 2: a) Quitar los permisos de acceso a la aplicación del personal identificado como posible atacante. En caso de que la detección se haya originado por el disparador 3: b) Verificar la posibilidad de un falso positivo y luego ejecutar el plan de contingencia indicado en a)"

> R6: "a) Revisión de las áreas consideradas Seguras (con existencia de documentación sensible); b) Ante la detección comunicar al propietario de los activos involucrados; c) Proceder a evaluar las necesidades de asegurar el área o el activo amenazado: Cerrar el área / Mover las cajas con sobres de Exámenes Físicos a lugar seguro"

Notar el manejo del **falso positivo** en R1: es la desventaja que se había declarado en la mitigación 4, y reaparece como paso del plan. Coherencia de punta a punta.

**Recuperación.** Restaurar el activo + remediar (típicamente el sumario administrativo):
> R1: "1. Modificar la Nota a su valor real en función de la información obtenida del Acta de Exámenes física o digitalizada. 2. Iniciar el sumario administrativo correspondiente"
> R6: "En función de la actividad desarrollada en el plan de contingencia - c) 1. Volver las cajas con sobres de Exámenes Físicos al lugar correcto. 2. Iniciar el sumario administrativo correspondiente a las personas consideradas custodios del Activo"

**Continuidad de Negocio.** Cómo sigue operando el proceso mientras tanto:
> R1: "Reemplazar al Personal identificado como posible atacante por otro empleado con las competencias necesarias para el registro de Actas de Exámenes"
> R6: "No se requieren acciones para la continuidad del negocio"

Que la respuesta válida sea "no se requieren acciones" es parte del patrón: **se responde siempre, aunque sea para descartar.**

**Controles de Garantía de los Planes.** Cierran la ficha, agrupados por familia:

| Riesgo | Familia | Controles |
|---|---|---|
| 1 | Controles de Personas | Antes de la Contratación: Investigación de antecedentes / Términos y Condiciones del empleo. Durante la Contratación: Concientización – Educación – Capacitación / Proceso Disciplinario |
| 1 | Controles organizacionales | Respuesta a incidentes de seguridad de la Información |
| 6 | Controles de Personas | Durante la Contratación: Concientización – Educación – Capacitación / Proceso Disciplinario |
| 6 | Controles organizacionales | Gestión de incidentes de seguridad de la Información |

###### Cadena de trazabilidad completa (el patrón en una línea)

Activo del inventario → C/I/D → Criticidad ≥ 6 o alguna dimensión = 3 → amenaza descompuesta (Acceso / Actor / Motivo / Resultado) → vulnerabilidad explotada → **Especificación** → Clasificación SEI → factores FAIR de probabilidad e impacto → P × I = Severidad → priorización decreciente → Evitar/Transferir/Mitigar (con ventaja/desventaja) → Controles + Evidencias → Riesgo Residual → Disparadores → Contingencia / Recuperación / Continuidad → Controles de Garantía.

**Cada eslabón tiene que poder rastrearse al anterior.** El ejemplo lo hace explícito: la mitigación cita el factor FAIR que ataca, el disparador cita el número de la estrategia que lo produce, la contingencia cita el disparador que la activa, la recuperación cita el paso de la contingencia.

###### Errores y cosas a evitar (deducidos del ejemplo)

Del material mismo — el ejemplo tiene defectos que conviene no replicar:

1. **IDs duplicados.** `SW_REDES001` se usa para SYSACAD y para Microsoft SQL Server. `INS_002` para dos instalaciones distintas. `I_EXA007` para "Exámenes Físicos" y para "Planilla de Entrega de Exámenes Físicos". El ID debe ser único.
2. **Valores inconsistentes entre planilla y ficha.** Riesgo 1: P=5/I=2/Sev=10 en la planilla vs. P=4/I=1/Sev=4 en la ficha. Si se llenan dos artefactos, tienen que decir lo mismo.
3. **Texto de factores contradictorio entre artefactos.** El impacto sobre Productividad del riesgo 1 dice una cosa en la planilla y la contraria en la ficha.
4. **Riesgos sin valorar.** Los riesgos 2, 3, 4, 5 tienen Probabilidad e Impacto vacíos y Severidad 0 en la planilla. Sin valoración no hay priorización posible.
5. **Ficha de Planes con el Id. equivocado.** La ficha de Planes del riesgo 6 arranca con "Id. 1". Copy-paste sin revisar.
6. **Activos inventariados sin valorar.** Hardware, Instalaciones y Servicios quedan con criticidad 0 y sin C/I/D. Si un activo no se valora, no puede entrar nunca en el corte de criticidad — y sin embargo el riesgo 6 depende de las instalaciones del Departamento de Carrera.
7. **La criticidad del proceso `PO_EXA` (=5) no responde a la fórmula C+I+D** que declara el documento (que daría 20 con las 5 dimensiones, o 10 con C+I+D). Si se cambia de escala hay que declararlo.
8. **La escala 1–4 del documento vs. 0–3 de la planilla.** Fijar la escala una sola vez y usarla en todos lados.

Errores conceptuales que el ejemplo evita y conviene imitar:

- No confundir **riesgo** con **vulnerabilidad**: "falta de trazabilidad" es vulnerabilidad; el riesgo es "modificación deliberada del registro… por parte de…".
- No poner el **control** dentro de la especificación del riesgo.
- No fusionar deliberado y accidental en un solo riesgo.
- No dejar Evitar/Transferir en blanco: la negativa argumentada es la respuesta correcta cuando no aplican.
- No poner ventajas sin decir **sobre qué variable** (probabilidad / impacto) actúan.
- No poner controles sin **evidencia objetiva** asociada.
- No cerrar el riesgo residual con un número sin argumento; y si hay estrategias alternativas, evaluarlas por separado.

###### Fuentes

- `fuentes/ASI/Material de Cursado/Unidad 2/5 - Ejemplo (ProcesoExamenesUTN)/ASI-2-InventarioActivos_ProcesoExamenes.xlsx` — inventario de activos (8 hojas) + hoja RiesgosInherentes (6 riesgos).
- `fuentes/ASI/Material de Cursado/Unidad 2/5 - Ejemplo (ProcesoExamenesUTN)/ASI_2_GestiónDeRiesgos-ProcesoExamenes.docx` — metodología, escalas C/I/D, comunidades de amenaza, y fichas completas de Identificación / Tratamiento / Planes para los riesgos 1 y 6.

Nota sobre la conversión: el .docx incluye un organigrama del Comité de Seguridad de la Información como imagen embebida (base64) que markitdown no convirtió a texto — su contenido no está disponible. Las tablas del .docx vienen con celdas combinadas mal reconstruidas (columnas vacías sobrantes), pero el contenido es legible. La planilla vino con celdas fusionadas convertidas en filas con `NaN`, que corresponden a contenedores adicionales del activo de la fila superior.

#### Ejercicios resueltos tipo

- **Ejemplo de cátedra:** Gestión de Riesgos del Proceso de Exámenes UTN (transcripto arriba). Fija el nivel de detalle esperado en las planillas.
- **Resolución propia:** Etapa 2 del TP Integrador — 11 activos, 10 riesgos, 5 planillas completas. Ver sección **TP Integrador**.

#### Dudas / pendientes

- Confirmar con cátedra si la escala de valoración C/I/D es siempre 1–3 (así se usó en el ejemplo y en la Etapa 2) o si admite 1–5.
- Confirmar si la escala de Probabilidad/Impacto 1–5 con severidad 1–25 es la oficial de cátedra o una elección del grupo.

#### Fuentes

- `fuentes/ASI/Material de Cursado/Unidad 2/1 - Apunte - AreasTI (V1.0).pdf`
- `fuentes/ASI/Material de Cursado/Unidad 2/2 - PPT - AreasTI Riesgos (V2.5).pdf`
- `fuentes/ASI/Material de Cursado/Unidad 2/3 - Definición de Riesgo.docx`
- `fuentes/ASI/Material de Cursado/Unidad 2/4 - Taxonomia FAIR.pdf`
- `fuentes/ASI/Material de Cursado/Unidad 2/6 - PPT - AreasTI Servicios (V2.1).pdf`
- `fuentes/ASI/Material de Cursado/Unidad 2/Planillas utiles/` (Estructura de la Tabla de Activos, Planillas de Riesgo, ISO 27002 Controles, Taxonomías para la Identificación de Riesgos)
- `fuentes/ASI/Material de Cursado/Unidad 2/5 - Ejemplo (ProcesoExamenesUTN)/` (Inventario de Activos + Gestión de Riesgos)

---

### Unidad 3 — Dirección de Talento y Capital Humano

> Unidad ingerida el 2026-08-19 desde el campus. **Desarrollo parcial**: los DIAP de cátedra son mayormente imágenes y la conversión rescató poco texto. Lo que sigue es lo que sí se extrajo, más el ejemplo de puesto de trabajo, que es lo que la Etapa 3 necesita.

#### Conceptos clave

- **De "recursos humanos" a "talento humano"** — el cambio de paradigma que plantea la cátedra: la persona deja de ser un recurso intercambiable y pasa a ser portadora de competencias.
- **El planeamiento del capital humano se deriva del planeamiento estratégico de la organización**, no al revés. Es el mismo encadenamiento de la Unidad 1.
- **Tres familias de procesos de RRHH**: *atraer y captar* (reclutamiento y selección) · *retener* (remuneración, ambiente seguro, higiene laboral, relaciones laborales) · *desarrollar* (capacitación, evaluación de desempeño, desarrollo de personal).
- **Perfil ≠ descripción de puesto.** La descripción dice qué se hace en el puesto; el perfil dice qué tiene que tener la persona para hacerlo.
- **Gestión por competencias** (Alles) — bibliografía obligatoria de la cátedra para esta unidad.

#### Desarrollo

##### 1. Descripción de puesto y perfil — la plantilla de cátedra

Este es el aporte concreto de la unidad para el **punto 5 de la Etapa 3**. La cátedra tiene un ejemplo real (`EjemploPuestoTrabajo/`) con esta estructura:

| Bloque | Campos |
|---|---|
| **Identificación** | Nombre del puesto · Área · Objetivo del puesto · El puesto reporta a · Personal a cargo |
| **Descripción de tareas** | Principales tareas y responsabilidades, redactadas como acciones con finalidad (*"analizar los procesos operativos… **con la finalidad de** desarrollar e instalar sistemas de información"*) |
| **Perfil del puesto** | Estudios · Experiencia requerida · Idiomas · Conocimientos específicos · Capacidades y habilidades |

> Ejemplo de cátedra: *Encargado de Sistemas* del Instituto de Bioquímica Clínica. Objetivo del puesto: "gestionar y coordinar los recursos necesarios relacionados con el desarrollo e implementación de Sistemas de Información". Reporta a Dirección, con soporte técnico y desarrollador a cargo. En *capacidades y habilidades* lista: liderazgo, habilidad analítica, iniciativa, flexibilidad, orientación al cliente, manejo de personal, trabajo en equipo, responsabilidad, disciplina, toma de decisiones.

**Para la Etapa 3**: la consigna pide "perfiles y competencias". Esta plantilla es más rica que la tabla de cinco columnas que sugieren las prácticas — conviene usar la tabla resumen para la vista general y esta ficha para dos o tres perfiles clave.

##### 2. Evaluación de desempeño

La cátedra da un ejemplo completo (`3-Evaluacion de desempeño - Encargado de Sistemas.doc`) y una planilla modelo. No lo pide la Etapa 3, pero es contenido de unidad evaluable.

#### Ejercicios resueltos tipo

- `ASI-3_Ejercitacion1- Talento y Capital Humano.docx` — ejercitación de la unidad. *(Ingerida, sin desarrollar en detalle.)*
- `EjemploPuestoTrabajo/` — 4 archivos: consigna del trabajo final de Adm. RRHH, descripción de puesto y perfil, planilla modelo y evaluación de desempeño.

#### Dudas / pendientes

- **Desarrollo incompleto.** Los DIAP v2.3 y v2.4 son casi todo imágenes; la conversión rescató los títulos pero no el contenido de las láminas. Hay que leerlos a mano o pedir el apunte en texto.
- **No hay apunte de texto** de esta unidad, solo diapositivas.
- No se copió `CompetenciasIngSistemas/` del campus (CONFEDI, Res. 1254-2018, Competencias del Ingeniero Iberoamericano) — son 4 PDF grandes de estándares de carrera. Están en el campus si hacen falta.

#### Fuentes

- `fuentes/ASI/Campus/ASI-Unidad3_DireccionTalento_CapitalHumano/ASI-3-Direccion de Talento y Capital Humano_DIAP.v2.3.pdf` y `otros/…v2.4.pdf`
- `fuentes/ASI/Campus/ASI-Unidad3_DireccionTalento_CapitalHumano/ASI-3_Ejercitacion1- Talento y Capital Humano.docx`
- `fuentes/ASI/Campus/ASI-Unidad3_DireccionTalento_CapitalHumano/EjemploPuestoTrabajo/` (4 archivos, `.doc` legacy → `textutil`)
- `fuentes/ASI/Campus/ASI-Unidad3_DireccionTalento_CapitalHumano/ASI-3-…_EjemploEvaluaciónCompetencias.pdf`

---

### Unidad 4 — Higiene y Seguridad Laboral

> Unidad ingerida el 2026-08-19 desde el campus. Apunte de 64 páginas (Lic. Sergio J. Gasparroni) + diapositivas.
> **Es la unidad que sostiene el punto 6 de la Etapa 3** (layout + medidas de protección).

#### Conceptos clave

- **Riesgo laboral** = la posibilidad de que un trabajador sufra un determinado daño derivado del trabajo. **Daños derivados del trabajo** = enfermedades o accidentes laborales.
- **Salud, definición de la OMS**: no es la mera ausencia de afecciones y enfermedades, sino el **estado de plena satisfacción física, psíquica y social**. Por eso la unidad no se agota en accidentes.
- **Condiciones de trabajo** — cuatro grupos: *de seguridad* (locales, instalaciones, equipos, almacenamiento y manipulación de cargas, inflamables, químicos) · *ambientales* (agentes físicos, químicos y biológicos, calor y frío, iluminación, ventilación) · *carga de trabajo* (física y mental) · *organización del trabajo* (monotonía, repetitividad, aislamiento, participación). Cuando pueden originar daño se las llama **factores de riesgo** o **peligros**.
- **Tres tipos de riesgo**: de **accidentes** · **ambientales** (dosis de agente recibida; efectos *agudos* inmediatos vs. *crónicos* diferidos) · **psicosociales**.
- **Cinco disciplinas de la prevención**: Seguridad en el Trabajo · Higiene Industrial · Medicina del Trabajo · Psicosociología del Trabajo · **Ergonomía**.
- **Tres niveles de prevención (OMS)** — y esto es lo más útil para el TP, ver abajo.

#### Desarrollo

##### 1. Agentes de riesgo ambiental

| Químicos | Físicos | Biológicos |
|---|---|---|
| Gases · Vapores · Nieblas · Polvos · Humos | Ruido · Vibraciones · Presiones extremas · Temperaturas extremas · Radiaciones | Insectos · Bacterias · Virus · Hongos · Mohos |

##### 2. Los tres niveles de prevención — y por qué importan en el layout

**Prevención primaria** — evitar el riesgo o su materialización. Es *la más eficaz y la más eficiente*, y se ordena en cuatro acciones, de mayor a menor jerarquía:

| Orden | Acción | Objeto |
|---|---|---|
| 1 | **En el diseño** — de instalaciones, equipos, herramientas y **puestos de trabajo** | Evitar el riesgo o minimizarlo |
| 2 | **En el origen** — evitar riesgos por defectos de fabricación, construcción o instalación | Eliminar o reducir el riesgo |
| 3 | **En el medio de transmisión** — interponer barreras entre el origen y la persona | Controlar el riesgo |
| 4 | **Sobre la persona** — EPP, educación, vigilancia de la salud, reducción del tiempo de exposición | Proteger a la persona |

**Prevención secundaria** — la alteración de la salud ya empezó aunque no se manifieste: vigilancia de la salud, diagnóstico precoz, tratamiento eficaz.
**Prevención terciaria** — evitar reincidencias, recaídas, complicaciones o secuelas: tratamiento y rehabilitación.

> **Por qué esto resuelve la crítica de la cátedra al punto 6.** Las prácticas advierten que no alcanza con "silla ergonómica, pausas activas y matafuegos". El motivo, con el marco de la unidad a la vista, es que **todas esas medidas son de nivel 4 — prevención sobre la persona, el escalón más débil**. Un layout bien hecho demuestra **prevención en el diseño** (nivel 1): circulación separada de peatones y vehículos, distancias, ubicación de salidas, zonas restringidas. El EPP se menciona como complemento, no como respuesta principal.

##### 3. Las cinco disciplinas

- **Seguridad en el Trabajo** — medidas en todas las fases de actividad de la empresa para evitar o minimizar los riesgos laborales.
- **Higiene Industrial** — protege la integridad física y mental estudiando dos variables, *el hombre y su ambiente de trabajo*. Es preventiva: identificar agentes · medir la exposición (concentración y tiempo) · valorar contra valores de referencia · corregir · controlar periódicamente · **capacitar a los trabajadores sobre los riesgos identificados**.
- **Medicina del Trabajo** — exámenes preocupacionales y periódicos, psicotécnicos, aptitud para **trabajos en altura**, asistencia por accidentes, campañas y capacitación.
- **Psicosociología del Trabajo** — precariedad, estrés, esfuerzo mental, monotonía, acoso laboral, síndrome del trabajador quemado (*burn-out*).
- **Ergonomía** — adaptación del puesto a la persona.

##### 4. Sistema de Gestión en Higiene y Seguridad Laboral

Elementos que enumera el apunte: administración y entrega de **EPP** · mediciones de desempeño del personal (sistemas seguros de trabajo, **permisos de trabajo**, respeto de procedimientos) · mediciones de efectividad por auditorías, acciones correctivas e **indicadores de siniestralidad** · mediciones de agentes químicos por laboratorios acreditados · **preparación y respuesta ante emergencias**. Cierra con verificación (no conformidades, acciones correctivas y preventivas, auditorías internas y externas) y revisión por la Dirección.

Certificación: **OHSAS 18001** (*Occupational Health and Safety Assessment Series*), compatible con ISO 9001 e ISO 14001. La bibliografía del programa suma la familia **ISO 45000**.

##### 5. Legislación argentina

| Norma | Qué regula |
|---|---|
| **Ley 19.587** de Higiene y Seguridad en el Trabajo + decreto reglamentario | Marco general de condiciones de higiene y seguridad |
| **Ley 24.557** de Riesgos del Trabajo (1995) + decreto reglamentario | Cambio estructural: crea el sistema de **ART** y la **SRT** (Superintendencia de Riesgos del Trabajo) |
| **Ley 20.744** de Contrato de Trabajo | Relación laboral |
| **Ley 27.555** de Teletrabajo | Régimen legal del contrato de teletrabajo |

> Esta tabla alimenta directamente la **factibilidad legal** de la Etapa 3, que hasta ahora solo tenía las normas de telecomunicaciones y datos personales. Un proyecto con trabajo en altura, espacios confinados y riesgo eléctrico tiene obligaciones bajo 19.587 y 24.557 que hay que nombrar.

#### Ejercicios resueltos tipo

- *(Pendiente: no hay ejercitación específica de esta unidad en el campus.)*

#### Dudas / pendientes

- El apunte es de **abril de 2014** y menciona OHSAS 18001, que fue reemplazada por **ISO 45001:2018**. La bibliografía del Programa Analítico sí cita la familia ISO 45000. Confirmar cuál toma la cátedra hoy.
- Los Anexos I a IV del apunte (riesgos por lugar de trabajo, ergonomía y psicología aplicada, medicina laboral, certificación OHSAS) están ingeridos pero **sin desarrollar acá**. El Anexo I es el catálogo de riesgos por tipo de lugar y equipo — es la fuente natural para justificar las medidas del layout.
- Falta el número de decreto reglamentario de la Ley 19.587 (es el **351/79**, *conocimiento general, no del apunte* — verificar antes de citarlo en la entrega).

#### Fuentes

- `fuentes/ASI/Campus/ASI-Unidad4_Higiene_y_Seguridad_Laboral/ASI-4-Higiene y Seguridad_APUNTE.V1.2.pdf` — 64 páginas, Lic. Sergio J. Gasparroni.
- `fuentes/ASI/Campus/ASI-Unidad4_Higiene_y_Seguridad_Laboral/ASI-4-Higiene y Seguridad_DIAP.V2.0.pdf` — **casi todo imágenes, la conversión rescató muy poco**.

---

### Unidad 5 — Administración de Recursos en Proyectos de Sistemas y Tecnologías de Información

> Unidad de cinco capítulos en el campus: **T1 Proyectos · T2 Integración, Alcance y Cierre · T3 Gestión del Tiempo · T4 Gestión de Costos · T5 Gestión de Adquisiciones**. Apuntes de la Esp. Lic. Fabiana María Riva.
>
> **Origen del material.** Ingerido completo el 2026-08-19 desde el campus. Se suman la consigna de la Etapa 3 del TPI, las sugerencias de cátedra del 28/07/2026, la ejercitación de U5 y el caso integral resuelto (Centro de Servicios). Está indicado en cada caso cuando algo no sale del apunte.
>
> **Ojo — la ejercitación de U5 y la Etapa 3 del TPI no piden lo mismo.** Ver la tabla comparativa en §13. Para entregar el TP se sigue la consigna de la Etapa 3; la ejercitación de U5 cubre la unidad completa y **puede aparecer en evaluación**.

#### Conceptos clave

- **La cadena de la Etapa 3** (lo que la cátedra pide encadenar, no responder por separado):

  `Problema o necesidad detectada → Proyecto de TI → Objetivos → Alternativas → Solución seleccionada → EDT → Recursos → Tiempo → Costos → Factibilidad`

- **Nada es una respuesta independiente.** Los perfiles surgen de las actividades de la EDT; las adquisiciones surgen de la solución seleccionada; el Gantt surge de las actividades, duraciones y dependencias; los costos surgen de los recursos y adquisiciones; y la factibilidad evalúa si todo lo anterior puede realizarse.
- **Objetivo ≠ actividad.** "Capacitar al personal" o "desarrollar el sistema" son entregables, no objetivos. El objetivo expresa el **resultado**: "lograr que el 90% de los usuarios apruebe la evaluación posterior a la capacitación".
- **La EDT es la fuente principal del resto de la planificación.**
- **RFI** se usa cuando todavía hay que explorar el mercado; **RFP** cuando los requerimientos ya están definidos y se pide una propuesta formal.
- **CPM**: sobre la red de precedencias se calculan ES / EF / LS / LF por actividad. **Holgura = LS − ES = LF − EF**. Las actividades de holgura 0 forman el **camino crítico**, que fija la duración del proyecto. La duración total **no es la suma de las duraciones** — las ramas paralelas se solapan.
- **TCO (Total Cost of Ownership)** — costo real de poseer, usar, mantener y retirar un activo o servicio **a lo largo de todo su ciclo de vida**, no solo el precio de compra.
- **BAC (Budget At Completion)** — presupuesto total del proyecto; sale de asignar presupuesto a cada actividad de la EDT y sumarlos.
- **Los beneficios se monetizan.** Un beneficio sirve para la factibilidad económica cuando se traduce a horas liberadas × costo hora, o a costos evitados. "Mejora la gestión" no es un beneficio evaluable.
- **RA3 de la asignatura** (resultado de aprendizaje que esta unidad cubre): *evaluar propuestas de proyectos y emprendimientos de base tecnológica vinculados a los SI y TI **considerando su impacto social y ambiental***.
- **Proyecto** = trabajo **singular**, con fechas definidas de inicio y fin, alcance claro, presupuesto preestablecido y una organización temporal que se desmantela al terminar. Tres rasgos: **temporal**, **producto/servicio/resultado único**, **elaboración gradual**.
- **Proyecto vs. proceso**: comparten que los hacen personas, están restringidos por recursos y se planifican, ejecutan y controlan. Difieren en que **los procesos son continuos y repetitivos, y los proyectos temporales y únicos**.
- **Triple restricción**: alcance, tiempo y costo. La **calidad** se ve afectada por el equilibrio entre los tres — si cambia uno, cambia al menos otro.
- **Las 9 áreas de conocimiento del PMI**: Integración · Alcance · Tiempos · Costos · Calidad · RRHH · Comunicaciones · Riesgos · Adquisiciones.
- **Fast tracking** (paralelizar lo que iría en secuencia, sube el riesgo) y **crashing** (agregar recursos, sube el costo) son los dos métodos para acortar la duración **sin reducir el alcance**.
- **Cuatro técnicas de evaluación de inversiones**: TR (tiempo de recuperación) · TPR (tasa promedio de retorno) · VAN · TIR.
- **Beneficios = Ingresos + Costos evitados.**

#### Desarrollo

##### 1. Definición del proyecto

**Qué es un proyecto, según el apunte.** Un trabajo singular con fechas definidas de inicio y finalización, una especificación clara del objetivo o el alcance, un presupuesto preestablecido y, habitualmente, una organización temporal que se desmantela cuando el proyecto termina.

- **Temporal** — tiene comienzo y final definidos. El final llega cuando se lograron los objetivos, cuando queda claro que **no** podrán alcanzarse, o cuando la necesidad desaparece y el proyecto se cancela. *Temporal no significa de corta duración.*
- **Producto, servicio o resultado único** — un artículo cuantificable, la capacidad de prestar un servicio, o un resultado (salidas o documentos que sirven para determinar una tendencia).
- **Elaboración gradual** — desarrollar en fases e ir incorporando funcionalidad por incrementos, coordinado con una definición adecuada del alcance (crítico si hay contrato de por medio).

**Jerarquía:** *Portafolio* = conjunto de proyectos, programas y procesos para cumplir los objetivos estratégicos del negocio. *Programa* = agrupación de proyectos. *Subproyecto* = subdivisión de un proyecto para mejorar su gestión.

> **Por qué existen los proyectos:** son una forma de organizar actividades que **no pueden tratarse dentro de los límites operativos normales** de la organización. Por eso se usan como medio para lograr el plan estratégico — el mismo hilo que la Unidad 1.

**Tipos de proyecto**, según qué tan conocidos sean el producto y el método: producto conocido + método conocido → *Producción* · producto nuevo + método conocido → *Construcción* · producto conocido + método desconocido → *Servicios* · producto nuevo + método desconocido → *Ingeniería*.

La descripción del proyecto tiene que responder seis preguntas:

| Pregunta | Qué se espera |
|---|---|
| ¿Qué problema resuelve? | Falla concreta u oportunidad detectada: tickets repetidos, procesos manuales, falta de trazabilidad, sistema obsoleto, demoras, errores, baja disponibilidad |
| ¿Qué solución se propone? | Implementar / desarrollar / mejorar / adquirir una solución de TI |
| ¿Qué proceso o servicio afecta? | El proceso crítico ya definido en la Etapa 1 |
| ¿Quiénes serán sus usuarios? | Roles concretos, no "la empresa" |
| ¿Qué incluye? | Alcance positivo |
| ¿Qué NO incluye? | Alcance negativo — esto es lo que evita el proyecto-paraguas tipo "digitalizar toda la empresa" |

Formulación tipo: *"Vamos a implementar/desarrollar/mejorar/adquirir una solución de TI para resolver X problema en Y proceso."*

**Ejemplo incompleto (cátedra):** "Implementar inteligencia artificial en la empresa."
**Ejemplo correcto (cátedra):** "Implementar un asistente virtual interno integrado a Microsoft Teams para responder consultas operativas frecuentes, reducir la carga de tickets de nivel 1 y derivar a soporte humano las consultas no resueltas."

##### 2. Objetivos cuantificables

La consigna no pide "objetivos" sino **criterios que permitan evaluar avance y cumplimiento**. Cada objetivo debe tener cinco componentes:

| Componente | Descripción |
|---|---|
| Resultado | Qué estado se alcanza |
| Indicador | Fórmula o métrica concreta |
| Valor inicial (línea base) o meta | Desde dónde se parte y a dónde se llega |
| Plazo | En cuánto tiempo |
| Forma de medición | Con qué sistema/reporte se mide y quién es responsable |

**Ejemplo de cátedra:** *"Reducir en un 30% la cantidad mensual de tickets de soporte de nivel 1 durante los primeros seis meses posteriores a la implementación, utilizando los reportes del sistema ITSM."*

Otros ejemplos de formulación válida dados en clase: reducir 30% los tiempos de respuesta en 6 meses; disminuir 40% los tickets repetidos; alcanzar 95% de disponibilidad mensual.

**Error frecuente marcado por la cátedra:** definir actividades como objetivos.

##### 3. Alternativas y selección

Las alternativas deben resolver **el mismo problema** de maneras distintas. Menú típico: desarrollo interno, solución SaaS configurable, desarrollo tercerizado, mejora del sistema actual, reemplazo completo, integración con herramienta existente.

**Criterios de comparación** que enumera la cátedra: costo, tiempo, calidad, riesgo, conocimientos disponibles, dependencia de proveedores, seguridad, escalabilidad, mantenimiento, integración con sistemas actuales.

**Matriz de selección ponderada** (formato de la cátedra):

| Criterio | Peso | Interno | SaaS | Tercerizado |
|---|---|---|---|---|
| Costo | 25% | 3 | 4 | 2 |
| Tiempo | 20% | 2 | 5 | 3 |
| Integración | 20% | 5 | 3 | 4 |
| Seguridad | 20% | 4 | 4 | 3 |
| Mantenimiento | 15% | 3 | 4 | 3 |

**Cómo NO redactar la conclusión:** "Elegimos SaaS porque es la mejor."
**Cómo SÍ:** *"Se selecciona SaaS porque obtiene el mayor resultado ponderado, reduce el plazo de implementación y se integra con la infraestructura existente, aunque genera dependencia del proveedor y costos recurrentes."* — es decir: resultado + razones por criterio + **contras asumidas explícitamente**.

##### 4. Ciclo de vida

No se elige por moda, se justifica por la naturaleza de los requerimientos:

| Ciclo de vida | Cuándo corresponde |
|---|---|
| **Predictivo / cascada** | Requerimientos estables, alta regulación, entregables claramente definidos |
| **Iterativo o incremental** | Se requieren entregas parciales y retroalimentación |
| **Ágil** | Alta incertidumbre y necesidad de revisar prioridades frecuentemente |
| **Híbrido** | Algunas etapas son previsibles y otras necesitan iteración |

##### 5. Fases y EDT / WBS

**Fases tipo para una implementación de software** (ejemplo de cátedra): 1. Inicio — 2. Relevamiento y análisis — 3. Diseño — 4. Adquisición o configuración — 5. Desarrollo e integración — 6. Pruebas — 7. Capacitación y puesta en producción — 8. Cierre.

**La EDT no es una lista general** ("analizar, desarrollar, probar, implementar"). Debe descomponerse hasta un nivel que permita estimar **responsable, duración, costo y entregable**.

Formato de tabla exigido:

| ID | Paquete/actividad | Predecesora | Duración | Perfil | Entregable |
|---|---|---|---|---|---|
| 1.1 | Elaborar Acta del Proyecto | — | 2 días | PM | Acta aprobada |
| 1.2 | Relevar requerimientos | 1.1 | 5 días | Analista funcional | Documento de requerimientos |
| 1.3 | Validar requerimientos | 1.2 | 2 días | Analista + usuario clave | Requerimientos aprobados |
| 2.1 | Configurar plataforma | 1.3 | 7 días | Especialista técnico | Entorno configurado |
| 2.2 | Integrar con sistemas | 2.1 | 10 días | Desarrollador | Integración funcional |
| 3.1 | Ejecutar pruebas | 2.2 | 5 días | Tester | Informe de pruebas |
| 3.2 | Capacitar usuarios | 3.1 | 3 días | Capacitador | Usuarios capacitados |
| 3.3 | Salida a producción | 3.2 | 1 día | Equipo técnico | Sistema operativo |

##### 6. Acta de Proyecto (PMI)

**Plantilla oficial conseguida** — `fuentes/ASI/Ejercitación/ASI-5-T1-Proyectos_AnexoI_ActaProyecto.doc` (Anexo I de cátedra, 3 páginas). Es un **formulario**, no un documento libre. Campos, en orden:

| Campo | Qué va |
|---|---|
| `ACTA DEL PROYECTO:` | Nombre del proyecto |
| `DE:` | Quién emite el acta — el patrocinador o autoridad que designa |
| `PARA:` | A quién se dirige — el líder de proyecto designado |
| `DESIGNACIÓN` | Designación formal del líder de proyecto |
| `DESCRIPCIÓN DE SU RESPONSABILIDAD` | Qué debe hacer el líder |
| `DESCRIPCIÓN DE SU AUTORIDAD` | Qué puede decidir por sí mismo y qué debe elevar |
| **ALCANCE DEL PROYECTO** → `Justificación` | Por qué se hace el proyecto |
| → `Producto` | Qué queda cuando termina |
| → `Entregables` | Lista de entregables |
| → `Objetivos` | Los objetivos cuantificables — **los mismos del punto 2**, no otros |
| → `Límite` | Qué **no** incluye |
| `Firma Autorizante` | Nombre y Título del autorizante |

> El campo `Límite` es el que suele quedar vacío y es justamente donde se demuestra que el alcance está acotado. Se completa con el "qué NO incluye" ya redactado.

**Instrucciones de la cátedra, campo por campo** (Anexo I del apunte T2, con ejemplo del proyecto *Redefinición de la arquitectura tecnológica para servicios de base de datos de ESABAL S.A.*):

| Campo | Qué pide la cátedra | Ejemplo del apunte |
|---|---|---|
| `DE` | Nombre y rol dentro de la organización del **patrocinador** | *Miguel Fernández, Gerente General de ESABAL S.A.* |
| `PARA` | **Todos los stakeholders** que deben tener conocimiento del proyecto | *Integrantes de los Departamentos de Sistemas, Compras, Financiera y RRHH, y el equipo del proyecto* |
| `DESIGNACIÓN` | Lista de personas designadas por el patrocinador **y sus roles** | *Juan Pérez – Director de Proyecto · María Rodríguez – Administradora de Bases de Datos* |
| `RESPONSABILIDAD` | Para cada persona de la lista, qué le **encomienda** el patrocinador | *Juan Pérez dirigirá el proyecto y nombrará al equipo. María Rodríguez será el nexo con la organización* |
| `AUTORIDAD` | Para cada persona, qué le **delega** el patrocinador | *María Rodríguez puede aprobar compras hasta el monto fijado; para excederlo debe pedir autorización a Gerencia Financiera* |
| `Justificación` | Debilidades, amenazas, mejora de competencias que justifican el proyecto | — |
| `Producto` | Nombre del producto, puede relacionarse con el nombre del proyecto | — |
| `Entregables` | **Una primera aproximación de la EDT**, con los entregables más importantes | — |
| `Objetivos` | Lista de objetivos que permitan **medir después** si el proyecto tuvo éxito | — |
| `Límite` | Qué queda **fuera** del alcance | — |
| `Firma Autorizante` | La del **patrocinador** | — |

> Fijate en el ejemplo de autoridad: no dice "tiene autoridad sobre el proyecto", dice **hasta qué monto puede aprobar y a quién debe elevar por encima de eso**. Ese nivel de concreción es el que espera la cátedra.

**Contenido que el PMI atribuye al Acta de Constitución** (apunte T2, para redactar la justificación y el encuadre): requisitos que satisfacen necesidades y expectativas del cliente, patrocinador e interesados · necesidades de negocio y descripción de alto nivel · **finalidad o justificación** · director designado y **nivel de autoridad** · resumen del cronograma de **hitos** · influencias de los interesados · organizaciones funcionales y su participación · **asunciones** y **restricciones** (de la organización, ambientales y externas) · oportunidades de negocio que lo justifican, incluido el ROI · **presupuesto resumido**.

> **El Acta autoriza formalmente el proyecto y confiere al Director la autoridad para aplicar recursos de la organización.** Ese es su rol, no ser un resumen del proyecto.

**Ejemplo resuelto de cátedra** (caso Centro de Servicios), para calibrar el nivel de detalle:

| Campo | Resolución modelo |
|---|---|
| Justificación | Centralizar y profesionalizar la Gestión de Incidentes, mejorando trazabilidad, priorización, cumplimiento de SLA y capacidad de gestión |
| Producto | Centro de Servicios operativo soportado por una herramienta ITSM configurada e integrada |
| Entregables | Requerimientos; solución seleccionada; herramienta configurada; taxonomías y SLA; integraciones; reportes; documentación; capacitación; puesta en producción |
| Objetivos | Los tres objetivos cuantificables definidos en el punto de objetivos |
| Límites | No incluye la implementación completa de Gestión de Problemas, Cambios ni el rediseño integral de la infraestructura de TI |
| Designación | Director/Líder de Proyecto designado por la organización |
| Responsabilidad | Coordinar equipo, cronograma, recursos, proveedor, riesgos, comunicaciones y cumplimiento de entregables |
| Autoridad | Asignar trabajo dentro del equipo, coordinar con áreas y proveedor, validar entregables intermedios y **elevar cambios que afecten alcance, costo o plazo** |

##### 7. Del EDT al diagrama de Red y al Gantt

Flujo que exige la cátedra:

`Actividades + predecesoras + duraciones → Diagrama de Red → camino crítico → fechas → Gantt → asignación de recursos → aplanamiento`

- El **diagrama de Red** muestra dependencias y determina el **camino crítico**.
- El **Gantt** ubica las actividades en el tiempo.
- La **asignación de recursos** permite detectar sobrecarga.
- El **aplanamiento (nivelación)** modifica fechas o asignaciones para evitar que un mismo recurso tenga tareas incompatibles en simultáneo.

**Qué hay que informar sí o sí:** fecha o período estimado de inicio; duración total; camino crítico; actividades con holgura; cantidad de personas por perfil; conflictos de recursos detectados; ajustes realizados al cronograma.

> Consecuencia práctica: si el cronograma se planifica 100% secuencial no hay conflicto que aplanar y ese punto de la consigna se responde con "no se detectaron conflictos", que es la peor respuesta posible. **Hay que diseñar paralelismo real** para que aparezca sobreasignación genuina y se pueda mostrar el aplanamiento.

**Cómo se calcula el camino crítico (CPM).** Cuatro valores por actividad:

| Sigla | Nombre | Cálculo |
|---|---|---|
| ES | Early Start | Recorrido **hacia adelante**: el mayor EF de sus predecesoras (0 si no tiene) |
| EF | Early Finish | ES + duración |
| LF | Late Finish | Recorrido **hacia atrás**: el menor LS de sus sucesoras (= duración total si no tiene) |
| LS | Late Start | LF − duración |

`Holgura = LS − ES = LF − EF`. Holgura 0 → actividad **crítica**. El camino crítico es la cadena de actividades con holgura 0, y su longitud es la duración del proyecto.

> **La duración total no se obtiene sumando duraciones.** En el caso de cátedra las nueve actividades suman 62 h, pero el proyecto dura **39 h**, porque varias ramas corren en paralelo. Confundir esto es el error clásico.

**El aplanamiento va después del CPM, no antes.** La red y el Gantt se arman **sin restricción de recursos**; recién cuando se asignan personas concretas se detecta si un mismo recurso está al 100% en dos actividades simultáneas. Ahí se reordena, se extiende, se reasigna o se reduce dedicación — y **la duración real puede cambiar**. Las actividades con holgura son las primeras candidatas a correr, porque moverlas no estira el proyecto.

**Formas de diagramar la red** (apunte T3):

- **AON — Activity On Node** (diagramación por precedencias): actividades en cuadros, conectadas por flechas. Es la que usa la cátedra.
- **AOA — Activity On Arrow**: actividades en flechas, conectadas por nodos. Usa solo relaciones fin-inicio y puede requerir tareas **dummy** (sin duración) para poder controlar.

**Esquema del nodo que usa la cátedra** — seis casilleros:

```
┌─────────────────────────────────────────────┐
│ Inicio Temprano │ Duración │ Fin Temprano   │
│         Denominación de la tarea            │
│ Inicio Tardío │ Holgura Total │ Holgura     │
│               │               │ Libre │ Fin │
│                                       │Tardío│
└─────────────────────────────────────────────┘
```

> El apunte remite explícitamente al **apunte de Investigación Operativa — CPM/PERT** como anexo. Si hace falta profundizar el cálculo, está en IO.

**El camino crítico** es: la secuencia de actividades críticas · el **más largo** de todos los caminos · el camino con holgura total cero (o mínima). **Puede haber más de uno**, lo que aumenta el riesgo de demora. Para acortar el proyecto hay que tocar las actividades del camino crítico; puede ser útil **reasignar recursos de una actividad no crítica a una crítica**.

**Cómo se aplana, paso a paso** (método del apunte, con su ejemplo de 15 tareas y 23 días):

1. Del diagrama de Red se deriva el **Gantt**.
2. Debajo de cada barra se anota, día por día, **cuánto recurso de cada tipo** consume esa tarea (el ejemplo usa fracciones: 0,25 · 0,5 · 1 · 2).
3. Se suma cada columna → fila de **totales por día**.
4. Se grafica el **histograma de recursos** y se marca la línea de **disponibilidad**.
5. Donde el total supera la disponibilidad hay **sobreutilización**. Se nivela **ajustando la holgura de las tareas no críticas**, tratando de no modificar la duración del proyecto.

> **Advertencia del apunte:** *"el camino crítico no está definido solamente por los tiempos sino también por los recursos"*. Aplanar puede obligar a rearmar la red y **cambiar el camino crítico**.

**Si aun así no entra: reducir la duración sin reducir el alcance.** Los proyectos pueden estar limitados por tiempo (fechas prefijadas) o por recursos (recursos escasos); **cuando ambos están limitados, el proyecto no es factible**. Dos métodos:

| Método | Qué hace | Qué cuesta |
|---|---|---|
| **Fast tracking** | Actividades que normalmente irían en secuencia se realizan en paralelo | **Incrementa el riesgo** |
| **Crashing** | Análisis costo-tiempo para obtener la mayor reducción al menor costo, agregando recursos | **Incrementa el costo** |

##### 8. Recursos Humanos

Los perfiles **surgen de la solución y de la EDT**. No hay que armar una lista extensa de puestos porque "podrían participar".

| Perfil | Responsabilidades | Competencias | Cantidad | Dedicación |
|---|---|---|---|---|
| Project Manager | Coordinar alcance, tiempo, costo y comunicación | Liderazgo, planificación, negociación | 1 | Parcial, todo el proyecto |
| Analista funcional | Relevar y validar requerimientos | Análisis de procesos, documentación | 1 | Inicio y validaciones |
| Especialista técnico | Configurar o desarrollar la solución | Tecnología elegida e integraciones | 1–2 | Desarrollo |
| Tester | Diseñar y ejecutar pruebas | Testing funcional y no funcional | 1 | Etapa de pruebas |
| Capacitador | Preparar materiales y capacitar | Comunicación y conocimiento funcional | 1 | Implementación |

> "Perfil requerido" no significa una persona exclusiva. Una persona puede cubrir más de un rol, **pero hay que justificarlo y reflejar su disponibilidad en el Gantt**.

##### 9. Higiene y Seguridad Laboral

La consigna pide un **layout real de los sectores afectados en el proceso crítico** y las medidas preventivas para las personas de esos sectores. Ojo con la letra: dice *"sector/es involucrados en el proceso crítico afectado"*, no "sectores donde se ejecuta el proyecto".

**No alcanza** con listar silla ergonómica, pausas activas y matafuegos. Hay que encadenar:

`sector → personas expuestas → riesgo → medida preventiva → representación en el layout`

| Tipo de proyecto | Qué mirar |
|---|---|
| Administrativos / digitales | Puestos y distancias, circulación, iluminación, ubicación de pantallas, cableado, salidas de emergencia, ventilación, ruido, ergonomía, fatiga visual, pausas, riesgos psicosociales |
| Industriales / logísticos / de campo | Circulación de peatones y vehículos, señalización, trabajos eléctricos, trabajo en altura, instalación de sensores, zonas restringidas, EPP, bloqueo de energía (LOTO), emergencias y evacuación |

Formato de tabla sugerido por la cátedra:

| Sector | Riesgo | Personas expuestas | Medida |
|---|---|---|---|
| Oficina de soporte | Fatiga visual y mala postura | Operadores | Monitor regulable, silla ergonómica y pausas |
| Sala técnica | Riesgo eléctrico | Infraestructura | Acceso restringido, señalización y procedimiento seguro |
| Zona operativa | Circulación de vehículos | Técnicos | Senderos, chaleco y coordinación con operaciones |

##### 10. Adquisiciones, RFI y RFP

| Activo o servicio | Cantidad | Características mínimas | Forma de adquisición | Justificación |
|---|---|---|---|---|
| Licencias de plataforma | 50 | SSO, auditoría, SLA, integración API | SaaS anual | Reduce tiempo de implementación |
| Servicio cloud | Según consumo | Escalabilidad, backup, región y cifrado | Pago por uso | Demanda variable |
| Dispositivos de prueba | 3 | Diferentes sistemas y capacidades | Compra | Necesarios para validación |
| Consultoría especializada | 120 horas | Experiencia comprobable | Outsourcing | Competencia no disponible internamente |

**RFI (Request for Information)** — se usa cuando todavía hay que explorar: qué ofrece el mercado, qué tecnologías hay disponibles, qué proveedores existen, rangos de precio, capacidades generales.

**RFP (Request for Proposal)** — se usa cuando los requerimientos ya están definidos y se quiere recibir una propuesta: técnica, económica, cronograma, equipo, SLA y condiciones contractuales.

> No alcanza con definir las siglas: hay que explicar **en qué adquisición concreta del propio proyecto se usaría cada uno**.

**Qué se evalúa de un proveedor en un RFP** (caso integral de cátedra):

| Criterio | Qué evaluar |
|---|---|
| Capacidad técnica | Cobertura de requerimientos, integraciones, escalabilidad y seguridad |
| Experiencia | Implementaciones similares y referencias |
| Soporte | Horarios, tiempos de respuesta, canales, SLA y escalamiento |
| Implementación | Metodología, plazo, migración, configuración y pruebas |
| Capacitación | Plan de formación para administradores, operadores y usuarios |
| Costo total | Licencias, servicios, infraestructura, soporte, renovaciones y costos asociados |

**Variables del TCO** — licencias o suscripciones · servicios de implementación y parametrización · integraciones y migración de datos · infraestructura o consumo cloud · capacitación · soporte y mantenimiento · actualizaciones y renovaciones · administración interna de la herramienta · escalabilidad y crecimiento · **costos de salida o cambio de proveedor**.

> El TCO **no** lo exige la Etapa 3 (pide "variables de costo" y "forma de adquisición"), pero la propia cátedra dice que puede enriquecerla. Para comparar desarrollo interno contra SaaS es la herramienta correcta.

##### 11. Costos

Variables mínimas a considerar: horas por perfil; valor hora; licencias; hardware; servicios cloud; proveedores; capacitación; implementación; mantenimiento inicial; viáticos; costos indirectos; reserva de contingencia.

```
Costo RRHH  = cantidad de horas × valor hora por perfil
Costo total = RRHH + adquisiciones + servicios + indirectos + contingencia
```

**BAC (Budget At Completion).** El presupuesto total sale de asignar presupuesto a **cada actividad de la EDT** y sumarlos. En el caso de cátedra las nueve actividades dan **BAC = $3.700**.

**Los beneficios hay que monetizarlos.** Se conectan con los objetivos y se traducen a plata o a costos evitados.

| Beneficio | Cómo se mide |
|---|---|
| Menor FRT (First Response Time) y MTTR | Horas de soporte ahorradas, menor indisponibilidad, menor costo por incidente |
| Mayor cumplimiento de SLA | Menos penalizaciones, reclamos y escalaciones |
| Mayor trazabilidad | Menos tiempo administrativo, mejor capacidad de auditoría |
| Menos incidentes perdidos o repetidos | Reducción de reprocesos y duplicaciones |
| Mejor información de gestión | Decisiones basadas en tendencias, categorías y volumen |

> **Monetización — ejemplo de cátedra:** si el seguimiento manual consume 150 horas mensuales y con la solución baja a 80, se liberan **70 horas mensuales**. Esas horas se valorizan al costo/hora y se comparan contra la inversión y los costos recurrentes. Ese es el formato que espera la factibilidad económica.

**La fórmula de base del apunte T4:** `Beneficios = Ingresos + Costos evitados`. El procedimiento: determinar y calcular los costos · determinar, listar y definir los beneficios · identificar las fuentes de información · **determinar un indicador de costo-beneficio**.

##### 11 bis. Técnicas de evaluación de inversiones

| # | Técnica | Qué mide | Ventajas | Desventajas |
|---|---|---|---|---|
| 1 | **TR** — Tiempo de Recuperación | Cuántos años hasta que `Beneficios = Inversión` | Fácil de calcular y comprender | No considera beneficios posteriores al recupero, ni el momento en que se producen los flujos, ni el rendimiento de la inversión |
| 2 | **TPR** — Tasa Promedio de Retorno | `Beneficio Promedio Anual ÷ Inversión Total`, con BPA = Beneficio Total ÷ Vida Útil | Fácil, y **sí considera la vida útil** | No considera el momento de los flujos ni el valor del dinero en el tiempo |
| 3 | **VAN** — Valor Actual Neto | Valor neto de dinero que se espera obtener. **La inversión conviene si VAN > 0** | Considera el valor del dinero en el tiempo y la vida útil | Depende de elegir bien la **tasa de descuento**, y del costo de capital variable |
| 4 | **TIR** — Tasa Interna de Retorno | La tasa a la que el VAN se hace cero | — | — |

**Valor del dinero en el tiempo** — el dinero vale más hoy que el mismo monto en el futuro, por su potencial de inversión, la inflación y el riesgo.

- **Valor Futuro (VF)**: cuánto valdrá en el futuro una suma que tenemos hoy, *capitalizando* a una tasa de interés.
- **Valor Actual (VA)**: cuánto vale hoy una suma que recibiremos en el futuro, *descontando* a una tasa.
- Ejemplo del apunte: al 10% anual, **$1 dentro de 4 años representa $0,68 hoy**. Con tasa 0%, VF = VA.

> El apunte aclara: **no confundir la tasa de descuento con la tasa de inflación**.

> **Para la Etapa 3.** La consigna pide "variables para calcular los costos" y factibilidad económica — no exige VAN ni TIR. Con **SaaS** (costo recurrente por usuario, sin inversión inicial fuerte) el indicador que mejor muestra el peso real es el **TCO a 3 años**; el TR y el VAN sirven para contrastar el ahorro de horas contra la licencia acumulada.

##### 12. Análisis de Factibilidad

**Técnica** — disponibilidad de tecnología, compatibilidad, infraestructura existente, conocimientos del equipo, capacidad, seguridad, integración, soporte, riesgos técnicos.

**Económica** — inversión inicial, costos operativos, costos evitados, ahorros, mejoras de productividad, beneficios cuantificables, plazo de recuperación cuando sea posible.

> **No sirve escribir** "es económicamente factible porque traerá beneficios". Hay que mostrar, aunque sea estimado: *el proyecto cuesta X; reduce Y horas mensuales; el valor de esas horas es Z; además evita determinados costos o pérdidas.*

Según el nivel de la ejercitación pueden usarse indicadores: **plazo de recuperación (TPR), VAN o TIR**.

**Legal** — qué revisar, según el caso integral de cátedra: protección de datos, confidencialidad, licenciamiento, condiciones contractuales, responsabilidades del proveedor, **ubicación y almacenamiento de la información** cuando corresponda, y políticas internas de seguridad y auditoría.

Para el caso Personal: Ley 25.326 (datos personales), Ley 27.078 Argentina Digital, normativa ENACOM de calidad de servicio, Ley 24.240 de Defensa del Consumidor, y marco contractual con contratistas. *(La lista sale del punto 7 de la Etapa 1.)*

> **Cómo cierra la conclusión (modelo de cátedra):** *"La alternativa X resulta viable si el RFI/RFP confirma que existe una solución que satisface los requerimientos técnicos y de seguridad dentro del presupuesto y plazo disponibles. La aprobación definitiva depende del análisis de TCO, beneficios, restricciones y condiciones contractuales."* — **no se declara factible antes de verificar esas condiciones.**

##### 13. La ejercitación de U5 vs. la Etapa 3 del TPI

La cátedra tiene **dos consignas distintas** sobre esta unidad, y no piden lo mismo.

**La ejercitación de U5** (`ASI-5_Ejercitacion1 - Proyectos de TI.docx`) está organizada por **áreas de conocimiento del PMI**:

1. **Gestión del Alcance** — objetivos cuantificables · alternativas y selección · ciclo de vida, fases, actividades y EDT/WBS · Acta de Proyecto.
2. **Gestión de Adquisiciones** — lista de requerimientos · **ejecutar un RFI** sobre las soluciones existentes · descripción de una propuesta de implementación y su impacto en el proceso · características a evaluar de proveedores en un RFP y **consulta de presupuesto a al menos 3 proveedores** · variables del **TCO**.
3. **Gestión de Tiempos y asignación de recursos** — a partir de la EDT y **con una herramienta de planificación**, estimar la duración · Red de Tareas y Gantt · perfiles y competencias.
4. **Gestión de Costos** — costos del proyecto e identificación de los que no se detectaron antes (alquileres, viajes, conectividad) · **Presupuesto del Proyecto** · **estudio de beneficios** y sus variables · factibilidad técnica, económica y legal.

**Capacidades del RA3** que declara la ejercitación: identificar objetivos · analizar y justificar soluciones (desarrollo propio o contratación externa) · **investigar mecanismos de financiación** · analizar viabilidad y factibilidad económica, técnica y legal **y evaluar el impacto social y ambiental** · realizar el plan de proyecto.

**Qué pide cada una** — tabla de la propia cátedra:

| Tema | Ejercitación U5 | TP Integrador Etapa 3 |
|---|---|---|
| Proyecto TI, objetivos, alternativas y selección | Sí | Sí |
| Ciclo de vida, fases y EDT/WBS | Sí | Sí |
| Acta de Proyecto | Sí | Sí |
| **RFI completo y relevamiento de soluciones** | Sí | **No** — solo explicar RFI vs. RFP y cuándo usar cada uno |
| **RFP y 3 cotizaciones** | Sí | **No** |
| **TCO detallado** | Sí | Pide variables de costo y forma de adquisición; el TCO **puede enriquecer** |
| Red de tareas y Gantt | Sí | Sí |
| Perfiles y competencias | Sí | Sí |
| Aplanamiento de recursos | Relacionado con gestión de tiempos | **Sí, expresamente** |
| **Higiene y Seguridad / Layout** | **No** | **Sí** |
| Factibilidad técnica, económica y legal | Sí | Sí |

> **Para entregar el TP se sigue la consigna de la Etapa 3.** La ejercitación de U5 es más ancha y cubre la unidad completa: la cátedra avisa explícitamente que **puede aparecer en evaluación**. Los tres temas que están en U5 y no en la Etapa 3 — RFI ejecutado, 3 cotizaciones y TCO — son los candidatos naturales a pregunta de parcial.

#### Ejercicios resueltos tipo

**Caso integral de cátedra — Centro de Servicios y Gestión de Incidentes.** Única resolución completa de la unidad. Recorre la cadena entera: problema → proyecto → objetivos → alternativas → ciclo de vida → EDT → adquisiciones → tiempos → costos → beneficios → factibilidad.

**Problema.** La organización gestiona incidentes con canales y herramientas dispersas: no hay trazabilidad, priorización, seguimiento de SLA ni escalamiento. *El problema no es la falta de una herramienta, es la falta de un proceso centralizado, medible y controlable.*

**Proyecto.** Implementar un Centro de Servicios soportado por una herramienta centralizada de Gestión de Incidentes que permita registrar, categorizar, priorizar, asignar, escalar y hacer seguimiento, con indicadores de desempeño y trazabilidad. *(Ejemplo de la cátedra: compañía de 3.000 empleados donde hoy cada usuario manda WhatsApp o llama directo a "Fulano de Sistemas"; el proyecto crea un **único punto de contacto**.)*

> La formulación **no arranca por una marca ni un producto**. Primero qué problema se resuelve y qué resultado se espera; después cómo implementarlo.

**Objetivos** — resultado + métrica + meta + plazo + criterio de verificación:

| # | Objetivo | Criterio de verificación |
|---|---|---|
| 1 | Reducir 30% el tiempo promedio de primera respuesta en los primeros 6 meses post-producción | Tiempo promedio antes vs. después |
| 2 | Resolver ≥90% de los incidentes dentro del SLA acordado en los primeros 6 meses de operación | % de incidentes resueltos dentro del SLA |
| 3 | Alcanzar 95% de incidentes registrados y trazables en la herramienta dentro de los primeros 3 meses | Incidentes registrados / incidentes totales estimados |

> "Mejorar la Gestión de Incidentes" no sirve como objetivo porque no permite saber cuándo se alcanzó.

**Ciclo de vida: híbrido con implementación incremental.** La primera parte es predecible (relevamiento, requerimientos, consulta al mercado, RFP, selección de proveedor); la configuración y puesta en marcha conviene validarla de a poco con soporte y usuarios antes del despliegue completo. *No alcanza con decir "es incremental porque trabaja por incrementos": hay que explicar qué característica del proyecto lo hace conveniente.*

**Fases (6):** 1. Inicio y definición · 2. Selección de solución · 3. Diseño y configuración · 4. Integración · 5. Piloto y validación · 6. Despliegue y cierre.

**EDT (7 paquetes):** 1. Inicio y requerimientos · 2. Selección de solución · 3. Diseño del proceso · 4. Configuración e integración · 5. Validación · 6. Implementación · 7. Cierre.

> **Relación clave que enuncia la cátedra:** `EDT → actividades → perfiles y recursos → duraciones → dependencias → Red/Gantt → esfuerzo/horas → costos`. **Si la EDT es pobre, todo lo que viene después queda débil.**

**Tiempos y costos — el ejercicio numérico completo.** Unidad: horas. Valores didácticos, no de mercado.

| ID | Actividad | Pred. | Dur. (h) | Ppto. ($) | ES | EF | LS | LF | Holgura | Crítica |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Análisis de requisitos según la infraestructura de servicios | — | 12 | 600 | 0 | 12 | 0 | 12 | 0 | **Sí** |
| 2 | Relevamiento de propuestas y soluciones del mercado | 1 | 4 | 200 | 12 | 16 | 12 | 16 | 0 | **Sí** |
| 3 | Desarrollo de los RFP para selección de proveedores | 1 | 8 | 400 | 12 | 20 | 13 | 21 | 1 | No |
| 4 | Selección de proveedor según la matriz de comparación | 2 | 5 | 300 | 16 | 21 | 16 | 21 | 0 | **Sí** |
| 5 | Implementación del Centro de Servicios / mejora de procesos | 3, 4 | 7 | 600 | 21 | 28 | 21 | 28 | 0 | **Sí** |
| 6 | Definición de taxonomías para la Gestión de Incidentes | 1 | 8 | 500 | 12 | 20 | 18 | 26 | 6 | No |
| 7 | Relevamiento de infraestructura y definición de herramientas | 5, 6 | 5 | 400 | 28 | 33 | 28 | 33 | 0 | **Sí** |
| 8 | Definición de políticas de seguridad y auditoría de datos | 6 | 7 | 400 | 20 | 27 | 26 | 33 | 6 | No |
| 9 | Implementación y alineación de las herramientas | 7, 8 | 6 | 300 | 33 | 39 | 33 | 39 | 0 | **Sí** |

**Red de precedencias.** Inicio → 1. Desde la actividad 1 se abren tres ramas: `1→2→4`, `1→3` y `1→6`. Las actividades 3 y 4 habilitan la 5; las 5 y 6 habilitan la 7; la 6 habilita también la 8; finalmente 7 y 8 habilitan la 9.

**Resultados:**

```
Duración del proyecto : 39 h   (la suma de las duraciones da 62 h — no es eso)
Camino crítico        : 1 → 2 → 4 → 5 → 7 → 9
Holguras              : act. 3 = 1 h · act. 6 = 6 h · act. 8 = 6 h
BAC                   : $3.700
```

En el Gantt: **rojo** = actividad crítica (holgura 0), **azul** = no crítica.

**Perfiles del caso (7):** Líder/Director de Proyecto · Analista ITSM/funcional · Administrador-configurador de la herramienta · Especialista de infraestructura · Especialista de seguridad · Responsable de Service Desk · Capacitador / gestión del cambio.

> **Advertencia sobre el Gantt del caso:** representa la lógica de precedencias **sin restricciones de recursos**. Al asignar personas concretas hay que verificar sobreasignaciones y aplanar — y la duración real puede cambiar.

> **Aviso de la propia cátedra sobre este caso:** *"No reemplaza la consigna específica del TP Integrador Etapa 3: para el TP, se deben seguir exactamente los puntos exigidos en la consigna."* Sirve para entender la unidad y para evaluación.

#### Dudas / pendientes

- ~~Falta la plantilla del Acta de Proyecto.~~ **Conseguida el 2026-08-19** — `fuentes/ASI/Ejercitación/ASI-5-T1-Proyectos_AnexoI_ActaProyecto.doc`. Detalle menor: la consigna del TPI dice que está en el **e-Group** y la ejercitación de U5 dice **campus**; es el mismo Anexo I.
- ~~Falta el apunte teórico de cátedra de la unidad.~~ **Conseguidos los cinco capítulos el 2026-08-19** (T1 a T5). T1, T2 y T3 tienen apunte en texto; T4 y T5 solo diapositivas.
- ~~La cátedra llama Unidad 5 a esta unidad.~~ **Renumerada el 2026-08-19** según el Programa Analítico: esta es la Unidad 5. La wiki ahora sigue la numeración oficial.
- **T5 Adquisiciones está poco desarrollado acá.** Las diapositivas cubren el proceso de abastecimiento, definición de requerimientos, consulta a pares/expertos/proveedores y etapas del proceso; se ingirió pero no se volcó en detalle. Si el punto 8 y 9 de la Etapa 3 lo piden, hay que volver ahí.
- El apunte T3 remite a un **anexo de Investigación Operativa (CPM-PERT)** para el cálculo detallado de la red. Está en `fuentes/4º AÑO/Investigación Operativa/`, no se copió.
- La ejercitación de U5 declara dos temas del RA3 que **no aparecen en la consigna de la Etapa 3**: **mecanismos de financiación** de proyectos de base tecnológica e **impacto social y ambiental** de la solución. Pueden entrar en evaluación.
- La consigna numera los puntos de forma irregular: la sección "Higiene y Seguridad Laboral" reinicia en 1 y 2, y luego "Adquisiciones" sigue en 6. **Al armar el índice del documento, mantener el orden de la consigna pero numerar corrido.**
- El punto 3 dice **"Validar con el docente"** la alternativa seleccionada. Hay que hacerlo antes de desarrollar el resto.

#### Fuentes

- `fuentes/ASI/ASI26_TPIntegrador_Etapa3 - Proyecto de TI.md` — consigna oficial del TPI.
- `fuentes/ASI/TPIntegrador - Etapa 3 - Practica Sugerencias.md` — sugerencias de cátedra, clase 28/07/2026.
- `fuentes/ASI/Ejercitación/ASI-5_Ejercitacion1 - Proyectos de TI.docx` — ejercitación de la Unidad 5 (RA3 y las 4 áreas PMI).
- `fuentes/ASI/Ejercitación/ASI-5-T1-Proyectos_AnexoI_ActaProyecto.doc` — **plantilla oficial del Acta de Proyecto**. Formato `.doc` legacy: markitdown no lo soporta, se convirtió con `textutil -convert txt`.
- `fuentes/ASI/Ejercitación/ASI26_U5_Caso_Integral_Resolucion_Centro_Servicios.docx` — caso integral resuelto.
- `fuentes/ASI/Ejercitación/ASI26_U5_Caso_Integral_Gantt_Centro_Servicios.xlsx` — Gantt + CPM + presupuestos del caso.
- `fuentes/ASI/Campus/ASI-Unidad5_Adm_Recursos_en_ProyectosIT/` — los cinco capítulos de la unidad (19/08/2026):
  - `ASI-5-T1-Proyectos_APUNTE.V1.0.pdf` + `_DIAP.V2.2.pdf` — qué es un proyecto, tipos, objetivos, ciclos de vida, organización, PMI.
  - `ASI-5-T2-Integración_Alcance_Cierre_APUNTE.V1.0.pdf` + `_DIAP.V2.0.pdf` — grupos de procesos, Acta de Constitución, enunciado del alcance, control de cambios, cierre, EDT. **Trae el Anexo I con la plantilla del Acta anotada y el ejemplo ESABAL.**
  - `ASI-5-T3-Tiempos_APUNTE.V1.0.pdf` + `_DIAP.V2.0.pdf` — estimación de esfuerzo (modelos, juicio de expertos, Delphi), diagrama de Red, CPM, histograma de recursos, fast tracking y crashing, control y seguimiento.
  - `ASI-5-T4-Costos_DIAP.V2.2.pdf` — justificación económica, TR, TPR, VAN, TIR. *(Solo diapositivas, no hay apunte.)*
  - `ASI-5-T5-Adquisiciones_DIAP.V2.0.pdf` — proceso de abastecimiento y definición de requerimientos. *(Solo diapositivas.)*
  - `ASI-5-T3-Ejemplo Costos_GANTT.xlsx` · `ASI-5-T4-Método del valor ganado - EJERCICIO.docx` y `- RESOLUCION.xlsx` · `ASI-5-T1-Proyectos_Ejemplo.docx`.

---

### Unidad 6 — Emprendedorismo

> **Unidad no desarrollada.** No toca la Etapa 3 del TPI. Material identificado en el campus pero **no copiado a `fuentes/ASI/`** — se copia cuando haga falta.

#### Conceptos clave

Contenidos según el Programa Analítico: proyectos innovadores y emprendimientos de base científica y tecnológica · tendencias actuales y transformación digital · ecosistemas emprendedores · herramientas de desarrollo y modelado de proyectos innovadores (**Design Thinking**, **Canvas**) · gestión de emprendimientos tecnológicos, **método Lean Start-up**.

#### Dudas / pendientes

- Sin desarrollar. Material disponible en el campus: cinco diapositivas (`ASI-6-C1 Desarrollo Emprendedor` · `C2 Gestión del Negocio` · `C3 Producto y Clientes` · `C4 Funcionamiento del Emprendimiento` · `C5 Rentabilidad`) más `Business Model Canvas` en dos versiones (español y Strategyzer).
- Bibliografía del programa para esta unidad: Ries, *El método Lean Startup* · Osterwalder y Pigneur, *Business Model Generation* · Lockwood, *Design Thinking* · Orzen y Paider, *The Lean IT field guide*.

---

### TP Integrador — Personal (Telecom) / Proceso de instalación de fibra óptica

#### Conceptos clave

| Dato | Valor |
|---|---|
| Comisión | 403 |
| Grupo | 310 |
| Integrantes | 53535 Bonadeo Juan Cruz · 52674 Casermeiro Gonzalo · 53543 De la Rosa Valentín Yael · 53215 Lezcano Diego · 52688 Lurati Ignacio |
| Ciudad de análisis | Rosario (evaluada como "en transición" hacia ciudad inteligente, con el modelo Smart City Wheel de Boyd Cohen) |
| Organización elegida | **Personal (Telecom Argentina)** — empresa de telecomunicaciones |
| Proceso crítico elegido | **Instalación de internet con fibra óptica** |
| Etapa 1 | Entregada 23/04/2026 · corregida por cátedra 19/05/2026 · ajustada por el grupo 21/05/2026 (v3) |
| Etapa 2 | Entregada 18/05/2026 (v1). **La tabla de versiones no registra corrección posterior — corregir antes de la Etapa 3.** |
| Etapa 3 | En curso. Consigna y sugerencias recibidas 28–29/07/2026. Alcance cerrado por el grupo el 10/08/2026 (candidato B, alcance B medio). **Punto 3 validado por el docente el 23/08/2026**: proyecto aprobado, modo de construcción SaaS FSM configurable, y alternativas redefinidas como proyectos distintos. Puntos 1 a 4 escritos; 5 a 12 pendientes |

##### Formato del documento de entrega (usar el mismo en la Etapa 3)

Encabezado fijo, en este orden:

1. `Universidad Tecnológica Nacional`
2. `CÁTEDRA` → `Administración de Sistemas de Información - 4º Año Ingeniería en Sistemas de Información`
3. `Ejercitación Unidad Nº: N  [título de la unidad]` + subtítulo en cursiva
4. `Comisión Nº: 403` · `Grupo Nº: 310`
5. `INTEGRANTES` — lista con *Legajo, Apellido y Nombres, Email*
6. `VERSIÓN DEL DOCUMENTO` — tabla `Mod | Fecha | Autor | Descripción`. El autor es `Grupo N310` para las entregas y `CC` para las correcciones de cátedra.
7. Índice con los títulos de los puntos de la consigna y su número de página.
8. Desarrollo: **un título por punto de la consigna**, con el enunciado del punto como título (en negrita las palabras clave del enunciado).

#### Desarrollo

##### Etapa 1 — Análisis para la implementación de soluciones de TI (entregada y corregida)

**Rosario como ciudad inteligente.** Conclusión del grupo: *está en transición, no lo es de forma plena*. Fundamento: cumple criterios en las seis dimensiones del Smart City Wheel (Government: CIO, +300 trámites online, datos abiertos, IBM Smarter Cities Challenge 2012 · Mobility: 150 km de fibra óptica municipal, semáforos con ondas verdes, SUBE/NFC/QR, Mi Bici Tu Bici · Environment: Plan de Acción Climática 2030, telegestión de alumbrado LED, economía circular por ordenanza · Economy: Polo Tecnológico Rosario (Zona i), Personal, Globant, Mercado Pago · People: UNR y UTN FRRo, alfabetización digital · Living: CIO con monitoreo 24/7), pero **falta una estrategia smart city unificada y financiamiento para escalar**.

**Empresas identificadas que aportan valor:** Personal (Telecom), YPF Luz, Globant Government & Social Impact Studio, SUBE / Nación Servicios, Mercado Pago, Google, Microsoft, PedidosYa, Uber, Amazon, Mercado Libre. Se transcribieron visión/misión/valores de cinco: Personal, YPF Luz, Globant, SUBE y Mercado Pago.

**Organización seleccionada:** Personal (Telecom Argentina).

- *Visión (área de infraestructura de fibra):* ser líderes en el desarrollo de infraestructura digital en Argentina, expandiendo redes de fibra óptica de alta calidad.
- *Misión:* diseñar, desplegar y mantener redes de fibra óptica eficientes y escalables, con conectividad de alta velocidad y calidad.
- *Valores:* innovación tecnológica, calidad de servicio, orientación al cliente, trabajo en equipo entre áreas técnicas/comerciales/sistemas, sustentabilidad y ética y transparencia.

**Normas y regulaciones aplicables** (base para la factibilidad legal de la Etapa 3):

| Norma | Qué regula |
|---|---|
| Ley 27.078 — Argentina Digital | Servicios de telecomunicaciones, derechos de usuarios, obligaciones de las empresas |
| Regulación ENACOM | Licencias, calidad del servicio, administración del espectro radioeléctrico |
| Normativa de espectro radioeléctrico | Asignación de frecuencias 4G/5G, obligaciones de cobertura y calidad |
| Ley 25.326 — Protección de Datos Personales | Tratamiento y protección de datos de usuarios |
| Ley 24.240 — Defensa del Consumidor | Información clara, baja del servicio, reclamos |
| Ley 25.891 — Servicios de Comunicaciones Móviles | Identificación de usuarios, registro de SIM, contratación y baja |
| Normativas de calidad de servicio (ENACOM) | Velocidad, disponibilidad, tiempos de respuesta |

**Metas y objetivos definidos** (proceso: instalación de internet con fibra óptica):

| Plano | Metas | Objetivos |
|---|---|---|
| **Negocio** | Expandir la cobertura de red de fibra óptica aumentando la base de clientes · Mejorar el tiempo de instalación · Aumentar la cantidad de turnos para instalación · Mejorar la calidad de servicio | Llegar con fibra óptica a 3 nuevas localidades en 2026 · Recuperar en 2 años los clientes perdidos en 2020 por la pandemia · Aumentar el rendimiento de los técnicos un 5% (instalaciones/horas de trabajo) para 2026 |
| **TI** | Expandir red de fibra en barrios del Gran Rosario · Implementar un sistema de recuperación de clientes dados de baja · Implementar un sistema de feedback post-instalación · Asignación optimizada de técnicos | Plan de despliegue en ≥3 barrios del Gran Rosario, cobertura ≥60% de hogares en 18 meses, ≥100 Mbps simétricos, cumpliendo ENACOM y normativa municipal · Plataforma de gestión de clientes con campañas digitales automatizadas para recupero, 2 años · **App de gestión para técnicos de campo: digitalizar y optimizar las OT, mejorar el seguimiento de instalaciones y aumentar la productividad operativa 5% para 2026** |

> ⚠ **Defecto de maquetado en el documento entregado:** el tercer objetivo de TI (la app de campo) quedó como **título de nivel 1** suelto entre los puntos 9 y 10, en vez de como ítem de la lista "Objetivos de TI". Es justamente el objetivo del que se desprende el proyecto de la Etapa 3. **Corregir antes de entregar.**

**Descripción del proceso — Instalación de fibra óptica**

| Entradas | Actividades | Salidas |
|---|---|---|
| Solicitud del cliente (presencial, web o telefónica) · Datos del cliente y dirección · Disponibilidad de infraestructura en la zona · Stock de equipos (router, cable de fibra) · Agenda de técnicos disponibles | 1. Recepción y registro de la solicitud · 2. Verificación de cobertura y viabilidad técnica · 3. Asignación de turno y técnico instalador · 4. Visita técnica al domicilio · 5. Tendido del cable desde el nodo hasta el domicilio · 6. Instalación y configuración del ONT/router · 7. Prueba de señal y verificación de conectividad · 8. Firma de conformidad del cliente · 9. Cierre y registro del servicio activado | Servicio de internet por fibra activo · Contrato firmado / conformidad · Registro de instalación en el sistema · Reporte técnico de la instalación |


---


##### Estado de las fuentes gráficas (ASI — TP Integrador, Etapa 1)

| Archivo | Contenido real | Coincide con lo esperado |
|---|---|---|
| `fuentes/ASI/modeloPersonal.png` | Diagrama BPMN del proceso **"Instalación de Fibra Óptica"** (pool único, 3 lanes), renderizado en Bizagi Modeler. **NO es un organigrama.** | No |
| `fuentes/ASI/fibraOpticaBPMN.png` | Diagrama BPMN del proceso **"Instalación de Fibra Óptica"**, misma estructura que el anterior con nombres de tareas corregidos. | Sí |

Ambos archivos son **el mismo diagrama en dos versiones**, no un organigrama y un BPMN. Los llamo **Versión A** (`modeloPersonal.png`) y **Versión B** (`fibraOpticaBPMN.png`). Por el estilo de los nombres de tarea, B es posterior a A *(inferencia)*.

##### 1. Organigrama de Personal (Telecom) — FALTANTE

No hay ningún organigrama en los archivos provistos. No hay jerarquía, gerencias ni áreas que transcribir: **ninguna de las dos imágenes contiene cajas de estructura organizacional, ni líneas de dependencia, ni nombres de gerencias**. Lo único parecido a "estructura organizacional" en el material son los tres lanes del BPMN (Cliente, Sistema IT, Técnico), que son roles de proceso, no unidades del organigrama.

Acción requerida: subir el archivo correcto a `fuentes/ASI/`. El nombre `modeloPersonal.png` sugiere que se pisó o se exportó mal desde Bizagi (probablemente se exportó dos veces el mismo diagrama) *(inferencia)*.

##### 2. BPMN "Instalación de Fibra Óptica" — Pools, lanes y actores

- **Pool (único):** `Instalación de Fibra Óptica`
- **Lanes (3), de arriba hacia abajo:**

| Orden | Lane | Actor / rol | Qué hace en el diagrama |
|---|---|---|---|
| 1 | **Cliente** | Solicitante externo del servicio | Origina la solicitud, recibe la notificación de rechazo, firma la conformidad final |
| 2 | **Sistema IT** | Sistema/back office de la empresa | Verifica cobertura, decide, asigna turno y técnico, cierra la instalación |
| 3 | **Técnico** | Técnico instalador de campo | Conecta la fibra, instala y configura el módem, verifica y decide si la instalación fue exitosa |

**Inventario de elementos**

| Tipo BPMN | Nombre (Versión B) | Nombre (Versión A) | Lane |
|---|---|---|---|
| Evento de inicio (none) | *(sin nombre)* | *(sin nombre)* | Cliente |
| Tarea | Solicitar instalación de servicio | ídem | Cliente |
| Tarea | Verificar cobertura en la zona | ídem | Sistema IT |
| Gateway exclusivo (divergente) | ¿Hay cobertura en la zona? | ídem | Sistema IT |
| Tarea | Notificar sin cobertura | ídem | Cliente |
| Evento de fin | Rechazado | Rechazado | Cliente |
| Tarea | Asignar turno y técnico instalador | ídem | Sistema IT |
| Evento intermedio de tiempo (timer) | El día del turno | El día del turno | **Técnico** (en A está en **Sistema IT**) |
| Tarea | Conectar cable de fibra desde el nodo. | Conexión de cable de fibra desde el nodo. | Técnico |
| Tarea | Instalar y configurar el modem | Instalación y configuración del modem | Técnico |
| Tarea | Verificar señal y conectividad. | Verificación de conectividad. | Técnico |
| Gateway exclusivo (divergente) | ¿Instalación exitosa? | ídem | Técnico |
| Tarea | Cerrar instalacion *(sin tilde en el original)* | ídem | Sistema IT |
| Tarea | Firmar conformidad | ídem | Cliente |
| Evento de fin | Fin | Fin. Servicio Activo | Cliente |

Totales: 1 pool, 3 lanes, 1 evento de inicio, 1 evento intermedio (timer), 2 eventos de fin, 8 tareas, 2 gateways exclusivos, 0 data objects, 0 message flows, 0 subprocesos, 0 eventos adjuntos (boundary).

##### 3. BPMN — Secuencia completa paso a paso

Camino principal y ramas, legible sin la imagen. Nombres según Versión B.

1. **[Cliente]** Evento de inicio (círculo simple, sin nombre) → dispara el proceso.
2. **[Cliente]** Tarea `Solicitar instalación de servicio`.
3. El flujo baja al lane **Sistema IT**.
4. **[Sistema IT]** Tarea `Verificar cobertura en la zona`.
5. **[Sistema IT]** Gateway exclusivo `¿Hay cobertura en la zona?` — dos salidas etiquetadas:
   - **5.a — Rama "No"** → el flujo sube al lane **Cliente**:
     1. **[Cliente]** Tarea `Notificar sin cobertura`.
     2. **[Cliente]** Evento de fin `Rechazado`. **Fin del proceso por esta rama.**
   - **5.b — Rama "Si"** *(escrito sin tilde en el original)* → continúa en Sistema IT, paso 6.
6. **[Sistema IT]** Tarea `Asignar turno y técnico instalador`.
7. El flujo baja al lane **Técnico** (en Versión A el timer queda en Sistema IT y recién después baja).
8. **[Técnico]** Evento intermedio de tiempo `El día del turno` → el proceso queda en espera hasta la fecha del turno pactado.
9. **[Técnico]** Tarea `Conectar cable de fibra desde el nodo.`
10. **[Técnico]** Tarea `Instalar y configurar el modem`. *(Esta tarea recibe dos flujos entrantes: el del paso 9 y el de retorno del paso 12.a — merge implícito, sin gateway de convergencia.)*
11. **[Técnico]** Tarea `Verificar señal y conectividad.`
12. **[Técnico]** Gateway exclusivo `¿Instalación exitosa?` — dos salidas etiquetadas:
    - **12.a — Rama "No"** → el flujo sale hacia arriba y **vuelve al paso 10** (`Instalar y configurar el modem`). Loop de reintento sin límite ni salida alternativa.
    - **12.b — Rama "Si"** → sube al lane **Sistema IT**, paso 13.
13. **[Sistema IT]** Tarea `Cerrar instalacion`.
14. El flujo sube al lane **Cliente**.
15. **[Cliente]** Tarea `Firmar conformidad`.
16. **[Cliente]** Evento de fin `Fin` (en Versión A: `Fin. Servicio Activo`). **Fin del proceso por el camino feliz.**

**Resumen de caminos posibles**

| # | Camino | Recorrido | Termina en |
|---|---|---|---|
| 1 | Sin cobertura | 1 → 2 → 4 → 5(No) → Notificar sin cobertura | `Rechazado` |
| 2 | Instalación exitosa al primer intento | 1 → 2 → 4 → 5(Si) → 6 → 8 → 9 → 10 → 11 → 12(Si) → 13 → 15 | `Fin / Servicio Activo` |
| 3 | Instalación con N reintentos | igual que 2 pero con el ciclo 10 → 11 → 12(No) repetido N veces | `Fin / Servicio Activo` |
| 4 | Instalación que nunca resulta exitosa | ciclo 10 → 11 → 12(No) infinito | **No termina** — no hay salida modelada |

##### 4. Diferencias entre las dos versiones

| Aspecto | Versión A (`modeloPersonal.png`) | Versión B (`fibraOpticaBPMN.png`) |
|---|---|---|
| Tarea 9 | `Conexión de cable de fibra desde el nodo.` (sustantivo) | `Conectar cable de fibra desde el nodo.` (infinitivo) |
| Tarea 10 | `Instalación y configuración del modem` (sustantivo) | `Instalar y configurar el modem` (infinitivo) |
| Tarea 11 | `Verificación de conectividad.` (sustantivo) | `Verificar señal y conectividad.` (infinitivo, alcance ampliado a "señal") |
| Ubicación del timer | Lane **Sistema IT** | Lane **Técnico** |
| Evento de fin del camino feliz | `Fin. Servicio Activo` | `Fin` |
| Estructura (flujos, gateways, lanes) | Idéntica | Idéntica |

B corrige la convención de nombres (verbo en infinitivo) pero **pierde el nombre descriptivo del evento de fin**. La wiki debería consolidar: nombres de B + evento de fin de A.

##### 5. Observaciones técnicas — qué marcaría un docente

**Errores de notación / modelado (los que bajan nota)**

| # | Hallazgo | Por qué está mal | Corrección |
|---|---|---|---|
| O1 | **El Cliente está como lane dentro del pool de la empresa** | Los lanes de un pool representan roles *internos* de un mismo participante. El cliente es un participante externo: no se lo puede coordinar con flujo de secuencia porque eso implica que la empresa controla su comportamiento. | Sacar `Cliente` a un **pool separado** (colapsado o expandido) y unirlo con **flujos de mensaje** (línea punteada con punta hueca), no con flujos de secuencia. Es el error estructural más grave del diagrama. |
| O2 | **`Notificar sin cobertura` está en el lane Cliente** | La notificación la emite la empresa; el cliente la *recibe*. La tarea está asignada al actor equivocado. | Mover la tarea a `Sistema IT` y, con el cliente en pool aparte, modelar la llegada como flujo de mensaje hacia un evento de mensaje en el pool del cliente. |
| O3 | **Merge implícito antes de `Instalar y configurar el modem`** | La tarea tiene dos flujos de secuencia entrantes (secuencia normal + retorno del "No"). BPMN lo permite (unión implícita OR), pero en trabajo académico se exige explicitar la convergencia. | Insertar un **gateway exclusivo de convergencia** antes de la tarea, con las dos entradas y una salida. |
| O4 | **Ningún gateway de divergencia tiene su convergencia explícita** | `¿Hay cobertura?` diverge y las ramas mueren en dos eventos de fin distintos (esto sí es válido), pero el patrón queda inconsistente con O3. | Definir criterio único: o se cierra todo con gateways, o se acepta cierre por eventos de fin y se corrige solo O3. |
| O5 | **Tareas sin tipificar** | Las 8 tareas son tareas genéricas (rectángulo sin marcador). Las de `Sistema IT` son ejecutadas por un sistema y las de `Técnico`/`Cliente` por personas. | Marcar `Verificar cobertura en la zona`, `Asignar turno y técnico instalador` y `Cerrar instalacion` como **Service Task** (o Script/Business Rule según el caso), y las restantes como **User Task** / **Manual Task**. |
| O6 | **El pool se llama con el nombre del proceso, no del participante** | El pool representa al participante (`Telecom`), no a la actividad. | Renombrar el pool a `Telecom` y dejar `Instalación de Fibra Óptica` como nombre del diagrama/proceso. |
| O7 | **Evento de inicio sin nombre** | Todo evento debería estar nombrado para saber qué lo dispara. | Nombrarlo, p. ej. `Cliente requiere servicio de fibra` (o convertirlo en **evento de inicio de mensaje** si el disparo llega desde el pool del cliente). |
| O8 | **Inconsistencia de lane del timer entre versiones** | En A el timer está en `Sistema IT` y en B en `Técnico`. Dos versiones del mismo proceso no pueden diferir en la asignación de un elemento. | Unificar: el timer va en el lane que retoma el trabajo, es decir `Técnico` *(inferencia)*. |

**Problemas de lógica y completitud del proceso**

| # | Hallazgo | Consecuencia | Corrección |
|---|---|---|---|
| L1 | **Loop de reintento sin límite ni escape** | Si `¿Instalación exitosa?` da "No" indefinidamente, el proceso nunca termina (livelock). No hay contador de intentos ni rama de escalamiento. | Agregar un segundo gateway después del "No": `¿Se superó el máximo de intentos?` → sí → tarea `Reprogramar turno` o `Escalar a soporte técnico` → evento de fin `Instalación fallida`. |
| L2 | **`Cerrar instalacion` ocurre ANTES de `Firmar conformidad`** | Se cierra administrativamente la orden antes de tener la conformidad del cliente. Si el cliente no conforma, el proceso ya cerró y no hay vuelta atrás modelada. | Invertir: `Firmar conformidad` (Cliente/Técnico en sitio) → `Cerrar instalación` (Sistema IT) → evento de fin. *(inferencia sobre el orden real del negocio)* |
| L3 | **No hay camino para "el cliente no firma / no conforma"** | Falta la rama de disconformidad después de `Firmar conformidad`. | Gateway `¿Cliente conforme?` con rama "No" hacia reprogramación o gestión de reclamo. |
| L4 | **Cero manejo de excepciones** | No se modela: cliente ausente el día del turno, falta de materiales/ONT, imposibilidad de acceso al domicilio, cancelación del cliente. | Agregar **eventos intermedios adjuntos (boundary events)** a las tareas críticas: timer de ausencia sobre `Conectar cable...`, evento de cancelación del cliente sobre el tramo de espera. |
| L5 | **El timer `El día del turno` no valida que el turno se haya confirmado** | Se asume que el cliente acepta el turno asignado. No hay confirmación del cliente. | Agregar tarea/mensaje `Confirmar turno con el cliente` con gateway `¿Turno aceptado?`. |
| L6 | **No hay ningún objeto de datos** | No se ve qué información circula: solicitud, orden de trabajo, resultado de la medición de señal, acta de conformidad. | Agregar **Data Objects** asociados: `Solicitud de servicio`, `Orden de trabajo`, `Acta de conformidad`, y un **Data Store** `Sistema de gestión de clientes`. |
| L7 | **El lane `Sistema IT` mezcla decisión de negocio con ejecución sistémica** | Verificar cobertura y cerrar instalación son sistémicas, pero asignar turno y técnico normalmente involucra un área de despacho/planificación. | Evaluar separar un lane `Despacho / Planificación` o justificar la automatización en la memoria del TP. |

**Forma, prolijidad y convenciones**

| # | Hallazgo | Corrección |
|---|---|---|
| F1 | `Cerrar instalacion` sin tilde | `Cerrar instalación` |
| F2 | Etiquetas de gateway `Si` sin tilde (ambos gateways, ambas versiones) | `Sí` |
| F3 | Nombres de tarea con punto final inconsistente (`Conectar cable de fibra desde el nodo.` vs `Instalar y configurar el modem`) | Sin punto final en todas |
| F4 | Versión A mezcla sustantivo e infinitivo en los nombres de tarea | Usar siempre **verbo en infinitivo + objeto** (ya corregido en Versión B) |
| F5 | Rombos de gateway dibujados vacíos, sin la "X" del exclusive gateway | En BPMN 2.0 el rombo vacío **es** válido como exclusivo, pero conviene activar el marcador "X" en Bizagi para que no quede ambiguo frente a un gateway inclusivo o paralelo |
| F6 | El evento de fin del camino feliz perdió su nombre en la Versión B (`Fin` en vez de `Fin. Servicio Activo`) | Restaurar el nombre descriptivo: los eventos de fin deben nombrar el **estado final alcanzado** |
| F7 | Etiqueta `El día del turno` posicionada como texto suelto al costado del evento (Versión B) en vez de como nombre del evento | Escribirla como nombre del evento intermedio, no como anotación |
| F8 | Ninguna rama tiene marcado el **flujo por defecto** (barra oblicua) | Marcar como default la rama más frecuente en cada gateway (`Si` en `¿Hay cobertura?`, `Si` en `¿Instalación exitosa?`) |
| F9 | En Versión A hay mucho espacio muerto a la derecha y el layout se estira innecesariamente | Compactar antes de exportar; el diagrama tiene que leerse en una carilla |

**Lo que está bien hecho** (para no reescribirlo de más): los dos gateways están correctamente etiquetados en ambas salidas; el uso del evento intermedio de tiempo para modelar la espera hasta el turno es correcto y es lo que más suma; todos los caminos terminan en un evento de fin explícito (salvo el loop de L1); no hay tareas huérfanas ni flujos sin destino; no falta ningún evento de fin en el sentido estricto de la notación.

##### Etapa 2 — Gestión de riesgos y servicios de TI (entregada)

**Inventario de activos** (11 activos, escala C/I/D 1–3, criticidad = C+I+D):

| ID | Activo | Tipo | Contenedor | Rel. | Propietario | Custodio | C | I | D | Crit. |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CRM | Software | Servidor / Cloud | 3, 5 | Gerencia Comercial | Área de TI | 3 | 2 | 3 | **8** |
| 2 | Fusionador de fibra óptica | Equipamiento | Vehículo del técnico | 6 | Área de Operaciones | Técnico instalador | 1 | 1 | 3 | **5** |
| 3 | Sistema de gestión de OT (SGOT) | Software | Servidor / Cloud | 1, 5 | Gerencia de Operaciones | Área de TI | 2 | 3 | 3 | **8** |
| 4 | Personal de soporte remoto (NOC) | Personas | N/A | 8, 1, 3, 10 | Gerencia de RRHH | Supervisor de Instalaciones | 1 | 2 | 2 | **5** |
| 5 | Base de datos de clientes y OT | Soporte | Servidor de BD | 1, 3 | Gerencia Comercial | Área de TI / DBA | 3 | 3 | 3 | **9** |
| 6 | Cable de fibra óptica | Equipamiento | Depósito / Vehículo | 2, 7 | Área de Logística | Personal de almacén | 1 | 1 | 3 | **5** |
| 7 | Balanceador de cargas | Hardware | Data Center / Nodo Telecom | 3, 9, 6, 10 | Área de TI / Infraestructura | NOC / Área de TI | 1 | 2 | 3 | **6** |
| 8 | Técnico instalador de campo | Personas | N/A | 2, 6, 7 | Gerencia de RRHH | Supervisor de Instalaciones | 1 | 2 | 3 | **6** |
| 9 | Firewall | Hardware | Data Center / Nodo Telecom | 7, 10 | Área de TI / Seguridad | NOC / Área de TI | 3 | 3 | 3 | **9** |
| 10 | Software de monitoreo NMS | Software | Servidor de monitoreo | 7, 9 | Área de TI / NOC | NOC / Área de TI | 2 | 2 | 3 | **7** |
| 11 | Nodo de distribución | Instalaciones | Edificio Telecom | 7, 9, 10 | Gerencia de Infraestructura | NOC / Área de TI | 1 | 2 | 3 | **6** |

**Método de valoración adoptado:** Severidad = Probabilidad × Impacto, ambas en escala 1–5 (severidad 1–25). Probabilidad justificada con dos factores FAIR (frecuencia de contacto con la amenaza + capacidad de resistencia actual); impacto con dos factores FAIR (pérdida primaria + pérdida secundaria). Umbrales: 1–4 Bajo (aceptar/monitorear), 5–9 Medio (mediano plazo), 10–14 Alto (tratamiento prioritario), 15–25 Muy alto (urgente).

**Riesgos identificados y priorizados:**

| Prio. | ID | Riesgo | Activo | P | I | Sev. | Nivel | ¿Tiene planilla? |
|---|---|---|---|---|---|---|---|---|
| 1 | R03 | Firewall obsoleto sin soporte del fabricante (EOL) | 9 | 3 | 5 | **15** | Muy Alto | Sí |
| 2 | R05 | Acceso no autorizado por credenciales de contratista no dadas de baja | 5 | 3 | 5 | **15** | Muy Alto | Sí |
| 3 | R09 | Balanceador de carga como punto único de falla sin redundancia | 7 | 2 | 5 | 10 | Alto | **No** |
| 4 | R04 | Técnico instalador sin capacitación en nuevo modelo de ONT | 8 | 4 | 3 | 12 | Alto | **No** |
| 5 | R06 | CRM sin flujo de escalamiento a agente humano | 1 | 4 | 3 | 12 | Alto | Sí |
| 6 | R07 | SGOT sin criterio de priorización en la cola de OT | 3 | 4 | 3 | 12 | Alto | **No** |
| 7 | R01 | Corte de suministro eléctrico en nodo de distribución | 11 | 3 | 4 | 12 | Alto | **No** |
| 8 | R08 | Cable de fibra óptica sin plan de mantenimiento preventivo | 6 | 3 | 3 | 9 | Medio | Sí |
| 9 | R10 | NMS genera información imprecisa o falsos positivos | 10 | 3 | 3 | 9 | Medio | **No** |
| 10 | R11 | Nodo de distribución sin puertos disponibles para nuevas altas | 11 | 3 | 3 | 9 | Medio | Sí |

**Criterio de desempate ante severidades iguales:** (1) mayor impacto; (2) dimensión crítica afectada, priorizando C > I > D por la exposición legal bajo Ley 25.326; (3) criticidad del activo involucrado.

**Riesgos con planilla completa** (identificación + tratamiento + contingencia/recuperación/continuidad + controles ISO 27002): R11, R08, R05, R06 y R03.

| Riesgo | Clasificación SEI | Riesgo residual declarado |
|---|---|---|
| R11 — Nodo sin puertos | 3. Procesos / 3.2 Gestión de Ingeniería / 3.2.1 Planificación de Capacidad | P1 × I3 = **3** (Bajo) |
| R08 — Cable sin mantenimiento preventivo | 3. Procesos / 3.1 Gestión de Operaciones / 3.1.3 Mantenimiento | P1 × I2 = **2** (Bajo) |
| R05 — Credenciales de contratista | 1. Acciones de las Personas / 1.1.3 Omisión y/o 1.2.3 Robo | P1 × I5 = **5** (Medio) |
| R06 — CRM sin escalamiento | 2. Fallas de Sistemas y Tecnología / 2.2 Software / 2.2.1 Diseño Defectuoso | P1 × I3 = **3** (Bajo) |
| R03 — Firewall EOL | 2. Fallas de Sistemas y Tecnología / 2.1 Hardware / 2.1.4 Obsolescencia | P1 × I3 = **3** (Bajo) |

**Conclusión sobre ITIL en la organización (punto 9.1):** Personal tiene las herramientas de base (NMS para eventos, SGOT como tickets de campo, CRM como canal del cliente) **pero le falta la capa de gobierno ITIL que las conecte**: matriz de priorización única, reglas de correlación de eventos, flujo de escalamiento formal y medible, y derivación sistemática de incidentes recurrentes a Gestión de Problemas. *(Esta conclusión es el fundamento directo de uno de los proyectos candidatos de la Etapa 3.)*

- **Umbrales de evento definidos** (Informativo / Advertencia / Excepción) para Firewall, Balanceador y Nodo de distribución. Solo Excepción abre ticket automático.
- **SLA definidos:** primera respuesta 15 min (crítica) / 1 h (alta) / 4 h (media-baja); resolución 2 h / 8 h / 48 h.
- **CMDB:** ficha de CI con 13 atributos, clases de CI (Hardware, Software/Aplicación, Datos, Servicio de negocio, Ubicaciones), relaciones tipificadas ("corre sobre", "depende de", "se conecta con", "es parte de", "monitorea a"), y 7 KPI de control.
- **Problemas y Cambios:** proceso de 6 pasos para Problemas (identificación reactiva/proactiva → registro → RCA con 5 porqués o Ishikawa → Error Conocido + workaround en KB → RFC → cierre) y de 8 pasos para Cambios (RFC → categorización estándar/normal/emergencia → evaluación de impacto vía CMDB → CAB → construcción y prueba → implementación con rollback → revisión post-implementación → actualización de CMDB). Dos KPI gerenciales: Change Success Rate ≥90% y reducción ≥30% de incidentes recurrentes por problema resuelto.

##### Inconsistencias detectadas en lo ya entregado

Encontradas al revisar los documentos el 2026-07-29. Ninguna es de contenido: todas son de trazabilidad, y la Etapa 3 se apoya en esos números.

**Corregidas** — en `materias/ASI/ASI26_310_UNIDAD1_corregido.docx` y `materias/ASI/ASI26_310_UNIDAD2_corregido.docx`. Los originales entregados quedaron intactos en `fuentes/ASI/`, que es inmutable.

| # | Dónde | Problema | Qué se hizo |
|---|---|---|---|
| I1 | Etapa 2, planillas | Los **títulos** de las planillas iban R01…R05 pero los **identificadores internos** son R11, R08, R05, R06 y R03. La planilla titulada "R03" contenía el riesgo R05 y la titulada "R05" contenía R03 | Títulos renumerados al identificador real: R11, R08, R05, R06, R03 |
| I2 | Etapa 2, planilla de R03 y ficha de CI (10.1) | El Firewall figuraba con C3 **I2** D3 = **8** en la tabla de activos involucrados de R03 y con "3, **2**, 3" en la ficha de CI, contra C3 I3 D3 = **9** del inventario y de la tabla de riesgos identificados | Unificado en **3, 3, 3 = 9** (el valor del inventario, que es el que coincide con el punto 2) |
| I5 | Etapa 1, punto 9 | El objetivo de TI de la app de campo estaba maquetado como **título de nivel 1**, suelto entre los puntos 9 y 10 | Bajado a párrafo normal con la misma sangría que los otros dos objetivos de TI |

**Pendientes** — requieren una decisión o un dato que no está en los archivos.

| # | Dónde | Problema | Qué falta |
|---|---|---|---|
| I3 | Etapa 2, punto 5 | **R09 es prioridad 3 (severidad 10) y quedó sin planilla de tratamiento.** Es el riesgo de mayor severidad no tratado del documento. También quedaron sin planilla R04, R07, R01 y R10 | Decisión: si la Etapa 3 toma alguno de ellos como problema del proyecto, agregar la planilla faltante como anexo o justificar la selección |
| I4 | Etapa 2, encabezado | La tabla `VERSIÓN DEL DOCUMENTO` tiene una sola fila (Entrega Inicial, 18/05/2026) y una fila vacía, pese a que la entrega ya fue corregida | Dato: fecha de la corrección de cátedra y fecha del ajuste del grupo, para agregar las filas `CC` y `Grupo N310` como en la Etapa 1 |
| I6 | `fuentes/ASI/` | **Falta el organigrama.** `modeloPersonal.png` no es un organigrama: es una segunda versión del mismo BPMN. El organigrama del punto 6 de la Etapa 1 no está entre los archivos | Archivo: recuperar el organigrama y subirlo a `fuentes/ASI/` |

##### Etapa 3 — Proyecto de TI (en curso)

**Fecha de entrega: 28/08/2026.**

**Estado al 2026-08-23: punto 3 validado por el docente.** Proyecto aprobado con su formulación; modo de construcción **SaaS FSM configurable**; las alternativas del punto 3 pasan a ser **proyectos distintos que atacan otros problemas**, dos de ellas solo mencionadas. Cerradas D1, D4 y D5. **D2 y D3 siguen abiertas**: el docente no respondió las consultas de cronograma ni de líneas base. **Los doce puntos de la consigna están desarrollados** y el Acta va embebida como Anexo I. Documento en 54 páginas. Quedan dos cosas que dependen del grupo: los nombres propios y el monto de autoridad de compra del Acta, y el dibujo de los dos planos del punto 6, cuya especificación ya está escrita. Ante las consultas que el docente no respondió, **el grupo decidió y siguió adelante**: líneas base como supuestos con medición en la fase 2 (D3), cronograma en meses relativos (D2) y justificación cualitativa sin matriz. Quedan sujetas a revisión si se pronuncia.

###### ▶ Por dónde retomar

**Paso 1 — Reescribir el punto 3 con el encuadre nuevo. HECHO el 2026-08-23.** El docente validó el proyecto y redefinió qué son las "alternativas". Ver *Alternativas y selección*. Queda enviarle el mensaje de seguimiento con las tres consultas que no respondió más la que surgió de su respuesta — ver *Validación del punto 3*.

**Paso 2 — Producir, en este orden de dependencia:**

```
EDT ──┬─→ perfiles y competencias (punto 5)
      ├─→ diagrama de Red → camino crítico → Gantt → aplanamiento (punto 10)
      └─→ adquisiciones + RFI/RFP (puntos 7, 8, 9) ─→ costos (punto 11) ─→ factibilidad (punto 12)

En paralelo, sin depender de la EDT: Acta de Proyecto (punto 4.b) y layout de H&S (punto 6).
```

**Ojo con D5 al armar la EDT**, no después: hay que meter paralelismo real y hacer que dos o tres tareas compitan por el mismo perfil. Con SaaS **ya no aparece solo** — hay que diseñarlo explícitamente (ver D5).

**El punto más pesado ahora es la factibilidad legal (punto 12).** Con SaaS los datos personales de clientes salen del perímetro, lo que agrava R05 (severidad 15) y activa de lleno la Ley 25.326: transferencia internacional, encargado de tratamiento, región de alojamiento, cláusulas contractuales y notificación de brecha. Es un apartado ganador si se escribe bien y una masacre si se omite. La factibilidad económica se resuelve con el TCO a 3 años de la licencia por usuario acumulada contra las horas y los costos evitados.

**Acta de Proyecto (punto 4.b) — BORRADOR ESCRITO al 2026-08-19.** Fuente de verdad: `materias/ASI/etapa3-acta-proyecto.md`; el `.docx` se regenera con `npm run docx -- <in.md> <out.docx>` (`scripts/build-docx.js`), no se edita a mano. Sigue el Anexo I de cátedra y las instrucciones campo por campo del apunte T2 (ver Unidad 5 §6).

Pendiente de resolver en el Acta: los **nombres propios** (van inventados, marcados con ⚠ y en rojo en el `.docx`) y el **monto de autoridad de compra** del Director de Proyecto, que hoy quedó genérico — es el campo donde el ejemplo de cátedra es más concreto.

> **Dependencia con D4 — ya se activó.** El Acta se había escrito sobre A1 desarrollo interno. Con la validación del 23/08 hay que actualizar `Producto` y `Entregables` (pasan a "solución configurada sobre plataforma FSM de mercado") y la autoridad de compra (de infraestructura a licenciamiento y servicios). `Justificación`, `Objetivos` y `Límite` no cambian.

**Lo que falta conseguir:** fecha de entrega, y si la cátedra acepta cronograma en meses relativos.

**Entregables exigidos por la consigna**, en orden:

1. Proponer un proyecto de TI.
2. Objetivos con criterios cuantificables.
3. Alternativas, selección y justificación. **Validar con el docente.**
4. Según la alternativa: (a) ciclo de vida, fases, actividades y **EDT/WBS**; (b) **Acta de Proyecto** con la plantilla PMI del e-Group.
5. Perfiles y competencias del equipo.
6. **Layout** de los sectores involucrados en el proceso crítico + medidas de higiene y seguridad.
7. Activos a adquirir y características a considerar.
8. Forma de adquisición de cada activo.
9. Diferencia RFI / RFP y en qué adquisición concreta se usaría cada uno.
10. Asignación de recursos a la EDT, estimación de tiempos, **diagrama de Red** y **Gantt** con aplanamiento de recursos, y duración total del proyecto.
11. Variables para calcular los costos.
12. Factibilidad **técnica, económica y legal**.

###### Los tres candidatos evaluados

| | **A — Seguridad perimetral + IAM** | **B — Gestión de OT + app de campo** | **C — ITSM unificado + CMDB** |
|---|---|---|---|
| Nace de | R03, R05, R09 (mayor severidad) | El objetivo de TI ya escrito en Etapa 1 | La conclusión del punto 9.1 de Etapa 2 |
| Trazabilidad hacia atrás | Alta (riesgos #1, #2, #3) | **Máxima** (cita textual del propio trabajo) | Alta (cita textual de la conclusión) |
| ¿Toca el BPMN? | No | **Sí, actividades 3 a 9** | No (gobierna las excepciones) |
| Layout H&S | Bueno (data center: riesgo eléctrico, LOTO) | **Muy bueno** (oficina + depósito + campo) | **Malo** (proyecto de oficina) |
| RFI / RFP | Bueno | Bueno | **Muy bueno** (mercado ITSM diverso) |
| Factibilidad económica | **Floja** (beneficio = pérdida evitada) | **Buena** (+5% × N técnicos × costo hora) | Media |
| Factibilidad legal | **Muy buena** | Buena | **Muy buena** |
| EDT / Gantt | Buena (dependencias duras reales) | **Muy buena** | Buena, con riesgo de EDT genérica |

**A — Implementar una plataforma de seguridad perimetral y de gestión de identidades** (NGFW en clúster HA + segmentación de red + balanceador redundante + IAM/SSO con MFA y baja automática de credenciales integrada con RRHH). Cierra R03 (15→3), R05 (15→5) y R09.
*A favor:* las tres alternativas de implementación salen literalmente de las columnas EVITAR / TRANSFERIR / MITIGAR de las planillas de la Etapa 2, y las metas de los objetivos ya están escritas ahí como riesgo residual. Cierra el circuito ITIL que el grupo diseñó (riesgo → RFC → CAB → CMDB).
*En contra:* el beneficio es pérdida evitada, no ahorro — la factibilidad económica hay que construirla con costos evitados (multas Ley 25.326, penalidades por SLA, horas de auditoría manual). No toca ninguna actividad del BPMN. No hay hilo con los objetivos de negocio de la Etapa 1 (cobertura, tiempos, productividad); habría que agregar uno de cumplimiento normativo y declararlo como ajuste. Riesgo de percepción "es solo comprar un firewall".

**C — Implementar una plataforma ITSM unificada con CMDB.** Cola única sobre CRM/SGOT/NMS, motor de priorización por impacto/urgencia, correlación de eventos, CMDB formal y vínculo incidente–problema–cambio. Ataca R06, R07 y R10.
*A favor:* máxima reutilización de lo ya escrito en la Etapa 2 — umbrales de evento, SLA, ficha de CI, relaciones, KPI de 10.2 y 11.3, procesos de 11.2. Buena parte del contenido técnico ya está redactado. El mejor caso de RFI/RFP de los tres: hay mercado real, diverso y comparable. Factibilidad legal jugosa (datos personales en nube de proveedor extranjero → transferencia internacional, encargado de tratamiento, notificación de brecha).
*En contra:* **el layout de higiene y seguridad es el punto débil** — es un proyecto de oficina y el layout se derrumba a "silla ergonómica y pausas activas", justo lo que la cátedra marca como insuficiente. Además, con olas secuenciales no hay conflicto de recursos que aplanar.

###### Candidato B — desarrollo (ELEGIDO, 2026-08-10)

**Nombre.** *Implementar una plataforma de gestión de órdenes de trabajo con aplicación móvil de campo, para resolver la falta de trazabilidad, priorización y control de competencias técnicas en el proceso de instalación de fibra óptica.*

**Trazabilidad con la Etapa 1** — el proyecto no introduce un objetivo nuevo:

| Origen | Texto ya comprometido | Cómo lo ataca |
|---|---|---|
| Objetivo de TI | "Implementar una aplicación de gestión para técnicos de campo… aumentar la productividad operativa en un 5% para el año 2026" | Es literalmente el alcance del proyecto |
| Meta de TI | "Asignación Optimizada de Técnicos" | Motor de asignación por competencia + zona + carga + ventana horaria |
| Objetivo de negocio | "Aumentar el rendimiento de los técnicos en un 5% (instalaciones / horas de trabajo) para este 2026" | Objetivo O1, **mismo indicador** |
| Meta de negocio | "Mejorar el tiempo de instalación" | Objetivo O2 (tiempo de ciclo de la OT) |
| Meta de negocio | "Mejorar la calidad de servicio a los clientes" | Trazabilidad de estado + conformidad digital |

> El alineamiento negocio↔TI que pide la cátedra **ya está escrito, con el mismo 5% y la misma fórmula, en los dos planos**. Ningún otro candidato tiene eso.

**Trazabilidad con la Etapa 2:**

| ID | Riesgo | Sev. | Estado en Etapa 2 | Aporte del proyecto |
|---|---|---|---|---|
| R04 | Técnico sin capacitación en nuevo modelo de ONT | 12 | **Sin planilla** | Matriz de competencias por técnico; el motor bloquea asignar una OT con ONT modelo X a un técnico no certificado |
| R07 | SGOT sin criterio de priorización en la cola de OT | 12 | **Sin planilla** | Motor de priorización por matriz impacto/urgencia, con los SLA ya definidos en 9.1 |
| R06 | CRM sin flujo de escalamiento | 12 | Tratado | Reduce la causa aguas arriba: el estado real de la OT queda disponible, se cortan los reclamos duplicados |
| R05 | Credenciales de contratista no dadas de baja | 15 | Tratado | **La app de campo es el control ya comprometido**: la columna EVITAR dice textual "los técnicos contratistas solo acceden a la app móvil de campo, sin acceso a los sistemas backend" |

> Argumento a escribir explícito: R04 y R07 quedaron identificados, valorados en severidad 12 y **sin plan de tratamiento**. Este proyecto es el tratamiento de ambos — tapa un hueco de la entrega anterior en vez de repetirla. Esto también resuelve la inconsistencia I3.

**Solución (6 componentes).** 1) Módulo de despacho y priorización con cola única alimentada por CRM, SGOT y excepciones del NMS, con cronómetro de SLA y escalamiento. 2) Motor de asignación por competencia certificada, zona/nodo, carga del día, ventana horaria y stock del vehículo. 3) App móvil offline-first: agenda, ficha de OT con datos mínimos, checklist por modelo de ONT, mediciones ópticas, fotos de evidencia, geolocalización, consumo de materiales, tipificación obligatoria de motivo cuando la visita no se completa, y conformidad del cliente con firma digital. 4) Integraciones con SGOT (A3), CRM (A1), BD de clientes y OT (A5), NMS (A10) y stock. 5) Seguridad: SSO + MFA, mínimo privilegio, baja automática de credenciales integrada con RRHH, logs. 6) Tablero de KPI para supervisores y Gerencia de Operaciones.

**Proceso afectado:** instalación de fibra óptica, actividades 3 a 9 del proceso modelado en la Etapa 1. Las actividades 1 y 2 (recepción de solicitud y verificación de cobertura) quedan fuera y siguen en CRM.

**Usuarios:** técnico instalador de campo (A8, propios y contratistas) · supervisor de instalaciones · NOC (A4) · área comercial (consulta) · logística/almacén · Gerencia de Operaciones. El cliente final no es usuario: recibe notificaciones y firma la conformidad.

**Alcance sugerido — QUÉ NO INCLUYE** (esto es lo que evita el proyecto-paraguas): rediseño del flujo de escalamiento del CRM (R06, es proyecto hermano y ya tiene planilla) · reemplazo o migración de CRM, SGOT o BD · obra civil, tendido troncal, ampliación de nodos (R11) y mantenimiento preventivo del cable (R08) · reemplazo del firewall (R03), redundancia del balanceador (R09) y correlación del NMS (R10) · venta, facturación y recupero de clientes · otros procesos de campo (reparaciones, mudanzas, desinstalaciones) · compra de vehículos y fusionadoras (A2).

**Objetivos cuantificables propuestos** (las líneas base son supuestos a validar, ver decisión 3):

| # | Resultado | Indicador | Línea base | Meta | Plazo |
|---|---|---|---|---|---|
| O1 | Productividad del técnico de campo | Instalaciones finalizadas conformes ÷ horas-técnico disponibles | 0,50 inst./hora-técnico *(supuesto)* | 0,525 (+5%) | 6 meses desde go-live |
| O2 | Latencia de registro del cierre de OT | % de OT cerradas en el sistema dentro de los 15 min de terminada la visita; tiempo medio asignación→cierre | 20% / 26 h *(supuesto)* | ≥90% / ≤8 h | Mes 4, sostenido 3 meses |
| O3 | Visitas fallidas por causa evitable | OT reprogramadas por "técnico sin competencia" o "kit incompleto" ÷ OT despachadas | 12% *(supuesto)* | ≤6% | 6 meses desde go-live |
| O4 | Cumplimiento de la priorización de la cola | % de OT despachadas según el orden del motor; % de cumplimiento de SLA de primera respuesta | No medible hoy (esa **es** la definición de R07) | ≥95% / ≥90% | Mes 3 desde go-live |

**Alternativas y selección — REDEFINIDA POR EL DOCENTE (2026-08-23).**

Respuesta textual del docente a la consulta del punto 3:

> Hola Gonza! me parece muy buen proyecto TI, lo validaría como: implementar una plataforma de gestión de órdenes de trabajo con app móvil de campo para resolver trazabilidad, priorización y control de competencias técnicas en instalaciones de fibra óptica.
> En alternativa solo dejaría SaaS FSM configurable. Y piensen en otra alternativa TI distinta al proyecto, otro problema que detecten que puedan atacar (uno o dos alternativas). No hace falta que la elaboren/desarrollen, simplemente mencionarlas

Tiene tres consecuencias, y la primera es la que más cambia el trabajo:

1. **"Alternativas" no son modos de construcción sino proyectos distintos.** El grupo las había planteado como interno / SaaS / tercerizado: tres formas de construir lo mismo. El docente las lee como **proyectos alternativos que atacan problemas distintos**. Bajo su lectura, "seleccionar una y justificar" recién tiene sentido — con una sola alternativa no había nada que seleccionar.
2. **El modo de construcción queda fijado en SaaS FSM configurable.** Esto revierte D4, que el grupo había cerrado en A1 desarrollo interno el 10/08.
3. **El nombre del proyecto lo da él.** Usar su formulación textual: si el que corrige propone el título, ese es el título.

###### Estructura del punto 3

<!-- cols: 6,30,42,22 -->

| | Alternativa | Problema que ataca | Estado |
|---|---|---|---|
| 1 | **OT-Campo** — plataforma de gestión de órdenes de trabajo con app móvil de campo, sobre **SaaS FSM configurable** | Falta de trazabilidad de la OT, ausencia de criterio de priorización en la cola (**R07**, sev. 12, sin tratamiento) y falta de control de competencias al asignar (**R04**, sev. 12, sin tratamiento) | **Seleccionada** — se desarrolla |
| 2 | Plataforma de seguridad perimetral y gestión de identidades | Perímetro sobre equipo obsoleto sin soporte (**R03**, sev. 15) y credenciales de contratistas que sobreviven al fin del contrato (**R05**, sev. 15) — los dos riesgos más altos del trabajo | Solo mencionada |
| 3 | Gestión de capacidad y mantenimiento preventivo de planta externa | Nodos que se saturan sin aviso y bloquean altas comerciales (**R11**) y cable que se degrada sin plan de inspección hasta que corta (**R08**) | Solo mencionada |

**Por qué esas dos y no otras.** Las tres condiciones que tienen que cumplir: atacar un problema **distinto** del proyecto elegido, salir del análisis de riesgos que el grupo ya hizo, y no pisarse entre sí.

- La 2 es de **otro dominio**: perímetro e identidades, no gestión de OT. Y ataca los dos únicos riesgos de severidad 15 del trabajo, así que es la que más contrasta en importancia.
- La 3 es de **otro dominio otra vez**: planta externa, ni sistemas de gestión ni infraestructura de datacenter. Ataca dos riesgos de severidad 9.
- Se descartó mencionar la **plataforma ITSM unificada con CMDB**, aunque está analizada en esta wiki: se pisa con el proyecto elegido, porque ambos tocan R06/R07 y la cola de tickets. El docente pidió *otro problema*.

**Justificación de la selección** (cualitativa, no por matriz — ver la consulta pendiente abajo). Se selecciona la alternativa 1 por cuatro razones, en orden de peso:

1. **Trata riesgos que quedaron sin tratamiento.** R04 y R07 fueron identificados y valorados en severidad 12 en la Etapa 2, y no recibieron planilla. Este proyecto es el tratamiento de ambos: cierra un hueco de la entrega anterior en lugar de repetirla.
2. **Ejecuta un objetivo ya comprometido.** El objetivo de TI de la Etapa 1 —"implementar una aplicación de gestión para técnicos de campo… aumentar la productividad operativa en un 5%"— es literalmente el alcance de este proyecto, con el mismo indicador que el objetivo de negocio.
3. **Impacta directamente sobre el proceso crítico.** Interviene las actividades 3 a 9 del proceso modelado en la Etapa 1. Las alternativas 2 y 3 sostienen la infraestructura o la planta, pero no modifican ninguna actividad del proceso.
4. **Habilita el resto de la planificación.** Al tocar oficina, depósito y trabajo de campo, es el único de los tres que da material real para el layout de higiene y seguridad del punto 6.

**Modo de construcción: SaaS FSM configurable**, por indicación del docente. Se contrata una plataforma de *Field Service Management* de mercado y se configura: flujos, roles, matriz de competencias, reglas de priorización, SLA y app de campo. La organización no construye el producto; construye las **integraciones**, la **configuración funcional** y la **capa de seguridad**.

**Contrapartida a declarar en el documento** (la cátedra pide que la desventaja se admita explícitamente): costo recurrente por usuario que crece con la dotación, dependencia del proveedor, y —lo más sensible acá— los datos personales de clientes salen del perímetro de la organización. Esto último agrava directamente **R05**, valorado en severidad 15 en la Etapa 2, y por eso se compensa por contrato: región de alojamiento habilitada, cifrado en tránsito y en reposo, SSO con doble factor, mínimo privilegio, notificación de bajas de credenciales en menos de 24 horas y derecho de auditoría. Ese párrafo es obligatorio en la factibilidad legal del punto 12.

> **Qué se cae de lo decidido el 10/08.** La matriz ponderada de ocho criterios que comparaba interno / SaaS / tercerizado, con los pesos justificados por R03 y R05. Queda archivada más abajo como respaldo: si el docente responde que igual quiere una matriz, se readapta a las tres alternativas nuevas; si no, no va al documento. **Consulta pendiente.**

###### Matriz de construcción (archivada — respaldo, no va al documento salvo que el docente la pida)

Comparaba las tres formas de construir el mismo alcance. El docente indicó dejar solo SaaS, de modo que la comparación perdió objeto, pero la justificación de los pesos sigue siendo material reutilizable.

<!-- cols: 41,10,16,16,17 -->

| Criterio | Peso | A1 Interno | A2 SaaS FSM | A3 Tercerizado |
|---|---|---|---|---|
| Seguridad y cumplimiento (Ley 25.326, R03, R05) | 20% | 5 | 3 | 4 |
| Integración con SGOT / CRM / BD / NMS | 20% | 5 | 3 | 4 |
| Dependencia del proveedor | 15% | 5 | 2 | 3 |
| Costo total de propiedad a 3 años | 10% | 2 | 4 | 3 |
| Tiempo hasta el go-live | 10% | 2 | 5 | 4 |
| Mantenimiento y evolución | 10% | 4 | 5 | 3 |
| Escalabilidad | 10% | 3 | 5 | 3 |
| Conocimiento disponible en el equipo | 5% | 3 | 4 | 3 |
| **Ponderado** | **100%** | **4,00** | **3,60** | **3,50** |

**Ciclo de vida: híbrido.** Predictivo para la selección del proveedor, la contratación, la arquitectura de integración, la seguridad y el cumplimiento normativo: requerimientos estables, compras corporativas con RFI/RFP, evaluación legal e integraciones con sistemas heredados definidas de antemano. Incremental/iterativo para la configuración funcional, la UX de la app de campo, las reglas de priorización y de asignación, y el despliegue territorial: la usabilidad con guantes, bajo sol directo y con conectividad intermitente no se especifica por adelantado, y los pesos del motor de asignación se calibran con datos de operación, no en una reunión de diseño.

No cascada pura: si la app se especifica de punta a punta y se entrega recién al final, el riesgo es entregar una herramienta que los técnicos no usan y falsean —cierres cargados en masa a fin de jornada—, lo que destruye la medición de O1 y O2 y deja el proyecto sin evidencia de resultado. No ágil puro: hay compromisos contractuales con un proveedor, adquisiciones con plazos de entrega, marco regulatorio de datos personales y un presupuesto que la Gerencia de Operaciones necesita aprobado por anticipado.

> **Cambio respecto del 10/08.** Con SaaS el tramo iterativo se justifica por la **configuración y la adopción**, no por la construcción: no se desarrolla la app, se la configura y se la calibra contra el uso real. El argumento sigue en pie, pero hay que redactarlo así — decir que se itera "porque se construye" ya no aplica.

**Fases propuestas (base de la EDT) — 11 fases:** 1. Inicio (Acta aprobada) · 2. Relevamiento y análisis (**incluye la medición de líneas base como entregable propio**, ver D3) · 3. Selección de proveedor (RFI → lista corta → RFP → evaluación → contrato) · 4. Diseño y configuración de la plataforma (flujos, roles, matriz de competencias, reglas de priorización, SLA, tableros) · 5. Integración y seguridad (SGOT, CRM, BD, NMS y stock; SSO, doble factor, mínimo privilegio, baja automática de credenciales) · 6. Migración de datos (OT abiertas, padrón de técnicos, matriz de competencias inicial) · 7. Pruebas (funcionales, de integración, de carga y de seguridad) · 8. Piloto en zona acotada · 9. Capacitación · 10. Despliegue por olas geográficas · 11. Estabilización y cierre.

> **Volvimos de 12 a 11 fases.** Con desarrollo interno se habían partido en *arquitectura y diseño técnico* + *adquisiciones* + *desarrollo por módulos*. Con SaaS eso se reunifica en *selección de proveedor* + *diseño y configuración*. Es exactamente la estructura que tenía la wiki el 29/07.

> **Dónde nace el paralelismo ahora (D5).** Con SaaS ya no aparece solo, hay que diseñarlo: las adquisiciones de dispositivos rugerizados y MDM corren en paralelo a la configuración; las cuatro integraciones (SGOT, CRM, BD, NMS) se planifican solapadas compitiendo por **un único especialista de integraciones**; el material de capacitación se prepara en paralelo a las pruebas; y la carga de la matriz de competencias va en paralelo a la integración. Sin eso, el punto 10 se responde con "no se detectaron conflictos", que es la peor respuesta posible.

> La fase 11 cierra el circuito con la Etapa 2: el nuevo sistema es un CI nuevo en la CMDB (clase Software/Aplicación) y su puesta en producción es un **cambio normal que pasa por el CAB**, tal como se definió en el punto 11.2. Es un punto fácil de sumar.

**Adquisiciones — vuelven al perfil SaaS.** Licencias de plataforma FSM por usuario/mes (dimensionar: técnicos + supervisores + NOC + despacho) · servicio de implantación y configuración por partner certificado (horas) · horas de consultoría para las cuatro integraciones · dispositivos móviles rugerizados para los técnicos · MDM para administrarlos · servicio de mapas y geolocalización si no viene incluido en la plataforma · ambiente de pruebas no productivo · capacitación · soporte premium durante el período de estabilización. Cada uno con forma de adquisición distinta: suscripción anual, contrato de servicios por hora, compra directa, pago por uso.

> **Esto mejora los puntos 7, 8 y 9.** Con SaaS hay un mercado real, diverso y comparable de plataformas FSM, con diferencias sustantivas entre proveedores en motor de asignación, modo offline, precio por usuario y región de alojamiento. El **RFI** se justifica solo —relevar qué plataformas existen, con qué conectores, en qué rango de precio y dónde alojan los datos— y el **RFP** también, una vez definidos los requisitos de integración, SLA y seguridad. Con desarrollo interno este punto era más flojo.

**Sectores para el layout de Higiene y Seguridad** — la mayor ventaja de este candidato: cubre los dos bloques de la guía en un solo trabajo.

| Sector | Personas | Riesgos | Medidas |
|---|---|---|---|
| Depósito / pañol (contenedor de A2 y A6) | Almacén, técnicos que retiran kits | Caída de objetos, sobreesfuerzo por bobinas, atrapamiento, autoelevador | Estanterías ancladas con carga señalizada, carros, EPP, senderos peatonales demarcados, zona de armado de kits |
| Playa de carga y estacionamiento | Técnicos, almacén | Atropellamiento, retroceso de vehículos, carga/descarga | Circulación unidireccional señalizada, espejos, chaleco reflectivo, velocidad máxima, punto de encuentro |
| Oficina NOC / sala 24×7 (A4) | Soporte remoto, supervisores | Fatiga visual, postura sostenida, ruido, riesgos psicosociales por turnos rotativos | Monitores regulables a ≥50 cm, iluminación sin reflejos, sillas ergonómicas, pausas cada 2 h, canaletas, rotación con descanso planificado |
| Mesa de despacho / Supervisión | Supervisores, despachantes | Ídem videoterminal, con más carga de atención simultánea | Ídem + límite de pantallas por operador, auriculares con limitador |
| Sala técnica / nodo (A7, A9, A11) | TI/Infraestructura, NOC | Riesgo eléctrico, arco eléctrico, temperatura, ruido, acceso no autorizado | Acceso restringido, señalización, procedimiento seguro con bloqueo/etiquetado (LOTO), matafuego clase C, EPP dieléctrico |
| Campo — tendido aéreo (vía pública) | Técnicos | **Trabajo en altura**, **riesgo eléctrico** por proximidad a línea, circulación vehicular, caída de herramientas | Arnés con doble cabo y anclaje certificado, escalera dieléctrica, distancia mínima a línea energizada, conos y vallado, casco, **habilitación registrada por técnico (engancha con R04 y la matriz de competencias)**, prohibición con viento o tormenta |
| Campo — cámara subterránea | Técnicos | **Espacio confinado**: atmósfera deficiente, anegamiento, caída a distinto nivel | Permiso de trabajo, medición previa de atmósfera, ventilación forzada, trabajo de a dos con vigía, arnés con línea de rescate, vallado de la boca |
| Campo — domicilio del cliente | Técnicos | Riesgo eléctrico en tablero, altura sobre escalera, animales, conflicto con el cliente | Verificación de corte de energía, escalera propia, EPP, protocolo de trabajo solo, checklist de seguridad **obligatorio en la app antes de iniciar la OT** |
| Aula de capacitación (sector temporal) | Técnicos y supervisores | Aforo, evacuación, fatiga en jornadas largas | Aforo declarado, salidas señalizadas, pausas cada 90 min, práctica de altura con supervisión |

Presentación sugerida: **dos planos, no nueve.** (1) Base operativa en una planta: depósito, playa de carga, mesa de despacho, NOC y sala técnica, con circulación peatonal/vehicular, matafuegos, salidas y punto de encuentro. (2) Croquis tipo de trabajo en campo con la escena de tendido aéreo y vallado; domicilio y cámara subterránea como esquemas complementarios.

###### Decisiones — estado al 2026-08-23

<!-- cols: 6,54,40 -->

| | Decisión | Estado |
|---|---|---|
| D1 | Alcance: **B medio** | **Cerrada** por el grupo |
| D2 | Cronograma en **meses relativos** + plazo de O1 desde el go-live | **Cerrada** por el grupo — **sin confirmar** por el docente (consulta 3, no respondida) |
| D3 | Líneas base declaradas como supuestos, con su medición como entregable de la fase 2 | **Abierta** — consulta 2, no respondida |
| D4 | Alternativa: **SaaS FSM configurable**, y alternativas = proyectos distintos | **Cerrada por el docente** el 2026-08-23 |
| D5 | Paralelismo obligatorio en la EDT | **Cerrada** por el grupo — ahora hay que diseñarlo, ya no aparece solo |

**D1 — Dónde se corta el alcance de B. → CERRADA: B medio.**

| Opción | Qué incluye | Problema |
|---|---|---|
| B chico | Solo la app móvil | EDT pobre, adquisiciones de dos filas, costos triviales |
| **B medio** | Despacho + priorización + motor de asignación + app móvil + integraciones + seguridad | **ELEGIDA** |
| B grande | B medio + correlación de eventos del NMS + CMDB | Se come el candidato C entero. Paraguas |

> **Acoplamiento crítico:** si se recorta la app móvil, se cae el punto de higiene y seguridad — sin trabajo de campo el layout queda en una oficina. La decisión de alcance y el punto 6 de la consigna están atados.

**D2 — El calendario. → CERRADA: meses relativos + plazo desde el go-live.** El objetivo dice "para el año 2026". Se descartaron: fechar el inicio en enero 2026 para que el Gantt cierre en el año (es ficción), y usar fechas de calendario absolutas. Se adopta **Gantt en meses relativos** (Mes 1, Mes 2…) desde la aprobación del Acta, y el plazo de O1 medido **desde el go-live**, declarado como ajuste. Lo que no puede pasar es que el Gantt diga una cosa y el objetivo otra.

> **Consecuencia con SaaS.** El plazo se acorta respecto del desarrollo interno: configuración, cuatro integraciones, piloto y despliegue por olas son del orden de 7 a 9 meses, no de 12 a 18. Sigue sin cerrar dentro de 2026 si se arranca ahora, así que D2 se mantiene. **El docente no respondió si acepta meses relativos** — está en el mensaje de seguimiento.

**D3 — Las líneas base. → SIGUE ABIERTA.** Se consultó el 2026-08-19 y el docente no la respondió; está en el mensaje de seguimiento. No hay ningún dato medido en las Etapas 1 y 2, así que los valores van a ser estimados. Eso no es el problema; el problema es cómo se presentan. Un número estimado presentado como dato medido es lo más fácil de detectar. Un número estimado **declarado como supuesto** es metodológicamente correcto — así se planifica cuando todavía no se mide.

Lo que lo blinda: **la medición de la línea base es una actividad con entregable propio en la fase 2 de la EDT**. El proyecto mismo se hace cargo de medirla. Redacción a usar en el documento:

> *Línea base estimada: 0,50 instalaciones/hora-técnico. **Valor supuesto**, no medido: las Etapas 1 y 2 no relevaron indicadores de operación. Su medición formal es el entregable 2.4 de la fase de Relevamiento y Análisis, y la meta de O1 se recalibrará sobre el valor real.*

No pedir permiso para estimar: preguntar si **este tratamiento** le sirve.

**D4 — La alternativa. → CERRADA POR EL DOCENTE (2026-08-23).** Respondió la consulta 1 del documento de validación. Dos definiciones: el modo de construcción es **SaaS FSM configurable**, y las alternativas del punto 3 pasan a ser **proyectos distintos que atacan problemas distintos**, no modos de construir el mismo proyecto. Ver *Alternativas y selección* más arriba.

> **Qué implicó el cambio.** El grupo había cerrado A1 desarrollo interno el 10/08 con una matriz re-ponderada. La indicación del docente lo revierte. Lo que se perdió y cómo se compensa:
>
> | Punto | Qué se pierde con SaaS | Compensación |
> |---|---|---|
> | 5 — Perfiles | El equipo deja de tener arquitecto, backend, mobile y DBA | Queda un equipo igual defendible: PM, analista funcional, **especialista de integraciones** (son cuatro), especialista de seguridad, consultor del proveedor, UX de configuración, tester, capacitador y referente de operaciones |
> | 10 — Aplanamiento | La sobreasignación ya no aparece sola entre módulos paralelos | Hay que diseñarla: integraciones solapadas sobre un único integrador, adquisiciones en paralelo a la configuración, capacitación en paralelo a pruebas. Ver D5 |
> | 11 — Costos | Deja de haber inversión inicial fuerte; pasa a OPEX recurrente | El TCO a 3 años sigue sirviendo, ahora para mostrar cuánto pesa la licencia por usuario acumulada |
> | 12 — Legal | Se pierde el argumento "los datos no salen del perímetro" | **Mejora**: ahora hay transferencia internacional de datos, encargado de tratamiento, región de alojamiento y notificación de brecha bajo Ley 25.326. Es material propio y específico, no genérico, y reconecta con R05 |
> | 7, 8, 9 — Adquisiciones y RFI/RFP | Nada | **Mejora**: hay mercado real y comparable, el RFI y el RFP se justifican sin forzar el ejemplo |
>
> Saldo: se pierde en los puntos 5 y 10, se gana en 7, 8, 9 y 12. Y el rehacer está acotado porque el análisis SaaS ya existía en esta wiki desde el 29/07.

**D5 — Paralelismo en el cronograma. → CERRADA: paralelismo obligatorio, diseñado desde la EDT.** El punto 10 pide aplanar recursos. Si el cronograma sale secuencial no hay conflicto que aplanar y ese punto se responde con "no se detectaron conflictos", que es la peor respuesta posible. Hay que meterlo desde el diseño de la EDT y que dos o tres actividades compitan por **el mismo perfil**, para que aparezca sobreasignación genuina.

Fuentes de paralelismo con A1: adquisiciones (fase 4) en paralelo al desarrollo (fase 5) · módulo de despacho e integraciones compitiendo por el mismo desarrollador backend · el especialista en seguridad partido entre SSO/MFA y la revisión de la app · material de capacitación en paralelo a las pruebas · carga de la matriz de competencias en paralelo a la integración.

> Con SaaS **no aparece solo**: hay que diseñarlo en la EDT a propósito. Las fuentes de paralelismo están listadas en el bloque de fases, más arriba.

###### Validación del punto 3 — respuesta del docente (2026-08-23)

El documento `materias/ASI/etapa3-validacion-punto3.md` se le envió el 2026-08-19 con los puntos 1, 2 y 3 y cuatro consultas al final. Respondió el 2026-08-23.

**Respondió la consulta 1.** Validó el proyecto, dio la formulación del nombre, indicó dejar solo SaaS FSM configurable como modo de construcción, y pidió agregar una o dos alternativas de TI que ataquen **otro problema**, solo mencionadas. Texto completo y consecuencias: ver *Alternativas y selección* más arriba.

**No respondió las consultas 2, 3 ni 4.** Quedan abiertas:

<!-- cols: 8,52,40 -->

| # | Consulta | Qué bloquea |
|---|---|---|
| 2 | ¿Vale declarar las líneas base como supuestos y poner su medición como entregable de la fase de Relevamiento? | **D3.** Los cuatro objetivos O1–O4 y el Acta, que ya los reproduce |
| 3 | ¿Gantt en meses relativos desde la aprobación del Acta, o fechas de calendario? | **D2 definitivo.** El diagrama de red, el Gantt y el aplanamiento (punto 10) |
| 4 | Fecha de entrega de la Etapa 3 | **RESUELTA fuera del documento: 28/08/2026** |

**Consulta nueva que surgió de su respuesta:** si las alternativas ahora son proyectos distintos, ¿se mantiene una matriz ponderada para justificar la selección, o alcanza con la justificación cualitativa y las otras dos solo mencionadas? Comparar proyectos incomparables con criterios de costo, tiempo e integración es forzado, y él mismo dijo que las otras dos no hace falta elaborarlas.

**Mensaje de seguimiento a enviar:**

> Gracias! Dos cosas para no equivocar el enfoque:
>
> 1. Con las alternativas como proyectos distintos, ¿mantenemos la matriz ponderada para justificar la selección, o alcanza con una justificación cualitativa y las otras dos solo mencionadas?
> 2. Nos quedaron tres consultas del documento sin responder: (a) las líneas base no están medidas — ¿vale declararlas como supuestos y poner su medición como entregable de la fase de Relevamiento?; (b) ¿acepta un Gantt en meses relativos desde la aprobación del Acta o pide fechas de calendario?; (c) ¿cuál es la fecha de entrega de la Etapa 3?

#### Dudas / pendientes

**Para el grupo:**

- **D3** es la única decisión abierta, y depende de la respuesta del docente del 2026-08-11.
- **D4 está cerrada por el grupo pero no validada por el docente.** Hasta que se valide, no conviene invertir tiempo en la EDT ni en el Acta: si voltea la alternativa, ese trabajo se tira.

**Datos que faltan:**

- **Fecha de entrega** de la Etapa 3.
- ~~Plantilla del Acta de Proyecto~~ — **conseguida el 2026-08-19**. Campos y ejemplo resuelto en Unidad 5 §6.
- ¿La cátedra acepta cronograma en **meses relativos** o pide fechas de calendario? (cierra D2)
- Fechas de corrección de la Etapa 2 para completar la tabla de versiones (inconsistencia I4).
- Archivo del **organigrama** de Personal (inconsistencia I6).

#### Fuentes

- `fuentes/ASI/ASI26_310_UNIDAD1.docx` — resolución Etapa 1 (v3, corregida).
- `fuentes/ASI/ASI26_310_UNIDAD2.docx` — resolución Etapa 2 (v1).
- `fuentes/ASI/fibraOpticaBPMN.png` y `fuentes/ASI/modeloPersonal.png` — BPMN del proceso (dos versiones).
- `fuentes/ASI/procesoInstacionFibraOptica.bpm` — archivo fuente Bizagi del BPMN.
- `fuentes/ASI/ASI26_TPIntegrador_Etapa3 - Proyecto de TI.md` — consigna Etapa 3.
- `fuentes/ASI/TPIntegrador - Etapa 3 - Practica Sugerencias.md` — sugerencias de cátedra 28/07/2026.
- `fuentes/ASI/Ejercitación/` — ejercitación de U5, plantilla del Acta de Proyecto y caso integral resuelto (Centro de Servicios), 19/08/2026. Desarrollado en Unidad 5.

Derivados que generamos (en esta misma carpeta, `materias/ASI/`):

- `ASI26_310_UNIDAD1_corregido.docx` — Etapa 1 con la corrección I5 aplicada.
- `ASI26_310_UNIDAD2_corregido.docx` — Etapa 2 con las correcciones I1 e I2 aplicadas.

## Log

- 2026-07-29: primer ingest completo de la materia. Se incorporó todo el Material de Cursado (Unidad 1 y Unidad 2), las resoluciones de las Etapas 1 y 2 del TPI, el BPMN del proceso, y la consigna + sugerencias de la Etapa 3. Se crearon las cuatro unidades del índice. Se detectaron 6 inconsistencias en lo ya entregado (ver sección TP Integrador) y se dejaron 3 candidatos de proyecto para la Etapa 3 a decidir.
- 2026-07-29: corregidas I1, I2 e I5 sobre copias nuevas (`ASI26_310_UNIDAD1_corregido.docx`, `ASI26_310_UNIDAD2_corregido.docx`). Verificado por reconversión y diff: solo cambiaron las 8 celdas previstas. Quedan pendientes I3 (decisión), I4 (falta dato de fechas) e I6 (falta archivo).
- 2026-07-29: documentada la Etapa 3 — comparación de los tres candidatos, desarrollo completo del candidato B (trazabilidad con Etapas 1 y 2, solución, alcance, 4 objetivos cuantificables, matriz de alternativas, ciclo de vida, 11 fases y 9 sectores de H&S), y las cinco decisiones abiertas D1–D5. **Preferencia por B declarada, sin cerrar.** Discusión con el grupo pendiente. Punto de retomada marcado al inicio de la sección Etapa 3.
- 2026-07-29: los dos `.docx` corregidos pasan a `materias/ASI/` como derivados, para que los tenga el grupo. Se subieron también las fuentes crudas a `fuentes/ASI/` (23 archivos).
- 2026-08-10: **cerradas D1, D2, D4 y D5.** Alcance = B medio · cronograma en meses relativos con plazo de O1 desde el go-live · alternativa = **A1 desarrollo interno** (con componentes de mercado acotados: mapas, MDM, dispositivos, infraestructura) · paralelismo obligatorio diseñado desde la EDT. La matriz de selección se rehízo contra los diez criterios que lista la cátedra en el Bloque 4 de las sugerencias: se sumaron *dependencia del proveedor* y *escalabilidad*, y se re-ponderaron los pesos justificándolos con R03 y R05 (severidad 15) de la Etapa 2 — sin tocar ningún puntaje. Resultado: Interno 4,00 · SaaS 3,60 · Tercerizado 3,50. En consecuencia se reformularon el ciclo de vida (el tramo iterativo queda mejor justificado), las fases (de 11 a 12: se parte "selección de proveedor" en *arquitectura y diseño técnico* + *adquisiciones*, y "diseño y configuración" pasa a *desarrollo por módulos*) y las adquisiciones (de licencias SaaS a hardware, infraestructura, mapas y MDM). Agregado el paquete de validación para la clase del 11/08. **Queda abierta D3** (líneas base), a consultar con el docente ese día.
- 2026-08-19: ingerida la carpeta `Ejercitación` (4 archivos) → `fuentes/ASI/Ejercitación/`. Aporta tres cosas que faltaban: **(1) la plantilla oficial del Acta de Proyecto** — desbloquea el punto 4.b de la Etapa 3, que estaba trabado desde el 29/07; **(2) el caso integral resuelto** (Centro de Servicios) — primer y único ejemplo resuelto de la unidad, con CPM completo (ES/EF/LS/LF, holguras, camino crítico `1→2→4→5→7→9`, duración 39 h, BAC $3.700); **(3) la ejercitación de U5**, que es más ancha que la Etapa 3 e incluye RFI ejecutado, RFP con 3 cotizaciones y TCO. Se agregaron a la Unidad 3: CPM y aplanamiento en §7, criterios de evaluación de proveedores y variables de TCO en §10, BAC y monetización de beneficios en §11, checklist legal e indicadores VAN/TIR/TPR en §12, la plantilla del Acta con ejemplo en §6, y el nuevo §13 con la tabla comparativa U5 vs. Etapa 3. La sección "Ejercicios resueltos tipo", que estaba vacía, ahora tiene el caso completo. **Dos hallazgos:** la cátedra numera esta unidad como **Unidad 5** (la wiki la llama Unidad 3), y falta el apunte teórico — el caso cita `ASI-5-T1` a `ASI-5-T5`, ninguno en nuestras fuentes.
- 2026-08-19: redactado el **borrador del Acta de Proyecto** (punto 4.b de la Etapa 3) en `materias/ASI/etapa3-acta-proyecto.md`, con su `.docx` generado por `scripts/build-docx.js` (conversor md→docx reutilizable: A4, Arial 11, justificado con partición es-AR, tablas con anchos por directiva `<!-- cols: … -->`, pie con numeración). Se instaló LibreOffice y `scripts/preview-docx.sh` para **ver el render** antes de dar por bueno un entregable — revisando a ciegas se habían colado listas con numeración encadenada, celdas justificadas con ríos y partición de palabras en inglés. El Acta quedó en 5 páginas. Trazabilidad completa hacia atrás: la justificación cita R04 y R07 sin tratamiento de la Etapa 2 y el objetivo de TI del 5% de la Etapa 1; los objetivos son O1–O4 con las líneas base declaradas como supuestos y su medición como entregable de la fase 2; el límite reproduce el "qué no incluye" acordado. Quedan por definir los nombres propios y el monto de autoridad de compra.
- 2026-08-19: ingerido el **campus completo** (`ASI_Apuntes_Campus`, 93 archivos). Se copiaron 28 a `fuentes/ASI/Campus/` — Unidades 3, 4 y 5 completas más Normas de Cátedra; se dejaron fuera los complementarios de U2 (NIST, MAGERIT, SEI), la U6, los exámenes finales y los duplicados de U1/U2 que ya estaban. **Reestructuración mayor de la wiki**: el Programa Analítico (Plan 2023) define **6 unidades**, no 3. La vieja "Unidad 3 — Proyectos de TI" pasó a ser **Unidad 5**, y se crearon **Unidad 3 (Dirección de Talento y Capital Humano)** y **Unidad 4 (Higiene y Seguridad Laboral)** — las dos que sostienen los puntos 5 y 6 de la Etapa 3 y que hasta ahora se venían respondiendo con conocimiento general. Se agregó también un stub de **Unidad 6 (Emprendedorismo)**. En la Unidad 5 se volcaron los cinco capítulos del apunte: definición formal de proyecto, tipos, portafolio/programa/subproyecto y triple restricción (T1); la **plantilla del Acta anotada campo por campo con el ejemplo ESABAL** y el contenido PMI del Acta de Constitución (T2); el esquema de nodo de la red, AON/AOA, el método completo de **histograma de recursos y aplanamiento**, y fast tracking vs. crashing (T3); y las **cuatro técnicas de evaluación de inversiones** TR/TPR/VAN/TIR con el valor del dinero en el tiempo (T4). **Hallazgo para el punto 6 de la Etapa 3:** los tres niveles de prevención de la Unidad 4 explican por qué la cátedra rechaza "silla ergonómica y pausas activas" — son prevención sobre la persona, el escalón más débil; el layout tiene que mostrar **prevención en el diseño**. Se sumó además la legislación laboral (Leyes 19.587, 24.557, 20.744 y 27.555), que le faltaba a la factibilidad legal.
- 2026-08-23: **el docente validó el punto 3** y redefinió el encuadre de las alternativas. Aprobó el proyecto y dio su formulación del nombre; indicó dejar **SaaS FSM configurable** como único modo de construcción —lo que revierte D4, cerrada por el grupo en desarrollo interno el 10/08— y pidió sumar una o dos **alternativas de TI que ataquen otro problema**, solo mencionadas. En consecuencia se reescribió el punto 3 con las alternativas como *proyectos distintos* (OT-Campo seleccionada · seguridad perimetral e identidades · capacidad y mantenimiento de planta externa), la matriz de construcción quedó archivada como respaldo, el ciclo de vida volvió a justificarse por configuración y adopción, las fases volvieron de 12 a 11 y las adquisiciones al perfil SaaS. Se actualizó el **Acta** (`Producto`, `Entregables`, autoridad de compra) y se creó **`materias/ASI/etapa3.md`**, el entregable consolidado que se sube a Drive a medida que se completa. **No respondió las consultas 2, 3 ni 4** (líneas base, meses relativos, fecha de entrega): D2 y D3 siguen abiertas y quedó redactado el mensaje de seguimiento.
- 2026-08-23: entregable consolidado generado. Se instaló **Node 24 LTS en la máquina Windows** y se corrió el conversor: `materias/ASI/etapa3.docx` (8 páginas) y `materias/ASI/etapa3-acta-proyecto.docx` (5 páginas), con sus PDF. El encabezado de `etapa3.md` se alineó al formato de las entregas de las Etapas 1 y 2 (UTN / CÁTEDRA / título / comisión y grupo / integrantes con legajo y email / tabla de versiones / índice). Se agregó `scripts/preview-docx.ps1`, equivalente Windows de `preview-docx.sh`: convierte con Word en vez de LibreOffice y rasteriza con pymupdf. **Fecha de entrega confirmada: 28/08/2026.** Ante las tres consultas sin responder, el grupo decidió: líneas base como supuestos con medición como entregable de la fase 2, cronograma en meses relativos, y justificación de la selección cualitativa sin matriz ponderada.
- 2026-08-23: **EDT completa** (punto 4.3). Once paquetes de primer nivel y **46 paquetes de trabajo**, cada uno con predecesora, duración en días hábiles, perfil y entregable verificable, en el formato que exige la cátedra. Se definieron los **nueve perfiles** (JP, AF, EI, ES, CP, UX, QA, CA, RO), que son el insumo directo del punto 5. El paralelismo de D5 quedó **diseñado dentro de la estructura, no agregado después**: cinco focos de solapamiento documentados —el analista funcional entre 2.2 y 2.4, el especialista de integraciones encadenado en 5.1 a 5.4 mientras 5.6 y 6.1 lo reclaman, el de seguridad entre el cierre de la fase 3 y 5.5/5.6, el consultor de plataforma en 4.6/4.7/5.1 y después en 8.3/10.1/11.1, y el referente de operaciones entre relevamiento, configuración y despliegue—. Son el insumo del análisis de sobreasignación del punto 10. El **Acta se embebió como Anexo I** dentro de `etapa3.md`: a la carpeta compartida sube un solo archivo y el Acta es entregable obligatorio del punto 4.b. Se corrigió también el título del Acta, que conservaba la formulación vieja, a la que dio el docente. Documento en **16 páginas**. Se arregló `scripts/preview-docx.ps1`, que fallaba porque `Join-Path` devuelve un PSObject y `SaveAs` de Word no lo acepta.
- 2026-08-23: **Etapa 3 completa, puntos 5 a 12.** Antes de redactar se calculó el **CPM real** sobre las 51 actividades de la EDT (pasada adelante y atrás, holguras, camino crítico): **187 días hábiles** a fechas tempranas, camino crítico de 30 actividades, y seis conflictos de sobreasignación. Se corrigieron dos fallas de modelado de la EDT: `2.4 medir líneas base` y `9.4 evaluar la capacitación` quedaban sin sucesor, con holguras irreales de 158 y 28 días; se les asignaron las dependencias que corresponden. El **aplanamiento** se resolvió comparando dos estrategias: nivelar con una persona por perfil lleva el proyecto a 215 días (+28), y reforzar con un segundo especialista de integraciones y un segundo responsable de pruebas lo deja en **192 días hábiles (~9,1 meses)**, que es la adoptada — un tercer refuerzo en RO solo bajaría a 189 y no se justifica. Esos números fijos alimentaron la redacción de los puntos 5 a 12.
- 2026-08-23: **detectada y corregida una inconsistencia grave entre los puntos 11 y 12.** El punto 11 había estimado sobre 220 técnicos, 260 usuarios licenciados y 240 dispositivos, y el punto 12 sobre 60 técnicos y 78 usuarios: cuatro veces de diferencia dentro del mismo documento. Se unificó sobre la cifra menor, que es la ya documentada para el alcance Gran Rosario, y se recalculó **todo** lo que colgaba de ella. Modelo único resultante: RRHH 3.456 h por USD 112.624 · adquisiciones y servicios año 1 USD 142.210 · costo directo USD 254.834 · **presupuesto año 1 USD 328.226** · **TCO a 3 años USD 531.460**. La evaluación económica se rehízo distinguiendo el presupuesto a autorizar (con contingencia) de la inversión que se descuenta (sin ella, por ser una previsión ante riesgo y no una erogación esperada): **VAN a 5 años al 15% = +USD 31.515 · TIR 19,0% · repago 3,14 años · umbral de indiferencia en el 85% de realización de beneficios**. El resultado es viable pero de margen estrecho, y así quedó escrito: a tres años el proyecto todavía no se repaga. Se corrigió también la sensibilidad, que con la dotación menor pasa de "los usuarios pesan 2,5 veces más que el valor hora" a que ambas variables pesan casi igual.
