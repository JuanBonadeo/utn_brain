---
title: "Plan completo del TPI - Molinetes de Constitución, Línea C"
subject: "Simulación"
status: "Plan de ejecución; requiere decisiones D1-D8 antes de la fase 3"
fecha: 2026-09-24
grupo: "Bonadeo - Estevez (comisión 401)"
---

# Plan completo del TPI de subte

Este documento surge de una sesión de planificación del 2026-09-24. En esa sesión se leyeron los archivos 01-06, `SIM.md`, el `.alp`, la planilla y los scripts, sin modificar el modelo, el informe ni la planilla. Se corrió `verificar_modelo.py`, se consultó la ayuda offline de AnyLogic 8.9.x, se reprocesó el dataset SBASE 2026 y se revisaron fuentes externas.

Convención usada en todo el plan:

- **[DATO]**: dato con fuente citada.
- **[SUP]**: supuesto declarado.
- **[PEND]**: pendiente que depende de terceros.
- **[VERIF]**: comprobado en esta sesión.

## 1. Resumen ejecutivo

1. **El modelo existe, pero ninguna corrida de la franja completa terminó bien.** El único piloto no drenó y además tardó ~43 min. La corrección de las colas invertidas **no está confirmada**. Lo primero es un piloto corto y barato que no necesita datos externos.
2. **Hallazgo nuevo que invalida E1 tal como está escrito.** En el dataset SBASE 2026 el vestíbulo Principal tiene **22 identificadores de molinete**: `Turn09`-`Turn29`, con tráfico, y `Turn07`, casi sin uso. Los "28 instalados" son el total de la **estación** e incluyen los 7-8 de Plaza [VERIF]. Hay que redefinir E1 (decisión **D1**) antes de producir.
3. **No hace falta esperar a SBASE, Emova ni Trenes Argentinos.** Hay fuentes citables para acotar el tiempo de validación, la descarga y la marcha: TCQSM 3.ª ed. (TRB), SPSG de London Underground y la cota empírica de SBASE. Con eso se proponen rangos a la cátedra y la respuesta de los organismos queda como mejora, no como requisito.
4. **Cómputo.** PLE permite corridas en paralelo, pero hoy están desactivadas, y los experimentos tienen 512-1024 MB de memoria [VERIF]. La recomendación es escalonada: primero corregir y medir; después paralelizar y repartir entre dos máquinas. Recién si nada de eso alcanza, acotar el horizonte a la hora pico. La capa lógica queda como plan B.
5. **Brechas formales con la consigna:**
   - no hay TeX, pandoc, OBS ni Zoom instalados;
   - las diapositivas son `.pptx`, no Google Slides;
   - no existe localmente ninguna "pauta de entregas parciales" ni plantilla LaTeX.

   Todas son tareas cortas y en paralelo, salvo la plantilla: esa es una pregunta para Classroom.
6. **Camino crítico:** D1 y rangos → piloto corto → piloto de franja con tiempo medido → producción E0-E1 → análisis → informe LaTeX y video.

### Camino crítico

```text
D1 (redefinir E1) ─┐
D2 (rangos, cátedra)┼─► F3 calibración ─► F4 producción E0-E1 ─► análisis ─► F5 informe final ─► entrega
F2 pilotos (ya) ───┘                         │                                   ▲
F1 saneamiento (ya) ─────────────────────────┴──► F5 capítulos 1-7 (ya) ──────────┘
F6 slides/video: preparación ya; grabación después del análisis
F7 administración: ya (Classroom es el insumo de fechas y plantilla)
```

Lo único que bloquea de verdad es **la cadena F2 → F4**. Los organismos externos **no** están en el camino crítico, siempre que la cátedra acepte los rangos (D2).

## 2. Qué se puede hacer ya y qué está bloqueado

| Se puede hacer ya, sin datos externos | Bloqueado hasta... |
|---|---|
| Piloto corto 07:00-07:30 con valores de prueba (T2.1) | Producción: hasta decidir D1 (E1) y D2 (rangos aprobados o asumidos) |
| Subir la memoria y medir tiempos; probar el límite de 50.000 agentes (T2.2-T2.4) | Validar la espera y el largo de cola reales: bloqueado sin medición (no se hará; se declara) |
| Protocolo del IDE y migración deliberada a 8.9.10 (T1.1-T1.2) | Plano oficial: bloqueado hasta que responda SBASE/Emova (se usa el plano hipotético) |
| Corregir las contradicciones entre documentos (T1.4) | Carga real por tren y proporción de transferencia: bloqueado (se reemplaza por rango) |
| Consulta a la cátedra: rangos, E1, E2/E3, plantilla (T0.1) | Plantilla LaTeX y pautas: hasta leer Classroom o consultar a la cátedra |
| Instalar el toolchain LaTeX y migrar los capítulos 1-7 (T5.1-T5.3) | Fechas del calendario: hasta leer Classroom |
| Pasar la presentación a Google Slides y preparar la grabación (T6.1-T6.3) | Grabación final: hasta tener los resultados de F4 |
| Reprocesar el perfil SBASE por período y medir la distancia del andén al vestíbulo (T3.1-T3.2) | |

## 3. Decisiones que tenés que tomar (o consultar con la cátedra)

**D1 — Qué es E1. Es la más urgente.**

- Datos [VERIF, reprocesado de `molinetes-2026.zip`]:
  - Principal = `LineaC_Constitucion_Turn07`, `Turn09`…`Turn29`, o sea 22 IDs.
  - `Turn07` tiene 3 pasajeros en seis meses.
  - Plaza = 8 IDs, incluido `TurnEMV+QR`, que tiene 0 pasajeros desde mayo, cuando aparece `Plaza_Turn`.
  - Los 28 de 01 y del formulario suman ambos vestíbulos.
- Opciones:
  - (a) **E1 = todos los molinetes del Principal operativos**: 21, o 22 si se repara `Turn07`. E0 = 20, o la disponibilidad observada por ventana (~19,5). Es realista y barato, pero la diferencia de capacidad es chica, así que es probable que no haya diferencia significativa. Ese resultado es válido.
  - (b) **E1 = ampliación hipotética**, por ejemplo 21 → 28 molinetes, en el mismo banco. Mantiene el modelo actual de 28 puestos, pero es una inversión y no una decisión operativa, y hay que declarar que el espacio no está verificado.
  - (c) **E1 = balanceo de carga.** El desbalance real es de factor ~11 entre `Turn14` y `Turn23`; se propone señalización o guiado que reparta la demanda. Es más original, pero exige modelar la preferencia de cola.
- **Recomendación:** (a) como comparación obligatoria, E0 = 20 contra E1 = 22, porque es lo único que el dato sostiene. (b) como segundo escenario alternativo sólo si el cómputo lo permite. Consultarlo con la cátedra junto con D2, porque el tema se aprobó con "abrir los 28".

**D2 — Parámetros sin dato: rangos con fuente contra esperar a los organismos.**

- Opciones:
  - (a) proponer rangos optimista/intermedio/pesimista a la cátedra y avanzar;
  - (b) esperar las respuestas.
- **Recomendación:** (a), con la tabla de la sección 5. Los pedidos del 23/09 siguen abiertos y, si llegan datos a tiempo, reemplazan al rango intermedio.

**D3 — Período representativo de la demanda.**

- 17.482 es la media ene-jun de 117 días hábiles e incluye enero y febrero, que son de vacaciones y menor carga. Para abril, la mediana es 19.245 [VERIF, subagente].
- Opciones:
  - (a) mantener ene-jun;
  - (b) usar mar-jun;
  - (c) usar mar-jun y además un factor de sensibilidad.
- **Recomendación:** (b). Reprocesar con `scripts/sbase-perfil.py` y citar el período exacto. `factorDemandaPed` queda para sensibilidad.

**D4 — Métricas primarias y alfa.**

- Hoy la planilla usa como primarias "procesados con drenaje", P90 y proporción > 30 s. Pero "procesados con drenaje" da D = 0 en cada par por conservación: gasta alfa sin informar nada.
- **Recomendación:** tres primarias:
  - P90 de espera (franja);
  - proporción con espera > 30 s;
  - P90 de la cohorte pico 08:15-08:45.

  α global = 0,05 con Bonferroni (α_s = 0,05/3). El throughput y la conservación pasan a ser **controles de verificación**. La espera media, Lq, la cola máxima, la disipación y la utilización son **secundarias**, con IC individual del 95 % descriptivo.

**D5 — E2 (Plaza) y E3 (EMV/QR).**

- **Recomendación:** no evaluarlos en el informe final. Se describen como extensiones implementadas en la capa lógica, sin resultados, y como trabajo futuro.
- Motivos:
  - E2 exige un segundo circuito sin datos de geometría;
  - E3 no tiene tiempo de validación EMV/QR citable, y el único molinete EMV/QR está en **Plaza** [VERIF], no en el Principal.
- La pregunta de "validación más rápida" queda cubierta de forma cualitativa por la sensibilidad del tiempo de servicio.

**D6 — Vía del informe LaTeX.**

- Opciones:
  - (a) MacTeX sin GUI instalado localmente (`brew install --cask mactex-no-gui`, ~5 GB; hay 212 GB libres) más pandoc;
  - (b) Overleaf;
  - (c) tectonic.
- **Recomendación:** (a). La fuente queda versionada en el repo, Claude puede compilarla y verificarla, y biber/biblatex-apa funcionan sin fricción. Overleaf sólo si Matías quiere editar online: se sube el zip y la fuente de verdad sigue siendo el repo. tectonic es liviano, pero su soporte de biber es frágil. La instalación la autorizás vos.

**D7 — Grabación del video.**

- **Recomendación:** OBS, con los dos en el mismo lugar (ambos viven en Rosario): una escena con Slides más webcam y otra con AnyLogic más webcam. Cambiar de escena en vivo no es edición. Zoom queda como alternativa si están separados, pero hay que verificar en un ensayo que la grabación local muestre a los dos y la pantalla a la vez.

**D8 — Qué hacer con el `.docx` del TP del hospital**, hoy sin seguimiento en `fuentes/`.

- Es trabajo de otro grupo y el repo es público.
- **Recomendación:** no commitearlo; agregarlo a `.gitignore` o moverlo fuera del repo. No lo commiteé en esta sesión.

**Preguntas para la cátedra**, en un solo mensaje para T0.1:

1. ¿Aceptan rangos con fuente para los parámetros no publicados (tabla de la sección 5)?
2. ¿E1 = todos los molinetes del Principal (22) en lugar de 28?
3. ¿E2 y E3 como trabajo futuro?
4. ¿Hay plantilla LaTeX o "pautas de entregas parciales" 2026? ¿Hay avances parciales obligatorios?
5. ¿La carátula lleva docentes? ¿Cómo se escribe la comisión (401 o 4K01)?

## 4. Fases y tareas

Formato de cada tarea: **Responsable · Depende de · Archivos · Aceptación observable · Esfuerzo**. Responsables posibles: Juan, Matías, Claude o externo. Toda edición del `.alp` la hace **un solo dueño a la vez** (ver T1.1).

### F0 — Decisiones y consulta (esta semana)

- **T0.1 Consulta a la cátedra (D1, D2, D5 y plantilla).**
  - Responsable: Juan (Claude redacta el borrador).
  - Depende de: sección 5 de este plan.
  - Archivos: nuevo `08-consulta-catedra.md` como borrador.
  - Aceptación: mensaje enviado por el canal de la cátedra y respuesta registrada en `SIM.md`.
  - Esfuerzo: 1 h. Claude no envía nada: lo mandás vos.
- **T0.2 Revisar Classroom:** fechas de entrega y presentación, avances parciales, plantilla o pautas LaTeX y docentes.
  - Responsable: Juan o Matías.
  - Depende de: —
  - Archivos: sección 7 de este plan y `06-checklist-cierre.md`.
  - Aceptación: fechas cargadas en el calendario y ruta de la plantilla (o "no existe").
  - Esfuerzo: 20 min.
- **T0.3 Tomar las decisiones D3, D4, D6, D7 y D8.**
  - Responsable: Juan (con Matías).
  - Depende de: —
  - Archivos: este plan (marcar la opción elegida).
  - Aceptación: cada D con su opción elegida y la fecha.
  - Esfuerzo: 15 min.

### F1 — Saneamiento (ya, sin datos)

- **T1.1 Protocolo de trabajo con el IDE.** Adoptarlo tal cual:
  1. Antes de abrir AnyLogic: `git status` limpio para el `.alp` y commit si hay cambios. Si hay un `SubteConstitucion.alp.autosave`, renombrarlo a `*.autosave.bak`. Hoy existe, pero es sólo normalización del IDE sin cambios de modelo [VERIF, subagente].
  2. **Un solo escritor.** Con el IDE abierto, nadie edita el `.alp` desde afuera (ni Claude ni scripts). Claude edita el XML sólo con el IDE cerrado.
  3. Si el IDE ofrece restaurar un autosave, responder **No**, salvo que el cambio perdido sea propio y reciente.
  4. Al cerrar: `git diff --stat` del `.alp`, `python3 …/verificar_modelo.py` y commit con mensaje. Si el diff es inesperado, `git restore` y avisar.
  5. Los CSV de corridas se renombran con fecha antes de relanzar, porque el experimento agrega al final (APPEND).

  - Responsable: Claude documenta; Juan aplica.
  - Archivos: `02-modelo-anylogic.md` §1 y `06-checklist-cierre.md`.
  - Aceptación: el protocolo está escrito en 02/06.
  - Esfuerzo: 30 min.
- **T1.2 Migración deliberada a 8.9.10.**
  - Pasos:
    1. Abrir el modelo, guardarlo desde el IDE una vez y commitear el formato nuevo.
    2. Adaptar `verificar_modelo.py` a la normalización de 8.9.10. Hoy falla con un autosave 8.9.10 por los `Id=0` repetidos de `DatasetExpression` y por `FinalTime == '900'` contra `900.0` [VERIF, subagente sobre una copia].
    3. Matías instala exactamente 8.9.10.
  - Responsable: Juan (IDE) y Claude (verificador).
  - Depende de: T1.1.
  - Archivos: `.alp` y `verificar_modelo.py`.
  - Aceptación: el verificador da 5 OK sobre el `.alp` en 8.9.10.
  - Esfuerzo: 1,5 h.
- **T1.3 Reproducibilidad entre máquinas.**
  - Qué hacer: correr el mismo par de prueba en la Mac de Juan y en la de Matías y comparar las filas CSV.
  - Responsable: Juan y Matías.
  - Depende de: T1.2 y T2.1.
  - Aceptación: filas idénticas campo a campo. Si no lo son, no se reparten corridas entre máquinas.
  - Esfuerzo: 30 min más el tiempo de cómputo.
- **T1.4 Corregir las contradicciones de la sección 11** (sólo documentos: 01, 02, 03, 05, 06, `SIM.md` y formulario).
  - Responsable: Claude.
  - Depende de: D1, D3, D4 y D5.
  - Aceptación: `grep` de "28 instalados", "modoDemo" en 03/05 y "8.9.9 el 24/09" sin resultados indebidos; el Log de `SIM.md` actualizado.
  - Esfuerzo: 2 h.
- **T1.5 Generalizar la planilla y el cargador a n pares variable** (≥ 10), con t crítico calculado según n y k.
  - Motivo: hoy 30 pares y 29 gl están fijos, y K = 2,5409 o 2,0452 está escrito a mano.
  - Responsable: Claude.
  - Depende de: D4.
  - Archivos: `04-resultados-corridas.xlsx` (vía script) y `cargar_corridas.py`.
  - Aceptación:
    - una prueba con datos sintéticos transitorios de n = 12 y n = 30 reproduce a mano un IC paired-t;
    - la planilla vuelve a quedar vacía;
    - las primarias son las de D4.
  - Esfuerzo: 2 h.

### F2 — Diagnóstico del modelo espacial (ya, con valores de prueba)

Estas tareas usan los valores de prueba de `PeatonalFranjaPrueba` (80 % / 60 / 120 / triangular 2-3-5). **Nada de esto es un resultado.**

- **T2.1 Piloto corto 07:00-07:30 (`PeatonalFranjaPrueba`, un par).**
  - Qué hacer: antes de lanzar, abrir la consola y dejarla visible, para capturar cualquier excepción; la E1 del primer piloto murió a los 787 s sin causa registrada.
  - Responsable: Juan (IDE).
  - Depende de: T1.1.
  - Archivos: `corridas_peatonales_demo.csv` (gitignorado) y una captura de consola.
  - Aceptación:
    - E0 y E1 terminan con fila `CSV_PEATONAL_DEMO`, sin `INCOMPLETO`;
    - generados = procesados con drenaje;
    - drenaje < 10 min simulados después del corte;
    - tiempo real por corrida anotado.
  - Esfuerzo: 30-60 min.
- **T2.2 Instrumentar "peatones fuera de cola".**
  - Motivo: en el piloto E0, a las 5 h quedaban 3.198 peatones en el sistema, pero sólo 497 en cola. Unos 2.700 estaban trabados en el hall, y las métricas no los ven porque todo se mide desde `onEnterQueue` [VERIF, subagente].
  - Qué hacer:
    - agregar un contador de peatones en tránsito (ingresados que no entraron a cola ni salieron), con su máximo;
    - imprimir el tiempo real de pared al terminar (`System.currentTimeMillis()`).
  - Responsable: Claude (XML, con el IDE cerrado).
  - Depende de: T1.2.
  - Archivos: `.alp`, `verificar_modelo.py` y 02 §7.
  - Aceptación: el verificador da OK; la fila de consola incluye `enTransitoMax` y `segundosReales`. No se agregan columnas al CSV oficial sin actualizar el cargador.
  - Esfuerzo: 2 h.
- **T2.3 Memoria y paralelismo.**
  - Hechos [VERIF, ayuda de AnyLogic `editions.html` y `parameter-variation.html`]:
    - los experimentos de simulación tienen `MaximumMemory` 512 MB y los de variación de parámetros, 1024 MB;
    - `AllowParallelEvaluations = false`;
    - la ayuda de AnyLogic no lista las evaluaciones en paralelo entre las limitaciones de PLE;
    - la máquina tiene 10 núcleos y 16 GB.
  - Qué hacer:
    1. Subir la memoria a 4096 MB.
    2. Activar el paralelismo en `PeatonalCorridasApareadas` recién después de comprobar tres condiciones: que no haya estado `static` (generadores y colecciones), que la escritura del CSV sea por archivo por corrida o esté sincronizada, y que las filas en paralelo sean idénticas a las secuenciales para el par 1.
  - Responsable: Claude (XML) y Juan (prueba).
  - Depende de: T2.1.
  - Aceptación: un par en paralelo produce las mismas filas que en secuencia; el tiempo por par baja.
  - Esfuerzo: 2-3 h.
- **T2.4 Prueba del límite de 50.000 agentes.**
  - Hecho: la ayuda dice "50 000 dynamically created agents … in a model" y no aclara si el conteo se acumula entre las corridas de un experimento.
  - Qué hacer: con el horizonte de prueba de 1800 s (~3.000 peatones por corrida), lanzar 20 corridas seguidas en un solo experimento (~60.000 acumulados).
  - Responsable: Juan.
  - Depende de: T2.1.
  - Aceptación: las 20 corridas emiten fila. Si se corta cerca de la corrida 17, el límite es acumulado y la producción se parte en tandas de ≤ 2 corridas de franja por lanzamiento (ver sección 6).
  - Esfuerzo: tiempo de cómputo más 15 min.
- **T2.5 Piloto de franja completa, un par, con los valores de prueba.**
  - Responsable: Juan.
  - Depende de: T2.1-T2.3.
  - Aceptación:
    - ambas corridas drenan;
    - `enTransitoMax` es acotado;
    - se registra el tiempo real por corrida (T_run).
  - T_run alimenta la regla de decisión de la sección 6.
  - Esfuerzo: 1-2 h de cómputo.
- **T2.6 Plan B si el atasco persiste en T2.1 o T2.5.**
  - Diagnóstico visual en un experimento de simulación con franja y animación. Crear `PeatonalFranjaVisual`, porque `PeatonalE0/E1` terminan a los 900 s y no activan `modoFranjaPed`. Revisar:
    - densidad en el acceso oeste;
    - colas que invaden el pasillo de circulación;
    - `PedGoTo` hacia la salida con un destino alcanzable;
    - columnas y paredes que estrangulan el paso.
  - Remedios, en orden:
    1. ensanchar pasillos y el acceso del plano hipotético (es hipotético: se puede y se declara);
    2. reevaluar la elección de cola dinámicamente, y no una sola vez;
    3. como último recurso, la capa lógica para la estadística (sección 6, opción D).
  - Responsable: Claude (análisis y XML) y Juan (IDE).
  - Aceptación: T2.1 pasa.
  - Esfuerzo: 3-6 h.
- **T2.7 Piloto demo de la cadena** (`PeatonalCorridasDemo` → `cargar_corridas.py --demo`).
  - Responsable: Juan y Claude.
  - Depende de: T2.1.
  - Aceptación: el cargador valida 3 pares demo y la planilla oficial queda vacía.
  - Esfuerzo: 30 min.

### F3 — Calibración con rangos (depende de D1 y D2; no de los organismos)

- **T3.1 Reprocesar el perfil SBASE** según D3 (mar-jun) y fijar `perfilPed15min`/`perfil15min`.
  - Responsable: Claude.
  - Archivos: `scripts/sbase-perfil.py` (sólo un parámetro de período), 01, 02 y el `.alp`.
  - Aceptación:
    - tabla por ventana con n días, media y CV;
    - total de la franja citado con su período;
    - el verificador actualizado.
  - Esfuerzo: 1,5 h.
- **T3.2 Distancia del andén del Roca al vestíbulo Principal y desnivel.**
  - Qué hacer: medir en imagen satelital o planimetría pública y documentar el método, la fecha y la herramienta.
  - Con eso se calcula `demoraAccesoRocaSeg` con la fórmula de la sección 5.
  - Responsable: Matías.
  - Aceptación: D (m) y h (m) con captura y método reproducible.
  - Esfuerzo: 1 h.
- **T3.3 Puertas por lado de los coches del Roca** (hoy son formaciones de 7 coches [DATO, argentina.gob.ar]).
  - Qué hacer: buscar una ficha técnica oficial o del fabricante. Si no aparece, [SUP] 3 puertas por lado, declarado.
  - Responsable: Matías.
  - Aceptación: un número con fuente o un supuesto marcado.
  - Esfuerzo: 1 h.
- **T3.4 Cargar el escenario intermedio y los extremos.**
  - Qué hacer: reemplazar los `-1` por los valores intermedios aprobados. Crear experimentos parametrizados para el contexto (optimista/intermedio/pesimista) y para E0/E1 según D1. Ajustar la geometría a 22 puestos si D1 = (a).
  - Responsable: Claude (XML) y Juan (Build).
  - Depende de: D1, D2, T2.x y T3.1-T3.3.
  - Aceptación: verificador 5 OK, Build correcto y un piloto de franja intermedio de un par con fila `CSV_PEATONAL`.
  - Esfuerzo: 3-4 h.
- **T3.5 Validación operacional** (ver sección 6.2).
  - Responsable: Claude (análisis) y Juan (corrida).
  - Depende de: T3.4.
  - Archivos: nueva hoja o CSV de validación y 03 §Paso 6.
  - Aceptación: tabla de caudal simulado contra observado por ventana, y chequeo de la cota por molinete.
  - Esfuerzo: 2 h.

### F4 — Producción y análisis

- **T4.1 Pares iniciales, n0 = 10** (contexto intermedio, E0 contra E1).
  - Responsable: Juan (y Matías si T1.3 pasa).
  - Depende de: T3.4, T3.5 y T2.4.
  - Archivos: `corridas_peatonales.csv` y la planilla vía cargador.
  - Aceptación: 10 pares validados por `cargar_corridas.py`.
  - Esfuerzo: 10 × 2 × T_run / paralelismo.
- **T4.2 Tamaño de muestra.**
  - Qué hacer: con los 10 pares, calcular n_a*(β) para cada primaria (fórmula de §7.3).
  - Resultado: n final = max(30, n*) si el cómputo lo permite, o n* con justificación si n* < 30.
  - Responsable: Claude.
  - Aceptación: n justificado por escrito en 03 §Paso 7.
  - Esfuerzo: 1 h.
- **T4.3 Completar los pares hasta n.**
  - Responsable: Juan y Matías.
  - Aceptación: planilla con n pares, sin filas `INCOMPLETO` ni demo.
  - Esfuerzo: cómputo.
- **T4.4 Sensibilidad** (sólo si el presupuesto de la sección 6 alcanza).
  - Qué hacer: contextos optimista y pesimista, con 10 pares cada uno, E0 contra E1.
  - Responsable: Juan.
  - Aceptación: IC paired-t por contexto.
  - Esfuerzo: 40 corridas × T_run / paralelismo.
- **T4.5 Análisis y gráficos** (§7).
  - Responsable: Claude.
  - Archivos: script `analisis_corridas.py` (nuevo) y `materias/SIM/figs/tpi-subte-*.png`.
  - Aceptación: tabla de resultados, IC con Bonferroni, gráfico de intervalos y conclusión según la regla de §7.4.
  - Esfuerzo: 3 h.

### F5 — Informe LaTeX

- **T5.1 Toolchain** según D6: `brew install --cask mactex-no-gui` y `brew install pandoc`.
  - Responsable: Juan autoriza; Claude ejecuta.
  - Aceptación: `latexmk -v`, `biber -v` y `pandoc -v` responden.
  - Esfuerzo: 30 min (descarga incluida).
- **T5.2 Esqueleto.**
  - Contenido:
    - `informe/tpi-subte.tex`;
    - `informe/referencias.bib`;
    - `informe/Makefile` o `latexmk`;
    - carátula UTN FRRO según la plantilla, o, si no hay, la carátula propia de §8.2.
  - Responsable: Claude.
  - Depende de: T0.2.
  - Archivos: `materias/SIM/entregables/TPI/subte/informe/`.
  - Aceptación: el PDF compila sin warnings de referencias.
  - Esfuerzo: 2 h.
- **T5.3 Migración de los capítulos 1-7** (pasos 1-7) desde `03-informe-tpi.md` con pandoc y revisión manual. Ver §8.
  - Responsable: Claude, con revisión de Juan.
  - Depende de: T1.4 y T5.2.
  - Aceptación: capítulos con figuras y tablas numeradas, citas `\parencite` resueltas y ninguna fuente sin cita.
  - Esfuerzo: 4 h.
- **T5.4 Capítulos 8-10** (producción, análisis, conclusiones) y anexos.
  - Responsable: Claude, con revisión de Juan y Matías.
  - Depende de: T4.5.
  - Aceptación: fórmulas de §7 presentes y los tres resultados comentados.
  - Esfuerzo: 3 h.
- **T5.5 Revisión final.**
  - Qué controlar:
    - checklist de la sección 9;
    - `grep -i wikipedia` en el `.bib` y el `.tex` = 0;
    - el PDF se abre en otra máquina.
  - Responsable: Matías.
  - Esfuerzo: 1,5 h.

### F6 — Presentación y video

- **T6.1 Pasar la presentación a Google Slides.** Subir el `.pptx` a Drive y abrirlo con Slides. Revisar fuentes y gráficos, y agregar una diapositiva de limitaciones.
  - Responsable: Matías.
  - Aceptación: el enlace de Slides se registra en 05 y las 6-7 diapositivas se ven sin deformarse.
  - Esfuerzo: 1 h.
- **T6.2 Experimento de exhibición** `PeatonalFranjaVisualE0/E1`: simulación con animación, franja intermedia y arranque que se pueda pausar cerca de las 08:20 simuladas.
  - Responsable: Claude (XML) y Juan.
  - Depende de: T3.4.
  - Aceptación: a los 5 s de reanudar se ve movimiento y colas, y el rótulo del escenario queda visible.
  - Esfuerzo: 1,5 h.
- **T6.3 Montaje de la grabación** (D7). Instalar OBS con dos escenas: "Slides + cámara" y "AnyLogic + cámara", con los dos en cuadro. Hacer una prueba de audio.
  - Responsable: Juan y Matías.
  - Aceptación: una prueba de 20 s muestra a ambos, las diapositivas y AnyLogic.
  - Esfuerzo: 1 h.
- **T6.4 Actualizar el guion 05** con resultados, el nuevo E1 y el período SBASE. Sacar la mención a `modoDemo` y dejar E2/E3 en una frase.
  - Responsable: Claude.
  - Depende de: T4.5.
  - Aceptación: lectura en voz alta ≤ 2:40.
  - Esfuerzo: 1 h.
- **T6.5 Ensayos y toma.**
  - Qué hacer: al menos 2 ensayos completos cronometrados y después la toma única.
  - Si una toma pasa de 2:55 o sale mal, se descarta y se graba otra completa. **No se recorta, ni siquiera en YouTube Studio.**
  - Responsable: Juan y Matías.
  - Aceptación: archivo ≤ 3:00 según el reproductor.
  - Esfuerzo: 2 h.
- **T6.6 Publicación.**
  - Pasos:
    1. YouTube con visibilidad "Oculto" y la opción "No, no es contenido creado para niños".
    2. Probar el enlace en una ventana privada sin sesión.
    3. Subir el enlace al Classroom.
  - Responsable: Juan.
  - Aceptación: el enlace abre sin iniciar sesión y la duración es ≤ 3:00.
  - Esfuerzo: 20 min.

### F7 — Administración (ya)

- **T7.1 Formularios web** de SBASE/GCBA (Ley 104), Emova y Trenes Argentinos, con número de trámite y captura.
  - Responsable: Juan o Matías (humano; Claude no completa formularios).
  - Aceptación: comprobantes en `datos/solicitudes/` (sin datos sensibles) y fecha de seguimiento.
  - Esfuerzo: 1 h.
- **T7.2 Correo de Matías:** sumarlo a la carátula y al frontmatter sólo con su confirmación.
  - Responsable: Matías.
  - Esfuerzo: 5 min.
- **T7.3 Carátula:** UTN FRRO · Cátedra Simulación · comisión 401 · integrantes y legajos (53533 y 53528) · docentes.
  - Según el TP 2025 los docentes son Guillermo Leale y Juan Ignacio Torres; confirmar para 2026 (T0.1/T0.2).
  - Responsable: Juan.
  - Esfuerzo: 10 min.
- **T7.4 Formulario del tema.**
  - Hecho: `SIM.md` dice "Aprobado por Leale el 2026-09-20", pero también "falta reenviarlo en el envío real".
  - Qué hacer: confirmar si hay que reenviarlo.
  - Responsable: Juan.
  - Esfuerzo: 5 min.
- **T7.5 Avances parciales.**
  - Hecho: el grupo 2025 tenía "Avance TPI 1/8".
  - Qué hacer: si en 2026 hay avances en Classroom, cada uno se arma con este esquema: estado, trabajo hecho con capturas, próximos pasos.
  - Responsable: Juan.
  - Depende de: T0.2.
- **T7.6 Entrega.**
  - Qué entregar: el PDF subido **como archivo** y el enlace del video en el Classroom. Guardar una captura de "Entregado".
  - Responsable: Juan.
  - Aceptación: los dos entregables figuran en el Classroom.

## 5. Parámetros sin dato: rangos propuestos con fuente

Todos los valores son de **propuesta** a la cátedra (D2). La columna "Estado" marca qué es dato y qué es supuesto.

| Parámetro | Optimista | Intermedio | Pesimista | Fuente / justificación | Estado |
|---|---:|---:|---:|---|---|
| `servicioPedSeg` (s/pax) | 2,0 | 2,4 | 3,0 | TCQSM 3.ª ed., Exh. 10-27, p. 10-42: smart card en London, 2,4 s; torniquete de NY, 2,6-2,9 s. SPSG 2012 §3.3: 25 pax/min por molinete. Cota SBASE: en 15 min se observaron hasta 246 pax en un molinete, así que la media sostenida es ≤ 900/246 = **3,66 s** | Rango [DATO externo]; que aplique al molinete de trípode SUBE es [SUP] |
| Forma del servicio | triangular (1,5; 2,0; 3,0) | triangular (1,8; 2,4; 3,5) | triangular (2,2; 3,0; 4,5) | El modelo admite triangular (`servicioMin/MaxPedSeg`). La asimetría a derecha refleja fallas de lectura. Los extremos son [SUP]; la media de cada triangular queda ≤ 3,66 s | [SUP] |
| `duracionDescargaSeg` | ≈ 45 | ≈ 75 | 120 | N_bajan × t_flujo / (n_puertas × 2). t_flujo = 1,38 / 1,7 / 2,03 s por pasajero (TCQSM Exh. 8-12, p. 8-25). 120 s = criterio de diseño del SPSG (el tren se vacía por los molinetes en 2 min). 45 y 75 suponen 7 coches × 3 puertas por lado (T3.3) | Fórmula [DATO]; puertas y carga [SUP] |
| `demoraAccesoRocaSeg` | D/1,25 + h/0,30 | D/0,95 + h/0,30 | D/0,63 + h/0,20 | 1,25 m/s = velocidad de diseño (TCQSM p. 10-20). 0,63 m/s = SPSG §5.1, flujo congestionado. Escaleras: 18 m/min bajando (TCQSM p. 10-24/25) y 12 m/min (SPSG). El 0,95 intermedio es interpolación [SUP]. D y h salen de T3.2 | [DATO] + [PEND T3.2] |
| `proporcionRocaPed` | 0,70 | 0,80 | 0,90 | **Sin fuente citable** de transferencia Roca → Línea C (el subagente buscó en CNRT, GCBA y prensa). Contexto: Plaza Constitución vende el 29,3 % de los pasajes del Roca, 35,3 M en 2024 (CNRT, pp. 15 y 31), y el vestíbulo Principal da al hall ferroviario [SUP] | [SUP] explícito; pedir aval |

**Qué parámetros entran en la sensibilidad:**

- `demoraAccesoRocaSeg` es un retardo: desplaza las oleadas en el tiempo y casi no cambia su forma. Se fija en el valor intermedio y queda **fuera** de la sensibilidad.
- Los que moldean la congestión son `servicioPedSeg`, `duracionDescargaSeg` (qué tan "puntiaguda" es la oleada) y `proporcionRocaPed` (cuánto de la demanda viene en oleadas).
- Los contextos combinados (todo optimista contra todo pesimista) cubren el esquema de Weitz con 2 × 10 pares, en lugar de un factorial 3³ que es inviable.

## 6. Factibilidad computacional y validación

### 6.1 Regla de decisión según el tiempo real medido (T2.5)

**Qué se sabe:**

- 43 min por corrida es una cota pesimista, porque se midió con un modelo atascado: unos 3.000 peatones activos durante 5 h de modelo y 1 GB de memoria.
- Límites de PLE:
  - 5 h de modelo por corrida en la Pedestrian Library;
  - 50.000 agentes "in a model" (T2.4);
  - sin exportación standalone ni ejecución por línea de comandos;
  - con evaluaciones en paralelo en Parameter Variation.

**Alternativas evaluadas:**

| Opción | Qué cambia | Consecuencia metodológica | Cuándo |
|---|---|---|---|
| **A. Corregir y medir, más memoria y paralelismo** | Nada del diseño | Ninguna. Es el diseño previsto: sistema terminal 07:00-09:30 con drenaje | Siempre primero |
| **B. Tandas y dos máquinas** | Rango de pares por lanzamiento: parámetro `parInicial` en la expresión *freeform*. Pares repartidos entre la Mac de Juan y la de Matías | Ninguna, si T1.3 prueba determinismo. Las semillas por par no cambian | Si 10 < T_run ≤ 30 min, o si el límite de 50.000 resulta acumulado |
| **C. Procedimiento secuencial (Unidad 9)** | n0 = 10 pares y n final según n_a*(β) | Válido y citable (Law §9.5-9.6). Conviene precisión **absoluta** β, porque la relativa se indefine si la diferencia real es ≈ 0 | Siempre, para justificar n. Evita correr de más |
| **D. Horizonte acotado a la hora pico** | Arribos 07:45-09:00. Métricas sólo para la cohorte 08:00-09:00. Calentamiento de 15 min | La pregunta pasa a ser "hora pico", no la franja. Es defendible si el piloto muestra que la cola se vacía entre trenes, porque con ρ ≈ 0,3 el sistema "olvida" en pocos minutos. Hay que mostrar esa evidencia (Law §9.7). Baja el cómputo ~50 % | Si T_run > 30 min con A+B |
| **E. Capa lógica para la estadística** | `Main` (Process Modeling, sin límite de 5 h, rápida) | Requiere portar a `Main` la demanda por horario del Roca, porque hoy usa tandas constantes. `Main` tiene **una cola común y servidores intercambiables**; el espacial, una cola por molinete con elección. Son sistemas distintos, así que habría que mostrar consistencia en un subconjunto de pares (IC de E0 y E1 superpuestos en ambas capas) o declarar que el espacial es sólo visualización. Debilita el aporte del modelo espacial | Plan B si el espacial no drena tras T2.6 |

**Recomendación:** A, más C para fijar n, más B si hace falta. D es el primer recorte y E, el último.

Estimación con 4 corridas en paralelo:

| T_run | 60 corridas (30 pares) | Más sensibilidad (40 corridas) |
|---|---|---|
| 10 min | ~2,5 h | +1,7 h |
| 20 min | ~5 h | +3,3 h |
| 43 min | ~11 h | +7 h |

Aun en el peor caso, 11 h en dos noches o dos máquinas es viable. Por eso **no se recomienda bajar de entrada a menos de 30 pares**. Si T2.4 muestra que el límite de agentes se acumula, las corridas se lanzan de a una por experimento, a mano o por tandas, y el costo es de operación, no de cómputo.

### 6.2 Validación del modelo espacial

**Verificación:** el programa hace lo que se diseñó. Estos controles corren en cada corrida o con el verificador:

- conservación: generados = procesados con drenaje;
- desviados = 0 en E0-E1;
- drenaje completo antes de 18.000 s y `enTransitoMax` acotado (T2.2);
- filas sin `INCOMPLETO`;
- mismos ingresos y servicios en E0 y E1 con la misma semilla (ya lo verifica el verificador);
- orientación de las colas (ya lo verifica el verificador);
- una traza de 5 pasajeros en la capa lógica (ya existe).

**Validación:** qué se puede validar contra la realidad y qué no.

| Control | Cómo | Tipo | Limitación |
|---|---|---|---|
| Caudal por ventana de 15 min contra SBASE | `caudalPorVentana` contra el perfil del período D3; tolerancia propuesta ±5 % con E0 | Parcialmente circular, porque la demanda se construye con ese perfil. Se declara como **calibración**, no como validación | — |
| Caudal con datos no usados | Correr con el perfil de **mayo-junio** si la calibración usa **marzo-abril**, o un día-tipo miércoles contra lunes (2.510 contra 1.976 en la ventana 08:30), y comparar | Validación de réplica, *holdout* | Depende de que el modelo sea sensible a la demanda |
| Cota por molinete | Máximo simulado de pax/15 min por molinete ≤ 246 observado; nunca se supera la capacidad física | Validación de un extremo | — |
| Reparto entre molinetes | Utilización simulada por puesto contra la participación observada (`Turn14` a `Turn23`, factor ~11) | Validación de la regla de elección de cola | Con elección "más corta" el modelo va a repartir más parejo que la realidad. Hay que declararlo: E1 podría **sobreestimar** la mejora |
| Molinetes activos | Molinetes con uso en E0 contra 19,5 activos por ventana | Consistencia | — |
| Espera y largo de cola reales | **No validable** sin medición: no hay dato público | Se declara como limitación principal y como condición de las conclusiones | — |
| Juicio experto | Mostrar la animación a la cátedra y, si SBASE responde, al operador (validación "cara a cara", Law) | Validación conceptual | — |

## 7. Análisis estadístico (va textual al capítulo del Paso 9)

La notación sigue a la wiki (Unidades 9 y 10 = Law) y se unifica con el borrador 03, que usaba `D_i`.

### 7.1 Diferencias apareadas y paired-t (Unidad 10 §10.2)

Para cada par j = 1..n con la misma semilla (números aleatorios comunes, §10.5), y para la medida X:

$$Z_j = X_{E1,j} - X_{E0,j}, \qquad \bar Z(n) = \frac{1}{n}\sum_{j=1}^{n} Z_j, \qquad
\widehat{\mathrm{Var}}[\bar Z(n)] = \frac{\sum_{j=1}^{n}\left[Z_j - \bar Z(n)\right]^2}{n(n-1)}$$

$$\bar Z(n) \pm t_{n-1,\,1-\alpha_s/2}\sqrt{\widehat{\mathrm{Var}}[\bar Z(n)]}$$

- **Signo:** en las métricas de espera, Z < 0 significa que E1 mejora.
- **Unidad de observación:** cada X_{i,j} es **una salida por réplica** (P90 y proporción calculados dentro de la réplica, §9.5-bis), nunca esperas individuales agrupadas.
- **Varianza reducida por los números aleatorios comunes:** Var(m₁ − m₂) = Var(m₁) + Var(m₂) − 2 Cov(m₁, m₂). El informe muestra la covarianza estimada como evidencia de que el apareamiento funcionó.

### 7.2 Bonferroni (Unidad 9 §9.8)

$$P(\mu_s \in I_s\ \forall s = 1..k) \ge 1 - \sum_{s=1}^{k}\alpha_s$$

- Con k = 3 primarias (D4) y α = 0,05: α_s = 0,05/3, cada IC al 98,33 %.
- Valor crítico para n = 30: t_{29; 0,99167} = **2,5409** [VERIF, subagente; coincide con la planilla].
- Las secundarias usan IC individuales al 95 % (t_{29; 0,975} = 2,0452) y se presentan como descriptivas, fuera de la familia.

### 7.3 Tamaño de muestra (Unidad 9 §9.5-9.6)

Con n0 = 10 pares, para cada primaria:

$$n_a^*(\beta) = \min\left\{ i \ge n_0 : t_{i-1,\,1-\alpha_s/2}\sqrt{S^2(n_0)/i} \le \beta \right\}$$

- β es la mitad del ancho aceptable del IC de la diferencia, en unidades de la métrica. Por ejemplo, β = 2 s para el P90 y β = 0,02 para la proporción. **Hay que fijarlo antes de ver los datos** y dejarlo escrito en el Paso 7.
- n final = max(n0, máx_s n_a*). Si el cómputo lo permite, se usa ≥ 30 (tamaño fijo, más simple de explicar); si n* es menor, se usa n* con la justificación.
- Se usa precisión **absoluta** y no relativa (γ), porque γ se indefine cuando la diferencia real es ≈ 0, que es un resultado posible.

### 7.4 Interpretación (regla escrita antes de correr)

| Resultado del IC de Z (primaria) | Lectura | Qué se escribe |
|---|---|---|
| Todo < 0 | E1 reduce la espera con evidencia estadística | Se recomienda E1 **si** el throughput a las 09:30 no empeora y las otras primarias no contradicen. Se cuantifica la mejora con el IC, no con la media sola |
| Todo > 0 | E1 empeora | Se recomienda mantener E0 y se explica el mecanismo (por ejemplo, la elección de cola) |
| Contiene 0 | Sin diferencia significativa con n pares | **Resultado válido** (consigna §1). Si el ancho del IC es ≤ β, además se puede afirmar que cualquier diferencia es menor a β en la práctica. Si es > β, se informa que la precisión fue insuficiente |
| Mixto entre primarias | Compromiso | Se describe el trade-off y no se declara una mejora global |

Supuestos que se declaran: normalidad aproximada de los Z_j, que con n ≥ 30 se apoya en el TCL (se muestra un histograma o QQ de los Z_j del P90), e independencia entre pares (semillas distintas por par).

### 7.5 Tablas y gráficos del análisis

- **Tablas:**
  - T-a: parámetros, con la columna dato/supuesto/fuente;
  - T-b: validación del caudal por ventana;
  - T-c: medias de E0 y E1, Z̄, error estándar, IC Bonferroni y decisión, por métrica;
  - T-d: sensibilidad por contexto;
  - T-e: controles de verificación (conservación y drenaje) de las n corridas.
- **Gráficos** (en `materias/SIM/figs/tpi-subte-*.png`):
  - perfil SBASE por ventana;
  - arribos del Roca en el tiempo;
  - diagrama conceptual;
  - plano hipotético (ya existe: `tpi-subte-plano-hipotetico.png`);
  - captura de AnyLogic en ejecución;
  - caudal simulado contra observado;
  - IC de las diferencias (*forest plot*) de las primarias;
  - boxplot de Z_j;
  - utilización por molinete.

## 8. Informe LaTeX

### 8.1 Vía y migración

- **Vía:** D6, recomendado MacTeX sin GUI más pandoc. La fuente queda en `subte/informe/` y el PDF final como artefacto del repo. La consigna exige "generado en LaTeX", así que el `.tex` es la evidencia.
- **Migración:**
  - `pandoc 03-informe-tpi.md -f markdown -t latex --top-level-division=section -o informe/cuerpo-borrador.tex`;
  - después, revisión manual: tablas a `booktabs`, figuras con `\label`, citas a `\parencite{}` y fórmulas a `align`.
  - No se usa `scripts/monografia-pdf.js`: es HTML → PDF con Chrome, no es LaTeX y no soporta fórmulas.
- **Plantilla:** no se encontró ninguna en el repo ni en `archivo/` [VERIF, subagente]. Es **pregunta para vos o para la cátedra** (T0.1/T0.2). Si no hay, la propuesta es:
  - clase `article`, A4, 11 pt;
  - `babel[spanish]`, `geometry`, `booktabs`, `graphicx`, `amsmath`, `siunitx` (coma decimal) e `hyperref`;
  - `biblatex[style=apa]` + biber.
- **Bibliografía:** `referencias.bib` con las entradas de la sección 13 y cero Wikipedia.

### 8.2 Estructura capítulo por capítulo

| Sección | Contenido | Paso(s) |
|---|---|---|
| Portada | UTN FRRO, Cátedra Simulación, título, comisión 401, integrantes y legajos, docentes, fecha | — |
| Resumen | 150 palabras: problema, método, resultado del IC y recomendación | — |
| Índice | `\tableofcontents`, más índice de figuras y tablas | — |
| 1. Introducción | Constitución, oleadas del Roca y por qué M/M/c falla (ρ ≈ 0,3 con colas) | — |
| 2. Formulación del problema y planificación | Pregunta de decisión, alcance (Principal, días hábiles, 07:00-09:30), métricas, escenarios, plan de trabajo | 1 |
| 3. Datos y modelo conceptual | SBASE (período D3), horario del Roca, tabla de parámetros con dato/supuesto/fuente, diagrama | 2 |
| 4. Validación conceptual | Supuestos revisados, límites (sin medición presencial) y consulta a la cátedra | 3 |
| 5. Construcción y verificación | Capa lógica y espacial, verificador (traza de 5 pasajeros), números aleatorios comunes, conservación, protocolo del IDE | 4 |
| 6. Ejecuciones piloto | Atasco, diagnóstico, corrección y tiempos de cómputo, contados con honestidad | 5 |
| 7. Validación del modelo programado | Tabla de §6.2 y lo que no se puede validar | 6 |
| 8. Diseño de experimentos | E0 contra E1 (D1), contextos, sistema terminal y drenaje, semillas, n0 y β, α y Bonferroni | 7 |
| 9. Corridas de producción | n pares, tiempo de cómputo, controles de las corridas | 8 |
| 10. Análisis de los datos de salida | Fórmulas de §7, tablas T-c/T-d, *forest plot*, comentario | 9 |
| 11. Conclusiones y recomendaciones | Regla de §7.4, alcance, limitaciones, trabajo futuro (E2, E3, plano real, medición) | 10 |
| 12. Documentación y uso | Repo, verificador, cargador, video | 10 |
| Bibliografía | biblatex APA | — |
| Anexos | Esquema `CSV_PEATONAL`, parámetros del `.alp` y extracto del horario del Roca | — |

## 9. Cumplimiento de la consigna

| Requisito o causal de recuperatorio | Cómo se cubre | Tarea |
|---|---|---|
| ≥ 2 escenarios (causal) | E0 y E1 (D1); contextos de sensibilidad aparte | T3.4, T4.1 |
| Más de una corrida por escenario (causal) | n ≥ 10 pares, objetivo 30 | T4.1-T4.3 |
| Test de medias con fórmulas y comentario (causal) | paired-t + Bonferroni (§7), comentario con la regla de §7.4 | T4.5, T5.4 |
| Video ≤ 3 min (causal) | Guion ≤ 2:40, 2 ensayos, toma descartable si pasa de 2:55 | T6.4-T6.5 |
| Informe en LaTeX (causal) | MacTeX + fuente `.tex` en el repo | T5.1-T5.5 |
| Sin Wikipedia (causal) | `grep` en `.bib`/`.tex`; fuentes de la sección 13 | T5.5 |
| Faltan entregables (causal) | PDF como archivo más el enlace de YouTube en Classroom | T7.6 |
| Portada, índice, introducción, desarrollo, conclusiones y recomendaciones, bibliografía | Estructura de §8.2 | T5.2-T5.4 |
| Los 10 pasos referenciados (lista de la **consigna**, Law, no la de Weitz) | Una sección por paso | T5.3-T5.4 |
| Escenarios explicados | Cap. 8 | T5.4 |
| Citas de toda fuente externa | `referencias.bib` | T5.2 |
| El PDF se sube directo, sin enlace | — | T7.6 |
| "Conforme a las pautas de las entregas parciales" | **Pendiente**: no se encontraron | T0.2 |
| Video: caso → escenarios y variables → análisis → conclusión | Guion 05 | T6.4 |
| Extracto de AnyLogic en ejecución | Experimento de exhibición | T6.2 |
| Todos en cámara | OBS con los dos en cuadro | T6.3 |
| Apoyo en Google Slides | Migración del `.pptx` | T6.1 |
| Sin edición | Toma única; ni siquiera recorte en YouTube | T6.5 |
| YouTube "Oculto", no "para niños" | — | T6.6 |
| Recomendación fundada en evidencia; "sin diferencia" es válido | Regla de §7.4 escrita antes de correr | T4.5 |

## 10. Calendario por semanas

Las fechas de Classroom están como marcadores: completarlas en T0.2. **Riesgo de carga:** en 2025 el parcial fue el 04/10 (`fuentes/txt/examenes__parciales__2025__2025-10-04.md`). Si en 2026 cae en la misma época, choca con la F2-F3.

| Semana | Fechas | Objetivo | Tareas |
|---|---|---|---|
| S1 | 24/09-30/09 | Decidir y diagnosticar | T0.1-T0.3, T1.1-T1.2, T2.1-T2.3, T2.7, T7.1-T7.4, T5.1 |
| S2 | 01/10-07/10 | Modelo sano y tiempo medido; toolchain | T2.4-T2.6, T1.3-T1.5, T3.1-T3.3, T5.2-T5.3 (caps. 1-5) · **[PARCIAL SIM: ___/10]** |
| S3 | 08/10-14/10 | Calibrado y validado; producción inicial | T3.4-T3.5, T4.1-T4.2, T6.1, T6.3 · **[AVANCE PARCIAL: ___]** |
| S4 | 15/10-21/10 | Producción completa y análisis | T4.3-T4.5, T5.3 (caps. 6-7) |
| S5 | 22/10-28/10 | Informe completo y video | T5.4-T5.5, T6.2, T6.4-T6.6 |
| S6 | 29/10-04/11 | Colchón y entrega | T7.6 · **[ENTREGA: ___]** · **[PRESENTACIÓN: ___]** |

Si la entrega real es antes de S6, se comprime S4-S5. Lo primero que se sacrifica es T4.4 (sensibilidad) y el escenario E1-(b).

## 11. Auditoría de consistencia (corregir en T1.4 antes de redactar la versión final)

| # | Contradicción | Dónde | Correcto / acción |
|---|---|---|---|
| 1 | "28 molinetes instalados" en el Principal | 01:113-121, formulario:76-77, `SIM.md` §TPI, 02 §4, 05, pptx | SBASE 2026: el Principal tiene 22 IDs (21 con tráfico) y la estación ~29-30. Redefinir con D1 |
| 2 | 17.482 validaciones como "día hábil" sin período | 01, 02, `SIM.md`, pptx | Es la media ene-jun; abril da 19.245 (mediana). Citar el período (D3) |
| 3 | Métricas primarias distintas | 01:128-136 y `SIM.md` (espera media, P90, > 30 s, disipación) contra la planilla y 03:269 (drenaje, P90, > 30 s) | D4; sacar "procesados con drenaje" de las primarias (D = 0 trivial) |
| 4 | IC del 95 % contra Bonferroni al 98,3 % | 01:144 contra 03:262 y la planilla | Unificar según §7.2 |
| 5 | "Disipación" con dos definiciones | 01:135 y `Main` (por tanda) contra CSV campo 12 (desde el último ingreso, 02:403) | Renombrar el campo espacial ("tiempo de vaciado final") o alinearlo |
| 6 | 03 promete exportar la utilización por molinete y todas las métricas de la cohorte pico | 03:233-234 contra el CSV (sólo media, dispersión y n/media/P90 del pico) | Corregir 03 o ampliar el CSV |
| 7 | Parámetros pendientes descritos como "tamaño, intervalo, desfase" | 03:166-170, Log (7) | Son proporción, demora, descarga y servicio (02:343) |
| 8 | "desactivar `modoDemo`" para producir | 03:226-227, 05:19 | La producción usa `modoFranjaPed = true` en `MainPeatonal` |
| 9 | El piloto de franja se pide con `PeatonalE0/E1` | 06:51, 05:47 | Esos experimentos terminan a los 900 s sin franja: darían `INCOMPLETO`. Usar un experimento de variación o el nuevo `PeatonalFranjaVisual` |
| 10 | Piloto de 480 peatones "hecho" | 06:21, 02:501 contra 03:187 y 06:33 | Se hizo con la geometría anterior; con el plano hipotético está pendiente |
| 11 | "Compilación 8.9.9 el 24/09" | 06:20, 03:158, 02:24 | El IDE ya era 8.9.10 ese día (02:6, Log (8)); el verificador compila contra jars 8.9.10 |
| 12 | Espera "desde el ingreso a `PedService`" | 02:303 | El código mide desde `onEnterQueue` (02:289-291) |
| 13 | La cohorte pico de `Main` figura como pendiente | 02:183 | Ya está implementada (`nPico`, `percentil90Pico`) |
| 14 | Checks del motor de `Main` "verificados" | 06:18 contra 02:195 | Verificados en el harness Java; en el IDE sólo arrancó E0 |
| 15 | Faltan experimentos en la lista | 02:212 | Falta `PeatonalFranjaPrueba` |
| 16 | El corte de E1 a 787 s no aparece | 03:194-200, Log (10) de `SIM.md` | Agregarlo |
| 17 | "Mínimo 30 pares con ampliación secuencial" | 03:219 contra la planilla, el cargador y el experimento fijos en 30 | T1.5 más §7.3 |
| 18 | "50 trenes" | 03:99, 06:23 | Con 60 s de demora entran 51 (el de las 06:59): aclarar "50 arribos en la franja; 51 ingresos" |
| 19 | E3 "medible en campo" | 01:116 contra 01:151 y `SIM.md` (sin medición presencial) | Corregir 01 |
| 20 | `SIM.md` desactualizado | Tabla de datasets ("⏳ medición en campo"), "conseguir horarios del Roca", "próximo hito 23/09" | Actualizar; los horarios ya están desde el 24/09 |
| 21 | Log de `SIM.md` con entradas del **2026-09-25** (Casermeiro) | `SIM.md`:2771-2788 | Hoy es 24/09 y los commits son del 24/09: corregir la fecha |
| 22 | "Tema aprobado el 20/09" contra "falta reenviar el formulario" | `SIM.md` §TPI | Confirmar (T7.4) |
| 23 | Fecha del informe 23/09 | 03:10 | Actualizar al generar el PDF |
| 24 | 10 pasos: la consigna usa la lista de Law; el TP 2025 y los parciales usan la de Weitz | Unidad 5 de `SIM.md` | El informe referencia la lista de la **consigna** |
| 25 | Formato del informe y de las diapositivas | 03 (`.md`) y pptx contra la consigna | F5 y F6 |

## 12. Lecciones del TP del hospital (TPI 2025 de otro grupo, mismos docentes)

El `.docx` no es el informe final: es el documento de trabajo del grupo, con pestañas de organización, 10 pasos, "Avance TPI 1/8", métricas, mejoras y guion. No tiene LaTeX, tablas de IC ni test.

**Adoptar:**

- en el Paso 1, objetivo general más objetivos específicos;
- métricas definidas con fórmula (por ejemplo, utilización = tiempo ocupado / tiempo total);
- el esquema "trabajo hecho / mejoras / próximos pasos" con capturas del modelo, si hay avances parciales (T7.5);
- llevar a clase "realidad, escenario base, alternativo y datos" antes de pedir el aval de los rangos (T0.1);
- reglas de cola y de abandono fijadas desde el principio. A ellos les costó corregir un supuesto de llamada perdida; a nosotros, las colas invertidas.

**No aplica o no copiar:**

- GIS, Road Traffic y el ejemplo Trauma Center: nosotros usamos la Pedestrian Library.
- Escenarios optimista y pesimista como eje: para nosotros son **contextos de sensibilidad**. El eje es E0 contra E1.
- 100 corridas independientes: los pares con números aleatorios comunes son más eficientes, y n se justifica con §7.3.
- Reparto del guion entre 7 oradores: somos dos, ~80 s cada uno.
- **Errores que no hay que repetir:**
  - sin test de medias (hoy es causal de recuperatorio);
  - resultados en "unidades de tiempo" y sin IC;
  - anunciar 4 escenarios y entregar 2 sin explicarlo;
  - guion al límite de 3 min sin marcar la demo de AnyLogic;
  - sin bibliografía;
  - usar los 10 pasos de Weitz en lugar de los de la consigna.

## 13. Riesgos y mitigaciones

| Riesgo | Prob. | Impacto | Mitigación |
|---|---|---|---|
| El IDE pisa el `.alp` con un autosave viejo | Media | Alto | Protocolo T1.1, commit antes y después, `git diff --stat` y verificador |
| Verificador frágil ante el formato 8.9.10 | Alta | Medio | T1.2 |
| El atasco peatonal persiste | Media | Alto | T2.2 (instrumentar), T2.6 (plan B de geometría) y la opción E de §6.1 |
| E1 corta sin causa (787 s) | Media | Alto | Consola visible (T2.1), memoria (T2.3) |
| T_run alto | Media | Medio | §6.1: paralelismo, dos máquinas, n por secuencial y recorte a la hora pico |
| Límite de 50.000 agentes acumulado entre corridas | Desconocida | Alto | T2.4 antes de producir; lanzamientos cortos |
| Distinto resultado entre máquinas | Baja | Medio | T1.3; si falla, todo en una máquina |
| Los organismos no responden | Alta | Bajo (con D2) | Rangos citables (§5); los pedidos siguen abiertos |
| La cátedra rechaza los rangos | Baja-media | Alto | Consultar ya (T0.1). Alternativa: sensibilidad más amplia o ajustar el alcance |
| E1 = 22 da "sin diferencia" | Media | Bajo | Resultado válido; E1-(b) como segundo alternativo si hay cómputo |
| El reparto parejo del modelo sobreestima E1 | Media | Medio | Declararlo; validación del reparto (§6.2) |
| Choque con el parcial de SIM | Media | Medio | Adelantar F1-F2 a S1 |
| Video > 3:00 o editado | Baja | Crítico | Guion ≤ 2:40, cronómetro, toma completa descartable |
| Plantilla LaTeX desconocida | Media | Bajo | Esqueleto genérico adaptable (§8.1) |
| Contradicciones entre documentos llegan al informe | Alta si no se hace T1.4 | Medio | T1.4 antes de T5.3 |
| Publicar trabajo ajeno (el `.docx` del hospital) en un repo público | Media | Medio | D8 |

## 14. Fuentes citables encontradas

Las verificadas se abrieron y leyeron en esta sesión, con consulta el 2026-09-24. Wikipedia está excluida.

**Verificadas:**

1. Subterráneos de Buenos Aires S.E. y Secretaría de Transporte y Obras Públicas (GCBA). (2026). *Subte: Viajes Molinetes* [conjunto de datos; pasajeros por molinete cada 15 min; CC-BY-2.5-AR; última actualización 03/09/2026]. Buenos Aires Data. https://data.buenosaires.gob.ar/dataset/subte-viajes-molinetes
2. Kittelson & Associates, Inc., Parsons Brinckerhoff, KFH Group, Inc., Texas A&M Transportation Institute y Arup. (2013). *Transit Capacity and Quality of Service Manual* (3.ª ed., TCRP Report 165). Transportation Research Board. Cap. 8, Exh. 8-12, p. 8-25 (tiempos de descenso por puerta); cap. 10, pp. 10-20, 10-21, 10-24/25, Exh. 10-27, pp. 10-42/43 (velocidad de marcha, escaleras y headways de molinetes). https://onlinepubs.trb.org/onlinepubs/tcrp/tcrp_rpt_165ch-10.pdf y https://onlinepubs.trb.org/onlinepubs/tcrp/tcrp_rpt_165ch-08.pdf
3. London Underground Limited. (2012). *Station Planning Standards and Guidelines* (SPSG, ed. 2012; versión redactada publicada por solicitud FOI-0523-2122). Transport for London. §3.3 (25 pax/min por molinete; vaciado en 2 min), §3.10 (capacidad de pasillos y escaleras), §5.1 (velocidades de evacuación). Las páginas son aproximadas por la extracción del PDF: verificar al citar. https://foi.tfl.gov.uk/FOI-0523-2122/SPSG%202012_Redacted.pdf
4. Comisión Nacional de Regulación del Transporte. (2025). *Informe estadístico anual 2024: Red ferroviaria AMBA* (IF-2025-36543746-APN-GFGF#CNRT). pp. 15, 30 y 31. https://www.argentina.gob.ar/sites/default/files/if-2025-36543746-apn-gfgfcnrt_-_informe_estadistico_amba_2024.pdf
5. Trenes Argentinos. (2026). *Horarios línea Roca, vigentes desde el 03/08/2026* [PDF oficiales en `datos/roca/`]. https://www.argentina.gob.ar/transporte/trenes-argentinos/horarios-tarifas-y-recorridos/areametropolitana/linearoca
6. Argentina.gob.ar. (2026). *El Tren Roca sumará 200 coches nuevos* [noticia; formaciones de 7 coches]. https://www.argentina.gob.ar/noticias/el-tren-roca-sumara-200-coches-nuevos
7. The AnyLogic Company. (2026). *AnyLogic Help: AnyLogic editions — Limitations in AnyLogic PLE; Parameter variation experiment* [ayuda offline 8.9.x]. https://anylogic.help/
8. Law, A. M. (2015). *Simulation Modeling and Analysis* (5.ª ed.). McGraw-Hill Education. Caps. 9-10, según la wiki (Unidades 9-10).

**No verificadas** (no citar hasta leerlas):

- Weidmann, U. (1993). *Transporttechnik der Fussgänger* (Schriftenreihe IVT Nr. 90). ETH Zürich. El PDF no abrió.
- Puong, A. (2000). *Dwell time model and analysis for the MBTA Red Line*. MIT. Sólo se leyó el resumen.
- Fruin, J. J. (1971). *Pedestrian Planning and Design*. Metropolitan Association of Urban Designers and Environmental Planners. No se consultó.

**Sin fuente encontrada:**

- proporción de pasajeros del Roca que transfieren a la Línea C;
- tiempo de validación EMV/QR;
- puertas por lado de los coches del Roca;
- plano de la estación.

Quedan como [SUP] o [PEND].

## 15. Qué no se pudo verificar en esta sesión

- Si la corrección de las colas resuelve el atasco (requiere el IDE: T2.1).
- La causa del corte de E1 a los 787 s: no quedaron el CSV ni el log del piloto.
- Si el límite de 50.000 agentes se acumula entre corridas (T2.4).
- Si las evaluaciones en paralelo funcionan de verdad en esta instalación de PLE. La ayuda no las excluye de PLE, pero no se probó.
- Que los IDs `LineaC_Constitucion_Turn*` (sin `_Plaza_`) sean el vestíbulo Principal: se infiere por el nombre y SBASE no lo documenta.
- El tiempo real de validación SUBE en Constitución y la espera y cola reales.
- Fechas, plantilla, avances y docentes 2026 (Classroom).
