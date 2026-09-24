---
title: "Checklist de cierre - TPI Subte Constitución"
subject: "Simulación"
status: "Operativo; bloqueado en calibración externa"
---

# Checklist de cierre

Este archivo separa lo terminado de lo que depende de datos o decisiones externas. Una tarea no se marca
como completa por haber funcionado con la demostración sintética.

## Estado actual

| Bloque | Estado | Evidencia o condición de cierre |
|---|---|---|
| Tema, alcance y escenario base | Hecho | Vestíbulo Principal, días hábiles 07:00-09:30, E0 contra E1 |
| Perfilado de SBASE | Hecho | 117 días hábiles y diez ventanas de 15 minutos reproducibles con `scripts/sbase-perfil.py` |
| Modelo lógico E0-E3 | Hecho como prototipo | Conservación, cierre 09:30, drenaje y métricas verificados |
| Capa peatonal E0-E1 | Hecho como prototipo | 28 puestos, configuración 20/28, misma semilla y salida `CSV_PEATONAL` |
| Compilación AnyLogic 8.9.9 | Hecho | Build correcto el 2026-09-24 |
| Piloto espacial E0-E1 | Hecho | Ambos escenarios drenaron 480 de 480 peatones y terminaron con cola cero |
| Extensión peatonal a 07:00-09:30 | Preparada | `modoFranjaPed`, corte a 09:30, drenaje, cohorte pico y conservación; entradas en `-1` bloquean la corrida |
| Demanda por horario del Roca | Hecha | 50 trenes hábiles 07:00-09:30 extraídos de los PDF oficiales; descarga escalonada, acceso de calle Poisson, servicio triangular y control de caudal por ventana |
| Automatización de 30 pares | Preparada | `PeatonalCorridasApareadas` escribe `corridas_peatonales.csv`; `cargar_corridas.py` valida y carga la planilla |
| Build con la extensión | Hecho | El IDE regeneró y compiló el modelo el 2026-09-24; `PeatonalCorridasApareadas` terminó en t = 0 sin pasajeros, consistente con el bloqueo por calibración |
| Piloto de franja completa (valores de prueba) | Ejecutado con hallazgos | E0 no drenó por un atasco de colas (corregido: colas invertidas); una corrida tardó ~43 min; E1 se cortó a 787 s |
| Piloto corto `PeatonalFranjaPrueba` (07:00-07:30) | Pendiente | Confirmar drenaje, esperas razonables y tiempo de cómputo tras invertir las colas |
| Piloto demo de la cadena automatizada | Pendiente | Ejecutar `PeatonalCorridasDemo` y validar `corridas_peatonales_demo.csv` con `cargar_corridas.py --demo` |
| Planilla estadística | Hecho | 30 pares, diferencias E1-E0, intervalos y Bonferroni; entradas reales todavía vacías |
| Guion de video | Hecho como plantilla | Duración objetivo 2:45; faltan resultados y conclusión |
| Presentación del video | Hecha como plantilla | Seis diapositivas editables; faltan resultados y conclusión |
| Plano hipotético | Hecho como supuesto | Vestíbulo 70 × 34 m con paredes, 28 molinetes lineales orientados hacia la zona paga, una cola por molinete; el IDE lo carga sin errores |
| Piloto visual del plano hipotético | Pendiente | Build y `PeatonalE0`/`PeatonalE1` en el IDE: comprobar sentido de paso, colas y drenaje de 480 peatones |
| Plano y geometría real | Bloqueado | Esperar respuesta de SBASE/Emova o conseguir un croquis verificable |
| Tiempo de servicio | Bloqueado | Esperar medición o rango aprobado por la cátedra |
| Horarios del Roca | Hecho con dato oficial | Horarios vigentes desde el 03/08/2026; falta la carga real por tren |
| Proporción Roca/calle, demora y descarga | Bloqueado | Esperar datos de transferencia o rangos aprobados por la cátedra |
| Validación de espera y cola | Bloqueado | Requiere observación, video o juicio experto documentado |
| E2 completo | Pendiente no prioritario | Modelar Plaza como segundo circuito solo si entra en el alcance final |
| E3 calibrado | Pendiente no prioritario | Requiere tiempo de validación SUBE y EMV/QR medido |

## Al recibir los datos

1. Guardar el original recibido sin modificar y registrar fecha, organismo y alcance.
2. Confirmar con la cátedra qué valores son mediciones y cuáles serán rangos de sensibilidad.
3. Reemplazar el plano hipotético y los parámetros sintéticos; mantener visible la versión y la fuente.
4. Completar en `MainPeatonal` `proporcionRocaPed`, `demoraAccesoRocaSeg`, `duracionDescargaSeg` y
   `servicioPedSeg` (y, si se aprueba un rango, `servicioMinPedSeg`/`servicioMaxPedSeg`). El horario del
   Roca, el perfil SBASE, los 9000 s de ingresos y el drenaje ya están implementados. Si se publica un
   horario nuevo, volver a correr `python3 datos/extraer_arribos_roca.py` y actualizar `llegadasRocaSeg`.
5. Ejecutar un piloto `PeatonalE0`/`PeatonalE1` con `modoFranjaPed = true` y controlar balance, cierre a las
   09:30, cohorte pico y drenaje antes de producir resultados.
6. Ejecutar `PeatonalCorridasApareadas`: 30 pares E0-E1, semilla común dentro de cada par y distinta entre
   pares (20260923-20260952).
7. Validar y cargar con `python3 cargar_corridas.py corridas_peatonales.csv` y luego `--escribir`; revisar
   la hoja `Resumen`.
8. Completar resultados, discusión y conclusión de `03-informe-tpi.md`.
9. Reemplazar los campos entre corchetes de `05-guion-video.md` y `TPI_Subte_Presentacion.pptx`, y ensayar.

## Control de cada par de corridas

- E0 y E1 usan la misma semilla, demanda, tiempos de servicio y geometría.
- La única diferencia del par es `molinetesOperativosPed`: 20 en E0 y 28 en E1.
- `generados = procesados con drenaje + desviados`; para E0-E1, desviados debe ser cero.
- El experimento continúa hasta que la cohorte generada antes del corte abandona el sistema.
- Cada corrida produce exactamente una fila `CSV_PEATONAL`; ninguna queda como `CSV_PEATONAL_INCOMPLETO`.
- No se mezclan filas `CSV_PEATONAL_DEMO` con las corridas de producción (el cargador lo impide).

## Esquema de `CSV_PEATONAL`

La línea tiene uno de tres prefijos: `CSV_PEATONAL;` (franja, cargable), `CSV_PEATONAL_DEMO;`
(demostración sintética, nunca va a la planilla oficial) o `CSV_PEATONAL_INCOMPLETO;` (corrida sin drenar,
bloquea la carga). Después siguen estos campos, en el orden que `cargar_corridas.py` comprueba contra los
encabezados de la hoja `Corridas`:

| Posición | Campo | Columna correspondiente de la planilla |
|---:|---|---|
| 1 | Escenario | determina si se carga en E0 o E1 |
| 2 | Semilla | Semilla |
| 3 | Pasajeros generados | Pasajeros generados |
| 4 | Pasajeros desviados | Pasajeros desviados; vale 0 en E0-E1 |
| 5 | Procesados al horizonte | Procesados a las 09:30 en producción |
| 6 | Procesados con drenaje | Procesados con drenaje |
| 7 | Espera media | Espera media |
| 8 | P90 de espera | P90 de espera |
| 9 | Proporción sobre 30 s | Proporción con espera mayor a 30 s |
| 10 | Lq | Lq |
| 11 | Cola máxima | Cola máxima |
| 12 | Tiempo de disipación | Tiempo de disipación |
| 13 | Utilización media | Utilización media |
| 14 | Dispersión de utilización | Dispersión de utilización |
| 15 | Pasajeros de cohorte pico | Pasajeros de la cohorte pico |
| 16 | Espera media de cohorte pico | Espera media de la cohorte pico |
| 17 | P90 de cohorte pico | P90 de la cohorte pico |

En la demostración, el campo 5 corresponde al segundo 600. Solo puede llamarse “procesados a las 09:30”
cuando la corrida usa `modoFranjaPed = true` con un horizonte de arribos de 9000 s. Las proporciones y
utilizaciones se exportan como fracción entre 0 y 1; la planilla las muestra con formato de porcentaje.

## Verificación reproducible

Desde la raíz del repositorio:

```bash
python3 materias/SIM/entregables/TPI/subte/verificar_modelo.py
```

Después se abre `SubteConstitucion.alp` en AnyLogic 8.9.9, se ejecuta **Build model** y se realizan los
pilotos indicados. El verificador estático no reemplaza la ejecución del motor.

## Cierre administrativo

- [ ] Completar los formularios web que se dejaron expresamente como pendientes y guardar comprobantes.
- [ ] Registrar número de trámite y fecha de seguimiento de cada organismo.
- [ ] Confirmar fecha de entrega y presentación en Classroom.
- [ ] Confirmar si la carátula debe incluir docentes y si se reutiliza la plantilla LaTeX.
- [ ] Incorporar el correo de Matías únicamente con su confirmación.
- [ ] Exportar la versión final del informe al formato exigido por la cátedra.
- [ ] Subir el video como oculto y probar el enlace desde una sesión sin permisos especiales.
