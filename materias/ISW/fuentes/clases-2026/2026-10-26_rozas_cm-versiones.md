# Clase del 26/10/2026 (Rozas) — CM 2/2: versiones

Material de Classroom "NC-20261026-CM 2/2" (publicado el 28/10) y tarea "Trabajando con versiones"
(26/10, 100 puntos, entregada por el Grupo 1). Texto extraído el 2026-11-19 de los adjuntos:
CM-P04-Versiones.v1.02.pptx, CM-P04-Versiones-ciclos.v1.0.pptx, CM-P05-Artefactos.pptx y el
documento de clase TT-20261026-CM 2/2.

## CM-P04 Versiones y variantes (v1.02, 21/10/26, ALRO)

- **Versión:** evolución **temporal** de un elemento. **Variante:** evolución **espacial** de un elemento.
- Conceptos:
  - **Alpha:** se usa para prueba, no tiene toda la funcionalidad, puede tener muchos errores. Trabaja un grupo interno.
  - **Beta:** más madura que la alfa pero inestable. Tiene la mayoría de las funciones principales y se lanza a un grupo de usuarios más amplio (o al público, "beta abierta") para encontrar errores que el equipo interno no detectó.
  - **Versión candidata (Release Candidate, RC):** versión previa al lanzamiento definitivo.
  - **Release:** versión distribuible, de lanzamiento, incluida la documentación.
  - **Versión de desarrollo (development build, dev build, db):** compilación para uso interno, pruebas y programación; no es para el usuario final.
  - **Hotfix.**
- **Versionado semántico:** `<Mayor>.<Menor>.<Parche> -(<etiqueta>)`. Indica reglas de inicio y de cambio. Hay orden de precedencia: 1.0.2 < 1.1.0. Etiquetas: 1.1.0-Alpha < 1.1.0-beta.1 < 1.1.0-beta.2.
- **Retrocompatibilidad:** la nueva versión interactúa bien con datos, archivos o interfaces de versiones anteriores y funciona en los entornos preexistentes.
  - **Hacia atrás (backward):** la versión nueva entiende lo creado para una anterior. La más común y deseada.
  - **Hacia adelante (forward):** una versión vieja procesa lo generado por una más nueva (o se degrada sin fallar).
  - V1.0.0 → V1.1.0: SemVer indica retrocompatible. V1.0.0 → V2.0.0: el cambio en la sección mayor indica incompatibilidad.
- **Tipos de versionado:** en la convención de nombres; a través de metadatos; carpetas; sistemas de control de versiones (Git).

## CM-P04 Versiones y ciclos (v1.0, 22/10/26)

- **Cascada:** una entrega, v1.0.0.
- **Incremental:** Inc-1 v1.0.0, Inc-2 v1.1.0, Inc-3 v1.2.0.
- **Iterativo:** It-1 v0.1.0, It-2 v0.2.0, … hasta v1.0.0 y luego v1.1.0 … v1.6.0.
- **Ciclo de vida del producto:** V1.0.0 → V1.0.1 (+ hotfix arregla x) → V1.0.2 (+ hotfix arregla y).

## CM-P05 Productos de trabajo de CM (v1.00, 21/10/26)

Productos de trabajo: **Inventario**, **Notas de versión**, Aprobación, Matriz de trazabilidad con requerimientos.

- **Inventario:** documento que deja testimonio, por escrito y sin ambigüedades, de qué elementos exactos componen una versión, paquete o línea base.
  - Producto + Datos-inventario + 1{EC + {archivo}}n (EC = elemento de configuración)
  - Datos-inventario = Nombre + Versión + fecha-aprobación-congelamiento + Estado + Responsable-CM + 1{aprobación} + (versión-anterior) + … + (observaciones)
  - Archivo = Nombre + Versión + Ubicación + fecha-actualización + Responsable + Estado + … + (observaciones)
  - Aprobación = {apellido-nombre-aprobador + rol + firma + …}
- **Notas de versión:** responden "¿qué hay de nuevo?, ¿qué cambió respecto de la versión anterior y qué problemas se solucionaron?". Resumen funcional para el usuario o el equipo.
  - Producto + versión + fecha-emisión-lanzamiento + descripción-contenido + (versión-anterior) + …

## Documento de clase TT-20261026-CM 2/2

Políticas de versiones (ejemplo):

- P1: se usa versionado semántico (`<mayor>.<menor>.<parche>(-etiqueta)`).
- P2: cada vez que aparece un error grave se incrementa en uno el parche.
- P3: cada vez que se agrega una funcionalidad se incrementa el menor; el parche vuelve a 0 y el mayor se mantiene, salvo que la funcionalidad rompa la compatibilidad hacia atrás.
- P4: cuando una versión no es retrocompatible se incrementa el mayor y el resto se reinicia.

Es importante definir: convención de nombres de archivos y carpetas (se explicita al planificar el proyecto), convención y forma de versionado, políticas de versionado y procedimientos.

En el release aparecen dos artefactos nuevos: **inventario** (declara al menos todos los componentes del software en esa versión) y **notas de versión** (novedades respecto de la anterior: funcionalidades nuevas, correcciones de errores graves, modificaciones y eliminaciones).

## Tarea "Trabajando con versiones" (26/10, fecha límite 27/10)

Consigna: "Realizar un ordenamiento de las versiones y responder qué tiene el cliente y qué se viene
de nuevo en un futuro". Versiones: 2.0.0, 2.0.0-dev, 2.1.0-dev, 2.2.0-dev, 2.2.0-alpha,
2.0.0-beta, 2.0.1-rc, 2.0.2-rc. Nota: "dev ES LA ETIQUETA PARA DESARROLLO".

Resolución de la clase (documento TT):

- Orden: 2.0.0-dev → 2.0.0-beta → 2.0.0 → 2.0.1-rc → 2.0.2-rc → 2.1.0-dev → 2.2.0-dev → 2.2.0-alpha
- Lo que tiene el cliente: **2.0.0**
- Versiones posibles (lo que viene): 2.0.1-rc, 2.0.2-rc, 2.2.0-alpha

Entrega del Grupo 1 (documento "Grupo 1 - Trabajando con versiones"): el mismo orden y las mismas
respuestas, con dos erratas en la lista ("2.2.0" por 2.2.0-dev y "2.0.2-alpha" por 2.2.0-alpha).
