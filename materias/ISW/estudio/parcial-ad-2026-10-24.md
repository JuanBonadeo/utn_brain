# Parcial de Aprobación Directa — 24/10/2026 (EXAM336), resuelto

> Reconstruido desde las fotos del examen (`fuentes/parciales-ad/parcial-ad-2026-10-24-p*.jpg`;
> faltan las páginas 2 y 4, que no tenían consignas nuevas). Formato Google Forms, 1 punto por
> consigna salvo donde se indica. Las preguntas 1 a 3 eran datos personales (correo, legajo,
> comisión). Lo marcado `[?]` es texto reconstruido porque en la foto no se lee bien.
> Las resoluciones aplican los criterios de la wiki (`ISW.md`); cuando algo es razonamiento
> propio y no criterio de cátedra, se aclara.

---

## 4. a) Activos de proceso y herramientas de la gestión de configuración

**Consigna.** Defina los activos de proceso y herramientas que deberían formar parte de la gestión
de configuración del proyecto.

**Contexto.**

- Una software factory nos contrata para organizar la estrategia de identificación de elementos de
  gestión de configuración `[?] en lo que respecta a sus activos:` plantillas y definiciones de
  productos de trabajo.
- Las **plantillas** describen un formato de uso a través de su extensión. Una plantilla docx
  puede abrirse y usarse desde `[?] Word 2007 en adelante`; los Word anteriores a 2007 abren
  perfectamente los formatos doc.
- Como la política de trabajo puede verse afectada por el producto Word en sus distintas versiones
  o variantes, cuando la organización decide un nuevo producto para manipular sus plantillas
  realiza varias evaluaciones. Ej.: Word permite abrir doc y docx `[?] manteniendo sus propiedades
  funcionales y visuales`.
- La **definición de un producto de trabajo** es un artefacto que describe productos de trabajo
  (objetivo, secciones `[?] y otros aspectos de organización del producto al que refiere`). No
  tiene formato ni cuestiones visuales. `[?] Tiene extensión txt: la puede abrir y usar cualquier
  herramienta de las usadas por las plantillas.`

**Política de la organización.** Cuando el proyecto inicia, los productos de trabajo se hacen con
determinadas plantillas y se basan en determinadas definiciones de producto. `[?] Se usa la versión
vigente al momento de comenzar el proyecto.`

**Formato.**

```
Activos:            <tipo-artefacto>-<nombre>-<fecha-invertida>.<extension>
Productos Trabajo:  <tipo-artefacto>-<nombre>.<extension>
Herramienta:        <nombre><<espacio>><version>
```

- `<tipo-artefacto>`: tipo de artefacto (ej.: Plla = plantilla, CUR = caso de uso resumen).
- `<nombre>`: descripción breve, sin espacios ni símbolos especiales.
- `<fecha-invertida>`: fecha de actualización del artefacto, AAAAMMDD.
- `<extension>`: 2 a 5 caracteres que sugieren la herramienta con que se abre el archivo.
- `<<espacio>>`: un blanco.

El proyecto se inició el **01/10/23**. Los casos de uso nombrados son los desarrollados hasta el
momento. **Nota:** las versiones de activos con extensión doc no se usan más a partir del
**01/08/23**.

**Opciones.** Plla-CUR-20230803.docx · Plla-CUR-20221212.docx · Plla-CUR-20230305.docx ·
Plla-CUU-20230305.doc · Plla-CUU-20230305.docx · Def-CUF-20221213.txt · Word 2003 · Word 2005 ·
Word 2007 · CUR-Realizar-inscripción-carrera.docx · CUU-Realizar-inscripción-cursado-asignatura.docx
· CUU-Realizar-inscripción-parcial.docx · CUU-Realizar-inscripción-examen-final.docx ·
CUF-Hacer-logueo-app.docx · Ninguna de las presentadas · NO CONTESTA.

**Resolución** (algoritmo de `clave-activos-pt-ec.html`: descartar productos de trabajo → agrupar
activos por tipo → tachar lo posterior al inicio y el formato discontinuado → el más nuevo de cada
grupo).

```
Plla-CUR:  20221212 ✗ · 20230305 ✗ · 20230803 ✓   (el más nuevo antes del 01/10/23)
Plla-CUU:  20230305.doc ✗ (doc discontinuado) · 20230305.docx ✓
Def-CUF:   20221213.txt ✓   (único: va aunque sea viejo)
Herram.:   Word 2003 ✗ · Word 2005 ✗ · Word 2007 ✓
CUR-…, CUU-…, CUF-…: ✗   (productos de trabajo, no activos ni herramientas)
```

**Respuesta:** Plla-CUR-20230803.docx, Plla-CUU-20230305.docx, Def-CUF-20221213.txt, Word 2007.

Los Word anteriores a 2007 sólo servían para doc, que ya no se usa; las plantillas vigentes son
docx. La definición txt la abre cualquier herramienta, así que no suma ninguna.

---

## 5. b) Verdadero o falso (cada respuesta correcta vale 1 punto)

1. *"Analizar los requerimientos de Registrar al 100 %, antes de ver los requerimientos de
   Informar, garantiza cero retrabajo porque se asegura la entrada de datos primero."*
   → **Falso.** Al analizar Informar suelen aparecer datos que los reportes necesitan y que nadie
   carga, y eso obliga a volver sobre Registrar. "Garantiza cero" es lo que la delata.
2. *"Estamos haciendo diseño y se detectan campos faltantes. Luego el desvío en el esfuerzo afecta
   únicamente al módulo de reportes en el Diseño."*
   → **Falso.** Los campos faltantes obligan a revisar requerimientos, el diseño de la entrada de
   datos (Registrar) y su persistencia, además de reportes. "Únicamente" es la trampa.

*(Razonamiento propio: el enunciado no tenía contexto y no está en las fuentes.)* Las dos se
contestan entre sí: la 2 es justo el caso que demuestra que la 1 es falsa.

---

## 6. c) Día de comienzo de cada tarea

**Consigna.** Determine el día de comienzo de cada tarea solicitada. La columna predecesoras indica
las predecesoras de cada tarea (ej.: la tarea 4 Diseño RE tiene como predecesora a la tarea 3
Análisis RE). Cada tarea la realiza un profesional distinto, así que no faltan recursos.
Nota 1: cada columna representa un día. Nota 2: cada línea vale un punto. Se marcan sólo las
filas de RD (grilla de días 1 a 17+).

```
Id  Tarea                               Duración   Predecesoras
 1  Incremento 2 – Resolución Ejerc.    120 horas
 2   Resolución de ejercicios            96 horas
 3     Análisis RE                       2 días
 4     Diseño RE                         3 días     3
 5     Codificación RE                   3 días     4
 6     Prueba RE                         4 días     5
 7   Inscripción de ejercicios           96 horas
 8     Análisis IE                       1 día
 9     Diseño IE                         2 días     8;4
10     Codificación IE                   2 días     9
11     Prueba IE                         3 días     10
12   Registro de datos                  112 horas
13     Análisis RD                       2 días     3;8
14     Diseño RD                         3 días     13;4;9
15     Codificación RD                   3 días     14
16     Prueba RD                         2 días     15
```

**Resolución.** Jornada de 8 h (se confirma con Resolución de ejercicios: 2+3+3+4 = 12 días = 96 h).

```
comienzo(tarea) = máx(fin de cada predecesora) + 1
fin(tarea)      = comienzo + duración − 1
```

Hay que usar el **fin** de cada predecesora, no su duración: una tarea corta puede terminar tarde
porque a su vez esperó a otra. Por eso se arma la tabla completa en orden, aunque pregunten sólo RD.

```
Tarea                 Dur   Pred      Empieza   Termina
3  Análisis RE         2    –           1         2
4  Diseño RE           3    3           3         5
5  Codificación RE     3    4           6         8
6  Prueba RE           4    5           9        12
8  Análisis IE         1    –           1         1
9  Diseño IE           2    8;4         6         7    (espera a Diseño RE, día 5)
10 Codificación IE     2    9           8         9
11 Prueba IE           3    10         10        12
13 Análisis RD         2    3;8         3         4    (Análisis RE termina el día 2)
14 Diseño RD           3    13;4;9      8        10    (manda Diseño IE: termina el día 7)
15 Codificación RD     3    14         11        13
16 Prueba RD           2    15         14        15
```

**Respuesta:** Análisis RD → día **3** · Diseño RD → día **8** · Codificación RD → día **11** ·
Prueba RD → día **14**.

En Diseño RD, la predecesora que más dura es Diseño RE (3 días), pero termina el día 5. Diseño IE
dura 2 días y termina el día 7, porque no pudo empezar hasta que terminó Diseño RE.

**Control con las resumen.** Inscripción de ejercicios: días 1–12 = 96 h ✓. Incremento: días 1–15
= 120 h ✓. Registro de datos: días 3–15 = 13 días = **104 h**, no las 112 h del enunciado. Para
112 h, Análisis RD tendría que empezar el día 2, y su predecesora 3 termina ese día. El dato del
enunciado no cierra, pero no cambia los días de comienzo.

---

## 7. d) CMMI: relacionar actividad con área de proceso y práctica específica

**Consigna.** *"En el marco del proyecto 'APP para viajes compartidos', cada programador, antes de
pasar a la siguiente tarea, le entrega el programa que acaba de terminar a un integrante del grupo
de testing para que lo revise leyendo el código fuente, cumpliendo así su responsabilidad definida
en la planificación del proyecto."* Relacione con el área de proceso y la práctica específica que
corresponda (sólo una), o indique NINGUNA.

**Opciones.** REQM/SP 1.2 Obtener el compromiso sobre los requerimientos · CM/SP 2.2 Controlar los
elementos de configuración · PPQA/SP 1.2 Evaluar objetivamente los productos de trabajo y los
servicios · RD/SP 1.1 Obtener las necesidades · MA/SP 1.3 Especificar los procedimientos de
recogida y almacenamiento de datos · CM/SP 3.2 Realizar auditorías de configuración · PMC/SP 1.7
Llevar a cabo revisiones de hitos · VER/SP 2.1 Preparar las revisiones entre pares · PPQA/SP 2.2
Establecer registros · VER/SP 2.2 Llevar a cabo las revisiones entre pares · VAL/SP 2.1 Realizar la
validación · VER/SP 3.1 Realizar el control de estándares · PMC/SP 1.2 Monitorizar los compromisos
· PMC/SP 1.5 Monitorizar la involucración de las partes interesadas · RD/SP 3.5 Validar los
requerimientos · Ninguna de las otras opciones · NO CONTESTA.

**Respuesta:** **VER / SP 2.2 Llevar a cabo las revisiones entre pares.**

- Revisión **estática** (leer el código, sin ejecutarlo) de un producto de trabajo, hecha por otro
  integrante del proyecto → revisión entre pares → VER.
- Presente ("le entrega… para que lo revise") → **llevar a cabo** (SP 2.2), no preparar (SP 2.1)
  ni analizar los datos ya registrados (SP 2.3).
- No es PPQA: no se compara contra un estándar organizacional ni lo hace alguien externo al
  proyecto. No es VAL: no participa el usuario.
- La opción "VER/SP 3.1 Realizar el control de estándares" tiene el texto cambiado: VER SP 3.1 es
  *Realizar la verificación*, y el control de estándares es PPQA.

---

## 8. e) ¿Podrían surgir problemas de calidad?

**Consigna.** El procedimiento establecido indica que es obligatorio hacer revisiones entre pares
(internas en la SW factory) de todos los artefactos generados en un proyecto. Además, sobre el
código se hacen pruebas unitarias, de integración y de regresión, y una prueba de sistema al final
de cada iteración. Con esto se consideran cumplidos los objetivos de Verificación y Validación en
cuanto a aspectos funcionales, por lo que no se hace ningún otro tipo de prueba funcional. En los
casos en que se justifica se hacen pruebas no funcionales. Indique si podrían surgir problemas de
calidad, eligiendo una o varias afirmaciones, o NINGUNA. No se pueden combinar las de "sí hay
problemas" con las de "no".

**Opciones.**

1. No genera problemas de calidad; es una implementación correcta de CM.
2. No genera problemas de calidad, porque se cumplen los objetivos de Verificación y Validación.
3. Sí podría… porque faltan las pruebas funcionales internas en la SF, con lo cual no se cumplen
   los objetivos de Verificación.
4. No genera problemas de calidad, porque es muy bueno que se hagan revisiones entre pares.
5. Sí podría… porque faltan las revisiones de pares con usuarios.
6. Sí podría… porque las revisiones entre pares deberían hacerlas un grupo externo al proyecto.
7. Sí podría… porque no incluye la revisión de cumplimiento de estándares de la SF como parte de la
   Verificación y Validación.
8. Sí podría… porque faltan las pruebas funcionales internas en la SF, con lo cual no se cumplen
   los objetivos de Validación.
9. Sí podría… porque el mayor inconveniente es que las pruebas no funcionales deberían ser
   obligatorias para todos los objetos de software, en todos los atributos de calidad.
10. Sí podría… porque faltan las pruebas con usuarios, con lo cual no se cumplen los objetivos de
    Validación.
11. Sí podría… porque es inadmisible hacer revisiones entre pares de todos los artefactos.
12. Sí podría… porque no es compatible repetir pruebas unitarias en más de una iteración.
13. NINGUNA de las otras opciones / NO CONTESTA.

**Respuesta:** sólo la **10**.

La trampa es "se consideran cumplidos los objetivos de Verificación **y Validación**". Todo lo
descripto es VER (revisiones entre pares; pruebas unitarias, de integración, de regresión y de
sistema; prueba de sistema → VER, aceptación → VAL). No hay ninguna actividad con el usuario, así
que VAL no se cumple.

- 3 y 8: las pruebas funcionales internas existen.
- 5: la revisión entre pares es sólo de VER; con el usuario sería VAL, no "de pares".
- 6: las revisiones entre pares las hacen pares; el grupo externo es cosa de PPQA.
- 7: el control de estándares es PPQA, no VER ni VAL.
- 9: exagerada; hacer no funcionales cuando se justifica está bien.
- 11 y 12: falsas. 1, 2 y 4: hay problema.

---

## 9. f) Diagrama de conjuntos A / B / C

**Consigna.** Dado el gráfico (dos rectángulos superpuestos), donde **A** representa los procesos
organizacionales estándar definidos por la empresa, **B** los procesos y actividades que el
proyecto considera necesarios según sus características particulares, y **C** la intersección.
Un equipo debe definir los procesos que usará en un nuevo proyecto, considerando tanto los
estándares organizacionales como sus características particulares. ¿Qué afirmaciones interpretan
correctamente el gráfico y su relación con la gestión de procesos en CMMI?

1. C son los procesos comunes entre la organización y el proyecto; el proyecto debería limitarse
   exclusivamente a ellos, descartando cualquier actividad fuera de la intersección.
2. C es la coincidencia entre los procesos organizacionales y las necesidades del proyecto. Para
   definir su proceso, el proyecto debe considerar los estándares aplicables y hacer las
   adaptaciones necesarias según criterios organizacionales establecidos.
3. A − C son los procesos organizacionales que no coinciden con las necesidades del proyecto y que,
   por lo tanto, deben eliminarse de los estándares de la organización.
4. B − C son los procesos particulares del proyecto que necesariamente deben incorporarse a los
   estándares organizacionales para garantizar la mejora continua.
5. La definición del proceso del proyecto puede requerir incorporar actividades específicas no
   contempladas explícitamente en los procesos estándar, siempre que esas adaptaciones respeten
   los criterios y lineamientos establecidos por la organización.
6. NO CONTESTA.

**Respuesta:** **2 y 5.** Describen el *tailoring*: el proyecto parte del proceso estándar (A) y lo
adapta a sus necesidades (B) según los criterios y guías de adaptación de la organización (OPD).

- 1: "limitarse exclusivamente" niega la adaptación.
- 3: que un proyecto no use un proceso no implica borrarlo del estándar organizacional.
- 4: "necesariamente" es falso; lo propio del proyecto puede proponerse como mejora (OPF), no es
  obligatorio.

---

## 10. g) Cambio pedido por el cliente y REQM

**Consigna.** Durante una fase de desarrollo interno, el cliente le pide directamente a un
desarrollador un pequeño cambio en la interfaz. El equipo discute cómo gestionar la solicitud:

1. "Aunque el cambio parezca pequeño, debe registrarse y evaluarse su impacto antes de
   incorporarlo al proyecto."
2. "Si el cambio solicitado no modifica la funcionalidad principal del sistema, puede
   implementarse sin actualizar los requisitos documentados."
3. "Una vez que los requisitos fueron aprobados por el cliente, no deberían modificarse durante la
   etapa de desarrollo, para evitar desviaciones en el proyecto."
4. "Si el cambio es aprobado, es necesario revisar la trazabilidad de los requisitos y asegurar la
   consistencia con los productos de trabajo afectados, incluyendo los casos de prueba cuando
   corresponda."

¿Cuáles son coherentes con las prácticas de REQM de CMMI? Opciones: sólo 2 y 3 · sólo 1 y 4 ·
sólo 2 · todas (1, 2, 3 y 4) · NO CONTESTA.

**Respuesta:** **sólo 1 y 4.**

- 1 ✓: cambio pedido por el **cliente** → REQM (no CM); se registra y se evalúa su impacto antes
  de aceptarlo (SP 1.3 Gestionar los cambios en los requerimientos).
- 2 ✗: implementar sin actualizar los requerimientos deja inconsistentes documentos y producto
  (contradice SP 1.5 Identificar inconsistencias).
- 3 ✗: REQM no congela los requerimientos: gestiona sus cambios.
- 4 ✓: SP 1.4 Mantener la trazabilidad bidireccional + SP 1.5.
