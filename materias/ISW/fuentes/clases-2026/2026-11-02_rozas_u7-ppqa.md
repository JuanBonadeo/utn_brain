# Clase del 02/11/2026 (Rozas) — U7: PPQA

Material de Classroom "NC-20261102 - PPQA" (documento de clase TT-20261102) y "Practica de PPQA
(no es para entregar)", ambos del 2/11. La práctica es un enlace al OneDrive de Rozas con el PDF
`IS-PRACT-PPQA01_enum-practica_v1.00.pdf`, el mismo que está en `../practica-ad/`. Texto extraído
el 2026-11-19.

## Documento de clase TT-20261102

**PPQA: aseguramiento de calidad de productos de trabajo y procesos.**

- Propósito: dar una visión objetiva a la gerencia y al equipo sobre la **adherencia** de los productos de trabajo y los procesos, en el marco del proyecto.
- VER, VAL y PMC se complementan con PPQA. Se busca observar y medir si se cumplen los procesos y productos de trabajo.
- **VER controla la correctitud del contenido; PPQA se centra en el contexto del contenido.** Ejemplo:
  - ¿El caso de uso **alcanza** la meta? → **VER**
  - ¿El caso de uso **tiene** meta? → **PPQA**
- VER y PPQA se evalúan juntas en algunas situaciones.
- PPQA busca medir la **cobertura, la completitud y el uso** de productos de trabajo y procesos.
- Se lleva adelante con un **proceso de auditoría**, que puede implementarse de distintas formas:
  1. Lo hace un **par**, en general fuera del equipo.
  2. **Área de QA** totalmente externa al proyecto, que no depende del líder de proyecto ni del jefe del líder; en general depende directamente de la gerencia.
  3. **Tercerizar** el servicio con otra organización.

**Proceso:** planear la auditoría → evaluar los procesos y productos de trabajo → preparar resultados
→ acordar la resolución de las no conformidades → evaluar el cumplimiento de los acuerdos →
escalar las no conformidades.

- **Planear la auditoría:** qué se va a auditar y cuándo → **plan de aseguramiento de calidad** → agenda → se publica → se mezcla con el cronograma del proyecto.
- **Evaluar procesos y productos de trabajo:** el auditor busca **evidencias** de que se realizan los productos y procesos. El artefacto es la **lista de comprobación (checklist)**, que recopila evidencias.
- **Preparar resultados:** al consolidar lo recopilado por los auditores aparecen elementos no deseados → **no conformidades**.
- **Escalar las no conformidades:** informar al superior que no se está cumpliendo con la resolución de las no conformidades.
- Las NC descubren problemas subyacentes en el proceso, en los productos de trabajo o en la interpretación. Hay que analizar sus causas. **En general los auditores no dan opinión: presentan las situaciones.**

**Lista de comprobación:** Cabecera + ítems + pie.

- Cabecera = qué se evalúa, cuándo, quién, etc.
- Pie = la **lista de escalamiento** y la fecha en que son anoticiados.
- Ítem = {nro + pregunta / afirmación + respuesta}, o agrupados por categoría: {categoría + {nro + pregunta + respuesta}}.

Ejemplo de ítems para un caso de uso:

1. El nombre del CU está indicado → Sí / No
2. El CU tiene meta
3. El CU menciona el actor primario
4. Están presentes las precondiciones
5. El CU presenta disparador → Sí / No
6. El CU describe el camino básico → Sí / No
7. El CU describe el camino alternativo → Sí / No
   1. Si el CU no describe camino alternativo debería decir `<vacío>` → Sí / No
8. El CU describe postcondiciones de negocio o de sistema → Sí / No (quizás armar dos ítems)
9. Todas las entradas del camino básico poseen flujo de datos de entrada → Sí / No
10. Indique cantidad de entradas en los pasos
11. Indique cantidad de FE en el diccionario

## Práctica IS-PRACT-PPQ01 (v1.00, 06/11/14, ALRO), "no es para entregar"

1. **Lista de comprobación de casos de uso.** Meta: "Establecer el grado de adherencia a la plantilla de casos de uso utilizada en el desarrollo de proyectos en nuestra empresa". Primero se define la plantilla de CU (cualquiera usada en la carrera).
2. **Lista de comprobación del proceso de planificar proyecto.** Meta: "Determinar el grado de aplicación del proceso de planificación de un proyecto". Proceso (no completo): 1. Establecer los requerimientos funcionales. 2. Establecer los no funcionales. 3. Priorizar los requerimientos. 4. Definir la estructura de trabajo que permite visualizar cómo se alcanzan los requerimientos. 5. Definir la estructura del equipo. 6. Definir tiempos, costos. 7. Asignar las personas al proyecto. 8. …
3. **Lista de comprobación para el procedimiento de la tarea "Realizar codificación de requerimientos"** de una software factory hipotética. Meta: "Determinar el grado de adherencia al procedimiento". Responsable: programador. Requisitos: no tiene trabajos pendientes; tiene instaladas las herramientas. Pasos: (1) el LP comunica por un medio documental la asignación; (2) el programador verifica que está asignado al proyecto con esa tarea; (3) llegada la fecha, se reúne con su referente para determinar el trabajo; (4) realiza la tarea; (5) al terminar la jornada indica las horas trabajadas (4 y 5 se repiten a diario); (6) al finalizar, lo indica al LP por un medio documental. Excepciones: 2.a no encuentra la asignación → lo comunica por un medio documental al LP; 3.a no pudo reunirse con el referente → lo comunica formalmente; 4.a tiene dudas → consulta al referente, que lo soluciona; 4.a.2.a si no se puede resolver, el referente se comunica con el LP y se suspende temporalmente la tarea.
