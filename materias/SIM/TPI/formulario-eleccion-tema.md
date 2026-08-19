# TPI Simulación — Propuesta de tema

> Primera actividad del TP Integrador (ver [SIM.md](../SIM.md) §3 — Unidad 3).
> Versión entregable en Word: [`TPI_Simulacion_Propuesta_de_Tema.docx`](TPI_Simulacion_Propuesta_de_Tema.docx) (carátula y estilos heredados de los informes de RD).
> La prioridad se asigna **por fecha de entrega del formulario**: conviene mandarlo temprano.
> El docente confirma la viabilidad o pide reformulación. **No arrancar el modelado antes de esa confirmación.**

> ⚠️ El enunciado pide **tres** temas candidatos y acá van **dos**, por decisión propia. Ver nota al pie.

---

## Datos del grupo

| Integrante | Legajo |
|---|---|
| Juan Cruz Bonadeo | 53533 |
| Matias Estevez | 53528 |

Comisión 403 — Facultad Regional Rosario (heredado del formato de RD; confirmar que aplique a Simulación).

---

## Tema 1 — Ecobici (opción prioritaria)

**Tema:**

> Simulación del sistema de bicicletas públicas Ecobici de la Ciudad de Buenos Aires, acotada al corredor Constitución/Retiro–Catalinas/Puerto Madero, para evaluar el efecto de una política de rebalanceo en hora pico sobre la disponibilidad de bicicletas y de anclajes libres.

**Observaciones:**

> Elegimos este tema porque los datos ya están verificados y son de acceso público: el Gobierno de la Ciudad publica los recorridos realizados de 2024 con 3.559.284 viajes individuales, cada uno con estación de origen y destino y marcas de tiempo de retiro y devolución, y la capacidad de anclajes de las 394 estaciones se obtiene del feed GBFS del operador. Sobre esos datos ya cuantificamos el fenómeno a mejorar: en días hábiles, las estaciones de las terminales ferroviarias pierden bicicletas netas entre las 7 y las 10 h mientras las del área de oficinas se saturan (la estación Madero Office recibe unas 14,5 bicicletas netas por día sobre 28 anclajes), y el patrón se revierte por la tarde. La hipótesis de mejora es concreta y evaluable como escenario alternativo: incorporar un camión de rebalanceo en la ventana matutina, o redistribuir anclajes entre estaciones del corredor. El alcance se acota a unas 12 estaciones, lo que preserva el fenómeno sin extender el estudio a las 394 estaciones del sistema.

---

## Tema 2 — Despacho de emergencias

**Tema:**

> Simulación del despacho de unidades de emergencia médica y de bomberos de la ciudad de San Francisco, para evaluar el efecto de incorporar una unidad adicional o modificar la política de asignación sobre el tiempo de respuesta a los incidentes.

**Observaciones:**

> El conjunto de datos abierto del Departamento de Bomberos de San Francisco contiene 7.386.640 registros de unidades despachadas, con la cadena completa de marcas de tiempo de cada llamado: recepción, despacho, salida, llegada a escena y liberación de la unidad. Eso permite ajustar tanto la tasa de arribos como los tiempos de servicio a partir de datos reales y, además, el intervalo entre la recepción del llamado y el despacho es el tiempo de espera en cola medido sobre el sistema real, lo que aporta un punto de validación directo para el modelo programado. La demanda es marcadamente no homogénea (de 9 a 27 llamados por hora según la franja horaria) y los tiempos de servicio son fuertemente asimétricos (mediana de 16,6 minutos y percentil 90 de 95,7 minutos). Como medida de salida se emplearía el percentil 90 del tiempo de respuesta contra el umbral de 8 minutos de la norma NFPA 1710, lo que aporta un criterio externo para la recomendación final.

---

## Anexo — respaldo técnico

Verificación de los cuatro criterios de selección del enunciado (§5):

| Criterio | Tema 1 — Ecobici | Tema 2 — Emergencias |
|---|---|---|
| **1. Aleatoriedad relevante** | Arribos por estación, destino y duración del viaje. Ratio pico/valle 22:1 | Arribos por franja y barrio, servicio asimétrico. Ratio 3:1 |
| **2. Datos disponibles** | ✅ Verificado: 3,56 M viajes + capacidad de 394 estaciones | ✅ Verificado: 7,39 M registros con cadena completa de timestamps |
| **3. Hipótesis de mejora** | Camión de rebalanceo / redistribución de anclajes | Unidad adicional / cambio de política de despacho |
| **4. Alcance acotable** | ⚠️ Acotar a ~12 estaciones del corredor | ✅ Un batallón o distrito |
| **Originalidad / aplicabilidad** | Alta — caso local, sistema en operación | Media — caso no local |

### Fuentes de datos

| Dataset | Origen | Estado |
|---|---|---|
| Recorridos realizados 2024 (3.559.284 viajes) | [Buenos Aires Data — Bicicletas Públicas](https://data.buenosaires.gob.ar/dataset/bicicletas-publicas) | ✅ Descargado y perfilado |
| Capacidad de estaciones (394, 7.304 anclajes) | Feed GBFS del operador — `station_information` | ✅ Descargado. Los CSV de estaciones del portal **no** traen capacidad |
| Fire Dept. & EMS Dispatched Calls (7.386.640 filas) | [DataSF — `nuek-vuh3`](https://data.sfgov.org/Public-Safety/Fire-Department-and-Emergency-Medical-Services-Dis/nuek-vuh3) | ✅ Muestra de una semana descargada y perfilada |

### Limitaciones conocidas a declarar en el informe

**Tema 1 (Ecobici):**
- El archivo registra únicamente viajes exitosos. No existe registro de "llegué y no había bicicleta / no había anclaje libre" — esa tasa de falla es la **salida** del modelo, no un dato contra el cual validar. La validación se hace contra los flujos observados (viajes por hora y por estación) y la distribución de duraciones.
- 9,11% de los viajes duran menos de 1 minuto y 13,47% tienen origen igual a destino (se superponen): firma del retiro fallido por bicicleta en mal estado. Hay que filtrarlos con criterio explícito o se infla la demanda ~10%.
- Duraciones atípicas: percentil 99 en 99 min pero máximo de 42.853 min (29 días). Truncar con criterio justificado.
- La capacidad del feed GBFS es el estado **actual**, no el de 2024. Declarar como supuesto.

**Tema 2 (Emergencias):**
- Cada fila es una unidad despachada, no un llamado: ~2 unidades por incidente (6.833 filas para 3.321 llamados en la muestra). El modelo debe contemplar que un arribo toma varios recursos simultáneos de tipos distintos (ENGINE + MEDIC).

### Nota sobre la cantidad de temas

El enunciado (§6) pide **tres** temas candidatos. Se presentan dos por decisión del grupo. El riesgo concreto es que el docente pida reformular o completar la propuesta, lo que costaría posiciones en la prioridad por fecha de entrega. Si conviene sumar un tercero, el candidato relevado es la simulación del flujo de pasajeros en los molinetes de una estación de subte de Buenos Aires: [SBASE publica pasajeros por molinete en rangos de 15 minutos](https://data.buenosaires.gob.ar/dataset/subte-viajes-molinetes) con serie hasta 2025, pero el tiempo de servicio del molinete no está en los datos y habría que medirlo en campo.

### Advertencia operativa

Los archivos de datos (ZIP de 168 MB, CSV de 765 MB) **no deben commitearse** a este repositorio. Mantenerlos fuera del árbol o agregarlos al `.gitignore`.
