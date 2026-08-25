# Handoff — ASI, TP Integrador Etapa 3

> Documento de traspaso. Pegalo entero como contexto en un asistente, o leelo vos.
> Actualizado al 2026-08-23. Entrega: **28/08/2026**.

## Contexto

Materia: Administración de Sistemas de Información, 4º año Ingeniería en Sistemas, UTN FRRo.
Comisión 403, Grupo 310. Empresa analizada: **Personal (Telecom Argentina)**. Proceso crítico:
**instalación de internet con fibra óptica**.

## El proyecto — ya validado por el docente, no lo cambies

> Implementar una plataforma de gestión de órdenes de trabajo con aplicación móvil de campo
> para resolver trazabilidad, priorización y control de competencias técnicas en instalaciones
> de fibra óptica.

Modo de construcción indicado por el docente el 23/08: **SaaS FSM configurable**. La
organización **no** construye el producto: lo configura, construye las integraciones (SGOT,
CRM, base de datos, NMS) y la capa de seguridad. Nunca escribas que se "desarrolla" la
plataforma.

El docente también redefinió qué son las "alternativas" del punto 3: no son modos de construir
lo mismo (interno / SaaS / tercerizado) sino **proyectos distintos que atacan otros problemas**.
Quedaron tres, con las dos últimas solo mencionadas: OT-Campo (la elegida), seguridad perimetral
e identidades (R03 y R05), y capacidad y mantenimiento de planta externa (R11 y R08).

## Dónde está todo

Repo `github.com/JuanBonadeo/utn_brain`. Se trabaja y pushea **directo a main**, sin ramas.

| Ruta | Qué es |
|---|---|
| `materias/ASI/ASI.md` | Wiki de la materia, ~5400 líneas. Fuente de verdad conceptual. Buscá con grep. La sección *TP Integrador → Etapa 3* tiene el estado, las decisiones D1–D5 y el historial completo en el Log del final |
| `materias/ASI/entregables/etapa3.md` | **EL ENTREGABLE.** Los 12 puntos + Acta como Anexo I. Fuente de verdad: el `.docx` y el `.pdf` se generan desde acá, no se editan a mano |
| `materias/ASI/entregables/etapa3.docx` | Generado. 53 páginas |
| `materias/ASI/entregables/etapa3-acta-proyecto.md` | El Acta suelta, para control interno. Va embebida en el entregable |
| `materias/ASI/entregables/etapa3-validacion-punto3.md` | Lo que se le mandó al docente el 19/08. Registro histórico |
| `materias/ASI/estudio/` | Los `.docx` corregidos de las Etapas 1 y 2 |
| `materias/ASI/fuentes/` | Material de cátedra, consigna, sugerencias, entregas anteriores, BPMN |

## Estado: los 12 puntos están escritos

Falta solo lo de abajo.

### Pendiente 1 — cuatro dibujos (es lo único que bloquea la entrega)

El documento los promete como adjuntos y no existen. El conversor a `.docx` no admite imágenes,
así que van en archivo aparte.

| Qué | De dónde salen los datos |
|---|---|
| Diagrama de Red | Tabla del punto 10: predecesoras, duración, ES/EF/LS/LF y holgura de las 51 actividades, con las críticas en negrita. Es transcribir, no diseñar |
| Diagrama de Gantt | Misma tabla, más la tabla de fases. Barras por actividad, camino crítico destacado, holguras en trazo discontinuo, histograma de recursos al pie |
| Plano de la base operativa | Punto 6, sección *Especificación de los planos*. Depósito y pañol, playa de carga, mesa de despacho, oficina del NOC y sala técnica |
| Croquis de trabajo en campo | Ídem. Escena de tendido aéreo con vallado |

Los dos planos tienen su especificación escrita elemento por elemento. Seguila, sirve de
instructivo.

### Pendiente 2 — dos datos del Acta (punto 4.4 / Anexo I)

- Nombres propios del patrocinador y del director de proyecto designado.
- Monto de la autoridad de compra.

Están marcados en el documento. Es decisión del grupo, no se inventan.

### Pendiente 3 — cuatro consultas al docente sin responder

El mensaje ya está redactado en la wiki, listo para copiar. Mientras tanto el grupo decidió y
siguió, dejándolas marcadas como revisables:

- Líneas base declaradas como supuestos, con su medición como entregable de la fase 2.
- Cronograma en meses relativos desde la aprobación del Acta, no en fechas de calendario.
- Justificación de la selección cualitativa, sin matriz ponderada.

La cuarta, la fecha de entrega, ya se sabe: 28/08.

## Números clave — no los recalcules a mano

Salen de un CPM real sobre la EDT, reproducible con los scripts.

| | |
|---|---|
| Duración teórica a fechas tempranas | 187 días hábiles |
| Camino crítico | 30 actividades |
| Aplanada con 1 persona por perfil | 215 días |
| **Aplanada con +1 integrador y +1 tester** | **192 días hábiles (~9,1 meses)** — la adoptada |
| Esfuerzo | 4.240 horas-persona, 9 perfiles (JP, AF, EI, ES, CP, UX, QA, CA, RO) |
| Presupuesto año 1 | USD 328.226 |
| TCO a 3 años | USD 531.460 |
| VAN a 5 años al 15% | +USD 31.515 |
| TIR | 19,0% |
| Repago | 3,14 años |
| Umbral de indiferencia | 85% de realización de beneficios |
| Dotación supuesta | 60 técnicos, 78 usuarios licenciados, 63 dispositivos |

El resultado económico es **viable pero de margen estrecho**, y está escrito así a propósito:
a tres años el proyecto todavía no se repaga. No lo maquilles.

## Cómo regenerar el documento

```
npm install                                    # una sola vez; necesita Node
npm run docx -- materias/ASI/entregables/etapa3.md materias/ASI/entregables/etapa3.docx
```

**Antes de dar por bueno un cambio, mirá el render, no el markdown.** Revisando a ciegas se
colaron listas con numeración encadenada, celdas con ríos de espacio y una tabla con la primera
columna en ancho negativo.

```
# Windows
powershell -File scripts/preview-docx.ps1 materias/ASI/entregables/etapa3.docx
# macOS
scripts/preview-docx.sh materias/ASI/entregables/etapa3.docx
```

Si agregás o modificás tablas, corré después el ajuste de anchos de columna:

```
.venv/Scripts/python.exe scripts/fix-cols-md.py materias/ASI/entregables/etapa3.md --write
```

Verificá que una **segunda corrida dé cero cambios**. Si sigue proponiendo ajustes, algo quedó mal.

Si tocás la EDT (duraciones, dependencias, perfiles) hay que rehacer los números:

```
.venv/Scripts/python.exe scripts/cpm-edt.py        # CPM, aplanamiento, carga por perfil
.venv/Scripts/python.exe scripts/costos-etapa3.py  # costos, TCO, VAN, TIR, repago
```

Y después actualizar a mano los puntos 5, 10, 11 y 12 del entregable con los valores nuevos.

## Convenciones del documento — respetalas o se rompe el conversor

- Solo soporta: `## sección`, `### apartado`, `#### subapartado`, párrafos, listas `- ` y `1. `,
  `> citas`, `---`, tablas, `**negrita**`, `*itálica*`, `` `código` ``. **Nada de imágenes, HTML,
  enlaces markdown ni notas al pie.**
- Toda tabla lleva antes su directiva de anchos: `<!-- cols: 20,50,30 -->`, que suman 100.
- Fuente **Lexend**, encabezados de tabla en celeste `DCE9F7` con texto azul `15406B`.
- Registro académico formal, tercera persona. Lo lee un docente.
- Todo valor numérico que no salga de las Etapas 1 y 2 va declarado como supuesto.

## Cuidado con

- **Los puntos 11 y 12 comparten base de costos.** Si cambiás la dotación o un precio hay que
  recalcular ambos: adquisiciones, estructura de costos, TCO, sensibilidad y toda la evaluación
  económica. Ya se rompió una vez por esto — el 11 quedó escrito sobre 220 técnicos y el 12 sobre
  60, y hubo que reconciliar todo a mano. Por eso existe `scripts/costos-etapa3.py`: hay un solo
  lugar donde tocar.
- **Los IDs de riesgo (R03 a R11)** vienen de la Etapa 2 y se citan en varios puntos. R04 y R07
  son los que el proyecto trata; R03 y R05 son los de severidad 15.
- **Arrastres de etapas anteriores sin resolver:** faltan las fechas de corrección de la Etapa 2
  para su tabla de versiones, falta el archivo del organigrama de Personal, y R09 sigue sin
  planilla de tratamiento.
