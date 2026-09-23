# Brain académico UTN

Este repositorio es una wiki académica personal de 4.º año de Ingeniería en
Sistemas (UTN). Trabajá directamente sobre sus archivos y priorizá material
existente antes de aportar conocimiento general.

## Fuente de instrucciones

- `CLAUDE.md` es la guía operativa canónica y detallada del repositorio.
- Este `AGENTS.md` permite que agentes que siguen la convención `AGENTS.md`
  (incluidos los de OpenAI/Codex) adopten esa misma guía.
- Si hay una contradicción, prevalece `CLAUDE.md`, salvo instrucciones de
  mayor prioridad entregadas por la plataforma o por el usuario.

**Antes de cualquier tarea**, leé completo [`CLAUDE.md`](CLAUDE.md) y seguí
sus reglas de estructura, ingesta, consultas, lint, Git y tono.

## Reglas irrenunciables

- Cada materia vive exclusivamente en `materias/[CÓDIGO]/` y su wiki
  `[CÓDIGO].md` es la única fuente de verdad curada.
- `fuentes/` y `archivo/` son inmutables. No editar, mover ni borrar archivos
  allí; los insumos binarios se convierten con `scripts/ingest.py` antes de
  analizarlos.
- Al incorporar material, fusionarlo en la unidad correspondiente de la wiki,
  actualizar el índice si hace falta y registrar el cambio en el Log.
- Para responder consultas, leer primero la wiki relevante y distinguir con
  claridad lo que proviene de ella de conocimiento general externo.
- No sobrescribir ni eliminar trabajo existente sin una autorización explícita.
- Respetar el flujo Git definido en `CLAUDE.md`; no incluir archivos generados,
  dependencias ni basura del sistema cuando estén excluidos por sus reglas.

## Compatibilidad de herramientas

No presupongas herramientas exclusivas de un proveedor. Cuando una instrucción
requiera una herramienta no disponible, aplicá un equivalente seguro y
explicá brevemente cualquier limitación material.
