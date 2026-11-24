# Podcasts CD — cómo usarlos en NotebookLM

Este archivo **no se sube**: es la guía. Se suben los ocho `0N-*.md`, uno por episodio.
Se regeneran desde el resumen y los bancos con `python3 scripts/cd/cd-podcasts.py`. Si cambia
`resumen-final.md`, corré el script de nuevo antes de volver a subirlos.

## Armado

1. Creá un cuaderno en NotebookLM y subí los ocho archivos como fuentes.
2. Para cada episodio, dejá tildada **solo su fuente** en el panel de fuentes. Si quedan todas tildadas, el podcast mezcla temas.
3. En *Audio Overview*, tocá **Personalizar**:
   - idioma: **español**;
   - formato: **Análisis en profundidad**;
   - duración: **más larga** para el 1, el 3 y el 6; la predeterminada para el resto;
   - en el cuadro de texto, pegá el prompt del episodio (abajo).
4. Generalo y pasá al siguiente.

## Prompts por episodio

Todos comparten el comienzo; cambia la última oración.

> Somos estudiantes de Ingeniería en Sistemas y rendimos el final de Comunicación de Datos: tres problemas de práctica y tres preguntas de teoría para desarrollar. Explicá con ejemplos concretos, usá las definiciones tal como están en la fuente, marcá los errores típicos y no leas fórmulas ni tablas en voz alta: contá qué significan y para qué sirven. Cerrá con dos o tres preguntas de las que tomaron en los finales, dando la respuesta y por qué.

| # | Archivo | Agregá al final del prompt |
|---|---|---|
| 1 | `01-mapa-y-teoria-de-la-informacion.md` | Usá la analogía de una videollamada para el recorrido del mensaje y explicá la información mutua como "lo que el canal deja pasar". |
| 2 | `02-transmision-multinivel.md` | Contá el problema del final 2025 como una receta de cinco pasos y aclará qué pasa con los pulsos de arranque y stop. |
| 3 | `03-codificacion-de-fuente.md` | Armá en voz alta la respuesta completa a "explicar código unívoco, instantáneo, compacto, Kraft y cota inferior". |
| 4 | `04-deteccion-y-correccion-de-errores.md` | Explicá el síndrome con la imagen de un detective que mira qué controles fallaron. |
| 5 | `05-modulacion.md` | Describí cómo se ve cada modulación como si la dibujaras en el pizarrón, y por qué QAM manda más bits con los mismos baudios. |
| 6 | `06-pcm-tdm-fdm.md` | Explicá la trama TDM como un tren con vagones y por qué el ancho de banda depende de la duración del pulso. |
| 7 | `07-medios-de-acceso.md` | Planteá tres empresas en zonas distintas y elegí el medio de cada una justificando. |
| 8 | `08-colas-y-repaso-del-final.md` | Hacé la última parte en formato quiz: planteá la pregunta, esperá un momento y explicá la respuesta. |

## Qué no va al audio

Las cuentas de los problemas (multinivel, trama PCM, canal binario, colas), el árbol de Huffman, las matrices G y H y la hoja de fórmulas se practican en papel con `resumen-final.pdf` y `banco-ejercicios.md`.
