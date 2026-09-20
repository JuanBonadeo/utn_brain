# Plantillas de entregables

## Cómo arrancar un TP nuevo

    cp scripts/templates/tp.md materias/XXX/entregables/nombre-del-tp.md

Completá el frontmatter, escribí el cuerpo y generá el PDF:

    node scripts/monografia-pdf.js materias/XXX/entregables/nombre-del-tp.md

Sale un PDF con carátula, índice automático, A4, Arial 10, interlineado 1.5,
texto justificado y numeración de páginas — el formato que piden las cátedras.

## Dónde están los datos fijos

`scripts/datos-alumno.json`: institución, facultad, carrera, nombre, correo,
legajo y la comisión por materia. Se editan ahí una sola vez, no en cada TP.
Cualquier campo se puede pisar desde el frontmatter del `.md` del trabajo.

## Opciones

| Flag | Efecto |
|---|---|
| `--no-cover` | sin carátula |
| `--no-toc` | sin índice |
| `--html-only` | deja el `.html` sin imprimir (para ajustar estilos) |

## Logo

Si existe `scripts/templates/logo-utn.png` se incrusta en la carátula. Si no
está, la carátula sale sin logo (no rompe).

## El otro conversor

`scripts/build-docx.js` genera `.docx` en vez de PDF. Usalo cuando la cátedra
pida Word o cuando haya que entregar algo editable.
