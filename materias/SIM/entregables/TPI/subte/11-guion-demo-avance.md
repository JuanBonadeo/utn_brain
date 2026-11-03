---
title: "Guion de demo del avance - TPI Subte Constitución"
subject: "Simulación"
status: "Para la reunión con el docente del 2026-11-04 (10 min)"
---

# Demo del avance al docente (10 min)

Objetivo de la reunión: que el docente vea que el modelo existe y funciona, y **cerrar las decisiones que
bloquean la producción**. La defensa presencial es el **10 y 11 de noviembre**; esto es el último ensayo.

Todo lo que sigue sale de los archivos de esta carpeta, salvo lo marcado como *[general]* (conocimiento mío,
no verificado contra los materiales de la materia).

## Lo que tiene que quedar claro (y lo que no hay que decir)

| Sí | No |
|---|---|
| El modelo corre, está calibrado con datos reales de entrada (SBASE, horario oficial del Roca, plano de Trenes Argentinos) | "Los resultados dicen que E1 mejora 35 %" como resultado final |
| La tabla de resultados del 05/10 es **una corrida intermedia que prueba la cadena de análisis** (30 pares, IC con Bonferroni, reproducida en otra máquina) | Que la espera o la cola son las reales de Constitución: no hay dato para validarlas (solo el caudal agregado) |
| Se va a **re-correr** porque el modelo cambió el 02/11 (andén caminado, escalera B2, pasillo, demora 106 → 10 s + caminata) | Esconder que los resultados están desfasados |

## Preparación (hoy a la noche, ~30 min)

1. **Protocolo del `.alp`** ([02-modelo-anylogic.md](02-modelo-anylogic.md) §1): `git status` limpio del `.alp`;
   si existe `SubteConstitucion.alp.autosave`, renombrarlo a `.autosave.bak`; al abrir el IDE, responder **No**
   a restaurar el autosave.
2. **Figuras 3D**: en esta máquina no existe `entregables/TPI/subte/3d/`. Sin esas figuras el modelo abre pero
   los peatones no se ven en 3D. Correr `python datos/copiar_figuras_3d.py` desde la carpeta del subte. Ojo: la
   doc dice que copia desde la instalación de AnyLogic y el verificador menciona la ruta de Mac; no verifiqué
   que ande tal cual en Windows.
3. **Medir cuánto tarda la franja completa.** El piloto viejo tardó ~43 min; las corridas de producción del 05/10
   tardaban ~7 s, pero eso era antes del andén caminado y de los dos niveles (la propia doc advierte "más
   peatones simultáneos... medir el tiempo de corrida"). **No se sabe cuánto tarda hoy.** Probá `PeatonalE0`
   una vez antes de dormir:
   - si tarda menos de ~1 min a velocidad máxima: mostrarlo en vivo;
   - si tarda más: mostrar la animación en las primeras corridas (primer tren y su oleada) y tener **una captura
     de pantalla / grabación corta** del resto como respaldo.
4. Dejar abiertos en este orden: las slides o imágenes de apoyo (abajo), AnyLogic con `MainPeatonal`, y
   `04-resultados-corridas.xlsx` (hoja `Resumen`).
5. Imágenes de apoyo, ya en `materias/SIM/figs/`: `tpi-subte-perfil-demanda.png`, `tpi-subte-plano-acceso.png`,
   `tpi-subte-estacion-niveles.png`.
6. Anotar quién habla cada bloque con Juan (el guion del video usa turnos alternados; acá igual).

## Guion cronometrado

| Min | Bloque | Qué se muestra | Qué decir (idea, no texto) |
|---|---|---|---|
| 0:00-1:30 | **Problema** | `perfil-demanda.png` | Constitución es la terminal del Roca. En el pico, un molinete recibe un pasajero cada 8,5 s y valida en 2-3 s: ρ ≈ 0,3. Un M/M/c diría "sin cola". Pero los pasajeros llegan en **tandas** (47 trenes en la franja) y hay cola. Congestión transitoria por arribos en lote en un sistema subutilizado en promedio: ahí la fórmula falla y simular es la herramienta correcta. |
| 1:30-3:00 | **Datos reales** | `plano-acceso.png` | SBASE ene-jun 2026 por molinete (117 días hábiles; las 14 ventanas más cargadas de toda la red son de Constitución). Horario oficial del Roca vigente desde el 03/08 (47 trenes hábiles 07:00-09:30). Plano de Trenes Argentinos georreferenciado con OSM. Antecedentes: validación 2-3,5 s (Seriani 2025, Wang 2024), la cercanía domina la elección de molinete. Lo que **no** hay: tiempo de servicio ni espera real (no se puede medir desde Rosario). |
| 3:00-6:30 | **Modelo en vivo** | AnyLogic, `PeatonalE0` | Recorrido del pasajero: tren llega a su andén → baja por las 21 puertas → camina el andén y el hall (obstáculos del plano) → escalera B2 caminada en pendiente → pasillo → elige cola → molinete → zona paga. Mostrar las cámaras 3D (general, molinetes, pasillo, hall). Señalar el panel: espera media, P90, proporción > 30 s, cola. Aclarar qué es animación (trenes, vista 3D) y qué es lógica (la demanda sale de `liberacionesPed`). Mostrar E0 (20 molinetes) y, si el tiempo da, E1 (22) con **la misma semilla**. |
| 6:30-8:00 | **Resultados (intermedios)** | planilla, hoja `Resumen` | 30 pares con números aleatorios comunes, paired-t con IC Bonferroni (k = 3). Con el modelo del 05/10: P90 −9,8 s, proporción > 30 s de 8,5 % a 2,1 %, drenaje sin cambio. Reproducido en Windows con diferencias de décimas. **Decirlo explícito:** son del modelo anterior, se re-corren. Limitación propia: el IC es chico porque todas las réplicas usan el mismo perfil medio; la variación entre días reales no está. |
| 8:00-10:00 | **Decisiones que necesitamos** | (sin pantalla) | Las preguntas de abajo. Anotar las respuestas al momento. |

## Preguntas para el docente (en orden de importancia)

Salen de [08-consulta-catedra.md](08-consulta-catedra.md) más el aviso del 28/10. **No sé si la consulta se
llegó a enviar** (el borrador dice que la manda Juan); si no se mandó, esta reunión la reemplaza.

1. **Formato del informe.** El aviso del 28/10 pide paper (abstract, objetivos, metodología, resultados y
   conclusiones) con los 10 pasos *implícitos*; nuestro informe LaTeX tiene un capítulo por paso. ¿Se
   reestructura? (Cambia cuánto del trabajo hecho se reutiliza.)
2. **E1.** ¿"Habilitar los 22 del vestíbulo Principal" en lugar de "abrir los 28"? Hoy el checklist dice 20 vs 22 y
   el guion de video y la wiki dicen 20 vs 28.
3. **Parámetros sin dato** (tiempo de validación, descarga, demora, proporción Roca/calle): ¿se aceptan rangos con
   fuente (TCQSM, London Underground SPSG) y análisis de sensibilidad, con el intermedio para la comparación
   principal?
4. **Alcance:** E2 y E3 como extensión sin resultados; el informe compara E0 contra E1.
5. **AnyLogic Cloud.** La entrega pide el link del modelo. *[general, a verificar]*: creo que subir a Cloud
   requiere una licencia que la PLE no tiene; si es así, preguntar cómo lo resuelve la cátedra (¿cuenta
   de la facultad?) antes del 10.
6. **Defensa 10/11:** ¿qué escenario hay que mostrar en vivo? ¿Cuánto tiempo hay? ¿Va solo uno de los dos?

## Preguntas que probablemente te hagan (y la respuesta honesta)

| Pregunta | Respuesta |
|---|---|
| ¿Cómo validaron el modelo? | Solo el **caudal agregado** contra SBASE (por ventana de 15 min). La espera y el largo de cola reales no se pueden validar sin medición; está declarado. |
| ¿De dónde sale el tiempo de servicio? | Triangular (1,8; 2,4; 3,5) s, media 2,57, de la literatura (Seriani 2025; Wang 2024; Tian 2026) y la cota del propio dataset. Es supuesto con rango de sensibilidad. |
| ¿Por qué tanta diferencia entre E0 y E1 si ρ ≈ 0,3? | Porque la cola es de tandas, no de utilización promedio: con más molinetes se disipa antes la oleada. Eso es el argumento del trabajo. |
| ¿Por qué el IC es tan angosto? | Todas las réplicas usan el mismo perfil medio de demanda; falta sortear días reales. Mejora posible: sortear el perfil de uno de los 80 días hábiles de mar-jun por par. |
| ¿Qué cambió desde el 05/10? | Pasamos de una demora fija a simular el andén (21 puertas), el hall, la escalera B2 y dos niveles. Hay que re-correr la producción. |
| ¿Por qué la vista 3D? | Es solo visual; no cambia la lógica ni los números aleatorios. |

## Después de la reunión (hasta el 10/11)

Orden por riesgo, no por gusto:

1. **Piloto con el modelo actual** (cuánto tarda, si drena 100 %), y decidir E1 con la respuesta del docente.
2. **Re-correr los 30 pares**, cargar con `cargar_corridas.py`, `analisis_corridas.py`. Archivar el CSV anterior
   como se hizo el 02/11 (`corridas-descartadas/`).
3. **Informe:** pasos 7 a 10 vacíos (`[PENDIENTE: T5.4]`) + reestructurar a formato paper si el docente lo confirma.
4. **Link de AnyLogic Cloud** (puede bloquear, ver pregunta 5).
5. **Video ≤ 3 min** con ambos en cámara y sin editar: reemplazar `[RESULTADO]` en
   [05-guion-video.md](05-guion-video.md) y la presentación, que sigue diciendo 20 vs 28.
6. Actualizar [06-checklist-cierre.md](06-checklist-cierre.md) y la sección del subte de `SIM.md`
   (siguen en el estado de septiembre).
