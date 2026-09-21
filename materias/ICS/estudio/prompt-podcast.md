# Prompt para podcast de repaso — parcial de Regularización

Fuente única: `resumen.pdf` (versión completa de 26 páginas, alineada al temario).
Pensado para NotebookLM (Resumen de audio → Personalizar). Formato sugerido: **Análisis en
profundidad**, duración **Más larga**, idioma **Español**.

## Versión completa

```text
Generá un podcast de repaso para un estudiante de 4.º año de Ingeniería en Sistemas que rinde el sábado el parcial de Regularización de Ingeniería y Calidad de Software. El examen es presencial, de opciones múltiples y NO es a libro abierto: tiene que salir del podcast sabiendo reconocer conceptos, nombres exactos y trampas. Usá únicamente el documento cargado; no agregues temas que no estén ahí.

TONO Y FORMATO
- Español rioplatense, dos voces. Una explica; la otra hace de alumno que pregunta y que cae en las confusiones típicas, para que la primera lo corrija.
- Para cada concepto: primero un ejemplo concreto, después la definición, después la confusión típica.
- Usá los nombres literales de las áreas, metas y prácticas de CMMI, porque así aparecen en las opciones del examen. La primera vez que aparezca una sigla, decí qué significa.
- Cada tanto, frená y hacé una pregunta estilo parcial ("¿esto es verificación o validación?"), dejá un segundo para pensar y respondé explicando por qué.
- Sin introducciones largas ni relleno.

CÓMO REPARTIR EL TIEMPO

Prioridad máxima (alrededor del 60 % del episodio):
1. Componentes de un área de proceso: lo requerido son sólo las metas (específicas y genéricas); las prácticas son esperadas; lo genérico trata la institucionalización.
2. Niveles de madurez: qué caracteriza a cada uno, las diferencias entre 2 y 3 y entre 4 y 5, y las reglas del modelo escalonado (hay que cumplir todas las áreas del nivel y de los anteriores; los niveles son acumulativos). Resolvé en voz alta el caso "cumple todo el nivel 3 pero le falta MA". Qué áreas hay en cada nivel, y la errata de OT.
3. OPF, OPD y OT: propósito, metas y prácticas de cada una; la regla "OPF diagnostica y despliega, OPD define y guarda, OT capacita"; y por qué el repositorio de medición de la organización es de OPD y no de MA.
4. Activos de proceso versus productos de trabajo, con varios ejemplos para clasificar.
5. Verificación versus validación: la distinción, el criterio de "contra qué se contrasta", sus metas y prácticas, y que las revisiones entre pares existen sólo en VER.
6. Técnicas dinámicas: cómo elegir la técnica según el enunciado; particionamiento de equivalencia (incluida la partición intermedia donde el sistema no hace nada); valores límite; tablas de decisión (cómo contar condiciones, acciones y columnas, condiciones de más de dos valores y combinaciones imposibles); transición de estados y casos de uso.

Prioridad media (alrededor del 30 %):
7. PP y PMC: propósitos y metas; cómo distinguirlas según la reunión esté en el futuro o ya haya ocurrido; qué es un desvío significativo; cuándo se definen los controles; los grupos de procesos de gestión; la EDT, las predecesoras directas y la diferencia entre esfuerzo y duración.
8. SPEM y RUP: quién, qué y cómo; los niveles de detalle; fase, disciplina, actividad, tarea, rol, producto de trabajo y los tipos de guía.
9. Los principios de Myers, por qué el desarrollador no debe probar su propio código, y regresión versus confirmación.
10. Puntos función: componentes, ponderación y factor de ajuste.

Repaso rápido (el resto): definiciones y tipos de calidad, características del software, tipos de mantenimiento, ciclos de vida, niveles de prueba, tipos y roles de las revisiones, y métodos de estimación.

CIERRE
Terminá con las ideas que más se confunden, tomando la sección final del documento, en formato "si en el examen ves X, pensá Y".
```

## Versión corta (si el campo tiene límite de caracteres)

```text
Podcast de repaso en español rioplatense para un parcial de opciones múltiples, sin libro. Priorizá: componentes requeridos de CMMI (sólo metas), niveles de madurez y sus reglas, OPF/OPD/OT con sus prácticas, activo vs producto de trabajo, VER vs VAL, y técnicas de prueba. Menos tiempo a PP/PMC, SPEM/RUP, Myers y puntos función. Un host hace de alumno que cae en las confusiones típicas y el otro lo corrige. Hacé preguntas estilo parcial. Cerrá con las ideas clave.
```

## Si queda superficial

Generá dos episodios con el mismo prompt, agregando al principio:

- Episodio 1: `Este episodio cubre sólo CMMI, gestión de procesos, SPEM/RUP y gestión de proyectos (puntos 1 a 4, 7, 8 y 10).`
- Episodio 2: `Este episodio cubre sólo verificación, validación y pruebas (puntos 5, 6 y 9).`
