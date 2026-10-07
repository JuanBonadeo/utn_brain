# TPI Caser — modelo en AnyLogic, Etapa 1 (horno con llegadas exógenas)

> Archivo: [`modelo/CaserHorno.alp`](modelo/CaserHorno.alp), formato **AnyLogic 8.9.9** (PLE, Process Modeling
> Library). Diseño: `05-respuestas-al-docente.md` §1-§5. Estado (2026-10-07): **verificado fuera del IDE,
> todavía no abierto en AnyLogic**. Las entradas son reales (agregadas); los resultados no están validados.

## 1. Protocolo con el IDE (igual que el grupo del subte)

1. Antes de abrir AnyLogic: `git status` limpio para el `.alp`. Si existe `CaserHorno.alp.autosave`,
   renombrarlo a `CaserHorno.alp.autosave.bak` (ignorado por Git).
2. Con el IDE abierto nadie edita el `.alp` desde afuera (ni Claude ni scripts). Claude edita el XML solo con el
   IDE cerrado.
3. Si el IDE ofrece restaurar un autosave, responder **No**.
4. Al cerrar: `git diff --stat` del `.alp`, correr el verificador (abajo) y commitear. Si el diff es inesperado,
   `git restore` y avisar.
5. El CSV de corridas se agrega al final: renombrarlo con fecha antes de relanzar el experimento.

`modelo/construir_modelo.py` generó la **primera** versión del `.alp`. Desde que se abra y guarde en el IDE, el
`.alp` es la fuente de verdad: el generador se niega a pisarlo salvo con `--forzar`.

## 2. Verificación fuera del IDE

Desde la raíz del repo (tarda ~10 s):

```sh
.venv/Scripts/python.exe -I materias/SIM/entregables/TPI/caser/modelo/verificar_modelo.py
```

Usa el JDK y las bibliotecas de `D:\AnyLogic 8.9 Personal Learning Edition` (o `ANYLOGIC_HOME`). No modifica el
modelo. Hace tres cosas, todas sobre el `.alp` tal como está:

1. **Estructura**: XML bien formado, Ids únicos, `source → colaHorno (Wait) → horno (Delay, capacidad 1) → sink`,
   experimentos que nombran todos los parámetros.
2. **Compilación contra la API instalada**: parámetros, variables, funciones, acciones de eventos y callbacks de
   los bloques, como subclase de `Agent` con `Source/Wait/Delay/Sink<Agent>` y `EventTimeout` reales.
3. **Ejecución de las mismas funciones** en un motor de eventos discretos mínimo que imita el cableado
   (`inject` → `colaHorno.onEnter`; `colaHorno.free` → `Delay` de capacidad 1 con el `delayTime` del `.alp` →
   `sink.onEnter`). Pruebas:
   - trazas exactas: umbral, calentamiento, vacío que se cancela con una llegada, enfriamiento, kWh y días de
     campaña;
   - modo `cupo` contra `workConserving`;
   - prioridad: enciende bajo el umbral y trata solo la urgente;
   - espera máxima, medida desde la ULI más vieja aunque haya llegado durante el enfriamiento;
   - conservación de ULI, límite de 50.000 agentes de la PLE, números aleatorios comunes (E0-E3 reciben
     exactamente las mismas ULI con la misma semilla), y resultado idéntico con desempate FIFO y LIFO de
     eventos simultáneos;
   - **caso degenerado M/M/1** (05- §4.1: umbral 1, calentamiento y enfriamiento 0, vacío 0, ciclo
     exponencial, llegadas Poisson λ = 0,7/h, μ = 1/h). Resultado:

     ```
                       configuración del IDE     largo (12.000 d × 5 semillas)   teoría
     Lq                    1,6146 (−1,15 %)          1,6319 (−0,09 %)            1,6333
     L                     2,3131 (−0,87 %)          2,3317 (−0,07 %)            2,3333
     W (h)                 3,3027 (−0,92 %)          3,3305 (−0,09 %)            3,3333
     Wq (h)                2,3053 (−1,20 %)          2,3309 (−0,11 %)            2,3333
     ρ                     0,6985 (−0,21 %)          0,6998 (−0,02 %)            0,7000
     ```

Además escribe `modelo/corridas_horno_harness.csv`: las 120 corridas de `CorridasE0E3` ejecutadas por el motor
mínimo. **No es un resultado del TPI**: es la referencia para comprobar que AnyLogic ejecuta la misma lógica
(ver §6).

## 3. Estructura del modelo

Unidad de tiempo: **hora**. `t = 0` es un lunes a las 00:00. Entidad: **ULI** (agente con `tLlegada`, `kg`,
`urgente`, `enCupo`, `despachado`, `tInicio`). Nunca la pieza.

```
eDia (cada 24 h) ─ nuevoDia(): lun-vie, ULI lavadas del día ─► eLlegada ─► source.inject(1)
source (inject) ─► colaHorno (Wait, ∞) ─► horno (Delay, capacidad 1, tiempoCiclo()) ─► sink
                    onEnter: entraCola()      la elige despachar() con free()          onEnter: finCiclo()
```

`colaHorno` es un `Wait`, no un `Queue`: la ULI sale solo cuando `despachar()` la libera con `free(uli)`. Así el
horno elige **cuál** carga (urgentes primero, después FIFO) y **si** carga (solo en `Procesando`). El despacho se
difiere con un evento de tiempo 0 (`eDespacho`) para no liberar una ULI desde el propio `onEnter` del bloque.

**Estado del horno** (variable `estado`; el statechart visual se agrega en el IDE, ver §7):

| `estado` | Nombre | Entra | Sale |
|---|---|---|---|
| 0 | Apagado | inicio; fin del enfriamiento | hay ULI en cola → Acumulando |
| 1 | Acumulando | primera ULI | cola ≥ `umbralULI` → Calentando; o una urgente en cola → Calentando (prioridad); o vence `esperaMaxDias` desde la ULI más vieja |
| 2 | Calentando | encendido | `hCalentamiento` (36 h) |
| 3 | Procesando (Cargando / Caliente en vacío) | fin del calentamiento | sin candidata: espera `horasEnVacio` (48 h); si llega una ULI, sigue cargando; si vence, Enfriando. Encendido por prioridad: trata solo las urgentes y enfría sin espera |
| 4 | Enfriando | fin de la campaña | `hEnfriamiento` (48 h) → Apagado |

**Regla de fin de campaña** — `modoFinCampana`:
- `workConserving` (**base**): carga mientras haya cola. **Confirmado por el encargado el 07/10/2026**
  ("las cargamos igual") y consistente con el registro (campañas largas de mediana 186 ULI).
- `cupo`: solo lo que estaba en cola al llegar a temperatura (más urgentes). Es la regla que se había
  anotado el 27/09; queda como alternativa, sin uso en los escenarios.

**Energía**: `kWh = kWhPorEncendido × encendidos + kWhPorDiaCaliente / 24 × horas en Procesando`. Es la misma
estructura que la regresión sobre las facturas (término por campaña + término por día activo); el calentamiento
está dentro del término por encendido.

## 4. Entradas

Generadas por `datos-locales/_perfil/entradas_etapa1.py` (gitignorado) desde `Seguimiento TR ulis`. En el `.alp`
quedan solo agregados.

| Parámetro | Valor | Origen |
|---|---|---|
| `llegadasSemanas` | 52 semanas reales × 5 días hábiles (ULI lavadas que van al horno, 18/08/2025-14/08/2026) | Bootstrap por **semanas completas**: cada lunes se sortea una de las 52. Conserva los días sin lavado (49 % de los hábiles), los picos de 10-20 ULI y la autocorrelación dentro de la semana (0,43). Media 33,6 ULI/semana = 4,8/día calendario. Hora de llegada uniforme entre las 6 y las 22 |
| `kgCuantiles` | 101 cuantiles de kg por ULI (media 140,9, mediana 131,6) | Mismas ULI; inversa de la distribución empírica |
| `umbralULI` | 75 | Relevado 70-80; cola al encender medida: mediana 77 |
| `minPorULI` | 1440/17 ≈ 85 min | Encargado. Medido en fines de semana (cola nunca vacía por llegadas): ≈ 99 min → sensibilidad |
| `horasEnVacio` | 48 h | Huecos de 1-2 días sin cementado dentro de campañas, imposibles con apagado y recalentado (≥ 84 h) |
| `hCalentamiento`, `hEnfriamiento` | 36 h, 48 h | Relevado |
| `pPrioridad` | 0,0095 | 17 encendidos chicos / 1.794 ULI llegadas con el horno apagado (2024-2026) |
| `soloUrgentesEnPrioridad` | `true` | Campañas chicas: encienden con 39 en cola y tratan 5 (decisión del 07/10) |
| `kWhPorDiaCaliente`, `kWhPorEncendido` | 2.445, 1.384 | Regresión de facturas (05- §2.3) |
| `tarifaKWh` | 290 $/kWh | Factura del horno, mar/2025 |
| `calentamientoModeloDias`, `horizonteDias` | 90, 365 | El calentamiento se fija con Welch en los pilotos (05- §5.1) |

Generadores: uno por fuente (`rngLlegadas`, `rngKg`, `rngUrgente`, `rngDemanda`, `rngCiclo`), sembrados con
`semilla × 10 + k`. Ninguno depende del estado del horno, así que con la misma semilla todos los escenarios
reciben exactamente las mismas ULI (números aleatorios comunes, 05- §5.3).

## 5. Experimentos

| Experimento | Qué hace |
|---|---|
| `Visual` | E0, semilla 1, con animación (escala 48 h/s). Para mirar el modelo y para el video |
| `VerificacionMM1` | Caso degenerado de §2 (2.400 días, ~42.000 ULI). La consola imprime `CSV_HORNO;MM1;...`: comparar `colaMediaULI` (Lq), `sistemaMedioULI` (L), `sistemaMedioHoras` (W), `esperaMediaDias`×24 (Wq) y `utilizacion` (ρ) con la tabla de §2 |
| `CorridasE0E3` | 120 corridas: `index / 30` = escenario, semilla `1 + index % 30`. Escribe `corridas_horno.csv` en la carpeta del modelo |

| Escenario | `umbralULI` | `esperaMaxDias` | `horasEnVacio` |
|---|---:|---:|---:|
| E0 base | 75 | ∞ | 48 |
| E1 umbral bajo | 45 | ∞ | 48 |
| E2 umbral + espera máxima | 75 | 15 | 48 |
| E3 mantener caliente | 75 | ∞ | 96 |

E3 se redefinió: la base ya mantiene el horno caliente 48 h (lo que muestra el registro), así que la alternativa
es mantenerlo el doble. Los valores 45, 15 y 96 son provisorios: se ajustan con las corridas piloto (paso 5).

Cada corrida escribe una fila con 33 campos (`encabezado()` en `Main`) y la imprime en consola con el prefijo
`CSV_HORNO`. El test de medias:

```sh
.venv/Scripts/python.exe -I materias/SIM/entregables/TPI/caser/modelo/analizar_corridas.py materias/SIM/entregables/TPI/caser/modelo/corridas_horno.csv
```

Primarias (Bonferroni, α = 0,05/3): kWh por kg, kg promedio en cola (producto inmovilizado antes del horno) y
espera media. Secundarias al 95 %: espera p90, campañas por mes, encendidos por prioridad, ULI por campaña,
fracción del tiempo a temperatura y $ de energía por kg. El nivel de servicio y el capital en pesos entran en la
Etapa 2.

## 6. Primera sesión en el IDE (checklist)

1. Abrir `CaserHorno.alp` en AnyLogic 8.9 PLE. **Build** (F7): tiene que compilar sin errores. Si hay errores,
   copiarlos tal cual.
2. Correr `VerificacionMM1` y pegar la línea `CSV_HORNO;MM1;...` de la consola.
3. Correr `Visual` un rato: el texto de estado tiene que pasar por Acumulando → Calentando → Cargando →
   Caliente en vacío → Enfriando, y la cola tiene que crecer de lunes a viernes.
4. Correr `CorridasE0E3` y después:
   ```sh
   .venv/Scripts/python.exe -I materias/SIM/entregables/TPI/caser/modelo/analizar_corridas.py materias/SIM/entregables/TPI/caser/modelo/corridas_horno.csv --comparar materias/SIM/entregables/TPI/caser/modelo/corridas_horno_harness.csv
   ```
   Tiene que decir que coinciden campo por campo. Si no coinciden, AnyLogic está ejecutando algo distinto de lo
   verificado (orden de eventos, comportamiento de `Wait.free`) y hay que encontrarlo antes de seguir.
5. Confirmar que 120 corridas seguidas no chocan con el límite de 50.000 agentes de la PLE (~2.200 por corrida).
6. Cerrar el IDE, `git diff --stat`, verificador, commit.

## 7. Statechart visual (lo agrega el grupo en el IDE)

La lógica vive en las funciones y en `estado`. Para que el statechart no duplique ni contradiga esa lógica, la
forma más segura es que **solo la refleje**: estados `Apagado`, `Acumulando`, `Calentando`, `Procesando` (con
`Cargando` y `CalienteEnVacio`) y `Enfriando`, con transiciones por **condición** sobre `estado` (y `enVacio`), por
ejemplo `estado == 2`. AnyLogic reevalúa esas condiciones después de cada evento del agente, así que el diagrama
sigue al horno sin decidir nada. Si se agrega, volver a correr el paso 4 de §6: el CSV no debe cambiar.

## 8. Limitaciones conocidas de esta etapa

- **Lavado y horno no son del todo independientes**: el 68 % de las ULI se lavan en días con el horno prendido,
  que son el 58 % de los días hábiles. Las llegadas exógenas ignoran ese acople.
- La autocorrelación entre semanas (órdenes de fabricación largas) no se conserva: cada semana se sortea
  independiente.
- `pPrioridad` se estimó con la cantidad de encendidos chicos, así que **esa métrica no sirve para validar**
  (calibrar no es validar). Se valida con ULI por campaña, duración, espera y kWh.
- Primera comparación con el registro, motor mínimo, E0 (no es validación formal): espera media ≈ 7 días contra
  10,2 del registro y p90 ≈ 15 contra 26; ULI por campaña ≈ 100 contra 164 de media. El registro mezcla
  2024-2025 (más volumen) con 2026, mientras que las llegadas son de los últimos 12 meses. Antes de validar hay
  que comparar contra el mismo período.
