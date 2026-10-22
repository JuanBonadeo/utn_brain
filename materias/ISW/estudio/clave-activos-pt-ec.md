# ISW — Activo, producto de trabajo y elemento de configuración

**Ingeniería y Calidad de Software · UTN · 4.º año**

**La clave para resolver los ejercicios de U2 (activo vs. producto de trabajo) y U6 (qué va bajo gestión de configuración)**

En el recu del 24/10 entra la grilla de U2. La parte de configuración (U6) es para el AD.

## 1. La idea central: dos preguntas separadas

Todo ejercicio de este tipo se resuelve haciéndose **dos preguntas distintas** sobre cada elemento del enunciado:

1. **¿Qué es?** Producto de trabajo, producto o activo. No cambia nunca.
2. **¿Lo pongo bajo control de configuración?** Si la respuesta es sí, además es un **elemento de configuración (EC)**.

Ser EC **no es una cuarta categoría**: un producto, un producto de trabajo interno o una herramienta *pasan a ser* EC cuando se decide ponerlos bajo control.

**Analogía.** En una facultad cada persona es estudiante, docente o no docente: eso es *qué es*. Aparte, cualquiera puede estar afiliado o no a la obra social. "Afiliado" no es un cuarto tipo de persona: un estudiante afiliado sigue siendo estudiante.

## 2. Pregunta 1: qué es cada cosa

| Categoría | Qué es | Pregunta que lo decide | Ejemplos |
|---|---|---|---|
| **Producto de trabajo** | Resultado concreto de una tarea **de un proyecto**. No necesariamente se entrega | ¿Salió de un proyecto? | Minuta, informe de taller, regla de negocio, código `.java`, `.class`, caso de uso |
| **Producto** | El producto de trabajo **que se entrega** al cliente | ¿Se le entrega al cliente? | La aplicación, el manual de usuario del sistema del cliente |
| **Activo** | Lo que la organización tiene **para usar en muchos proyectos**. Incluye las **herramientas que adquiere** y su documentación | ¿Existe para usarse en varios proyectos o se compró? | Plantillas, guías, directrices, estándares, Word, Java, el manual del compilador Java |

**Señales en el texto:**

- **Activo:** plantilla, guía, directriz, modelo, estándar, política, checklist, herramienta comprada.
- **Producto de trabajo:** "del cliente", "del sistema desarrollado", "del proyecto X", un artefacto puntual.

**El par que fija el criterio:** la *plantilla* de manual de instalación es un **activo** (el molde es de la organización). El *manual de instalación del sistema del cliente* es un **producto de trabajo** (lo moldeado es del proyecto).

**Ojo:** en los 10 ítems confirmados de la grilla de U2, **"Ambos" nunca fue la respuesta correcta**.

**Ojo:** el manual de usuario **del compilador Java** es **activo**, no producto de trabajo. Es documentación de una herramienta que la organización adquiere; ningún proyecto lo produjo.

## 3. Pregunta 2: qué va bajo configuración

Va bajo configuración lo que cumple alguno de estos criterios:

- lo usan **dos o más grupos**;
- **puede cambiar** (por cambios de requisitos o por errores);
- otros elementos **dependen** de él;
- es **crítico** para el proyecto.

En la práctica: planes, especificación de requisitos, matriz de trazabilidad, diseño, código fuente y compilado, casos y datos de prueba, minutas, informes, manuales, entregables y las plantillas que se usan.

**Un EC puede agrupar varios productos de trabajo.** Un manual escrito por capítulos tiene un producto de trabajo por capítulo, pero es **un solo EC**. Por eso es **falso** que "cada producto de trabajo es un EC y un EC es uno solo".

**Herramientas.** Pueden ser EC si hacen falta para **reconstruir** una versión: sin el lenguaje y el compilador en la versión usada, el código fuente no alcanza. En las respuestas de la cátedra:

| La pregunta pide... | ¿Entran las herramientas? | Caso |
|---|---|---|
| Garantizar la evolución / reconstruir el software | **Sí** (lenguaje A, MS-Word 2002) | Caso 2002 |
| Productos de trabajo bajo CM | **No** (no son productos de trabajo) | Organización 2021 |
| Lo que no es producto de trabajo / activos de proceso del proyecto | **No** quedaron en la respuesta | Organización 2021, plantillas Plla |

Este último criterio sale de comparar las respuestas de la cátedra, no de una definición escrita.

## 4. Los filtros del caso

Después de clasificar, cada elemento tiene que pasar los filtros que pone el enunciado. Acá es donde más se marca de más.

| Filtro | Qué preguntarse | Ejemplo |
|---|---|---|
| **Aplica al caso** | ¿El enunciado lo menciona como algo que se usa? | La plantilla Base-clase **v1.0** no aparece en el caso: queda afuera |
| **Versión vigente** | ¿Es la última versión **anterior al inicio** del proyecto? | Proyecto del 01/10/23 → de cada plantilla, la de fecha más nueva hasta esa fecha |
| **Formato discontinuado** | ¿Hay una nota que deja un formato fuera de uso? | "Los `.doc` no se usan desde 01/08/23" → se descartan |
| **Existía en esa fecha** | Si te paran en un año, ¿eso ya existía? | En 2002 no existía el lenguaje B (las apps móviles son de los últimos 2 años) |
| **Existe la herramienta** | ¿Es una versión real y compatible? | Word 2005 no existe; Word 2003 no abre `.docx` |

## 5. El método paso a paso

1. **Subrayá qué pide la pregunta.** ¿Productos de trabajo? ¿Activos? ¿Lo que **no** es producto de trabajo? ¿Lo que hace falta **en un año dado**? Buscá la negación: hay preguntas espejo.
2. **Clasificá cada opción** con la tabla de la sección 2 (pregunta 1).
3. **Decidí si va bajo configuración** con la sección 3 (pregunta 2).
4. **Pasá los filtros** de la sección 4.
5. **Cruzá** lo que quedó con lo que pide la pregunta. Marcá solo lo que cumple **todo**.
6. **Revisá opción por opción** antes de entregar. En multiple choice con varias correctas, el error típico es marcar de más.

## 6. Tus errores, resueltos con el método

**Manual de usuario del compilador Java (U2).**

- Paso 2: ningún proyecto lo produjo; viene con una herramienta comprada.
- Respuesta: **activo**. Marcaste producto de trabajo.

**Organización 2021: productos de trabajo aceptables para CM.**

- Paso 1: piden **productos de trabajo**.
- Paso 2: minuta, informe de talleres, `.java` y `.class` son productos de trabajo. Write/OpenOffice y Java SE 7 son herramientas (activos).
- Respuesta: **minuta, informe de resultados de talleres, código fuente `.java`, código compilado `.class`**. Marcaste justo las herramientas.

**Organización 2021: viables de CM que no son productos de trabajo.**

- Paso 1: piden lo **contrario** de la anterior: lo que *no* es producto de trabajo.
- Paso 2: candidatos: Java SE 7, Word 2013, plantilla Base-clase v2.0, plantilla v1.0.
- Paso 4: la v1.0 no está en el caso. Las herramientas no quedaron en la respuesta de la cátedra.
- Respuesta: **solo la plantilla Base-clase-v2.0**.

**"Cada producto de trabajo es un EC; un EC refiere a uno solo."**

- Un EC puede agrupar varios productos de trabajo (el manual por capítulos).
- Respuesta: **falso**.

**Plantillas Plla y definiciones Def (proyecto iniciado el 01/10/23).**

| Elemento | ¿Vigente al 01/10/23? | ¿Formato válido? | ¿Va? |
|---|---|---|---|
| Plla-CUR-20230803.docx | Sí (la CUR más nueva) | Sí | **Sí** |
| Plla-CUR-20221212.docx | No, hay una CUR más nueva | Sí | No |
| Plla-CUR-20230305.docx | No, hay una CUR más nueva | Sí | No |
| Plla-CUU-20230305.doc | — | No (`.doc` fuera desde 01/08/23) | No |
| Plla-CUU-20230305.docx | Sí (la única CUU válida) | Sí | **Sí** |
| Def-CUF-20221213.txt | Sí (la única CUF) | Sí | **Sí** |
| Word 2003 / 2005 / 2019 | — | — | No (herramientas; 2005 ni existe) |

Marcaste las nueve opciones. El error fue no aplicar los filtros.

**Caso 2002: qué debería quedar bajo CM para garantizar la evolución.**

- Paso 1: te paran en **2002** y piden poder **reconstruir**: entran herramientas.
- Paso 4 (existía en 2002): app de escritorio, código fuente, lenguaje A, MS-Word 2002, manuales PDF y la documentación del sistema de contrataciones (no se nombra explícitamente pero se deduce: la empresa desarrolla a partir de sus requerimientos).
- No existían: lenguaje B, app móvil, estándar de interfaces (2010), manual on-line.
- Respuesta: **documentación del sistema de contrataciones, app de escritorio, lenguaje A, código fuente, MS-Word 2002, manuales PDF**. Marcaste el lenguaje B (no existía) y te faltó la documentación.

## 7. Trampas que se repiten

- **Confundir herramienta con producto de trabajo.** Word o Java nunca son productos de trabajo: son activos.
- **Preguntas espejo.** Una pide productos de trabajo y la siguiente pide lo que *no* es producto de trabajo, sobre el mismo caso.
- **Marcar todo lo que "suena" a configuración** sin pasar los filtros de vigencia y formato.
- **Olvidar lo que el enunciado no nombra** pero se deduce (la documentación del sistema en el caso 2002).
- **"Ambos"** en la grilla de U2: nunca fue la correcta.
- **"Nivel organizacional" con productos de trabajo:** ¿qué área verifica y almacena los productos de trabajo a nivel organizacional? **NINGUNA**. Si dijera *activos*, sería OPD.

## 8. Preguntas de práctica

**1) Plantilla del plan de proyecto: ¿activo, producto de trabajo o ambos?**

**2) Plan de proyecto del sistema de facturación del cliente X: ¿activo, producto de trabajo o ambos?**

**3) Guía para estimar con puntos función: ¿activo, producto de trabajo o ambos?**

**4) Licencia y manual de instalación de Eclipse, IDE que compró la organización: ¿activo, producto de trabajo o ambos?**

**5) Casos de prueba del módulo de cobranzas: ¿pueden ser elemento de configuración? ¿Qué son en la pregunta 1?**

**6) Un proyecto arranca el 15/03/24. Hay Plla-ERS-20231120.docx, Plla-ERS-20240310.docx y Plla-ERS-20240401.docx. ¿Cuál se usa en el proyecto?**

**7) Verdadero o falso: "Si una herramienta está bajo gestión de configuración, deja de ser un activo y pasa a ser un elemento de configuración."**

## Respuestas

**1) Activo.** Es el molde que la organización usa en todos sus proyectos.

**2) Producto de trabajo.** Salió de un proyecto concreto ("del cliente X").

**3) Activo.** "Guía" es señal de activo: sirve para muchos proyectos.

**4) Activo.** Es una herramienta adquirida y su documentación, como el manual del compilador Java.

**5) Sí, pueden ser EC** (pueden cambiar y otros dependen de ellos). En la pregunta 1 son **producto de trabajo**: salen del proyecto.

**6) Plla-ERS-20240310.docx.** Es la más nueva **anterior al inicio**. La del 01/04/24 se creó después de arrancar el proyecto: por la política de la organización, no se usa en él.

**7) Falso.** Sigue siendo un activo. Ser EC no reemplaza su categoría: se le suma. Son dos preguntas separadas.
