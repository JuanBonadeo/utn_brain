# Prompts para los podcasts de repaso — 2do parcial de Legislación

Para NotebookLM: Studio → Resumen de audio → Personalizar. Formato **Análisis detallado**, duración
**Predeterminada** (no hay opción más larga), idioma **español (Latinoamérica)**.

## Versión 2 (2026-10-27)

Armada después de escuchar la v1 y de los relatos del parcial de la noche. Cambios:
- **Repetición**: los podcasts se escuchan de fondo en el gimnasio, así que cada idea clave se dice
  al menos tres veces (al explicarla, en un mini resumen al cerrar el bloque y en el repaso final).
  Por eso son **ocho episodios** más cortos, con menos temas cada uno.
- **Menos ejemplos**: uno por concepto, como mucho dos.
- **Metadata**: cada episodio empieza y termina diciendo versión, número de episodio, unidad y parte.
- **Prioridad según lo que tomaron** (ver "Lo que tomaron en la comisión de la noche" en `LEG.md`):
  primero el caso (título de propiedad industrial, responsabilidad civil, ética), después U5.

**Fuentes del cuaderno** (Google Docs, uno por unidad): U4, U5, U6 y "Lo que tomaron en la noche y
agregados (v2)". Cada episodio usa sólo las que dice su encabezado.

**Orden para escuchar** = número de episodio.

| # | Unidad y parte | Tema | Fuentes |
|---|---|---|---|
| 1 | U4, parte 1 | Elegir el título de propiedad industrial | U4 + agregados |
| 2 | U6, parte 1 | Responsabilidad civil: funciones, presupuestos y daño | U6 + agregados |
| 3 | U6, parte 2 | Ética y el Colegio: ¿hay falta y ante quién? | U6 + agregados |
| 4 | U5, parte 1 | La reforma, el contrato, las modalidades y la jornada | U5 |
| 5 | U5, parte 2 | Remuneración y suspensiones | U5 |
| 6 | U5, parte 3 | Menores, maternidad, vacaciones, licencias y enfermedad | U5 + agregados |
| 7 | U5, parte 4 | Preaviso, extinción e indemnización | U5 |
| 8 | U4, parte 2 | Derecho de autor, y qué no se patenta ni se registra como marca | U4 |

Bloque común, al principio de cada prompt (cambian el número, la unidad, la parte y el tema):

```text
METADATA: empezá el episodio diciendo exactamente: «Legislación, segundo parcial. Podcast versión 2, episodio N de 8. Unidad X, parte Y: TEMA.» Repetí esa misma frase al terminar.
QUIÉN ESCUCHA: un estudiante de Ingeniería en Sistemas (UTN) que rinde el parcial escrito el miércoles 28 de octubre. Lo escucha de fondo en el gimnasio y se pierde partes. Por eso REPETÍ: cada idea clave se dice al menos tres veces: cuando se explica, en un mini resumen al cerrar cada bloque y en un repaso final de todo el episodio. Pocos temas, bien repetidos.
EJEMPLOS: uno por concepto, como mucho dos. No encadenes ejemplos.
TONO: español rioplatense, dos voces; una explica y la otra pregunta y se confunde en lo típico. Usá únicamente las fuentes seleccionadas.
```

### Episodio 1 — U4, parte 1: elegir el título de propiedad industrial

```text
METADATA: empezá el episodio diciendo exactamente: «Legislación, segundo parcial. Podcast versión 2, episodio 1 de 8. Unidad 4, parte 1: cómo elegir el título de propiedad industrial.» Repetí esa misma frase al terminar.
QUIÉN ESCUCHA: un estudiante de Ingeniería en Sistemas (UTN) que rinde el parcial escrito el miércoles 28 de octubre. Lo escucha de fondo en el gimnasio y se pierde partes. Por eso REPETÍ: cada idea clave se dice al menos tres veces: cuando se explica, en un mini resumen al cerrar cada bloque y en un repaso final de todo el episodio. Pocos temas, bien repetidos.
EJEMPLOS: uno por concepto, como mucho dos. No encadenes ejemplos.
TONO: español rioplatense, dos voces; una explica y la otra pregunta y se confunde en lo típico. Usá únicamente las fuentes seleccionadas.

POR QUÉ ESTE EPISODIO: en el parcial de la otra comisión, el caso práctico empezaba siempre igual: un ingeniero en sistemas crea algo y hay que decir qué título de propiedad industrial pide, ante qué organismo, con qué requisitos, por cuántos años y a qué rama pertenece. En un tema era patente de invención y en el otro, modelo de utilidad.

CONTENIDO
1. Propiedad industrial vs. propiedad intelectual: la aplicación industrial como criterio. Si el caso habla de "solicitar un título", es propiedad industrial.
2. Los cuatro títulos que otorga el INPI: patente de invención, modelo de utilidad, diseño industrial y marca. Para cada uno: qué protege, requisitos y plazo.
3. La distinción que más importa: patente (novedad, actividad inventiva, aplicación industrial; 20 años) vs. modelo de utilidad (novedad y aplicación industrial, sin mérito inventivo; 10 años).
4. Software con hardware que resuelve un problema técnico: patente. Programa solo: derecho de autor, sin título.

RESOLVÉ EN VOZ ALTA, completo, los dos casos del parcial de la otra comisión: el software con hardware para el tráfico con mal clima, y el invento que mejora una herramienta.

CIERRE: repasá dos veces las cinco respuestas que pide el caso (título, organismo, requisitos, plazo, rama) y la regla "si ves X, es Y" para los cuatro títulos.
```

### Episodio 2 — U6, parte 1: responsabilidad civil

```text
METADATA: empezá el episodio diciendo exactamente: «Legislación, segundo parcial. Podcast versión 2, episodio 2 de 8. Unidad 6, parte 1: la responsabilidad civil del ingeniero.» Repetí esa misma frase al terminar.
QUIÉN ESCUCHA: un estudiante de Ingeniería en Sistemas (UTN) que rinde el parcial escrito el miércoles 28 de octubre. Lo escucha de fondo en el gimnasio y se pierde partes. Por eso REPETÍ: cada idea clave se dice al menos tres veces: cuando se explica, en un mini resumen al cerrar cada bloque y en un repaso final de todo el episodio. Pocos temas, bien repetidos.
EJEMPLOS: uno por concepto, como mucho dos. No encadenes ejemplos.
TONO: español rioplatense, dos voces; una explica y la otra pregunta y se confunde en lo típico. Usá únicamente las fuentes seleccionadas.

POR QUÉ ESTE EPISODIO: en los dos temas del parcial de la otra comisión, la responsabilidad civil salió dos veces: en el caso (qué función entra en juego) y en una pregunta a desarrollar (la responsabilidad civil del ingeniero, o el daño patrimonial y extrapatrimonial). El Estatuto del Colegio no entra.

CONTENIDO
1. Responsabilidad civil vs. penal: resarcitoria vs. punitiva.
2. Las tres funciones: preventiva, resarcitoria y punitiva, y cuándo aplica cada una: si el daño todavía no ocurrió (un riesgo), preventiva; si ya ocurrió, resarcitoria; la punitiva es excepcional.
3. Contractual vs. extracontractual.
4. Los cuatro presupuestos: antijuridicidad, factor de atribución, nexo causal y daño. El profesional liberal responde subjetivamente salvo que haya comprometido un resultado (art. 1768); el principal responde por su dependiente (art. 1753).
5. El daño: patrimonial (emergente, lucro cesante, pérdida de chance) y extrapatrimonial o moral.

CIERRE: cómo responder por escrito, en un minuto, "desarrolle la responsabilidad civil del ingeniero" y "desarrolle el daño". Repetilo dos veces.
```

### Episodio 3 — U6, parte 2: ética y el Colegio

```text
METADATA: empezá el episodio diciendo exactamente: «Legislación, segundo parcial. Podcast versión 2, episodio 3 de 8. Unidad 6, parte 2: la falta ética y el Colegio de Ingenieros.» Repetí esa misma frase al terminar.
QUIÉN ESCUCHA: un estudiante de Ingeniería en Sistemas (UTN) que rinde el parcial escrito el miércoles 28 de octubre. Lo escucha de fondo en el gimnasio y se pierde partes. Por eso REPETÍ: cada idea clave se dice al menos tres veces: cuando se explica, en un mini resumen al cerrar cada bloque y en un repaso final de todo el episodio. Pocos temas, bien repetidos.
EJEMPLOS: uno por concepto, como mucho dos. No encadenes ejemplos.
TONO: español rioplatense, dos voces; una explica y la otra pregunta y se confunde en lo típico. Usá únicamente las fuentes seleccionadas.

POR QUÉ ESTE EPISODIO: en el caso del parcial preguntaban si hay falta ética del ingeniero, por qué y ante quién. Y en el verdadero o falso salió un requisito para matricularse en el Colegio. El Estatuto del Colegio no entra; no lo expliques.

CONTENIDO
1. A quién alcanza el Código de Ética: a todos los profesionales, matriculados o no (art. 2).
2. Ante quién hay deberes: la profesión, los colegas, los comitentes o empleadores y el Colegio (art. 5).
3. Las faltas de cada ámbito (art. 6), con un solo ejemplo de software por ámbito.
4. Quién juzga: el Tribunal de Ética Profesional y Disciplina (ley 11.291, art. 11). Causales (art. 18) y sanciones (art. 19).
5. El Colegio: persona jurídica de derecho privado con funciones públicas (art. 1); requisitos para matricularse (art. 21); suspensión y cancelación de la matrícula (art. 24).

RESOLVÉ EN VOZ ALTA, con el método de cuatro pasos (¿lo alcanza el Código?, ¿ante quién falló?, ¿qué falta del art. 6?, ¿qué causal y qué sanción?), los dos casos del parcial: el software que genera un riesgo vial para bajar costos, y el invento que sale mal.

CIERRE: repetí dos veces el método de cuatro pasos y los cuatro requisitos para matricularse.
```

### Episodio 4 — U5, parte 1: la reforma, el contrato, las modalidades y la jornada

```text
METADATA: empezá el episodio diciendo exactamente: «Legislación, segundo parcial. Podcast versión 2, episodio 4 de 8. Unidad 5, parte 1: la reforma, el contrato, las modalidades y la jornada.» Repetí esa misma frase al terminar.
QUIÉN ESCUCHA: un estudiante de Ingeniería en Sistemas (UTN) que rinde el parcial escrito el miércoles 28 de octubre. Lo escucha de fondo en el gimnasio y se pierde partes. Por eso REPETÍ: cada idea clave se dice al menos tres veces: cuando se explica, en un mini resumen al cerrar cada bloque y en un repaso final de todo el episodio. Pocos temas, bien repetidos.
EJEMPLOS: uno por concepto, como mucho dos. No encadenes ejemplos.
TONO: español rioplatense, dos voces; una explica y la otra pregunta y se confunde con la ley anterior a la reforma. Usá únicamente las fuentes seleccionadas.

POR QUÉ ESTE EPISODIO: la Unidad 5 entra en un verdadero o falso de diez afirmaciones, sin justificar, con datos finos de la Ley de Contrato de Trabajo y de la reforma de la Ley 27.802. En la otra comisión preguntaron, por ejemplo, si una actividad tenía que hacerse con contrato a plazo fijo.

CONTENIDO (secciones 1 a 4 del documento de la Unidad 5)
1. Los cambios de la Ley 27.802.
2. El contrato de trabajo, la relación de dependencia y sus tres formas.
3. Las modalidades: plazo fijo, temporada, eventual y tiempo parcial; cuándo corresponde cada una.
4. El período de prueba según el tamaño de la empresa.
5. La jornada y las horas extra.

Cada bloque cierra con dos afirmaciones de verdadero o falso, una pausa y la respuesta.

CIERRE: un repaso de los números que hay que saber (plazos, topes, porcentajes), dicho dos veces.
```

### Episodio 5 — U5, parte 2: remuneración y suspensiones

```text
METADATA: empezá el episodio diciendo exactamente: «Legislación, segundo parcial. Podcast versión 2, episodio 5 de 8. Unidad 5, parte 2: la remuneración y las suspensiones.» Repetí esa misma frase al terminar.
QUIÉN ESCUCHA: un estudiante de Ingeniería en Sistemas (UTN) que rinde el parcial escrito el miércoles 28 de octubre. Lo escucha de fondo en el gimnasio y se pierde partes. Por eso REPETÍ: cada idea clave se dice al menos tres veces: cuando se explica, en un mini resumen al cerrar cada bloque y en un repaso final de todo el episodio. Pocos temas, bien repetidos.
EJEMPLOS: uno por concepto, como mucho dos. No encadenes ejemplos.
TONO: español rioplatense, dos voces; una explica y la otra pregunta y se confunde con la ley anterior a la reforma. Usá únicamente las fuentes seleccionadas.

POR QUÉ ESTE EPISODIO: en la otra comisión, un tema tuvo como pregunta a desarrollar "la remuneración", y el verdadero o falso preguntó si las propinas son remuneración con la nueva ley y cuántos días de sanción puede dar el empleador.

CONTENIDO (secciones 6 y 7 del documento de la Unidad 5)
1. Qué es la remuneración (art. 103) y el salario mínimo, vital y móvil.
2. Sus formas: por tiempo, por resultado, complementarias (SAC), en dinero o en especie (tope del 20 %).
3. Remunerativo vs. no remunerativo; propinas y beneficios sociales después de la reforma.
4. Las suspensiones: requisitos, causas y topes por año, sobre todo la disciplinaria.

CIERRE: cómo desarrollar por escrito "la remuneración" en un minuto, dicho dos veces, y un verdadero o falso rápido de cinco afirmaciones.
```

### Episodio 6 — U5, parte 3: menores, maternidad, vacaciones, licencias y enfermedad

```text
METADATA: empezá el episodio diciendo exactamente: «Legislación, segundo parcial. Podcast versión 2, episodio 6 de 8. Unidad 5, parte 3: trabajo de menores, maternidad, vacaciones, licencias y enfermedad.» Repetí esa misma frase al terminar.
QUIÉN ESCUCHA: un estudiante de Ingeniería en Sistemas (UTN) que rinde el parcial escrito el miércoles 28 de octubre. Lo escucha de fondo en el gimnasio y se pierde partes. Por eso REPETÍ: cada idea clave se dice al menos tres veces: cuando se explica, en un mini resumen al cerrar cada bloque y en un repaso final de todo el episodio. Pocos temas, bien repetidos.
EJEMPLOS: uno por concepto, como mucho dos. No encadenes ejemplos.
TONO: español rioplatense, dos voces; una explica y la otra pregunta y se confunde con los números. Usá únicamente las fuentes seleccionadas.

POR QUÉ ESTE EPISODIO: en la otra comisión, un tema tuvo como pregunta a desarrollar "el trabajo de menores". Y el verdadero o falso pide números exactos.

CONTENIDO (sección 5 del documento de la Unidad 5 y la sección de trabajo de menores del documento de agregados)
1. Trabajo de menores: la prohibición antes de los 16 y su excepción; las reglas de 16 a 18 años (jornada, nocturno, descanso semanal, descanso al mediodía, vacaciones).
2. Maternidad: licencia, estabilidad e indemnización agravada.
3. Vacaciones según antigüedad y cómo se dan.
4. Licencias especiales.
5. Enfermedad inculpable: aviso, certificado y meses pagos.

CIERRE: cómo desarrollar por escrito "el trabajo de menores" en un minuto, dicho dos veces, y los números de vacaciones y licencias repetidos.
```

### Episodio 7 — U5, parte 4: preaviso, extinción e indemnización

```text
METADATA: empezá el episodio diciendo exactamente: «Legislación, segundo parcial. Podcast versión 2, episodio 7 de 8. Unidad 5, parte 4: el preaviso, la extinción del contrato y la indemnización.» Repetí esa misma frase al terminar.
QUIÉN ESCUCHA: un estudiante de Ingeniería en Sistemas (UTN) que rinde el parcial escrito el miércoles 28 de octubre. Lo escucha de fondo en el gimnasio y se pierde partes. Por eso REPETÍ: cada idea clave se dice al menos tres veces: cuando se explica, en un mini resumen al cerrar cada bloque y en un repaso final de todo el episodio. Pocos temas, bien repetidos.
EJEMPLOS: uno por concepto, como mucho dos. No encadenes ejemplos.
TONO: español rioplatense, dos voces; una explica y la otra pregunta y se confunde con los números. Usá únicamente las fuentes seleccionadas.

POR QUÉ ESTE EPISODIO: completa la Unidad 5 para el verdadero o falso y por si la pregunta a desarrollar de laboral es sobre la extinción.

CONTENIDO (sección 7 del documento de la Unidad 5, sin las suspensiones)
1. El preaviso: plazos del trabajador y del empleador, indemnización sustitutiva e integración del mes.
2. Las formas de extinción: despido con causa, sin causa e indirecto, renuncia, mutuo acuerdo y las demás.
3. La indemnización por antigüedad: cómo se calcula, el mínimo y el tope.
4. La liquidación final: qué se paga siempre y qué según el caso.

RESOLVÉ EN VOZ ALTA un solo caso: despido sin causa ni preaviso con 6 años y 4 meses de antigüedad.

CIERRE: repetí dos veces qué se paga en un despido sin causa, en orden.
```

### Episodio 8 — U4, parte 2: derecho de autor, y qué no se patenta ni se registra

```text
METADATA: empezá el episodio diciendo exactamente: «Legislación, segundo parcial. Podcast versión 2, episodio 8 de 8. Unidad 4, parte 2: el derecho de autor, y qué no se patenta ni se registra como marca.» Repetí esa misma frase al terminar.
QUIÉN ESCUCHA: un estudiante de Ingeniería en Sistemas (UTN) que rinde el parcial escrito el miércoles 28 de octubre. Lo escucha de fondo en el gimnasio y se pierde partes. Por eso REPETÍ: cada idea clave se dice al menos tres veces: cuando se explica, en un mini resumen al cerrar cada bloque y en un repaso final de todo el episodio. Pocos temas, bien repetidos.
EJEMPLOS: uno por concepto, como mucho dos. No encadenes ejemplos.
TONO: español rioplatense, dos voces; una explica y la otra pregunta y se confunde en lo típico. Usá únicamente las fuentes seleccionadas.

POR QUÉ ESTE EPISODIO: completa la Unidad 4 por si el caso o una pregunta van por el lado del derecho de autor o de lo que no se puede patentar o registrar.

CONTENIDO
1. Derechos personales, reales e intelectuales, en un minuto.
2. Ley de patentes: art. 6 (lo que no es invención) vs. art. 7 (lo que es invención pero no se patenta).
3. Ley de marcas: art. 2 (lo que no es marca) vs. art. 3 (lo que está prohibido registrar).
4. Ley 11.723: qué protege (la expresión, no la idea), el software, los titulares (el empleado contratado para programar), obra en colaboración vs. colectiva, 70 años.

CIERRE: las distinciones que no hay que confundir, en formato "si ves X, es Y", dichas dos veces.
```

## Versión 1 (2026-10-26)

Cuatro episodios armados con el formato que circulaba antes de los relatos del parcial de la noche.

Pensados para NotebookLM: Studio → Resumen de audio → Personalizar. Formato **Análisis en
profundidad**, duración **Más larga**, idioma **Español**.

**Fuentes del cuaderno:** `resumen-2do-parcial.pdf` (actualizado el 2026-10-26 con el formato del
parcial y los artículos de U6 que dijo la profesora). Para el episodio de U6 sumá también
`fuentes/catedra/u6/codigo-de-etica.pdf`, por el art. 6 completo.

**Formato del parcial** (`fuentes/2026-10-26_formato-parcial2.md`): un caso práctico de U4 o U6; un
verdadero o falso de U5, sin justificar las falsas; una pregunta de la unidad (U4 o U6) que no fue
caso, y otra de laboral. Los prompts están armados para eso: **U4 y U6 entrenan caso y pregunta**, y
**U5 entrena V o F y pregunta**. U5 va en dos episodios porque es la que más pesa y la que más
contenido tiene.

**Orden para escuchar:** 1) U5 parte 1, 2) U5 parte 2, 3) U6, 4) U4. Si la cuenta gratuita limita
la cantidad de resúmenes de audio por día, los tres primeros van primero.

### Episodio 1 — U5, parte 1: la reforma, el contrato y la jornada

```text
Podcast de repaso para un estudiante de Ingeniería en Sistemas (UTN) que rinde el 2do parcial escrito de Legislación. Este episodio es sólo la primera mitad de la Unidad 5, derecho laboral: secciones 3.1 a 3.4 del documento y los bloques 1 a 3 de la guía de lectura (capítulo 5). Usá únicamente el documento.

CÓMO SE TOMA: un verdadero o falso de la Unidad 5 sin justificar, y una pregunta a desarrollar. Por eso importan los datos exactos (plazos, porcentajes, días, topes) y las trampas, sobre todo lo que cambió con la Ley 27.802: el V o F suele armarse con la regla vieja.

FORMATO
- Español rioplatense, dos voces: una explica, la otra hace de alumno que todavía tiene en la cabeza la ley anterior a la reforma y la corrigen.
- Casos de la vida real, en lo posible de alguien que trabaja en una empresa de software.
- Cada tema cierra con dos o tres afirmaciones de verdadero o falso dichas en voz alta, una pausa, y la respuesta con el porqué en una frase.

CONTENIDO
1. Qué cambió con la Ley 27.802: concepto de trabajo, presunción del art. 23 y la factura, nuevas exclusiones, período de prueba según el tamaño de la empresa, propinas.
2. Qué es trabajo dependiente y qué queda afuera; las tres subordinaciones; contrato vs. relación; elementos esenciales, capacidad y forma; los sujetos.
3. Deberes y facultades de cada parte; invenciones y software del trabajador (art. 82 LCT y art. 4 inc. d de la 11.723); ius variandi y despido indirecto.
4. Modalidades del contrato, período de prueba, jornada, horas extra y sus recargos.

CIERRE: un V o F rápido de diez afirmaciones de esta mitad, sin pausa larga, con la respuesta inmediata.
```

### Episodio 2 — U5, parte 2: vacaciones, remuneración y extinción

```text
Podcast de repaso para un estudiante de Ingeniería en Sistemas (UTN) que rinde el 2do parcial escrito de Legislación. Este episodio es sólo la segunda mitad de la Unidad 5, derecho laboral: secciones 3.5 a 3.7 del documento y los bloques 4 y 5 de la guía de lectura (capítulo 5). Usá únicamente el documento.

CÓMO SE TOMA: un verdadero o falso de la Unidad 5 sin justificar, y una pregunta a desarrollar. Por eso importan los datos exactos (días de vacaciones según antigüedad, plazos de licencia, topes de suspensión, plazos de preaviso, cómo se calcula la indemnización) y las trampas de la reforma de la Ley 27.802.

FORMATO
- Español rioplatense, dos voces: una explica, la otra hace de alumno que confunde los números y la regla vieja con la nueva, y la corrigen.
- Casos concretos con números: alguien con tantos años de antigüedad, tal sueldo, tal situación.
- Cada tema cierra con dos o tres afirmaciones de verdadero o falso en voz alta, una pausa, y la respuesta con el porqué en una frase.

CONTENIDO
1. Vacaciones y cómo se cuentan, licencias especiales, enfermedad inculpable, maternidad.
2. Remuneración: formas, SAC, remunerativo vs. no remunerativo, beneficios sociales, pago.
3. Suspensiones: causas y topes.
4. Preaviso y formas de extinción del contrato; despido con y sin causa, indemnización por antigüedad y liquidación final.

RESOLVÉ EN VOZ ALTA: un despido sin causa y sin preaviso con 6 años y 4 meses de antigüedad, qué se paga y por qué.

CIERRE: un V o F rápido de diez afirmaciones de esta mitad, con la respuesta inmediata.
```

### Episodio 3 — U6: ejercicio profesional y ética

```text
Podcast de repaso para un estudiante de Ingeniería en Sistemas (UTN) que rinde el 2do parcial escrito de Legislación. Este episodio es sólo la Unidad 6, ejercicio profesional: capítulo 4 del documento, el Código de Ética cargado y las preguntas guía del capítulo 6. Usá únicamente las fuentes.

CÓMO SE TOMA: puede salir como caso práctico o como pregunta a desarrollar. La profesora dijo que el caso va a pedir analizar si una conducta constituye o no una falta, y ante quién. Los artículos no se piden de memoria: hay que saber qué regula cada uno y usarlo.

QUÉ ENTRA Y QUÉ NO: el Estatuto NO entra; no lo expliques. De la ley 11.291 entran los arts. 1, 4 (incisos a, b, c, e, f, g, l, m y p), 11, 18, 19, 21 y 24. Del Código de Ética, los arts. 2, 5 y 6. Más la responsabilidad civil del profesional.

FORMATO
- Español rioplatense, dos voces: una explica y la otra hace de alumno que resuelve casos y a veces ve una falta donde no la hay, o al revés.
- La mayor parte del episodio son casos de un ingeniero en sistemas, resueltos siempre con el mismo orden: 1) ¿lo alcanza el Código? (art. 2, matriculado o no); 2) ¿ante quién falló? (art. 5: la profesión, los colegas, el comitente o empleador, el Colegio); 3) ¿qué conducta del art. 6 encaja?; 4) causal (ley, art. 18) y sanción (art. 19), y si toca la matrícula (art. 24); 5) si hubo daño a un cliente, la responsabilidad civil.
- Incluí al menos un caso donde NO hay falta.

CONTENIDO
1. Responsabilidad civil: función resarcitoria, contractual vs. extracontractual, los cuatro presupuestos, el profesional liberal (art. 1768) y el principal por el dependiente (art. 1753).
2. Ley 11.291: carácter del Colegio, las atribuciones del art. 4 que entran, el Tribunal de Ética, causales y sanciones, matriculación, suspensión y cancelación de la matrícula.
3. Código de Ética: a quién alcanza, ante quién hay deberes y los actos contrarios a la ética de cada ámbito, con ejemplos de software (firmar lo que no se revisó, usar código ajeno, revelar datos de un cliente, aceptar comisiones de un proveedor).

CIERRE: tres casos cortos para que el oyente resuelva solo, con la respuesta después de una pausa.
```

### Episodio 4 — U4: derechos intelectuales

```text
Podcast de repaso para un estudiante de Ingeniería en Sistemas (UTN) que rinde el 2do parcial escrito de Legislación. Este episodio es sólo la Unidad 4, derechos intelectuales: capítulo 2 del documento. Usá únicamente el documento.

CÓMO SE TOMA: puede salir como caso práctico o como pregunta a desarrollar. Los artículos no se piden de memoria: para cada uno hay que saber qué regula y tener tres ejemplos listos.

FORMATO
- Español rioplatense, dos voces: una explica, la otra pregunta y cae en las confusiones típicas.
- Para cada tema: un caso concreto, en lo posible del mundo del software; después la regla con su artículo; después la trampa.
- Resolvé casos en voz alta con un orden fijo: qué derecho está en juego, qué norma y artículo se aplica, quién es el titular y qué puede hacer.

CONTENIDO
1. Derechos personales vs. reales vs. intelectuales; propiedad industrial vs. intelectual y la aplicación industrial como criterio.
2. Patente, modelo de utilidad, diseño industrial y marca: qué protegen, requisitos y plazos.
3. Ley de patentes, art. 6 (no es invención) vs. art. 7 (es invención pero no es patentable), con tres ejemplos de cada uno. Por qué el software no se patenta.
4. Ley de marcas, art. 1 (qué se registra), art. 2 (no es marca) vs. art. 3 (prohibido), con tres ejemplos de cada uno.
5. Ley 11.723: arts. 1, 2, 4, 5 y 59. Qué protege (la expresión, no la idea), facultades del autor, titulares (el software hecho por un empleado), obra en colaboración vs. colectiva, 70 años, registro de obras.

RESOLVÉ EN VOZ ALTA: quién es dueño de un software hecho por un empleado en tres versiones (en su casa y por su cuenta, contratado para programarlo, usando los medios de la empresa); una startup que quiere patentar su app; una marca que se parece a otra ya registrada.

CIERRE: las distinciones que no hay que confundir en el escrito, en formato "si ves X, es Y".
```
