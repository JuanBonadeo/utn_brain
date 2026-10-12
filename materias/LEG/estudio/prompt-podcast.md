# Prompts para el podcast de repaso — 2do parcial de Legislación

Fuente: `resumen-2do-parcial.pdf` (unidades 4, 5 y 6). Pensado para NotebookLM (Resumen de audio →
Personalizar). Formato sugerido: **Análisis en profundidad**, duración **Más larga**, idioma
**Español**.

Hay dos opciones:
- **Un solo episodio** que repasa las tres unidades. Sirve para una vuelta general.
- **Tres episodios**, uno por unidad, cargando el mismo PDF y cambiando el prompt. Entran en más detalle.

Si el campo de personalización no acepta el texto largo, usá la versión corta.

## Episodio único — las tres unidades

```text
Generá un podcast de repaso para un estudiante de 4.º año de Ingeniería en Sistemas (UTN) que rinde el 2do parcial de Legislación: escrito, con preguntas a desarrollar y casos. Entran tres unidades: derechos intelectuales (U4), derecho laboral (U5) y ejercicio profesional (U6). Usá únicamente el documento cargado; no agregues normas ni datos que no estén ahí.

TONO Y FORMATO
- Español rioplatense, dos voces. Una explica; la otra hace de alumno que pregunta, se confunde en lo típico y es corregido.
- Para cada tema: primero un caso concreto (en lo posible del mundo del software), después la regla y el artículo, después la trampa.
- Nombrá siempre la norma y el número de artículo; en el escrito se pide citarlos.
- Los artículos no se piden de memoria: se piden ejemplos. Cuando aparezca un artículo marcado, decí qué regula y da tres ejemplos.
- Cada tanto, frená con una pregunta estilo parcial, dejá un segundo para pensar y respondela como se respondería por escrito.
- Sin introducciones largas ni relleno.

CONTENIDO, EN ESTE ORDEN
1. U4 (alrededor del 25 %): derechos personales, reales e intelectuales; propiedad industrial vs. intelectual; patentes, modelos de utilidad, diseños y marcas con requisitos y plazos; ley de patentes arts. 6 y 7 (qué no es invención vs. qué no es patentable); ley de marcas arts. 2 y 3 (qué no es marca vs. qué está prohibido); ley 11.723: qué protege, el software, titulares, obra en colaboración vs. colectiva, 70 años.
2. U5 (alrededor del 40 %): primero los cambios de la Ley 27.802 (período de prueba según el tamaño de la empresa, presunción del art. 23 con factura, propinas). Después: dependencia y sus tres formas, contrato vs. relación, deberes y facultades, invenciones y software del trabajador (art. 82 LCT), ius variandi, modalidades, jornada y horas extra, vacaciones, enfermedad inculpable, remunerativo vs. no remunerativo, suspensiones, preaviso, despido e indemnización.
3. U6 (alrededor del 35 %): responsabilidad civil y sus cuatro presupuestos, con el profesional liberal (art. 1768) y el principal por el dependiente (art. 1753); el Colegio de Ingenieros Especialistas: carácter, distritos, autoridades, matriculación, ejercicio profesional y firma personal (Estatuto arts. 4 a 10), inhabilitados, causales y tipos de sanción, Tribunal de Ética y su composición, y los actos contrarios a la ética por ámbito (Código, art. 6). Remarcá la regla: donde la ley y el Estatuto se repiten, vale el Estatuto.

RESOLVÉ EN VOZ ALTA
- Quién es dueño de un software hecho por un empleado, en tres versiones: en su casa y por su cuenta, contratado para programarlo, derivado de los sistemas de la empresa.
- Un programador monotributista que factura a una sola empresa y cumple horario: ¿hay contrato de trabajo después de la reforma?
- Despido sin causa ni preaviso con 6 años y 4 meses de antigüedad: qué se paga.
- Un ingeniero que firma una auditoría que no hizo: responsabilidad civil y falta ética.
- Un matriculado que le presta la firma a un técnico sin título.

CIERRE
Terminá con las cinco ideas que más conviene llevar al escrito, en formato "si te preguntan X, respondé con Y y citá el artículo Z".
```

Versión corta (470 caracteres):

```text
Podcast de repaso en español rioplatense, dos voces (una explica, otra pregunta y se confunde), para el 2do parcial escrito de Legislación (UTN, Sistemas). Sólo con el documento. Cubrí U4 derechos intelectuales, U5 laboral con los cambios de la Ley 27.802 y U6 responsabilidad civil y Colegio de Ingenieros (ley, Estatuto, Código de Ética). Para cada tema: caso concreto, regla con su artículo y tres ejemplos. Frená con preguntas de parcial y cerrá con las ideas clave.
```

## Episodio 1 — Unidad 4: derechos intelectuales

```text
Generá un podcast de repaso para un estudiante de Ingeniería en Sistemas (UTN) que rinde el 2do parcial escrito de Legislación. Este episodio cubre sólo la Unidad 4, derechos intelectuales (capítulo 2 del documento). Usá únicamente el documento cargado.

TONO Y FORMATO
- Español rioplatense, dos voces: una explica, la otra pregunta y cae en las confusiones típicas.
- Caso concreto primero, después la regla con su artículo, después la trampa.
- Los artículos se piden con ejemplos: para cada artículo marcado, decí qué regula y da tres ejemplos.
- Frená cada tanto con una pregunta estilo parcial y respondela como por escrito.

CONTENIDO
1. Derechos extrapatrimoniales y patrimoniales; personales vs. reales (sujeto pasivo, entre partes o frente a todos, quién los crea); dónde entran los intelectuales.
2. Propiedad industrial vs. intelectual: la aplicación industrial como criterio.
3. Patente, modelo de utilidad, diseño industrial y marca: qué protegen, requisitos y plazos.
4. Ley de patentes: art. 6 (no es invención) vs. art. 7 (es invención pero no es patentable), con tres ejemplos de cada uno. Por qué el software no se patenta.
5. Ley de marcas: art. 1 (qué se puede registrar), art. 2 (no es marca) vs. art. 3 (prohibido), con tres ejemplos de cada uno.
6. Ley 11.723: qué protege (la expresión, no la idea), facultades del autor, titulares (incluido el software hecho por empleados), obra en colaboración vs. colectiva, plazo de 70 años.

CIERRE
Las cuatro distinciones que no hay que confundir en el escrito, en formato "si ves X, es Y".
```

## Episodio 2 — Unidad 5: derecho laboral

```text
Generá un podcast de repaso para un estudiante de Ingeniería en Sistemas (UTN) que rinde el 2do parcial escrito de Legislación. Este episodio cubre sólo la Unidad 5, derecho laboral (capítulo 3 del documento y las preguntas de la guía de lectura del capítulo 5). Usá únicamente el documento cargado.

TONO Y FORMATO
- Español rioplatense, dos voces: una explica, la otra pregunta y se confunde con lo que cambió en la reforma.
- Caso concreto primero (en lo posible, un trabajador de una empresa de software), después la regla con su artículo.
- Números exactos: plazos, porcentajes, días.
- Frená cada tanto con una pregunta de la guía de lectura y respondela como por escrito.

CONTENIDO
1. Qué cambió con la Ley 27.802: concepto de trabajo, presunción del art. 23 con factura o pago bancario, nuevas exclusiones, período de prueba según el tamaño de la empresa, propinas, banco de horas, vacaciones fraccionadas, certificados médicos.
2. Trabajo dependiente: qué queda afuera, las tres subordinaciones, contrato vs. relación, elementos esenciales, sujetos.
3. Deberes y facultades de cada parte; invenciones y software del trabajador (art. 82 LCT y art. 4 inc. d de la 11.723); ius variandi y despido indirecto.
4. Modalidades, período de prueba, jornada diurna, nocturna e insalubre, horas extra y sus recargos.
5. Vacaciones, licencias, enfermedad inculpable, maternidad.
6. Remuneración: clasificación, SAC, remunerativo vs. no remunerativo, beneficios sociales.
7. Suspensiones y sus topes, preaviso, formas de extinción, indemnización por antigüedad y liquidación final.

RESOLVÉ EN VOZ ALTA
El programador monotributista con horario fijo; la analista despedida a los 6 meses en una empresa de 40 empleados; el traslado a una sucursal sin cubrir el viaje; el despido con 6 años y 4 meses de antigüedad.

CIERRE
Los cinco cambios de la reforma que más probablemente se pregunten.
```

## Episodio 3 — Unidad 6: ejercicio profesional

```text
Generá un podcast de repaso para un estudiante de Ingeniería en Sistemas (UTN) que rinde el 2do parcial escrito de Legislación. Este episodio cubre sólo la Unidad 6, ejercicio profesional (capítulo 4 del documento y las preguntas guía del capítulo 6). Usá únicamente el documento cargado.

TONO Y FORMATO
- Español rioplatense, dos voces: una explica, la otra pregunta y mezcla qué dice la ley, qué dice el Estatuto y qué dice el Código.
- Caso concreto primero, después la regla con su norma y artículo.
- Remarcá la regla de la cátedra: donde la ley y el Estatuto regulan lo mismo, vale el Estatuto.
- Frená cada tanto con una pregunta guía y respondela como por escrito.

CONTENIDO
1. Responsabilidad civil, penal y administrativa; funciones de la civil; contractual vs. extracontractual; los cuatro presupuestos (antijuridicidad, factor de atribución, nexo causal, daño) con sus variantes; profesional liberal (art. 1768) y principal por el dependiente (art. 1753).
2. Ley 11.291: carácter del Colegio, distritos, normativa, finalidades, autoridades, Tribunal de Ética, matriculación.
3. Estatuto: qué es ejercicio profesional, actuación personal y prohibición de ceder la firma, uso del título, visado y aportes, quiénes deben matricularse, inhabilitados, cancelación, causales y sanciones, composición del Tribunal.
4. Código de Ética: competencia del Tribunal, actos contrarios a la ética por ámbito (tres ejemplos de cada uno), composición del Tribunal (juez unipersonal y tribunal colegiado), apelación y la diferencia con lo que dice la ley.

RESOLVÉ EN VOZ ALTA
El ingeniero que firma una auditoría que no hizo; el matriculado que presta la firma; si un ingeniero en sistemas en relación de dependencia tiene que matricularse; la consultora cuyo empleado borra la base de un cliente.

CIERRE
Las tres listas que conviene saber con ejemplos: causales de sanción, tipos de sanción y actos contrarios a la ética.
```
