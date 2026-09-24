---
codigo: SIM
materia: Simulación
tipo: Trabajo Práctico Integrador
titulo: Simulación de los molinetes de Constitución
subtitulo: Congestión transitoria por arribos en tandas en el vestíbulo Principal de la Línea C
comision: 401
grupo: Bonadeo - Estevez
etapa: Borrador técnico previo a calibración
fecha: 23/09/2026
alumnos:
  - Bonadeo, Juan Cruz | juancruzbonadeo04@gmail.com | 53533
  - Estevez, Matias |  | 53528
---

## 1. Introducción

Este trabajo estudia el ingreso al subte por la línea de molinetes del vestíbulo Principal de la
estación Constitución, Línea C, durante los días hábiles entre las 07:00 y las 09:30. El problema de
decisión es determinar si conviene habilitar todos los molinetes instalados y, en extensiones posteriores,
redistribuir parte del flujo hacia el vestíbulo Plaza o modificar el medio de validación.

El fenómeno no queda bien representado por una cola estacionaria alimentada por arribos individuales. La
estación recibe oleadas de pasajeros provenientes de las formaciones del Ferrocarril Roca: entre dos
oleadas la capacidad puede permanecer ociosa, mientras que inmediatamente después de un arribo se forma
una cola transitoria. Por este motivo se construyó en AnyLogic un modelo de eventos discretos y una capa
espacial con la Pedestrian Library.

El documento sigue los diez pasos de un estudio de simulación exigidos por la cátedra. La versión actual
documenta el caso, la implementación y la verificación. Los resultados de las demostraciones sintéticas no
se presentan como resultados del sistema real: la calibración y las corridas de producción requieren los
tiempos de servicio y la estructura de las tandas solicitados a los organismos responsables.

## 2. Paso 1 - Formulación del problema y planificación

El alcance se limita al vestíbulo Principal de Constitución. El sistema comienza cuando un pasajero llega
desde el entorno ferroviario a la zona de espera y finaliza cuando atraviesa el molinete y alcanza la salida
hacia la Línea C. No se modelan los andenes, el viaje en subte, la venta de tarjetas ni el flujo vespertino.

La pregunta principal es:

> ¿Cuánto cambia la espera de los pasajeros si durante el pico matutino se habilitan los 28 molinetes
> instalados en lugar de los aproximadamente 20 observados en operación?

El escenario actual E0 y la alternativa E1 forman la comparación obligatoria. E2 y E3 se mantienen como
extensiones condicionadas a la disponibilidad de datos.

**Tabla 1. Escenarios definidos**

| Escenario | Configuración | Estado |
|---|---|---|
| E0 | 20 molinetes, aproximación entera a los 19,5 activos promedio | Implementado |
| E1 | 28 molinetes habilitados | Implementado |
| E2 | Desvío de una fracción del flujo hacia Plaza | Implementado solo como alivio de Principal; falta el segundo circuito |
| E3 | Sustitución del servicio SUBE por EMV/QR | Implementado; falta medir el tiempo de servicio |

*Fuente: elaboración propia.*

Las medidas primarias son la espera media, el percentil 90 de la espera, la proporción que supera 30 s y
el tiempo de disipación de cada tanda. Como controles se utilizan el largo medio y máximo de cola, la
utilización por molinete, su dispersión y la conservación de pasajeros.

## 3. Paso 2 - Recolección de datos y definición del modelo

La fuente cuantitativa principal es el dataset *Subte - Viajes Molinetes* de BA Data. Se analizaron enero
a junio de 2026, con una fila por molinete y ventana de 15 minutos. El preprocesamiento normaliza el campo
horario, cuyo formato cambia entre meses, y elimina 11 feriados detectados por una caída del flujo diario
inferior al 50 % de la mediana. La muestra final contiene 117 días hábiles.

**Tabla 2. Perfil medio del vestíbulo Principal**

| Ventana | Pasajeros | Molinetes activos promedio |
|---|---:|---:|
| 07:00 | 1.437 | 19,5 |
| 07:15 | 1.578 | 19,5 |
| 07:30 | 1.765 | 19,5 |
| 07:45 | 1.824 | 19,5 |
| 08:00 | 1.799 | 19,5 |
| 08:15 | 2.054 | 19,5 |
| 08:30 | 2.066 | 19,5 |
| 08:45 | 1.742 | 19,5 |
| 09:00 | 1.581 | 19,5 |
| 09:15 | 1.636 | 19,5 |

*Fuente: elaboración propia sobre BA Data, 117 días hábiles de enero-junio de 2026.*

El total medio de la franja es 17.482 validaciones. El pico se concentra entre las 08:15 y las 08:45. El
vestíbulo Principal absorbe el 84,7 % del flujo de Constitución y Plaza el 15,3 %. Entre los molinetes se
observa un fuerte desbalance: Turn14 registra 1.485 pasajeros por día hábil en la franja, mientras Turn23
registra 129.

Los conteos representan validaciones efectivamente realizadas, no arribos ni esperas. Por ello no permiten
reconstruir por sí solos el tamaño y el intervalo de las tandas. Tampoco contienen tiempos de servicio. Los
parámetros pendientes se solicitaron a SBASE, Emova y Trenes Argentinos. Hasta obtenerlos, cualquier rango
utilizado debe declararse como supuesto y someterse a sensibilidad.

### 3.1 Modelo conceptual

Un agente representa un pasajero. En la capa lógica, un evento genera tandas y las inyecta en el circuito
`Source -> Queue -> Seize -> Delay -> Release -> Sink`. Los molinetes son recursos paralelos y la cola es
FIFO. La capa espacial utiliza `PedSource -> PedService -> PedGoTo -> PedSink`, 28 posiciones de servicio y
una línea física de salida.

La unidad de tiempo es el segundo. `t = 0` equivale a las 07:00, el pico corresponde a
`[4500, 6300)` y el cierre de arribos ocurre en `t = 9000`. La cohorte ingresada antes de las 09:30 se
drena completamente para no censurar esperas.

## 4. Paso 3 - Validación del modelo conceptual

La definición del caso, el alcance y los escenarios fueron presentados al docente y el tema fue aprobado el
20/09/2026. La validación conceptual pendiente consiste en confirmar con personal operativo:

- si los 28 registros corresponden a puestos utilizables para ingreso en Principal;
- si la cola puede representarse como una única fila con servidores intercambiables;
- la cola existente a las 07:00;
- la proporción de pasajeros del Roca que se dirige a la Línea C;
- la factibilidad operativa del desvío hacia Plaza.

Hasta completar esa revisión, el modelo se considera un prototipo verificable pero no validado.

## 5. Paso 4 - Construcción y verificación del programa

El modelo `SubteConstitucion.alp` fue construido para AnyLogic 8.9.9 PLE. La capa lógica implementa E0-E3,
el corte de arribos, el drenaje posterior, la conservación de pasajeros y las medidas primarias. La capa
peatonal mantiene la misma demanda y semilla para E0 y E1 y cambia solamente la cantidad de servicios
habilitados.

La verificación automatizada controla XML, identificadores, conexiones, parámetros de experimentos y
compilación de las funciones Java contra las bibliotecas instaladas. Una traza de cinco pasajeros, dos
servidores y 3 s de servicio produce esperas `0, 0, 3, 3, 6`, espera media 2,4 s, P90 de 6 s, cola máxima
3, área de cola 12 pasajero-s y ocupación 15 molinete-s.

La capa peatonal registra las esperas individuales, P90, proporción sobre 30 s, cohorte pico y ocupación
por puesto. Los callbacks de inicio y fin de servicio identifican el molinete utilizado; las ocho
posiciones finales se suspenden en PeatonalE0 y se habilitan en PeatonalE1.

El 2026-09-24 se recompiló el modelo completo en AnyLogic 8.9.9 y se ejecutaron `PeatonalE0` y
`PeatonalE1`. La primera prueba mostró que el corte fijo de 600 s dejaba peatones dentro del circuito. Se
amplió el final de ambos experimentos a 900 s. La implementación final separa el corte de métricas a 600 s
del cierre técnico a 900 s: congela throughput, $L_q$ y ocupación dentro de la ventana, pero mantiene el
conteo total hasta vaciar el circuito.
La repetición terminó en ambos casos con 480 generados, 480 procesados y cola cero. Los valores de espera
de esta prueba no se usan como resultados por provenir de datos y geometría sintéticos.

## 6. Paso 5 - Ejecuciones piloto

El modo demostración utiliza seis tandas de 80 pasajeros, separadas por 30 s, con 3 s de servicio. Estos
valores fuerzan una cola visible y permiten revisar el movimiento, pero no son estimaciones de
Constitución. Cada salida debe conservar el rótulo `DEMO PEATONAL SINTETICA`.

Antes de las corridas de producción se consideran los siguientes pilotos:

1. Traza determinística de cinco pasajeros y dos molinetes, comparada con el cálculo manual.
2. PeatonalE0 y PeatonalE1 con igual semilla, comprobando 20 y 28 puestos habilitados. **Completado:** ambos
   drenan los 480 peatones sin pérdida al extender el cierre técnico a 900 s.
3. E2 con desvio 0 y 1, comprobando los extremos de conservación.
4. Servicio que cruza las 09:30, verificando que quede pendiente al cierre y atendido en el drenaje.

## 7. Paso 6 - Validación del modelo programado

La validación posible con los datos actuales se limita al caudal agregado por ventana de 15 minutos y a la
distribución de validaciones entre molinetes. No puede validarse la espera ni el largo de cola porque no hay
observaciones publicadas de esas variables.

Se reservarán ventanas o días no utilizados en la calibración y se comparará el throughput simulado con
el observado. La validación de espera requerirá datos de campo, video o juicio experto documentado. Si esos
datos no se obtienen, las conclusiones se formularán condicionalmente a los rangos de entrada y no como una
descripción del desempeño real.

## 8. Paso 7 - Diseño de experimentos

El sistema es terminal: cada réplica representa la franja 07:00-09:30 y luego drena la cohorte. No se
aplica calentamiento arbitrario. E0 y E1 utilizarán las mismas entradas y semillas dentro de cada par de
réplicas para reducir la varianza de la diferencia.

El diseño definitivo tendrá como mínimo 30 pares de réplicas. El número final se ampliará mediante el
procedimiento secuencial visto en la Unidad 9 hasta alcanzar la precisión relativa acordada. Los factores
de sensibilidad son el tamaño de tanda, el intervalo entre tandas, el tiempo de servicio, la proporción de
transferencia desde el Roca y la cantidad de molinetes efectivamente disponibles.

## 9. Paso 8 - Corridas de producción

Las corridas de producción comenzarán solamente cuando se reemplacen los valores `-1` de los parámetros
operativos y se desactive `modoDemo`. Por cada réplica se exportarán:

- escenario y semilla;
- pasajeros generados, desviados, procesados a las 09:30 y procesados con drenaje;
- espera media, P90 y proporción sobre 30 s;
- Lq, cola máxima y tiempo de disipación;
- utilización media, utilización por molinete y dispersión;
- las mismas medidas restringidas a la cohorte 08:15-08:45.

No se completará esta sección con resultados de la demostración sintética.

La planilla [`04-resultados-corridas.xlsx`](04-resultados-corridas.xlsx) deja preparado el registro de los
30 pares iniciales. Cada fila conserva una semilla común para E0 y E1, calcula la diferencia `E1 - E0` y
separa las entradas de producción de las columnas calculadas. La hoja `Resumen` permanece en estado
`Sin corridas cargadas` hasta recibir resultados calibrados.

## 10. Paso 9 - Análisis de los datos de salida

La comparación principal será apareada. Para cada par se calculará

$$D_i = X_{i,E1} - X_{i,E0}$$

y el intervalo de confianza del 95 % para la diferencia media:

$$\bar D \pm t_{n-1,0.975}\frac{S_D}{\sqrt{n}}.$$

La regla de decisión es recomendar E1 cuando reduzca el P90 de espera y el intervalo de la diferencia no
contenga cero, sin degradar el throughput. Si el intervalo contiene cero, se informará que no existe
evidencia suficiente de una mejora. Para analizar simultáneamente varias medidas se ajustará el nivel de
confianza mediante Bonferroni.

Las proporciones sobre 30 s se analizarán sobre las estimaciones por réplica. Los percentiles se calcularán
primero dentro de cada réplica; esas salidas, y no las esperas individuales agrupadas entre réplicas, serán
las observaciones del test.

Para el diseño inicial de 30 pares, la planilla usa 29 grados de libertad. Aplica el intervalo bilateral del
95 % a las medidas descriptivas y Bonferroni sobre tres comparaciones primarias: procesados con drenaje,
P90 de espera y proporción con espera mayor a 30 s. Los valores críticos y las conclusiones se habilitan
recién al completar los 30 pares, evitando interpretar pilotos incompletos como resultados finales.

## 11. Paso 10 - Documentación, presentación y uso de resultados

El repositorio conserva la definición del caso, el modelo AnyLogic, la guía técnica y un verificador
reproducible. La presentación final incluirá un extracto del modelo peatonal en ejecución, una comparación
visual E0-E1 y una conclusión limitada a la evidencia estadística obtenida.

El video tendrá una duración máxima de tres minutos y mostrará a ambos integrantes. No se utilizará la
animación como evidencia cuantitativa: los resultados provendrán de las corridas exportadas. El guion
cronometrado y sus campos pendientes están en [`05-guion-video.md`](05-guion-video.md).

## 12. Conclusiones preliminares y trabajo pendiente

La evidencia disponible justifica el uso de simulación: Constitución concentra el mayor flujo de la red y
combina una utilización promedio moderada con arribos ferroviarios en tandas. El modelo implementa el caso
base y las alternativas, conserva pasajeros y mide la congestión transitoria sin censurar el drenaje.

Todavía no existe evidencia para recomendar una configuración. Faltan calibrar el tiempo de servicio y la
estructura de las oleadas, validar la geometría y ejecutar las réplicas. E2 tampoco puede interpretarse
para toda la estación hasta modelar Plaza como un segundo circuito con su flujo propio.

## 13. Referencias bibliográficas

Buenos Aires Ciudad. (2026). *Subte - Viajes Molinetes*. BA Data.
https://data.buenosaires.gob.ar/dataset/subte-viajes-molinetes

AnyLogic. (2026). *AnyLogic Help: Pedestrian Library y Process Modeling Library*. The AnyLogic Company.
https://anylogic.help/

Law, A. M. (2015). *Simulation Modeling and Analysis* (5.a ed.). McGraw-Hill.

Universidad Tecnológica Nacional. (2026). *Trabajo Práctico Integrador - Simulación: aplicación de
técnicas de simulación a un caso real*. Consigna de cátedra.

## 14. Anexos

- Definición y perfilado del caso: `01-definicion-del-caso.md`.
- Guía técnica y supuestos del modelo: `02-modelo-anylogic.md`.
- Modelo: `SubteConstitucion.alp`.
- Verificador: `verificar_modelo.py`.
- Script de perfilado: `scripts/sbase-perfil.py`.
- Checklist operativo y esquema de salida: `06-checklist-cierre.md`.
- Presentación editable del video: `TPI_Subte_Presentacion.pptx`.
