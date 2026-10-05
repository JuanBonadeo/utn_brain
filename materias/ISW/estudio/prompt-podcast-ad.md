# Prompts para los podcasts de repaso — parcial de Aprobación Directa

Seis episodios, cada uno con **su propio PDF** en `podcast-ad/`, recortado del resumen
`resumen-ad.md` (57 págs.). Pensado para NotebookLM (Resumen de audio → Personalizar). Formato
sugerido: **Análisis en profundidad**, duración **Más larga**, idioma **Español**.

**Cómo usarlo.** Cargá los seis PDFs en un mismo cuaderno y, antes de generar cada episodio, dejá
tildada **sólo la fuente de ese episodio** (o armá un cuaderno por episodio). Pegá en el campo de
personalización el bloque completo del episodio; si el campo no lo acepta por largo, usá la versión
corta.

**Orden sugerido:** 1 → 2 → 3 → 4 → 5 → 6. Con poco tiempo: 1, 2 y 6. El 4 y el 5 cubren casi lo
mismo que el parcial de Regularización.

| Ep | Fuente | Capítulos del resumen | Págs. |
|---|---|---|---|
| 1 | `podcast-ad/ep1-requerimientos-cambios-configuracion.pdf` | 14, 15 y 20 | 10 |
| 2 | `podcast-ad/ep2-ppqa-medicion-pericias.pdf` | 21, 22 y 23 | 8 |
| 3 | `podcast-ad/ep3-proyecto-estimacion-riesgos.pdf` | 10 a 13 | 9 |
| 4 | `podcast-ad/ep4-verificacion-validacion-pruebas.pdf` | 16 a 19 | 12 |
| 5 | `podcast-ad/ep5-calidad-cmmi-procesos.pdf` | 2 a 9 | 13 |
| 6 | `podcast-ad/ep6-simulacro.pdf` | 1, 24, 25 y 26, más el anexo de preguntas de los AD | 10 |

Si el resumen cambia, los PDFs de los episodios hay que regenerarlos: son recortes por capítulo.

## Episodio 1 — Requerimientos, cambios y configuración

Fuente: `podcast-ad/ep1-requerimientos-cambios-configuracion.pdf` (capítulos 14, 15 y 20).

```text
Generá un podcast de repaso para un estudiante de 4.º año de Ingeniería en Sistemas (UTN) que rinde el parcial de Aprobación Directa de Ingeniería y Calidad de Software: opción múltiple, a libro abierto pero sólo en papel. Como va a tener el resumen impreso, no necesita memorizar listas: tiene que salir sabiendo razonar y decidir rápido —qué área de CMMI corresponde, si una práctica genera problemas de calidad y por qué, qué opción es una trampa—. Usá únicamente el documento cargado; no agregues temas que no estén ahí.

TONO Y FORMATO
- Español rioplatense, dos voces. Una explica; la otra hace de alumno que pregunta y cae en las confusiones típicas, para que la primera lo corrija.
- Para cada concepto: primero un ejemplo concreto, después la idea, después la trampa típica.
- Usá los nombres literales de las áreas, metas y prácticas de CMMI. La primera vez que aparezca una sigla, decí qué significa.
- Cada tanto, frená con una pregunta estilo parcial, dejá un segundo para pensar y respondé explicando el criterio, no sólo la respuesta.
- Sin introducciones largas ni relleno.

ESTE EPISODIO
Requerimientos, gestión de cambios y gestión de configuración: lo que más pesó en los parciales de Aprobación Directa.

Prioridad máxima (alrededor del 70 %):
1. El circuito de un cambio: RD produce los requisitos, REQM los gestiona, la solicitud de cambio la tramita CM y el resultado queda en una nueva línea base. El orden ante un cambio: registrar, evaluar el impacto con la matriz de trazabilidad, y recién después implementar.
2. REQM, RD o CM: ¿el requisito ya está acordado? ¿El cambio todavía se evalúa (REQM SP 1.3) o ya se decidió aceptarlo (CM SP 2.1)? ¿Altera un requisito o es un cambio técnico interno?
3. La línea base y por qué relaciona las versiones de los artefactos; versión, variante y release; los repositorios; el comité de control de cambios; las auditorías de configuración.
4. Qué va bajo configuración, incluidas las herramientas.

Prioridad media (alrededor del 30 %): tipos de requisitos (los no funcionales no son opcionales), la obtención y la puerta de calidad, las metas de RD y de REQM, la trazabilidad y los estados de una solicitud de cambio.

RESOLVÉ EN VOZ ALTA
La variante de descuento ("se está chequeando con el contador" frente a "ya se decidió aceptarla"), la pregunta del año 2002, cuántos releases tiene ALFA 3 con cuatro incrementos, la supervivencia del esquema de versión (24 años), el BP del versionado sin relación entre artefactos y el cliente que pide acceso móvil sin decir qué dispositivos.

CIERRE
Terminá con las tres o cuatro ideas más importantes del episodio, en formato "si en el examen ves X, pensá Y".
```

Versión corta (452 caracteres):

```text
Podcast de repaso en español rioplatense, parcial de opción múltiple a libro abierto: entrená a razonar y decidir, no a memorizar. Tema: requerimientos, cambios y configuración. Clave: REQM, RD o CM (¿se evalúa o ya se aceptó el cambio?), el orden ante un cambio, línea base, versión, variante y release. Resolvé en voz alta: año 2002, releases de ALFA 3, supervivencia de 24 años y el BP de versionado. Un host cae en las trampas y el otro lo corrige.
```

## Episodio 2 — Aseguramiento de la calidad, medición y pericias

Fuente: `podcast-ad/ep2-ppqa-medicion-pericias.pdf` (capítulos 21, 22 y 23).

```text
Generá un podcast de repaso para un estudiante de 4.º año de Ingeniería en Sistemas (UTN) que rinde el parcial de Aprobación Directa de Ingeniería y Calidad de Software: opción múltiple, a libro abierto pero sólo en papel. Como va a tener el resumen impreso, no necesita memorizar listas: tiene que salir sabiendo razonar y decidir rápido —qué área de CMMI corresponde, si una práctica genera problemas de calidad y por qué, qué opción es una trampa—. Usá únicamente el documento cargado; no agregues temas que no estén ahí.

TONO Y FORMATO
- Español rioplatense, dos voces. Una explica; la otra hace de alumno que pregunta y cae en las confusiones típicas, para que la primera lo corrija.
- Para cada concepto: primero un ejemplo concreto, después la idea, después la trampa típica.
- Usá los nombres literales de las áreas, metas y prácticas de CMMI. La primera vez que aparezca una sigla, decí qué significa.
- Cada tanto, frená con una pregunta estilo parcial, dejá un segundo para pensar y respondé explicando el criterio, no sólo la respuesta.
- Sin introducciones largas ni relleno.

ESTE EPISODIO
Aseguramiento de la calidad de proceso y de producto (PPQA), medición y análisis (MA) y pericias informáticas.

Prioridad máxima (alrededor del 75 %):
1. PPQA: objetividad e independencia; adherencia a estándares frente a cumplimiento de requerimientos (PPQA frente a VER); el ciclo de una no conformidad —resolverla en el proyecto, escalarla, seguirla hasta el cierre— y las tres formas de resolverla; cuándo termina una auditoría; el sector de SQA no es el área PPQA.
2. Los dos BP de SQA: en 2024 se escala a la misma gerencia de la que dependen los líderes de proyecto (falta independencia); en 2025 se archiva en el legajo del líder (falta escalamiento y seguimiento). Insistí en que la misma opción es correcta o no según el final del enunciado.
3. MA: primero alinear y después medir; métrica, medida e indicador; métricas de proceso, de proyecto y de producto con la regla para decidir; el uso inapropiado de los datos; el repositorio de medición de la organización es de OPD.

Repaso rápido (alrededor del 25 %): pericias. Imagen forense frente a backup, orden de volatilidad, hash y bloqueador de escritura, cadena de custodia, quién hace qué, y el equipo encendido según cada fuente.

RESOLVÉ EN VOZ ALTA
Los verdadero o falso sobre auditorías, qué indicadores salen del checklist de casos de uso, la clasificación de las cinco métricas del AD 2024 y qué afirmaciones son coherentes con MA.

CIERRE
Terminá con las tres o cuatro ideas más importantes del episodio, en formato "si en el examen ves X, pensá Y".
```

Versión corta (425 caracteres):

```text
Podcast de repaso en español rioplatense, parcial de opción múltiple a libro abierto: entrená a razonar y decidir. Tema: PPQA, medición y pericias. Clave: independencia de QA, ciclo de una no conformidad y escalamiento, los dos BP de SQA (2024 y 2025), métricas de proceso, proyecto y producto, uso inapropiado de datos. Breve: imagen forense, volatilidad, cadena de custodia. Un host cae en las trampas y el otro lo corrige.
```

## Episodio 3 — Proyecto, estimación, riesgos y ciclos de vida

Fuente: `podcast-ad/ep3-proyecto-estimacion-riesgos.pdf` (capítulos 10 a 13).

```text
Generá un podcast de repaso para un estudiante de 4.º año de Ingeniería en Sistemas (UTN) que rinde el parcial de Aprobación Directa de Ingeniería y Calidad de Software: opción múltiple, a libro abierto pero sólo en papel. Como va a tener el resumen impreso, no necesita memorizar listas: tiene que salir sabiendo razonar y decidir rápido —qué área de CMMI corresponde, si una práctica genera problemas de calidad y por qué, qué opción es una trampa—. Usá únicamente el documento cargado; no agregues temas que no estén ahí.

TONO Y FORMATO
- Español rioplatense, dos voces. Una explica; la otra hace de alumno que pregunta y cae en las confusiones típicas, para que la primera lo corrija.
- Para cada concepto: primero un ejemplo concreto, después la idea, después la trampa típica.
- Usá los nombres literales de las áreas, metas y prácticas de CMMI. La primera vez que aparezca una sigla, decí qué significa.
- Cada tanto, frená con una pregunta estilo parcial, dejá un segundo para pensar y respondé explicando el criterio, no sólo la respuesta.
- Sin introducciones largas ni relleno.

ESTE EPISODIO
Planificación y seguimiento de proyectos, estimación, gestión de riesgos y ciclos de vida.

Prioridad máxima (alrededor del 65 %):
1. PP frente a PMC: el momento decide (reunión futura o ya ocurrida). Las prácticas que más se preguntan: PP SP 1.2 (tamaño) frente a SP 1.4 (esfuerzo), SP 2.2 (riesgos), SP 2.3 (datos), SP 2.5 (formación del proyecto) y SP 2.6 (involucración de los interesados); PMC SG 2 según el tiempo verbal; el desvío significativo.
2. Riesgos: PP SP 2.2, PMC SP 1.3 o RSKM; identificar, analizar y priorizar, en ese orden; umbrales; mitigación frente a contingencia; aceptar y transferir según CMMI y según INTECO; las reservas.
3. Ciclos de vida: cuándo conviene cada uno; incremental, iterativo y espiral; en el incremental cada incremento es una cascada completa.

Prioridad media (alrededor del 35 %): esfuerzo frente a duración y camino crítico; los diez grupos de procesos (definir las actividades es de Alcance); puntos función: componentes, pesos, factor de ajuste (65 + TDI) / 100 y la medición de mejoras.

RESOLVÉ EN VOZ ALTA
El BP del plan de proyecto con sólo roles de la software factory (AD 2025), "informar que aumentó la probabilidad de un riesgo respecto de lo planificado", el cálculo con 200 PFD y un TDI de 42, y qué ciclo de vida elegir con requisitos poco claros.

CIERRE
Terminá con las tres o cuatro ideas más importantes del episodio, en formato "si en el examen ves X, pensá Y".
```

Versión corta (416 caracteres):

```text
Podcast de repaso en español rioplatense, parcial de opción múltiple a libro abierto: entrená a razonar y decidir. Tema: proyecto, estimación, riesgos y ciclos de vida. Clave: PP o PMC según el momento, tamaño (SP 1.2) frente a esfuerzo (SP 1.4), riesgos en PP, PMC o RSKM, mitigación frente a contingencia, ciclos de vida. Breve: esfuerzo y duración, puntos función. Un host cae en las trampas y el otro lo corrige.
```

## Episodio 4 — Verificación, validación y pruebas

Fuente: `podcast-ad/ep4-verificacion-validacion-pruebas.pdf` (capítulos 16 a 19).

```text
Generá un podcast de repaso para un estudiante de 4.º año de Ingeniería en Sistemas (UTN) que rinde el parcial de Aprobación Directa de Ingeniería y Calidad de Software: opción múltiple, a libro abierto pero sólo en papel. Como va a tener el resumen impreso, no necesita memorizar listas: tiene que salir sabiendo razonar y decidir rápido —qué área de CMMI corresponde, si una práctica genera problemas de calidad y por qué, qué opción es una trampa—. Usá únicamente el documento cargado; no agregues temas que no estén ahí.

TONO Y FORMATO
- Español rioplatense, dos voces. Una explica; la otra hace de alumno que pregunta y cae en las confusiones típicas, para que la primera lo corrija.
- Para cada concepto: primero un ejemplo concreto, después la idea, después la trampa típica.
- Usá los nombres literales de las áreas, metas y prácticas de CMMI. La primera vez que aparezca una sigla, decí qué significa.
- Cada tanto, frená con una pregunta estilo parcial, dejá un segundo para pensar y respondé explicando el criterio, no sólo la respuesta.
- Sin introducciones largas ni relleno.

ESTE EPISODIO
Verificación, validación y pruebas.

Prioridad máxima (alrededor del 65 %):
1. VER, VAL o PPQA: contra qué se contrasta y quién participa; la prueba de sistema es VER y la de aceptación es VAL; las revisiones entre pares existen sólo en VER, y la trampa de la sigla que vuelve correcta la opción NINGUNA; RD SP 3.5 frente a VAL.
2. De la actividad a la práctica: el tiempo verbal elige entre preparar, realizar y analizar.
3. Técnicas dinámicas: cómo elegir la técnica según el enunciado; particiones de equivalencia (la partición intermedia y que no se pisen); valores límite; los errores al traducir el enunciado ("superior a 65" empieza en 66, "mayor a cero" deja el 0 inválido); tablas de decisión; derivación de casos de prueba desde casos de uso con la matriz V/I.

Prioridad media (alrededor del 35 %): los niveles de prueba y a qué área corresponde cada uno; alfa, beta y piloto; regresión frente a confirmación; qué es probar según Myers y sus principios; los tipos de revisión y sus roles; el análisis estático.

RESOLVÉ EN VOZ ALTA
Los diagramas de conjuntos del AD 2025, qué se tiene en cuenta al definir casos de prueba desde las particiones (AD 2025), si unas pruebas internas sobre un prototipo son alfa, y el caso B = 0.

CIERRE
Terminá con las tres o cuatro ideas más importantes del episodio, en formato "si en el examen ves X, pensá Y".
```

Versión corta (407 caracteres):

```text
Podcast de repaso en español rioplatense, parcial de opción múltiple a libro abierto: entrená a razonar y decidir. Tema: verificación, validación y pruebas. Clave: VER, VAL o PPQA según contra qué se contrasta, sistema es VER y aceptación es VAL, revisiones entre pares sólo en VER, particiones, valores límite, tablas de decisión y casos desde casos de uso. Un host cae en las trampas y el otro lo corrige.
```

## Episodio 5 — Calidad, CMMI y gestión de procesos

Fuente: `podcast-ad/ep5-calidad-cmmi-procesos.pdf` (capítulos 2 a 9).

```text
Generá un podcast de repaso para un estudiante de 4.º año de Ingeniería en Sistemas (UTN) que rinde el parcial de Aprobación Directa de Ingeniería y Calidad de Software: opción múltiple, a libro abierto pero sólo en papel. Como va a tener el resumen impreso, no necesita memorizar listas: tiene que salir sabiendo razonar y decidir rápido —qué área de CMMI corresponde, si una práctica genera problemas de calidad y por qué, qué opción es una trampa—. Usá únicamente el documento cargado; no agregues temas que no estén ahí.

TONO Y FORMATO
- Español rioplatense, dos voces. Una explica; la otra hace de alumno que pregunta y cae en las confusiones típicas, para que la primera lo corrija.
- Para cada concepto: primero un ejemplo concreto, después la idea, después la trampa típica.
- Usá los nombres literales de las áreas, metas y prácticas de CMMI. La primera vez que aparezca una sigla, decí qué significa.
- Cada tanto, frená con una pregunta estilo parcial, dejá un segundo para pensar y respondé explicando el criterio, no sólo la respuesta.
- Sin introducciones largas ni relleno.

ESTE EPISODIO
Calidad, CMMI y gestión de procesos de la organización.

Prioridad máxima (alrededor del 65 %):
1. Componentes de un área de proceso: lo requerido son sólo las metas; las prácticas son esperadas; las genéricas tratan la institucionalización.
2. Niveles de madurez: cómo se reconoce cada uno; nivel 2 frente a 3 y 4 frente a 5; las reglas del modelo escalonado (si falla un área de nivel 2, la organización queda en nivel 1); las erratas de la traducción.
3. OPF, OPD y OT: "OPF diagnostica y despliega, OPD define y guarda, OT capacita"; OPF SG 2 frente a SG 3; repositorio de medición frente a biblioteca de activos; OT frente a PP SP 2.5.
4. Activo frente a producto de trabajo, y la trampa del NINGUNA.

Repaso rápido (alrededor del 35 %): definiciones de calidad, aseguramiento frente a control, tipos de mantenimiento (perfectivo no es evolutivo), principios de la ingeniería del software, SPEM y RUP.

RESOLVÉ EN VOZ ALTA
"Cumple todo el nivel 3 pero le falta MA", si una práctica crea un activo o lo despliega, y qué área verifica y almacena los productos de trabajo a nivel organizacional.

CIERRE
Terminá con las tres o cuatro ideas más importantes del episodio, en formato "si en el examen ves X, pensá Y".
```

Versión corta (420 caracteres):

```text
Podcast de repaso en español rioplatense, parcial de opción múltiple a libro abierto: entrená a razonar y decidir. Tema: calidad, CMMI y gestión de procesos. Clave: sólo las metas son requeridas, niveles de madurez y sus reglas, OPF diagnostica y despliega, OPD define y guarda, OT capacita, activo frente a producto de trabajo. Breve: calidad, mantenimiento, SPEM y RUP. Un host cae en las trampas y el otro lo corrige.
```

## Episodio 6 — Simulacro

Fuente: `podcast-ad/ep6-simulacro.pdf` (capítulos 1, 24, 25 y 26, más el anexo de preguntas de los AD).

```text
Generá un podcast de repaso para un estudiante de 4.º año de Ingeniería en Sistemas (UTN) que rinde el parcial de Aprobación Directa de Ingeniería y Calidad de Software: opción múltiple, a libro abierto pero sólo en papel. Como va a tener el resumen impreso, no necesita memorizar listas: tiene que salir sabiendo razonar y decidir rápido —qué área de CMMI corresponde, si una práctica genera problemas de calidad y por qué, qué opción es una trampa—. Usá únicamente el documento cargado; no agregues temas que no estén ahí.

TONO Y FORMATO
- Español rioplatense, dos voces. Una explica; la otra hace de alumno que pregunta y cae en las confusiones típicas, para que la primera lo corrija.
- Para cada concepto: primero un ejemplo concreto, después la idea, después la trampa típica.
- Usá los nombres literales de las áreas, metas y prácticas de CMMI. La primera vez que aparezca una sigla, decí qué significa.
- Cada tanto, frená con una pregunta estilo parcial, dejá un segundo para pensar y respondé explicando el criterio, no sólo la respuesta.
- Sin introducciones largas ni relleno.

ESTE EPISODIO
Un simulacro del parcial. Casi todo el episodio son preguntas: planteá cada pregunta del anexo y cada par de áreas que se confunden, dale al alumno un momento, y resolvé aplicando el método.

1. El método de cinco preguntas para reconocer el área de proceso en un enunciado, y los pares de áreas que se confunden.
2. El método de las preguntas BP: buscar el eslabón que falta, evaluar cada razón por separado, la regla de no mezclar el "sí" con el "no", lo que no es un problema y los distractores que se repiten.
3. Todas las preguntas reales de los AD 2024 y 2025 del anexo, con su criterio.

Recordá que en el parcial marcar una opción incorrecta además de la correcta deja la pregunta en cero.

CIERRE
Terminá con las tres o cuatro ideas más importantes del episodio, en formato "si en el examen ves X, pensá Y".
```

Versión corta (397 caracteres):

```text
Simulacro en español rioplatense de un parcial de opción múltiple a libro abierto. Casi todo preguntas: planteá cada pregunta del anexo de los AD 2024 y 2025 y cada par de áreas que se confunden, dejá pensar y resolvé con el método: cinco preguntas para reconocer el área, y para los BP, el eslabón que falta y no mezclar el sí con el no. Un host responde y cae en las trampas; el otro lo corrige.
```
