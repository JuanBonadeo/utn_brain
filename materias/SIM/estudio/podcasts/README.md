# Podcasts SIM — cómo usarlos en NotebookLM

Este archivo **no se sube**: es la guía. Se suben los ocho `0N-*.md`, uno por episodio.
Se regeneran desde el resumen y el banco con `python3 scripts/sim/sim-podcasts.py`.

## Armado

1. Creá un cuaderno en NotebookLM y subí los ocho archivos como fuentes.
2. Para cada episodio, dejá tildada **solo su fuente** en el panel de fuentes. Si quedan todas tildadas, el podcast mezcla temas.
3. En *Audio Overview*, tocá **Personalizar**:
   - idioma: **español**;
   - formato: **Análisis en profundidad**;
   - duración: **más larga** para el 6 y el 7, y la predeterminada para el resto;
   - en el cuadro de texto, pegá el prompt del episodio (abajo).
4. Generalo y pasá al siguiente.

## Prompts por episodio

Todos comparten el comienzo; cambia la última oración.

> Somos estudiantes de Ingeniería en Sistemas y el sábado rendimos un parcial multiple choice de Simulación. Explicá con ejemplos concretos, usá las definiciones tal como están en la fuente, marcá las trampas típicas de las preguntas y no leas fórmulas ni tablas en voz alta: contá qué significan. Cerrá con tres o cuatro preguntas de las del final, dando la respuesta y por qué.

| # | Archivo | Agregá al final del prompt |
|---|---|---|
| 1 | `01-que-es-simular.md` | Enfocate en distinguir sistema, modelo y simulación, y verificación de validación. |
| 2 | `02-eventos-discretos-cola-simple.md` | Contá la traza de la cola como una historia de clientes que llegan y se van. |
| 3 | `03-inventario.md` | Explicá por qué aparece el backlog y qué costo va con cada nivel de inventario. |
| 4 | `04-colas-1.md` | Explicá la ley de Little con un ejemplo y por qué ρ tiene que ser menor que 1. |
| 5 | `05-colas-2.md` | Usá los ejemplos resueltos para mostrar cuándo conviene agregar un servidor. |
| 6 | `06-probabilidad.md` | Separá bien qué cuenta la Poisson y qué mide la exponencial, y qué dice cada ley límite. |
| 7 | `07-numeros-aleatorios.md` | Explicá por qué fallan los generadores malos y la idea de la transformada inversa. |
| 8 | `08-anylogic-y-trampas.md` | Hacelo en formato quiz: planteá cada pregunta, esperá un momento y explicá la respuesta. |

## Qué no va al audio

La traza numérica de la cola, el ejercicio de inventario del 2025, la tabla de las 9 distribuciones y las fórmulas de colas se practican en papel con `resumen-parcial1.pdf` y `banco-preguntas.pdf`.
