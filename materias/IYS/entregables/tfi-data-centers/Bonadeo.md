---
codigo: IYS
materia: Ingeniería y Sociedad
tipo: Trabajo Final Integrador
titulo: La nube tiene territorio
subtitulo: Infraestructura de cómputo para inteligencia artificial en la Patagonia argentina — análisis crítico de un proceso ingenieril en curso (2024-2026)
comision: IC 01
fecha: 22/09/2026

profesores:
  - Vanina López
---

## 1. Introducción

Existe una metáfora que la industria del software repite hasta volverla invisible: *la nube*. La palabra sugiere algo liviano, disperso, sin peso ni lugar. Cada vez que un usuario guarda un archivo, entrena un modelo o le hace una pregunta a un asistente conversacional, el vocabulario le indica que eso ocurre en ninguna parte.

Ocurre en algún lado. Ocurre en galpones refrigerados, conectados a líneas de alta tensión, construidos sobre un terreno concreto, en una provincia concreta, bajo una legislación concreta. La infraestructura de cómputo es, tal vez, el punto donde la ingeniería en sistemas deja de ser una disciplina simbólica y se vuelve obra civil, consumo eléctrico y negociación política. Es también el punto donde las decisiones técnicas que toma un ingeniero dejan de tener consecuencias únicamente técnicas.

Este trabajo analiza el proceso de instalación de centros de datos de gran escala orientados a inteligencia artificial en la Argentina, con foco en el proyecto **Stargate Argentina** —anunciado en octubre de 2025 por OpenAI y la empresa argentina Sur Energy— y en el marco normativo que lo habilita. Se lo aborda desde cuatro dimensiones —tecnológica, ambiental, política y social— y se lo interpreta con las herramientas conceptuales trabajadas en la materia: el esquema de olas de Alvin Toffler y el análisis de la sociedad de hiperconsumo de Gilles Lipovetsky.

La tesis que se sostiene es la siguiente: **el proceso presenta todos los rasgos discursivos de la Tercera Ola —conocimiento, desmaterialización, economía de la información— mientras reproduce, en su estructura económica concreta, la lógica de enclave extractivo propia de la Segunda**. Y que esa tensión no es una contradicción del discurso, sino el modo específico en que la Tercera Ola llega a un país periférico.

## 2. Elección del proceso y argumentación

### 2.1 El proceso seleccionado

Se seleccionó el **diseño, emplazamiento y puesta en operación de centros de datos de alta densidad para cargas de trabajo de inteligencia artificial**. No se trata de un producto sino de un proceso ingenieril completo, que involucra: selección de sitio en función de variables climáticas y energéticas; diseño eléctrico y de redundancia; ingeniería térmica de refrigeración; arquitectura de red y conectividad internacional; y operación bajo métricas de eficiencia.

### 2.2 Por qué este proceso

**Primero, por pertinencia disciplinar directa.** La carrera de Ingeniería en Sistemas de Información forma profesionales que escriben software que se ejecuta en algún lugar. Durante la mayor parte de la formación, ese lugar es una abstracción: se habla de «servidores», «instancias» o «la nube» sin que el plan de estudios obligue a preguntar dónde están, con qué energía funcionan y quién los regula. Elegir este proceso es, deliberadamente, hacer visible el sustrato material de la propia práctica profesional.

**Segundo, por su condición de proceso en curso y no resuelto.** A diferencia de un caso histórico cerrado, este proceso se está decidiendo mientras se escribe este trabajo: el marco normativo que lo regularía —el denominado «Súper RIGI»— obtuvo media sanción en la Cámara de Diputados en junio de 2026 y se debatía en el Senado en septiembre del mismo año. Analizar un proceso abierto obliga a un tipo de rigor distinto: no hay desenlace conocido que permita acomodar retrospectivamente el análisis.

**Tercero, porque condensa las cuatro dimensiones sin forzarlas.** Un centro de datos de 500 MW es simultáneamente un problema de ingeniería térmica, un problema de matriz energética y uso del agua, un problema de régimen fiscal y soberanía jurisdiccional, y un problema de expectativas de empleo y desarrollo regional. Pocos objetos técnicos permiten recorrer las cuatro dimensiones con la misma densidad de evidencia.

**Cuarto, por la posición del ingeniero en él.** Es un proceso en el que el profesional de sistemas no es espectador: es quien dimensiona la carga, quien elige la arquitectura de refrigeración, quien decide qué se almacena dónde. La pregunta por la responsabilidad profesional tiene aquí un referente concreto, no retórico.

## 3. Marco de referencia, ubicación temporal y territorial

### 3.1 La temática que enmarca el proceso

El proceso se inscribe en una temática mayor: **la reconfiguración material de la economía de la información**. Durante tres décadas, el relato dominante sobre la informática fue el de la desmaterialización: menos papel, menos traslado, menos consumo físico. El ciclo abierto por los modelos de lenguaje de gran escala invierte esa tendencia. El entrenamiento y la inferencia de estos modelos son intensivos en cómputo, y el cómputo es intensivo en electricidad y en disipación de calor. La economía de la información descubre, tardíamente, que tiene una huella física creciente.

Ese descubrimiento reorganiza geografías. La localización de un centro de datos ya no se decide por cercanía al usuario —la latencia importa poco para entrenar un modelo— sino por tres variables: **energía abundante y barata, clima frío y estabilidad jurídica de largo plazo**. Países que no eran relevantes en la cadena de valor del software pasan a serlo por razones que no tienen nada que ver con el software: porque tienen gas, viento o baja temperatura media.

### 3.2 Ubicación temporal

El recorte temporal adoptado es **2024-2026**, con proyección declarada hasta 2027. Los hitos que lo estructuran:

- **Julio de 2024**: se publica la Ley 27.742, «Ley de Bases y Puntos de Partida para la Libertad de los Argentinos», que crea el Régimen de Incentivo para Grandes Inversiones (RIGI), con beneficios fiscales, aduaneros y cambiarios por 30 años para proyectos superiores a USD 200 millones. Se reglamenta por Decreto 749/2024 en agosto del mismo año.
- **Octubre de 2025**: OpenAI y Sur Energy firman una carta de intención para desarrollar *Stargate Argentina*, un proyecto de hasta 500 MW y una inversión declarada de hasta USD 25.000 millones.
- **Junio de 2026**: la Cámara de Diputados aprueba con 130 votos afirmativos el proyecto conocido como «Súper RIGI», orientado específicamente a infraestructura digital, inteligencia artificial y centros de datos.
- **Agosto de 2026**: por Resolución 202/2026 de la Secretaría de Energía se lanza la licitación AMBA I, dentro de un programa de 16 obras de transporte eléctrico que contempla más de 5.610 km de líneas y una inversión de USD 6.600 millones.
- **Septiembre de 2026**: el Súper RIGI se debate en el Senado. El oficialismo acepta dos modificaciones para destrabar el dictamen: un piso de contratación de proveedores nacionales y la obligación, para quienes instalen centros de datos, de construir sus propias subestaciones eléctricas.
- **2027 (proyectado)**: entrada en operación de la primera etapa de 100 MW.

Es importante señalar el estado real de avance: a junio de 2026, ocho meses después del anuncio, el progreso público del proyecto era limitado, y la propia empresa lo caracterizaba como un proceso complejo y de largo plazo. **Lo que se analiza aquí es, en rigor, un proceso anunciado y parcialmente normado, no una obra ejecutada.** Esa distinción es parte del análisis, no una limitación de él.

### 3.3 Ubicación territorial

El territorio en disputa es la **Patagonia argentina**, con las provincias de **Neuquén, Río Negro y Chubut** como candidatas principales, y el **AMBA** como localización histórica de la capacidad instalada existente.

Las razones del desplazamiento hacia el sur son técnicas y se detallan en la sección 5.1, pero conviene adelantarlas: temperaturas medias anuales de entre 5 y 12 °C que habilitan refrigeración por aire exterior durante buena parte del año; potencial eólico e hidroeléctrico de alta capacidad; y proximidad al gas de Vaca Muerta como respaldo firme. En paralelo, Pampa Energía impulsa un centro de datos en Neuquén, contiguo a su central térmica de Loma de la Lata, con un consumo proyectado de hasta 500 MW.

El contraste con la capacidad existente es el dato más elocuente del proceso (Tabla 1).

**Tabla 1.** Capacidad instalada de centros de datos: Argentina y comparación regional (2026)

<!-- cols: 34,22,44 -->

| Localización | Capacidad (MW) | Observación |
|---|---|---|
| Argentina (total, 13 centros de más de 1 MW) | 32 | 71 % concentrado en CABA (23 MW) |
| Proyecto Stargate Argentina (declarado) | 500 | Multiplicaría por ~16 la capacidad nacional actual |
| São Paulo, Brasil | 536,7 | Principal mercado regional |
| Querétaro, México | 298,2 | Crecimiento de 450,2 % en doce meses |
| Santiago, Chile | 165,8 | — |
| Bogotá, Colombia | 44,3 | — |

*Fuente: elaboración propia sobre datos de AgendAR (2026). Nota metodológica: distintas fuentes reportan la capacidad argentina entre 32 MW y cifras cercanas a 75 MW según el umbral de tamaño considerado, por lo que el multiplicador varía entre ~7 y ~16 veces. Se adopta aquí la serie más conservadora respecto del denominador.*

La Tabla 1 permite dimensionar lo que está en discusión: **un solo proyecto privado propone una capacidad de cómputo un orden de magnitud superior a toda la infraestructura nacional acumulada**, y comparable al principal polo regional. No se trata de una ampliación incremental de capacidad existente, sino de la creación de una infraestructura sin precedente local, con las asimetrías de negociación que eso implica.

## 4. Marco teórico: los ejes de la materia

### 4.1 Toffler y el análisis del frente de ola

Toffler (1980) propone leer la historia como la superposición de olas de cambio civilizatorio que corren a velocidades distintas y chocan entre sí. La Segunda Ola —la civilización industrial— organizó la producción según seis principios: estandarización, especialización, sincronización, concentración, maximización y centralización. La Tercera Ola —la sociedad de la información— desplazaría ese código: el conocimiento reemplazaría al capital y a la fuerza como palanca principal de poder, la producción se desmasificaría y el trabajo se desanclaría del espacio fabril.

El aporte metodológico más útil de Toffler no es su cronología sino su indicación de dónde mirar: el **frente de ola**, la línea donde una civilización que se retira roza a otra que avanza. Este trabajo toma esa indicación al pie de la letra y sostiene que el centro de datos de IA es, hoy, uno de esos frentes.

También se retoma la crítica estándar al autor, que resulta operativa para el análisis: su **determinismo tecnológico**, que presenta a la tecnología como motor autónomo; y el efecto de **naturalización** que produce su metáfora, ya que una ola no tiene autor, intención ni responsables a quienes reclamar.

### 4.2 Lipovetsky y la demanda que sostiene la infraestructura

Lipovetsky (2007) distingue tres fases del capitalismo de consumo y caracteriza la actual —la sociedad de hiperconsumo— por el desplazamiento del consumo distintivo, dirigido a los otros, hacia un consumo emocional y experiencial orientado a uno mismo. La figura del **turboconsumidor** —desregulado, nómade, infiel— describe a un sujeto que consume servicios de modo continuo, personalizado y bajo demanda.

La conexión con este proceso es directa y suele pasarse por alto: **la infraestructura que se analiza existe porque existe esa demanda**. Un modelo de lenguaje disponible las veinticuatro horas, que responde en segundos, gratuito o por suscripción baja, personalizado y sin fricción, es exactamente el tipo de servicio que el hiperconsumo vuelve esperable. Los 500 MW proyectados son la contracara material de un patrón de consumo que se experimenta como inmaterial.

## 5. Las cuatro dimensiones del proceso

### 5.1 Dimensión tecnológica

**El problema de ingeniería.** Un centro de datos de IA no es un centro de datos tradicional con más equipos. La diferencia es la **densidad de potencia por rack**: mientras un rack convencional de servicios web disipa entre 5 y 10 kW, un rack de aceleradores para entrenamiento de modelos puede superar los 40-100 kW. Esa densidad rompe el paradigma de refrigeración por aire forzado y empuja hacia refrigeración líquida directa al chip. El problema ingenieril central deja de ser el cómputo y pasa a ser **la disipación del calor**.

**Por qué la Patagonia.** De ahí se desprende la lógica de emplazamiento. Con temperaturas medias anuales de entre 5 y 12 °C, buena parte del año puede operarse con *free cooling*: enfriar las salas con aire exterior en lugar de comprimir refrigerante mediante compresores eléctricos. Esto tiene dos efectos acoplados: reduce el consumo eléctrico destinado a refrigeración —que en un centro de datos convencional puede representar entre el 30 % y el 40 % del total— y **reduce drásticamente el consumo de agua**, porque evita o limita el uso de torres de enfriamiento evaporativo.

Este punto merece subrayarse porque contradice el argumento ambiental más difundido: en el caso específico patagónico, la crítica por consumo de agua es considerablemente más débil que en emplazamientos de clima cálido o árido como Querétaro o Santiago. El análisis crítico exige reconocerlo.

**El cuello de botella real.** La restricción dominante no es de generación sino de **transporte**. La red eléctrica argentina llegó a 2026 con excedente de recurso —gas, hidráulica, viento, sol— y déficit de línea de 500 kV. La Patagonia enfrenta congestión de transmisión justamente donde el recurso abunda. Es un problema clásico de ingeniería de sistemas: el cuello de botella no está donde está el recurso ni donde está la demanda, sino en el vínculo entre ambos.

La respuesta del proyecto Stargate es significativa: asociarse a parques eólicos y solares propios y **operar sin depender de la red nacional**. Técnicamente es una solución elegante. Políticamente, como se verá, significa otra cosa.

### 5.2 Dimensión ambiental

**Energía.** La demanda eléctrica de los centros de datos a escala global pasó de aproximadamente 448 TWh en 2025 a una proyección de 565 TWh para 2026, con estimaciones de 945 TWh hacia 2030; el segmento de servidores de IA crece a un ritmo cercano al 84 % interanual (AgendAR, 2026). Si el conjunto de centros de datos del mundo fuera un país, se ubicaría alrededor del undécimo puesto en consumo eléctrico mundial.

En términos locales: 500 MW de demanda continua equivalen, en orden de magnitud, al consumo residencial de una ciudad intermedia argentina. La pregunta ambiental relevante no es si ese consumo es grande —lo es— sino **con qué se lo abastece y a costa de qué usos alternativos**.

**Agua.** Las estimaciones globales para 2025 sitúan el consumo hídrico asociado a IA entre 312.500 y 764.600 millones de litros anuales, con proyecciones que llegan a cifras muy superiores. Aquí corresponde una advertencia metodológica que el propio trabajo debe asumir: **varias de las cifras de consumo de agua más difundidas periodísticamente tienen trazabilidad débil**, y han sido cuestionadas por reconstruir estimaciones a partir de fuentes secundarias poco sólidas. Un análisis riguroso no puede usarlas como si fueran mediciones. Lo que sí puede afirmarse con solidez es que el consumo es material, creciente, y que su magnitud depende críticamente del sistema de refrigeración elegido —lo cual devuelve el problema al terreno de la decisión ingenieril.

**Emisiones.** Las estimaciones para 2025 ubican las emisiones asociadas a sistemas de IA alojados en centros de datos entre 32,6 y 79,7 millones de toneladas de CO₂.

**La tensión de fondo.** Si el proyecto se abastece de eólica y solar patagónica, su huella de carbono directa es baja. Pero la energía renovable que consume un centro de datos privado es energía renovable que no descarboniza otro consumo del sistema. En un país con una matriz eléctrica fuertemente dependiente del gas, **el costo ambiental no es la emisión del centro de datos: es el costo de oportunidad de la renovable que se le asigna**. Esta es una distinción que el debate público argentino rara vez hace.

### 5.3 Dimensión política

**El régimen de incentivos.** El RIGI (Ley 27.742, 2024) ofrece estabilidad fiscal, aduanera y cambiaria por **30 años** a proyectos de más de USD 200 millones. El «Súper RIGI» debatido en 2026 extiende y especializa ese esquema para infraestructura digital e inteligencia artificial.

Treinta años es un horizonte que conviene dimensionar: excede ampliamente la vida útil del equipamiento que se instalaría —los aceleradores de IA se renuevan en ciclos de tres a cinco años— y abarca aproximadamente siete períodos presidenciales. **Se otorga estabilidad de tres décadas a una tecnología cuyo horizonte de obsolescencia es de un lustro.** La asimetría entre el plazo del beneficio y el plazo del activo es, en sí misma, un objeto de análisis.

**Lo que el Senado discutió.** Las dos modificaciones aceptadas en septiembre de 2026 son reveladoras de qué estaba efectivamente en juego. La primera: que un 20 % de la contratación con proveedores nacionales se limite a bienes efectivamente **producidos** en Argentina —es decir, el reconocimiento explícito de que «proveedor nacional» podía significar simplemente un importador local. La segunda: obligar a quienes instalen centros de datos a **construir sus propias subestaciones eléctricas**, para no trasladar al sistema el riesgo de interrupción. Ambas enmiendas son, leídas de cerca, admisiones de las dos debilidades principales del esquema original.

**Soberanía de datos: la promesa más frágil.** El argumento de que alojar datos en territorio nacional otorga soberanía sobre ellos no resiste el examen jurídico. La **Cloud Act** estadounidense habilita al gobierno de los Estados Unidos a requerir datos en poder de empresas sujetas a su jurisdicción con independencia del país donde estén físicamente almacenados. Un centro de datos operado por una empresa estadounidense en Neuquén no produce soberanía de datos: produce **localización física de datos bajo jurisdicción extranjera**. Son cosas distintas y la diferencia es sustantiva.

A esto se suma el estado del marco local. La Ley 25.326 de Protección de Datos Personales, sancionada en 2000, le valió a la Argentina la declaración de nivel adecuado de protección por parte de la Unión Europea, pero cumplió veinticinco años sin reforma integral. Existen al menos tres proyectos en danza —impulsados por los legisladores Carro, Doñate y Yeza, este último bajo el expediente 1751-D-2026, que deroga expresamente la ley vigente—, con incorporación de principios de *accountability*, privacidad por diseño, portabilidad, derecho de oposición a decisiones automatizadas y, en el caso del último, tratamiento explícito del entrenamiento de sistemas con datos públicos. **El país discutiría recibir la mayor infraestructura de IA de la región con una ley de datos anterior a la existencia de las redes sociales.**

### 5.4 Dimensión social

**La promesa de empleo y la evidencia.** Es el punto donde la brecha entre lo anunciado y lo documentado es mayor, y donde la evidencia comparada es más contundente (Tabla 2).

**Tabla 2.** Promesas de empleo declaradas frente a empleo efectivamente registrado

<!-- cols: 26,16,29,29 -->

| Caso | País | Promesa declarada | Registro efectivo |
|---|---|---|---|
| Microsoft | México | 20.000 empleos indirectos | 17 personas empleadas (2024) |
| Meta | Suecia | 30.000 puestos | 56 personas contratadas |
| AWS (3 centros) | España | — | ~100 personas en total |
| Promedio sectorial | — | — | 25 a 150 permanentes por centro; 30 a 50 en instalaciones *hyperscale* |

*Fuente: elaboración propia sobre Chequeado (2026) y AgendAR (2026).*

La explicación no es el incumplimiento sino la **naturaleza técnica del activo**: un centro de datos es una instalación altamente automatizada, monitoreada de manera remota, cuya dotación permanente se concentra en mantenimiento, refrigeración, electricidad y seguridad física. El empleo intensivo existe, pero es **temporal y de construcción**.

Lo notable es que esta caracterización no proviene únicamente de la crítica externa. El propio desarrollador del proyecto lo formuló sin eufemismos:

> «Un data center de IA no es una fuente de empleo para la Argentina. Es una fuente de dólares.»
> — Emiliano Kargieman, fundador de Satellogic y de Sur Energy (*La Nación*, 7 de diciembre de 2025).

Desde la crítica política, la objeción apunta al modelo antes que a la cifra: «Convertirnos en un enclave de data centers no es bueno para la Argentina» (Grabois, en *Infobae*, 18 de septiembre de 2026).

**La composición real de la inversión.** El segundo desajuste está en la cifra de inversión. Del gasto total de un centro de datos, aproximadamente un **62 % corresponde a hardware y software importado**, cerca de un 25 % a energía y refrigeración, y apenas un **15 % a construcción y terrenos** (Chequeado, 2026). Es decir: de los USD 25.000 millones anunciados, la porción que efectivamente circula en la economía local es una fracción menor del titular. Una inversión nominada en dólares no es lo mismo que una inversión que ocurre en el país.

**Brecha y distribución.** Un último efecto social documentado en la experiencia comparada es el aumento de los costos eléctricos para la población local cuando grandes consumidores se incorporan a un sistema con infraestructura de transporte saturada. Si el proyecto opera efectivamente aislado de la red —como se anunció—, ese riesgo se mitiga; pero el aislamiento tiene, como se verá, su propio costo conceptual.

## 6. Análisis crítico integrador

### 6.1 El data center como frente de ola

Si se aplica el método de Toffler y se busca la línea donde una civilización roza a otra, el centro de datos de IA en la Patagonia es un frente de ola casi de manual. Pero lo es de una forma que el autor no anticipó, y que invierte su propio esquema.

Toffler sostiene que la Tercera Ola **desmasifica, descentraliza y desconcentra**. El centro de datos hace exactamente lo contrario. Reúne el cómputo del mundo en instalaciones gigantescas, lo concentra geográficamente donde la energía es barata, lo estandariza en racks idénticos, lo sincroniza en ciclos de entrenamiento continuos y lo maximiza en escala. Vale la pena enunciarlo de manera directa: **el centro de datos cumple, uno por uno, los seis principios del código de la Segunda Ola que Toffler daba por superados** —estandarización, especialización, sincronización, concentración, maximización y centralización—, sólo que aplicados a la producción de información en lugar de a la de bienes.

La Tercera Ola no disolvió la fábrica. La rebautizó. Y la construyó lejos.

### 6.2 La fábrica invisible del hiperconsumo

Aquí converge el segundo eje. Lipovetsky describe un consumidor que accede a servicios personalizados, inmediatos y continuos, y que experimenta ese acceso como una relación consigo mismo —con su productividad, su bienestar, su curiosidad— antes que como una transacción económica. Ese es, exactamente, el modo en que se usa un asistente de IA.

El punto crítico es el siguiente: **el hiperconsumo de servicios digitales funciona porque su infraestructura es invisible**. Ningún usuario que consulta un modelo de lenguaje percibe los megavatios involucrados. La experiencia está diseñada para no tener peso, y ese diseño no es un accidente: la fricción cero es el producto. Toffler describió al usuario de la Tercera Ola como *prosumidor*, productor y consumidor a la vez; lo que muestra este proceso es que la producción efectiva se concentró en un galpón patagónico mientras el consumo se distribuyó globalmente y se volvió emocional.

En ese sentido, el par Toffler-Lipovetsky funciona mejor combinado que por separado. Toffler explica la estructura productiva; Lipovetsky explica **por qué existe la demanda que la justifica**. La infraestructura que este trabajo analiza no se construye por un imperativo técnico: se construye porque un patrón de consumo la vuelve rentable.

### 6.3 Tercera Ola en el discurso, Segunda Ola en la estructura

La tesis central del trabajo puede ahora formularse con precisión. El proyecto se presenta con el vocabulario íntegro de la Tercera Ola: conocimiento, innovación, transformación digital, inserción en la economía global. Su estructura económica, en cambio, responde a un patrón que la Argentina conoce bien: **capital extranjero, recurso natural local, beneficio fiscal de largo plazo, escaso empleo permanente, insumos importados, valor agregado producido en otra jurisdicción**. Es la descripción de un enclave.

Tres indicadores lo confirman. Primero, la composición de la inversión: el 62 % es equipamiento importado, de modo que la mayor parte del capital anunciado nunca circula localmente. Segundo, la decisión de operar al margen de la red eléctrica nacional: técnicamente razonable, pero simbólicamente decisiva, porque un enclave se define precisamente por su desconexión de la trama productiva que lo rodea. Tercero, la asimetría temporal del beneficio: treinta años de estabilidad para activos que se renuevan cada cinco.

La Tabla 3 sintetiza las cuatro dimensiones bajo esta clave.

**Tabla 3.** Síntesis de las cuatro dimensiones analizadas

<!-- cols: 16,42,42 -->

| Dimensión | Lo que se afirma en el discurso | Lo que muestra la evidencia |
|---|---|---|
| Tecnológica | Salto a la frontera tecnológica global | Infraestructura de alta densidad cuyo problema central es térmico y de transporte eléctrico; el diseño es global, el emplazamiento es local |
| Ambiental | Energía limpia, clima frío, bajo impacto | Impacto hídrico efectivamente menor por *free cooling*; el costo real es el de oportunidad de la renovable asignada, en una matriz aún dependiente del gas |
| Política | Soberanía digital e inserción estratégica | Localización física bajo jurisdicción extranjera (Cloud Act); ley de datos de 2000 sin reforma; estabilidad fiscal por 30 años |
| Social | Miles de empleos y desarrollo regional | 25 a 150 empleos permanentes; el empleo intensivo es temporal y de obra; 62 % de la inversión es importación |

*Fuente: elaboración propia.*

### 6.4 Una objeción al propio análisis

Un trabajo crítico debe someter a crítica también su propia posición. La conclusión anterior admite al menos tres objeciones serias, y omitirlas sería deshonesto.

**Primera: el enclave puede ser preferible a la nada.** Si el proyecto genera divisas genuinas y financia infraestructura de transmisión que de otro modo no se construiría, su balance puede ser positivo aun con empleo directo bajo. La comparación relevante no es contra un escenario ideal de desarrollo endógeno, sino contra el escenario de que la inversión se radique en Chile o Brasil.

**Segunda: la crítica ambiental es más débil de lo que suele afirmarse.** Buena parte del discurso crítico importa argumentos sobre consumo de agua formulados para emplazamientos en zonas áridas. En la Patagonia, el *free cooling* modifica sustantivamente ese cálculo. Sostener un argumento por inercia retórica, cuando la evidencia técnica local lo debilita, es un error metodológico.

**Tercera: la capacidad de cómputo instalada tiene valor estratégico propio.** Aun siendo un enclave, la existencia de infraestructura de cómputo de escala en el territorio modifica las condiciones de posibilidad de la investigación y el desarrollo locales. Es un argumento débil respecto de lo prometido, pero no es nulo.

Lo que estas objeciones no alcanzan a revertir es el problema de fondo: **ninguna de ellas depende de decisiones técnicas, y todas dependen de decisiones normativas que se están tomando ahora**. El contenido de la ley determina si el proyecto es un enclave o el inicio de una cadena de valor. Y esa es, precisamente, la conclusión que interpela a la ingeniería.

### 6.5 El lugar del ingeniero

La crítica más productiva que puede hacerse a Toffler es que su metáfora naturaliza: una ola no tiene autor ni intención, y por lo tanto no admite reclamo. Pero un centro de datos sí tiene autor. Alguien dimensiona la carga térmica. Alguien decide si la refrigeración es evaporativa o de circuito cerrado. Alguien define si el almacenamiento se replica en una jurisdicción o en otra. Alguien escribe el pliego técnico de la subestación que el Senado terminó exigiendo por ley.

Cada una de esas decisiones es una decisión de ingeniería con consecuencias ambientales, jurídicas y sociales directas. **La oposición entre «lo técnico» y «lo político» no describe este proceso: lo oculta.** El ingeniero en sistemas que trabaja en infraestructura de IA no es un observador del frente de ola; es uno de los agentes que determinan de qué lado cae.

Esto no supone que el profesional deba asumir responsabilidades que corresponden al Estado o a la empresa. Supone algo más acotado y más exigible: que la formación profesional incluya la capacidad de identificar cuándo una decisión presentada como técnica está resolviendo, de hecho, un problema distributivo.

## 7. Aportes de la entrevista

### 7.1 El entrevistado y la modalidad

Se entrevistó a **Mateo**, ingeniero de software que se desempeña como desarrollador *backend* en una empresa de software de la ciudad de Rosario, con cuatro a cinco años de experiencia profesional. Su trabajo actual se centra en integraciones complejas entre sistemas, diseño de arquitecturas, automatización de procesos y bases de datos. A pedido del entrevistado, se omite el nombre de la empresa.

La entrevista se realizó en forma oral y fue grabada con su autorización. El entrevistado recibió previamente las preguntas de la versión breve del guion (Anexo I) y las respondió en una intervención continua. La transcripción se obtuvo con una herramienta de reconocimiento de voz, fue revisada contra el audio y editada para su lectura. Figura completa en el Anexo II.

Corresponde explicitar el alcance del material. Se trata de **una sola entrevista**, a un profesional de desarrollo y no de infraestructura física, por lo que no es representativa del sector: funciona como testimonio de la práctica cotidiana, no como evidencia estadística. Por otra parte, algunas afirmaciones —en particular el ejemplo de la sección 7.5— son de segunda mano según el propio entrevistado («rascando un poco en los pasillos») y se consignan como tales.

### 7.2 «Para mí es una IP»: la infraestructura invisible en la práctica

La primera respuesta confirma de manera casi literal la hipótesis de la sección 6.2. Consultado sobre si piensa dónde está físicamente el servidor cuando despliega una aplicación, el entrevistado respondió:

> «Uno casi nunca piensa dónde está el servidor. [...] Para mí es una IP, o un servicio en un desplegable. [...] Pero la imagen del galpón gigante en el medio de la nada, lleno de cables y ventiladores, ni se te cruza por la cabeza.»

El pasaje muestra que la desmaterialización no es solo un rasgo de la experiencia del consumidor final que describe Lipovetsky: se extiende a quienes construyen el software. La geografía reaparece únicamente cuando se vuelve un problema operativo —latencia— o jurídico —el entrevistado menciona la normativa europea de protección de datos, que obliga a alojar datos en Europa—. Fuera de esos casos, la decisión se reduce a «plata y latencia» o a «lo que ya estaba configurado en el proyecto».

La respuesta sobre el impacto ambiental es todavía más tajante:

> «Del impacto ambiental, nada. Literalmente nada. Jamás se habla de eso en una planning. La única vez que se habla de “consumo” es cuando llega el resumen de la tarjeta con los costos de la nube a fin de mes [...]. Como no ves el humo salir de la notebook, parece que la nube es mágica.»

Esta observación se conecta con la sección 5.2. El costo energético no está ausente del trabajo del desarrollador: **está presente, pero traducido a dólares y mezclado en una factura**. La única señal material que llega al equipo es monetaria, y por lo tanto la única pregunta que se hace es cómo pagar menos, no qué se consume.

### 7.3 El precio como anestesia: IA y costo de cómputo

La respuesta sobre las herramientas de inteligencia artificial resulta especialmente útil para el cruce con Lipovetsky de la sección 6.2:

> «Yo sé, porque lo leés por ahí, que entrenar esos modelos gasta muchísima plata y muchísima energía, pero como a mí en la API me cobran un par de centavos por unos miles de tokens, mi cerebro no hace la conexión con el gasto energético que hay detrás de la preguntita más tonta que le acabo de hacer.»

El entrevistado identifica con precisión el mecanismo que el trabajo describe en términos teóricos. La información existe —«lo leés por ahí»—, pero el precio unitario ínfimo y la fricción nula desconectan el acto de consumo de su soporte material. Es la lógica del hiperconsumo aplicada al cómputo: un servicio experimentado como inmaterial, disponible a cualquier hora, cuyo costo real queda fuera de la percepción de quien lo usa. En este caso, además, quien lo usa es un profesional que sabe perfectamente que ese costo existe.

### 7.4 El proyecto patagónico visto desde el sector

Sobre el proyecto Stargate Argentina, el entrevistado expresó una ambivalencia que reproduce el eje de la sección 6.3:

> «Como ingeniero, obviamente te entusiasma que pongan infraestructura de ese calibre acá. Pero te entra la duda [...]: ¿vienen porque les interesa desarrollar la región y buscar talento, o vienen solamente porque hace muchísimo frío y se ahorran millones en aire acondicionado para enfriar las máquinas?»

Y sobre las condiciones para que la inversión signifique algo para quienes hacen software en el país:

> «Si vienen, ponen los servidores, los encierran con alambre de púas y el mantenimiento lo hacen de forma remota desde Silicon Valley, a nosotros nos da exactamente igual. Tendría que venir con convenios con las facultades y puestos de infraestructura pesada a nivel local. Si no, es humo.»

La imagen del alambre de púas y el mantenimiento remoto describe, en lenguaje coloquial, lo que la literatura denomina **economía de enclave**: una instalación desconectada de la trama productiva que la rodea. La coincidencia con la evidencia de la Tabla 2 —pocos empleos permanentes, operación monitoreada a distancia— es completa. La propuesta del entrevistado —convenios con universidades y puestos técnicos locales— coincide también con la tercera objeción de la sección 6.4: el valor de la infraestructura depende de las condiciones de acceso que se negocien, no del edificio en sí.

### 7.5 La responsabilidad, entre la teoría y la trinchera

La respuesta sobre la responsabilidad profesional es la que más tensiona el argumento del trabajo, y por eso es la más valiosa:

> «En la teoría te digo que sí, obviamente deberíamos hacernos cargo. Pero en la trinchera, en el día a día, estás corriendo, tenés que cerrar el sprint, te apuran para que no se caiga producción... ¿qué vas a estar pensando en la huella de carbono de un `while`? Eso se decide en otro nivel, más arriba.»

La sección 6.5 sostiene que el ingeniero no es un observador del proceso sino uno de sus agentes. El testimonio no refuta esa afirmación, pero le agrega una condición que el trabajo no había considerado con suficiente peso: **la organización del trabajo produce activamente la separación entre lo técnico y lo político**. El sprint, la urgencia de producción y las métricas de entrega no dejan espacio para la pregunta por las consecuencias. La responsabilidad existe, pero se ejerce dentro de condiciones que no la favorecen.

El entrevistado agrega un matiz revelador: el código más eficiente consume menos recursos, pero «no lo hacés por el planeta, lo hacés para que no explote el servidor». Cuando la eficiencia energética ocurre, ocurre como efecto colateral de un incentivo económico, no como objetivo.

Finalmente, ante la pregunta por decisiones presentadas como técnicas que escondían otra cosa, relató un caso que ilustra con precisión la crítica a Toffler planteada en la sección 4.1:

> «Te la venden como “vamos a migrar todo a una arquitectura serverless porque es la vanguardia técnica, súper moderno, escala solo”. [...] Después, rascando un poco en los pasillos, te enterás de que en realidad querían despedir a dos chicos de infraestructura para achicar sueldos y necesitaban que la nube se manejara sola. [...] Muchas veces disfrazamos de “modernización” o “buenas prácticas” lo que es puramente recortar gastos operativos.»

El ejemplo es, a escala de una empresa, el mismo mecanismo que el trabajo identifica a escala nacional. El vocabulario de la vanguardia tecnológica —la «ola» que llega, lo moderno, lo que «escala solo»— presenta como necesidad técnica lo que es una decisión con costo humano y con responsables concretos. La crítica a la metáfora toffleriana, según la cual una ola no tiene autor, encuentra aquí un caso de la práctica profesional: la modernización tampoco despide a nadie; alguien decide despedir y la modernización le da el lenguaje. Cabe reiterar que el propio entrevistado presenta este caso como información obtenida de manera informal, por lo que se lo toma como ilustración del mecanismo y no como un hecho verificado.

## 8. Conclusiones

**Primera.** El proceso analizado invierte el pronóstico de Toffler. La Tercera Ola no desconcentró la producción: concentró el cómputo del mundo en instalaciones que reproducen íntegramente el código de la Segunda Ola. La fábrica no desapareció; cambió de insumo y de localización.

**Segunda.** Esa infraestructura no responde a un imperativo técnico autónomo sino a un patrón de consumo. La sociedad de hiperconsumo que describe Lipovetsky —acceso continuo, personalizado, sin fricción y experimentado como inmaterial— es la condición de demanda que vuelve rentables los 500 MW. La invisibilidad de la infraestructura no es un efecto colateral del diseño: es parte del producto.

**Tercera.** En el caso argentino, el proceso presenta la forma de un enclave: alta inversión nominal con 62 % de contenido importado, empleo permanente en el orden de decenas de puestos, beneficios fiscales por treinta años sobre activos que se renuevan cada cinco, y operación proyectada al margen de la red nacional. El discurso corresponde a la Tercera Ola; la estructura, a un patrón de inserción que el país ya recorrió con otros recursos.

**Cuarta.** El análisis crítico obliga a matizar dos argumentos habituales. El ambiental, porque el *free cooling* patagónico debilita efectivamente la objeción por consumo de agua —el costo relevante es el de oportunidad de la energía renovable asignada—. Y el de soberanía, que no se refuta por débil sino al revés: es **más grave** de lo que suele plantearse, porque la localización física de los datos no produce soberanía jurídica mientras rijan marcos extraterritoriales como la Cloud Act y siga vigente una ley de datos de 2000.

**Quinta y principal.** La diferencia entre que este proceso sea un enclave o el punto de partida de una capacidad tecnológica nacional no se juega en el terreno técnico. Se juega en el contenido del marco normativo que se estaba discutiendo mientras se escribía este trabajo. Esa constatación, lejos de excluir a la ingeniería, la interpela: porque los pliegos, los dimensionamientos y las arquitecturas que traducen una ley en una obra los escriben ingenieros. Sostener que se trata de decisiones meramente técnicas es, en este proceso, la manera más eficaz de no hacerse cargo de ellas.

**Sexta.** La entrevista realizada agrega una condición que el análisis documental no alcanzaba a ver: la separación entre lo técnico y lo político no es solo un error conceptual de los ingenieros, sino un producto de la organización del trabajo. Donde la única señal material que llega a un equipo es la factura mensual de la nube, y donde el tiempo se mide en *sprints*, la pregunta por las consecuencias no tiene lugar en la agenda. Hacerse cargo de las decisiones técnicas exige, por lo tanto, algo más que voluntad individual: exige que esas consecuencias entren en las métricas con las que se evalúa el trabajo.

## 9. Referencias bibliográficas

AgendAR. (2026, 28 de julio). *Argentina tiene hoy 13 data centers: 32 megavatios. El proyecto Stargate, solo, plantea 500*. https://agendarweb.com.ar/2026/07/28/argentina-tiene-hoy-13-data-centers-32-megavatios-el-proyecto-stargate-solo-plantea-500/

AgendAR. (2026, 28 de agosto). *Data centers: posibles impactos del boom de la IA en nuestro territorio y nuestra sociedad*. https://agendarweb.com.ar/2026/08/28/data-centers-posibles-impactos-del-boon-de-la-ia-en-nuestro-territorio-y-nuestra-sociedad/

Chequeado. (2026). *Data centers en América Latina: por qué las promesas de las big techs no coinciden con la evidencia*. https://chequeado.com/investigaciones/data-centers-en-america-latina-por-que-las-promesas-de-las-big-techs-no-coinciden-con-la-evidencia/

Chequeado. (2026). *Mega data centers de IA: cómo se regulan en América Latina y Europa y qué puede pasar en Argentina*. https://chequeado.com/el-explicador/mega-data-centers-de-ia-como-se-regulan-en-america-latina-y-europa-y-que-puede-pasar-en-argentina/

El Economista. (2026). *La red eléctrica argentina: sobra recurso, falta cable*. https://eleconomista.com.ar/energia/la-red-electrica-argentina-sobra-recurso-falta-cable-n97926

Honorable Congreso de la Nación Argentina. (2024). *Ley 27.742. Ley de Bases y Puntos de Partida para la Libertad de los Argentinos*. Boletín Oficial de la República Argentina, 8 de julio de 2024.

Honorable Congreso de la Nación Argentina. (2000). *Ley 25.326. Protección de los Datos Personales*. Boletín Oficial de la República Argentina.

Lipovetsky, G. (2007). *La felicidad paradójica. Ensayo sobre la sociedad de hiperconsumo*. Barcelona: Anagrama. (Obra original publicada en 2006).

Poder Ejecutivo Nacional. (2024). *Decreto 749/2024. Reglamentación del Régimen de Incentivo para Grandes Inversiones*. Boletín Oficial de la República Argentina, 23 de agosto de 2024.

Secretaría de Energía de la Nación. (2026). *Resolución 202/2026. Licitación AMBA I — Programa de obras de transporte eléctrico*.

Toffler, A. (1980). *La tercera ola*. Barcelona: Plaza & Janés.

*La Nación*. (2025, 7 de diciembre). Kargieman, E.: «Un data center de IA no es una fuente de empleo para la Argentina. Es una fuente de dólares». *Conversaciones de Domingo*.

*Infobae*. (2026, 18 de septiembre). Grabois, J.: «Convertirnos en un enclave de data centers no es bueno para la Argentina».

## 10. Anexo I — Guion de entrevista

**Perfil buscado:** profesional del desarrollo de software con experiencia en despliegue de aplicaciones en infraestructura de nube.

**Modalidad:** entrevista semiestructurada, con registro de audio previa autorización expresa del entrevistado.

**Consentimiento (leer antes de iniciar el registro):** *«Esta entrevista forma parte de un trabajo final de la materia Ingeniería y Sociedad de la carrera de Ingeniería en Sistemas de Información (UTN). El audio será transcripto e incorporado como anexo del trabajo, de uso exclusivamente académico. ¿Autorizás la grabación? ¿Preferís que tu nombre o el de tu empresa figuren, o que se consignen de forma anónima?»*

### Bloque A — Trayectoria y contexto

1. ¿Podrías contarme brevemente tu formación y tu trayectoria profesional hasta hoy?
2. ¿En qué tipo de proyectos trabajás actualmente y qué rol ocupás en ellos?
3. ¿Cuánto hace que trabajás con infraestructura en la nube?

### Bloque B — La infraestructura como objeto cotidiano

4. Cuando desplegás una aplicación, ¿en qué momento del proceso —si en alguno— pensás dónde está físicamente el servidor?
5. ¿Quién decide, en tu experiencia real, la región de despliegue? ¿Qué criterios pesan: latencia, costo, cumplimiento normativo, costumbre?
6. ¿Alguna vez un requerimiento legal o de residencia de datos condicionó una decisión técnica tuya? ¿Cómo se resolvió?
7. ¿Se discute en tu entorno de trabajo el costo energético o la huella ambiental de lo que se despliega? Si no, ¿por qué creés que no aparece?

### Bloque C — IA, cómputo y escala

8. ¿Cómo cambió tu trabajo con la incorporación de herramientas de IA en los últimos años?
9. ¿Tenés dimensión del costo de cómputo detrás de las herramientas de IA que usás a diario? ¿Es algo visible para el desarrollador o está completamente abstraído?
10. Desde tu experiencia, ¿el modelo de suscripción cambió la forma en que se diseñan los productos de software? ¿En qué se nota?

### Bloque D — El proceso argentino

11. ¿Seguiste el anuncio del proyecto de centro de datos de IA en la Patagonia? ¿Qué te pareció?
12. En tu opinión profesional, ¿qué tendría que pasar para que una inversión así signifique algo concreto para alguien que hace software en Argentina?
13. Hay una diferencia importante entre alojar datos en el país y tener soberanía sobre esos datos. ¿Cómo se ve eso desde adentro de la industria?
14. ¿Creés que cambiaría algo de tu trabajo cotidiano si existiera capacidad de cómputo de gran escala en el país?

### Bloque E — Rol profesional y cierre

15. ¿Te parece que un ingeniero en sistemas tiene responsabilidad sobre las consecuencias sociales o ambientales de lo que construye, o eso corresponde a otro nivel de decisión?
16. ¿Hubo en tu carrera alguna decisión que se presentó como puramente técnica y que, mirada con distancia, era en realidad una decisión de otro tipo?
17. ¿Qué le dirías a un estudiante de cuarto año sobre lo que la facultad no enseña de este oficio?
18. ¿Querés agregar algo que no te haya preguntado?

### Versión breve aplicada

Para facilitar la participación del entrevistado, el guion completo se condensó en ocho preguntas, que se le enviaron por escrito antes de la grabación junto con una presentación del tema del trabajo:

1. Cuando desplegás una aplicación, ¿en algún momento pensás dónde está físicamente el servidor? ¿O es algo que nunca te planteaste?
2. ¿Quién decide en la práctica en qué región o proveedor se despliega, y con qué criterio? ¿Costo, latencia, alguna norma, o lo que ya venía configurado?
3. ¿Se habla en tu trabajo del consumo de energía o del impacto ambiental de lo que se despliega? Si no se habla, ¿por qué te parece que no aparece?
4. ¿Cómo cambió tu trabajo con las herramientas de IA en estos años? ¿Tenés idea del costo de cómputo que hay detrás cada vez que las usás?
5. ¿Viste algo del anuncio del data center de IA en la Patagonia? ¿Qué te parece?
6. ¿Qué tendría que pasar para que una inversión así signifique algo concreto para alguien que hace software acá?
7. ¿Te parece que alguien que hace software tiene responsabilidad por las consecuencias sociales o ambientales de lo que construye, o eso se decide en otro nivel?
8. ¿Te acordás de alguna decisión en el trabajo que se presentó como «puramente técnica» y que en realidad escondía otra cosa, como costos, personas afectadas o prioridades del negocio?

Se le solicitó además una breve presentación profesional y su preferencia sobre la identificación en el trabajo.

**Notas para el entrevistador:** no inducir la respuesta en las preguntas 11 a 13, que son las de mayor riesgo de sesgo; repreguntar siempre por casos concretos cuando la respuesta sea general («¿te acordás de alguna situación puntual?»); registrar silencios y dudas, que suelen ser informativos; y anotar la hora de los pasajes salientes para facilitar la desgrabación.

## 11. Anexo II — Desgrabación de la entrevista

**Entrevistado:** Mateo, ingeniero de software (desarrollador *backend*) en una empresa de software de Rosario. Se omite el nombre de la empresa a pedido del entrevistado.
**Experiencia:** cuatro a cinco años de trabajo profesional.
**Modalidad:** oral, grabada con autorización del entrevistado.
**Fecha:** 22 de septiembre de 2026.
**Nota sobre la transcripción:** el entrevistado recibió previamente las ocho preguntas de la versión breve del guion (Anexo I) y las respondió en una intervención continua. La transcripción se obtuvo con una herramienta de reconocimiento de voz y fue revisada contra el audio. Se presenta una **transcripción editada**: se suprimieron muletillas, repeticiones y expresiones malsonantes, y se ajustó la puntuación, sin agregar ni modificar el contenido de lo dicho. Los encabezados entre corchetes, que indican a qué pregunta corresponde cada tramo, se agregaron para facilitar la lectura y no forman parte de la grabación.

---

**[Presentación e identificación]**

Para la presentación en el trabajo, podés ponerme como Mateo, no hay problema, pero preferiría que no figure la empresa. Poné «desarrollador backend de una empresa de software de Rosario» o algo así; después recursos humanos se complica si nombrás a la empresa sin pedir permiso. Hoy estoy trabajando como ingeniero de software, sobre todo en integraciones complejas, armando arquitecturas, automatizando procesos y con bases de datos. Trabajando de esto de manera profesional, hace unos cuatro o cinco años.

**[Pregunta 1 — Ubicación física del servidor]**

Te soy sincero: uno casi nunca piensa dónde está el servidor. Cuando levantás algo, hacés un deploy o armás un flujo enorme para integrar un CRM, para mí es una IP, o un servicio en un desplegable. Elegís `us-east`, en Virginia, o `sa-east`, en San Pablo, pero más que nada por un tema de latencia, para que la request responda más rápido. Pero la imagen del galpón gigante en el medio de la nada, lleno de cables y ventiladores, ni se te cruza por la cabeza.

**[Pregunta 2 — Quién decide y con qué criterio]**

Lo de quién decide viene atado a eso. En la práctica es plata y latencia. Lo define el arquitecto o el líder técnico junto con la gente de negocio. Si AWS o Google Cloud te cobran menos en un lado, vas ahí directo. Salvo que tengas clientes en Europa: ahí sí, por la GDPR o esas leyes de protección de datos, te obligan a tener los servidores físicamente allá. Pero si no hay un tema legal de por medio, vamos a lo más barato o a lo que ya estaba configurado en el proyecto.

**[Pregunta 3 — Impacto ambiental en el trabajo]**

Del impacto ambiental, nada. Literalmente nada. Jamás se habla de eso en una planning. La única vez que se habla de «consumo» es cuando llega el resumen de la tarjeta con los costos de la nube a fin de mes y se quieren matar, o si un proceso te comió toda la memoria y se te cae todo. Como no ves el humo salir de la notebook, parece que la nube es mágica. Esa charla no existe en el trabajo diario.

**[Pregunta 4 — Herramientas de IA y costo de cómputo]**

Las herramientas de IA me cambiaron la vida, cien por ciento. Hoy le paso un JSON de tres mil líneas que no me parsea y le digo «encontrame dónde rompe», o la uso de pato de goma cuando estoy quemado a las tres de la mañana tratando de arreglar un bug. Pero del costo de cómputo real de hacer eso, ni idea. Yo sé, porque lo leés por ahí, que entrenar esos modelos gasta muchísima plata y muchísima energía, pero como a mí en la API me cobran un par de centavos por unos miles de tokens, mi cerebro no hace la conexión con el gasto energético que hay detrás de la preguntita más tonta que le acabo de hacer.

**[Pregunta 5 — El data center en la Patagonia]**

Lo del data center en la Patagonia lo vi en las noticias, lo leí por arriba. Como ingeniero, obviamente te entusiasma que pongan infraestructura de ese calibre acá. Pero te entra la duda —justo lo hablábamos el otro día en el club, después de jugar un partido de pádel—: ¿vienen porque les interesa desarrollar la región y buscar talento, o vienen solamente porque hace muchísimo frío y se ahorran millones en aire acondicionado para enfriar las máquinas? Y la energía acá seguramente la negocian muy barata.

**[Pregunta 6 — Qué haría falta para que impacte localmente]**

Para que nos sirva a los que hacemos software acá, tendrían que armar ecosistema y transferir conocimiento. Si vienen, ponen los servidores, los encierran con alambre de púas y el mantenimiento lo hacen de forma remota desde Silicon Valley, a nosotros nos da exactamente igual. Tendría que venir con convenios con las facultades y puestos de infraestructura pesada a nivel local. Si no, es humo.

**[Pregunta 7 — Responsabilidad del desarrollador]**

Sobre nuestra responsabilidad: en la teoría te digo que sí, obviamente deberíamos hacernos cargo. Pero en la trinchera, en el día a día, estás corriendo, tenés que cerrar el sprint, te apuran para que no se caiga producción... ¿qué vas a estar pensando en la huella de carbono de un `while`? Eso se decide en otro nivel, más arriba. Igual, como somos medio obsesivos con la optimización, si hacés un código más limpio y más performante, de rebote consumís menos CPU y menos energía. Pero seamos honestos: no lo hacés por el planeta, lo hacés para que no explote el servidor.

**[Pregunta 8 — Decisiones técnicas que esconden otra cosa]**

¿Decisiones técnicas que escondían otra cosa? Sí, mil veces. Me acuerdo de una: te la venden como «vamos a migrar todo a una arquitectura *serverless* porque es la vanguardia técnica, súper moderno, escala solo». Y vos decís: qué visión. Después, rascando un poco en los pasillos, te enterás de que en realidad querían despedir a dos chicos de infraestructura para achicar sueldos y necesitaban que la nube se manejara sola. O que habían cerrado un acuerdo comercial con el proveedor de cloud y les daban créditos gratis. Muchas veces disfrazamos de «modernización» o «buenas prácticas» lo que es puramente recortar gastos operativos. Es así.
